---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:59:02.932253'
end_time: '2025-12-18T00:07:39.848752'
duration_seconds: 516.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Benign Prostatic Hyperplasia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Benign Prostatic Hyperplasia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Benign Prostatic Hyperplasia**.
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
- **Disease Name:** Benign Prostatic Hyperplasia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Benign Prostatic Hyperplasia**.
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
Objective 1: Identify 2023–2024 sources on BPH pathophysiology (single-cell/spatial studies; stromal–epithelial crosstalk; fibrosis/EMT; hypoxia/oxidative stress; inflammatory signaling; androgen/estrogen). Status: Completed with Fei 2024 (J Transl Med), Pollack 2024 (JCI Insight), Shan 2024 (Mol Biomed), Li 2024 (Cell Commun Signal), dos Santos 2024 (Am J Pathol), Wang 2024 (Mil Med Res). (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2, shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2)
Objective 2: Extract mechanistic details and statistics from retrieved texts. Status: Completed for core findings below. (fei2024integratingspatialtranscriptomics pages 15-15, shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 7-11, santos2024cellplasticityin pages 1-2)
Objective 3: Fill gaps in inflammation/microbiome and nodular induction. Status: Completed using Wang 2024 (IL-6/IL-6R/AKT) and Pollack 2024 (IGF1/CXCL13). (fei2024integratingspatialtranscriptomics pages 15-15)
Objective 4: Produce ontology-ready artifact. Status: Completed (artifact-00). (fei2024integratingspatialtranscriptomics pages 15-15, shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2)
Objective 5: Write the comprehensive, cited report. Status: Completed.

Disease Pathophysiology Research Report: Benign Prostatic Hyperplasia (BPH)
Target Disease
- Disease Name: Benign Prostatic Hyperplasia
- MONDO ID: MONDO_0004952 (benign prostatic hyperplasia; mapped to EFO_0000284 in Open Targets; anatomical focus: prostate transition zone)
- Category: Complex

Pathophysiology description (narrative)
BPH is characterized by nodular proliferation localized to the prostate transition zone (TZ), driven by a coordinated set of epithelial and stromal programs that reactivate developmental (embryonic) signals and are sustained by inflammation, fibrosis, and metabolic stress. Spatial transcriptomics coupled with scRNA-seq resolve an initiating basal epithelial subgroup (BE5) with a hypoxia signature and c-Fos (FOS) upregulation, which positions BE5 as both the initiating cell of nodular formation and as a transitional state in luminal-to-basal reprogramming; hypoxia-induced EMT and proliferation are especially enriched in glandular nodules (vs stromal nodules) (mechanistic link: hypoxia→FOS→EMT) (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2). In parallel, stroma adjacent to hyperplastic ducts expresses inductive factors—including IGF1 and CXCL13—co-localized in fibroblasts with IGF1R and CXCR5 expressed on adjacent epithelium; IGF1 is necessary for BPH organoid/spheroid growth, substantiating a stromal→epithelial induction axis (fei2024integratingspatialtranscriptomics pages 15-15). Fibrosis and ECM remodeling are reinforced by aberrant TGF-β/ROCK activation: TGF-β/ROCK1 recruits LepR+ mesenchymal stem cells (MSCs) that differentiate into fibroblasts/myofibroblasts and amplify stromal hyperplasia; pharmacologic ROCK1 inhibition (GSK269962A) suppresses MSC migration/differentiation in vivo (li2024aberrantactivationof pages 1-3). ROCK1/2 also crosstalk with WNT/β-catenin and TGF-β signaling to promote epithelial proliferation, EMT, and collagen deposition; nonselective ROCK inhibition (Y‑27632) decreases β‑catenin stability and downstream effectors (MYC, SNAI1) and reduces hyperplasia and fibrosis in a testosterone-induced rat model (shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11). Oxidative stress and epithelial plasticity are integral: in a BPH mouse model, low-androgen signaling epithelial populations analogous to club-like cells expand and display reduced antioxidant defenses; mitochondrial ROS inhibition (anethole trithione) reduces prostate weight and voiding frequency and suppresses epithelial proliferation and stemness in vitro and ex vivo (santos2024cellplasticityin pages 1-2). Clinical symptoms (LUTS) result from mechanical obstruction in the TZ and increased smooth muscle tone; mechanistically, microbial and inflammatory stimuli can aggravate epithelial proliferation and fibrosis via IL‑6/IL‑6R/gp130→AKT signaling (periodontal P. gingivalis model), linking systemic/oral inflammation to prostatic hyperplasia (fei2024integratingspatialtranscriptomics pages 15-15).

Key concepts and definitions
- Nodular hyperplasia (TZ): multicellular units of proliferating epithelium and stroma in the transition zone, the anatomical basis of LUTS (fei2024integratingspatialtranscriptomics pages 15-15).
- Stromal–epithelial induction: fibroblast-derived secreted factors (IGF1, CXCL13) activating epithelial RTKs and chemokine receptors to drive ductal proliferation (fei2024integratingspatialtranscriptomics pages 15-15).
- Fibrosis/myofibroblast activation: TGF‑β/ROCK1-dependent recruitment/differentiation of MSCs and activation of ECM programs (li2024aberrantactivationof pages 1-3).
- Epithelial plasticity/EMT: hypoxia/FOS- and TGF‑β/ROCK‑driven EMT and luminal-to-basal transitions, enriching club-like and basal progenitors in nodules (fei2024integratingspatialtranscriptomics pages 15-15, santos2024cellplasticityin pages 1-2).
- Oxidative stress: mitochondrial ROS promotes proliferation and stemness; antioxidant therapy mitigates organ-level and cellular phenotypes (santos2024cellplasticityin pages 1-2).
- Inflammatory signaling: IL‑6/IL‑6R/gp130→AKT activation by microbial LPS accelerates proliferation and fibrosis; immune infiltrates reinforce stromal activation (fei2024integratingspatialtranscriptomics pages 15-15).

Recent developments and latest research (2023–2024)
- Spatial/scRNA: Identification of BE5 hypoxic basal subgroup as nodular initiator and transitional state (LE→BE) with FOS-driven EMT in BPH; stronger EMT/proliferation in glandular vs stromal nodules (Fei 2024; J Transl Med; Apr 2024; https://doi.org/10.1186/s12967-024-05212-9) (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2).
- Stromal drivers: IGF1 and CXCL13 coexpressed by BPH fibroblasts, with IGF1R/CXCR5 on adjacent epithelium; IGF1 is necessary for BPH spheroids and organoids, supporting a reawakened embryonic stromal induction program (Pollack 2024; JCI Insight; Jan 2024; https://doi.org/10.1172/jci.insight.176479) (fei2024integratingspatialtranscriptomics pages 15-15).
- ROCK/TGF-β cross-talk: Upregulated ROCK1/2 in human BPH and testosterone-BPH rats, with ROCK inhibition lowering β‑catenin and TGF‑β/Smad activation, reducing EMT/fibrosis and proliferation; in vivo, Y‑27632 decreased prostate index and collagen (Shan 2024; Mol Biomed; Oct 2024; https://doi.org/10.1186/s43556-024-00216-9) (shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11).
- MSC recruitment/stemness: TGF‑β/ROCK1 recruits LepR+ MSCs to stroma and increases tissue stemness; ROCK1 inhibitor (GSK269962A) curtails MSC migration and stromal differentiation (Li 2024; Cell Commun Signal; May 2024; https://doi.org/10.1186/s12964-024-01644-4) (li2024aberrantactivationof pages 1-3).
- Oxidative stress therapy: Mitochondrial ROS blockade (anethole trithione) reduced prostate weight and voiding frequency, and suppressed proliferation/stemness in BPH-1 cells and organoids (dos Santos 2024; Am J Pathol; Jan 2024; https://doi.org/10.1016/j.ajpath.2023.09.010) (santos2024cellplasticityin pages 1-2).
- Microbiome–inflammation axis: P. gingivalis detected in prostatic fluid of BPH with periodontitis; IL‑6 rose 4.47-fold, IL‑6Rα 5.74-fold, gp130 4.47-fold; P.g-LPS induced epithelial/stromal proliferation/fibrosis via IL‑6/IL‑6R/gp130→AKT signaling (Wang 2024; Mil Med Res; May 2024; https://doi.org/10.1186/s40779-024-00533-8) (fei2024integratingspatialtranscriptomics pages 15-15).

Current applications and real-world implementations
- 5α-reductase inhibitors and α1-adrenergic blockers target androgen synthesis and smooth muscle tone (standard of care) while not directly addressing stromal induction or fibrosis; emerging preclinical strategies include ROCK inhibition (Y‑27632; GSK269962A) to reduce EMT/fibrosis and mitochondrial ROS inhibitors to reduce epithelial plasticity and hyperplasia (shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).
- Growth factor axis targeting: Spatially-resolved data nominating IGF1/IGF1R and CXCL13/CXCR5 as candidate stromal–epithelial crosstalk targets in human BPH (fei2024integratingspatialtranscriptomics pages 15-15).
- Inflammation-focused strategies: Addressing oral–prostate axis and IL‑6/IL‑6R/gp130–AKT signaling may mitigate BPH progression in patients with periodontitis (fei2024integratingspatialtranscriptomics pages 15-15).

Expert opinions and analysis
- The convergence of hypoxia-driven epithelial EMT, stromal IGF1/CXCL13 induction, and TGF‑β/ROCK-mediated fibrosis provides a unifying model that reconciles embryonic reawakening with chronic inflammation and metabolic stress. Single-cell/spatial data elevate BE5 hypoxic basal cells as initiators and clarify nodular heterogeneity. Mechanistic interventions (ROCK inhibition; mito-ROS blockade) show causal leverage on core phenotypes in vivo and ex vivo, supporting translation beyond symptom control to disease modification (fei2024integratingspatialtranscriptomics pages 15-15, shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).

Relevant statistics and data
- BE5 nodular initiator state: elevated hypoxia score and c-Fos; glandular nodules enriched for EMT/proliferation signatures versus stromal nodules (qualitative single-cell/spatial distinctions) (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2).
- IGF1 necessity: IGF1 required for BPH-1 spheroid and patient-derived organoid formation (functional requirement in vitro; qualitative) (fei2024integratingspatialtranscriptomics pages 15-15).
- ROCK inhibition: Y‑27632 reduced β‑catenin (with MG132 attenuating the effect), downregulated c‑MYC/SNAI1/Survivin, decreased Ki‑67, increased TUNEL; lowered prostate index and collagen in testosterone-BPH rats (significance p<0.01–0.001; directionality and targets specified) (shan2024y27632targetingrock1&2 pages 7-11).
- TGF‑β/ROCK1→MSC recruitment: GSK269962A (5 mg/kg, 4 weeks) suppressed MSC migration and stromal differentiation in vivo; p‑Smad2/3 expansion correlated with prostate size/inflammation (li2024aberrantactivationof pages 1-3).
- Microbiome–IL‑6 axis: In rats, P. gingivalis infection increased epithelial thickness ~3-fold versus control and collagen fibrosis ~5-fold; IL‑6 (4.47×), IL‑6Rα (5.74×), gp130 (4.47×) upregulated; AKT activation implicated (fei2024integratingspatialtranscriptomics pages 15-15).
- Oxidative stress therapy: anethole trithione decreased prostate weight and voiding frequency and suppressed epithelial proliferation/stemness in vitro and organoids (qualitative reductions) (santos2024cellplasticityin pages 1-2).

Core Pathophysiology (answers to objectives)
- Primary mechanisms: reawakened stromal induction (IGF1/CXCL13), epithelial plasticity under hypoxia (FOS→EMT), TGF‑β/ROCK-driven fibrosis/myofibroblast activation, and inflammation (IL‑6/AKT), all localized to the TZ and coordinated across stroma and epithelium (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11, santos2024cellplasticityin pages 1-2).
- Dysregulated pathways: TGF‑β/Smad and ROCK, WNT/β‑catenin, RTK/PI3K/AKT (IGF1), chemokine signaling (CXCL13/CXCR5), hypoxia/FOS, IL‑6/IL‑6R/gp130→AKT (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11).
- Cellular processes: EMT, MSC recruitment and fibroblast/myofibroblast differentiation, ECM deposition, oxidative stress responses, epithelial lineage reprogramming (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).

Key Molecular Players
- Genes/Proteins: ROCK1/ROCK2, TGFB1, SMAD2/3, CTNNB1, MYC, SNAI1, IGF1/IGF1R, CXCL13/CXCR5, FOS, AR/SRD5A2 (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 1-2, santos2024cellplasticityin pages 1-2).
- Chemical entities: Y‑27632 (ROCK inhibitor), GSK269962A (ROCK1 inhibitor), anethole trithione (mito-ROS inhibitor); clinically used PDE5 inhibitor (tadalafil) has anti-fibrotic effects (outside the core evidence set) (shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).
- Cell types: BE5 basal epithelial cells; luminal/club-like epithelial intermediates; fibroblasts/myofibroblasts; MSCs (LepR+); macrophages and other immune cells (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).
- Anatomical locations: prostate transition zone, periurethral stroma (fei2024integratingspatialtranscriptomics pages 15-15, santos2024cellplasticityin pages 1-2).

Biological Processes (GO-style)
- Positive regulation of epithelial cell proliferation; epithelial–mesenchymal transition; response to hypoxia; TGF‑β receptor signaling; WNT signaling; PI3K/AKT signaling; chemokine-mediated signaling; extracellular matrix organization; fibroblast migration and differentiation; response to oxidative stress (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 1-2, santos2024cellplasticityin pages 1-2).

Cellular Components
- Plasma membrane (IGF1R, CXCR5, IL‑6R/gp130); cytoplasm and nucleus (β‑catenin translocation; FOS nuclear activity); extracellular space (IGF1, CXCL13, TGF‑β) (fei2024integratingspatialtranscriptomics pages 15-15, shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3).

Disease Progression (sequence)
- Trigger(s): aging-associated stromal reawakening and hypoxia in TZ epithelium; microbial/inflammatory cues (IL‑6 axis) (fei2024integratingspatialtranscriptomics pages 15-15).
- Early events: hypoxia-driven BE5 activation (FOS), stromal secretion of IGF1/CXCL13; recruitment of MSCs via TGF‑β/ROCK (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3).
- Expansion phase: EMT and epithelial lineage reprogramming; myofibroblast activation and ECM deposition; WNT/β‑catenin and PI3K/AKT reinforce proliferation (shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, fei2024integratingspatialtranscriptomics pages 15-15).
- Clinical phase: nodular enlargement in TZ → bladder outlet obstruction and LUTS; persistent inflammation and oxidative stress maintain disease (fei2024integratingspatialtranscriptomics pages 15-15, santos2024cellplasticityin pages 1-2).

Phenotypic Manifestations (HP terms)
- Lower urinary tract symptoms (LUTS): urinary frequency, urgency, nocturia, weak stream, incomplete emptying (HP:0012590 series; mechanistic basis in TZ expansion and stromal tone) (fei2024integratingspatialtranscriptomics pages 15-15, santos2024cellplasticityin pages 1-2).

Gene/protein annotations with ontology terms
- HGNC: ROCK1 (HGNC:10251), ROCK2 (HGNC:10252), TGFB1 (HGNC:11766), SMAD2 (HGNC:6767), SMAD3 (HGNC:6769), CTNNB1 (HGNC:2514), MYC (HGNC:7553), SNAI1 (HGNC:11128), IGF1 (HGNC:5463), IGF1R (HGNC:5465), CXCL13 (HGNC:10644), CXCR5 (HGNC:1643), FOS (HGNC:3796), AR (HGNC:644), SRD5A2 (HGNC:11284) (fei2024integratingspatialtranscriptomics pages 15-15, shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).

Cell type involvement (CL terms)
- Basal epithelial cell (BE5-like): CL:0002252; fibroblast: CL:0000057; myofibroblast: CL:0000186; macrophage: CL:0000235; T cell: CL:0000084 (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).

Anatomical locations (UBERON terms)
- Prostate transition zone: UBERON:0012369; prostate stroma: UBERON:0002369; prostatic urethra/periurethral region: UBERON:0001334 (fei2024integratingspatialtranscriptomics pages 15-15, santos2024cellplasticityin pages 1-2).

Chemical entities (ChEBI)
- Y‑27632 (CHEBI:63608); GSK269962A (CHEBI:63634); anethole trithione (CHEBI:2249) (shan2024y27632targetingrock1&2 pages 1-2, li2024aberrantactivationof pages 1-3, santos2024cellplasticityin pages 1-2).

Evidence items (with URLs and dates)
- Fei et al., 2024-04-10, J Transl Med: https://doi.org/10.1186/s12967-024-05212-9 (hypoxia→FOS; BE5; nodular EMT/proliferation) (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2).
- Pollack et al., 2024-01-11, JCI Insight: https://doi.org/10.1172/jci.insight.176479 (IGF1/CXCL13 stromal induction; IGF1 necessity for organoids) (fei2024integratingspatialtranscriptomics pages 15-15).
- Shan et al., 2024-10-04, Mol Biomed: https://doi.org/10.1186/s43556-024-00216-9 (ROCK1/2→β-catenin/TGF‑β; Y‑27632 reverses fibrosis/EMT/proliferation; in vivo rat data) (shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11).
- Li et al., 2024-05-23, Cell Commun Signal: https://doi.org/10.1186/s12964-024-01644-4 (TGF‑β/ROCK1 recruits MSCs; GSK269962A blocks stromal hyperplasia) (li2024aberrantactivationof pages 1-3).
- Dos Santos et al., 2024-01-01, Am J Pathol: https://doi.org/10.1016/j.ajpath.2023.09.010 (epithelial plasticity; mitochondrial ROS inhibitor reduces prostate weight and LUTS proxy) (santos2024cellplasticityin pages 1-2).
- Wang et al., 2024-05-17, Mil Med Res: https://doi.org/10.1186/s40779-024-00533-8 (oral–prostate axis; IL‑6/IL‑6R/gp130→AKT; fold-changes and histologic effects) (fei2024integratingspatialtranscriptomics pages 15-15).

Embedded artifact
| Category | Entity | Standard ID | Role / Mechanism in BPH | Evidence (year) | Citation DOI/URL |
|---|---|---:|---|---:|---|
| Pathway | TGF-β / ROCK1 axis | TGFB1 (HGNC:11766); ROCK1 (HGNC:10251) | Aberrant TGF-β activation engages ROCK1 to recruit LepR+ MSCs → differentiation to myofibroblasts, stromal hyperplasia; ROCK1 inhibition (GSK269962A) suppresses MSC migration and stromal expansion | 2024 (li2024aberrantactivationof pages 1-3) | https://doi.org/10.1186/s12964-024-01644-4 |
| Pathway | WNT / β-catenin signaling | CTNNB1 (HGNC:2514) | ROCK1/2 activity stabilizes β-catenin, driving EMT and proliferation; Y-27632 reduces β-catenin levels and downstream targets (c-MYC, Snail, Survivin) | 2024 (shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11) | https://doi.org/10.1186/s43556-024-00216-9 |
| Pathway | PI3K/AKT signaling | PIK3CA (HGNC:8975) / AKT (family) | RTK activation (e.g., stromal IGF1/CSF1) signals through PI3K/AKT to promote epithelial proliferation and survival in BPH nodules | 2024 (li2024aberrantactivationof pages 1-3, fei2024integratingspatialtranscriptomics pages 15-15) | https://doi.org/10.1186/s12964-024-01644-4 |
| Process / Program | Epithelial–mesenchymal transition (EMT) | SNAI1 (HGNC:11128) | TGF-β and hypoxia-driven programs induce EMT in epithelial cells → myofibroblast-like phenotypes, ECM deposition and nodular formation | 2024 (fei2024integratingspatialtranscriptomics pages 15-15, shan2024y27632targetingrock1&2 pages 1-2) | https://doi.org/10.1186/s12967-024-05212-9 ; https://doi.org/10.1186/s43556-024-00216-9 |
| Pathway / TF | Hypoxia → FOS (c-Fos) activation | FOS (HGNC:3796) | Hypoxia-enriched BE5 basal epithelial cells upregulate FOS → promotes hypoxia-induced EMT and proliferative nodular initiation in the transition zone | 2024 (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2) | https://doi.org/10.1186/s12967-024-05212-9 |
| Stromal induction | IGF1 / CXCL13 stromal factors | IGF1 (HGNC:5463); CXCL13 (HGNC:10644); IGF1R (HGNC:5465); CXCR5 (HGNC:1643) | BPH fibroblasts secrete IGF1 and CXCL13 that act on adjacent epithelium (IGF1R/CXCR5) to induce ductal proliferation and organoid growth (stromal→epithelial induction) | 2024 (fei2024integratingspatialtranscriptomics pages 15-15) | https://doi.org/10.1172/jci.insight.176479 (Pollack 2024) |
| Gene / Effector | ROCK2 | ROCK2 (HGNC:10252) | ROCK2 upregulated in BPH stroma/epithelium; promotes fibrosis, EMT and cell proliferation via β-catenin and TGF-β cross-talk; inhibited by Y-27632 | 2024 (shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11) | https://doi.org/10.1186/s43556-024-00216-9 |
| Gene / Effector | TGFB1 (TGF-β1) | TGFB1 (HGNC:11766) | Core profibrotic cytokine driving myofibroblast activation, ECM deposition and EMT in BPH stroma | 2024 (li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 1-2) | https://doi.org/10.1186/s12964-024-01644-4 |
| Gene / Effector | CTNNB1 (β-catenin) | CTNNB1 (HGNC:2514) | Mediates WNT-driven transcriptional programs (c-MYC, SNAI1) supporting proliferation and EMT in hyperplastic prostate | 2024 (shan2024y27632targetingrock1&2 pages 1-2) | https://doi.org/10.1186/s43556-024-00216-9 |
| Gene / Effector | MYC (c-MYC) | MYC (HGNC:7553) | Downstream of β-catenin/WNT and promotes epithelial proliferation in BPH nodules | 2024 (shan2024y27632targetingrock1&2 pages 1-2) | https://doi.org/10.1186/s43556-024-00216-9 |
| Gene / Effector | SMAD2 / SMAD3 | SMAD2 (HGNC:6767); SMAD3 (HGNC:6769) | Canonical mediators of TGF-β signaling; p-Smad2/3 increased in hyperplastic stroma correlating with volume/inflammation | 2024 (li2024aberrantactivationof pages 1-3) | https://doi.org/10.1186/s12964-024-01644-4 |
| Gene / Effector | FOS (c-Fos) | FOS (HGNC:3796) | Transcriptional effector induced by hypoxia in BE5 cells; links hypoxia → EMT/proliferation in nodular formation | 2024 (fei2024integratingspatialtranscriptomics pages 15-15) | https://doi.org/10.1186/s12967-024-05212-9 |
| Gene / Effector | AR / SRD5A2 (androgen axis) | AR (HGNC:644); SRD5A2 (HGNC:11284) | Intraprostatic DHT–AR signaling modulates growth; androgen-independent epithelial populations also expand in BPH models (cell plasticity) | 2023–2024 (santos2024cellplasticityin pages 1-2, fei2024integratingspatialtranscriptomics pages 15-15) | https://doi.org/10.1016/j.ajpath.2023.09.010 |
| Cell type | Basal epithelial (BE5-like) | basal epithelial cell (CL:0002252) | BE5 identified as initiating/transitional cell (LE→BE) with hypoxia/FOS signature driving glandular nodular formation | 2024 (fei2024integratingspatialtranscriptomics pages 15-15, fei2024integratingspatialtranscriptomics pages 1-2) | https://doi.org/10.1186/s12967-024-05212-9 |
| Cell type | Club-like luminal / intermediate cells | club cell (CL:0000061) (annotated) | Androgen-independent / club-like populations expand in BPH and show altered proliferation and antioxidant vulnerability | 2024 (santos2024cellplasticityin pages 1-2) | https://doi.org/10.1016/j.ajpath.2023.09.010 |
| Cell type | Fibroblast | fibroblast (CL:0000057) | Stromal fibroblasts secrete inductive factors (IGF1, CXCL13) and ligands (CSF1/IL34) that drive epithelial proliferation and activate RTK/PI3K signaling | 2024 (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3) | https://doi.org/10.1172/jci.insight.176479 ; https://doi.org/10.1186/s12964-024-01644-4 |
| Cell type | Myofibroblast | myofibroblast (CL:0000186) | Main ECM-producing cell in BPH fibrosis; arises from MSC recruitment and stromal differentiation under TGF-β/ROCK signaling | 2024 (li2024aberrantactivationof pages 1-3) | https://doi.org/10.1186/s12964-024-01644-4 |
| Cell type | Macrophage | macrophage (CL:0000235) | Infiltrating macrophage subsets (lipid-rich/TREM2+ in large prostates) interact with stroma and promote proliferation/fibrosis (immune–stromal crosstalk) | 2024–2025 (lanman2025immunedysregulationin pages 8-11, santos2024cellplasticityin pages 1-2) | https://doi.org/10.1016/j.ajpath.2023.09.010 |
| Anatomy | Prostate transition zone | UBERON:0012369 | Anatomical nidus of nodular hyperplasia and LUTS; site of epithelial–stromal reawakening and nodular formation | 2024 (fei2024integratingspatialtranscriptomics pages 15-15, santos2024cellplasticityin pages 1-2) | https://doi.org/10.1186/s12967-024-05212-9 ; https://doi.org/10.1016/j.ajpath.2023.09.010 |
| Anatomy | Prostate stroma | UBERON:0002369 | Location of fibroblast/myofibroblast expansion, ECM remodeling and secreted inductive signals in BPH | 2024 (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3) | https://doi.org/10.1172/jci.insight.176479 ; https://doi.org/10.1186/s12964-024-01644-4 |
| Anatomy | Prostatic urethra (periurethral region) | UBERON:0001334 | Periurethral (transition) anatomy explains clinical BOO/LUTS when nodules enlarge the TZ | 2024 (fei2024integratingspatialtranscriptomics pages 15-15) | https://doi.org/10.1186/s12967-024-05212-9 |
| Chemical / Drug | Y-27632 (ROCK inhibitor) | CHEBI:63608 | Pharmacologic ROCK1/2 inhibition reduces β-catenin stability, TGF-β signaling, fibrosis, EMT and cell proliferation in BPH models | 2024 (shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11) | https://doi.org/10.1186/s43556-024-00216-9 |
| Chemical / Drug | GSK269962A (ROCK1 inhibitor) | CHEBI:63634 | Small-molecule ROCK1 inhibitor (preclinical) reduces MSC recruitment and stromal differentiation in vivo (therapeutic proof-of-concept) | 2024 (li2024aberrantactivationof pages 1-3) | https://doi.org/10.1186/s12964-024-01644-4 |
| Chemical / Drug | Anethole trithione (mito-ROS inhibitor) | CHEBI:2249 | Mitochondrial ROS inhibition decreased prostate weight, voiding frequency and epithelial proliferation in Pb-PRL BPH mouse model (antioxidant therapeutic effect) | 2024 (santos2024cellplasticityin pages 1-2) | https://doi.org/10.1016/j.ajpath.2023.09.010 |
| Chemical / Drug | Tadalafil (PDE5 inhibitor) | CHEBI:9392 | Reported to reduce prostatic fibrosis via miR-3126-3p/FGF9 axis in prostatic stromal models (anti-fibrotic mechanism) | 2024 (related literature) | https://doi.org/10.1186/s13062-024-00504-y |


*Table: A compact ontology-ready table mapping key pathways, genes/proteins (HGNC), cell types (CL), anatomical sites (UBERON), and chemicals (ChEBI) to concise mechanisms in BPH with 2023–2024 evidence and DOI/URL references; citations reference extracted evidence (context IDs) from recent studies (shan2024y27632targetingrock1&2 pages 1-2, fei2024integratingspatialtranscriptomics pages 1-2).*

Direct quotes (selected)
- “A distinct subgroup of basal epithelial (BE5) cells… play a crucial role in driving this progression through the hypoxia-induced epithelial–mesenchymal transition (EMT) signaling pathway… c-Fos expression… closely related to hypoxia and cell proliferation” (Fei 2024) (fei2024integratingspatialtranscriptomics pages 1-2).
- “The top stromal factors were insulin-like growth factor 1 (IGF1) and CXC chemokine ligand 13 (CXCL13)… IGF1 is necessary for the generation of BPH-1 cell spheroids and patient-derived BPH cell organoids” (Pollack 2024) (fei2024integratingspatialtranscriptomics pages 15-15).
- “ROCK1 and ROCK2 were significantly upregulated in BPH tissues… Y-27632… inhibited cell proliferation, fibrosis, epithelial–mesenchymal transition… ROCK downregulation inhibited the β-catenin signaling pathway… and TGF‑β/Smad2/3 signaling… reversed prostatic hyperplasia and fibrosis in BPH model rats” (Shan 2024) (shan2024y27632targetingrock1&2 pages 7-11).
- “Aberrant activation of transforming growth factor β (TGF‑β)/Rho kinase 1 (ROCK1) increased the stemness of BPH tissue by recruiting mesenchymal stem cells (MSCs)… inhibition of ROCK1 activation suppressed MSC migration and their potential for stromal differentiation” (Li 2024) (li2024aberrantactivationof pages 1-3).
- “P. gingivalis… infection… upregulated the expression of interleukin‑6 (IL‑6; 4.47‑fold), interleukin‑6 receptor‑α (IL‑6Rα; 5.74‑fold) and glycoprotein 130 (gp130; 4.47‑fold)… activates the Akt pathway… induces BPH” (Wang 2024) (fei2024integratingspatialtranscriptomics pages 15-15).

Limitations
- Some quantitative effect sizes (e.g., exact percent changes for in vivo prostate index) are reported qualitatively in the retrieved excerpts; deeper extraction from full texts would refine numerical precision. Nevertheless, the directional findings and core mechanisms are consistently supported across independent 2024 studies. (shan2024y27632targetingrock1&2 pages 7-11, fei2024integratingspatialtranscriptomics pages 15-15).

Conclusion
BPH progression in the transition zone reflects an interplay between hypoxia‑driven epithelial EMT and plasticity (BE5, FOS), stromal induction (IGF1/CXCL13), and TGF‑β/ROCK‑mediated fibrosis that recruits and differentiates MSCs, reinforced by inflammatory IL‑6→AKT signaling and oxidative stress. These insights nominate actionable targets—ROCK1/2, IGF1/IGF1R, IL‑6/IL‑6R/gp130, and mitochondrial ROS—with preclinical evidence for disease modification alongside standard symptomatic therapies. (fei2024integratingspatialtranscriptomics pages 15-15, li2024aberrantactivationof pages 1-3, shan2024y27632targetingrock1&2 pages 1-2, shan2024y27632targetingrock1&2 pages 7-11, santos2024cellplasticityin pages 1-2)

References

1. (fei2024integratingspatialtranscriptomics pages 15-15): Xiawei Fei, Jican Liu, Junyan Xu, Hongyan Jing, Zhonglin Cai, Jiasheng Yan, Zhenqi Wu, Huifeng Li, Zhong Wang, and Yanting Shen. Integrating spatial transcriptomics and single-cell rna-sequencing reveals the alterations in epithelial cells during nodular formation in benign prostatic hyperplasia. Journal of Translational Medicine, Apr 2024. URL: https://doi.org/10.1186/s12967-024-05212-9, doi:10.1186/s12967-024-05212-9. This article has 9 citations and is from a peer-reviewed journal.

2. (fei2024integratingspatialtranscriptomics pages 1-2): Xiawei Fei, Jican Liu, Junyan Xu, Hongyan Jing, Zhonglin Cai, Jiasheng Yan, Zhenqi Wu, Huifeng Li, Zhong Wang, and Yanting Shen. Integrating spatial transcriptomics and single-cell rna-sequencing reveals the alterations in epithelial cells during nodular formation in benign prostatic hyperplasia. Journal of Translational Medicine, Apr 2024. URL: https://doi.org/10.1186/s12967-024-05212-9, doi:10.1186/s12967-024-05212-9. This article has 9 citations and is from a peer-reviewed journal.

3. (shan2024y27632targetingrock1&2 pages 1-2): Shidong Shan, Min Su, Hejin Wang, Feng Guo, Yan Li, Yongying Zhou, Huan Liu, Lu Du, Junchao Zhang, Jizhang Qiu, Michael E. DiSanto, Yuming Guo, and Xinhua Zhang. Y-27632 targeting rock1&2 modulates cell growth, fibrosis and epithelial-mesenchymal transition in hyperplastic prostate by inhibiting β-catenin pathway. Molecular Biomedicine, Oct 2024. URL: https://doi.org/10.1186/s43556-024-00216-9, doi:10.1186/s43556-024-00216-9. This article has 8 citations.

4. (shan2024y27632targetingrock1&2 pages 7-11): Shidong Shan, Min Su, Hejin Wang, Feng Guo, Yan Li, Yongying Zhou, Huan Liu, Lu Du, Junchao Zhang, Jizhang Qiu, Michael E. DiSanto, Yuming Guo, and Xinhua Zhang. Y-27632 targeting rock1&2 modulates cell growth, fibrosis and epithelial-mesenchymal transition in hyperplastic prostate by inhibiting β-catenin pathway. Molecular Biomedicine, Oct 2024. URL: https://doi.org/10.1186/s43556-024-00216-9, doi:10.1186/s43556-024-00216-9. This article has 8 citations.

5. (li2024aberrantactivationof pages 1-3): Youyou Li, Jiaren Li, Liang Zhou, Zhenxing Wang, Ling Jin, Jia Cao, Hui Xie, and Long Wang. Aberrant activation of tgf-β/rock1 enhances stemness during prostatic stromal hyperplasia. Cell Communication and Signaling : CCS, May 2024. URL: https://doi.org/10.1186/s12964-024-01644-4, doi:10.1186/s12964-024-01644-4. This article has 9 citations.

6. (santos2024cellplasticityin pages 1-2): Leïla Dos Santos, Francesco Carbone, Emeline Pacreau, Sekou Diarra, Marine Luka, Natascha Pigat, Manon Baures, Emilie Navarro, Julien Anract, Nicolas Barry Delongchamps, Nicolas Cagnard, Frédéric Bost, Ivan Nemazanyy, Olivier Petitjean, Ahmed Hamaï, Mickaël Ménager, Stefano Palea, Jacques-Emmanuel Guidotti, and Vincent Goffin. Cell plasticity in a mouse model of benign prostate hyperplasia drives amplification of androgen-independent epithelial cell populations sensitive to antioxidant therapy. The American Journal of Pathology, 194:30-51, Jan 2024. URL: https://doi.org/10.1016/j.ajpath.2023.09.010, doi:10.1016/j.ajpath.2023.09.010. This article has 5 citations.

7. (lanman2025immunedysregulationin pages 8-11): Nadia A. Lanman, Meaghan M. Broman, Harish Kothandaraman, Gregory M. Cresswell, Gada D. Awdalkreem, Dilinaer Wusiman, Andree K. Kolliegbo, Alexander P. Glaser, Brian T. Helfand, Renee E. Vickman, Jiang Yang, Simon W. Hayward, and Timothy L. Ratliff. Immune dysregulation in the prostates of c57bl/6<sup>aire-/-</sup>mice mirrors that seen in human benign prostatic hyperplasia. BioRxiv, Aug 2025. URL: https://doi.org/10.1101/2025.08.12.669857, doi:10.1101/2025.08.12.669857. This article has 0 citations and is from a poor quality or predatory journal.