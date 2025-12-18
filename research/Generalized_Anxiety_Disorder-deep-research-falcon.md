---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:38.454527'
end_time: '2025-12-17T23:35:46.213274'
duration_seconds: 427.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Generalized Anxiety Disorder
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Generalized Anxiety Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Generalized Anxiety Disorder**.
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
- **Disease Name:** Generalized Anxiety Disorder
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Generalized Anxiety Disorder**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Generalized Anxiety Disorder (GAD)
- MONDO ID: MONDO_0001627 (Generalized anxiety disorder)
- Category: Complex

Pathophysiology overview
GAD arises from convergent dysfunction across inhibitory GABAergic signaling, monoaminergic (serotonergic/noradrenergic) modulation, stress-endocrine (HPA) axis regulation, glutamatergic plasticity, and immune–inflammatory pathways that remodel cortico-limbic threat circuits (amygdala–prefrontal cortex–hippocampus and bed nucleus of the stria terminalis, BNST). Large-scale multi-ancestry and European-ancestry GWAS map common-variant liability to dozens of loci enriched in brain-expressed genes and prioritize GABAergic mechanisms; EWAS and peripheral biomarker data point to stress-related epigenetic and oxidative signatures; imaging and electrophysiology indicate altered large-scale network connectivity and beta/gamma-band abnormalities. The gut–brain axis may modulate HPA signaling and systemic inflammation in anxiety. (friligkou2024genediscoveryand pages 1-3, strom2024genomewideassociationstudy pages 1-3, tomasi2024geneticinvestigationof pages 47-50, cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)

1) Core pathophysiology
- Inhibitory signaling deficits: GWAS meta-analyses identify 58 genome-wide variants and 66 supported genes for anxiety disorders, with follow-up analyses highlighting GABAergic signaling enrichment across major brain regions, consistent with impaired inhibitory control of threat circuits. This supports longstanding models of reduced GABA-A receptor–mediated inhibition within amygdala–PFC networks. URL: https://doi.org/10.1101/2024.07.03.24309466 (posted Jul 3, 2024). (strom2024genomewideassociationstudy pages 1-3)
- Monoaminergic dysregulation: Reviews and candidate-gene syntheses implicate serotonergic transporters and receptors (SLC6A4/5-HTTLPR, HTR1A/HTR2A), norepinephrine/adrenergic genes, and dopaminergic regulators, aligning with SSRI/SNRI efficacy and noradrenergic arousal in anxiety. (tomasi2024geneticinvestigationof pages 47-50, merkouris2025molecularbasisof pages 1-2)
- HPA-axis and cortisol: Chronic stress and impaired glucocorticoid feedback are repeatedly linked to anxiety pathophysiology; peripheral studies show elevated cortisol and blunted regulation in subsets; meta-analytic evidence indicates probiotics can modestly reduce cortisol, consistent with gut–brain modulation of HPA tone. URL (Nutrients meta-analysis Oct 2024): https://doi.org/10.3390/nu16203564. (merkouris2025molecularbasisof pages 1-2)
- Glutamatergic plasticity: Converging reviews implicate glutamatergic signaling and synaptic plasticity (e.g., NTRK2/BDNF pathways from GWAS; circuit-level extinction learning under glucocorticoid modulation). (tomasi2024geneticinvestigationof pages 47-50, merkouris2025molecularbasisof pages 1-2)
- Immune–inflammatory/oxidative stress: Clinical data in GAD demonstrate increased oxidative stress markers (elevated malondialdehyde/lipid hydroperoxides, reduced SOD/CAT/GSH-Px), which correlate with symptom severity and change with SSRI treatment; immune signaling and neuroinflammation are implicated as modulators of anxiety circuits. Preprint/early publication with URL: https://doi.org/10.1101/2024.09.07.24313247. (cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)

2) Key molecular players
- Genes/Proteins (HGNC): 
  • GABA-A receptor subunits (e.g., GABRA1, GABRA2, GABRA3, GABRA5, GABRG1, GABRG3) prioritized via genetic enrichment and pharmacological relevance. (strom2024genomewideassociationstudy pages 1-3)
  • Serotonergic system: SLC6A4, HTR1A/HTR2A; noradrenergic: ADRA1A/ADRB2; dopaminergic: COMT/DAT1 (candidate synthesis). (tomasi2024geneticinvestigationof pages 47-50)
  • Neurotrophin signaling: NTRK2/BDNF implicated in GWAS/linkage and mechanistic models of plasticity. (tomasi2024geneticinvestigationof pages 47-50)
  • HPA-axis regulators: NR3C1 (GR), CRHR1; FKBP5 (candidate/epigenetic literature). (merkouris2025molecularbasisof pages 1-2, tomasi2024geneticinvestigationof pages 47-50)
- Chemical entities (CHEBI): GABA, serotonin (5-HT), norepinephrine, cortisol; oxidative markers malondialdehyde (MDA), lipid hydroperoxides; antioxidants SOD, catalase, glutathione peroxidase. (cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)
- Cell types (CL): Cortical and amygdala parvalbumin-positive GABAergic interneurons (drivers of gamma oscillations) and principal glutamatergic pyramidal neurons; microglia as mediators of neuroinflammation. (merkouris2025molecularbasisof pages 1-2)
- Anatomical locations (UBERON): Amygdala, hippocampus, medial/ventromedial/dorsomedial prefrontal cortex, anterior cingulate cortex, thalamus, BNST; large-scale networks include salience and default mode networks. (strom2024genomewideassociationstudy pages 1-3, merkouris2025molecularbasisof pages 1-2)

3) Biological processes (GO terms)
- Synaptic signaling and inhibition: GABAergic synaptic transmission; regulation of membrane potential; inhibitory postsynaptic potential. (strom2024genomewideassociationstudy pages 1-3)
- Monoaminergic neurotransmission: serotonin transport and receptor signaling; adrenergic receptor signaling. (tomasi2024geneticinvestigationof pages 47-50)
- Stress response: response to glucocorticoid; regulation of HPA axis; response to cortisol; fear learning and extinction. (merkouris2025molecularbasisof pages 1-2)
- Neuroinflammation/immune signaling: microglial activation; cytokine-mediated signaling pathway; oxidative stress response; cellular response to reactive oxygen species. (cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)
- Synaptic plasticity: long-term potentiation/depression; neurotrophin/TrkB signaling. (tomasi2024geneticinvestigationof pages 47-50)

4) Cellular components (GO-CC)
- GABA-A receptor complex at inhibitory synapse; postsynaptic density; presynaptic active zone.
- Glucocorticoid receptor complex (cytosol/nucleus); mitochondrial membrane (oxidative stress sites).
- Extracellular space/plasma and saliva (peripheral cortisol and inflammatory markers). (cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)

5) Disease progression (conceptual sequence)
- Predisposition: Polygenic risk distributed across 51–58 loci (multi-ancestry and European GWAS) enriched in brain-expressed genes, with notable GABAergic involvement. URL Nature Genetics (Sep 2024): https://doi.org/10.1038/s41588-024-01908-2; medRxiv (Jul 2024): https://doi.org/10.1101/2024.07.03.24309466. (friligkou2024genediscoveryand pages 1-3, strom2024genomewideassociationstudy pages 1-3)
- Environmental inputs: Early-life stress and chronic psychosocial stress engage HPA, induce epigenetic changes (e.g., NR3C1 methylation), and promote inflammatory/oxidative states. (merkouris2025molecularbasisof pages 1-2)
- Circuit remodeling: Reduced inhibitory control (GABAergic interneuron dysfunction) and altered monoaminergic gain destabilize amygdala–PFC–hippocampal/BST circuits, biasing threat appraisal and sustained anxiety; network-level dysconnectivity emerges. (strom2024genomewideassociationstudy pages 1-3, merkouris2025molecularbasisof pages 1-2)
- Clinical manifestation: Persistent, excessive worry, hyperarousal, and somatic symptoms; peripheral biomarkers show elevated oxidative stress and sometimes altered cortisol. (cui2025oxidativestressmarkers pages 11-13, bamalan2023generalizedanxietydisorder pages 3-6)

6) Phenotypic manifestations (HP terms)
- Excessive worry and anxiety (HP:0000739), restlessness (HP:0000711), sleep disturbance/insomnia (HP:0100785), concentration impairment (HP:0100543), autonomic hyperarousal (e.g., palpitations HP:0001962, sweating HP:0000975), muscle tension (HP:0001371). (bamalan2023generalizedanxietydisorder pages 3-6)

Recent developments (2023–2024 priority)
- Multi-ancestry GWAS in Nature Genetics (Sep 2024): Identified 51 loci (39 novel), with heritability enrichment in limbic system, cortex, cerebellum; cross-ancestry PRS transferability; 115 transcriptome/proteome-nominated genes, mapping risk to brain systems implicated in anxiety. URL: https://doi.org/10.1038/s41588-024-01908-2. (friligkou2024genediscoveryand pages 1-3)
- European mega-GWAS (Jul 2024): 58 independent loci, 66 genes, replicated 51/58 in 1.17M cases; pathway enrichment highlights GABAergic signaling; broad brain enrichment supports systems-level liability. URL: https://doi.org/10.1101/2024.07.03.24309466. (strom2024genomewideassociationstudy pages 1-3)
- EWAS of anxiety disorders (Aug 2023): Methylome-wide analysis across anxiety phenotypes demonstrates DNAm associations, supporting stress-related epigenetic involvement in anxiety biology. URL: https://doi.org/10.1038/s41380-023-02205-w. (tomasi2024geneticinvestigationof pages 47-50)
- Biomarkers and electrophysiology/imaging updates:
  • EEG in GAD (Scientific Reports 2025): Increased beta power and reduced fronto-temporal and fronto-parietal/occipital connectivity, plus rightward temporal alpha asymmetry, provide candidate electrophysiological markers of altered excitatory–inhibitory balance and network integration. URL: https://doi.org/10.1038/s41598-025-90362-z. (merkouris2025molecularbasisof pages 1-2)
  • World Psychiatry 2023 biomarker state-of-field review: Identifies error-related negativity (ERN) as a promising predictive biomarker for first-onset GAD, while overall emphasizing the lack of clinically validated markers and the need for rigorous validation. URL: https://doi.org/10.1002/wps.21078 (May 2023). (merkouris2025molecularbasisof pages 1-2)
  • Probiotics and cortisol (Nutrients 2024 meta-analysis): Across 46 RCTs (n=3516), probiotics modestly reduce cortisol (SMD −0.45; low certainty), consistent with gut–brain–HPA modulation but underscoring heterogeneity. URL: https://doi.org/10.3390/nu16203564 (Oct 2024). (merkouris2025molecularbasisof pages 1-2)
- Oxidative stress in GAD and treatment response (2024/2025): Elevated baseline MDA/LPO and reduced antioxidant enzymes correlate with symptom severity; changes track SSRI response with ROC AUC ~0.80 for baseline MDA predicting response. URL: https://doi.org/10.1101/2024.09.07.24313247. (cui2025oxidativestressmarkers pages 11-13)

Circuits, networks, and cell types
- Threat and sustained anxiety circuitry: Dysregulation in amygdala–mPFC–hippocampus and BNST underpins exaggerated threat appraisal and persistent anxiety; genetic enrichment across broad brain regions supports network-level liability. (strom2024genomewideassociationstudy pages 1-3, friligkou2024genediscoveryand pages 1-3)
- Large-scale networks: Altered connectivity within salience and default-mode networks is consistent with hypervigilance and perseverative cognition. Multicenter rs-fMRI in anxiety disorders reports insula–thalamus increases and midbrain–cortical dysconnectivity, with disorder-specific patterns; these findings align with GAD literature on cortico-limbic dysconnectivity. (merkouris2025molecularbasisof pages 1-2)
- Cell types: PV+ GABA interneuron dysfunction is a cross-disorder model for gamma-band changes; microglial activation and neuroinflammation are implicated via TSPO literature and preclinical anxiolytics modulating neurosteroids/microglia. (merkouris2025molecularbasisof pages 1-2)

Applications and real-world implementations
- Genetic risk and target nomination: The 2024 GWASs provide prioritized genes and pathways for functional follow-up (e.g., GABA-A receptor subunits) and potential stratification in clinical trials. (strom2024genomewideassociationstudy pages 1-3, friligkou2024genediscoveryand pages 1-3)
- Biomarker development: ERN for GAD risk prediction; EEG beta/gamma and connectivity metrics as candidate markers; however, current consensus emphasizes limited clinical readiness and the need for validation pipelines. (merkouris2025molecularbasisof pages 1-2)
- Adjunctive strategies: Gut–brain axis modulation (diet/probiotics) may modestly influence HPA and symptomatology; peripheral oxidative stress panels (e.g., MDA, antioxidant enzymes) show promise for monitoring and response prediction but require replication. (cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)

Expert opinions and authoritative analyses
- World Psychiatry consensus (2023) stresses the gap between numerous candidate biomarkers and a paucity of clinically validated tools; prioritizes definitive testing of a limited set (e.g., ERN for GAD onset prediction). URL: https://doi.org/10.1002/wps.21078. (merkouris2025molecularbasisof pages 1-2)
- Translational reviews highlight heterogeneity and advocate cross-species and computational models to bridge mechanisms and clinical phenotypes in anxiety. URL: https://doi.org/10.3758/s13415-024-01162-3 (Feb 2024). (merkouris2025molecularbasisof pages 1-2)

Relevant statistics and data
- Common-variant risk: 51 loci identified (39 novel) in multi-ancestry GWAS (Nature Genetics 2024) and 58 loci in European mega-GWAS (medRxiv 2024), with replication of 51/58 variants in an independent 1.17M-case dataset; enrichment in GABAergic signaling and brain-wide expression. (friligkou2024genediscoveryand pages 1-3, strom2024genomewideassociationstudy pages 1-3)
- Epigenetics: Methylome-wide associations observed for anxiety disorders (Molecular Psychiatry 2023), supporting systemic stress-related DNAm signatures; specific CpGs vary across cohorts. (tomasi2024geneticinvestigationof pages 47-50)
- Electrophysiology: In GAD, increased beta activity and decreased long-range connectivity (fronto–temporal/parietal/occipital), plus rightward alpha asymmetry, suggesting altered E/I balance and network integration. (merkouris2025molecularbasisof pages 1-2)
- Oxidative stress: Baseline serum MDA ROC AUC ~0.80 for SSRI response; group differences and correlations with severity reported (details above). (cui2025oxidativestressmarkers pages 11-13)
- Gut–brain/HPA: Probiotics meta-analysis shows cortisol reduction SMD −0.45 (low certainty) across 46 RCTs. (merkouris2025molecularbasisof pages 1-2)

Ontology-style annotations (examples)
- Genes/Proteins (HGNC): GABRA1, GABRA2, GABRA3, GABRA5, GABRG1, GABRG3; SLC6A4; HTR1A; HTR2A; NTRK2; BDNF; NR3C1; CRHR1; FKBP5. (strom2024genomewideassociationstudy pages 1-3, tomasi2024geneticinvestigationof pages 47-50, merkouris2025molecularbasisof pages 1-2)
- Biological processes (GO): GABAergic synaptic transmission; serotonergic signaling pathway; adrenergic receptor signaling; response to glucocorticoid; regulation of synaptic plasticity; microglial activation; response to oxidative stress. (strom2024genomewideassociationstudy pages 1-3, tomasi2024geneticinvestigationof pages 47-50, cui2025oxidativestressmarkers pages 11-13)
- Cellular components (GO-CC): GABA-A receptor complex; postsynaptic density; cytosol/nuclear GR complex; mitochondrial membrane. (strom2024genomewideassociationstudy pages 1-3, cui2025oxidativestressmarkers pages 11-13)
- Cell types (CL): Parvalbumin-expressing GABAergic interneuron; glutamatergic pyramidal neuron; microglial cell. (merkouris2025molecularbasisof pages 1-2)
- Anatomical (UBERON): Amygdala (UBERON:0001872), hippocampus (UBERON:0001954), prefrontal cortex (UBERON:0001870), anterior cingulate cortex (UBERON:0001873), thalamus (UBERON:0001897), BNST (UBERON:0001882). (strom2024genomewideassociationstudy pages 1-3, friligkou2024genediscoveryand pages 1-3)
- Chemical entities (CHEBI): gamma-aminobutyric acid; serotonin; norepinephrine; cortisol; malondialdehyde. (cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)
- Phenotypes (HP): Anxiety (HP:0000739), Insomnia (HP:0100785), Palpitations (HP:0001962), Sweating (HP:0000975), Muscle hypotonia/tension as applicable. (bamalan2023generalizedanxietydisorder pages 3-6)

Evidence items with links
- Friligkou et al., Nature Genetics, Sep 2024: https://doi.org/10.1038/s41588-024-01908-2. Multi-ancestry GWAS; 51 loci; limbic/cortical enrichment; PRS transferability. (friligkou2024genediscoveryand pages 1-3)
- Strom et al., medRxiv, Jul 2024: https://doi.org/10.1101/2024.07.03.24309466. European mega-GWAS; 58 loci; GABAergic enrichment; 51/58 replicated. (strom2024genomewideassociationstudy pages 1-3)
- Hettema et al., Molecular Psychiatry, Aug 2023: https://doi.org/10.1038/s41380-023-02205-w. Methylome-wide association in anxiety disorders. (tomasi2024geneticinvestigationof pages 47-50)
- Abi-Dargham et al., World Psychiatry, May 2023: https://doi.org/10.1002/wps.21078. Biomarker state-of-field; ERN identified for GAD onset prediction. (merkouris2025molecularbasisof pages 1-2)
- Jain et al., Nutrients, Oct 2024: https://doi.org/10.3390/nu16203564. Probiotics meta-analysis: cortisol reduction (SMD −0.45). (merkouris2025molecularbasisof pages 1-2)
- Cui et al., medRxiv/Neuropsychobiology 2025: https://doi.org/10.1101/2024.09.07.24313247. Oxidative stress markers in GAD; treatment response prediction AUC ~0.80. (cui2025oxidativestressmarkers pages 11-13)

Limitations and open questions
- Heterogeneity across anxiety phenotypes and comorbidities complicates disorder-specific inference; many biomarkers remain preclinical or unvalidated clinically. (merkouris2025molecularbasisof pages 1-2)
- EWAS signals require replication and tissue-specific mechanistic mapping; directionality of cortisol alterations varies with context and sampling.

Conclusion
Current evidence places GAD within a polygenic, circuit-level disorder of inhibitory control, monoaminergic modulation, and stress endocrine regulation, with immune–oxidative processes and gut–brain interactions as modulators. Genetic findings newly prioritize GABAergic signaling; electrophysiological and imaging markers reflect altered network dynamics; peripheral oxidative and endocrine signatures show potential for monitoring. Continued multi-omic, longitudinal, and mechanistic studies are needed to translate these convergences into validated biomarkers and precision therapeutics. (friligkou2024genediscoveryand pages 1-3, strom2024genomewideassociationstudy pages 1-3, tomasi2024geneticinvestigationof pages 47-50, cui2025oxidativestressmarkers pages 11-13, merkouris2025molecularbasisof pages 1-2)

References

1. (friligkou2024genediscoveryand pages 1-3): Eleni Friligkou, Solveig Løkhammer, Brenda Cabrera-Mendoza, Jie Shen, Jun He, Giovanni Deiana, Mihaela Diana Zanoaga, Zeynep Asgel, Abigail Pilcher, Luciana Di Lascio, Ana Makharashvili, Dora Koller, Daniel S. Tylee, Gita A. Pathak, and Renato Polimanti. Gene discovery and biological insights into anxiety disorders from a large-scale multi-ancestry genome-wide association study. Nature genetics, 56:2036-2045, Sep 2024. URL: https://doi.org/10.1038/s41588-024-01908-2, doi:10.1038/s41588-024-01908-2. This article has 50 citations and is from a highest quality peer-reviewed journal.

2. (strom2024genomewideassociationstudy pages 1-3): Nora I. Strom, Brad Verhulst, Silviu-Alin Bacanu, Rosa Cheesman, Kirstin L. Purves, Hüseyin Gedik, Brittany L. Mitchell, Alex S. Kwong, Annika B. Faucon, Kritika Singh, Sarah Medland, Lucia Colodro-Conde, Kristi Krebs, Per Hoffmann, Stefan Herms, Jan Gehlen, Stephan Ripke, Swapnil Awasthi, Teemu Palviainen, Elisa M. Tasanko, Roseann E. Peterson, Daniel E. Adkins, Andrey A. Shabalin, Mark J. Adams, Matthew H. Iveson, Archie Campbell, Laurent F. Thomas, Bendik S. Winsvold, Ole Kristian Drange, Sigrid Børte, Abigail R. ter Kuile, Tan-Hoang Nguyen, Sandra M. Meier, Elizabeth C. Corfield, Laurie Hannigan, Daniel F. Levey, Darina Czamara, Heike Weber, Karmel W. Choi, Giorgio Pistis, Baptiste Couvy-Duchesne, Sandra Van der Auwera, Alexander Teumer, Robert Karlsson, Miguel Garcia-Argibay, Donghyung Lee, Rujia Wang, Ottar Bjerkeset, Eystein Stordal, Julia Bäckmann, Giovanni A. Salum, Clement C. Zai, James L. Kennedy, Gwyneth Zai, Arun K. Tiwari, Stefanie Heilmann-Heimbach, Börge Schmidt, Jaakko Kaprio, Martin M. Kennedy, Joseph Boden, Alexandra Havdahl, Christel M. Middeldorp, Fabiana L. Lopes, Nirmala Akula, Francis J. McMahon, Elisabeth B. Binder, Lydia Fehm, Andreas Ströhle, Enrique Castelao, Henning Tiemeier, Dan J. Stein, David Whiteman, Catherine Olsen, Zachary Fuller, Xin Wang, Naomi R. Wray, Enda M. Byrne, Glyn Lewis, Nicholas J. Timpson, Lea K. Davis, Ian B. Hickie, Nathan A. Gillespie, Lili Milani, Johannes Schumacher, David P. Woldbye, Andreas J. Forstner, Markus M. Nöthen, Iiris Hovatta, John Horwood, William E. Copeland, Hermine H. Maes, Andrew M. McIntosh, Ole A. Andreassen, John-Anker Zwart, Ole Mors, Anders D. Børglum, Preben B. Mortensen, Helga Ask, Ted Reichborn-Kjennerud, Jackob M. Najman, Murray B. Stein, Joel Gelernter, Yuri Milaneschi, Brenda W. Penninx, Dorret I. Boomsma, Eduard Maron, Angelika Erhardt-Lehmann, Christian Rück, Tilo T. Kircher, Christiane A. Melzig, Georg W. Alpers, Volker Arolt, Katharina Domschke, Jordan W. Smoller, Martin Preisig, Nicholas G. Martin, Michelle K. Lupton, Annemarie I. Luik, Andreas Reif, Hans J. Grabe, Henrik Larsson, Patrik K. Magnusson, Albertine J. Oldehinkel, Catharina A. Hartman, Gerome Breen, Anna R. Docherty, Hilary Coon, Rupert Conrad, Kelli Lehto, Jürgen Deckert, Thalia C. Eley, Manuel Mattheisen, and John M. Hettema. Genome-wide association study of major anxiety disorders in 122,341 european-ancestry cases identifies 58 loci and highlights gabaergic signaling. MedRxiv, Jul 2024. URL: https://doi.org/10.1101/2024.07.03.24309466, doi:10.1101/2024.07.03.24309466. This article has 19 citations.

3. (tomasi2024geneticinvestigationof pages 47-50): J Tomasi. Genetic investigation of physiological phenotypes to understand anxiety mechanisms. Unknown journal, 2024.

4. (cui2025oxidativestressmarkers pages 11-13): Lijun Cui, Jingjing Lu, Zhongxia Shen, Jielin Zhu, Huanxin Chen, Shenliang Yang, Shikai Wang, and Xinhua Shen. Oxidative stress markers predict treatment outcomes in patients with generalized anxiety disorder treated with selective serotonin reuptake inhibitors. Neuropsychobiology, pages 1-19, Sep 2025. URL: https://doi.org/10.1101/2024.09.07.24313247, doi:10.1101/2024.09.07.24313247. This article has 3 citations and is from a peer-reviewed journal.

5. (merkouris2025molecularbasisof pages 1-2): Ermis Merkouris, Alexandra Brasinika, Meropi Patsiavoura, Chrysanthi Siniosoglou, Dimitrios Tsiptsios, Andreas S. Triantafyllis, Christoph Mueller, Ioulia Mpikou, Myrto T. Samara, Nikolaos Christodoulou, and Konstantinos Tsamakis. Molecular basis of anxiety: a comprehensive review of 2014–2024 clinical and preclinical studies. International Journal of Molecular Sciences, 26:5417, Jun 2025. URL: https://doi.org/10.3390/ijms26115417, doi:10.3390/ijms26115417. This article has 2 citations and is from a poor quality or predatory journal.

6. (bamalan2023generalizedanxietydisorder pages 3-6): Omar Abdulqader Bamalan, Nader Mohammed Alosaimi, Abdulrahman Abdulrazzaq Alfryyan, Hussain Jawad Aljubran, Faris Hamoud Alanazi, and Zaheenul Islam Siddiqui. Generalized anxiety disorder: a review of current literature in saudi arabia. Psychology, 14:35-51, Jan 2023. URL: https://doi.org/10.4236/psych.2023.141003, doi:10.4236/psych.2023.141003. This article has 8 citations and is from a poor quality or predatory journal.