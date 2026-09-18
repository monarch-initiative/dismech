# Claim–evidence mismatch classification

Use TypeSafe to vet a snippet against the claim it accompanies, including the
recorded `supports` and `directness`. See issue
[12106](https://github.com/monarch-initiative/dismech/issues/12106).

The small framework is in `src/dismech/classifier/`: a provider-independent task
and result, a TypeSafe HTTP adapter, and one evidence classifier. It uses the
existing `httpx` dependency. No schema changes or KB annotations are written.

## Run

Set `TYPESAFE_API_KEY` in the environment for live calls. Never put it in an input
file or command argument. From the repository root:

```bash
# Inspect the extracted claims without credentials or network access.
uv run python -m dismech.classifier kb/disorders/IKK2_Deficiency.yaml \
  --kb --dry-run --output /tmp/ikk2-tasks.jsonl

# Classify at most 20 evidence items by default; opt into more with --limit.
uv run python -m dismech.classifier kb/disorders/IKK2_Deficiency.yaml \
  --kb --output /tmp/ikk2-assessments.jsonl

# Run the frozen 25-case smoke test.
uv run python -m dismech.classifier \
  experiments/claim_evidence/2026-09-18/cases.jsonl \
  --limit 25 --output /tmp/claim-evidence-results.jsonl
```

Output paths must not exist. A report records the exact task, response
probabilities, model, usage, timestamp and request hash. Errors are separate from
scientific verdicts and make the command exit nonzero; a `MISMATCH` is advisory
and does not fail the command. No automatic acceptance threshold is implemented.
`--model` defaults to the pinned `jev-1.13.0` used in this experiment.

JSONL input rows contain `id`, optional `reference`, and `input`:

```json
{"id":"example","input":{"claim":{"description":"X causes Y"},"context":{"disease":"Example"},"snippet":"X did not cause Y.","supports":"REFUTE","directness":"DIRECT"}}
```

`explanation` is optional. The classifier checks the specific assertion the
explanation claims to justify; it does not treat the explanation as evidence.
Missing or `UNKNOWN` directness asserts nothing about directness. Existing quote
validation remains separate: a semantic `MATCH` does not prove quote authenticity
or scientific truth. Run `just count-verified-snippets FILE` / the authoritative
reference validator as usual.

## KB extraction limitation

`--kb` takes the containing object as the claim, with disease and ancestor
name/description/subtype context. Child causal links are assessed separately.
It removes other evidence, rather than letting sibling quotations establish that
this snippet is appropriate. Top-level evidence uses the document name and
description. Arbitrary cross-file targets are not resolved.

A long object can contain several assertions with separately scoped evidence.
The explanation helps locate the intended assertion but can itself overclaim.
Use explicit JSONL claims when extraction is ambiguous. This is a report-only
prototype, not a whole-KB quality gate.

## Runs

- [2026-09-18](2026-09-18/FINDINGS.md): paired smoke test and two unmodified KB audits.
  Expected smoke-test labels were assigned by the implementing agent before the
  first run; they are not independently adjudicated ground truth.

Recompute metrics from saved responses:

```bash
uv run python experiments/claim_evidence/summarize.py experiments/claim_evidence/2026-09-18
```

`build_cases.py` documents construction and verifies every smoke-test quotation
against the existing reference cache. Regenerating reads the current KB; the
committed `cases.jsonl` is the frozen input for this run. The records distinguish
reconstructed historical failures, constructed claims/annotation flips, and
unmodified KB evidence. Do not treat paired variants as independent examples.
