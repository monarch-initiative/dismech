---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T10:17:27.116090'
end_time: '2025-12-15T10:25:25.042608'
duration_seconds: 477.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vitiligo
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Vitiligo
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Vitiligo**.
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
- **Disease Name:** Vitiligo
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Vitiligo**.
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
- Disease Name: Vitiligo
- MONDO ID: 
- Category: Complex

Pathophysiology description (narrative)
Vitiligo is an autoimmune depigmenting disorder marked by selective loss of epidermal melanocytes. Converging evidence supports a multi-hit model: environmental and metabolic stress in melanocytes leads to oxidative damage and unfolded protein response (UPR), release of danger signals (notably inducible HSP70), and activation of innate pathways (e.g., type I interferons), which license keratinocytes and dendritic cells to drive a type 1 (IFN-γ–dominant) adaptive response. Keratinocyte-derived chemokines CXCL9 and CXCL10 recruit and retain CXCR3+ cytotoxic CD8+ T cells that kill melanocytes via perforin/granzyme and Fas-FasL pathways; these T cells also establish tissue-resident memory (TRM) populations maintained by IL‑15, enabling relapse from lesional margins. Genetic susceptibility loci in immune regulation (e.g., HLA, PTPN22, IFIH1, BACH2, IRF4) and melanocyte biology (e.g., TYR) modulate risk and disease course. Melanocyte adhesion defects and stromal signals (e.g., DKK1/Wnt, MMP9/E‑cadherin) further destabilize melanocyte survival in the basal epidermis. Together, these mechanisms produce well-demarcated hypopigmented macules and, when hair follicle melanocyte reservoirs are affected, leukotrichia. (iwanowski2023etiopathogenesisandemerging pages 1-2, iwanowski2023etiopathogenesisandemerging pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8, speeckaert2024vitiligofrompathogenesis pages 2-4)

1) Core Pathophysiology
- Primary mechanisms
  - Oxidative stress/UPR and DAMPs: Patients demonstrate systemic oxidative imbalance with reduced antioxidant defenses (TAS, catalase, GPx, GST) and elevated oxidation products (MDA, AOPP). Oxidative damage promotes keratinocyte and melanocyte stress responses that include HSP70i release, a key DAMP that activates dendritic/plasmacytoid dendritic cells and type I IFN pathways. (kassab2023seruminflammatoryand pages 5-8, kassab2023seruminflammatoryand pages 1-2, iwanowski2023etiopathogenesisandemerging pages 1-2)
  - IFN-γ–CXCL9/CXCL10–CXCR3 axis: IFN‑γ induces keratinocyte CXCL9/CXCL10, recruiting CXCR3+ CD8+ T cells that mediate melanocyte killing; JAK/STAT signaling is central. Elevated serum CXCL9/CXCL10 associate with disease activity. (iwanowski2023etiopathogenesisandemerging pages 1-2, aulakh2024differentialexpressionof pages 1-2)
  - Innate activation: DAMP‑driven activation of pDCs and DCs promotes type I interferon signaling, antigen presentation, and licensing of Th1/cytotoxic immunity; NK cells and other innate lymphoid cells participate in bridging innate to adaptive responses. (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)
  - IL‑15–TRM axis: IL‑15 promotes survival and cytotoxic function of CD49a+ CD8+ TRM cells in skin, supporting persistence/relapse; serum IL‑15 is elevated and correlates with extent. (iwanowski2023etiopathogenesisandemerging pages 1-2, kassab2023seruminflammatoryand pages 5-8)
  - Melanocyte adhesion and stromal cues: IFN‑γ and MMP9 can disrupt E‑cadherin-mediated adhesion; Wnt/β‑catenin antagonism (e.g., DKK1) and DDR1 signaling affect melanocyte localization/survival. (yamaguchi2024pathogenesisofalopecia pages 7-8)

- Dysregulated molecular pathways
  - IFN pathways (type I and type II), JAK/STAT; chemokine networks (CXCL9, CXCL10/CXCR3); IL‑15 signaling; oxidative stress/UPR; inflammasome components; apoptosis and cytotoxic granule pathways; Wnt/β‑catenin and adhesion signaling. (iwanowski2023etiopathogenesisandemerging pages 1-2, yamaguchi2024pathogenesisofalopecia pages 7-8, speeckaert2024vitiligofrompathogenesis pages 2-4)

- Affected cellular processes
  - Antigen presentation; chemotaxis and tissue homing; cytotoxic lymphocyte effector function; oxidative stress response and proteostasis; adhesion and extracellular matrix interactions; memory T-cell formation and tissue residency. (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - Immune regulation: HLA class I/II, PTPN22, IFIH1 (MDA5), BACH2, IRF4, FOXP3; checkpoint/activation components (JAK1/2, STAT1), cytokines/chemokines (IFNG, IL15, CXCL9, CXCL10, CXCR3); cytotoxic mediators (GZMB, PRF1). (iwanowski2023etiopathogenesisandemerging pages 1-2, yamaguchi2024pathogenesisofalopecia pages 7-8)
  - Melanocyte biology: TYR (tyrosinase); adhesion/remodeling: MMP9, DDR1; Wnt modulators: DKK1. (yamaguchi2024pathogenesisofalopecia pages 7-8, speeckaert2024vitiligofrompathogenesis pages 2-4)
  - DAMPs/stress sensors: HSP70 (HSPA1A), oxidative enzymes (CAT, SOD1/2, GPX1), inflammasome components (NLRP1/3). (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

- Chemical Entities (CHEBI) and drugs
  - Oxidants/ROS (CHEBI:26523; CHEBI:41741); antioxidant enzymes/activity measures; emerging/approved immunomodulators that act on these pathways (e.g., JAK inhibitors). (speeckaert2024vitiligofrompathogenesis pages 2-4, iwanowski2023etiopathogenesisandemerging pages 1-2)

- Cell Types (selected)
  - Effector and resident memory CD8+ T cells, keratinocytes, plasmacytoid/conventional dendritic cells, NK cells/innate lymphoid cells, regulatory T cells, B cells, monocytes/macrophages. (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

- Anatomical Locations
  - Epidermal basal layer (melanocyte niche), papillary dermis, hair follicle bulge/outer root sheath (melanocyte stem cell reservoir), lesional and perilesional skin. (speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

3) Biological Processes (GO annotation; examples)
- GO:0034341 response to interferon-gamma; GO:0034340 response to type I interferon; GO:0006955 immune response; GO:0007160 cell-matrix adhesion; GO:0006915 apoptotic process; GO:0030595 leukocyte chemotaxis; GO:0006979 response to oxidative stress; GO:0035966 endoplasmic reticulum unfolded protein response; GO:0042438 melanin biosynthetic process. (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

4) Cellular Components (examples)
- Plasma membrane (chemokine receptors, adhesion molecules), immunological synapse, cytotoxic granules, ER (UPR), mitochondria (ROS generation), extracellular space (DAMPs, chemokines). (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

5) Disease Progression (sequence of events)
- Trigger/exposure (e.g., UV/trauma/metabolic stress) → melanocyte oxidative stress and UPR → DAMP release (HSP70i) → dendritic cell/pDC activation and type I IFN → keratinocyte IFN-γ–inducible chemokines (CXCL9, CXCL10) → recruitment/retention of CXCR3+ CD8+ T cells → cytotoxic melanocyte killing (perforin/granzyme; Fas-FasL) → establishment of IL‑15–dependent CD8+ TRM maintaining local susceptibility and relapse. (iwanowski2023etiopathogenesisandemerging pages 1-2, iwanowski2023etiopathogenesisandemerging pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

6) Phenotypic Manifestations (HP terms; examples)
- Vitiligo (depigmented macules/patches), often symmetrical; leukotrichia (white hairs in lesions); Koebner phenomenon; peri-lesional inflammatory border in active disease. These phenotypes arise from melanocyte loss in basal epidermis and involvement of follicular melanocyte reservoirs. (speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

Embedded mechanism-to-entity map
| Mechanism | Key Molecules (HGNC / CHEBI) | Principal Cells (CL terms) | Core Processes (GO terms) | Anatomical Sites (UBERON terms) | Biomarkers / Readouts | Representative Evidence (PMID / DOI / URL / year, context) |
| --- | --- | --- | --- | --- | --- | --- |
| IFN-γ → CXCL9/CXCL10 → CXCR3 recruitment axis | IFNG, CXCL9, CXCL10, CXCR3, JAK1/JAK2 | CXCR3+ CD8+ T cells (TRM and effector), keratinocytes, antigen-presenting cells | GO:0034341 response to interferon-gamma; GO:0006955 immune response | Epidermis (basal layer), papillary dermis (UBERON:0001004) | Serum/tissue IFN‑γ, CXCL9, CXCL10; JAK‑STAT activation signatures | Iwanowski et al., Int J Mol Sci 2023; DOI:10.3390/ijms24119749 (iwanowski2023etiopathogenesisandemerging pages 1-2), Yamaguchi et al., Int J Mol Sci 2024; DOI:10.3390/ijms25084409 (yamaguchi2024pathogenesisofalopecia pages 7-8) |
| Oxidative stress / UPR → HSP70i (DAMP) release | HSPA1A (HSP70i), ROS (CHEBI:41741), MMP9 | Stressed melanocytes, keratinocytes, Langerhans cells (DCs) | GO:0006979 response to oxidative stress; GO:0035966 unfolded protein response | Epidermal basal layer (melanocyte niche), hair follicle outer root sheath | Oxidative markers (MDA, AOPP), catalase/SOD activity, HSP70 expression | Iwanowski et al., Int J Mol Sci 2023; DOI:10.3390/ijms24119749 (iwanowski2023etiopathogenesisandemerging pages 1-2), Speeckaert et al., J Clin Med 2024; DOI:10.3390/jcm13175225 (speeckaert2024vitiligofrompathogenesis pages 2-4) |
| Innate immune activation (pDC / DC / NK / ILCs) bridging to adaptive immunity | IFNA genes, TLRs, NLRP3/NLRP1, GNLY (granulysin) | Plasmacytoid DCs, conventional DCs, NK cells, ILCs, macrophages | GO:0002250 adaptive immune response; GO:0002376 immune system process; GO:0034340 response to type I interferon | Epidermis, dermis (papillary dermis), draining lymph nodes | Type I IFN signatures, antigen presentation markers, granulysin in lesional skin | Iwanowski et al., Int J Mol Sci 2023; DOI:10.3390/ijms24119749 (iwanowski2023etiopathogenesisandemerging pages 1-2), Speeckaert et al., J Clin Med 2024; DOI:10.3390/jcm13175225 (speeckaert2024vitiligofrompathogenesis pages 2-4) |
| IL-15–driven TRM survival and relapse | IL15, IL15RA, CD69, ITGA1 (CD49a), BCL2 | CD8+ tissue-resident memory T cells (TRM), CD49a+ resident CD8+ cells, keratinocytes (IL‑15 source) | GO:0042093 T cell proliferation; GO:0070669 regulation of T cell activation | Perilesional & non-lesional epidermis; hair follicle bulge niches | Elevated IL-15 (serum/skin); persistence of CD69+CD103+ TRM; granzyme B/perforin expression | Iwanowski et al., Int J Mol Sci 2023; DOI:10.3390/ijms24119749 (iwanowski2023etiopathogenesisandemerging pages 1-2), Yamaguchi et al., Int J Mol Sci 2024; DOI:10.3390/ijms25084409 (yamaguchi2024pathogenesisofalopecia pages 7-8) |
| Melanocyte adhesion loss & mitochondrial dysfunction → apoptosis/ferroptosis | TYR, DKK1, DDR1, MMP9, mitochondrial ROS (CHEBI:41741) | Mature melanocytes, melanocyte stem/progenitor cells (hair follicle) | GO:0006915 apoptotic process; GO:0071456 cellular response to oxidative stress; GO:0042438 melanin biosynthetic process | Epidermal basal layer; hair follicle bulge / outer root sheath | Reduced TYR expression; leukotrichia; mitochondrial dysfunction assays; increased DKK1 | Yamaguchi et al., Int J Mol Sci 2024; DOI:10.3390/ijms25084409 (yamaguchi2024pathogenesisofalopecia pages 7-8), Speeckaert et al., J Clin Med 2024; DOI:10.3390/jcm13175225 (speeckaert2024vitiligofrompathogenesis pages 2-4) |
| Genetic susceptibility: immune & melanocyte loci (polygenic risk) | HLA loci, PTPN22, TYR, NLRP1, IFIH1, BACH2, IRF4, FOXP3 | Influences T cells, APCs and melanocyte biology (systemic immune cells) | GO:0006955 immune response; GO:0042438 melanin biosynthetic process | Systemic (immune organs) with skin manifestation (epidermis) | GWAS risk alleles; altered expression of immune genes in blood/skin; population allele-frequency variation | Reviews/GWAS summarized in Iwanowski et al., Int J Mol Sci 2023; DOI:10.3390/ijms24119749 (iwanowski2023etiopathogenesisandemerging pages 1-2), Yamaguchi et al., Int J Mol Sci 2024; DOI:10.3390/ijms25084409 (yamaguchi2024pathogenesisofalopecia pages 7-8) |


*Table: Concise mapping of principal vitiligo pathogenic mechanisms to molecules, cell types, GO/UBERON annotations, key biomarkers, and representative 2023–2024 evidence (context citations included).*

Recent developments and latest research (2023–2024; selected findings with data)
- Systemic oxidative stress and inflammation in patients (2023): In 96 subjects (30 active, 30 stable vitiligo; 36 controls), total antioxidant status (TAS), catalase, GPx, and GST were significantly lower in vitiligo vs controls, while SOD was higher. Oxidation products were elevated (MDA active 5.30±1.00 vs controls 4.50±1.20; AOPP active 250.15±200.20 vs controls 100.45±50.18). CRP was higher in active vs stable (4.46±1.09 vs 3.75±1.08). Authors conclude that “oxidative damage induces an increase in pro-inflammatory IL‑15, which in turn promotes IFN‑γ‑inducible chemokines such as CXCL9 and CXCL10.” Published 9 Sep 2023; URL: https://doi.org/10.3390/jcm12185861. (kassab2023seruminflammatoryand pages 5-8, kassab2023seruminflammatoryand pages 1-2)
- Chemokines as activity biomarkers (2024): In a cross-sectional study (60 vitiligo, 30 controls), serum CXCL9 and CXCL10 were significantly elevated in patients (p=0.001 each) and correlated with VASI (both p=0.001) and VIDA (CXCL9 p=0.032; CXCL10 p=0.001), supporting their mechanistic role and biomarker utility. Epub July 2024; URL: https://doi.org/10.25259/ijdvl_793_2023. (aulakh2024differentialexpressionof pages 1-2)
- Mechanistic quotes (supporting chemokine biology): “CXCL9 plays the role of a ‘recruit’ signal… CXCL10 acts as a tethering signal that increases T cell activity and controls their movement,” summarizing the coordinated recruitment/retention of CXCR3+ effector cells. 9 Sep 2023; URL: https://doi.org/10.3390/jcm12185861. (kassab2023seruminflammatoryand pages 2-4)
- Integrated mechanistic reviews (2023–2024): The 2023 and 2024 reviews synthesize the dominance of the IFN‑γ–JAK/STAT–CXCL9/10 pathway, the role of HSP70i as a DAMP linking oxidative stress to innate activation, and the contribution of IL‑15 to TRM maintenance and relapse. URLs: 2023 (https://doi.org/10.3390/ijms24119749), 2024 (https://doi.org/10.3390/jcm13175225; https://doi.org/10.3390/ijms25084409). (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

Current applications and real-world implementations
- JAK/STAT pathway inhibition: Targeting the IFN‑γ–JAK/STAT axis with JAK inhibitors is a leading therapeutic strategy; topical JAK inhibitors (e.g., ruxolitinib) have been adopted clinically and are often combined with NB‑UVB to enhance repigmentation. Review notes: “Immunomodulatory therapies, especially those targeting the JAK‑IFNγ pathway, are currently at the forefront,” and combination with phototherapy is “impressive.” 16 Sep 2024; URL: https://doi.org/10.3390/jcm13175225. (speeckaert2024vitiligofrompathogenesis pages 2-4)
- Biomarker-informed monitoring: Serum CXCL9/CXCL10 correlate with VASI/VIDA, supporting their use as activity biomarkers; elevated IL‑15 and oxidative markers (MDA/AOPP) may complement assessment. 2023–2024 URLs: https://doi.org/10.3390/jcm12185861; https://doi.org/10.25259/ijdvl_793_2023. (kassab2023seruminflammatoryand pages 5-8, aulakh2024differentialexpressionof pages 1-2)

Expert opinions and analysis from authoritative sources
- 2024 narrative reviews emphasize a convergence model linking oxidative stress, innate activation, and type 1 adaptive immunity in both segmental and non-segmental disease, with TRM cells explaining relapse and recalcitrance; Wnt/adhesion biology contributes to melanocyte vulnerability. URLs: https://doi.org/10.3390/jcm13175225; https://doi.org/10.3390/ijms25084409. (speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)
- 2023 mechanistic review highlights HSP70i as a principal DAMP and consolidates GWAS evidence indicating predominantly immune loci with a minority of melanocyte loci, consistent with autoimmune pathogenesis. URL: https://doi.org/10.3390/ijms24119749. (iwanowski2023etiopathogenesisandemerging pages 1-2)

Relevant statistics and data from recent studies
- Oxidative stress and inflammation (mean ± SD; 2023 cohort): TAS active 1.70±0.45 vs controls 2.05±0.22; CAT 34.75±3.5 vs 38.5±3.1; GPx 1.72±0.85 vs 2.20±0.44; GST 18.12±4.1 vs 20.00±1.23; SOD 3.70±0.75 vs 3.15±1.02; MDA 5.30±1.00 vs 4.50±1.20; AOPP 250.15±200.20 vs 100.45±50.18; CRP active 4.46±1.09 vs stable 3.75±1.08. (Published 9 Sep 2023; https://doi.org/10.3390/jcm12185861). (kassab2023seruminflammatoryand pages 5-8)
- Chemokine activity biomarkers (2024 cohort): Serum CXCL9 and CXCL10 significantly higher in vitiligo vs controls (both p=0.001) with positive correlations to VASI (both p=0.001) and VIDA (CXCL9 p=0.032; CXCL10 p=0.001). (https://doi.org/10.25259/ijdvl_793_2023). (aulakh2024differentialexpressionof pages 1-2)

Structured annotations
- Gene/protein annotations (HGNC)
  - IFNG; CXCL9; CXCL10; CXCR3; IL15; JAK1; JAK2; STAT1; HSPA1A (HSP70i); TYR; PTPN22; IFIH1; BACH2; IRF4; FOXP3; MMP9; DDR1; GZMB; PRF1. (iwanowski2023etiopathogenesisandemerging pages 1-2, yamaguchi2024pathogenesisofalopecia pages 7-8, speeckaert2024vitiligofrompathogenesis pages 2-4)

- Biological processes (GO; examples)
  - GO:0034341 response to interferon-gamma; GO:0034340 response to type I interferon; GO:0006955 immune response; GO:0007160 cell-matrix adhesion; GO:0030595 leukocyte chemotaxis; GO:0006979 response to oxidative stress; GO:0035966 ER UPR; GO:0042438 melanin biosynthesis. (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

- Phenotype associations (HP terms; examples)
  - Vitiligo (depigmented macules/patches), leukotrichia (white hairs), Koebner phenomenon. (speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

- Cell type involvement (CL terms; labels)
  - CD8+ cytotoxic T lymphocytes (including TRM), keratinocytes, dendritic cells (including pDCs), NK cells/ILCs, regulatory T cells, monocytes/macrophages, B cells, melanocytes. (iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4)

- Anatomical locations (UBERON terms; labels)
  - Epidermis (basal layer), papillary dermis, hair follicle bulge/outer root sheath; lesional and perilesional skin. (speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

- Chemical entities (CHEBI; labels)
  - Reactive oxygen species; lipid peroxidation products (MDA), advanced oxidation protein products (AOPP). (kassab2023seruminflammatoryand pages 5-8)

Evidence items with PMIDs/DOIs and dates
- Kassab et al., Journal of Clinical Medicine, 9 Sep 2023. “Serum inflammatory and oxidative stress markers in patients with vitiligo.” DOI: 10.3390/jcm12185861; URL: https://doi.org/10.3390/jcm12185861. Quantitative oxidative stress, IL‑15, and CXCL9/CXCL10 data. (kassab2023seruminflammatoryand pages 5-8, kassab2023seruminflammatoryand pages 1-2, kassab2023seruminflammatoryand pages 2-4)
- Aulakh et al., Indian J Dermatol Venereol Leprol, Epub Jul 2024. “Differential expression of serum CXCL9 and CXCL10….” DOI: 10.25259/IJDVL_793_2023; URL: https://doi.org/10.25259/ijdvl_793_2023. Chemokine levels correlate with VASI/VIDA. (aulakh2024differentialexpressionof pages 1-2)
- Iwanowski et al., Int J Mol Sci, 5 Jun 2023. “Etiopathogenesis and Emerging Methods for Treatment of Vitiligo.” DOI: 10.3390/ijms24119749; URL: https://doi.org/10.3390/ijms24119749. Mechanistic review: HSP70i, IFN‑γ–CXCL9/10–CXCR3, IL‑15/TRM, genetics. (iwanowski2023etiopathogenesisandemerging pages 1-2, iwanowski2023etiopathogenesisandemerging pages 2-4)
- Speeckaert et al., J Clin Med, 16 Sep 2024. “Vitiligo: From Pathogenesis to Treatment.” DOI: 10.3390/jcm13175225; URL: https://doi.org/10.3390/jcm13175225. Mechanisms (DAMPs, chemokines), therapeutic implications (JAK inhibitors + phototherapy). (speeckaert2024vitiligofrompathogenesis pages 2-4)
- Yamaguchi et al., Int J Mol Sci, 16 Apr 2024. “Pathogenesis of Alopecia Areata and Vitiligo: Commonalities and Differences.” DOI: 10.3390/ijms25084409; URL: https://doi.org/10.3390/ijms25084409. IFN‑γ axis, adhesion/Wnt pathways, shared genetics, innate cells. (yamaguchi2024pathogenesisofalopecia pages 7-8, yamaguchi2024pathogenesisofalopecia pages 4-5, yamaguchi2024pathogenesisofalopecia pages 11-13)
- Meta-analytic synthesis on cytokines (contextual): Paganelli et al., Life, 30 Apr 2025. “Comprehensive Overview of Cytokine Interplay….” DOI: 10.3390/life15050684; URL: https://doi.org/10.3390/life15050684. Summarizes IFN‑γ and IL‑17 roles; supportive context. (paganelli2025comprehensiveoverviewof pages 3-5, paganelli2025comprehensiveoverviewof pages 12-13)

Direct supporting quotes
- “CXCL9 plays the role of a ‘recruit’ signal… CXCL10 acts as a tethering signal that increases T cell activity and controls their movement.” (Kassab 2023; 9 Sep 2023; https://doi.org/10.3390/jcm12185861). (kassab2023seruminflammatoryand pages 2-4)
- Reviews emphasize the IFN‑γ–JAK/STAT–CXCL9/10 axis and TRM: “Immunomodulatory therapies, especially those targeting the JAK‑IFNγ pathway, are currently at the forefront.” (Speeckaert 2024; 16 Sep 2024; https://doi.org/10.3390/jcm13175225). (speeckaert2024vitiligofrompathogenesis pages 2-4)

Notes and limitations
- While single-cell studies of peripheral and lesional compartments are rapidly advancing, the quantitative scRNA-seq findings requested here were not extractable from the available evidence context. Nevertheless, multiple reviews consolidate that innate and adaptive immune activation signatures (type I/II IFN responses, antigen presentation) are elevated in skin and peripheral immune cells in vitiligo. (speeckaert2024vitiligofrompathogenesis pages 2-4, iwanowski2023etiopathogenesisandemerging pages 1-2)

Overall synthesis
Vitiligo pathophysiology reflects a convergence of oxidative stress and innate sensing with a dominant IFN‑γ–driven chemokine circuit that recruits and sustains CXCR3+ cytotoxic responses in the epidermis. IL‑15–maintained TRM underlies relapse and chronicity, while adhesion/Wnt dysregulation and genetic susceptibility bias melanocytes toward loss. Recent 2023–2024 clinical and biomarker studies provide quantitative support for systemic oxidative stress and the IFN‑γ–CXCL9/CXCL10 axis as practical activity biomarkers, with therapeutic implications for JAK/STAT and IL‑15–targeted strategies. (kassab2023seruminflammatoryand pages 5-8, aulakh2024differentialexpressionof pages 1-2, iwanowski2023etiopathogenesisandemerging pages 1-2, speeckaert2024vitiligofrompathogenesis pages 2-4, yamaguchi2024pathogenesisofalopecia pages 7-8)

References

1. (iwanowski2023etiopathogenesisandemerging pages 1-2): Tomasz Iwanowski, Karol Kołkowski, Roman Janusz Nowicki, and Małgorzata Sokołowska-Wojdyło. Etiopathogenesis and emerging methods for treatment of vitiligo. International Journal of Molecular Sciences, 24:9749, Jun 2023. URL: https://doi.org/10.3390/ijms24119749, doi:10.3390/ijms24119749. This article has 43 citations and is from a poor quality or predatory journal.

2. (iwanowski2023etiopathogenesisandemerging pages 2-4): Tomasz Iwanowski, Karol Kołkowski, Roman Janusz Nowicki, and Małgorzata Sokołowska-Wojdyło. Etiopathogenesis and emerging methods for treatment of vitiligo. International Journal of Molecular Sciences, 24:9749, Jun 2023. URL: https://doi.org/10.3390/ijms24119749, doi:10.3390/ijms24119749. This article has 43 citations and is from a poor quality or predatory journal.

3. (yamaguchi2024pathogenesisofalopecia pages 7-8): Hiroki L. Yamaguchi, Yuji Yamaguchi, and Elena Peeva. Pathogenesis of alopecia areata and vitiligo: commonalities and differences. International Journal of Molecular Sciences, 25:4409, Apr 2024. URL: https://doi.org/10.3390/ijms25084409, doi:10.3390/ijms25084409. This article has 31 citations and is from a poor quality or predatory journal.

4. (speeckaert2024vitiligofrompathogenesis pages 2-4): Reinhart Speeckaert, Elise Van Caelenberg, Arno Belpaire, Marijn M. Speeckaert, and Nanja van Geel. Vitiligo: from pathogenesis to treatment. Journal of Clinical Medicine, 13:5225, Sep 2024. URL: https://doi.org/10.3390/jcm13175225, doi:10.3390/jcm13175225. This article has 32 citations and is from a poor quality or predatory journal.

5. (kassab2023seruminflammatoryand pages 5-8): Asma Kassab, Yassine Khalij, Yosra Ayed, Najla Dar-Odeh, Amal A. Kokandi, Meriam Denguezli, and Monia Youssef. Serum inflammatory and oxidative stress markers in patients with vitiligo. Journal of Clinical Medicine, 12:5861, Sep 2023. URL: https://doi.org/10.3390/jcm12185861, doi:10.3390/jcm12185861. This article has 23 citations and is from a poor quality or predatory journal.

6. (kassab2023seruminflammatoryand pages 1-2): Asma Kassab, Yassine Khalij, Yosra Ayed, Najla Dar-Odeh, Amal A. Kokandi, Meriam Denguezli, and Monia Youssef. Serum inflammatory and oxidative stress markers in patients with vitiligo. Journal of Clinical Medicine, 12:5861, Sep 2023. URL: https://doi.org/10.3390/jcm12185861, doi:10.3390/jcm12185861. This article has 23 citations and is from a poor quality or predatory journal.

7. (aulakh2024differentialexpressionof pages 1-2): Shayna Aulakh, Seema Goel, Loveleen Kaur, Samridhi Gulati, Maninder Kaur, Dimple Chopra, Rishu Sarangal, and Jayati Batra. Differential expression of serum cxcl9 and cxcl10 levels in vitiligo patients and their correlation with disease severity and stability: a cross-sectional study. Indian journal of dermatology, venereology and leprology, 91:1-7, Jul 2024. URL: https://doi.org/10.25259/ijdvl\_793\_2023, doi:10.25259/ijdvl\_793\_2023. This article has 7 citations.

8. (kassab2023seruminflammatoryand pages 2-4): Asma Kassab, Yassine Khalij, Yosra Ayed, Najla Dar-Odeh, Amal A. Kokandi, Meriam Denguezli, and Monia Youssef. Serum inflammatory and oxidative stress markers in patients with vitiligo. Journal of Clinical Medicine, 12:5861, Sep 2023. URL: https://doi.org/10.3390/jcm12185861, doi:10.3390/jcm12185861. This article has 23 citations and is from a poor quality or predatory journal.

9. (yamaguchi2024pathogenesisofalopecia pages 4-5): Hiroki L. Yamaguchi, Yuji Yamaguchi, and Elena Peeva. Pathogenesis of alopecia areata and vitiligo: commonalities and differences. International Journal of Molecular Sciences, 25:4409, Apr 2024. URL: https://doi.org/10.3390/ijms25084409, doi:10.3390/ijms25084409. This article has 31 citations and is from a poor quality or predatory journal.

10. (yamaguchi2024pathogenesisofalopecia pages 11-13): Hiroki L. Yamaguchi, Yuji Yamaguchi, and Elena Peeva. Pathogenesis of alopecia areata and vitiligo: commonalities and differences. International Journal of Molecular Sciences, 25:4409, Apr 2024. URL: https://doi.org/10.3390/ijms25084409, doi:10.3390/ijms25084409. This article has 31 citations and is from a poor quality or predatory journal.

11. (paganelli2025comprehensiveoverviewof pages 3-5): Alessia Paganelli, Cristina Cristofoletti, Francesco Moro, Alessandra Corrente, Laura Colonna, Emanuele Scala, and Mauro Picardo. Comprehensive overview of cytokine interplay in vitiligo: a decade of meta-analyses systematically reviewed. Life, 15:684, Apr 2025. URL: https://doi.org/10.3390/life15050684, doi:10.3390/life15050684. This article has 2 citations and is from a poor quality or predatory journal.

12. (paganelli2025comprehensiveoverviewof pages 12-13): Alessia Paganelli, Cristina Cristofoletti, Francesco Moro, Alessandra Corrente, Laura Colonna, Emanuele Scala, and Mauro Picardo. Comprehensive overview of cytokine interplay in vitiligo: a decade of meta-analyses systematically reviewed. Life, 15:684, Apr 2025. URL: https://doi.org/10.3390/life15050684, doi:10.3390/life15050684. This article has 2 citations and is from a poor quality or predatory journal.