---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-24T11:50:33.995572'
end_time: '2026-07-24T11:59:52.639824'
duration_seconds: 558.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hajdu-Cheney Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hajdu-Cheney_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hajdu-Cheney Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hajdu-Cheney Syndrome** covering all of the
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
- **Disease Name:** Hajdu-Cheney Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hajdu-Cheney Syndrome** covering all of the
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


# Hajdu–Cheney syndrome: comprehensive disease-characteristics report

## Executive summary

Hajdu–Cheney syndrome (HCS) is an ultra-rare, progressive, autosomal-dominant skeletal dysplasia caused by heterozygous gain-of-function variants in **NOTCH2**. Its defining manifestations are distal phalangeal acro-osteolysis and generalized osteoporosis, accompanied variably by short stature, craniofacial dysmorphism, wormian bones, dental disease, vertebral deformity, skull-base abnormalities, renal cysts, congenital cardiac defects, and respiratory or neurologic complications. Published prevalence is **<1 per 1,000,000**, but this estimate is uncertain because only approximately 50–100 patients had been described in historical reviews. Evidence is therefore dominated by case reports, small family series, reviews, and engineered mice—not registries or large prospective cohorts. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2)

The causal variants are predominantly nonsense or small deletion/frameshift variants in **exon 34**, the terminal exon of NOTCH2. They truncate the receptor before its PEST degradation domain, stabilize the NOTCH2 intracellular domain (NICD2), and prolong canonical signaling. Experimental evidence supports increased osteoclastogenesis and high-turnover bone loss, although reduced or dysregulated bone formation may also contribute. There is no curative or approved disease-specific treatment; surveillance, rehabilitation, fracture prevention, dental care, and complication-directed surgery are central. Antiresorptive or anabolic drugs have only low-level, case-based evidence. (canalis2014hajducheneysyndromea pages 1-2, canalis2014hajducheneysyndromea pages 5-6, cortesmartin2020hajdu–cheneysyndromea pages 9-13, canalis2016hajducheneymouse pages 1-2)

The following table provides a curation-oriented synopsis.

| Domain | Knowledge-base statement | Evidence type/strength | Suggested ontology terms |
|---|---|---|---|
| Identity / epidemiology | Hajdu-Cheney syndrome (HCS) is an ultra-rare Mendelian connective-tissue/skeletal disorder characterized by acro-osteolysis and generalized osteoporosis; commonly cited identifiers include ORPHA:955, OMIM #102500, and MONDO:0007057 (acroosteolysis dominant type / Hajdu-Cheney syndrome groupings). Reported prevalence is **<1/1,000,000** and historical literature reviews estimate roughly **50-100 described cases**, indicating that most current knowledge comes from aggregated case reports/reviews rather than EHR-scale cohorts. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 3-6, OpenTargets Search: Hajdu-Cheney syndrome-NOTCH2) | Human clinical aggregated review evidence; moderate for definition/rarity, low for exact prevalence because of ascertainment and historical undercount. | MONDO:0007057; MeSH: use disease name if mapping required; HCS synonyms: acroosteolysis dominant type, serpentine fibula-polycystic kidney syndrome |
| Genetics / inheritance | HCS is usually **autosomal dominant** and caused by **heterozygous germline NOTCH2** pathogenic variants, typically **nonsense or small deletion/frameshift variants in exon 34**. Many cases are de novo/sporadic, but familial transmission is established. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, canalis2016hajducheneymouse pages 1-2) | Human genetics + review evidence; strong for causal gene/inheritance. | HGNC:7882 **NOTCH2**; inheritance: autosomal dominant |
| Variant mechanism | Pathogenic variants truncate NOTCH2 **upstream of the PEST domain**, preserving signaling machinery but impairing NICD2 degradation, producing a **stabilized gain-of-function receptor** with excessive NOTCH2 signaling. (canalis2014hajducheneysyndromea pages 1-2, canalis2014hajducheneysyndromea pages 5-6, cortesmartin2020hajdu–cheneysyndromea pages 9-13, canalis2016hajducheneymouse pages 1-2, canalis2016hajducheneymouse pages 18-19) | Human molecular genetics + engineered mouse knock-in; strong for gain-of-function mechanism. | GO:0007219 Notch signaling pathway; protein region: PEST domain |
| Pathophysiology / mechanism | Current disease model supports **high-turnover bone loss** with increased osteoclastogenesis/bone resorption and relative dysregulation of bone formation. NOTCH2 activation is linked to pro-osteoclastogenic mediators such as **NFATC1**, **RANKL**, and **IL6**; mouse studies show osteopenia, increased osteoclast number, and increased bone resorption. (canalis2014hajducheneysyndromea pages 1-2, canalis2014hajducheneysyndromea pages 5-6, cortesmartin2020hajdu–cheneysyndromea pages 9-13, ballhause2023fracturehealingin pages 7-8, canalis2016hajducheneymouse pages 1-2) | Mechanistic review + knock-in mouse functional evidence; moderate-strong. | GO:0045453 bone resorption; GO:0030316 osteoclast differentiation; GO:0001649 osteoblast differentiation; CL:0000090 osteoclast; CL:0000062 osteoblast |
| Cardinal skeletal phenotypes | Core manifestations are **acro-osteolysis of distal phalanges**, **osteoporosis/osteopenia**, short stature, fractures, wormian bones, kyphoscoliosis, vertebral anomalies/collapse, serpentine fibula, joint laxity, and progressive distal bone resorption. These features are variable but progressive over time. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13) | Human case-series/review evidence; strong for recurrent phenotype set, low for precise frequency percentages. | HP:0001841 Acroosteolysis; HP:0000939 Osteoporosis; HP:0004322 Short stature; HP:0000928 Scoliosis; HP:0008466 Wormian bones |
| Craniofacial / dental / neurologic / renal / cardiovascular phenotypes | Frequent extra-appendicular features include coarse/dysmorphic facies, micrognathia, hypertelorism/telecanthus, high-arched palate, delayed/premature tooth loss, malocclusion, basilar invagination/platybasia, hydrocephalus, hearing issues, renal cysts/polcystic kidneys, congenital heart disease/patent ductus arteriosus, and recurrent respiratory infections from thoracic deformity. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13, cortesmartin2022hajducheneysyndromea pages 8-11) | Human review + case evidence; moderate. | HP:0000347 Micrognathia; HP:0000235 Hydrocephalus; HP:0000107 Renal cyst; HP:0001643 Patent ductus arteriosus; UBERON:0002101 skull; UBERON:0001134 kidney |
| Temporal course | Onset is often **congenital or early childhood**, with early craniofacial/hand findings and later progressive skeletal fragility. The course is **chronic, age-dependent, and progressive**, with increasing disability risk from fractures, vertebral collapse, and skull-base complications. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 12-14, cortesmartin2020hajdu–cheneysyndromea pages 9-13, cortesmartin2022hajducheneysyndromea pages 8-11) | Human longitudinal case/review evidence; moderate. | HPO onset terms: congenital onset, childhood onset; course descriptors: progressive |
| Diagnostics | Diagnosis is primarily **clinical-radiologic plus molecular**. Imaging may show distal phalangeal acro-osteolysis, wormian bones, platybasia/basilar invagination, vertebral deformities, serpentine fibula, and renal cysts. **Genetic confirmation** is typically by sequencing **NOTCH2**, especially exon 34; broad exome/panel testing is useful when phenotype is unclear or syndromic short stature is present. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13, cortesmartin2022hajducheneysyndromea pages 8-11) | Human clinical/review evidence; strong for gene testing utility, moderate for formal criteria. | MAXO: genetic testing; imaging terms: radiography, MRI, ultrasound; NOTCH2 single-gene testing / exome sequencing |
| Differential diagnosis | Important differentials for acro-osteolysis and overlapping syndromic features include **systemic sclerosis/scleroderma**, sarcoidosis, hyperparathyroidism, local trauma/thermal injury, neuropathic causes, progeria, and **Alagille syndrome** or other NOTCH-related disorders. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, cortesmartin2022hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13) | Review evidence; moderate. | HPO anchor feature: Acroosteolysis; related disease names as differential set |
| Treatment / management | There is **no curative therapy**. Management is multidisciplinary and complication-directed: bone health surveillance, fracture prevention, orthopedic/neurosurgical management, respiratory and renal monitoring, dental care, and rehabilitation. **Bisphosphonates** are the most commonly reported pharmacologic intervention; denosumab, pamidronate, zoledronic acid, teriparatide, and romosozumab have only case-level/off-label evidence with variable benefit. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, cortesmartin2020hajdu–cheneysyndromea pages 7-9, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 12-14, cortesmartin2022hajducheneysyndromea pages 1-2, kaczorukwieremczuk2021oralsurgeryprocedures pages 3-10) | Human case reports/reviews; low-moderate for drug efficacy, strong that no standard curative therapy exists. | MAXO: bisphosphonate therapy; denosumab therapy; physical therapy / rehabilitation; surgical management |
| Real-world implementation / safety | Real-world care issues include rehabilitation approaches (e.g., gait-focused vibrotherapy/physiotherapy), dental extraction/implant planning, and antiresorptive safety concerns such as delayed oral healing and medication-related osteonecrosis of the jaw risk in denosumab-treated patients. (cortesmartin2022hajducheneysyndromea pages 12-14, kaczorukwieremczuk2021oralsurgeryprocedures pages 3-10, cortesmartin2022hajducheneysyndromea pages 8-11) | Human case evidence; low but clinically actionable. | MAXO: dental procedure management; physical therapy; supportive care |
| Prognosis | Life expectancy is not well quantified, but morbidity can be substantial due to fractures, vertebral compression/collapse, ventilatory restriction, basilar invagination, hydrocephalus, and rare sudden death/central respiratory complications. Prognosis depends on severity of skeletal and skull-base disease and adequacy of surveillance/intervention. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13) | Review evidence; low-moderate because no registry-scale survival data. | Prognostic features: basilar invagination, fractures, ventilatory restriction |
| Research gaps / omics | No disease-specific **single-cell**, **spatial transcriptomic**, **proteomic**, **metabolomic**, or large natural-history registry dataset was identified in the retrieved evidence; current knowledge remains dominated by case reports, reviews, and mouse models. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, cortesmartin2020hajdu–cheneysyndromea pages 3-6) | Absence-of-evidence statement from available literature set; low but important for KB completeness. | Evidence gap annotation; omics not available / not established |
| Experimental models | Engineered **heterozygous Notch2 knock-in mice** recapitulate major bone features of HCS, including short femora, cortical/cancellous osteopenia, increased osteoclastogenesis and bone resorption. In a 2023 fracture-healing model, overall structural healing appeared near-normal, but callus turnover was increased and **biomechanical stability of healed femora was impaired**. (ballhause2023fracturehealingin pages 1-2, ballhause2023fracturehealingin pages 10-11, canalis2016hajducheneymouse pages 1-2, canalis2016hajducheneymouse pages 18-19) | Primary in vivo model evidence; strong for skeletal mechanism/model utility. | Mouse model; CL:0000090 osteoclast; GO:0042060 wound healing; GO:0060348 bone development |
| Other species / natural disease | No convincing naturally occurring veterinary counterpart or zoonotic relevance was identified in the retrieved evidence; current comparative biology relies mainly on engineered murine models. (canalis2016hajducheneymouse pages 1-2, canalis2016hajducheneymouse pages 18-19) | Evidence gap / comparative inference; low. | NCBI Taxon: Mus musculus (model organism) |


*Table: This table condenses the most actionable disease-characterization points for Hajdu-Cheney syndrome into a knowledge-base format, with evidence strength and ontology suggestions. It is useful for rapid curation across clinical, molecular, and translational domains.*

## 1. Disease information

### Definition and identifiers

HCS is a Mendelian connective-tissue and skeletal disorder characterized by **progressive acro-osteolysis, severe low bone mass, skeletal dysplasia, and multisystem developmental abnormalities**. The disorder’s phenotype evolves with age, so absence of classic acro-osteolysis early in childhood does not exclude it. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, canalis2014hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13)

| Resource | Identifier / designation |
|---|---|
| MONDO | **MONDO:0007057**, acroosteolysis, dominant type |
| OMIM | **#102500**, Hajdu–Cheney syndrome |
| Orphanet | **ORPHA:955** |
| Open Targets | NOTCH2–MONDO:0007057 association; target ENSG00000134250 |
| ICD-10/ICD-11 | No highly specific HCS code was established in the retrieved evidence; coding generally falls under an appropriate congenital osteochondrodysplasia/other specified skeletal disorder category |
| MeSH | No uniquely disease-specific MeSH identifier was confirmed in the retrieved evidence; use “Hajdu-Cheney Syndrome” as a supplementary concept/search term where supported |

Open Targets reports five genetic/curation evidence items linking **NOTCH2** to MONDO:0007057, including literature evidence associated with PMID **21378985**, the landmark causal-gene report. (OpenTargets Search: Hajdu-Cheney syndrome-NOTCH2)

**Synonyms:** acro-osteolysis, dominant type; acroosteolysis with osteoporosis; acro-dento-osteo-dysplasia; arthro-dento-osteo dysplasia; Cheney syndrome; and serpentine fibula–polycystic kidney syndrome. The latter is now regarded as part of the HCS phenotypic spectrum, not a separate disorder. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 3-6, cortesmartin2020hajdu–cheneysyndromea pages 9-13)

**Data provenance:** almost all available information is aggregated disease-level evidence derived from published individual patients/families and model organisms. No EHR-scale cohort or population registry was identified.

## 2. Etiology and risk factors

### Causal factor

The primary cause is a **heterozygous germline pathogenic variant in NOTCH2**, usually a truncating variant in exon 34. Familial autosomal-dominant transmission and de novo cases both occur. This is not an environmentally caused, infectious, autoimmune, or lifestyle-mediated disorder. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2, canalis2016hajducheneymouse pages 1-2)

The landmark human genetic study is Simpson et al., *Nature Genetics*, published April 2011, “Mutations in NOTCH2 cause Hajdu-Cheney syndrome, a disorder of severe and progressive bone loss,” PMID **21378985**, DOI: https://doi.org/10.1038/ng.779. Open Targets independently links this PMID to the NOTCH2–HCS association. (OpenTargets Search: Hajdu-Cheney syndrome-NOTCH2)

### Risk and protective factors

* **Genetic risk:** inheriting a causal allele from an affected parent confers an a priori 50% transmission probability per pregnancy. De novo pathogenic variants explain many sporadic patients.
* **Modifiers:** no reproducible modifier gene, susceptibility locus, founder allele, or protective NOTCH2 allele has been established. Marked intrafamilial variability implies modifiers, stochastic developmental effects, age, or exposures, but these remain unproven.
* **Environment/lifestyle:** no exposure causes HCS. Falls, immobilization, low mechanical loading, poor nutrition, vitamin-D deficiency, and medications harmful to bone could plausibly amplify fragility, but disease-specific interaction estimates are unavailable.
* **Protective factors:** no genetic protection is known. Adequate calcium/vitamin-D status, safe weight-bearing activity, physiotherapy, healthy weight, and fall avoidance support skeletal health but do not prevent the genotype or reverse acro-osteolysis.
* **Gene–environment interaction:** no formal HCS G×E study was identified. A 2023 fracture study noted lifestyle factors as general determinants of non-union but did not establish an HCS-specific interaction. (ballhause2023fracturehealingin pages 1-2)

## 3. Phenotypes

Reliable percentages are generally unavailable: published samples are tiny, age-heterogeneous, and affected by reporting bias. “Cardinal,” “common,” or “variable” is therefore more defensible than numerical frequency except where noted.

| Phenotype/type | Onset, course, severity and impact | Suggested HPO term |
|---|---|---|
| Distal phalangeal acro-osteolysis; radiographic sign | Usually emerges/progresses in childhood; progressive and cardinal; causes shortening, pseudoclubbing, deformity, impaired grip/gait | **HP:0001841 Acroosteolysis** |
| Generalized osteoporosis/osteopenia; imaging/laboratory phenotype | Early-onset, progressive or persistently severe; fractures, pain, deformity and reduced mobility | **HP:0000939 Osteoporosis** |
| Recurrent/fragility fractures | Childhood onward; variable; non-union has been reported | HP:0002757 Recurrent fractures |
| Short stature | Childhood, variable, may worsen with vertebral collapse | **HP:0004322 Short stature** |
| Wormian bones/delayed cranial-suture closure | Congenital or early childhood; stable structural sign | **HP:0002645 Wormian bones**; curator should verify the artifact’s alternative ID before ingestion |
| Coarse/dysmorphic facies, micrognathia, hypertelorism/telecanthus, low-set ears, long philtrum | Features change with age; early synophrys/hypotelorism may give way to coarser childhood/adolescent facies | **HP:0000347 Micrognathia**, HP:0000316 Hypertelorism |
| Kyphosis/scoliosis, biconcave vertebrae and vertebral collapse | Progressive; moderate to severe; pain, height loss, restrictive ventilation | HP:0002808 Kyphosis; HP:0002650 Scoliosis; HP:0002953 Vertebral compression fracture |
| Joint laxity and long-bone deformity | Childhood onward; gait impairment and dislocation risk | HP:0001382 Joint hypermobility |
| Basilar invagination/platybasia | Variable but potentially life-threatening; may compress brainstem or cause syringomyelia/hydrocephalus | HP:0005758 Basilar invagination; HP:0002691 Platybasia |
| Dental eruption abnormalities, malocclusion, periodontitis, premature tooth loss/root or alveolar resorption | Childhood/adulthood; substantial feeding, speech and quality-of-life effects | HP:0006480 Premature loss of teeth; HP:0000689 Dental malocclusion |
| Renal cysts/polcystic kidneys | Variable; congenital to adult; occasionally renal impairment | **HP:0000107 Renal cyst** |
| Congenital heart disease/PDA/septal defects | Congenital, variably severe | **HP:0001643 Patent ductus arteriosus** |
| Recurrent respiratory infections/restrictive ventilation | Secondary to thoracic deformity and airway/ENT problems; episodic infections with potentially progressive restriction | HP:0002205 Recurrent respiratory infections; HP:0002091 Restrictive ventilatory defect |
| Hydrocephalus/syringomyelia | Variable neurologic complication, potentially severe | **HP:0000238 Hydrocephalus**; HP:0003396 Syringomyelia |
| Hearing loss, hypotonia, delayed motor or expressive-language development | Variable, often mild-to-moderate but can affect education and independence | HP:0000365 Hearing impairment; HP:0001252 Hypotonia |

The broad reported phenotype also includes serpentine fibula, dolichocephaly/bathrocephaly, absent or hypoplastic frontal sinuses, high-arched palate, hypertrichosis, short nails, hypospadias, cryptorchidism, intestinal malrotation, hernia, plantar ulcers, and deep voice. (cortesmartin2020hajdu–cheneysyndromea pages 9-13)

A detailed 2022 pediatric case documented delayed lambdoid closure, short broad phalanges, hypotonia, expressive-language delay, megalocornea/blue sclerae, delayed tooth eruption, bilateral foot valgus and Trendelenburg gait. Focal vibration plus aquatic/hippotherapy was followed by longer steps, faster cadence, and disappearance of the observed Trendelenburg pattern, but this uncontrolled observation cannot establish efficacy. (cortesmartin2022hajducheneysyndromea pages 8-11)

## 4. Genetic and molecular information

### Gene and variant class

* **Gene:** NOTCH2, notch receptor 2; chromosome 1p12 region; Ensembl **ENSG00000134250**; HGNC **HGNC:7882**.
* **Typical variants:** heterozygous nonsense or small deletion/frameshift variants in terminal exon 34, creating a premature stop upstream of the PEST domain.
* **Origin:** germline; either inherited or de novo. HCS is not a somatic neoplasm-associated phenotype.
* **ACMG interpretation:** a terminal-exon truncation requires phenotype, segregation/de novo status, database evidence, and the established gain-of-function mechanism. Ordinary “loss-of-function” rules must be applied carefully because HCS truncations escape conventional nonsense-mediated decay and act through protein stabilization.
* **Population frequency:** pathogenic HCS variants are expected to be absent or extremely rare in gnomAD/1000 Genomes. Variant-specific frequencies should be queried at curation time; no defensible pooled carrier frequency exists.

The mechanistic distinction from **NOTCH2-related Alagille syndrome** is important: HCS terminal-exon variants stabilize NICD2, whereas Alagille syndrome generally reflects NOTCH-pathway haploinsufficiency/reduced signaling. (cortesmartin2020hajdu–cheneysyndromea pages 9-13)

### Functional consequence

Normal ligand engagement triggers proteolysis and release of NICD2, which enters the nucleus and complexes with RBPJ and Mastermind-like proteins. The PEST domain normally permits ubiquitination and degradation. HCS truncation removes that degron while retaining RAM/ankyrin and nuclear-signaling elements, producing prolonged **gain-of-function** signaling. (cortesmartin2020hajdu–cheneysyndromea pages 9-13, canalis2016hajducheneymouse pages 1-2, canalis2016hajducheneymouse pages 18-19)

**Exact primary-study abstract quote:** “Hajdu Cheney Syndrome…is associated with NOTCH2 mutations resulting in a truncated stable protein and gain-of-function.” Canalis et al., published online December 1, 2015/final 2016, DOI: https://doi.org/10.1074/jbc.M115.685453. (canalis2016hajducheneymouse pages 1-2)

No established modifier gene, disease-specific methylation episignature, recurrent chromosomal rearrangement, or pathogenic aneuploidy was identified. CMA/karyotype findings therefore are not defining features.

## 5. Environmental information

No toxin, radiation, pollution, occupation, infectious agent, smoking behavior, alcohol exposure, or diet has been shown to cause HCS. Such factors can modify general bone health, surgical risk, or fracture healing but are secondary rather than etiologic. HCS has no infectious transmission and no zoonotic potential.

Practical lifestyle considerations are individualized safe activity, avoidance of high-impact trauma and falls, maintenance of muscle strength, healthy weight, adequate nutrition, and avoidance of smoking/excess alcohol in adults. A 2022 case report recommended continued physical/intellectual activity and avoidance of overweight, but this is expert supportive advice rather than trial evidence. (cortesmartin2022hajducheneysyndromea pages 12-14)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** germline terminal-exon NOTCH2 truncation.
2. **Protein defect:** loss of the PEST degron impairs NICD2 ubiquitination/degradation.
3. **Signaling:** persistent canonical NOTCH2–RBPJ/MAML transcriptional activity, including HES/HEY programs.
4. **Cellular response:** altered skeletal progenitor/osteoblast-lineage signaling and a pro-osteoclastogenic marrow environment; NOTCH2 can promote NFATC1-dependent osteoclast differentiation. Mouse marrow shows increased **Rankl/Tnfsf11** and **Il6** expression.
5. **Tissue process:** excessive osteoclastogenesis/resorption and high bone turnover, with possible concurrent dysregulation of formation and developmental ossification.
6. **Clinical result:** generalized osteopenia/osteoporosis, fractures, deformity and focal distal phalangeal osteolysis. Skull-base and vertebral changes can secondarily cause neurologic or respiratory injury. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13, ballhause2023fracturehealingin pages 7-8, canalis2016hajducheneymouse pages 1-2)

**Suggested GO annotations:** GO:0007219 Notch signaling pathway; GO:0030316 osteoclast differentiation; GO:0045453 bone resorption; GO:0001649 osteoblast differentiation; GO:0060348 bone development; GO:0042060 wound healing. **Cell Ontology:** CL:0000090 osteoclast; CL:0000062 osteoblast; bone-marrow stromal/mesenchymal progenitor and chondrocyte terms should be added after identifier validation.

The mechanism of sharply localized acro-osteolysis remains less certain than generalized high-turnover osteopenia. Inflammatory/local mechanical mechanisms have been proposed but not demonstrated conclusively. (canalis2014hajducheneysyndromea pages 5-6)

### Molecular profiling and advanced technologies

Disease-specific large-scale transcriptomics, proteomics, metabolomics, lipidomics, single-cell RNA sequencing, spatial transcriptomics, multi-omics integration, or CRISPR-screen datasets were not identified through 2024. Existing expression measurements are mostly targeted qRT-PCR in mice. This is a major research gap—not evidence that these layers are normal.

## 7. Anatomical structures affected

* **Primary organs/tissues:** appendicular and axial skeleton—distal phalanges, hands/feet, long bones, vertebrae, skull, cranial sutures, skull base, jaw and alveolar bone.
* **Secondary systems:** kidneys, heart/great vessels, respiratory thorax/airways, CNS/craniovertebral junction, ear/hearing apparatus, dentition/periodontium, and connective tissues/joints. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13)
* **Cells:** osteoclasts and precursors are the best-supported effector population; osteoblasts, stromal progenitors, chondrocytes and osteocytes participate in development/remodeling.
* **Subcellular compartments:** plasma membrane NOTCH2; cleaved NICD2 in cytoplasm/nucleus; nuclear RBPJ/MAML transcriptional complex; ubiquitin-proteasome degradation machinery.
* **Localization:** usually bilateral/generalized rather than lateralized, although severity can be asymmetric.

Suggested UBERON mappings include skeleton (UBERON:0004288), bone tissue (UBERON:0002481), skull (UBERON:0003129), vertebral column (UBERON:0001130), kidney (UBERON:0002113), heart (UBERON:0000948), and distal phalanx/hand/foot terms after curator validation.

## 8. Temporal development

HCS is congenital/genetic, but clinical recognition ranges from infancy to adulthood. Early findings can include craniofacial differences, wormian bones, delayed suture closure, short stature or hand/foot abnormalities. Acro-osteolysis, osteoporosis, vertebral collapse and coarse facial features often become more apparent with age. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13, cortesmartin2022hajducheneysyndromea pages 8-11)

The course is lifelong, chronic, progressive and highly variable—not relapsing-remitting. There is no spontaneous remission. Critical intervention windows include early recognition of osteoporosis/fractures, serial evaluation of the craniovertebral junction before irreversible neurologic injury, and early dental/rehabilitation support. Formal disease stages and validated progression rates do not exist.

## 9. Inheritance and population

* **Inheritance:** autosomal dominant.
* **Penetrance:** apparently high for some phenotype, but age-dependent and incompletely quantified.
* **Expressivity:** markedly variable, including within families.
* **Anticipation:** not established; HCS is not a repeat-expansion disorder.
* **Mosaicism:** parental/germline mosaicism is biologically possible but no frequency estimate is available.
* **Founder effects/consanguinity:** none established; consanguinity is not etiologically relevant to a dominant disorder.
* **Carrier frequency:** unknown and likely extremely low.
* **Prevalence:** <1/1,000,000; approximately 50 cases in the 2020 systematic review and roughly 100 described in some later summaries. Differences reflect search dates and case definitions, not a documented incidence increase. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, cortesmartin2022hajducheneysyndromea pages 12-14, cortesmartin2022hajducheneysyndromea pages 1-2)
* **Incidence, sex ratio, ethnicity and geography:** no robust estimates or population enrichment. Cases occur worldwide and both sexes are affected.

## 10. Diagnostics

### Clinical-radiologic approach

Suspect HCS when progressive distal phalangeal acro-osteolysis occurs with generalized osteoporosis, short stature, wormian bones, craniofacial dysmorphism, dental loss, vertebral abnormalities, basilar invagination, serpentine fibula or renal cysts. A historical Brennan–Pauli clinical tool incorporates acro-osteolysis, wormian bones, platybasia, premature tooth loss, micrognathia, coarse facies and short stature, but molecular confirmation is preferred. (cortesmartin2020hajdu–cheneysyndromea pages 7-9)

Recommended evaluation:

1. Hand/foot radiographs and skeletal survey where appropriate.
2. Spine radiographs/vertebral-fracture assessment and DXA, corrected for age, sex, height and pediatric body size.
3. CT or MRI of the craniovertebral junction when platybasia, basilar invagination, Chiari-type crowding or neurologic symptoms are suspected.
4. Renal ultrasound, echocardiography, dental/periodontal examination, hearing assessment, respiratory evaluation and developmental assessment according to phenotype.
5. Serum calcium, phosphate, alkaline phosphatase, creatinine/eGFR, 25-hydroxyvitamin D, PTH and selected turnover markers—mainly to assess bone health and exclude acquired mimics; no diagnostic biochemical biomarker exists.

Characteristic imaging includes transverse osteolysis of terminal phalanges, reduced bone density, wormian bones, hypoplastic frontal sinuses, serpentine fibula, biconcave “fish” vertebrae, scoliosis, renal cysts and craniovertebral abnormalities. (cortesmartin2020hajdu–cheneysyndromea pages 9-13)

### Genetic testing

Use **NOTCH2 sequencing with adequate exon-34 coverage** and deletion/duplication analysis. A skeletal-dysplasia/acro-osteolysis panel or WES is appropriate for an uncertain phenotype; targeted exome sequencing diagnosed rare syndromic short-stature disorders including HCS in a 2021 cohort. WGS can detect difficult coding, structural or mosaic variants when panel/WES results are negative. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2022hajducheneysyndromea pages 1-2)

CMA, karyotyping, FISH, mitochondrial sequencing and repeat-expansion assays are not first-line unless another diagnosis is suspected. RNA-seq may help resolve a splice VUS but is not routine. Cascade testing should follow identification of a familial variant.

### Differential diagnosis

Major alternatives include systemic sclerosis/scleroderma, psoriatic arthritis, primary hypertrophic osteoarthropathy, multicentric carpotarsal osteolysis, Winchester syndrome/MMP2-related osteolysis, progeroid disorders, hyperparathyroidism, sarcoidosis, neuropathy, thermal injury/trauma, spinal dysraphism, osteogenesis imperfecta, idiopathic juvenile osteoporosis, pycnodysostosis and Alagille syndrome. Acro-osteolysis itself is a radiographic sign that should trigger etiologic investigation. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, cortesmartin2022hajducheneysyndromea pages 1-2)

## 11. Outcome and prognosis

No reliable 5-year survival, mortality rate, or life-expectancy estimate exists. Many affected individuals survive into adulthood, but morbidity may be considerable: recurrent fractures, impaired healing, pain, progressive short stature, deformity, reduced mobility, dental loss and cardiopulmonary or renal complications. No validated HCS-specific EQ-5D, SF-36 or PROMIS dataset was found.

The most dangerous complications are basilar invagination with brainstem injury, hydrocephalus, syringomyelia, vertebral collapse, restrictive ventilation and—rarely—central respiratory arrest or sudden death. (canalis2014hajducheneysyndromea pages 1-2, cortesmartin2020hajdu–cheneysyndromea pages 9-13)

Likely prognostic factors are fracture burden, bone density/architecture, spinal deformity, craniovertebral-junction severity, respiratory restriction, renal/cardiac involvement and access to multidisciplinary management. No validated molecular prognostic biomarker or genotype-based outcome model exists.

## 12. Treatment

There is no approved, curative, genotype-directed HCS therapy. Management should be coordinated by a metabolic-bone specialist with genetics, orthopedics, neurosurgery, dentistry, nephrology, cardiology, pulmonology, ENT/audiology and rehabilitation as indicated.

### Pharmacotherapy

* **Bisphosphonates**—alendronate, pamidronate and zoledronic acid—are most often reported. Some patients gain BMD or experience fewer fractures; others show limited or nonpersistent benefit, and convincing control of acro-osteolysis has not been demonstrated. A referenced pediatric report described increased BMD and no fractures during two years of cyclic pamidronate, but this remains uncontrolled evidence. (cortesmartin2020hajdu–cheneysyndromea pages 7-9, cortesmartin2022hajducheneysyndromea pages 15-17)
* **Denosumab** suppresses RANKL-dependent osteoclast activity and has been used off label. Risks include hypocalcemia, rebound high turnover/vertebral fractures after discontinuation, delayed oral healing and medication-related osteonecrosis of the jaw. Dental planning is essential. (kaczorukwieremczuk2021oralsurgeryprocedures pages 3-10)
* **Teriparatide** has anecdotal use; disease-specific fracture-efficacy and safety are not established, particularly in growing children.
* **Romosozumab:** a 2023 single-patient exploratory report exists (DOI: https://doi.org/10.1007/s00198-023-06668-z), but one case cannot define benefit/risk or establish standard care.
* Calcium or vitamin D should correct deficiency, not be represented as disease-modifying therapy. No HCS-specific pharmacogenomic guidance exists.

Suggested MAXO concepts: genetic counseling; bone-density surveillance; bisphosphonate therapy; denosumab therapy; calcium/vitamin-D supplementation when deficient; physical therapy; occupational therapy; dental surveillance; orthopedic surgery; spinal fusion/decompression; renal ultrasonography; echocardiography.

### Surgery and supportive care

Treat fractures using careful fixation and prolonged follow-up where healing is uncertain. Severe scoliosis, cervical instability, basilar invagination, hydrocephalus and syringomyelia may require specialized orthopedic/neurosurgical intervention. Dental management includes intensive periodontal prevention, conservative restoration where possible and carefully planned extraction/prosthodontics.

A real-world dental series reported successful osseointegration and five-year follow-up of multiple implants with extended healing and three-month maintenance intervals, illustrating feasibility in selected patients rather than general efficacy. (kaczorukwieremczuk2021oralsurgeryprocedures pages 3-10)

Physical/occupational therapy, muscle strengthening, aquatic therapy, gait aids, fall prevention, pain management, hearing/speech support and educational accommodations address function and quality of life. (cortesmartin2022hajducheneysyndromea pages 12-14, cortesmartin2022hajducheneysyndromea pages 8-11)

### Experimental approaches and trials

No disease-specific interventional HCS trial was identified in the retrieved ClinicalTrials.gov search. The returned **NCT02823925** study concerns MONA spectrum disorder, not HCS, and must not be misclassified. Proposed molecular approaches—NOTCH2-selective antibodies, disruption of the NICD transcriptional complex, or allele-specific RNA/gene editing—remain preclinical concepts. Broad systemic Notch inhibition could produce substantial on-target toxicity because Notch regulates many tissues. (canalis2014hajducheneysyndromea pages 5-6)

## 13. Prevention

**Primary prevention:** no lifestyle or vaccine prevents a de novo/inherited NOTCH2 variant. Reproductive genetic counseling, prenatal diagnosis and preimplantation genetic testing are options once a familial pathogenic variant is known.

**Secondary prevention:** cascade testing of relatives, early skeletal/radiologic assessment, DXA and vertebral screening, craniovertebral-junction surveillance, renal ultrasound, echocardiography and dental evaluation can detect complications before irreversible injury.

**Tertiary prevention:** optimize bone nutrition, use safe individualized weight-bearing activity, prevent falls/trauma, avoid smoking and excess alcohol, minimize immobilization, maintain dental hygiene before antiresorptives, monitor spinal/respiratory function, and intervene promptly for neurologic warning signs. Routine vaccination follows standard recommendations; no HCS-specific immunization exists.

## 14. Other species and natural disease

No convincing naturally occurring HCS counterpart was identified in companion animals, livestock or wildlife. No breed association or VBO term is established. The disease is noninfectious and nonzoonotic.

NOTCH2 is evolutionarily conserved across vertebrates, enabling engineered **Mus musculus** models (NCBI Taxonomy **10090**). Ortholog identifiers should be obtained directly from NCBI Gene/Alliance at ingestion because database records can change.

## 15. Model organisms

The principal model is a heterozygous knock-in mouse carrying a human HCS-like terminal Notch2 truncation. In the Canalis model, a **6955C>T, p.Gln2319Ter (Q2319X)** allele produced smaller mice, shorter femora, early cancellous and cortical osteopenia, increased osteoclast numbers/resorption, and increased RANKL-driven osteoclast differentiation. A γ-secretase inhibitor suppressed the enhanced in-vitro osteoclast phenotype, demonstrating Notch dependence. (canalis2016hajducheneymouse pages 1-2, canalis2016hajducheneymouse pages 18-19)

**Exact abstract quote:** “Notch2Q2319X mice exhibit cancellous and cortical bone osteopenia, enhanced osteoclastogenesis and increased bone resorption.” (canalis2016hajducheneymouse pages 1-2)

A 2023 study used 88 operated male Notch2+/HCS mice carrying **6272delT**, created standardized femoral osteotomies, and examined healing on days 3, 7, 14, 21 and 28. Static radiology/histology showed only minor morphologic changes, but HCS callus had increased osteoclast parameters and osteoblast/osteoclast marker expression, and healed femora had inferior biomechanical stability. (ballhause2023fracturehealingin pages 1-2, ballhause2023fracturehealingin pages 10-11)

**Exact 2023 abstract quote:** “structural indices of bone regeneration are normal in HCS mice, which, however, exhibit signs of increased callus turnover and display impaired biomechanical stability of healed fractures.” Ballhause et al., *Scientific Reports*, July 2023, DOI: https://doi.org/10.1038/s41598-023-38638-0. (ballhause2023fracturehealingin pages 1-2)

These models are valuable for osteoclast biology, high-turnover osteopenia, fracture healing and preclinical antiresorptive/Notch-directed studies. Limitations include incomplete reproduction of human acro-osteolysis and multisystem disease, species-specific skeletal remodeling, engineered alleles, and controlled laboratory environments. The 2023 study used only male 12–14-week-old mice, limiting sex- and age-generalization. (ballhause2023fracturehealingin pages 10-11)

## Recent developments, evidence appraisal and priorities

The most consequential 2023–2024 development was the 2023 demonstration that apparently normal structural fracture repair in HCS mice can conceal increased turnover and reduced mechanical competence. This argues that radiographic union alone may be an inadequate endpoint and supports biomechanical/functional follow-up in future human natural-history studies. (ballhause2023fracturehealingin pages 1-2, ballhause2023fracturehealingin pages 7-8)

Recent human literature remains predominantly case reports: exploratory romosozumab treatment in 2023, new NOTCH2 variants and phenotype expansions in 2023–2024, dental/orofacial reports, and perioperative descriptions. These improve recognition but do not establish frequencies or treatment efficacy. The expert consensus across authoritative reviews remains that HCS has no curative therapy and that antiresorptive/anabolic benefits are unproven at syndrome level. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, canalis2014hajducheneysyndromea pages 1-2)

Priority research needs are: an international prospective registry; standardized HPO-based phenotyping; longitudinal DXA, HR-pQCT, fracture and craniovertebral outcomes; patient-reported quality-of-life measures; systematic ClinVar/gnomAD variant curation; patient-derived iPSC osteoclast/osteoblast studies; single-cell and spatial profiling of bone; and multicenter treatment protocols with prespecified fracture, function and safety endpoints.

## Selected primary and authoritative references

1. Simpson MA et al. **Mutations in NOTCH2 cause Hajdu-Cheney syndrome, a disorder of severe and progressive bone loss.** *Nature Genetics*. Published April 2011. PMID: **21378985**. DOI: https://doi.org/10.1038/ng.779. (OpenTargets Search: Hajdu-Cheney syndrome-NOTCH2)
2. Canalis E, Zanotti S. **Hajdu-Cheney syndrome: a review.** *Orphanet Journal of Rare Diseases*. Published December 2014. DOI: https://doi.org/10.1186/s13023-014-0200-y. (canalis2014hajducheneysyndromea pages 1-2)
3. Canalis E et al. **Hajdu Cheney Mouse Mutants Exhibit Osteopenia, Increased Osteoclastogenesis, and Bone Resorption.** *Journal of Biological Chemistry*. Published 2016. DOI: https://doi.org/10.1074/jbc.M115.685453. (canalis2016hajducheneymouse pages 1-2)
4. Cortés-Martín J et al. **Hajdu–Cheney Syndrome: A Systematic Review of the Literature.** *International Journal of Environmental Research and Public Health*. Published August 2020. DOI: https://doi.org/10.3390/ijerph17176174. (cortesmartin2020hajdu–cheneysyndromea pages 6-7, cortesmartin2020hajdu–cheneysyndromea pages 3-6)
5. Cortés-Martín J et al. **Hajdu-Cheney Syndrome: A Novel NOTCH2 Mutation in a Spanish Child in Treatment with Vibrotherapy.** *Journal of Clinical Medicine*. Published September 2022. DOI: https://doi.org/10.3390/jcm11175205. (cortesmartin2022hajducheneysyndromea pages 12-14, cortesmartin2022hajducheneysyndromea pages 8-11)
6. Ballhause TM et al. **Fracture healing in a mouse model of Hajdu–Cheney-Syndrome with high turnover osteopenia results in decreased biomechanical stability.** *Scientific Reports*. Published July 2023. DOI: https://doi.org/10.1038/s41598-023-38638-0. (ballhause2023fracturehealingin pages 1-2)

**Overall evidence judgment:** causal gene and gain-of-function mechanism are strong; cardinal phenotype evidence is moderate-to-strong but frequency estimates are weak; treatment evidence is very low because it consists mainly of uncontrolled individual cases; epidemiology, survival, quality of life, modifiers and advanced omics remain major evidence gaps.

References

1. (cortesmartin2020hajdu–cheneysyndromea pages 7-9): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Raquel Rodríguez-Blanque, Antonio Bermejo-Fernández, and Juan Carlos Sánchez-García. Hajdu–cheney syndrome: a systematic review of the literature. International Journal of Environmental Research and Public Health, 17:6174, Aug 2020. URL: https://doi.org/10.3390/ijerph17176174, doi:10.3390/ijerph17176174. This article has 33 citations.

2. (canalis2014hajducheneysyndromea pages 1-2): Ernesto Canalis and Stefano Zanotti. Hajdu-cheney syndrome: a review. Orphanet Journal of Rare Diseases, Dec 2014. URL: https://doi.org/10.1186/s13023-014-0200-y, doi:10.1186/s13023-014-0200-y. This article has 109 citations and is from a peer-reviewed journal.

3. (cortesmartin2022hajducheneysyndromea pages 1-2): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Juan Carlos Sánchez-García, Antonio Liñán González, and Raquel Rodríguez-Blanque. Hajdu-cheney syndrome: a novel notch2 mutation in a spanish child in treatment with vibrotherapy: a case report. Sep 2022. URL: https://doi.org/10.3390/jcm11175205, doi:10.3390/jcm11175205. This article has 4 citations.

4. (canalis2014hajducheneysyndromea pages 5-6): Ernesto Canalis and Stefano Zanotti. Hajdu-cheney syndrome: a review. Orphanet Journal of Rare Diseases, Dec 2014. URL: https://doi.org/10.1186/s13023-014-0200-y, doi:10.1186/s13023-014-0200-y. This article has 109 citations and is from a peer-reviewed journal.

5. (cortesmartin2020hajdu–cheneysyndromea pages 9-13): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Raquel Rodríguez-Blanque, Antonio Bermejo-Fernández, and Juan Carlos Sánchez-García. Hajdu–cheney syndrome: a systematic review of the literature. International Journal of Environmental Research and Public Health, 17:6174, Aug 2020. URL: https://doi.org/10.3390/ijerph17176174, doi:10.3390/ijerph17176174. This article has 33 citations.

6. (canalis2016hajducheneymouse pages 1-2): Ernesto Canalis, Lauren Schilling, Siu-Pok Yee, Sun-Kyeong Lee, and Stefano Zanotti. Hajdu cheney mouse mutants exhibit osteopenia, increased osteoclastogenesis, and bone resorption. Journal of Biological Chemistry, 291:1538-1551, Jan 2016. URL: https://doi.org/10.1074/jbc.m115.685453, doi:10.1074/jbc.m115.685453. This article has 96 citations and is from a domain leading peer-reviewed journal.

7. (cortesmartin2020hajdu–cheneysyndromea pages 3-6): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Raquel Rodríguez-Blanque, Antonio Bermejo-Fernández, and Juan Carlos Sánchez-García. Hajdu–cheney syndrome: a systematic review of the literature. International Journal of Environmental Research and Public Health, 17:6174, Aug 2020. URL: https://doi.org/10.3390/ijerph17176174, doi:10.3390/ijerph17176174. This article has 33 citations.

8. (OpenTargets Search: Hajdu-Cheney syndrome-NOTCH2): Open Targets Query (Hajdu-Cheney syndrome-NOTCH2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (canalis2016hajducheneymouse pages 18-19): Ernesto Canalis, Lauren Schilling, Siu-Pok Yee, Sun-Kyeong Lee, and Stefano Zanotti. Hajdu cheney mouse mutants exhibit osteopenia, increased osteoclastogenesis, and bone resorption. Journal of Biological Chemistry, 291:1538-1551, Jan 2016. URL: https://doi.org/10.1074/jbc.m115.685453, doi:10.1074/jbc.m115.685453. This article has 96 citations and is from a domain leading peer-reviewed journal.

10. (ballhause2023fracturehealingin pages 7-8): Tobias Malte Ballhause, Shan Jiang, Weixin Xie, Jan Sevecke, Christine Dowling, Tobias Dust, Sabine Brandt, Peter R. Mertens, Timur Alexander Yorgan, Thorsten Schinke, Karl-Heinz Frosch, Anke Baranowsky, and Johannes Keller. Fracture healing in a mouse model of hajdu–cheney-syndrome with high turnover osteopenia results in decreased biomechanical stability. Scientific Reports, Jul 2023. URL: https://doi.org/10.1038/s41598-023-38638-0, doi:10.1038/s41598-023-38638-0. This article has 4 citations and is from a peer-reviewed journal.

11. (cortesmartin2020hajdu–cheneysyndromea pages 6-7): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Raquel Rodríguez-Blanque, Antonio Bermejo-Fernández, and Juan Carlos Sánchez-García. Hajdu–cheney syndrome: a systematic review of the literature. International Journal of Environmental Research and Public Health, 17:6174, Aug 2020. URL: https://doi.org/10.3390/ijerph17176174, doi:10.3390/ijerph17176174. This article has 33 citations.

12. (cortesmartin2022hajducheneysyndromea pages 8-11): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Juan Carlos Sánchez-García, Antonio Liñán González, and Raquel Rodríguez-Blanque. Hajdu-cheney syndrome: a novel notch2 mutation in a spanish child in treatment with vibrotherapy: a case report. Sep 2022. URL: https://doi.org/10.3390/jcm11175205, doi:10.3390/jcm11175205. This article has 4 citations.

13. (cortesmartin2022hajducheneysyndromea pages 12-14): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Juan Carlos Sánchez-García, Antonio Liñán González, and Raquel Rodríguez-Blanque. Hajdu-cheney syndrome: a novel notch2 mutation in a spanish child in treatment with vibrotherapy: a case report. Sep 2022. URL: https://doi.org/10.3390/jcm11175205, doi:10.3390/jcm11175205. This article has 4 citations.

14. (kaczorukwieremczuk2021oralsurgeryprocedures pages 3-10): Magdalena Kaczoruk-Wieremczuk, Paulina Adamska, Łukasz Jan Adamski, Piotr Wychowański, Barbara Alicja Jereczek-Fossa, and Anna Starzyńska. Oral surgery procedures in a patient with hajdu-cheney syndrome treated with denosumab—a rare case report. International Journal of Environmental Research and Public Health, 18:9099, Aug 2021. URL: https://doi.org/10.3390/ijerph18179099, doi:10.3390/ijerph18179099. This article has 9 citations.

15. (ballhause2023fracturehealingin pages 1-2): Tobias Malte Ballhause, Shan Jiang, Weixin Xie, Jan Sevecke, Christine Dowling, Tobias Dust, Sabine Brandt, Peter R. Mertens, Timur Alexander Yorgan, Thorsten Schinke, Karl-Heinz Frosch, Anke Baranowsky, and Johannes Keller. Fracture healing in a mouse model of hajdu–cheney-syndrome with high turnover osteopenia results in decreased biomechanical stability. Scientific Reports, Jul 2023. URL: https://doi.org/10.1038/s41598-023-38638-0, doi:10.1038/s41598-023-38638-0. This article has 4 citations and is from a peer-reviewed journal.

16. (ballhause2023fracturehealingin pages 10-11): Tobias Malte Ballhause, Shan Jiang, Weixin Xie, Jan Sevecke, Christine Dowling, Tobias Dust, Sabine Brandt, Peter R. Mertens, Timur Alexander Yorgan, Thorsten Schinke, Karl-Heinz Frosch, Anke Baranowsky, and Johannes Keller. Fracture healing in a mouse model of hajdu–cheney-syndrome with high turnover osteopenia results in decreased biomechanical stability. Scientific Reports, Jul 2023. URL: https://doi.org/10.1038/s41598-023-38638-0, doi:10.1038/s41598-023-38638-0. This article has 4 citations and is from a peer-reviewed journal.

17. (cortesmartin2022hajducheneysyndromea pages 15-17): Jonathan Cortés-Martín, Lourdes Díaz-Rodríguez, Beatriz Piqueras-Sola, Juan Carlos Sánchez-García, Antonio Liñán González, and Raquel Rodríguez-Blanque. Hajdu-cheney syndrome: a novel notch2 mutation in a spanish child in treatment with vibrotherapy: a case report. Sep 2022. URL: https://doi.org/10.3390/jcm11175205, doi:10.3390/jcm11175205. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](Hajdu-Cheney_Syndrome-deep-research-falcon_artifacts/artifact-00.md)