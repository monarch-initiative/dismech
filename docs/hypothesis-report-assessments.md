# Hypothesis Report Assessments and Reconciliation

Provider-generated hypothesis-exploration reports are useful research leads, but
they are not curated disease evidence. An assessment sidecar records a review of
one provider's report by one assessor without silently promoting its claims into
the disease YAML. When two or more separately assessed reports address the
same hypothesis, one hypothesis-local reconciliation can record where their
claims converge, diverge, or merely repeat material supplied in their seeds.

## File structure

```text
kb/hypotheses/<Disease>/<hypothesis_id>/
  <provider-a>.md
  <provider-b>.md
  reconciliation.yaml
  assessments/
    <provider-a>-assessment-by-<assessor>.yaml
    <provider-b>-assessment-by-<assessor>.yaml
    <provider>-assessment-by-<assessor>.md       # optional narrative
    <provider>-assessment-by-<assessor>.pdf      # optional rendering
```

Each assessment YAML is authoritative for that provider-by-assessor review.
Markdown and PDF files are optional human-readable artifacts with the same
filename stem. The naming makes each review independently addressable:
`openscientist-assessment-by-openai-5-pro.yaml` and
`biomni-assessment-by-reviewer-a.yaml` can coexist for the same hypothesis, as
can multiple assessors for one provider. `reconciliation.yaml` is the single
authoritative comparison for the hypothesis; it points to the selected
assessment for each provider rather than replacing those reviews.

| Artifact | Purpose |
| --- | --- |
| Raw provider report | A hypothesis-exploration lead; it is not a source of truth. |
| Provider-by-assessor assessment | Structured judgment of that report, including source-anchored claim dispositions. |
| Hypothesis reconciliation | Optional, structured comparison of two or more separately assessed reports about one `hypothesis_id`. |
| Disease-level research synthesis | Cross-provider harmonization of broad disease reports under `research/`; see [Cross-Provider Research Synthesis](research-synthesis.md). |
| Disease YAML | Curated, literature-grounded knowledge only. |

## Assessment YAML

Each sidecar identifies the provider, assessor, raw report, and hypothesis. Its
`claims` record the disposition of an individual report assertion or inference:

```yaml
provider: openscientist
assessor: openai-5-pro
source_report: ../openscientist.md
hypothesis_id: example_hypothesis
overall_verdict: WEAKLY_SUPPORTED_UNRESOLVED
claims:
  - claim_id: example-claim
    statement: Provider-neutral description of the assessed claim.
    disposition: QUALIFIED
    report_quote: Exact words copied from the raw provider report.
    rationale: Why the claim was qualified.
    citations:
      - PMID:12345678
```

Allowed overall verdicts are `SUPPORTED`, `PARTIALLY_SUPPORTED`,
`WEAKLY_SUPPORTED_UNRESOLVED`, `UNRESOLVED`, `REFUTED`, and `INCONCLUSIVE`.
Claim dispositions are `RETAINED`, `QUALIFIED`, `REJECTED`, and
`NEEDS_VERIFICATION`.

`report_quote` is a short verbatim anchor to the reviewed report, rather than a
quote from a paper. `citations` identify sources the assessor consulted; they
are review context, not automatically evidence in the disease YAML. A
paper-derived claim is promoted only through the normal reference cache and
evidence-validation workflow.

## Reconciliation YAML

Create `reconciliation.yaml` only when comparing providers adds useful
information. Every input must already have a separate assessment; a
reconciliation is not a shortcut around reviewing each report. The selected
assessments may share an assessor, but each source report must be reviewed on its
own first. The reconciliation names one selected assessment and its corresponding
raw report for every provider. `reconciled_at`, `overall_verdict`, `summary`, and
at least one reconciled claim are required:

```yaml
schema_version: '1.0.0'
assessor: codex
hypothesis_id: example_hypothesis
reconciled_at: '2026-08-29T00:00:00Z'
providers:
  - provider: biomni
    source_assessment: assessments/biomni-assessment-by-codex.yaml
    source_report: biomni.md
    contribution_summary: Concrete experiment proposals.
    limitations: Literature retrieval failed, so cited claims came from the seed.
  - provider: openscientist
    source_assessment: assessments/openscientist-assessment-by-reviewer-a.yaml
    source_report: openscientist.md
    contribution_summary: Broader primary-literature discovery.
    limitations: One disease-specific inference was rejected on source review.
overall_verdict: PARTIALLY_SUPPORTED
summary: The shared scaffold is plausible, but its distinctive human edge is untested.
reconciled_claims:
  - claim_id: example-reconciled-claim
    claim_kind: SCIENTIFIC_CLAIM
    statement: Provider-neutral statement being reconciled.
    disposition: QUALIFIED
    rationale: Why this is the final disposition after comparing the reviews.
    provider_support:
      - provider: biomni
        stance: SILENT
        rationale: The Biomni report does not address this claim.
      - provider: openscientist
        stance: CONCORDANT
        assessment_claim_ids:
          - example-claim
        report_quote: Exact words copied from the OpenScientist report.
        claim_origin: PROVIDER_DISCOVERY
        rationale: The report surfaced this claim through its own retrieval.
    citations:
      - PMID:12345678
```

Each reconciled claim has one final assessment `disposition`, using the same
`RETAINED`, `QUALIFIED`, `REJECTED`, and `NEEDS_VERIFICATION` values as an
individual assessment. `claim_kind` distinguishes `SCIENTIFIC_CLAIM`,
`EVIDENCE_QUALITY`, `COVERAGE`, and `RESEARCH_PRIORITY` comparisons.

Every claim must include exactly one `provider_support` block for every declared
provider, and every `claim_id` must be unique. `stance` describes what the raw report says relative to the
provider-neutral statement (`CONCORDANT`, `PARTIAL`, `CONTRADICTORY`, or
`SILENT`); it is not itself the reconciler's endorsement. For a non-`SILENT`
position, `assessment_claim_ids` must resolve in the selected source
assessment, `report_quote` must be a whitespace-normalized verbatim substring of
the raw report, and `claim_origin` must record whether the position was
`PROVIDER_DISCOVERY`, `PROVIDER_EXTRACTION`, `PROVIDER_INFERENCE`,
`SEED_DERIVED`, `PRIOR_PROVIDER_DERIVED`, or `UNKNOWN`.
`PROVIDER_EXTRACTION` means the provider extracted a new claim or detail from a
source that its seed already cited; it is distinct from discovering a new source.
`PRIOR_PROVIDER_DERIVED` also requires `derived_from_provider`; provider lineage
must be acyclic and cannot derive from a provider that is `SILENT` on that claim.
A `SILENT` position omits claim anchors and lineage.

This lineage is important when one provider was seeded with another provider's
findings: repetition is not independent convergence. More generally, provider
agreement and citation count do not establish biomedical truth. Base the final
disposition and overall verdict on the independently checked evidence. As with
assessment citations, reconciliation `citations` are review context and require
the normal reference-cache and evidence-validation workflow before promotion to
the disease YAML.

This file is narrower than `research/<Disease>-research-synthesis.yaml`. A
hypothesis reconciliation compares focused reports about one hypothesis beside
those reports; a disease-level research synthesis harmonizes broad reports across
the whole disorder.

## Validation

Validate one assessment or every assessment with:

```bash
just validate-hypothesis-assessment \
  kb/hypotheses/<Disease>/<hypothesis_id>/assessments/<provider>-assessment-by-<assessor>.yaml

just validate-hypothesis-assessment-all
```

Validate one reconciliation or every reconciliation with:

```bash
just validate-hypothesis-reconciliation \
  kb/hypotheses/<Disease>/<hypothesis_id>/reconciliation.yaml

just validate-hypothesis-reconciliation-all
```

Assessment validation checks the prescribed filename and directory, source and
artifact existence, and raw-report quote anchoring. Reconciliation validation
also requires at least two unique providers; keeps reports, assessments, and
artifacts inside the hypothesis directory; checks that each selected assessment
has matching provider, hypothesis, and report metadata; resolves assessment claim
IDs; rejects duplicate source-assessment claim IDs; requires each raw `.md` report
directly under the hypothesis directory; enforces all-provider claim coverage and
acyclic lineage rules; and verifies nonblank raw-report quotes. These checks establish structural and source-traceability
integrity, not biomedical truth; that remains the assessor's documented reasoning
and the project's normal evidence-curation process.
