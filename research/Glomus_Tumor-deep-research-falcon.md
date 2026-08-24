---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:01:34.598069'
end_time: '2026-07-31T17:11:43.099029'
duration_seconds: 608.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glomus Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Glomus_Tumor-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glomus Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Glomus Tumor** covering all of the
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
- **Disease Name:** Glomus Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Glomus Tumor** covering all of the
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


# Glomus Tumor: Disease Characteristics Research Report

**Scope.** This report concerns the **soft-tissue glomus tumor**, a perivascular/pericytic neoplasm showing differentiation toward modified smooth-muscle cells of the normal glomus body. It does **not** concern “glomus jugulare,” “glomus tympanicum,” or carotid-body tumors, which are paragangliomas with different cells of origin, genetics, management, and ontology mappings.

**Evidence note.** Glomus tumor is rare, and much of the literature consists of retrospective series and case reports. The strongest retrieved recent evidence comprised a 2023 NF1 surveillance guideline and the 2024 ClinicalTrials.gov update of a molecularly selected malignant-glomus-tumor trial. Some requested database fields could not be validated from accessible primary sources and are therefore marked as unconfirmed rather than inferred.

| Domain | Established finding | Evidence/recency | Suggested ontology terms |
|---|---|---|---|
| Scope/definition | **Soft-tissue glomus tumor** is the target entity here; it is a **pericytic/glomus-cell neoplasm** and should **not be conflated with glomus jugulare/tympanicum paraganglioma**. ClinicalTrials.gov indexes “Glomus Tumor” under MeSH **D005918**; NOTCH-focused malignant glomus tumor trial eligibility further supports this soft-tissue usage. (NCT03422679 chunk 1, NCT03422679 chunk 2) | Clinical registry evidence, updated **2024-01-16**; mechanistic review notes glomus tumors as a subset of **pericytic tumours** with MIR143-NOTCH fusions. (gaudio2022notchsignallingin pages 10-11, NCT03422679 chunk 1, NCT03422679 chunk 2) | MeSH: **D005918 Glomus Tumor**; NCIT: *Glomus Tumor*; MONDO: *not confirmed from available context* |
| Typical phenotype | Classic presentation is a **small painful lesion**, often digital/subungual, with marked **tenderness** and often **cold sensitivity**; extradigital and visceral tumors also occur. NF1 guidance specifically mentions **glomus tumours of the digits** in adults. (carton2023erngenturistumour pages 7-8) | Mixed evidence base; strong clinical tradition, but only digit localization is directly supported in retrieved context. NF1 surveillance guideline is **2023**. (carton2023erngenturistumour pages 7-8) | HPO: **Pain (HP:0012531)**, **Tenderness (HP:0033748)**, **Abnormality of the nail (HP:0001597)**, **Cold-induced pain** *suggested term if curated* |
| Anatomy | Common sites include **digits/finger**, but glomus tumors can also occur in **soft tissue of limbs, trunk, head/neck**, and less commonly **stomach, bone, tongue, lung** in fusion-defined or related pericytic neoplasms. (agaram2019gli1amplificationsexpandthe pages 1-2) | Molecular pathology review/series context; **2019-2022** evidence indicates broad anatomic spectrum for pericytic tumors with related signaling lesions. (agaram2019gli1amplificationsexpandthe pages 1-2, gaudio2022notchsignallingin pages 10-11) | UBERON: **finger (UBERON:0002389)**, **nail unit (suggested)**, **soft tissue of upper limb/lower limb (suggested)**, **stomach (UBERON:0000945)** |
| Histology/IHC | Histology typically shows **uniform round/ovoid to epithelioid cells** in nests/trabeculae around a **delicate vascular network**. In related pericytic tumors, **smooth muscle actin (SMA)** and **laminin/collagen IV-type pericellular basement membrane** support pericytic/glomus differentiation; immunophenotype may be variable. (agaram2019gli1amplificationsexpandthe pages 1-2, gaudio2022notchsignallingin pages 10-11) | Pathology/mechanistic review evidence; **2019-2022**. GLI1-amplified comparator series emphasizes nested epithelioid morphology and variable SMA positivity, useful in differential diagnosis. (agaram2019gli1amplificationsexpandthe pages 1-2, gaudio2022notchsignallingin pages 10-11) | GO/CL/NCIT suggestions: **vascular smooth muscle cell differentiation (GO:0051146)**, **pericyte (CL:0000669)**, **smooth muscle actin positive** *pathology annotation* |
| Somatic genetics: MIR143-NOTCH | **MIR143-NOTCH1/2/3 fusions** are a major recurrent driver in glomus tumors; review text states these fusions are found in **almost 50%** of glomus tumours. This supports aberrant **NOTCH pathway activation** as an upstream oncogenic mechanism. (gaudio2022notchsignallingin pages 10-11, mertens2016genefusionsin pages 19-20) | Mechanistic review **2022** citing primary fusion literature; gene-fusion review **2016** notes MIR143-NOTCH fusions in both **benign and malignant** lesions. (gaudio2022notchsignallingin pages 10-11, mertens2016genefusionsin pages 19-20) | HGNC: **MIR143HG**, **NOTCH1**, **NOTCH2**, **NOTCH3**; GO: **Notch signaling pathway (GO:0007219)** |
| Somatic genetics: BRAF | **BRAF-mutant glomus tumors** are a recognized subset, reported in the literature and associated with **malignant histologic characteristics**; however, precise frequency is not available from retrieved full-text context here. | Evidence present only indirectly in retrieved search metadata/unobtainable citation trail; **supportive but not directly quotable from available contexts**. | HGNC: **BRAF**; GO: **MAPK cascade (GO:0000165)** |
| Germline associations | **NF1** is an established predisposition context for **digital glomus tumors**; the 2023 ERN GENTURIS NF1 guideline lists **glomus tumours of the digits** among tumors with increased adult risk. By contrast, **GLMN (glomulin)** classically underlies **glomuvenous malformation/glomangioma**, which is related but **distinct from typical solitary soft-tissue glomus tumor**. (carton2023erngenturistumour pages 7-8) | NF1 evidence is directly supported and **2023**. GLMN distinction is standard disease-taxonomy knowledge but **not directly documented in retrieved contexts**, so should be curated cautiously. (carton2023erngenturistumour pages 7-8) | HGNC: **NF1**, **GLMN**; MONDO/Orphanet suggestions: **Neurofibromatosis type 1**, **Glomuvenous malformation** |
| Mechanism/pathophysiology | Working model: recurrent **MIR143-driven NOTCH fusion** places a strong smooth-muscle/pericytic regulatory locus upstream of **NOTCH intracellular signaling**, promoting abnormal perivascular cell growth and glomus-tumor phenotype. Reviews frame glomus tumors within **dysregulated vascular NOTCH signaling**. (gaudio2022notchsignallingin pages 10-11, mertens2016genefusionsin pages 19-20) | Mechanistic synthesis from review evidence **2016, 2022**. | GO: **Notch signaling pathway (GO:0007219)**, **blood vessel morphogenesis (GO:0048514)**; CL: **pericyte (CL:0000669)** |
| Diagnosis | Diagnosis is usually based on **clinical localization + imaging + excision pathology**. For malignant/unusual cases, **molecular testing** for **NOTCH pathway alterations** can be clinically relevant, as shown by trial enrollment criteria requiring **activating mutation or genetic lesion**. (NCT03422679 chunk 1) | Direct clinical-trial evidence **2024 registry update**; broader routine diagnostic specifics are not fully captured in available contexts. (NCT03422679 chunk 1) | NCIT: **Magnetic Resonance Imaging**, **Biopsy**, **Surgical Excision**, **Molecular Diagnostic Testing** |
| Treatment | For typical localized disease, standard care is **complete surgical excision**; no systemic standard is established for most benign tumors. For advanced malignant disease with NOTCH activation, investigational targeted therapy has included the **pan-NOTCH inhibitor CB-103**. (NCT03422679 chunk 1, NCT03422679 chunk 2) | Trial evidence current to **2024**; localized surgical management is established practice but not directly detailed in retrieved full text. | NCIT: **Surgical Excision**, **Targeted Therapy**, **CB-103** *if mapped*, **Notch Pathway Inhibitor** |
| Malignant disease/trial | Malignant glomus tumor is **rare** but clinically important. A dedicated phase I/II basket trial (**NCT03422679**) included **“Glomus Tumor, Malignant”** among eligible advanced solid tumors with NOTCH-pathway lesions; trial status was **terminated for business reason**, not efficacy. (NCT03422679 chunk 1, NCT03422679 chunk 2) | High-value recent implementation evidence: ClinicalTrials.gov results posted **2024-01-16**. (NCT03422679 chunk 1, NCT03422679 chunk 2) | NCIT: **Malignant Glomus Tumor**, **Advanced Solid Neoplasm**, **Clinical Trial** |
| Prognosis | **Benign solitary glomus tumors** generally have excellent outcomes after complete excision; adverse behavior is mainly a concern in **malignant/atypical** lesions. Precise recurrence/metastasis rates are **not available from retrieved contexts**. | Inference from disease class and rarity literature; direct numeric prognosis data **not captured** in available full text. | HPO/NCIT suggestions: **Recurrence**, **Metastatic malignant neoplasm** |
| Prevention | No established **primary prevention** exists for sporadic glomus tumor. In **NF1**, practical prevention is limited to **clinical vigilance/earlier recognition** of symptomatic digital tumors rather than population screening. (carton2023erngenturistumour pages 7-8) | NF1 tumor-surveillance framework **2023** supports awareness-based secondary prevention. | NCIT: **Surveillance**, **Genetic Counseling**; HPO: symptom monitoring terms |
| Animal/models | No dedicated, well-established **in vivo glomus tumor model** was identified in the retrieved contexts. Mechanistic inference currently relies more on **human tumor genomics** and broader **vascular NOTCH biology** than on disease-specific models. (gaudio2022notchsignallingin pages 10-11) | Evidence gap, based on absence in retrieved literature and reliance on pathway reviews. | GO: **Notch signaling pathway**; model ontology terms: *not available from current evidence* |
| Evidence gaps | Key gaps from the available evidence set: **validated MONDO/Orphanet mapping**, robust **epidemiology/incidence**, direct **HPO frequency estimates**, standardized **malignancy-risk biomarkers**, disease-specific **QoL** data, curated **GLMN vs glomus tumor** boundary resources, and **animal/model systems**. | Important for curation quality; several requested knowledge-base fields remain under-supported by currently retrieved full text. | MONDO/HPO/UBERON/CL/NCIT mappings require targeted follow-up curation |


*Table: This compact table summarizes core disease-knowledge-base facts for soft-tissue glomus tumor while clearly separating it from paraganglioma terminology. It emphasizes molecular drivers, NF1 association, malignant-disease trial evidence, and current evidence gaps relevant for structured curation.*

## 1. Disease information

### Definition and classification

A glomus tumor is usually a small, circumscribed neoplasm of uniform round glomus cells arranged around branching vessels. It belongs to the **pericytic/perivascular tumor** family. Most lesions are benign and occur in the distal extremities, especially the subungual region; extradigital, deep-soft-tissue, visceral, and very rarely malignant tumors occur.

ClinicalTrials.gov and MeSH index the entity as **Glomus Tumor, MeSH D005918**. The registry places it under vascular-tissue and connective/soft-tissue neoplasms. The trial terminology “Glomus Tumor, Malignant” confirms that this indexing includes the malignant soft-tissue entity rather than only paraganglioma. (NCT03422679 chunk 1, NCT03422679 chunk 2)

**Identifiers and suggested mappings**

- **MeSH:** D005918, Glomus Tumor—directly validated. (NCT03422679 chunk 2)
- **MONDO:** a separate current MONDO identifier could not be validated from the retrieved sources; curate against the live MONDO release rather than assigning an uncertain ID.
- **OMIM/Orphanet:** typical sporadic solitary glomus tumor does not have a single well-established Mendelian disease entry. Do not substitute entries for **glomuvenous malformation caused by GLMN**.
- **ICD-10-CM:** coding is site and behavior dependent, commonly under benign neoplasm of connective/other soft tissue or uncertain/unknown behavior when appropriate; there is no universally satisfactory disease-specific code.
- **ICD-11:** use morphology plus site/behavior coding after confirmation in the current release.
- **Category:** pericytic/perivascular soft-tissue neoplasm; usually benign, rarely malignant.
- **Synonyms:** glomus cell tumor, glomangioma, glomangiomyoma, solid glomus tumor. Strictly, the latter three may denote histologic variants and should not always be treated as exact synonyms. “Glomus jugulare tumor” is an excluded paraganglioma synonym.

This report synthesizes **aggregated disease-level resources and published cohorts**, not individual EHR-derived patient data. The ClinicalTrials.gov record is aggregated study-level information.

## 2. Etiology

### Causal and genetic factors

Most solitary tumors are sporadic somatic neoplasms. The principal established molecular class has rearrangements joining the **MIR143/MIR143HG locus to NOTCH1, NOTCH2, or NOTCH3**. A vascular-NOTCH review reports that such fusions occur in “**almost 50% of glomus tumours**,” while a gene-fusion review notes their detection in both benign and malignant lesions. (gaudio2022notchsignallingin pages 10-11, mertens2016genefusionsin pages 19-20)

The strongest recognized constitutional association is **neurofibromatosis type 1 (NF1)**, particularly with multiple or recurrent painful digital tumors. The 2023 ERN GENTURIS guideline states that in adulthood the risk of “**glomus tumours of the digits**” increases in NF1. This is an authoritative human guideline association, although it does not supply a penetrance estimate for glomus tumors. Published February 2023; DOI: [10.1016/j.eclinm.2022.101818](https://doi.org/10.1016/j.eclinm.2022.101818). (carton2023erngenturistumour pages 7-8)

**GLMN** requires careful separation. Germline loss-of-function variants in GLMN cause autosomal-dominant glomuvenous malformations, historically called multiple glomangiomas. These vascular malformations overlap morphologically and terminologically with glomus tumors but are not equivalent to the typical solitary neoplasm. Variant-level ClinVar/gnomAD frequencies were not available in the retrieved evidence.

Somatic **BRAF p.Val600Glu** has been reported in a minority of glomus tumors and appears enriched among lesions with malignant histologic features, but an exact frequency was not recoverable from accessible full text and should not be entered without verification of the primary cohort.

### Environmental, infectious, lifestyle, and protective factors

No reproducible causal association with smoking, alcohol, diet, toxins, radiation, occupation, infection, or trauma has been established. Trauma may bring a painful lesion to attention but is not a proven cause. No validated genetic or environmental protective factor is known. There is no demonstrated gene–environment interaction.

## 3. Phenotypes

The classic digital phenotype is a small, intensely painful nodule with pinpoint tenderness and cold hypersensitivity. Pain can be spontaneous or pressure-provoked and may substantially impair sleep, manual work, typing, footwear tolerance, and daily activities despite the tumor’s small size. Formal EQ-5D, SF-36, or PROMIS studies and reliable phenotype frequencies are lacking.

Suggested structured phenotypes include:

- **Localized pain:** symptom; often severe and chronic/episodic; **HP:0012531 Pain**.
- **Tenderness:** clinical sign, typically sharply localized; **HP:0033748 Tenderness**.
- **Cold-provoked pain/hypersensitivity:** symptom; no confidently validated dedicated HPO identifier was established from retrieved evidence, so use a curated cold-sensitivity child term if available.
- **Subungual blue-red nodule or nail-bed discoloration:** physical manifestation; suggest **HP:0001597 Abnormality of the nail** plus a more specific nail-bed term if available.
- **Nail plate distortion:** sign in larger or longstanding subungual lesions; HP:0001597.
- **Gastric or visceral presentation:** abdominal pain, gastrointestinal bleeding, anemia, or an incidental submucosal mass; site-specific evidence is predominantly small series and case reports.
- **Malignant disease:** enlarging deep mass, local invasion, recurrence, or metastasis; highly variable and exceptionally rare.

Typical onset is in adolescence through middle adulthood, but pediatric and older-adult cases occur. Solitary digital disease is often reported more frequently in women, whereas extradigital lesions show less consistent sex bias. The disease is usually indolent until excision; symptoms may persist for years because of diagnostic delay.

## 4. Genetic and molecular information

### MIR143–NOTCH alterations

MIR143–NOTCH1/2/3 fusions are recurrent somatic structural variants and probably the most characteristic known drivers. The available review states that they occur in nearly half of tumors, and another review explicitly records them in both benign and malignant lesions. (gaudio2022notchsignallingin pages 10-11, mertens2016genefusionsin pages 19-20)

**Proposed consequence:** juxtaposition of the active smooth-muscle/perivascular MIR143 regulatory region with a truncated NOTCH receptor drives ligand-independent or otherwise dysregulated NOTCH transcriptional output. This promotes survival and proliferation of glomus/pericytic-lineage cells. The causal chain is therefore:

**somatic rearrangement → constitutive NOTCH signaling → altered perivascular-cell differentiation/proliferation → vascular-rich glomus-cell nodule → focal tenderness and cold-provoked pain.**

Suggested annotations: **NOTCH1, NOTCH2, NOTCH3, MIR143HG**; GO:0007219 Notch signaling pathway; GO:0048514 blood-vessel morphogenesis; CL:0000669 pericyte.

### Other alterations and differential molecular diagnoses

BRAF V600E defines a smaller MAPK-pathway subset. Testing may be informative in malignant, metastatic, histologically atypical, or diagnostically difficult tumors, although it is not required for routine classic digital lesions.

GLI1-rearranged or GLI1-amplified pericytic tumors may mimic glomus tumor. In a 2019 comparator series of ten GLI1-amplified tumors, all ten had GLI1 amplification, nine had CDK4 co-amplification, and eight had MDM2 co-amplification; four had at least 15 mitoses per ten high-power fields and three had necrosis. The authors concluded that amplification may provide an alternative mechanism of GLI1 activation in an emerging malignant soft-tissue-tumor group. DOI: [10.1038/s41379-019-0293-x](https://doi.org/10.1038/s41379-019-0293-x), received February 18 and accepted May 1, 2019. These are **differential-diagnosis data, not frequencies in conventional glomus tumor**. (agaram2019gli1amplificationsexpandthe pages 2-4, agaram2019gli1amplificationsexpandthe pages 1-2)

No validated modifier gene, recurrent epigenetic class, germline carrier frequency, or protective allele has been established for sporadic solitary tumors. WGS/WES studies remain too small for dependable population-frequency inference.

## 5. Environmental information

No toxin, radiation exposure, pollution source, occupational exposure, lifestyle behavior, or infectious agent is recognized as causal. Glomus tumor is noncommunicable and noninfectious. Consequently, CTD-style chemical–disease causal annotations should not be added without direct experimental evidence. CHEBI annotations are relevant only to administered diagnostic agents or treatments, not etiology.

## 6. Mechanism and pathophysiology

Normal glomus bodies are specialized arteriovenous thermoregulatory structures in acral skin. Modified smooth-muscle glomus cells surround vascular channels and regulate blood flow. Neoplastic proliferation produces a compact, vascular-rich nodule in a confined and highly innervated space. Pressure, vascular tone changes, and cold-triggered contraction plausibly explain the disproportionate pain.

**Upstream:** MIR143–NOTCH rearrangement, less often MAPK activation such as BRAF V600E, or NF1-associated RAS pathway dysregulation.

**Intermediate:** abnormal NOTCH/RAS-MAPK signaling, perivascular-cell proliferation, and altered smooth-muscle differentiation. NOTCH has broad physiological roles in vascular genesis, remodeling, arterial–venous identity, branching, and homeostasis; therefore, its dysregulation is biologically coherent in a pericytic tumor. DOI: [10.1098/rsob.220004](https://doi.org/10.1098/rsob.220004), published April 2022. (gaudio2022notchsignallingin pages 10-11)

**Downstream:** circumscribed tumor growth around vessels, local compression and stimulation of sensory fibers, severe tenderness, and cold-sensitive pain. Malignant progression adds high mitotic activity, atypical mitoses, genomic instability, invasion, and metastatic capability.

Suggested terms include CL:0000669 pericyte; GO:0007219 Notch signaling; GO:0000165 MAPK cascade; GO:0001525 angiogenesis; GO:0048514 blood-vessel morphogenesis; GO:0008283 cell population proliferation; GO:0006939 smooth-muscle contraction. Relevant cellular compartments include plasma membrane, cytoplasm, and nucleus for receptor cleavage and transcriptional signaling. No reproducible metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic, or CRISPR-screen signature is presently established.

## 7. Anatomical structures affected

The prototypic sites are the distal fingers and toes, especially the subungual nail bed and fingertip pulp. Other cutaneous and deep-soft-tissue locations include forearm, arm, leg, trunk, head/neck, and peripheral nerve. Visceral tumors occur most characteristically in the gastric wall and more rarely in respiratory, genitourinary, bone, and other sites.

At tissue level, the lesion involves connective/soft tissue surrounding small vascular channels and comprises glomus cells with pericytic/smooth-muscle differentiation. Suggested mappings include CL:0000669 pericyte; UBERON:0002389 finger; UBERON:0000945 stomach; and current-release UBERON terms for nail bed, toe, skin, subcutaneous tissue, and vascular wall. Digital tumors are usually unilateral and solitary; multiplicity should prompt consideration of NF1 or glomuvenous malformation.

## 8. Temporal development

Onset is usually insidious. Small lesions may produce chronic intermittent or progressively intrusive pain for years without substantial growth. There is no accepted stage system for benign disease. A practical course classification is localized benign, incompletely excised/recurrent, uncertain malignant potential, and malignant/metastatic.

Following complete excision, pain often resolves promptly. Early postoperative persistence or rapid recurrence suggests residual tumor; late recurrence can represent regrowth or a second lesion. Malignant tumors have a variable course and may metastasize after a prolonged interval, so long-term surveillance is reasonable. No validated critical prevention window or spontaneous-remission pattern is known.

## 9. Inheritance and population

Robust population-based incidence and prevalence per 100,000 are unavailable. Frequently repeated proportions in narrative reviews derive from surgical pathology archives rather than population registries and should not be interpreted as prevalence.

Most solitary tumors are sporadic and nonfamilial. NF1 is autosomal dominant, with variable expressivity, and confers increased susceptibility to digital glomus tumors. The 2023 guideline specifically places digital glomus tumors among neoplasms whose risk increases in adults with NF1. (carton2023erngenturistumour pages 7-8)

Familial multiple glomuvenous malformation due to GLMN is autosomal dominant with incomplete penetrance and variable expression, but it is a related vascular-malformation disorder rather than a simple inheritance model for all glomus tumors. No genetic anticipation, consistent founder effect, consanguinity effect, germline mosaicism rate, or carrier frequency is established for conventional solitary glomus tumor. No convincing ethnic or geographic concentration is recognized.

## 10. Diagnostics

### Clinical and imaging diagnosis

For a painful digital lesion, examination should document pinpoint tenderness, cold sensitivity, nail discoloration/deformity, and whether pressure or transient arterial occlusion changes pain. These bedside maneuvers can localize disease but do not replace pathology.

High-resolution ultrasonography may show a small hypoechoic hypervascular nodule. MRI typically shows a sharply defined lesion with low/intermediate T1 signal, high T2 signal, and strong enhancement, but very small tumors can be missed. Plain radiographs are usually normal, although longstanding subungual lesions may erode the distal phalanx.

### Pathology

Definitive diagnosis is histopathologic. Typical lesions contain uniform round cells with sharply defined borders surrounding branching vessels. Variants include solid glomus tumor, glomangioma with a larger vascular component, and glomangiomyoma with spindle-cell/smooth-muscle maturation.

The expected immunophenotype is strong smooth-muscle actin and often h-caldesmon, calponin, vimentin, collagen IV, and laminin; desmin is variable. Cytokeratin, S100/SOX10, CD34, and endothelial markers are generally absent in tumor cells, though vessels label with CD31/ERG. Molecular confirmation by RNA sequencing, fusion panel, or NOTCH break-apart testing is most useful for atypical, deep, malignant, or diagnostically ambiguous lesions.

### Differential diagnosis

- **Hemangioma/venous malformation:** vascular spaces dominate; endothelial cells rather than perivascular glomus cells constitute the lesion.
- **Blue nevus/melanoma:** melanocytic markers S100, SOX10, and melan-A support melanocytic lineage.
- **Schwannoma/neuroma:** neural morphology and diffuse S100/SOX10.
- **Leiomyoma/angioleiomyoma:** intersecting fascicles of spindle smooth-muscle cells rather than rounded glomus cells.
- **Myopericytoma/myofibroma:** concentric vessel-associated myoid growth or biphasic morphology.
- **GIST in stomach:** KIT/DOG1 expression and KIT/PDGFRA molecular alterations.
- **Neuroendocrine tumor:** keratin and neuroendocrine-marker expression.
- **Paraganglioma:** neuroendocrine chief cells with sustentacular S100/SOX10; fundamentally different entity.
- **GLI1-altered pericytic tumor:** molecular GLI1 alteration, often S100 positivity and malignant morphology; the 2019 series shows why molecular analysis can prevent misclassification. (agaram2019gli1amplificationsexpandthe pages 2-4, agaram2019gli1amplificationsexpandthe pages 1-2)

Routine WES/WGS, CMA, karyotyping, mitochondrial testing, repeat-expansion analysis, liquid biopsy, and population screening are not indicated. For multiple digital tumors, syndromic features, or family history, evaluate **NF1** clinically and consider appropriate germline testing; consider **GLMN** testing for multiple glomuvenous lesions.

## 11. Outcome and prognosis

Localized benign tumors have an excellent prognosis and ordinarily do not affect life expectancy. Complete excision is usually curative. Morbidity before diagnosis is dominated by pain, sleep interruption, impaired hand use, reduced occupational function, and repeated ineffective treatment. Recurrence is mainly associated with incomplete excision, multifocal disease, or an initially missed satellite lesion.

Malignant glomus tumor is rare but can recur and metastasize, particularly to lung, liver, bone, and soft tissue. Histologic concern rises with marked nuclear atypia, atypical mitoses, high mitotic activity, and deep/large tumors, but modern WHO practice emphasizes cytologic atypia and atypical mitotic figures more than size/depth alone. No reliable 5- or 10-year survival estimate can be given because reported cohorts are very small and heterogeneous. Molecular markers such as BRAF or NOTCH fusion have not yet been validated as independent prognostic biomarkers.

## 12. Treatment

### Localized disease

**Complete surgical excision** with preservation of the nail matrix, neurovascular structures, or involved organ is standard. A transungual approach gives direct access to central subungual lesions; lateral or periungual approaches may reduce nail-matrix injury for appropriately located tumors. Gastric lesions are generally treated by wedge/partial gastrectomy or selected endoscopic full-thickness techniques after multidisciplinary review. Suggested NCIT terms: Surgical Excision, Local Tumor Excision, Partial Gastrectomy, and Endoscopic Resection.

Analgesics and avoidance of cold may provide temporary symptomatic relief but do not eradicate the tumor. Rehabilitation is rarely required except after extensive surgery or prolonged functional avoidance.

### Malignant or unresectable disease

Management should occur in a sarcoma multidisciplinary center. Resectable disease is treated surgically, sometimes with radiotherapy for local-control indications. There is no glomus-tumor-specific standard chemotherapy regimen; anthracycline-based soft-tissue-sarcoma therapy, pazopanib, or other agents may be considered case by case, with limited evidence.

Molecularly selected targeted therapy is investigational. **NCT03422679** evaluated oral **CB-103**, a pan-NOTCH pathway inhibitor, in a phase I/IIA open-label basket study. Eligibility explicitly included surgically unresectable, locally advanced, or metastatic malignant glomus tumor after systemic therapy, or another cancer with a confirmed NOTCH1–4 activating lesion. The study enrolled 79 participants overall, used 28-day cycles, and assessed dose-limiting toxicity and objective response. It was terminated for a **business reason**, not because the registry established inefficacy; results were posted January 16, 2024. [ClinicalTrials.gov NCT03422679](https://clinicaltrials.gov/study/NCT03422679). (NCT03422679 chunk 1, NCT03422679 chunk 2)

The linked phase I publication is Hanna et al., *Cancer Research Communications*, September 14, 2023, PMID **37712875**, DOI: [10.1158/2767-9764.CRC-23-0333](https://doi.org/10.1158/2767-9764.CRC-23-0333). The available registry does not provide a glomus-tumor-specific response rate; basket-level outcomes must not be attributed to this rare subgroup. (NCT03422679 chunk 2)

There is no established pharmacogenomic dosing guideline, approved gene/cell/RNA therapy, or proven checkpoint inhibitor strategy.

## 13. Prevention

No primary prevention, vaccine, prophylactic medication, or environmental intervention is available. Population, newborn, and carrier screening are not recommended.

Secondary prevention consists of early recognition and complete removal of symptomatic lesions. Individuals with NF1 should be educated to report focal digital pain, cold sensitivity, or nail changes. The ERN GENTURIS guideline recommends broad adult NF1 clinical assessment at least every three years and identifies digital glomus tumor as an adult risk, although it does not recommend routine imaging specifically for asymptomatic digits. (carton2023erngenturistumour pages 7-8)

Tertiary prevention includes complete excision, pathology review of atypical lesions, re-excision when margins are clinically concerning, and surveillance for malignant or recurrent disease. Genetic counseling is appropriate for NF1 or suspected GLMN-associated familial disease.

## 14. Other species and natural disease

Sporadic glomus-cell tumors have been reported rarely in companion animals, including cats and dogs, but available evidence consists primarily of isolated pathology reports. No breed predisposition, incidence, zoonotic potential, transmission pathway, or validated cross-species susceptibility estimate is established. Human NOTCH, NF1, BRAF, and GLMN pathways are evolutionarily conserved, but conservation alone does not establish an equivalent animal syndrome.

Suggested taxa for future curation are **Homo sapiens, NCBI Taxon 9606; Canis lupus familiaris, 9615; Felis catus, 9685; Mus musculus, 10090**. Veterinary cases are noninfectious and have no zoonotic significance.

## 15. Model organisms

No widely adopted disease-specific genetically engineered mouse, rat, zebrafish, organoid, or patient-derived xenograft model was identified. Existing mechanistic interpretation relies mainly on human tumor sequencing and general vascular-NOTCH models. The vascular review establishes that NOTCH regulates vessel development, branching, identity, and homeostasis, but these experiments are pathway models rather than faithful glomus-tumor models. (gaudio2022notchsignallingin pages 10-11)

Priority models would include conditional expression of a MIR143–NOTCH fusion in mural-cell lineages such as **PDGFRB-, CSPG4-, or ACTA2-expressing cells**, NF1 loss in the same compartment, and patient-derived cultures or xenografts from malignant disease. Required validation should include perivascular rounded-cell morphology, SMA/h-caldesmon expression, vascular architecture, pain-related innervation, metastatic behavior where applicable, and reversibility with NOTCH inhibition.

## Current understanding and key gaps

The contemporary model is that glomus tumor is a usually benign pericytic neoplasm in which recurrent **MIR143–NOTCH fusions—reported in almost 50%—provide the clearest molecular driver**, with NF1 representing the best-established inherited susceptibility context. (gaudio2022notchsignallingin pages 10-11, mertens2016genefusionsin pages 19-20, carton2023erngenturistumour pages 7-8) Clinical practice remains dominated by recognition and complete excision. The main 2023–2024 translational development was molecular selection of malignant glomus tumors for NOTCH inhibition, although no subgroup efficacy estimate or approved targeted therapy has emerged. (NCT03422679 chunk 1, NCT03422679 chunk 2)

High-priority gaps are population-based epidemiology, standardized HPO frequencies and quality-of-life measures, prospective recurrence and survival cohorts, harmonized malignant-risk criteria, validated prognostic biomarkers, single-cell/spatial profiling, and disease-specific experimental models. Ontology curation should preserve the boundary between soft-tissue glomus tumor, GLMN-associated glomuvenous malformation, and head-and-neck paraganglioma.

References

1. (NCT03422679 chunk 1):  Study of CB-103 in Adult Patients With Advanced or Metastatic Solid Tumours and Haematological Malignancies. Cellestia Biotech AG. 2017. ClinicalTrials.gov Identifier: NCT03422679

2. (NCT03422679 chunk 2):  Study of CB-103 in Adult Patients With Advanced or Metastatic Solid Tumours and Haematological Malignancies. Cellestia Biotech AG. 2017. ClinicalTrials.gov Identifier: NCT03422679

3. (gaudio2022notchsignallingin pages 10-11): Francesca Del Gaudio, Dongli Liu, and Urban Lendahl. Notch signalling in healthy and diseased vasculature. Open Biology, Apr 2022. URL: https://doi.org/10.1098/rsob.220004, doi:10.1098/rsob.220004. This article has 68 citations and is from a peer-reviewed journal.

4. (carton2023erngenturistumour pages 7-8): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 123 citations and is from a peer-reviewed journal.

5. (agaram2019gli1amplificationsexpandthe pages 1-2): Narasimhan P. Agaram, Lei Zhang, Yun-Shao Sung, Samuel Singer, Todd Stevens, Carlos N. Prieto-Granada, Justin A. Bishop, Benjamin A. Wood, David Swanson, Brendan C. Dickson, and Cristina R. Antonescu. Gli1-amplifications expand the spectrum of soft tissue neoplasms defined by gli1 gene fusions. Modern Pathology, 32:1617-1626, Nov 2019. URL: https://doi.org/10.1038/s41379-019-0293-x, doi:10.1038/s41379-019-0293-x. This article has 117 citations and is from a domain leading peer-reviewed journal.

6. (mertens2016genefusionsin pages 19-20): Fredrik Mertens, Cristina R. Antonescu, and Felix Mitelman. Gene fusions in soft tissue tumors: recurrent and overlapping pathogenetic themes. Genes, 55:291-310, Apr 2016. URL: https://doi.org/10.1002/gcc.22335, doi:10.1002/gcc.22335. This article has 165 citations.

7. (agaram2019gli1amplificationsexpandthe pages 2-4): Narasimhan P. Agaram, Lei Zhang, Yun-Shao Sung, Samuel Singer, Todd Stevens, Carlos N. Prieto-Granada, Justin A. Bishop, Benjamin A. Wood, David Swanson, Brendan C. Dickson, and Cristina R. Antonescu. Gli1-amplifications expand the spectrum of soft tissue neoplasms defined by gli1 gene fusions. Modern Pathology, 32:1617-1626, Nov 2019. URL: https://doi.org/10.1038/s41379-019-0293-x, doi:10.1038/s41379-019-0293-x. This article has 117 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Glomus_Tumor-deep-research-falcon_artifacts/artifact-00.md)