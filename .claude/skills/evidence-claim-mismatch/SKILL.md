---
name: evidence-claim-mismatch
description: >-
  Review and repair mismatches between claims and evidence snippets in an existing
  dismech disease entry. Use for evidence-claim-mismatch issues, evaluation-queue
  findings, or a requested claim/snippet audit.
---

# Review evidence–claim mismatches

Find claims whose selected snippets do not support what the YAML asserts. Expand
the literature search to include more papers where necessary. Evaluation results
are leads for review, not instructions to agree with a model.

## Read the claim in context

- Read the current disease YAML and the issue discussion, including linked PRs.
  Issue examples are saved evaluation inputs and may lag behind edits. Skip
  resolved findings; do not recreate old problems to match a snapshot.
- Use the linked saved assessments to go beyond the issue's few examples.
  Assess the disease/subtype and inherited context as well as the assertion's
  terms, descriptions, qualifiers, support/refutation, and directness. `/` means
  the whole claim; other paths identify individual aspects of that claim.
- A snippet may support the term but not a bundled description or qualifier.
  Distinguish overclaiming from a claim that is simply less detailed than its
  source. A broader, correctly supported claim does not need to repeat every
  detail of the excerpt.
- Nested claims with their own evidence are separate assertions. In particular,
  evidence on a pathophysiology node need not justify its downstream edges.
  Check those edges' evidence separately. Consider complementary evidence on the
  assertion before deciding that the KB claim itself is unsupported.
- Treatment/medical-action claims may describe hypotheses about an action's
  effect on a mechanism; do not automatically read them as clinical recommendations.

## Repair the evidence or claim

Read the cached reference to understand the passage, while asking whether the
selected snippet conveys the needed support. The task is claim–snippet fit,
not rating the source. Extend or replace a snippet to make its context clear;
`...` and `[editorial context]` are available when faithful to the source.
Do not add an unsupported qualifier inside editorial brackets. Follow
[dismech-references](../dismech-references/SKILL.md) for quoting, cache generation,
and validation.

Retain correct claims and limitations. Revise an assertion only when the evidence
justifies doing so; seek additional literature if the existing sources do not
cover it. `PARTIAL` can reflect weak, incomplete, or ambiguous support and is not
by itself an error. Record the reason when a flagged claim should remain.

Follow `CLAUDE.md` for history records and validation. Make targeted YAML edits
without unrelated serialization churn. Summarize the substantive corrections and
retained findings in the curation history. Link the PR with `Closes #<issue>` so
merging completes the queued task. If review finds no changes necessary, explain
the findings on the issue and close it without a content PR.
