# IEMbase 0211: DMGDH-related Dimethylglycine dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 211 |
| Nosology | 2.3.01.01 |
| Gene | DMGDH |
| External IDs | OMIM:605849; ORPHA:243343 |
| Generated mapping | MAPPED; `Dimethylglycine_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `Dimethylglycine_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as DMGDH-related dimethylglycine dehydrogenase
deficiency, with alternate labels dimethylglycinuria and DMGLY. The record is
autosomal recessive, marked as a benign form, and treatability is listed as
unknown.

The biochemical rows are increased dimethylglycine in plasma and urine. The
clinical signal is sparse: fish odor in urine is the only characteristic
clinical row, and a separate row states no clinical significance. No treatment
rows are listed in the cached record.

## DisMech phenotype coverage

`Dimethylglycine_Dehydrogenase_Deficiency.yaml` is the correct target. The local
entry covers autosomal recessive DMGDH disease, mitochondrial DMGDH molecular
function deficiency, FAD/tetrahydrofolate-dependent oxidative demethylation of
dimethylglycine to sarcosine, dimethylglycine accumulation in serum and urine,
fish odor, the reported muscle-fatigue/creatine-kinase branch, molecular
testing, and supportive monitoring.

## Concordance and completeness

Judgement: correct mapped target with high concordance.

IEMbase and DisMech agree on the DMGDH disease identity, recessive inheritance,
dimethylglycine accumulation, and fish-odor presentation. DisMech is richer for
the H109R functional mechanism, mitochondrial electron-transfer context, muscle
fatigue, and elevated creatine kinase. IEMbase is more conservative about
clinical significance and does not carry the muscle/CK branch.

One cross-reference caveat should be preserved for later cleanup: the IEMbase
source row records OMIM:605849, while the local mapping justification cites
OMIM:605850. The ORPHA and MONDO identity still support the disease mapping.

## Curation actions

- Keep this record mapped to `Dimethylglycine_Dehydrogenase_Deficiency.yaml`.
- Consider reviewing the DMGDH OMIM cross-reference discrepancy in the mapping
  metadata, but do not change source values in this comparison note.
- No phenotype-enrichment action is required from IEMbase beyond the already
  represented dimethylglycine and fish-odor features.
