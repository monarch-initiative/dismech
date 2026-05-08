---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:54:25.372727'
end_time: '2026-05-08T13:04:58.626528'
duration_seconds: 633.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dieulafoy Lesion
  mondo_id: ''
  category: Acquired
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dieulafoy Lesion
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Dieulafoy Lesion** covering all of the
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
- **Disease Name:** Dieulafoy Lesion
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Dieulafoy Lesion** covering all of the
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


# Disease Characteristics Research Report: Dieulafoy Lesion (Acquired)

## Executive summary
Dieulafoy lesion (DL) is a rare but high-impact cause of acute gastrointestinal (GI) hemorrhage due to a persistent-caliber submucosal artery that erodes through a minute mucosal defect without primary ulceration. DL is most often gastric (especially on the lesser curvature near the gastroesophageal junction), frequently causes severe intermittent arterial bleeding, and can be difficult to diagnose on index endoscopy (diagnostic yield ~70%), often necessitating repeat endoscopy or adjunct localization modalities. Modern endoscopic hemostasis achieves primary hemostasis in ~88–90% of cases, and mortality has declined to ~9–13% compared with ~30% in the pre-endoscopic era. Recent (2023–2024) literature emphasizes multidisciplinary escalation pathways and adoption of newer hemostasis tools (e.g., over-the-scope/cap-mounted clips, Doppler guidance, and topical hemostatic agents) for high-risk non-variceal upper GI bleeding contexts that include DL. (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7)

## 1. Disease information

### 1.1 Overview (current understanding)
DL is characterized by an aberrant, dilated submucosal artery that **maintains a large caliber despite its peripheral location** and becomes exposed through a **tiny mucosal defect with otherwise minimal mucosal abnormality**, leading to potentially massive bleeding. A key clinical teaching point is that the lesion may look like a **“visible vessel sans ulcer”** at endoscopy. (nojkov2015gastrointestinalbleedingfrom pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 3-4)

**Direct abstract quote (Nojkov & Cappell, 2015):** “Unlike normal vessels of the gastrointestinal tract which become progressively smaller in caliber peripherally, Dieulafoy’s lesions maintain a large caliber despite their peripheral, submucosal, location within gastrointestinal wall.” (nojkov2015gastrointestinalbleedingfrom pages 1-2)

### 1.2 Key identifiers
* **MONDO ID:** Not identified in the retrieved full-text evidence set.
* **MeSH / ICD-10 / ICD-11 / Orphanet / OMIM:** Not identified in the retrieved full-text evidence set.

> Note: This report is grounded primarily in peer-reviewed reviews and case-based clinical literature rather than structured ontology resources. (nojkov2015gastrointestinalbleedingfrom pages 1-2, inayat2022rectaldieulafoy’slesion pages 1-2)

### 1.3 Synonyms and alternative names
* **Exulceratio simplex** (historical terminology). (falt2023recurrentbleedingin pages 2-2, inayat2022rectaldieulafoy’slesion pages 1-2)
* **“Miliary aneurysms of the stomach”** (historical descriptor). (inayat2022rectaldieulafoy’slesion pages 1-2)

### 1.4 Evidence provenance
Information summarized here is derived from **aggregated disease-level evidence** (systematic/comparative reviews and large case-based syntheses) and **individual case reports** that illustrate diagnostic challenges and escalation pathways. (nojkov2015gastrointestinalbleedingfrom pages 1-2, inayat2022rectaldieulafoy’slesion pages 1-2, kusnik2023dieulafoylesionscope pages 1-2)

## 2. Etiology

### 2.1 Disease causal factors
DL is primarily an **anatomic vascular abnormality**: a caliber-persistent (dilated) submucosal artery that becomes superficially exposed and bleeds without a primary ulcer crater. (nojkov2015gastrointestinalbleedingfrom pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3)

For rectal DL, proposed contributors include **mechanical/erosional mucosal injury and mucosal atrophy**, particularly in the setting of constipation or local tissue changes. (inayat2022rectaldieulafoy’slesion pages 4-6)

### 2.2 Risk factors
Large-scale, universally accepted causal risk factors are not clearly established in the retrieved evidence; however, multiple sources describe **clinical associations and precipitating contexts**:
* **Older age** and **male predominance (~2:1)** in many series. (nojkov2015gastrointestinalbleedingfrom pages 2-3)
* **Antithrombotic/NSAID exposure** is frequently present in case-based literature and may precipitate clinically apparent bleeding. (kusnik2023dieulafoylesionscope pages 1-2, inayat2022rectaldieulafoy’slesion pages 4-6, nojkov2015gastrointestinalbleedingfrom pages 2-3)
* In rectal DL specifically, common comorbidities in a pooled case review (n=101) included **hypertension (29%)**, **diabetes (21%)**, **chronic kidney disease (16%)**, along with other comorbidities variably reported (e.g., cancer, ischemic heart disease). (inayat2022rectaldieulafoy’slesion pages 1-2, inayat2022rectaldieulafoy’slesion pages 4-6)

### 2.3 Protective factors
No protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No gene–environment interaction data were identified in the retrieved evidence set.

## 3. Phenotypes (clinical presentation)

### 3.1 Core phenotypes and frequencies
DL most commonly presents as **acute overt GI bleeding** that can be severe and intermittent.

Upper-GI presentation frequencies from a 177-case review summarized by Nojkov & Cappell (2015):
* **Hematemesis + melena:** 51%
* **Hematemesis alone:** 28%
* **Melena alone:** 18% (nojkov2015gastrointestinalbleedingfrom pages 3-4)

Rectal DL presentation (pooled 101 cases):
* **Bright red blood per rectum:** 47%
* **Hematochezia:** 36%
* **Painless rectal bleeding:** 11%
* **Melena:** 4% (inayat2022rectaldieulafoy’slesion pages 4-6, inayat2022rectaldieulafoy’slesion pages 1-2)

Clinical severity is highlighted by frequent **hemodynamic instability** and **transfusion requirement**. (nojkov2015gastrointestinalbleedingfrom pages 1-2)

### 3.2 Candidate HPO term suggestions (not exhaustive)
* Hematemesis — **HP:0002130** (candidate)
* Melena — **HP:0002249** (candidate)
* Hematochezia — **HP:0002247** (candidate)
* Gastrointestinal hemorrhage — **HP:0002239** (candidate)
* Syncope — **HP:0001279** (candidate; reported in clinical descriptions/cases) (inayat2022rectaldieulafoy’slesion pages 4-6)
* Hemorrhagic shock — **HP:0030140** (candidate; consistent with severe presentation) (nojkov2015gastrointestinalbleedingfrom pages 1-2)
* Anemia / iron deficiency anemia — **HP:0001903 / HP:0001899** (candidates) (shumilina2024duodenaldieulafoylesion pages 6-7, inayat2022rectaldieulafoy’slesion pages 4-6)

### 3.3 Quality-of-life impact
Quality-of-life impacts were not quantified using standardized instruments in the retrieved evidence; however, the condition can cause abrupt life-threatening bleeding requiring ICU-level care and transfusion, implying major acute functional impact. (nojkov2015gastrointestinalbleedingfrom pages 1-2, kusnik2023dieulafoylesionscope pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes / variants
No causal genes, pathogenic variants, or inherited patterns were identified in the retrieved evidence. DL is generally treated as an **acquired/anatomic vascular lesion** rather than a monogenic disorder in the referenced GI literature. (nojkov2015gastrointestinalbleedingfrom pages 2-3)

### 4.2 Epigenetics / modifiers
No relevant evidence identified.

## 5. Environmental information
No specific toxins, infectious triggers, or environmental exposures were established as causal in the retrieved evidence. Medication exposure (NSAIDs/antithrombotics) is repeatedly noted as a contextual factor for presentation/bleeding. (kusnik2023dieulafoylesionscope pages 1-2, inayat2022rectaldieulafoy’slesion pages 4-6)

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (conceptual)
1. **Upstream anatomic substrate:** A **large-caliber submucosal artery** persists (fails to narrow) as it approaches the mucosa. (nojkov2015gastrointestinalbleedingfrom pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3)
2. **Local mucosal failure:** A **minute mucosal defect** develops without primary ulceration; the vessel becomes exposed (“visible vessel sans ulcer”) and may thrombose intermittently. (nojkov2015gastrointestinalbleedingfrom pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 3-4)
3. **Clinical manifestation:** Vessel rupture/erosion produces **intermittent, potentially massive arterial GI bleeding**, leading to anemia, hemodynamic instability, and recurrent hemorrhage if not definitively treated. (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7)

Mechanistic contributors proposed in reviewed sources include **mechanical trauma/pulsation** and, for rectal lesions, **stercoral injury/constipation-related mucosal damage** and degenerative tissue changes. (inayat2022rectaldieulafoy’slesion pages 4-6, al‐bawardy2022gastrointestinalvascularmalformations pages 2-3)

### 6.2 Candidate GO biological process terms (proposed)
* Blood vessel morphogenesis — **GO:0048514** (candidate)
* Hemostasis — **GO:0007599** (candidate)
* Blood coagulation — **GO:0007596** (candidate)
* Response to wounding — **GO:0009611** (candidate)

### 6.3 Candidate CL cell types (proposed)
* Endothelial cell — **CL:0000115** (candidate)
* Vascular smooth muscle cell — **CL:0000192** (candidate)

### 6.4 Molecular profiling / omics
No transcriptomic/proteomic/metabolomic profiling evidence was identified.

## 7. Anatomical structures affected

### 7.1 Organ-level distribution
* Predominantly **stomach** (~70–75% in major reviews; some sources cite 80–95%), especially along the **lesser curvature within ~6 cm of the gastroesophageal junction**. (nojkov2015gastrointestinalbleedingfrom pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3, ather2024dieulafoyslesionsomething pages 1-3)
* Extragastric lesions reported in duodenum, esophagus, jejunoileum, and colorectum. (inayat2022rectaldieulafoy’slesion pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3)

### 7.2 Candidate UBERON terms (proposed)
* Stomach — **UBERON:0000945** (candidate)
* Duodenum — **UBERON:0002114** (candidate)
* Jejunum — **UBERON:0002115** (candidate)
* Ileum — **UBERON:0002116** (candidate)
* Colon — **UBERON:0001155** (candidate)
* Rectum — **UBERON:0001052** (candidate)

## 8. Temporal development

### 8.1 Onset
Often **sudden/acute** presentation with overt bleeding and no prodromal symptoms. (nojkov2015gastrointestinalbleedingfrom pages 1-2)

### 8.2 Progression/course
Bleeding can be **intermittent and recurrent**, and without prompt treatment, early recurrence (within **~72 hours**) is highlighted as common in reviews of NVUGIB due to DL. (martino2023rarecausesof pages 6-7)

## 9. Inheritance and population

### 9.1 Epidemiology (statistics)
* DL accounts for **~1–2% of acute GI bleeding** in multiple clinical reviews/case-based sources. (kusnik2023dieulafoylesionscope pages 1-2, ather2024dieulafoyslesionsomething pages 1-3)
* A major review estimates **~1.5% of acute upper GI bleeding** attributable to DL. (nojkov2015gastrointestinalbleedingfrom pages 3-4)
* Anatomic distribution estimates in reviews: duodenum **~15%**, esophagus **~8%**, colon **~2%**, jejunoileal **<1%**, with extragastric lesions **<35%** overall in one synthesis. (inayat2022rectaldieulafoy’slesion pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3)

### 9.2 Demographics
Male predominance (~2:1) and typical presentation in the sixth–seventh decade are reported, though DL can occur at any age. (nojkov2015gastrointestinalbleedingfrom pages 2-3)

## 10. Diagnostics

### 10.1 Clinical/endoscopic diagnosis
Endoscopy is the primary diagnostic modality, but index diagnostic yield is imperfect:
* **Endoscopic diagnostic yield ~70%** (i.e., nondiagnostic in up to ~30%). (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7)

**Endoscopic diagnostic criteria** (as summarized in recent review literature):
* Active arterial spurting/oozing from a minute mucosal defect (<3 mm) or through normal mucosa
* Protruding visible vessel with/without bleeding
* Fresh adherent clot attached to a tiny mucosal defect on otherwise normal mucosa (martino2023rarecausesof pages 6-7, shumilina2024duodenaldieulafoylesion pages 6-7)

### 10.2 Adjunct localization modalities (real-world implementation)
When endoscopy is nondiagnostic (often due to intermittent bleeding, small lesion size, or clot/blood obscuring the field), escalation may include:
* **CTA and angiography/embolization** (especially with active bleeding)
* **Capsule endoscopy / push enteroscopy** for suspected small-bowel lesions
* **EUS and/or Doppler (endoscopic Doppler ultrasound) guidance** as adjuncts discussed in contemporary NVUGIB hemostasis reviews (ather2024dieulafoyslesionsomething pages 1-3, martino2023rarecausesof pages 6-7)

A representative recent small-bowel case illustrates this escalation: initial EGD/colonoscopy negative, CTA localized active jejunal branch bleeding leading to coil embolization; persistent bleeding prompted capsule endoscopy and eventually surgical resection with histologic confirmation. (ather2024dieulafoyslesionsomething pages 1-3)

### 10.3 Differential diagnosis (high-level)
Although detailed differential diagnosis lists were not exhaustively enumerated in retrieved evidence, practical differentials in NVUGIB/LGIB evaluations include peptic ulcer bleeding, angiodysplasia/vascular ectasias, Mallory–Weiss tears, neoplasms, and variceal bleeding—conditions commonly contrasted with “rare causes” such as DL in NVUGIB reviews. (martino2023rarecausesof pages 6-7)

## 11. Outcome / prognosis

### 11.1 Mortality and prognosis
With modern endoscopic therapy, mortality is reported at **~9–13%**, down from ~30% historically. (nojkov2015gastrointestinalbleedingfrom pages 1-2)

### 11.2 Complications
The principal complication is **recurrent hemorrhage**, which may occur within **~72 hours** if inadequately treated or missed. (martino2023rarecausesof pages 6-7)

## 12. Treatment

### 12.1 First-line therapy (endoscopic)
Endoscopic therapy is recommended as initial management and includes:
* **Mechanical:** through-the-scope hemoclips, band ligation, over-the-scope clips (OTSC)
* **Injection:** epinephrine and/or sclerotherapy
* **Thermal/ablative:** argon plasma coagulation, thermocoagulation/electrocoagulation

A key management principle is **dual therapy** (e.g., epinephrine injection followed by mechanical/thermal therapy), reported to be effective in **>90%** in review summaries, with primary hemostasis “nearly 90%” overall in a major review. (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7)

**Direct abstract quote (Nojkov & Cappell, 2015):** “Endoscopic therapy… is the recommended initial therapy, with primary hemostasis achieved in nearly 90% of cases.” (nojkov2015gastrointestinalbleedingfrom pages 1-2)

Rectal DL review (n=101 cases) reported **primary endoscopic hemostasis 88%** and overall mortality 6% (deaths unrelated to DL per authors). (inayat2022rectaldieulafoy’slesion pages 1-2)

### 12.2 Rescue therapy
If endoscopic therapy fails or the lesion is inaccessible:
* **Repeat endoscopic therapy**
* **Angiography ± transcatheter arterial embolization (TAE)**
* **Surgery (e.g., wedge resection/segmental resection)** as a last resort (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7)

### 12.3 Recent developments and latest research (prioritizing 2023–2024)
Recent (2023–2024) review literature in NVUGIB highlights several technology trends relevant to DL management:
* **Cap-mounted/over-the-scope mechanical hemostasis devices** and other “novel endoscopic treatments” discussed as reducing rebleeding risk in NVUGIB, including contexts such as DL. (martino2023rarecausesof pages 6-7)
* **Doppler ultrasound–guided hemostasis assessment** and **endoscopic ultrasound** as adjuncts for diagnosis and for confirming vessel ablation/ongoing arterial flow in complex bleeding lesions. (martino2023rarecausesof pages 6-7)
* **Topical hemostatic agents:** A 2024 systematic review of self-assembling peptides across GI bleeding studies reported an overall success rate **87.7%** and mean rebleeding **4.7%** (range 0–16.2%), supporting their broader role as endoscopic hemostasis adjuncts (not DL-specific). (martino2023rarecausesof pages 6-7)

### 12.4 MAXO term suggestions (proposed)
* Endoscopic hemostasis — **MAXO:0000809** (candidate)
* Endoscopic clip placement — (candidate)
* Endoscopic band ligation — (candidate)
* Transcatheter arterial embolization — (candidate)
* Surgical resection — (candidate)

## 13. Prevention
No primary prevention strategies are established, as DL is an anatomic vascular abnormality. Practical prevention is largely **secondary/tertiary**, focusing on:
* Rapid recognition and urgent endoscopy in acute GI bleeding
* Repeat endoscopy when index exam is negative (intermittent bleeding; ~70% diagnostic yield)
* Medication review in high-risk bleeding contexts (anticoagulants/NSAIDs) (nojkov2015gastrointestinalbleedingfrom pages 1-2, kusnik2023dieulafoylesionscope pages 1-2)

## 14. Other species / natural disease
No evidence of naturally occurring DL in non-human species was identified in the retrieved evidence set.

## 15. Model organisms
No model organism systems were identified in the retrieved evidence set.

## Visual evidence
Endoscopic appearance of an oozing Dieulafoy lesion and post-hemoclip hemostasis, plus a management options table, are shown in the retrieved figure/table regions from Nojkov & Cappell (2015). (nojkov2015gastrointestinalbleedingfrom media ebf94cbf, nojkov2015gastrointestinalbleedingfrom media 528ec365)

## Key facts table
| Finding | Quantitative data | Source (year, DOI/PMID, URL) |
|---|---:|---|
| Definition / pathology | Aberrant dilated submucosal artery that fails to narrow peripherally; caliber ~1–3 mm, up to ~10× normal submucosal vessels; erodes overlying mucosa with minimal surrounding erosion and no primary ulceration | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295 (nojkov2015gastrointestinalbleedingfrom pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3) |
| Share of GI bleeding | ~1%–2% of all acute GI bleeding; ~1.5% of acute upper GI bleeding | Kusnik et al. 2023, DOI: 10.7759/cureus.36097, URL: https://doi.org/10.7759/cureus.36097; Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295 (kusnik2023dieulafoylesionscope pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 3-4) |
| Mortality | Current mortality ~9%–13%; down from ~30% in the 1970s with modern endoscopic therapy | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295; Ather & Mwengela 2024, URL not clearly available in evidence excerpt (nojkov2015gastrointestinalbleedingfrom pages 1-2, ather2024dieulafoyslesionsomething pages 1-3) |
| Typical location: stomach | ~70%–75% gastric overall; 80%–95% reported in stomach in some reviews; strong predilection for lesser curvature within 6 cm of gastroesophageal junction | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295; Ather & Mwengela 2024 (nojkov2015gastrointestinalbleedingfrom pages 1-2, ather2024dieulafoyslesionsomething pages 1-3) |
| Typical location: extragastric distribution | Duodenum ~15%; esophagus ~8%; colon ~2%; jejunoileal <1%; extragastric lesions <35% overall | Inayat et al. 2022, DOI: 10.21037/tgh.2020.02.17, URL: https://doi.org/10.21037/tgh.2020.02.17; Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295 (inayat2022rectaldieulafoy’slesion pages 1-2, nojkov2015gastrointestinalbleedingfrom pages 2-3) |
| Sex / age pattern | Male predominance about 2:1; most often presents in 6th–7th decades, but can occur at any age | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295 (nojkov2015gastrointestinalbleedingfrom pages 2-3) |
| Clinical presentation frequencies (upper GI reviews) | In 177-case review: hematemesis + melena 51%, hematemesis alone 28%, melena alone 18% | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295 (nojkov2015gastrointestinalbleedingfrom pages 3-4) |
| Clinical presentation frequencies (rectal lesions) | Bright-red blood per rectum 47%, hematochezia 36%, painless rectal bleeding 11%, melena 4% | Inayat et al. 2022, DOI: 10.21037/tgh.2020.02.17, URL: https://doi.org/10.21037/tgh.2020.02.17 (inayat2022rectaldieulafoy’slesion pages 4-6, inayat2022rectaldieulafoy’slesion pages 1-2) |
| Diagnostic yield of initial endoscopy | Initial endoscopic diagnostic yield ~70%; about half identified on first endoscopy and ~33% require additional endoscopy in one review | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295; Ather & Mwengela 2024 (nojkov2015gastrointestinalbleedingfrom pages 1-2, ather2024dieulafoyslesionsomething pages 1-3) |
| Endoscopic diagnostic criteria | Active arterial spurting/oozing from a minute mucosal defect (<3 mm) or through normal mucosa; protruding visible vessel with or without bleeding; fresh adherent clot attached to a tiny mucosal defect on otherwise normal mucosa | Martino et al. 2023, DOI: 10.3748/wjg.v29.i27.4222, URL: https://doi.org/10.3748/wjg.v29.i27.4222; Shumilina et al. 2024, DOI: 10.32345/usmyj.2(146).2024.53-59, URL: https://doi.org/10.32345/usmyj.2(146).2024.53-59 (martino2023rarecausesof pages 6-7, shumilina2024duodenaldieulafoylesion pages 6-7) |
| Endoscopic appearance | Typical lesion ~10–15 mm wide, ~5–10 mm high, with 1–5 mm point source; actively bleeding at index EGD in ~50%–60%; one series: oozing 66%, spurting 28% | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295 (nojkov2015gastrointestinalbleedingfrom pages 3-4) |
| Adjunct diagnostics | CTA/angiography, capsule endoscopy, push enteroscopy, Doppler probe/EUS used when standard endoscopy is nondiagnostic; no single pooled accuracy estimate provided in retrieved evidence | Tripathi et al. 2024, DOI: 10.1186/s40792-024-02064-9, URL: https://doi.org/10.1186/s40792-024-02064-9; Martino et al. 2023, DOI: 10.3748/wjg.v29.i27.4222, URL: https://doi.org/10.3748/wjg.v29.i27.4222; Ather & Mwengela 2024 (ather2024dieulafoyslesionsomething pages 1-3, martino2023rarecausesof pages 6-7) |
| Main first-line treatments | Endoscopic therapy is first line: mechanical (hemoclips, band ligation, OTSC), injection (epinephrine/sclerosant), thermal (APC, electrocoagulation); combination/dual therapy preferred | Martino et al. 2023, DOI: 10.3748/wjg.v29.i27.4222, URL: https://doi.org/10.3748/wjg.v29.i27.4222; Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295; Li & Fung 2024, DOI: 10.4253/wjge.v16.i7.376, URL: https://doi.org/10.4253/wjge.v16.i7.376 (martino2023rarecausesof pages 6-7, nojkov2015gastrointestinalbleedingfrom pages 1-2) |
| Primary hemostasis after endoscopic therapy | Nearly 90% overall; rectal lesion review reported 88% primary hemostasis | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295; Inayat et al. 2022, DOI: 10.21037/tgh.2020.02.17, URL: https://doi.org/10.21037/tgh.2020.02.17 (nojkov2015gastrointestinalbleedingfrom pages 1-2, inayat2022rectaldieulafoy’slesion pages 1-2) |
| Rebleeding | Recurrent bleeding commonly occurs within 72 h if untreated; combined endoscopic therapy has lower rebleeding than monotherapy; self-assembling peptide hemostatic agents across GI bleeding studies showed mean rebleeding 4.7% (range 0%–16.2%), not specific to Dieulafoy lesions | Martino et al. 2023, DOI: 10.3748/wjg.v29.i27.4222, URL: https://doi.org/10.3748/wjg.v29.i27.4222; Voiosu et al. 2024, DOI: 10.5946/ce.2023.168, URL: https://doi.org/10.5946/ce.2023.168 (martino2023rarecausesof pages 6-7) |
| Rescue therapy when endoscopy fails | Transcatheter arterial embolization/angiography second line; surgery (e.g., wedge resection or segmental resection) reserved for refractory or inaccessible bleeding | Nojkov & Cappell 2015, DOI: 10.4253/wjge.v7.i4.295, URL: https://doi.org/10.4253/wjge.v7.i4.295; Martino et al. 2023, DOI: 10.3748/wjg.v29.i27.4222, URL: https://doi.org/10.3748/wjg.v29.i27.4222; Tripathi et al. 2024, DOI: 10.1186/s40792-024-02064-9, URL: https://doi.org/10.1186/s40792-024-02064-9 (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7, ather2024dieulafoyslesionsomething pages 1-3) |


*Table: This table condenses the most actionable, evidence-supported facts on Dieulafoy lesion, including pathology, distribution, presentation, diagnosis, and treatment outcomes. It is useful as a quick reference for a disease knowledge base or clinical summary.*

## Notes on evidence gaps and limitations
* Several highly relevant 2023–2024 cohort studies and meta-analyses were not obtainable in the current retrieval session (e.g., small-bowel double-balloon endoscopy series; disease-specific outcome comparisons; DL-specific sclerotherapy efficacy study). Therefore, the report relies on a combination of (i) foundational high-citation syntheses (2015), (ii) disease-site-specific systematic review (rectal DL, 2022), and (iii) 2023–2024 reviews/case-based evidence for recent technology direction. (nojkov2015gastrointestinalbleedingfrom pages 1-2, martino2023rarecausesof pages 6-7, inayat2022rectaldieulafoy’slesion pages 1-2)
* Ontology identifiers (MONDO/ICD/MeSH) were not present in the retrieved sources; these would typically be supplemented using ICD/MeSH/MONDO lookup resources outside this evidence corpus.

## References (URLs and publication dates where available in evidence)
* Nojkov B, Cappell MS. World J Gastrointest Endosc. 2015-04. “Gastrointestinal bleeding from Dieulafoy’s lesion…” DOI:10.4253/wjge.v7.i4.295. URL: https://doi.org/10.4253/wjge.v7.i4.295 (nojkov2015gastrointestinalbleedingfrom pages 1-2)
* Martino A, et al. World J Gastroenterol. 2023-07. DOI:10.3748/wjg.v29.i27.4222. URL: https://doi.org/10.3748/wjg.v29.i27.4222 (martino2023rarecausesof pages 6-7)
* Kusnik A, et al. Cureus. 2023-03-13. DOI:10.7759/cureus.36097. URL: https://doi.org/10.7759/cureus.36097 (kusnik2023dieulafoylesionscope pages 1-2)
* Inayat F, et al. Transl Gastroenterol Hepatol. 2022-01-25. DOI:10.21037/tgh.2020.02.17. URL: https://doi.org/10.21037/tgh.2020.02.17 (inayat2022rectaldieulafoy’slesion pages 1-2)
* Li XJ, Fung BM. World J Gastrointest Endosc. 2024-07. DOI:10.4253/wjge.v16.i7.376. URL: https://doi.org/10.4253/wjge.v16.i7.376 (martino2023rarecausesof pages 6-7)
* Voiosu A, et al. Clinical Endoscopy. 2024-07. DOI:10.5946/ce.2023.168. URL: https://doi.org/10.5946/ce.2023.168 (martino2023rarecausesof pages 6-7)
* Ather N, Mwengela D. Proceedings of UCLA Health. 2024-11-12. “Dieulafoy’s Lesion: Something Not to Be Forgotten.” (ather2024dieulafoyslesionsomething pages 1-3)


References

1. (nojkov2015gastrointestinalbleedingfrom pages 1-2): Borko Nojkov and Mitchell S Cappell. Gastrointestinal bleeding from dieulafoy's lesion: clinical presentation, endoscopic findings, and endoscopic therapy. World journal of gastrointestinal endoscopy, 7 4:295-307, Apr 2015. URL: https://doi.org/10.4253/wjge.v7.i4.295, doi:10.4253/wjge.v7.i4.295. This article has 190 citations.

2. (martino2023rarecausesof pages 6-7): Alberto Martino, Marco Di Serafino, Luigi Orsini, Francesco Giurazza, Roberto Fiorentino, Enrico Crolla, Severo Campione, Carlo Molino, Luigia Romano, and Giovanni Lombardi. Rare causes of acute non-variceal upper gastrointestinal bleeding: a comprehensive review. World Journal of Gastroenterology, 29:4222-4235, Jul 2023. URL: https://doi.org/10.3748/wjg.v29.i27.4222, doi:10.3748/wjg.v29.i27.4222. This article has 23 citations.

3. (nojkov2015gastrointestinalbleedingfrom pages 3-4): Borko Nojkov and Mitchell S Cappell. Gastrointestinal bleeding from dieulafoy's lesion: clinical presentation, endoscopic findings, and endoscopic therapy. World journal of gastrointestinal endoscopy, 7 4:295-307, Apr 2015. URL: https://doi.org/10.4253/wjge.v7.i4.295, doi:10.4253/wjge.v7.i4.295. This article has 190 citations.

4. (inayat2022rectaldieulafoy’slesion pages 1-2): Faisal Inayat, Amna Hussain, Sidra Yahya, Simcha Weissman, Nuraiz Sarfraz, Muhammad Salman Faisal, Iqra Riaz, Saad Saleem, and Muhammad Wasif Saif. Rectal dieulafoy’s lesion: a comprehensive review of patient characteristics, presentation patterns, diagnosis, management, and clinical outcomes. Translational Gastroenterology and Hepatology, 7:10-10, Jan 2022. URL: https://doi.org/10.21037/tgh.2020.02.17, doi:10.21037/tgh.2020.02.17. This article has 23 citations and is from a peer-reviewed journal.

5. (falt2023recurrentbleedingin pages 2-2): Premysl Falt and Lumir Kunovsky. Recurrent bleeding in a patient with hepaticojejunostomy caused by dieulafoy's lesion. United European Gastroenterology Journal, 11:904-905, Jul 2023. URL: https://doi.org/10.1002/ueg2.12440, doi:10.1002/ueg2.12440. This article has 1 citations and is from a peer-reviewed journal.

6. (kusnik2023dieulafoylesionscope pages 1-2): Alexander Kusnik, Mostafa Reda Mostafa, Rutwik Pradeep Sharma, and Ari Chodos. Dieulafoy lesion: scope it until you find it. Cureus, Mar 2023. URL: https://doi.org/10.7759/cureus.36097, doi:10.7759/cureus.36097. This article has 8 citations.

7. (nojkov2015gastrointestinalbleedingfrom pages 2-3): Borko Nojkov and Mitchell S Cappell. Gastrointestinal bleeding from dieulafoy's lesion: clinical presentation, endoscopic findings, and endoscopic therapy. World journal of gastrointestinal endoscopy, 7 4:295-307, Apr 2015. URL: https://doi.org/10.4253/wjge.v7.i4.295, doi:10.4253/wjge.v7.i4.295. This article has 190 citations.

8. (inayat2022rectaldieulafoy’slesion pages 4-6): Faisal Inayat, Amna Hussain, Sidra Yahya, Simcha Weissman, Nuraiz Sarfraz, Muhammad Salman Faisal, Iqra Riaz, Saad Saleem, and Muhammad Wasif Saif. Rectal dieulafoy’s lesion: a comprehensive review of patient characteristics, presentation patterns, diagnosis, management, and clinical outcomes. Translational Gastroenterology and Hepatology, 7:10-10, Jan 2022. URL: https://doi.org/10.21037/tgh.2020.02.17, doi:10.21037/tgh.2020.02.17. This article has 23 citations and is from a peer-reviewed journal.

9. (shumilina2024duodenaldieulafoylesion pages 6-7): Tetiana Shumilina, Boldizhar Patricia, and Mykhailo Kochmar. Duodenal dieulafoy lesion: a rare and fatal cause of gastrointestinal bleeding. The Ukrainian Scientific Medical Youth Journal, 146:53-59, Jun 2024. URL: https://doi.org/10.32345/usmyj.2(146).2024.53-59, doi:10.32345/usmyj.2(146).2024.53-59. This article has 0 citations.

10. (al‐bawardy2022gastrointestinalvascularmalformations pages 2-3): Badr Al‐Bawardy and Deborah D. Proctor. Gastrointestinal vascular malformations and neoplasms: arterial, venous, arteriovenous, and capillary. Yamada's Textbook of Gastroenterology, pages 2293-2314, Feb 2022. URL: https://doi.org/10.1002/9781119600206.ch113, doi:10.1002/9781119600206.ch113. This article has 1 citations.

11. (ather2024dieulafoyslesionsomething pages 1-3): N Ather and D Mwengela. Dieulafoy's lesion: something not to be forgotten. Unknown journal, 2024.

12. (nojkov2015gastrointestinalbleedingfrom media ebf94cbf): Borko Nojkov and Mitchell S Cappell. Gastrointestinal bleeding from dieulafoy's lesion: clinical presentation, endoscopic findings, and endoscopic therapy. World journal of gastrointestinal endoscopy, 7 4:295-307, Apr 2015. URL: https://doi.org/10.4253/wjge.v7.i4.295, doi:10.4253/wjge.v7.i4.295. This article has 190 citations.

13. (nojkov2015gastrointestinalbleedingfrom media 528ec365): Borko Nojkov and Mitchell S Cappell. Gastrointestinal bleeding from dieulafoy's lesion: clinical presentation, endoscopic findings, and endoscopic therapy. World journal of gastrointestinal endoscopy, 7 4:295-307, Apr 2015. URL: https://doi.org/10.4253/wjge.v7.i4.295, doi:10.4253/wjge.v7.i4.295. This article has 190 citations.
