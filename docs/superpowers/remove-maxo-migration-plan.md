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

**Done — frozen in the companion TSV `docs/superpowers/maxo_ncit_crosswalk.tsv`** (all
352 distinct terms, every NCIT id OAK-verified, labels canonical). Coverage weighted by
the 4,354 occurrences:

| Confidence | Terms | Occurrences | Handling |
|---|---|---|---|
| HIGH (exact NCIT equivalent) | 173 | 3,379 (77.6%) | Direct flat swap. |
| MED (broader NCIT parent / equivalent) | 137 | 826 (19.0%) | Flat swap to the parent; minor specificity loss. |
| LOW (fallback, mostly drug-class → Pharmacotherapy) | 37 | 137 (3.1%) | See restructure note below. |
| NONE (no NCIT term at all) | 5 | 12 (0.3%) | Maintainer decision. |

**59 terms (204 occ, 4.7%) are "flagged"** — NONE, or a mapping whose target may not be
reachable from `NCIT:C25218` (Intervention or Procedure) because it isn't a procedure.
They split into actionable categories, most of which are **not** truly unmappable:

1. **Drug-class "X agent therapy" (~30 terms)** — NSAID, ACE inhibitor, statin, SGLT2i,
   beta-agonist/-blocker, PPI, CCB, SSRI/SNRI, diuretic, antihistamine, C5-inhibitor,
   copper chelator, etc. These map to NCIT *drug-class* nodes (Diuretic, Antiplatelet
   Agent, …) that are chemicals, **not** procedures. **Correct handling is a structural
   remap, not a flat swap:** set `treatment_term` → `NCIT:C15986 Pharmacotherapy` (a
   generic action reachable from `C25218`) and move the drug class into `therapeutic_agent`
   (whose binding is exactly for NCIT/CHEBI drug classes — the documented "Therapeutic
   Agent Pattern"). This *improves* the data model.
2. **Supplement-substance terms (~4)** — carnitine/calcium/magnesium supplementation map
   to NCIT *substance* nodes. Same fix: nutritional/supplementation action term +
   substance in `therapeutic_agent`.
3. **Avoidance / lifestyle (~8)** — sunlight/exercise/chemical-exposure avoidance →
   `NCIT:C54264 Avoidance` / `Lifestyle Therapy` / `Behavioral Intervention`. Reachability
   from `C25218` uncertain (Phase 0 confirms).
4. **Device terms (~4)** — hearing aid, cochlear implant, glasses, denture → NCIT *device*
   nodes (not procedures/usage actions).
5. **Diagnostic/lab (~2)** — enzyme-activity / RBC-enzyme assay → `Laboratory Procedure`.
6. **True NONE (5)** — `orthotic device usage`, `application of emollient to skin`,
   `airway management`, `apoptosis assay`, `transepithelial nasal potential difference
   measurement`. No NCIT equivalent; maintainer decision (drop `term:` + keep free-text
   `preferred_term`, or broaden — the former needs the binding relaxed from REQUIRED).

**Note on `diagnosis_term`:** the schema comment says "MAXO includes diagnostic procedures
under medical actions." NCIT's diagnostic/imaging/lab branches exist and most head-tier
diagnostic terms mapped cleanly, but reachability from `NCIT:C25218` for the procedure
branch is confirmed empirically by Phase 0's enum-cache regen — terms that don't land in
the regenerated cache need a second `source_node` (a diagnostic-procedure root) or a
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

1. **Drug-class "agent therapy" terms (~30, cat. 1 above):** adopt the structural remap
   (`Pharmacotherapy` action + drug class in `therapeutic_agent`)? Recommended — it's the
   documented pattern and keeps the treatment term reachable from `C25218`. The alternative
   (leave the NCIT drug-class node in `treatment_term`) will likely **fail** the enum-cache
   reachability check.
2. **The 5 true-NONE terms + device/avoidance/substance terms whose NCIT node isn't a
   procedure:** broaden to a reachable parent (e.g. `Therapeutic Procedure`,
   `Nutritional Support`), or relax the `treatment_term` binding from REQUIRED to allow a
   free-text `preferred_term` with no `term:`? (Prior direction: **resolve case-by-case**.)
3. **`diagnosis_term` root**: if Phase 0 shows NCIT diagnostic procedures aren't reachable
   from `NCIT:C25218`, add a diagnostic-procedure `source_node` or relax the binding?
4. **Design-decision register:** keep MAXO listed as *deprecated/removed* with a dated
   rationale, or scrub it entirely?

## Crosswalk provenance

Built by 6 parallel agents against `ols:ncit` (label-verified, no fabricated ids),
grounded in the 167-term known-good NCIT treatment vocabulary already in the enum cache.
Every mapping is reviewable in `maxo_ncit_crosswalk.tsv` (columns: count, maxo_id,
maxo_label, ncit_id, ncit_label, confidence, note). Freeze this file before Phase 2.
