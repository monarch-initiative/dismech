# Model Mapping Guide (FHIR / OHDSI / CQL -> dismech)

Use this guide to translate computable phenotype logic into dismech `definitions`.

## dismech target structure

- `definitions[]`: Top-level phenotype definition or diagnostic criteria set.
- `criteria_sets[]`: Named sub-blocks (primary criteria, inclusion rules, confirmation).
- `inclusion_criteria[]`, `exclusion_criteria[]`, `core_clinical_characteristics[]`,
  `imaging_requirements[]`, `laboratory_requirements[]`, `additional_requirements[]`.
- `minimum_required`: Use for count thresholds (>=2 events, >=1 lab, etc.).
- `notes`: Use for cohort exit and temporal logic if no dedicated slot.

## OHDSI / OMOP cohort definition

- **ConceptSet** -> `CriteriaItem` under `inclusion_criteria`.
  - `preferred_term`: "Concept set: <name>".
  - `description`: concept count, domain, and any constraints.
- **PrimaryCriteria** (entry events) -> `criteria_sets` entry named "Primary criteria".
- **InclusionRule** -> separate `criteria_sets` entry (one per rule).
- **CorrelatedCriteria** -> `additional_requirements` or `imaging_requirements`.
- **Cohort exit** -> `notes` or a `CriteriaItem` in `additional_requirements`.
- **Temporal windows** (e.g., 31-365 days) -> `description` on the relevant `CriteriaItem`.

Concept IDs:
- If a concept maps to a configured prefix (ICD10CM, NCIT, HP), add a `term` object.
- Otherwise keep the code in `description` and the label in `preferred_term`.

## FHIR phenotype logic

- **Condition** -> `inclusion_criteria` item.
  - Use `term` if ICD-10-CM or other configured prefix.
- **Observation** (lab/serology) -> `laboratory_requirements`.
- **Procedure / Imaging** -> `imaging_requirements` or `additional_requirements`.
- **MedicationRequest / MedicationAdministration** -> `additional_requirements`.
- **Encounter** (setting) -> `scope` or `notes` on the definition.
- **ValueSet** -> treat as a concept set (same mapping as OHDSI).

## CQL phenotype logic

- **define** statements -> `criteria_sets` or `CriteriaItem` entries.
- **exists / count** -> `minimum_required` or describe in the criterion.
- **temporal operators** (during, overlaps, before/after) -> describe in the criterion.
- **negation** -> `exclusion_criteria`.

## Notes

- Keep the algorithm in plain language; do not copy vendor-specific syntax.
- Evidence: attach at least one EvidenceItem if the algorithm is drawn from a paper.
