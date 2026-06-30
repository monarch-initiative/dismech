# Phenoagent

This package contains phenotype-matching and explanation-loop tooling.

## Deterministic Init

Generate an initial matching file:

```bash
just matching-init <phenopacket.json> <disease_ref>
```

## Agentic Explanation Loop (cyberian + Claude)

Run deterministic init, then iterate until no non-match row points to `NO_EXPLANATION`:

```bash
just matching-agent <phenopacket.json> <disease_ref> "" "" --dry-run --verbosity 0
just matching-agent <phenopacket.json> <disease_ref>
```

When `workdir` is not provided, runs default to:

```text
./workdirs/matching/<case_id>/<disease_slug>/<shortuuid>/
```

Direct module entrypoint:

```bash
uv run python -m phenoagent.cyberian_wrapper <phenopacket.json> <disease_ref>
```

## Match-Aware Causal Graph

Render an augmented HTML report (embedded Mermaid + metadata) from a dismech disease model and a matching report:

```bash
just matching-graph <disease_ref_or_path> <matching_report.yaml>
```

Direct module entrypoint:

```bash
uv run python -m phenoagent.match_graph <disease_ref_or_path> <matching_report.yaml>
```

## Phenopacket Match-Quality Eval

Deterministic evaluation of the matcher against phenopackets that carry a
ground-truth diagnosis (`interpretations[].diagnosis.disease` or top-level
`diseases[]`). For each packet the eval resolves the ground-truth disease to a
dismech disorder, runs the matcher against *that true disease only*, and reports
phenotype-overlap quality plus KB coverage.

```bash
# Bundled fixtures (default)
just phenopacket-eval

# A phenopacket-store checkout (gene-organized notebooks/<GENE>/phenopackets/*.json)
just phenopacket-eval projects/PHENOPACKETS/files/phenopacket-store
```

Direct module entrypoint:

```bash
uv run python -m phenoagent.eval <phenopacket_or_dir>... [--store-dir DIR] \
    [--kb-dir kb/disorders] [--json out.json] [--markdown out.md]
```

**Metrics** (per scored packet, averaged in the summary):
- `exact_recall` — case terms with an exact model match / case terms
- `related_recall` — exact + broader/narrower matches / case terms
- `model_coverage` / `weighted_model_coverage` — modelled phenotypes hit by the
  case (the weighted form scores by frequency: OBLIGATE > VERY_FREQUENT > …)

**Coverage**: a packet whose ground-truth disease is not in dismech is reported
as a `KB_MISS` (feeds the KB-coverage rate); packets with no ground truth are
`NO_GROUND_TRUTH`.

> **Why not `pr_is_diagnosis`?** At deterministic init every non-exact /
> model-only row points to `NO_EXPLANATION` (probability 0.0), so the product
> `pr_is_diagnosis` is ~0.0 for every packet — it only becomes meaningful after
> the agentic explanation loop assigns real probabilities. The eval therefore
> grades on the match-quality surrogate above and reports `pr_is_diagnosis`
> alongside purely so a zero column is not mistaken for a broken matcher.

This v1 is the minimal *match-quality* scope (each packet scored only against
its true disease). Candidate **ranking** (score every packet against all
disorders, report rank-of-true-diagnosis) and a pinned phenopacket-store
**fetch** recipe are the scoped follow-ups.
