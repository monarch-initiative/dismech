---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T23:37:33.829448'
end_time: '2026-07-30T23:49:55.631084'
duration_seconds: 741.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Blepharophimosis-Intellectual Disability Syndrome, MKB Type
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Blepharophimosis_Intellectual_Disability_Syndrome_MKB_Type-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blepharophimosis-Intellectual Disability Syndrome, MKB Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Blepharophimosis-Intellectual Disability Syndrome, MKB Type** covering all of the
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
- **Disease Name:** Blepharophimosis-Intellectual Disability Syndrome, MKB Type
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Blepharophimosis-Intellectual Disability Syndrome, MKB Type** covering all of the
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


# Blepharophimosis–Intellectual Disability Syndrome, MKB Type

## Executive summary

Blepharophimosis–intellectual disability syndrome, MKB type is the **Maat–Kievit–Brunner form of X-linked Ohdo syndrome** (OSMKB/XLOS), an exceptionally rare congenital neurodevelopmental disorder caused by pathogenic variants in **MED12**, an X-chromosomal regulator of RNA-polymerase-II-dependent transcription. The defining combination is intellectual/developmental disability with blepharophimosis, ptosis, a small or narrow mouth, characteristic nose, and age-dependent facial coarsening. Congenital cardiac, palatal, auditory, genital, growth, and musculoskeletal abnormalities are variably present. Most classically affected individuals are hemizygous males; heterozygous females are often unaffected but can manifest MED12-related disease depending on variant class and X-chromosome inactivation. No disease-modifying treatment or OSMKB-specific interventional trial was identified. Evidence remains dominated by individual families and small case series, so prevalence, penetrance, phenotype frequencies, survival, and formal management standards are unknown. (graham2013med12relateddisorders pages 3-5, rocchetti2021med12mutationin pages 5-7, silfhout2013mutationsinmed12 pages 1-2, li2021denovolossoffunction pages 1-2)

The following table gives a curation-oriented synopsis.

| Domain | High-confidence finding | Suggested ontology identifiers/terms | Evidence level or caveat |
|---|---|---|---|
| Identity / identifiers | Disease corresponds to X-linked Ohdo syndrome, Maat-Kievit-Brunner type; also called blepharophimosis-intellectual disability syndrome, MKB type. Supported identifiers include OMIM 300895 and Orphanet 293707. | OMIM: 300895; Orphanet: 293707; MONDO: not confirmed from retrieved evidence | Strong disease-entity resolution from human genetics/review sources; MONDO ID not established here. (OpenTargets Search: Blepharophimosis-intellectual disability syndrome, MKB type, graham2013med12relateddisorders pages 3-5, silfhout2013mutationsinmed12 pages 1-2) |
| Causal gene and inheritance | Causal gene is MED12 on the X chromosome; inheritance is primarily X-linked, with affected hemizygous males and carrier/occasionally affected females depending on variant class and X-inactivation context. | MED12; inheritance: X-linked recessive / X-linked dominant-like female presentations for some de novo variants | Strong for male X-linked OSMKB; female disease expression is better established for broader MED12-related disorders than classic OSMKB. (silfhout2013mutationsinmed12 pages 1-2, rocchetti2021med12mutationin pages 7-8, li2021denovolossoffunction pages 1-2) |
| Established variants | Human OSMKB-associated MED12 missense variants reported include p.Arg1148His, p.Ser1165Pro, p.His1729Asn, and p.Arg296Gln. | Sequence variant classes: missense_variant | Strong for these reported families; not a complete catalog. (graham2013med12relateddisorders pages 3-5, silfhout2013mutationsinmed12 pages 1-2, rocchetti2021med12mutationin pages 5-7) |
| Core phenotype | Core syndrome combines congenital craniofacial anomalies and neurodevelopmental impairment: blepharophimosis, ptosis, round/coarsening face, characteristic nose with thick alae nasi, narrow/small mouth, long philtrum, micrognathia/retrognathia, intellectual disability, psychomotor delay, and severe speech impairment/limited expressive language. | HPO: Blepharophimosis, Ptosis, Intellectual disability, Global developmental delay, Speech delay, Long philtrum, Micrognathia, Retrognathia, Small mouth | Strong, repeatedly described across foundational and follow-up families; exact frequencies usually unavailable because cohorts are very small. (silfhout2013mutationsinmed12 pages 1-2, rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7) |
| Variable organ findings | Additional variable findings include congenital heart disease (VSD, ASD, tetralogy of Fallot), cleft palate, hearing loss, abnormal ears, inguinal hernia, short stature, genital anomalies, sialorrhea, and mobility limitations. | HPO: Ventricular septal defect, Atrial septal defect, Tetralogy of Fallot, Cleft palate, Hearing impairment, Inguinal hernia, Short stature, Genital abnormality | Moderate: documented in specific families/cases, variable expressivity likely high. (rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7) |
| Natural history / temporal pattern | Onset is congenital or early childhood; disability is lifelong. Facial appearance may evolve with age toward coarse features, thick alae nasi, and triangular face in older males. | HPO: Congenital onset; Progressive facial coarsening (descriptive) | Moderate: age-related facial progression is noted, but formal longitudinal natural-history data are sparse. (graham2013med12relateddisorders pages 3-5, silfhout2013mutationsinmed12 pages 1-2) |
| Mechanism | MED12 is a Mediator kinase-module subunit regulating RNA polymerase II transcription. Direct OSMKB evidence shows impaired REST-mediated repression without loss of Mediator incorporation; broader MED12 studies implicate dysregulated immediate-early genes, enhancer/super-enhancer control, neural stem-cell adhesion/cell-cycle programs, and Wnt/Wnt-PCP developmental signaling. | GO: regulation of transcription by RNA polymerase II; chromatin organization; cell cycle G1/S transition; Wnt signaling pathway; CL: neural stem cell | Strong for MED12 pathway involvement; direct OSMKB mechanistic evidence is strongest for REST-related repression, while Wnt/NSC findings are from broader Med12 models. (silfhout2013mutationsinmed12 pages 4-5, plassche2021med12related(neuro)developmentaldisorders pages 6-7, kim2016mediatorsubunitmed12 pages 1-2, donnio2017med12relatedxliddisorders pages 10-14) |
| Diagnostics | Diagnosis in reported cases relied on exome sequencing with Sanger confirmation after nondiagnostic conventional testing (e.g., normal karyotype, negative fragile X testing in one report). Clinical suspicion arises from blepharophimosis-plus-intellectual-disability phenotype with X-linked family history. | Genetic testing: WES; single-gene MED12 analysis; family segregation testing | Strong for sequencing utility; no disease-specific formal diagnostic criteria were retrieved. (rocchetti2021med12mutationin pages 2-4, rocchetti2021med12mutationin pages 7-8) |
| Treatment / management | No disease-modifying therapy was identified. Current care is supportive and anomaly-directed: developmental/rehabilitative support, speech support, ophthalmologic and craniofacial evaluation, cardiac assessment and surgical repair when needed, and management of associated congenital anomalies. | MAXO: supportive care; speech therapy; cardiac surgery; ophthalmologic evaluation | Moderate: based mainly on case management rather than trials or guidelines. (rocchetti2021med12mutationin pages 5-7, rocchetti2021med12mutationin pages 7-8) |
| Epidemiology / prognosis | Extremely rare Mendelian disorder; no robust prevalence, incidence, survival, or life-expectancy estimates were found in retrieved sources. Morbidity is dominated by persistent intellectual/developmental disability and congenital anomaly burden. | Orphan disease; epidemiology unavailable | High-confidence evidence gap: rarity and small family-based literature preclude precise estimates. (graham2013med12relateddisorders pages 3-5, rocchetti2021med12mutationin pages 7-8) |
| Models | Relevant models include patient/family cellular studies, patient-derived iPSC neural models, mouse embryonic and neural stem-cell Med12 perturbation models, and zebrafish developmental models. These support roles in neural development, cell-cycle control, adhesion, and Wnt-related morphogenesis. | CL: neural stem cell; model systems: mouse, zebrafish, iPSC-derived neural cells | Strong for general MED12 biology; only some model findings are variant-specific to OSMKB. (shaw2025functionalcharacterizationof pages 9-11, kim2016mediatorsubunitmed12 pages 1-2, plassche2021med12related(neuro)developmentaldisorders pages 6-7) |
| Trials / real-world research | No OSMKB- or MED12-specific interventional trial was found. NCT04463316 is a recruiting observational rare-syndrome adult cohort at Erasmus MC (target enrollment 600) and does not explicitly list OSMKB/MED12. | ClinicalTrials.gov: NCT04463316 | Strong for absence of syndrome-specific trial in retrieved search; registry inclusion of OSMKB is unconfirmed. (NCT04463316 chunk 1) |
| Major evidence gaps | Missing or limited: MONDO confirmation, phenotype frequencies, penetrance, carrier frequency, prevalence/incidence, survival, standardized surveillance guidelines, biomarker studies, proteomics/metabolomics, single-cell/spatial omics, and controlled treatment outcome data. | Knowledge gap annotation | High-confidence gaps based on absence across retrieved literature and registry data. (plassche2021med12related(neuro)developmentaldisorders pages 11-13, rocchetti2021med12mutationin pages 7-8, NCT04463316 chunk 1) |


*Table: This compact table summarizes high-confidence disease knowledge for blepharophimosis-intellectual disability syndrome, MKB type / X-linked Ohdo syndrome, emphasizing what is established versus what remains uncertain. It is useful as a quick-reference scaffold for database curation and evidence-gap tracking.*

## 1. Disease information

### Definition and classification

OSMKB is a **Mendelian, X-linked syndromic intellectual-developmental disorder**. It belongs to the clinically heterogeneous blepharophimosis–intellectual-disability/Ohdo-syndrome group and to the broader spectrum of MED12-related developmental disorders. The causal relationship was established by exome sequencing in the landmark 2013 *American Journal of Human Genetics* study, which examined two multiplex families and nine additional simplex males. (silfhout2013mutationsinmed12 pages 1-2)

**Synonyms** include:

- X-linked Ohdo syndrome;
- Ohdo syndrome, Maat–Kievit–Brunner type;
- OSMKB syndrome;
- MKB syndrome;
- blepharophimosis–intellectual disability syndrome, MKB type;
- X-linked blepharophimosis–intellectual disability syndrome.

**Identifiers and cross-references**

- **OMIM phenotype:** **300895**.
- **Orphanet:** **ORPHA:293707**.
- **Causal target:** MED12, Ensembl **ENSG00000184634**; Open Targets reports MED12 as the sole associated target, with an association score of approximately 0.768. (OpenTargets Search: Blepharophimosis-intellectual disability syndrome, MKB type)
- **MONDO:** no disease-specific MONDO identifier was confirmed in the retrieved evidence; it should therefore remain unresolved rather than inferred.
- **ICD-10/ICD-11 and MeSH:** no dedicated disease-specific code or descriptor was confirmed. In practice, coding will generally use broader congenital-malformation and intellectual-disability categories.

This report synthesizes **aggregated disease-level resources and published family/case data**, not individual EHR records. The clinical evidence is nevertheless patient-level at origin because almost all publications describe single pedigrees or very small cohorts.

**Foundational citation:** Vulto-van Silfhout et al., “Mutations in MED12 cause X-linked Ohdo syndrome,” published February 7, 2013/March 2013, DOI: [10.1016/j.ajhg.2013.01.007](https://doi.org/10.1016/j.ajhg.2013.01.007), **PMID: 23395478**. Its central finding can be quoted concisely as: **“Mutations in MED12 cause X-linked Ohdo syndrome.”** (silfhout2013mutationsinmed12 pages 1-2, silfhout2013mutationsinmed12 pages 4-5)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The disease is genetic. Pathogenic **germline MED12 variants** alter a subunit of the Mediator complex, which couples transcription factors and regulatory elements to RNA polymerase II. Classic OSMKB was initially associated with hemizygous missense variants in males. No infectious, toxic, nutritional, occupational, or lifestyle cause has been demonstrated. (silfhout2013mutationsinmed12 pages 1-2, silfhout2013mutationsinmed12 pages 4-5)

### Risk factors

The principal risk factor is inheritance of a pathogenic maternal MED12 allele or, less commonly, a de novo pathogenic variant. For a heterozygous carrier mother, the conventional X-linked recurrence framework is a 50% probability of transmitting the allele in each pregnancy; sex and X-inactivation strongly influence the resulting phenotype. The 2021 family study demonstrated hemizygous affected boys and heterozygous, clinically unaffected mothers. (rocchetti2021med12mutationin pages 5-7)

Female expression is not adequately described by a simple recessive model. Broader MED12 literature shows that heterozygous females may be affected by de novo missense or truncating variants and that unfavorable X-inactivation can influence severity. Extremely skewed X-inactivation was found in all informative females in a Hardikar-syndrome cohort, while a later MED12 p.Arg1138Trp series reported random, 85%, and 98% skewing in different affected females. These observations are relevant to counseling but are not equivalent to penetrance estimates for classic OSMKB. (li2021denovolossoffunction pages 1-2, shaw2025functionalcharacterizationof pages 8-9)

### Protective factors and gene–environment interactions

No protective MED12 allele, modifier gene, diet, behavior, medication, or environmental intervention is known to reduce OSMKB occurrence or severity. No OSMKB-specific gene–environment interaction has been demonstrated. Environmental teratogens can phenocopy portions of the craniofacial/developmental presentation, but that does not establish interaction with MED12.

## 3. Phenotypes

The evidence base is too small for reliable percentages. Features below are therefore labeled **core**, **recurrent**, or **case-specific**, rather than assigned misleading frequencies.

### Core/recurrent phenotypes

- **Intellectual disability**, generally moderate to severe in the 2021 cases; **global/psychomotor developmental delay** and markedly delayed or limited expressive language are central functional impairments. Suggested terms: **HP:0001249 Intellectual disability**, **HP:0001263 Global developmental delay**, **HP:0000750 Delayed speech and language development**, **HP:0001344 Absent speech** where applicable. (rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7)
- **Blepharophimosis** and **ptosis**, congenital craniofacial signs and the syndrome’s most recognizable diagnostic clues. Suggested terms: **HP:0000581 Blepharophimosis**, **HP:0000508 Ptosis**. (graham2013med12relateddisorders pages 3-5, silfhout2013mutationsinmed12 pages 1-2)
- A characteristic facial gestalt comprising a round face in younger children, thick or arched eyebrows, characteristic/beaked nose, thick alae nasi, long or flat philtrum, small/narrow mouth, and micrognathia or retrognathia. Suggested terms include **HP:0002553 Highly arched eyebrow**, **HP:0000343 Long philtrum**, **HP:0000160 Narrow mouth**, **HP:0000347 Micrognathia**, and **HP:0000278 Retrognathia**. (rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7)
- **Age-dependent facial evolution:** younger males resemble other Ohdo phenotypes; older males may develop coarser features, prominent/thick alae nasi, and a triangular face. This is the clearest documented progressive component. Neurodevelopmental disability itself is chronic rather than episodic. (graham2013med12relateddisorders pages 3-5, silfhout2013mutationsinmed12 pages 1-2)

### Variable findings

- **Congenital heart disease:** VSD/ASD in one 2021 proband and tetralogy of Fallot in the other; both underwent surgical correction. Suggested terms: **HP:0001629 Ventricular septal defect**, **HP:0001631 Atrial septal defect**, **HP:0001636 Tetralogy of Fallot**. These observations show association but do not establish population frequency. (rocchetti2021med12mutationin pages 5-7)
- **Cleft palate**, reported in one of the two 2021 boys: **HP:0000175**. (rocchetti2021med12mutationin pages 5-7)
- **Hearing impairment**, described within the recognized syndrome phenotype, although patient-specific audiometric data were not supplied in the retrieved cohort excerpt: **HP:0000365**. (rocchetti2021med12mutationin pages 5-7)
- **Short stature**, abnormal external ears, brachycephaly, inguinal hernia, genital abnormalities, sialorrhea, and restricted mobility are variable. Suggested terms include **HP:0004322 Short stature**, **HP:0000238 Brachycephaly**, **HP:0000023 Inguinal hernia**, and **HP:0002307 Drooling**. (rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7)
- Corpus-callosum dysgenesis and imperforate anus were **absent** in the two 2021 probands, illustrating that findings from other MED12 disorders should not automatically be assigned to OSMKB. (rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7)

### Onset, severity, progression, and quality of life

Craniofacial and structural anomalies are congenital. Developmental and speech delays become evident in infancy or early childhood. Severity is variable even among individuals carrying the same p.Arg296Gln allele. One seven-year-old could not walk spontaneously and had substantial difficulty with activities of daily living, while the broader cohort showed moderate-to-severe intellectual disability and limited expressive communication. The likely quality-of-life burden includes dependence for education and daily care, communication impairment, mobility limitation in severe cases, and repeated specialty or surgical care for congenital anomalies. No validated EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was found. (rocchetti2021med12mutationin pages 7-8, rocchetti2021med12mutationin pages 5-7)

## 4. Genetic and molecular information

### Gene and protein

**MED12** lies at **Xq13.1/Xq13** and encodes mediator complex subunit 12. It is part of the Mediator kinase module and is required for context-dependent transcriptional regulation. The retrieved Open Targets evidence recognizes MED12 as the only associated target for ORPHA:293707. (OpenTargets Search: Blepharophimosis-intellectual disability syndrome, MKB type, graham2013med12relateddisorders pages 1-2, fazio2025geneticclinicaland pages 6-8)

Suggested annotations include **HGNC symbol MED12**, GO **regulation of transcription by RNA polymerase II**, **Mediator complex**, **chromatin organization**, and **transcription regulatory region binding**. Exact GO accessions should be validated against the current GO release before database loading.

### Reported pathogenic/likely pathogenic OSMKB variants

| Variant | Type/origin | Evidence |
|---|---|---|
| c.3443G>A, p.Arg1148His | Hemizygous missense, germline | Foundational OSMKB family; functional impairment of REST-element recruitment. |
| c.3493T>C, p.Ser1165Pro | Hemizygous missense, germline | Foundational OSMKB family; functional impairment of REST-element recruitment. |
| c.5185C>A, p.His1729Asn | Hemizygous missense, germline | Foundational OSMKB family. |
| c.887G>A, p.Arg296Gln | Hemizygous missense in affected boys; heterozygous in carrier mothers | Reported in two first cousins and earlier unrelated cases; absent from gnomAD in the 2021 analysis and classified there as likely pathogenic in ClinVar. |

(graham2013med12relateddisorders pages 3-5, rocchetti2021med12mutationin pages 5-7, silfhout2013mutationsinmed12 pages 1-2, silfhout2013mutationsinmed12 pages 4-5)

The p.Arg296Gln recurrence demonstrates substantial intrafamilial and interfamilial variable expressivity. The evidence does **not** support a single reliable genotype–phenotype rule. (rocchetti2021med12mutationin pages 7-8)

The classic variants are germline, not somatic. No founder effect, carrier frequency, anticipation, confirmed germline mosaicism rate, or protective modifier has been established. Large MED12 copy-number changes and truncating variants can cause other MED12 phenotypes, but they should not be conflated with classic missense-associated OSMKB.

### Epigenetics and chromosomal abnormalities

Direct functional work implicates failure of chromatin-associated REST repression. Broader MED12 research shows participation in enhancer/super-enhancer maintenance; MED12 loss can reduce super-enhancer-driven expression by approximately 50%. A blood DNA-methylation study of nine individuals with FG syndrome did not identify a specific signature, but that negative result is not OSMKB-specific. (plassche2021med12related(neuro)developmentaldisorders pages 6-7, plassche2021med12related(neuro)developmentaldisorders pages 11-13)

A 2024 study reported overlapping phenotype and episignature between blepharophimosis with intellectual disability and Helsmoortel–Van der Aa syndrome (DOI: [10.1002/ajmg.c.32089](https://doi.org/10.1002/ajmg.c.32089), June 2024), but its full text was unavailable in this retrieval; consequently, detailed claims from it are not used here.

No recurrent OSMKB-defining aneuploidy, translocation, or inversion was found.

## 5. Environmental, lifestyle, and infectious information

OSMKB is not an infectious, toxic, radiation-associated, occupational, dietary, or lifestyle-mediated disease. Smoking, alcohol, exercise, and nutrition have not been shown to modify penetrance. Routine healthy lifestyle measures remain appropriate for general health but are not primary prevention for this Mendelian disorder. No pathogen, zoonotic route, or transmissible mechanism applies.

## 6. Mechanism and pathophysiology

### Evidence-graded causal chain

1. **Upstream genetic lesion:** a pathogenic MED12 allele alters the MED12 protein within the Mediator transcriptional apparatus.
2. **Direct transcriptional defect:** p.Arg1148His and p.Ser1165Pro did not prevent incorporation into Mediator or interaction with the histone methyltransferase G9a; instead, they impaired recruitment of Mediator to REST-bound RE1 elements and thereby weakened repression of neuronal targets including **CHRM4, SNAP25, and SYN1**. (silfhout2013mutationsinmed12 pages 4-5)
3. **Broader regulatory dyscontrol:** seven MED12 XLID variants produced variant-specific, dose-dependent abnormalities in immediate-early genes such as **JUN, FOS, and EGR1**, with altered RNA polymerase II/MED12 promoter recruitment and downstream effects on late-response genes. (donnio2017med12relatedxliddisorders pages 10-14)
4. **Cellular-developmental consequences:** Med12 depletion in mouse neural stem cells changed 240 transcripts—177 increased and 73 decreased—enhanced adhesion through genes including **Sdc2**, reduced G1/S regulators, caused a G1/S block, and markedly impaired proliferation without evidence of apoptosis. This supports disturbed balance between neural-stem-cell self-renewal and differentiation. (kim2016mediatorsubunitmed12 pages 1-2)
5. **Developmental pathway disruption:** mouse and zebrafish evidence implicates canonical **Wnt/β-catenin**, Wnt/planar-cell-polarity, neural-tube, hindbrain, neural-crest, and endoderm development. These models explain biological plausibility for neurodevelopmental, craniofacial, cardiac, and other congenital abnormalities, but whole-gene depletion is more severe and not equivalent to an OSMKB missense allele. (plassche2021med12related(neuro)developmentaldisorders pages 6-7, kim2016mediatorsubunitmed12 pages 1-2)
6. **Clinical manifestations:** altered neurogenesis and neuronal gene regulation plausibly produce intellectual disability, severe speech delay, and motor impairment; disturbed craniofacial and organogenesis programs plausibly produce blepharophimosis, ptosis, jaw/palatal anomalies, and variable heart defects.

### Recent functional development

A 2025 patient-derived iPSC study of MED12 p.Arg1138Trp—slightly beyond the requested 2023–2024 priority window—found 51 differentially expressed genes at day 24 of neural differentiation, including reduced **TBR1, EMX1, DMRTA2, PEG3, ZIM2**, and **ZFP3**. It implicated RNA-polymerase-II regulation, delayed forebrain/axon/neural-cell specification, pre-ribosome pathways, and altered MED12/MED12L balance. This is important modern human-neural-model evidence, but p.Arg1138Trp has had variable clinical classification and is not one of the original classic OSMKB alleles. DOI: [10.1186/s10020-025-01365-5](https://doi.org/10.1186/s10020-025-01365-5), September 2025. (shaw2025functionalcharacterizationof pages 9-11, shaw2025functionalcharacterizationof pages 8-9)

### Ontology suggestions

- **Biological processes:** regulation of transcription by RNA polymerase II; chromatin-mediated gene regulation; canonical Wnt signaling; planar-cell-polarity pathway; neural-tube closure; neural-crest development; forebrain development; axon development; stem-cell proliferation; G1/S transition; cell adhesion.
- **Cell types:** neural stem cell, neural progenitor cell, neuron, neural-crest cell, craniofacial mesenchymal cell, cardiomyocyte/cardiac progenitor. Suggested CL concepts should be validated against the current Cell Ontology.
- **Subcellular components:** nucleus, chromatin, Mediator complex, transcription regulator complex.

No OSMKB-specific immune, inflammatory, metabolic, mitochondrial, lipidomic, proteomic, metabolomic, single-cell, spatial-transcriptomic, or CRISPR-screen signature was found.

## 7. Anatomical structures affected

### Primary systems

- **Nervous system:** developing brain and neural circuits, clinically expressed as intellectual disability, speech/language impairment, psychomotor delay, and sometimes severe mobility limitation. Suggested UBERON concepts: brain, forebrain, nervous system. (rocchetti2021med12mutationin pages 7-8, shaw2025functionalcharacterizationof pages 9-11)
- **Eye/adnexal and craniofacial structures:** bilateral palpebral fissures/eyelids, nose, philtrum, mouth, mandible, external ear, and occasionally palate. Blepharophimosis and ptosis are generally bilateral syndromic findings. Suggested UBERON concepts: eyelid, palpebral fissure, nose, mandible, palate, external ear. (graham2013med12relateddisorders pages 3-5, rocchetti2021med12mutationin pages 7-8)

### Secondary/variable systems

The heart and great-vessel developmental system, genitourinary tract, auditory system, skeleton/growth axis, and inguinal region can be involved. The 2021 cases specifically documented septal defects and tetralogy of Fallot. (rocchetti2021med12mutationin pages 5-7)

At tissue/cell level, the strongest experimental candidates are neural progenitors, neurons, neural-crest-derived craniofacial mesenchyme, and embryonic cardiac/developmental cell populations. At subcellular level, dysfunction centers on the **nucleus**, chromatin, and Mediator/RNA-polymerase-II transcriptional machinery.

## 8. Temporal development and natural history

Onset is **prenatal/congenital**, although intellectual and speech impairment becomes clinically recognizable during infancy or childhood. The course is chronic and lifelong. There is no evidence for acute attacks, relapsing-remitting disease, or spontaneous remission. Facial morphology evolves with age toward coarsening, thick alae nasi, and a more triangular configuration. (graham2013med12relateddisorders pages 3-5, silfhout2013mutationsinmed12 pages 1-2)

No validated disease stages or progression-rate model exists. Critical biological vulnerability is presumed to be embryonic organogenesis and early neural development, making early developmental assessment and treatment of vision, hearing, cardiac, feeding, and communication problems the practical window for reducing secondary disability.

## 9. Inheritance, epidemiology, and population

Classic OSMKB has an **X-linked** inheritance pattern. The original report identified affected males in multiplex families, and the 2021 study demonstrated hemizygous affected boys with heterozygous carrier mothers. (rocchetti2021med12mutationin pages 5-7, silfhout2013mutationsinmed12 pages 1-2)

Penetrance in hemizygous males is presumed high for well-established pathogenic alleles, but it has not been quantified. Expressivity is clearly variable. Anticipation is not reported. Female penetrance depends on variant class and X-inactivation, but no OSMKB-specific estimate exists. (rocchetti2021med12mutationin pages 7-8, li2021denovolossoffunction pages 1-2)

The disease is **ultra-rare**. No defensible prevalence, incidence, carrier-frequency, sex-ratio, ethnic enrichment, founder mutation, or geographic distribution estimate was found. Published families from different populations and a 2024 conference report of a first Hispanic case argue against restriction to one ancestry, but case reporting cannot establish demographic rates.

## 10. Diagnostics

### Clinical suspicion and confirmation

Suspect OSMKB in a child—especially a boy—with blepharophimosis/ptosis plus developmental or intellectual disability, severe language delay, characteristic small mouth/nose/mandibular features, and an X-linked pedigree. Molecular confirmation is required because the facial gestalt overlaps other syndromes.

A practical testing sequence is:

1. **Trio whole-exome sequencing or genome sequencing**, or a comprehensive neurodevelopmental/blepharophimosis panel containing MED12.
2. Confirm the variant by an orthogonal method where required and perform **maternal/parental segregation testing**.
3. Apply ACMG/AMP criteria using population frequency, inheritance/de novo status, computational evidence, functional data, and phenotype specificity.
4. If sequencing is negative, assess exon-level CNVs and consider CMA/WGS for structural variants and alternative diagnoses.

The 2021 cases were diagnosed by WES followed by Sanger confirmation; prior karyotype and fragile-X testing were normal/negative. (rocchetti2021med12mutationin pages 2-4, rocchetti2021med12mutationin pages 7-8)

Karyotyping, FISH, mitochondrial sequencing, repeat-expansion testing, biopsy, and biochemical enzyme assays are not first-line OSMKB tests unless another diagnosis is suspected. No diagnostic blood protein, metabolite, liquid-biopsy, EEG, or imaging biomarker is validated.

### Baseline clinical assessment

Reasonable phenotype-directed evaluation includes developmental and neurologic examination; formal speech/language, hearing, and ophthalmologic assessment; echocardiography; growth and feeding review; examination for palate, genital, hernia, and skeletal abnormalities; and brain MRI or EEG only when neurologic findings indicate. This is expert extrapolation from the reported anomaly spectrum, not a society-approved OSMKB guideline.

### Differential diagnosis

Important alternatives include:

- **Ohdo syndrome, SBBYS type/KAT6B disorder:** often includes patellar, genital, dental, thyroid, and long-thumb/great-toe abnormalities.
- **Say–Barber–Biesecker–Young–Simpson and Genitopatellar syndromes:** KAT6B-related spectrum.
- **Helsmoortel–Van der Aa syndrome:** ADNP-related, with overlapping intellectual disability and facial/eyelid phenotype; recent methylation research suggests overlap.
- **Other MED12 disorders:** FG/Opitz–Kaveggia syndrome, Lujan–Fryns syndrome, nonspecific MED12-related ID, and female-limited Hardikar syndrome.
- **BPES due to FOXL2:** prominent blepharophimosis/ptosis but generally without the characteristic syndromic intellectual-disability phenotype.
- Kabuki, Wiedemann–Steiner, Cornelia de Lange, and other chromatin/transcription disorders.

## 11. Outcome and prognosis

No five- or ten-year survival rate, mortality rate, disease-specific cause-of-death series, or life-expectancy estimate exists. Published individuals surviving through childhood and adolescence show that the condition is not uniformly lethal, but available cohorts are too small for survival inference. (silfhout2013mutationsinmed12 pages 1-2)

Morbidity is driven by lifelong cognitive, language, educational, and adaptive-function impairment, with additional burden from mobility limitation and surgically significant congenital heart or palatal disease in some individuals. Cardiac defects in both 2021 probands were surgically corrected. (rocchetti2021med12mutationin pages 5-7)

Recovery of the underlying neurodevelopmental disorder is not expected; functional gains are possible through early therapies and correction of treatable comorbidities. No validated prognostic biomarker or model exists. Variant identity alone is insufficient because the same p.Arg296Gln change produced variable phenotypes. (rocchetti2021med12mutationin pages 7-8)

## 12. Treatment and real-world implementation

There is no approved MED12-targeted, gene-replacement, gene-editing, RNA, cell, or pharmacologic disease-modifying therapy for OSMKB. Management is individualized and multidisciplinary:

- early developmental intervention, special education, speech/language therapy, augmentative communication, occupational therapy, and physical therapy;
- ophthalmology/oculoplastic evaluation for ptosis or visual-axis compromise, with surgery when clinically indicated;
- audiology and hearing support;
- cardiology evaluation and surgical/interventional correction of significant congenital heart disease;
- craniofacial/ENT management of cleft palate, airway, feeding, and speech consequences;
- treatment of hernia, genital, orthopedic, nutritional, gastrointestinal, sleep, or behavioral problems as present;
- psychosocial and respite support for families.

Suggested MAXO concepts include **genetic counseling**, **molecular genetic testing**, **developmental assessment**, **speech therapy**, **occupational therapy**, **physical therapy**, **hearing evaluation**, **ophthalmologic examination**, **echocardiography**, **ptosis repair**, **cleft-palate repair**, and **cardiac surgery**. Exact MAXO identifiers should be validated against the current ontology release.

No response rates, controlled adverse-event data, pharmacogenomic recommendations, or treatment algorithm specific to OSMKB are available.

### Clinical trials

No OSMKB- or MED12-specific interventional trial was found. **NCT04463316**, “GROWing Up With Rare GENEtic Syndromes,” is a recruiting, non-interventional retrospective cohort at Erasmus Medical Center, Rotterdam. It plans approximately 600 adults aged 18 years or older, began in October 2018, and has estimated completion in January 2030. It evaluates medical history, laboratory values, physical/psychological complaints, and medication use across more than 30 rare syndromes; MED12/OSMKB was not explicitly listed in the retrieved registry text. [ClinicalTrials.gov record](https://clinicaltrials.gov/study/NCT04463316). (NCT04463316 chunk 1)

## 13. Prevention

No vaccine, medication, lifestyle modification, or environmental avoidance prevents a de novo or inherited MED12 pathogenic variant.

**Primary/reproductive prevention options** after identification of a familial pathogenic variant include genetic counseling, cascade testing of at-risk female relatives, preimplantation genetic testing, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and use of donor gametes where desired. Counseling must address uncertainty in female expression and variable severity.

**Secondary prevention** consists of early molecular diagnosis and prompt assessment of vision, hearing, cardiac anatomy, development, feeding, palate, and mobility. **Tertiary prevention** focuses on early rehabilitation, communication support, correction of congenital defects, and surveillance for patient-specific complications. Population newborn screening is not available or justified by present evidence.

## 14. Other species and natural disease

No naturally occurring veterinary syndrome directly equivalent to human OSMKB was identified, and there is no zoonotic potential. MED12 is evolutionarily conserved in vertebrates; experimental ortholog disruption affects development in mouse and zebrafish. Suggested taxa are **Mus musculus, NCBI Taxon 10090**, and **Danio rerio, NCBI Taxon 7955**. Exact ortholog NCBI Gene identifiers should be checked in the current NCBI Gene release before curation.

Because available nonhuman phenotypes are experimentally induced rather than recognized spontaneous breed diseases, no VBO breed annotation or veterinary prevalence is applicable.

## 15. Model organisms and experimental systems

### Human cellular models

Patient fibroblast studies of p.Arg1148His and p.Ser1165Pro provide the most disease-proximal mechanistic evidence: defective REST-element recruitment and neuronal-gene repression despite retained Mediator incorporation and G9a interaction. (silfhout2013mutationsinmed12 pages 4-5)

Patient-derived iPSC/isogenic neural models are an emerging platform. The 2025 p.Arg1138Trp model identified altered neural differentiation and POLR2A-related transcription, but variant classification and generalizability to classic OSMKB remain limitations. (shaw2025functionalcharacterizationof pages 9-11)

### Mouse

- Constitutive Med12 loss is developmentally severe or embryonically lethal, demonstrating essentiality but poorly modeling viable human missense disease.
- Mouse neural-stem-cell RNAi showed altered adhesion, proliferation, G1/S progression, and 240 differentially expressed genes. It is useful for neural progenitor biology but does not reproduce a specific human allele. (kim2016mediatorsubunitmed12 pages 1-2)
- Embryonic/conditional models support roles in neural-tube closure, neural crest, hematopoiesis, and canonical Wnt/Wnt-PCP signaling. Conditional designs are necessary because null alleles are often lethal. (plassche2021med12related(neuro)developmentaldisorders pages 6-7, kim2016mediatorsubunitmed12 pages 1-2)

### Zebrafish

Med12 perturbation affects hindbrain, neural-crest, and endoderm development. Zebrafish are useful for rapid developmental and pathway studies, but anatomy, X-chromosome biology, cognition, and variant dosage differ substantially from humans. (kim2016mediatorsubunitmed12 pages 1-2)

### Current model gaps

No well-validated knock-in mouse or zebrafish line was found that reproduces a classic OSMKB allele together with blepharophimosis, intellectual-disability-relevant behavior, age-dependent facial evolution, and variable congenital heart disease. No OSMKB organoid, single-cell atlas, spatial-transcriptomic study, or high-throughput therapeutic screen was identified.

## Evidence quality, recent developments, and major gaps

The highest-confidence evidence comprises the 2013 causal-gene discovery and functional experiments, segregation-confirmed families, and reproducible MED12 developmental biology. The main limitation is sample size: published evidence is insufficient for reliable phenotype percentages, penetrance, prevalence, sex ratio, survival, quality-of-life estimates, or treatment outcomes. The principal 2023–2024 development located was the 2024 methylation/phenotypic-overlap study with Helsmoortel–Van der Aa syndrome; however, full-text evidence was unavailable for detailed extraction. A 2024 p.Arg1138Trp female report and a first Hispanic case report broaden ascertainment, but neither establishes population-level statistics. The strongest recent functional advance is the 2025 patient-iPSC neural study, which supports variant-specific transcriptional and neurodevelopmental disruption. (shaw2025functionalcharacterizationof pages 9-11, shaw2025functionalcharacterizationof pages 8-9)

For knowledge-base use, assertions should therefore retain evidence qualifiers: **established** for MED12 causality, X-linked transmission, blepharophimosis/ptosis, intellectual-developmental disability, and characteristic facial morphology; **recurrent but variably expressed** for cardiac, palatal, hearing, genital, growth, and mobility findings; and **unknown** for epidemiology, survival, protective factors, standardized surveillance, and disease-modifying treatment.

References

1. (graham2013med12relateddisorders pages 3-5): John M. Graham and Charles E. Schwartz. Med12 related disorders. American Journal of Medical Genetics Part A, 161:2734-2740, Nov 2013. URL: https://doi.org/10.1002/ajmg.a.36183, doi:10.1002/ajmg.a.36183. This article has 97 citations.

2. (rocchetti2021med12mutationin pages 5-7): Luca Rocchetti, Eloisa Evangelista, Luigia De Falco, Giovanni Savarese, Pasquale Savarese, Raffaella Ruggiero, Luigi D’Amore, Alberto Sensi, and Antonio Fico. Med12 mutation in two families with x-linked ohdo syndrome. Genes, 12:1328, Aug 2021. URL: https://doi.org/10.3390/genes12091328, doi:10.3390/genes12091328. This article has 5 citations.

3. (silfhout2013mutationsinmed12 pages 1-2): Anneke T. Vulto-van Silfhout, Bert B.A. de Vries, Bregje W.M. van Bon, Alexander Hoischen, Martina Ruiterkamp-Versteeg, Christian Gilissen, Fangjian Gao, Marloes van Zwam, Cornelis L. Harteveld, Anthonie J. van Essen, Ben C.J. Hamel, Tjitske Kleefstra, Michèl A.A.P. Willemsen, Helger G. Yntema, Hans van Bokhoven, Han G. Brunner, Thomas G. Boyer, and Arjan P.M. de Brouwer. Mutations in med12 cause x-linked ohdo syndrome. American journal of human genetics, 92 3:401-6, Mar 2013. URL: https://doi.org/10.1016/j.ajhg.2013.01.007, doi:10.1016/j.ajhg.2013.01.007. This article has 125 citations and is from a highest quality peer-reviewed journal.

4. (li2021denovolossoffunction pages 1-2): Dong Li, Alanna Strong, Kaitlyn M. Shen, David Cassiman, Maria Van Dyck, Natalia Duarte Linhares, Eugenia Ribeiro Valadares, Tiancheng Wang, Sergio D.J. Pena, Jaak Jaeken, Samantha Vergano, Elaine Zackai, Anne Hing, Penny Chow, Arupa Ganguly, Tasja Scholz, Tatjana Bierhals, Deindl Philipp, Hakon Hakonarson, and Elizabeth Bhoj. De novo loss-of-function variants in x-linked med12 are associated with hardikar syndrome in females. Genetics in Medicine, 23:637-644, Apr 2021. URL: https://doi.org/10.1038/s41436-020-01031-7, doi:10.1038/s41436-020-01031-7. This article has 44 citations and is from a highest quality peer-reviewed journal.

5. (OpenTargets Search: Blepharophimosis-intellectual disability syndrome, MKB type): Open Targets Query (Blepharophimosis-intellectual disability syndrome, MKB type, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (rocchetti2021med12mutationin pages 7-8): Luca Rocchetti, Eloisa Evangelista, Luigia De Falco, Giovanni Savarese, Pasquale Savarese, Raffaella Ruggiero, Luigi D’Amore, Alberto Sensi, and Antonio Fico. Med12 mutation in two families with x-linked ohdo syndrome. Genes, 12:1328, Aug 2021. URL: https://doi.org/10.3390/genes12091328, doi:10.3390/genes12091328. This article has 5 citations.

7. (silfhout2013mutationsinmed12 pages 4-5): Anneke T. Vulto-van Silfhout, Bert B.A. de Vries, Bregje W.M. van Bon, Alexander Hoischen, Martina Ruiterkamp-Versteeg, Christian Gilissen, Fangjian Gao, Marloes van Zwam, Cornelis L. Harteveld, Anthonie J. van Essen, Ben C.J. Hamel, Tjitske Kleefstra, Michèl A.A.P. Willemsen, Helger G. Yntema, Hans van Bokhoven, Han G. Brunner, Thomas G. Boyer, and Arjan P.M. de Brouwer. Mutations in med12 cause x-linked ohdo syndrome. American journal of human genetics, 92 3:401-6, Mar 2013. URL: https://doi.org/10.1016/j.ajhg.2013.01.007, doi:10.1016/j.ajhg.2013.01.007. This article has 125 citations and is from a highest quality peer-reviewed journal.

8. (plassche2021med12related(neuro)developmentaldisorders pages 6-7): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

9. (kim2016mediatorsubunitmed12 pages 1-2): Nam Hee Kim, Carolina B. Livi, P. Renee Yew, and Thomas G. Boyer. Mediator subunit med12 contributes to the maintenance of neural stem cell identity. BMC Developmental Biology, May 2016. URL: https://doi.org/10.1186/s12861-016-0114-0, doi:10.1186/s12861-016-0114-0. This article has 6 citations and is from a peer-reviewed journal.

10. (donnio2017med12relatedxliddisorders pages 10-14): Lise-Marie Donnio, Baptiste Bidon, Satoru Hashimoto, Melanie May, Alexey Epanchintsev, Colm Ryan, William Allen, Anna Hackett, Jozef Gecz, Cindy Skinner, Roger E. Stevenson, Arjan P.M. de Brouwer, Charles Coutton, Christine Francannet, Pierre-Simon Jouk, Charles E. Schwartz, and Jean-Marc Egly. Med12-related xlid disorders are dose-dependent of immediate early genes (iegs) expression. Human Molecular Genetics, 26:2062–2075, Jun 2017. URL: https://doi.org/10.1093/hmg/ddx099, doi:10.1093/hmg/ddx099. This article has 33 citations and is from a domain leading peer-reviewed journal.

11. (rocchetti2021med12mutationin pages 2-4): Luca Rocchetti, Eloisa Evangelista, Luigia De Falco, Giovanni Savarese, Pasquale Savarese, Raffaella Ruggiero, Luigi D’Amore, Alberto Sensi, and Antonio Fico. Med12 mutation in two families with x-linked ohdo syndrome. Genes, 12:1328, Aug 2021. URL: https://doi.org/10.3390/genes12091328, doi:10.3390/genes12091328. This article has 5 citations.

12. (shaw2025functionalcharacterizationof pages 9-11): Nicole C. Shaw, Saraya Harrison, Kevin Chen, Catherine A. Forbes, Emma Kuzminski, Mitchell Hedges, Kathryn O. Farley, Michelle Ward, Lily Loughman, Cathryn Poulton, Gareth Baynam, Timo Lassmann, and Vanessa S. Fear. Functional characterization of the med12 p.arg1138trp variant in females: implications for neural development and disease mechanism. Molecular Medicine, Sep 2025. URL: https://doi.org/10.1186/s10020-025-01365-5, doi:10.1186/s10020-025-01365-5. This article has 0 citations and is from a peer-reviewed journal.

13. (NCT04463316 chunk 1): dr. Laura C. G. de Graaff-Herder. GROWing Up With Rare GENEtic Syndromes. dr. Laura C. G. de Graaff-Herder. 2018. ClinicalTrials.gov Identifier: NCT04463316

14. (plassche2021med12related(neuro)developmentaldisorders pages 11-13): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 28 citations.

15. (shaw2025functionalcharacterizationof pages 8-9): Nicole C. Shaw, Saraya Harrison, Kevin Chen, Catherine A. Forbes, Emma Kuzminski, Mitchell Hedges, Kathryn O. Farley, Michelle Ward, Lily Loughman, Cathryn Poulton, Gareth Baynam, Timo Lassmann, and Vanessa S. Fear. Functional characterization of the med12 p.arg1138trp variant in females: implications for neural development and disease mechanism. Molecular Medicine, Sep 2025. URL: https://doi.org/10.1186/s10020-025-01365-5, doi:10.1186/s10020-025-01365-5. This article has 0 citations and is from a peer-reviewed journal.

16. (graham2013med12relateddisorders pages 1-2): John M. Graham and Charles E. Schwartz. Med12 related disorders. American Journal of Medical Genetics Part A, 161:2734-2740, Nov 2013. URL: https://doi.org/10.1002/ajmg.a.36183, doi:10.1002/ajmg.a.36183. This article has 97 citations.

17. (fazio2025geneticclinicaland pages 6-8): Alessandro Fazio, Roberta Leonardi, Lorenzo Aliotta, Manuela Lo Bianco, Gennaro Anastasio, Giuseppe Messina, Corrado Spatola, Pietro Valerio Foti, Stefano Palmucci, Antonio Basile, Martino Ruggieri, and Emanuele David. Genetic, clinical and neuroradiological spectrum of med-related disorders: an updated review. Genes, 16:1444, Dec 2025. URL: https://doi.org/10.3390/genes16121444, doi:10.3390/genes16121444. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](Blepharophimosis_Intellectual_Disability_Syndrome_MKB_Type-deep-research-falcon_artifacts/artifact-00.md)