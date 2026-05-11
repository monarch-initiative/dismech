---
provider: codex
model: gpt-5
cached: true
start_time: '2026-05-11T20:21:17Z'
end_time: '2026-05-11T20:51:31Z'
duration_seconds: 1814.0
template_file: codex_surrogate_endpoint_curation
template_variables:
  disease_name: Primary Hyperoxaluria Type 1
  mondo_id: MONDO:0009823
  category: Mendelian
citation_count: 3
source_providers:
- pubmed
- fda_surrogate_endpoint_table
---

## Question

Curate primary hyperoxaluria type 1 in dismech with emphasis on the FDA adult
and pediatric urinary oxalate surrogate endpoint rows, integrating the marker
into the disease pathograph rather than creating a separate disease-level
surrogate endpoint section.

# Primary Hyperoxaluria Type 1 - deep research synthesis

## Scope

This curation maps the FDA adult and pediatric non-cancer surrogate endpoint
rows for primary hyperoxaluria type 1:

- FDA-SE-adult-noncancer-094: urinary oxalate, traditional approval, siRNA against hydroxyacid oxidase 1 gene.
- FDA-SE-pediatric-noncancer-062: urinary oxalate, traditional approval, siRNA against hydroxyacid oxidase 1 gene.

The main disease YAML keeps the biological assertion centered on PH1:
AGXT deficiency causes hepatic oxalate overproduction; urinary oxalate is the
measured biochemical burden and pharmacodynamic readout of that node.

## Disease Mechanism Synthesis

PH1 is a Mendelian hepatic glyoxylate-metabolism disorder caused by biallelic
AGXT pathogenic variants. The initiating defect is reduced liver peroxisomal
alanine-glyoxylate aminotransferase activity, which normally converts glyoxylate
to glycine. When that reaction is deficient, glyoxylate is converted to oxalate.
Oxalate cannot be metabolized and must be cleared renally, making urinary
oxalate both a direct disease-burden marker and a pharmacodynamic endpoint for
therapies that reduce hepatic oxalate production.

The pathograph therefore separates five linked events: AGT glyoxylate
transamination deficiency, hepatic oxalate overproduction, urinary oxalate
burden, calcium oxalate kidney deposition, and advanced CKD oxalate retention.
The phenotype layer captures nephrolithiasis, nephrocalcinosis, progressive
kidney dysfunction, and systemic oxalosis. Systemic oxalosis is modeled as an
advanced-disease consequence: reduced renal clearance permits high plasma
oxalate, driving calcium oxalate deposition in extra-renal tissues, especially
bone, heart, and retina.

## Treatment Landscape

The cached GeneReviews abstract identifies three targeted therapeutic
categories. Pyridoxine is variant-specific and reduces liver oxalate production
in individuals with missense AGXT variants known to be responsive. RNA
interference therapeutics, including lumasiran and nedosiran, target hepatic
enzymes to reduce liver oxalate overproduction. Liver transplantation restores
normal hepatic AGT enzyme activity. The disorder YAML models all three
categories, with lumasiran and nedosiran targeting hepatic oxalate
overproduction and pyridoxine/liver transplantation targeting the upstream AGT
deficiency node.

## Endpoint Interpretation

The FDA adult and pediatric rows identify urinary oxalate as a validated
surrogate endpoint in PH1 for traditional approval. The main disease YAML keeps
FDA row details in the source table and uses `biochemical.readouts` as the
bridge: urinary oxalate is a positive pharmacodynamic marker of hepatic oxalate
overproduction. ILLUMINATE-A provides human clinical evidence that lumasiran
reduces hepatic oxalate production by targeting glycolate oxidase and that the
primary endpoint was percent change in 24-hour urinary oxalate excretion.

## Ontology decisions

- Disease: MONDO:0009823 primary hyperoxaluria type 1.
- Gene: hgnc:341 AGXT for the causal defect.
- Treatment target context: hgnc:4809 HAO1 is the FDA-described siRNA target
  gene, but HAO1 is not modeled as disease-causal in the disorder YAML.
- Cell type: CL:0000182 hepatocyte.
- Molecular function: GO:0008453 L-alanine:glyoxylate transaminase activity.
- Biological process: GO:0009436 glyoxylate catabolic process.
- Chemical entities: CHEBI:30623 oxalate(2-), CHEBI:60579 calcium oxalate.
- Phenotypes: HP:0000787 nephrolithiasis, HP:0000121 nephrocalcinosis,
  HP:0000083 renal insufficiency with progressive course.
- Treatment action: MAXO:0001592 RNA interference therapy.
- Therapeutic agent: NCIT:C170137 Lumasiran.

## Evidence inventory

PMID:20301460 GeneReviews:

- "Primary hyperoxaluria type 1 (PH1) is caused by deficiency of the liver peroxisomal enzyme alanine-glyoxylate aminotransferase (AGT), which catalyzes the conversion of glyoxylate to glycine."
- "When AGT activity is reduced or absent, glyoxylate is converted to oxalate, which cannot be metabolized and must be excreted by the kidneys."
- "Insoluble calcium oxalate crystals form due to high urinary oxalate concentration."
- "Urinary crystals aggregate, leading to nephrolithiasis (i.e., calcium oxalate kidney stones)"
- "often the crystals deposit in kidney parenchyma (nephrocalcinosis)."
- "The diagnosis of PH1 is established in a proband with supportive laboratory findings (excess excretion of oxalate in the urine and/or markedly increased plasma oxalate concentration) and biallelic pathogenic variants in AGXT identified by molecular genetic testing."
- "Pyridoxine (vitamin B6) to reduce liver oxalate production in individuals with missense AGXT variants known to be pyridoxine responsive;"
- "RNA interference (RNAi) therapeutics (lumasiran and nedosiran) that target specific hepatic enzymes to reduce liver overproduction of oxalate"
- "liver transplantation to restore normal hepatic AGT enzyme activity."
- "in persons with advanced chronic kidney disease (CKD), high plasma oxalate concentrations result in other organ and tissue damage from calcium oxalate deposition (i.e., \"oxalosis\"), most commonly in the bones, heart, and retina."
- "PH1 is inherited in an autosomal recessive manner."

PMID:33789010 ILLUMINATE-A:

- "Primary hyperoxaluria type 1 (PH1) is a rare genetic disease caused by hepatic overproduction of oxalate that leads to kidney stones, nephrocalcinosis, kidney failure, and systemic oxalosis."
- "Lumasiran, an investigational RNA interference (RNAi) therapeutic agent, reduces hepatic oxalate production by targeting glycolate oxidase."
- "The primary end point was the percent change in 24-hour urinary oxalate excretion from baseline to month 6 (mean percent change across months 3 through 6)."
- "The least-squares mean difference in the change in 24-hour urinary oxalate excretion (lumasiran minus placebo) was -53.5 percentage points (P<0.001), with a reduction in the lumasiran group of 65.4% and an effect seen as early as month 1."
- "Lumasiran reduced urinary oxalate excretion, the cause of progressive kidney failure in PH1."

PMID:35257062 ILLUMINATE-A extension:

- "Long-term lumasiran treatment enabled sustained lowering of UOx levels with acceptable safety and encouraging results on clinical outcomes."

## Modeling notes

The FDA rows remain the regulatory source of truth for traditional approval and
the context of use. The disease YAML uses `biochemical.readouts` to bridge
urinary oxalate back to the pathograph node "Hepatic oxalate overproduction" and
stores the FDA row IDs only as `regulatory_endpoint_refs`.

No separate disease-level `surrogate_endpoints` section was added. This follows
the agreed pattern that disorder YAML should emphasize biology while the FDA
source table preserves precise regulatory metadata.
