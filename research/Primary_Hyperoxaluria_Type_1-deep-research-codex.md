# Primary Hyperoxaluria Type 1 - surrogate endpoint curation notes

## Scope

This curation maps the FDA adult and pediatric non-cancer surrogate endpoint
rows for primary hyperoxaluria type 1:

- FDA-SE-adult-noncancer-094: urinary oxalate, traditional approval, siRNA against hydroxyacid oxidase 1 gene.
- FDA-SE-pediatric-noncancer-062: urinary oxalate, traditional approval, siRNA against hydroxyacid oxidase 1 gene.

The main disease YAML keeps the biological assertion centered on PH1:
AGXT deficiency causes hepatic oxalate overproduction; urinary oxalate is the
measured biochemical burden and pharmacodynamic readout of that node.

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
- "RNA interference (RNAi) therapeutics (lumasiran and nedosiran) that target specific hepatic enzymes to reduce liver overproduction of oxalate"
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
