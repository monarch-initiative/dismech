# IEMbase 0746: CYCS-related mitochondrial cytochrome c deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 746 |
| Nosology | 8.3.03.01 |
| Nosology code | IEM0489 |
| Gene | CYCS |
| External IDs | OMIM:612004; ORPHA:168629 |
| Generated mapping | UNMAPPED; weak candidate `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` |
| Candidate DisMech targets | `CYCS-Related_Thrombocytopenia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this record CYCS-related mitochondrial cytochrome c deficiency,
with alternate name thrombocytopenia type 4. It is autosomal dominant. The
cached rows are highly specific and hematologic: decreased blood thrombocytes
from childhood through adulthood and characteristic thrombocytopenia across
the same age bands.

## DisMech phenotype coverage

`CYCS-Related_Thrombocytopenia.yaml` is the exact local target despite the
generated mapper miss. The DisMech entry deliberately models the OMIM:612004 /
ORPHA:168629 disease identity as CYCS-related thrombocytopenia 4 rather than as
a generic cytochrome c oxidase deficiency. It captures autosomal dominant CYCS
missense variants, altered cytochrome c respiratory and apoptotic function,
dysregulated megakaryocyte platelet release, and isolated mild-to-moderate
thrombocytopenia with normal platelet size.

The generated `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` candidate is
a false positive with no disease-identity relationship to CYCS thrombocytopenia.

## Concordance and completeness

Judgement: false negative; resolve to exact
`CYCS-Related_Thrombocytopenia.yaml`.

IEMbase is concise but concordant for the dominant clinical phenotype: low
platelets/thrombocytopenia. DisMech is more complete mechanistically and
nosologically, especially in clarifying that CYCS is mitochondrial but the
curated disease entity is thrombocytopenia 4 rather than a syndromic COX
assembly disorder.

## Curation actions

- Treat `CYCS-Related_Thrombocytopenia.yaml` as the exact local mapping.
- Reject `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` as exact
  coverage.
- Preserve the IEMbase label caveat: primary label says mitochondrial
  cytochrome c deficiency, while the disease identity is thrombocytopenia type
  4 / CYCS-related thrombocytopenia.
