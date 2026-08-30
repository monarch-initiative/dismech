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
  <provider-a>_artifacts/                         # optional provider bundle
    MANIFEST.yaml                                 # required for computational bundles
    analysis.py                                   # example committed code
    results.tsv                                   # example small derived output
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
| Provider artifact bundle | Code, manifests, environment specifications, and small derived outputs that make data-backed claims auditable. |
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

## Dataset and analysis inventory

An assessment covers the provider's research run, not only its prose. Use
`data_sources` and `analyses` whenever the report names a dataset/database,
claims a computation, reports a negative search, or proposes a future analysis.
These blocks distinguish data actually used from data merely discussed.

```yaml
data_sources:
  - data_source_id: geo-gse197406
    source_type: PUBLIC_DATASET
    name: Wilson disease liver transcriptome
    identifier: geo:GSE197406
    access_status: ACCESSED
    retrieved_at: '2026-08-29T21:58:56Z'
    cohort: Liver tissue from people with Wilson disease and controls.
    subset: Samples retained after the provider's documented quality filters.
    organism: Homo sapiens
    tissue: Liver
    assay: Affymetrix Human Genome U133 Plus 2.0 Array
    checksum: sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
    byte_count: 2831048
    source_artifacts:
      - ../biomni_artifacts/MANIFEST.yaml
      - ../biomni_artifacts/input_manifest.tsv
      - ../biomni_artifacts/sample_manifest.tsv
  - data_source_id: geo-gpl570
    source_type: PUBLIC_DATASET
    name: GPL570 platform annotation
    identifier: geo:GPL570
    access_status: ACCESSED
    retrieved_at: '2026-08-29T21:58:57Z'
    organism: Homo sapiens
    assay: Affymetrix Human Genome U133 Plus 2.0 Array annotation
    source_artifacts:
      - ../biomni_artifacts/MANIFEST.yaml
      - ../biomni_artifacts/input_manifest.tsv
analyses:
  - analysis_id: wilson-liver-de
    status: PARTIAL
    auditability: REPRODUCIBLE
    method: >-
      Per-probe two-sided Welch tests on the deposited log2-like expression
      scale, with Benjamini-Hochberg correction over all platform probes.
    comparison: Wilson disease liver versus normal-control liver.
    input_data_source_ids:
      - geo-gse197406
      - geo-gpl570
    software:
      - software_name: Python
        software_version: '3.12.9'
      - software_name: SciPy
        software_version: '1.18.1'
      - software_name: statsmodels
        software_version: '0.15.0'
    parameters:
      - transform=none
      - test=two-sided Welch t-test per probe
      - multiplicity=Benjamini-Hochberg over all platform probes
    code_artifacts:
      - ../biomni_artifacts/analysis.py
    environment_artifact: ../biomni_artifacts/environment.txt
    output_artifacts:
      - ../biomni_artifacts/sample_manifest.tsv
      - ../biomni_artifacts/probe_level_results.tsv
      - ../biomni_artifacts/gene_level_results.tsv
    status_reason: >-
      The corrected replay is reproducible, but the provider did not attest the
      correction, so the assessment does not grade it as SUCCEEDED.
    limitations: Small cohort, age imbalance, and transplant-versus-resection confounding.
claims:
  - claim_id: copper-iron-expression-shift
    statement: Wilson disease liver shows a specified iron-homeostasis expression shift.
    disposition: QUALIFIED
    report_quote: Exact words copied from the provider report.
    rationale: The direction is present, but the cohort is small and confounded.
    analysis_ids:
      - wilson-liver-de
```

When any structured source or analysis artifact is present, the assessment also
declares its provider-specific root:

```yaml
artifact_root: ../biomni_artifacts
```

The root must be exactly `../<provider>_artifacts/`; all `source_artifacts`,
`code_artifacts`, `environment_artifact`, and `output_artifacts` must be
non-empty regular files beneath it. This prevents one provider from borrowing
another provider's code or outputs and appearing independently reproducible.

### Data-use classifications

Classify what happened, not what the report's rhetoric implies:

| Situation | Record |
| --- | --- |
| Provider downloaded, queried, or otherwise read the source | `access_status: ACCESSED`; a database/API access also records the exact query |
| Provider documents a scoped search that returned no usable result | `SEARCHED_NO_RESULT`, with query, date, and a committed response/log artifact |
| Report cites or recommends a dataset but did not inspect it | `CITED_NOT_ACCESSED` |
| Access cannot be established from the report or artifacts | `UNVERIFIABLE` |
| Provider proposes an analysis for future work | Data source is normally `CITED_NOT_ACCESSED`; analysis is `SKIPPED` with the proposal in `status_reason` |
| Provider claims an analysis but supplies no inspectable execution evidence | Analysis is `REPORTED_ONLY` / `UNVERIFIABLE`, not `SUCCEEDED` |

An accession resolving is necessary but not sufficient. For supported prefixes,
run `just verify-datasets --accession <CURIE>` to check existence. Then inspect
the repository record for disease/entity identity, organism, tissue, cohort,
assay, and comparison relevance. A real sibling-disease or gene-only dataset is
still the wrong input. Run `just verify-datasets` again if a dataset is later
promoted into a disorder YAML.

### Analysis and claim lineage

Every computed claim should have an inspectable chain:

```text
data_sources[] -> analyses[].input_data_source_ids -> method/code/environment
               -> analyses[].output_artifacts -> claims[].analysis_ids
               -> reconciliation provider_support[].analysis_ids
```

Record versioned software, material parameters, input subset/cohort, code or
workflow, environment, and result files. `SUCCEEDED` is intentionally strict:
it requires accessed inputs, versioned software, and enough committed
code/environment/output material for `auditability: REPRODUCIBLE`. A successful
negative-search analysis may use a documented `SEARCHED_NO_RESULT` input. Use `PARTIAL`
when execution produced only part of the intended result, `FAILED` for a failed
attempt, `SKIPPED` for an analysis not run, and `REPORTED_ONLY` when prose claims
execution but the repository cannot substantiate it. A fully captured failure
may itself be `REPRODUCIBLE` (rerunning reproduces the failure); a reported-only
analysis may be `PARTIALLY_AUDITABLE` when a provider table or plot survives, or
`UNVERIFIABLE` when only prose survives. Neither outcome substantiates
execution. A reported-only analysis cannot support a `RETAINED` assessment
claim, and a `QUALIFIED` computational claim must link at least one succeeded or
partial analysis.

Fallback is part of this lineage. If a provider's database, data lake, package,
or scientific tool is unavailable, keep the failed/skipped attempt as its own
analysis record. If a lower-fidelity analysis actually runs instead, record it
separately and set its `fallback_from_analysis_id` to the failed, partial, or
skipped attempt; every such link requires an explanation in `status_reason`.
Do not silently relabel
literature synthesis or model knowledge as a computational result; when that is
the only fallback, document it in the failed attempt's `status_reason` rather
than inventing a second analysis.

## Hypothesis artifact policy

Provider bundles normally live at
`kb/hypotheses/<Disease>/<hypothesis_id>/<provider>_artifacts/`. Keep the report
useful after the provider service or local cache disappears, without turning Git
into a raw-data warehouse.

Every computational provider bundle uses `MANIFEST.yaml` as its canonical
machine-readable run manifest. It records schema version `1.0`, run status,
fallback and direct-execution flags, inputs and outputs with byte counts and
SHA-256 checksums, and clean-replay verification. In the manifest's `sha256`
field, store exactly 64 lowercase hexadecimal characters; the assessment's
generic `checksum` field instead uses the explicit `sha256:<digest>` form.
Before promotion, run:

```bash
just validate-hypothesis-analysis-run \
  kb/hypotheses/<Disease>/<hypothesis_id>/<provider>.md \
  kb/hypotheses/<Disease>/<hypothesis_id>/<provider>_artifacts
```

This rejects a marker-only or failed run even when the provider process exited
zero. It verifies the saved contract, primary outputs, replay assets, and actual
byte identity for every `TABULAR_RESULT`; independently execute the saved
analysis in a clean output directory as well, because the validator deliberately
does not run provider-generated code. The gate accepts the canonical provider
report and sibling artifact directory, not an agent log or hand-written marker
file: it requires provider frontmatter, one `## Output` section, a single success
marker inside that section, and a provider matching the manifest. The report
frontmatter also carries
`artifact_manifest_sha256: sha256:<64 lowercase hex>`, which must match the exact
current `MANIFEST.yaml` bytes; changing the manifest makes the report stale until
the binding is regenerated. The hypothesis runner adds this binding after a new
DRC report is written and before validation. Artifact roles remain provider
declarations—the gate cannot establish that labeled code is scientifically
correct—so code review and independent replay remain necessary.

If review finds a scientific or statistical defect after the provider has
answered, do not silently repair the bundle and re-bind the old success report.
Preserve the provider's claim, record the assessor's exact correction and
before/after code hashes in the manifest, regenerate outputs and replay them,
and classify the provider analysis as at most `PARTIAL` until the provider
successfully reruns or attests the corrected bytes. A clean assessor replay is
valuable verification, but it is not retroactive provider execution. Leave the
stale or missing report-manifest binding failing: that failure is the provenance
signal that prevents an assessor-corrected result from masquerading as the
provider's original result.

`templates/hypothesis_dataset_analysis.md` opts the hypothesis runner into this
contract. A report produced from that template without either exact analysis
status marker is invalid, rather than an ordinary literature report. Existing
failed or invalid outputs do not satisfy `run-missing`; an explicit overwrite
quarantines the prior artifact directory before launching the provider so a new
report cannot pass against stale outputs.

Supply the analysis-specific values through runner flags; the runner supplies
the canonical `<provider>_artifacts/` path and rejects an override to a different
directory:

```bash
uv run python scripts/hypothesis_deep_research.py run \
  biomni <Disease> <hypothesis_id> \
  --template templates/hypothesis_dataset_analysis.md \
  --dataset-inputs 'geo:GSE123; geo:GPL456' \
  --target-variables 'FDX1, DLAT' \
  --analysis-objective 'Prespecified case-versus-control expression contrast'
```

Commit when reviewable and reasonably small:

- a manifest naming external inputs, accessions/versions, retrieval dates, and
  checksums where available;
- analysis code, queries, configuration, random seeds, package/environment
  specifications, and sanitized execution logs;
- small derived tables, network files, figures, and summaries needed to inspect
  the reported result.

Do not commit:

- raw public downloads that can be recovered from a stable accession, a
  provider data lake, or large cache/database snapshots;
- controlled-access, patient-level, or otherwise restricted data;
- credentials, tokens, signed URLs, or logs/configuration containing secrets;
- opaque heavy binaries whose provenance can instead be recorded in a manifest.

All paths in `source_artifacts`, `code_artifacts`, `environment_artifact`, and
`output_artifacts` name non-empty files actually committed beneath the declared
provider `artifact_root`. Code, environment, and output roles are disjoint
within a reproducible analysis. These structured paths are the authoritative
assessment inventory; `MANIFEST.yaml` is the run-level integrity contract but
does not replace them. Reference every committed file that bears on an assessed result
from the corresponding data source or analysis. For an artifact that is
external, local-only, missing, or not produced, record that state and its stable
identifier/checksum in
`data_sources[].notes`, `analyses[].status_reason`, or `analyses[].limitations`;
never put a nonexistent or machine-specific absolute path in an artifact slot.
A local data lake such as `~/.biomni-lake` stays outside the repository.
Biomni execution is disabled by default and requires the explicit opt-in
`DISMECH_ENABLE_BIOMNI=1`. Without that opt-in, repository-supported entry
points also exclude Biomni from automatic provider fallback; dry-run command
inspection remains available. After opt-in, the hypothesis runner passes the
persistent path to Biomni and explicitly enables lake use
(`skip_data_lake=false`) unless the caller overrides it.

Review files selectively before staging. The repository does not blanket-ignore
OpenScientist artifact bundles, because that would also hide manifests, code,
and small derived results that should be reviewed. The same policy applies to
all providers.

Local path validation proves containment, role separation, existence, and
non-emptiness; it cannot prove that an untracked file has been staged. CI sees
only committed files, so the same checks enforce that property after push.

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
        analysis_ids:
          - wilson-liver-de
        report_quote: Exact words copied from the OpenScientist report.
        claim_origin: PROVIDER_ANALYSIS
        rationale: The report derived this claim from the linked executed analysis.
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
`PROVIDER_DISCOVERY`, `PROVIDER_EXTRACTION`, `PROVIDER_ANALYSIS`, `PROVIDER_INFERENCE`,
`SEED_DERIVED`, `PRIOR_PROVIDER_DERIVED`, or `UNKNOWN`.
`PROVIDER_EXTRACTION` means the provider extracted a new claim or detail from a
source that its seed already cited; it is distinct from discovering a new source.
`PROVIDER_ANALYSIS` means the raw report attributes the position to the linked
`analysis_ids`. Because `provider_support` describes provider lineage rather
than endorsing it, this may point to a `REPORTED_ONLY` analysis; the linked
`UNVERIFIABLE` auditability makes clear that execution was not established, and
it must not be treated as independent computational support. `FAILED` and
`SKIPPED` analyses cannot originate a provider position.
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

Apply the same rule to data lineage. Two providers that reuse the same input
table, code, seed-derived result, or prior-provider output have not independently
replicated a finding. Sharing a public accession does not by itself destroy
independence, but the comparison must inspect the cohort subset, method,
parameters, and output. Reconciliation `provider_support[].analysis_ids` resolve
against that provider's selected assessment and anchor what the report
attributes to an analysis. The linked status and auditability state whether
execution was actually established.

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
acyclic lineage rules; resolves data-source and analysis foreign keys; applies
the strict `SUCCEEDED`/reproducibility and reported-only claim rules; and verifies
nonblank raw-report quotes. These checks establish structural and source-traceability
integrity, not biomedical truth; that remains the assessor's documented reasoning
and the project's normal evidence-curation process.
