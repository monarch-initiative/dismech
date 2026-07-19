# IEMbase 0214: GGT1-related Gamma-glutamyl transpeptidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 214 |
| Nosology | 2.1.03.01 |
| Gene | GGT1 |
| External IDs | OMIM:231950; ORPHA:33573 |
| Generated mapping | UNMAPPED; best candidate `Lipoyl_Transferase_1_Deficiency.yaml` |
| Candidate DisMech targets | No valid local target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as GGT1-related gamma-glutamyl transpeptidase
deficiency, with alternate labels glutathionuria, gamma-glutamyl transferase
deficiency, and GGT1. The record is autosomal recessive and treatability is
marked unknown.

The biochemical signal is distinctive for a gamma-glutamyl-cycle/leukotriene
handling defect: decreased gamma-glutamyltranspeptidase activity in fibroblasts
and white blood cells, decreased LTD4 synthesis in nucleated white blood cells,
normal LTB4, increased LTC4, decreased LTD4 and LTE4, and increased plasma and
urinary glutathione with normal RBC glutathione. Clinical rows are sparse and
include intellectual disability, psychotic behavior, and tremor. No treatment
rows are listed in the cached record.

## DisMech phenotype coverage

No dedicated GGT1 or gamma-glutamyl transpeptidase deficiency disorder was found
in `kb/disorders`. The generated candidate
`Lipoyl_Transferase_1_Deficiency.yaml` is not a valid target: it covers LIPT1
mitochondrial protein lipoylation defects with combined alpha-ketoacid
dehydrogenase deficiency and lactic acidosis, not GGT1-mediated
gamma-glutamyl-cycle or leukotriene metabolism. `5-Oxoprolinase_Deficiency.yaml`
mentions the gamma-glutamyl cycle, but it is OPLAH-specific and does not cover
GGT1 deficiency.

## Concordance and completeness

Judgement: true local gap.

IEMbase has a clear disease identity and biomarker profile for GGT1 deficiency.
The available local files contain only pathway-neighbor or lexical-neighbor
content. The LIPT1 candidate should be rejected because the gene, molecular
lesion, biochemical markers, and clinical mechanism are all different.

## Curation actions

- Add GGT1-related gamma-glutamyl transpeptidase deficiency as a future local
  disease if this class is prioritized.
- Reject `Lipoyl_Transferase_1_Deficiency.yaml` as a false candidate.
- Use IEMbase as a lead for GGT enzyme activity, glutathione compartment, and
  leukotriene-profile rows when the disease is curated.
