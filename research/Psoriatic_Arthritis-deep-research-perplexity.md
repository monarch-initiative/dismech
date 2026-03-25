---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-02-01T09:14:12.927990'
end_time: '2026-02-01T09:16:48.037291'
duration_seconds: 155.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Psoriatic Arthritis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 56
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Psoriatic Arthritis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Psoriatic Arthritis**.
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

# Comprehensive Pathophysiology of Psoriatic Arthritis: Molecular, Cellular, and Clinical Mechanisms

Psoriatic arthritis (PsA) represents a complex inflammatory musculoskeletal disease characterized by the disruption of both innate and adaptive immune homeostasis, resulting in chronic joint inflammation, cartilage and bone destruction, and new bone formation. Recent advances in molecular profiling and mechanistic studies have revealed that PsA develops through the interplay of genetic susceptibility, environmental triggers, and dysregulated immune activation targeting multiple anatomical sites including synovial joints, the enthesis (site of tendon and ligament insertion), and skin. The disease emerges in approximately thirty percent of patients with psoriasis vulgaris, typically between five to twelve years following initial skin manifestations, though concurrent or sequential skin and joint disease presentations occur frequently. This comprehensive analysis synthesizes current understanding of the pathophysiological mechanisms driving PsA across multiple biological scales, from molecular signaling pathways to tissue-level inflammation and systemic immune dysregulation.

## Genetic Architecture and Susceptibility Loci Underlying Psoriatic Arthritis

The genetic foundation of psoriatic arthritis demonstrates substantially higher heritability than its cutaneous-only counterpart, with sibling recurrence risks (λS) estimated between twenty-seven to forty-seven, compared to the four to nineteen observed for psoriasis vulgaris alone[7][9]. This striking difference in genetic contribution indicates that specific genetic variants confer arthritis-specific risk beyond those associated with skin disease alone. Genome-wide association studies encompassing over thirty-six thousand cases and four hundred fifty-eight thousand controls have identified one hundred nine distinct psoriasis susceptibility loci, with approximately forty-five newly identified variants, though the distinction between PsA-specific and psoriasis-shared genetic factors remains an active area of investigation[12].

The major histocompatibility complex region demonstrates the strongest association signals with PsA, particularly at chromosome 6p21 approximately thirty-five kilobases upstream of the HLA-C gene[7][10]. The HLA-C*06:02 allele exhibits strong association with psoriasis vulgaris but shows weaker association with PsA, suggesting divergent genetic architecture between cutaneous and articular manifestations[9]. Conversely, HLA-B*27 displays stronger association with PsA, particularly in patients with axial skeletal involvement, though at substantially lower frequency than observed in ankylosing spondylitis[20]. These HLA class I associations underscore the critical role of CD8+ T cell recognition and response in PsA pathogenesis, as these molecules present peptide antigens to CD8+ T cells.

Beyond the HLA complex, multiple non-MHC loci contribute to PsA susceptibility through diverse immunological mechanisms. The IL23R locus demonstrates genome-wide significant association with PsA, encoding the receptor for interleukin-23, a critical driver of T helper 17 (Th17) cell differentiation and inflammatory cytokine production[7][12]. The IL12B region harbors multiple independent susceptibility variants, reflecting the importance of IL-23/IL-17 axis dysregulation in PsA pathogenesis[9]. Additional susceptibility loci include TNIP1, TNFAIP3, NFκBIA, and TYK2, which encode molecules involved in NF-κB signaling, TNF-α pathway modulation, and JAK/STAT signaling, respectively, highlighting the convergence of multiple inflammatory pathways in PsA[7][12].

The REL locus, encoding the c-Rel member of the NF-κB family, demonstrates PsA-specific association stronger than observed for psoriasis vulgaris alone[7][10]. This finding implicates NF-κB-dependent transcription particularly in joint inflammation and suggests that innate immune pathway dysregulation through altered transcription factor activity constitutes a core PsA mechanism. The identification of multiple independent PsA susceptibility variants within regions such as IL12B, NOS2, and IFIH1 indicates complex allelic architecture with distinct functional consequences for each variant, requiring comprehensive functional characterization to fully understand their contributions to disease[9].

## The IL-23/IL-17 Axis: Central Orchestrator of Inflammatory Pathology

The interleukin-23 and interleukin-17 signaling axis has emerged as the dominant cytokine pathway driving PsA pathogenesis, building upon extensive evidence from genetic association studies, animal models, and clinical treatment responses[3][4]. This pathway initiates at the level of antigen-presenting cells, particularly dendritic cells resident in skin, enthesis, and synovial tissues, where stimulation triggers the release of multiple pro-inflammatory cytokines that work in concert to promote Th17 cell differentiation and expansion[3][4].

Upon encountering inflammatory stimuli, dendritic cells release interleukin-23, interleukin-12, interleukin-1β, and tumor necrosis factor-alpha, which collectively promote the differentiation of naive CD4+ T cells into T helper 17 cells[3][4]. Interleukin-23 binding to its heterodimeric receptor composed of IL-23R and IL-12Rβ1 chains activates the JAK2 and Tyk2 protein tyrosine kinases, which phosphorylate signal transducer and activator of transcription 3 (STAT3) at tyrosine 705[3][4]. Phosphorylated STAT3 translocates to the nucleus where it induces expression of RORγ (RAR-related orphan receptor gamma), the master transcription factor controlling Th17 differentiation and IL-17 production[3][4]. This initial differentiation also requires transforming growth factor-beta and interleukin-6 signaling, which together with IL-23 support sustained IL-17 production[3].

The Th17 subset of CD4+ T cells serves as a primary source of interleukin-17A, the prototypical member of the IL-17 cytokine family[3][4]. Studies utilizing flow cytometry and intracellular cytokine staining consistently demonstrate increased frequencies of Th17 cells in the peripheral blood, synovial fluid, and synovial tissue of PsA patients compared with healthy controls and osteoarthritis patients[5][3]. This expanded Th17 population releases an array of pro-inflammatory cytokines including IL-17A, IL-17B, IL-17F, IL-21, IL-22, and IL-26, which amplify downstream inflammatory responses[3][4].

Interleukin-17 exerts pleiotropic effects on multiple effector cell types within the joint microenvironment[3][4]. IL-17A stimulation of synovial fibroblasts induces their proliferation and upregulation of matrix metalloproteinases (particularly MMP-1, MMP-3, and MMP-13) that degrade cartilage extracellular matrix components[3]. Synovial fibroblasts activated by IL-17 further produce chemokines including CXCL1, CXCL2, CXCL5, and CXCL8, which promote recruitment of neutrophils and additional myeloid cells to inflamed joints[3]. The actions of IL-17 extend to skeletal cells, where IL-17A increases expression of receptor activator of nuclear factor kappa-B ligand (RANKL) on both fibroblasts and Th17 cells themselves, leading to enhanced osteoclast precursor differentiation and bone-resorbing osteoclast maturation[3][4]. Paradoxically, IL-17 also appears to promote osteoblast differentiation through mechanisms involving IL-22 signaling, contributing to the distinctive pattern of bone erosion coupled with new bone formation characteristic of PsA[3][4].

The IL-23/IL-17 axis effects extend beyond CD4+ T cells, as gamma-delta T cells (γδT cells) represent an additional IL-17 source in PsA. These innate-like lymphocytes express the IL-23 receptor and rapidly produce IL-17 upon IL-23 stimulation, providing an early source of this cytokine during inflammation[3][5]. Gamma-delta T cells express chemokine receptors CCR6 and CCR2, which direct them to skin and synovial sites in response to CCL6 and CCL2 gradients[5]. Natural killer T cells and mucosal-associated invariant T (MAIT) cells also contribute to IL-17 production in PsA synovium and psoriatic skin[5]. This multiplicity of IL-17-producing cell types ensures sustained inflammatory responses even when one population is incompletely controlled by therapy.

Interleukin-22, another product of Th17 and related T cell subsets, plays a distinct role in PsA pathogenesis through effects on keratinocyte hyperproliferation and bone homeostasis[3][4]. IL-22 signaling through its heterodimeric receptor on keratinocytes downregulates differentiation genes while promoting proliferation and expression of antimicrobial peptides[3]. Within the joint, IL-22 promotes osteoblast differentiation through STAT3-mediated signaling and upregulation of bone morphogenetic protein pathways, leading to the paradoxical new bone formation observed at entheseal sites and within synovial tissue[3][4]. This simultaneous bone erosion and formation distinguishes PsA from rheumatoid arthritis, where erosions typically predominate without significant periosteal or enthesal new bone formation.

The IL-23/IL-17 axis operates within a complex inflammatory milieu, with considerable cross-talk and synergistic interactions with other pro-inflammatory pathways. Tumor necrosis factor-alpha, discussed in detail below, synergizes with IL-17A to amplify inflammatory responses through combined effects on endothelial cells, fibroblasts, and immune cell recruitment[3][4]. The combination of TNF-α and IL-17A induces greater expression of adhesion molecules (ICAM-1, VCAM-1, P-selectin, E-selectin) on endothelial cells than either cytokine alone, facilitating enhanced leukocyte extravasation into inflamed tissues[3].

## TNF-α Pathway: Amplification and Tissue Destruction

Tumor necrosis factor-alpha, a prototypical pro-inflammatory cytokine, reaches elevated concentrations in PsA serum, synovial fluid, and synovial tissue, where it drives multiple aspects of inflammatory joint disease[5]. TNF-α expression predominantly derives from activated macrophages, T cells, and other myeloid cells within the inflamed synovium, though keratinocytes, dendritic cells, and fibroblasts also contribute to systemic and local TNF-α production[5]. The biological effects of TNF-α occur through binding to two distinct receptors, TNF receptor 1 (TNFR1, p55 subunit) and TNF receptor 2 (TNFR2, p75 subunit), which activate different downstream signaling cascades and produce divergent cellular outcomes[5].

TNFR1 activation triggers both pro-inflammatory and pro-apoptotic signaling pathways, leading to NF-κB and mitogen-activated protein kinase (MAPK) pathway activation with consequent inflammatory cytokine production and induction of cell death receptors[5]. TNF-α stimulation of synovial fibroblasts increases their expression of IL-6, IL-8, and granulocyte-macrophage colony-stimulating factor (GM-CSF), amplifying the pro-inflammatory milieu[5]. TNF-α also stimulates synovial fibroblasts to produce additional matrix metalloproteinases and tissue inhibitors of metalloproteinases, with the net effect being enhanced cartilage degradation when MMP production exceeds TIMP production[3][5].

The role of TNF-α extends critically to bone remodeling in PsA, where it exerts complex effects on osteoclast and osteoblast biology[5]. TNF-α stimulates RANKL expression in bone marrow stromal cells and activates p38 mitogen-activated protein kinase signaling, leading to increased c-Fms expression and enhanced responsiveness of osteoclast precursors to M-CSF (macrophage colony-stimulating factor)[5]. TNF-α additionally activates TRAF6, a critical adaptor molecule in RANK signaling essential for osteoclastogenesis[5]. The combination of TNF-α-induced RANKL upregulation and enhanced osteoclast precursor sensitivity creates a permissive environment for accelerated bone loss[5].

Studies of PsA peripheral blood mononuclear cells have demonstrated elevated frequencies of circulating osteoclast precursors in unstimulated cultures, with particularly high numbers in patients with radiographically evident bone erosions[28]. The elevated TNF-α produced by PsA peripheral blood mononuclear cells can independently induce these precursor cells to differentiate into mature osteoclasts, an effect blocked by anti-TNF-α monoclonal antibodies[28]. These findings establish a mechanistic link between elevated TNF-α and the aggressive bone erosions characteristic of PsA.

TNF-α simultaneously inhibits the Wnt signaling pathway critical for bone formation through upregulation of Dickkopf-1 (DKK-1) and sclerostin, factors that antagonize the Wnt receptor complex[3][4]. This TNF-α-mediated suppression of bone formation through Wnt pathway inhibition contrasts with the IL-17/IL-22-mediated promotion of bone formation, creating the distinctive radiographic pattern of PsA with both erosive and proliferative bone lesions[3][4].

The effectiveness of TNF-α inhibitor therapy in controlling both skin and joint manifestations of PsA validates TNF-α as a central therapeutic target, though approximately thirty to forty percent of patients demonstrate inadequate response or loss of response to TNF-α inhibitor monotherapy[6]. This variable responsiveness has prompted investigation into combination approaches and alternative cytokine targets, including IL-17 and IL-23 inhibitors that may be more effective in TNF-α-inadequate responders.

## JAK/STAT Signaling: Integration of Cytokine Pathways

The Janus kinase-signal transducer and activator of transcription (JAK/STAT) pathway integrates signals from multiple cytokines including IL-6, IL-17, IL-23, interferons, and type I interferons, serving as a crucial convergence point for inflammatory signaling in PsA[1][3]. Recent research has unveiled previously unappreciated roles of JAK/STAT signaling in driving synovial cell proliferation and pannus formation beyond its established role in T cell differentiation[1].

In the context of PsA, T cells infiltrating joint tissue release inflammatory cytokines that activate JAK/STAT signaling in synovial lining cells[1]. The JAK enzyme family members JAK1, JAK2, and Tyk2 become phosphorylated upon receptor engagement, which in turn phosphorylate STAT proteins on critical tyrosine residues, promoting their dimerization and nuclear translocation[1][3]. Research conducted at UC Davis Health demonstrated that when this pathway becomes activated in synovial cells, it drives their abnormal proliferation and contributes to pannus formation, the invasive fibrovascular tissue that erodes cartilage and bone[1].

Specifically, IL-9 and IL-22 cytokines have been shown to activate JAK/STAT signaling in synovial cells, promoting their proliferation[1][3]. Studies using JAK inhibitors revealed that blocking JAK kinase activity reduces both synovial cell proliferation and the subsequent pannus formation and joint damage[1]. This finding has important therapeutic implications, as JAK inhibitors available for clinical use (including tofacitinib, baricitinib, and upadacitinib) may exert benefits through both immune cell modulation and direct effects on synovial cell biology[1].

The STAT3 protein, downstream of JAK activation, has emerged as a critical transcription factor in PsA pathogenesis[37]. STAT3 phosphorylation at tyrosine 705 is required for homodimer formation and optimal transcriptional activity[37]. In addition to its role in Th17 differentiation, STAT3 drives expression of pro-inflammatory cytokines including IL-6, IL-8, IL-23, and IL-17 in multiple cell types[37]. Studies of transgenic mice with constitutively active STAT3 in CD4+ T cells demonstrated development of spontaneous psoriasis-like arthritis, validating the pathogenic role of STAT3 hyperactivation[37]. Furthermore, individuals with higher STAT3 transcriptional activity in CD4+ T cells displayed increased susceptibility to joint disease, indicating that genetic variation affecting STAT3 function may contribute to PsA risk[37].

## Innate Immune Cell Populations: Macrophages, Dendritic Cells, and Neutrophils

The innate immune response in PsA involves multiple cell types that serve as primary drivers of inflammation before, during, and in coordination with adaptive immune responses. Macrophages accumulate within PsA synovium where they produce abundant pro-inflammatory cytokines and growth factors[30]. Immunohistochemical studies reveal marked macrophage infiltration particularly in the synovial sublining layer, where CD68+ macrophages correlate with disease activity[30]. Macrophages in the PsA joint exhibit polarization toward a pro-inflammatory M1 phenotype that secretes TNF-α, IL-1β, IL-6, IL-12, and IL-23, supporting ongoing Th17 responses[30]. Additionally, activated macrophages produce matrix metalloproteinases including MMP-9, which directly degrade cartilage components and facilitate immune cell infiltration[30].

Dendritic cells serve as critical antigen-presenting cells that bridge innate and adaptive immunity in PsA[2][15]. A specialized subset of monocyte-derived dendritic cells (Mo-DCs) has been identified in PsA synovial fluid, characterized by expression of CD14, CD209 (DC-SIGN), and classical dendritic cell markers HLA-DR and CD11c[18]. These CD209+/CD14+ dendritic cells are significantly enriched in the inflamed joint compared with peripheral blood[18]. Within the synovium, dendritic cells present antigen to naive T cells and provide critical co-stimulatory signals through expression of CD40, CD80, and CD86 molecules[18]. Dendritic cells within PsA tissue release high concentrations of IL-23, IL-12, and TNF-α, which together drive Th17 cell differentiation[3].

Recent single-cell transcriptomic analysis of synovial fluid from PsA patients revealed profound alterations in the myeloid compartment, with elevated expression of proinflammatory genes and an interferon-induced signature[2][15]. Type 2 conventional dendritic cells and monocytes were identified as particularly activated, expressing high levels of molecules involved in antigen presentation and immune activation[2][15]. Notably, in patients whose PsA proved refractory to standard disease-modifying antirheumatic drugs, elevated expression of genes associated with the immunoproteasome and major histocompatibility complex class I molecules was identified as a major distinguishing feature[2][15]. This finding suggests that enhanced antigen presentation capacity through both classical and immunoproteasome-mediated pathways may contribute to treatment resistance, potentially through amplification of CD8+ T cell responses.

Neutrophils accumulate in PsA synovium at substantially higher frequencies than observed in rheumatoid arthritis[30]. Polymorphonuclear cells infiltrate the synovial tissue where they produce pro-inflammatory cytokines and form neutrophil extracellular traps (NETs), web-like structures released when neutrophils undergo a specialized form of cell death[27][30]. These NETs trap microbial pathogens and autoantigens while releasing proteolytic enzymes and antimicrobial peptides that can damage host tissues[27][30]. IL-17 enhances neutrophil recruitment through upregulation of endothelial adhesion molecules and production of chemokines, particularly CXCL8 (IL-8)[27][30]. Chronic neutrophil activation and NET formation have been proposed to contribute to PsA pathogenesis through sustained tissue damage and perpetuation of the inflammatory cascade[27][30].

Mast cells represent a previously underappreciated cellular component particularly enriched in PsA synovium compared with rheumatoid arthritis[30]. These cells are characterized by prominent IL-17A production and constitute a major cellular source of IL-17 within PsA synovial tissue[30]. Mast cells release multiple inflammatory mediators including prostaglandins, leukotrienes, growth factors (platelet-derived growth factor, fibroblast growth factor, vascular endothelial growth factor), and pro-inflammatory cytokines upon activation[3][30]. The IL-17A stored within mast cells may be rapidly mobilized during inflammation, serving a sentinel function in providing early IL-17A signaling during tissue inflammatory responses[30].

## Synovial Fibroblasts: From Structural Cells to Invasive Effector Cells

Fibroblast-like synoviocytes (FLS) line the synovial membrane and normally maintain joint homeostasis by producing lubricating hyaluronic acid, structural proteins, and growth factors[30]. In PsA, these cells undergo phenotypic transformation and acquire invasive properties, contributing to pannus formation and joint destruction. Synovial fibroblasts in PsA proliferate abnormally, demonstrating reduced apoptosis and increased expression of anti-apoptotic proteins including Bcl-2[44]. IL-17 signaling substantially enhances fibroblast survival through STAT3-mediated upregulation of Bcl-2 and suppression of pro-apoptotic molecules[44].

The activated FLS phenotype in PsA involves marked upregulation of adhesion molecules, growth factors, and proteolytic enzymes. Synovial fibroblasts produce abundant matrix metalloproteinases including MMP-1 (collagenase), MMP-3 (stromelysin), and MMP-13 (collagenase-3), which directly degrade collagen and proteoglycan components of cartilage[26]. TNF-α and IL-1β serve as potent activators of FLS MMP production, with IL-1β particularly effective at stimulating MMP-3 synthesis[26]. The expression of these collagenases within pannus tissue at the cartilage-pannus junction correlates with radiographic evidence of cartilage erosion[26].

Beyond matrix degradation, synovial fibroblasts produce chemokines critical for immune cell recruitment including CCL2, CCL5, CXCL12, CXCL13, and CXCL16, which promote T cell and B cell infiltration[43]. Fibroblasts further express CCL20, the ligand for CCR6, which preferentially recruits Th17 cells, creating a self-amplifying inflammatory loop[43]. Recent studies employing single-cell transcriptomics have identified distinct fibroblast subsets with specific inflammatory signatures in PsA synovium[4]. A WNT5A+/IL24+ fibroblast subset has been identified as particularly inflammatory, located in proximity to activated keratinocytes and expressing high levels of inflammatory mediators[17].

Importantly, synovial fibroblasts undergo dynamic phenotypic changes during response to anti-inflammatory therapy. Studies demonstrate that effective IL-17A and TNF-α blockade leads to phenotypic switching from a destructive IL-6+/MMP3+/THY1+ subset toward a CD200+/DKK3+ phenotype with resolution-promoting properties[4]. This fibroblast plasticity suggests that successful therapeutics may work partially through reprogramming of synovial fibroblasts toward tissue-protective rather than tissue-destructive states.

## CD8+ T Cells and Tissue-Resident Memory T Cells: Linking Skin and Joint Inflammation

While CD4+ T cells and Th17 differentiation have classically dominated discussions of PsA pathogenesis, accumulating evidence indicates that CD8+ T cells play critical roles in both cutaneous and articular manifestations of the disease. Human leukocyte antigen class I presentation of peptides to CD8+ T cells has been genetically linked to PsA development, with HLA-C*06:02 and HLA-B*27 alleles showing strong associations with disease[13][20]. Recent advances in single-cell transcriptomics have revealed enrichment of CD8+ tissue-resident memory T (Trm) cells in both psoriatic skin and PsA synovium[50][53].

Studies comparing CD8+ T cell phenotypes between skin and joint compartments demonstrate that tissue-resident memory CD8+ cells (characterized by expression of CD69 and lack of CD45RA) exhibit a stronger IL-17 signature in skin compared with joint tissue[50][53]. Importantly, these studies identified CD8+ T cell clones that are shared between skin and joint compartments, with a median of thirteen percent of skin CD8+ T cell receptors also present in joint tissue, and eight percent of joint CD8+ T cells found in skin[50][53]. These skin-joint shared clones typically maintain a similar CD8+ Trm phenotype at both sites, characterized by increased expression of cytotoxic genes and genes associated with tissue residency[50][53]. This clonal sharing provides direct evidence for trafficking of specific T cells between skin and joint compartments and suggests that targeting of shared antigens by these clones may drive inflammation across both tissue sites.

Patients with mild-to-moderate psoriasis demonstrate altered CD8+ T cell functionality, with reduced frequencies of circulating CD8+ memory T cells and decreased release of cytotoxic mediators (Granzyme B, IFN-γ) upon T cell receptor stimulation[8]. These alterations suggest that psoriatic disease involves dysregulation of CD8+ T cell activation and effector functions. The reduction of circulating CD8+ memory cells may reflect their migration into inflamed skin and joints, consistent with the elevated frequencies observed within these tissues[8].

## Bone Remodeling: The Distinctive Pattern of Erosion with New Bone Formation

A pathognomonic feature of PsA distinguishing it from rheumatoid arthritis is the simultaneous occurrence of bone erosion and new bone formation, often within the same joint or even the same digit[20][29]. This uncoupling of osteoblast and osteoclast homeostasis creates the characteristic "pencil-in-cup" deformity and periosteal reactions visible on radiographs. Understanding the cellular and molecular basis of this paradoxical bone remodeling requires examination of both bone-resorbing osteoclasts and bone-forming osteoblasts.

### Osteoclastogenesis and Bone Erosion

Osteoclasts, derived from hematopoietic precursor cells of monocyte lineage, serve as the only cell type capable of resorbing the mineralized bone matrix[25][28]. The differentiation of osteoclast precursor cells into mature multinucleated osteoclasts depends critically on two signals: macrophage colony-stimulating factor (M-CSF) and receptor activator of nuclear factor kappa-B ligand (RANKL)[25][28]. M-CSF binds to the c-Fms receptor on osteoclast precursors, promoting their survival and proliferation, while RANKL binding to RANK triggers the differentiation cascade[25][28].

In PsA, multiple pro-inflammatory cytokines upregulate RANKL expression, including TNF-α, IL-1β, IL-6, and IL-17[25][28]. T cells, particularly Th17 cells, express membrane-bound RANKL and can directly activate osteoclast differentiation[25][28]. The elevated TNF-α present in PsA synovial fluid and tissue amplifies RANKL expression in both fibroblasts and T cells while simultaneously enhancing osteoclast precursor sensitivity to these signals[25][28]. Studies quantifying circulating osteoclast precursor frequencies in PsA patients have revealed dramatically elevated numbers in peripheral blood, with particularly high frequencies in patients with radiographically evident bone erosions[28]. These circulating precursors spontaneously differentiate into osteoclasts without exogenous RANKL or M-CSF stimulation, indicating pre-activation by systemic inflammatory mediators[28]. Intriguingly, peripheral blood mononuclear cells from PsA patients can induce osteoclastogenesis in healthy control cells through production of TNF-α and other soluble mediators[28].

The RANK-RANKL interaction triggers multiple intracellular signaling cascades within osteoclast precursors, particularly activation of the TNF receptor-associated factor 6 (TRAF6) adaptor protein[25][28]. TRAF6 activation drives NF-κB and mitogen-activated protein kinase signaling, leading to calcium-calcineurin signaling and activation of the critical transcription factor nuclear factor of activated T cells, cytoplasmic 1 (NFATc1)[25]. NFATc1 drives expression of genes encoding the osteoclast-specific proteolytic enzymes cathepsin K and tartrate-resistant acid phosphatase as well as the proton pump necessary for the acidic microenvironment required for bone resorption[25].

Osteoprotegerin (OPG), a soluble decoy receptor for RANKL, acts as a physiological brake on osteoclastogenesis[25][28]. Studies of PsA patient synovial fluid demonstrate that treatment with recombinant OPG substantially reduces osteoclast formation from patient mononuclear cells, establishing RANKL as critical for the enhanced osteoclastogenesis observed in PsA[28]. Therapeutic strategies targeting the RANKL pathway through OPG-Fc molecules represent an alternative approach to TNF-α and IL-17/IL-23 inhibition for controlling bone loss in PsA.

### Osteoblastogenesis and New Bone Formation

The formation of new bone at entheseal sites and within synovial tissue constitutes a peculiar aspect of PsA pathogenesis not prominently observed in rheumatoid arthritis[29]. Bone morphogenetic proteins (BMPs) and members of the Wnt signaling family play central roles in driving osteoblast differentiation and bone formation[16][29]. The Wnt/β-catenin pathway promotes osteoblast formation by stimulating expression of Runx2, the master transcription factor controlling osteoblast gene expression[16][29]. However, in the inflammatory milieu of PsA, TNF-α-mediated upregulation of DKK-1 and sclerostin antagonizes Wnt signaling and suppresses osteoblastogenesis[16][29], creating local areas of impaired bone formation adjacent to erosion sites.

Conversely, IL-22, produced by Th17 and other T cell subsets, potently promotes osteoblast differentiation through STAT3-dependent signaling[3][4]. IL-22 stimulation of synovial fibroblasts and osteoblast precursors leads to increased expression of bone morphogenetic proteins and upregulation of genes driving mineralized bone matrix synthesis[3][4]. The IL-17A-induced production of IL-22 by specific T cell subsets may explain the localized bone formation observed within PsA synovium and entheseal tissues, where these cells concentrate[3][4]. Additionally, IL-22 suppresses osteoclastogenesis through mechanisms involving GM-CSF production, creating a local environment where bone formation predominates over bone loss[3][4].

The enigmatic simultaneous occurrence of bone erosion and formation in PsA likely reflects spatial segregation of these processes, with IL-17 and TNF-α driving osteoclastogenesis at the pannus-bone interface while IL-22 and bone morphogenetic proteins promote osteoblastogenesis in adjacent synovial tissue[3][4]. Recent work examining the osteoid production by osteoblasts and mineralization processes suggests that IL-17 may actually stimulate osteoblasts to produce RANKL, providing a direct link between the Th17 response and both bone formation and resorption through different mechanisms[16].

## The Enthesis: A Special Site of Vulnerability and Inflammation

The enthesis, defined as the anatomical junction where tendons, ligaments, and joint capsules insert into bone, represents a unique anatomical site that bears the brunt of PsA pathology[4][56]. Enthesitis—inflammation at these insertion sites—characterizes the spondyloarthritis family of diseases, to which PsA belongs, and often precedes peripheral joint involvement. The enthesis experiences substantial mechanical stress during normal movements, generating forces that exceed those experienced by synovial joints[4][56]. This biomechanical loading creates microtrauma at entheseal sites, triggering activation of mesenchymal stem cells and local immune responses[4][56].

Recent investigations indicate that patients with PsA possess an altered threshold to mechanical stress, responding to physiological levels of force with pathological inflammation[56]. This differential response likely results from genetic predisposition combined with dysregulated innate immune pathways including increased Toll-like receptor sensitivity[31]. Mechanical loading of mesenchymal stem cells and fibroblasts activates production of CXCL1 and CCL2 chemokines, recruiting monocytes that can differentiate into bone-resorbing osteoclasts[4]. The enthesis becomes infiltrated with innate immune cells including macrophages, mast cells, and neutrophils, which release IL-17 and TNF-α[3][4][56]. IL-17 acts as a major inflammatory mediator at the enthesis, promoting neutrophil infiltration through upregulation of adhesion molecules and production of chemokines[3][56].

The chronic inflammation at entheseal sites in PsA is accompanied by new bone formation, creating characteristic entheseophytes (bony entheseal spurs) and syndesmophytes (ossification of ligamentous insertions) visible on radiographs[56]. IL-22 plays a particularly important role in entheseal new bone formation, acting on mesenchymal stem cells to promote osteoblast differentiation and bone matrix synthesis[3][56]. The presence of IL-17-producing mast cells and T cells at entheseal sites, combined with local IL-23 production, creates an environment conducive to both inflammatory damage and paradoxical new bone formation.

## Metabolic Reprogramming and Glycolytic Activation

Recent research has revealed that inflammatory cells in PsA, including keratinocytes and immune cells, undergo metabolic reprogramming characterized by elevated aerobic glycolysis, a process distinct from oxidative phosphorylation despite adequate oxygen availability[48]. This metabolic shift, termed the Warburg effect when observed in cancer cells, provides rapid ATP synthesis supporting the energy demands of proliferating cells and enables synthesis of biosynthetic precursors[48]. In psoriatic lesions and PsA joints, enhanced glycolytic flux has been documented in keratinocytes and dendritic cells, driven by upregulation of glycolytic enzyme expression including hexokinase 2 (HK2), phosphoglycerate mutase 1 (PGAM1), and enolase[48].

The metabolic shift toward glycolysis is regulated by multiple signaling pathways activated in PsA. The Akt/mTOR/HIF-1α (hypoxia-inducible factor-1 alpha) pathway controls glycolytic enzyme expression in activated immune cells and keratinocytes[48]. HIF-1α, stabilized under hypoxic conditions characteristic of inflamed tissues, transcriptionally activates genes encoding glycolytic enzymes and simultaneously suppresses oxidative phosphorylation[48]. In PsA synovium, the combination of increased cellularity, enhanced vascular permeability, and intermittent vascular occlusion creates localized hypoxia that stabilizes HIF-1α and promotes glycolytic metabolism[45].

The functional consequences of this metabolic reprogramming extend beyond merely providing ATP. Glycolytic intermediates feed into biosynthetic pathways including those producing nucleotides, amino acids, and lipids required for rapid cell proliferation and inflammatory mediator synthesis[48]. Activated dendritic cells in PsA require enhanced glycolysis to support the synthesis of IL-23, TNF-α, and other pro-inflammatory cytokines, and pharmacological inhibition of glycolytic enzymes reduces pro-inflammatory cytokine production[45][48]. Furthermore, the metabolic state of T cells influences their differentiation, with enhanced glycolysis promoting Th17 rather than Treg differentiation through effects on mTOR signaling[48].

## Epigenetic Modifications and Chromatin Remodeling

Beyond genetic variations affecting protein sequences, heritable changes in DNA methylation and histone modifications drive dysregulated gene expression in PsA. DNA methylation at CpG dinucleotides, catalyzed by DNA methyltransferases, typically correlates with transcriptional repression of affected genes[38][41]. Genome-wide methylation studies comparing psoriatic and normal skin have identified numerous differentially methylated regions affecting genes involved in immune regulation, keratinocyte differentiation, and inflammatory pathways[38][41].

Histone modifications, including acetylation and methylation of specific lysine and arginine residues on histone proteins, profoundly influence chromatin accessibility and transcriptional activity[38][41]. Histone acetylation generally promotes transcription by opening chromatin structure and facilitating transcription factor binding, while certain histone methylation marks (such as H3K9 and H3K27 trimethylation) typically repress transcription[38][41]. In psoriasis and PsA, dysregulation of histone acetyltransferase and histone deacetylase activity leads to altered expression of IL-23, IL-17, and other inflammatory genes[38][41].

TNF-α signaling can directly influence histone modifications through effects on chromatin-modifying enzymes. Research has demonstrated that TNF-α phosphorylation of neural Wiskott-Aldrich syndrome protein (N-WASP) leads to degradation of histone methyltransferases G9a and GLP, reducing repressive H3K9 methylation marks and increasing IL-23 expression[38][41]. This mechanistic link between TNF-α signaling and IL-23 regulation through histone modifications exemplifies the integration of inflammatory signaling with epigenetic control of gene expression.

MicroRNAs, non-coding RNA molecules of approximately twenty-two nucleotides, regulate gene expression post-transcriptionally through base-pairing with mRNA targets, leading to translational repression or mRNA degradation[42]. Dysregulated microRNA expression has been documented in PsA, with several microRNAs showing altered abundance in CD4+ T cells and other immune cells. The miR-146a microRNA, highly expressed in T cells from inflammatory arthritis patients, demonstrates upregulation in response to TNF-α stimulation, suggesting a feedback regulation of TNF-α signaling[42]. Genetic variants in microRNA genes, including the miR-146a rs2910164 polymorphism and miR-155 rs767649 variant, have been associated with PsA susceptibility in case-control studies, though the functional consequences remain incompletely characterized[42].

## Angiogenesis and Vascular Dysregulation

The inflamed synovium and psoriatic skin lesions in PsA demonstrate dysregulated angiogenesis characterized by formation of immature, morphologically abnormal blood vessels[33][36]. Histomorphological examination reveals elongated, bushy, torturous vessels in PsA joints, contrasting with the straighter, more orderly vasculature of rheumatoid arthritis[29][33]. These morphological abnormalities reflect an imbalance between angiogenic and anti-angiogenic signals, promoting new vessel formation while compromising vessel maturation and function.

Vascular endothelial growth factor (VEGF), the prototypical angiogenic factor, becomes elevated in PsA serum and synovial fluid, where it stimulates endothelial cell proliferation, migration, and permeability[33][36]. VEGF levels correlate with disease activity measures including the Disease Activity Score, C-reactive protein elevation, and swollen joint counts[36]. Hypoxia-inducible factor-1α (HIF-1α) drives VEGF transcription in response to local tissue hypoxia characteristic of inflamed joints[36]. The inflammatory milieu itself promotes angiogenesis through effects of TNF-α, IL-17, and interleukins on endothelial cells and supporting cells[33][36].

Angiopoietins regulate vascular maturation through effects on the Tie-2 receptor expressed on endothelial cells[33]. Ang-1 promotes vessel maturation and stabilization, while Ang-2 acts antagonistically in the absence of VEGF or agonistically when VEGF is present, promoting vascular sprout formation[33]. The elevated Ang-2 levels observed in PsA synovium, especially following anti-TNF-α therapy, suggest VEGF-dependent promotion of angiogenesis[33]. The concomitant expression of multiple angiogenic molecules creates a permissive environment for pathological vessel formation.

Angiogenesis contributes to PsA pathogenesis through multiple mechanisms beyond merely increasing nutrient delivery. Expanded vasculature increases vascular permeability through effects of VEGF and other permeability factors, facilitating immune cell extravasation into inflamed tissues[33]. Newly formed vessels express enhanced levels of adhesion molecules promoting leukocyte recruitment[33]. Additionally, angiogenesis driven by hypoxia-induced HIF-1α expression creates local metabolic conditions favoring glycolytic metabolism and pro-inflammatory immune responses[45][48].

## Complement Activation and Alternative Pathway Dysregulation

The complement system, comprising over thirty plasma and membrane-bound proteins, serves as an essential component of innate immunity and also modulates adaptive immune responses[32]. Activation through three distinct pathways—classical, alternative, and lectin—converges on formation of the membrane attack complex and generation of anaphylatoxins C3a and C5a that promote inflammation and immune cell recruitment[32]. While complement activation is well-established in rheumatoid arthritis, less information exists regarding complement in PsA[32].

Evidence suggests involvement of the complement system in PsA pathogenesis, with some studies demonstrating complement activation in PsA synovial fluid[32]. The contribution of different complement pathways to PsA requires further investigation, though genetic associations with complement-related genes and the therapeutic effectiveness of TNF-α inhibitors (which may partially work through reducing complement activation) suggest a pathogenic role[32]. The alternative pathway of complement, initiated by direct activation of C3 by pathogen-associated molecular patterns or damage-associated molecular patterns, may be particularly relevant in PsA given the proposed role of innate immune dysregulation in this disease[32][35].

## Toll-Like Receptors: Pattern Recognition and Innate Immune Activation

Toll-like receptors (TLRs) represent a family of pattern-recognition receptors that detect microbial pathogens and endogenous damage signals, triggering innate immune responses[31][34]. TLR2, which recognizes peptidoglycan from gram-positive bacteria, demonstrates upregulated expression on peripheral blood monocytes of PsA patients compared with healthy controls[31]. This upregulation of TLR2 suggests enhanced responsiveness to gram-positive bacterial components, potentially through streptococcal antigens, which have been proposed as environmental triggers for PsA[31].

TLR ligation on innate immune cells leads to MyD88-dependent signaling activating NF-κB and mitogen-activated protein kinases, culminating in pro-inflammatory cytokine production[31][34]. The upregulation of TLR2 on PsA monocytes may enhance their inflammatory responses to bacterial components, providing a mechanism through which environmental microbial triggers could amplify disease activity[31]. Additionally, TLR4, which recognizes lipopolysaccharide from gram-negative bacteria, shows association with PsA in some studies, suggesting dysregulated responsiveness to multiple bacterial species[34].

## Microbiota-Immune Dysregulation Interface

Emerging evidence indicates that dysbiosis—abnormal composition of the microbiota—contributes to PsA pathogenesis through breakdown of immune tolerance to commensal bacteria[24]. The skin microbiota in psoriasis differs substantially from healthy skin, with alterations in bacterial community composition potentially enabling expansion of pro-inflammatory strains[24]. Similarly, the gut microbiota in PsA patients shows evidence of dysbiosis, with reduced diversity and altered representation of specific bacterial taxa[24]. The gut barrier dysfunction frequently accompanying PsA allows bacterial lipopolysaccharides and other microbial antigens to cross into the lamina propria, triggering innate immune activation[24].

The proposed role of molecular mimicry, wherein cross-reactive T cells respond to both streptococcal antigens and host self-antigens, has been investigated as a mechanism linking streptococcal infection to PsA[24]. However, recent studies emphasize that while CD8+ peripheral blood T cells may respond to homologous peptides shared between streptococcal and self-proteins, the critical CD4+ T cells necessary to initiate psoriasis may not be similarly engaged[24]. This suggests that abnormal innate immune responses to bacterial dysbiosis rather than classical molecular mimicry may better explain the microbial connection to PsA pathogenesis[24].

## Clinical Phenotypes and Their Mechanistic Basis

Psoriatic arthritis presents with striking heterogeneity in clinical phenotypes, reflecting variable involvement of different joint groups and anatomical sites[20][22][23]. This heterogeneity complicates diagnosis, predicts disease progression, and influences treatment response, underscoring the need for mechanistic understanding of phenotypic variation[20][22][23].

### Oligoarticular and Polyarticular Presentations

The asymmetric oligoarticular pattern, affecting four or fewer joints, represents the most common initial presentation, occurring in at least sixty percent of PsA cases at disease onset[20]. However, the majority of oligoarticular patients progress to polyarticular disease over time[20]. Notably, the phenotypic transition from oligoarthritis to polyarthritis correlates with expansion and proliferation of pro-inflammatory T cell populations, particularly elevation of Th17 cells and CD8+ T cells expressing IL-17[20].

Polyarticular arthritis, typically symmetric and involving five or more joints, resembles rheumatoid arthritis superficially but differs pathologically through greater frequency of distal interphalangeal joint involvement and higher propensity for bone proliferation[20]. Mechanistically, polyarticular disease associates with heightened systemic levels of pro-inflammatory cytokines including IL-17, TNF-α, and IL-6 compared with oligoarticular presentations[29]. The expanded inflammatory cell populations in polyarticular PsA may reflect both increased Th17 differentiation and altered regulatory T cell function, though studies directly comparing T cell frequencies between oligoarticular and polyarticular phenotypes remain limited.

### Enthesitis and Dactylitis: Distinctive PsA Features

Enthesitis, recognized as a hallmark of PsA and other spondyloarthropathies, may precede joint involvement and independently predicts disease progression[4][56]. The susceptibility of the enthesis to inflammation likely reflects its unique anatomical properties—the concentrated mechanical stresses it experiences during normal movement trigger localized innate immune activation[4][56]. The presence of PsA-specific genetic associations with IL-23/IL-17 pathway components combined with mechanical stress-induced mesenchymal cell activation creates the milieu promoting entheseal inflammation[4][56].

Dactylitis—swelling of entire fingers or toes creating a "sausage digit" appearance—occurs in up to forty percent of PsA patients and associates with severe synovial inflammation extending across tendon sheaths and synovial membranes[3][4]. Histopathological examination of dactylitic digits reveals tenosynovitis (inflammation of the tendon sheath), microenthesitis at tendon insertion sites, and extensive synovial infiltration[3][4]. The pathogenesis involves T cell infiltration into affected tissues with production of IL-17 and TNF-α, promoting neutrophil recruitment and activation of fibroblasts producing matrix-degrading enzymes[3][4].

### Axial Involvement and Spondylitis

Axial involvement in PsA manifests as sacroiliitis and spondylitis, occurring in approximately forty-three percent of patients, often coexisting with peripheral joint disease[20][23]. PsA-associated axial disease differs from ankylosing spondylitis through less frequent HLA-B*27 positivity (twenty percent vs. eighty-ninety percent), higher female prevalence, older age at onset, and asymmetric radiographic findings[20]. The syndesmophytes bridging vertebral bodies in PsA are characteristically bulky, asymmetric, and discontinuous, skipping vertebral levels, in contrast to the marginal, symmetric syndesmophytes of ankylosing spondylitis[20].

The mechanisms underlying axial involvement likely parallel those of peripheral PsA, with IL-23/IL-17 axis activation at entheseal and ligamentous insertions promoting bone formation coupled with inflammatory destruction[3][4]. The IL-22 cytokine may play a particularly important role in axial new bone formation, given its potent effects on osteoblast differentiation[3][4].

## Therapeutic Implications and Future Directions

The mechanistic understanding of PsA pathogenesis has directly informed development of targeted therapeutics demonstrating clinical efficacy[1][3][4][6]. TNF-α inhibitors, including monoclonal antibodies (infliximab, adalimumab) and soluble receptor fusion proteins (etanercept), remain first-line therapies for moderate-to-severe PsA, with approximately fifty to seventy percent of patients achieving low disease activity with these agents[6]. However, approximately thirty to forty percent demonstrate inadequate initial response or loss of response over time.

IL-17 inhibitors, including monoclonal antibodies against IL-17A (secukinumab, ixekizumab), demonstrate superiority to TNF-α inhibitors in some efficacy measures, particularly for skin disease, though polyarticular joint response rates remain comparable[6]. IL-23 inhibitors (guselkumab, tildrakizumab, risankizumab) represent emerging therapeutic options targeting the upstream cytokine driving Th17 differentiation, with early clinical trials demonstrating efficacy in both skin and joint manifestations[6].

JAK inhibitors (tofacitinib, baricitinib, upadacitinib), which block multiple cytokine signaling pathways simultaneously, offer an oral therapeutic option with efficacy approaching or potentially exceeding conventional biologic therapies for some patients[1][6]. The breadth of cytokine pathways affected by JAK inhibition—including IL-6, IL-23, IL-22, and interferons—may explain their effectiveness in treatment-resistant populations.

The discovery of immunoproteasome pathway involvement in treatment-resistant PsA suggests that selective immunoproteasome inhibitors may benefit patients failing conventional therapies[2][15]. Functional validation studies confirm that immunoproteasome inhibition reduces myeloid-driven inflammation in model systems, supporting clinical investigation of this approach[2][15].

Emerging recognition of the CD8+ T cell contribution to PsA pathogenesis raises the possibility that therapeutics targeting CD8+ T cell responses or promoting CD8+ regulatory T cell generation could prove beneficial. Additionally, the identification of distinct fibroblast subsets with either inflammatory or resolution-promoting phenotypes suggests that therapeutic approaches encouraging fibroblast phenotype switching might prevent permanent joint damage.

The heterogeneity of PsA pathophysiology and variable treatment responses have prompted investigation into predictive biomarkers enabling personalized therapeutic selection. Studies demonstrate that baseline T cell phenotype composition—specifically the relative abundance of Th1 versus Th17 cells—predicts response to specific therapeutic approaches, with TNF-α inhibitors benefiting patients with enriched Th1/Th17 populations while IL-17 inhibitors may be superior for other subsets[6]. This concept of precision medicine in PsA, guided by mechanistic biomarkers, represents a promising future direction.

## Conclusion

The pathophysiology of psoriatic arthritis emerges from the integration of genetic predisposition, environmental triggers, and dysregulated immune responses targeting multiple anatomical sites including skin, synovium, enthesis, and bone. The IL-23/IL-17 cytokine axis represents the dominant inflammatory pathway, operating within a complex inflammatory milieu that includes TNF-α, IL-6, and numerous chemokines and growth factors. Multiple innate immune cell populations—macrophages, dendritic cells, neutrophils, and mast cells—serve as primary drivers of inflammation, creating a permissive environment for Th17 and CD8+ T cell responses. Paradoxically, the same inflammatory mediators that drive synovial inflammation and cartilage destruction simultaneously promote new bone formation at entheseal sites, creating the distinctive radiographic pattern of PsA with simultaneous erosions and proliferation[1][3][4][5][6]. Synovial fibroblasts, activated by IL-17 and TNF-α, undergo phenotypic transformation from structural cells to invasive effector cells producing matrix-degrading enzymes and pro-inflammatory mediators. Metabolic reprogramming toward enhanced glycolysis supports the inflammatory responses while epigenetic modifications ensure sustained dysregulation of key inflammatory genes. The mechanistic insights gained from recent molecular and cellular investigations have directly enabled development of effective targeted therapies, with JAK inhibitors, IL-17 inhibitors, and IL-23 inhibitors demonstrating efficacy in controlling disease activity. Future directions include refinement of mechanistic biomarkers to guide precision medicine approaches, investigation of previously underappreciated pathways such as immunoproteasome-mediated antigen presentation in treatment-resistant disease, and exploration of therapies promoting resolution of inflammation through fibroblast phenotype switching and regulatory T cell expansion. The remarkable clinical heterogeneity of PsA reflects variable involvement of these mechanistic pathways across affected individuals, emphasizing the need for continued integration of molecular understanding with clinical phenotyping to achieve optimal patient outcomes.