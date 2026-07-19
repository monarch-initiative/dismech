# IEMbase 0270: ACAT2-related cytosolic acetoacetyl-CoA thiolase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 270 |
| Nosology | 4.3.9.01 |
| Gene | ACAT2 |
| External IDs | OMIM:100678 |
| Generated mapping | UNMAPPED; weak candidate `Beta-Ketothiolase_Deficiency.yaml` |
| Candidate DisMech targets | No valid current target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ACAT2-related acetoacetyl-CoA thiolase deficiency
with the alternate abbreviation CT deficiency. The inheritance field is
unknown, treatability is marked unknown, and the cached JSON has no treatment
rows.

The phenotype signal is very sparse. The only clinical row is developmental
delay. The only biochemical row is urinary ketones marked normal to increased
in infancy and childhood.

## DisMech phenotype coverage

The generated weak candidate, `Beta-Ketothiolase_Deficiency.yaml`, should be
rejected for this record. The local beta-ketothiolase entry is ACAT1
mitochondrial T2 deficiency, with a well-defined autosomal recessive
ketoacidotic crisis phenotype and isoleucine-derived organic-acid signature.
It is not equivalent to a sparse ACAT2/cytosolic thiolase record.

No local ACAT2-specific disease or subtype was found.

## Concordance and completeness

Judgement: no valid local mapping.

The lexical overlap with beta-ketothiolase deficiency is not enough to map this
record. IEMbase's ACAT2 record is too sparse and mechanistically distinct from
ACAT1/T2 deficiency. If this remains in scope for DisMech, it needs a separate
scope review and primary-literature curation rather than reuse of the ACAT1
entry.

## Curation actions

- Keep this IEMbase record unmapped.
- Reject `Beta-Ketothiolase_Deficiency.yaml` as a false-positive weak
  candidate.
- If curated later, anchor the entry explicitly to ACAT2/cytosolic thiolase and
  reassess whether the IEMbase disease assertion is clinically well supported.
