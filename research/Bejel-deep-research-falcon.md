---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:07:29.131904'
end_time: '2026-04-04T12:24:28.534460'
duration_seconds: 1019.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bejel
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 53
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bejel
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Bejel** covering all of the
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
- **Disease Name:** Bejel
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Bejel** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Bejel (Endemic Syphilis)

### Target disease
- **Disease name:** Bejel
- **Category:** Infectious disease (endemic/nonvenereal treponematosis)
- **Causative agent:** *Treponema pallidum* subsp. *endemicum* (TEN) (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2)
- **MONDO ID:** Not found in the retrieved evidence set (reported as unavailable).

---

## 1. Disease information

### 1.1 Overview (current understanding)
Bejel (also called **endemic syphilis**) is a chronic human treponemal infection caused by *Treponema pallidum* subsp. *endemicum* (TEN), one of the “endemic treponematoses” alongside yaws and pinta (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2). Classically, it is acquired in childhood in hot, dry (semiarid/arid) regions and is considered **nonvenereal**, spreading through close mucosal/skin contact (giacani2014theendemictreponematoses pages 1-2, shinohara2022clinicalperspectivesof pages 1-2).

**Key point:** Recent molecular epidemiology indicates TEN can also circulate outside classical endemic settings and can plausibly be transmitted in sexual networks, where it is clinically indistinguishable from venereal syphilis (TPA) (shinohara2022clinicalperspectivesof pages 2-4, sato2024epidemicofmultiple pages 1-2).

### 1.2 Synonyms and alternative names
- Bejel (mitja2013advancesinthe pages 1-2)
- Endemic syphilis (mitja2013advancesinthe pages 1-2)
- Endemic (nonvenereal) treponematosis / endemic treponemal disease (contextual classification) (giacani2014theendemictreponematoses pages 1-2)

### 1.3 Key identifiers (ontology and coding)
The retrieved primary/review sources did **not** contain explicit mappings for:
- ICD-10/ICD-11
- MeSH
- Orphanet
- OMIM
- MONDO

Therefore, these identifiers are **not reported** here and should be obtained from dedicated ontology resources (outside the current evidence set).

### 1.4 Evidence source type
This report integrates:
- **Aggregated disease-level resources/reviews:** Clinical Microbiology Reviews (2014), PLoS NTD (2013), and CDC MMWR (2024) (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2, papp2024cdclaboratoryrecommendations pages 7-8)
- **Human clinical observational evidence:** adult TEN case series (Japan, 2022) and molecular epidemiology (Tokyo MSM cohort, 2024) (shinohara2022clinicalperspectivesof pages 2-4, sato2024epidemicofmultiple pages 1-2)
- **Human epidemiologic/diagnostic study in endemic-like ulcer settings:** Ghana lesion study (2024) (boaitey2024prevalenceofyaws pages 4-5)
- **Genomics/evolution studies:** TEN WGS (2020) and ancient treponemal genomes related to TEN (Nature 2024) (mikalova2020wholegenomesequence pages 1-2, majander2024redefiningthetreponemal pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
Bejel is caused by infection with **TEN**, a subspecies of *T. pallidum* that is extremely closely related genetically to other pathogenic subspecies (notably TPA and TPE) (giacani2014theendemictreponematoses pages 1-2, mikalova2020wholegenomesequence pages 1-2).

- Genomic similarity: review sources report **~99.7% identity** of TEN to TPA and genome size around **1,137.7 kbp** (giacani2014theendemictreponematoses pages 1-2).

### 2.2 Risk factors
**Classical epidemiology** (disease-level):
- Residence in **arid/semiarid regions** (Sahelian Africa, Saudi Arabia/Middle East) (giacani2014theendemictreponematoses pages 1-2)
- **Childhood exposure** (peak incidence ~2–15 years) (giacani2014theendemictreponematoses pages 1-2)
- Close-contact living conditions facilitating shared utensils/vessels (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2)

**Emerging risk context (recent evidence):**
- Adult cases in developed settings, particularly among MSM, raise concern for sexual-network transmission outside historically endemic areas (shinohara2022clinicalperspectivesof pages 2-4, sato2024epidemicofmultiple pages 1-2).

### 2.3 Protective factors
No specific protective genetic variants or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
Not applicable as a primary framework: bejel is an infectious disease. However, ecological context (arid climate) and behavioral factors (household contact patterns; potentially sexual networks in new contexts) interact with exposure opportunities (giacani2014theendemictreponematoses pages 1-2, sato2024epidemicofmultiple pages 1-2).

---

## 3. Phenotypes

### 3.1 Clinical phenotypes (classical description)
Bejel has staged manifestations broadly similar to syphilis, with predominant involvement of oral/nasal mucosa and bone.

**Primary stage**
- Primary lesion often **unnoticed**; when observed it is described as a **small painless mucous papule or ulcer** in the **oral cavity or nasopharynx** (giacani2014theendemictreponematoses pages 4-5).

**Secondary stage**
- “Mucous patches on the oral mucosa,” “condylomata lata,” “nonitchy skin eruptions,” “generalized lymphadenopathy,” and “laryngitis” (giacani2014theendemictreponematoses pages 4-5).
- Bone involvement can occur (osteitis/periostitis of long bones/hands; nocturnal bone pain) (giacani2014theendemictreponematoses pages 4-5).

**Latency / tertiary stage**
- Secondary lesions typically heal in **6–9 months** with subsequent latency (giacani2014theendemictreponematoses pages 4-5).
- Tertiary disease includes **gummatous** and destructive lesions of mucosa/skin/bone; destructive lesions of palate/nasal septum (“gangosa”) are described (giacani2014theendemictreponematoses pages 4-5, giacani2014theendemictreponematoses pages 1-2).
- Neurologic/cardiac/congenital involvement is considered rare (giacani2014theendemictreponematoses pages 1-2).

### 3.2 Phenotypes in recent adult TEN case series (Japan, 2022)
In a molecularly confirmed adult TEN series (MSM, Kansai):
- Genital lesions in **4 of 5** cases
- Non-itchy maculopapular eruption (“rose spots”), tonsillar enlargement, cervical lymphadenopathy
- No observed CNS or destructive bone involvement in that series (shinohara2022clinicalperspectivesof pages 2-4).

### 3.3 Suggested HPO terms (examples; mapping suggestions)
These are ontology suggestions based on described phenotypes (not directly provided in sources):
- Oral ulcer: **HP:0000210** (oral ulcers) (supported by oral mucosal lesions described in bejel) (giacani2014theendemictreponematoses pages 4-5)
- Skin rash (maculopapular): **HP:0000981** (supported by “nonitchy skin eruptions”) (giacani2014theendemictreponematoses pages 4-5)
- Generalized lymphadenopathy: **HP:0002716** (giacani2014theendemictreponematoses pages 4-5)
- Laryngitis: **HP:0012796** (giacani2014theendemictreponematoses pages 4-5)
- Osteitis / periostitis: **HP:0012749** (osteitis), **HP:0002755** (periostitis) (giacani2014theendemictreponematoses pages 4-5)
- Nasal septum destruction: **HP:0000386** (nasal septum deviation/perforation—closest) (giacani2014theendemictreponematoses pages 4-5)

**Note:** Exact HPO IDs should be validated against the HPO database during curation.

---

## 4. Genetic / molecular information

### 4.1 “Causal genes” and variants
Not applicable in the human Mendelian sense. Pathogen genomic loci are relevant.

### 4.2 Pathogen genomic features relevant to TEN
**tpr gene family and antigenic variation**
- Differences among *T. pallidum* subspecies are repeatedly linked to the **tpr** gene family, which encodes predicted outer membrane antigens implicated in host–pathogen interactions and immune evasion (mikalova2020wholegenomesequence pages 10-11, giacani2014theendemictreponematoses pages 8-9).
- **TprK antigenic variation**: seven variable regions diversify via gene conversion and support immune evasion/persistence (mikalova2020wholegenomesequence pages 10-11, kaminiow2024thesignificanceof pages 2-3).

**TEN genome variation example (Iraq B)**
- WGS of TEN strain Iraq B shows a genome size ~1,137,653 bp and limited SNP/indel differences vs Bosnia A, highlighting overall high conservation (mikalova2020wholegenomesequence pages 1-2).
- Presence/absence variation in **tprF/tprG** (deleted in Bosnia A reference but present in a subpopulation of Iraq B and Bosnia A) suggests genome evolution via deletion and/or subpopulation structure (mikalova2020wholegenomesequence pages 1-2).

**Positive selection and recombination**
- Genes under positive selection are enriched for surface-exposed/secreted proteins (including multiple **tpr genes** and OMPs such as TP0136, TP0548, TP0856/TP0858 and BamA), consistent with immune-driven adaptation (maderankova2019identificationofpositively pages 11-13).
- Recombination has been reported at loci including TP0548 in TEN lineages, consistent with horizontal sequence exchange shaping subspecies differences (maderankova2019identificationofpositively pages 11-13, mikalova2017humantreponemapallidum pages 11-12).

### 4.3 Epigenetics, chromosomal abnormalities
Not applicable/not reported.

---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors
Bejel is associated with **arid/semiarid climates** and is sustained through close contact in settings where sharing utensils/vessels is common (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2).

### 5.2 Infectious agent taxonomy
- Pathogen: *Treponema pallidum* subsp. *endemicum* (TEN) (giacani2014theendemictreponematoses pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → clinical manifestations)
1. **Exposure and entry**: TEN transmission occurs via mucosal/skin contact (often oral mucosa in classical disease) (giacani2014theendemictreponematoses pages 1-2, giacani2014theendemictreponematoses pages 4-5).
2. **Early infection and immune evasion**: *T. pallidum* employs immune evasion mechanisms including limited outer membrane antigen exposure and antigenic variation (TprK), enabling persistence and dissemination within tissues (kaminiow2024thesignificanceof pages 2-3, mikalova2020wholegenomesequence pages 10-11).
3. **Inflammation and lesion formation**: mucous patches/ulcers and rash/lymphadenopathy arise in secondary stages; some patients develop osteitis/periostitis (giacani2014theendemictreponematoses pages 4-5).
4. **Late destructive disease**: gummatous/destructive lesions of mucosa/skin/bone (e.g., palate/nasal septum) can occur in untreated disease (giacani2014theendemictreponematoses pages 4-5, giacani2014theendemictreponematoses pages 1-2).

### 6.2 Molecular pathways and cellular processes (ontology suggestions)
Evidence supports immune evasion and inflammatory tissue damage, but specific named pathways (e.g., mTOR) are not provided in the bejel-specific evidence excerpts.

**Suggested GO biological process terms (to validate during curation):**
- GO:0045087 (innate immune response) (conceptually supported by host–pathogen interaction) (kaminiow2024thesignificanceof pages 2-3)
- GO:0006954 (inflammatory response) (giacani2014theendemictreponematoses pages 4-5)
- GO:0042742 (defense response to bacterium) (kaminiow2024thesignificanceof pages 2-3)

**Suggested Cell Ontology (CL) cell types:**
- Macrophage (CL:0000235) and dendritic cell (CL:0000451) are discussed as important in treponemal immune responses (syphilis literature) (kaminiow2024thesignificanceof pages 2-3).

### 6.3 Tissue tropism and damage mechanisms
Bejel classically targets oral/nasal mucosa and bone, with destructive osteitis in late disease (giacani2014theendemictreponematoses pages 1-2, giacani2014theendemictreponematoses pages 4-5). Differences in tissue tropism among subspecies are hypothesized to arise from small genomic differences in selected loci (e.g., OMPs, chemotaxis proteins) (giacani2014theendemictreponematoses pages 8-9).

### 6.4 Molecular profiling / omics
No TEN-specific transcriptomic/proteomic/metabolomic signatures were identified in the retrieved evidence set.

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level (UBERON suggestions)
- Oral mucosa (UBERON:0000344) and nasopharynx (UBERON:0001728) (primary lesion sites described) (giacani2014theendemictreponematoses pages 4-5)
- Skin (UBERON:0002097) (secondary rash/lesions) (giacani2014theendemictreponematoses pages 4-5)
- Bone tissue (UBERON:0002481) (osteitis/periostitis; destructive osteitis) (giacani2014theendemictreponematoses pages 4-5, giacani2014theendemictreponematoses pages 1-2)
- Nasal septum (UBERON:0001828) and palate (UBERON:0001726) (gangosa/destructive lesions) (giacani2014theendemictreponematoses pages 4-5, giacani2014theendemictreponematoses pages 1-2)

---

## 8. Temporal development

### 8.1 Onset
- Classical onset typically in childhood (2–15 years) in endemic settings (giacani2014theendemictreponematoses pages 1-2).
- Adult-onset cases increasingly recognized when TEN is identified in sexually active adults outside classical endemic regions (shinohara2022clinicalperspectivesof pages 2-4, sato2024epidemicofmultiple pages 1-2).

### 8.2 Progression
- Secondary lesions heal over months (6–9 months) and transition to latency; tertiary destructive disease may develop in untreated cases (giacani2014theendemictreponematoses pages 4-5).

---

## 9. Inheritance and population

### 9.1 Epidemiology (key data)
**Geography and population**
- Classical distribution: Sahelian Africa and Saudi Arabia/Middle East; associated with arid/semiarid climates (giacani2014theendemictreponematoses pages 1-2).

**Historical burden estimates (WHO, mid-20th century)**
- WHO (1950 estimate): ~**1 million endemic syphilis (bejel)** cases (alongside 160 million yaws, 0.7 million pinta) (asiedu2014eradicationofyaws pages 1-2).

**Control campaign quantitative outcomes (WHO/UNICEF 1952–1964)**
- ~**300 million** screened; **>50 million** cases/contacts treated; global burden reduced by ~**95%** to ~**2.5 million** cases (all endemic treponematoses combined) (asiedu2014eradicationofyaws pages 2-3, giacani2014theendemictreponematoses pages 13-14).

**Recent molecular epidemiology suggesting new transmission contexts**
- Tokyo MSM cohort (2019–2022): among 71 whole-blood samples, 26/71 (36.6%) TP0136-positive; TEN detected in 3 samples and reported as ~12% in their typed set; none of the 3 had traveled to bejel-endemic tropical regions (sato2024epidemicofmultiple pages 1-2, sato2024epidemicofmultiple pages 4-6).

### 9.2 Demographics
- Classical: children <15 years are key affected group/reservoir in endemic treponematoses (bejel included) (giacani2014theendemictreponematoses pages 1-2, asiedu2014eradicationofyaws pages 1-2).
- Emerging: adult MSM clusters in Japan described (shinohara2022clinicalperspectivesof pages 2-4, sato2024epidemicofmultiple pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical and laboratory testing
**Serology (CDC 2024)**
- Diagnostic algorithms rely on **both nontreponemal and treponemal tests** (papp2024cdclaboratoryrecommendations pages 1-3).
- Nontreponemal titers correlate with infection activity and are used to **monitor treatment response** (papp2024cdclaboratoryrecommendations pages 8-9).
- Treponemal antibodies often persist after treatment and cannot distinguish active vs past treated infection (papp2024cdclaboratoryrecommendations pages 7-8).

**Key limitation for bejel**
- CDC explicitly states: **“None of the nontreponemal (lipoidal antigen) or treponemal tests can distinguish infections caused by other *T. pallidum* subspecies”** (papp2024cdclaboratoryrecommendations pages 7-8).

**Direct detection**
- Darkfield microscopy: sensitivity ~75–100% and specificity ~94–100% for primary lesions in published estimates, but requires expertise and is less available; conventional Gram stain is inadequate (papp2024cdclaboratoryrecommendations pages 20-21, papp2024morbidityandmortality pages 7-8).
- NAAT/PCR: used in laboratory-developed tests; no FDA-cleared NAATs are marketed in the US (papp2024morbidityandmortality pages 7-8).

**Subspecies identification in practice (research/advanced labs)**
- Adult TEN case series used TpN47 and polA NAAT plus sequence analysis/MLSA for tp0548/tp0856 (shinohara2022clinicalperspectivesof pages 2-4).
- Tokyo MSM study used MLST (TP0136, TP0548, TP0705) from blood and BLAST/phylogeny to detect likely TEN (sato2024epidemicofmultiple pages 1-2).

### 10.2 Differential diagnosis (important in real-world implementation)
A Ghana lesion study (2024) shows that clinically “yaws-like” or “syphilis-like” ulcers can have multiple non-treponemal etiologies:
- Among 110 yaws-like lesions, PCR detected *H. ducreyi* 10/110 (9.1%), HSV-1 2/110 (1.8%), and *T. pallidum* only 1/110 (0.9%) despite higher seropositivity; among 46 syphilis-like lesions, HSV-2 was detected in 13/46 (28.3%) (boaitey2024prevalenceofyaws pages 7-8, boaitey2024prevalenceofyaws pages 1-2).
This supports use of multiplex molecular panels and careful interpretation of serology (boaitey2024prevalenceofyaws pages 10-11).

---

## 11. Outcome / prognosis

Bejel is typically **nonfatal** but can cause disfiguring and disabling late complications if untreated. A WHO-oriented review notes that in endemic treponematoses, ~**10%** of chronic untreated cases can lead to permanent disability and stigma (asiedu2014eradicationofyaws pages 1-2). Bejel-specific modern survival statistics were not identified in the retrieved evidence set.

---

## 12. Treatment

### 12.1 Pharmacotherapy
**First-line (classical, highly effective)**
- **Benzathine penicillin G, intramuscular, single dose**: examples given as **2.4 million units in adults** and **1.2 million units in children <10 years** for early endemic treponematoses (marks2020syphilisandthe pages 7-7).
- Penicillin resistance has not been demonstrated in treponemal infections in the reviewed sources (marks2020syphilisandthe pages 4-6).

**Alternatives and special situations**
- **Doxycycline** is a favored non-penicillin alternative in treponemal infections but is contraindicated in pregnancy (marks2020syphilisandthe pages 4-6).
- In an adult TEN case series (Japan), patients were initially treated with **oral amoxicillin** with serologic and clinical improvement; doxycycline also used (shinohara2022clinicalperspectivesof pages 2-4).

### 12.2 Azithromycin and resistance (expert analysis)
Azithromycin is central for yaws eradication strategies and can enable mass administration, but macrolide resistance is a major concern.
- CDC/WHO-aligned literature describes 23S rRNA point mutations conferring macrolide resistance and the need for surveillance assays (giacani2014theendemictreponematoses pages 13-14).
- In a TEN adult case series, all patients carried **A2058G** (23S rRNA) macrolide-resistance mutation, arguing against macrolides as empiric therapy when TEN is possible and supporting molecular resistance surveillance (shinohara2022clinicalperspectivesof pages 2-4).

### 12.3 Suggested MAXO terms (curation suggestions)
- Benzathine penicillin administration (MAXO term to be selected)
- Azithromycin administration (MAXO term to be selected)
- Mass drug administration (MAXO term to be selected) (marks2015challengesandkey pages 4-6)
- Contact tracing and treatment (MAXO term to be selected)
- Serologic screening/testing (MAXO term to be selected) (papp2024cdclaboratoryrecommendations pages 1-3)
- Molecular diagnostic testing (PCR/NAAT) (MAXO term to be selected) (papp2024morbidityandmortality pages 7-8)

---

## 13. Prevention

### 13.1 Primary prevention
- No vaccine is discussed in the retrieved evidence.
- Public health prevention is primarily by reducing transmission through early case identification and treatment, and (in endemic treponematoses programs) mass treatment strategies (asiedu2014eradicationofyaws pages 2-3, marks2015challengesandkey pages 4-6).

### 13.2 Secondary/tertiary prevention and public health
**Historic implementation (real-world)**
- WHO/UNICEF mass penicillin campaigns (1952–1964) screened ~300 million and treated >50 million cases/contacts, reducing burden ~95% (asiedu2014eradicationofyaws pages 2-3).

**Modern implementation principles (from yaws eradication programs, relevant to bejel where endemic)**
- MDA with azithromycin (30 mg/kg, max 2 g) plus resurveys and targeted treatment is the core of the Morges strategy (marks2015challengesandkey pages 4-6).
- Implementation challenges include non-treponemal ulcer pathogens (e.g., *H. ducreyi*) that can reduce perceived benefit and complicate surveillance (marks2015challengesandkey pages 4-6, boaitey2024prevalenceofyaws pages 7-8).

---

## 14. Other species / natural disease

Bejel is a human disease. However, animal models for endemic treponematoses include rabbit and hamster (giacani2014theendemictreponematoses pages 1-2). The retrieved evidence does not identify a natural non-human reservoir specific for TEN.

---

## 15. Model organisms

- **Rabbit and hamster** are listed as animal models for bejel/endemic treponematoses in Clinical Microbiology Reviews (giacani2014theendemictreponematoses pages 1-2).
- Rabbit infection induces protective immunity primarily against homologous subspecies rather than heterologous subspecies, supporting subspecies-specific antigenic determinants (giacani2014theendemictreponematoses pages 8-9).

---

## Recent developments and latest research (prioritizing 2023–2024)

1. **Diagnostic standards modernization (CDC 2024):** Updated laboratory recommendations emphasize serologic algorithms and direct detection by microscopy/NAAT, explicitly noting subspecies cannot be distinguished by standard serology (papp2024cdclaboratoryrecommendations pages 7-8).
2. **Molecular epidemiology suggesting new transmission routes (2024):** Blood-based MLST in Tokyo MSM identified possible TEN in ~12% of typed positives and found cases without travel to endemic regions (sato2024epidemicofmultiple pages 1-2, sato2024epidemicofmultiple pages 4-6).
3. **Differential diagnosis and programmatic implications (2024 Ghana study):** In ulcer surveillance, PCR frequently identifies *H. ducreyi* and HSV (especially HSV-2 in syphilis-like lesions), while *T. pallidum* DNA may be rare even with seropositivity, emphasizing diagnostic discordance and need for multiplex approaches (boaitey2024prevalenceofyaws pages 7-8, boaitey2024prevalenceofyaws pages 1-2).
4. **Evolutionary reframing (Nature 2024):** Ancient genomes from Brazil most closely related to TEN challenge assumptions that bejel lineages are confined to arid ecologies and refine treponemal divergence timing (majander2024redefiningthetreponemal pages 1-2).

---

## Expert opinions / analysis (authoritative sources)

- Clinical Microbiology Reviews emphasizes that endemic treponematoses are extremely closely related genetically/antigenically and that firm biological bases for subspecies differences are difficult to establish; small genetic changes may underlie differences in virulence and tissue tropism (giacani2014theendemictreponematoses pages 1-2, giacani2014theendemictreponematoses pages 8-9).
- CDC 2024 explicitly highlights a practical diagnostic limitation: routine serology cannot distinguish subspecies, implying that clinical context and (where available) molecular methods are required in settings where endemic and venereal treponematoses overlap (papp2024cdclaboratoryrecommendations pages 7-8).

---

## Key statistics (recent studies)

- Tokyo MSM cohort (2019–2022): TP0136-positive 26/71 (36.6%); full MLST 22/71 (31.0%); TEN detected in 3 samples (~12% of typed positives) (sato2024epidemicofmultiple pages 1-2).
- Ghana Ashanti region lesion study (2021 recruitment; published 2024): overall DPP seroprevalence 24/156 (15.4%); in yaws-like lesions, *T. pallidum* DNA 1/110 (0.9%), *H. ducreyi* 10/110 (9.1%), HSV-1 2/110 (1.8%); in syphilis-like lesions HSV-2 13/46 (28.3%) (boaitey2024prevalenceofyaws pages 4-5, boaitey2024prevalenceofyaws pages 7-8, boaitey2024prevalenceofyaws pages 1-2).
- Historical WHO estimate (1950): ~1 million endemic syphilis cases (asiedu2014eradicationofyaws pages 1-2).

---

## Included evidence table and key visual

The following summary table consolidates the most actionable disease knowledge-base facts.

| Domain | Key facts | Evidence |
|---|---|---|
| Synonyms / definition | **Bejel** = **endemic syphilis**; classically a **nonvenereal endemic treponematosis**. Recent reports note TEN infections can present as syphilis-like disease outside classic endemic settings. | (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2, shinohara2022clinicalperspectivesof pages 1-2) |
| Causative agent | Caused by **_Treponema pallidum_ subsp. _endemicum_ (TEN)**; closely related to other human treponemes, with ~**99.7% genomic identity** to _T. pallidum_ subsp. _pallidum_; genome size reported around **1,137.7 kbp**. | (giacani2014theendemictreponematoses pages 1-2, mikalova2020wholegenomesequence pages 1-2) |
| Transmission | Classical transmission is **mucous-membrane/skin-to-skin contact**, including **sharing eating utensils/drinking vessels**; organism survives only briefly outside host (**~1–2 h**). In recent adult case series and molecular epidemiology studies, **sexual transmission** is strongly suspected/likely in MSM cohorts. | (giacani2014theendemictreponematoses pages 1-2, mitja2013advancesinthe pages 1-2, shinohara2022clinicalperspectivesof pages 1-2, sato2024epidemicofmultiple pages 1-2) |
| Typical age / geography | Classical epidemiology: mainly **children ~2–15 years** in **hot, dry/arid or semiarid regions**, especially **Sahelian Africa** and **Saudi Arabia/Middle East**. Recent molecularly confirmed cases have been reported in **Cuba, Japan, France, Canada** and among adults outside endemic areas. | (giacani2014theendemictreponematoses pages 1-2, mikalova2017humantreponemapallidum pages 1-2, shinohara2022clinicalperspectivesof pages 1-2, shinohara2022clinicalperspectivesof pages 2-4) |
| Primary-stage clinical features | Often **unnoticed**; when present, a **small painless mucous papule/ulcer** usually in the **oral cavity/nasopharynx**. In modern adult cases, **genital lesions** can occur and may be clinically indistinguishable from venereal syphilis. | (giacani2014theendemictreponematoses pages 4-5, mikalova2017humantreponemapallidum pages 1-2, shinohara2022clinicalperspectivesof pages 2-4) |
| Secondary-stage clinical features | **Mucous patches**, **condylomata lata**, **non-itchy skin eruptions**, **generalized lymphadenopathy**, **laryngitis**, split labial papules; may include **osteitis/periostitis** of long bones/hands with **night bone pain**. Adult MSM case series reported genital lesions, rose-spot/maculopapular eruption, tonsillar enlargement, and cervical lymphadenopathy. | (giacani2014theendemictreponematoses pages 4-5, shinohara2022clinicalperspectivesof pages 2-4) |
| Latent / tertiary disease | Secondary manifestations usually heal in **6–9 months** then latency. Tertiary disease includes **gummatous/destructive lesions** of **skin, mucosa, bones**, especially **nose/palate/nasal septum** (gangosa). CNS, cardiac, and congenital disease are considered **rare**. | (giacani2014theendemictreponematoses pages 4-5, giacani2014theendemictreponematoses pages 1-2) |
| Diagnostics: serology | Standard testing uses **both nontreponemal** (e.g., **RPR/VDRL**) and **treponemal** assays. Nontreponemal titers are useful for treatment monitoring; treponemal antibodies often persist after treatment. | (papp2024cdclaboratoryrecommendations pages 7-8, papp2024cdclaboratoryrecommendations pages 8-9) |
| Diagnostic limitations | **Serology cannot distinguish TEN from other _T. pallidum_ subspecies** and cannot by itself separate active from past treated infection. Early lesions may be seronegative/weakly reactive; direct detection methods are limited by availability. | (papp2024cdclaboratoryrecommendations pages 7-8, mitja2013advancesinthe pages 1-2, shinohara2022clinicalperspectivesof pages 2-4) |
| Direct detection / molecular diagnosis | Direct methods include **darkfield microscopy**, lesion staining/histology, and **PCR/NAATs**; subspecies identification in research settings has used **TpN47/polA PCR** plus **MLST** or sequence analysis of loci such as **TP0136, TP0548, TP0705, tp0856**. | (papp2024cdclaboratoryrecommendations pages 7-8, shinohara2022clinicalperspectivesof pages 2-4, sato2024epidemicofmultiple pages 4-6) |
| Treatment and dosing | Classical treatment remains **single-dose intramuscular benzathine penicillin G**: **2.4 million units in adults** and **1.2 million units in children <10 y**. Adult TEN case series reported improvement with **oral amoxicillin**; doxycycline was also used in some cases. | (marks2020syphilisandthe pages 7-7, shinohara2022clinicalperspectivesof pages 2-4, mikalova2017humantreponemapallidum pages 1-2) |
| Azithromycin | Oral **single-dose azithromycin** is effective for **yaws** and underpins mass-treatment strategies for endemic treponematoses, but it has **not been formally studied in bejel** to the same extent; concern exists about **macrolide resistance**. | (mitja2013advancesinthe pages 1-2, marks2020syphilisandthe pages 7-7, shinohara2022clinicalperspectivesof pages 1-2) |
| Recent development (2022): adult TEN case series | Japanese case series reviewed **21 TEN cases outside endemic regions** across 6 articles; among these, **13 were <20 y** and **8 were adults**. In the Kansai series, **4/5** patients had genital lesions; all improved after treatment, and all carried **A2058G** macrolide-resistance mutation. | (shinohara2022clinicalperspectivesof pages 2-4) |
| Recent development (2024): TEN in MSM blood-based MLST study | In Tokyo MSM with syphilis diagnosis, **71** whole-blood samples were studied; **26/71 (36.6%)** were TP0136-positive, full MLST obtained in **22/71 (31.0%)**, and **3/26 (12%)** typed samples were identified as **TEN**. None of those three had visited tropical bejel-endemic regions, supporting possible local sexual transmission. | (sato2024epidemicofmultiple pages 1-2, sato2024epidemicofmultiple pages 4-6) |
| Recent development (2024): lesion diagnostics in Ghana | Among **156** participants with yaws-/syphilis-like lesions, overall DPP seroprevalence was **24/156 (15.4%)**. In yaws-like lesions, seroprevalence was **17.2–17.3%** but lesion PCR detected **_T. pallidum_ in only 1/110 (0.9%)**; other pathogens included **_H. ducreyi_ 10/110 (9.1%)** and **HSV-1 2/110 (1.8%)**. In syphilis-like lesions, seroprevalence was **10.8%** and **HSV-2 13/46 (28.3%)** was common. This highlights major serology–PCR discordance and differential-diagnosis challenges. | (boaitey2024prevalenceofyaws pages 4-5, boaitey2024prevalenceofyaws pages 8-10, boaitey2024prevalenceofyaws pages 1-2, boaitey2024prevalenceofyaws pages 7-8, boaitey2024prevalenceofyaws pages 10-11) |
| Recent development (2024): ancient-genome research | Nature 2024 reconstructed **four ~2,000-year-old treponemal genomes** from Brazil that were **most closely related to TEN** and basal to modern TEN diversity, challenging the assumption that bejel-associated lineages are confined to arid ecologies. | (majander2024redefiningthetreponemal pages 1-2) |
| Key knowledge-base takeaways | Bejel is best modeled as a **treponemal infectious disease** with **classical pediatric, nonsexual, arid-region epidemiology**, but **modern genomic surveillance shows TEN can appear in sexually transmitted networks and mimic venereal syphilis**. Diagnostic workflows therefore require **clinical context + serology + molecular typing where available**. | (giacani2014theendemictreponematoses pages 1-2, papp2024cdclaboratoryrecommendations pages 7-8, sato2024epidemicofmultiple pages 1-2, majander2024redefiningthetreponemal pages 1-2) |


*Table: This table summarizes core bejel characteristics for a disease knowledge base, including classical epidemiology, phenotype, diagnosis, treatment, and notable 2022-2024 research findings. It highlights where modern molecular studies are reshaping understanding of transmission and geographic distribution.*

A key authoritative visual summary (Table 1) of classical bejel features (geography, transmission, clinical involvement, genomic similarity) was retrieved from Clinical Microbiology Reviews (2014) (giacani2014theendemictreponematoses media 9caad504).

---

## Direct quotes (from abstracts in retrieved evidence)

- CDC (2024) abstract: “These tests can be divided into nontreponemal and treponemal tests…” and emphasizes the need for both in an algorithm, and that “Direct detection of *T. pallidum* continues to evolve…” (papp2024morbidityandmortality pages 1-3).
- Mitjà et al. (2013) abstract: “Serological tests are still considered standard laboratory methods… [but] the etiologic agents are indistinguishable in the laboratory.” (mitja2013advancesinthe pages 1-2).

(Note: Abstract-quote availability is limited by the retrieved excerpt content for some papers.)

---

## URLs and publication dates (where available from retrieved sources)

- Papp JR et al. **CDC Laboratory Recommendations for Syphilis Testing, United States, 2024**. MMWR Recomm Rep. **Feb 2024**. https://doi.org/10.15585/mmwr.rr7301a1 (papp2024cdclaboratoryrecommendations pages 1-3)
- Sato W et al. **Epidemic of multiple *Treponema pallidum* strains in MSM in Japan**. AIDS Res Ther. **Oct 2024**. https://doi.org/10.1186/s12981-024-00663-y (sato2024epidemicofmultiple pages 1-2)
- Boaitey YA et al. **Prevalence of yaws and syphilis in Ashanti region of Ghana…** PLOS ONE. **May 2024**. https://doi.org/10.1371/journal.pone.0295088 (boaitey2024prevalenceofyaws pages 1-2)
- Majander K et al. **Redefining the treponemal history through pre-Columbian genomes from Brazil**. Nature. **Jan 2024**. https://doi.org/10.1038/s41586-023-06965-x (majander2024redefiningthetreponemal pages 1-2)
- Giacani L, Lukehart SA. **The Endemic Treponematoses**. Clin Microbiol Rev. **Jan 2014**. https://doi.org/10.1128/cmr.00070-13 (giacani2014theendemictreponematoses pages 1-2)
- Shinohara K et al. **Clinical perspectives of TEN infection in adults (Japan)**. J Infect Chemother. **Mar 2022**. https://doi.org/10.1016/j.jiac.2021.11.012 (shinohara2022clinicalperspectivesof pages 1-2)

---

## Limitations of this report
- Explicit MONDO/MeSH/ICD/Orphanet identifiers were not present in the retrieved full-text excerpts; they should be sourced from ontology databases.
- Modern global incidence/prevalence estimates for bejel specifically are scarce in the retrieved set; available quantitative burden information is largely historical and/or derived from endemic treponematoses as a group.


References

1. (giacani2014theendemictreponematoses pages 1-2): Lorenzo Giacani and Sheila A. Lukehart. The endemic treponematoses. Clinical Microbiology Reviews, 27:89-115, Jan 2014. URL: https://doi.org/10.1128/cmr.00070-13, doi:10.1128/cmr.00070-13. This article has 276 citations and is from a highest quality peer-reviewed journal.

2. (mitja2013advancesinthe pages 1-2): Oriol Mitjà, David Šmajs, and Quique Bassat. Advances in the diagnosis of endemic treponematoses: yaws, bejel, and pinta. PLoS Neglected Tropical Diseases, 7:e2283, Oct 2013. URL: https://doi.org/10.1371/journal.pntd.0002283, doi:10.1371/journal.pntd.0002283. This article has 88 citations and is from a domain leading peer-reviewed journal.

3. (shinohara2022clinicalperspectivesof pages 1-2): Koh Shinohara, Keiichi Furubayashi, Yoko Kojima, Haruyo Mori, Jun Komano, and Takuya Kawahata. Clinical perspectives of treponema pallidum subsp. endemicum infection in adults, particularly men who have sex with men in the kansai area, japan: a case series. Journal of Infection and Chemotherapy, 28:444-450, Mar 2022. URL: https://doi.org/10.1016/j.jiac.2021.11.012, doi:10.1016/j.jiac.2021.11.012. This article has 19 citations and is from a peer-reviewed journal.

4. (shinohara2022clinicalperspectivesof pages 2-4): Koh Shinohara, Keiichi Furubayashi, Yoko Kojima, Haruyo Mori, Jun Komano, and Takuya Kawahata. Clinical perspectives of treponema pallidum subsp. endemicum infection in adults, particularly men who have sex with men in the kansai area, japan: a case series. Journal of Infection and Chemotherapy, 28:444-450, Mar 2022. URL: https://doi.org/10.1016/j.jiac.2021.11.012, doi:10.1016/j.jiac.2021.11.012. This article has 19 citations and is from a peer-reviewed journal.

5. (sato2024epidemicofmultiple pages 1-2): Wakana Sato, Ayako Sedohara, Michiko Koga, Yu Nakagama, Hiroshi Yotsuyanagi, Yasutoshi Kido, and Eisuke Adachi. Epidemic of multiple treponema pallidum strains in men who have sex with men in japan: efficient multi-locus sequence typing scheme and indicator biomarkers. AIDS Research and Therapy, Oct 2024. URL: https://doi.org/10.1186/s12981-024-00663-y, doi:10.1186/s12981-024-00663-y. This article has 2 citations and is from a peer-reviewed journal.

6. (papp2024cdclaboratoryrecommendations pages 7-8): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

7. (boaitey2024prevalenceofyaws pages 4-5): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

8. (mikalova2020wholegenomesequence pages 1-2): Lenka Mikalová, Klára Janečková, Markéta Nováková, Michal Strouhal, Darina Čejková, Kristin N. Harper, and David Šmajs. Whole genome sequence of the treponema pallidum subsp. endemicum strain iraq b: a subpopulation of bejel treponemes contains full-length tprf and tprg genes similar to those present in t. p. subsp. pertenue strains. PLOS ONE, 15:e0230926, Apr 2020. URL: https://doi.org/10.1371/journal.pone.0230926, doi:10.1371/journal.pone.0230926. This article has 16 citations and is from a peer-reviewed journal.

9. (majander2024redefiningthetreponemal pages 1-2): Kerttu Majander, Marta Pla-Díaz, Louis du Plessis, Natasha Arora, Jose Filippini, Luis Pezo-Lanfranco, Sabine Eggers, Fernando González-Candelas, and Verena J. Schuenemann. Redefining the treponemal history through pre-columbian genomes from brazil. Nature, 627:182-188, Jan 2024. URL: https://doi.org/10.1038/s41586-023-06965-x, doi:10.1038/s41586-023-06965-x. This article has 35 citations and is from a highest quality peer-reviewed journal.

10. (giacani2014theendemictreponematoses pages 4-5): Lorenzo Giacani and Sheila A. Lukehart. The endemic treponematoses. Clinical Microbiology Reviews, 27:89-115, Jan 2014. URL: https://doi.org/10.1128/cmr.00070-13, doi:10.1128/cmr.00070-13. This article has 276 citations and is from a highest quality peer-reviewed journal.

11. (mikalova2020wholegenomesequence pages 10-11): Lenka Mikalová, Klára Janečková, Markéta Nováková, Michal Strouhal, Darina Čejková, Kristin N. Harper, and David Šmajs. Whole genome sequence of the treponema pallidum subsp. endemicum strain iraq b: a subpopulation of bejel treponemes contains full-length tprf and tprg genes similar to those present in t. p. subsp. pertenue strains. PLOS ONE, 15:e0230926, Apr 2020. URL: https://doi.org/10.1371/journal.pone.0230926, doi:10.1371/journal.pone.0230926. This article has 16 citations and is from a peer-reviewed journal.

12. (giacani2014theendemictreponematoses pages 8-9): Lorenzo Giacani and Sheila A. Lukehart. The endemic treponematoses. Clinical Microbiology Reviews, 27:89-115, Jan 2014. URL: https://doi.org/10.1128/cmr.00070-13, doi:10.1128/cmr.00070-13. This article has 276 citations and is from a highest quality peer-reviewed journal.

13. (kaminiow2024thesignificanceof pages 2-3): Konrad Kaminiów, Martyna Kiołbasa, and Maciej Pastuszczak. The significance of the cell-mediated host immune response in syphilis. Microorganisms, 12:2580, Dec 2024. URL: https://doi.org/10.3390/microorganisms12122580, doi:10.3390/microorganisms12122580. This article has 6 citations.

14. (maderankova2019identificationofpositively pages 11-13): Denisa Maděránková, Lenka Mikalová, Michal Strouhal, Šimon Vadják, Ivana Kuklová, Petra Pospíšilová, Lenka Krbková, Pavlína Koščová, Ivo Provazník, and David Šmajs. Identification of positively selected genes in human pathogenic treponemes: syphilis-, yaws-, and bejel-causing strains differ in sets of genes showing adaptive evolution. PLOS Neglected Tropical Diseases, 13:e0007463, Jun 2019. URL: https://doi.org/10.1371/journal.pntd.0007463, doi:10.1371/journal.pntd.0007463. This article has 26 citations and is from a domain leading peer-reviewed journal.

15. (mikalova2017humantreponemapallidum pages 11-12): Lenka Mikalová, Michal Strouhal, Jan Oppelt, Philippe Alain Grange, Michel Janier, Nadjet Benhaddou, Nicolas Dupin, and David Šmajs. Human treponema pallidum 11q/j isolate belongs to subsp. endemicum but contains two loci with a sequence in tp0548 and tp0488 similar to subsp. pertenue and subsp. pallidum, respectively. PLOS Neglected Tropical Diseases, 11:e0005434, Mar 2017. URL: https://doi.org/10.1371/journal.pntd.0005434, doi:10.1371/journal.pntd.0005434. This article has 57 citations and is from a domain leading peer-reviewed journal.

16. (asiedu2014eradicationofyaws pages 1-2): Kingsley Asiedu, Christopher Fitzpatrick, and Jean Jannin. Eradication of yaws: historical efforts and achieving who's 2020 target. PLoS Neglected Tropical Diseases, 8:e3016, Sep 2014. URL: https://doi.org/10.1371/journal.pntd.0003016, doi:10.1371/journal.pntd.0003016. This article has 81 citations and is from a domain leading peer-reviewed journal.

17. (asiedu2014eradicationofyaws pages 2-3): Kingsley Asiedu, Christopher Fitzpatrick, and Jean Jannin. Eradication of yaws: historical efforts and achieving who's 2020 target. PLoS Neglected Tropical Diseases, 8:e3016, Sep 2014. URL: https://doi.org/10.1371/journal.pntd.0003016, doi:10.1371/journal.pntd.0003016. This article has 81 citations and is from a domain leading peer-reviewed journal.

18. (giacani2014theendemictreponematoses pages 13-14): Lorenzo Giacani and Sheila A. Lukehart. The endemic treponematoses. Clinical Microbiology Reviews, 27:89-115, Jan 2014. URL: https://doi.org/10.1128/cmr.00070-13, doi:10.1128/cmr.00070-13. This article has 276 citations and is from a highest quality peer-reviewed journal.

19. (sato2024epidemicofmultiple pages 4-6): Wakana Sato, Ayako Sedohara, Michiko Koga, Yu Nakagama, Hiroshi Yotsuyanagi, Yasutoshi Kido, and Eisuke Adachi. Epidemic of multiple treponema pallidum strains in men who have sex with men in japan: efficient multi-locus sequence typing scheme and indicator biomarkers. AIDS Research and Therapy, Oct 2024. URL: https://doi.org/10.1186/s12981-024-00663-y, doi:10.1186/s12981-024-00663-y. This article has 2 citations and is from a peer-reviewed journal.

20. (papp2024cdclaboratoryrecommendations pages 1-3): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

21. (papp2024cdclaboratoryrecommendations pages 8-9): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

22. (papp2024cdclaboratoryrecommendations pages 20-21): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

23. (papp2024morbidityandmortality pages 7-8): JR Papp, IU Park, Y Fakile, L Pereira, and A Pillay. Morbidity and mortality weekly report: recommendations and reports, february 8, 2024/vol. 73/no. rr-1. Unknown journal, 2024.

24. (boaitey2024prevalenceofyaws pages 7-8): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

25. (boaitey2024prevalenceofyaws pages 1-2): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

26. (boaitey2024prevalenceofyaws pages 10-11): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

27. (marks2020syphilisandthe pages 7-7): Michael Marks and David Mabey. Syphilis and the endemic treponematoses. ArXiv, pages 494-500, Jan 2020. URL: https://doi.org/10.1016/b978-0-323-55512-8.00057-0, doi:10.1016/b978-0-323-55512-8.00057-0. This article has 0 citations.

28. (marks2020syphilisandthe pages 4-6): Michael Marks and David Mabey. Syphilis and the endemic treponematoses. ArXiv, pages 494-500, Jan 2020. URL: https://doi.org/10.1016/b978-0-323-55512-8.00057-0, doi:10.1016/b978-0-323-55512-8.00057-0. This article has 0 citations.

29. (marks2015challengesandkey pages 4-6): Michael Marks, Oriol Mitjà, Lasse S Vestergaard, Allan Pillay, Sascha Knauf, Cheng-Yen Chen, Quique Bassat, Diana L Martin, David Fegan, Fasihah Taleo, Jacob Kool, Sheila Lukehart, Paul M Emerson, Anthony W Solomon, Tun Ye, Ronald C Ballard, David C W Mabey, and Kingsley B Asiedu. Challenges and key research questions for yaws eradication. The Lancet. Infectious diseases, 15 10:1220-1225, Oct 2015. URL: https://doi.org/10.1016/s1473-3099(15)00136-x, doi:10.1016/s1473-3099(15)00136-x. This article has 64 citations.

30. (mikalova2017humantreponemapallidum pages 1-2): Lenka Mikalová, Michal Strouhal, Jan Oppelt, Philippe Alain Grange, Michel Janier, Nadjet Benhaddou, Nicolas Dupin, and David Šmajs. Human treponema pallidum 11q/j isolate belongs to subsp. endemicum but contains two loci with a sequence in tp0548 and tp0488 similar to subsp. pertenue and subsp. pallidum, respectively. PLOS Neglected Tropical Diseases, 11:e0005434, Mar 2017. URL: https://doi.org/10.1371/journal.pntd.0005434, doi:10.1371/journal.pntd.0005434. This article has 57 citations and is from a domain leading peer-reviewed journal.

31. (boaitey2024prevalenceofyaws pages 8-10): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

32. (giacani2014theendemictreponematoses media 9caad504): Lorenzo Giacani and Sheila A. Lukehart. The endemic treponematoses. Clinical Microbiology Reviews, 27:89-115, Jan 2014. URL: https://doi.org/10.1128/cmr.00070-13, doi:10.1128/cmr.00070-13. This article has 276 citations and is from a highest quality peer-reviewed journal.

33. (papp2024morbidityandmortality pages 1-3): JR Papp, IU Park, Y Fakile, L Pereira, and A Pillay. Morbidity and mortality weekly report: recommendations and reports, february 8, 2024/vol. 73/no. rr-1. Unknown journal, 2024.
