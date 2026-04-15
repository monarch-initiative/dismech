---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T22:42:41.668243'
end_time: '2026-04-05T22:53:16.511345'
duration_seconds: 634.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SUFU-related nevoid basal cell carcinoma syndrome
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
- **Disease Name:** SUFU-related nevoid basal cell carcinoma syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SUFU-related nevoid basal cell carcinoma syndrome** covering all of the
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
- **Disease Name:** SUFU-related nevoid basal cell carcinoma syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SUFU-related nevoid basal cell carcinoma syndrome** covering all of the
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


# SUFU-related nevoid basal cell carcinoma syndrome (SUFU-related NBCCS): Disease Characteristics Research Report

**Scope:** Mendelian cancer predisposition syndrome caused by germline pathogenic variants in **SUFU**, a core negative regulator of **Sonic Hedgehog (SHH)/Hedgehog** signaling. Evidence is drawn primarily from (i) the large collaborative SUFU cohort study (2022), (ii) a 2024 scoping review specific to germline SUFU variants, (iii) SIOPE HGWG surveillance recommendations (2021) and AACR-focused pediatric brain tumor predisposition surveillance update (2024), and (iv) 2023–2024 basal cell carcinoma (BCC) pathway and treatment literature plus clinical-trials records. Citations refer to the provided evidence context.

---

## 1. Disease Information

### 1.1 Disease overview (current understanding)
SUFU-related NBCCS is the **SUFU-genotype** form of **Gorlin syndrome / nevoid basal cell carcinoma syndrome (NBCCS) / basal cell nevus syndrome (BCNS)**—an **autosomal dominant** cancer predisposition condition characterized by developmental anomalies (often subtle) and increased risk of specific neoplasms, particularly **infant SHH-medulloblastoma**, **adult basal cell carcinoma**, and **adult meningioma**, with additional risk for **gonadal/ovarian tumors**. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2022cancerriskand pages 1-1, lee2024medulloblastomaandother pages 1-2)

### 1.2 Key identifiers and terminology
- **OMIM:** Gorlin syndrome / NBCCS **MIM 109400** (explicitly stated in SIOPE HGWG and SUFU scoping review). (guerrinirousseau2021currentrecommendationsfor pages 1-2, lee2024medulloblastomaandother pages 1-2)
- **Gene:** **SUFU** (Suppressor of Fused homolog), located at **10q24** (reported in SUFU scoping review). (lee2024medulloblastomaandother pages 2-2)
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not directly retrievable from the current tool-accessible evidence set; therefore **not asserted here**.

### 1.3 Common synonyms / alternative names
- Gorlin syndrome
- Gorlin–Goltz syndrome
- Nevoid basal cell carcinoma syndrome (NBCCS)
- Basal cell nevus syndrome (BCNS)
(These are explicitly listed as equivalent names in the 2024 SUFU scoping review and SIOPE surveillance paper.) (lee2024medulloblastomaandother pages 1-2, guerrinirousseau2021currentrecommendationsfor pages 1-2)

### 1.4 Evidence sources (patient-level vs aggregated)
- **Aggregated cohorts:** 172-carrier collaborative cohort defining tumor spectrum/risk. (guerrinirousseau2022cancerriskand pages 1-1)
- **Aggregated guidelines:** SIOPE HGWG genotype-stratified surveillance; AACR-focused surveillance update for childhood brain tumors. (guerrinirousseau2021currentrecommendationsfor pages 1-2, hansford2024updateoncancer pages 3-4)
- **Aggregated literature synthesis:** scoping review of 176 patients across 30 studies. (lee2024medulloblastomaandother pages 1-2)
- **Clinical trial registry records:** multiple BCC/Gorlin trials of Hedgehog inhibitors. (NCT01350115 chunk 1, NCT00957229 chunk 1, NCT00961896 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline heterozygous **pathogenic SUFU variants** conferring cancer predisposition and variable developmental features. SUFU is a negative intracellular regulator of SHH signaling; impaired negative regulation is a central causal mechanism. (lee2024medulloblastomaandother pages 2-2, guerrinirousseau2021currentrecommendationsfor pages 1-2)

**Molecular causal chain (high level):** SUFU loss-of-function (or impaired SUFU–GLI binding) → derepression of GLI transcription factors → increased SHH target-gene expression → tumor predisposition (notably SHH-medulloblastoma and BCC). Mechanistic support includes statements that activated SMO can bind SUFU and enable GLI2 nuclear translocation and target gene transcription; sporadic BCC frequently harbors PTCH/SMO/SUFU lesions activating this axis. (vallini2023signalingpathwaysand pages 2-3, hoashi2022molecularmechanismsand pages 3-5)

### 2.2 Inheritance pattern
**Autosomal dominant** inheritance is explicitly stated for Gorlin syndrome/NBCCS in the SIOPE HGWG guideline and SUFU scoping review. (guerrinirousseau2021currentrecommendationsfor pages 1-2, lee2024medulloblastomaandother pages 1-2)

### 2.3 Risk factors
**Genetic risk factors**
- Germline SUFU pathogenic variants are the defining risk factor, with 64 distinct pathogenic variants reported in the 172-carrier cohort. (guerrinirousseau2022cancerriskand pages 1-1)
- In that cohort, inheritance was **73% inherited** among those where inheritance could be evaluated, consistent with a substantial inherited component. (guerrinirousseau2022cancerriskand pages 1-1)

**Environmental/iatrogenic risk factors (important in clinical practice)**
- **Ionizing radiation**: SIOPE HGWG notes prolonged and thorough follow-up is needed after radiotherapy due to secondary malignancy risk; SUFU carriers treated for childhood medulloblastoma may develop BCC/meningioma earlier, suggesting radiation can modify tumor emergence/timing. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2022cancerriskand pages 6-7)
- **Ultraviolet exposure**: not quantified SUFU-specifically in the available evidence, but BCC risk is part of the syndrome and UV exposure is a known BCC driver; the SIOPE text highlights BCC risk variation across ancestry groups and increased BCC risk with irradiation. (guerrinirousseau2021currentrecommendationsfor pages 2-4)

**Modifier genes (genetic risk modifiers)**
- SIOPE HGWG notes “evidence for modifier genes,” specifically referencing **MC1R ‘red hair’ polymorphisms** as modifiers of BCC risk/feature clustering. (guerrinirousseau2021currentrecommendationsfor pages 2-4)

### 2.4 Protective factors
No SUFU-specific protective alleles are identified in the provided evidence set.

**Practical protective measures (risk reduction):** avoidance of unnecessary ionizing radiation and rigorous photoprotection are supported indirectly by the radiation sensitivity/risk discussion and BCC risk context in guidelines/reviews. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2021currentrecommendationsfor pages 2-4)

### 2.5 Gene–environment interaction
Evidence suggests clinically meaningful interaction between **germline SUFU predisposition** and **radiotherapy** (earlier BCC/meningioma occurrence after MB therapy), and between predisposition and **UV-related BCC risk** (ancestry/skin type differences and modifier-gene effects). However, quantitative GxE interaction models were not available in the retrieved texts. (guerrinirousseau2022cancerriskand pages 6-7, guerrinirousseau2021currentrecommendationsfor pages 2-4)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Core tumor phenotypes (with frequencies and ages)
The best quantitative data are from the 172-carrier SUFU cohort:
- **Any tumor:** 117/172 (68%) had ≥1 tumor; in relatives, cumulative incidence **44.1% by age 50**. (guerrinirousseau2022cancerriskand pages 1-1)
- **Medulloblastoma (SHH subtype):** 86/172 affected; median age **1.5 years**; relative cumulative risk by age 50 **13.3%** (95% CI 6–20.1). (guerrinirousseau2022cancerriskand pages 1-1)
- **Basal cell carcinoma:** 25/172 affected; median age **40 years**; cumulative risk by age 50 **28.5%** (95% CI 13.4–40.9). (guerrinirousseau2022cancerriskand pages 1-1)
- **Meningioma:** 20/172 affected; median age **44 years**; cumulative risk by age 50 **5.2%** (95% CI 0–12). (guerrinirousseau2022cancerriskand pages 1-1)
- **Gonadal tumors:** 11/172 affected; median age **14 years**; cumulative risk by age 50 **4.6%** (95% CI 0–9.7). (guerrinirousseau2022cancerriskand pages 1-1)

The 2024 SUFU scoping review (176 literature cases) further highlights incomplete penetrance/variable expressivity: among 95 patients with data on the three most frequent tumors, **32.6% had none**, **53.7% had one**, **8.4% had two**, and **5.3% had all three** (medulloblastoma, BCC, meningioma). (lee2024medulloblastomaandother pages 1-2)

### 3.2 Developmental/congenital phenotypes (non-tumoral)
SIOPE HGWG notes Gorlin syndrome includes diverse developmental features such as **macrocephaly**, **hypertelorism**, **skeletal anomalies**, and **palmar/plantar pitting**, but also emphasizes that **SUFU-related clinical features may be less prominent** and that many SUFU carriers may not meet classic criteria even later in life. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2021currentrecommendationsfor pages 2-4)

### 3.3 Phenotype ontology mapping (suggested HPO terms)
Tumors
- Medulloblastoma: **HP:0002885** (medulloblastoma)
- Basal cell carcinoma: **HP:0002671** (basal cell carcinoma)
- Meningioma: **HP:0002858** (meningioma)
- Ovarian fibroma / ovarian tumor: **HP:0030680** (ovarian fibroma) / **HP:0100615** (ovarian neoplasm)

Selected non-tumoral findings commonly used in Gorlin syndrome criteria (not SUFU-specific frequency in evidence)
- Macrocephaly: **HP:0000256**
- Hypertelorism: **HP:0000316**
- Palmar pits / plantar pits: **HP:0007400** (palmar pits), **HP:0007418** (plantar pits)
- Odontogenic keratocyst (jaw cyst): **HP:0010603** (odontogenic keratocyst)

(These HPO mappings are standard; however, the evidence base here does not provide SUFU-specific frequencies for most non-tumoral features.)

### 3.4 Quality of life impact
QoL impacts are not quantified SUFU-specifically in the available evidence set. Nonetheless, guideline and treatment studies emphasize that multiple BCCs can drive repeated surgeries, scarring, and chronic treatment burden, and that tolerability issues with chronic Hedgehog inhibitor therapy are common. (lang2024s2kguidelinebasal pages 11-12, murgia2024gorlinsyndromeassociatedbasal pages 2-4)

---

## 4. Genetic/Molecular Information

### 4.1 Causal gene(s)
- **SUFU** is a causal gene for SUFU-related NBCCS. (lee2024medulloblastomaandother pages 2-2)

### 4.2 Variant spectrum / pathogenic variant types
The large SUFU cohort reports **64 different SUFU pathogenic variants** across the gene, consistent with broad allelic heterogeneity. (guerrinirousseau2022cancerriskand pages 1-1)

Variant types are not enumerated in the extracted cohort snippet; however, tumor-derived SUFU mutations in sporadic BCC include loss-of-function variants that disrupt SUFU–GLI binding and inappropriately activate Hedgehog signaling. (taylor2002mutationsinsufu pages 1-2)

### 4.3 Functional consequences
Mechanistic statements strongly support **loss of SUFU repression of GLI** as a core functional consequence:
- In advanced BCC review: activated SMO binds SUFU (a “crucial negative regulator”) enabling GLI2 nuclear translocation and transcription of HH targets. (vallini2023signalingpathwaysand pages 2-3)
- In sporadic BCC sequencing study abstract: “SUFU normally binds… GLI1… to prevent it from initiating transcription of Hedgehog target genes”; loss-of-function SUFU variants “disrupt its binding to GLI, leading to constitutive pathway activation.” (taylor2002mutationsinsufu pages 1-2)

### 4.4 Pathways / molecular function (ontology suggestions)
- **Primary pathway:** Sonic Hedgehog/Hedgehog signaling with downstream **GLI** transcription factors. (vallini2023signalingpathwaysand pages 2-3, lee2024medulloblastomaandother pages 2-2)

**Suggested GO biological process terms** (mechanism-consistent)
- Hedgehog signaling pathway: **GO:0007224**
- Regulation of transcription by RNA polymerase II: **GO:0006357**
- Negative regulation of signal transduction: **GO:0009968**

**Suggested GO molecular function terms**
- Protein binding: **GO:0005515** (SUFU–GLI interactions)

**Suggested CL cell-type terms** (disease-relevant)
- Cerebellar granule neuron precursor: **CL:0002603** (relevant to SHH medulloblastoma cell-of-origin context)
- Keratinocyte: **CL:0000312** (relevant to BCC pathogenesis)

---

## 5. Environmental Information

No SUFU-specific environmental exposures beyond general BCC/radiotherapy context were quantified in the retrieved evidence.

Key practical environmental/iatrogenic considerations include:
- **Ionizing radiation exposure**: noted as a risk modifier for secondary malignancies and earlier BCC/meningioma after MB therapy. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2022cancerriskand pages 6-7)

---

## 6. Mechanism / Pathophysiology

### 6.1 Canonical mechanism: SUFU loss → Hedgehog pathway activation
SUFU is repeatedly described as a **negative intracellular regulator** of SHH signaling, and impaired SUFU function results in increased pathway output. (lee2024medulloblastomaandother pages 2-2, vallini2023signalingpathwaysand pages 2-3)

A particularly direct mechanistic statement from a sporadic BCC tumor sequencing/functional study abstract is:
- “**SUFU normally binds… GLI1… to prevent it from initiating transcription** of Hedgehog target genes… loss of function SUFU variants… **disrupt its binding to GLI, leading to constitutive pathway activation**.” (taylor2002mutationsinsufu pages 1-2)

### 6.2 Tissue- and context-dependence
The SUFU scoping review emphasizes that while SUFU is a negative regulator, “the **precise mechanisms**… still **not fully understood**,” and that phenotype is poorly characterized due to limited longitudinal data—highlighting ongoing research needs. (lee2024medulloblastomaandother pages 2-2, lee2024medulloblastomaandother pages 1-2)

A major 2024 mouse-model paper suggests a more complex dosage-dependent role (expert-level nuance): increased SUFU gene dosage was associated with heightened SHH signaling and **promoted medulloblastoma tumorigenesis** in certain genetic contexts (Ptch1 ablation). (han2024increasingsufugene pages 1-2)

### 6.3 Suggested causal chain to clinical manifestations
**Medulloblastoma (infant SHH-MB):** germline SUFU PV → increased SHH pathway output in developing cerebellum → abnormal proliferation/survival of SHH-responsive progenitors → SHH-medulloblastoma in infancy. Tumor risk in carriers is concentrated in the first years of life, motivating high-frequency early MRI surveillance. (guerrinirousseau2022cancerriskand pages 1-1, guerrinirousseau2022cancerriskand pages 7-8)

**Basal cell carcinoma (adult):** germline SUFU PV (plus UV/radiation and somatic second hits) → derepressed GLI transcriptional program in keratinocytes → BCC emergence, often in adulthood; sporadic BCC commonly shows PTCH/SMO/SUFU lesions, supporting shared pathway etiology. (vallini2023signalingpathwaysand pages 2-3, guerrinirousseau2022cancerriskand pages 1-1)

---

## 7. Anatomical Structures Affected (ontology suggestions)

### 7.1 Primary organs/tissues
- **Skin** (BCC): UBERON:0002097
- **Brain/cerebellum** (medulloblastoma; meningioma): UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0001875 (meninges)
- **Gonads/ovary** (gonadal tumors/ovarian fibromas): UBERON:0000992 (ovary)

Supported by the tumor spectrum and surveillance focus (dermatologic exams, brain MRI, pelvic ultrasound). (guerrinirousseau2022cancerriskand pages 1-1, guerrinirousseau2022cancerriskand pages 7-8)

### 7.2 Subcellular localization (mechanistically relevant)
- Nuclear/cytoplasmic control of GLI is central; SUFU’s role is described in preventing GLI transcriptional activation by binding GLI and affecting nuclear activity. (taylor2002mutationsinsufu pages 1-2)

---

## 8. Temporal Development (natural history)

**Key temporal pattern (strongly supported):**
- **Medulloblastoma:** early childhood (median ~1.5 years). (guerrinirousseau2022cancerriskand pages 1-1)
- **Gonadal tumors:** adolescence (median ~14 years). (guerrinirousseau2022cancerriskand pages 1-1)
- **Basal cell carcinoma:** adulthood (median first BCC ~40 years). (guerrinirousseau2022cancerriskand pages 1-1)
- **Meningioma:** adulthood (median ~44 years). (guerrinirousseau2022cancerriskand pages 1-1)

This age-stratified risk directly drives surveillance design. (guerrinirousseau2022cancerriskand pages 7-8)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Birth incidence** of clinical Gorlin syndrome (PTCH1/SUFU combined) is reported in SIOPE HGWG, but SUFU-specific population prevalence is not directly provided in the accessible excerpt. (guerrinirousseau2021currentrecommendationsfor pages 1-2)

### 9.2 Penetrance and expressivity
- In relatives in the 172-carrier cohort, cumulative incidence of any tumor reaches **44.1% by age 50**, indicating incomplete penetrance. (guerrinirousseau2022cancerriskand pages 1-1)
- In the 2024 scoping review subset, about **one-third** of patients had none of the three most frequent tumors (MB/BCC/meningioma), highlighting variable expressivity and incomplete penetrance. (lee2024medulloblastomaandother pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria
SIOPE HGWG provides standard diagnostic criteria and emphasizes integration with genetics:
- Diagnosis requires **“Two major diagnostic criteria and one minor diagnostic criterion or one major and three minor diagnostic criteria”** and may be confirmed by identification of a heterozygous **PTCH1 or SUFU** pathogenic variant. (guerrinirousseau2021currentrecommendationsfor pages 1-2)

Major criteria listed include (among others): early/multiple BCCs, odontogenic keratocysts, palmar/plantar pits, falx calcification, medulloblastoma (typically desmoplastic), first-degree relative. Minor criteria include skeletal malformations, macrocephaly, cleft lip/palate, ovarian/cardiac fibroma, etc. (guerrinirousseau2021currentrecommendationsfor pages 1-2)

### 10.2 Genetic testing approach
- SIOPE HGWG notes molecular confirmation by testing **PTCH1, PTCH2, SUFU** (though PTCH2 is de-emphasized as rare/uncertain in some series); and specifically recommends **germline testing for PTCH1 and SUFU in all children with SHH-medulloblastoma**, particularly <5 years. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2021currentrecommendationsfor pages 4-5)

### 10.3 Screening / surveillance as part of diagnostic and management pathway
The surveillance program is a major component of real-world implementation (see Section 11 and Table artifact below). (guerrinirousseau2022cancerriskand pages 7-8, hansford2024updateoncancer pages 3-4)

---

## 11. Outcome / Prognosis

### 11.1 Tumor risks and mortality
- In the 172-carrier cohort, follow-up was available for 160 carriers: **137 alive** and **23 deceased** (cause not specified in the excerpt), emphasizing that medulloblastoma and other neoplasms can be life-threatening. (guerrinirousseau2022cancerriskand pages 1-1)

### 11.2 Prognostic factors
Not quantified SUFU-specifically in the available evidence beyond:
- Strong age-dependence of tumor spectrum (early MB vs later BCC/meningioma). (guerrinirousseau2022cancerriskand pages 1-1)
- Radiotherapy history as a modifier for later tumor risks. (guerrinirousseau2022cancerriskand pages 6-7)

---

## 12. Treatment

### 12.1 Management of basal cell carcinomas (real-world implementations)

**Surgery remains first-line for most BCC**, with systemic therapies reserved for advanced/multiple lesions; this is reflected in BCC guideline updates. (lang2024s2kguidelinebasal pages 11-12)

**Targeted therapy: Hedgehog pathway inhibitors (HHIs)**
- Vismodegib (GDC-0449) and sonidegib (LDE225) are oral SMO inhibitors used in advanced/multiple BCC, including Gorlin syndrome cases. (murgia2024gorlinsyndromeassociatedbasal pages 2-4)

**Recent real-world Gorlin cohort (2024):** retrospective study of 16 Gorlin patients treated March 2012–Jan 2024.
- At 4 months, **clinical remission 61.5%** with sonidegib vs **16.7%** with vismodegib; **adverse events** occurred in **100%** vismodegib vs **57.9%** sonidegib patients (p<0.05). (murgia2024gorlinsyndromeassociatedbasal pages 5-7)

**Advanced BCC trial context (2023 synthesis):**
- ERIVANCE 39-month update: ORR 48.5% (mBCC), 60.3% (laBCC); median DOR 14.8 months (mBCC), 26.2 months (laBCC).
- STEVIE: laBCC RR 68.5%; mBCC RR 36.9%; DOR in laBCC subgroup **28.8 months** with Gorlin vs **18.7 months** without Gorlin. (vallini2023signalingpathwaysand pages 6-7)

**Tolerability and intermittent dosing:**
- German S2k BCC guideline (update 2023; published 2024) notes in a long-term follow-up of a Gorlin vismodegib trial, only **3/18 (17%)** tolerated continuous therapy for 36 months and intermittent regimens (e.g., 12 weeks on/8 weeks off) are proposed to improve feasibility. (lang2024s2kguidelinebasal pages 11-12)

**MAXO (treatment action ontology) suggestions**
- Surgical excision of BCC: MAXO:0000455 (excision)
- Mohs micrographic surgery: MAXO:0000462 (Mohs surgery)
- Hedgehog pathway inhibitor therapy: MAXO:0001026 (targeted therapy) / MAXO:0000058 (drug therapy)
- Dermatologic surveillance: MAXO:0000127 (screening)

### 12.2 Pediatric medulloblastoma (SUFU carriers)
Treatment details are not provided in full in the accessible SUFU-specific guideline excerpts; however, both SIOPE HGWG and AACR emphasize that identifying germline predisposition can affect management and surveillance. (guerrinirousseau2021currentrecommendationsfor pages 4-5, hansford2024updateoncancer pages 3-4)

### 12.3 Clinical trials (selected; real-world implementations)
ClinicalTrials.gov records document multiple interventional studies in Gorlin/NBCCS:
- **NCT00957229** (Vismodegib; Phase II; randomized; 41 participants; start Aug 2009; completed Jan 2014). Primary endpoint: number of new surgically eligible BCCs; linked NEJM publication (PMID **22670904**, per registry). (NCT00957229 chunk 1)
- **NCT01350115** (Sonidegib/LDE225 oral; Phase II; randomized; 10 participants; start Apr 2011; completed Oct 2012; results posted Oct 19, 2015). (NCT01350115 chunk 1)
- **NCT00961896** (Topical LDE225; Phase II; 18 participants; started Jul 2009; primary completion Aug 2010; completed). (NCT00961896 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
- Avoidance of unnecessary **ionizing radiation** is a key preventive principle given secondary malignancy concerns and earlier tumor emergence after radiotherapy. (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2022cancerriskand pages 6-7)
- Photoprotection to reduce BCC burden is clinically standard, though not SUFU-quantified in available evidence.

### 13.2 Secondary prevention (screening / early detection)
This is the most actionable prevention layer and is strongly evidence-based via guidelines and cohort-risk estimates.

**Key surveillance table (SIOPE HGWG) image evidence:** Table 5 extracted from the SIOPE HGWG surveillance guideline provides genotype-stratified recommendations (PTCH1 vs SUFU). (guerrinirousseau2021currentrecommendationsfor media 7a72a3c0)

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary SUFU-NBCCS analogs were identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Mouse models relevant to SUFU/SHH tumorigenesis (selected)
- A 2024 JCI Insight study reports that **increasing Sufu gene dosage** in mice can produce **preaxial polydactyly** and, in combination with Ptch1 ablation, can **promote medulloblastoma tumorigenesis**, highlighting complex dosage effects beyond a simple tumor-suppressor model. (han2024increasingsufugene pages 1-2)
- Foundational human genetics demonstrate SUFU truncations can lead to SHH pathway activation by failing to export GLI from nucleus to cytoplasm; this establishes mechanistic plausibility for SUFU-driven SHH tumorigenesis and aligns with mouse SHH-pathway tumor models (Ptch+/− medulloblastoma; SHH/GLI skin models). (taylor2002mutationsinsufu pages 1-2)

### 15.2 Model utility and limitations
- Utility: enables mechanistic dissection of SUFU–GLI regulation and testing of pathway inhibitors, though SUFU-driven tumors may be downstream of SMO and thus not responsive to SMO inhibitors in some contexts (not fully supported in the accessible mouse excerpts).
- Limitations: phenotype penetrance varies by genetic background and cooperating hits; increased SUFU dosage effects complicate simplistic assumptions about SUFU as solely a negative regulator in vivo. (han2024increasingsufugene pages 1-2)

---

## Consolidated risk and surveillance summary table

| Domain | Item (tumor or test) | Key quantitative estimate | Age window/start | Notes (e.g., SUFU vs PTCH1 differences) | Source |
|---|---|---|---|---|---|
| Risk | Any tumor | 117/172 carriers (68%) developed ≥1 tumor; cumulative incidence in relatives 14.4% by age 5, 18.2% by age 20, 44.1% by age 50 | Lifelong; strongest early-childhood risk for MB | Multiple tumors in 28% of affected carriers; lifelong but age-stratified spectrum | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385 (guerrinirousseau2022cancerriskand pages 1-1, guerrinirousseau2022cancerriskand pages 6-7) |
| Risk | Medulloblastoma | 86/172 total cases in cohort; cumulative risk by age 50 = 13.3% (95% CI 6.0-20.1) in relatives | Median age 1.5 years; largely before age 5, especially first 3 years | Predominant SUFU-associated tumor; SHH subgroup; risk higher in SUFU than PTCH1 in prior literature/reviews | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385; Lee et al., Am J Med Genet A 2024, doi:10.1002/ajmg.a.63496 (guerrinirousseau2022cancerriskand pages 1-1, lee2024medulloblastomaandother pages 1-2, lee2024medulloblastomaandother pages 2-2) |
| Risk | Basal cell carcinoma | 25/172 total cases; cumulative risk by age 50 = 28.5% (95% CI 13.4-40.9) | Median age 40 years for first BCC | Adult-onset predominance; lower/less certain risk than classic PTCH1-related Gorlin syndrome; risk may be increased after radiotherapy | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385; Guerrini-Rousseau et al., Familial Cancer 2021, doi:10.1007/s10689-021-00247-z (guerrinirousseau2022cancerriskand pages 1-1, guerrinirousseau2021currentrecommendationsfor pages 2-4) |
| Risk | Meningioma | 20/172 total cases; cumulative risk by age 50 = 5.2% (95% CI 0-12) | Median age 44 years | Often later-onset; earlier/more frequent after prior cranial irradiation; considered more frequent in SUFU than PTCH1 carriers | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385; Lee et al., Am J Med Genet A 2024, doi:10.1002/ajmg.a.63496 (guerrinirousseau2022cancerriskand pages 1-1, lee2024medulloblastomaandother pages 16-16) |
| Risk | Gonadal/ovarian tumors | 11/172 total gonadal tumors; cumulative risk by age 50 = 4.6% (95% CI 0-9.7) overall | Median age 14 years | Adolescent-predominant; ovarian tumors/fibromas are emphasized in females; more frequent in SUFU than PTCH1 cohorts | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385; Guerrini-Rousseau et al., Familial Cancer 2021, doi:10.1007/s10689-021-00247-z (guerrinirousseau2022cancerriskand pages 1-1, guerrinirousseau2021currentrecommendationsfor pages 1-2) |
| Risk | Spectrum in scoping review | Among 176 literature cases: medulloblastoma 59, BCC 21, meningioma 19; among 95 with data on top 3 tumors, 32.6% had none, 53.7% had one, 8.4% had two, 5.3% had all three | Germline SUFU diagnosis median age 4.5 years; MB median 1.42 years | Demonstrates incomplete penetrance and variable expressivity | Lee et al., Am J Med Genet A 2024, doi:10.1002/ajmg.a.63496 (lee2024medulloblastomaandother pages 1-2) |
| Surveillance | Brain MRI for medulloblastoma | Every 3-4 months during first 3 years, then every 6 months until age 5 | From birth / diagnosis to age 5 | SUFU-specific recommendation; not recommended routinely for PTCH1 carriers | Guerrini-Rousseau et al., Familial Cancer 2021, doi:10.1007/s10689-021-00247-z; Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385 (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2022cancerriskand pages 7-8, lee2024medulloblastomaandother pages 14-14) |
| Surveillance | Neurologic exams / head circumference | Regular clinical monitoring with frequent neurologic exams and serial head circumference assessment in infancy/early childhood | Infancy / diagnosis through first 5 years | Supportive surveillance adjunct to MRI for SUFU carriers with early-childhood MB risk | Hansford et al., Clin Cancer Res 2024, doi:10.1158/1078-0432.CCR-23-4033 (hansford2024updateoncancer pages 3-4, hansford2024updateoncancer pages 2-3) |
| Surveillance | Brain MRI for meningioma | Every 3-5 years | Start at age 30 if no prior MB; after completion/healing of MB follow-up if previously treated | Particularly relevant for SUFU carriers and those exposed to cranial irradiation | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385; Lee et al., Am J Med Genet A 2024, doi:10.1002/ajmg.a.63496 (guerrinirousseau2022cancerriskand pages 7-8, lee2024medulloblastomaandother pages 14-14) |
| Surveillance | Dermatologic examination | Annual skin examination | Start at age 20 | Later start than PTCH1 carriers (PTCH1: age 10); start earlier if prior radiotherapy | Guerrini-Rousseau et al., Familial Cancer 2021, doi:10.1007/s10689-021-00247-z; Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385 (guerrinirousseau2021currentrecommendationsfor pages 1-2, guerrinirousseau2022cancerriskand pages 7-8) |
| Surveillance | Pelvic ultrasound | Every 3 years | Begin at age 5 years | Intended to screen ovarian/gonadal tumors/fibromas in females; SUFU carriers included | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385 (guerrinirousseau2022cancerriskand pages 7-8) |
| Surveillance | Echocardiogram | One-time baseline screen at diagnosis | At diagnosis, ideally in first 6 months of life | Cardiac fibromas are less clearly part of SUFU phenotype than PTCH1, but SIOPE table includes baseline echo | Guerrini-Rousseau et al., J Med Genet 2022, doi:10.1136/jmedgenet-2021-108385; Lee et al., Am J Med Genet A 2024, doi:10.1002/ajmg.a.63496 (guerrinirousseau2022cancerriskand pages 7-8, lee2024medulloblastomaandother pages 16-16) |


*Table: This table summarizes the major tumor risks, ages of onset, and SUFU-specific surveillance recommendations for germline SUFU pathogenic variant carriers. It is useful as a quick-reference comparison of natural history and screening guidance drawn from the key cohort, scoping review, and SIOPE recommendations.*

### Key surveillance figure/table (from SIOPE HGWG)
A cropped image of the SIOPE HGWG surveillance recommendations table (Table 5) was retrieved to support implementation details. (guerrinirousseau2021currentrecommendationsfor media 7a72a3c0)

---

## Expert synthesis / analytical notes (authoritative interpretation)
1. **SUFU genotype shifts clinical priorities** toward early-life **brain tumor surveillance** (high-frequency MRI in infancy/early childhood), in contrast to PTCH1 where dermatologic and odontogenic manifestations often dominate early clinical suspicion. (guerrinirousseau2021currentrecommendationsfor pages 2-4, guerrinirousseau2022cancerriskand pages 7-8)
2. **Penetrance is incomplete** and expressivity is variable: in aggregated SUFU datasets, a substantial fraction of carriers may remain asymptomatic for major tumors, necessitating careful counseling about probabilistic risk rather than deterministic outcomes. (lee2024medulloblastomaandother pages 1-2, guerrinirousseau2022cancerriskand pages 1-1)
3. **Therapeutic tradeoffs are prominent** for chronic BCC control: HHIs suppress new and existing BCCs but often have substantial adverse-event burden and limited long-term tolerability; evidence in Gorlin cohorts suggests **sonidegib may be better tolerated** than vismodegib in some real-world settings, though datasets remain small. (murgia2024gorlinsyndromeassociatedbasal pages 5-7, lang2024s2kguidelinebasal pages 11-12)

---

## URLs and publication dates (selected key sources)
- Guerrini-Rousseau et al. **Familial Cancer** (published online **16 Apr 2021**). “Current recommendations for cancer surveillance in Gorlin syndrome…” https://doi.org/10.1007/s10689-021-00247-z (guerrinirousseau2021currentrecommendationsfor pages 1-2)
- Guerrini-Rousseau et al. **Journal of Medical Genetics** (**Jun 2022**). “Cancer risk and tumour spectrum in 172 patients…” https://doi.org/10.1136/jmedgenet-2021-108385 (guerrinirousseau2022cancerriskand pages 1-1)
- Lee et al. **Am J Med Genet A** (**Jan 2024**; accepted 24 Nov 2023). “Medulloblastoma and other neoplasms…” https://doi.org/10.1002/ajmg.a.63496 (lee2024medulloblastomaandother pages 1-2)
- Hansford et al. **Clin Cancer Res** (**Apr 2024**). “Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors.” https://doi.org/10.1158/1078-0432.CCR-23-4033 (hansford2024updateoncancer pages 3-4)
- Vallini et al. **Cells** (**Oct 2023**). “Signaling Pathways and Therapeutic Strategies in Advanced Basal Cell Carcinoma.” https://doi.org/10.3390/cells12212534 (vallini2023signalingpathwaysand pages 2-3)
- Murgia et al. **Cancers** (**Jun 2024**). “Gorlin Syndrome-Associated BCCs Treated with Vismodegib or Sonidegib.” https://doi.org/10.3390/cancers16122166 (murgia2024gorlinsyndromeassociatedbasal pages 5-7)
- Lang et al. **J Dtsch Dermatol Ges** (**Nov 2024**; guideline update 2023). “S2k guideline basal cell carcinoma…” https://doi.org/10.1111/ddg.15566 (lang2024s2kguidelinebasal pages 11-12)

---

### Notes on evidence gaps
- MONDO/Orphanet/MeSH/ICD identifiers were not available in the retrieved evidence and are not inferred.
- SUFU-specific frequencies for non-tumoral developmental features, QoL scales, and robust environmental risk quantification were not present in the accessed excerpts.


References

1. (guerrinirousseau2021currentrecommendationsfor pages 1-2): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

2. (guerrinirousseau2022cancerriskand pages 1-1): Léa Guerrini-Rousseau, Julien Masliah-Planchon, Sebastian M Waszak, Pia Alhopuro, Patrick R Benusiglio, Franck Bourdeaut, Ines B Brecht, Giada Del Baldo, Sandeep Kumar Dhanda, Maria Luisa Garrè, Corrie E M Gidding, Steffen Hirsch, Pauline Hoarau, Mette Jorgensen, Christian Kratz, Lucie Lafay-Cousin, Angela Mastronuzzi, Lorenza Pastorino, Stefan M Pfister, Christopher Schroeder, Miriam Jane Smith, Pia Vahteristo, Roseline Vibert, Catheline Vilain, Nicolas Thomas Waespe Laredo, Ingrid M Winship, D Gareth Evans, and Laurence Brugieres. Cancer risk and tumour spectrum in 172 patients with a germline sufu pathogenic variation: a collaborative study of the siope host genome working group. Journal of Medical Genetics, 59:1123-1132, Jun 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108385, doi:10.1136/jmedgenet-2021-108385. This article has 18 citations and is from a domain leading peer-reviewed journal.

3. (lee2024medulloblastomaandother pages 1-2): Stephanie G. Lee, Gareth Evans, Maddie Stephen, Rachel Goren, Melissa Bondy, and Steven Goodman. Medulloblastoma and other neoplasms in patients with heterozygous germline sufu variants: a scoping review. American Journal of Medical Genetics Part A, Jan 2024. URL: https://doi.org/10.1002/ajmg.a.63496, doi:10.1002/ajmg.a.63496. This article has 10 citations.

4. (lee2024medulloblastomaandother pages 2-2): Stephanie G. Lee, Gareth Evans, Maddie Stephen, Rachel Goren, Melissa Bondy, and Steven Goodman. Medulloblastoma and other neoplasms in patients with heterozygous germline sufu variants: a scoping review. American Journal of Medical Genetics Part A, Jan 2024. URL: https://doi.org/10.1002/ajmg.a.63496, doi:10.1002/ajmg.a.63496. This article has 10 citations.

5. (hansford2024updateoncancer pages 3-4): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 49 citations.

6. (NCT01350115 chunk 1):  Efficacy, Safety and Pharmacokinetics of Oral LDE225 in Treatment of Patients With Nevoid Basal Cell Carcinoma Syndrome (NBCCS). Novartis Pharmaceuticals. 2011. ClinicalTrials.gov Identifier: NCT01350115

7. (NCT00957229 chunk 1):  To Determine The Efficacy and Safety of GDC-0449 in Patients With Basal Cell Nevus Syndrome (BCNS). UCSF Benioff Children's Hospital Oakland. 2009. ClinicalTrials.gov Identifier: NCT00957229

8. (NCT00961896 chunk 1):  A Trial to Evaluate the Safety, Local Tolerability, Pharmacokinetics and Pharmacodynamics of LDE225 on Skin Basal Cell Carcinomas in Gorlin Syndrome Patients. Novartis Pharmaceuticals. 2009. ClinicalTrials.gov Identifier: NCT00961896

9. (vallini2023signalingpathwaysand pages 2-3): Giulia Vallini, Laura Calabrese, Costanza Canino, Emanuele Trovato, Stefano Gentileschi, Pietro Rubegni, and Linda Tognetti. Signaling pathways and therapeutic strategies in advanced basal cell carcinoma. Cells, 12:2534, Oct 2023. URL: https://doi.org/10.3390/cells12212534, doi:10.3390/cells12212534. This article has 13 citations.

10. (hoashi2022molecularmechanismsand pages 3-5): Toshihiko Hoashi, Naoko Kanda, and Hidehisa Saeki. Molecular mechanisms and targeted therapies of advanced basal cell carcinoma. International Journal of Molecular Sciences, 23:11968, Oct 2022. URL: https://doi.org/10.3390/ijms231911968, doi:10.3390/ijms231911968. This article has 28 citations.

11. (guerrinirousseau2022cancerriskand pages 6-7): Léa Guerrini-Rousseau, Julien Masliah-Planchon, Sebastian M Waszak, Pia Alhopuro, Patrick R Benusiglio, Franck Bourdeaut, Ines B Brecht, Giada Del Baldo, Sandeep Kumar Dhanda, Maria Luisa Garrè, Corrie E M Gidding, Steffen Hirsch, Pauline Hoarau, Mette Jorgensen, Christian Kratz, Lucie Lafay-Cousin, Angela Mastronuzzi, Lorenza Pastorino, Stefan M Pfister, Christopher Schroeder, Miriam Jane Smith, Pia Vahteristo, Roseline Vibert, Catheline Vilain, Nicolas Thomas Waespe Laredo, Ingrid M Winship, D Gareth Evans, and Laurence Brugieres. Cancer risk and tumour spectrum in 172 patients with a germline sufu pathogenic variation: a collaborative study of the siope host genome working group. Journal of Medical Genetics, 59:1123-1132, Jun 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108385, doi:10.1136/jmedgenet-2021-108385. This article has 18 citations and is from a domain leading peer-reviewed journal.

12. (guerrinirousseau2021currentrecommendationsfor pages 2-4): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

13. (lang2024s2kguidelinebasal pages 11-12): Berenice M. Lang, Panagiotis Balermpas, Andrea Bauer, Andreas Blum, Thomas Dirschka, Markus Follmann, Jorge Frank, Bernhard Frerich, Klaus Fritz, Axel Hauschild, Ludwig M. Heindl, Hans‐Peter Howaldt, Stephan Ihrler, Vinodh Kakkassery, Bernhard Klumpp, Albrecht Krause‐Bergmann, Christoph Löser, Markus Meissner, Michael M. Sachse, Max Schlaak, Michael P. Schön, Lutz Tischendorf, Michael Tronnier, Dirk Vordermark, Julia Welzel, Michael Weichenthal, Susanne Wiegand, Roland Kaufmann, and Stephan Grabbe. S2k guideline basal cell carcinoma of the skin (update 2023). Journal Der Deutschen Dermatologischen Gesellschaft, 22:1697-1714, Nov 2024. URL: https://doi.org/10.1111/ddg.15566, doi:10.1111/ddg.15566. This article has 10 citations and is from a peer-reviewed journal.

14. (murgia2024gorlinsyndromeassociatedbasal pages 2-4): Giulia Murgia, Luca Valtellini, Nerina Denaro, Gianluca Nazzaro, Paolo Bortoluzzi, Valentina Benzecry, Emanuela Passoni, and Angelo Valerio Marzano. Gorlin syndrome-associated basal cell carcinomas treated with vismodegib or sonidegib: a retrospective study. Cancers, 16:2166, Jun 2024. URL: https://doi.org/10.3390/cancers16122166, doi:10.3390/cancers16122166. This article has 15 citations.

15. (taylor2002mutationsinsufu pages 1-2): Michael D. Taylor, Ling Liu, Corey Raffel, Chi-chung Hui, Todd G. Mainprize, Xiaoyun Zhang, Ron Agatep, Sharon Chiappa, Luzhang Gao, Anja Lowrance, Aihau Hao, Alisa M. Goldstein, Theodora Stavrou, Stephen W. Scherer, Wieslaw T. Dura, Brandon Wainwright, Jeremy A. Squire, James T. Rutka, and David Hogg. Mutations in sufu predispose to medulloblastoma. Nature Genetics, 31:306-310, Jun 2002. URL: https://doi.org/10.1038/ng916, doi:10.1038/ng916. This article has 1053 citations and is from a highest quality peer-reviewed journal.

16. (han2024increasingsufugene pages 1-2): Boang Han, Yu Wang, Shen Yue, Yun-hao Zhang, Lun Kuang, Bin-bin Gao, Yue Wang, Ziyu Zhang, Xiaohong Pu, Xin-fa Wang, Chi-chung Hui, Ting-ting Yu, Chen Liu, and Steven Y. Cheng. Increasing sufu gene dosage reveals its unorthodox role in promoting polydactyly and medulloblastoma tumorigenesis. JCI Insight, Feb 2024. URL: https://doi.org/10.1172/jci.insight.176044, doi:10.1172/jci.insight.176044. This article has 3 citations and is from a domain leading peer-reviewed journal.

17. (guerrinirousseau2022cancerriskand pages 7-8): Léa Guerrini-Rousseau, Julien Masliah-Planchon, Sebastian M Waszak, Pia Alhopuro, Patrick R Benusiglio, Franck Bourdeaut, Ines B Brecht, Giada Del Baldo, Sandeep Kumar Dhanda, Maria Luisa Garrè, Corrie E M Gidding, Steffen Hirsch, Pauline Hoarau, Mette Jorgensen, Christian Kratz, Lucie Lafay-Cousin, Angela Mastronuzzi, Lorenza Pastorino, Stefan M Pfister, Christopher Schroeder, Miriam Jane Smith, Pia Vahteristo, Roseline Vibert, Catheline Vilain, Nicolas Thomas Waespe Laredo, Ingrid M Winship, D Gareth Evans, and Laurence Brugieres. Cancer risk and tumour spectrum in 172 patients with a germline sufu pathogenic variation: a collaborative study of the siope host genome working group. Journal of Medical Genetics, 59:1123-1132, Jun 2022. URL: https://doi.org/10.1136/jmedgenet-2021-108385, doi:10.1136/jmedgenet-2021-108385. This article has 18 citations and is from a domain leading peer-reviewed journal.

18. (guerrinirousseau2021currentrecommendationsfor pages 4-5): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

19. (murgia2024gorlinsyndromeassociatedbasal pages 5-7): Giulia Murgia, Luca Valtellini, Nerina Denaro, Gianluca Nazzaro, Paolo Bortoluzzi, Valentina Benzecry, Emanuela Passoni, and Angelo Valerio Marzano. Gorlin syndrome-associated basal cell carcinomas treated with vismodegib or sonidegib: a retrospective study. Cancers, 16:2166, Jun 2024. URL: https://doi.org/10.3390/cancers16122166, doi:10.3390/cancers16122166. This article has 15 citations.

20. (vallini2023signalingpathwaysand pages 6-7): Giulia Vallini, Laura Calabrese, Costanza Canino, Emanuele Trovato, Stefano Gentileschi, Pietro Rubegni, and Linda Tognetti. Signaling pathways and therapeutic strategies in advanced basal cell carcinoma. Cells, 12:2534, Oct 2023. URL: https://doi.org/10.3390/cells12212534, doi:10.3390/cells12212534. This article has 13 citations.

21. (guerrinirousseau2021currentrecommendationsfor media 7a72a3c0): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

22. (lee2024medulloblastomaandother pages 16-16): Stephanie G. Lee, Gareth Evans, Maddie Stephen, Rachel Goren, Melissa Bondy, and Steven Goodman. Medulloblastoma and other neoplasms in patients with heterozygous germline sufu variants: a scoping review. American Journal of Medical Genetics Part A, Jan 2024. URL: https://doi.org/10.1002/ajmg.a.63496, doi:10.1002/ajmg.a.63496. This article has 10 citations.

23. (lee2024medulloblastomaandother pages 14-14): Stephanie G. Lee, Gareth Evans, Maddie Stephen, Rachel Goren, Melissa Bondy, and Steven Goodman. Medulloblastoma and other neoplasms in patients with heterozygous germline sufu variants: a scoping review. American Journal of Medical Genetics Part A, Jan 2024. URL: https://doi.org/10.1002/ajmg.a.63496, doi:10.1002/ajmg.a.63496. This article has 10 citations.

24. (hansford2024updateoncancer pages 2-3): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 49 citations.
