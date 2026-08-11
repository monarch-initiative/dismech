# IEMbase 0228: CPT1A-related Carnitine palmitoyltransferase 1A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 228 |
| Nosology | 4.1.02.01 |
| Gene | CPT1A |
| External IDs | OMIM:255120 |
| Generated mapping | CANDIDATE; `Carnitine_Palmitoyltransferase_II_Deficiency.yaml` |
| Candidate DisMech targets | Correct target: `Carnitine_Palmitoyltransferase_1A_Deficiency.yaml`; reject generated CPT II candidate |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CPT1A-related carnitine palmitoyltransferase 1A
deficiency, with the alternate label carnitine palmitoyl-CoA transferase 1
deficiency. The record is autosomal recessive and treatability is marked
unknown.

The biochemical rows include free carnitine, long-chain acylcarnitines, C16
and C18 species, transaminases, hypoketotic hypoglycemia context, dicarboxylic
organic acids, and glucose. Clinical and characteristic rows include liver
dysfunction and renal tubular acidosis. Treatments listed by IEMbase are
fasting avoidance and a carbohydrate-rich, long-chain-triglyceride-restricted
diet, sometimes with MCT supplementation.

## DisMech phenotype coverage

`Carnitine_Palmitoyltransferase_1A_Deficiency.yaml` is the correct target.
The local CPT1A entry covers the liver isoform of carnitine palmitoyltransferase
1, impaired outer-mitochondrial conversion of long-chain acyl-CoA to
acylcarnitine, hepatic energy failure, hypoketotic hypoglycemia,
hyperammonemia, high free carnitine with low total and long-chain
acylcarnitines, the C0/(C16+C18) diagnostic pattern, liver-focused disease,
fasting avoidance, high-carbohydrate/low-fat diet, MCT use, illness protocols,
and medication-avoidance cautions.

## Concordance and completeness

Judgement: generated fuzzy candidate is a false positive; local exact CPT1A
coverage exists.

The generated CPT II candidate is mechanistically wrong because CPT1A and CPT2
affect opposite sides of the carnitine shuttle and have different biochemical
signatures. IEMbase and the local CPT1A entry agree on hepatic long-chain
fatty-acid oxidation disease, fasting risk, hypoketotic hypoglycemia, liver
dysfunction, and dietary management. The local entry is stronger for the
distinctive CPT1A high-free-carnitine/low-long-chain-acylcarnitine pattern,
while IEMbase adds renal tubular acidosis as a review prompt.

## Curation actions

- Correct the mapping to `Carnitine_Palmitoyltransferase_1A_Deficiency.yaml`.
- Do not map this record to
  `Carnitine_Palmitoyltransferase_II_Deficiency.yaml`.
- Treat renal tubular acidosis as a potential phenotype-enrichment item for
  CPT1A if supported by primary evidence.
