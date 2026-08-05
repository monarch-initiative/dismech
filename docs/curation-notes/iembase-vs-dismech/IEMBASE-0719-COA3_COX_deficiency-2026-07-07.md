# IEMbase 0719: COA3-related cytochrome c oxidase assembly factor 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 719 |
| Nosology | 7.4.17.01 |
| Nosology code | IEM1146 |
| Gene | COA3 |
| External IDs | OMIM:619058; ORPHA:254905 |
| Generated mapping | UNMAPPED; weak candidate `COA3-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | `COA3-Related_COX_Deficiency.yaml` is exact local coverage |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive COA3-related cytochrome c oxidase
assembly factor 3 deficiency. The cached rows include exercise intolerance,
neuropathy, obesity, developmental delay, and short stature, with the
exercise-intolerance, neuropathy, and obesity signal concentrated in adolescent
and adult windows.

## DisMech phenotype coverage

DisMech has exact local coverage in `COA3-Related_COX_Deficiency.yaml`. The
entry resolves to mitochondrial complex IV deficiency nuclear type 14
(MONDO:0033649) and describes biallelic COA3/CCDC56 loss as an inner-membrane
complex IV assembly-factor defect that destabilizes COX1 and stalls early COX
assembly.

The local phenotype coverage is strong for peripheral neuropathy, exercise
intolerance, obesity, and short stature. It also captures the unusually mild,
adult-compatible clinical course and the COA3-COX14 interdependence that are
not expressed in the compact IEMbase row set.

## Concordance and completeness

Judgement: false negative from the generated mapper. The correct target is
`COA3-Related_COX_Deficiency.yaml`.

Identity, inheritance, gene, complex, assembly mechanism, and core phenotype
signal all align. IEMbase adds a developmental-delay row that is not prominent
in the local COA3 file, while DisMech is richer for the COX1-coupling assembly
mechanism and the mild adult-compatible presentation.

## Curation actions

- Resolve IEMbase 719 to `COA3-Related_COX_Deficiency.yaml`.
- Treat the generated UNMAPPED status as stale or overly strict.
- Consider whether the IEMbase developmental-delay row should prompt review of
  local phenotype breadth.
- Preserve local mechanistic detail on COA3/COX14 interdependence and COX1
  assembly coupling.
