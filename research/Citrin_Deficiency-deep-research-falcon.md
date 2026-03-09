---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:20:51.078308'
end_time: '2026-02-23T23:35:52.715510'
duration_seconds: 901.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Citrin Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Citrin Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Citrin Deficiency**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Citrin Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Citrin Deficiency**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Title: Citrin Deficiency (SLC25A13) — Pathophysiology Research Report (Genetic; MONDO_0016602)

Publication focus: molecular/cellular mechanisms of disease progression with 2023–2024 emphasis.

1. Executive summary (current understanding)
Citrin deficiency is an autosomal recessive disorder caused by biallelic loss-of-function variants in SLC25A13, which encodes citrin (aspartate–glutamate carrier 2; AGC2), an inner mitochondrial membrane carrier and core component of the hepatic malate–aspartate shuttle (MAS). Loss of citrin impairs (i) export of mitochondrial aspartate to the cytosol and (ii) cytosolic NADH→mitochondrial NADH transfer needed to regenerate cytosolic NAD+. These defects produce a characteristic hepatocellular energy/redox crisis that secondarily perturbs carbohydrate handling, de novo lipogenesis, fatty-acid oxidation, and ammonia detoxification, yielding a staged phenotype: NICCD (neonatal intrahepatic cholestasis), FTTDCD (failure to thrive and dyslipidemia), and CTLN2 (adult-onset hyperammonemic encephalopathy). The most up-to-date mechanistic synthesis (2024) explicitly frames the disease as a “mitochondrial hepatopathy” with carbohydrate toxicity and identifies medium-chain triglyceride (MCT) plus low-carbohydrate dietary therapy as a rational energy-substitution strategy. (hayasaka2024pathogenesisandmanagement pages 1-2, hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 7-9)

2. Disease definition, identifiers, and key concepts
2.1 Disease names and MONDO identifiers
• Citrin deficiency: MONDO_0016602 (OpenTargets disease association evidence). (hayasaka2024pathogenesisandmanagement pages 2-4)
• Neonatal intrahepatic cholestasis due to citrin deficiency (NICCD): MONDO_0011601. (hayasaka2024pathogenesisandmanagement pages 2-4)
• Citrullinemia type II / adult-onset type II citrullinemia (CTLN2): MONDO_0016603. (hayasaka2024pathogenesisandmanagement pages 2-4)

2.2 Core molecular definition
Citrin (AGC2; SLC25A13) is an aspartate–glutamate carrier in the inner mitochondrial membrane that functions within the MAS. A key mechanistic statement from a 2024 review is that the MAS “transports NADH produced by glycolysis from the cytosol to the mitochondria and regenerates cytosolic NAD+,” and that citrin is “indispensable for hepatic glycolysis, de novo lipogenesis, and energy metabolism.” (Hayasaka 2024, Jul 2024, Internal Medicine; https://doi.org/10.2169/internalmedicine.2595-23) (hayasaka2024pathogenesisandmanagement pages 1-2)

Complementary 2023 review-level mechanism: “Through MAS, AGC2 is necessary to maintain intracellular redox balance, mitochondrial respiration, and ATP synthesis.” (Holeček 2023, Jun 2023, BMB Reports; https://doi.org/10.5483/bmbrep.2023-0052) (holecek2023aspartateglutamatecarrier2 pages 1-2)

PMID note: The retrieved excerpts for the 2023–2024 reviews included DOIs and URLs but did not display PMIDs; therefore PMIDs cannot be cited from the retrieved text itself. (hayasaka2024pathogenesisandmanagement pages 1-2, holecek2023aspartateglutamatecarrier2 pages 1-2)

3. Core pathophysiology (molecular and cellular mechanisms)
3.1 Primary defect: mitochondrial aspartate export and MAS failure
Citrin deficiency disrupts the malate–aspartate shuttle, reducing cytosolic aspartate availability and impairing cytosolic redox balance (NADH/NAD+), which is required for sustained hepatic glycolysis and downstream ATP production. The 2024 synthesis explicitly links MAS failure to reduced “cytosolic aspartate, NAD+ and ATP,” and to impaired “glycolysis, glycogenesis and de novo lipogenesis.” (hayasaka2024pathogenesisandmanagement pages 2-4)

Mechanistic schematic evidence: Hayasaka 2024 Figure 2 contrasts control vs citrin-deficient livers and highlights MAS impairment, compensatory malate–citrate shuttle (MCS), and the role of MCT supplementation in restoring ATP/cytosolic NAD+ (figure evidence). (hayasaka2024pathogenesisandmanagement media 4eb23285)

3.2 Secondary energy metabolism derailment: glycolysis block and carbohydrate toxicity
A major contemporary concept is that high carbohydrate exposure is not neutral in citrin deficiency; it can be actively harmful (“carbohydrate toxicity”). The 2024 review states: “its metabolism is inhibited at the glyceraldehyde 3-phosphate dehydrogenase step, leading to the accumulation of glucose metabolites and a decrease in Pi and ATP levels in hepatocytes,” and warns that “Infusion of glycerol- and fructose-containing osmotic agents is lethal and contraindicated.” (hayasaka2024pathogenesisandmanagement pages 7-9)

This is consistent with the MAS role described in 2023, which emphasizes MAS as the route for indirect transfer of cytosolic NADH generated by GAPDH into mitochondria, thereby coupling glycolysis to oxidative phosphorylation. (holecek2023aspartateglutamatecarrier2 pages 2-4)

3.3 Urea cycle / hyperammonemia: aspartate and ATP limitation, plus GS-centered detoxification failure
Classically, CTLN2 presents with hyperammonemia and citrullinemia; mechanistically, two layers are highlighted in 2024:
• Aspartate/ATP dependence of citrulline metabolism: “Citrulline is metabolized by ASS1, which requires aspartate and ATP,” and citrin is described as the essential mitochondrial→cytosol aspartate transport route in liver, providing a direct mechanism for citrullinemia when aspartate/ATP are limited. (hayasaka2024pathogenesisandmanagement pages 2-4)
• Hyperammonemia may be driven less by intrinsic ASS1 enzymatic failure and more by failure of perivenous ammonia “mopping up” through glutamine synthesis. The 2024 review states: “These findings indicate that hyperammonemia is not primarily caused by a defect in ASS1 but rather by a defect in GS due to a substrate (glutamate) and/or ATP deficiency.” (hayasaka2024pathogenesisandmanagement pages 4-6)

Mechanistic schematic evidence: Hayasaka 2024 Figure 4 summarizes periportal ureagenesis and the requirement for cytosolic aspartate for the ASS1 reaction, connecting citrin deficiency to impaired ureagenesis and hyperammonemia (figure evidence). (hayasaka2024pathogenesisandmanagement media c2a905ba)

A notable biochemical phenotype emphasized in 2024 is: “The absence of increased plasma glutamine concentrations despite hyperammonemia is also a characteristic symptom associated with CTLN2.” (hayasaka2024pathogenesisandmanagement pages 4-6)

3.4 Lipid metabolism: de novo lipogenesis defects, PPARα downregulation, impaired β-oxidation, fatty liver
The 2024 review states that “citrin-deficient hepatocytes have primary defects in glycolysis and de novo lipogenesis and exhibit secondarily downregulated PPARα, leading to impaired β-oxidation.” (hayasaka2024pathogenesisandmanagement pages 1-2)

The integrated model is that impaired de novo lipogenesis decreases signals that would otherwise maintain PPARα activity, lowering fatty-acid oxidation capacity and contributing to hepatic steatosis; the review further links fatty liver to PPARα downregulation and suppressed fatty-acid oxidation gene expression. (hayasaka2024pathogenesisandmanagement pages 2-4)

3.5 Stress biology: ER/oxidative stress and arrested hepatic maturation/zonation
The 2024 synthesis describes increased ER/oxidative stress and frames citrin deficiency as a “mitochondrial hepatopathy” where energy failure impairs normal hepatocyte maturation, including lobular zonation. It highlights that in CTLN2 the distribution of ASS1- and GS-positive hepatocytes is altered, consistent with impaired periportal/perivenous functional partitioning of ammonia detoxification. (hayasaka2024pathogenesisandmanagement pages 4-6)

4. Key molecular players (genes/proteins, metabolites/chemicals, cell types, anatomical locations)
4.1 Genes/proteins
Causal gene
• SLC25A13 (encodes citrin/AGC2): causal for citrin deficiency across NICCD/FTTDCD/CTLN2. (hayasaka2024pathogenesisandmanagement pages 1-2, wang2023casereportthree pages 1-2)

Core pathway components (as referenced mechanistically)
• MAS enzymes/transporters: malate dehydrogenase (MDH; cytosol and mitochondrial matrix), aspartate aminotransferase (AST/GOT; cytosol and mitochondrial matrix), 2-oxoglutarate carrier (OGC), and AGC2 (citrin) in the inner mitochondrial membrane. (holecek2023aspartateglutamatecarrier2 pages 2-4)
• Urea cycle and ammonia detoxification: ASS1 (argininosuccinate synthetase 1) is highlighted as requiring cytosolic aspartate and ATP; GS (glutamine synthetase) is implicated as the critical ammonia “backup” route affected by substrate/ATP deficiency. (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6)
• Lipid oxidation regulator: PPARα downregulation is linked to impaired β-oxidation. (hayasaka2024pathogenesisandmanagement pages 1-2)

Regulatory/structural note
• AGC2 contains EF-hand motifs “facing the intermembrane space for calcium binding,” consistent with Ca2+-regulated carrier activity. (holecek2023aspartateglutamatecarrier2 pages 1-2)

4.2 Chemical entities (metabolites, dietary therapeutics, contraindicated agents)
Key metabolites implicated
• Aspartate, glutamate (carrier substrates; nitrogen flux), citrulline (biomarker/urea-cycle intermediate), ammonia (toxic effector), glutamine (often not elevated in CTLN2 despite hyperammonemia), citrate (MCS intermediate), NADH/NAD+ (redox pair), ATP, inorganic phosphate (Pi). (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6, hayasaka2024pathogenesisandmanagement pages 7-9)

Therapeutically relevant chemicals
• Medium-chain triglycerides (MCT) / medium-chain free fatty acids (MCFA): provide hepatocyte energy and support metabolic shuttles; MCT supplementation can normalize urea-cycle amino acids in NICCD within days and improves biochemical/clinical status when combined with carbohydrate restriction. (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement media 4eb23285)

Contraindicated/triggering chemicals
• Fructose and glycerol infusions: “lethal and contraindicated.” (hayasaka2024pathogenesisandmanagement pages 7-9)

4.3 Cell types (CL-oriented)
• Hepatocyte (CL:0000182) as the key disease cell type; “citrin-deficient hepatocytes” have primary glycolysis/lipogenesis defects and energy deficiency. (hayasaka2024pathogenesisandmanagement pages 1-2)
• Periportal (zone 1) ureagenic hepatocytes vs perivenous/pericentral (zone 3) glutamine-synthesizing hepatocytes: ammonia detoxification is partitioned; CTLN2 disrupts zonation and ASS1/GS distribution. (hayasaka2024pathogenesisandmanagement pages 4-6, holecek2023aspartateglutamatecarrier2 pages 1-2)

4.4 Anatomical locations (UBERON-oriented)
• Liver (UBERON:0002107): primary affected organ across all stages. (hayasaka2024pathogenesisandmanagement pages 1-2, hayasaka2024pathogenesisandmanagement pages 2-4)
• Hepatic lobule zones (periportal vs perivenous/pericentral regions): functional zonation relevant to urea cycle vs glutamine synthesis. (hayasaka2024pathogenesisandmanagement pages 4-6, holecek2023aspartateglutamatecarrier2 pages 1-2)
• Brain (UBERON:0000955): affected clinically via hyperammonemic encephalopathy in CTLN2. (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6)
• Pancreas (UBERON:0001264): pancreatitis is listed among complications in the disease spectrum. (hayasaka2024pathogenesisandmanagement pages 2-4)

4.5 Cellular components (GO-CC oriented)
• Mitochondrial inner membrane (GO:0005743): localization of citrin/AGC2 and other carriers. (holecek2023aspartateglutamatecarrier2 pages 2-4)
• Mitochondrial matrix (GO:0005759) and cytosol (GO:0005829): MDH/AST reactions operate in both compartments; MAS couples these compartments. (holecek2023aspartateglutamatecarrier2 pages 2-4)
• Mitochondrial intermembrane space (GO:0005758): AGC2 EF-hand motifs face the IMS for Ca2+ regulation. (holecek2023aspartateglutamatecarrier2 pages 1-2)

5. Biological processes disrupted (GO terms; suggested mappings)
The following GO biological processes are directly supported by the cited mechanistic descriptions (terms are suggested targets for annotation; exact ontology IDs should be confirmed against GO):
• Malate–aspartate shuttle activity / NADH shuttling / cellular redox homeostasis (supported by explicit MAS redox balance statements). (hayasaka2024pathogenesisandmanagement pages 1-2, holecek2023aspartateglutamatecarrier2 pages 1-2)
• Glycolytic process and regulation of glycolysis (glycolysis impairment; GAPDH-step inhibition under carbohydrate load). (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 7-9)
• Aspartate and glutamate transmembrane transport (mitochondrial export/import by AGC2). (holecek2023aspartateglutamatecarrier2 pages 2-4)
• Urea cycle and ammonia detoxification (ASS1 dependence on aspartate/ATP; zonated detoxification and GS-centered failure mechanism). (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6)
• De novo lipogenesis / fatty acid biosynthetic process (primary defect described). (hayasaka2024pathogenesisandmanagement pages 1-2, hayasaka2024pathogenesisandmanagement pages 2-4)
• Fatty acid beta-oxidation and its regulation via PPARα (secondary PPARα downregulation with impaired β-oxidation). (hayasaka2024pathogenesisandmanagement pages 1-2)
• Response to ER stress / oxidative stress (increased ER/oxidative stress described in pathogenesis). (hayasaka2024pathogenesisandmanagement pages 6-7)

6. Disease progression model (sequence of events; stages)
6.1 Mechanistic sequence (molecular-to-clinical)
1) Trigger: congenital loss of citrin transport activity in hepatocyte mitochondria. (hayasaka2024pathogenesisandmanagement pages 1-2)
2) Early metabolic consequences: impaired MAS and aspartate export → reduced cytosolic NAD+ and ATP and cytosolic aspartate deficiency. (hayasaka2024pathogenesisandmanagement pages 2-4)
3) Pathway-level effects:
   • Glycolysis and glycogenesis fall; carbohydrate load can further deplete ATP due to GAPDH-step inhibition and redox imbalance. (hayasaka2024pathogenesisandmanagement pages 7-9)
   • De novo lipogenesis decreases; PPARα downregulates; β-oxidation becomes impaired → steatosis and dyslipidemia risk. (hayasaka2024pathogenesisandmanagement pages 1-2)
   • Urea-cycle flux is perturbed by limited aspartate/ATP; hyperammonemia may be driven by impaired GS-mediated detoxification due to glutamate/ATP deficiency and altered zonation. (hayasaka2024pathogenesisandmanagement pages 4-6)
4) Tissue/organ manifestations: neonatal cholestasis/steatosis (NICCD), later growth failure/hypoglycemia/hyperlipidemia (FTTDCD), and episodic hyperammonemic encephalopathy in a subset (CTLN2). (hayasaka2024pathogenesisandmanagement pages 2-4)

6.2 Clinical stages (phenotype spectrum)
A 2024 synthesis explicitly describes NICCD, an interstage that may appear “apparently healthy,” possible evolution to FTTDCD, and adult-onset CTLN2 (~5% of patients; age range stated as 10–70 years) with complications including pancreatitis and HCC risk. (hayasaka2024pathogenesisandmanagement pages 2-4)

7. Phenotypic manifestations (HP terms; suggested mappings)
Suggested phenotype mappings (HP IDs should be validated in the target ontology build):
• Neonatal cholestasis / conjugated hyperbilirubinemia (NICCD). (chuenwattana2024neonatalintrahepaticcholestasis pages 1-3)
• Failure to thrive / growth impairment (FTTDCD; also NICCD severe cases). (hayasaka2024pathogenesisandmanagement pages 2-4)
• Dyslipidemia / hyperlipidemia (FTTDCD; CTLN2-associated metabolic phenotype). (hayasaka2024pathogenesisandmanagement pages 2-4)
• Fatty liver / hepatic steatosis (common across stages). (hayasaka2024pathogenesisandmanagement pages 2-4)
• Hypoketotic hypoglycemia (mechanistically linked to impaired glycogenesis/gluconeogenesis/ketogenesis). (hayasaka2024pathogenesisandmanagement pages 1-2)
• Hyperammonemia and encephalopathy (CTLN2). (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6)
• Elevated citrulline (biochemical hallmark; reflects urea-cycle perturbation). (hayasaka2024pathogenesisandmanagement pages 2-4)

8. Recent developments (2023–2024) and real-world implementations
8.1 Newborn screening and second-tier genetic testing
A 2024 implementation study reports an operational two-tier newborn screening strategy combining first-tier MS/MS analytes with second-tier targeted NGS on dried blood spots for six IEMs including citrin deficiency. Quantitative performance/operations:
• N screened: 22,883 newborns (Sept 2021–Aug 2022). (chan2024harnessingnextgenerationsequencing pages 3-5)
• Second-tier genetic testing applied to 1.8% (421/22,883). (chan2024harnessingnextgenerationsequencing pages 3-5)
• Recall rate: 0.031% (7/22,883). (chan2024harnessingnextgenerationsequencing pages 3-5)
• False positive rate (post-NGS): 0.017% across six conditions. (chan2024harnessingnextgenerationsequencing pages 1-2, chan2024harnessingnextgenerationsequencing pages 3-5)
• Turnaround time: median 3.5 days, TAT90 = 5 working days. (chan2024harnessingnextgenerationsequencing pages 3-5)
• Clinical yield: true positives included citrin deficiency/citrullinemia type II (n=2); authors state two CD cases would have been missed if relying on first-tier biochemical screening alone. (chan2024harnessingnextgenerationsequencing pages 1-2)
• Implementation detail: targeted detection of SLC25A13 hotspot IVS16ins3kb using a CNV-calling approach began May 2023. (chan2024harnessingnextgenerationsequencing pages 2-3)
(Chan et al., Mar 2024; https://doi.org/10.3390/ijns10010019) (chan2024harnessingnextgenerationsequencing pages 1-2, chan2024harnessingnextgenerationsequencing pages 2-3)

8.2 Recognition of biochemical false negatives / borderline citrulline
A 2024 Thai NICCD series emphasizes that dried blood spot citrulline can be borderline/normal and that relying only on biochemical cutoffs may miss cases; it explicitly discusses eNBS expansion (regions 7/8 from Oct 2023) and argues for ethnicity-tailored molecular second-tier testing. (Chuenwattana et al., Apr 2024; https://doi.org/10.1016/j.hmedic.2024.100051) (chuenwattana2024neonatalintrahepaticcholestasis pages 3-5, chuenwattana2024neonatalintrahepaticcholestasis pages 1-3)

8.3 Variant spectrum expansion via clinical genomics
A 2023 NICCD case report of four infants reported three novel SLC25A13 variants (nonsense, frameshift, and whole-exon deletion) and reiterates that genetic testing is important for diagnosis due to atypical phenotypes. (Wang et al., Mar 2023; https://doi.org/10.3389/fped.2023.1103877) (wang2023casereportthree pages 1-2)

9. Epidemiology and statistics (recently reported)
9.1 Carrier rates and incidence (selected populations)
• Japan: carrier rate approximately 1:42–1:65 in parts of Japan. (hayasaka2024pathogenesisandmanagement pages 1-2)
• China: carrier rate reported as 1/65. (wang2023casereportthree pages 1-2)
• Thailand: incidence estimated at ~1 in 33,000 live births; cited Thai carrier frequency for a variant at least 1 in 90. (chuenwattana2024neonatalintrahepaticcholestasis pages 1-3, chuenwattana2024neonatalintrahepaticcholestasis pages 3-5)

9.2 Screening yield improvement with molecular methods (Thailand; cited within 2024 report)
The Thai series cites that adding molecular testing after MS/MS screening increased detection from 1/32,673 to 1/18,006. (chuenwattana2024neonatalintrahepaticcholestasis pages 3-5)

9.3 Hospitalized newborn cohort burden (China)
A 2024 cohort study of 21,840 hospitalized infants (Chongqing; 2017–2022) reports IEM incidence among hospitalized newborns of 1/377 (58/21,840) and notes NICCD among prevalent disorders in premature infants (contextualizing NICCD in hospital-based diagnostic practice). (Wang et al., May 2024; https://doi.org/10.3389/fgene.2024.1395988) (hayasaka2024pathogenesisandmanagement pages 2-4)

10. Current applications and real-world management
10.1 Dietary therapy (MCT + carbohydrate restriction)
The 2024 review frames therapy as addressing hepatocyte energy deficiency and redox/ATP limitations. It recommends MCT supplementation with a minimal-carbohydrate diet “promptly after the diagnosis” to prevent irreversible damage. (hayasaka2024pathogenesisandmanagement pages 2-4)

Operational dietary rationale and quantitative response:
• The review describes an ~8 h “energy depletion period” after meals due to insulin-mediated lowering of free fatty acids, recommending MCT supplementation during this interval. (hayasaka2024pathogenesisandmanagement pages 7-9)
• It provides a quantitative biochemical change: plasma glutamate increased from 51.3±18.8 to 168.3±92.0 μmol/L at 2–3 weeks after MCT (p=0.012). (hayasaka2024pathogenesisandmanagement pages 6-7)

10.2 Clinical caution points relevant to implementation
• Avoid fructose/glycerol-containing infusions (contraindicated). (hayasaka2024pathogenesisandmanagement pages 7-9)

10.3 Newborn screening program design
• A practical recent implementation is the addition of second-tier NGS with specific hotspot detection (IVS16ins3kb) and refined recall rules to reduce false positives while maintaining sensitivity. (chan2024harnessingnextgenerationsequencing pages 3-5, chan2024harnessingnextgenerationsequencing pages 2-3)

11. Expert analysis (authoritative perspectives)
A key expert-level synthesis (Internal Medicine, 2024) interprets the disorder primarily as an energy/redox hepatopathy rather than a simple urea-cycle enzyme deficiency, emphasizing the MAS/MCS interplay, carbohydrate toxicity, and secondary transcriptional dysregulation (PPARα) that impairs lipid oxidation. (hayasaka2024pathogenesisandmanagement pages 1-2, hayasaka2024pathogenesisandmanagement pages 7-9)

The same synthesis argues that hyperammonemia in CTLN2 is better explained by failure of GS-dependent detoxification due to glutamate/ATP shortage (“not primarily caused by a defect in ASS1”), which reorients mechanistic thinking and provides a rationale for energy-targeted therapy. (hayasaka2024pathogenesisandmanagement pages 4-6)

12. Knowledge-base style annotations
12.1 Gene/protein annotations (HGNC-like)
• Gene: SLC25A13 (solute carrier family 25 member 13) → Protein: citrin/AGC2; subcellular: mitochondrial inner membrane; IMS-facing Ca2+-binding EF-hand extension. (hayasaka2024pathogenesisandmanagement pages 1-2, holecek2023aspartateglutamatecarrier2 pages 1-2)

12.2 Suggested GO Biological Process annotations (evidence-cited)
• Cellular redox homeostasis / NADH oxidation via MAS (holecek2023aspartateglutamatecarrier2 pages 1-2)
• Malate-aspartate shuttle / mitochondrial NADH shuttling (hayasaka2024pathogenesisandmanagement pages 1-2)
• Aspartate transport (mitochondrion→cytosol) (holecek2023aspartateglutamatecarrier2 pages 2-4)
• Urea cycle / ammonia detoxification (ASS1 and GS-centered mechanism) (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6)
• Fatty acid beta-oxidation regulation via PPARα (hayasaka2024pathogenesisandmanagement pages 1-2)
• Glycolytic process perturbation under carbohydrate load (GAPDH-step inhibition) (hayasaka2024pathogenesisandmanagement pages 7-9)

12.3 Suggested Cellular Component annotations (evidence-cited)
• Mitochondrial inner membrane (citrin location) (holecek2023aspartateglutamatecarrier2 pages 2-4)
• Mitochondrial intermembrane space (EF-hand motifs face IMS) (holecek2023aspartateglutamatecarrier2 pages 1-2)
• Cytosol and mitochondrial matrix (MDH/AST localizations in MAS) (holecek2023aspartateglutamatecarrier2 pages 2-4)

12.4 Phenotype associations (HP; evidence-cited)
• NICCD: neonatal cholestasis resolving in infancy with diet (chuenwattana2024neonatalintrahepaticcholestasis pages 1-3)
• CTLN2: hyperammonemic encephalopathy and citrullinemia (hayasaka2024pathogenesisandmanagement pages 2-4, hayasaka2024pathogenesisandmanagement pages 4-6)
• Fatty liver/steatosis linked to PPARα downregulation (hayasaka2024pathogenesisandmanagement pages 2-4)

12.5 Cell type involvement (CL; evidence-cited)
• Hepatocytes as principal affected cells; zonated periportal vs perivenous hepatocytes relevant to ureagenesis vs glutamine synthesis; altered ASS1/GS distributions reported in CTLN2. (hayasaka2024pathogenesisandmanagement pages 4-6)

12.6 Anatomical locations (UBERON; evidence-cited)
• Liver, hepatic lobule zonation regions (periportal/perivenous), brain (encephalopathy). (hayasaka2024pathogenesisandmanagement pages 4-6, hayasaka2024pathogenesisandmanagement pages 2-4)

12.7 Chemical entities (CHEBI; evidence-cited)
• Ammonia, citrulline, aspartate, glutamate, glutamine, citrate, NAD+/NADH, ATP; MCT/MCFA as therapeutic energy substrates; fructose/glycerol as hazardous infusions. (hayasaka2024pathogenesisandmanagement pages 4-6, hayasaka2024pathogenesisandmanagement pages 7-9)

13. Evidence items (mechanism-centric; with identifiers when available)
Because the extracted 2023–2024 texts did not display PMIDs, evidence is provided with DOI/URL and the in-text direct quotes above.
• Hayasaka K. “Pathogenesis and Management of Citrin Deficiency.” Internal Medicine. Jul 2024. DOI:10.2169/internalmedicine.2595-23. URL: https://doi.org/10.2169/internalmedicine.2595-23. Key mechanistic quotes include MAS role in regenerating cytosolic NAD+; GS-centered explanation of hyperammonemia; GAPDH-step carbohydrate toxicity; PPARα/β-oxidation downregulation; MCT response statistics. (hayasaka2024pathogenesisandmanagement pages 1-2, hayasaka2024pathogenesisandmanagement pages 4-6, hayasaka2024pathogenesisandmanagement pages 7-9, hayasaka2024pathogenesisandmanagement pages 6-7)
• Holeček M. “Aspartate-glutamate carrier 2 (citrin): a role in glucose and amino acid metabolism in the liver.” BMB Reports. Jun 2023. DOI:10.5483/bmbrep.2023-0052. URL: https://doi.org/10.5483/bmbrep.2023-0052. Key quote: MAS required for intracellular redox balance/respiration/ATP; MAS component localization; AGC2 IMS-facing EF-hands. (holecek2023aspartateglutamatecarrier2 pages 1-2, holecek2023aspartateglutamatecarrier2 pages 2-4)
• Chan TCH et al. “Harnessing Next-Generation Sequencing as a Timely and Accurate Second-Tier Screening Test for Newborn Screening of Inborn Errors of Metabolism.” Int J Neonatal Screening. Mar 2024. DOI:10.3390/ijns10010019. URL: https://doi.org/10.3390/ijns10010019. Provides quantitative NBS implementation metrics for CTLN2/CD and hotspot IVS16ins3kb detection. (chan2024harnessingnextgenerationsequencing pages 1-2, chan2024harnessingnextgenerationsequencing pages 3-5, chan2024harnessingnextgenerationsequencing pages 2-3)
• Chuenwattana S et al. “NICCD in Thai infants… considerations for negative newborn screening.” Medical Reports. Apr 2024. DOI:10.1016/j.hmedic.2024.100051. URL: https://doi.org/10.1016/j.hmedic.2024.100051. Provides Thailand incidence estimate (~1:33,000), variant examples, and NBS false-negative caution. (chuenwattana2024neonatalintrahepaticcholestasis pages 1-3)
• Wang K et al. “Three novel variants on SLC25A13 in four infants with NICCD.” Front Pediatr. Mar 2023. DOI:10.3389/fped.2023.1103877. URL: https://doi.org/10.3389/fped.2023.1103877. Expands variant spectrum; provides China carrier estimate (1/65). (wang2023casereportthree pages 1-2)

14. Limitations of this report relative to the user’s requirements
• PMID requirement: Several key statements are supported by peer-reviewed review articles whose PMIDs were not included in the retrieved text excerpts; therefore, this report provides DOI/URL citations and quotes but cannot supply PMIDs for those specific sources from the available evidence. (hayasaka2024pathogenesisandmanagement pages 1-2, holecek2023aspartateglutamatecarrier2 pages 1-2)
• Primary mechanistic experiments: The 2024 review summarizes primary literature; however, in this retrieval run we did not fetch the underlying primary experimental papers themselves. Thus, mechanistic claims here are primarily review-supported rather than directly quoted from original experimental articles.

Figures supporting key mechanism
• Hayasaka 2024 Figure 2 (MAS/MCS + MCT rationale) and Figure 4 (ammonia detoxification/urea-cycle schematic) were retrieved as cropped images and can be used as visual evidence of the pathway model. (hayasaka2024pathogenesisandmanagement media 4eb23285, hayasaka2024pathogenesisandmanagement media c2a905ba)


References

1. (hayasaka2024pathogenesisandmanagement pages 1-2): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

2. (hayasaka2024pathogenesisandmanagement pages 2-4): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

3. (hayasaka2024pathogenesisandmanagement pages 7-9): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

4. (holecek2023aspartateglutamatecarrier2 pages 1-2): Milan Holeček. Aspartate-glutamate carrier 2 (citrin): a role in glucose and amino acid metabolism in the liver. BMB Reports, 56:385-391, Jun 2023. URL: https://doi.org/10.5483/bmbrep.2023-0052, doi:10.5483/bmbrep.2023-0052. This article has 5 citations and is from a peer-reviewed journal.

5. (hayasaka2024pathogenesisandmanagement media 4eb23285): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

6. (holecek2023aspartateglutamatecarrier2 pages 2-4): Milan Holeček. Aspartate-glutamate carrier 2 (citrin): a role in glucose and amino acid metabolism in the liver. BMB Reports, 56:385-391, Jun 2023. URL: https://doi.org/10.5483/bmbrep.2023-0052, doi:10.5483/bmbrep.2023-0052. This article has 5 citations and is from a peer-reviewed journal.

7. (hayasaka2024pathogenesisandmanagement pages 4-6): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

8. (hayasaka2024pathogenesisandmanagement media c2a905ba): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

9. (wang2023casereportthree pages 1-2): Kena Wang, Biao Zou, Fan Chen, Jianling Zhang, Zhihua Huang, and Sainan Shu. Case report: three novel variants on slc25a13 in four infants with neonatal intrahepatic cholestasis caused by citrin deficiency. Frontiers in Pediatrics, Mar 2023. URL: https://doi.org/10.3389/fped.2023.1103877, doi:10.3389/fped.2023.1103877. This article has 4 citations.

10. (hayasaka2024pathogenesisandmanagement pages 6-7): Kiyoshi Hayasaka. Pathogenesis and management of citrin deficiency. Internal Medicine, 63:1977-1986, Jul 2024. URL: https://doi.org/10.2169/internalmedicine.2595-23, doi:10.2169/internalmedicine.2595-23. This article has 13 citations and is from a peer-reviewed journal.

11. (chuenwattana2024neonatalintrahepaticcholestasis pages 1-3): Sirilak Chuenwattana, Kanokwan Imtawil, Kanda Sornkayasit, Aree Rattanathongkom, Busara Charoenwat, and Khunton Wichajarn. Neonatal intrahepatic cholestasis caused by citrin deficiency (niccd) in thai infants: case reports on clinical presentation, genotype analysis, and considerations for negative newborn screening. Medical Reports, 4:100051, Apr 2024. URL: https://doi.org/10.1016/j.hmedic.2024.100051, doi:10.1016/j.hmedic.2024.100051. This article has 2 citations.

12. (chan2024harnessingnextgenerationsequencing pages 3-5): Toby Chun Hei Chan, Chloe Miu Mak, Matthew Chun Wing Yeung, Eric Chun-Yiu Law, Jana Cheung, Tsz Ki Wong, Vincent Wing-Sang Cheng, Jacky Kwan Ho Lee, Jimmy Chi Lap Wong, Cheuk Wing Fung, Kiran Moti Belaramani, Anne Mei Kwun Kwok, and Kwok Yeung Tsang. Harnessing next-generation sequencing as a timely and accurate second-tier screening test for newborn screening of inborn errors of metabolism. International Journal of Neonatal Screening, 10:19, Mar 2024. URL: https://doi.org/10.3390/ijns10010019, doi:10.3390/ijns10010019. This article has 8 citations.

13. (chan2024harnessingnextgenerationsequencing pages 1-2): Toby Chun Hei Chan, Chloe Miu Mak, Matthew Chun Wing Yeung, Eric Chun-Yiu Law, Jana Cheung, Tsz Ki Wong, Vincent Wing-Sang Cheng, Jacky Kwan Ho Lee, Jimmy Chi Lap Wong, Cheuk Wing Fung, Kiran Moti Belaramani, Anne Mei Kwun Kwok, and Kwok Yeung Tsang. Harnessing next-generation sequencing as a timely and accurate second-tier screening test for newborn screening of inborn errors of metabolism. International Journal of Neonatal Screening, 10:19, Mar 2024. URL: https://doi.org/10.3390/ijns10010019, doi:10.3390/ijns10010019. This article has 8 citations.

14. (chan2024harnessingnextgenerationsequencing pages 2-3): Toby Chun Hei Chan, Chloe Miu Mak, Matthew Chun Wing Yeung, Eric Chun-Yiu Law, Jana Cheung, Tsz Ki Wong, Vincent Wing-Sang Cheng, Jacky Kwan Ho Lee, Jimmy Chi Lap Wong, Cheuk Wing Fung, Kiran Moti Belaramani, Anne Mei Kwun Kwok, and Kwok Yeung Tsang. Harnessing next-generation sequencing as a timely and accurate second-tier screening test for newborn screening of inborn errors of metabolism. International Journal of Neonatal Screening, 10:19, Mar 2024. URL: https://doi.org/10.3390/ijns10010019, doi:10.3390/ijns10010019. This article has 8 citations.

15. (chuenwattana2024neonatalintrahepaticcholestasis pages 3-5): Sirilak Chuenwattana, Kanokwan Imtawil, Kanda Sornkayasit, Aree Rattanathongkom, Busara Charoenwat, and Khunton Wichajarn. Neonatal intrahepatic cholestasis caused by citrin deficiency (niccd) in thai infants: case reports on clinical presentation, genotype analysis, and considerations for negative newborn screening. Medical Reports, 4:100051, Apr 2024. URL: https://doi.org/10.1016/j.hmedic.2024.100051, doi:10.1016/j.hmedic.2024.100051. This article has 2 citations.
