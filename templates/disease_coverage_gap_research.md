# Coverage-Gap Research Template

## Target Disease
- **Disease Name:** {disease_name}
- **MONDO ID:** {mondo_id} (if available)

## What Is Already Curated — Do Not Re-Derive Any Of It

Clinical features already recorded, by organ system:

{existing_phenotypes}

Mechanism already recorded:

{existing_mechanism}

**Everything above is done.** Do not restate it, re-justify it, or return it as a
finding. A report that re-describes the established mechanism has failed this
brief.

## Research Objective — Absences Only

Report what a complete account of this disease would contain that the list
above does **not**. Two passes:

### Pass 1 — Organ-system fan-out for missing clinical features

Work through each organ system in turn — gastrointestinal, hepatic,
hematologic, skeletal, endocrine, cardiovascular, renal, respiratory,
neurologic, psychiatric, dermatologic, oral and dental, reproductive and
obstetric, ophthalmic, immune and infectious susceptibility, neoplastic — and
for each, name any clinical feature of this disease **not** in the list above.
For each new feature report:

- the feature, with a suggested HPO term
- its frequency among affected individuals, as reported, with the source
- whether it is a feature of the disease, a treatment effect, or a feature of a
  comorbid condition that travels with the disease — these are different claims
  and must not be blended
- one PMID with an exact quote from the abstract

Say explicitly when an organ system has nothing to add. An empty system is a
useful result, not a gap in the report.

### Pass 2 — Missing structured dimensions

For each of the following, report what the literature establishes, or state
that the dimension does not apply to this disease:

- **Histopathology and grading.** The named histological classification used in
  practice, its grades or stages in order, and what distinguishes each from the
  one before it. Give the classification's own terminology.
- **Disease subtypes and clinical forms.** The recognized forms, what defines
  each, and their relative frequency. Include forms defined by absence of a
  usual feature, and treatment-refractory forms.
- **Progression and natural history.** Ordered phases, what drives movement
  between them, and what is reversible at each.
- **Animal models.** Species, genotype or intervention, which disease features
  each reproduces, and which it fails to reproduce.
- **Non-animal experimental models.** Organoids, organ-chips, primary or iPSC
  cultures: what each system captures and what it omits.
- **Interventional trials.** Registered trials of disease-modifying therapy,
  with registry identifiers, phase, status, and primary result where reported.
- **Comorbid conditions** that co-occur at above-background rates, with the
  measured strength of association, and whether shared genetic susceptibility
  is the proposed explanation.
- **Biomarkers and laboratory monitoring** beyond the diagnostic antibodies
  already listed, including reference intervals where standardized.

## Rules

- **Absence is the deliverable.** If a dimension is genuinely well covered by
  what is already curated, say so in one line and move on.
- **Do not inflate.** A feature reported once in a single case report is
  reported as exactly that. Do not present a case report as a disease feature.
- **Distinguish the disease from its treatment.** Where a feature is caused by
  the therapy rather than the disease, say so.
- Cite primary literature with PMIDs and exact abstract quotes. Never cite a
  paper for a claim its abstract does not make. Where a registry identifier is
  the right citation, give the registry identifier.
