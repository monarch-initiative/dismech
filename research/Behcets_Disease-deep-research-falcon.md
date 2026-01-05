---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-18T09:46:25.066260'
end_time: '2025-12-18T09:53:57.515947'
duration_seconds: 452.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Behcet's Disease
  mondo_id: ''
  category: Autoimmune
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
- **Disease Name:** Behcet's Disease
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Behcet's Disease**.
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
- **Disease Name:** Behcet's Disease
- **MONDO ID:**  (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Behcet's Disease**.
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
- Disease Name: Behçet’s Disease (BD)
- MONDO ID:  
- Category: Autoimmune/autoinflammatory variable-vessel vasculitis

Pathophysiology overview (current understanding, 2023–2024)
Behçet’s disease is now regarded as a primary systemic vasculitis affecting veins and arteries of any size, driven by gene–environment interactions that dysregulate both innate and adaptive immunity. Core features include neutrophil hyperactivation and NET formation, Th1/Th17 polarization with impaired regulatory T-cell control, endothelial dysfunction and microthrombosis, and genetic risk dominated by HLA-B*51 with ERAP1 epistasis and non‑HLA loci linked to IL-23/Th17 and IL-10 pathways (IL23R–IL12RB2, STAT4, IL10, CCR1/KLRC4, MICA). Interferon/JAK–STAT and NF‑κB signaling in antigen-presenting cells contribute to systemic inflammation. Oral/gut microbial dysbiosis is plausibly involved as a trigger and amplifier of mucosal and ocular auto-inflammation. These mechanisms connect to major organ phenotypes: mucocutaneous ulcers, vision-threatening uveitis, vascular thrombosis/aneurysm, ileocecal intestinal disease, and neuro-Behçet (parenchymal and vascular forms) (https://doi.org/10.1056/NEJMra2305712; Feb 15, 2024) (saadoun2024behçetssyndrome. pages 1-2). Ocular reviews and integrated omics reinforce Th1/Th17 dominance and neutrophil/endothelial axes, with emerging targets in JAK–STAT and Th17/Treg balance (https://doi.org/10.1186/s12974-024-03123-6; May 2024; https://doi.org/10.3389/fimmu.2023.1206959; Sep 2023; https://doi.org/10.1038/s41598-025-87130-4; Jan 2025) (guan2024decodingbehcet’suveitis pages 1-2, lin2023advancesinpathogenesis pages 1-2, pu2025integratedanalysisof pages 8-9).

Evidence table
| Mechanism / Theme | Key molecules / genes (HGNC) | Cell types (CL) | Organ / tissue (UBERON) | Representative finding (2023–2024, quantitative where available) | Therapeutic implication | Source |
|---|---|---:|---|---|---|---|
| Neutrophil hyperactivation & NETs | MPO, ELANE, PADI4 | Neutrophil (CL) | Blood, skin, oral mucosa (UBERON) | NET formation and neutrophil hyperactivation drive endothelial injury and a procoagulant state in BD; NETs linked to tissue vasculitis and mucosal damage (multiple 2023–2025 multi-omic/review reports). | Targeting innate neutrophil activation/NETs (anti-TNF, anti-IL‑1, DNase approaches) may reduce vasculitis and mucosal injury. | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Shimizu J., Front Med/2023, https://doi.org/10.3389/fmed.2023.1055753 (shimizu2023innateimmuneresponses pages 10-11); Pu Y., Sci Rep/2025, https://doi.org/10.1038/s41598-025-87130-4 (pu2025integratedanalysisof pages 8-9) |
| Th1 / Th17 / Treg imbalance and Tc17 | IFNG, IL17A, IL23R, IL10, STAT4 | CD4+ Th1/Th17, CD8+ Tc17, Treg (CL) | Peripheral blood, mucosa, ocular tissues | Consistent Th1 (IFN-γ)/Th17 (IL‑17/IL‑23) skewing with reduced regulatory T‑cell control; multi‑omic data identify Th1/Th17 hyperactivity as dominant signature in BD (integrated analyses). | Cytokine-targeting (anti‑IL‑17, anti‑IL‑12/23), JAK inhibition and therapies restoring Treg/Th17 balance are rational strategies. | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Pu Y., Sci Rep/2025, https://doi.org/10.1038/s41598-025-87130-4 (pu2025integratedanalysisof pages 8-9); Guan Y., J Neuroinflamm/2024, https://doi.org/10.1186/s12974-024-03123-6 (guan2024decodingbehcet’suveitis pages 1-2) |
| Endothelial dysfunction & vasculitis biology | ICAM1, SELE, prothrombotic mediators | Endothelial cell, platelets, neutrophils (CL) | Arterial & venous vessels (UBERON:vasculature) | Histology shows leukocytoclastic vasculitis, perivascular infiltrates and microthrombi; multi‑omics report endothelial injury and haemostatic activation as core features. | Anticytokine (anti‑TNF), anticoagulation considerations and therapies reducing endothelial activation are key; IL‑1/IL‑6 blockade considered in selected vascular BD. | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Pu Y., Sci Rep/2025, https://doi.org/10.1038/s41598-025-87130-4 (pu2025integratedanalysisof pages 8-9); Lavalle S., Medicina/2024, https://doi.org/10.3390/medicina60040562 (lavalle2024behçet’sdiseasepathogenesis pages 10-11) |
| Genetics: HLA‑B*51 – ERAP1, IL10, IL23R–IL12RB2, STAT4, CCR1/KLRC4, MICA | HLA‑B (HLA‑B*51), ERAP1, IL10, IL23R, IL12RB2, STAT4, CCR1, KLRC4, MICA | Antigen‑presenting cells, T cells (CL) | Systemic (immune organs, mucosa) | Strong HLA‑B*51 association (~~6‑fold increased risk reported) with epistatic interaction with ERAP1 (reported OR ~4.6 for combined effect); multiple GWAS loci implicate IL10, IL23R–IL12RB2, STAT4 and NK/CCR loci. | Genetic strata inform mechanistic subtypes and suggest antigen‑processing (ERAP1/HLA) and cytokine pathway targets (IL‑23/IL‑17, JAK/STAT). | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Lin S., Front Immunol/2023, https://doi.org/10.3389/fimmu.2023.1206959 (lin2023advancesinpathogenesis pages 1-2) |
| IFN / JAK‑STAT signatures & APC NF‑κB | IFNA/IFNB/IFNG, JAK1, STAT1/3, NFKB1 | Dendritic cells, monocytes/macrophages (CL) | Blood, skin, ocular tissues | Transcriptomic/interferome signals and enhanced NF‑κB activity in antigen‑presenting cells have been reported, supporting IFN and JAK‑STAT pathway involvement in BD immune activation. | JAK inhibitors and modulators of IFN/NF‑κB pathways are under study and show case/series evidence for refractory ocular/intestine/vascular BD. | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Pu Y., Sci Rep/2025, https://doi.org/10.1038/s41598-025-87130-4 (pu2025integratedanalysisof pages 8-9); Lin S., Front Immunol/2023, https://doi.org/10.3389/fimmu.2023.1206959 (lin2023advancesinpathogenesis pages 1-2) |
| Microbiome & metabolome (oral / gut; intestinal BD) | Microbial taxa shifts (no single HGNC) | Mucosal immune cells, MAIT/γδ T cells (CL) | Oral cavity, gut (UBERON) | Studies report oral/gut dysbiosis signatures linked to BD flares and intestinal BD; integrated microbiome–metabolome work highlights disease‑specific profiles distinguishing intestinal BD from IBD. | Microbiome‑based biomarkers and microbiota‑targeted therapies (diet, probiotics, FMT experimental) are emerging research directions. | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Guan Y., J Neuroinflamm/2024, https://doi.org/10.1186/s12974-024-03123-6 (guan2024decodingbehcet’suveitis pages 1-2); Pu Y., Sci Rep/2025, https://doi.org/10.1038/s41598-025-87130-4 (pu2025integratedanalysisof pages 8-9) |
| Organ phenotype — Oral / Genital ulcers | IL1B, TNF, NE (ELANE) | Neutrophils, keratinocytes, mucosal T cells (CL) | Oral & genital mucosa (UBERON) | Recurrent oral ulcers are the near‑universal presenting sign (>90% of patients); mucosal lesions show neutrophil‑predominant infiltration and leukocytoclastic vasculitis. | Local/topical care plus systemic anti‑inflammatory (colchicine, azathioprine) and targeted biologics (apremilast for mucocutaneous disease) reduce ulcer burden. | Lavalle S., Medicina/2024, https://doi.org/10.3390/medicina60040562 (lavalle2024behçet’sdiseasepathogenesis pages 10-11); Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2) |
| Organ phenotype — Uveitis (ocular BD) | IL17A, IFNG, TNF, RORC | CD4+/CD8+ T cells, macrophages, retinal endothelium (CL) | Uveal tract, retina (UBERON) | Behçet uveitis affects >2/3 of BD patients and is vision‑threatening; one review estimates ~20.4% of affected eyes may become blind from recurrent episodes. | Rapid immunosuppression and biologics (anti‑TNF agents; IL‑6/IL‑17 blockers; increasing evidence for JAK inhibitors) improve outcomes and are used for refractory cases. | Guan Y., J Neuroinflamm/2024, https://doi.org/10.1186/s12974-024-03123-6 (guan2024decodingbehcet’suveitis pages 1-2); Lin S., Front Immunol/2023, https://doi.org/10.3389/fimmu.2023.1206959 (lin2023advancesinpathogenesis pages 1-2); Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2) |
| Organ phenotype — Vascular / Intestinal / Neurologic BD | Procoagulant factors, IL1B, IFNs | Endothelium, monocytes, neutrophils, CNS glia (CL) | Large/small vessels, ileocecal gut, CNS (UBERON) | Vascular BD shows venous/arterial thrombosis and aneurysm risk; intestinal BD often targets ileocecal region with neutrophil/lymphocyte infiltrates; neuro‑BD shows perivascular cuffing—linking immune activation to organ damage. | Organ‑specific immunosuppression (anti‑TNF, anti‑IL‑1/IL‑6, JAK inhibitors), surgical approaches for aneurysms/intestinal complications; therapeutic choice informed by phenotype and molecular signatures. | Saadoun D., NEJM/2024, https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2); Shimizu J., Front Med/2023, https://doi.org/10.3389/fmed.2023.1055753 (shimizu2023innateimmuneresponses pages 10-11); Lavalle S., Medicina/2024, https://doi.org/10.3390/medicina60040562 (lavalle2024behçet’sdiseasepathogenesis pages 10-11) |


*Table: A compact evidence table summarizing major molecular/cellular mechanisms, affected cell types and tissues, representative quantitative findings, therapeutic implications, and primary 2023–2025 sources (selected evidence IDs). This supports linking mechanistic biology to organ phenotypes and current targeted therapies (saadoun2024behçetssyndrome. pages 1-2).*

1) Core pathophysiology
- Innate immunity and NETs: Neutrophils in BD are primed to generate ROS and form NETs, promoting endothelial injury, perivascular inflammation, and a procoagulant milieu; lesions often show leukocytoclastic vasculitis and microthrombi (https://doi.org/10.1056/NEJMra2305712; 2024) (saadoun2024behçetssyndrome. pages 1-2). Reviews of innate mechanisms corroborate NET-linked macrophage activation and neutrophilic panniculitis/vasculitis in skin and mucosa (https://doi.org/10.3389/fmed.2023.1055753; 2023) (shimizu2023innateimmuneresponses pages 10-11).
- Adaptive immunity: Th1 (IFN-γ/TNF-α) and Th17 (IL‑17/IL‑23) pathways are upregulated relative to Treg control; multi-omic integration emphasizes Th1/Th17 hyperactivity as the dominant molecular signature (https://doi.org/10.1038/s41598-025-87130-4; 2025) (pu2025integratedanalysisof pages 8-9). Ocular BD literature highlights Th1/Th17 and Treg imbalance in uveitis pathogenesis (https://doi.org/10.1186/s12974-024-03123-6; 2024; https://doi.org/10.3389/fimmu.2023.1206959; 2023) (guan2024decodingbehcet’suveitis pages 1-2, lin2023advancesinpathogenesis pages 1-2).
- Endothelial dysfunction and vasculitis biology: Endothelial activation, perivascular leukocyte infiltration, and microthrombi underpin the variable-vessel vasculitis phenotype; haemostatic system activation and oxidative stress emerge in integrated analyses (https://doi.org/10.1056/NEJMra2305712; 2024; https://doi.org/10.1038/s41598-025-87130-4; 2025) (saadoun2024behçetssyndrome. pages 1-2, pu2025integratedanalysisof pages 8-9).
- Genetic architecture and antigen processing: HLA‑B*51 confers major risk (reported ~6-fold) with a notable epistatic interaction with ERAP1 altering peptide trimming and HLA-I immunopeptidomes; non‑HLA loci include IL23R–IL12RB2, IL10, STAT4, CCR1/KLRC4, MICA that converge on Th1/Th17 and innate cell pathways (https://doi.org/10.1056/NEJMra2305712; 2024; https://doi.org/10.3389/fimmu.2023.1206959; 2023) (saadoun2024behçetssyndrome. pages 1-2, lin2023advancesinpathogenesis pages 1-2).
- Interferon/JAK–STAT and NF‑κB signatures: Transcriptomic/interferome signals and APC NF‑κB activation have been reported in BD, consistent with heightened cytokine and co‑stimulatory signaling; these signatures motivate trials of JAK inhibition and anti‑cytokine therapies (https://doi.org/10.1056/NEJMra2305712; 2024; https://doi.org/10.1038/s41598-025-87130-4; 2025) (saadoun2024behçetssyndrome. pages 1-2, pu2025integratedanalysisof pages 8-9).
- Microbiome/metabolome: Oral and gut dysbiosis are implicated as triggers, with intestinal BD showing disease‑specific microbial and metabolic profiles distinct from UC/controls in integrative studies; BD shares reduction in SCFA producers with IBD (NEJM 2024 summary; ocular BD review; integrated omics) (saadoun2024behçetssyndrome. pages 1-2, guan2024decodingbehcet’suveitis pages 1-2, pu2025integratedanalysisof pages 8-9).

2) Key molecular players
- Genes/proteins (HGNC): HLA‑B (HLA‑B*51), ERAP1, IL10, IL23R, IL12RB2, STAT4, CCR1, KLRC4, MICA; cytokines: TNF (TNF), IFNG (IFN‑γ), IL17A, IL23A/IL12B; signaling: JAK1/JAK3/STAT3/STAT1; innate mediators: MPO, ELANE (neutrophil elastase), PADI4; transcription factors: NFKB1‑RELA (p50/p65), RORC (RORγt) (https://doi.org/10.1056/NEJMra2305712; 2024; https://doi.org/10.3389/fimmu.2023.1206959; 2023; https://doi.org/10.1186/s12974-024-03123-6; 2024) (saadoun2024behçetssyndrome. pages 1-2, lin2023advancesinpathogenesis pages 1-2, guan2024decodingbehcet’suveitis pages 1-2).
- Chemical entities (CHEBI): TNF inhibitors (infliximab, adalimumab), PDE4 inhibitor apremilast, IL‑12/23 inhibitor, IL‑17 inhibitors, JAK inhibitors; anti‑IL‑1 agents used in selected phenotypes (https://doi.org/10.3390/medicina60040562; 2024) (lavalle2024behçet’sdiseasepathogenesis pages 10-11).
- Cell types (CL): Neutrophils (NETosis), monocytes/macrophages and dendritic cells (APC activation), CD4+ Th1/Th17 and Tregs, CD8+ Tc17, NK cells (KLRC4 pathway) (saadoun2024behçetssyndrome. pages 1-2, shimizu2023innateimmuneresponses pages 2-4).
- Anatomical locations (UBERON): Oral/genital mucosa, skin, uveal tract/retina, systemic vasculature (veins/arteries), ileocecal intestine, CNS (parenchymal and vascular neuro‑BD) (saadoun2024behçetssyndrome. pages 1-2, shimizu2023innateimmuneresponses pages 2-4).

3) Disrupted biological processes (candidate GO terms)
- Positive regulation of neutrophil activation and NET formation; response to reactive oxygen species; leukocyte adhesion to endothelium; cytokine-mediated signaling via JAK–STAT; NF‑κB signaling; Th17 cell differentiation; regulation of Treg-mediated tolerance; antigen processing and presentation via MHC class I (ERAP1/HLA‑B*51 axis); type I/II interferon signaling; regulation of coagulation and platelet activation (saadoun2024behçetssyndrome. pages 1-2, pu2025integratedanalysisof pages 8-9, lin2023advancesinpathogenesis pages 1-2).

4) Cellular components (GO-CC mapping)
- Neutrophil granules and extracellular region (NETs); plasma membrane of endothelial cells (adhesion molecules); MHC class I peptide-loading complex in ER (ERAP1); cytosol/nucleus for NF‑κB and STAT transcriptional complexes; extracellular space (cytokines/chemokines) (saadoun2024behçetssyndrome. pages 1-2, lin2023advancesinpathogenesis pages 1-2).

5) Disease progression (sequence of events)
- Triggering (microbial dysbiosis, mucosal injury, environmental stimuli) in genetically susceptible hosts → innate activation with neutrophil priming, ROS and NETs → endothelial activation/leukocytoclastic vasculitis and microthrombi → antigen presentation bias (HLA‑B*51/ERAP1) and APC NF‑κB upregulation → Th1/Th17 polarization with insufficient Treg control, with possible Tc17 involvement → organ-specific inflammation: oral/genital ulcers, ocular uveitis with retinal vasculitis, vascular thrombosis/aneurysm, ileocecal ulcers, and neuroinflammation (https://doi.org/10.1056/NEJMra2305712; 2024; ocular/innate reviews) (saadoun2024behçetssyndrome. pages 1-2, guan2024decodingbehcet’suveitis pages 1-2, shimizu2023innateimmuneresponses pages 10-11).

6) Phenotypic manifestations and mechanistic links
- Mucocutaneous: recurrent oral (>90%) and genital ulcers with neutrophil‑predominant infiltrates and small‑vessel vasculitis; linked to NET/IL‑1/TNF axes and barrier dysbiosis (https://doi.org/10.3390/medicina60040562; 2024; NEJM 2024) (lavalle2024behçet’sdiseasepathogenesis pages 10-11, saadoun2024behçetssyndrome. pages 1-2).
- Ocular: bilateral, recurrent, non‑granulomatous uveitis with retinal vasculitis; Th1/Th17 and endothelial activation dominate; cumulative blindness risk is substantial without targeted therapy (https://doi.org/10.1186/s12974-024-03123-6; 2024) (guan2024decodingbehcet’suveitis pages 1-2).
- Vascular: venous thrombosis and arterial aneurysms result from endothelial injury, neutrophil/NET-driven thrombogenicity, and cytokine activation (NEJM 2024) (saadoun2024behçetssyndrome. pages 1-2).
- Intestinal BD: ileocecal ulcers with neutrophil/lymphocyte infiltrates; microbiome–metabolome profiles differ from UC/controls but share SCFA depletion, implicating barrier and innate pathways (integrated omics and reviews) (saadoun2024behçetssyndrome. pages 1-2, guan2024decodingbehcet’suveitis pages 1-2, pu2025integratedanalysisof pages 8-9).
- Neurologic BD: perivascular cuffing and inflammatory infiltrates suggest vasculitic and parenchymal mechanisms downstream of Th1/Th17 and innate activation (innate review; NEJM 2024) (shimizu2023innateimmuneresponses pages 10-11, saadoun2024behçetssyndrome. pages 1-2).

Recent developments and latest research (priority 2023–2024)
- Consolidation of BD as a variable-vessel vasculitis with combined autoinflammatory/autoimmune features, with quantitative synthesis of genetic architecture (HLA‑B*51–ERAP1 epistasis) and Th1/Th17/NETs mechanisms in NEJM 2024 review (https://doi.org/10.1056/NEJMra2305712; 2024) (saadoun2024behçetssyndrome. pages 1-2).
- Ocular BD reviews (2023–2024) emphasize Th1/Th17 dominance, Treg dysfunction, and new targets including JAK inhibition and Th17/Treg rebalancing (https://doi.org/10.3389/fimmu.2023.1206959; 2023; https://doi.org/10.1186/s12974-024-03123-6; 2024) (lin2023advancesinpathogenesis pages 1-2, guan2024decodingbehcet’suveitis pages 1-2).
- Integrated multi‑omics (2025; data collected 2024) identify Th1/Th17 hyperactivity, enhanced neutrophil chemotaxis, endothelial injury, coagulation activation, and oxidative stress as central molecular programs (https://doi.org/10.1038/s41598-025-87130-4; 2025) (pu2025integratedanalysisof pages 8-9).

Current applications and real-world implementations
- Organ‑tailored therapy grounded in mechanisms: mucocutaneous disease often responds to colchicine, azathioprine, PDE4 inhibition (apremilast), while sight‑threatening uveitis and major organ involvement utilize anti‑TNF agents; IL‑1/IL‑6, IL‑12/23 or IL‑17 blockade and JAK inhibitors are used in refractory cases in practice and studies (https://doi.org/10.3390/medicina60040562; 2024; NEJM 2024) (lavalle2024behçet’sdiseasepathogenesis pages 10-11, saadoun2024behçetssyndrome. pages 1-2).

Expert opinions and consensus
- Authoritative reviews recommend a phenotype‑driven, early biologic approach for ocular and vascular disease, with escalation to targeted cytokine/JAK pathways for refractory inflammation; they stress genetic–immunologic heterogeneity (NEJM 2024; ocular/innate reviews 2023–2024) (saadoun2024behçetssyndrome. pages 1-2, guan2024decodingbehcet’suveitis pages 1-2, shimizu2023innateimmuneresponses pages 10-11).

Relevant statistics and data (selected)
- Epidemiology: prevalence varies widely by geography (e.g., Turkey up to ~420 per 100,000) (NEJM 2024) (saadoun2024behçetssyndrome. pages 1-2).
- Genetics: HLA‑B*51 association (approximate ~6× risk) and ERAP1 epistasis reported with odds ratio ~4.6 in combined analyses (NEJM 2024) (saadoun2024behçetssyndrome. pages 1-2).
- Ocular outcomes: BD uveitis occurs in >2/3 of patients; recurrent attacks can result in blindness in a substantial fraction of affected eyes without effective therapy (J Neuroinflammation 2024) (guan2024decodingbehcet’suveitis pages 1-2).

Ontology-annotated knowledge elements
- Genes/proteins (HGNC): HLA‑B, ERAP1, IL10, IL23R, IL12RB2, STAT4, CCR1, KLRC4, MICA; cytokines TNF, IFNG, IL17A; signaling JAK1, STAT1/3, NFKB1/RELA; NET enzymes MPO, ELANE, PADI4 (saadoun2024behçetssyndrome. pages 1-2, lin2023advancesinpathogenesis pages 1-2, guan2024decodingbehcet’suveitis pages 1-2).
- GO Biological Processes: neutrophil activation and extracellular trap formation; antigen processing and presentation via MHC class I; JAK–STAT cascade; regulation of NF‑κB transcription factor activity; Th17 cell differentiation; negative regulation of immune response by Treg; response to type I/II interferon; regulation of blood coagulation (saadoun2024behçetssyndrome. pages 1-2, pu2025integratedanalysisof pages 8-9).
- GO Cellular Components: ER lumen/peptide-loading complex (ERAP1); extracellular region (NETs/cytokines); nucleus (NF‑κB/STAT complexes); plasma membrane (adhesion molecules) (lin2023advancesinpathogenesis pages 1-2, saadoun2024behçetssyndrome. pages 1-2).
- Phenotype associations (HP): HP:0011107 Recurrent oral ulcers; HP:0001112 Uveitis; HP:0002632 Deep venous thrombosis; HP:0012387 Arterial aneurysm; HP:0002589 Abdominal pain/ileocecal ulcer; HP:0001287 Encephalopathy (neuro‑Behçet) (saadoun2024behçetssyndrome. pages 1-2, guan2024decodingbehcet’suveitis pages 1-2, shimizu2023innateimmuneresponses pages 2-4).
- Cell types (CL): CL:0000096 Neutrophil; CL:0000545 Dendritic cell; CL:0000236 Monocyte; CL:0000911 CD4+ T cell (Th1/Th17/Treg); CL:0000905 CD8+ T cell; CL:0000623 Endothelial cell (saadoun2024behçetssyndrome. pages 1-2, shimizu2023innateimmuneresponses pages 10-11).
- Anatomical locations (UBERON): UBERON:0001836 Oral mucosa; UBERON:0000066 Skin; UBERON:0001772 Uvea; UBERON:0002390 Retina; UBERON:0002405 Vein; UBERON:0001987 Artery; UBERON:0002114 Small intestine (ileum/ileocecal); UBERON:0000955 Brain (saadoun2024behçetssyndrome. pages 1-2, shimizu2023innateimmuneresponses pages 2-4).
- Chemical entities (CHEBI): apremilast (PDE4 inhibitor), infliximab/adalimumab (anti‑TNF), ustekinumab (anti‑IL‑12/23), secukinumab (anti‑IL‑17A), JAK inhibitors (e.g., tofacitinib/baricitinib/upadacitinib), canakinumab/anakinra (anti‑IL‑1)—mechanistically aligned classes (lavalle2024behçet’sdiseasepathogenesis pages 10-11, saadoun2024behçetssyndrome. pages 1-2).

Key evidence items (PMIDs/DOIs, dates, URLs)
- Saadoun D, Bodaghi B, Cacoub P. Behçet’s syndrome. NEJM. Feb 15, 2024. DOI: 10.1056/NEJMra2305712. https://doi.org/10.1056/NEJMra2305712 (saadoun2024behçetssyndrome. pages 1-2).
- Lin S et al. Advances in pathogenesis and treatment of ocular involvement in BD. Front Immunol. Sep 29, 2023. DOI: 10.3389/fimmu.2023.1206959. https://doi.org/10.3389/fimmu.2023.1206959 (lin2023advancesinpathogenesis pages 1-2).
- Guan Y et al. Decoding Behçet’s uveitis. J Neuroinflammation. May 2024. DOI: 10.1186/s12974-024-03123-6. https://doi.org/10.1186/s12974-024-03123-6 (guan2024decodingbehcet’suveitis pages 1-2).
- Shimizu J et al. Innate immune responses in BD and RP. Front Med. Jun 2023. DOI: 10.3389/fmed.2023.1055753. https://doi.org/10.3389/fmed.2023.1055753 (shimizu2023innateimmuneresponses pages 10-11).
- Lavalle S et al. Behçet’s disease: pathogenesis, clinical features, and treatment. Medicina. Mar 2024. DOI: 10.3390/medicina60040562. https://doi.org/10.3390/medicina60040562 (lavalle2024behçet’sdiseasepathogenesis pages 10-11, lavalle2024behçet’sdiseasepathogenesis pages 9-10).
- Pu Y et al. Integrated analysis of genetic, proteinic, and metabolomic alterations in BD. Sci Rep. Jan 2025 (data collected in 2024). DOI: 10.1038/s41598-025-87130-4. https://doi.org/10.1038/s41598-025-87130-4 (pu2025integratedanalysisof pages 8-9).

Direct supporting statements (quotes)
- “Pathogenesis is viewed as genetically predisposed hosts exposed to environmental triggers … alterations of gut/salivary mucosal flora. Genetics: strong HLA‑B*51 association … loci include genes linked to Th1/Th17 polarization … and IL10. Immune mechanisms: … Th1 … Th17 … diminished regulatory T‑cell activity, and neutrophil hyperactivation.” (NEJM 2024) (saadoun2024behçetssyndrome. pages 1-2).
- “Modules of antigen-presenting cells were associated with BS … Th17 cells … activation of the NF‑κB pathway … IL‑17‑associated pathways … IL‑17‑producing CD8+ T cells (Tc17) may play a critical role in BS.” (Ocular/immune system reviews; summarized) (lin2023advancesinpathogenesis pages 1-2, guan2024decodingbehcet’suveitis pages 1-2).

Mechanism-to-therapy mapping (applications)
- NETs/endothelial axis → anti‑TNF for ocular/vascular disease; consideration of anti‑IL‑1/IL‑6 in selected phenotypes (saadoun2024behçetssyndrome. pages 1-2, lavalle2024behçet’sdiseasepathogenesis pages 10-11).
- Th17/Tc17 axis → anti‑IL‑17 or anti‑IL‑12/23; JAK inhibition as pathway‑level modulation (guan2024decodingbehcet’suveitis pages 1-2, lin2023advancesinpathogenesis pages 1-2).
- APC NF‑κB and IFN/JAK–STAT signatures → JAK inhibitors in refractory mucocutaneous/ocular/intestinal disease; phenotype‑guided escalation (saadoun2024behçetssyndrome. pages 1-2, pu2025integratedanalysisof pages 8-9).

Limitations and open questions
- The precise microbiome causal pathways and antigenic drivers remain incompletely defined; interferome and cell‑type–resolved datasets are expanding but heterogeneous. Prospective mechanotype‑guided trials are needed to align genetic/immune endotypes with therapy selection (saadoun2024behçetssyndrome. pages 1-2, pu2025integratedanalysisof pages 8-9).

Overall synthesis
BD pathophysiology reflects a genetically primed, mucosa‑initiated systemic vasculitis in which neutrophil/NET–endothelial circuits, Th1/Th17 skewing (with possible Tc17), and APC NF‑κB/IFN–JAK–STAT signaling cooperate to produce relapsing inflammation across mucocutaneous, ocular, vascular, intestinal, and neurologic sites. Current real‑world practice increasingly targets these axes with anti‑TNF, IL‑17/IL‑12‑23, PDE4, and JAK inhibition in phenotype‑guided regimens (https://doi.org/10.1056/NEJMra2305712; 2024; https://doi.org/10.1186/s12974-024-03123-6; 2024) (saadoun2024behçetssyndrome. pages 1-2, guan2024decodingbehcet’suveitis pages 1-2).

References

1. (saadoun2024behçetssyndrome. pages 1-2): David Saadoun, Bahram Bodaghi, and Patrice Cacoub. Behçet's syndrome. The New England journal of medicine, 390 7:640-651, Feb 2024. URL: https://doi.org/10.1056/nejmra2305712, doi:10.1056/nejmra2305712. This article has 78 citations and is from a highest quality peer-reviewed journal.

2. (guan2024decodingbehcet’suveitis pages 1-2): Yuxuan Guan, Fuzhen Li, Na Li, and Peizeng Yang. Decoding behcet’s uveitis: an in-depth review of pathogenesis and therapeutic advances. Journal of Neuroinflammation, May 2024. URL: https://doi.org/10.1186/s12974-024-03123-6, doi:10.1186/s12974-024-03123-6. This article has 19 citations and is from a peer-reviewed journal.

3. (lin2023advancesinpathogenesis pages 1-2): Suibin Lin, Zhirong Xu, Zhiming Lin, Baozhao Xie, and Junmei Feng. Advances in pathogenesis and treatment of ocular involvement in behcet’s disease. Frontiers in Immunology, Sep 2023. URL: https://doi.org/10.3389/fimmu.2023.1206959, doi:10.3389/fimmu.2023.1206959. This article has 7 citations and is from a peer-reviewed journal.

4. (pu2025integratedanalysisof pages 8-9): Yanlin Pu, Jing Liang, Yao Wang, Wanyun Zhang, Chuiren Zhou, Ju Shao, Jin Hu, Minghui Chen, Yunjie Shi, Yongdan Mao, and Zhijun Chen. Integrated analysis of genetic, proteinic, and metabolomic alterations in behcet’s disease. Scientific Reports, Jan 2025. URL: https://doi.org/10.1038/s41598-025-87130-4, doi:10.1038/s41598-025-87130-4. This article has 4 citations and is from a peer-reviewed journal.

5. (shimizu2023innateimmuneresponses pages 10-11): Jun Shimizu, Masanori A. Murayama, Yoshihisa Mizukami, Nagisa Arimitsu, Kenji Takai, and Yoshishige Miyabe. Innate immune responses in behçet disease and relapsing polychondritis. Frontiers in Medicine, Jun 2023. URL: https://doi.org/10.3389/fmed.2023.1055753, doi:10.3389/fmed.2023.1055753. This article has 13 citations and is from a poor quality or predatory journal.

6. (lavalle2024behçet’sdiseasepathogenesis pages 10-11): Salvatore Lavalle, Sebastiano Caruso, Roberta Foti, Caterina Gagliano, Salvatore Cocuzza, Luigi La Via, Federica Maria Parisi, Christian Calvo-Henriquez, and Antonino Maniaci. Behçet’s disease, pathogenesis, clinical features, and treatment approaches: a comprehensive review. Medicina, 60:562, Mar 2024. URL: https://doi.org/10.3390/medicina60040562, doi:10.3390/medicina60040562. This article has 55 citations and is from a poor quality or predatory journal.

7. (shimizu2023innateimmuneresponses pages 2-4): Jun Shimizu, Masanori A. Murayama, Yoshihisa Mizukami, Nagisa Arimitsu, Kenji Takai, and Yoshishige Miyabe. Innate immune responses in behçet disease and relapsing polychondritis. Frontiers in Medicine, Jun 2023. URL: https://doi.org/10.3389/fmed.2023.1055753, doi:10.3389/fmed.2023.1055753. This article has 13 citations and is from a poor quality or predatory journal.

8. (lavalle2024behçet’sdiseasepathogenesis pages 9-10): Salvatore Lavalle, Sebastiano Caruso, Roberta Foti, Caterina Gagliano, Salvatore Cocuzza, Luigi La Via, Federica Maria Parisi, Christian Calvo-Henriquez, and Antonino Maniaci. Behçet’s disease, pathogenesis, clinical features, and treatment approaches: a comprehensive review. Medicina, 60:562, Mar 2024. URL: https://doi.org/10.3390/medicina60040562, doi:10.3390/medicina60040562. This article has 55 citations and is from a poor quality or predatory journal.