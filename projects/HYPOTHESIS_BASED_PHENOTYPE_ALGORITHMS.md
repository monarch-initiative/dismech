---
title: Hypothesis-Based Phenotype Algorithms & Trigger-Provoked Latent-Disease EHR Case-Finding
status: IN_PROGRESS
description: >-
  Represent computable EHR/OMOP case-finding queries that are predicated on a
  disease mechanism (not just consensus criteria), so a mechanism-derived scan
  for latent/mild carriers is never conflated with a validated phenotype — with
  paired population (EHR biobank) and mechanistic (NAM) tests.
tags: [METHODOLOGY, EHR, PHENOTYPE_ALGORITHM, NAM, CHANNELOPATHY]
diseases:
  - Timothy_Syndrome
  - Brugada_Syndrome
  - Long_QT_Syndrome
  - Malignant_Hyperthermia_of_Anesthesia
phenotypes:
  - id: HP:0001250
    label: Seizure
  - id: HP:0001657
    label: Prolonged QT interval
---

# Hypothesis-Based Phenotype Algorithms & Trigger-Provoked Latent-Disease EHR Case-Finding

## Motivation

A zebrafish Timothy-syndrome study ([#6245](https://github.com/monarch-initiative/dismech/issues/6245),
PMID:42426269) showed that fever elicits arrhythmia and seizures **even in overtly
normal CACNA1C heterozygotes**. That implies a computable idea: scan EHRs for a
new arrhythmia or seizure shortly after a fever, to surface *latent/mild* carriers
a classical case definition would never catch. But such a query is valid only if
the mechanism holds — so running it is simultaneously case-finding **and** a test
of the mechanism. A standard PheKB/OHDSI phenotype library cannot say which of its
algorithms is speculative; DisMech can, because it links the algorithm to the
mechanism.

## The archetype: trigger-provoked latent disease

> A physiological / pharmacological / procedural **trigger** transiently unmasks a
> **latent channel/enzyme defect**. Most carriers are asymptomatic at baseline. An
> EHR query for **trigger-associated events** is enriched for latent carriers, and
> that enrichment tests the mechanism.

## What was built

1. **Schema** (enacted, `@cmungall`-approved) — `Definition` gained
   `derivation_basis` (`ESTABLISHED_CRITERIA` / `MECHANISTIC_HYPOTHESIS` /
   `MODEL_SYSTEM_EXTRAPOLATION`), a structured `validation_status` object
   (`status` + `rationale` + `evidence`), and reuses `attaches_to` to link the
   pathograph node(s) a hypothesis-based algorithm is predicated on. Gated by
   `test_hypothesis_based_definition_attaches_to_foreign_keys`. See
   [the design write-up](../hypothesis-based-phenotype-algorithms.md).
2. **Worked examples** — each carries a `PHENOTYPE_ALGORITHM` case-finding
   definition **and** a NAM confirmation experiment (below).
3. **Candidate register + validation guidance** — see
   [the survey report](../reports/hypothesis-driven-ehr-case-finding-2026-07-12.md).

## Worked examples

| Disease | Trigger | Trigger type | System | `derivation_basis` | Genotype yield of a hit |
|---|---|---|---|---|---|
| Timothy_Syndrome | fever | physiological | cardiac + CNS | `MECHANISTIC_HYPOTHESIS` | (unknown — hypothesis) |
| Brugada_Syndrome | fever | physiological | cardiac | `ESTABLISHED_CRITERIA` | ~26% SCN5A |
| Long_QT_Syndrome | QT-prolonging drug | pharmacological | cardiac | `ESTABLISHED_CRITERIA` | ~10–15% |
| Malignant_Hyperthermia_of_Anesthesia | volatile anesthetic / succinylcholine | procedural | skeletal muscle | `ESTABLISHED_CRITERIA` | 50–>70% |

Timothy_Syndrome is the one genuine `MECHANISTIC_HYPOTHESIS` (zebrafish-derived,
human validity open); the other three are established mechanisms where the *EHR
operationalization* is the new artifact. Together they span emerging↔established
grounding × physiological/pharmacological/procedural triggers × cardiac/muscle.

## Two-armed test strategy: population × mechanistic

Each hypothesis has two complementary tests, both first-class in the schema:

- **Population arm** — the `PHENOTYPE_ALGORITHM` definition run against a
  **genotype-linked EHR biobank** (eMERGE/PheKB, All of Us, UK Biobank; not MIMIC
  — no linked DNA, ICU-confounded). This is what flips `validation_status` to
  `VALIDATED_AGAINST_GOLD_STANDARD`.
- **Mechanistic arm** — a **New Approach Methodology** `proposed_experiment`
  (NAMO-aligned `model_systems`: iPSC-derived cells, organ-on-chip, in-silico).
  For Timothy_Syndrome the NAM *bridges the `HUMAN_MODEL_MISMATCH`* (is the
  zebrafish effect human-relevant?); for the established examples it *functionally
  confirms / risk-stratifies* the carriers the query surfaces (VUS resolution).

| Disease | Mechanistic NAM experiment |
|---|---|
| Timothy_Syndrome | iPSC-CM + iPSC-neuron + heart-on-chip + in-silico hyperthermia challenge (`exp_ts_fever_ipsc_nam_challenge`) |
| Brugada_Syndrome | iPSC-CM + heterologous Nav1.5 temperature ramp (`exp_brs_nav15_temperature_nam`) |
| Long_QT_Syndrome | **CiPA** (in-vitro hERG/multi-channel + in-silico O'Hara-Rudy/ToR-ORd) + iPSC-CM drug challenge (`exp_lqt_cipa_nam_confirmation`) |
| Malignant_Hyperthermia_of_Anesthesia | RyR1 Ca²⁺-release + iPSC-myotube caffeine/4-CmC/halothane challenge, an in-vitro complement to the invasive CHCT (`exp_mh_ryr1_ipsc_calcium_nam`) |

This connects to two adjacent projects: `NAMO_RD_MODELS` (the NAMO bridge) and
`MONDO_EHR_MAPPINGS` (MONDO-driven OMOP concept sets the population arm would use).

## Status & worklist

- [x] Schema extension enacted + gating test + docs (proposal, design-decisions §11, CLAUDE.md)
- [x] Timothy_Syndrome — hypothesis, fever nodes/edges, case-finding definition, HUMAN_MODEL_MISMATCH discussion, NAM experiment
- [x] Brugada_Syndrome — fever-unmasking node, definition, NAM experiment
- [x] Long_QT_Syndrome — drug-unmasking node, definition, CiPA NAM experiment
- [x] Malignant_Hyperthermia_of_Anesthesia — definition + NAM experiment (attaches to existing trigger node)
- [x] Candidate register + validation-pathway (MIMIC vs genotype-linked biobank) + NAM guidance
- [ ] Next candidates: `RYR2_CPVT` (exercise/catecholamine), `Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency` (oxidant drug — first hematologic/metabolic example)
- [ ] Follow-ups: renderer badge (⚗ hypothesis-based), declared-vs-inferred consistency lint, KGX/BioLink export treatment
- [ ] Pilot the population arm on a genotype-linked biobank to move a `validation_status` toward `VALIDATED_AGAINST_GOLD_STANDARD`

## Links

- Design write-up: [`docs/hypothesis-based-phenotype-algorithms.md`](../hypothesis-based-phenotype-algorithms.md)
- Candidate register & datasets: [`docs/reports/hypothesis-driven-ehr-case-finding-2026-07-12.md`](../reports/hypothesis-driven-ehr-case-finding-2026-07-12.md)
- Decision register: [Design Decisions §11](../explanation/design-decisions.md)
- Driving issue: [#6245](https://github.com/monarch-initiative/dismech/issues/6245)
