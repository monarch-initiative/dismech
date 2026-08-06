---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T11:47:27.657418'
end_time: '2026-08-01T11:55:33.400998'
duration_seconds: 485.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: GRIN2A-Related Epileptic Encephalopathy and Intellectual Disability
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: GRIN2A-Related_Epileptic_Encephalopathy_and_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GRIN2A-Related Epileptic Encephalopathy and Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GRIN2A-Related Epileptic Encephalopathy and Intellectual Disability** covering all of the
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
- **Disease Name:** GRIN2A-Related Epileptic Encephalopathy and Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GRIN2A-Related Epileptic Encephalopathy and Intellectual Disability** covering all of the
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


# GRIN2A-Related Epileptic Encephalopathy and Intellectual Disability

## Executive summary

**GRIN2A-related disorder** is an autosomal-dominant, variably penetrant neurodevelopmental synaptopathy caused by pathogenic variants in **GRIN2A**, which encodes the GluN2A subunit of the NMDA-type ionotropic glutamate receptor. It is better regarded as a spectrum than as one narrowly defined syndrome. Manifestations range from self-limited childhood focal epilepsy with speech dyspraxia to Landau–Kleffner syndrome, developmental/epileptic encephalopathy with spike-wave activation in sleep (D/EE-SWAS), severe intellectual disability, and early-onset developmental and epileptic encephalopathy. The largest aggregated study comprised 248 individuals and found epilepsy and speech disorder in more than 80% and intellectual disability/developmental impairment in 62.7%. Variant location and functional effect are major determinants of severity. Transmembrane/linker missense variants are usually de novo, frequently gain-of-function (GoF), and associated with severe disease; amino-terminal/ligand-binding-domain missense and protein-null variants more often cause loss-of-function (LoF) and milder epilepsy–aphasia phenotypes. This distinction is clinically important because proposed precision therapies act in opposite directions. (strehlow2019grin2arelateddisordersgenotype pages 1-1, strehlow2019grin2arelateddisordersgenotype pages 11-11)

The compact knowledge-base mapping below summarizes major findings and ontology suggestions.

| Domain | Core finding/statistic | Suggested ontology terms | Evidence type/source |
|---|---|---|---|
| Disease identity | GRIN2A-related disorder spans mild focal epilepsy/speech disorder to severe developmental and epileptic encephalopathy within the epilepsy-aphasia spectrum; largest aggregated cohort included 248 affected individuals. Orphanet entry referenced as 289266 in trial registry material. (strehlow2019grin2arelateddisordersgenotype pages 1-1, NCT04646447 chunk 1) | MONDO: GRIN2A-related disorder (if mapped); Orphanet: 289266; HP:0001250 Seizure; HP:0000750 Delayed speech and language development | Human aggregated cohort; trial registry background (Brain 2019; ClinicalTrials.gov) |
| Gene/protein | Causal gene is **GRIN2A** encoding GluN2A, an NMDA receptor subunit; pathogenic variation affects receptor function, trafficking, and localization. (vieira2024aframeshiftvariant pages 1-2, tumdam2024nmdareceptorsin pages 4-6) | HGNC: GRIN2A; NCBI Gene: GRIN2A; UniProt: GluN2A; GO:0004972 NMDA glutamate receptor activity | Human molecular genetics; review/in vitro mechanistic synthesis |
| Epilepsy/EEG | In the 2019 cohort, 27/219 (12.3%) had no seizures; among 152 with EEG, 143/152 (94.1%) had epileptiform discharges, including centrotemporal spikes (34), multifocal discharges (28), and CSWS/SWAS (51). (strehlow2019grin2arelateddisordersgenotype pages 6-7) | HP:0001250 Seizure; HP:0011175 Focal-onset seizure; HP:0010848 Abnormality of EEG; HP:0011185 Centrotemporal spike waves; HP:0011187 Continuous spike-wave during slow-wave sleep | Human cohort (Brain 2019) |
| Speech-language | Speech disorder was the dominant phenotype: 129/140 (92.1%) had impairment; reported subgroups included moderate dysarthria/dyspraxia (55), aphasia with speech loss (26), delayed speech development (26), and temporary regression (8). (strehlow2019grin2arelateddisordersgenotype pages 6-7) | HP:0000750 Delayed speech and language development; HP:0002167 Dysarthria; HP:0002376 Developmental regression; HP:0031988 Aphasia | Human cohort |
| ID/development | Intellectual disability/developmental delay present in 62.7% overall; severity ranged from none to profound, with misTMD+linker variants associated with markedly greater severity than misATD+LBD variants. (strehlow2019grin2arelateddisordersgenotype pages 11-11, strehlow2019grin2arelateddisordersgenotype pages 6-7) | HP:0001249 Intellectual disability; HP:0011342 Developmental delay; HP:0010864 Global developmental delay | Human cohort with genotype-phenotype analysis |
| Motor/behavior | Hypotonia in 40/139 (28.8%); movement disorders in 19/72 (26.4%), including ataxic/dystonic/spastic/choreatic features; neuropsychiatric comorbidity in 17/70 (24.3%), including ADHD (6), autism (6), schizophrenia (2), anxiety (1). (strehlow2019grin2arelateddisordersgenotype pages 6-7) | HP:0001252 Hypotonia; HP:0001251 Ataxia; HP:0001332 Dystonia; HP:0002317 Unsteady gait/ataxia-related; HP:0007018 Attention deficit hyperactivity disorder; HP:0000717 Autism | Human cohort |
| Anatomy | Imaging abnormalities were reported in 12/85 (14.1%) in the human cohort; mouse knockout imaging showed transient abnormalities in neocortex, corpus callosum, hippocampus, and thalamus, strongest around postnatal day 30. (strehlow2019grin2arelateddisordersgenotype pages 6-7, salmi2018transientmicrostructuralbrain pages 1-2) | UBERON:0000955 brain; UBERON:0001950 cerebral cortex/neocortex; UBERON:0000956 corpus callosum; UBERON:0002421 hippocampus; UBERON:0001897 thalamus | Human cohort; mouse MRI/DTI model |
| Mechanism (GoF/LoF) | Variant class/domain predicts function and phenotype: missense variants in transmembrane/linker regions are associated with severe developmental phenotypes and NMDAR gain-of-function; missense variants in ATD/LBD and null variants more often associate with NMDAR loss-of-function and milder developmental phenotypes. Severe GoF can also result from specific missense variants such as L812M. (strehlow2019grin2arelateddisordersgenotype pages 1-1, strehlow2019grin2arelateddisordersgenotype pages 3-3) | GO:0004972 NMDA glutamate receptor activity; GO:0050890 cognition/synaptic signaling-related; SO:0001583 missense_variant; SO:0001587 stop_gained; SO:0001909 frameshift_variant | Human cohort integrated with electrophysiology; case functional study |
| Protein/trafficking dysfunction | A de novo **P1199Rfs*32** frameshift truncating the GluN2A CTD caused impaired PSD-95 binding, preserved Scribble1 interaction, increased extrasynaptic expression, fewer synapses, decreased spine density, and was interpreted as loss-of-function. (vieira2024aframeshiftvariant pages 1-2) | GO:0098978 glutamatergic synapse; GO:0043197 dendritic spine; GO:0006897 endocytosis/recycling trafficking; HP:0001250 Seizure | Human case plus heterologous-cell and rat-neuron in vitro study |
| Diagnosis | Recommended diagnosis is molecular: pathogenic/likely pathogenic **GRIN2A** variant in an individual with epilepsy, sleep-activated epileptiform EEG/SWAS, speech-language disorder, and/or developmental impairment; functional annotation is important because treatment direction differs for GoF vs LoF variants. (strehlow2019grin2arelateddisordersgenotype pages 11-11, krey2022lserinetreatmentis pages 1-2) | NCIT: Genetic Testing; HP:0010848 Abnormality of EEG; HP:0000750 Delayed speech and language development | Human cohort; retrospective treatment series |
| Inheritance | Unlike several other GRIN-associated disorders, inherited variants are common: 60.2% of GRIN2A variants were inherited overall; all 32 misTMD+linker variants were de novo, while 18/47 misATD+LBD variants were de novo. Apparent penetrance is incomplete, with only three individuals reported as apparently normal. (strehlow2019grin2arelateddisordersgenotype pages 11-11, strehlow2019grin2arelateddisordersgenotype pages 6-7) | HP:0000006 Autosomal dominant inheritance; HP:0003829 Variable expressivity; HP:0003828 Reduced penetrance | Human cohort |
| Temporal course | EAS/GRIN2A phenotypes are age-dependent childhood disorders; in mouse knockout, structural abnormalities were transient and most evident at ~1 month, paralleling the childhood onset and variable adolescent outcome described for EAS. (salmi2018transientmicrostructuralbrain pages 1-2) | HP:0011463 Childhood onset; HP:0002376 Developmental regression; HP:0012378 Episodic course | Mouse model with human syndrome framing |
| Recent SWAS relevance | In a 2024 D/EE-SWAS study, genetic etiology was found in 31/91 (34%) of the core cohort; GRIN genes are part of the etiologic landscape of SWAS disorders, reinforcing GRIN2A testing in relevant EEG-language-regression phenotypes. (viswanathan2024solvingtheetiology pages 1-3) | HP:0011187 Continuous spike-wave during slow-wave sleep; HP:0001288 Aphasia; HP:0001249 Intellectual disability | Human 2024 syndrome cohort |
| Treatment | Precision treatment remains experimental and mechanism-dependent. In a 10-patient retrospective GRIN2A/GRIN2B series, among 9 LoF/null cases, L-serine was associated with improvement in behavior in 8/9 (89%), development in 4/9 (44%), and EEG or seizure frequency in 4/9 (44%); no side effects were reported in these 9. A GoF case worsened transiently with L-serine. (krey2022lserinetreatmentis pages 1-2) | NCIT:C61742 Serine; NCIT:Anticonvulsant Therapy; HP:0010848 Abnormality of EEG | Human retrospective n-of-1/case-series evidence |
| Clinical trials | **NCT04646447**: L-serine in GRIN-related encephalopathy, interventional single-group, estimated enrollment 20, last known recruiting, focused on LoF variants. **NCT05818943** Honeycomb: radiprodil (NR2B negative allosteric modulator), phase 1, open-label, active not recruiting, estimated enrollment 24, for pediatric GoF GRIN-related disorder. (NCT04646447 chunk 1, NCT05818943 chunk 1, NCT05818943 chunk 2) | NCIT:C61742 Serine; NCIT:C000626801 radiprodil; NCIT:Clinical Trial | Trial registry |
| Animal/cellular models | **Grin2a KO mouse**: transient microstructural brain anomalies and epileptiform discharges in third postnatal week. **Grin2a N615S mouse**: voltage-independent Ca2+ signaling caused audiogenic seizures, exploratory hyperactivity, attentional/cognitive abnormalities, and altered hippocampal activity. **Rat primary neurons/heterologous cells**: P1199Rfs*32 caused trafficking/synaptic defects. (salmi2018transientmicrostructuralbrain pages 1-2, bertocchi2021voltageindependentglun2atypenmda pages 1-2, vieira2024aframeshiftvariant pages 1-2) | MGI:Grin2a; GO:0007611 learning or memory; GO:0051930 regulation of sensory perception; CL:0000540 neuron | Mouse model; in vitro neuronal/cell-system evidence |
| Major evidence gaps | No robust prevalence/incidence estimates specific to GRIN2A-related epileptic encephalopathy/ID were identified; no standardized diagnostic criteria unique to GRIN2A disorder; no approved disease-modifying therapy; treatment evidence remains small, retrospective, and mechanism-stratified; limited data on biomarkers, long-term prognosis, and protective/environmental modifiers. (strehlow2019grin2arelateddisordersgenotype pages 11-11, krey2022lserinetreatmentis pages 1-2, NCT04646447 chunk 1, NCT05818943 chunk 1) | NCIT:Evidence Gap; HP:0000007 Autosomal dominant; GO:0007268 synaptic transmission | Evidence synthesis across cohort, case series, and trial registries |


*Table: This table maps the main disease-characteristic domains for GRIN2A-related epileptic encephalopathy/intellectual disability to concise evidence-backed findings and suggested ontology terms. It is designed as a compact knowledge-base scaffold that distinguishes cohort, mechanistic, model, and trial-registry evidence.*

## 1. Disease information

### Definition and scope

GRIN2A-related disorder is a monogenic disorder of glutamatergic neurotransmission. The historical clinical center of gravity is the **epilepsy–aphasia spectrum (EAS)**, including epilepsy with centrotemporal spikes, atypical childhood epilepsy with centrotemporal spikes, Landau–Kleffner syndrome, and continuous spike-wave during sleep/SWAS. Severe cases qualify as developmental and epileptic encephalopathy, because both the underlying molecular defect and epileptiform activity impair development. EAS is described as an age-dependent childhood disorder with sleep-activated discharges, often infrequent seizures, and language, cognitive, or behavioral deficits. (strehlow2019grin2arelateddisordersgenotype pages 6-7, salmi2018transientmicrostructuralbrain pages 1-2)

The 2022 ILAE framework distinguishes **DEE-SWAS**, in which developmental impairment predates SWAS, from **EE-SWAS**, in which development was previously normal and regression or plateauing accompanies SWAS. Developmental sequelae may persist after seizures and SWAS remit. (viswanathan2024solvingtheetiology pages 1-3)

### Identifiers and synonyms

* **Gene:** GRIN2A; gene-level OMIM identifier **OMIM 138253** is stated in the trial registry. (NCT04646447 chunk 1)
* **Orphanet:** **ORPHA:289266**, cited for GRIN2A-related encephalopathy in the registry. (NCT04646447 chunk 1)
* **MONDO:** a single confidently verified MONDO identifier was not recovered from the available literature; the knowledge base should map at the broader “GRIN2A-related disorder” level and retain syndrome-level child terms where available.
* **OMIM phenotype:** GRIN2A is historically associated with focal epilepsy with speech disorder, with or without intellectual disability; the exact current phenotype-record number should be verified directly in OMIM before database deposition.
* **ICD-10/ICD-11 and MeSH:** there is no specific GRIN2A code. Cases are coded under genetic/developmental and epileptic encephalopathy, focal epilepsy, Landau–Kleffner syndrome, intellectual disability, and speech/language disorder as clinically appropriate.
* **Synonyms:** GRIN2A-related neurodevelopmental disorder; GRIN2A-related epilepsy; GRIN2A-related epilepsy–aphasia spectrum; focal epilepsy with speech disorder with or without intellectual disability; GRIN2A encephalopathy; GRIN2A-related D/EE-SWAS.

The evidence base is predominantly **aggregated disease-level research cohorts, literature-ascertained cases, laboratory functional studies, and registries**, rather than routine EHR-derived population surveillance. The landmark cohort combined 92 new cases with 156 published individuals. (strehlow2019grin2arelateddisordersgenotype pages 1-1)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is a heterozygous germline pathogenic or likely pathogenic **GRIN2A** variant. Relevant classes include missense, nonsense, frameshift, splice-altering variants, exon/multiexon deletions, and larger deletions involving GRIN2A. Variants may be de novo or inherited from an affected, mildly affected, or apparently unaffected parent. In the largest cohort, 60.2% were inherited, while all 32 assessed transmembrane/linker missense variants were de novo; 18/47 amino-terminal/ligand-binding-domain missense variants were de novo. (strehlow2019grin2arelateddisordersgenotype pages 11-11, strehlow2019grin2arelateddisordersgenotype pages 6-7)

### Risk factors and modifiers

* **Genetic:** variant domain and functional direction are the strongest established severity predictors. Severe GoF changes cluster around transmembrane/linker/pore regions; null and ATD/LBD LoF variants generally have milder average developmental effects, although exceptions occur. (strehlow2019grin2arelateddisordersgenotype pages 1-1)
* **Epileptiform activity during development:** sleep-activated discharges/SWAS are plausibly secondary contributors to language and cognitive regression. This is an interaction between an upstream genetic synaptopathy and a developmentally timed network insult, not a conventional environmental exposure. (salmi2018transientmicrostructuralbrain pages 1-2, viswanathan2024solvingtheetiology pages 1-3)
* **Family history:** relevant because inherited variants are common and expression may be mild or apparently absent. (strehlow2019grin2arelateddisordersgenotype pages 11-11)
* **Sex, ancestry, lifestyle, toxins, occupation, diet, or infectious exposure:** no replicated disease-specific risk association was identified.

No validated **protective allele**, modifier gene, environmental protective factor, or conventional gene–environment interaction has been established. Avoid inferring protection from the presence of mildly affected carriers; that may reflect reduced penetrance, variant effect, ascertainment, polygenic background, or unmeasured modifiers.

## 3. Phenotypes

### Core clinical frequencies

In the 2019 aggregate cohort, 27/219 individuals with available data (12.3%) had no seizures. EEG was abnormal in 143/152 (94.1%): 34 had centrotemporal spikes, 28 multifocal discharges, and 51 continuous spike-wave during sleep. Speech disorder occurred in 129/140 (92.1%): moderate dysarthria/dyspraxia in 55, aphasia with speech loss in 26, delayed speech in 26, and temporary regression in 8; only 11 had normal speech. Intellectual disability/developmental impairment affected 62.7%, with severity from mild to profound. (strehlow2019grin2arelateddisordersgenotype pages 11-11, strehlow2019grin2arelateddisordersgenotype pages 6-7)

Other reported findings were hypotonia in 40/139 (28.8%), movement disorder in 19/72 (26.4%), neuropsychiatric comorbidity in 17/70 (24.3%), and MRI abnormalities in 12/85 (14.1%). The neuropsychiatric subset included ADHD (6), autism (6), schizophrenia (2), and anxiety (1); movement findings included ataxic, dystonic, spastic, and choreatic abnormalities. (strehlow2019grin2arelateddisordersgenotype pages 6-7)

### Phenotype annotations

* **Seizures:** focal, multifocal, generalized, and mixed seizure types; severity ranges from infrequent childhood seizures to drug-resistant DEE. Suggested HPO: **HP:0001250 Seizure**, **HP:0011175 Focal-onset seizure**.
* **Sleep-activated epileptiform EEG:** centrotemporal spikes, multifocal discharges, CSWS/SWAS. Suggested HPO: **HP:0010848 Abnormality of EEG**, **HP:0011187 Continuous spike-wave during slow-wave sleep**.
* **Speech/language disorder:** delayed language, verbal dyspraxia, dysarthria, aphasia, acquired language loss, or transient regression. Suggested HPO: **HP:0000750 Delayed speech and language development**, **HP:0002167 Dysarthria**, **HP:0002376 Developmental regression**, aphasia term as locally mapped.
* **Developmental delay/ID:** variable from normal cognition to profound ID. Suggested HPO: **HP:0011342 Developmental delay**, **HP:0010864 Global developmental delay**, **HP:0001249 Intellectual disability**.
* **Motor findings:** hypotonia, dyspraxia, ataxia, dystonia, spasticity, choreiform movement. Suggested HPO: **HP:0001252 Hypotonia**, **HP:0001251 Ataxia**, **HP:0001332 Dystonia**, plus phenotype-specific terms.
* **Behavior/psychiatry:** ADHD, autism, anxiety, aggression, and occasionally psychosis/schizophrenia. Suggested HPO: **HP:0007018 ADHD**, **HP:0000717 Autism**, **HP:0000739 Anxiety**.

Quality-of-life effects have not been quantified with a GRIN2A-specific validated instrument. Clinically, aphasia, cognitive disability, seizures, motor impairment, disturbed sleep, and behavioral dysregulation impair education, communication, independence, family functioning, and caregiver well-being. PedsQL and caregiver burden are outcomes in the ongoing radiprodil program, but no completed GRIN2A-specific estimates were recovered. (NCT05818943 chunk 1, NCT05818943 chunk 2)

## 4. Genetic and molecular information

**GRIN2A** encodes GluN2A, a component of heterotetrameric NMDA receptors, typically assembled with two obligatory GluN1 subunits and GluN2/GluN3 subunits. GluN2A-containing receptors are prominent in forebrain excitatory synapses and have developmentally regulated expression. (vieira2024aframeshiftvariant pages 1-2)

### Variant interpretation

Pathogenicity assessment should combine ACMG/AMP evidence with inheritance, population rarity, constraint, domain, phenotype, and—where feasible—functional testing. Pathogenic variants causing severe disease are generally absent or extremely rare in population databases; a universal allele-frequency threshold cannot substitute for variant-specific curation. Disease-causing variants are normally germline. Somatic mosaicism is possible in neurodevelopmental genetics but is not established as a major GRIN2A mechanism in the retrieved cohort.

Functional classes include:

1. **Haploinsufficiency/null LoF:** nonsense, frameshift, splice, and deletions reduce functional GluN2A dosage.
2. **Missense LoF:** altered agonist sensitivity, reduced current, impaired surface/synaptic localization, or defective trafficking.
3. **Missense GoF:** increased agonist potency/open probability, reduced magnesium/proton/zinc inhibition, prolonged responses, or excess current.
4. **Mixed/complex effects:** trafficking and channel-gating effects may coexist; “null equals simple hypofunction” and “missense equals GoF” are unsafe assumptions.

The cohort-level correlation was explicit: transmembrane/linker missense variants were associated with severe developmental phenotypes and GoF, whereas ATD/LBD missense and null variants were associated on average with LoF and milder phenotypes. (strehlow2019grin2arelateddisordersgenotype pages 1-1, strehlow2019grin2arelateddisordersgenotype pages 6-7)

A mechanistically informative 2024 study examined de novo **GluN2A p.P1199Rfs*32**, which truncates approximately half the C-terminal domain. The authors reported increased extrasynaptic receptor localization, impaired PSD-95 binding, retained Scribble1-mediated recycling, fewer synapses, and decreased dendritic-spine density. Their abstract concludes: **“Overall, our data show that GluN2A P1199Rfs*32 is a loss-of-function variant with altered membrane localization in neurons.”** (vieira2024aframeshiftvariant pages 1-2)

No validated GRIN2A modifier gene or reproducible disease-specific epigenetic signature is established. Large deletions/CNVs involving GRIN2A can cause disease, but karyotype-level aneuploidy, balanced translocation, repeat expansion, and mitochondrial mechanisms are not characteristic.

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, occupation, smoking, alcohol, diet, exercise, or infectious agents cause the Mendelian disorder. Fever, sleep deprivation, illness, or medication nonadherence may trigger seizures in susceptible individuals, as in epilepsy generally, but this is not equivalent to causing GRIN2A disease. Lifestyle measures support seizure safety and general health but do not reverse the genotype.

## 6. Mechanism and pathophysiology

### Upstream-to-downstream causal chain

1. **Upstream trigger:** pathogenic GRIN2A variant.
2. **Protein effect:** altered GluN2A abundance, folding, gating, magnesium block, agonist sensitivity, intracellular interactions, recycling, or synaptic targeting.
3. **Receptor effect:** NMDA-receptor hypo- or hyperfunction and disturbed Ca²⁺/Na⁺ influx.
4. **Synaptic effect:** abnormal coincidence detection, excitatory transmission, long-term potentiation, dendritic-spine maintenance, synapse formation, and activity-dependent gene regulation.
5. **Circuit effect:** disturbed excitatory–inhibitory balance and maturation of cortical/thalamocortical, hippocampal, language, attention, and sensory circuits.
6. **Clinical effect:** seizures and sleep-activated epileptiform activity, language delay/regression, ID, behavior abnormalities, and movement dysfunction. Recurrent epileptiform activity can then become a downstream amplifier of developmental impairment.

NMDAR activation normally requires glutamate plus a co-agonist and postsynaptic depolarization sufficient to relieve the magnesium pore block. Resulting calcium influx activates signaling underlying synaptic plasticity, dendritic organization, and gene regulation. Disease variants can cause either receptor hypofunction or hyperfunction, explaining why both insufficient and excessive glutamatergic signaling produce epilepsy and developmental disability. (tumdam2024nmdareceptorsin pages 4-6)

The p.P1199Rfs*32 work provides a trafficking-to-phenotype chain: CTD truncation → loss of PSD-95 interactions with preserved Scribble1 recycling → excess extrasynaptic relative to synaptic localization → reduced spine/synapse density → compromised synaptic transmission → epilepsy, aphasia, and behavioral/developmental disease. This evidence combines one human case with heterologous cells and rat primary neurons; it is not a clinical cohort. (vieira2024aframeshiftvariant pages 1-2)

Suggested terms include **GO:0004972 NMDA glutamate receptor activity**, **GO:0035249 synaptic transmission, glutamatergic**, **GO:0098978 glutamatergic synapse**, **GO:0043197 dendritic spine**, **GO:0007611 learning or memory**, **CL:0000540 neuron**, excitatory-neuron and cortical-pyramidal-neuron child terms where supported.

No replicated GRIN2A-specific metabolomic, lipidomic, immune, inflammatory, or tissue-necrosis signature is established. The biochemical abnormality is receptor/channel dysfunction, not an enzyme deficiency. Patient single-cell or spatial-transcriptomic atlases and systematic multi-omics studies remain major gaps.

## 7. Anatomical structures affected

The primary organ is the **central nervous system**, particularly cortical and thalamocortical networks responsible for language and sleep-activated epileptiform synchronization, plus hippocampal circuits involved in memory. Suggested UBERON terms include **UBERON:0000955 brain**, cerebral cortex/neocortex, **UBERON:0000956 corpus callosum**, **UBERON:0002421 hippocampus**, and **UBERON:0001897 thalamus**.

Routine MRI is often normal; abnormalities were reported in only 12/85 individuals in the aggregate cohort. (strehlow2019grin2arelateddisordersgenotype pages 6-7) Grin2a-knockout mouse diffusion imaging showed transient microstructural abnormalities in neocortex, corpus callosum, hippocampus, and thalamus, strongest at postnatal day 30. (salmi2018transientmicrostructuralbrain pages 1-2) There is no consistent lateralization, peripheral-organ pathology, or characteristic biopsy finding.

At the cellular/subcellular level, the principal sites are excitatory postsynaptic membranes, postsynaptic density, dendritic spines, and extrasynaptic neuronal membrane. Suggested GO cellular-component terms include glutamatergic synapse, postsynaptic density, dendritic spine, and plasma membrane.

## 8. Temporal development

Onset is usually pediatric and often follows apparently normal early development in classic EAS. Seizures and sleep-activated discharges emerge during childhood; language delay may precede seizures, whereas acquired aphasia or broader regression may coincide with increasing sleep epileptiform activity. Severe GoF variants can cause much earlier DEE.

Course is variable and lifelong at the genetic level. Seizures and SWAS may remit with age, but speech, cognitive, behavioral, or motor sequelae can persist. The 2024 SWAS cohort found that DEE-SWAS was associated with longer epilepsy duration and poorer intellectual outcome than EE-SWAS. (viswanathan2024solvingtheetiology pages 1-3)

The Grin2a-knockout mouse recapitulates developmental timing: epileptiform discharges appeared in the third postnatal week and MRI abnormalities peaked at approximately one month before becoming less evident later. The authors interpreted this as evidence for early maturation abnormalities in neocortical and thalamocortical systems. (salmi2018transientmicrostructuralbrain pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with both de novo and inherited variants. Expressivity is strikingly variable. Apparent penetrance is incomplete: only three individuals in the aggregate cohort were described as apparently normal, but subtle language, EEG, psychiatric, or learning phenotypes may be missed. (strehlow2019grin2arelateddisordersgenotype pages 11-11)

Parental testing is essential. A clinically unaffected parent carrying the variant changes recurrence risk substantially. Germline mosaicism remains possible even after apparently de novo occurrence, so recurrence risk is above population baseline. There is no anticipation mechanism, established founder effect, consanguinity dependence, or meaningful “carrier frequency” analogous to a recessive disorder.

Robust incidence and prevalence per 100,000 are unavailable. One study noted that GRIN2A defects had been identified in up to 20% of selected EAS patients/families; this is an **etiologic fraction in an enriched phenotype**, not population prevalence. (salmi2018transientmicrostructuralbrain pages 1-2) Another study stated that monogenic GRIN2A variants account for more than 5% of rolandic epilepsy cases, again not general-population prevalence. No reproducible sex, ethnic, or geographic enrichment is established.

## 10. Diagnostics

### Clinical evaluation

Diagnosis should be considered in a child with focal or mixed epilepsy plus speech dyspraxia/dysarthria, delayed language, acquired aphasia, intellectual disability, or regression—especially when EEG shows centrotemporal spikes, multifocal discharges, or marked activation in non-REM sleep.

Recommended evaluation includes:

* detailed seizure and developmental history, three-generation pedigree, and dysmorphology/neurologic examination;
* prolonged EEG including adequate non-REM sleep; video-EEG where seizure classification is uncertain;
* formal speech-language, neuropsychological, motor, behavioral, and autism/ADHD assessment;
* brain MRI to exclude structural etiologies, despite frequently normal imaging;
* hearing evaluation in language regression and targeted metabolic/infectious testing only where clinically indicated.

There is no diagnostic blood, urine, CSF, protein, or metabolite biomarker. EEG is the principal functional biomarker but is not gene-specific.

### Genetic testing strategy

1. Use a comprehensive epilepsy/DEE/epilepsy–aphasia panel or trio exome/genome sequencing with **GRIN2A** and other SWAS genes.
2. Ensure copy-number calling; use chromosomal microarray if exome/panel CNV sensitivity is limited or syndromic findings suggest a chromosomal lesion.
3. Confirm the variant and test parents. Deep sequencing can be considered if mosaicism is suspected.
4. Interpret with ACMG/AMP criteria and ClinVar/ClinGen evidence, avoiding treatment assignment from in-silico prediction alone.
5. For candidate missense variants, receptor electrophysiology and trafficking assays can be decisive because GoF versus LoF determines the logic of experimental therapy.

Karyotyping/FISH are reserved for suspected large rearrangements. Mitochondrial, repeat-expansion, liquid-biopsy, proteomic, and metabolomic tests have no routine role.

Differentials include structural D/EE-SWAS, non-GRIN2A epilepsy–aphasia disorders, and other monogenic epilepsies. The 2024 D/EE-SWAS cohort found an etiology in 42/91 (46%), including a genetic cause in 31/91 (34%) and structural cause in 12/91 (13%), demonstrating substantial etiologic heterogeneity. (viswanathan2024solvingtheetiology pages 1-3)

Population newborn screening is not available. Cascade testing is appropriate after a familial variant is identified. Prenatal diagnosis and preimplantation genetic testing are technically possible for a known familial pathogenic variant.

## 11. Outcome and prognosis

No reliable disease-specific survival curve, life expectancy, or mortality rate is available. Most morbidity derives from communication disability, cognitive impairment, seizures, behavioral/psychiatric complications, motor dysfunction, and caregiver burden. Severe drug-resistant epilepsy may carry the general risks of injury, status epilepticus, and sudden unexpected death in epilepsy, but GRIN2A-specific rates are unknown.

Prognosis is strongly variable. More favorable indicators include null or ATD/LBD LoF variants, milder early development, infrequent seizures, and absence of prolonged SWAS. Worse outcomes correlate with transmembrane/linker GoF variants, early DEE, severe ID, and prolonged D/EE-SWAS. These are group-level associations rather than deterministic individual predictions. (strehlow2019grin2arelateddisordersgenotype pages 1-1, strehlow2019grin2arelateddisordersgenotype pages 6-7, viswanathan2024solvingtheetiology pages 1-3)

Speech and cognitive recovery may be incomplete even after electrographic and seizure remission. There is no validated molecular prognostic biomarker beyond variant class/domain and functional characterization.

## 12. Treatment

### Standard symptomatic care

No GRIN2A-specific drug is approved. Treatment is individualized by epilepsy syndrome and seizure type and may include conventional antiseizure medicines, rescue medication and status-epilepticus planning, and—when SWAS is present—therapies used for ESES/SWAS such as benzodiazepines, corticosteroids, or other specialist-directed regimens. Ketogenic diet, vagus-nerve stimulation, or epilepsy surgery may be considered for refractory disease, although surgery is most rational when a focal structural/epileptogenic lesion is demonstrated rather than for a diffuse germline synaptopathy.

Speech-language therapy, augmentative communication, occupational/physical therapy, educational accommodations, behavioral treatment, sleep management, and psychiatric care are central. Suggested NCIT mappings include Anticonvulsant Therapy, Speech Therapy, Occupational Therapy, Physical Therapy, Ketogenic Diet, Vagus Nerve Stimulation, and Genetic Counseling.

### Mechanism-directed experimental therapy

**L-serine for LoF/null variants.** L-serine is converted to D-serine, an NMDAR co-agonist. In a retrospective series of ten GRIN2A/GRIN2B patients treated as independent n-of-1 trials, nine had LoF/null variants. Eight of nine (89%) had reported behavioral improvement, four (44%) developmental improvement, and four (44%) EEG or seizure-frequency improvement; none of these nine had reported adverse findings. The single erroneously treated GoF case had immediate, temporary behavioral deterioration. Doses ranged from 100–850 mg/kg/day, usually in three or four divided doses, and most patients received concomitant antiseizure medication. These uncontrolled, partly subjective observations are hypothesis-generating, not proof of efficacy. (krey2022lserinetreatmentis pages 1-2)

The relevant abstract states: **“Among all nine individuals with LoF missense or null variants, L-serine treatment was associated with improvements in behavior in eight (89%), in development in four (44%), and/or in EEG or seizure frequency in four (44%).”** (krey2022lserinetreatmentis pages 1-2)

**NCT04646447** is an open-label, single-group study of L-serine in functionally annotated LoF GRIN-related encephalopathy, planned enrollment 20, age over two years. The registry record’s last known status was recruiting but had not been recently verified. It proposed approximately 500 mg/kg/day based on prior experience. [ClinicalTrials.gov: NCT04646447](https://clinicaltrials.gov/study/NCT04646447). (NCT04646447 chunk 1)

**NMDAR antagonism for GoF variants.** Memantine has mechanistic and anecdotal support for selected GoF variants, but efficacy cannot be generalized because variant pharmacology differs. Functional testing and specialist oversight are essential. A 2024 expert review summarized memantine for GoF and L-serine for LoF as potentially available personalized approaches while emphasizing that effectiveness requires trials. The severe functional consequences of pore/linker GoF variants support this precision strategy, but not empirical antagonist use in every GRIN2A patient. (strehlow2019grin2arelateddisordersgenotype pages 1-1)

**Radiprodil.** Honeycomb, **NCT05818943**, is an open-label phase 1 study of radiprodil in 24 children aged 6 months–12 years with functionally confirmed GoF GRIN variants. Radiprodil is an orally active negative allosteric modulator of the GluN2B/NR2B subunit; outcomes include safety, pharmacokinetics, video-EEG seizure burden, seizure frequency, behavior, motor function, sleep, PedsQL, and caregiver burden. As of the registry’s November 2024 verification it was active, not recruiting. This is a pan-GRIN mechanistic trial, not evidence of established GRIN2A efficacy. [ClinicalTrials.gov: NCT05818943](https://clinicaltrials.gov/study/NCT05818943). (NCT05818943 chunk 1, NCT05818943 chunk 2)

Gene replacement, CRISPR editing, antisense/RNA therapy, and cell therapy remain preclinical concepts; no approved or disease-specific clinical implementation was identified.

## 13. Prevention

Primary prevention through lifestyle or vaccination is not applicable to a dominantly inherited/de novo disorder. Relevant prevention is reproductive and complication-focused:

* preconception and prenatal genetic counseling;
* parental/cascade testing;
* prenatal diagnosis or PGT-M for a known pathogenic familial variant;
* early EEG including sleep and rapid treatment of escalating SWAS or seizures;
* seizure first-aid plans, water/heights precautions, medication adherence, rescue therapy, and SUDEP counseling according to epilepsy risk;
* early speech, developmental, behavioral, and educational intervention.

No prophylactic medication is recommended for an asymptomatic carrier solely on genotype. There is no population or newborn-screening program.

## 14. Other species and natural disease

GRIN2A/Grin2a orthologs are evolutionarily conserved across mammals and vertebrates because NMDA-receptor signaling is fundamental to synaptic plasticity. No well-established naturally occurring veterinary syndrome directly homologous to human GRIN2A epilepsy–aphasia disorder was recovered. There is no infectious transmission or zoonotic potential.

Suggested taxonomy annotations include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)**, and **Danio rerio (7955)** for experimental systems. Breed ontology is not applicable without a confirmed natural animal disease.

## 15. Model organisms and experimental systems

### Grin2a knockout mouse

Longitudinal diffusion MRI found transient microstructural changes in neocortex, corpus callosum, hippocampus, and thalamus, mainly at postnatal day 30, while EEG showed neocortical epileptiform discharges in the third postnatal week. The abstract states: **“Grin2a KO mice replicated several anomalies found in patients with EAS disorders.”** The model supports study of developmental thalamocortical/cortical maturation and treatment timing, but it models complete loss rather than heterozygous human domain-specific GoF variants and cannot recapitulate human language. [Epilepsia 2018; DOI 10.1111/epi.14543](https://doi.org/10.1111/epi.14543). (salmi2018transientmicrostructuralbrain pages 1-2)

### Grin2a N615S knock-in mouse

This pore-region model reduces voltage-dependent magnesium block. It developed NMDAR-dependent audiogenic seizures from hyperexcitable midbrain circuits, exploratory hyperactivity, dysregulated attention and associative learning, reduced hippocampal c-Fos response, and impaired theta–gamma synchronization. It is valuable for GoF pore physiology and circuit-specific consequences but does not model typical haploinsufficiency. [Communications Biology 2021; DOI 10.1038/s42003-020-01538-4](https://doi.org/10.1038/s42003-020-01538-4). (bertocchi2021voltageindependentglun2atypenmda pages 1-2)

### Cellular systems

Heterologous expression, Xenopus-oocyte/two-electrode voltage clamp, and mammalian electrophysiology define agonist potency, current density, magnesium block, deactivation, open probability, surface expression, and drug response. Rat primary cortical neurons assess receptor localization, dendritic spines, and synapses. These systems are indispensable for variant classification and precision-treatment logic but lack whole-brain developmental and pharmacokinetic context. The p.P1199Rfs*32 study is a recent exemplar. [Journal of Neuroscience, published January 24, 2024; DOI 10.1523/JNEUROSCI.0557-23.2023](https://doi.org/10.1523/JNEUROSCI.0557-23.2023). (vieira2024aframeshiftvariant pages 1-2)

Patient-derived iPSC neurons, cerebral organoids, zebrafish knockouts, and CRISPR isogenic lines are promising for cell-type-specific phenotyping and drug screening, but mature GRIN2A-specific datasets were not established in the retrieved 2023–2024 literature.

## Evidence limitations and curation recommendations

The strongest natural-history evidence remains the 2019 248-person aggregate cohort; ascertainment was referral- and publication-based, denominators vary by phenotype, and frequencies should not be treated as population prevalence. (strehlow2019grin2arelateddisordersgenotype pages 1-1, strehlow2019grin2arelateddisordersgenotype pages 6-7) Recent 2023–2024 advances are predominantly mechanistic—especially C-terminal trafficking—and syndrome-level genomic work in D/EE-SWAS rather than new large GRIN2A-specific prospective cohorts. (vieira2024aframeshiftvariant pages 1-2, viswanathan2024solvingtheetiology pages 1-3)

For knowledge-base curation, record **variant-specific functional direction**, assay system, inheritance, EEG state during sleep, developmental status before seizures/SWAS, speech phenotype, and treatment exposure. Do not annotate L-serine, memantine, or radiprodil as established effective therapy; label them experimental and mechanism-stratified. PMID values were not consistently present in the retrieved full texts, so DOI and trial URLs are provided rather than risking incorrect PMID assignment.

References

1. (strehlow2019grin2arelateddisordersgenotype pages 1-1): Vincent Strehlow, Henrike O Heyne, Danique R M Vlaskamp, Katie F M Marwick, Gabrielle Rudolf, Julitta de Bellescize, Saskia Biskup, Eva H Brilstra, Oebele F Brouwer, Petra M C Callenbach, Julia Hentschel, Edouard Hirsch, Peter C Kind, Cyril Mignot, Konrad Platzer, Patrick Rump, Paul A Skehel, David J A Wyllie, Giles E Hardingham, Conny M A van Ravenswaaij-Arts, Gaetan Lesca, Johannes R Lemke, Alexis Arzimanoglou, Paul B Augustijn, Patrick Van Bogaert, Helene Bourry, Peter Burfeind, Yoyo Chu, Brian Chung, Diane Doummar, Patrick Edery, Aviva Fattal-Valevski, Mélanie Fradin, Marion Gerard, Christa de Geus, Boudewijn Gunning, Danielle Hasaerts, Ingo Helbig, Katherine L Helbig, Rami Jamra, Mélanie Jennesson Lyver, Jolien S Klein Wassink-Ruiter, David A Koolen, Damien Lederer, Roelineke J Lunsing, Mikaël Mathot, Hélène Maurey, Shay Menascu, Anne Michel, Ghayda Mirzaa, Diana Mitter, Hiltrud Muhle, Rikke S Møller, Caroline Nava, Margaret O’Brien, Evelyn van Pinxteren-Nagler, Anne van Riesen, Christelle Rougeot, Damien Sanlaville, Jolanda H Schieving, Steffen Syrbe, Hermine E Veenstra-Knol, Nienke Verbeek, Dorothée Ville, Yvonne J Vos, Pascal Vrielynck, Sabrina Wagner, Sarah Weckhuysen, and Marjolein H Willemsen. Grin2a-related disorders: genotype and functional consequence predict phenotype. Brain, 142:80-92, Dec 2019. URL: https://doi.org/10.1093/brain/awy304, doi:10.1093/brain/awy304. This article has 282 citations and is from a highest quality peer-reviewed journal.

2. (strehlow2019grin2arelateddisordersgenotype pages 11-11): Vincent Strehlow, Henrike O Heyne, Danique R M Vlaskamp, Katie F M Marwick, Gabrielle Rudolf, Julitta de Bellescize, Saskia Biskup, Eva H Brilstra, Oebele F Brouwer, Petra M C Callenbach, Julia Hentschel, Edouard Hirsch, Peter C Kind, Cyril Mignot, Konrad Platzer, Patrick Rump, Paul A Skehel, David J A Wyllie, Giles E Hardingham, Conny M A van Ravenswaaij-Arts, Gaetan Lesca, Johannes R Lemke, Alexis Arzimanoglou, Paul B Augustijn, Patrick Van Bogaert, Helene Bourry, Peter Burfeind, Yoyo Chu, Brian Chung, Diane Doummar, Patrick Edery, Aviva Fattal-Valevski, Mélanie Fradin, Marion Gerard, Christa de Geus, Boudewijn Gunning, Danielle Hasaerts, Ingo Helbig, Katherine L Helbig, Rami Jamra, Mélanie Jennesson Lyver, Jolien S Klein Wassink-Ruiter, David A Koolen, Damien Lederer, Roelineke J Lunsing, Mikaël Mathot, Hélène Maurey, Shay Menascu, Anne Michel, Ghayda Mirzaa, Diana Mitter, Hiltrud Muhle, Rikke S Møller, Caroline Nava, Margaret O’Brien, Evelyn van Pinxteren-Nagler, Anne van Riesen, Christelle Rougeot, Damien Sanlaville, Jolanda H Schieving, Steffen Syrbe, Hermine E Veenstra-Knol, Nienke Verbeek, Dorothée Ville, Yvonne J Vos, Pascal Vrielynck, Sabrina Wagner, Sarah Weckhuysen, and Marjolein H Willemsen. Grin2a-related disorders: genotype and functional consequence predict phenotype. Brain, 142:80-92, Dec 2019. URL: https://doi.org/10.1093/brain/awy304, doi:10.1093/brain/awy304. This article has 282 citations and is from a highest quality peer-reviewed journal.

3. (NCT04646447 chunk 1):  Tolerability and Efficacy of L-Serine in Patients With GRIN-related Encephalopathy. Fundació Sant Joan de Déu. 2020. ClinicalTrials.gov Identifier: NCT04646447

4. (vieira2024aframeshiftvariant pages 1-2): M. M. Vieira, S. Peng, S. Won, E. Hong, S. K. Inati, A. Thurm, A. H. Thiam, S. Kim, S. J. Myers, J. D. Badger, S. F. Traynelis, W. Lu, and K. W. Roche. A frameshift variant of glun2a identified in an epilepsy patient results in nmda receptor mistargeting. The Journal of Neuroscience, 44:e0557232023, Nov 2023. URL: https://doi.org/10.1523/jneurosci.0557-23.2023, doi:10.1523/jneurosci.0557-23.2023. This article has 6 citations.

5. (tumdam2024nmdareceptorsin pages 4-6): Roshan Tumdam, Yara Hussein, Tali Garin-Shkolnik, and Shani Stern. Nmda receptors in neurodevelopmental disorders: pathophysiology and disease models. International Journal of Molecular Sciences, Nov 2024. URL: https://doi.org/10.3390/ijms252212366, doi:10.3390/ijms252212366. This article has 40 citations.

6. (strehlow2019grin2arelateddisordersgenotype pages 6-7): Vincent Strehlow, Henrike O Heyne, Danique R M Vlaskamp, Katie F M Marwick, Gabrielle Rudolf, Julitta de Bellescize, Saskia Biskup, Eva H Brilstra, Oebele F Brouwer, Petra M C Callenbach, Julia Hentschel, Edouard Hirsch, Peter C Kind, Cyril Mignot, Konrad Platzer, Patrick Rump, Paul A Skehel, David J A Wyllie, Giles E Hardingham, Conny M A van Ravenswaaij-Arts, Gaetan Lesca, Johannes R Lemke, Alexis Arzimanoglou, Paul B Augustijn, Patrick Van Bogaert, Helene Bourry, Peter Burfeind, Yoyo Chu, Brian Chung, Diane Doummar, Patrick Edery, Aviva Fattal-Valevski, Mélanie Fradin, Marion Gerard, Christa de Geus, Boudewijn Gunning, Danielle Hasaerts, Ingo Helbig, Katherine L Helbig, Rami Jamra, Mélanie Jennesson Lyver, Jolien S Klein Wassink-Ruiter, David A Koolen, Damien Lederer, Roelineke J Lunsing, Mikaël Mathot, Hélène Maurey, Shay Menascu, Anne Michel, Ghayda Mirzaa, Diana Mitter, Hiltrud Muhle, Rikke S Møller, Caroline Nava, Margaret O’Brien, Evelyn van Pinxteren-Nagler, Anne van Riesen, Christelle Rougeot, Damien Sanlaville, Jolanda H Schieving, Steffen Syrbe, Hermine E Veenstra-Knol, Nienke Verbeek, Dorothée Ville, Yvonne J Vos, Pascal Vrielynck, Sabrina Wagner, Sarah Weckhuysen, and Marjolein H Willemsen. Grin2a-related disorders: genotype and functional consequence predict phenotype. Brain, 142:80-92, Dec 2019. URL: https://doi.org/10.1093/brain/awy304, doi:10.1093/brain/awy304. This article has 282 citations and is from a highest quality peer-reviewed journal.

7. (salmi2018transientmicrostructuralbrain pages 1-2): Manal Salmi, Radu Bolbos, Sylvian Bauer, Marat Minlebaev, Nail Burnashev, and Pierre Szepetowski. Transient microstructural brain anomalies and epileptiform discharges in mice defective for epilepsy and language‐related nmda receptor subunit gene grin2a. Epilepsia, 59:1919-1930, Aug 2018. URL: https://doi.org/10.1111/epi.14543, doi:10.1111/epi.14543. This article has 47 citations and is from a domain leading peer-reviewed journal.

8. (strehlow2019grin2arelateddisordersgenotype pages 3-3): Vincent Strehlow, Henrike O Heyne, Danique R M Vlaskamp, Katie F M Marwick, Gabrielle Rudolf, Julitta de Bellescize, Saskia Biskup, Eva H Brilstra, Oebele F Brouwer, Petra M C Callenbach, Julia Hentschel, Edouard Hirsch, Peter C Kind, Cyril Mignot, Konrad Platzer, Patrick Rump, Paul A Skehel, David J A Wyllie, Giles E Hardingham, Conny M A van Ravenswaaij-Arts, Gaetan Lesca, Johannes R Lemke, Alexis Arzimanoglou, Paul B Augustijn, Patrick Van Bogaert, Helene Bourry, Peter Burfeind, Yoyo Chu, Brian Chung, Diane Doummar, Patrick Edery, Aviva Fattal-Valevski, Mélanie Fradin, Marion Gerard, Christa de Geus, Boudewijn Gunning, Danielle Hasaerts, Ingo Helbig, Katherine L Helbig, Rami Jamra, Mélanie Jennesson Lyver, Jolien S Klein Wassink-Ruiter, David A Koolen, Damien Lederer, Roelineke J Lunsing, Mikaël Mathot, Hélène Maurey, Shay Menascu, Anne Michel, Ghayda Mirzaa, Diana Mitter, Hiltrud Muhle, Rikke S Møller, Caroline Nava, Margaret O’Brien, Evelyn van Pinxteren-Nagler, Anne van Riesen, Christelle Rougeot, Damien Sanlaville, Jolanda H Schieving, Steffen Syrbe, Hermine E Veenstra-Knol, Nienke Verbeek, Dorothée Ville, Yvonne J Vos, Pascal Vrielynck, Sabrina Wagner, Sarah Weckhuysen, and Marjolein H Willemsen. Grin2a-related disorders: genotype and functional consequence predict phenotype. Brain, 142:80-92, Dec 2019. URL: https://doi.org/10.1093/brain/awy304, doi:10.1093/brain/awy304. This article has 282 citations and is from a highest quality peer-reviewed journal.

9. (krey2022lserinetreatmentis pages 1-2): Ilona Krey, Sarah von Spiczak, Kathrine M. Johannesen, Christiane Hikel, Gerhard Kurlemann, Hiltrud Muhle, Diane Beysen, Tobias Dietel, Rikke S. Møller, Johannes R. Lemke, and Steffen Syrbe. L-serine treatment is associated with improvements in behavior, eeg, and seizure frequency in individuals with grin-related disorders due to null variants. Neurotherapeutics, 19:334-341, Jan 2022. URL: https://doi.org/10.1007/s13311-021-01173-9, doi:10.1007/s13311-021-01173-9. This article has 68 citations and is from a peer-reviewed journal.

10. (viswanathan2024solvingtheetiology pages 1-3): Sindhu Viswanathan, Karen L. Oliver, Brigid M. Regan, Amy L. Schneider, Candace T. Myers, Michele G. Mehaffey, Amy J. LaCroix, Jayne Antony, Richard Webster, Michael Cardamone, Gopinath M. Subramanian, Annie T.G. Chiu, Eugenia Roza, Raluca I. Teleanu, Stephen Malone, Richard J. Leventer, Deepak Gill, Samuel F. Berkovic, Michael S. Hildebrand, Beatrice S. Goad, Katherine B. Howell, Joseph D. Symonds, Andreas Brunklaus, Lynette G. Sadleir, Sameer M. Zuberi, Heather C. Mefford, and Ingrid E. Scheffer. Solving the etiology of developmental and epileptic encephalopathy with spike–wave activation in sleep <scp>(d/ee‐swas</scp>). Annals of Neurology, 96:932-943, Aug 2024. URL: https://doi.org/10.1002/ana.27041, doi:10.1002/ana.27041. This article has 21 citations and is from a highest quality peer-reviewed journal.

11. (NCT05818943 chunk 1):  Honeycomb: Evaluation of Radiprodil in Children with GRIN-related Disorder. GRIN Therapeutics, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05818943

12. (NCT05818943 chunk 2):  Honeycomb: Evaluation of Radiprodil in Children with GRIN-related Disorder. GRIN Therapeutics, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05818943

13. (bertocchi2021voltageindependentglun2atypenmda pages 1-2): Ilaria Bertocchi, Ahmed Eltokhi, Andrey Rozov, Vivan Nguyễn Chi, Vidar Jensen, Thorsten Bus, Verena Pawlak, Marta Serafino, Hannah Sonntag, Boyi Yang, Nail Burnashev, Shi-Bin Li, Horst A. Obenhaus, Martin Both, Burkhard Niewoehner, Frank N. Single, Michael Briese, Thomas Boerner, Peter Gass, John Nick P. Rawlins, Georg Köhr, David M. Bannerman, and Rolf Sprengel. Voltage-independent glun2a-type nmda receptor ca2+ signaling promotes audiogenic seizures, attentional and cognitive deficits in mice. Communications Biology, Jan 2021. URL: https://doi.org/10.1038/s42003-020-01538-4, doi:10.1038/s42003-020-01538-4. This article has 45 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](GRIN2A-Related_Epileptic_Encephalopathy_and_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md)