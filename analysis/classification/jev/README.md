# Jev assessment history

One file per disease and classification task: `<Disease>/evidence_claim_match.yaml`.
These are generated model assessments for recuration triage; keep historical
claim snapshots and scores when the disease changes.

Use `just jev-audit` to assess new inputs and `just jev-audit-cache` to reconcile
`active` flags without inference. See the [audit guide](../../../docs/jev-evidence-audit.md)
for the record fields, timestamps, import/merge commands and weekly workflow.

Only the audit/cache commands should update these YAML files. `active` describes
the input's presence at the last recorded inventory, not the currency of a model
or prompt. A future HTML renderer must match the current assessment hash before
showing a score.
