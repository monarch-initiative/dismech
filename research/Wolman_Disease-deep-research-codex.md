---
provider: codex-local-synthesis
model: gpt-5
cached: true
start_time: '2026-04-14T19:53:03Z'
end_time: '2026-04-14T19:53:03Z'
duration_seconds: 0.0
template_file: codex_wolman_manual_curation
template_variables:
  disease_name: Wolman disease
  category: Mendelian
citation_count: 9
source_providers:
- pubmed
- mondo-ols
- clingen-cache
---

## Question

Curated deep-research synthesis for a disease-level Wolman disease dismech entry.

## Output

# Wolman Disease Curation Synthesis

## MONDO and ClinGen checks

- `MONDO:0019148` exact label: `Wolman disease` (MONDO/OLS).
- `MONDO:0800449` exact label: `lysosomal acid lipase deficiency` (MONDO/OLS).
- `MONDO:0019149` exact label: `cholesteryl ester storage disease` (MONDO/OLS).
- MONDO/OLS description for `MONDO:0019148`: `Wolman disease represents the most severe manifestation of lysosomal acid lipase deficiency. Milder phenotypes as a whole are referred to as cholesterol ester storage disease.`
- Local ClinGen cache cross-check: `cache/clingen/gene_validity.csv` records `LIPA -> lysosomal acid lipase deficiency (MONDO:0800449)` as `Definitive` by the `Lysosomal Diseases Gene Curation Expert Panel` on `2023-04-28`.
- Curation implication: anchor the disease file to the specific child term `Wolman disease`, while making the broader `lysosomal acid lipase deficiency` umbrella and the later-onset sibling phenotype `cholesteryl ester storage disease` explicit in the narrative and differential framing.

## Exact PMID-backed quote inventory

### Core disease framing

- PMID:28786388
  - `Lysosomal acid lipase deficiency is a rare, autosomal recessive condition caused by mutations in the gene encoding lysosomal acid lipase (LIPA) that result in reduced or absent activity of this essential enzyme.`
  - `Wolman's disease is a severe disorder that presents during infancy, resulting in failure to thrive, hepatomegaly, and hepatic failure, and an average life expectancy of less than 4 months.`
  - `Cholesteryl ester storage disorder arises later in life and is less severe, although the two diseases share many common features, including dyslipidaemia and transaminitis.`

### Proximal enzymatic defect

- PMID:30866656
  - `Lysosomal acid lipase (LAL), encoded by the lipase A ( LIPA) gene, hydrolyzes cholesteryl esters and triglycerides to generate free fatty acids and cholesterol in the cell.`
  - `In humans, loss-of-function mutations of LIPA cause rare lysosomal disorders, Wolman disease and cholesteryl ester storage disease, in which LAL enzyme-replacement therapy has shown significant benefits in a phase 3 clinical trial.`

- PMID:36204319
  - `Lysosomal acid lipase (LAL), encoded by the gene LIPA, is the sole neutral lipid hydrolase in lysosomes, responsible for cleavage of cholesteryl esters and triglycerides into their component parts.`
  - `Inherited forms of complete (Wolman Disease, WD) or partial LAL deficiency (cholesteryl ester storage disease, CESD) are fortunately rare.`

### Storage biology and tissue distribution

- PMID:41599846
  - `LAL deficiency leads to the accumulation of cholesteryl esters and triglycerides within the lysosomes, macrophages, and parenchymal cells in most tissue types, including those in the liver, gastrointestinal tract, and lymph nodes but excluding the central nervous system.`
  - `Infants with rapidly progressive LAL-D present with gastrointestinal disturbance, adrenomegaly with calcification, hepatosplenomegaly, growth failure due to malabsorption, and systemic inflammation.`

- PMID:23624251
  - `Lysosomal Acid Lipase (LAL) deficiency is a rare metabolic storage disease, caused by a marked reduction in activity of LAL, which leads to accumulation of cholesteryl esters (CE) and triglycerides (TG) in lysosomes in many tissues.`

### Natural history and severe infantile phenotype

- PMID:28179030
  - `Infants presenting with lysosomal acid lipase deficiency have marked failure to thrive, diarrhea, massive hepatosplenomegaly, anemia, rapidly progressive liver disease, and death typically in the first 6 months of life`
  - `Sebelipase alfa markedly improved survival with substantial clinically meaningful improvements in growth and other key disease manifestations in infants with rapidly progressive lysosomal acid lipase deficiency`

- PMID:34906190
  - `Wolman disease (WD), the rapidly progressive phenotype of lysosomal acid lipase (LAL) deficiency, presents in neonates with failure to thrive and hepatosplenomegaly, and leads to multi-organ failure and death before 12 months of age.`
  - `Early ERT initiation allowed 100% survival with positive outcomes.`

- PMID:33407676
  - `The findings of these 2 studies of infants with rapidly progressive LAL-D demonstrated that enzyme replacement therapy with sebelipase alfa prolonged survival with normal psychomotor development, improved growth, hematologic parameters, and liver parameters, and was generally well tolerated, with an acceptable safety profile.`

- PMID:24832708
  - `In early onset LAL deficiency, clinical manifestations start in the first few weeks of life with persistent vomiting, failure to thrive, hepatosplenomegaly, liver dysfunction and hepatic failure.`
  - `Adrenal calcification is a striking feature but is present in only about 50% of cases.`

## Curation decisions derived from the evidence

- Use a connected proximal chain:
  - `LIPA loss of function`
  - `Lysosomal acid lipase deficiency`
  - `Impaired lysosomal cholesteryl ester and triglyceride hydrolysis`
  - `Lysosomal cholesteryl ester and triglyceride storage`
- Split downstream tissue dysfunction rather than shortcutting directly to symptoms:
  - `Hepatic and reticuloendothelial lipid storage` -> `Progressive liver dysfunction`
  - `Intestinal lipid storage` -> `Malabsorption and severe gastrointestinal dysfunction`
  - `Adrenal cortical lipid storage`
- Keep phenotype assertions at the disease level and do not encode frequency unless the abstract supports the quantitative band directly.
- Connect `sebelipase alfa` to the proximal deficiency/storage nodes with `target_mechanisms`, and add dietary management separately because the literature frames treatment as a two-pronged ERT plus nutritional-management approach.

## Term shortlist used for grounding

- Disease terms:
  - `MONDO:0019148` `Wolman disease`
  - `MONDO:0019149` `cholesteryl ester storage disease`
- Gene:
  - `hgnc:6617` `LIPA`
- Molecular functions:
  - `GO:0004771` `sterol ester esterase activity`
  - `GO:0004806` `triacylglycerol lipase activity`
- Cellular component:
  - `GO:0043202` `lysosomal lumen`
- Biological processes:
  - `GO:0006629` `lipid metabolic process`
  - `GO:0008203` `cholesterol metabolic process`
- Chemicals:
  - `CHEBI:17002` `cholesteryl ester`
  - `CHEBI:17855` `triglyceride`
- Cell types:
  - `CL:0000235` `macrophage`
  - `CL:0000182` `hepatocyte`
  - `CL:0000584` `enterocyte`
- Anatomical locations:
  - `UBERON:0002107` `liver`
  - `UBERON:0002106` `spleen`
  - `UBERON:0002108` `small intestine`
  - `UBERON:0001235` `adrenal cortex`
  - `UBERON:0000029` `lymph node`
- Phenotypes:
  - `HP:0001508` `Failure to thrive`
  - `HP:0001433` `Hepatosplenomegaly`
  - `HP:0002014` `Diarrhea`
  - `HP:0002013` `Vomiting`
  - `HP:0002024` `Malabsorption`
  - `HP:0010512` `Adrenal calcification`
  - `HP:0001903` `Anemia`
- Treatments:
  - `MAXO:0000933` `enzyme replacement or supplementation therapy`
  - `NCIT:C152312` `Sebelipase Alfa`
  - `MAXO:0000088` `dietary intervention`
