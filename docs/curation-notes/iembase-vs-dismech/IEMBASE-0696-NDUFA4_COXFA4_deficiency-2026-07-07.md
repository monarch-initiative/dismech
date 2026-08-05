# IEMbase 0696: NDUFA4-related cytochrome c oxidase subunit NDUFA4 (COXFA4) deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 696 |
| Nosology | 7.4.18.01 |
| Nosology code | IEM1149 |
| Gene | NDUFA4, current HGNC symbol COXFA4 |
| External IDs | OMIM:619065; ORPHA:255241 |
| Generated mapping | MAPPED to `COXFA4-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Exact COXFA4/NDUFA4 target; broad Leigh context is secondary |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA4-related cytochrome c oxidase
subunit deficiency. This is the complex IV disease now curated under the
HGNC-approved symbol COXFA4; the historical NDUFA4 name reflects the older
misassignment of the protein to complex I.

The biochemical rows include increased plasma alanine, increased CSF lactate,
and increased plasma lactate. Clinical rows include brainstem MRI lesions,
developmental delay, failure to thrive, hypertension, regression, peripheral
neuropathy, nystagmus, optic atrophy, renal tubular acidosis, respiratory
failure, and characteristic dystonia.

## DisMech phenotype coverage

`COXFA4-Related_COX_Deficiency.yaml` is the correct local target. It explicitly
models COXFA4/NDUFA4 as a complex IV structural subunit, explains the historical
complex I naming problem, records OMIM:619065/MONDO:0033656, and covers failed
complex IV assembly, impaired terminal electron transfer, lactic acidosis, and
a Leigh-syndrome neurologic phenotype with leukoencephalopathy/brainstem
involvement.

Coverage is high for identity and mechanism, but not complete for every
IEMbase phenotype row. The local entry is leaner for plasma alanine, CSF lactate
as a separate row, failure to thrive, hypertension, regression, peripheral
neuropathy, nystagmus, optic atrophy, renal tubular acidosis, respiratory
failure, and dystonia.

## Concordance and completeness

Judgement: mapped with high identity/mechanism concordance and phenotype-detail
gaps.

This is the key exception in the batch: although the record is named NDUFA4 in
IEMbase, it belongs with the complex IV COXFA4 entry rather than the complex I
NDUFA/NDUFB gap set. DisMech is stronger on the corrected mechanism and gene
symbol; IEMbase adds granular clinical rows that should be reviewed if the
COXFA4 entry is expanded.

## Curation actions

- Keep `COXFA4-Related_COX_Deficiency.yaml` as the canonical target.
- Preserve the NDUFA4 synonym because IEMbase, OMIM, and older literature use it.
- Consider adding IEMbase-specific phenotype detail for alanine, CSF lactate,
  failure to thrive, regression, peripheral neuropathy, nystagmus, optic
  atrophy, renal tubular acidosis, respiratory failure, dystonia, and
  hypertension if supported by evidence.
- Do not treat COXFA4/NDUFA4 as a complex I subunit disease.
