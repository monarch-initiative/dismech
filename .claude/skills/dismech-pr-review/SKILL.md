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

## Trust the Validation Process

**Do NOT second-guess deterministic validation.**

The dismech CI pipeline runs `just validate`, `just validate-terms-file`, and `just validate-references` on every PR. If a file passes those checks, it is schema-valid and structurally correct. The reviewer's job is NOT to re-inspect the output of these checks — that is redundant and leads to false positives.

Concretely:
- **Do not flag empty YAML keys** (e.g., `datasets:` with no content). In LinkML, a null value, an empty list, and a missing key are semantically equivalent. If validation passes, the entry is valid.
- **Do not flag YAML structure or whitespace issues** — these are linting concerns outside the review scope.
- **Do not flag schema fields** (required/optional presence, field types, enum values) — the schema validator is authoritative.
- **Do not flag HGNC CURIE case** if you have not confirmed it actually fails validation. Only flag it if you can verify the mismatch exists and causes validation failure.

The reviewer's role is to evaluate **non-deterministic components** using biological judgment, domain expertise, and the rubrics below: biological plausibility, ontology specificity, evidence quality, claim–snippet alignment, and section appropriateness. Focus there.

## Things NOT to flag

- **`updated_date`**: Do NOT flag or request updates to `updated_date` in reviews. Change tracking is handled via separate git logs and traces.
- **Empty YAML keys** that pass schema validation (e.g., `datasets:`, `clinical_trials:`).
- **Structural or formatting issues** that would be caught by `just validate` — trust CI.

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
- HGNC CURIEs should use the canonical lowercase prefix `hgnc:` (e.g., `hgnc:1100`), not `HGNC:1100`. Only flag if you have verified the mismatch causes a validation failure — do not flag preemptively.

10. Subtypes, Stages, and Mappings
- Verify MONDO mappings reflect the same disease concept
- Use `has_subtypes` for true subtypes
- Use `stages` for phased diseases (e.g., cancer phases)
- When diseases share a name, confirm which one is intended

11. Evidence at Cell-Type Granularity
When possible, consider evidence at the cell-type level and annotate `cell_types` accordingly.

## Review Decision: Formal GitHub Review

After completing the review, you MUST submit a formal GitHub review (not just a comment).
Use `gh pr review` with one of the three events below.

### APPROVE
Submit `--approve` when **all** of the following hold:
- No fabricated snippets or wrong PMIDs detected through spot-checking
- No major ontology placement errors (e.g., GO molecular function term in `biological_processes`)
- All pathophysiology entries are atomic (not chained multi-step sentences)
- At most minor wording / completeness issues
- (CI handles schema/term/reference validation — do not duplicate that work)

### REQUEST_CHANGES
Submit `--request-changes` when **any one** of the following is true:
- Fabricated or paraphrased snippet (not an exact quote from the cited abstract)
- Wrong PMID (paper topic does not match the claim being evidenced)
- Significant ontology misuse (e.g., GO MF term in `biological_processes`)
- Pathophysiology entries bundled into chains rather than single atomic events
- Claim–evidence mismatch (evidence snippet does not support the stated claim)

### COMMENT + reassign to @cmungall
Submit `--comment` and reassign the PR/issue to `@cmungall` when:
- An ambiguous biological claim requires human domain expertise to adjudicate
- It is genuinely unclear whether an issue is blocking or merely cosmetic
- There are conflicting signals between different validation checks

### Strictness policy
Do NOT defer fixable problems with "can be addressed in a future PR". The curating agent
can act on feedback immediately. If something is wrong, request changes. Only approve when
the entry is genuinely ready to merge.
