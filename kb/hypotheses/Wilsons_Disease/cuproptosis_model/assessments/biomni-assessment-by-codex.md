# Codex assessment of the Biomni report

## Verdict

**Weakly supported and unresolved.** Biomni produced a useful, directly
executed comparison of the two GEO studies, and the corrected output is fully
inspectable and byte-reproducible. That is strong evidence about what these
microarray contrasts show. It is not direct evidence that cuproptosis occurs in
Wilson disease, and it is not a fully provider-attested result.

## Why the analysis is `PARTIAL` / `REPRODUCIBLE`

Biomni downloaded the two series matrices and two official platform annotations,
derived sample groups from deposited metadata, ran the primary analysis, and
created an offline replay. The run used the specified GEO inputs directly and
the manifest records `fallback_used: false`; it did not replace failed tools or
data access with literature synthesis or another provider's results.

The initial bundle nevertheless had a material q-value defect. Probe-level BH
correction was correctly performed across each full platform, but the
gene-table builder then applied a second BH correction over the selected gene
rows and overwrote those values. That violated the stated full-platform
multiplicity contract. Codex removed only this second correction and reran both
the primary analysis and a clean offline replay. The corrected key tables are
byte-identical between runs:

| Artifact | Corrected SHA-256 |
| --- | --- |
| `sample_manifest.tsv` | `99be400a6298c8be66ad19fc9d3eba76dd1906df1c1289c38eb140d4ca2475ac` |
| `probe_level_results.tsv` | `2ed88b772ba5dd5f11165aa9256151ad8b72cdd013d1cbfad71ec32f055be4bf` |
| `gene_level_results.tsv` | `b9c9e28a14890e247f9c46ec2f26f76af40dc1ba45bf3717f508d77458ea5331` |

Two read-only Biomni attempts to attest this corrected bundle failed closed:
the first used incorrect saved-schema assumptions, and the second execution
wrapper returned no result. The canonical report therefore still shows the pre-correction q-values.
The structured assessment deliberately grades the analysis `PARTIAL`, because
the provider did not attest the corrected output, and `REPRODUCIBLE`, because
the corrected code, input identities, environment, outputs, and clean replay
are committed. Do not cite q-values from `biomni.md`; use the corrected tables.

## Corrected comparison results

The values below are from the corrected `gene_level_results.tsv`. They use the
prespecified probe with the highest global mean before viewing group labels;
Welch tests are per probe and q-values retain the BH correction across the full
platform.

| Dataset | Gene | Case-control log2 difference | Welch p | Full-platform BH q | Comparison consequence |
| --- | --- | ---: | ---: | ---: | --- |
| GSE197406 | FDX1 | -0.6315 | 0.002701 | 0.0569 | Lower direction agrees with OpenScientist, but adjusted significance does not. |
| GSE125637 | Fdx1 | -0.1855 | 0.04257 | 0.1793 | Lower direction agrees; only nominal significance. |
| GSE197406 | DLAT | +0.5144 | 0.03081 | 0.2173 | Positive, contradicting OpenScientist's reported decrease. |
| GSE197406 | DLD | -0.0549 | 0.6369 | 0.8622 | Small negative estimate, not OpenScientist's reported increase. |
| GSE125637 | Gls | -0.1713 | 0.3557 | 0.5406 | Does not reproduce OpenScientist's reported p=0.006. |
| GSE125637 | Dlst | +0.5607 | 2.449e-05 | 0.00601 | Positive and adjusted-significant, contradicting the reported decrease. |

The corrected q-values matter most for FDX1: neither the human nor mouse
representative probe passes a 0.05 full-platform FDR threshold. The shared lower
direction is still a legitimate descriptive comparison, but it does not support
a temporal stage claim.

## Dataset and platform audit

The committed bundle pins all four external inputs by URL, retrieval time, byte
count, and SHA-256. Raw GEO files remain in the local Biomni lake, while the
repository retains the manifest, input and sample tables, code, environment,
derived tables, logs, and replay outputs.

The provider-generated downloader still hardcodes the original local lake path;
the stable URLs and checksums are therefore the portable recovery contract.
The analysis itself accepts explicit input and output directories.

- GSE197406 is a GPL570 Affymetrix human liver microarray with seven Wilson
  transplant/cirrhotic samples and eight histologically normal resection
  controls. Cases were substantially younger (median 30 years versus 57), so
  age and clinical sampling context are confounded with disease status.
- GSE125637 is a GPL1261 Affymetrix mouse liver microarray with four wild-type,
  four untreated Atp7b-null, and four zinc-treated Atp7b-null samples. The zinc
  arm was identified from metadata and excluded from the four-versus-four
  contrast.

This directly corrects OpenScientist's description of GSE125637 as mouse
RNA-seq. The platform conclusion comes from the committed input and analysis
artifacts; the canonical Biomni prose report does not state it explicitly.

## Interpretation boundary

Both datasets are small, cross-sectional, and differ in species, platform,
clinical context, and sampling. Expression shifts in genes associated with the
cuproptosis literature do not measure copper binding to lipoylated proteins,
lipoylated-protein aggregation, iron-sulfur-protein loss, proteotoxic stress,
cell death, or pathway-specific rescue. They cannot establish causality or a
temporal progression from an early cuproptosis-high state to late cirrhosis.

The useful conclusion is narrow: the corrected Biomni bundle resolves several
reported expression and platform conflicts under one documented rule, while
leaving the Wilson-disease cuproptosis mechanism weakly supported and
unresolved.

The authoritative structured dispositions and provenance are in
`biomni-assessment-by-codex.yaml`.
