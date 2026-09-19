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
`prognosis`, `diagnosis`, `epidemiology`, `comorbidity`), records a
`curation_status` (`INTEGRATED` / `LEAD` / `REJECTED` — a genuine curation
decision), and lists one `provider_support` block per report with:

- `stance` — `CONCORDANT` / `PARTIAL` / `CONTRADICTORY` / `SILENT`
- `score` — curator-assigned concordance/similarity in `[0,1]`
- `best_matching_text` — a **verbatim excerpt** from that provider's report
- `explanation` — why the report earns this stance
- `citations` — the PMIDs/DOIs the provider cited for the claim

Consensus is **not** an authored field — it is derived from the provider
stances (`dismech.research_synthesis.derive_consensus`): any `CONTRADICTORY`
stance → `CONFLICT`; at most one asserting provider → `SINGLE`; more than one,
all `CONCORDANT` → `UNANIMOUS`; otherwise `MAJORITY`. `curation_status`, by
contrast, is a real human decision and is authored.

The artifact deliberately does **not** re-annotate claims with ontology terms or
carry verified literature `evidence:` blocks — that is the job of the main
curation pipeline on the disorder YAML. This file exists only to evaluate and
compare claims across providers, so the only reference provenance it keeps is the
per-provider `citations` (which sources each report leaned on).

## Recording how a provider run went

A `providers[]` entry describes the run as well as the report. Omit these slots
for an ordinary successful run; set them when the run was not ordinary:

- `run_status` — `COMPLETED` / `FAILED` / `UNUSABLE`. `FAILED` means no report
  file was produced (API error, credit exhaustion, timeout), and is the one case
  where `report` may legitimately be absent. `UNUSABLE` means a file exists but
  its content is off-topic or empty; commit the file anyway so the coverage gap
  is attributable.
- `status_detail` — why. Record the actual HTTP status or what the off-topic
  report retrieved instead.
- `nec_preflight_verdict` / `nec_preflight_detail` — the result of
  `just preflight-dr <report> <mondo>` (`PASS` / `WARN` / `FAIL` / `SKIP` /
  `NOT_RUN`). Recording `PASS` matters as much as recording `FAIL`: it tells a
  later reader the Named Entity Confusion check was actually run.

This exists so that an absent provider reads as *attempted and failed* rather
than as *never tried*.

## Recording identifier hallucinations

`identifier_issues[]` on a provider entry records identifier- and quote-level
defects in that report — the failure modes enumerated in
[CLAUDE.md §2a/§2b](https://github.com/monarch-initiative/dismech/blob/main/CLAUDE.md).
Each issue carries an `identifier`, an `issue_kind`, what the report `cited_as`,
what it actually `resolves_to`, an optional `report_quote`, how it was
`verified_with`, and a `disposition` (`DISCARDED` / `CORRECTED` /
`RETAINED_WITH_CAVEAT`).

`issue_kind` values:

| Kind | Meaning |
|---|---|
| `NONEXISTENT_IDENTIFIER` | The ID does not resolve at all — a fabricated PMID/DOI/NCT/accession. |
| `MISATTRIBUTED_IDENTIFIER` | The ID resolves, but to a different work than the report claims. |
| `FABRICATED_QUOTE` | A quoted snippet is not present in the cited source. |
| `NONEXISTENT_ONTOLOGY_TERM` | An HP/GO/CL/CHEBI/NCIT/MONDO CURIE does not exist. |
| `MISMATCHED_ONTOLOGY_LABEL` | The CURIE exists but the report's label for it is not canonical. |
| `NAMED_ENTITY_CONFUSION` | The identifier or passage belongs to a different disease entity (§2b). |
| `OTHER` | Anything else, e.g. a correct identifier described with the wrong journal. |

These are properties of the **report**, not of a harmonized finding, so they are
recorded on the provider rather than on a claim. That placement is deliberate: a
hallucinated citation is most often attached to a claim that gets dropped, so
recording it against the claim would delete the very finding worth keeping. The
point is that the next curator to read that report does not re-trust a citation
this review already disproved.

Note that `MISATTRIBUTED_IDENTIFIER` is the class that defeats eyeballing.
`research/Mitchell-Riley_Syndrome-research-synthesis.yaml` is the worked example:
a report cited `PMID:20040488` for a real RFX6 paper whose actual identifier is
`PMID:20040487`, one digit away, in the same journal and issue. The citation
looks right, resolves successfully, and is wrong. Only resolving the identifier
catches it.

## Free-text narrative

The structured findings capture *what* each provider claimed; an optional
top-level `narrative:` block preserves the qualitative *story* the legacy
freehand `.md` roll-ups carried. It has five optional prose slots mirroring the
old section headings — `overview`, `agreement`, `divergence`, `integration`,
`not_integrated` — plus a free-text `notes` field on the synthesis (and on each
finding) for caveats. Use the narrative to say things that do not reduce to a
per-claim stance; the harmonized findings remain the machine-readable backbone.

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

## Curation is manual

A synthesis is **hand-curated**, not generated. The curator reads every provider
report in full and writes the harmonized statements, per-provider `stance`/`score`,
`best_matching_text` quotes, and `curation_status` directly. There is deliberately
no scaffolding tool that pre-seeds "deterministic" parts (citation intersection,
provider stubs): those shortcuts add little — citation overlap is a weak signal
(providers routinely agree on a claim while citing entirely different papers) —
and a partial auto-fill nudges the curator toward the tool's framing instead of
the reports'. The one automated step is the **validator** (`just validate-synthesis`),
which is a check run *after* curation, never a generator: it confirms the schema
is satisfied and every `best_matching_text` is a verbatim substring of its report.

`best_matching_text` values must be exact quotes from the report files.

## Validation

The artifact validates against a standalone schema,
`src/dismech/schema/research_synthesis.yaml` (`ResearchSynthesis` root class):

```bash
just validate-synthesis research/ALK_Rearranged_NSCLC-research-synthesis.yaml
just validate-synthesis-all
```

`validate-synthesis` also runs `dismech.research_synthesis`, which enforces that
every `best_matching_text` is a verbatim (whitespace-normalized) substring of the
`source_report` it quotes — `linkml-validate` only checks that the field is a
string, so this is what actually prevents fabricated quotes. `tests/test_data.py`
mirrors both checks (schema validity, verbatim quotes, and that each
`provider_support.provider` resolves to a declared top-level provider).

## Worked example

`research/ALK_Rearranged_NSCLC-research-synthesis.yaml` is the reference
implementation, comparing the `falcon` (pathophysiology-focused) and
`openscientist` (comprehensive) reports across eight harmonized findings that
exercise the `CONCORDANT` / `PARTIAL` / `SILENT` stances and the `UNANIMOUS` /
`MAJORITY` / `SINGLE` consensus values.
