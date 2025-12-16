---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:13:05.710819'
end_time: '2025-12-15T09:23:06.393079'
duration_seconds: 600.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ehlers-Danlos Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Ehlers-Danlos Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ehlers-Danlos Syndrome**.
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
- **Disease Name:** Ehlers-Danlos Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Ehlers-Danlos Syndrome**.
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
- Disease Name: Ehlers-Danlos Syndrome (EDS)
- MONDO ID: [not specified]
- Category: Genetic

Pathophysiology overview
EDS comprises a group of heritable connective tissue disorders with subtype-specific molecular etiologies that converge on extracellular matrix (ECM) dysfunction. Established monogenic subtypes arise from defects in fibrillar collagens or their processing, cross-linking, folding, or ECM regulatory proteins; periodontal EDS uniquely reflects dysregulated complement protease activity. Hypermobile EDS (hEDS) remains genetically unresolved and likely reflects complex polygenic/regulatory mechanisms affecting ECM, neuroimmune signaling, pain, and autonomic function (see details below) (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3, wilson2024clinicalgenomicanalysisof pages 17-19, wilson2023agenenetwork pages 19-21).

1) Core pathophysiology
- Primary mechanisms across subtypes
  - Collagen fibrillogenesis defects: classical EDS (cEDS; COL5A1/COL5A2) reduces type V collagen, impairing type I fibril nucleation/organization; vascular EDS (vEDS; COL3A1) weakens type III–rich vessels; dermatosparaxis EDS (dEDS; ADAMTS2) impairs procollagen N-propeptide removal; kyphoscoliotic EDS (kEDS; PLOD1/FKBP14) compromises collagen cross-linking (PLOD1) and folding (FKBP14); classical-like EDS (clEDS; TNXB) disrupts ECM organization and cell–matrix mechanics; GAG-biosynthesis EDS (spEDS; B4GALT7/B3GALT6/B3GAT3) alters proteoglycan linker assembly and growth-factor signaling; AEBP1-related clEDS2 alters ECM assembly (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3).
  - Complement-driven ECM degradation in periodontal EDS (pEDS; C1R/C1S): intracellular activation of C1r/C1s yields extracellular activated C1s that degrades collagen I and destabilizes ECM (“pathogenesis in pEDS is not solely mediated by activation of the complement cascade but by inadequate C1s-mediated degradation of matrix proteins”) (Frontiers in Immunology, 2023; DOI: 10.3389/fimmu.2023.1157421) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
  - Complex/polygenic mechanisms in hEDS: GWAS/meta-analytic and clinical-genomic studies implicate regulatory loci (e.g., near ACKR3), SLC39A13/ZIP13, neuroimmune/pain pathways, and autonomic/immune networks, supporting a “neuroimmune–stromal” disease model (preprint; medRxiv 2025) and a clinically derived “articulo–autonomic gene network” (2024) (petruccinelson2025complexgeneticsand pages 11-14, wilson2024clinicalgenomicanalysisof pages 17-19, wilson2023agenenetwork pages 19-21).

- Dysregulated molecular pathways (selected)
  - ECM organization, fibril assembly, integrin signaling (e.g., αvβ3 upregulation), and inflammatory programs (e.g., IL-1β) in cEDS; targeting αvβ3 partially rescues wound healing in Col5a1-deficient mouse wounds (iScience, 2024; DOI: 10.1016/j.isci.2024.110676) (kellyscumpia2024modulatingtheextracellular pages 6-8).
  - vEDS dermal fibroblasts show integrated proteomic/transcriptomic abnormalities implicating impaired ECM organization, autophagy–lysosome pathways, cellular stress responses, and miRNA regulation (e.g., miR-29b-3p), with miR-29b-3p inhibition increasing type V and I collagen (Biomedicines, 2024) (zschocke2024geneticdiagnosisof pages 5-6).
  - pEDS illustrates complement–ECM crosstalk: activated C1s enzymatically degrades collagen I in vitro and in patient fibroblast matrices (Frontiers in Immunology, 2023) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
  - clEDS (TNXB) pain mechanisms: TNX-deficient mice exhibit mechanical allodynia mediated by A-fiber hypersensitivity and constitutive TLR5 signaling (Scientific Reports, 2023) ().

- Affected cellular processes
  - Procollagen processing (ADAMTS2), collagen cross-link formation (PLOD1), ER folding/isomerization (FKBP14), ECM gene regulation (miRNAs, ZNF469/PRDM5), complement activation (C1R/C1S), integrin mechanosignaling, autophagy/proteostasis, and neuroimmune–nociceptive signaling (ACKR3/neuroimmune axes) (zschocke2024geneticdiagnosisof pages 5-6, kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, petruccinelson2025complexgeneticsand pages 11-14).

2) Key molecular players
- Genes/proteins (HGNC; representative)
  - cEDS: COL5A1, COL5A2 (type V collagen) (kellyscumpia2024modulatingtheextracellular pages 6-8, doolan2023extracutaneousfeaturesand pages 2-3)
  - vEDS: COL3A1 (type III collagen) (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3)
  - hEDS: unresolved; regulatory loci (ACKR3), SLC39A13/ZIP13 implicated (preprint) (petruccinelson2025complexgeneticsand pages 11-14)
  - pEDS: C1R, C1S (classical complement C1 proteases; activated C1s degrades collagen I) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6)
  - kEDS: PLOD1 (lysyl hydroxylase 1), FKBP14 (ER PPIase) (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3)
  - dEDS: ADAMTS2 (procollagen I/II N-proteinase) (doolan2023extracutaneousfeaturesand pages 2-3)
  - clEDS: TNXB (tenascin‑X; anti-adhesive ECM glycoprotein) (doolan2023extracutaneousfeaturesand pages 2-3)
  - clEDS2: AEBP1 (ECM-associated) (doolan2023extracutaneousfeaturesand pages 2-3)
  - spEDS: B4GALT7, B3GALT6, B3GAT3 (GAG linker biosynthesis) (doolan2023extracutaneousfeaturesand pages 2-3)
  - BCS: ZNF469, PRDM5 (ECM gene regulation in cornea) (zschocke2024geneticdiagnosisof pages 5-6)
  - Additional modifier/regulatory candidates: miR-29b-3p (vEDS fibroblasts), integrins (αvβ3), inflammatory cytokines (IL‑1β), TLR5 (TNXB model) (zschocke2024geneticdiagnosisof pages 5-6, kellyscumpia2024modulatingtheextracellular pages 6-8).

- Chemical entities (CHEBI; examples)
  - Collagens and ECM proteins; integrin antagonists (e.g., cilengitide) tested in model systems; complement proteases (serine proteases C1r/C1s); cytokines (IL‑1β) (kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).

- Cell types (CL) and anatomical locations (UBERON)
  - Dermal fibroblasts (CL:0000057), vascular smooth muscle cells (CL:0000187), endothelial cells (CL:0000115), peripheral sensory neurons (CL:0000103), myofibroblasts (CL:0001059). Key tissues: skin dermis (UBERON:0002067), arterial wall (UBERON:0001981), periodontal tissues (UBERON:0004114), corneal stroma (UBERON:0001772), fascia/tendon/ligament (UBERON:0001987/0001338/0002076) (kellyscumpia2024modulatingtheextracellular pages 6-8, zschocke2024geneticdiagnosisof pages 5-6, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3).

3) Biological processes for GO annotation (selected)
- Extracellular matrix organization; collagen fibril organization; collagen biosynthetic process; procollagen N‑terminal propeptide cleavage; collagen cross-linking; protein folding (ER); integrin-mediated signaling pathway; regulation of inflammatory response; complement activation, classical pathway; autophagy; cellular response to mechanical stimulus; regulation of neuron projection development; sensory perception of pain (zschocke2024geneticdiagnosisof pages 5-6, kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3, wilson2024clinicalgenomicanalysisof pages 17-19, wilson2023agenenetwork pages 19-21).

4) Cellular components (selected)
- Extracellular matrix; collagen fibril; basement membrane; ER lumen; Golgi apparatus; lysosome/autophagosome; plasma membrane integrin complexes; complement C1 complex (zschocke2024geneticdiagnosisof pages 5-6, kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3).

5) Disease progression (sequence of events; subtype examples)
- cEDS (COL5A1/2): type V collagen deficiency → impaired type I fibrillogenesis and ECM disarray → altered mechanotransduction (αvβ3 upregulation) and persistent dermal inflammation (↑IL‑1β) → poor wound tensile strength, atrophic scarring, skin hyperextensibility and joint instability. Direct experimental evidence: “Col5a1 conditional KO wounds show fibrillar disarray, increased αvβ3 and IL‑1β, reduced mechanical strength,” with pharmacologic αvβ3 antagonism or WT fibroblasts partially rescuing healing (iScience, 2024; DOI: 10.1016/j.isci.2024.110676) (kellyscumpia2024modulatingtheextracellular pages 6-8).
- vEDS (COL3A1): mutant type III collagen → fragile arterial/organ ECM → fibroblast proteome/transcriptome shows impaired ECM organization, autophagy–lysosome and stress responses; miR‑29b‑3p inhibition restores ECM proteins (Biomedicines, 2024) → clinical arterial dissection/rupture and aneurysm (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3).
- pEDS (C1R/C1S): intracellular activation of C1r/C1s → extracellular activated C1s (aC1s) → collagen I degradation and high collagen turnover → unstable periodontal/CT matrix → severe early-onset periodontitis, thin fragile gums; frequent white-matter changes suggest small-vessel involvement (Frontiers in Immunology, 2023; Frontiers in Genetics, 2023) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3).
- clEDS (TNXB): tenascin‑X deficiency → disordered ECM and altered cell–matrix adhesion → peripheral A‑fiber hypersensitivity via constitutive TLR5 activation → mechanical allodynia and neuropathic pain (Scientific Reports, 2023) ().
- hEDS: complex regulatory variation (e.g., ACKR3 enhancer; SLC39A13 locus) → neuroimmune–stromal dysregulation and altered nociception, autonomic imbalance, gastrointestinal and pain comorbidities; integrated clinical-genomic networks link connective tissue laxity to autonomic/neuromuscular features (medRxiv 2025 preprint; Current Issues in Molecular Biology, 2024) (petruccinelson2025complexgeneticsand pages 11-14, wilson2024clinicalgenomicanalysisof pages 17-19, wilson2023agenenetwork pages 19-21).

6) Phenotypic manifestations and quantitative data
- Systematic review across 839 cases reported:
  - Joint hypermobility prevalence: kyphoscoliotic 100% (39/39), spEDS 96.0% (24/25), hEDS 95.6% (153/160) (Frontiers in Medicine, 2023; DOI: 10.3389/fmed.2023.1053466) (doolan2023extracutaneousfeaturesand pages 2-3).
  - Musculoskeletal complications: decreased bone density 90.7% (39/43), joint pain 80.4% (217/270), hypotonia/weakness 56.4% (79/140) (doolan2023extracutaneousfeaturesand pages 2-3).
  - vEDS vascular outcomes: cerebrovascular events 16.3% (25/153), aneurysm 31.4% (77/245), arterial dissection/rupture 35.5% (89/250) (doolan2023extracutaneousfeaturesand pages 2-3).
- Direct quotes highlighting mechanisms
  - pEDS: “pathogenesis in pEDS is not solely mediated by activation of the complement cascade but by inadequate C1s-mediated degradation of matrix proteins, confirming pEDS as a primary connective tissue disorder” (Frontiers in Immunology, 2023; DOI: 10.3389/fimmu.2023.1157421) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
  - cEDS (mouse model): Col5a1-deficient wounds show “increased αvβ3 and IL-1β,” fibrillar disarray, and reduced mechanical strength; αvβ3 antagonism or WT fibroblasts partially rescue healing (iScience, 2024; DOI: 10.1016/j.isci.2024.110676) (kellyscumpia2024modulatingtheextracellular pages 6-8).
  - clEDS pain: “mechanical allodynia due to TNX deficiency is caused by the hypersensitivity of Aδ- and Aβ-fibers, and it is induced by constitutive activation of TLR5” (Scientific Reports, 2023; DOI: 10.1038/s41598-023-45638-7) ().

Recent developments and latest research (2023–2024 priority)
- cEDS: in vivo mechanobiology of COL5A1 deficiency establishes αvβ3/IL‑1β signaling as wound-healing modulators and demonstrates partial rescue by integrin antagonism or fibroblast therapy (iScience, 2024) (kellyscumpia2024modulatingtheextracellular pages 6-8).
- vEDS: patient-fibroblast multi-omics highlights miRNA (miR‑29b‑3p)–mediated control of ECM and autophagy–lysosome pathways; miR‑29b‑3p inhibition restores collagen I/V expression (Biomedicines, 2024) (zschocke2024geneticdiagnosisof pages 5-6). Clinical reviews reinforce vigilance for arterial events and outline prevention strategies (2024) (doolan2023extracutaneousfeaturesand pages 2-3).
- pEDS: mechanistic confirmation that aC1s degrades collagen I and accelerates matrix turnover in patient fibroblasts, providing a direct link between complement proteases and ECM fragility (Frontiers in Immunology, 2023) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6). Clinical series emphasize leukoencephalopathy (white-matter changes) in adults with C1R variants (Frontiers in Genetics, 2023) (doolan2023extracutaneousfeaturesand pages 2-3).
- clEDS (TNXB): murine models connect ECM deficiency to nociceptive pathway sensitization via TLR5 (Scientific Reports, 2023) ().
- hEDS: convergent evidence for complex, multisystem pathogenesis involving neuroimmune–stromal regulation and shared genetic correlations with pain, autonomic, and GI disorders; clinical-genomic networks identify autonomic and neuromuscular linkages (2024; preprint 2025) (wilson2024clinicalgenomicanalysisof pages 17-19, petruccinelson2025complexgeneticsand pages 11-14, wilson2023agenenetwork pages 19-21).

Current applications and real-world implementations
- Molecular diagnosis: 12 of 13 subtypes have identifiable monogenic causes and are amenable to panel/exome testing; structural variants (e.g., PLOD1 duplication, TNXB/RCCX rearrangements) may require long-range methods (Medizinische Genetik, 2024; DOI: 10.1515/medgen-2024-2061) (zschocke2024geneticdiagnosisof pages 5-6).
- Clinical surveillance: systematic review data support high rates of joint hypermobility, musculoskeletal morbidity, and vEDS vascular events, reinforcing routine vascular imaging and risk reduction (Frontiers in Medicine, 2023) (doolan2023extracutaneousfeaturesand pages 2-3).
- Emerging targeted concepts: 
  - ECM-modulating therapeutics in cEDS wound repair (integrin αvβ3 antagonists; cell therapy) (iScience, 2024) (kellyscumpia2024modulatingtheextracellular pages 6-8).
  - miRNA modulation (miR‑29b‑3p) and autophagy–lysosome pathways in vEDS fibroblasts (Biomedicines, 2024) (zschocke2024geneticdiagnosisof pages 5-6).
  - Protease/complement modulation in pEDS (targeting aberrant aC1s activity) (Frontiers in Immunology, 2023) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).

Expert opinions and authoritative analyses
- Diagnostic framework: “Pathogenesis is related to disturbances of collagen formation and/or stability… No monogenic cause has been identified for hypermobile EDS (hEDS), … unlikely to represent a single gene disorder” (Medizinische Genetik, 2024; DOI: 10.1515/medgen-2024-2061) (zschocke2024geneticdiagnosisof pages 5-6).
- Network view: An “articulo–autonomic gene network” links tissue laxity, autonomic imbalance, and neuromuscular dysfunction, supporting polygenic and pathway-level interpretation—consistent with multisystem clinical expression (Current Issues in Molecular Biology, 2024; DOI: 10.3390/cimb46030166) (wilson2024clinicalgenomicanalysisof pages 17-19).

Relevant statistics and data from recent studies
- Extracutaneous burden (2023 systematic review; n=839): joint hypermobility up to 100% in kEDS, 96% in spEDS, 95.6% in hEDS; decreased bone density 90.7%; joint pain 80.4%; hypotonia 56.4% (Frontiers in Medicine, 2023; DOI: 10.3389/fmed.2023.1053466) (doolan2023extracutaneousfeaturesand pages 2-3).
- vEDS vascular outcomes (same review): cerebrovascular 16.3%, aneurysm 31.4%, arterial dissection/rupture 35.5% (doolan2023extracutaneousfeaturesand pages 2-3).
- Experimental (cEDS mouse wounds): significant reductions in mechanical strength and collagen content with elevated αvβ3 and IL‑1β; partial pharmacologic rescue (iScience, 2024; DOI: 10.1016/j.isci.2024.110676) (kellyscumpia2024modulatingtheextracellular pages 6-8).

Structured subtype summary (2023–2024 evidence prioritized)

| Subtype | Gene(s) (HGNC) | Primary mechanism | Key pathways | Affected tissues / cell types | Hallmark phenotypes (HP terms) | Selected recent mechanistic evidence (2023–2024) with DOI/URL | Therapeutic implications |
|---|---|---|---|---|---|---:|---|
| cEDS (classical) | COL5A1, COL5A2 | Type V collagen haploinsufficiency → defective collagen I/V fibrillogenesis, abnormal fibril nucleation & organization | ECM organization, TGF-β signalling, integrin (αvβ3) mediated cell–matrix signalling | Dermal fibroblasts, epidermis, tendon/ligament ECM, skin dermis | Skin hyperextensibility, atrophic scarring, joint hypermobility (HP:0001382, HP:0000969) | Kelly-Scumpia et al., 2024: Col5a1 conditional KO wounds show fibrillar disarray, increased αvβ3 and IL-1β, reduced mechanical strength (iScience 2024) https://doi.org/10.1016/j.isci.2024.110676 (kellyscumpia2024modulatingtheextracellular pages 6-8, doolan2023extracutaneousfeaturesand pages 2-3) | ECM-modulating strategies: integrin αvβ3 antagonists (cilengitide in models), fibroblast cell therapy, wound-focused approaches (kellyscumpia2024modulatingtheextracellular pages 6-8) |
| vEDS (vascular) | COL3A1 | Mutant type III collagen → weakened arterial/organ walls; abnormal fibril assembly and ECM homeostasis | ECM/vascular integrity, PLC/IP3/PKC/ERK signalling dysregulation, proteostasis/autophagy, miRNA regulation | Vascular smooth muscle cells, endothelial cells, dermal fibroblasts, arterial ECM | Arterial/organ rupture, aneurysm, thin translucent skin (HP:0000826, HP:0004942) | Chiarelli et al., 2024: integrative proteomics/transcriptomics in vEDS fibroblasts implicates impaired ECM organization, autophagy and miR-29b-3p; miR-29b-3p inhibition restored ECM proteins (Biomedicines 2024) https://doi.org/10.3390/biomedicines12122749 (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3) | Vascular surveillance; blood-pressure control (celiprolol evidence discussed 2024); emerging molecular targets: ERK/PKC pathway and miRNA modulation (zschocke2024geneticdiagnosisof pages 5-6, wilson2024clinicalgenomicanalysisof pages 17-19) |
| hEDS (hypermobile; genetically unresolved) | — (no single-gene HGNC) | Complex, likely polygenic/regulatory; ECM fragility + neuroimmune–stromal dysregulation; altered cell–matrix adhesion | Neuroimmune signaling, nociception/pain pathways, zinc/metal transport (SLC39A13), inflammation, mechanotransduction | Dermal/fascial fibroblasts, peripheral nerves (small fibers), autonomic neurons, musculoskeletal fascia | Generalized joint hypermobility, chronic pain, dysautonomia/POTS, fatigue (HP:0001382, HP:0001249, HP:0001278) | GWAS/meta (preprint) and clinical-genomic studies propose regulatory loci (ACKR3) and SLC39A13 implicating neuroimmune–stromal model; Petrucci-Nelson et al. (preprint, 2025) & Wilson/Tonk clinical-genomic analyses (2024) propose polygenic/regulatory drivers (petruccinelson2025complexgeneticsand pages 11-14, wilson2024clinicalgenomicanalysisof pages 17-19, wilson2023agenenetwork pages 19-21) | Symptom-directed multidisciplinary care (pain, rehab, autonomic management); research on neuroimmune modulators, zinc/metal homeostasis and fascia-targeted therapies (petruccinelson2025complexgeneticsand pages 11-14, wilson2024clinicalgenomicanalysisof pages 17-19) |
| pEDS (periodontal) | C1R, C1S | Gain-of-function intracellular activation of C1r/C1s → extracellular activated C1s protease degrades ECM (collagen I) → periodontal/connective-tissue destruction | Classical complement activation, protease-mediated ECM degradation, inflammation | Gingival fibroblasts, periodontal ECM, small vessels, neural tissue (leukoencephalopathy in cohorts) | Early severe periodontitis, tooth loss, pretibial plaques, easy bruising (HP:0000674, HP:0000209) | Amberger et al., 2023: activated C1s degrades collagen I in vitro and patient fibroblasts → destabilized ECM; Angwin et al., 2023: pEDS associated with white-matter changes; DOI: 10.3389/fimmu.2023.1157421, https://doi.org/10.3389/fgene.2023.1136339 (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3) | Dental surveillance, periodontal management; potential approaches targeting aberrant complement activation or protease activity (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6) |
| kEDS-PLOD1 (kyphoscoliotic) | PLOD1 | Lysyl hydroxylase (LH1) deficiency → impaired hydroxylysine formation → defective collagen cross-linking and unstable fibrils | Collagen post-translational modification, cross-linking, ECM stability | Skin, ligaments, bone matrix, muscle connective tissue | Congenital hypotonia, progressive kyphoscoliosis, joint laxity (HP:0001251, HP:0002948) | Diagnostic/mechanistic synthesis in reviews and genetic-diagnosis updates (Zschocke 2024; transcriptome distinctions noted in prior studies) (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3) | Orthopedic/rehab management; genetic counseling; research into stabilizing cross-link pathways and tailored supportive care (zschocke2024geneticdiagnosisof pages 5-6) |
| kEDS-FKBP14 (kyphoscoliotic) | FKBP14 | ER-localized peptidyl-prolyl isomerase dysfunction → impaired collagen folding/secretion → abnormal ECM | ER protein folding, collagen biosynthesis, ECM assembly | Fibroblasts, muscle connective tissue, tendon ECM | Kyphoscoliosis, hypotonia, joint laxity, myopathy (HP:0002948, HP:0001251) | Cohort and mechanistic literature summarised in reviews and genetic-diagnosis updates (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3) | Supportive orthopedic care; potential exploration of chaperone/ER-stress modulating strategies in research (zschocke2024geneticdiagnosisof pages 5-6) |
| dEDS (dermatosparaxis) | ADAMTS2 | Loss of procollagen N-proteinase activity → failure to remove N-propeptides → defective fibrillogenesis, fragile skin | Procollagen processing, ECM protease activity, collagen fibrillogenesis | Dermal fibroblasts, skin ECM | Skin fragility, cutaneous tears, abnormal collagen ultrastructure (HP:0001593) | ADAMTS2 pathogenicity established across species (animal/veterinary reports) and case reports; ADAMTS2 functional links summarized in classical reviews (Malfait 2014; recent animal/case reports) (sciclunaUnknownyearthegeneticsof pages 20-25, doolan2023extracutaneousfeaturesand pages 2-3) | Wound care, surgical precautions; potential future protease-replacement or ECM-targeting therapies (doolan2023extracutaneousfeaturesand pages 2-3) |
| clEDS (classical-like; TNXB) | TNXB | Tenascin‑X deficiency → defective ECM organization, altered collagen–cell interactions and dysregulated MMP clearance (via THBS2 interactions) | ECM organization, MMP regulation, cell–matrix adhesion, TLR5-linked neuronal sensitization (pain) | Dermis, fascia, peripheral nerves, blood vessels | Skin hyperextensibility without atrophic scarring, joint hypermobility, chronic pain, neuropathy (HP:0001382, HP:0001388) | Okuda-Ashitaka 2023 and Kamada 2023: TNX-deficient mice show mechanical allodynia via A-fiber/TLR5 hypersensitivity; Hadar et al., 2024: THBS2 variant causes vascular-like EDS via MMP2 dysregulation (sciclunaUnknownyearthegeneticsofb pages 25-27, wilson2024clinicalgenomicanalysisof pages 17-19) | Pain-targeted strategies; attention to neuropathic mechanisms (A-fibre sensitization); research into MMP modulation and matricellular protein pathways (wilson2024clinicalgenomicanalysisof pages 17-19) |
| clEDS2 (AEBP1-related) | AEBP1 | ECM scaffolding/collagen-associated protein defects → abnormal collagen assembly and ECM maintenance | ECM assembly, transcriptional regulation of matrix components | Skin, connective tissues, dermal fibroblasts | Skin hyperextensibility, joint hypermobility, poor wound healing (HP:0001382, HP:0001593) | AEBP1 bi-allelic alterations described in recent clinical cohorts and reviews linking AEBP1 to collagen assembly (cited in systematic reviews) (doolan2023extracutaneousfeaturesand pages 2-3, dijk2024clinicaldiagnosisof pages 3-4) | Supportive care and surveillance; research into ECM-restorative strategies (dijk2024clinicaldiagnosisof pages 3-4) |
| spEDS (spondylodysplastic; GAG-biosynthesis forms) | B4GALT7, B3GALT6, B3GAT3 | Defects in glycosaminoglycan (GAG) linker synthesis → abnormal proteoglycan/heparan-sulfate assembly → altered ECM signalling and structure | GAG biosynthesis, growth-factor sequestration/signalling, ECM–cell signalling | Cartilage, bone, skin ECM, tendon | Short stature, radiologic skeletal dysplasia, hypermobile joints (HP:0004322, HP:0001382) | Systematic/genetic reviews and case series document GAG-biosynthesis gene effects on skeletal/connective development (doolan2023extracutaneousfeaturesand pages 2-3, sciclunaUnknownyearthegeneticsof pages 20-25) | Orthopedic/skeletal management; potential interest in modifying GAG-related signalling in future research (doolan2023extracutaneousfeaturesand pages 2-3) |
| BCS (Brittle Cornea Syndrome) | ZNF469, PRDM5 | Transcriptional regulators of ECM/collagen gene programs → corneal thinning and ECM fragility | ECM gene regulation, collagen biosynthesis, ocular ECM maintenance | Corneal stroma, ocular connective tissues, dermal ECM | Keratoconus, corneal thinning, ocular rupture risk (HP:0000592, HP:0000557) | Genetic/clinical summaries and reviews noting ZNF469/PRDM5 regulation of ECM and corneal phenotype; discussed in genetic-diagnosis literature (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3) | Ophthalmologic surveillance, protective measures; molecular studies target ECM regulatory pathways (zschocke2024geneticdiagnosisof pages 5-6) |


*Table: Compact summary table of major Ehlers–Danlos subtypes showing genes, core molecular mechanisms, affected tissues, hallmark phenotypes, 2023–2024 mechanistic evidence (DOI/URL), and therapeutic implications; useful as an at-a-glance reference for knowledgebase curation and research planning.*

Ontology-linked annotations for knowledge base
- Genes/proteins (HGNC): COL5A1/COL5A2 (cEDS), COL3A1 (vEDS), C1R/C1S (pEDS), PLOD1/FKBP14 (kEDS), ADAMTS2 (dEDS), TNXB (clEDS), AEBP1 (clEDS2), B4GALT7/B3GALT6/B3GAT3 (spEDS), ZNF469/PRDM5 (BCS); candidate/regulatory: ACKR3, SLC39A13 (hEDS, emerging) (zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3, petruccinelson2025complexgeneticsand pages 11-14).
- GO Biological Processes: extracellular matrix organization; collagen fibril organization; collagen biosynthetic process; procollagen N‑terminal peptidase activity; collagen cross-linking; protein folding; complement activation, classical pathway; integrin-mediated signaling; autophagy; inflammatory response; sensory perception of pain (kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, zschocke2024geneticdiagnosisof pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3).
- GO Cellular Components: extracellular matrix; collagen trimer/fibril; basement membrane; ER lumen; Golgi apparatus; autophagosome/lysosome; integrin complex; complement C1 complex (zschocke2024geneticdiagnosisof pages 5-6, kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
- Phenotype associations (HP): generalized joint hypermobility (HP:0001382), skin hyperextensibility (HP:0000974), atrophic scarring (HP:0001075; not typical in clEDS), arterial aneurysm (HP:0002617), arterial rupture (HP:0002642), early periodontitis (HP:0000674), white-matter abnormalities (HP:0002539) (doolan2023extracutaneousfeaturesand pages 2-3, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
- Cell types (CL): dermal fibroblast (CL:0000057), vascular smooth muscle cell (CL:0000187), endothelial cell (CL:0000115), myofibroblast (CL:0001059), peripheral sensory neuron (CL:0000103) (kellyscumpia2024modulatingtheextracellular pages 6-8, zschocke2024geneticdiagnosisof pages 5-6).
- Anatomical locations (UBERON): skin dermis (UBERON:0002067), arterial wall (UBERON:0001981), periodontal tissue (UBERON:0004114), corneal stroma (UBERON:0001772), tendon/ligament (UBERON:0001987/0002076) (doolan2023extracutaneousfeaturesand pages 2-3, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
- Chemical entities (CHEBI): collagen, integrin antagonists (e.g., cilengitide), complement serine proteases (C1r/C1s), cytokines (IL‑1β) (kellyscumpia2024modulatingtheextracellular pages 6-8, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).

Evidence items with links (recent priority)
- Kelly‑Scumpia KM et al. Modulating the extracellular matrix to treat wound healing defects in Ehlers‑Danlos syndrome. iScience. 2024-09. DOI: 10.1016/j.isci.2024.110676. URL: https://doi.org/10.1016/j.isci.2024.110676 (cEDS, integrin/IL‑1β) (kellyscumpia2024modulatingtheextracellular pages 6-8).
- Chiarelli N et al. Integrative Multi‑Omics Approach in Vascular Ehlers–Danlos Syndrome… Biomedicines. 2024-11. DOI: 10.3390/biomedicines12122749. URL: https://doi.org/10.3390/biomedicines12122749 (vEDS, miR‑29b‑3p/autophagy) (zschocke2024geneticdiagnosisof pages 5-6).
- Amberger A et al. Degradation of collagen I by activated C1s in periodontal EDS. Front Immunol. 2023-03. DOI: 10.3389/fimmu.2023.1157421. URL: https://doi.org/10.3389/fimmu.2023.1157421 (pEDS, C1s proteolysis) (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6).
- Doolan BJ et al. Extracutaneous features and complications of the EDS: a systematic review. Front Med. 2023-01. DOI: 10.3389/fmed.2023.1053466. URL: https://doi.org/10.3389/fmed.2023.1053466 (quantitative burden) (doolan2023extracutaneousfeaturesand pages 2-3).
- Zschocke J et al. Genetic diagnosis of the EDS. Medizinische Genetik. 2024-11. DOI: 10.1515/medgen-2024-2061. URL: https://doi.org/10.1515/medgen-2024-2061 (diagnostic genes/subtypes) (zschocke2024geneticdiagnosisof pages 5-6).
- Kamada H et al. Hypersensitivity of myelinated A‑fibers via TLR5 promotes mechanical allodynia in tenascin‑X‑deficient mice. Sci Rep. 2023-10. DOI: 10.1038/s41598-023-45638-7. URL: https://doi.org/10.1038/s41598-023-45638-7 (clEDS pain) ().
- Wilson GN & Tonk VS. Clinical‑Genomic Analysis of 1261 Patients with EDS outlines an Articulo‑Autonomic Gene Network. Curr Issues Mol Biol. 2024-03. DOI: 10.3390/cimb46030166. URL: https://doi.org/10.3390/cimb46030166 (network model) (wilson2024clinicalgenomicanalysisof pages 17-19).
- Petrucci‑Nelson T et al. Complex Genetics and Regulatory Drivers of hEDS (GWAS meta‑analysis). medRxiv. 2025-09 (preprint). DOI: 10.1101/2025.09.19.25336146. URL: https://doi.org/10.1101/2025.09.19.25336146 (regulatory/neuroimmune model) (petruccinelson2025complexgeneticsand pages 11-14).

Conclusion and future directions
EDS pathophysiology reflects convergent ECM failure with subtype-specific mechanisms—collagen fibrillogenesis and cross-link defects, procollagen processing deficits, complement protease overactivity, and dysregulated mechanobiology and autophagy—with growing evidence for neuroimmune–stromal mechanisms in hEDS. Recent experimental advances (2023–2024) provide tractable targets: integrin αvβ3 and inflammatory mediators in cEDS wound healing; miRNA/autophagy in vEDS fibroblasts; complement protease activity in pEDS; and TLR5-mediated A‑fiber sensitization in clEDS. Translating these into therapies will require controlled trials, mechanistically matched biomarkers, and integration with vigilant clinical surveillance and multidisciplinary care (kellyscumpia2024modulatingtheextracellular pages 6-8, zschocke2024geneticdiagnosisof pages 5-6, pliegoarreaga2024jointhypermobilitysyndrome pages 5-6, doolan2023extracutaneousfeaturesand pages 2-3, wilson2024clinicalgenomicanalysisof pages 17-19).

References

1. (zschocke2024geneticdiagnosisof pages 5-6): Johannes Zschocke, Serwet Demirdas, and Fleur S. van Dijk. Genetic diagnosis of the ehlers-danlos syndromes. Medizinische Genetik, 36:235-245, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2061, doi:10.1515/medgen-2024-2061. This article has 3 citations and is from a poor quality or predatory journal.

2. (doolan2023extracutaneousfeaturesand pages 2-3): Brent J. Doolan, Mark E. Lavallee, Ingrid Hausser, Jane R. Schubart, F. Michael Pope, Suranjith L. Seneviratne, Ingrid M. Winship, and Nigel P. Burrows. Extracutaneous features and complications of the ehlers-danlos syndromes: a systematic review. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2023.1053466, doi:10.3389/fmed.2023.1053466. This article has 23 citations and is from a poor quality or predatory journal.

3. (wilson2024clinicalgenomicanalysisof pages 17-19): Golder N. Wilson and Vijay S. Tonk. Clinical-genomic analysis of 1261 patients with ehlers–danlos syndrome outlines an articulo-autonomic gene network (entome). Current Issues in Molecular Biology, 46:2620-2643, Mar 2024. URL: https://doi.org/10.3390/cimb46030166, doi:10.3390/cimb46030166. This article has 8 citations and is from a poor quality or predatory journal.

4. (wilson2023agenenetwork pages 19-21): Golder N. Wilson. A gene network implicated in the joint-muscle pain, brain fog, chronic fatigue, and bowel irregularity of ehlers-danlos and "long" covid19 syndromes. MedRxiv, Mar 2023. URL: https://doi.org/10.1101/2023.03.24.23287706, doi:10.1101/2023.03.24.23287706. This article has 1 citations.

5. (pliegoarreaga2024jointhypermobilitysyndrome pages 5-6): Raquel Pliego-Arreaga, Juan Antonio Cervantes-Montelongo, Guillermo Antonio Silva-Martínez, Fabiola Estefanía Tristán-Flores, Miguel Angel Pantoja-Hernández, and Juan Raúl Maldonado-Coronado. Joint hypermobility syndrome and membrane proteins: a comprehensive review. Biomolecules, 14:472, Apr 2024. URL: https://doi.org/10.3390/biom14040472, doi:10.3390/biom14040472. This article has 6 citations and is from a poor quality or predatory journal.

6. (petruccinelson2025complexgeneticsand pages 11-14): Taylor Petrucci-Nelson, Sacha Guilhaumou, Takiy E Berrandou, Cortney Gensemer, Adrien Georges, Matthew Huff, Margaux-Alison Fustier, Asraa Esmael, Josephine Henry, Olivia Jaye, Ranan Phookan, Sarah Dooley, Kathryn Byerly, Brian Loizzi, Roman Fenner, Emma Mach, Amy Weintraub, Victoria Daylor, Julianna Weninger, Natalie Koren, Erika Bistran, Charlotte Griggs, Molly Griggs, Sydney Severance, Rebecca Byrd, Sunil Patel, Steven A Kautz, Anne Maitland, Nabila Bouatia-Naji, and Russell A Norris. Complex genetics and regulatory drivers of hypermobile ehlers-danlos syndrome: insights from genome-wide association study meta-analysis. MedRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.19.25336146, doi:10.1101/2025.09.19.25336146. This article has 0 citations.

7. (kellyscumpia2024modulatingtheextracellular pages 6-8): Kindra M. Kelly-Scumpia, Maani M. Archang, Prabhat K. Purbey, Tomohiro Yokota, Rimao Wu, Jackie McCourt, Shen Li, Rachelle H. Crosbie, Philip O. Scumpia, and Arjun Deb. Modulating the extracellular matrix to treat wound healing defects in ehlers-danlos syndrome. iScience, 27:110676, Sep 2024. URL: https://doi.org/10.1016/j.isci.2024.110676, doi:10.1016/j.isci.2024.110676. This article has 5 citations and is from a peer-reviewed journal.

8. (sciclunaUnknownyearthegeneticsof pages 20-25): K Scicluna. The genetics of hypermobile ehlers-danlos syndrome: a local study. Unknown journal, Unknown year.

9. (sciclunaUnknownyearthegeneticsofb pages 25-27): K Scicluna. The genetics of hypermobile ehlers-danlos syndrome: a local study. Unknown journal, Unknown year.

10. (dijk2024clinicaldiagnosisof pages 3-4): Fleur S. van Dijk, Chloe Angwin, Serwet Demirdas, Neeti Ghali, and Johannes Zschocke. Clinical diagnosis of the monogenic ehlers-danlos syndromes. Medizinische Genetik, 36:225-234, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2060, doi:10.1515/medgen-2024-2060. This article has 1 citations and is from a poor quality or predatory journal.