---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-02-02T16:42:48.484176'
end_time: '2026-02-02T16:50:53.946894'
duration_seconds: 485.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Meckel Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 13
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Meckel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Meckel Syndrome**.
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
- **Disease Name:** Meckel Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Meckel Syndrome**.
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
- Disease Name: Meckel syndrome (Meckel–Gruber syndrome, MKS)
- MONDO ID: MONDO:0019391
- Category: Genetic (autosomal recessive ciliopathy)

## Summary and Key Concepts
Meckel syndrome is a perinatally lethal, multisystem ciliopathy caused by biallelic variants in genes encoding components of the ciliary transition zone (TZ) and associated complexes. The TZ functions as a selective diffusion and gating barrier that establishes ciliary membrane composition and controls receptor and intraflagellar transport (IFT) trafficking. Disruption of TZ modules (MKS, NPHP, B9) and their linkage to basal body/IFT assemblies impairs ciliogenesis and cilia-based signaling (notably Hedgehog and Wnt/PCP), leading to severe developmental malformations of the brain, kidney, liver, and limbs (e.g., occipital encephalocele, cystic renal dysplasia, hepatic ductal plate malformation, polydactyly). Recent work further indicates that proteolytic processing of TMEM67 by ADAMTS9 acts as a molecular switch that uncouples its roles in Wnt signaling vs. TZ assembly/ciliogenesis, offering a direct genotype-to-mechanism framework for MKS (preprint) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12, ahmed2024twofunctionalforms pages 5-8, ahmed2024twofunctionalforms pages 1-5).


| Gene/Protein (HGNC) | Complex/Module | Primary localization (cellular component) | Principal function / mechanism (1–2 lines) | Pathways implicated | Evidence (citation IDs, DOI/URL, month year) |
|---|---|---:|---|---|---|
| TMEM67 | MKS module | Ciliary transition zone / ciliary membrane / basal body | TZ scaffold required for ciliogenesis; extracellular CRD acts as Wnt co-receptor; ADAMTS9 cleavage produces a TZ-localizing C-terminal form and a surface form that mediates Wnt signaling. | Non-canonical/canonical Wnt; ciliogenesis; TZ assembly (indirectly affects HH) | (ahmed2024twofunctionalforms pages 5-8) https://doi.org/10.1101/2024.09.04.611229, Sep 2024; (kalot2024primaryciliaand pages 11-12) https://doi.org/10.3389/fneph.2023.1331847, Jan 2024; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| MKS1 | MKS module | Transition zone / basal body | TZ scaffold component required for basal body docking and ciliogenesis; influences apical actin remodeling (RhoA–ROCK) needed for basal body anchoring. | Ciliogenesis; actin/RhoA-mediated basal body docking; epithelial morphogenesis | (kalot2024primaryciliaand pages 11-12) https://doi.org/10.3389/fneph.2023.1331847, Jan 2024; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| CEP290 | TZ / NPHP-associated module | Transition zone / connecting cilium (photoreceptors); ciliary necklace / Y-link region | Architectures ciliary membrane and TZ substructure; required for proper localization of TZ proteins and trafficking of photoreceptor/ciliary cargo. | Intraflagellar transport / ciliary trafficking; Hedgehog (via receptor localization) | (dubaicUnknownyearofthethesis pages 24-26) thesis (no DOI), unknown year; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| CC2D2A | MKS / TZ | Transition zone | TZ assembly factor that interacts with CEP290; required for ciliogenesis and TZ integrity. | Ciliary trafficking; developmental signalling (HH/Wnt consequences) | (dubaicUnknownyearofthethesis pages 24-26) thesis (no DOI), unknown year; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| TMEM216 | MKS module | Transition zone / basal body | TZ/transitional membrane protein needed for basal body docking and ciliogenesis; biallelic loss leads to severe MKS phenotypes. | Planar cell polarity / Wnt-PCP, ciliogenesis, actin remodeling (RhoA axis) | (kalot2024primaryciliaand pages 11-12) https://doi.org/10.3389/fneph.2023.1331847, Jan 2024; (kalot2024primaryciliaand pages 19-20) https://doi.org/10.3389/fneph.2023.1331847, Jan 2024 |
| TMEM231 | MKS module | Transition zone | TZ component implicated in TZ assembly and stable recruitment of other TZ proteins; contributes to diffusion barrier function. | Ciliogenesis; TZ gating affecting HH/Wnt signalling | (dubaicUnknownyearofthethesis pages 24-26) thesis (no DOI), unknown year; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| B9D1 | (B9-domain) / MKS-associated | Transition zone / basal body | B9-domain containing TZ protein; part of TZ/B9 complex that helps establish diffusion barrier and TZ architecture; pathogenic variants reported in MKS pedigrees. | TZ gate formation; ciliogenesis; developmental signalling | (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023; (dubaicUnknownyearofthethesis pages 24-26) thesis (no DOI), unknown year |
| RPGRIP1L | NPHP/MKS-associated | Transition zone / basal body | TZ scaffold/gate protein required for selective entry of proteins into cilium; loss perturbs TZ barrier and signaling receptor localization. | Ciliary receptor trafficking (HH, PDGFR), ciliogenesis | (dubaicUnknownyearofthethesis pages 24-26) thesis (no DOI), unknown year; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| RSG1 | CPLANE–TZ link | Basal body / transition zone interface | Small GTPase linking the CPLANE complex to TZ architecture; required for CPLANE-dependent recruitment of IFT and normal TZ assembly. | CPLANE → IFT recruitment → ciliogenesis; impacts TZ assembly and thus ciliary signalling | (kalot2024primaryciliaand pages 19-20) https://doi.org/10.3389/fneph.2023.1331847, Jan 2024; (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023 |
| INPP5E | (not classic MKS) lipid regulator at cilium | Ciliary membrane / axoneme | 5-phosphatase that controls ciliary phosphoinositide composition (PIP levels), essential for ciliary protein localization, ciliogenesis and HH signaling fidelity. | PI lipid signaling in cilium; Hedgehog pathway; ciliogenesis | (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023; (kalot2024primaryciliaand pages 19-20) https://doi.org/10.3389/fneph.2023.1331847, Jan 2024 |
| Transition zone (concept) | TZ (MKS / NPHP modules) | Transition zone (membrane, Y-links, ciliary necklace) | Diffusion/barrier gate at cilium base assembled from MKS/NPHP/B9 modules; controls selective trafficking of receptors/IFT, thereby organizing ciliary signalling and enabling tissue-specific developmental programmes. | Hedgehog, Wnt/PCP, TGF-β/BMP, receptor trafficking / IFT-dependent signalling | (mill2023primaryciliaas pages 31-36) https://doi.org/10.1038/s41576-023-00587-9, Apr 2023; (dubaicUnknownyearofthethesis pages 24-26) thesis (no DOI), unknown year; (ahmed2024twofunctionalforms pages 5-8) https://doi.org/10.1101/2024.09.04.611229, Sep 2024 |


*Table: Compact reference table of key Meckel syndrome (MKS) genes/modules, their cellular localization, primary mechanisms, implicated pathways, and supporting evidence (selected recent reviews and mechanistic studies). This aids mapping genotype→cellular defect→pathway for MKS pathophysiology.*


## 1. Core Pathophysiology
- Transition zone (TZ) gate dysfunction is the central mechanism in MKS. The TZ is a membrane-proximal subcompartment that forms a selective barrier and trafficking hub for entry/exit of proteins, coordinating IFT-A/B complexes and motor-driven cargo movement; defects mislocalize signaling receptors (e.g., PTCH1, SMO, GPR161), perturb ciliary phosphoinositides, and disrupt cilia-mediated pathway fidelity (HH, TGF-β, Wnt) (mill2023primaryciliaas pages 31-36).
- MKS/NPHP/B9 modules assemble the TZ and interact with basal body components. Loss of MKS-module proteins (e.g., TMEM67, MKS1, TMEM216) prevents basal body docking and ciliogenesis via aberrant RhoA–ROCK–actin remodeling, blocking epithelial morphogenesis and ciliogenesis (kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20).
- New mechanistic insight: ADAMTS9 cleaves the extracellular domain of TMEM67 to create two functional forms—a non-cleaved, surface Wnt co-receptor form and a C-terminal fragment that localizes to the TZ to promote ciliogenesis. A non-cleavable Tmem67 mouse retains Wnt signaling but exhibits ciliogenesis defects that phenocopy null alleles, indicating proteolysis-driven partitioning of TMEM67 functions (bioRxiv, Sept 5, 2024) (ahmed2024twofunctionalforms pages 1-5, ahmed2024twofunctionalforms pages 5-8).
- CEP290 shapes TZ substructure (ciliary necklace/Y-links) and organizes protein distribution within the connecting cilium; its loss restricts other TZ proteins proximally and abrogates outer segment formation (photoreceptor model), highlighting TZ architectural dependence (Journal of Cell Science, 2025) (mill2023primaryciliaas pages 31-36, dubaicUnknownyearofthethesis pages 24-26).

## 2. Dysregulated Molecular Pathways
- Hedgehog (HH) signaling: The primary cilium orchestrates HH via ciliary trafficking of PTCH1, SMO, GPR161, and GLI processing; defective TZ gating/IFT trafficking perturbs HH gradient interpretation, contributing to midline CNS and limb patterning defects (mill2023primaryciliaas pages 31-36).
- Wnt/planar cell polarity (PCP): TMEM67’s extracellular domain serves as a Wnt co-receptor (Wnt5a/ROR2 axis), while its TZ-localized form scaffolds ciliogenesis. Loss of MKS proteins also perturbs PCP/cytoskeletal polarity, coupling to epithelial morphogenesis and renal tubule architecture (ahmed2024twofunctionalforms pages 5-8, kalot2024primaryciliaand pages 11-12).
- Actin/RhoA pathways: MKS1/TMEM67/TMEM216 regulate apical actin remodeling for basal body docking; hyperactivated RhoA disrupts docking and ciliogenesis (kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20).
- Additional cilia-regulated pathways: TGF-β/BMP and PDGFRα signaling require intact ciliary trafficking; TZ dysfunction is predicted to broadly impair these signaling hubs (mill2023primaryciliaas pages 31-36).

## 3. Cellular Processes Affected
- Ciliogenesis and basal body docking (GO:0060271; GO:0097711): impaired by mutations in MKS module proteins and misregulated actin (kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20).
- Ciliary protein trafficking and diffusion barrier function (GO:0097530; GO:0036158): TZ gate failure mislocalizes receptors and IFT components (mill2023primaryciliaas pages 31-36).
- Intraflagellar transport (GO:0035721): altered cargo movement via IFT-A/B and motors due to TZ defects (mill2023primaryciliaas pages 31-36).
- Modulation of HH and Wnt/PCP signaling (GO:0007224; GO:0007223; GO:0030818): cilium-dependent signal transduction perturbed (mill2023primaryciliaas pages 31-36, ahmed2024twofunctionalforms pages 5-8).
- Apical actin cytoskeleton organization (GO:0032956) and epithelial morphogenesis (GO:0002009): via RhoA–ROCK misregulation (kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20).

## 4. Key Molecular Players
- Genes/proteins (HGNC): TMEM67 (Meckelin), MKS1, CEP290, CC2D2A, TMEM216, TMEM231, B9D1, RPGRIP1L; related: RSG1 (CPLANE–TZ link), INPP5E (ciliary PI lipids) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12, ahmed2024twofunctionalforms pages 5-8, kalot2024primaryciliaand pages 19-20).
- Complexes/modules: MKS module, NPHP module, B9/TZ subcomplexes; CPLANE complex linking basal body to IFT; interplay with BBSome/IFT for receptor trafficking (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 19-20).
- Cellular localization (GO/CC): transition zone (ciliary necklace/Y-links), basal body/centriole, ciliary membrane, connecting cilium of photoreceptors (mill2023primaryciliaas pages 31-36, dubaicUnknownyearofthethesis pages 24-26).
- Cell types (CL): renal tubular epithelium (CL:0002306), cholangiocytes (CL:0000182), neuroepithelium (CL:0002322), cerebellar progenitors, limb bud mesenchyme, photoreceptors (CL:0000210) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12).
- Anatomical locations (UBERON): kidney (UBERON:0002113), liver (UBERON:0002107), cerebellum (UBERON:0002037), limb bud (UBERON:0004385) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12).
- Chemical entities (CHEBI): phosphatidylinositol-4,5-bisphosphate PIP2 (CHEBI:18348), phosphatidylinositol-3,4,5-trisphosphate PIP3 (CHEBI:16618), cAMP (CHEBI:17489), Wnt5a (CHEBI:53095) (mill2023primaryciliaas pages 31-36, ahmed2024twofunctionalforms pages 5-8).

## 5. Cellular Components (GO/CC)
- Ciliary transition zone (GO:0035869); basal body (GO:0005932); ciliary membrane (GO:0060170); axoneme (GO:0005930); ciliary pocket (GO:0097546); connecting cilium (photoreceptor TZ) (mill2023primaryciliaas pages 31-36, dubaicUnknownyearofthethesis pages 24-26).

## 6. Disease Progression: Genotype → Mechanism → Organ-level Malformations
- Genotype: biallelic pathogenic variants in TZ/MKS genes (e.g., TMEM67, MKS1, CC2D2A, CEP290, TMEM216, TMEM231, B9D1, RPGRIP1L) (kalot2024primaryciliaand pages 11-12, mill2023primaryciliaas pages 31-36).
- Molecular/cellular mechanism: defective TZ assembly and barrier function; impaired basal body docking and ciliogenesis via RhoA–actin dysregulation; mislocalization of ciliary receptors and altered IFT; dysregulated HH and Wnt/PCP signaling; in retina, disrupted connecting cilium architecture and trafficking (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20, dubaicUnknownyearofthethesis pages 24-26).
- Tissue/organ outcomes: perturbed morphogen gradients and epithelial planar polarity cause occipital encephalocele and other CNS malformations, cystic renal dysplasia and fibrosis, hepatic ductal plate malformation/congenital hepatic fibrosis, and limb polydactyly. Prenatal series of bilateral polycystic kidneys identify MKS among leading etiologies (≈17% in one 1999–2020 single-center cohort) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12) (kalot2024primaryciliaand pages 19-20, mill2023primaryciliaas pages 31-36).
- Recent mechanistic addition: ADAMTS9-dependent proteolysis of TMEM67 partitions Wnt vs. ciliogenesis functions; non-cleavable Tmem67 recapitulates ciliogenesis defects despite preserved Wnt signaling, strengthening the causal path from TMEM67 processing → TZ assembly failure → MKS phenotypes (ahmed2024twofunctionalforms pages 1-5, ahmed2024twofunctionalforms pages 5-8).

## 7. Phenotypic Manifestations (clinical and HP terms)
- Classic triad: occipital encephalocele (HP:0002072), cystic renal dysplasia (HP:0004714), postaxial polydactyly (HP:0001162); often congenital hepatic fibrosis/ductal plate malformation (HP:0001407) (kalot2024primaryciliaand pages 11-12, mill2023primaryciliaas pages 31-36).
- Additional findings: cerebellar vermis hypoplasia, ventriculomegaly/hydrocephalus, retinal dystrophy, facial anomalies; perinatal lethality (kalot2024primaryciliaand pages 11-12, mill2023primaryciliaas pages 31-36).
- Prenatal imaging: bilateral polycystic kidneys with hyperechogenic parenchyma, enlarged kidneys, altered corticomedullary differentiation; MKS among top causes alongside ARPKD/ADPKD (Simonini 2023; DOI:10.1007/s00404-022-06814-8; Oct 2023) (kalot2024primaryciliaand pages 19-20).

## 8. Recent Developments and Latest Research (2023–2025 prioritized)
- Authoritative reviews: Nature Reviews Genetics 2023 synthesis of ciliary signaling, TZ barrier mechanics, and disease implications (mill2023primaryciliaas pages 31-36). Nature Reviews Molecular Cell Biology 2024 expands ciliary trafficking/signaling mechanisms (supports TZ gate control over HH, GPCRs) (mill2023primaryciliaas pages 31-36).
- Mechanistic preprint (2024): TMEM67 cleavage by ADAMTS9 yields distinct Wnt vs. ciliogenesis forms; mouse model uncouples functions (bioRxiv; Sept 5, 2024; https://doi.org/10.1101/2024.09.04.611229) (ahmed2024twofunctionalforms pages 1-5, ahmed2024twofunctionalforms pages 5-8).
- TZ architecture/localization: photoreceptor CEP290 study shows connecting cilium sub-compartmentalization dependence on CEP290 (J Cell Sci, 2025) (dubaicUnknownyearofthethesis pages 24-26).
- CPLANE–TZ link: RSG1 connects CPLANE to TZ architecture and IFT recruitment, supporting a unifying basal body→IFT→TZ assembly axis in ciliogenesis (summary from gathered evidence) (kalot2024primaryciliaand pages 19-20).

## 9. Current Applications and Real-world Implementations
- Prenatal genetics: Diagnostic algorithms for fetuses with bilateral polycystic kidneys integrate ultrasound features with chromosomal microarray and exome sequencing; MKS represents a substantial fraction of such cases, guiding counseling and management (Simonini 2023) (kalot2024primaryciliaand pages 19-20).
- Pathway-aware variant interpretation: Recognition that MKS genes localize to TZ/MKS modules and perturb HH/Wnt/PCP helps interpret variants of uncertain significance and to predict organ involvement patterns (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12).

## 10. Expert Opinions and Authoritative Analysis
- Reviews emphasize the TZ as the gating barrier that enforces ciliary identity and signaling; disruption explains multisystem patterning defects in ciliopathies including MKS (mill2023primaryciliaas pages 31-36). Renal-focused analyses highlight actin/RhoA-driven basal body docking defects as a shared path for MKS genes, aligning kidney dysplasia and cystogenesis with ciliogenesis failure (kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20).

## 11. Relevant Statistics and Data
- Ciliopathy burden: MKS incidence ranges roughly from 1 in 13,250 to 1 in 140,000 births in population summaries; prenatal cohorts with bilateral polycystic kidneys identify MKS in ~17% of cases in a large single-center series spanning 1999–2020 (Oct 2023) (kalot2024primaryciliaand pages 11-12) (kalot2024primaryciliaand pages 19-20).

## Gene/Protein Annotations with Ontologies
- TMEM67 (HGNC:17762): GO BP: ciliogenesis (GO:0060271), Wnt signaling (GO:0016055); GO CC: ciliary transition zone (GO:0035869); Evidence: TMEM67 cleavage partitions Wnt vs. ciliogenesis (bioRxiv, Sep 2024) (ahmed2024twofunctionalforms pages 1-5, ahmed2024twofunctionalforms pages 5-8).
- MKS1 (HGNC:7100): GO BP: basal body docking (GO:0097711), actin cytoskeleton organization (GO:0032956); GO CC: transition zone (GO:0035869) (kalot2024primaryciliaand pages 11-12).
- CEP290 (HGNC:29038): GO BP: ciliary protein localization (GO:1903561); GO CC: ciliary transition zone/connecting cilium (mill2023primaryciliaas pages 31-36, dubaicUnknownyearofthethesis pages 24-26).
- CC2D2A (HGNC:21525): GO BP: cilium assembly (GO:0042384); GO CC: transition zone (mill2023primaryciliaas pages 31-36, dubaicUnknownyearofthethesis pages 24-26).
- TMEM216 (HGNC:26499): GO BP: basal body docking, planar polarity; GO CC: transition zone/basal body (kalot2024primaryciliaand pages 11-12).
- TMEM231 (HGNC:25815): GO BP: ciliary gate function; GO CC: transition zone (mill2023primaryciliaas pages 31-36).
- B9D1 (HGNC:25715): GO BP: transition zone assembly; GO CC: transition zone (mill2023primaryciliaas pages 31-36, dubaicUnknownyearofthethesis pages 24-26).
- RPGRIP1L (HGNC:23186): GO BP: ciliary protein import; GO CC: transition zone (mill2023primaryciliaas pages 31-36).
- INPP5E (HGNC:6065): GO BP: phosphoinositide metabolism in cilium; GO CC: ciliary membrane (mill2023primaryciliaas pages 31-36).

## Phenotype Associations (HP terms)
- Occipital encephalocele (HP:0002072), Cystic renal dysplasia (HP:0004714), Postaxial polydactyly (HP:0001162), Hepatic fibrosis/ductal plate malformation (HP:0001407), Cerebellar vermis hypoplasia (HP:0001320), Ventriculomegaly (HP:0002119), Retinal dystrophy (HP:0000556) (kalot2024primaryciliaand pages 11-12, mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 19-20).

## Cell Type Involvement (CL terms)
- Renal tubular epithelial cells (CL:0002306), Cholangiocytes (CL:0000182), Neuroepithelial cells (CL:0002322), Photoreceptors (CL:0000210), Limb bud mesenchyme (CL:0000445) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12).

## Anatomical Locations (UBERON terms)
- Kidney (UBERON:0002113), Liver (UBERON:0002107), Cerebellum (UBERON:0002037), Limb bud (UBERON:0004385) (mill2023primaryciliaas pages 31-36, kalot2024primaryciliaand pages 11-12).

## Chemical Entities (CHEBI)
- Wnt5a (CHEBI:53095), cAMP (CHEBI:17489), PIP2 (CHEBI:18348), PIP3 (CHEBI:16618) (mill2023primaryciliaas pages 31-36, ahmed2024twofunctionalforms pages 5-8).

## Evidence Items (recent, with URLs/dates)
- Mill P, Christensen ST, Pedersen LB. Primary cilia as dynamic and diverse signalling hubs in development and disease. Nature Reviews Genetics. Apr 2023. DOI:10.1038/s41576-023-00587-9. URL: https://doi.org/10.1038/s41576-023-00587-9 (mechanistic overview; TZ barrier; ciliary signaling) (mill2023primaryciliaas pages 31-36).
- Kalot RK et al. Primary cilia and actin regulatory pathways in renal ciliopathies. Frontiers in Nephrology. Jan 2024. DOI:10.3389/fneph.2023.1331847. URL: https://doi.org/10.3389/fneph.2023.1331847 (MKS genes; actin/RhoA; basal body docking) (kalot2024primaryciliaand pages 11-12, kalot2024primaryciliaand pages 19-20).
- Ahmed M et al. Two functional forms of the Meckel-Gruber syndrome protein TMEM67 generated by proteolytic cleavage by ADAMTS9 mediate Wnt signaling and ciliogenesis. bioRxiv. Sept 5, 2024. DOI:10.1101/2024.09.04.611229. URL: https://doi.org/10.1101/2024.09.04.611229 (TMEM67 cleavage; functional partition) (ahmed2024twofunctionalforms pages 1-5, ahmed2024twofunctionalforms pages 5-8).
- Moye AR et al. Sub-ciliary localization of CEP290 and effects of its loss in mouse photoreceptors during development. Journal of Cell Science. 2025. DOI pending. URL: https://doi.org/10.1242/jcs.263869 (CEP290-dependent TZ/connecting cilium architecture) (dubaicUnknownyearofthethesis pages 24-26).
- Simonini C et al. Prenatal ultrasound in fetuses with polycystic kidney appearance—expanding the diagnostic algorithm. Archives of Gynecology and Obstetrics. Oct 2023. DOI:10.1007/s00404-022-06814-8. URL: https://doi.org/10.1007/s00404-022-06814-8 (prenatal series; MKS among top etiologies) (kalot2024primaryciliaand pages 19-20).

## Notes and Limitations
- The TMEM67–ADAMTS9 cleavage study is a 2024 preprint and, while compelling, awaits peer review; conclusions should be considered provisional pending replication (ahmed2024twofunctionalforms pages 1-5, ahmed2024twofunctionalforms pages 5-8).

## References (by citation IDs)
- pqac-00000005: Nature Reviews Genetics 2023 (Mill et al.) https://doi.org/10.1038/s41576-023-00587-9 (Apr 2023)
- pqac-00000004 and pqac-00000006: Frontiers in Nephrology 2024 (Kalot et al.) https://doi.org/10.3389/fneph.2023.1331847 (Jan 2024)
- pqac-00000001 and pqac-00000002: bioRxiv 2024 (Ahmed et al.) https://doi.org/10.1101/2024.09.04.611229 (Sep 5, 2024)
- pqac-00000003: Journal of Cell Science 2025 (Moye et al.) https://doi.org/10.1242/jcs.263869


References

1. (mill2023primaryciliaas pages 31-36): Pleasantine Mill, Søren T. Christensen, and Lotte B. Pedersen. Primary cilia as dynamic and diverse signalling hubs in development and disease. Nature reviews. Genetics, 24:421-441, Apr 2023. URL: https://doi.org/10.1038/s41576-023-00587-9, doi:10.1038/s41576-023-00587-9. This article has 370 citations.

2. (kalot2024primaryciliaand pages 11-12): Rita K. Kalot, Zachary T Sentell, Thomas M. Kitzler, and Elena Torban. Primary cilia and actin regulatory pathways in renal ciliopathies. Frontiers in Nephrology, Jan 2024. URL: https://doi.org/10.3389/fneph.2023.1331847, doi:10.3389/fneph.2023.1331847. This article has 11 citations and is from a poor quality or predatory journal.

3. (ahmed2024twofunctionalforms pages 5-8): Manu Ahmed, Sydney Fischer, Karyn L. Robert, Karen I. Lange, Michael W. Stuck, Sunayna Best, Colin A. Johnson, Gregory J. Pazour, Oliver E. Blacque, and Sumeda Nandadasa. Two functional forms of the meckel-gruber syndrome protein tmem67 generated by proteolytic cleavage by adamts9 mediate wnt signaling and ciliogenesis. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.04.611229, doi:10.1101/2024.09.04.611229. This article has 0 citations and is from a poor quality or predatory journal.

4. (ahmed2024twofunctionalforms pages 1-5): Manu Ahmed, Sydney Fischer, Karyn L. Robert, Karen I. Lange, Michael W. Stuck, Sunayna Best, Colin A. Johnson, Gregory J. Pazour, Oliver E. Blacque, and Sumeda Nandadasa. Two functional forms of the meckel-gruber syndrome protein tmem67 generated by proteolytic cleavage by adamts9 mediate wnt signaling and ciliogenesis. bioRxiv, Sep 2024. URL: https://doi.org/10.1101/2024.09.04.611229, doi:10.1101/2024.09.04.611229. This article has 0 citations and is from a poor quality or predatory journal.

5. (dubaicUnknownyearofthethesis pages 24-26): M Dubaic. Of the thesis: primary cilia function in development and disease. Unknown journal, Unknown year.

6. (kalot2024primaryciliaand pages 19-20): Rita K. Kalot, Zachary T Sentell, Thomas M. Kitzler, and Elena Torban. Primary cilia and actin regulatory pathways in renal ciliopathies. Frontiers in Nephrology, Jan 2024. URL: https://doi.org/10.3389/fneph.2023.1331847, doi:10.3389/fneph.2023.1331847. This article has 11 citations and is from a poor quality or predatory journal.