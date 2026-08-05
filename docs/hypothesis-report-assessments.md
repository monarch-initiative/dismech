# Hypothesis Report Assessments

Provider-generated hypothesis-exploration reports are useful research leads, but
they are not curated disease evidence. An assessment sidecar records a review of
one provider's report by one assessor without silently promoting its claims into
the disease YAML.

## File structure

```text
kb/hypotheses/<Disease>/<hypothesis_id>/
  <provider>.md
  assessments/
    <provider>-assessment-by-<assessor>.yaml
    <provider>-assessment-by-<assessor>.md     # optional narrative
    <provider>-assessment-by-<assessor>.pdf    # optional rendering
```

The YAML sidecar is authoritative. Markdown and PDF files are optional
human-readable artifacts with the same filename stem. The naming makes each
review independently addressable: `openscientist-assessment-by-openai-5-pro.yaml`
and `kosmos-assessment-by-reviewer-a.yaml` can coexist for the same hypothesis,
as can multiple assessors for one provider.

| Artifact | Purpose |
| --- | --- |
| Raw provider report | A hypothesis-exploration lead; it is not a source of truth. |
| Provider-by-assessor assessment | Structured judgment of that report, including source-anchored claim dispositions. |
| Cross-provider research synthesis | Optional reconciliation across reports when comparison itself is needed; see [Cross-Provider Research Synthesis](research-synthesis.md). |
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

## Validation

Validate a sidecar with:

```bash
just validate-hypothesis-assessment \
  kb/hypotheses/<Disease>/<hypothesis_id>/assessments/<provider>-assessment-by-<assessor>.yaml
```

This runs LinkML validation and additionally checks the prescribed filename and
directory, that the raw report and listed artifacts exist, and that every
`report_quote` is a whitespace-normalized verbatim substring of the raw report.
It does not adjudicate biomedical truth; that remains the assessor's documented
reasoning and the project’s normal evidence-curation process.
