# What Monarch KG content is not yet in DisMech — gap analysis & recommendations

*Analysis date: 2026-07-30. Author: AI-assisted (Claude Code).*

## Question

*"What Monarch Knowledge Graph content is not yet in DisMech, and what should be
added?"*

This report maps the association categories carried by the
[Monarch knowledge graph](https://monarch-initiative.github.io/monarch-ingest/)
against what DisMech models today, separates **genuine gaps** from **deliberate
scope boundaries** (per [design-decisions](../explanation/design-decisions.md)),
and gives a prioritized recommendation set. It is a strategy/worklist document,
not a schema change.

## TL;DR

- DisMech and Monarch KG are **complementary, not overlapping**. Monarch KG is a
  broad, automated *association* graph (gene↔phenotype↔disease↔ortholog across
  species). DisMech is a narrow, curated, evidence-grounded *mechanism* graph
  (etiology → molecular/cellular dysfunction → phenotype causal chains). Most of
  what Monarch has "extra" is either **already flowing into DisMech via existing
  comparison tooling** or is **deliberately out of DisMech's mechanism-first
  scope**.
- The **highest-value, in-scope, already-tooled** gap is **per-disease
  phenotype completeness**: DisMech covers a curated subset of each disease's
  HPOA phenotype set. A single audit of Marfan syndrome (below) surfaces **116**
  source-backed phenotype-completeness issues. This is systematically
  discoverable today with `dismech.compare.d2p audit_all`.
- The **one Monarch content *type* DisMech genuinely does not model** is
  **cross-species / model-organism structured data** — gene orthology (Panther),
  gene–gene interactions (BioGrid/String), model-organism phenotypes
  (ZFIN/Alliance/Pombase), and gene expression→anatomy (BGee). DisMech's policy
  keeps model-organism findings as **evidence** (`evidence_source:
  MODEL_ORGANISM`), not as first-class graph nodes. Recommendation: **keep it
  that way** for most of it; only structured model-organism *phenotype* capture
  is a defensible future schema follow-up.

## Method

- **Monarch KG side:** the ingested sources per the monarch-ingest docs are
  *Alliance, BGee, BioGrid, GO, HGNC, HPOA, NCBI, Panther, Phenio, Pombase,
  Reactome, STRING, ZFIN*, emitted as a BioLink-Model graph.
- **DisMech side:** the `Disease`-class schema, the KGX export categories
  (design-decisions §5), and coverage statistics over the 1,645 `kb/disorders/`
  entries (measured 2026-07-30).
- **Live check:** ran `uv run python -m dismech.compare.d2p audit
  kb/disorders/Marfan_Syndrome.yaml` against the Monarch association API to
  confirm the phenotype-gap tooling works and to quantify a representative
  disease.

### DisMech current coverage (1,645 disorders)

| Section | Coverage |
|---|---|
| `disease_term` (MONDO) | 1,626 (98%) |
| `pathophysiology` (causal pathograph) | 1,640 (99%) |
| `phenotypes` (HP-bound) | 1,643 (99%) |
| `genetic` (gene–disease) | 1,357 (82%) |
| `treatments` | 1,566 (95%) |
| `biochemical` | 603 (36%) |
| `differential_diagnoses` | 405 (24%) |
| `clinical_trials` | 340 (20%) |
| `histopathology` | 291 (17%) |

Comorbidity/trajectory associations live in `kb/comorbidities/` (17 files, using
`ICEES`, `COHD`, `DISEASE_TRAJECTORIES`, and literature sources), not on the
disorder files.

## Category-by-category map

Legend: **✅ modeled** · **◐ partial / different granularity** · **○ absent** ·
**⛔ deliberately out of scope**

| Monarch KG edge category | Source(s) | DisMech status | Notes |
|---|---|---|---|
| Disease → Phenotype | HPOA | ✅ / under-covered | Curated subset per disease; gap is *completeness*, tooled by `compare.d2p`. |
| Gene → Disease (causal) | HPOA, Alliance, (ClinGen via structured sources) | ✅ 82% | `genetic:` section + `relationship_type`; gap is *coverage*, tooled by `compare.g2p`. |
| Gene → Phenotype | HPOA, Alliance | ◐ | Phenotypes attach to the *disease*, not to genes directly. |
| Gene → GO (function/process/component) | GO | ◐ | GO terms attach to *pathophysiology nodes* as mechanism, not as gene annotations. |
| Gene → Pathway | Reactome | ◐ | Pathway captured as `biological_processes`; no Reactome IDs. |
| Gene ↔ Gene interaction | BioGrid, STRING | ○ / ⛔ | Only mechanism-relevant interactions belong in a pathograph, with evidence. |
| Gene orthology (cross-species) | Panther | ○ | Not modeled; model-organism data enters as evidence only. |
| Gene expression → Anatomy | BGee | ○ | `located_in` (UBERON) is curated by mechanism, not expression atlases. |
| Model-organism phenotype | ZFIN, Pombase, Alliance | ◐ (as evidence) | Captured via `evidence_source: MODEL_ORGANISM`, not as structured MP/ZP nodes. |
| Disease → Disease (subclass backbone) | Phenio/MONDO | ⛔ | Design decision §4: DisMech **does not re-implement MONDO**; uses curated `groupings`. |
| Disease → Disease (comorbidity) | — (DisMech-specific) | ✅ | `kb/comorbidities/` w/ ICEES/COHD/DisTraj — Monarch KG has *no* comorbidity edges. |
| Variant → Disease | (ClinVar, not in current ingest) | ◐ | DisMech models variant *categories*/ACMG significance, not variant instances. |

### What DisMech has that Monarch KG does *not*

The relationship is bidirectional. DisMech's differentiators — none of which
exist in Monarch KG — are: **mechanistic causal pathographs** (node chains with
directional `downstream` edges and hypothesis grouping), **mechanism modules +
conformance**, **exact-quote-validated evidence**, **mechanism-linked treatments**
(target mechanisms, ASO detail, named regimens), **structured prevalence /
reference ranges / clinical trials**, and **statistically-backed comorbidity /
trajectory** entries. DisMech already **feeds back** to the Monarch ecosystem via
`export/hpoa_export.py`, `export/mondo_emc_export.py`, and the KGX exporter.

## Worked example — Marfan syndrome phenotype gap

`compare.d2p audit` against the Monarch API classified **116** issues for
`MONDO:0007947`, in three actionable buckets:

- **`source_phenotype_missing_locally`** — OMIM/Orphanet-backed HP terms with no
  local phenotype at all (e.g. *Motor delay* HP:0001270, *Retinal detachment*
  HP:0000541, *Osteoporosis* HP:0000939, *Ventricular tachycardia* HP:0004756).
- **`source_phenotype_covered_only_by_broader_local_term`** — DisMech asserts a
  parent term where the source has a more specific one (e.g. local *Myopia*
  HP:0000545 vs source *High myopia* HP:0011003).
- **`local_phenotype_unlinked_to_pathograph`** — DisMech *has* the phenotype but
  it is not wired into a causal `downstream` edge (e.g. *Mitral regurgitation*,
  *Dural ectasia*).

This pattern generalizes across the KB and is the single largest concrete,
in-scope, machine-discoverable source of Monarch-vs-DisMech deltas.

## Recommendations

### Tier 1 — In scope, high value, already tooled (act now)

1. **Systematic disease→phenotype completeness sweep.** Run
   `dismech.compare.d2p audit_all` across the KB and triage the
   `source_phenotype_missing_locally` and
   `source_phenotype_covered_only_by_broader_local_term` rows. Prioritize
   phenotypes the existing pathograph can mechanistically explain (so they can be
   added *linked*, not just listed). Follow the existing evidence SOP — a
   source-backed HP term still needs an exact-quote PMID/ORPHA snippet before it
   lands as a top-level phenotype.
2. **Close `local_phenotype_unlinked_to_pathograph` gaps.** These need no new
   external content — they are DisMech phenotypes that should be connected into
   the causal graph with an evidence-backed `downstream` edge. This directly
   raises DisMech's mechanistic value over Monarch's flat associations.
3. **Gene→disease coverage sweep.** Run `dismech.compare.g2p compare_all` against
   the EBI gene2phenotype release (the tool already downloads it) to surface
   `NO_DISMECH_MATCH` / `UNDERREPRESENTED_IN_DISMECH` genes, then feed
   MONDO-diseases-not-yet-curated into `dismech-mondo-prioritize` (which already
   scores by ClinGen definitive-gene counts).
4. **Disease-level coverage.** DisMech curates 1,645 of the tens of thousands of
   MONDO disease classes. Keep using `mondo_priority` to rank the next entries;
   this is coverage-by-design, not a defect.

### Tier 2 — Structured enrichment of existing slots (opportunistic)

5. **Reactome pathway IDs / GO gene-function annotations** could enrich
   `biological_processes` / `molecular_functions` on pathophysiology nodes. Do
   this **per-entry, evidence-first**, not as a bulk import — bulk GO/Reactome
   gene annotations would dilute the mechanism-first, curated character.
   Low-to-medium priority.

### Tier 3 — New content *types* (evaluate against scope; mostly decline)

6. **Cross-species model-organism *phenotypes* (ZFIN/Alliance/Pombase).** This is
   the one genuinely-missing content *type* with mechanistic value. Today these
   enter only as free evidence. A structured, optional model-organism phenotype
   block (MP/ZP terms + ortholog gene + human-phenotype mapping) is a **defensible
   schema follow-up** — but note it overlaps the existing `HUMAN_MODEL_MISMATCH`
   discussion pattern, which already exists precisely to flag model→human
   translation uncertainty. Recommend scoping as an issue, not building now.
7. **Gene orthology (Panther), gene–gene interactions (BioGrid/STRING), gene
   expression atlases (BGee).** Recommend **do not import.** These are generic,
   gene-centric association layers with no per-disease mechanistic narrative;
   importing them would recreate Monarch KG inside DisMech and violate the
   mechanism-first / "not a re-implementation" scope decisions. Where a specific
   interaction *is* mechanistically load-bearing, it already belongs in a
   pathograph node with its own evidence.
8. **Variant instances (ClinVar).** Stay at the current variant-*category*/ACMG
   granularity. Individual variant records are patient/allele-level data outside
   DisMech's mechanism scope (cf. the individual-data decision).

### Cross-cutting

9. **Stand up a recurring "Monarch gap scan."** DisMech already runs scheduled
   agentic workflows (`knowledge-gap-scan`, `curation-scanner`). A sibling
   workflow that runs `d2p audit_all` + `g2p compare_all` + `mondo-prioritize`
   and posts a ranked worklist would convert this one-off analysis into a
   standing feed. The comparison CLIs already exist; only the workflow wrapper is
   new.
10. **Finish the export-side gaps** so DisMech's mechanism content is fully
    visible *to* Monarch: `differential_diagnoses` / `diagnosis` are not yet in
    the KGX export ([#2100](https://github.com/monarch-initiative/dismech/issues/2100)).

## Bottom line

There is no large hidden reservoir of Monarch KG content that DisMech "should"
absorb wholesale — that would fight its design. The real, actionable gap is
**depth within the categories DisMech already owns** (phenotype completeness +
pathograph linkage + gene/disease coverage), all of which is already discoverable
with the in-repo `compare/` tooling. The only new *type* worth a schema
conversation is structured cross-species model-organism phenotype capture, and
even that should be weighed against the deliberate "evidence, not nodes" policy
for model-organism data.

## References (in-repo)

- `src/dismech/compare/d2p.py` — disease→phenotype audit vs Monarch OMIM/Orphanet.
- `src/dismech/compare/g2p.py` — gene→disease coverage vs gene2phenotype.
- `src/dismech/compare/mondo_priority.py` — MONDO curation prioritization.
- `src/dismech/export/kgx_export.py`, `hpoa_export.py`, `mondo_emc_export.py` —
  DisMech → Monarch-ecosystem exports.
- [Design decisions §4 (ontology / not re-implementing MONDO), §5 (BioLink at
  export layer only)](../explanation/design-decisions.md).
