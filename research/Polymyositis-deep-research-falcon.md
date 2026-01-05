---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:45:16.332272'
end_time: '2025-12-18T09:55:06.559540'
duration_seconds: 590.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Polymyositis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Polymyositis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Polymyositis**.
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
- **Disease Name:** Polymyositis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Polymyositis**.
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
- Disease Name: Polymyositis (PM)
- MONDO ID: MONDO:0005294
- Category: Autoimmune

Overview and current understanding
Polymyositis is an idiopathic inflammatory myopathy characterized pathologically by endomysial inflammation in skeletal muscle with CD8+ cytotoxic T cells invading non-necrotic myofibers that aberrantly express MHC class I, consistent with an antigen-specific, cell-mediated autoimmune process (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22, nishidate2025recentadvancesin pages 1-2). Recent transcriptomic analyses and immunohistologic studies reinforce dysregulation of antigen processing/presentation pathways, interferon-related signaling, and stress responses within myofibers, and support diagnostic utility for immunostains (e.g., MHC class I, CD163) in clinical practice (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, ghang2024expressionofcd163 pages 1-2, nagaraju2005activationofthe pages 5-8).

Core pathophysiology
1) Primary mechanisms
- CD8+ T cell cytotoxicity against non-necrotic fibers: Muscle biopsies in PM show endomysial CD8+ T cells that “invade non-necrotic muscle fibers,” expressing cytotoxic molecules (perforin/granzyme). An antigen-specific in vitro model demonstrated CD8+ T cell invasion into myotubes via MHC class I, with earlier death of invaded myotubes, supporting direct cytotoxicity (Rheumatology 2020; https://doi.org/10.1093/rheumatology/kez248) (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22). “CD8 T-cell infiltration around muscle fibers” with direct damage via myocyte MHC class I is a defining feature (Inflammation & Regeneration 2025; https://doi.org/10.1186/s41232-025-00395-0) (nishidate2025recentadvancesin pages 1-2).
- MHC class I upregulation on myofibers and antigen presentation: PM muscles overexpress MHC class I; omics identify antigen-presentation hub genes (HLA-A/B/C, B2M, TAP1). RNA-seq in PM found upregulation of B2M, TAP1, HLA-C, and TAPBPL (Front Neurol 2023; https://doi.org/10.3389/fneur.2023.1328547) (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, nishidate2025recentadvancesin pages 1-2).
- Interferon signatures and JAK/STAT signaling: Interferon pathways drive MHC I and immune activation in IIM; JAK/STAT is central to IFN signaling, with clinical targeting under evaluation (Front Med 2023; https://doi.org/10.3389/fmed.2023.1158768) (rocca2023targetingintracellularpathways pages 3-4). Although type I IFN signatures are more prominent in dermatomyositis, IFN-γ/STAT1 signaling is implicated in IIM muscle immune activation and MHC I induction (rocca2023targetingintracellularpathways pages 3-4).

2) Key molecular pathways and stress responses
- ER stress/Unfolded Protein Response (UPR): Overexpressed MHC class I localizes to ER (HLA-ABC colocalized with calnexin) and activates robust UPR in myositis muscle (elevated Grp78/BiP; upregulation of PERK/ATF genes; NF-κB activation), linking antigen presentation overload to myofiber stress and dysfunction (Arthritis Rheum 2005; https://doi.org/10.1002/art.21103) (nagaraju2005activationofthe pages 5-8). These mechanisms mechanistically connect MHC I upregulation to ER stress and inflammatory amplification (nagaraju2005activationofthe pages 5-8).
- Regulated cell death and DAMPs: Apoptotic myonuclei occur in IIM with partial invasion; fibres surrounded by CD8+ and granzyme B+ cells and macrophages were enriched for apoptosis, supporting CD8+ T cell–mediated death pathways parallel to partial invasion (PLoS One 2020; https://doi.org/10.1371/journal.pone.0239176) (danielsson2020apoptosisinidiopathic pages 2-3). Necroptosis of myofibers contributes to inflammation and weakness in IIM models of polymyositis; inhibition of necroptosis or the DAMP HMGB1 ameliorated inflammation and weakness, implicating DAMP-driven vicious cycles (Front Immunol 2023; https://doi.org/10.3389/fimmu.2023.1191815) (kamiya2023musclefibernecroptosis pages 11-11, kamiya2023musclefibernecroptosis pages 2-3).

Key molecular players and entities
- Genes/Proteins (HGNC where applicable):
  • HLA-A, HLA-B, HLA-C; B2M (HGNC:914); TAP1; PDIA3; immunoproteasome PSMB8 (HGNC:9536), PSMB9 (HGNC:9538): implicated in PM antigen processing/presentation; hub genes identified in PM (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, nishidate2025recentadvancesin pages 1-2).
  • Cytotoxicity molecules: perforin/granzyme in CD8+ T cells invading fibers (pandya2014tcellsubsets pages 20-22, kamiya2020anewin pages 1-1).
  • Interferon pathway/JAK-STAT: IFN-γ/STAT1 and JAK/STAT signaling implicated in muscle immune activation (rocca2023targetingintracellularpathways pages 3-4).
  • ER stress/UPR: GRP78/BiP, PERK/ATF genes; NF-κB activation downstream of ER overload (nagaraju2005activationofthe pages 5-8).
  • DAMPs: HMGB1 implicated in necroptosis-driven inflammation and muscle dysfunction (kamiya2023musclefibernecroptosis pages 11-11).
  • Autoantigens/autoantibodies relevant to PM subsets: FHL1 (~20% across IIM; enriched in PM/IBM) and TRIM72 (>10% in PM/DM) (nishidate2025recentadvancesin pages 1-2).
- Chemical entities (CHEBI): Not consistently implicated across PM-specific evidence; DAMPs (e.g., HMGB1) function as endogenous inflammatory mediators (kamiya2023musclefibernecroptosis pages 11-11).
- Cell types (CL): CD8+ T cells (principal effectors); macrophages; dendritic cells; B cells/plasma cells may be present in muscle/blood; regulatory T cell alterations suggested by Mendelian randomization (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22, nishidate2025recentadvancesin pages 1-2, yang2024causalitybetweenimmunocytes pages 3-5).
- Anatomical locations (UBERON): Endomysium within skeletal muscle is the site of CD8+ T cell infiltration and myofiber invasion (kamiya2020anewin pages 1-1, nishidate2025recentadvancesin pages 1-2).

Biological processes (GO) disrupted
- Antigen processing and presentation of peptide antigen via MHC class I [GO:0002474] is upregulated in PM muscle (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9).
- T cell–mediated cytotoxicity [GO:0001913] is central to myofiber injury in PM (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22).
- ER stress and UPR pathways drive inflammatory signaling (NF-κB) and contribute to muscle dysfunction (nagaraju2005activationofthe pages 5-8).
- Interferon signaling and JAK/STAT activation in myofibers and the muscle microenvironment (rocca2023targetingintracellularpathways pages 3-4).
- Regulated cell death (apoptosis, necroptosis) and DAMP release perpetuate inflammation (danielsson2020apoptosisinidiopathic pages 2-3, kamiya2023musclefibernecroptosis pages 11-11).

Cellular components (GO)
- MHC class I protein complex [GO:0042612] upregulated at the sarcolemma/ER of myofibers; colocalization with ER markers observed (nagaraju2005activationofthe pages 5-8, jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9).

Disease progression sequence
- Proposed mechanistic cascade: Environmental/immune triggers induce MHC class I upregulation on myofibers → ER stress/UPR and NF-κB activation within muscle → enhanced antigen processing/presentation (HLA-A/B/C, B2M, TAP1) → recruitment and activation of antigen-specific CD8+ T cells (endomysial infiltration) → partial invasion of non-necrotic myofibers and cytotoxic injury (perforin/granzyme) → regulated myofiber death (apoptosis and necroptosis) and DAMP release (e.g., HMGB1), amplifying local inflammation and sustaining weakness (nagaraju2005activationofthe pages 5-8, jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, kamiya2020anewin pages 1-1, danielsson2020apoptosisinidiopathic pages 2-3, kamiya2023musclefibernecroptosis pages 11-11).

Phenotypic manifestations and correlations
- Clinical: Symmetric proximal muscle weakness; elevated CK is typical. In a PM biopsy series, patients with intrafiber CD8+ T cells showed higher CK, linking cytotoxic invasion to biochemical injury (Rheumatology 2020; https://doi.org/10.1093/rheumatology/kez248) (kamiya2020anewin pages 1-1).
- Histopathology: Endomysial CD8+ T cell infiltrates; invasion of non-necrotic myofibers; diffuse myofiber MHC class I upregulation; presence of macrophages; variable B cell/plasma cells (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22, nagaraju2005activationofthe pages 5-8, nishidate2025recentadvancesin pages 1-2).
- Molecular signatures: Upregulated antigen presentation genes (B2M, HLA-C, TAP1, TAPBPL) in PM; IFN-responsive transcripts variably increased; ER stress markers elevated with MHC I overload (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, nagaraju2005activationofthe pages 5-8).

Recent developments (2023–2024) and expert analysis
- PM muscle transcriptomics (2023): PM exhibits enrichment of MHC I antigen processing/presentation with hub genes PDIA3, HLA-C, B2M, and TAP1; provides molecular specificity distinguishing PM from DM and dysferlinopathy (Front Neurol 2023; 12/2023; https://doi.org/10.3389/fneur.2023.1328547) (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9).
- Necroptosis as a therapeutic target (2023): Polymyositis models implicate myofiber necroptosis and DAMPs (HMGB1) in muscle inflammation/weakness; inhibition ameliorates disease, suggesting new treatment avenues beyond immunosuppression (Front Immunol 2023; 07/2023; https://doi.org/10.3389/fimmu.2023.1191815) (kamiya2023musclefibernecroptosis pages 11-11).
- Immunostaining-based diagnostics (2024): An algorithm combining muscular CD163 and MHC class I immunostaining achieved 95.5% diagnostic accuracy (sensitivity 96.1%, specificity 94.5%) in IIM versus controls and correctly classified 94.1% of expert-diagnosed IIM cases not meeting ACR/EULAR criteria (Arthritis Res Ther 2024; 07/2024; https://doi.org/10.1186/s13075-024-03364-z) (ghang2024expressionofcd163 pages 1-2). While this analysis was across IIM, it supports real-world implementation of objective pathology markers that capture the immunopathology relevant to PM.
- Immune-cell causal signals (2024): Mendelian randomization prioritizes CD8+ T cell phenotypes, myeloid markers (CD11b, CD33dim, HLA-DR), and B-cell activation (CD20+, IgD−CD38+) in PM susceptibility/activity, highlighting the combined roles of cytotoxic, myeloid, and B-cell compartments (Medicine 2024; 10/2024; https://doi.org/10.1097/md.0000000000040254). Authors note results did not survive stringent multiple testing but provide directional hypotheses for biomarkers and pathogenesis (yang2024causalitybetweenimmunocytes pages 3-5).
- Interferon/JAK–STAT axis (2023): Review synthesis underscores JAK/STAT coupling to IFN signaling in IIM pathogenesis and therapeutic developments targeting this pathway (Front Med 2023; 03/2023; https://doi.org/10.3389/fmed.2023.1158768) (rocca2023targetingintracellularpathways pages 3-4).

Current applications and implementations
- Diagnostic pathology: Routine assessment of myofiber MHC class I and CD163+ macrophage staining improves diagnostic performance for IIM in clinical practice; algorithmic use can assist pathologists in borderline cases (ghang2024expressionofcd163 pages 1-2).
- Mechanism-informed targets: Evidence supports exploring inhibitors of necroptosis or DAMP pathways (e.g., HMGB1) to complement T cell–directed therapies, particularly where inflammation persists or weakness remains despite immunosuppression (kamiya2023musclefibernecroptosis pages 11-11).
- Pathway-directed therapies: Given IFN/JAK–STAT involvement, judicious consideration of JAK inhibition and interferon-pathway–targeted agents is mechanistically supported in IIM, with strongest evidence in DM but biologically plausible in PM subsets with IFN/STAT signatures (rocca2023targetingintracellularpathways pages 3-4).

Relevant statistics and data
- Immunostaining algorithm (IIM cohort): CD163 positivity 99.2% vs 20.8% in controls; MHC class I 87.6% vs 23.1% (p<0.001); combined CD163+MHC I algorithm accuracy 95.5% (sensitivity 96.1%, specificity 94.5%) (ghang2024expressionofcd163 pages 1-2).
- Autoantibody prevalence (IIM/PM): Anti-FHL1 detected in approximately 20% of IIM, enriched in PM/IBM; anti-TRIM72 in >10% of PM and DM (Inflammation & Regeneration 2025; 10/2025; https://doi.org/10.1186/s41232-025-00395-0) (nishidate2025recentadvancesin pages 1-2).
- Transcriptomic hub genes in PM: Upregulated antigen-presentation genes include B2M, HLA-C, TAP1, TAPBPL; pathway enrichment for antigen processing/presentation (Front Neurol 2023; 12/2023; https://doi.org/10.3389/fneur.2023.1328547) (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9).
- Apoptosis in partial invasion IIM: TUNEL+ myonuclei present in biopsies with partial invasion; fibres with TUNEL+ nuclei were surrounded by CD8+ and granzyme B+ cells and macrophages (PLoS One 2020; 09/2020; https://doi.org/10.1371/journal.pone.0239176) (danielsson2020apoptosisinidiopathic pages 2-3).

Selected evidence quotations
- “The hallmark histopathology of PM is the presence of CD8+ T cells in the non‑necrotic muscle cells.” (Rheumatology 2020; https://doi.org/10.1093/rheumatology/kez248) (kamiya2020anewin pages 1-1).
- “PM is primarily characterized by endomysial CD8+ T-cell infiltration… causing direct cellular damage through interaction with muscle cell MHC class I.” (Inflammation & Regeneration 2025; https://doi.org/10.1186/s41232-025-00395-0) (nishidate2025recentadvancesin pages 1-2).
- “Overexpression of genes related to… MHC class I formation was identified in PM” with hub genes PDIA3, HLA‑C, B2M, TAP1 (Front Neurol 2023; https://doi.org/10.3389/fneur.2023.1328547) (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9).
- “HLA‑ABC colocalized with the ER marker calnexin… Grp78 levels were increased… demonstrating activation of the ER stress response” (Arthritis Rheum 2005; https://doi.org/10.1002/art.21103) (nagaraju2005activationofthe pages 5-8).
- “Apoptotic myonuclei were found… fibres with TUNEL positive nuclei were surrounded by CD8+ T-cells, granzyme B+ cells and macrophages” (PLoS One 2020; https://doi.org/10.1371/journal.pone.0239176) (danielsson2020apoptosisinidiopathic pages 2-3).

Ontology-linked annotations
| Category | Entity (Name) | Ontology ID | Role/Association in PM | Evidence (citation id) |
|---|---|---:|---|---|
| Gene / Protein | HLA-A |  | Upregulated/implicated in MHC class I antigen presentation in PM muscle (supports CD8+ T cell recognition) | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | HLA-B |  | Upregulated/implicated in MHC class I antigen presentation in PM muscle (supports CD8+ T cell recognition) | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | HLA-C |  | Upregulated/implicated in MHC class I antigen presentation in PM muscle (supports CD8+ T cell recognition) | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | B2M | HGNC:914 | Component of MHC class I complex; implicated in antigen presentation in PM muscle | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | PSMB8 | HGNC:9536 | Proteasome subunit (immunoproteasome) — hub gene linked to antigen processing for MHC I in PM | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | PSMB9 | HGNC:9538 | Proteasome subunit (immunoproteasome) — hub gene linked to antigen processing for MHC I in PM | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | FHL1 | HGNC:3700 | Muscle antigen reported as autoantibody target (associated with PM/IBM subsets) | (nishidate2025recentadvancesin pages 1-2) |
| Gene / Protein | TRIM72 / MG53 | HGNC:16265 | Muscle antigen reported as autoantibody target in a subset of PM/DM patients | (nishidate2025recentadvancesin pages 1-2) |
| Process (GO) | Antigen processing and presentation of peptide antigen via MHC class I | GO:0002474 | Central disrupted process in PM: myofiber MHC I upregulation enables CD8+ T cell recognition | (nishidate2025recentadvancesin pages 1-2) |
| Process (GO) | T cell mediated cytotoxicity | GO:0001913 | Effector mechanism: CD8+ cytotoxic T cells invade non-necrotic fibers and mediate cytotoxicity (perforin/granzyme implied) | (yang2024causalitybetweenimmunocytes pages 3-5, nishidate2025recentadvancesin pages 1-2) |
| Cellular Component (GO) | MHC class I protein complex | GO:0042612 | Localized to sarcolemma/myofiber surface when upregulated; enables antigen display to CD8+ T cells | (nishidate2025recentadvancesin pages 1-2) |
| Cell Type (CL) | CD8+ T cell | CL:0000625 | Primary effector cell in PM endomysial infiltrates; mediates invasion/partial invasion of non-necrotic fibers | (yang2024causalitybetweenimmunocytes pages 3-5, nishidate2025recentadvancesin pages 1-2) |
| Cell Type (CL) | Macrophage | CL:0000235 | Present in infiltrates; contribute to inflammation, phagocytosis and cytokine milieu in muscle | (nishidate2025recentadvancesin pages 1-2, yang2024causalitybetweenimmunocytes pages 3-5) |
| Cell Type (CL) | B cell | CL:0000236 | B-cell activation / plasma cells reported in muscle and blood; B-cell phenotypes increased in MR analysis (CD20+) | (yang2024causalitybetweenimmunocytes pages 3-5) |
| Cell Type (CL) | Dendritic cell | CL:0000451 | Antigen-presenting cells that may prime/autonomously present antigen to T cells in muscle microenvironment | (nishidate2025recentadvancesin pages 1-2) |
| Anatomy (UBERON) | Skeletal muscle tissue | UBERON:0001134 | Primary anatomical site of inflammation and antigen presentation in PM | (nishidate2025recentadvancesin pages 1-2) |
| Anatomy (UBERON) | Endomysium | UBERON:0002396 | Microanatomical compartment with endomysial CD8+ T cell infiltrates and fiber invasion in PM | (nishidate2025recentadvancesin pages 1-2, yang2024causalitybetweenimmunocytes pages 3-5) |


*Table: Compact, evidence-linked ontology table mapping genes/proteins, processes, cellular components, cell types and anatomical sites implicated in polymyositis, with supporting context citations to the gathered evidence (nishidate2025recentadvancesin pages 1-2, yang2024causalitybetweenimmunocytes pages 3-5). This table is useful for populating structured disease-knowledge entries.*

Gene/protein annotations (HGNC) and pathways
- HLA-A/B/C (MHC I alpha chains), B2M (HGNC:914), TAP1; PDIA3; immunoproteasome PSMB8 (HGNC:9536), PSMB9 (HGNC:9538): involved in GO:0002474 antigen processing/presentation via MHC I; localized to GO:0042612 MHC I complex (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, nishidate2025recentadvancesin pages 1-2).
- Cytotoxic effectors: perforin/granzyme expressed by CD8+ T cells invading myofibers; process GO:0001913 T cell–mediated cytotoxicity (pandya2014tcellsubsets pages 20-22, kamiya2020anewin pages 1-1).
- ER stress/UPR: GRP78/BiP upregulation; PERK/ATF responses; NF-κB activation; links to MHC I overexpression (nagaraju2005activationofthe pages 5-8).
- Interferon/JAK–STAT: pathway activation contributes to MHC I induction and inflammatory milieu (rocca2023targetingintracellularpathways pages 3-4).

Phenotype associations (HP terms; representative)
- HP:0003323 Proximal muscle weakness of the limbs; HP:0008990 Elevated serum creatine kinase; HP:0003391 Myopathy with endomysial inflammation; Histologic partial invasion of non-necrotic fibers (supported mechanistically by CD8+ cytotoxicity) (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22, nishidate2025recentadvancesin pages 1-2).

Cell types (CL terms)
- CL:0000625 CD8+ T cell (principal effector); CL:0000235 macrophage; CL:0000451 dendritic cell; CL:0000236 B cell (kamiya2020anewin pages 1-1, pandya2014tcellsubsets pages 20-22, nishidate2025recentadvancesin pages 1-2, yang2024causalitybetweenimmunocytes pages 3-5).

Anatomical locations (UBERON terms)
- UBERON:0001134 skeletal muscle tissue; UBERON:0002396 endomysium (kamiya2020anewin pages 1-1, nishidate2025recentadvancesin pages 1-2).

Chemical entities (CHEBI)
- DAMP mediator HMGB1 (endogenous alarmin) implicated in necroptosis-driven inflammation; no PM-specific exogenous chemical drivers consistently implicated in the gathered evidence (kamiya2023musclefibernecroptosis pages 11-11).

Evidence items with PMIDs/DOIs/URLs
- Kamiya M et al. A new in vitro model of polymyositis… Rheumatology (Oxford). 2020-06; doi:10.1093/rheumatology/kez248; URL: https://doi.org/10.1093/rheumatology/kez248 (kamiya2020anewin pages 1-1).
- Jeong H-N et al. Transcriptome analysis… Front Neurol. 2023-12; doi:10.3389/fneur.2023.1328547; URL: https://doi.org/10.3389/fneur.2023.1328547 (jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9).
- Ghang B et al. Expression of CD163 and MHC class I… Arthritis Res Ther. 2024-07; doi:10.1186/s13075-024-03364-z; URL: https://doi.org/10.1186/s13075-024-03364-z (ghang2024expressionofcd163 pages 1-2).
- Danielsson O et al. Apoptosis in IIM with partial invasion… PLoS One. 2020-09; doi:10.1371/journal.pone.0239176; URL: https://doi.org/10.1371/journal.pone.0239176 (danielsson2020apoptosisinidiopathic pages 2-3).
- Nagaraju K et al. Activation of the ER stress response… Arthritis Rheum. 2005-06; doi:10.1002/art.21103; URL: https://doi.org/10.1002/art.21103 (nagaraju2005activationofthe pages 5-8).
- La Rocca G et al. Targeting intracellular pathways… Front Med. 2023-03; doi:10.3389/fmed.2023.1158768; URL: https://doi.org/10.3389/fmed.2023.1158768 (rocca2023targetingintracellularpathways pages 3-4).
- Nishidate A et al. Recent advances… Inflammation & Regeneration. 2025-10; doi:10.1186/s41232-025-00395-0; URL: https://doi.org/10.1186/s41232-025-00395-0 (nishidate2025recentadvancesin pages 1-2).
- Yang N et al. Causality between immunocytes and polymyositis… Medicine (Baltimore). 2024-10; doi:10.1097/MD.0000000000040254; URL: https://doi.org/10.1097/md.0000000000040254 (yang2024causalitybetweenimmunocytes pages 3-5).

Conclusions
Polymyositis pathogenesis is centered on MHC class I–restricted CD8+ T cell–mediated cytotoxicity against non-necrotic myofibers, supported by molecular upregulation of antigen processing/presentation machinery and by ER stress responses within muscle. Interferon/JAK–STAT signaling and regulated cell-death pathways (apoptosis and necroptosis with DAMP release) amplify and sustain tissue injury. Diagnostic immunostaining for MHC class I and CD163 has strong real-world utility to classify IIM—including PM—in pathology workflows. These convergent lines of evidence provide mechanistic anchors for developing targeted therapies (e.g., JAK/STAT modulation, necroptosis/DAMP pathway inhibition) and for biomarker-driven diagnostics in PM (kamiya2020anewin pages 1-1, jeong2023transcriptomeanalysisof pages 1-2, jeong2023transcriptomeanalysisof pages 7-9, nagaraju2005activationofthe pages 5-8, rocca2023targetingintracellularpathways pages 3-4, danielsson2020apoptosisinidiopathic pages 2-3, kamiya2023musclefibernecroptosis pages 11-11, ghang2024expressionofcd163 pages 1-2, nishidate2025recentadvancesin pages 1-2, yang2024causalitybetweenimmunocytes pages 3-5).

References

1. (kamiya2020anewin pages 1-1): Mari Kamiya, Fumitaka Mizoguchi, Akito Takamura, Naoki Kimura, Kimito Kawahata, and Hitoshi Kohsaka. A new in vitro model of polymyositis reveals cd8+ t cell invasion into muscle cells and its cytotoxic role. Rheumatology (Oxford, England), 59:224-232, Jun 2020. URL: https://doi.org/10.1093/rheumatology/kez248, doi:10.1093/rheumatology/kez248. This article has 35 citations.

2. (pandya2014tcellsubsets pages 20-22): J Pandya. T cell subsets and disease mechanisms in inflammatory myopathies. Unknown journal, 2014.

3. (nishidate2025recentadvancesin pages 1-2): Akiko Nishidate, Mariam Piruzyan, Manami Kikuchi, and Yuzo Koda. Recent advances in immunological mechanisms and murine disease models of idiopathic inflammatory myopathies. Inflammation and Regeneration, Oct 2025. URL: https://doi.org/10.1186/s41232-025-00395-0, doi:10.1186/s41232-025-00395-0. This article has 0 citations.

4. (jeong2023transcriptomeanalysisof pages 1-2): Ha-Neul Jeong, Taek Gyu Lee, Hyung Jun Park, Young Yang, Seung-Hun Oh, Seong-Woong Kang, and Young-Chul Choi. Transcriptome analysis of skeletal muscle in dermatomyositis, polymyositis, and dysferlinopathy, using a bioinformatics approach. Frontiers in Neurology, Dec 2023. URL: https://doi.org/10.3389/fneur.2023.1328547, doi:10.3389/fneur.2023.1328547. This article has 1 citations and is from a peer-reviewed journal.

5. (jeong2023transcriptomeanalysisof pages 7-9): Ha-Neul Jeong, Taek Gyu Lee, Hyung Jun Park, Young Yang, Seung-Hun Oh, Seong-Woong Kang, and Young-Chul Choi. Transcriptome analysis of skeletal muscle in dermatomyositis, polymyositis, and dysferlinopathy, using a bioinformatics approach. Frontiers in Neurology, Dec 2023. URL: https://doi.org/10.3389/fneur.2023.1328547, doi:10.3389/fneur.2023.1328547. This article has 1 citations and is from a peer-reviewed journal.

6. (ghang2024expressionofcd163 pages 1-2): Byeongzu Ghang, So Hye Nam, Wonho Choi, Hwa Jung Kim, Jungsun Lee, Doo-Ho Lim, Soo Min Ahn, Ji Seon Oh, Seokchan Hong, Yong-Gil Kim, Chang-Keun Lee, Jinseok Kim, Bin Yoo, and Soo Jeong Nam. Expression of cd163 and major histocompatibility complex class i as diagnostic markers for idiopathic inflammatory myopathies. Arthritis Research & Therapy, Jul 2024. URL: https://doi.org/10.1186/s13075-024-03364-z, doi:10.1186/s13075-024-03364-z. This article has 2 citations and is from a domain leading peer-reviewed journal.

7. (nagaraju2005activationofthe pages 5-8): Kanneboyina Nagaraju, Livia Casciola‐Rosen, Ingrid Lundberg, Rashmi Rawat, Shawna Cutting, Rachana Thapliyal, Jason Chang, Sunita Dwivedi, Megan Mitsak, Yi‐Wen Chen, Paul Plotz, Antony Rosen, Eric Hoffman, and Nina Raben. Activation of the endoplasmic reticulum stress response in autoimmune myositis: potential role in muscle fiber damage and dysfunction. Arthritis and rheumatism, 52 6:1824-35, Jun 2005. URL: https://doi.org/10.1002/art.21103, doi:10.1002/art.21103. This article has 386 citations.

8. (rocca2023targetingintracellularpathways pages 3-4): Gaetano La Rocca, Francesco Ferro, Chiara Baldini, Alessandro Libra, Domenico Sambataro, Michele Colaci, Lorenzo Malatino, Stefano Palmucci, Carlo Vancheri, and Gianluca Sambataro. Targeting intracellular pathways in idiopathic inflammatory myopathies: a narrative review. Frontiers in Medicine, Mar 2023. URL: https://doi.org/10.3389/fmed.2023.1158768, doi:10.3389/fmed.2023.1158768. This article has 17 citations and is from a poor quality or predatory journal.

9. (danielsson2020apoptosisinidiopathic pages 2-3): Olof Danielsson, Bo Häggqvist, Liv Gröntoft, Karin Öllinger, and Jan Ernerudh. Apoptosis in idiopathic inflammatory myopathies with partial invasion; a role for cd8+ cytotoxic t cells? PLoS ONE, 15:e0239176, Sep 2020. URL: https://doi.org/10.1371/journal.pone.0239176, doi:10.1371/journal.pone.0239176. This article has 11 citations and is from a peer-reviewed journal.

10. (kamiya2023musclefibernecroptosis pages 11-11): Mari Kamiya, Naoki Kimura, Natsuka Umezawa, Hisanori Hasegawa, and Shinsuke Yasuda. Muscle fiber necroptosis in pathophysiology of idiopathic inflammatory myopathies and its potential as target of novel treatment strategy. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1191815, doi:10.3389/fimmu.2023.1191815. This article has 15 citations and is from a peer-reviewed journal.

11. (kamiya2023musclefibernecroptosis pages 2-3): Mari Kamiya, Naoki Kimura, Natsuka Umezawa, Hisanori Hasegawa, and Shinsuke Yasuda. Muscle fiber necroptosis in pathophysiology of idiopathic inflammatory myopathies and its potential as target of novel treatment strategy. Frontiers in Immunology, Jul 2023. URL: https://doi.org/10.3389/fimmu.2023.1191815, doi:10.3389/fimmu.2023.1191815. This article has 15 citations and is from a peer-reviewed journal.

12. (yang2024causalitybetweenimmunocytes pages 3-5): Ni Yang, Chang Li, Ruhui Liu, Xianghua Qi, and Xing Qian. Causality between immunocytes and polymyositis: a mendelian randomization analysis. Medicine, 103:e40254, Oct 2024. URL: https://doi.org/10.1097/md.0000000000040254, doi:10.1097/md.0000000000040254. This article has 0 citations and is from a peer-reviewed journal.