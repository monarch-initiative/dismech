# Schema Directory

This folder contains the LinkML schema yaml files.

- `dismech.yaml`: Main disorder mechanisms knowledge base schema.
- `history.yaml`: Append-only curation/review history records (`history/`).
- `research_synthesis.yaml`: Cross-provider deep-research synthesis artifacts.
- `hypothesis_assessment.yaml`: Assessments of provider hypothesis-exploration reports.
- `phenotype_distribution.yaml`: Statistical phenotype distributions for a disease
  cohort (`kb/phenotype_distributions/`), with a SEPIO-aligned evidence layer and
  an explicit import bridge into dismech entries. See
  [`docs/phenotype-distributions.md`](../../../docs/phenotype-distributions.md).
- `src/phenoagent/schema/matching.yaml`: Case-to-disease phenotype matching run/output schema.
