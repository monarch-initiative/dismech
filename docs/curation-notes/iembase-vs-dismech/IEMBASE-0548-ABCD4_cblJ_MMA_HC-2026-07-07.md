# IEMbase 0548: ABCD4-related cblJ methylmalonic aciduria and homocystinuria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 548 |
| Nosology | 21.9.08.01 |
| Gene | ABCD4 |
| External IDs | OMIM:614857; ORPHA:369955 |
| Generated mapping | MAPPED; `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblJ` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblJ` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABCD4-related methylmalonic aciduria and homocystinuria,
cblJ type, with alternate labels adenosylcobalamin and methylcobalamin
synthesis defect cblJ and cblJ. The record is autosomal recessive, marked
treatable, and lists betaine and hydroxocobalamin.

The biochemical rows show combined cobalamin disease: increased urinary and
total homocysteine, low-to-normal methionine, increased C3 propionylcarnitine,
3-hydroxypropionic acid, methylcitric acid, and methylmalonic acid, plus low
plasma and CSF S-adenosylmethionine. Characteristic clinical rows include
megaloblastic anemia, failure to thrive, life-threatening illness, neurologic
dysfunction, and impaired vision. Additional rows include cardiomyopathy,
cerebral atrophy, dementia, developmental delay, extrapyramidal signs, feeding
difficulties, hematuria, hemolytic uremic syndrome, hypotonia, liver
dysfunction, maculopathy, myelopathy, hypersegmented neutrophils, nystagmus,
psychiatric disturbances, retinopathy, and seizures.

## DisMech phenotype coverage

The generated cblJ subtype mapping is correct. The local cobalamin umbrella
explicitly includes cblJ as ABCD4 deficiency, with impaired lysosomal cobalamin
export producing combined methylmalonic acidemia and homocystinuria. It models
reduced active cobalamin cofactor supply, impaired methionine synthase and
methylmalonyl-CoA mutase branches, homocysteine accumulation, methionine
depletion, methylmalonic acid accumulation, neurologic disease, megaloblastic
anemia, failure to thrive, seizures, ocular disease, and hydroxocobalamin plus
betaine treatment context.

## Concordance and completeness

Judgement: correct high-concordance mapping to the cblJ subtype.

IEMbase and DisMech agree on ABCD4 identity, cblJ scope, combined MMA/HC
biochemistry, recessive inheritance, neurologic and hematologic presentation,
ocular involvement, and hydroxocobalamin/betaine therapy. DisMech is stronger
for the mechanism from cobalamin transport to the two cofactor-dependent enzyme
branches.

IEMbase adds useful detail for S-adenosylmethionine in plasma and CSF,
hypersegmented neutrophils, maculopathy/retinopathy/nystagmus, myelopathy,
hematuria, hemolytic uremic syndrome, and age-patterned severity.

## Curation actions

- Keep this record mapped to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblJ`.
- Consider adding the IEMbase SAM, CSF SAM, hypersegmented-neutrophil, HUS,
  renal, myelopathy, and detailed ocular rows as enrichment prompts.
- Preserve treatment wording for hydroxocobalamin and betaine.
