---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T07:31:47.382207'
end_time: '2026-05-08T07:51:27.206605'
duration_seconds: 1179.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum** covering all of the
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
- **Disease Name:** ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALDH18A1-Related Spastic Paraplegia and Neurocutaneous Spectrum** covering all of the
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


## Comprehensive research report: ALDH18A1‑Related Spastic Paraplegia and Neurocutaneous Spectrum (P5CS deficiency continuum)

### Executive summary
ALDH18A1 encodes the mitochondrial bifunctional enzyme Δ1‑pyrroline‑5‑carboxylate synthase (P5CS), which catalyzes conversion of glutamate to pyrroline‑5‑carboxylate (P5C), a branch point for **proline** and **ornithine/arginine‑urea‑cycle–linked** metabolism. Pathogenic ALDH18A1 variants produce a **continuous clinicogenetic spectrum** spanning neurocutaneous cutis laxa / de Barsy–like presentations and hereditary spastic paraplegia (HSP) type 9 (SPG9), with dominant forms frequently proposed to act by **dominant‑negative loss‑of‑function** and recessive forms by partial/marked deficiency. A widely cited synthesis proposes severity ordering **SPG9A < SPG9B < ADCL3 ≤ ARCL3A** as a single disease entity (“P5CS deficiency”). (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

Recent (2023) multi‑omics work in patient fibroblasts with a homozygous ALDH18A1 variant demonstrates broad alterations in **amino‑acid and antioxidant metabolism**, including reduced glutamate‑derived metabolites (proline, glutathione) and decreased ornithine‑derived putrescine, providing a modern mechanistic and biomarker framework for this Mendelian spectrum. (colonna2023functionalassessmentof pages 1-1)

### 1. Disease information (definitions, identifiers, synonyms)

#### 1.1 Disease concept
**ALDH18A1‑related spastic paraplegia and neurocutaneous spectrum** refers to Mendelian disorders caused by mono‑ or biallelic pathogenic variants in **ALDH18A1**, producing a phenotype continuum that includes:
- **Hereditary spastic paraplegia type 9**: SPG9A (AD) and SPG9B (AR).
- **Cutis laxa 3**: autosomal dominant cutis laxa 3 (ADCL3) and autosomal recessive cutis laxa type IIIA (ARCL3A).
- **ALDH18A1‑related de Barsy syndrome** as a neurocutaneous entity overlapping the cutis laxa/progeroid spectrum.

A central definition from a 2020 expert review states that ALDH18A1 mutations cause “two neurocutaneous syndromes … and two SPG9 syndromes” and that they “represent a continuum of increasing severity … of the same disease, P5CS deficiency.” (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

#### 1.2 Key identifiers
- **Gene**: ALDH18A1 at **10q24.1** (OMIM gene entry cited as **OMIM 138250** in a SPG9B case report). (kalmar2021tremorasan pages 1-2)
- **SPG9A**: **OMIM/MIM 601162**. (kalmar2021tremorasan pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- **SPG9B**: **OMIM/MIM 616586**. (kalmar2021tremorasan pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2)
- **ADCL3**: **OMIM/MIM 616603**. (kalmar2021tremorasan pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- **ARCL3A**: **OMIM/MIM 219150**. (kalmar2021tremorasan pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- **De Barsy syndrome (DBS)**: discussed within ARCL3 / ARCL3A spectrum; DBS listed with **MIM 219150** within a cutis laxa diagnostic/nosology paper. (gardeitchik2014clinicalandbiochemical pages 1-2)

**MONDO (via Open Targets association evidence)**:
- MONDO:0009053 “ALDH18A1‑related de Barsy syndrome”
- MONDO:0014702 “autosomal recessive complex spastic paraplegia type 9B”
- MONDO:0014706 “cutis laxa, autosomal dominant 3”
- MONDO:0015091 “autosomal dominant spastic paraplegia type 9” (OpenTargets Search: -ALDH18A1)

#### 1.3 Synonyms and alternative names
- P5CS deficiency / Δ1‑pyrroline‑5‑carboxylate synthetase deficiency (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- ALDH18A1‑related cutis laxa (dominant or recessive) (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- ALDH18A1‑associated HSP / spastic paraplegia 9 (chen2021novelcompoundmissense pages 1-2)
- De Barsy‑like progeroid cutis laxa phenotype (fischerzirnsak2015recurrentdenovo pages 1-2)

#### 1.4 Evidence source types
Most information in the available corpus is derived from **aggregated disease‑level resources and literature synthesis** (e.g., JIMD review) (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) and **primary case series** (e.g., Am J Hum Genet Arg138 de novo cohort) (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media 44a36465), complemented by **functional studies** in patient cells (colonna2023functionalassessmentof pages 1-1) and **clinical cohort sequencing studies** (mahungu2023themutationalprofile pages 1-2).

### 2. Etiology

#### 2.1 Disease causal factors
Primary cause is **genetic**: pathogenic variants in **ALDH18A1**. The encoded enzyme P5CS catalyzes the first and common step of **proline and ornithine biosynthesis from glutamate**, linking glutamate metabolism to urea cycle and broader amino‑acid/polyamine metabolism. (coutelier2015alterationofornithine pages 1-2, colonna2023functionalassessmentof pages 1-2)

#### 2.2 Risk factors
- **Genetic**: Monoallelic variants (dominant) or biallelic variants (recessive) in ALDH18A1. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2)
- Environmental/lifestyle risk factors are not established in the retrieved disease‑specific literature.

#### 2.3 Protective factors / gene–environment interactions
The initial ARCL3A description included “paradoxical hyperammonemia (alleviated by protein),” indicating **dietary protein intake** can acutely modify a biochemical phenotype in severe P5CS deficiency. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

### 3. Phenotypes (clinical spectrum)

#### 3.1 Overarching phenotype architecture
A key modern framing is that ALDH18A1 disorders encompass at least two named syndromic groupings—**SPG9A/B** and **cutis laxa 3 (ADCL3/ARCL3A)**—with overlapping neurological and cutaneous findings. (colonna2023functionalassessmentof pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

| Entity/synonym | Inheritance | Typical onset | Core neuro features | Core cutaneous/connective-tissue features | Key biochemical clues | Notes/quantitative stats | Key references |
|---|---|---|---|---|---|---|---|
| SPG9A / autosomal dominant spastic paraplegia type 9 / dominant ALDH18A1-related HSP | Autosomal dominant; monoallelic ALDH18A1 variants, with dominant-negative loss-of-function proposed (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, panza2016aldh18a1genemutations pages 8-8) | Generally later-onset than recessive/neurocutaneous forms; upper motor neuron syndrome with progressive course (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) | Progressive spastic paraparesis/paraplegia; can be pure or complex HSP; corticospinal tract involvement; tremor can occur in ALDH18A1-related HSP spectrum (coutelier2015alterationofornithine pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, kalmar2021tremorasan pages 1-2) | Typically lacks overt cutis laxa/joint hypermobility seen in neurocutaneous forms (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) | Plasma ornithine, citrulline, arginine, and proline may be low or low-normal; amino-acid chromatography suggested as a trait biomarker in ALDH18A1 HSP (coutelier2015alterationofornithine pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) | Review cited 50 total SPG9 patients, of whom 36 were monoallelic; SPG9A framed as the mildest end of the ALDH18A1/P5CS deficiency continuum (SPG9A < SPG9B < ADCL3 ≤ ARCL3A) (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) | Coutelier et al., 2015, Brain, https://doi.org/10.1093/brain/awv143; Panza et al., 2016, Brain, https://doi.org/10.1093/brain/awv247; Marco-Marín et al., 2020, JIMD, https://doi.org/10.1002/jimd.12220 |
| SPG9B / autosomal recessive complex spastic paraplegia type 9B / recessive ALDH18A1-related HSP | Autosomal recessive; biallelic ALDH18A1 variants (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2, kalmar2021tremorasan pages 1-2) | Usually childhood onset; clinically more severe than SPG9A, but milder than cutis laxa neurocutaneous forms overall (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2, kalmar2021tremorasan pages 1-2) | Complex HSP with spasticity, developmental delay/intellectual impairment in some cases, tremor as early sign in at least one child, white-matter reduction/corpus callosum hypoplasia reported, variable cognitive involvement (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2, kalmar2021tremorasan pages 1-2) | Usually no frank cutis laxa; may have growth issues/dysmorphic traits in more severe cases (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, kalmar2021tremorasan pages 1-2) | P5CS concentration can be significantly decreased in plasma; amino-acid abnormalities may include low or low-normal ornithine/citrulline/arginine/proline, but can also be normal except mild hypocitrullinemia; RNA splicing analysis can clarify intronic variants (coutelier2015alterationofornithine pages 1-2, chen2021novelcompoundmissense pages 1-2, kalmar2021tremorasan pages 1-2) | Review cited 50 total SPG9 patients, 14 biallelic; Chen 2021 reported novel c.880T>C (p.S294P) plus c.-28-13A>G in one AR family; Kalmár 2021 detailed early tremor (~2 months), DQ 45 at 2 years, MRI abnormalities, normal fasting ammonia, normal proline/ornithine/arginine, slightly decreased citrulline (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2, kalmar2021tremorasan pages 1-2) | Magini et al., 2019, Ann Clin Transl Neurol, https://doi.org/10.1002/acn3.50821; Chen et al., 2021, Front Neurol, https://doi.org/10.3389/fneur.2021.627531; Kalmár et al., 2021, Brain Dev, https://doi.org/10.1016/j.braindev.2020.07.015 |
| ADCL3 / cutis laxa, autosomal dominant 3 / progeroid autosomal-dominant cutis laxa due to ALDH18A1 | Autosomal dominant, typically de novo heterozygous ALDH18A1 variants; recurrent Arg138 substitutions highlighted (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, fischerzirnsak2015recurrentdenovo pages 1-2) | Congenital/prenatal to early infancy; growth restriction often prenatal and postnatal (fischerzirnsak2015recurrentdenovo pages 1-2) | Developmental/psychomotor delay common; neurodevelopmental impairment; vascular tortuosity reported in some; overlaps with De Barsy-like neurocutaneous phenotype (fischerzirnsak2015recurrentdenovo pages 1-2) | Lax thin skin, progeroid appearance, joint hyperlaxity; cataracts frequent; adducted thumbs in many patients (fischerzirnsak2015recurrentdenovo pages 1-2) | Reduced P5CS enzymatic activity; delayed proline accumulation; altered sub-mitochondrial distribution of mutant P5CS (fischerzirnsak2015recurrentdenovo pages 1-2) | In a cohort of 8 unrelated individuals, all had lax thin skin and joint hyperlaxity; all had prenatal growth restriction and 7/8 postnatal growth restriction; 6/8 had cataracts; 5/8 adducted thumbs; 4/8 cranial vessel tortuosity; de novo origin confirmed in all 6 probands with parental DNA available (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media 44a36465) | Fischer-Zirnsak et al., 2015, Am J Hum Genet, https://doi.org/10.1016/j.ajhg.2015.08.001; Marco-Marín et al., 2020, JIMD, https://doi.org/10.1002/jimd.12220 |
| ARCL3A / cutis laxa, autosomal recessive type IIIA / recessive neurocutaneous P5CS deficiency | Autosomal recessive; homozygous or compound heterozygous ALDH18A1 variants (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, lugli2022autosomalrecessivecutis pages 6-6, gardeitchik2014clinicalandbiochemical pages 1-2) | Usually congenital/infantile; often severe, including fetal presentations in some reports (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, lugli2022autosomalrecessivecutis pages 6-6) | Developmental disability/intellectual disability, severe neurologic involvement in many cases, growth restriction, cataracts; corpus callosum agenesis/dysgenesis and dystonic posturing associated in broader cutis laxa diagnostic series (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, lugli2022autosomalrecessivecutis pages 6-6, gardeitchik2014clinicalandbiochemical pages 1-2) | Cutis laxa, connective-tissue laxity, joint laxity, hernias; systemic involvement typical (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, lugli2022autosomalrecessivecutis pages 6-6) | Plasma proline, arginine, citrulline, and ornithine can be decreased or low-normal; hyperammonemia reported in classic P5CS deficiency; considered a multifaceted urea-cycle-related disorder (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, lugli2022autosomalrecessivecutis pages 6-6) | Review cited 32 neurocutaneous patients: 21 familial with homozygous/compound heterozygous variants and 11 sporadic with de novo heterozygous variants across the broader neurocutaneous spectrum; ARCL3A considered among the most severe manifestations (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) | Gardeitchik et al., 2014, Eur J Hum Genet, https://doi.org/10.1038/ejhg.2013.154; Angelini et al., 2020, Neuropediatrics, https://doi.org/10.1055/s-0040-1701671; Lugli et al., 2022, Eur J Med Genet, https://doi.org/10.1016/j.ejmg.2022.104568 |
| ALDH18A1-related de Barsy syndrome / De Barsy-like neurocutaneous syndrome / P5CS deficiency spectrum | Usually autosomal recessive in classic de Barsy-like presentations, but ALDH18A1-related disease spans recessive neurocutaneous forms and de novo dominant cutis laxa phenotypes (lugli2022autosomalrecessivecutis pages 6-6, fischerzirnsak2015recurrentdenovo pages 1-2, OpenTargets Search: -ALDH18A1) | Congenital to infantile in classic neurocutaneous presentations (lugli2022autosomalrecessivecutis pages 6-6, fischerzirnsak2015recurrentdenovo pages 1-2) | Neurodevelopmental delay, cataracts, neurodegeneration/neurologic deficits; overlap with spastic paraplegia and broader ALDH18A1 neurocutaneous disease (OpenTargets Search: -ALDH18A1, lugli2022autosomalrecessivecutis pages 6-6, fischerzirnsak2015recurrentdenovo pages 1-2) | Cutis laxa/progeroid appearance, joint laxity, connective-tissue manifestations; fat pads/retinopathy and cardiovascular involvement reported in broader ALDH18A1 literature (lugli2022autosomalrecessivecutis pages 6-6, panza2016aldh18a1genemutations pages 8-8) | Hyperammonemia with reduced ornithine, citrulline, arginine, and proline described in classic P5CS deficiency; recent work also shows altered amino-acid and antioxidant metabolism, including reduced glutamate, proline, glutathione, and putrescine (fischerzirnsak2026neurocutaneousdisordersduea pages 20-22, colonna2023functionalassessmentof pages 1-1) | Open Targets links ALDH18A1 to MONDO:0009053 “ALDH18A1-related de Barsy syndrome”; named disease concept overlaps substantially with ARCL3A/ADCL3 and is best understood as part of a continuous ALDH18A1/P5CS deficiency spectrum rather than a sharply separate entity (OpenTargets Search: -ALDH18A1, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5) | Colonna et al., 2023, Hum Mol Genet, https://doi.org/10.1093/hmg/ddac226; Fischer-Zirnsak et al., 2015, Am J Hum Genet, https://doi.org/10.1016/j.ajhg.2015.08.001; Open Targets disease association (OpenTargets Search: -ALDH18A1) |


*Table: This table summarizes the named ALDH18A1/P5CS deficiency entities across the spastic paraplegia and neurocutaneous spectrum, including inheritance, onset, core features, biochemical clues, and available quantitative cohort data. It is useful for comparing how SPG9 and cutis laxa/de Barsy-like presentations fit into a single mechanistic disease continuum.*

#### 3.2 Neurocutaneous / cutis laxa / de Barsy‑like phenotypes (ADCL3; ARCL3A; ALDH18A1‑related de Barsy)
**Core clinical features** in an autosomal‑dominant progeroid cutis laxa cohort (8 unrelated individuals) include:
- Lax thin skin with visible veins and **joint hyperlaxity** in all individuals
- **Prenatal growth restriction** in all; **postnatal growth restriction** in 7/8
- **Cataracts** in 6/8
- **Adducted thumbs** in 5/8
- **Cranial vessel tortuosity** in 4/8
- Psychomotor development delayed in all probands
These individuals carried heterozygous de novo ALDH18A1 variants affecting **Arg138** of P5CS. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media 44a36465)

The same paper provides a concise abstract statement (useful for knowledge‑base evidence quoting): it reports “eight unrelated individuals … clinically diagnosed with DBS or wrinkly skin syndrome” with “three heterozygous mutations in ALDH18A1 … Arg138,” and notes reduced enzymatic activity and delayed proline accumulation, concluding that these recurrent de novo variants “cause an autosomal‑dominant form of cutis laxa with progeroid features” and “will have immediate impact on diagnostics and genetic counseling.” (fischerzirnsak2015recurrentdenovo pages 1-2)

**Suggested HPO terms (examples)**:
- Cutis laxa (HP:0000973)
- Joint hypermobility (HP:0001382)
- Cataract (HP:0000518)
- Prenatal growth restriction / IUGR (HP:0001511)
- Postnatal growth retardation (HP:0008897)
- Developmental delay (HP:0001263)
- Arterial/cerebral vessel tortuosity (HP:0005116)

#### 3.3 Spastic paraplegia phenotypes (SPG9A/B)
**SPG9 clinical definition and spectrum**: HSP due to ALDH18A1 can be pure (lower‑limb spasticity with mild urinary symptoms and distal vibration impairment) or complicated (cognitive impairment, seizures, neuropathy, amyotrophy, short stature, vision abnormalities, etc.). (chen2021novelcompoundmissense pages 1-2)

**Primary HSP series evidence**: In 2015, ALDH18A1 variants were found to cause both recessive and dominant HSP; low plasma ornithine/citrulline/arginine/proline suggested P5CS deficiency, and fibroblast glutamine‑loading tests confirmed a metabolic block at P5CS. The authors propose amino‑acid chromatography in the clinico‑genetic work‑up. (coutelier2015alterationofornithine pages 1-2)

**Example SPG9B natural history (case report)**: a child with compound heterozygous ALDH18A1 variants had tremor onset at ~2 months, developmental delay (unable to sit at 10 months, stand at 12 months), DQ 45 at age 2 years, MRI showing reduced white matter and corpus callosum hypoplasia, and slightly decreased citrulline with otherwise normal proline/ornithine/arginine and normal fasting ammonia. (kalmar2021tremorasan pages 1-2)

**Suggested HPO terms (examples)**:
- Spastic paraplegia (HP:0001258)
- Hyperreflexia (HP:0001347)
- Urinary urgency (HP:0000012)
- Tremor (HP:0001337)
- Corpus callosum hypoplasia/dysgenesis (HP:0002079)
- White matter abnormality / hypomyelination (HP:0002500)
- Intellectual disability / developmental delay (HP:0001249, HP:0001263)

#### 3.4 Quality of life impact
Disease‑specific QoL instruments were not present in the retrieved ALDH18A1‑specific sources. For HSP broadly, the disease “significantly impairs … quality of life” and worsens with severity/age. (awuah2024hereditaryspasticparaplegia pages 1-2)

### 4. Genetic/molecular information

#### 4.1 Causal gene
- **ALDH18A1** encodes P5CS (Δ1‑pyrroline‑5‑carboxylate synthetase), a bifunctional mitochondrial enzyme. (colonna2023functionalassessmentof pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

#### 4.2 Pathogenic variants and variant classes (examples)
- **Autosomal dominant progeroid cutis laxa (ADCL3)**: recurrent heterozygous de novo missense variants affecting **Arg138** (amino‑acid substitutions of the same conserved residue). (fischerzirnsak2015recurrentdenovo pages 1-2)
- **Autosomal recessive SPG9B**: compound missense plus intronic splicing variants (e.g., c.880T>C p.S294P and c.-28-13A>G) with reduced P5CS concentration in plasma by ELISA. (chen2021novelcompoundmissense pages 1-2)
- **Biallelic ARCL3A / neurocutaneous**: early reports include biallelic variants and biochemical evidence of impaired ornithine/proline synthesis and paradoxical hyperammonemia. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

#### 4.3 Functional consequences and inheritance mechanisms
A 2020 review concludes that dominant mutations “cause loss‑of‑function by dominant‑negative mechanisms,” and that decreased P5CS function underlies all four named syndromes. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

A primary study of Arg138 de novo variants shows the mutant protein can interact with wild‑type P5CS but has altered sub‑mitochondrial distribution and reduced enzymatic activity, consistent with a dominant negative/complex destabilization model. (fischerzirnsak2015recurrentdenovo pages 1-2)

#### 4.4 Population frequencies, modifier genes, epigenetics
No gnomAD‑style allele frequencies, established modifier genes, or disease‑specific epigenetic mechanisms were available in the retrieved sources.

### 5. Environmental information
No specific environmental toxins/lifestyle exposures were implicated in the retrieved ALDH18A1‑specific literature. Diet can modulate biochemical expression in severe cases (protein alleviating paradoxical hyperammonemia). (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

### 6. Mechanism / pathophysiology

#### 6.1 Core metabolic pathway and causal chain
ALDH18A1/P5CS converts **glutamate → P5C**, which then supports:
- Proline synthesis via PYCR1
- Ornithine synthesis via OAT, connecting to urea‑cycle amino acids (citrulline, arginine)
This connects P5CS to the urea cycle and TCA cycle and to synthesis of polyamines and glutathione (redox). (colonna2023functionalassessmentof pages 1-2)

**Causal chain (simplified)**:
1) Pathogenic ALDH18A1 variant → reduced P5CS function/complex formation (fischerzirnsak2015recurrentdenovo pages 1-2, colonna2023functionalassessmentof pages 1-1)
2) Reduced de novo proline/ornithine production → low/low‑normal plasma proline/ornithine/citrulline/arginine (trait biomarker) and, in severe cases, paradoxical hyperammonemia (coutelier2015alterationofornithine pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 5-9)
3) Downstream consequences:
   - Connective tissue/skin: impaired proline availability plausibly limits collagen/elastin production → cutis laxa/progeroid appearance (colonna2023functionalassessmentof pages 1-2)
   - Neurodevelopment/neurodegeneration: not fully understood mechanistically, but may relate to metabolic/redox stress and selective neuronal vulnerability (colonna2023functionalassessmentof pages 1-2)
   - Antioxidant pathway: reduced glutathione and polyamine metabolism → impaired cellular antioxidant responses (colonna2023functionalassessmentof pages 1-1)

#### 6.2 Recent mechanistic developments (2023)
A 2023 Human Molecular Genetics functional study of a homozygous ALDH18A1 variant (p.Thr331Pro) used NMR metabolomics and showed reduced glutamate and glutamate‑derived metabolites “including proline and glutathione,” and decreased biosynthesis of putrescine (ornithine‑derived), with RNA‑seq changes in metabolic and ECM‑related genes. (colonna2023functionalassessmentof pages 1-1)

#### 6.3 Suggested ontology terms
- **GO biological process (examples)**: proline biosynthetic process; ornithine biosynthetic process; glutathione metabolic process; polyamine biosynthetic process.
- **GO cellular component**: mitochondrion.
- **CHEBI (examples)**: L‑proline, L‑ornithine, L‑arginine, L‑citrulline, glutamate, glutathione, putrescine.
- **Cell types (CL)**: upper motor neuron (for HSP manifestations; specific CL mapping not provided in retrieved texts).

### 7. Anatomical structures affected
- **Nervous system**: corticospinal tract degeneration/upper motor neuron syndrome in SPG9; brain structural abnormalities (white matter, corpus callosum) in some complex cases. (awuah2024hereditaryspasticparaplegia pages 1-2, kalmar2021tremorasan pages 1-2)
- **Skin/connective tissue**: cutis laxa, joint hyperlaxity. (fischerzirnsak2015recurrentdenovo pages 1-2)
- **Eye**: cataracts/corneal clouding common in neurocutaneous and some SPG9 cases. (fischerzirnsak2015recurrentdenovo pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- **Vasculature**: cranial vessel tortuosity in a subset of ADCL3 Arg138 cases. (fischerzirnsak2015recurrentdenovo pages 1-2, fischerzirnsak2015recurrentdenovo media 44a36465)

Suggested UBERON (examples): skin; brain; corpus callosum; corticospinal tract; eye lens; arteries.

### 8. Temporal development
- **ARCL3A / severe neurocutaneous**: typically congenital/early onset; can be very severe; associated with growth restriction and early systemic involvement. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- **ADCL3 Arg138**: prenatal growth restriction and early postnatal manifestations; psychomotor delay. (fischerzirnsak2015recurrentdenovo pages 1-2)
- **SPG9A/SPG9B**: generally later onset upper motor neuron syndrome, with SPG9B typically more severe than SPG9A in growth/cognitive features per review synthesis. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

### 9. Inheritance and population

#### 9.1 Inheritance
- **Autosomal dominant**: SPG9A; ADCL3 (often de novo). (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, fischerzirnsak2015recurrentdenovo pages 1-2)
- **Autosomal recessive**: SPG9B; ARCL3A. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5, chen2021novelcompoundmissense pages 1-2)

#### 9.2 Epidemiology and statistics
ALDH18A1‑specific prevalence is not established in the retrieved sources. Available proxy statistics:
- **Cutis laxa (overall)** estimated incidence: **1:2–400,000**. (gardeitchik2014clinicalandbiochemical pages 1-2)
- **HSP (overall)**: global incidence reported as **3.6 per 100,000** in a 2024 review; HSP “does not reduce a person’s lifespan.” (awuah2024hereditaryspasticparaplegia pages 1-2)
- Literature case counts compiled in a 2020 review: **32 neurocutaneous patients** (21 familial biallelic; 11 sporadic de novo heterozygous) and **50 SPG9 patients** (14 biallelic; 36 monoallelic). (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- Detection benchmarking in cohorts: ALDH18A1 heterozygous variants in **2/530** screened HSP patients in one 2015 study. (coutelier2015alterationofornithine pages 5-5)

### 10. Diagnostics

#### 10.1 Clinical and biochemical testing
- **Plasma amino acids**: low ornithine/citrulline/arginine/proline may suggest P5CS deficiency. (coutelier2015alterationofornithine pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- **Functional confirmation**: glutamine loading tests in patient fibroblasts can show a metabolic block at P5CS. (coutelier2015alterationofornithine pages 1-2)
- **Protein quantification**: ELISA can show significantly decreased plasma P5CS concentration in SPG9B (used to support variant pathogenicity). (chen2021novelcompoundmissense pages 1-2)

#### 10.2 Imaging
- Corpus callosum dysgenesis/hypoplasia and white‑matter reduction are reported in PYCR1/ALDH18A1‑related cutis laxa spectrum and in an SPG9B child. (gardeitchik2014clinicalandbiochemical pages 1-2, kalmar2021tremorasan pages 1-2)

#### 10.3 Genetic testing and real‑world implementation
- Whole‑exome sequencing with RNA splicing analysis was used to diagnose SPG9B and characterize intronic splice variants; splicing prediction and RNA assays were emphasized as informative. (chen2021novelcompoundmissense pages 1-2)
- Large HSP screening approach (2015): ALDH18A1 evaluated across 530 HSP patients (435 WES; 95 panel). (coutelier2015alterationofornithine pages 5-5)
- 2023 real‑world cohort (South Africa; 61 probands total): after initial targeted tests, remaining cases underwent WES or WGS; among 29 HSP probands, **48%** were solved genetically, with ALDH18A1 represented among solved genes (single case). Variant curation used internal African‑ancestry control genomes (n=537) and ClinGen SVI guidance. (mahungu2023themutationalprofile pages 1-2)

#### 10.4 Differential diagnosis
Within “neurometabolic cutis laxa,” strong overlap exists early in life; diagnostic discrimination can depend on metabolic testing and imaging. In a 26‑child cohort referred for suspected ARCL, mutations were found in 16 children (14 probands), and corpus callosum dysgenesis/dystonic posturing were associated with PYCR1 and ALDH18A1. (gardeitchik2014clinicalandbiochemical pages 1-2)

### 11. Outcomes / prognosis
- The ALDH18A1 spectrum ranges from severe early neurocutaneous disease (including growth restriction and multisystem involvement) to later‑onset spastic paraplegia. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- HSP broadly does not reduce lifespan, but impairs quality of life. (awuah2024hereditaryspasticparaplegia pages 1-2)
- No ALDH18A1‑specific survival curves, life expectancy estimates, or validated prognostic biomarkers were present in the retrieved sources.

### 12. Treatment

#### 12.1 Metabolic interventions (evidence and rationale)
- Early ARCL3A cases included paradoxical hyperammonemia “alleviated by protein,” suggesting dietary intake can modulate metabolic phenotype. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
- A 2020 review cites literature describing a “novel therapy with arginine” (full primary report not retrievable here), consistent with the pathway logic of replenishing urea‑cycle amino acids. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 18-22)

#### 12.2 Supportive management
Disease‑specific management guidelines were not present in the retrieved corpus. For HSP broadly, there is “no disease‑modifying treatment,” implying management is symptomatic/supportive. (awuah2024hereditaryspasticparaplegia pages 1-2)

#### 12.3 Experimental directions
A review of amino‑acid synthesis deficiencies summarizes attempted and hypothesized treatments in P5CS deficiency, including L‑glutamine escalation (minimal clinical change despite biochemical/EEG improvement) and potential therapeutic interest in nicotinamide due to NAD rescue in cellular models. (koning2017aminoacidsynthesis pages 6-7)

#### 12.4 Clinical trials
A ClinicalTrials.gov search for ALDH18A1/P5CS did not surface any clearly ALDH18A1‑specific interventional trials in the retrieved set; returned trials were unrelated. (clinical‑trial tool output; no trial context IDs were provided for ALDH18A1‑specific disease trials).

**Suggested MAXO terms (examples)**:
- Amino acid supplementation therapy (arginine/proline/ornithine) (conceptual; limited primary evidence in retrieved texts) (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 18-22)
- Physical therapy / rehabilitation therapy for spasticity (general HSP supportive care; not ALDH18A1‑specific in evidence) (awuah2024hereditaryspasticparaplegia pages 1-2)

### 13. Prevention
Primary prevention is not available (genetic disorder). Secondary/tertiary prevention centers on:
- Early molecular diagnosis enabling anticipatory care and family counseling (fischerzirnsak2015recurrentdenovo pages 1-2)
- Genetic counseling given de novo dominant cases and recessive inheritance patterns (fischerzirnsak2015recurrentdenovo pages 1-2, marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)

### 14. Other species / natural disease
No naturally occurring veterinary ALDH18A1‑related analogs were identified in the retrieved sources.

### 15. Model organisms
The retrieved sources did not include specific ALDH18A1 animal models. The 2023 functional study used patient fibroblasts and an ALDH18A1‑null human embryonic kidney cell system expressing variant P5CS for mechanistic validation. (colonna2023functionalassessmentof pages 1-1)

### Expert opinion / analysis (synthesis across authoritative sources)
1) **Nosology**: Multiple expert sources argue ALDH18A1 disorders should be conceptualized as a **single P5CS deficiency continuum**, with “essentially different spectra of ALDH18A1 mutations” producing dominant/recessive and neurocutaneous/motor presentations but sharing decreased P5CS function. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5)
2) **Diagnostics**: ALDH18A1 is unusual among HSP genes in having a plausible **trait biomarker** (low urea‑cycle amino acids/proline) and functional confirmation tests in fibroblasts; therefore adding plasma amino‑acid chromatography can be rational in the diagnostic work‑up, especially when genetic results are uncertain. (coutelier2015alterationofornithine pages 1-2)
3) **Current research direction**: The 2023 multi‑omics study shifts the field from single‑metabolite thinking to **system‑level metabolic and redox pathway disruption** (glutathione/putrescine), suggesting new biomarker candidates and therapeutic hypotheses (antioxidant/NAD‑related interventions) that need clinical validation. (colonna2023functionalassessmentof pages 1-1, koning2017aminoacidsynthesis pages 6-7)

### Key figure/table evidence
A key table summarizing frequency of clinical findings in the eight‑person Arg138 de novo cohort is available and should be consulted for structured phenotyping. (fischerzirnsak2015recurrentdenovo media 44a36465)

### Limitations of this report (evidence gaps)
- Orphanet/ICD‑10/ICD‑11/MeSH identifiers and ALDH18A1‑specific prevalence/incidence were not retrievable via the provided tools in this run.
- The primary 2012 “novel therapy with arginine” study was not obtainable, so arginine treatment details (dose/outcomes) cannot be stated beyond citation‑level mention in a review. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 18-22)
- No ALDH18A1‑specific interventional clinical trials were identified in the retrieved ClinicalTrials.gov results.


References

1. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 1-5): Clara Marco‐Marín, Juan M. Escamilla‐Honrubia, José L. Llácer, Marco Seri, Emanuele Panza, and Vicente Rubio. Δ<sup>1</sup>‐pyrroline‐5‐carboxylate synthetase deficiency: an emergent multifaceted urea cycle‐related disorder. Journal of Inherited Metabolic Disease, 43:657-670, Feb 2020. URL: https://doi.org/10.1002/jimd.12220, doi:10.1002/jimd.12220. This article has 33 citations and is from a peer-reviewed journal.

2. (colonna2023functionalassessmentof pages 1-1): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 20 citations and is from a domain leading peer-reviewed journal.

3. (kalmar2021tremorasan pages 1-2): Tibor Kalmár, Zoltán Maróti, Alíz Zimmermann, and László Sztriha. Tremor as an early sign of hereditary spastic paraplegia due to mutations in aldh18a1. Brain and Development, 43:144-151, Jan 2021. URL: https://doi.org/10.1016/j.braindev.2020.07.015, doi:10.1016/j.braindev.2020.07.015. This article has 10 citations and is from a peer-reviewed journal.

4. (chen2021novelcompoundmissense pages 1-2): Yi-Jun Chen, Zai-Qiang Zhang, Meng-Wen Wang, Yu-Sen Qiu, Ru-Ying Yuan, En-Lin Dong, Zhe Zhao, Hai-Tao Zhou, Ning Wang, Wan-Jin Chen, and Xiang Lin. Novel compound missense and intronic splicing mutation in aldh18a1 causes autosomal recessive spastic paraplegia. Frontiers in Neurology, May 2021. URL: https://doi.org/10.3389/fneur.2021.627531, doi:10.3389/fneur.2021.627531. This article has 7 citations and is from a peer-reviewed journal.

5. (gardeitchik2014clinicalandbiochemical pages 1-2): Thatjana Gardeitchik, Miski Mohamed, Björn Fischer, Martin Lammens, Dirk Lefeber, Baiba Lace, Michael Parker, Ki-Joong Kim, Bing C Lim, Johannes Häberle, Livia Garavelli, Sujatha Jagadeesh, Ariana Kariminejad, Deanna Guerra, Michel Leão, Riikka Keski-Filppula, Han Brunner, Leo Nijtmans, Bert van den Heuvel, Ron Wevers, Uwe Kornak, and Eva Morava. Clinical and biochemical features guiding the diagnostics in neurometabolic cutis laxa. European Journal of Human Genetics, 22:888-895, Aug 2014. URL: https://doi.org/10.1038/ejhg.2013.154, doi:10.1038/ejhg.2013.154. This article has 67 citations and is from a domain leading peer-reviewed journal.

6. (OpenTargets Search: -ALDH18A1): Open Targets Query (-ALDH18A1, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (fischerzirnsak2015recurrentdenovo pages 1-2): Björn Fischer-Zirnsak, Nathalie Escande-Beillard, Jaya Ganesh, Yu Xuan Tan, Mohammed Al Bughaili, Angela E. Lin, Inderneel Sahai, Paulina Bahena, Sara L. Reichert, Abigail Loh, Graham D. Wright, Jaron Liu, Elisa Rahikkala, Eniko K. Pivnick, Asim F. Choudhri, Ulrike Krüger, Tomasz Zemojtel, Conny van Ravenswaaij-Arts, Roya Mostafavi, Irene Stolte-Dijkstra, Sofie Symoens, Leila Pajunen, Lihadh Al-Gazali, David Meierhofer, Peter N. Robinson, Stefan Mundlos, Camilo E. Villarroel, Peter Byers, Amira Masri, Stephen P. Robertson, Ulrike Schwarze, Bert Callewaert, Bruno Reversade, and Uwe Kornak. Recurrent de novo mutations affecting residue arg138 of pyrroline-5-carboxylate synthase cause a progeroid form of autosomal-dominant cutis laxa. American journal of human genetics, 97 3:483-92, Sep 2015. URL: https://doi.org/10.1016/j.ajhg.2015.08.001, doi:10.1016/j.ajhg.2015.08.001. This article has 93 citations and is from a highest quality peer-reviewed journal.

8. (fischerzirnsak2015recurrentdenovo media 44a36465): Björn Fischer-Zirnsak, Nathalie Escande-Beillard, Jaya Ganesh, Yu Xuan Tan, Mohammed Al Bughaili, Angela E. Lin, Inderneel Sahai, Paulina Bahena, Sara L. Reichert, Abigail Loh, Graham D. Wright, Jaron Liu, Elisa Rahikkala, Eniko K. Pivnick, Asim F. Choudhri, Ulrike Krüger, Tomasz Zemojtel, Conny van Ravenswaaij-Arts, Roya Mostafavi, Irene Stolte-Dijkstra, Sofie Symoens, Leila Pajunen, Lihadh Al-Gazali, David Meierhofer, Peter N. Robinson, Stefan Mundlos, Camilo E. Villarroel, Peter Byers, Amira Masri, Stephen P. Robertson, Ulrike Schwarze, Bert Callewaert, Bruno Reversade, and Uwe Kornak. Recurrent de novo mutations affecting residue arg138 of pyrroline-5-carboxylate synthase cause a progeroid form of autosomal-dominant cutis laxa. American journal of human genetics, 97 3:483-92, Sep 2015. URL: https://doi.org/10.1016/j.ajhg.2015.08.001, doi:10.1016/j.ajhg.2015.08.001. This article has 93 citations and is from a highest quality peer-reviewed journal.

9. (mahungu2023themutationalprofile pages 1-2): Amokelani C. Mahungu, Elizabeth Steyn, Niki Floudiotis, Lindsay A. Wilson, Jana Vandrovcova, Mary M. Reilly, Christopher J. Record, Michael Benatar, Gang Wu, Sharika Raga, Jo M. Wilmshurst, Kireshnee Naidu, Michael Hanna, Melissa Nel, and Jeannine M. Heckmann. The mutational profile in a south african cohort with inherited neuropathies and spastic paraplegia. Frontiers in Neurology, Aug 2023. URL: https://doi.org/10.3389/fneur.2023.1239725, doi:10.3389/fneur.2023.1239725. This article has 14 citations and is from a peer-reviewed journal.

10. (coutelier2015alterationofornithine pages 1-2): Marie Coutelier, Cyril Goizet, Alexandra Durr, Florence Habarou, Sara Morais, Alexandre Dionne-Laporte, Feifei Tao, Juliette Konop, Marion Stoll, Perrine Charles, Maxime Jacoupy, Raphaël Matusiak, Isabel Alonso, Chantal Tallaksen, Mathilde Mairey, Marina Kennerson, Marion Gaussen, Rebecca Schule, Maxime Janin, Fanny Morice-Picard, Christelle M. Durand, Christel Depienne, Patrick Calvas, Paula Coutinho, Jean-Marie Saudubray, Guy Rouleau, Alexis Brice, Garth Nicholson, Frédéric Darios, José L. Loureiro, Stephan Zuchner, Chris Ottolenghi, Fanny Mochel, and Giovanni Stevanin. Alteration of ornithine metabolism leads to dominant and recessive hereditary spastic paraplegia. Brain : a journal of neurology, 138 Pt 8:2191-205, Aug 2015. URL: https://doi.org/10.1093/brain/awv143, doi:10.1093/brain/awv143. This article has 114 citations.

11. (colonna2023functionalassessmentof pages 1-2): Maxwell B Colonna, Tonya Moss, Sneha Mokashi, Sujata Srikanth, Julie R Jones, Jackson R Foley, Cindy Skinner, Angie Lichty, Anthony Kocur, Tim Wood, Tracy Murray Stewart, Robert A Casero Jr., Heather Flanagan-Steet, Arthur S Edison, Michael J Lyons, and Richard Steet. Functional assessment of homozygous aldh18a1 variants reveals alterations in amino acid and antioxidant metabolism. Human molecular genetics, 32:732-744, Sep 2023. URL: https://doi.org/10.1093/hmg/ddac226, doi:10.1093/hmg/ddac226. This article has 20 citations and is from a domain leading peer-reviewed journal.

12. (panza2016aldh18a1genemutations pages 8-8): Emanuele Panza, Juan M. Escamilla-Honrubia, Clara Marco-Marín, Nadine Gougeard, Giuseppe De Michele, Vincenzo Brescia Morra, Rocco Liguori, Leonardo Salviati, Maria Alice Donati, Roberto Cusano, Tommaso Pippucci, Roberto Ravazzolo, Andrea H. Németh, Sarah Smithson, Sally Davies, Jane A. Hurst, Domenico Bordo, Vicente Rubio, and Marco Seri. Aldh18a1 gene mutations cause dominant spastic paraplegia spg9: loss of function effect and plausibility of a dominant negative mechanism. Brain : a journal of neurology, 139 Pt 1:e3, Aug 2016. URL: https://doi.org/10.1093/brain/awv247, doi:10.1093/brain/awv247. This article has 61 citations.

13. (lugli2022autosomalrecessivecutis pages 6-6): Licia Lugli, Francesca Cavalleri, Emma Bertucci, Björn Fischer-Zirnsak, Giulia Cinelli, Viola Trevisani, Cecilia Rossi, Marika Riva, Lorenzo Iughetti, and Alberto Berardi. Autosomal recessive cutis laxa type iiia: report of a patient with severe phenotype and review of the literature. European Journal of Medical Genetics, 65:104568, Sep 2022. URL: https://doi.org/10.1016/j.ejmg.2022.104568, doi:10.1016/j.ejmg.2022.104568. This article has 6 citations and is from a peer-reviewed journal.

14. (fischerzirnsak2026neurocutaneousdisordersduea pages 20-22): B Fischer-Zirnsak and BL Callewaert. Neurocutaneous disorders due to mitochondrial proline synthesis defects. Unknown journal, 2026.

15. (awuah2024hereditaryspasticparaplegia pages 1-2): Wireko Andrew Awuah, Joecelyn Kirani Tan, Anastasiia D Shkodina, Tomas Ferreira, Favour Tope Adebusoye, Adele Mazzoleni, Jack Wellington, Lian David, Ellie Chilcott, Helen Huang, Toufik Abdul-Rahman, Vallabh Shet, Oday Atallah, Jacob Kalmanovich, Riaz Jiffry, Divine Elizabeth Madhu, Kateryna Sikora, Oleksii Kmyta, and Mykhailo Yu Delva. Hereditary spastic paraplegia: novel insights into the pathogenesis and management. SAGE Open Medicine, Dec 2024. URL: https://doi.org/10.1177/20503121231221941, doi:10.1177/20503121231221941. This article has 29 citations.

16. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 5-9): Clara Marco‐Marín, Juan M. Escamilla‐Honrubia, José L. Llácer, Marco Seri, Emanuele Panza, and Vicente Rubio. Δ<sup>1</sup>‐pyrroline‐5‐carboxylate synthetase deficiency: an emergent multifaceted urea cycle‐related disorder. Journal of Inherited Metabolic Disease, 43:657-670, Feb 2020. URL: https://doi.org/10.1002/jimd.12220, doi:10.1002/jimd.12220. This article has 33 citations and is from a peer-reviewed journal.

17. (coutelier2015alterationofornithine pages 5-5): Marie Coutelier, Cyril Goizet, Alexandra Durr, Florence Habarou, Sara Morais, Alexandre Dionne-Laporte, Feifei Tao, Juliette Konop, Marion Stoll, Perrine Charles, Maxime Jacoupy, Raphaël Matusiak, Isabel Alonso, Chantal Tallaksen, Mathilde Mairey, Marina Kennerson, Marion Gaussen, Rebecca Schule, Maxime Janin, Fanny Morice-Picard, Christelle M. Durand, Christel Depienne, Patrick Calvas, Paula Coutinho, Jean-Marie Saudubray, Guy Rouleau, Alexis Brice, Garth Nicholson, Frédéric Darios, José L. Loureiro, Stephan Zuchner, Chris Ottolenghi, Fanny Mochel, and Giovanni Stevanin. Alteration of ornithine metabolism leads to dominant and recessive hereditary spastic paraplegia. Brain : a journal of neurology, 138 Pt 8:2191-205, Aug 2015. URL: https://doi.org/10.1093/brain/awv143, doi:10.1093/brain/awv143. This article has 114 citations.

18. (marco‐marin2020δ1‐pyrroline‐5‐carboxylatesynthetasedeficiency pages 18-22): Clara Marco‐Marín, Juan M. Escamilla‐Honrubia, José L. Llácer, Marco Seri, Emanuele Panza, and Vicente Rubio. Δ<sup>1</sup>‐pyrroline‐5‐carboxylate synthetase deficiency: an emergent multifaceted urea cycle‐related disorder. Journal of Inherited Metabolic Disease, 43:657-670, Feb 2020. URL: https://doi.org/10.1002/jimd.12220, doi:10.1002/jimd.12220. This article has 33 citations and is from a peer-reviewed journal.

19. (koning2017aminoacidsynthesis pages 6-7): T. J. de Koning. Amino acid synthesis deficiencies. Journal of Inherited Metabolic Disease, 40:609-620, Jun 2017. URL: https://doi.org/10.1007/s10545-017-0063-1, doi:10.1007/s10545-017-0063-1. This article has 87 citations and is from a peer-reviewed journal.
