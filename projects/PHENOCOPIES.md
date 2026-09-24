---
title: Phenocopies
status: IN_PROGRESS
description: >-
  Whether and how dismech should record that a toxic or pharmacologic exposure can
  reproduce a Mendelian disease's presentation closely enough to mislead diagnosis.
tags: [ENVIRONMENTAL_EXPOSURE, RARE_DISEASE, SCHEMA_EVOLUTION, PHENOTYPE_COVERAGE]
diseases:
  - Drug-Induced_Methemoglobinemia
  - Hereditary_Methemoglobinemia
  - Lead_Poisoning
  - Porphyria_due_to_ALA_Dehydratase_Deficiency
  - Apparent_Mineralocorticoid_Excess
  - Brugada_Syndrome
  - Arsenic_Poisoning
  - Bartter_Syndrome
  - Gitelman_Syndrome
  - Cystinosis
  - Smith-Lemli-Opitz_Syndrome
  - Alpers-Huttenlocher_Syndrome
modules:
  - primary_hemostatic_plug_failure
  - drug_induced_liver_injury
  - drug_induced_nephrotoxicity
---

# Phenocopies

## Scope

Issue [#10395](https://github.com/monarch-initiative/dismech/issues/10395) asks for a
phenocopy presentation on rare genetic disease entries: where an exposure can produce what
looks like a Mendelian disease in someone carrying none of its variants, show the exposure
and show what tells the two apart.

The clinical observation is not in dispute. What is open is whether dismech needs a new
construct to record it, and if so which.

**Two senses of the word, and they must not be merged.** "Phenocopy" already appears
throughout `kb/`, almost entirely in the *experimental* sense: a chemical or knockdown
reproducing a mutant phenotype in a model system. This project concerns the
*clinical/diagnostic* sense. The two carry different evidence rules, and a slot added
without naming the distinction will fill with model-system results.

## Source artefacts

| File | What it is |
|---|---|
| [`phenocopy-table.md`](PHENOCOPIES/phenocopy-table.md) | 48 exposure–gene pairs in five sections, with a cross-cutting tier and a per-pair "what separates them" column |
| [`Toxicologic-Phenocopy-Atlas.pdf`](PHENOCOPIES/Toxicologic-Phenocopy-Atlas.pdf) | The same material formatted |

**The compilation's own caveats govern.** It states that tiers are a judgement about
mechanistic tightness and **not** an evidence rating, that two rows are arguably
gene–environment interaction rather than phenocopy, that valproate/`POLG` is deliberately
both a phenocopy and a trigger and would need two edge types, and that the set is a
literature compilation rather than curated content. No row has been verified for this
project.

**Decided 2026-09-24: every row is verified against primary literature before it is
curated.** The compilation is a starting list, not a source, so no entry is written from a
row that has not been checked.

## What the knowledge base already expresses

dismech already carries phenocopy pairs, and in one case already models the relation.

| Pair | Status |
|---|---|
| `Drug-Induced_Methemoglobinemia` / `Hereditary_Methemoglobinemia` | Both curated. The acquired entry names the hereditary form as "the genetic phenocopy" and records `distinguishing_features` |
| `Lead_Poisoning` / `Porphyria_due_to_ALA_Dehydratase_Deficiency` | Both curated |
| Licorice / `Apparent_Mineralocorticoid_Excess` | Genetic side curated; exposure side is not a separate entry |

The construct is `DifferentialDiagnosis`, reached through `differential_diagnoses`, carrying
`name`, `disease_term`, `description`, `phenotypes`, `distinguishing_features`, `evidence`
and `notes`.

So the question is narrower than the issue implies. It is not whether dismech can express
this, but that:

- the relation is **untyped**, so the phenocopy claim lives in free text and is not
  queryable;
- the relation is **one-directional**, so a pair is discoverable from one side only;
- the **mechanistic tightness** distinction, between sharing a molecular target and merely
  converging on a presentation, has nowhere structured to go.

## Implementation options

From [comment 5497102936](https://github.com/monarch-initiative/dismech/issues/10395#issuecomment-5497102936),
cheapest first. All three are undecided.

That comment's argument for schema content over prose is that where an exposure hits the
same gene product the mutation hits, the phenocopy is not really a differential diagnosis
but a second etiologic route into an existing pathograph node. Assess that claim before
choosing, since it is what separates option B from option A.

**A. Fields on `DifferentialDiagnosis`.** An `etiology_class`, an optional ECTO/CHEBI
`exposure_term`, and a relation grade. Existing differential blocks stay valid, no new
section, no new foreign-key surface, and the view becomes a render-time filter on the
existing differentials card. That last point rests on the disorder page being one long
page of anchored section cards rather than a tab widget, which is unverified.

**B. A top-level `phenocopies:` section** with `attaches_to`, `distinguishing_features`,
`discriminating_tests`, `reversibility` and `evidence`. Richer, but a new section and a new
foreign-key surface. Better deferred until A has produced a corpus to design against.

**C. A `Grouping`** at `kb/groupings/Toxic_Phenocopies_of_Genetic_Disease.yaml`. No schema
change, following the `Digenic_and_Oligogenic_Disorders` pattern.

## Open questions

1. **Does a typed qualifier on `DifferentialDiagnosis` suffice?** A negative answer removes
   most of the remaining work. Settle this first.
2. **What counts as verified?** The decision above settles that rows are verified, not what
   the check covers. The pair and its shared lesion are the minimum; whether it also covers
   the tier assignment and the distinguishing test changes the cost across 48 rows.
3. **One tier scheme or two?** The compilation proposes T1/T2/T3; the issue comment proposes
   mechanistic, pathway and phenotypic grades. They were written independently and appear to
   mean nearly the same thing. One should win, and neither may be rendered anywhere it could
   read as a confidence grade.
4. **Where does the relation attach?** Disease to disease, exposure to disease, or exposure
   to a named pathophysiology node.
5. **Directionality.** Recorded on the genetic entry, the toxic entry, or both. dismech's
   convention for cross-entry claims is duplication rather than inheritance, which argues
   for both, each written from its own point of view.
6. **Is `discriminating_tests` the highest-value field?** No existing construct has it. The
   compilation already supplies it for all 48 rows.
7. **How is reversibility handled?** 20 of the 48 pairs halt or regress on withdrawal, which
   is diagnostically decisive and has no home in the schema.
8. **What about pairs that are both phenocopy and interaction?** Valproate/`POLG` is the
   worked case.

## Relation to the AOP work

Issue #10395 notes the overlap with the AOP work, and it is real but narrower than first
framed. An agent asserted that a toxic phenocopy is an AOP whose adverse outcome is a
genetic disease's phenotype set. That does not hold: a phenocopy could correspond to an
AO at the end of an AOP, but shouldn't be conflated with an entire AOP.

An AOP defines a causal series of biological events leading to an adverse outcome (AO).
An AO is often an adverse phenotype, but only by virtue of biology rather than by
definition. The definition is tied to the purpose AOPs were designed to serve, which is
regulatory: an AO is defined by its relevance as a regulatory endpoint informing
chemical safety decision-making. That said, the framework has since been adopted for
organizing evidence on causal biological sequences outside regulatory science.

## Not yet included

- Any proposed slot name or enum.
- Any rendering design.
- Verification of the 48 rows, or of the pairs listed above.
