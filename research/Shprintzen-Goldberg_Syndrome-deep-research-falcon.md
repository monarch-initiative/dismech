---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-10T07:44:37.467860'
end_time: '2026-02-10T07:53:08.805228'
duration_seconds: 511.34
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Shprintzen-Goldberg Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Shprintzen-Goldberg Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Shprintzen-Goldberg Syndrome**.
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
- **Disease Name:** Shprintzen-Goldberg Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Shprintzen-Goldberg Syndrome**.
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


Disease Pathophysiology Research Report

Target Disease
- Disease Name: Shprintzen-Goldberg Syndrome (SGS)
- MONDO ID: MONDO_0008426 (from OpenTargets disease record)
- Category: Mendelian, autosomal dominant

Pathophysiology overview
Shprintzen-Goldberg syndrome is caused by heterozygous de novo mutations in SKI, a transcriptional corepressor that negatively regulates TGF-β/SMAD signaling. Most pathogenic variants cluster in exon 1 within the N‑terminal SMAD-binding region (R‑SMAD-binding/SMAD-interacting hotspot), disrupting SKI’s interaction with phosphorylated SMAD2/3 and altering its regulated degradation and cofactor dynamics. The net consequence is dysregulated TGF‑β target gene expression with epigenetic remodeling (notably increased H3K27 acetylation via CBP/P300) in key mesenchymal lineages, including vascular smooth muscle cells and fibroblasts. These cellular programs underlie craniosynostosis and connective-tissue manifestations such as aortic root aneurysm, skeletal abnormalities, and skin/ocular features, placing SGS among the TGF‑β signalopathies related to Marfan and Loeys–Dietz syndromes (disease spectrum with ongoing debate about increased vs attenuated TGF‑β responses in different contexts). (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2, kang2021epigeneticmodulationin pages 12-16, schepers2015thesmadbindingdomain pages 4-5)

1) Core Pathophysiology
- Primary mechanisms: SKI loss-of-function/dominant-negative effects at the SMAD interface. Doyle et al. identified heterozygous SKI mutations causing SGS; patient fibroblasts showed “enhanced activation of TGF‑β signaling cascades and higher expression of TGF‑β–responsive genes,” supporting pathogenic upregulation of TGF‑β programs in vivo (Nature Genetics, 2012; URL: https://doi.org/10.1038/ng.2421; published Sep 2012). Schepers et al. localized a mutation hotspot to the SMAD‑binding domain in exon 1 (EJHG, 2015; URL: https://doi.org/10.1038/ejhg.2014.61; published Apr 2015). Mechanistically, preclinical work indicates mutant SKI exhibits impaired binding to pSMAD2/3 and altered displacement of CBP/P300, leading to sustained TGF‑β transcriptional outputs and increased H3K27ac in aorta and skin; CBP/P300 inhibition reverses these signals (bioRxiv, 2021; URL: https://doi.org/10.1101/2021.02.12.431010; posted Feb 2021). (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2, kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 1-5)
- Dysregulated pathways: Canonical TGF‑β/SMAD2/3→SMAD4 signaling with aberrant chromatin cofactor balance (CBP/P300 vs HDAC/mSin3A/NCoR). Kang et al. report increased H3K27ac at TGF‑β target loci and broad upregulation of ECM and stress-response genes in Ski-mutant VSMCs and SGS fibroblasts; C646 (CBP/P300 HAT inhibitor) normalizes both acetylation and target gene expression and prevents aortic root growth in mouse models. (kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 5-8)
- Affected cellular processes: Transcriptional regulation of ECM and matrix remodeling genes (e.g., COL1A1, COL3A1, FN1, MMP2/MMP9, CTGF, SERPINE1), epigenetic acetylation (H3K27ac), and vascular media remodeling (elastin fiber fragmentation, collagen accumulation). (kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 5-8)

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - SKI (HGNC:10896): Causative gene; exon 1 SMAD-binding hotspot mutations; SKI represses TGF‑β by binding R‑SMADs and recruiting corepressors/HDACs. (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2)
  - SMAD2 (HGNC:6767), SMAD3 (HGNC:6769), SMAD4 (HGNC:6770): SKI interaction partners in canonical signaling; SGS mutations impair SKI–pSMAD2/3 binding and regulated degradation, altering transcriptional outputs. (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2)
  - CREBBP (HGNC:2348) and EP300 (HGNC:3373): CBP/P300 histone acetyltransferases; increased activity/H3K27ac at TGF‑β targets in SGS; inhibition with C646 blunts disease programs in models. (kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 5-8)
  - HDAC1 (HGNC:4852), SIN3A (HGNC:11128), NCOR1 (HGNC:7664): Corepressor/HDAC complexes recruited by SKI to repress SMAD-driven transcription; balance perturbed in SGS. (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2)
- Chemical entities (CHEBI)
  - Histone acetyltransferase inhibitor C646 (CHEBI:138488; used tool-referenced as CBP/P300 inhibitor) reduced H3K27ac and TGF‑β target expression, preventing aortic root growth in Ski-mutant and Marfan mouse models. (kang2021epigeneticmodulationin pages 12-16)
  - Angiotensin II receptor blockers (e.g., losartan; CHEBI:65330) referenced in TGF‑β signalopathy literature as modulators of TGF‑β activity and aneurysm progression in related conditions; discussed as contextual therapy rather than SGS‑specific trial evidence. (kang2021epigeneticmodulationin pages 1-5)
- Cell types (CL)
  - Vascular smooth muscle cells (CL:0000192): Effector cells for aortic pathology; show increased TGF‑β target expression, ECM remodeling and aneurysm in SkiVSMC:G34D/+ mice. (kang2021epigeneticmodulationin pages 12-16)
  - Fibroblasts (CL:0000057): SGS dermal fibroblasts display elevated baseline/stimulated TGF‑β responses (COL3A1, FN1, SMAD7, SKI). (kang2021epigeneticmodulationin pages 12-16, doyle2012mutationsinthe pages 1-9)
  - Cranial neural crest–derived progenitors (CL:0002320): Implicated in craniosynostosis and facial dysmorphology; morpholino knockdown of ski paralogs in zebrafish recapitulates craniofacial defects. (doyle2012mutationsinthe pages 1-9)
  - TH17 cells (CL:0001039): SKI–SMAD4 chromatin regulation controls RORγt expression and TH17 differentiation; illustrates SKI’s immune context in TGF‑β signalopathies. (kang2021epigeneticmodulationin pages 16-19)
- Anatomical locations (UBERON)
  - Aorta (UBERON:0000947): Aortic root aneurysm with elastin fragmentation and collagen accumulation. (doyle2012mutationsinthe pages 1-9, kang2021epigeneticmodulationin pages 12-16)
  - Cranial sutures (UBERON:0003681): Premature suture fusion (craniosynostosis) with cranial base angle abnormalities. (almpani2022loeysdietzandshprintzengoldberg pages 1-2)
  - Skin (UBERON:0002097): Excess fibrillar collagen deposition in SGS models and fibroblast phenotypes. (kang2021epigeneticmodulationin pages 12-16)

3) Biological Processes (suggested GO annotations)
- TGF‑β receptor signaling pathway (GO:0007179) and SMAD protein signal transduction (GO:0060395). (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2)
- Regulation of transcription by RNA polymerase II (GO:0006357) via SMAD–SKI cofactor dynamics; negative regulation of transcription (GO:0045892). (doyle2012mutationsinthe pages 1-9)
- Histone acetylation (GO:0016573) and regulation of chromatin organization (GO:0016568), notably H3K27 acetylation. (kang2021epigeneticmodulationin pages 12-16)
- Extracellular matrix organization (GO:0030198), collagen fibril organization (GO:0030199), and regulation of matrix metallopeptidase activity (GO:0030193). (kang2021epigeneticmodulationin pages 12-16)

4) Cellular Components (suggested GO CC)
- Nucleus (GO:0005634): SKI–SMAD complexes assemble on chromatin. (doyle2012mutationsinthe pages 1-9)
- Chromatin (GO:0000785)/Transcriptional repressor complex (GO:0017053): SKI–HDAC/NCoR/mSin3A complexes. (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2)
- SMAD complex (GO:0071141): R‑SMAD2/3–SMAD4 complexes targeted by SKI. (schepers2015thesmadbindingdomain pages 1-2)

5) Disease Progression (conceptual sequence)
- Initiating event: De novo heterozygous SKI missense mutation in exon 1 (SMAD‑binding hotspot). (schepers2015thesmadbindingdomain pages 1-2, doyle2012mutationsinthe pages 1-9)
- Molecular consequence: Impaired SKI binding to pSMAD2/3 and defective ligand-induced SKI degradation; aberrant cofactor exchange with increased CBP/P300 occupancy and H3K27ac at TGF‑β target loci; net upregulation of many TGF‑β–responsive genes in VSMCs and fibroblasts. (kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 5-8)
- Cellular/tissue effects: ECM remodeling with collagen accumulation and elastin fragmentation in aortic media; dysregulated cranial suture biology from altered neural crest progenitor signaling; fibroblast hyper-responsiveness. (kang2021epigeneticmodulationin pages 12-16, doyle2012mutationsinthe pages 1-9, almpani2022loeysdietzandshprintzengoldberg pages 1-2)
- Clinical manifestations: Progressive aortic root dilation/aneurysm, craniosynostosis and craniofacial dysmorphology, marfanoid skeletal features, skin and ocular findings. (doyle2012mutationsinthe pages 1-9, almpani2022loeysdietzandshprintzengoldberg pages 1-2)

6) Phenotypic Manifestations (HPO terms with links to mechanisms)
- Craniosynostosis (HP:0001363): Premature suture fusion; cranial base angle and craniofacial growth abnormalities quantified in SGS cohort. (almpani2022loeysdietzandshprintzengoldberg pages 1-2)
- Aortic root dilatation/aneurysm (HP:0002616/HP:0004942): Media remodeling with ECM dysregulation driven by altered TGF‑β signaling. (doyle2012mutationsinthe pages 1-9, kang2021epigeneticmodulationin pages 12-16)
- Marfanoid habitus (HP:0001519), scoliosis (HP:0002650), pectus deformity (HP:0000767/HP:0000768): Connective-tissue manifestations consistent with TGF‑β pathway dysregulation. (doyle2012mutationsinthe pages 1-9)
- Ocular features: Hypertelorism (HP:0000316), downslanting palpebral fissures (HP:0000494), myopia (HP:0000545), ectopia lentis variably reported—quantified ophthalmic summary in systematic review. (almpani2022loeysdietzandshprintzengoldberg pages 1-2)
- Skin/soft tissue: Skin laxity/abnormal scarring may reflect ECM remodeling and collagen deposition observed in models and patient cells. (kang2021epigeneticmodulationin pages 12-16)

7) Relation to Marfan/Loeys–Dietz and signaling controversy
- Doyle et al. reported enhanced TGF‑β signaling in SGS fibroblasts, aligning SGS with MFS/LDS signalopathies that show increased canonical and non‑SMAD signaling and phenotypic rescue by TGF‑β antagonism/ARB in models. (doyle2012mutationsinthe pages 1-9)
- Subsequent mechanistic work (e.g., SKI stabilization due to lost pSMAD2/3 binding) indicates attenuation of acute TGF‑β transcriptional responses in engineered cells, yet in vivo SGS mouse models and patient fibroblasts exhibit net increased TGF‑β target expression with heightened H3K27ac, suggesting cell context, time scale, and chromatin cofactor dynamics reconcile the apparent paradox. Therapeutically, CBP/P300 inhibition corrected the in vivo epigenetic/transcriptional phenotype and aortic growth. (kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 5-8)

8) Therapeutic implications and real-world considerations
- Epigenetic therapy: Pharmacologic CBP/P300 inhibition (C646) reduced H3K27ac, normalized TGF‑β target expression, and prevented aortic root enlargement in Ski-mutant and Fbn1C1039G/+ mice, highlighting a mechanistically anchored strategy under preclinical evaluation. (kang2021epigeneticmodulationin pages 12-16)
- TGF‑β pathway modulation: ARBs (e.g., losartan) have been effective in related TGF‑β signalopathies in preclinical and selected clinical contexts; while SGS-specific trials are lacking here, these data motivate individualized consideration under expert care. (kang2021epigeneticmodulationin pages 1-5)
- Multidisciplinary management: Given severe craniofacial involvement, airway compromise, and aortic disease, coordinated craniofacial, cardiology, genetics, and ophthalmology care is indicated; Almpani et al. demonstrate objective craniofacial clustering and airway metrics in SGS/LDS cohorts. (almpani2022loeysdietzandshprintzengoldberg pages 1-2)

Embedded artifact summary table
| Entity | Identifier (ontology) | Role in SGS Pathophysiology | Pathway / Process (GO terms) | Primary Cell Types (CL) | Primary Tissues / Organs (UBERON) | Key Evidence (DOI / URL with citation) |
|---|---|---|---|---|---|---|
| SKI | HGNC:10896 (SKI) | Transcriptional corepressor of TGF-β/SMADs; SGS-causing missense variants cluster in the N-terminal R‑SMAD / SMAD‑binding hotspot (exon 1) → impaired pSMAD2/3 binding, SKI stabilization and altered cofactor displacement, leading to dysregulated TGF‑β target transcription and chromatin changes. | TGF‑β signaling regulation (GO:0007179); transcriptional repression / chromatin modulation (histone acetylation changes, H3K27ac) | Vascular smooth muscle cell (CL:0000192); fibroblast (CL:0000057); neural progenitors | Aorta (UBERON:0000947); cranial structures / sutures (UBERON:0003681); skin (UBERON:0002097) | Doyle et al., Nat Genet 2012 doi:10.1038/ng.2421 https://doi.org/10.1038/ng.2421 (doyle2012mutationsinthe pages 1-9); Schepers et al., Eur J Hum Genet 2015 doi:10.1038/ejhg.2014.61 https://doi.org/10.1038/ejhg.2014.61 (schepers2015thesmadbindingdomain pages 1-2); Kang et al., bioRxiv 2021 doi:10.1101/2021.02.12.431010 https://doi.org/10.1101/2021.02.12.431010 (kang2021epigeneticmodulationin pages 5-8) |
| TGF‑β / SMAD signaling | GO:0007179 (TGF‑β receptor signaling pathway) | Central signaling axis dysregulated in SGS; net effects context-dependent but associated with altered canonical SMAD2/3 responses and downstream target gene programs (matrix, ECM, MMPs, CTGF, SERPINE1). | GO:0007179 (TGF‑β pathway); GO:0006351 (transcription) | VSMC (CL:0000192), fibroblast (CL:0000057), immune cells (e.g., TH17 CL:0001039) | Aorta (UBERON:0000947); craniofacial tissues (UBERON:0003681) | Doyle et al., Nat Genet 2012 (NG doi:10.1038/ng.2421) (doyle2012mutationsinthe pages 1-9); Schepers 2015 (schepers2015thesmadbindingdomain pages 1-2); Kang bioRxiv 2021 (kang2021epigeneticmodulationin pages 12-16) |
| SMAD2 / SMAD3 / SMAD4 complexes | HGNC:SMAD2, HGNC:SMAD3, HGNC:SMAD4 | R‑SMADs (SMAD2/3) are SKI interaction partners; loss of regulated SKI–pSMAD binding perturbs SMAD complex turnover, cofactor exchange and transcriptional output. | Canonical SMAD-mediated transcription (GO:0006355 / GO:0007179) | VSMC, fibroblast, neural crest derivatives | Aorta, cranial tissues | Functional interaction and disruption described in Doyle 2012 and Schepers 2015; SKI–SMAD mechanistics and consequences summarized in Kang et al., bioRxiv 2021 (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2, kang2021epigeneticmodulationin pages 5-8) |
| CBP / P300 (CREBBP / EP300) | HGNC:CREBBP, HGNC:EP300 | Histone acetyltransferases that deposit H3K27ac at TGF‑β target regulatory elements; SGS SKI variants fail to displace CBP/P300 from SMAD complexes → increased H3K27ac and sustained target transcription; CBP/P300 inhibition (C646) normalizes acetylation and blunts aneurysm progression in mouse models. | Chromatin acetylation / transcription coactivation (H3K27ac) | VSMC, fibroblast | Aortic media, skin | Kang et al., bioRxiv 2021 doi:10.1101/2021.02.12.431010 (kang2021epigeneticmodulationin pages 12-16, kang2021epigeneticmodulationin pages 5-8) |
| HDAC / corepressor complexes (HDAC1, NCoR1, SIN3A) | HGNC:HDAC1, HGNC:NCoR1, HGNC:SIN3A | Components recruited by SKI to repress SMAD-driven transcription; SGS mutations perturb the balance between corepressor (HDAC) recruitment and coactivator (CBP/P300) activity, altering chromatin state. | Histone deacetylation / transcriptional repression | VSMC, fibroblast, neural crest cells | Aorta, craniofacial tissues | Doyle et al., Nat Genet 2012; Schepers et al., Eur J Hum Genet 2015 (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2) |
| Vascular smooth muscle cell | CL:0000192 | Key effector cell in aortic pathology; mutant Ski in VSMCs drives increased TGF‑β target expression, ECM remodeling (collagens, MMPs), elastin fragmentation and aortic root dilation in mouse models. | TGF‑β signaling / ECM organization | VSMC (CL:0000192) | Aorta (UBERON:0000947) | Kang et al., bioRxiv 2021 (SkiVSMC:G34D/+ model) doi:10.1101/2021.02.12.431010 (kang2021epigeneticmodulationin pages 12-16) |
| Fibroblast | CL:0000057 | Patient dermal fibroblasts show altered baseline and TGF‑β–stimulated expression of COL3A1, FN1, SMAD7 and SKI; used as cellular readout of SKI mutation effects. | TGF‑β response / ECM gene expression | Fibroblast (CL:0000057) | Skin (UBERON:0002097) | Kang et al., bioRxiv 2021; Doyle et al., 2012 (kang2021epigeneticmodulationin pages 12-16, doyle2012mutationsinthe pages 1-9) |
| Cranial neural crest cell | CL:0002320 | Neural-crest–derived craniofacial progenitors implicated in craniosynostosis and facial dysmorphology; SKI function required during craniofacial development (animal models, morpholino knockdown phenocopy). | Developmental signaling (TGF/BMP cross-talk) | Neural crest derivatives | Cranial sutures (UBERON:0003681) | Doyle et al., Nat Genet 2012; Almpani et al., J Med Genet 2022 (doyle2012mutationsinthe pages 1-9, almpani2022loeysdietzandshprintzengoldberg pages 1-2) |
| T helper 17 cell (TH17) | CL:0001039 | SKI–SMAD4 axis regulates TH17 differentiation by controlling chromatin at RORγt locus; SKI degradation is required to reverse SKI–SMAD4 suppression during TH17 development → links SKI to immune modulation in TGF‑β signalopathies. | TGF‑β–dependent T cell differentiation (immune regulation) | TH17 (CL:0001039) | Secondary lymphoid tissues | Zhang et al., Nature 2017 doi:10.1038/nature24283 (cited in evidence syntheses) (kang2021epigeneticmodulationin pages 16-19, doyle2012mutationsinthe pages 1-9) |
| Aorta | UBERON:0000947 | Principal clinical site of life‑threatening pathology (aortic root aneurysm/dilation); histology shows elastin fragmentation, collagen accumulation and medial remodeling driven by altered TGF‑β/epigenetic programs. | Vascular development / ECM organization | VSMC, fibroblast | Aorta (UBERON:0000947) | Doyle et al., Nat Genet 2012; Kang et al., bioRxiv 2021 (doyle2012mutationsinthe pages 1-9, kang2021epigeneticmodulationin pages 12-16) |
| Cranial suture | UBERON:0003681 | Site of premature fusion (craniosynostosis) in SGS; developmental perturbation linked to aberrant SKI/TGF‑β signaling in cranial neural crest–derived tissues. | Cranial development / ossification | Neural crest progenitors | Cranial sutures (UBERON:0003681) | Almpani et al., J Med Genet 2022; Doyle 2012 (almpani2022loeysdietzandshprintzengoldberg pages 1-2, doyle2012mutationsinthe pages 1-9) |
| Skin | UBERON:0002097 | Dermatologic manifestations and fibroblast phenotypes reflect altered ECM deposition (increased fibrillar collagen) and epigenetic changes (H3K27ac) seen in patient cells and mouse models. | ECM organization / chromatin modification | Fibroblast (CL:0000057) | Skin (UBERON:0002097) | Kang et al., bioRxiv 2021 doi:10.1101/2021.02.12.431010 (kang2021epigeneticmodulationin pages 12-16) |


*Table: Concise, ontology-aligned summary of key molecular players, cell/tissue involvement, and primary evidence for Shprintzen-Goldberg syndrome, useful for knowledgebase curation and mechanistic overviews.*

Evidence quotations (selected mechanistic quotes)
- “We identified causative variation in ten individuals with SGS in the proto-oncogene SKI, a known repressor of TGF‑β activity. Cultured dermal fibroblasts from affected individuals showed enhanced activation of TGF‑β signaling cascades and higher expression of TGF‑β–responsive genes relative to control cells.” (Nature Genetics, 2012; doi:10.1038/ng.2421; URL: https://doi.org/10.1038/ng.2421) (doyle2012mutationsinthe pages 1-9)
- “The SMAD-binding domain of SKI: a hotspot for de novo mutations causing Shprintzen–Goldberg syndrome.” (EJHG, 2015; doi:10.1038/ejhg.2014.61; URL: https://doi.org/10.1038/ejhg.2014.61) (schepers2015thesmadbindingdomain pages 1-2)
- “Aortic root aneurysm in SGS mice is associated with both increased acetylation of histone H3 at lysine-27 (H3K27) and TGFβ target gene expression, all of which can be ameliorated by pharmacological CBP/P300 inhibition in vivo; similar findings were seen in cultured dermal fibroblast from SGS patients.” (bioRxiv preprint, 2021; doi:10.1101/2021.02.12.431010; URL: https://doi.org/10.1101/2021.02.12.431010) (kang2021epigeneticmodulationin pages 12-16)
- Craniofacial phenotyping: “increased cranial base angle with shortened anterior cranial base and underdevelopment of the maxilla and mandible… reduced pharyngeal airway in 55%… distinct clustering of patients with SGS… particularly severe phenotype associated with … SKI mutations.” (J Med Genet, 2022; doi:10.1136/jmedgenet-2021-107695; URL: https://doi.org/10.1136/jmedgenet-2021-107695) (almpani2022loeysdietzandshprintzengoldberg pages 1-2)

Expert perspectives and analysis
- Foundational discovery and animal/cell data support a unifying model: SKI mutations in SGS disable regulated SKI–R‑SMAD interactions and cofactor exchange, producing sustained TGF‑β target gene activation through increased CBP/P300-driven H3K27ac despite reports of attenuated acute responses in engineered systems. This reconciles the long-standing debate by invoking context-specific kinetics and chromatin state, consistent with in vivo disease phenotypes and therapeutic rescue by CBP/P300 inhibition. (kang2021epigeneticmodulationin pages 12-16, doyle2012mutationsinthe pages 1-9)

Key statistics and data
- Genetic architecture: SKI exon 1 hotspot (SMAD-binding domain) accounts for the majority of pathogenic SGS variants identified to date; recurrent substitutions include p.Gly116 and p.Gly117 (Doyle 2012; Schepers 2015). (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2)
- Craniofacial cohort (n=44 across LDS/SGS): 84% mandibular retrognathism; 84% flat midface projection; 73% abnormal eye shape; 73% low-set ears; reduced pharyngeal airway in 55% (Almpani 2022; published Dec 2022). (almpani2022loeysdietzandshprintzengoldberg pages 1-2)

References (URLs and publication dates)
- Doyle AJ et al. Mutations in the TGF‑β repressor SKI cause Shprintzen‑Goldberg syndrome with aortic aneurysm. Nature Genetics. Published Sep 2012. DOI/URL: https://doi.org/10.1038/ng.2421 (doyle2012mutationsinthe pages 1-9)
- Schepers D et al. The SMAD‑binding domain of SKI: a hotspot for de novo mutations causing Shprintzen–Goldberg syndrome. European Journal of Human Genetics. Published Apr 2015. DOI/URL: https://doi.org/10.1038/ejhg.2014.61 (schepers2015thesmadbindingdomain pages 1-2, schepers2015thesmadbindingdomain pages 4-5)
- Kang BE et al. Epigenetic modulation in the pathogenesis and treatment of inherited aortic aneurysm conditions. bioRxiv preprint. Posted Feb 2021. DOI/URL: https://doi.org/10.1101/2021.02.12.431010 (kang2021epigeneticmodulationin pages 1-5, kang2021epigeneticmodulationin pages 5-8, kang2021epigeneticmodulationin pages 12-16)
- Almpani K et al. Loeys‑Dietz and Shprintzen‑Goldberg syndromes: analysis of TGF‑β‑opathies with craniofacial manifestations using an innovative multimodality method. Journal of Medical Genetics. Published Dec 2022. DOI/URL: https://doi.org/10.1136/jmedgenet-2021-107695 (almpani2022loeysdietzandshprintzengoldberg pages 1-2)
- Additional mechanistic background: Zhang S et al. Reversing SKI–SMAD4-mediated suppression is essential for TH17 cell differentiation. Nature. Published Oct 2017. DOI/URL: https://doi.org/10.1038/nature24283 (context for SKI’s role in immune TGF‑β signaling) (kang2021epigeneticmodulationin pages 16-19)

Ontology-ready annotations (examples)
- HGNC: SKI (HGNC:10896); SMAD2 (HGNC:6767); SMAD3 (HGNC:6769); SMAD4 (HGNC:6770); CREBBP (HGNC:2348); EP300 (HGNC:3373); HDAC1 (HGNC:4852); SIN3A (HGNC:11128); NCOR1 (HGNC:7664). (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2, kang2021epigeneticmodulationin pages 12-16)
- GO BP: TGF‑β receptor signaling pathway (GO:0007179); SMAD protein signal transduction (GO:0060395); regulation of transcription by RNA Pol II (GO:0006357); histone acetylation (GO:0016573); extracellular matrix organization (GO:0030198). (doyle2012mutationsinthe pages 1-9, schepers2015thesmadbindingdomain pages 1-2, kang2021epigeneticmodulationin pages 12-16)
- GO CC: SMAD complex (GO:0071141); transcriptional repressor complex (GO:0017053); chromatin (GO:0000785); nucleus (GO:0005634). (schepers2015thesmadbindingdomain pages 1-2, doyle2012mutationsinthe pages 1-9)
- HPO: Craniosynostosis (HP:0001363); Aortic root dilatation (HP:0002616); Aortic aneurysm (HP:0004942); Marfanoid habitus (HP:0001519); Scoliosis (HP:0002650); Pectus excavatum/carinatum (HP:0000767/HP:0000768); Hypertelorism (HP:0000316); Downslanting palpebral fissures (HP:0000494); Myopia (HP:0000545). (doyle2012mutationsinthe pages 1-9, almpani2022loeysdietzandshprintzengoldberg pages 1-2)
- CL: Vascular smooth muscle cell (CL:0000192); Fibroblast (CL:0000057); Cranial neural crest cell (CL:0002320); TH17 cell (CL:0001039). (kang2021epigeneticmodulationin pages 12-16, doyle2012mutationsinthe pages 1-9, kang2021epigeneticmodulationin pages 16-19)
- UBERON: Aorta (UBERON:0000947); Cranial suture (UBERON:0003681); Skin (UBERON:0002097). (doyle2012mutationsinthe pages 1-9, almpani2022loeysdietzandshprintzengoldberg pages 1-2, kang2021epigeneticmodulationin pages 12-16)
- CHEBI: Losartan (CHEBI:65330); C646 (CBP/P300 inhibitor; CHEBI:138488). (kang2021epigeneticmodulationin pages 1-5, kang2021epigeneticmodulationin pages 12-16)

Limitations and open questions
- Reconciling disparate reports of attenuated versus enhanced TGF‑β responses requires further human tissue studies across developmental windows and cell types. SGS-specific clinical trials of epigenetic or TGF‑β–modulatory therapies have not yet been reported here. (kang2021epigeneticmodulationin pages 12-16, doyle2012mutationsinthe pages 1-9)

References

1. (doyle2012mutationsinthe pages 1-9): Alexander J Doyle, Jefferson J Doyle, Seneca L Bessling, Samantha Maragh, Mark E Lindsay, Dorien Schepers, Elisabeth Gillis, Geert Mortier, Tessa Homfray, Kimberly Sauls, Russell A Norris, Nicholas D Huso, Dan Leahy, David W Mohr, Mark J Caulfield, Alan F Scott, Anne Destrée, Raoul C Hennekam, Pamela H Arn, Cynthia J Curry, Lut Van Laer, Andrew S McCallion, Bart L Loeys, and Harry C Dietz. Mutations in the tgf-β repressor ski cause shprintzen-goldberg syndrome with aortic aneurysm. Nature genetics, 44:1249-1254, Sep 2012. URL: https://doi.org/10.1038/ng.2421, doi:10.1038/ng.2421. This article has 327 citations and is from a highest quality peer-reviewed journal.

2. (schepers2015thesmadbindingdomain pages 1-2): Dorien Schepers, Alexander J Doyle, Gretchen Oswald, Elizabeth Sparks, Loretha Myers, Patrick J Willems, Sahar Mansour, Michael A Simpson, Helena Frysira, Anneke Maat-Kievit, Rick Van Minkelen, Jeanette M Hoogeboom, Geert R Mortier, Hannah Titheradge, Louise Brueton, Lois Starr, Zornitza Stark, Charlotte Ockeloen, Charles Marques Lourenco, Ed Blair, Emma Hobson, Jane Hurst, Isabelle Maystadt, Anne Destrée, Katta M Girisha, Michelle Miller, Harry C Dietz, Bart Loeys, and Lut Van Laer. The smad-binding domain of ski: a hotspot for de novo mutations causing shprintzen–goldberg syndrome. European Journal of Human Genetics, 23:224-228, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.61, doi:10.1038/ejhg.2014.61. This article has 75 citations and is from a domain leading peer-reviewed journal.

3. (kang2021epigeneticmodulationin pages 12-16): Benjamin E. Kang, Rustam Bagirzadeh, Djahida Bedja, Jefferson J. Doyle, Elena G. MacFarlane, and Harry C. Dietz. Epigenetic modulation in the pathogenesis and treatment of inherited aortic aneurysm conditions. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.12.431010, doi:10.1101/2021.02.12.431010. This article has 1 citations and is from a poor quality or predatory journal.

4. (schepers2015thesmadbindingdomain pages 4-5): Dorien Schepers, Alexander J Doyle, Gretchen Oswald, Elizabeth Sparks, Loretha Myers, Patrick J Willems, Sahar Mansour, Michael A Simpson, Helena Frysira, Anneke Maat-Kievit, Rick Van Minkelen, Jeanette M Hoogeboom, Geert R Mortier, Hannah Titheradge, Louise Brueton, Lois Starr, Zornitza Stark, Charlotte Ockeloen, Charles Marques Lourenco, Ed Blair, Emma Hobson, Jane Hurst, Isabelle Maystadt, Anne Destrée, Katta M Girisha, Michelle Miller, Harry C Dietz, Bart Loeys, and Lut Van Laer. The smad-binding domain of ski: a hotspot for de novo mutations causing shprintzen–goldberg syndrome. European Journal of Human Genetics, 23:224-228, Apr 2015. URL: https://doi.org/10.1038/ejhg.2014.61, doi:10.1038/ejhg.2014.61. This article has 75 citations and is from a domain leading peer-reviewed journal.

5. (kang2021epigeneticmodulationin pages 1-5): Benjamin E. Kang, Rustam Bagirzadeh, Djahida Bedja, Jefferson J. Doyle, Elena G. MacFarlane, and Harry C. Dietz. Epigenetic modulation in the pathogenesis and treatment of inherited aortic aneurysm conditions. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.12.431010, doi:10.1101/2021.02.12.431010. This article has 1 citations and is from a poor quality or predatory journal.

6. (kang2021epigeneticmodulationin pages 5-8): Benjamin E. Kang, Rustam Bagirzadeh, Djahida Bedja, Jefferson J. Doyle, Elena G. MacFarlane, and Harry C. Dietz. Epigenetic modulation in the pathogenesis and treatment of inherited aortic aneurysm conditions. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.12.431010, doi:10.1101/2021.02.12.431010. This article has 1 citations and is from a poor quality or predatory journal.

7. (kang2021epigeneticmodulationin pages 16-19): Benjamin E. Kang, Rustam Bagirzadeh, Djahida Bedja, Jefferson J. Doyle, Elena G. MacFarlane, and Harry C. Dietz. Epigenetic modulation in the pathogenesis and treatment of inherited aortic aneurysm conditions. bioRxiv, Feb 2021. URL: https://doi.org/10.1101/2021.02.12.431010, doi:10.1101/2021.02.12.431010. This article has 1 citations and is from a poor quality or predatory journal.

8. (almpani2022loeysdietzandshprintzengoldberg pages 1-2): Konstantinia Almpani, Denise K. Liberton, Priyam Jani, Cyrus Keyvanfar, Rashmi Mishra, Natasha Curry, Pamela Orzechowski, Pamela A. Frischmeyer-Guerrerio, and Janice S. Lee. Loeys-dietz and shprintzen-goldberg syndromes: analysis of tgf-β-opathies with craniofacial manifestations using an innovative multimodality method. Journal of Medical Genetics, 59:938-946, Dec 2022. URL: https://doi.org/10.1136/jmedgenet-2021-107695, doi:10.1136/jmedgenet-2021-107695. This article has 20 citations and is from a domain leading peer-reviewed journal.