---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T16:12:23.958465'
end_time: '2026-07-24T16:27:26.984966'
duration_seconds: 903.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nipah Virus Disease
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Nipah_Virus_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nipah Virus Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Nipah Virus Disease** covering all of the
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
- **Disease Name:** Nipah Virus Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Nipah Virus Disease** covering all of the
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


# Nipah Virus Disease: Comprehensive Disease-Characteristics Report

## Executive summary

Nipah virus disease (NVD) is an acute, bat-borne zoonotic infection caused by Nipah virus (NiV), an enveloped negative-sense single-stranded RNA henipavirus. Disease ranges from asymptomatic infection or influenza-like illness to rapidly progressive pneumonia, acute respiratory distress syndrome (ARDS), encephalitis, seizures, coma, and death. The major biological lesion is systemic infection of ephrin-B2/B3-expressing endothelium and neural cells, producing vasculitis, thrombosis, blood–brain-barrier injury, and neuronal infection. Pteropus fruit bats are the reservoir; transmission occurs through contaminated food, infected livestock, and close contact with infected people. Outbreak-specific case-fatality ratios (CFRs) range from approximately 25% to 100%, and an aggregated 2024 review reported 424 deaths among 729 recognized cases (58%). No human vaccine or disease-specific treatment is licensed; supportive intensive care remains standard, while m102.4 and remdesivir are the leading candidates for clinical efficacy trials. (hassan2024nipahvirusdisease pages 11-14, hassan2024nipahvirusdisease pages 9-11, fauscotino2024nipahvirusa pages 3-5, fauscotino2024nipahvirusa pages 7-9, chan2024nipahvirustherapeutics pages 12-14)

The following compact table is intended for direct knowledge-base curation.

| Domain | High-confidence annotation/finding | Suggested ontology identifiers/terms | Evidence type and caveat |
|---|---|---|---|
| Disease identifier/classification | Nipah virus disease is a zoonotic henipavirus infection causing severe acute encephalitis and/or respiratory disease. Confident retrieved identifier: MeSH **D045464 Henipavirus Infections**; specific MONDO ID not confidently established from retrieved evidence, so mark **unknown/not confirmed here**. | MeSH: **D045464 Henipavirus Infections**; Disease label: **Nipah virus infection / disease**; MONDO: **unknown in retrieved sources** | Clinical trial registry-derived MeSH plus recent reviews; MeSH term in trials is broader than Nipah-specific disease, so disease-level normalization should be reviewed separately (NCT05178901 chunk 1, NCT04199169 chunk 1, NCT05398796 chunk 1, fauscotino2024nipahvirusa pages 3-5) |
| Pathogen | Cause is **Nipah virus (NiV)**, a negative-sense ssRNA henipavirus in family Paramyxoviridae; major clades/strains discussed are Malaysia and Bangladesh/India lineages. | Pathogen label: **Nipah virus**; Taxon term label acceptable if needed; CHEBI: not applicable | Review/pathobiology evidence; strain nomenclature and clade proposals are evolving, especially for India lineage (tan2024asystematicreview pages 1-2, fauscotino2024nipahvirusa pages 3-5, anish2024pandemicpotentialof pages 2-3) |
| Reservoir and spillover ecology | Natural reservoir is **Pteropus fruit bats**; spillover occurs directly via bat-contaminated food (notably raw date palm sap) and indirectly via amplifying hosts such as **pigs**; horses also noted in some outbreaks/reviews. | Host/reservoir terms: **Pteropus bats**, **swine**, **horse**; Exposure term: **raw date palm sap consumption** | Strong epidemiologic consensus; exact reservoir species differs by geography, and not all spillover events involve an intermediate host (tan2024asystematicreview pages 1-2, anish2024pandemicpotentialof pages 2-3, NCT01811784 chunk 1, pigeaud2023animalmodelsfor pages 1-2) |
| Transmission/risk factors | Major routes: pig-to-human in Malaysia/Singapore, contaminated date palm sap in Bangladesh, and person-to-person spread in Bangladesh/India/Kerala; close patient contact is a major risk factor. | Exposure terms: **zoonotic transmission**, **person-to-person transmission**, **foodborne exposure**, **occupational exposure** | Human outbreak investigations and reviews; route contributions vary strongly by outbreak setting (rahman2024riskevaluationand pages 3-4, tan2024asystematicreview pages 1-2, hassan2024nipahvirusdisease pages 11-14, hassan2024nipahvirusdisease pages 9-11) |
| Core phenotype set | Dominant phenotype spectrum: fever, headache, myalgia, cough/shortness of breath, acute encephalitis, confusion, seizures, coma; respiratory disease can be prominent, especially Bangladesh/India clade. | HPO suggestions: **Fever**, **Headache**, **Myalgia**, **Cough**, **Dyspnea**, **Encephalitis**, **Confusion**, **Seizure**, **Coma** | Human clinical reviews and outbreaks; exact frequency by symptom is incompletely standardized across cohorts (hassan2024nipahvirusdisease pages 11-14, chan2024nipahvirustherapeutics pages 1-4, saha2024recentadvancesof pages 6-7) |
| Long-term sequelae / QoL | Survivors may develop persistent neurologic disability, including paralysis and oculomotor/neurologic deficits; relapsing or late encephalitis is recognized. | HPO suggestions: **Paralysis**, **Abnormality of eye movement**, **Neurocognitive impairment** | Based on follow-up literature summarized in reviews; precise prevalence and QoL instrument data are limited (chan2024nipahvirustherapeutics pages 1-4, saha2024recentadvancesof pages 6-7, chan2024nipahvirustherapeutics pages 12-14) |
| Host genes / molecular host factors | **EFNB2** and **EFNB3** are key host entry receptors for NiV G glycoprotein. These are **host susceptibility/entry factors**, **not inherited monogenic causes** of disease. | Gene symbols: **EFNB2**, **EFNB3**; Mechanism labels: **viral receptor activity**, **virus entry into host cell** | Strong mechanistic evidence from virology studies and reviews; no retrieved evidence supports inherited pathogenic variants causing Nipah disease susceptibility (fauscotino2024nipahvirusa pages 3-5, brown2023immunopathogenesisofnipah pages 5-7, anish2024pandemicpotentialof pages 2-3) |
| Viral genes and immune evasion | Viral genome encodes N, P, M, F, G, L and accessory **V/W/C** proteins; G mediates receptor binding, F mediates fusion, and V/W/P antagonize interferon pathways. | GO suggestions: **virus entry into host cell**, **membrane fusion**, **negative regulation of type I interferon production**, **suppression by virus of host type I interferon-mediated signaling pathway** | Mostly mechanistic review synthesis from primary experimental work; gene-by-gene effects are largely derived from in vitro/animal systems rather than direct human intervention studies (fauscotino2024nipahvirusa pages 3-5, brown2023immunopathogenesisofnipah pages 5-7) |
| Pathophysiology | Upstream-to-downstream chain: respiratory entry → local replication → viremia/leukocyte-associated spread → endothelial and neuronal tropism → vasculitis, thrombosis, syncytia, BBB disruption, encephalitis, pulmonary edema/ARDS. | GO suggestions: **viral process**, **cell-cell fusion**, **vasculitis**, **inflammatory response**, **blood-brain barrier disruption**; CL suggestions: **endothelial cell**, **neuron**, **monocyte**, **natural killer cell**, **T cell** | Combined human pathology, in vitro, and animal-model evidence; BBB and leukocyte “Trojan horse” mechanisms remain incompletely resolved (fauscotino2024nipahvirusa pages 3-5, saha2024recentadvancesof pages 6-7, anish2024pandemicpotentialof pages 2-3) |
| Affected anatomy and cells | Primary organs/systems: **brain/CNS**, **lung/respiratory tract**, **vascular endothelium**; secondary involvement includes kidney, liver, and heart in severe systemic disease. Key target cells include **neurons**, **vascular endothelial cells**, and probably leukocyte populations during dissemination. | UBERON suggestions: **brain**, **lung**, **blood vessel endothelium**, **kidney**, **liver**, **heart**; CL suggestions: **neuron**, **endothelial cell**, **smooth muscle cell**, **monocyte**, **NK cell**, **CD8-positive T cell** | Human pathology and animal data agree on CNS/lung/endothelium; cell-type ranking outside endothelium/neurons is less certain in humans (fauscotino2024nipahvirusa pages 3-5, saha2024recentadvancesof pages 6-7, anish2024pandemicpotentialof pages 2-3) |
| Diagnostics | Outbreak diagnosis relies on laboratory confirmation plus clinical/epidemiologic context; recent reviews emphasize need for rapid diagnosis and strengthened diagnostic capacity. Experimental immunoassays using recombinant ephrin-B2 capture have been described. | Diagnostic labels: **RT-PCR**, **serology/ELISA**, **antigen detection**, **contact/exposure history** | Retrieved evidence set gives only partial test-detail coverage; exact specimen hierarchy and reference-standard algorithms are not fully captured here, so formal WHO/CDC lab guidance should be added in production (rahman2024riskevaluationand pages 3-4, fauscotino2024nipahvirusa pages 3-5) |
| Prognosis / statistics | High mortality overall. Recent review summarized **729 cases, 424 deaths (58%)** overall; CFRs are typically **<40% in Malaysia** and often **>70% in Bangladesh/India/Philippines**. 2023 Bangladesh outbreak reported **14 cases, 10 deaths (71%)** in one review. | Prognostic labels: **case fatality rate**, **neurologic sequelae**, **rapid progression** | Aggregated review data; outbreak-specific CFRs depend on strain, detection intensity, and care access, so statistics should be stored with location/year provenance (tan2024asystematicreview pages 1-2, hassan2024nipahvirusdisease pages 11-14, hassan2024nipahvirusdisease pages 9-11) |
| Treatment status and care | **No licensed therapy or vaccine for humans**. Current care is mainly **supportive/ICU care**; evidence-based priorities for trials are **m102.4** and **remdesivir** for prophylaxis/early treatment. Ribavirin has observational human use but uncertain efficacy and tolerability concerns. | MAXO suggestions: **supportive care**, **intensive care management**, **mechanical ventilation/respiratory support**, **antiviral treatment**, **monoclonal antibody therapy** | Strong expert consensus from 2024 reviews; efficacy evidence for most agents is preclinical or observational, not definitive randomized clinical efficacy (anish2024pandemicpotentialof pages 9-10, chan2024nipahvirustherapeutics pages 4-6, fauscotino2024nipahvirusa pages 7-9, chan2024nipahvirustherapeutics pages 12-14, chan2024nipahvirustherapeutics pages 1-4) |
| Prevention / public health | Key preventive measures: avoid **raw date palm sap**, use tree skirts/barriers to prevent bat contamination, infection-control measures for human-to-human spread, surveillance/contact tracing, and community education. | MAXO suggestions: **exposure avoidance counseling**, **infection prevention and control**, **contact tracing**, **behavior change intervention** | Includes interventional prevention trial context; effectiveness depends on local adherence and outbreak ecology (NCT01811784 chunk 1, NCT01811784 chunk 2, anish2024pandemicpotentialof pages 1-2) |
| Vaccine clinical development | Human vaccine trials through 2024 include **HeV-sG-V / HenipaVax** Phase 1 (**NCT04199169**, completed, n=192), **mRNA-1215** Phase 1 (**NCT05398796**, completed, n=40), **PHV02** Phase 1 (**NCT05178901**, completed, n=60), and PHV02 prime-boost Phase 1b (**NCT06221813**, completed, n=120). | Intervention labels: **subunit vaccine**, **mRNA vaccine**, **rVSV-vectored vaccine** | ClinicalTrials.gov records are high-confidence for status/design/enrollment; efficacy against clinical disease is not established from these early-phase studies (NCT05178901 chunk 1, NCT04199169 chunk 1, NCT05398796 chunk 1, NCT06221813 chunk 1) |
| Animal models / comparative biology | Reservoir biology centers on **Pteropus** bats; major models include **Syrian hamster**, **ferret**, **guinea pig**, **swine**, **cat**, and **nonhuman primates**. **African green monkeys** most closely reproduce human disease; hamsters/ferrets are practical for countermeasure triage but incompletely capture all human features. | Model labels: **Pteropus bat**, **Syrian hamster**, **ferret**, **guinea pig**, **pig**, **cat**, **African green monkey**, **marmoset**, **cynomolgus monkey** | Dedicated 2023 model review plus 2024 summaries; route/phenotype details vary by strain and inoculation method, and some companion-animal models are used sparingly for ethical/practical reasons (anish2024pandemicpotentialof pages 2-3, pigeaud2023animalmodelsfor pages 34-35, pigeaud2023animalmodelsfor pages 35-36, pigeaud2023animalmodelsfor pages 24-26, pigeaud2023animalmodelsfor pages 2-4) |


*Table: This table summarizes high-confidence knowledge-base annotations for Nipah virus disease across identifiers, pathogenesis, clinical features, prognosis, prevention, treatment status, vaccine trials, and animal models. It is designed as a compact curation aid and notes where ontology IDs or evidence remain uncertain.*

## 1. Disease information

### Definition and terminology

NVD is a zoonotic henipavirus infection characterized principally by acute encephalitis and/or severe respiratory disease. Synonyms include **Nipah virus infection**, **Nipah encephalitis**, **NiV infection**, and, less specifically, **henipavirus infection**. It was first recognized during the 1998–1999 Malaysia–Singapore outbreak; subsequent recurrent outbreaks have occurred mainly in Bangladesh and India, with an equine-associated outbreak in the Philippines. (tan2024asystematicreview pages 1-2, hassan2024nipahvirusdisease pages 11-14)

### Identifiers

* **MeSH:** D045464, *Henipavirus Infections*—a broader parent concept consistently assigned in the retrieved ClinicalTrials.gov records. (NCT05178901 chunk 1, NCT04199169 chunk 1)
* **MONDO:** a Nipah-specific MONDO identifier was not reliably returned by the resources accessed and should be curator-verified rather than inferred.
* **ICD-10/ICD-11:** no specific code was established in the retrieved evidence. Coding generally falls under viral encephalitis or other specified zoonotic viral disease, depending on jurisdiction; production use requires verification against the current national ICD modification.
* **OMIM/Orphanet:** not applicable as primary sources for a non-Mendelian acute infection; no disease-specific entries were confirmed.

This report synthesizes **aggregated disease-level resources, outbreak cohorts, clinical-trial registries, and experimental literature**. It is not derived from an individual EHR.

## 2. Etiology, risk, and protective factors

### Cause

The sole necessary causal agent is NiV. Important lineages include NiV-Malaysia and the Bangladesh/India clade. The latter is associated epidemiologically with severe pulmonary involvement, person-to-person transmission, and CFRs often exceeding 70%, whereas Malaysian outbreaks had CFRs below 40%; ascertainment, route, health-system capacity, and viral biology all probably contribute. (tan2024asystematicreview pages 1-2, anish2024pandemicpotentialof pages 2-3)

### Exposure risks

* **Bangladesh:** consumption of raw date-palm sap contaminated by bat saliva or urine; direct caregiving and exposure to respiratory/oral secretions.
* **Malaysia/Singapore:** occupational contact with infected pigs; 93% of patients in the initial setting reportedly had direct swine contact.
* **India/Kerala:** zoonotic spillover followed by household or nosocomial transmission; hospital superspreading has occurred.
* **Other:** contact with infected horses or contaminated meat was implicated in the Philippines.

One review estimated that 51% of recognized Bangladeshi cases followed close contact with another patient. A reported effective reproduction number around 1.46–1.80 should be interpreted cautiously because most transmission chains terminate and superspreading creates marked heterogeneity. (rahman2024riskevaluationand pages 3-4, anish2024pandemicpotentialof pages 1-2, hassan2024nipahvirusdisease pages 9-11, pigeaud2023animalmodelsfor pages 1-2)

### Genetic, protective, and gene–environment factors

No validated human germline causal variant, susceptibility locus, protective allele, modifier gene, Mendelian inheritance pattern, or clinically actionable pharmacogenomic association is established. **EFNB2** and **EFNB3** are host entry factors, not inherited causes. The dominant gene–environment relationship is functional: exposure introduces virus to tissues expressing these receptors. Environmental protection consists of avoiding raw sap, blocking bat access to collection sites, reducing infected-animal contact, and infection-control precautions. A 7,782-participant community protocol evaluated “do not drink raw sap” messaging and sap collection from trees protected by bamboo skirts or *banas*. (NCT01811784 chunk 1, NCT01811784 chunk 2, fauscotino2024nipahvirusa pages 3-5)

## 3. Phenotypes

Disease affects all age groups and usually begins acutely after a **4–14-day incubation period**, although longer incubations have occasionally been reported. Early fever, headache, myalgia, vomiting, cough, and dyspnea can progress over hours to days to altered consciousness, seizures, encephalitis, and coma; coma may develop within 24–48 hours after major neurological deterioration. Severity and respiratory prominence vary by lineage and outbreak. (chan2024nipahvirustherapeutics pages 1-4, anish2024pandemicpotentialof pages 2-3)

| Phenotype | Type/course | Suggested HPO annotation |
|---|---|---|
| Fever, headache, myalgia | Early symptoms; common but exact pooled frequencies unavailable | Fever; Headache; Myalgia |
| Cough, dyspnea, atypical pneumonia | Respiratory symptom/sign; variable to severe | Cough; Dyspnea; Pneumonia |
| Pulmonary edema/ARDS | Severe progressive complication | Pulmonary edema; Acute respiratory distress |
| Confusion/somnolence | Neurological/behavioral change; progressive | Confusion; Somnolence |
| Acute encephalitis | Cardinal severe manifestation | Encephalitis |
| Seizures and coma | Advanced disease; poor functional state | Seizure; Coma |
| Paralysis, cognitive/sensory/motor or oculomotor deficits | Long-term survivor morbidity | Paralysis; Neurocognitive impairment; Abnormality of eye movement |
| Relapsing/late-onset encephalitis | Episodic delayed complication, sometimes >1 year later | Recurrent encephalitis/encephalopathy—curator review recommended |

Survivors may have substantial dependence, impaired mobility, cognition, communication, or employment. However, recent disease-specific EQ-5D, SF-36, or PROMIS estimates were not found; quality-of-life effects are chiefly inferred from neurological disability studies. (chan2024nipahvirustherapeutics pages 1-4, chan2024nipahvirustherapeutics pages 12-14, saha2024recentadvancesof pages 6-7)

## 4. Genetic and molecular information

NVD is **not a genetic disorder**. Therefore causal human genes, ACMG-classified pathogenic variants, allele frequencies, chromosomal abnormalities, anticipation, mosaicism, founder effects, and carrier frequency are not applicable.

The approximately 18.2-kb viral genome encodes structural proteins **N, P, M, F, G, and L**; RNA editing/alternative expression from the P locus produces **V, W, and C**. G is the attachment protein, F mediates membrane fusion, M coordinates assembly/egress through phosphatidylserine and PI(4,5)P2 interactions, and L is the RNA-dependent RNA polymerase. V/W/P antagonize interferon production or STAT-dependent signaling; C contributes to budding. (fauscotino2024nipahvirusa pages 3-5, brown2023immunopathogenesisofnipah pages 5-7)

Relevant human genes are **EFNB2** and **EFNB3**, whose products act as viral receptors. Deep mutational scanning published in 2023 engineered an EFNB2 decoy that retained henipavirus-G binding while reducing Eph-receptor binding, illustrating a potential therapeutic rather than inherited-disease mechanism.

No reproducible human disease-associated DNA methylation, histone modification, structural variant, or clinically actionable epigenetic signature was established in the evidence reviewed.

## 5. Environmental and infectious-agent information

The primary non-genetic determinants are ecological and behavioral: bat habitat overlap, date-palm-sap harvesting, livestock intensification, occupational swine exposure, unsafe caregiving, inadequate personal protective equipment, and delayed recognition in resource-constrained settings. Smoking, alcohol, exercise, and ordinary diet have no established disease-specific causal role apart from consumption of contaminated raw foods. (rahman2024riskevaluationand pages 3-4, tan2024asystematicreview pages 1-2, NCT01811784 chunk 1)

**Agent:** Nipah virus, genus *Henipavirus*, family *Paramyxoviridae*. The virus requires maximum-containment laboratory practices for live-virus work. Pteropus bats shed virus through saliva and urine without the fulminant disease seen in spillover hosts. (NCT01811784 chunk 1, pigeaud2023animalmodelsfor pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Attachment and fusion:** NiV-G binds EFNB2/EFNB3; conformational activation of trimeric F drives fusion at the plasma/endosomal membrane.
2. **Local replication:** respiratory epithelial infection produces syncytia and inflammatory mediators; severe cases develop alveolar hemorrhage, edema, and ARDS.
3. **Immune evasion:** V/W/P suppress type-I interferon production or signaling, including STAT pathways; W also suppresses inflammatory mediators including CCL4, CCL5, and TNF-α in experimental systems.
4. **Dissemination:** free virus and leukocyte-associated virus enter blood. T cells, natural-killer cells, and monocytes have been implicated experimentally.
5. **Endotheliotropism:** infection of vascular endothelial cells causes multinucleated syncytia, necrotizing vasculitis, permeability, thrombosis, and microinfarction.
6. **Neuroinvasion:** hematogenous endothelial infection, disrupted blood–brain barrier, leukocyte-associated transport, olfactory routes, and direct neuronal spread are plausible, nonexclusive mechanisms.
7. **Clinical injury:** neuronal infection plus ischemic/perivascular lesions causes encephalitis, seizures, coma, and persistent deficits; systemic vascular disease contributes to renal, hepatic, and cardiac injury. (fauscotino2024nipahvirusa pages 3-5, saha2024recentadvancesof pages 6-7, anish2024pandemicpotentialof pages 2-3)

Suggested annotations include **GO: virus entry into host cell; membrane fusion; viral genome replication; negative regulation of type-I interferon signaling; inflammatory response; cell–cell fusion**, and cell types **endothelial cell, neuron, bronchiolar epithelial cell, alveolar type-II cell, smooth-muscle cell, monocyte, NK cell, and CD8-positive T cell**. Smooth-muscle cells can support prolonged high-titer replication without obvious cytopathic effect in vitro, so infection does not invariably equal tissue destruction.

### Molecular profiling and advanced technology

Bulk immune-expression studies report TNF-α, IL-1β, IL-6, IL-8, CXCL10, and G-CSF perturbation, but validated diagnostic transcriptomic, proteomic, metabolomic, or lipidomic signatures are not established. No mature human single-cell atlas, spatial-transcriptomic map, integrated clinical multi-omics classifier, or validated genome-wide CRISPR dependency panel was identified. These should be marked **insufficient evidence**, not negative findings. (saha2024recentadvancesof pages 6-7)

## 7. Anatomical structures affected

Primary systems are the **CNS, respiratory tract, and systemic vasculature**. Suggested UBERON labels are brain, cerebral blood vessel, blood–brain barrier, lung, bronchial epithelium, pulmonary alveolus, blood vessel endothelium, kidney, liver, and heart. Major lesions include encephalitis with necrosis/perivascular cuffing, pulmonary edema and hemorrhage, endothelial syncytia, vasculitis, and thrombosis. Kidney, liver, and heart are secondary systemic targets. Disease is diffuse rather than consistently unilateral; lateralization is not characteristic. (fauscotino2024nipahvirusa pages 3-5, saha2024recentadvancesof pages 6-7, pigeaud2023animalmodelsfor pages 2-4)

Subcellular annotations include plasma membrane (G–receptor attachment and fusion), endosome (F trafficking/activation), cytoplasm (replication complex), and plasma-membrane lipid domains (M-mediated assembly). There is no established primary mitochondrial, lysosomal, or nuclear storage defect.

## 8. Temporal development

Onset is acute or subacute in children and adults rather than congenital or age-dependent. A pragmatic sequence is incubation → febrile/prodromal illness → respiratory or neurological deterioration → encephalitis/ARDS and multiorgan injury → death or recovery with possible neurological sequelae. The critical treatment window is probably before high viral burden, encephalitis, and irreversible vascular/neural injury. (chan2024nipahvirustherapeutics pages 1-4, chan2024nipahvirustherapeutics pages 12-14)

Most disease is self-limited through death or recovery, not chronically replicative lifelong disease. Nevertheless, persistent viral foci or delayed inflammatory/reactivation phenomena may produce relapsing or late-onset encephalitis months to years later. Spontaneous clinical remission occurs in survivors; no therapy-induced remission rate has been established.

## 9. Inheritance, epidemiology, and population

No inheritance pattern, penetrance, carrier state, anticipation, or genetic counseling indication applies. Population risk is exposure-driven.

The 2024 global review synthesized 97 articles and found almost annual outbreaks in Bangladesh. Aggregate counts in another clinical review were 729 recognized cases and 424 deaths (58%). Country/outbreak CFRs varied from approximately 25% to 100%; mortality was generally below 40% in Malaysia and above 70% in Bangladesh, India, and the Philippines. The 2023 Bangladesh outbreak had 14 cases and 10 deaths (71%); Kerala’s September 2023 outbreak had six cases and two deaths. Kerala’s 2018 event included 23 infections (18 confirmed and five probable) and 21 deaths. (tan2024asystematicreview pages 1-2, anish2024pandemicpotentialof pages 1-2, hassan2024nipahvirusdisease pages 11-14, hassan2024nipahvirusdisease pages 9-11)

Because NiV is episodic and geographically focal, stable prevalence and annual incidence per 100,000 are not meaningful globally. Surveillance limitations likely cause underascertainment. No consistent sex ratio is established; occupational exposure produced male predominance in some swine-associated cohorts. All ages can be affected. (rahman2024riskevaluationand pages 3-4, chan2024nipahvirustherapeutics pages 1-4)

## 10. Diagnostics

Diagnosis requires epidemiological suspicion plus laboratory confirmation. Recommended outbreak testing includes:

* **Real-time RT-PCR** for viral RNA from respiratory/throat or nasal swabs, blood/serum, urine, and cerebrospinal fluid as clinically appropriate; timing and local reference-laboratory protocols matter.
* **Serology**, especially NiV-specific IgM/IgG ELISA or neutralization, for later disease or retrospective confirmation.
* **Virus isolation** only in appropriately equipped high-containment laboratories.
* MRI may show multifocal small ischemic or inflammatory brain lesions; EEG and CSF studies support encephalitis assessment but are not pathogen-specific.
* Histopathology may show necrotizing vasculitis, thrombosis, endothelial syncytia, and neuronal/endothelial viral antigen.

Experimental ephrin-B2-capture ELISA and lateral-flow formats can distinguish NiV/HeV antigen in research settings, but they are not replacements for validated public-health assays.

Clinical differentials include Japanese encephalitis, herpes simplex encephalitis, other arboviral encephalitides, bacterial meningitis, cerebral malaria, influenza/COVID-19 and other severe viral pneumonias, toxic-metabolic encephalopathy, and stroke. Exposure history, combined respiratory–neurological disease, clustering, and NiV-specific testing are discriminating.

Human genetic testing—WGS, WES, panels, CMA, karyotype, FISH, mitochondrial, or repeat-expansion testing—is **not indicated** for etiologic diagnosis. There is no population newborn or carrier screening. During outbreaks, contact identification, symptom surveillance, and targeted molecular testing constitute secondary prevention.

## 11. Outcome and prognosis

Mortality is high and usually occurs during acute encephalitic, respiratory, or multiorgan disease. Conventional five- or ten-year survival estimates are not applicable. Poor prognostic features plausibly include severe encephalopathy, coma, seizures, respiratory distress, high viral burden, and delayed supportive care, although validated bedside prognostic models are lacking. (chan2024nipahvirustherapeutics pages 1-4, anish2024pandemicpotentialof pages 2-3)

Survivors can recover substantially but remain at risk for paralysis, cognitive/sensory/motor deficits, oculomotor dysfunction, psychiatric or functional consequences, and late encephalitis. There is no validated prognostic molecular biomarker. Viral RNA burden, inflammatory mediators, and neutralizing-antibody responses remain research measures rather than approved prognostic tests. (chan2024nipahvirustherapeutics pages 1-4, saha2024recentadvancesof pages 6-7)

## 12. Treatment

### Current standard

There is **no licensed NiV-specific drug or human vaccine**. Management consists of isolation and infection prevention, oxygen and ventilatory support, fluid/electrolyte management, hemodynamic and renal support, seizure treatment, treatment of secondary infections, nutrition, pressure-injury prevention, and rehabilitation. Suggested MAXO labels include supportive care, intensive-care management, mechanical ventilation, anticonvulsant therapy, renal replacement therapy, physical therapy, occupational therapy, and speech therapy. (chan2024nipahvirustherapeutics pages 4-6, fauscotino2024nipahvirusa pages 7-9)

### Investigational agents

* **m102.4:** human monoclonal antibody targeting the G–EFNB2/B3 interface. A Phase 1 study in 40 healthy volunteers found no serious adverse events and a placebo-like safety profile; headache was most common. Post-exposure protection has been demonstrated in ferrets and nonhuman primates. MAXO: monoclonal-antibody therapy. (chan2024nipahvirustherapeutics pages 6-8)
* **Remdesivir:** nucleotide-analog viral polymerase inhibitor. It protected African green monkeys when given early; one review reported 67% survival with early dosing. Compassionate-use Kerala observations are uncontrolled and too small for efficacy inference. MAXO: antiviral therapy. (anish2024pandemicpotentialof pages 9-10, kallon2024therapeuticadvancementin pages 6-7)
* **Ribavirin:** observational Malaysian data suggested a 36% relative mortality-risk reduction, but confounding is substantial and African-green-monkey efficacy was absent. Fatigue, headache, hyperbilirubinemia, and hemoglobin reduction caused all eight recipients in one post-exposure series to discontinue therapy. (fauscotino2024nipahvirusa pages 7-9, chan2024nipahvirustherapeutics pages 6-8)
* **Favipiravir:** RNA-polymerase inhibitor giving 100% survival in one hamster regimen; no demonstrated human efficacy. (kallon2024therapeuticadvancementin pages 6-7)
* Other antibodies, including h5B3.1, nAH1.3, HENV-26, and HENV-32, remain preclinical.

The clearest 2024 expert assessment was that **only m102.4 and remdesivir had sufficient evidence to prioritize for trials**, alone or in combination, for prophylaxis or early treatment. This is a prioritization judgment, not proof of clinical efficacy. PK/PD optimization and pre-positioned adaptive outbreak protocols are essential. (chan2024nipahvirustherapeutics pages 12-14, chan2024nipahvirustherapeutics pages 1-4)

### Vaccine trials and recent development

* **HeV-sG-V/HenipaVax**, Hendra soluble-G subunit with alum: Phase 1, NCT04199169, completed, 192 adults; 10-, 30-, and 100-µg schedules. (NCT04199169 chunk 1)
* **PHV02**, live attenuated rVSV-ΔG-EBOV-GP-NiV-G: NCT05178901, Phase 1, completed, 60 adults; NCT06221813, Phase 1b prime–boost study, 120 adults, begun January 2024. (NCT05178901 chunk 1, NCT06221813 chunk 1)
* **mRNA-1215**, lipid-nanoparticle mRNA encoding a secreted prefusion-stabilized F/G immunogen: NCT05398796, Phase 1, 40 adults, two doses at 10–100 µg. (NCT05398796 chunk 1, NCT05398796 chunk 2)

These studies address safety and immunogenicity, not clinical disease prevention. Gene therapy, cell therapy, surgery, and genotype-guided treatment are not applicable.

## 13. Prevention

**Primary prevention:** avoid raw date-palm sap and fruit contaminated by bats; boil/pasteurize sap; cover collection sites with bat-exclusion skirts; use gloves and respiratory/eye protection when handling sick livestock; improve farm biosecurity and separate pigs from bat-attracting fruit trees. (NCT01811784 chunk 1)

**Secondary prevention:** rapid case recognition and RT-PCR confirmation, immediate isolation, contact tracing and active monitoring, safe specimen handling, appropriate PPE, and targeted testing. Healthcare-associated superspreading makes ventilation, hand hygiene, droplet/contact precautions, and escalation to airborne precautions for aerosol-generating procedures especially important. (anish2024pandemicpotentialof pages 1-2)

**Tertiary prevention:** aggressive organ support, seizure control, prevention of aspiration and secondary infection, and long-term neurological rehabilitation.

There is no licensed immunization or established antiviral prophylaxis. m102.4 and remdesivir prophylaxis remain investigational. Community engagement and One Health surveillance of humans, bats, livestock, food production, and land-use change are authoritative priorities. (tan2024asystematicreview pages 1-2, chan2024nipahvirustherapeutics pages 12-14)

## 14. Other species and natural disease

Pteropus fruit bats—including **Pteropus medius** in South Asia—are principal reservoirs. Pigs were amplification hosts in Malaysia/Singapore; 93% of patients in the original setting had direct infected-swine contact. Horses were implicated in the Philippines. Infection or serological evidence has also occurred in dogs and cats near outbreaks. Breed-specific VBO associations and orthologous “disease genes” are not applicable. (anish2024pandemicpotentialof pages 2-3, pigeaud2023animalmodelsfor pages 1-2)

Cross-species susceptibility is facilitated by conservation of EFNB2/B3. Spillover hosts develop much more severe respiratory, neurological, and vascular disease than reservoir bats. Swine are both veterinary disease hosts and epidemiologically important amplifiers, making livestock vaccination and surveillance potentially valuable One Health interventions.

## 15. Model organisms

* **Syrian golden hamster:** intranasal challenge emphasizes pneumonia/respiratory disease; intraperitoneal challenge produces dose-dependent lung, brain, kidney, hemorrhagic, and vascular lesions. It recapitulates most major human features but not myocarditis consistently. Practical for antiviral/vaccine screening. (anish2024pandemicpotentialof pages 2-3)
* **Ferret:** develops acute respiratory, neurological, and systemic disease and is widely used for antibody and vaccine evaluation. It is more expensive and less immunologically tractable than rodents and does not reproduce every human lesion. (pigeaud2023animalmodelsfor pages 34-35, mishra2024advancementsinnipah pages 11-12)
* **Guinea pig:** useful for histopathology, but disease reproducibility and translational fidelity are weaker.
* **Swine:** biologically relevant amplifier-host model for transmission and livestock vaccines; requires both humoral and cellular immunity for protection. Husbandry and containment constrain sample size. (pigeaud2023animalmodelsfor pages 35-36)
* **Cats/dogs:** susceptible and historically useful, but companion-animal ethics, inconsistent recapitulation, and superior alternatives limit routine use. (pigeaud2023animalmodelsfor pages 24-26)
* **African green monkey:** most faithful model of human pulmonary, vascular, and neurological disease; used for remdesivir, antibody, vaccine, aerosol, intratracheal, and intranasal studies. Limitations are cost, small cohorts, ethics, and BSL-4 requirements. (pigeaud2023animalmodelsfor pages 35-36, pigeaud2023animalmodelsfor pages 2-4)
* **Common marmoset:** intranasal/intratracheal NiV-B challenge caused 4/4 lethality, pulmonary edema, systemic vasculitis, hyperventilation, lethargy, anorexia, and hind-limb tremor after 8–11 days. Its small size permits larger NHP cohorts, but brain lesions were limited and immunological reagents are sparse. (pigeaud2023animalmodelsfor pages 24-26)
* **Cynomolgus and squirrel monkeys:** reproduce portions of respiratory and neurological disease, but vasculitis and brain pathology can be less pronounced than in humans. (pigeaud2023animalmodelsfor pages 35-36, pigeaud2023animalmodelsfor pages 24-26)

No standard transgenic, knockout, humanized, zebrafish, Drosophila, yeast, organoid, or iPSC model has supplanted challenge models. Model outcomes depend strongly on viral strain, dose, route, and age, so cross-study efficacy comparisons require standardized challenge stocks and endpoints.

## Evidence limitations and authoritative interpretation

The evidence base is constrained by small, unpredictable outbreaks, limited access to acute specimens, BSL-4 requirements, nonrandomized compassionate treatment, and heterogeneous case definitions. Consequently, outbreak CFRs should retain year/location provenance; animal protection must not be presented as demonstrated human efficacy; and host entry genes must not be misclassified as causal germline genes. The 2024 systematic review’s abstract accurately summarizes the central development gap: many countermeasures protect animals, but only a small number have entered human trials. (tan2024asystematicreview pages 1-2, chan2024nipahvirustherapeutics pages 4-6)

### Key recent sources and URLs

1. Tan FH et al. **A systematic review on Nipah virus: global molecular epidemiology and medical countermeasures development.** *Virus Evolution*. Published July 2024. https://doi.org/10.1093/ve/veae048. (tan2024asystematicreview pages 1-2)
2. Hassan MZ et al. **Nipah virus disease: what can we do to improve patient care?** *Lancet Infectious Diseases*. Published July 2024. https://doi.org/10.1016/S1473-3099(23)00707-7. (hassan2024nipahvirusdisease pages 11-14)
3. Faus-Cotino J et al. **Nipah Virus: A Multidimensional Update.** *Viruses*. Published January 2024. https://doi.org/10.3390/v16020179. (fauscotino2024nipahvirusa pages 3-5, fauscotino2024nipahvirusa pages 7-9)
4. Anish TS et al. **Pandemic potential of the Nipah virus and public health strategies adopted during outbreaks.** *PLOS Global Public Health*. Published December 2024. https://doi.org/10.1371/journal.pgph.0003926. (anish2024pandemicpotentialof pages 1-2)
5. Pigeaud DD et al. **Animal Models for Henipavirus Research.** *Viruses*. Published September 2023. https://doi.org/10.3390/v15101980. (pigeaud2023animalmodelsfor pages 34-35)
6. Chan XHS et al. **Nipah Virus Therapeutics: A Systematic Review to Support Prioritisation for Clinical Trials.** medRxiv preprint, posted March 2024. https://doi.org/10.1101/2024.03.11.24304091. Its recommendations require the additional caution appropriate to a preprint. (chan2024nipahvirustherapeutics pages 1-4)

References

1. (hassan2024nipahvirusdisease pages 11-14): Md Zakiul Hassan, Tahmina Shirin, Syed M Satter, Mohammed Z Rahman, Josephine Bourner, Ashleigh Cheyne, Els Torreele, Peter Horby, and Piero Olliaro. Nipah virus disease: what can we do to improve patient care? Jul 2024. URL: https://doi.org/10.1016/s1473-3099(23)00707-7, doi:10.1016/s1473-3099(23)00707-7. This article has 26 citations and is from a highest quality peer-reviewed journal.

2. (hassan2024nipahvirusdisease pages 9-11): Md Zakiul Hassan, Tahmina Shirin, Syed M Satter, Mohammed Z Rahman, Josephine Bourner, Ashleigh Cheyne, Els Torreele, Peter Horby, and Piero Olliaro. Nipah virus disease: what can we do to improve patient care? Jul 2024. URL: https://doi.org/10.1016/s1473-3099(23)00707-7, doi:10.1016/s1473-3099(23)00707-7. This article has 26 citations and is from a highest quality peer-reviewed journal.

3. (fauscotino2024nipahvirusa pages 3-5): Javier Faus-Cotino, Gabriel Reina, and Javier Pueyo. Nipah virus: a multidimensional update. Viruses, 16:179, Jan 2024. URL: https://doi.org/10.3390/v16020179, doi:10.3390/v16020179. This article has 46 citations.

4. (fauscotino2024nipahvirusa pages 7-9): Javier Faus-Cotino, Gabriel Reina, and Javier Pueyo. Nipah virus: a multidimensional update. Viruses, 16:179, Jan 2024. URL: https://doi.org/10.3390/v16020179, doi:10.3390/v16020179. This article has 46 citations.

5. (chan2024nipahvirustherapeutics pages 12-14): Xin Hui S Chan, Ilsa L Haeusler, Bennett J K Choy, Md Zakiul Hassan, Junko Takata, Tara P Hurst, Luke M Jones, Shanghavie Loganathan, Elinor Harriss, Jake Dunning, Joel Tarning, Miles W Carroll, Peter W Horby, and Piero L Olliaro. Nipah virus therapeutics: a systematic review to support prioritisation for clinical trials. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.24304091, doi:10.1101/2024.03.11.24304091. This article has 4 citations.

6. (NCT05178901 chunk 1):  A Phase 1 Study to Evaluate Safety & Immunogenicity of RVSV-Nipah Virus Vaccine Candidate PHV02 in Healthy Adult Subjects. Public Health Vaccines LLC. 2022. ClinicalTrials.gov Identifier: NCT05178901

7. (NCT04199169 chunk 1):  Safety and Immunogenicity of a Nipah Virus Vaccine. Auro Vaccines LLC. 2020. ClinicalTrials.gov Identifier: NCT04199169

8. (NCT05398796 chunk 1):  Dose Escalation, Open-Label Clinical Trial to Evaluate Safety, Tolerability and Immunogenicity of a Nipah Virus (NiV) mRNA Vaccine, mRNA-1215, in Healthy Adults. National Institute of Allergy and Infectious Diseases (NIAID). 2022. ClinicalTrials.gov Identifier: NCT05398796

9. (tan2024asystematicreview pages 1-2): Foo Hou Tan, Asif Sukri, Nuryana Idris, Kien Chai Ong, Jie Ping Schee, Chong Tin Tan, Soon Hao Tan, Kum Thong Wong, Li Ping Wong, Kok Keng Tee, and Li-Yen Chang. A systematic review on nipah virus: global molecular epidemiology and medical countermeasures development. Virus Evolution, Jul 2024. URL: https://doi.org/10.1093/ve/veae048, doi:10.1093/ve/veae048. This article has 38 citations and is from a peer-reviewed journal.

10. (anish2024pandemicpotentialof pages 2-3): Thekkumkara Surendran Anish, Reghukumar Aravind, Chandni Radhakrishnan, Nivedita Gupta, Pragya D. Yadav, Jerin Jose Cherian, Rima Sahay, Shubin Chenayil, Anoop Kumar A. S., Anitha Puduvail Moorkoth, Ashadevi, Velichapat Ramakrishnan Lathika, Shamsudeen Moideen, Sekhar Lukose Kuriakose, Kalathil Joseph Reena, and Thomas Mathew. Pandemic potential of the nipah virus and public health strategies adopted during outbreaks: lessons from kerala, india. PLOS Global Public Health, 4:e0003926, Dec 2024. URL: https://doi.org/10.1371/journal.pgph.0003926, doi:10.1371/journal.pgph.0003926. This article has 26 citations and is from a peer-reviewed journal.

11. (NCT01811784 chunk 1):  Community Intervention to Prevent Nipah Spillover. International Centre for Diarrhoeal Disease Research, Bangladesh. 2012. ClinicalTrials.gov Identifier: NCT01811784

12. (pigeaud2023animalmodelsfor pages 1-2): Declan D. Pigeaud, Thomas W. Geisbert, and Courtney Woolsey. Animal models for henipavirus research. Viruses, 15:1980, Sep 2023. URL: https://doi.org/10.3390/v15101980, doi:10.3390/v15101980. This article has 40 citations.

13. (rahman2024riskevaluationand pages 3-4): Md. Ashrafur Rahman, Yeasna Shanjana, Sydney Cronmiller, Donovan Zong, Rob Davis, Julianne Ernest, Jonah Nguyen, Amanda Rawa, Marie Roke Thomas, and Md. Rabiul Islam. Risk evaluation and mitigation strategies for potential outbreaks of nipah virus infection: evidenced by the recent incidences in southeast asian countries. Health Science Reports, Dec 2024. URL: https://doi.org/10.1002/hsr2.70239, doi:10.1002/hsr2.70239. This article has 4 citations and is from a peer-reviewed journal.

14. (chan2024nipahvirustherapeutics pages 1-4): Xin Hui S Chan, Ilsa L Haeusler, Bennett J K Choy, Md Zakiul Hassan, Junko Takata, Tara P Hurst, Luke M Jones, Shanghavie Loganathan, Elinor Harriss, Jake Dunning, Joel Tarning, Miles W Carroll, Peter W Horby, and Piero L Olliaro. Nipah virus therapeutics: a systematic review to support prioritisation for clinical trials. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.24304091, doi:10.1101/2024.03.11.24304091. This article has 4 citations.

15. (saha2024recentadvancesof pages 6-7): Sagnik Saha, Manojit Bhattacharya, Sang-Soo Lee, and Chiranjib Chakraborty. Recent advances of nipah virus disease: pathobiology to treatment and vaccine advancement. Journal of microbiology, 62:811-828, Sep 2024. URL: https://doi.org/10.1007/s12275-024-00168-3, doi:10.1007/s12275-024-00168-3. This article has 8 citations and is from a peer-reviewed journal.

16. (brown2023immunopathogenesisofnipah pages 5-7): Brent Brown, Tanya Gravier, Ingo Fricke, Suhaila A. Al-Sheboul, Theodor-Nicolae Carp, Chiuan Yee Leow, Chinua Imarogbe, and Javad Arabpour. Immunopathogenesis of nipah virus infection and associated immune responses. Immuno, 3:160-181, Apr 2023. URL: https://doi.org/10.3390/immuno3020011, doi:10.3390/immuno3020011. This article has 19 citations.

17. (anish2024pandemicpotentialof pages 9-10): Thekkumkara Surendran Anish, Reghukumar Aravind, Chandni Radhakrishnan, Nivedita Gupta, Pragya D. Yadav, Jerin Jose Cherian, Rima Sahay, Shubin Chenayil, Anoop Kumar A. S., Anitha Puduvail Moorkoth, Ashadevi, Velichapat Ramakrishnan Lathika, Shamsudeen Moideen, Sekhar Lukose Kuriakose, Kalathil Joseph Reena, and Thomas Mathew. Pandemic potential of the nipah virus and public health strategies adopted during outbreaks: lessons from kerala, india. PLOS Global Public Health, 4:e0003926, Dec 2024. URL: https://doi.org/10.1371/journal.pgph.0003926, doi:10.1371/journal.pgph.0003926. This article has 26 citations and is from a peer-reviewed journal.

18. (chan2024nipahvirustherapeutics pages 4-6): Xin Hui S Chan, Ilsa L Haeusler, Bennett J K Choy, Md Zakiul Hassan, Junko Takata, Tara P Hurst, Luke M Jones, Shanghavie Loganathan, Elinor Harriss, Jake Dunning, Joel Tarning, Miles W Carroll, Peter W Horby, and Piero L Olliaro. Nipah virus therapeutics: a systematic review to support prioritisation for clinical trials. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.24304091, doi:10.1101/2024.03.11.24304091. This article has 4 citations.

19. (NCT01811784 chunk 2):  Community Intervention to Prevent Nipah Spillover. International Centre for Diarrhoeal Disease Research, Bangladesh. 2012. ClinicalTrials.gov Identifier: NCT01811784

20. (anish2024pandemicpotentialof pages 1-2): Thekkumkara Surendran Anish, Reghukumar Aravind, Chandni Radhakrishnan, Nivedita Gupta, Pragya D. Yadav, Jerin Jose Cherian, Rima Sahay, Shubin Chenayil, Anoop Kumar A. S., Anitha Puduvail Moorkoth, Ashadevi, Velichapat Ramakrishnan Lathika, Shamsudeen Moideen, Sekhar Lukose Kuriakose, Kalathil Joseph Reena, and Thomas Mathew. Pandemic potential of the nipah virus and public health strategies adopted during outbreaks: lessons from kerala, india. PLOS Global Public Health, 4:e0003926, Dec 2024. URL: https://doi.org/10.1371/journal.pgph.0003926, doi:10.1371/journal.pgph.0003926. This article has 26 citations and is from a peer-reviewed journal.

21. (NCT06221813 chunk 1):  Study to Evaluate Safety and Immunogenicity of a Prime-Boost Regimen of rVSV-Nipah Virus Vaccine Candidate PHV02 in Healthy Adult Subjects. Public Health Vaccines LLC. 2024. ClinicalTrials.gov Identifier: NCT06221813

22. (pigeaud2023animalmodelsfor pages 34-35): Declan D. Pigeaud, Thomas W. Geisbert, and Courtney Woolsey. Animal models for henipavirus research. Viruses, 15:1980, Sep 2023. URL: https://doi.org/10.3390/v15101980, doi:10.3390/v15101980. This article has 40 citations.

23. (pigeaud2023animalmodelsfor pages 35-36): Declan D. Pigeaud, Thomas W. Geisbert, and Courtney Woolsey. Animal models for henipavirus research. Viruses, 15:1980, Sep 2023. URL: https://doi.org/10.3390/v15101980, doi:10.3390/v15101980. This article has 40 citations.

24. (pigeaud2023animalmodelsfor pages 24-26): Declan D. Pigeaud, Thomas W. Geisbert, and Courtney Woolsey. Animal models for henipavirus research. Viruses, 15:1980, Sep 2023. URL: https://doi.org/10.3390/v15101980, doi:10.3390/v15101980. This article has 40 citations.

25. (pigeaud2023animalmodelsfor pages 2-4): Declan D. Pigeaud, Thomas W. Geisbert, and Courtney Woolsey. Animal models for henipavirus research. Viruses, 15:1980, Sep 2023. URL: https://doi.org/10.3390/v15101980, doi:10.3390/v15101980. This article has 40 citations.

26. (chan2024nipahvirustherapeutics pages 6-8): Xin Hui S Chan, Ilsa L Haeusler, Bennett J K Choy, Md Zakiul Hassan, Junko Takata, Tara P Hurst, Luke M Jones, Shanghavie Loganathan, Elinor Harriss, Jake Dunning, Joel Tarning, Miles W Carroll, Peter W Horby, and Piero L Olliaro. Nipah virus therapeutics: a systematic review to support prioritisation for clinical trials. MedRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.11.24304091, doi:10.1101/2024.03.11.24304091. This article has 4 citations.

27. (kallon2024therapeuticadvancementin pages 6-7): Mary K. Kallon, Daniel Maada Mami, Emmanuel Tom Mami, Mariam Romba, M. Patrick Andrew, and M. Sylvester Martain. Therapeutic advancement in treatment and prevention of nipah viral infection: a review. Asian Journal of Research in Infectious Diseases, 15:51-65, Apr 2024. URL: https://doi.org/10.9734/ajrid/2024/v15i4343, doi:10.9734/ajrid/2024/v15i4343. This article has 5 citations.

28. (NCT05398796 chunk 2):  Dose Escalation, Open-Label Clinical Trial to Evaluate Safety, Tolerability and Immunogenicity of a Nipah Virus (NiV) mRNA Vaccine, mRNA-1215, in Healthy Adults. National Institute of Allergy and Infectious Diseases (NIAID). 2022. ClinicalTrials.gov Identifier: NCT05398796

29. (mishra2024advancementsinnipah pages 11-12): Gayatree Mishra, Vishal Prajapat, and Debasis Nayak. Advancements in nipah virus treatment: analysis of current progress in vaccines, antivirals, and therapeutics. Immunology, 171:155-169, Sep 2024. URL: https://doi.org/10.1111/imm.13695, doi:10.1111/imm.13695. This article has 78 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Nipah_Virus_Disease-deep-research-falcon_artifacts/artifact-00.md)