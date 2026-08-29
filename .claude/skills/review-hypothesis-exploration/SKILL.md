---
name: review-hypothesis-exploration
description: Review one provider-generated mechanistic-hypothesis exploration report, or reconcile multiple separately assessed reports for one hypothesis. Use when assessing or comparing Biomni, OpenScientist, Kosmos, or another provider's hypothesis report.
---

# Review Hypothesis Exploration

Treat a provider report as a research lead, not as a source of truth. Assess the
report's reasoning and claims without automatically promoting its claims into a
disorder YAML.

## Assess one report

1. Locate the raw report at
   `kb/hypotheses/<Disease>/<hypothesis_id>/<provider>.md` and identify the
   hypothesis directory and provider slug.
2. Check the report's consequential claims against the cited primary literature.
   Distinguish direct support, external plausibility, qualification, and
   contradiction. Check taxonomic level, disease/model context, directionality,
   and causal versus correlational language.
3. Create one authoritative YAML sidecar per provider and assessor at
   `assessments/<provider>-assessment-by-<assessor>.yaml`. Use a lowercase,
   hyphenated assessor slug (for example, `openai-5-pro`).
4. Include the relative `source_report`, `hypothesis_id`, an overall verdict,
   and claim-level dispositions. For every assessment claim, use a short
   `report_quote` copied verbatim from the provider report and explain the
   assessment in `rationale`.
5. Add an optional Markdown narrative and/or PDF using the same stem when it
   helps human review. The YAML remains authoritative; the rendered artifacts
   must be listed in `artifacts`.
6. Keep a report-review citation as context only. Promote a paper-derived claim
   to the disease YAML only after normal reference-cache and evidence validation.
   Never hand-edit `references_cache/*.md`; use `just fetch-reference <ID>`.
7. Validate the sidecar:

   ```bash
   just validate-hypothesis-assessment \
     kb/hypotheses/<Disease>/<hypothesis_id>/assessments/<provider>-assessment-by-<assessor>.yaml
   ```

## Reconcile multiple assessed reports

Create a reconciliation only when comparing at least two provider reports adds
useful information.

1. Ensure every input report has a separate, valid
   `assessments/<provider>-assessment-by-<assessor>.yaml`. If an assessment is
   missing, complete the single-report workflow first. A reconciliation never
   replaces report-by-report assessment; the selected assessments may share an
   assessor, but each source report must be reviewed on its own first.
2. Read every selected raw report and assessment in full. Create one authoritative
   `kb/hypotheses/<Disease>/<hypothesis_id>/reconciliation.yaml`, using a
   lowercase, hyphenated `assessor` slug and
   `src/dismech/schema/hypothesis_reconciliation.yaml`. Record `reconciled_at`,
   an `overall_verdict`, and its concise `summary`.
3. In `providers`, link each `provider` to both `source_report` and
   `source_assessment`, relative to `reconciliation.yaml`. Record each report's
   distinctive contribution and material limitations when useful. The selected
   assessment's provider, hypothesis, and resolved report must match these links;
   the provider slug does not have to equal the raw report filename stem. Each
   raw report must be a `.md` file directly in the hypothesis directory, not a
   citation sidecar.
4. Phrase each `reconciled_claims[].statement` provider-neutrally, classify it as
   `SCIENTIFIC_CLAIM`, `EVIDENCE_QUALITY`, `COVERAGE`, or `RESEARCH_PRIORITY`,
   and assign the final assessment `disposition` with a reasoned `rationale`.
5. Give every reconciled claim exactly one `provider_support` block per declared
   provider. `stance` describes what the raw report says relative to the claim;
   it is not the reconciler's endorsement. For `CONCORDANT`, `PARTIAL`, or
   `CONTRADICTORY`, cite resolving `assessment_claim_ids`, copy a short verbatim
   `report_quote` from the raw report, record `claim_origin`, and explain the
   position. For `SILENT`, omit claim anchors and lineage and explain the silence.
6. Use `claim_origin` to distinguish `PROVIDER_DISCOVERY`,
   `PROVIDER_EXTRACTION`, `PROVIDER_INFERENCE`, `SEED_DERIVED`,
   `PRIOR_PROVIDER_DERIVED`, and `UNKNOWN`. Use `PROVIDER_EXTRACTION` when the
   provider extracts a new claim or detail from a source already cited in its
   seed. When a claim was inherited from an earlier provider through the seed, use
   `PRIOR_PROVIDER_DERIVED` plus `derived_from_provider`; do not count it as
   independent convergence. The lineage graph must be acyclic, and a position
   cannot derive from a provider that is `SILENT` on that claim.
7. Base the final claim dispositions and `overall_verdict` on checked source
   evidence, not provider majority or citation count. Reconciliation citations
   remain review context, not disease-YAML evidence. Promotion still requires
   normal reference-cache and evidence validation.
8. Validate the reconciliation:

   ```bash
   just validate-hypothesis-reconciliation \
     kb/hypotheses/<Disease>/<hypothesis_id>/reconciliation.yaml
   ```
