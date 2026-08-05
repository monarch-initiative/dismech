# IEMbase 0084: TCN1-related haptocorrin deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 84 |
| Nosology | 21.9.04.01 |
| Gene | TCN1 |
| External IDs | OMIM:193090 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Best fuzzy candidate `Pyruvate_Dehydrogenase_Deficiency.yaml#E3-binding protein deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as TCN1-related haptocorrin deficiency, with alternate
labels transcobalamin I deficiency, cobalamin R binder protein deficiency, and
HCD. Inheritance is recorded as autosomal dominant and autosomal recessive.
Treatability is marked unknown.

The characteristic biochemical signal is abnormal vitamin B12/cobalamin in serum
or plasma.

The characteristic clinical row is "no consistent clinical picture."

No treatment rows are present in the cached IEMbase record.

## DisMech phenotype coverage

No valid local DisMech target was found for TCN1 or haptocorrin deficiency.

The local `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml` entry
covers transcobalamin II deficiency (TCN2), LMBRD1/cblF, ABCD4/cblJ, and
intracellular cobalamin complementation groups, but it does not model TCN1 or
haptocorrin deficiency.

The best fuzzy candidate, `Pyruvate_Dehydrogenase_Deficiency.yaml#E3-binding
protein deficiency`, is a false positive. PDH E3-binding protein deficiency is a
PDHX/pyruvate metabolism disorder, not a cobalamin-binding protein phenotype.

## Concordance and completeness

Judgement: local gap, but scope review is needed before prioritizing a full
disease entry.

Unlike TCN2 deficiency, IEMbase itself records no consistent clinical picture
for TCN1 deficiency. This may be better handled as a low-priority cobalamin
transport/biomarker note unless future evidence supports a clear disease
mechanism and phenotype.

## Curation actions

- Keep this IEMbase record unmapped for now.
- Do not map it to TCN2 deficiency or PDH E3-binding protein deficiency.
- If the cobalamin transport area is expanded, decide whether TCN1 belongs as a
  disease entry, subtype, or scoped-out biochemical trait.
