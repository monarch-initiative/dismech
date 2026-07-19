# IEMbase 0605: ALG13-related UDP-N-acetylglucosamine transferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 605 |
| Nosology | 18.1.04.01 |
| Gene | ALG13 |
| External IDs | OMIM:300884; ORPHA:324422 |
| Generated mapping | UNMAPPED; best candidate `Undetermined_Early_Onset_Epileptic_Encephalopathy.yaml#DEE13` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ALG13-related UDP-N-acetylglucosamine transferase catalytic
subunit deficiency, labelled ALG13-CDG, early infantile epileptic
encephalopathy-36, and CDG-Is. The record is X-linked recessive, classified
under disorders of N-glycosylation, has unknown treatability, and has no
treatment rows.

Biochemical rows include normal-to-increased asialotransferrin and
disialotransferrin, decreased-to-normal tetrasialotransferrin, normal
dolichol-linked GlcNAc1, and normal-to-increased thromboplastin time. Clinical
rows include refractory epilepsy, intellectual disability, developmental
regression, extrapyramidal and pyramidal signs, delayed visual maturation,
feeding difficulties, microcephaly, hepatomegaly, broad coarse face,
hypertelorism, low-set ears, retromicrognathia, and dysmorphic features.

## DisMech phenotype coverage

`Undetermined_Early_Onset_Epileptic_Encephalopathy.yaml#DEE13` is a weak
false-positive generated candidate. It provides an epileptic-encephalopathy
neighborhood but does not represent ALG13, X-linked CDG-Is,
UDP-N-acetylglucosamine transferase deficiency, transferrin abnormalities, or
the ALG13-specific dysmorphic and hepatic phenotype.

Local UGDH/UGP2 developmental and epileptic encephalopathy entries are also
mechanistic neighbors only. No exact ALG13-CDG / EIEE36 target was identified.

## Concordance and completeness

Judgement: true local gap; reject the generic DEE candidate.

The generated candidate is driven by refractory early epilepsy, but IEMbase
anchors a specific N-glycosylation disorder. Disease identity, gene, inheritance,
pathway, and biochemical readouts do not match local DEE coverage.

## Curation actions

- Create or identify an exact ALG13-CDG / EIEE36 / CDG-Is target before import.
- Reject `Undetermined_Early_Onset_Epileptic_Encephalopathy.yaml#DEE13` as an
  exact mapping.
- Preserve transferrin isoform pattern, dolichol-linked GlcNAc1, thromboplastin
  time, refractory epilepsy, developmental regression, extrapyramidal/pyramidal
  signs, delayed visual maturation, feeding difficulty, microcephaly,
  hepatomegaly, and facial-dysmorphism prompts.
