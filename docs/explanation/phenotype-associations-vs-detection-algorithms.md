# Phenotype Associations vs. Detection Algorithms

Two knowledge layers in a dismech entry describe a disease's phenotypes, and they
answer *opposite* questions. This note contrasts them so curators keep the two
distinct — a distinction that recurs for every disease that carries both a
`phenotypes:` block and a `definitions:` block (a computable case definition).
Familial hypercholesterolemia (FH) is the worked example throughout.

## The core distinction: direction of inference

| | HPOA-style phenotype associations (`phenotypes:`) | Detection algorithms (`definitions:` with `definition_type: PHENOTYPE_ALGORITHM`) |
|---|---|---|
| **Encodes** | **P(phenotype \| disease)** — given the disease, what features appear, and how often | **P(disease \| data)** — given a patient's data, is this the disease |
| **Direction** | Forward (disease → feature); **descriptive** | Backward (features → disease); **discriminative / ascertainment** |
| **Question** | What does the disease look like? | Which patients probably have the disease? |
| **Quantity attached** | Frequency within disease (`FrequencyEnum`: `OBLIGATE`, `VERY_FREQUENT`, …) | Discriminative weight / likelihood: point scores, model coefficients, ML feature importance, PPV/AUC |
| **Feature vocabulary** | HP ontology terms only | HP-mappable features **plus** numeric lab cutoffs, ICD codes, medication records, data trajectories, healthcare-utilization signals |
| **Values** | Qualitative HP terms | Operational thresholds (e.g. LDL-C ≥190 mg/dL) |
| **Exclusion logic** | None — a union of observed features | Explicit (e.g. rule out secondary causes) |
| **Provenance** | Literature / expert curation, aggregated over the disease | Real EHR/claims cohorts, statistically validated |

## The key asymmetry: frequency ≠ discriminative weight

The single most important point is that **a feature's frequency in the disease
and its value for detecting the disease are different axes**, and both
representations are correct on their own axis. Detection algorithms effectively
re-weight the phenotype spectrum by *specificity / likelihood ratio*, not by
prevalence-within-disease.

FH makes this vivid (weights below are from the Dutch Lipid Clinic Network score,
which the FH `definitions:` block operationalizes):

| Feature | Frequency in FH (`phenotypes:`) | Weight for detecting FH (DLCN) |
|---|---|---|
| Hypercholesterolemia (raw high cholesterol) | `OBLIGATE` (~100%) | **Low** — common in the general population, weakly discriminative |
| Very high LDL-C (e.g. ≥ ~325 mg/dL) | — (a threshold, not an HP term) | **8 / max** |
| Tendon xanthoma | `FREQUENT` / `OCCASIONAL` | **6** — near-pathognomonic |
| Pathogenic *LDLR/APOB/PCSK9* variant | (modeled in `genetic:`, not a phenotype) | **8** |

Hypercholesterolemia is *obligate* yet *poorly discriminative*; tendon xanthoma
is only occasional yet *highly discriminative*. A representation optimized for one
axis is the wrong tool for the other.

## What each layer holds that the other cannot

- **Only the phenotype associations have** the long tail of pleiotropic / rare
  features — for FH (HoFH), optic neuropathy, hepatic/renal/myocardial steatosis,
  arthralgia. Detection algorithms drop these because they add little
  discriminative power.
- **Only the detection algorithms have** numeric thresholds, exclusion criteria,
  family-history / pedigree variables, non-phenotypic administrative signals
  (diagnosis codes, medication records), and — for ML models such as FIND FH —
  emergent, clinically-uninterpretable features. None of these are representable
  as an HPOA annotation.
- **The shared core** (the intersection) is exactly the *discriminative*
  phenotypes: for FH, high LDL-C, tendon xanthoma, corneal arcus, premature CAD,
  family history. Point-score algorithms that operationalize published clinical
  criteria (DLCN, Simon Broome) are the **bridge** — they are HPOA-style
  phenotypes plus numeric thresholds and family history, assembled into a rule.
  Statistical models (FAMCAT) depart from that by re-weighting; ML models
  (FIND FH) depart the most.

## Where the pathograph fits

Neither HPOA associations nor detection algorithms explain *why* a feature is
discriminative. The dismech **pathograph** does: it is the causal layer that
connects the descriptive and the diagnostic. In FH, tendon xanthoma and corneal
arcus both trace to a single *Extra-arterial Cholesterol Deposition* node driven
by the obligate LDL elevation — so their shared cause is exactly what makes them
jointly informative for detection. An entry that carries all three layers holds
three complementary views of one disease:

1. **Mechanism** — the pathograph (gene defect → ↑LDL → atherosclerosis /
   extra-arterial deposition → phenotypes);
2. **Phenotype spectrum** — the `phenotypes:` block (P(phenotype | disease) +
   frequency + evidence);
3. **Computable detection** — the `definitions:` block (P(disease | data), with
   thresholds, weights, and validation metrics).

## Curation guidance

- **Do not import a detection algorithm's variable list into `phenotypes:`.**
  LDL-C thresholds, ICD codes, and family-history variables are not phenotype
  associations; they belong in a `definitions:` block.
- **Do not infer frequency from an algorithm's weight, or a weight from
  frequency.** They are different quantities; each needs its own evidence
  (see [`frequency-evidence-guidelines`](../frequency-evidence-guidelines.md)).
- **Record detection algorithms as `definitions:` entries** with
  `definition_type: PHENOTYPE_ALGORITHM`, a `derivation_basis`, and a
  `validation_status` carrying the reported metric (PPV/AUC). See the FH entry
  (`kb/disorders/Familial_Hypercholesterolemia.yaml`) for worked DLCN/PheKB,
  FAMCAT, and FIND FH examples, and
  [`hypothesis-based-phenotype-algorithms`](../hypothesis-based-phenotype-algorithms.md)
  for the epistemic-grounding fields.
- **Keep the discriminative core mechanistically anchored.** When a phenotype is
  both frequent-and-discriminative, it should be reachable in the pathograph so
  its diagnostic value has a causal explanation.
