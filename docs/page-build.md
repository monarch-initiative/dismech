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
   `classify_page_build.py --check-page-drift`, which compares the number of
   `kb/disorders/*.yaml` inputs with the number of `pages/disorders/*.html`
   files. They are 1:1 in a healthy tree (page filenames are
   `slugify(disease name).html`, and slugs are unique). Any inequality means an
   earlier build under- or over-rendered, and the workflow escalates to
   `just gen-pages` in the same run. The check runs *after* rendering on purpose —
   before it, every disorder-adding push looks drifted and would escalate.
2. **A hard gate before publishing.** After `just gen-browser-data`, the workflow
   runs [`just check-browser-links`](https://github.com/monarch-initiative/dismech/blob/main/scripts/check_browser_data_links.py),
   which resolves every `page_url` in `window.searchData` against the filesystem
   and **fails the job** if any target is missing. A count comparison cannot see
   a rename that keeps the counts equal but changes a slug; this can.

Run the gate locally against a build with `just check-browser-links`.

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
