# OAK Ontology Database Caching (CI)

This page explains how dismech avoids re-downloading large ontology databases
during continuous integration, and — just as importantly — what this caching is
*not*. It is the companion to [Ontology Term Caches](ontology-caches.md): that
page covers the committed CSV label snapshots (`cache/*/terms.csv`); this page
covers the SQLite databases that sit underneath them.

## The two-layer picture

Term validation resolves ontology labels through two layers:

1. **Committed CSV label cache** (`cache/<prefix>/terms.csv`). Checked first. A
   pinned snapshot of `curie → label`. If a term is here, no ontology is
   touched at all. This is the deterministic, hermetic layer described in
   [Ontology Term Caches](ontology-caches.md).
2. **OAK SQLite database** (this page). Consulted **only on a cache miss** —
   i.e. when a KB entry introduces a term that is not yet in the committed CSV.
   OAK then lazily builds a `sqlite:obo:<name>` adapter, which downloads the
   whole compressed ontology database and unpacks it locally.

So in steady state — validating entries whose terms are already cached — CI
downloads nothing. A download happens only when genuinely new terms appear. The
problem this page addresses: a fresh CI runner has an empty database layer, so
**every** run that hits even one new term re-downloads a whole ontology, over
and over, run after run.

## Where the databases come from, and why we care

OAK fetches `sqlite:obo:<name>` databases from the public **bbop-sqlite** bucket:

```
https://s3.amazonaws.com/bbop-sqlite/<name>.db.gz
```

This bucket is part of the Berkeley/OBO ontology-tooling infrastructure that our
own institution helps host. Every uncached download is **egress we are
effectively paying for**. A single fresh runner re-pulling, say, `chebi.db`
(~3.7 GB uncompressed) on every curation PR added up quickly across the many CI
runs this repo does each week — which is why CHEBI, and the other large
ontologies, are no longer fetched for term validation (see below; `ncit.db`,
`hp.db`, and `mondo.db` are still fetched by page generation, which bypasses the
config).

For term validation the heavy ones are now all handled: `conf/oak_config.yaml`
routes the giants — NCBITaxon (~13.5 GB), CHEBI (~3.7 GB), NCIT (~2.7 GB), HP
(~1.1 GB) — plus MONDO, GO, UBERON, CL, PATO, ENVO, and FOODON to EBI's Ontology
Lookup Service (`ols:`) instead, which does cheap single-term lookups against
EBI's servers and does not touch our bucket (see issue #5160). Note this is a
statement about *that path only*: NCIT, HP, and MONDO are still pulled locally
during page generation, which does not read this config — see below.

Concretely, `just validate-terms-schema` from a clean OAK cache used to download
`chebi.db` (~3.5 GB unpacked); it now pulls only `geno.db` (~5 MB).

**This covers the term-validation path only — it is not the whole story.**
`conf/oak_config.yaml` governs the validators (`linkml-term-validator` and the
enum-cache tooling). Along that path, no multi-GB build remains local: what is
still fetched is small (`hgnc`, `geno`, `icd10cm`, `icd11f`, `ecto`, `xco`,
`opl`).

Several modules bypass the config entirely and construct an adapter directly.
**Page generation is where this costs real egress**, because
`.github/workflows/generate-pages.yaml` has **no** OAK cache step (its only
`cache` line is `setup-uv`'s Python-dependency cache). It runs on a **daily
`0 6 * * *` full-rebuild cron**, plus every push to `main` matching a path
filter much broader than the KB itself — 13 patterns covering not just
`kb/disorders/*.yaml` and `kb/comorbidities/*.yaml` but also `research/*.md`,
several `src/dismech/**` paths, `conf/qc_config.yaml`, `project.justfile`,
`mkdocs.yml`, and `docs/**`; see `on.push.paths` for the current set. (A
docs-only change to this very file matches it.) Two paths in that workflow pull
cold builds:

| Path | Build | Trigger |
|---|---|---|
| `render.py` `STRICT_HIERARCHIES` → `_augment_mapping_hierarchies`, called per disorder from `render_disorder` | `sqlite:obo:ncit` (~2.7 GB), `sqlite:obo:icd10cm` | `just gen-pages`; fires for the 54 entries carrying `ncit_mappings`/`icd10cm_mappings` |
| `HPOCategoryResolver` (`src/dismech/export/browser_export.py`), called per HP id | `sqlite:obo:hp` (~1.1 GB) | `just gen-browser-data` |

`render.py` also builds `sqlite:obo:mondo` in `_cached_mondo_descendants` /
`_cached_mondo_label`. Every one of these is lazy — the adapter is constructed
only when an entry actually has a matching mapping or term — so none of it fires
on an empty corpus. The corpus is not empty.

None of this is a regression; it all predates the OLS migration and became
visible only because the config-driven downloads were removed around it. It is
tracked in issue #8173. Other modules bypass the config the same way but are not
on a CI hot path: `scripts/ncit_p302_audit.py` (also `sqlite:obo:ncit`, reached
from `just ncit-p302-audit`), `scripts/validate_terms.py`,
`src/dismech/compare/d2p.py`, and `src/phenoagent/matching.py`. That list is
"the ones known as of writing", not a guarantee — `grep -rn 'sqlite:obo:' src/
scripts/` is the way to re-derive it.

Note the rendering path is **not** a candidate for a straight `ols:` swap: both
`_build_hierarchy_path` and `_cached_mondo_descendants` do bulk hierarchy
traversal, which is exactly the access pattern OLS is worst at. Fixing this
likely means caching the build in the workflow, or precomputing the derived
paths — not changing the adapter string.

Moving a prefix to `ols:` is only safe when OLS agrees with the local build on
both the canonical label *and* whether its `rdfs:subClassOf` ancestor closure
reaches the enum source nodes that prefix is validated against. Verify that
term-by-term before migrating another one — it is not automatic. The
counter-example is instructive: newer MONDO terms have an OLS closure that omits
`MONDO:0000001`, so per-value `reachable_from` checks fail for them even though
label lookup works. HP, CL, CHEBI, ENVO, and FOODON were each compared against
their local build with zero disagreements; the per-prefix source nodes are
listed in the note at the bottom of `conf/oak_config.yaml`.

## What we are NOT doing

**We are a consumer of these ontology databases, not a redistributor.** This
caching layer exists solely to stop our own CI from re-fetching the same files
from the source bucket. Concretely:

- The `.db` / `.db.gz` files are **never committed** to this repository and
  **never republished** anywhere public. They stay in an ephemeral,
  **private GitHub Actions cache** scoped to this repo.
- We do not mirror, host, or serve these ontologies to anyone else. If you want
  the databases, get them from the authoritative sources (OBO / bbop-sqlite /
  the ontology projects themselves), not from us.
- The GitHub Actions cache is a build accelerator with automatic eviction, not a
  durable archive. It can vanish at any time and correctness never depends on
  it — the committed CSV layer is what pins the labels we validate against.

In short: the goal is to be a *polite* consumer that pulls each database about
as rarely as possible, not to become an alternative distribution point.

## How OAK decides where the database lives

This detail matters because it is easy to cache the wrong directory and get a
silent re-download anyway.

OAK resolves and stores databases via `pystow`:

```
pystow.module("oaklib")  →  <PYSTOW_HOME>/oaklib/<name>.db
```

- `PYSTOW_HOME` defaults to `~/.data`, so the default location is
  `~/.data/oaklib/<name>.db`.
- OAK reads **only** `PYSTOW_HOME` for this. It does **not** honor `OAK_DB_DIR`
  or any other variable. (`scripts/fetch_ontology_dbs.sh` accepts `OAK_DB_DIR`
  as a staging escape hatch, but if that path is not `<PYSTOW_HOME>/oaklib`, OAK
  will ignore the files you fetched and download fresh copies. The script now
  warns when that mismatch is about to happen — always prefer `PYSTOW_HOME`.)
- OAK's default cache policy refreshes a database that is older than **one
  month**, so even a cached file is re-downloaded roughly monthly. That is a
  reasonable freshness cadence and still a massive reduction from per-run pulls.

## What CI does

The reusable composite action **`.github/actions/oak-cache`** wires this up in
one line. Each workflow that runs OAK-backed validation adds:

```yaml
- name: Cache OAK ontology databases
  uses: ./.github/actions/oak-cache
```

The action:

1. **Pins `PYSTOW_HOME`** to a stable runner-local path (under `RUNNER_TEMP`) and
   exports it, so the directory it caches is provably the directory OAK reads.
2. **Restores and saves `<PYSTOW_HOME>/oaklib`** with `actions/cache`, using an
   accumulating key pattern:

   ```
   key:          oak-sqlite-<hash of conf/oak_config.yaml>-<run_id>
   restore-keys: oak-sqlite-<hash of conf/oak_config.yaml>-
                 oak-sqlite-
   ```

   The unique `run_id` in the key guarantees the post-job save always runs (so
   any newly downloaded database is captured for next time), while the
   `restore-keys` prefixes restore the most recent prior cache. Hashing
   `conf/oak_config.yaml` invalidates the cache when the adapter configuration
   changes — for example when an ontology is moved between `sqlite:obo:` and
   `ols:`.

Because the cache accumulates lazily, it only ever contains the databases that
validation actually needed. Now that CHEBI is served over OLS, that is only the
small remaining builds — tens of MB rather than the multi-GB `chebi.db`.

Workflows currently using the action: `main.yaml` (the PR validation path —
`validate-terms-schema`, `validate-disorders`, `test-kb`) and
`weekly-compliance.yaml` (its agent runs `just validate`). The dormant
`test-linkml-rc3.yml` canary (which only runs when its own file changes) is
deliberately left out — the marginal egress it would save is not worth waking it
on unrelated PRs.

## Local development

You normally don't need to do anything — the first validation run downloads what
it needs into `~/.data/oaklib` and every later run reuses it. To pre-provision
(e.g. before offline work) with resume/retry:

```bash
just fetch-ontology-dbs             # all sqlite:obo:* DBs in oak_config.yaml
just fetch-ontology-dbs hgnc geno   # just the named ones
```

If you keep your ontology cache somewhere other than the default, set
`PYSTOW_HOME` (not `OAK_DB_DIR`) so both OAK and the fetch script agree:

```bash
PYSTOW_HOME=/big/disk/pystow just fetch-ontology-dbs
PYSTOW_HOME=/big/disk/pystow just validate kb/disorders/Asthma.yaml
```

## Related

- [Ontology Term Caches](ontology-caches.md) — the committed CSV label layer
  that sits on top of this one.
- `conf/oak_config.yaml` — which prefixes use `sqlite:obo:` (local DB) vs `ols:`
  (remote lookup), with rationale for the ones moved off local DBs.
- `scripts/fetch_ontology_dbs.sh` — the resume/retry pre-provisioning script.
- Issue #5160 — moving the largest ontologies to OLS.
