---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-22T22:14:02.290259'
end_time: '2026-04-22T22:30:33.904504'
duration_seconds: 991.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Atypical Hemolytic Uremic Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Atypical Hemolytic Uremic Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Atypical Hemolytic Uremic Syndrome** covering all of the
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
- **Disease Name:** Atypical Hemolytic Uremic Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Atypical Hemolytic Uremic Syndrome** covering all of the
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


## Comprehensive Disease Characteristics Report: Atypical Hemolytic Uremic Syndrome (aHUS)

**Target disease:** Atypical hemolytic uremic syndrome (aHUS) (also increasingly referred to as *complement-mediated thrombotic microangiopathy* (CM-TMA) or *complement-mediated HUS* in recent expert nomenclature). (musalem2025tentipsfor pages 1-2)

**Disease category:** Mendelian (incompletely penetrant genetic predisposition; “multi-hit”/trigger-dependent). (cole2025updateinthe pages 1-3, bogdan2025atypicalhemolyticuremic pages 2-4)

### Key identifiers (available from retrieved sources)
- **MONDO:** **MONDO_0016244** (“atypical hemolytic-uremic syndrome”) from Open Targets disease mapping (URL: https://platform.opentargets.org/disease/MONDO_0016244/associations; accessed via Open Targets integration in this run). (dixon2024ravulizumabinatypical pages 1-2)
- **MeSH Unique ID:** **D065766** (“Atypical Hemolytic Uremic Syndrome”) as recorded in ClinicalTrials.gov registry metadata. (NCT01522183 chunk 5, NCT04861259 chunk 3)
- **Other identifiers (OMIM / Orphanet / ICD-10 / ICD-11):** Not explicitly retrievable from the provided full-text excerpts in this run; therefore not asserted here.

### Common synonyms / alternative names
- “Atypical hemolytic uremic syndrome” (aHUS). (java2024atypicalhemolyticuremic pages 1-2)
- “Complement-mediated thrombotic microangiopathy” (CM-TMA) / “complement-mediated TMA.” (musalem2025tentipsfor pages 1-2, java2024atypicalhemolyticuremic pages 1-2)
- “Complement-mediated thrombotic microangiopathy/atypical hemolytic uremic syndrome” (used synonymously in diagnostic update literature). (cole2025updateinthe pages 1-3, cole2025updateinthe pages 12-12)

### Evidence provenance note
The evidence below is derived from **aggregated disease-level resources** (reviews/consensus statements), **clinical trials**, **registry analyses**, and **systematic reviews/meta-analyses**, rather than EHR-only single-center phenotyping. (musalem2025tentipsfor pages 1-2, dixon2024ravulizumabinatypical pages 1-2, meena2025kidneyandpregnancy pages 1-2, yan2020epidemiologyofatypical pages 3-5)


## 1. Disease Information (concise overview; current understanding)
Atypical hemolytic uremic syndrome is a **complement-mediated thrombotic microangiopathy (TMA)** characterized clinically by the triad of **microangiopathic hemolytic anemia (MAHA), thrombocytopenia, and end-organ injury**—most often **acute kidney injury**. (java2024atypicalhemolyticuremic pages 1-2, dixon2024ravulizumabinatypical pages 1-2)

Recent clinical reviews emphasize that aHUS is “a prototypical complement-mediated thrombotic microangiopathy (TMA)” and that it occurs due to endothelial injury from **overactivation of the alternative complement pathway**, driven by either **genetic variants** or **acquired autoantibodies**. (java2024atypicalhemolyticuremic pages 1-2)

**Direct abstract quote (definition/etiology):**
- Java (Dec 2024, Hematology): “**aHUS occurs due to endothelial injury resulting from overactivation of the alternative pathway of the complement system. The etiology… is either a genetic mutation… or an acquired deficiency due to autoantibodies.**” (java2024atypicalhemolyticuremic pages 1-2)


## 2. Etiology
### 2.1 Disease causal factors
**Primary mechanism:** Dysregulated activation of the **alternative complement pathway**, often conceptualized as impaired regulation of the complement amplification loop (loss-of-function in regulators) or gain-of-function in activators. (java2024atypicalhemolyticuremic pages 1-2, musalem2025tentipsfor pages 1-2)

**Genetic vs acquired causes:**
- Genetic predisposition via variants in complement genes (examples: CFH, CFI, CD46/MCP, C3, CFB, THBD) and complement-related loci (e.g., CFHR rearrangements). (maria2025recommendationsfordiagnosis pages 5-7, java2024atypicalhemolyticuremic pages 1-2)
- Acquired predisposition via autoantibodies, especially anti–factor H (anti-FH / anti-CFH) antibodies (often linked to CFHR1–CFHR3 deletions). (java2024atypicalhemolyticuremic pages 1-2, maria2025recommendationsfordiagnosis pages 7-10)

### 2.2 Risk factors (genetic; triggers as “environmental/clinical exposures”)
**Multi-hit model / triggers:** Multiple expert sources describe a “double-hit” or “multi-hit” model in which a genetic or acquired complement-control defect often requires a precipitating trigger (e.g., infection, pregnancy, surgery, autoimmune disease, transplantation, certain drugs) to manifest clinically. (cole2025updateinthe pages 1-3, bogdan2025atypicalhemolyticuremic pages 2-4, java2024atypicalhemolyticuremic pages 1-2)

**Examples of triggers (from recent review/consensus):** infections, pregnancy-related complications, malignancy, autoimmune diseases, surgery, transplantation, and other secondary TMA contexts. (musalem2025tentipsfor pages 1-2, cole2025updateinthe pages 1-3)

### 2.3 Protective factors
No explicit genetic or environmental protective factors were identified in the retrieved evidence excerpts. (Not available in this run.)

### 2.4 Gene–environment interaction
The “multi-hit” framing implies gene–environment/clinical interactions: genetically predisposed individuals may remain asymptomatic until an external trigger (infection/pregnancy/surgery/etc.) provokes complement-mediated endothelial injury and TMA. (java2024atypicalhemolyticuremic pages 1-2, bogdan2025atypicalhemolyticuremic pages 2-4)


## 3. Phenotypes (clinical, laboratory, QoL)
### 3.1 Core phenotype (TMA triad)
- **MAHA:** anemia with hemolysis markers (elevated LDH, low haptoglobin, schistocytes; Coombs-negative). (maria2025recommendationsfordiagnosis pages 5-7, bogdan2025atypicalhemolyticuremic pages 7-9)
- **Thrombocytopenia.** (java2024atypicalhemolyticuremic pages 1-2, dixon2024ravulizumabinatypical pages 1-2)
- **Organ injury:** most commonly kidney (acute kidney injury, reduced eGFR, creatinine rise), but can be multi-organ. (dixon2024ravulizumabinatypical pages 1-2, bogdan2025atypicalhemolyticuremic pages 5-7)

### 3.2 Renal phenotype (primary)
Renal involvement is emphasized as predominant: “acute kidney injury is almost always seen,” and may be severe, including dialysis dependence; some presentations can be kidney-limited TMA detectable only by biopsy (with minimal hematologic manifestations). (java2024atypicalhemolyticuremic pages 1-2)

Quantitative renal outcome statements reported in a recent review excerpt include **AKI in 60–70%** and **up to 50% progressing to ESKD**, with frequent dialysis/RRT requirement. (bogdan2025atypicalhemolyticuremic pages 4-5)

### 3.3 Extrarenal manifestations (selected; with frequencies where available)
Evidence supports a broad extrarenal spectrum including neurologic, cardiac, GI, pulmonary, dermatologic, and ocular involvement. (bogdan2025atypicalhemolyticuremic pages 5-7)

- **Neurologic involvement:** reported **8–48%** with a registry estimate **27.2%**; manifestations include seizures, encephalopathy/altered consciousness, hemiparesis, and visual impairment. (bogdan2025atypicalhemolyticuremic pages 5-7)
- **Cardiac involvement:** in one review excerpt, cardiovascular involvement reported up to **43% in pediatric** and **3–10% in adults**; includes cardiomyopathy, intracardiac thrombi, and other dysfunction. (bogdan2025atypicalhemolyticuremic pages 4-5)
- **Pulmonary:** respiratory failure requiring mechanical ventilation reported up to **21% in pediatric patients**, often secondary to pulmonary edema/fluid overload/cardiac dysfunction. (bogdan2025atypicalhemolyticuremic pages 5-7)
- **Ocular:** ocular involvement reported ~**4%**, potentially with acute vision loss. (bogdan2025atypicalhemolyticuremic pages 5-7)
- **Gastrointestinal:** diarrhea reported ~**50%** overall and **>80%** in anti–factor H antibody-associated aHUS; severe complications can include pancreatitis, GI bleeding, and intestinal perforation. (bogdan2025atypicalhemolyticuremic pages 5-7)

### 3.4 Quality of life (QoL) impact
- aHUS can cause significant functional impairment; Java’s clinical case vignette describes “severe ongoing fatigue requiring assistance with activities of daily living” and inability to work during recovery. (java2024atypicalhemolyticuremic pages 1-2)
- In ravulizumab trials, fatigue improvement (FACIT-F) achieved by 26 weeks was maintained through 2 years. (dixon2024ravulizumabinatypical pages 1-2)

### 3.5 Suggested HPO terms (examples; not exhaustive)
(These are ontology mappings proposed for knowledge-base structuring; they are not asserted to be provided verbatim by the cited papers.)
- **Hematologic/TMA:** Schistocytosis; Hemolytic anemia; Thrombocytopenia. (maria2025recommendationsfordiagnosis pages 5-7, bogdan2025atypicalhemolyticuremic pages 7-9)
- **Renal:** Acute kidney injury; Proteinuria; Hematuria; Hypertension; End-stage renal disease; Dialysis-dependent renal failure. (bogdan2025atypicalhemolyticuremic pages 7-9, bogdan2025atypicalhemolyticuremic pages 4-5)
- **Neurologic:** Seizures; Encephalopathy; Stroke; Altered consciousness. (java2024atypicalhemolyticuremic pages 1-2, bogdan2025atypicalhemolyticuremic pages 5-7)
- **Cardiac:** Cardiomyopathy; Myocardial infarction; Intracardiac thrombosis. (bogdan2025atypicalhemolyticuremic pages 4-5, java2024atypicalhemolyticuremic pages 1-2)
- **GI:** Diarrhea; Pancreatitis; Gastrointestinal hemorrhage. (bogdan2025atypicalhemolyticuremic pages 5-7)
- **Dermatologic/vascular:** Digital gangrene. (java2024atypicalhemolyticuremic pages 1-2)


## 4. Genetic / Molecular Information
### 4.1 Causal genes (core set supported in retrieved evidence)
Commonly evaluated genes include **CFH, CFI, CD46 (MCP), C3, CFB, CFHR genes (copy-number changes/rearrangements), CFH-CFHR hybrid genes, DGKE, THBD**. (maria2025recommendationsfordiagnosis pages 5-7, java2024atypicalhemolyticuremic pages 1-2)

**Quantitative genetic architecture:**
- “Approximately 60–70% of patients with aHUS have identifiable genetic or acquired abnormalities in complement-regulating components,” and genetic mutations are detected in ~60% in one review. (bogdan2025atypicalhemolyticuremic pages 2-4)
- VUS findings are common: “In approximately 30% to 40%… a genetic variant of uncertain significance (VUS) may be identified.” (java2024atypicalhemolyticuremic pages 1-2)

### 4.2 Variant types / functional consequences (high-level)
- Loss-of-function in complement regulators (e.g., CFH/CFI/CD46) and gain-of-function in activators (e.g., C3/CFB) are emphasized as etiologic themes. (musalem2025tentipsfor pages 1-2)

### 4.3 Gene-level frequency estimates (from review excerpts)
- **CFH:** ~20–30% (and in one table range up to ~20–45%). (bogdan2025atypicalhemolyticuremic pages 2-4)
- **CFI:** ~5–10%. (bogdan2025atypicalhemolyticuremic pages 4-5, bogdan2025atypicalhemolyticuremic pages 2-4)
- **C3:** ~2–10%. (bogdan2025atypicalhemolyticuremic pages 2-4)
- **THBD:** ~3–5%. (bogdan2025atypicalhemolyticuremic pages 4-5)
- **CFB:** rare (<1% in one excerpt). (bogdan2025atypicalhemolyticuremic pages 4-5)

### 4.4 Anti–factor H autoantibodies and CFHR deletions
- Anti-FH/anti-CFH autoantibodies: ~10% in US/European cohorts, up to ~50% in some Indian cohorts. (java2024atypicalhemolyticuremic pages 1-2)
- Strong association with CFHR1–CFHR3 deletions: one consensus statement cites CFHR1–CFHR3 deletion in **87%** of antibody-positive pediatric cases. (maria2025recommendationsfordiagnosis pages 5-7, maria2025recommendationsfordiagnosis pages 7-10)

### 4.5 Modifier genes / oligogenicity
About **10%** of affected patients carry >1 variant or risk polymorphism (supporting additive/oligogenic effects). (java2024atypicalhemolyticuremic pages 1-2)

### 4.6 Penetrance and expressivity
- Overall penetrance of genetic predisposition is reported as ~**50%**, consistent with trigger dependence. (java2024atypicalhemolyticuremic pages 1-2)
- Gene-specific penetrance examples: **CFH ~50%**, **MCP/CD46 ~20%** (with MCP often associated with better prognosis). (bogdan2025atypicalhemolyticuremic pages 2-4)

### 4.7 Epigenetic information / chromosomal abnormalities
No specific epigenetic mechanisms were identified in the retrieved excerpts. (Not available in this run.)


## 5. Environmental Information (triggers and exposures)
aHUS is not classically caused by a single environmental agent, but multiple *clinical exposures* can trigger disease in predisposed individuals, including infection and pregnancy-associated complications; malignancy and other inflammatory/immune contexts are described as triggers in CM-TMA literature. (musalem2025tentipsfor pages 1-2, cole2025updateinthe pages 1-3)

**Infectious triggers:** STEC infection can coexist and may precipitate complement-mediated aHUS in genetically predisposed individuals; thus STEC positivity does not exclude aHUS in atypical/severe courses. (mortari2025shigatoxinproducingescherichia pages 1-2)

**Lifestyle/toxin exposures:** Not supported by the retrieved evidence excerpts (not asserted).


## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (current consensus)
1) **Genetic variants or acquired autoantibodies** reduce control of the alternative complement pathway amplification loop. (java2024atypicalhemolyticuremic pages 1-2, musalem2025tentipsfor pages 1-2)
2) **Uncontrolled complement activation** leads to endothelial injury (and downstream microthrombi formation). (java2024atypicalhemolyticuremic pages 1-2)
3) **Microvascular thrombosis** causes MAHA (shear-related schistocytes), thrombocytopenia (consumption), and ischemic organ injury (kidney predominant). (maria2025recommendationsfordiagnosis pages 5-7)

### 6.2 Cellular and tissue targets
The proximate site of injury is the **microvascular endothelium** with consequent small-vessel thrombosis; renal microvasculature and glomerular capillaries are highlighted by renal-dominant clinical manifestations. (maria2025recommendationsfordiagnosis pages 5-7, dixon2024ravulizumabinatypical pages 1-2)

**Suggested Cell Ontology (CL) terms (examples):** endothelial cell; platelet; erythrocyte (RBC). (maria2025recommendationsfordiagnosis pages 5-7)

**Suggested GO biological process terms (examples):** complement activation (alternative pathway), regulation of complement activation, platelet aggregation, blood coagulation, endothelial cell injury/activation.

### 6.3 Biomarkers / functional assays (recent developments)
Because no single definitive diagnostic test exists, emerging *functional complement assays* are discussed as adjuncts to demonstrate complement hyperactivity (e.g., modified Ham assay and endothelial C5b-9 deposition assays). (cole2025updateinthe pages 1-3)


## 7. Anatomical Structures Affected
### 7.1 Organ level (UBERON suggestions)
- **Kidney (primary):** acute kidney injury, proteinuria/hematuria, reduced eGFR; frequent progression to CKD/ESKD in severe cases. (bogdan2025atypicalhemolyticuremic pages 4-5, java2024atypicalhemolyticuremic pages 1-2)
- **Brain / CNS:** seizures, encephalopathy, stroke. (java2024atypicalhemolyticuremic pages 1-2, bogdan2025atypicalhemolyticuremic pages 5-7)
- **Heart:** cardiomyopathy, myocardial infarction, intracardiac thrombi. (bogdan2025atypicalhemolyticuremic pages 4-5, java2024atypicalhemolyticuremic pages 1-2)
- **Gastrointestinal tract / pancreas / liver:** diarrhea, pancreatitis, transaminitis/hepatitis. (bogdan2025atypicalhemolyticuremic pages 5-7, java2024atypicalhemolyticuremic pages 1-2)
- **Lung:** pulmonary edema/respiratory failure in severe cases. (bogdan2025atypicalhemolyticuremic pages 5-7)

### 7.2 Tissue and cell level
Microvascular beds are implicated (TMA with microvascular occlusion and endothelial injury). (maria2025recommendationsfordiagnosis pages 5-7)

### 7.3 Subcellular level
Not explicitly described in retrieved excerpts.


## 8. Temporal Development
### 8.1 Onset
aHUS can present across the lifespan (pediatric to adult), and onset is often acute/subacute in the setting of a trigger. (bogdan2025atypicalhemolyticuremic pages 2-4, maria2025recommendationsfordiagnosis pages 3-5)

### 8.2 Progression
Without prompt targeted therapy, disease may progress to chronic kidney disease/ESKD and multi-organ morbidity. (dixon2024ravulizumabinatypical pages 1-2, bogdan2025atypicalhemolyticuremic pages 4-5)

### 8.3 Relapse/recurrence
Relapse risk is linked to underlying genetic/acquired etiology; long-term discontinuation decisions remain complex and are a focus of hematology guidance. (java2024atypicalhemolyticuremic pages 1-2, musalem2025tentipsfor pages 1-2)


## 9. Inheritance and Population
### 9.1 Epidemiology (statistics)
A systematic review of population-based studies reported:
- **All-ages annual incidence:** **0.23–1.9 per million per year**. (yan2020epidemiologyofatypical pages 1-2)
- **≤20 years annual incidence:** **0.26–0.75 per million per year**. (yan2020epidemiologyofatypical pages 1-2)
- **Prevalence ≤20 years:** **2.2–9.4 per million**; **single all-ages prevalence estimate: 4.9 per million**. (yan2020epidemiologyofatypical pages 1-2)

**Extrarenal complications frequency:** extrarenal complications can occur in up to ~20% in some epidemiologic descriptions. (yan2020epidemiologyofatypical pages 1-2, bogdan2025atypicalhemolyticuremic pages 7-9)

### 9.2 Inheritance pattern
The retrieved evidence supports a **genetic predisposition with incomplete penetrance** rather than a single uniform Mendelian pattern; both dominant and recessive mechanisms can exist across genes/variants, and acquired autoantibodies also contribute. Because explicit mode(s) of inheritance were not enumerated in the provided excerpts, a detailed AD/AR breakdown is not asserted here. (java2024atypicalhemolyticuremic pages 1-2, bogdan2025atypicalhemolyticuremic pages 2-4)

### 9.3 Population demographics
- Children: roughly equal sex distribution.
- Adults: higher female frequency. (yan2020epidemiologyofatypical pages 1-2)


## 10. Diagnostics
### 10.1 Clinical tests and biomarkers
Diagnostic work-up centers on confirming TMA and excluding close mimics:
- Hemolysis labs: LDH↑, schistocytes, haptoglobin↓, Coombs negative, indirect bilirubin↑. (maria2025recommendationsfordiagnosis pages 5-7)
- Platelets decreased; creatinine elevated / AKI. (java2024atypicalhemolyticuremic pages 1-2)

### 10.2 Differential diagnosis (must exclude)
- **TTP:** exclude using **ADAMTS13 activity**; severe deficiency (≤10%) supports TTP, while normal/above 10% supports non-TTP TMA context. (maria2025recommendationsfordiagnosis pages 5-7, bogdan2025atypicalhemolyticuremic pages 7-9)
- **STEC-HUS:** exclude using **Shiga toxin PCR/stool culture**. (maria2025recommendationsfordiagnosis pages 5-7)

### 10.3 Complement testing (caveats)
- Plasma C3 may be low but **low C3 occurs in <20%**; **normal C3 does not rule out aHUS**. (maria2025recommendationsfordiagnosis pages 5-7)

### 10.4 Genetic testing strategy
Expert sources recommend **complement gene panel testing plus autoantibody testing** in suspected aHUS, including evaluation for CFHR deletions/rearrangements (e.g., by MLPA when NGS is negative) and work-up of VUS by antigenic/functional assays. (java2024atypicalhemolyticuremic pages 1-2, maria2025recommendationsfordiagnosis pages 7-10)


## 11. Outcome / Prognosis
### 11.1 Renal outcomes
aHUS can lead to CKD/ESKD without timely treatment; review data cite AKI common and up to 50% ESKD in some cohorts. (bogdan2025atypicalhemolyticuremic pages 4-5)

### 11.2 Pregnancy-associated aHUS (p-aHUS) outcomes (systematic review/meta-analysis; 2025, searches through Mar 2024)
In 10 studies (386 pregnancies in 380 patients):
- **Dialysis required:** **66.6%**. (meena2025kidneyandpregnancy pages 1-2)
- **ESKD:** **25%**. (meena2025kidneyandpregnancy pages 1-2)
- **Maternal mortality:** **5%**. (meena2025kidneyandpregnancy pages 1-2)
- Obstetric complications: **preeclampsia 36.4%**, **HELLP 29.7%**. (meena2025kidneyandpregnancy pages 1-2)
- **Eculizumab benefit:** reduced CKD/ESKD risk with pooled **risk ratio 0.20 (95% CI 0.09–0.44)**. (meena2025kidneyandpregnancy pages 1-2)


## 12. Treatment
### 12.1 Pharmacotherapy (current standard; real-world implementation)
**Terminal complement inhibition (C5 inhibitors):**
- **Eculizumab:** effective since approval in 2011; requires q2 week infusions (treatment burden noted). (dixon2024ravulizumabinatypical pages 1-2)
- **Ravulizumab:** next-generation C5 inhibitor designed for extended dosing interval; maintenance every 4–8 weeks weight-based. (dixon2024ravulizumabinatypical pages 1-2)

**Ravulizumab 2-year phase 3 outcomes (published online June 14, 2024):**
- Complete TMA response over 2 years: **61% (C5i-naïve adults)** and **90% (C5i-naïve pediatrics)**. (dixon2024ravulizumabinatypical pages 1-2)
- Median eGFR improvement maintained: **+35** (adults) and **+82.5 mL/min/1.73m²** (pediatrics). (dixon2024ravulizumabinatypical pages 1-2)
- Safety: “No meningococcal infections were reported” over 2 years; most AEs/SAEs occurred in the first 26 weeks. (dixon2024ravulizumabinatypical pages 1-2)

**Real-world registry implementation (kidney transplant recipients switching eculizumab→ravulizumab; data cut Sep 2, 2024; published Aug 2025):**
- After switching, labs remained stable; **no graft failures/rejections** reported; in safety population (n=38), **50%** had any AE, **none treatment-related**; no meningococcal infections or deaths reported. (gaeckler2025effectivenessandsafety pages 1-2)

### 12.2 Supportive care / plasma exchange
Plasma exchange historically served as primary therapy in the pre-C5 inhibitor era, and remains relevant particularly in anti–factor H autoantibody–associated disease (often combined with immunosuppression), while prompt complement inhibition is emphasized for complement-driven disease. (musalem2025tentipsfor pages 1-2)

### 12.3 Prevention / prophylaxis related to therapy
Prophylactic measures against infections—particularly **meningococcal disease**—are described as mandatory/required for patients receiving C5 inhibitors. (musalem2025tentipsfor pages 1-2)

### 12.4 Suggested MAXO terms (examples)
- Complement inhibitor therapy; monoclonal antibody therapy; plasma exchange (therapeutic apheresis); kidney replacement therapy (dialysis); kidney transplantation; vaccination (meningococcal).


## 13. Prevention
Primary prevention of genetically predisposed aHUS is not established in the retrieved evidence. Prevention is primarily **tertiary** in practice (prevent relapse/complications) via appropriate complement inhibition strategies, infection prophylaxis/vaccination for C5 blockade, and trigger management (e.g., pregnancy-associated risk planning, transplant risk stratification). (musalem2025tentipsfor pages 1-2, gaeckler2025effectivenessandsafety pages 1-2)


## 14. Other Species / Natural Disease
Not available from retrieved sources in this run; no claims made.


## 15. Model Organisms
Not available from retrieved sources in this run; no claims made.


## Recent developments and 2023–2024 highlights (prioritized)
- **2024 ASH Hematology review (Java, Dec 2024)** emphasizes systematic genetic/autoantibody testing, high VUS rate (30–40%), and clinical stratification for discontinuation decisions. (java2024atypicalhemolyticuremic pages 1-2)
- **2024 Kidney Medicine phase 3 long-term analysis (Dixon et al., published online Jun 14, 2024)** provides durable 2-year efficacy/safety and sustained QoL improvements for ravulizumab in adults and children. (dixon2024ravulizumabinatypical pages 1-2)


## Summary statistics and key points table
The following table consolidates high-yield identifiers, diagnostic criteria, genetic architecture, epidemiology, and treatment outcomes.

| Category | Data point | Value/Statement | Source (first author, year) | URL | Evidence citation id (pqac-...) |
|---|---|---|---|---|---|
| Definition | Core disease definition | aHUS/complement-mediated TMA is a rare, severe thrombotic microangiopathy driven by dysregulated alternative complement pathway activation, typically presenting with microangiopathic hemolytic anemia (MAHA), thrombocytopenia, and organ injury. | Cole, 2025 | https://doi.org/10.1182/hematology.2025000702 | (cole2025updateinthe pages 1-3) |
| Definition | TMA triad | Clinical suspicion is based on the TMA triad: MAHA + thrombocytopenia + organ damage/acute kidney injury; kidneys are most commonly affected but multiorgan disease occurs. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 1-2, bogdan2025atypicalhemolyticuremic pages 7-9) |
| Diagnosis | Exclude TTP | TTP should be rapidly excluded; severe ADAMTS13 deficiency (≤10%) supports TTP, while aHUS is more likely when ADAMTS13 is >10%. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 5-7, bogdan2025atypicalhemolyticuremic pages 7-9) |
| Diagnosis | Exclude STEC-HUS | STEC-HUS should be excluded using Shiga toxin testing (stool PCR/culture/serology as available); aHUS diagnosis is one of exclusion. | Maria, 2025 | https://doi.org/10.1590/2175-8239-jbn-2024-0087en | (maria2025recommendationsfordiagnosis pages 5-7, maria2025recommendationsfordiagnosis pages 3-5) |
| Diagnosis | Typical hemolysis/lab features | Supportive findings include schistocytes, elevated LDH, low haptoglobin, negative direct Coombs test, indirect hyperbilirubinemia, hemoglobinuria, and often AKI. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 7-9) |
| Genetics | Overall genetic/acquired basis | Approximately 60–70% of patients have identifiable genetic or acquired abnormalities in complement-regulating components; genetic mutations are detected in roughly 60% of cases. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 2-4) |
| Genetics | Genetic basis phrasing from consensus | A genetic basis is present in nearly two-thirds of aHUS cases. | Maria, 2025 | https://doi.org/10.1590/2175-8239-jbn-2024-0087en | (maria2025recommendationsfordiagnosis pages 5-7, maria2025recommendationsfordiagnosis pages 7-10) |
| Genetics | Major genes implicated | Commonly implicated genes include CFH, CFI, CD46/MCP, C3, CFB, THBD, DGKE, and CFHR rearrangements/deletions; anti-CFH autoimmunity is an important acquired mechanism. | Java, 2024 | https://doi.org/10.1182/hematology.2024000543 | (java2024atypicalhemolyticuremic pages 1-2) |
| Genetics | CFH frequency | CFH variants are the most common, accounting for about 20–30% of cases (some reports/tables up to ~20–45%). | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 2-4) |
| Genetics | CFI frequency | CFI variants account for about 5–10% of cases. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 4-5, bogdan2025atypicalhemolyticuremic pages 2-4) |
| Genetics | C3 frequency | C3 variants account for about 2–10% of cases. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 2-4) |
| Genetics | Other gene frequencies | CFB variants are rare (<1% in one review excerpt); THBD variants ~3–5%. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 4-5) |
| Genetics | Penetrance examples | Estimated penetrance varies by gene: CFH ~50%; MCP/CD46 ~20%, with MCP often associated with better prognosis and lower post-transplant recurrence risk. | Bogdan, 2025 | https://doi.org/10.3390/jcm14072527 | (bogdan2025atypicalhemolyticuremic pages 2-4) |
| Genetics | Multi-hit model | Penetrance is incomplete (~50% overall in one review), consistent with a multi-hit model requiring triggers such as infection, pregnancy, surgery, autoimmune disease, or transplantation. | Java, 2024 | https://doi.org/10.1182/hematology.2024000543 | (java2024atypicalhemolyticuremic pages 1-2, bogdan2025atypicalhemolyticuremic pages 2-4) |
| Genetics | Anti-factor H autoantibody prevalence | Anti-FH/anti-CFH autoantibodies occur in ~10% of US/European cohorts, affect ~10–15% of pediatric aHUS in some reviews, and may reach ~50% in some Indian cohorts. | Java, 2024 | https://doi.org/10.1182/hematology.2024000543 | (bogdan2025atypicalhemolyticuremic pages 4-5, java2024atypicalhemolyticuremic pages 1-2) |
| Genetics | CFHR deletion association | Anti-CFH autoantibodies are strongly associated with homozygous CFHR1-CFHR3 deletions; one consensus cited this deletion in 87% of antibody-positive pediatric cases. | Maria, 2025 | https://doi.org/10.1590/2175-8239-jbn-2024-0087en | (maria2025recommendationsfordiagnosis pages 5-7, maria2025recommendationsfordiagnosis pages 7-10) |
| Diagnosis | Complement C3 level caveat | Low plasma C3 is found in fewer than 20% of patients; normal C3 does not exclude aHUS. | Maria, 2025 | https://doi.org/10.1590/2175-8239-jbn-2024-0087en | (maria2025recommendationsfordiagnosis pages 5-7) |
| Epidemiology | Overall incidence | Annual all-ages incidence in the literature ranges from 0.23 to 1.9 per million population. | Yan, 2020 | https://doi.org/10.2147/CLEP.S245642 | (yan2020epidemiologyofatypical pages 3-5, yan2020epidemiologyofatypical pages 1-2) |
| Epidemiology | Pediatric incidence | Annual incidence in individuals ≤20 years ranges from 0.26 to 0.75 per million. | Yan, 2020 | https://doi.org/10.2147/CLEP.S245642 | (yan2020epidemiologyofatypical pages 3-5, yan2020epidemiologyofatypical pages 1-2) |
| Epidemiology | Prevalence | Prevalence in individuals ≤20 years ranges from 2.2 to 9.4 per million; one all-ages prevalence estimate was 4.9 per million. | Yan, 2020 | https://doi.org/10.2147/CLEP.S245642 | (yan2020epidemiologyofatypical pages 3-5, yan2020epidemiologyofatypical pages 1-2) |
| Epidemiology | Demographics | Children show roughly equal sex distribution; adults show higher female frequency. Mean/median diagnosis age is typically <2 years in pediatric reports and ~31–37 years in adults. | Yan, 2020 | https://doi.org/10.2147/CLEP.S245642 | (yan2020epidemiologyofatypical pages 3-5, yan2020epidemiologyofatypical pages 1-2) |
| Treatment | Approved complement target | C5 is a validated therapeutic target; FDA/clinical development evidence includes eculizumab and ravulizumab, with additional phase 3 development for crovalimab. | Open Targets, accessed via platform evidence | https://platform.opentargets.org/disease/MONDO_0016244/associations | (dixon2024ravulizumabinatypical pages 1-2) |
| Treatment | Ravulizumab 2-year complete TMA response | In phase 3 trials, 2-year complete TMA response rates were 61% in C5 inhibitor-naive adults and 90% in pediatric patients. | Dixon, 2024 | https://doi.org/10.1016/j.xkme.2024.100855 | (dixon2024ravulizumabinatypical pages 1-2, dixon2024ravulizumabinatypical pages 9-10) |
| Treatment | Ravulizumab renal benefit | Median eGFR improvement at 2 years was +35 mL/min/1.73 m² in adults and +82.5 mL/min/1.73 m² in pediatric patients. | Dixon, 2024 | https://doi.org/10.1016/j.xkme.2024.100855 | (dixon2024ravulizumabinatypical pages 1-2) |
| Treatment | Ravulizumab safety highlights | Most AEs/SAEs occurred in the first 26 weeks and declined thereafter; no meningococcal infections were reported over 2 years. Common adult AEs included headache (40%) and diarrhea (35%). | Dixon, 2024 | https://doi.org/10.1016/j.xkme.2024.100855 | (dixon2024ravulizumabinatypical pages 9-10, dixon2024ravulizumabinatypical pages 5-6) |
| Treatment | Ravulizumab dosing practicality | Ravulizumab provides immediate, complete, sustained C5 inhibition with maintenance dosing every 4–8 weeks by weight. | Dixon, 2024 | https://doi.org/10.1016/j.xkme.2024.100855 | (dixon2024ravulizumabinatypical pages 1-2, dixon2024ravulizumabinatypical pages 9-10) |
| Treatment | Real-world switch: transplant recipients | In Global aHUS Registry kidney transplant recipients switched from eculizumab to ravulizumab, labs remained stable, with no TMA signs/symptoms, no dialysis, and no transplant rejection/graft failure reported after switching. | Gaeckler, 2025 | https://doi.org/10.1111/ctr.70278 | (gaeckler2025effectivenessandsafety pages 1-2, gaeckler2025effectivenessandsafety pages 2-3) |
| Treatment | Real-world switch safety | In the registry safety population (n=38), 23 AEs occurred in 19 patients (50.0%), none treatment-related; no meningococcal infections or deaths were reported. | Gaeckler, 2025 | https://doi.org/10.1111/ctr.70278 | (gaeckler2025effectivenessandsafety pages 1-2) |
| Pregnancy-associated aHUS | Disease burden in meta-analysis | Systematic review/meta-analysis included 386 pregnancies in 380 patients with pregnancy-associated aHUS. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 1-2, meena2025kidneyandpregnancy pages 3-4) |
| Pregnancy-associated aHUS | Dialysis requirement | 228/342 patients (66.6%) required dialysis. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 2-3, meena2025kidneyandpregnancy pages 1-2) |
| Pregnancy-associated aHUS | ESKD proportion | About 25% developed ESKD. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 2-3, meena2025kidneyandpregnancy pages 1-2) |
| Pregnancy-associated aHUS | CKD/persistent dysfunction | Persistent renal dysfunction/CKD was reported in about 20% of patients. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 2-3) |
| Pregnancy-associated aHUS | Maternal mortality | Maternal deaths occurred in 5% of reported cases. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 2-3, meena2025kidneyandpregnancy pages 1-2) |
| Pregnancy-associated aHUS | Obstetric complications | Preeclampsia occurred in 36.4% and HELLP syndrome in 29.7% of reported patients. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 2-3, meena2025kidneyandpregnancy pages 1-2) |
| Pregnancy-associated aHUS | Eculizumab effect estimate (CKD/ESKD) | Eculizumab significantly reduced poor renal outcomes; pooled risk ratio/odds ratio for CKD/ESKD was 0.20 (95% CI 0.09–0.44), with low heterogeneity. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 1-2, meena2025kidneyandpregnancy pages 3-4) |
| Pregnancy-associated aHUS | Eculizumab effect estimate (ESKD) | Unadjusted hazard ratio for ESKD with eculizumab was 0.14 (95% CI 0.04–0.47; P=.002) in the meta-analysis synthesis. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 3-4) |
| Pregnancy-associated aHUS | Mortality/safety signal with eculizumab | Meta-analysis described a significant mortality benefit and reported no allergic reactions, infections, drug-related deaths, or fetal congenital abnormalities attributed to eculizumab in included studies. | Meena, 2025 | https://doi.org/10.1097/MD.0000000000041403 | (meena2025kidneyandpregnancy pages 7-9) |


*Table: This table compiles high-yield clinical, genetic, epidemiologic, treatment, and pregnancy-associated statistics for atypical hemolytic uremic syndrome from the gathered evidence. It is designed as a compact reference for a disease knowledge base or research summary.*


## Limitations of this evidence package
- ICD-10/ICD-11, Orphanet ORPHA, and OMIM identifiers were **not explicitly present** in the retrieved excerpts; therefore they are not asserted despite being likely available in external disease resources.
- Dedicated model-organism/animal-model primary literature was not retrieved in this run; therefore model organism sections are intentionally left as “not available.”


References

1. (musalem2025tentipsfor pages 1-2): Pilar Musalem. Ten tips for managing complement-mediated thrombotic microangiopathies (formerly atypical hemolytic uremic syndrome): narrative review. BMC Nephrology, Mar 2025. URL: https://doi.org/10.1186/s12882-025-04080-9, doi:10.1186/s12882-025-04080-9. This article has 3 citations and is from a peer-reviewed journal.

2. (cole2025updateinthe pages 1-3): Michael Arthur Cole. Update in the diagnosis of complement-mediated thrombotic microangiopathy/atypical hemolytic uremic syndrome. Hematology, 2025:164-175, Dec 2025. URL: https://doi.org/10.1182/hematology.2025000702, doi:10.1182/hematology.2025000702. This article has 2 citations and is from a peer-reviewed journal.

3. (bogdan2025atypicalhemolyticuremic pages 2-4): Razvan-George Bogdan, Paula Anderco, Cristian Ichim, Anca-Maria Cimpean, Samuel Bogdan Todor, Mihai Glaja-Iliescu, Zorin Petrisor Crainiceanu, and Mirela Livia Popa. Atypical hemolytic uremic syndrome: a review of complement dysregulation, genetic susceptibility and multiorgan involvement. Journal of Clinical Medicine, 14:2527, Apr 2025. URL: https://doi.org/10.3390/jcm14072527, doi:10.3390/jcm14072527. This article has 18 citations.

4. (dixon2024ravulizumabinatypical pages 1-2): Bradley P. Dixon, David Kavanagh, Alvaro Domingo Madrid Aris, Brigitte Adams, Hee Gyung Kang, Edward Wang, Katherine Garlo, Masayo Ogawa, Praveen Amancha, Sourish Chakravarty, Nils Heyne, Seong Heon Kim, Spero Cataland, Sung-Soo Yoon, Yoshitaka Miyakawa, Yosu Luque, Melissa Muff-Luett, Kazuki Tanaka, and Larry A. Greenbaum. Ravulizumab in atypical hemolytic uremic syndrome: an analysis of 2-year efficacy and safety outcomes in 2 phase 3 trials. Kidney Medicine, 6:100855, Aug 2024. URL: https://doi.org/10.1016/j.xkme.2024.100855, doi:10.1016/j.xkme.2024.100855. This article has 27 citations.

5. (NCT01522183 chunk 5):  Atypical Hemolytic-Uremic Syndrome (aHUS) Registry. Alexion Pharmaceuticals, Inc.. 2013. ClinicalTrials.gov Identifier: NCT01522183

6. (NCT04861259 chunk 3):  A Study Evaluating the Efficacy, Safety, Pharmacokinetics and Pharmacodynamics of Crovalimab in Adult and Adolescent Participants With Atypical Hemolytic Uremic Syndrome (aHUS). Hoffmann-La Roche. 2021. ClinicalTrials.gov Identifier: NCT04861259

7. (java2024atypicalhemolyticuremic pages 1-2): Anuja Java. Atypical hemolytic uremic syndrome: diagnosis, management, and discontinuation of therapy. Hematology, 2024:200-205, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000543, doi:10.1182/hematology.2024000543. This article has 15 citations and is from a peer-reviewed journal.

8. (cole2025updateinthe pages 12-12): Michael Arthur Cole. Update in the diagnosis of complement-mediated thrombotic microangiopathy/atypical hemolytic uremic syndrome. Hematology, 2025:164-175, Dec 2025. URL: https://doi.org/10.1182/hematology.2025000702, doi:10.1182/hematology.2025000702. This article has 2 citations and is from a peer-reviewed journal.

9. (meena2025kidneyandpregnancy pages 1-2): Priti Meena, Ruju Gala, Rashmi Ranjan Das, Vinant Bhargava, Yellampalli Saivani, Sandip Panda, Alok Mantri, and Krishna Kumar Agrawaal. Kidney and pregnancy outcomes in pregnancy-associated atypical hemolytic uremic syndrome: a systematic review and meta-analysis. Medicine, 104:e41403, Jan 2025. URL: https://doi.org/10.1097/md.0000000000041403, doi:10.1097/md.0000000000041403. This article has 9 citations and is from a peer-reviewed journal.

10. (yan2020epidemiologyofatypical pages 3-5): Kevin Yan, Kamal Desai, Lakshmi Gullapalli, Eric Druyts, and Chakrapani Balijepalli. Epidemiology of atypical hemolytic uremic syndrome: a systematic literature review. Clinical Epidemiology, 12:295-305, Mar 2020. URL: https://doi.org/10.2147/clep.s245642, doi:10.2147/clep.s245642. This article has 144 citations and is from a highest quality peer-reviewed journal.

11. (maria2025recommendationsfordiagnosis pages 5-7): Helena Vaisbich Maria, Andrade Luis Gustavo Modelli de, Barbosa Maria Izabel Neves de Holan da, Castro Maria Cristina Ribeiro de, Miranda Silvana Maria Carvalho, Poli-de-Figueiredo Carlos Eduardo, Araujo Stanley de Almeida, Neto Miguel Ernandes, Penido Maria Goretti Moreira Guimarães, Sobral Roberta Mendes Lima, Neto Oreste Ferra, Neves Precil Diego Miranda de Menezes, Silva Cassiano Augusto Braga da, Barreto Fellype Carvalho, Pietrobom Igor Gouveia, and Palma Lilian Monteiro Pereira. Recommendations for diagnosis and treatment of atypical hemolytic uremic syndrome (ahus): an expert consensus statement from the rare diseases committee of the brazilian society of nephrology (comdora-sbn). Jornal Brasileiro de Nefrologia, Feb 2025. URL: https://doi.org/10.1590/2175-8239-jbn-2024-0087en, doi:10.1590/2175-8239-jbn-2024-0087en. This article has 7 citations.

12. (maria2025recommendationsfordiagnosis pages 7-10): Helena Vaisbich Maria, Andrade Luis Gustavo Modelli de, Barbosa Maria Izabel Neves de Holan da, Castro Maria Cristina Ribeiro de, Miranda Silvana Maria Carvalho, Poli-de-Figueiredo Carlos Eduardo, Araujo Stanley de Almeida, Neto Miguel Ernandes, Penido Maria Goretti Moreira Guimarães, Sobral Roberta Mendes Lima, Neto Oreste Ferra, Neves Precil Diego Miranda de Menezes, Silva Cassiano Augusto Braga da, Barreto Fellype Carvalho, Pietrobom Igor Gouveia, and Palma Lilian Monteiro Pereira. Recommendations for diagnosis and treatment of atypical hemolytic uremic syndrome (ahus): an expert consensus statement from the rare diseases committee of the brazilian society of nephrology (comdora-sbn). Jornal Brasileiro de Nefrologia, Feb 2025. URL: https://doi.org/10.1590/2175-8239-jbn-2024-0087en, doi:10.1590/2175-8239-jbn-2024-0087en. This article has 7 citations.

13. (bogdan2025atypicalhemolyticuremic pages 7-9): Razvan-George Bogdan, Paula Anderco, Cristian Ichim, Anca-Maria Cimpean, Samuel Bogdan Todor, Mihai Glaja-Iliescu, Zorin Petrisor Crainiceanu, and Mirela Livia Popa. Atypical hemolytic uremic syndrome: a review of complement dysregulation, genetic susceptibility and multiorgan involvement. Journal of Clinical Medicine, 14:2527, Apr 2025. URL: https://doi.org/10.3390/jcm14072527, doi:10.3390/jcm14072527. This article has 18 citations.

14. (bogdan2025atypicalhemolyticuremic pages 5-7): Razvan-George Bogdan, Paula Anderco, Cristian Ichim, Anca-Maria Cimpean, Samuel Bogdan Todor, Mihai Glaja-Iliescu, Zorin Petrisor Crainiceanu, and Mirela Livia Popa. Atypical hemolytic uremic syndrome: a review of complement dysregulation, genetic susceptibility and multiorgan involvement. Journal of Clinical Medicine, 14:2527, Apr 2025. URL: https://doi.org/10.3390/jcm14072527, doi:10.3390/jcm14072527. This article has 18 citations.

15. (bogdan2025atypicalhemolyticuremic pages 4-5): Razvan-George Bogdan, Paula Anderco, Cristian Ichim, Anca-Maria Cimpean, Samuel Bogdan Todor, Mihai Glaja-Iliescu, Zorin Petrisor Crainiceanu, and Mirela Livia Popa. Atypical hemolytic uremic syndrome: a review of complement dysregulation, genetic susceptibility and multiorgan involvement. Journal of Clinical Medicine, 14:2527, Apr 2025. URL: https://doi.org/10.3390/jcm14072527, doi:10.3390/jcm14072527. This article has 18 citations.

16. (mortari2025shigatoxinproducingescherichia pages 1-2): Gabriele Mortari, Carolina Bigatti, Giulia Proietti Gaffi, Barbara Lionetti, Andrea Angeletti, Simona Matarese, Enrico Eugenio Verrina, Gianluca Caridi, Francesca Lugani, Valerio Gaetano Vellone, Decimo Silvio Chiarenza, and Edoardo La Porta. Shiga toxin-producing escherichia coli infection as a precipitating factor for atypical hemolytic-uremic syndrome. Pediatric Nephrology (Berlin, Germany), 40:449-461, Sep 2025. URL: https://doi.org/10.1007/s00467-024-06480-9, doi:10.1007/s00467-024-06480-9. This article has 2 citations.

17. (maria2025recommendationsfordiagnosis pages 3-5): Helena Vaisbich Maria, Andrade Luis Gustavo Modelli de, Barbosa Maria Izabel Neves de Holan da, Castro Maria Cristina Ribeiro de, Miranda Silvana Maria Carvalho, Poli-de-Figueiredo Carlos Eduardo, Araujo Stanley de Almeida, Neto Miguel Ernandes, Penido Maria Goretti Moreira Guimarães, Sobral Roberta Mendes Lima, Neto Oreste Ferra, Neves Precil Diego Miranda de Menezes, Silva Cassiano Augusto Braga da, Barreto Fellype Carvalho, Pietrobom Igor Gouveia, and Palma Lilian Monteiro Pereira. Recommendations for diagnosis and treatment of atypical hemolytic uremic syndrome (ahus): an expert consensus statement from the rare diseases committee of the brazilian society of nephrology (comdora-sbn). Jornal Brasileiro de Nefrologia, Feb 2025. URL: https://doi.org/10.1590/2175-8239-jbn-2024-0087en, doi:10.1590/2175-8239-jbn-2024-0087en. This article has 7 citations.

18. (yan2020epidemiologyofatypical pages 1-2): Kevin Yan, Kamal Desai, Lakshmi Gullapalli, Eric Druyts, and Chakrapani Balijepalli. Epidemiology of atypical hemolytic uremic syndrome: a systematic literature review. Clinical Epidemiology, 12:295-305, Mar 2020. URL: https://doi.org/10.2147/clep.s245642, doi:10.2147/clep.s245642. This article has 144 citations and is from a highest quality peer-reviewed journal.

19. (gaeckler2025effectivenessandsafety pages 1-2): Anja Gaeckler, Imad Al‐Dakkak, Nuria Saval, Hans Herman Dieperink, Margriet Eygenraam, Larry A. Greenbaum, Nicole Isbel, and Johan Vande Walle. Effectiveness and safety of switching to ravulizumab from eculizumab in kidney transplant recipients with atypical hemolytic uremic syndrome: a global ahus registry analysis. Clinical Transplantation, Aug 2025. URL: https://doi.org/10.1111/ctr.70278, doi:10.1111/ctr.70278. This article has 2 citations and is from a peer-reviewed journal.

20. (bogdan2025atypicalhemolyticuremic pages 1-2): Razvan-George Bogdan, Paula Anderco, Cristian Ichim, Anca-Maria Cimpean, Samuel Bogdan Todor, Mihai Glaja-Iliescu, Zorin Petrisor Crainiceanu, and Mirela Livia Popa. Atypical hemolytic uremic syndrome: a review of complement dysregulation, genetic susceptibility and multiorgan involvement. Journal of Clinical Medicine, 14:2527, Apr 2025. URL: https://doi.org/10.3390/jcm14072527, doi:10.3390/jcm14072527. This article has 18 citations.

21. (dixon2024ravulizumabinatypical pages 9-10): Bradley P. Dixon, David Kavanagh, Alvaro Domingo Madrid Aris, Brigitte Adams, Hee Gyung Kang, Edward Wang, Katherine Garlo, Masayo Ogawa, Praveen Amancha, Sourish Chakravarty, Nils Heyne, Seong Heon Kim, Spero Cataland, Sung-Soo Yoon, Yoshitaka Miyakawa, Yosu Luque, Melissa Muff-Luett, Kazuki Tanaka, and Larry A. Greenbaum. Ravulizumab in atypical hemolytic uremic syndrome: an analysis of 2-year efficacy and safety outcomes in 2 phase 3 trials. Kidney Medicine, 6:100855, Aug 2024. URL: https://doi.org/10.1016/j.xkme.2024.100855, doi:10.1016/j.xkme.2024.100855. This article has 27 citations.

22. (dixon2024ravulizumabinatypical pages 5-6): Bradley P. Dixon, David Kavanagh, Alvaro Domingo Madrid Aris, Brigitte Adams, Hee Gyung Kang, Edward Wang, Katherine Garlo, Masayo Ogawa, Praveen Amancha, Sourish Chakravarty, Nils Heyne, Seong Heon Kim, Spero Cataland, Sung-Soo Yoon, Yoshitaka Miyakawa, Yosu Luque, Melissa Muff-Luett, Kazuki Tanaka, and Larry A. Greenbaum. Ravulizumab in atypical hemolytic uremic syndrome: an analysis of 2-year efficacy and safety outcomes in 2 phase 3 trials. Kidney Medicine, 6:100855, Aug 2024. URL: https://doi.org/10.1016/j.xkme.2024.100855, doi:10.1016/j.xkme.2024.100855. This article has 27 citations.

23. (gaeckler2025effectivenessandsafety pages 2-3): Anja Gaeckler, Imad Al‐Dakkak, Nuria Saval, Hans Herman Dieperink, Margriet Eygenraam, Larry A. Greenbaum, Nicole Isbel, and Johan Vande Walle. Effectiveness and safety of switching to ravulizumab from eculizumab in kidney transplant recipients with atypical hemolytic uremic syndrome: a global ahus registry analysis. Clinical Transplantation, Aug 2025. URL: https://doi.org/10.1111/ctr.70278, doi:10.1111/ctr.70278. This article has 2 citations and is from a peer-reviewed journal.

24. (meena2025kidneyandpregnancy pages 3-4): Priti Meena, Ruju Gala, Rashmi Ranjan Das, Vinant Bhargava, Yellampalli Saivani, Sandip Panda, Alok Mantri, and Krishna Kumar Agrawaal. Kidney and pregnancy outcomes in pregnancy-associated atypical hemolytic uremic syndrome: a systematic review and meta-analysis. Medicine, 104:e41403, Jan 2025. URL: https://doi.org/10.1097/md.0000000000041403, doi:10.1097/md.0000000000041403. This article has 9 citations and is from a peer-reviewed journal.

25. (meena2025kidneyandpregnancy pages 2-3): Priti Meena, Ruju Gala, Rashmi Ranjan Das, Vinant Bhargava, Yellampalli Saivani, Sandip Panda, Alok Mantri, and Krishna Kumar Agrawaal. Kidney and pregnancy outcomes in pregnancy-associated atypical hemolytic uremic syndrome: a systematic review and meta-analysis. Medicine, 104:e41403, Jan 2025. URL: https://doi.org/10.1097/md.0000000000041403, doi:10.1097/md.0000000000041403. This article has 9 citations and is from a peer-reviewed journal.

26. (meena2025kidneyandpregnancy pages 7-9): Priti Meena, Ruju Gala, Rashmi Ranjan Das, Vinant Bhargava, Yellampalli Saivani, Sandip Panda, Alok Mantri, and Krishna Kumar Agrawaal. Kidney and pregnancy outcomes in pregnancy-associated atypical hemolytic uremic syndrome: a systematic review and meta-analysis. Medicine, 104:e41403, Jan 2025. URL: https://doi.org/10.1097/md.0000000000041403, doi:10.1097/md.0000000000041403. This article has 9 citations and is from a peer-reviewed journal.