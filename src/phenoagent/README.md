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
