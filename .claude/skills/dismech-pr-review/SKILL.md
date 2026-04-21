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

## Deep Research Cross-Check

When a PR adds or updates a disorder YAML and matching deep-research artifacts exist in
`research/`, treat those artifacts as first-class curation inputs, not optional background.

At minimum:
- Find the matching `research/*-deep-research-*.md` file and corresponding `.citations.md`.
- Read the research artifact before finalizing review.
- Compare the research artifact against the YAML and ask:
  - Are central mechanisms, phenotypes, diagnostics, treatments, biomarkers, or subtype distinctions present in research but absent or oversimplified in YAML?
  - Are there high-value disease-specific PMIDs or DOIs surfaced by research, especially ones already fetched into `references_cache/`, that never made it into the YAML?
  - Does the YAML appear intentionally narrower than the research artifact, or does it look like the research was simply under-consumed?
- For narrative providers, pay special attention to sections that explicitly call out omitted themes, unmodeled mechanisms, future work, or broader disease context.
- For `asta` outputs, do NOT treat every retrieved paper as a review issue. Prioritize disease-specific, central, quotable, cache-backed items with clear modeling value.
- Classify research-backed omissions:
  - Blocking: central to the disease, directly supported by quotable abstract or trial text, and straightforward to model now.
  - Non-blocking: secondary, speculative, weakly evidenced, not easily snippet-supported, or plausibly outside the intended scope of the YAML.
  - Out of scope: useful narrative context that belongs in research notes rather than the structured entry.
- Mention the result of this cross-check in the final review summary when research artifacts were present.

Always check the deep research markdown file. Occasionally agents will cheat and put a "fake" deep research entry. Real entries will always have a frontmatter block
with metadata about the run, and after some rote repetition of the original prompt, should have dense narrative results, with citations.

For NEW dismech entries, there MUST be at least one deep research entry in the PR. A dismech entry that lacks this will likely be highly incomplete

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
- For new entries, NCIT is favored over MAXO
- When MAXO is used, use specific MAXO terms, not generic "pharmacotherapy"  if a better term exists (but this term is ok if combined with other terms)
- Explicitly model ion therapies when relevant
- Include therapeutic agents (CHEBI) when known
- Generic MAXO terms are acceptable but less informative. Always check for a more informative NCIT

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

12. Research-Backed Completeness
If matching deep-research artifacts exist, use them as a completeness baseline for non-deterministic review.
- Flag omissions when a central research-backed mechanism, phenotype, diagnostic, treatment, biomarker, or subtype is missing and the evidence is both quotable and in scope for the current YAML.
- If the YAML is narrower than the research artifact, ask whether that narrowing is intentional and sufficiently signaled rather than assuming it is correct.
- Do not flood the review with every uncited paper from a retrieval-heavy artifact; focus on the highest-value misses.

13. Pathograph completeness
- insofar as evidence allows, the pathograph should include both proximal events/perturbations/mutations, and distal events (phenotypes, histopathology)
- there should be join points between treatments and models and the pathograph, where evidence allows
- pathographs should generally link up into a single strongly connected component

14. Lumping and splitting
- A dismech entry should correspond to a discrete pathomechanism.
- Do not have entries for high level disease groupings or phenotypes (see `kb/modules/` for these)
- Do not make multiple entries where there is little distinction (e.g. gene specific forms of Bardet Biedl)
- Do not make distinct entries for e.g. severity types
- Align with clingen where possible
- Lumping and splitting can be hard and ambiguous - it is OK to summon a human to help you resolve, and hold off on approving until the human approves

## Review Decision: Formal GitHub Review

After completing the review, you MUST submit a formal GitHub review (not just a comment).
Use `gh pr review` with one of the three events below.

### APPROVE
Submit `--approve` when **all** of the following hold:
- No fabricated snippets or wrong PMIDs detected through spot-checking
- No major ontology placement errors (e.g., GO molecular function term in `biological_processes`)
- All pathophysiology entries are atomic (not chained multi-step sentences)
- When matching deep-research artifacts exist, they were checked and no blocking research-backed omissions remain
- At most minor wording / completeness issues
- (CI handles schema/term/reference validation — do not duplicate that work)

### REQUEST_CHANGES
Submit `--request-changes` when **any one** of the following is true:
- Fabricated or paraphrased snippet (not an exact quote from the cited abstract)
- Wrong PMID (paper topic does not match the claim being evidenced)
- Significant ontology misuse (e.g., GO MF term in `biological_processes`)
- Pathophysiology entries bundled into chains rather than single atomic events
- Claim–evidence mismatch (evidence snippet does not support the stated claim)
- A central research-backed mechanism, phenotype, diagnostic, treatment, biomarker, or subtype was omitted even though the supporting evidence is clear, quotable, and in scope for this YAML

### COMMENT + reassign to @cmungall
Submit `--comment` and reassign the PR/issue to `@cmungall` when:
- An ambiguous biological claim requires human domain expertise to adjudicate
- It is genuinely unclear whether an issue is blocking or merely cosmetic
- There are conflicting signals between different validation checks
- It is unclear whether a research-backed omission reflects valid scope narrowing or a genuine modeling miss

### Strictness policy
Do NOT defer fixable problems with "can be addressed in a future PR". The curating agent
can act on feedback immediately. If something is wrong, request changes. Only approve when
the entry is genuinely ready to merge. This includes central research-backed omissions when
matching deep-research artifacts were available in the PR.
