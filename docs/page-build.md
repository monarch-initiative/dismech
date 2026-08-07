# Page Build: Full vs Incremental

The `generate-pages` workflow renders the browsable HTML under `pages/` (one page
per disorder, comorbidity, and module, plus index and classification pages) and
the derived browser data, pathographs, dashboards, and schema docs. Rendering
every disorder page is the bulk of the work — there are ~1,500 of them — so on a
push the workflow renders **only what changed** when it safely can, and falls
back to a **full** rebuild when a change could affect every page.

## How the mode is decided

A push's changed files are classified by
[`scripts/classify_page_build.py`](https://github.com/monarch-initiative/dismech/blob/main/scripts/classify_page_build.py)
into one of two modes:

- **`full`** — re-render every page. Chosen when a change could alter any page's
  HTML: anything under `src/**` (the renderer, templates including the CSS
  partial, the schema, the graph/export code), `conf/**`, or `project.justfile`.
  Also chosen for deletions/renames of a page input, for scheduled and manual
  runs, and — by design — for **any path the classifier does not recognize**
  (fail-safe: never silently under-build).
- **`incremental`** — render only the changed `kb/disorders/*.yaml` pages. Chosen
  when the changes are limited to page inputs (disorder / comorbidity / module
  YAML, research reports) and render-neutral companions (`references_cache/**`,
  `history/**`, `cache/**`, `docs/**`, derived outputs, …). The common curation
  PR — a disorder edit plus its cached references and a history record — is
  incremental.

The classifier writes the changed disorder paths to a file, and the workflow
runs `just gen-pages-changed-from <file>` (which calls
`python -m dismech.render --changed-from <file>`).

## What incremental always regenerates

Even in incremental mode, the cheap disorder-**dependent** aggregate pages are
regenerated so anything that lists disorders stays current: the comorbidity,
module, and classification pages and their indexes, plus the browser data,
pathographs, dashboard, and schema docs. The expensive research index/report
pass is skipped unless a `research/*.md` file actually changed, since it is
essentially independent of disorder edits.

Incremental output is byte-identical to what a full build would have produced for
the changed pages; only the unchanged disorder pages are left untouched.

## The full-rebuild backstop

Because an incremental build does not re-render *other* disorders, a change to a
disorder's display name could in principle leave a stale cross-link on another
disorder's page until that page is next rendered. A **daily scheduled run** does
a full rebuild to heal any such drift, and a manual `workflow_dispatch` run is
always full as well.

## Page/KB drift and the dead-link gate

The daily backstop alone was not enough. An incremental render is scoped to a
single push's `event.before..sha` range, but the workflow's concurrency group
uses `cancel-in-progress: false`, so **queued runs collapse**: only the newest
pending run survives, and its range covers only its own push. Disorder YAMLs
belonging to the collapsed pushes are never rendered at all — while `app/data.js`
is *always* rebuilt from the whole KB. The browser index then lists disorders
whose `page_url` 404s. [PR #7903](https://github.com/monarch-initiative/dismech/pull/7903)
published 205 such dead links (1,826 KB entries vs. 1,621 rendered pages).

Two mechanisms now close that gap:

1. **Self-healing escalation.** After an incremental render, the workflow runs
   `classify_page_build.py --check-page-drift`, which compares the KB with the
   rendered pages on two axes:

   - **Count.** The number of `kb/disorders/*.yaml` inputs against the number of
     `pages/disorders/*.html` files. They are 1:1 in a healthy tree (page
     filenames are `slugify(disease name).html`, and slugs are unique), so any
     inequality means an earlier build under- or over-rendered.
   - **Content.** Every page is stamped with `sha256(source yaml)[:12]` — the
     renderer computes it for the OpenScientist panel and the template emits it
     as `yamlRevision` — so comparing that stamp against a fresh digest of the
     file says whether a page is *current*, not merely *present*.

   The check runs *after* rendering on purpose — before it, every
   disorder-adding push looks drifted and would escalate.

   The content axis was added after the count axis proved blind to the more
   common failure. A build's checkout is a snapshot and a full build takes
   30–60 minutes, so a KB merge landing mid-build is simply absent from it; the
   resulting page keeps older content while the file counts stay perfectly
   equal. Worse, it does not heal: the `auto/generate-pages` branch is rebuilt
   from `main`'s already-stale pages on every run and force-pushed, so a
   12-minute incremental build silently overwrote a 32-minute full rebuild that
   had just corrected 29 pages. On 2026-08-07 that left the whole
   [#8085](https://github.com/monarch-initiative/dismech/issues/8085)
   environmental-pathograph backfill invisible on the site with 1,871 YAMLs and
   1,871 pages — zero count drift. See
   [#8033](https://github.com/monarch-initiative/dismech/issues/8033) and
   [PR #8140](https://github.com/monarch-initiative/dismech/pull/8140).

   **Repair is proportional.** Pure staleness — the counts already agree and
   re-rendering the drifted entries would land on exactly the stale pages — is
   healed by rendering only those (measured: 1m28s for 29) rather than everything
   (~30–60 min); the checker writes that worklist with `--stale-files-out` and
   reports `heal=targeted`. A count mismatch, or an orphan page left by a
   rename, reports `heal=full`, because only a full build prunes. A targeted
   heal is re-checked afterwards and falls back to a full rebuild if drift
   survives. Without the cheap path, a repo whose merges outpace a full build
   would sit in permanent full-rebuild mode.
2. **A hard gate before publishing.** After `just gen-browser-data`, the workflow
   runs [`just check-browser-links`](https://github.com/monarch-initiative/dismech/blob/main/scripts/check_browser_data_links.py),
   which resolves every `page_url` in `window.searchData` against the filesystem
   and **fails the job** if any target is missing. The drift check escalates and
   repairs; this one refuses to publish, and it is checking a different thing —
   the links `data.js` actually emits, rather than the KB/page correspondence.

The gate also catches a second, sneakier shape: a page that renders perfectly on
the build machine but is dropped from the commit by `.gitignore`, and so never
reaches the published site. That is a *permanent* dead link, invisible to both an
on-disk existence check and a count comparison — the file is right there on the
runner. `pages/disorders/Holt-Oram_syndrome.html` had sat in the `.gitignore`
"Local files" block since it was added, so that disorder was published in the
browser index with no page behind it on every single build. `git check-ignore`
reports ignored **and untracked** paths, which is exactly the failing set
(a committed page matching an ignore pattern is correctly not flagged).

Run the gate locally against a build with `just check-browser-links`.

**Never add a `pages/` path to `.gitignore`.** If a rendered page is unwanted,
remove the disorder or fix the renderer — ignoring the output just publishes a
dead link.

## Running it locally

```bash
# Full build (everything)
just gen-pages

# Incremental: render only specific changed disorder pages (+ aggregates)
just gen-pages-changed kb/disorders/Asthma.yaml kb/disorders/Marfan_Syndrome.yaml

# Incremental from a newline-delimited file (robust to any filename characters)
just gen-pages-changed-from changed.txt
```

See issue [#5507](https://github.com/monarch-initiative/dismech/issues/5507) for
the design rationale and [#5198](https://github.com/monarch-initiative/dismech/issues/5198)
for the broader build-speed work.
