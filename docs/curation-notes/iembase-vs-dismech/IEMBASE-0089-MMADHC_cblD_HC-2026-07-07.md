# IEMbase 0089: MMADHC-related homocystinuria, cblDv1 type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 89 |
| Nosology | 21.9.11.02 |
| Gene | MMADHC |
| External IDs | OMIM:277410 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Manual target `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MMADHC-related homocystinuria,
cblD variant 1 type, with alternate labels cblD-HC and homocystinuria cblD
type variant 1. Treatability is marked yes.

The characteristic clinical rows are megaloblastic anemia and neurological
symptoms.

The biochemical panel is remethylation-predominant: homocysteine in urine,
total plasma homocysteine, low-to-normal plasma methionine, and reduced
S-adenosylmethionine in CSF or plasma. Methylmalonic acid in plasma and urine
is present but recorded as normal across age strata for this cblD-HC record.

Treatment rows include betaine and hydroxycobalamin.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. The best local target is
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD`.

DisMech already has a cblD subtype for MMADHC deficiency and explicitly states
that MMADHC defects can produce isolated methylmalonic acidemia, isolated
homocystinuria, or combined disease. The pathophysiology section includes
MMADHC in impaired intracellular cobalamin cofactor synthesis and cites
cblD-homocystinuria among the intracellular cobalamin processing defects. The
remethylation branch captures impaired methionine synthase activity,
homocysteine accumulation, methionine depletion, megaloblastic anemia, and
hydroxocobalamin/betaine treatment logic.

## Concordance and completeness

Judgement: false-negative mapping with high local umbrella-level coverage.

The main gap is subtype granularity. DisMech currently has one cblD subtype
rather than separate cblD-HC/cblDv1, cblD-MMA/cblDv2, and combined cblD forms.
That loses the IEMbase distinction between remethylation-predominant disease
and isolated MMA disease.

## Curation actions

- Update the mapping logic or manual crosswalk to resolve this record to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblD`.
- Consider splitting cblD into cblD-HC, cblD-MMA, and combined forms if subtype
  granularity becomes important.
- Preserve the remethylation-specific cblD-HC signal: high homocysteine,
  low-to-normal methionine, megaloblastic anemia, and betaine plus
  hydroxycobalamin therapy.
