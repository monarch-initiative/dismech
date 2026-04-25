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

## IMPORTANT: check for silent reversions when the PR owner has resolved conflicts

Although your primary objective is to evaluate the biological and clinical content of PRs,
you MUST be vigilant for cases where the committed has botched a rebase or merge arising from
merge conflict resolution (usually in cache files). You should also try ensure that all changes in the PR
are in scope. If files are touched that are not relevant to the original request this is a warning sign.

If in doubt, mark the PR as being review-required, and assign to cmungall.

If the author truly did intend to include changes that seem out of scope, they will label the PR as scope-override.

If you see a massive number of files touched and these are not relevant, this is a sure sign something has gone horribly wrong.
Flag the PR assign to cmungall and stop.

Typically conflicts arise from difference in cache files. We don't really care so much how these are resolved as they
are derived files. More care should be taken when looking at conflicts resolution in anything authored, whether it is yaml, python,
markdown etc.

If the case seems nuanced, consult issue #1430 for further guidance.

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
- Compare the research artifact against the YAML using the **Content-Completeness Checklist** below.
- For narrative providers, pay special attention to sections that explicitly call out omitted themes, unmodeled mechanisms, future work, or broader disease context.
- For `asta` outputs, do NOT treat every retrieved paper as a review issue. Prioritize disease-specific, central, quotable, cache-backed items with clear modeling value.
- Classify research-backed omissions:
  - Blocking: central to the disease, directly supported by quotable abstract or trial text, and straightforward to model now.
  - Non-blocking: secondary, speculative, weakly evidenced, not easily snippet-supported, or plausibly outside the intended scope of the YAML.
  - Out of scope: useful narrative context that belongs in research notes rather than the structured entry.
- Mention the result of this cross-check in the final review summary when research artifacts were present.

Always check the deep research markdown file. Occasionally agents will cheat and put a "fake" deep research entry. Real entries will always have a frontmatter block
with metadata about the run, and after some rote repetition of the original prompt, should have dense narrative results, with citations.

For NEW dismech entries, there MUST be at least one deep research entry in the PR. A dismech entry that lacks this will likely be highly incomplete.

### Content-Completeness Checklist

When deep-research artifacts are present, the reviewer MUST walk through each dimension
below and note whether the YAML adequately covers what the research surfaced. This
checklist exists because schema-compliance review alone systematically misses content
gaps (see issue #1673 — the HHT retrospective).

For each dimension, compare the research artifact against the YAML and record one of:
- **Adequate**: YAML covers the central items surfaced by research.
- **Gaps noted**: Specific omissions listed; classify each as blocking or non-blocking.
- **N/A**: Research did not surface meaningful content for this dimension.

Include the completed checklist (or a summary of it) in your review body.

#### 1. Phenotype coverage
- Does the YAML capture the major organ-system manifestations described in research?
- Are organ-specific phenotypes present (e.g., pulmonary, hepatic, cerebral AVMs for vascular diseases)?
- Are frequency data and subtype-specific phenotype assignments included when the research provides them?
- Missing a phenotype that affects >10% of patients and has an HPO term is blocking.

#### 2. Subtype completeness
- Do all subtypes listed in research appear in `has_subtypes`?
- Does each subtype have a `disease_term` with MONDO or OMIM identifier when the research provides one?
- Are subtype-specific phenotype, genetic, and treatment distinctions captured?
- Missing MONDO/OMIM mappings for well-characterized subtypes is blocking when identifiers are available in the research.

#### 3. Pathophysiology depth
- Are the key mechanistic models described in research represented as atomic pathophysiology nodes?
- Are secondary or recently discovered mechanisms captured (e.g., somatic second-hit models, immune involvement at lesion sites)?
- Is histopathological detail (e.g., AVM morphogenesis, perivascular infiltrates) modeled when the research describes it?
- A central disease mechanism described in research with PMID support that is entirely absent from the YAML is blocking.

#### 4. Treatments and clinical trials
- Are all drug treatments named in research present in the YAML `treatments` section?
- Are off-label or emerging therapies with observational data or mechanistic rationale included?
- Are clinical trials (NCT identifiers) surfaced by research captured in `clinical_trials`?
- Missing a treatment with published trial data (Phase II+) is blocking.

#### 5. Genetic section depth
- Does the genetic section include penetrance data when research provides it?
- Are modifier genes with evidence included?
- Are variant class summaries (missense, splice-site, CNV, etc.) present?
- Is somatic mutation evidence (e.g., second-hit models) captured when described in research?
- A genetic section that lists only gene names when the research provides penetrance, modifiers, and variant data is blocking.

#### 6. Biomarkers and diagnostics
- Are diagnostic biomarkers and imaging findings described in research reflected in the YAML?
- Are diagnostic criteria or screening protocols mentioned in research captured?

#### 7. PMIDs and references
- Are high-value disease-specific PMIDs surfaced by research, especially ones already fetched into `references_cache/`, incorporated into the YAML?
- Does the YAML appear to under-consume the available references relative to what the research provided?
- Note: deep-research PMIDs can be hallucinated — do not flag missing PMIDs as blocking unless you have verified they are real.

#### 8. Overall consumption assessment
- Does the YAML appear intentionally narrower than the research artifact (acceptable if signaled), or does it look like the research was simply under-consumed (blocking)?
- As a rough heuristic: if the research artifact surfaces N major themes and the YAML covers fewer than half, the entry is likely under-consumed unless the PR description explains the scoping decision.

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
- Temporal (`temporality: RECURRENT`, `CHRONIC`, `ACUTE`, `SUBACUTE`, `TRANSIENT`, etc.)
- Laterality (when applicable)
- Clinical course (`clinical_course: PROGRESSIVE` / `STABLE`)
- Descriptor severity (`severity: MILD|MODERATE|SEVERE`)
- Descriptor onset (`onset.onset_category: CHILDHOOD`, etc.)

Prefer the explicit descriptor slots above over the deprecated generic `qualifiers`
field for common post-composition. Reserve `qualifiers` for predicate-value cases
that are not covered by dedicated slots.

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

12. Research-Backed Completeness (Content-Completeness Checklist)
If matching deep-research artifacts exist, walk through the **Content-Completeness Checklist**
in the "Deep Research Cross-Check" section above. This is not optional — it is the primary
defence against schema-valid but content-incomplete entries.
- Flag omissions when a central research-backed mechanism, phenotype, diagnostic, treatment, biomarker, or subtype is missing and the evidence is both quotable and in scope for the current YAML.
- If the YAML is narrower than the research artifact, ask whether that narrowing is intentional and sufficiently signaled rather than assuming it is correct.
- Do not flood the review with every uncited paper from a retrieval-heavy artifact; focus on the highest-value misses.
- Include the checklist results (or a summary) in the review body so the curation agent knows exactly what to address.

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
- When matching deep-research artifacts exist, the **Content-Completeness Checklist** was completed and no blocking omissions remain across any dimension (phenotypes, subtypes, pathophysiology, treatments, genetics, biomarkers, references)
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
