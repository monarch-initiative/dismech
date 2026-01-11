---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-08T14:13:00.447661'
end_time: '2026-01-08T14:22:44.926520'
duration_seconds: 584.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Scurvy
  mondo_id: ''
  category: Nutritional
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Scurvy
- **MONDO ID:**  (if available)
- **Category:** Nutritional

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Scurvy**.
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
- **Disease Name:** Scurvy
- **MONDO ID:**  (if available)
- **Category:** Nutritional

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Scurvy**.
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


# Disease Pathophysiology Research Template

## Target Disease
- Disease Name: Scurvy (vitamin C deficiency)
- MONDO ID: 
- Category: Nutritional

## Pathophysiology description (concise overview)
Scurvy results from inadequate L-ascorbate (vitamin C), an essential reducing cofactor for multiple non-heme Fe(II)/2-oxoglutarate (2-OG)–dependent dioxygenases and select monooxygenases. The cardinal molecular lesion is failure of collagen post-translational hydroxylation (proline, lysine), which destabilizes the triple helix, impairs cross-linking, and weakens extracellular matrix (ECM). Clinically, this manifests as capillary fragility with bleeding (petechiae, ecchymoses, gingival hemorrhage), poor wound healing, musculoskeletal pain, and characteristic bone/growth plate abnormalities. Ascorbate also supports HIF hydroxylases (EGLN/PHDs, FIH), TET DNA demethylases, dopamine β-hydroxylase (DBH), peptidylglycine α-amidating monooxygenase (PAM), and carnitine biosynthesis, so deficiency can secondarily perturb hypoxia signaling, epigenetic regulation, catecholamine and peptide amidation pathways, and cellular energy metabolism. Tissue vitamin C homeostasis depends on SLC23A1/SLC23A2 (SVCT1/2) and complementary uptake of dehydroascorbic acid (DHA) via GLUT transporters; dietary lack depletes the small total body pool within weeks, producing the clinical picture of scurvy (gastrointestinal and systemic bleeding, mucocutaneous and skeletal features). (gandhi2023scurvyrediscoveringa pages 1-2, gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7)

## 1. Core Pathophysiology
- Collagen hydroxylation failure • Ascorbate donates electrons to prolyl and lysyl hydroxylases during collagen biosynthesis; without ascorbate, hydroxyproline/4-hydroxylysine formation is inadequate, preventing triple-helix stability and mature cross-links. “This reaction uses ascorbic acid as an electron donor,” and failure of hydroxylation impairs bone and fibroblast function, tooth development, wound healing, and vessel integrity. (Gandhi 2023, Diseases, May 2023; doi:10.3390/diseases11020078; https://doi.org/10.3390/diseases11020078) (gandhi2023scurvyrediscoveringa pages 2-4)
- ECM and vascular integrity • Matrix failure in skin and mucosa explains perifollicular hemorrhage, petechiae, ecchymoses, gingival swelling/bleeding, and gastrointestinal bleeding with normal coagulation tests in many patients. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 1-2, gandhi2023scurvyrediscoveringa pages 4-5)
- Bone and growth plate • Deficient osteoid formation and increased bone resorption yield osteopenia/osteoporosis, cortical thinning, metaphyseal changes and growth-plate abnormalities; pediatric scurvy often presents with limb pain, limp or refusal to walk, and characteristic radiologic bands and periosteal changes. (Gandhi 2023; Lu 2023, Front Nutr, Oct 2023; doi:10.3389/fnut.2023.1265334; https://doi.org/10.3389/fnut.2023.1265334) (gandhi2023scurvyrediscoveringa pages 4-5, lu2023scurvyina pages 2-3)
- Hypoxia/epigenetic enzyme effects • Ascorbate supports Fe(II)/2-OG dioxygenases beyond collagen: HIF prolyl hydroxylases (EGLN1/2/3) and the asparaginyl hydroxylase FIH regulate HIF; ascorbate helps maintain their catalytic cycles, so deficiency can dysregulate HIF activity. TET dioxygenases (TET1–3) require ascorbate to promote DNA demethylation; low vitamin C may contribute to aberrant methylation. (Fandrey 2006, Cardiovasc Res, Sep 2006; doi:10.1016/j.cardiores.2006.05.005; https://doi.org/10.1016/j.cardiores.2006.05.005; Yue & Rao 2020, Blood, Sep 2020; doi:10.1182/blood.2019004158; https://doi.org/10.1182/blood.2019004158) (ramanujan2024vitamincis pages 7-7, alberts2025vitaminca pages 1-2)
- Neurochemical and energy pathways • DBH uses ascorbate to convert dopamine to norepinephrine; vitamin C deficiency therefore can lower NE synthesis, contributing to fatigue, mood/cognitive symptoms and autonomic complaints. Ascorbate also serves as electron donor for carnitine biosynthesis steps; deficiency can reduce carnitine availability and worsen fatigue. (Gandhi 2023; Plevin & Galletly 2020, BMC Psychiatry, Jun 2020; doi:10.1186/s12888-020-02730-w; https://doi.org/10.1186/s12888-020-02730-w) (gandhi2023scurvyrediscoveringa pages 2-4, gandhi2023scurvyrediscoveringa pages 4-5)

## 2. Key Molecular Players
- Genes/Proteins (HGNC): Prolyl 4-hydroxylase (P4HA1/2/3); Lysyl hydroxylase (PLOD1/2/3); EGLN1/2/3 (PHD1–3); HIF1AN (FIH); TET1/2/3; DBH; PAM; TMLHE/BBOX1 (carnitine biosynthesis); SLC23A1/2 (SVCT1/2); SLC2A family (GLUTs for DHA). Mechanistic roles and evidence mapping are synthesized in the artifact below. (ramanujan2024vitamincis pages 7-7, gandhi2023scurvyrediscoveringa pages 2-4, alberts2025vitaminca pages 1-2)
- Chemical Entities (CHEBI): L‑ascorbate; dehydroascorbic acid; dopamine; norepinephrine; carnitine. (gandhi2023scurvyrediscoveringa pages 2-4, lu2023scurvyina pages 2-3)
- Cell Types (CL): Fibroblasts (collagen production), endothelial cells (capillary integrity), osteoblasts and chondrocytes (osteoid and growth plate matrix). (gandhi2023scurvyrediscoveringa pages 4-5)
- Anatomical Locations (UBERON): Skin, gingiva, bone, epiphyseal (growth) plate, GI mucosa. (gandhi2023scurvyrediscoveringa pages 4-5, gandhi2023scurvyrediscoveringa pages 1-2)

| Category | Entity Name | Ontology ID / Abbrev | Role in Scurvy Pathophysiology (1-2 sentences) | Evidence |
|---|---|---|---|---|
| Enzyme | Prolyl 4-hydroxylase alpha subunits (P4HA1/2/3) | HGNC:P4HA1/P4HA2/P4HA3 | Hydroxylate proline residues in procollagen to enable triple-helix formation; impaired activity from ascorbate deficiency destabilizes collagen and weakens ECM, causing bleeding and poor wound healing. | (ramanujan2024vitamincis pages 7-7, gandhi2023scurvyrediscoveringa pages 2-4) |
| Enzyme | Lysyl hydroxylases (PLOD1/2/3) | HGNC:PLOD1/PLOD2/PLOD3 | Hydroxylate lysine residues required for collagen cross-linking; deficiency reduces crosslinks leading to fragile connective tissue and defective bone matrix. | (ramanujan2024vitamincis pages 7-7, gandhi2023scurvyrediscoveringa pages 2-4) |
| Enzyme (oxygen sensor) | HIF prolyl hydroxylases (EGLN1/2/3, a.k.a. PHD1/2/3) | HGNC:EGLN1/EGLN2/EGLN3 | 2‑OG/Fe(II)-dependent prolyl hydroxylases that regulate HIF stability; ascorbate maintains enzyme activity so deficiency can dysregulate hypoxia signaling. | (ramanujan2024vitamincis pages 7-7) |
| Enzyme (regulator) | Factor inhibiting HIF (HIF1AN / FIH) | HGNC:HIF1AN | Asparaginyl hydroxylase that modulates HIF transcriptional activity; requires reducing cofactor activity supported by ascorbate, so deficiency can alter HIF transcriptional outputs. | (ramanujan2024vitamincis pages 7-7) |
| Enzyme (epigenetic) | TET1 / TET2 / TET3 | HGNC:TET1/TET2/TET3 | Fe(II)/2‑OG dioxygenases that oxidize 5mC to 5hmC promoting active DNA demethylation; ascorbate is a cofactor and deficiency may impair epigenetic regulation. | (alberts2025vitaminca pages 1-2, gandhi2023scurvyrediscoveringa pages 2-4) |
| Enzyme (catecholamine) | Dopamine beta-hydroxylase (DBH) | HGNC:DBH | Converts dopamine → norepinephrine within secretory vesicles using ascorbate as electron donor; deficiency can reduce NE synthesis and contribute to neuropsychiatric/autonomic features. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Enzyme (peptide maturation) | Peptidylglycine alpha-amidating monooxygenase (PAM) | HGNC:PAM | Amidating monooxygenase requiring ascorbate for peptide hormone/neuropeptide maturation; deficiency may impair peptide signaling. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Enzymes (carnitine biosynthesis) | TMLHE, BBOX1 | HGNC:TMLHE, BBOX1 | Ascorbate-dependent dioxygenase steps in carnitine biosynthesis; deficiency can reduce carnitine levels and contribute to muscle fatigue. | (gandhi2023scurvyrediscoveringa pages 2-4, lu2023scurvyina pages 2-3) |
| Transporter | Vitamin C transporters (SLC23A1 / SLC23A2; SVCT1/2) | HGNC:SLC23A1, SLC23A2 | Sodium-dependent vitamin C transporters mediate ascorbate uptake and tissue accumulation; altered expression or saturation affects tissue ascorbate and scurvy susceptibility. | (ramanujan2024vitamincis pages 7-7) |
| Transporter (alternative) | DHA transport via GLUTs (SLC2A family) | HGNC:SLC2A* (GLUTs) | Oxidized form dehydroascorbic acid (DHA) can be transported via GLUT family members and reduced intracellularly to ascorbate, providing an alternative uptake route. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Structural protein / GO | Collagen (generic) | GO:0005581 (extracellular matrix) | Principal ECM protein requiring prolyl/lysyl hydroxylation for structural stability; defective collagen underlies capillary fragility, mucosal bleeding, poor wound healing, and defective bone matrix. | (gandhi2023scurvyrediscoveringa pages 2-4, lu2023scurvyina pages 2-3) |
| Cell type (CL) | Fibroblast | CL:Fibroblast | Major collagen-producing stromal cell; impaired collagen processing in fibroblasts leads to weakened dermal and connective tissues seen in scurvy. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Cell type (CL) | Osteoblast | CL:Osteoblast | Bone-forming cells that produce osteoid rich in type I collagen; defective collagen synthesis impairs osteoid formation, causing osteoporosis, cortical thinning, and growth-plate pathology. | (gandhi2023scurvyrediscoveringa pages 4-5, nefihancoro2024analysisofthe pages 4-7) |
| Cell type (CL) | Chondrocyte | CL:Chondrocyte | Cartilage/growth-plate cells that depend on collagen-rich matrix; ascorbate deficiency impairs endochondral matrix formation producing metaphyseal and epiphyseal abnormalities. | (gandhi2023scurvyrediscoveringa pages 4-5, lu2023scurvyina pages 2-3) |
| Cell type (CL) | Endothelial cell | CL:Endothelial cell | Vascular integrity relies on collagen-containing basement membrane; impaired collagen leads to capillary fragility and hemorrhage (petechiae, ecchymoses). | (gandhi2023scurvyrediscoveringa pages 2-4, gandhi2023scurvyrediscoveringa pages 1-2) |
| Anatomy (UBERON) | Gingiva | UBERON:Gingiva | Highly vascular mucosa with collagen-rich stroma; scurvy causes gingival swelling, bleeding, and periodontal disease due to ECM failure. | (gandhi2023scurvyrediscoveringa pages 2-4, lu2023scurvyina pages 2-3) |
| Anatomy (UBERON) | Skin | UBERON:Skin | Dermal ECM failure causes perifollicular hemorrhages, petechiae, and poor wound healing characteristic of scurvy. | (gandhi2023scurvyrediscoveringa pages 4-5, gandhi2023scurvyrediscoveringa pages 2-4) |
| Anatomy (UBERON) | Bone | UBERON:Bone | Impaired collagen in osteoid leads to brittle bones, osteoporosis, cortical thinning, and fracture risk in scurvy. | (nefihancoro2024analysisofthe pages 4-7, gandhi2023scurvyrediscoveringa pages 4-5) |
| Anatomy (UBERON) | Epiphyseal (growth) plate | UBERON:Epiphyseal_plate | Collagen-dependent cartilage zone for endochondral ossification; deficiency produces growth-plate abnormalities, metaphyseal bands, and limp/pseudoparalysis in children. | (gandhi2023scurvyrediscoveringa pages 4-5, lu2023scurvyina pages 2-3) |
| Chemical (CHEBI) | L-ascorbate (vitamin C) | CHEBI:Asc | Essential reducing cofactor for multiple Fe(II)/2‑OG dioxygenases and antioxidant; insufficient levels cause scurvy. | (gandhi2023scurvyrediscoveringa pages 1-2, ramanujan2024vitamincis pages 7-7) |
| Chemical (CHEBI) | Dehydroascorbic acid (DHA) | CHEBI:DHA | Oxidized form of ascorbate transported via GLUTs and reduced intracellularly to regenerate ascorbate; important alternative uptake pathway. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Chemical (CHEBI) | Dopamine | CHEBI:Dopamine | Catecholamine precursor converted by DBH to norepinephrine using ascorbate; impaired DBH activity can alter neurotransmitter balance. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Chemical (CHEBI) | Norepinephrine | CHEBI:Norepinephrine | Product of DBH; reduced synthesis in severe ascorbate deficiency may contribute to autonomic and neuropsychiatric symptoms. | (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7) |
| Chemical (CHEBI) | Carnitine | CHEBI:Carnitine | Requires ascorbate-dependent enzymatic steps for biosynthesis; deficiency can impair fatty acid transport into mitochondria and produce fatigue/weakness. | (gandhi2023scurvyrediscoveringa pages 2-4, lu2023scurvyina pages 2-3) |


*Table: A concise reference table mapping enzymes, cells, tissues, and chemicals relevant to scurvy to ontology identifiers, their roles in pathophysiology, and the supporting evidence (context IDs). This facilitates ontology-driven annotation and rapid linking of mechanisms to sources.*

## 3. Biological Processes (GO) disrupted
- Collagen biosynthetic process and post-translational modification (proline/lysine hydroxylation; triple-helix formation; cross-linking); ECM organization; wound healing; angiogenesis and vascular integrity. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 2-4, gandhi2023scurvyrediscoveringa pages 4-5)
- Cellular responses to hypoxia; regulation of HIF signaling by prolyl/asparaginyl hydroxylation (EGLN/PHDs; FIH). (Fandrey 2006) (ramanujan2024vitamincis pages 7-7)
- DNA demethylation via TET-mediated oxidation of 5-mC to 5-hmC; epigenetic regulation of immune and lineage programs. (Yue & Rao 2020; Morante-Palacios 2022, Nucleic Acids Res, Oct 2022; doi:10.1093/nar/gkac941; https://doi.org/10.1093/nar/gkac941) (alberts2025vitaminca pages 1-2, ramanujan2024vitamincis pages 7-8)
- Catecholamine biosynthetic process (DBH step dopamine→norepinephrine); peptide amidation (PAM); carnitine biosynthetic process. (Gandhi 2023; Plevin 2020) (gandhi2023scurvyrediscoveringa pages 2-4, gandhi2023scurvyrediscoveringa pages 4-5)

## 4. Cellular Components affected
- Endoplasmic reticulum lumen and cisternae (collagen prolyl/lysyl hydroxylases act co-translationally/post-translationally on procollagen); secretory pathway/extracellular space (ECM deposition). (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 2-4)
- Nucleus/chromatin (TET-mediated DNA demethylation); cytosol and mitochondria (carnitine metabolism); secretory vesicles (DBH in catecholaminergic vesicles). (Yue 2020; Plevin 2020) (alberts2025vitaminca pages 1-2, gandhi2023scurvyrediscoveringa pages 4-5)

## 5. Disease Progression
- Trigger and depletion: Humans lack GULO and must ingest vitamin C; limited body pool (approx. 1–3 weeks to deplete on very low intake) and saturable gut/renal handling cause rapid deficiency under poor diet/malabsorption. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 1-2)
- Early biochemical failure: Insufficient ascorbate disrupts collagen hydroxylation, compromising ECM repair and capillary integrity; fatigue may occur early via reduced catecholamines and carnitine. (Lu 2023; Gandhi 2023) (lu2023scurvyina pages 2-3, gandhi2023scurvyrediscoveringa pages 2-4)
- Clinical evolution: Within 4–12 weeks of inadequate intake, nonspecific symptoms progress to gingival bleeding, perifollicular hemorrhages, ecchymoses, joint pain/hemarthrosis, and in children, limb pain and refusal to walk due to metaphyseal and periosteal changes. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 4-5)
- Advanced skeletal involvement: Osteoporosis and cortical thinning correlate with severity; growth-plate pathology and fractures may occur if untreated. (Nefihancoro 2024, Bioscientia Medicina, Jun 2024; doi:10.37275/bsm.v8i9.1066; https://doi.org/10.37275/bsm.v8i9.1066) (nefihancoro2024analysisofthe pages 4-7)
- Reversibility: Vitamin C repletion rapidly reverses constitutional and bleeding symptoms; musculoskeletal recovery follows over weeks. (Lu 2023) (lu2023scurvyina pages 2-3)

## 6. Phenotypic Manifestations and mechanistic links
- Mucocutaneous: Perifollicular hemorrhages, petechiae, ecchymoses, corkscrew hairs, gingival swelling/bleeding—due to fragile capillaries and ECM failure from defective collagen. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 4-5)
- Musculoskeletal: Arthralgias, hemarthrosis, muscle hematomas; in children, limp/refusal to walk; radiologic metaphyseal bands, periosteal reaction, and osteopenia—reflecting defective osteoid/calcified cartilage matrix. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 4-5)
- Gastrointestinal: Occult or overt bleeding due to mucosal/vascular fragility. (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 1-2)
- Neuropsychiatric: Fatigue, depression, cognitive complaints are reported in deficiency; biologically linked to decreased NE synthesis (DBH cofactor role) and broader neurotransmitter/antioxidant roles. (Plevin 2020) (gandhi2023scurvyrediscoveringa pages 4-5)

## Evidence items (with selected direct quotations)
- “This reaction uses ascorbic acid as an electron donor,” referring to hydroxylation of proline and lysine residues in collagen; failure of hydroxylation impairs bone and fibroblast function, tooth development, wound healing, and vessel integrity. (Gandhi 2023, Diseases, May 2023; https://doi.org/10.3390/diseases11020078) (gandhi2023scurvyrediscoveringa pages 2-4)
- Pediatric skeletal presentation: review and MRI/radiograph features (periosteal reaction, metaphyseal bands, refusal to walk) summarized in Gandhi 2023. (gandhi2023scurvyrediscoveringa pages 4-5)
- Observational 2024 bone study: “Radiological examination shows significant changes in long bones, especially osteoporosis and thinning of the cortex... positive correlation between the severity of scurvy and the incidence of osteoporosis (rho = 0.495, p = 0.005) and cortical thinning (rho = 0.394, p = 0.031).” (Nefihancoro 2024; https://doi.org/10.37275/bsm.v8i9.1066) (nefihancoro2024analysisofthe pages 4-7)
- TET and vitamin C: Vitamin C “serves as a cofactor for Fe(II) and 2-oxoglutarate (2OG)-dependent dioxygenases including TET family enzymes,” promoting DNA demethylation. (Yue & Rao 2020, Blood; https://doi.org/10.1182/blood.2019004158) (alberts2025vitaminca pages 1-2)
- HIF hydroxylases: Mechanistic role of ascorbate in preserving prolyl hydroxylase activity and regulating HIF signaling reviewed by Fandrey et al. (Cardiovasc Res 2006; https://doi.org/10.1016/j.cardiores.2006.05.005) (ramanujan2024vitamincis pages 7-7)
- Immune/epigenetic reprogramming: Vitamin C enhances NF-κB–driven epigenomic remodeling in dendritic cells via TET2, boosting antigen presentation. (Morante‑Palacios 2022; https://doi.org/10.1093/nar/gkac941) (ramanujan2024vitamincis pages 7-8)

## Current applications and real‑world implementations
- Clinical detection and radiology • Recent case reports and observational data (2023–2024) emphasize that scurvy should be considered in patients with unexplained mucocutaneous bleeding and musculoskeletal pain; radiographs/MRI can reveal metaphyseal bands, periosteal reactions, osteopenia, and cortical thinning that improve with repletion. (Lu 2023; Nefihancoro 2024) (lu2023scurvyina pages 2-3, nefihancoro2024analysisofthe pages 4-7)
- Risk stratification and transporters • Contemporary pediatric review synthesizes transporter biology (SLC23A1/2; DHA uptake via GLUTs) and vulnerable populations (e.g., chronic disease, critical illness), informing screening and supplementation strategies. (Ramanujan 2024, Curr Pediatr Rep, May 2024; https://doi.org/10.1007/s40124-024-00315-9) (ramanujan2024vitamincis pages 7-8, ramanujan2024vitamincis pages 7-7)

## Expert opinions and analysis
- Consensus from recent reviews supports a central role for ascorbate in collagen hydroxylation and broader dioxygenase biology, with clinical scurvy arising from ECM failure and secondarily from dysregulated hypoxia and epigenetic pathways in some contexts. (Gandhi 2023; Ramanujan 2024; Yue 2020) (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-8, alberts2025vitaminca pages 1-2)
- The 2024 observational bone study underscores that scurvy still presents with significant skeletal morbidity; systematic radiological assessment and prompt vitamin C repletion can mitigate complications. (Nefihancoro 2024) (nefihancoro2024analysisofthe pages 4-7)

## Relevant statistics and data (recent)
- Nefihancoro 2024 (Indonesia, 2020–2023; n=30): fatigue 86.7%, joint pain 73.3%, bleeding gums 60%, skin bleeding 53.3%; radiology showed osteoporosis and cortical thinning with severity; Spearman correlations: osteoporosis rho=0.495 (p=0.005), cortical thinning rho=0.394 (p=0.031). (https://doi.org/10.37275/bsm.v8i9.1066) (nefihancoro2024analysisofthe pages 4-7)
- Pediatric presentation patterns summarized across recent literature (limp/refusal to walk ~one-third; musculoskeletal complaints ~90% in children). (Gandhi 2023) (gandhi2023scurvyrediscoveringa pages 4-5)

## Gene/protein annotations with ontology terms
- HGNC: P4HA1/2/3; PLOD1/2/3; EGLN1/2/3; HIF1AN; TET1/2/3; DBH; PAM; TMLHE; BBOX1; SLC23A1/SLC23A2; SLC2A family. (ramanujan2024vitamincis pages 7-7, alberts2025vitaminca pages 1-2)
- GO processes: collagen biosynthetic process; extracellular matrix organization; wound healing; response to hypoxia; DNA demethylation; catecholamine biosynthetic process; peptide amidation; carnitine biosynthetic process. (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-7, alberts2025vitaminca pages 1-2)
- Cellular components: endoplasmic reticulum lumen; secretory vesicle; extracellular matrix; chromatin. (gandhi2023scurvyrediscoveringa pages 2-4, alberts2025vitaminca pages 1-2)

## Phenotype associations (HP terms; narrative mapping)
- Mucocutaneous bleeding (petechiae, ecchymoses), gingival hypertrophy/bleeding, poor wound healing, perifollicular hemorrhages; musculoskeletal pain/hemarthrosis; pediatric limp/refusal to walk; osteopenia/osteoporosis; cortical thinning; metaphyseal bands and periosteal reaction on imaging. Mechanistic links: collagen hydroxylation failure → ECM weakness and capillary fragility; impaired osteoid matrix. (gandhi2023scurvyrediscoveringa pages 4-5, nefihancoro2024analysisofthe pages 4-7)

## Cell type involvement (CL terms; narrative mapping)
- Fibroblasts (dermal ECM); endothelial cells (capillary walls); osteoblasts and chondrocytes (bone/growth plate matrix); immune dendritic cells (ascorbate-dependent TET reprogramming). (gandhi2023scurvyrediscoveringa pages 4-5, ramanujan2024vitamincis pages 7-8)

## Anatomical locations (UBERON; narrative mapping)
- Skin, gingiva, bone, epiphyseal (growth) plate, gastrointestinal mucosa. (gandhi2023scurvyrediscoveringa pages 4-5, gandhi2023scurvyrediscoveringa pages 1-2)

## Chemical entities (CHEBI; narrative mapping)
- L‑ascorbate, dehydroascorbic acid (DHA), dopamine, norepinephrine, carnitine. (gandhi2023scurvyrediscoveringa pages 2-4, lu2023scurvyina pages 2-3)

## Transport and tissue distribution
- Active intestinal uptake and renal handling are saturable; dehydroascorbic acid can “passively penetrate cellular membranes” and is preferentially taken up by erythrocytes and leukocytes (DHA → ascorbate intracellular reduction). SLC23A1/SLC23A2 (SVCT1/2) underlie systemic/tissue accumulation; decreased plasma ascorbate with compensatory changes in SLC23A1/2 expression is observed in disease states, underscoring reliance on these transporters. (Gandhi 2023; Ramanujan 2024; Linowiecka 2024, Sci Rep, Mar 2024; doi:10.1038/s41598-024-56326-5; https://doi.org/10.1038/s41598-024-56326-5) (gandhi2023scurvyrediscoveringa pages 2-4, ramanujan2024vitamincis pages 7-8, ramanujan2024vitamincis pages 7-7)

## References with URLs and dates (selected)
- Gandhi M et al. Scurvy: Rediscovering a Forgotten Disease. Diseases. May 2023. doi:10.3390/diseases11020078. https://doi.org/10.3390/diseases11020078 (gandhi2023scurvyrediscoveringa pages 1-2, gandhi2023scurvyrediscoveringa pages 2-4, gandhi2023scurvyrediscoveringa pages 4-5)
- Lu R-L et al. Scurvy in a young man: a rare case report. Front Nutr. Oct 2023. doi:10.3389/fnut.2023.1265334. https://doi.org/10.3389/fnut.2023.1265334 (lu2023scurvyina pages 2-3)
- Nefihancoro UH, Faisal R. Analysis of the Role of Vitamin C Hypovitaminosis in Scurvy on Bone Health. Bioscientia Medicina. Jun 2024. doi:10.37275/bsm.v8i9.1066. https://doi.org/10.37275/bsm.v8i9.1066 (nefihancoro2024analysisofthe pages 4-7)
- Ramanujan S et al. Vitamin C: Is it Relevant or Obsolete in the Modern Era? Curr Pediatr Rep. May 2024. doi:10.1007/s40124-024-00315-9. https://doi.org/10.1007/s40124-024-00315-9 (ramanujan2024vitamincis pages 7-8, ramanujan2024vitamincis pages 7-7)
- Yue X, Rao A. TET family dioxygenases and the TET activator vitamin C in immune responses and cancer. Blood. Sep 2020. doi:10.1182/blood.2019004158. https://doi.org/10.1182/blood.2019004158 (alberts2025vitaminca pages 1-2)
- Morante‑Palacios O et al. Vitamin C enhances NF‑κB‑driven epigenomic reprogramming… Nucleic Acids Res. Oct 2022. doi:10.1093/nar/gkac941. https://doi.org/10.1093/nar/gkac941 (ramanujan2024vitamincis pages 7-8)
- Fandrey J et al. Regulating cellular oxygen sensing by hydroxylation. Cardiovasc Res. Sep 2006. doi:10.1016/j.cardiores.2006.05.005. https://doi.org/10.1016/j.cardiores.2006.05.005 (ramanujan2024vitamincis pages 7-7)
- Plevin D, Galletly C. The neuropsychiatric effects of vitamin C deficiency: a systematic review. BMC Psychiatry. Jun 2020. doi:10.1186/s12888-020-02730-w. https://doi.org/10.1186/s12888-020-02730-w (gandhi2023scurvyrediscoveringa pages 4-5)

Notes on evidence strength and recency: We prioritized 2023–2024 clinical and review literature for modern presentations and radiologic skeletal data (Gandhi 2023; Lu 2023; Nefihancoro 2024; Ramanujan 2024). Mechanistic underpinnings referencing ascorbate’s enzymology and transporter biology are supported by these recent reviews and by established mechanistic reviews on HIF/TET dioxygenases (Fandrey 2006; Yue 2020; Morante‑Palacios 2022). Where possible, we included direct quotations for key mechanistic claims and provided DOI/URL and publication dates. (gandhi2023scurvyrediscoveringa pages 2-4, nefihancoro2024analysisofthe pages 4-7, ramanujan2024vitamincis pages 7-8, alberts2025vitaminca pages 1-2, ramanujan2024vitamincis pages 7-7)

References

1. (gandhi2023scurvyrediscoveringa pages 1-2): Mustafa Gandhi, Omar Elfeky, Hamza Ertugrul, Harleen Kaur Chela, and Ebubekir Daglilar. Scurvy: rediscovering a forgotten disease. Diseases, 11:78, May 2023. URL: https://doi.org/10.3390/diseases11020078, doi:10.3390/diseases11020078. This article has 82 citations and is from a poor quality or predatory journal.

2. (gandhi2023scurvyrediscoveringa pages 2-4): Mustafa Gandhi, Omar Elfeky, Hamza Ertugrul, Harleen Kaur Chela, and Ebubekir Daglilar. Scurvy: rediscovering a forgotten disease. Diseases, 11:78, May 2023. URL: https://doi.org/10.3390/diseases11020078, doi:10.3390/diseases11020078. This article has 82 citations and is from a poor quality or predatory journal.

3. (ramanujan2024vitamincis pages 7-7): Suruchi Ramanujan, Sanu Yadav, Andrea Adler, Sara Bewley, and Kadakkal Radhakrishnan. Vitamin c: is it relevant or obsolete in the modern era? Current Pediatrics Reports, 12:35-43, May 2024. URL: https://doi.org/10.1007/s40124-024-00315-9, doi:10.1007/s40124-024-00315-9. This article has 6 citations.

4. (gandhi2023scurvyrediscoveringa pages 4-5): Mustafa Gandhi, Omar Elfeky, Hamza Ertugrul, Harleen Kaur Chela, and Ebubekir Daglilar. Scurvy: rediscovering a forgotten disease. Diseases, 11:78, May 2023. URL: https://doi.org/10.3390/diseases11020078, doi:10.3390/diseases11020078. This article has 82 citations and is from a poor quality or predatory journal.

5. (lu2023scurvyina pages 2-3): Rui-Ling Lu, Jie-Wen Guo, Bao-dong Sun, Yu-Lan Chen, and Dong-Zhou Liu. Scurvy in a young man: a rare case report. Frontiers in Nutrition, Oct 2023. URL: https://doi.org/10.3389/fnut.2023.1265334, doi:10.3389/fnut.2023.1265334. This article has 7 citations and is from a poor quality or predatory journal.

6. (alberts2025vitaminca pages 1-2): Adina Alberts, Elena-Theodora Moldoveanu, Adelina-Gabriela Niculescu, and Alexandru Mihai Grumezescu. Vitamin c: a comprehensive review of its role in health, disease prevention, and therapeutic potential. Molecules, 30:748, Feb 2025. URL: https://doi.org/10.3390/molecules30030748, doi:10.3390/molecules30030748. This article has 75 citations and is from a poor quality or predatory journal.

7. (nefihancoro2024analysisofthe pages 4-7): Udi Heru Nefihancoro and Rachmad Faisal. Analysis of the role of vitamin c hypovitaminosis in scurvy on bone health: a single center observational study at dr. moewardi general hospital, surakarta, indonesia. Bioscientia Medicina : Journal of Biomedicine and Translational Research, 8:4894-4902, Jun 2024. URL: https://doi.org/10.37275/bsm.v8i9.1066, doi:10.37275/bsm.v8i9.1066. This article has 0 citations.

8. (ramanujan2024vitamincis pages 7-8): Suruchi Ramanujan, Sanu Yadav, Andrea Adler, Sara Bewley, and Kadakkal Radhakrishnan. Vitamin c: is it relevant or obsolete in the modern era? Current Pediatrics Reports, 12:35-43, May 2024. URL: https://doi.org/10.1007/s40124-024-00315-9, doi:10.1007/s40124-024-00315-9. This article has 6 citations.