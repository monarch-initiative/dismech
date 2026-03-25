---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-30T19:25:24.811871'
end_time: '2026-01-30T19:30:43.998522'
duration_seconds: 319.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypochondroplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Hypochondroplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypochondroplasia**.
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
- **Disease Name:** Hypochondroplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Hypochondroplasia**.
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
- Identify and synthesize the most recent primary and review literature on hypochondroplasia (HCH) pathophysiology (completed).
- Extract and organize core mechanisms centered on FGFR3 gain-of-function and downstream pathways in growth-plate biology.
- Map key molecular players, cell types, and anatomical sites with ontology-style annotations.
- Summarize biological processes (GO) and cellular components involved.
- Describe disease progression from molecular trigger to clinical phenotype.
- Include phenotypic spectrum and mechanistic links.
- Add current applications/therapeutics, diagnostics, and recent data, prioritizing 2023–2024 sources.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Hypochondroplasia (HCH)
- MONDO ID: [not confirmed]
- Category: Mendelian (autosomal dominant)

1) Core Pathophysiology: current understanding
- Primary mechanism: Hypochondroplasia is driven by activating (gain-of-function) missense variants in FGFR3, most commonly p.Asn540Lys, which “constitutively” activate the receptor tyrosine kinase and disengage its autoinhibitory brake, making FGFR3 a stronger negative regulator of bone growth (JCI Insight, Jun 2023; DOI: 10.1172/jci.insight.168796) (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2). In vivo, FGFR3 activation perturbs the growth plate and broader skeleton leading to short-limbed dwarfism, cranial base involvement, and altered bone mineralization (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- Dysregulated signaling pathways: Downstream of mutant FGFR3, Ras–MAPK/ERK signaling is over-activated in growth-plate chondrocytes, with contributions from STAT signaling; the imbalance inhibits chondrocyte proliferation and differentiation and impairs endochondral ossification (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6).
- Affected cellular processes: In the growth plate, there is reduced chondrocyte proliferation, altered hypertrophic differentiation, and delayed cartilage-to-bone transition; in bone, osteoblast and osteocyte function and mineralization are disrupted, producing decreased trabecular BMD and age-related increases in cortical BMD with reduced toughness (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).

Direct supporting quotes
- “Hypochondroplasia (HCH) is a mild dwarfism caused by missense mutations in fibroblast growth factor receptor 3 (FGFR3), with the majority of cases resulting from a heterozygous p.Asn540Lys gain-of-function mutation.” (JCI Insight, 2023-06; https://doi.org/10.1172/jci.insight.168796) (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2)
- “Fgfr3Asn534Lys/+ mice exhibited progressive dwarfism and impairment of the synchondroses of the cranial base, resulting in defective formation of the foramen magnum… Trabecular bone mineral density… was decreased, but cortical BMD increased with age…” (JCI Insight, 2023-06; https://doi.org/10.1172/jci.insight.168796) (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3)

2) Key molecular players
- Genes/Proteins (HGNC): FGFR3 (HGNC:3689; activating variants drive HCH); MAPK cascade (ERK1/2: MAPK3/MAPK1); STAT family (notably STAT1 downstream of FGFR3) (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6).
- Chemical entities and modulators: CNP (NPPC) and NPR2/GC-B signaling antagonize FGFR3–MAPK, providing a mechanistic rationale for CNP analog therapy (vosoritide) developed in related FGFR3 dysplasia; selective/pan-FGFR tyrosine kinase inhibitors (e.g., infigratinib/BGJ398) have shown preclinical benefits in FGFR3-driven models; meclozine has been reported to dampen ERK1/2 signaling in preclinical contexts (chen2017moleculartherapeuticstrategies pages 8-9, chen2017moleculartherapeuticstrategies pages 4-6).
- Cell types (CL): Growth-plate chondrocytes (CL:0000138) are primary targets; osteoblasts (CL:0000062) and osteocytes (CL:0000137) show altered gene expression/mineralization phenotypes in models (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- Anatomical locations (UBERON): Growth plate (UBERON:0003860), cranial base synchondroses (e.g., spheno-occipital synchondrosis, UBERON:0010315), foramen magnum (UBERON:0001680), vertebral body (UBERON:0002371), long bone cortex (UBERON:0002476), trabecular bone (UBERON:0002481) (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).

3) Biological processes (for GO annotation)
- Dysregulated processes include: fibroblast growth factor receptor signaling; MAPK cascade; negative regulation of chondrocyte proliferation; regulation of chondrocyte differentiation and hypertrophy; endochondral ossification; bone mineralization; osteoblast differentiation and osteocyte-mediated bone maintenance (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5, chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6).

4) Cellular components
- Key cellular locations: plasma membrane (FGFR3 receptor); cytoplasm (MAPK/ERK signaling); nucleus (STAT-mediated transcriptional effects); extracellular matrix of cartilage and bone (endochondral ossification and mineralization) (chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).

5) Disease progression: molecular-to-clinical sequence
- Trigger: Heterozygous FGFR3 gain-of-function mutations (e.g., p.Asn540Lys) cause constitutive receptor autophosphorylation and hyperactive signaling (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2).
- Early growth-plate effects: Excess FGFR3 signaling via MAPK/ERK and STAT reduces chondrocyte proliferation and alters differentiation/hypertrophy, impairing endochondral ossification and longitudinal bone growth (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 1-2).
- Cranial base and spine: Premature fusion/impairment of cranial base synchondroses reduces skull base length and foramen magnum area; vertebral bodies shorten and interpedicular distance narrows (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- Bone tissue remodeling/mineralization: Decreased trabecular bone volume/BMD and age-related increased cortical BMD with reduced toughness arise from altered osteoblast/osteocyte biology and matrix mineralization; biomechanics are compromised (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- Clinical consequence: Disproportionate short stature (“mild dwarfism”), foramen magnum stenosis risk, vertebral/spinal features, and potential fragility due to microarchitectural changes (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).

6) Phenotypic manifestations and mechanistic links
- Short stature with limb disproportion (milder than achondroplasia) stems from suppressed chondrocyte proliferation and impaired endochondral ossification (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 1-2).
- Cranial base/foramen magnum involvement results from synchondrosis dysfunction; mechanical stenosis risk follows skull base shortening (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- Axial skeleton: reduced vertebral body length and interpedicular distance; trabecular bone deficits and mechanical weakness link to altered osteoblast/osteocyte function and bone matrix properties (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).

7) Current applications and real-world implementations (2023–2024 prioritized)
- Preclinical-to-clinical therapeutic rationale: Antagonizing FGFR3–MAPK signaling via CNP/NPR2 pathway (e.g., CNP analogs such as vosoritide) is mechanistically justified; tyrosine kinase inhibition (e.g., BGJ398/infigratinib) improved outcomes in FGFR3-driven models, though pediatric safety requires caution (J Mol Med, Oct 2017; DOI: 10.1007/s00109-017-1602-9; JCI Insight, Jun 2023; DOI: 10.1172/jci.insight.168796) (chen2017moleculartherapeuticstrategies pages 8-9, chen2017moleculartherapeuticstrategies pages 4-6, loisay2023hypochondroplasiagainoffunctionmutation pages 20-21).
- Clinical monitoring implications from 2023 model data: The 2023 HCH mouse study highlights decreased trabecular BMD and paradoxical cortical changes with reduced toughness, suggesting the need to monitor BMD/microarchitecture and potential fracture risk as HCH patients age (JCI Insight, Jun 2023; https://doi.org/10.1172/jci.insight.168796) (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- Diagnostic genomics: FGFR3 testing is central to confirming HCH; mechanistic insights emphasize identifying activating variants for precise counseling and potential trial eligibility (supported mechanistically by FGFR3 GOF biology) (chen2017moleculartherapeuticstrategies pages 1-2).

8) Expert opinions and analysis
- Authoritative consensus places FGFR3 as a negative regulator of growth-plate chondrogenesis; activating variants in the receptor lead to a spectrum from HCH to achondroplasia and lethal dysplasias depending on allele strength and pathway output. Reviews emphasize the antagonism between FGFR3–MAPK and CNP–NPR2–cGMP signaling as a tractable therapeutic axis, with practical considerations around systemic kinase inhibition in children (J Mol Med 2017; DOI: 10.1007/s00109-017-1602-9) (chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6). The 2023 HCH mouse model underscores the breadth of skeletal involvement, including cranial base and bone quality, refining clinical surveillance priorities (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).

9) Relevant statistics and data (recent)
- In the HCH mouse model, lumbar vertebrae exhibited an “18% reduction in bone volume per tissue volume (BV/TV),” “15% decrease in trabecular thickness,” “7% reduction in BMD,” and mechanical deficits including “22% reduction in maximal load” and “34% decrease in stiffness,” linking FGFR3 activation to biomechanical vulnerability (JCI Insight, Jun 2023; https://doi.org/10.1172/jci.insight.168796) (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5).
- The same model documented decreased trabecular BMD across long bones and vertebrae with age-related increase in cortical BMD and reduced toughness, suggesting a complex remodeling phenotype relevant to long-term outcomes (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).

Ontology-style annotations
- Gene/Protein annotations (HGNC): FGFR3 (HGNC:3689); MAPK1 (HGNC:6871), MAPK3 (HGNC:6877); STAT1 (HGNC:11362) (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 1-2).
- Biological processes (GO terms, names): fibroblast growth factor receptor signaling; MAPK cascade; regulation of chondrocyte proliferation; chondrocyte differentiation; endochondral ossification; bone mineralization (chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).
- Cellular components (GO names): plasma membrane; cytoplasm; nucleus; extracellular matrix (chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6).
- Cell types (CL): growth-plate chondrocyte (CL:0000138); osteoblast (CL:0000062); osteocyte (CL:0000137) (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).
- Anatomical locations (UBERON): growth plate (UBERON:0003860); cranial base synchondrosis (UBERON:0010315); foramen magnum (UBERON:0001680); vertebral body (UBERON:0002371); long bone cortex (UBERON:0002476); trabecular bone (UBERON:0002481) (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3).
- Chemical entities (examples): CNP analog (vosoritide); pan-FGFR inhibitors (infigratinib/BGJ398); meclozine (chen2017moleculartherapeuticstrategies pages 8-9, chen2017moleculartherapeuticstrategies pages 4-6, loisay2023hypochondroplasiagainoffunctionmutation pages 20-21).

Embedded mapping table
| Category | Item | Identifier | Notes/Role | Primary Evidence (PMID/DOI) |
|---|---|---|---|---|
| Genes/Proteins | FGFR3 | HGNC:3689 | Causative gain-of-function mutations in HCH; constitutive RTK activation alters growth-plate signaling | https://doi.org/10.1172/jci.insight.168796; https://doi.org/10.1007/s00109-017-1602-9 (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 8-9) |
| Genes/Proteins | MAPK pathway (ERK1/2; MAPK1/MAPK3) | MAPK1 (HGNC:6871), MAPK3 (HGNC:6877) | Principal downstream cascade (FGF→Ras→MAPK/ERK) mediating inhibition of chondrocyte proliferation/differentiation | https://doi.org/10.1172/jci.insight.168796; https://doi.org/10.1007/s00109-017-1602-9 (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 8-9) |
| Genes/Proteins | STAT1 | HGNC:11362 | STAT family activation reported downstream of activated FGFR3, influences chondrocyte proliferation signals | https://doi.org/10.1172/jci.insight.168796; https://doi.org/10.1007/s00109-017-1602-9 (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, chen2017moleculartherapeuticstrategies pages 8-9) |
| Receptors/Modulators | NPR2 / GC-B | HGNC:7950 | Receptor for CNP; CNP–NPR2 signaling antagonizes FGFR3-MAPK to promote endochondral growth | https://doi.org/10.1007/s00109-017-1602-9 (chen2017moleculartherapeuticstrategies pages 8-9) |
| Receptors/Modulators | CNP (NPPC) | NPPC (HGNC:7961) | Endogenous peptide that counteracts FGFR3 effects; therapeutic CNP analogs developed (e.g., vosoritide) | https://doi.org/10.1007/s00109-017-1602-9 (chen2017moleculartherapeuticstrategies pages 8-9) |
| Small-molecule / biologic modulators | Vosoritide (CNP analog) | (no CHEBI id shown) | CNP analog in clinical development/approval for FGFR3-related short stature (ACH); mechanistic rationale to oppose MAPK signaling | https://doi.org/10.1007/s00109-017-1602-9 (chen2017moleculartherapeuticstrategies pages 8-9) |
| Small-molecule / biologic modulators | Pan-FGFR inhibitors (e.g., NVP-BGJ398 / infigratinib) | — | TKIs that inhibit FGFR3 kinase activity; preclinical/repurposing evidence improves FGFR3-driven growth deficits | https://doi.org/10.1007/s00109-017-1602-9; https://doi.org/10.1172/jci.insight.168796 (chen2017moleculartherapeuticstrategies pages 8-9, loisay2023hypochondroplasiagainoffunctionmutation pages 20-21) |
| Small-molecule / biologic modulators | Meclozine | — | Oral drug repurposing candidate reported to inhibit ERK1/2 phosphorylation and rescue growth-plate phenotypes in models | https://doi.org/10.1007/s00109-017-1602-9 (chen2017moleculartherapeuticstrategies pages 8-9) |
| Cell types | Growth plate chondrocyte | CL:0000138 | Primary cellular target where FGFR3 GOF reduces proliferation/differentiation and impairs endochondral ossification | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2) |
| Cell types | Osteoblast | CL:0000062 | Affected secondarily by dysregulated cartilage-to-bone transition; altered osteoblast gene expression and mineralization observed | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5) |
| Cell types | Osteocyte | CL:0000137 | Osteocyte lacunar anomalies reported in FGFR3 GOF mouse model, implicating bone matrix/maintenance defects | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3) |
| Cell types | Osteoclast | CL:0000092 | Bone remodeling compartment altered downstream of FGFR3-driven changes in osteoblast/osteocyte signaling | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 20-21) |
| Anatomical structures | Growth plate (epiphyseal plate) | UBERON:0003860 | Site of endochondral ossification disrupted in HCH leading to shortened long bones | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2) |
| Anatomical structures | Cranial base synchondrosis (spheno-occipital) | UBERON:0010315 | Premature fusion / synchondrosis defects reduce skull base length and foramen magnum area | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5) |
| Anatomical structures | Foramen magnum | UBERON:0001680 | Clinically relevant site affected by skull base shortening; risk of stenosis in FGFR3 disorders | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5) |
| Anatomical structures | Vertebral body | UBERON:0002371 | Vertebral shortening and reduced interpedicular distance reported; biomechanical weakening observed | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5) |
| Anatomical structures | Long bone cortex | UBERON:0002476 | Altered cortical BMD (age-related increases) with reduced toughness described in FGFR3 GOF mice | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3) |
| Anatomical structures | Trabecular bone | UBERON:0002481 | Decreased trabecular BMD and BV/TV in FGFR3 GOF models; contributes to fracture risk hypothesis | https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5) |


*Table: Table mapping genes, pathways, modulators, cell types and anatomical sites relevant to hypochondroplasia with ontology identifiers and primary evidence DOIs; useful for building structured disease annotations and linking mechanistic claims to source documents. (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 20-21, chen2017moleculartherapeuticstrategies pages 8-9, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5)*

Evidence items (with publication details)
- Loisay L, et al. Hypochondroplasia gain-of-function mutation in FGFR3 causes defective bone mineralization in mice. JCI Insight. 2023-06. DOI: 10.1172/jci.insight.168796; URL: https://doi.org/10.1172/jci.insight.168796 (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5, loisay2023hypochondroplasiagainoffunctionmutation pages 20-21).
- Chen J, et al. Molecular therapeutic strategies for FGFR3 gene-related skeletal dysplasia. Journal of Molecular Medicine. 2017-10. DOI: 10.1007/s00109-017-1602-9; URL: https://doi.org/10.1007/s00109-017-1602-9 (chen2017moleculartherapeuticstrategies pages 8-9, chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6).

Limitations of current evidence set
- The mechanistic synthesis above is strongly supported by the 2023 HCH mouse model and an authoritative FGFR3 review. Additional 2023–2024 clinical studies (e.g., on cardiometabolic risk or AI-driven assessments in skeletal dysplasias) were identified in search but did not yield extractable mechanistic evidence in this run; thus, claims are focused on directly supported FGFR3–HCH biology and therapeutic rationale (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2, loisay2023hypochondroplasiagainoffunctionmutation pages 2-3, loisay2023hypochondroplasiagainoffunctionmutation pages 3-5, chen2017moleculartherapeuticstrategies pages 8-9, chen2017moleculartherapeuticstrategies pages 1-2, chen2017moleculartherapeuticstrategies pages 4-6).

References

1. (loisay2023hypochondroplasiagainoffunctionmutation pages 1-2): Léa Loisay, Davide Komla-Ebri, Anne Morice, Yann Heuzé, Camille Viaut, Amélie de La Seiglière, Nabil Kaci, Danny Chan, Audrey Lamouroux, Geneviève Baujat, J.H. Duncan Bassett, Graham R. Williams, and Laurence Legeai-Mallet. Hypochondroplasia gain-of-function mutation in fgfr3 causes defective bone mineralization in mice. JCI Insight, Jun 2023. URL: https://doi.org/10.1172/jci.insight.168796, doi:10.1172/jci.insight.168796. This article has 9 citations and is from a domain leading peer-reviewed journal.

2. (loisay2023hypochondroplasiagainoffunctionmutation pages 2-3): Léa Loisay, Davide Komla-Ebri, Anne Morice, Yann Heuzé, Camille Viaut, Amélie de La Seiglière, Nabil Kaci, Danny Chan, Audrey Lamouroux, Geneviève Baujat, J.H. Duncan Bassett, Graham R. Williams, and Laurence Legeai-Mallet. Hypochondroplasia gain-of-function mutation in fgfr3 causes defective bone mineralization in mice. JCI Insight, Jun 2023. URL: https://doi.org/10.1172/jci.insight.168796, doi:10.1172/jci.insight.168796. This article has 9 citations and is from a domain leading peer-reviewed journal.

3. (loisay2023hypochondroplasiagainoffunctionmutation pages 3-5): Léa Loisay, Davide Komla-Ebri, Anne Morice, Yann Heuzé, Camille Viaut, Amélie de La Seiglière, Nabil Kaci, Danny Chan, Audrey Lamouroux, Geneviève Baujat, J.H. Duncan Bassett, Graham R. Williams, and Laurence Legeai-Mallet. Hypochondroplasia gain-of-function mutation in fgfr3 causes defective bone mineralization in mice. JCI Insight, Jun 2023. URL: https://doi.org/10.1172/jci.insight.168796, doi:10.1172/jci.insight.168796. This article has 9 citations and is from a domain leading peer-reviewed journal.

4. (chen2017moleculartherapeuticstrategies pages 1-2): Jia Chen, Jiaqi Liu, Yangzhong Zhou, Sen Liu, Gang Liu, Yuzhi Zuo, Zhihong Wu, Nan Wu, and Guixing Qiu. Molecular therapeutic strategies for fgfr3 gene-related skeletal dysplasia. Journal of Molecular Medicine, 95:1303-1313, Oct 2017. URL: https://doi.org/10.1007/s00109-017-1602-9, doi:10.1007/s00109-017-1602-9. This article has 9 citations.

5. (chen2017moleculartherapeuticstrategies pages 4-6): Jia Chen, Jiaqi Liu, Yangzhong Zhou, Sen Liu, Gang Liu, Yuzhi Zuo, Zhihong Wu, Nan Wu, and Guixing Qiu. Molecular therapeutic strategies for fgfr3 gene-related skeletal dysplasia. Journal of Molecular Medicine, 95:1303-1313, Oct 2017. URL: https://doi.org/10.1007/s00109-017-1602-9, doi:10.1007/s00109-017-1602-9. This article has 9 citations.

6. (chen2017moleculartherapeuticstrategies pages 8-9): Jia Chen, Jiaqi Liu, Yangzhong Zhou, Sen Liu, Gang Liu, Yuzhi Zuo, Zhihong Wu, Nan Wu, and Guixing Qiu. Molecular therapeutic strategies for fgfr3 gene-related skeletal dysplasia. Journal of Molecular Medicine, 95:1303-1313, Oct 2017. URL: https://doi.org/10.1007/s00109-017-1602-9, doi:10.1007/s00109-017-1602-9. This article has 9 citations.

7. (loisay2023hypochondroplasiagainoffunctionmutation pages 20-21): Léa Loisay, Davide Komla-Ebri, Anne Morice, Yann Heuzé, Camille Viaut, Amélie de La Seiglière, Nabil Kaci, Danny Chan, Audrey Lamouroux, Geneviève Baujat, J.H. Duncan Bassett, Graham R. Williams, and Laurence Legeai-Mallet. Hypochondroplasia gain-of-function mutation in fgfr3 causes defective bone mineralization in mice. JCI Insight, Jun 2023. URL: https://doi.org/10.1172/jci.insight.168796, doi:10.1172/jci.insight.168796. This article has 9 citations and is from a domain leading peer-reviewed journal.