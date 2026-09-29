---
name: review-hypothesis-exploration
description: Review one provider-generated mechanistic-hypothesis exploration report, including its dataset use, analyses, and artifacts, or reconcile multiple separately assessed reports for one hypothesis. Use when assessing or comparing Biomni, OpenScientist, Kosmos, or another provider's hypothesis report or computational research run.
---

# Review Hypothesis Exploration

Treat a provider report as a research lead, not as a source of truth. Assess the
report's reasoning and claims without automatically promoting its claims into a
disorder YAML.

## Assess one report

1. Locate the raw report at
   `kb/hypotheses/<Disease>/<hypothesis_id>/<provider>.md` and identify the
   hypothesis directory, provider slug, and any provider artifact bundle. Read
   the report and inventory before judging the run.
2. Inventory every material data source in `data_sources`, including databases
   searched with no result. Distinguish `CITED_NOT_ACCESSED`, `ACCESSED`,
   `SEARCHED_NO_RESULT`, and `UNVERIFIABLE`; a proposed future dataset is not an
   accessed input. Preserve a committed query/response or search-log artifact
   for `ACCESSED` and `SEARCHED_NO_RESULT`. Verify each accession with
   `just verify-datasets --accession <CURIE>` where supported, then separately
   check disease, tissue, cohort, organism, and assay relevance. Resolution does
   not establish relevance.
3. Inventory every claimed computation in `analyses`. Trace input data-source
   IDs through method, software/version, parameters, code/environment, and
   outputs to the assessment claims the report attributes to that analysis;
   status and auditability determine whether execution actually supports them. Use `SUCCEEDED` only when
   inspectable artifacts substantiate execution; otherwise use
   `PARTIAL`, `REPORTED_ONLY`, `FAILED`, or `SKIPPED` as appropriate.
4. Treat tool availability and fallback as evidence-quality facts. If retrieval,
   a data lake, or a scientific tool failed, record the failure and any fallback;
   do not silently treat a literature-only or model-knowledge fallback as a
   provider analysis or independent result. Biomni is disabled at repository
   entry points unless `DISMECH_ENABLE_BIOMNI=1`; do not bypass that opt-in.
   Without it, Biomni must also remain unavailable to automatic provider
   fallback. The hypothesis runner's dry-run command inspection is safe without
   the opt-in.
5. Check the report's consequential claims against the cited primary literature.
   Distinguish direct support, external plausibility, qualification, and
   contradiction. Check taxonomic level, disease/model context, directionality,
   and causal versus correlational language.
6. Create one authoritative YAML sidecar per provider and assessor at
   `assessments/<provider>-assessment-by-<assessor>.yaml`. Use a lowercase,
   hyphenated assessor slug (for example, `openai-5-pro`).
7. Include the relative `source_report`, `hypothesis_id`, an overall verdict,
   and claim-level dispositions. For every assessment claim, use a short
   `report_quote` copied verbatim from the provider report and explain the
   assessment in `rationale`; attach `analysis_ids` only to claims the report
   attributes to those analyses, and use status/auditability to state whether
   execution supports them.
8. Add an optional Markdown narrative and/or PDF using the same stem when it
   helps human review. The YAML remains authoritative; the rendered artifacts
   must be listed in `artifacts`.
9. Apply the hypothesis artifact policy in
   `docs/hypothesis-report-assessments.md`: commit manifests, code, environment
   specifications, and small derived outputs; keep large/raw, controlled, or
   credential-bearing data outside Git and record whether each artifact is
   committed, external, local-only, missing, or not produced. Structured paths
   must be non-empty files beneath `artifact_root: ../<provider>_artifacts`.
   For a computational bundle, require canonical `MANIFEST.yaml`, run
   `just validate-hypothesis-analysis-run <report> <artifact_dir>`, and replay
   the saved code separately; the validator does not execute generated code.
   Confirm that report frontmatter has an `artifact_manifest_sha256` binding to
   the exact current manifest bytes; a manifest edit makes an older report stale.
   If you correct provider code or results after its response, record the exact
   correction and before/after hashes in the manifest, replay it independently,
   and keep the provider analysis at most `PARTIAL` until the provider reruns or
   attests the corrected bytes. Never stamp a stale provider report onto an
   assessor-corrected bundle merely to make the gate pass.
10. Keep a report-review citation as context only. Promote a paper-derived claim
   to the disease YAML only after normal reference-cache and evidence validation.
   Never hand-edit `references_cache/*.md`; use `just fetch-reference <ID>`.
11. Validate the sidecar:

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
   `PROVIDER_EXTRACTION`, `PROVIDER_ANALYSIS`, `PROVIDER_INFERENCE`, `SEED_DERIVED`,
   `PRIOR_PROVIDER_DERIVED`, and `UNKNOWN`. Use `PROVIDER_EXTRACTION` when the
   provider extracts a new claim or detail from a source already cited in its
   seed. Use `PROVIDER_ANALYSIS` for a result the report attributes to a linked
   analysis. It may describe `REPORTED_ONLY` lineage, but that is unverified
   execution and not independent computational support; `FAILED` and `SKIPPED`
   analyses cannot originate a position. When a claim was inherited from an
   earlier provider through the seed, use
   `PRIOR_PROVIDER_DERIVED` plus `derived_from_provider`; do not count it as
   independent convergence. The lineage graph must be acyclic, and a position
   cannot derive from a provider that is `SILENT` on that claim.
7. Compare data and analysis lineage, not just prose. Two providers using the
   same source dataset, seed-derived table, code, or upstream result are not
   independent replication. A shared accession can still support distinct
   analyses only when their methods and outputs are separately auditable.
8. Base the final claim dispositions and `overall_verdict` on checked source
   evidence, not provider majority or citation count. Reconciliation citations
   remain review context, not disease-YAML evidence. Promotion still requires
   normal reference-cache and evidence validation.
9. Validate the reconciliation:

   ```bash
   just validate-hypothesis-reconciliation \
     kb/hypotheses/<Disease>/<hypothesis_id>/reconciliation.yaml
   ```
