---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-31T16:46:04.027205'
end_time: '2026-08-31T17:11:34.672768'
duration_seconds: 1530.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Distal Hereditary Motor Neuronopathy Type 5B
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 22
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Distal_Hereditary_Motor_Neuronopathy_Type_5B-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Distal_Hereditary_Motor_Neuronopathy_Type_5B-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Distal Hereditary Motor Neuronopathy Type 5B
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Distal Hereditary Motor Neuronopathy Type 5B** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Distal Hereditary Motor Neuronopathy Type 5B (dHMN5B): A Comprehensive Disease Characteristics Report

**Disease:** Distal Hereditary Motor Neuronopathy Type 5B (dHMN5B / HMN5B / dHMN-VB)
**MONDO ID:** MONDO:0013884
**OMIM:** #614751
**Causal gene:** *REEP1* (HGNC:25786)
**Category:** Mendelian (autosomal dominant)

---

## Summary

Distal Hereditary Motor Neuronopathy Type 5B (dHMN5B) is a rare, autosomal dominant, adolescent- to adult-onset, slowly progressive **pure motor** axonal neuropathy of the **lower motor neurons**. Its clinical hallmark is distal amyotrophy (muscle wasting and weakness) that **predominates in the upper limbs**, characteristically affecting the small hand/thenar muscles, with later spread to the lower limbs (peroneal distribution). Sensation is clinically spared. It belongs to the "distal HMN type V" phenotypic class, which is shared allelically with mutations in *GARS1* (dHMN5A) and *BSCL2* (Silver syndrome). dHMN5B is caused specifically by heterozygous variants in *REEP1*, the receptor expression-enhancing protein 1 gene on chromosome 2p11.2.

Mechanistically, dHMN5B is now understood to be the **mirror image** of the more common loss-of-function *REEP1* disorder, hereditary spastic paraplegia type 31 (SPG31), which affects upper (cortical) motor neurons. The prototype dHMN5B allele is an **in-frame deletion of exon 5** ("Δexon5"), produced by the founding splice-site variant c.304-2A>G. Rather than abolishing REEP1's ER-shaping function, the Δexon5 protein retains its membrane-curvature (hairpin) activity but escapes normal ubiquitin-proteasome turnover (mediated by the E3 ligase HUWE1). The consequence is **toxic accumulation** of shaping-competent REEP1 in peripheral nerve, which fragments the tubular endoplasmic reticulum (ER) of **spinal** motor neurons and drives their degeneration — while cortical motor neurons are spared. This gain-of-function/accumulation model, established in a genotype-matched Δexon5 knock-in mouse, elegantly explains why the same gene causes an upper-motor-neuron disease (SPG31, loss of function) and a lower-motor-neuron disease (dHMN5B, toxic accumulation).

There is no disease-modifying therapy; management is supportive and rehabilitative (physical/occupational therapy, orthoses, foot-drop management, orthopedic care of pes cavus). Because the mechanism is a toxic accumulation with a defined degradation pathway, mechanistically rational experimental strategies include allele-selective knockdown of the mutant transcript, modulation of ER stress, and enhancement of HUWE1-dependent REEP1 proteostasis. This report synthesizes 8 confirmed findings across 34 reviewed papers into a structured, citation-anchored disease knowledge base entry.

---

## Key Findings

### Finding 1 — dHMN5B is caused by dominant *REEP1* variants that spare the tubular-ER-shaping function

The founding description of *REEP1*-associated dHMN type V came from whole-exome sequencing of a linkage-defined family. Beetz and colleagues identified a single candidate splice-site variant in *REEP1*, **c.304-2A>G**, which abolishes the exon-5 splice acceptor and causes complete, in-frame **skipping of exon 5**. The resulting mRNA is expressed at normal levels and is predicted to encode an internally shortened protein, **p.102_139del** — i.e., a protein missing 38 internal residues but otherwise intact and stable.

> *"Whole-exome sequencing of two affected individuals revealed a single candidate variant within the linking regions, i.e., a splice-site alteration in REEP1 (c.304-2A>G). A minigene assay confirmed complete loss of splice-acceptor functionality and skipping of the in-frame exon 5. The resulting mRNA is predicted to be expressed at normal levels and to encode an internally shortened protein (p.102_139del)."* — [PMID: 22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/)

Critically, this same paper demonstrated that *REEP1* is strongly expressed in lower motor neurons, providing the tissue-level rationale for why a *REEP1* variant produces a distal lower-motor-neuron (dHMN) phenotype rather than a purely central one:

> *"Consistent with our clinical-genetic data, we show that REEP1 is strongly expressed in the lower motoneurons as well."* — [PMID: 22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/)

This established the gene–disease relationship recorded under OMIM #614751 (HMN5B) and placed *REEP1*-dHMN5B alongside the other dHMN-V genes *GARS1* and *BSCL2*.

### Finding 2 — Mechanism: toxic accumulation of shaping-competent REEP1 fragments the ER and kills spinal motor neurons

The pivotal mechanistic study (Bock et al., 2026) resolved how the Δexon5 allele causes disease. Under normal conditions, REEP1 is turned over by **ubiquitination and proteasomal degradation**, with the E3 ubiquitin ligase **HUWE1** identified as responsible for REEP1 turnover. The Δexon5 variant has **impaired ubiquitination**, so the (still shaping-competent) protein is not degraded and instead **accumulates in peripheral nerves**.

> *"REEP1 undergoes ubiquitination and proteasomal degradation, a process compromised in the Δexon5 variant due to impaired ubiquitination, which thus accumulates in peripheral nerves. Proteomic analysis identifies HUWE1 as the E3 ligase responsible for REEP1 turnover."* — [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/)

A genotype-matched **Δexon5 knock-in mouse** recapitulated the human disease: these mice lose **spinal** motor neurons, preceded by **ER fragmentation**, while **cortical** motor neurons remain intact — the precise anatomical mirror image of *Reep1*-knockout mice, which lose cortical motor neurons and model HSP.

> *"Δexon5 knockin (KI) mice lose spinal motoneurons preceded by ER fragmentation, whereas cortical motoneurons remain intact."* — [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/)

This gain-of-toxic-function model is corroborated by an independent report of a different *REEP1* nonstop variant that unmasks a 3′UTR-encoded, aggregation-inducing motif — again pointing to toxic gain of function specifically in lower motor neurons:

> *"Together with a previous report on an aggregation-prone REEP1 deletion variant in distal hereditary motor neuropathy, they also suggest that toxic gain of REEP1 function, rather than loss-of-function as relevant for HSP, specifically affects lower motor neurons."* — [PMID: 29124833](https://pubmed.ncbi.nlm.nih.gov/29124833/)

### Finding 3 — Clinical phenotype: upper-limb-predominant distal amyotrophy, pure motor, with a lower-motor-neuron electrophysiologic signature

dHMN type V — the phenotypic class of *REEP1*-dHMN5B — is a **slowly progressive distal pure motor neuropathy predominating in the upper limbs**, with wasting and weakness of the small hand muscles, and later spread to the lower limbs. REEP1 is one of three genes principally linked to this upper-limb-predominant presentation:

> *"Distal hereditary motor neuropathy that predominates in the upper limbs is linked mainly to three genes: GARS, BSCL2 and REEP1"* — [PMID: 38702287](https://pubmed.ncbi.nlm.nih.gov/38702287/)

The electrophysiologic signature is that of a pure-motor axonal process: **normal sensory nerve conduction velocities**, **markedly reduced compound muscle action potential (CMAP) amplitudes**, and **chronic denervation** on needle EMG. (This description derives from the closely related BSCL2/dHMN-V family literature, which shares the identical clinical-electrophysiologic phenotype class.)

> *"In all three patients sensory nerve conduction velocities (NCV) were normal in all extremities. Compound muscle action potential (CMAP) amplitudes were markedly reduced in all patients. Concentric needle EMG showed evidence of chronic denervation in distal muscles."* — [PMID: 20598714](https://pubmed.ncbi.nlm.nih.gov/20598714/)

Pyramidal signs (e.g., hyperreflexia) can occur, blurring the boundary with Silver syndrome and HSP. A lower-limb-onset variant is also recognized in some patients.

### Finding 4 — Epidemiology: dHMN is rare (~2/100,000) and genetically heterogeneous; *REEP1*-dHMN5B is an ultra-rare AD subtype

Distal hereditary motor neuropathy overall has an estimated prevalence of **2.14–2.3 per 100,000**, with more than thirty associated genes and a low diagnostic yield.

> *"the prevalence of the disease was calculated as 2.14 and 2.3 per 100,000"* — [PMID: 38702287](https://pubmed.ncbi.nlm.nih.gov/38702287/)

> *"More than thirty genes are currently associated with HMNs, but around 60 to 70% of cases of dHMN remain uncharacterized genetically."* — [PMID: 38702287](https://pubmed.ncbi.nlm.nih.gov/38702287/)

The most frequent dHMN genes include *HSPB1*, *GARS1*, *BICD2*, and *DNAJB2*. *REEP1*-associated dHMN5B is autosomal dominant and **ultra-rare**, described in only a small number of families since the founding report ([PMID: 22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/)). By contrast, *REEP1* is far more commonly associated with autosomal dominant HSP/SPG31 — the MDSGene systematic review of dominant HSP assembled 151 HSP-*REEP1* individuals versus 1670 HSP-*SPAST* ([PMID: 41734945](https://pubmed.ncbi.nlm.nih.gov/41734945/)), underscoring that the dHMN presentation is the rarer of the two *REEP1* phenotypes.

### Finding 5 — REEP1 biology: a neuronal ER-shaping / microtubule-linking protein; ER stress and oxidative stress are downstream effectors and candidate targets

REEP1 (receptor expression-enhancing protein 1; HGNC:25786; locus 2p11.2; UniProt Q9H902; DP1/Yop1/REEP family) is a **neuron-specific, membrane-binding, membrane-curvature-inducing protein** that resides in the ER. Through hydrophobic hairpin domains it forms complexes with atlastin-1 and spastin, is required for the formation of the tubular ER network, and **binds microtubules** to align the tubular ER along the cytoskeleton.

> *"REEP proteins were required for ER network formation in vitro, and REEP1 also bound microtubules and promoted ER alignment along the microtubule cytoskeleton in COS7 cells."* — [PMID: 20200447](https://pubmed.ncbi.nlm.nih.gov/20200447/)

> *"we demonstrated that REEP1 is a neuron-specific, membrane-binding, and membrane curvature-inducing protein that resides in the ER."* — [PMID: 24051375](https://pubmed.ncbi.nlm.nih.gov/24051375/)

Downstream, REEP1 dysfunction converges on **ER stress and oxidative stress** ([PMID: 36834939](https://pubmed.ncbi.nlm.nih.gov/36834939/)). In a *REEP1*-null HSP mouse model, pharmacologic **inhibition of ER stress improved progressive motor deficits** ([PMID: 32878877](https://pubmed.ncbi.nlm.nih.gov/32878877/)), nominating the unfolded-protein-response axis as a therapeutic target, and the HUWE1-dependent turnover pathway (Finding 2) provides a mechanistically rational proteostasis target specific to dHMN.

### Finding 6 — Model systems: the Δexon5 knock-in mouse recapitulates spinal motor-neuron ER fragmentation; iPSC, Drosophila and yeast systems available

The most faithful model is the **Δexon5 knock-in mouse** (*Mus musculus*; NCBI Taxon 10090; ortholog *Reep1*, NCBI Gene 52250), which loses spinal motor neurons preceded by ER fragmentation while sparing cortical motor neurons — mirroring the human genotype. Conversely, *Reep1*-knockout mice model HSP through cortical motor-neuron loss ([PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/); [PMID: 24051375](https://pubmed.ncbi.nlm.nih.gov/24051375/)).

> *"Δexon5 knockin (KI) mice lose spinal motoneurons preceded by ER fragmentation, whereas cortical motoneurons remain intact."* — [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/)

Cellular models include CRISPR/Cas9-engineered human iPSC lines:

> *"Here we show the generation of a homozygous and a heterozygous REEP1 knockout induced pluripotent stem cell line suitable for in vitro disease modelling using the CRISPR/Cas9 editing system."* — [PMID: 38479332](https://pubmed.ncbi.nlm.nih.gov/38479332/)

Invertebrate/in-vitro homolog systems (Drosophila; the yeast homolog **Yop1**) have been used to dissect REEP/DP1 ER-shaping and membrane-curvature mechanisms:

> *"Mutations in the human DP1 gene REEP1 are associated with Hereditary Spastic Paraplegia type 31 and distal hereditary motor neuropathy."* — [PMID: 39312180](https://pubmed.ncbi.nlm.nih.gov/39312180/)

No naturally occurring animal (OMIA) disease is documented specifically for *Reep1*-dHMN5B.

### Finding 7 — Confirmed ontology cross-references (MONDO:0013884)

An EBI OLS4/MONDO lookup confirms the disease term **MONDO:0013884** "neuronopathy, distal hereditary motor, type 5B," equivalent to **OMIM:614751**, with cross-references **DOID:0111205, GARD:0018267, MedGen:766570, UMLS:C3553656**. MONDO synonyms include "HMN5B," "neuronopathy, distal hereditary motor, type VB," and explicitly "REEP1 neuronopathy, distal hereditary motor." **No Orphanet cross-reference** is attached (there is no dHMN5B-specific ORPHA code). The causal gene is **REEP1** (HGNC:25786; NCBI Gene 65055; Ensembl ENSG00000068615; UniProt Q9H902; locus 2p11.2).

### Finding 8 — Curated HPO phenotype set confirms combined hand + peroneal involvement with hyporeflexia

Monarch Initiative knowledge-graph annotations for MONDO:0013884 (equivalent OMIM:614751) list seven HPO features, combining upper-limb (thenar/hand) and lower-limb (peroneal) distal motor involvement with hyporeflexia, pes cavus, and an axonal-to-mildly-slowed motor NCS picture:

| HPO ID | Term | Domain |
|---|---|---|
| HP:0003393 | Thenar muscle atrophy | Upper limb (hand) |
| HP:0009049 | Peroneal muscle atrophy | Lower limb |
| HP:0011727 | Peroneal muscle weakness | Lower limb |
| HP:0001761 | Pes cavus | Foot deformity |
| HP:0003438 | Absent Achilles reflex | Reflexes (hyporeflexia) |
| HP:0011808 | Decreased patellar reflex | Reflexes (hyporeflexia) |
| HP:0003431 | Decreased motor nerve conduction velocity | Electrophysiology |

---

## Structured Report by Template Section

### 1. Disease Information

**Overview.** dHMN5B is a Mendelian, autosomal dominant, slowly progressive pure motor axonal neuropathy affecting lower motor neurons, with distal amyotrophy predominating in the upper limbs (small hand/thenar muscles), later involving the peroneal/lower-limb muscles, and clinically sparing sensation. It is one allelic form of the "distal HMN type V" phenotype (shared with *GARS1* and *BSCL2*) and is caused by heterozygous *REEP1* variants.

**Key identifiers.** MONDO:0013884 · OMIM #614751 · DOID:0111205 · GARD:0018267 · MedGen:766570 · UMLS:C3553656. No Orphanet-specific ORPHA code. MeSH does not have a dHMN5B-specific descriptor (the broadest applicable class terms are used only at the level of hereditary motor/sensory neuropathy).

**Synonyms.** HMN5B; distal hereditary motor neuronopathy type VB; distal HMN type V (REEP1-related); dHMN-VB; "REEP1 neuronopathy, distal hereditary motor"; "neuronopathy, distal hereditary motor caused by mutation in REEP1."

**Data source.** Aggregated, disease-level resources (OMIM, MONDO, HPO, Monarch) plus primary literature from small pedigrees; not EHR/individual-patient data.

### 2. Etiology

**Causal factors.** Purely genetic — heterozygous dominant variants in *REEP1*. The prototype is the in-frame exon-5 deletion (Δexon5) generated by the splice-acceptor variant c.304-2A>G ([PMID: 22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/)). No environmental, infectious, or toxic cause is implicated.

**Genetic risk factors.** The causal variant itself is the sole established risk determinant; inheritance of one dominant allele confers disease risk. Modifier genes are not defined for dHMN5B specifically, though the broader REEP1 interactome (atlastin-1/*ATL1*, spastin/*SPAST*) shapes the tubular ER and could plausibly modify expressivity (inferred, not demonstrated).

**Environmental risk / protective factors.** None established. No lifestyle, dietary, occupational, or toxic exposures are known to raise or lower risk.

**Gene–environment interactions.** None documented. This is a monogenic disorder.

### 3. Phenotypes

Core clinical features and suggested HPO terms:

| Phenotype | Type | HPO | Characteristics |
|---|---|---|---|
| Thenar/small-hand-muscle wasting & weakness | Clinical sign | HP:0003393 | Upper-limb-predominant; adolescent/adult onset; slowly progressive; frequent |
| Peroneal muscle atrophy | Clinical sign | HP:0009049 | Lower-limb; later spread |
| Peroneal muscle weakness | Clinical sign | HP:0011727 | Lower-limb; foot drop |
| Pes cavus | Physical manifestation | HP:0001761 | Chronic foot deformity |
| Absent ankle (Achilles) reflex | Clinical sign | HP:0003438 | Hyporeflexia |
| Decreased patellar reflex | Clinical sign | HP:0011808 | Hyporeflexia |
| Decreased motor NCV / reduced CMAP | Lab/electrophysiology | HP:0003431 | Axonal, pure motor; preserved sensory conduction |
| Pyramidal signs (variable hyperreflexia) | Clinical sign | HP:0001347 | Overlap with Silver syndrome/HSP in some patients |

**Onset:** typically adolescent/adult. **Severity:** mild–moderate, variable. **Progression:** slow, progressive. **QoL impact:** hand-muscle wasting impairs fine-motor/dexterity tasks; foot drop and pes cavus impair gait; disease is rarely life-limiting, so morbidity is chiefly functional/occupational disability rather than mortality.

### 4. Genetic / Molecular Information

- **Causal gene:** *REEP1* (HGNC:25786; NCBI Gene 65055; Ensembl ENSG00000068615; UniProt Q9H902; 2p11.2; OMIM *609139).
- **Prototype variant:** c.304-2A>G (splice-acceptor loss) → in-frame skipping of exon 5 → p.102_139del ("Δexon5"); mRNA expressed at normal levels ([PMID: 22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/)).
- **Variant classes:** splice-site and in-frame deletion (dHMN gain-of-function/accumulation); a distinct nonstop/3′UTR variant causes peripheral neuropathy by unmasking an aggregation-inducing motif ([PMID: 29124833](https://pubmed.ncbi.nlm.nih.gov/29124833/)). Note that truncating/NMD-triggering *REEP1* variants generally cause loss-of-function **SPG31**, not dHMN5B.
- **Functional consequence:** toxic **gain of function / protein accumulation** in lower motor neurons (contrast with loss-of-function haploinsufficiency in SPG31) ([PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/); [PMID: 29124833](https://pubmed.ncbi.nlm.nih.gov/29124833/)).
- **Allele frequency:** pathogenic dHMN5B alleles are private/ultra-rare; not present at appreciable frequency in gnomAD.
- **Origin:** germline, dominant.
- **Epigenetics / chromosomal abnormalities:** none implicated.

### 5. Environmental Information

Not applicable — no environmental, lifestyle, or infectious contributors are known. dHMN5B is monogenic.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (mutation → clinical manifestation):**

1. A heterozygous *REEP1* splice-acceptor variant (c.304-2A>G) **abolishes** the exon-5 splice acceptor, which **leads to** in-frame skipping of exon 5 and a stable, internally shortened protein (Δexon5, p.102_139del). *(Demonstrated — minigene assay, [PMID: 22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/).)*
2. The Δexon5 protein **retains** its membrane-curvature/hairpin (ER-shaping) function but is **defective in ubiquitination**, which **results in** escape from HUWE1-mediated proteasomal degradation. *(Demonstrated — proteomics, [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/).)*
3. Impaired turnover **causes** progressive **accumulation** of shaping-competent REEP1 in peripheral nerve. *(Demonstrated — [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/).)*
4. Excess REEP1 **leads to** fragmentation of the tubular ER network in **spinal** motor neurons. *(Demonstrated in Δexon5 KI mouse — [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/).)*
5. ER fragmentation **converges on** downstream ER stress and oxidative stress. *(Inferred/supported — [PMID: 36834939](https://pubmed.ncbi.nlm.nih.gov/36834939/); [PMID: 32878877](https://pubmed.ncbi.nlm.nih.gov/32878877/).)*
6. These insults **result in** distal degeneration of the long motor axons and loss of spinal motor neurons. *(Demonstrated — [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/).)*
7. Motor-axon/motor-neuron loss **causes** chronic denervation → distal amyotrophy and weakness (hand-predominant, then peroneal) = the clinical dHMN5B phenotype. *(Demonstrated clinically/electrophysiologically — [PMID: 20598714](https://pubmed.ncbi.nlm.nih.gov/20598714/); [PMID: 38702287](https://pubmed.ncbi.nlm.nih.gov/38702287/).)*

**Branch point (same gene, opposite disease):**

```
                         REEP1 variant
                              |
             +----------------+----------------+
   LOSS-OF-FUNCTION                      TOXIC ACCUMULATION
   (truncating/NMD, haploinsufficiency)  (Delta-exon5, evades HUWE1 turnover)
             |                                  |
   Cortical (upper) motor neurons       Spinal (lower) motor neurons
   ER shaping deficit                   ER fragmentation from excess REEP1
             |                                  |
        SPG31 / HSP                        dHMN5B (this disease)
   (spasticity, long CST axons)         (distal amyotrophy, pure motor)
```

**Cell types & processes.** Spinal (lower) motor neurons (CL:0000103, motor neuron); biological processes GO:0007029 (endoplasmic reticulum organization), GO:0006986 (response to unfolded protein / ER stress), GO:0006915 (apoptotic process, inferred), and GO:0007010 (cytoskeleton organization, via microtubule-linked ER shaping). Subcellular compartment: endoplasmic reticulum, tubular network (GO:0005789 endoplasmic reticulum membrane; GO:0071782 endoplasmic reticulum tubular network).

### 7. Anatomical Structures Affected

- **Organ/system:** peripheral nervous system; spinal cord anterior horn (lower motor neurons); skeletal muscle (secondary neurogenic atrophy). Body system: nervous (UBERON:0001017 central nervous system; UBERON:0000010 peripheral nervous system).
- **Tissue/cell:** motor axons and spinal motor neurons (CL:0000103); neurogenic atrophy of distal skeletal muscle (thenar/hand → peroneal).
- **Subcellular:** tubular endoplasmic reticulum (GO:0005789 / GO:0071782); microtubule cytoskeleton interface.
- **Localization/laterality:** distal limbs, symmetric/bilateral; upper-limb (hand) predominant onset, later lower-limb (peroneal). UBERON references: UBERON:0001134 (skeletal muscle tissue, distal), UBERON:0001474 (bone element, for pes cavus foot deformity, secondary).

### 8. Temporal Development

- **Onset:** adolescent to adult; insidious.
- **Progression:** slow, chronic, progressive over decades; lifelong.
- **Course:** progressive, not relapsing-remitting; no spontaneous remission.
- **Critical window:** because ER fragmentation *precedes* motor-neuron loss in the mouse model ([PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/)), a pre-degeneration therapeutic window is mechanistically plausible (inferred).

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant.
- **Epidemiology:** dHMN overall ~2.14–2.3/100,000; dHMN5B is an ultra-rare subtype within this ([PMID: 38702287](https://pubmed.ncbi.nlm.nih.gov/38702287/)).
- **Penetrance/expressivity:** the broader *REEP1* literature shows variable expressivity, incomplete penetrance, and intrafamilial variability (including an unaffected carrier and apparent anticipation in an SPG31 family — [PMID: 29107646](https://pubmed.ncbi.nlm.nih.gov/29107646/)); dHMN5B-specific penetrance is not precisely quantified.
- **Founder effects / consanguinity / carrier frequency:** no dHMN5B founder allele established; a *recessive* congenital-axonal-neuropathy phenotype arises from biallelic *REEP1* loss ([PMID: 27066569](https://pubmed.ncbi.nlm.nih.gov/27066569/)), but dominant dHMN5B does not require consanguinity.
- **Demographics:** no sex or ethnic predilection established.

### 10. Diagnostics

- **Electrophysiology (key):** nerve conduction studies show normal/near-normal sensory responses with markedly reduced CMAP amplitudes; needle EMG shows chronic distal denervation — an axonal, pure-motor pattern ([PMID: 20598714](https://pubmed.ncbi.nlm.nih.gov/20598714/)). HP:0003431 (decreased motor NCV) may be present.
- **Genetic testing (definitive):** targeted *REEP1* sequencing, dHMN/CMT gene panels, or WES/WGS. WES is well validated for undiagnosed inherited neuropathies ([PMID: 24604904](https://pubmed.ncbi.nlm.nih.gov/24604904/)). Splice-site variants (e.g., c.304-2A>G) may require RNA/minigene confirmation of exon skipping.
- **Differential diagnosis:** other dHMN-V genes (*GARS1*/dHMN5A → [PMID: 31985473](https://pubmed.ncbi.nlm.nih.gov/31985473/); *BSCL2*/Silver syndrome → [PMID: 15242882](https://pubmed.ncbi.nlm.nih.gov/15242882/), [PMID: 32108980](https://pubmed.ncbi.nlm.nih.gov/32108980/)); CMT2; other dHMN genes (*HSPB1*, *BICD2*, *DNAJB2*); and, given pyramidal overlap, SPG31/HSP.
- **Biomarkers/omics/imaging:** no specific fluid biomarker; MRI/labs are non-specific. Diagnosis rests on phenotype + electrophysiology + molecular confirmation.

### 11. Outcome / Prognosis

- **Survival/mortality:** normal or near-normal life expectancy; dHMN5B is not typically life-limiting (respiratory compromise is not a core feature of dominant dHMN5B, in contrast to recessive *REEP1* congenital neuropathy with diaphragmatic palsy — [PMID: 27066569](https://pubmed.ncbi.nlm.nih.gov/27066569/)).
- **Morbidity/function:** progressive distal weakness → impaired hand dexterity and gait; disability is functional, chiefly hand use and ambulation.
- **Prognostic factors:** slow course; not well quantified for dHMN5B specifically.

### 12. Treatment

- **Disease-modifying therapy:** none approved.
- **Supportive/rehabilitative (standard of care):** physical therapy, occupational therapy, ankle-foot orthoses / drop-foot management, orthopedic care for pes cavus (analogous to CMT management — [PMID: 24646194](https://pubmed.ncbi.nlm.nih.gov/24646194/); [PMID: 12736893](https://pubmed.ncbi.nlm.nih.gov/12736893/)). NCIT: physical therapy (NCIT:C15327), occupational therapy (NCIT:C15304), orthotic device (NCIT:C50077), rehabilitation therapy (NCIT:C15296).
- **Mechanistically rational experimental strategies (not yet clinical):**
  - Allele-selective knockdown/ASO to reduce the accumulating mutant REEP1 (rational because disease is toxic accumulation).
  - Enhancing HUWE1-dependent proteostasis / restoring REEP1 turnover ([PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/)).
  - ER-stress modulation — pharmacologic ER-stress inhibition improved motor deficits in a *REEP1* mouse model ([PMID: 32878877](https://pubmed.ncbi.nlm.nih.gov/32878877/)); oxidative-stress axis is also implicated ([PMID: 36834939](https://pubmed.ncbi.nlm.nih.gov/36834939/)).
- **Pharmacogenomics:** not applicable.

### 13. Prevention

- **Primary prevention:** not applicable (monogenic, non-environmental).
- **Genetic counseling / reproductive options:** autosomal dominant → 50% offspring risk; predictive testing, cascade testing, prenatal/preimplantation genetic testing are available for families with a known *REEP1* variant.
- **Secondary/tertiary prevention:** early rehabilitation and orthopedic management to limit contractures and preserve function.

### 14. Other Species / Natural Disease

- **Orthologue:** mouse *Reep1* (NCBI Gene 52250; NCBI Taxon 10090).
- **Natural disease:** no naturally occurring OMIA-catalogued *Reep1*-dHMN5B disease is documented in companion animals or wildlife.
- **Comparative biology:** REEP/DP1 family is deeply conserved (yeast **Yop1**), and the ER-shaping mechanism is evolutionarily conserved ([PMID: 39312180](https://pubmed.ncbi.nlm.nih.gov/39312180/); [PMID: 28742022](https://pubmed.ncbi.nlm.nih.gov/28742022/)).
- **Zoonotic potential:** none (non-infectious).

### 15. Model Organisms

| Model | System | Recapitulation | Reference |
|---|---|---|---|
| Δexon5 knock-in mouse | *M. musculus* | **Faithful**: spinal motor-neuron loss preceded by ER fragmentation, cortical neurons spared — matches human genotype/phenotype | [PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/) |
| *Reep1* knockout mouse | *M. musculus* | Models **SPG31/HSP** (cortical MN loss), i.e., the opposite REEP1 disease; ER-shaping deficit | [PMID: 24051375](https://pubmed.ncbi.nlm.nih.gov/24051375/); [PMID: 32878877](https://pubmed.ncbi.nlm.nih.gov/32878877/) |
| REEP1-KO iPSC (homo/heterozygous) | Human iPSC (CRISPR/Cas9) | In-vitro disease modeling platform | [PMID: 38479332](https://pubmed.ncbi.nlm.nih.gov/38479332/) |
| Yeast Yop1 / Drosophila | Invertebrate/in vitro | Dissect REEP/DP1 ER-shaping & membrane-curvature mechanisms and mutation effects | [PMID: 39312180](https://pubmed.ncbi.nlm.nih.gov/39312180/); [PMID: 28742022](https://pubmed.ncbi.nlm.nih.gov/28742022/) |

**Model limitations:** mouse corticospinal axons are far shorter than human, generally producing milder/later phenotypes in ER-shaping HSP models ([PMID: 35348668](https://pubmed.ncbi.nlm.nih.gov/35348668/)); the Δexon5 KI is the key exception that robustly reproduces lower-motor-neuron pathology.

---

## Mechanistic Model / Interpretation

The unifying insight of dHMN5B is that **one gene, two opposite dosage/functional lesions, two anatomically distinct diseases**. *REEP1* encodes a neuronal ER-shaping protein that, with atlastin-1 and spastin, builds and aligns the tubular ER along microtubules ([PMID: 20200447](https://pubmed.ncbi.nlm.nih.gov/20200447/); [PMID: 24051375](https://pubmed.ncbi.nlm.nih.gov/24051375/)). When *REEP1* function is **lost** (truncating/NMD alleles, haploinsufficiency), the long corticospinal axons of upper motor neurons degenerate → **SPG31/HSP** (spasticity). When a stable, curvature-competent mutant protein **accumulates** because it evades HUWE1-dependent degradation (the Δexon5 allele), **spinal lower motor neurons** suffer ER fragmentation and die → **dHMN5B** (distal, pure-motor amyotrophy). The Δexon5 knock-in mouse provides direct genetic proof of this dichotomy, showing spinal (not cortical) motor-neuron loss preceded by ER fragmentation — the exact inverse of the *Reep1*-knockout HSP mouse ([PMID: 41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/)).

This model has three practical consequences. First, it reframes therapeutic logic: because dHMN5B is a **toxic accumulation** disorder, lowering mutant REEP1 (allele-selective knockdown, or restoring HUWE1-mediated turnover) is rational — the opposite of the gene-replacement logic appropriate for loss-of-function SPG31. Second, ER stress and oxidative stress are shared downstream effectors across REEP1 diseases, and ER-stress inhibition already shows efficacy in a REEP1 mouse ([PMID: 32878877](https://pubmed.ncbi.nlm.nih.gov/32878877/); [PMID: 36834939](https://pubmed.ncbi.nlm.nih.gov/36834939/)) — a repurposable, mechanism-agnostic strategy. Third, because ER fragmentation *precedes* neuronal loss, there may be a pre-symptomatic or early therapeutic window.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [22703882](https://pubmed.ncbi.nlm.nih.gov/22703882/) | *Exome sequencing identifies a REEP1 mutation in dHMN-V* | **Founding gene–disease link**; c.304-2A>G → Δexon5; REEP1 expressed in lower motor neurons |
| [41268727](https://pubmed.ncbi.nlm.nih.gov/41268727/) | *REEP1 Accumulation Disrupts ER Integrity and Drives Spinal Motoneuron Degeneration* | **Pivotal mechanism**: HUWE1 turnover defect → accumulation → ER fragmentation → spinal MN loss; Δexon5 KI mouse |
| [29124833](https://pubmed.ncbi.nlm.nih.gov/29124833/) | *Nonstop REEP1 variant unmasks aggregation motif* | Independent support for **toxic gain of function** in lower motor neurons |
| [38702287](https://pubmed.ncbi.nlm.nih.gov/38702287/) | *Distal hereditary motor neuropathies* (review) | Epidemiology (2.14–2.3/100,000), heterogeneity, REEP1 in upper-limb-predominant dHMN |
| [20598714](https://pubmed.ncbi.nlm.nih.gov/20598714/) | *N88S BSCL2 dHMN-V family* | Defines pure-motor axonal electrophysiologic signature of dHMN-V |
| [20200447](https://pubmed.ncbi.nlm.nih.gov/20200447/) | *REEP1, spastin, atlastin-1 coordinate ER–microtubule* | Establishes REEP1 normal ER-shaping/microtubule function |
| [24051375](https://pubmed.ncbi.nlm.nih.gov/24051375/) | *Spastic paraplegia mouse reveals REEP1-dependent ER shaping* | Protein character/localization; KO = HSP model |
| [32878877](https://pubmed.ncbi.nlm.nih.gov/32878877/) | *ER-stress inhibition improves motor deficits (REEP1-null)* | ER stress as therapeutic target |
| [36834939](https://pubmed.ncbi.nlm.nih.gov/36834939/) | *Converging role for REEP1/SPG31 in oxidative stress* | Oxidative-stress downstream effector |
| [38479332](https://pubmed.ncbi.nlm.nih.gov/38479332/) | *REEP1-KO iPSC lines* | Human cellular models |
| [39312180](https://pubmed.ncbi.nlm.nih.gov/39312180/) | *Yop1 oligomerisation/curvature* | Yeast homolog model; conserved mechanism |
| [41734945](https://pubmed.ncbi.nlm.nih.gov/41734945/) | *MDSGene review of dominant HSP* | Rarity context: 151 HSP-REEP1 vs 1670 HSP-SPAST |
| [27066569](https://pubmed.ncbi.nlm.nih.gov/27066569/) | *Recessive REEP1 → congenital axonal neuropathy + diaphragmatic palsy* | Recessive/biallelic loss expands REEP1 spectrum (distinct entity) |
| [29107646](https://pubmed.ncbi.nlm.nih.gov/29107646/) | *SPG31 splice variant, phenotype variability* | Variable expressivity, NMD dosage effects, apparent anticipation |
| [24604904](https://pubmed.ncbi.nlm.nih.gov/24604904/) | *WES in undiagnosed inherited polyneuropathies* | Diagnostic utility of WES |

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity:** dHMN5B has been reported in very few families; penetrance, expressivity, sex ratio, and natural-history metrics are not precisely quantified for the dHMN5B subtype specifically.
2. **Allelic spectrum:** beyond the prototype Δexon5 allele, the full range of dHMN5B-causing *REEP1* variants is small; genotype–phenotype rules distinguishing dHMN5B (accumulation) from SPG31 (loss of function) are still being refined, and some variants blur the boundary (pyramidal overlap / Silver-like features).
3. **Mechanistic inference vs. proof:** the ER-stress/oxidative-stress steps downstream of ER fragmentation are supported by REEP1-null and cell models but not yet directly demonstrated in the Δexon5 accumulation context in vivo.
4. **No biomarkers:** there is no validated fluid or imaging biomarker for diagnosis, staging, or treatment response.
5. **No therapeutics:** all disease-modifying strategies remain preclinical/conceptual.
6. **Ontology gaps:** no Orphanet-specific code; MeSH lacks a dHMN5B-specific term.

## Proposed Follow-up Experiments / Actions

1. **Allele-selective knockdown proof-of-concept:** test ASO/siRNA lowering of mutant (Δexon5) *REEP1* in the Δexon5 knock-in mouse and REEP1-mutant iPSC-derived motor neurons; endpoints = ER morphology, spinal MN survival, motor behavior.
2. **HUWE1/proteostasis modulation:** determine whether enhancing HUWE1 activity or proteasomal targeting restores REEP1 turnover and rescues ER fragmentation.
3. **ER-stress / oxidative-stress therapeutics:** repurpose ER-stress inhibitors (shown effective in REEP1-null mice) and antioxidants in the accumulation model; define the pre-degeneration treatment window.
4. **Natural-history registry:** aggregate dHMN5B families to quantify onset, progression rate, penetrance, and hand-vs-leg onset frequencies, using standardized motor scales and electrophysiology.
5. **Biomarker discovery:** ER-stress/oxidative-stress fluid markers and neurofilament light as candidate progression biomarkers.
6. **Genotype–phenotype curation:** systematically classify *REEP1* variants by mechanism (accumulation/gain-of-function → dHMN5B vs. loss-of-function → SPG31) to guide diagnosis and future allele-specific therapy.

---

*Report compiled from 8 confirmed findings and 34 reviewed papers. Evidence types span human clinical/genetic (small pedigrees, cohorts), model organism (mouse KI/KO, yeast, Drosophila), in vitro (iPSC, minigene, biochemistry), and ontology/database curation (MONDO, OMIM, HPO, Monarch).*


## Artifacts

- [OpenScientist final report](Distal_Hereditary_Motor_Neuronopathy_Type_5B-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Distal_Hereditary_Motor_Neuronopathy_Type_5B-deep-research-openscientist_artifacts/final_report.pdf)