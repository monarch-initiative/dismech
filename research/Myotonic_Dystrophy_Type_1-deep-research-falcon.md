---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:29.288190'
end_time: '2026-04-25T22:26:41.275526'
duration_seconds: 671.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myotonic Dystrophy Type 1
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
- **Disease Name:** Myotonic Dystrophy Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myotonic Dystrophy Type 1** covering all of the
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
- **Disease Name:** Myotonic Dystrophy Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Myotonic Dystrophy Type 1** covering all of the
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


# Myotonic Dystrophy Type 1 (DM1) — Disease Characteristics Research Report

**Target disease:** Myotonic dystrophy type 1 (DM1)  
**Category:** Mendelian (repeat-expansion disorder)  
**MONDO:** **MONDO_0008056** (via Open Targets disease mapping) (berengercurrias2023pluripotentstemcells pages 1-2)

## 1. Disease Information

### 1.1 Concise overview
Myotonic dystrophy type 1 (DM1) is a progressive, multisystemic neuromuscular disorder characterized by myotonia and progressive muscle weakness, with frequent involvement of the heart (conduction disease/arrhythmias), eyes (cataracts), endocrine/metabolic systems (e.g., insulin resistance/diabetes), gastrointestinal function, and the central nervous system. DM1 is caused by an unstable CTG repeat expansion in the **3′ untranslated region (3′UTR) of the DMPK gene**, and disease pathogenesis is largely driven by toxic expanded-repeat RNA that perturbs RNA-binding proteins and alternative splicing (“spliceopathy”). (hale2023dynamicsandvariability pages 1-2, almeida2023promisingaav.u7snrnasvectors pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 1-2)

**Direct abstract quote (mechanism + overview):** A 2023 Frontiers paper states: “DM1 is caused by a **CTG repeat expansion in the 3′UTR region of the DMPK gene that sequesters muscleblind-like proteins, blocking their splicing activity and forming nuclear RNA foci. Consequently, many genes have their splicing reversed to a fetal pattern**.” (Almeida et al., 2023-06, https://doi.org/10.3389/fcell.2023.1181040) (almeida2023promisingaav.u7snrnasvectors pages 1-2)

### 1.2 Key identifiers (and common names)
| Disease name | Synonyms | MONDO ID | OMIM | Orphanet | MeSH | ICD-10/ICD-11 | Notes |
|---|---|---|---|---|---|---|---|
| Myotonic Dystrophy Type 1 (DM1) | Steinert disease; Steinert’s myotonic dystrophy; myotonic dystrophy type I; MDI | MONDO_0008056 | 160900 | 273 | D009223 | Not available from the provided evidence | OMIM #160900 explicitly reported in peer-reviewed DM1 sources; Steinert/MDI naming used in epidemiology and review papers; MeSH D009223 reported in a DM1 registry record; Open Targets reports MONDO_0008056 and Orphanet_273 for DM1. URLs: https://doi.org/10.3389/fneur.2024.1493570 ; https://doi.org/10.1186/s13023-024-03114-z ; https://doi.org/10.1186/s13023-024-03114-z ; https://doi.org/10.3390/healthcare12080838 (abati2024cardiacriskand pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2, hernaez2024prevalenceofsteinert’s pages 1-2, NCT06979024 chunk 1) |


*Table: This table summarizes the core identifiers and common alternative names for Myotonic Dystrophy Type 1. It is useful for harmonizing disease records across ontology, registry, and literature sources while noting that ICD codes were not established from the provided evidence.*

Additional identifier evidence from recent literature:
- **OMIM:** DM1 = **#160900** (reported explicitly in multiple 2023–2024 sources) (abati2024cardiacriskand pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2)
- **Orphanet concept:** “Steinert myotonic dystrophy” (Open Targets reports Orphanet_273 mapping) (berengercurrias2023pluripotentstemcells pages 1-2)

**ICD-10/ICD-11:** Not established from the provided evidence; would require an ICD browser or coding guidance not retrieved in this tool run.

### 1.3 Synonyms and alternative names
Commonly used synonyms in recent sources include:
- **Steinert disease / Steinert’s myotonic dystrophy** (hernaez2024prevalenceofsteinert’s pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2)
- **Myotonic dystrophy type I / MDI** (hernaez2024prevalenceofsteinert’s pages 1-2)

### 1.4 Evidence sources: individual vs aggregated
DM1 knowledge in this report is derived from:
- **Aggregated disease-level resources/registries:** Madrid rare disease registry (SIERMA) used for population estimates (2010–2017) (hernaez2024prevalenceofsteinert’s pages 1-2); China DM1 patient registry (ClinicalTrials.gov observational cohort) (NCT06979024 chunk 1)
- **Cohort-based clinical genetics studies:** multicenter Chinese cohort (n=211) (zhong2024clinicalfeaturesand pages 1-2)
- **Mechanistic disease modeling studies:** patient-derived myoblasts, iPSC/hPSC models, and mouse models (almeida2023promisingaav.u7snrnasvectors pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 8-9)

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline **CTG trinucleotide repeat expansion** in the **DMPK** gene 3′UTR (autosomal dominant). (hale2023dynamicsandvariability pages 1-2, almeida2023promisingaav.u7snrnasvectors pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 1-2)

**Repeat-size categories (clinical correlation; indicative, not absolute):**
- Healthy alleles: ~5–37 CTGs (almeida2023promisingaav.u7snrnasvectors pages 1-2, stoodley2023applicationofantisense pages 1-2)
- Premutation: ~38–49 CTGs (almeida2023promisingaav.u7snrnasvectors pages 1-2)
- Symptomatic: typically **>50 CTGs**, with larger expansions associated with earlier onset and more severe phenotypes, including congenital forms that can exceed 1,000 CTGs. (almeida2023promisingaav.u7snrnasvectors pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 1-2)

### 2.2 Risk factors
**Genetic risk factors**
- **Repeat length and instability:** CTG repeat length correlates with phenotype severity and age of onset, complicated by **somatic instability** (repeat length varies by tissue/age). (stoodley2023applicationofantisense pages 1-2, ionova2024thestudyof pages 1-2)
- **Anticipation:** Intergenerational repeat expansion contributes to earlier onset and increased severity in successive generations, with congenital disease often associated with large maternal expansions. (hale2023dynamicsandvariability pages 1-2, ionova2024thestudyof pages 1-2)

**Non-genetic modifiers and clinical risk factors**
- Cardiopulmonary complications are major determinants of morbidity/mortality; surveillance and early interventions are emphasized in care recommendations and clinical management sources. (ricci2024assessmentofthe pages 17-20, abati2024cardiacriskand pages 1-2)

### 2.3 Protective factors / modifier factors
Protective “factors” in DM1 primarily refer to **genetic modifiers** that mitigate repeat instability or molecular toxicity.

- **Interrupted/variant repeat tracts** and epigenetic context: A Mexican reference cohort reported **interrupted CTG repeat tracts** in **2.8%** of carriers and associated these interruptions with milder phenotypes and reduced instability (cohort details in excerpt). (cerecedozapata2025fifteenyearsof pages 15-16)
- **Epigenetic variability (methylation) at the DM1 locus:** DMPK expanded alleles are flanked by CpG islands; variant repeats may influence methylation patterns and phenotypic variability (summarized in recent molecular work). (ionova2024thestudyof pages 1-2)

### 2.4 Gene–environment interactions
No robust, specific gene–environment interaction mechanisms were directly established from the retrieved evidence. However, dietary context can exacerbate metabolic pathology in model systems (see Mechanisms/Pathophysiology). (stoodley2023applicationofantisense pages 1-2)

## 3. Phenotypes

### 3.1 Core phenotype spectrum (multisystem)
**Adult/classical DM1** commonly includes:
- Myotonia and progressive distal muscle weakness (hale2023dynamicsandvariability pages 1-2, stoodley2023applicationofantisense pages 1-2)
- Cardiac conduction defects/arrhythmias (hale2023dynamicsandvariability pages 1-2, abati2024cardiacriskand pages 1-2)
- Early cataracts (hale2023dynamicsandvariability pages 1-2)
- CNS impairment (cognitive/behavioral) (hale2023dynamicsandvariability pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2)

**Congenital DM1 (CDM)** can present at birth with:
- Neonatal hypotonia, respiratory failure, feeding difficulty, and congenital features (e.g., clubfoot), with motor improvement in early childhood reported in natural history. (hale2023dynamicsandvariability pages 1-2)

### 3.2 Quantitative phenotype frequencies and statistics (prioritize 2024)

**Large multicenter Chinese Han DM1 cohort (genetically confirmed n=211; detailed phenotyping n=64; enrollment 2020–2023)** reported: (Zhong et al., 2024-03, Orphanet J Rare Dis, https://doi.org/10.1186/s13023-024-03114-z)
- In the detailed cohort, **muscle weakness 92.2%**, **myotonia 85.9%**, **fatigue 73.4%** (zhong2024clinicalfeaturesand pages 1-2)
- **Daytime sleepiness 70.3%**; **dysphagia 43.8%**; **cognitive impairment 25%**; **intermittent insomnia 28.1%**; **dyspnea 23.4%**; **diabetes 17.2%**; **tumors 4.7%** (zhong2024clinicalfeaturesand pages 1-2)
- Supportive interventions/markers: **cataract surgery 14.1%**, **wheelchair use 7.8%**, **ventilatory support 4.7%**, **gastric tube 1.6%** (zhong2024clinicalfeaturesand pages 1-2)
- Mean **ESS 10.50 (SD 6.18)** and mean **FSS 42.02 (SD 15.01)** (zhong2024clinicalfeaturesand pages 5-7)

A cropped table of the Zhong et al. cohort summarizing frequencies across CTG strata was retrieved (Table 1) (zhong2024clinicalfeaturesand media 408fef39).

**Pediatric (congenital/childhood onset) sleep/behavior cohort (Italy; n=46)** reported:
- Daytime sleepiness/disrupted sleep in **30%** of children (CDM and ChDM), with associations to autism traits, executive function, and disease burden measures. (Trucco et al., 2024-09, https://doi.org/10.3390/jcm13185459) (hernaez2024prevalenceofsteinert’s pages 1-2)

### 3.3 Quality-of-life and functional impact
DM1 is associated with reduced physical activity and aerobic capacity, contributing to adverse body composition.

A prospective case-control study (n=15 DM1 vs 15 matched controls) found:
- **Total energy expenditure 23% lower** in DM1; **steps/day 63% lower** (median 3090 vs 8283 steps/24 h); and reduced **VO2peak** (22 vs 33 mL/min/kg). (Joosten et al., 2023-05, J Neuromuscul Dis, https://doi.org/10.3233/JND-230036) (hernaez2024prevalenceofsteinert’s pages 1-2)

### 3.4 Suggested HPO terms (examples; non-exhaustive)
- Myotonia → **HP:0002486**
- Distal muscle weakness → **HP:0002460** (distal muscle weakness)
- Progressive muscle wasting → **HP:0003202**
- Cardiac conduction defect → **HP:0001678**
- Cardiac arrhythmia → **HP:0011675**
- Cataract → **HP:0000518**
- Dysphagia → **HP:0002015**
- Excessive daytime sleepiness → **HP:0002329**
- Respiratory insufficiency/failure (congenital) → **HP:0002093/HP:0002878**
- Cognitive impairment → **HP:0100543**

(These HPO IDs are standard ontology mappings; specific HPO IDs were not enumerated in the retrieved papers and should be validated against the HPO browser when integrating into a KB.)

## 4. Genetic/Molecular Information

### 4.1 Causal gene
- **DMPK** (DM1 protein kinase); pathogenic mechanism triggered by expanded repeat in **3′UTR**. (almeida2023promisingaav.u7snrnasvectors pages 1-2, stoodley2023applicationofantisense pages 1-2)

Open Targets disease-target associations identify **DMPK** as the top associated target and report DM1 locus antisense RNA (DM1-AS) as another association in the locus context (mapping evidence). (berengercurrias2023pluripotentstemcells pages 1-2)

### 4.2 Pathogenic variant class
- **Repeat expansion**: CTG expansion in the DMPK 3′UTR (structural/repeat-expansion class; germline). (hale2023dynamicsandvariability pages 1-2, stoodley2023applicationofantisense pages 1-2)

**Somatic mosaicism/instability:** A major complexity in DM1 is that repeat lengths expand over time and differ by tissue (somatic instability), complicating genotype–phenotype correlations. (ionova2024thestudyof pages 1-2)

### 4.3 Modifier genes and molecular modifiers
- **MBNL family** sequestration is primary; additional regulators include **CELF1** upregulation/hyperphosphorylation as part of spliceopathy amplification. (berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 1-2)
- **Core spliceosomal proteins** as modifiers: A 2024 Human Molecular Genetics study identified core spliceosomal proteins (e.g., SNRPD2) as modifiers capable of reducing DMPK expression and partially rescuing mis-splicing in cellular models (modifier class concept). (stoodley2023applicationofantisense pages 1-2)

### 4.4 Epigenetics
Epigenetic variability at CpG islands flanking the expansion has been implicated as a contributor to phenotypic variability, particularly in the context of variant repeat interruptions and parental origin effects. (ionova2024thestudyof pages 1-2)

## 5. Environmental Information

No infectious etiologies apply.

Environmental/lifestyle factors are not causal, but lifestyle may influence secondary metabolic phenotypes. For example, a liver-specific DM1 mouse model showed that high-fat/high-sugar diets exacerbate lipid accumulation and susceptibility to MAFLD-like phenotypes in the context of CUGexp RNA toxicity. (Dewald et al., 2024-10, Nat Commun, https://doi.org/10.1038/s41467-024-53378-z) (stoodley2023applicationofantisense pages 1-2)

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (key concepts and definitions)
**RNA toxicity / RNA gain-of-function model:** The expanded DMPK allele is transcribed, producing expanded CUG repeat RNA that forms nuclear foci and **sequesters MBNL proteins**, leading to depletion of functional MBNL in the nucleoplasm and widespread defects in alternative splicing. (hale2023dynamicsandvariability pages 1-2, almeida2023promisingaav.u7snrnasvectors pages 1-2, stoodley2023applicationofantisense pages 1-2)

**CELF1 dysregulation:** Stress signaling pathways can increase CELF1 activity, and an **MBNL/CELF1 imbalance** drives persistent fetal splicing patterns across hundreds of transcripts. (berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 1-2)

**Direct abstract quote (pathogenic chain):** “DM1 is caused by a CTG repeat expansion in the 3′UTR region of the DMPK gene that sequesters muscleblind-like proteins… forming nuclear RNA foci… [and] splicing [is] reversed to a fetal pattern.” (Almeida et al., 2023-06, https://doi.org/10.3389/fcell.2023.1181040) (almeida2023promisingaav.u7snrnasvectors pages 1-2)

### 6.2 Downstream pathways and tissue-specific consequences
**Spliceopathy targets with clinical relevance:** Mis-spliced transcripts include **CLCN1** (myotonia), **SCN5A** (cardiac conduction), **BIN1**, and **INSR** (metabolic phenotype), among others. (hale2023dynamicsandvariability pages 1-2, stoodley2023applicationofantisense pages 1-2)

**Developmental dynamics (congenital DM1):** RNA-seq of congenital DM1 skeletal muscle across pediatric development showed an MBNL-dependent mis-splicing signature with a triphasic pattern: severe mis-splicing in infancy, improvement in early childhood, and variability in adolescence. (Hale et al., 2023-10, https://doi.org/10.1093/hmg/ddac254) (hale2023dynamicsandvariability pages 1-2)

### 6.3 Suggested GO biological processes (examples)
- Alternative mRNA splicing via spliceosome → **GO:0000380**
- mRNA processing → **GO:0006397**
- Regulation of RNA splicing → **GO:0043484**
- Muscle contraction (downstream functional impairment) → **GO:0006936**

### 6.4 Suggested CL cell types (examples)
- Skeletal muscle myoblast / myotube → **CL:0000056** (myoblast; verify exact CL term usage)
- Cardiomyocyte → **CL:0000746**
- Motor neuron (CNS involvement) → **CL:0000100**

(As with HPO, CL/GO IDs should be validated in ontology browsers; the mechanistic linkage is supported by DM1 literature cited above.)

## 7. Anatomical Structures Affected

**Primary/commonly affected systems:**
- Skeletal muscle (UBERON:0001134) (almeida2023promisingaav.u7snrnasvectors pages 1-2, stoodley2023applicationofantisense pages 1-2)
- Heart (UBERON:0000948) including conduction system (abati2024cardiacriskand pages 1-2)
- Brain/CNS (UBERON:0000955) (hale2023dynamicsandvariability pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2)
- Eye lens (UBERON:0000962) — cataracts (hale2023dynamicsandvariability pages 1-2)
- Respiratory system (UBERON:0001004) — respiratory insufficiency/failure (hale2023dynamicsandvariability pages 1-2, ricci2024assessmentofthe pages 17-20)

**Subcellular localization (core lesion):** nuclear RNA foci (nucleus; GO CC:0005634) and RNA-binding protein sequestration. (almeida2023promisingaav.u7snrnasvectors pages 1-2, stoodley2023applicationofantisense pages 1-2)

## 8. Temporal Development

### 8.1 Onset
DM1 spans congenital, childhood/juvenile, and adult-onset forms; congenital DM1 can present at birth and is often linked to large intergenerational expansions. (hale2023dynamicsandvariability pages 1-2, ionova2024thestudyof pages 1-2)

In congenital DM1, hallmark adult features can be absent early, and early-life symptoms include neonatal hypotonia and respiratory failure. (hale2023dynamicsandvariability pages 1-2)

### 8.2 Progression
DM1 is typically progressive across neuromuscular and systemic domains. The congenital DM1 transcriptome/spliceopathy can show dynamic changes across pediatric development, suggesting time windows for intervention/biomarkers. (hale2023dynamicsandvariability pages 1-2)

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal dominant** inheritance with **anticipation** (intergenerational repeat expansion and earlier onset). (hale2023dynamicsandvariability pages 1-2, ionova2024thestudyof pages 1-2)
- Maternal transmission enrichment and maternal expansions are often linked to congenital forms. (hale2023dynamicsandvariability pages 1-2, ionova2024thestudyof pages 1-2)

### 9.2 Epidemiology (recent data)
Recent studies show considerable geographic variation:
- Global/Europe estimates: ~**1 in 8,000** cited in mechanistic and clinical sources (almeida2023promisingaav.u7snrnasvectors pages 1-2, abati2024cardiacriskand pages 1-2)
- **Community of Madrid (Spain)** population registry: **14.4 per 100,000** (2010–2017; n=1101; mean age 47.8; 49.1% women). (Hernáez et al., 2024-04, https://doi.org/10.3390/healthcare12080838) (hernaez2024prevalenceofsteinert’s pages 1-2)
- **North Ossetia-Alania families study**: prevalence **14.17 per 100,000 (Ossetians)** and **18.74 per 100,000 (Ingush)**; anticipation and correlation of CTG length with onset/severity; higher maternal transmission frequency. (Ionova et al., 2024-09, https://doi.org/10.3390/ijms25179734) (ionova2024thestudyof pages 1-2)
- **Chinese multicenter cohort**: minimal prevalence estimate **0.13/100,000** in the authors’ ascertainment context; cohort suggests possible underdiagnosis or population differences. (zhong2024clinicalfeaturesand pages 2-5)

## 10. Diagnostics

### 10.1 Clinical and electrophysiologic testing
- EMG can show myotonic discharges; in a Chinese cohort, EMG abnormalities were reported in **92.2%** (195/211). (zhong2024clinicalfeaturesand pages 2-5)

### 10.2 Genetic testing (repeat expansion testing)
**Core diagnostic test:** detection of CTG repeat expansion at the **DMPK** locus.

- Zhong et al. used **TP-PCR and flanking PCR** to size peak CTG repeats (range 92–1945) and diagnose DM1. (zhong2024clinicalfeaturesand pages 2-5)
- Registry study notes genotyping can use **triplet-primed PCR or long-read sequencing**, with DM1 confirmation as CTG repeats **>50**. (NCT06979024 chunk 1)

**Emerging diagnostics (long-read):** Repeat expansion disorders increasingly use long-read sequencing for repeat length, composition, mosaicism, and methylation assessment; the DM1 testing landscape is moving in that direction (general diagnostic perspective; not DM1-only). (berengercurrias2023pluripotentstemcells pages 1-2)

### 10.3 Imaging and biomarkers
**Cardiac imaging biomarker candidate:** In a small retrospective cohort, DM1 patients had higher cardiac extracellular volume (ECV) on CMR (a fibrosis-associated metric), suggesting CMR ECV as a marker of subclinical cardiac involvement. (Abati et al., 2024-11, https://doi.org/10.3389/fneur.2024.1493570) (abati2024cardiacriskand pages 1-2)

### 10.4 Differential diagnosis
Not enumerated in the retrieved evidence; clinically, DM2 (CNBP CCTG expansion) is a principal genetic differential (noted in review/imaging context). (abati2024cardiacriskand pages 1-2)

## 11. Outcome / Prognosis

**Major causes of morbidity/mortality:** cardiopulmonary complications.
- Cardiac dysrhythmias and conduction disease are prominent; one recent review-style paper notes dysrhythmias can be implicated in a large fraction of patients and are a leading cause of mortality, second to respiratory failure. (abati2024cardiacriskand pages 1-2, ricci2024assessmentofthe pages 17-20)

A recent synthesis cites median survival around **59–60 years**, with respiratory failure and adverse cardiac events as leading causes of death. (misquitta2024investigatingthetherapeutic pages 9-13)

## 12. Treatment

### 12.1 Current real-world management (symptomatic/supportive)
DM1 management is multidisciplinary and largely symptomatic.

**Cardiac surveillance/intervention:** surveillance is emphasized; device therapy (pacemaker/ICD) may be indicated for conduction disease and tachyarrhythmias. (ricci2024assessmentofthe pages 17-20)

**Respiratory support:** non-invasive ventilation (BiPAP/CPAP), respiratory physiotherapy, and supportive interventions can improve quality of life and survival in respiratory involvement. (ricci2024assessmentofthe pages 17-20)

**Myotonia pharmacotherapy:** mexiletine is a commonly used antimyotonia therapy; symptomatic agents require ECG assessment due to cardiac risk considerations. A care/outcome measures source reports “Class 1 evidence” supporting mexiletine **150–200 mg three times daily** for myotonia. (ricci2024assessmentofthe pages 17-20)

**Sleepiness:** modafinil or methylphenidate may be used for disabling daytime sleepiness (symptomatic). (ricci2024assessmentofthe pages 17-20)

**MAXO term suggestions (examples):**
- Antiarrhythmic drug therapy (mexiletine) → MAXO:0000105 (drug therapy; confirm specific MAXO term)
- Cardiac pacemaker implantation → MAXO:0000621 (device implantation; verify)
- Noninvasive ventilation → MAXO:0000504 (ventilatory support; verify)
- Physical therapy/rehabilitation → MAXO:0000019 (rehabilitation; verify)

(Exact MAXO IDs should be verified; MAXO mappings were not provided in the retrieved documents.)

### 12.2 Recent developments and latest research (2023–2024 priority)

#### 12.2.1 RNA-/gene-targeting approaches (preclinical/translation)
**AAV-delivered antisense (U7snRNA) targeting DMPK/CTG tracts:** Patient-derived myoblasts treated with AAV8.U7snRNA antisense constructs showed reduced RNA foci, MBNL relocalization, and broad splicing correction (RNA-seq), supporting long-lasting delivery strategies beyond systemic ASOs. (Almeida et al., 2023-06, https://doi.org/10.3389/fcell.2023.1181040) (almeida2023promisingaav.u7snrnasvectors pages 1-2)

**Antisense conjugates review (delivery focus):** Research is focusing on improving ASO biodistribution using lipid/cell-penetrating peptide/antibody conjugation to improve muscle (including cardiac) delivery; CNS delivery remains challenging. (Stoodley et al., 2023-01, https://doi.org/10.3390/ijms24032697) (stoodley2023applicationofantisense pages 1-2, stoodley2023applicationofantisense pages 8-9)

**AntimiR strategy (MBNL1 derepression):** A 2024 Science Advances study in primary DM1 myoblasts reports that antimiRs targeting miR-23b and miR-218 can boost MBNL1 and improve RNA toxicity readouts and myoblast phenotypes; the abstract notes a leading antimiR reversed **68%** of dysregulated genes and also reduced DMPK transcripts and ribonuclear foci. (Cerro-Herreros et al., 2024-10, https://doi.org/10.1126/sciadv.adn6525) (stoodley2023applicationofantisense pages 1-2)

#### 12.2.2 Clinical trials (registry evidence; 2023–2024 status emphasis)

**Avidity Biosciences (AOC 1001 / del-desiran) programs**
- AOC 1001 study in adult DM1: **NCT05027269**, Phase 1/2, **COMPLETED**, enrollment 39. (ClinicalTrials.gov) (NCT02858908 chunk 1)
- Open-label extension: **NCT05479981**, Phase 2, **COMPLETED**, enrollment 37. (ClinicalTrials.gov) (NCT02858908 chunk 1)
- Global Phase 3 study del-desiran: **NCT06411288**, Phase 3, **ACTIVE_NOT_RECRUITING**, enrollment 159. (ClinicalTrials.gov) (NCT02858908 chunk 1)
- Global Phase 3 open-label extension: **NCT07008469**, Phase 3, **ENROLLING_BY_INVITATION**, enrollment 230. (ClinicalTrials.gov) (NCT02858908 chunk 1)

**Gene therapy trial**
- Sanofi AAV gene therapy: **SAR446268**, **NCT06844214**, Phase 1/2, **RECRUITING**, enrollment 32. (ClinicalTrials.gov) (NCT02858908 chunk 1)

**Small-molecule/repurposed therapy trials (examples)**
- Tideglusib trial: **NCT02858908**, Phase 2, **COMPLETED**, enrollment 16; endpoints include safety and multiple functional measures; results posted in 2025 per registry metadata. (ClinicalTrials.gov) (NCT02858908 chunk 1)
- Mexiletine (once-daily PR) trial: **NCT06523400**, Phase 3, **RECRUITING**, enrollment 176. (ClinicalTrials.gov) (NCT02858908 chunk 1)

**Important limitation:** Quantitative efficacy results for AOC 1001/del-desiran, VX-670, SAR446268, and mexiletine PR were not available in the retrieved evidence snippets (trial registry metadata were retrieved; full results would require additional extraction). (NCT02858908 chunk 1)

## 13. Prevention

### 13.1 Primary prevention
No primary prevention exists for a germline Mendelian repeat-expansion disorder other than reproductive options.

### 13.2 Secondary prevention (early detection)
- **Cascade testing** in families and early molecular confirmation are core strategies due to anticipation and variable onset. (ionova2024thestudyof pages 1-2)

### 13.3 Tertiary prevention (complication prevention)
- Routine **cardiac surveillance** and proactive management of conduction disease to reduce sudden death risk. (ricci2024assessmentofthe pages 17-20, abati2024cardiacriskand pages 1-2)
- Proactive **respiratory monitoring** and ventilation support where indicated. (ricci2024assessmentofthe pages 17-20)

### 13.4 Genetic counseling and reproductive options
A Mexican national reference cohort described implementation of clinical and molecular evaluation including **predictive testing, prenatal diagnosis, and preimplantation genetic diagnosis**, but with limited uptake due to legal, cultural, and cost barriers. (cerecedozapata2025fifteenyearsof pages 15-16)

## 14. Other Species / Natural Disease

No naturally occurring DM1 in non-human species was established from the retrieved evidence (e.g., OMIA/veterinary sources were not retrieved in this run). This section is therefore **not available from current evidence**.

## 15. Model Organisms

### 15.1 Cellular and stem cell models
Human pluripotent stem cell (hPSC/iPSC) models are used for disease mechanism decoding and drug discovery, motivated by DM1 multisystem involvement beyond skeletal muscle. (Bérenger-Currias et al., 2023-02, https://doi.org/10.3390/cells12040571) (berengercurrias2023pluripotentstemcells pages 1-2)

### 15.2 Mouse models
- DMSXL and related models carrying human DMPK with large CTG expansions (>1,000) have been used to study CNS delivery strategies (mentioned in antisense conjugate review context). (stoodley2023applicationofantisense pages 8-9)
- Tissue-targeted models (e.g., liver-specific expression of CUGexp RNA) reproduce metabolic and drug-metabolism phenotypes and link CUGexp RNA toxicity to hepatic dysfunction. (Dewald et al., 2024-10, https://doi.org/10.1038/s41467-024-53378-z) (stoodley2023applicationofantisense pages 1-2)

---

## Expert synthesis / analysis (authoritative interpretation)

1. **Mechanism-guided therapeutic logic:** The convergence of evidence across cohorts and models supports DM1 as an RNA-mediated spliceopathy. This coherently explains multisystem involvement, since DMPK is broadly expressed and MBNL/CELF-driven splicing programs are fundamental in multiple tissues. (almeida2023promisingaav.u7snrnasvectors pages 1-2, berengercurrias2023pluripotentstemcells pages 1-2, stoodley2023applicationofantisense pages 1-2)
2. **Why delivery dominates translational risk:** ASOs can correct foci/splicing in models but face systemic delivery limitations in human muscle; the 2023–2024 literature emphasizes conjugation, viral delivery, and alternative nucleic-acid modalities to overcome biodistribution barriers. (almeida2023promisingaav.u7snrnasvectors pages 1-2, stoodley2023applicationofantisense pages 1-2, stoodley2023applicationofantisense pages 8-9)
3. **Clinical heterogeneity is biologically grounded:** Anticipation, tissue mosaicism, and repeat interruptions/methylation provide plausible explanations for substantial inter-individual variability and complicate prognosis based on blood repeat length alone. (ionova2024thestudyof pages 1-2)

---

## Key gaps (not resolved in retrieved evidence)
- **ICD-10/ICD-11 codes** and a definitive MeSH term specific to “DM1” (beyond MeSH Myotonic Dystrophy D009223) were not retrieved. (NCT06979024 chunk 1)
- **Outcome results** for several major contemporary trials (AOC 1001/del-desiran Phase 3; VX-670; SAR446268) were not available in the evidence snippets. (NCT02858908 chunk 1)
- **Cross-species natural disease** evidence (OMIA) and comprehensive differential diagnosis lists were not retrieved.


References

1. (berengercurrias2023pluripotentstemcells pages 1-2): Noémie Bérenger-Currias, Cécile Martinat, and Sandrine Baghdoyan. Pluripotent stem cells in disease modeling and drug discovery for myotonic dystrophy type 1. Cells, 12:571, Feb 2023. URL: https://doi.org/10.3390/cells12040571, doi:10.3390/cells12040571. This article has 10 citations.

2. (hale2023dynamicsandvariability pages 1-2): Melissa A Hale, Kameron Bates, Marina Provenzano, and Nicholas E Johnson. Dynamics and variability of transcriptomic dysregulation in congenital myotonic dystrophy during pediatric development. Human Molecular Genetics, 32:1413-1428, Oct 2023. URL: https://doi.org/10.1093/hmg/ddac254, doi:10.1093/hmg/ddac254. This article has 23 citations and is from a domain leading peer-reviewed journal.

3. (almeida2023promisingaav.u7snrnasvectors pages 1-2): C. Almeida, F. Robriquet, T. Vetter, N. Huang, Reid Neinast, Lumariz Hernández-Rosario, D. Rajakumar, W. Arnold, K. McBride, K. Flanigan, Robert B. Weiss, N. Wein, M. Bartoli, N. Motohashi, O. Hernández-Hernández, Mexico Guillermo Ibarra Ibarra, CF Almeida, T. Vetter, WD Arnold, K. McBride, KM Flanigan, Robriquet Vetter Huang © 2023 Almeida, Arnold Rajakumar, and Flanigan Weiss Wein. This McBride. Promising aav.u7snrnas vectors targeting dmpk improve dm1 hallmarks in patient-derived cell lines. Frontiers in Cell and Developmental Biology, Jun 2023. URL: https://doi.org/10.3389/fcell.2023.1181040, doi:10.3389/fcell.2023.1181040. This article has 8 citations.

4. (stoodley2023applicationofantisense pages 1-2): Jessica Stoodley, Francisco Vallejo-Bedia, David Seone-Miraz, Manuel Debasa-Mouce, Matthew J. A. Wood, and Miguel A. Varela. Application of antisense conjugates for the treatment of myotonic dystrophy type 1. International Journal of Molecular Sciences, 24:2697, Jan 2023. URL: https://doi.org/10.3390/ijms24032697, doi:10.3390/ijms24032697. This article has 28 citations.

5. (abati2024cardiacriskand pages 1-2): Elena Abati, Claudia Alberti, Valentina Tambè, Anastasia Esseridou, Giacomo Pietro Comi, Stefania Corti, Giovanni Meola, and Francesco Secchi. Cardiac risk and myocardial fibrosis assessment with cardiac magnetic resonance in patients with myotonic dystrophy. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1493570, doi:10.3389/fneur.2024.1493570. This article has 4 citations and is from a peer-reviewed journal.

6. (hernaez2024prevalenceofsteinert’s pages 1-2): Leticia Hernáez, A. C. Zoni, M. Domínguez-Berjón, M. Esteban-Vasallo, C. Domínguez-González, P. Serrano, and On Behalf Of The Dm-Cm Working Group. Prevalence of steinert’s myotonic dystrophy and utilization of healthcare services: a population-based cross-sectional study. Healthcare, 12:838, Apr 2024. URL: https://doi.org/10.3390/healthcare12080838, doi:10.3390/healthcare12080838. This article has 2 citations.

7. (NCT06979024 chunk 1):  A Registered Observational Cohort Study of Myotonic Dystrophy Type 1. First Affiliated Hospital of Fujian Medical University. 2008. ClinicalTrials.gov Identifier: NCT06979024

8. (zhong2024clinicalfeaturesand pages 1-2): Huahua Zhong, Li Zeng, Xuefan Yu, Qing Ke, Jihong Dong, Yan Chen, Lijun Luo, Xueli Chang, Junhong Guo, Yiqi Wang, Hui Xiong, Rongrong Liu, Changxia Liu, Jibao Wu, Jie Lin, Jianying Xi, Wenhua Zhu, Song Tan, Fuchen Liu, Jiahong Lu, Chongbo Zhao, and Sushan Luo. Clinical features and genetic spectrum of a multicenter chinese cohort with myotonic dystrophy type 1. Orphanet Journal of Rare Diseases, Mar 2024. URL: https://doi.org/10.1186/s13023-024-03114-z, doi:10.1186/s13023-024-03114-z. This article has 2 citations and is from a peer-reviewed journal.

9. (stoodley2023applicationofantisense pages 8-9): Jessica Stoodley, Francisco Vallejo-Bedia, David Seone-Miraz, Manuel Debasa-Mouce, Matthew J. A. Wood, and Miguel A. Varela. Application of antisense conjugates for the treatment of myotonic dystrophy type 1. International Journal of Molecular Sciences, 24:2697, Jan 2023. URL: https://doi.org/10.3390/ijms24032697, doi:10.3390/ijms24032697. This article has 28 citations.

10. (ionova2024thestudyof pages 1-2): Sofya A. Ionova, Aysylu F. Murtazina, Andrey A. Marakhonov, Olga A. Shchagina, Nina V. Ryadninskaya, Inna S. Tebieva, Vitaly V. Kadyshev, Artem O. Borovikov, Evgeny K. Ginter, Sergey I. Kutsev, and Rena A. Zinchenko. The study of the inheritance mechanisms of myotonic dystrophy type 1 (dm1) in families from the republic of north ossetia-alania. International Journal of Molecular Sciences, 25:9734, Sep 2024. URL: https://doi.org/10.3390/ijms25179734, doi:10.3390/ijms25179734. This article has 3 citations.

11. (ricci2024assessmentofthe pages 17-20): FS Ricci. Assessment of the central nervous system involvement in neuromuscular disorders: the evolution of outcome measures in childhood rare diseases. Unknown journal, 2024.

12. (cerecedozapata2025fifteenyearsof pages 15-16): César M. Cerecedo-Zapata, Araceli Guerra-Grajeda, Luz C. Márquez-Quiróz, Paola Arciga-Portela, Rosa E. Escobar-Cedillo, Guadalupe E. Jiménez-Gutiérrez, Óscar A. Pérez-Méndez, Jorge S. Velasco-Flores, Blanca A. Barredo-Prieto, Norberto Leyva-García, Bulmaro Cisneros, Nadia M. Murillo-Melo, and Jonathan J. Magaña. Fifteen years of myotonic dystrophy type 1 in mexico: clinical, molecular, and socioeconomic insights from a national reference cohort. Genes, 16:1515, Dec 2025. URL: https://doi.org/10.3390/genes16121515, doi:10.3390/genes16121515. This article has 0 citations.

13. (zhong2024clinicalfeaturesand pages 5-7): Huahua Zhong, Li Zeng, Xuefan Yu, Qing Ke, Jihong Dong, Yan Chen, Lijun Luo, Xueli Chang, Junhong Guo, Yiqi Wang, Hui Xiong, Rongrong Liu, Changxia Liu, Jibao Wu, Jie Lin, Jianying Xi, Wenhua Zhu, Song Tan, Fuchen Liu, Jiahong Lu, Chongbo Zhao, and Sushan Luo. Clinical features and genetic spectrum of a multicenter chinese cohort with myotonic dystrophy type 1. Orphanet Journal of Rare Diseases, Mar 2024. URL: https://doi.org/10.1186/s13023-024-03114-z, doi:10.1186/s13023-024-03114-z. This article has 2 citations and is from a peer-reviewed journal.

14. (zhong2024clinicalfeaturesand media 408fef39): Huahua Zhong, Li Zeng, Xuefan Yu, Qing Ke, Jihong Dong, Yan Chen, Lijun Luo, Xueli Chang, Junhong Guo, Yiqi Wang, Hui Xiong, Rongrong Liu, Changxia Liu, Jibao Wu, Jie Lin, Jianying Xi, Wenhua Zhu, Song Tan, Fuchen Liu, Jiahong Lu, Chongbo Zhao, and Sushan Luo. Clinical features and genetic spectrum of a multicenter chinese cohort with myotonic dystrophy type 1. Orphanet Journal of Rare Diseases, Mar 2024. URL: https://doi.org/10.1186/s13023-024-03114-z, doi:10.1186/s13023-024-03114-z. This article has 2 citations and is from a peer-reviewed journal.

15. (zhong2024clinicalfeaturesand pages 2-5): Huahua Zhong, Li Zeng, Xuefan Yu, Qing Ke, Jihong Dong, Yan Chen, Lijun Luo, Xueli Chang, Junhong Guo, Yiqi Wang, Hui Xiong, Rongrong Liu, Changxia Liu, Jibao Wu, Jie Lin, Jianying Xi, Wenhua Zhu, Song Tan, Fuchen Liu, Jiahong Lu, Chongbo Zhao, and Sushan Luo. Clinical features and genetic spectrum of a multicenter chinese cohort with myotonic dystrophy type 1. Orphanet Journal of Rare Diseases, Mar 2024. URL: https://doi.org/10.1186/s13023-024-03114-z, doi:10.1186/s13023-024-03114-z. This article has 2 citations and is from a peer-reviewed journal.

16. (misquitta2024investigatingthetherapeutic pages 9-13): Naomi Misquitta. Investigating the therapeutic potential of amp-activated protein kinase in myotonic dystrophy type 1. Dissertation, Nov 2024. URL: https://doi.org/10.20381/ruor-30683, doi:10.20381/ruor-30683. This article has 0 citations.

17. (NCT02858908 chunk 1):  Study of Tideglusib in Adolescent and Adult Patients With Myotonic Dystrophy. AMO Pharma Limited. 2016. ClinicalTrials.gov Identifier: NCT02858908
