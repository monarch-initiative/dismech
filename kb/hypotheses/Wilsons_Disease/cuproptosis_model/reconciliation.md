# Wilson disease cuproptosis reconciliation

## Outcome

**Weakly supported and unresolved.** The two reports share a lower FDX1/Fdx1
direction in the deposited human and mouse contrasts, but the corrected
full-platform analysis does not establish adjusted significance for either
representative probe. The expression results do not demonstrate cuproptosis or
a temporal disease-stage model.

## Result comparison

The corrected values below come from the Codex-audited, byte-replayed Biomni
artifact bundle. They are **not Biomni-attested q-values**: `biomni.md` predates
the correction and retains the superseded selected-gene BH values.

| Contrast | OpenScientist report | Corrected audit result | Reconciliation |
| --- | --- | --- | --- |
| Human FDX1 | Down, nominal p=0.032 | log2 difference -0.6315; Welch p=0.002701; full-platform BH q=0.0569 | Direction agrees; adjusted significance is unresolved. |
| Mouse Fdx1 | Down, p=0.039 | log2 difference -0.1855; Welch p=0.04257; full-platform BH q=0.1793 | Direction agrees; only nominal evidence. |
| Human DLAT | Down/trending down | log2 difference +0.5144; BH q=0.2173 | OpenScientist direction contradicted; no adjusted-significant change. |
| Human DLD | Up, p=0.017 | log2 difference -0.0549; BH q=0.8622 | OpenScientist increase not reproduced; no differential signal. |
| Mouse Gls | Down, p=0.006 | log2 difference -0.1713; Welch p=0.3557; BH q=0.5406 | Negative direction overlaps, but the reported signal is not reproduced. |
| Mouse Dlst | Down, p=0.008 | log2 difference +0.5607; Welch p=2.449e-05; BH q=0.00601 | Direction and interpretation contradicted. |

GSE125637 is a GPL1261 Affymetrix Mouse Genome 430 2.0 microarray, not
RNA-seq. Biomni's raw report is silent on that platform fact; it comes from the
accessed GEO metadata and committed audit artifacts.

## Provenance boundary

- The corrected Biomni bundle has pinned inputs, code, environment, outputs,
  and byte-identical replay tables, but its provider did not attest the narrow
  q-value correction. Its analysis is therefore `PARTIAL / REPRODUCIBLE`.
- OpenScientist's two calculations are `REPORTED_ONLY / UNVERIFIABLE`: no
  committed inputs, code, environment, probe rule, outputs, or replay establish
  execution.
- Both reports address the same two public accessions. Shared accessions do not
  constitute independent computational convergence, particularly when only one
  execution is auditable.
- The human series confounds disease status with age and
  transplant-versus-resection sampling, further limiting causal interpretation.
- These small cross-sectional microarrays measure expression, not copper binding
  to lipoylated proteins, aggregation, iron-sulfur-protein loss, cell death, or
  pathway-specific rescue. They cannot prove cuproptosis, causality, or temporal
  stages.
