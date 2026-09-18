# First TypeSafe claim–evidence mismatch experiment

The classifier detected all 13 deliberately selected mismatches and accepted all
12 expected matches in a 25-case smoke test. On unmodified KB evidence it also
produced clear false alarms. This is promising for review triage, not evidence
that it is ready to gate curation.

## What ran

- Model: `jev-1.13.0`, TypeSafe HTTP API, 2026-09-18 UTC.
- One binary Choice question per evidence item: does the snippet justify the
  claim as annotated, including `supports` and `directness`?
- 25 frozen smoke-test inputs in `cases.jsonl`, followed by all 20 evidence
  items in `IKK2_Deficiency` and all 38 in `Diabetic_Retinopathy` at local commit
  `088e3bce6ee`.
- Two versions: 166 requests total, no service errors. Every selected quotation
  passed the existing cache-backed snippet checker (25 smoke-test cases and 58
  original evidence items). Reference caches and KB entries were not modified.
- Each response JSONL records its full input/task, prompt version, probabilities,
  response model, token usage, timestamp, elapsed time, and request hash.

The smoke-test expectations were assigned by the implementing agent before
running the model. They are not independent expert labels. Most cases are
constructed claims or annotation flips around real quotations; five reconstruct
historical review failures/comparisons, and two retain unmodified KB objects.
Paired variants share quotations. These are development examples, not a held-out
benchmark or a corpus accuracy estimate.

## Results

| Input | Version 1 | Version 2 (current) |
| --- | --- | --- |
| 25 smoke-test cases | 25/25 agree with expectations | 25/25 agree with expectations |
| Expected mismatches | 13/13 detected | 13/13 detected |
| Expected matches | 12/12 accepted | 12/12 accepted |
| IKK2, 20 unmodified items | 7 flagged | 8 flagged |
| Diabetic retinopathy, 38 unmodified items | 23 flagged | 18 flagged |

Audit flags are model judgments, not confirmed defects. The 58 unmodified items
were not comprehensively adjudicated, so no precision/recall is claimed for them.

Version 1 required each snippet to establish every material part of the parent
object, and extraction retained child-edge descriptions. That overreached when
several evidence items supported different assertions in one long description.
Version 2 excludes child links from the parent claim and uses the explanation to
locate the assertion being justified, while explicitly treating the explanation
as an assertion to check, not as additional evidence. Both the prompt and extraction
changed; this is not a controlled estimate of either change's separate effect.
The old inputs and outputs are retained unchanged for comparison.

## Useful behavior

- **Generic quotation, specific claim:** the DR prevention sentence does not
  establish laser treatment, vitrectomy, or a 50%/one-year progression rate.
  All three reconstructed mismatches were detected. A deliberately persuasive
  explanation asserting that the guideline confirms laser cost-effectiveness
  did not fool it.
- **Wrong gene:** the comparator passage describes NFKBIA patients' infections,
  not an IKBKB cohort's pneumocystis finding. The reconstructed failure from
  issue [10751](https://github.com/monarch-initiative/dismech/issues/10751) was
  flagged; changing the claim to NFKBIA produced a match. Version 2 assigned
  mismatch probability **0.64** to the wrong-gene case: demanding 0.8 before
  reporting would miss this particular failure.
- **Direction matters:** a snippet saying TREC screening misses IKBKB cases
  correctly matches a `REFUTE` annotation on a claim that screening detects
  them (match probability 0.99). Incorrect direction flips were detected.
- **Directness matters:** mouse conduction evidence matched an appropriately
  inferential human mechanism claim (`INDIRECT`, match probability 0.85), but
  the same claim marked `DIRECT` was flagged (mismatch probability 0.92).
- **Unmodified KB:** severe NPDR staging/progression attached to generic public
  health text was flagged at 0.98, and PRP attached to that same generic text at
  0.97. These agree with the existing eye-disorder mismatch review.
- **Scope mismatch:** the IKK2 prevalence item asserts `ULTRA_RARE` but quotes
  only “rare”; it was flagged at 0.87. This is a useful review candidate, not
  an adjudication of the disease's true prevalence.

## False alarms and limitations

The current model still struggles with correctly scoped evidence inside a long
parent description. Concrete examples from `retinopathy-audit-v2.jsonl`:

- `treatments[1].evidence[0]`: the quote explicitly says panretinal
  photocoagulation is the primary treatment for PDR, and the explanation claims
  exactly that support. The classifier nevertheless flags it at **0.73**.
  Contrast the genuinely uninformative generic prevention quotation at the next
  evidence item, flagged at 0.97.
- `treatments[0].evidence[1]`: a quotation explicitly calling anti-VEGF the
  standard of care for DME is flagged at **0.58**, despite matching the stated
  explanation. The parent description contains many additional treatment facts.
- `pathophysiology[2].evidence[2]`: the quote explicitly frames PDR as a
  neurovascular/inflammatory disease with glial activation, matching the
  explanation's contextual claim, but is flagged at **0.88**. Thus even a high
  probability is not a dependable gate.

These are the implementing agent's readings of the saved inputs; TypeSafe
returns a typed choice and probabilities, not a rationale. The proposed cause
(long-description scope) is an interpretation, not a model-reported explanation.

Version 2 corrected some other apparent overreach, including the ROS/inflammation
feedback quotation and the macular-edema quotation, but flipped one fungal
infection item from MATCH to MISMATCH. A lower total flag count alone does not
establish improvement.

No whole source paper was supplied: the question is whether the agent's chosen
snippet does its claimed job. Context is extracted from the KB, and can be
ambiguous or contain more assertions than that one snippet addresses. Existing
`supports` and `directness` are always included, never hidden. Missing directness
is not silently upgraded to DIRECT. Correct `NO_EVIDENCE` is also allowed.

## Practical conclusion

Keep the binary check and the small framework. It catches the intended lazy
citation failure on these examples, including when the agent supplies a confident
but unsupported explanation. Use its report as a review queue and inspect each
flag. The next useful refinement is to test a cleaner representation of the
specific claim being justified against the concrete false alarms above, without
letting a narrow explanation excuse an unrelated parent claim. Do not add more
classification axes or wire this into a mandatory gate yet.

## Reproduce

See [the experiment README](../README.md) for live commands. Recompute counts from
saved responses without API access:

```bash
uv run python experiments/claim_evidence/summarize.py experiments/claim_evidence/2026-09-18
```

Version 2 used 94,745 input tokens across its 83 requests. Summed per-request
elapsed time was 18.774 seconds (the three commands ran concurrently, so this is
not wall-clock duration). The 25-case smoke test took 5.217 seconds of summed
request time. These are this run's measurements, not latency guarantees.
