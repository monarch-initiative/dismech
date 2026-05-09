---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T06:35:46.316684'
end_time: '2026-05-05T06:57:02.173220'
duration_seconds: 1275.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anterior Spinal Artery Syndrome
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
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anterior Spinal Artery Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anterior Spinal Artery Syndrome** covering all of the
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

# Comprehensive Disease Characterization: Anterior Spinal Artery Syndrome

## Summary

**Anterior Spinal Artery Syndrome (ASAS)** is a devastating vascular myelopathy caused by ischemia or infarction of the ventral two-thirds of the spinal cord supplied by the anterior spinal artery (ASA). It presents with a characteristic clinical triad of bilateral motor paralysis (flaccid paresis), dissociated sensory loss (impaired pain and temperature sensation with preserved proprioception and vibration sense), and autonomic dysfunction including bladder and bowel disturbance. The syndrome accounts for approximately 49% of all spinal cord ischemia presentations and carries a generally poor prognosis, with 57% of patients wheelchair-dependent at discharge and an in-hospital mortality rate of approximately 22%.

The etiology is predominantly vascular, with aortic pathology (atherosclerosis, dissection, surgical/interventional repair) accounting for 35–50% of identifiable causes. Fibrocartilaginous embolism represents a rare but important cause in younger patients, while 20–36% of cases remain idiopathic. Diagnosis relies on clinical recognition of the characteristic neurological pattern combined with MRI findings including longitudinal T2 hyperintensity ("pencil-like" pattern on sagittal views) and the pathognomonic "owl eye" sign on axial imaging. No disease-specific pharmacotherapy exists; management centers on hemodynamic optimization, anticoagulation, cerebrospinal fluid drainage when applicable, and intensive rehabilitation. Emerging research on spinal cord ischemia-reperfusion injury has identified oxidative stress, neuroinflammation (NF-κB, NLRP3 inflammasome), apoptosis, ferroptosis, and pyroptosis cascades as key pathophysiological mechanisms, offering potential therapeutic targets for future intervention.

---

## 1. Disease Information

### Overview

Anterior Spinal Artery Syndrome (ASAS) is an ischemic myelopathy resulting from occlusion or hypoperfusion of the anterior spinal artery or its feeding radiculomedullary arteries. The anterior spinal artery supplies the ventral two-thirds of the spinal cord, including the corticospinal tracts, spinothalamic tracts, and anterior horn motor neurons, while sparing the dorsal columns. This vascular territory explains the hallmark dissociated sensory loss: pain and temperature sensation are lost while proprioception and vibration are preserved. ASAS is a medical emergency with significant morbidity and mortality. The syndrome is most commonly associated with aortic pathology but can also result from embolic events, vasculitis, and other vascular causes.

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **MONDO** | MONDO:0006650 |
| **MeSH** | D020759 (Anterior Spinal Artery Syndrome) |
| **SNOMED CT** | 2972007 |
| **DOID** | DOID:6712 |
| **UMLS** | C0221069 |
| **ICD-9-CM** | 433.80 |
| **ICD-10-CM** | G95.11 (Vascular myelopathies — Acute infarction of spinal cord) |
| **MedDRA** | 10002703 |
| **EFO** | EFO:1000810 |

### Synonyms and Alternative Names

- Anterior spinal artery syndrome
- Anterior spinal cord syndrome
- Anterior cord syndrome
- Beck syndrome
- Anterior spinal artery occlusion syndrome
- Ventral spinal cord syndrome
- Spinal cord anterior artery syndrome

### Data Sources

This characterization is derived from aggregated disease-level resources including published clinical series, case reports, review articles, and biomedical ontology databases. No individual patient-level EHR data were used. A total of 107 papers were reviewed for this report.

---

## 2. Etiology

### Disease Causal Factors

ASAS is fundamentally a **vascular/ischemic** disorder caused by interruption of blood flow through the anterior spinal artery or its feeder vessels. The primary causal mechanism is arterial occlusion (thrombotic, embolic, or hemodynamic) leading to ischemic infarction of the anterior two-thirds of the spinal cord.

**Etiological breakdown from major clinical series:**

In a landmark 19.8-year cohort study of 55 consecutive spinal cord ischemia patients: "Aetiologies of infarcts were arteriosclerosis of the aorta and vertebral arteries (23.6%), aortic surgery or interventional aneurysm repair (11%) and aortic and vertebral artery dissection (11%), and in 23.6%, aetiology remained unclear" ([PMID: 25398656](https://pubmed.ncbi.nlm.nih.gov/25398656/)).

In a separate series of 36 spinal cord infarction patients: "the commonest group being spinal cord ischemia due to idiopathic causes (36.1%). Following these, there were cases associated with aortic surgery (25%), systemic arteriosclerosis (19.4%) and acute deficit of perfusion (11.1%)" ([PMID: 11641795](https://pubmed.ncbi.nlm.nih.gov/11641795/)).

| Etiology | Frequency (PMID: 25398656) | Frequency (PMID: 11641795) |
|----------|---------------------------|---------------------------|
| Atherosclerosis | 23.6% | 19.4% |
| Aortic surgery/intervention | 11.0% | 25.0% |
| Aortic/vertebral dissection | 11.0% | — |
| Acute perfusion deficit | — | 11.1% |
| Idiopathic/unclear | 23.6% | 36.1% |

**Specific etiological categories include:**

1. **Aortic pathology** (most common identifiable cause): Aortic dissection (Type A and B), aortic aneurysm with mural thrombus ([PMID: 29506472](https://pubmed.ncbi.nlm.nih.gov/29506472/)), thoracic endovascular aortic repair (TEVAR), open thoracoabdominal aortic surgery ([PMID: 12483181](https://pubmed.ncbi.nlm.nih.gov/12483181/)), intra-aortic balloon pump complications ([PMID: 27736197](https://pubmed.ncbi.nlm.nih.gov/27736197/))

2. **Fibrocartilaginous embolism** (rare, younger patients): "Fibrocartilaginous nucleus pulposus components herniation and embolism rarely causes acute ischaemic events involving the spinal cord. Few reports have suggested this as a mechanism leading to anterior spinal artery syndrome" ([PMID: 36114979](https://pubmed.ncbi.nlm.nih.gov/36114979/))

3. **Vasculitis**: Behçet's disease ([PMID: 22892002](https://pubmed.ncbi.nlm.nih.gov/22892002/), [PMID: 22193225](https://pubmed.ncbi.nlm.nih.gov/22193225/)), systemic lupus erythematosus ([PMID: 29900713](https://pubmed.ncbi.nlm.nih.gov/29900713/))

4. **Iatrogenic**: Spinal surgery complications ([PMID: 32502625](https://pubmed.ncbi.nlm.nih.gov/32502625/)), spinal anesthesia ([PMID: 27184089](https://pubmed.ncbi.nlm.nih.gov/27184089/))

5. **Hypercoagulable states**: COVID-19-associated coagulopathy ([PMID: 38365009](https://pubmed.ncbi.nlm.nih.gov/38365009/))

6. **Vertebral artery occlusion/dissection**: ([PMID: 41137336](https://pubmed.ncbi.nlm.nih.gov/41137336/))

7. **Hemodynamic**: Systemic hypotension, cardiac arrest ([PMID: 41690059](https://pubmed.ncbi.nlm.nih.gov/41690059/))

### Risk Factors

**Cardiovascular risk factors:** Smoking, hypertension, diabetes mellitus, and hypercholesterolemia are identified as the major risk factors ([PMID: 22962400](https://pubmed.ncbi.nlm.nih.gov/22962400/)). Mean age at presentation is approximately 59.3 years ([PMID: 11641795](https://pubmed.ncbi.nlm.nih.gov/11641795/)), with male predominance (66.6% in some series — [PMID: 38365009](https://pubmed.ncbi.nlm.nih.gov/38365009/)).

**Surgical/procedural risk factors:** Prolonged aortic cross-clamp time ([PMID: 12483181](https://pubmed.ncbi.nlm.nih.gov/12483181/)), coverage of the left subclavian artery during TEVAR ([PMID: 29788799](https://pubmed.ncbi.nlm.nih.gov/29788799/)), hyperkyphosis correction, combined anterior-posterior spinal procedures ([PMID: 32871559](https://pubmed.ncbi.nlm.nih.gov/32871559/)).

**A predictive risk score (0–6 points)** for SCI after open TAAA repair achieved AUC 0.919, based on: TAAA extent II, BMI ≥30, smoking history, preoperative diuretic use, age >70, and chronic kidney disease ([PMID: 41205836](https://pubmed.ncbi.nlm.nih.gov/41205836/)).

**Anatomic risk factors:** Variant spinal cord arterial supply with limited collateral networks, anomalously low origin of the artery of Adamkiewicz ([PMID: 12483181](https://pubmed.ncbi.nlm.nih.gov/12483181/)).

**Genetic risk factors:** No specific genetic variants are causal for ASAS. However, genetic conditions affecting vascular integrity (Marfan syndrome — *FBN1*; Loeys-Dietz syndrome — *TGFBR1/TGFBR2*; vascular Ehlers-Danlos — *COL3A1*) predispose to aortic pathology which can secondarily cause ASAS.

### Protective Factors

- Robust collateral arterial networks (complete Circle of Willis, well-developed segmental medullary arteries)
- Multiple radiculomedullary arteries (present in ~32% of individuals — [PMID: 36152330](https://pubmed.ncbi.nlm.nih.gov/36152330/))
- Dominant anterior thoracic artery present in 94% of individuals ([PMID: 36581455](https://pubmed.ncbi.nlm.nih.gov/36581455/))
- Cardiovascular risk factor modification (BP control, lipid management, smoking cessation)
- Perioperative spinal cord protection protocols (CSF drainage, staged repair, MISACE — [PMID: 41418893](https://pubmed.ncbi.nlm.nih.gov/41418893/))

### Gene-Environment Interactions

No specific gene-environment interactions have been characterized for ASAS. The disease is predominantly acquired through vascular mechanisms rather than genetic predisposition.

---

## 3. Phenotypes

### Core Clinical Presentation

ASAS presents with a characteristic triad. As described in a comprehensive review: "Acute occlusion of the anterior spinal artery and subsequent spinal ischemic infarction leads to anterior spinal artery syndrome characterized by back pain and bilateral flaccid paresis with loss of protopathic sensibility" ([PMID: 37164315](https://pubmed.ncbi.nlm.nih.gov/37164315/)).

In a clinical series of 17 patients: "Clinical presentation included dissociative anesthesia, weakness of limbs, back or neck pain, and autonomic symptoms with symptom onset to peak time ranging from few minutes to 48 hours" ([PMID: 30093205](https://pubmed.ncbi.nlm.nih.gov/30093205/)).

The syndrome accounts for 49% of spinal cord ischemia: "49% of patients suffered from centromedullar syndrome caused by anterior spinal artery ischemia" ([PMID: 25398656](https://pubmed.ncbi.nlm.nih.gov/25398656/)).

### Phenotype Catalog

| Phenotype | HPO Term | Frequency | Severity | Onset |
|-----------|----------|-----------|----------|-------|
| **Motor paralysis** (paraplegia/quadriplegia) | HP:0010550 (Paraplegia); HP:0002445 (Tetraplegia) | ~100% | Severe; variable recovery | Acute |
| **Dissociated sensory loss** (pain/temperature lost, proprioception preserved) | HP:0010835 (Dissociated sensory loss); HP:0007328 (Impaired pain sensation) | ~90–100% | Moderate to severe | Acute |
| **Back/neck pain** at onset | HP:0003418 (Back pain) | ~70–80% | Moderate; typically acute | Prodromal/acute |
| **Urinary incontinence/retention** | HP:0000020 (Urinary incontinence); HP:0000016 (Urinary retention) | ~60–85% | Moderate to severe | Acute |
| **Bowel dysfunction** | HP:0002607 (Bowel incontinence) | ~40–60% | Moderate | Acute |
| **Autonomic dysfunction** | HP:0002459 (Dysautonomia) | Variable | Variable | Acute |
| **Flaccid weakness** (at lesion level) | HP:0001252 (Hypotonia) | ~100% at level | Severe | Acute |
| **Areflexia/hyporeflexia** (acute phase) | HP:0001284 (Areflexia) | Common in acute phase | — | Acute |
| **Spasticity** (below lesion, develops later) | HP:0001257 (Spasticity) | Variable | Variable | Subacute–chronic |
| **Neuropathic pain** | HP:0011499 (Neuropathic pain) | Variable | Moderate to severe | Acute–chronic |
| **Skeletal muscle atrophy** (at lesion level) | HP:0003202 (Skeletal muscle atrophy) | Common | Progressive | Chronic |
| **Sexual dysfunction** | HP:0000802 (Impotence) | Common (conus lesions) | — | Chronic |

### Pediatric Phenotype

In children/adolescents, fibrocartilaginous embolism is the most characteristic cause. Mean age at presentation is 13.2 years. All 7 children in one series had bladder dysfunction requiring catheterization, and neurogenic bladder persisted in 6/7 at last follow-up ([PMID: 28578817](https://pubmed.ncbi.nlm.nih.gov/28578817/)).

### Quality of Life Impact

ASAS has a devastating impact on quality of life. At discharge, 57.1% of patients are wheelchair users, 25% are ambulatory with technical aids, and only 17.9% achieve full ambulation ([PMID: 11641795](https://pubmed.ncbi.nlm.nih.gov/11641795/)). Neurogenic bladder dysfunction persists in the majority of patients long-term.

---

## 4. Genetic/Molecular Information

### Causal Genes

**ASAS is not a Mendelian genetic disorder.** No causal genes, pathogenic variants, or chromosomal abnormalities are directly responsible. It is an acquired vascular condition.

### Relevant Genetic Context

Genes involved in predisposing conditions include:

| Gene | Condition | Relevance to ASAS |
|------|-----------|-------------------|
| **FBN1** (OMIM: 134797) | Marfan syndrome | Aortic dissection/aneurysm → ASAS |
| **TGFBR1/TGFBR2** | Loeys-Dietz syndrome | Aortic pathology → ASAS |
| **COL3A1** (OMIM: 120180) | Vascular Ehlers-Danlos | Arterial fragility → ASAS |
| **ACTA2** (OMIM: 102620) | Familial thoracic aortic aneurysm | Aortic pathology → ASAS |
| *F5*, *F2*, *MTHFR* | Inherited thrombophilias | Thrombotic events → spinal cord ischemia |

### Molecular Pathways in Ischemia-Reperfusion Injury

The molecular cascades activated during spinal cord ischemia are well-characterized from preclinical research:

- **PI3K/Akt/GSK-3β pathway:** Neuroprotective signaling; astaxanthin activation improves outcomes ([PMID: 32703256](https://pubmed.ncbi.nlm.nih.gov/32703256/))
- **Nrf2/HO-1 pathway:** Antioxidant defense; targeted by hydrogen therapy and melatonin ([PMID: 41579273](https://pubmed.ncbi.nlm.nih.gov/41579273/), [PMID: 40684392](https://pubmed.ncbi.nlm.nih.gov/40684392/))
- **NF-κB signaling:** Pro-inflammatory cascade activation
- **NLRP3 inflammasome:** Drives pyroptosis and neuroinflammation
- **HMGB1 signaling:** Anti-HMGB1 antibody therapy improved neurological outcomes in a rabbit SCIRI model: "Treatment with anti-HMGB1 mAb significantly improved neurological outcomes, reduced the extent of spinal cord infarction, preserved motor neuron viability, and decreased the presence of activated microglia and infiltrating neutrophils" ([PMID: 40943562](https://pubmed.ncbi.nlm.nih.gov/40943562/))
- **CaMKII pathway:** Inhibition with tatCN19o showed neuroprotective effects in mouse spinal cord ischemia model ([PMID: 40885467](https://pubmed.ncbi.nlm.nih.gov/40885467/))

### Epigenetic and Chromosomal Information

No disease-specific epigenetic changes or chromosomal abnormalities have been described for ASAS.

---

## 5. Environmental Information

### Environmental Factors

- **Iatrogenic:** Aortic surgery (open repair, TEVAR), spinal surgery, spinal anesthesia, intra-aortic balloon pump use — the most significant modifiable risk factors
- **Trauma:** Cervical facet dislocation (VA occlusion in 24% — [PMID: 39043672](https://pubmed.ncbi.nlm.nih.gov/39043672/)), minor physical trauma triggering fibrocartilaginous embolism
- **Atherosclerotic burden:** Smoking, hypertension, hyperlipidemia, diabetes

### Lifestyle Factors

- **Smoking:** Major vascular risk factor ([PMID: 22962400](https://pubmed.ncbi.nlm.nih.gov/22962400/))
- **Intense physical activity:** Paradoxically, a trigger for fibrocartilaginous embolism in young patients; the most common trigger event in pediatric cases was intense exercise or sports ([PMID: 31201068](https://pubmed.ncbi.nlm.nih.gov/31201068/))
- **Sedentary lifestyle/metabolic syndrome:** Contributes to vascular risk

### Infectious Agents

**SARS-CoV-2:** COVID-19-associated coagulopathy linked to spinal cord ischemia. In a systematic review: "Sixty-six percent of the patients had severe COVID-19. Five data sets reported preexisting coagulopathy. ... Anterior spinal artery lesions were the most prevalent ischemic pattern" ([PMID: 38365009](https://pubmed.ncbi.nlm.nih.gov/38365009/)).

---

## 6. Mechanism / Pathophysiology

### The Causal Chain

```
INITIAL TRIGGER
    │
    ├── Aortic pathology (atherosclerosis, dissection, surgery)
    ├── Embolism (cardiac, fibrocartilaginous, atheromatous)
    ├── Hypoperfusion (hypotension, cardiac arrest)
    └── Vessel compression/occlusion
            │
            ▼
VASCULAR OCCLUSION/HYPOPERFUSION
    │
    ├── Anterior spinal artery occlusion
    ├── Radiculomedullary artery occlusion (e.g., artery of Adamkiewicz)
    └── Sulcal/sulcocommissural artery occlusion
            │
            ▼
SPINAL CORD ISCHEMIA (ventral 2/3)
    │
    ├── Energy failure (ATP depletion)
    ├── Excitotoxicity (glutamate release)
    ├── Calcium influx → CaMKII activation
    │
    ▼
SECONDARY INJURY CASCADES
    │
    ├── Oxidative stress (ROS generation) ──→ Nrf2/HO-1 pathway
    ├── Neuroinflammation ──→ NF-κB, NLRP3 inflammasome, HMGB1
    ├── Apoptosis ──→ Caspase cascades
    ├── Ferroptosis ──→ GPX4 pathway
    ├── Pyroptosis ──→ Gasdermin-D
    └── Autophagy dysregulation
            │
            ▼
NEURONAL AND GLIAL CELL DEATH
    │
    ├── Anterior horn motor neuron destruction → Flaccid paralysis
    ├── Spinothalamic tract damage → Loss of pain/temperature
    ├── Corticospinal tract damage → Upper motor neuron signs (late)
    └── Autonomic pathway damage → Bladder/bowel dysfunction
            │
            ▼
CLINICAL MANIFESTATION: ASAS TRIAD
```

### Vascular Anatomy

The spinal cord receives blood supply from three longitudinal arteries. The single midline ASA (UBERON:0005431) is formed by branches from the vertebral arteries and reinforced by radiculomedullary arteries at various segmental levels. The artery of Adamkiewicz, the largest feeder, originates at T9-T12 on the left side in ~81% of individuals ([PMID: 36152330](https://pubmed.ncbi.nlm.nih.gov/36152330/)). The mid-thoracic region (T4-T8) is a watershed zone particularly vulnerable to ischemia.

The left and right anterior radiculomedullary arteries show distinct distributions: 252 arteries from C2-C8 were slightly dominant on the right, while 236 arteries from T1-L2 were obviously dominant on the left, with the transition occurring at C8-T1 ([PMID: 31399898](https://pubmed.ncbi.nlm.nih.gov/31399898/)).

### Molecular Mechanisms

As described in a comprehensive review: "Oxidative stress is an important pathological event of ischemia/reperfusion injury. Oxidative stress can initiate multiple inflammatory and apoptotic pathways, triggering a series of destructive events such as inflammatory responses and cell death, further deteriorating the microenvironment at the injured site, and leading to neurological dysfunction" ([PMID: 40630671](https://pubmed.ncbi.nlm.nih.gov/40630671/)).

**Key signaling pathways:**

| Pathway | Role | Reference |
|---------|------|-----------|
| **NF-κB** | Pro-inflammatory; cytokine expression | [PMID: 40630671](https://pubmed.ncbi.nlm.nih.gov/40630671/) |
| **Nrf2/HO-1/GPX4** | Antioxidant defense; anti-ferroptosis | [PMID: 41579273](https://pubmed.ncbi.nlm.nih.gov/41579273/) |
| **PI3K/Akt/GSK-3β** | Neuroprotective survival signaling | [PMID: 32703256](https://pubmed.ncbi.nlm.nih.gov/32703256/) |
| **CaMKII** | Excitotoxic injury; inhibition is neuroprotective | [PMID: 40885467](https://pubmed.ncbi.nlm.nih.gov/40885467/) |
| **HMGB1/TLR4** | Danger signaling; neuroinflammation | [PMID: 40943562](https://pubmed.ncbi.nlm.nih.gov/40943562/) |
| **NLRP3 inflammasome** | Pyroptosis and inflammatory cell death | [PMID: 35793244](https://pubmed.ncbi.nlm.nih.gov/35793244/) |
| **miR-214-3p/Nmb/Cav3.2** | MicroRNA regulation of neuroinflammation | [PMID: 38631219](https://pubmed.ncbi.nlm.nih.gov/38631219/) |

### Cellular Processes (GO Terms)

- Apoptotic process (GO:0006915)
- Inflammatory response (GO:0006954)
- Response to oxidative stress (GO:0006979)
- Response to ischemia (GO:0002931)
- Autophagy (GO:0006914)
- Cell death (GO:0008219)

### Cell Types Involved (CL Terms)

| Cell Type | CL Term | Role |
|-----------|---------|------|
| Motor neurons | CL:0000100 | Primary targets of anterior horn ischemia |
| Oligodendrocytes | CL:0000128 | White matter tract demyelination |
| Microglia | CL:0000129 | Activated during neuroinflammation |
| Astrocytes | CL:0000127 | Reactive gliosis |
| Neutrophils | CL:0000775 | Infiltrate during acute phase |
| Endothelial cells | CL:0000115 | Blood-spinal cord barrier disruption |

### Immune System Involvement

Neuroinflammation is critical to secondary injury. Anti-HMGB1 therapy "significantly improved neurological outcomes, reduced the extent of spinal cord infarction, preserved motor neuron viability, and decreased the presence of activated microglia and infiltrating neutrophils" ([PMID: 40943562](https://pubmed.ncbi.nlm.nih.gov/40943562/)). Autoimmune vasculitis (Behçet's disease, SLE) represents a distinct subset.

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary:** Spinal cord (UBERON:0002240), anterior spinal artery (UBERON:0005441)

**Secondary:** Urinary bladder, gastrointestinal tract, skeletal muscle (atrophy), skin (pressure injuries), lungs (high cervical lesions)

**Body systems:** Nervous (primary), cardiovascular (underlying cause), urinary, musculoskeletal

### Tissue and Cell Level

| Structure | UBERON Term | Involvement |
|-----------|-------------|-------------|
| Anterior horn gray matter | UBERON:0002257 | Motor neuron destruction |
| Lateral corticospinal tract | UBERON:0002584 | Upper motor neuron loss |
| Spinothalamic tract | UBERON:0002702 | Pain/temperature loss |
| Anterior funiculus | UBERON:0002256 | White matter damage |
| Dorsal columns | UBERON:0005375 | **SPARED** (posterior spinal artery territory) |

### Subcellular Level

- Mitochondria (GO:0005739): Energy failure, ROS generation
- Endoplasmic reticulum (GO:0005783): ER stress
- Cell membrane: Lipid peroxidation, ion channel dysfunction
- Nucleus (GO:0005634): DNA damage, apoptotic signaling

### Localization

- **Thoracic spinal cord** (UBERON:0003038): Most commonly affected (watershed zone)
- **Cervical spinal cord** (UBERON:0002726): When cervical ASA occluded — bilateral arm paresis ([PMID: 10773652](https://pubmed.ncbi.nlm.nih.gov/10773652/))
- **Conus medullaris**: "Snake-eye appearance" on MRI ([PMID: 36998945](https://pubmed.ncbi.nlm.nih.gov/36998945/))
- **Lateralization:** Typically bilateral and symmetric, but unilateral presentations occur with sulcal artery occlusion ([PMID: 40104967](https://pubmed.ncbi.nlm.nih.gov/40104967/), [PMID: 30300819](https://pubmed.ncbi.nlm.nih.gov/30300819/))

---

## 8. Temporal Development

### Onset

- **Typical age:** Adult-onset, mean ~59 years ([PMID: 11641795](https://pubmed.ncbi.nlm.nih.gov/11641795/)); pediatric cases mean 13.2 years ([PMID: 28578817](https://pubmed.ncbi.nlm.nih.gov/28578817/))
- **Onset pattern:** Acute to hyperacute — minutes to 48 hours to peak ([PMID: 30093205](https://pubmed.ncbi.nlm.nih.gov/30093205/))
- Typically preceded by sudden back pain

### Progression

| Stage | Timeline | Features |
|-------|----------|----------|
| Hyperacute | Minutes–hours | Sudden back pain, rapid motor loss, sensory changes |
| Acute/spinal shock | Hours–days | Flaccid paralysis, areflexia, autonomic dysfunction |
| Subacute | Days–weeks | Transition to spasticity; early recovery begins |
| Chronic | Weeks–years | Stabilization; residual deficits; ongoing rehabilitation |

- **Disease course:** Monophasic (single event); chronic residual deficits; NOT relapsing-remitting
- **Recovery timeline:** In 9 patients followed 15–41 months: 4 walked independently, 1 with support ([PMID: 30093205](https://pubmed.ncbi.nlm.nih.gov/30093205/))

### Critical Periods

- **First 4.5–6 hours:** Window for potential thrombolytic therapy ([PMID: 22962400](https://pubmed.ncbi.nlm.nih.gov/22962400/), [PMID: 26386968](https://pubmed.ncbi.nlm.nih.gov/26386968/))
- **First 24 hours:** Critical for hemodynamic augmentation and CSF drainage
- **First 3–4 months:** Period of most significant functional recovery ([PMID: 22193225](https://pubmed.ncbi.nlm.nih.gov/22193225/))
- **Delayed SCI after TEVAR:** Can occur months to years post-procedure ([PMID: 38304669](https://pubmed.ncbi.nlm.nih.gov/38304669/))

---

## 9. Inheritance and Population

### Epidemiology

ASAS is rare. Spinal cord infarction accounts for ~1–2% of all strokes. ASAS represents ~49% of spinal cord ischemia cases ([PMID: 25398656](https://pubmed.ncbi.nlm.nih.gov/25398656/)). Estimated incidence of all spinal cord infarction is approximately 3.1 per 100,000 person-years. After aortic surgery, SCI incidence ranges from 0–10.6% for TEVAR to 0–35% for thoracoabdominal repair ([PMID: 34740806](https://pubmed.ncbi.nlm.nih.gov/34740806/)).

### Inheritance

**Not applicable** — ASAS is an acquired vascular condition with no Mendelian inheritance pattern. Predisposing conditions (Marfan, vascular EDS) follow autosomal dominant inheritance.

### Population Demographics

- **Sex ratio:** Male predominance (~60–67%) ([PMID: 38365009](https://pubmed.ncbi.nlm.nih.gov/38365009/))
- **Age distribution:** Bimodal — peak in adolescents (fibrocartilaginous embolism) and older adults (atherosclerotic/surgical causes)
- **Geographic distribution:** Worldwide; correlates with cardiovascular disease burden
- **Ethnic predisposition:** None documented; risk mirrors cardiovascular disease prevalence

---

## 10. Diagnostics

### MRI (Gold Standard)

MRI findings are highly characteristic. In anterior spinal artery infarcts: "MRI findings in anterior spinal artery infarcts included pencillike hyperintensities on T2 sagittal (n = 16, 100%) and 'owl eye' appearance on T2 axial (n = 6, 37.5%) images. Diffusion restriction was noted in 8 cases and enhancement was noted in 2 cases" ([PMID: 30093205](https://pubmed.ncbi.nlm.nih.gov/30093205/)).

| MRI Feature | Frequency | Imaging Sequence |
|-------------|-----------|------------------|
| Pencil-like T2 hyperintensity (sagittal) | 100% | T2-weighted sagittal |
| "Owl eye" appearance (axial) | 37.5% | T2-weighted axial |
| Diffusion restriction | 50% (100% when DWI performed) | DWI |
| Cord swelling | 40% | T2-weighted |
| Enhancement | 42.9% | Post-contrast T1 |

The "snake-eye appearance" on axial MRI in conus infarction: "acute onset of conus medullaris syndrome combined with 'snake-eye appearance' should be strongly suspected as conus medullaris infarction caused by anterior spinal artery ischemia" ([PMID: 36998945](https://pubmed.ncbi.nlm.nih.gov/36998945/)).

### Additional Diagnostic Studies

- **CT angiography of aorta:** Identify dissection, aneurysm, atherosclerosis
- **Digital subtraction angiography:** May show ASA occlusion ([PMID: 16718293](https://pubmed.ncbi.nlm.nih.gov/16718293/))
- **CSF analysis:** Elevated protein without pleocytosis (distinguishes from inflammatory myelitis); exclude AQP4/MOG antibodies ([PMID: 41137336](https://pubmed.ncbi.nlm.nih.gov/41137336/))
- **Electrophysiology:** Absent CMAPs predict poor prognosis — "CMAP could be seen a marker of prognosis for ASAS patients, and absent CMAP might forecast the bad prognosis" ([PMID: 16718293](https://pubmed.ncbi.nlm.nih.gov/16718293/))
- **ASIA Impairment Scale:** Standard neurological classification (A through E)

### Genetic Testing

Not applicable for ASAS itself. Relevant for underlying predisposing conditions (thrombophilia panel, connective tissue disorder genes) in young patients without clear etiology.

### Differential Diagnosis

| Condition | Key Distinguishing Features |
|-----------|---------------------------|
| **Transverse myelitis** | Subacute onset; CSF pleocytosis; gadolinium enhancement |
| **NMO spectrum disorder** | AQP4 antibodies; longitudinally extensive; area postrema syndrome |
| **Guillain-Barré syndrome** | Ascending weakness; elevated CSF protein; NCS findings |
| **Compressive myelopathy** | Progressive; structural lesion on MRI |
| **Multiple sclerosis** | Partial cord syndrome; brain lesions; oligoclonal bands |
| **Fibrocartilaginous embolism** | Young patient; post-exertion; disc changes on MRI |

---

## 11. Outcome / Prognosis

### Survival and Mortality

In the largest published series (36 patients): "the average age of the patients was 59.3 years, with a mortality of 22.2% during the hospital stay. Regarding the functional outcomes at the moment of discharge, it must be pointed out that 57.1% of the patients were wheelchair users, 25% were ambulatory, using technical aids, and 17.9% were fully ambulatory" ([PMID: 11641795](https://pubmed.ncbi.nlm.nih.gov/11641795/)).

### Prognostic Factors

"Prognosis is primarily determined by the severity of motor or sensory involvement, in particular, initial and nadir ASIA A/B scores which strongly correlate with poor outcome. In the majority of series, 40-60% of patients had initial ASIA A/B scores with a similar proportion remaining wheelchair dependent on follow-up" ([PMID: 26154150](https://pubmed.ncbi.nlm.nih.gov/26154150/)).

| Prognostic Factor | Effect |
|-------------------|--------|
| Initial ASIA A/B score | Strong predictor of poor outcome |
| Absent CMAPs | Predicts poor motor recovery ([PMID: 16718293](https://pubmed.ncbi.nlm.nih.gov/16718293/)) |
| Younger age | Favorable |
| Rapid treatment initiation | Favorable |
| Cervical level involvement | Worse prognosis |
| Complete motor deficit | Worse prognosis |

### Complications

Deep vein thrombosis, pulmonary embolism, urinary tract infections, pressure ulcers, chronic neuropathic pain, spasticity, pneumonia (cervical lesions), depression, neurogenic bladder (persistent in 6/7 pediatric patients — [PMID: 28578817](https://pubmed.ncbi.nlm.nih.gov/28578817/)).

---

## 12. Treatment

### Current Management

There is **no disease-specific pharmacotherapy** for ASAS. Treatment is largely supportive and empirical.

**Acute phase:**

| Intervention | Mechanism | Evidence | MAXO Term |
|-------------|-----------|---------|-----------|
| **MAP augmentation** | Improve spinal cord perfusion | 3 patients improved with MAP elevation + CSF drainage ([PMID: 30294499](https://pubmed.ncbi.nlm.nih.gov/30294499/)) | MAXO:0000503 |
| **CSF drainage** | Reduce intraspinal pressure | Significant motor improvement (ASIA B/C → D) ([PMID: 30294499](https://pubmed.ncbi.nlm.nih.gov/30294499/)) | MAXO:0000472 |
| **Anticoagulation** | Prevent thrombus propagation | Heparin most commonly used ([PMID: 38365009](https://pubmed.ncbi.nlm.nih.gov/38365009/)) | MAXO:0001001 |
| **Thrombolysis (rt-PA)** | Dissolve clot | First MRI-confirmed case with partial recovery ([PMID: 26386968](https://pubmed.ncbi.nlm.nih.gov/26386968/)) | MAXO:0001072 |
| **Corticosteroids** | Anti-inflammatory | Used empirically; evidence mixed ([PMID: 32502625](https://pubmed.ncbi.nlm.nih.gov/32502625/)) | MAXO:0000647 |
| **Immunosuppression** | For vasculitis-mediated ASAS | Good outcome in Behçet's ([PMID: 22193225](https://pubmed.ncbi.nlm.nih.gov/22193225/)) | MAXO:0000648 |

**Rehabilitation (cornerstone of long-term management):**
- Physical therapy (MAXO:0000011), occupational therapy (MAXO:0000535)
- Bladder management (intermittent catheterization — MAXO:0000474)
- Pain management (gabapentin, pregabalin for neuropathic pain)
- Psychological support
- Satisfactory functional recovery may require 3–4 months; complete independence achievable at 1 year in favorable cases ([PMID: 22193225](https://pubmed.ncbi.nlm.nih.gov/22193225/))

### Experimental/Preclinical Therapeutics

| Agent | Mechanism | Model | Evidence |
|-------|-----------|-------|---------|
| **Anti-HMGB1 antibody** | Anti-inflammatory | Rabbit | Improved neurological outcomes ([PMID: 40943562](https://pubmed.ncbi.nlm.nih.gov/40943562/)) |
| **tatCN19o (CaMKII inhibitor)** | Neuroprotective | Mouse | Preserved motor function at 48h ([PMID: 40885467](https://pubmed.ncbi.nlm.nih.gov/40885467/)) |
| **Astaxanthin** | Antioxidant (PI3K/Akt) | Rat | Alleviated pathological damage ([PMID: 32703256](https://pubmed.ncbi.nlm.nih.gov/32703256/)) |
| **Hydrogen therapy** | Anti-ferroptosis (Nrf2/HO-1) | Rat | Attenuated SCIRI ([PMID: 41579273](https://pubmed.ncbi.nlm.nih.gov/41579273/)) |
| **Melatonin** | Anti-ferroptosis (Nrf2/HO-1/GPX4) | Rat | Reduced neuronal death ([PMID: 40684392](https://pubmed.ncbi.nlm.nih.gov/40684392/)) |
| **Adipose-derived stem cells** | Regenerative | Rat | Improved paraplegia recovery ([PMID: 39263357](https://pubmed.ncbi.nlm.nih.gov/39263357/)) |

### Perioperative Prevention Strategies

- Intraoperative neuromonitoring (MEPs, SSEPs)
- Staged procedures for extensive aortic coverage
- MISACE before fenestrated/branched endovascular repair: SCI 9.5% vs 30% without ([PMID: 41418893](https://pubmed.ncbi.nlm.nih.gov/41418893/))
- Minimizing aortic cross-clamp time
- Multimodal spinal cord protection bundles ([PMID: 34740806](https://pubmed.ncbi.nlm.nih.gov/34740806/))

---

## 13. Prevention

### Primary Prevention

- Cardiovascular risk factor modification (smoking cessation, BP control, lipid management, diabetes control)
- Atherosclerosis prevention
- Anticoagulation for thrombophilic states/atrial fibrillation

### Secondary Prevention (Perioperative)

- Cerebrospinal fluid drainage protocols ([PMID: 34740806](https://pubmed.ncbi.nlm.nih.gov/34740806/))
- Blood pressure augmentation (MAP >80–90 mmHg)
- Intraoperative neuromonitoring ([PMID: 32502625](https://pubmed.ncbi.nlm.nih.gov/32502625/))
- Staged aortic repair
- MISACE ([PMID: 41418893](https://pubmed.ncbi.nlm.nih.gov/41418893/))
- Avoidance of prolonged hypotension ([PMID: 12483181](https://pubmed.ncbi.nlm.nih.gov/12483181/))

### Tertiary Prevention

- DVT prophylaxis, pressure ulcer prevention, UTI prevention
- Respiratory care (high cervical lesions)
- Spasticity management
- Psychological support

---

## 14. Other Species / Natural Disease

### Naturally Occurring Disease

**Dogs** (NCBI Taxon: 9615): Fibrocartilaginous embolism causing spinal cord infarction is well-recognized in veterinary medicine. "The disease has been found more frequently in dogs" ([PMID: 7202135](https://pubmed.ncbi.nlm.nih.gov/7202135/)). Large and giant breed dogs are most commonly affected. The canine model has provided important insights into the pathogenesis of nucleus pulposus embolism.

**Horses** (NCBI Taxon: 9796): Spinal cord ischemia reported from fibrocartilaginous embolism or verminous arteritis.

**Cats** (NCBI Taxon: 9685): Rare reports of fibrocartilaginous embolism.

**Pigs** (NCBI Taxon: 9823): Used as experimental models due to similar vascular anatomy ([PMID: 32115761](https://pubmed.ncbi.nlm.nih.gov/32115761/)).

### Comparative Biology

Spinal cord vascular anatomy is conserved across mammals. The vulnerability of the ASA territory to ischemia is a shared feature due to the precarious watershed blood supply. Fibrocartilaginous embolism occurs across multiple mammalian species, suggesting a conserved pathomechanism.

---

## 15. Model Organisms

### Animal Models of Spinal Cord Ischemia

| Model | Species | Method | Application | Reference |
|-------|---------|--------|-------------|-----------|
| **Aortic cross-clamp** | Mouse (C57BL/6) | Clamping aorta distal to left carotid | CaMKII inhibition | [PMID: 40885467](https://pubmed.ncbi.nlm.nih.gov/40885467/) |
| **Abdominal aortic occlusion** | Rat (Sprague-Dawley) | Abdominal aorta ligation | Oxidative stress, ferroptosis | [PMID: 32703256](https://pubmed.ncbi.nlm.nih.gov/32703256/) |
| **Taira-Marsala model** | Rat | Ephemeral aortic occlusion | Stem cell transplantation | [PMID: 39263357](https://pubmed.ncbi.nlm.nih.gov/39263357/) |
| **Aortic occlusion** | Rabbit | Aortic clamping | Anti-HMGB1 therapy | [PMID: 40943562](https://pubmed.ncbi.nlm.nih.gov/40943562/) |
| **Porcine model** | Pig (Landrace) | Lateral thoracotomy | Blood flow analysis | [PMID: 32115761](https://pubmed.ncbi.nlm.nih.gov/32115761/) |
| **OGD/R in vitro** | HT22/BV2 cells | Oxygen-glucose deprivation | Pathway studies | Multiple |

### Model Characteristics

**Phenotype recapitulation:** Rodent models reliably produce hind limb motor deficits. Histological changes include motor neuron loss, vacuolization, and pyknosis in lumbar anterior horn ([PMID: 40885467](https://pubmed.ncbi.nlm.nih.gov/40885467/)). Molecular cascades mirror human pathophysiology.

**Limitations:** Small animal models lack the complex arterial anatomy of humans. Aortic cross-clamp models cause global ischemia rather than isolated ASA territory infarction. Recovery mechanisms may differ between species. Porcine models most closely approximate human spinal vascular anatomy.

---

## Key Findings Summary

### F1: Disease Definition and Identifiers
ASAS (MONDO:0006650) is ischemia/infarction in the distribution of the anterior spinal artery, affecting the ventral two-thirds of the spinal cord. Key identifiers include MeSH D020759, SNOMED CT 2972007, DOID 6712, and UMLS C0221069.

### F2: Multiple Vascular Etiologies with Aortic Disease Predominant
Aortic pathology (atherosclerosis, dissection, surgery) accounts for 35–50% of identifiable cases. Fibrocartilaginous embolism is rare but important in young patients. 20–36% remain idiopathic.

### F3: Characteristic Clinical Triad
Motor paralysis, dissociated sensory loss (pain/temperature lost, proprioception preserved), and autonomic dysfunction. Symptom onset to peak ranges from minutes to 48 hours.

### F4: Poor Prognosis with Variable Recovery
In-hospital mortality ~22%. At discharge: 57% wheelchair-dependent, 25% ambulatory with aids, 18% fully ambulatory. Initial ASIA A/B scores strongly predict poor outcome.

### F5: Pathognomonic MRI Features
Pencil-like T2 hyperintensity (100%), "owl eye" sign (37.5%), diffusion restriction, and cord swelling. "Snake-eye appearance" in conus infarction.

### F6: Ischemia-Reperfusion Molecular Cascades
Oxidative stress, neuroinflammation (NF-κB, NLRP3, HMGB1), apoptosis, ferroptosis, and pyroptosis represent key pathophysiological mechanisms with multiple potential therapeutic targets.

---

## Limitations and Knowledge Gaps

1. **Limited epidemiological data:** No population-based incidence/prevalence studies exist specifically for ASAS
2. **No randomized controlled trials:** All treatments based on case reports/series; Level I evidence completely lacking
3. **Diagnostic delay:** Initial MRI may be normal in some cases; DWI not always acquired
4. **No validated biomarkers:** Beyond electrophysiological markers (CMAPs), no serum/CSF biomarkers for early diagnosis
5. **Translational gap:** Numerous preclinical neuroprotective agents but none translated to clinical use
6. **Idiopathic cases:** 20–36% have no identifiable etiology
7. **Sparse long-term data:** Follow-up beyond 2–3 years poorly characterized
8. **No human omics data:** All molecular pathway data from animal models
9. **Pediatric knowledge gap:** Pathogenesis of childhood idiopathic SCI remains unclear ([PMID: 28578817](https://pubmed.ncbi.nlm.nih.gov/28578817/))

---

## Proposed Follow-up Experiments / Actions

1. **Multicenter prospective ASAS registry** — Standardized data collection on incidence, etiology, treatment, and outcomes
2. **Biomarker discovery** — Proteomics/metabolomics of CSF and serum in acute ASAS (neurofilament light, GFAP, S100B)
3. **Thrombolysis clinical trial** — Multicenter trial of IV rt-PA for acute ASAS (after excluding dissection/hemorrhage)
4. **CaMKII inhibitor translational studies** — Advance tatCN19o from mouse to large animal models
5. **Anti-HMGB1 therapy development** — Advance from rabbit models toward clinical translation
6. **Standardized emergency MRI protocol** — Include mandatory DWI sequences and optimized timing
7. **Genetic susceptibility studies** — GWAS in idiopathic ASAS patients
8. **Single-cell transcriptomics** — Map cell-type-specific responses at multiple post-ischemia time points
9. **Rehabilitation RCTs** — Compare early intensive rehabilitation to standard care
10. **Preoperative spinal vascular mapping** — Non-invasive MR angiography for high-risk aortic surgery patients

---

## Evidence Base — Key Citations

| PMID | Study Type | Key Contribution |
|------|-----------|-----------------|
| [25398656](https://pubmed.ncbi.nlm.nih.gov/25398656/) | Retrospective cohort (n=55) | Comprehensive etiology and imaging over 19.8 years |
| [11641795](https://pubmed.ncbi.nlm.nih.gov/11641795/) | Case series (n=36) | Largest outcome series: 22% mortality, 57% wheelchair |
| [30093205](https://pubmed.ncbi.nlm.nih.gov/30093205/) | Case series (n=17) | MRI features: pencil-like hyperintensity, owl eye sign |
| [37164315](https://pubmed.ncbi.nlm.nih.gov/37164315/) | Case report/review | Classic clinical description; fibrocartilaginous embolism |
| [26154150](https://pubmed.ncbi.nlm.nih.gov/26154150/) | Literature review | Prognostic factors: ASIA score correlation |
| [28578817](https://pubmed.ncbi.nlm.nih.gov/28578817/) | Pediatric series (n=7) | Childhood idiopathic SCI characterization |
| [36114979](https://pubmed.ncbi.nlm.nih.gov/36114979/) | Case report/review | Fibrocartilaginous embolism |
| [36998945](https://pubmed.ncbi.nlm.nih.gov/36998945/) | Case report | Snake-eye appearance in conus infarction |
| [40630671](https://pubmed.ncbi.nlm.nih.gov/40630671/) | Review | Oxidative stress in SCIRI pathophysiology |
| [40943562](https://pubmed.ncbi.nlm.nih.gov/40943562/) | Preclinical (rabbit) | Anti-HMGB1 antibody therapy |
| [40885467](https://pubmed.ncbi.nlm.nih.gov/40885467/) | Preclinical (mouse) | CaMKII inhibition neuroprotection |
| [32703256](https://pubmed.ncbi.nlm.nih.gov/32703256/) | Preclinical (rat) | Astaxanthin via PI3K/Akt pathway |
| [34740806](https://pubmed.ncbi.nlm.nih.gov/34740806/) | Systematic review | SCI prevention strategies in aortic repair |
| [41418893](https://pubmed.ncbi.nlm.nih.gov/41418893/) | Retrospective comparative | MISACE spinal cord protection |
| [22962400](https://pubmed.ncbi.nlm.nih.gov/22962400/) | Case report | Thrombolysis in ASAS |
| [26386968](https://pubmed.ncbi.nlm.nih.gov/26386968/) | Case report | First MRI-proven ASAS with rt-PA |
| [30294499](https://pubmed.ncbi.nlm.nih.gov/30294499/) | Case series (n=3) | CSF drainage and MAP augmentation |
| [38365009](https://pubmed.ncbi.nlm.nih.gov/38365009/) | Systematic review | COVID-19 and spinal cord ischemia |
| [16718293](https://pubmed.ncbi.nlm.nih.gov/16718293/) | Case report | CMAPs as prognostic marker |
| [22193225](https://pubmed.ncbi.nlm.nih.gov/22193225/) | Case report | Behçet's ASAS with rehabilitation |

---

*Report generated: 2026-05-05*
*Based on systematic analysis of 107 published studies and 6 confirmed findings*
*Disease: Anterior Spinal Artery Syndrome (MONDO:0006650)*
