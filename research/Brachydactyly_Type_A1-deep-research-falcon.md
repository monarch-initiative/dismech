---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:16:48.562759'
end_time: '2026-05-08T10:32:00.966624'
duration_seconds: 912.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Brachydactyly Type A1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brachydactyly Type A1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Brachydactyly Type A1** covering all of the
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
- **Disease Name:** Brachydactyly Type A1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Brachydactyly Type A1** covering all of the
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


# Disease Characteristics Research Report: Brachydactyly Type A1 (BDA1)

## Executive summary
Brachydactyly type A1 (BDA1) is a rare, typically autosomal-dominant, congenital digital malformation primarily characterized by hypoplasia/aplasia of the middle phalanges of digits 2–5, often with short proximal phalanges of the thumb and big toe and occasional symphalangism. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)
The best-established causal gene is **IHH** (Indian hedgehog), with pathogenic variants clustering in the N-terminal signaling fragment (classically codons ~95–154) and recurrent hotspots at residues such as E95, D100, and E131. (racacho2015thegeneticheterogeneity pages 72-76, zeng2022casereportbrachydactyly pages 1-2)
Recent case-level work (2024) underscores that some IHH-related families present with mild/non-classical BDA1 plus short stature and may be misclassified as idiopathic short stature; whole-exome sequencing (WES) can resolve diagnosis, and recombinant human growth hormone (rhGH) therapy improved height SDS in a small family case report. (chen2024shortstaturewith pages 1-2, chen2024shortstaturewith pages 2-4)

## 1. Disease information
### 1.1 Overview / definition
BDA1 is an **isolated brachydactyly** subtype in which shortening is mainly confined to the **middle phalanges**: “middle phalanges of all digits are variably short or rudimentary and are occasionally fused with terminal phalanges,” and “the proximal phalanges of the thumbs and big toes are short.” (temtamy2008brachydactyly pages 2-5)
Radiographically, classification relies on the selective pattern of middle phalanx hypoplasia/aplasia on standard postero-anterior (PA) hand radiographs. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)

### 1.2 Key identifiers
* **OMIM (phenotype):** 112500 (explicitly stated). (zeng2022casereportbrachydactyly pages 1-2)
* **Causal locus:** IHH at **2q35–36**; a second locus (“BDA1B”) maps to **5p13.3–p13.2**. (temtamy2008brachydactyly pages 2-5)
* **MONDO / Orphanet / ICD-10/ICD-11 / MeSH:** not directly retrievable from the provided tool evidence (evidence gap).

### 1.3 Synonyms / alternative names
* “Brachydactyly type A1”
* “Brachymesophalangy” (middle phalanx shortening)
* “Isolated brachydactyly type A1” (used in radiology/clinical genetics contexts) (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)

### 1.4 Evidence source type
The knowledge base content below integrates:
* Aggregated disease-level resources/reviews (e.g., Orphanet Journal of Rare Diseases review). (temtamy2008brachydactyly pages 2-5)
* Radiology review evidence for diagnostic imaging hallmarks. (david2015isolatedandsyndromic pages 1-3)
* Family case reports/series and molecular diagnostics/functional follow-up reports. (zeng2022casereportbrachydactyly pages 1-2, chen2024shortstaturewith pages 2-4, zhu2025anovelheterozygous pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors
BDA1 is a **Mendelian** congenital limb malformation primarily caused by **germline pathogenic variants** affecting endochondral ossification signaling pathways—most prominently **IHH**. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)

### 2.2 Risk factors
**Genetic risk factors (causal variants):**
* **IHH** heterozygous variants are the canonical cause; classic reviews identify IHH mutations at 2q35–36. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)
* Additional reported causal genes/loci include **GDF5** and **BMPR1B** in genetic synthesis work; these converge on BMP/TGF-β axis biology relevant to digit formation and can phenocopy/overlap BDA1. (racacho2015thegeneticheterogeneity pages 111-116, racacho2015thegeneticheterogeneity pages 98-102)

**Environmental risk factors:**
No environmental, infectious, or lifestyle risk factors are established in the retrieved evidence, consistent with a primary Mendelian etiology.

### 2.3 Protective factors / gene–environment interaction
No protective factors or gene–environment interactions were identified in the retrieved evidence.

## 3. Phenotypes
### 3.1 Core phenotypes and HPO suggestions
**Digital skeletal phenotypes**
* Middle phalanges of digits 2–5 are variably short/absent; can be fused to distal/terminal phalanges (symphalangism). (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)
* Thumb proximal phalanx and big toe proximal phalanx often short. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)
* Metacarpals can be short with broad epiphyses; distal phalanges may be short; digit 2 and 5 often most affected. (david2015isolatedandsyndromic pages 1-3)

**Suggested HPO terms (non-exhaustive)**
* Brachydactyly — **HP:0001156**
* Brachydactyly, type A1 — (HPO term exists in many installations; not verified in retrieved evidence)
* Symphalangism — **HP:0001204**
* Clinodactyly — **HP:0004209**
* Short stature (variable) — **HP:0004322** (lacombe2010brachydactylytypea1 pages 3-5, chen2024shortstaturewith pages 2-4)

### 3.2 Age of onset, severity, progression
* **Onset:** congenital (structural). (temtamy2008brachydactyly pages 2-5)
* **Course:** generally stable/non-progressive as a malformation; functional impact varies with severity. (temtamy2008brachydactyly pages 2-5)

### 3.3 Quality of life impact
No validated QoL instrument data (e.g., SF-36/EQ-5D) were found in the retrieved evidence. Functional limitation is typically the driver of intervention decisions. (temtamy2008brachydactyly pages 2-5)

## 4. Genetic / molecular information
### 4.1 Causal genes
**Primary causal gene:**
* **IHH** (Indian hedgehog). (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)

**Additional reported genes/loci (evidence in retrieved context but less canonical):**
* **GDF5**, **BMPR1B**, and a locus at **5p13.3–p13.2 (BDA1B)**. (temtamy2008brachydactyly pages 2-5, racacho2015thegeneticheterogeneity pages 111-116, racacho2015thegeneticheterogeneity pages 98-102)

### 4.2 Pathogenic variant spectrum and hotspots
A recurring theme is that BDA1-causing IHH variants cluster in the N-terminal signaling fragment. Genetic synthesis evidence states: “all of the BDA1-causing IHH mutations are missense and are limited to a 59 amino acid region… (codons 95–154).” (racacho2015thegeneticheterogeneity pages 72-76)
Hotspots/recurrent residues include codons/residues **E95**, **D100**, and **E131**, among others; case reports add in-frame indels and frameshift examples. (racacho2015thegeneticheterogeneity pages 72-76, zeng2022casereportbrachydactyly pages 1-2, chen2024shortstaturewith pages 2-4)
Examples in the retrieved evidence:
* **In-frame duplication:** IHH NM_002181.4 c.383_415dup, p.(R128_H138dup). (zeng2022casereportbrachydactyly pages 1-2)
* **Frameshift (short stature + non-classical BDA1):** IHH c.387_388insC, p.Thr130Hisfs*18. (chen2024shortstaturewith pages 1-2)
* **In-frame deletion (prenatal case; functional maturation defect):** IHH c.331_333delCTG, p.Leu111del. (zhu2025anovelheterozygous pages 1-2)

**Allele frequency:** population allele-frequency values (gnomAD/1000G) were not available in retrieved tool evidence (gap).

### 4.3 Functional consequences
A recent functional report highlights the importance of precursor processing and maturation: IHH is synthesized as a precursor and autocatalytically generates an active N-terminal signaling fragment; the p.Leu111del variant led to increased precursor with reduced mature functional IHH in HEK293T assays, consistent with “protein maturation failure.” (zhu2025anovelheterozygous pages 1-2)

## 5. Environmental information
No specific environmental/lifestyle/toxin/infectious contributors were identified in the retrieved evidence; the condition is primarily genetic.

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic understanding
IHH is central to growth plate biology and endochondral ossification. The 2024 case report explicitly summarizes that IHH “regulates proliferation and differentiation of chondrocytes and is essential for bone formation,” and “coordinates endochondral bone growth and morphogenesis via parathyroid hormone related-protein-dependent and -independent pathways,” referencing the **Ihh–PTHrP feedback loop**. (chen2024shortstaturewith pages 8-8)
Mechanistic chain (high-level):
1. **Upstream trigger:** germline pathogenic variant in IHH (or related pathway genes). (temtamy2008brachydactyly pages 2-5, zeng2022casereportbrachydactyly pages 1-2)
2. **Molecular dysfunction:** reduced functional IHH (maturation/secretion/binding defects) or altered hedgehog signaling output. (zhu2025anovelheterozygous pages 1-2)
3. **Cellular/tissue consequence:** disrupted chondrocyte proliferation/differentiation gradients and growth plate signaling, altering cartilage template growth for phalanges/metacarpals. (chen2024shortstaturewith pages 8-8)
4. **Clinical phenotype:** congenital shortening/aplasia of middle phalanges ± symphalangism and variable short stature. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)

### 6.2 Suggested GO / CL terms
* Endochondral ossification — **GO:0001958**
* Hedgehog signaling pathway — **GO:0007224**
* Chondrocyte differentiation — **GO:0002062**
* Chondrocyte (growth plate) — **CL:0000138**; hypertrophic chondrocyte — **CL:0000218**
(ontology suggestions derived from mechanism described in retrieved evidence) (chen2024shortstaturewith pages 8-8)

## 7. Anatomical structures affected
Primary structures:
* Middle phalanges (digits 2–5), thumb proximal phalanx, toe phalanges, and sometimes metacarpals/metatarsals. (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3)
Growth plate cartilage is the key tissue context. (chen2024shortstaturewith pages 8-8)

Suggested UBERON terms:
* Phalanx — **UBERON:0006002**
* Metacarpal bone — **UBERON:0011137**
* Metatarsal bone — **UBERON:0011138**
* Growth plate cartilage — **UBERON:0004367**

## 8. Temporal development
**Typical onset:** congenital. (temtamy2008brachydactyly pages 2-5)
**Critical periods:** embryonic and postnatal growth plate development (implied by IHH growth plate function). (chen2024shortstaturewith pages 8-8)
**Progression:** not a progressive systemic disorder; skeletal proportions are established developmentally and remain stable, though secondary issues (e.g., arthritis) have been reported in some families. (racacho2015thegeneticheterogeneity pages 72-76)

## 9. Inheritance and population
### 9.1 Inheritance pattern
Classic descriptions indicate autosomal dominant inheritance (“denoting autosomal dominant inheritance”). (temtamy2008brachydactyly pages 2-5)

### 9.2 Penetrance and expressivity
Marked **phenotypic heterogeneity** and variable expressivity across families is documented; one synthesis notes “remarkable phenotypic heterogeneity.” (racacho2015thegeneticheterogeneity pages 72-76)

### 9.3 Epidemiology
A key knowledge-base limitation is the lack of formal epidemiology: “No epidemiological studies have been reported. It is a rare hand malformation with only few pedigrees reported.” (temtamy2008brachydactyly pages 2-5)

## 10. Diagnostics
### 10.1 Clinical and imaging tests
Diagnosis relies on **clinical exam + anthropometry + radiographs**; “X-ray of hands on postero-anterior (PA) view show the selective distribution of the hypoplasia and aplasia of the middle phalanges.” (temtamy2008brachydactyly pages 2-5)
A radiology review emphasizes that standard PA radiographs are first-line to classify subtype and localize shortening, and that BDA1 shows short/absent middle phalanges with occasional fusion and often short metacarpals with broad epiphyses. (david2015isolatedandsyndromic pages 1-3)

### 10.2 Genetic testing (real-world implementations)
Modern implementation is WES in families with mild skeletal signs and short stature:
* In a 2024 family with short stature and non-classical BDA1, WES identified a heterozygous IHH frameshift (c.387_388insC; p.Thr130Hisfs*18) with Sanger confirmation. (chen2024shortstaturewith pages 2-4)
Similarly, case reports identify novel in-frame IHH insertions in multi-generation pedigrees. (zeng2022casereportbrachydactyly pages 1-2)

### 10.3 Differential diagnosis
Differentials reported in a 2022 case report include **Robinow syndrome**, **Feingold syndrome**, and **Temtamy preaxial brachydactyly syndrome**, reflecting the need to distinguish isolated BDA1 from syndromic brachydactylies. (zeng2022casereportbrachydactyly pages 1-2)

## 11. Outcome / prognosis
BDA1 is generally compatible with normal life expectancy; morbidity is primarily functional/cosmetic. Surgical intervention is typically reserved for function/cosmesis. (temtamy2008brachydactyly pages 2-5)
No quantitative mortality/survival statistics were found in the retrieved evidence (gap).

## 12. Treatment
### 12.1 Standard management
A commonly cited management approach is conservative:
* “Plastic surgery is only indicated if the brachydactyly affects hand function or for cosmetic reasons… Physical therapy and ergotherapy may ameliorate hand function.” (temtamy2008brachydactyly pages 2-5)
A 2022 case report similarly notes most patients are treated only if function is affected or for cosmetic reasons. (zeng2022casereportbrachydactyly pages 1-2)

**Suggested MAXO terms:**
* Surgical procedure — MAXO:0000004
* Physical therapy — MAXO:0000011
* Occupational therapy — MAXO:0000014

### 12.2 Recent developments (2023–2024 priority)
**rhGH in selected IHH-related short stature presentations:**
A 2024 report treated two siblings with rhGH (33 μg/kg/day) for 4 years, observing height SDS changes of **+2.54** (boy) and **+1.86** (girl), with “No noticeable adverse effect.” (chen2024shortstaturewith pages 1-2)
Interpretation: this is not a corrective therapy for brachydactyly per se, but a real-world implementation relevant when BDA1 co-occurs with clinically significant short stature and growth hormone axis abnormalities. (chen2024shortstaturewith pages 2-4)

### 12.3 Experimental / targeted therapies
No BDA1-specific interventional clinical trials were retrieved; however, mechanistic literature referenced in a 2024 report notes Smoothened agonist (SAG) rescue in Ihh-deficiency models, suggesting pathway-modulation concepts in broader skeletal dysplasia research. (chen2024shortstaturewith pages 8-8)

## 13. Prevention
No primary prevention is applicable for this Mendelian condition. Prevention focuses on **genetic counseling**, cascade testing, and reproductive options when a familial variant is known. (temtamy2008brachydactyly pages 2-5)
Prenatal phenotyping with ultrasound plus WES has been used in recent fetal IHH-related BDA1 diagnosis. (zhu2025anovelheterozygous pages 1-2)

**Suggested MAXO terms:** Genetic counseling — MAXO:0000055.

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

## 15. Model organisms
Evidence supporting pathway relevance includes:
* **Bmpr1b-null mice** exhibit phalange-restricted brachydactyly, supporting the role of BMP receptor biology in digit development. (racacho2015thegeneticheterogeneity pages 111-116)
* Growth-plate models of Ihh deficiency and pharmacologic manipulation (e.g., SAG) are referenced in recent clinical mechanistic summaries. (chen2024shortstaturewith pages 8-8)
Limitations: these models are not necessarily allele-matched to the common human BDA1 IHH hotspot variants.

## Visual evidence
A schematic classification figure including a BDA1 panel is available in the Temtamy & Aglan review. (temtamy2008brachydactyly media a1b197b0)

## Data/statistics extracted from recent studies (2023–2024 priority)
* **Height SDS gain with 4 years rhGH** in an IHH-related short stature + non-classical BDA1 family: **+2.54** (boy) and **+1.86** (girl) at rhGH 33 μg/kg/day, no noticeable adverse effects (case report-level evidence). (chen2024shortstaturewith pages 1-2)
* **Epidemiology:** “No epidemiological studies have been reported” for BDA1; rare with few pedigrees (evidence gap for prevalence/incidence). (temtamy2008brachydactyly pages 2-5)

---

## Knowledge-base summary table
| Domain | Key knowledge-base fields | Suggested ontology terms | Supporting citation IDs |
|---|---|---|---|
| Disease identifiers / names | **Disease:** Brachydactyly type A1 (BDA1); isolated brachydactyly / brachymesophalangy predominantly affecting middle phalanges; **OMIM:** 112500; historic alternate locus **BDA1B** at 5p13.3-p13.2; information here is derived from aggregated disease-level literature/reviews plus family case reports and case series. | Suggested MONDO: *Brachydactyly type A1* (MONDO not confirmed in retrieved evidence); MeSH/ICD/Orphanet identifiers not directly confirmed in retrieved context. | (temtamy2008brachydactyly pages 2-5, zeng2022casereportbrachydactyly pages 1-2, racacho2015thegeneticheterogeneity pages 84-88) |
| Inheritance / population genetics | Usually **autosomal dominant** with generally high/complete penetrance reported in classic descriptions; marked **variable expressivity** between and within families; rare evidence for **semi-dominant** behavior in some **GDF5**-related BDA1 presentations (milder heterozygotes, more severe homozygotes). Founder and recurrent hotspot mutations have been described for some **IHH** alleles. | HP: Autosomal dominant inheritance **HP:0000006**; Variable expressivity **HP:0003828**. | (temtamy2008brachydactyly pages 2-5, racacho2015thegeneticheterogeneity pages 84-88, racacho2015thegeneticheterogeneity pages 72-76, racacho2015thegeneticheterogeneity pages 98-102) |
| Core phenotypes | Congenital shortening/aplasia of **middle phalanges of digits 2-5**, often most severe in digits 2 and 5; short proximal phalanx of thumb and sometimes hallux; occasional fusion of middle and terminal phalanges (**symphalangism**); short/broad metacarpals; short toes; clinodactyly; absent distal finger creases; variable short stature and mild limb shortening in some families. | HP: Brachydactyly **HP:0001156**; Aplasia/Hypoplasia of middle phalanges of the hand **HP:0009843/HP:0009882**; Short thumb **HP:0009778**; Toe brachydactyly **HP:0001773**; Symphalangism **HP:0001204**; Clinodactyly **HP:0004209**; Short stature **HP:0004322**. | (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3, lacombe2010brachydactylytypea1 pages 3-5, zeng2022casereportbrachydactyly pages 1-2, chen2024shortstaturewith pages 2-4) |
| Radiographic hallmarks | Postero-anterior hand radiographs show selective hypoplasia/aplasia of middle phalanges; short or absent middle phalanges, occasional fusion with distal phalanges, short distal phalanges, short metacarpals with broad epiphyses; “chess pawn-shaped” distal bone described in classic BDA1; hand X-rays are central to subtype classification. | HP: Abnormality of hand bone morphology **HP:0011304**; Short middle phalanx of the 2nd finger **HP:0009871**; Short middle phalanx of the 5th finger **HP:0009175**. | (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3, racacho2015thegeneticheterogeneity pages 72-76, zhu2025anovelheterozygous pages 10-11, temtamy2008brachydactyly media a1b197b0) |
| Causal genes / loci | **Primary causal gene:** **IHH** (Indian hedgehog signaling molecule); additional reported BDA1 genes/loci include **GDF5**, **BMPR1B**, and a mapped locus at **5p13.3-p13.2**. **IHH** explains a substantial fraction of molecularly solved cases (~40% cited in review-level evidence). | HGNC: **IHH**, **GDF5**, **BMPR1B**. | (racacho2015thegeneticheterogeneity pages 84-88, racacho2015thegeneticheterogeneity pages 111-116, racacho2015thegeneticheterogeneity pages 98-102, temtamy2008brachydactyly pages 2-5) |
| Pathogenic variants / hotspots | **IHH** BDA1 variants cluster in the N-terminal active/signaling fragment, especially codons **95-154**; recurrent/hotspot residues include **E95** (e.g., p.Glu95del / p.Glu95Lys), **D100** (p.Asp100Asn/Glu), **L111del**, **R128_H138dup**, **Thr130Hisfs*18**, **E131K**. Variant classes include mostly **missense**, plus **in-frame insertion/deletion** and rare **frameshift** changes. **GDF5** BDA1 variants include cysteine-disrupting missense alleles affecting the mature domain; **BMPR1B** missense/splice variants also reported. Germline origin is implied/observed. | Sequence Ontology suggestions: missense_variant, inframe_insertion, inframe_deletion, frameshift_variant, splice_acceptor_variant. | (racacho2015thegeneticheterogeneity pages 72-76, zeng2022casereportbrachydactyly pages 1-2, chen2024shortstaturewith pages 2-4, zhu2025anovelheterozygous pages 1-2, zhu2025anovelheterozygous pages 10-11, racacho2015thegeneticheterogeneity pages 111-116, racacho2015thegeneticheterogeneity pages 98-102) |
| Mechanism / pathways | Disease reflects disturbed **endochondral ossification** and growth-plate signaling. **IHH** normally regulates chondrocyte proliferation/differentiation and couples chondrogenesis to osteogenesis through **IHH–PTCH1–SMO–GLI** signaling and the **IHH–PTHrP feedback loop**. BDA1-associated variants can reduce mature functional IHH, impair **IHH-PTC/PTCH** binding, alter secretion/maturation, and downstream perturb digit cartilage template growth. BDA1 genes converge on **BMP-SMAD / GDF5-BMPR1B** signaling interacting with IHH-PTHrP biology. | GO: endochondral ossification **GO:0001958**; chondrocyte differentiation **GO:0002062**; regulation of chondrocyte differentiation **GO:0032330**; hedgehog signaling pathway **GO:0007224**; ossification **GO:0001503**. Key nodes: **IHH, PTCH1, SMO, GLI1/2/3, PTHLH/PTHrP, PTH1R, GDF5, BMPR1B, SMADs**. | (chen2024shortstaturewith pages 8-8, zhu2025anovelheterozygous pages 1-2, racacho2015thegeneticheterogeneity pages 84-88, racacho2015thegeneticheterogeneity pages 111-116, racacho2015thegeneticheterogeneity pages 98-102, alqattan2014embryologyoffamilial pages 3-7) |
| Anatomy / cell types | Primarily affects **phalanges, metacarpals, metatarsals**, and growth-plate cartilage of hands/feet; in some families also short humerus/femur or ulna-related changes. Key cell type is the **growth plate chondrocyte**. | UBERON: phalanx **UBERON:0006002**; metacarpal bone **UBERON:0011137**; metatarsal bone **UBERON:0011138**; growth plate cartilage **UBERON:0004367**. CL: chondrocyte **CL:0000138**; hypertrophic chondrocyte **CL:0000218**. | (lacombe2010brachydactylytypea1 pages 3-5, david2015isolatedandsyndromic pages 1-3, chen2024shortstaturewith pages 8-8) |
| Onset / course / prognosis | Typically **congenital** and usually **non-progressive/stable** as a structural limb malformation; lifelong but generally compatible with normal lifespan. Functional impact is often mild, though dexterity/cosmetic concerns and short stature may prompt evaluation. Osteoarthritis/arthritis has occasionally been reported in some families. | HP: Congenital onset **HP:0003577**; Abnormal hand morphology **HP:0005922**. | (temtamy2008brachydactyly pages 2-5, racacho2015thegeneticheterogeneity pages 72-76, zeng2022casereportbrachydactyly pages 1-2) |
| Epidemiology | No robust prevalence/incidence estimates for **BDA1** were identified in the retrieved evidence. Reviews state brachydactylies are rare overall and specifically note that **BDA1** is a rare hand malformation with only a few pedigrees/case series reported; prevalence figures around ~2% apply to types **A3** and **D**, not A1. | Rare disease designation appropriate; no disease-specific frequency ontology assignment supported by retrieved evidence. | (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3, zeng2022casereportbrachydactyly pages 1-2) |
| Diagnostics | Diagnosis is primarily **clinical + radiographic** (PA hand/foot X-rays), followed by **molecular confirmation**. Current real-world testing uses **WES** with Sanger confirmation; targeted skeletal dysplasia / short stature / brachydactyly panels are reasonable when phenotype is suggestive. Differential diagnosis includes other isolated brachydactylies and syndromic entities such as **Robinow syndrome**, **Feingold syndrome**, and Temtamy preaxial brachydactyly syndrome; radiographs help subtype classification. | MAXO not applicable here; HPO terms above support phenotyping. Testing methods: WES, Sanger sequencing, multigene panel. | (temtamy2008brachydactyly pages 2-5, david2015isolatedandsyndromic pages 1-3, zeng2022casereportbrachydactyly pages 1-2, chen2024shortstaturewith pages 2-4, chen2024shortstaturewith pages 1-2) |
| Management / treatment | No disease-modifying therapy established for classic isolated BDA1. Management is usually **conservative**, with **plastic/orthopedic surgery** only if hand function or cosmesis is significantly affected; **physical therapy/ergotherapy (occupational therapy)** may improve function. In recent IHH-related short stature families, **recombinant human growth hormone (rhGH)** produced substantial height SDS gains over 4 years without major adverse effects, but evidence is limited to case-level reports and applies mainly to selected short-stature presentations rather than hand malformation correction. | MAXO: physical therapy **MAXO:0000011**; occupational therapy **MAXO:0000014**; surgical procedure **MAXO:0000004**; growth hormone therapy **MAXO:0010020**. | (temtamy2008brachydactyly pages 2-5, zeng2022casereportbrachydactyly pages 1-2, chen2024shortstaturewith pages 2-4, chen2024shortstaturewith pages 1-2, chen2024shortstaturewith pages 8-8) |
| Prevention / counseling | No primary environmental prevention known for this Mendelian malformation. Key preventive actions are **genetic counseling**, family segregation testing, and consideration of **prenatal/preimplantation testing** when a familial pathogenic variant is known. | MAXO: genetic counseling **MAXO:0000055**; cascade genetic testing **MAXO:0000127**. | (temtamy2008brachydactyly pages 2-5, chen2024shortstaturewith pages 2-4, chen2024shortstaturewith pages 1-2) |
| Model organism / comparative evidence | Mouse and developmental studies support pathway relevance: **Bmpr1b-null mice** show phalange-restricted brachydactyly; broader skeletal biology literature shows **Ihh** is essential for growth-plate homeostasis and chondrocyte hypertrophy/differentiation. Model evidence is mechanistically strong but does not perfectly recapitulate the full human BDA1 hand phenotype for every allele. | GO as above; model organism: *Mus musculus*. | (racacho2015thegeneticheterogeneity pages 111-116, chen2024shortstaturewith pages 8-8) |


*Table: This table condenses the main disease-knowledge fields for brachydactyly type A1, including phenotype, genetics, mechanism, diagnosis, and management. It is designed for rapid knowledge-base population and each row links to supporting evidence context IDs.*

---

## Key references (with URLs and publication dates)
* Temtamy SA, Aglan MS. **Brachydactyly.** Orphanet Journal of Rare Diseases. **2008-06**. https://doi.org/10.1186/1750-1172-3-15 (temtamy2008brachydactyly pages 2-5)
* David A, et al. **Isolated and syndromic brachydactylies: Diagnostic value of hand X-rays.** Diagnostic and Interventional Imaging. **2015-05**. https://doi.org/10.1016/j.diii.2014.12.007 (david2015isolatedandsyndromic pages 1-3)
* Zeng F, et al. **Case Report: Brachydactyly Type A1 Induced by a Novel Variant of in-Frame Insertion in the IHH Gene.** Frontiers in Genetics. **2022-05**. https://doi.org/10.3389/fgene.2022.814786 (zeng2022casereportbrachydactyly pages 1-2)
* Chen Y, et al. **Short stature with brachydactyly caused by a novel mutation in the IHH gene and response to 4-year growth hormone therapy: a case report.** Translational Pediatrics. **2024-05**. https://doi.org/10.21037/tp-23-578 (chen2024shortstaturewith pages 1-2)
* Zhu T, et al. **A Novel Heterozygous IHH c.331_333del Mutation… Causes IHH Protein Maturation Failure in HEK293T Cells.** Phenomics. **2025-12**. https://doi.org/10.1007/s43657-024-00191-9 (zhu2025anovelheterozygous pages 1-2)

## Notes on evidence gaps
Within the retrieved tool evidence, the following could not be confirmed and should be filled by targeted database queries (OMIM/Orphanet/MONDO/MeSH/GTR/ClinVar/gnomAD) in a subsequent pass: MONDO ID; Orphanet ORPHA code; ICD-10/ICD-11 codes; MeSH descriptor; ClinVar variant classifications and population allele frequencies; and validated QoL statistics.


References

1. (temtamy2008brachydactyly pages 2-5): Samia A Temtamy and Mona S Aglan. Brachydactyly. Orphanet Journal of Rare Diseases, Jun 2008. URL: https://doi.org/10.1186/1750-1172-3-15, doi:10.1186/1750-1172-3-15. This article has 223 citations and is from a peer-reviewed journal.

2. (david2015isolatedandsyndromic pages 1-3): A. David, M. Vincent, M.-P. Quéré, T. Lefrançois, E. Frampas, and A. David. Isolated and syndromic brachydactylies: diagnostic value of hand x-rays. Diagnostic and interventional imaging, 96 5:443-8, May 2015. URL: https://doi.org/10.1016/j.diii.2014.12.007, doi:10.1016/j.diii.2014.12.007. This article has 27 citations and is from a peer-reviewed journal.

3. (racacho2015thegeneticheterogeneity pages 72-76): Lemuel Jean Racacho. The genetic heterogeneity of brachydactyly type a1: identifying the molecular pathways. ArXiv, Mar 2015. URL: https://doi.org/10.20381/ruor-2868, doi:10.20381/ruor-2868. This article has 0 citations.

4. (zeng2022casereportbrachydactyly pages 1-2): Feier Zeng, Huan Liu, Xuyang Xia, Yang Shu, Wei Cheng, Heng Xu, Geng Yin, and Qibing Xie. Case report: brachydactyly type a1 induced by a novel variant of in-frame insertion in the ihh gene. Frontiers in Genetics, May 2022. URL: https://doi.org/10.3389/fgene.2022.814786, doi:10.3389/fgene.2022.814786. This article has 3 citations and is from a peer-reviewed journal.

5. (chen2024shortstaturewith pages 1-2): Yulin Chen, Mingyue Yin, Yiyi Lu, Zhiya Dong, Wenli Lu, Lin Lin, and Yuan Xiao. Short stature with brachydactyly caused by a novel mutation in the ihh gene and response to 4-year growth hormone therapy: a case report. Translational Pediatrics, 13:856-863, May 2024. URL: https://doi.org/10.21037/tp-23-578, doi:10.21037/tp-23-578. This article has 3 citations and is from a peer-reviewed journal.

6. (chen2024shortstaturewith pages 2-4): Yulin Chen, Mingyue Yin, Yiyi Lu, Zhiya Dong, Wenli Lu, Lin Lin, and Yuan Xiao. Short stature with brachydactyly caused by a novel mutation in the ihh gene and response to 4-year growth hormone therapy: a case report. Translational Pediatrics, 13:856-863, May 2024. URL: https://doi.org/10.21037/tp-23-578, doi:10.21037/tp-23-578. This article has 3 citations and is from a peer-reviewed journal.

7. (zhu2025anovelheterozygous pages 1-2): Ting Zhu, Lijie Guan, Dan Chen, Yi Luo, Mianmian Zhu, Rongyue Sun, Jiamin Shi, Qiu Wang, Yuan Chen, Yihong Wang, Hongwei Wang, Zhongqiu Lu, and Dan Wang. A novel heterozygous ihh c.331_333del mutation identified in a fetus with brachydactyly type a1 causes ihh protein maturation failure in hek293t cells. Phenomics, 5:123-136, Dec 2025. URL: https://doi.org/10.1007/s43657-024-00191-9, doi:10.1007/s43657-024-00191-9. This article has 1 citations.

8. (racacho2015thegeneticheterogeneity pages 111-116): Lemuel Jean Racacho. The genetic heterogeneity of brachydactyly type a1: identifying the molecular pathways. ArXiv, Mar 2015. URL: https://doi.org/10.20381/ruor-2868, doi:10.20381/ruor-2868. This article has 0 citations.

9. (racacho2015thegeneticheterogeneity pages 98-102): Lemuel Jean Racacho. The genetic heterogeneity of brachydactyly type a1: identifying the molecular pathways. ArXiv, Mar 2015. URL: https://doi.org/10.20381/ruor-2868, doi:10.20381/ruor-2868. This article has 0 citations.

10. (lacombe2010brachydactylytypea1 pages 3-5): Didier Lacombe, Marie‐Ange Delrue, Caroline Rooryck, Fanny Morice‐Picard, Benoît Arveiler, Brigitte Maugey‐Laulom, Stefan Mundlos, Annick Toutain, and Jean‐François Chateil. Brachydactyly type a1 with short humerus and associated skeletal features. American Journal of Medical Genetics Part A, 152A:3016-3021, Dec 2010. URL: https://doi.org/10.1002/ajmg.a.33761, doi:10.1002/ajmg.a.33761. This article has 4 citations.

11. (chen2024shortstaturewith pages 8-8): Yulin Chen, Mingyue Yin, Yiyi Lu, Zhiya Dong, Wenli Lu, Lin Lin, and Yuan Xiao. Short stature with brachydactyly caused by a novel mutation in the ihh gene and response to 4-year growth hormone therapy: a case report. Translational Pediatrics, 13:856-863, May 2024. URL: https://doi.org/10.21037/tp-23-578, doi:10.21037/tp-23-578. This article has 3 citations and is from a peer-reviewed journal.

12. (temtamy2008brachydactyly media a1b197b0): Samia A Temtamy and Mona S Aglan. Brachydactyly. Orphanet Journal of Rare Diseases, Jun 2008. URL: https://doi.org/10.1186/1750-1172-3-15, doi:10.1186/1750-1172-3-15. This article has 223 citations and is from a peer-reviewed journal.

13. (racacho2015thegeneticheterogeneity pages 84-88): Lemuel Jean Racacho. The genetic heterogeneity of brachydactyly type a1: identifying the molecular pathways. ArXiv, Mar 2015. URL: https://doi.org/10.20381/ruor-2868, doi:10.20381/ruor-2868. This article has 0 citations.

14. (zhu2025anovelheterozygous pages 10-11): Ting Zhu, Lijie Guan, Dan Chen, Yi Luo, Mianmian Zhu, Rongyue Sun, Jiamin Shi, Qiu Wang, Yuan Chen, Yihong Wang, Hongwei Wang, Zhongqiu Lu, and Dan Wang. A novel heterozygous ihh c.331_333del mutation identified in a fetus with brachydactyly type a1 causes ihh protein maturation failure in hek293t cells. Phenomics, 5:123-136, Dec 2025. URL: https://doi.org/10.1007/s43657-024-00191-9, doi:10.1007/s43657-024-00191-9. This article has 1 citations.

15. (alqattan2014embryologyoffamilial pages 3-7): M. M. Al-Qattan. Embryology of familial (non-syndromic) brachydactyly of the hand. Journal of Hand Surgery (European Volume), 39:926-933, Nov 2014. URL: https://doi.org/10.1177/1753193413514363, doi:10.1177/1753193413514363. This article has 12 citations.
