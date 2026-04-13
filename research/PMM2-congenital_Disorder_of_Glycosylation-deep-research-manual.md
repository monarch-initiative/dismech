# PMM2-congenital disorder of glycosylation deep research

## Scope decision

- Curated entity: `MONDO:0008907` PMM2-congenital disorder of glycosylation.
- Disease framing: classical multisystem PMM2-CDG / historical CDG-Ia.
- Explicitly excluded from this root: the distinct PMM2 promoter-related hyperinsulinism/polycystic-kidney phenotype, because its tissue-restricted presentation and mechanistic framing differ from the canonical type I N-glycosylation disorder.

## Main mechanistic story

1. PMM2 pathogenic variants reduce phosphomannomutase activity.
   Supporting PMID: `26014514`.
   Key abstract sentence: PMM2-CDG is caused by PMM2 mutations that reduce phosphomannomutase 2 activity.
2. Reduced PMM2 activity lowers conversion of mannose-6-phosphate to mannose-1-phosphate.
   Supporting PMID: `39053125`.
   Key abstract sentence: PMM2 converts M6P to M1P, a critical upstream metabolite for proper protein N-glycosylation.
3. Lower mannose flux into glycosylation causes underoccupied N-glycosylation sites.
   Supporting PMID: `21949237`.
   Key abstract sentence: PMM2 deficiency reduces mannose-6-phosphate flux into glycosylation, resulting in unoccupied N-glycosylation sites.
4. Downstream vascular consequences are experimentally supported.
   Supporting PMID: `35717947`.
   Findings used in YAML: reduced activated protein C generation and impaired endothelial monolayer integrity after PMM2 knockdown.

## Genetics and modifier takeaways

- Large cohort anchor: PMID `40225925` (`n=137`, `60` unique variants).
- Common allele in the multicenter cohort: `p.Arg141His` in `58.4%`.
- Modifier evidence worth carrying into YAML:
  - `p.Cys241Ser` associated with milder disease.
  - `p.Val231Met` associated with more severe disease.
  - Folding and dimerization-class variants also tracked with greater severity.
- Take-home framing: genotype effects are better modeled by mutation mechanism classes (catalysis/activation, folding, dimerization) than by a single binary severe/mild split.

## Phenotype curation choices

- Strong neurologic anchors came from PMID `37955240` and PMID `39105373`.
- Added with direct frequency support:
  - developmental delay
  - ataxia
  - seizures
  - peripheral neuropathy
  - stroke-like episodes
- Added with qualitative frequency mapping:
  - cerebellar atrophy as a characteristic imaging finding
  - growth delay as a common phenotype
  - hepatomegaly as a frequent hepatic manifestation
- Added without forcing a frequency band:
  - hypotonia
- Deliberately not overexpanded in YAML:
  - broad ophthalmologic abnormalities
  - endocrine manifestations
  - skeletal deformities
  - retinitis pigmentosa
  These are real parts of the literature but I left them out of the first pass unless the abstract evidence was direct enough for a clean disease-level assertion.

## Treatment landscape

- Included in YAML:
  - `Acetazolamide` for symptomatic neurologic treatment.
    Anchor PMID: `37955240`.
    Rationale: direct human follow-up data; benefit was partial, so evidence is marked `PARTIAL`.
  - `Liver transplantation` as rescue treatment for end-stage liver disease.
    Anchor PMID: `36965289`.
    Rationale: human case report with clear post-transplant biochemical improvement.
  - `GLM101` / liposomal mannose-1-phosphate as an experimental substrate-replacement concept.
    Anchor PMID: `39053125`.
    Rationale: strong preclinical fibroblast rescue, but still `IN_VITRO` only.
- Intentionally not included in YAML:
  - `D-galactose` and `oral mannose` were reviewed during literature collection, but I did not include them in the disease entry because the evidence base is mixed and I did not need them to achieve a coherent, validator-safe treatment section.

## Evidence sourcing choices

- `HUMAN_CLINICAL`:
  - multicenter natural history and genotype-phenotype studies
  - prospective neurodevelopmental and neurologic cohorts
  - liver-transplant case report
- `IN_VITRO`:
  - mutant-protein functional assays
  - patient-derived fibroblast rescue studies
  - endothelial PMM2 knockdown experiments
- Avoided mixing human and preclinical evidence inside a single evidence item when the abstract made the distinction clear enough to separate.

## References used in the YAML

- PMID `21949237` Phosphomannose isomerase inhibitors improve N-glycosylation in selected phosphomannomutase-deficient fibroblasts.
- PMID `26014514` The Effects of PMM2-CDG-Causing Mutations on the Folding, Activity, and Stability of the PMM2 Protein.
- PMID `28685491` The Prevalence of PMM2-CDG in Estonia Based on Population Carrier Frequencies and Diagnosed Patients.
- PMID `35717947` N-Glycosylation Deficiency Reduces the Activation of Protein C and Disrupts Endothelial Barrier Integrity.
- PMID `36965289` Liver transplantation recovers hepatic N-glycosylation with persistent IgG glycosylation abnormalities.
- PMID `37955240` Neurological manifestations in PMM2-CDG.
- PMID `39053125` In vitro treatment with liposome-encapsulated Mannose-1-phosphate restores N-glycosylation in PMM2-CDG patient-derived fibroblasts.
- PMID `39105373` Neurodevelopmental profiles of 14 individuals with phosphomannomutase deficiency.
- PMID `40225925` Genotype/Phenotype Relationship: Lessons From 137 Patients With PMM2-CDG.
- PMID `40555085` Multiorgan involvement and genetic spectrum of 20 Chinese patients with PMM2-CDG.
