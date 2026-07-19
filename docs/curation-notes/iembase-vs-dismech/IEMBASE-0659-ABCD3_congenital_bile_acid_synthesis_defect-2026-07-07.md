# IEMbase 0659: ABCD3-related congenital bile acid synthesis defect

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 659 |
| Nosology | 14.8.08.01 |
| Nosology code | IEM1187 |
| Gene | ABCD3 |
| External IDs | OMIM:616278 |
| Generated mapping | MAPPED to `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` |
| Candidate DisMech targets | Broad bile-acid umbrella only; no exact ABCD3 subtype found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive ABCD3-related congenital bile acid
synthesis defect, also labeled peroxisomal membrane transporter 70-kD defect
or PMP70.

Biochemical rows include increased plasma THCA, increased plasma C27 bile acid,
increased ASAT/ALAT and transaminase, low serum iron, and normal serum
pristanic acid, phytanic acid, and very-long-chain fatty acids. Clinical rows
include optional neonatal/infantile jaundice, infantile/childhood liver failure,
liver fibrosis, anemia, and hepatosplenomegaly.

## DisMech phenotype coverage

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` is a valid broad family context
for congenital bile acid synthesis defects. It covers hepatocyte bile-acid
synthetic enzyme defects, accumulation of hepatotoxic C27 bile-acid
intermediates, cholestasis, progressive liver injury, fat-soluble vitamin
malabsorption, steatorrhea, failure to thrive, and bile-acid replacement
treatment. It explicitly describes C27 bile-acid intermediate toxicity.

However, the local file does not list ABCD3/PMP70 as a subtype or gene. It is
centered on HSD3B7, AKR1D1, CYP7B1, AMACR, CYP27A1, BAAT, and related canonical
bile-acid synthesis/conjugation defects. `Peroxisome_Biogenesis_Disorder.yaml`
also provides broad peroxisomal hepatotoxic metabolite context, but it is not an
ABCD3 disease target.

## Concordance and completeness

Judgement: broad family-level coverage only; exact ABCD3/PMP70 coverage remains
a local gap.

The generated mapped target is useful but overstates completeness if treated as
exact. IEMbase's ABCD3 row has a specific peroxisomal transporter mechanism and
a diagnostic pattern of elevated THCA/C27 bile acids with normal phytanic,
pristanic, and very-long-chain fatty acids that is not captured as a subtype in
the DisMech bile-acid umbrella.

## Curation actions

- Keep `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` as broad context, not exact
  ABCD3 subtype coverage.
- Consider adding an ABCD3/PMP70 subtype or separate disease entry after source
  review.
- Preserve THCA, C27 bile acid, transaminases, low iron, normal pristanic/
  phytanic/VLCFA, jaundice, liver failure, liver fibrosis, anemia, and
  hepatosplenomegaly prompts.
