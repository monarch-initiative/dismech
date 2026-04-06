---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:04:38.756163'
end_time: '2026-02-23T23:26:11.786406'
duration_seconds: 1293.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tyrosinemia Type I
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Tyrosinemia Type I
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Tyrosinemia Type I**.
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
- **Disease Name:** Tyrosinemia Type I
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Tyrosinemia Type I**.
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


Title: Pathophysiology Research Report—Tyrosinemia Type I (HT1)

Target disease
- Disease: Tyrosinemia type I (hepatorenal tyrosinemia)
- MONDO: MONDO_0010161 (Open Targets disease mapping) ()
- Category: Genetic (autosomal recessive inborn error of metabolism)

1. Key concepts and current understanding (core definitions)

1.1 Definition and primary biochemical defect
Tyrosinemia type I (HT1/TT1) is caused by deficiency of fumarylacetoacetate hydrolase (FAH), the terminal enzyme of tyrosine catabolism, leading to accumulation of toxic intermediates. Recent newborn-screening review language is explicit that FAH deficiency “disrupts the catabolic pathway of tyrosine (Tyr). Consequently, toxic metabolites, including fumarylacetoacetate and succinylacetone (SUAC), accumulate” with major hepatic and renal consequences (published 16 Dec 2024) (kuypers2024evaluationofneonatal pages 1-2). The causative gene–disease association is strongly supported in Open Targets, where FAH is the sole top-associated target for MONDO_0010161 with multiple literature evidences ().

1.2 Pathognomonic metabolite and diagnostic concept
Succinylacetone (SA; SUAC in dried blood spots) is central to both pathophysiology and diagnostics. A 2023 Dutch newborn-screening case report states: “Elevated succinylacetone (SA) is pathognomonic for TT1 and therefore often used as marker for TT1 newborn screening (NBS)” (published 4 Dec 2023) (dijkstra2023afalsenegativenewborn pages 1-2). Kehar et al. (Feb 2024) similarly note that accumulating fumarylacetoacetate ultimately forms SA, which is “a highly sensitive and specific marker” (kehar2024decodinghepatorenaltyrosinemia pages 2-4).

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Metabolic block → accumulation of reactive/mutagenic metabolites
FAH loss causes accumulation of maleylacetoacetate (MAA) and fumarylacetoacetate (FAA), with formation of SA through alternative routes (illustrated schematically for liver tyrosine degradation and NTBC block) (neuckermans2023hereditarytyrosinemiatype media 50dfa151). Kehar et al. describe FAA as “highly reactive,” “mutagenic,” and able to cause “oxidative damage to cells by reacting with glutathione and sulfhydryl groups of proteins” (kehar2024decodinghepatorenaltyrosinemia pages 2-4). This provides a mechanistic bridge from a metabolic lesion to oxidative stress and macromolecular damage.

2.2 Hepatocellular injury: mitochondrial cytochrome c release → caspase cascade → apoptosis (primary evidence)
A landmark mechanistic study (Kubo et al., PNAS, Aug 1998; URL: https://doi.org/10.1073/pnas.95.16.9552) demonstrated that FAA can directly trigger mitochondrial apoptotic signaling. They report that in FAH-deficient mice, “Cytochrome c was released from mitochondria prior to liver failure” and that “in a cell-free system, the addition of fumarylacetoacetate induced the release of cytochrome c from the mitochondria” (kubo1998hepatocyteinjuryin pages 1-2). The same paper states “caspase inhibitors were highly effective in preventing the liver failure induced by HGA” (a precursor that generates FAA in their model) (kubo1998hepatocyteinjuryin pages 1-2). Together, these data support a causal chain: toxic tyrosine intermediates → mitochondrial outer membrane permeabilization → caspase activation → hepatocyte apoptosis.

3. Dysregulated pathways and cellular processes (beyond the metabolic block)

3.1 Persistent pro-carcinogenic liver programs even under nitisinone (NTBC)
Although nitisinone substantially prevents acute toxicity, it does not reconstitute FAH activity. Neuckermans et al. (Genes, 11 Mar 2023; URL: https://doi.org/10.3390/genes14030693) emphasize that “NTBC does not restore the enzymatic defects inflicted by the disease nor does it cure HT1” (neuckermans2023hereditarytyrosinemiatype pages 1-2). Their mouse transcriptome study found enrichment of differentially expressed genes in “toxicological gene classes related to liver disease, liver damage, liver regeneration and liver cancer, in particular HCC,” and they interpret their results as showing that “NTBC therapy does not completely resolves HT1-driven liver disease and supports the sustained risk to develop HCC over time” (neuckermans2023hereditarytyrosinemiatype pages 1-2). Visual evidence from their pathway/toxicology analyses and gene signatures under continuous NTBC is available in extracted figures/tables (neuckermans2023hereditarytyrosinemiatype media 0fafe895).

3.2 Porphyria-like crises: SA inhibition of ALAD → ALA accumulation → neurovisceral crises
HT1 includes episodic “porphyria crises with neuropathy” in modern screening reviews (kuypers2024evaluationofneonatal pages 1-2). A 2023 nitisinone-focused dissertation/review synthesizes a mechanistic explanation: SA is a competitive inhibitor of δ-aminolevulinic acid dehydratase (ALAD), causing δ-aminolevulinic acid (ALA) accumulation with downstream mitochondrial, hepatic, and neuropsychiatric toxicity and “neurological crises … similar to porphyria/lead poisoning” (rudebeck2023nitisinonetreatmentfor pages 16-21). Kehar et al. include 5-aminolevulinic acid (5-ALA) as a relevant biochemical entity in HT1 clinical workups (kehar2024decodinghepatorenaltyrosinemia pages 2-4), consistent with heme-pathway involvement.

3.3 Renal tubular dysfunction and Fanconi-like phenotype
Renal tubular dysfunction is a core multi-organ manifestation: TT1 toxic metabolites “accumulate, resulting in … renal tubular dysfunction” (kuypers2024evaluationofneonatal pages 1-2), and Dijkstra et al. list renal tubular dysfunction among classic outcomes of untreated disease (dijkstra2023afalsenegativenewborn pages 1-2). A 2024 clinical report summarizes cohort frequencies of tubulopathy-related findings (aminoaciduria, hypercalciuria, tubular acidosis, nephromegaly, nephrocalcinosis, reduced GFR), reflecting proximal tubular injury consistent with a Fanconi-like syndrome (ilyaz2024hereditarytyrosinemiatype1 pages 4-5).

4. Key molecular players (knowledge-base style)

4.1 Genes / proteins
- FAH (fumarylacetoacetate hydrolase; causal gene). Open Targets identifies FAH as the associated target for MONDO_0010161 with multiple supporting studies/literature ().
- HPD / 4-hydroxyphenylpyruvate dioxygenase (4HPPD): upstream enzyme pharmacologically inhibited by nitisinone (NTBC) to prevent formation of toxic downstream metabolites (kehar2024decodinghepatorenaltyrosinemia pages 2-4, neuckermans2023hereditarytyrosinemiatype pages 1-2).
- Caspase cascade components / mitochondrial apoptosis machinery: cytochrome c release and caspase involvement shown in FAH-deficiency injury model (kubo1998hepatocyteinjuryin pages 1-2).
- ALAD (δ-aminolevulinic acid dehydratase): inhibited by SA, linking HT1 to porphyria-like neurovisceral crises via ALA accumulation (rudebeck2023nitisinonetreatmentfor pages 16-21).

4.2 Chemical entities (metabolites, drugs, biomarkers)
- Tyrosine (substrate; elevated upstream of NTBC block)
- Fumarylacetoacetate (FAA): reactive, mutagenic; triggers oxidative damage via glutathione/protein sulfhydryls (kehar2024decodinghepatorenaltyrosinemia pages 2-4); induces cytochrome c release (kubo1998hepatocyteinjuryin pages 1-2)
- Maleylacetoacetate (MAA): upstream toxic intermediate (neuckermans2023hereditarytyrosinemiatype media 50dfa151)
- Succinylacetone (SA/SUAC): toxic and diagnostic metabolite; “pathognomonic” marker for NBS (dijkstra2023afalsenegativenewborn pages 1-2)
- δ-aminolevulinic acid (ALA/5-ALA): accumulates via ALAD inhibition in porphyria-like crises (rudebeck2023nitisinonetreatmentfor pages 16-21, kehar2024decodinghepatorenaltyrosinemia pages 2-4)
- Nitisinone (NTBC; 2-(2-nitro-4-trifluoromethylbenzoyl)-1,3-cyclohexanedione): 4HPPD inhibitor; blocks toxic metabolite formation (kehar2024decodinghepatorenaltyrosinemia pages 2-4, kuypers2024evaluationofneonatal pages 1-2)
- Alpha-fetoprotein (AFP): biomarker of metabolic derangement and HCC risk; AFP decreases after NTBC, and abnormal AFP kinetics can raise suspicion for HCC or nonadherence (kehar2024decodinghepatorenaltyrosinemia pages 2-4)

4.3 Cell types and anatomical locations
- Primary affected tissues: liver and kidney; pathophysiologic damage occurs in hepatic and renal cells (kuypers2024evaluationofneonatal pages 1-2, neuckermans2023hereditarytyrosinemiatype pages 1-2).
- Key cell types: hepatocytes (site of most severe organ pathology and carcinogenic transformation risk) (neuckermans2023hereditarytyrosinemiatype pages 1-2); renal tubular epithelial cells/proximal tubule cells (tubulopathy/Fanconi-like syndrome) (ilyaz2024hereditarytyrosinemiatype1 pages 4-5).
- Nervous system involvement: porphyria-like crises with neuropathy (kuypers2024evaluationofneonatal pages 1-2, dijkstra2023afalsenegativenewborn pages 1-2).

5. Biological processes and cellular components (GO-style narrative)

5.1 Disrupted biological processes (examples of GO terms)
- Tyrosine catabolic process (disrupted at FAH; upstream pathway blockade with NTBC) (kuypers2024evaluationofneonatal pages 1-2, kehar2024decodinghepatorenaltyrosinemia pages 2-4)
- Response to oxidative stress / glutathione metabolism and thiol-dependent redox homeostasis (FAA reacting with glutathione/protein sulfhydryls) (kehar2024decodinghepatorenaltyrosinemia pages 2-4)
- Intrinsic apoptotic signaling pathway / caspase activation (FAA-induced cytochrome c release; caspase inhibitors protective) (kubo1998hepatocyteinjuryin pages 1-2)
- Heme biosynthetic process (functional inhibition via SA→ALAD inhibition; porphyria-like crises through ALA accumulation) (rudebeck2023nitisinonetreatmentfor pages 16-21)
- Renal tubular transport (renal tubular dysfunction; Fanconi-like phenotype) (kuypers2024evaluationofneonatal pages 1-2, ilyaz2024hereditarytyrosinemiatype1 pages 4-5)
- Liver regeneration and carcinogenesis programs (persistent enrichment of liver-damage/regeneration/cancer gene classes under NTBC in murine model) (neuckermans2023hereditarytyrosinemiatype pages 1-2, neuckermans2023hereditarytyrosinemiatype media 0fafe895)

5.2 Cellular components (examples of GO CC)
- Cytosol (accumulation of intermediates and cytochrome c release measured in cytosolic fractions) (kubo1998hepatocyteinjuryin pages 2-4)
- Mitochondrial intermembrane space/outer membrane (cytochrome c release as key event) (kubo1998hepatocyteinjuryin pages 1-2)
- Hepatocyte cytosol (tyrosine catabolism described as present in liver cytosol) (neuckermans2023hereditarytyrosinemiatype pages 1-2)

6. Disease progression (sequence of events)

6.1 Initiation (genetic trigger)
Biallelic pathogenic variants in FAH cause FAH deficiency (kehar2024decodinghepatorenaltyrosinemia pages 2-4), blocking the terminal step of tyrosine catabolism.

6.2 Early biochemical stage
Toxic intermediates accumulate (FAA/MAA) and SA is formed/accumulates early in blood and urine; Kehar et al. note that “Marked SA elevation occurs early in blood and urine” (kehar2024decodinghepatorenaltyrosinemia pages 2-4). This biochemical stage underpins newborn screening and early confirmatory testing.

6.3 Cellular injury and organ dysfunction
- Liver: FAA-driven oxidative stress and mitochondrial apoptosis contribute to acute hepatic decompensation, progressive liver damage, and predisposition to malignant transformation (kehar2024decodinghepatorenaltyrosinemia pages 2-4, kubo1998hepatocyteinjuryin pages 1-2).
- Kidney: renal tubular dysfunction develops, manifesting as tubulopathy/Fanconi-like syndrome and rickets in many patients (kuypers2024evaluationofneonatal pages 1-2, ilyaz2024hereditarytyrosinemiatype1 pages 4-5).
- Nervous system: metabolic decompensation can trigger porphyria-like neurovisceral crises via heme-pathway disruption (kuypers2024evaluationofneonatal pages 1-2, rudebeck2023nitisinonetreatmentfor pages 16-21).

6.4 Chronic stage and malignancy risk
HT1 carries prominent risk for hepatocellular carcinoma (HCC); even under continuous NTBC, transcriptomic signals associated with liver cancer can persist in model systems (neuckermans2023hereditarytyrosinemiatype pages 1-2, neuckermans2023hereditarytyrosinemiatype media 0fafe895).

7. Phenotypic manifestations (mechanism-linked)

Key clinical phenotypes noted in recent screening and management literature include:
- Hepatic: acute liver failure, fibrosis, cirrhosis, hepatocellular carcinoma and hepatoblastoma (kuypers2024evaluationofneonatal pages 1-2, dijkstra2023afalsenegativenewborn pages 1-2)
- Renal: renal tubular dysfunction with downstream growth/bone disease (rickets) (kuypers2024evaluationofneonatal pages 1-2, ilyaz2024hereditarytyrosinemiatype1 pages 4-5)
- Neurologic: porphyria crises with neuropathy; neurocognitive impairment risk highlighted in management review (kuypers2024evaluationofneonatal pages 1-2, kehar2024decodinghepatorenaltyrosinemia pages 1-2)
Mechanistic mapping: FAA reactivity and apoptotic signaling align with liver failure/cirrhosis; SA-mediated ALAD inhibition aligns with porphyria-like crises; renal tubular injury aligns with Fanconi-like findings and rickets (kehar2024decodinghepatorenaltyrosinemia pages 2-4, kubo1998hepatocyteinjuryin pages 1-2, rudebeck2023nitisinonetreatmentfor pages 16-21, ilyaz2024hereditarytyrosinemiatype1 pages 4-5).

8. Recent developments and latest research (prioritizing 2023–2024)

8.1 Newborn screening optimization (2023–2024)
A 2024 worldwide evaluation of NBS programs reported that “TT1 incidence ranged from 1/13,636 to 1/750,000,” with most programs using DBS SUAC (78.9%) and a “pooled median cut-off for SUAC … 1.50 µmol/L (range 0.3–7.0 µmol/L)” (published 16 Dec 2024; URL: https://doi.org/10.3390/ijns10040082) (kuypers2024evaluationofneonatal pages 1-2). In the same report, overall positive predictive values were “27.3% for SUAC” and “90.1% for Tyr + SUAC,” and false negatives were reported for both SUAC and Tyr-based strategies (kuypers2024evaluationofneonatal pages 1-2).
A 2023 Dutch report provides real-world evidence that SUAC-based screening can be falsely negative near cut-off thresholds (SUAC 1.08 µmol/L vs Dutch cut-off 1.20 µmol/L), reinforcing the need for protocol re-evaluation (published 4 Dec 2023; URL: https://doi.org/10.3390/ijns9040066) (dijkstra2023afalsenegativenewborn pages 1-2).

8.2 Persistent residual disease biology under NTBC (2023)
Neuckermans et al. (published 11 Mar 2023) used transcriptomics in Fah/Hgd-deficient mice to identify that NTBC does not fully normalize liver disease programs and identified a 25-gene set related to liver disease and HCC development that differs between HT1 and a reference tyrosine disorder (AKU) under NTBC (neuckermans2023hereditarytyrosinemiatype pages 1-2). Extracted pathway/toxicology figures provide visual support for these claims (neuckermans2023hereditarytyrosinemiatype media 0fafe895).

9. Current applications and real-world implementation

9.1 Standard-of-care therapy: NTBC + diet
Kehar et al. describe NTBC as a “potent inhibitor” of 4-hydroxyphenylpyruvate dioxygenase (second enzyme in tyrosine degradation) and state that it “prevents the formation of toxic metabolites” with “greater than 90% survival rate” when combined with dietary therapy (kehar2024decodinghepatorenaltyrosinemia pages 2-4). Their extracted figure/table includes dietary therapy targets (tyrosine and phenylalanine ranges) used in practice (kehar2024decodinghepatorenaltyrosinemia media e8fe4339).

9.2 Monitoring for cancer risk
AFP kinetics are used clinically for both metabolic control and HCC suspicion: AFP should fall after NTBC; abnormal decline or rising AFP suggests HCC or poor adherence (kehar2024decodinghepatorenaltyrosinemia pages 2-4).

9.3 Liver transplantation
Liver transplantation is described as curative for HT1 liver disease but does not correct renal FAH deficiency; Kehar et al. note that post-transplant “LT does not correct renal FAH deficiency, and residual SA production by the kidney remains” (kehar2024decodinghepatorenaltyrosinemia pages 2-4). Indications include acute liver failure, HCC/dysplastic nodules, or failure of medical management (kehar2024decodinghepatorenaltyrosinemia pages 1-2).

10. Relevant statistics and data (recent)

- Global incidence: ~1 in 100,000 newborns worldwide (reported in 2023 review) (neuckermans2023hereditarytyrosinemiatype pages 1-2).
- NBS survey incidence range: 1/13,636 to 1/750,000 (2024 worldwide survey) (kuypers2024evaluationofneonatal pages 1-2).
- Screening cut-offs (SUAC): pooled median 1.50 µmol/L (range 0.3–7.0 µmol/L) (kuypers2024evaluationofneonatal pages 1-2).
- Screening performance: PPV 27.3% for SUAC vs 90.1% for Tyr+SUAC (kuypers2024evaluationofneonatal pages 1-2).
- Clinical outcomes with early NTBC: Quebec cohort example—mortality 36% in non-NTBC-treated children (10/28) vs 0 deaths among children receiving NTBC before 1 month; none of early-treated Quebec cases developed HCC (Kehar 2024; publication Feb 2024; URL: https://doi.org/10.3138/canlivj-2023-0018) (kehar2024decodinghepatorenaltyrosinemia pages 2-4).

11. Expert opinions / authoritative analysis (interpretive synthesis)

- Early detection + early NTBC is the major modifiable determinant of outcome: Kehar et al. explicitly frame this as “EARLY DIAGNOSIS AND THERAPY SAVES LIVES” and link pre-symptomatic NTBC to improved outcomes and reduced transplant need (kehar2024decodinghepatorenaltyrosinemia pages 2-4).
- Residual long-term risk (especially HCC) remains a key unmet need: both clinical reviews and transcriptomic models support continued surveillance, because NTBC blocks toxic metabolite formation but does not restore FAH function and does not fully normalize liver disease biology (neuckermans2023hereditarytyrosinemiatype pages 1-2, kehar2024decodinghepatorenaltyrosinemia pages 2-4).

12. Knowledge-base-ready annotation blocks

12.1 Pathophysiology description (narrative)
HT1 results from FAH deficiency, causing accumulation of reactive tyrosine-catabolic intermediates (notably FAA/MAA) and formation of SA. FAA is described as mutagenic and capable of oxidative damage via glutathione/protein thiol reactions, and primary evidence indicates FAA can directly induce mitochondrial cytochrome c release, activating caspase-dependent apoptosis in hepatocytes. SA contributes to systemic manifestations and is pathognomonic diagnostically; mechanistically, SA inhibits ALAD, leading to ALA accumulation and porphyria-like neurovisceral crises. Chronic liver injury and regeneration pressures create a high risk for hepatocellular carcinoma; emerging 2023 transcriptomic evidence suggests that even under continuous NTBC, residual dysregulation of liver-disease and HCC-related gene programs persists, aligning with the need for long-term surveillance.

12.2 Gene/protein annotations (HGNC; selected GO suggestions)
- FAH (HGNC:3375): causal gene for HT1/TT1 (MONDO_0010161). GO suggestions: tyrosine catabolic process; cellular detoxification; response to oxidative stress (kuypers2024evaluationofneonatal pages 1-2).
- HPD/4HPPD: pharmacologic target of nitisinone; GO: tyrosine catabolic process (kehar2024decodinghepatorenaltyrosinemia pages 2-4).
- ALAD: inhibited by SA; GO: heme biosynthetic process; porphobilinogen synthase activity (rudebeck2023nitisinonetreatmentfor pages 16-21).
- Apoptosis effectors (cytochrome c release; caspase cascade): GO: intrinsic apoptotic signaling; mitochondrial outer membrane permeabilization (kubo1998hepatocyteinjuryin pages 1-2).

12.3 Phenotype associations (HPO term names)
- Liver failure; liver fibrosis; cirrhosis; hepatocellular carcinoma; hepatoblastoma; elevated AFP (kuypers2024evaluationofneonatal pages 1-2, dijkstra2023afalsenegativenewborn pages 1-2, kehar2024decodinghepatorenaltyrosinemia pages 2-4)
- Renal tubular dysfunction; Fanconi syndrome-like tubulopathy; rickets; nephrocalcinosis; reduced GFR (kuypers2024evaluationofneonatal pages 1-2, ilyaz2024hereditarytyrosinemiatype1 pages 4-5)
- Porphyria-like crises; neuropathy; neurocognitive impairment (kuypers2024evaluationofneonatal pages 1-2, rudebeck2023nitisinonetreatmentfor pages 16-21, kehar2024decodinghepatorenaltyrosinemia pages 1-2)

12.4 Cell types (CL term names)
- Hepatocyte (primary site of injury and carcinogenesis) (neuckermans2023hereditarytyrosinemiatype pages 1-2)
- Renal proximal tubule epithelial cell (tubulopathy/Fanconi-like syndrome) (ilyaz2024hereditarytyrosinemiatype1 pages 4-5)

12.5 Anatomical locations (UBERON term names)
- Liver; kidney; nervous system (neuropathy crises) (kuypers2024evaluationofneonatal pages 1-2, dijkstra2023afalsenegativenewborn pages 1-2)

12.6 Chemicals (CHEBI names)
- Tyrosine; fumarylacetoacetate; maleylacetoacetate; succinylacetone; δ-aminolevulinic acid; nitisinone (kuypers2024evaluationofneonatal pages 1-2, kehar2024decodinghepatorenaltyrosinemia pages 2-4, rudebeck2023nitisinonetreatmentfor pages 16-21)

13. Evidence items with PMIDs (where available in retrieved full text)
- Kubo et al. PNAS 1998 (Hepatocyte injury … induced by fumarylacetoacetate … inhibited by caspase inhibitors). PMID not present in extracted text; DOI provided: 10.1073/pnas.95.16.9552 (kubo1998hepatocyteinjuryin pages 1-2).

Note on PMID coverage: Several 2023–2024 open-access clinical/review sources used here (MDPI journals; Canadian Liver Journal) and the dissertation-style text excerpts did not display PMIDs in the extracted full text. Where PMIDs were not retrievable from the provided content, DOI/URL and publication date are provided, and mechanistic claims are tied to direct quotations from the accessible text.

Key URLs (recent prioritized)
- Kuypers et al., “Evaluation of Neonatal Screening Programs for Tyrosinemia Type 1 Worldwide” (Published 16 Dec 2024): https://doi.org/10.3390/ijns10040082 (kuypers2024evaluationofneonatal pages 1-2)
- Kehar et al., “Decoding hepatorenal tyrosinemia type 1 …” (Feb 2024): https://doi.org/10.3138/canlivj-2023-0018 (kehar2024decodinghepatorenaltyrosinemia pages 2-4)
- Dijkstra et al., “A False-Negative Newborn Screen for Tyrosinemia Type 1 …” (Published 4 Dec 2023): https://doi.org/10.3390/ijns9040066 (dijkstra2023afalsenegativenewborn pages 1-2)
- Neuckermans et al., “Hereditary Tyrosinemia Type 1 Mice under Continuous Nitisinone Treatment …” (Published 11 Mar 2023): https://doi.org/10.3390/genes14030693 (neuckermans2023hereditarytyrosinemiatype pages 1-2)
- Kubo et al., PNAS (Aug 1998): https://doi.org/10.1073/pnas.95.16.9552 (kubo1998hepatocyteinjuryin pages 1-2)


References

1. (kuypers2024evaluationofneonatal pages 1-2): Allysa M. Kuypers, Marelle J. Bouva, J. Gerard Loeber, Anita Boelen, Eugenie Dekkers, Konstantinos Petritis, C. Austin Pickens, Francjan J. van Spronsen, and M. Rebecca Heiner-Fokkema. Evaluation of neonatal screening programs for tyrosinemia type 1 worldwide. International Journal of Neonatal Screening, 10:82, Dec 2024. URL: https://doi.org/10.3390/ijns10040082, doi:10.3390/ijns10040082. This article has 4 citations.

2. (dijkstra2023afalsenegativenewborn pages 1-2): Allysa M. Dijkstra, Kimber Evers-van Vliet, M. Rebecca Heiner-Fokkema, Frank A. J. A. Bodewes, Dennis K. Bos, József Zsiros, Koen J. van Aerde, Klaas Koop, Francjan J. van Spronsen, and Charlotte M. A. Lubout. A false-negative newborn screen for tyrosinemia type 1—need for re-evaluation of newborn screening with succinylacetone. International Journal of Neonatal Screening, 9:66, Dec 2023. URL: https://doi.org/10.3390/ijns9040066, doi:10.3390/ijns9040066. This article has 14 citations.

3. (kehar2024decodinghepatorenaltyrosinemia pages 2-4): Mohit Kehar, Moinak Sen Sarma, Jayendra Seetharaman, Carolina Jimenez Rivera, and Pranesh Chakraborty. Decoding hepatorenal tyrosinemia type 1: unraveling the impact of early detection, ntbc, and the role of liver transplantation. Canadian Liver Journal, 7:54-63, Feb 2024. URL: https://doi.org/10.3138/canlivj-2023-0018, doi:10.3138/canlivj-2023-0018. This article has 5 citations.

4. (neuckermans2023hereditarytyrosinemiatype media 50dfa151): Jessie Neuckermans, Sien Lequeue, Paul Claes, Anja Heymans, Juliette H. Hughes, Haaike Colemonts-Vroninks, Lionel Marcélis, Georges Casimir, Philippe Goyens, Geert A. Martens, James A. Gallagher, Tamara Vanhaecke, George Bou-Gharios, and Joery De Kock. Hereditary tyrosinemia type 1 mice under continuous nitisinone treatment display remnants of an uncorrected liver disease phenotype. Genes, 14:693, Mar 2023. URL: https://doi.org/10.3390/genes14030693, doi:10.3390/genes14030693. This article has 6 citations.

5. (kubo1998hepatocyteinjuryin pages 1-2): Shuji Kubo, Maosen Sun, Michio Miyahara, Kazuhiro Umeyama, Ken-ichi Urakami, Tetsuro Yamamoto, Cornelis Jakobs, Ichiro Matsuda, and Fumio Endo. Hepatocyte injury in tyrosinemia type 1 is induced by fumarylacetoacetate and is inhibited by caspase inhibitors. Proceedings of the National Academy of Sciences of the United States of America, 95 16:9552-7, Aug 1998. URL: https://doi.org/10.1073/pnas.95.16.9552, doi:10.1073/pnas.95.16.9552. This article has 102 citations and is from a highest quality peer-reviewed journal.

6. (neuckermans2023hereditarytyrosinemiatype pages 1-2): Jessie Neuckermans, Sien Lequeue, Paul Claes, Anja Heymans, Juliette H. Hughes, Haaike Colemonts-Vroninks, Lionel Marcélis, Georges Casimir, Philippe Goyens, Geert A. Martens, James A. Gallagher, Tamara Vanhaecke, George Bou-Gharios, and Joery De Kock. Hereditary tyrosinemia type 1 mice under continuous nitisinone treatment display remnants of an uncorrected liver disease phenotype. Genes, 14:693, Mar 2023. URL: https://doi.org/10.3390/genes14030693, doi:10.3390/genes14030693. This article has 6 citations.

7. (neuckermans2023hereditarytyrosinemiatype media 0fafe895): Jessie Neuckermans, Sien Lequeue, Paul Claes, Anja Heymans, Juliette H. Hughes, Haaike Colemonts-Vroninks, Lionel Marcélis, Georges Casimir, Philippe Goyens, Geert A. Martens, James A. Gallagher, Tamara Vanhaecke, George Bou-Gharios, and Joery De Kock. Hereditary tyrosinemia type 1 mice under continuous nitisinone treatment display remnants of an uncorrected liver disease phenotype. Genes, 14:693, Mar 2023. URL: https://doi.org/10.3390/genes14030693, doi:10.3390/genes14030693. This article has 6 citations.

8. (rudebeck2023nitisinonetreatmentfor pages 16-21): M Rudebeck. Nitisinone treatment for inherited disorders of tyrosine metabolism–investigating long-term outcomes, optimal monitoring, and new treatment options and indications. Unknown journal, 2023.

9. (ilyaz2024hereditarytyrosinemiatype1 pages 4-5): Md Ilyaz, Renuka S Jadhav, Vineeta Pande, Shailaja V Mane, and Pranavi Mokkarala. Hereditary tyrosinemia type-1 with late presentation: a case report. Cureus, Jun 2024. URL: https://doi.org/10.7759/cureus.62990, doi:10.7759/cureus.62990. This article has 3 citations.

10. (kubo1998hepatocyteinjuryin pages 2-4): Shuji Kubo, Maosen Sun, Michio Miyahara, Kazuhiro Umeyama, Ken-ichi Urakami, Tetsuro Yamamoto, Cornelis Jakobs, Ichiro Matsuda, and Fumio Endo. Hepatocyte injury in tyrosinemia type 1 is induced by fumarylacetoacetate and is inhibited by caspase inhibitors. Proceedings of the National Academy of Sciences of the United States of America, 95 16:9552-7, Aug 1998. URL: https://doi.org/10.1073/pnas.95.16.9552, doi:10.1073/pnas.95.16.9552. This article has 102 citations and is from a highest quality peer-reviewed journal.

11. (kehar2024decodinghepatorenaltyrosinemia pages 1-2): Mohit Kehar, Moinak Sen Sarma, Jayendra Seetharaman, Carolina Jimenez Rivera, and Pranesh Chakraborty. Decoding hepatorenal tyrosinemia type 1: unraveling the impact of early detection, ntbc, and the role of liver transplantation. Canadian Liver Journal, 7:54-63, Feb 2024. URL: https://doi.org/10.3138/canlivj-2023-0018, doi:10.3138/canlivj-2023-0018. This article has 5 citations.

12. (kehar2024decodinghepatorenaltyrosinemia media e8fe4339): Mohit Kehar, Moinak Sen Sarma, Jayendra Seetharaman, Carolina Jimenez Rivera, and Pranesh Chakraborty. Decoding hepatorenal tyrosinemia type 1: unraveling the impact of early detection, ntbc, and the role of liver transplantation. Canadian Liver Journal, 7:54-63, Feb 2024. URL: https://doi.org/10.3138/canlivj-2023-0018, doi:10.3138/canlivj-2023-0018. This article has 5 citations.
