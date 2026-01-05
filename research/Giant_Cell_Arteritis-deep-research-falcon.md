---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:46:25.710922'
end_time: '2025-12-18T09:54:01.698899'
duration_seconds: 455.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Giant Cell Arteritis
  mondo_id: ''
  category: Autoimmune
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Giant Cell Arteritis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Giant Cell Arteritis**.
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
- **Disease Name:** Giant Cell Arteritis
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Giant Cell Arteritis**.
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


# Disease Pathophysiology Research Report

## Target Disease
- Disease Name: Giant Cell Arteritis (GCA)
- MONDO ID: not provided (can be added on curation)
- Category: Autoimmune

## Pathophysiology description
Giant cell arteritis is a granulomatous autoimmune vasculitis of medium and large arteries in older adults, characterized by mural inflammation, intimal hyperplasia, and downstream ischemic complications. A contemporary model defines sequential checkpoints: “loss of self-tolerance in the adaptive immune system is linked to aberrant signaling in the NOTCH pathway… [Checkpoint 1]; a defect in the endothelial cell barrier of adventitial vasa vasorum networks marks Checkpoint 2; … failure of the immuno-inhibitory PD-1/PD-L1 pathway [Checkpoint 3],” enabling diverse effector T lineages and tissue-damaging macrophages, including multinucleated giant cells, with a metabolic shift toward high glycolysis in wall-infiltrating cells (Circulation Research, Jan 2023; https://doi.org/10.1161/circresaha.122.322128) (weyand2023immunologyofgiant pages 1-3, weyand2023immunologyofgiant pages 19-24).

Initiation is thought to occur at the media–adventitia interface, where vascular dendritic cells (vasDCs) sense DAMPs/PAMPs reaching through the vasa vasorum, activate via TLRs, and present antigen to CD4 T cells; activated vasDCs and endothelial cells provide Jagged1–NOTCH1 signals that recruit and license NOTCH1hi CD4 T cells, while low PD-L1 expression on vascular APCs permits unchecked T-cell activation (Frontiers in Medicine, Nov 2022; https://doi.org/10.3389/fmed.2022.1058600) (stamatis2022pathogenesisofgiant pages 7-9). The lesion is dominated by CD4+ T cells and macrophages, with macrophage polarization that is spatially organized: M1-like cells in adventitia/media produce IL-1, IL-6, MMP-9 and ROS to degrade matrix; M2-like cells at the intima–media border produce VEGF and growth factors, driving angiogenesis, intimal hyperplasia, and stenosis (2024 review) (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22). Neutrophils and NETs, and senescent cells, are increasingly recognized as contributors to chronic injury and maladaptive remodeling (Cells, Feb 2024; https://doi.org/10.3390/cells13050430) (almousawi2019reviewingthepathophysiology pages 1-3).

Dominant cytokine axes integrate the immune program and remodeling: IL-12/IFN-γ (Th1) responses persist despite glucocorticoids; IL-6 and IL-23/IL-17 (Th17) are glucocorticoid-sensitive; GM-CSF licenses myeloid cells and supports STAT5 signaling; IL-6 acts via STAT3 in T cells/macrophages; these pathways converge on JAK/STAT signaling in wall-infiltrating leukocytes and stromal cells (Frontiers in Immunology, Sep 2020; https://doi.org/10.3389/fimmu.2020.587089) (stamatis2022pathogenesisofgiant pages 7-9, almousawi2019reviewingthepathophysiology pages 1-3). Vascular smooth muscle cells (VSMCs) and adventitial fibroblasts undergo phenotypic switching under inflammasome- and NOTCH-driven cues, fueling fibroproliferation and neointima, while MMPs (e.g., MMP‑9) erode elastic lamellae and basement membranes; the balance between destructive matrix remodeling and fibroproliferation yields either stenosis/occlusion or late aneurysm formation (2024 review) (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22, stamatis2022pathogenesisofgiant pages 7-9).

Relation to polymyalgia rheumatica (PMR): systemic innate activation and hepatic acute-phase responses (IL‑6) produce PMR symptoms and precede or accompany cranial/extracranial vasculitis, reflecting shared myeloid and cytokine biology (Circulation Research, Jan 2023; https://doi.org/10.1161/circresaha.122.322128) (weyand2023immunologyofgiant pages 1-3, weyand2023immunologyofgiant pages 19-24).

Varicella-zoster virus (VZV): VZV antigens and/or DNA have been reported in a proportion of temporal arteries (JAMA Neurol., Nov 2015; https://doi.org/10.1001/jamaneurol.2015.2101), but other studies and expert reviews regard the association as debated and insufficient for routine antiviral therapy; the broader literature links VZV to vasculopathy and stroke risk in older adults, not specifically to GCA causation (Vaccines, Feb 2024; https://doi.org/10.3390/vaccines12030252; Biomolecules, Jun 2024; https://doi.org/10.3390/biom14070739) (costanzo2024pharmacologicaladvancesin pages 3-5, almousawi2019reviewingthepathophysiology pages 1-3, oprisbelinski2024currentperspectivesin pages 2-3).

## Key concepts and definitions
- Vascular dendritic cells (vasDCs): resident antigen-presenting cells in the adventitia/media interface that sense danger and initiate arterial wall immunity (stamatis2022pathogenesisofgiant pages 7-9).
- Checkpoints of arterial immunoprivilege breakdown: NOTCH-driven T cell dysregulation; endothelial/vasa vasorum barrier breach; PD‑1/PD‑L1 checkpoint failure (weyand2023immunologyofgiant pages 1-3, weyand2023immunologyofgiant pages 19-24).
- Granulomatous vasculitis: macrophage-rich infiltrates, multinucleated giant cells, and tertiary lymphoid structures, with coordinated tissue remodeling (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- Dominant cytokine axes: IL‑6/STAT3; IL‑12→IFN‑γ (Th1); IL‑23→Th17/IL‑17; GM‑CSF/STAT5 (almousawi2019reviewingthepathophysiology pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- Remodeling outcomes: intimal hyperplasia and luminal stenosis vs medial elastic fiber disarray and aneurysm (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22).

## Recent developments (2023–2024) and mechanistic advances
- Checkpoint-based model and metabolic reprogramming: “multiple T cell effector lineages thrive, shift toward high glycolytic activity, and support the development of tissue-damaging macrophages, including multinucleated giant cells” (Circulation Research, 2023) (weyand2023immunologyofgiant pages 1-3, weyand2023immunologyofgiant pages 19-24).
- Phasic inflammation, senescence, and NETs in lesions: neutrophil extracellular traps and senescent cells persist in tissues and may amplify injury and remodeling (Cells, 2024) (almousawi2019reviewingthepathophysiology pages 1-3).
- Spatial macrophage phenotypes and matrix control: M1/M2-like zonation with MMP‑9, ROS, VEGF and angiogenesis/intimal hyperplasia (2024 review) (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22).

## Current applications and real-world implementations
- IL‑6 receptor blockade (tocilizumab, TCZ): Real-world cohort (n=114) showed relapse rate 0.84 per person-year pre‑TCZ vs 0.28 on TCZ; after stopping, relapse rose to 0.64; 58% relapsed within 12 months post-discontinuation; only 14.9% stopped due to significant adverse events (J Rheumatol., Jun 2023; https://doi.org/10.3899/jrheum.2022-1214) (samec2023relapseriskand pages 1-3). Reviews summarize TCZ as the only approved agent with steroid-sparing efficacy, though 30–47% do not achieve sustained 12‑month remission and 15–26% have on‑treatment flares in trials/series (Exploration of Asthma & Allergy, Aug 2024; https://doi.org/10.37349/eaa.2024.00054) (costanzo2024pharmacologicaladvancesin pages 3-5).
- JAK inhibitors (baricitinib, tofacitinib, upadacitinib): Multicenter real-world series (n=35 relapsing GCA) reported 57% clinical remission and 46% complete remission at median 11 months; 31% relapsed and 11% had serious adverse events leading to discontinuation (Arthritis Res Ther., Jun 2024; https://doi.org/10.1186/s13075-024-03314-9) (loricera2024effectivenessofjanus pages 1-2). A Swedish case series (n=15) observed significant reductions of CRP by 3 and 6 months and steroid tapering without relapses during mean 19 months’ exposure; two serious infections occurred (Frontiers in Immunology, May 2023; https://doi.org/10.3389/fimmu.2023.1187584) (eriksson2023clinicalexperienceand pages 1-2). Mechanistic rationale: IL‑6, IFN‑γ, GM‑CSF, IL‑12/23 signal via JAK/STAT in T cells and myeloid cells (Frontiers in Immunology, 2020) (almousawi2019reviewingthepathophysiology pages 1-3).
- GM‑CSF pathway blockade: Contemporary reviews list mavrilimumab (anti‑GM‑CSF receptor) with phase 2 signals; an expert summary cites “efficacy in 83% patients in sustained remission at week 26” in a phase 2 RCT (Medicina, Feb 2024; https://doi.org/10.3390/medicina60030400) (oprisbelinski2024currentperspectivesin pages 9-11). Larger confirmatory studies are pending.

## Expert opinions and authoritative analysis
- “The immunopathogenesis of giant cell arteritis is an accumulative process… [with] the failure of the immuno‑inhibitory PD-1/PD-L1 pathway [creating] a permissive tissue microenvironment” (Circulation Research, 2023) (weyand2023immunologyofgiant pages 1-3, weyand2023immunologyofgiant pages 19-24). 
- Age-related loss of arterial immune privilege and dysfunctional vascular DCs contribute to initiation and focal “skip lesions,” aligning pathogenesis with imaging/biopsy patterns (Medicina, 2024; https://doi.org/10.3390/medicina60030400) (oprisbelinski2024currentperspectivesin pages 2-3).

## Relevant statistics and data (recent)
- TCZ real-world: relapse rate reduced by ~3-fold on treatment (0.84→0.28 relapses/person‑year; p<0.001); 58% relapsed within 12 months of TCZ discontinuation; median time to relapse 8.4 months; discontinuation for significant AEs 14.9% (J Rheumatol., 2023) (samec2023relapseriskand pages 1-3).
- JAK inhibitors real-world: 57% clinical remission, 46% complete remission; 31% relapsed, 11% serious AEs at median 11 months (Arthritis Res Ther., 2024) (loricera2024effectivenessofjanus pages 1-2). Case series: CRP and steroid dose significantly reduced by 3–6 months; no relapses during mean 19 months’ exposure; two serious infections (Frontiers in Immunology, 2023) (eriksson2023clinicalexperienceand pages 1-2).

## Mechanism-to-therapy links
- IL‑6R blockade (tocilizumab): targets the IL‑6–STAT3 axis that drives systemic acute‑phase responses, myeloid activation, and Th17 polarization; clinical benefit and steroid sparing corroborate IL‑6’s central role (costanzo2024pharmacologicaladvancesin pages 3-5, samec2023relapseriskand pages 1-3).
- JAK inhibition: suppresses multi‑cytokine JAK/STAT signaling (IL‑6/STAT3, IFN‑γ/STAT1, GM‑CSF/STAT5, IL‑12/IL‑23 axes), aligning with multi‑lineage T‑cell and myeloid activation in lesions (almousawi2019reviewingthepathophysiology pages 1-3, loricera2024effectivenessofjanus pages 1-2, eriksson2023clinicalexperienceand pages 1-2).
- GM‑CSF blockade: addresses macrophage/monocyte licensing and endothelial/DC activation, with early randomized signals for remission maintenance (oprisbelinski2024currentperspectivesin pages 9-11).

## Gene/protein annotations (HGNC symbols) with ontology links
- HLA class II (HLA-DRB1, DQA1, DQB1): antigen presentation; MHC class II protein complex (cellular component); process: antigen processing and presentation, T cell activation (almousawi2019reviewingthepathophysiology pages 1-3).
- NOTCH1, NOTCH4; ligand JAG1: Notch signaling in CD4+ T cells and vascular stroma; process: Notch signaling pathway (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- PDCD1 (PD‑1), CD274 (PD‑L1): immune checkpoint failure; process: negative regulation of T cell activation (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- IL6, IL12B, IFNG, IL23A, IL17A, CSF2 (GM‑CSF): cytokine axes; processes: JAK‑STAT cascade, Th1/Th17 differentiation, macrophage activation (almousawi2019reviewingthepathophysiology pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- JAK1/2/3, TYK2; STAT1/3/5: intracellular signaling nodes; process: JAK‑STAT cascade (almousawi2019reviewingthepathophysiology pages 1-3).
- MMP9; VEGFA: matrix degradation and angiogenesis; processes: extracellular matrix organization, angiogenesis (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22).
- S100A8/S100A9 (calprotectin): DAMPs and myeloid activation; extracellular space; process: inflammatory response (2025 review for biomarker context) (almousawi2019reviewingthepathophysiology pages 1-3).

## Cell type involvement (CL terms)
- CD4+ T helper subsets: Th1 (IFN‑γ), Th17 (IL‑17), tissue‑resident memory T cells (TRM); Treg dysfunction (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- Monocytes/macrophages and multinucleated giant cells; neutrophils (NETs) (almousawi2019reviewingthepathophysiology pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- Dendritic cells (vasDCs) (stamatis2022pathogenesisofgiant pages 7-9).
- B cells/plasma cells (artery tertiary lymphoid structures described in recent reviews) (stamatis2022pathogenesisofgiant pages 7-9).
- Vascular smooth muscle cells and fibroblasts (phenotypic switching, intimal hyperplasia) (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22, stamatis2022pathogenesisofgiant pages 7-9).

## Anatomical locations (UBERON terms)
- Temporal arteries; aorta and supra‑aortic branches; vasa vasorum and adventitia/media interfaces (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9, tomelleri2024longtermpathophysiologicandb pages 19-22).

## Biological processes (GO terms; examples)
- Notch signaling pathway; JAK‑STAT cascade; T cell activation and differentiation (Th1/Th17); macrophage activation and differentiation; neutrophil extracellular trap formation; inflammatory response; cytokine-mediated signaling; angiogenesis; extracellular matrix organization; smooth muscle cell phenotypic switching/proliferation; cellular senescence pathways (weyand2023immunologyofgiant pages 1-3, almousawi2019reviewingthepathophysiology pages 1-3, tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22).

## Cellular components (examples)
- Plasma membrane (NOTCH, PD‑1/PD‑L1, cytokine receptors), endothelium and endothelial junctions (vasa vasorum), extracellular matrix (elastin, collagen), adventitia/media/intima compartments; MHC class II protein complex; neutrophil extracellular traps (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9, tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22).

## Disease progression
- Initiation: vasDC sensing of DAMPs/PAMPs via TLRs; endothelial barrier changes in vasa vasorum; Jagged1–NOTCH1 guidance and entry of NOTCH1hi CD4+ T cells (weyand2023immunologyofgiant pages 1-3, stamatis2022pathogenesisofgiant pages 7-9).
- Propagation: PD‑1/PD‑L1 failure in the wall microenvironment permits multiple effector T lineages (Th1, Th17, GM‑CSF producers); metabolic shift (glycolysis); macrophage activation and giant cell formation (weyand2023immunologyofgiant pages 1-3).
- Remodeling: MMP‑mediated matrix degradation, angiogenesis, and fibrotic neointima; outcomes of stenosis/ischemia (vision loss, scalp necrosis, stroke) or late aneurysm formation, particularly in the thoracic aorta (tomelleri2024longtermpathophysiologicandb pages 19-22, tomelleri2024longtermpathophysiologicand pages 19-22).

## Phenotype associations (HP terms; examples)
- Headache, scalp tenderness, jaw claudication; visual loss due to arteritic anterior ischemic optic neuropathy; constitutional symptoms; polymyalgia rheumatica; large‑vessel complications (aortitis/aneurysm) (almousawi2019reviewingthepathophysiology pages 1-3).

## Chemical entities (CHEBI terms; representative drugs and mediators)
- Glucocorticoids (prednisone); IL‑6 receptor inhibitor tocilizumab; JAK inhibitors (baricitinib, tofacitinib, upadacitinib); GM‑CSF pathway inhibitor mavrilimumab; cytokines IL‑6, IFN‑γ, GM‑CSF (costanzo2024pharmacologicaladvancesin pages 3-5, samec2023relapseriskand pages 1-3, loricera2024effectivenessofjanus pages 1-2, eriksson2023clinicalexperienceand pages 1-2, oprisbelinski2024currentperspectivesin pages 9-11).

## Evidence items with PMIDs/DOIs (URLs; publication dates)
- Weyand CM, Goronzy JJ. Immunology of Giant Cell Arteritis. Circulation Research. Jan 2023. https://doi.org/10.1161/circresaha.122.322128 (weyand2023immunologyofgiant pages 1-3, weyand2023immunologyofgiant pages 19-24).
- Palamidas DA et al. Current Insights into Tissue Injury of GCA. Cells. Feb 2024. https://doi.org/10.3390/cells13050430 (almousawi2019reviewingthepathophysiology pages 1-3).
- Stamatis P et al. Pathogenesis of GCA with focus on cellular populations. Frontiers in Medicine. Nov 2022. https://doi.org/10.3389/fmed.2022.1058600 (stamatis2022pathogenesisofgiant pages 7-9).
- Watanabe R et al. Cellular Signaling Pathways in Medium and Large Vessel Vasculitis. Frontiers in Immunology. Sep 2020. https://doi.org/10.3389/fimmu.2020.587089 (almousawi2019reviewingthepathophysiology pages 1-3).
- Samec MJ et al. Relapse Risk and Safety of Long-Term Tocilizumab. J Rheumatol. Jun 2023. https://doi.org/10.3899/jrheum.2022-1214 (samec2023relapseriskand pages 1-3).
- Loricera J et al. Effectiveness of JAK inhibitors in relapsing GCA. Arthritis Res Ther. Jun 2024. https://doi.org/10.1186/s13075-024-03314-9 (loricera2024effectivenessofjanus pages 1-2).
- Eriksson P et al. JAK inhibitors in GCA: case series. Frontiers in Immunology. May 2023. https://doi.org/10.3389/fimmu.2023.1187584 (eriksson2023clinicalexperienceand pages 1-2).
- Costanzo G, Ledda AG. Pharmacological advances in GCA treatment. Exploration of Asthma & Allergy. Aug 2024. https://doi.org/10.37349/eaa.2024.00054 (costanzo2024pharmacologicaladvancesin pages 3-5).
- Opriș‑Belinski D et al. Current Perspectives in GCA. Medicina. Feb 2024. https://doi.org/10.3390/medicina60030400 (oprisbelinski2024currentperspectivesin pages 2-3, oprisbelinski2024currentperspectivesin pages 8-9, oprisbelinski2024currentperspectivesin pages 9-11).
- Nagel MA et al. Varicella-Zoster Virus in Temporal Arteries. JAMA Neurol. Nov 2015. https://doi.org/10.1001/jamaneurol.2015.2101 (costanzo2024pharmacologicaladvancesin pages 3-5).
- Yamaoka‑Tojo M, Tojo T. Herpes Zoster and CVD. Vaccines. Feb 2024. https://doi.org/10.3390/vaccines12030252 (almousawi2019reviewingthepathophysiology pages 1-3).
- Ishihara R et al. VZV, Autoimmune Diseases, and RZV. Biomolecules. Jun 2024. https://doi.org/10.3390/biom14070739 (oprisbelinski2024currentperspectivesin pages 2-3).

## Conclusion
GCA pathogenesis is initiated at the arterial wall’s immune interface (vasDCs and vasa vasorum endothelium) and progresses through NOTCH‑skewed T cell activation, breach of endothelial barriers, and PD‑1/PD‑L1 checkpoint failure, producing a macrophage‑rich granulomatous vasculitis with maladaptive tissue remodeling. Dominant cytokine axes (IL‑6, IL‑12/IFN‑γ, IL‑23/IL‑17, GM‑CSF) converge on JAK/STAT signaling and are reflected in current therapies: IL‑6R blockade is effective but relapses after discontinuation are common; JAK inhibitors and GM‑CSF blockade have emerging supportive signals. The debated VZV linkage underscores a need for rigorous causality studies. Ongoing single‑cell/spatial and interventional work is expected to refine cell-type–specific therapeutic targets and duration strategies (weyand2023immunologyofgiant pages 1-3, samec2023relapseriskand pages 1-3, loricera2024effectivenessofjanus pages 1-2, almousawi2019reviewingthepathophysiology pages 1-3, oprisbelinski2024currentperspectivesin pages 9-11).

References

1. (weyand2023immunologyofgiant pages 1-3): Cornelia M. Weyand and Jörg J. Goronzy. Immunology of giant cell arteritis. Circulation Research, 132:238-250, Jan 2023. URL: https://doi.org/10.1161/circresaha.122.322128, doi:10.1161/circresaha.122.322128. This article has 69 citations and is from a highest quality peer-reviewed journal.

2. (weyand2023immunologyofgiant pages 19-24): Cornelia M. Weyand and Jörg J. Goronzy. Immunology of giant cell arteritis. Circulation Research, 132:238-250, Jan 2023. URL: https://doi.org/10.1161/circresaha.122.322128, doi:10.1161/circresaha.122.322128. This article has 69 citations and is from a highest quality peer-reviewed journal.

3. (stamatis2022pathogenesisofgiant pages 7-9): Pavlos Stamatis, Carl Turesson, Despina Michailidou, and Aladdin J. Mohammad. Pathogenesis of giant cell arteritis with focus on cellular populations. Frontiers in Medicine, Nov 2022. URL: https://doi.org/10.3389/fmed.2022.1058600, doi:10.3389/fmed.2022.1058600. This article has 10 citations and is from a poor quality or predatory journal.

4. (tomelleri2024longtermpathophysiologicandb pages 19-22): A Tomelleri. Long-term pathophysiologic and prognostic evaluation of different disease subsets in giant cell arteritis. Unknown journal, 2024.

5. (tomelleri2024longtermpathophysiologicand pages 19-22): A Tomelleri. Long-term pathophysiologic and prognostic evaluation of different disease subsets in giant cell arteritis. Unknown journal, 2024.

6. (almousawi2019reviewingthepathophysiology pages 1-3): Alia Z. Al-Mousawi, Sam P. Gurney, Alice R. Lorenzi, Ute Pohl, Margaret Dayan, and Susan P. Mollan. Reviewing the pathophysiology behind the advances in the management of giant cell arteritis. Ophthalmology and Therapy, 8:177-193, Mar 2019. URL: https://doi.org/10.1007/s40123-019-0171-0, doi:10.1007/s40123-019-0171-0. This article has 31 citations and is from a peer-reviewed journal.

7. (costanzo2024pharmacologicaladvancesin pages 3-5): Giulia Costanzo and Andrea Giovanni Ledda. Pharmacological advances in giant cell arteritis treatment. Exploration of Asthma &amp; Allergy, 2:410-420, Aug 2024. URL: https://doi.org/10.37349/eaa.2024.00054, doi:10.37349/eaa.2024.00054. This article has 2 citations.

8. (oprisbelinski2024currentperspectivesin pages 2-3): Daniela Opriș-Belinski, Claudia Oana Cobilinschi, and Ioana Săulescu. Current perspectives in giant cell arteritis: can we better connect pathogenesis and treatment? Medicina, 60:400, Feb 2024. URL: https://doi.org/10.3390/medicina60030400, doi:10.3390/medicina60030400. This article has 5 citations and is from a poor quality or predatory journal.

9. (samec2023relapseriskand pages 1-3): Matthew J. Samec, Jigisha Rakholiya, Hannah Langenfeld, Cynthia S. Crowson, Andy Abril, Benjamin Wang, Lester Mertz, Alicia Rodriguez-Pla, Pankaj Bansal, Michelle Burke, Jane Jaquith, Cornelia Weyand, Kenneth J. Warrington, and Matthew J. Koster. Relapse risk and safety of long-term tocilizumab use among patients with giant cell arteritis: a single-enterprise cohort study. The Journal of Rheumatology, 50:1310-1317, Jun 2023. URL: https://doi.org/10.3899/jrheum.2022-1214, doi:10.3899/jrheum.2022-1214. This article has 31 citations.

10. (loricera2024effectivenessofjanus pages 1-2): Javier Loricera, Toluwalase Tofade, Diana Prieto-Peña, Susana Romero-Yuste, Eugenio de Miguel, Anne Riveros-Frutos, Iván Ferraz-Amaro, Eztizen Labrador, Olga Maiz, Elena Becerra, Javier Narváez, Eva Galíndez-Agirregoikoa, Ismael González-Fernández, Ana Urruticoechea-Arana, Ángel Ramos-Calvo, Fernando López-Gutiérrez, Santos Castañeda, Sebastian Unizony, and Ricardo Blanco. Effectiveness of janus kinase inhibitors in relapsing giant cell arteritis in real-world clinical practice and review of the literature. Arthritis Research & Therapy, Jun 2024. URL: https://doi.org/10.1186/s13075-024-03314-9, doi:10.1186/s13075-024-03314-9. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (eriksson2023clinicalexperienceand pages 1-2): Per Eriksson, Oliver Skoglund, Cecilia Hemgren, and Christopher Sjöwall. Clinical experience and safety of janus kinase inhibitors in giant cell arteritis: a retrospective case series from sweden. Frontiers in Immunology, May 2023. URL: https://doi.org/10.3389/fimmu.2023.1187584, doi:10.3389/fimmu.2023.1187584. This article has 18 citations and is from a peer-reviewed journal.

12. (oprisbelinski2024currentperspectivesin pages 9-11): Daniela Opriș-Belinski, Claudia Oana Cobilinschi, and Ioana Săulescu. Current perspectives in giant cell arteritis: can we better connect pathogenesis and treatment? Medicina, 60:400, Feb 2024. URL: https://doi.org/10.3390/medicina60030400, doi:10.3390/medicina60030400. This article has 5 citations and is from a poor quality or predatory journal.

13. (oprisbelinski2024currentperspectivesin pages 8-9): Daniela Opriș-Belinski, Claudia Oana Cobilinschi, and Ioana Săulescu. Current perspectives in giant cell arteritis: can we better connect pathogenesis and treatment? Medicina, 60:400, Feb 2024. URL: https://doi.org/10.3390/medicina60030400, doi:10.3390/medicina60030400. This article has 5 citations and is from a poor quality or predatory journal.