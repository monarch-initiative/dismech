# Cross-Provider Research Synthesis

When a disorder has deep-research reports from **more than one provider**
(`research/<Disease>-deep-research-<provider>.md`), the comparison between those
reports is curated as a structured, validated artifact:

```
research/<Disease>-research-synthesis.yaml
```

This supersedes the earlier freehand `*-research-synthesis.md` roll-ups, which
had ad-hoc frontmatter (hardcoded to a `falcon`/`openscientist` pair, or absent)
and inconsistent, prose-only body sections that no tooling validated.

## What it captures

The unit of curation is a **harmonized finding** — one canonical, provider-neutral
claim — paired with a **per-provider assessment** scoring how each report stands
relative to that claim. This is curation *workspace* provenance; it is distinct
from the integrated `references:`/`findings:` block that survives into the
disorder YAML (`kb/disorders/<Disease>.yaml`). The disease entry holds what was
promoted; the synthesis holds the cross-provider reasoning that got you there.

Each harmonized finding is tagged to the dismech `sections` it informs
(`pathophysiology`, `phenotype`, `treatment`, `genetic_factor`, `gene_function`,
`prognosis`, `diagnosis`, `epidemiology`, `comorbidity`), records an overall
`consensus` (`UNANIMOUS` / `MAJORITY` / `SINGLE` / `CONFLICT`) and a
`curation_status` (`INTEGRATED` / `LEAD` / `REJECTED`), and lists one
`provider_support` block per report with:

- `stance` — `CONCORDANT` / `PARTIAL` / `CONTRADICTORY` / `SILENT`
- `score` — curator-assigned concordance/similarity in `[0,1]`
- `best_matching_text` — a **verbatim excerpt** from that provider's report
- `explanation` — why the report earns this stance
- `citations` — the PMIDs/DOIs the provider cited for the claim

The artifact deliberately does **not** re-annotate claims with ontology terms or
carry verified literature `evidence:` blocks — that is the job of the main
curation pipeline on the disorder YAML. This file exists only to evaluate and
compare claims across providers, so the only reference provenance it keeps is the
per-provider `citations` (which sources each report leaned on).

## Relationship to `deep-research-client`

The schema deliberately mirrors the field names in
`deep_research_client.evaluation.models` (that package's `GroundTruthClaim.category`,
and `ClaimMatch.matched` / `similarity_score` / `best_matching_text` /
`explanation`) so the curated artifact interoperates with the deep-research-client
evaluation harness. The two additions over that harness are:

1. an **aggregate** that groups every provider under one harmonized finding
   (the harness scores each provider independently, one `EvalResult` per
   provider); and
2. an explicit **`stance`** enum that distinguishes concordance from
   contradiction (the harness's `ClaimMatch` is coverage-only —
   `matched` true/false).

## What is deterministic vs. agentic

- **Deterministic** (a script can help): intersecting the citation sets across
  providers, and pre-listing the provider reports.
- **Agentic** (the curator): extracting the harmonized statements, assigning
  each provider's `stance`/`score`, and deciding `curation_status`. These are
  qualitative judgments and are not auto-generated.

`best_matching_text` values must be exact quotes from the report files.

## Validation

The artifact validates against a standalone schema,
`src/dismech/schema/research_synthesis.yaml` (`ResearchSynthesis` root class):

```bash
just validate-synthesis research/ALK_Rearranged_NSCLC-research-synthesis.yaml
just validate-synthesis-all
```

`tests/test_data.py` also validates every `research/*-research-synthesis.yaml`
against the schema and checks that each `provider_support.provider` resolves to a
declared top-level provider.

## Worked example

`research/ALK_Rearranged_NSCLC-research-synthesis.yaml` is the reference
implementation, comparing the `falcon` (pathophysiology-focused) and
`openscientist` (comprehensive) reports across eight harmonized findings that
exercise the `CONCORDANT` / `PARTIAL` / `SILENT` stances and the `UNANIMOUS` /
`MAJORITY` / `SINGLE` consensus values.
