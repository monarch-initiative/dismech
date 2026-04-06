---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-23T22:58:40.117361'
end_time: '2026-02-23T23:18:07.194890'
duration_seconds: 1167.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Homocystinuria
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Homocystinuria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Homocystinuria**.
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
- **Disease Name:** Homocystinuria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Homocystinuria**.
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


Title: Pathophysiology of Homocystinuria (Genetic) — Molecular and Cellular Mechanisms

Target disease and ontology mapping
- Disease: Homocystinuria (genetic heterogeneous group)
- MONDO ID: MONDO_0004737 (homocystinuria) (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
- Key subtype emphasized here: Classical homocystinuria due to cystathionine β-synthase (CBS) deficiency (also “CBS-deficient homocystinuria”). (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4)

Executive summary (current understanding)
Homocystinuria comprises inherited disorders that elevate homocysteine (Hcy) by blocking either (i) Hcy transsulfuration (classical CBS deficiency) or (ii) Hcy remethylation (e.g., MTHFR/MTR/MTRR and cobalamin-processing defects). In classical CBS deficiency, a metabolic block at the methionine-cycle/transsulfuration branchpoint causes accumulation of Hcy and upstream one-carbon metabolites (methionine, SAM, SAH) with depletion of cystathionine/cysteine, and these biochemical perturbations drive multisystem disease through redox stress/mitochondrial dysfunction, toxic protein modifications (notably via Hcy thiolactone), ER stress/proteostasis disruption, endothelial dysfunction/platelet activation with thrombosis, and neuro-excitotoxicity via homocysteic acid/NMDA signaling. (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4)

1. Key concepts and definitions (mechanism-centered)

1.1 Definitions
- Hyperhomocysteinemia (HHcy): blood Hcy >15 µmol/L. Severity categories often used clinically: mild 16–30 µmol/L, moderate 31–100 µmol/L, severe >100 µmol/L. (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
- Classical homocystinuria (CBS deficiency): an autosomal recessive inborn error of sulfur amino acid metabolism; the biochemical hallmark is markedly elevated total homocysteine (tHcy), typically with elevated methionine and reduced cysteine/cystathionine. (collard2023geneticandpharmacological pages 1-2, ziegler2023inbornerrorsof pages 7-8)
- Biochemical diagnostic heuristics used in practice: normal tHcy is typically <15 µM and tHcy >100 µM is usually diagnostic/highly suggestive for classical HCU in the right biochemical context. (jain2024estimatingprevalenceof pages 1-2, ziegler2023inbornerrorsof pages 7-8)

1.2 Core biochemical lesion in CBS deficiency
CBS “lies at the branch point where the fate of Hcy is decided” between remethylation back to methionine and irreversible commitment to cysteine synthesis via transsulfuration. (philipp2024mechanismofaction pages 1-2)
- CBS reaction: condensation of homocysteine (Hcy) + serine → cystathionine; downstream steps produce cysteine and support glutathione/redox homeostasis. (philipp2024mechanismofaction pages 1-2)
- Cofactor/regulatory biology: CBS uses PLP (pyridoxal-5′-phosphate; vitamin B6-derived) and a heme cofactor, and is allosterically activated by S-adenosylmethionine (SAM). (philipp2024mechanismofaction pages 1-2)
- Loss of CBS function leads to a characteristic metabolite pattern: upstream accumulation (Hcy, methionine, SAM, SAH) and downstream depletion (cystathionine, cysteine). (philipp2024mechanismofaction pages 1-2, ziegler2023inbornerrorsof pages 7-8)

2. Core pathophysiology (molecular and cellular mechanisms)

2.1 Redox stress, oxidative damage, and mitochondrial dysfunction
A central current model is that massively elevated Hcy (a reactive thiol) and depletion of cysteine/cysteine-derived antioxidants jointly drive oxidative stress and mitochondrial injury.
- Review-level mechanism: Hcy is described as “highly reactive, redox active” and implicated in “formation of reactive oxygen species” and ER stress; decreased cysteine “contribute[s] to oxidative stress”. (majtan2023recenttherapeuticapproaches pages 3-4)
- Primary 2024 human biomarker evidence (CBS-deficient cohort): Balci et al. (Scientific Reports; publication month Nov 2024; https://doi.org/10.1038/s41598-024-80273-w) quantified mitochondrial/redox stress markers in 23 CBS-deficient patients vs controls. Patients had markedly elevated tHcy (102±63 µmol/L vs 8.9±1.7 µmol/L; p=0.000) with altered NAD redox metrics (NAD+ 16±1.2 vs 29.0±0.6 pmol/µL; NAD+/NADH ratio 0.66±0.10 vs 1.89±0.06; all p=0.000) and elevated mitokines FGF-21 (median 446 pg/mL vs 30 pg/mL) and GDF-15 (median 153 pg/mL vs 78 pg/mL). Mitochondrial DAMPs were ~2-fold elevated (e.g., MT-COX1/GAPDH 2.4±0.4 vs 1.0±0.1). (balci2024oxidativedamageand pages 2-3)
- Correlation structure linking biochemistry to mitochondrial stress: total homocysteine correlated positively with GDF-15 (r=0.524, p<0.05) and with NAD+/NADH (r=0.499, p<0.05), and negatively with total NAD (r=-0.446, p<0.05) and NADH (r=-0.512, p<0.05). (balci2024oxidativedamageand pages 4-5)
Interpretation: these data support a disease-relevant coupling between Hcy burden and mitochondrial stress signaling/redox imbalance, consistent with oxidative damage coexisting with mitochondrial dysfunction in CBS deficiency. (balci2024oxidativedamageand pages 1-2, balci2024oxidativedamageand pages 2-3)

2.2 Proteome damage and proteostasis/ER stress (conformational disease biology)
A major contemporary mechanistic theme (2023–2024) is that classical HCU is not only a metabolite-toxicity disorder but also a “conformational disorder” at the protein level, because many CBS pathogenic variants misfold and are cleared by cellular quality-control systems.
- Review/primary evidence: “HCU should be viewed as a protein conformational disorder with protein misfolding and instability as the main mechanism resulting in CBS deficiency.” (Protein Science; Jul 2024; https://doi.org/10.1002/pro.5123) (mijatovic2024cellularturnoverand pages 1-2)
- Cellular degradation pathways: Mijatovic et al. (2024) found “proteasomal degradation is the major pathway for CBS disposal, with a minor involvement of lysosomal-autophagic and endoplasmic reticulum-associated degradation (ERAD) pathways for HCU mutants”; proteasome inhibition increased half-life and activity of T191M and I278T, and ERAD inhibition also rescued activity. (mijatovic2024cellularturnoverand pages 1-2)
- Variant stability kinetics (quantitative): WT CBS half-life ~16.6 h; common pathogenic variants show shorter half-lives, e.g., I278T 5.9 h and T191M 7.7 h. (mijatovic2024cellularturnoverand pages 8-10)
- ER stress signaling and chaperone biology (2023): Collard & Majtan (Molecular and Cellular Biology; Dec 2023; https://doi.org/10.1080/10985549.2023.2284147) describe upregulation of ER stress sensor BiP and association with proteasomes for I278T, implicating proteotoxic stress and proteasomal degradation; they also show partial rescue of permissive variants via HSP70/HSF1 co-expression and pharmacologic proteostasis modulation. (collard2023geneticandpharmacological pages 1-2, collard2023geneticandpharmacological pages 2-4)
Mechanistic implication: at the cellular level, ER proteostasis pathways (UPR/ISR), ubiquitin–proteasome system (UPS), ERAD, and autophagy contribute to the degree of residual CBS function and may be leveraged therapeutically. (mijatovic2024cellularturnoverand pages 1-2, collard2023geneticandpharmacological pages 1-2)

2.3 Toxic homocysteine chemistry: homocysteic acid, Hcy thiolactone, and (N/S)-homocysteinylation
Several chemically defined Hcy-derived species link the metabolic lesion to specific molecular damage.
- Homocysteic acid: described as “excitotoxic” and a “potent agonist of glutamatergic NMDA receptors,” supporting a mechanistic bridge to seizures and neurocognitive pathology. (majtan2023recenttherapeuticapproaches pages 3-4)
- Hcy thiolactone and irreversible N-homocysteinylation: Hcy thiolactone “reacts with free amino groups of protein lysine residues causing irreversible N-homocysteinylation,” leading to “structural changes, protein aggregation and loss of function.” (majtan2023recenttherapeuticapproaches pages 3-4)
- Pro-thrombotic protein modification: “Modification of fibrinogen by Hcy thiolactone increases resistance to fibrinolysis” (mechanistic basis for thrombosis). (majtan2023recenttherapeuticapproaches pages 3-4)
- Connective tissue mechanism: N-homocysteinylation “impairs collagen cross-linking” in mouse HCU models, supporting skeletal/connective-tissue abnormalities. (majtan2023recenttherapeuticapproaches pages 3-4)

2.4 Endothelial dysfunction, platelet activation, and thrombosis
Vascular complications are among the most clinically consequential outcomes, and current models connect them to Hcy redox chemistry, protein modifications, and methylation imbalance.
- Mechanistic chain: Hcy-driven ROS/protein stress contributes to “endothelial cell dysfunction and platelet activation,” progressing to “thrombus formation and vascular occlusion.” (majtan2023recenttherapeuticapproaches pages 3-4)
- SAH and methylation: “Endothelial dysfunction was found to associate with increased levels of SAH” in CBS-deficient mice; increased SAH can inhibit methylation reactions, contributing to cognitive impairment and potentially vascular dysfunction. (majtan2023recenttherapeuticapproaches pages 3-4)
- Natural history risk statistic: thromboembolic risk in untreated classical HCU can rise to ~50% by age 30, and risk appears proportional to degree/duration of Hcy elevation. (ziegler2023inbornerrorsof pages 7-8)

3. Key molecular players (structured)

3.1 Genes/proteins (HGNC symbols)
Causal/central
- CBS (cystathionine beta-synthase): loss-of-function causes classical homocystinuria; CBS is PLP-dependent, heme-containing, SAM-activated enzyme at the remethylation/transsulfuration branchpoint. (philipp2024mechanismofaction pages 1-2)
Remethylation and cobalamin/folate-related (important for disease heterogeneity and differential diagnosis)
- MTHFR, MTR, MTRR: remethylation pathway components; defects can cause HHcy/homocystinuria phenotypes, often with hypomethioninemia. (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
- MMACHC/MMADHC and other cobalamin-processing genes: implicated in methylmalonic acidemia with homocystinuria (cblC/cblD spectrum). (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
Proteostasis modifiers (mechanistic context)
- HSPA1A/HSP70, HSF1, BiP (HSPA5), HSPB3, HSPB8, HSP40 family: implicated in CBS mutant folding/ER stress and partial functional rescue in cellular models. (collard2023geneticandpharmacological pages 1-2)

3.2 Chemical entities/metabolites (CHEBI)
Central metabolites
- Homocysteine (Hcy) (CHEBI:17230); total homocysteine (tHcy) used clinically as key biomarker. (jain2024estimatingprevalenceof pages 1-2)
- Methionine (Met) (CHEBI:16811); elevated in classical HCU and used in newborn screening. (ziegler2023inbornerrorsof pages 6-7)
- S-adenosylmethionine (SAM) (CHEBI:15414), S-adenosylhomocysteine (SAH) (CHEBI:16680): accumulate upstream of CBS block; SAH inhibits methylation reactions. (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4)
- Cystathionine (Cth) (CHEBI:15611), cysteine (Cys) (CHEBI:15356): depleted downstream of CBS; cysteine depletion contributes to oxidative stress. (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4)
Reactive/toxic derivatives and redox-linked species
- Homocysteic acid (CHEBI:17241): NMDA receptor agonist implicated in excitotoxicity/seizures. (majtan2023recenttherapeuticapproaches pages 3-4)
- Homocysteine thiolactone: reactive acylating intermediate driving N-homocysteinylation. (majtan2023recenttherapeuticapproaches pages 3-4)
- NAD+/NADH (CHEBI:13389 / CHEBI:57945): redox coenzymes altered in patients; linked to mitochondrial dysfunction. (balci2024oxidativedamageand pages 2-3)
- GDF-15, FGF-21: mitokines elevated in CBS deficiency; correlate with disease biochemistry (GDF-15 particularly). (balci2024oxidativedamageand pages 2-3, balci2024oxidativedamageand pages 4-5)
Therapeutic chemicals
- Pyridoxine / PLP (vitamin B6): cofactor and potential pharmacological chaperone for some variants. (majtan2023recenttherapeuticapproaches pages 4-6)
- Betaine (trimethylglycine): methyl donor supporting remethylation in liver via BHMT. (majtan2023recenttherapeuticapproaches pages 4-6)
- Biological reductants: N-acetylcysteine (NAC), MESNA, cysteamine can increase reduced Hcy availability (substrate form for CBS), improving efficacy of CBS-based enzyme replacement therapy in models. (philipp2024mechanismofaction pages 1-2)

3.3 Cell types (CL) and tissues/anatomy (UBERON) most implicated
- Hepatocytes / liver (UBERON:0002107): main site of transsulfuration/remethylation flux; therapies target restoring hepatic CBS activity; betaine remethylation via liver BHMT. (majtan2023recenttherapeuticapproaches pages 4-6)
- Vascular endothelial cells (CL:0000115) and platelets (CL:0000233): key in thrombosis phenotype; Hcy-associated ROS and protein modifications contribute to endothelial dysfunction and platelet activation. (majtan2023recenttherapeuticapproaches pages 3-4)
- Neurons (CL:0000540) / brain (UBERON:0000955): NMDA receptor-mediated excitotoxicity implicated; cognitive impairment/seizures common in untreated patients. (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 6-7)
- Ocular lens zonular fibers / eye (UBERON:0000970): ectopia lentis is common and tied to connective tissue/ECM disruption. (ziegler2023inbornerrorsof pages 6-7)
- Bone/connective tissue (UBERON:0002384 / UBERON:0002385): collagen cross-link impairment and ECM alterations; osteoporosis and marfanoid habitus. (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 6-7)

4. Biological processes disrupted (GO-oriented; suggested annotations)
The following GO biological-process themes are supported by the mechanistic evidence in recent literature:
- Sulfur amino acid metabolic process / homocysteine metabolic process (block at CBS) (philipp2024mechanismofaction pages 1-2)
- Transsulfuration pathway / cysteine biosynthetic process (depletion of Cth/Cys) (philipp2024mechanismofaction pages 1-2)
- Cellular response to oxidative stress / reactive oxygen species metabolic process (Hcy-driven ROS; cysteine depletion) (majtan2023recenttherapeuticapproaches pages 3-4, balci2024oxidativedamageand pages 2-3)
- Mitochondrial dysfunction pathways (mitochondrial DAMP release; altered NAD redox; mitokines) (balci2024oxidativedamageand pages 2-3)
- Protein folding / protein refolding / proteasome-mediated ubiquitin-dependent protein catabolic process (CBS variant misfolding and UPS disposal; rescue by proteasome inhibition/chaperones) (mijatovic2024cellularturnoverand pages 1-2, collard2023geneticandpharmacological pages 1-2)
- Endoplasmic reticulum stress / unfolded protein response (UPR) (BiP upregulation; ER stress in CBS variants; Hcy-induced ER stress) (majtan2023recenttherapeuticapproaches pages 3-4, collard2023geneticandpharmacological pages 1-2)
- Blood coagulation / thrombosis-related processes (endothelial dysfunction, platelet activation, fibrinolysis resistance via fibrinogen modification) (majtan2023recenttherapeuticapproaches pages 3-4)
- Regulation of methylation / transmethylation (SAH inhibition of methylation; DNA methylation effects) (majtan2023recenttherapeuticapproaches pages 3-4, gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
- Glutamatergic synaptic signaling / NMDA receptor signaling (homocysteic acid; seizure mechanisms) (majtan2023recenttherapeuticapproaches pages 3-4)

5. Cellular components (where processes occur)
- Cytosol and enzyme complexes of methionine cycle/transsulfuration (CBS enzymatic function) (philipp2024mechanismofaction pages 1-2)
- Endoplasmic reticulum (ER) quality control, ERAD interfaces and associated proteostasis signaling (BiP/ER stress; ERAD involvement) (mijatovic2024cellularturnoverand pages 1-2, collard2023geneticandpharmacological pages 1-2)
- Proteasome complex (UPS disposal of misfolded CBS variants) (mijatovic2024cellularturnoverand pages 1-2)
- Mitochondria (redox imbalance, DAMP release, mitokines; mtDNA-linked markers) (balci2024oxidativedamageand pages 2-3)
- Extracellular space/plasma (tHcy biomarker; reduced vs protein-bound homocysteine fractions; fibrinogen modification) (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4)

6. Disease progression model (sequence of events and phases)

6.1 Trigger and early biochemical phase
- Primary trigger: biallelic pathogenic variants in CBS causing reduced/absent enzyme activity, frequently via misfolding/instability rather than active-site disruption. (mijatovic2024cellularturnoverand pages 1-2, collard2023geneticandpharmacological pages 1-2)
- Immediate biochemical consequences: accumulation of Hcy and upstream metabolites (Met, SAM, SAH) with depletion of downstream products (cystathionine, cysteine). (philipp2024mechanismofaction pages 1-2, ziegler2023inbornerrorsof pages 7-8)

6.2 Cellular injury phase (parallel mechanisms)
A. Oxidative/mitochondrial arm
- ROS generation and redox imbalance; in patients, NAD metrics and mitochondrial stress markers (GDF-15, FGF-21, mtDAMPs) are elevated and correlate with tHcy. (balci2024oxidativedamageand pages 2-3, balci2024oxidativedamageand pages 4-5)
B. Proteostasis/ER stress arm
- Hcy is linked to unfolded protein response/ER stress at a general level, while CBS variants specifically trigger ER stress and are cleared primarily by the proteasome with contributions from ERAD/autophagy. (majtan2023recenttherapeuticapproaches pages 3-4, mijatovic2024cellularturnoverand pages 1-2)
C. Protein modification/ECM and coagulation arm
- Hcy thiolactone causes irreversible N-homocysteinylation; fibrinogen modification increases resistance to fibrinolysis (pro-thrombotic), and collagen cross-link impairment contributes to skeletal/connective tissue defects. (majtan2023recenttherapeuticapproaches pages 3-4)
D. Neuro-excitotoxic arm
- Homocysteic acid is a potent NMDA receptor agonist; NMDA-related mechanisms are invoked to explain seizures and neurocognitive injury. (majtan2023recenttherapeuticapproaches pages 3-4)

6.3 Organ-level clinical manifestation phase (temporal patterns)
- Clinical variability and staging: individuals may appear normal at birth; manifestations can appear at any age. (ziegler2023inbornerrorsof pages 6-7)
- Ocular: ectopia lentis is common by age 5–10 and becomes very frequent by later adulthood if untreated. (ziegler2023inbornerrorsof pages 6-7)
- Neurologic: developmental delay/cognitive impairment (~60% untreated) and seizures (~50% untreated) are reported. (ziegler2023inbornerrorsof pages 6-7)
- Vascular: thromboembolism often emerges in young adulthood; untreated risk may approach ~50% by age 30 and correlates with degree/duration of Hcy elevation. (ziegler2023inbornerrorsof pages 7-8)

6.4 Major modifier: pyridoxine responsiveness
- Pyridoxine responsiveness stratifies phenotype: non-responders often manifest in early childhood with multi-system features; “extreme responders” may present in (late) adulthood predominantly with thromboembolism. (majtan2023recenttherapeuticapproaches pages 3-4)

7. Phenotypic manifestations (HP terms; selected)
Mechanistically linked phenotypes highlighted in recent sources include:
- Thromboembolism / stroke (vascular occlusion; endothelial dysfunction and platelet activation) (majtan2023recenttherapeuticapproaches pages 3-4)
- Ectopia lentis / lens dislocation / myopia (connective tissue/ECM changes) (ziegler2023inbornerrorsof pages 6-7, philipp2024mechanismofaction pages 1-2)
- Osteoporosis / osteopenia and marfanoid habitus (collagen cross-linking impairment, ECM alterations) (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 6-7)
- Cognitive impairment / developmental delay; seizures (neurotoxicity, NMDA mechanisms, methylation disruption) (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 6-7)

8. Recent developments and latest research (prioritizing 2023–2024)

8.1 Mitochondrial dysfunction biomarkers (2024)
Balci et al. (Nov 2024) provide recent patient-based evidence connecting tHcy to altered NAD metrics, elevated mitokines (GDF-15/FGF-21) and increased mitochondrial DAMPs, supporting mitochondria-centered pathogenic hypotheses and potentially actionable monitoring biomarkers. (balci2024oxidativedamageand pages 2-3, balci2024oxidativedamageand pages 4-5)

8.2 CBS proteostasis as a therapeutic target (2023–2024)
- Collard & Majtan (Dec 2023) propose and experimentally support proteostasis modulation (chaperone induction, ISR modulation, proteasome inhibition) as variant-dependent functional rescue of misfolded CBS variants (e.g., R125Q permissive; I278T refractory for activity rescue in their system). (collard2023geneticandpharmacological pages 1-2, collard2023geneticandpharmacological pages 2-4)
- Mijatovic et al. (Jul 2024) refine the degradation-pathway map for common CBS mutants and quantify half-life defects, reinforcing UPS/ERAD as mechanistically central and druggable. (mijatovic2024cellularturnoverand pages 1-2, mijatovic2024cellularturnoverand pages 8-10)

8.3 Enzyme replacement therapy (ERT) mechanism refinement (2024)
Philipp et al. (Redox Biology; accepted Oct 2024; https://doi.org/10.1016/j.redox.2024.103383) clarify an important mechanistic detail for ERT: “only a reduced homocysteine serves as a substrate for CBS,” and biological reductants (NAC, MESNA, cysteamine) can increase reduced Hcy and improve ERT efficacy, lowering plasma tHcy below a “clinically relevant 100 µM threshold” in mouse models. (philipp2024mechanismofaction pages 1-2)

9. Current applications and real-world implementations

9.1 Newborn screening (NBS)
- Current implementation: most NBS programs screen using methionine (tandem MS). A positive screening methionine range cited is ~200–1500 µM (reference 10–40 µM). (ziegler2023inbornerrorsof pages 6-7)
- Known limitation: pyridoxine-responsive/milder cases may be missed because methionine may not reach the screening threshold at sampling time. (ziegler2023inbornerrorsof pages 6-7, majtan2023recenttherapeuticapproaches pages 3-4)
- Alternative approach: Qatar includes direct Hcy measurement in NBS; most programs do not, because total Hcy measurement requires chemical reduction. (ziegler2023inbornerrorsof pages 6-7, ziegler2023inbornerrorsof pages 7-8)

9.2 Standard-of-care biochemical targets and treatments
- Guideline-based biochemical targets summarized in recent sources: tHcy <100 µM for pyridoxine non-/partial responders; <50 µM for full/extreme responders; free Hcy <11 µM is also cited as a goal. (majtan2023recenttherapeuticapproaches pages 4-6, ziegler2023inbornerrorsof pages 7-8)
- Pyridoxine testing and dosing framework: standardized pyridoxine loading tests guide stratification; responsiveness categories correlate with severity. (majtan2023recenttherapeuticapproaches pages 4-6)
- Dietary methionine/protein restriction: key intervention for non-responders and some partial responders; requires Met-free, cysteine-enriched amino acid mixtures to maintain nitrogen balance. (majtan2023recenttherapeuticapproaches pages 4-6)
- Betaine: adjunct remethylation strategy; recommended dosing in recent review: 50 mg/kg/day (children, split twice daily) and ~3 g/day (adults), with methionine monitoring to keep plasma methionine <1,000 µM due to rare cerebral edema risk. (majtan2023recenttherapeuticapproaches pages 6-7)

9.3 Thrombosis prevention considerations (implementation)
Because thromboembolism is a major morbidity driver:
- Practical prevention guidance highlighted in 2023 literature includes avoiding oral contraceptives, considering prophylactic anticoagulation in the third trimester and postpartum, and surgical caution given high thrombotic risk. (ziegler2023inbornerrorsof pages 6-7)

10. Epidemiology and statistics (recent/real-world data)
- Worldwide prevalence estimates vary widely; in a 2024 US claims/EHR algorithm study (Jain et al.; Sep 2024; https://doi.org/10.1016/j.ymgmr.2024.101101), average annual standardized prevalence across 2016–2020 was estimated at 5.29 per 100,000 (broad definition) and 1.04 per 100,000 (strict definition). (jain2024estimatingprevalenceof pages 1-2)
- The same study restates widely cited diagnostic anchors: normal tHcy <15 µM and tHcy >100 µM usually diagnostic; it also notes that tHcy >30 µM may indicate HCU in some undiagnosed individuals. (jain2024estimatingprevalenceof pages 1-2)
- NBS-based global incidence estimates for classic HCU are ~1 in 200,000 to 1 in 340,000, but underestimation is likely because of NBS detection limitations and ascertainment bias. (ziegler2023inbornerrorsof pages 6-7)

11. Expert opinions and analysis (authoritative sources; with direct quotes)

Selected direct mechanistic quotes from 2023–2024 sources:
- CBS branchpoint and metabolite directionality: “CBS lies at the branch point where the fate of Hcy is decided…” and CBS deficiency leads to upstream metabolite accumulation with downstream depletion. (philipp2024mechanismofaction pages 1-2)
- Hcy chemical reactivity and ER stress: “Hcy with its free sulfhydryl group is a highly reactive, redox active compound with potential pathological mechanisms involving formation of reactive oxygen species, protein modification, induction of unfolded protein response and endoplasmic reticulum stress.” (majtan2023recenttherapeuticapproaches pages 3-4)
- Conformational disorder framing: “HCU should be viewed as a protein conformational disorder with protein misfolding and instability as the main mechanism resulting in CBS deficiency.” (mijatovic2024cellularturnoverand pages 1-2)
- ERT substrate form: “only a reduced homocysteine serves as a substrate for CBS.” (philipp2024mechanismofaction pages 1-2)

12. Knowledge-base ready annotation blocks

12.1 Pathophysiology description (narrative)
Classical homocystinuria results from biallelic CBS deficiency at the branchpoint of methionine metabolism, producing accumulation of homocysteine and upstream one-carbon metabolites (methionine, SAM, SAH) with depletion of cystathionine/cysteine. The elevated, reactive thiol homocysteine drives oxidative stress and mitochondrial dysfunction (as shown by altered NAD redox, mitokine elevation, and mitochondrial DAMP release in patients), induces ER stress/UPR, and generates reactive derivatives including homocysteic acid (NMDA agonist) and homocysteine thiolactone. Homocysteine thiolactone mediates irreversible N-homocysteinylation of proteins such as fibrinogen (increasing resistance to fibrinolysis) and collagen (impairing cross-linking), mechanistically linking the biochemical lesion to thrombosis and connective tissue/bone phenotypes. Endothelial dysfunction and platelet activation promote vascular occlusion and thromboembolism, while NMDA-linked excitotoxicity and methylation inhibition (via SAH) contribute to seizures and cognitive impairment. Disease timing and severity are strongly modified by pyridoxine responsiveness, with non-responders typically presenting earlier and with broader multi-organ involvement. (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4, balci2024oxidativedamageand pages 2-3)

12.2 Gene/protein annotations (HGNC; evidence items)
- CBS (HGNC:1550): causal for classical homocystinuria; mechanistic roles include transsulfuration flux control and H2S generation; pathogenic variants frequently misfold and are cleared mainly by UPS/proteasome with ERAD contributions. Evidence: Philipp et al. 2024; Mijatovic et al. 2024; Collard & Majtan 2023. (philipp2024mechanismofaction pages 1-2, mijatovic2024cellularturnoverand pages 1-2, collard2023geneticandpharmacological pages 1-2)
- MTHFR, MTR, MTRR: remethylation pathway genes causing HHcy/homocystinuria phenotypes when defective (disease heterogeneity). (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)

12.3 Suggested GO biological process terms (evidence)
- Homocysteine metabolic process / sulfur amino acid metabolic process (philipp2024mechanismofaction pages 1-2)
- Cellular response to oxidative stress; mitochondrial dysfunction-associated processes (balci2024oxidativedamageand pages 2-3)
- Protein folding; proteasome-mediated ubiquitin-dependent catabolic process; ERAD/UPR (mijatovic2024cellularturnoverand pages 1-2, collard2023geneticandpharmacological pages 1-2)
- Blood coagulation/fibrinolysis regulation (via fibrinogen modification) (majtan2023recenttherapeuticapproaches pages 3-4)
- NMDA receptor signaling / excitotoxicity-associated processes (majtan2023recenttherapeuticapproaches pages 3-4)

12.4 Phenotype associations (HP; evidence)
- Thromboembolism/stroke (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 7-8)
- Ectopia lentis / myopia (ziegler2023inbornerrorsof pages 6-7, philipp2024mechanismofaction pages 1-2)
- Osteoporosis / skeletal abnormalities / marfanoid habitus (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 6-7)
- Cognitive impairment / seizures (majtan2023recenttherapeuticapproaches pages 3-4, ziegler2023inbornerrorsof pages 6-7)

12.5 Cell type involvement (CL; evidence)
- Endothelial cells, platelets (vascular pathology) (majtan2023recenttherapeuticapproaches pages 3-4)
- Hepatocyte/liver metabolism (BHMT/betaine remethylation; CBS target tissue) (majtan2023recenttherapeuticapproaches pages 4-6)
- Neurons (NMDA-mediated excitotoxicity; neurotoxicity) (majtan2023recenttherapeuticapproaches pages 3-4)

12.6 Anatomical locations (UBERON; evidence)
- Liver (metabolic control; therapeutic target) (majtan2023recenttherapeuticapproaches pages 4-6)
- Vasculature (thrombosis phenotype) (majtan2023recenttherapeuticapproaches pages 3-4)
- Eye/lens zonules (ectopia lentis) (ziegler2023inbornerrorsof pages 6-7)
- Bone/connective tissue (osteoporosis, marfanoid features) (majtan2023recenttherapeuticapproaches pages 3-4)

12.7 Chemical entities (CHEBI; evidence)
- Homocysteine; methionine; cystathionine; cysteine; SAM; SAH; homocysteic acid; homocysteine thiolactone; NAD+/NADH; betaine; pyridoxine/PLP; N-acetylcysteine. (philipp2024mechanismofaction pages 1-2, majtan2023recenttherapeuticapproaches pages 3-4, balci2024oxidativedamageand pages 2-3)

12.8 Evidence items (PMIDs and notes)
The current tool-accessible excerpts did not reliably expose PMIDs for all cited sources. Where PMID information was visible in retrieved metadata, it was limited (e.g., OpenTargets evidence for MTHFR included PMID: 36567323 in association data). (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
Primary citations with DOIs and publication dates (URLs included):
- Majtan T, Kožich V, Kruger WD. “Recent therapeutic approaches to cystathionine beta-synthase-deficient homocystinuria.” British Journal of Pharmacology. Dec 2023. https://doi.org/10.1111/bph.15991 (majtan2023recenttherapeuticapproaches pages 3-4)
- Collard R, Majtan T. “Genetic and Pharmacological Modulation of Cellular Proteostasis…” Molecular and Cellular Biology. Dec 2023. https://doi.org/10.1080/10985549.2023.2284147 (collard2023geneticandpharmacological pages 1-2)
- González-Lamuño D, et al. “Hyperhomocysteinemia in Adult Patients: A Treatable Metabolic Condition.” Nutrients. Dec 2023. https://doi.org/10.3390/nu16010135 (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4)
- Mijatovic E, et al. “Cellular turnover and degradation of the most common missense CBS variants…” Protein Science. Jul 2024. https://doi.org/10.1002/pro.5123 (mijatovic2024cellularturnoverand pages 1-2)
- Jain M, et al. “Estimating prevalence of classical homocystinuria in the United States…” Molecular Genetics and Metabolism Reports. Sep 2024. https://doi.org/10.1016/j.ymgmr.2024.101101 (jain2024estimatingprevalenceof pages 1-2)
- Philipp TM, et al. “Mechanism of action and impact of thiol homeostasis on efficacy of an enzyme replacement therapy for classical homocystinuria.” Redox Biology. Available online Oct 2024; issue/month Nov 2024. https://doi.org/10.1016/j.redox.2024.103383 (philipp2024mechanismofaction pages 1-2)
- Balci MC, et al. “Oxidative damage and mitochondrial dysfunction in cystathionine beta-synthase deficiency.” Scientific Reports. Nov 2024. https://doi.org/10.1038/s41598-024-80273-w (balci2024oxidativedamageand pages 2-3)

13. Visual evidence
- Figure: Methionine cycle and transsulfuration pathway with therapeutic intervention points for CBS-deficient homocystinuria (Majtan et al., 2023). (majtan2023recenttherapeuticapproaches media c1dbb0d7)

Limitations
- PMID fields were not consistently available in the retrieved full-text excerpts. Mechanistic claims above are supported by the cited 2023–2024 primary and review literature via DOI-linked sources, but a comprehensive PMID list would require direct PubMed lookups beyond the currently retrieved excerpts. (majtan2023recenttherapeuticapproaches pages 3-4, balci2024oxidativedamageand pages 2-3)


References

1. (gonzalezlamuno2023hyperhomocysteinemiainadult pages 2-4): Domingo González-Lamuño, Francisco Jesús Arrieta-Blanco, Elena Dios Fuentes, María Teresa Forga-Visa, Monstserrat Morales-Conejo, Luis Peña-Quintana, and Isidro Vitoria-Miñana. Hyperhomocysteinemia in adult patients: a treatable metabolic condition. Nutrients, 16:135, Dec 2023. URL: https://doi.org/10.3390/nu16010135, doi:10.3390/nu16010135. This article has 70 citations.

2. (philipp2024mechanismofaction pages 1-2): Thilo Magnus Philipp, Teodoro Bottiglieri, Wilmelenne Clapper, Kai Liu, Steve Rodems, Csaba Szabo, and Tomas Majtan. Mechanism of action and impact of thiol homeostasis on efficacy of an enzyme replacement therapy for classical homocystinuria. Nov 2024. URL: https://doi.org/10.1016/j.redox.2024.103383, doi:10.1016/j.redox.2024.103383. This article has 5 citations and is from a domain leading peer-reviewed journal.

3. (majtan2023recenttherapeuticapproaches pages 3-4): Tomas Majtan, Viktor Kožich, and Warren D. Kruger. Recent therapeutic approaches to cystathionine beta‐synthase‐deficient homocystinuria. Dec 2023. URL: https://doi.org/10.1111/bph.15991, doi:10.1111/bph.15991. This article has 27 citations and is from a highest quality peer-reviewed journal.

4. (collard2023geneticandpharmacological pages 1-2): Renata Collard and Tomas Majtan. Genetic and pharmacological modulation of cellular proteostasis leads to partial functional rescue of homocystinuria-causing cystathionine-beta synthase variants. Molecular and Cellular Biology, 43:664-674, Dec 2023. URL: https://doi.org/10.1080/10985549.2023.2284147, doi:10.1080/10985549.2023.2284147. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (ziegler2023inbornerrorsof pages 7-8): SG Ziegler, J Kim, and JT Ehmsen. Inborn errors of amino acid metabolism–from underlying pathophysiology to therapeutic advances. Unknown journal, 2023.

6. (jain2024estimatingprevalenceof pages 1-2): Mahim Jain, Mehul Shah, Kamlesh M. Thakker, Andrew Rava, Agness Pelts Block, Colette Ndiba-Markey, and Lionel Pinto. Estimating prevalence of classical homocystinuria in the united states using optum's de-identified market clarity data. Sep 2024. URL: https://doi.org/10.1016/j.ymgmr.2024.101101, doi:10.1016/j.ymgmr.2024.101101. This article has 2 citations.

7. (balci2024oxidativedamageand pages 2-3): Mehmet Cihan Balci, Asuman Gedikbasi, Sukru Anil Dogan, Sevde Kahraman, Suzin Tatoryan, Sebnem Tekin Neijmann, Meryem Karaca, Fatmahan Atalar, and Gulden Gokcay. Oxidative damage and mitochondrial dysfunction in cystathionine beta-synthase deficiency. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80273-w, doi:10.1038/s41598-024-80273-w. This article has 1 citations and is from a peer-reviewed journal.

8. (balci2024oxidativedamageand pages 4-5): Mehmet Cihan Balci, Asuman Gedikbasi, Sukru Anil Dogan, Sevde Kahraman, Suzin Tatoryan, Sebnem Tekin Neijmann, Meryem Karaca, Fatmahan Atalar, and Gulden Gokcay. Oxidative damage and mitochondrial dysfunction in cystathionine beta-synthase deficiency. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80273-w, doi:10.1038/s41598-024-80273-w. This article has 1 citations and is from a peer-reviewed journal.

9. (balci2024oxidativedamageand pages 1-2): Mehmet Cihan Balci, Asuman Gedikbasi, Sukru Anil Dogan, Sevde Kahraman, Suzin Tatoryan, Sebnem Tekin Neijmann, Meryem Karaca, Fatmahan Atalar, and Gulden Gokcay. Oxidative damage and mitochondrial dysfunction in cystathionine beta-synthase deficiency. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-80273-w, doi:10.1038/s41598-024-80273-w. This article has 1 citations and is from a peer-reviewed journal.

10. (mijatovic2024cellularturnoverand pages 1-2): Ela Mijatovic, Kelly Ascenção, Csaba Szabo, and Tomas Majtan. Cellular turnover and degradation of the most common missense cystathionine beta‐synthase variants causing homocystinuria. Protein Science : A Publication of the Protein Society, Jul 2024. URL: https://doi.org/10.1002/pro.5123, doi:10.1002/pro.5123. This article has 9 citations.

11. (mijatovic2024cellularturnoverand pages 8-10): Ela Mijatovic, Kelly Ascenção, Csaba Szabo, and Tomas Majtan. Cellular turnover and degradation of the most common missense cystathionine beta‐synthase variants causing homocystinuria. Protein Science : A Publication of the Protein Society, Jul 2024. URL: https://doi.org/10.1002/pro.5123, doi:10.1002/pro.5123. This article has 9 citations.

12. (collard2023geneticandpharmacological pages 2-4): Renata Collard and Tomas Majtan. Genetic and pharmacological modulation of cellular proteostasis leads to partial functional rescue of homocystinuria-causing cystathionine-beta synthase variants. Molecular and Cellular Biology, 43:664-674, Dec 2023. URL: https://doi.org/10.1080/10985549.2023.2284147, doi:10.1080/10985549.2023.2284147. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (ziegler2023inbornerrorsof pages 6-7): SG Ziegler, J Kim, and JT Ehmsen. Inborn errors of amino acid metabolism–from underlying pathophysiology to therapeutic advances. Unknown journal, 2023.

14. (majtan2023recenttherapeuticapproaches pages 4-6): Tomas Majtan, Viktor Kožich, and Warren D. Kruger. Recent therapeutic approaches to cystathionine beta‐synthase‐deficient homocystinuria. Dec 2023. URL: https://doi.org/10.1111/bph.15991, doi:10.1111/bph.15991. This article has 27 citations and is from a highest quality peer-reviewed journal.

15. (majtan2023recenttherapeuticapproaches pages 6-7): Tomas Majtan, Viktor Kožich, and Warren D. Kruger. Recent therapeutic approaches to cystathionine beta‐synthase‐deficient homocystinuria. Dec 2023. URL: https://doi.org/10.1111/bph.15991, doi:10.1111/bph.15991. This article has 27 citations and is from a highest quality peer-reviewed journal.

16. (majtan2023recenttherapeuticapproaches media c1dbb0d7): Tomas Majtan, Viktor Kožich, and Warren D. Kruger. Recent therapeutic approaches to cystathionine beta‐synthase‐deficient homocystinuria. Dec 2023. URL: https://doi.org/10.1111/bph.15991, doi:10.1111/bph.15991. This article has 27 citations and is from a highest quality peer-reviewed journal.
