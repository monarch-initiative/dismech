# Structured claims for evidence evaluation

`StructuredClaim` in the main dismech LinkML schema is a derived view, not a new
curator-authored Disease section. It preserves one complete original assertion
object and brings disease identity and inherited context into the same input.
The classifier is owned by dismech; benchmark answers, reviews and results are
owned by dismech-bench. Nothing in dismech imports a benchmark schema or case.

```python
from dismech.classifier.claims import extract_claim
from dismech.classifier.structured import structured_claim_task

claim = extract_claim(document, '/biochemical/0/evidence/3')
task = structured_claim_task(claim, source_text=source_text)
```

The assertion retains original names, ontology bindings, subtypes, context,
quantities, assay details and nested objects. The extractor never turns it into
an agent-written sentence. It removes only `evidence`, `references` and
`review_notes`, recursively. Separate nested assertions remain part of a selected
parent object; selecting an edge instead evaluates that edge with parent context.

`assertion_type` is resolved through the main schema's containment slot ranges.
`assertion` uses the existing LinkML `Any` container to carry those heterogeneous
objects unchanged, not a second hand-maintained union of every dismech class.
The wrapper schema validates its envelope and evidence; it does not independently
validate the opaque assertion against `assertion_type`. Validate the source DM
record normally, and verify benchmark derivation against its frozen source.

## Context and provenance

- `about.disease` copies `/name` and `/disease_term` when present.
- `about.context` records ancestor objects with their JSON Pointers. Ancestor
  projections retain local fields and qualifiers but omit evidence-bearing child
  objects, avoiding sibling assertions and other citations.
- `subtype` and `subtypes` foreign keys resolve exactly against `has_subtypes`.
  The corresponding original subtype descriptors are included with their paths.
  Missing or ambiguous names fail; inheritance is not inferred from prose.
- Additional `context_paths`, such as `/description`, explicitly request original
  values. JSON Pointer escaping follows RFC 6901. Evidence/review paths are rejected.
- `origin` records the assertion, evidence and context paths. Benchmark snapshots
  additionally pin document bytes and repository commits. Array indices are stable
  only relative to that frozen document; this is not a mutable-KB identity scheme.

Conflicting ancestor/local qualifiers remain visible. The extractor does not
silently override them or invent a disease/subtype summary. The population or
assay of the cited paper is not substituted for the claim's population or assay.

## Evaluation contract

The whole assertion is evaluated. SUPPORT must cover its substantive content;
support for only a broader or partial claim is a mismatch. REFUTE remains on the
selected evidence relationship: a material contradiction can refute a conjunction;
one does not need to contradict every conjunct. NO_EVIDENCE is also preserved.
Directness is checked if annotated; missing directness stays missing.

The selected evidence's explanatory prose cannot narrow the assertion. Model
state includes only its snippet, direction and optional directness, plus the
structured assertion, type and about context. Provenance, other citations,
benchmark expectations and reviews are excluded. Source text can resolve referents
and qualifications but cannot supply independent results outside the snippet.

The primary task returns MATCH/MISMATCH. An optional second Choice task diagnoses
mismatches as `insufficient_specificity`, `incompatible_assertion`, `unrelated`, or
`other`. A different assay or population is not automatically contradictory.
Jev returns these fixed choices and probabilities, not invented free-text reasons
or paths. `ClaimEvaluation.disputed_paths` and `justification` support human or
other evaluator annotations; paths refer to the wrapper (e.g. `/assertion/presence`).

This derives from the existing evidence-direction distinctions in design decisions
§6 and the subtype foreign-key convention in §3. Evaluation reasons are not new
`EvidenceItem.supports` values. The older text-only direct-support task remains
available to replay its recorded benchmarks; new structured cases use `whole_claim`.

## Aspect-level classification

`dismech.classifier.aspects.aspect_output_schema(claim)` builds a typed result
map from fields present in a claim. `/` means the whole claim; other keys are
JSON Pointers relative to the claim envelope, such as
`/assertion/phenotype_term/term`. The slash root is a deliberate convention
(RFC 6901 itself uses an empty string for the root).

The default profile selects `term`, `description`, `frequency`, and `temporality`.
A term's ID and label form one assessment. Absent fields produce no question;
other profiles can select different field names. Slot and enum meanings come
from the installed dismech schema, including numeric frequency bands. The whole
claim assessment still covers fields outside the selected profile.

`aspect_prompt()` supplies the shared instructions. A provider compiles each
property description into a question, keeping the complete sanitized claim as
shared context. `TypeSafeClassifier.classify_many()` sends those independent
Choice questions in one request and records usage once. Jev returns judgments,
probabilities and confidence, not curator rationales. Existing single-question
classification remains supported. Review records and target aggregation belong
to the consuming benchmark, not to this model-input schema.
