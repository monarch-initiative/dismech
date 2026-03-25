---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-20T16:47:37.830402'
end_time: '2026-01-20T16:57:18.747363'
duration_seconds: 580.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Melkersson-Rosenthal syndrome
  mondo_id: ''
  category: Genetic
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
- **Disease Name:** Melkersson-Rosenthal syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Melkersson-Rosenthal syndrome**.
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
- **Disease Name:** Melkersson-Rosenthal syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Melkersson-Rosenthal syndrome**.
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


Plan (current status)
- Completed: (1) identify recent sources; (2) extract core mechanisms; (3) catalog molecular players; (6) create evidence artifact. Pending objectives have been synthesized into the narrative below.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Melkersson–Rosenthal syndrome (MRS)
- MONDO ID: not firmly established in retrieved evidence
- Category: Genetic/immune-mediated granulomatous disorder (etiology incompletely defined)

Pathophysiology description
MRS is a neuromucocutaneous granulomatous disorder defined clinically by the triad of recurrent orofacial edema, relapsing peripheral facial nerve palsy, and fissured tongue; only a minority present with the complete triad, and underdiagnosis with long diagnostic delays is common (age of onset often adolescence/young adult; estimated incidence variably reported 0.2–80 per 100,000 per year) (legert2024oralmanifestationsofa pages 5-7). Histopathology of affected lip mucosa shows non-caseating granulomas with epithelioid histiocytes and perivascular/perineural inflammation; non-caseating granulomas remain the diagnostic gold standard on biopsy in contemporary case descriptions (wu2024acaseof pages 3-5). Orofacial granulomatosis (OFG), which includes Miescher’s cheilitis as a monosymptomatic variant, shares the same granulomatous morphology as oral Crohn disease; the two are indistinguishable histologically, emphasizing immune-mediated granuloma biology in the orofacial mucosa (muller2019noninfectiousgranulomatouslesions pages 4-6).

Emerging lymphatic pathology is suggested by reports of intralymphatic histiocytosis characterized by dilated lymphatic channels lined by D2-40/podoplanin-positive endothelium and filled with CD68-positive histiocytes; these lesions have been associated with chronic inflammation and lymphatic stasis and provide a plausible mechanism for persistent swelling and granuloma persistence in OFG/MRS (extrapolated from skin/dermal cases using lymphatic endothelial markers such as D2-40/podoplanin, Prox1, and LYVE-1) (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4). Immunologically, Th1/Th17 cytokine axes are implicated by therapeutic response of granulomatous cheilitis/OFG to ustekinumab (anti–IL-12/23), and by longstanding evidence that TNF-α and IFN-γ drive granuloma formation and maintenance; case-based discussion links interferon-γ with MRS in the setting of concomitant autoimmunity (coeliac disease and atopy), supporting a T cell–macrophage granulomatous program (taxonera2020recurrentgranulomatouscheilitis pages 2-3, martins2019melkerssonrosenthalsyndromewith pages 1-2). Collectively, current understanding favors an immune-mediated granulomatous process in orofacial tissues with contributions from lymphatic dysfunction, Th1/Th17 cytokines, and macrophage activation, with infectious/allergic triggers plausible in subsets (wu2024acaseof pages 3-5, muller2019noninfectiousgranulomatouslesions pages 4-6, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4, taxonera2020recurrentgranulomatouscheilitis pages 2-3, martins2019melkerssonrosenthalsyndromewith pages 1-2, legert2024oralmanifestationsofa pages 5-7).

Recent developments and latest research (prioritizing 2023–2024)
- 2024 clinical overview emphasizes diagnostic underrecognition, incidence variability, and classic triad with histologic features; reinforces exclusion of Crohn disease and other granulomas in evaluation (legert2024oralmanifestationsofa pages 5-7).
- 2024 case with histologically proven non-caseating granulomas in lip mucosa reiterates tissue-level hallmarks of MRS and documents perivascular and perineural inflammation; quantifies clinical response to multimodal care while highlighting persistent synovial granulomas in a comorbid TMJ site (wu2024acaseof pages 3-5).
- Updated immunopathology linking Th1/Th17 axis: case-based literature review shows ustekinumab induced durable remission of recalcitrant granulomatous cheilitis when anti-TNF therapy failed, strengthening a mechanistic role for IL-12/23-driven T helper programs in orofacial granulomas (though initial report 2020, it remains a current mechanistic anchor and is frequently cited in recent discussions) (taxonera2020recurrentgranulomatouscheilitis pages 2-3).

Current applications and real-world implementations
- Diagnostic practice: lip biopsy targeting mucosa with edema to identify non-caseating granulomas, perivascular lymphocytic infiltrates, and perineural inflammation (wu2024acaseof pages 3-5, legert2024oralmanifestationsofa pages 5-7).
- Immunohistochemistry: when lymphatic involvement is suspected, staining for D2-40/podoplanin, Prox1, and LYVE-1 to demonstrate lymphatic endothelium; CD68 for intraluminal histiocytes consistent with intralymphatic histiocytosis (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).
- Therapeutics: intralesional triamcinolone for labial swelling and oral corticosteroids remain first-line; failure of conventional therapy prompts biologics. Anti–IL-12/23 (ustekinumab) has induced remission of granulomatous cheilitis in refractory cases, supporting pathway targeting; anti-TNF agents (e.g., infliximab) are variably effective, especially in Crohn-associated disease (taxonera2020recurrentgranulomatouscheilitis pages 2-3, legert2024oralmanifestationsofa pages 5-7).

Expert opinions and analysis from authoritative sources
- Head & Neck Pathology review underscores that OFG and oral Crohn disease are histologically indistinguishable, requiring clinicoradiologic correlation and systemic evaluation; this supports a shared immune granuloma program and cautions against overreliance on morphology alone (muller2019noninfectiousgranulomatouslesions pages 4-6).
- Oral medicine overview article (2024) emphasizes that MRS is often oligosymptomatic and underrecognized, with diagnostic value added by histopathology, and positions Miescher’s cheilitis as the most common monosymptomatic variant (legert2024oralmanifestationsofa pages 5-7).
- Dermatopathology series on intralymphatic histiocytosis delineates lymphatic endothelial marker profiles and ties lesions to lymphatic stasis in chronic inflammatory contexts, a pathophysiologic concept congruent with the persistent orofacial edema in MRS/OFG (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).

Relevant statistics and data
- Age of onset typically 14–39 years; mean onset frequently in the second decade; complete triad in only 8–25% of patients; incidence estimates ranging 0.2–80 per 100,000/year (legert2024oralmanifestationsofa pages 5-7).
- In pediatric OFG cohorts, up to 40–72% may develop gastrointestinal Crohn disease over time; oral granulomas are indistinguishable from OFG histologically, anchoring the immune granuloma framework (muller2019noninfectiousgranulomatouslesions pages 4-6).
- Therapeutic evidence: in a literature-based case review, ustekinumab induced remission of granulomatous cheilitis after anti-TNF failure, illustrating translational targeting of IL-12/23 signaling (taxonera2020recurrentgranulomatouscheilitis pages 2-3).

Core Pathophysiology
- Primary mechanisms: immune granuloma formation in orofacial mucosa with epithelioid histiocytes and multinucleated giant cells, perivascular lymphocytic infiltrates, and perineural inflammation; non-caseating granulomas constitute the histologic hallmark (wu2024acaseof pages 3-5, muller2019noninfectiousgranulomatouslesions pages 4-6, legert2024oralmanifestationsofa pages 5-7).
- Dysregulated pathways: Th1/Th17 cytokine axes (IL-12/23 signaling) and TNF/IFN-γ effector programs in macrophage activation and granuloma maintenance; suggested lymphatic dysfunction (intralymphatic histiocytosis) contributing to edema and antigen persistence (taxonera2020recurrentgranulomatouscheilitis pages 2-3, martins2019melkerssonrosenthalsyndromewith pages 1-2, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).
- Affected cellular processes: macrophage activation, T cell activation/differentiation (Th1/Th17), lymphangiogenesis/lymphatic flow abnormalities, antigen presentation in mucosa, perineural inflammation potentially linking to facial nerve dysfunction (wu2024acaseof pages 3-5, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4, legert2024oralmanifestationsofa pages 5-7).

Key Molecular Players
- Genes/Proteins (HGNC terms):
  - TNF (TNF-α): granuloma formation effector cytokine; targeted by infliximab in Crohn-associated orofacial disease (taxonera2020recurrentgranulomatouscheilitis pages 2-3, muller2019noninfectiousgranulomatouslesions pages 4-6).
  - IFNG (IFN-γ): proposed driver in MRS pathophysiology in a coeliac/allergy context; central to macrophage polarization in granulomas (martins2019melkerssonrosenthalsyndromewith pages 1-2).
  - IL12B/IL23A (IL-12/IL-23): pathway implicated by clinical remission with ustekinumab (anti–IL-12/23) in granulomatous cheilitis (taxonera2020recurrentgranulomatouscheilitis pages 2-3).
- Chemical entities (examples; CHEBI terms where applicable):
  - Triamcinolone acetonide (intralesional steroid); methylprednisolone (systemic corticosteroid) (wu2024acaseof pages 3-5, legert2024oralmanifestationsofa pages 5-7).
  - Ustekinumab (monoclonal antibody against IL-12/23) (taxonera2020recurrentgranulomatouscheilitis pages 2-3).
  - Infliximab (anti–TNF-α; variable efficacy) (taxonera2020recurrentgranulomatouscheilitis pages 2-3).
- Cell types (CL terms):
  - Macrophages/epithelioid histiocytes; multinucleated giant cells (muller2019noninfectiousgranulomatouslesions pages 4-6, wu2024acaseof pages 3-5).
  - T lymphocytes (Th1/Th17 involvement inferred from IL-12/23 targeting) (taxonera2020recurrentgranulomatouscheilitis pages 2-3).
  - Dendritic cells/antigen-presenting cells in mucosa (inferred from granulomatous inflammation) (muller2019noninfectiousgranulomatouslesions pages 4-6).
  - Lymphatic endothelial cells (D2-40/podoplanin, Prox1, LYVE-1) (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).
- Anatomical locations (UBERON terms): lip and oral mucosa (primary), perivascular/perineural regions, lymphatic vessels, facial nerve (cranial nerve VII), tongue (lingua plicata) (wu2024acaseof pages 3-5, legert2024oralmanifestationsofa pages 5-7, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).

Biological Processes (GO annotation candidates)
- TNF signaling pathway; interferon-gamma–mediated signaling; IL-12– and IL-23–mediated signaling.
- T cell activation and Th1/Th17 differentiation; macrophage activation and granuloma formation.
- Lymphangiogenesis and lymphatic vessel development; leukocyte migration and perivascular infiltration.
- Antigen processing/presentation in mucosal tissues; wound healing and fibrosis pathways in chronic inflammation.
Supporting evidence: granulomatous histopathology (muller2019noninfectiousgranulomatouslesions pages 4-6, wu2024acaseof pages 3-5), lymphatic endothelial marker expression in intralymphatic histiocytosis (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4), and pathway-directed therapeutic response (taxonera2020recurrentgranulomatouscheilitis pages 2-3).

Cellular Components (where processes occur)
- Extracellular space and stromal lamina propria of lip/oral mucosa (granuloma core) (wu2024acaseof pages 3-5, muller2019noninfectiousgranulomatouslesions pages 4-6).
- Lymphatic vessel lumina and endothelium (D2-40/podoplanin+ channels) (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).
- Perivascular niches (perivascular lymphocytic infiltrates) and perineural spaces (wu2024acaseof pages 3-5).

Disease Progression (sequence of events)
- Putative trigger (immune, allergic, or infectious exposure) initiates mucosal immune activation.
- Perivascular and perineural inflammation develops in lip/oral mucosa.
- Granuloma formation ensues with epithelioid histiocytes and giant cells in a Th1/Th17 cytokine milieu (TNF/IFN-γ; IL-12/23 pathways); edema may be sustained by lymphatic channel dilation/intralymphatic histiocytosis and lymphatic stasis (wu2024acaseof pages 3-5, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4, taxonera2020recurrentgranulomatouscheilitis pages 2-3).
- Clinical relapses of edema occur; some patients develop facial nerve palsy and lingua plicata over time; underdiagnosis and delayed recognition are common (legert2024oralmanifestationsofa pages 5-7).

Phenotypic Manifestations (HP terms)
- Recurrent orofacial edema (HP:0010742); labial swelling (HP:0010280) (legert2024oralmanifestationsofa pages 5-7, wu2024acaseof pages 3-5).
- Peripheral facial nerve palsy (HP:0010628) (legert2024oralmanifestationsofa pages 5-7).
- Fissured tongue (lingua plicata) (HP:0000187) (legert2024oralmanifestationsofa pages 5-7).
- Oral non-caseating granulomas (histologic phenotype) (wu2024acaseof pages 3-5, muller2019noninfectiousgranulomatouslesions pages 4-6).

Evidence items with direct quotes and sources (with URLs and publication dates)
- “Non-caseous granuloma is the gold standard for MRS,” lip biopsy with perivascular/perineural inflammation (BMC Oral Health, 2024; doi:10.1186/s12903-024-04723-7; URL: https://doi.org/10.1186/s12903-024-04723-7) (wu2024acaseof pages 3-5).
- “Histologically the granulomas in oral CD is indistinguishable from OFG.” (Head and Neck Pathology, 2019; doi:10.1007/s12105-018-00997-w; URL: https://doi.org/10.1007/s12105-018-00997-w) (muller2019noninfectiousgranulomatouslesions pages 4-6).
- Lymphatic endothelium immunoreactive for D2-40/podoplanin with intraluminal CD68+ histiocytes in ectatic vessels, consistent with intralymphatic histiocytosis (Am J Dermatopathol, 2015; doi:10.1097/dad.0000000000000257; URL: https://doi.org/10.1097/dad.0000000000000257) (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).
- Ustekinumab (anti–IL-12/23) induced remission of severe, recurrent granulomatous cheilitis after anti-TNF failure (Therapeutic Advances in Gastroenterology, 2020; doi:10.1177/1756284820934327; URL: https://doi.org/10.1177/1756284820934327) (taxonera2020recurrentgranulomatouscheilitis pages 2-3).
- “Interferon gamma could play a key role” in a case of classic triad with coeliac disease/allergies (BMJ Case Reports, 2019; doi:10.1136/bcr-2019-229857; URL: https://doi.org/10.1136/bcr-2019-229857) (martins2019melkerssonrosenthalsyndromewith pages 1-2).
- Clinical overview: “Only 8–25% of the cases show the complete triad,” underdiagnosis and diagnostic delay highlighted (2024; URL not provided in retrieved excerpt) (legert2024oralmanifestationsofa pages 5-7).

Embedded evidence summary
| Mechanistic theme | Key finding / quote | Molecular / cellular players | Tissue / anatomy | Evidence type | Source (authors / year) | DOI / URL | Context ID for citation |
|---|---|---|---|---|---|---|---|
| Non-caseating granulomas; perivascular & perineural inflammation | "Non-caseous granuloma is the gold standard for MRS" | Epithelioid histiocytes, multinucleated giant cells, lymphocytes, perineural inflammatory cells | Upper lip mucosa (lip biopsy); TMJ synovium reported in case | Histopathology; case report | Wu et al., 2024 | https://doi.org/10.1186/s12903-024-04723-7 | (wu2024acaseof pages 3-5) |
| Intralymphatic histiocytosis / lymphatic dilation with D2-40/podoplanin+ endothelium | "endothelium... immunoreactivity with D2-40/podoplanin" | CD68+ intraluminal histiocytes; D2-40/podoplanin+, Prox-1+, Lyve-1+ lymphatic endothelium | Dermal / intralymphatic vessels (reports in orofacial sites and skin) | Immunohistochemistry; histopathology; case series | Demirkesen et al., 2015 | https://doi.org/10.1097/dad.0000000000000257 | (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4) |
| Overlap with Crohn disease; indistinguishable granuloma morphology | "Histologically the granulomas in oral CD is indistinguishable from OFG." | Epithelioid histiocytes, giant cells, plasma cells, lymphocytes; mast cells, eosinophils | Oral mucosa (lips, buccal mucosa, vestibule) | Review; clinicopathologic correlation | Müller, 2019 | https://doi.org/10.1007/s12105-018-00997-w | (muller2019noninfectiousgranulomatouslesions pages 4-6) |
| Th1 / Th17 cytokine axis implicated; IL-12/23 blockade response (therapy evidence) | "ustekinumab... to induce the remission of severe and recurrent granulomatous cheilitis" | IL-12 / IL-23 pathway (Th1/Th17), TNF-α implicated in granuloma formation | Lip granulomas / systemic Crohn-associated OFG | Therapy response; case report + literature review (ustekinumab) | Taxonera et al., 2020; (cautious additional support Nagy 2025) | https://doi.org/10.1177/1756284820934327 ; https://doi.org/10.7759/cureus.80879 | (taxonera2020recurrentgranulomatouscheilitis pages 2-3, nagy2025cheilitisgranulomatosaa pages 10-11) |
| Autoimmune / infectious associations (coeliac, allergy, HSV); IFN-γ hypothesis | "interferon gamma could play a key role." | IFN-γ, TNF-α; links to autoimmune markers and prior infections (HSV, other microbes) | Systemic associations; oral/lip manifestations | Case report with literature discussion (associative evidence) | Martins et al., 2019 | https://doi.org/10.1136/bcr-2019-229857 | (martins2019melkerssonrosenthalsyndromewith pages 1-2) |
| Clinical triad, underdiagnosis, and diagnostic features overview | "Only 8-25% of the cases show the complete triad" | (clinical diagnostic features rather than molecular players) | Orofacial swelling (lips/cheeks), facial nerve (CN VII), lingua plicata (tongue) | Review / clinical overview | Legert et al., 2024 (overview) | n/a | (legert2024oralmanifestationsofa pages 5-7) |


*Table: Compact, source-linked evidence table summarizing pathological mechanisms, key findings (quotes), cellular players, tissues, evidence types, and citations (context IDs) for Melkersson–Rosenthal syndrome and orofacial granulomatosis.*

Gene/protein annotations with ontology terms (examples)
- TNF (HGNC): TNF signaling; positive regulation of granuloma formation; macrophage activation (taxonera2020recurrentgranulomatouscheilitis pages 2-3, muller2019noninfectiousgranulomatouslesions pages 4-6).
- IFNG (HGNC): interferon-gamma–mediated signaling; classical macrophage activation (martins2019melkerssonrosenthalsyndromewith pages 1-2).
- IL12B; IL23A (HGNC): IL-12/23 signaling; Th1/Th17 differentiation; targeted by ustekinumab (taxonera2020recurrentgranulomatouscheilitis pages 2-3).

Cell type involvement (CL terms)
- Macrophage/epithelioid histiocyte; multinucleated giant cell; T lymphocyte (Th1/Th17); lymphatic endothelial cell (D2-40/podoplanin+) (muller2019noninfectiousgranulomatouslesions pages 4-6, wu2024acaseof pages 3-5, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4, taxonera2020recurrentgranulomatouscheilitis pages 2-3).

Anatomical locations (UBERON terms)
- Lip/oral mucosa, buccal mucosa, perivascular/perineural compartments, lymphatic vessels, facial nerve, tongue (wu2024acaseof pages 3-5, legert2024oralmanifestationsofa pages 5-7, demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).

Chemical entities (CHEBI terms, by common names)
- Triamcinolone acetonide; methylprednisolone; infliximab; ustekinumab (wu2024acaseof pages 3-5, taxonera2020recurrentgranulomatouscheilitis pages 2-3, legert2024oralmanifestationsofa pages 5-7).

Limitations and open questions
- No single causative gene is established for MRS; genetic heterogeneity is suspected, but specific associations (e.g., HLA, NOD2) require rigorous confirmation and were not identified in the present evidence set (legert2024oralmanifestationsofa pages 5-7, muller2019noninfectiousgranulomatouslesions pages 4-6).
- Infectious triggers remain proposed (e.g., herpesvirus in individual histories), but consistent pathogenetic agents have not been verified; mechanistic links to SARS-CoV-2 were not supported by the included sources (martins2019melkerssonrosenthalsyndromewith pages 1-2, legert2024oralmanifestationsofa pages 5-7).

Citations (with URLs and dates when available)
- Wu A, et al. BMC Oral Health. 2024. “A case of Melkersson-Rosenthal syndrome with temporomandibular joint osteoarthritis...” doi:10.1186/s12903-024-04723-7. URL: https://doi.org/10.1186/s12903-024-04723-7 (wu2024acaseof pages 3-5).
- Legert KG, et al. Oral manifestations of systemic disorders—part 1. 2024. Clinical overview of MRS (URL not provided in excerpt) (legert2024oralmanifestationsofa pages 5-7).
- Taxonera C, et al. Ther Adv Gastroenterol. 2020. “Recurrent granulomatous cheilitis... successfully treated with ustekinumab.” doi:10.1177/1756284820934327. URL: https://doi.org/10.1177/1756284820934327 (taxonera2020recurrentgranulomatouscheilitis pages 2-3).
- Müller S. Head Neck Pathol. 2019. “Non-infectious Granulomatous Lesions of the Orofacial Region.” doi:10.1007/s12105-018-00997-w. URL: https://doi.org/10.1007/s12105-018-00997-w (muller2019noninfectiousgranulomatouslesions pages 4-6).
- Demirkesen C, et al. Am J Dermatopathol. 2015. “Intravascular/Intralymphatic Histiocytosis: A Report of 3 Cases.” doi:10.1097/dad.0000000000000257. URL: https://doi.org/10.1097/dad.0000000000000257 (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4).
- Martins JA, et al. BMJ Case Rep. 2019. “Melkersson-Rosenthal syndrome with coeliac and allergic diseases.” doi:10.1136/bcr-2019-229857. URL: https://doi.org/10.1136/bcr-2019-229857 (martins2019melkerssonrosenthalsyndromewith pages 1-2).

All major mechanistic claims above are supported by the cited sources, with emphasis on 2024 clinical and review evidence and pathway-directed therapeutic observations from recent literature.


References

1. (legert2024oralmanifestationsofa pages 5-7): KG Legert, AML Pedersen, and G Gale. Oral manifestations of systemic disorders–part 1. Unknown journal, 2024.

2. (wu2024acaseof pages 3-5): Antong Wu, Ying Zhang, Wei Cao, Xinhong Wang, Zhiqiang Song, Richard T. Jaspers, Lu Chen, Janak L. Pathak, and Qingbin Zhang. A case of melkersson-rosenthal syndrome with temporomandibular joint osteoarthritis: multidisciplinary treatment and autoimmune etiological hypothesis. BMC Oral Health, Aug 2024. URL: https://doi.org/10.1186/s12903-024-04723-7, doi:10.1186/s12903-024-04723-7. This article has 3 citations and is from a peer-reviewed journal.

3. (muller2019noninfectiousgranulomatouslesions pages 4-6): Susan Müller. Non-infectious granulomatous lesions of the orofacial region. Head and Neck Pathology, 13:449-456, Jan 2019. URL: https://doi.org/10.1007/s12105-018-00997-w, doi:10.1007/s12105-018-00997-w. This article has 32 citations and is from a peer-reviewed journal.

4. (demirkesen2015intravascularintralymphatichistiocytosisa pages 2-4): Cuyan Demirkesen, Tugce Kran, Cem Leblebici, Deniz Yücelten, Ayşe Esra Koku Aksu, and Cem Mat. Intravascular/intralymphatic histiocytosis: a report of 3 cases. The American Journal of dermatopathology, 37 10:783-9, Oct 2015. URL: https://doi.org/10.1097/dad.0000000000000257, doi:10.1097/dad.0000000000000257. This article has 28 citations.

5. (taxonera2020recurrentgranulomatouscheilitis pages 2-3): Carlos Taxonera, Cristina Alba, Michel Colmenares, David Olivares, and Enrique Rey. Recurrent granulomatous cheilitis associated with crohn’s disease successfully treated with ustekinumab: case report and literature review. Therapeutic Advances in Gastroenterology, Jan 2020. URL: https://doi.org/10.1177/1756284820934327, doi:10.1177/1756284820934327. This article has 14 citations and is from a peer-reviewed journal.

6. (martins2019melkerssonrosenthalsyndromewith pages 1-2): Joana Albuquerque Martins, António Azenha, Rui Almeida, and João Páscoa Pinheiro. Melkersson-rosenthal syndrome with coeliac and allergic diseases. BMJ Case Reports, 12:e229857, Aug 2019. URL: https://doi.org/10.1136/bcr-2019-229857, doi:10.1136/bcr-2019-229857. This article has 7 citations and is from a peer-reviewed journal.

7. (nagy2025cheilitisgranulomatosaa pages 10-11): Stephanie Nagy, Marika Fraser, and Marc M. Kesselman. Cheilitis granulomatosa: a case report of a sarcoid mimic. Cureus, Mar 2025. URL: https://doi.org/10.7759/cureus.80879, doi:10.7759/cureus.80879. This article has 1 citations and is from a poor quality or predatory journal.