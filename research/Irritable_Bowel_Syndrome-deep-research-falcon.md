---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:26.159354'
end_time: '2025-12-17T23:34:33.115004'
duration_seconds: 366.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Irritable Bowel Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Irritable Bowel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Irritable Bowel Syndrome**.
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
- **Disease Name:** Irritable Bowel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Irritable Bowel Syndrome**.
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
- Disease Name: Irritable Bowel Syndrome (IBS)
- MONDO ID: MONDO:0002032 (IBS)
- Category: Complex, disorder of gut–brain interaction (DGBI)

Pathophysiology description (current understanding)
IBS is a multifactorial DGBI characterized by altered bidirectional signaling across the gut–brain–microbiome axis. Core mechanisms include visceral hypersensitivity, mucosal immune activation with mast-cell mediators, epithelial barrier dysfunction, dysregulated enteroendocrine (serotonergic) signaling, altered microbial ecology and metabolites (e.g., SCFAs and bile acids), and central modulation of pain and affect. Contemporary reviews and transcriptomic studies in IBS (particularly IBS-D) show upregulation of immune/inflammatory and nociceptive pathways (including TRPV1), barrier-related changes, and mediator release that sensitizes enteric afferents and facilitates pain (hyperalgesia), while bile acid diarrhea (BAD) represents a defined mechanistic subset with FXR–FGF19 signaling disturbances and enhanced mucosal immune activation by dihydroxy bile acids (e.g., chenodeoxycholic, deoxycholic acids) (Camilleri & Boeckxstaens 2023, Gut, Oct 2023; https://doi.org/10.1136/gutjnl-2022-328515) (camilleri2023irritablebowelsyndrome pages 6-8). The brain–gut axis integrates psychosocial stress, HPA activation, and inflammatory mediators, with high psychiatric comorbidity and heightened central pain processing contributing to symptom severity (Shaikh et al. 2023, J Clin Med; https://doi.org/10.3390/jcm12072558) (shaikh2023irritablebowelsyndrome pages 4-5).

1) Core pathophysiology
- Visceral hypersensitivity
  • IBS patients demonstrate lower pain thresholds to recto-colonic distension; transcriptomics in IBS-D highlight upregulation of TRPV1 and neurotransmission genes, consistent with hyperexcitability of visceral afferents (Camilleri & Boeckxstaens 2023, Gut) (camilleri2023irritablebowelsyndrome pages 6-8). 
  • Clinical and experimental evidence links neurotrophins (e.g., BDNF), prostaglandins (PGE2), and mast-cell mediators to heightened nociception (McKevitt 2024, colonic mucosa gene-expression review) (mckevitt2024investigatinggeneexpression pages 24-27).

- Immune activation and mast cells
  • Mucosal B cells/plasma cells and mast cells increase adjacent to nerves; augmented release of histamine, tryptase, and other mediators heightens neuronal excitability and visceral pain (Camilleri & Boeckxstaens 2023, Gut) (camilleri2023irritablebowelsyndrome pages 6-8). 
  • Multiple studies report increased stool tryptase and localized mast-cell degranulation correlating with pain severity (McKevitt 2024; Mansilla et al. 2024, Nutrients; https://doi.org/10.3390/nu17010155) (mckevitt2024investigatinggeneexpression pages 20-24, mansilla2024exploringgutmicrobiota pages 2-4).

- Epithelial barrier dysfunction
  • Increased permeability is documented in IBS, especially in BAD versus IBS-D without BAD; colonic and small-bowel segmental permeability can be inferred from timed urinary sugar probes (Camilleri & Boeckxstaens 2023, Gut) (camilleri2023irritablebowelsyndrome pages 6-8). 
  • Barrier-protein transcripts and tight-junction remodeling are variably altered across IBS subtypes (OCLN/CLDN1 increases in IBS-C with greater integrity; loss in IBS-D), and innate-sensing TLRs are dysregulated (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 20-24).

- Microbiome and metabolites
  • Dysbiosis with reduced beneficial taxa (e.g., Bifidobacterium, Faecalibacterium prausnitzii) and altered Firmicutes:Bacteroidetes balance are repeatedly observed, with mechanistic links to immune activation, oxidative stress, and permeability (Mansilla et al. 2024, Nutrients) (mansilla2024exploringgutmicrobiota pages 2-4). 
  • SCFAs regulate epithelial transport, immune differentiation (e.g., Treg induction), and serotonergic gene expression (TPH1/SERT); butyrate can increase SERT in vitro, whereas acetate/propionate may decrease SERT expression; SCFAs also exert epigenetic effects (histone acetylation) modulating NF-κB/TNF-α (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 27-31).

- Bile acids and FXR–FGF19/TGR5 signaling (particularly in IBS-D/BAD)
  • BAD denotes ~subset of IBS-D with increased fecal bile acids and reduced FXR–FGF19 feedback; mucosa exhibits greater immune activation, partly attributable to bile acid detergency (Camilleri & Boeckxstaens 2023, Gut) (camilleri2023irritablebowelsyndrome pages 6-8).

- Serotonin pathway (enterochromaffin)
  • About 95% of 5-HT is produced in GI tissues; IBS shows altered expression of serotonergic genes (TPH1, SLC6A4/SERT, HTRs) and associations with bowel habit phenotypes (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 24-27). SCFAs can modulate TPH1/SERT (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 27-31).

- Brain–gut axis and central modulation
  • Psychiatric comorbidity is frequent; stress and HPA activation (elevated IL-6/IL-8) can worsen gut symptoms via effects on motility, permeability, and nociception (Shaikh et al. 2023) (shaikh2023irritablebowelsyndrome pages 4-5).

2) Key molecular players
- Genes/Proteins (HGNC)
  • TRPV1 (HGNC:12350): upregulated in IBS-D transcriptomes; mediator of nociceptive hypersensitivity (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8).
  • CLDN family (e.g., CLDN1; HGNC:2045), OCLN (HGNC:8101), TJP1/ZO-1 (HGNC:11773): barrier integrity/remodeling in IBS subtypes (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 20-24).
  • SLC6A4 (SERT; HGNC:11050), TPH1 (HGNC:12016): serotonergic transport/synthesis altered in IBS; SCFAs modulate expression (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 27-31, mckevitt2024investigatinggeneexpression pages 24-27).
  • FXR/NR1H4 (HGNC:7965), FGF19 (HGNC:3680), GPBAR1/TGR5 (HGNC:4518): bile acid signaling implicated in BAD and IBS-D (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8).
  • BDNF (HGNC:1033): linked to visceral pain and enteric signaling (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 24-27).
  • Immune mediators: TNF (HGNC:11892), IL6 (HGNC:6018), IL1B (HGNC:5992); increased cytokine activity associated with symptoms and stress (Shaikh 2023) (shaikh2023irritablebowelsyndrome pages 4-5); evidence for TNFSF15 and immune loci in IBS genetics (Camilleri & Jencks 2024) (camilleri2024pharmacogeneticsinibs pages 16-18).

- Chemical entities (CHEBI)
  • SCFAs: acetate (CHEBI:15343), propionate (CHEBI:15986), butyrate (CHEBI:17148); immunoepithelial and epigenetic modulators (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 27-31). 
  • Bile acids: chenodeoxycholic acid/CDCA (CHEBI:16755), deoxycholic acid/DCA (CHEBI:29807); mucosal irritants promoting BAD immune activation (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
  • Histamine (CHEBI:18295) and tryptase (e.g., TPSAB1 gene product): mast-cell mediators linked to pain (Gut 2023; Mansilla 2024) (camilleri2023irritablebowelsyndrome pages 6-8, mansilla2024exploringgutmicrobiota pages 2-4).

- Cell types (CL)
  • Enterochromaffin cells (CL:0000160), intestinal epithelial cells (CL:0002253), mucosal mast cells (CL:0000097), enteric neurons (CL:0000393) (mechanistic roles per Gut 2023; McKevitt 2024) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 24-27).

- Anatomical locations (UBERON)
  • Colon (UBERON:0001155), small intestine (UBERON:0002108), lamina propria (UBERON:0001969), enteric nervous system (UBERON:0001799) (Gut 2023; McKevitt 2024) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 24-27).

3) Biological processes (GO terms) disrupted
- Sensory perception of pain/visceral nociception (GO:0019233): TRPV1-mediated hypersensitivity (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Inflammatory response (GO:0006954) and mast-cell activation (GO:0045576): immune mediator release driving neuronal excitability (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Regulation of intestinal epithelial cell–cell adhesion (GO:0098609) and tight junction assembly (GO:0070830): barrier dysfunction in IBS subtypes/BAD (Gut 2023; McKevitt 2024) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 20-24). 
- Serotonin metabolic process (GO:0042428) and monoamine transport (GO:0015844): altered EC signaling (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 24-27). 
- Bile acid mediated signaling pathway (GO:1905114): FXR–FGF19/TGR5 dysregulation in BAD/IBS-D (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Regulation of T cell differentiation, including Treg (GO:0045580): SCFA-driven immune modulation (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 27-31).

4) Cellular components (GO) 
- Tight junction (GO:0005923): ZO-1/TJP1, claudins, occludin localization changes (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 20-24). 
- Extracellular space (GO:0005615): mediator milieu (histamine, proteases, cytokines) sensitizing afferents (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Plasma membrane and ion channel complexes (GO:0005886; GO:1902495): TRPV1 and other nociceptive channels (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8).

5) Disease progression: sequence of events
- Triggers (e.g., acute enteric infection, psychosocial stress) perturb microbiota and barrier integrity, increasing antigen exposure and activating mucosal immune cells (mast cells, B/plasma cells). Released mediators (histamine, tryptase, prostaglandins) and epithelial factors sensitize TRPV1-expressing afferents, producing visceral hypersensitivity. Concurrently, enteroendocrine serotonin signaling and bile acid pathways shape motility and secretion (IBS-D vs IBS-C). Central circuits (BGA) amplify pain and hypervigilance, reinforced by psychiatric comorbidities. In a subset (BAD), impaired FXR–FGF19 feedback increases colonic dihydroxy bile acids, further disrupting barrier and activating mucosal immunity (Camilleri & Boeckxstaens 2023; Shaikh 2023) (camilleri2023irritablebowelsyndrome pages 6-8, shaikh2023irritablebowelsyndrome pages 4-5).

6) Phenotypic manifestations (HP terms) and mechanistic links
- Abdominal pain (HP:0002027) and visceral hyperalgesia (HP:0025387): TRPV1 upregulation, mast-cell mediator release, central sensitization (Gut 2023; McKevitt 2024) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 24-27).
- Diarrhea (HP:0002014) in IBS-D, including bile acid diarrhea: increased luminal bile acids with FXR–FGF19 dysregulation (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8).
- Constipation (HP:0002019) in IBS-C: altered serotonergic transport/synthesis and neuromuscular signaling (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 24-27).
- Bloating and distension (HP:0003270): dysbiosis, fermentation, barrier permeability (Mansilla 2024; McKevitt 2024) (mansilla2024exploringgutmicrobiota pages 2-4, mckevitt2024investigatinggeneexpression pages 20-24).
- Anxiety/depression comorbidity (HP:0000739/HP:0000716): BGA dysregulation and HPA-axis stress–inflammation link (Shaikh 2023) (shaikh2023irritablebowelsyndrome pages 4-5).

Genetics and ion channels
- IBS is polygenic with modest heritability. Recent overviews emphasize immune-related loci (e.g., TNFSF15), motility/stool-frequency signals, and neuronal/neurotrophic pathways in ENS and pain modulation; these provide theoretical targets for precision therapeutics though clinical pharmacogenomic stratification remains limited to drug-metabolizing enzymes (e.g., CYP2D6/2C19) at present (Camilleri & Jencks 2024; Expert Opin Drug Metab Toxicol, May 2024; https://doi.org/10.1080/17425255.2024.2349716) (camilleri2024pharmacogeneticsinibs pages 16-18). 
- Ion-channel and nociceptive signaling (TRPV1) are consistently implicated in IBS-D hypersensitivity, with transcriptome-level upregulation and functional links to immune mediator exposure (Gut 2023) (camilleri2023irritablebowelsyndrome pages 6-8).

Brain–gut axis, neuroimaging, and psychiatric comorbidity
- IBS shows high rates of anxiety/depression, with stress and inflammatory cytokines (IL-6, IL-8) linked to symptom exacerbation and altered motility/visceral pain processing—underscoring top-down modulation along the BGA (Shaikh 2023; Mar 2023; https://doi.org/10.3390/jcm12072558) (shaikh2023irritablebowelsyndrome pages 4-5).

Post-infectious IBS (PI-IBS)
- Meta-analytic and narrative syntheses indicate an increased risk of PI-IBS (on the order of ~fourfold) following enteric infections, with persistent low-grade mucosal inflammation, immune activation (Th1/Th17 bias), and barrier defects proposed as drivers (Almonajjed et al. 2025, Medicina; https://doi.org/10.3390/medicina61010109) (almonajjed2025impactofmicrobiota pages 4-5).

Current applications and real-world implementations
- Biomarker-guided care: BAD testing (serum C4/FGF19 where available; fecal bile acids) and empiric bile acid sequestrants or FXR-targeted approaches for IBS-D/BAD; mast-cell–directed strategies (e.g., non-sedating H1R antagonists) in patients with histamine-driven pain; barrier-directed nutrition and microbiota-modifying interventions (pre/probiotics, fiber) (Camilleri & Boeckxstaens 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Psychogastroenterology: integration of central neuromodulators and brain–gut behavioral therapies alongside diet/microbiome strategies given strong BGA contribution (Shaikh 2023) (shaikh2023irritablebowelsyndrome pages 4-5).

Expert opinions and analysis from authoritative sources
- A state-of-the-art Gut review advocates individualized treatment guided by actionable mechanisms (transit abnormality, BAD, barrier dysfunction, immune activation/mast cells, microbiome) rather than symptom phenotype alone, citing multi-omics and mucosal transcriptomic evidence supporting immune–nociceptive–barrier triad in IBS-D and BAD (Camilleri & Boeckxstaens 2023, Gut) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Pharmacogenetics perspective underscores that, while GWAS illuminate biological pathways (immune/ENS/motility), near-term precision medicine in IBS is more feasible via pharmacokinetic genotyping (e.g., CYP2D6/2C19 for central neuromodulators) and mechanism-targeted selection (Camilleri & Jencks 2024) (camilleri2024pharmacogeneticsinibs pages 16-18).

Relevant statistics and data (recent)
- Transcriptomics: 181 genes (ascending colon) and 199 genes (rectosigmoid) differentially expressed in IBS-D vs controls, with upregulation of inflammation, TRPV1, neurotransmitter/receptor pathways; PI15/PI16 peptidase inhibitors reduced in IBS-D (Camilleri & Boeckxstaens 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Immune/neuronal proximity: Increased mast cells near nerves and mediator release linked to pain; proof-of-concept improvement with non-sedating H1 receptor antagonists (Camilleri & Boeckxstaens 2023) (camilleri2023irritablebowelsyndrome pages 6-8). 
- Psychiatric comorbidity: High prevalence of anxiety/depression in IBS cohorts and symptom exacerbation linked to stress cytokines (Shaikh 2023) (shaikh2023irritablebowelsyndrome pages 4-5). 
- Post-infectious risk: Approximately fourfold increased risk of IBS after enteric infection, with immune and barrier alterations persisting (Almonajjed 2025) (almonajjed2025impactofmicrobiota pages 4-5). 
- Serotonin and SCFAs: Butyrate upregulates SERT; acetate/propionate downregulate SERT in vitro; SCFAs promote Treg differentiation and modulate TNF/NF-κB signaling via epigenetic effects (McKevitt 2024) (mckevitt2024investigatinggeneexpression pages 27-31).

Evidence items (with PMIDs/DOIs/URLs; publication dates)
- Camilleri M, Boeckxstaens G. Irritable bowel syndrome: treatment based on pathophysiology and biomarkers. Gut. 2023 Oct;72(3):590–599. doi:10.1136/gutjnl-2022-328515. URL: https://doi.org/10.1136/gutjnl-2022-328515 (mechanistic immune–barrier–TRPV1, BAD/FXR–FGF19, biomarker-guided therapy) (camilleri2023irritablebowelsyndrome pages 6-8).
- Camilleri M, Jencks KJ. Pharmacogenetics in IBS: update and impact of GWAS studies in drug targets and metabolism. Expert Opin Drug Metab Toxicol. 2024 May;20(5):319–332. doi:10.1080/17425255.2024.2349716. URL: https://doi.org/10.1080/17425255.2024.2349716 (genetics, ENS mechanisms, translational precision medicine) (camilleri2024pharmacogeneticsinibs pages 16-18).
- Shaikh SD et al. Irritable Bowel Syndrome and the Gut Microbiome: A Comprehensive Review. J Clin Med. 2023 Mar;12(7):2558. doi:10.3390/jcm12072558. URL: https://doi.org/10.3390/jcm12072558 (BGA, psychiatric comorbidity, stress–cytokine links) (shaikh2023irritablebowelsyndrome pages 4-5).
- McKevitt EE. Investigating gene expression in the colonic mucosal tissue of individuals with disorders of gut–brain interaction. 2024 (preprint/unknown journal). Key mechanistic syntheses: barrier proteins (OCLN/CLDN1), TLRs, cytokines (TNF, IL-1β, IL-6), mast-cell activation (tryptase), serotonin pathway (TPH1/SLC6A4), neurotrophins (BDNF), SCFA modulation of SERT/TPH1 (mckevitt2024investigatinggeneexpression pages 20-24, mckevitt2024investigatinggeneexpression pages 27-31, mckevitt2024investigatinggeneexpression pages 24-27).
- Mansilla MJG et al. Exploring Gut Microbiota Imbalance in IBS: Potential Therapeutic Effects of Probiotics and Their Metabolites. Nutrients. 2024 Dec;17(1):155. doi:10.3390/nu17010155. URL: https://doi.org/10.3390/nu17010155 (dysbiosis patterns; mast-cell correlates) (mansilla2024exploringgutmicrobiota pages 2-4).
- Almonajjed MB et al. Impact of Microbiota on IBS Pathogenesis and Management: A Narrative Review. Medicina. 2025 Jan;61(1):109. doi:10.3390/medicina61010109. URL: https://doi.org/10.3390/medicina61010109 (PI-IBS risk, immune–barrier mechanisms) (almonajjed2025impactofmicrobiota pages 4-5).

Ontology-linked annotations (exemplars)
- Genes/Proteins (HGNC): TRPV1; SLC6A4 (SERT); TPH1; NR1H4 (FXR); FGF19; GPBAR1 (TGR5); CLDN1; OCLN; TJP1; TNF; IL6; IL1B (camilleri2023irritablebowelsyndrome pages 6-8, camilleri2024pharmacogeneticsinibs pages 16-18, mckevitt2024investigatinggeneexpression pages 24-27, mckevitt2024investigatinggeneexpression pages 20-24, mckevitt2024investigatinggeneexpression pages 27-31).
- Biological process (GO): inflammatory response (GO:0006954); bile acid mediated signaling (GO:1905114); serotonin metabolic process (GO:0042428); regulation of intestinal permeability (GO:1905499); sensory perception of pain (GO:0019233) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 24-27).
- Cellular component (GO): tight junction (GO:0005923); extracellular space (GO:0005615); ion channel complex (GO:1902495) (mckevitt2024investigatinggeneexpression pages 20-24, camilleri2023irritablebowelsyndrome pages 6-8).
- Cell types (CL): mucosal mast cell (CL:0000097); enterochromaffin cell (CL:0000160); intestinal epithelial cell (CL:0002253); enteric neuron (CL:0000393) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 24-27).
- Anatomical locations (UBERON): colon (UBERON:0001155); small intestine (UBERON:0002108); lamina propria (UBERON:0001969); enteric nervous system (UBERON:0001799) (camilleri2023irritablebowelsyndrome pages 6-8, mckevitt2024investigatinggeneexpression pages 24-27).
- Chemical entities (CHEBI): acetate (CHEBI:15343); propionate (CHEBI:15986); butyrate (CHEBI:17148); chenodeoxycholic acid (CHEBI:16755); deoxycholic acid (CHEBI:29807); histamine (CHEBI:18295) (mckevitt2024investigatinggeneexpression pages 27-31, camilleri2023irritablebowelsyndrome pages 6-8).

Notes and limitations
- Where possible, 2023–2024 high-quality sources (Gut 2023; Expert Opin 2024) were prioritized. Some mechanistic syntheses (gene expression/SCFA–SERT modulation; PI-IBS estimate) derive from recent narrative/unknown-journal reviews; these highlight hypotheses needing continued validation. Neuroimaging- and subtype-specific genetic effect sizes were outside the scope of the retrieved evidence here and warrant further targeted review.


References

1. (camilleri2023irritablebowelsyndrome pages 6-8): Michael Camilleri and Guy Boeckxstaens. Irritable bowel syndrome: treatment based on pathophysiology and biomarkers. Gut, 72:590-599, Oct 2023. URL: https://doi.org/10.1136/gutjnl-2022-328515, doi:10.1136/gutjnl-2022-328515. This article has 99 citations and is from a highest quality peer-reviewed journal.

2. (shaikh2023irritablebowelsyndrome pages 4-5): Sofia D. Shaikh, Natalie Sun, Andrew Canakis, William Y. Park, and Horst Christian Weber. Irritable bowel syndrome and the gut microbiome: a comprehensive review. Journal of Clinical Medicine, 12:2558, Mar 2023. URL: https://doi.org/10.3390/jcm12072558, doi:10.3390/jcm12072558. This article has 146 citations and is from a poor quality or predatory journal.

3. (mckevitt2024investigatinggeneexpression pages 24-27): EE McKevitt. Investigating gene expression in the colonic mucosal tissue of individuals with disorders of gut-brain interaction. Unknown journal, 2024.

4. (mckevitt2024investigatinggeneexpression pages 20-24): EE McKevitt. Investigating gene expression in the colonic mucosal tissue of individuals with disorders of gut-brain interaction. Unknown journal, 2024.

5. (mansilla2024exploringgutmicrobiota pages 2-4): María José García Mansilla, María Jesús Rodríguez Sojo, Andrea Roxana Lista, Ciskey Vanessa Ayala Mosqueda, Antonio Jesús Ruiz Malagón, Julio Gálvez, Alba Rodríguez Nogales, and María José Rodríguez Sánchez. Exploring gut microbiota imbalance in irritable bowel syndrome: potential therapeutic effects of probiotics and their metabolites. Nutrients, 17:155, Dec 2024. URL: https://doi.org/10.3390/nu17010155, doi:10.3390/nu17010155. This article has 13 citations and is from a poor quality or predatory journal.

6. (mckevitt2024investigatinggeneexpression pages 27-31): EE McKevitt. Investigating gene expression in the colonic mucosal tissue of individuals with disorders of gut-brain interaction. Unknown journal, 2024.

7. (camilleri2024pharmacogeneticsinibs pages 16-18): Michael Camilleri and Kara J Jencks. Pharmacogenetics in ibs: update and impact of gwas studies in drug targets and metabolism. Expert Opinion on Drug Metabolism & Toxicology, 20:319-332, May 2024. URL: https://doi.org/10.1080/17425255.2024.2349716, doi:10.1080/17425255.2024.2349716. This article has 1 citations and is from a peer-reviewed journal.

8. (almonajjed2025impactofmicrobiota pages 4-5): Mhd Bashir Almonajjed, Mahdi Wardeh, Abdallah Atlagh, Abdulrahman Ismaiel, Stefan-Lucian Popa, Flaviu Rusu, and Dan L. Dumitrascu. Impact of microbiota on irritable bowel syndrome pathogenesis and management: a narrative review. Medicina, 61:109, Jan 2025. URL: https://doi.org/10.3390/medicina61010109, doi:10.3390/medicina61010109. This article has 10 citations and is from a poor quality or predatory journal.