# IEMbase 0218: PC-related Pyruvate carboxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 218 |
| Nosology | 3.2.03.01 |
| Gene | PC |
| External IDs | OMIM:266150 |
| Generated mapping | UNMAPPED; best candidate `Pyruvate_Carboxylase_Deficiency_Disease.yaml` |
| Candidate DisMech targets | `Pyruvate_Carboxylase_Deficiency_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as PC-related pyruvate carboxylase deficiency, with the
alternate label PCD. The record is autosomal recessive and treatability is
marked unknown.

The biochemical rows include increased alanine, citrulline, lysine, ketones,
ammonia, lactate, lactate/pyruvate ratio, and
3-OH-butyrate/acetoacetate ratio, with decreased glucose and decreased
pyruvate carboxylase activity in fibroblasts. Clinical rows include absent
myelination, basal ganglia MRI abnormalities, developmental delay,
hepatomegaly, hypoglycemia, muscular hypotonia, leukodystrophy, liver
dysfunction, fatty liver, renal tubular acidosis, and seizures. No treatment
rows are listed in the cached record.

## DisMech phenotype coverage

`Pyruvate_Carboxylase_Deficiency_Disease.yaml` is the correct target despite
the generated UNMAPPED status. The local entry covers biallelic PC disease,
pyruvate carboxylase activity loss, impaired pyruvate-to-oxaloacetate
conversion, impaired gluconeogenesis, impaired anaplerosis, lactate
accumulation, lactic acidosis, ketonuria, hypoglycemia, secondary urea-cycle
perturbation, hypercitrullinemia, hyperammonemia, neurologic dysfunction,
developmental delay, hypotonia, seizures, delayed myelination, and type A/B/C
subtypes.

## Concordance and completeness

Judgement: generated false negative; resolve to
`Pyruvate_Carboxylase_Deficiency_Disease.yaml`.

IEMbase and DisMech agree on PC disease identity, autosomal recessive
inheritance, the enzyme defect, lactic acidosis/lactate accumulation,
hypoglycemia, ketone abnormalities, citrulline/ammonia abnormalities,
developmental delay, hypotonia, seizures, and myelination/CNS involvement.
IEMbase adds useful granular analytes, especially alanine, lysine,
lactate/pyruvate ratio, 3-OH-butyrate/acetoacetate ratio, fatty liver, and renal
tubular acidosis. DisMech is richer for mechanism, subtype framing, and
triheptanoin/anaplerosis treatment context.

## Curation actions

- Correct the generated UNMAPPED status to
  `Pyruvate_Carboxylase_Deficiency_Disease.yaml`.
- Consider adding IEMbase's renal tubular acidosis, fatty liver, and specific
  amino-acid/redox-ratio biomarker leads if supported by source evidence.
- No new PC disease file is needed.
