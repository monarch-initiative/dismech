# Removing MAXO from dismech — full migration plan

**Status:** Draft for review (do not execute until approved)
**Branch:** `claude/remove-maxo-dismech-w86v1a`
**Goal:** Remove the Medical Action Ontology (MAXO) from dismech entirely, remapping
every MAXO treatment/diagnostic term to its best-equivalent NCI Thesaurus (NCIT) term.

## Why this is non-trivial

MAXO is used **4,354 times across 1,358 KB files** (352 distinct MAXO terms), almost
entirely as `treatment_term` bindings (with a smaller set of `diagnosis_term` uses).
It is also a documented, co-equal treatment ontology in the design-decision register.
This is a large data migration plus a schema/code/docs cleanup, not a config toggle.

The migration is feasible because the schema's `TreatmentActionTerm` dynamic enum
**already accepts NCIT** alongside MAXO:

```yaml
TreatmentActionTerm:
  description: A term representing a medical action or treatment (from MAXO or NCIT)
  reachable_from:
    source_nodes:
      - MAXO:0000001  ## medical action
      - NCIT:C25218   ## Clinical Intervention or Procedure
```

NCIT is the natural replacement target for every MAXO term.

## Key technical risk — NCIT reachability validation

Treatment terms are validated against a **materialized enum cache**
(`cache/enums/treatmentactionterm_<hash>.csv`) — currently **502 CURIEs: 334 MAXO +
167 NCIT** (the reachable-and-used subset). The `<hash>` is derived from the enum
definition; removing `MAXO:0000001` from `source_nodes` changes the hash → a new cache
file regenerates to an **NCIT-only** set.

**The catch:** NCIT is now served via **OLS** (`ols:ncit`, issue #5160), and the OLS
adapter **cannot compute ancestors** (`NotImplementedError`). MAXO's reachability was
computed from local SQLite; NCIT's cannot be recomputed offline the same way. Before
touching data we must confirm how `dismech.enum_cache` regenerates the NCIT-reachable
member set for `TreatmentActionTerm` (it may rely on a frozen snapshot, a local NCIT
SQLite build, or a different path). **If the enum cache cannot be regenerated with the
migrated NCIT terms, term validation will fail even for correct NCIT terms** — this
gates the whole migration and must be resolved in Phase 0.

## Phase 0 — De-risk (do first, no content changes)

**Confirmed mechanism:** `enum_cache --offline` does only structural checks. The actual
membership re-derivation — asking OAK whether a used CURIE is reachable from the enum
roots and writing positive hits into the cache CSV — runs in **non-offline** mode via
`linkml-term-validator`'s `BindingValidationPlugin`. That reachability query is what the
OLS NCIT adapter cannot answer, so **new NCIT terms cannot be auto-added to the treatment
enum cache while `NCIT: ols:ncit`.** (The 167 NCIT terms already in the cache predate the
OLS switch, issue #5160.)

**Concrete resolution — the repo already has the tool.** The `ncit-edges` structured
source (`data/ncit-edges/MANIFEST.yaml`, `adapter: sqlite:obo:ncit`) downloads and uses a
**local NCIT SQLite** via OAK/semsql (~2.7 GB, never committed). So the enum-cache
regeneration path is:

1. Temporarily point the `NCIT:` adapter at `sqlite:obo:ncit` in `conf/oak_config.yaml`
   (or a copy) so OAK can compute reachability. Pre-provision with `just fetch-ontology-dbs
   ncit` / the ncit-edges refresh.
2. With the schema's `source_nodes` set to NCIT-only, run the non-offline term validation /
   `enum_cache` regeneration so the new `treatmentactionterm_<newhash>.csv` is populated
   with every migrated NCIT term that is genuinely reachable from `NCIT:C25218`.
3. **Revert `oak_config` to `NCIT: ols:ncit`** — the committed state stays OLS-served; the
   local SQLite is only a build-time tool, consistent with how ncit-edges already works.
4. Prototype end-to-end on one migrated file (`validate` + `validate-terms` +
   `validate-references`) before proceeding.

This step also *empirically answers* the `NCIT:C25218` reachability question for
diagnostic/imaging/lab terms (open decision #2): terms that don't land in the regenerated
cache are the ones that aren't reachable from that root and need a second `source_node` or
a schema relaxation.

## Phase 1 — The crosswalk (the real work)

Build and freeze a MAXO→NCIT map for all **352 distinct terms**. See the companion
crosswalk TSV (`docs/superpowers/maxo_ncit_crosswalk.tsv`). Structure:

| Tier | What | Handling |
|---|---|---|
| Head (~40 terms) | Generic actions covering ~80% of occurrences (supportive care 654×, surgical procedure 360×, molecular genetic testing 284×, diagnostic procedure 198×, dietary intervention 158×, physical therapy 134×, chemotherapy 108×, gene therapy 87× …) | Map to NCIT equivalents (several already in CLAUDE.md's tables and the 167-term known-good NCIT vocab). High confidence. |
| Tail (~310 terms) | Single-/low-use diagnostic, imaging, lab, examination, avoidance, and drug-class "agent therapy" terms | Per-term NCIT lookup; many map cleanly, some only to a broader parent. |
| **Flagged (count TBD)** | MAXO concepts with **no reasonable NCIT equivalent** or that are **not procedures** (avoidances, drug-class "X agent therapy", counseling that may not sit under `NCIT:C25218`) | **Resolve case-by-case with the maintainer** before executing (per decision). |

**Note on `diagnosis_term`:** the schema comment says "MAXO includes diagnostic
procedures under medical actions." NCIT's diagnostic/imaging/lab-procedure branches
exist, but reachability from `NCIT:C25218` for these must be confirmed in Phase 0 —
if diagnostic procedures are not reachable from that root, the `diagnosis_term`
binding either needs a second `source_node` (e.g. a diagnostic-procedure root) or a
schema relaxation.

## Phase 2 — Data migration (`kb/disorders/*.yaml`)

- Script a deterministic find-replace over the frozen crosswalk, rewriting each
  `term.id` **and** `term.label` (label must match the NCIT canonical label exactly).
- No `kb/modules/*.yaml` changes needed (zero MAXO usage there).
- Re-verify every migrated file: `just validate <file>` + `just validate-terms <file>`.
- Add matching `history/` records for the KB edits (CI warns without them).

## Phase 3 — Schema (`src/dismech/schema/dismech.yaml`)

- Remove `MAXO:0000001` from `TreatmentActionTerm.source_nodes` (keep `NCIT:C25218`;
  add a diagnostic-procedure root if Phase 0 shows it's needed).
- Scrub MAXO from ~6 descriptions/comments: `treatment_term`, `diagnosis_term`,
  `TreatmentDescriptor`, `therapeutic_agent`, `TherapeuticModalityEnum`,
  `dietary_modifications`.
- Regenerate derived datamodels: `src/dismech/datamodel/dismech.py` and
  `dismech_pydantic.py`.
- Regenerate the treatment enum cache (new hash filename); delete the old
  `treatmentactionterm_a34e0d755d16.csv`.

## Phase 4 — Config, caches, code

- `conf/oak_config.yaml`: remove the `MAXO: sqlite:obo:maxo` adapter (line 53).
- Delete `cache/maxo/terms.csv` (and the `cache/maxo/` dir).
- `src/dismech/render.py:2278`: remove `MAXO` from the CURIE→browser-URL prefix list.
- Templates `disorder.html.j2` / `module.html.j2`: remove `.curie-chip-maxo` CSS.
- `src/dismech/export/kgx_export.py`: MAXO only appears in docstrings/comments
  (treatment nodes are prefix-agnostic) — cosmetic scrub.
- Delete `scripts/add_maxo_terms.py`.

## Phase 5 — Tests (4 files)

- `tests/test_data.py`: swap `MAXO:0000088` / `MAXO:0000124` fixtures to NCIT.
- `tests/test_kgx_export.py`: swap MAXO fixtures (`MAXO:0000001/0000312/0000648`) to
  NCIT; the test names/comments about "canonical MAXO label" should be reworded.
- `tests/test_tabular_export.py`: swap the `MAXO:0000088` fixture.
- `tests/test_term_cache_stability.py`: drop the `cache/maxo/terms.csv` reference
  (Asthma no longer references MAXO after migration).

## Phase 6 — Docs & governance

- `CLAUDE.md` (35 mentions): rewrite the "Treatment Terms (MAXO or NCIT)" section, the
  common-MAXO-terms table, the mechanical-backfill table's MAXO rows, and scattered
  references. `scripts/add_maxo_terms.py` reference removed.
- `docs/explanation/design-decisions.md`: update the ontology table (line 133) and the
  treatment selection rule (lines 146–147). **This reverses a recorded decision** — log
  the change with rationale in the register rather than silently editing.
- Grep for stray MAXO references across `docs/`, skills (`.claude/skills/*`), templates,
  and `projects/`.

## Validation gate (before commit)

```
just check-enum-cache-offline      # treatment enum cache regenerates NCIT-only
just validate-all                  # schema conformance
just validate-terms-all            # every migrated NCIT term exists + label matches
just validate-references <changed> # unaffected, but run on touched files
just pytest-all                    # fixtures updated
just qc
```

Final grep must show **zero** `MAXO`/`maxo` in committed source (schema, kb, conf,
src, scripts, tests, docs, CLAUDE.md) — derived `pages/`/`details`/`dashboard` HTML are
regenerated downstream and are out of scope.

## Open decisions for the maintainer

1. **Flagged unmappable terms** (count/list filled from the crosswalk): map to a broader
   NCIT parent, or relax the schema binding to allow term-less treatments? (Decision so
   far: **flag and resolve case-by-case**.)
2. **`diagnosis_term` root**: if NCIT diagnostic procedures aren't reachable from
   `NCIT:C25218`, add a diagnostic-procedure `source_node` or relax the binding?
3. Should the design-decision register keep MAXO listed as *deprecated/removed* with a
   dated rationale, or be fully scrubbed?
