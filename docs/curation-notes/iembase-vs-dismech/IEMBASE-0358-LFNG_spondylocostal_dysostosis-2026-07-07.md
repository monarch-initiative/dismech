# IEMbase 0358: LFNG-related spondylocostal dysostosis type 3

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 358 |
| Nosology | 18.2.02.01 |
| Gene | LFNG |
| External IDs | OMIM:609813; ORPHA:2311 |
| Generated mapping | UNMAPPED; low candidate `Spondylocostal_Dysostosis.yaml` |
| Candidate DisMech targets | `Spondylocostal_Dysostosis.yaml#LFNG/SCDO3` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents LFNG-CDG, also listed as spondylocostal dysostosis type 3,
an autosomal recessive O-fucose glycosylation disorder. The source disease
label contains a typo, "LFNG-rerlated", but the gene and alternate name resolve
to LFNG/SCDO3.

Characteristic rows include decreased body height, long slender fingers,
scoliosis, normal sialotransferrins, and vertebral anomalies of the whole
spine. IEMbase lists no additional clinical rows beyond these characteristic
features, and the only biochemical row is sialotransferrins. No treatment rows
are present.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a
Spondylocostal Dysostosis file that explicitly includes LFNG among the
autosomal recessive segmentation-clock genes causing SCDO. Local mechanism
frames LFNG disease as disruption of Notch-pathway somitogenesis, producing
multiple vertebral segmentation defects with rib abnormalities, short trunk,
small thorax, scoliosis, and possible respiratory compromise.

Local coverage is stronger for the axial segmentation and serial somite
malformation mechanism than IEMbase. IEMbase is stronger for the CDG/O-fucose
labeling and the normal-sialotransferrin row.

## Concordance and completeness

Judgement: false negative; resolve to the local spondylocostal dysostosis
LFNG/SCDO3 context.

The resources agree on LFNG identity, autosomal recessive inheritance,
spondylocostal dysostosis type 3, short stature, scoliosis, and widespread
vertebral anomalies. The generated candidate points to the correct file despite
being below the exact-mapping threshold.

## Curation actions

- Map this record to `Spondylocostal_Dysostosis.yaml`, specifically the
  LFNG/SCDO3 segmentation-clock context.
- Preserve the source typo as a source-label issue only; do not propagate it to
  curated disease labels.
- Consider future enrichment with the CDG/O-fucose framing, long slender
  fingers, and normal sialotransferrins after source verification.
