---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:51:57.686624'
end_time: '2026-08-01T18:02:05.595334'
duration_seconds: 607.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Idiopathic Pulmonary Arterial Hypertension
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Idiopathic_Pulmonary_Arterial_Hypertension-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Pulmonary Arterial Hypertension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Pulmonary Arterial Hypertension** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Pulmonary Arterial Hypertension
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Pulmonary Arterial Hypertension** covering all of the
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


# Idiopathic Pulmonary Arterial Hypertension: Disease Characteristics Report

## Executive summary

Idiopathic pulmonary arterial hypertension (IPAH) is a rare, progressive **WHO Group 1 pulmonary arterial hypertension (PAH)** in which precapillary pulmonary hypertension is confirmed invasively and no associated disease, drug exposure, or recognized heritable cause adequately explains it. The current hemodynamic definition is mean pulmonary arterial pressure (mPAP) **>20 mmHg**, pulmonary arterial wedge pressure (PAWP) **≤15 mmHg**, and pulmonary vascular resistance (PVR) **>2 Wood units**, measured by right-heart catheterization (RHC). IPAH is therefore a diagnosis of both positive hemodynamic findings and exclusion. Contemporary incidence estimates for PAH are approximately 2.5–7.5 per million person-years and prevalence 15–50 per million; diagnostic delay remains about 2.8 years because early symptoms are nonspecific. (eichstaedt2023geneticcounsellingand pages 1-2)

The central biological model is genetically or epigenetically reduced endothelial BMP–BMPR2 signaling, interacting with sex, aging, inflammation, metabolism, and other “second hits.” Endothelial dysfunction initiates vasoconstriction, thrombosis and endothelial-to-mesenchymal transition; smooth-muscle and fibroblast proliferation then produces obliterative remodeling, rising PVR, right-ventricular (RV) overload, and ultimately RV failure. Recent advances include expert-curated gene panels, single-cell identification of immune–vascular CCL5 signaling, multi-omic evidence implicating ferroptosis, and approval of the activin-signaling ligand trap sotatercept. (austin2024geneticsandprecision pages 2-3, li2024bonemorphogeneticprotein pages 9-11, li2024anewintegrative pages 1-2, kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5)

| Domain | Current finding | Quantitative detail | Evidence type/source/year |
|---|---|---|---|
| Hemodynamic definition | IPAH is a subgroup of precapillary pulmonary arterial hypertension defined by elevated pulmonary pressures with normal left-sided filling pressure and increased pulmonary vascular resistance. | PH: mPAP >20 mmHg; precapillary PH: PAWP ≤15 mmHg and PVR >2 Wood units. Updated threshold reflected in 2022 ESC/ERS and 2024 WSPH-aligned sources. | Human clinical/guideline review, ERJ 2024; consensus statement 2023 (eichstaedt2023geneticcounsellingand pages 1-2) |
| Epidemiology | IPAH/PAH remains a rare disease with low incidence and prevalence, but registries show persistent global burden. | Incidence 2.5–7.5 cases per million/year; prevalence 15–50 per million. Female predominance reported; one review cites PAH female:male ratio 4.3:1 and IPAH 4.1:1. | Human registry/review, ERJ 2023; J Transl Med 2023 (eichstaedt2023geneticcounsellingand pages 1-2, dave2023unravelingtheepigenetic pages 1-2) |
| Genetics | BMPR2 is the leading causal gene; current gene curation supports a broader panel for heritable/idiopathic disease. | 12 genes with definitive evidence: BMPR2, ACVRL1, ATP13A3, CAV1, EIF2AK4, ENG, GDF2, KCNK3, KDR, SMAD9, SOX17, TBX4; 3 moderate: ABCC8, GGCX, TET2; 6 limited including AQP1, BMP10, FBLN2, KLF2, KLK1, PDGFD. | Human genetics review/consensus, ERJ 2024 and 2023 (austin2024geneticsandprecision pages 2-3, eichstaedt2023geneticcounsellingand pages 1-2, OpenTargets Search: idiopathic pulmonary arterial hypertension) |
| Symptoms / diagnostic delay | Clinical presentation is nonspecific and commonly delayed, contributing to advanced disease at diagnosis. | Common symptoms: fatigue, dyspnea on exertion, chest pain, syncope; mean diagnostic delay ~2.8 years. | Human clinical consensus/review, ERJ 2023 (eichstaedt2023geneticcounsellingand pages 1-2) |
| Survival / prognosis | Outcomes have improved with therapy but long-term prognosis remains poor and heterogeneous. | Historical median survival without treatment ~2.8 years; current era median survival >7 years in one review. Population-based adult PAH survival ranges: 1-year 85–99%, 3-year 65–95%, 5-year 50–86%; Europe pooled 1-year 90%, 3-year 78%, 5-year 61%. | Human observational review/systematic review, 2023–2024 (dave2023unravelingtheepigenetic pages 1-2, mocumbi2024pulmonaryhypertension pages 17-17) |
| Risk assessment | Low-risk status remains the therapeutic goal; noninvasive markers anchor current models, with hemodynamics/imaging adding value. | Core predictors across tools: WHO functional class, 6MWD, natriuretic peptides; additional prognostic variables include PVR, CI, RAP/right atrial area, and RV imaging parameters. | Human prognostic review, ERJ 2024 (mocumbi2024pulmonaryhypertension pages 17-17) |
| Sotatercept | First-in-class activin-signaling inhibitor adds disease-modifying therapy beyond vasodilator pathways. | In STELLAR post hoc analysis at 24 weeks vs placebo: mPAP −13.9 mmHg, PVR −254.8 dyn·s·cm⁻⁵, mean RAP −2.7 mmHg, mixed venous O2 saturation +3.84%, PA compliance +0.58 mL·mmHg⁻¹, RV end-diastolic area −5.31 cm². PULSAR showed ~18% PVR reduction. | Human phase 2/3 trial evidence, ERJ 2023; review 2023 (jin2023medicalmanagementof pages 16-17) |
| 2024 single-cell immune findings | IPAH inflammatory signaling includes adaptive immune–vascular crosstalk, especially T/NK-cell mediated communication. | Hub genes identified: CXCL9, CCL5, GZMA, GZMK; scRNA-seq localized CCL5/GZMA mainly to T and NK cells interacting with endothelial cells, smooth muscle cells, and fibroblasts. | Human transcriptomic + scRNA-seq with animal validation, J Transl Med 2024 (li2024anewintegrative pages 1-2) |
| 2024 ferroptosis findings | Ferroptosis is implicated as a pathogenic upstream inflammatory mechanism linking endothelial injury to remodeling. | In MCT rats, ferrostatin-1 1 mg/kg/day mitigated PAH severity; model used MCT 60 mg/kg. Mechanistic data linked ferroptotic PAEC DAMPs to complement activation, macrophage recruitment, PASMC proliferation, and inflammatory monocyte phenotypes. | Human multiomics + animal + in vitro mechanistic study, Circ Res 2024 (kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5) |


*Table: This table compiles compact, high-yield evidence for idiopathic pulmonary arterial hypertension across core knowledge-base domains. It highlights current definitions, burden, genetics, prognosis, treatment advances, and 2024 mechanistic discoveries using only previously gathered sources.*

## 1. Disease information

### Definition and classification

IPAH is PAH without an identified associated condition or exposure after a complete evaluation. It belongs to WHO clinical **Group 1**, not to PH caused by left-heart disease (Group 2), lung disease/hypoxia (Group 3), pulmonary-artery obstruction including chronic thromboembolic PH (Group 4), or multifactorial disease (Group 5). Pulmonary microvascular obliteration raises PVR and pulmonary arterial pressure, progressively impairing RV function. (eichstaedt2023geneticcounsellingand pages 1-2)

**Current identifiers and terminology**

- **MONDO:** MONDO:0001999, idiopathic pulmonary arterial hypertension; broader PAH is MONDO:0015924. OpenTargets independently maps MONDO:0001999 to BMPR2, EIF2AK4, SMAD9 and PTGIR evidence. (OpenTargets Search: idiopathic pulmonary arterial hypertension)
- **OMIM:** 178600, historically “primary pulmonary hypertension 1,” primarily associated with BMPR2-related disease. OMIM’s historical category overlaps IPAH and heritable PAH and should not be treated as perfectly equivalent to modern IPAH.
- **Orphanet:** ORPHA:275777 is commonly used for idiopathic PAH; verify against the release used by the target knowledge base.
- **ICD-10-CM:** I27.0, primary pulmonary hypertension. **ICD-11:** BB01.0, pulmonary arterial hypertension; local extensions may be needed to encode idiopathic etiology.
- **MeSH:** “Hypertension, Pulmonary” and “Familial Primary Pulmonary Hypertension”; MeSH does not always preserve the modern IPAH/HPAH distinction.
- **Synonyms:** idiopathic PAH, primary pulmonary hypertension, sporadic primary pulmonary hypertension, unexplained PAH. “Primary pulmonary hypertension” is retained in legacy records but is less precise.

This report synthesizes **aggregated disease-level evidence**—registries, cohorts, trials, guidelines and experimental studies—not individual EHR records.

## 2. Etiology and risk architecture

### Causal factors

“Idiopathic” means that no recognized cause remains after evaluation, not that disease is biologically causeless. IPAH is usually modeled as a complex threshold disorder involving rare or common genetic susceptibility, epigenetic regulation and acquired stresses. A patient initially labeled IPAH may be reclassified as heritable PAH after a pathogenic germline variant is found.

### Genetic factors

The 2024 World Symposium genetics task force identified **12 genes with definitive PAH evidence**: **BMPR2, ACVRL1, ATP13A3, CAV1, EIF2AK4, ENG, GDF2, KCNK3, KDR, SMAD9, SOX17, and TBX4**. **ABCC8, GGCX and TET2** had moderate evidence; **AQP1, BMP10, FBLN2, KLF2, KLK1 and PDGFD** had limited evidence. This evidence grading is preferable to treating every published candidate as causal. (austin2024geneticsandprecision pages 2-3)

- **BMPR2** is the dominant gene and usually acts through haploinsufficiency/loss of function. Variants include nonsense, frameshift, splice, missense and exon/whole-gene deletions or duplications.
- **ACVRL1/ENG** connect PAH with hereditary hemorrhagic telangiectasia; **GDF2/BMP10, SMAD9** affect BMP signaling.
- **KCNK3/ABCC8** affect membrane-potential and ion-channel biology.
- **SOX17, TBX4 and KDR** implicate vascular or lung development; TBX4 disease is enriched in childhood onset.
- **Biallelic EIF2AK4** variants indicate pulmonary veno-occlusive disease/pulmonary capillary hemangiomatosis rather than ordinary IPAH and materially alter management. (eichstaedt2023geneticcounsellingand pages 13-14)

PAH panel testing in 325 consecutive patients found pathogenic defects in 23%, with 51 of 79 identified variants in BMPR2. Variant yield depends strongly on phenotype and ancestry. Most clinically relevant variants are germline; a routine somatic-mutation model is not established. Population frequency should be assessed in gnomAD using ancestry-matched data, but no universal allele-frequency cutoff substitutes for ACMG/AMP interpretation.

### Inheritance

BMPR2 and most established genes produce **autosomal-dominant susceptibility with incomplete, age- and sex-dependent penetrance and variable expressivity**. Biallelic EIF2AK4 disease is autosomal recessive. De novo variants occur, especially in developmental genes. Genetic anticipation and germline mosaicism are not established general features. Founder variants have been described in particular families or populations, but no single global founder allele explains IPAH.

### Non-genetic and gene–environment factors

Female sex increases susceptibility—one review reported female:male ratios of 4.3:1 for PAH and 4.1:1 for IPAH—yet males often have poorer RV adaptation. Pregnancy and sex-hormone metabolism can modify risk. Aging, hypoxia, inflammation, viral illness, oxidative stress and vascular injury are plausible second hits, but none is sufficient to define IPAH. (dave2023unravelingtheepigenetic pages 1-2)

Anorexigens/methamphetamines, dasatinib, interferons, mitomycin-C and carfilzomib, portal hypertension, HIV, schistosomiasis, congenital heart disease and connective-tissue disease cause **associated or drug-induced PAH**, not IPAH, and must be excluded. Smoking and air pollution may worsen cardiopulmonary reserve, but neither is a validated specific cause of IPAH. No infectious agent causes IPAH. No reproducible genetic, dietary, pharmacologic or lifestyle **protective factor** is established.

## 3. Phenotypes

IPAH can begin in childhood or late life but is most often recognized in adults. Onset is usually insidious, followed by chronic progressive limitation. The following ontology mappings are suggested; exact phenotype frequencies are inconsistently reported and should not be inferred from referral cohorts.

- **Exertional dyspnea** — symptom; usually early and progressive; often moderate-to-severe by diagnosis. HPO **HP:0002875**. It restricts walking, work and self-care.
- **Fatigue/exercise intolerance** — symptoms caused by low cardiac-output reserve. HPO **HP:0012378**, **HP:0003546**.
- **Chest pain** — symptom, particularly with exertion; HPO **HP:0100749**.
- **Presyncope/syncope** — symptom/sign of inadequate output during exertion; later disease and adverse prognosis. HPO **HP:0001279**.
- **Palpitations/tachycardia** — symptoms/signs; HPO **HP:0001962**, **HP:0001649**.
- **Loud pulmonic component, RV heave, tricuspid-regurgitation murmur** — clinical signs of pressure overload.
- **Peripheral edema, ascites, jugular venous distension and hepatomegaly** — advanced right-heart failure; HPO **HP:0000969**, **HP:0001541**, **HP:0002240**.
- **Cyanosis/hypoxemia** — variable, generally advanced or associated with shunting/low output; HPO **HP:0000961**, **HP:0012418**.
- **Hemodynamic abnormalities** — increased mPAP/PVR, reduced cardiac index and elevated right-atrial pressure in advanced disease.
- **Biomarkers** — elevated BNP/NT-proBNP reflects RV wall stress; iron deficiency, hyperuricemia and abnormal red-cell distribution width may occur but are nonspecific.

The consensus description specifically lists “fatigue, dyspnea on exertion, chest pain, syncope” and reports a mean diagnostic delay of 2.8 years. (eichstaedt2023geneticcounsellingand pages 1-2)

Quality of life is impaired across physical mobility, sleep, emotional health, employment and social participation. PAH-specific instruments include **emPHasis-10**, CAMPHOR and PAH-SYMPACT; generic instruments include EQ-5D and SF-36. Recent population evidence remains much stronger for survival than for longitudinal QoL, an important evidence gap.

## 4. Genetic and molecular information

### Variant interpretation and testing consequences

Use ACMG/AMP classes—pathogenic, likely pathogenic, VUS, likely benign and benign—with disease-specific expert curation. A VUS must not drive predictive testing or irreversible treatment decisions. Test methods should capture single-nucleotide variants, small indels and exon-level copy-number variants. WES/WGS is useful after a negative panel, for atypical syndromic presentations, or in research; WGS may capture noncoding and structural variants but has a larger interpretation burden. Routine karyotype, FISH, repeat-expansion and mitochondrial-DNA testing are not indicated unless another phenotype suggests them.

The international consensus recommends genetic counseling and testing for idiopathic, heritable, anorexigen-induced and congenital-heart-disease PAH and for PVOD/PCH. Benefits include correcting misclassification and cascade detection of healthy carriers who can enter regular surveillance. (eichstaedt2023geneticcounsellingand pages 1-2)

### Modifier and epigenetic biology

Penetrance likely reflects common variants, sex-hormone biology and modifiers of BMP signaling, inflammation and metabolism; validated individual-level modifier tests are not yet available. Reported epigenetic abnormalities include altered DNA methylation, histone acetylation/methylation and noncoding RNAs. Candidate regulators include **DNMTs, TET enzymes, SIN3A, EZH2, HDACs and BRD4**. These findings are mechanistically credible but not clinical diagnostic biomarkers. (dave2023unravelingtheepigenetic pages 1-2)

Large chromosomal abnormalities are not a typical IPAH mechanism, although copy-number loss involving a PAH gene can be pathogenic.

## 5. Environmental and lifestyle information

There is no IPAH-specific toxin, radiation, occupation, diet, alcohol pattern or pathogen. The practical environmental assessment seeks exposures that would **reclassify** disease: appetite suppressants, methamphetamine, dasatinib and other implicated drugs; HIV and schistosomiasis; high-altitude/chronic hypoxia; and occupational or recreational stimulant exposure. Smoking cessation, healthy weight, supervised activity and avoidance of hypoxia improve general reserve but are not proven primary prevention.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream susceptibility:** germline variation or acquired suppression of BMP/BMPR2 signaling, developmental abnormalities, epigenetic dysregulation, sex-hormone effects and environmental second hits.
2. **Endothelial injury:** impaired endothelial survival and repair, reduced nitric oxide/prostacyclin, excess endothelin-1, barrier disruption, EndMT, oxidative stress and thrombogenicity.
3. **Remodeling:** PASMC and adventitial-fibroblast proliferation, apoptosis resistance, extracellular-matrix deposition and inflammatory-cell recruitment produce medial hypertrophy, intimal fibrosis and plexiform/occlusive lesions.
4. **Hemodynamic consequence:** vascular narrowing and vasoconstriction raise PVR and reduce pulmonary arterial compliance.
5. **Clinical consequence:** RV hypertrophy initially compensates; ischemia, fibrosis, dilation and tricuspid regurgitation then cause low output, congestion, syncope and death.

### Core pathways and cells

Reduced endothelial BMP9/BMP10–ALK1–BMPRII–SMAD1/5/9 signaling removes antiproliferative and endothelial-survival signals, while relatively increased TGF-β/activin–SMAD2/3 activity favors remodeling. BMP and activin ligands also compete across BMPRII, ActRIIA and ActRIIB, explaining the mechanistic rationale for sotatercept. (li2024bonemorphogeneticprotein pages 9-11)

Other implicated pathways include PI3K–AKT–mTOR, MAPK/ERK, HIF-1α/HIF-2α, PDGF, serotonin, RhoA/ROCK, NOTCH, Wnt/β-catenin, NF-κB and JAK/STAT3. Metabolic reprogramming includes increased glycolysis, mitochondrial fragmentation/dysfunction, altered fatty-acid oxidation, glutaminolysis and redox imbalance.

**Suggested GO biological processes:** BMP signaling (**GO:0030509**), TGF-β receptor signaling (**GO:0007179**), angiogenesis (**GO:0001525**), endothelial-cell proliferation (**GO:0001935**), smooth-muscle-cell proliferation (**GO:0048661**), inflammatory response (**GO:0006954**), response to hypoxia (**GO:0001666**), apoptotic process (**GO:0006915**), extracellular-matrix organization (**GO:0030198**), reactive-oxygen-species metabolic process (**GO:0072593**) and ferroptosis (**GO:0097707**).

**Principal Cell Ontology targets:** vascular endothelial cell (**CL:0000115**), smooth-muscle cell (**CL:0000192**), fibroblast (**CL:0000057**), macrophage (**CL:0000235**), monocyte (**CL:0000576**), T cell (**CL:0000084**), natural-killer cell (**CL:0000623**) and dendritic cell (**CL:0000451**).

### Immune, omic and 2024 advances

A 2024 IPAH integrative analysis identified **CXCL9, CCL5, GZMA and GZMK** as inflammation-associated hub genes. Human GEO microarray and scRNA-seq data localized CCL5/GZMA predominantly to T and NK cells interacting with endothelial cells, PASMCs and fibroblasts; Cxcl9, Ccl5 and Gzma were then validated in monocrotaline rats. This is combined human computational/single-cell and animal evidence—not yet a validated clinical target. (li2024anewintegrative pages 1-2)

A 2024 multi-omics study implicated endothelial **ferroptosis** upstream of complement activation, macrophage recruitment and PASMC proliferation. In monocrotaline rats, ferrostatin-1 mitigated disease; AAV1-ACSL4 induction and PAEC/PASMC/monocyte experiments supported causality. Human samples and genetic associations increased relevance, but therapeutic evidence remains preclinical. (kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5)

Transcriptomics, proteomics, metabolomics and spatial profiling collectively show substantial cell-state and lesion heterogeneity. They are discovery platforms rather than validated IPAH diagnostic assays.

## 7. Anatomical structures affected

The primary lesion is bilateral and diffuse within small pulmonary arteries/arterioles—**lung (UBERON:0002048), pulmonary artery (UBERON:0002012), blood-vessel endothelium and vascular wall**. Intimal endothelial cells, medial PASMCs and adventitial fibroblasts are directly affected. Secondary injury involves the **right ventricle (UBERON:0002080)**, right atrium, tricuspid valve, liver and systemic veins through venous congestion. Relevant subcellular compartments include plasma membrane/receptor complexes, nucleus/chromatin, mitochondrion (**GO:0005739**), endoplasmic reticulum and caveolae (**GO:0005901**). Lateralization is not a defining feature.

## 8. Temporal development

Onset ranges from childhood to late adulthood and is typically insidious. Early disease may be detectable only through carrier surveillance or abnormal exercise physiology. Clinical stages are best represented by WHO functional class and multidimensional low/intermediate/high mortality risk rather than a fixed anatomical staging system. Untreated disease is progressive; spontaneous durable remission is exceptional. Treatment can improve risk status and function but usually does not eradicate vascular pathology.

The critical intervention window is before severe RV dysfunction or irreversible obliterative remodeling. Early referral is particularly important for rapidly progressive symptoms, syncope, RV failure, low cardiac output, very high PVR or suspected PVOD.

## 9. Inheritance and population

PAH incidence is approximately **2.5–7.5/million/year** and prevalence **15–50/million**, although estimates vary by ascertainment and geography. (eichstaedt2023geneticcounsellingand pages 1-2) Women are affected more often, while age at diagnosis has increased in modern registries because older patients and patients with comorbidities are increasingly recognized.

No ethnicity is intrinsically exempt. Current genomic cohorts are disproportionately European, limiting ancestry-specific penetrance and allele-frequency estimates; the 2024 genetics task force identifies increased diversity as a priority. (austin2024geneticsandprecision pages 2-3)

For dominant PAH predisposition, a first-degree relative of a heterozygous carrier has a 50% chance of inheriting the variant, but substantially less than 50% lifetime probability of developing disease because penetrance is incomplete. Carrier frequency and penetrance should be reported gene-, variant-, sex-, age- and ancestry-specifically rather than as universal values.

## 10. Diagnostics

### Clinical algorithm

1. **Suspect PH:** unexplained exertional dyspnea, syncope, RV signs, abnormal ECG/chest radiograph or reduced diffusion capacity.
2. **Estimate probability:** transthoracic echocardiography evaluates tricuspid-regurgitation velocity, RV/RA size and function, septal flattening and pericardial effusion.
3. **Characterize and exclude:** ECG, chest radiograph, BNP/NT-proBNP, full blood count/iron studies, chemistry, liver/thyroid tests, HIV and autoimmune serology; pulmonary-function tests with DLCO; arterial oxygen assessment; high-resolution CT; ventilation–perfusion scan to exclude CTEPH; sleep assessment when indicated; and evaluation for portal hypertension and congenital shunts.
4. **Confirm:** expert-center RHC measuring mPAP, PAWP, cardiac output/index, PVR, right-atrial pressure and mixed venous oxygen saturation.
5. **Assign etiology:** IPAH only after Group 2–5 PH and associated/drug-induced PAH have been excluded.

RHC is mandatory for definitive classification. Current precapillary thresholds are mPAP >20 mmHg, PAWP ≤15 mmHg and PVR >2 WU. (eichstaedt2023geneticcounsellingand pages 1-2)

### Vasoreactivity and risk tests

Acute vasoreactivity testing with inhaled nitric oxide, inhaled iloprost or intravenous epoprostenol is recommended for IPAH/HPAH/drug-associated PAH to identify the small calcium-channel-blocker-responsive subgroup. A positive response is conventionally a fall in mPAP by at least 10 mmHg to ≤40 mmHg with unchanged or increased cardiac output.

WHO functional class, 6-minute walk distance and BNP/NT-proBNP are the three noninvasive variables shared across major validated risk tools. RHC and cardiac MRI/echo measures—right-atrial pressure, cardiac index, stroke-volume index, PVR, RV ejection fraction, RV strain and pericardial effusion—add prognostic resolution.

### Histopathology and biomarkers

Pathology may show medial hypertrophy, eccentric/concentric intimal fibrosis, in-situ thrombosis, adventitial inflammation and plexiform lesions. Lung biopsy is generally avoided because of procedural risk and is not needed for routine diagnosis.

No circulating molecule is specific enough to diagnose IPAH. BNP/NT-proBNP is validated for severity and prognosis; troponin, uric acid, renal/liver indices, iron deficiency and emerging proteomic markers are supportive or investigational.

### Genetic diagnosis and screening

Offer pre-test counseling and a comprehensive PAH/PVOD panel with copy-number analysis. Test an affected person first. Confirm familial variants orthogonally where appropriate, then offer targeted cascade testing. Negative panel testing does not exclude genetic susceptibility. RNA sequencing, proteomics, metabolomics, methylation profiling and liquid biopsy remain research tools.

## 11. Outcome and prognosis

Historical untreated median survival was approximately **2.8 years**; contemporary management has extended median survival beyond seven years in some cohorts, but IPAH remains incurable. (dave2023unravelingtheepigenetic pages 1-2) A 2024 population-based systematic review found adult PAH survival ranges of **85–99% at one year, 65–95% at three years and 50–86% at five years**. European pooled estimates were 90%, 78% and 61%, respectively. These PAH-wide figures should not be interpreted as IPAH-only estimates. 

Adverse prognostic factors include older age, male sex, WHO-FC III/IV, syncope, low 6MWD, high BNP/NT-proBNP, high right-atrial pressure/PVR, low cardiac index or mixed venous oxygen saturation, RV dilation/dysfunction, renal or hepatic dysfunction, and failure to reach low-risk status. A 183-patient machine-learning cohort identified age, 6MWD, red-cell distribution width, cardiac index, PVR, NT-proBNP and right-atrial area as a mortality signature, but this requires broader external validation.

Major complications are progressive RV failure, atrial arrhythmia, hemoptysis, thrombosis, sudden death and treatment-related adverse events. Full recovery without ongoing therapy is unusual.

## 12. Treatment

### Risk-based strategy

Treatment should occur at a PH center, aiming for a low-risk profile. General NCIT concepts include **pharmacotherapy, combination therapy, oxygen therapy, exercise rehabilitation, lung transplantation and heart–lung transplantation**; exact NCIT codes should be resolved against the implementation’s NCIT release.

- **True vasoreactive IPAH:** high-dose amlodipine, nifedipine or diltiazem with close reassessment. Calcium-channel blockers are unsafe as empiric PAH therapy without a positive vasoreactivity test.
- **Low/intermediate risk without major cardiopulmonary comorbidity:** initial oral dual therapy, usually an endothelin-receptor antagonist (ambrisentan, bosentan or macitentan) plus a PDE5 inhibitor (sildenafil or tadalafil).
- **High risk:** include parenteral prostacyclin, especially intravenous epoprostenol, within combination therapy and evaluate early for transplantation.
- **Follow-up:** reassess symptoms, WHO-FC, 6MWD, BNP/NT-proBNP and imaging/hemodynamics; sequentially add prostacyclin-pathway therapy, sotatercept or another appropriate class if low risk is not achieved.

### Drug classes

- **Endothelin pathway:** bosentan, ambrisentan, macitentan; adverse effects include edema, anemia, hypotension and class-specific hepatic or teratogenic risk.
- **NO–cGMP pathway:** sildenafil/tadalafil inhibit PDE5; riociguat stimulates soluble guanylate cyclase. Riociguat must not be combined with PDE5 inhibitors because of hypotension.
- **Prostacyclin pathway:** epoprostenol, treprostinil, iloprost and oral selexipag; adverse effects include headache, flushing, jaw pain, diarrhea and hypotension. Parenteral delivery adds catheter infection, thrombosis and abrupt-withdrawal risk.
- **Sotatercept:** an ActRIIA-Fc ligand trap that rebalances activin/BMP signaling. In phase 2 PULSAR, PVR decreased approximately 18%; phase 3 STELLAR (NCT04576988) improved exercise capacity, NT-proBNP, PVR, risk score and time to death/clinical worsening. (jin2023medicalmanagementof pages 16-17) A 24-week STELLAR analysis reported placebo-adjusted changes of mPAP −13.9 mmHg, PVR −254.8 dyn·s·cm⁻⁵, right-atrial pressure −2.7 mmHg and improved RV–pulmonary-arterial coupling. Important monitoring issues include increased hemoglobin, thrombocytopenia, telangiectasia, epistaxis and bleeding.

The mechanistic importance of sotatercept is that it is the first approved PAH therapy directly addressing extracellular TGF-β-superfamily imbalance rather than only vascular tone. Its exact target cells and complete mechanism remain unresolved. (li2024bonemorphogeneticprotein pages 9-11)

### Supportive and interventional care

Use diuretics for congestion, oxygen for documented hypoxemia, iron replacement for deficiency, supervised exercise rehabilitation once stable, vaccination against respiratory infections, pregnancy avoidance/counseling and psychosocial support. Routine anticoagulation in IPAH is controversial and should be individualized. Balloon atrial septostomy may bridge selected refractory patients. Bilateral lung transplantation or heart–lung transplantation is considered for refractory high-risk disease.

### Experimental and active research

Retrieved active studies included long-acting inhaled treprostinil palmitil (**NCT05649748**), early rapid treprostinil with hemodynamic targets (**NCT05203510**), seralutinib/GB002 extension (**NCT04816604**), high-dose macitentan (**NCT04273945**), PF-07868489 (**NCT06137742**) and sotatercept extension studies. These are not equivalent to established indications. No approved gene, cell, CRISPR, ASO or siRNA therapy exists for IPAH.

## 13. Prevention

There is no proven population-level primary prevention because the initiating cause of IPAH is unknown. Practical measures are:

- **Primary:** avoid recognized PAH-associated drugs/toxins; address hypoxia and general cardiovascular risks; provide reproductive counseling to pathogenic-variant carriers.
- **Secondary:** genetic counseling, cascade testing and periodic clinical surveillance of asymptomatic carriers/families; prompt evaluation of unexplained exertional symptoms. There is no newborn or universal population screen.
- **Tertiary:** vaccination, medication adherence, pregnancy prevention, infection and catheter-care education, supervised exercise, oxygen when indicated, iron correction, serial risk assessment and timely transplant referral.

Prenatal or preimplantation genetic testing is technically possible when a familial pathogenic variant is known, but requires non-directive counseling because penetrance and severity are uncertain.

## 14. Other species and natural disease

Spontaneous pulmonary hypertension occurs in dogs, cats, cattle at altitude and other mammals, usually secondary to heart, lung, thromboembolic or hypoxic disease; a rigorously defined natural veterinary analogue of human IPAH is uncommon. There is no zoonotic transmission. Conserved orthologues of BMPR2/BMP/TGF-β, ion-channel and hypoxia pathways enable comparative study, but breed-specific idiopathic PAH and corresponding VBO annotations are insufficiently established for routine knowledge-base assertion.

## 15. Model organisms

- **Monocrotaline rat:** reproducible endothelial injury, inflammation, medial remodeling and RV failure; inexpensive but toxin-driven and does not reproduce the full human plexiform phenotype. It supported the 2024 CCL5 and ferroptosis studies. (li2024anewintegrative pages 1-2, kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5)
- **SU5416 plus hypoxia rat:** severe, partly irreversible angioproliferative PH with plexiform-like lesions; valuable for occlusive remodeling but depends on VEGFR blockade and hypoxia.
- **Chronic-hypoxia mouse/rat:** useful for hypoxic vasoconstriction and muscularization; generally milder and more reversible than human IPAH.
- **Genetic models:** Bmpr2 heterozygous or conditional mutants, Kcnk3, Smad and endothelial developmental-gene models test susceptibility and second hits. A 2024 Bmpr2-mutant rat study showed that pulmonary-artery occlusion produced more severe PH and mortality in mutants, illustrating incomplete penetrance and gene–environment interaction.
- **Zebrafish:** rapid developmental and vascular genetics, especially BMPR2/TBX4/SOX17; limited RV and pulmonary-circulation equivalence.
- **Human systems:** primary PAEC/PASMC cultures, endothelial–smooth-muscle co-culture, patient iPSCs, organoids and precision-cut lung slices permit genotype-specific studies but lack full immune, flow and RV–lung interactions.

No single model reproduces genetic heterogeneity, female susceptibility, plexiform pathology, chronic RV adaptation and treatment response simultaneously. Convergent findings across human tissue, multiple models and orthogonal assays should therefore receive the highest evidentiary weight.

## Evidence limitations and authoritative interpretation

The modern expert view is that IPAH is a heterogeneous endpoint rather than one molecular disease. Genetics can reveal previously hidden heritable disease; single-cell studies expose lesion- and cell-state heterogeneity; and sotatercept validates TGF-β-superfamily imbalance therapeutically. Nevertheless, gene penetrance, ancestry-specific risk, environmental triggers, longitudinal QoL, pediatric outcomes, and clinically actionable omic biomarkers remain incompletely characterized. The strongest current clinical evidence comes from expert-center RHC cohorts, international genetic consensus, randomized PAH trials and registries; animal or computational findings should not be promoted to clinical facts without prospective human validation.

### Key recent sources and publication dates

- Austin et al., **“Genetics and precision genomics approaches to pulmonary hypertension,”** *European Respiratory Journal*, August 2024. DOI/URL: https://doi.org/10.1183/13993003.01370-2024. (austin2024geneticsandprecision pages 2-3)
- Li & Quigley, **“Bone morphogenetic protein signalling in pulmonary arterial hypertension,”** *Biochemical Society Transactions*, May 2024. DOI/URL: https://doi.org/10.1042/BST20231547. (li2024bonemorphogeneticprotein pages 9-11)
- Li et al., **IPAH CCL5 single-cell analysis**, *Journal of Translational Medicine*, May 2024. DOI/URL: https://doi.org/10.1186/s12967-024-05304-6. (li2024anewintegrative pages 1-2)
- Kazmirczak et al., **“Ferroptosis-Mediated Inflammation Promotes Pulmonary Hypertension,”** *Circulation Research*, November 2024. DOI/URL: https://doi.org/10.1161/CIRCRESAHA.123.324138. (kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5)
- Eichstaedt et al., **genetic-counseling consensus**, *European Respiratory Journal*, 2023. DOI/URL: https://doi.org/10.1183/13993003.01471-2022. (eichstaedt2023geneticcounsellingand pages 1-2)
- Jin et al., **medical management and investigational drugs**, *Pharmaceutics*, May 2023. DOI/URL: https://doi.org/10.3390/pharmaceutics15061579. (jin2023medicalmanagementof pages 16-17)

**Exact source language supporting central claims:** the 2023 consensus describes PAH as a disorder involving “pulmonary microvascular obliteration” and identifies “fatigue, dyspnea on exertion, chest pain, syncope” as common presentations. The 2024 single-cell study concluded that T and NK cells drove heightened inflammation “predominantly via the upregulation of CCL5,” while the 2024 ferroptosis study concluded that “ferroptosis promotes PAH through metabolic and inflammatory mechanisms in the pulmonary vasculature.” (eichstaedt2023geneticcounsellingand pages 1-2, li2024anewintegrative pages 1-2, kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5)

References

1. (eichstaedt2023geneticcounsellingand pages 1-2): Christina A. Eichstaedt, Catharina Belge, Wendy K. Chung, Stefan Gräf, Ekkehard Grünig, David Montani, Rozenn Quarck, Jair A. Tenorio-Castano, Florent Soubrier, Richard C. Trembath, and Nicholas W. Morrell. Genetic counselling and testing in pulmonary arterial hypertension: a consensus statement on behalf of the international consortium for genetic studies in pah. The European Respiratory Journal, 61:2201471, Oct 2023. URL: https://doi.org/10.1183/13993003.01471-2022, doi:10.1183/13993003.01471-2022. This article has 76 citations.

2. (austin2024geneticsandprecision pages 2-3): Eric D. Austin, Micheala A. Aldred, Mona Alotaibi, Stefan Gräf, William C. Nichols, Richard C. Trembath, and Wendy K. Chung. Genetics and precision genomics approaches to pulmonary hypertension. The European Respiratory Journal, 64:2401370, Aug 2024. URL: https://doi.org/10.1183/13993003.01370-2024, doi:10.1183/13993003.01370-2024. This article has 68 citations.

3. (li2024bonemorphogeneticprotein pages 9-11): Wei Li and Kate Quigley. Bone morphogenetic protein signalling in pulmonary arterial hypertension: revisiting the bmprii connection. Biochemical Society Transactions, 52:1515-1528, May 2024. URL: https://doi.org/10.1042/bst20231547, doi:10.1042/bst20231547. This article has 30 citations and is from a peer-reviewed journal.

4. (li2024anewintegrative pages 1-2): Xincheng Li, Shuangshuang Ma, Qi Wang, Yishan Li, Xiaofan Ji, Jixiang Liu, Jing Ma, Yongbing Wang, Zhu Zhang, Hong Zhang, Hong Chen, Linfeng Xi, Yunxia Zhang, Wanmu Xie, Lu Sun, Zhihui Fu, Peiran Yang, Chen Wang, and Zhenguo Zhai. A new integrative analysis of histopathology and single cell rna-seq reveals the ccl5 mediated t and nk cell interaction with vascular cells in idiopathic pulmonary arterial hypertension. Journal of Translational Medicine, May 2024. URL: https://doi.org/10.1186/s12967-024-05304-6, doi:10.1186/s12967-024-05304-6. This article has 18 citations and is from a peer-reviewed journal.

5. (kazmirczak2024ferroptosismediatedinflammationpromotes pages 3-5): Felipe Kazmirczak, Neal T. Vogel, Sasha Z. Prisco, Michael T. Patterson, Jeffrey Annis, Ryan T. Moon, Lynn M. Hartweck, Jenna B. Mendelson, Minwoo Kim, Natalia Calixto Mancipe, Todd Markowski, LeeAnn Higgins, Candace Guerrero, Ben Kremer, Madelyn L. Blake, Christopher J. Rhodes, Jesse W. Williams, Evan L. Brittain, and Kurt W. Prins. Ferroptosis-mediated inflammation promotes pulmonary hypertension. Circulation Research, 135:1067-1083, Nov 2024. URL: https://doi.org/10.1161/circresaha.123.324138, doi:10.1161/circresaha.123.324138. This article has 90 citations and is from a highest quality peer-reviewed journal.

6. (dave2023unravelingtheepigenetic pages 1-2): Jaydev Dave, Vineeta Jagana, Radoslav Janostiak, and Malik Bisserier. Unraveling the epigenetic landscape of pulmonary arterial hypertension: implications for personalized medicine development. Journal of Translational Medicine, Jul 2023. URL: https://doi.org/10.1186/s12967-023-04339-5, doi:10.1186/s12967-023-04339-5. This article has 52 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: idiopathic pulmonary arterial hypertension): Open Targets Query (idiopathic pulmonary arterial hypertension, 35 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (mocumbi2024pulmonaryhypertension pages 17-17): Ana Mocumbi, Marc Humbert, Anita Saxena, Zhi-Cheng Jing, Karen Sliwa, Friedrich Thienemann, Stephen L. Archer, and Simon Stewart. Pulmonary hypertension. Jan 2024. URL: https://doi.org/10.1038/s41572-023-00486-7, doi:10.1038/s41572-023-00486-7. This article has 445 citations.

9. (jin2023medicalmanagementof pages 16-17): Qi Jin, Dandan Chen, Xiaochun Zhang, Feng Zhang, Dongxiang Zhong, Dawei Lin, Lihua Guan, Wenzhi Pan, Daxin Zhou, and Junbo Ge. Medical management of pulmonary arterial hypertension: current approaches and investigational drugs. Pharmaceutics, 15:1579, May 2023. URL: https://doi.org/10.3390/pharmaceutics15061579, doi:10.3390/pharmaceutics15061579. This article has 22 citations.

10. (eichstaedt2023geneticcounsellingand pages 13-14): Christina A. Eichstaedt, Catharina Belge, Wendy K. Chung, Stefan Gräf, Ekkehard Grünig, David Montani, Rozenn Quarck, Jair A. Tenorio-Castano, Florent Soubrier, Richard C. Trembath, and Nicholas W. Morrell. Genetic counselling and testing in pulmonary arterial hypertension: a consensus statement on behalf of the international consortium for genetic studies in pah. The European Respiratory Journal, 61:2201471, Oct 2023. URL: https://doi.org/10.1183/13993003.01471-2022, doi:10.1183/13993003.01471-2022. This article has 76 citations.

## Artifacts

- [Edison artifact artifact-00](Idiopathic_Pulmonary_Arterial_Hypertension-deep-research-falcon_artifacts/artifact-00.md)