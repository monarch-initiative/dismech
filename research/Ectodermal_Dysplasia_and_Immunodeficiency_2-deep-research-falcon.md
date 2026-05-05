---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T18:07:15.653499'
end_time: '2026-04-24T18:32:33.969727'
duration_seconds: 1518.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ectodermal Dysplasia and Immunodeficiency 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ectodermal Dysplasia and Immunodeficiency 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ectodermal Dysplasia and Immunodeficiency 2** covering all of the
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
- **Disease Name:** Ectodermal Dysplasia and Immunodeficiency 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Ectodermal Dysplasia and Immunodeficiency 2** covering all of the
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


# Disease Characteristics Research Report: Ectodermal Dysplasia and Immunodeficiency 2 (EDID2)

## Executive summary
Ectodermal dysplasia and immunodeficiency 2 (EDID2) is an ultra-rare, autosomal dominant inborn error of immunity caused by germline **NFKBIA** (IκBα) variants that render IκBα degradation-resistant, thereby **suppressing stimulus-induced NF-κB activation**. This produces a syndromic combined immunodeficiency with classic ectodermal defects (hair/teeth/sweat gland abnormalities) and recurrent severe infections; some patients also develop prominent sterile systemic inflammation and/or autoimmune features. Pathogenic variants cluster at the **IκBα N-terminal phosphodegron (around Ser32/Ser36)** or create **N-terminal truncations** removing these residues, leading to defective IκBα phosphorylation/ubiquitination/degradation and impaired NF-κB nuclear translocation and transcriptional responses. (petersheim2018mechanismsofgenotypephenotype pages 1-6, lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2)

The most consistent actionable clinical implications are: (i) ensure **early immunologic evaluation** in any patient with ectodermal dysplasia plus infections; (ii) test **functional antibody responses**, including **anti-polysaccharide responses**; (iii) implement **immunoglobulin replacement** and **antimicrobial/antifungal prophylaxis** when indicated; and (iv) recognize that **HSCT has been high-risk** with substantial mortality and frequent persistence of partial immunodeficiency and ectodermal findings. (kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 13-16, fasshauer2024monogenicinbornerrors pages 2-4)

---

## 1. Disease information

### 1.1 Overview and current definition
EDID2 (also described in the literature as **autosomal dominant anhidrotic ectodermal dysplasia with immunodeficiency**, AD EDA-ID) is a syndromic immunodeficiency characterized by ectodermal abnormalities (hair, teeth, sweat glands) with recurrent severe infections and variable immune dysregulation, caused by heterozygous pathogenic variants in **NFKBIA**, encoding IκBα, a major inhibitor of NF-κB. (petersheim2018mechanismsofgenotypephenotype pages 1-6, derfalvi2020adaandpnp pages 13-16, chear2022anovelde pages 1-2)

A succinct mechanistic definition supported by primary literature is that EDID2 results from **IκBα variants that resist normal phosphorylation/degradation**, causing **blunted canonical NF-κB activation** after TNF/TLR/IL-1R/CD40 signaling, with downstream failure of appropriate innate/adaptive immune responses. (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, derfalvi2020adaandpnp pages 13-16)

### 1.2 Key identifiers and nomenclature
| Identifier system | ID | Name used | Source citation | URL |
|---|---|---|---|---|
| OMIM | 612132 | Ectodermal dysplasia and immunodeficiency 2 | (derfalvi2020adaandpnp pages 13-16) | https://omim.org/entry/612132 |
| MONDO | MONDO:0012806 | ectodermal dysplasia and immunodeficiency 2 | (derfalvi2020adaandpnp pages 13-16) | https://monarchinitiative.org/disease/MONDO:0012806 |
| Gene association | NFKBIA | NFKBIA-related ectodermal dysplasia with immunodeficiency 2 | (petersheim2018mechanismsofgenotypephenotype pages 1-6, derfalvi2020adaandpnp pages 13-16, schimke2013anovelgainoffunction pages 1-2) | https://www.ncbi.nlm.nih.gov/gene/4792 |
| Literature synonym | — | autosomal dominant anhidrotic ectodermal dysplasia with immunodeficiency | (petersheim2018mechanismsofgenotypephenotype pages 1-6, chear2022anovelde pages 1-2) | https://doi.org/10.1016/j.jaci.2017.05.030 |
| Literature synonym | — | autosomal-dominant EDA-ID | (derfalvi2020adaandpnp pages 13-16, chear2022anovelde pages 1-2) | https://doi.org/10.1007/978-1-4614-8678-7_172 |
| Literature synonym | — | AD EDA-ID | (petersheim2018mechanismsofgenotypephenotype pages 1-6, schimke2013anovelgainoffunction pages 1-2) | https://doi.org/10.1016/j.jaci.2017.05.030 |
| Literature synonym | — | IκBα-related EDA-ID | (derfalvi2020adaandpnp pages 13-16, schimke2013anovelgainoffunction pages 1-2) | https://doi.org/10.1007/s10875-013-9906-1 |
| Literature synonym | — | ectodermal dysplasia with immunodeficiency (NFKBIA form) | (lopezgranados2008anovelmutation pages 1-2, schimke2013anovelgainoffunction pages 1-2) | https://doi.org/10.1002/humu.20740 |
| Related but distinct disorder | OMIM 300291 / IKBKG | X-linked anhidrotic ectodermal dysplasia with immunodeficiency (XL-EDA-ID; NEMO-related), distinct from EDID2 | (lopezgranados2008anovelmutation pages 1-2, kawai2012diagnosisandtreatment pages 8-9) | https://omim.org/entry/300291 |


*Table: This table summarizes the principal identifiers and commonly used names for Ectodermal Dysplasia and Immunodeficiency 2, highlighting its OMIM and MONDO entries and its association with NFKBIA. It also distinguishes the autosomal dominant NFKBIA-related disorder from the related but separate X-linked IKBKG/NEMO form.*

**Notes on resource provenance:** The knowledge for EDID2 is derived largely from **aggregated disease resources (OMIM/MONDO)** plus **individual patient case reports and small case series** due to extreme rarity. Published numbers in reviews/summaries are on the order of tens of patients worldwide (see Epidemiology). (wen2022aheterozygousnterminal pages 1-2, derfalvi2020adaandpnp pages 13-16)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline, heterozygous pathogenic variants in **NFKBIA** (IκBα). Inheritance is **autosomal dominant**, frequently **de novo** in reported cases. (schimke2013anovelgainoffunction pages 1-2, chear2022anovelde pages 2-4, moriya2018ikbas32mutations pages 1-2)

**Variant classes:**
- Missense variants at/near the IκBα N-terminal degron **Ser32/Ser36** (e.g., Ser32 substitutions). (petersheim2018mechanismsofgenotypephenotype pages 1-6, moriya2018ikbas32mutations pages 1-2)
- N-terminal truncations eliminating these phospho-acceptor sites (e.g., early stop with downstream reinitiation producing a truncated protein). (lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2)

A concise genotype summary is provided in:
| Gene (HGNC) | Protein | Inheritance | Pathogenic mechanism | Variant hotspots/classes | Functional consequence on NF-κB signaling | Key phenotype associations | Key citations with URLs and publication year |
|---|---|---|---|---|---|---|---|
| **NFKBIA (HGNC:7797)** | **IκBα / NF-κB inhibitor alpha** | **Autosomal dominant** | **Hypermorphic / gain-of-function inhibitory effect; often functionally dominant-negative toward canonical NF-κB activation** | **Missense substitutions at or near the N-terminal degron containing Ser32/Ser36**; recurrent classes include **Ser32** and nearby residue changes; examples: **p.Ser32R**, **p.Ser32N**, **p.Ser32Cys**, **p.Met37Lys** | Mutant IκBα resists stimulus-induced phosphorylation/degradation, remains bound to NF-κB, and impairs nuclear translocation and transcriptional activation of downstream targets; point mutants are associated with stronger inhibition and more severe phenotype than truncations in comparative studies | Anhidrotic/hypohidrotic ectodermal dysplasia, sparse hair, conical/abnormal teeth, absent sweat glands, recurrent severe bacterial/fungal/viral infections, hypogammaglobulinemia or dysgammaglobulinemia/hyper-IgM-like phenotype, reduced memory B cells, reduced memory/Treg compartments, mucocutaneous candidiasis, systemic inflammation in some patients (petersheim2018mechanismsofgenotypephenotype pages 1-6, schimke2013anovelgainoffunction pages 1-2, moriya2018ikbas32mutations pages 1-2) | Petersheim et al., *J Allergy Clin Immunol* 2018, https://doi.org/10.1016/j.jaci.2017.05.030 (petersheim2018mechanismsofgenotypephenotype pages 1-6); Schimke et al., *J Clin Immunol* 2013, https://doi.org/10.1007/s10875-013-9906-1 (schimke2013anovelgainoffunction pages 1-2); Moriya et al., *J Clin Immunol* 2018, https://doi.org/10.1007/s10875-018-0522-y (moriya2018ikbas32mutations pages 1-2); Chear et al., *Genes* 2022, https://doi.org/10.3390/genes13101900 (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2) |
| **NFKBIA (HGNC:7797)** | **IκBα / NF-κB inhibitor alpha** | **Autosomal dominant** | **Hypermorphic truncation allele producing degradation-resistant N-terminally truncated protein** | **N-terminal truncations lacking Ser32/Ser36 phosphorylation sites**; example: **p.Glu14\*** with downstream reinitiation generating truncated IκBα | Loss of N-terminal phospho-acceptor region prevents normal IKK-mediated degradation; truncated protein persists and suppresses NF-κB activation in lymphocytes/monocytes; generally associated with somewhat milder signaling impairment than Ser32/Ser36 point mutants in genotype-phenotype analyses | Early-onset ectodermal dysplasia with immunodeficiency, anhidrosis, failure to thrive, recurrent diarrhea, opportunistic infection (including *Pneumocystis*), bacteremia, interstitial lung disease, severe infantile course with poor transplant outcome in reported cases (lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2) | Lopez-Granados et al., *Hum Mutat* 2008, https://doi.org/10.1002/humu.20740 (lopezgranados2008anovelmutation pages 1-2); Wen et al., *Genes & Diseases* 2022, https://doi.org/10.1016/j.gendis.2021.03.005 (wen2022aheterozygousnterminal pages 1-2); Petersheim et al., *J Allergy Clin Immunol* 2018, https://doi.org/10.1016/j.jaci.2017.05.030 (petersheim2018mechanismsofgenotypephenotype pages 1-6) |
| **NFKBIA (HGNC:7797)** | **IκBα / NF-κB inhibitor alpha** | **Usually de novo autosomal dominant** | **GOF/hypermorphic inhibitory allele affecting conserved degron/post-translational regulation** | **Degron variant p.Ser32Cys** in the conserved **Asp31-Ser36** motif | Predicted loss of phosphorylation at Ser32 and altered post-translational modification state, impairing NF-κB activation; mechanistically linked to defective class-switch recombination / somatic hypermutation via reduced induction of AID/UNG downstream of NF-κB | Mild ectodermal dysplasia with dysgammaglobulinemia or hyper-IgM-like presentation, persistent mucocutaneous candidiasis, severe recurrent bacterial/fungal infections, low IgG/IgA with elevated IgM, suspicion of Hyper-IgM syndrome before molecular diagnosis (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2) | Chear et al., *Genes* 2022, https://doi.org/10.3390/genes13101900 (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2) |
| **NFKBIA (HGNC:7797)** | **IκBα / NF-κB inhibitor alpha** | **Autosomal dominant** | **GOF/hypermorphic missense affecting residue adjacent to degron** | **p.Met37Lys** | Abolished IκBα degradation after TNF-α/TLR stimulation, impaired NF-κB nuclear translocation, reduced NF-κB-dependent reporter activity, impaired cytokine responses including IL-6 and IL-10 pathways | Classic ectodermal dysplasia with profound combined immunodeficiency, recurrent mucocutaneous candidiasis, decreased IL-17+ T cells, and polyendocrinopathy/hypothyroidism-hypopituitarism in the reported patient (schimke2013anovelgainoffunction pages 1-2) | Schimke et al., *J Clin Immunol* 2013, https://doi.org/10.1007/s10875-013-9906-1 (schimke2013anovelgainoffunction pages 1-2) |
| **NFKBIA (HGNC:7797)** | **IκBα / NF-κB inhibitor alpha** | **Autosomal dominant, often de novo** | **GOF/hypermorphic Ser32 mutants with particularly strong inhibitory effect** | **p.Ser32Arg, p.Ser32Asn** | Strong suppression of NF-κB activation in functional assays; associated with especially severe impairment of immune-cell differentiation and inflammatory control | Ectodermal dysplasia plus severe noninfectious systemic inflammation, persistent CRP elevation, pulmonary infiltrates, CNS inflammation, lymphocytosis, low immunoglobulins, near-absence of memory T cells/Tregs, reduced memory B cells; steroids may control inflammation but transplant benefit may be incomplete (moriya2018ikbas32mutations pages 1-2) | Moriya et al., *J Clin Immunol* 2018, https://doi.org/10.1007/s10875-018-0522-y (moriya2018ikbas32mutations pages 1-2) |
| **NFKBIA (HGNC:7797)** | **IκBα / NF-κB inhibitor alpha** | **Autosomal dominant** | **Overall disease mechanism across EDID2** | **Published mutational spectrum includes missense variants at/near Ser32/Ser36 and N-terminal truncations**; reported totals in reviews/case summaries were approximately **11 mutations in 14 patients** or **~19 patients** by 2020-2022 literature snapshots | Shared mechanism is impaired stimulus-induced IκBα turnover, defective canonical NF-κB signaling, and secondary defects in TIR/TNFR1/CD40/TCR-linked immune responses; comparative work also implicates impaired noncanonical NF-κB/lymphoid organogenesis in some alleles | Broad phenotype spectrum: ectodermal malformations, recurrent severe infections, poor vaccine/polysaccharide antibody responses, enlarged total B-cell pool with reduced/absent memory B cells, defective T-cell proliferation, chronic diarrhea/colitis, occasional mycobacterial disease, and incomplete correction after HSCT (petersheim2018mechanismsofgenotypephenotype pages 1-6, wen2022aheterozygousnterminal pages 1-2, derfalvi2020adaandpnp pages 13-16) | Petersheim et al., *J Allergy Clin Immunol* 2018, https://doi.org/10.1016/j.jaci.2017.05.030 (petersheim2018mechanismsofgenotypephenotype pages 1-6); Wen et al., *Genes & Diseases* 2022, https://doi.org/10.1016/j.gendis.2021.03.005 (wen2022aheterozygousnterminal pages 1-2); Derfalvi, *Encyclopedia of Medical Immunology* 2020, https://doi.org/10.1007/978-1-4614-8678-7_172 (derfalvi2020adaandpnp pages 13-16) |


*Table: This table summarizes the genetic etiology of ectodermal dysplasia and immunodeficiency 2, focusing on pathogenic NFKBIA variant classes, their effects on NF-κB signaling, and the main associated clinical phenotypes. It is useful for linking genotype classes to mechanism and disease presentation.*

### 2.2 Risk factors
Because EDID2 is Mendelian, **the dominant risk factor is carrying a pathogenic NFKBIA variant** (often de novo). No robust environmental susceptibility factors were identified in the retrieved corpus.

### 2.3 Protective factors / gene–environment interactions
No validated protective genetic variants or gene–environment interaction studies specific to EDID2 were identified in the retrieved papers.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with HPO suggestions)
| Domain | Phenotype | Suggested HPO term(s) | Typical onset/course | Notes/frequency | Key citations |
|---|---|---|---|---|---|
| Ectodermal | Sparse scalp hair / hypotrichosis | HP:0001006 Hypotrichosis | Congenital or infancy; persistent | Recurrently reported across NFKBIA cases; part of the core ectodermal phenotype in AD EDA-ID (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, moriya2018ikbas32mutations pages 1-2) | (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, moriya2018ikbas32mutations pages 1-2) |
| Ectodermal | Absent or reduced sweating / anhidrosis-hypohidrosis | HP:0000977 Hypohidrosis; HP:0000963 Abnormality of sweating | Congenital/early infancy; lifelong | Classic feature; reported with absent sweat glands and abnormal sweat testing in severe infantile cases (lopezgranados2008anovelmutation pages 1-2, derfalvi2020adaandpnp pages 13-16) | (lopezgranados2008anovelmutation pages 1-2, derfalvi2020adaandpnp pages 13-16) |
| Ectodermal | Absent sweat glands | HP:0030436 Aplasia/Hypoplasia of sweat glands | Congenital; structural | Pathology-confirmed in some cases; useful distinguishing sign of EDID2 from isolated antibody defects (lopezgranados2008anovelmutation pages 1-2, moriya2018ikbas32mutations pages 1-2) | (lopezgranados2008anovelmutation pages 1-2, moriya2018ikbas32mutations pages 1-2) |
| Ectodermal | Conical or abnormal teeth / tooth anomalies | HP:0000699 Conical teeth; HP:0006483 Abnormality of dentition | Childhood, when dentition emerges; persistent | Common ectodermal clue; conical teeth specifically described in severe S32-mutant cases (moriya2018ikbas32mutations pages 1-2) | (moriya2018ikbas32mutations pages 1-2, derfalvi2020adaandpnp pages 13-16) |
| Ectodermal | Sparse or absent eyebrows | HP:0045075 Sparse eyebrow | Infancy; persistent | Described in infant truncation case; often accompanies hypotrichosis (wen2022aheterozygousnterminal pages 1-2) | (wen2022aheterozygousnterminal pages 1-2) |
| Immune | Hypogammaglobulinemia | HP:0004313 Decreased circulating immunoglobulin level | Infancy/early childhood; chronic | Major immune phenotype; may coexist with severe infections and poor vaccine responses (lopezgranados2008anovelmutation pages 1-2, moriya2018ikbas32mutations pages 1-2, kawai2012diagnosisandtreatment pages 8-9) | (lopezgranados2008anovelmutation pages 1-2, moriya2018ikbas32mutations pages 1-2, kawai2012diagnosisandtreatment pages 8-9) |
| Immune | Dysgammaglobulinemia / hyper-IgM-like pattern | HP:0012140 Abnormal immunoglobulin level; HP:0003237 Hypergammaglobulinemia of IgM | Infancy or toddler years; chronic/variable | Case reports describe elevated IgM with low IgG/IgA despite preserved CD40/CD40L; can mimic Hyper-IgM syndrome (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2) | (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2) |
| Immune | Poor or absent vaccine antibody responses, especially to polysaccharide antigens | HP:0033258 Abnormality of humoral immune system physiology | Early childhood after immunization/testing; persistent | A key diagnostic clue; reviews emphasize impaired response to polysaccharide antigens despite some preserved protein responses. Reported in NFKBIA series and highlighted for routine workup (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 8-9, fasshauer2024monogenicinbornerrors pages 2-4) | (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 8-9, fasshauer2024monogenicinbornerrors pages 2-4) |
| Immune | Reduced or absent memory B cells | HP:0005428 Absent B cells is too narrow; suggested: HP:0011839 Abnormal B-cell subset distribution | Childhood; persistent | Recurrent across reported patients; Derfalvi summary notes enlarged total B-cell counts with reduced/absent memory B cells (derfalvi2020adaandpnp pages 13-16, moriya2018ikbas32mutations pages 1-2) | (derfalvi2020adaandpnp pages 13-16, moriya2018ikbas32mutations pages 1-2) |
| Immune | Predominance of naïve T cells / absent memory T cells | HP:0011837 Abnormal T-cell subset distribution | Childhood; persistent | Near absence of CD45RO+ memory T cells reported in severe inflammatory S32-mutant cases; supports combined immunodeficiency phenotype (moriya2018ikbas32mutations pages 1-2, giancane2013anhidroticectodermaldysplasia pages 3-3) | (moriya2018ikbas32mutations pages 1-2, giancane2013anhidroticectodermaldysplasia pages 3-3) |
| Immune | Reduced/absent regulatory T cells | HP:0012441 Abnormal regulatory T-cell count | Childhood; persistent | Reported in severe NFKBIA S32-mutant patients with inflammation (moriya2018ikbas32mutations pages 1-2) | (moriya2018ikbas32mutations pages 1-2) |
| Immune | Impaired T-cell proliferation / defective TCR-mediated responses | HP:0002843 Abnormal T-cell function | Childhood; persistent | Seen in review summaries and clinical reports; contributes to combined immunodeficiency phenotype (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 6-7, kawai2012diagnosisandtreatment pages 7-8) | (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 6-7, kawai2012diagnosisandtreatment pages 7-8) |
| Immune | Impaired innate receptor signaling (TLR/IL-1R/TNFR1/CD40 pathways) | HP:0033255 Abnormal innate immunity | Congenital molecular defect; detected on functional testing | Central mechanistic immune abnormality of EDID2; explains susceptibility to bacterial, fungal, and mycobacterial pathogens (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 9-10) | (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 9-10) |
| Infectious | Recurrent severe bacterial infections | HP:0002718 Recurrent bacterial infections | Infancy/early childhood; recurrent | Common and often life-threatening; organisms reported include Klebsiella, Pseudomonas, Haemophilus, Streptococcus, Staphylococcus (derfalvi2020adaandpnp pages 13-16) | (derfalvi2020adaandpnp pages 13-16) |
| Infectious | Recurrent pneumonia / severe sinopulmonary infection | HP:0006536 Recurrent pneumonia; HP:0002205 Recurrent respiratory infections | Infancy/early childhood; recurrent | Frequent presenting feature; can progress to respiratory failure or bronchiectatic damage if diagnosis delayed (wen2022aheterozygousnterminal pages 1-2, chear2022anovelde pages 2-4, fasshauer2024monogenicinbornerrors pages 2-4) | (wen2022aheterozygousnterminal pages 1-2, chear2022anovelde pages 2-4, fasshauer2024monogenicinbornerrors pages 2-4) |
| Infectious | Chronic mucocutaneous candidiasis / oral candidiasis | HP:0002721 Chronic mucocutaneous candidiasis; HP:0000202 Oral thrush | Infancy/childhood; recurrent or persistent | Strongly represented in NFKBIA cases, including oral and perianal thrush; linked with impaired IL-17 immunity in one patient (schimke2013anovelgainoffunction pages 1-2, chear2022anovelde pages 2-4, moriya2018ikbas32mutations pages 1-2) | (schimke2013anovelgainoffunction pages 1-2, chear2022anovelde pages 2-4, moriya2018ikbas32mutations pages 1-2) |
| Infectious | Opportunistic infection including Pneumocystis jirovecii | HP:0002724 Opportunistic infections | Infancy; severe | Reported in severe truncation cases and highlighted in reviews as an important complication (lopezgranados2008anovelmutation pages 1-2, kawai2012diagnosisandtreatment pages 7-8) | (lopezgranados2008anovelmutation pages 1-2, kawai2012diagnosisandtreatment pages 7-8) |
| Infectious | Mycobacterial susceptibility / BCG disease | HP:0002728 Mycobacterial infection, recurrent | Infancy/childhood; risk after BCG exposure | Reported in some AD EDA-ID patients and emphasized in reviews; relevant to vaccine decisions and prophylaxis (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 9-10, derfalvi2020adaandpnp pages 16-17) | (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 9-10, derfalvi2020adaandpnp pages 16-17) |
| Inflammatory | Persistent fever and elevated inflammatory markers | HP:0001945 Fever; HP:0011227 Elevated C-reactive protein level | Infancy/childhood; episodic or chronic | Some NFKBIA mutants, especially Ser32 substitutions, show severe noninfectious systemic inflammation with high CRP and leukocytosis (moriya2018ikbas32mutations pages 1-2) | (moriya2018ikbas32mutations pages 1-2) |
| Inflammatory | Skin rash / erythema | HP:0000988 Skin rash; HP:0001047 Erythema | Early infancy; persistent or relapsing | Seen in inflammatory presentations; may precede systemic manifestations (moriya2018ikbas32mutations pages 1-2) | (moriya2018ikbas32mutations pages 1-2) |
| Inflammatory | Pulmonary inflammatory infiltrates / consolidations | HP:0002209 Pulmonary infiltrates | Infancy/childhood; relapsing or persistent | Described in severe inflammatory S32-mutant disease and infectious pneumonia presentations (moriya2018ikbas32mutations pages 1-2, wen2022aheterozygousnterminal pages 1-2) | (moriya2018ikbas32mutations pages 1-2, wen2022aheterozygousnterminal pages 1-2) |
| Inflammatory | CNS inflammation / seizures / MRI lesions | HP:0001250 Seizure; HP:0012638 Abnormality of CNS white matter | Infancy/childhood; severe episodic | Reported in severe S32-mutant disease with steroid-responsive brain inflammation (moriya2018ikbas32mutations pages 1-2) | (moriya2018ikbas32mutations pages 1-2) |
| GI | Chronic diarrhea | HP:0002028 Chronic diarrhea | Infancy; persistent or recurrent | Common presenting problem in severe infantile cases; may accompany infections or inflammatory bowel disease–like manifestations (lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2) | (lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2) |
| GI | Colitis / enterocolitis | HP:0002037 Inflammatory abnormality of the intestine | Childhood; chronic/relapsing | Reported in EDA-ID reviews; may respond to corticosteroids, and can persist despite HSCT in broader EDA-ID experience (kawai2012diagnosisandtreatment pages 8-9, kawai2012diagnosisandtreatment pages 9-10, kawai2012diagnosisandtreatment pages 10-11) | (kawai2012diagnosisandtreatment pages 8-9, kawai2012diagnosisandtreatment pages 9-10, kawai2012diagnosisandtreatment pages 10-11) |
| GI | Failure to thrive | HP:0001508 Failure to thrive | Infancy; progressive if untreated | Reported in severe infantile truncation case with recurrent infection and diarrhea (lopezgranados2008anovelmutation pages 1-2) | (lopezgranados2008anovelmutation pages 1-2) |
| Endocrine | Polyendocrinopathy / hypopituitarism / hypothyroidism | HP:0000820 Abnormality of the thyroid gland; HP:0000837 Hypopituitarism; HP:0003117 Polyendocrine abnormality | Childhood; chronic | Not universal, but important expansion of phenotype in p.M37K case with profound immunodeficiency and reduced IL-17+ T cells (schimke2013anovelgainoffunction pages 1-2) | (schimke2013anovelgainoffunction pages 1-2) |
| Epidemiology / spectrum | Reported case burden in literature | HP:0000007 Autosomal dominant inheritance | Ultra-rare; congenital Mendelian disease | Literature snapshots report approximately 14 patients with 11 mutations (2020 summary) and ~19 reported patients by 2022, indicating extreme rarity and likely ascertainment from case reports/series rather than registries (derfalvi2020adaandpnp pages 13-16, wen2022aheterozygousnterminal pages 1-2) | (derfalvi2020adaandpnp pages 13-16, wen2022aheterozygousnterminal pages 1-2) |


*Table: This table summarizes the reported clinical and immunologic spectrum of NFKBIA-related ectodermal dysplasia and immunodeficiency 2, with suggested HPO mappings, typical onset, and practical notes from key case reports and reviews. It is useful for disease knowledge base curation and phenotype-driven diagnostic recognition.*

**Key phenotype themes supported by primary literature**:
- **Ectodermal dysplasia:** hypotrichosis/sparse hair, abnormal or conical teeth, and reduced or absent sweating/sweat glands. (lopezgranados2008anovelmutation pages 1-2, moriya2018ikbas32mutations pages 1-2)
- **Immunodeficiency:** hypogammaglobulinemia or dysgammaglobulinemia/hyper-IgM-like patterns, poor vaccine responses, reduced memory B cells, and in some patients profound T-cell subset abnormalities (absent memory T cells, reduced Tregs). (chear2022anovelde pages 2-4, moriya2018ikbas32mutations pages 1-2, derfalvi2020adaandpnp pages 13-16)
- **Infectious susceptibility:** recurrent severe bacterial infections (including invasive disease), pneumonia, chronic mucocutaneous candidiasis, opportunistic infections including *Pneumocystis*, and occasional mycobacterial disease (including in the broader EDA-ID spectrum). (lopezgranados2008anovelmutation pages 1-2, derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 7-8)
- **Inflammation/immune dysregulation:** a subset—especially with Ser32 variants—can have severe noninfectious systemic inflammation (persistent CRP elevation, CNS inflammation) that is steroid-responsive but may recur after transplantation with mixed chimerism. (moriya2018ikbas32mutations pages 1-2)
- **Endocrinopathy (subset):** polyendocrinopathy/hypothyroidism/hypopituitarism reported in at least one NFKBIA GOF case. (schimke2013anovelgainoffunction pages 1-2)

### 3.2 Quality-of-life impact
Direct validated QoL instrument data (e.g., SF-36/EQ-5D) were not found in the retrieved corpus. However, case reports and reviews describe prolonged hospitalizations, recurrent severe infections, chronic prophylaxis/IVIG dependence, and persistent ectodermal manifestations, all of which strongly imply substantial QoL burden. (chear2022anovelde pages 2-4, derfalvi2020adaandpnp pages 13-16)

---

## 4. Genetic/molecular information

### 4.1 Causal gene
- **NFKBIA** (HGNC:7797), encoding **IκBα**. (petersheim2018mechanismsofgenotypephenotype pages 1-6, schimke2013anovelgainoffunction pages 1-2)

### 4.2 Pathogenic variants and functional consequences
Mechanistically, IKK-mediated phosphorylation of IκBα at **Ser32/Ser36** normally triggers ubiquitination and proteasomal degradation; EDID2 variants interfere with this step and lead to **persistent inhibition of NF-κB**. (wen2022aheterozygousnterminal pages 1-2, derfalvi2020adaandpnp pages 13-16)

**Genotype–phenotype correlation:** Petersheim et al. report that **point mutants accumulate at higher levels than truncations** and are associated with **greater clinical severity** and larger deficits in both canonical and non-canonical NF-κB pathway readouts in stimulated patient fibroblasts. (petersheim2018mechanismsofgenotypephenotype pages 1-6)

### 4.3 Molecular pathway mapping (ontology suggestions)
- **Canonical NF-κB signaling** (Reactome/KEGG concept); suggested GO biological process terms:
  - GO:0043122 “regulation of I-kappaB kinase/NF-kappaB signaling”
  - GO:0038061 “NIK/NF-kappaB signaling” (for the noncanonical component implicated in lymphoid organogenesis phenotypes)

Cell types (Cell Ontology suggestions) implicated by functional assays and phenotype:
- CL:0000542 “lymphocyte” (broad)
- CL:0000236 “B cell”; CL:0000084 “T cell”; CL:0000623 “natural killer cell”
- CL:0000451 “dendritic cell” (based on TLR-driven cytokine defects and mouse DC subset changes)

---

## 5. Environmental information
No EDID2-specific environmental toxin/lifestyle risk literature was identified in the retrieved corpus. Infectious exposures (e.g., respiratory pathogens; Candida; and in some contexts live mycobacterial exposure such as BCG) are clinically important because of heightened susceptibility. (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 9-10)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → pathway defect → phenotype)
1. **Germline NFKBIA variant** produces a **degradation-resistant IκBα** (by disrupting the Ser32/Ser36 phosphodegron or deleting it). (lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2)
2. Impaired IκBα turnover prevents normal **NF-κB nuclear translocation** and **NF-κB-dependent transcription** after TNF/TLR/IL-1R/CD40 stimulation. (schimke2013anovelgainoffunction pages 1-2, chear2022anovelde pages 2-4)
3. Downstream consequences include:
   - **Innate immune defects** (blunted cytokine production to TLR ligands; impaired IL-1R/TLR4 activation). (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2)
   - **Humoral immune failure** (poor specific antibody responses, impaired responses to polysaccharide vaccines/antigens; memory B-cell defects). (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 8-9)
   - **Combined immune deficiency features** (abnormal T-cell subset distribution and T-cell functional defects in severe cases). (moriya2018ikbas32mutations pages 1-2, giancane2013anhidroticectodermaldysplasia pages 3-3)
4. Clinical manifestations: recurrent severe infections, opportunistic infections, chronic candidiasis, ectodermal dysplasia, and (in some) systemic inflammation/autoimmunity. (derfalvi2020adaandpnp pages 13-16, moriya2018ikbas32mutations pages 1-2)

### 6.2 Mechanistic evidence from functional studies
- Schimke et al. report an NFKBIA GOF variant with **“abolished IκB-α degradation after TNF-α and TLR stimulation”** and impaired NF-κB activation with broad cytokine defects, consistent with hypermorphic inhibition. (schimke2013anovelgainoffunction pages 1-2)
- Wen et al. describe impaired NF-κB translocation and defective IL-1R/TLR4 pathway activation in a truncation case. (wen2022aheterozygousnterminal pages 1-2)

### 6.3 Molecular profiling / omics
EDID2-specific systematic transcriptomic/proteomic/metabolomic cohort studies were not found in the retrieved corpus; existing evidence is largely pathway-functional (cytokine readouts, reporter assays, immunoblotting). (petersheim2018mechanismsofgenotypephenotype pages 1-6, schimke2013anovelgainoffunction pages 1-2)

---

## 7. Anatomical structures affected

**Primary tissues/organs:**
- Ectodermal appendages: hair follicles (hypotrichosis), teeth (conical/abnormal dentition), eccrine sweat glands (hypoplasia/aplasia). (lopezgranados2008anovelmutation pages 1-2, moriya2018ikbas32mutations pages 1-2)
- Immune system: secondary lymphoid tissues (functional impairment; in model organism, absent lymph nodes/Peyer’s patches and disorganized spleen). (mooster2015defectivelymphoidorganogenesis pages 2-3)

UBERON suggestions:
- UBERON:0002106 “spleen”; UBERON:0000029 “lymph node”; UBERON:0001085 “Peyer’s patch”; UBERON:0001003 “skin”; UBERON:0000970 “tooth”; UBERON:0001820 “sweat gland”.

---

## 8. Temporal development

**Onset:** commonly **infancy/early childhood**, with ectodermal features often congenital and immunologic/infectious manifestations presenting early (including severe pneumonia, diarrhea, candidiasis, sepsis). (lopezgranados2008anovelmutation pages 1-2, wen2022aheterozygousnterminal pages 1-2, chear2022anovelde pages 2-4)

**Course/progression:** recurrent severe infections and chronic immune dysfunction; a subset with Ser32 variants can have persistent inflammatory disease requiring immunosuppression. (moriya2018ikbas32mutations pages 1-2)

---

## 9. Inheritance and population

### 9.1 Inheritance
**Autosomal dominant**; many reported cases are **de novo**. (schimke2013anovelgainoffunction pages 1-2, moriya2018ikbas32mutations pages 1-2)

### 9.2 Epidemiology
No robust prevalence/incidence estimates specific to EDID2 were identified in the retrieved corpus. Available quantitative information is limited to **case-count snapshots** in reviews/case series summaries:
- A 2020 summary describes **“14 patients with 11 mutations”** (literature to that point). (derfalvi2020adaandpnp pages 13-16)
- A 2022 report notes **~19 reported patients** and distribution of variant classes (point mutants at/near S32/S36; truncations; mosaic). (wen2022aheterozygousnterminal pages 1-2)

These figures reflect published case ascertainment rather than population-based prevalence.

---

## 10. Diagnostics

### 10.1 Recommended diagnostic approach (tests + rationale)
| Category | Specific action | Rationale / what it detects | Real-world implementation notes | Outcome data / statistics when available | Key citations with URLs and publication years |
|---|---|---|---|---|---|
| Diagnostic test | Quantitative immunoglobulins (IgG, IgA, IgM) | Detects hypogammaglobulinemia or dysgammaglobulinemia/hyper-IgM-like patterns reported in EDID2 | Basic first-line immune workup in infants/children with ectodermal dysplasia plus recurrent infection; abnormalities may be variable, so normal total IgG does not exclude disease (derfalvi2020adaandpnp pages 13-16, chear2022anovelde pages 2-4, kawai2012diagnosisandtreatment pages 7-8) | Low Ig levels reported in severe NFKBIA cases; hyper-IgM-like phenotype also described (chear2022anovelde pages 2-4, moriya2018ikbas32mutations pages 1-2) | Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172; Chear et al. 2022 https://doi.org/10.3390/genes13101900; Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446 (derfalvi2020adaandpnp pages 13-16, chear2022anovelde pages 2-4, kawai2012diagnosisandtreatment pages 7-8) |
| Diagnostic test | Vaccine antibody titers, including protein antigens | Assesses functional humoral immunity and specific antibody production | Should be part of routine workup because EDID2 can show absent/poor specific antibodies even when some quantitative immunoglobulins are preserved (kawai2012diagnosisandtreatment pages 6-7, derfalvi2020adaandpnp pages 13-16) | Poor or absent vaccine antibody responses repeatedly reported in summaries of AD EDA-ID (derfalvi2020adaandpnp pages 13-16) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172 (kawai2012diagnosisandtreatment pages 6-7, derfalvi2020adaandpnp pages 13-16) |
| Diagnostic test | Polysaccharide response testing (e.g., pneumococcal polysaccharide antibodies pre/post vaccination) | Detects impaired IgG response to polysaccharide antigens, a key clue in NF-κB-pathway IEI | Particularly important because basic workup may miss monogenic IEI with normal total IgG but defective anti-polysaccharide responses; recommended even when protein vaccine responses are preserved (kawai2012diagnosisandtreatment pages 8-9, fasshauer2024monogenicinbornerrors pages 2-4) | 2024 review emphasizes that delayed diagnosis without anti-polysaccharide testing can lead to irreversible damage such as bronchiectasis (fasshauer2024monogenicinbornerrors pages 2-4) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Fasshauer et al. 2024 https://doi.org/10.3389/fped.2024.1386959 (kawai2012diagnosisandtreatment pages 8-9, fasshauer2024monogenicinbornerrors pages 2-4) |
| Diagnostic test | Lymphocyte subset immunophenotyping, including memory B cells, memory T cells, Tregs, NK cells | Defines combined immunodeficiency phenotype and immune dysregulation | Useful because EDID2 often shows enlarged total B-cell counts with reduced/absent memory B cells, naïve-predominant T-cell compartments, reduced Tregs, and sometimes NK defects (derfalvi2020adaandpnp pages 13-16, moriya2018ikbas32mutations pages 1-2, kawai2012diagnosisandtreatment pages 6-7) | Severe S32-mutant cases showed near absence of memory T cells and Tregs plus reduced memory B cells (moriya2018ikbas32mutations pages 1-2) | Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172; Moriya et al. 2018 https://doi.org/10.1007/s10875-018-0522-y; Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446 (derfalvi2020adaandpnp pages 13-16, moriya2018ikbas32mutations pages 1-2, kawai2012diagnosisandtreatment pages 6-7) |
| Diagnostic test | T-cell proliferation / TCR-mediated functional assays | Detects defective adaptive cellular signaling downstream of NF-κB | Recommended when recurrent/opportunistic infections or inflammatory features suggest combined immunodeficiency; abnormalities may help distinguish EDID2 from isolated ectodermal dysplasia (kawai2012diagnosisandtreatment pages 6-7, derfalvi2020adaandpnp pages 13-16, giancane2013anhidroticectodermaldysplasia pages 3-3) | Impaired T-cell responses are a recurrent feature in reported series/reviews (derfalvi2020adaandpnp pages 13-16, giancane2013anhidroticectodermaldysplasia pages 3-3) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172; Giancane et al. 2013 https://doi.org/10.1016/j.jaci.2013.05.034 (kawai2012diagnosisandtreatment pages 6-7, derfalvi2020adaandpnp pages 13-16, giancane2013anhidroticectodermaldysplasia pages 3-3) |
| Diagnostic test | Innate signaling assays (TLR, IL-1R, TNFR1, CD40 pathways; cytokine readouts) | Detects the pathway-level defect caused by degradation-resistant IκBα and impaired NF-κB activation | Helpful when diagnosis is uncertain or phenotype is atypical; can show defective IL-1R/TLR4 signaling and reduced cytokine induction after stimulation (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, kawai2012diagnosisandtreatment pages 9-10) | Functional defects documented in case reports include impaired IL-6 secretion and defective NF-κB nuclear translocation (schimke2013anovelgainoffunction pages 1-2) | Wen et al. 2022 https://doi.org/10.1016/j.gendis.2021.03.005; Schimke et al. 2013 https://doi.org/10.1007/s10875-013-9906-1; Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446 (wen2022aheterozygousnterminal pages 1-2, schimke2013anovelgainoffunction pages 1-2, kawai2012diagnosisandtreatment pages 9-10) |
| Diagnostic test | Genetic confirmation with NFKBIA sequencing, targeted panel, WES | Confirms EDID2 and identifies variant class (Ser32/Ser36-adjacent missense vs N-terminal truncation) | NGS/WES is especially useful when phenotype mimics Hyper-IgM syndrome or when ectodermal findings are subtle; de novo variants are common (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2) | 2022 review/case notes ~13 distinct NFKBIA mutations reported; 2022 truncation review mentions ~19 patients reported (chear2022anovelde pages 1-2, wen2022aheterozygousnterminal pages 1-2) | Chear et al. 2022 https://doi.org/10.3390/genes13101900; Wen et al. 2022 https://doi.org/10.1016/j.gendis.2021.03.005 (chear2022anovelde pages 2-4, chear2022anovelde pages 1-2, wen2022aheterozygousnterminal pages 1-2) |
| Management | Early empiric intravenous antibiotics for suspected serious infection | Addresses high risk of rapid progression/sepsis in immunodeficient patients | Reviews emphasize prompt treatment because some patients may not mount robust fever or CRP responses; threshold for treatment should be low (kawai2012diagnosisandtreatment pages 8-9) | No response-rate statistics given, but recommendation is strong due to recurrent life-threatening infections (kawai2012diagnosisandtreatment pages 8-9) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446 (kawai2012diagnosisandtreatment pages 8-9) |
| Management | Immunoglobulin replacement (IVIG or SCIG) | Replaces deficient antibody function and compensates for poor vaccine/polysaccharide responses | Recommended for most/all AD EDA-ID patients with antibody dysfunction; used long term in real-world case management (kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 13-16) | In Derfalvi summary, 2 non-HSCT patients remained on IVIG; among 5 HSCT survivors, 4 had ongoing partial immunodeficiency requiring IVIG (derfalvi2020adaandpnp pages 13-16) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172 (kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 13-16) |
| Management | TMP-SMX (co-trimoxazole) prophylaxis | Reduces risk of recurrent bacterial infection and Pneumocystis | Strongly recommended in EDA-ID reviews; also used in individual NFKBIA cases alongside IVIG (kawai2012diagnosisandtreatment pages 8-9, chear2022anovelde pages 2-4) | Case-level use documented in 2022 NFKBIA patient receiving co-trimoxazole prophylaxis (chear2022anovelde pages 2-4) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Chear et al. 2022 https://doi.org/10.3390/genes13101900 (kawai2012diagnosisandtreatment pages 8-9, chear2022anovelde pages 2-4) |
| Management | Antifungal prophylaxis / treatment | Addresses frequent Candida and other fungal infections | Strongly recommended because chronic mucocutaneous candidiasis and invasive fungal disease are recurrent features; itraconazole was used in practice (kawai2012diagnosisandtreatment pages 8-9, chear2022anovelde pages 2-4) | Individual case used itraconazole prophylaxis with IVIG and co-trimoxazole (chear2022anovelde pages 2-4) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Chear et al. 2022 https://doi.org/10.3390/genes13101900 (kawai2012diagnosisandtreatment pages 8-9, chear2022anovelde pages 2-4) |
| Management | Antimycobacterial surveillance and caution with BCG exposure | Detects/prevents mycobacterial disease related to impaired CD40/IL-12/NF-κB signaling | Periodic surveillance is advised in EDA-ID because mycobacterial susceptibility is well recognized; live mycobacterial exposure warrants caution (kawai2012diagnosisandtreatment pages 8-9, kawai2012diagnosisandtreatment pages 9-10, derfalvi2020adaandpnp pages 16-17) | One non-HSCT patient in summary received anti-TB therapy plus IFN-γ and antibiotics (derfalvi2020adaandpnp pages 13-16) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172 (kawai2012diagnosisandtreatment pages 8-9, kawai2012diagnosisandtreatment pages 9-10, derfalvi2020adaandpnp pages 13-16, derfalvi2020adaandpnp pages 16-17) |
| Management | Corticosteroids for severe inflammation or colitis | Suppresses noninfectious systemic inflammation linked to NF-κB dysregulation | Used successfully for inflammatory colitis in EDA-ID and for severe systemic/CNS inflammation in NFKBIA Ser32-mutant cases (kawai2012diagnosisandtreatment pages 8-9, moriya2018ikbas32mutations pages 1-2) | In Moriya 2018, systemic corticosteroids were effective for controlling severe inflammatory symptoms (moriya2018ikbas32mutations pages 1-2) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Moriya et al. 2018 https://doi.org/10.1007/s10875-018-0522-y (kawai2012diagnosisandtreatment pages 8-9, moriya2018ikbas32mutations pages 1-2) |
| Management | Anti-TNF therapy for refractory colitis/inflammation | Targets inflammatory bowel disease–like or cytokine-driven manifestations | Has been used in EDA-ID, but reviews warn it may increase risk of mycobacterial infection; should be considered only with careful infectious risk assessment (kawai2012diagnosisandtreatment pages 9-10) | No EDID2-specific success rate provided; caution emphasized more strongly than efficacy claims (kawai2012diagnosisandtreatment pages 9-10) | Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446 (kawai2012diagnosisandtreatment pages 9-10) |
| Management / advanced therapy | Hematopoietic stem cell transplantation (HSCT) | Attempts immune reconstitution for severe combined immunodeficiency phenotype | Real-world outcomes are mixed to poor; engraftment difficulties, infectious mortality, and persistence of ectodermal features are major issues; should be considered high-risk and individualized (petersheim2018mechanismsofgenotypephenotype pages 1-6, kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 13-16) | Derfalvi summary: 11 HSCT recipients, 6 deaths post-HSCT; among 5 surviving “successful” HSCT cases, all retained ectodermal phenotype and 4 had persistent partial immunodeficiency on IVIG (derfalvi2020adaandpnp pages 13-16). Petersheim also notes poor outcomes despite chimerism (petersheim2018mechanismsofgenotypephenotype pages 1-6) | Petersheim et al. 2018 https://doi.org/10.1016/j.jaci.2017.05.030; Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446; Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172 (petersheim2018mechanismsofgenotypephenotype pages 1-6, kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 13-16) |
| Outcome / prognosis | Long-term monitoring for persistent immune deficiency and non-hematopoietic disease burden | Captures residual antibody deficiency, inflammatory disease, and persistent ectodermal manifestations | Even after transplant or stabilization, ongoing follow-up is needed for IVIG dependence, infection surveillance, GI inflammation, and supportive ectodermal care (derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 10-11) | Historical prognosis is poor in severe cases; Kawai review cites poor survival in broader EDA-ID experience, and Derfalvi data show substantial HSCT mortality (kawai2012diagnosisandtreatment pages 6-7, derfalvi2020adaandpnp pages 13-16) | Derfalvi 2020 https://doi.org/10.1007/978-1-4614-8678-7_172; Kawai et al. 2012 https://doi.org/10.2332/allergolint.12-rai-0446 (kawai2012diagnosisandtreatment pages 6-7, derfalvi2020adaandpnp pages 13-16, kawai2012diagnosisandtreatment pages 10-11) |


*Table: This table summarizes clinically relevant diagnostic tests, real-world management practices, and reported outcomes for NFKBIA-related ectodermal dysplasia and immunodeficiency 2. It is useful for translating case-report and review evidence into a practical disease knowledge base entry.*

**Key diagnostic principle (2024 development):** Fasshauer et al. emphasize that many monogenic IEIs may initially have **normal total IgG** but impaired **IgG response to polysaccharide antigens**, and that failure to measure anti-polysaccharide antibodies can delay diagnosis and allow irreversible damage such as bronchiectasis. (fasshauer2024monogenicinbornerrors pages 2-4)

### 10.2 Differential diagnosis
Important differentials include:
- **X-linked EDA-ID** due to **IKBKG/NEMO** (overlapping ectodermal phenotype and NF-κB-pathway immunodeficiency). (kawai2012diagnosisandtreatment pages 8-9)
- **Classical Hyper-IgM syndromes** (e.g., CD40L deficiency): NFKBIA patients may have hyper-IgM-like immunoglobulin patterns but can have preserved CD40/CD40L expression; genetic testing distinguishes. (chear2022anovelde pages 2-4)

---

## 11. Outcome / prognosis

Outcomes vary by variant class and severity. Available quantitative outcome data include HSCT experiences summarized in a 2020 reference source:
- In a reported series summarized by Derfalvi, **11 patients underwent HSCT and 6 died** post-HSCT (causes included sepsis and other severe complications). Among **5 surviving HSCT cases**, **all retained ectodermal phenotype** and **4 had ongoing partial immunodeficiency requiring IVIG**. (derfalvi2020adaandpnp pages 13-16)

Kawai et al. (2012) also highlight **mixed/poor HSCT outcomes** and transplant complications in the broader EDA-ID spectrum and emphasize the need for improved HSCT strategies. (kawai2012diagnosisandtreatment pages 8-9)

---

## 12. Treatment

### 12.1 Real-world management
- **Immunoglobulin replacement (IVIG/SCIG):** recommended for most/all AD EDA-ID patients due to impaired antibody responses (particularly polysaccharide responses). (kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 13-16)
- **Antimicrobial prophylaxis:** Kawai et al. strongly recommend **co-trimoxazole** and **antifungal prophylaxis** given frequent Candida and Pneumocystis infections; case-level real-world use (co-trimoxazole + itraconazole) is documented in an NFKBIA patient. (kawai2012diagnosisandtreatment pages 8-9, chear2022anovelde pages 2-4)
- **Inflammation control:** systemic **corticosteroids** can be effective for severe noninfectious inflammation (including CNS inflammation) and colitis within the broader EDA-ID spectrum. (moriya2018ikbas32mutations pages 1-2, kawai2012diagnosisandtreatment pages 8-9)
- **Anti-TNF therapy:** reported for inflammatory colitis in EDA-ID, but authors caution it may increase mycobacterial infection risk. (kawai2012diagnosisandtreatment pages 9-10)
- **HSCT:** considered in severe combined immunodeficiency phenotypes but is **high-risk** with significant mortality and frequent incomplete immune correction and persistence of ectodermal defects. (petersheim2018mechanismsofgenotypephenotype pages 1-6, derfalvi2020adaandpnp pages 13-16)

MAXO suggestions (examples):
- MAXO:0000747 “immunoglobulin replacement therapy”
- MAXO:0000775 “antibacterial prophylaxis”
- MAXO:0000776 “antifungal prophylaxis”
- MAXO:0000180 “hematopoietic stem cell transplantation”
- MAXO:0000016 “glucocorticoid therapy”

### 12.2 Clinical trials
A clinicaltrials.gov search for ectodermal dysplasia + immunodeficiency retrieved general PID observational studies/registries, but **no EDID2-specific interventional trials** were identified among the retrieved trials. (No EDID2-specific NCT IDs available in retrieved set.)

---

## 13. Prevention

Because EDID2 is a Mendelian disorder, prevention focuses on:
- **Genetic counseling** (autosomal dominant; frequently de novo but familial transmission is possible).
- **Secondary/tertiary prevention** via early immunologic recognition and infection prevention (IVIG, prophylaxis, rapid antibiotics, avoidance of high-risk live exposures such as BCG where relevant to NF-κB-pathway immunodeficiency). (kawai2012diagnosisandtreatment pages 8-9, derfalvi2020adaandpnp pages 16-17)

---

## 14. Other species / natural disease
No naturally occurring EDID2-like disease in non-human species was identified in the retrieved corpus.

---

## 15. Model organisms
A mechanistically faithful model exists:

### 15.1 Mouse knock-in model (IκBα S32I)
Mooster et al. generated a **heterozygous IκBα S32I knock-in mouse**, a mutation identified in a human ED-ID/AD EDA-ID patient. The mice exhibit:
- **Ectodermal abnormalities** (including hair/teeth and eccrine gland defects).
- Profound **secondary lymphoid organogenesis defects** (absence of lymph nodes and Peyer’s patches; disorganized spleen lacking follicles and follicular dendritic cells).
- Functional **innate cytokine response defects** to TLR ligands and impaired adhesion molecule induction.
These data support the concept that EDID2 can include both canonical NF-κB signaling failure and disruption of lymphoid organogenesis programs relevant to humoral immunity. (mooster2015defectivelymphoidorganogenesis pages 2-3, mooster2015defectivelymphoidorganogenesis pages 3-4)

---

## Key abstract quotes (supporting evidence)
- **Kawai et al. 2012 (review abstract):** “Two genes responsible for EDA-ID have been identified: … NEMO for X-linked EDA-ID … and IκBα for autosomal-dominant EDA-ID (AD-EDA-ID). Both genes are involved in NF-κB activation, such that mutations or related defects cause impaired NF-κB signaling.” (Published 2012-01; https://doi.org/10.2332/allergolint.12-rai-0446) (kawai2012diagnosisandtreatment pages 8-9)
- **Chear et al. 2022 (abstract):** “The variant analysis demonstrated a novel missense mutation in NFKBIA … The mutation occurred at the six degrons (Asp31-Ser36) in IκBα…” (Published 2022-10; https://doi.org/10.3390/genes13101900) (chear2022anovelde pages 2-4)

---

## Limitations of this report
- Orphanet/ICD/MeSH identifiers were not retrievable from the current tool context; OMIM and MONDO identifiers were captured reliably. 
- 2023–2024 primary publications specifically focused on EDID2 (NFKBIA) were sparse in the retrieved corpus; the strongest 2024 “recent development” applicable to EDID2 is improved emphasis on **anti-polysaccharide antibody testing** for monogenic IEI detection (Frontiers in Pediatrics 2024). (fasshauer2024monogenicinbornerrors pages 2-4)
- No EDID2-specific prevalence estimates or standardized QoL outcome studies were identified.


References

1. (petersheim2018mechanismsofgenotypephenotype pages 1-6): Daniel Petersheim, Michel J. Massaad, Saetbyul Lee, Alessia Scarselli, Caterina Cancrini, Kunihiko Moriya, Yoji Sasahara, Arjan C. Lankester, Morna Dorsey, Daniela Di Giovanni, Liliana Bezrodnik, Hidenori Ohnishi, Ryuta Nishikomori, Kay Tanita, Hirokazu Kanegane, Tomohiro Morio, Erwin W. Gelfand, Ashish Jain, Elizabeth Secord, Capucine Picard, Jean-Laurent Casanova, Michael H. Albert, Troy R. Torgerson, and Raif S. Geha. Mechanisms of genotype-phenotype correlation in autosomal dominant anhidrotic ectodermal dysplasia with immune deficiency. Journal of Allergy and Clinical Immunology, 141:1060-1073.e3, Mar 2018. URL: https://doi.org/10.1016/j.jaci.2017.05.030, doi:10.1016/j.jaci.2017.05.030. This article has 27 citations and is from a highest quality peer-reviewed journal.

2. (lopezgranados2008anovelmutation pages 1-2): Eduardo Lopez-Granados, Jeffrey E. Keenan, Matthew C. Kinney, Harvey Leo, Neal Jain, Chi A. Ma, Ralph Quinones, Erwin W. Gelfand, and Ashish Jain. A novel mutation in nfkbia/ikba results in a degradation‐resistant n‐truncated protein and is associated with ectodermal dysplasia with immunodeficiency. Human Mutation, 29:861-868, Jun 2008. URL: https://doi.org/10.1002/humu.20740, doi:10.1002/humu.20740. This article has 109 citations and is from a domain leading peer-reviewed journal.

3. (wen2022aheterozygousnterminal pages 1-2): Wen Wen, Li Wang, Mengyue Deng, Yue Li, Xuemei Tang, Huawei Mao, and Xiaodong Zhao. A heterozygous n-terminal truncation mutation of nfkbia results in an impaired nf-κb dependent inflammatory response. Genes &amp; Diseases, 9:176-186, Jan 2022. URL: https://doi.org/10.1016/j.gendis.2021.03.005, doi:10.1016/j.gendis.2021.03.005. This article has 7 citations.

4. (schimke2013anovelgainoffunction pages 1-2): Lena F. Schimke, Nikolaus Rieber, Stacey Rylaarsdam, Otávio Cabral-Marques, Nicholas Hubbard, Anne Puel, Laura Kallmann, Stephanie Anover Sombke, Gundula Notheis, Hans-Peter Schwarz, Birgit Kammer, Tomas Hökfelt, Reinald Repp, Capucine Picard, Jean-Laurent Casanova, Bernd H. Belohradsky, Michael H. Albert, Hans D. Ochs, Ellen D. Renner, and Troy R. Torgerson. A novel gain-of-function ikba mutation underlies ectodermal dysplasia with immunodeficiency and polyendocrinopathy. Journal of Clinical Immunology, 33:1088-1099, May 2013. URL: https://doi.org/10.1007/s10875-013-9906-1, doi:10.1007/s10875-013-9906-1. This article has 72 citations and is from a domain leading peer-reviewed journal.

5. (kawai2012diagnosisandtreatment pages 8-9): Tomoki Kawai, Ryuta Nishikomori, and Toshio Heike. Diagnosis and treatment in anhidrotic ectodermal dysplasia with immunodeficiency. Allergology international : official journal of the Japanese Society of Allergology, 61 2:207-17, Jan 2012. URL: https://doi.org/10.2332/allergolint.12-rai-0446, doi:10.2332/allergolint.12-rai-0446. This article has 82 citations.

6. (derfalvi2020adaandpnp pages 13-16): Beata Derfalvi. Ada and pnp deficiency. Encyclopedia of Medical Immunology, pages 4-9, Jan 2020. URL: https://doi.org/10.1007/978-1-4614-8678-7\_172, doi:10.1007/978-1-4614-8678-7\_172. This article has 0 citations.

7. (fasshauer2024monogenicinbornerrors pages 2-4): Maria Fasshauer, Sarah Dinges, Olga Staudacher, Mirjam Völler, Anna Stittrich, Horst von Bernuth, Volker Wahn, and Renate Krüger. Monogenic inborn errors of immunity with impaired igg response to polysaccharide antigens but normal igg levels and normal igg response to protein antigens. Frontiers in Pediatrics, Jun 2024. URL: https://doi.org/10.3389/fped.2024.1386959, doi:10.3389/fped.2024.1386959. This article has 3 citations.

8. (chear2022anovelde pages 1-2): Chai Teng Chear, Bader Abdul Kader El Farran, Marina Sham, Kavetha Ramalingam, Lokman Mohd Noh, Intan Hakimah Ismail, Mei Yee Chiow, Mohd Farid Baharin, Adiratna Mat Ripen, and Saharuddin Bin Mohamad. A novel de novo nfkbia missense mutation associated to ectodermal dysplasia with dysgammaglobulinemia. Genes, 13:1900, Oct 2022. URL: https://doi.org/10.3390/genes13101900, doi:10.3390/genes13101900. This article has 8 citations.

9. (chear2022anovelde pages 2-4): Chai Teng Chear, Bader Abdul Kader El Farran, Marina Sham, Kavetha Ramalingam, Lokman Mohd Noh, Intan Hakimah Ismail, Mei Yee Chiow, Mohd Farid Baharin, Adiratna Mat Ripen, and Saharuddin Bin Mohamad. A novel de novo nfkbia missense mutation associated to ectodermal dysplasia with dysgammaglobulinemia. Genes, 13:1900, Oct 2022. URL: https://doi.org/10.3390/genes13101900, doi:10.3390/genes13101900. This article has 8 citations.

10. (moriya2018ikbas32mutations pages 1-2): Kunihiko Moriya, Yoji Sasahara, Hidenori Ohnishi, Tomoki Kawai, and Hirokazu Kanegane. Ikba s32 mutations underlie ectodermal dysplasia with immunodeficiency and severe noninfectious systemic inflammation. Journal of Clinical Immunology, 38:543-545, Jun 2018. URL: https://doi.org/10.1007/s10875-018-0522-y, doi:10.1007/s10875-018-0522-y. This article has 14 citations and is from a domain leading peer-reviewed journal.

11. (giancane2013anhidroticectodermaldysplasia pages 3-3): Gabriella Giancane, Simona Ferrari, Rita Carsetti, Paola Papoff, Metello Iacobini, and Marzia Duse. Anhidrotic ectodermal dysplasia: a new mutation. The Journal of allergy and clinical immunology, 132 6:1451-3, Dec 2013. URL: https://doi.org/10.1016/j.jaci.2013.05.034, doi:10.1016/j.jaci.2013.05.034. This article has 17 citations.

12. (kawai2012diagnosisandtreatment pages 6-7): Tomoki Kawai, Ryuta Nishikomori, and Toshio Heike. Diagnosis and treatment in anhidrotic ectodermal dysplasia with immunodeficiency. Allergology international : official journal of the Japanese Society of Allergology, 61 2:207-17, Jan 2012. URL: https://doi.org/10.2332/allergolint.12-rai-0446, doi:10.2332/allergolint.12-rai-0446. This article has 82 citations.

13. (kawai2012diagnosisandtreatment pages 7-8): Tomoki Kawai, Ryuta Nishikomori, and Toshio Heike. Diagnosis and treatment in anhidrotic ectodermal dysplasia with immunodeficiency. Allergology international : official journal of the Japanese Society of Allergology, 61 2:207-17, Jan 2012. URL: https://doi.org/10.2332/allergolint.12-rai-0446, doi:10.2332/allergolint.12-rai-0446. This article has 82 citations.

14. (kawai2012diagnosisandtreatment pages 9-10): Tomoki Kawai, Ryuta Nishikomori, and Toshio Heike. Diagnosis and treatment in anhidrotic ectodermal dysplasia with immunodeficiency. Allergology international : official journal of the Japanese Society of Allergology, 61 2:207-17, Jan 2012. URL: https://doi.org/10.2332/allergolint.12-rai-0446, doi:10.2332/allergolint.12-rai-0446. This article has 82 citations.

15. (derfalvi2020adaandpnp pages 16-17): Beata Derfalvi. Ada and pnp deficiency. Encyclopedia of Medical Immunology, pages 4-9, Jan 2020. URL: https://doi.org/10.1007/978-1-4614-8678-7\_172, doi:10.1007/978-1-4614-8678-7\_172. This article has 0 citations.

16. (kawai2012diagnosisandtreatment pages 10-11): Tomoki Kawai, Ryuta Nishikomori, and Toshio Heike. Diagnosis and treatment in anhidrotic ectodermal dysplasia with immunodeficiency. Allergology international : official journal of the Japanese Society of Allergology, 61 2:207-17, Jan 2012. URL: https://doi.org/10.2332/allergolint.12-rai-0446, doi:10.2332/allergolint.12-rai-0446. This article has 82 citations.

17. (mooster2015defectivelymphoidorganogenesis pages 2-3): Jana L. Mooster, Severine Le Bras, Michel J. Massaad, Haifa Jabara, Juhan Yoon, Claire Galand, Balthasar A. Heesters, Oliver T. Burton, Hamid Mattoo, John Manis, and Raif S. Geha. Defective lymphoid organogenesis underlies the immune deficiency caused by a heterozygous s32i mutation in iκbα. The Journal of Experimental Medicine, 212:185-202, Feb 2015. URL: https://doi.org/10.1084/jem.20140979, doi:10.1084/jem.20140979. This article has 36 citations.

18. (mooster2015defectivelymphoidorganogenesis pages 3-4): Jana L. Mooster, Severine Le Bras, Michel J. Massaad, Haifa Jabara, Juhan Yoon, Claire Galand, Balthasar A. Heesters, Oliver T. Burton, Hamid Mattoo, John Manis, and Raif S. Geha. Defective lymphoid organogenesis underlies the immune deficiency caused by a heterozygous s32i mutation in iκbα. The Journal of Experimental Medicine, 212:185-202, Feb 2015. URL: https://doi.org/10.1084/jem.20140979, doi:10.1084/jem.20140979. This article has 36 citations.