---
name: review-hypothesis-exploration
description: Review a provider-generated mechanistic-hypothesis exploration report and record a structured, source-anchored assessment sidecar. Use when assessing OpenScientist, Kosmos, or another provider report for one hypothesis.
---

# Review Hypothesis Exploration

Treat a provider report as a research lead, not as a source of truth. Assess the
report's reasoning and claims without automatically promoting its claims into a
disorder YAML.

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

For comparative reconciliation of multiple provider reports, create a separate
cross-provider synthesis only when it is needed. Do not replace independent
provider-by-assessor assessments with a synthesis.
