# DisMech Data Model

A curated map of the DisMech schema. The schema has ~100 classes; this page
surfaces the ones you actually reach for when curating a disorder, grouped by
what they describe. Each link goes to the full auto-generated page for that
class.

> The complete, always-up-to-date reference is generated from the schema — see
> the [Schema Reference](schema/schemas/dismech.md) for every class, slot, enum,
> and type. This page is the hand-curated entry point into it.

## Core entity

The spine of every entry: one disease, optionally split into subtypes.

| Class | What it is |
|-------|------------|
| [Disease](schema/classes/Disease.md) | The top-level entry. Everything else hangs off it. |
| [Subtype](schema/classes/Subtype.md) | A named subdivision of a disease (`has_subtypes`); the foreign-key target other sections reference via `subtype`. |
| [Genetic](schema/classes/Genetic.md) | Gene/variant-level genetic findings for the disease or a subtype. |
| [GeneticContext](schema/classes/GeneticContext.md) | The genetic scope under which a scoped assertion holds — see the [phenotype-context primer](primers/phenotype-context.md). |

## Mechanism (pathophysiology)

How the disease actually works — the causal mechanism graph.

| Class | What it is |
|-------|------------|
| [Pathophysiology](schema/classes/Pathophysiology.md) | A node in the mechanism graph: a pathological process with cell types, biological processes, and evidence. |
| [CausalEdge](schema/classes/CausalEdge.md) | A directed `downstream` link between mechanism nodes, optionally tagged with hypothesis groups. |
| [Mechanism](schema/classes/Mechanism.md) | A higher-level mechanism grouping. |
| [MechanisticHypothesis](schema/classes/MechanisticHypothesis.md) | Canonical / alternative / emerging mechanism models, referenced by causal edges. |

Mechanism modules and the `conforms_to` pattern are explained in the
[Modules & Conformance primer](primers/modules-and-conformance.md).

## Clinical presentation

What the disease looks like in patients.

| Class | What it is |
|-------|------------|
| [Phenotype](schema/classes/Phenotype.md) | A disease–phenotype association (HPO-bound), with frequency, onset, and evidence. |
| [PhenotypeContext](schema/classes/PhenotypeContext.md) | A scoped phenotype assertion (by subtype, genetic context, etc.). |
| [PhenotypeDescriptor](schema/classes/PhenotypeDescriptor.md) | The HPO term binding plus post-composition (modifier, laterality, onset, temporality, severity). |
| [Demographics](schema/classes/Demographics.md) / [Prevalence](schema/classes/Prevalence.md) | Population-level descriptors. |
| [ProgressionInfo](schema/classes/ProgressionInfo.md) | Natural-history / disease-course information. |
| [HistopathologyFinding](schema/classes/HistopathologyFinding.md) | Tissue-level pathology findings. |
| [Biochemical](schema/classes/Biochemical.md) | Lab markers, with optional LOINC-coded reference ranges and interpretation bands. |

## Evidence & provenance

Every claim is backed by a citable source.

| Class | What it is |
|-------|------------|
| [EvidenceItem](schema/classes/EvidenceItem.md) | A PMID/DOI/structured reference with an exact `snippet`, `supports` verdict, and `evidence_source`. Used everywhere. |
| [Definition](schema/classes/Definition.md) | Computable phenotype / cohort definitions for the disease. |
| [Dataset](schema/classes/Dataset.md) | Linked datasets (e.g. MorPhiC perturbation data). |
| [ClinicalTrial](schema/classes/ClinicalTrial.md) | Trials validated against ClinicalTrials.gov. |

## Therapeutics

How the disease is treated, linked back to the mechanism it targets.

| Class | What it is |
|-------|------------|
| [Treatment](schema/classes/Treatment.md) | A treatment, with `target_phenotypes`, `target_mechanisms`, `therapeutic_modality`, and `therapeutic_agent`. |
| [TreatmentDescriptor](schema/classes/TreatmentDescriptor.md) | The MAXO/NCIT action binding plus therapeutic agent(s). |
| [TreatmentMechanismTarget](schema/classes/TreatmentMechanismTarget.md) | The mechanism node a treatment acts on. |

## Descriptors & post-composition

The reusable building blocks that bind free text to ontology terms. The
two-field contract (`preferred_term` vs `term.label`) is covered in the
[Preferred Term vs Ontology Label primer](primers/preferred-term-vs-label.md).

| Class | What it is |
|-------|------------|
| [CellTypeDescriptor](schema/classes/CellTypeDescriptor.md) | CL cell-type binding. |
| [BiologicalProcessDescriptor](schema/classes/BiologicalProcessDescriptor.md) | GO process binding. |
| [AnatomicalEntityDescriptor](schema/classes/AnatomicalEntityDescriptor.md) | UBERON anatomy binding. |
| [ModelVariableDescriptor](schema/classes/ModelVariableDescriptor.md) | Computational-model variable thresholds (distinct from clinical reference ranges). |

## Classification & cross-references

Where the disease sits in the broader taxonomies.

| Class | What it is |
|-------|------------|
| [DiseaseClassifications](schema/classes/DiseaseClassifications.md) | The `classifications` block (Harrison's part, mechanistic nosology, etc.). |
| [DiseaseMappings](schema/classes/DiseaseMappings.md) | MONDO/ICD/NCIT cross-references. |
| [ComorbidityAssociation](schema/classes/ComorbidityAssociation.md) | Disease-trajectory / comorbidity links. |

---

*Looking for the splash site, disorder browser, or detailed docs? See*
[*dismech.monarchinitiative.org*](https://dismech.monarchinitiative.org/) ·
[*Browse disorders*](https://dismech.monarchinitiative.org/app/) ·
[*Detailed docs*](https://dismech.monarchinitiative.org/details/).
