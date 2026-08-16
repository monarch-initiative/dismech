# AADC deficiency publication-readiness review — 2026-08-05

Scope: `kb/disorders/Aromatic_L_Amino_Acid_Decarboxylase_Deficiency.yaml` and
its directly cited reference caches. The review used the existing fallback
research artifact and citation sidecar, all previously cited caches, the 2025
GeneReviews update (PMID:37824694), targeted PubMed/PMC and ClinicalTrials.gov
searches, and literature indexed through 2026-08-05. The newest included
clinical papers are the 2026 GT-002 report (PMID:41724580) and the July 2026
French clinical/imaging cohort (PMID:42389831).

## D2P audit dispositions

The pre-edit audit returned 20 recommendations. Every recommendation was
reviewed against the cited source, the available exact text, its appropriate
section in the disease model, and whether a defensible causal path exists.

| Recommendation | Disposition | Rationale |
|---|---|---|
| HP:0002104 Apnea | Not promoted | The suggested 54.5% derives from an 11-person historical source mapping that is not stated in the cached abstract. GeneReviews discusses obstructive sleep apnea management but does not supply a disease-wide frequency. |
| HP:0002305 Athetosis | Added, no population frequency | PMID:12891654 explicitly reports generalized athetosis in its 11 patients. The small selected cohort does not justify extrapolating 100% to all AADC deficiency. |
| HP:0006543 Cardiorespiratory arrest | Not promoted | The source mapping represents a severe complication in a very small historical cohort, not a stable common phenotype. Mortality and severe autonomic risk are represented in prognosis without inventing a routine causal edge. |
| HP:0001266 Choreoathetosis | Not added as a duplicate composite | Athetosis and dyskinesia are now represented directly. The source-backed abstract says generalized athetosis, not the composite HPO term. |
| HP:6001002 Elevated urinary vanillactic acid level | Added under `biochemical`, not `phenotypes` | The consensus supports urinary VLA as a subtle, non-exclusionary diagnostic biomarker. Section placement preserves its role as a readout. |
| HP:0002267 Exaggerated startle response | Not promoted | The D2P percentage is not recoverable from the cited abstract, and the consensus table only marks occurrence without a defensible population frequency. |
| HP:0001347 Hyperreflexia | Not promoted | The D2P percentage is not recoverable from the cited abstract and would sit uneasily beside source-backed reduced tendon reflexes without patient-level reconciliation. |
| HP:0005964 Intermittent hypothermia | Covered by broader HP:0005968 Temperature instability | Exact episodicity and direction are not supported by the cached source. GeneReviews directly supports temperature instability. |
| HP:0001254 Lethargy | Not promoted | In the full consensus text, lethargy is documented as an adverse effect of attempted 5-HTP/COMT-inhibitor treatment; the D2P disease-frequency estimate is not recoverable from the cited abstract. |
| HP:0001336 Myoclonus | Added, no population frequency | The consensus age-stratified table recognizes myoclonus, but available exact text does not support the 72.7% D2P estimate as a general frequency. |
| HP:6000037 Reduced circulating AADC activity | Retained under `biochemical`, not duplicated as a phenotype | Reduced plasma AADC activity was already modeled as a diagnostic readout of the primary enzyme defect. |
| HP:0005968 Temperature instability | Added, no population frequency | GeneReviews explicitly lists it within autonomic dysfunction; no exact source supports a separate numeric frequency. |
| HP:0008936 Axial hypotonia | Broader local term retained | Hypotonia and poor head control are both present and connected. The proposed 100% comes from the small historical source mapping, not exact abstract text. |
| HP:0000643 Blepharospasm | Broader local dystonia retained | No exact cached text establishes blepharospasm or its proposed frequency; adding it would overfit the source mapping. |
| HP:0000712 Emotional lability | Broader behavioral terms retained | Irritability and atypical behavior are directly supported; the proposed 90.9% is not recoverable from the cited abstract. |
| HP:0008872 Feeding difficulties in infancy | Broader feeding-difficulty term retained | Feeding difficulty is directly supported and early onset is modeled in progression. A second age-precoordinated phenotype would be redundant without stronger evidence. |
| HP:0002451 Limb dystonia | Broader dystonia retained | Limb dystonia appears in the 11-patient abstract, but broader dystonia is the stable, multi-source disease assertion and avoids overgeneralizing 100%. |
| HP:0200085 Limb tremor | Broader tremor retained | The proposed limb-specific 63.6% conflicts with Orphanet's very-rare broad tremor assertion and is not stated in the cited abstract. |
| HP:0100703 Tongue thrusting | Not promoted | The proposed 81.8% is not in the cited abstract; mapping this motor sign to the existing broad behavioral term is also not treated as mechanistic evidence. |
| HP:0000473 Torticollis | Broader dystonia retained | The proposed frequency is not recoverable from the cited abstract and the term would duplicate a posture-specific dystonic manifestation. |

The post-edit audit reports 18 items: the three supported missing concepts were
resolved, while a new medium-priority item notes that seizure is deliberately
unconnected. That recommendation is explicitly declined: true seizures occur
in fewer than 5% per GeneReviews, oculogyric crises are commonly mistaken for
epilepsy, and no cited evidence establishes a causal route from the modeled
monoamine/developmental nodes to epilepsy. A fabricated edge would misstate the
evidence merely to raise connectivity.

## Evidence and scope decisions

- Corrected seizure from `FREQUENT` to `VERY_RARE`, replacing the conflicting
  Orphanet frequency evidence with the GeneReviews estimate of fewer than 5%.
- Kept worldwide Orphanet point prevalence separate from population-specific
  prospective newborn-screening estimates in Germany and Taiwan; the Taiwan
  founder-population result is not generalized worldwide.
- Added persistent disability, regression, survival, and caregiver-attributed
  causes of death from the 63-person international cohort. Mortality inference
  is marked `PARTIAL` where the study itself only suggests risk from an
  age-skewed sample.
- Treated GeneReviews and consensus guidance without pooled patient data as
  `OTHER`. The data-bearing systematic review of 261 patients is
  `HUMAN_CLINICAL`, as are prospective screens, cohorts, and trials; mouse and
  cell experiments use `MODEL_ORGANISM` and `IN_VITRO`, respectively.
- Added only direct biomarker readouts and retained screening limitations. DBS
  3-OMD is not represented as a definitive standalone diagnosis; urinary VLA
  is not represented as an exclusionary test.
- Added variant-directed levodopa and low-CSF-5-MTHF-directed folinic acid with
  their conditional boundaries, plus GeneReviews medication-avoidance advice.
- Added completed precursor trials and current 48-week evidence for
  NCT04903288, while preserving the trial's active-not-recruiting status.
- Added a mild S250F mouse and a CRISPR DDC-knockout SH-SY5Y model, with an
  explicit human-model mismatch and proposed isogenic human-neuron experiment.
- Preserved the open long-term/comparative gene-therapy and ascertainment gaps;
  small uncontrolled cohorts do not close them.
