# Mechanism-hypothesis-driven EHR case-finding: candidate diseases

**Date:** 2026-07-12
**Related:** [#6245](https://github.com/monarch-initiative/dismech/issues/6245) ·
[Hypothesis-Based Phenotype Algorithms proposal](../hypothesis-based-phenotype-algorithms.md)

## Why this survey

The Timothy syndrome curation ([#6245](https://github.com/monarch-initiative/dismech/issues/6245))
turned one zebrafish finding — *fever elicits arrhythmia and seizures even in
overtly normal cacna1c heterozygotes* — into a computable idea: **scan EHRs for
rhythm disturbance or seizures following a fever, to surface latent/mild CACNA1C
carriers.** That query is valid only if the fever→CaV1.2 mechanism holds in
humans, so running it is simultaneously case-finding *and* a test of the
mechanism.

Timothy is not special in this respect. It is one instance of a recurring
archetype. This report catalogs other diseases where a **mechanistic hypothesis
underpins an EHR case-finding scan**, so that (a) the schema proposal is grounded
in a general pattern rather than a single example, and (b) we have a concrete
worklist of future hypothesis-based phenotype algorithms — most of them attaching
to disease entries that **already exist** in the KB.

## The archetype: trigger-provoked latent disease

> A physiological or pharmacological **trigger** transiently unmasks a **latent
> channel/enzyme/pathway defect**. Most carriers are asymptomatic at baseline and
> never meet the classical case definition. An EHR query for **trigger-associated
> events** (event *shortly after* exposure, in patients without prior such events)
> should be **enriched for latent carriers**. The enrichment, tested against
> genotype or a reference standard, is itself evidence for the mechanism.

The classical case definition finds the severe, syndromic tail. The
mechanism-hypothesis scan reaches down the severity distribution toward the
latent/mild cases — which is precisely where the mechanism, not the syndrome, is
what defines membership. This is what DisMech's mechanism-first stance is *for*.

## The epistemic spectrum (why `derivation_basis` matters)

These candidates do **not** sit at one point on the evidence axis — they span it,
which is exactly why the proposed `derivation_basis` slot is orthogonal to
`definition_type`:

- **Established trigger biology** (`derivation_basis: ESTABLISHED_CRITERIA`, or
  near it) — the trigger→unmasking link is textbook and often already used
  clinically. Brugada fever-unmasking, malignant hyperthermia on volatile
  anesthetics, G6PD oxidant-triggered hemolysis, drug-induced long-QT unmasking
  latent congenital LQTS. Here the *scan* is a well-motivated case-finding tool;
  the "hypothesis" is mostly about EHR operationalization/yield.
- **Emerging / model-system-derived** (`MECHANISTIC_HYPOTHESIS` /
  `MODEL_SYSTEM_EXTRAPOLATION`) — the trigger→unmasking link is shown chiefly in a
  model system and unproven in humans. **Timothy fever-exacerbation** is the
  worked example: zebrafish evidence, human validity open.

A hypothesis-based algorithm should be born with its point on this spectrum
attached, so a downstream consumer never mistakes a speculative scan (Timothy) for
a well-grounded one (Brugada), even though both are `PHENOTYPE_ALGORITHM`.

## Candidate register

All "dismech entry" links are existing KB files (real attach points). "Maturity"
is the mechanism's human-evidence status, mapping to `derivation_basis`.

| Disease (dismech entry) | Latent trigger | Mechanism (channel/enzyme) | Proposed EHR scan | Maturity |
|---|---|---|---|---|
| **Timothy syndrome** (`Timothy_Syndrome`) | Fever / hyperthermia | CaV1.2 (CACNA1C) temperature activation → arrhythmia + seizure threshold | New arrhythmia/QT event or seizure shortly after documented fever | Emerging (zebrafish) — **curated, #6245** |
| **Brugada syndrome** (`Brugada_Syndrome`) | Fever | Nav1.5 (SCN5A) temperature-sensitive trafficking/gating → type-1 ECG unmasking | Fever-associated type-1 Brugada ECG / fever-triggered VF, structurally normal heart | Established — **gap: entry does not yet capture fever-unmasking** |
| **Congenital long-QT** (`Long_QT_Syndrome`) | QT-prolonging drug | KCNH2/KCNQ1 reduced repolarization reserve | Marked QT prolongation or torsade on a QT-prolonging drug → latent LQTS | Established (pharmacogenomic) |
| **CPVT** (`RYR2_CPVT`) | Exercise / catecholamines | RYR2/CASQ2 Ca²⁺-release instability → DADs | Exertion/stress-provoked syncope or bidirectional/polymorphic VT, structurally normal heart | Established |
| **Malignant hyperthermia** (`Malignant_Hyperthermia_of_Anesthesia`) | Volatile anesthetic / succinylcholine | RYR1/CACNA1S Ca²⁺-release → hypermetabolic crisis | Peri-anesthetic hyperthermia / masseter spasm / unexplained rhabdomyolysis | Established |
| **G6PD deficiency** (`Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency`) | Oxidant drug / fava / infection | G6PD NADPH shortfall → oxidative RBC injury | Acute hemolytic anemia within days of an oxidant drug/infection | Established |
| **Acute intermittent porphyria** (`Acute_Intermittent_Porphyria`) | CYP-inducing drug / fasting / hormones | HMBS haploinsufficiency → ALA/PBG accumulation | Recurrent unexplained abdominal pain + neuro/autonomic signs after inducing drugs | Established, under-recognized |
| **MCAD deficiency** (`MCAD_Deficiency`) | Fasting / intercurrent illness | ACADM fatty-acid-oxidation block → energy failure | Hypoketotic hypoglycemia / Reye-like decompensation during fasting/illness | Established (also newborn-screened) |
| **Hereditary angioedema** (`Hereditary_Angioedema`) | ACE inhibitor / estrogen / trauma | SERPING1 (C1-INH) → bradykinin surge | Recurrent angioedema without urticaria, esp. ACE-inhibitor-associated | Established, under-recognized |
| **Hypokalemic periodic paralysis** (`Hypokalemic_Periodic_Paralysis`) | Carbohydrate load / rest-after-exercise / stress | CACNA1S/SCN4A → transient hypokalemic weakness | Recurrent transient weakness with documented hypokalemia after trigger | Established |

## How each would be represented (the Timothy template, reused)

Every row follows the same shape now committed for Timothy — all achievable with
**existing** slots today, and upgraded to structured epistemic markers once the
[#6245 schema extension](../hypothesis-based-phenotype-algorithms.md) lands:

1. **`mechanistic_hypotheses`** entry with a stable `hypothesis_group_id` and a
   `status` matching the maturity column (`EMERGING` for Timothy; `CANONICAL`/
   `ALTERNATIVE` for the established-trigger rows where the biology is settled but
   the *EHR operationalization* is the new claim).
2. A **trigger pathophysiology node** ("Fever-triggered …", "Anesthetic-triggered
   …", "Oxidant-triggered …") whose `downstream` edges opt into
   `hypothesis_groups: [<id>]`.
3. A **hypothesis-based `PHENOTYPE_ALGORITHM` definition** — the EHR case-finding
   query — that (post-#6245) sets `derivation_basis`, a structured
   `validation_status` object, and `attaches_to` the trigger node so the basis is
   inferred from the pathograph. Until then, the unvalidated status is stated in
   the name/scope/notes (as done for Timothy).
4. A **`discussions` / `HUMAN_MODEL_MISMATCH`** (or `KNOWLEDGE_GAP`) entry whose
   `proposed_experiments` is the genotype-enrichment test of the scan.

## Near-term opportunities

- **Brugada + fever** is the highest-value quick win: fever-unmasking of the
  type-1 ECG is textbook, the `Brugada_Syndrome` entry does **not** yet capture
  it, and it is the established-biology mirror image of the Timothy case — an ideal
  second worked example spanning the other end of the `derivation_basis` spectrum.
- **Drug-induced long-QT → latent congenital LQTS** is the cleanest
  *pharmacological-trigger* example and pairs naturally with the existing
  `Long_QT_Syndrome` entry and drug-target machinery.
- Timothy + Brugada together would let the proposal show one `EMERGING` and one
  `ESTABLISHED` hypothesis-based algorithm side by side.

## Scope and evidence discipline

This is a **design/landscape survey**, not KB evidence. The trigger biology cited
here is well-established textbook knowledge; the disease/gene/trigger framings were
cross-checked against the referenced dismech entries. **Per-claim PMIDs with
verified exact-quote snippets are added at curation time**, following the standard
anti-hallucination workflow (fetch abstract → verify snippet substring → validate
terms) — no citations are asserted in this survey to avoid unverified references.
Candidate selection favored disorders already in the KB so each has a concrete
attach point.
