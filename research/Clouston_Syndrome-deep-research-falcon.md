---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:06:34.251499'
end_time: '2026-04-24T18:21:18.540709'
duration_seconds: 884.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Clouston Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Clouston Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Clouston Syndrome** covering all of the
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
- **Disease Name:** Clouston Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Clouston Syndrome** covering all of the
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


# Clouston Syndrome (Hidrotic Ectodermal Dysplasia 2; HED2): Comprehensive Disease Characteristics Report

## Executive summary (current understanding)
Clouston syndrome is a rare **autosomal dominant** ectodermal dysplasia primarily affecting **hair, nails, and palmoplantar skin**, classically presenting with the triad of **nail dystrophy, hypotrichosis/alopecia, and palmoplantar hyperkeratosis**, typically with **normal sweating and normal dentition** (OMIM #129500). Core evidence includes a large 2023 multi-generation Chinese pedigree study identifying a novel GJB6 variant and detailing age-related clinical evolution, and mechanistic 2024 synthesis highlighting **connexin hemichannel gain-of-function** as a therapeutic target. (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3, yasarbas2024connexinsinepidermal pages 15-17)

## 1. Disease information
### 1.1 Disease overview
Clouston syndrome (hidrotic ectodermal dysplasia type 2) is an ectodermal dysplasia characterized by the triad of **nail dystrophy**, **partial-to-complete alopecia/hypotrichosis**, and **palmoplantar hyperkeratosis**, with **no sweat gland or tooth abnormalities** in typical cases. (huang2023anovelvariant pages 1-2)

**Direct abstract quote (2023, Frontiers of Medicine):** “Clouston syndrome (OMIM #129500), also known as hidrotic ectodermal dysplasia type 2, is a rare autosomal dominant skin disorder.” (huang2023anovelvariant pages 1-2)

### 1.2 Key identifiers (available from retrieved full text)
- **OMIM:** 129500 (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)
- **ICD-10 (used in a Danish ectodermal dysplasia cohort):** Q82.4B “dysplasia ectodermalis hidrotica” (used for case ascertainment; Clouston syndrome was the second most common condition in that cohort). (svendsen2014aretrospectivestudy pages 1-2)
- **MONDO / Orphanet / MeSH:** Not directly retrievable from the full-text sources obtained in this run; therefore not asserted here.

### 1.3 Synonyms / alternative names
- Hidrotic ectodermal dysplasia type 2; hidrotic ectodermal dysplasia 2 (HED2) (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)
- “Ectodermal dysplasia 2, Clouston type (ECTD2)” (as listed in a 2024 classification-oriented text) (peschel2024differentialdiagnostischeeinordnungektodermaler pages 22-23)

### 1.4 Evidence source type
Most disease information here is derived from **aggregated disease-level resources embedded in primary/review literature** (OMIM-linked descriptions) and from **individual/family-based studies** (case/family cohorts with molecular confirmation). (huang2023anovelvariant pages 1-2, kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3, baris2008anovelgjb6 pages 1-3)

## 2. Etiology
### 2.1 Primary causal factors
**Genetic etiology:** Pathogenic variants in **GJB6** (encoding **connexin 30, Cx30**) cause Clouston syndrome. (baris2008anovelgjb6 pages 1-3, huang2023anovelvariant pages 1-2)

- Baris et al. (2008) states positional cloning identified **GJB6 on chromosome 13q12** as the causative gene; the disorder is autosomal dominant with hair, nail, and palmoplantar findings and normal sweating/dentition. (baris2008anovelgjb6 pages 1-3)

### 2.2 Risk factors
- **Genetic risk factor:** having a heterozygous pathogenic variant in **GJB6** (autosomal dominant). (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)
- **Family history:** consistent with autosomal dominant segregation in large pedigrees. (huang2023anovelvariant pages 2-4)

No credible environmental/toxic/infectious risk factors were identified in the retrieved corpus.

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved corpus.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved corpus.

## 3. Phenotypes
### 3.1 Core phenotype spectrum
**Canonical triad and typical sparing of sweat glands/teeth**
- Nail dystrophy, hypotrichosis/alopecia, palmoplantar hyperkeratosis; sweating and dentition typically normal. (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)

**Detailed phenotypes from a large 2023 pedigree (China; 60 individuals, 22 affected):**
- Hair: absent/sparse scalp hair, eyebrows, eyelashes from birth in the proband; severity may intensify with age. (huang2023anovelvariant pages 1-2)
- Nails: curvature increase by ~5–6 months; thickened/shortened/slow-growing by ~1 year in the proband. (huang2023anovelvariant pages 1-2)
- Palmoplantar keratoderma/hyperkeratosis: developed gradually after puberty in the proband; palms mild, soles more obvious. (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 2-4)
- Sweat glands/teeth/hearing/cognition: reported as normal in that pedigree. (huang2023anovelvariant pages 1-2)

**Novel/expanded phenotype (2023 pedigree):** “all nail needling pain” (cold-triggered nail pain is described in the study body) (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 4-7)

### 3.2 Onset, severity, progression
- **Onset:** can be congenital/early-life for hair and nail changes (birth to infancy). (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)
- **Progression:** variable expressivity; in the 2023 pedigree, palmoplantar hyperkeratosis emerged after puberty and some individuals worsened with age while others improved. (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 2-4)
- **Variable expressivity:** documented within families; mild forms can complicate diagnosis. (kutkowskakazmierczak2015phenotypicvariabilityin pages 3-5)

### 3.3 Suggested HPO terms (non-exhaustive; for knowledge base population)
(ontology suggestions; not claims of frequency unless noted above)
- Nail dystrophy: **HP:0002164**
- Onycholysis: **HP:0001806**
- Palmoplantar keratoderma: **HP:0000972**
- Alopecia: **HP:0001596**
- Hypotrichosis: **HP:0001006**
- Sparse eyebrows: **HP:0000535**
- Sparse eyelashes: **HP:0000653**
- Normal sweating (as absence of hypohidrosis): **HP:0000970** is *hypohidrosis* (use negation/absence where supported) (baris2008anovelgjb6 pages 1-3)

### 3.4 Quality of life impact
The retrieved sources did not include standardized quality-of-life instruments. However, clinically, nail dystrophy and palmoplantar hyperkeratosis can plausibly impair function and cause pain; in the 2023 pedigree, cold-triggered nail pain was severe (NRS values described in the paper body). (huang2023anovelvariant pages 4-7)

## 4. Genetic / molecular information
### 4.1 Causal gene
- **GJB6** (connexin 30, Cx30) (baris2008anovelgjb6 pages 1-3, huang2023anovelvariant pages 1-2)

### 4.2 Pathogenic variants (reported in retrieved primary literature)
**Variants repeatedly referenced as confirmed disease-causing in Clouston syndrome:**
- **G11R**, **V37E**, **A88V**, **D50N** (huang2023anovelvariant pages 1-2)

**Examples with specific evidence and mapping**
- **D50N**: Baris et al. (2008) reports heterozygous nucleotide 148 G>A leading to **D50N** in the first extracellular loop (E1) in a mother and son with HED2. (baris2008anovelgjb6 pages 1-3)
- **p.Gly11Arg (c.31G>C)**: reported in a Polish family with Clouston syndrome; authors emphasize diagnostic difficulty due to variability. (kutkowskakazmierczak2015phenotypicvariabilityin pages 3-5)
- **c.134G>C (p.G45A)**: novel heterozygous missense variant reported in a large Chinese pedigree; absent from gnomAD in the study’s report and classified as likely pathogenic by ACMG criteria. (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 2-4)

**Domain localization (from 2023 synthesis within the pedigree paper):**
- G11R in cytoplasmic N-terminus; V37E in M1; A88V in M2; D50N in E1; and the newly reported G45A in an adjacent membrane region. (huang2023anovelvariant pages 7-8)

### 4.3 Variant consequences (functional class)
A current mechanistic theme is **hemichannel gain-of-function (“hyperactive hemichannels”)** for at least some Cx30 mutants (e.g., A88V, G11R) with downstream ATP/Ca2+ signaling effects in keratinocytes, alongside trafficking/gap-junction effects that may be context dependent. (yasarbas2024connexinsinepidermal pages 11-12, yasarbas2024connexinsinepidermal pages 15-17)

### 4.4 Modifier genes / epigenetics
The 2023 pedigree study discusses potential reasons for intrafamilial variability (e.g., polymorphisms in keratins/connexins and regulatory-region variants) and suggests sequencing regulatory regions, but specific validated modifier genes were not established in the retrieved text. (huang2023anovelvariant pages 7-8)

## 5. Environmental information
No specific environmental, lifestyle, or infectious contributors were identified in the retrieved corpus. Clouston syndrome is primarily a monogenic disorder (GJB6). (baris2008anovelgjb6 pages 1-3, huang2023anovelvariant pages 1-2)

## 6. Mechanism / pathophysiology (prioritizing 2024–2023)
### 6.1 Connexin biology and pathogenic mechanism
Connexins form **gap junction channels** (cell-to-cell) and can also form **hemichannels** (cell-to-extracellular). A key disease mechanism highlighted in recent work is **hyperactive (“leaky”) hemichannel activity**, enabling abnormal flux of signaling molecules such as **ATP and Ca2+**, which can disrupt keratinocyte proliferation/differentiation programs. (yasarbas2024connexinsinepidermal pages 15-17, yasarbas2024connexinsinepidermal pages 11-12)

### 6.2 Causal chain (example: Cx30-A88V)
1. **GJB6 missense variant** → mutant Cx30 with altered trafficking/function (some context-dependent rescue by WT co-expression). (yasarbas2024connexinsinepidermal pages 11-12)
2. **Hyperactive hemichannels** → increased ATP release and Ca2+ influx signaling. (yasarbas2024connexinsinepidermal pages 11-12, yasarbas2024connexinsinepidermal pages 15-17)
3. **Altered keratinocyte behavior** (proliferation/differentiation) and adnexal effects (e.g., sebaceous gland enlargement in models) → clinical hyperkeratosis and appendage phenotypes. (yasarbas2024connexinsinepidermal pages 11-12)

### 6.3 Pathways / GO / cell types (suggestions)
- Suggested GO Biological Process terms:
  - Gap junction assembly (**GO:1904322**)
  - Cell–cell junction organization (**GO:0045216**)
  - Epidermis development (**GO:0008544**)
  - Keratinocyte differentiation (**GO:0030216**)
  - ATP metabolic/signaling processes (context-dependent)
- Suggested Cell Ontology (CL) terms:
  - Keratinocyte (**CL:0000312**)
  - Sebocyte (**CL:0000638**)

### 6.4 Model systems / molecular profiling
- A **Cx30-A88V mouse model** recapitulated key features including “mild palmoplantar hyperkeratosis, enlarged sebaceous glands, and deafness,” and was used to validate hemichannel blockade strategies. (yasarbas2024connexinsinepidermal pages 11-12)
- The 2023 family study used histopathology and hair microscopy/SEM to characterize hair follicle scarcity and distinctive hair ultrastructure. (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 2-4)

## 7. Anatomical structures affected
### 7.1 Organ/system level (primary)
- Skin and appendages: hair follicles, nails, palmoplantar epidermis. (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)

### 7.2 Tissue/cell level (suggestions)
- Epidermis (keratinocytes), hair follicle outer root sheath (Cx30 expression referenced in discussion), nail bed dermis with superficial vessels (reported histology in the 2023 pedigree). (huang2023anovelvariant pages 2-4)

### 7.3 UBERON suggestions
- Skin of body (**UBERON:0002097**)
- Hair follicle (**UBERON:0002199**)
- Nail (**UBERON:0001708**)
- Palm skin (**UBERON:0001456**) / sole of foot skin (use relevant UBERON terms)

## 8. Temporal development
- **Congenital/early childhood onset** is common for hair and nail findings in reported cases. (baris2008anovelgjb6 pages 1-3, huang2023anovelvariant pages 1-2)
- **Adolescent/post-pubertal development** of palmoplantar hyperkeratosis was documented in the 2023 pedigree’s proband. (huang2023anovelvariant pages 1-2)
- Course is **variable**, including worsening with age in some and partial self-improvement in others (intrafamilial variability). (huang2023anovelvariant pages 2-4)

## 9. Inheritance and population
### 9.1 Inheritance, penetrance, expressivity
- **Autosomal dominant** inheritance is repeatedly stated. (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)
- **Variable expressivity** is well documented, including mild presentations that could be misclassified without molecular testing. (kutkowskakazmierczak2015phenotypicvariabilityin pages 3-5, kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3)

### 9.2 Epidemiology (available statistics)
- **Prevalence estimate (global):** “affecting 1 out of 100 000 individuals” (from the 2023 paper’s introduction). (huang2023anovelvariant pages 1-2)
- **Danish clinical cohort context (1994–2013):** In a retrospective study of 45 Danish ED families, **Clouston syndrome was the second most common condition (n=10 patients, 4 families)** among ED diagnoses captured via ICD-10 codes including Q82.4B. This is not a prevalence estimate, but provides real-world ascertainment frequency in a tertiary center cohort. (svendsen2014aretrospectivestudy pages 1-2)

### 9.3 Population/variant notes
- The 2023 pedigree paper summarizes that G11R and A88V are common in Chinese pedigree reports, and catalogs multiple variants across diverse reported ancestries. (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 7-8)

## 10. Diagnostics
### 10.1 Clinical diagnosis
Clinical recognition is based on the triad (nail, hair, palmoplantar keratoderma) with preserved sweating and teeth; however, phenotypic overlap with other genodermatoses and intrafamilial variability can confound diagnosis. (kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3)

### 10.2 Genetic testing (recommended approach based on evidence)
- **Molecular confirmation is strongly recommended.**
  - Kutkowska-Kaźmierczak et al. (2015) abstract conclusion: “proper diagnosis of these syndromes is still challenging and should always be followed by molecular verification.” (kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3)
  - The 2023 pedigree paper concludes that “genetic testing is necessary for the diagnosis of Clouston syndrome.” (huang2023anovelvariant pages 1-2)
- Testing modalities used in key reports include **whole-exome sequencing (WES)** followed by **Sanger sequencing** for segregation/confirmation. (huang2023anovelvariant pages 1-2, huang2023anovelvariant pages 2-4)

### 10.3 Histology / ancillary studies
- Scalp biopsy in Clouston may show **absent hair follicles with preserved eccrine/sebaceous gland distribution** (documented both in 2008 and 2023 reports). (baris2008anovelgjb6 pages 1-3, huang2023anovelvariant pages 2-4)

### 10.4 Differential diagnosis (examples from retrieved sources)
Connexin-related and ectodermal dysplasia differential considerations include other hair–nail disorders and keratodermas; in practice, overlap can necessitate testing of multiple connexin genes. (kutkowskakazmierczak2015phenotypicvariabilityin pages 5-6, kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3)

## 11. Outcome / prognosis
The retrieved sources do not report disease-specific survival statistics for Clouston syndrome. The condition is generally described as affecting ectodermal appendages; major morbidity relates to hair/nail/keratoderma burden and potentially pain.

Mechanistic/model evidence indicates mutant Cx30 can drive proliferative epidermal pathology in vivo, which is relevant to long-term monitoring, but Clouston-specific carcinoma risk statistics were not found in the retrieved corpus. (yasarbas2024connexinsinepidermal pages 11-12)

## 12. Treatment
### 12.1 Current standard of care
No disease-modifying therapy for Clouston syndrome was identified in the retrieved sources. Management is therefore inferred to be **supportive/symptomatic** (e.g., keratoderma care; nail care; pain management), but specific regimens were not detailed in the extracted texts.

### 12.2 Recent developments / experimental therapeutics (2024–2023 prioritized)
A major 2024 development theme is **targeting connexin hemichannels** (and related connexin-directed strategies) for connexinopathies.

- **Hemichannel-blocking antibody approach (preclinical, Clouston model):**
  - A 2024 review reports that the monoclonal antibody **abEC1.1** “also blocked the Cx30-A88V hyperactive hemichannels in Clouston syndrome mouse model,” and that topical/systemic administration reduced skin cell proliferation and sebaceous gland size (supporting hemichannel blockade as a candidate strategy). (yasarbas2024connexinsinepidermal pages 15-17)
- **Allele-specific RNA interference / antisense strategies (platform approaches; not Clouston-specific clinical trials):**
  - The same 2024 review summarizes allele-specific RNAi and antisense oligonucleotide approaches used in related dominant skin disorders and highlights their promise for single-nucleotide pathogenic variants. (yasarbas2024connexinsinepidermal pages 15-17)

### 12.3 MAXO term suggestions (supportive mapping)
- Symptomatic management of hyperkeratosis: **MAXO:0000759** (Skin care) (suggested)
- Genetic testing: **MAXO:0000127** (Genetic testing) (supported by repeated recommendations for molecular verification) (huang2023anovelvariant pages 1-2, kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3)
- Genetic counseling: **MAXO:0000079** (Genetic counseling) (implied by autosomal dominant inheritance and family-based testing) (huang2023anovelvariant pages 1-2, baris2008anovelgjb6 pages 1-3)
- Experimental hemichannel-blocking antibody therapy: map to a therapeutic antibody intervention term (MAXO suggestion; preclinical) (yasarbas2024connexinsinepidermal pages 15-17)

## 13. Prevention
Primary prevention is not applicable for an autosomal dominant Mendelian disorder except via reproductive options.

Secondary/tertiary prevention:
- **Cascade testing** in families and early diagnosis to guide supportive care and anticipate complications is supported by the emphasis on molecular confirmation and pedigree evaluation. (huang2023anovelvariant pages 2-4, kutkowskakazmierczak2015phenotypicvariabilityin pages 7-8)

## 14. Other species / natural disease
No naturally occurring non-human Clouston syndrome analog was identified in the retrieved corpus.

## 15. Model organisms
- **Mouse model (Cx30-A88V):** used to study phenotype and test hemichannel-blocking approaches; recapitulated palmoplantar hyperkeratosis and sebaceous gland enlargement (and deafness in mice). (yasarbas2024connexinsinepidermal pages 11-12)

## Notes on evidence gaps (important for knowledge base curation)
- **Orphanet ID, MeSH ID, and MONDO ID** were not extractable from the retrieved full-text literature in this run; direct database lookups would be required for completeness.
- Clouston-specific standardized QoL measures, penetrance estimates, and robust population prevalence/incidence are limited in the retrieved corpus; one prevalence estimate (1/100,000) is provided in the 2023 pedigree paper introduction. (huang2023anovelvariant pages 1-2)

## Key recent sources (URLs and publication dates)
- Huang H, et al. *Frontiers of Medicine*. Jan 2023. “A novel variant in the GJB6 gene in a large Chinese family with a unique phenotype of Clouston syndrome.” https://doi.org/10.1007/s11684-022-0933-2 (huang2023anovelvariant pages 1-2)
- Yasarbas SS, et al. *Frontiers in Physiology*. May 2024. “Connexins in epidermal health and diseases: insights into their mutations, implications, and therapeutic solutions.” https://doi.org/10.3389/fphys.2024.1346971 (yasarbas2024connexinsinepidermal pages 15-17)
- Baris HN, et al. *British Journal of Dermatology*. Dec 2008. “A novel GJB6 missense mutation in hidrotic ectodermal dysplasia 2 (Clouston syndrome)…” https://doi.org/10.1111/j.1365-2133.2008.08796.x (baris2008anovelgjb6 pages 1-3)
- Kutkowska-Kaźmierczak A, et al. *Journal of Applied Genetics*. Published online 10 Jan 2015 (issue year 2015). https://doi.org/10.1007/s13353-014-0266-1 (kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3)
- Svendsen MT, et al. *Acta Dermato-Venereologica*. Epub ahead of print Feb 4, 2014. https://doi.org/10.2340/00015555-1799 (svendsen2014aretrospectivestudy pages 1-2)


References

1. (huang2023anovelvariant pages 1-2): Hequn Huang, Mengyun Chen, Xia Liu, Xixi Xiong, Lanbo Zhou, Zhonglan Su, Yan Lu, and Bo Liang. A novel variant in the gjb6 gene in a large chinese family with a unique phenotype of clouston syndrome. Frontiers of Medicine, 17:330-338, Jan 2023. URL: https://doi.org/10.1007/s11684-022-0933-2, doi:10.1007/s11684-022-0933-2. This article has 1 citations.

2. (baris2008anovelgjb6 pages 1-3): Hagit N. Baris, Abraham Zlotogorski, G. Peretz-Amit, V. Doviner, Mordechai Shohat, H. Reznik‐Wolf, and E. Pras. A novel gjb6 missense mutation in hidrotic ectodermal dysplasia 2 (clouston syndrome) broadens its genotypic basis. British Journal of Dermatology, 159:1373-1376, Dec 2008. URL: https://doi.org/10.1111/j.1365-2133.2008.08796.x, doi:10.1111/j.1365-2133.2008.08796.x. This article has 47 citations and is from a highest quality peer-reviewed journal.

3. (yasarbas2024connexinsinepidermal pages 15-17): S. Suheda Yasarbas, Ece Inal, M. Azra Yildirim, Sandrine Dubrac, Jérôme Lamartine, and Gulistan Mese. Connexins in epidermal health and diseases: insights into their mutations, implications, and therapeutic solutions. Frontiers in Physiology, May 2024. URL: https://doi.org/10.3389/fphys.2024.1346971, doi:10.3389/fphys.2024.1346971. This article has 20 citations.

4. (svendsen2014aretrospectivestudy pages 1-2): M. Svendsen, E. Henningsen, J. Hertz, Dorthe Vestergaard Grejsen, and A. Bygum. A retrospective study of clinical and mutational findings in 45 danish families with ectodermal dysplasia. Acta dermato-venereologica, 94 5:531-3, Feb 2014. URL: https://doi.org/10.2340/00015555-1799, doi:10.2340/00015555-1799. This article has 19 citations and is from a domain leading peer-reviewed journal.

5. (peschel2024differentialdiagnostischeeinordnungektodermaler pages 22-23): Nicolai Peschel. Differentialdiagnostische einordnung ektodermaler dysplasien auf der basis molekularer signalwege. Text, Jan 2024. URL: https://doi.org/10.25593/open-fau-805, doi:10.25593/open-fau-805. This article has 0 citations and is from a peer-reviewed journal.

6. (kutkowskakazmierczak2015phenotypicvariabilityin pages 1-3): Anna Kutkowska-Kaźmierczak, Katarzyna Niepokój, Katarzyna Wertheim-Tysarowska, Aleksandra Giza, Maria Mordasewicz-Goliszewska, Jerzy Bal, and Ewa Obersztyn. Phenotypic variability in gap junction syndromic skin disorders: experience from kid and clouston syndromes’ clinical diagnostics. Journal of Applied Genetics, 56:329-337, Jan 2015. URL: https://doi.org/10.1007/s13353-014-0266-1, doi:10.1007/s13353-014-0266-1. This article has 18 citations and is from a peer-reviewed journal.

7. (huang2023anovelvariant pages 2-4): Hequn Huang, Mengyun Chen, Xia Liu, Xixi Xiong, Lanbo Zhou, Zhonglan Su, Yan Lu, and Bo Liang. A novel variant in the gjb6 gene in a large chinese family with a unique phenotype of clouston syndrome. Frontiers of Medicine, 17:330-338, Jan 2023. URL: https://doi.org/10.1007/s11684-022-0933-2, doi:10.1007/s11684-022-0933-2. This article has 1 citations.

8. (huang2023anovelvariant pages 4-7): Hequn Huang, Mengyun Chen, Xia Liu, Xixi Xiong, Lanbo Zhou, Zhonglan Su, Yan Lu, and Bo Liang. A novel variant in the gjb6 gene in a large chinese family with a unique phenotype of clouston syndrome. Frontiers of Medicine, 17:330-338, Jan 2023. URL: https://doi.org/10.1007/s11684-022-0933-2, doi:10.1007/s11684-022-0933-2. This article has 1 citations.

9. (kutkowskakazmierczak2015phenotypicvariabilityin pages 3-5): Anna Kutkowska-Kaźmierczak, Katarzyna Niepokój, Katarzyna Wertheim-Tysarowska, Aleksandra Giza, Maria Mordasewicz-Goliszewska, Jerzy Bal, and Ewa Obersztyn. Phenotypic variability in gap junction syndromic skin disorders: experience from kid and clouston syndromes’ clinical diagnostics. Journal of Applied Genetics, 56:329-337, Jan 2015. URL: https://doi.org/10.1007/s13353-014-0266-1, doi:10.1007/s13353-014-0266-1. This article has 18 citations and is from a peer-reviewed journal.

10. (huang2023anovelvariant pages 7-8): Hequn Huang, Mengyun Chen, Xia Liu, Xixi Xiong, Lanbo Zhou, Zhonglan Su, Yan Lu, and Bo Liang. A novel variant in the gjb6 gene in a large chinese family with a unique phenotype of clouston syndrome. Frontiers of Medicine, 17:330-338, Jan 2023. URL: https://doi.org/10.1007/s11684-022-0933-2, doi:10.1007/s11684-022-0933-2. This article has 1 citations.

11. (yasarbas2024connexinsinepidermal pages 11-12): S. Suheda Yasarbas, Ece Inal, M. Azra Yildirim, Sandrine Dubrac, Jérôme Lamartine, and Gulistan Mese. Connexins in epidermal health and diseases: insights into their mutations, implications, and therapeutic solutions. Frontiers in Physiology, May 2024. URL: https://doi.org/10.3389/fphys.2024.1346971, doi:10.3389/fphys.2024.1346971. This article has 20 citations.

12. (kutkowskakazmierczak2015phenotypicvariabilityin pages 5-6): Anna Kutkowska-Kaźmierczak, Katarzyna Niepokój, Katarzyna Wertheim-Tysarowska, Aleksandra Giza, Maria Mordasewicz-Goliszewska, Jerzy Bal, and Ewa Obersztyn. Phenotypic variability in gap junction syndromic skin disorders: experience from kid and clouston syndromes’ clinical diagnostics. Journal of Applied Genetics, 56:329-337, Jan 2015. URL: https://doi.org/10.1007/s13353-014-0266-1, doi:10.1007/s13353-014-0266-1. This article has 18 citations and is from a peer-reviewed journal.

13. (kutkowskakazmierczak2015phenotypicvariabilityin pages 7-8): Anna Kutkowska-Kaźmierczak, Katarzyna Niepokój, Katarzyna Wertheim-Tysarowska, Aleksandra Giza, Maria Mordasewicz-Goliszewska, Jerzy Bal, and Ewa Obersztyn. Phenotypic variability in gap junction syndromic skin disorders: experience from kid and clouston syndromes’ clinical diagnostics. Journal of Applied Genetics, 56:329-337, Jan 2015. URL: https://doi.org/10.1007/s13353-014-0266-1, doi:10.1007/s13353-014-0266-1. This article has 18 citations and is from a peer-reviewed journal.