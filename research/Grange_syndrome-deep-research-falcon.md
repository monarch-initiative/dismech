---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-06T10:22:21.398269'
end_time: '2026-01-06T10:29:40.177479'
duration_seconds: 438.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Grange syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Grange syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Grange syndrome**.
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
- **Disease Name:** Grange syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Grange syndrome**.
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


Plan
- Objective 1 (completed): Establish core pathophysiology centered on YY1AP1 loss-of-function, INO80 chromatin remodeling, and vascular smooth muscle cell (VSMC) biology (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 9-10, guo2017lossoffunctionmutationsin pages 4-5).
- Objective 2: Catalog key molecular players, cell types, anatomical sites, and relevant chemical entities (supported below and summarized in artifact).
- Objective 3: Map disrupted biological processes and cellular components and outline disease progression.
- Objective 4: Compile phenotype manifestations with ontology terms.
- Objective 5: Summarize recent developments (with emphasis on 2023) and expert analyses.
- Objective 6: Provide structured artifact for knowledge-base population.
- Objective 7: Deliver a comprehensive, well-cited research report.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Grange syndrome
- MONDO ID: Not definitively established in the evidence pulled here. The disorder is OMIM 602531; the causal gene is YY1AP1.
- Category: Genetic (autosomal recessive)

Pathophysiology description
Grange syndrome is an autosomal-recessive, early-onset, systemic steno-occlusive arteriopathy with features resembling fibromuscular dysplasia (FMD) and, in the brain, moyamoya-like occlusions with collateralization. The causal mechanism is biallelic loss-of-function mutations in YY1AP1, which encodes a nuclear protein that associates with the transcription factor YY1 and is a component of the ATP-dependent INO80 chromatin-remodeling complex. In vascular smooth muscle cells (VSMCs), YY1AP1 is required for appropriate cell-cycle control and differentiation responses, particularly TGF-β–driven induction of contractile programs. YY1AP1 loss elevates CDKN1A/p21, causes G1/G2 cell-cycle arrest, reduces proliferation, and impairs upregulation of SMC markers (SM α-actin, SM22α, calponin), thereby altering SMC phenotype and contributing to focal stenoses and occlusions in multiple arterial beds, especially renal and intracranial arteries (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 4-5, raggio2021wholegenomesequencing pages 1-2).

Direct mechanistic statements and selected quotes
- “Loss-of-function mutations in YY1AP1 lead to Grange syndrome and a fibromuscular dysplasia-like vascular disease.” (American Journal of Human Genetics, Jan 2017; DOI: 10.1016/j.ajhg.2016.11.008; https://doi.org/10.1016/j.ajhg.2016.11.008) (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 9-10).
- “YY1AP1 is a ~90 kDa nuclear protein…a component of the INO80 ATP-dependent chromatin-remodeling complex and associates with YY1…YY1AP1 deficiency [in SMCs] increased p21/WAF/CDKN1A, decreased proliferation, [and] caused G1 and G2 cell-cycle arrest…[and] disrupted TGF-β1–driven differentiation, blocking upregulation of contractile markers (SM α-actin and SM22α).” (Guo et al., 2017; URL above) (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9).
- “YY1AP1 protein levels increase after TGF-β1 exposure in SMCs (maximal at 24 hr). YY1AP1 knockdown suppresses TGF-β1–induced upregulation of SMC differentiation markers (calponin, SM22α, SM α-actin), increases p21 levels, [and] reduces SMC proliferation.” (Guo et al., 2017) (guo2017lossoffunctionmutationsin pages 7-9).
- “YY1AP1 localizes to the nucleoplasm and nucleolus” and “associates with the INO80 complex” by co-immunoprecipitation (Guo et al., 2017) (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2).
- “VSMCs are the most compromised cell types in this pathology,” with prior functional data showing “G2 cell-cycle arrest without apoptosis” upon YY1AP1 loss (Raggio et al., Human Genomics, May 2021; DOI: 10.1186/s40246-021-00328-1; https://doi.org/10.1186/s40246-021-00328-1) (raggio2021wholegenomesequencing pages 1-2, raggio2021wholegenomesequencing pages 2-5).

1) Core Pathophysiology
- Primary pathophysiological mechanisms:
  - Causal gene disruption: Biallelic loss-of-function variants in YY1AP1 cause Grange syndrome (guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 4-5).
  - Chromatin-remodeling defect: YY1AP1 is a component of the INO80 complex, linking epigenetic regulation to VSMC phenotype (guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 9-10).
  - VSMC cell-state dysregulation: YY1AP1 deficiency increases p21/CDKN1A, induces G1/G2 arrest, reduces proliferation, and disrupts TGF-β–driven contractile differentiation, compromising arterial wall maintenance and repair (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 4-5).
- Dysregulated molecular pathways:
  - INO80-dependent chromatin remodeling impacting transcriptional programs for SMC contractile differentiation (guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 9-10).
  - TGF-β signaling responses in VSMCs (induction of YY1AP1 and SMC markers) (guo2017lossoffunctionmutationsin pages 7-9).
  - Cell-cycle regulation through CDKN1A/p21 (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 4-5).
- Affected cellular processes:
  - SMC differentiation program (markers: ACTA2/SM α-actin, TAGLN/SM22α, CNN1/calponin) impaired upon YY1AP1 loss (guo2017lossoffunctionmutationsin pages 7-9).
  - Proliferation and cell-cycle progression altered (p21 upregulation; arrest) (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 4-5).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - YY1AP1 (HGNC:23166): causal gene; loss-of-function causes Grange syndrome; INO80 complex component (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 1-2).
  - YY1 (HGNC:12828): transcription factor interacting with YY1AP1; cooperates with INO80 in transcriptional regulation (guo2017lossoffunctionmutationsin pages 2-3).
  - INO80 complex subunits (e.g., INO80; HGNC:19191): functional convergence with YY1AP1 in cell-cycle control; silencing INO80 components mirrors YY1AP1 knockdown effects (guo2017lossoffunctionmutationsin pages 9-10).
  - CDKN1A/p21 (HGNC:1784): elevated upon YY1AP1 loss; linked to cell-cycle arrest (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 4-5).
- Chemical entities (ChEBI):
  - Transforming growth factor beta (TGF-β; CHEBI:18420): upregulates YY1AP1 and drives SMC differentiation; response impaired when YY1AP1 is deficient (guo2017lossoffunctionmutationsin pages 7-9).
- Cell types (CL):
  - Vascular smooth muscle cell (CL:0000746): primary affected cell type; site of YY1AP1 nuclear/nucleolar localization and functional studies (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 2-3, raggio2021wholegenomesequencing pages 1-2).
- Anatomical locations (UBERON):
  - Renal artery (UBERON:0001637): frequent site of stenosis → renovascular hypertension (guo2017lossoffunctionmutationsin pages 7-9, persu2021beyondatherosclerosisand pages 5-7).
  - Cerebral arteries (e.g., internal carotid artery; UBERON:0001620 and cerebral artery UBERON:0002254): moyamoya-like intracranial occlusions/collaterals (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
  - Other involvement: celiac (UBERON:0001514), mesenteric (UBERON:0001625), coronary (UBERON:0001629) arteries in panvascular disease cases (raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 3-4).

3) Biological Processes (for GO annotation)
- Chromatin remodeling (GO:0006338)/INO80 complex activity affecting transcriptional programs in SMCs (guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 9-10).
- Regulation of cell cycle (GO:0051726), particularly negative/positive regulation via CDKN1A/p21 (GO:0007050 related processes), with YY1AP1 loss increasing p21 and causing arrest (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 4-5).
- Smooth muscle cell differentiation (GO:0051145) and response to TGF-β (GO:0071559); impaired induction of contractile gene expression (guo2017lossoffunctionmutationsin pages 7-9).
- Vascular development/artery morphogenesis (GO:0072110/GO:0035901) plausibly perturbed due to SMC dysfunction (supported by stenotic/occlusive lesions) (guo2017lossoffunctionmutationsin pages 7-9, raggio2021wholegenomesequencing pages 2-5).

4) Cellular Components
- INO80 complex (GO:0031011-like complex annotation for INO80) with YY1AP1 association (guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 9-10).
- Nuclear compartment and nucleolus as subcellular localization of YY1AP1 in SMCs (GO:0005634 nucleus; GO:0005730 nucleolus) (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 1-2).

5) Disease Progression (sequence of events)
- Genetic trigger: Biallelic YY1AP1 loss-of-function variants (nonsense/frameshift; intronic splice; multi-exon deletion) (guo2017lossoffunctionmutationsin pages 2-3, raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 3-4).
- Cellular mechanism: INO80/YY1AP1 dysfunction in VSMCs → increased p21, cell-cycle arrest, and impaired TGF-β–driven differentiation; nuclear/nucleolar YY1AP1 deficiency alters chromatin state (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
- Tissue/organ impact: Failure to maintain/repair the arterial media and intima in specific vascular beds → focal stenoses/occlusions; moyamoya-like intracranial changes with collateralization; in some cases, potential vulnerability to aneurysm where SMC population/maintenance is compromised (proposed model) (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
- Clinical manifestations: Progressive renovascular hypertension and ischemic cerebrovascular events in childhood or young adulthood; multi-territory arterial involvement (renal, cerebral, mesenteric/celiac, coronary) (guo2017lossoffunctionmutationsin pages 7-9, raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 3-4, persu2021beyondatherosclerosisand pages 5-7).

6) Phenotypic Manifestations (with HP terms)
- Renovascular hypertension (HP:0004421) due to renal artery stenosis (HP:0005366) (persu2021beyondatherosclerosisand pages 5-7, guo2017lossoffunctionmutationsin pages 7-9).
- Cerebral artery stenosis and moyamoya phenomenon (HP:0002610; HP:0005347) with stroke/TIA (HP:0001297) (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
- FMD-like arterial lesions (radiographic string-of-beads/focal stenoses) (no specific HP term; clinical description) (guo2017lossoffunctionmutationsin pages 7-9, persu2021beyondatherosclerosisand pages 5-7).
- Congenital heart defect (HP:0001627), including PDA in a 2023 case (karakaya2023thenewyoungest pages 1-3).
- Brachydactyly (HP:0001156) and syndactyly (HP:0001159) (guo2017lossoffunctionmutationsin pages 4-5, karakaya2023thenewyoungest pages 1-3).
- Bone fragility (HP:0002659) and learning disability/intellectual disability (HP:0001249) variably present (guo2017lossoffunctionmutationsin pages 4-5, persu2021beyondatherosclerosisand pages 5-7).
- Systemic arterial involvement: celiac/mesenteric/coronary artery stenoses documented in panvascular cases (raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 3-4).

Recent developments and latest research (prioritizing 2023)
- 2023: “The New Youngest Case of Grange Syndrome with a Novel Biallelic Pathogenic Variant in YY1AP1” reported a homozygous frameshift (c.2291del; p.Pro764Leufs*12) in a 1.5-year-old, expanding the allelic spectrum; clinical features included hypertension, PDA, and brachysyndactyly (Molecular Syndromology, Jan 2023; DOI: 10.1159/000527785; https://doi.org/10.1159/000527785) (karakaya2023thenewyoungest pages 1-3, karakaya2023thenewyoungest pages 3-4).
- Ongoing synthesis in expert reviews (renovascular hypertension and rare causes) continues to cite YY1AP1 loss-of-function in Grange syndrome and emphasize FMD-like pathology, consolidating the mechanistic axis of chromatin remodeling and SMC phenotypes (Hypertension, Oct 2021; DOI: 10.1161/HYPERTENSIONAHA.121.17004; https://doi.org/10.1161/hypertensionaha.121.17004) (persu2021beyondatherosclerosisand pages 5-7).
- 2021 case with combined frameshift and large deletion provides structural-variant spectrum in YY1AP1 and highlights panvascular involvement (Human Genomics, May 2021; DOI: 10.1186/s40246-021-00328-1; https://doi.org/10.1186/s40246-021-00328-1) (raggio2021wholegenomesequencing pages 2-5).
Note: Our evidence set did not retrieve 2024 regulatory-genomics or large-scale artery-specific datasets with citable IDs; thus, 2024 mechanistic extensions are not included here to maintain citation integrity.

Current applications and real-world implementations
- Genetic diagnosis: Whole exome/genome sequencing reliably identifies biallelic YY1AP1 loss-of-function (nonsense, frameshift, splice, multi-exon deletion) enabling definitive diagnosis of Grange syndrome and guiding surveillance for systemic vascular involvement (guo2017lossoffunctionmutationsin pages 2-3, raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 3-4).
- Clinical management implications: Recognition of bilateral renal artery stenosis risk and renovascular hypertension; procedural planning (e.g., hemodynamic risks during PDA closure noted in a 2023 case) and cautious use of renin-angiotensin system blockers if bilateral RAS is suspected (karakaya2023thenewyoungest pages 1-3, persu2021beyondatherosclerosisand pages 5-7).
- Phenotype-directed vascular imaging: Screening cerebrovascular and renovascular beds for stenoses/occlusions with attention to FMD-like and moyamoya-like morphologies (guo2017lossoffunctionmutationsin pages 7-9, persu2021beyondatherosclerosisand pages 5-7).

Expert opinions and authoritative analyses
- The AJHG 2017 report by Guo et al. provides foundational mechanistic evidence linking YY1AP1/INO80 to SMC biology and Grange syndrome, proposing that SMC de-differentiation/hyperplasia or failed SMC population/maintenance underlie occlusive versus aneurysmal phenotypes, respectively (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
- Hypertension (2021) review emphasizes Grange syndrome among rare causes of renovascular hypertension, reinforcing the clinical signature of focal, FMD-like lesions and the genetic etiology in YY1AP1 (persu2021beyondatherosclerosisand pages 5-7).

Relevant statistics and data from recent studies
- 2023 case report notes that only 14 individuals (12 molecularly confirmed) had been reported up to that time, underscoring the ultra-rare nature of Grange syndrome (Molecular Syndromology, 2023) (karakaya2023thenewyoungest pages 1-3).
- 2021 WGS case demonstrates compound heterozygosity (frameshift + large deletion) with parental segregation, illustrating the diagnostic utility of genome sequencing in suspected panvascular arteriopathy (Human Genomics, 2021) (raggio2021wholegenomesequencing pages 2-5).

Gene/protein annotations with ontology terms
- YY1AP1 (HGNC:23166): nucleus/nucleolus; INO80 complex; positive regulation of SMC differentiation (context-dependent); cell-cycle progression; loss elevates CDKN1A/p21 (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 4-5).
- YY1 (HGNC:12828): transcription factor partnering with YY1AP1/INO80 in transcriptional regulation (guo2017lossoffunctionmutationsin pages 2-3).
- INO80 (HGNC:19191) and related subunits: chromatin remodeling; silencing induces p21 and cell-cycle arrest (guo2017lossoffunctionmutationsin pages 9-10).
- CDKN1A/p21 (HGNC:1784): cell-cycle inhibitor elevated with YY1AP1 loss (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 4-5).

Cell type involvement (CL terms)
- Vascular smooth muscle cell (CL:0000746): primary site of YY1AP1 function and dysfunction; altered proliferation/differentiation responses (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, raggio2021wholegenomesequencing pages 1-2).

Anatomical locations (UBERON terms)
- Renal artery (UBERON:0001637) (persu2021beyondatherosclerosisand pages 5-7, guo2017lossoffunctionmutationsin pages 7-9).
- Cerebral/internal carotid arteries (UBERON:0002254/UBERON:0001620) (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
- Celiac (UBERON:0001514), mesenteric (UBERON:0001625), coronary (UBERON:0001629) arteries (raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 3-4).

Chemical entities (CHEBI terms)
- Transforming growth factor beta (TGF-β; CHEBI:18420) (guo2017lossoffunctionmutationsin pages 7-9).

Phenotype associations (HP terms)
- Renovascular hypertension (HP:0004421); renal artery stenosis (HP:0005366) (persu2021beyondatherosclerosisand pages 5-7, guo2017lossoffunctionmutationsin pages 7-9).
- Moyamoya phenomenon (HP:0005347); cerebral artery stenosis (HP:0002610); stroke/TIA (HP:0001297) (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10).
- Congenital heart defect (HP:0001627) including PDA (karakaya2023thenewyoungest pages 1-3).
- Brachydactyly (HP:0001156), syndactyly (HP:0001159) (guo2017lossoffunctionmutationsin pages 4-5, karakaya2023thenewyoungest pages 1-3).
- Bone fragility (HP:0002659), intellectual disability (HP:0001249) (guo2017lossoffunctionmutationsin pages 4-5, persu2021beyondatherosclerosisand pages 5-7).

Embedded artifact
| Category | Item | Ontology ID | Evidence | Mechanistic/clinical note |
|---|---|---|---|---|
| Gene/Protein | YY1AP1 |  | Guo et al. 2017; DOI:10.1016/j.ajhg.2016.11.008 (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 2-3) | Biallelic loss-of-function causes Grange syndrome; INO80 component; alters SMC differentiation |
| Cellular Component (GO/CC) | INO80 chromatin-remodeling complex |  | Guo et al. 2017; DOI:10.1016/j.ajhg.2016.11.008 (guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2) | YY1AP1 associates with INO80 in SMCs; chromatin remodeling linked to cell-cycle control |
| Gene/Protein | YY1 |  | Guo et al. 2017; DOI:10.1016/j.ajhg.2016.11.008 (guo2017lossoffunctionmutationsin pages 2-3) | Transcription factor interacting with YY1AP1/INO80 complex |
| Biological Process (GO) | VSMC differentiation / TGF-β response |  | Guo et al. 2017; Raggio et al. 2021 (guo2017lossoffunctionmutationsin pages 5-7, raggio2021wholegenomesequencing pages 1-2) | YY1AP1 required for TGF-β–driven induction of SMC contractile markers (SM α-actin, SM22α) |
| Biological Process (GO) | Cell-cycle regulation / CDKN1A (p21) upregulation |  | Guo et al. 2017; multiple functional assays (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 4-5) | YY1AP1 loss increases p21 (CDKN1A), causing G1/G2 arrest and reduced proliferation in SMCs |
| Cellular Component (GO/CC) | Nuclear / nucleolar localization |  | Guo et al. 2017 (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 1-2) | YY1AP1 localizes to nucleus and nucleolus in SMCs and cell models |
| Cell Type (CL) | Vascular smooth muscle cell (VSMC) |  | Guo et al. 2017; Raggio et al. 2021 (guo2017lossoffunctionmutationsin pages 5-7, raggio2021wholegenomesequencing pages 1-2) | Primary affected cell type; SMC dysfunction underlies stenotic/occlusive arteriopathy |
| Anatomy (UBERON) | Renal artery |  | Guo et al. 2017; Persu et al. 2021; case reports (guo2017lossoffunctionmutationsin pages 7-9, raggio2021wholegenomesequencing pages 2-5) | Frequent site of stenosis → renovascular hypertension in Grange syndrome |
| Anatomy (UBERON) | Cerebral arteries (moyamoya-like) |  | Guo et al. 2017; Guo et al. AJHG excerpts (guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 9-10) | Intracranial stenoses/occlusions with collateral formation (moyamoya-like phenotype) |
| Anatomy (UBERON) | Celiac / coronary / mesenteric arteries (panvascular) |  | Raggio et al. 2021; Karakaya 2023 case (raggio2021wholegenomesequencing pages 2-5, karakaya2023thenewyoungest pages 1-3) | Multi-territory arterial involvement reported in molecularly confirmed cases |
| Chemical/Drug (ChEBI) | Transforming growth factor beta (TGF-β) |  | Guo et al. 2017 (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9) | TGF-β upregulates YY1AP1 in SMCs and drives differentiation programs |
| Biological Process (GO) | Fibromuscular dysplasia–like arteriopathy |  | Guo et al. 2017; Persu et al. 2021 (guo2017lossoffunctionmutationsin pages 7-9, persu2021beyondatherosclerosisand pages 5-7) | Clinical pattern: focal stenoses/beaded appearance resembling FMD |
| Anatomy (UBERON) | Hypertension (clinical consequence) |  | Guo et al. 2017; clinical case reports (guo2017lossoffunctionmutationsin pages 7-9, karakaya2023thenewyoungest pages 1-3) | Result of renal artery stenosis and systemic vascular involvement |
| Anatomy (UBERON) | Brachydactyly / syndactyly (skeletal) |  | Guo et al. 2017; Karakaya 2023 (guo2017lossoffunctionmutationsin pages 4-5, karakaya2023thenewyoungest pages 1-3) | Recurrent skeletal anomalies in Grange syndrome alongside vascular disease |


*Table: Compact table of key genes, processes, cell types, anatomical sites, and evidence linking YY1AP1/INO80 dysfunction to Grange syndrome; useful as a quick ontology-ready reference for knowledge-base entry.*

Evidence items (primary literature with PMIDs/DOIs/URLs)
- Guo et al., 2017, The American Journal of Human Genetics. “Loss-of-Function Mutations in YY1AP1 Lead to Grange Syndrome and a Fibromuscular Dysplasia-Like Vascular Disease.” DOI: 10.1016/j.ajhg.2016.11.008. URL: https://doi.org/10.1016/j.ajhg.2016.11.008 (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 9-10, guo2017lossoffunctionmutationsin pages 4-5, guo2017lossoffunctionmutationsin pages 10-10).
- Raggio et al., 2021, Human Genomics. “Whole genome sequencing reveals a frameshift mutation and a large deletion in YY1AP1 in a girl with a panvascular artery disease.” DOI: 10.1186/s40246-021-00328-1. URL: https://doi.org/10.1186/s40246-021-00328-1 (raggio2021wholegenomesequencing pages 1-2, raggio2021wholegenomesequencing pages 2-5).
- Karakaya et al., 2023, Molecular Syndromology. “The New Youngest Case of Grange Syndrome with a Novel Biallelic Pathogenic Variant in YY1AP1.” DOI: 10.1159/000527785. URL: https://doi.org/10.1159/000527785 (karakaya2023thenewyoungest pages 1-3, karakaya2023thenewyoungest pages 3-4).
- Persu et al., 2021, Hypertension. “Beyond Atherosclerosis and Fibromuscular Dysplasia: Rare Causes of Renovascular Hypertension.” DOI: 10.1161/HYPERTENSIONAHA.121.17004. URL: https://doi.org/10.1161/hypertensionaha.121.17004 (persu2021beyondatherosclerosisand pages 5-7).

Limitations and open questions
- Lack of arterial tissue pathology in published cases limits direct histopathological correlation, as noted by Guo et al. (guo2017lossoffunctionmutationsin pages 7-9).
- While SMC-autonomous mechanisms are well-supported, contributions from endothelial cells or adventitial fibroblasts remain to be defined.
- The extent to which heterozygous YY1AP1 variation confers predisposition to adult FMD remains uncertain at the population level (guo2017lossoffunctionmutationsin pages 7-9).

Summary
Grange syndrome is a chromatin-remodeling disorder of the arterial media driven by YY1AP1 loss-of-function within the INO80 complex. The consequence is dysregulated VSMC cell-cycle control and impaired TGF-β–dependent contractile differentiation, producing a systemic, FMD-like steno-occlusive arteriopathy with moyamoya-like intracranial involvement. Clinical recognition should prompt genomic testing and comprehensive vascular screening, with management focused on renovascular hypertension and ischemia risk (guo2017lossoffunctionmutationsin pages 5-7, guo2017lossoffunctionmutationsin pages 7-9, guo2017lossoffunctionmutationsin pages 2-3, guo2017lossoffunctionmutationsin pages 1-2, guo2017lossoffunctionmutationsin pages 9-10, guo2017lossoffunctionmutationsin pages 4-5, raggio2021wholegenomesequencing pages 1-2, karakaya2023thenewyoungest pages 1-3, karakaya2023thenewyoungest pages 3-4, raggio2021wholegenomesequencing pages 2-5, persu2021beyondatherosclerosisand pages 5-7).

References

1. (guo2017lossoffunctionmutationsin pages 5-7): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.

2. (guo2017lossoffunctionmutationsin pages 7-9): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.

3. (guo2017lossoffunctionmutationsin pages 2-3): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.

4. (guo2017lossoffunctionmutationsin pages 1-2): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.

5. (guo2017lossoffunctionmutationsin pages 9-10): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.

6. (guo2017lossoffunctionmutationsin pages 4-5): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.

7. (raggio2021wholegenomesequencing pages 1-2): Víctor Raggio, Nicolas Dell’Oca, Camila Simoes, Alejandra Tapié, Conrado Medici, Gonzalo Costa, Soledad Rodriguez, Gonzalo Greif, Estefania Garrone, María Laura Rovella, Virgina Gonzalez, Margarita Halty, Gabriel González, Jong-Yeon Shin, Sang-Yoon Shin, Changhoon Kim, Jeong-Sun Seo, Martin Graña, Hugo Naya, and Lucia Spangenberg. Whole genome sequencing reveals a frameshift mutation and a large deletion in yy1ap1 in a girl with a panvascular artery disease. Human Genomics, May 2021. URL: https://doi.org/10.1186/s40246-021-00328-1, doi:10.1186/s40246-021-00328-1. This article has 11 citations and is from a peer-reviewed journal.

8. (raggio2021wholegenomesequencing pages 2-5): Víctor Raggio, Nicolas Dell’Oca, Camila Simoes, Alejandra Tapié, Conrado Medici, Gonzalo Costa, Soledad Rodriguez, Gonzalo Greif, Estefania Garrone, María Laura Rovella, Virgina Gonzalez, Margarita Halty, Gabriel González, Jong-Yeon Shin, Sang-Yoon Shin, Changhoon Kim, Jeong-Sun Seo, Martin Graña, Hugo Naya, and Lucia Spangenberg. Whole genome sequencing reveals a frameshift mutation and a large deletion in yy1ap1 in a girl with a panvascular artery disease. Human Genomics, May 2021. URL: https://doi.org/10.1186/s40246-021-00328-1, doi:10.1186/s40246-021-00328-1. This article has 11 citations and is from a peer-reviewed journal.

9. (persu2021beyondatherosclerosisand pages 5-7): Alexandre Persu, Caitriona Canning, Aleksander Prejbisz, Piotr Dobrowolski, Laurence Amar, Constantina Chrysochou, Jacek Kądziela, Mieczysław Litwin, Daan van Twist, Patricia Van der Niepen, Gregoire Wuerzner, Peter de Leeuw, Michel Azizi, Magda Januszewicz, and Andrzej Januszewicz. Beyond atherosclerosis and fibromuscular dysplasia: rare causes of renovascular hypertension. Hypertension, 78:898-911, Oct 2021. URL: https://doi.org/10.1161/hypertensionaha.121.17004, doi:10.1161/hypertensionaha.121.17004. This article has 38 citations and is from a domain leading peer-reviewed journal.

10. (karakaya2023thenewyoungest pages 3-4): Taner Karakaya, Ayberk Turkyilmaz, Deniz Eris, Mehtap Kaya, Kupra Oksuz, Meltem Aygul Eryigit, and Gizem Gönen. The new youngest case of grange syndrome with a novel biallelic pathogenic variant in yy1ap1. Molecular Syndromology, 14:239-245, Jan 2023. URL: https://doi.org/10.1159/000527785, doi:10.1159/000527785. This article has 1 citations and is from a peer-reviewed journal.

11. (karakaya2023thenewyoungest pages 1-3): Taner Karakaya, Ayberk Turkyilmaz, Deniz Eris, Mehtap Kaya, Kupra Oksuz, Meltem Aygul Eryigit, and Gizem Gönen. The new youngest case of grange syndrome with a novel biallelic pathogenic variant in yy1ap1. Molecular Syndromology, 14:239-245, Jan 2023. URL: https://doi.org/10.1159/000527785, doi:10.1159/000527785. This article has 1 citations and is from a peer-reviewed journal.

12. (guo2017lossoffunctionmutationsin pages 10-10): Dong-chuan Guo, Xue-Yan Duan, Ellen S. Regalado, Lauren Mellor-Crummey, Callie S. Kwartler, Dong Kim, Kenneth Lieberman, Bert B.A. de Vries, Rolph Pfundt, Albert Schinzel, Dieter Kotzot, Xuetong Shen, Min-Lee Yang, Michael J. Bamshad, Deborah A. Nickerson, Heather L. Gornik, Santhi K. Ganesh, Alan C. Braverman, Dorothy K. Grange, and Dianna M. Milewicz. Loss-of-function mutations in yy1ap1 lead to grange syndrome and a fibromuscular dysplasia-like vascular disease. The American Journal of Human Genetics, 100:21-30, Jan 2017. URL: https://doi.org/10.1016/j.ajhg.2016.11.008, doi:10.1016/j.ajhg.2016.11.008. This article has 71 citations.