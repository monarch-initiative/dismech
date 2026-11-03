# Citations for Research Query

**Query:** # Mechanism Module Research Template

## Target Module
- **Module Name:** Hepatic Gluconeogenesis Failure Module
- **Module Slug:** hepatic_gluconeogenesis_failure
- **Category:** Module

## Current Module Description

A conserved mechanism module representing the final common pathway by which a loss-of-function lesion at any one of the rate-controlling gluconeogenic enzymes collapses de novo glucose synthesis in the liver and produces the shared biochemical signature of the gluconeogenic enzymopathies: fasting (and catabolic-stress) hypoglycemia together with lactic acidosis. The four classic enzyme blocks - pyruvate carboxylase (PC), cytosolic phosphoenolpyruvate carboxykinase (PEPCK/PCK1), fructose-1,6-bisphosphatase (FBP1), and glucose-6-phosphatase (G6PC) - sit at different points of the pathway but converge on one gene-agnostic step: the hepatocyte can no longer convert three-carbon precursors into glucose and release it into the circulation. Two consequences fan out from that convergence. On the output side, failed hepatic glucose production causes fasting hypoglycemia, which deprives the brain of its obligate fuel and produces neuroglycopenic manifestations (lethargy, seizures, coma). On the substrate side, the three-carbon precursors that cannot be consumed by gluconeogenesis (pyruvate, lactate, alanine, glycerol) accumulate, driving lactate overproduction and a high-anion-gap lactic acidosis. Conforming disorder entries substitute the specific blocked enzyme and its position on the pathway while preserving this core chain. Key conformance target: `hepatic_gluconeogenesis_failure#Failure of Hepatic De Novo Glucose Production`. Real and potential conformers already in kb that a curator would wire to this module: Fructose-1,6-Bisphosphatase_Deficiency (FBP1, the committed gluconeogenic step converting fructose-1,6-bisphosphate to fructose-6- phosphate), Pyruvate_Carboxylase_Deficiency_Disease (PC, the anaplerotic pyruvate-to-oxaloacetate entry step), Glycogen_Storage_Disease_Type_I (G6PC, the terminal glucose-6-phosphate dephosphorylation shared by gluconeogenesis and glycogenolysis), and the cytosolic PEPCK (PCK1) entry being curated in parallel. Complementary to, and deliberately distinct from, the respiratory-chain and bioenergetic modules. complex_i_deficiency and mitochondrial_dysfunction also terminate in lactic acidosis, but by a different mechanism - failed oxidative ATP synthesis forcing anaerobic glycolysis - and they do not primarily impair de novo glucose synthesis; this module's lactic acidosis arises from unconsumed gluconeogenic substrate, not from a respiratory-chain block. peroxisomal_metabolic_failure and congenital_disorder_of_glycosylation are other hepatic/metabolic modules that act on entirely different substrates and do not converge on hepatic glucose output. Where a conformer carries both a gluconeogenic block and a secondary respiratory-chain phenotype (PC deficiency can show secondary complex IV deficiency), it may conform to this module and a respiratory-chain module at different nodes.

## Current Provisional Nodes

- Gluconeogenic Flux Block: A loss-of-function lesion in one of the rate-controlling gluconeogenic enzymes - pyruvate carboxylase, cytosolic phosphoenolpyruvate carboxykinase, fructose-1,6-bisphosphatase, or glucose-6-phosphatase - interrupts carbon flux through the hepatic gluconeogenic pathway. Conforming entries substitute the specific enzyme and its position on the pathway.
- Failure of Hepatic De Novo Glucose Production: With any committed step blocked, the hepatocyte can no longer synthesize new glucose from three-carbon precursors. This is the gene-agnostic, rate-limiting convergence every conforming disorder funnels through, whatever the specific enzyme lesion. PC, PEPCK, and FBP1 fail to build free glucose-6-phosphate, while G6PC fails to dephosphorylate it to glucose; both routes abolish net de novo glucose production.
- Reduced Hepatic Glucose Output: The liver fails to release glucose into the circulation during fasting. Hepatic gluconeogenesis is one of the fluxes summed into net hepatic glucose production, so losing it lowers the glucose the liver can supply once dietary intake stops and glycogen stores are depleted.
- Fasting Hypoglycemia: Once dietary glucose and glycogen stores are exhausted, the loss of hepatic glucose output causes blood glucose to fall during fasting or catabolic stress (fever, intercurrent illness, reduced intake).
- Accumulation of Gluconeogenic Three-Carbon Substrates: Three-carbon precursors that would normally be consumed by gluconeogenesis - pyruvate, lactate, alanine, and glycerol - accumulate upstream of the enzyme block. The accumulation is most prominent for the enzymes nearest pyruvate (PC, PEPCK), where the entry steps of the pathway are blocked.
- Lactate Overproduction: The accumulated pyruvate is reduced to lactate, elevating the circulating lactate concentration. Because the gluconeogenic sink for lactate is disabled, lactate generated by ongoing glycolysis is no longer recycled to glucose.
- Lactic Acidosis: Elevated circulating lactate produces a high-anion-gap metabolic acidosis, the second cardinal biochemical feature of the gluconeogenic enzymopathies alongside hypoglycemia.
- CNS Glucose Deprivation: The brain depends on blood glucose as its obligate fuel, so fasting hypoglycemia deprives neurons of their primary energy substrate. Prolonged or recurrent deprivation injures the central nervous system.
- Neuroglycopenic Dysfunction: Neuronal energy failure from glucose deprivation produces the acute neuroglycopenic manifestations of the gluconeogenic enzymopathies: lethargy, seizures, and - in severe crises - coma.

## Research Objective

Prepare a mechanism-focused research report for the dismech module above. This
is not a disease entry. The goal is to support a reusable mechanism module that
multiple gene-axis disease entries can conform to.

Focus the search on the shared biology described in the module description and
provisional nodes above. Prioritize evidence for:

- The conserved causal chain represented by the proposed nodes.
- The biological distinctions between node subgroups, especially if the module
  defines branching pathways.
- Any optional or gene-specific branches described in the node list, while
  distinguishing them from core module requirements.
- Explicit exclusions or boundary conditions stated in the module description.

## Questions To Answer

1. What is the best-supported shared mechanism for this module?
2. Is the current module name and scope appropriate, or is a clearer name or
   narrower boundary supported by the literature?
3. Which nodes should be core and required for conformance, and which nodes
   should be optional or gene-specific?
4. Which genes, variants, exposures, cell types, tissues, or molecular
   processes support each branch or node?
5. What evidence supports the causal edges between upstream drivers, central
   effectors, and downstream consequences?
6. What direct human evidence links the same causal factor or variant class to
   multiple clinical or pathological manifestations?
7. What model organism, in vitro, or other experimental evidence clarifies the
   causal path from molecular perturbation to phenotype?
8. What Gene Ontology biological process terms, Cell Ontology cell types, and
   anatomical terms should be used in the module?
9. What claims are speculative, weakly supported, or should remain out of scope?

## Evidence Requirements

- Cite primary literature with PMID identifiers whenever possible.
- Include exact abstract quotes for candidate evidence snippets.
- Separate human clinical, model organism, in vitro, and review evidence.
- Flag papers where the abstract is insufficient and full-text verification is
  needed before curation.
- Do not invent ontology IDs. Suggest terms by label when unsure.

## Desired Output

Structure the report with:

- Executive recommendation for module name and scope.
- Proposed DAG nodes and causal edges.
- Gene-to-node mapping table.
- Evidence table with PMID, evidence type, exact quote, and supported claim.
- Ontology suggestions for GO, CL, and UBERON terms.
- Out-of-scope boundary notes.
- Open questions for curator review.

**Provider:** claude_code
**Generated:** 2026-10-16T03:42:07.996679

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31804789,34687058,28368361,25246452,23622387,12013992,37924129,35868242,34622459,33445193&rettype=abstract&retmode=text
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=20301489,20301764&rettype=abstract&retmode=text