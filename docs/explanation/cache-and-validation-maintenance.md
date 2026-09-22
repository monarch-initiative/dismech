# Cache and validation maintenance

Read this when changing corpus readers, ontology-dependent rendering, or fixing
merge-induced validation failures. Curators should start with the
[term skill](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/dismech-terms/SKILL.md) and
[reference skill](https://github.com/monarch-initiative/dismech/blob/main/.claude/skills/dismech-references/SKILL.md).

### Parsed-KB Cache (`src/dismech/kb_cache.py`)
Many code paths walk `kb/disorders/` and parse every file to build a small
index. One walk parses ~2,700 files (~17 s). `kb_cache.load_document(path)`
keeps one parsed copy per file per process, keyed on the file's content hash,
so later walks cost a read and a hash. The returned object is **shared and
read-only**: code that decorates or edits a document must parse its own copy
(`dismech.yaml_io.safe_load_path`), which is what `render.load_disorder` does
for the page being rendered while the index walks use `load_disorder_shared`.
Holding the parsed disorder corpus costs ~450 MB per process;
`DISMECH_KB_CACHE=0` turns the cache off. Route a new corpus walk through it
rather than adding another `glob` + `safe_load` loop (issue #11003).

**A CLI that walks the corpus exactly once should call `kb_cache.default_off()`
from its `main()`.** With no second walk there are no hits to collect, so the
cache is pure cost -- `check_snippet_length` measures 17.1 s / 34 MB without it
against 20.5 s / 522 MB with it, while the two-walk
`check_environmental_evidence` goes the other way (28.0 s -> 18.3 s). Put the
call in `main()`, never at import: pytest imports these scripts' `scan_repo`
functions directly and runs several of them in one process, which is exactly
the case the cache exists for. `default_off()` uses `setdefault`, so an
explicit `DISMECH_KB_CACHE` still wins.

**The hierarchy cache is a speed cache, never a correctness gate.** A miss falls
back to a live OAK walk, so an entry curated after the last rebuild still
renders — just slowly. That is why `check-hierarchy-cache` is advisory and is
not in `just qc`: it reports staleness, and staleness costs seconds, not a wrong
page. The reason it exists at all is that one `hierarchical_parents` call
against the local NCIT build takes roughly 4.7 s, so a single ten-node
breadcrumb costs about 47 s (#11186). Ten nodes is the NCIT tail; the mapped set
averages closer to six, which is the ~30 s
`scripts/build_hierarchy_cache.py --check` quotes for a miss. The two figures
agree — one is the worst case, the other the mean.

Two things worth knowing before you touch it:

- **`STRICT_HIERARCHIES` declares an ICD10CM root that the walk never reaches.**
  `ICD10CM:ICD-10-CM` exists in the `sqlite:obo:icd10cm` build but nothing links
  up to it: chapter codes such as `ICD10CM:C00-D49` report no
  `hierarchical_parents`, so every ICD10CM breadcrumb tops out at its chapter.
  None of the mapped CURIEs reach the declared root. This predates the cache and
  the cache reproduces it faithfully; it is pinned by
  `test_icd10cm_paths_stop_at_a_chapter_not_at_the_configured_root` so a future
  build that does connect the chapters is noticed rather than silently changing
  every ICD10CM breadcrumb. NCIT reaches its root for every mapped CURIE.
- **Rebuilding needs the local SQLite build for that prefix**
  (`just fetch-ontology-dbs icd10cm ncit`). The builder memoises parent and
  label lookups across CURIEs, which matters: the mapped NCIT set resolves in
  146 parent queries rather than one full walk per CURIE. It also keeps the
  existing `retrieved_at` on any row whose path and labels did not move, so
  adding one mapping is a one-line diff rather than a whole-file restamp — the
  same incremental contract `cache/<prefix>/terms.csv` follows, and for the
  reason the [frozen dataset-cache history](../dataset-curation.md#cachedataset_accessionsjson-is-frozen--never-touch-it) records.
- **The drift guard is local-only, deliberately.** The test that compares the
  committed cache against a live OAK walk is marked `oak_db`, a marker meaning
  "needs a local ontology database" — distinct from `kb_data`, which is about KB
  files. Do not treat one as a CI gate.

  **An `oak_db` test needs two guards, and the obvious one is not enough.**
  `just test-code` deselects the marker, and each such test must *also* check
  for the build file with `dismech.oak_db.local_build_present`. Opening the
  adapter is not a check: `get_adapter("sqlite:obo:ncit")` does **not** fail
  when the build is missing — semsql downloads it. So an
  `if adapter is None: pytest.skip(...)` guard never fires, and a lane that
  forgets the marker (a bare `pytest`, as `test-linkml-rc3.yml` runs) pulls
  gigabytes instead of skipping. This is not hypothetical: it cost one CI run
  11m35s and 3.6 GB. The same trap applies to any script that means to *require*
  a local build — `scripts/build_hierarchy_cache.py` asks about the file for
  exactly this reason.

  What runs in CI is `just check-hierarchy-cache` in the nightly sweep:
  offline, seconds, and it catches the drift case that actually happens — a
  curator adds an ICD10CM/NCIT mapping and nobody rebuilds. The `oak_db` drift
  test compares **every** committed row in both prefixes against a live walk,
  which takes about 15 minutes against the local builds — budget for that before
  running `pytest -m oak_db`, and do not put it in a loop.

**The same rule governs the MONDO and HP lookups, which are not hierarchy
lookups at all.** Several call sites hardcode a `sqlite:obo:` adapter and so
bypass `conf/oak_config.yaml`, which routes both prefixes to `ols:` precisely to
keep the builds off the machine. Each of these therefore used to fetch its build
silently — no error, no log line, just a slow run (#11299):

| Call site | Adapter | Build | Guard now |
|---|---|---|---|
| `render._mondo_adapter` (grouping coverage descendants + labels) | `sqlite:obo:mondo` | 588 MB | returns `None`, so the coverage table degrades to "MONDO descendant lookup unavailable" |
| `export/browser_export.HPOCategoryResolver` (HP term → broad phenotype category) | `sqlite:obo:hp` | 440 MB | falls back to the committed `app/hpo_category_cache.json`, then to no categories |
| `phenoagent.matching._HPOIsARelationshipResolver` (is-a ancestry for broader/narrower phenotype matches) | `sqlite:obo:hp` | 440 MB | reports no ancestry, so a match is exact or nothing |
| `compare/d2p.HPOClosureResolver` (is-a closure for the OMIM/Orphanet audit) | `sqlite:obo:hp` | 440 MB | warns once, then reports no ancestors and no labels |

All four ask `dismech.oak_db.local_build_present` before opening the adapter, so
none of these degradations is a decision about whether MONDO or HP *matters* — it
is the answer to "can this be served without a download". They have in common
that the ontology is incidental to what they are doing, and each already had a
degradation path to take.

**Not everything that opens a build is a bug, so check before adding a guard.**
`compare/mondo_export._materialize_default_mondo_db` opens `sqlite:obo:mondo` to
download it on purpose — that is a CLI whose job is to export MONDO, and its own
docstring says so. And `groupings.py` only *looks* like another bypass: it
resolves its adapter through `conf/oak_config.yaml`, so HP there is `ols:hp` and
no build is involved. The test is whether the caller can do its job without the
ontology.

**The `phenoagent` one is the case that shows why the two-guard rule exists.**
Its tests are what actually pulled `hp.db` in the fast lane, and 21 of them
genuinely need real HPO ancestry — `HP:0002123` is-a `HP:0001250` is not
something a stub can answer. Those carry `@pytest.mark.oak_db` *and* their own
`local_build_present` check, exactly as the marker's own description requires:
the marker keeps them out of `just test-code`, and the file check makes a bare
`pytest` skip them rather than download 440 MB to run them. Either guard alone
leaves a lane that downloads. **Page generation needs the
real thing and fetches it deliberately**: `generate-grouping-pages.yaml` runs
`just fetch-ontology-dbs mondo` and `generate-pages.yaml` runs
`just fetch-ontology-dbs hp` before the step that needs it — the same bytes
those jobs already pulled, now stated in the log and fetched with resume/retry.
Do the same locally before regenerating those pages, or the output loses MONDO
descendant rows and newly curated HP terms' categories.

Two consequences worth keeping straight:

- **`app/hpo_category_cache.json` is now committed on every page build, and
  read back as a fallback.** It was not: the path was missing from
  `generate-pages.yaml`'s `BUILT_PATHS`, so the workflow regenerated and then
  discarded it on every run. It was added by hand in `1805aa943` (2026-02-09),
  last touched in `85e61f51e` (2026-04-09), and sat frozen for the five months
  after that while the KB grew around it — 1,415 HP terms in the cache against
  4,526 in the `app/data.js` written by the same step, which is why `render` was
  dropping most phenotypes into the "Other" group. Adding the path fixes it; the
  first page build after it carries the catch-up diff, and the two counts should
  track each other from then on. A term the exporter could not resolve is
  **never** written back as an empty category list — that would bake the gap in
  permanently — it is left out and counted, and the exporter says so.

  **Do not date this file from `git log` in a CI checkout.** Both the review of
  #11462 and the reply correcting it named the wrong commit, independently and
  for the same reason: these runners use a shallow clone, so
  `git log --diff-filter=A` reports the *shallow boundary* commit as the one
  that added a file. Two different truncation depths, two different wrong
  answers, both confident. Ask the API (`list_commits` with a `path`), or
  `git fetch --unshallow` first.
- **A grouping's exact-match roots survive the outage.** They come from the
  grouping's own YAML, not from MONDO, so the unavailable branch keeps them in
  scope and the coverage figure stays computable; only the descendant rows go.

## Duplicate YAML Keys (dismech#8623)

A YAML mapping may not repeat a key. PyYAML's safe loaders — what
`dismech.yaml_io.safe_load`, and so nearly everything here, uses — accept a
repeated key anyway and silently keep the **last** value; the ruamel-backed
`linkml-reference-validator` raises `DuplicateKeyError` and aborts. A duplicate
is therefore invisible to every test, renderer, and export in this repo while
being fatal to validation CI.

Crucially, duplicates arrive by **merge**, not by authoring: two concurrent
curation PRs each adding a `classifications:` block at a different point in one
entry merge without a git conflict. Both PRs are green against their own base,
and only the post-merge push build on `main` goes red.

```bash
just check-duplicate-keys                              # kb/ + schema + conf (~12s, offline)
just check-duplicate-keys kb/disorders/Asthma.yaml     # specific files
```

It runs in `just qc` and, unlike `just validate-disorders`, as an **ungated,
whole-KB** CI step — checking only the changed files is what let a duplicated
`classifications:` sit unnoticed in `Ulcerative_Colitis.yaml`.

**Fixing one: merge the blocks, do not delete a block.** Each side is somebody's
curation, and the two usually differ — one carries `notes`, the other cited
`evidence`. Fold them into the single block at the canonical position and keep
both sets of values, then re-read the surviving prose: an `explanation` arguing
for the narrower choice will contradict the merged result and needs trimming.

## Case-Colliding Paths (dismech#11204)

Git must never track two paths that differ only in letter case, such as
`references_cache/DOI_10.1172_JCI89626.md` and
`references_cache/DOI_10.1172_jci89626.md`. On the macOS and Windows default
filesystem only one of them can exist, so one path shows as modified forever,
no `git checkout` or `git stash` clears it, and `git rebase` refuses to run.
Linux CI sees nothing wrong, which is how 17 such DOI pairs accumulated before
they were removed.

```bash
just check-case-collisions      # whole repo, <1s, offline
```

It runs in `just qc` and as an ungated CI step. The usual source was a DOI
fetched in two capitalizations: DOIs resolve case-insensitively, but the cache
filename copies the DOI as written. The patched fetcher now reuses an existing
`DOI_*.md` file whose name differs only in case, on both read and write
(`src/dismech/doi_cache_case.py`, #9112), so a second spelling no longer writes a
second file; a DOI with no cache file yet is still saved as written. To fix a
collision that gets past it, keep the path matching the publisher's
capitalization and remove the other from the index with `git rm --cached <path>`,
which works on a case-insensitive disk because it never touches the file itself.

## Retired Enum Values (dismech#10061)

The sibling of the duplicate-key problem above, with the same merge-shaped
cause. When a schema change **narrows** an enum, every PR already in flight
carries values that were legal when written and are illegal on merge. Nothing
either side runs can see it: the narrowing PR does not contain the curation
files, and the curation PRs do not contain the narrowed enum. Only the merge
result holds both.

That is exactly how #10003 played out. It retired `supports: PARTIAL` and
migrated every occurrence on its own base; ~15 open curation PRs then landed
more. Nine invalid values reached `main` within 90 seconds of the merge, and
100 within a day.

```bash
just check-enum-values                              # whole KB (~21s, offline)
just check-enum-values kb/disorders/Asthma.yaml     # specific files
```

It runs in `just qc` and as an **ungated, whole-KB** CI step, for the same
reason `check-duplicate-keys` is. The path-gated `just test-kb` sweep cannot
cover it: that filter fires on schema changes, and the PRs that carry the stale
value touch no schema.

**Scope, and what it deliberately skips.** It checks one constraint — is this
value permissible in this slot's enum — not conformance, which is what keeps it
cheap enough to run everywhere. Dynamic (`reachable_from`) ontology enums are
`linkml-term-validator`'s job and are skipped; so is any slot name that is
enum-bound in one class and free text in another (`severity`), since flagging
those would flag correct prose. `kb/hypotheses/` is checked against
`hypothesis_assessment.yaml` / `hypothesis_reconciliation.yaml` rather than
`dismech.yaml` — running the wrong schema there reports five legal values as
errors.

**When you narrow an enum, the values are only half the job.** #10003 migrated
11,804 `PARTIAL` items to `SUPPORT` and left every `explanation` that argued for
the retired grade in place, so ~3,600 evidence items still say "Marked PARTIAL
because…" above a value the schema no longer has. Prose that names a retired
value is not caught by any gate. Budget for it, or record it in a worklist the
way #10003 did.
