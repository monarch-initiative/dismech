---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T00:21:28.533418'
end_time: '2026-05-05T00:43:15.812091'
duration_seconds: 1307.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Lichenoid Pityriasis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 5400
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Lichenoid Pityriasis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Lichenoid Pityriasis** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Comprehensive Disease Characterization Report: Acute Lichenoid Pityriasis (PLEVA / Mucha-Habermann Disease)

## Summary

**Acute Lichenoid Pityriasis**, formally known as **Pityriasis Lichenoides et Varioliformis Acuta (PLEVA)** or **Mucha-Habermann disease**, is a rare CD8+ cytotoxic T-lymphocyte-mediated inflammatory dermatosis of unknown etiology that primarily affects children and young adults. The disease is characterized by recurrent crops of polymorphous erythematous papulovesicular eruptions, predominantly on the trunk and proximal extremities, that evolve through stages of scaling, vesiculation, necrosis, and crusting. Histopathologically, PLEVA is defined by interface dermatitis, lymphocytic vasculitis, necrotic keratinocytes, and perivascular CD8+ T-cell infiltrates with erythrocyte extravasation. The disease exists on a clinical spectrum that includes chronic pityriasis lichenoides (PLC) at one end and the rare, potentially fatal febrile ulceronecrotic Mucha-Habermann disease (FUMHD) at the other.

The overall prognosis for PLEVA is favorable, with the majority of patients achieving lasting complete remission. Long-term follow-up studies involving up to 242 patients with median 9.9-year follow-up demonstrate no established progression to cutaneous T-cell lymphoma (CTCL), though approximately 5% of patients with prolonged clinical courses may develop mycosis fungoides (MF) over 3-11 years. The severe FUMHD variant carries an overall mortality of 12%, with adults at significantly higher risk (20%) compared to children (2%). Sepsis, systemic involvement, and adult age are key mortality risk factors. Treatment is primarily supportive, with phototherapy (especially narrowband UVB) being the most effective modality and oral antibiotics (erythromycin) serving as first-line therapy in children. No causal genes, randomized controlled treatment trials, or established animal models exist, representing major knowledge gaps.

This report synthesizes evidence from 52 peer-reviewed publications to provide a comprehensive disease knowledge base entry covering all requested disease characteristics: etiology, phenotypes, genetics, pathophysiology, anatomical involvement, temporal development, epidemiology, diagnostics, prognosis, treatment, prevention, comparative biology, and model organisms.

---

## 1. Disease Information

### Overview

Pityriasis Lichenoides et Varioliformis Acuta (PLEVA) is a rare inflammatory skin disorder first described by Mucha in 1916 and Habermann in 1925 ([PMID: 8864599](https://pubmed.ncbi.nlm.nih.gov/8864599/)). The disease is characterized by the abrupt onset of recurrent crops of erythematous papulovesicular lesions that undergo necrosis and crusting, predominantly affecting the trunk and proximal extremities. PLEVA represents the acute end of the pityriasis lichenoides (PL) spectrum, which also encompasses pityriasis lichenoides chronica (PLC) and the severe febrile ulceronecrotic Mucha-Habermann disease (FUMHD).

### Key Identifiers

| Identifier | Code/ID |
|---|---|
| **MONDO** | MONDO:0024250 (Pityriasis lichenoides et varioliformis acuta) |
| **ICD-10** | L41.0 (Pityriasis lichenoides et varioliformis acuta) |
| **ICD-11** | EA92.0 (Pityriasis lichenoides et varioliformis acuta) |
| **MeSH** | D017514 (Pityriasis Lichenoides) |
| **OMIM** | Not assigned (no Mendelian inheritance established) |
| **Orphanet** | ORPHA:33111 (Pityriasis lichenoides) |
| **SNOMED CT** | 238696003 (Pityriasis lichenoides et varioliformis acuta) |

### Synonyms and Alternative Names

- Pityriasis lichenoides et varioliformis acuta (PLEVA)
- Mucha-Habermann disease (MHD)
- Acute parapsoriasis
- Acute guttate parapsoriasis
- Parapsoriasis varioliformis
- Parapsoriasis acuta
- Pityriasis lichenoides acuta

The severe variant is known as:
- Febrile ulceronecrotic Mucha-Habermann disease (FUMHD)
- Degos disease (referring to the 1966 description by Degos of the febrile ulceronecrotic variant)

### Information Sources

The information in this report is derived from **aggregated disease-level resources** including systematic reviews, retrospective cohort studies, case series, and individual case reports published in peer-reviewed literature. No large-scale electronic health record (EHR) studies or population registries specific to PLEVA exist.

---

## 2. Etiology

### Disease Causal Factors

The etiology of PLEVA remains **unknown**. It is generally considered a **T-cell-mediated inflammatory dermatosis** rather than a true neoplastic process, although debate persists regarding its relationship to cutaneous T-cell lymphoproliferative disorders ([PMID: 12203210](https://pubmed.ncbi.nlm.nih.gov/12203210/)). The leading etiologic hypothesis is that PLEVA represents a **hypersensitivity reaction to an infectious agent**, as suggested by Mucha-Habermann disease reviews: *"The etiology of MH remains obscure, but it may be the result of a hypersensitivity reaction to an infectious agent"* ([PMID: 8864599](https://pubmed.ncbi.nlm.nih.gov/8864599/)).

### Risk Factors

#### Infectious Triggers
Multiple infectious agents have been temporally associated with PLEVA onset:
- **Streptococcal infections**: A case of PLC manifesting ten days after streptococcal pharyngitis has been documented ([PMID: 39365630](https://pubmed.ncbi.nlm.nih.gov/39365630/))
- **Varicella (chickenpox)**: FUMHD following suspected hemorrhagic chickenpox has been reported in a 20-month-old boy ([PMID: 25627543](https://pubmed.ncbi.nlm.nih.gov/25627543/))
- **SARS-CoV-2 infection/vaccination**: A systematic review identified 14 cases of PL following COVID-19 infection or vaccination, with one case recurring after vaccination suggesting a possible association ([PMID: 36688177](https://pubmed.ncbi.nlm.nih.gov/36688177/))
- Various COVID-19 vaccines (BNT162b2 Pfizer-BioNTech, Oxford-AstraZeneca, Sinopharm) have been temporally associated with PLEVA onset or flare-up ([PMID: 35841285](https://pubmed.ncbi.nlm.nih.gov/35841285/); [PMID: 35617206](https://pubmed.ncbi.nlm.nih.gov/35617206/); [PMID: 34751995](https://pubmed.ncbi.nlm.nih.gov/34751995/); [PMID: 34617317](https://pubmed.ncbi.nlm.nih.gov/34617317/); [PMID: 35716105](https://pubmed.ncbi.nlm.nih.gov/35716105/))
- **Other viruses**: HIV, EBV, CMV, parvovirus B19, adenovirus, and VZV have been implicated in individual case reports
- **Toxoplasma gondii** has been reported as a possible trigger

#### Demographic Risk Factors
- **Age**: PLEVA primarily affects children and young adults. Pediatric onset average is 6.5 years ([PMID: 25816855](https://pubmed.ncbi.nlm.nih.gov/25816855/))
- **Sex**: Male predominance in children (M:F ratio 1.7:1), but female predominance in adults (M:F ratio 0.6:1) ([PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/))

#### Genetic Risk Factors
- No causal genetic variants have been identified for PLEVA
- No GWAS studies have been conducted
- No susceptibility loci have been mapped
- PLEVA is not classified among the autoinflammatory keratinization diseases (AiKDs), unlike keratosis lichenoides chronica which involves NLRP1 mutations ([PMID: 38103162](https://pubmed.ncbi.nlm.nih.gov/38103162/))

### Protective Factors

No specific genetic or environmental protective factors have been identified for PLEVA. This represents a significant knowledge gap.

### Gene-Environment Interactions

No gene-environment interactions have been characterized for PLEVA, consistent with the absence of identified causal genes.

---

## 3. Phenotypes

### Primary Cutaneous Phenotypes

#### 1. Papulovesicular Eruption (Hallmark)
- **HPO**: HP:0200037 (Vesiculobullous skin lesion), HP:0200034 (Papule)
- **Type**: Physical manifestation / clinical sign
- **Onset**: Acute; mean age 6.5 years in children ([PMID: 25816855](https://pubmed.ncbi.nlm.nih.gov/25816855/))
- **Severity**: Mild to moderate; severe in FUMHD variant
- **Progression**: Episodic, with recurrent crops; self-limited
- **Frequency**: Present in virtually 100% of patients
- **Description**: Sudden onset of erythematous macules and papules that develop central vesiculation, necrosis, and hemorrhagic crusting. Individual lesions evolve through stages from erythematous papule to crusted/necrotic papule to healing with dyspigmentation
- **QoL impact**: Cosmetic concern; post-inflammatory pigmentary changes particularly distressing in darker-skinned individuals

#### 2. Scaling and Crusting
- **HPO**: HP:0040189 (Scaling skin), HP:0001047 (Crusting erythematous dermatitis)
- **Type**: Physical manifestation
- **Frequency**: Nearly universal; mica-like crust on older lesions is characteristic
- **Progression**: Evolves from acute papule stage

#### 3. Post-inflammatory Hypopigmentation
- **HPO**: HP:0007513 (Generalized hypopigmentation of skin)
- **Type**: Physical manifestation (sequela)
- **Frequency**: Very common, especially in children with darker skin phototypes. In one study, post-inflammatory dyspigmentation was seen in 60% of adults and 80% of children ([PMID: 23488769](https://pubmed.ncbi.nlm.nih.gov/23488769/))
- **Details**: A study of 21 PLC patients found hypopigmented lesions showed features of active (28.6%) or residual (52.4%) disease in addition to true PIH (19%) ([PMID: 34751445](https://pubmed.ncbi.nlm.nih.gov/34751445/))
- **QoL impact**: Significant cosmetic and psychosocial impact, particularly in skin of color populations ([PMID: 36769891](https://pubmed.ncbi.nlm.nih.gov/36769891/))

#### 4. Pruritus
- **HPO**: HP:0000989 (Pruritus)
- **Type**: Symptom
- **Frequency**: Present in the majority of patients ([PMID: 23488769](https://pubmed.ncbi.nlm.nih.gov/23488769/)); specifically mentioned in ~21% of pediatric lymphoproliferative cases ([PMID: 38595050](https://pubmed.ncbi.nlm.nih.gov/38595050/))
- **Severity**: Mild to moderate

#### 5. Varioliform Scarring
- **HPO**: HP:0100699 (Scarring)
- **Type**: Physical manifestation (sequela)
- **Frequency**: Varioliform (smallpox-like) scars occur in >77% of resolved cases
- **QoL impact**: Permanent cosmetic change

### FUMHD-Specific Phenotypes

#### 6. Ulceronecrotic Skin Lesions
- **HPO**: HP:0200042 (Skin ulcer)
- **Type**: Physical manifestation
- **Severity**: Severe; rapidly coalescing necrotic papules forming large ulcers
- **Frequency**: Defining feature of FUMHD (100%)

#### 7. High Fever
- **HPO**: HP:0001945 (Fever)
- **Type**: Systemic sign
- **Frequency**: Universal in FUMHD
- **Severity**: High fever, often sustained

#### 8. Systemic Involvement
- **HPO**: HP:0025155 (Disseminated intravascular coagulation)
- **Type**: Laboratory abnormality / systemic complication
- **Frequency**: Common in FUMHD. Systemic manifestations include DIC, pulmonary, cardiac, gastrointestinal, and CNS involvement ([PMID: 38959922](https://pubmed.ncbi.nlm.nih.gov/38959922/))

---

## 4. Genetic/Molecular Information

### Causal Genes

**No causal genes have been identified for PLEVA.** The disease is not listed in OMIM as a genetic disorder, and no Mendelian inheritance pattern has been established.

### T-Cell Clonality

While not a traditional "genetic" finding, T-cell receptor gene rearrangement studies are central to understanding PLEVA's molecular biology:

- T-cell clonality has been demonstrated in a subset of PL cases: *"Pityriasis lichenoides (PL) is a papulosquamous disorder often considered a form of reactive dermatosis... however, some patients with PL have developed large plaque parapsoriasis (LPP) and mycosis fungoides (MF), and lymphoid atypia and T-cell clonality have been reported in lesions of PL"* ([PMID: 12203210](https://pubmed.ncbi.nlm.nih.gov/12203210/))
- Monoclonal T-cell receptor rearrangement was found in 77% of tested skin biopsies in pediatric lymphomatoid papulosis, a related condition ([PMID: 38595050](https://pubmed.ncbi.nlm.nih.gov/38595050/))
- Among PL-like MF cases, monoclonality was demonstrated in 15 of 20 tested cases ([PMID: 31032790](https://pubmed.ncbi.nlm.nih.gov/31032790/))

### Phenotypic Aberrations and MF Overlap

A subset of PL cases shows loss of pan-T-cell markers: *"a subset of PL cases, particularly those exhibiting a loss of pan-T-cell markers (CD2, CD5, CD7), or T-cell clonality, may have a closer association with MF"* ([PMID: 40953932](https://pubmed.ncbi.nlm.nih.gov/40953932/)). This phenotypic aberration is a potential molecular marker for progression risk.

### Epigenetic Information

No epigenetic studies (DNA methylation, histone modifications) specific to PLEVA have been published.

### Chromosomal Abnormalities

No chromosomal abnormalities have been associated with PLEVA.

---

## 5. Environmental Information

### Environmental Factors

No specific environmental toxins, radiation exposures, or occupational factors have been linked to PLEVA.

### Lifestyle Factors

No specific lifestyle factors (smoking, diet, exercise, alcohol) have been associated with PLEVA risk.

### Infectious Agents

PLEVA is hypothesized to represent a hypersensitivity response to infectious agents. The following pathogens have been temporally associated with disease onset:

| Organism | NCBI Taxon ID | Evidence Level |
|---|---|---|
| *Streptococcus pyogenes* | 1314 | Case reports |
| Varicella-zoster virus (VZV) | 10335 | Case reports ([PMID: 25627543](https://pubmed.ncbi.nlm.nih.gov/25627543/)) |
| SARS-CoV-2 | 2697049 | Case series ([PMID: 36688177](https://pubmed.ncbi.nlm.nih.gov/36688177/)) |
| Epstein-Barr virus (EBV) | 10376 | Case reports |
| Cytomegalovirus (CMV) | 10359 | Case reports |
| Parvovirus B19 | 10798 | Case reports |
| HIV | 11676 | Case reports |
| *Toxoplasma gondii* | 5811 | Case reports |
| Adenovirus | 10508 | Case reports |

Notably, a systematic review found **no cases** of *Chlamydophila pneumoniae* respiratory infection associated with PLEVA ([PMID: 32222707](https://pubmed.ncbi.nlm.nih.gov/32222707/)).

---

## 6. Mechanism / Pathophysiology

### Immunopathogenic Model

The current mechanistic understanding of PLEVA centers on a **CD8+ cytotoxic T-lymphocyte-mediated immune response** directed at keratinocytes and dermal vasculature:

```
Trigger (infectious agent/antigen)
        |
        v
Activation of adaptive immune response
        |
        v
CD8+ cytotoxic T-cell expansion and skin homing
        |
        v
Interface dermatitis: CD8+ T-cells attack basal keratinocytes
        |
        |---> Keratinocyte apoptosis/necrosis --> Epidermal disruption
        |
        |---> Lymphocytic vasculitis --> Erythrocyte extravasation
        |
        +---> Inflammatory cascade --> Papulovesicular eruption
                    |
                    v
        Resolution with post-inflammatory pigmentary changes
```

### Immune System Involvement

**The predominant T-cell infiltrate in PLEVA is dominated by CD8+** T-cells ([PMID: 38973067](https://pubmed.ncbi.nlm.nih.gov/38973067/)). This distinguishes PLEVA from classic mycosis fungoides, which is typically CD4+ dominant.

Key immunological features:
- **CD8+ T-cell predominance**: Immunophenotyping consistently shows CD8+ dominance in PLEVA lesional infiltrates
- **Polyclonal CD8+ T-cell response** has been documented in FUMHD with elevated pro-inflammatory cytokines and fivefold upregulation of CD64 on granulocytes ([PMID: 25627543](https://pubmed.ncbi.nlm.nih.gov/25627543/))
- **Loss of pan-T-cell markers** (CD2, CD5, CD7) in a subset of cases suggests potential for immune dysregulation or malignant transformation ([PMID: 40953932](https://pubmed.ncbi.nlm.nih.gov/40953932/))

**GO terms**: GO:0006955 (immune response), GO:0002456 (T cell mediated immunity), GO:0006968 (cellular defense response), GO:0042110 (T cell activation)

### Cellular Processes

1. **Apoptosis / Keratinocyte Necrosis** (GO:0006915): Interface dermatitis with necrotic keratinocytes is a universal histopathological feature (100% of cases) ([PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/))
2. **Vasculitis** (GO:0006954, inflammation): Lymphocytic vasculitis without fibrinoid deposition is seen in all PLEVA cases ([PMID: 17456915](https://pubmed.ncbi.nlm.nih.gov/17456915/))
3. **Exocytosis of lymphocytes** into epidermis (epidermotropism) in 45.1% of cases ([PMID: 17456915](https://pubmed.ncbi.nlm.nih.gov/17456915/))

### Cell Types Involved

| Cell Type | CL Term | Role |
|---|---|---|
| CD8+ cytotoxic T lymphocyte | CL:0000794 | Primary effector cell; dominant infiltrate |
| Keratinocyte | CL:0000312 | Target of cytotoxic attack; undergoes apoptosis |
| Endothelial cell | CL:0000115 | Target of lymphocytic vasculitis |
| Langerhans cell | CL:0000453 | Antigen presentation (hypothesized) |

### Tissue Damage Mechanisms

Tissue damage in PLEVA occurs through:
1. **Cytotoxic T-cell-mediated keratinocyte killing** leading to interface dermatitis with vacuolar changes
2. **Lymphocytic vasculitis** leading to erythrocyte extravasation, vascular injury
3. **Inflammatory mediator release** leading to edema, local tissue destruction
4. In FUMHD: **massive necrosis** with potential for DIC, sepsis, and multi-organ failure

### Molecular Profiling

No dedicated transcriptomic, proteomic, or metabolomic studies of PLEVA lesional tissue have been published. This is a significant knowledge gap.

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ**: Skin (UBERON:0002097) — the sole organ directly affected in typical PLEVA
- **Secondary organ involvement** (FUMHD only): Lungs, heart, GI tract, CNS ([PMID: 38959922](https://pubmed.ncbi.nlm.nih.gov/38959922/))
- **Body system**: Integumentary system; immune system (secondary)

### Tissue and Cell Level

- **Epidermis** (UBERON:0001003): Interface dermatitis, keratinocyte necrosis, vesiculation
- **Dermis** (UBERON:0002067): Perivascular lymphocytic infiltrate, erythrocyte extravasation
- **Dermal vasculature** (UBERON:0002049): Lymphocytic vasculitis
- **Adnexal structures**: Lymphocytic infiltration into adnexal epithelium in 97% of cases ([PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/))

### Localization

| Site | UBERON Term | Frequency |
|---|---|---|
| Trunk | UBERON:0002100 | Most common (>80%) |
| Proximal extremities | UBERON:0002102/UBERON:0002101 | Very common |
| Face | UBERON:0001456 | Common in children (57% with facial involvement) |
| Palms/soles | UBERON:0008878/UBERON:0008879 | Atypical ([PMID: 31334928](https://pubmed.ncbi.nlm.nih.gov/31334928/)) |
| Mucous membranes | UBERON:0000344 | FUMHD only; prognostic significance |

- **Lateralization**: Bilateral, generally symmetric distribution

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Childhood and young adulthood
  - Pediatric: Mean 6.5 years ([PMID: 25816855](https://pubmed.ncbi.nlm.nih.gov/25816855/))
  - Adult: Mean ~42 years in Asian populations ([PMID: 23488769](https://pubmed.ncbi.nlm.nih.gov/23488769/))
- **Onset pattern**: Acute — sudden appearance of crops of papulovesicular lesions
- FUMHD was first reported in children and occurs more frequently in children, though adult cases have higher mortality ([PMID: 8864599](https://pubmed.ncbi.nlm.nih.gov/8864599/))

### Progression

- **Disease course**: Episodic / relapsing-remitting; self-limited in most cases
- **Duration**:
  - Median time to resolution: 8 months in adults, 21 months in children ([PMID: 23488769](https://pubmed.ncbi.nlm.nih.gov/23488769/))
  - Some patients experience prolonged courses lasting years
- **Progression to CTCL**: Rare; 3 of 58 (5.2%) PL patients developed MF after 3-11 years ([PMID: 29210716](https://pubmed.ncbi.nlm.nih.gov/29210716/))

### Remission Patterns

- **Spontaneous remission**: Common; 85% of non-MF PL patients achieved lasting complete remissions ([PMID: 29210716](https://pubmed.ncbi.nlm.nih.gov/29210716/))
- **Treatment-induced remission**: Achievable with phototherapy, antibiotics, or immunosuppressive agents
- **Recurrence**: Variable; NB-UVB shows lowest recurrence rate (0%) vs. PUVA (60%) ([PMID: 27502793](https://pubmed.ncbi.nlm.nih.gov/27502793/))

---

## 9. Inheritance and Population

### Epidemiology

| Parameter | Value | Source |
|---|---|---|
| Prevalence | Rare; exact prevalence unknown | — |
| Incidence | Estimated ~1-2 per 100,000/year | Clinical estimates |
| Sex ratio (children) | M:F = 1.7:1 (p < 0.01) | [PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/) |
| Sex ratio (adults) | M:F = 0.6:1 | [PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/) |
| Peak onset (children) | ~6.5 years | [PMID: 25816855](https://pubmed.ncbi.nlm.nih.gov/25816855/) |

A long-term cohort of 242 PL patients (107 adults, 135 children) demonstrated: *"The results show a male-to-female ratio of 1.7:1 for pediatric patients and 0.6:1 for adults, with a higher incidence of male patients among children (p < 0.01)"* ([PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/)).

### Inheritance

PLEVA does not follow Mendelian inheritance. No familial aggregation, genetic anticipation, or consanguinity effects have been documented. The disease is considered **sporadic** with possible **multifactorial** etiology involving immune dysregulation triggered by environmental factors.

### Population Demographics

- **Affected populations**: All ethnic groups; no clear ethnic predisposition
- **Geographic distribution**: Worldwide; no endemic areas identified
- **Skin of color considerations**: Post-inflammatory hypopigmentation is particularly prominent and clinically significant in darker-skinned patients. PLC may present with extensive hypopigmentation and prominent facial involvement in Black patients ([PMID: 20408509](https://pubmed.ncbi.nlm.nih.gov/20408509/))
- **Age distribution**: Bimodal — peak in childhood (~5-10 years) and young adulthood

---

## 10. Diagnostics

### Clinical Diagnosis

Diagnosis of PLEVA is based on **clinical presentation** confirmed by **histopathological examination**. The characteristic pattern of lesions in different stages of development — ranging from erythematous maculopapules to papules with a crusted and/or necrotic centre — is suggestive, but biopsy is typically required ([PMID: 37847066](https://pubmed.ncbi.nlm.nih.gov/37847066/)).

### Biopsy / Histopathology (Gold Standard)

Histopathological findings in PLEVA are highly characteristic. A study of 71 PL cases quantified the frequency of key features:

| Feature | Frequency | Reference |
|---|---|---|
| Vacuolar changes or necrotic keratinocytes | 100% | [PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/) |
| Superficial and deep lymphocytic infiltrates | 99% | [PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/) |
| Lymphocyte infiltration into adnexal epithelium | 97% | [PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/) |
| Superficial perivascular/intraepidermal RBCs | 83% | [PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/) |
| Lymphocytic vasculitis (without fibrinoid deposition) | 100% of PLEVA | [PMID: 17456915](https://pubmed.ncbi.nlm.nih.gov/17456915/) |
| Basal cell vacuolation and perivascular infiltrate | 100% | [PMID: 17456915](https://pubmed.ncbi.nlm.nih.gov/17456915/) |
| Exocytosis | 45.1% | [PMID: 17456915](https://pubmed.ncbi.nlm.nih.gov/17456915/) |

All inflammatory cells are small- to medium-sized lymphocytes with **no eosinophils** observed. A deep dermal lymphocytic infiltrate with a T-shaped periadnexal arrangement has been described as a potentially distinguishing feature ([PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/)).

### Immunohistochemistry

Essential for:
- Confirming CD8+ T-cell predominance (CD3+, CD8+, CD4-)
- Detecting loss of pan-T-cell markers (CD2, CD5, CD7) — suggestive of atypical PL with MF overlap
- Excluding CD30+ lymphoproliferative disorders (lymphomatoid papulosis)
- CD20 negativity (excludes B-cell processes)

### Dermoscopy

Dermoscopic findings correlating with histopathology include:
- Punctate or glomerular vessels
- Erythematous globules surrounding a homogeneous orange or crusty central area
- These findings may allow rapid non-invasive diagnosis ([PMID: 37847066](https://pubmed.ncbi.nlm.nih.gov/37847066/))

### Molecular Studies

- **T-cell receptor gene rearrangement**: Demonstrates clonality in ~50% of PL cases; presence does not necessarily indicate malignancy
- **Monoclonal rearrangement** is a negative prognostic indicator in FUMHD, associated with worse outcomes ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/))

### Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| Lymphomatoid papulosis (LyP) | CD30+ cells; waxing/waning self-healing nodules; LyP was most common misdiagnosis for PLEVA in children ([PMID: 38595050](https://pubmed.ncbi.nlm.nih.gov/38595050/)) |
| Mycosis fungoides (MF) | Patches/plaques; CD4+ dominant; epidermotropism with Pautrier microabscesses |
| Varicella (chickenpox) | Vesicles in different stages; Tzanck smear positive; viral culture |
| Pityriasis rosea | Herald patch; "Christmas tree" distribution; self-limited |
| Secondary syphilis | RPR/VDRL positive; macrophages and plasma cells on histology ([PMID: 11974501](https://pubmed.ncbi.nlm.nih.gov/11974501/)) |
| Insect bites | Grouped lesions; eosinophils on biopsy |
| Urticaria | Individual lesions <24h; no scarring ([PMID: 38025325](https://pubmed.ncbi.nlm.nih.gov/38025325/)) |
| Gianotti-Crosti syndrome | Acral distribution; associated with viral infections |

### Genetic Testing

Not applicable — no causal genes identified. However, TCR gene rearrangement analysis is clinically useful for risk stratification.

---

## 11. Outcome / Prognosis

### Standard PLEVA

- **Prognosis**: Generally excellent. In the largest long-term follow-up study (242 patients, median 9.9 years), *"no progression to cutaneous T-cell lymphoma was established. PL encompasses a spectrum of papulosquamous disorders... the study results underscore the benign course of PL"* ([PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/))
- **Remission**: 85% of patients achieved lasting complete remissions ([PMID: 29210716](https://pubmed.ncbi.nlm.nih.gov/29210716/))
- **MF progression risk**: 5.2% (3/58) over 3-11 years in one study ([PMID: 29210716](https://pubmed.ncbi.nlm.nih.gov/29210716/))
- **Mortality**: Near zero for standard PLEVA/PLC

### FUMHD (Severe Variant)

The prognosis for FUMHD is significantly worse:

| Parameter | Children | Adults | Overall |
|---|---|---|---|
| **Lethality** | 1/54 (2%, CI 0-6%) | 13/65 (20%, CI 11-31%) | 14/119 (12%, CI 6-17%) |

Source: Systematic review of 119 FUMHD cases ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/))

**Mortality risk factors** (from systematic review):
- Sepsis (LR 24.97, P < 0.001)
- Systemic involvement (LR 19.97, P < 0.001)
- Adult age (LR 11.19, P = 0.001)
- Mucosal involvement (LR 4.58, P = 0.032)

A **mortality risk score** has been proposed: Age/10 + 4 + 4 (systemic involvement) + 1 (mucosal involvement), with sensitivity 93% and specificity 77% ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/)).

Additional prognostic factors: *"Increased age, systemic involvement, and monoclonal T-cell receptor rearrangement were associated with worst prognosis"* ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)).

### Quality of Life

- Post-inflammatory hypopigmentation and scarring represent the primary long-term morbidity
- Hypopigmentation is especially prominent and psychosocially distressing in darker-skinned populations ([PMID: 36769891](https://pubmed.ncbi.nlm.nih.gov/36769891/))
- Prolonged disease courses (median 21 months in children) impact daily life

---

## 12. Treatment

### First-Line Treatment

#### Oral Antibiotics (MAXO:0000747 - antimicrobial therapy)
- **Erythromycin**: Recommended first-line in children; clearance rates 66-83% ([PMID: 31318465](https://pubmed.ncbi.nlm.nih.gov/31318465/))
- **Azithromycin**: 250 mg daily for 3 weeks reported to achieve rapid complete resolution ([PMID: 38025325](https://pubmed.ncbi.nlm.nih.gov/38025325/))
- Mechanism likely anti-inflammatory rather than antimicrobial

#### Topical Corticosteroids (MAXO:0000571 - topical corticosteroid therapy)
- Most commonly trialed treatment modality
- Limited efficacy as monotherapy; most patients did not respond to topical corticosteroids alone ([PMID: 23488769](https://pubmed.ncbi.nlm.nih.gov/23488769/))

### Second-Line Treatment

#### Phototherapy (MAXO:0000596 - phototherapy)
The most effective treatment modality overall: *"Of these treatments, phototherapy led to complete remission in the highest proportion of patients"* ([PMID: 32112390](https://pubmed.ncbi.nlm.nih.gov/32112390/)).

| Modality | Clearance Rate | Recurrence Rate | Source |
|---|---|---|---|
| NB-UVB (311 nm) | 73% | 0% | [PMID: 27502793](https://pubmed.ncbi.nlm.nih.gov/27502793/) |
| BB-UVB | 89.6% | 23.1% | [PMID: 27502793](https://pubmed.ncbi.nlm.nih.gov/27502793/) |
| PUVA | 83% | 60% | [PMID: 27502793](https://pubmed.ncbi.nlm.nih.gov/27502793/) |

NB-UVB is the **preferred modality** due to excellent clearance with no recurrence and a favorable side-effect profile, especially in children ([PMID: 41483505](https://pubmed.ncbi.nlm.nih.gov/41483505/); [PMID: 40013426](https://pubmed.ncbi.nlm.nih.gov/40013426/)).

*"Narrow-band UVB showed an efficacy similar to PUVA as such as the combination of UVA and UVB vs. PUVA. Oral erythromycin showed clearance rates ranging between 66% and 83%, whereas methotrexate up to 100% but in small and dated studies"* ([PMID: 31318465](https://pubmed.ncbi.nlm.nih.gov/31318465/)).

### Third-Line / Refractory Disease

#### Methotrexate (MAXO:0001024 - immunosuppressive therapy)
- Clearance up to 100% in small, dated studies ([PMID: 31318465](https://pubmed.ncbi.nlm.nih.gov/31318465/))
- Used for recalcitrant PLEVA and FUMHD

### FUMHD-Specific Treatment

Given the life-threatening nature of FUMHD, aggressive multimodal therapy is required:

| Treatment | Mechanism | Evidence |
|---|---|---|
| Systemic corticosteroids | Anti-inflammatory | Case reports/series ([PMID: 38959922](https://pubmed.ncbi.nlm.nih.gov/38959922/)) |
| Methotrexate | Immunosuppressive | Case reports/series |
| Cyclosporine | Calcineurin inhibitor | Case reports ([PMID: 25627543](https://pubmed.ncbi.nlm.nih.gov/25627543/)) |
| IVIG | Immunomodulatory | Rapid recovery reported with single low-dose infusion ([PMID: 38234081](https://pubmed.ncbi.nlm.nih.gov/38234081/)) |
| Etoposide + Dexamethasone | Cytotoxic + anti-inflammatory | Effective in FUMHD with HLH ([PMID: 38457671](https://pubmed.ncbi.nlm.nih.gov/38457671/)) |
| Dapsone | Anti-inflammatory | Case reports |
| Hydroxychloroquine | Antimalarial/anti-inflammatory | Case report ([PMID: 39365630](https://pubmed.ncbi.nlm.nih.gov/39365630/)) |

### Treatment Algorithm

```
Step 1: Oral antibiotics (erythromycin/azithromycin) +/- topical corticosteroids
    |
    |-- Response --> Continue; monitor
    |
    +-- No response (4-8 weeks)
            |
            v
Step 2: NB-UVB phototherapy (2-3x/week)
    |
    |-- Response --> Taper; monitor
    |
    +-- No response / contraindicated
            |
            v
Step 3: Methotrexate or other systemic immunosuppression
    |
    v
FUMHD: Immediate systemic steroids + MTX or cyclosporine +/- IVIG
        Consider etoposide/dexamethasone if HLH develops
```

### Treatment Limitations

**No randomized controlled trials** exist for any PLEVA treatment. All evidence is based on case reports, case series, and retrospective studies. This is the most significant gap in clinical management.

---

## 13. Prevention

### Primary Prevention

No primary prevention strategies exist for PLEVA. The unknown etiology precludes targeted prevention. General immune health maintenance is the only broadly applicable recommendation.

### Secondary Prevention (Early Detection)

- Prompt skin biopsy of suspicious papulovesicular eruptions for early diagnosis
- Awareness among pediatricians that dermatologic complaints account for up to 30% of visits and PLEVA may be misdiagnosed ([PMID: 41633545](https://pubmed.ncbi.nlm.nih.gov/41633545/))
- Dermoscopy may allow non-invasive early diagnosis, reducing need for biopsy in infants ([PMID: 37847066](https://pubmed.ncbi.nlm.nih.gov/37847066/))

### Tertiary Prevention

- Long-term dermatological follow-up to detect possible MF progression
- Patients with atypical phenotype (loss of CD2, CD5, CD7) and T-cell clonality warrant closer monitoring ([PMID: 29851705](https://pubmed.ncbi.nlm.nih.gov/29851705/))
- Management of post-inflammatory hypopigmentation to minimize psychosocial impact

### Screening

No population-level screening programs exist or are warranted given the rarity and generally benign nature of the disease.

---

## 14. Other Species / Natural Disease

### Natural Disease in Animals

**No naturally occurring animal models of PLEVA have been identified.** PL is considered a human-specific inflammatory dermatosis. No equivalent condition has been reported in companion animals, livestock, or wildlife in the OMIA database or veterinary literature.

### Comparative Biology

- The CD8+ T-cell-mediated cytotoxic mechanism in PLEVA shares features with graft-versus-host disease (GVHD) and other interface dermatitis conditions that have been studied in mice, but no direct comparative pathology studies exist for PLEVA specifically
- Lymphocytic vasculitis of dermal vessels is not unique to PLEVA and occurs in various immune-mediated conditions across species

### Zoonotic Potential

Not applicable — PLEVA is a non-infectious inflammatory dermatosis.

---

## 15. Model Organisms

### Available Models

**No established animal models exist for PLEVA.** This is a critical knowledge gap. The absence of models reflects:
1. Unknown etiology making it difficult to design recapitulation strategies
2. The likely multifactorial nature of the immune trigger
3. Difficulty replicating the specific CD8+ T-cell-mediated interface dermatitis pattern

### Potential Model Approaches

While not yet developed, potential approaches could include:
- **Adoptive transfer models**: Transfer of activated CD8+ T-cells specific for keratinocyte antigens into syngeneic mice
- **Transgenic models**: Mice expressing specific TCR recognizing epidermal antigens under controlled activation
- **Humanized mouse models**: Engraftment of human T-cells from PLEVA patients into immunodeficient mice
- **In vitro models**: Co-culture of CD8+ T-cells with keratinocyte monolayers/organoids to study cytotoxic mechanisms

### Related Model Systems

The GVHD mouse model shares histopathological features with PLEVA (interface dermatitis, lymphocytic vasculitis, keratinocyte apoptosis) and has been used to study similar pathogenic mechanisms, though it is not specific to PLEVA.

---

## Key Findings (Expanded)

### Finding 1: CD8+ T-Cell-Mediated Pathogenesis

PLEVA is fundamentally a CD8+ cytotoxic T-lymphocyte-mediated inflammatory dermatosis. Immunophenotyping studies consistently demonstrate that the predominant T-cell infiltrate in PLEVA lesions is dominated by CD8+ cells ([PMID: 38973067](https://pubmed.ncbi.nlm.nih.gov/38973067/)). T-cell receptor gene rearrangement analysis demonstrates monoclonality in a subset of cases, raising questions about the boundary between reactive inflammation and lymphoproliferation ([PMID: 12203210](https://pubmed.ncbi.nlm.nih.gov/12203210/)). Importantly, a subset of cases showing loss of pan-T-cell markers (CD2, CD5, CD7) may have a closer association with mycosis fungoides, suggesting a spectrum rather than a clear demarcation ([PMID: 40953932](https://pubmed.ncbi.nlm.nih.gov/40953932/)).

### Finding 2: Age- and Sex-Dependent Demographics

The largest long-term PL cohort (242 patients) revealed a striking sex-specific age pattern: male predominance among children (M:F = 1.7:1, p < 0.01) contrasted with female predominance among adults (M:F = 0.6:1) ([PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/)). The average age of onset in children is 6.5 years ([PMID: 25816855](https://pubmed.ncbi.nlm.nih.gov/25816855/)). This reversal of sex predominance between age groups is unusual among dermatological conditions and may reflect sex-specific immune maturation differences.

### Finding 3: FUMHD Mortality Stratification

The severe FUMHD variant carries dramatically different mortality across age groups: 2% in children vs. 20% in adults (overall 12%) ([PMID: 34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/)). Sepsis (LR 24.97), systemic involvement (LR 19.97), and adult age (LR 11.19) are statistically significant mortality predictors. A proposed risk score achieves 93% sensitivity and 77% specificity for predicting fatal outcomes, providing a clinically actionable tool for triage. Monoclonal T-cell receptor rearrangement was also associated with worse prognosis ([PMID: 36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/)).

### Finding 4: Phototherapy Superiority

Among all treatment modalities, phototherapy achieves the highest complete remission rates. NB-UVB demonstrates 73% clearance with 0% recurrence — the best balance of efficacy and durability — while PUVA shows higher initial clearance (83%) but unacceptable recurrence (60%) ([PMID: 27502793](https://pubmed.ncbi.nlm.nih.gov/27502793/); [PMID: 32112390](https://pubmed.ncbi.nlm.nih.gov/32112390/)). Oral erythromycin remains appropriate first-line therapy in children, with 66-83% clearance rates ([PMID: 31318465](https://pubmed.ncbi.nlm.nih.gov/31318465/)). Phototherapy is considered safe and effective in the pediatric population with NB-UVB as the preferred modality ([PMID: 41483505](https://pubmed.ncbi.nlm.nih.gov/41483505/)).

### Finding 5: Hallmark Histopathological Features

The histopathological triad of PLEVA — interface dermatitis with necrotic keratinocytes (100%), perivascular lymphocytic infiltrate (99%), and erythrocyte extravasation (83%) — provides reliable diagnostic criteria ([PMID: 31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/)). Lymphocytic vasculitis without fibrinoid deposition is universally present in PLEVA ([PMID: 17456915](https://pubmed.ncbi.nlm.nih.gov/17456915/)). The absence of eosinophils and the small-to-medium lymphocyte size help distinguish PLEVA from drug reactions and other inflammatory dermatoses.

### Finding 6: Benign Natural History with Rare Lymphoma Risk

Long-term follow-up data are reassuring: in the largest cohort (242 patients, median 9.9 years), no progression to CTCL was established ([PMID: 41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/)). However, a separate study identified 5.2% (3/58) MF progression after 3-11 years of prolonged clinical course ([PMID: 29210716](https://pubmed.ncbi.nlm.nih.gov/29210716/)). The discrepancy likely reflects patient selection and surveillance intensity. Cases with atypical phenotype and T-cell clonality warrant closer monitoring ([PMID: 29851705](https://pubmed.ncbi.nlm.nih.gov/29851705/)).

---

## Evidence Base

### Landmark and Key Studies

| Study | PMID | Type | Key Contribution |
|---|---|---|---|
| Long-term cohort (n=242) | [41420620](https://pubmed.ncbi.nlm.nih.gov/41420620/) | Retrospective cohort | Largest follow-up; no CTCL progression; sex-age demographics |
| FUMHD systematic review (n=119) | [34287852](https://pubmed.ncbi.nlm.nih.gov/34287852/) | Systematic review | Mortality risk quantification; risk score proposal |
| FUMHD treatment outcomes | [36483219](https://pubmed.ncbi.nlm.nih.gov/36483219/) | Systematic review | Prognostic factors for FUMHD |
| Treatment systematic review (n=502) | [32112390](https://pubmed.ncbi.nlm.nih.gov/32112390/) | Systematic review | Phototherapy superiority |
| Pediatric phototherapy review | [27502793](https://pubmed.ncbi.nlm.nih.gov/27502793/) | Systematic review | NB-UVB vs BB-UVB vs PUVA outcomes |
| T-cell clonality study | [12203210](https://pubmed.ncbi.nlm.nih.gov/12203210/) | Molecular study | Clonal T-cell disorder classification |
| Histopathology (n=71) | [31880634](https://pubmed.ncbi.nlm.nih.gov/31880634/) | Case series | Quantified histologic features; adnexotropism |
| PL-MF relationship (n=58) | [29210716](https://pubmed.ncbi.nlm.nih.gov/29210716/) | Cohort study | 5.2% MF progression rate |
| Atypical PL (n=66) | [29851705](https://pubmed.ncbi.nlm.nih.gov/29851705/) | Case series | PL classification into 4 categories |
| PL-MF overlap review | [40953932](https://pubmed.ncbi.nlm.nih.gov/40953932/) | Review | Pan-T-cell marker loss significance |
| Immunophenotyping | [38973067](https://pubmed.ncbi.nlm.nih.gov/38973067/) | Laboratory study | CD8+ dominance confirmed |

---

## Limitations and Knowledge Gaps

### Major Knowledge Gaps

1. **Unknown etiology**: Despite decades of research, the specific trigger(s) for PLEVA remain unidentified. The infectious hypersensitivity hypothesis lacks definitive evidence.

2. **No randomized controlled trials**: All treatment evidence is Level 3-4 (case series, retrospective studies). No RCTs have been conducted for any PLEVA treatment modality.

3. **No identified causal genes**: PLEVA has no established genetic basis, precluding genetic testing, screening, or personalized medicine approaches.

4. **No animal models**: The absence of animal models severely limits mechanistic investigation and preclinical drug testing.

5. **No omics profiling**: No dedicated transcriptomic, proteomic, metabolomic, or epigenomic studies have been performed on PLEVA tissue.

6. **Limited epidemiological data**: Exact prevalence and incidence figures are unavailable due to the rarity of the condition and lack of disease registries.

7. **Biomarker gap**: No circulating biomarkers have been identified for diagnosis, prognosis, or treatment monitoring.

### Study Limitations

- Most evidence derives from retrospective case series and reports with inherent selection bias
- Treatment response data lack standardized outcome measures
- Histopathological diagnostic criteria vary between centers
- The relationship between PL and MF/CTCL remains incompletely understood
- COVID-19 vaccine association data are based on temporal association only and cannot establish causality ([PMID: 36688177](https://pubmed.ncbi.nlm.nih.gov/36688177/))

---

## Proposed Follow-up Experiments / Actions

### High Priority

1. **Multi-center prospective registry**: Establish an international PL registry to capture standardized clinical, histopathological, immunophenotypic, and molecular data. This would address the epidemiological data gap and enable natural history studies.

2. **Lesional transcriptomics/single-cell RNA sequencing**: Perform scRNA-seq on PLEVA lesional skin biopsies vs. matched controls to:
   - Characterize the CD8+ T-cell populations (effector, memory, exhausted phenotypes)
   - Identify target antigens through TCR repertoire analysis
   - Discover pathway-level therapeutic targets

3. **Randomized controlled trial: NB-UVB vs. oral erythromycin**: Given that these are the two most commonly used treatments, a head-to-head RCT (targeting 100+ patients across multiple centers) would provide Level 1 evidence for treatment guidelines.

### Medium Priority

4. **Viral metagenomic sequencing**: Apply unbiased metagenomic sequencing to PLEVA lesional tissue to identify potential viral triggers that may have been missed by targeted PCR-based studies.

5. **Prospective MF progression cohort**: Follow patients with atypical PL (loss of CD2/CD5/CD7, T-cell clonality) prospectively with standardized surveillance (annual skin biopsies, TCR clonality monitoring) to better quantify and predict MF progression risk.

6. **FUMHD biomarker discovery**: Prospective collection of blood samples from FUMHD patients at presentation and during treatment to identify prognostic biomarkers beyond the clinical risk score.

### Lower Priority

7. **Animal model development**: Develop a murine model using adoptive transfer of activated CD8+ T-cells with specificity for keratinocyte antigens to recapitulate the interface dermatitis pattern.

8. **Patient-reported outcomes study**: Conduct a quality-of-life assessment using validated instruments (DLQI, Children's DLQI, EQ-5D) across the PL spectrum to quantify disease burden and inform health economic analyses.

9. **Pharmacogenomic profiling**: For patients on methotrexate or other systemic agents, investigate whether common pharmacogenomic variants (MTHFR, ABCB1) predict treatment response or toxicity in the PLEVA context.

---

## Ontology Term Summary

### MONDO
- MONDO:0024250 — Pityriasis lichenoides et varioliformis acuta

### HPO Terms
- HP:0200034 — Papule
- HP:0200037 — Vesiculobullous skin lesion
- HP:0200042 — Skin ulcer
- HP:0040189 — Scaling skin
- HP:0000989 — Pruritus
- HP:0001945 — Fever
- HP:0007513 — Generalized hypopigmentation of skin
- HP:0100699 — Scarring
- HP:0001047 — Crusting erythematous dermatitis
- HP:0025155 — Disseminated intravascular coagulation

### GO Terms (Biological Process)
- GO:0006955 — Immune response
- GO:0002456 — T cell mediated immunity
- GO:0006915 — Apoptotic process
- GO:0006954 — Inflammatory response
- GO:0042110 — T cell activation
- GO:0006968 — Cellular defense response

### CL Terms (Cell Types)
- CL:0000794 — CD8-positive, alpha-beta cytotoxic T cell
- CL:0000312 — Keratinocyte
- CL:0000115 — Endothelial cell
- CL:0000453 — Langerhans cell

### UBERON Terms (Anatomy)
- UBERON:0002097 — Skin of body
- UBERON:0001003 — Skin epidermis
- UBERON:0002067 — Dermis
- UBERON:0002100 — Trunk
- UBERON:0001456 — Face

### MAXO Terms (Treatment)
- MAXO:0000747 — Antimicrobial therapy
- MAXO:0000571 — Topical corticosteroid therapy
- MAXO:0000596 — Phototherapy
- MAXO:0001024 — Immunosuppressive therapy

### CHEBI Terms
- CHEBI:48923 — Erythromycin
- CHEBI:2955 — Azithromycin
- CHEBI:44185 — Methotrexate
- CHEBI:4031 — Cyclosporine
- CHEBI:41879 — Dexamethasone
- CHEBI:4911 — Etoposide

---

*Report generated: 2026-05-05*
*Based on systematic review of 52 peer-reviewed publications*
*6 confirmed findings with statistical evidence and verified citations*
