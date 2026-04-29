---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:54.987033'
end_time: '2026-04-04T12:34:09.860138'
duration_seconds: 554.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: TGFBI Corneal Dystrophies
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TGFBI Corneal Dystrophies
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **TGFBI Corneal Dystrophies** covering all of the
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
- **Disease Name:** TGFBI Corneal Dystrophies
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **TGFBI Corneal Dystrophies** covering all of the
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


# Comprehensive Research Report: TGFBI Corneal Dystrophies (Genetic)

## Executive summary
TGFBI corneal dystrophies (also termed epithelial–stromal TGFBI dystrophies in IC3D nomenclature) are autosomal-dominant, genotype-driven corneal deposition disorders caused by pathogenic variants in **TGFBI** (5q31) that lead to progressive accumulation of abnormal extracellular deposits (hyaline and/or amyloid) within corneal layers, resulting in recurrent erosions, stromal opacification, and vision loss. Mutational “hotspots” at **Arg124** and **Arg555** account for many classic subtype presentations (e.g., p.Arg124His in granular corneal dystrophy type 2/Avellino, p.Arg555Trp in granular corneal dystrophy type 1). Recurrence after corneal procedures is common, so management emphasizes conservative treatment for erosions and staged surgical approaches (PTK → lamellar keratoplasty → penetrating keratoplasty for deep disease) while avoiding refractive surgery in susceptible individuals. (kheir2019mutationupdatetgfbi pages 1-2, chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 8-9)

## 1. Disease information
### 1.1 Overview / definition
Corneal dystrophies are inherited disorders characterized by progressive deposition of abnormal material in the cornea. (zhu2023variantlandscapeof pages 1-2)

**TGFBI corneal dystrophies** are a genetically-defined subset (“epithelial–stromal TGFBI dystrophies”) in the IC3D classification and include Reis–Bücklers corneal dystrophy (RBCD), Thiel–Behnke corneal dystrophy (TBCD), lattice corneal dystrophies (LCDs), granular corneal dystrophy type 1 (GCD1), and granular corneal dystrophy type 2 (GCD2/Avellino). (mdUnknownyearnomenclatureréviséedu pages 11-15, mdUnknownyearnomenclatureréviséedu pages 8-11, sciriha2024geneticvariantsina pages 58-61)

### 1.2 Key identifiers and ontology mapping
**IC3D (3rd edition) group:** Epithelial–stromal TGFBI dystrophies. (mdUnknownyearnomenclatureréviséedu pages 11-15, mdUnknownyearnomenclatureréviséedu pages 8-11)

**OMIM (MIM) IDs reported in IC3D-derived table text:**
- RBCD: **MIM #608470** (sciriha2024geneticvariantsina pages 58-61)
- TBCD: **MIM #602082** (sciriha2024geneticvariantsina pages 58-61)
- LCD1: **MIM #122200** (sciriha2024geneticvariantsina pages 58-61)
- GCD1: **MIM #121900** (sciriha2024geneticvariantsina pages 58-61)
- GCD2: **MIM #607541** (sciriha2024geneticvariantsina pages 58-61)

**MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not retrieved from the available tool-accessible sources in this run; additional targeted retrieval from OMIM/Orphanet/NCBI MeSH/WHO ICD would be required for authoritative IDs. (mdUnknownyearnomenclatureréviséedu pages 11-15, mdUnknownyearnomenclatureréviséedu pages 8-11)

### 1.3 Synonyms / alternative names
TGFBI gene/protein synonyms and related terms include **BIGH3**, **βig-h3**, **keratoepithelin**, **TGFBIp**, and **RGD-CAP**. (kheir2019mutationupdatetgfbi pages 1-2, kheir2019mutationupdatetgfbi pages 2-3)

Key disease synonym highlighted in multiple sources:
- GCD2 is also called **Avellino corneal dystrophy**. (ashena2023managementofstromal pages 13-15, sciriha2024geneticvariantsinb pages 78-82)

### 1.4 Evidence sources (individual vs aggregated)
- **Aggregated disease resources/classifications:** IC3D genetics-based nomenclature and grouping. (mdUnknownyearnomenclatureréviséedu pages 11-15, mdUnknownyearnomenclatureréviséedu pages 8-11)
- **Aggregated variant resources:** a TGFBI locus-specific variant database (LOVD) is cited/used for keeping variant lists current. (kheir2019mutationupdatetgfbi pages 1-2, kheir2019mutationupdatetgfbi pages 2-3)
- **Primary/clinical evidence:** cohort sequencing studies and clinical case series (e.g., PTK outcomes, population screening). (cho2025geneticepidemiologyof pages 1-2, zeng2019multiplephototherapeutickeratectomy pages 1-3)

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants in **TGFBI** (chromosome **5q31**) encoding an extracellular matrix (ECM) adhesion protein (TGFBIp) that accumulates in corneal deposits. (sciriha2025transcriptomeanalysisof pages 1-3, kheir2019mutationupdatetgfbi pages 2-3)

### 2.2 Risk factors
**Genetic risk factors (causal variants):**
- Pathogenic/likely pathogenic TGFBI variants are enriched at amino acids **Arg124** and **Arg555** (“hotspots”), and many phenotypes have strong genotype–phenotype correlations. (kheir2019mutationupdatetgfbi pages 1-2, kheir2019mutationupdatetgfbi pages 2-3)
- Examples of classic genotype–phenotype links include:
  - **p.Arg555Trp → GCD1**; **p.Arg555Gln → TBCD**; **p.Arg124Cys → LCD1**; **p.Arg124His → GCD2**. (kheir2019mutationupdatetgfbi pages 1-2)

**Iatrogenic/surgical risk:** corneal laser refractive procedures can exacerbate GCD2 with rapid worsening and severe visual deterioration; this is repeatedly cited and used as a rationale for genetic screening in refractive surgery candidates. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, zeng2017tgfbigenemutation pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved evidence. (kheir2019mutationupdatetgfbi pages 1-2)

### 2.4 Gene–environment interactions
The clearest gene–environment interaction supported here is **surgical trauma (e.g., LASIK/PRK/LASEK/SMILE)** interacting with **TGFBI mutations (notably p.Arg124His)** to accelerate deposit formation and clinical progression. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5)

## 3. Phenotypes
### 3.1 Core clinical phenotype spectrum (with suggested HPO terms)
Because IC3D emphasizes overlap across TGFBI phenotypes, the following are recurring features:

**A. Corneal stromal opacities / deposits**
- Clinical: granular/linear (lattice-like) stromal opacities; central predominance. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, sciriha2024geneticvariantsinb pages 78-82)
- Suggested HPO: **Corneal opacity (HP:0007957)**; **Corneal stromal haze** (often mapped under corneal opacity)

**B. Recurrent corneal epithelial erosion with pain**
- Particularly highlighted in GCD2 and RBCD-like superficial phenotypes. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, sciriha2024geneticvariantsina pages 78-82)
- Suggested HPO: **Recurrent corneal erosion (HP:0000557)**; **Eye pain (HP:0004444)**

**C. Decreased visual acuity / progressive visual impairment**
- Reported as deposits progress and haze develops. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5)
- Suggested HPO: **Reduced visual acuity (HP:0007663)**

**D. Genotype-specific histopathologic patterns**
- GCD2: combined **hyaline granular** + **amyloid linear** deposits; hyaline stains with Masson trichrome; amyloid with Congo red; TEM rod-shaped deposits in anterior stroma. (chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 13-15, sciriha2024geneticvariantsinb pages 78-82)
- LCD: branching/interdigitating linear **amyloid** opacities; Congo red positive. (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82)

### 3.2 Age of onset, severity, progression
- GCD2 heterozygotes often present in **teens/young adulthood**; **homozygotes** can present very early (reported as early as **3 years**) with more severe and faster progression. (chang2023minireviewclinicalfeatures pages 3-5)

### 3.3 Phenotype frequency among affected individuals
A subtype-specific frequency estimate is available for GCD2 within regions:
- In Korea/Japan, GCD2 is reported as **72–91% of TGFBI dystrophies**; **67% in China**, **36% in the U.S.**, and **3% in Poland**. (chang2023minireviewclinicalfeatures pages 1-3)

### 3.4 Quality of life impact
Direct QoL instruments (EQ-5D/SF-36) were not found in the retrieved evidence; however, the combination of painful erosions and progressive vision loss implies substantial functional impairment. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5)

## 4. Genetic / molecular information
### 4.1 Causal gene
**TGFBI** (transforming growth factor beta induced), locus **5q31**; a 17-exon gene encoding a secreted ~683-aa ECM protein. (kheir2019mutationupdatetgfbi pages 2-3, sciriha2024geneticvariantsina pages 58-61)

### 4.2 Pathogenic variants (hotspots, types, classification notes)
- A mutation update reported **~68–69 pathogenic/likely pathogenic variants** as of 2019, predominantly autosomal dominant; variants cluster at **Arg124 and Arg555** and in/near FAS1 domains. (kheir2019mutationupdatetgfbi pages 1-2, kheir2019mutationupdatetgfbi pages 2-3)
- Large literature synthesis across corneal dystrophy genes found **TGFBI** to be the most frequently implicated gene (62.82% of families in compiled datasets). (zhu2023variantlandscapeof pages 1-2)
- Caution on variant interpretation: c.1501C>A, p.(Pro501Thr) is highlighted as commonly misinterpreted in literature-scale analyses. (zhu2023variantlandscapeof pages 1-2)

**Representative genotype–phenotype associations (examples):**
- **p.Arg124His (R124H)** → GCD2 / Avellino (kheir2019mutationupdatetgfbi pages 1-2, chang2023minireviewclinicalfeatures pages 1-3)
- **p.Arg555Trp (R555W)** → GCD1 (kheir2019mutationupdatetgfbi pages 1-2, sciriha2024geneticvariantsinb pages 78-82)
- **p.Arg124Cys (R124C)** → LCD1 (kheir2019mutationupdatetgfbi pages 1-2, sciriha2024geneticvariantsinb pages 78-82)
- **p.Arg555Gln (R555Q)** → TBCD (kheir2019mutationupdatetgfbi pages 1-2)

### 4.3 Functional consequences / mechanism hypotheses
TGFBIp is a secreted ECM protein with an N-terminal EMI domain, four FAS1 repeats, and a C-terminal RGD integrin-binding motif, and it binds collagens and contributes to corneal ECM architecture. (sciriha2025transcriptomeanalysisof pages 1-3, kheir2019mutationupdatetgfbi pages 2-3)

Mechanistic hypotheses summarized include altered protein–protein interactions, misfolding/solubility changes, oxidative stress susceptibility, and impaired autophagy, with a cornea-specific extracellular milieu contributing to deposit formation. (sciriha2025transcriptomeanalysisof pages 1-3)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
Not identified in the retrieved evidence for this run. (kheir2019mutationupdatetgfbi pages 1-2)

## 5. Environmental information
No strong evidence for environmental toxins, lifestyle factors, or infectious triggers was retrieved. The clearest non-genetic contributor is **corneal surgery/trauma** (e.g., refractive surgery) accelerating disease expression in mutation carriers. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (conceptual)
1) **Pathogenic TGFBI variant** produces an abnormal TGFBIp (ECM adhesion protein). (kheir2019mutationupdatetgfbi pages 1-2, kheir2019mutationupdatetgfbi pages 2-3)
2) Abnormal TGFBIp undergoes **aberrant extracellular accumulation/aggregation** in the cornea (often detectable by anti-TGFBI immunoreactivity). (kheir2019mutationupdatetgfbi pages 2-3)
3) Deposits can be **hyaline** (granular; Masson trichrome red) and/or **amyloid** (lattice; Congo red), depending on genotype/phenotype. (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82)
4) Deposits disrupt corneal transparency and can protrude toward the epithelium, leading to **recurrent erosions**, pain, and progressive visual impairment. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5)

### 6.2 Pathways and cellular processes (with ontology suggestions)
Transcriptomic analysis of TGFBI knockdown in human corneal epithelial cells reported enrichment of pathways including **SMAD**, **JAK-STAT**, and **PI3K-Akt** (as pathway-level signals potentially tied to epithelial homeostasis and scarring/angiogenesis programs). (sciriha2025transcriptomeanalysisof pages 1-3)

Suggested GO Biological Process terms (high-level, consistent with evidence):
- **extracellular matrix organization**
- **cell adhesion**
- **integrin-mediated signaling pathway**
- **autophagy** (as a hypothesized mechanism) (sciriha2025transcriptomeanalysisof pages 1-3)

### 6.3 Cell types involved (CL suggestions)
Evidence supports major relevance of **corneal epithelial cells** (major transcription source) and **keratocytes** (stromal cells) as contributors to ECM/deposit dynamics. (sciriha2025transcriptomeanalysisof pages 1-3, chang2023minireviewclinicalfeatures pages 3-5)

Suggested Cell Ontology (CL) terms:
- **Corneal epithelial cell**
- **Keratocyte**

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
Primary affected organ: **cornea**. (zhu2023variantlandscapeof pages 1-2)

Localization includes epithelial–stromal involvement and often multi-layer involvement under IC3D’s genetics-based grouping. (sciriha2024geneticvariantsina pages 58-61, mdUnknownyearnomenclatureréviséedu pages 8-11)

Suggested UBERON terms:
- **cornea (UBERON:0000964)**
- **corneal stroma (UBERON:0001775)**
- **corneal epithelium (UBERON:0001774)**

### 7.2 Subcellular level
No subcellular compartment-specific pathology (e.g., ER/lysosome) was directly established in retrieved evidence; impaired autophagy is discussed as a hypothesis. (sciriha2025transcriptomeanalysisof pages 1-3)

## 8. Temporal development
- **Onset:** typically childhood to early adulthood depending on genotype; GCD2 homozygotes can present in early childhood. (chang2023minireviewclinicalfeatures pages 3-5)
- **Course:** generally slowly progressive with episodic exacerbations via erosions; recurrence after procedures is common. (chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 8-9)

## 9. Inheritance and population
### 9.1 Inheritance pattern
Most TGFBI dystrophies are **autosomal dominant**. (kheir2019mutationupdatetgfbi pages 1-2, sciriha2024geneticvariantsina pages 58-61)

### 9.2 Epidemiology statistics (recent)
**Large Korean population genetic screening (129,933 individuals; July 2021–Aug 2024):**
- Allele frequencies detected: **R124H 0.10%**, **P501T 0.58%**, **R555W 0.001%**. (cho2025geneticepidemiologyof pages 1-2)
- Estimated prevalence (per 100,000): **GCD2 203.9**, **LCD variant 1,160.3**, **GCD1 2.3**; combined epithelial–stromal TGFBI dystrophies **1,365.2 per 100,000**. (cho2025geneticepidemiologyof pages 1-2)

**GCD2 prevalence estimate in Korea (review):** about **11.5 per 10,000**. (chang2023minireviewclinicalfeatures pages 1-3)

### 9.3 Population distributions / founder effects
Population differences in subtype proportions (e.g., high prevalence in East Asia) are emphasized for GCD2. (chang2023minireviewclinicalfeatures pages 1-3)

## 10. Diagnostics
### 10.1 Clinical assessment
Diagnosis is based on slit-lamp findings of characteristic deposits/opacities and clinical history (recurrent erosions, visual decline), with genotype confirmation recommended due to phenotypic overlap in IC3D-classified TGFBI dystrophies. (mdUnknownyearnomenclatureréviséedu pages 11-15, chang2023minireviewclinicalfeatures pages 3-5)

### 10.2 Genetic testing
Evidence supports broad use of NGS/exome sequencing (with Sanger confirmation) in corneal dystrophy cohorts and targeted genotyping for known TGFBI hotspots, including screening in refractive surgery settings. (zhu2023variantlandscapeof pages 1-2, zeng2017tgfbigenemutation pages 1-2, cho2025geneticepidemiologyof pages 1-2)

In Eastern China, a pilot study using a commercial “Avellino gene test kit” detected heterozygous TGFBI mutations in **36/42** subjects; among 24 typical granular corneal dystrophy patients, mutation distribution included **R124H 37.5%**, **R555Q 16.7%**, **R124L 25.0%**, **R555W 20.8%**, and **R124C 0%**. The mutation detection rate was **69.2%** among relatives with no corneal signs but positive family history. (zeng2017tgfbigenemutation pages 1-2)

### 10.3 Differential diagnosis
Not systematically extracted from the retrieved texts; however, IC3D emphasizes that genotype can overturn phenotype-based misclassification due to overlap. (mdUnknownyearnomenclatureréviséedu pages 11-15)

### 10.4 Screening (real-world implementation)
A multicenter observational ClinicalTrials.gov study aimed to determine prevalence of five TGFBI dystrophies in refractive surgery candidates using buccal swab PCR genotyping. (NCT02746055 chunk 1)
- ClinicalTrials.gov ID: **NCT02746055**
- Start: **April 2016**; estimated primary completion **Dec 2016**; estimated completion **Apr 2017**; first posted **Apr 21, 2016**. (NCT02746055 chunk 1)
- URL (standard): https://clinicaltrials.gov/study/NCT02746055 (NCT02746055 chunk 1)

Suggested MAXO terms:
- **Genetic screening**
- **Genetic counseling**

## 11. Outcomes / prognosis
- Visual morbidity arises from progressive stromal haze/opacification and recurrent erosions; long-term course often requires repeated procedures due to recurrence. (chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 8-9)
- Procedure recurrence ranges are wide in the literature for GCD2; one mini-review explicitly notes reported recurrence rates vary from **“0%–100%”** across studies depending on definitions/follow-up. (chang2023minireviewclinicalfeatures pages 3-5)

## 12. Treatment
### 12.1 Conservative care (symptom management)
For GCD2-associated erosions, conservative measures include **artificial tears**, **topical antibiotics**, and **bandage contact lenses**. (chang2023minireviewclinicalfeatures pages 1-3)

Suggested MAXO:
- **Lubricant therapy**
- **Topical antibiotic therapy**
- **Therapeutic contact lens fitting**

### 12.2 Phototherapeutic keratectomy (PTK) and related laser approaches
PTK is widely used for anterior deposits in stromal TGFBI dystrophies and is valued for **repeatability** and for delaying keratoplasty, but recurrence is common. (ashena2023managementofstromal pages 1-2, ashena2023managementofstromal pages 21-22)

**Quantitative PTK outcomes:**
- Long-term pedigree study (R124L): mean follow-up **19.6 ± 1.78 years**; multiple PTKs per eye (2–4); after each PTK, “effective visual acuity” maintained **3.60 ± 1.12 years** before significant recurrence; satisfaction **8.6 ± 0.89**. (zeng2019multiplephototherapeutickeratectomy pages 1-3)
- Granular dystrophy series summarized in review: vision improved in **79%** with **20% recurrence** over mean follow-up **3 ± 2.7 years**; other series show ~**23%** significant recurrence at ~40 months; mean time to significant recurrence **23.7 ± 11.2 months** in one cohort. (ashena2023managementofstromal pages 8-9)
- Avellino/GCD2: PTK recurrence can be rapid (reported **7–9 months**), and genotype dependent (homozygotes vs heterozygotes recurrence-free interval **9.5 ± 3.1 vs 38.4 ± 6.2 months**, p < 0.001). (ashena2023managementofstromal pages 13-15)

**Technique considerations:** PTK is less invasive than transplantation; PTK uses 193 nm excimer light and ablates ~0.25 µm tissue per pulse/step as described in a management review. (ashena2023managementofstromal pages 1-2)

Suggested MAXO:
- **Phototherapeutic keratectomy**

### 12.3 Keratoplasty (lamellar and penetrating)
For deeper stromal disease or repeated recurrences, surgical options include **ALK**, **DALK**, or **PK**, with DALK often preferred when endothelium is spared to reduce rejection risk. (chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 19-21)

**Recurrence after keratoplasty (selected data):**
- Avellino: deposits can recur in grafts within **12–24 months**, often at suture tracts or graft–host interfaces; a DALK recurrence was reported at **13 months** in one case. (ashena2023managementofstromal pages 13-15)
- Granular dystrophy: DALK recurrence has been reported as **43%** at mean **38.4 ± 18.6 months** in one series; recurrence is associated with residual host stroma/keratocytes and may be mitigated by Descemet-baring techniques, with trade-offs in perforation risk. (ashena2023managementofstromal pages 11-12)

Suggested MAXO:
- **Deep anterior lamellar keratoplasty**
- **Penetrating keratoplasty**

### 12.4 Refractive surgery (contraindication / harm)
Multiple sources emphasize that refractive laser procedures can exacerbate GCD2; therefore genetic screening can be used to prevent iatrogenic harm in mutation carriers. (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, NCT02746055 chunk 1)

### 12.5 Experimental / emerging therapeutics
Emerging strategies discussed in recent clinical reviews include pharmacologic reduction of TGFBI and gene-based approaches (siRNA/shRNA/CRISPR), but these are not established clinical treatments in the retrieved evidence set. (chang2023minireviewclinicalfeatures pages 5-6, sciriha2025transcriptomeanalysisof pages 1-3)

## 13. Prevention
Primary prevention is not currently established (genetic disease), but **secondary prevention** is feasible:
- **Preoperative genetic screening** in refractive surgery candidates to avoid surgery-triggered exacerbation (implemented in observational prevalence screening programs). (NCT02746055 chunk 1, zeng2017tgfbigenemutation pages 1-2)

Suggested MAXO:
- **Genetic counseling**
- **Cascade genetic testing**

## 14. Other species / natural disease
No naturally occurring non-human species evidence was retrieved in this run. (kheir2019mutationupdatetgfbi pages 1-2)

## 15. Model organisms
No model-organism details were retrieved in this run; additional retrieval focused on TGFBI knock-in/CRISPR animal models would be required. (sciriha2025transcriptomeanalysisof pages 1-3)

## Subtype-oriented synopsis (IC3D epithelial–stromal TGFBI dystrophies)
The following table compiles subtype-level features, variants, deposit types, and treatment/recurrence notes using only retrieved evidence.

| Disease/subtype (synonyms) | Typical TGFBI hotspot variant(s) | Deposit type / histopathology | Typical onset / clinical hallmarks | Common procedures | Recurrence notes |
|---|---|---|---|---|---|
| Reis–Bücklers corneal dystrophy (RBCD; superficial GCD; Bowman's layer type I; historically linked to GCD3/"true" Reis–Bücklers in older literature) | p.Arg124Leu (R124L) (sciriha2024geneticvariantsina pages 58-61, sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Superficial/subepithelial deposits; histochemistry described as similar to GCD1 (hyaline-type), with early recurrent epithelial erosions; deep stroma/endothelium spared (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Early recurrent painful epithelial erosions; diffuse gray-white sand-like superficial deposits; epithelial/subepithelial localization (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | PTK first-line for anterior disease; FLK if PTK not feasible; keratoplasty for deeper/advanced disease (ashena2023managementofstromal pages 1-2, ashena2023managementofstromal pages 19-21, ashena2023managementofstromal pages 5-7) | For Bowman's/anterior TGFBI dystrophies, PTK is preferred because deposits are superficial. Quantitative RBCD-specific recurrence intervals were not provided in the evidence snippets reviewed (ashena2023managementofstromal pages 1-2, ashena2023managementofstromal pages 19-21, ashena2023managementofstromal pages 5-7) |
| Thiel–Behnke corneal dystrophy (TBCD) | p.Arg555Gln (R555Q) (kheir2019mutationupdatetgfbi pages 1-2, sciriha2024geneticvariantsina pages 58-61) | Not detailed in the provided IC3D snippets beyond TGFBI epithelial–stromal classification; clinically grouped with anterior/Bowman-layer TGFBI dystrophies (sciriha2024geneticvariantsina pages 58-61, mdUnknownyearnomenclatureréviséedu pages 11-15, mdUnknownyearnomenclatureréviséedu pages 8-11) | Anterior/superficial opacity pattern within the Bowman/anterior stromal group; managed similarly to other superficial TGFBI dystrophies (ashena2023managementofstromal pages 1-2, ashena2023managementofstromal pages 5-7) | PTK first-line when opacity is not deeper than ~1/3 corneal thickness; FLK or keratoplasty if PTK unsuitable (ashena2023managementofstromal pages 1-2, ashena2023managementofstromal pages 5-7) | Quantitative PTK data available: simple recurrence 100% over long follow-up (~9.7 years) in one series; 50% (5/10 eyes) recurred within 12 months in another; one report noted recurrence in 16.7% after prior keratoplasty (ashena2023managementofstromal pages 5-7) |
| Lattice corneal dystrophy type 1 / LCD variants (classic LCD, LCD1) | p.Arg124Cys (R124C); other variant examples include p.Ala546Asp, p.Pro551Gln (kheir2019mutationupdatetgfbi pages 1-2, sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsin pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Amyloid deposits with central branching/interdigitating linear opacities; amyloid stains with Congo red; reduced corneal sensation may occur (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsin pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Progressive visual loss, recurrent erosions, central branching lattice lines/amyloid opacities (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsin pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | PTK recommended initially; repeat PTK can delay keratoplasty; DALK preferred over PK when transplant needed, with careful AS-OCT and Descemet-baring technique (ashena2023managementofstromal pages 21-22, ashena2023managementofstromal pages 19-21, ashena2023managementofstromal pages 5-7) | PTK recurrence is common but often slow: one series reported 30.1% recurrence with median time ~96 months; repeat PTK is often feasible before keratoplasty (ashena2023managementofstromal pages 21-22, ashena2023managementofstromal pages 5-7) |
| Granular corneal dystrophy type 1 (GCD1) | p.Arg555Trp (R555W) (kheir2019mutationupdatetgfbi pages 1-2, sciriha2024geneticvariantsina pages 58-61, sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Hyaline deposits; Masson trichrome red staining used for hyaline material (contrasted with amyloid/Congo red) (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Granular stromal opacities; homozygous disease reported as more severe with earlier graft recurrence (sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | PTK for anterior stromal lesions; repeat PTK if corneal thickness permits; DALK/ALK for less-deep disease; PK for deep/pre-Descemet involvement (ashena2023managementofstromal pages 21-22, ashena2023managementofstromal pages 8-9, ashena2023managementofstromal pages 13-15, ashena2023managementofstromal pages 11-12) | Quantitative GCD data from mixed granular series: 79% visual improvement with 20% recurrence at mean 3 ± 2.7 years; ~23% significant recurrence at ~40 months in another series; mean time to significant recurrence 23.7 ± 11.2 months in one cohort. DALK recurrence reported as 43% at mean 38.4 ± 18.6 months in one series (ashena2023managementofstromal pages 8-9, ashena2023managementofstromal pages 11-12) |
| Granular corneal dystrophy type 2 (GCD2; Avellino corneal dystrophy) | p.Arg124His (R124H) (kheir2019mutationupdatetgfbi pages 1-2, chang2023minireviewclinicalfeatures pages 1-3, ashena2023managementofstromal pages 13-15, sciriha2024geneticvariantsina pages 58-61, sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Mixed hyaline granular + amyloid lattice-like deposits; hyaline stains with Masson trichrome and amyloid with Congo red; rod-shaped electron-dense/anterior stromal deposits described (chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 13-15, sciriha2024geneticvariantsina pages 78-82, sciriha2024geneticvariantsinb pages 78-82) | Often first–second decade (heterozygotes may present in teens/young adulthood; homozygotes can present as early as age 3); central superficial white dots progressing to ring/stellate granular deposits, later deeper linear lattice-like opacities, stromal haze, painful epithelial erosions; refractive surgery can markedly exacerbate disease (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, chang2023minireviewclinicalfeatures pages 6-8, ashena2023managementofstromal pages 13-15, sciriha2024geneticvariantsinb pages 78-82) | Conservative therapy for erosions (artificial tears, antibiotics, bandage contact lens); PTK for anterior deposits; DALK/ALK for deeper disease; PK for deep or pre-Descemet involvement (chang2023minireviewclinicalfeatures pages 1-3, chang2023minireviewclinicalfeatures pages 3-5, ashena2023managementofstromal pages 13-15) | PTK recurrence is often early and genotype-dependent: recurrence intervals 7–9 months reported; homozygous vs heterozygous recurrence-free interval 9.5 ± 3.1 vs 38.4 ± 6.2 months (p < 0.001); deposits may recur within 18 months after first PTK and within 3 months after repeat PTK. After keratoplasty, graft recurrence may begin within 12–24 months; recurrence after DALK reported at 13 months in one case (chang2023minireviewclinicalfeatures pages 3-5, chang2023minireviewclinicalfeatures pages 5-6, ashena2023managementofstromal pages 13-15) |


*Table: This table summarizes the major IC3D epithelial–stromal TGFBI corneal dystrophies, their typical hotspot variants, pathology, clinical presentation, and current procedure/recurrence patterns supported by the retrieved evidence. It is useful as a compact subtype-oriented reference for phenotype interpretation and management planning.*

## Recent developments and expert analysis (2023–2024 emphasis)
1) **Genetics-driven classification and variant interpretation:** Recent literature-scale analyses emphasize TGFBI’s disproportionate contribution to monogenic corneal dystrophies and the need to avoid variant misinterpretation (e.g., p.Pro501Thr). (zhu2023variantlandscapeof pages 1-2)
2) **Procedure recurrence remains a dominant clinical challenge:** 2023 management syntheses highlight that PTK is valuable but recurrence is common and genotype dependent (especially Avellino/GCD2). (ashena2023managementofstromal pages 13-15, ashena2023managementofstromal pages 8-9)
3) **Growing emphasis on screening in refractive surgery:** Clinical screening initiatives and cohort mutation studies explicitly connect TGFBI genotyping to refractive safety decisions. (NCT02746055 chunk 1, zeng2017tgfbigenemutation pages 1-2)

## References (tool-retrieved; key URLs)
- Kheir V et al. *Human Mutation* (Mar 2019). “Mutation update: TGFBI pathogenic and likely pathogenic variants in corneal dystrophies.” DOI/URL: https://doi.org/10.1002/humu.23737 (kheir2019mutationupdatetgfbi pages 1-2)
- Zhu D et al. *Int J Mol Sci* (Published 6 Mar 2023). DOI/URL: https://doi.org/10.3390/ijms24055012 (zhu2023variantlandscapeof pages 1-2)
- Chang MS et al. *Korean J Ophthalmol* (Aug 2023). DOI/URL: https://doi.org/10.3341/kjo.2023.0032 (chang2023minireviewclinicalfeatures pages 1-3)
- Ashena Z et al. *Vision* (Mar 2023). DOI/URL: https://doi.org/10.3390/vision7010022 (ashena2023managementofstromal pages 1-2)
- Zeng L et al. *BMC Ophthalmology* (Aug 2019). DOI/URL: https://doi.org/10.1186/s12886-019-1167-1 (zeng2019multiplephototherapeutickeratectomy pages 1-3)
- Cho EH et al. *Scientific Reports* (Jul 2025; cohort covers 2021–2024). DOI/URL: https://doi.org/10.1038/s41598-025-08189-7 (cho2025geneticepidemiologyof pages 1-2)
- ClinicalTrials.gov. “Study of the Prevalence of TGFBI Corneal Dystrophies.” NCT02746055 (posted Apr 21, 2016). URL: https://clinicaltrials.gov/study/NCT02746055 (NCT02746055 chunk 1)

References

1. (kheir2019mutationupdatetgfbi pages 1-2): Valeria Kheir, Vianney Cortés‐González, Juan C. Zenteno, and Daniel F. Schorderet. Mutation update: tgfbi pathogenic and likely pathogenic variants in corneal dystrophies. Human Mutation, 40:675-693, Mar 2019. URL: https://doi.org/10.1002/humu.23737, doi:10.1002/humu.23737. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (chang2023minireviewclinicalfeatures pages 1-3): Myung Soo Chang, Ikhyun Jun, and Eung Kweon Kim. Mini-review: clinical features and management of granular corneal dystrophy type 2. Korean Journal of Ophthalmology, 37:340-347, Aug 2023. URL: https://doi.org/10.3341/kjo.2023.0032, doi:10.3341/kjo.2023.0032. This article has 7 citations.

3. (chang2023minireviewclinicalfeatures pages 3-5): Myung Soo Chang, Ikhyun Jun, and Eung Kweon Kim. Mini-review: clinical features and management of granular corneal dystrophy type 2. Korean Journal of Ophthalmology, 37:340-347, Aug 2023. URL: https://doi.org/10.3341/kjo.2023.0032, doi:10.3341/kjo.2023.0032. This article has 7 citations.

4. (ashena2023managementofstromal pages 8-9): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

5. (zhu2023variantlandscapeof pages 1-2): Di Zhu, Junwen Wang, Yingwei Wang, Yi Jiang, Shi-qiang Li, Xueshan Xiao, Panfeng Wang, and Qingjiong Zhang. Variant landscape of 15 genes involved in corneal dystrophies: report of 30 families and comprehensive analysis of the literature. International Journal of Molecular Sciences, 24:5012, Mar 2023. URL: https://doi.org/10.3390/ijms24055012, doi:10.3390/ijms24055012. This article has 4 citations.

6. (mdUnknownyearnomenclatureréviséedu pages 11-15): JSW MD, CJR MD, and MD Berthold Seitz. Nomenclature révisée du comité international pour la classification des dystrophies cornéennes (ic3d)–édition 3. Unknown journal, Unknown year.

7. (mdUnknownyearnomenclatureréviséedu pages 8-11): JSW MD, CJR MD, and MD Berthold Seitz. Nomenclature révisée du comité international pour la classification des dystrophies cornéennes (ic3d)–édition 3. Unknown journal, Unknown year.

8. (sciriha2024geneticvariantsina pages 58-61): GMG Sciriha. Genetic variants in corneal dystrophy genes: a maltese cohort study: inhibition of tgfbi as a treatment modality. Unknown journal, 2024.

9. (kheir2019mutationupdatetgfbi pages 2-3): Valeria Kheir, Vianney Cortés‐González, Juan C. Zenteno, and Daniel F. Schorderet. Mutation update: tgfbi pathogenic and likely pathogenic variants in corneal dystrophies. Human Mutation, 40:675-693, Mar 2019. URL: https://doi.org/10.1002/humu.23737, doi:10.1002/humu.23737. This article has 47 citations and is from a domain leading peer-reviewed journal.

10. (ashena2023managementofstromal pages 13-15): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

11. (sciriha2024geneticvariantsinb pages 78-82): GMG Sciriha. Genetic variants in corneal dystrophy genes: a maltese cohort study: inhibition of tgfbi as a treatment modality. Unknown journal, 2024.

12. (cho2025geneticepidemiologyof pages 1-2): Eun Hye Cho, Myoungkeun Lee, Chang-Seok Ki, Chang Ahn Seol, and Mi-Ae Jang. Genetic epidemiology of epithelial-stromal tgfbi dystrophies in a large korean population. Scientific Reports, Jul 2025. URL: https://doi.org/10.1038/s41598-025-08189-7, doi:10.1038/s41598-025-08189-7. This article has 1 citations and is from a peer-reviewed journal.

13. (zeng2019multiplephototherapeutickeratectomy pages 1-3): Li Zeng, Jing Zhao, Yingjun Chen, Jianmin Shang, Aruma Aruma, and Xingtao Zhou. Multiple phototherapeutic keratectomy treatments in a chinese pedigree with corneal dystrophy and an r124l mutation: a 20-year observational study. BMC Ophthalmology, Aug 2019. URL: https://doi.org/10.1186/s12886-019-1167-1, doi:10.1186/s12886-019-1167-1. This article has 6 citations and is from a peer-reviewed journal.

14. (sciriha2025transcriptomeanalysisof pages 1-3): Gabriella Guo Sciriha, Josef Borg, Janet Sultana, and Joseph Borg. Transcriptome analysis of tgfbi knockdown vs normal corneal epithelial cells: implications for tgfbi corneal dystrophy treatment. Biochemical genetics, Jul 2025. URL: https://doi.org/10.1007/s10528-025-11191-3, doi:10.1007/s10528-025-11191-3. This article has 0 citations and is from a peer-reviewed journal.

15. (zeng2017tgfbigenemutation pages 1-2): Li Zeng, Jing Zhao, Yingjun Chen, Feng Zhao, Meiyan Li, Connie Chao-Shern, Tara Moore, John Marshall, and Xingtao Zhou. Tgfbi gene mutation analysis of clinically diagnosed granular corneal dystrophy patients prior to ptk: a pilot study from eastern china. Scientific Reports, Apr 2017. URL: https://doi.org/10.1038/s41598-017-00716-5, doi:10.1038/s41598-017-00716-5. This article has 8 citations and is from a peer-reviewed journal.

16. (sciriha2024geneticvariantsina pages 78-82): GMG Sciriha. Genetic variants in corneal dystrophy genes: a maltese cohort study: inhibition of tgfbi as a treatment modality. Unknown journal, 2024.

17. (NCT02746055 chunk 1):  Study of the Prevalence of TGFBI Corneal Dystrophies. Avellino Labs USA, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02746055

18. (ashena2023managementofstromal pages 1-2): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

19. (ashena2023managementofstromal pages 21-22): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

20. (ashena2023managementofstromal pages 19-21): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

21. (ashena2023managementofstromal pages 11-12): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

22. (chang2023minireviewclinicalfeatures pages 5-6): Myung Soo Chang, Ikhyun Jun, and Eung Kweon Kim. Mini-review: clinical features and management of granular corneal dystrophy type 2. Korean Journal of Ophthalmology, 37:340-347, Aug 2023. URL: https://doi.org/10.3341/kjo.2023.0032, doi:10.3341/kjo.2023.0032. This article has 7 citations.

23. (ashena2023managementofstromal pages 5-7): Zahra Ashena, Magdalena Niestrata, and Shokufeh Tavassoli. Management of stromal corneal dystrophies; review of the literature with a focus on phototherapeutic keratectomy and keratoplasty. Vision, 7:22, Mar 2023. URL: https://doi.org/10.3390/vision7010022, doi:10.3390/vision7010022. This article has 19 citations and is from a peer-reviewed journal.

24. (sciriha2024geneticvariantsin pages 78-82): GMG Sciriha. Genetic variants in corneal dystrophy genes: a maltese cohort study: inhibition of tgfbi as a treatment modality. Unknown journal, 2024.

25. (chang2023minireviewclinicalfeatures pages 6-8): Myung Soo Chang, Ikhyun Jun, and Eung Kweon Kim. Mini-review: clinical features and management of granular corneal dystrophy type 2. Korean Journal of Ophthalmology, 37:340-347, Aug 2023. URL: https://doi.org/10.3341/kjo.2023.0032, doi:10.3341/kjo.2023.0032. This article has 7 citations.