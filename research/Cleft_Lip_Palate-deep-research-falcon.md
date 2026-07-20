---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-01T19:06:51.961117'
end_time: '2026-07-01T19:23:22.027976'
duration_seconds: 990.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cleft Lip/Palate
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 59
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Cleft_Lip_Palate-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Cleft_Lip_Palate-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Cleft_Lip_Palate-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cleft Lip/Palate
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cleft Lip/Palate** covering all of the
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
- **Disease Name:** Cleft Lip/Palate
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cleft Lip/Palate** covering all of the
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


# Comprehensive Research Report: Cleft Lip and/or Palate (CL/P)

## 1. Disease Information

### Overview

Cleft lip and/or palate (CL/P) represents the most common congenital craniofacial malformation worldwide, affecting approximately 1 in 700 live births (ma2025burdenoforofacial pages 1-2, im2025molecularregulationof pages 5-6). The condition results from failure of fusion of the facial processes during embryogenesis, leading to structural discontinuity of the lip, alveolus, and/or palate (won2023generegulatorynetworks pages 1-2). Craniofacial development relies on proper growth and fusion of initially distinct collections of mesenchyme derived from the cranial neural crest, covered by epithelium of ectodermal origin (won2023generegulatorynetworks pages 1-2). Perturbation of the coordinated morphogenetic events underlying these processes—including cell migration, survival, proliferation, death, patterning, adhesion, and differentiation—can lead to orofacial cleft phenotypes (won2023generegulatorynetworks pages 1-2).

### Key Identifiers

- **MONDO:** MONDO:0016044 (cleft lip/palate)
- **OMIM:** Multiple entries including #119530 (CL/P nonsyndromic), #119300 (Van der Woude syndrome with IRF6)
- **ICD-10:** Q35 (Cleft palate), Q36 (Cleft lip), Q37 (Cleft palate with cleft lip)
- **ICD-11:** LA20.0 (Cleft lip), LA20.1 (Cleft palate), LA20.2 (Cleft lip with cleft palate)
- **MeSH:** D002971 (Cleft Lip), D002972 (Cleft Palate)
- **Orphanet:** ORPHA:199306 (Cleft lip/palate)

### Synonyms and Alternative Names

Common synonyms include: orofacial cleft (OFC), harelip (archaic), cheiloschisis (cleft lip), palatoschisis (cleft palate), CL/P, NSCL/P (nonsyndromic cleft lip with or without palate), CLP (cleft lip with cleft palate), CPO (cleft palate only). The condition is classified into three main subtypes: cleft lip only (CL), cleft palate only (CP), and cleft lip with cleft palate (CLP) (jaruga2022orofacialcleftand pages 3-5).

### Data Sources

The information herein is derived from aggregated disease-level resources including population-based epidemiological studies (Global Burden of Disease), molecular genetic research (GWAS, WES, WGS), curated disease-gene databases (OpenTargets, ClinVar, OMIM), clinical trial registries, and primary research literature.

---

## 2. Etiology

### Disease Causal Factors

CL/P has a complex, multifactorial etiology involving interactions between genetic susceptibility and environmental exposures. Approximately 93–97% of cases are nonsyndromic (NSCLP), arising from cumulative effects of multiple genetic alterations with modest effect sizes interacting with environmental factors (im2025molecularregulationof pages 5-6). The remaining 5–7% are syndromic, associated with over 400 genetic syndromes following Mendelian inheritance patterns (jaruga2022orofacialcleftand pages 3-5).

### Genetic Risk Factors

Major susceptibility genes identified through GWAS, linkage studies, and sequencing include IRF6, MSX1, ARHGAP29, CTNND1, PAX7, TP63, CDH1, BMP4, NTN1, NECTIN1, FOXE1, TGFB3, GRHL3, and others (OpenTargets Search: cleft lip,cleft palate, jaruga2022orofacialcleftand pages 5-6, cheng2023geneticinheritancemodels pages 2-5, im2025molecularregulationof pages 5-6). IRF6 is the most extensively validated susceptibility gene, with heterozygous pathogenic mutations causing Van der Woude syndrome (the most common syndromic form, affecting ~15% of patients) and common regulatory variants contributing to nonsyndromic risk (cheng2023geneticinheritancemodels pages 2-5, rahimov2024highincidenceand pages 1-4). MSX1 and IRF6 are the only two genes in which rare mutations contribute to both syndromic and nonsyndromic forms of CL/P and CP (rahimov2024highincidenceand pages 1-4). Linkage analysis has identified over 20 chromosomal regions linked to NSCLP, including 1p36, 2p21, 3p11.1, 8q21.3, 8q24, 13q31.1, and 15q22 (cheng2023geneticinheritancemodels pages 5-6, im2025molecularregulationof pages 6-8). Patients with a positive family history have up to a 32-fold increased risk, with an estimated recurrence risk of 4–10% (im2025molecularregulationof pages 5-6, jaruga2022orofacialcleftand pages 5-6).

The following table summarizes the key genes implicated in CL/P with their functions and association evidence:

| Gene symbol | Full name | OMIM ID (if known) | Associated syndrome / phenotype | Gene function relevant to CL/P | Typical variant type(s) reported | OpenTargets association score | Key evidence |
|---|---|---:|---|---|---|---:|---|
| IRF6 | Interferon regulatory factor 6 | 607199 | Van der Woude syndrome; popliteal pterygium syndrome; syndromic and non-syndromic cleft lip/palate; regulatory variant associated with cleft palate in Finland | Periderm differentiation; epithelial integrity; palatal fusion transcriptional regulator | Heterozygous pathogenic variants; common risk SNPs; regulatory/enhancer variants | 0.57 (cleft lip); 0.42 (cleft lip/palate) | (OpenTargets Search: cleft lip,cleft palate, cheng2023geneticinheritancemodels pages 2-5, rahimov2024highincidenceand pages 1-4, im2025molecularregulationof pages 5-6, im2025molecularregulationof pages 16-18) |
| MSX1 | Msh homeobox 1 | 142983 | Non-syndromic CL/P; tooth agenesis; rare syndromic and non-syndromic cleft palate/lip-palate | Homeobox transcription factor in craniofacial patterning; regulates epithelial-mesenchymal signaling during palate development | Rare pathogenic coding variants; common susceptibility variants; null alleles in models | 0.47 (cleft lip); 0.77 (cleft lip/palate) | (OpenTargets Search: cleft lip,cleft palate, cheng2023geneticinheritancemodels pages 2-5, rahimov2024highincidenceand pages 1-4, cheng2023geneticinheritancemodels pages 11-12, won2023generegulatorynetworks pages 13-14) |
| BMP4 | Bone morphogenetic protein 4 | 112262 | Cleft lip/palate susceptibility; craniofacial malformations | BMP pathway ligand controlling proliferation, differentiation, apoptosis, and palatal mesenchyme growth | Susceptibility SNPs; missense/duplication evidence in broader craniofacial anomaly literature | 0.74 (cleft lip/palate) | (OpenTargets Search: cleft lip,cleft palate, im2025molecularregulationof pages 36-37, im2025molecularregulationof pages 12-13, won2023generegulatorynetworks pages 13-14) |
| TP63 | Tumor protein p63 | 603273 | EEC syndrome; Hay-Wells syndrome; Rapp-Hodgkin syndrome; CL/P susceptibility | Epithelial development, adhesion, and palatal seam biology; upstream regulator of epithelial differentiation | Rare pathogenic missense / truncating variants; GWAS SNP rs76479869 association | 0.42 (cleft lip); 0.49 (cleft lip/palate) | (OpenTargets Search: cleft lip,cleft palate, jaruga2022orofacialcleftand pages 5-6, cheng2023geneticinheritancemodels pages 5-6, won2023generegulatorynetworks pages 8-10) |
| ARHGAP29 | Rho GTPase activating protein 29 | 610496 | Non-syndromic cleft lip / palate susceptibility | Cytoskeletal / Rho signaling regulator implicated in craniofacial morphogenesis | Rare pathogenic variants; susceptibility variants from sequencing/GWAS-supported studies | 0.61 (cleft lip) | (OpenTargets Search: cleft lip,cleft palate, jaruga2022orofacialcleftand pages 5-6) |
| CTNND1 | Catenin delta 1 | 601045 | Non-syndromic CL/P; epithelial adhesion-related cleft phenotypes | Cadherin–catenin complex component regulating epithelial adhesion and integrity | Pathogenic/likely pathogenic variants; splice-related dysregulation via ESRP1/2 | 0.51 (cleft lip) | (OpenTargets Search: cleft lip,cleft palate, cheng2023geneticinheritancemodels pages 5-6, im2025molecularregulationof pages 15-16) |
| PAX7 | Paired box 7 | 167410 | Non-syndromic cleft lip susceptibility; frontonasal patterning-related phenotypes | Transcription factor involved in craniofacial/frontonasal mesenchyme development | Common susceptibility variants/SNPs | 0.49 (cleft lip) | (OpenTargets Search: cleft lip,cleft palate, jaruga2022orofacialcleftand pages 5-6, im2025molecularregulationof pages 24-26) |
| CDH1 | Cadherin 1 | 192090 | Blepharocheilodontic syndrome; cleft lip susceptibility | Cell-cell adhesion protein essential for epithelial integrity | Heterozygous pathogenic variants; likely loss-of-function / missense variants | 0.39 (cleft lip) | (OpenTargets Search: cleft lip,cleft palate, cheng2023geneticinheritancemodels pages 2-5, cheng2023geneticinheritancemodels pages 12-14) |
| NECTIN1 | Nectin cell adhesion molecule 1 | 600644 | Cleft lip/palate-ectodermal dysplasia syndrome; cleft lip susceptibility | Cell adhesion molecule contributing to epithelial fusion processes | Pathogenic variants in syndromic clefting; curated gene-disease evidence | 0.48 (cleft lip); 0.85 (cleft lip/palate-ectodermal dysplasia syndrome) | (OpenTargets Search: cleft lip,cleft palate) |
| NTN1 | Netrin 1 | 601614 | Non-syndromic cleft lip susceptibility | Guidance cue involved in tissue morphogenesis and craniofacial developmental signaling | Common susceptibility variants; sequencing-supported variants | 0.47 (cleft lip) | (OpenTargets Search: cleft lip,cleft palate, cheng2023geneticinheritancemodels pages 12-14) |
| GRHL3 | Grainyhead like transcription factor 3 | 608317 | Cleft palate; downstream effector of IRF6; syndromic/non-syndromic palatal defects | Periderm differentiation and epithelial barrier/fusion regulation | Rare pathogenic variants; GWAS locus evidence for cleft palate | Not listed in retrieved OpenTargets results | (rahimov2024highincidenceand pages 1-4, alhazmi2024theapplicationof pages 1-3) |
| FOXE1 | Forkhead box E1 | 602617 | Associated with all major OFC types; non-syndromic CL/P susceptibility | Craniofacial developmental transcription factor | Susceptibility SNPs, including rs12347191 near FOXE1 | Not listed in retrieved OpenTargets results | (jaruga2022orofacialcleftand pages 5-6, im2025molecularregulationof pages 5-6, im2025molecularregulationof pages 6-8) |
| TGFB3 | Transforming growth factor beta 3 | 190230 | Cleft palate / CL/P susceptibility; smoking-interaction risk locus | Key regulator of palatal shelf adhesion/fusion and MES breakdown | Susceptibility variants/polymorphisms; gene-environment interaction variants | Not listed in retrieved OpenTargets results | (im2025molecularregulationof pages 6-8, im2025molecularregulationof pages 36-37, im2025molecularregulationof pages 15-16) |
| FGFR1 | Fibroblast growth factor receptor 1 | 136350 | CL/P susceptibility; craniofacial developmental anomalies | FGF receptor mediating epithelial-mesenchymal signaling in palatogenesis | Susceptibility variants; rare pathogenic variants in craniofacial syndromes | Not listed in retrieved OpenTargets results | (im2025molecularregulationof pages 5-6, im2025molecularregulationof pages 6-8, im2025molecularregulationof pages 9-12) |
| SUMO1 | Small ubiquitin-like modifier 1 | 601912 | Cleft lip/palate | Post-translational modifier implicated in craniofacial development | Rare pathogenic / copy-number-related evidence in curated datasets | 0.42 (cleft lip/palate) | (OpenTargets Search: cleft lip,cleft palate) |


*Table: This table summarizes high-priority genes implicated in cleft lip and/or palate, integrating curated disease-target associations with mechanistic and genetic evidence. It is useful for building a disease knowledge base entry and prioritizing genes for annotation, diagnostics, and pathway analysis.*

### Environmental Risk Factors

Multiple modifiable environmental risk factors have been identified. Maternal smoking is a significant risk factor with odds ratios ranging from 1.3–1.8 for unilateral CLP and up to 4.2 for bilateral cases when exceeding 25 cigarettes daily (viswapurna2024roleofepigenetics pages 3-4). Folate deficiency during the first trimester increases cleft lip risk 4.36-fold (viswapurna2024roleofepigenetics pages 3-4). Additional risk factors include maternal pre-pregnancy diabetes mellitus (OR 1.96), maternal obesity (OR 1.32 for grade II and extreme obesity), pre-pregnancy hypertension (OR 1.17), use of assisted reproductive technology (OR 1.40), maternal alcohol consumption, air pollutant exposure (PM2.5, PM10, ozone, carbon monoxide), teratogenic medications (corticosteroids, phenytoin), and TCDD/dioxin exposure (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47, iwaya2023micrornasandgene pages 10-12).

### Protective Factors

Periconceptional folic acid supplementation (≥400 µg/day during the first four weeks of gestation) is the most well-established protective factor, supporting folate-dependent one-carbon metabolism, nucleotide synthesis, and methylation during neural crest and palatal development (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47, viswapurna2024roleofepigenetics pages 7-8).

### Gene-Environment Interactions

Significant gene-environment interactions have been documented. Infants born to smoking mothers carrying the MSX1 susceptibility genotype have a 7.16-fold increased cleft risk (viswapurna2024roleofepigenetics pages 2-3). The RUNX2 genetic variant also increases cleft risk with maternal smoking exposure (viswapurna2024roleofepigenetics pages 3-4). Polymorphisms in TGF-α, TGFB3, and BMP4 interact with smoking to increase OFC risk (im2025molecularregulationof pages 36-37). MTHFR polymorphisms (C677T, 1298A>C) modify the impact of folate deficiency on cleft risk (viswapurna2024roleofepigenetics pages 3-4, alghonemy2025metaanalysisandsystematic pages 7-7).

The following table provides a detailed summary of environmental risk and protective factors:

| Factor | Category (Risk/Protective) | Effect Size (OR if available) | Mechanism | Gene-Environment Interaction | Source |
|---|---|---:|---|---|---|
| Maternal smoking | Risk | OR 1.3-1.8 overall; up to OR 4.2 for bilateral cases with >25 cigarettes/day | Nicotine-mediated vasoconstriction may impair uteroplacental blood flow and fetal oxygen delivery; smoke exposure is also linked to DNA methylation changes and oxidative-stress/cell-cycle dysregulation during craniofacial development | Reported interactions with **MSX1**, **RUNX2**, **TGFA**, **TGFB3**, and **BMP4** susceptibility variants | (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 36-37, viswapurna2024roleofepigenetics pages 2-3, iwaya2023micrornasandgene pages 10-12) |
| Folate deficiency / low periconceptional folate | Risk | OR 4.36 | Reduced one-carbon metabolism and methyl-donor availability can impair neural crest/palatal development and alter DNA methylation during embryogenesis | Strongly linked to **MTHFR** and other folate-pathway variants such as **SHMT1** | (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47, alghonemy2025metaanalysisandsystematic pages 7-7) |
| Maternal alcohol exposure | Risk | Not consistently quantified in retrieved evidence | Alcohol can inhibit retinoic acid biosynthesis via acetaldehyde and disrupt craniofacial morphogenesis; first-trimester binge drinking is particularly implicated | Gene-environment interaction frameworks reported; **PDGFRA** noted as protective in animal models against alcohol-related craniofacial defects | (im2025molecularregulationof pages 46-47, cheng2023geneticinheritancemodels pages 14-15, iwaya2023micrornasandgene pages 10-12) |
| Maternal obesity (including grade II/extreme obesity) | Risk | OR 1.32 | Likely contributes through metabolic/inflammatory dysregulation during early development | No specific interaction quantified in retrieved evidence | (viswapurna2024roleofepigenetics pages 3-4, cheng2023geneticinheritancemodels pages 14-15) |
| Pre-pregnancy diabetes mellitus | Risk | OR 1.96 | Hyperglycemia and metabolic teratogenicity may perturb craniofacial development | No specific interaction quantified in retrieved evidence | (viswapurna2024roleofepigenetics pages 3-4) |
| Pre-pregnancy hypertension | Risk | OR 1.17 | Vascular and placental dysfunction may adversely affect embryonic craniofacial development | No specific interaction quantified in retrieved evidence | (viswapurna2024roleofepigenetics pages 3-4) |
| Assisted reproductive technology | Risk | OR 1.40 | Mechanism uncertain; may reflect parental/subfertility factors or early embryologic influences | No specific interaction quantified in retrieved evidence | (viswapurna2024roleofepigenetics pages 3-4) |
| TCDD / dioxins | Risk | Not quantified in retrieved evidence | TCDD can inhibit palatal fusion and acts through epigenetic mechanisms including histone acetylation and microRNA dysregulation | Interacts with genetically susceptible developmental pathways; exact human genotype modifier not specified in retrieved evidence | (im2025molecularregulationof pages 46-47) |
| Retinoic acid excess / vitamin A toxicity | Risk | Not quantified in retrieved evidence | Excess retinoids impair key signaling pathways during palatogenesis and are recognized teratogens; dysregulated RA signaling disrupts facial process fusion | Alcohol-related RA deficiency and retinoid pathway susceptibility may modify risk | (im2025molecularregulationof pages 46-47, viswapurna2024roleofepigenetics pages 2-3) |
| Air pollutants (PM2.5, PM10, ozone, carbon monoxide) | Risk | Not quantified in retrieved evidence | Early gestational pollutant exposure may induce oxidative stress and developmental disruption | No specific interaction quantified in retrieved evidence | (viswapurna2024roleofepigenetics pages 3-4) |
| Maternal stress | Risk | Not quantified in retrieved evidence | Psychophysiologic stress is associated with increased risk in observational studies; likely mediated through neuroendocrine and inflammatory pathways | No specific interaction quantified in retrieved evidence | (cheng2023geneticinheritancemodels pages 14-15, viswapurna2024roleofepigenetics pages 2-3) |
| Folic acid supplementation (>=400 µg/day during first 4 weeks/periconception) | Protective | Protective; inverse association reported | Supports folate-dependent one-carbon metabolism, nucleotide synthesis, and methylation during neural crest/palatal development | Particularly relevant in carriers of folate-pathway risk variants such as **MTHFR** | (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47, viswapurna2024roleofepigenetics pages 7-8, alghonemy2025metaanalysisandsystematic pages 7-7) |
| MTHFR polymorphisms (e.g., C677T, 1298A>C) | Genetic susceptibility / risk modifier | Not uniform across studies | Reduced folate utilization and lower SAM availability may lead to hypomethylation and increased susceptibility to clefting | Modifies impact of folate deficiency and may alter response to folic acid supplementation | (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47, alghonemy2025metaanalysisandsystematic pages 7-7) |
| MSX1 genotype with maternal smoking | Gene-environment risk interaction | 7.16-fold increased risk | Smoking exposure plus cleft-susceptibility genotype likely amplifies developmental signaling disruption during lip/palate fusion | **MSX1 × smoking** | (viswapurna2024roleofepigenetics pages 2-3) |
| RUNX2 variant with maternal smoking | Gene-environment risk interaction | Increased risk reported; exact OR not provided in retrieved evidence | Smoking appears to enhance the effect of craniofacial regulatory variation on cleft risk | **RUNX2 × smoking** | (viswapurna2024roleofepigenetics pages 3-4, viswapurna2024roleofepigenetics pages 2-3) |
| TGFA / TGFB3 / BMP4 polymorphisms with smoking | Gene-environment risk interaction | Increased risk reported; exact ORs not provided in retrieved evidence | Tobacco exposure may interact with growth-factor signaling and methylation-sensitive pathways central to fusion and epithelial-mesenchymal signaling | **TGFA × smoking**, **TGFB3 × smoking**, **BMP4 × smoking** | (im2025molecularregulationof pages 36-37, viswapurna2024roleofepigenetics pages 2-3) |


*Table: This table summarizes major environmental and gene-environment contributors to cleft lip/palate risk, including effect sizes where available. It is useful for etiologic annotation, prevention planning, and linking modifiable exposures to molecular susceptibility pathways.*

---

## 3. Phenotypes

### Clinical Features

CL/P phenotypes are characterized by structural discontinuity in the lip and/or palate, resulting in impairment of multiple critical functions (jaruga2022orofacialcleftand pages 3-5). The most common presentation is unilateral cleft lip and palate (UCLP, 30–35%), followed by isolated CL or CP (20–25% each), with bilateral cleft lip and palate (BCLP) being least common (10%) (wongsirichat2022theprevalenceof pages 2-5). Unilateral clefts are twice as frequent on the left side (jaruga2022orofacialcleftand pages 3-5).

**Feeding difficulties (HP:0011968):** Cleft lip prevents proper nipple seal during breastfeeding, while cleft palate prevents negative pressure generation needed for milk intake and impairs tongue compression, leading to poor nutrition and inadequate weight gain (wongsirichat2022theprevalenceof pages 2-5, jaruga2022orofacialcleftand pages 3-5). Surgical palatal repair improved feeding in 79% of cases (wongsirichat2022theprevalenceof pages 5-6, wongsirichat2022theprevalenceof pages 2-5).

**Speech and language impairment (HP:0000750):** Patients manifest atypical consonant production, abnormal nasal resonance (hypernasality), and delayed language acquisition. Velopharyngeal insufficiency (VPI) requiring surgical intervention occurs in approximately 59% of bilateral cleft patients (wongsirichat2022theprevalenceof pages 5-6, hattori2023longtermtreatmentoutcome pages 1-2).

**Hearing loss/otitis media (HP:0000365, HP:0000388):** High rates of otitis media with effusion and hearing problems are documented in CL/P patients (NCT00829101 chunk 1).

**Dental anomalies (HP:0000164):** Dental development is delayed an average of 6–7 months compared to unaffected children. Complications include hypodontia, malocclusion, transverse maxillary arch collapse with crossbite, crowding, and incisor retroclination (wongsirichat2022theprevalenceof pages 5-6, jaruga2022orofacialcleftand pages 3-5).

**Maxillary growth impairment (HP:0000347):** Maxillary underdevelopment is a significant complication, with skeletal class III anteroposterior deficiency occurring in operated cleft patients (wongsirichat2022theprevalenceof pages 2-5). Orthognathic surgery was required in 60.7% of BCLP patients with midface retrusion (hattori2023longtermtreatmentoutcome pages 1-2).

**Quality of Life Impact:** CL/P causes major morbidity throughout life as a result of problems with facial appearance, feeding, speaking, obstructive apnea, hearing, and social adjustment, requiring complex multidisciplinary care at considerable cost to healthcare systems worldwide (wongsirichat2022theprevalenceof pages 1-2).

### Suggested HPO Terms
- HP:0000175 (Cleft palate)
- HP:0000204 (Cleft upper lip)
- HP:0000202 (Cleft lip and palate)
- HP:0011968 (Feeding difficulties)
- HP:0000750 (Delayed speech and language development)
- HP:0000164 (Abnormality of the dentition)
- HP:0000347 (Micrognathia/maxillary hypoplasia)
- HP:0000365 (Hearing impairment)
- HP:0000388 (Otitis media)

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants

For syndromic forms, IRF6 (OMIM 607199) heterozygous pathogenic mutations cause Van der Woude syndrome (autosomal dominant); CDH1 heterozygous mutations cause blepharocheilodontic syndrome; TP63 mutations are associated with ectrodactyly-ectodermal dysplasia-cleft syndrome, Hay-Wells syndrome, and Rapp-Hodgkin syndrome (cheng2023geneticinheritancemodels pages 2-5, cheng2023geneticinheritancemodels pages 5-6). A regulatory variant (rs570516915) disrupting an IRF6 transcription factor binding site in an enhancer was identified as strongly associated with CP in the Finnish population (rahimov2024highincidenceand pages 1-4).

For nonsyndromic forms, pathogenic variants in CTNND1, PLEKHA5, and ESRP2 influence epithelial Cadherin-p120-Catenin complex expression (cheng2023geneticinheritancemodels pages 5-6, im2025molecularregulationof pages 15-16). Whole-genome sequencing in 130 African case-parent trios identified high-confidence protein-altering de novo mutations in ACTL6A, ARHGAP10, MINK1, TMEM5, TTN, DHRS3, DLX6, EPHB2, SHH, and TP63, among others (alhazmi2024theapplicationof pages 1-3).

### GWAS Loci

Major GWAS-identified susceptibility regions include 1p36, 2p21, 3p11.1, 8q21.3, 8q24, 13q31.1, and 15q22 (cheng2023geneticinheritancemodels pages 5-6). Key SNPs include rs8001641, rs58593329, rs7650466, rs2235371, rs4791774, rs6072081, and rs76479869 in TP63 (jaruga2022orofacialcleftand pages 5-6, cheng2023geneticinheritancemodels pages 2-5, cheng2023geneticinheritancemodels pages 5-6). Fifteen GWAS loci for cleft palate specifically include candidate genes GRHL3, IRF6, CTNNA2, PTCH1, YAP1, PAX9, and others (rahimov2024highincidenceand pages 1-4).

### Epigenetic Information

DNA methylation alterations are involved in CL/P etiology. Hypomethylated genes include MYC, FAT1, WHSC1, VAX1, NTN1, BICC1, and MTHFR, while hypermethylated genes include IRF6, TBX1, CRISPLD2, WNT3A, GLI2, SOX2, and PITX2 (viswapurna2024roleofepigenetics pages 4-5). MicroRNAs serve as critical epigenetic regulators: miR-21, miR-181a, miR-452, miR-133b, miR-374a-5p, miR-497-5p, miR-27b, and miR-205 regulate genes involved in cell proliferation, apoptosis, and EMT during palatal development (im2025molecularregulationof pages 23-24, iwaya2023micrornasandgene pages 4-6, im2025molecularregulationof pages 24-26). The mir-17-92 cluster is functionally associated with mammalian CL/P and regulates TGF-β signaling (im2025molecularregulationof pages 24-26). Histone modifications including H3K4 methylation and H4R3me2a (via PRMT1), and regulation by HDAC3 and HDAC4, contribute to palatogenesis (im2025molecularregulationof pages 23-24).

---

## 5. Environmental Information

Environmental teratogens are detailed in Section 2 above. Key lifestyle factors include maternal cigarette smoking (vasoconstriction, DNA methylation changes, oxidative stress) (im2025molecularregulationof pages 36-37), alcohol consumption (inhibition of retinoic acid biosynthesis via acetaldehyde) (im2025molecularregulationof pages 46-47), and inadequate dietary folate intake. Occupational and ambient environmental exposures include air pollutants (PM2.5, PM10, ozone, CO) during early gestation and TCDD/dioxin exposure through histone acetylation and microRNA dysregulation mechanisms (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

Palatogenesis is regulated by a complex network of signaling pathways including TGF-β, BMP, SHH, WNT, and FGF, which control palatal shelf outgrowth, elevation, adhesion, and fusion (won2023generegulatorynetworks pages 1-2, im2025molecularregulationof pages 12-13, won2023generegulatorynetworks pages 5-7). These pathways operate through reciprocal epithelial-mesenchymal interactions along the anterior-posterior axis (won2023generegulatorynetworks pages 4-5).

| Pathway Name | Key Components/Genes | Role in Palatogenesis | Consequence of Disruption | Associated Mouse Models |
|---|---|---|---|---|
| TGF-β | **TGFB3**, **TGFBR2**, **SMAD2**, **TAK1**, p38 MAPK, **CTNNB1**-linked regulation of TGF-β3 | Essential for palatal shelf adhesion and fusion; promotes midline epithelial seam (MES) breakdown, periderm desquamation, and epithelial remodeling during fusion; also modulates epithelial-mesenchymal interactions and influences Shh signaling via lipid metabolism (im2025molecularregulationof pages 12-13, im2025molecularregulationof pages 15-16, won2023generegulatorynetworks pages 13-14, im2025molecularregulationof pages 16-18) | Failure of palatal fusion, persistent MES, delayed/abnormal periderm removal, cleft palate (im2025molecularregulationof pages 15-16, im2025molecularregulationof pages 16-18) | **Tgfbr2** conditional inactivation in cranial neural crest causes cleft palate and calvarial defects (won2023generegulatorynetworks pages 13-14) |
| BMP | **BMP2**, **BMP4**, **BMPR1A**, **NOGGIN**, p-SMAD1/5/8, **PAX9**-BMP4 network | Regulates palatal mesenchymal proliferation, differentiation, apoptosis, and anterior-posterior patterning; interacts with Shh to stimulate mesenchymal proliferation; crucial in cranial neural crest-derived mesenchyme (im2025molecularregulationof pages 12-13, won2023generegulatorynetworks pages 5-7, won2023generegulatorynetworks pages 13-14) | Dysregulated BMP signaling causes cleft palate/cleft lip, impaired palatal growth, abnormal patterning; BMP antagonism (Noggin) leads to retarded growth and cleft palate (im2025molecularregulationof pages 12-13, won2023generegulatorynetworks pages 5-7) | Mesenchymal/neural crest **Bmpr1a** loss causes severe craniofacial defects; **Msx1**-null cleft palate can be linked to altered BMP/Shh network activity (im2025molecularregulationof pages 12-13, won2023generegulatorynetworks pages 13-14) |
| SHH (Sonic Hedgehog) | **SHH**, **SMO**, primary cilia, **FOXF1/2**, **FGF10**, **BMP2**, **PTCH** | Drives palatal shelf outgrowth through reciprocal epithelial-mesenchymal signaling; maintains proliferation of palatal epithelial and mesenchymal cells; participates in regional patterning and works in feedback with FGF and BMP pathways (won2023generegulatorynetworks pages 1-2, won2023generegulatorynetworks pages 5-7, won2023generegulatorynetworks pages 13-14, im2025molecularregulationof pages 9-12, won2023generegulatorynetworks pages 4-5) | Reduced cell proliferation, defective palatal outgrowth, impaired shelf development, cleft palate (won2023generegulatorynetworks pages 13-14, im2025molecularregulationof pages 9-12, won2023generegulatorynetworks pages 4-5) | Epithelial **Shh** inactivation impairs palatal cell proliferation; mesodermal **Smo** inactivation disrupts outgrowth (im2025molecularregulationof pages 9-12, won2023generegulatorynetworks pages 4-5) |
| WNT | Canonical **WNT/β-catenin (CTNNB1)**, **PAX9**, **OSR2**, **WNT5A**, **SFRP2** | Regulates proliferation, migration, differentiation, mediolateral/anterior-posterior patterning, and secondary palate development; also regulates **TGFB3** expression and integrates with BMP/FGF/SHH signaling (im2025molecularregulationof pages 12-13, im2025molecularregulationof pages 15-16, won2023generegulatorynetworks pages 5-7, won2023generegulatorynetworks pages 13-14) | Disrupted WNT signaling contributes to cleft pathogenesis through abnormal proliferation/patterning; persistent canonical WNT can induce ectopic mesenchymal condensation, soft palate agenesis, and impaired palatal osteogenesis (im2025molecularregulationof pages 12-13, won2023generegulatorynetworks pages 13-14) | **Osr2-cre; Ctnnb1** constitutive activation model shows abnormal mesenchymal condensation, impaired osteogenesis, and soft palate defects; **Osr2−/−; Pax9−/−** embryos exhibit cleft palate (won2023generegulatorynetworks pages 4-5) |
| FGF | **FGF10**, **FGFR2b**, **FGF7**, **FGF18**, **JAG2/NOTCH**, **FOXF1/2** | Controls epithelial-mesenchymal crosstalk, palatal epithelial differentiation, shelf outgrowth, and proliferation; **FGF10-FGFR2b** maintains epithelial Shh and coordinates with Jag2-Notch signaling; **FGF7** can suppress Shh (im2025molecularregulationof pages 15-16, won2023generegulatorynetworks pages 5-7, won2023generegulatorynetworks pages 13-14, won2023generegulatorynetworks pages 8-10, im2025molecularregulationof pages 9-12, won2023generegulatorynetworks pages 4-5) | Cleft palate due to impaired shelf outgrowth, defective epithelial differentiation/adhesion, and disrupted epithelial-mesenchymal signaling (im2025molecularregulationof pages 15-16, won2023generegulatorynetworks pages 8-10, im2025molecularregulationof pages 9-12) | **Fgf10−/−** mice develop cleft palate with impaired palatal shelf outgrowth; **Fgf10/Fgfr2b** disruption causes cleft palate through disturbed epithelial-mesenchymal interactions (won2023generegulatorynetworks pages 4-5, won2023generegulatorynetworks pages 13-14) |


*Table: This table summarizes the core developmental signaling pathways implicated in palatogenesis and cleft lip/palate pathogenesis, linking pathway-level functions to disruption phenotypes and representative mouse models. It is useful for connecting mechanistic biology with disease annotations and experimental systems.*

### Cellular Processes

The causal chain from initial trigger to clinical manifestation involves: (1) Cranial neural crest cell (NCC) specification, migration, and colonization of the facial primordia (upstream); (2) Palatal shelf outgrowth from maxillary prominences regulated by SHH-FGF feedback loops and BMP signaling (intermediate); (3) Palatal shelf elevation above the tongue; (4) Shelf contact, epithelial adhesion, midline epithelial seam (MES) formation, and periderm removal; and (5) MES dissolution through apoptosis and epithelial-mesenchymal transition (EMT), achieving mesenchymal continuity (downstream) (im2025molecularregulationof pages 15-16, won2023generegulatorynetworks pages 8-10, im2025molecularregulationof pages 16-18).

Key cell types involved include cranial neural crest-derived mesenchyme (CL:0000008, neural crest cell), palatal epithelium, periderm cells, and medial edge epithelium (MEE). Periderm cells express CEACAM1 and undergo desquamation regulated by Snai1/Snai2-mediated E-cadherin downregulation and TGF-β3 signaling, which is essential for palatal fusion (im2025molecularregulationof pages 16-18).

### GO Terms for Biological Processes
- GO:0060021 (palate development)
- GO:0060022 (hard palate development)
- GO:0060023 (soft palate development)
- GO:0001843 (neural tube closure)
- GO:0001838 (neural crest cell migration)
- GO:0001837 (epithelial to mesenchymal transition)
- GO:0006915 (apoptotic process)
- GO:0042476 (odontogenesis)

---

## 7. Anatomical Structures Affected

### Organ and Tissue Level
- **Primary structures:** Upper lip (UBERON:0001833), primary palate (UBERON:0005620), secondary palate (hard palate UBERON:0003216, soft palate UBERON:0001785), alveolar ridge (UBERON:0004535)
- **Secondary involvement:** Nasal cavity (communication due to oronasal fistula), middle ear (otitis media), dentition, maxilla (UBERON:0002397)
- **Body systems:** Craniofacial (UBERON:0007811), digestive (feeding impairment), respiratory (obstructive apnea), auditory

### Cell Types
- Cranial neural crest cells (CL:0000008)
- Palatal mesenchymal cells
- Oral epithelial cells (CL:0002251)
- Periderm cells
- Osteoblasts (CL:0000062)

### Lateralization
Unilateral clefts are approximately twice as common as bilateral clefts, with left-sided clefts being more frequent than right-sided (jaruga2022orofacialcleftand pages 3-5).

---

## 8. Temporal Development

### Onset
CL/P is congenital, with the developmental defect occurring during weeks 4–12 of embryogenesis. Upper lip fusion occurs during weeks 4–8, while secondary palate fusion occurs during weeks 6–12. The condition is detectable prenatally via ultrasound.

### Progression
CL/P itself is a static structural malformation present at birth, but its consequences are lifelong and progressive in terms of functional impact on feeding (neonatal), speech (childhood), dental development (childhood–adolescence), and maxillofacial growth (adolescence–adulthood) (wongsirichat2022theprevalenceof pages 5-6, hattori2023longtermtreatmentoutcome pages 1-2, wongsirichat2022theprevalenceof pages 1-2). Cleft patients show lower weight and smaller size compared to non-cleft children, with maxillary underdevelopment peaking in adulthood (wongsirichat2022theprevalenceof pages 2-5).

### Critical Periods
- Weeks 4–8 gestation: lip/primary palate fusion (critical window for CL)
- Weeks 6–12 gestation: secondary palate fusion (critical window for CP)
- First trimester: maximum sensitivity to environmental teratogens (viswapurna2024roleofepigenetics pages 3-4, iwaya2023micrornasandgene pages 10-12)

---

## 9. Inheritance and Population

### Epidemiology

In 2021, there were approximately 4,124,007 prevalent cases of orofacial clefts globally, with an age-standardized prevalence rate of 53.4 per 100,000 population (wang2025globalregionaland pages 1-2, ma2025burdenoforofacial pages 1-2). The global incidence is approximately 1 in 700 live births (ma2025burdenoforofacial pages 1-2). From 1990–2021, prevalence decreased 40.38%, mortality decreased 86.08%, and DALYs decreased 68.33% (ma2025burdenoforofacial pages 1-2). Over 80% of the burden is borne by low- and middle-income countries (ma2025burdenoforofacial pages 1-2, ma2025burdenoforofacial pages 7-9).

The total prevalence per 10,000 births from 2016–2021 in the United States was 4.88, with 5.96 for males and 3.75 for females (viswapurna2024roleofepigenetics pages 3-4). International surveillance data report a CLP prevalence of 6.4 per 10,000 births (goldrick2023amultiprogramanalysis pages 8-10).

### Inheritance Pattern
NSCLP follows multifactorial/polygenic inheritance with both genetic and environmental contributions (cheng2023geneticinheritancemodels pages 2-5, im2025molecularregulationof pages 5-6). Syndromic forms follow Mendelian patterns (autosomal dominant for Van der Woude syndrome/IRF6, etc.) (cheng2023geneticinheritancemodels pages 2-5).

### Population Demographics
Males have a higher prevalence of CL/P than females (male:female ratio approximately 1.6:1), while isolated CP shows more equal sex distribution (wang2025globalregionaland pages 1-2, wang2023globalregionaland pages 1-2, jaruga2022orofacialcleftand pages 3-5). Ethnic variation is notable: American Indians show the highest rate (3.6 per 1,000), followed by Asians and Whites, with African Americans having the lowest incidence (~0.5 per 1,000) (im2025molecularregulationof pages 5-6, jaruga2022orofacialcleftand pages 3-5). Geographically, CL/P occurs more frequently in China, Japan, and Latin America but is less common in Israel, South Africa, and Southern Europe (jaruga2022orofacialcleftand pages 3-5). In 2021, South Asia, North Africa/Middle East, and Central Asia had the highest prevalence rates (wang2025globalregionaland pages 1-2, ma2025burdenoforofacial pages 1-2).

---

## 10. Diagnostics

### Clinical Diagnosis
CL/P is primarily diagnosed by physical examination at birth. Prenatal detection via ultrasound is possible, particularly for cleft lip; cleft palate alone is more difficult to detect prenatally. AI-based prenatal ultrasound systems utilizing deep learning (e.g., YOLOv5) have achieved AUC of 0.971 for standard coronal nasal-lip sections in single-center studies (wongsirichat2022theprevalenceof pages 5-6).

### Genetic Testing
Given the complex genetic architecture, genetic testing approaches include:
- **Chromosomal microarray (CMA):** For detecting copy number variants and regions of homozygosity
- **Gene panels:** Targeting known CL/P genes (IRF6, MSX1, CDH1, TP63, ARHGAP29, CTNND1, etc.)
- **Whole exome/genome sequencing (WES/WGS):** For identifying rare de novo and inherited variants, particularly useful in unexplained syndromic presentations
- **Karyotyping:** For ruling out chromosomal abnormalities in syndromic cases

### Differential Diagnosis
- Isolated CL vs. CLP vs. CP
- Nonsyndromic vs. syndromic forms (>400 syndromes including Van der Woude, Pierre Robin, DiGeorge/22q11.2 deletion, Treacher Collins, EEC syndrome)
- Submucosal cleft palate (may be clinically occult)

### Screening
Prenatal ultrasound (routine second-trimester anatomy scan), newborn physical examination. Cascade genetic testing is recommended for families with affected members.

---

## 11. Outcome/Prognosis

### Survival and Mortality
Global mortality from orofacial clefts was 1,719 deaths in 2021, with 408,775 DALYs (ma2025burdenoforofacial pages 1-2). Mortality has declined 86.08% from 1990–2021 globally (ma2025burdenoforofacial pages 1-2). Isolated CLP cases have the highest survival rate at 97.7%, while cases associated with genetic/chromosomal syndromes have significantly worse survival at 40.9% (goldrick2023amultiprogramanalysis pages 8-10). Long-term outcomes include increased mortality compared with unaffected siblings (wongsirichat2022theprevalenceof pages 1-2).

### Morbidity
The age-standardized DALY rate was 5.8 per 100,000 in 2021, with burden strongly correlating with socioeconomic development (wang2025globalregionaland pages 1-2, ma2025burdenoforofacial pages 7-9). Morbidity is lifelong, encompassing feeding difficulties, speech impairment, hearing loss, dental anomalies, psychological/social impacts, and maxillofacial growth disturbances (wongsirichat2022theprevalenceof pages 1-2).

### Treatment Burden
Patients with complete BCLP require an average of 5.9 surgical operations to complete treatment (hattori2023longtermtreatmentoutcome pages 1-2). Revisional lip/nose surgery was performed in 73% of patients, with VPI surgery in 59% and orthognathic surgery in 60.7% (hattori2023longtermtreatmentoutcome pages 1-2, hattori2023longtermtreatmentoutcome pages 5-6).

---

## 12. Treatment

### Surgical Interventions (MAXO:0000004, Surgical procedure)

Treatment follows a staged, multidisciplinary protocol:
- **Presurgical nasoalveolar molding (NAM):** Performed in early infancy to approximate cleft segments
- **Lip adhesion:** ~3 months of age (in selected cases)
- **Primary cheiloplasty (lip repair):** ~3–8 months (MAXO:0000004)
- **Palatoplasty (palate repair):** ~12–18 months, typically two-flap technique (NCT00829101 chunk 1, hattori2023longtermtreatmentoutcome pages 1-2, hattori2023longtermtreatmentoutcome pages 5-6)
- **VPI surgery:** As needed (pharyngeal flap or sphincter pharyngoplasty)
- **Alveolar bone grafting:** ~9–10 years of age
- **Orthodontic treatment:** Throughout childhood and adolescence
- **Orthognathic surgery:** At skeletal maturity (~18 years), applied in 60.7% of BCLP patients with midface retrusion; 97.3% underwent two-jaw surgery (hattori2023longtermtreatmentoutcome pages 1-2)
- **Revisional rhinoplasty/lip surgery:** After skeletal maturity for esthetic enhancement (hattori2023longtermtreatmentoutcome pages 5-6)

### Supportive and Rehabilitative Care
- **Speech therapy (MAXO:0000930):** Essential for managing VPI and articulation disorders
- **Audiology management:** Monitoring for otitis media and hearing loss
- **Psychological support (MAXO:0000016):** Addressing social adjustment and self-esteem
- **Nutritional support:** Specialized feeding techniques and devices in infancy

### Experimental Treatments
Active clinical trials include:
- **BIOCLEFT (NCT06408337):** Phase I-IIa evaluating safety and efficacy of a tissue-engineered product for cleft palate treatment
- **AI applications (NCT04342234, NCT06970158):** Neural network-based morphological assessment and clinical decision support
- **Analgesic innovations (NCT04928352, NCT04771156):** Nebulized bupivacaine and ketorolac for post-palatoplasty pain management

---

## 13. Prevention

### Primary Prevention
- **Folic acid supplementation:** Periconceptional supplementation (≥400 µg/day) is the most established primary prevention strategy (viswapurna2024roleofepigenetics pages 3-4, im2025molecularregulationof pages 46-47, viswapurna2024roleofepigenetics pages 7-8)
- **Smoking cessation:** Given the significant dose-dependent risk (OR up to 4.2 for heavy smoking) (viswapurna2024roleofepigenetics pages 3-4)
- **Maternal health optimization:** Managing pre-pregnancy diabetes, hypertension, and obesity (viswapurna2024roleofepigenetics pages 3-4)
- **Avoidance of teratogens:** Including excess alcohol, retinoids, and certain medications during first trimester

### Secondary Prevention
- **Prenatal ultrasound screening:** Routine second-trimester anatomy scan for early detection
- **Genetic counseling (MAXO:0000079):** Risk assessment for families with history of CL/P, particularly given 4–10% recurrence risk (im2025molecularregulationof pages 5-6)
- **Preimplantation genetic diagnosis:** Available for known monogenic syndromic forms

### Tertiary Prevention
- **Multidisciplinary team care:** Preventing complications through coordinated surgical, orthodontic, speech, audiology, and psychological management from birth through adulthood (hattori2023longtermtreatmentoutcome pages 1-2, wongsirichat2022theprevalenceof pages 1-2)

---

## 14. Other Species / Natural Disease

Orofacial clefts occur naturally in multiple species, most notably in dogs (particularly brachycephalic breeds including Bulldogs, Boxers, and Labrador Retrievers), cats, cattle, sheep, and horses. The condition is documented in OMIA (Online Mendelian Inheritance in Animals).

### Comparative Biology
The developmental mechanisms underlying palatal fusion are highly conserved across vertebrates. Key signaling pathways (SHH, BMP, FGF, TGF-β, WNT) controlling palatogenesis are conserved from zebrafish to humans, enabling cross-species study of cleft mechanisms (alhazmi2024theapplicationof pages 1-3, jaruga2022orofacialcleftand pages 13-15).

---

## 15. Model Organisms

### Mouse Models (Mus musculus; NCBI Taxon: 10090)
The mouse is the preeminent animal model for studying CL/P, with 395 genes identified in mice and 131 in humans related to cleft palate as of 2021 (iwaya2023micrornasandgene pages 6-8). A total of 365 mouse strains exhibit complete cleft of the secondary palate (CPO), 44 strains show CLP, 14 display anterior cleft palate, 16 present posterior/soft palate cleft, and 37 have submucous cleft palate (iwaya2023micrornasandgene pages 6-8). Key knockout models include:
- **Fgf10−/−:** Cleft palate with impaired palatal shelf outgrowth (won2023generegulatorynetworks pages 4-5)
- **Msx1-null:** Cleft palate, rescued by Dlx5 modulation of Shh signaling (won2023generegulatorynetworks pages 13-14)
- **Tgfbr2 conditional inactivation in cranial neural crest:** Cleft palate and calvarial defects (won2023generegulatorynetworks pages 13-14)
- **Osr2−/−; Pax9−/−:** Cleft palate (won2023generegulatorynetworks pages 4-5)
- **Foxf1/Foxf2 ablation in neural crest:** Defective palatal outgrowth (won2023generegulatorynetworks pages 4-5)
- **DicerF/F;Wnt1-Cre:** Severe craniofacial deformities including cleft palate (iwaya2023micrornasandgene pages 2-4)
- **Bmpr1a conditional loss in neural crest:** Severe craniofacial defects (im2025molecularregulationof pages 12-13)

### Zebrafish Models (Danio rerio; NCBI Taxon: 7955)
Zebrafish have emerged as a powerful complementary model. The zebrafish ethmoid plate serves as the functional equivalent of the mammalian palate. Genetic control of palatal development is conserved across vertebrates, enabling study of human cleft genes (alhazmi2024theapplicationof pages 1-3, jaruga2022orofacialcleftand pages 13-15). IRF6-deficient zebrafish demonstrate a cleft phenotype, with downstream genes GRHL3, KLF17, and ESRP1/2 also critical (alhazmi2024theapplicationof pages 1-3). Advantages include transparent embryos, rapid external development, and amenability to CRISPR/Cas9 editing (alhazmi2024theapplicationof pages 1-3, jaruga2022orofacialcleftand pages 13-15).

### Xenopus Models (NCBI Taxon: 8364)
Xenopus has emerged as a powerful model for investigating craniofacial morphogenesis, owing to external fertilization, large experimentally accessible embryos, and evolutionarily conserved developmental pathways. These allow direct in vivo visualization and manipulation of cranial neural crest cell behaviors at single-cell resolution (jaruga2022orofacialcleftand pages 13-15).

### Model Limitations
Mouse palate development occurs in utero, limiting real-time observation (jaruga2022orofacialcleftand pages 13-15). Zebrafish, while genetically manipulable, have anatomical differences from mammalian palates (alhazmi2024theapplicationof pages 1-3). No single model fully recapitulates all aspects of human CL/P, necessitating multi-model approaches (jaruga2022orofacialcleftand pages 13-15).

---

## Summary

Cleft lip and/or palate is a complex congenital malformation with global prevalence of approximately 1 in 700 births, imposing substantial morbidity particularly in low- and middle-income countries. The condition arises from disrupted palatogenesis involving multiple conserved signaling pathways (TGF-β, BMP, SHH, WNT, FGF) and is influenced by both genetic susceptibility (IRF6, MSX1, BMP4, TP63, ARHGAP29, and many others) and environmental factors (maternal smoking, folate deficiency, diabetes). Treatment requires lifelong, staged, multidisciplinary management including multiple surgical procedures, orthodontic care, speech therapy, and psychological support. Primary prevention through periconceptional folic acid supplementation and maternal health optimization represents the most actionable public health intervention. Advances in genomics, AI-assisted diagnostics, and tissue engineering (BIOCLEFT trial) represent promising frontiers in CL/P research and care.

References

1. (ma2025burdenoforofacial pages 1-2): Qinqin Ma, Jie Wei, Bo Peng, Jianying Liu, and Shuixue Mo. Burden of orofacial clefts from 1990–2021 at global, regional, and national levels. Frontiers in Pediatrics, Mar 2025. URL: https://doi.org/10.3389/fped.2025.1502877, doi:10.3389/fped.2025.1502877. This article has 15 citations.

2. (im2025molecularregulationof pages 5-6): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

3. (won2023generegulatorynetworks pages 1-2): Hyung-Jin Won, Jin-Woo Kim, Hyung-Sun Won, and Jeong-Oh Shin. Gene regulatory networks and signaling pathways in palatogenesis and cleft palate: a comprehensive review. Cells, 12:1954, Jul 2023. URL: https://doi.org/10.3390/cells12151954, doi:10.3390/cells12151954. This article has 34 citations.

4. (jaruga2022orofacialcleftand pages 3-5): Anna Jaruga, Jakub Ksiazkiewicz, Krystian Kuzniarz, and Przemko Tylzanowski. Orofacial cleft and mandibular prognathism—human genetics and animal models. International Journal of Molecular Sciences, 23:953, Jan 2022. URL: https://doi.org/10.3390/ijms23020953, doi:10.3390/ijms23020953. This article has 25 citations.

5. (OpenTargets Search: cleft lip,cleft palate): Open Targets Query (cleft lip,cleft palate, 21 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (jaruga2022orofacialcleftand pages 5-6): Anna Jaruga, Jakub Ksiazkiewicz, Krystian Kuzniarz, and Przemko Tylzanowski. Orofacial cleft and mandibular prognathism—human genetics and animal models. International Journal of Molecular Sciences, 23:953, Jan 2022. URL: https://doi.org/10.3390/ijms23020953, doi:10.3390/ijms23020953. This article has 25 citations.

7. (cheng2023geneticinheritancemodels pages 2-5): Xi Cheng, Fengzhou Du, Xiao Long, and Jiuzuo Huang. Genetic inheritance models of non-syndromic cleft lip with or without palate: from monogenic to polygenic. Genes, 14:1859, Sep 2023. URL: https://doi.org/10.3390/genes14101859, doi:10.3390/genes14101859. This article has 22 citations.

8. (rahimov2024highincidenceand pages 1-4): Fedik Rahimov, Pekka Nieminen, Priyanka Kumari, Emma Juuri, Tiit Nikopensius, Kitt Paraiso, Jakob German, Antti Karvanen, Mart Kals, Abdelrahman G. Elnahas, Juha Karjalainen, Mitja Kurki, Aarno Palotie, Arja Heliövaara, Tõnu Esko, Sakari Jukarainen, Priit Palta, Andrea Ganna, Anjali P. Patni, Daniel Mar, Karol Bomsztyk, Julie Mathieu, Hannele Ruohola-Baker, Axel Visel, Walid D. Fakhouri, Brian C. Schutte, Robert A. Cornell, and David P. Rice. High incidence and geographic distribution of cleft palate cases in finland are associated with a regulatory variant in irf6. medRxiv : the preprint server for health sciences, Jul 2024. URL: https://doi.org/10.1101/2024.07.09.24310146, doi:10.1101/2024.07.09.24310146. This article has 2 citations.

9. (cheng2023geneticinheritancemodels pages 5-6): Xi Cheng, Fengzhou Du, Xiao Long, and Jiuzuo Huang. Genetic inheritance models of non-syndromic cleft lip with or without palate: from monogenic to polygenic. Genes, 14:1859, Sep 2023. URL: https://doi.org/10.3390/genes14101859, doi:10.3390/genes14101859. This article has 22 citations.

10. (im2025molecularregulationof pages 6-8): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

11. (im2025molecularregulationof pages 16-18): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

12. (cheng2023geneticinheritancemodels pages 11-12): Xi Cheng, Fengzhou Du, Xiao Long, and Jiuzuo Huang. Genetic inheritance models of non-syndromic cleft lip with or without palate: from monogenic to polygenic. Genes, 14:1859, Sep 2023. URL: https://doi.org/10.3390/genes14101859, doi:10.3390/genes14101859. This article has 22 citations.

13. (won2023generegulatorynetworks pages 13-14): Hyung-Jin Won, Jin-Woo Kim, Hyung-Sun Won, and Jeong-Oh Shin. Gene regulatory networks and signaling pathways in palatogenesis and cleft palate: a comprehensive review. Cells, 12:1954, Jul 2023. URL: https://doi.org/10.3390/cells12151954, doi:10.3390/cells12151954. This article has 34 citations.

14. (im2025molecularregulationof pages 36-37): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

15. (im2025molecularregulationof pages 12-13): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

16. (won2023generegulatorynetworks pages 8-10): Hyung-Jin Won, Jin-Woo Kim, Hyung-Sun Won, and Jeong-Oh Shin. Gene regulatory networks and signaling pathways in palatogenesis and cleft palate: a comprehensive review. Cells, 12:1954, Jul 2023. URL: https://doi.org/10.3390/cells12151954, doi:10.3390/cells12151954. This article has 34 citations.

17. (im2025molecularregulationof pages 15-16): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

18. (im2025molecularregulationof pages 24-26): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

19. (cheng2023geneticinheritancemodels pages 12-14): Xi Cheng, Fengzhou Du, Xiao Long, and Jiuzuo Huang. Genetic inheritance models of non-syndromic cleft lip with or without palate: from monogenic to polygenic. Genes, 14:1859, Sep 2023. URL: https://doi.org/10.3390/genes14101859, doi:10.3390/genes14101859. This article has 22 citations.

20. (alhazmi2024theapplicationof pages 1-3): Nora Alhazmi, Khalid A. Alamoud, Farraj Albalawi, Bassam Alalola, and Fathima F. Farook. The application of zebrafish model in the study of cleft lip and palate development: a systematic review. Heliyon, 10:e28322, Mar 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e28322, doi:10.1016/j.heliyon.2024.e28322. This article has 4 citations.

21. (im2025molecularregulationof pages 9-12): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

22. (viswapurna2024roleofepigenetics pages 3-4): Amritaa Viswapurna. Role of epigenetics, environmental and chemical agents in nonsyndromic orofacial clefts. International Journal of High School Research, 6:16-23, Jul 2024. URL: https://doi.org/10.36838/v6i7.4, doi:10.36838/v6i7.4. This article has 0 citations.

23. (im2025molecularregulationof pages 46-47): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

24. (iwaya2023micrornasandgene pages 10-12): Chihiro Iwaya, Akiko Suzuki, and Junichi Iwata. Micrornas and gene regulatory networks related to cleft lip and palate. International Journal of Molecular Sciences, 24:3552, Feb 2023. URL: https://doi.org/10.3390/ijms24043552, doi:10.3390/ijms24043552. This article has 22 citations.

25. (viswapurna2024roleofepigenetics pages 7-8): Amritaa Viswapurna. Role of epigenetics, environmental and chemical agents in nonsyndromic orofacial clefts. International Journal of High School Research, 6:16-23, Jul 2024. URL: https://doi.org/10.36838/v6i7.4, doi:10.36838/v6i7.4. This article has 0 citations.

26. (viswapurna2024roleofepigenetics pages 2-3): Amritaa Viswapurna. Role of epigenetics, environmental and chemical agents in nonsyndromic orofacial clefts. International Journal of High School Research, 6:16-23, Jul 2024. URL: https://doi.org/10.36838/v6i7.4, doi:10.36838/v6i7.4. This article has 0 citations.

27. (alghonemy2025metaanalysisandsystematic pages 7-7): Wafaa Yahia Alghonemy and Mohamed Gaber Ashmawy. Meta-analysis and systematic review for the genetic basis of cleft lip and palate. Journal of Oral Biology and Craniofacial Research, 15:146-152, Jan 2025. URL: https://doi.org/10.1016/j.jobcr.2024.12.012, doi:10.1016/j.jobcr.2024.12.012. This article has 7 citations.

28. (cheng2023geneticinheritancemodels pages 14-15): Xi Cheng, Fengzhou Du, Xiao Long, and Jiuzuo Huang. Genetic inheritance models of non-syndromic cleft lip with or without palate: from monogenic to polygenic. Genes, 14:1859, Sep 2023. URL: https://doi.org/10.3390/genes14101859, doi:10.3390/genes14101859. This article has 22 citations.

29. (wongsirichat2022theprevalenceof pages 2-5): Nattharin Wongsirichat, Basel Mahardawi, Montien Manosudprasit, Aggasit Manosudprasit, and Natthamet Wongsirichat. The prevalence of cleft lip and palate and their effect on growth and development: a narrative review. Siriraj Medical Journal, 74:819-827, Nov 2022. URL: https://doi.org/10.33192/smj.2022.96, doi:10.33192/smj.2022.96. This article has 6 citations.

30. (wongsirichat2022theprevalenceof pages 5-6): Nattharin Wongsirichat, Basel Mahardawi, Montien Manosudprasit, Aggasit Manosudprasit, and Natthamet Wongsirichat. The prevalence of cleft lip and palate and their effect on growth and development: a narrative review. Siriraj Medical Journal, 74:819-827, Nov 2022. URL: https://doi.org/10.33192/smj.2022.96, doi:10.33192/smj.2022.96. This article has 6 citations.

31. (hattori2023longtermtreatmentoutcome pages 1-2): Yoshitsugu Hattori, Betty C.-J. Pai, Takafumi Saito, Pang-Yun Chou, Ting-Chen Lu, Chun-Shin Chang, Yu-Ray Chen, and Lun-Jou Lo. Long-term treatment outcome of patients with complete bilateral cleft lip and palate: a retrospective cohort study. International Journal of Surgery (London, England), 109:1656-1667, Apr 2023. URL: https://doi.org/10.1097/js9.0000000000000406, doi:10.1097/js9.0000000000000406. This article has 47 citations.

32. (NCT00829101 chunk 1):  Articulation and Phonology in Children With Unilateral Cleft Lip and Palate. Region Skane. 2009. ClinicalTrials.gov Identifier: NCT00829101

33. (wongsirichat2022theprevalenceof pages 1-2): Nattharin Wongsirichat, Basel Mahardawi, Montien Manosudprasit, Aggasit Manosudprasit, and Natthamet Wongsirichat. The prevalence of cleft lip and palate and their effect on growth and development: a narrative review. Siriraj Medical Journal, 74:819-827, Nov 2022. URL: https://doi.org/10.33192/smj.2022.96, doi:10.33192/smj.2022.96. This article has 6 citations.

34. (viswapurna2024roleofepigenetics pages 4-5): Amritaa Viswapurna. Role of epigenetics, environmental and chemical agents in nonsyndromic orofacial clefts. International Journal of High School Research, 6:16-23, Jul 2024. URL: https://doi.org/10.36838/v6i7.4, doi:10.36838/v6i7.4. This article has 0 citations.

35. (im2025molecularregulationof pages 23-24): Hyuna Im, Yujeong Song, Young Hyun Jung, Jae Kyeom Kim, Dae-Kyoon Park, Duk-Soo Kim, Hankyu Kim, and Jeong-Oh Shin. Molecular regulation of palatogenesis and clefting: an integrative analysis of genetic, epigenetic networks, and environmental interactions. International Journal of Molecular Sciences, Feb 2025. URL: https://doi.org/10.3390/ijms26031382, doi:10.3390/ijms26031382. This article has 18 citations.

36. (iwaya2023micrornasandgene pages 4-6): Chihiro Iwaya, Akiko Suzuki, and Junichi Iwata. Micrornas and gene regulatory networks related to cleft lip and palate. International Journal of Molecular Sciences, 24:3552, Feb 2023. URL: https://doi.org/10.3390/ijms24043552, doi:10.3390/ijms24043552. This article has 22 citations.

37. (won2023generegulatorynetworks pages 5-7): Hyung-Jin Won, Jin-Woo Kim, Hyung-Sun Won, and Jeong-Oh Shin. Gene regulatory networks and signaling pathways in palatogenesis and cleft palate: a comprehensive review. Cells, 12:1954, Jul 2023. URL: https://doi.org/10.3390/cells12151954, doi:10.3390/cells12151954. This article has 34 citations.

38. (won2023generegulatorynetworks pages 4-5): Hyung-Jin Won, Jin-Woo Kim, Hyung-Sun Won, and Jeong-Oh Shin. Gene regulatory networks and signaling pathways in palatogenesis and cleft palate: a comprehensive review. Cells, 12:1954, Jul 2023. URL: https://doi.org/10.3390/cells12151954, doi:10.3390/cells12151954. This article has 34 citations.

39. (wang2025globalregionaland pages 1-2): Zhenghao Wang, Weikun Qi, Yiru Chen, and Feng Niu. Global, regional, and national burden of orofacial clefts, 1990–2021: an analysis of data from the global burden of disease study 2021. Frontiers in Medicine, Jun 2025. URL: https://doi.org/10.3389/fmed.2025.1609700, doi:10.3389/fmed.2025.1609700. This article has 7 citations.

40. (ma2025burdenoforofacial pages 7-9): Qinqin Ma, Jie Wei, Bo Peng, Jianying Liu, and Shuixue Mo. Burden of orofacial clefts from 1990–2021 at global, regional, and national levels. Frontiers in Pediatrics, Mar 2025. URL: https://doi.org/10.3389/fped.2025.1502877, doi:10.3389/fped.2025.1502877. This article has 15 citations.

41. (goldrick2023amultiprogramanalysis pages 8-10): Niall Mc Goldrick, Gavin Revie, Boris Groisman, Paula Hurtado‐Villa, Antonin Sipek, Babak Khoshnood, Anke Rissmann, Saeed Dastgiri, Danielle Landau, Giovanna Tagliabue, Anna Pierini, Miriam Gatt, Osvaldo M. Mutchinick, Laura Martínez, Hermein E.K. de Walle, Elena Szabova, Jorge Lopez Camelo, Karin Källén, Margery Morgan, Wladimir Wertelecki, Amy Nance, Erin B. Stallings, Wendy N. Nembhard, and Peter Mossey. A multi-program analysis of cleft lip with cleft palate prevalence and mortality using data from 22 international clearinghouse for birth defects surveillance and research programs, 1974–2014. Birth defects research, 115:980-997, Apr 2023. URL: https://doi.org/10.1002/bdr2.2176, doi:10.1002/bdr2.2176. This article has 25 citations and is from a peer-reviewed journal.

42. (wang2023globalregionaland pages 1-2): Dawei Wang, Boyu Zhang, Qi Zhang, and Yiping Wu. Global, regional and national burden of orofacial clefts from 1990 to 2019: an analysis of the global burden of disease study 2019. Annals of Medicine, May 2023. URL: https://doi.org/10.1080/07853890.2023.2215540, doi:10.1080/07853890.2023.2215540. This article has 63 citations and is from a domain leading peer-reviewed journal.

43. (hattori2023longtermtreatmentoutcome pages 5-6): Yoshitsugu Hattori, Betty C.-J. Pai, Takafumi Saito, Pang-Yun Chou, Ting-Chen Lu, Chun-Shin Chang, Yu-Ray Chen, and Lun-Jou Lo. Long-term treatment outcome of patients with complete bilateral cleft lip and palate: a retrospective cohort study. International Journal of Surgery (London, England), 109:1656-1667, Apr 2023. URL: https://doi.org/10.1097/js9.0000000000000406, doi:10.1097/js9.0000000000000406. This article has 47 citations.

44. (jaruga2022orofacialcleftand pages 13-15): Anna Jaruga, Jakub Ksiazkiewicz, Krystian Kuzniarz, and Przemko Tylzanowski. Orofacial cleft and mandibular prognathism—human genetics and animal models. International Journal of Molecular Sciences, 23:953, Jan 2022. URL: https://doi.org/10.3390/ijms23020953, doi:10.3390/ijms23020953. This article has 25 citations.

45. (iwaya2023micrornasandgene pages 6-8): Chihiro Iwaya, Akiko Suzuki, and Junichi Iwata. Micrornas and gene regulatory networks related to cleft lip and palate. International Journal of Molecular Sciences, 24:3552, Feb 2023. URL: https://doi.org/10.3390/ijms24043552, doi:10.3390/ijms24043552. This article has 22 citations.

46. (iwaya2023micrornasandgene pages 2-4): Chihiro Iwaya, Akiko Suzuki, and Junichi Iwata. Micrornas and gene regulatory networks related to cleft lip and palate. International Journal of Molecular Sciences, 24:3552, Feb 2023. URL: https://doi.org/10.3390/ijms24043552, doi:10.3390/ijms24043552. This article has 22 citations.

## Artifacts

- [Edison artifact artifact-00](Cleft_Lip_Palate-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Cleft_Lip_Palate-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Cleft_Lip_Palate-deep-research-falcon_artifacts/artifact-02.md)