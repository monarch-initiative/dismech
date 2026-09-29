# Citations for Research Query

**Query:** # Finalize the completed Wilson-disease GEO analysis bundle

Work only in this existing Biomni artifact directory:

`/Users/cjm/.biomni-lake/runs/wilson-cuproptosis-unseeded-20260829/artifacts`

This is a contract-only finalization of an already completed and replayed
analysis. Do not search for or use another provider's report. Do not change the
scientific contrast, probe selection, tests, or numerical results. Do not
download anything and do not substitute prose or model knowledge for execution.

Inspect `MANIFEST.yaml` and make only these integrity fixes:

1. Add every required existing executable/environment artifact to `outputs`:
   `analysis.py` and `download_inputs.py` with role `CODE`, and
   `environment.txt` with role `ENVIRONMENT`. Record their current positive byte
   counts and exact 64-character lowercase SHA-256 digests.
2. Keep the existing `TABULAR_RESULT` outputs and their current hashes. Ensure
   every declared output exists and matches its recorded size and digest.
3. Keep `fallback_used: false`, `direct_analysis_completed: true`,
   `status: SUCCEEDED`, `replay.verified: true`, and the existing
   `replay.byte_identity` mapping. Remove or update any older replay detail whose
   checksums no longer match the current files.
4. Write `MANIFEST.yaml` last. Do not declare `raw/`, `replay/`, backup files, or
   local absolute paths as outputs.
5. From `/Users/cjm/worktrees/biomni`, create a temporary candidate report
   containing one success-marker line and run:

   `just validate-hypothesis-analysis-run <candidate-report> /Users/cjm/.biomni-lake/runs/wilson-cuproptosis-unseeded-20260829/artifacts`

   The repository gate, not a substitute manual audit, must pass. Remove the
   temporary candidate report afterward.

If the gate fails, fix only contract/provenance defects and rerun it. If any
artifact no longer verifies, set the manifest status to FAILED and report the
failure; do not fall back.

When the gate passes, finish with a `<solution>` block and do not issue another
tool call. The first content line inside that block must be the success-marker
text `ANALYSIS_STATUS: SUCCEEDED` with no Markdown formatting. Include that
marker exactly once in your response. Then give a concise table of the
pre-specified target-gene results from `analysis_summary.md`, the three replay
hashes, and the limitation that cross-sectional expression does not establish
cuproptosis, causality, or temporal stages.
**Provider:** biomni
**Generated:** 2026-08-29T15:32:22.968586

1. GEO:GSE125637
2. GEO:GSE197406
