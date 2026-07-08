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
(~3.7 GB uncompressed) on every curation PR adds up quickly across the many CI
runs this repo does each week.

The heavy ones are already handled where possible: `conf/oak_config.yaml` routes
the two giants — NCIT (~2.7 GB) and NCBITaxon (~13.5 GB) — plus MONDO, GO, and
UBERON to EBI's Ontology Lookup Service (`ols:`) instead, which does cheap
single-term lookups against EBI's servers and never touches our bucket (see
issue #5160). What remains on `sqlite:obo:` and can still be pulled from the
bucket: `chebi` (the big one), `cl`, `hp`, `hgnc`, `maxo`, `geno`, and the
smaller `icd10cm`, `icd11f`, `ecto`, `envo`, `foodon`, `xco`, `opl`.

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
validation actually needed — typically a few hundred MB, and the multi-GB
`chebi.db` only if a new CHEBI term was introduced.

Workflows currently using the action: `main.yaml` (the PR validation path —
`validate-terms-schema`, `validate-disorders`, `test-kb`), `test-linkml-rc3.yml`
(`validate-terms-schema`), and `weekly-compliance.yaml` (its agent runs
`just validate`).

## Local development

You normally don't need to do anything — the first validation run downloads what
it needs into `~/.data/oaklib` and every later run reuses it. To pre-provision
(e.g. before offline work) with resume/retry:

```bash
just fetch-ontology-dbs             # all sqlite:obo:* DBs in oak_config.yaml
just fetch-ontology-dbs hp chebi    # just the named ones
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
