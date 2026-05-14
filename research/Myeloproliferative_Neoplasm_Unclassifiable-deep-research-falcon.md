---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T11:02:22.466369'
end_time: '2026-05-11T11:32:37.450668'
duration_seconds: 1814.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myeloproliferative Neoplasm, Unclassifiable
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myeloproliferative Neoplasm, Unclassifiable
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Myeloproliferative Neoplasm, Unclassifiable** covering all of the
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
- **Disease Name:** Myeloproliferative Neoplasm, Unclassifiable
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Myeloproliferative Neoplasm, Unclassifiable** covering all of the
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


## Disease Characteristics Research Report: Myeloproliferative Neoplasm, Unclassifiable (MPN-U) / MPN, Not Otherwise Specified (MPN-NOS)

### Scope note
This report is constrained to information available in the retrieved full-text excerpts and trial records in this run. Some requested identifier mappings (e.g., MONDO, Orphanet, MeSH), PMIDs, and model-organism details were not present in the retrieved corpus and are explicitly marked as unavailable/insufficient in this evidence set.

| Topic | Key sourced facts | Citation |
|---|---|---|
| Definition | MPN-U is a rare, heterogeneous myeloproliferative neoplasm showing features of an MPN but not fulfilling diagnostic criteria for another defined MPN; dynamic reassessment is recommended because some cases can later be reclassified. | (mclornan2022howimanage pages 1-1, mclornan2022howimanage pages 1-2) |
| WHO-HAEM5 vs ICC naming | WHO-HAEM5 retains the category as **MPN-NOS**; ICC 2022 uses **MPN-unclassifiable**. Both are catch-all categories for MPNs that cannot otherwise be classified. | (xiao2024apracticalapproach pages 2-4) |
| Estimated proportion among MPNs | Published estimates vary widely from about **5% to 30%** of all MPNs, but recent expert reviews state the true proportion is likely near the lower end when strict criteria are applied. In a large UK tertiary registry, **82/1512 = 5.4%** of MPN patients were classified as MPN-U. Review articles also summarize a typical range of **~5–10%**. | (mclornan2022howimanage pages 1-1, hargreaves2022diagnosticandmanagement pages 1-2, deschamps2021clinicopathologicalcharacterisationof pages 1-2, mclornan2022howimanage pages 1-2, pizzi2021theclassificationof pages 7-8) |
| Key diagnostic exclusions | A diagnosis of MPN-U should **not** be made when another defining lesion/entity is present, including **BCR::ABL1**, **PCM1-JAK2**, and rearrangements involving **PDGFRA, PDGFRB, or FGFR1**; reactive causes such as infection, toxin/drug exposure, growth factors, cytokines, or immunosuppressive drugs should be excluded. | (mclornan2022howimanage pages 2-2, hargreaves2022diagnosticandmanagement pages 1-2, gianelli2023internationalconsensusclassification pages 13-14, mclornan2022howimanage pages 1-2) |
| Typical clinical features | Common presentations include **thrombocytosis**, **raised LDH**, **clustered/pleomorphic megakaryocytes** on marrow biopsy, **splenomegaly**, **pruritus**, constitutional symptoms, and clinically important **thrombosis**, including atypical sites such as splanchnic vein thrombosis. Early-phase cases may have overlapping ET/pre-PMF morphology; advanced fibrotic cases may be harder to subtype. | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, pizzi2021theclassificationof pages 7-8, mclornan2022howimanage pages 2-2, deschamps2021clinicopathologicalcharacterisationof pages 2-3, gianelli2023internationalconsensusclassification pages 13-14) |
| Quantified phenotype frequencies in the UK cohort | In the 82-patient Guy’s and St Thomas’ cohort: **thrombocytosis 78%**, **elevated LDH 72%**, **splenomegaly 27%**, **pruritus 36%**, constitutional symptoms **29%**, thrombosis **20.7–21%**, and transfusion dependence **2.4%**. Median age was **49.7 years** and **56%** were female. | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, deschamps2021clinicopathologicalcharacterisationof pages 2-3) |
| Driver mutation frequencies | In the same cohort, driver lesions were: **JAK2 V617F 53.7% (44/82)**, **JAK2 exon 12 2.4% (2/82)**, **CALR type 1 8.5% (7/82)**, **CALR type 2 4.8% (4/82)**, **MPL 6.1% (5/82)**; **triple-negative 24% (20/82)**. No **PDGFRA/B, CSF3R, BCR/ABL1, FGFR1, or PCM1-JAK2** rearrangements were found in that series. | (deschamps2021clinicopathologicalcharacterisationof pages 1-2) |
| Other molecular findings | Extended molecular testing showed additional non-driver mutations in **24% (7/29)** of tested patients; review sources note that evidence of clonality may also come from mutations such as **ASXL1, EZH2, TET2, IDH1/2, SRSF2, SF3B1**. Cytogenetic abnormalities support diagnosis and occur in roughly **20–30%** of cases in review summaries, although **88.5%** of tested cases in the UK cohort had normal cytogenetics. | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, pizzi2021theclassificationof pages 7-8, gianelli2023internationalconsensusclassification pages 13-14) |
| Prognosis: event-free and overall survival | In the UK cohort, median **event-free survival (EFS) was 11.25 years** (95% CI **9.3–not reached**); median **overall survival was not reached**; estimated **10-year OS was 88.8%** (95% CI **77.7–100.0%**). | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, deschamps2021clinicopathologicalcharacterisationof pages 2-3) |
| Prognosis: transformation and progression | **7/82 (8.5%)** transformed to accelerated/blast phase, with median time to transformation **88.2 months**; approximately **19.2%** ultimately showed disease progression including accelerated phase/transformation or fibrosis. Advanced/fibrotic MPN-U is generally viewed as having worse prognosis than early-phase disease. | (mclornan2022howimanage pages 1-2, deschamps2021clinicopathologicalcharacterisationof pages 2-3, deschamps2021clinicopathologicalcharacterisationof pages 5-6, pizzi2021theclassificationof pages 7-8) |
| Prognostic factors | Worse EFS was associated with **platelet count <500 × 10^9/L** and **leukocytosis ≥12 × 10^9/L** at presentation. Multivariable analysis found low platelets independently adverse (**HR 3.45, 95% CI 1.43–8.32**) and leukocytosis also adverse (**HR 2.91, 95% CI 1.11–7.64**). | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, deschamps2021clinicopathologicalcharacterisationof pages 2-3, deschamps2021clinicopathologicalcharacterisationof pages 5-6, deschamps2021clinicopathologicalcharacterisationof media cb1fee4a) |


*Table: This table summarizes high-yield, source-backed facts on myeloproliferative neoplasm, unclassifiable, including nomenclature, diagnostic boundaries, phenotype, molecular findings, and prognosis. It is useful as a compact evidence table for building a disease knowledge base entry.*

| Management domain | Therapy/approach | Real-world implementation in MPN-U / MPN-NOS | Quantitative details | Citation |
|---|---|---|---|---|
| Cytoreduction | Any cytoreductive therapy | Commonly used in practice, but indications are phenotype-driven rather than guideline-standardized | In the UK cohort, 51/82 patients (62.2%) received cytoreductive therapy; in the survey, 66% of centres would offer cytoreduction for thrombocytosis | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7) |
| Cytoreduction | Hydroxycarbamide / hydroxyurea | Most commonly used first-line cytoreductive agent in cohort and survey practice | UK cohort: 40/82 (48.8%) received hydroxycarbamide; survey: 14 centres (41%) targeted platelets around 400 × 10^9/L, and 20 centres (59%) combined hydroxycarbamide with extended postoperative thromboprophylaxis | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6) |
| Cytoreduction | Interferon / pegylated interferon | Used in a minority overall; may be considered in selected settings such as pregnancy or younger patients, but not a common first-choice agent in survey responses | UK cohort: 14/82 (17.1%) received interferon; survey of thrombocytosis management: no centres selected interferon as agent of choice; pregnancy-focused recommendations note interferon-based approaches at some centres | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6, mclornan2022howimanage pages 4-5) |
| Cytoreduction | Anagrelide | Used infrequently for platelet control in selected patients | UK cohort: 8/82 (9.8%) received anagrelide | (deschamps2021clinicopathologicalcharacterisationof pages 1-2) |
| Symptom/spleen-directed therapy | Ruxolitinib / JAK inhibitor | Off-label, phenotype-driven use for splenomegaly and symptom burden; many centres report little or no use, reflecting uncertainty and lack of approval | UK cohort: 5/82 (6.1%) received a JAK inhibitor; survey/review: about half of centres reported off-label ruxolitinib use for splenomegaly and/or symptoms, while many centres had no MPN-U patients on ruxolitinib | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 3-6, mclornan2022howimanage pages 7-7) |
| Antithrombotic management | Aspirin | Frequently used, especially with thrombocytosis and in pregnancy; does not eliminate thrombosis risk | Review suggests aspirin 75 mg once daily in selected phenotype-driven strategies; pregnancy recommendations include aspirin throughout pregnancy; cohort noted thromboses still occurred despite low-dose aspirin plus effective cytoreduction | (mclornan2022howimanage pages 8-9, mclornan2022howimanage pages 4-5, deschamps2021clinicopathologicalcharacterisationof pages 3-5) |
| Antithrombotic management | LMWH | Used particularly in pregnancy and postpartum; also part of broader thrombosis management strategies extrapolated from other MPNs | Pregnancy guidance: antenatal LMWH plus standard 6-week postpartum prophylaxis | (mclornan2022howimanage pages 4-5) |
| Antithrombotic management | VKA / warfarin | Common choice after venous thromboembolism, especially in heterogeneous real-world practice | Survey: most centres preferred warfarin/VKA after VTE; some reserved VKA specifically for splanchnic vein thrombosis | (hargreaves2022diagnosticandmanagement pages 3-6) |
| Antithrombotic management | DOACs | Used by some centres; authors cautiously support DOACs in uncomplicated acute SVT, but liver dysfunction may limit use | Review notes VKA vs DOAC decisions are individualized; cohort/international data cited as showing comparable recurrent thrombosis and bleeding rates with DOACs in selected settings | (mclornan2022howimanage pages 5-6, hargreaves2022diagnosticandmanagement pages 3-6) |
| Cytoreduction triggers | Thrombosis history | Many centres start cytoreduction after arterial or venous thrombosis, despite lack of MPN-U-specific evidence | 81% of surveyed centres initiate cytoreduction after venous or arterial thrombosis | (mclornan2022howimanage pages 7-7) |
| Cytoreduction triggers | Blood count thresholds | Centres variably use platelet/WBC thresholds to start therapy | Survey: platelet threshold >450 × 10^9/L in 20% of centres, >1500 × 10^9/L in 72%, WBC >15 × 10^9/L in 45% | (mclornan2022howimanage pages 7-7) |
| Response in cohort | Cytoreductive treatment outcomes | Outcomes are mixed, reinforcing need for better prognostic tools and standardized management | Among treated cohort patients, ~50% achieved adequate cytoreduction, 26.9% had stable blood counts, and 19.2% progressed (accelerated/transformation or fibrosis) | (deschamps2021clinicopathologicalcharacterisationof pages 3-5) |
| Transplant | Allogeneic hematopoietic cell transplantation | Rare but considered for accelerated, blast-phase, fibrotic, or otherwise aggressive disease; early referral is recommended in suitable patients | UK cohort: 5/82 (6.1%) considered for allo-HCT and 2/82 (2.4%) transplanted; survey: observation 7%, HMA with planned allo-SCT 61%, induction chemotherapy then allo-SCT 7%, upfront allo-SCT 24% for progressive/accelerating disease | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, mclornan2022howimanage pages 6-7, deschamps2021clinicopathologicalcharacterisationof pages 3-5) |
| Transplant outcomes | Allo-HCT registry data | Best evidence comes from retrospective registry series rather than MPN-U-specific trials | Reported 3-year OS after allo-SCT approximately 55% with myeloablative conditioning vs 44% with reduced-intensity conditioning; relapse rates 23% vs 36% | (hargreaves2022diagnosticandmanagement pages 6-7) |
| Monitoring/implementation | Practice framework | Management is individualized because there are no agreed guidelines; cases often managed similarly to classical MPNs and re-reviewed over time | Survey explicitly reports “lack of agreed guidelines” and wide heterogeneity in MDT review, genomic testing, anticoagulant choice, pregnancy care, and transplant referral | (hargreaves2022diagnosticandmanagement pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6) |
| Relevant trial/registry | NCT07362225 | Large observational registry tracking symptoms, treatments, and disease progression in people with MPNs; relevant because MPN-U patients are commonly excluded from interventional studies but can be captured in broad registries | Recruiting; observational; target enrollment 5000 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT03618485 | Taiwan MPN registry; observational real-world resource potentially capturing unclassifiable cases under broader MPN umbrella | Active, not recruiting; observational; target enrollment 500 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT07384039 | Supportive-care/exercise intervention in patients with MPNs; relevant to symptom burden and quality-of-life research though not MPN-U-specific | Not yet recruiting; interventional; target enrollment 80 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT06661915 | Phase 2 study in advanced MPNs using ASTX727 with or without iadademstat; relevant for transformed/advanced phenotypes that may include unclassifiable MPN biology | Recruiting; phase 2; target enrollment 62 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT04282187 | Phase 2 study of decitabine with ruxolitinib/fedratinib/pacritinib for accelerated/blast-phase MPN; relevant to aggressive MPN-U scenarios managed as advanced MPN | Recruiting; phase 2; target enrollment 25 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT03566446 | CALR-mutant peptide vaccine study in CALR-mutant MPN; relevant to molecularly defined subsets that may overlap with some MPN-U cases | Completed; phase 1; enrollment 10 | (xiao2024apracticalapproach pages 2-4) |


*Table: This table summarizes how MPN-U/MPN-NOS is managed in real-world cohorts, surveys, and broader MPN studies. It highlights the absence of standardized guidelines, the phenotype-driven use of cytoreduction and antithrombotic therapy, transplant escalation in advanced disease, and relevant current trial or registry infrastructure.*

### Key visual evidence (prognosis)
Event-free survival stratified by platelet count and leukocytosis (and accompanying prognostic factor table) was extracted from the largest available contemporary cohort; this supports the statement that lower platelets and leukocytosis identify higher-risk MPN-U subgroups. (deschamps2021clinicopathologicalcharacterisationof media cb1fee4a, deschamps2021clinicopathologicalcharacterisationof media 1f80ac50)

---

## 1. Disease Information

### Overview / definition
Myeloproliferative neoplasm, unclassifiable (MPN-U) is defined as a myeloproliferative neoplasm with clinical/hematologic/morphologic features of an MPN that does not fulfill diagnostic criteria for any other defined MPN entity; it is described as rare, heterogeneous, and often requiring “dynamic review over time” because some cases may later become classifiable as PV/ET/PMF or another MPN. (mclornan2022howimanage pages 1-1, mclornan2022howimanage pages 1-2)

### Current classification terminology (WHO vs ICC)
Both WHO-HAEM5 and the International Consensus Classification (ICC) retain a “catch-all” entity for otherwise unclassifiable MPNs, but with different names: **MPN-NOS** in WHO-HAEM5 versus **MPN-unclassifiable** in the ICC. (xiao2024apracticalapproach pages 2-4)

### Synonyms / alternative names
Commonly used names include “myeloproliferative neoplasm, unclassifiable” and “MPN not otherwise specified (NOS)” in WHO-era usage. (mclornan2022howimanage pages 1-1, xiao2024apracticalapproach pages 2-4, pizzi2021theclassificationof pages 7-8)

### Key identifiers (available in retrieved sources)
* **ICD-10**: in a Danish population cohort using registry codes, MPN-U/MPN-NOS was identified using **ICD-10 D47.1**. (pedersen2018smokingisassociated pages 2-3)

Identifiers not found in retrieved corpus: MONDO ID, Orphanet ID, and MeSH term mappings were not present in the excerpts retrieved for this run.

### Evidence type note (patient-level vs aggregated)
Evidence spans (i) aggregated cohort/registry studies (UK tertiary-center cohort; population-based Danish and Swedish studies) and (ii) expert review/survey synthesis. (deschamps2021clinicopathologicalcharacterisationof pages 2-3, hargreaves2022diagnosticandmanagement pages 6-7, landtblom2018secondmalignanciesin pages 3-4, pedersen2020twofoldriskof pages 1-2)

---

## 2. Etiology

### Disease causal factors (current understanding)
MPN-U is best understood as a **clonal hematopoietic stem/progenitor cell disorder** that manifests as myeloproliferation but lacks sufficient integrated clinicopathologic criteria to be assigned to a specific MPN subtype at a given timepoint. Clonality is commonly supported by canonical MPN “driver” mutations (JAK2/CALR/MPL) and/or other myeloid neoplasm–associated mutations and cytogenetic abnormalities. (gianelli2023internationalconsensusclassification pages 13-14, pizzi2021theclassificationof pages 7-8)

### Risk factors
**Smoking (lifestyle/environmental):** In a Danish general-population cohort (DANHES), smoking was associated with higher risk of incident MPN overall and particularly high relative risks for MPN-U. Multivariable HR for **any MPN** was 2.5 (95% CI 1.3–5.0) for daily smokers versus never-smokers; subtype analysis showed **MPN-U HR 6.2 (1.5–25)** for daily smokers and **MPN-U HR 6.2 (1.8–21)** for occasional/ex-smokers. (pedersen2018smokingisassociated pages 1-2)

Other environmental/occupational risk factors were mentioned only qualitatively as conflicting/limited in the retrieved excerpts; no robust, MPN-U-specific quantitative estimates beyond smoking were retrieved. (pedersen2018smokingisassociated pages 5-6)

### Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence set.

### Gene–environment interactions
No explicit gene–environment interaction evidence (e.g., JAK2 genotype-by-smoking) was available in the retrieved excerpts.

---

## 3. Phenotypes (clinical features) and HPO suggestions

### Typical phenotype spectrum
MPN-U shows a broad phenotype that can include constitutional symptoms, hepatosplenomegaly, thrombosis (including splanchnic vein thrombosis), and variable blood-count abnormalities; cases may represent a prodromal/pre-proliferative stage of classical MPN. (mclornan2022howimanage pages 2-2)

### Quantified phenotype frequencies from a contemporary cohort (UK tertiary center)
In a single-center cohort of **82 MPN-U** patients (median age 49.7 years; 56% female): splenomegaly **27%**, pruritus **36%**, constitutional symptoms **29%**, transfusion dependency **2.4%**; thrombocytosis **78%** (median platelets 650×10^9/L); LDH elevated **72%**; peripheral blood film features included teardrop cells (18.3%), leukoerythroblastosis (7%), and prominent large granular lymphocytes (19.7%). (deschamps2021clinicopathologicalcharacterisationof pages 2-3)

### Thrombotic phenotype (including timing)
In the same cohort, thrombosis occurred in **~21%** (arterial 10; portal vein 4; other venous 3), with median time from diagnosis to thrombotic event **0.2 months** (0–208.3); 47% of those with thrombosis presented with a “heralding” thrombosis (9.9% of the whole cohort). (deschamps2021clinicopathologicalcharacterisationof pages 2-3)

### Suggested HPO terms (non-exhaustive; mapping requires ontology validation)
* Thrombocytosis — **HP:0001894** (supported by cohort frequency) (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* Elevated lactate dehydrogenase — **HP:0003287** (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* Splenomegaly — **HP:0001744** (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* Pruritus — **HP:0000989** (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* Constitutional symptoms / weight loss / night sweats — consider **HP:0004377** (weight loss) and related terms (symptom list in review) (mclornan2022howimanage pages 2-2)
* Portal vein thrombosis / splanchnic vein thrombosis — consider **HP:0030244** (portal vein thrombosis) and related SVT terms (deschamps2021clinicopathologicalcharacterisationof pages 2-3, pizzi2021theclassificationof pages 7-8)
* Anemia — **HP:0001903** (not frequent in the cohort, but part of advanced phenotype in reviews) (pizzi2021theclassificationof pages 7-8)

Quality-of-life: MPN-SAF symptom scores ranged 0–73/100 in a subset, indicating wide symptom-burden variability, but no standardized QoL instruments (EQ-5D/SF-36) or comparative QoL statistics were available in retrieved excerpts. (deschamps2021clinicopathologicalcharacterisationof pages 3-5)

---

## 4. Genetic/Molecular Information

### Molecular hallmarks and clonality support
Diagnosis requires exclusion of reactive conditions (infection/toxin/drug-related) and can be supported by detection of canonical MPN driver mutations or other myeloid neoplasm–associated mutations (e.g., ASXL1, EZH2, TET2, IDH1/2, SRSF2, SF3B1) and/or cytogenetic abnormalities. (gianelli2023internationalconsensusclassification pages 13-14, pizzi2021theclassificationof pages 7-8)

### Driver mutation frequencies (cohort data)
In the 82-patient UK cohort:
* **JAK2 V617F**: 53.7% (44/82)
* **JAK2 exon 12**: 2.4% (2/82)
* **CALR type 1**: 8.5% (7/82)
* **CALR type 2**: 4.8% (4/82)
* **MPL**: 6.1% (5/82)
* **Triple-negative (JAK2/CALR/MPL negative)**: 24% (20/82)
No PDGFRA/B, CSF3R, BCR/ABL1, FGFR1, or PCM1-JAK2 rearrangements were detected in that series. (deschamps2021clinicopathologicalcharacterisationof pages 1-2)

### Additional somatic mutations / cytogenetics
Extended molecular testing identified additional non-driver mutations in 24% (7/29) of those tested in the UK cohort. (deschamps2021clinicopathologicalcharacterisationof pages 1-2)
Reviews summarize cytogenetic abnormalities in ~20–30% (or ~30%) of MPN-U cases; in the UK cohort with available cytogenetics, 88.5% were normal (suggesting cohort and testing differences). (gianelli2023internationalconsensusclassification pages 13-14, deschamps2021clinicopathologicalcharacterisationof pages 1-2)

### Variant classification / allele frequency / germline vs somatic
Not available in the retrieved excerpts (no ClinVar/gnomAD-style allele frequency reporting was present).

### Epigenetics / transcriptomics / proteomics / metabolomics
Not available in the retrieved excerpts.

---

## 5. Environmental Information

Beyond smoking (Section 2), no specific toxins/radiation/pollution or infectious triggers with reproducible quantitative evidence specific to MPN-U were available in the retrieved excerpts. (pedersen2018smokingisassociated pages 5-6)

---

## 6. Mechanism / Pathophysiology (high-level)

Mechanistically, MPN-U is interpreted as clonal myeloid proliferation driven by canonical MPN signaling lesions (JAK2/CALR/MPL) in many cases, with additional cooperating mutations in epigenetic regulators and splicing factors in subsets; however, the defining feature of MPN-U is not a unique pathway but rather failure to meet integrated diagnostic thresholds for a specific MPN subtype at the time of evaluation. (gianelli2023internationalconsensusclassification pages 13-14, pizzi2021theclassificationof pages 7-8)

Mechanistic details (e.g., JAK-STAT pathway activation, inflammatory cytokine loops) were not available as primary mechanistic experiments in this evidence set; only epidemiologic/mechanistic plausibility statements linking smoking to inflammatory signaling were present. (pedersen2018smokingisassociated pages 5-6)

Suggested GO biological-process terms (hypothesis-driven; requires validation):
* “myeloid cell proliferation” (GO:0008283 related), “hematopoietic stem cell proliferation” (GO terms vary)

Suggested CL cell types (hypothesis-driven; requires validation):
* Hematopoietic stem cell (CL:0000037), myeloid progenitor (CL:0000763), megakaryocyte (CL:0000554)

---

## 7. Anatomical Structures Affected

Primary anatomic sites include:
* **Bone marrow** (hypercellularity; megakaryocytic clustering/pleomorphism; variable fibrosis) (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* **Spleen** (splenomegaly; extramedullary hematopoiesis mentioned in reviews) (deschamps2021clinicopathologicalcharacterisationof pages 2-3, mclornan2022howimanage pages 2-2)
* **Splanchnic vasculature** (portal vein thrombosis and broader SVT association; a major clinical presentation route) (deschamps2021clinicopathologicalcharacterisationof pages 2-3, pizzi2021theclassificationof pages 7-8)

Suggested UBERON terms (requires validation):
* Bone marrow — UBERON:0002371
* Spleen — UBERON:0002106
* Portal vein — UBERON:0001189

Subcellular localization was not addressed in retrieved excerpts.

---

## 8. Temporal Development

MPN-U is commonly conceptualized as including:
* **Early/prodromal phase** with incompletely developed subtype-specific morphology (often overlapping ET/pre-PMF) and fewer organomegaly features (gianelli2023internationalconsensusclassification pages 13-14, pizzi2021theclassificationof pages 7-8)
* **Advanced fibrotic phase** with cytopenias, organomegaly, fibrosis-related marrow changes, and higher transformation risk (pizzi2021theclassificationof pages 7-8)

In the UK cohort, transformation to accelerated/blast phase occurred in 7/82 (8.5%) with median time to transformation 88.2 months (15.6–183.9). (deschamps2021clinicopathologicalcharacterisationof pages 2-3)

---

## 9. Inheritance and Population

### Inheritance
MPN-U is generally discussed as a somatic clonal neoplasm; explicit Mendelian inheritance patterns were not described in the retrieved excerpts.

### Epidemiology (proportion among MPNs)
MPN-U is estimated at **~5–10%** of MPNs in reviews/classification discussions. (pizzi2021theclassificationof pages 7-8, gianelli2023internationalconsensusclassification pages 11-13)
In a UK tertiary registry, MPN-U constituted **82/1512 = 5.4%** of MPN patients. (deschamps2021clinicopathologicalcharacterisationof pages 1-2)

### Age/sex distribution
In the UK cohort: median age 49.7 years (range 13–79) and 56% female. (deschamps2021clinicopathologicalcharacterisationof pages 2-3)

---

## 10. Diagnostics (limited to retrieved evidence)

### Diagnostic framing
Diagnosis is clinicopathologic and by exclusion: “features of an MPN are present” but criteria for defined entities are not met, and exclusionary rearrangements/fusions (e.g., BCR::ABL1, PCM1-JAK2; PDGFRA/B; FGFR1) must be absent; reactive drivers such as infection/toxin/drug exposure should be ruled out. (gianelli2023internationalconsensusclassification pages 13-14, mclornan2022howimanage pages 1-2)

### WHO vs ICC placement
WHO-HAEM5 uses MPN-NOS; ICC uses MPN-unclassifiable. (xiao2024apracticalapproach pages 2-4)

### Molecular testing sensitivity / contemporary updates
ICC-focused review text recommends highly sensitive molecular techniques for identifying JAK2/CALR/MPL driver mutations, with “minimal level of VAF 1%” as a recommended diagnostic backbone (in the ICC MPN classification paper’s conclusion). (gianelli2023internationalconsensusclassification pages 14-15)

### Differential diagnosis (high-level)
Key exclusions include entities defined by specific lesions (e.g., BCR::ABL1; eosinophilia with tyrosine kinase fusions), and careful separation from MDS/MPN overlap neoplasms when dysplasia predominates. (gianelli2023internationalconsensusclassification pages 13-14)

Not available in retrieved evidence: complete WHO-HAEM5/ICC “major/minor criteria” tables for MPN-NOS/MPN-U, SNOMED/LOINC mappings, and structured genetic testing panel recommendations beyond general statements.

---

## 11. Outcome / Prognosis

### Cohort-based survival estimates
In the UK cohort (n=82):
* Median **event-free survival (EFS) 11.25 years** (95% CI 9.3–not reached)
* Median OS not reached; **10-year OS 88.8%** (95% CI 77.7–100.0%) (deschamps2021clinicopathologicalcharacterisationof pages 2-3)

### Transformation/progression
* Transformation to accelerated/blast phase: **8.5%** (7/82), median 88.2 months (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* Overall progression (accelerated/transformation or fibrosis): ~19.2% in treated subgroup reporting (deschamps2021clinicopathologicalcharacterisationof pages 3-5, deschamps2021clinicopathologicalcharacterisationof pages 5-6)

### Prognostic factors (EFS)
Lower platelets and leukocytosis stratified higher-risk groups: low platelet quartile HR 3.45 (95% CI 1.43–8.32) and leukocytosis HR 2.91 (95% CI 1.11–7.64) in multivariable analysis. (deschamps2021clinicopathologicalcharacterisationof pages 5-6, deschamps2021clinicopathologicalcharacterisationof media cb1fee4a)

### Complications and comorbidity burden (population-based)
* **Pneumonia and respiratory mortality:** In a Danish cohort, myelofibrosis/unclassifiable MPN had HR 3.03 (95% CI 1.86–4.93) for pneumonia and HR 2.40 (95% CI 1.11–5.19) for respiratory death (subtypes combined). (pedersen2020twofoldriskof pages 1-2)
* **Second malignancies:** In a Swedish population cohort (9379 MPN patients; 1113 MPN-U), the hazard ratio for non-hematologic second malignancies in **MPN-U** was **HR 1.9 (95% CI 1.5–2.5)** versus controls. (landtblom2018secondmalignanciesin pages 3-4)

---

## 12. Treatment (evidence-limited; phenotype-driven)

There are no licensed, MPN-U-specific therapies highlighted in the retrieved evidence; management is explicitly described as challenging due to “lack of agreed guidelines” and is generally **phenotype- and complication-driven** (treating cytoses, symptoms/splenomegaly, and thrombosis risk similarly to classical MPNs). (hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6)

Real-world approaches are summarized in the management artifact (cytoreduction, antithrombotics, ruxolitinib off-label, allo-HCT escalation, and key MPN registries/trials). | Management domain | Therapy/approach | Real-world implementation in MPN-U / MPN-NOS | Quantitative details | Citation |
|---|---|---|---|---|
| Cytoreduction | Any cytoreductive therapy | Commonly used in practice, but indications are phenotype-driven rather than guideline-standardized | In the UK cohort, 51/82 patients (62.2%) received cytoreductive therapy; in the survey, 66% of centres would offer cytoreduction for thrombocytosis | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7) |
| Cytoreduction | Hydroxycarbamide / hydroxyurea | Most commonly used first-line cytoreductive agent in cohort and survey practice | UK cohort: 40/82 (48.8%) received hydroxycarbamide; survey: 14 centres (41%) targeted platelets around 400 × 10^9/L, and 20 centres (59%) combined hydroxycarbamide with extended postoperative thromboprophylaxis | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6) |
| Cytoreduction | Interferon / pegylated interferon | Used in a minority overall; may be considered in selected settings such as pregnancy or younger patients, but not a common first-choice agent in survey responses | UK cohort: 14/82 (17.1%) received interferon; survey of thrombocytosis management: no centres selected interferon as agent of choice; pregnancy-focused recommendations note interferon-based approaches at some centres | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6, mclornan2022howimanage pages 4-5) |
| Cytoreduction | Anagrelide | Used infrequently for platelet control in selected patients | UK cohort: 8/82 (9.8%) received anagrelide | (deschamps2021clinicopathologicalcharacterisationof pages 1-2) |
| Symptom/spleen-directed therapy | Ruxolitinib / JAK inhibitor | Off-label, phenotype-driven use for splenomegaly and symptom burden; many centres report little or no use, reflecting uncertainty and lack of approval | UK cohort: 5/82 (6.1%) received a JAK inhibitor; survey/review: about half of centres reported off-label ruxolitinib use for splenomegaly and/or symptoms, while many centres had no MPN-U patients on ruxolitinib | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 3-6, mclornan2022howimanage pages 7-7) |
| Antithrombotic management | Aspirin | Frequently used, especially with thrombocytosis and in pregnancy; does not eliminate thrombosis risk | Review suggests aspirin 75 mg once daily in selected phenotype-driven strategies; pregnancy recommendations include aspirin throughout pregnancy; cohort noted thromboses still occurred despite low-dose aspirin plus effective cytoreduction | (mclornan2022howimanage pages 8-9, mclornan2022howimanage pages 4-5, deschamps2021clinicopathologicalcharacterisationof pages 3-5) |
| Antithrombotic management | LMWH | Used particularly in pregnancy and postpartum; also part of broader thrombosis management strategies extrapolated from other MPNs | Pregnancy guidance: antenatal LMWH plus standard 6-week postpartum prophylaxis | (mclornan2022howimanage pages 4-5) |
| Antithrombotic management | VKA / warfarin | Common choice after venous thromboembolism, especially in heterogeneous real-world practice | Survey: most centres preferred warfarin/VKA after VTE; some reserved VKA specifically for splanchnic vein thrombosis | (hargreaves2022diagnosticandmanagement pages 3-6) |
| Antithrombotic management | DOACs | Used by some centres; authors cautiously support DOACs in uncomplicated acute SVT, but liver dysfunction may limit use | Review notes VKA vs DOAC decisions are individualized; cohort/international data cited as showing comparable recurrent thrombosis and bleeding rates with DOACs in selected settings | (mclornan2022howimanage pages 5-6, hargreaves2022diagnosticandmanagement pages 3-6) |
| Cytoreduction triggers | Thrombosis history | Many centres start cytoreduction after arterial or venous thrombosis, despite lack of MPN-U-specific evidence | 81% of surveyed centres initiate cytoreduction after venous or arterial thrombosis | (mclornan2022howimanage pages 7-7) |
| Cytoreduction triggers | Blood count thresholds | Centres variably use platelet/WBC thresholds to start therapy | Survey: platelet threshold >450 × 10^9/L in 20% of centres, >1500 × 10^9/L in 72%, WBC >15 × 10^9/L in 45% | (mclornan2022howimanage pages 7-7) |
| Response in cohort | Cytoreductive treatment outcomes | Outcomes are mixed, reinforcing need for better prognostic tools and standardized management | Among treated cohort patients, ~50% achieved adequate cytoreduction, 26.9% had stable blood counts, and 19.2% progressed (accelerated/transformation or fibrosis) | (deschamps2021clinicopathologicalcharacterisationof pages 3-5) |
| Transplant | Allogeneic hematopoietic cell transplantation | Rare but considered for accelerated, blast-phase, fibrotic, or otherwise aggressive disease; early referral is recommended in suitable patients | UK cohort: 5/82 (6.1%) considered for allo-HCT and 2/82 (2.4%) transplanted; survey: observation 7%, HMA with planned allo-SCT 61%, induction chemotherapy then allo-SCT 7%, upfront allo-SCT 24% for progressive/accelerating disease | (deschamps2021clinicopathologicalcharacterisationof pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, mclornan2022howimanage pages 6-7, deschamps2021clinicopathologicalcharacterisationof pages 3-5) |
| Transplant outcomes | Allo-HCT registry data | Best evidence comes from retrospective registry series rather than MPN-U-specific trials | Reported 3-year OS after allo-SCT approximately 55% with myeloablative conditioning vs 44% with reduced-intensity conditioning; relapse rates 23% vs 36% | (hargreaves2022diagnosticandmanagement pages 6-7) |
| Monitoring/implementation | Practice framework | Management is individualized because there are no agreed guidelines; cases often managed similarly to classical MPNs and re-reviewed over time | Survey explicitly reports “lack of agreed guidelines” and wide heterogeneity in MDT review, genomic testing, anticoagulant choice, pregnancy care, and transplant referral | (hargreaves2022diagnosticandmanagement pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6) |
| Relevant trial/registry | NCT07362225 | Large observational registry tracking symptoms, treatments, and disease progression in people with MPNs; relevant because MPN-U patients are commonly excluded from interventional studies but can be captured in broad registries | Recruiting; observational; target enrollment 5000 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT03618485 | Taiwan MPN registry; observational real-world resource potentially capturing unclassifiable cases under broader MPN umbrella | Active, not recruiting; observational; target enrollment 500 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT07384039 | Supportive-care/exercise intervention in patients with MPNs; relevant to symptom burden and quality-of-life research though not MPN-U-specific | Not yet recruiting; interventional; target enrollment 80 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT06661915 | Phase 2 study in advanced MPNs using ASTX727 with or without iadademstat; relevant for transformed/advanced phenotypes that may include unclassifiable MPN biology | Recruiting; phase 2; target enrollment 62 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT04282187 | Phase 2 study of decitabine with ruxolitinib/fedratinib/pacritinib for accelerated/blast-phase MPN; relevant to aggressive MPN-U scenarios managed as advanced MPN | Recruiting; phase 2; target enrollment 25 | (xiao2024apracticalapproach pages 2-4) |
| Relevant trial/registry | NCT03566446 | CALR-mutant peptide vaccine study in CALR-mutant MPN; relevant to molecularly defined subsets that may overlap with some MPN-U cases | Completed; phase 1; enrollment 10 | (xiao2024apracticalapproach pages 2-4) |


*Table: This table summarizes how MPN-U/MPN-NOS is managed in real-world cohorts, surveys, and broader MPN studies. It highlights the absence of standardized guidelines, the phenotype-driven use of cytoreduction and antithrombotic therapy, transplant escalation in advanced disease, and relevant current trial or registry infrastructure.*

Suggested MAXO terms (requires ontology validation):
* Cytoreductive therapy — e.g., MAXO term for “cytoreductive therapy”
* Antiplatelet therapy (aspirin)
* Anticoagulation therapy
* Allogeneic hematopoietic stem cell transplantation

---

## 13. Prevention

No primary-prevention interventions specific to MPN-U were identified. Smoking is a modifiable risk factor associated with MPN risk including MPN-U in one large cohort; smoking cessation is therefore a plausible risk-reduction strategy, although direct evidence for prevention of MPN-U is not established. (pedersen2018smokingisassociated pages 1-2)

Secondary/tertiary prevention in practice focuses on prevention of thrombosis/bleeding and monitoring for disease evolution or transformation, but no consensus prevention protocols were available in the retrieved excerpts. (hargreaves2022diagnosticandmanagement pages 3-6, mclornan2022howimanage pages 7-7)

---

## 14. Other Species / Natural Disease

No cross-species naturally occurring MPN-U analogs were identified in the retrieved evidence set.

---

## 15. Model Organisms

The retrieved evidence set did not include dedicated model-organism studies for MPN-U. Mechanistic model systems for canonical MPN driver mutations (e.g., JAK2/CALR/MPL) are widely used in the broader MPN field, but explicit, citable details were not present in the retrieved excerpts and therefore are not asserted here.

---

## “Expert opinion” synthesis (authoritative-source analysis)
Across expert reviews and international survey data, a consistent expert conclusion is that MPN-U is a **heterogeneous, diagnosis-of-exclusion category** with meaningful thrombotic and transformation risks but **insufficient evidence for standardized, disease-specific guidelines**, leading to high inter-center practice variability and reliance on extrapolation from classical MPN management and individualized risk assessment. (mclornan2022howimanage pages 1-2, hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6)

---

## References (URLs and publication dates from retrieved sources)
* Xiao W et al. *A practical approach on the classifications of myeloid neoplasms and acute leukemia: WHO and ICC*. **Jul 2024**. https://doi.org/10.1186/s13045-024-01571-4 (xiao2024apracticalapproach pages 2-4)
* Gianelli U et al. *International Consensus Classification… myeloproliferative neoplasms*. **Dec 2023**. https://doi.org/10.1007/s00428-022-03480-8 (gianelli2023internationalconsensusclassification pages 14-15, gianelli2023internationalconsensusclassification pages 13-14)
* McLornan DP et al. *How I manage myeloproliferative neoplasm-unclassifiable: Practical approaches for 2022 and beyond*. **Feb 2022**. https://doi.org/10.1111/bjh.18087 (mclornan2022howimanage pages 1-2, mclornan2022howimanage pages 4-5)
* Hargreaves R et al. *Diagnostic and management strategies for MPN-U: an international survey*. **Jul 2022**. https://doi.org/10.1016/j.retram.2022.103338 (hargreaves2022diagnosticandmanagement pages 6-7, hargreaves2022diagnosticandmanagement pages 3-6)
* Deschamps P et al. *Clinicopathological characterisation of MPN-U… UK tertiary referral centre*. **Mar 2021**. https://doi.org/10.1111/bjh.17375 (deschamps2021clinicopathologicalcharacterisationof pages 2-3)
* Pizzi M et al. *Classification of MPNs… focus on unclassifiable cases*. **Nov 2021**. https://doi.org/10.3390/cancers13225666 (pizzi2021theclassificationof pages 7-8)
* Pedersen KM et al. *Smoking is associated with increased risk of MPNs*. **Oct 2018**. https://doi.org/10.1002/cam4.1815 (pedersen2018smokingisassociated pages 1-2, pedersen2018smokingisassociated pages 2-3)
* Pedersen KM et al. *Two-fold risk of pneumonia and respiratory mortality in individuals with MPN*. **Apr 2020**. https://doi.org/10.1016/j.eclinm.2020.100295 (pedersen2020twofoldriskof pages 1-2)
* Landtblom AR et al. *Second malignancies in patients with MPNs… 9379 patients*. **Jan 2018**. https://doi.org/10.1038/s41375-018-0027-y (landtblom2018secondmalignanciesin pages 3-4)

PMIDs: Not available in the retrieved excerpts for the above sources in this run; therefore PMID numbers cannot be reliably provided from the current evidence context.

References

1. (mclornan2022howimanage pages 1-1): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

2. (mclornan2022howimanage pages 1-2): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

3. (xiao2024apracticalapproach pages 2-4): Wenbin Xiao, Valentina Nardi, Eytan Stein, and Robert P. Hasserjian. A practical approach on the classifications of myeloid neoplasms and acute leukemia: who and icc. Journal of Hematology & Oncology, Jul 2024. URL: https://doi.org/10.1186/s13045-024-01571-4, doi:10.1186/s13045-024-01571-4. This article has 40 citations and is from a domain leading peer-reviewed journal.

4. (hargreaves2022diagnosticandmanagement pages 1-2): Rupen Hargreaves, Claire N Harrison, and Donal P McLornan. Diagnostic and management strategies for myeloproliferative neoplasm-unclassifiable (mpn-u): an international survey of contemporary practice. Current Research in Translational Medicine, 70:103338, Jul 2022. URL: https://doi.org/10.1016/j.retram.2022.103338, doi:10.1016/j.retram.2022.103338. This article has 6 citations and is from a peer-reviewed journal.

5. (deschamps2021clinicopathologicalcharacterisationof pages 1-2): Paul Deschamps, Mufaddal Moonim, Deepti Radia, Natalia Curto‐Garcia, Claire Woodley, Sarah Bassiony, Jennifer O'Sullivan, Patrick Harrington, Kavita Raj, Yvonne Francis, Shahram Kordasti, Sahra Ali, Claire N. Harrison, and Donal P. McLornan. Clinicopathological characterisation of myeloproliferative neoplasm‐unclassifiable (mpn‐u): a retrospective analysis from a large uk tertiary referral centre. British Journal of Haematology, 193:792-797, Mar 2021. URL: https://doi.org/10.1111/bjh.17375, doi:10.1111/bjh.17375. This article has 19 citations and is from a domain leading peer-reviewed journal.

6. (pizzi2021theclassificationof pages 7-8): Marco Pizzi, Giorgio Alberto Croci, Marco Ruggeri, Silvia Tabano, Angelo Paolo Dei Tos, Elena Sabattini, and Umberto Gianelli. The classification of myeloproliferative neoplasms: rationale, historical background and future perspectives with focus on unclassifiable cases. Cancers, 13:5666, Nov 2021. URL: https://doi.org/10.3390/cancers13225666, doi:10.3390/cancers13225666. This article has 46 citations.

7. (mclornan2022howimanage pages 2-2): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

8. (gianelli2023internationalconsensusclassification pages 13-14): Umberto Gianelli, Jürgen Thiele, Attilio Orazi, Naseema Gangat, Alessandro M. Vannucchi, Ayalew Tefferi, and Hans Michael Kvasnicka. International consensus classification of myeloid and lymphoid neoplasms: myeloproliferative neoplasms. Virchows Archiv, 482:53-68, Dec 2023. URL: https://doi.org/10.1007/s00428-022-03480-8, doi:10.1007/s00428-022-03480-8. This article has 61 citations and is from a peer-reviewed journal.

9. (deschamps2021clinicopathologicalcharacterisationof pages 2-3): Paul Deschamps, Mufaddal Moonim, Deepti Radia, Natalia Curto‐Garcia, Claire Woodley, Sarah Bassiony, Jennifer O'Sullivan, Patrick Harrington, Kavita Raj, Yvonne Francis, Shahram Kordasti, Sahra Ali, Claire N. Harrison, and Donal P. McLornan. Clinicopathological characterisation of myeloproliferative neoplasm‐unclassifiable (mpn‐u): a retrospective analysis from a large uk tertiary referral centre. British Journal of Haematology, 193:792-797, Mar 2021. URL: https://doi.org/10.1111/bjh.17375, doi:10.1111/bjh.17375. This article has 19 citations and is from a domain leading peer-reviewed journal.

10. (deschamps2021clinicopathologicalcharacterisationof pages 5-6): Paul Deschamps, Mufaddal Moonim, Deepti Radia, Natalia Curto‐Garcia, Claire Woodley, Sarah Bassiony, Jennifer O'Sullivan, Patrick Harrington, Kavita Raj, Yvonne Francis, Shahram Kordasti, Sahra Ali, Claire N. Harrison, and Donal P. McLornan. Clinicopathological characterisation of myeloproliferative neoplasm‐unclassifiable (mpn‐u): a retrospective analysis from a large uk tertiary referral centre. British Journal of Haematology, 193:792-797, Mar 2021. URL: https://doi.org/10.1111/bjh.17375, doi:10.1111/bjh.17375. This article has 19 citations and is from a domain leading peer-reviewed journal.

11. (deschamps2021clinicopathologicalcharacterisationof media cb1fee4a): Paul Deschamps, Mufaddal Moonim, Deepti Radia, Natalia Curto‐Garcia, Claire Woodley, Sarah Bassiony, Jennifer O'Sullivan, Patrick Harrington, Kavita Raj, Yvonne Francis, Shahram Kordasti, Sahra Ali, Claire N. Harrison, and Donal P. McLornan. Clinicopathological characterisation of myeloproliferative neoplasm‐unclassifiable (mpn‐u): a retrospective analysis from a large uk tertiary referral centre. British Journal of Haematology, 193:792-797, Mar 2021. URL: https://doi.org/10.1111/bjh.17375, doi:10.1111/bjh.17375. This article has 19 citations and is from a domain leading peer-reviewed journal.

12. (hargreaves2022diagnosticandmanagement pages 6-7): Rupen Hargreaves, Claire N Harrison, and Donal P McLornan. Diagnostic and management strategies for myeloproliferative neoplasm-unclassifiable (mpn-u): an international survey of contemporary practice. Current Research in Translational Medicine, 70:103338, Jul 2022. URL: https://doi.org/10.1016/j.retram.2022.103338, doi:10.1016/j.retram.2022.103338. This article has 6 citations and is from a peer-reviewed journal.

13. (hargreaves2022diagnosticandmanagement pages 3-6): Rupen Hargreaves, Claire N Harrison, and Donal P McLornan. Diagnostic and management strategies for myeloproliferative neoplasm-unclassifiable (mpn-u): an international survey of contemporary practice. Current Research in Translational Medicine, 70:103338, Jul 2022. URL: https://doi.org/10.1016/j.retram.2022.103338, doi:10.1016/j.retram.2022.103338. This article has 6 citations and is from a peer-reviewed journal.

14. (mclornan2022howimanage pages 4-5): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

15. (mclornan2022howimanage pages 7-7): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

16. (mclornan2022howimanage pages 8-9): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

17. (deschamps2021clinicopathologicalcharacterisationof pages 3-5): Paul Deschamps, Mufaddal Moonim, Deepti Radia, Natalia Curto‐Garcia, Claire Woodley, Sarah Bassiony, Jennifer O'Sullivan, Patrick Harrington, Kavita Raj, Yvonne Francis, Shahram Kordasti, Sahra Ali, Claire N. Harrison, and Donal P. McLornan. Clinicopathological characterisation of myeloproliferative neoplasm‐unclassifiable (mpn‐u): a retrospective analysis from a large uk tertiary referral centre. British Journal of Haematology, 193:792-797, Mar 2021. URL: https://doi.org/10.1111/bjh.17375, doi:10.1111/bjh.17375. This article has 19 citations and is from a domain leading peer-reviewed journal.

18. (mclornan2022howimanage pages 5-6): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

19. (mclornan2022howimanage pages 6-7): Donal P. McLornan, Rupen Hargreaves, Juan Carlos Hernández‐Boluda, and Claire N. Harrison. How i manage myeloproliferative neoplasm‐unclassifiable: practical approaches for 2022 and beyond. British Journal of Haematology, 197:407-416, Feb 2022. URL: https://doi.org/10.1111/bjh.18087, doi:10.1111/bjh.18087. This article has 11 citations and is from a domain leading peer-reviewed journal.

20. (deschamps2021clinicopathologicalcharacterisationof media 1f80ac50): Paul Deschamps, Mufaddal Moonim, Deepti Radia, Natalia Curto‐Garcia, Claire Woodley, Sarah Bassiony, Jennifer O'Sullivan, Patrick Harrington, Kavita Raj, Yvonne Francis, Shahram Kordasti, Sahra Ali, Claire N. Harrison, and Donal P. McLornan. Clinicopathological characterisation of myeloproliferative neoplasm‐unclassifiable (mpn‐u): a retrospective analysis from a large uk tertiary referral centre. British Journal of Haematology, 193:792-797, Mar 2021. URL: https://doi.org/10.1111/bjh.17375, doi:10.1111/bjh.17375. This article has 19 citations and is from a domain leading peer-reviewed journal.

21. (pedersen2018smokingisassociated pages 2-3): Kasper M. Pedersen, Marie Bak, Anders L. Sørensen, Ann‐Dorthe Zwisler, Christina Ellervik, Morten K. Larsen, Hans C. Hasselbalch, and Janne S. Tolstrup. Smoking is associated with increased risk of myeloproliferative neoplasms: a general population‐based cohort study. Cancer Medicine, 7:5796-5802, Oct 2018. URL: https://doi.org/10.1002/cam4.1815, doi:10.1002/cam4.1815. This article has 47 citations and is from a peer-reviewed journal.

22. (landtblom2018secondmalignanciesin pages 3-4): Anna Ravn Landtblom, Hannah Bower, Therese M.-L. Andersson, Paul W. Dickman, Jan Samuelsson, Magnus Björkholm, Sigurdur Yngvi Kristinsson, and Malin Hultcrantz. Second malignancies in patients with myeloproliferative neoplasms: a population-based cohort study of 9379 patients. Leukemia, 32:2203-2210, Jan 2018. URL: https://doi.org/10.1038/s41375-018-0027-y, doi:10.1038/s41375-018-0027-y. This article has 107 citations and is from a highest quality peer-reviewed journal.

23. (pedersen2020twofoldriskof pages 1-2): Kasper Mønsted Pedersen, Yunus Çolak, Hans Carl Hasselbalch, Christina Ellervik, Børge Grønne Nordestgaard, and Stig Egil Bojesen. Two-fold risk of pneumonia and respiratory mortality in individuals with myeloproliferative neoplasm: a population-based cohort study. EClinicalMedicine, 21:100295, Apr 2020. URL: https://doi.org/10.1016/j.eclinm.2020.100295, doi:10.1016/j.eclinm.2020.100295. This article has 9 citations and is from a peer-reviewed journal.

24. (pedersen2018smokingisassociated pages 1-2): Kasper M. Pedersen, Marie Bak, Anders L. Sørensen, Ann‐Dorthe Zwisler, Christina Ellervik, Morten K. Larsen, Hans C. Hasselbalch, and Janne S. Tolstrup. Smoking is associated with increased risk of myeloproliferative neoplasms: a general population‐based cohort study. Cancer Medicine, 7:5796-5802, Oct 2018. URL: https://doi.org/10.1002/cam4.1815, doi:10.1002/cam4.1815. This article has 47 citations and is from a peer-reviewed journal.

25. (pedersen2018smokingisassociated pages 5-6): Kasper M. Pedersen, Marie Bak, Anders L. Sørensen, Ann‐Dorthe Zwisler, Christina Ellervik, Morten K. Larsen, Hans C. Hasselbalch, and Janne S. Tolstrup. Smoking is associated with increased risk of myeloproliferative neoplasms: a general population‐based cohort study. Cancer Medicine, 7:5796-5802, Oct 2018. URL: https://doi.org/10.1002/cam4.1815, doi:10.1002/cam4.1815. This article has 47 citations and is from a peer-reviewed journal.

26. (gianelli2023internationalconsensusclassification pages 11-13): Umberto Gianelli, Jürgen Thiele, Attilio Orazi, Naseema Gangat, Alessandro M. Vannucchi, Ayalew Tefferi, and Hans Michael Kvasnicka. International consensus classification of myeloid and lymphoid neoplasms: myeloproliferative neoplasms. Virchows Archiv, 482:53-68, Dec 2023. URL: https://doi.org/10.1007/s00428-022-03480-8, doi:10.1007/s00428-022-03480-8. This article has 61 citations and is from a peer-reviewed journal.

27. (gianelli2023internationalconsensusclassification pages 14-15): Umberto Gianelli, Jürgen Thiele, Attilio Orazi, Naseema Gangat, Alessandro M. Vannucchi, Ayalew Tefferi, and Hans Michael Kvasnicka. International consensus classification of myeloid and lymphoid neoplasms: myeloproliferative neoplasms. Virchows Archiv, 482:53-68, Dec 2023. URL: https://doi.org/10.1007/s00428-022-03480-8, doi:10.1007/s00428-022-03480-8. This article has 61 citations and is from a peer-reviewed journal.