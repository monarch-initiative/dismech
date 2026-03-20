---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T22:58:40.117390'
end_time: '2026-02-23T23:16:26.883357'
duration_seconds: 1066.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ornithine Carbamoyltransferase Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ornithine Carbamoyltransferase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ornithine Carbamoyltransferase Deficiency**.
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
- **Disease Name:** Ornithine Carbamoyltransferase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ornithine Carbamoyltransferase Deficiency**.
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


Title: Pathophysiology Research Report — Ornithine Carbamoyltransferase (Ornithine Transcarbamylase) Deficiency (OTCD)

Publication focus: molecular/cellular mechanisms, disease progression, and current translational landscape (prioritizing 2023–2024 where available)

Target Disease
- Disease name: Ornithine carbamoyltransferase deficiency / Ornithine transcarbamylase deficiency (OTCD)
- Category: Genetic; inborn error of metabolism; urea cycle disorder; X-linked
- MONDO ID: Not found in the retrieved full-text and registry excerpts used for this report; therefore cannot be asserted with evidence here. (OpenTargets Search: Ornithine carbamoyltransferase deficiency,Ornithine transcarbamylase deficiency-OTC, NCT05345171 chunk 2)
- Cross-references supported by retrieved sources:
  - OMIM/MIM: 311250 (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)
  - MeSH: D020163 (“Ornithine Carbamoyltransferase Deficiency Disease”, ClinicalTrials.gov records) (NCT05345171 chunk 2, NCT03767270 chunk 1)
  - Open Targets disease ID in retrieved evidence: EFO_0007409 (OpenTargets Search: Ornithine carbamoyltransferase deficiency,Ornithine transcarbamylase deficiency-OTC)

1. Key Concepts and Current Core Understanding (definitions + canonical mechanism)

1.1 Core biochemical defect (urea cycle)
OTCD is caused by deleterious variants in the X-linked OTC gene, encoding ornithine transcarbamylase, a nuclear-encoded mitochondrial enzyme highly expressed in hepatocytes. OTC catalyzes the urea-cycle reaction combining carbamoyl phosphate and ornithine to generate citrulline, a step essential for hepatic conversion of neurotoxic ammonia into urea. (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)

A concise definition from a 2023 high-quality genetics paper: “OTC is a nuclear-encoded mitochondrial protein that converts ornithine and carbamoyl phosphate to citrulline in human liver cells.” (lo2023thefunctionalimpact pages 1-3)

1.2 Compartmentalization (mitochondria–cytosol coupling)
The proximal urea-cycle steps (including CPS1 and OTC) occur in mitochondria, while downstream arginine synthesis steps proceed in the cytosol; transporters move intermediates across mitochondrial membranes. This mitochondria↔cytosol coordination is central to OTCD pathophysiology because disruption at the mitochondrial OTC step blocks flux into cytosolic ureagenesis. (matsumoto2019ureacycledisorders—update pages 4-5, hu2024indepthanalysisof pages 4-7)

1.3 Core toxic driver: hyperammonemia
Loss of hepatic urea-cycle capacity leads to accumulation of nitrogen as ammonia (hyperammonemia), which is neurotoxic and drives acute encephalopathy, cerebral edema, seizures, coma, and death if not rapidly treated. (lo2023thefunctionalimpact pages 1-3)

2. Core Pathophysiology (molecular pathways dysregulated; cellular processes affected)

2.1 Dysregulated metabolic pathways
A. Ureagenesis failure / nitrogen disposal blockade
OTCD blocks ureagenesis at the mitochondrial OTC step, producing systemic hyperammonemia. (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)

B. Amino-acid nitrogen buffering shifts
With impaired urea-cycle flux, nitrogen is shifted into amino-acid pools, especially glutamine (and often alanine), producing a characteristic biochemical signature used diagnostically and monitored therapeutically. (ribas2022hyperammonemiaininherited pages 5-6, matsumoto2019ureacycledisorders—update pages 4-5)

C. Secondary orotic aciduria (biomarker)
Urinary orotic acid is characteristically elevated in OTCD and can help distinguish OTCD from CPS1 deficiency (which tends not to elevate orotic acid). (nambiar2022acutefulminantencephalopathy pages 3-4, matsumoto2019ureacycledisorders—update pages 4-5)

A 2024 mechanistic pediatric report also explicitly links OTC block to downstream metabolite consequences: “accumulation of carbamoyl phosphate and glutamine and activation of the pyrimidine pathway with increased orotic acid excretion.” (hu2024indepthanalysisof pages 1-2)

Note: Many sources describe orotic aciduria as a key marker of OTCD; within the retrieved excerpts, explicit mechanistic narration of carbamoyl-phosphate diversion into cytosolic pyrimidine synthesis is present in Hu 2024 (hu2024indepthanalysisof pages 1-2) but is not explicitly spelled out in some other classic UCD summaries (matsumoto2019ureacycledisorders—update pages 4-5).

2.2 Cellular and neurobiological injury mechanisms (ammonia → astrocyte-centered brain injury)
A. Astrocytic ammonia detoxification and glutamine-driven osmotic stress
The brain cannot convert NH4+ to urea and relies on astrocytic glutamine synthetase to detoxify ammonia into glutamine. Hyperammonemia therefore causes “toxic effects exerted by ammonia on the astrocytes” and increased brain glutamine (“glutaminosis”). (ribas2022hyperammonemiaininherited pages 1-2, zielinska2022dysregulationofastrocytic pages 1-2)

B. Astrocyte swelling → cerebral edema → intracranial hypertension
A clinically actionable sequence summarized in an intensivist-oriented review: ammonia crosses the BBB, is converted to glutamine, and glutamine (a major intracellular osmole) accumulates in astrocytes causing swelling, then “brain swelling, intracranial hypertension, coma, cerebral herniation … and death.” (redant2021managementoflate pages 1-3)

C. Mitochondrial dysfunction, oxidative/nitrosative stress, excitotoxicity
A 2022 mechanistic review compiles evidence that ammonia toxicity includes mitochondrial impairment (e.g., TCA enzyme inhibition, permeability transition pore opening), oxidative stress, and glutamatergic/NMDA-mediated excitotoxicity, contributing to neuronal injury and apoptosis. (ribas2022hyperammonemiaininherited pages 2-4, ribas2022hyperammonemiaininherited pages 1-2)

D. Glutamine transport dysregulation as an amplifier of edema/injury
A 2022 neuroscience review emphasizes that brain glutamine synthesis is “the only route of ammonia detoxification” and that hyperammonemia is “as a rule associated with increased brain glutamine content,” which contributes to edema; it highlights astrocytic glutamine transporters (SNAT3/SLC38A3; y+LAT2/SLC7A6) as modulators linking glutaminosis, mitochondrial dysfunction, and oxidative/nitrosative stress (the “Trojan Horse” hypothesis). (zielinska2022dysregulationofastrocytic pages 1-2)

3. Key Molecular Players (genes/proteins, metabolites, cell types, anatomy)

3.1 Genes / proteins
- OTC (HGNC symbol: OTC; enzyme EC 2.1.3.3): mitochondrial enzyme catalyzing carbamoyl phosphate + ornithine → citrulline; X-linked. (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)
- CPS1 (carbamoyl phosphate synthetase 1): upstream mitochondrial enzyme forming carbamoyl phosphate from ammonia + bicarbonate. (ribas2022hyperammonemiaininherited pages 1-2, matsumoto2019ureacycledisorders—update pages 4-5)
- ASS1, ASL, ARG1: downstream cytosolic urea-cycle enzymes that process citrulline to arginine and ultimately urea (pathway context relevant to blocked flux in OTCD). (ribas2022hyperammonemiaininherited pages 1-2)
- Astrocyte glutamine synthetase (GS/GLUL): principal brain ammonia detoxification route generating glutamine. (ribas2022hyperammonemiaininherited pages 1-2, zielinska2022dysregulationofastrocytic pages 1-2)

3.2 Chemical entities / metabolites (diagnostic + mechanistic)
- Ammonia / ammonium (CHEBI: ammonia CHEBI:16134; ammonium CHEBI:28938): central neurotoxin and acute crisis biomarker. (ribas2022hyperammonemiaininherited pages 1-2, lo2023thefunctionalimpact pages 1-3)
- Ornithine (CHEBI:15729): urea-cycle substrate; may be altered in UCD contexts. (nambiar2022acutefulminantencephalopathy pages 3-4)
- Carbamoyl phosphate (CHEBI:17674): mitochondrial urea-cycle intermediate upstream of OTC reaction; can accumulate when OTC is deficient (explicitly stated in Hu 2024). (hu2024indepthanalysisof pages 1-2)
- Citrulline (CHEBI:16349): product of OTC reaction; typically low in OTCD and used diagnostically (but has limitations in newborn screening). (lo2023thefunctionalimpact pages 1-3, matsumoto2019ureacycledisorders—update pages 4-5)
- Arginine (CHEBI:29016): often low in OTCD biochemical profiles and supplemented therapeutically. (ribas2022hyperammonemiaininherited pages 5-6, matsumoto2019ureacycledisorders—update pages 11-12)
- Glutamine (CHEBI:28300): nitrogen buffer; elevated in blood and brain; mechanistically linked to astrocyte swelling and used as a monitoring target. (matsumoto2019ureacycledisorders—update pages 4-5, takanashi2002distinctlyabnormalbrain pages 1-2)
- Alanine (CHEBI:16449): often elevated in OTCD/UCD biochemical patterns. (ribas2022hyperammonemiaininherited pages 5-6, matsumoto2019ureacycledisorders—update pages 4-5)
- Orotic acid / orotate (CHEBI:30845): elevated urinary biomarker; helps differentiate OTCD from CPS1 deficiency. (nambiar2022acutefulminantencephalopathy pages 3-4, matsumoto2019ureacycledisorders—update pages 4-5)
- Uracil (CHEBI:17568): may be elevated in urine organic acids in OTCD cohorts. (tran2024apreliminaryretrospective pages 2-4)

3.3 Cell types primarily implicated
- Hepatocytes (CL:0000182): dominant site of OTC expression and ureagenesis; hepatic failure of ammonia detoxification drives systemic hyperammonemia. (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)
- Astrocytes (CL:0000127): key brain cell detoxifying ammonia via glutamine synthetase; central to edema pathogenesis. (ribas2022hyperammonemiaininherited pages 1-2, zielinska2022dysregulationofastrocytic pages 1-2)
- Neurons (CL:0000540): downstream victims of metabolic/oxidative/excitotoxic injury; involved in glutamine–glutamate neurotransmitter cycling. (zielinska2022dysregulationofastrocytic pages 1-2)

3.4 Anatomical locations
- Liver (UBERON:0002107): primary organ for urea cycle/ammonia detoxification. (yilmaz2023genetictherapyapproaches pages 1-2)
- Brain (UBERON:0000955), including cerebral cortex (UBERON:0000956) and white matter regions assessed by MRS in OTCD. (takanashi2002distinctlyabnormalbrain pages 1-2)

3.5 Cellular components
- Mitochondrial matrix (GO:0005759): CPS1 and OTC proximal urea-cycle steps occur here. (matsumoto2019ureacycledisorders—update pages 4-5)
- Cytosol (GO:0005829): downstream urea-cycle steps (e.g., ASS1) proceed here. (matsumoto2019ureacycledisorders—update pages 4-5)
- Astrocyte plasma membrane: relevant for glutamine transporters implicated in edema (SLC38A3/SNAT3 and SLC7A6/y+LAT2). (zielinska2022dysregulationofastrocytic pages 1-2)

4. Biological Processes for GO-style annotation (disrupted processes)

Candidate disrupted GO biological processes (representative):
- Urea cycle / ureagenesis (e.g., “urea cycle” GO:0000050) and nitrogen compound metabolic process (GO:0006807): reduced flux due to OTC deficiency. (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)
- Ammonia assimilation / detoxification via glutamine biosynthesis (e.g., “glutamine biosynthetic process” GO:0006541): increased in astrocytes under hyperammonemia. (ribas2022hyperammonemiaininherited pages 1-2)
- Amino acid transport (including glutamine transport): dysregulated astrocytic transporter function contributing to glutaminosis and edema. (zielinska2022dysregulationofastrocytic pages 1-2)
- Response to oxidative stress (GO:0006979) and mitochondrial dysfunction-related pathways: implicated in ammonia toxicity. (ribas2022hyperammonemiaininherited pages 2-4)
- Neurotransmitter metabolic process (GO:0042133) and glutamate/GABA cycling: affected via altered glutamine–glutamate cycling. (zielinska2022dysregulationofastrocytic pages 1-2)

5. Disease Progression (sequence from molecular defect to clinical manifestation)

5.1 Stages / phenotypic strata
A. Severe neonatal-onset OTCD
Neonatal OTCD often presents in full-term infants at 24–48 hours with progressive lethargy, hypothermia, apnea, and very high plasma ammonia. (takanashi2002distinctlyabnormalbrain pages 1-2)
In a 2024 pediatric cohort, early-onset male cases (1–7 days) could progress “to seizures and coma within 1–2 days” and death within 10 days despite treatment. (yuan2024clinicalcharacteristicsand pages 2-3)

B. Late-onset OTCD (childhood–adult; often heterozygous females)
Late-onset OTCD can present at any age with vomiting, altered mental status, ataxia, seizures, and developmental delay. (takanashi2002distinctlyabnormalbrain pages 1-2)
A 2024 referral-center study operationally defined late-onset as presentation after 30 days, emphasizing heterogeneity and that some late-onset individuals can have episodic or even initially normal ammonia with suggestive urine organic acids and family history. (tran2024apreliminaryretrospective pages 2-4)

5.2 Triggered decompensation (catabolic stress model)
Late-onset hyperammonemic crises are frequently precipitated by metabolic stressors such as high protein intake, fasting, surgery, infection, certain drugs (e.g., valproate), pregnancy/puerperium, and other physiologic stress. (lo2023thefunctionalimpact pages 1-3, redant2021managementoflate pages 1-3)

5.3 Mechanistic cascade to neurologic injury
A high-level mechanistic sequence:
1) Urea-cycle block → hyperammonemia (systemic). (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3)
2) Ammonia crosses BBB; astrocytes detoxify ammonia to glutamine. (redant2021managementoflate pages 1-3)
3) Intracellular glutamine accumulation drives astrocyte swelling (cytotoxic edema), contributing to cerebral edema and intracranial hypertension. (redant2021managementoflate pages 1-3)
4) Secondary injury pathways include mitochondrial dysfunction/oxidative stress and neurotransmitter disturbances, worsening encephalopathy and promoting seizures/coma. (ribas2022hyperammonemiaininherited pages 2-4, hu2024indepthanalysisof pages 1-2)

5.4 Neurochemical progression (OTCD-specific MRS evidence)
Quantitative 1H-MRS in late-onset OTCD shows patterns that correlate with clinical stage, including increased glutamine+glutamate (Glx) that “progressed in proportion to the clinical stage,” depletion of myo-inositol in symptomatic patients, and decreased choline in severe patients; metabolites normalized after liver transplantation in one patient. (takanashi2002distinctlyabnormalbrain pages 1-2)

6. Phenotypic Manifestations (clinical phenotypes and mechanistic linkage)

6.1 Core phenotypes
- Hyperammonemic encephalopathy with vomiting, lethargy, altered mental status, behavioral abnormalities, seizures, coma, and death. (lo2023thefunctionalimpact pages 1-3, takanashi2002distinctlyabnormalbrain pages 1-2)
- Cerebral edema / intracranial hypertension, mechanistically linked to astrocyte glutamine accumulation and swelling. (redant2021managementoflate pages 1-3)
- Neurodevelopmental impairment and neurologic sequelae in survivors of severe episodes. (yilmaz2023genetictherapyapproaches pages 1-2, takanashi2002distinctlyabnormalbrain pages 1-2)

6.2 Example phenotype terms (HPO-style; representative)
(IDs included as knowledge-base candidates; clinical details supported by cited sources)
- HP:0002181 (Cerebral edema) (supported conceptually by cerebral edema descriptions) (lo2023thefunctionalimpact pages 1-3, redant2021managementoflate pages 1-3)
- HP:0001250 (Seizures) (lo2023thefunctionalimpact pages 1-3, takanashi2002distinctlyabnormalbrain pages 1-2)
- HP:0001259 (Coma) (lo2023thefunctionalimpact pages 1-3, redant2021managementoflate pages 1-3)
- HP:0000716 (Depression of consciousness / altered mental status) (takanashi2002distinctlyabnormalbrain pages 1-2, redant2021managementoflate pages 1-3)
- HP:0002013 (Vomiting) (lo2023thefunctionalimpact pages 1-3, takanashi2002distinctlyabnormalbrain pages 1-2)
- HP:0001270 (Motor delay) / HP:0001263 (Global developmental delay) (late-onset pediatric manifestations) (takanashi2002distinctlyabnormalbrain pages 1-2)

7. Recent Developments (2023–2024 priority): genetics, biomarkers, and therapeutic translation

7.1 Variant interpretation and genotype–phenotype (2023)
A 2023 AJHG study measured functional impacts of 1,570 OTC amino-acid substitutions and emphasized OTCD’s clinical actionability, including that OTC deficiency accounts for ~half of UCD cases and that de novo mutations account for ~20–30% of OTCD; it also highlights triggers for late-onset crises (protein, fasting, surgery, drugs, pregnancy, organic chemical exposure). (lo2023thefunctionalimpact pages 1-3)

7.2 Screening/diagnostic refinement and biomarker performance (2024)
A 2024 Vietnam referral-center study of 21 OTCD patients reported that low citrulline in DBS was not uniformly present (only half of early-onset), whereas plasma glutamine was markedly elevated in all early-onset cases; the authors argue glutamine may be a sensitive marker for neonatal OTCD and underline limitations of citrulline-based screening. (tran2024apreliminaryretrospective pages 2-4)

7.3 Gene therapy, mRNA therapy, and genome editing: current landscape (2023–2024)
A 2023 review (Yilmaz & Gissen) summarizes gene therapy modalities (AAV gene addition, mRNA therapy, genome editing) and provides key translational constraints: pediatric liver growth can dilute episomal AAV expression; risk from off-target editing and immune responses to gene-editing components is non-trivial; and liver transplantation remains the only widely accepted curative option today. (yilmaz2023genetictherapyapproaches pages 9-10, yilmaz2023genetictherapyapproaches pages 1-2)

8. Current Applications and Real-World Implementation (clinical practice)

8.1 Standard-of-care chronic management
Standard chronic management described in 2023 includes protein-restricted diet, nitrogen/ammonia scavengers, and arginine/citrulline supplementation; however, this does not reliably prevent catabolic stress–triggered crises and neurologic injury. (yilmaz2023genetictherapyapproaches pages 1-2)

8.2 Acute hyperammonemia management (hospital/ICU)
Guideline-style management summarized in a high-citation UCD update includes urgent ammonia reduction, stopping protein initially but avoiding >24–48 h complete protein withdrawal, provision of high-calorie IV glucose/lipids to suppress catabolism, and IV L-arginine plus nitrogen scavengers (e.g., sodium phenylacetate, sodium benzoate). (matsumoto2019ureacycledisorders—update pages 9-10)

An adult ICU-oriented review provides a quantitative threshold: emergent hemodialysis is advised when ammonia >200 µmol/L, noting cerebral edema risk >55% above this level. (redant2021managementoflate pages 1-3)

8.3 Liver transplantation (curative implementation) — timing and outcomes
Liver transplantation normalizes plasma ammonia and improves quality of life; in OTCD, reported 5-year survival after transplant improved to 86% (neonatal-onset) and 92% (late-onset) in one cited summary. (matsumoto2019ureacycledisorders—update pages 11-12)

9. Clinical Trials and Translational Programs (with URLs and key metadata)

9.1 AAV gene transfer (Phase 3)
- DTX301 (avalotcagene ontaparvovec), AAV8-based gene transfer
  - Trial: NCT05345171 (Ultragenyx), Phase 3, randomized, double-blind, placebo-controlled (quadruple-masked)
  - Status: Active, not recruiting
  - Enrollment: 32
  - Design: single IV infusion DTX301 vs placebo; planned crossover after Week 36–64
  - Primary outcomes include 24-hour plasma ammonia AUC0–24 at Week 36 and a complete responder rate after DTX301 exposure
  - URL: https://clinicaltrials.gov/study/NCT05345171 (registry); also see registry-linked condition page (NCT05345171 chunk 1)
  - Registry publication year in record excerpt: 2022 (NCT05345171 chunk 1)

9.2 mRNA therapy (LNP-OTC mRNA)
- ARCT-810 multiple ascending dose study in OTCD
  - Trial: NCT06488313 (Arcturus), Phase 2a open-label, recruiting
  - Start date: 2024-11-04; estimated completion ~2026-09-01
  - Enrollment: 9
  - Primary endpoint: safety/tolerability through Day 85
  - Secondary endpoints include stable isotope ureagenesis assay AUCs and proportion maintaining normal fasting plasma ammonia; changes in plasma glutamine
  - URL: https://clinicaltrials.gov/study/NCT06488313 (NCT06488313 chunk 1)

- ARCT-810 randomized placebo-controlled Phase 2 trial (terminated after slow enrollment)
  - Trial: NCT05526066, Phase 2, quadruple-masked, enrollment 8, terminated after completion of Cohort 1
  - Completion date: 2024-10-31
  - URL: https://clinicaltrials.gov/study/NCT05526066 (NCT05526066 chunk 1)

9.3 Infant gene editing program
- ECUR-506 (iECURE), single IV administration AAV-delivered gene editing payload
  - Trial: NCT06255782, Phase 1/2/3, recruiting
  - Population: male infants with neonatal-onset OTCD
  - Enrollment: 8
  - Endpoints include normalization of fasting plasma ammonia, complete clinical response definition including discontinuation of scavenger medications without reduced protein intake, and extensive genomic safety assays for on-target and off-target events
  - URL: https://clinicaltrials.gov/study/NCT06255782 (NCT06255782 chunk 1)

10. Evidence Items (PMIDs and evidence anchors)

Because the tool-provided excerpts sometimes do not display PMIDs even for PubMed-indexed articles, this report uses DOI and journal metadata plus ClinicalTrials.gov IDs as primary anchors. One exception: a clinical-trial excerpt references a PubMed ID (pmid 38171926) for a review article, but the underlying paper was not retrieved in full text here. (NCT05345171 chunk 2)

Key evidence anchors used in this report include:
- Lo et al., AJHG (2023-05-04). DOI: 10.1016/j.ajhg.2023.03.019. (lo2023thefunctionalimpact pages 1-3)
- Yilmaz & Gissen, Biomedicines (2023-08-08). DOI: 10.3390/biomedicines11082227. (yilmaz2023genetictherapyapproaches pages 1-2)
- Hu et al., Frontiers in Pediatrics (2024-09). DOI: 10.3389/fped.2024.1450859. (hu2024indepthanalysisof pages 1-2)
- Tran et al., Heliyon (2024-08). DOI: 10.1016/j.heliyon.2024.e36003. (tran2024apreliminaryretrospective pages 2-4)
- Zielińska et al., Frontiers in Neuroscience (2022-06-06). DOI: 10.3389/fnins.2022.874750. (zielinska2022dysregulationofastrocytic pages 1-2)
- Takanashi et al., Neurology (2002-07). DOI: 10.1212/wnl.59.2.210. (takanashi2002distinctlyabnormalbrain pages 1-2)
- ClinicalTrials.gov: NCT05345171 (DTX301), NCT06488313 (ARCT-810), NCT05526066, NCT06255782 (ECUR-506). (NCT05345171 chunk 1, NCT06488313 chunk 1, NCT05526066 chunk 1, NCT06255782 chunk 1)

11. Knowledge-base Ready Summary (concise)

Pathophysiology description
OTCD is an X-linked urea-cycle disorder caused by loss-of-function variants in OTC, a mitochondrial hepatocyte enzyme catalyzing carbamoyl phosphate + ornithine → citrulline. Blockade of ureagenesis causes episodic or persistent hyperammonemia. The brain detoxifies ammonia primarily via astrocytic glutamine synthetase, increasing glutamine (glutaminosis). Glutamine accumulation drives astrocyte osmotic swelling, cerebral edema, intracranial hypertension, seizures, coma, and potentially herniation/death; mitochondrial dysfunction, oxidative stress, and neurotransmitter disturbances amplify injury. Biomarker patterns include hyperammonemia, elevated glutamine (and often alanine), low citrulline (variable in DBS), and elevated urinary orotic acid. (yilmaz2023genetictherapyapproaches pages 1-2, lo2023thefunctionalimpact pages 1-3, redant2021managementoflate pages 1-3, ribas2022hyperammonemiaininherited pages 5-6, matsumoto2019ureacycledisorders—update pages 4-5)

Gene/protein annotations (HGNC)
- OTC (X-linked; mitochondrial enzyme; hepatocyte expression) (yilmaz2023genetictherapyapproaches pages 1-2)

Cell type involvement (CL)
- Hepatocyte (CL:0000182) — primary site of ureagenesis defect (yilmaz2023genetictherapyapproaches pages 1-2)
- Astrocyte (CL:0000127) — ammonia→glutamine detoxification, swelling, edema (zielinska2022dysregulationofastrocytic pages 1-2, redant2021managementoflate pages 1-3)

Anatomical locations (UBERON)
- Liver (UBERON:0002107) — primary site of defective ammonia detoxification (yilmaz2023genetictherapyapproaches pages 1-2)
- Brain (UBERON:0000955) — site of ammonia neurotoxicity and edema (redant2021managementoflate pages 1-3)

Chemical entities (CHEBI)
- Ammonia (CHEBI:16134); glutamine (CHEBI:28300); citrulline (CHEBI:16349); ornithine (CHEBI:15729); carbamoyl phosphate (CHEBI:17674); orotic acid (CHEBI:30845) (supported as key metabolites/biomarkers in text) (ribas2022hyperammonemiaininherited pages 5-6, matsumoto2019ureacycledisorders—update pages 4-5, hu2024indepthanalysisof pages 1-2)

12. Limitations of this report (evidence availability)
- A MONDO identifier for OTCD was not present in the retrieved excerpts; therefore it is not asserted.
- Several mechanistic sections rely on peer-reviewed reviews that cite primary studies without listing PMIDs in the excerpt text; PMIDs are therefore not consistently recoverable from the tool context alone, though DOIs and full citations are provided.


References

1. (OpenTargets Search: Ornithine carbamoyltransferase deficiency,Ornithine transcarbamylase deficiency-OTC): Open Targets Query (Ornithine carbamoyltransferase deficiency,Ornithine transcarbamylase deficiency-OTC, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (NCT05345171 chunk 2):  Clinical Study of DTX301 AAV-Mediated Gene Transfer for Ornithine Transcarbamylase (OTC) Deficiency. Ultragenyx Pharmaceutical Inc. 2022. ClinicalTrials.gov Identifier: NCT05345171

3. (yilmaz2023genetictherapyapproaches pages 1-2): Berna Seker Yilmaz and Paul Gissen. Genetic therapy approaches for ornithine transcarbamylase deficiency. Biomedicines, 11:2227, Aug 2023. URL: https://doi.org/10.3390/biomedicines11082227, doi:10.3390/biomedicines11082227. This article has 30 citations.

4. (lo2023thefunctionalimpact pages 1-3): Russell S. Lo, Gareth A. Cromie, Michelle Tang, Kevin Teng, Katherine Owens, Amy Sirr, J. Nathan Kutz, Hiroki Morizono, Ljubica Caldovic, Nicholas Ah Mew, Andrea Gropman, and Aimée M. Dudley. The functional impact of 1,570 individual amino acid substitutions in human otc. American journal of human genetics, 110 5:863-879, May 2023. URL: https://doi.org/10.1016/j.ajhg.2023.03.019, doi:10.1016/j.ajhg.2023.03.019. This article has 28 citations and is from a highest quality peer-reviewed journal.

5. (NCT03767270 chunk 1):  Safety, Tolerability and PK/PD Evaluation of Intravenous Administration of MRT5201 in Patients With OTC Deficiency. Translate Bio, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03767270

6. (matsumoto2019ureacycledisorders—update pages 4-5): Shirou Matsumoto, Johannes Häberle, Jun Kido, Hiroshi Mitsubuchi, Fumio Endo, and Kimitoshi Nakamura. Urea cycle disorders—update. Journal of Human Genetics, 64:833-847, May 2019. URL: https://doi.org/10.1038/s10038-019-0614-4, doi:10.1038/s10038-019-0614-4. This article has 261 citations and is from a peer-reviewed journal.

7. (hu2024indepthanalysisof pages 4-7): Qingyang Hu, Haiming Chen, Tianyi Liu, Xue-Tao Dong, Xuejiao Hu, Wenxin Yan, and Zhong Li. In-depth analysis of otc a208t case induced by otc gene mutation and research on the prediction and simulation of the impact on protein function. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1450859, doi:10.3389/fped.2024.1450859. This article has 2 citations.

8. (ribas2022hyperammonemiaininherited pages 5-6): Graziela Schmitt Ribas, Franciele Fátima Lopes, Marion Deon, and Carmen Regla Vargas. Hyperammonemia in inherited metabolic diseases. Cellular and Molecular Neurobiology, 42:2593-2610, Oct 2022. URL: https://doi.org/10.1007/s10571-021-01156-6, doi:10.1007/s10571-021-01156-6. This article has 83 citations and is from a peer-reviewed journal.

9. (nambiar2022acutefulminantencephalopathy pages 3-4): Vivek K. Nambiar, Aakash Shridharani, Sudheeran Kannoth, Siby Gopinath, and Anand Kumar. Acute fulminant encephalopathy in an adult due to ornithine transcarbamylase deficiency. Annals of Indian Academy of Neurology, 25:722-724, Jul 2022. URL: https://doi.org/10.4103/aian.aian\_1028\_21, doi:10.4103/aian.aian\_1028\_21. This article has 1 citations and is from a peer-reviewed journal.

10. (hu2024indepthanalysisof pages 1-2): Qingyang Hu, Haiming Chen, Tianyi Liu, Xue-Tao Dong, Xuejiao Hu, Wenxin Yan, and Zhong Li. In-depth analysis of otc a208t case induced by otc gene mutation and research on the prediction and simulation of the impact on protein function. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1450859, doi:10.3389/fped.2024.1450859. This article has 2 citations.

11. (ribas2022hyperammonemiaininherited pages 1-2): Graziela Schmitt Ribas, Franciele Fátima Lopes, Marion Deon, and Carmen Regla Vargas. Hyperammonemia in inherited metabolic diseases. Cellular and Molecular Neurobiology, 42:2593-2610, Oct 2022. URL: https://doi.org/10.1007/s10571-021-01156-6, doi:10.1007/s10571-021-01156-6. This article has 83 citations and is from a peer-reviewed journal.

12. (zielinska2022dysregulationofastrocytic pages 1-2): Magdalena Zielińska, Jan Albrecht, and Mariusz Popek. Dysregulation of astrocytic glutamine transport in acute hyperammonemic brain edema. Frontiers in Neuroscience, Jun 2022. URL: https://doi.org/10.3389/fnins.2022.874750, doi:10.3389/fnins.2022.874750. This article has 22 citations and is from a peer-reviewed journal.

13. (redant2021managementoflate pages 1-3): S. Redant, A. Empain, A. Mugisha, P. Kamgang, R. Attou, P. M. Honoré, and D. De Bels. Management of late onset urea cycle disorders—a remaining challenge for the intensivist? Annals of Intensive Care, Jan 2021. URL: https://doi.org/10.1186/s13613-020-00797-y, doi:10.1186/s13613-020-00797-y. This article has 41 citations and is from a peer-reviewed journal.

14. (ribas2022hyperammonemiaininherited pages 2-4): Graziela Schmitt Ribas, Franciele Fátima Lopes, Marion Deon, and Carmen Regla Vargas. Hyperammonemia in inherited metabolic diseases. Cellular and Molecular Neurobiology, 42:2593-2610, Oct 2022. URL: https://doi.org/10.1007/s10571-021-01156-6, doi:10.1007/s10571-021-01156-6. This article has 83 citations and is from a peer-reviewed journal.

15. (matsumoto2019ureacycledisorders—update pages 11-12): Shirou Matsumoto, Johannes Häberle, Jun Kido, Hiroshi Mitsubuchi, Fumio Endo, and Kimitoshi Nakamura. Urea cycle disorders—update. Journal of Human Genetics, 64:833-847, May 2019. URL: https://doi.org/10.1038/s10038-019-0614-4, doi:10.1038/s10038-019-0614-4. This article has 261 citations and is from a peer-reviewed journal.

16. (takanashi2002distinctlyabnormalbrain pages 1-2): J. Takanashi, A. Kurihara, M. Tomita, M. Kanazawa, S. Yamamoto, F. Morita, H. Ikehira, S. Tanada, and Y. Kohno. Distinctly abnormal brain metabolism in late-onset ornithine transcarbamylase deficiency. Neurology, 59:210-214, Jul 2002. URL: https://doi.org/10.1212/wnl.59.2.210, doi:10.1212/wnl.59.2.210. This article has 69 citations and is from a highest quality peer-reviewed journal.

17. (tran2024apreliminaryretrospective pages 2-4): Dien Minh Tran, Trang Thi Thu Tran, Quyen Hue Luong, and Mai Thi Chi Tran. A preliminary retrospective evaluation of screening and diagnosis of ornithine transcarbamylase deficiency in high-risk patients at a referral center in vietnam. Heliyon, 10:e36003, Aug 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e36003, doi:10.1016/j.heliyon.2024.e36003. This article has 0 citations.

18. (yuan2024clinicalcharacteristicsand pages 2-3): Gaopin Yuan, Zhiyong Liu, Zhixu Chen, Xiaohong Zhang, Weifeng Zhang, and Dongmei Chen. Clinical characteristics and molecular genetic analysis of ten cases of ornithine carbamoyltransferase deficiency in southeastern china. Italian Journal of Pediatrics, Sep 2024. URL: https://doi.org/10.1186/s13052-024-01740-8, doi:10.1186/s13052-024-01740-8. This article has 0 citations and is from a peer-reviewed journal.

19. (yilmaz2023genetictherapyapproaches pages 9-10): Berna Seker Yilmaz and Paul Gissen. Genetic therapy approaches for ornithine transcarbamylase deficiency. Biomedicines, 11:2227, Aug 2023. URL: https://doi.org/10.3390/biomedicines11082227, doi:10.3390/biomedicines11082227. This article has 30 citations.

20. (matsumoto2019ureacycledisorders—update pages 9-10): Shirou Matsumoto, Johannes Häberle, Jun Kido, Hiroshi Mitsubuchi, Fumio Endo, and Kimitoshi Nakamura. Urea cycle disorders—update. Journal of Human Genetics, 64:833-847, May 2019. URL: https://doi.org/10.1038/s10038-019-0614-4, doi:10.1038/s10038-019-0614-4. This article has 261 citations and is from a peer-reviewed journal.

21. (NCT05345171 chunk 1):  Clinical Study of DTX301 AAV-Mediated Gene Transfer for Ornithine Transcarbamylase (OTC) Deficiency. Ultragenyx Pharmaceutical Inc. 2022. ClinicalTrials.gov Identifier: NCT05345171

22. (NCT06488313 chunk 1):  A Study to Evaluate the Pharmacodynamics and Safety of ARCT-810 in Participants With OTCD. Arcturus Therapeutics, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06488313

23. (NCT05526066 chunk 1):  Study for Adolescents and Adults With Ornithine Transcarbamylase Deficiency to Evaluate Safety and Tolerability of ARCT-810. Arcturus Therapeutics, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05526066

24. (NCT06255782 chunk 1):  An Open-label Study to Investigate ECUR-506 in Male Babies Less Than 9 Months of Age With Neonatal Onset OTC Deficiency. iECURE, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06255782
