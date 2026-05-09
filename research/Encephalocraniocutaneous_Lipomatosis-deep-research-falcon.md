---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T15:25:59.108961'
end_time: '2026-05-08T15:56:54.738205'
duration_seconds: 1855.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Encephalocraniocutaneous Lipomatosis
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Encephalocraniocutaneous Lipomatosis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Encephalocraniocutaneous Lipomatosis** covering all of the
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
- **Disease Name:** Encephalocraniocutaneous Lipomatosis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Encephalocraniocutaneous Lipomatosis** covering all of the
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


# Encephalocraniocutaneous Lipomatosis (ECCL; Haberland syndrome) — Disease Characteristics Research Report

## Target disease
Encephalocraniocutaneous lipomatosis (ECCL) is a rare, congenital neurocutaneous syndrome characterized by a triad of cutaneous, ocular, and central nervous system (CNS) malformations that are often patchy/asymmetric, consistent with postzygotic mosaicism. (bennett2016mosaicactivatingmutations pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 1-2)

**Scope note (evidence type):** The ECCL knowledge base evidence base is primarily aggregated from published case reports/series and reviews (e.g., Moog’s 54-case synthesis) rather than from population-scale cohorts or EHR-derived datasets. (moog2009encephalocraniocutaneouslipomatosis pages 5-6, moog2009encephalocraniocutaneouslipomatosis pages 1-2)

## 1. Disease information
### 1.1 Concise overview / definition
ECCL is a sporadic congenital condition with ocular, cutaneous, and CNS involvement; hallmark lesions include nevus psiloliparus (alopecic fatty scalp nevus), ocular choristomas (epibulbar dermoids/lipodermoids), and intracranial/intraspinal lipomas and related brain malformations. (bennett2016mosaicactivatingmutations pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 5-6)

### 1.2 Key identifiers and synonyms
- **OMIM:** **#613001** (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2)
- **Orphanet:** **ORPHA:2396** (marechal2024brafmutantschwanncells pages 1-4)
- **Synonyms:** Haberland syndrome; Fishman syndrome / Fishman’s syndrome. (siddiqui2017encephalocraniocutaneouslipomatosisa pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 1-2)

**Not found in retrieved full texts (flag for external verification):** MONDO ID, MeSH heading, ICD-10/ICD-11 codes. (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, marechal2024brafmutantschwanncells pages 1-4)

## 2. Etiology
### 2.1 Disease causal factors (genetic/mechanistic)
**Current understanding:** ECCL is best understood as a **mosaic developmental RAS/MAPK-pathway disorder** (a mosaic RASopathy spectrum disorder). Multiple genetic mechanisms can converge on **RAS-MAPK signaling upregulation**:

1) **Postzygotic mosaic activating FGFR1 variants** (primary established mechanism)
- Bennett et al. identified recurrent FGFR1 kinase-domain mosaic variants in affected tissues (not reliably in blood), including **FGFR1 c.1638C>A (p.Asn546Lys; N546K)** and **c.1966A>G (p.Lys656Glu; K656E)**. (bennett2016mosaicactivatingmutations pages 1-2)
- Functional studies in ECCL fibroblast cell lines showed increased phosphorylated FGFR/FRS2 and constitutive downstream signaling consistent with **RAS-MAPK pathway activation**. (bennett2016mosaicactivatingmutations pages 1-2)

2) **Postzygotic KRAS variants (codon 146 hotspot)**
- ECCL is described as a sporadic RASopathy in which mosaic FGFR1 hotspot variants are common; a 2024 neuroradiology case report of ECCL with diffuse leptomeningeal glioneural tumor (DL-GNT) reported a **KRAS codon 146 mutation** in the patient described. (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3)

3) **Alternative convergent pathway mechanism via NF1** (recent development)
- A 2024 Journal of Medical Genetics report described an ECCL phenotype explained by **early embryonic mosaic biallelic NF1 inactivation** (germline NF1 nonsense plus somatic second hit on the other allele) localized to affected tissues, arguing that distinct mosaic mechanisms can produce an ECCL phenotype by converging on the RAS-MAPK pathway. (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6)

### 2.2 Risk factors and protective factors
- **Risk factors:** For most patients, ECCL arises sporadically via postzygotic events; **familial risk is not supported by available evidence** (no recurrence in siblings/offspring reported in Moog’s synthesis). (moog2009encephalocraniocutaneouslipomatosis pages 7-8)
- **Protective factors / gene–environment interactions:** Not reported in retrieved evidence; ECCL is not described as environmentally triggered in available sources.

## 3. Phenotypes (with frequencies, when available)
Moog (2009) synthesized **54** ECCL cases and provides the most commonly cited quantitative phenotype frequencies in retrieved evidence. (moog2009encephalocraniocutaneouslipomatosis pages 5-6)

### 3.1 Core phenotypes and frequencies (selected)
- **Nevus psiloliparus:** 44/54. (moog2009encephalocraniocutaneouslipomatosis pages 1-2)
- **Subcutaneous frontotemporal/zygomatic fatty masses:** 21/54. (moog2009encephalocraniocutaneouslipomatosis pages 1-2)
- **Scarring alopecia (often from focal scalp aplasia):** 14/54. (moog2009encephalocraniocutaneouslipomatosis pages 1-2)
- **Ocular choristomas (epibulbar/limbal dermoids/lipodermoids):** reported in the majority, **43/54**. (moog2009encephalocraniocutaneouslipomatosis pages 4-4)
- **Bilateral skin/eye abnormalities:** 22/54 (40%). (moog2009encephalocraniocutaneouslipomatosis pages 5-6)
- **CNS lipomas on imaging:** 33/54; **intracranial lipomas** 31/54 (cerebellopontine angle in 19/31). (moog2009encephalocraniocutaneouslipomatosis pages 5-6)
- **Spinal lipomas:** 12/14 when specifically investigated (supports routine consideration of spinal MRI). (moog2009encephalocraniocutaneouslipomatosis pages 5-6)
- **Arachnoid cysts:** 21 cases. (moog2009encephalocraniocutaneouslipomatosis pages 5-6)
- **Seizures/epilepsy:** 27/54; among seizure cases, onset occurred within first month (9), within first year (7), or after 1 year (6). Response categories among seizure cases: refractory (8), difficult to treat (6), responded well (13). (moog2009encephalocraniocutaneouslipomatosis pages 5-6)
- **Neurodevelopmental outcomes (45 with data):** normal (13), mild delay (16), moderate–severe/unspecified delay (16). (moog2009encephalocraniocutaneouslipomatosis pages 5-6)

**Additional frequency estimates (Bennett 2016 excerpt):** nevus psiloliparus and ocular choristomas each ~80%; intracranial/intraspinal lipomas ~61%. (bennett2016mosaicactivatingmutations pages 1-2)

### 3.2 Phenotype ontology suggestions (examples)
Selected HPO mappings are summarized in the phenotype table artifact. (moog2009encephalocraniocutaneouslipomatosis pages 5-6, moog2009encephalocraniocutaneouslipomatosis pages 1-2)

## 4. Genetic / molecular information
### 4.1 Causal genes and variant classes
- **FGFR1** (activating, postzygotic mosaic variants; typically kinase-domain hotspots N546K and K656E). (bennett2016mosaicactivatingmutations pages 1-2)
- **KRAS** (postzygotic mosaic variants including codon 146 hotspot in ECCL spectrum). (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3)
- **NF1** (rare/expanded mechanism: mosaic biallelic inactivation in affected tissues producing ECCL phenotype via RAS-MAPK dysregulation). (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13)

### 4.2 Somatic vs germline
ECCL is primarily described as **postzygotic constitutional mosaicism**, with variants often absent from peripheral blood; sensitive detection from affected tissue is frequently required. (bennett2016mosaicactivatingmutations pages 1-2, kordacka2019sensitivedetectionof pages 1-2)

### 4.3 Functional consequences / pathway
- FGFR1 activating variants are supported by functional signaling readouts (phospho-FGFR/FRS2; downstream RAS-MAPK activation) in patient-derived fibroblast lines. (bennett2016mosaicactivatingmutations pages 1-2)
- NF1 mosaic biallelic loss provides an alternate route to RAS-MAPK hyperactivation. (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13)

### 4.4 Population allele frequency
Population allele frequency information (gnomAD/ExAC/TOPMed) was not available in retrieved full-text evidence; variants are typically mosaic and thus not expected at appreciable germline frequencies.

## 5. Environmental information
No specific environmental/lifestyle or infectious contributors are described in retrieved evidence; ECCL is treated as a congenital developmental mosaic condition. (bennett2016mosaicactivatingmutations pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 7-8)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (current model)
A plausible causal chain is:
1) **Early embryonic postzygotic mutation** (most often FGFR1 activation; sometimes KRAS activation; rarely NF1 biallelic inactivation in mosaic tissues) →
2) **Localized hyperactivation of RAS-MAPK signaling** in a subset of embryonic lineages →
3) **Abnormal development of neural-crest/mesenchyme-derived tissues** (skin adnexa/subcutis, ocular surface/choristomas, meninges/cranial vessels, brain malformations, lipomas/cysts) →
4) Clinical triad of cutaneous, ocular, and CNS abnormalities; in some, secondary complications such as epilepsy, hydrocephalus, and tumor predisposition. (bennett2016mosaicactivatingmutations pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 7-8, ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3)

### 6.2 Candidate pathway/ontology terms (suggested)
- **GO biological process (suggested):** “MAPK cascade”, “RAS protein signal transduction”, “embryonic morphogenesis”, “neural crest cell migration/differentiation” (pathway-level mapping inferred from the RAS-MAPK convergence described in primary genetics/functional evidence). (bennett2016mosaicactivatingmutations pages 1-2, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13)
- **Cell Ontology (suggested):** neural crest cell; fibroblast (patient-derived fibroblasts used for functional assays). (bennett2016mosaicactivatingmutations pages 1-2)

## 7. Anatomical structures affected
ECCL predominantly affects:
- **Skin/scalp and craniofacial subcutis** (nevus psiloliparus; subcutaneous lipomas; alopecia/aplasia). (moog2009encephalocraniocutaneouslipomatosis pages 1-2)
- **Eye/adnexa** (epibulbar/limbal dermoids/lipodermoids; choristomas). (moog2009encephalocraniocutaneouslipomatosis pages 4-4)
- **CNS and meninges** (intracranial/spinal lipomas; arachnoid cysts; hemispheric atrophy; porencephalic cysts; cortical dysplasia/calcification patterns). (moog2009encephalocraniocutaneouslipomatosis pages 5-6, siddiqui2017encephalocraniocutaneouslipomatosisa pages 2-5)

**Lateralization:** although often unilateral/asymmetric, bilateral skin/eye involvement occurs in ~40% of Moog’s 54-case synthesis. (moog2009encephalocraniocutaneouslipomatosis pages 5-6)

## 8. Temporal development
### 8.1 Onset
Most characteristic lesions are **congenital/present at birth** (scalp/ocular/cerebral malformations). (moog2009encephalocraniocutaneouslipomatosis pages 1-2, siddiqui2017encephalocraniocutaneouslipomatosisa pages 1-2)

### 8.2 Progression
ECCL is often described as **non-progressive/static**, but selected features may emerge or progress (e.g., certain vascular lesions, hydrocephalus; progressive jaw/bone lesions in some). (moog2009encephalocraniocutaneouslipomatosis pages 7-8, moog2009encephalocraniocutaneouslipomatosis pages 5-6)

### 8.3 Seizure timing
Among reported seizure cases in Moog’s synthesis, many began in infancy (9 within first month; 7 within first year). (moog2009encephalocraniocutaneouslipomatosis pages 5-6)

## 9. Inheritance and population
### 9.1 Inheritance pattern
ECCL is predominantly **sporadic** with no reported recurrence in siblings/offspring in Moog’s review, supporting a postzygotic mosaic mechanism rather than Mendelian inheritance. (moog2009encephalocraniocutaneouslipomatosis pages 7-8)

### 9.2 Epidemiology
- Moog’s review included **54** cases (32 male; 22 female). (moog2009encephalocraniocutaneouslipomatosis pages 7-8)
- Later reviews cited **<80** cases, including a literature search identifying **77** patients. (garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 1-2)

**Prevalence/incidence:** Not available in retrieved evidence; no population-based estimates were found.

## 10. Diagnostics
### 10.1 Clinical criteria
Moog (2009) revised diagnostic criteria (Box 1) define major/minor features across eye, skin, CNS, and other findings; examples include ocular choristoma and proven nevus psiloliparus (major) and multiple CNS imaging features (minor) such as arachnoid cysts, hemispheric atrophy, porencephalic cysts, asymmetric ventricles/hydrocephalus, and calcifications (not basal ganglia). (moog2009encephalocraniocutaneouslipomatosis pages 6-7, moog2009encephalocraniocutaneouslipomatosis media 02ca15fc)

### 10.2 Imaging
Neuroimaging commonly identifies intracranial/spinal lipomas, arachnoid and porencephalic cysts, hemispheric atrophy, and calcifications; these findings also guide differential diagnosis (e.g., Sturge–Weber syndrome, hemimegalencephaly). (siddiqui2017encephalocraniocutaneouslipomatosisa pages 2-5)

### 10.3 Genetic testing strategy (mosaic disease)
Because variants can be absent in blood, diagnostic yield is improved by sequencing **affected tissue** (e.g., scalp lesion fibroblasts, lipoma, brain/tumor tissue) with **high-depth approaches** and/or sensitive mosaic detection such as **ddPCR**. (kordacka2019sensitivedetectionof pages 1-2, venigalla2025histopathologicfeaturesand pages 5-7)

## 11. Outcome / prognosis
Outcomes vary widely. In Moog’s synthesis, about two-thirds had normal development or mild delay; seizures were present in ~half, with a subset refractory. (moog2009encephalocraniocutaneouslipomatosis pages 5-6, moog2009encephalocraniocutaneouslipomatosis pages 7-8)

## 12. Treatment
There is no disease-specific curative treatment; management is **symptom-directed** and multidisciplinary. (siddiqui2017encephalocraniocutaneouslipomatosisa pages 5-5, karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5)

**Examples of real-world implementations (from recent case literature):**
- **Drug-refractory epilepsy:** A child with ECCL failed multiple antiseizure medications (levetiracetam, zonisamide, valproate, clobazam) and underwent **functional hemispherectomy**, achieving **Engel class IA seizure freedom at 2.5 years** with functional and neuropsychological improvements. (koueik2025functionalhemispherectomyfor pages 2-3)
- **Hydrocephalus:** ventriculoperitoneal shunting may be required in some cases. (karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5)
- **Ocular complications:** topical timolol for secondary glaucoma; temporary tarsorrhaphy for lagophthalmos in an infant managed conservatively with serial MRI. (subbiah2022encephalocraniocutaneouslipomatosisa pages 1-2)
- **Targeted therapy (tumor-associated):** In a child with progressive pilocytic astrocytoma and mosaic activating FGFR1 p.Lys656Glu, off-label **trametinib (MEK inhibitor)** was associated with stable tumor size at 6 months after multiple chemotherapy regimens. (bavle2018encephalocraniocutaneouslipomatosis. pages 1-2)

**Clinical trials:** A ClinicalTrials.gov query retrieved no ECCL-specific interventional trials; the returned trials were unrelated false matches. (clinical trial search state; no relevant trial context IDs available)

## 13. Prevention
Primary prevention is not currently feasible because ECCL is a sporadic postzygotic mosaic developmental disorder. Secondary/tertiary prevention is implemented as **surveillance and early management of complications** (seizures, hydrocephalus, spinal cord compression, tumor monitoring where indicated). (karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5, koueik2025functionalhemispherectomyfor pages 2-3)

## 14. Other species / natural disease
No naturally occurring non-human ECCL analogs were identified in retrieved sources.

## 15. Model organisms
No ECCL-specific animal models, iPSC-derived models, or organoid models were identified in retrieved sources. Experimental evidence includes **patient-derived fibroblast cell lines** used for functional signaling studies demonstrating activated FGFR/RAS-MAPK signaling. (bennett2016mosaicactivatingmutations pages 1-2)

## Expert opinion / synthesis (authoritative perspectives)
- Moog emphasized strict diagnostic criteria pending molecular clarity and proposed a mosaic autosomal mutation mechanism; subsequent genetics studies support and refine this model by identifying recurrent FGFR1 mosaic activating variants and pathway convergence. (moog2009encephalocraniocutaneouslipomatosis pages 7-8, bennett2016mosaicactivatingmutations pages 1-2)
- Recent expert interpretation expands ECCL from a single-gene hypothesis to a **convergent pathway phenotype** (FGFR1/KRAS activation or NF1 biallelic mosaic inactivation) resulting in an ECCL clinical pattern via RAS-MAPK dysregulation. (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13)

## Artifacts (structured summaries)
| Identifier type | Value | Source | Notes |
|---|---|---|---|
| Disease name | Encephalocraniocutaneous lipomatosis (ECCL) | Machnikowska-Sokołowska et al., 2022; Moog, 2009 (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 1-2) | Rare sporadic neurocutaneous disorder; common abbreviation ECCL. |
| OMIM | #613001 | Machnikowska-Sokołowska et al., 2022 (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2) | Explicitly stated in retrieved source. |
| Orphanet | ORPHA:2396 | Marechal et al., 2024 preprint (marechal2024brafmutantschwanncells pages 1-4) | Explicitly stated in retrieved source; preprint rather than peer-reviewed disease database paper. |
| Synonym | Haberland syndrome | Siddiqui et al., 2017; Garozzo et al., 2018; Moog, 2009 (siddiqui2017encephalocraniocutaneouslipomatosisa pages 1-2, garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 1-2) | Common eponymous synonym used across reviews/case reports. |
| Synonym | Fishman syndrome / Fishman’s syndrome | Siddiqui et al., 2017; Garozzo et al., 2018; Moog, 2009 (siddiqui2017encephalocraniocutaneouslipomatosisa pages 1-2, garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 1-2) | Alternate historical synonym. |
| MONDO ID | Not found in retrieved sources | Retrieved literature only (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, marechal2024brafmutantschwanncells pages 1-4) | Should be verified directly in MONDO/OBO resource. |
| MeSH | Not found in retrieved sources | Retrieved literature only (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, marechal2024brafmutantschwanncells pages 1-4) | Should be verified directly in MeSH. |
| ICD-10 | Not found in retrieved sources | Retrieved literature only (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, marechal2024brafmutantschwanncells pages 1-4) | No explicit ICD-10 code identified in retrieved sources. |
| ICD-11 | Not found in retrieved sources | Retrieved literature only (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, marechal2024brafmutantschwanncells pages 1-4) | No explicit ICD-11 code identified in retrieved sources. |


*Table: This table summarizes the key disease identifiers and synonyms for encephalocraniocutaneous lipomatosis (ECCL) that were explicitly available in the retrieved sources. It is useful for standardizing nomenclature before populating a disease knowledge base entry.*

| Gene/pathway | Variant examples (HGVS protein and c.) | Evidence type/tissue and mosaicism | Mechanistic interpretation | Key citation |
|---|---|---|---|---|
| **FGFR1** | p.Asn546Lys / c.1638C>A; p.Lys656Glu / c.1966A>G | Primary human genetic evidence from affected tissues in ECCL; postzygotic mosaic activating variants detected by exome/targeted resequencing, with low-level/variable allele fractions across lesional tissues and often absent from blood/saliva; hotspot variants also identified in cultured skin/lesional tissue (bennett2016mosaicactivatingmutations pages 1-2, venigalla2025histopathologicfeaturesand pages 5-7) | Canonical activating FGFR1 kinase-domain variants. Bennett et al. showed increased phosphorylated FGFRs and FRS2 with constitutive downstream signaling, supporting **RAS-MAPK pathway activation** as a core ECCL mechanism; explains mosaic neurocutaneous malformation phenotype and overlap with mosaic RASopathies (bennett2016mosaicactivatingmutations pages 1-2, venigalla2025histopathologicfeaturesand pages 5-7) | Bennett 2016; Kordacka 2019 (bennett2016mosaicactivatingmutations pages 1-2, venigalla2025histopathologicfeaturesand pages 5-7) |
| **FGFR1** | p.Asn546Lys / c.1638C>A (reported as N546K) | Human case report with coexisting pilocytic astrocytoma; mutation detected in ECCL patient, with **ddPCR** demonstrating differential low-level mosaic distribution across affected and unaffected tissues, highlighting diagnostic utility of highly sensitive assays for mosaicism (bennett2016mosaicactivatingmutations pages 1-2) | Supports FGFR1 N546K as a plausible causative ECCL variant and reinforces that mosaic distribution can extend beyond overt lesions; also supports link between ECCL molecular etiology and brain tumor predisposition (bennett2016mosaicactivatingmutations pages 1-2) | Kordacka 2019; Bennett 2016 background (bennett2016mosaicactivatingmutations pages 1-2) |
| **KRAS** | Codon 146 hotspot variants (exact nucleotide/protein change not specified in retrieved 2024 excerpt) | Human clinical/tumor-associated evidence; Ferraciolli 2024 describes ECCL as a sporadic **RASopathy** and reports a KRAS codon 146 mutation in an ECCL patient with diffuse leptomeningeal glioneural tumor; broader retrieved literature places codon 146 KRAS variants within mosaic neurocutaneous/RASopathy spectrum overlapping ECCL and related disorders (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3) | Alternative postzygotic activator converging on **RAS-MAPK signaling**; supports molecular heterogeneity of ECCL and a continuum with other mosaic RASopathies rather than a single-gene disorder (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3) | Ferraciolli 2024 (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3) |
| **NF1 / RAS-MAPK** | Germline p.Ser1745* / c.5234C>G plus somatic second hit p.Arg1306* / c.3916C>T on different alleles | Human molecular pathology evidence from blood, cerebral tissue, and jaw giant cell lesions; **early embryonic mosaic biallelic NF1 inactivation** (Happle type 2 / second-hit mosaicism) demonstrated in affected tissues, not explained by FGFR1/KRAS alone (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6) | **Alternate mechanism** for ECCL phenotype: not activating FGFR1/KRAS directly, but producing localized severe **RAS-MAPK upregulation** through loss of neurofibromin. Expands ECCL etiologic spectrum to convergent pathway dysregulation from different mosaic events (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6) | Smeijers 2024 (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6) |
| **RAS-MAPK pathway (downstream convergence)** | Not a single variant; pathway-level convergence downstream of FGFR1/KRAS and via NF1 loss | Functional assay evidence plus clinicogenetic convergence across human cases: FGFR1 activating variants increase receptor phosphorylation/signaling; ECCL-associated mechanisms from FGFR1, KRAS, and NF1 all point to embryonic mosaic dysregulation of the same pathway (bennett2016mosaicactivatingmutations pages 1-2, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6) | Best current model: ECCL is a **mosaic developmental RASopathy** in which early postzygotic alterations in cranial/neural crest–related lineages cause ocular, cutaneous, and CNS malformations; tumor predisposition likely reflects the oncogenic nature of the same pathway lesions (bennett2016mosaicactivatingmutations pages 1-2, ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13) | Bennett 2016; Ferraciolli 2024; Smeijers 2024 (bennett2016mosaicactivatingmutations pages 1-2, ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3, smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13) |


*Table: This table summarizes the main genetic mechanisms currently linked to encephalocraniocutaneous lipomatosis, emphasizing mosaic FGFR1 activation, KRAS codon 146 involvement, and convergent NF1-associated RAS-MAPK dysregulation. It is useful for quickly mapping reported variants, tissue evidence, and mechanistic interpretation for knowledge-base curation.*

| Domain | Phenotype (plain language) | Frequency/statistic | Suggested HPO term(s) | Notes (laterality/onset) |
|---|---|---:|---|---|
| Skin | Nevus psiloliparus (hairless fatty scalp nevus) | 44/54 in Moog 2009; ~80% in Bennett 2016 | HP:0010747 Nevus psiloliparus; HP:0001596 Alopecia | Congenital hallmark lesion; often scalp/frontotemporal; may support definite/probable diagnosis depending on associated criteria (moog2009encephalocraniocutaneouslipomatosis pages 1-2, bennett2016mosaicactivatingmutations pages 1-2) |
| Skin | Subcutaneous fatty masses (frontotemporal/zygomatic region) | 21/54 | HP:0001001 Abnormality of the skin; HP:0012052 Subcutaneous lipoma | Typically craniofacial/frontotemporal; usually congenital and often asymmetric (moog2009encephalocraniocutaneouslipomatosis pages 1-2) |
| Skin | Scarring alopecia from focal scalp aplasia | 14/54 | HP:0200024 Scarring alopecia; HP:0001067 Aplasia cutis congenita | Present from birth/early infancy; may coexist with non-scarring alopecia patches (moog2009encephalocraniocutaneouslipomatosis pages 1-2) |
| Skin/Eye patterning | Bilateral skin and/or eye abnormalities | 22/54 (40%) | HP:0012832 Bilateral; HP:0000621 Abnormality of the eye; HP:0001574 Abnormality of the integument | Although ECCL is often asymmetric/unilateral, bilateral involvement is well documented (moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| Eye | Ocular choristomas / epibulbar or limbal dermoids / lipodermoids | 43/54 in Moog review; ~80% ocular choristomas in Bennett 2016 | HP:0100012 Epibulbar dermoid; HP:0001140 Ocular choristoma | Can be unilateral or bilateral; among the most characteristic ocular findings (bennett2016mosaicactivatingmutations pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 4-4) |
| CNS imaging | Lipomas on neuroimaging (overall) | 33/54 | HP:0012032 Intracranial lipoma; HP:0009721 Spinal lipoma | Lipomas were the most prominent neuroimaging feature in the review cohort (moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| CNS imaging | Intracranial lipomas | 31/54; cerebellopontine angle in 19/31 | HP:0012032 Intracranial lipoma | Frequent posterior fossa/CPA involvement; generally congenital, often ipsilateral to cutaneous/ocular findings (moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| CNS imaging | Intraspinal/spinal lipomas | 12/14 when specifically investigated; ~61% intracranial and intraspinal lipomas in Bennett 2016 | HP:0009721 Spinal lipoma | Spinal MRI is recommended when ECCL is suspected because lesions are common when looked for and may be extensive (moog2009encephalocraniocutaneouslipomatosis pages 5-6, bennett2016mosaicactivatingmutations pages 1-2) |
| CNS imaging | Arachnoid cysts | 21 cases | HP:0006721 Arachnoid cyst | Minor CNS criterion in Moog framework; contributes to asymmetric congenital brain malformation pattern (moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| Neurology | Seizures / epilepsy | 27/54 had seizures; onset among seizure cases: 9 in first month, 7 within first year, 6 after first year; 24/54 not reported | HP:0001250 Seizure; HP:0002373 Febrile seizures not specified / use broad seizure term | About half of reported patients affected; response among 27 seizure cases: 8 refractory, 6 difficult to treat, 13 responded well to medication (moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| Neurodevelopment | Developmental outcome distribution | Among 45 with data: 13 normal, 16 mild delay, 16 moderate-severe/unspecified delay | HP:0011344 Intellectual disability, mild; HP:0001249 Intellectual disability; HP:0001263 Global developmental delay | Roughly two-thirds had normal development or only mild delay; severity did not clearly track extent of CNS malformations (moog2009encephalocraniocutaneouslipomatosis pages 1-2, moog2009encephalocraniocutaneouslipomatosis pages 5-6) |


*Table: This table compiles the best-available quantitative phenotype data for encephalocraniocutaneous lipomatosis from the 54-patient Moog 2009 review, with Bennett 2016 estimates added where available. It is useful for rapid knowledge-base curation of core clinical features, frequencies, laterality, and suggested HPO mappings.*

| Area | Key points | Real-world implementation examples | Suggested ontology terms (MAXO/LOINC/RadLex as applicable) | Key citations |
|---|---|---|---|---|
| Clinical diagnostic criteria | Diagnosis is primarily clinical and syndromic using Moog 2009 revised criteria (Box 1): major/minor findings across eye, skin, CNS, and other systems; major examples include ocular choristoma, proven nevus psiloliparus, intracranial lipoma, and intraspinal lipoma. Definite diagnosis generally requires multi-system involvement with sufficient major criteria; strict criteria were recommended pending molecular clarification. | Use structured assessment of ocular choristoma/dermoid, scalp nevus psiloliparus or patchy alopecia, and CNS lipoma/cyst/atrophy pattern at first specialist evaluation. | MAXO: clinical examination; RadLex: MRI brain, MRI spine, CT head; LOINC: not disease-specific | (moog2009encephalocraniocutaneouslipomatosis pages 6-7, siddiqui2017encephalocraniocutaneouslipomatosisa pages 2-5, moog2009encephalocraniocutaneouslipomatosis media 02ca15fc) |
| Neuroimaging workup | Characteristic imaging findings include intracranial lipomas, intraspinal lipomas, arachnoid cysts, porencephalic cysts, hemispheric atrophy, ventricular asymmetry/hydrocephalus, leptomeningeal angiomatosis, dysplastic cortex, and non-basal-ganglia calcifications. MRI is preferred for brain/spine malformations; CT can better show calcifications. | Brain MRI at diagnosis; spine MRI when ECCL is suspected because spinal lipomas are common when specifically investigated; CT used when cortical calcification pattern needs clarification. | MAXO: MRI surveillance; RadLex: MRI brain, MRI spine, CT head | (siddiqui2017encephalocraniocutaneouslipomatosisa pages 2-5, moog2009encephalocraniocutaneouslipomatosis pages 5-6, karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5, garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 4-5) |
| Molecular diagnosis | Mosaic disease biology means blood/saliva may be negative. Highest-yield testing uses affected tissue (eg, scalp lesion/nevus psiloliparus fibroblasts, lipoma, brain or tumor tissue) with high-depth sequencing; recurrent FGFR1 variants include p.Asn546Lys and p.Lys656Glu, and KRAS codon 146 variants are established in the ECCL spectrum. ddPCR and other sensitive methods improve low-level mosaic detection. | Sequence affected tissue rather than relying only on blood; ddPCR detected FGFR1 N546K mosaicism across tissues in a patient with ECCL and pilocytic astrocytoma. | MAXO: genetic testing; LOINC: molecular genetics study; RadLex: image-guided biopsy if needed | (kordacka2019sensitivedetectionof pages 1-2, bennett2016mosaicactivatingmutations pages 1-2, venigalla2025histopathologicfeaturesand pages 5-7, garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 4-5) |
| Multidisciplinary surveillance | Ongoing care should involve ophthalmology, dermatology, neurology/neurosurgery, radiology, neurodevelopmental/rehabilitation services, and musculoskeletal assessment. Surveillance is recommended because ECCL can be associated with epilepsy, hydrocephalus, spinal cord compression, and tumor predisposition. | Multisystem evaluation after diagnosis; serial developmental follow-up and repeat brain/spine imaging when clinically indicated; literature recommends close clinical and radiologic follow-up. | MAXO: multidisciplinary care; MAXO: MRI surveillance; MAXO: neurodevelopmental assessment | (koueik2025functionalhemispherectomyfor pages 2-3, koueik2025functionalhemispherectomyfor pages 3-5, karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5, ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3) |
| Antiseizure therapy | There is no disease-specific drug therapy for ECCL; seizure treatment is symptomatic. About half of patients have seizures, with a subset having refractory epilepsy. | Reported antiseizure medications include levetiracetam, zonisamide, valproate, and clobazam in a child later treated surgically for drug-refractory epilepsy. | MAXO: antiseizure medication therapy | (koueik2025functionalhemispherectomyfor pages 2-3, siddiqui2017encephalocraniocutaneouslipomatosisa pages 5-5, moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| Hydrocephalus management | Hydrocephalus occurs in a substantial minority; some patients require neurosurgical CSF diversion. | Ventriculoperitoneal shunt placement is specifically recommended/used for symptomatic hydrocephalus in case-based literature. | MAXO: neurosurgical shunt procedure | (karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5, siddiqui2017encephalocraniocutaneouslipomatosisa pages 2-5) |
| Spinal lipoma management | Spinal lipomas are common when sought and may cause tethered cord or compression; treatment is symptom-driven. | Debulking of spinal lipomas is described for cord compression/tethered cord symptoms. | MAXO: surgical debulking; MAXO: spinal surgery | (karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5, moog2009encephalocraniocutaneouslipomatosis pages 5-6) |
| Conservative monitoring | Many lesions are static, so watchful waiting with serial imaging is appropriate when surgery risks outweigh benefit. | In an infant with enlarging orbital/retrobulbar dermoids and intracranial lipomas, a multidisciplinary team chose close monitoring with serial MRIs and reserved surgery for airway compression or neurologic deficits. | MAXO: MRI surveillance; MAXO: expectant management | (subbiah2022encephalocraniocutaneouslipomatosisa pages 1-2) |
| Ocular symptomatic management | Ocular disease can include choristomas/dermoids, secondary glaucoma, exposure symptoms, and progressive surface compromise; management is individualized. | Topical timolol was used for secondary glaucoma; temporary tarsorrhaphy was used for lagophthalmos in an ECCL infant. | MAXO: ophthalmic drug therapy; MAXO: tarsorrhaphy; MAXO: glaucoma management | (subbiah2022encephalocraniocutaneouslipomatosisa pages 1-2) |
| Cosmetic / lesion-directed surgery | Cutaneous and ocular lesions may be surgically corrected for symptoms or cosmesis; surgery is individualized because some lesions are extensive and non-urgent. | Surgical correction of ocular or cutaneous lesions is described in reviews/case reports; cosmetic improvement is a typical indication. | MAXO: surgical excision; MAXO: reconstructive surgery | (siddiqui2017encephalocraniocutaneouslipomatosisa pages 5-5, karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5) |
| Epilepsy surgery | For unilateral hemispheric drug-refractory epilepsy with concordant presurgical data, hemispherectomy/hemispheric disconnection is feasible. | A 5-year-old with ECCL underwent left peri-insular functional hemispherectomy after failed medications; she was seizure free (Engel class IA) at 2.5 years, ambulatory with orthotic assistance by 3 months, and had neuropsychological improvement at 1.5 years. | MAXO: hemispherectomy; MAXO: epilepsy surgery; RadLex: video-EEG, fMRI, PET-MRI | (koueik2025functionalhemispherectomyfor pages 2-3, koueik2025functionalhemispherectomyfor pages 1-2, koueik2025functionalhemispherectomyfor pages 5-6) |
| Targeted therapy / tumor management | ECCL is a mosaic RAS/MAPK-pathway disorder and tumor predisposition syndrome; targeted therapy evidence is limited to case reports. | In a child with progressive pilocytic astrocytoma and mosaic FGFR1 p.Lys656Glu, off-label trametinib (MEK inhibitor) was started after progression on vinblastine, carboplatin/vincristine, and irinotecan/bevacizumab, with stable tumor size at 6 months. | MAXO: targeted small-molecule therapy; MAXO: MEK inhibitor therapy | (bavle2018encephalocraniocutaneouslipomatosis. pages 1-2) |


*Table: This table summarizes the best-supported diagnostic and management practices for encephalocraniocutaneous lipomatosis, including Moog diagnostic criteria, imaging, mosaic genetic testing, surveillance, and reported real-world treatments. It is useful for translating case-series and primary literature into structured knowledge-base entries with ontology-ready actions.*

## Key figures/tables from retrieved literature
Moog 2009 revised diagnostic criteria (Box 1) were retrieved as an image crop. (moog2009encephalocraniocutaneouslipomatosis media 02ca15fc)

## Reference metadata (publication dates and URLs from retrieved sources)
- Moog U. *Journal of Medical Genetics*. 2009-07. https://doi.org/10.1136/jmg.2009.066068 (moog2009encephalocraniocutaneouslipomatosis pages 1-2)
- Bennett JT et al. *American Journal of Human Genetics*. 2016-03. https://doi.org/10.1016/j.ajhg.2016.02.006 (bennett2016mosaicactivatingmutations pages 1-2)
- Kordacka J et al. *American Journal of Medical Genetics Part A*. 2019-08. https://doi.org/10.1002/ajmg.a.61256 (kordacka2019sensitivedetectionof pages 1-2)
- Machnikowska-Sokołowska M et al. *Brain Sciences*. 2022-11. https://doi.org/10.3390/brainsci12121641 (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2)
- Subbiah D et al. *Cureus*. 2022-12. https://doi.org/10.7759/cureus.32498 (subbiah2022encephalocraniocutaneouslipomatosisa pages 1-2)
- Ferraciolli SF et al. *Clinical Neuroradiology*. 2024-02. https://doi.org/10.1007/s00062-024-01389-0 (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3)
- Smeijers S et al. *Journal of Medical Genetics*. 2024-06. https://doi.org/10.1136/jmg-2023-109785 (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6)
- Koueik J et al. *Journal of Neurosurgery: Case Lessons*. 2025-04. https://doi.org/10.3171/case2578 (koueik2025functionalhemispherectomyfor pages 2-3)

## Requested items not available in retrieved evidence (transparent gaps)
- MONDO ID, MeSH identifier, ICD-10/ICD-11 codes: not explicitly present in tool-retrieved full texts. (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2, marechal2024brafmutantschwanncells pages 1-4)
- Population prevalence/incidence and quantitative malignancy risk estimates: not found in retrieved evidence (case-based literature predominates). (moog2009encephalocraniocutaneouslipomatosis pages 7-8, garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 1-2)


References

1. (bennett2016mosaicactivatingmutations pages 1-2): James T. Bennett, Tiong Yang Tan, Diana Alcantara, Martine Tétrault, Andrew E. Timms, Dana Jensen, Sarah Collins, Malgorzata J.M. Nowaczyk, Marjorie J. Lindhurst, Katherine M. Christensen, Stephen R. Braddock, Heather Brandling-Bennett, Raoul C.M. Hennekam, Brian Chung, Anna Lehman, John Su, SuYuen Ng, David J. Amor, Jacek Majewski, Les G. Biesecker, Kym M. Boycott, William B. Dobyns, Mark O’Driscoll, Ute Moog, and Laura M. McDonell. Mosaic activating mutations in fgfr1 cause encephalocraniocutaneous lipomatosis. American journal of human genetics, 98 3:579-587, Mar 2016. URL: https://doi.org/10.1016/j.ajhg.2016.02.006, doi:10.1016/j.ajhg.2016.02.006. This article has 121 citations and is from a highest quality peer-reviewed journal.

2. (moog2009encephalocraniocutaneouslipomatosis pages 1-2): U. Moog. Encephalocraniocutaneous lipomatosis. Journal of Medical Genetics, 46:721-729, Jul 2009. URL: https://doi.org/10.1136/jmg.2009.066068, doi:10.1136/jmg.2009.066068. This article has 159 citations and is from a domain leading peer-reviewed journal.

3. (moog2009encephalocraniocutaneouslipomatosis pages 5-6): U. Moog. Encephalocraniocutaneous lipomatosis. Journal of Medical Genetics, 46:721-729, Jul 2009. URL: https://doi.org/10.1136/jmg.2009.066068, doi:10.1136/jmg.2009.066068. This article has 159 citations and is from a domain leading peer-reviewed journal.

4. (machnikowskasokołowska2022encephalocraniocutaneouslipomatosisa pages 1-2): Magdalena Machnikowska-Sokołowska, Piotr Fabrowicz, Jacek Pilch, Weronika Roesler, Mikołaj Kuźniak, Katarzyna Gruszczyńska, and Justyna Paprocka. Encephalocraniocutaneous lipomatosis, a radiological challenge: two atypical case reports and literature review. Brain Sciences, 12:1641, Nov 2022. URL: https://doi.org/10.3390/brainsci12121641, doi:10.3390/brainsci12121641. This article has 3 citations.

5. (marechal2024brafmutantschwanncells pages 1-4): Elise Marechal, Patrice Quintana, Daniel Aldea, Grégoire Mondielli, Nathalie Bernard-Marissal, Mathias Moreno, Valérie Delague, Lauren A. Weiss, Anne Barlier, and Heather C. Etchevers. <i>braf</i>-mutant schwann cells divert to a repair phenotype to induce congenital demyelinating neuropathy. BioRxiv, Apr 2024. URL: https://doi.org/10.1101/2024.04.24.590951, doi:10.1101/2024.04.24.590951. This article has 1 citations.

6. (siddiqui2017encephalocraniocutaneouslipomatosisa pages 1-2): Shaista Siddiqui, Shazia Naaz, Mehtab Ahmad, Zafar Ahmad Khan, Shagufta Wahab, and Basmah Abdur Rashid. Encephalocraniocutaneous lipomatosis: a case report with review of literature. The Neuroradiology Journal, 30:578-582, Jul 2017. URL: https://doi.org/10.1177/1971400917693638, doi:10.1177/1971400917693638. This article has 10 citations and is from a peer-reviewed journal.

7. (ferraciolli2024haberlandsyndrome(encephalocraniocutaneous pages 1-3): Suely Fazio Ferraciolli, Mario Tortora, Luis Felipe de Souza Godoy, Yuri Reis Casal, and Leandro Tavares Lucato. Haberland syndrome (encephalocraniocutaneous lipomatosis) with development of diffuse leptomeningeal glioneural tumor (dl-gnt) during adolescence. Clinical neuroradiology, 34:973-976, Feb 2024. URL: https://doi.org/10.1007/s00062-024-01389-0, doi:10.1007/s00062-024-01389-0. This article has 2 citations and is from a peer-reviewed journal.

8. (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 9-13): Steven Smeijers, Hilde Brems, Alexander Verhaeghe, Wim van Paesschen, Johannes van Loon, Seppe Van der Auweraer, Raf Sciot, Dietmar Rudolf Thal, Lieven Lagae, Eric Legius, and Tom Theys. Encephalocraniocutaneous lipomatosis phenotype associated with mosaic biallelic pathogenic variants in the<i>nf1</i>gene. Journal of Medical Genetics, 61:904-907, Jun 2024. URL: https://doi.org/10.1136/jmg-2023-109785, doi:10.1136/jmg-2023-109785. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (smeijers2024encephalocraniocutaneouslipomatosisphenotype pages 1-6): Steven Smeijers, Hilde Brems, Alexander Verhaeghe, Wim van Paesschen, Johannes van Loon, Seppe Van der Auweraer, Raf Sciot, Dietmar Rudolf Thal, Lieven Lagae, Eric Legius, and Tom Theys. Encephalocraniocutaneous lipomatosis phenotype associated with mosaic biallelic pathogenic variants in the<i>nf1</i>gene. Journal of Medical Genetics, 61:904-907, Jun 2024. URL: https://doi.org/10.1136/jmg-2023-109785, doi:10.1136/jmg-2023-109785. This article has 1 citations and is from a domain leading peer-reviewed journal.

10. (moog2009encephalocraniocutaneouslipomatosis pages 7-8): U. Moog. Encephalocraniocutaneous lipomatosis. Journal of Medical Genetics, 46:721-729, Jul 2009. URL: https://doi.org/10.1136/jmg.2009.066068, doi:10.1136/jmg.2009.066068. This article has 159 citations and is from a domain leading peer-reviewed journal.

11. (moog2009encephalocraniocutaneouslipomatosis pages 4-4): U. Moog. Encephalocraniocutaneous lipomatosis. Journal of Medical Genetics, 46:721-729, Jul 2009. URL: https://doi.org/10.1136/jmg.2009.066068, doi:10.1136/jmg.2009.066068. This article has 159 citations and is from a domain leading peer-reviewed journal.

12. (kordacka2019sensitivedetectionof pages 1-2): Joanna Kordacka, Krzysztof Zakrzewski, Renata Gruszka, Monika Witusik‐Perkowska, Joanna Taha, Beata Sikorska, Paweł P. Liberski, and Magdalena Zakrzewska. Sensitive detection of fgfr1 n546k mosaic mutation in patient with encephalocraniocutaneous lipomatosis and pilocytic astrocytoma. American Journal of Medical Genetics Part A, 179:1622-1627, Aug 2019. URL: https://doi.org/10.1002/ajmg.a.61256, doi:10.1002/ajmg.a.61256. This article has 15 citations.

13. (siddiqui2017encephalocraniocutaneouslipomatosisa pages 2-5): Shaista Siddiqui, Shazia Naaz, Mehtab Ahmad, Zafar Ahmad Khan, Shagufta Wahab, and Basmah Abdur Rashid. Encephalocraniocutaneous lipomatosis: a case report with review of literature. The Neuroradiology Journal, 30:578-582, Jul 2017. URL: https://doi.org/10.1177/1971400917693638, doi:10.1177/1971400917693638. This article has 10 citations and is from a peer-reviewed journal.

14. (garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 1-2): Maria Garozzo, Daniele Attardo, Pierluigi Smilari, Filippo Greco, Agata Fiumara, Agata Polizzi, Concetta Pirrone, Antonio Zanghì, Carmelo Schepis, Francesco Lacarrubba, Giuseppe Micali, Martino Ruggieri, Andrea Praticò, and Marina Mazzurco. Encephalocraniocutaneous lipomatosis (haberland syndrome or fishman syndrome). Journal of Pediatric Neurology, 16:369-378, Aug 2018. URL: https://doi.org/10.1055/s-0038-1667004, doi:10.1055/s-0038-1667004. This article has 2 citations and is from a peer-reviewed journal.

15. (moog2009encephalocraniocutaneouslipomatosis pages 6-7): U. Moog. Encephalocraniocutaneous lipomatosis. Journal of Medical Genetics, 46:721-729, Jul 2009. URL: https://doi.org/10.1136/jmg.2009.066068, doi:10.1136/jmg.2009.066068. This article has 159 citations and is from a domain leading peer-reviewed journal.

16. (moog2009encephalocraniocutaneouslipomatosis media 02ca15fc): U. Moog. Encephalocraniocutaneous lipomatosis. Journal of Medical Genetics, 46:721-729, Jul 2009. URL: https://doi.org/10.1136/jmg.2009.066068, doi:10.1136/jmg.2009.066068. This article has 159 citations and is from a domain leading peer-reviewed journal.

17. (venigalla2025histopathologicfeaturesand pages 5-7): Siddharth Venigalla, Tanvir K. Dhaliwal, Anvita Anumolu, Lena Rafey, Arturo P. Saavedra, and David D. Limbrick. Histopathologic features and molecular markers of encephalocraniocutaneous lipomatosis (eccl). Dermatopathology, 12:39, Nov 2025. URL: https://doi.org/10.3390/dermatopathology12040039, doi:10.3390/dermatopathology12040039. This article has 0 citations.

18. (siddiqui2017encephalocraniocutaneouslipomatosisa pages 5-5): Shaista Siddiqui, Shazia Naaz, Mehtab Ahmad, Zafar Ahmad Khan, Shagufta Wahab, and Basmah Abdur Rashid. Encephalocraniocutaneous lipomatosis: a case report with review of literature. The Neuroradiology Journal, 30:578-582, Jul 2017. URL: https://doi.org/10.1177/1971400917693638, doi:10.1177/1971400917693638. This article has 10 citations and is from a peer-reviewed journal.

19. (karaman2021encephalocraniocutaneouslipomatosıs(haberland pages 4-5): Zehra Filiz Karaman and Şerife Ebru Özüdoğru. Encephalocraniocutaneous lipomatosıs (haberland syndrome) in a newborn baby: a case report with review of literature. Child's Nervous System, 37:3951-3955, Mar 2021. URL: https://doi.org/10.1007/s00381-021-05099-7, doi:10.1007/s00381-021-05099-7. This article has 4 citations.

20. (koueik2025functionalhemispherectomyfor pages 2-3): Joyce Koueik, David Hsu, Jeffrey Helgager, and Raheel Ahmed. Functional hemispherectomy for seizure control in encephalocraniocutaneous lipomatosis: illustrative case. Journal of Neurosurgery: Case Lessons, Apr 2025. URL: https://doi.org/10.3171/case2578, doi:10.3171/case2578. This article has 0 citations.

21. (subbiah2022encephalocraniocutaneouslipomatosisa pages 1-2): Deivanai Subbiah, Nur Hafidza Asiff, Norhafizah Hamzah, and Amir Samsudin. Encephalocraniocutaneous lipomatosis: a case report and literature review. Cureus, Dec 2022. URL: https://doi.org/10.7759/cureus.32498, doi:10.7759/cureus.32498. This article has 2 citations.

22. (bavle2018encephalocraniocutaneouslipomatosis. pages 1-2): Abhishek Bavle, Rikin Shah, Naina Gross, Theresa Gavula, Alejandro Ruiz-Elizalde, Klaas Wierenga, and Rene McNall-Knapp. Encephalocraniocutaneous lipomatosis. Journal of pediatric hematology/oncology, 40 7:553-554, Oct 2018. URL: https://doi.org/10.1097/mph.0000000000001170, doi:10.1097/mph.0000000000001170. This article has 22 citations.

23. (garozzo2018encephalocraniocutaneouslipomatosis(haberland pages 4-5): Maria Garozzo, Daniele Attardo, Pierluigi Smilari, Filippo Greco, Agata Fiumara, Agata Polizzi, Concetta Pirrone, Antonio Zanghì, Carmelo Schepis, Francesco Lacarrubba, Giuseppe Micali, Martino Ruggieri, Andrea Praticò, and Marina Mazzurco. Encephalocraniocutaneous lipomatosis (haberland syndrome or fishman syndrome). Journal of Pediatric Neurology, 16:369-378, Aug 2018. URL: https://doi.org/10.1055/s-0038-1667004, doi:10.1055/s-0038-1667004. This article has 2 citations and is from a peer-reviewed journal.

24. (koueik2025functionalhemispherectomyfor pages 3-5): Joyce Koueik, David Hsu, Jeffrey Helgager, and Raheel Ahmed. Functional hemispherectomy for seizure control in encephalocraniocutaneous lipomatosis: illustrative case. Journal of Neurosurgery: Case Lessons, Apr 2025. URL: https://doi.org/10.3171/case2578, doi:10.3171/case2578. This article has 0 citations.

25. (koueik2025functionalhemispherectomyfor pages 1-2): Joyce Koueik, David Hsu, Jeffrey Helgager, and Raheel Ahmed. Functional hemispherectomy for seizure control in encephalocraniocutaneous lipomatosis: illustrative case. Journal of Neurosurgery: Case Lessons, Apr 2025. URL: https://doi.org/10.3171/case2578, doi:10.3171/case2578. This article has 0 citations.

26. (koueik2025functionalhemispherectomyfor pages 5-6): Joyce Koueik, David Hsu, Jeffrey Helgager, and Raheel Ahmed. Functional hemispherectomy for seizure control in encephalocraniocutaneous lipomatosis: illustrative case. Journal of Neurosurgery: Case Lessons, Apr 2025. URL: https://doi.org/10.3171/case2578, doi:10.3171/case2578. This article has 0 citations.
