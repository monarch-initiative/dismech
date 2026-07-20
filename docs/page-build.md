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
