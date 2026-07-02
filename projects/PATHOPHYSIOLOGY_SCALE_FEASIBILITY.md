---
title: Pathophysiology `biological_scale:` Slot Feasibility Analysis
status: COMPLETE
description: >-
  Three-pass LLM classification survey across 91 pathophysiology nodes from 8
  disorders to test whether a small `biological_scale:` enum (MOLECULAR /
  CELLULAR / TISSUE / ORGANISM) is viable as an incremental addition to the
  pathograph schema. Finding: 4-value scale-only enum works; no STATE additions
  needed; ~41% of sampled nodes are bundle candidates that the slot would
  surface. (Working name during the analysis was `kind:`; renamed on completion
  once the enum's scale-only nature was confirmed — see historical note in the
  report body.)
tags: [SCHEMA_EVOLUTION, PATHOPHYSIOLOGY, FEASIBILITY_ANALYSIS]
diseases:
  - APL_PML_RARA
  - Ayme-Gripp_Syndrome
  - Blau_Syndrome
  - Endometriosis
  - Familial_Hypercholesterolemia
  - Parkinsons_Disease
  - Phenylketonuria
  - Wilms_Tumor
---

# Pathophysiology `biological_scale:` Survey — Final Report

**Sample:** 91 pathophysiology nodes across 8 dismech disorders, each classified three times under different prompt specifications.
**Classifier:** Sonnet 4.6 via subagents.
**Raw data:** [pass1-sonnet-all.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass1-sonnet-all.csv), [pass2-sonnet-all.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass2-sonnet-all.csv), [pass3-sonnet-all.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass3-sonnet-all.csv).

**Naming note.** The slot was called `kind:` throughout the analysis (which is what appears in the classifier prompts, CSV column names, and design doc). The analysis concluded that the four values encode biological scale only — not "kind of thing" in a broader sense — so the slot was renamed `biological_scale:` on completion. Historical references to "kind" in artifact filenames (`primary_kind` CSV column, `classifier-prompt.md`) are intentionally preserved to keep the analysis reproducible. Prose in this report uses `biological_scale:` where it refers to the current recommendation and "kind" where it describes what the classifier did at time of run.

## What this analysis answered

The proposed `biological_scale:` slot on `Pathophysiology` (an additive incremental improvement to the dismech pathograph model, worked on under the working name `kind:`) needed two design questions answered before implementation:

1. **Does a small enum cover real pathophysiology nodes?** And if so, how many values?
2. **Does forcing a single-kind assignment usefully surface bundled nodes that should be split?**

The three-pass survey answered both: **yes, four scale-only kinds suffice** (MOLECULAR / CELLULAR / TISSUE / ORGANISM), and **yes, ~41% of nodes in the sample are bundle candidates** that the slot would surface.

## Three passes, three prompts

| Pass | Enum | Prompt focus | Hypothesis tested |
|---|---|---|---|
| 1 (v1) | 4 process-named: MOLECULAR_ACTIVITY / CELLULAR_PROCESS / TISSUE_PROCESS / ORGANISM_PROCESS | Calibrated for confidence/split independence | Baseline: do the 4 kinds cover the corpus? |
| 2 (v2) | 4 scale-only: MOLECULAR / CELLULAR / TISSUE / ORGANISM | Same as v1 + states explicitly in-scope for each kind | Does renaming eliminate the state-vs-process ambiguity surfaced in v1? |
| 3 (v3) | 4 scale-only (same as v2) | Same as v2 + sharpened split-detection as a co-equal task | Was v2's collapse in split rate a real signal or a prompt-attention artifact? |

## Three-pass headline

| Metric | Pass 1 (v1) | Pass 2 (v2) | Pass 3 (v3) |
|---|---:|---:|---:|
| Ambiguous (conf ≤ 3) | 29% | **4%** | 23% |
| Proposes new kind | 4% | **0%** | **0%** |
| Split candidate | 41% | 4% | **41%** |
| Avg confidence | 3.95 | 4.52 | 3.99 |

**Two cleanly separated findings:**

- **Renaming the enum to be scale-only (v1 → v2) eliminated the state-vs-process taxonomy problem.** New-kind proposals went from 4 to 0 and stayed at 0 across passes 2 and 3. State-shaped nodes (Ectopic Endometrial Tissue, Persistent Blastemal Progenitor State, Hyperphenylalaninemia, Elevated Circulating LDL) all landed cleanly when the suffixes that pre-judged process-vs-state were removed.

- **Sharpening the prompt to treat split detection as a co-equal task (v2 → v3) recovered the bundle-surfacing signal.** Split rate returned to 41% — identical to pass 1's number — confirming that v2's 4% was a prompt-attention artifact (agents anchored on "this is clean now"). The split-detection value of the `biological_scale:` slot is real and substantial.

## Per-disorder breakdown (Pass 3, final)

| Disorder | n | MOL | CEL | TIS | ORG | Ambig | Splits |
|---|---:|---:|---:|---:|---:|---:|---:|
| APL_PML_RARA | 7 | 2 | 2 | 1 | 2 | 14% | 57% |
| Ayme-Gripp_Syndrome | 3 | 2 | 0 | 0 | 1 | 33% | 67% |
| Blau_Syndrome | 6 | 1 | 0 | 5 | 0 | 67% | 67% |
| Endometriosis | 10 | 2 | 2 | 6 | 0 | 40% | 80% |
| Familial_Hypercholesterolemia | 17 | 5 | 3 | 7 | 2 | 12% | 24% |
| Parkinsons_Disease | 20 | 4 | 7 | 7 | 2 | 25% | 30% |
| Phenylketonuria | 17 | 10 | 0 | 3 | 4 | 6% | 24% |
| Wilms_Tumor | 11 | 6 | 4 | 1 | 0 | 27% | 45% |
| **Total** | 91 | 32 (35%) | 18 (20%) | 30 (33%) | 11 (12%) | **23%** | **41%** |

Histogram is balanced — every kind has population, none dominates. Split rate varies widely by disorder (24-80%) — curators differ substantially in how atomically they decompose pathology.

## The state-vs-process finding (resolved)

Pass 1 flagged 4 explicit new-kind proposals, all variations on `*_STATE`:

| Pass-1 node | Pass-1 forced kind | Proposed new kind | Pass-3 kind (with scale-only enum) |
|---|---|---|---|
| Ectopic Endometrial Tissue | TISSUE_PROCESS (conf 2) | PATHOLOGICAL_STATE | **TISSUE (conf 5)** |
| Biallelic PAH Pathogenic Variant Burden | MOLECULAR_ACTIVITY (conf 3) | GENETIC_STATE | **MOLECULAR (conf 5)** |
| Residual PAH Activity and BH4 Responsiveness | MOLECULAR_ACTIVITY (conf 3) | GENETIC_STATE | **MOLECULAR (conf 4)** |
| Persistent Blastemal Progenitor State | CELLULAR_PROCESS (conf 3) | CELLULAR_STATE | **CELLULAR (conf 5)** |

Plus agent-narrated state nodes (METABOLIC_STATE for Hyperphenylalaninemia, MOLECULAR_STATE for elevated LDL, ECOLOGICAL_STATE for gut dysbiosis) all became clean ORGANISM calls under the scale-only enum.

The insight: the v1 names suggested processes were the noun. Renaming made the substrate's biological scale the noun, and "process vs. state" became a verb-level detail — handled by the node's description and the existing `modifier:` slot.

## The bundle/split finding (~41% of nodes)

Pass 3 confirmed pass 1's 41% rate (37/91 nodes flagged as split candidates) on the same 91-node sample, with strong but not identical overlap (24 nodes flagged by both passes, 13 unique to each).

**Bundle patterns the agents named, by frequency in pass 3:**

| Pattern | Frequency | Worked example |
|---|---|---|
| Etiology bundled with consequence | most common | "PML-RARA Fusion Oncogene Formation" (APL) bundles t(15;17) translocation with fusion protein's repressor activity |
| Multi-step pathway compressed | common | "Brain Phenylalanine Toxicity" (PKU) bundles toxicity mechanism with white matter injury, microcephaly, encephalopathy, seizures |
| Multi-organ enumeration | frequent | "Multisystem developmental defects in lens, ear, brain, and growth" (Ayme) bundles 4 separate organ malformations |
| Conjunctions in node name ("and", "&") | reliable trigger | "Stabilized MAF protein **and** dysregulated transcriptional programs" (Ayme), "Hypoxia **and** Angiogenesis" (Endo) |
| Mechanism + outcome bundled | common in cancer | "TP53-Deficient Anaplastic Progression" (Wilms) bundles molecular tumor-suppressor loss with tissue-level histological evolution |

Per-disorder split rates from pass 3 vary from 24% (PKU, FH) to 80% (Endometriosis). **Curators differ substantially in atomicity** — the `biological_scale:` slot's split-surfacing value will be higher for some disorders than others.

## Representative examples

### Clean exemplars (high-confidence, atomic) per kind

| Kind | Example | Why clean |
|---|---|---|
| MOLECULAR | **Transcriptional Repression of Differentiation Genes** (APL) | PML-RARA recruits NCoR/SMRT/HDAC at RA response elements — canonical TF-corepressor activity |
| MOLECULAR | **APOB-LDLR Binding Defect** (FH) | Specific molecular interaction failure |
| CELLULAR | **Autophagy-Lysosome Pathway Dysfunction** (Parkinson) | Impaired intracellular protein degradation, cell-intrinsic |
| CELLULAR | **Macrophage-Derived Foam Cell Formation** (FH) | Macrophage lipid accumulation drives differentiation into foam cells |
| TISSUE | **Granulomatous Inflammation** (Blau) — kind clean even though bundle | Non-caseating epithelioid granulomas, tissue-level architecture |
| TISSUE | **Wilms Tumor Outgrowth** (Wilms) | Neoplastic mass formation in renal blastemal tissue |
| ORGANISM | **Coagulopathy** (APL) | DIC + hyperfibrinolysis spanning the entire vascular compartment |
| ORGANISM | **Hyperphenylalaninemia** (PKU) | Systemic metabolite accumulation, hub for downstream edges |

### Splits where pieces land cleanly (validation that splits don't just shift the problem)

11 atomic pieces from 4 batch-1 bundles were independently classified ([split-pieces.md](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/split-pieces.md)). 7 of 11 (64%) landed at confidence ≥ 4 in a single kind. The 2 pieces still proposing new kinds were both `*_STATE` variants that the v2 enum subsequently absorbed:

| Bundle | Splits into | Outcome under v2/v3 enum |
|---|---|---|
| **Visceral and Vascular Involvement** (Blau) | (1) Granulomatous ILD, (2) Systemic Vasculitis, (3) Hepatic/Renal Granulomatous Involvement | All 3 pieces → TISSUE, conf 4-5 |
| **Stabilized MAF + Dysregulated Programs** (Ayme) | (1) MAF Stabilization, (2) Aberrant MAF Transcriptional Activity | Both → MOLECULAR, clean under scale-only |

### Deep-split (bundles whose pieces themselves bundle)

| Bundled node | First split | Pieces still bundled |
|---|---|---|
| **Multisystem developmental defects in lens, ear, brain, and growth** (Ayme) | Lens defect / Auditory defect / Neurodev impairment / Growth+craniofacial | "Neurodev impairment" bundles brain morphology vs. behavioral outcome; "Growth+craniofacial" bundles whole-body growth vs. local skull morphology |

### Edge cases — genuine substrate-boundary ambiguity

These are nodes any 4-bucket enum would find hard, and the survey is honest about them:

- **Competitive LNAA Transport at the Blood-Brain Barrier** (PKU) — molecular kinetics at an anatomical structure
- **Vagal-Brainstem Alpha-Synuclein Propagation** (Parkinson) — prion-like cell-to-cell mechanism routed through anatomical conduits
- **Canonical Wnt Signaling Hyperactivation** (Wilms) — pathway-level signaling, MOLECULAR vs CELLULAR genuine tie
- **PCSK9 Gain-of-Function vs PCSK9-Mediated LDLR Degradation** (FH) — adjacent nodes covering one gene at different scales (variant vs. consequence)

## Conclusion and recommendation

**Land the 4-value scale-only optional enum on `Pathophysiology`:**

```yaml
BiologicalScaleEnum:
  permissible_values:
    MOLECULAR: "Pathology at molecular scale — activities or states of molecules,
                complexes, or genetic elements"
    CELLULAR:  "Pathology at cellular scale — processes or states of a cell type
                or single cell"
    TISSUE:    "Pathology at tissue/organ scale — processes or states of a tissue,
                organ, or anatomical structure"
    ORGANISM:  "Pathology at organism scale — systemic / multi-organ / whole-body
                processes or states"
```

### Why this works

1. **Coverage** — 91/91 nodes in the sample fit one of these 4 kinds with zero new-kind proposals across two passes.
2. **Confidence** — average classifier confidence 4.0+, with most residual ambiguity at genuine substrate-boundary cases that no enum would resolve.
3. **No structural commitment** — slot is optional; legacy 958 disorders work unchanged.
4. **Heuristic backfill** — for legacy nodes, a deterministic script can infer `biological_scale:` from existing descriptor slot usage (presence of `molecular_functions` → MOLECULAR; `cell_types` + `biological_processes` without anatomy → CELLULAR; etc.) for the confident cases.
5. **Side benefit: node hygiene** — 41% of sampled nodes are bundle candidates. The slot's forced single-value assignment, combined with curator awareness of split patterns (etiology+consequence, multi-organ enumeration, conjunctions), creates pressure toward atomic decomposition that no other slot currently provides.

### What we did *not* recommend

- **Adding STATE kinds.** Pass 1 implied this was needed; passes 2/3 showed it was a v1 naming artifact.
- **Splitting `Pathophysiology` into multiple classes.** A single optional tag is far less disruptive than class-level decomposition.
- **Multi-value (multivalued `biological_scale:`).** Single-value assignment is the friction that surfaces bundles. Multi-value would lose this.

### Caveats

- **Sample is 8 disorders / 91 nodes**, biased toward recently curated and toward mature/well-decomposed pathographs. A larger or differently-sampled corpus (older curations; thin pathographs; non-Mendelian conditions) may surface different patterns.
- **Classifier is LLM** (Sonnet 4.6). Calibration check with Opus 4.7 on the batch-1 16 nodes showed 94% primary-kind agreement after rename mapping; the methodology is not model-fragile but the absolute numbers carry the usual single-classifier caveats.
- **The 41% split rate is what the classifier surfaced**, not what a human reviewer would necessarily agree with. The batch-1 split-piece validation (where 7 of 11 hypothesized pieces landed cleanly) is the strongest evidence the splits aren't classifier hallucination, but a human-curator review pass would tighten this.

## Files

- [classifier-prompt.md](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/classifier-prompt.md) — v1 spec (process-named enum, calibrated for confidence/split independence)
- [classifier-prompt-v2.md](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/classifier-prompt-v2.md) — v2 spec (scale-only enum)
- [classifier-prompt-v3.md](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/classifier-prompt-v3.md) — v3 spec (scale-only + sharpened split detection)
- [pass1-sonnet-all.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass1-sonnet-all.csv) — v1 results (91 nodes)
- [pass2-sonnet-all.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass2-sonnet-all.csv) — v2 results (91 nodes)
- [pass3-sonnet-all.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass3-sonnet-all.csv) — v3 results (91 nodes, the authoritative pass)
- Per-disorder per-pass CSVs in same directory
- [split-pieces.md](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/split-pieces.md) — split-piece validation from batch 1 (11 atomic pieces from 4 bundles)
- [pass1-results.csv](PATHOPHYSIOLOGY_SCALE_FEASIBILITY/pass1-results.csv) — initial Opus inline pass (kept for record, superseded)
