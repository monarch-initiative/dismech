# IEMbase 0221: PDHB-related Pyruvate dehydrogenase E1 beta deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 221 |
| Nosology | 5.1.02.01 |
| Gene | PDHB |
| External IDs | OMIM:179060 |
| Generated mapping | MAPPED; `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-beta deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as PDHB-related pyruvate dehydrogenase E1 beta
deficiency, with alternate label PDH. The record is autosomal recessive and
treatability is marked unknown, though treatment rows list thiamine and
ketogenic diet.

The biochemical rows mirror PDH deficiency generally: increased alanine,
lactate, lactate/pyruvate ratio, pyruvate, and ketones, with normal glucose.
Clinical rows include corpus-callosum agenesis or hypogenesis, developmental
delay, failure to thrive, hypotonia, lactic acidosis, Leigh syndrome,
microcephaly, and pyramidal signs.

## DisMech phenotype coverage

`Pyruvate_Dehydrogenase_Deficiency.yaml` is the correct target, with subtype
resolution to `E1-beta deficiency`. The local entry explicitly covers the rare
autosomal recessive PDHB subtype, reduced PDH complex activity, lactate and
pyruvate accumulation, lactic acidosis, cerebral energy failure,
neurodevelopmental delay, hypotonia, seizures/movement disorders,
corpus-callosum and brain MRI abnormalities, microcephaly, ketogenic diet,
thiamine, biochemical testing, enzyme assay, and molecular testing.

## Concordance and completeness

Judgement: correct mapped target, with subtype resolution needed.

IEMbase and DisMech agree on PDHB/E1-beta identity, autosomal recessive
inheritance, PDH biochemical abnormalities, lactic acidosis, developmental
delay, failure to thrive, hypotonia, Leigh-spectrum disease, microcephaly, and
pyramidal/CNS involvement. IEMbase adds explicit corpus-callosum hypogenesis as
a row, while DisMech is richer for mechanism and diagnostic/treatment context.

## Curation actions

- Keep the record mapped to `Pyruvate_Dehydrogenase_Deficiency.yaml`.
- Prefer subtype resolution to
  `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-beta deficiency`.
- Consider adding or checking corpus-callosum hypogenesis terminology if the
  PDHB subtype is later enriched.
