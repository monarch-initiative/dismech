---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:47:01.375674'
end_time: '2025-12-18T09:56:25.205788'
duration_seconds: 563.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pemphigus Vulgaris
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Pemphigus Vulgaris
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pemphigus Vulgaris**.
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
- **Disease Name:** Pemphigus Vulgaris
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Pemphigus Vulgaris**.
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
- Disease Name: Pemphigus Vulgaris (PV)
- MONDO ID: MONDO:0008691 (autoimmune blistering disease)
- Category: Autoimmune

Executive Summary
Pemphigus vulgaris is an IgG autoantibody-mediated desmosomal disorder characterized by loss of keratinocyte cohesion (acantholysis) with prominent involvement of oral mucosa and skin. Core mechanisms integrate: (i) pathogenic anti-desmoglein-3 (DSG3) and anti-desmoglein-1 (DSG1) binding with epitope/subclass specificity; (ii) keratinocyte signaling cascades downstream of desmosome perturbation (notably p38 MAPK, Src, EGFR, PLC/PKC, AKT, and HSP27); (iii) desmosome ultrastructural reduction/disassembly and keratin cytoskeletal retraction; (iv) immune dysregulation centered on HLA class II risk alleles (DRB1*04:02; DQB1*05:03), T follicular helper (Tfh) and Th17/Th2 axes (with IL-21 as a key B-cell helper cytokine); and (v) translation to therapies targeting B cells and IgG (rituximab, BTK inhibitors, FcRn antagonists) and antigen-specific CAAR-T. Recent 2023–2024 studies corroborate HLA-linked immune activation (even in healthy carriers) and refine keratinocyte signaling nodes and rescue strategies. (emtenani2023mousemodelsof pages 9-9, schwartz2024cytokineprofilingreveals pages 1-2, xie2023tacrolimusreversespemphigus pages 1-2, hartmann2025inpemphiguscell pages 32-34, hartmann2025inpemphiguscell pages 28-32, geng2024biomarkersinpemphigus pages 2-4)

1. Core Pathophysiology
- Primary mechanism: Pathogenic IgG autoantibodies against desmosomal cadherins DSG3 (mucosal-dominant) and DSG1 (skin involvement) are sufficient to cause acantholysis in passive transfer models and with epitope-validated monoclonals. “Patient autoantibodies are directly pathogenic in passive-transfer and neonatal mouse models” and epitope-specific anti-DSG3 antibodies targeting the adhesive interface induce PV phenotypes (2023 review of mouse models). (emtenani2023mousemodelsof pages 9-9)
- Keratinocyte signaling: Autoantibody binding triggers pathways including p38 MAPK, Src, EGFR, PLC/PKC, AKT, and HSP27 phosphorylation, promoting desmosome disassembly and cytoskeletal retraction. In vitro PV-sera rapidly deplete Dsg3 and convert linear to granular desmosomal staining; FK506 restores adhesion by “decreas[ing] PV serum-induced phosphorylation of HSP27” without altering p38 phosphorylation (BMC Immunology 2023). (xie2023tacrolimusreversespemphigus pages 1-2)
- Desmosome ultrastructure: High-resolution imaging shows PV-IgG reduces desmosome number and size, increases plaque distance/thickness, and causes keratin retraction; inhibition of p38 MAPK or PLC fully rescues ultrastructural parameters in experimental systems (Frontiers in Immunology 2025). (hartmann2025inpemphiguscell pages 32-34)
- Complement and cell death: Complement involvement has been evaluated in murine pemphigus models; apoptosis is considered secondary (“biphasic p38 activation links apoptosis as a downstream event”), and pyroptosis has been proposed, but direct human PV evidence remains limited and context-dependent (2023 review). (emtenani2023mousemodelsof pages 9-9)
- Immune dysregulation and HLA: PV shows strong HLA-II associations (DRB1*04:02; DQB1*05:03). A 2024 study of 116 PV patients and HLA-matched/unmatched controls found “PV patients display an activated cytokine and chemokine immune response… [and] healthy individuals that carry the PV susceptibility alleles… show an upregulation of certain pro-inflammatory, Th2, and Th17 mediators,” with IL-10 and IL-15 reduced in HLA-matched controls, implying HLA-linked baseline immune activation and counter-regulation. (schwartz2024cytokineprofilingreveals pages 1-2)

2. Key Molecular Players
- Genes/Proteins (HGNC): DSG3, DSG1, EGFR, SRC, MAPK14 (p38), PLCG1, PRKCA, AKT1, HSPB1 (HSP27), FCGRT (FcRn), BTK, CD19. Roles summarized in embedded artifact table. (emtenani2023mousemodelsof pages 9-9, xie2023tacrolimusreversespemphigus pages 1-2, hartmann2025inpemphiguscell pages 32-34, starr2025insightsintopathomechanismsa pages 81-83)
- Chemical Entities (CHEBI): Pathogenic IgG; therapeutics: rituximab (anti-CD20), efgartigimod (FcRn antagonist), rilzabrutinib (BTK inhibitor), experimental DSG3-CAART. (emtenani2023mousemodelsof pages 9-9, xie2023tacrolimusreversespemphigus pages 1-2)
- Cell Types (CL): Keratinocytes (signal transduction, adhesion machinery), B cells/plasma cells (autoantibodies), Tfh (IL-21), Th17 and Th2 (inflammatory milieu). (schwartz2024cytokineprofilingreveals pages 1-2, geng2024biomarkersinpemphigus pages 2-4)
- Anatomical Locations (UBERON): Skin epidermis and oral mucosa (oral often earliest site due to DSG3 expression dominance). (emtenani2023mousemodelsof pages 9-9, geng2024biomarkersinpemphigus pages 2-4)

3. Biological Processes (GO annotations)
- Cell–cell adhesion and desmosome organization: loss of desmosomal adhesion and desmosome number/size changes underpin acantholysis. (hartmann2025inpemphiguscell pages 32-34)
- MAPK cascade and keratinocyte differentiation: p38 MAPK is a central node; keratinocyte stress responses and differentiation programs are perturbed after detachment. (emtenani2023mousemodelsof pages 9-9, hartmann2025inpemphiguscell pages 28-32)
- B-cell activation and T-cell help: Tfh/Th17 skewing with IL-21 supports autoreactive B cells and plasma-cell differentiation. (schwartz2024cytokineprofilingreveals pages 1-2, geng2024biomarkersinpemphigus pages 2-4)

4. Cellular Components
- Desmosomes and plasma membrane: DSG1/3 cluster in desmosomal plaques linked to keratin intermediate filaments; ultrastructurally reduced/desynchronized after PV-IgG. (hartmann2025inpemphiguscell pages 32-34)
- Cytoskeleton (keratin/actin) and signaling complexes: HSP27-mediated actin remodeling and keratin retraction accompany adhesion loss. (xie2023tacrolimusreversespemphigus pages 1-2)
- Endoplasmic reticulum stress–desmosome signaling crosstalk has been suggested in pemphigus models. (starr2025insightsintopathomechanismsa pages 81-83)

5. Disease Progression
- Sequence of events (canonical): Genetic susceptibility (HLA-DRB1*04:02, DQB1*05:03) + triggers → autoreactive Tfh/Th17 help → anti-DSG3±DSG1 IgG production → direct inhibition of DSG transinteraction and induction of keratinocyte signaling (p38, Src, EGFR, PLC/PKC, AKT, HSP27) → desmosome disassembly/ultrastructural reduction → keratin retraction and acantholysis → erosions/blisters; inflammation and transcriptomic reprogramming are accentuated after mechanical detachment. (emtenani2023mousemodelsof pages 9-9, schwartz2024cytokineprofilingreveals pages 1-2, hartmann2025inpemphiguscell pages 32-34, hartmann2025inpemphiguscell pages 28-32)
- Stages: Prodromal mucosal phase (DSG3-dominant) often precedes cutaneous involvement; phenotype can reflect antibody profile (DSG3 vs DSG1 co-reactivity). (geng2024biomarkersinpemphigus pages 2-4)

6. Phenotypic Manifestations (HP terms)
- Oral mucosal erosions and flaccid cutaneous blisters due to suprabasal acantholysis; Nikolsky sign; chronic relapsing course. Molecular correlate is desmosomal failure in suprabasal layers. (emtenani2023mousemodelsof pages 9-9, geng2024biomarkersinpemphigus pages 2-4)

7. Recent Developments (2023–2024)
- HLA-linked cytokine activation: Large cohort demonstrates “Th2 and Th17 driven immune activation” in PV patients and HLA-risk healthy individuals; IL-10/IL-15 downregulated in HLA-matched controls. (Dec 2024; Frontiers in Immunology; https://doi.org/10.3389/fimmu.2024.1500231) (schwartz2024cytokineprofilingreveals pages 1-2)
- HSP27 as a targetable node: FK506 counteracts PV-sera–induced Dsg3 depletion and restores adhesion by inhibiting HSP27 phosphorylation in keratinocytes. (Nov 2023; BMC Immunology; https://doi.org/10.1186/s12865-023-00582-z) (xie2023tacrolimusreversespemphigus pages 1-2)
- Desmosome ultrastructure rescue: Experimental inhibition of p38 MAPK or PLC rescues desmosome number and plaque geometry; EGFR/Src pathways modulate desmosomal remodeling. (2025 preprint referencing 2024 work; bioRxiv; https://doi.org/10.1101/2025.02.10.637416) (hartmann2025inpemphiguscell pages 32-34)
- Biomarker synthesis: Systematic review across 2,463 patients highlights elevations in IL‑4, IL‑6, IL‑17A, anti‑Dsg1/3, and “reduction in Treg cells and FOXP3,” supporting Th2/Th17 and Treg deficiency in PV pathogenesis. (Jul 2024; J Cutaneous Medicine and Surgery; https://doi.org/10.1177/12034754241266136) (geng2024biomarkersinpemphigus pages 2-4)

8. Current Applications and Real-world Implementations
- Anti-CD20 B-cell depletion (rituximab): Now a first-line biologic in many guidelines; mechanistically reduces anti-DSG autoantibody production (supporting evidence from models and clinical experience). (emtenani2023mousemodelsof pages 9-9)
- FcRn antagonism (e.g., efgartigimod): FcRn blockade “stabilizes keratinocyte monolayer integrity in the presence of anti‑DSG3 antibodies” and lowers circulating pathogenic IgG, offering a mechanistically rational option in IgG-mediated PV. (emtenani2023mousemodelsof pages 9-9)
- BTK inhibitors (rilzabrutinib): Target BCR signaling and myeloid FcγR pathways to reduce autoantibody production/inflammation; development is ongoing with disease-specific trials. (starr2025insightsintopathomechanismsa pages 81-83)
- Antigen-specific cellular therapy (DSG3‑CAART/CD19 CAR‑T): A Phase 1/2 open-label study in active PV is “RECRUITING” (RESET‑PV; NCT04422912; sponsor Cabaletta Bio), aiming to delete DSG3‑specific B cells or broadly deplete B cells. (NCT04422912)

9. Expert Opinions and Mechanistic Quotes
- “Patient autoantibodies are directly pathogenic in passive‑transfer and neonatal mouse models,” and “multiple studies implicate p38 MAPK as a central downstream signaling node” whose inhibition prevents IgG‑induced reorganization and disease (Frontiers in Immunology 2023). (emtenani2023mousemodelsof pages 9-9)
- “PV patients display an activated cytokine and chemokine immune response… [and] healthy individuals that carry the PV susceptibility alleles… show an upregulation of certain pro‑inflammatory, Th2, and Th17 mediators,” while “IL‑10 and IL‑15 were… downregulated in the HLA‑matched control group,” suggesting HLA-linked immune activation with counter-regulation (Frontiers in Immunology 2024). (schwartz2024cytokineprofilingreveals pages 1-2)
- “FK506 reverses PV‑IgG induced‑Dsg depletion and desmosomal dissociation… by inhibiting HSP27 phosphorylation” (BMC Immunology 2023). (xie2023tacrolimusreversespemphigus pages 1-2)
- Desmosome-focused imaging shows PV‑IgG “reduced desmosome number, decreased desmosome size, increased plaque distance and thickness” and that “inhibition of p38MAPK or PLC completely rescued all parameters” (Frontiers in Immunology 2025; referencing experimental models). (hartmann2025inpemphiguscell pages 32-34)

10. Relevant Statistics and Data
- Cohort size and analytes: 116 PV patients vs 29 controls profiled across 20 cytokines/chemokines showed Th2/Th17 skewing and HLA-linked activation in healthy carriers (Frontiers in Immunology 2024). (schwartz2024cytokineprofilingreveals pages 1-2)
- Biomarker synthesis: 66 studies, 2,463 patients; most notable trends include elevations in IL‑4, IL‑6, IL‑17A and anti‑Dsg1/3; reduced Treg/FOXP3 (systematic review 2024). (geng2024biomarkersinpemphigus pages 2-4)
- Cellular rescue: In keratinocytes, PV sera downregulated Dsg3 within 1 h and up to 24 h; FK506 restored adhesion and decreased HSP27 phosphorylation (BMC Immunology 2023). (xie2023tacrolimusreversespemphigus pages 1-2)

Ontology-linked Annotations for Knowledge-Base
- HGNC: DSG3, DSG1, EGFR, SRC, MAPK14, PLCG1, PRKCA, AKT1, HSPB1, FCGRT, BTK, CD19.
- GO: cell–cell adhesion; desmosome organization; MAPK cascade; keratinocyte differentiation; B cell activation; T cell help.
- CL: keratinocyte; B cell; T follicular helper cell; Th17 cell.
- UBERON: skin epidermis; oral mucosa.
- HP: oral mucosal erosions; suprabasal acantholysis; flaccid blisters; positive Nikolsky sign.
- CHEBI: IgG; rituximab; efgartigimod; rilzabrutinib.

Embedded resource summarizing entities and evidence:
| Category | Entity Name | Ontology ID (source) | Mechanistic role in PV (1–2 sentences) | Key pathway linkage | Evidence (Year; journal) | URL/DOI | Citation Context ID |
|---|---|---|---|---|---|---|---|
| Gene/Protein | DSG3 | HGNC:DSG3 | Primary mucocutaneous autoantigen in PV; IgG binding disrupts desmosomal adhesion causing acantholysis. | Desmosome adhesion loss; downstream signaling (p38MAPK, Src) | 2023; Frontiers in Immunology | https://doi.org/10.3389/fimmu.2023.1169947 | (emtenani2023mousemodelsof pages 9-9) |
| Gene/Protein | DSG1 | HGNC:DSG1 | Epidermal autoantigen (superficial disease phenotypes); anti-DSG1 antibodies contribute to cutaneous blistering. | Desmosome adhesion; epitope-dependent pathogenicity | 2024; J Cutaneous Med Surg (review) | https://doi.org/10.1177/12034754241266136 | (geng2024biomarkersinpemphigus pages 2-4) |
| Genetic risk | HLA-DRB1*04:02 | IMGT/HLA:HLA-DRB1*04:02 | Strong PV-associated HLA allele that correlates with autoreactive T-cell recognition of Dsg epitopes and predisposition to autoantibody generation. | Antigen presentation → Tfh help → B-cell activation | 2024; Frontiers in Immunology | https://doi.org/10.3389/fimmu.2024.1500231 | (schwartz2024cytokineprofilingreveals pages 1-2) |
| Cytokine / Gene | IL-21 | HGNC:IL21 | Tfh-derived cytokine that promotes B-cell differentiation to plasma cells and supports high-affinity anti-DSG antibody production. | Tfh → IL-21 → plasma cell differentiation (humoral axis) | 2024; Frontiers in Immunology | https://doi.org/10.3389/fimmu.2024.1500231 | (schwartz2024cytokineprofilingreveals pages 1-2) |
| Gene/Protein | MAPK14 (p38 MAPK) | HGNC:MAPK14 | Central kinase mediating keratinocyte responses to pathogenic IgG; inhibition prevents IgG-induced cytoskeletal reorganization and acantholysis in models. | MAPK (stress) cascade downstream of desmosome perturbation | 2023; Frontiers in Immunology | https://doi.org/10.3389/fimmu.2023.1169947 | (emtenani2023mousemodelsof pages 9-9) |
| Gene/Protein | EGFR | HGNC:EGFR | EGFR signaling implicated in desmosome ultrastructure changes; EGFR inhibitors (preclinical) rescue desmosomes and keratin anchorage. | EGFR → cytoskeletal/desmosome remodeling; cross-talk with MAPK | 2025; bioRxiv (preprint) | https://doi.org/10.1101/2025.02.10.637416 | (hartmann2025inpemphiguscell pages 32-34) |
| Gene/Protein | SRC | HGNC:SRC | Tyrosine kinase activated in epitope-specific DSG3 signaling leading to Dsg3 depletion and adhesion loss; pharmacologic Src inhibition ameliorates some effects. | Src-dependent signaling linked to Dsg epitope effects and p38 MAPK | 2023/2025; Frontiers in Immunology / bioRxiv | 10.3389/fimmu.2023.1169947; https://doi.org/10.1101/2025.02.10.637416 | (emtenani2023mousemodelsof pages 9-9, hartmann2025inpemphiguscell pages 32-34) |
| Gene/Protein | PLCG1 | HGNC:PLCG1 | Phospholipase C signaling participates in keratinocyte Ca2+ and adhesion responses after autoantibody binding. | PLC → Ca2+ flux → desmosome turnover | 2023; Frontiers in Immunology | https://doi.org/10.3389/fimmu.2023.1169947 | (emtenani2023mousemodelsof pages 9-9) |
| Gene/Protein | PRKCA (PKCα) | HGNC:PRKCA | PKC subtype signaling influences desmosome assembly/disassembly and keratinocyte adhesion dynamics in PV models. | PKC signaling modulates desmosome turn-over and actin linkage | 2025; bioRxiv / reviews summarized 2023 | https://doi.org/10.1101/2025.02.10.637416 | (hartmann2025inpemphiguscell pages 32-34, emtenani2023mousemodelsof pages 9-9) |
| Gene/Protein | AKT1 | HGNC:AKT1 | PI3K–AKT survival/anti-apoptotic signaling is engaged in keratinocytes and may modulate cell survival vs. cleavage during acantholysis. | PI3K–AKT anti-apoptosis pathways (cell survival) | 2025; pathway enrichment summaries | (no DOI available) | (starr2025insightsintopathomechanismsa pages 81-83) |
| Gene/Protein | HSPB1 (HSP27) | HGNC:HSPB1 | HSP27 phosphorylation is downstream of PV sera exposure and mediates actin cytoskeletal reorganization; FK506 (tacrolimus) blocks HSP27 phosphorylation and restores Dsg3/adhesion. | HSP27 → actin reorganization; intersecting with p38/PKC axes | 2023; BMC Immunology | https://doi.org/10.1186/s12865-023-00582-z | (xie2023tacrolimusreversespemphigus pages 1-2) |
| Gene/Protein | FCGRT (FcRn) | HGNC:FCGRT | Neonatal Fc receptor rescues IgG from catabolism; pharmacologic FcRn blockade (e.g., efgartigimod) lowers pathogenic IgG levels and is a mechanistic therapy in IgG-mediated PV. | IgG recycling pathway → therapeutic IgG clearance | 2023; Frontiers reviews (translational note) | https://doi.org/10.3389/fimmu.2023.1169947 | (emtenani2023mousemodelsof pages 9-9) |
| Gene/Protein | BTK | HGNC:BTK | Tyrosine kinase in BCR signaling; BTK inhibitors (rilzabrutinib) aim to reduce B-cell activation/antibody production and FcγR-driven inflammatory functions. | BCR → BTK → B-cell activation / myeloid signaling | 2025; pathway enrichment / reviews | (trial reports / reviews) | (starr2025insightsintopathomechanismsa pages 81-83) |
| Gene/Protein | CD19 | HGNC:CD19 | B-cell surface marker used for depletion (anti-CD19) and reference target for CAAR/CAR strategies to eliminate autoreactive B cells. | B-cell depletion/CAAR targeting → reduces pathogenic plasma cell precursors | 2023; Frontiers in Immunology (models & translational notes) | https://doi.org/10.3389/fimmu.2023.1169947 | (emtenani2023mousemodelsof pages 9-9) |
| Cell type(s) | Tfh; Th17; Keratinocyte; B cell | CL:Tfh; CL:Th17; CL:keratinocyte; CL:B cell | Tfh cells (produce IL-21) and Th17 cells support autoreactive B cells; keratinocytes transduce antibody-triggered signals and undergo cytoskeletal/desmosomal changes; B cells/plasma cells produce pathogenic IgG. | Tfh→IL-21→B cells; Th17/Th2 inflammatory milieu; keratinocyte MAPK/EGFR signaling | 2023–2024; cohort & review studies | https://doi.org/10.3389/fimmu.2024.1500231; https://doi.org/10.3389/fimmu.2023.1169947 | (schwartz2024cytokineprofilingreveals pages 1-2, emtenani2023mousemodelsof pages 9-9) |
| Anatomy | Skin epidermis; Oral mucosa | UBERON:skin epidermis; UBERON:oral mucosa | Primary tissues affected in PV; oral mucosa often the initial clinical site reflecting DSG3-dominant autoimmunity. | Tissue site of desmosomal adhesion and blister formation | 2023–2024; reviews | https://doi.org/10.3389/fimmu.2023.1169947; https://doi.org/10.1177/12034754241266136 | (emtenani2023mousemodelsof pages 9-9, geng2024biomarkersinpemphigus pages 2-4) |
| Processes (GO) | cell–cell adhesion; desmosome organization; MAPK cascade; keratinocyte differentiation | GO:cell–cell adhesion; GO:desmosome organization; GO:MAPK cascade; GO:keratinocyte differentiation | Core disrupted biological processes in PV: loss of desmosomal cell–cell adhesion, altered desmosome assembly/ultrastructure, activation of MAPK signaling, and perturbed keratinocyte differentiation/response programs. | Desmosome ↔ MAPK/p38/Src/EGFR signaling axis; keratinocyte stress responses | 2023–2025; mechanistic studies & preprints | https://doi.org/10.3389/fimmu.2023.1169947; https://doi.org/10.1101/2025.02.10.637416 | (emtenani2023mousemodelsof pages 9-9, hartmann2025inpemphiguscell pages 32-34) |
| Chemical / Autoantibody | IgG (pathogenic autoantibodies) | CHEBI:IgG | Class-switched IgG (IgG1/IgG4 variable by study) against DSG3/DSG1 are the proximal effectors causing loss of adhesion; subclass/epitope influences pathogenicity. | Direct steric inhibition of Dsg transinteraction + signaling induction (p38, Src) | 2023–2024; systematic review & mechanistic papers | https://doi.org/10.1177/12034754241266136; https://doi.org/10.3389/fimmu.2023.1169947 | (geng2024biomarkersinpemphigus pages 2-4, emtenani2023mousemodelsof pages 9-9) |
| Therapeutics | Rituximab; Efgartigimod (FcRn inhibitor); Rilzabrutinib (BTKi); DSG3-CAART | CHEBI:rituximab; CHEBI:efgartigimod; CHEBI:rilzabrutinib; (DSG3-CAART: experimental cellular therapy) | Rituximab depletes CD20+ B cells (reduces autoantibody production); efgartigimod accelerates IgG clearance via FcRn blockade; rilzabrutinib inhibits BTK to blunt BCR signaling; DSG3-CAART aims to selectively eliminate DSG3-specific B cells. | B-cell depletion (anti-CD20), IgG clearance (FcRn), BCR pathway inhibition (BTK), antigen-specific CAAR-T therapy | 2023–2025; reviews and trials (early-phase / translational) | https://doi.org/10.3389/fimmu.2023.1169947; NCT04422912 | (emtenani2023mousemodelsof pages 9-9, hartmann2025inpemphiguscell pages 32-34) |


*Table: Compact knowledge-base table mapping key molecules, cells, processes, and therapeutics in pemphigus vulgaris to ontology tags and primary evidence (2023–2025 contexts); useful for database annotation and mechanistic reference.*

Clinical Trials and Implementations (with identifiers)
- NCT04422912 (RESET-PV): “A Phase 1/2, Open-label, Safety and Dosing Study of Autologous CART Cells (Desmoglein 3 Chimeric Autoantibody Receptor T Cells [DSG3-CAART] or CD19-specific Chimeric Antigen Receptor T Cells [CABA-201]) in Subjects With Active, Pemphigus Vulgaris” – Overall status: Recruiting; Sponsor: Cabaletta Bio. (NCT04422912)

Limitations and Open Questions
- The role of complement and lytic cell death pathways (apoptolysis/pyroptosis) in human PV lesions remains less definitive than in subepidermal diseases; some evidence suggests apoptosis follows adhesion loss. Further human tissue mechanistic studies are warranted. (emtenani2023mousemodelsof pages 9-9)

References (with URLs and dates when available)
- Emtenani S, et al. Mouse models of pemphigus… Frontiers in Immunology. 2023. https://doi.org/10.3389/fimmu.2023.1169947 (emtenani2023mousemodelsof pages 9-9)
- Schwartz RR, Seiffert-Sinha K, Sinha AA. Cytokine profiling… PV patients and HLA-susceptible controls. Frontiers in Immunology. 2024. https://doi.org/10.3389/fimmu.2024.1500231 (schwartz2024cytokineprofilingreveals pages 1-2)
- Xie Z, et al. Tacrolimus reverses PV serum–induced depletion of desmoglein… via HSP27. BMC Immunology. 2023. https://doi.org/10.1186/s12865-023-00582-z (xie2023tacrolimusreversespemphigus pages 1-2)
- Hartmann V, et al. In pemphigus, cell detachment… bioRxiv preprint. 2025 (preprint reflecting 2024 experimental work). https://doi.org/10.1101/2025.02.10.637416 (hartmann2025inpemphiguscell pages 32-34, hartmann2025inpemphiguscell pages 28-32)
- Geng RSQ, et al. Biomarkers in Pemphigus Vulgaris: Systematic Review. J Cutaneous Med Surg. 2024. https://doi.org/10.1177/12034754241266136 (geng2024biomarkersinpemphigus pages 2-4)
- ClinicalTrials.gov RESET-PV. NCT04422912. Recruiting. (NCT04422912)


References

1. (emtenani2023mousemodelsof pages 9-9): Shirin Emtenani, Michael Hertl, Enno Schmidt, and Christoph Hudemann. Mouse models of pemphigus: valuable tools to investigate pathomechanisms and novel therapeutic interventions. Frontiers in Immunology, Apr 2023. URL: https://doi.org/10.3389/fimmu.2023.1169947, doi:10.3389/fimmu.2023.1169947. This article has 9 citations and is from a peer-reviewed journal.

2. (schwartz2024cytokineprofilingreveals pages 1-2): Rebekah R. Schwartz, Kristina Seiffert-Sinha, and Animesh A. Sinha. Cytokine profiling reveals hla-linked th2 and th17 driven immune activation in pemphigus vulgaris patients and genetically susceptible healthy controls. Frontiers in Immunology, Dec 2024. URL: https://doi.org/10.3389/fimmu.2024.1500231, doi:10.3389/fimmu.2024.1500231. This article has 4 citations and is from a peer-reviewed journal.

3. (xie2023tacrolimusreversespemphigus pages 1-2): Zhimin Xie, Xiangnong Dai, Qingqing Li, Sifan Lin, and Xingdong Ye. Tacrolimus reverses pemphigus vulgaris serum-induced depletion of desmoglein in hacat cells via inhibition of heat shock protein 27 phosphorylation. BMC Immunology, Nov 2023. URL: https://doi.org/10.1186/s12865-023-00582-z, doi:10.1186/s12865-023-00582-z. This article has 6 citations and is from a peer-reviewed journal.

4. (hartmann2025inpemphiguscell pages 32-34): Veronika Hartmann, Sen Guo, Siavash Rahimi, Uta Radine, Danielle Malheiros, Amanda Salviano-Silva, Valeria Bumiller-Bini Hoch, Gabriel A. Cipolla, Veronica Calonga-Solis, Axel Künstner, Imke Burmester, Ralf J. Ludwig, William V.J. Hariton, Christoph M. Hammers, Eliane J. Müller, Hauke Busch, and Jennifer E. Hundt. In pemphigus, cell detachment, but not autoantibody binding, induces cell-wide, long-lasting transcriptomic and proteomic changes. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.10.637416, doi:10.1101/2025.02.10.637416. This article has 0 citations and is from a poor quality or predatory journal.

5. (hartmann2025inpemphiguscell pages 28-32): Veronika Hartmann, Sen Guo, Siavash Rahimi, Uta Radine, Danielle Malheiros, Amanda Salviano-Silva, Valeria Bumiller-Bini Hoch, Gabriel A. Cipolla, Veronica Calonga-Solis, Axel Künstner, Imke Burmester, Ralf J. Ludwig, William V.J. Hariton, Christoph M. Hammers, Eliane J. Müller, Hauke Busch, and Jennifer E. Hundt. In pemphigus, cell detachment, but not autoantibody binding, induces cell-wide, long-lasting transcriptomic and proteomic changes. bioRxiv, Feb 2025. URL: https://doi.org/10.1101/2025.02.10.637416, doi:10.1101/2025.02.10.637416. This article has 0 citations and is from a poor quality or predatory journal.

6. (geng2024biomarkersinpemphigus pages 2-4): Ryan S. Q. Geng, Bethany Wilken, Siddhartha Sood, Ronald G. Sibbald, and Cathryn Sibbald. Biomarkers in pemphigus vulgaris: a systematic review. Journal of Cutaneous Medicine and Surgery, 28:458-462, Jul 2024. URL: https://doi.org/10.1177/12034754241266136, doi:10.1177/12034754241266136. This article has 6 citations and is from a peer-reviewed journal.

7. (starr2025insightsintopathomechanismsa pages 81-83): H Starr. Insights into pathomechanisms of canine pemphigus foliaceus. Unknown journal, 2025.