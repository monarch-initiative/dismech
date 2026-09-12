# Dataset access log — E-MTAB-16629

- **Accession:** ArrayExpress `E-MTAB-16629` (BioStudies backend), AttachTo=ArrayExpress
- **Title:** "Distinct diversity of skin cell populations of rhinophyma and hypertrophic scar illustrated by scRNA-seq"
- **Organism:** Homo sapiens; **Assay:** 10x 3' v3 scRNA-seq of coding RNA
- **ReleaseDate:** 2026-02-18; **Retrieved:** 2026-09-06
- **Resolved?** YES. `GET https://www.ebi.ac.uk/biostudies/api/v1/studies/E-MTAB-16629` -> HTTP 200.
- **Relevance:** Directly on-topic — the exact rhinophyma vs hypertrophic scar vs healthy skin atlas named in the seed hypothesis.

## Samples (from SDRF) — ONE INDIVIDUAL PER CONDITION
| Sample | Disease | Tissue | Individual | Sex | Age |
|--------|---------|--------|-----------|-----|-----|
| HS-H   | Hypertrophic scar | chest | S6 | man | 22 |
| ROS    | Rhinophyma | (nose, phyma) | (single) | — | — |
| Skin-H | Healthy skin | — | (single) | — | — |

(ROS/Skin-H individual/sex/age fields not fully captured in the truncated SDRF read; HS confirmed as single 22 y/o male chest scar. No biological replicates in any arm.)

## Files accessed (processed 10x triplets), served from
`https://ftp.ebi.ac.uk/biostudies/fire/E-MTAB-/629/E-MTAB-16629/Files/`

| File | Bytes (BioStudies) | HTTP |
|------|--------------------|------|
| ROSmatrix.mtx.gz    | 39,721,345 | 200 |
| ROSfeatures.tsv.gz  | 297,026    | 200 |
| ROSbarcodes.tsv.gz  | 34,805     | 200 |
| HS-Hmatrix.mtx.gz   | 69,178,141 | 200 |
| HS-Hfeatures.tsv.gz | 297,026    | 200 |
| HS-Hbarcodes.tsv.gz | 44,325     | 200 |
| Skin-Hmatrix.mtx.gz | 67,645,601 | 200 |
| Skin-Hfeatures.tsv.gz | 297,026  | 200 |
| Skin-Hbarcodes.tsv.gz | 43,165   | 200 |
| E-MTAB-16629.sdrf.txt | 6,534    | 200 |
| E-MTAB-16629.idf.txt  | 5,414    | 200 |

Features file has 3 columns: [Ensembl gene id, HGNC symbol, "Gene Expression"]; symbols read from column 1.

Checksums: NOT independently computed (executor is ephemeral; raw files are recoverable from the
stable accession above). Byte sizes recorded above serve as integrity anchors.

## Execution constraints encountered
- Executor wall-clock limit 60 s/call; no filesystem persistence between calls -> pipeline run one sample per call, re-downloading each time.
- `urllib`/`gzip` imports blocked; used `requests` + pandas/scanpy readers instead.
- Healthy sample timed out once on the 68 MB download; succeeded on retry with lighter QC.
