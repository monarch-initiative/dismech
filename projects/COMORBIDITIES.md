# Comorbidities and Trajectories (Scoping)

Goal: curate comorbidity/trajectory evidence from the literature (complementary to EHR-derived signals such as Disease Trajectories / Distraj), with directionality when supported. Do **not** start curation yet; this is a scoping log and candidate list.

## Key observations from Disease Trajectories (EHR-based)
- The temporal component is **not dominant**: most edges are "same time" rather than directional.
- If we define a trajectory as "A before B" (or "B before A") with strong directionality, only a minority of edges qualify.

Derived from `tmp/disease-trajectories/*_dis_pair_phase_dict.json`:
- Male: 1,281 edges total; 963 (~75%) same-time dominant; 258 (~20%) strongly directional (>=0.7).
- Female: 1,189 edges total; 973 (~82%) same-time dominant; 170 (~14%) strongly directional (>=0.7).

## Candidate directional edges with GO enrichment (start list)
These are **directional** edges with GO enrichment terms (from `tmp/disease-trajectories/go_enrichment_*.json`) and genetic overlap signal (FDR from `G_elma_icd_*_genetic_fdr_dict.json`). Directional probabilities are from `*_dis_pair_phase_dict.json`.

### Male
| Edge (A -> B) | Phase (A before B) | Genetic FDR | Top GO terms (lowest FDR) |
|---|---:|---:|---|
| E12 -> L28 (Malnutrition-related diabetes mellitus -> Lichen simplex chronicus/prurigo) | 1.0 | 9.82e-80 | Glucose homeostasis; Cellular response to insulin stimulus; Regulation of insulin secretion |
| I10 -> I15 (Essential hypertension -> Secondary hypertension) | 1.0 | 1.14e-31 | Regulation of vasoconstriction; Blood vessel diameter maintenance; Intracellular signaling cassette |
| M54 -> L50 (Dorsalgia -> Urticaria) | 1.0 (B before A in raw file) | 5.71e-05 | Alpha-adrenergic receptor activity; Adrenergic receptor signaling pathway; Positive regulation of signaling receptor activity |

### Female
| Edge (A -> B) | Phase (A before B) | Genetic FDR | Top GO terms (lowest FDR) |
|---|---:|---:|---|
| K21 -> K25 (GERD -> Gastric ulcer) | 1.0 | 8.18e-04 | Regulation of neuroinflammatory response; Positive regulation of acute inflammatory response; Positive regulation of nitric oxide biosynthesis |
| K21 -> K58 (GERD -> Irritable bowel syndrome) | 1.0 | 2.10e-04 | cAMP/cGMP phosphodiesterase activity (multiple PDE terms) |
| F10 -> G93 (Alcohol-related disorders -> Other disorders of brain) | 1.0 | 8.75e-11 | Transmitter-gated ion channel activity; Benzodiazepine receptor activity; Chemical synaptic transmission |

## Scheduling (curation backlog)
- Create curation tasks for each candidate edge above (literature-based, directional if supported).
- Add a second pass to pull additional directional edges with:
  - Phase >= 0.9, and
  - GO enrichment present, and
  - Genetic FDR <= 0.05

## Notes
- This list is **not** evidence; it is a prioritization queue for manual literature curation.
- Disease Trajectories (EHR) is complementary to the dismech model; our goal is mechanistic + evidence-backed comorbidity directionality, not to mirror EHR associations.
