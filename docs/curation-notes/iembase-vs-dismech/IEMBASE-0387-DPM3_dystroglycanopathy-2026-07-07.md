# IEMbase 0387: DPM3-related GDP-Man:Dol-P mannosyltransferase 3 deficiency (CDG)

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 387 |
| Nosology | 18.4.07.01 |
| Gene | DPM3 |
| External IDs | OMIM:612937; ORPHA:263494 |
| Generated mapping | UNMAPPED; low candidate `Dystroglycanopathy.yaml#DPM3-related dystroglycanopathy` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml#DPM3-related dystroglycanopathy` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive DPM3-CDG, also listed as CDG-Io and
GDP-Man:Dol-P mannosyltransferase 3 deficiency.

Clinical rows include adult dilated cardiomyopathy, gait disturbance, proximal
muscle weakness, pes planus, dysmorphic features, limb-girdle muscular
dystrophy, psychomotor delay, and adult stroke-like episodes. Biochemical rows
include increased creatine kinase, increased transaminase, type I
sialotransferrin findings, decreased dolichol-P-mannose, increased
dolichol-linked Man5GlcNAc2, and normal Factor XI.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Dystroglycanopathy.yaml` explicitly includes a DPM3-related
dystroglycanopathy subtype: DPM3 is described as a stabilizing subunit of
dolichol-phosphate mannose synthase, with mutations causing CDG with secondary
dystroglycanopathy, muscular dystrophy, and dilated cardiomyopathy. The same
file also includes DPM3 in the genetic findings section.

Local DisMech is stronger for shared dystroglycanopathy mechanism,
alpha-dystroglycan O-mannosyl glycosylation, and supportive management. IEMbase
is stronger for CDG-Io biochemical details and the DPM3-specific adult muscle,
cardiac, and stroke-like phenotype rows.

## Concordance and completeness

Judgement: false negative; resolve to
`Dystroglycanopathy.yaml#DPM3-related dystroglycanopathy`.

The resources agree on DPM3 identity, autosomal recessive inheritance,
dolichol-phosphate mannose synthase involvement, secondary
dystroglycanopathy/CDG framing, muscular dystrophy, proximal weakness, elevated
creatine kinase, and dilated cardiomyopathy.

## Curation actions

- Map this record to the DPM3-related dystroglycanopathy branch of
  `Dystroglycanopathy.yaml`.
- Consider adding IEMbase's dolichol-P-mannose, dolichol-linked Man5GlcNAc2,
  type I sialotransferrin, Factor XI, pes planus, gait disturbance, and
  stroke-like episode prompts after source verification.
- If future CDG-specific subtype anchors are added, preserve the connection to
  the dystroglycanopathy mechanism rather than creating duplicate disconnected
  disease entries.
