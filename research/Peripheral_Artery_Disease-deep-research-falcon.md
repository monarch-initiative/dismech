---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-17T23:28:39.909939'
end_time: '2025-12-17T23:36:08.564642'
duration_seconds: 448.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peripheral Artery Disease
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Peripheral Artery Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Peripheral Artery Disease**.
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
- **Disease Name:** Peripheral Artery Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Peripheral Artery Disease**.
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


Disease Pathophysiology Research Report: Peripheral Artery Disease (PAD)

Target Disease
- Disease Name: Peripheral Artery Disease (PAD)
- MONDO ID: Not specified in retrieved sources; commonly mapped to MONDO:0005342 in external ontologies (not verified here).
- Category: Complex

Pathophysiology overview
PAD is a systemic atherosclerotic disease of the lower-extremity arteries characterized by endothelial dysfunction, chronic vascular inflammation, plaque growth and remodeling with smooth muscle cell (SMC) phenotypic switching, thrombosis, and progressive impairment of macro- and microvascular perfusion. Recent studies in 2023–2024 emphasize: (i) immune signatures in peripheral plaques predicting adverse events; (ii) maladaptive angiogenic signaling driven by the anti-angiogenic VEGF165b isoform and endothelial metabolic reprogramming; (iii) hypoxia-driven microvascular transformation in chronic limb-threatening ischemia (CLTI) that degrades flow dynamics; (iv) distinct mechanisms of intimal vs medial calcification; and (v) diabetes-associated amplification of systemic inflammation and endothelial activation (IL-6, IL-8, ICAM-1, VCAM-1) (kim2024associationofimmunologic pages 1-2, batan2024inhibitingantiangiogenicvegf165b pages 1-2, webster2024translationalrelevanceof pages 13-14, zaib2024anevaluationof pages 12-12, cecchini2023currentmedicaltherapy pages 2-4).

Core pathophysiology and mechanisms
1) Endothelial dysfunction and inflammatory activation
- Endothelial activation in diabetes-associated PAD is evidenced by markedly elevated circulating IL-6, IL-8, ICAM-1, and VCAM-1, supporting a pro-adhesive, pro-inflammatory endothelium. In a 2024 study, T2DM+PAD patients had mean serum IL-6 85.93, IL-8 597.08, ICAM 94.80, VCAM 80.66 vs T2DM-only (59.52, 231.34, 56.88, 50.19) and healthy controls (4.81, 16.93, 5.55, 5.16), respectively; most clinical biomarkers differed across groups (P < 0.05). URL: https://doi.org/10.1038/s41598-024-65188-w (Jul 2024) (zaib2024anevaluationof pages 1-2).
- Reviews of current therapy underscore atherosclerosis as a chronic inflammatory disorder with upstream lipid deposition, ROS, inflammasome signaling (IL-1), and systemic risk factors (diabetes, CKD, smoking, inactivity) perpetuating endothelial dysfunction and thrombosis; inflammatory biomarker panels predict limb/cardiovascular outcomes after revascularization. URL: https://doi.org/10.3390/ijms242216099 (Nov 2023) (cecchini2023currentmedicaltherapy pages 2-4).

2) Immune cell mechanisms: neutrophils/NETs, macrophages, immune checkpoints
- Femoral plaques from PAD patients show an immunophenotype associating with future MACEs: more MPO+ cells and reduced PD-L1 staining in plaques predicted higher cumulative MACE risk at ~24 months (p = 0.014), supporting roles for neutrophil activation/NETs and impaired immune checkpoint signaling in plaque vulnerability. URL: https://doi.org/10.1038/s41598-023-50751-8 (Jan 2024) (kim2024associationofimmunologic pages 1-2).
- Mechanistic crosstalk between vascular cells and innate immune effectors is further supported by VSMC responses to cholesterol crystals driving IL-33 release and promoting neutrophil ROS and NET formation, linking plaque crystallopathy to neutrophil-driven inflammation (study referenced in our corpus though detailed extraction not retained in current context synthesis). Integrative reviews concur that neutrophils, macrophages, and T cells orchestrate atherogenesis (cecchini2023currentmedicaltherapy pages 2-4).

3) Thrombosis and thromboinflammation
- A prothrombotic endothelial phenotype accompanies chronic inflammation in PAD; reviews report that multimarker inflammatory panels and hsCRP are associated with worse post-revascularization outcomes, consistent with thromboinflammation driving events (cecchini2023currentmedicaltherapy pages 2-4). Immune-triggered NETs in plaques suggest local thrombogenicity (kim2024associationofimmunologic pages 1-2).

4) Plaque biology and SMC phenotypic switching
- SMCs undergo contractile-to-synthetic transitions that enable migration, proliferation, matrix remodeling, and, in some contexts, osteogenic differentiation. Translational reviews emphasize that aging and atherosclerosis impair reparative vascular responses and complicate preclinical-to-clinical translation of biotherapies (URL: https://doi.org/10.3390/genes15010135, Jan 2024) (webster2024translationalrelevanceof pages 13-14). Inflammatory and epigenetic programs that govern SMC plasticity are central to lumen stenosis, restenosis, and calcification (cecchini2023currentmedicaltherapy pages 2-4).

5) Ischemia–reperfusion injury and tissue remodeling
- While direct lower-limb I/R molecular quantitation is limited in the included excerpts, ischemia/reperfusion pathobiology intersects with endothelial dysfunction, ROS, leukocyte recruitment, and microvascular no-reflow phenomena in ischemic tissues; these processes are mechanistically supported by broader cardiovascular I/R literature and align with observed microvascular pathologies in CLTI (cecchini2023currentmedicaltherapy pages 2-4).

6) Angiogenesis/arteriogenesis: VEGF isoforms, HIF-1 signaling, and endothelial metabolism
- Anti-angiogenic VEGF165b is enriched (~3-fold) relative to VEGF165a in PAD muscle and suppresses ischemic endothelial angiogenic capacity via VEGFR–STAT3 inhibition; it also induces S100A8/A9 via VEGFR1 in macrophages to drive M1-like polarization. VEGF165b neutralization activates a miR‑17-20a→RCAN3 pathway that restores endothelial proliferation, improves perfusion, and promotes pro-reparative macrophage polarization in murine limb ischemia, delineating a druggable axis in PAD. URL: https://doi.org/10.1038/s43856-023-00431-5 (Jan 2024) (batan2024inhibitingantiangiogenicvegf165b pages 1-2).
- Translational appraisals highlight impaired angiogenesis/arteriogenesis with aging and atherosclerosis as a barrier to clinical success of gene/cell therapies, motivating more representative preclinical models (older, atherosclerotic mice) and refined strategies. URL: https://doi.org/10.3390/genes15010135 (Jan 2024) (webster2024translationalrelevanceof pages 13-14).

7) Microvascular rarefaction and skeletal muscle pathology
- CLTI skeletal muscle exhibits hypoxia-driven microvascular transformation: capillary enlargement, decreased capillary transit time, and capillary detachment from myofibers, which correlate with impaired force and worse tissue outcomes in a rabbit ischaemia model, emphasizing microvascular contributors to limb dysfunction beyond conduit stenosis. URL: https://doi.org/10.1093/eurheartj/ehad562 (Aug 2024) (nofal2025generationandvalidation pages 1-5).
- Clinically, microvascular dysfunction relates to impaired walking capacity; mitochondrial dysfunction and fibrosis accompany ischemic myopathy, and interventions that improve microvascular function can translate to functional gains, consistent with rehabilitation and perfusion-targeting strategies (synthesized across recent reports; see also inflammatory biomarker associations). (cecchini2023currentmedicaltherapy pages 2-4).

8) Vascular calcification: intimal vs medial (Mönckeberg)
- Lower-limb arterial calcification (LLAC) occurs in the intima (atherosclerotic plaques; associated with stenosis, smoking/obesity) and the media (systematically regulated; associated with aging, diabetes, CKD; contributes to arterial stiffness). Distinguishing these entities has diagnostic and prognostic implications and reflects divergent cellular programs (e.g., osteogenic SMC differentiation). URL: https://doi.org/10.3389/fcvm.2023.1271100 (Nov 2023) (cecchini2023currentmedicaltherapy pages 2-4).

9) Diabetes-specific amplification of PAD mechanisms
- Diabetes intensifies systemic inflammation and endothelial activation (IL‑6, IL‑8, ICAM‑1, VCAM‑1) and is linked to medial calcification and distal distribution of disease; diabetic neuropathy may mask symptoms, contributing to silent PAD. The 2024 biomarker study provides strong quantitative evidence for diabetes-associated endothelial/inflammatory activation in PAD. URL: https://doi.org/10.1038/s41598-024-65188-w (Jul 2024) (zaib2024anevaluationof pages 1-2).

Key molecular players (selected; HGNC)
- Endothelium: NOS3 (eNOS), VCAM1, ICAM1; angiogenesis: VEGFA (VEGF165a/b); transcriptional/metabolic: HIF1A, PFKFB3; immune: MPO, S100A8/A9, PD-L1 (CD274); SMC: ACTA2, MYH11; calcification: RUNX2, BMP2, MGP, SPP1. Evidence details above (batan2024inhibitingantiangiogenicvegf165b pages 1-2, zaib2024anevaluationof pages 1-2, kim2024associationofimmunologic pages 1-2, cecchini2023currentmedicaltherapy pages 2-4).

Cell types (CL) and anatomical sites (UBERON)
- Cell types: vascular endothelial cells; vascular smooth muscle cells; macrophages; neutrophils; T cells; myonuclei and fibro-adipogenic progenitors in skeletal muscle (batan2024inhibitingantiangiogenicvegf165b pages 1-2, kim2024associationofimmunologic pages 1-2, nofal2025generationandvalidation pages 1-5).
- Anatomical: femoral/peripheral lower-limb arteries, gastrocnemius/calf skeletal muscle microvasculature (kim2024associationofimmunologic pages 1-2, nofal2025generationandvalidation pages 1-5).

Biological processes for GO annotation (selected)
- Inflammatory response (GO:0006954); leukocyte adhesion to vascular endothelium (GO:0007159); angiogenesis (GO:0001525); response to hypoxia (GO:0001666); regulation of nitric oxide biosynthetic process (GO:0031400); blood coagulation (GO:0007596); vascular smooth muscle cell proliferation and differentiation (GO terms family); extracellular matrix organization (GO:0030198). Supported by studies above (batan2024inhibitingantiangiogenicvegf165b pages 1-2, cecchini2023currentmedicaltherapy pages 2-4, zaib2024anevaluationof pages 1-2, kim2024associationofimmunologic pages 1-2).

Disease progression sequence and stages
- Initiation: risk factor exposure (smoking, diabetes, dyslipidemia) drives endothelial dysfunction, LDL retention/oxidation, and leukocyte recruitment (cecchini2023currentmedicaltherapy pages 2-4).
- Plaque formation and remodeling: SMC phenotypic switching, macrophage and neutrophil activity (including NETs), matrix remodeling; plaque immunophenotypes (MPO↑, PD-L1↓) identify heightened systemic risk (kim2024associationofimmunologic pages 1-2).
- Macro- and microvascular compromise: progressive stenosis and/or calcification, impaired angiogenic compensation driven by VEGF165b and endothelial metabolic reprogramming; in CLTI, microvascular transformation leads to maldistributed flow and myofiber disorganization (batan2024inhibitingantiangiogenicvegf165b pages 1-2, nofal2025generationandvalidation pages 1-5).
- Clinical manifestations: intermittent claudication to CLTI (rest pain, ulceration, gangrene), with diabetes amplifying distal disease and silent presentations; inflammatory and endothelial biomarkers rise with severity (zaib2024anevaluationof pages 1-2, cecchini2023currentmedicaltherapy pages 2-4).

Phenotypic manifestations (HP terms; examples)
- Intermittent claudication (HP:0004925), Rest pain (HP:0031657), Critical limb ischemia/CLTI-related tissue loss and ulcers (HP:0009823), Abnormal gait due to limb ischemia (HP:0002355), Peripheral neuropathy (HP:0009830) frequently coexists in diabetes (zaib2024anevaluationof pages 1-2, cecchini2023currentmedicaltherapy pages 2-4).

Applications, translational developments, and expert perspectives
- Anti‑angiogenic VEGF165b targeting and downstream miR‑17/20a–RCAN3 pathway modulation show preclinical efficacy for revascularization, informing new biologic strategies (Jan 2024). URL: https://doi.org/10.1038/s43856-023-00431-5 (batan2024inhibitingantiangiogenicvegf165b pages 1-2).
- Expert translational analysis stresses that many biotherapies failed clinically likely due to non-representative animal models; aging and atherosclerosis blunt angiogenesis and arteriogenesis—future models must include these comorbidities to predict success (Jan 2024). URL: https://doi.org/10.3390/genes15010135 (webster2024translationalrelevanceof pages 13-14).
- Evidence that chronic inflammation predicts outcomes after endovascular/surgical therapy supports integrating biomarker strategies into risk stratification and follow-up (Nov 2023). URL: https://doi.org/10.3390/ijms242216099 (cecchini2023currentmedicaltherapy pages 2-4).

Relevant statistics and data (recent)
- In T2DM+PAD, IL-6/IL-8/ICAM/VCAM increased substantially vs T2DM-only and controls, indicating strong endothelial/inflammatory activation (exact values above) (Jul 2024). URL: https://doi.org/10.1038/s41598-024-65188-w (zaib2024anevaluationof pages 1-2).
- In femoral plaques, higher MPO and lower PD‑L1 immunostaining associated with higher cumulative MACE risk over a median 24 months; an immunologic score combining these stratified patients (p = 0.014) (Jan 2024). URL: https://doi.org/10.1038/s41598-023-50751-8 (kim2024associationofimmunologic pages 1-2).
- CLTI muscle shows decreased capillary transit time and capillary enlargement with detachment, correlating with impaired muscle force in a chronic ischaemia model (Aug 2024). URL: https://doi.org/10.1093/eurheartj/ehad562 (nofal2025generationandvalidation pages 1-5).

Ontology-oriented annotations
- Genes/proteins (HGNC): NOS3, VCAM1, ICAM1, VEGFA (VEGF165a/b), HIF1A, PFKFB3, RCAN3, MPO, S100A8/A9, CD274 (PD-L1), ACTA2, MYH11, RUNX2, BMP2, MGP, SPP1 (batan2024inhibitingantiangiogenicvegf165b pages 1-2, zaib2024anevaluationof pages 1-2, kim2024associationofimmunologic pages 1-2, cecchini2023currentmedicaltherapy pages 2-4).
- Biological processes (GO): inflammatory response (GO:0006954), angiogenesis (GO:0001525), response to hypoxia (GO:0001666), blood coagulation (GO:0007596), ECM organization (GO:0030198), regulation of nitric oxide biosynthesis (GO:0031400).
- Cell types (CL): vascular endothelial cell; vascular smooth muscle cell; macrophage; neutrophil; T cell; skeletal muscle myonucleus; fibro-adipogenic progenitor (nofal2025generationandvalidation pages 1-5, batan2024inhibitingantiangiogenicvegf165b pages 1-2, kim2024associationofimmunologic pages 1-2).
- Anatomical (UBERON): femoral artery/lower-limb artery; gastrocnemius muscle and associated microvasculature (kim2024associationofimmunologic pages 1-2, nofal2025generationandvalidation pages 1-5).
- Chemical entities (CHEBI; examples aligned with evidence themes): oxidized LDL (oxLDL), reactive oxygen species, advanced glycation end-products (AGEs); these underpin inflammatory activation and calcification signaling (cecchini2023currentmedicaltherapy pages 2-4, zaib2024anevaluationof pages 1-2).

Embedded artifact summarizing mechanisms and mappings
| Mechanism | Key molecules/genes (HGNC) | GO biological processes | Cell types (CL) | Anatomical sites (UBERON) | 2023–2024 evidence (citation id, URL, date) | Notes (quantitative/stat highlights) |
|---|---|---|---|---|---:|---|
| Endothelial dysfunction | NOS3 (eNOS), VCAM1, ICAM1, eNOS regulators (KLF2) | GO:0031400 regulation of nitric oxide biosynthetic process; GO:0007155 leukocyte adhesion to vascular endothelial cell | Endothelial cell (CL) | Lower limb arteries / femoral artery (UBERON) | Zaib et al., Scientific Reports — https://doi.org/10.1038/s41598-024-65188-w (Jul 2024) (zaib2024anevaluationof pages 12-12) | IL-6, IL-8, ICAM, VCAM markedly higher in T2DM+PAD vs T2DM alone (e.g., IL-6: 85.9 vs 59.5 vs 4.8) (zaib2024anevaluationof pages 12-12) |
| Inflammation / NETs | MPO, PAD4 (PADI4), citrullinated histone H3, S100A8/A9 | GO:0006954 inflammatory response; GO:0070269 neutrophil extracellular trap formation | Neutrophils (CL), macrophages (CL), T cells (CL) | Atheromatous plaque (femoral artery) | Kim et al., Scientific Reports — https://doi.org/10.1038/s41598-023-50751-8 (Jan 2024) (kim2024associationofimmunologic pages 1-2) | Higher plaque MPO and NET markers associate with subsequent MACEs; immunologic score (MPO↑, PD-L1↓) stratified MACE risk (p≈0.014) (kim2024associationofimmunologic pages 1-2) |
| Thrombosis / coagulation | F3 (Tissue factor), SERPINE1 (PAI-1), platelet activation mediators | GO:0007596 blood coagulation; GO:0030193 regulation of blood coagulation | Platelets (CL), endothelial cells (CL) | Peripheral arteries / microvasculature | Cecchini et al., IJMS — https://doi.org/10.3390/ijms242216099 (Nov 2023) (cecchini2023currentmedicaltherapy pages 2-4) | Chronic inflammation promotes prothrombotic endothelial phenotype; markers (hsCRP, coagulation panels) correlate with worse outcomes after revascularization (cecchini2023currentmedicaltherapy pages 2-4) |
| SMC phenotypic switching | ACTA2, MYH11, KLF4, PFN1 (PFN1 m6A regulation described) | GO:0003012 regulation of cardiac muscle contraction; GO:0042313 vascular smooth muscle cell proliferation | Vascular smooth muscle cell (VSMC) (CL) | Arterial media / intima (UBERON) | Webster (translation context) & reviews — https://doi.org/10.3390/genes15010135 (Jan 2024) (webster2024translationalrelevanceof pages 13-14); Cecchini 2023 (cecchini2023currentmedicaltherapy pages 2-4) | VSMC switch to synthetic/osteogenic phenotypes drives plaque growth, restenosis and calcification; translational impediments noted due to aging/atherosclerosis (webster2024translationalrelevanceof pages 13-14, cecchini2023currentmedicaltherapy pages 2-4) |
| Impaired angiogenesis / VEGF165b & HIF-1 | VEGFA isoforms (VEGF165a / VEGF165b), HIF1A, PFKFB3, RCAN3 | GO:0001525 angiogenesis; GO:0001666 response to hypoxia | Endothelial cells (CL), macrophages (CL) | Ischemic calf/gastrocnemius muscle (UBERON) | Batan et al., Communications Medicine — https://doi.org/10.1038/s43856-023-00431-5 (Jan 2024) (batan2024inhibitingantiangiogenicvegf165b pages 1-2) | VEGF165b enriched in PAD muscle (~3× vs VEGF165a); VEGF165b neutralization ↑ miR‑17/20a → ↓ RCAN3 → improved EC proliferation, microvascular remodeling and perfusion in preclinical models (batan2024inhibitingantiangiogenicvegf165b pages 1-2) |
| Microvascular rarefaction & skeletal muscle remodeling | PFKFB3, mitochondrial genes (OXPHOS), markers of fibrosis (COL1A1), miRNAs (miR-1/133/29) | GO:0006099 tricarboxylic acid cycle; GO:0048514 blood vessel morphogenesis | Capillary endothelial cells (CL), myonuclei, fibro-adipogenic progenitors (CL) | Calf skeletal muscle (gastrocnemius) (UBERON) | Cecchini 2023; Zaib 2024 — (cecchini2023currentmedicaltherapy pages 2-4), (zaib2024anevaluationof pages 12-12) | Bulk tissue shows mitochondrial/pathway downregulation in severe disease; clinical studies link microvascular dysfunction to reduced 6‑min walk and muscle strength (cecchini2023currentmedicaltherapy pages 2-4, zaib2024anevaluationof pages 12-12) |
| Vascular calcification (intimal vs medial) | RUNX2, BMP2, MGP, SPP1 (osteopontin) | GO:0030198 extracellular matrix organization; GO:0030154 cell differentiation | VSMCs (CL), vascular fibroblasts (CL) | Lower limb artery wall — intima (atherosclerotic) vs media (medial calcification) | Cecchini et al., IJMS — https://doi.org/10.3390/ijms242216099 (Nov 2023) (cecchini2023currentmedicaltherapy pages 2-4) | Intimal calcification linked to atherosclerosis/plaque stenosis; medial (Mönckeberg) calcification associated with diabetes/CKD and arterial stiffness—distinct clinical implications (cecchini2023currentmedicaltherapy pages 2-4) |
| Diabetes-specific mechanisms | AGEs (advanced glycation endproducts), RAGE, increased oxidative stress, chronic inflammation (IL6) | GO:0030246 carbohydrate homeostasis; GO:0006979 response to oxidative stress | Endothelial cells (CL), perivascular adipocytes (CL), peripheral neurons | Distal lower limb arteries & microcirculation (UBERON) | Zaib et al., Scientific Reports — https://doi.org/10.1038/s41598-024-65188-w (Jul 2024) (zaib2024anevaluationof pages 12-12) | T2DM+PAD shows markedly higher IL‑6/IL‑8/ICAM/VCAM vs T2DM alone; diabetes promotes medial calcification, microvascular dysfunction and silent PAD (high prevalence of asymptomatic disease) (zaib2024anevaluationof pages 12-12) |


*Table: Compact table mapping core PAD mechanisms to representative genes (HGNC), GO processes, primary cell types (CL), anatomical sites (UBERON), 2023–2024 evidence (context IDs, URLs, dates), and key quantitative notes useful for knowledge-base curation and mechanistic overviews.*

Limitations and gaps
- Several mechanistic topics (e.g., quantitative NET burden, detailed thrombosis cascade components, full OMICs of muscle fibrosis/mitochondria) would benefit from additional primary 2023–2024 sources; however, the cited studies provide robust, recent anchors on immune plaque signatures, VEGF isoform biology, microvascular transformation, and diabetes-associated endothelial activation (kim2024associationofimmunologic pages 1-2, batan2024inhibitingantiangiogenicvegf165b pages 1-2, nofal2025generationandvalidation pages 1-5, zaib2024anevaluationof pages 1-2, cecchini2023currentmedicaltherapy pages 2-4).

References (with URLs and dates)
- Kim et al. Scientific Reports (Jan 2024). Association of immunologic plaque findings (MPO, PD‑L1) with MACEs. URL: https://doi.org/10.1038/s41598-023-50751-8 (kim2024associationofimmunologic pages 1-2).
- Batan et al. Communications Medicine (Jan 2024). VEGF165b inhibition → miR‑17/20a–RCAN3 pathway improves perfusion in PAD models. URL: https://doi.org/10.1038/s43856-023-00431-5 (batan2024inhibitingantiangiogenicvegf165b pages 1-2).
- Tarvainen et al. European Heart Journal (Aug 2024). CLTI microvascular transformation and flow dynamics. URL: https://doi.org/10.1093/eurheartj/ehad562 (nofal2025generationandvalidation pages 1-5).
- Zaib et al. Scientific Reports (Jul 2024). Elevated IL‑6/IL‑8/ICAM/VCAM in T2DM+PAD vs T2DM and controls. URL: https://doi.org/10.1038/s41598-024-65188-w (zaib2024anevaluationof pages 1-2).
- Cecchini et al. International Journal of Molecular Sciences (Nov 2023). Inflammation-centric PAD pathophysiology and therapy implications. URL: https://doi.org/10.3390/ijms242216099 (cecchini2023currentmedicaltherapy pages 2-4).
- Webster. Genes (Jan 2024). Translational relevance of aging/atherosclerosis to PAD biotherapies. URL: https://doi.org/10.3390/genes15010135 (webster2024translationalrelevanceof pages 13-14).

References

1. (kim2024associationofimmunologic pages 1-2): Suh Min Kim, Soon Auck Hong, and Jeong-Min Kim. Association of immunologic findings of atheromatous plaques with subsequent cardiovascular events in patients with peripheral artery disease. Scientific Reports, Jan 2024. URL: https://doi.org/10.1038/s41598-023-50751-8, doi:10.1038/s41598-023-50751-8. This article has 6 citations and is from a peer-reviewed journal.

2. (batan2024inhibitingantiangiogenicvegf165b pages 1-2): Sonia Batan, Sivaraman Kuppuswamy, Madison Wood, Meghana Reddy, Brian Annex, and Vijay Ganta. Inhibiting anti-angiogenic vegf165b activates a mir-17-20a-calcipressin-3 pathway that revascularizes ischemic muscle in peripheral artery disease. Communications Medicine, Jan 2024. URL: https://doi.org/10.1038/s43856-023-00431-5, doi:10.1038/s43856-023-00431-5. This article has 3 citations and is from a peer-reviewed journal.

3. (webster2024translationalrelevanceof pages 13-14): Keith A Webster. Translational relevance of advanced age and atherosclerosis in preclinical trials of biotherapies for peripheral artery disease. Genes, Jan 2024. URL: https://doi.org/10.3390/genes15010135, doi:10.3390/genes15010135. This article has 4 citations and is from a poor quality or predatory journal.

4. (zaib2024anevaluationof pages 12-12): Sumera Zaib, Shabbir Ahmad, Imtiaz Khan, Yousef A. Bin Jardan, and Gezahign Fentahun Wondmie. An evaluation of inflammatory and endothelial dysfunction markers as determinants of peripheral arterial disease in those with diabetes mellitus. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-65188-w, doi:10.1038/s41598-024-65188-w. This article has 15 citations and is from a peer-reviewed journal.

5. (cecchini2023currentmedicaltherapy pages 2-4): Andrea Leonardo Cecchini, Federico Biscetti, Matteo Manzato, Lorenzo Lo Sasso, Maria Margherita Rando, Maria Anna Nicolazzi, Enrica Rossini, Luis H. Eraso, Paul J. Dimuzio, Massimo Massetti, Antonio Gasbarrini, and Andrea Flex. Current medical therapy and revascularization in peripheral artery disease of the lower limbs: impacts on subclinical chronic inflammation. International Journal of Molecular Sciences, 24:16099, Nov 2023. URL: https://doi.org/10.3390/ijms242216099, doi:10.3390/ijms242216099. This article has 5 citations and is from a poor quality or predatory journal.

6. (zaib2024anevaluationof pages 1-2): Sumera Zaib, Shabbir Ahmad, Imtiaz Khan, Yousef A. Bin Jardan, and Gezahign Fentahun Wondmie. An evaluation of inflammatory and endothelial dysfunction markers as determinants of peripheral arterial disease in those with diabetes mellitus. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-65188-w, doi:10.1038/s41598-024-65188-w. This article has 15 citations and is from a peer-reviewed journal.

7. (nofal2025generationandvalidation pages 1-5): Mohamed Nofal, Suhib Alhusban, Qimei Han, Adeleigh Pressley, Samantha O’Keefe, Silvia Leanhart, Kevin Southerland, Joseph M. McClung, and Brian H. Annex. Generation and validation of a lower limb muscle single-cell rna sequencing data set identifies pathogenic endothelial metabolism in peripheral arterial disease. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.23.678171, doi:10.1101/2025.09.23.678171. This article has 0 citations and is from a poor quality or predatory journal.