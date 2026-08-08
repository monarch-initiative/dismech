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

Three mechanisms now close that gap:

1. **Self-healing escalation.** After rendering — and after the re-anchor in (2),
   which is what gives it a current KB to compare against — the workflow runs
   `classify_page_build.py --check-page-drift`, which compares the KB with the
   rendered pages on two axes. It runs for full builds as well as incremental
   ones: post-re-anchor, even a full rebuild's pages can be stale with respect to
   a disorder that merged while it was running.

   - **Count.** The number of `kb/disorders/*.yaml` inputs against the number of
     `pages/disorders/*.html` files. They are 1:1 in a healthy tree (page
     filenames are `slugify(disease name).html`, and slugs are unique), so any
     inequality means an earlier build under- or over-rendered.
   - **Content.** Every page is stamped with `sha256(source yaml)[:12]` — the
     renderer computes it for the OpenScientist panel and the template emits it
     as `yamlRevision` — so comparing that stamp against a fresh digest of the
     file says whether a page is *current*, not merely *present*.

     Note what that stamp covers: the **source YAML**, not the renderer. A
     template, CSS, or `render.py` change merging mid-build leaves every stamp
     matching while every page is out of date, so the drift check will report
     clean. That case is handled upstream instead — any change under `src/**`
     classifies the *next* build as `full` (see "How the mode is decided"), which
     re-renders everything regardless.

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

   **Repair is proportional.** One question decides it: a targeted render
   rewrites exactly the pages the drifted inputs map to, so is every stale page
   one of those? If so the checker writes that worklist with `--stale-files-out`
   and reports `heal=targeted`, and only those pages are rendered (measured:
   1m28s for 29) rather than everything (~30–60 min). If not — a page left
   orphaned by a rename or a deletion, which nothing in the render's output will
   rewrite — it reports `heal=full`, because only a full build prunes. A targeted
   heal is re-checked afterwards and falls back to a full rebuild if drift
   survives.

   Note that counting inputs against pages is the right *drift* signal but the
   wrong *repair* signal: it cannot tell an addition, which a targeted render
   fixes, from a deletion, which it cannot. That distinction matters because
   re-anchoring (2) makes a disorder added mid-build the common case, and gating
   the cheap path on equal counts would make a second full rebuild the routine
   response to the most routine event. Without the cheap path, a repo whose
   merges outpace a full build would sit in permanent full-rebuild mode.
2. **Re-anchoring the output on current `main`.** Immediately after rendering and
   *before* the drift check, the job commits the pages it rendered, fetches
   `main`, recreates `auto/generate-pages` at that new tip, and re-applies **only
   the pages this build actually changed**.

   This is what lets tier 1 above see anything at all. The job checked `main` out
   once, 30–60 minutes earlier; without re-anchoring, a disorder merged mid-build
   is missing from the tree *along with* its page, so the drift check compares a
   stale KB against its own matching stale pages, finds perfect agreement, and
   reports clean. Re-anchoring makes `kb/` current while keeping this build's
   rendered pages, which is exactly the mismatch the check is looking for. It
   also puts the aggregates (`app/data.js`, dashboard, pathographs, schema docs —
   all generated *after* this step, deliberately) on current data.

   And it stops the regen PR conflicting. A branch built at a stale checkout
   collides with any later regen that touched the same page; that is what left
   [PR #8140](https://github.com/monarch-initiative/dismech/pull/8140)
   `CONFLICTING` with auto-merge armed but unable to fire, so a full rebuild that
   had already corrected 29 pages sat unmergeable until an incremental build
   overwrote it.

   **The re-apply must stay narrow.** Restoring all of `pages/` instead of just
   the changed files carries this build's stale copy of every *other* page with
   it and overwrites whatever `main` corrected in the meantime — converting the
   fix into a revert. The selective restore is the explicit form of what a
   three-way merge did implicitly.

   Not a `--force-with-lease` problem, which is the tempting reading. The lease
   works; it guards against the branch moving between this job's fetch and its
   push. On 2026-08-07 the clobbering run fetched at 15:53, two minutes *after*
   the rebuild it went on to overwrite, so its lease was legitimately current.
   What was stale was the page content it rebuilt from `main`, not its view of
   the branch.
3. **A hard gate before publishing.** After `just gen-browser-data`, the workflow
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

## The regen PR lifecycle

Generated output reaches `main` through a single reused branch,
`auto/generate-pages`, and a single PR that each run **updates in place** rather
than replacing. Two consequences are easy to get wrong:

- **"Stale" must mean abandoned, not old.** Because the PR is refreshed rather
  than reopened, it keeps ageing by its creation date no matter how current its
  contents are. The cleanup step therefore measures age from `updatedAt`, and
  never closes the PR whose head is the branch's current tip — that PR is by
  definition the pending output of the most recent run. Selecting on `createdAt`
  closed a PR 36 minutes after a full rebuild had force-pushed 29 corrected pages
  onto it and armed auto-merge, discarding a repair that had already succeeded
  ([#8149](https://github.com/monarch-initiative/dismech/pull/8149)).
- **Queued runs make the delay longer than it looks.** `concurrency` with
  `cancel-in-progress: false` means a run triggered while another is building
  does not start until that one finishes, so its "close stale PRs" step can
  execute an hour after the run was triggered — long enough for a PR that was
  fresh at trigger time to look abandoned by the time it is judged.

### Review and approval

Regen PRs get **no agentic review** — an LLM review of thousands of regenerated
HTML files is cost without signal. Two mechanisms enforce that, because these
PRs reach the review workflow by two different routes:

- The `claude-code-review` workflow's `pull_request` trigger skips its review
  job for any PR whose head branch starts with `auto/generate-` (covering
  `auto/generate-pages`, `auto/generate-grouping-pages`, and
  `auto/generate-project-pages`) *and* whose author is `github-actions[bot]`.
  In practice these `pull_request` runs were mostly gated at `action_required`
  with no jobs executed anyway — GITHUB_TOKEN pushes don't get auto-run —
  which is why the second route existed.
- The reviews that *actually* ran historically came from `pr-shepherd`
  dispatching the review workflow for PRs stuck in `REVIEW_REQUIRED`. The
  shepherd is now instructed to leave regen PRs alone, and as a deterministic
  backstop the review workflow's `dispatch-guard` job resolves any dispatched
  PR's head branch and author and declines page-build PRs there too.

Because branch protection still requires one approving review before the armed
auto-merge can fire, **each regen workflow approves its own PR** as its final
step (via the shared `.github/actions/approve-regen-pr` composite action, which
carries the full rationale in its `description`), using the ai4c-reviewer app
token (GITHUB_TOKEN is the PR author and cannot approve its own PR). The
approval names the exact commit the run just pushed and is skipped if the branch
tip has moved since, so nothing is vouched for sight-unseen; it re-arms after
every force-push, since pushes dismiss stale approvals. Placing it in the regen
workflows — which always execute — rather than a `pull_request`-triggered job is
deliberate, per the gating above.

Human-authored PRs are unaffected — every skip requires the bot author — and a
full agentic review of a regen PR can still be forced by commenting `/review`
on it (the one escape hatch left open: it requires a collaborator author, so it
is always an explicit human request).

> **Root cause worth chasing separately.** The reason `pull_request` runs on
> these branches conclude `action_required` with no jobs is a repository/org
> Actions setting that requires approval for workflow runs on `github-actions[bot]`
> pushes — not anything in these workflow files. The design above routes around
> it (and stays correct even if it is lifted, since the `pull_request` skip
> clause then takes over), but fixing that setting would let regen PRs run their
> checks on the `pull_request` trigger normally and would likely simplify other
> bot-push workflows too. Tracked as a maintainer follow-up.

See issue [#5507](https://github.com/monarch-initiative/dismech/issues/5507) for
the design rationale and [#5198](https://github.com/monarch-initiative/dismech/issues/5198)
for the broader build-speed work.
