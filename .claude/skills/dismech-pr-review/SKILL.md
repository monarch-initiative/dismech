---
name: dismech-pr-review
description: >
  Instructions for reviewing a dismech PR, in particular PRs relating to disorder curation,
  either creating new dismech entries or updating existing ones.
---

# PR Review Skill

Use this skill to review or draft curation guidance and to QA disorder entries
for correctness, specificity, and schema alignment.

Use all appropriate skills. What follows are some specific guidelines
aimed to catch common suboptimal things we see in PRs a lot. This list
is not complete and you should always consult skills and comparable entries.

## Common things to suggest fixing

1. Debundle Pathophysiology Entries
Each pathophysiology entry must be a single atomic event, not a chain or pathway.
Example:
- Bad: "Mutations cause X which leads to Y resulting in Z"
- Good: Separate nodes: mutation -> X -> Y -> Z, connected with `downstream` links.

2. Term Precision Over False Matches
Prefer no ontology term over a misleading or too-general term.
- Bad: Generic term that is only "close enough"
- Good: Precise descriptor with `term` omitted and a "needs term / NTR" note.

3. Ontology Term Granularity
- Too general: flag and request a more specific term.
- Too specific: note mismatch in description (the term is narrower than the claim).
- Missing term: add "needs term / NTR" note; consider filing an NTR.

4. GO Terms: Molecular/Cellular Only
GO is for molecular and cellular processes, not organ-level physiology.
- Bad: GO terms for systemic/physiological processes
- Good: GO terms for molecular signaling, protein activity, cellular processes
Use HP/UBERON for organ-level physiology instead.

5. Evidence Must Match Claims
Each evidence snippet must directly support what is claimed.
- Phenotype support != frequency support
- Single case reports do not support VERY_FREQUENT
- Model organism evidence must be `evidence_source: MODEL_ORGANISM`
Snippets must be exact quotes from abstracts or trial summaries. No paraphrase.

Allowed `evidence_source` values:
- `HUMAN_CLINICAL`
- `MODEL_ORGANISM`
- `IN_VITRO`
- `COMPUTATIONAL`
- `OTHER`
Split mixed sources into separate evidence items.

6. Post-Composition / Qualifiers
Add qualifiers when needed for precision:
- Location (`located_in`)
- Direction (`INCREASED`, `DECREASED`, `ABERRANT`)
- Temporal (`recurrent`, `chronic`)
- Laterality (when applicable)

7. Section Appropriateness
Put content in the correct section:
- Comorbidities -> `comorbidities`, not `histopathology`
- Diagnostic procedures -> `diagnosis`, not `treatments`
- MAXO diagnostic branch != treatment terms

8. Treatment Modeling
- Use specific MAXO terms, not generic "pharmacotherapy"  if a better term exists (but this term is ok if combined with other terms)
- Explicitly model ion therapies when relevant
- Include therapeutic agents (CHEBI) when known
- Generic MAXO terms are acceptable but less informative

9. Genetic Section Content
Only genetic information belongs in `genetic`:
- Good: Gene names (with HGNC terms), inheritance, variants
- Bad: Expression studies, biomarkers, biochemical markers
Put non-genetic data in `biochemical` or appropriate sections.
- HGNC CURIEs must use the canonical lowercase prefix `hgnc:` (e.g., `hgnc:1100`), not `HGNC:1100`.
- If HGNC CURIE case is wrong, request a direct fix (case mismatches create avoidable validation churn).

10. Subtypes, Stages, and Mappings
- Verify MONDO mappings reflect the same disease concept
- Use `has_subtypes` for true subtypes
- Use `stages` for phased diseases (e.g., cancer phases)
- When diseases share a name, confirm which one is intended

11. Evidence at Cell-Type Granularity
When possible, consider evidence at the cell-type level and annotate `cell_types` accordingly.
