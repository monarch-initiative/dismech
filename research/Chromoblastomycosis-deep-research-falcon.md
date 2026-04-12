---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T13:15:28.617134'
end_time: '2026-04-04T13:34:39.911009'
duration_seconds: 1151.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chromoblastomycosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromoblastomycosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chromoblastomycosis** covering all of the
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
- **Disease Name:** Chromoblastomycosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chromoblastomycosis** covering all of the
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


# Chromoblastomycosis (CBM) — Disease Characteristics Research Report

## Executive summary (current understanding)
Chromoblastomycosis (CBM) is a chronic implantation/subcutaneous mycosis caused by melanized (dematiaceous) fungi introduced via traumatic transcutaneous inoculation, producing slowly progressive, polymorphic skin/subcutaneous lesions and disability; diagnosis is defined by the presence of muriform (Medlar/sclerotic/“copper penny”) bodies on microscopy/histopathology. CBM is a WHO-designated neglected tropical disease (NTD) and a skin-NTD, but global burden estimates remain uncertain because surveillance and access to diagnostics/treatment are limited. (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2)

## 1. Disease information
### 1.1 Definition/overview
- CBM is an **implantation mycosis** acquired when melanized filamentous fungi enter the skin through **traumatic injury**; it is chronic, granulomatous, and predominantly involves skin and subcutaneous tissues. (smith2024aglobalchromoblastomycosis pages 2-3, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5)
- **Diagnostic hallmark:** thick-walled, pigmented, septate **muriform (Medlar/sclerotic) bodies** in clinical specimens (scrapings/biopsy). (smith2024aglobalchromoblastomycosis pages 2-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3)

### 1.2 Key identifiers and controlled vocabularies (available from retrieved sources)
| Field | Value |
|---|---|
| Disease name | Chromoblastomycosis (smith2024aglobalchromoblastomycosis pages 1-2) |
| Category / disease class | Neglected tropical disease; specifically a skin-NTD; chronic implantation/subcutaneous mycosis caused by melanized (dematiaceous) fungi (smith2024aglobalchromoblastomycosis pages 1-2, smith2024aglobalchromoblastomycosis pages 2-3) |
| WHO NTD status | WHO designated chromoblastomycosis as a neglected tropical disease in 2017; included in the WHO Road Map for Neglected Tropical Diseases 2021–2030 and designated as an NTD “targeted for control” (smith2024aglobalchromoblastomycosis pages 1-2, smith2024aglobalchromoblastomycosis pages 2-3) |
| Common synonyms / alternate names found in context | Chromomycosis / chromomycosis; chromomycotic infection not explicitly found in available context; clinical literature also refers to “chromoblastomycosis (CBM)” (NCT06523998 chunk 1, NCT06523998 chunk 2, sanchezdiaz2025chromoblastomycosisinperu pages 1-2) |
| MeSH term | Chromoblastomycosis (NCT06523998 chunk 2) |
| MeSH ID | D002862 (from ClinicalTrials.gov derived MeSH browsing for a study including chromoblastomycosis/chromomycosis) (NCT06523998 chunk 2) |
| ICD-10 code(s) explicitly available in context | B43.0 = cutaneous chromoblastomycosis; B43.8 and B43.9 also reported as additional B43 chromoblastomycosis hospitalization codes in U.S. inpatient analysis (smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5) |
| ICD-11 | Not found in available context/sources retrieved here (smith2024aglobalchromoblastomycosis pages 2-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 6-8) |
| MONDO ID | Not found in available context/sources retrieved here (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2) |
| Orphanet ID | Not found in available context/sources retrieved here (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2) |
| Source granularity | Primarily aggregated disease-level resources and observational case series/hospitalization datasets; not derived solely from individual EHR patients (smith2024aglobalchromoblastomycosis pages 1-2, valentin2024chromoblastomycosisinfrench pages 1-2, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5) |


*Table: This table summarizes the key classification terms, disease identifiers, and synonym information for chromoblastomycosis using only evidence available in the cited context. It is useful for normalizing a disease knowledge-base entry and documenting where identifier gaps remain.*

**Notes on identifier gaps:** ICD-11, MONDO, and Orphanet IDs were not found in the retrieved full texts; additional retrieval from those specific terminologies would be required rather than inference. (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2)

### 1.3 Synonyms and alternative names
- “Chromomycosis” appears as a synonym/umbrella term in a ClinicalTrials.gov observational study that includes “Chromomycosis” as a condition keyword and “Chromoblastomycosis” as a keyword. (NCT06523998 chunk 1)

### 1.4 Evidence source type
Evidence summarized below comes from:
- Aggregated disease-level strategy/gap-analysis for WHO NTD roadmap implementation. (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2)
- Regional retrospective clinical series (French Guiana; Peru) and administrative hospitalization analyses (US). (valentin2024chromoblastomycosisinfrench pages 1-2, sanchezdiaz2025chromoblastomycosisinperu pages 1-2, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5)
- Mechanistic studies in vitro and in murine experimental models, and review-level immunology synthesis. (ferreira2025il18productionis pages 1-2, zhong2024roleofdectin1 pages 1-2, lionakis2023immuneresponsesto pages 9-10)

## 2. Etiology
### 2.1 Primary causal factors
- **Cause:** infection by **dematiaceous (melanized) fungi**, acquired after traumatic inoculation from environmental reservoirs (soil, plants, decaying wood; splinters/thorns). (martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5, smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3)
- Common etiologic genera/species described in recent sources include **Fonsecaea** (*F. pedrosoi*, *F. monophora*, *F. nubica*), **Cladophialophora** (*C. carrionii*), **Phialophora** (*P. verrucosa*), and **Rhinocladiella** (*R. aquaspersa*). (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, sanchezdiaz2025chromoblastomycosisinperu pages 1-2)

### 2.2 Risk factors (human / environmental)
- **Occupational/outdoor exposure and rural work:** French Guiana series: **74%** outdoor occupations and **87%** male. (valentin2024chromoblastomycosisinfrench pages 2-4)
- **Trauma history:** French Guiana series: reported initial trauma in **39.1%**. (valentin2024chromoblastomycosisinfrench pages 2-4)
- **Endemicity and geography:** CBM is endemic in tropical/subtropical regions of Latin America, Africa, Asia, and the Caribbean; uncommon in the US but can occur (e.g., gardening exposure). (martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5)
- **Comorbidity/immunosuppression:** CBM can affect immunocompetent and immunosuppressed individuals; immunosuppression can be associated with severe/treatment-resistant disease (e.g., tacrolimus). (smith2024aglobalchromoblastomycosis pages 2-3, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5)

### 2.3 Protective factors
- No validated genetic protective variants were identified in the retrieved sources.
- Proposed/operational protective measures (behavioral/environmental) are described under Prevention (Section 13). (smith2024aglobalchromoblastomycosis pages 6-7)

### 2.4 Gene–environment interactions
Direct gene–environment interaction data were not identified in the retrieved clinical literature; strategy-level sources highlight traumatic inoculation and environmental reservoirs as key drivers and mention candidate host predisposition loci (Section 4/8). (smith2024aglobalchromoblastomycosis pages 2-3)

## 3. Phenotypes (clinical manifestations)
### 3.1 Core cutaneous phenotypes and frequencies (recent observational series)
**French Guiana (1955–2023; published Feb 2024):** lesion types included cicatricial **21.7%**, verrucous **21.7%**, nodular **13%**, tumoral **4.3%**, plaque **4.3%**, mixed **34.8%**; severity: mild **13%**, moderate **52.2%**, severe **30.4%**; symptoms: pruritus **26.1%**, pain **17.4%**. (valentin2024chromoblastomycosisinfrench pages 4-7, valentin2024chromoblastomycosisinfrench pages 2-4)

**Peru (2011–2024; published Aug 2025):** plaque-like and verrucous forms **38%** each; tumoral and cicatricial **15%** each; pruritus **84%**, pain **30%**; **30%** reported functional limitations affecting work. (sanchezdiaz2025chromoblastomycosisinperu pages 1-2)

**Anatomic distribution:** lower limb predominance is consistent across series (e.g., **78.3%** in French Guiana; **53%** in Peru). (valentin2024chromoblastomycosisinfrench pages 2-4, sanchezdiaz2025chromoblastomycosisinperu pages 1-2)

### 3.2 Severity/staging
- Both French Guiana and Peru series used the **Queiroz-Telles severity grading** (mild/moderate/severe) based on lesion size/extent (e.g., mild: single plaque/nodule <5 cm; severe: >15 cm or multiple non-adjacent areas). (valentin2024chromoblastomycosisinfrench pages 2-4, valentin2024chromoblastomycosisinfrench pages 1-2)

### 3.3 Complications and quality-of-life impact
- Strategy paper lists major complications: **tissue fibrosis, lymphedema, secondary bacterial infections, squamous cell carcinoma, ankylosis, ectropium**; risk-factor magnitude is considered poorly quantified globally. (smith2024aglobalchromoblastomycosis pages 4-6)
- French Guiana series observed long-term complications in **13%** (functional limitation, elephantiasis/lymphedema, and squamous cell carcinoma requiring amputation). (valentin2024chromoblastomycosisinfrench pages 2-4)
- CBM is described as causing decreased quality of life, stigma, and disability in WHO-aligned strategy framing. (smith2024aglobalchromoblastomycosis pages 3-4)

### 3.4 Suggested HPO terms (non-exhaustive; based on phenotypes evidenced above)
- Verrucous skin lesion (HPO suggestion: HP:0100804 “Verrucous skin lesion”) (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7)
- Cutaneous plaque (HP:0011124 “Plaque”) (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7)
- Skin nodule (HP:0001484 “Skin nodule”) (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7)
- Pruritus (HP:0000989) (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7)
- Pain (HP:0012531) (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7)
- Lymphedema/elephantiasis (HP:0001004 “Lymphedema”) (valentin2024chromoblastomycosisinfrench pages 2-4, smith2024aglobalchromoblastomycosis pages 4-6)
- Squamous cell carcinoma of the skin (HP:0006735 “Squamous cell carcinoma”) (valentin2024chromoblastomycosisinfrench pages 2-4, smith2024aglobalchromoblastomycosis pages 4-6)

## 4. Genetic / molecular information (human and fungal)
### 4.1 Human susceptibility genetics (current evidence status)
- A 2024 global strategy paper cites **HLA-A29** and **CARD9** as examples of genetic predisposing factors discussed in the CBM context. (smith2024aglobalchromoblastomycosis pages 2-3)
- No Mendelian “causal gene” for CBM was established in the retrieved clinical series; evidence is currently framed as susceptibility/predisposition rather than a monogenic etiology. (smith2024aglobalchromoblastomycosis pages 2-3)

### 4.2 Human immunologic markers (host response)
- Human lesion immunopathology (Dec 2023) emphasizes T-cell infiltration and immunoregulatory/exhaustion pathways, reporting PD-1/PD-L1 positivity in all samples and cytokine patterns that can favor chronic infection (e.g., increased IL-10/IL-17 associated with muriform cells). (cavallone2023newimmunologicalmarkers pages 6-9)

### 4.3 Fungal molecular determinants (virulence and persistence)
- **Melanin** is repeatedly implicated as a virulence factor; strategy framing links melanin to protection from host oxidative/nitrosative stresses and facilitation of transformation into thick-walled muriform bodies resistant to immunity and antifungals. (smith2024aglobalchromoblastomycosis pages 2-3)
- In vitro macrophage study (Sep 2024) supports a mechanistic role where fungal melanin hinders **Dectin-1** binding and reduces phagocytosis/killing and proinflammatory responses. (zhong2024roleofdectin1 pages 1-2)
- Fungal functional genomics: transformation tools and a *Fonsecaea pedrosoi* **trpB** knockout system were developed to enable gene-function studies in CBM agents, relevant for future target validation. (favilla2023expandingthetoolbox pages 1-2, favilla2023expandingthetoolbox pages 12-13)

### 4.4 Ontology suggestions
- GO biological process suggestions: “inflammasome complex assembly”, “interleukin-18 production”, “T helper 1 type immune response”, “phagocytosis”, “fungal cell wall organization” (ferreira2025il18productionis pages 1-2, zhong2024roleofdectin1 pages 1-2, smith2024aglobalchromoblastomycosis pages 2-3)
- CL cell-type suggestions: macrophage; neutrophil; CD4-positive, alpha-beta T cell; CD8-positive, alpha-beta T cell (ferreira2025il18productionis pages 1-2, cavallone2023newimmunologicalmarkers pages 6-9)

## 5. Environmental information
- **Reservoirs/exposure contexts:** fungi are environmental and can be associated with thorn/prick injuries and certain plants; the 2024 strategy highlights plant associations (e.g., *Mimosa pudica*) and climate sensitivity of causative fungi. (smith2024aglobalchromoblastomycosis pages 4-6)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (integrated)
1) **Traumatic inoculation** introduces melanized fungi into skin/subcutaneous tissue. (smith2024aglobalchromoblastomycosis pages 2-3)
2) Fungal adaptation includes formation of **muriform cells** with thickened pigmented cell walls, contributing to persistence and treatment refractoriness. (smith2024aglobalchromoblastomycosis pages 2-3)
3) **Innate immune recognition is suboptimal** in some models; a high-impact review describes modest CLR signaling via dectin-2/Mincle and failure to activate TLRs effectively, contributing to inadequate local inflammation. (lionakis2023immuneresponsesto pages 9-10)
4) **Protective pathways** include macrophage recognition/phagocytosis (e.g., Dectin-1-associated) and Th1/Th17 adaptive immunity; experimental work shows NLRP3→caspase-1→IL-18 supports Th1/IFN-γ-mediated fungal control. (ferreira2025il18productionis pages 1-2, zhong2024roleofdectin1 pages 1-2)
5) **Chronicity** may be reinforced by immunoregulatory/exhaustion mechanisms in human lesions (PD-1/PD-L1; IL-10/IL-17 patterns), impairing effective clearance. (cavallone2023newimmunologicalmarkers pages 6-9)

### 6.2 Recent mechanistic developments (2023–2024 prioritized)
- **Immune exhaustion markers:** PD-1/PD-L1 and altered cytokine landscapes in human CBM lesions (Dec 2023). (cavallone2023newimmunologicalmarkers pages 6-9)
- **Melanin–CLR interference:** melanin-dependent suppression of Dectin-1–mediated macrophage responses (Sep 2024). (zhong2024roleofdectin1 pages 1-2)

## 7. Anatomical structures affected
- **Primary sites:** skin and subcutaneous tissues, classically lower extremities (legs/feet). (valentin2024chromoblastomycosisinfrench pages 2-4, sanchezdiaz2025chromoblastomycosisinperu pages 1-2)
- **Complication-associated structures:** lymphatic system involvement (lymphedema/elephantiasis) and potential malignant transformation of skin; deeper involvement can occur (bone involvement described in SCC complication). (valentin2024chromoblastomycosisinfrench pages 2-4)

**UBERON suggestions:** skin of lower limb; subcutaneous adipose tissue; lymphatic vessel; (valentin2024chromoblastomycosisinfrench pages 2-4, sanchezdiaz2025chromoblastomycosisinperu pages 1-2)

## 8. Temporal development (natural history)
- **Onset pattern:** typically chronic/insidious after inoculation trauma. (smith2024aglobalchromoblastomycosis pages 2-3)
- **Diagnostic delay and chronicity:** median time to diagnosis 4 years in French Guiana; mean disease duration at diagnosis 10.7 years in Peru. (valentin2024chromoblastomycosisinfrench pages 2-4, sanchezdiaz2025chromoblastomycosisinperu pages 1-2)
- **Progression:** lesions can expand (e.g., large vegetating lesions) and complications become more likely with duration/severity. (smith2024aglobalchromoblastomycosis pages 4-6)

## 9. Inheritance and population
- **Inheritance:** not applicable as a primary cause (infectious implantation mycosis). Candidate susceptibility loci are discussed but not a defined inheritance pattern. (smith2024aglobalchromoblastomycosis pages 2-3)
- **Epidemiology and demographics:** summarized quantitatively in the table below.

| Study/setting | Publication date | Design | N | Key demographics | Diagnostic delay | Key diagnostic yields | Key outcomes/complications | URL |
|---|---|---|---:|---|---|---|---|---|
| French Guiana, cases diagnosed 1955–2023 | Feb 2024 (valentin2024chromoblastomycosisinfrench pages 1-2, valentin2024chromoblastomycosisinfrench pages 2-4) | Retrospective observational series (valentin2024chromoblastomycosisinfrench pages 1-2) | 23 (valentin2024chromoblastomycosisinfrench pages 1-2) | 87% male; mean age 60 years; 87% lived in coastal areas; 74% had outdoor occupations; trauma reported in 39.1% (valentin2024chromoblastomycosisinfrench pages 2-4) | Median disease duration at diagnosis 4 years; range 2 months–20 years; 52.2% had lesions evolving ≥3 years (valentin2024chromoblastomycosisinfrench pages 2-4) | Direct microscopy positive 78.3% in abstract, while detailed series pages report 12/23 (52.2%); culture positive 69.6%; histopathology positive 22/23 (95.7%); 14 cultured isolates were *Fonsecaea pedrosoi* (valentin2024chromoblastomycosisinfrench pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7) | Complications in 13%: functional limitation, elephantiasis, and 1 squamous cell carcinoma requiring amputation; severe disease 30.4% (valentin2024chromoblastomycosisinfrench pages 2-4, valentin2024chromoblastomycosisinfrench pages 4-7) | https://doi.org/10.3390/jof10030168 (valentin2024chromoblastomycosisinfrench pages 1-2) |
| Peru, cases diagnosed 2011–2024 | Aug 2025 (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | Retrospective review of tertiary-center cases (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | 13 analyzable cases (15 identified) (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | 84% male; median age 65.3 years; 77% acquired infection in the Peruvian Amazon, including Ucayali 46% and San Martin 23% (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | Average disease duration 10.7 years; range 1–25 years (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | Confirmation by muriform cells on direct microscopy or histopathology; etiologic morphology identified in 9 patients; *Fonsecaea* spp. 46%, *Cladophialophora* 15%, *Phialophora* 7% (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | Lesions 2–50 cm; lower limbs 53%; plaque-like and verrucous forms each 38%; 46% had single lesions; treatment duration 5–136 months; cure 46%; misdiagnosis included leishmaniasis/tuberculosis (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) | https://doi.org/10.1186/s12879-025-11475-4 (sanchezdiaz2025chromoblastomycosisinperu pages 1-2) |
| United States hospitalizations, 2016–2021 | Sep 2025 (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5) | HCUP National Inpatient Sample hospitalization analysis (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5) | 690 hospitalization estimates for chromoblastomycosis/phaeohyphomycotic abscesses; 155 coded as cutaneous chromoblastomycosis B43.0 (smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5) | Higher rates in males (0.4 vs 0.3 per 1,000,000); highest in age ≥65 years (0.9 per 1,000,000); highest regional rates in Northeast 0.5 and South 0.4 per 1,000,000 (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5) | Not reported; outpatient cases likely undercounted because NIS excludes outpatient visits (smith2025chromoblastomycosisandphaeohyphomycotic pages 6-8) | Administrative coding study; no direct microscopy/culture yield data reported (smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5, smith2025chromoblastomycosisandphaeohyphomycotic pages 6-8) | Mean hospital stay 9.9 days overall and 8.5 days for chromoblastomycosis; in-hospital mortality 3%; lymphedema in 14% of chromoblastomycosis hospitalizations / about 1 in 7 patients; common comorbidities: hypertension 34%, diabetes 33%, dyslipidemia 28%, CKD 21% (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5, smith2025chromoblastomycosisandphaeohyphomycotic pages 6-8) | https://doi.org/10.1371/journal.pntd.0013499 (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3) |
| Global burden / WHO strategy statements | Oct 2024 (smith2024aglobalchromoblastomycosis pages 1-2, smith2024aglobalchromoblastomycosis pages 2-3) | WHO roadmap-aligned strategy paper / expert gap assessment synthesis (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2) | Global case burden unknown; some researchers estimate >10,000 global cases (smith2024aglobalchromoblastomycosis pages 1-2) | No unified global demographic denominator because there is no national, regional, or global surveillance network (smith2024aglobalchromoblastomycosis pages 1-2) | Not quantifiable globally due to surveillance and diagnostic access gaps (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2) | No pooled diagnostic yields; WHO priorities include surveillance, affordable diagnostics/treatment, field manuals, training, and rapid diagnostics (smith2024aglobalchromoblastomycosis pages 2-3) | WHO designated chromoblastomycosis an NTD in 2017; included in WHO NTD Road Map 2021–2030 as “targeted for control”; 2023 gap assessment rated 5/11 dimensions orange and 6/11 red, indicating major unmet needs (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 1-2) | https://doi.org/10.1371/journal.pntd.0012562 (smith2024aglobalchromoblastomycosis pages 2-3) |


*Table: This table compiles recent quantitative epidemiology, demographics, diagnostic yield, and outcome data for chromoblastomycosis across regional studies and global strategy sources. It is useful for comparing burden estimates, diagnostic delays, and complications across settings.*

## 10. Diagnostics
### 10.1 Standard diagnostic concept
- Confirmatory diagnosis relies on identification of **muriform bodies** on **KOH direct microscopy** and/or **histopathology**. (smith2024aglobalchromoblastomycosis pages 4-6, valentin2024chromoblastomycosisinfrench pages 4-7)

### 10.2 Diagnostic modalities (real-world implementation)
| Modality | What it detects | Key hallmark | Yield/sensitivity (if available) | Notes/real-world implementation | Key source (with PMID if present; if not in text, leave blank) | URL |
|---|---|---|---|---|---|---|
| Direct microscopy (KOH) | Muriform/sclerotic/fumagoid cells in skin scrapings or lesion material (ariani2023clinicalandmycological pages 6-9, ariani2023clinicalandmycological pages 9-11, smith2024aglobalchromoblastomycosis pages 4-6, valentin2024chromoblastomycosisinfrench pages 4-7, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | Pathognomonic round brown thick-walled “copper penny”/Medlar/muriform bodies; highest yield from lesions with black dots (ariani2023clinicalandmycological pages 6-9, ariani2023clinicalandmycological pages 9-11) | Reported sensitivity 90–100% in a 2023 case series; French Guiana series: 12/23 positive (52.2%) in detailed results, while abstract reports 78.3% (ariani2023clinicalandmycological pages 9-11, valentin2024chromoblastomycosisinfrench pages 4-7, valentin2024chromoblastomycosisinfrench pages 1-2) | Low-cost, high-yield method emphasized for resource-limited settings; training is important; vinyl adhesive tape sampling has been proposed for field use (smith2024aglobalchromoblastomycosis pages 4-6) | Ariani et al., 2023; Valentin et al., 2024; PMID not provided in context (ariani2023clinicalandmycological pages 9-11, valentin2024chromoblastomycosisinfrench pages 4-7) | https://doi.org/10.3390/jof10030168 |
| Histopathology | Tissue architecture plus fungal elements in biopsy sections (ariani2023clinicalandmycological pages 9-11, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5, valentin2024chromoblastomycosisinfrench pages 4-7) | Pseudoepitheliomatous hyperplasia/granulomatous inflammation with muriform bodies; “copper penny” cells in tissue (ariani2023clinicalandmycological pages 9-11, valentin2024chromoblastomycosisinfrench pages 4-7) | French Guiana: 22/23 positive (95.7%) (valentin2024chromoblastomycosisinfrench pages 4-7) | Often the highest-yield confirmatory modality in series; useful when direct exam/culture are negative or clinical differential includes SCC, atypical mycobacteria, or other deep mycoses (martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5, valentin2024chromoblastomycosisinfrench pages 4-7) | Valentin et al., 2024; Martinelli et al., 2024; PMID not provided in context (martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5, valentin2024chromoblastomycosisinfrench pages 4-7) | https://doi.org/10.3390/jof10030168 |
| Mycological culture | Viable dematiaceous fungus for genus/species identification (ariani2023clinicalandmycological pages 9-11, zheng2024successfulmanagementof pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | Dark/black pigmented colonies; species-specific colony morphology on Sabouraud agar (ariani2023clinicalandmycological pages 9-11, zheng2024successfulmanagementof pages 1-2) | French Guiana: 16/23 positive (69.6%) (valentin2024chromoblastomycosisinfrench pages 4-7) | Enables etiologic identification (e.g., *Fonsecaea pedrosoi*, *Alternaria infectoria*); culture may be difficult to obtain in some settings and environmental cultures are challenging (valentin2024chromoblastomycosisinfrench pages 4-7, mahmoudi2024chromoblastomycosiscausedby pages 1-2, smith2024aglobalchromoblastomycosis pages 4-6) | Valentin et al., 2024; Mahmoudi et al., 2024; PMID not provided in context (valentin2024chromoblastomycosisinfrench pages 4-7, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | https://doi.org/10.3390/jof10030168 |
| ITS sequencing / NGS | Species-level molecular identification from isolates or tissue (zheng2024successfulmanagementof pages 1-2, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | ITS sequence match/homology identifying etiologic fungus (e.g., *Fonsecaea monophora*, *Alternaria infectoria*) (zheng2024successfulmanagementof pages 1-2, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | No pooled sensitivity reported in the cited case reports; one strategy paper notes molecular environmental tests/metagenomics may overcome culture limitations (zheng2024successfulmanagementof pages 1-2, mahmoudi2024chromoblastomycosiscausedby pages 1-2, smith2024aglobalchromoblastomycosis pages 4-6) | Used after culture or alongside advanced diagnostics; in one 2024 case, ITS plus NGS supported *F. monophora* identification; in another, ITS sequencing confirmed *A. infectoria* (zheng2024successfulmanagementof pages 1-2, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | Zheng et al., 2024; Mahmoudi et al., 2024; PMID not provided in context (zheng2024successfulmanagementof pages 1-2, mahmoudi2024chromoblastomycosiscausedby pages 1-2) | https://doi.org/10.1186/s12941-024-00718-y |
| Dermoscopy | Surface lesion patterns that help recognize CBM and target sampling sites (ariani2023clinicalandmycological pages 6-9, ariani2023clinicalandmycological pages 9-11, zheng2024successfulmanagementof pages 1-2) | Multiple irregular/reddish-black dots; yellowish-orange ovoid structures over pink/white areas (ariani2023clinicalandmycological pages 6-9, ariani2023clinicalandmycological pages 9-11, zheng2024successfulmanagementof pages 1-2) | No sensitivity/specificity reported in available context (ariani2023clinicalandmycological pages 9-11, zheng2024successfulmanagementof pages 1-2) | Noninvasive adjunct; can guide where to sample for KOH/culture; promising but not yet well validated and may be costly in some settings (smith2024aglobalchromoblastomycosis pages 4-6, zheng2024successfulmanagementof pages 1-2) | Ariani et al., 2023; Zheng et al., 2024; PMID not provided in context (ariani2023clinicalandmycological pages 9-11, zheng2024successfulmanagementof pages 1-2) | https://doi.org/10.1186/s12941-024-00718-y |
| Reflectance confocal microscopy (RCM) | In vivo microscopic reflectance patterns within lesions (zheng2024successfulmanagementof pages 1-2) | Small round hyperreflective bodies in the reported case (zheng2024successfulmanagementof pages 1-2) | No sensitivity/specificity reported in available context (zheng2024successfulmanagementof pages 1-2) | Reported as an adjunctive, noninvasive tool in a 2024 case; not established as a standard standalone test (zheng2024successfulmanagementof pages 1-2) | Zheng et al., 2024; PMID not provided in context (zheng2024successfulmanagementof pages 1-2) | https://doi.org/10.1186/s12941-024-00718-y |
| Antifungal susceptibility testing (AFST) | In vitro antifungal susceptibility / MICs of the isolate (zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 4-6) | Lower MICs for itraconazole/terbinafine than fluconazole/amphotericin in one case; strategy papers note need to monitor rising MICs/resistance (zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 6-7) | No standardized clinical sensitivity/yield reported; used selectively in case-level work (zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 6-7) | Performed with commercial panel (YeastOne) plus CLSI M38-A3 terbinafine assay in one 2024 case; global strategy recommends increased AFST and resistance surveillance (zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 6-7) | Zheng et al., 2024; Smith et al., 2024; PMID not provided in context (zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 6-7) | https://doi.org/10.1186/s12941-024-00718-y |


*Table: This table summarizes the main diagnostic modalities used for chromoblastomycosis, what each test detects, and the quantitative evidence available from recent studies. It is useful for comparing real-world diagnostic yield and understanding how microscopy, pathology, culture, and newer adjunctive tools fit together in practice.*

### 10.3 Visual diagnostic evidence (recent; 2024)
Cropped figures from a 2024 French Guiana series illustrate KOH microscopy fumagoid cells and histopathology “copper penny” bodies in tissue. (valentin2024chromoblastomycosisinfrench media 4ac5c53a, valentin2024chromoblastomycosisinfrench media f433a202, valentin2024chromoblastomycosisinfrench media 91754828)

### 10.4 Differential diagnosis
- Clinical differentials noted include squamous cell carcinoma, tuberculosis cutis verrucosa, and other deep fungal or atypical mycobacterial infections. (ariani2023clinicalandmycological pages 6-9, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5)

## 11. Outcome / prognosis
- CBM is described as curable when diagnosed early, but long treatment courses and relapse are common when diagnosis is delayed. (smith2024aglobalchromoblastomycosis pages 2-3, valentin2024chromoblastomycosisinfrench pages 9-10)
- Complications can include lymphedema/elephantiasis and squamous cell carcinoma (including amputations in severe cases). (valentin2024chromoblastomycosisinfrench pages 2-4, smith2024aglobalchromoblastomycosis pages 4-6)
- Hospitalization outcomes (US administrative dataset, 2016–2021): mean length of stay 9.9 days; **in-hospital death 3%**; lymphedema noted in **14%** of chromoblastomycosis hospitalizations. (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5)

## 12. Treatment
### 12.1 Current standard-of-care (practice patterns and evidence base)
- There are **no universally standardized protocols**; therapy is individualized based on lesion extent, pathogen, and feasibility of physical methods. (farid2025thecurrentlandscape pages 1-2)
- Recent clinical practice synthesis recommends **surgery for recent/limited lesions** and **systemic itraconazole and/or terbinafine** for broader disease, with combinations plus physical modalities often used. (valentin2024chromoblastomycosisinfrench pages 1-2, valentin2024chromoblastomycosisinfrench pages 9-10)

### 12.2 Treatments and outcomes (with MAXO/CHEBI suggestions)
| Intervention (drug/procedure) | Mechanism/class | Typical dose/duration (as reported) | Evidence type (case series/case report/review/strategy) | Reported outcomes/response rates | Notes/implementation considerations | MAXO term suggestion | CHEBI/Drug name where applicable | Key source (citation ID) and URL |
|---|---|---|---|---|---|---|---|---|
| Itraconazole | Triazole antifungal; inhibits ergosterol biosynthesis | Commonly 200–400 mg/day; prolonged therapy for at least 6–12 months in case-series/review data; months to years may be required (ariani2023clinicalandmycological pages 9-11, farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | Case series, retrospective series, review, strategy (ariani2023clinicalandmycological pages 9-11, sanchezdiaz2025chromoblastomycosisinperu pages 1-2, farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | Most widely used systemic agent; Peruvian series mainly used itraconazole-based regimens with overall cure in 46%; monotherapy in French Guiana produced one cure with relapse at 18 months and one partial remission (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, valentin2024chromoblastomycosisinfrench pages 4-7) | First-line systemic option but long duration, relapse, cost/access issues, and drug interactions/toxicity can limit use; QT prolongation caused discontinuation in one case (smith2024aglobalchromoblastomycosis pages 2-3, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | MAXO: antifungal pharmacotherapy | CHEBI: itraconazole | (sanchezdiaz2025chromoblastomycosisinperu pages 1-2, farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) https://doi.org/10.1186/s12879-025-11475-4 ; https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.3390/jof10030168 ; https://doi.org/10.7759/cureus.73619 |
| Terbinafine | Allylamine antifungal; inhibits squalene epoxidase | 250–1000 mg/day reported; review cites 500 mg/day commonly; often prolonged (ariani2023clinicalandmycological pages 9-11, farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 4-7) | Case series, retrospective series, review (ariani2023clinicalandmycological pages 9-11, farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 4-7) | French Guiana: terbinafine ± cryotherapy in 8 patients led to 2 improvements, 1 cure, 2 ongoing treatment, 3 lost to follow-up; single-case forearm lesion failed terbinafine 250 mg/day for 3 months (valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | Considered a first-line systemic alternative with itraconazole; useful alone or with cryotherapy/surgery, but responses are variable and relapses occur (valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | MAXO: antifungal pharmacotherapy | CHEBI: terbinafine | (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.3390/jof10030168 ; https://doi.org/10.7759/cureus.73619 |
| Itraconazole + terbinafine | Combination systemic antifungal therapy | Review reports itraconazole 200–400 mg/day with terbinafine 500 mg/day; one 2024 case used itraconazole 200 mg daily + terbinafine 250 mg daily for 3 months before imiquimod was added (farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2) | Review, case report, retrospective series (farid2025thecurrentlandscape pages 2-4, sanchezdiaz2025chromoblastomycosisinperu pages 2-5, zheng2024successfulmanagementof pages 1-2) | Reported success rates range from 15% to 80% depending on severity/species; considered synergistic and useful in refractory disease; in one case regimen alone was subtherapeutic until imiquimod was added (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, zheng2024successfulmanagementof pages 1-2) | Combination often used to hasten response or in refractory disease; evidence is heterogeneous and based on small studies/case reports (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | MAXO: combination antifungal pharmacotherapy | CHEBI: itraconazole; terbinafine | (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5, zheng2024successfulmanagementof pages 1-2) https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.3390/jof10030168 ; https://doi.org/10.1186/s12879-025-11475-4 ; https://doi.org/10.1186/s12941-024-00718-y |
| Itraconazole + 5-flucytosine | Combination azole + antimetabolite antifungal | French Guiana: itraconazole 200–400 mg/day plus 5-fluorocytosine; used notably in 1982–1990 cases (valentin2024chromoblastomycosisinfrench pages 4-7) | Retrospective series, review (valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7) | French Guiana: 5 patients received regimen; outcomes included 1 relapse at 3 months, 2 therapy switches, 2 lost to follow-up; one later received itraconazole maintenance and achieved complete response (valentin2024chromoblastomycosisinfrench pages 4-7) | Can be effective but limited by 5-flucytosine toxicity; older regimen less favored now compared with itraconazole/terbinafine-based approaches (valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7) | MAXO: combination antifungal pharmacotherapy | CHEBI: itraconazole; flucytosine | (valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7) https://doi.org/10.3390/jof10030168 |
| Posaconazole | Extended-spectrum triazole antifungal | 400–800 mg/day reported for refractory chronic lesions (farid2025thecurrentlandscape pages 2-4) | Review; cited case reports/series (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 12-12) | Used successfully in refractory disease; review notes refractory cases responsive to posaconazole, but no pooled cure rate available in context (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | Reserved mainly for refractory cases or intolerance/failure of first-line therapy; access/cost may be limiting (smith2024aglobalchromoblastomycosis pages 3-4, farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | MAXO: antifungal pharmacotherapy | CHEBI: posaconazole | (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 12-12) https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.3390/jof10030168 |
| Voriconazole | Extended-spectrum triazole antifungal | 200–400 mg/day reported in review; one case of concurrent CBM/eumycetoma used 200 mg twice daily for 4 weeks with improvement; one 2024 susceptibility profile showed lower MIC than itraconazole/terbinafine (farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2) | Review, case report (farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2) | Reported as successful in refractory chronic lesions; short-course case report showed gradual clinical improvement after 4 weeks (farid2025thecurrentlandscape pages 2-4) | Alternative triazole for refractory/intolerance settings; strategy papers call for further study of voriconazole and posaconazole (smith2024aglobalchromoblastomycosis pages 3-4, farid2025thecurrentlandscape pages 2-4) | MAXO: antifungal pharmacotherapy | CHEBI: voriconazole | (smith2024aglobalchromoblastomycosis pages 3-4, farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2) https://doi.org/10.1371/journal.pntd.0012562 ; https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.1186/s12941-024-00718-y |
| Cryotherapy | Physical tissue destruction by freezing | Number of sessions varies; one case had 3 sessions with liquid nitrogen; often combined with itraconazole or terbinafine (sanchezdiaz2025chromoblastomycosisinperu pages 2-5, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | Retrospective series, case report, review (valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | Common adjunct; Peruvian series predominantly used itraconazole + cryosurgery; however relapse is frequent, and one case had little/no improvement after 3 sessions (sanchezdiaz2025chromoblastomycosisinperu pages 2-5, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | High relapse indices and risk of disfiguring scars noted in review; most useful as adjunct in localized disease (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | MAXO: cryotherapy | CHEBI: not applicable | (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.3390/jof10030168 ; https://doi.org/10.1186/s12879-025-11475-4 ; https://doi.org/10.7759/cureus.73619 |
| Surgery (wide excision / Mohs / excision with margins) | Surgical removal of infected tissue | Recommended for early/localized lesions; one case used wide local excision with 0.5 cm margins to fascia; Mohs noted as effective in review (valentin2024chromoblastomycosisinfrench pages 9-10, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | Retrospective series, case report, review/strategy (valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | French Guiana: 3 early surgical patients cured without recurrence; 1 long-standing case relapsed after surgery. Wide excision case had clear margins and no recurrence at 3 months. Mohs described as having excellent efficacy and no distant recurrence in cited review context (valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) | Best for recent, limited lesions; delayed diagnosis and deep lesions may preclude safe excision; often combined with systemic antifungals (valentin2024chromoblastomycosisinfrench pages 1-2, valentin2024chromoblastomycosisinfrench pages 9-10) | MAXO: surgical excision | CHEBI: not applicable | (valentin2024chromoblastomycosisinfrench pages 1-2, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 4-7, martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5) https://doi.org/10.3390/jof10030168 ; https://doi.org/10.7759/cureus.73619 |
| Thermotherapy / local heat | Physical heat-based local therapy | Exact temperature schedules not detailed in available context; appears as adjunct with systemic therapy in some regimens (valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5) | Review, retrospective series (valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5) | Mentioned as adjuvant/local therapy; no pooled response rate available in retrieved context (valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5) | Included among physical methods alongside cryotherapy and surgery; evidence less robust than for itraconazole/terbinafine-based therapy (valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5) | MAXO: thermotherapy | CHEBI: not applicable | (valentin2024chromoblastomycosisinfrench pages 9-10, sanchezdiaz2025chromoblastomycosisinperu pages 2-5) https://doi.org/10.3390/jof10030168 ; https://doi.org/10.1186/s12879-025-11475-4 |
| Photodynamic therapy (ALA-PDT) | Light-activated local therapy using aminolevulinic acid photosensitization | Review cites 4–9 sessions in refractory cases; another review notes ~6 applications in 10 patients (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | Review / cited case series (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 12-12) | Lesion size reportedly reduced by 80–90% after six applications in 10 patients; refractory cases improved after 4–9 sessions (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10) | Promising adjunct, especially for refractory hyperkeratotic disease; evidence remains from small series/case reports (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 12-12) | MAXO: photodynamic therapy | CHEBI: 5-aminolevulinic acid | (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10, valentin2024chromoblastomycosisinfrench pages 12-12) https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.3390/jof10030168 |
| Topical imiquimod adjunct | TLR7 agonist immune-response modifier | Topical 5% imiquimod, 0.6 g every other day in one 2024 case; used with itraconazole ± terbinafine (zheng2024successfulmanagementof pages 1-2) | Case report, review (farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2, lionakis2023immuneresponsesto pages 9-10) | Review cites lesion improvement in four patients and complete recovery in three patients with non-extensive lesions; 2024 case showed serial improvement after adding imiquimod to systemic antifungals (farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2) | May augment weak innate/TLR activation and reduce scar hyperplasia; evidence remains limited but mechanistically attractive for refractory disease (zheng2024successfulmanagementof pages 1-2, lionakis2023immuneresponsesto pages 9-10) | MAXO: topical immunomodulatory therapy | CHEBI: imiquimod | (farid2025thecurrentlandscape pages 2-4, zheng2024successfulmanagementof pages 1-2, lionakis2023immuneresponsesto pages 9-10) https://doi.org/10.1007/s12281-025-00504-z ; https://doi.org/10.1186/s12941-024-00718-y ; https://doi.org/10.1038/s41577-022-00826-w |
| AFST-guided therapy / susceptibility-informed antifungal selection | In vitro MIC-based treatment support | No universal dose; one 2024 case used Sensititre YeastOne plus CLSI M38-A3 terbinafine assay; lower MICs for itraconazole/terbinafine than fluconazole/amphotericin, with voriconazole lower still (zheng2024successfulmanagementof pages 1-2) | Case report, strategy/review (zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 6-7) | No formal response rate; strategy papers emphasize need for AFST and surveillance because resistance/rising MICs are concerns (smith2024aglobalchromoblastomycosis pages 4-6, smith2024aglobalchromoblastomycosis pages 6-7) | Useful for refractory or relapsing disease and for evaluating alternative triazoles; lack of standardized testing and limited culture recovery constrain routine use (smith2024aglobalchromoblastomycosis pages 4-6, smith2024aglobalchromoblastomycosis pages 6-7) | MAXO: antimicrobial susceptibility testing-guided therapy | CHEBI: not applicable | (smith2024aglobalchromoblastomycosis pages 4-6, zheng2024successfulmanagementof pages 1-2, smith2024aglobalchromoblastomycosis pages 6-7) https://doi.org/10.1186/s12941-024-00718-y ; https://doi.org/10.1371/journal.pntd.0012562 |


*Table: This table summarizes the main drug and procedural treatments reported for chromoblastomycosis, including typical dosing, outcome data, and implementation caveats from the retrieved context. It is useful for comparing first-line, adjunctive, and refractory-disease management options.*

### 12.3 Recent developments / adjunctive strategies
- **Imiquimod** (TLR7 agonist) is highlighted mechanistically as a way to compensate for weak innate TLR activation in *Fonsecaea* infection models and is reported as a beneficial adjunct to antifungals in small case series/case reports. (lionakis2023immuneresponsesto pages 9-10, zheng2024successfulmanagementof pages 1-2, farid2025thecurrentlandscape pages 2-4)
- **Photodynamic therapy** (ALA-PDT) is reported as a possible adjunct with large lesion-size reductions in small studies. (farid2025thecurrentlandscape pages 2-4, valentin2024chromoblastomycosisinfrench pages 9-10)

## 13. Prevention
- The 2024 global strategy explicitly emphasizes **primary prevention** through **personal protective equipment** (e.g., gloves, shoes, appropriate clothing) and programmatic measures integrated with WASH and wound management, alongside capacity building for earlier recognition and access to diagnostics/treatment. (smith2024aglobalchromoblastomycosis pages 6-7)
- WHO-roadmap-aligned actions include establishing surveillance, improving access to affordable diagnostics and treatment, creating field manuals and training health care workers, and developing rapid diagnostics and more effective therapies. (smith2024aglobalchromoblastomycosis pages 2-3)

## 14. Other species / natural disease
No naturally occurring veterinary/chronic chromoblastomycosis burden in non-human species was identified in the retrieved sources. This section requires additional targeted veterinary literature retrieval.

## 15. Model organisms and experimental systems
- **Murine experimental CBM models** support roles for inflammasome signaling (NLRP3/caspase-1/IL-18) and Th1 responses in controlling fungal load. (ferreira2025il18productionis pages 1-2)
- **In vitro macrophage systems** (THP-1) have been used to study Dectin-1-dependent recognition and melanin-mediated immune evasion. (zhong2024roleofdectin1 pages 1-2)
- **Fungal genetic tools:** split-marker/biolistic transformation enabling targeted gene inactivation (e.g., ∆trpB) in *F. pedrosoi* expands functional genomics capacity for CBM agents. (favilla2023expandingthetoolbox pages 1-2, favilla2023expandingthetoolbox pages 12-13)

## Clinical trials and real-world implementation (recent)
- **ClinicalTrials.gov observational study**: NCT06523998 (Completed). Official title: “Retrospective Descriptive Observational Study of the Epidemiological, Clinical and Therapeutic Profile of Patients With Rare Infections of Dermatological Interest … in Costa Rica From 2019–2023.” Posted 2024-07-29; completed 2024-05-24; enrollment 95. This study includes chromomycosis/chromoblastomycosis among conditions and aims to characterize risk factors, diagnostics (culture/histology/molecular), and treatments. (NCT06523998 chunk 1)

## Expert opinions and authoritative-source analysis (WHO/NTD roadmap implementation)
- The 2024 Global Chromoblastomycosis Working Group strategy argues that progress toward WHO roadmap targets is limited and highlights the need for surveillance systems, access to diagnostics/therapeutics, standardized case definitions, and integration into existing NTD infrastructure. (smith2024aglobalchromoblastomycosis pages 2-3, smith2024aglobalchromoblastomycosis pages 3-4)

## Statistics (high-value recent quantitative findings)
- French Guiana (published 2024): median time to diagnosis 4 years; lower-limb involvement 78.3%; histopathology positivity 95.7%. (valentin2024chromoblastomycosisinfrench pages 2-4, valentin2024chromoblastomycosisinfrench pages 4-7)
- Peru (published 2025; cases through 2024): average disease duration 10.7 years; pruritus 84%; pain 30%; functional limitation 30%; cure 46%. (sanchezdiaz2025chromoblastomycosisinperu pages 1-2)
- US hospitalizations (published 2025; 2016–2021): 690 hospitalization estimates; in-hospital death 3%; comorbid diabetes 33%; lymphedema 14% among chromoblastomycosis hospitalizations. (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3, smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5)

## Direct quotes from abstracts (supporting key points)
- Global strategy paper abstract: “Chromoblastomycosis, an implantation mycosis, is a neglected tropical disease that causes decreased quality of life, stigma, and disability. The global burden of disease is unknown …” (smith2024aglobalchromoblastomycosis pages 3-4)
- US hospitalization study abstract: “An estimated 690 chromoblastomycosis and phaeohyphomycotic abscess-associated hospitalizations occurred during 2016–2021. … in-hospital death occurred in 3%.” (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3)

## Limitations of this report (evidence gaps)
- Standard ontology IDs (MONDO, Orphanet, ICD-11) were not present in the retrieved full texts and were not inferred.
- Several treatment outcome metrics in the literature are derived from small series and heterogeneous regimens; high-quality randomized trials remain sparse.
- Some mechanistic and epidemiologic developments appear in 2025 publications; these were used where they reported uniquely quantitative metrics, while 2023–2024 sources were prioritized when available.


References

1. (smith2024aglobalchromoblastomycosis pages 2-3): Dallas J. Smith, Flávio Queiroz-Telles, Fahafahantsoa Rapelanoro Rabenja, Roderick Hay, Alexandro Bonifaz, Marlous L. Grijsen, Romain Blaizot, Fernando Messina, Yinggai Song, Shawn R. Lockhart, Alexander Jordan, Alyson M. Cavanaugh, Anastasia P. Litvintseva, Tom Chiller, Marco Schito, Sybren de Hoog, Vania Aparecida Vicente, Muriel Cornet, Daniel Argaw Dagne, Lala S. Ramarozatovo, Conceição de Maria Pedrozo e Silva de Azevedo, and Daniel Wagner C. L. Santos. A global chromoblastomycosis strategy and development of the global chromoblastomycosis working group. PLOS Neglected Tropical Diseases, 18:e0012562, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012562, doi:10.1371/journal.pntd.0012562. This article has 23 citations and is from a domain leading peer-reviewed journal.

2. (smith2024aglobalchromoblastomycosis pages 1-2): Dallas J. Smith, Flávio Queiroz-Telles, Fahafahantsoa Rapelanoro Rabenja, Roderick Hay, Alexandro Bonifaz, Marlous L. Grijsen, Romain Blaizot, Fernando Messina, Yinggai Song, Shawn R. Lockhart, Alexander Jordan, Alyson M. Cavanaugh, Anastasia P. Litvintseva, Tom Chiller, Marco Schito, Sybren de Hoog, Vania Aparecida Vicente, Muriel Cornet, Daniel Argaw Dagne, Lala S. Ramarozatovo, Conceição de Maria Pedrozo e Silva de Azevedo, and Daniel Wagner C. L. Santos. A global chromoblastomycosis strategy and development of the global chromoblastomycosis working group. PLOS Neglected Tropical Diseases, 18:e0012562, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012562, doi:10.1371/journal.pntd.0012562. This article has 23 citations and is from a domain leading peer-reviewed journal.

3. (martinelli2024treatmentresistantchromoblastomycosissuccessfully pages 2-5): Matthew B Martinelli, Clay J Cockerell, and Philip R Cohen. Treatment-resistant chromoblastomycosis successfully managed with surgical excision. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.73619, doi:10.7759/cureus.73619. This article has 4 citations.

4. (smith2025chromoblastomycosisandphaeohyphomycotic pages 1-3): Dallas J. Smith, Kaitlin Benedict, Shawn R. Lockhart, and Sanjay G. Revankar. Chromoblastomycosis and phaeohyphomycotic abscess-associated hospitalizations, united states, 2016–2021. PLOS Neglected Tropical Diseases, 19:e0013499, Sep 2025. URL: https://doi.org/10.1371/journal.pntd.0013499, doi:10.1371/journal.pntd.0013499. This article has 1 citations and is from a domain leading peer-reviewed journal.

5. (NCT06523998 chunk 1): Daniel Barquero Orias. A Study on Rare Dermatological Infections Conducted at Three Major Reference Hospitals in Costa Rica.. Caja Costarricense de Seguro Social. 2023. ClinicalTrials.gov Identifier: NCT06523998

6. (NCT06523998 chunk 2): Daniel Barquero Orias. A Study on Rare Dermatological Infections Conducted at Three Major Reference Hospitals in Costa Rica.. Caja Costarricense de Seguro Social. 2023. ClinicalTrials.gov Identifier: NCT06523998

7. (sanchezdiaz2025chromoblastomycosisinperu pages 1-2): Mercedes Sanchez-Diaz, Nicolas Antunez de Mayolo, Cesar Ramos, Omayra Chincha, and Beatriz Bustamante. Chromoblastomycosis in peru: a retrospective review of 13 cases. BMC Infectious Diseases, Aug 2025. URL: https://doi.org/10.1186/s12879-025-11475-4, doi:10.1186/s12879-025-11475-4. This article has 1 citations and is from a peer-reviewed journal.

8. (smith2025chromoblastomycosisandphaeohyphomycotic pages 3-5): Dallas J. Smith, Kaitlin Benedict, Shawn R. Lockhart, and Sanjay G. Revankar. Chromoblastomycosis and phaeohyphomycotic abscess-associated hospitalizations, united states, 2016–2021. PLOS Neglected Tropical Diseases, 19:e0013499, Sep 2025. URL: https://doi.org/10.1371/journal.pntd.0013499, doi:10.1371/journal.pntd.0013499. This article has 1 citations and is from a domain leading peer-reviewed journal.

9. (smith2025chromoblastomycosisandphaeohyphomycotic pages 6-8): Dallas J. Smith, Kaitlin Benedict, Shawn R. Lockhart, and Sanjay G. Revankar. Chromoblastomycosis and phaeohyphomycotic abscess-associated hospitalizations, united states, 2016–2021. PLOS Neglected Tropical Diseases, 19:e0013499, Sep 2025. URL: https://doi.org/10.1371/journal.pntd.0013499, doi:10.1371/journal.pntd.0013499. This article has 1 citations and is from a domain leading peer-reviewed journal.

10. (valentin2024chromoblastomycosisinfrench pages 1-2): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

11. (ferreira2025il18productionis pages 1-2): L. Ferreira and S. R. de Almeida. Il-18 production is required for the generation of a th1 response during experimental chromoblastomycosis. PLOS One, May 2025. URL: https://doi.org/10.1371/journal.pone.0322127, doi:10.1371/journal.pone.0322127. This article has 0 citations and is from a peer-reviewed journal.

12. (zhong2024roleofdectin1 pages 1-2): Jiaojiao Zhong, Jing Zhang, Jianchi Ma, Wen-ying Cai, Xi-qing Li, and Junmin Zhang. Role of dectin-1 in immune response of macrophages induced by fonsecaea monophora wild strain and melanin-deficient mutant strain. Mycology, 15:45-56, Sep 2024. URL: https://doi.org/10.1080/21501203.2023.2249010, doi:10.1080/21501203.2023.2249010. This article has 5 citations.

13. (lionakis2023immuneresponsesto pages 9-10): Michail S. Lionakis, Rebecca A. Drummond, and Tobias M. Hohl. Immune responses to human fungal pathogens and therapeutic prospects. Nature Reviews. Immunology, 23:1-20, Jan 2023. URL: https://doi.org/10.1038/s41577-022-00826-w, doi:10.1038/s41577-022-00826-w. This article has 349 citations.

14. (valentin2024chromoblastomycosisinfrench pages 2-4): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

15. (smith2024aglobalchromoblastomycosis pages 6-7): Dallas J. Smith, Flávio Queiroz-Telles, Fahafahantsoa Rapelanoro Rabenja, Roderick Hay, Alexandro Bonifaz, Marlous L. Grijsen, Romain Blaizot, Fernando Messina, Yinggai Song, Shawn R. Lockhart, Alexander Jordan, Alyson M. Cavanaugh, Anastasia P. Litvintseva, Tom Chiller, Marco Schito, Sybren de Hoog, Vania Aparecida Vicente, Muriel Cornet, Daniel Argaw Dagne, Lala S. Ramarozatovo, Conceição de Maria Pedrozo e Silva de Azevedo, and Daniel Wagner C. L. Santos. A global chromoblastomycosis strategy and development of the global chromoblastomycosis working group. PLOS Neglected Tropical Diseases, 18:e0012562, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012562, doi:10.1371/journal.pntd.0012562. This article has 23 citations and is from a domain leading peer-reviewed journal.

16. (valentin2024chromoblastomycosisinfrench pages 4-7): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

17. (smith2024aglobalchromoblastomycosis pages 4-6): Dallas J. Smith, Flávio Queiroz-Telles, Fahafahantsoa Rapelanoro Rabenja, Roderick Hay, Alexandro Bonifaz, Marlous L. Grijsen, Romain Blaizot, Fernando Messina, Yinggai Song, Shawn R. Lockhart, Alexander Jordan, Alyson M. Cavanaugh, Anastasia P. Litvintseva, Tom Chiller, Marco Schito, Sybren de Hoog, Vania Aparecida Vicente, Muriel Cornet, Daniel Argaw Dagne, Lala S. Ramarozatovo, Conceição de Maria Pedrozo e Silva de Azevedo, and Daniel Wagner C. L. Santos. A global chromoblastomycosis strategy and development of the global chromoblastomycosis working group. PLOS Neglected Tropical Diseases, 18:e0012562, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012562, doi:10.1371/journal.pntd.0012562. This article has 23 citations and is from a domain leading peer-reviewed journal.

18. (smith2024aglobalchromoblastomycosis pages 3-4): Dallas J. Smith, Flávio Queiroz-Telles, Fahafahantsoa Rapelanoro Rabenja, Roderick Hay, Alexandro Bonifaz, Marlous L. Grijsen, Romain Blaizot, Fernando Messina, Yinggai Song, Shawn R. Lockhart, Alexander Jordan, Alyson M. Cavanaugh, Anastasia P. Litvintseva, Tom Chiller, Marco Schito, Sybren de Hoog, Vania Aparecida Vicente, Muriel Cornet, Daniel Argaw Dagne, Lala S. Ramarozatovo, Conceição de Maria Pedrozo e Silva de Azevedo, and Daniel Wagner C. L. Santos. A global chromoblastomycosis strategy and development of the global chromoblastomycosis working group. PLOS Neglected Tropical Diseases, 18:e0012562, Oct 2024. URL: https://doi.org/10.1371/journal.pntd.0012562, doi:10.1371/journal.pntd.0012562. This article has 23 citations and is from a domain leading peer-reviewed journal.

19. (cavallone2023newimmunologicalmarkers pages 6-9): Italo N. Cavallone, Walter Belda, Caroline Heleno C. de Carvalho, Marcia D. Laurenti, and Luiz Felipe D. Passero. New immunological markers in chromoblastomycosis—the importance of pd-1 and pd-l1 molecules in human infection. Journal of Fungi, 9:1172, Dec 2023. URL: https://doi.org/10.3390/jof9121172, doi:10.3390/jof9121172. This article has 3 citations.

20. (favilla2023expandingthetoolbox pages 1-2): Luísa Dan Favilla, Tatiana Sobianski Herman, Camila da Silva Goersch, Rosangela Vieira de Andrade, Maria Sueli Soares Felipe, Anamélia Lorenzetti Bocca, and Larissa Fernandes. Expanding the toolbox for functional genomics in fonsecaea pedrosoi: the use of split-marker and biolistic transformation for inactivation of tryptophan synthase (trpb) gene. Journal of Fungi, 9:224, Feb 2023. URL: https://doi.org/10.3390/jof9020224, doi:10.3390/jof9020224. This article has 1 citations.

21. (favilla2023expandingthetoolbox pages 12-13): Luísa Dan Favilla, Tatiana Sobianski Herman, Camila da Silva Goersch, Rosangela Vieira de Andrade, Maria Sueli Soares Felipe, Anamélia Lorenzetti Bocca, and Larissa Fernandes. Expanding the toolbox for functional genomics in fonsecaea pedrosoi: the use of split-marker and biolistic transformation for inactivation of tryptophan synthase (trpb) gene. Journal of Fungi, 9:224, Feb 2023. URL: https://doi.org/10.3390/jof9020224, doi:10.3390/jof9020224. This article has 1 citations.

22. (ariani2023clinicalandmycological pages 6-9): T Ariani, Y Rizal, and RL Veroci. Clinical and mycological spectrum of chromoblastomycosis: a case series. Unknown journal, 2023.

23. (ariani2023clinicalandmycological pages 9-11): T Ariani, Y Rizal, and RL Veroci. Clinical and mycological spectrum of chromoblastomycosis: a case series. Unknown journal, 2023.

24. (mahmoudi2024chromoblastomycosiscausedby pages 1-2): Hamidreza Mahmoudi, Zahra Ramezanalipour, Mahmoud Khansari, Eelco F. J. Meijer, Shahram Mahmoudi, Bram Spruijtenburg, Abbas Rahimi Foroushani, Mohsen Gramishoar, and Hasti Kamali Sarvestani. Chromoblastomycosis caused by alternaria infectoria, concurrent with myiasis, in a recipient of a kidney transplant: a compelling case report. Frontiers in Medicine, Jul 2024. URL: https://doi.org/10.3389/fmed.2024.1396224, doi:10.3389/fmed.2024.1396224. This article has 2 citations.

25. (zheng2024successfulmanagementof pages 1-2): Jinjin Zheng, Shougang Liu, Zhenmou Xie, Yangxia Chen, Liyan Xi, Hongfang Liu, and Yinghui Liu. Successful management of chromoblastomycosis utilizing conventional antifungal agents and imiquimod therapy. Annals of Clinical Microbiology and Antimicrobials, Jun 2024. URL: https://doi.org/10.1186/s12941-024-00718-y, doi:10.1186/s12941-024-00718-y. This article has 6 citations and is from a peer-reviewed journal.

26. (valentin2024chromoblastomycosisinfrench media 4ac5c53a): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

27. (valentin2024chromoblastomycosisinfrench media f433a202): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

28. (valentin2024chromoblastomycosisinfrench media 91754828): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

29. (valentin2024chromoblastomycosisinfrench pages 9-10): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.

30. (farid2025thecurrentlandscape pages 1-2): Tahsin Farid, Keyla C. Tumas, Heather A. Stone, and Mili Duggal. The current landscape of repurposed drugs for fungal neglected tropical diseases. Current Fungal Infection Reports, May 2025. URL: https://doi.org/10.1007/s12281-025-00504-z, doi:10.1007/s12281-025-00504-z. This article has 1 citations.

31. (farid2025thecurrentlandscape pages 2-4): Tahsin Farid, Keyla C. Tumas, Heather A. Stone, and Mili Duggal. The current landscape of repurposed drugs for fungal neglected tropical diseases. Current Fungal Infection Reports, May 2025. URL: https://doi.org/10.1007/s12281-025-00504-z, doi:10.1007/s12281-025-00504-z. This article has 1 citations.

32. (sanchezdiaz2025chromoblastomycosisinperu pages 2-5): Mercedes Sanchez-Diaz, Nicolas Antunez de Mayolo, Cesar Ramos, Omayra Chincha, and Beatriz Bustamante. Chromoblastomycosis in peru: a retrospective review of 13 cases. BMC Infectious Diseases, Aug 2025. URL: https://doi.org/10.1186/s12879-025-11475-4, doi:10.1186/s12879-025-11475-4. This article has 1 citations and is from a peer-reviewed journal.

33. (valentin2024chromoblastomycosisinfrench pages 12-12): Julie Valentin, Geoffrey Grotta, Thibaut Muller, Pieter Bourgeois, Kinan Drak Alsibai, Magalie Demar, Pierre Couppie, and Romain Blaizot. Chromoblastomycosis in french guiana: epidemiology and practices, 1955–2023. Journal of Fungi, 10:168, Feb 2024. URL: https://doi.org/10.3390/jof10030168, doi:10.3390/jof10030168. This article has 7 citations.
