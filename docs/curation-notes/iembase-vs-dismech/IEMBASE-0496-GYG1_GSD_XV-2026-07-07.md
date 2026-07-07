# IEMbase 0496: GYG1-related muscle glycogenin 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 496 |
| Nosology | 3.4.01.01 |
| Gene | GYG1 |
| External IDs | OMIM:613507; ORPHA:263297 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_XV.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_XV.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive GYG1-related muscle glycogenin 1
deficiency as glycogen storage disease type XV / polyglucosan body myopathy
type 2. No treatments are listed. The only biochemical row in the local JSON is
markedly decreased muscle glycogen across life stages. No clinical rows are
listed in the local JSON.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_XV.yaml` is the correct local target despite the
generated CANDIDATE status. The entry models autosomal recessive GYG1
glycogenin-1 deficiency, failed glycogen synthesis initiation, skeletal-muscle
polyglucosan body myopathy, proteostasis/desmin sequestration, cardiac
polyglucosan involvement, proximal and distal weakness, exercise intolerance,
myalgia, waddling gait, scapular winging, skeletal-muscle atrophy/fatty
replacement on MRI, creatine kinase, depleted normal skeletal-muscle glycogen,
muscle biopsy, GYG1 genetic testing, and supportive management.

## Concordance and completeness

Judgement: correct candidate; accept as covered by
`Glycogen_Storage_Disease_XV.yaml`.

IEMbase and DisMech agree on GYG1/GSD XV identity, recessive inheritance, and
the key muscle-glycogen abnormality. DisMech captures the broader disease
mechanism and clinical spectrum that are sparse in the current IEMbase JSON:
polyglucosan body myopathy, weakness, exertional symptoms, cardiac involvement,
MRI findings, biopsy, and genetics. The IEMbase "decreased muscle glycogen" row
matches the DisMech observation that normal glycogen can be depleted in fibers
containing polyglucosan bodies.

## Curation actions

- Treat this as covered by `Glycogen_Storage_Disease_XV.yaml`.
- Consider promoting future automated matching from candidate to exact for
  GYG1, glycogenin-1 deficiency, GSD XV, and polyglucosan body myopathy type 2.
- If importing IEMbase prompts, verify the decreased-muscle-glycogen wording
  against the existing normal-glycogen depletion evidence.
