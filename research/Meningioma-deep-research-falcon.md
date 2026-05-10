---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T12:09:06.362419'
end_time: '2026-05-09T12:23:22.829197'
duration_seconds: 856.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Meningioma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Meningioma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Meningioma** covering all of the
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
- **Disease Name:** Meningioma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Meningioma** covering all of the
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


# Meningioma (Neoplastic) — Disease Characteristics Research Report (2023–2024 emphasis)

## Executive summary
Meningiomas are the most common primary intracranial tumors in adults and comprise the majority of non‑malignant primary brain/CNS tumors in US registry data. Contemporary disease management is increasingly driven by integrated histology plus molecular profiling, particularly DNA‑methylation classes and specific high‑risk alterations (TERT promoter mutation; CDKN2A/B loss) that are now incorporated into WHO grading. Standard-of-care remains local therapy (surgery ± radiotherapy), while **no FDA‑approved systemic therapy** exists for aggressive/recurrent disease; multiple molecularly stratified targeted, immunotherapy, and radionuclide trials are ongoing. (wang2024meningiomainternationalconsortium pages 4-4, deng2022moleculardiagnosisand pages 1-2, lotsch2024themolecularand pages 1-2)

| Domain | Key points | Quantitative highlights | Source / URL / date | Evidence |
|---|---|---|---|---|
| Definition & classification | Meningioma is the most common primary intracranial tumor in adults and a single WHO CNS tumor type with 15 histologic subtypes. WHO CNS5 (2021) grades meningiomas as CNS WHO grades 1–3; grade 3 can be assigned by molecular criteria even without classic anaplastic histology when **TERT promoter mutation** or **CDKN2A/B homozygous deletion** is present. Most cases are grade 1; grade 2–3 comprise the more aggressive subset. | ~80% grade 1; up to ~20% grade 2/3. WHO 2021 added **TERTp mutation** and **CDKN2A/B homozygous deletion** as grade 3 criteria. | Louis et al., *Neuro-Oncology* Jun 2021, https://doi.org/10.1093/neuonc/noab106; Deng et al., *Chinese Medical Journal* Sep 2022, https://doi.org/10.1097/cm9.0000000000002391; Torp et al., *Acta Neurochirurgica* Jul 2022, https://doi.org/10.1007/s00701-022-05301-y | (deng2022moleculardiagnosisand pages 1-2, torp2022thewho2021 pages 7-9) |
| Epidemiology | Recent US registry data show meningioma dominates the nonmalignant CNS tumor burden. Figure-based CBTRUS/consensus data indicate higher incidence in females and in Black individuals relative to several comparison groups. Risk rises with age. | Nonmalignant distribution: **meningiomas 56.2%** of nonmalignant primary brain tumors. All primary brain tumors: **5-year total 453,623; annual average 90,725**. Nonmalignant tumors: **5-year total 326,894; annual average 65,379**. Earlier CBTRUS series: meningioma **39.0% of all tumors** and **54.5% of nonmalignant tumors**. | Price et al., CBTRUS report, *Neuro-Oncology* Oct 2024, https://doi.org/10.1093/neuonc/noae145; Wang et al., *Neuro-Oncology* May 2024, https://doi.org/10.1093/neuonc/noae082; Wang et al., *Adv Exp Med Biol* Jan 2023, https://doi.org/10.1007/978-3-031-29750-2_11 | (wang2024meningiomainternationalconsortium pages 4-4, wang2024meningiomainternationalconsortium media 5c0c850b, wang2023genomiclandscapeof pages 1-2) |
| Molecular drivers | Canonical split is **NF2-mutant** versus **non-NF2** meningioma. NF2 alteration is the dominant event in sporadic disease; non-NF2 tumors are enriched for **TRAF7, KLF4, AKT1, SMO, PIK3CA, POLR2A** and often correlate with skull-base location / specific histologies. | **NF2** altered in ~40–60% (up to ~60%) of sporadic cases. Approximate non-NF2 frequencies: **TRAF7 20–25%**, **KLF4 10–15%**, **AKT1 ~10%**, **SMO 1–5%**, **PIK3CA ~5%**. | Wang et al., *J Neuro-Oncol* Jan 2023, https://doi.org/10.1007/s11060-023-04253-2; Hsieh et al., *Cancer* May 2024, https://doi.org/10.1002/cncr.35279; Lotsch et al., *IJMS* Sep 2024, https://doi.org/10.3390/ijms25179631 | (wang2023themultiomiclandscape pages 1-2, hsieh2024evolvingconceptsin pages 1-3, lotsch2024themolecularand pages 2-4) |
| Molecular subgroups & CNVs | Contemporary methylation/integrated classifications identify biologically meaningful subgroups. One widely used framework recognizes **Immunogenic**, **NF2-wild-type**, **Hypermetabolic**, and **Proliferative** groups; aggressive groups carry greater chromosomal instability. Recurrent CNVs include losses of **22q, 1p, 14q** and, in more aggressive tumors, additional losses such as **10, 18**. | Hypermetabolic/Proliferative tumors show higher CNV burden with losses including **1p, 10, 14, 18, 22q**. WHO grade 2/3 tumors have more genomic disruption than grade 1. | Wang et al., *Nature Medicine* Aug 2024, https://doi.org/10.1038/s41591-024-03167-4; Lotsch et al., *IJMS* Sep 2024, https://doi.org/10.3390/ijms25179631; Marastoni & Barresi, *Cancers* May 2023, https://doi.org/10.3390/cancers15112945 | (wang2024molecularclassificationto pages 1-2, lotsch2024themolecularand pages 2-4, marastoni2023meningiomagradingbeyond pages 1-2) |
| Prognostic biomarkers: TERTp | TERT promoter mutation is a high-risk biomarker enriched in higher-grade/aggressive meningiomas and now incorporated into WHO grade 3 criteria. | TERTp mutation frequency reported as **4.7% in WHO 1**, **7.9% in WHO 2**, **15.4% in WHO 3**; associated PFS **14 months vs 101 months** for TERTp-mutant vs wild-type. | Lotsch et al., *IJMS* Sep 2024, https://doi.org/10.3390/ijms25179631 | (lotsch2024themolecularand pages 2-4) |
| Prognostic biomarkers: CDKN2A/B | CDKN2A/B deletion is strongly associated with progression and poor PFS; homozygous loss is a WHO grade 3 criterion, while even heterozygous loss may be adverse. | Overall prevalence of **homozygous CDKN2A/B deletion 4.9%**. Median PFS: **180.0 months** (WT) vs **26.1 months** (heterozygous deletion) vs **11.0 months** (homozygous deletion). Meta-analysis HR for progression: **5.5** (heterozygous) and **8.4** (homozygous). | Wach et al., *Acta Neuropathol Commun* Nov 2023, https://doi.org/10.1186/s40478-023-01690-y; Lotsch et al., *IJMS* Sep 2024, https://doi.org/10.3390/ijms25179631 | (lotsch2024themolecularand pages 2-4, bhala2021incidenceofbenign pages 3-3) |
| Prognostic biomarkers: grade 2 integrated risk | DNA methylation/copy-number/TERTp-integrated risk stratification refines recurrence prediction in histologic grade 2 disease beyond morphology alone. | In a grade 2 cohort (n=100), local control **84.3% at 2 y**, **68.5% at 4 y**, **50.8% at 6 y**; integrated risk HR for local recurrence: **9.91** (intermediate) and **7.29** (high) vs low-risk; **GTR HR 0.19** for local progression. | Ehret et al., *Acta Neuropathol Commun* May 2024, https://doi.org/10.1186/s40478-024-01739-6 | (marastoni2023meningiomagradingbeyond pages 1-2) |
| Prognostic biomarkers: surgery / Simpson | Extent of resection remains a major real-world prognostic factor across molecular groups. Dural margin treatment matters. | Nature Medicine 2024 matched analysis: subtotal resection vs GTR associated with worse PFS **HR 2.02**; Simpson grade 3 vs Simpson 1/2 associated with shorter time to recurrence **HR 1.64**. | Wang et al., *Nature Medicine* Aug 2024, https://doi.org/10.1038/s41591-024-03167-4 | (wang2024molecularclassificationto pages 1-2) |
| Diagnostic / phenotypic notes | MRI is the preferred imaging modality; meningiomas usually show avid gadolinium enhancement and often a dural tail. CT helps detect calcification and skull-base bone changes. Many present with mass effect symptoms or seizures; edema can be substantial in selected subtypes. | Dural tail reported in **up to 72%**; calcification on non-contrast CT in **up to 25%**; perilesional edema in roughly **50%**. | Wang et al., *Neuro-Oncology* May 2024, https://doi.org/10.1093/neuonc/noae082; Pacult et al., *Cancers* May 2024, https://doi.org/10.3390/cancers16111978 | (wang2024meningiomainternationalconsortium pages 14-14, pacult2024surgicalmanagementof pages 1-2) |
| Systemic therapy status | Standard management remains surgery ± radiotherapy. No systemic therapy is established as routine standard; no FDA-approved systemic therapy is available for aggressive meningioma. Molecularly guided therapy, immunotherapy, and radionuclide therapy are active investigation areas. | EANO: no target achieved ESCAT I; systemic/radioligand approaches remain investigational. | Reifenberger et al., EANO guideline 2024; Lotsch et al., *IJMS* Sep 2024, https://doi.org/10.3390/ijms25179631; Hsieh et al., *Cancer* May 2024, https://doi.org/10.1002/cncr.35279 | (reifenberger2024eanoguidelineon pages 4-5, lotsch2024themolecularand pages 1-2, hsieh2024evolvingconceptsin pages 10-11, reifenberger2024eanoguidelineon pages 3-4, reifenberger2024eanoguidelineon pages 20-21) |
| Example trial: Alliance A071401 | Molecularly stratified phase II platform for progressive meningioma. Arms are matched to pathway alterations. | **NCT02523014**; arms: **vismodegib** (SMO/PTCH1), **GSK2256098** (FAK; NF2), **capivasertib** (AKT1/PIK3CA/PTEN), **abemaciclib** (CDK pathway). Primary endpoint: **6-month PFS**. Status: recruiting record with no posted results in retrieved excerpt. | ClinicalTrials.gov record (Alliance for Clinical Trials in Oncology), 2015, https://clinicaltrials.gov/study/NCT02523014 | (NCT02523014 chunk 1) |
| Example trial: pembrolizumab | Phase II single-arm immunotherapy for recurrent or residual high-grade meningioma. | **NCT03279692**; pembrolizumab q3 weeks; primary endpoint **PFS at 6 months**; enrollment **26**; results first posted **2023-06-06** in registry metadata. | ClinicalTrials.gov record (Massachusetts General Hospital), 2017, https://clinicaltrials.gov/study/NCT03279692 | (NCT03279692 chunk 1, NCT03279692 chunk 2) |
| Example trial: nivolumab ± ipilimumab | Phase II immunotherapy study in recurrent/progressive meningioma. | **NCT02648997**; nivolumab alone or nivolumab + ipilimumab after RT; actual enrollment **40**; primary endpoint **6-month non-progression**; secondary endpoints include median PFS, OS, ORR, CTCAE AEs. | ClinicalTrials.gov record (Dana-Farber), 2016, https://clinicaltrials.gov/study/NCT02648997 | (NCT02648997 chunk 1, NCT02648997 chunk 3) |
| Example trials: radionuclide therapy | SSTR2-targeted theranostics are emerging for recurrent/progressive disease. | **NCT06326190** (EORTC/LUMEN-1 mentioned in EANO context) and **NCT06955169 MOMENTUM-1** compare/assess **[177Lu]Lu-DOTATATE** in SSTR2-positive recurrent/progressive meningioma; MOMENTUM-1 randomizes against local SOC and uses **PFS** as primary endpoint. | EANO guideline 2024; ClinicalTrials.gov, 2024–2025, https://clinicaltrials.gov/study/NCT06326190 and https://clinicaltrials.gov/study/NCT06955169 | (reifenberger2024eanoguidelineon pages 12-12, NCT06955169 chunk 1) |
| Example trial: combination targeted radionuclide + mTOR inhibitor | Combination strategy for refractory higher-grade meningioma. | **NCT06126588 (ELUMEN)**; **everolimus + 177Lu-DOTATATE** in refractory **WHO grade 2–3** meningioma; primary endpoint **PFS at 7 months**; planned enrollment **28**. | ClinicalTrials.gov record (Central Hospital, Nancy, France), 2024, https://clinicaltrials.gov/study/NCT06126588 | (NCT06126588 chunk 1) |


*Table: This table compacts the most actionable current evidence on meningioma classification, epidemiology, molecular biology, prognosis, and investigational systemic therapies. It is designed as a quick-reference artifact for building a disease knowledge base entry with traceable citations.*

---

## 1. Disease information
### 1.1 Definition and overview
Meningiomas arise from the meninges and are typically slow growing, but a clinically important subset behaves aggressively and recurs despite therapy. A 2024 consensus review notes that “Meningiomas are the most common primary intracranial tumors in adults” and that incidence is increasing with aging and increased neuroimaging utilization. (wang2024meningiomainternationalconsortium pages 4-4)

### 1.2 Classification and grading (current understanding)
The WHO CNS5 (2021) framework treats meningioma as a single tumor type with multiple histologic subtypes and assigns **CNS WHO grades 1–3** based on histopathologic features and select molecular criteria. (torp2022thewho2021 pages 7-9, deng2022moleculardiagnosisand pages 1-2)

Key grading points captured in recent sources:
- WHO CNS5 recognizes **15 histological subtypes**, with grade assignment reflecting subtype and malignancy features. (torp2022thewho2021 pages 7-9)
- Chordoid and clear cell meningiomas are assigned grade 2 due to higher recurrence risk; anaplastic meningioma is grade 3. (torp2022thewho2021 pages 7-9)
- Importantly, WHO CNS5 integrates molecular markers into grading; a 2022 expert consensus summarizes that tumors “harboring TERT promoter mutation and/or CDKN2A/B homozygous deletion are allotted to WHO grade 3 regardless of histologic anaplasia.” (deng2022moleculardiagnosisand pages 1-2)

**Direct abstract quote (grading biomarker integration):** The 2023 review on grading beyond histopathology states: “The grading system established by the World Health Organization has recently included pTERT mutations and CDKN2A/B homozygous deletions as criteria for grade 3…” (marastoni2023meningiomagradingbeyond pages 1-2)

### 1.3 Key identifiers (ontology/terminology)
Within the retrieved evidence for this run, authoritative cross‑ontology identifiers (e.g., MONDO ID, MeSH descriptor code, ICD‑10/ICD‑11 codes, Orphanet) were not directly available as citable text. Consequently, I do not assert specific identifier values without additional retrieval of those controlled‑vocabulary resources.

### 1.4 Synonyms / alternative names
High‑grade meningiomas are often referred to clinically as **“atypical” (WHO grade 2)** and **“anaplastic/malignant” (WHO grade 3)** meningiomas. (pacult2024surgicalmanagementof pages 1-2)

### 1.5 Evidence source type
The report integrates evidence from:
- Aggregated disease-level resources (registry/CBTRUS analyses; consensus reviews). (wang2024meningiomainternationalconsortium pages 4-4, wang2023genomiclandscapeof pages 1-2)
- Human clinical cohorts (molecular prognostic cohorts; surgical/radiation outcome cohorts). (wang2024molecularclassificationto pages 1-2, marastoni2023meningiomagradingbeyond pages 1-2)
- ClinicalTrials.gov trial records. (NCT02523014 chunk 1, NCT03279692 chunk 1, NCT02648997 chunk 1, NCT06955169 chunk 1, NCT06126588 chunk 1)

---

## 2. Etiology
### 2.1 Causal factors and mechanisms (high-level)
Meningioma development is driven by recurrent somatic alterations that define molecular subgroups and influence anatomic distribution and phenotype (e.g., NF2‑driven versus non‑NF2‑driven disease). (wang2023themultiomiclandscape pages 1-2, torp2022thewho2021 pages 7-9)

### 2.2 Risk factors
- **Ionizing radiation:** A SEER‑focused epidemiology analysis states: “The only currently established environmental risk factor is ionizing radiation.” (bhala2021incidenceofbenign pages 3-3)
- **Age and sex:** Risk increases with age and is higher in females for largely non‑malignant lesions; sex differences are also supported by registry‑derived figures in the 2024 consensus epidemiology figure. (bhala2021incidenceofbenign pages 3-3, wang2024meningiomainternationalconsortium media 5c0c850b)
- **Race/ethnicity:** Elevated risk among non‑Hispanic Black individuals is noted in recent discussions of US registry patterns and shown in the consensus epidemiology figure panels. (hsieh2024evolvingconceptsin pages 1-3, wang2024meningiomainternationalconsortium media 5c0c850b)

### 2.3 Protective factors
No protective factors were identified in the retrieved evidence excerpts for this run.

### 2.4 Gene–environment interactions
Gene–environment interaction evidence was not directly extractable from the retrieved excerpts.

---

## 3. Phenotypes
### 3.1 Common clinical presentation (symptoms/signs)
Meningiomas commonly present with symptoms attributable to mass effect and cortical irritation.
- The 2024 consensus review summarizes that many present with “mass-effect symptoms or seizures.” (wang2024meningiomainternationalconsortium pages 14-14)

**Suggested HPO terms (symptoms/signs):**
- Seizures — HP:0001250 (supported by clinical presentation statement) (wang2024meningiomainternationalconsortium pages 14-14)
- Headache — HP:0002315 (mass-effect symptom; commonly reported clinically, but explicit frequency not provided in retrieved excerpts)
- Focal neurological deficit — HP:0001249 (mass effect; explicit enumeration not provided in retrieved excerpts)

### 3.2 Imaging phenotype (diagnostic radiology)
MRI is the preferred modality.
- The consensus review reports that meningiomas “avidly enhance with gadolinium” and a dural tail is “reported in up to 72%.” (wang2024meningiomainternationalconsortium pages 14-14)
- Non‑contrast CT can show calcification “in up to 25%,” and “roughly 50% may have some perilesional edema.” (wang2024meningiomainternationalconsortium pages 14-14)

**Suggested HPO terms (imaging‑linked):**
- Intracranial mass — HP:0002175
- Cerebral edema — HP:0100749 (perilesional edema) (wang2024meningiomainternationalconsortium pages 14-14)
- Intracranial calcification — HP:0002514 (CT calcification) (wang2024meningiomainternationalconsortium pages 14-14)

### 3.3 Pathology phenotype (histology)
High‑grade meningiomas demonstrate higher mitotic activity and brain invasion.
- A 2024 surgical review defines high‑grade meningiomas (WHO grade 2/3) and notes microscopic “high mitotic rates” and macroscopic “brain invasion.” (pacult2024surgicalmanagementof pages 1-2)

**Suggested HPO terms (pathology‑linked):**
- Neoplasm invasiveness (brain invasion) — HP:0032687 (conceptually aligned; term selection may require refinement)

### 3.4 Frequency/severity/progression
- Many benign lesions may show “stagnancy or a mean growth of 1–1.5 mm/year” in natural history observations of benign tumors. (hsieh2024evolvingconceptsin pages 1-3)
- Aggressive subtypes can have poor outcomes; a 2023 review notes a substantial clinically aggressive subset and that aggressive tumors often have “5-year progression free survival (PFS) probability less than 50%.” (wang2023themultiomiclandscape pages 1-2)

Quality-of-life metrics were not directly extractable from retrieved excerpts.

---

## 4. Genetic / molecular information
### 4.1 Recurrent driver genes (somatic)
A contemporary molecular view divides meningiomas into **NF2-altered** and **non‑NF2** tumors.
- NF2 alterations are “the most common genetic abnormality… found in up to 60% of sporadic cases.” (wang2023themultiomiclandscape pages 1-2)
- Non‑NF2 recurrent drivers include **TRAF7, KLF4, AKT1, SMO, PIK3CA**, and **POLR2A**, with approximate frequencies summarized in a 2023 multi‑omics review. (wang2023themultiomiclandscape pages 1-2)

### 4.2 Germline syndromes and lineage-defining genes
- WHO CNS5 updates and genomic-era management reviews highlight lineage‑defining alterations in some histologic entities (e.g., **SMARCE1** in clear cell; **BAP1** in rhabdoid meningioma). (hsieh2024evolvingconceptsin pages 1-3, lotsch2024themolecularand pages 2-4)

### 4.3 Chromosomal abnormalities / copy number variation (CNVs)
CNVs are central to prognosis and correlate with grade.
- Common alterations include losses of “22q, 1p and 14q,” with higher genomic disruption in WHO grade 2–3 tumors. (lotsch2024themolecularand pages 2-4)
- In a large outcomes study, aggressive molecular groups (Hypermetabolic/Proliferative) showed higher CNV burden including losses of “1p, 10, 14, 18 and 22q.” (wang2024molecularclassificationto pages 1-2)

### 4.4 Epigenetics and DNA methylation
DNA‑methylation profiling is increasingly used to refine diagnosis and risk.
- A 2024 brief review advocates for methylation profiling in contemporary meningioma management. (wang2023themultiomiclandscape pages 1-2)
- A 2023 implementation paper describes integrated risk prediction combining histology, methylation family, and CNVs, emphasizing practical deployment issues. (wang2023themultiomiclandscape pages 1-2)

### 4.5 High-risk grading biomarkers (WHO-integrated)
- **TERT promoter (TERTp) mutations:** Enriched in higher grade and associated with adverse PFS; one 2024 review reports PFS “14 months vs. 101 months” for TERTp mutant versus wild type. (lotsch2024themolecularand pages 2-4)
- **CDKN2A/B deletions:** A 2023 individual‑patient‑data meta‑analysis reports median PFS 180.0 months (WT) versus 26.1 months (heterozygous deletion) versus 11.0 months (homozygous deletion), with strong hazard ratios for progression. (bhala2021incidenceofbenign pages 3-3)

---

## 5. Mechanism / pathophysiology
### 5.1 Upstream drivers to downstream clinical behavior (causal chain)
1) Initiating genomic/epigenomic alterations (e.g., NF2 loss; pathway-specific non‑NF2 driver mutations; chromosomal instability) drive 2) transcriptional programs (hypermetabolic or proliferative states) and 3) invasive/recurrence phenotypes (brain invasion, rapid progression), yielding 4) clinical endpoints of recurrence and treatment resistance. (wang2023themultiomiclandscape pages 1-2, wang2024molecularclassificationto pages 1-2, pacult2024surgicalmanagementof pages 1-2)

### 5.2 Key pathways (examples with current emphasis)
Genomics-era management reviews link NF2 biology to signaling programs such as Hippo/YAP and PI3K/AKT/mTOR signaling. (hsieh2024evolvingconceptsin pages 1-3)

**Suggested GO Biological Process terms (examples):**
- Cell cycle process — GO:0022402 (proliferative subgroup biology) (wang2024molecularclassificationto pages 1-2)
- Regulation of cell proliferation — GO:0042127 (general)

### 5.3 Immune microenvironment
Immune‑focused meningioma reviews emphasize immunophenotyping and motivate checkpoint blockade trials, reflecting immune involvement in aggressive subtypes. (lotsch2024themolecularand pages 1-2)

**Suggested CL (Cell Ontology) terms (examples):**
- T cell — CL:0000084 (checkpoint blockade rationale)
- Macrophage — CL:0000235 (tumor-associated immune infiltrates; referenced in model discussions) (wang2024meningiomainternationalconsortium pages 26-27)

---

## 6. Anatomical structures affected
### 6.1 Organ/tissue level
- Primary site: intracranial meninges with frequent dural attachment; also spinal meningiomas occur and are managed using analogous principles. (wang2024meningiomainternationalconsortium pages 25-26)

**Suggested UBERON terms (examples):**
- Meninges — UBERON:0000930
- Dura mater — UBERON:0003129
- Spinal cord meninges — (site; specific UBERON mapping may require further lookup)

---

## 7. Temporal development
- Typical onset is adult; pediatric meningiomas are rare and show distinct distributions and higher grade proportions. (wang2024meningiomainternationalconsortium pages 25-26)
- Disease course varies from indolent growth (mean 1–1.5 mm/year in benign natural history observations) to aggressive recurrence/progression in higher-grade/molecularly high-risk disease. (hsieh2024evolvingconceptsin pages 1-3, wang2023themultiomiclandscape pages 1-2)

---

## 8. Inheritance and population
### 8.1 Epidemiology (recent statistics; emphasis on 2024 sources)
- CBTRUS-linked consensus figure indicates that among US **non‑malignant primary brain tumors**, **meningiomas account for 56.2%** (distribution panel). (wang2024meningiomainternationalconsortium media 5c0c850b)
- The same figure provides registry totals for all primary brain tumors (2017–2021) and nonmalignant tumors: **5-year total 453,623 (annual average 90,725)** and nonmalignant **5-year total 326,894 (annual average 65,379)**. (wang2024meningiomainternationalconsortium pages 4-4)
- Sex and race/ethnicity incidence differences are shown in the figure panels (higher in females; higher in Black individuals), supporting recognized demographic disparities. (wang2024meningiomainternationalconsortium media 5c0c850b)

### 8.2 Special populations
- **Radiation-induced meningiomas** are described as rare (1–2%) and more aggressive, with high cytogenetic burden and frequent 1p loss (>50%). (wang2024meningiomainternationalconsortium pages 25-26)
- **Pediatric meningiomas** comprise a small fraction of pediatric brain tumors (2.2–3.6%) and have higher spinal/intraventricular frequencies and more grade 2–3 histologies; NF2 alterations are common in pediatric cases. (wang2024meningiomainternationalconsortium pages 25-26)

---

## 9. Diagnostics
### 9.1 Imaging
- **MRI** is preferred; strong gadolinium enhancement is typical; dural tail is commonly observed. (wang2024meningiomainternationalconsortium pages 14-14)
- **CT** is helpful for calcification and skull-base/bony assessment. (wang2024meningiomainternationalconsortium pages 14-14, pacult2024surgicalmanagementof pages 1-2)

### 9.2 Histopathology and grading
- High-grade tumors show increased mitotic activity and brain invasion; grade 2 criteria include 4–19 mitoses per 10 high‑power fields and/or brain invasion in surgical pathology discussions. (pacult2024surgicalmanagementof pages 2-4)

### 9.3 Molecular diagnostics
- DNA methylation profiling and sequencing refine classification and risk stratification but may face access/reimbursement barriers in practice. (wang2024meningiomainternationalconsortium pages 14-14)

### 9.4 Differential diagnosis (not exhaustively captured)
Liquid biopsy and methylation profiling are described as potentially differentiating meningiomas from imaging mimics, but require external validation. (wang2024meningiomainternationalconsortium pages 14-14)

---

## 10. Outcome / prognosis
### 10.1 Prognostic factors (quantitative highlights)
- **Molecular high-risk markers:**
  - TERTp mutations: adverse PFS (14 vs 101 months). (lotsch2024themolecularand pages 2-4)
  - CDKN2A/B deletions: strong PFS impact across deletion states (median PFS 180.0 vs 26.1 vs 11.0 months). (bhala2021incidenceofbenign pages 3-3)
- **Extent of resection:**
  - A 2024 Nature Medicine outcomes study found subtotal resection associated with worse PFS (HR 2.02) and Simpson grade 3 with shorter time to recurrence versus Simpson grade 1/2 (HR 1.64). (wang2024molecularclassificationto pages 1-2)
- **Integrated molecular risk for grade 2:**
  - In a grade 2 cohort, local control rates were 84.3% (2y), 68.5% (4y), 50.8% (6y); integrated risk group was strongly associated with recurrence (HR 9.91 intermediate; HR 7.29 high vs low), and gross total resection decreased progression risk (HR 0.19). (marastoni2023meningiomagradingbeyond pages 1-2)

### 10.2 Survival by grade
A 2024 molecular/immunologic review reports grade-associated survival differences (reported survival 12.5 years for grade 1; 6.9 years for grade 2; 2.4 years for grade 3). (lotsch2024themolecularand pages 2-4)

---

## 11. Treatment
### 11.1 Standard-of-care (real-world implementation)
- **Surgery** is the cornerstone; maximal safe resection and dural margin management reduce recurrence risk. (pacult2024surgicalmanagementof pages 1-2, wang2024molecularclassificationto pages 1-2)
- **Radiotherapy** (adjuvant or definitive) is used in selected settings (particularly high-grade or residual disease), but optimal use remains an area of clinical equipoise in some subgroups and special populations. (marastoni2023meningiomagradingbeyond pages 1-2, wang2024meningiomainternationalconsortium pages 26-27)

### 11.2 Systemic therapy: current status and expert consensus
Multiple authoritative reviews and guidelines converge on the lack of an established systemic standard:
- “Despite intensive research, no systemic treatment options are yet available in the clinic for these challenging tumors…” (review statement). (lotsch2024themolecularand pages 1-2)
- EANO guideline: “other treatment options including various systemic therapies and targeted radionuclide therapy have been investigated, but none are established as management standard,” and “no approved targeted treatments are available for this tumor type.” (reifenberger2024eanoguidelineon pages 4-5)
- EANO guideline also states: “So far, sufficient data from prospective clinical trials are missing to justify clear recommendations for molecularly targeted therapy in routine practice.” (reifenberger2024eanoguidelineon pages 20-21)

### 11.3 Recent developments (2023–2024 focus): clinical trials and precision approaches
Key interventional trials retrieved from ClinicalTrials.gov include:
- **Alliance A071401 (NCT02523014)**: mutation‑directed arms with vismodegib (SMO/PTCH1), FAK inhibitor GSK2256098 (NF2), capivasertib (AKT1/PIK3CA/PTEN), abemaciclib (CDK pathway). Primary endpoint includes 6‑month PFS. (NCT02523014 chunk 1)
- **Pembrolizumab (NCT03279692)** in recurrent/residual high‑grade meningioma: primary endpoint PFS at 6 months; ClinicalTrials.gov indicates results posted (metadata). (NCT03279692 chunk 1)
- **Nivolumab ± ipilimumab (NCT02648997)**: primary endpoint is the number of participants without progression at 6 months; includes a combined regimen after radiotherapy. (NCT02648997 chunk 1)
- **Radionuclide therapy / theranostics**:
  - EANO notes SSTR2 as an actionable target and identifies a randomized trial effort for [177Lu]Lu‑DOTATATE (LUMEN‑1; NCT06326190 mentioned in guideline context) but emphasizes lack of conclusive controlled trial data to date. (reifenberger2024eanoguidelineon pages 12-12)
  - **MOMENTUM‑1 (NCT06955169)**: randomized phase 2 comparing [177Lu]Lu‑DOTATATE versus local standard-of-care systemic options, requiring positive [68Ga]Ga‑DOTATATE PET uptake; primary endpoint PFS. (NCT06955169 chunk 1)
  - **ELUMEN (NCT06126588)**: everolimus + 177Lu‑DOTATATE PRRT in refractory WHO grade 2–3 meningioma; primary endpoint PFS at 7 months. (NCT06126588 chunk 1)

**Suggested MAXO terms (examples):**
- Surgical resection — MAXO:0000004 (conceptual)
- Radiotherapy — MAXO:0000014 (conceptual)
- Immune checkpoint inhibitor therapy — MAXO term requires lookup; supported as clinical‑trial intervention (NCT03279692 chunk 1, NCT02648997 chunk 1)
- Peptide receptor radionuclide therapy (PRRT) — MAXO term requires lookup; supported as trial intervention (NCT06955169 chunk 1, NCT06126588 chunk 1)

---

## 12. Prevention
### 12.1 Primary prevention
No established primary prevention strategy exists for sporadic meningioma in the retrieved excerpts, aside from general avoidance/minimization of unnecessary **ionizing radiation exposure** (the only established environmental risk factor in the cited epidemiologic analysis). (bhala2021incidenceofbenign pages 3-3)

### 12.2 Secondary prevention / screening
No population screening paradigm was identified in retrieved excerpts.

### 12.3 Tertiary prevention
Recurrence risk mitigation relies on maximal safe resection, appropriate adjuvant radiotherapy selection, and emerging molecular risk stratification (e.g., integrated methylation/CNV/biomarker scoring). (wang2024molecularclassificationto pages 1-2, marastoni2023meningiomagradingbeyond pages 1-2)

---

## 13. Other species / natural disease
No citable evidence on naturally occurring meningioma in non-human species was retrieved in the excerpts used for this run.

---

## 14. Model organisms
A 2024 review on genetics/classification/mouse modeling was retrieved in search results, but model‑organism details were not present in the evidence excerpts used here; thus, I do not provide specific model organism assertions without additional excerpt retrieval. (wang2023themultiomiclandscape pages 1-2)

---

## Figures (registry epidemiology)
The CBTRUS-derived epidemiology visual panels (distribution and incidence by sex/race/grade) were retrieved from the 2024 consensus review figure; these panels support the numeric nonmalignant distribution (meningioma 56.2%) and qualitative sex/race incidence disparities discussed above. (wang2024meningiomainternationalconsortium media 5c0c850b, wang2024meningiomainternationalconsortium media cc65ec92, wang2024meningiomainternationalconsortium media 5f52723b)

---

## Notes on evidence gaps and how they affect this knowledge-base entry
- **Ontology identifiers (MONDO/MeSH/ICD/Orphanet)** were not directly retrievable as citable text in the current run; they should be populated from the respective controlled‑vocabulary resources and then cited.
- **Protective factors, gene–environment interactions, and cross‑species disease** were not supported by extracted evidence in this run.
- **Model organisms** likely exist (as suggested by retrieved review titles), but detailed, citable model descriptions were not extracted in the included evidence snippets.


References

1. (wang2024meningiomainternationalconsortium pages 4-4): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.

2. (deng2022moleculardiagnosisand pages 1-2): Jiaojiao Deng, Lingyang Hua, Liuguan Bian, Hong Chen, Ligang Chen, Hongwei Cheng, Changwu Dou, Dangmurenjiapu Geng, Tao Hong, Hongming Ji, Yugang Jiang, Qing Lan, Gang Li, Zhixiong Liu, Songtao Qi, Yan Qu, Songsheng Shi, Xiaochuan Sun, Haijun Wang, Yongping You, Hualin Yu, Shuyuan Yue, Jianming Zhang, Xiaohua Zhang, Shuo Wang, Ying Mao, Ping Zhong, and Ye Gong. Molecular diagnosis and treatment of meningiomas: an expert consensus (2022). Chinese Medical Journal, Sep 2022. URL: https://doi.org/10.1097/cm9.0000000000002391, doi:10.1097/cm9.0000000000002391. This article has 15 citations and is from a peer-reviewed journal.

3. (lotsch2024themolecularand pages 1-2): Catharina Lotsch, Rolf Warta, and Christel Herold-Mende. The molecular and immunological landscape of meningiomas. International Journal of Molecular Sciences, 25:9631, Sep 2024. URL: https://doi.org/10.3390/ijms25179631, doi:10.3390/ijms25179631. This article has 14 citations.

4. (torp2022thewho2021 pages 7-9): Sverre Helge Torp, Ole Solheim, and Anne Jarstein Skjulsvik. The who 2021 classification of central nervous system tumours: a practical update on what neurosurgeons need to know—a minireview. Acta Neurochirurgica, 164:2453-2464, Jul 2022. URL: https://doi.org/10.1007/s00701-022-05301-y, doi:10.1007/s00701-022-05301-y. This article has 380 citations and is from a peer-reviewed journal.

5. (wang2024meningiomainternationalconsortium media 5c0c850b): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.

6. (wang2023genomiclandscapeof pages 1-2): Justin Z. Wang, Farshad Nassiri, Christian Mawrin, and Gelareh Zadeh. Genomic landscape of meningiomas. Advances in experimental medicine and biology, 1416:137-158, Jan 2023. URL: https://doi.org/10.1007/978-3-031-29750-2\_11, doi:10.1007/978-3-031-29750-2\_11. This article has 12 citations and is from a peer-reviewed journal.

7. (wang2023themultiomiclandscape pages 1-2): Justin Z. Wang, Farshad Nassiri, Alexander P. Landry, Vikas Patil, Jeff Liu, Kenneth Aldape, Andrew Gao, and Gelareh Zadeh. The multiomic landscape of meningiomas: a review and update. Journal of Neuro-Oncology, 161:405-414, Jan 2023. URL: https://doi.org/10.1007/s11060-023-04253-2, doi:10.1007/s11060-023-04253-2. This article has 19 citations and is from a peer-reviewed journal.

8. (hsieh2024evolvingconceptsin pages 1-3): Annie L. Hsieh, Wenya Linda Bi, Vijaya Ramesh, Priscilla K. Brastianos, and Scott R. Plotkin. Evolving concepts in meningioma management in the era of genomics. Cancer, 130:2586-2600, May 2024. URL: https://doi.org/10.1002/cncr.35279, doi:10.1002/cncr.35279. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (lotsch2024themolecularand pages 2-4): Catharina Lotsch, Rolf Warta, and Christel Herold-Mende. The molecular and immunological landscape of meningiomas. International Journal of Molecular Sciences, 25:9631, Sep 2024. URL: https://doi.org/10.3390/ijms25179631, doi:10.3390/ijms25179631. This article has 14 citations.

10. (wang2024molecularclassificationto pages 1-2): Justin Z. Wang, Vikas Patil, Alexander P. Landry, Chloe Gui, Andrew Ajisebutu, Jeff Liu, Olli Saarela, Stephanie L. Pugh, Minhee Won, Zeel Patel, Rebeca Yakubov, Ramneet Kaloti, Christopher Wilson, Aaron Cohen-Gadol, Mohamed A. Zaazoue, Ghazaleh Tabatabai, Marcos Tatagiba, Felix Behling, Damian A. Almiron Bonnin, Eric C. Holland, Tim J. Kruser, Jill S. Barnholtz-Sloan, Andrew E. Sloan, Craig Horbinski, Silky Chotai, Lola B. Chambless, Andrew Gao, Alexander D. Rebchuk, Serge Makarenko, Stephen Yip, Felix Sahm, Sybren L. N. Maas, Derek S. Tsang, Michael W. McDermott, Thomas Santarius, Warren Selman, Marta Couce, Andrew E. Sloan, Bruno Carvalho, Patrick Y. Wen, Kyle M. Walsh, Eelke M. Bos, Wenya Linda Bi, Raymond Y. Huang, Priscilla K. Brastianos, Helen A. Shih, Tobias Walbert, Ian Lee, Michelle M. Felicella, Ana Valeria Castro, Houtan Noushmehr, James M. Snyder, Francesco Dimeco, Andrea Saladino, Bianca Pollo, Christian Schichor, Jörg-Christian Tonn, Felix Ehret, Timothy J. Kaufmann, Daniel H. Lachance, Caterina Giannini, Evanthia Galanis, Aditya Raghunathan, Michael A. Vogelbaum, Jill Barnholtz-Sloan, Patrick J. Cimino, Craig M. Horbinski, Mark Youngblood, Matija Snuderl, Sylvia C. Kurz, Erik P. Sulman, Ian F. Dunn, C. Oliver Hanemann, Mohsen Javadpour, Ho-Keung Ng, Paul C. Boutros, Richard G. Everson, Alkiviadis Tzannis, Konstantinos N. Fountas, Nils Ole Schmidt, Karolyn Au, Roland Goldbrunner, Norbert Galldiks, Marco Timmer, Tiit Illimar Mathiesen, Manfred Westphal, Katrin Lamszus, Franz L. Ricklefs, Christel Herold-Mende, Felix Sahm, Christine Jungk, Gerhard Jungwirth, Andreas von Deimling, Maximilian Deng, Susan C. Short, Michael D. Jenkinson, Christian Mawrin, Abdurrahman I. Islim, Daniel M. Fountain, Omar N. Pathmanaban, Katharine J. Drummond, Andrew Morokoff, David R. Raleigh, Arie Perry, Nicholas A. Butowski, Tathiane M. Malta, Viktor Zherebitskiy, Luke Hnenny, Gabriel Zada, Mirjam Renovanz, Antonio Santacroce, Christian la Fougère, Jens Schittenhelm, Paul Passlack, Jennifer Moliterno, Alper Dincer, C. Leland Rogers, Kenneth Aldape, Farshad Nassiri, and Gelareh Zadeh. Molecular classification to refine surgical and radiotherapeutic decision-making in meningioma. Nature Medicine, 30:3173-3183, Aug 2024. URL: https://doi.org/10.1038/s41591-024-03167-4, doi:10.1038/s41591-024-03167-4. This article has 79 citations and is from a highest quality peer-reviewed journal.

11. (marastoni2023meningiomagradingbeyond pages 1-2): Elena Marastoni and Valeria Barresi. Meningioma grading beyond histopathology: relevance of epigenetic and genetic features to predict clinical outcome. Cancers, 15:2945, May 2023. URL: https://doi.org/10.3390/cancers15112945, doi:10.3390/cancers15112945. This article has 14 citations.

12. (bhala2021incidenceofbenign pages 3-3): Sonia Bhala, Douglas R Stewart, Victoria Kennerley, Valentina I Petkov, Philip S Rosenberg, and Ana F Best. Incidence of benign meningiomas in the united states: current and future trends. JNCI cancer spectrum, 5 3:pkab035, Apr 2021. URL: https://doi.org/10.1093/jncics/pkab035, doi:10.1093/jncics/pkab035. This article has 38 citations and is from a peer-reviewed journal.

13. (wang2024meningiomainternationalconsortium pages 14-14): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.

14. (pacult2024surgicalmanagementof pages 1-2): Mark A. Pacult, Colin J. Przybylowski, Shaan M. Raza, and Franco DeMonte. Surgical management of high-grade meningiomas. Cancers, 16:1978, May 2024. URL: https://doi.org/10.3390/cancers16111978, doi:10.3390/cancers16111978. This article has 4 citations.

15. (reifenberger2024eanoguidelineon pages 4-5): LS Reifenberger, AK Suwala, G Tabatabai, and E Tabouret. Eano guideline on molecular testing of meningiomas for targeted therapy selection. Unknown journal, 2024.

16. (hsieh2024evolvingconceptsin pages 10-11): Annie L. Hsieh, Wenya Linda Bi, Vijaya Ramesh, Priscilla K. Brastianos, and Scott R. Plotkin. Evolving concepts in meningioma management in the era of genomics. Cancer, 130:2586-2600, May 2024. URL: https://doi.org/10.1002/cncr.35279, doi:10.1002/cncr.35279. This article has 12 citations and is from a domain leading peer-reviewed journal.

17. (reifenberger2024eanoguidelineon pages 3-4): LS Reifenberger, AK Suwala, G Tabatabai, and E Tabouret. Eano guideline on molecular testing of meningiomas for targeted therapy selection. Unknown journal, 2024.

18. (reifenberger2024eanoguidelineon pages 20-21): LS Reifenberger, AK Suwala, G Tabatabai, and E Tabouret. Eano guideline on molecular testing of meningiomas for targeted therapy selection. Unknown journal, 2024.

19. (NCT02523014 chunk 1):  Vismodegib, FAK Inhibitor GSK2256098, Capivasertib, and Abemaciclib in Treating Patients With Progressive Meningiomas. Alliance for Clinical Trials in Oncology. 2015. ClinicalTrials.gov Identifier: NCT02523014

20. (NCT03279692 chunk 1): Priscilla Brastianos. Phase II Trial of Pembrolizumab in Recurrent or Residual High Grade Meningioma. Massachusetts General Hospital. 2017. ClinicalTrials.gov Identifier: NCT03279692

21. (NCT03279692 chunk 2): Priscilla Brastianos. Phase II Trial of Pembrolizumab in Recurrent or Residual High Grade Meningioma. Massachusetts General Hospital. 2017. ClinicalTrials.gov Identifier: NCT03279692

22. (NCT02648997 chunk 1): David Reardon, MD. An Open-Label Phase II Study of Nivolumab or Nivolumab/Ipilimumab in Adult Participants With Progessive/ Recurrent Meningioma. Dana-Farber Cancer Institute. 2016. ClinicalTrials.gov Identifier: NCT02648997

23. (NCT02648997 chunk 3): David Reardon, MD. An Open-Label Phase II Study of Nivolumab or Nivolumab/Ipilimumab in Adult Participants With Progessive/ Recurrent Meningioma. Dana-Farber Cancer Institute. 2016. ClinicalTrials.gov Identifier: NCT02648997

24. (reifenberger2024eanoguidelineon pages 12-12): LS Reifenberger, AK Suwala, G Tabatabai, and E Tabouret. Eano guideline on molecular testing of meningiomas for targeted therapy selection. Unknown journal, 2024.

25. (NCT06955169 chunk 1):  Comparing the Radiopharmaceutical Drug, [177Lu]Lu-DOTATATE, to Standard of Care Treatment for Patients With Meningioma That Has Come Back After Prior Treatment. RTOG Foundation, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06955169

26. (NCT06126588 chunk 1): Antoine VERGER. Combination of Everolimus and 177Lu-DOTATATE in the Treatment of Grades 2 and 3 Refractory Meningioma: a Phase IIb Clinical Trial. Central Hospital, Nancy, France. 2024. ClinicalTrials.gov Identifier: NCT06126588

27. (wang2024meningiomainternationalconsortium pages 26-27): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.

28. (wang2024meningiomainternationalconsortium pages 25-26): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.

29. (pacult2024surgicalmanagementof pages 2-4): Mark A. Pacult, Colin J. Przybylowski, Shaan M. Raza, and Franco DeMonte. Surgical management of high-grade meningiomas. Cancers, 16:1978, May 2024. URL: https://doi.org/10.3390/cancers16111978, doi:10.3390/cancers16111978. This article has 4 citations.

30. (wang2024meningiomainternationalconsortium media cc65ec92): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.

31. (wang2024meningiomainternationalconsortium media 5f52723b): Justin Z Wang, Alexander P Landry, David R Raleigh, Felix Sahm, Kyle M Walsh, Roland Goldbrunner, Leeor S Yefet, Jörg C Tonn, Chloe Gui, Quinn T Ostrom, Jill Barnholtz-Sloan, Arie Perry, Yosef Ellenbogen, C Oliver Hanemann, Gerhard Jungwirth, Michael D Jenkinson, Ghazaleh Tabatabai, Tiit I Mathiesen, Michael W McDermott, Marcos Tatagiba, Christian la Fougère, Sybren L N Maas, Norbert Galldiks, Nathalie L Albert, Priscilla K Brastianos, Felix Ehret, Giuseppe Minniti, Katrin Lamszus, Franz L Ricklefs, Jens Schittenhelm, Katharine J Drummond, Ian F Dunn, Omar N Pathmanaban, Aaron A Cohen-Gadol, Erik P Sulman, Emeline Tabouret, Emelie Le Rhun, Christian Mawrin, Jennifer Moliterno, Michael Weller, Wenya (Linda) Bi, Andrew Gao, Stephen Yip, Maximilian Niyazi, Kenneth Aldape, Patrick Y Wen, Susan Short, Matthias Preusser, Farshad Nassiri, and Gelareh Zadeh. Meningioma: international consortium on meningiomas consensus review on scientific advances and treatment paradigms for clinicians, researchers, and patients. Neuro-Oncology, 26:1742-1780, May 2024. URL: https://doi.org/10.1093/neuonc/noae082, doi:10.1093/neuonc/noae082. This article has 116 citations and is from a domain leading peer-reviewed journal.
