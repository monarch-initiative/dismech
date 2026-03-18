---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T23:20:51.078309'
end_time: '2026-02-23T23:36:55.196705'
duration_seconds: 964.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Citrullinemia Type I
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
- **Disease Name:** Citrullinemia Type I
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Citrullinemia Type I**.
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
- **Disease Name:** Citrullinemia Type I
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Citrullinemia Type I**.
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


Title: Pathophysiology of Citrullinemia Type I (CTLN1; ASS1 deficiency) — 2023–2024-focused Research Report

1. Disease identity, definitions, and current understanding

Citrullinemia type I (CTLN1; “argininosuccinate synthetase deficiency”) is an autosomal recessive urea-cycle disorder caused by biallelic pathogenic variants in ASS1 (OMIM #215700). ASS1 encodes argininosuccinate synthase, a cytosolic enzyme of the urea cycle that catalyzes the condensation of citrulline and aspartate to form argininosuccinate (the third enzymatic step of the urea cycle) and is reported to be mainly expressed in periportal hepatocytes. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 1-2)

Core biochemical hallmarks used clinically to recognize CTLN1 include hyperammonemia, elevated plasma citrulline, low plasma arginine, and increased urinary orotic acid (orotic aciduria), reflecting a functional block in nitrogen disposal and secondary perturbations of pyrimidine metabolism. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 2-4, gu2024visualizationofargininosuccinate pages 1-2)

MONDO identifier: not confirmed in the retrieved full-text corpus during this run; should be added from MONDO/Ontobee in a subsequent curation step.

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Primary biochemical lesion: cytosolic urea-cycle block

ASS1 deficiency disrupts ureagenesis by limiting conversion of citrulline + aspartate → argininosuccinate. This leads to accumulation of upstream substrates (notably citrulline) and failure to detoxify nitrogen, causing hyperammonemia. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 1-2)

Representative quantitative laboratory abnormalities reported in a 2024 CTLN1 case report include ammonia rising to 655 μmol/L (reference 10–30 μmol/L) and citrulline 936 μmol/L (reference 5–25 μmol/L). (gu2024visualizationofargininosuccinate media 3a7cd48b, gu2024visualizationofargininosuccinate pages 1-2)

A 2024 genetics-focused analysis of urea-cycle gene variants summarized that “classical citrullinemia shows elevated blood citrulline levels 2000–5000 µmol/L (normal < 60)” (context: distinguishing classic from milder forms), emphasizing the magnitude of metabolite accumulation in severe disease. (karachanakyankova2024rarepathogenicvariants pages 5-7)

2.2 Hyperammonemic neurotoxicity: astrocyte glutamine-osmotic injury → cerebral edema

A key mechanistic model for CNS injury in CTLN1 (and other UCDs) is that ammonia that enters the brain is rapidly detoxified by astrocytes via conversion to glutamine. A clinical review of hyperammonemia states that ammonia is “detoxified via conversion to glutamine in astrocytes,” and that “rapid intracellular glutamine accumulation increases osmolarity causing astrocyte swelling… and cerebral edema.” (alshaya2018intravenousandoral pages 1-2)

This mechanism connects systemic metabolic failure (hepatic ureagenesis deficit) to cellular brain pathology (astrocyte swelling and downstream neuronal dysfunction), explaining acute symptoms such as lethargy, seizures, increased intracranial pressure, and coma during hyperammonemic crises. (alshaya2018intravenousandoral pages 1-2, simpson2025ureacycledisorders pages 1-4, karachanakyankova2024rarepathogenicvariants pages 5-7)

2.3 Genotype-to-molecular phenotype: disrupted catalysis or tetramerization reduces residual activity

Recent human genetics/functional work supports a residual-activity model for CTLN1 severity. In a 2024 study analyzing ASS1 variants, two pathogenic missense variants were described as having “below 2% of the wild-type protein enzymatic activity,” and the phenotype spectrum was explicitly linked to residual activity (classic neonatal vs late-onset/pregnancy-triggered vs asymptomatic). (karachanakyankova2024rarepathogenicvariants pages 5-7)

Structural mechanisms implicated include distortion of the citrulline-binding site and disruption of an “oligomerization helix” important for the oligomeric state of ASS1, consistent with other 2024 in silico work emphasizing instability of a C-terminal helix required for tetramer formation. (karachanakyankova2024rarepathogenicvariants pages 5-7, gu2024visualizationofargininosuccinate pages 1-2)

3. Key molecular players (genes/proteins, metabolites, cells, anatomy)

3.1 Genes/Proteins (HGNC)

• ASS1 (HGNC:758) — argininosuccinate synthase 1; cytosolic enzyme of the urea cycle; deficiency causes CTLN1. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 1-2)

3.2 Chemical entities / metabolites (ChEBI)

Primary diagnostic/causal metabolites:
• Ammonia (NH3/NH4+) — accumulates due to impaired ureagenesis; principal driver of acute neurotoxicity. (alshaya2018intravenousandoral pages 1-2, karachanakyankova2024rarepathogenicvariants pages 5-7)
• Citrulline — accumulates upstream of ASS1 block; markedly elevated in plasma in classic disease. (liu2023functionalidentificationof pages 1-2, karachanakyankova2024rarepathogenicvariants pages 5-7)

Key secondary/related metabolites:
• Arginine — low plasma arginine reported as a biochemical marker in CTLN1. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 2-4)
• Aspartate — ASS1 substrate; central to the blocked reaction. (liu2023functionalidentificationof pages 1-2)
• Glutamine — rises in brain/astrocytes during ammonia detoxification; implicated in osmotic swelling and cerebral edema. (alshaya2018intravenousandoral pages 1-2, karachanakyankova2024rarepathogenicvariants pages 5-7)
• Orotic acid — increased urinary excretion (orotic aciduria), reflecting secondary pathway effects. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 2-4)

Therapy-relevant small molecules (used across UCDs, including CTLN1):
• Sodium benzoate; sodium phenylbutyrate; glycerol phenylbutyrate — “nitrogen scavengers” that remove nitrogen through alternative pathways. (yin2024asurvivalguide pages 16-19, posset2024severityadjustedevaluationof pages 1-2)

3.3 Cell types (Cell Ontology, CL)

• Hepatocytes (periportal hepatocytes in particular) — predominant ASS1 expression and site of physiologic ureagenesis. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 1-2)
• Astrocytes — principal brain-resident ammonia-detoxifying cells implicated in glutamine-mediated swelling/edema. (alshaya2018intravenousandoral pages 1-2)

3.4 Anatomical locations (UBERON)

• Liver (periportal region) — primary site of urea cycle flux and ASS1 expression. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 1-2)
• Brain (CNS) — target of ammonia toxicity; edema/seizure risk during hyperammonemia. (alshaya2018intravenousandoral pages 1-2, simpson2025ureacycledisorders pages 1-4)

3.5 Cellular components (GO Cellular Component)

• Cytosol — ASS1 is described as a cytosolic enzyme. (gu2024visualizationofargininosuccinate pages 1-2, liu2023functionalidentificationof pages 1-2)

4. Biological processes disrupted (GO-oriented mapping)

Primary disrupted processes:
• Urea cycle / ureagenesis / nitrogen compound metabolic process — reduced conversion of waste nitrogen to urea due to ASS1 deficiency. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 1-2)
• Citrulline metabolic process / arginine biosynthetic process (urea-cycle dependent) — decreased arginine availability and citrulline accumulation at the ASS1 step. (liu2023functionalidentificationof pages 1-2, gu2024visualizationofargininosuccinate pages 2-4)

Downstream brain processes affected during crises:
• Ammonia detoxification to glutamine in astrocytes (part of glutamine biosynthetic process) — mechanistically linked to osmotic stress and edema. (alshaya2018intravenousandoral pages 1-2)
• Cellular osmotic stress response / cell swelling → cerebral edema cascade (pathophysiologic mechanism described clinically). (alshaya2018intravenousandoral pages 1-2)

5. Disease progression: sequence from trigger to clinical manifestations

5.1 Initial trigger: genetic loss-of-function in ASS1

Inherited ASS1 variants reduce ASS1 protein abundance and/or enzymatic activity, causing a constitutive reduction of hepatic ureagenesis capacity. Recent functional studies identify variants that decrease ASS1 at protein and transcription levels and demonstrate markedly reduced enzyme activity for truncating or in-frame coding variants. (liu2023functionalidentificationof pages 1-2)

5.2 Metabolic decompensation: nitrogen load and catabolic stress

Although baseline impairment exists, acute hyperammonemic crises are commonly precipitated when nitrogen production exceeds residual detoxification capacity (e.g., illness/catabolism), producing abrupt rises in ammonia and citrulline. (alshaya2018intravenousandoral pages 1-2, simpson2025ureacycledisorders pages 1-4)

5.3 CNS injury: ammonia entry into brain → astrocytic glutamine accumulation → edema

As ammonia rises systemically, it crosses into the CNS and is converted to glutamine in astrocytes. Rapid glutamine accumulation drives osmotic swelling, inflammatory cascades, and cerebral edema, producing encephalopathy (lethargy → seizures → coma). (alshaya2018intravenousandoral pages 1-2, karachanakyankova2024rarepathogenicvariants pages 5-7)

6. Phenotypic manifestations and their mechanistic links (HP-oriented)

Key clinical phenotypes described in recent literature include:
• Hyperammonemia (biochemical) and encephalopathy: neonatal acute form with “hyperammonemia, progressive lethargy, poor feeding, vomiting and signs of increased intracranial pressure.” (karachanakyankova2024rarepathogenicvariants pages 5-7)
• Seizures/convulsions during crises and evolving neurologic injury. (gu2024visualizationofargininosuccinate pages 1-2, simpson2025ureacycledisorders pages 1-4)
• Chronic/late-onset phenotypes: intermittent hyperammonemia, developmental delay, and neurocognitive impairment consistent with cumulative or early irreversible injury. (karachanakyankova2024rarepathogenicvariants pages 5-7)

7. Recent developments and latest research (prioritizing 2023–2024)

7.1 Variant interpretation and structure-function (2023–2024)

• 2023 functional validation studies have expanded pathogenic ASS1 variant spectra and demonstrated that some non-coding variants can be hypomorphic by reducing expression, linking genotype to residual activity. (liu2023functionalidentificationof pages 1-2)
• 2024 structural/in silico analysis emphasizes the importance of C-terminal structural elements for oligomer/tetramer stability, supporting a mechanistic explanation for loss of function in specific deletion-insertion variants. (gu2024visualizationofargininosuccinate pages 1-2)

7.2 RNA therapeutics and mRNA approaches (2024)

A 2024 authoritative review of RNA therapeutics for UCDs notes that “LNP-formulated mRNA therapy has been assayed preclinically for citrullinemia type I (CTLN1),” positioning liver-targeted RNA delivery as an emerging disease-modifying strategy beyond diet and scavengers. (richard2024exploringrnatherapeutics pages 1-2)

The same review provides an actionable genetic insight: nonsense mutations occur in a minority of UCD genes, including “~7–10%” for ASS1 among others, highlighting a defined subset potentially addressable by suppressor-tRNA or readthrough-style RNA approaches. (richard2024exploringrnatherapeutics pages 1-2)

7.3 Contemporary evaluation of liver transplantation (2024)

A 2024 Genetics in Medicine study provides severity-adjusted comparative outcomes for liver transplantation (LTx) vs medical management across UCDs including CTLN1. LTx was associated with sustained metabolic stability and “prevention of further [hyperammonemic events] after transplantation,” along with “liberalization of protein intake,” and the conclusion that LTx provides metabolic stability “without further need of protein restriction or nitrogen-scavenging therapy.” (posset2024severityadjustedevaluationof pages 1-2, posset2024severityadjustedevaluationof pages 8-9)

However, neurocognitive outcomes did not improve compared with medically managed counterparts; one interpretation is that neurocognitive impairment can reflect irreversible early injury related to NH4+max and early crisis severity. (posset2024severityadjustedevaluationof pages 1-2, posset2024severityadjustedevaluationof pages 8-9)

8. Current applications and real-world implementations

8.1 Newborn screening and early detection

Real-world registry evidence indicates that early diagnosis through newborn screening can improve survival and reduce neurological impairment in UCDs. In the Spanish UCD registry analysis (cases up to Feb 2024; published 2025), only 10.6% were diagnosed via newborn screening, yet diagnosis via NBS was associated with improved survival and reduced neurologic impairment. (martinhernandez2025understandingthenatural pages 2-3)

8.2 Acute hyperammonemia management (practice thresholds and interventions)

A clinical “survival guide” type resource (2024) summarizes operational thresholds and acute actions used in practice, including: “Stop protein intake (for a maximum 48 hours).” and dialysis escalation when “blood NH4+ escalates to >500 μmol/L” (continuous renal replacement therapy). It also provides common dosing ranges for IV nitrogen scavengers and arginine intermediates and distinguishes normal vs suspicious ammonia thresholds (e.g., suspect IEM >200 μmol/L in neonates). (yin2024asurvivalguide pages 16-19)

Mechanistic rationale for emergent management is grounded in the astrocyte/glutamine edema model described above. (alshaya2018intravenousandoral pages 1-2)

8.3 Long-term medical management

Long-term management for CTLN1 and other UCDs centers on protein-restricted nutrition with essential amino-acid support and nitrogen scavengers (benzoate/phenylbutyrate formulations) plus arginine/citrulline supplementation tailored to the specific enzyme defect. These principles are summarized in the transplantation comparative study background and in practical clinical guidance. (posset2024severityadjustedevaluationof pages 1-2, yin2024asurvivalguide pages 16-19)

8.4 Liver transplantation

LTx is currently the only established “curative” intervention at the metabolic level for hepatic ureagenesis defects. In a large modern analysis, transplant programs show “overall 5-year patient survival rate of over 90% and a 5-year graft survival rate of over 85%.” (posset2024severityadjustedevaluationof pages 1-2, posset2024severityadjustedevaluationof pages 2-4)

9. Relevant statistics and data (recent)

9.1 Registry outcomes (Spain; cases through Feb 2024; published 2025)

In the Spanish UCD registry update (n=255 UCD patients), outcomes included:
• Global mortality: 14.9%. (martinhernandez2025understandingthenatural pages 2-3)
• Early-onset vs late-onset mortality: 35.8% vs 7.1%. (martinhernandez2025understandingthenatural pages 2-3)
• Neurological impairment: 44% of patients. (martinhernandez2025understandingthenatural pages 2-3)
• Diagnostic ammonia as a prognostic marker: median ammonia in deceased patients 1058 μmol/L (IQR 410–1793) vs 294 μmol/L (IQR 71–494) in survivors. (martinhernandez2025understandingthenatural pages 2-3)
• Liver transplantation performed in 20.6% with survival 95.2%. (martinhernandez2025understandingthenatural pages 2-3)

9.2 Severity-adjusted transplant analysis (2024)

In Posset et al. (2024), liver transplantation eliminated hyperammonemic events post-transplant (mean HAEs 0.00 post-LTx in both severe and attenuated groups), while pre-LTx patients had higher HAE rates than medically managed peers (consistent with confounding-by-indication and/or modifying factors). (posset2024severityadjustedevaluationof pages 4-6)

10. Expert opinions and authoritative synthesis

Across authoritative sources, a convergent expert view emerges:
• CTLN1 is fundamentally a liver-based cytosolic ureagenesis defect, but its morbidity/mortality is dominated by acute brain injury during hyperammonemic crises via astrocyte glutamine-mediated edema. (alshaya2018intravenousandoral pages 1-2, liu2023functionalidentificationof pages 1-2)
• Prevention of hyperammonemic events is a primary therapeutic goal; however, neurocognitive outcomes may not normalize even with definitive hepatic correction (transplantation), supporting the concept of early irreversible injury and emphasizing the value of rapid diagnosis and early crisis avoidance. (posset2024severityadjustedevaluationof pages 1-2, martinhernandez2025understandingthenatural pages 2-3)
• Next-generation therapeutics are shifting toward liver-targeted gene/RNA modalities; notably, LNP mRNA therapy has already been tested preclinically for CTLN1, indicating a plausible route for future disease modification without transplantation. (richard2024exploringrnatherapeutics pages 1-2)

11. Knowledge-base–ready annotation block (structured)

11.1 Pathophysiology description (narrative)

Citrullinemia type I is caused by biallelic loss of argininosuccinate synthase 1 (ASS1), a cytosolic periportal-hepatocyte urea-cycle enzyme that catalyzes citrulline + aspartate → argininosuccinate. Enzyme deficiency blocks ureagenesis, producing hyperammonemia, citrullinemia, hypocitrulline-to-arginine conversion with low arginine, and orotic aciduria. During catabolic stress, systemic ammonia rises and enters the CNS, where astrocytes detoxify ammonia to glutamine; rapid intracellular glutamine accumulation raises osmolarity, inducing astrocyte swelling, inflammatory cascades, and cerebral edema with seizures, coma, and risk of death. Residual ASS1 activity and variant structural impacts (citrulline binding vs oligomerization/tetramer stability) contribute to the severity continuum from classic neonatal-onset to late-onset presentations.

11.2 Ontology-style entities

Genes (HGNC):
• ASS1 (argininosuccinate synthase 1). (liu2023functionalidentificationof pages 1-2)

Biological Processes (GO; representative):
• Urea cycle / ureagenesis (nitrogen disposal). (liu2023functionalidentificationof pages 1-2)
• Citrulline metabolic process / arginine biosynthesis (urea-cycle dependent). (liu2023functionalidentificationof pages 1-2)
• Glutamine biosynthetic process in astrocytes during ammonia detoxification (mechanistic). (alshaya2018intravenousandoral pages 1-2)

Cellular Components (GO CC):
• Cytosol (ASS1 localization). (gu2024visualizationofargininosuccinate pages 1-2, liu2023functionalidentificationof pages 1-2)

Cell Types (CL; representative):
• Hepatocyte (periportal hepatocyte emphasis). (liu2023functionalidentificationof pages 1-2)
• Astrocyte. (alshaya2018intravenousandoral pages 1-2)

Anatomy (UBERON; representative):
• Liver; periportal zone. (liu2023functionalidentificationof pages 1-2)
• Brain/CNS. (alshaya2018intravenousandoral pages 1-2)

Phenotypes (HP; representative, text-mapped):
• Hyperammonemia; encephalopathy; lethargy; seizures; cerebral edema/increased intracranial pressure; developmental delay/intellectual disability. (karachanakyankova2024rarepathogenicvariants pages 5-7, alshaya2018intravenousandoral pages 1-2)

Chemicals (ChEBI; representative):
• Ammonia; citrulline; arginine; aspartate; glutamine; orotic acid; benzoate; phenylbutyrate/glycerol phenylbutyrate. (alshaya2018intravenousandoral pages 1-2, liu2023functionalidentificationof pages 1-2, posset2024severityadjustedevaluationof pages 1-2)

11.3 Evidence items (PMID/DOI/URL)

Because PMIDs were not available in the tool metadata for several key 2023–2024 sources, the evidence list includes DOI and URL (both are stable identifiers). If PMIDs are required for downstream ingestion, a separate PubMed lookup step is recommended.

Key mechanistic/definition sources:
• Liu et al., Frontiers in Genetics (Jul 2023). DOI: 10.3389/fgene.2023.1172947. URL: https://doi.org/10.3389/fgene.2023.1172947 (liu2023functionalidentificationof pages 1-2)
• Gu et al., Frontiers in Molecular Biosciences (Nov 2024). DOI: 10.3389/fmolb.2024.1482773. URL: https://doi.org/10.3389/fmolb.2024.1482773 (gu2024visualizationofargininosuccinate pages 1-2)

Neurotoxicity mechanism:
• Alshaya et al., Current Emergency and Hospital Medicine Reports (Oct 2018). DOI: 10.1007/s40138-018-0174-5. URL: https://doi.org/10.1007/s40138-018-0174-5 (alshaya2018intravenousandoral pages 1-2)

Emerging therapies:
• Richard et al., Journal of Inherited Metabolic Disease (Oct 2024). DOI: 10.1002/jimd.12807. URL: https://doi.org/10.1002/jimd.12807 (richard2024exploringrnatherapeutics pages 1-2)

Transplant outcomes:
• Posset et al., Genetics in Medicine (Apr 2024). DOI: 10.1016/j.gim.2023.101039. URL: https://doi.org/10.1016/j.gim.2023.101039 (posset2024severityadjustedevaluationof pages 1-2)

Registry statistics:
• Martín-Hernández et al., Nutrients (Mar 2025; includes cases through Feb 2024). DOI: 10.3390/nu17071173. URL: https://doi.org/10.3390/nu17071173 (martinhernandez2025understandingthenatural pages 2-3)

Case quantitative labs (image-supported):
• Gu et al. 2024 CTLN1 case ammonia/citrulline values (cropped text image). (gu2024visualizationofargininosuccinate media 3a7cd48b)

Limitations and gaps in this run

• MONDO ID could not be verified from retrieved full texts.
• Several high-value clinical guidance documents (e.g., GeneReviews “Classic Citrullinemia” 2024) were not obtainable in-tool for full-text extraction; consequently, some classic guideline statements were supported instead by accessible peer-reviewed sources and a practice-oriented “survival guide” document.
• PMIDs were not consistently available in the retrieved metadata for 2023–2024 papers; DOI/URL-based referencing is provided.


References

1. (liu2023functionalidentificationof pages 1-2): Jing Liu, Zhongjie Wang, Huiming Yan, Yanling Teng, Qingxin Shi, Jing Chen, Wanglan Tang, Wenxian Yu, Ying Peng, Hui Xi, Na Ma, Desheng Liang, Zhuo Li, and Lingqian Wu. Functional identification of two novel variants and a hypomorphic variant in ass1 from patients with citrullinemia type i. Frontiers in Genetics, Jul 2023. URL: https://doi.org/10.3389/fgene.2023.1172947, doi:10.3389/fgene.2023.1172947. This article has 5 citations and is from a peer-reviewed journal.

2. (gu2024visualizationofargininosuccinate pages 1-2): Xia Gu, Wenhui Mo, Guiying Zhuang, Congcong Shi, Tao Wei, Jinze Zhang, Chiaowen Tu, Yao Cai, Biwen Liao, and Hu Hao. Visualization of argininosuccinate synthetase by in silico analysis: novel insights into citrullinemia type i disorders. Frontiers in Molecular Biosciences, Nov 2024. URL: https://doi.org/10.3389/fmolb.2024.1482773, doi:10.3389/fmolb.2024.1482773. This article has 0 citations.

3. (gu2024visualizationofargininosuccinate pages 2-4): Xia Gu, Wenhui Mo, Guiying Zhuang, Congcong Shi, Tao Wei, Jinze Zhang, Chiaowen Tu, Yao Cai, Biwen Liao, and Hu Hao. Visualization of argininosuccinate synthetase by in silico analysis: novel insights into citrullinemia type i disorders. Frontiers in Molecular Biosciences, Nov 2024. URL: https://doi.org/10.3389/fmolb.2024.1482773, doi:10.3389/fmolb.2024.1482773. This article has 0 citations.

4. (gu2024visualizationofargininosuccinate media 3a7cd48b): Xia Gu, Wenhui Mo, Guiying Zhuang, Congcong Shi, Tao Wei, Jinze Zhang, Chiaowen Tu, Yao Cai, Biwen Liao, and Hu Hao. Visualization of argininosuccinate synthetase by in silico analysis: novel insights into citrullinemia type i disorders. Frontiers in Molecular Biosciences, Nov 2024. URL: https://doi.org/10.3389/fmolb.2024.1482773, doi:10.3389/fmolb.2024.1482773. This article has 0 citations.

5. (karachanakyankova2024rarepathogenicvariants pages 5-7): Sena Karachanak-Yankova, Dimitar Serbezov, Georgi Antov, Mikaela Stancheva, Marta Mihaylova, Savina Hadjidekova, Draga Toncheva, Anastas Pashov, Diyana Belejanska, Yavor Zhelev, Mariya Petrova, Shima Mehrabian, and Latchezar Traykov. Rare pathogenic variants in pooled whole-exome sequencing data suggest hyperammonemia as a possible cause of dementia not classified as alzheimer’s disease or frontotemporal dementia. Genes, 15:753, Jun 2024. URL: https://doi.org/10.3390/genes15060753, doi:10.3390/genes15060753. This article has 2 citations.

6. (alshaya2018intravenousandoral pages 1-2): Abdulrahman Alshaya, John Fanikos, and Elizabeth DeMaio. Intravenous and oral hyperammonemia management. Current Emergency and Hospital Medicine Reports, 6:182-193, Oct 2018. URL: https://doi.org/10.1007/s40138-018-0174-5, doi:10.1007/s40138-018-0174-5. This article has 0 citations.

7. (simpson2025ureacycledisorders pages 1-4): KL Simpson, EL MacLeod, and A Kakajiwala. Urea cycle disorders overview. Unknown journal, 2025.

8. (yin2024asurvivalguide pages 16-19): LH YIN. A survival guide a survival guide. Unknown journal, 2024.

9. (posset2024severityadjustedevaluationof pages 1-2): Roland Posset, Sven F. Garbade, Florian Gleich, Svenja Scharre, Jürgen G. Okun, Andrea L. Gropman, Sandesh C.S. Nagamani, Ann-Catrin Druck, Friederike Epp, Georg F. Hoffmann, Stefan Kölker, Matthias Zielonka, Nicholas Ah Mew, Jennifer Seminara, Lindsay C. Burrage, Gerard T. Berry, Margo Breilyn, Andreas Schulze, Cary O. Harding, Susan A. Berry, Derek Wong, Shawn E. McCandless, Matthias R. Baumgartner, Laura Konczal, Can Ficicioglu, George A. Diaz, Curtis R. Coughlin, Gregory M. Enns, Renata C. Gallagher, Christina Lam, Tamar Stricker, Greta Wilkening, Carlo Dionisi-Vici, Dries Dobbelaere, Javier Blasco-Alonso, Alberto B. Burlina, Peter Freisinger, Peter M. van Hasselt, Anastasia Skouma, Allan M. Lund, Roshni Vara, Adrijan Sarajlija, Andrew A. Morris, Anupam Chakrapani, Ivo Barić, Persephone Augoustides-Savvopoulou, Yin-Hsiu Chien, Elisenda Cortès-Saladelafont, Francois Eyskens, Gwendolyn Gramer, Jiri Zeman, Daniela Karall, Maria L. Couce, Chris Mühlhausen, Consuelo Pedrón-Giner, Ute Spiekerkoetter, Jolanta Sykut-Cegielska, Margreet Wagenmakers, and Frits A. Wijburg. Severity-adjusted evaluation of liver transplantation on health outcomes in urea cycle disorders. Genetics in Medicine, 26:101039, Apr 2024. URL: https://doi.org/10.1016/j.gim.2023.101039, doi:10.1016/j.gim.2023.101039. This article has 11 citations and is from a highest quality peer-reviewed journal.

10. (richard2024exploringrnatherapeutics pages 1-2): Eva Richard, Ainhoa Martínez‐Pizarro, and Lourdes R. Desviat. Exploring rna therapeutics for urea cycle disorders. Journal of Inherited Metabolic Disease, 47:1269-1277, Oct 2024. URL: https://doi.org/10.1002/jimd.12807, doi:10.1002/jimd.12807. This article has 4 citations and is from a peer-reviewed journal.

11. (posset2024severityadjustedevaluationof pages 8-9): Roland Posset, Sven F. Garbade, Florian Gleich, Svenja Scharre, Jürgen G. Okun, Andrea L. Gropman, Sandesh C.S. Nagamani, Ann-Catrin Druck, Friederike Epp, Georg F. Hoffmann, Stefan Kölker, Matthias Zielonka, Nicholas Ah Mew, Jennifer Seminara, Lindsay C. Burrage, Gerard T. Berry, Margo Breilyn, Andreas Schulze, Cary O. Harding, Susan A. Berry, Derek Wong, Shawn E. McCandless, Matthias R. Baumgartner, Laura Konczal, Can Ficicioglu, George A. Diaz, Curtis R. Coughlin, Gregory M. Enns, Renata C. Gallagher, Christina Lam, Tamar Stricker, Greta Wilkening, Carlo Dionisi-Vici, Dries Dobbelaere, Javier Blasco-Alonso, Alberto B. Burlina, Peter Freisinger, Peter M. van Hasselt, Anastasia Skouma, Allan M. Lund, Roshni Vara, Adrijan Sarajlija, Andrew A. Morris, Anupam Chakrapani, Ivo Barić, Persephone Augoustides-Savvopoulou, Yin-Hsiu Chien, Elisenda Cortès-Saladelafont, Francois Eyskens, Gwendolyn Gramer, Jiri Zeman, Daniela Karall, Maria L. Couce, Chris Mühlhausen, Consuelo Pedrón-Giner, Ute Spiekerkoetter, Jolanta Sykut-Cegielska, Margreet Wagenmakers, and Frits A. Wijburg. Severity-adjusted evaluation of liver transplantation on health outcomes in urea cycle disorders. Genetics in Medicine, 26:101039, Apr 2024. URL: https://doi.org/10.1016/j.gim.2023.101039, doi:10.1016/j.gim.2023.101039. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (martinhernandez2025understandingthenatural pages 2-3): Elena Martín-Hernández, Marcello Bellusci, Patricia Pérez-Mohand, Patricia Correcher Medina, Javier Blasco-Alonso, Ana Morais-López, Javier de las Heras, Silvia María Meavilla Olivas, Lucy Dougherty-de Miguel, Maria Luz Couce, Elvira Cañedo Villarroya, María Concepción García Jiménez, Pedro Juan Moreno-Lozano, Inmaculada Vives, Mercedes Gil-Campos, Sinziana Stanescu, Leticia Ceberio-Hualde, María Camprodón, Elisenda Cortès-Saladelafont, Rafael López-Urdiales, Mercedes Murray Hurtado, Ana María Márquez Armenteros, Concha Sierra Córcoles, Luis Peña-Quintana, Mónica Ruiz-Pons, Carlos Alcalde, Fernando Castellanos-Pinedo, Elena Dios, Delia Barrio-Carreras, María Martín-Cazaña, Mónica García-Peris, José David Andrade, Camila García-Volpe, Mariela de los Santos, Angels García-Cazorla, Mireia del Toro, Ana Felipe-Rucián, María José Comino Monroy, Paula Sánchez-Pintos, Ana Matas, David Gil Ortega, Álvaro Martín-Rivada, Ana Bergua, Amaya Belanger-Quintana, Isidro Vitoria, Raquel Yahyaoui, Belén Pérez, Montserrat Morales-Conejo, and Pilar Quijada-Fraile. Understanding the natural history and the effects of current therapeutic strategies on urea cycle disorders: insights from the ucd spanish registry. Nutrients, 17:1173, Mar 2025. URL: https://doi.org/10.3390/nu17071173, doi:10.3390/nu17071173. This article has 0 citations.

13. (posset2024severityadjustedevaluationof pages 2-4): Roland Posset, Sven F. Garbade, Florian Gleich, Svenja Scharre, Jürgen G. Okun, Andrea L. Gropman, Sandesh C.S. Nagamani, Ann-Catrin Druck, Friederike Epp, Georg F. Hoffmann, Stefan Kölker, Matthias Zielonka, Nicholas Ah Mew, Jennifer Seminara, Lindsay C. Burrage, Gerard T. Berry, Margo Breilyn, Andreas Schulze, Cary O. Harding, Susan A. Berry, Derek Wong, Shawn E. McCandless, Matthias R. Baumgartner, Laura Konczal, Can Ficicioglu, George A. Diaz, Curtis R. Coughlin, Gregory M. Enns, Renata C. Gallagher, Christina Lam, Tamar Stricker, Greta Wilkening, Carlo Dionisi-Vici, Dries Dobbelaere, Javier Blasco-Alonso, Alberto B. Burlina, Peter Freisinger, Peter M. van Hasselt, Anastasia Skouma, Allan M. Lund, Roshni Vara, Adrijan Sarajlija, Andrew A. Morris, Anupam Chakrapani, Ivo Barić, Persephone Augoustides-Savvopoulou, Yin-Hsiu Chien, Elisenda Cortès-Saladelafont, Francois Eyskens, Gwendolyn Gramer, Jiri Zeman, Daniela Karall, Maria L. Couce, Chris Mühlhausen, Consuelo Pedrón-Giner, Ute Spiekerkoetter, Jolanta Sykut-Cegielska, Margreet Wagenmakers, and Frits A. Wijburg. Severity-adjusted evaluation of liver transplantation on health outcomes in urea cycle disorders. Genetics in Medicine, 26:101039, Apr 2024. URL: https://doi.org/10.1016/j.gim.2023.101039, doi:10.1016/j.gim.2023.101039. This article has 11 citations and is from a highest quality peer-reviewed journal.

14. (posset2024severityadjustedevaluationof pages 4-6): Roland Posset, Sven F. Garbade, Florian Gleich, Svenja Scharre, Jürgen G. Okun, Andrea L. Gropman, Sandesh C.S. Nagamani, Ann-Catrin Druck, Friederike Epp, Georg F. Hoffmann, Stefan Kölker, Matthias Zielonka, Nicholas Ah Mew, Jennifer Seminara, Lindsay C. Burrage, Gerard T. Berry, Margo Breilyn, Andreas Schulze, Cary O. Harding, Susan A. Berry, Derek Wong, Shawn E. McCandless, Matthias R. Baumgartner, Laura Konczal, Can Ficicioglu, George A. Diaz, Curtis R. Coughlin, Gregory M. Enns, Renata C. Gallagher, Christina Lam, Tamar Stricker, Greta Wilkening, Carlo Dionisi-Vici, Dries Dobbelaere, Javier Blasco-Alonso, Alberto B. Burlina, Peter Freisinger, Peter M. van Hasselt, Anastasia Skouma, Allan M. Lund, Roshni Vara, Adrijan Sarajlija, Andrew A. Morris, Anupam Chakrapani, Ivo Barić, Persephone Augoustides-Savvopoulou, Yin-Hsiu Chien, Elisenda Cortès-Saladelafont, Francois Eyskens, Gwendolyn Gramer, Jiri Zeman, Daniela Karall, Maria L. Couce, Chris Mühlhausen, Consuelo Pedrón-Giner, Ute Spiekerkoetter, Jolanta Sykut-Cegielska, Margreet Wagenmakers, and Frits A. Wijburg. Severity-adjusted evaluation of liver transplantation on health outcomes in urea cycle disorders. Genetics in Medicine, 26:101039, Apr 2024. URL: https://doi.org/10.1016/j.gim.2023.101039, doi:10.1016/j.gim.2023.101039. This article has 11 citations and is from a highest quality peer-reviewed journal.
