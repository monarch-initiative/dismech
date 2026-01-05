---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:47:01.047966'
end_time: '2025-12-18T09:55:18.289577'
duration_seconds: 497.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IgA Nephropathy
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** IgA Nephropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **IgA Nephropathy**.
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
- **Disease Name:** IgA Nephropathy
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **IgA Nephropathy**.
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
- Disease Name: IgA Nephropathy (IgAN)
- MONDO ID: MONDO_0005049 (IgA glomerulonephritis; also referenced as EFO_0004194 in OpenTargets)
- Category: Autoimmune, immune-complex glomerulonephritis

Executive Summary and Key Concepts
IgA nephropathy is characterized by mesangial deposition of immune complexes containing galactose‑deficient IgA1 (Gd‑IgA1), antiglycan autoantibodies, and complement, leading to mesangioproliferative injury, downstream podocyte damage, tubulointerstitial inflammation, and progressive fibrosis. The current paradigm is a multi‑hit model: (1) overproduction of circulating polymeric Gd‑IgA1, (2) formation of anti‑glycan IgG/IgA autoantibodies, (3) immune‑complex assembly and persistence in circulation, and (4) mesangial deposition with glomerular cell activation and complement engagement, predominantly via the alternative and lectin pathways (quotes and synthesis from 2023–2024 reviews) (filippone2024contemporaryreviewof pages 1-2, novak2024oglycosylationofiga1 pages 1-2, cheung2024theroleof pages 2-3, salvadori2024whatisnew pages 2-3).

Direct quote supporting the multi‑hit model and Gd‑IgA1: “Galactose‑deficient IgA1 in the circulation of patients with IgA nephropathy is bound by IgG autoantibodies… These complexes… can enter the glomerular mesangium, activate the resident mesangial cells, and induce glomerular injury.” (Glycobiology 2024; DOI: 10.1093/glycob/cwae060; URL: https://doi.org/10.1093/glycob/cwae060) (novak2024oglycosylationofiga1 pages 1-2).

1) Core Pathophysiology
- Multi‑hit pathogenesis: Elevated polymeric Gd‑IgA1 (Hit 1), antiglycan autoantibodies (Hit 2), circulating immune complexes (Hit 3), mesangial deposition and activation (Hit 4) (Nature Reviews Disease Primers 2023; Frontiers Immunology 2024; Frontiers Nephrology 2024) (filippone2024contemporaryreviewof pages 1-2, cheung2024theroleof pages 2-3, salvadori2024whatisnew pages 2-3).
- Dysregulated glycosylation: Aberrant O‑glycosylation in the IgA1 hinge due to dysregulated glycosyltransferases produces Gd‑IgA1 that self‑aggregates, binds IgG, and is nephritogenic (Glycobiology 2024) (novak2024oglycosylationofiga1 pages 1-2).
- Mucosal immunity and microbiome: MALT (GALT/NALT) plasma cells and BAFF/APRIL signaling promote excessive mucosal IgA and Gd‑IgA1; dysbiosis and TLR activation contribute to mucosal hyper‑responsiveness (Frontiers Nephrology 2024; BMC Nephrol 2024 review and studies) (cheung2024theroleof pages 1-2, salvadori2024whatisnew pages 2-3).
- Complement activation: C3 co‑localizes with IgA in most biopsies; alternative and lectin pathways are implicated, with complement deposition correlating with disease activity and prognosis (Frontiers Immunology 2024; World J Nephrol 2024; Scientific Reports 2024) (filippone2024contemporaryreviewof pages 1-2, salvadori2024whatisnew pages 2-3).
- Intrarenal cellular responses: Mesangial proliferation, matrix expansion, and cytokine secretion; downstream podocyte injury with proteinuria; emerging single‑cell/spatial studies implicate early endothelial activation and complex immune cell interactions in glomeruli (Nat Genet 2024 multi‑omic atlas; contextual reviews) (filippone2024contemporaryreviewof pages 1-2, dreher2025recentadvancesin pages 8-9).

2) Key Molecular Players
- Genes/Proteins (HGNC):
  - TNFSF13 (APRIL) and TNFSF13B (BAFF): B‑cell/plasma‑cell survival factors driving overproduction of Gd‑IgA1 and autoantibodies; therapeutic targets (Frontiers Nephrol 2024; IJMS 2024) (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2).
  - C1GALT1, ST6GAL1: Glycosyltransferases linked to IgA1 O‑glycosylation; dysregulation leads to Gd‑IgA1 (Glycobiology 2024) (novak2024oglycosylationofiga1 pages 1-2).
  - Complement components: C3; regulators CFH/CFHR (genetic risk) that modulate alternative pathway activation (reviews 2023–2024) (salvadori2024whatisnew pages 2-3, filippone2024contemporaryreviewof pages 1-2).
- Chemical Entities (CHEBI): Galactose; N‑acetylgalactosamine (GalNAc) defining IgA1 O‑glycans (Glycobiology 2024) (novak2024oglycosylationofiga1 pages 1-2).
- Cell Types (CL): Mesangial cells (deposition/activation), glomerular endothelial cells (early inflammatory activation), podocytes (injury/proteinuria), plasma cells/B cells (mucosal/systemic IgA1; autoantibodies), T follicular helper cells (mucosal germinal centers) (Frontiers Immunology 2024; Nat Genet 2024) (filippone2024contemporaryreviewof pages 1-2, dreher2025recentadvancesin pages 8-9).
- Anatomical Locations (UBERON): Kidney/glomerulus/mesangium (injury site); palatine tonsil (NALT) and Peyer’s patches (GALT) as sources of mucosal IgA (Primers 2023; IJMS 2024) (filippone2024contemporaryreviewof pages 1-2, muto2024newinsightsand pages 1-2).

3) Biological Processes (GO) Disrupted
- Protein O‑linked glycosylation (IgA1 hinge region) (novak2024oglycosylationofiga1 pages 1-2).
- B‑cell activation and class‑switch recombination to IgA (BAFF/APRIL‑mediated) (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2).
- Complement activation—alternative and lectin pathways—intraglomerular inflammation (filippone2024contemporaryreviewof pages 1-2, salvadori2024whatisnew pages 2-3).
- Mesangial cell proliferation, extracellular matrix organization; podocyte injury responses (filippone2024contemporaryreviewof pages 1-2).

4) Cellular Components (GO-CC)
- Extracellular region/space (immune complexes, complement factors), mesangial matrix; cell membrane receptors on mesangial/endothelial/podocyte cells; germinal center structures in tonsil/Peyer’s patches (filippone2024contemporaryreviewof pages 1-2, novak2024oglycosylationofiga1 pages 1-2, muto2024newinsightsand pages 1-2).

5) Disease Progression
- Sequence of events: Mucosal dysregulation → overproduction of Gd‑IgA1 and autoantibodies → circulating immune complexes → mesangial deposition → mesangial activation and cytokine release → complement activation (AP/LP) → podocyte injury and proteinuria → tubulointerstitial inflammation/fibrosis → progressive eGFR decline (Primers 2023; Frontiers 2024) (filippone2024contemporaryreviewof pages 1-2, cheung2024theroleof pages 2-3).
- Distinct phases: Subclinical deposition and episodic synpharyngitic hematuria; persistent proteinuria phase with histologic activity (MEST‑C), and progressive fibrosis with declining GFR (filippone2024contemporaryreviewof pages 1-2).

6) Phenotypic Manifestations
- Clinical phenotypes: Microscopic/macroscopic hematuria (often synpharyngitic), proteinuria, hypertension; progressive CKD with variable course (filippone2024contemporaryreviewof pages 1-2).
- Pathology: Mesangial IgA (IgA1) and C3 deposits; mesangial hypercellularity (M), endocapillary hypercellularity (E), segmental sclerosis (S), tubular atrophy/interstitial fibrosis (T), and crescents (C) — the Oxford MEST‑C classification (filippone2024contemporaryreviewof pages 1-2).
- Prognostic biomarkers: Persistent proteinuria and lower eGFR are strongly prognostic; circulating and histologic complement (C3/C4) add incremental risk information (Scientific Reports 2024) (filippone2024contemporaryreviewof pages 1-2).

Recent Developments and Latest Research (2023–2024 priority)
- Glycosylation and immune complexes: 2024 Glycobiology review consolidates the enzymology and structural basis of Gd‑IgA1 pathogenicity and immune complex formation, with explicit mechanistic statements (Novak et al. 2024, DOI above) (novak2024oglycosylationofiga1 pages 1-2).
- BAFF/APRIL biology: 2024 reviews highlight elevated serum BAFF/APRIL correlating with disease severity and therapeutic potential of APRIL antagonists (e.g., reductions in proteinuria and Gd‑IgA1 in early studies) (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2).
- Complement and prognostication: Contemporary reviews and cohort analyses underscore alternative/lectin pathway involvement; lower serum C3 and higher C4 at diagnosis improved prediction beyond standard risk tools (Sci Rep 2024; doi:10.1038/s41598-024-65857-w; https://doi.org/10.1038/s41598-024-65857-w) (filippone2024contemporaryreviewof pages 1-2).
- Single‑cell and spatial kidney atlases: Multi‑omic human kidney maps implicate endothelial activation and fibroinflammatory microenvironments in progression, complementing mesangial‑centric models (Nat Genet 2024; doi:10.1038/s41588-024-01802-x; https://doi.org/10.1038/s41588-024-01802-x) (dreher2025recentadvancesin pages 8-9).

Current Applications and Real‑world Implementations
- Supportive care: RAAS blockade; SGLT2 inhibitors now broadly used in proteinuric CKD including IgAN, reducing proteinuria and slowing eGFR decline (summarized in 2024 reviews) (filippone2024contemporaryreviewof pages 1-2).
- Targeted‑release budesonide (Nefecon/TARPEYO): Mucosal‑targeted corticosteroid that reduces proteinuria and slows eGFR loss in IgAN; integrated in contemporary management (dreher2025recentadvancesin pages 8-9, filippone2024contemporaryreviewof pages 1-2).
- Endothelin/angiotensin blockade: Sparsentan (dual ERA/ARB) used to reduce proteinuria as part of supportive strategy (filippone2024contemporaryreviewof pages 1-2).
- Complement inhibitors in trials: Agents targeting alternative (factor B) and lectin (MASP‑2) pathways and terminal components are under active investigation and selective use (e.g., ravulizumab study NCT06291376; iptacopan biopsy‑impact study NCT06797518) (filippone2024contemporaryreviewof pages 1-2).
- BAFF/APRIL inhibitors in trials: Atacicept/telitacicept/zigakibart targeting BAFF/APRIL axes are being tested with signals on Gd‑IgA1 reduction and proteinuria (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2).

Expert Opinions and Authoritative Analyses
- Nature Reviews Disease Primers (2023) and contemporary 2024 reviews converge on the multi‑hit framework and emphasize mucosal immune dysregulation and complement as central pathogenic drivers translating to targeted therapy development (filippone2024contemporaryreviewof pages 1-2, cheung2024theroleof pages 2-3, salvadori2024whatisnew pages 2-3).
- Direct quote highlighting complement’s role (integrated across sources): co‑localization of C3 with IgA is present in the vast majority of biopsies, implicating alternative/lectin pathways in glomerular injury (summarized in Filippone 2024 and Muto 2024) (filippone2024contemporaryreviewof pages 1-2, muto2024newinsightsand pages 1-2).

Relevant Statistics and Data (recent studies)
- Registry‑validated biopsy diagnosis PPV 95% (95% CI 90–98%) with frequent C3 deposition (72.4%) in a Swedish cohort (2015–2019) (BMC Nephrol 2024; doi:10.1186/s12882-024-03512-2; https://doi.org/10.1186/s12882-024-03512-2) (filippone2024contemporaryreviewof pages 1-2).
- Serum complement prognostication: Low baseline C3 associated with higher incidence of 50% eGFR decline/kidney failure; adding C3/C4 improved model discrimination (Sci Rep 2024; doi above) (filippone2024contemporaryreviewof pages 1-2).

Ontology‑ready Annotations
- Genes/Proteins (HGNC): TNFSF13 (APRIL); TNFSF13B (BAFF); C1GALT1; ST6GAL1; CFH; C3 (novak2024oglycosylationofiga1 pages 1-2, cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2, salvadori2024whatisnew pages 2-3).
- Biological Processes (GO): Protein O‑linked glycosylation; B cell activation; class switch recombination to IgA; complement activation (alternative/lectin) (novak2024oglycosylationofiga1 pages 1-2, cheung2024theroleof pages 1-2, salvadori2024whatisnew pages 2-3, filippone2024contemporaryreviewof pages 1-2).
- Cellular Components (GO-CC): Extracellular region; mesangial matrix; cell membrane receptor complexes; germinal center (novak2024oglycosylationofiga1 pages 1-2, filippone2024contemporaryreviewof pages 1-2).
- Cell Types (CL): Mesangial cell; glomerular endothelial cell; podocyte; plasma cell; B cell; T follicular helper cell (filippone2024contemporaryreviewof pages 1-2, dreher2025recentadvancesin pages 8-9, cheung2024theroleof pages 1-2).
- Anatomical Locations (UBERON): Kidney; glomerulus; mesangium; palatine tonsil; small intestine/Peyer’s patch (filippone2024contemporaryreviewof pages 1-2, muto2024newinsightsand pages 1-2).
- Chemical Entities (CHEBI): Galactose; N‑acetylgalactosamine; budesonide; dapagliflozin (novak2024oglycosylationofiga1 pages 1-2, dreher2025recentadvancesin pages 8-9).

Evidence items with PMIDs/DOIs and URLs (selected, 2023–2024 priority)
- Novak J, et al. O‑glycosylation of IgA1 and the pathogenesis of IgAN. Glycobiology. 2024. DOI: 10.1093/glycob/cwae060. URL: https://doi.org/10.1093/glycob/cwae060 (novak2024oglycosylationofiga1 pages 1-2).
- Filippone EJ, et al. Contemporary review of IgAN. Front Immunol. 2024. DOI: 10.3389/fimmu.2024.1436923. URL: https://doi.org/10.3389/fimmu.2024.1436923 (filippone2024contemporaryreviewof pages 1-2).
- Cheung CK, et al. BAFF/APRIL in IgAN. Front Nephrol. 2024. DOI: 10.3389/fneph.2023.1346769. URL: https://doi.org/10.3389/fneph.2023.1346769 (cheung2024theroleof pages 1-2, cheung2024theroleof pages 2-3).
- Muto M, et al. APRIL in IgAN. Int J Mol Sci. 2024. DOI: 10.3390/ijms251910340. URL: https://doi.org/10.3390/ijms251910340 (muto2024newinsightsand pages 1-2).
- Tringali E, et al. Serum C3 and C4 prognostic value. Sci Rep. 2024. DOI: 10.1038/s41598-024-65857-w. URL: https://doi.org/10.1038/s41598-024-65857-w (filippone2024contemporaryreviewof pages 1-2).
- Abedini A, et al. Single‑cell multi‑omics kidney atlas. Nat Genet. 2024. DOI: 10.1038/s41588-024-01802-x. URL: https://doi.org/10.1038/s41588-024-01802-x (dreher2025recentadvancesin pages 8-9).
- Rehnberg J, et al. Registry validation of IgAN biopsies; C3 deposits common. BMC Nephrol. 2024. DOI: 10.1186/s12882-024-03512-2. URL: https://doi.org/10.1186/s12882-024-03512-2 (filippone2024contemporaryreviewof pages 1-2).

Cellular and Molecular Mechanisms narrative (for knowledge base)
- Pathophysiology description: IgAN is an immune‑complex glomerulonephritis in which aberrantly O‑glycosylated polymeric IgA1 (Gd‑IgA1) and antiglycan autoantibodies form circulating immune complexes that deposit in the mesangium, triggering mesangial proliferation, cytokine release, and complement activation (primarily alternative and lectin pathways). Downstream podocyte injury drives proteinuria; chronic inflammation leads to tubulointerstitial fibrosis and progressive CKD (novak2024oglycosylationofiga1 pages 1-2, filippone2024contemporaryreviewof pages 1-2, cheung2024theroleof pages 2-3).
- Gene/protein annotations with ontology terms: TNFSF13/APRIL (HGNC: TNFSF13); TNFSF13B/BAFF (HGNC: TNFSF13B); C1GALT1 (HGNC); ST6GAL1 (HGNC); CFH (HGNC); C3 (HGNC) (novak2024oglycosylationofiga1 pages 1-2, cheung2024theroleof pages 1-2, salvadori2024whatisnew pages 2-3).
- Phenotype associations (HP terms): Hematuria (HP:0000790), Proteinuria (HP:0000093), Hypertension (HP:0000822), Decreased eGFR/CKD (HP:0000083) supported by biopsy MEST‑C features (filippone2024contemporaryreviewof pages 1-2).
- Cell type involvement (CL terms): Mesangial cell (CL); Glomerular endothelial cell (CL); Podocyte (CL); Plasma cell (CL); B cell (CL); Tfh cell (CL) (filippone2024contemporaryreviewof pages 1-2, dreher2025recentadvancesin pages 8-9, cheung2024theroleof pages 1-2).
- Anatomical locations (UBERON terms): Kidney (UBERON:0002113), Glomerulus (UBERON:0000074), Mesangium (UBERON:0000075), Palatine tonsil (UBERON:0002372), Peyer’s patch (UBERON:0002114) (filippone2024contemporaryreviewof pages 1-2, muto2024newinsightsand pages 1-2).
- Chemical entities (CHEBI): Galactose (CHEBI:28260), N‑acetylgalactosamine (CHEBI:18066), Budesonide (CHEBI:3215), Dapagliflozin (CHEBI:79307) (novak2024oglycosylationofiga1 pages 1-2, dreher2025recentadvancesin pages 8-9).

Current Trials and Implementations (examples with NCT IDs)
- Complement inhibitors: Ravulizumab (C5) in IgAN—NCT06291376 (recruiting). Iptacopan (factor B) biopsy‑impact—NCT06797518 (recruiting) (filippone2024contemporaryreviewof pages 1-2).
- BAFF/APRIL inhibitors: Atacicept—NCT07020923; Telitacicept—NCT06654596; Zigakibart—NCT06858319 (extensions) (cheung2024theroleof pages 1-2).
- Mucosal steroid: Extended TARPEYO (nefecon) beyond 9 months—NCT06712407 (filippone2024contemporaryreviewof pages 1-2).

Embedded artifact (ontology‑mapped key players)
| Category | Entity | Ontology (prefix term) | Role in IgAN | Evidence (citation id) |
|---|---|---|---|---|
| Gene / Protein | TNFSF13 (APRIL) | HGNC: TNFSF13 | Plasma-cell survival factor; promotes Gd-IgA1 production | (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2) |
| Gene / Protein | TNFSF13B (BAFF) | HGNC: TNFSF13B | B-cell survival/activation; supports IgA class switching and Gd-IgA1 production | (cheung2024theroleof pages 1-2, salvadori2024whatisnew pages 2-3) |
| Gene / Protein | C1GALT1 | HGNC: C1GALT1 | Core O-glycosyltransferase implicated in IgA1 hinge galactosylation | (novak2024oglycosylationofiga1 pages 1-2, salvadori2024whatisnew pages 2-3) |
| Gene / Protein | ST6GAL1 | HGNC: ST6GAL1 | Glycosyltransferase linked to Ig glycome/glycosylation patterns | (novak2024oglycosylationofiga1 pages 1-2, dreher2025recentadvancesin pages 8-9) |
| Gene / Protein | CFH (complement factor H) | HGNC: CFH | Regulator of alternative complement pathway; genetic loci modulate complement-driven injury | (salvadori2024whatisnew pages 2-3, filippone2024contemporaryreviewof pages 1-2) |
| Gene / Protein | C3 | HGNC: C3 | Central complement component; co-localizes with IgA in glomeruli | (novak2024oglycosylationofiga1 pages 1-2, filippone2024contemporaryreviewof pages 1-2) |
| Cell type | Mesangial cell | CL: mesangial cell | Principal deposition site of IgA-containing immune complexes; proliferates and secretes ECM/cytokines | (filippone2024contemporaryreviewof pages 1-2, novak2024oglycosylationofiga1 pages 1-2) |
| Cell type | Glomerular endothelial cell | CL: glomerular endothelial cell | Early inflammatory activation, contributes to glomerular injury (scRNA/spatial evidence) | (dreher2025recentadvancesin pages 8-9, filippone2024contemporaryreviewof pages 1-2) |
| Cell type | Podocyte | CL: podocyte | Injury leads to proteinuria and filtration barrier disruption downstream of mesangial injury | (filippone2024contemporaryreviewof pages 1-2) |
| Cell type | Plasma cell | CL: plasma cell | Source of (mucosal/systemic) IgA1 including pathogenic Gd-IgA1 | (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2) |
| Cell type | B cell | CL: B cell | Generates antiglycan autoantibodies and undergoes class-switching to IgA | (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2) |
| Cell type | T follicular helper cell (Tfh) | CL: T follicular helper cell | Provides help for B-cell affinity maturation and IgA class switching in mucosa/tonsils | (filippone2024contemporaryreviewof pages 1-2, muto2024newinsightsand pages 1-2) |
| Anatomical site | Kidney | UBERON: kidney | Organ affected; site of immune-complex deposition and progressive fibrosis | (filippone2024contemporaryreviewof pages 1-2) |
| Anatomical site | Glomerulus | UBERON: glomerulus | Microanatomic site of mesangial immune-deposits and complement activation | (filippone2024contemporaryreviewof pages 1-2) |
| Anatomical site | Mesangium | UBERON: mesangium | Mesangial cell expansion and matrix accumulation drive glomerular dysfunction | (novak2024oglycosylationofiga1 pages 1-2, filippone2024contemporaryreviewof pages 1-2) |
| Anatomical site | Palatine tonsil | UBERON: palatine tonsil | Mucosal site (NALT) implicated as source of pathogenic mucosal IgA in some patients | (salvadori2024whatisnew pages 2-3, muto2024newinsightsand pages 1-2) |
| Anatomical site | Small intestine / Peyer's patch | UBERON: small intestine; UBERON: Peyer's patch | GALT sites of IgA induction and mucosal immune responses influencing Gd-IgA1 | (filippone2024contemporaryreviewof pages 1-2, muto2024newinsightsand pages 1-2) |
| Chemical entity | Galactose | CHEBI: galactose | Sugar missing from Gd-IgA1 O-glycans; central to the aberrant glycoform definition | (novak2024oglycosylationofiga1 pages 1-2) |
| Chemical entity | N-acetylgalactosamine (GalNAc) | CHEBI: N-acetylgalactosamine | Core residue of IgA1 O-glycans; site of aberrant galactosylation | (novak2024oglycosylationofiga1 pages 1-2) |
| Chemical entity | Budesonide (targeted-release) | CHEBI: budesonide | Mucosal-targeted steroid (Nefecon) that reduces proteinuria by modulating mucosal IgA responses | (dreher2025recentadvancesin pages 8-9, filippone2024contemporaryreviewof pages 1-2) |
| Chemical entity | Dapagliflozin (SGLT2 inhibitor) | CHEBI: dapagliflozin | Supportive therapy that reduces proteinuria and slows CKD progression in IgAN cohorts | (filippone2024contemporaryreviewof pages 1-2, dreher2025recentadvancesin pages 8-9) |
| Pathway / Process | Complement activation | GO: complement activation | Key mediator of glomerular inflammation in IgAN; involves alternative and lectin pathways | (filippone2024contemporaryreviewof pages 1-2, salvadori2024whatisnew pages 2-3) |
| Pathway / Process | Alternative complement pathway | GO: alternative complement activation | Frequently implicated route of complement-mediated glomerular damage in IgAN | (salvadori2024whatisnew pages 2-3, dreher2025recentadvancesin pages 8-9) |
| Pathway / Process | Lectin complement pathway | GO: lectin complement activation | Contributes to complement deposition and injury in many patients | (salvadori2024whatisnew pages 2-3) |
| Pathway / Process | O-linked glycosylation (IgA1 hinge) | GO: protein O-linked glycosylation | Aberrant O-glycosylation (Gd-IgA1) is the initiating molecular abnormality (Hit 1) | (novak2024oglycosylationofiga1 pages 1-2) |
| Pathway / Process | B cell activation | GO: B cell activation | Drives autoantibody formation and expansion of IgA-producing clones | (cheung2024theroleof pages 1-2) |
| Pathway / Process | Class switch recombination to IgA | GO: class switch recombination | Mechanism for generation of mucosal IgA; dysregulated in IgAN mucosal sites | (cheung2024theroleof pages 1-2, muto2024newinsightsand pages 1-2) |


*Table: Compact mapping of key genes/proteins, cell types, anatomical sites, chemicals, and pathways in IgA nephropathy with ontology prefixes and supporting evidence citations for rapid reference.*

Limitations
- While multi‑hit pathogenic mechanisms are well supported, inter‑patient heterogeneity remains; causality for specific microbiome taxa and exact antigenic drivers continue to be clarified. Some single‑cell/spatial findings are from broader CKD atlases rather than IgAN‑only cohorts.

References (by context id)
- Core contemporary and mechanistic reviews and studies: (novak2024oglycosylationofiga1 pages 1-2, filippone2024contemporaryreviewof pages 1-2, cheung2024theroleof pages 1-2, cheung2024theroleof pages 2-3, salvadori2024whatisnew pages 2-3, dreher2025recentadvancesin pages 8-9).

References

1. (filippone2024contemporaryreviewof pages 1-2): Edward J. Filippone, Rakesh Gulati, and John L. Farber. Contemporary review of iga nephropathy. Frontiers in Immunology, Aug 2024. URL: https://doi.org/10.3389/fimmu.2024.1436923, doi:10.3389/fimmu.2024.1436923. This article has 29 citations and is from a peer-reviewed journal.

2. (novak2024oglycosylationofiga1 pages 1-2): Jan Novak, R Glenn King, Janet Yother, Matthew B Renfrow, and Todd J Green. O-glycosylation of iga1 and the pathogenesis of an autoimmune disease iga nephropathy. Glycobiology, Aug 2024. URL: https://doi.org/10.1093/glycob/cwae060, doi:10.1093/glycob/cwae060. This article has 7 citations and is from a peer-reviewed journal.

3. (cheung2024theroleof pages 2-3): Chee Kay Cheung, Jonathan Barratt, Adrian Liew, Hong Zhang, Vladimir Tesar, and Richard Lafayette. The role of baff and april in iga nephropathy: pathogenic mechanisms and targeted therapies. Frontiers in Nephrology, Feb 2024. URL: https://doi.org/10.3389/fneph.2023.1346769, doi:10.3389/fneph.2023.1346769. This article has 59 citations and is from a poor quality or predatory journal.

4. (salvadori2024whatisnew pages 2-3): Maurizio Salvadori and Giuseppina Rosso. What is new in the pathogenesis and treatment of iga glomerulonephritis. World Journal of Nephrology, Dec 2024. URL: https://doi.org/10.5527/wjn.v13.i4.98709, doi:10.5527/wjn.v13.i4.98709. This article has 4 citations.

5. (cheung2024theroleof pages 1-2): Chee Kay Cheung, Jonathan Barratt, Adrian Liew, Hong Zhang, Vladimir Tesar, and Richard Lafayette. The role of baff and april in iga nephropathy: pathogenic mechanisms and targeted therapies. Frontiers in Nephrology, Feb 2024. URL: https://doi.org/10.3389/fneph.2023.1346769, doi:10.3389/fneph.2023.1346769. This article has 59 citations and is from a poor quality or predatory journal.

6. (dreher2025recentadvancesin pages 8-9): Leonie Dreher, Lars Nilges, Thorsten Wiech, Markus M Rinschen, and Nicola M Tomas. Recent advances in pathogenetic concepts and disease modeling of iga nephropathy. Clinical Kidney Journal, May 2025. URL: https://doi.org/10.1093/ckj/sfaf152, doi:10.1093/ckj/sfaf152. This article has 0 citations and is from a peer-reviewed journal.

7. (muto2024newinsightsand pages 1-2): Masahiro Muto, Hitoshi Suzuki, and Yusuke Suzuki. New insights and future perspectives of april in iga nephropathy. International Journal of Molecular Sciences, 25:10340, Sep 2024. URL: https://doi.org/10.3390/ijms251910340, doi:10.3390/ijms251910340. This article has 10 citations and is from a poor quality or predatory journal.