---
provider: openai
model: gpt-5
cached: false
start_time: '2026-04-11T22:12:13.563037'
end_time: '2026-04-11T22:16:21.205720'
duration_seconds: 247.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chordoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    top_p: 1.0
citation_count: 93
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Chordoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Chordoma**.
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

Disease Pathophysiology Research Report: Chordoma

Target Disease
- Disease Name: Chordoma
- MONDO ID: MONDO:0002894 (spinal chordoma; closest specific MONDO entry identified); Disease Ontology DOID:3302 (chordoma)
- Category: Cancer (primary malignant bone tumor of the axial skeleton; notochordal origin)

Pathophysiology description (current understanding)
Chordoma is a malignant tumor arising from embryonic notochordal remnants along the skull base and spine. Tumor identity and survival are tightly coupled to persistent, high-level expression of the T-box transcription factor brachyury (TBXT), which is a lineage-defining dependency driven by enhancer/super‑enhancer programs and specific epigenetic states in chordoma cells. Somatic TBXT (T) focal duplications occur in a substantial subset of sporadic cases and germline duplications of TBXT cause hereditary chordoma; a common TBXT missense variant (rs2305089) confers sporadic risk in several populations. Downstream, multiple cooperating oncogenic circuits contribute to progression: constitutive activation of RTK signaling (PDGFR/EGFR) and the PI3K–AKT–mTOR axis; loss of cell‑cycle restraint via recurrent CDKN2A/B deletion; chromatin remodeling defects (including SMARCB1 loss in poorly differentiated chordoma) that reshape enhancer landscapes and reinforce TBXT programs; and acquired defects in homologous recombination (HR) DNA repair in advanced disease. Recent proteogenomic and single‑cell studies add two key themes: (1) widespread chromosomal instability with 1q gain and 9p/10q loss that correlates with mitochondrial upregulation, radioresistance, and worse outcomes; and (2) an immune‑“cold” microenvironment in specific molecular subtypes, alongside macrophage‑dominated niches driven by CCL5/IL‑6 → STAT3 signaling and TGF‑β–linked partial EMT that promotes invasion. Together, these mechanisms explain the hallmarks of chordoma: local invasion and recurrence, relative resistance to conventional cytotoxic therapy, and selective sensitivity to therapies that target TBXT‑centered transcriptional control, RTK–PI3K/mTOR signaling, chromatin/EZH2 dependencies (in SMARCB1‑deficient tumors), cell‑cycle kinases, or HR‑defect liabilities. ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))

Direct quotations supporting core concepts (short, <25 words each)
- “Somatic duplications of the… transcription factor brachyury (T) [occur] in up to 27% of cases.” (Published Oct 12, 2017.) ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))
- “T is super‑enhancer‑associated in chordoma.” (Published Jan 2019.) ([nature.com](https://www.nature.com/articles/s41591-018-0312-3.pdf?utm_source=openai))
- “Advanced chordomas may frequently harbor molecular alterations associated with impaired DNA repair via homologous recombination.” (Published Apr 10, 2019.) ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- “Immune cold subtype [is] linked to chromosome 9p/10q loss and immune evasion.” (Published Oct 2024.) ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))
- “Signatures related to partial epithelial–mesenchymal transition (p‑EMT)… were related to invasion and poor prognosis.” (Published Sep 20, 2022.) ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))

1) Core Pathophysiology
- Lineage addiction to TBXT/brachyury
  - Familial chordoma: germline TBXT duplication causes high penetrance susceptibility; sporadic disease shows somatic focal duplications and super‑enhancer–driven overexpression of TBXT. CRISPR loss‑of‑function and targeted degradation studies confirm TBXT as the top selective dependency maintaining tumor identity. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/19801981/?utm_source=openai))
- Epigenetic control of TBXT and global enhancer programs
  - TBXT expression is sustained by large H3K27ac‑rich super‑enhancers; transcriptional CDK inhibitors (CDK7/12/13, CDK9) preferentially deplete TBXT protein and suppress growth; KDM6A/B inhibition silences TBXT by increasing H3K27me3 at TBXT regulatory elements. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6633917/?utm_source=openai))
- RTK–PI3K–AKT–mTOR signaling
  - Frequent activation of PDGFR and EGFR signaling and aberrant PI3K–AKT–mTOR pathway activity are recurrent features; co‑targeting PI3K–mTOR and MAPK improves preclinical efficacy. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/22331945/?utm_source=openai))
- Cell‑cycle dysregulation
  - Homozygous deletion/loss of 9p21 (CDKN2A/B) is common and functionally enables CDK4/6‑RB1–mediated G1/S progression; recent phase II data show disease control with CDK4/6 inhibition in CDKN2A/p16‑deficient chordoma. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2361468/?utm_source=openai))
- Chromatin remodeling defects; SMARCB1‑deficient poorly differentiated chordoma
  - PDC (often pediatric) shows loss of SMARCB1/INI1, aggressive behavior, and EZH2 dependence; clinical responses to EZH2 inhibition (tazemetostat), sometimes augmented by radiotherapy, have been documented. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/32631481/?utm_source=openai))
- DNA repair and genomic instability
  - Advanced chordomas exhibit HR‑defect mutational signatures, recurrent large‑scale copy number changes (e.g., 1q gain, 9p/10q loss), and benefit in selected cases from PARP inhibition; resistance can arise via PARP1 structural alteration. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- Tumor microenvironment and immune evasion
  - Proteogenomic immune‑cold subtypes correlate with 9p/10q loss; macrophage‑dominated niches (M2‑like) are promoted by tumor‑derived CCL5 and IL‑6 with STAT3 activation; PD‑1/PD‑L1 expression is heterogeneous; rare INI1‑negative pediatric cases can respond to PD‑1 blockade with brachyury‑specific TCRs. ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))

2) Key Molecular Players
- Genes/Proteins (HGNC)
  - TBXT (HGNC:11610; brachyury): lineage‑defining TF; familial susceptibility (duplications), sporadic focal gains; top tumor dependency; super‑enhancer associated. Evidence: Nature Genet 2009; Nat Commun 2017; Nat Med 2019; Mol Cell 2021. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/19801981/?utm_source=openai))
  - CDKN2A/CDKN2B (HGNC:1787/1788): recurrent 9p21 loss; p16 loss predicts CDK4/6 dependence; biomarker for palbociclib trials. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2361468/?utm_source=openai))
  - PI3K pathway: PIK3CA/PIK3R1 (HGNC:8975/8979) mutations in subset; PTEN (HGNC:9588) loss/copy loss frequent; downstream mTORC1 activation common. ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))
  - RTKs: PDGFRA/PDGFRB (HGNC:8802/8803) and EGFR (HGNC:3236) activated/expression frequent; EGFR/ERBB inhibitors show preclinical and anecdotal clinical activity. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
  - SMARCB1 (HGNC:11103): loss defines poorly differentiated chordoma; marks aggressive biology; creates EZH2 dependency. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/32631481/?utm_source=openai))
  - LYST (HGNC:6729): recurrently inactivated (≈10%); candidate driver in sporadic chordoma. ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))
  - DNA repair genes (BRCA2, CHEK2, NBN, etc.): alterations contribute to HRD signatures and PARP inhibitor sensitivity in selected advanced cases. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
  - RPRD1B (HGNC:30862): proteogenomics nominate as a marker/putative target in radioresistance subgroups. ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))
  - Microenvironment mediators: CCL5–CCR5 axis; IL‑6–STAT3; TGF‑β pathway and p‑EMT programs (SOX6/SOX9 co‑activation). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37185233/?utm_source=openai))
- Chemical entities (selected; CHEBI where available)
  - Imatinib (PDGFR inhibitor; CHEBI:45783) and combinations with mTOR inhibitors (sirolimus/everolimus) target PDGFR→PI3K/mTOR signaling. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/22331945/?utm_source=openai))
  - EGFR inhibitors: erlotinib (CHEBI:114785), gefitinib (CHEBI:49668), lapatinib (CHEBI:49603) show preclinical and occasional clinical responses. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
  - Transcriptional CDK inhibitors: THZ1 (CDK7), CDK9 inhibitors (alvocidib/flavopiridol) suppress TBXT levels and growth. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6633917/?utm_source=openai))
  - KDM6A/B inhibitor (e.g., GSK‑J4 analogs/KDOBA67): epigenetically silences TBXT and induces death. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7616956/?utm_source=openai))
  - EZH2 inhibitor: tazemetostat (EZH2) effective in SMARCB1‑deficient PDC (case/PDX; immunologic remodeling). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9165752/?utm_source=openai))
  - CDK4/6 inhibitor: palbociclib (CHEBI:85993) yields disease control in CDKN2A/p16‑deficient chordoma (phase II). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40627883/?utm_source=openai))
  - PARP inhibitor: olaparib (CHEBI:83766) produced a prolonged response in an HRD‑positive case; resistance via PARP1 HD destabilization. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- Cell types (CL terms)
  - Malignant notochordal‑like tumor cells; cancer‑associated fibroblasts/myofibroblasts (CL:0000057/CL:0000186); endothelial cells (CL:0000115); tumor‑associated macrophages (CL:0000235), often M2‑skewed; T cells (CL:0000084) with variable infiltration. ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
- Anatomical locations (UBERON terms)
  - Skull base—clivus (internal surface of cranial base, UBERON:0017692); vertebral column (UBERON:0001130); sacrum; nucleus pulposus (UBERON:0002242) as developmental remnant site. ([amigo.geneontology.org](https://amigo.geneontology.org/amigo/term/UBERON%3A0017692?utm_source=openai))

3) Biological Processes (GO terms; disrupted pathways/processes)
- Lineage‑specific transcription and enhancer regulation: transcription by RNA polymerase II (GO:0006366); chromatin organization (GO:0006325); histone modification (GO:0016570); SWI/SNF complex function (GO:0016514); PRC2 complex (GO:0043623). Evidence: TBXT super‑enhancers; SMARCB1 loss/EZH2 dependency. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6633917/?utm_source=openai))
- Cell‑cycle control: G1/S transition of mitotic cell cycle (GO:0000082) via CDKN2A loss → CDK4/6 activation. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- Signal transduction: ERBB/Egfr signaling pathway (GO:0038127); PI3K signaling (GO:0014065); MAPK cascade (GO:0000165); TGF‑β receptor signaling (GO:0007179). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
- DNA damage response/repair: double‑strand break repair via homologous recombination (GO:0000724); response to DNA damage stimulus (GO:0006974). ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- Cell motility/invasion and EMT: epithelial to mesenchymal transition (GO:0001837); regulation of cell migration (GO:0030334); extracellular matrix organization (GO:0030198). ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
- Immune and inflammatory signaling in TME: response to interleukin‑6 (GO:0071354); positive regulation of macrophage differentiation (GO:0045651); negative regulation of T cell activation (GO:0050868) inferred in immune‑cold phenotypes. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39393273/?utm_source=openai))

4) Cellular Components (where key processes occur)
- Nuclear transcriptional machinery and chromatin condensates: nucleus/nuclear chromatin/super‑enhancer hubs (GO:0005634/GO:0000790); SWI/SNF complex (GO:0016514); PRC2 (GO:0043623). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7817874/?utm_source=openai))
- Plasma membrane RTK complexes and signaling endosomes: EGFR/PDGFR at the cell surface (GO:0005886). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
- Cytoplasm/lysosome: LYST‑linked lysosomal trafficking (GO:0005764). ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))
- Mitochondria: upregulated mitochondrial functions associated with 1q gain and radioresistance in defined proteomic subtypes. ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))
- Extracellular matrix: abundant matrix in conventional/chondroid chordoma; invasion along bone/soft tissue planes (GO:0031012/GO:0030198). ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))

5) Disease Progression (sequence of events)
- Initiation/susceptibility
  - Embryonic notochordal remnants persist (nucleus pulposus lineage); germline TBXT duplication or risk SNP (rs2305089) increases susceptibility in some populations. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/19801981/?utm_source=openai))
- Early tumorigenesis
  - TBXT‑driven transcriptional program established via super‑enhancers; somatic TBXT duplications in a subset; early 9p21 (CDKN2A/B) loss and PI3K pathway lesions commonly emerge. ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))
- Local progression
  - Activation of PDGFR/EGFR and PI3K–mTOR; ECM remodeling and p‑EMT (TGF‑β–linked) promote local invasion and recurrence after resection/radiation. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
- Advanced disease evolution
  - Chromosomal instability (1q gain; 9p/10q loss), mitochondrial upregulation, and—especially in pre‑treated tumors—HRD signatures support sensitivity to PARP inhibition in selected cases but also enable resistance via PARP1 alterations; immune‑cold phenotypes limit ICI responses except in subsets (e.g., INI1‑negative pediatric chordoma). ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))
- Distinct variants
  - Poorly differentiated chordoma (PDC): SMARCB1/INI1‑loss, aggressive clinical course, EZH2 dependency; dedifferentiated chordoma is rare and high‑grade. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/32631481/?utm_source=openai))

6) Phenotypic Manifestations (key clinical phenotypes; HPO examples)
- Skull base (clival) chordoma: headache (HPO:0002315), diplopia (HPO:0000651), cranial nerve palsies (e.g., VI palsy), dysphagia (HPO:0002015). Mechanism: local invasion/compression at skull base and cavernous sinus; p‑EMT/invasion programs. ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
- Mobile spine/sacral chordoma: back/sacral pain (HPO: Back pain), radiculopathy, bowel/bladder dysfunction (urinary incontinence, HPO:0000020). Mechanism: osseous destruction, epidural/foraminal extension; macrophage‑rich niches associated with bone destruction. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/39393273/?utm_source=openai))
- Metastasis (lung, bone, liver) occurs in a minority but increases with dedifferentiation or PDC; mechanism: EMT‑like programs, CXCR4 upregulation (reported in PDC). ([academic.oup.com](https://academic.oup.com/ajcp/article/154/Supplement_1/S151/5942235?utm_source=openai))

Gene/protein annotations with ontology terms (examples)
- TBXT (HGNC:11610)
  - Function: transcription regulator activity (GO:0140110); regulation of mesoderm/notochord development (GO:0001708).
  - Evidence: familial duplications; super‑enhancer–driven dependency; CRISPR and degrader studies. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/19801981/?utm_source=openai))
- CDKN2A (HGNC:1787)
  - Function: cyclin‑dependent kinase inhibitor activity (GO:0004861); negative regulation of G1/S (GO:2000134).
  - Evidence: frequent 9p21 loss; palbociclib activity in p16‑loss tumors. (Final results 2025.) ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2361468/?utm_source=openai))
- PTEN (HGNC:9588), PIK3CA (HGNC:8975)
  - Function: PI3K pathway regulation (GO:0014065); negative regulation of PI3K signaling (PTEN).
  - Evidence: copy loss/PTEN mutations; actionable PI3K signaling alterations in 16% of cases. ([nature.com](https://www.nature.com/articles/s41467-017-01026-0?utm_source=openai))
- EGFR (HGNC:3236), PDGFRB (HGNC:8803)
  - Function: receptor tyrosine kinase activity (GO:0004714).
  - Evidence: activation/expression in many chordomas; in vitro and case‑level responses to EGFR inhibitors; imatinib benefits disease control via PDGFR. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
- SMARCB1 (HGNC:11103)
  - Function: SWI/SNF complex subunit (GO:0016514); tumor suppressor.
  - Evidence: loss defines PDC, confers EZH2 dependency; clinical activity with tazemetostat +/− RT. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/32631481/?utm_source=openai))
- DNA repair: BRCA2 (HGNC:1101), CHEK2 (HGNC:1925), NBN (HGNC:7652)
  - Function: homologous recombination (GO:0000724); checkpoint control (GO:0000075).
  - Evidence: HRD signatures; PARP inhibitor response and resistance mechanism identified. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))

Cell type involvement (CL terms; examples)
- Malignant chordoma cell (notochordal‑like): TBXT‑high; p‑EMT subset drives invasion.
- Macrophages (CL:0000235): M2‑polarization via tumor IL‑6/CCL5; promote invasion/osteolysis. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37185233/?utm_source=openai))
- CAFs/myofibroblasts (CL:0000186): TGF‑β ligand–receptor interactions with tumor cells; ECM remodeling. ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
- Endothelial cells (CL:0000115) and T cells (CL:0000084): variable infiltration; immune‑cold proteomic subtypes noted. ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))

Anatomical locations (UBERON terms; examples)
- Skull base/clivus (internal surface of cranial base, UBERON:0017692); vertebral column (UBERON:0001130); sacrum; nucleus pulposus (UBERON:0002242) as notochordal remnant. ([amigo.geneontology.org](https://amigo.geneontology.org/amigo/term/UBERON%3A0017692?utm_source=openai))

Chemical entities (CHEBI) linked to mechanisms (examples)
- Imatinib (CHEBI:45783); sirolimus/everolimus (CHEBI:9168/68478) for PDGFR→mTOR axis. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/22331945/?utm_source=openai))
- Erlotinib (CHEBI:114785), gefitinib (CHEBI:49668), lapatinib (CHEBI:49603) for EGFR/ERBB signaling. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
- Palbociclib (CHEBI:85993) for CDKN2A loss/CDK4‑RB axis. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40627883/?utm_source=openai))
- Olaparib (CHEBI:83766) in HRD‑positive advanced tumors. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- Tazemetostat (EZH2 inhibitor) in SMARCB1‑deficient PDC. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9165752/?utm_source=openai))
- Transcriptional CDK inhibitors (e.g., THZ1; CDK9 inhibitors) and KDM6A/B inhibitors that suppress TBXT programs. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6633917/?utm_source=openai))

Evidence items (primary literature with PMIDs, publication dates; key findings)
- TBXT duplications cause familial chordoma; TBXT is lineage driver
  - Yang et al., Nature Genetics, 2009 (PMID:19801981): “T (brachyury) gene duplication confers major susceptibility to familial chordoma.” ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/19801981/?utm_source=openai))
  - Tarpey et al., Nature Communications, 2017 (PMID:29026114): sporadic driver landscape; TBXT focal duplications; PI3K genes; LYST. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/29026114/?utm_source=openai))
  - Sharifnia et al., Nature Medicine, 2019 (PDF), and DeCaprio lab, Molecular Cell, 2021: TBXT super‑enhancer dependency; TBXT degradation disrupts autoregulatory program. ([nature.com](https://www.nature.com/articles/s41591-018-0312-3.pdf?utm_source=openai))
- Epigenetic silencing of TBXT via KDM6A/B inhibition
  - Cottone et al., Sci. Transl. Med. (2020) reported by subsequent open‑access article: “Inhibition of H3K27 demethylases inactivates TBXT and promotes chordoma cell death.” (PMID:32855205). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7616956/?utm_source=openai))
- PI3K–mTOR/RTK signaling and targeted therapy
  - Tamborini/Stacchiotti et al., JCO, 2012 (PMID:22331945): phase II imatinib in PDGFR‑positive chordoma; disease control predominant. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/22331945/?utm_source=openai))
  - Small‑molecule EGFR inhibitors active in preclinical models; lapatinib phase II shows signals in EGFR‑positive patients (2013; PMID:23559153). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/23559153/?utm_source=openai))
  - Neuro‑Oncology (2025 supplement): co‑targeting PI3K–mTOR and MAPK more effective in preclinical models. ([academic.oup.com](https://academic.oup.com/neuro-oncology/article-abstract/27/Supplement_3/iii169/8272555?utm_source=openai))
- Cell‑cycle dysregulation and CDK4/6 inhibition
  - Frequent 9p21 deletion (array CGH; 2008) and targeted panel studies (2014) highlight CDKN2A/B loss. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC2361468/?utm_source=openai))
  - Palbociclib phase II (final results posted 2025; PMID:40627883): disease control with median PFS ≈5–6 months in p16/CDKN2A‑loss chordoma. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40627883/?utm_source=openai))
- DNA repair/HRD; PARP inhibition
  - Hölzl et al., Nature Communications, 2019: HRD signatures; clinical response and resistance mechanism to olaparib in advanced chordoma. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
- SMARCB1‑deficient poorly differentiated chordoma (PDC) and EZH2 dependency
  - Agaimy et al., Mod Pathol., 2017–2021; Dalessandri et al., 2020s: SMARCB1/INI1 loss defines PDC with dismal prognosis. ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/32631481/?utm_source=openai))
  - Alholle et al., Clin case/Neuro‑Oncol. Adv., 2022: abscopal‑like immune remodeling and durable control with tazemetostat plus RT in SMARCB1‑deleted PDC. ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC9165752/?utm_source=openai))
- Microenvironment, invasion, and immune contexture
  - Single‑cell atlas (Cell Discovery, 2022): p‑EMT programs drive invasion; TGF‑β–targeting (YL‑13027) showed clinical stabilization (phase I). ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
  - Proteogenomics (Nat Commun, 2024): chromosome instability and immune‑cold subtypes (9p/10q loss) with poorer outcomes; 1q gain/mitochondrial upregulation linked to radioresistance; RPRD1B highlighted. ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))
  - TME cytokines: CCL5–CCR5 axis and IL‑6–STAT3 promote M2 polarization and invasion (2023–2024). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/37185233/?utm_source=openai))
  - PD‑1/PD‑L1 expression is present in a subset; a pediatric INI1‑negative case responded to nivolumab with brachyury‑specific TCR expansion (2021). ([nature.com](https://www.nature.com/articles/s41698-021-00238-4?utm_source=openai))

Ontology‑ready summary (for knowledge base population)
- Disease (MONDO/DOID): Chordoma (DOID:3302); Spinal chordoma (MONDO:0002894).
- Core mechanisms:
  - TBXT dependency; super‑enhancer addiction (GO:0006366; GO:0006325; GO:0016570); nucleus/nuclear chromatin (GO:0005634/GO:0000790). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC6633917/?utm_source=openai))
  - RTKs (EGFR/PDGFR) → PI3K–AKT–mTOR (GO:0038127; GO:0014065); plasma membrane (GO:0005886). ([pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC4922416/?utm_source=openai))
  - CDKN2A loss → CDK4/6 activation; G1/S transition (GO:0000082). ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
  - HRD and DNA repair failure (GO:0000724); PARP inhibitor sensitivity/resistance. ([nature.com](https://www.nature.com/articles/s41467-019-09633-9))
  - SMARCB1 loss → PRC2/EZH2 dependency; SWI/SNF vs PRC2 balance (GO:0016514; GO:0043623). ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/32631481/?utm_source=openai))
  - TGF‑β–linked p‑EMT and ECM remodeling (GO:0007179; GO:0001837; GO:0030198). ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
- Cell types (CL): malignant notochordal‑like cells; CAFs/myofibroblasts (CL:0000186); macrophages (CL:0000235); endothelial cells (CL:0000115); T cells (CL:0000084). ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))
- Anatomy (UBERON): clivus (internal cranial base UBERON:0017692); vertebral column (UBERON:0001130); sacrum; nucleus pulposus (UBERON:0002242). ([amigo.geneontology.org](https://amigo.geneontology.org/amigo/term/UBERON%3A0017692?utm_source=openai))
- Phenotypes (HPO examples): headache, diplopia (HPO:0000651), cranial nerve palsy, dysphagia (HPO:0002015), back/sacral pain, urinary incontinence (HPO:0000020). ([nature.com](https://www.nature.com/articles/s41421-022-00459-2))

Notes on recency and data quality
- The 2024 proteogenomic study (Nature Communications; published Oct 2024) provides the most up‑to‑date multi‑omics classification, CIN patterns (1q gain, 9p/10q loss), and immune‑cold subtype associations. ([nature.com](https://www.nature.com/articles/s41467-024-52285-7))
- Final results of a 2025 multicenter phase II trial of palbociclib in CDKN2A/p16‑deficient chordoma reported disease control but modest PFS, supporting CDK4/6 inhibition as a rational backbone for combinations. (Published 2025; PMID:40627883.) ([pubmed.ncbi.nlm.nih.gov](https://pubmed.ncbi.nlm.nih.gov/40627883/?utm_source=openai))

If you’d like, I can translate this into a structured JSON/YAML payload with explicit HGNC, GO, CL, UBERON, CHEBI, and evidence (PMID/date/quote) fields for direct ingestion into your knowledge base.