---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-26T19:28:59.778222'
end_time: '2026-01-26T19:36:02.845990'
duration_seconds: 423.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Proteus syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Proteus syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Proteus syndrome**.
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
- **Disease Name:** Proteus syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Proteus syndrome**.
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


Disease Pathophysiology Research Template

Target Disease
- Disease Name: Proteus syndrome
- MONDO ID: 
- Category: Mendelian (mosaic, post-zygotic activating mutation disorder)

Pathophysiology description
Proteus syndrome is an ultra-rare, progressive, mosaic overgrowth disorder caused by a somatic, activating AKT1 c.49G>A (p.E17K) variant that dysregulates PI3K→AKT→mTOR signaling and drives regionally confined overgrowth across multiple tissues. The E17K substitution increases AKT affinity for membrane phosphoinositides and disrupts autoinhibition, producing constitutive pAKT and downstream signaling in mutation-positive clones, with both cell-autonomous and non–cell-autonomous effects evident in vivo and ex vivo (lateral spread of pathway activation into nearby wild-type cells) (https://doi.org/10.1038/srep17162, 2015-12-11; https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (lindhurst2015repressionofakt pages 1-2, lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15).

Endothelial and mural cell dysfunction is central to vascular malformations in Proteus syndrome. Human iPSC-derived vascular organoids engineered with mosaic AKT1 E17K recapitulate PS-like network hyperconnectivity with unstable vascular contacts, mural cell (PDGFRβ+) abnormalities, and increased vasculogenesis that can be pharmacologically normalized by AKT inhibitors, supporting a direct endothelial–mural etiology of the vascular phenotype (preprint; https://doi.org/10.1101/2024.01.26.577324, 2024-01-27) (he2024humanvascularorganoids pages 14-17). Clinically, thoracic imaging shows frequent pulmonary venous dilation, scarring, hyperlucent parenchyma, and intramyocardial fat, underscoring multi-tissue involvement and highlighting cardiopulmonary vulnerability (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2). Progressive cystic/emphysematous lung disease can be quantified and is more rapidly progressive in children (https://doi.org/10.1186/s13023-023-03013-9, 2024-02-15) (mirmomen2021cardiothoracicimagingfindings pages 1-2).

Core pathophysiology
- Primary mechanisms: Somatic mosaicism for AKT1 p.E17K drives constitutive AKT activity via enhanced PI(3,4,5)P3/PI(4,5)P2 binding and release of PH–kinase autoinhibition, with activation by PDK1 (T308) and mTORC2 (S473). Downstream, this promotes growth, proliferation, survival, anabolic metabolism, and extracellular matrix (ECM) remodeling, producing overgrowth, cysts, and ectasia (https://doi.org/10.1038/srep17162, 2015-12-11; https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (lindhurst2015repressionofakt pages 1-2, lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15).
- Dysregulated pathways: PI3K/AKT/mTOR signaling in endothelial, mural, mesenchymal (fibroblast), osteogenic, and adipocytic lineages; paracrine signaling drives non–cell-autonomous pAKT elevation in adjacent wild-type cells within lesions (https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15).
- Affected cellular processes: Enhanced vasculogenesis/angiogenic sprouting, impaired vessel stability (mural cell dysfunction), increased proliferation and matrix deposition in skin/dermis (cerebriform connective tissue nevi), hyperplasia in bone and adipose, and cyst formation in lung and biliary epithelium (https://doi.org/10.1101/2024.01.26.577324, 2024-01-27; https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (he2024humanvascularorganoids pages 14-17, lindhurst2019amousemodel pages 1-2).

Key molecular players, cells, anatomy, and phenotypes
| Category | Entity (ontology ID) | Role in Proteus syndrome pathophysiology | Supporting sources |
|---|---|---|---|
| Gene/Protein | AKT1 (HGNC:391) | Somatic activating mutation c.49G>A (p.E17K) → constitutive AKT activation driving mosaic overgrowth | (lindhurst2015repressionofakt pages 1-2, lindhurst2019amousemodel pages 1-2) |
| Gene/Protein | PDK1 / PDPK1 (HGNC:8769) | Phosphorylates AKT at T308; required for AKT activation downstream of PI3K | (lindhurst2015repressionofakt pages 1-2) |
| Gene/Protein | mTOR (MTOR; HGNC:3942) | Downstream nutrient/growth regulator; mediates anabolic responses to AKT signaling | (lindhurst2015repressionofakt pages 1-2, klimeczekchrapusta2024proteussyndromecase pages 2-5) |
| Complex | mTORC2 (RICTOR; HGNC:28611) | Phosphorylates AKT at S473, sustaining AKT activity | (lindhurst2015repressionofakt pages 1-2) |
| Gene/Protein | PI3K (PIK3CA; HGNC:8975) | Upstream lipid kinase generating PIP3; PIK3CA mutations produce overlapping overgrowth/VM phenotypes | (klimeczekchrapusta2024proteussyndromecase pages 2-5, lindhurst2015repressionofakt pages 1-2) |
| Gene/Protein | PTEN (HGNC:9588) | Negative regulator of PI3K-AKT signaling; loss produces AKT pathway activation and overlapping features | (klimeczekchrapusta2024proteussyndromecase pages 2-5, lindhurst2015repressionofakt pages 1-2) |
| Cell type | Endothelial cell (CL:0000115) | Key component of vascular malformations; shows altered signaling/structure in AKT1-mutant lesions | (he2024humanvascularorganoids pages 14-17, lindhurst2019amousemodel pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2) |
| Cell type | Pericyte / mural cell (CL:0000669) | Mural cell dysfunction and PDGFRβ+ mural cell abnormalities contribute to unstable vasculature in mosaic AKT1 models | (he2024humanvascularorganoids pages 14-17, lindhurst2019amousemodel pages 1-2) |
| Cell type | Fibroblast (CL:0000057) | Drives connective tissue overgrowth (e.g., cerebriform connective tissue nevus) via increased AKT signaling | (lindhurst2015repressionofakt pages 1-2, ours2021casereportfiveyear pages 1-2) |
| Cell type | Osteoblast (CL:0000062) | Mediates asymmetric bony overgrowth and scoliosis through AKT-driven hyperplasia | (lindhurst2019amousemodel pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2) |
| Cell type | Adipocyte (CL:0000136) | Lipomatous/fatty overgrowth and dysregulated adipose tissue in affected regions | (lindhurst2019amousemodel pages 1-2, ours2021casereportfiveyear pages 1-2) |
| Anatomy | Lung (UBERON:0002048) | Site of cystic/emphysematous changes and progressive pulmonary disease in PS | (mirmomen2021cardiothoracicimagingfindings pages 1-2, lindhurst2019amousemodel pages 1-2) |
| Anatomy | Skin / dermis (UBERON:0002097) | Location of cerebriform connective tissue nevi and epidermal/dermal overgrowth | (lindhurst2015repressionofakt pages 1-2, ours2021casereportfiveyear pages 1-2) |
| Anatomy | Bone (UBERON:0001474) | Skeletal overgrowth, deformities, and asymmetric limb enlargement | (mirmomen2021cardiothoracicimagingfindings pages 1-2, lindhurst2019amousemodel pages 1-2) |
| Anatomy | Vascular system (UBERON:0004535) | Vascular malformations (venous/lymphatic/other) are a central clinical and pathophysiologic feature | (klimeczekchrapusta2024proteussyndromecase pages 2-5, mirmomen2021cardiothoracicimagingfindings pages 1-2, he2024humanvascularorganoids pages 14-17) |
| Phenotype | Cerebriform connective tissue nevus (HP:0032365) | Hallmark localized connective tissue overgrowth reflecting fibroblast/EC matrix expansion | (ours2021casereportfiveyear pages 1-2, lindhurst2015repressionofakt pages 1-2) |
| Phenotype | Vascular malformation (HP:0004930) | Frequent manifestation driven by AKT/PI3K pathway dysregulation in endothelial and mural cells | (lindhurst2019amousemodel pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2, he2024humanvascularorganoids pages 14-17) |
| Phenotype | Asymmetric limb overgrowth (HP:0009828) | Classic progressive, mosaic overgrowth of bone/soft tissue due to focal AKT1-mutant clones | (lindhurst2019amousemodel pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2) |
| Phenotype | Pulmonary emphysema / cystic change (HP:0002090) | Progressive cystic lung disease associated with morbidity and radiographic progression | (mirmomen2021cardiothoracicimagingfindings pages 1-2, lindhurst2019amousemodel pages 1-2) |
| Complication | Deep venous thrombosis (HP:0002625) | Major morbidity likely multifactorial (vascular malformations, stasis, altered endothelial factors) | (lindhurst2015repressionofakt pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2) |
| Complication | Pulmonary embolism (HP:0002204) | Leading cause of premature mortality in PS; linked to DVT and vascular anomalies | (lindhurst2015repressionofakt pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2) |


*Table: Compact table mapping genes, cells, tissues, phenotypes, and complications in Proteus syndrome with concise roles and supporting evidence (pqac IDs). This aids rapid cross-referencing of molecular players to pathophysiology and literature sources.*

Biological processes (for GO annotation)
- PI3K/AKT signaling; AKT phosphorylation by PDK1 and mTORC2; mTOR signaling; regulation of cell growth and proliferation; angiogenesis and vasculogenesis; endothelial cell migration; pericyte development; extracellular matrix organization; response to phosphoinositides; apoptotic signaling suppression. Mechanistic grounding from patient-derived cells/tissues showing elevated pAKT and downstream target phosphorylation, and reversal by AKT inhibition (https://doi.org/10.1038/srep17162, 2015-12-11) (lindhurst2015repressionofakt pages 1-2), corroborated by organoid data (https://doi.org/10.1101/2024.01.26.577324, 2024-01-27) (he2024humanvascularorganoids pages 14-17) and by in vivo mosaic models showing paracrine activation (https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15).

Cellular components
- Plasma membrane (AKT PH-domain engagement with PIP2/PIP3), cytosol, and mTORC1/2-associated compartments; endothelial junctions and basement membrane; perivascular space (mural cells); dermal ECM; alveolar and biliary epithelia in cystic lesions. Supported by patient-cell signaling assays and tissue immunostaining for pAKT in mutant and neighboring wild-type cells, and by organoid localization in endothelial–mural networks (https://doi.org/10.1038/srep17162, 2015-12-11; https://doi.org/10.1093/hmg/ddz116, 2019-09-01; https://doi.org/10.1101/2024.01.26.577324, 2024-01-27) (lindhurst2015repressionofakt pages 1-2, lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15, he2024humanvascularorganoids pages 14-17).

Disease progression
- Trigger: Post-zygotic AKT1 p.E17K in an early progenitor generates mosaic clones.
- Early tissue-level events: Localized AKT hyperactivation induces hyperplasia/expansion and vascular maldevelopment (endothelial hyperconnectivity, unstable mural support), with ECM remodeling and cyst formation in susceptible epithelia (lung, biliary) (https://doi.org/10.1101/2024.01.26.577324, 2024-01-27; https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (he2024humanvascularorganoids pages 14-17, lindhurst2019amousemodel pages 1-2).
- Clinical emergence: Postnatal, progressive, asymmetric overgrowth; hallmark cerebriform connective tissue nevi; evolving vascular malformations; thoracic/lung changes detectable on imaging (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2).
- Complications: Elevated risk of deep venous thrombosis and pulmonary embolism (PE), pneumonia and respiratory failure; tumor predisposition (notably meningiomas and gonadal epithelial tumors) (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22; https://doi.org/10.1136/jmg-2024-110173, 2025-12-01) (mirmomen2021cardiothoracicimagingfindings pages 1-2, rostagni2025tumourspectrumin pages 8-9).
- Pace: Lung cystic disease is progressive and faster in children than adults, informing surveillance and interventional trial endpoints (https://doi.org/10.1186/s13023-023-03013-9, 2024-02-15) (mirmomen2021cardiothoracicimagingfindings pages 1-2).

Phenotypic manifestations (HP terms)
- Asymmetric limb and skeletal overgrowth; scoliosis; vascular malformations (venous/lymphatic); cerebriform connective tissue nevi; fatty overgrowth/lipomatosis; cystic/emphysematous lung disease; intramyocardial fat. Imaging prevalence includes scoliosis 94%, pulmonary venous dilation 62%, scarring 56%, hyperlucency 50%, intramyocardial fat 45% (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2). Increased thromboembolism risk is a key morbidity; tumors are mostly benign and occur predominantly in genitourinary and CNS sites (https://doi.org/10.1136/jmg-2024-110173, 2025-12-01) (rostagni2025tumourspectrumin pages 8-9).

Current applications and real-world implementations
- AKT inhibition (miransertib/MK-7075/ARQ-092): In patient-derived cells/tissues, ARQ-092 rapidly suppresses pAKT and downstream signaling without reducing viability, supporting target engagement (https://doi.org/10.1038/srep17162, 2015-12-11) (lindhurst2015repressionofakt pages 1-2). Clinical case experience demonstrates long-term tolerability with symptomatic benefit (reduced pain) and slowed progression of cerebriform nevi and overgrowth over 5 years in an individual with PS (https://doi.org/10.1101/mcs.a006134, 2021-10-01) (ours2021casereportfiveyear pages 1-2). A systematic review notes an ongoing Phase 2 AKT inhibitor trial in PS (NCT04316546) (https://doi.org/10.1136/jmg-2024-110173, 2025-12-01) (rostagni2025tumourspectrumin pages 8-9). Vascular organoids modeling mosaic AKT1 E17K demonstrate reversal of vascular malformations by AKT inhibitors (Miransertib, Capivasertib, Ipatasertib), functionally linking target inhibition to network normalization (preprint; https://doi.org/10.1101/2024.01.26.577324, 2024-01-27) (he2024humanvascularorganoids pages 14-17).
- mTOR pathway modulation: Contemporary reviews and case syntheses include sirolimus use in PS as pathway-directed therapy, though effects may be partial and surgical management remains critical for skeletal deformities (https://doi.org/10.1055/a-2300-7002, 2024-04-01) (klimeczekchrapusta2024proteussyndromecase pages 2-5).

Expert opinions and guidance
- Contemporary imaging and clinical syntheses emphasize the multisystem burden, cardiopulmonary surveillance (including PE risk), and the role of molecular diagnosis (AKT1 testing) in confirming PS (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2). Review of tumor spectrum recommends awareness of genitourinary and CNS lesions, highlights predominance of benign tumors, and notes limited data on adult-onset malignancy—underscoring the need for longitudinal care and research (https://doi.org/10.1136/jmg-2024-110173, 2025-12-01) (rostagni2025tumourspectrumin pages 8-9). Mouse modeling and organoid studies provide mechanistic expert insight into non–cell-autonomous signaling and endothelial–mural dysfunction, guiding therapeutic targets and trial endpoints (https://doi.org/10.1093/hmg/ddz116, 2019-09-01; https://doi.org/10.1101/2024.01.26.577324, 2024-01-27) (lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15, he2024humanvascularorganoids pages 14-17).

Relevant statistics and data
- Prevalence and demographics: Approximately 1 per 1,000,000 births; male predominance ≈2:1 in one institutional cohort (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2).
- Survival: Literature synthesis estimates survival to age 22 around 82% (95% CI 74–91%), consistent with prior cohort observations of substantial pediatric mortality (https://doi.org/10.1136/jmg-2024-110173, 2025-12-01) (rostagni2025tumourspectrumin pages 8-9).
- Cardiothoracic imaging prevalence: scoliosis 94%, pulmonary venous dilation 62%, band-like scarring 56%, hyperlucent lung 50%, intramyocardial fat 45% (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2).
- Lung disease progression: Cystic Lung Score progression faster in children vs adults, correlating with symptoms and PFT decline (https://doi.org/10.1186/s13023-023-03013-9, 2024-02-15) (mirmomen2021cardiothoracicimagingfindings pages 1-2).

Gene/protein annotations with ontology terms (examples)
- AKT1 (HGNC:391): PI3K/AKT signaling; positive regulation of cell growth; regulation of apoptosis; membrane recruitment via PIP3; kinase activity (supported by patient-cell pharmacology and mouse/paracrine data) (https://doi.org/10.1038/srep17162, 2015-12-11; https://doi.org/1093/hmg/ddz116, 2019-09-01) (lindhurst2015repressionofakt pages 1-2, lindhurst2019amousemodel pages 1-2).
- PDPK1/PDK1 (HGNC:8769): AKT T308 phosphorylation; AGC kinase activation (lindhurst2015repressionofakt pages 1-2).
- MTOR (HGNC:3942) and RICTOR (HGNC:28611): mTORC1/2 signaling; AKT S473 phosphorylation; anabolic growth responses (lindhurst2015repressionofakt pages 1-2).
- PIK3CA (HGNC:8975) and PTEN (HGNC:9588): Upstream positive/negative regulators; overlapping overgrowth phenotypes in PI3K-pathway disorders (klimeczekchrapusta2024proteussyndromecase pages 2-5, lindhurst2015repressionofakt pages 1-2).

Phenotype associations (HP terms; examples)
- HP:0032365 cerebriform connective tissue nevus; HP:0004930 vascular malformation; HP:0009828 asymmetric limb overgrowth; HP:0002090 pulmonary emphysema/cystic changes; HP:0002625 deep venous thrombosis; HP:0002204 pulmonary embolism (supported by clinical imaging and case series) (mirmomen2021cardiothoracicimagingfindings pages 1-2, ours2021casereportfiveyear pages 1-2, klimeczekchrapusta2024proteussyndromecase pages 2-5).

Cell type involvement (CL terms; examples)
- CL:0000115 endothelial cell; CL:0000669 pericyte/mural cell; CL:0000057 fibroblast; CL:0000062 osteoblast; CL:0000136 adipocyte (mechanistic and histologic evidence in models and clinical tissues) (he2024humanvascularorganoids pages 14-17, lindhurst2019amousemodel pages 1-2, lindhurst2015repressionofakt pages 1-2, mirmomen2021cardiothoracicimagingfindings pages 1-2).

Anatomical locations (UBERON terms; examples)
- UBERON:0004535 vasculature; UBERON:0002097 skin/dermis; UBERON:0001474 bone; UBERON:0002048 lung; UBERON:0002082 heart (imaging and pathology support) (mirmomen2021cardiothoracicimagingfindings pages 1-2, lindhurst2019amousemodel pages 1-2, ours2021casereportfiveyear pages 1-2).

Chemical entities (CHEBI names; examples)
- Miransertib (ARQ‑092/MK‑7075; AKT inhibitor); Capivasertib (AKT inhibitor); Ipatasertib (AKT inhibitor); Sirolimus (mTOR inhibitor). Preclinical reversal of vascular phenotypes and clinical case benefits reported for AKT inhibition; sirolimus use reported with partial benefit (https://doi.org/10.1101/2024.01.26.577324, 2024-01-27; https://doi.org/10.1101/mcs.a006134, 2021-10-01; https://doi.org/10.1055/a-2300-7002, 2024-04-01) (he2024humanvascularorganoids pages 14-17, ours2021casereportfiveyear pages 1-2, klimeczekchrapusta2024proteussyndromecase pages 2-5).

Evidence items with PMIDs/DOIs/URLs
- Lindhurst MJ et al. Repression of AKT signaling by ARQ 092 in cells and tissues from patients with Proteus syndrome. Scientific Reports. 2015-12-11. DOI: 10.1038/srep17162. URL: https://doi.org/10.1038/srep17162 (lindhurst2015repressionofakt pages 1-2).
- Lindhurst MJ et al. A mouse model of Proteus syndrome. Human Molecular Genetics. 2019-09-01. DOI: 10.1093/hmg/ddz116. URL: https://doi.org/10.1093/hmg/ddz116 (lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15).
- Mirmomen SM et al. Cardiothoracic imaging findings of Proteus syndrome. Scientific Reports. 2021-03-22. DOI: 10.1038/s41598-021-86029-0. URL: https://doi.org/10.1038/s41598-021-86029-0 (mirmomen2021cardiothoracicimagingfindings pages 1-2).
- Ours CA et al. Case report: five-year experience of AKT inhibition with miransertib (MK-7075) in an individual with Proteus syndrome. Cold Spring Harbor Molecular Case Studies. 2021-10-01. DOI: 10.1101/mcs.a006134. URL: https://doi.org/10.1101/mcs.a006134 (ours2021casereportfiveyear pages 1-2).
- He S et al. Human vascular organoids with a mosaic AKT1 mutation recapitulate Proteus syndrome. bioRxiv. 2024-01-27. DOI: 10.1101/2024.01.26.577324. URL: https://doi.org/10.1101/2024.01.26.577324 (he2024humanvascularorganoids pages 14-17).
- Klimeczek-Chrapusta MK et al. Proteus Syndrome: Case Report and Updated Literature Review. Archives of Plastic Surgery. 2024-04-01. DOI: 10.1055/a-2300-7002. URL: https://doi.org/10.1055/a-2300-7002 (klimeczekchrapusta2024proteussyndromecase pages 2-5).
- Rostagni OM et al. Tumour spectrum in AKT1-related Proteus syndrome: a systematic review. Journal of Medical Genetics. 2025-12-01. DOI: 10.1136/jmg-2024-110173. URL: https://doi.org/10.1136/jmg-2024-110173 (rostagni2025tumourspectrumin pages 8-9).

Direct quotes supporting key statements
- “A somatic activating mutation in AKT1, c.49G>A, pGlu17Lys… is responsible for the mosaic overgrowth condition, Proteus syndrome.” (https://doi.org/10.1038/srep17162, 2015-12-11) (lindhurst2015repressionofakt pages 1-2).
- “Variant-positive cells can induce lesion formation in a non-cell autonomous manner.” (https://doi.org/10.1093/hmg/ddz116, 2019-09-01) (lindhurst2019amousemodel pages 14-15).
- Thoracic phenotype prevalence: “scoliosis…94%, pulmonary venous dilation 62%, band-like areas of lung scarring 56%, hyperlucent lung parenchyma 50%… intramyocardial fat…45%.” (https://doi.org/10.1038/s41598-021-86029-0, 2021-03-22) (mirmomen2021cardiothoracicimagingfindings pages 1-2).
- Organoid reversal with AKT inhibitors: “The application of AKT inhibitors (ARQ092, AZD5363, or GDC0068) reversed the vascular malformations” (https://doi.org/10.1101/2024.01.26.577324, 2024-01-27) (he2024humanvascularorganoids pages 14-17).

Notes and limitations
- Some data on survival and tumor incidence derive from systematic review of case reports/series and may be influenced by ascertainment; nonetheless, they guide surveillance priorities (https://doi.org/10.1136/jmg-2024-110173, 2025-12-01) (rostagni2025tumourspectrumin pages 8-9).

Summary
AKT1 p.E17K somatic mosaicism is the causal driver of Proteus syndrome, producing sustained PI3K→AKT→mTOR activation across endothelial, mural, mesenchymal, and epithelial compartments. Non–cell-autonomous propagation of pathway activation amplifies lesion formation. Vascular malformations and connective tissue overgrowth are core features, and cystic/emphysematous lung disease is progressive. AKT inhibition (miransertib) shows target engagement and encouraging case-level benefits; organoid models provide a translational platform linking AKT blockade to vascular normalization and supporting ongoing clinical trials (lindhurst2015repressionofakt pages 1-2, lindhurst2019amousemodel pages 1-2, lindhurst2019amousemodel pages 14-15, mirmomen2021cardiothoracicimagingfindings pages 1-2, he2024humanvascularorganoids pages 14-17, ours2021casereportfiveyear pages 1-2, rostagni2025tumourspectrumin pages 8-9, klimeczekchrapusta2024proteussyndromecase pages 2-5).

References

1. (lindhurst2015repressionofakt pages 1-2): Marjorie J. Lindhurst, Miranda R. Yourick, Yi Yu, Ronald E. Savage, Dora Ferrari, and Leslie G. Biesecker. Repression of akt signaling by arq 092 in cells and tissues from patients with proteus syndrome. Scientific Reports, Dec 2015. URL: https://doi.org/10.1038/srep17162, doi:10.1038/srep17162. This article has 77 citations and is from a peer-reviewed journal.

2. (lindhurst2019amousemodel pages 1-2): Marjorie J Lindhurst, Lauren R Brinster, Hannah C Kondolf, Jasmine J Shwetar, Miranda R Yourick, Henoke Shiferaw, Kim M Keppler-Noreuil, Gene Elliot, Cecilia Rivas, Lisa Garrett, Julio Gomez-Rodriguez, Neil J Sebire, Stephen M Hewitt, Pamela L Schwartzberg, and Leslie G Biesecker. A mouse model of proteus syndrome. Human molecular genetics, 28:2920-2936, Sep 2019. URL: https://doi.org/10.1093/hmg/ddz116, doi:10.1093/hmg/ddz116. This article has 15 citations and is from a domain leading peer-reviewed journal.

3. (lindhurst2019amousemodel pages 14-15): Marjorie J Lindhurst, Lauren R Brinster, Hannah C Kondolf, Jasmine J Shwetar, Miranda R Yourick, Henoke Shiferaw, Kim M Keppler-Noreuil, Gene Elliot, Cecilia Rivas, Lisa Garrett, Julio Gomez-Rodriguez, Neil J Sebire, Stephen M Hewitt, Pamela L Schwartzberg, and Leslie G Biesecker. A mouse model of proteus syndrome. Human molecular genetics, 28:2920-2936, Sep 2019. URL: https://doi.org/10.1093/hmg/ddz116, doi:10.1093/hmg/ddz116. This article has 15 citations and is from a domain leading peer-reviewed journal.

4. (he2024humanvascularorganoids pages 14-17): Siyu He, Yuefei Zhu, Shradha Chauhan, Daniel Naveed Tavakol, Jong Ha Lee, Rayna Batya-Leia Berris, Cong Xu, Jounghyun H. Lee, Caleb Lee, Sarah Cai, Shannon McElroy, Gordana Vunjak-Novakovic, Raju Tomer, Elham Azizi, Bin Xu, Yeh-Hsing Lao, and Kam W. Leong. Human vascular organoids with a mosaic akt1 mutation recapitulate proteus syndrome. bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.26.577324, doi:10.1101/2024.01.26.577324. This article has 3 citations and is from a poor quality or predatory journal.

5. (mirmomen2021cardiothoracicimagingfindings pages 1-2): S. Mojdeh Mirmomen, Andrew E. Arai, Evrim B. Turkbey, Andrew J. Bradley, Julie C. Sapp, Leslie G. Biesecker, and Arlene Sirajuddin. Cardiothoracic imaging findings of proteus syndrome. Scientific Reports, Mar 2021. URL: https://doi.org/10.1038/s41598-021-86029-0, doi:10.1038/s41598-021-86029-0. This article has 11 citations and is from a peer-reviewed journal.

6. (klimeczekchrapusta2024proteussyndromecase pages 2-5): Maria K Klimeczek-Chrapusta, Marek Kachnic, and Anna Chrapusta. Proteus syndrome: case report and updated literature review. Archives of Plastic Surgery, 51:423-431, Apr 2024. URL: https://doi.org/10.1055/a-2300-7002, doi:10.1055/a-2300-7002. This article has 0 citations and is from a poor quality or predatory journal.

7. (ours2021casereportfiveyear pages 1-2): Christopher A. Ours, Julie C. Sapp, Mia B. Hodges, Allison J. de Moya, and Leslie G. Biesecker. Case report: five-year experience of akt inhibition with miransertib (mk-7075) in an individual with proteus syndrome. Cold Spring Harbor Molecular Case Studies, 7:a006134, Oct 2021. URL: https://doi.org/10.1101/mcs.a006134, doi:10.1101/mcs.a006134. This article has 31 citations and is from a peer-reviewed journal.

8. (rostagni2025tumourspectrumin pages 8-9): Olivia M Rostagni, Charlotte LR Early, Mia B Hodges, Justice O Obasohan, Julie C Sapp, Alicia A Livinski, Leslie G Biesecker, and Christopher A Ours. Tumour spectrum in akt1-related proteus syndrome: a systematic review of clinical reports and series. Journal of Medical Genetics, 62:74-81, Dec 2025. URL: https://doi.org/10.1136/jmg-2024-110173, doi:10.1136/jmg-2024-110173. This article has 0 citations and is from a domain leading peer-reviewed journal.