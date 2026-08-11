# IEMbase 0585: PHEX-related X-linked hypophosphatemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 585 |
| Nosology | 25.1.06.01 |
| Gene | PHEX |
| External IDs | OMIM:307800; ORPHA:89936 |
| Generated mapping | MAPPED; `X-Linked_Hypophosphatemia.yaml` |
| Candidate DisMech targets | `X-Linked_Hypophosphatemia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PHEX-related X-linked hypophosphatemia, with alternate labels
familial hypophosphatemic rickets, vitamin D-resistant rickets, and XLH. The
record is classified as unclassified nosology, lists X-linked dominant
inheritance, has unknown treatability, and has no treatment rows.

Biochemical rows include increased alkaline phosphatase, decreased plasma
phosphate, normal plasma calcium, and normal-to-increased urinary phosphate.
Clinical rows include dental anomalies, muscle weakness, tinnitus, and waddling
gait.

## DisMech phenotype coverage

`X-Linked_Hypophosphatemia.yaml` is the correct local target. It models PHEX
loss of function, excess FGF23, renal phosphate wasting, chronic
hypophosphatemia, rickets/osteomalacia, short stature, dental abscesses or
dental disease, hearing impairment, burosumab therapy, and conventional
phosphate plus active vitamin D therapy.

## Concordance and completeness

Judgement: correct exact mapping.

IEMbase and DisMech agree on PHEX, X-linked dominant inheritance, XLH identity,
renal phosphate wasting, hypophosphatemia, rickets framing, and dental
involvement. DisMech is stronger for the PHEX-FGF23 mechanism and treatment
coverage.

IEMbase adds useful import prompts for alkaline phosphatase, normal calcium,
urinary phosphate, tinnitus, muscle weakness, and waddling gait. The lack of
treatments in IEMbase contrasts with DisMech's explicit burosumab and
conventional phosphate/vitamin D coverage.

## Curation actions

- Keep `X-Linked_Hypophosphatemia.yaml` as the exact DisMech target.
- Review alkaline phosphatase, calcium, urinary phosphate, tinnitus, muscle
  weakness, and waddling-gait prompts for possible phenotype enrichment.
- Do not downgrade existing DisMech treatment coverage based on IEMbase's empty
  treatment rows.
