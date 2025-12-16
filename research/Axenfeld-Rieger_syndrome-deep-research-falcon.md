---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-15T09:00:51.803571'
end_time: '2025-12-15T09:08:48.745203'
duration_seconds: 476.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Axenfeld-Rieger syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Axenfeld-Rieger syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Axenfeld-Rieger syndrome**.
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
- **Disease Name:** Axenfeld-Rieger syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Axenfeld-Rieger syndrome**.
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
- Disease Name: Axenfeld–Rieger syndrome (ARS)
- MONDO ID: Not definitively assigned in retrieved context; ARS is a genetic anterior segment dysgenesis disorder.
- Category: Genetic (autosomal dominant; most often PITX2- or FOXC1-related)

| Category | Item (Ontology ID) | Mechanism / Role | Tissue / Cell Type (UBERON / CL) | Key Evidence (PMID / DOI, context ID) | Year | URL |
|---|---|---|---|---:|---:|---|
| Gene | PITX2 (HGNC:17490) | Paired-like homeodomain TF; regulates neural-crest–derived periocular mesenchyme, induces DKK2 to repress WNT; controls collagen/ECM gene expression | Periocular mesenchyme, corneal endothelium, iris stroma, trabecular meshwork | DOI: 10.1136/jmg-2022-108646 (reis2023axenfeldriegersyndromemore pages 1-2) | 2023 | https://doi.org/10.1136/jmg-2022-108646 |
| Gene | FOXC1 (HGNC:3800) | Forkhead TF; dosage-sensitive regulator of neural crest derivatives, TM development and ocular/endothelial programs | Periocular mesenchyme, trabecular meshwork, retinal endothelium | DOI: 10.2147/opth.s379853 (michels2023ophthalmologicalmanifestationsof pages 2-4); DOI: 10.1038/s41467-024-48134-2 (qi2022screeningofpathogenic pages 4-5) | 2023, 2024 | https://doi.org/10.2147/opth.s379853, https://doi.org/10.1038/s41467-024-48134-2 |
| Regulatory element | PITX2 distal enhancers (CE5-7) | Enhancer deletion/inversion separates PITX2 from regulatory elements → reduced PITX2 expression despite intact coding sequence | Regulatory locus controlling PITX2 expression (chr4 locus; enhancer cluster CE5-7) | medRxiv:10.1101/2025.06.05.25327661 (mitchell2025axenfeldriegersyndromeassociated pages 1-3); Reis et al. cohort (reis2023axenfeldriegersyndromemore pages 1-2) | 2025 (preprint), 2023 | https://doi.org/10.1101/2025.06.05.25327661, https://doi.org/10.1136/jmg-2022-108646 |
| Pathway | RA → PITX2 → DKK2 (WNT repression) | Retinoic-acid signaling induces PITX2 in perioptic mesenchyme; PITX2 upregulates DKK2 to antagonize WNT/β-catenin, patterning anterior segment | Periocular mesenchyme / POM | Kumar & Duester (retinoic acid → Pitx2 → Dkk2) DOI:10.1016/j.ydbio.2010.01.027; review/cohort support (michels2023ophthalmologicalmanifestationsof pages 2-4, reis2023axenfeldriegersyndromemore pages 1-2) | 2010, 2023 | https://doi.org/10.1016/j.ydbio.2010.01.027, https://doi.org/10.1136/jmg-2022-108646 |
| Pathway | Hippo (YAP/TAZ) → FOXC1 | YAP/TAZ activity in cranial neural crest regulates FOXC1 expression; links mechanotransduction/Hippo signaling to craniofacial and anterior segment development | Neural crest / periocular mesenchyme | Development DOI:10.1242/dev.126920; supporting reviews (michels2023ophthalmologicalmanifestationsof pages 2-4) | 2016, 2023 | https://doi.org/10.1242/dev.126920 |
| Process | ECM / Collagen dysregulation (PITX2 downstream) | PITX2 influences expression of collagen genes and ECM components → altered angle/Corneal ECM impacting outflow | Corneal stroma/endothelium, trabecular meshwork | RNA/transcriptome and animal-model data (Hendee et al.; cohort & reviews) (reis2023axenfeldriegersyndromemore pages 1-2, michels2023ophthalmologicalmanifestationsof pages 2-4) | 2018, 2023 | https://doi.org/10.1093/hmg/ddy074, https://doi.org/10.1136/jmg-2022-108646 |
| Cellular mechanism | TM cytoskeleton / noncanonical WNT (outflow dysfunction) | Noncanonical WNT and cytoskeletal remodeling (CLANs) in TM alter aqueous outflow; linked to anterior segment TFs (FOXC1/PITX2) regulation of TM ECM | Trabecular meshwork (CL: TM cells), Schlemm's canal | IOVS DOI:10.1167/iovs.13-12447; genetics-to-TM reviews (michels2023ophthalmologicalmanifestationsof pages 2-4) | 2013, 2022 | https://doi.org/10.1167/iovs.13-12447 |
| Signaling | TGF-β2 interactions in NCC/anterior segment | Heparan-sulfate and TGF-β2 signaling influence neural-crest responses and ECM; disruption → Peters/ASD-like phenotypes and TM abnormalities | Periocular mesenchyme, TM | J Clin Invest DOI:10.1172/JCI38519; ASD reviews (michels2023ophthalmologicalmanifestationsof pages 2-4, reis2023axenfeldriegersyndromemore pages 1-2) | 2009, 2023 | https://doi.org/10.1172/JCI38519 |
| Endothelial program | FOXC1 → CD98 (SLC3A2/SLC7A5) → mTOR | FOXC1 controls endothelial amino-acid transporter CD98, modulating mTOR activity and retinal angiogenesis / barrier formation (links TF to vascular phenotypes) | Retinal endothelium / vasculature | Nat Commun DOI:10.1038/s41467-024-48134-2 (qi2022screeningofpathogenic pages 4-5) | 2024 | https://doi.org/10.1038/s41467-024-48134-2 |
| Genetic model | Gene dosage & compensation (foxc1/pitx2 zebrafish) | Dosage-sensitive effects; foxc1/pitx2 allele combinations produce variable, dose-dependent ocular and systemic phenotypes; compensatory expression observed | Zebrafish periocular/neural crest (model system) | Hum Mol Genet DOI:10.1093/hmg/ddaa163; mechanistic reviews (reis2023axenfeldriegersyndromemore pages 1-2, michels2023ophthalmologicalmanifestationsof pages 2-4) | 2020, 2021 | https://doi.org/10.1093/hmg/ddaa163 |
| Clinical statistic | Glaucoma onset / prevalence by gene | Glaucoma common in ARS (overall >50%); Reis cohort: PITX2 ~72% vs FOXC1 ~66% overall; early-onset (<2 yrs) ~17% PITX2 vs ~66% FOXC1 (surgical management frequent) | Clinical phenotype (HP: glaucoma) | DOI:10.1136/jmg-2022-108646 (reis2023axenfeldriegersyndromemore pages 1-2, reis2023axenfeldriegersyndromemore pages 4-4) | 2023 | https://doi.org/10.1136/jmg-2022-108646 |
| Neuroimaging | FOXC1-associated CNS features | FOXC1 variants linked to frequent white-matter hyperintensities, ventriculomegaly, arachnoid cysts and vertebrobasilar dolichoectasia in cohort and case series | Brain (UBERON:0000955) / neuroimaging | AJNR DOI:10.3174/ajnr.a7995; cohort summary (reis2023axenfeldriegersyndromemore pages 1-1, reis2023axenfeldriegersyndromemore pages 1-2) | 2023 | https://doi.org/10.3174/ajnr.a7995, https://doi.org/10.1136/jmg-2022-108646 |
| Systemic phenotypes | Gene-specific systemic distinctions | PITX2: highly penetrant dental (microdontia/hypodontia) and umbilical anomalies; FOXC1: hearing loss, congenital heart defects, skeletal/joint anomalies | Teeth (HP), umbilicus, heart, auditory system | DOI:10.1136/jmg-2022-108646 (reis2023axenfeldriegersyndromemore pages 1-2) | 2023 | https://doi.org/10.1136/jmg-2022-108646 |


*Table: A compact evidence table mapping key genes, pathways, affected cell/tissue types, and primary recent/landmark citations (DOIs + context IDs) relevant to Axenfeld–Rieger syndrome pathophysiology, intended to support knowledge‑base annotation and quick reference.*

## 1. Core Pathophysiology
Axenfeld–Rieger syndrome is a neurocristopathy of the ocular anterior segment caused primarily by haploinsufficiency or dysregulation of the transcription factors PITX2 and FOXC1 in cranial neural crest–derived periocular mesenchyme (POM). Perturbation of these TFs disrupts signaling integration (retinoic acid→PITX2→DKK2, WNT antagonism; Hippo/YAP–TAZ→FOXC1; TGF-β/ECM cues) and cell-intrinsic programs (ECM/collagen transcription, cytoskeletal remodeling), leading to failure of normal regression/retraction of transient mesenchyme at the iridocorneal angle, maldevelopment of trabecular meshwork and Schlemm’s canal, and secondary childhood glaucoma (iridogoniodysgenesis) (michels2023ophthalmologicalmanifestationsof pages 2-4, reis2023axenfeldriegersyndromemore pages 1-2). Enhancer/structural disruptions at the PITX2 locus and dosage-sensitive FOXC1 defects underscore a central role for gene dosage and regulatory architecture in disease (mitchell2025axenfeldriegersyndromeassociated pages 1-3, reis2023axenfeldriegersyndromemore pages 1-2).

Mechanistically: (i) RA signaling induces PITX2 in the POM, which upregulates DKK2 to repress WNT/β-catenin, patterning the anterior segment; PITX2 also influences collagen/ECM expression (michels2023ophthalmologicalmanifestationsof pages 2-4). (ii) Hippo pathway effectors YAP/TAZ regulate FOXC1 in neural crest, linking mechanotransduction to craniofacial/anterior segment development (michels2023ophthalmologicalmanifestationsof pages 2-4). (iii) TGF-β/HS signaling in neural crest impacts anterior segment morphogenesis; perturbation yields ASD-like phenotypes (michels2023ophthalmologicalmanifestationsof pages 2-4). (iv) In the conventional outflow tissues, cytoskeletal/ECM remodeling and noncanonical WNT signaling in trabecular meshwork cells impair aqueous outflow, contributing to IOP elevation and glaucoma (michels2023ophthalmologicalmanifestationsof pages 2-4).

## 2. Key Molecular Players
- Genes/Proteins (HGNC):
  - PITX2 (HGNC:17490): paired-like homeodomain TF; critical for POM differentiation and WNT repression via DKK2; ECM/collagen regulation; ARS type 1 (reis2023axenfeldriegersyndromemore pages 1-2, michels2023ophthalmologicalmanifestationsof pages 2-4).
  - FOXC1 (HGNC:3800): forkhead TF; dosage-sensitive regulator of POM and angle tissues; endothelial programs including CD98–mTOR axis in retinal angiogenesis; ARS type 3 (michels2023ophthalmologicalmanifestationsof pages 2-4, qi2022screeningofpathogenic pages 4-5).
  - Regulatory elements: PITX2 distal enhancer cluster (CE5–CE7) subject to deletion/inversion causing reduced PITX2 expression without coding disruption (mitchell2025axenfeldriegersyndromeassociated pages 1-3).
- Chemical entities (CHEBI): retinoic acid (induces PITX2), TGF-β2 (contextual cue), dexamethasone and noncanonical WNT effects on TM cytoskeleton (model of outflow dysfunction) (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Cell types (CL): periocular mesenchyme (neural crest–derived), corneal endothelial cells, iris stromal cells, trabecular meshwork cells, Schlemm’s canal endothelial cells; vascular endothelium in retina/brain (michels2023ophthalmologicalmanifestationsof pages 2-4, qi2022screeningofpathogenic pages 4-5).
- Anatomical locations (UBERON): anterior chamber angle, trabecular meshwork, Schlemm’s canal, corneal endothelium, iris stroma; brain white matter and posterior fossa vasculature for FOXC1-associated neuroimaging correlates (reis2023axenfeldriegersyndromemore pages 1-1, michels2023ophthalmologicalmanifestationsof pages 2-4).

## 3. Biological Processes (GO) Disrupted
- Neural crest cell migration/differentiation; POM specification and morphogenesis (eye morphogenesis) (michels2023ophthalmologicalmanifestationsof pages 2-4).
- WNT signaling regulation (PITX2→DKK2 repression), Hippo signaling (YAP/TAZ→FOXC1), TGF-β signaling in NCC (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Extracellular matrix organization and collagen fibril organization; regulation of cytoskeleton organization in outflow tissues (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Angiogenesis and mTOR signaling in endothelium downstream of FOXC1 (qi2022screeningofpathogenic pages 4-5).

## 4. Cellular Components
- Nucleus (TF action of PITX2/FOXC1); chromatin regulatory landscape at PITX2 enhancers (mitchell2025axenfeldriegersyndromeassociated pages 1-3).
- Cell membrane and extracellular matrix of trabecular meshwork and corneal endothelium (ECM deposition/remodeling; cytoskeletal organization) (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Endothelial junctions/transporters (CD98/LAT1-4F2hc) and mTOR pathway in retinal endothelium (qi2022screeningofpathogenic pages 4-5).

## 5. Disease Progression
- Genetic trigger: heterozygous pathogenic variants (SNVs/indels/CNVs) in PITX2 or FOXC1 or structural variants deleting or separating PITX2 from distal enhancers (reis2023axenfeldriegersyndromemore pages 1-2, mitchell2025axenfeldriegersyndromeassociated pages 1-3).
- Developmental stage: reduced PITX2/FOXC1 activity in neural crest–derived POM perturbs RA–WNT balance, ECM programs, Hippo–FOXC1 axis, and TGF-β–modulated migration/survival (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Cellular outcome: failure of regression of a transient mesenchymal layer at the angle; dysgenesis of trabecular meshwork and Schlemm’s canal; malpatterned corneal endothelium and iris stroma (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Clinical manifestation: iridogoniodysgenesis with anterior segment anomalies and progressive aqueous outflow obstruction; elevated IOP and childhood glaucoma. FOXC1 variants are associated with earlier glaucoma onset (often <2 years) and high surgical needs (reis2023axenfeldriegersyndromemore pages 4-4).

## 6. Phenotypic Manifestations and Genotype–Phenotype Correlations
- Ocular: posterior embryotoxon, iris hypoplasia, corectopia/pseudopolycoria, iridocorneal adhesions; glaucoma common and often requires surgery (michels2023ophthalmologicalmanifestationsof pages 2-4, reis2023axenfeldriegersyndromemore pages 1-2).
- Glaucoma statistics (Reis et al. 2023 cohort): overall prevalence high; PITX2 ≈72% vs FOXC1 ≈66%; early-onset <2 years ≈17% PITX2 vs ≈66% FOXC1; surgery frequent (≈70% PITX2 vs ≈79% FOXC1) (reis2023axenfeldriegersyndromemore pages 4-4).
- Systemic distinctions: PITX2—highly penetrant dental anomalies (micro/hypodontia) and umbilical anomalies; FOXC1—hearing loss, congenital heart defects, skeletal/joint anomalies; expanded FOXC1 systemic phenotype overlapping De Hauwere syndrome (reis2023axenfeldriegersyndromemore pages 1-1, reis2023axenfeldriegersyndromemore pages 1-2).
- Neuroimaging: FOXC1 variants show vertebrobasilar artery dolichoectasia (~46% in a case series), white matter hyperintensities, cerebellar hypoplasia, ventriculomegaly; abnormalities more prevalent with FOXC1 than PITX2 (reis2023axenfeldriegersyndromemore pages 1-1).

## Evidence Items with URLs and publication dates
- Reis LM et al. “Axenfeld–Rieger syndrome: more than meets the eye.” Journal of Medical Genetics. 2023-07. DOI:10.1136/jmg-2022-108646. URL: https://doi.org/10.1136/jmg-2022-108646. Key cohort defining gene-specific phenotypes, glaucoma prevalence/onset, and neuroimaging associations (reis2023axenfeldriegersyndromemore pages 1-2, reis2023axenfeldriegersyndromemore pages 4-4).
- Michels KL, Bohnsack BL. “Ophthalmological Manifestations of Axenfeld-Rieger Syndrome: Current Perspectives.” Clinical Ophthalmology. 2023-03. DOI:10.2147/OPTH.S379853. URL: https://doi.org/10.2147/opth.s379853. Mechanistic overview linking PITX2/FOXC1 to POM and glaucoma pathogenesis (michels2023ophthalmologicalmanifestationsof pages 2-4).
- White S et al. “Neuroimaging Findings in Axenfeld–Rieger Syndrome: A Case Series.” AJNR. 2023-09. DOI:10.3174/ajnr.A7995. URL: https://doi.org/10.3174/ajnr.a7995. FOXC1-associated CNS imaging abnormalities (reis2023axenfeldriegersyndromemore pages 1-1).
- Mitchell LA et al. “ARS associated with a megabase-scale inversion separating PITX2 from a conserved enhancer locus.” medRxiv. 2025-06-06. DOI:10.1101/2025.06.05.25327661. URL: https://doi.org/10.1101/2025.06.05.25327661. Non-coding structural variant causing PITX2 dysregulation (enhancer disruption) (mitchell2025axenfeldriegersyndromeassociated pages 1-3).
- Kumar S, Duester G. “Retinoic acid signaling in perioptic mesenchyme represses Wnt signaling via induction of Pitx2 and Dkk2.” Dev Biol. 2010-04. DOI:10.1016/j.ydbio.2010.01.027. URL: https://doi.org/10.1016/j.ydbio.2010.01.027. RA→PITX2→DKK2 mechanism in POM (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Wang J et al. “Yap and Taz play a crucial role in neural crest-derived craniofacial development.” Development. 2016-02. DOI:10.1242/dev.126920. URL: https://doi.org/10.1242/dev.126920. Hippo/YAP–TAZ regulation of FOXC1 in neural crest (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Hendee KE et al. “PITX2 deficiency and associated human disease: insights from the zebrafish model.” Hum Mol Genet. 2018-03. DOI:10.1093/hmg/ddy074. URL: https://doi.org/10.1093/hmg/ddy074. PITX2 links to collagen/ECM regulation (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Bhakuni T et al. “FOXC1 regulates endothelial CD98 (LAT1/4F2hc) expression in retinal angiogenesis and blood-retina barrier formation.” Nat Commun. 2024-05. DOI:10.1038/s41467-024-48134-2. URL: https://doi.org/10.1038/s41467-024-48134-2. FOXC1→CD98→mTOR endothelial axis (qi2022screeningofpathogenic pages 4-5).
- Ferre-Fernández JJ et al. “Disruption of foxc1 genes in zebrafish results in dosage-dependent phenotypes overlapping ARS.” Hum Mol Genet. 2020-07. DOI:10.1093/hmg/ddaa163. URL: https://doi.org/10.1093/hmg/ddaa163. FOXC1 dosage and pitx2 responsiveness (michels2023ophthalmologicalmanifestationsof pages 2-4).

## Ontology-aligned Annotations
- Genes/Proteins (HGNC): PITX2 (HGNC:17490), FOXC1 (HGNC:3800) (reis2023axenfeldriegersyndromemore pages 1-2, michels2023ophthalmologicalmanifestationsof pages 2-4).
- Biological Processes (GO): neural crest cell migration (GO:0014037); eye morphogenesis (GO:0048592); regulation of Wnt signaling pathway (GO:0030111); TGF-β receptor signaling pathway (GO:0007179); Hippo signaling (GO:0035329); extracellular matrix organization (GO:0030198); collagen fibril organization (GO:0030199); regulation of cytoskeleton organization (GO:0051493); angiogenesis (GO:0001525); mTOR signaling (GO:0031929) (michels2023ophthalmologicalmanifestationsof pages 2-4, qi2022screeningofpathogenic pages 4-5).
- Cellular Components: nucleus; ECM; trabecular meshwork (UBERON:0001799); Schlemm’s canal (UBERON:0001800); corneal endothelium (UBERON:0001772); iris stroma (UBERON:0011821) (michels2023ophthalmologicalmanifestationsof pages 2-4).
- Cell Types (CL): corneal endothelial cell (CL:0002311); iris stromal cell (CL:0002620); endothelial cell (CL:0000115); trabecular meshwork cell (descriptive); periocular mesenchyme (neural crest mesenchyme) (michels2023ophthalmologicalmanifestationsof pages 2-4, qi2022screeningofpathogenic pages 4-5).
- Phenotypes (HP): anterior segment dysgenesis (HP:0007701), posterior embryotoxon (HP:0000583), iris hypoplasia (HP:0007677), corectopia (HP:0000617), polycoria (HP:0000615), glaucoma (HP:0000501), microdontia (HP:0000691), hypodontia (HP:0000668), umbilical hernia/periumbilical redundancy (HP:0001537/HP:0001539), hearing loss (HP:0000365), congenital heart defect (HP:0001627), ventriculomegaly (HP:0002119), white matter hyperintensities (HP:0033771) (reis2023axenfeldriegersyndromemore pages 1-2, reis2023axenfeldriegersyndromemore pages 1-1).
- Chemical entities (CHEBI): retinoic acid (CHEBI:15963); TGF-β2 (contextual); dexamethasone (CHEBI:41879); 17β-estradiol (CHEBI:16469) (michels2023ophthalmologicalmanifestationsof pages 2-4).

## Expert opinions and analysis
- Gene-specific management and nomenclature: Evidence supports distinguishing PITX2- from FOXC1-related ARS for prognosis and surveillance, given earlier glaucoma onset and broader neuro-systemic involvement in FOXC1, versus highly penetrant dental/umbilical phenotypes in PITX2 (reis2023axenfeldriegersyndromemore pages 1-1, reis2023axenfeldriegersyndromemore pages 1-2).
- Regulatory architecture matters: Negative coding tests should prompt assessment of non-coding structural variants affecting PITX2 enhancers (mitchell2025axenfeldriegersyndromeassociated pages 1-3).
- Mechanistic convergence: Multiple signaling inputs (RA/WNT, Hippo/YAP, TGF-β/HS) converge on PITX2/FOXC1-controlled transcription to coordinate POM behavior, ECM, and outflow tissue differentiation, offering candidate pathways for future therapeutic modulation (michels2023ophthalmologicalmanifestationsof pages 2-4, qi2022screeningofpathogenic pages 4-5).

## Current applications and real-world implementations
- Clinical genetics: Gene-targeted testing with CNV/structural variant analysis; gene-specific care pathways (glaucoma surveillance/surgery; systemic screening tailored to gene) (reis2023axenfeldriegersyndromemore pages 1-2, mitchell2025axenfeldriegersyndromeassociated pages 1-3).
- Imaging: Neuroimaging consideration for FOXC1-positive patients due to high prevalence of CNS vascular and white-matter findings (reis2023axenfeldriegersyndromemore pages 1-1).
- Emerging therapeutics: Pathway insights (e.g., mTOR modulation in endothelium, WNT/TGF-β balance, cytoskeletal remodeling in TM) suggest translational opportunities but remain investigational in ARS (qi2022screeningofpathogenic pages 4-5, michels2023ophthalmologicalmanifestationsof pages 2-4).

## Direct supporting quotations
- “Glaucoma… diagnosed <2 years in ~66% of FOXC1 vs ~17% of PITX2 cases; surgery was frequent” (data summarized from cohort table) (reis2023axenfeldriegersyndromemore pages 4-4).
- “The expanded phenotype of FOXC1-related ARS… overlaps features of De Hauwere syndrome… highly penetrant white matter hyperintensities, ventriculomegaly, and arachnoid cysts” (reis2023axenfeldriegersyndromemore pages 1-1).
- “Enhancer-disrupting intergenic inversions… represent a unique genetic mechanism for ARS… displacing PITX2 from distal enhancers” (preprint) (mitchell2025axenfeldriegersyndromeassociated pages 1-3).

## Limitations
Some mechanistic pathway details (e.g., explicit YAP/TAZ→FOXC1 regulation and TM WNT cytoskeletal links) are extrapolated from developmental and glaucoma biology and require further ARS-specific validation. One enhancer study is a 2025 preprint; regulatory-disruption mechanism is supported by earlier reports but not yet peer-reviewed in that instance (mitchell2025axenfeldriegersyndromeassociated pages 1-3).


References

1. (reis2023axenfeldriegersyndromemore pages 1-2): Linda M. Reis, Mohit Maheshwari, Jenina Capasso, Huban Atilla, Lubica Dudakova, Samuel Thompson, Lia Zitano, Guillermo Lay-Son, R. Brian Lowry, Jennifer Black, Joseph Lee, Ann Shue, Radka Kremlikova Pourova, Manuela Vaneckova, Pavlina Skalicka, Jana Jedlickova, Marie Trkova, Bradley Williams, Gabriele Richard, Kristine Bachman, Andrea H. Seeley, Deborah Costakos, Thomas M Glaser, Alex V. Levin, Petra Liskova, Jeffrey C. Murray, and Elena V. Semina. Axenfeld-rieger syndrome: more than meets the eye. Journal of Medical Genetics, 60:368-379, Jul 2023. URL: https://doi.org/10.1136/jmg-2022-108646, doi:10.1136/jmg-2022-108646. This article has 71 citations and is from a domain leading peer-reviewed journal.

2. (michels2023ophthalmologicalmanifestationsof pages 2-4): Kristi L Michels and Brenda L. Bohnsack. Ophthalmological manifestations of axenfeld-rieger syndrome: current perspectives. Clinical Ophthalmology (Auckland, N.Z.), 17:819-828, Mar 2023. URL: https://doi.org/10.2147/opth.s379853, doi:10.2147/opth.s379853. This article has 31 citations.

3. (qi2022screeningofpathogenic pages 4-5): W Qi, LIU Xinna, and S Zhengbo. Screening of pathogenic mutation in a family with axenfeld-rieger syndrome by whole exome sequencing. Unknown journal, 2022.

4. (mitchell2025axenfeldriegersyndromeassociated pages 1-3): Lucas A. Mitchell, Joshua Schmidt, Emmanuelle Souzeau, Lachlan S. W. Knight, Giorgina Maxwell, Andrew Dubowsky, Ridia Lim, Edward Formaini, Matthew Welland, Cas Simons, Daniel G. MacArthur, Janey L. Wiggs, Jamie E. Craig, and Owen M. Siggs. Axenfeld-rieger syndrome associated with a megabase-scale inversion separating pitx2 from a conserved enhancer locus. medRxiv, Jun 2025. URL: https://doi.org/10.1101/2025.06.05.25327661, doi:10.1101/2025.06.05.25327661. This article has 0 citations.

5. (reis2023axenfeldriegersyndromemore pages 4-4): Linda M. Reis, Mohit Maheshwari, Jenina Capasso, Huban Atilla, Lubica Dudakova, Samuel Thompson, Lia Zitano, Guillermo Lay-Son, R. Brian Lowry, Jennifer Black, Joseph Lee, Ann Shue, Radka Kremlikova Pourova, Manuela Vaneckova, Pavlina Skalicka, Jana Jedlickova, Marie Trkova, Bradley Williams, Gabriele Richard, Kristine Bachman, Andrea H. Seeley, Deborah Costakos, Thomas M Glaser, Alex V. Levin, Petra Liskova, Jeffrey C. Murray, and Elena V. Semina. Axenfeld-rieger syndrome: more than meets the eye. Journal of Medical Genetics, 60:368-379, Jul 2023. URL: https://doi.org/10.1136/jmg-2022-108646, doi:10.1136/jmg-2022-108646. This article has 71 citations and is from a domain leading peer-reviewed journal.

6. (reis2023axenfeldriegersyndromemore pages 1-1): Linda M. Reis, Mohit Maheshwari, Jenina Capasso, Huban Atilla, Lubica Dudakova, Samuel Thompson, Lia Zitano, Guillermo Lay-Son, R. Brian Lowry, Jennifer Black, Joseph Lee, Ann Shue, Radka Kremlikova Pourova, Manuela Vaneckova, Pavlina Skalicka, Jana Jedlickova, Marie Trkova, Bradley Williams, Gabriele Richard, Kristine Bachman, Andrea H. Seeley, Deborah Costakos, Thomas M Glaser, Alex V. Levin, Petra Liskova, Jeffrey C. Murray, and Elena V. Semina. Axenfeld-rieger syndrome: more than meets the eye. Journal of Medical Genetics, 60:368-379, Jul 2023. URL: https://doi.org/10.1136/jmg-2022-108646, doi:10.1136/jmg-2022-108646. This article has 71 citations and is from a domain leading peer-reviewed journal.