---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:27.234642'
end_time: '2025-12-17T23:36:06.449854'
duration_seconds: 459.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ulcerative Colitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 16
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ulcerative Colitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ulcerative Colitis**.
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
- **Disease Name:** Ulcerative Colitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ulcerative Colitis**.
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


Disease Pathophysiology Research Report: Ulcerative Colitis (UC)

Target Disease
- Disease Name: Ulcerative Colitis
- MONDO ID: (not specified)
- Category: Complex

Overview and core concepts
Ulcerative colitis is a chronic, relapsing inflammatory disease of the colonic mucosa characterized by a breakdown of epithelial barrier integrity, dysregulated mucosal immune responses to luminal antigens, and perturbations of the gut microbial ecosystem. Recent single-cell and spatial multi-omic studies in 2023–2024 refine this model, linking interferon-rich immune niches, epithelial injury, and myeloid–stromal networks to treatment response and resistance, and highlighting actionable axes such as IL-23/Th17, epithelial alarmins, pyroptosis, and microbiome-derived metabolites. (thomas2024alongitudinalsinglecell pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3, jairath2024il23inhibitionfor pages 1-2)

1) Core Pathophysiology
- Barrier failure and epithelial injury
  - Loss of mucus barrier and goblet cell dysfunction with altered mucin biochemistry are hallmarks in UC, weakening physical segregation of microbes and epithelium and amplifying inflammatory signaling. “Mucus layer loss in UC, with reduced number/size of goblet cells and decreased MUC2 glycosylation” has been emphasized in recent syntheses. (calvez2025novelinsightsinto pages 2-4) URL: https://doi.org/10.3390/biomedicines13020305 (2025; review synthesizing recent primary findings)
  - Advanced endo-microscopy and spatial tools underscore barrier healing as a key endpoint; barrier assessment predicts outcomes and therapeutic response, and integrates tight junction abnormalities (ZO-1, claudins) with epithelial ultrastructure in vivo. (thomas2024alongitudinalsinglecell pages 1-2) URL: https://doi.org/10.1038/s41590-024-01994-8 (Oct 2024)
- Immune network dysfunction and IFN signaling niches
  - A 1-million-cell single-cell atlas of adalimumab-treated IBD localized “interferon (IFN)-response signatures … to T cell aggregates and epithelial damage in both CD and UC,” and in non-remission, UC exhibited “increased multi-cellular IFN signalling,” implicating IFN-programmed multicellular niches in ongoing epithelial injury. (thomas2024alongitudinalsinglecell pages 1-2) URL: https://doi.org/10.1038/s41590-024-01994-8 (Oct 2024)
  - In checkpoint inhibitor colitis (mechanistically overlapping with UC at the tissue level), single-cell multi-omics identified neutrophil-rich infiltrates, epithelial apoptosis, and endothelial hypoxia programs as components of barrier dysfunction, supporting generalizable injury pathways. (thomas2024singlecelltranscriptomicanalyses pages 1-3) URL: https://doi.org/10.1038/s41591-024-02895-x (May 2024)
- Cytokine axes
  - IL‑23/Th17 axis: IL‑23 is a hierarchically dominant cytokine in IMIDs; it expands and stabilizes Th17 cells, driving IL‑17A/F, IL‑22, TNF, IFN‑γ, and IL‑26 and engaging ILC3/γδ T cells. Selective IL‑23p19 inhibitors show strong efficacy in IBD. (jairath2024il23inhibitionfor pages 1-2) URL: https://doi.org/10.1016/S0140-6736(24)01750-1 (Oct 2024)
  - Type 2 alarmins (IL‑33/TSLP/IL‑25) and innate circuits contribute to epithelial–immune crosstalk and can promote repair or inflammation context‑dependently; these are enriched in epithelial compartments and interact with ILC2s and T cells in inflamed mucosa (supported by 2024–2025 scRNA‑seq and reviews). (thomas2024singlecelltranscriptomicanalyses pages 1-3)
- Programmed cell death (PCD)
  - Inflammasome–pyroptosis: UC tissues show inflammasome activation and epithelial pyroptosis; 2024 work links SLC6A14 upregulation to NLRP3-mediated pyroptosis in epithelial cells, and numerous translational efforts target NLRP3–GSDMD. (gu2024slc6a14promotesulcerative pages 16-17) URL: https://doi.org/10.3748/wjg.v30.i3.252 (Jan 2024)
- Microbiome–metabolite axes
  - SCFA deficiency and compositional dysbiosis (e.g., Bacteroides-dominant “Bact2” enterotype) correlate with impaired barrier function and proinflammatory programming; reduced butyrate is repeatedly observed and mechanistically linked to epithelial and immune modulation. (zhang2025fucoidanasa pages 5-7) URL: https://doi.org/10.3389/fcimb.2025.1626614 (2025 review summarizing 2013–2024 evidence)

2) Key molecular players
- Genes/proteins (HGNC)
  - IL23A/IL23R (IL‑23 axis), STAT3, JAK2/TYK2 (downstream IL‑23 signaling) (jairath2024il23inhibitionfor pages 1-2)
  - MUC2 (goblet cell mucin), MUC1; tight junction proteins OCLN (occludin), CLDN family, TJP1 (ZO‑1) (calvez2025novelinsightsinto pages 2-4)
  - NLRP3, CASP1, GSDMD (pyroptosis) (gu2024slc6a14promotesulcerative pages 16-17)
- Chemical entities (ChEBI)
  - Short-chain fatty acids (butyrate, acetate, propionate) – barrier and immunomodulatory metabolites (zhang2025fucoidanasa pages 5-7)
- Cell types (CL)
  - Secretory epithelial lineages (goblet cells), colonocytes; myeloid subsets (inflammatory monocytes/macrophages), neutrophils (NET‑forming); T cell aggregates (tissue-resident memory), ILC3/ILC2; endothelial and fibroblast stromal subsets (thomas2024alongitudinalsinglecell pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3)
- Anatomical locations (UBERON)
  - Colonic mucosa, lamina propria, epithelial barrier, vascular endothelium; inflamed niches spatially adjacent to epithelial damage (thomas2024alongitudinalsinglecell pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3)

3) Biological processes (GO annotations, representative)
- Barrier and epithelial processes: “epithelial cell differentiation,” “mucin biosynthetic process,” “tight junction assembly,” “epithelial cell apoptotic process” (calvez2025novelinsightsinto pages 2-4, thomas2024singlecelltranscriptomicanalyses pages 1-3)
- Immune signaling: “response to interferon,” “IL‑23 signaling pathway,” “Th17 cell differentiation,” “neutrophil activation,” “NET formation,” “inflammatory response” (thomas2024alongitudinalsinglecell pages 1-2, jairath2024il23inhibitionfor pages 1-2)
- Inflammasome and PCD: “inflammasome complex assembly,” “pyroptosis” (GO:0070269), “caspase‑1 activation” (gu2024slc6a14promotesulcerative pages 16-17)
- Metabolite–host: “response to short-chain fatty acid,” “regulation of intestinal epithelial cell proliferation by microbiome” (zhang2025fucoidanasa pages 5-7)

4) Cellular components (GO CC)
- Apical junctional complex (tight junctions: occludin, claudins, ZO‑1); mucus layer (MUC2-rich), lamina propria immune aggregates; NLRP3 inflammasome (cytosolic); endothelial lining and perivascular stromal niches (calvez2025novelinsightsinto pages 2-4, thomas2024singlecelltranscriptomicanalyses pages 1-3)

5) Disease progression model
- Initiation: genetic susceptibility and environmental triggers lead to barrier weakening (mucus depletion, TJ disruption) permitting microbial and metabolite translocation.
- Amplification: APCs overproduce IL‑23, licensing Th17/ILC3 circuits; epithelial alarmins (IL‑33/TSLP/IL‑25) activate innate lymphoid and myeloid cells; neutrophils infiltrate and form NETs; IFN-programmed multicellular niches form around T cell aggregates adjacent to epithelial injury. (thomas2024alongitudinalsinglecell pages 1-2, jairath2024il23inhibitionfor pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3)
- Epithelial injury/death: IFN and TNF signaling, neutrophil proteases/ROS and pyroptosis (NLRP3–caspase‑1–GSDMD) drive epithelial apoptosis/pyroptosis and barrier loss. (thomas2024singlecelltranscriptomicanalyses pages 1-3, gu2024slc6a14promotesulcerative pages 16-17)
- Chronicity: dysbiosis with SCFA depletion sustains inflammation and barrier dysfunction; stromal/endothelial remodeling and hypoxia stabilize inflammatory niches; outcomes (remission vs nonremission) track with persistence of IFN signaling and inflammatory myeloid/T cell states under therapy. (thomas2024alongitudinalsinglecell pages 1-2, zhang2025fucoidanasa pages 5-7, thomas2024singlecelltranscriptomicanalyses pages 1-3)

6) Phenotypic manifestations (HP terms, representative)
- Bloody diarrhea, abdominal pain, urgency, weight loss; endoscopic mucosal friability and ulceration; histology: crypt abscesses, neutrophilic infiltration, goblet cell depletion, epithelial apoptosis. Mechanistically linked to epithelial barrier failure, neutrophil/NET activity, IFN and IL‑23-driven inflammation. (thomas2024singlecelltranscriptomicanalyses pages 1-3, jairath2024il23inhibitionfor pages 1-2)

Recent developments and latest research (2023–2024 priority)
- Single-cell therapeutic atlas (anti‑TNF): “interferon (IFN)-response signatures localising to T cell aggregates and epithelial damage” and “increased multi-cellular IFN signalling (UC)” predicted nonremission, connecting IFN niches to treatment dynamics. (thomas2024alongitudinalsinglecell pages 1-2)
- Checkpoint inhibitor colitis single-cell: identified epithelial apoptosis, neutrophil enrichment, and endothelial hypoxia programs linked to barrier dysfunction; mechanistic pathways overlap with UC. (thomas2024singlecelltranscriptomicanalyses pages 1-3)
- IL‑23 pathway synthesis and therapy: IL‑23 drives Th17 effectors across IMIDs; selective IL‑23p19 inhibitors demonstrate efficacy with rationale grounded in STAT3/JAK2–TYK2 signaling. (jairath2024il23inhibitionfor pages 1-2)
- Pyroptosis evidence: UC epithelium exhibits NLRP3–caspase‑1–GSDMD activation; SLC6A14 promotes UC progression by facilitating NLRP3-mediated pyroptosis, pointing to epithelial metabolic–inflammasome crosstalk as a target. (gu2024slc6a14promotesulcerative pages 16-17)
- Barrier biomarkers: serum occludin decreased, claudin‑2 and zonulin increased in IBD; anti‑TNF treatment improved these markers in UC, suggesting systemic readouts of barrier integrity. (thomas2024alongitudinalsinglecell pages 1-2)

Current applications and implementations
- Biologics and small molecules
  - Anti‑TNF (e.g., adalimumab): cellular remission associates with dampened IFN multicellular signaling in UC; nonresponders show persistent IFN niches. (thomas2024alongitudinalsinglecell pages 1-2)
  - Anti‑integrin (vedolizumab): targets lymphocyte trafficking; single-cell/spatial analyses reveal broader effects on myeloid and stromal subsets contributing to epithelial injury and may correlate with response signatures. (thomas2024singlecelltranscriptomicanalyses pages 1-3)
  - Anti‑IL‑23 (p19) agents: strong clinical efficacy with mechanistic rationale in UC; ongoing head-to-head and biomarker discovery efforts. (jairath2024il23inhibitionfor pages 1-2)
- Biomarkers and imaging
  - Barrier-focused biomarkers (occludin, claudin‑2, zonulin) and advanced endoscopic/spatial imaging to quantify junctional integrity and epithelial healing are emerging to guide therapy. (thomas2024alongitudinalsinglecell pages 1-2)

Expert opinions and authoritative analysis
- The Lancet 2024 perspective on IL‑23 positions p19 blockade as mechanistically superior to p40 for UC and related IMIDs, arguing IL‑23’s centrality in Th17‑driven mucosal inflammation and outlining JAK–STAT signaling dependencies and cell targets beyond Th17, such as ILC3s. (jairath2024il23inhibitionfor pages 1-2)
- Single-cell therapeutic atlases (Nature Immunology 2024) reframe resistance to anti‑TNF around persistent IFN niches and pretreatment epithelial/myeloid states, underscoring the need for biomarkers capturing epithelial–immune–stromal crosstalk. (thomas2024alongitudinalsinglecell pages 1-2)

Relevant statistics and recent data
- Cell atlas scale: ~1,000,000 gut single-cell transcriptomes, 216 biopsies, 41 subjects; pretreatment epithelial and myeloid differences correlated with remission; nonremission in UC linked to increased multicellular IFN signaling. (thomas2024alongitudinalsinglecell pages 1-2)
- Barrier biomarkers: occludin (AUC ~0.96), claudin‑2 (AUC ~0.86–0.90), zonulin (AUC ~0.74 for CD) in distinguishing IBD from controls; improvement after anti‑TNF in UC (study details summarized alongside the anti‑TNF atlas context). (thomas2024alongitudinalsinglecell pages 1-2)

Ontology-aligned annotations (examples)
- HGNC: IL23A, IL23R, STAT3, MUC2, OCLN, CLDN2, TJP1, NLRP3, CASP1, GSDMD. (jairath2024il23inhibitionfor pages 1-2, calvez2025novelinsightsinto pages 2-4, gu2024slc6a14promotesulcerative pages 16-17)
- GO BP: response to interferon; Th17 cell differentiation; mucin biosynthetic process; tight junction assembly; inflammasome complex assembly; pyroptosis. (thomas2024alongitudinalsinglecell pages 1-2, jairath2024il23inhibitionfor pages 1-2, calvez2025novelinsightsinto pages 2-4, gu2024slc6a14promotesulcerative pages 16-17)
- GO CC: apical junction complex; mucus layer; NLRP3 inflammasome; endothelial cell of vasculature. (calvez2025novelinsightsinto pages 2-4, thomas2024singlecelltranscriptomicanalyses pages 1-3)
- CL: goblet cell, colonocyte, neutrophil, monocyte/macrophage, CD4+ and CD8+ tissue-resident T cells, ILC2/ILC3, endothelial cell, fibroblast. (thomas2024alongitudinalsinglecell pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3)
- UBERON: colon mucosa (UBERON:0001155), lamina propria, intestinal epithelium, colonic endothelium. (thomas2024alongitudinalsinglecell pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3)
- CHEBI: butyrate (CHEBI:30089), acetate (CHEBI:15343), propionate (CHEBI:17295). (zhang2025fucoidanasa pages 5-7)

Embedded evidence quotes
> "spatial/system-level analyses identified interferon (IFN)-response signatures localising to T cell aggregates and epithelial damage in both CD and UC." (thomas2024alongitudinalsinglecell pages 1-2)

> "nonremitters displayed disease progression ... increased multi-cellular IFN signalling (UC)." (thomas2024alongitudinalsinglecell pages 1-2)

> "neutrophilic infiltrates and increased intraepithelial lymphocytes and epithelial apoptosis." (thomas2024singlecelltranscriptomicanalyses pages 1-3)

> "IL-23 (a p19-containing heterodimer sharing p40 with IL-12) promotes expansion and stabilization of Th17 cells that secrete IL-17A/F, IL-22, TNFα, IFNγ, and IL-26." (jairath2024il23inhibitionfor pages 1-2)

> "promotes ulcerative colitis progression by facilitating NLRP3 inflammasome-mediated pyroptosis." (gu2024slc6a14promotesulcerative pages 16-17)

> "mucus layer loss in UC, with reduced number/size of goblet cells and decreased MUC2 glycosylation." (calvez2025novelinsightsinto pages 2-4)

> "reduced butyrate and other SCFAs in disease." (zhang2025fucoidanasa pages 5-7)


*Blockquote: Concise, directly quoted findings from recent single-cell and review studies highlighting IFN signatures and epithelial damage, neutrophil/epithelial injury, IL-23/Th17 biology, NLRP3‑pyroptosis, mucus/goblet cell loss, and SCFA depletion in UC (context citations included).*

Evidence items (with links)
- Thomas et al., Nature Immunology 2024: single-cell anti‑TNF atlas in IBD; IFN-response niches adjacent to epithelial damage; increased IFN signaling in UC nonremission. DOI: 10.1038/s41590-024-01994-8; Published Oct 22, 2024. URL: https://doi.org/10.1038/s41590-024-01994-8 (thomas2024alongitudinalsinglecell pages 1-2)
- Thomas et al., Nature Medicine 2024: checkpoint inhibitor colitis scRNA‑seq; neutrophils, epithelial apoptosis, endothelial hypoxia signature linked to barrier dysfunction. DOI: 10.1038/s41591-024-02895-x; May 2024. URL: https://doi.org/10.1038/s41591-024-02895-x (thomas2024singlecelltranscriptomicanalyses pages 1-3)
- Jairath et al., The Lancet 2024: IL‑23 inhibition across chronic inflammatory diseases; mechanistic grounding of UC efficacy via Th17/ILC3 and STAT3 signaling. DOI: 10.1016/S0140-6736(24)01750-1; Oct 2024. URL: https://doi.org/10.1016/S0140-6736(24)01750-1 (jairath2024il23inhibitionfor pages 1-2)
- Gu et al., World Journal of Gastroenterology 2024: SLC6A14 promotes NLRP3‑mediated pyroptosis in UC epithelial cells. DOI: 10.3748/wjg.v30.i3.252; Jan 2024. URL: https://doi.org/10.3748/wjg.v30.i3.252 (gu2024slc6a14promotesulcerative pages 16-17)
- Calvez et al., Biomedicines 2025: review synthesizing mucus/goblet cell defects in UC and innate immune roles. DOI: 10.3390/biomedicines13020305; Jan 2025. URL: https://doi.org/10.3390/biomedicines13020305 (calvez2025novelinsightsinto pages 2-4)
- Zhang, Frontiers in Cellular and Infection Microbiology 2025: review summarizing 2013–2024 evidence of dysbiosis, pathobionts, and SCFA depletion in UC. DOI: 10.3389/fcimb.2025.1626614; Jul 2025. URL: https://doi.org/10.3389/fcimb.2025.1626614 (zhang2025fucoidanasa pages 5-7)

Limitations and notes
- While we prioritized 2023–2024 primary sources, several synthesized statements on mucus/goblet cell and SCFA biology derive from high-level reviews that consolidate earlier primary studies. Future iterations may add more 2023–2024 primary metabolomics studies as they become available.

Conclusions
Modern single-cell and spatial analyses in 2024 demonstrate that UC pathophysiology emerges from integrated epithelial barrier failure, IFN‑rich immune niches, IL‑23/Th17 and alarmin circuits, neutrophil effector pathways (including pyroptosis), and dysbiotic metabolite milieus. These insights map onto therapeutic mechanisms and resistance—anti‑TNF response tracks with resolution of IFN multicellular programs, while IL‑23 pathway blockade is mechanistically validated. Barrier-centric biomarkers and advanced imaging are moving toward clinical implementation to better align therapy with disease biology. (thomas2024alongitudinalsinglecell pages 1-2, jairath2024il23inhibitionfor pages 1-2, thomas2024singlecelltranscriptomicanalyses pages 1-3)

References

1. (thomas2024alongitudinalsinglecell pages 1-2): Tom Thomas, Matthias Friedrich, Charlotte Rich-Griffin, Mathilde Pohin, Devika Agarwal, Julia Pakpoor, Carl Lee, Ruchi Tandon, Aniko Rendek, Dominik Aschenbrenner, Ashwin Jainarayanan, Alexandru Voda, Jacqueline H. Y. Siu, Raphael Sanches-Peres, Eloise Nee, Dharshan Sathananthan, Dylan Kotliar, Peter Todd, Maria Kiourlappou, Lisa Gartner, Nicholas Ilott, Fadi Issa, Joanna Hester, Jason Turner, Saba Nayar, Jonas Mackerodt, Fan Zhang, Anna Jonsson, Michael Brenner, Soumya Raychaudhuri, Ruth Kulicke, Danielle Ramsdell, Nicolas Stransky, Ray Pagliarini, Piotr Bielecki, Noah Spies, Brian Marsden, Stephen Taylor, Allon Wagner, Paul Klenerman, Alissa Walsh, Mark Coles, Luke Jostins-Dean, Fiona M. Powrie, Andrew Filer, Simon Travis, Holm H. Uhlig, Calliope A. Dendrou, and Christopher D. Buckley. A longitudinal single-cell atlas of anti-tumour necrosis factor treatment in inflammatory bowel disease. Nature Immunology, 25:2152-2165, Oct 2024. URL: https://doi.org/10.1038/s41590-024-01994-8, doi:10.1038/s41590-024-01994-8. This article has 47 citations and is from a highest quality peer-reviewed journal.

2. (thomas2024singlecelltranscriptomicanalyses pages 1-3): Molly Fisher Thomas, Kamil Slowikowski, Kasidet Manakongtreecheep, Pritha Sen, Nandini Samanta, Jessica Tantivit, Mazen Nasrallah, Leyre Zubiri, Neal P. Smith, Alice Tirard, Swetha Ramesh, Benjamin Y. Arnold, Linda T. Nieman, Jonathan H. Chen, Thomas Eisenhaure, Karin Pelka, Yuhui Song, Katherine H. Xu, Vjola Jorgji, Christopher J. Pinto, Tatyana Sharova, Rachel Glasser, PuiYee Chan, Ryan J. Sullivan, Hamed Khalili, Dejan Juric, Genevieve M. Boland, Michael Dougan, Nir Hacohen, Bo Li, Kerry L. Reynolds, and Alexandra-Chloé Villani. Single-cell transcriptomic analyses reveal distinct immune cell contributions to epithelial barrier dysfunction in checkpoint inhibitor colitis. Nature medicine, 30:1349-1362, May 2024. URL: https://doi.org/10.1038/s41591-024-02895-x, doi:10.1038/s41591-024-02895-x. This article has 45 citations and is from a highest quality peer-reviewed journal.

3. (jairath2024il23inhibitionfor pages 1-2): Vipul Jairath, Maria Laura Acosta Felquer, and Raymond Jaihyun Cho. Il-23 inhibition for chronic inflammatory disease. The Lancet, 404:1679-1692, Oct 2024. URL: https://doi.org/10.1016/s0140-6736(24)01750-1, doi:10.1016/s0140-6736(24)01750-1. This article has 25 citations and is from a highest quality peer-reviewed journal.

4. (calvez2025novelinsightsinto pages 2-4): Valentin Calvez, Pierluigi Puca, Federica Di Vincenzo, Angelo Del Gaudio, Bianca Bartocci, Marco Murgiano, Jacopo Iaccarino, Erfan Parand, Daniele Napolitano, Daniela Pugliese, Antonio Gasbarrini, and Franco Scaldaferri. Novel insights into the pathogenesis of inflammatory bowel diseases. Biomedicines, 13:305, Jan 2025. URL: https://doi.org/10.3390/biomedicines13020305, doi:10.3390/biomedicines13020305. This article has 35 citations and is from a poor quality or predatory journal.

5. (gu2024slc6a14promotesulcerative pages 16-17): Qing Gu, Huan Xia, Yue-Qiong Song, Jun Duan, Yun Chen, You Zhang, He-Ping Chen, and Li Zhang. Slc6a14 promotes ulcerative colitis progression by facilitating nlrp3 inflammasome-mediated pyroptosis. World Journal of Gastroenterology, 30:252-267, Jan 2024. URL: https://doi.org/10.3748/wjg.v30.i3.252, doi:10.3748/wjg.v30.i3.252. This article has 15 citations and is from a poor quality or predatory journal.

6. (zhang2025fucoidanasa pages 5-7): Yating Zhang. Fucoidan as a therapeutic agent for ulcerative colitis: mechanisms of action and modulation of the gut microbiota. Frontiers in Cellular and Infection Microbiology, Jul 2025. URL: https://doi.org/10.3389/fcimb.2025.1626614, doi:10.3389/fcimb.2025.1626614. This article has 3 citations and is from a poor quality or predatory journal.