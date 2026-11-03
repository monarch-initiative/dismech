# Can DisMech and NAMO hold what an OECD Test Guideline says?

An OECD Test Guideline describes validated test methods in free text. For that content to
be citable rather than paraphrased, a method's identity, the biology it observes, and its
regulatory standing all have to land in a slot. This table checks one Test Guideline
against the two schemas available, asking for each fact the document states whether
DisMech has a slot, whether NAMO has a slot, and how good the fit is in each.

Companion to [the schema elements a NAM touches](nam-schema-elements.md), which maps the
DisMech side in detail, and to [the NAMO vocabulary gaps met while curating fibrosis
NAMs](namo-vocabulary-gaps-2026-10-13.md), which records the same kind of finding from the
model-system direction rather than the regulatory one. Machine-readable form in
[`oecd-tg442d-schema-coverage-2026-11-02.json`](oecd-tg442d-schema-coverage-2026-11-02.json).
Written 2026-11-02.

**Source document.** OECD Test No. 442D, *In Vitro Skin Sensitisation: Assays addressing
the Adverse Outcome Pathway Key Event on Keratinocyte activation*, adopted 2 July 2026
([10.1787/9789264229822-en](https://doi.org/10.1787/9789264229822-en)). It describes five
test methods across four appendices: KeratinoSens™, LuSens, EpiSensA, Epi2SensA and
α-Sens®. The facts below come from the General Introduction and from each appendix's
*Initial Considerations* and *Principle of the Test* sections.

**Schema versions.** DisMech at `aef740d` (2026-10-31); NAMO at `0a743c5` (2026-08-01).

## Legend

| Symbol | Meaning |
|---|---|
| ✅ | A slot exists whose range and documented purpose fit this fact |
| ⚠️ | A slot exists but the fit is partial — wrong granularity, free text where structure is wanted, or a slot documented for another use |
| ❌ | No slot; the fact can only be carried as prose, or not at all |

## Coverage

| TG 442D fact | DisMech slot | NAMO slot | DisMech | NAMO |
|---|---|---|---|---|
| Method name | `name` | `NamedThing.name` | ✅ | ✅ |
| Cell line and its derivation | `cell_types`, `cell_source` | `CellularSystem.cell_types` / `cell_source`; `CellLineModel.passage_range`, `authentication_method` | ✅ | ✅ |
| Model category (2D line vs reconstructed human epidermis) | `experimental_model_type` enum | class hierarchy (`CellLineModel` vs `ThreeDCellCulture`) plus `biological_organization_level`, `complexity_level` | ⚠️ no RhE value | ✅ |
| Tissue model product (LabCyte EPI-MODEL24, EpiDerm™ EPI-200) | `culture_system`, `tissue_term` | `three_d_architecture`, `matrix_composition` | ✅ free text | ⚠️ no product-identity slot |
| Sensing pathway (Keap1 → Nrf2 → ARE) | readout `biological_processes` (GO-bound) | `Pathway` (`pathway_database`, `pathway_id`) | ✅ | ✅ |
| **Marker genes** (*ATF3*, *IL-8*, *GCLM*, *DNAJB4*) | — | `Gene` (`gene_symbol`, `ensembl_id`, `fold_change`, `p_value`) | ❌ | ✅ |
| Which mechanism the method measures | `modeled_mechanisms[].target` → a pathophysiology node | `ModelsRelationship.biological_system_modeled` | ✅ | ⚠️ not a pathograph node |
| Limitations (no oxidative metabolism, hence the pro-hapten blind spot) | `limitations`, typed `divergences` | `StructuredConcordanceResult` quantifies match but carries no typed caveat | ✅ | ⚠️ |
| Inter- and intra-laboratory reproducibility (~85%) | — | `Reproducibility` | ❌ | ✅ |
| **Performance against the animal reference** (accuracy 77%, sensitivity 78%, specificity 76% vs LLNA) | — | `ModelPerformance` (`accuracy`, `sensitivity`, `specificity`, `auc`) | ❌ | ✅ |
| Numeric cut-offs (EC1.5; *ATF3* 15-fold, *GCLM* 2-fold) | — | `QualityControlMetric.threshold`, `FunctionalAssay.reference_value` | ❌ | ⚠️ repurposable |
| Viability constraint (≥80% EpiSensA, ≥60% Epi2SensA; IC30, IC50) | — | as above | ❌ | ⚠️ repurposable |
| Readout direction | `ExperimentalReadout.direction` enum | `FunctionalAssay.assay_result`, `Gene.fold_change` | ✅ | ⚠️ no direction enum |
| **Test Guideline number and appendix** (442D, Appendix IA) | — | `Reference` only (`id`, `title`, `year`, `url`) | ❌ | ❌ |
| **AOP and key event addressed** (AOP 40, KE2 keratinocyte activation) | — | — (AOPs appear in schema prose only) | ❌ | ❌ |
| **Reporter construct** (luciferase under the ARE of human *AKR1C2*; Firefly Luc+ with Renilla-TK) | — | — | ❌ | ❌ |
| **Validation route** (validated reference method vs Performance-Standards-based) | — | — | ❌ | ❌ |
| **Approving body and its role** (EURL ECVAM / ESAC; JaCVAM; ICATM cooperation) | — | — | ❌ | ❌ |
| Regulatory use (UN GHS Category 1; within an IATA; TG 497 defined approaches) | — | `Study.context_of_use`, free text | ❌ | ⚠️ |
| **Mutual Acceptance of Data status** | — | — | ❌ | ❌ |
| Proficiency substances | — | — | ❌ | ❌ |
| Methods cited but not described (TG 406, 429, 442A, 442B) | — | — | ❌ | ❌ |

## What the two columns say together

**The schemas are complementary, not redundant.** NAMO holds the performance and
gene-expression facts DisMech cannot: `ModelPerformance`, `Reproducibility`, and a `Gene`
class carrying fold-change and significance. DisMech holds the mechanism linkage and the
typed caveats NAMO cannot: a model links to a named pathophysiology node, and its
shortfalls are recorded as classified `divergences` rather than as prose.

**Neither holds a method's regulatory standing.** Eight rows are ❌ in both columns, and
seven of them belong to one group: the Test Guideline identity, the AOP key event, the
validation route, the approving body, Mutual Acceptance of Data, proficiency substances and
cited comparators. That group is what makes a method regulatorily usable rather than merely
scientifically described, and it is what a Test Guideline exists to establish. Nothing in
either schema asserts it today. The eighth row absent in both, the reporter construct, is a
biology fact rather than a regulatory one.

**Two DisMech gaps are narrow and separately fixable.** The model-type enum has no value
for reconstructed human epidermis, so EpiSensA and Epi2SensA would both be typed `OTHER`.
And a DisMech readout cannot name a gene, which matters because four of the five methods in
442D have gene-expression readouts.

**NAMO has OECD only as a prefix.** `OECD:` is declared and used in two example CURIEs.
There is no class for a Test Guideline, no enum for acceptance or validation status, and no
slot for an approving body.

## Caveats on reading this

- One Test Guideline, chosen as a worked case. TG 442C and 442E are built the same way, but
  a Test Guideline from another endpoint area may carry facts this table does not
  anticipate.
- `⚠️ repurposable` in the NAMO column means a slot's range fits but its documented purpose
  names a different use — `QualityControlMetric.threshold` standing in for an EC1.5
  cut-off, for instance. Those are a stretch rather than a fit.
- The table records what the schemas can *hold*. It says nothing about which repository
  should hold it, which is a separate and still-open question.
