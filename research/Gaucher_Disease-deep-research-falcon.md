---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:15.111798'
end_time: '2026-04-25T22:33:46.418270'
duration_seconds: 1111.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gaucher Disease
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
- **Disease Name:** Gaucher Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Gaucher Disease** covering all of the
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
- **Disease Name:** Gaucher Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Gaucher Disease** covering all of the
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


## Comprehensive Research Report: Gaucher Disease (Genetic)

### Target disease
- **Disease name:** Gaucher disease
- **MONDO ID:** **MONDO_0018150** (from OpenTargets disease mapping) (carubbi2026glucosylsphingosine(lysogb1)an pages 1-2)
- **Category:** Genetic (autosomal recessive lysosomal storage disorder) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, rossi2023noninvasivedbsbasedapproaches pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview
Gaucher disease (GD) is a lysosomal storage disorder caused by deficient activity of lysosomal **acid β-glucosidase / glucocerebrosidase (GCase)**, leading to lysosomal accumulation of **glucosylceramide (GlcCer)** and its deacylated derivative **glucosylsphingosine (GlcSph; lyso‑Gb1)**, particularly in macrophages, resulting in multi-organ disease (visceral, hematologic, skeletal; and sometimes neurologic) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, rossi2023noninvasivedbsbasedapproaches pages 1-2, dardis2022patientcenteredguidelines pages 1-2).

**Clinical types (classical):**
- **Type 1 (GD1):** non-neuronopathic; accounts for ~90–95% of cases (cojbasicUnknownyeardiagnosisandmanagement pages 5-8, rossi2023noninvasivedbsbasedapproaches pages 1-2).
- **Type 2 (GD2):** acute neuronopathic; rare, often fatal in early childhood (cojbasicUnknownyeardiagnosisandmanagement pages 5-8).
- **Type 3 (GD3):** chronic neuronopathic; less common than GD1 (cojbasicUnknownyeardiagnosisandmanagement pages 5-8).

### 1.2 Key identifiers and controlled vocabulary
- **MONDO:** MONDO_0018150 (carubbi2026glucosylsphingosine(lysogb1)an pages 1-2)
- **OMIM (clinical types):**
  - GD1: **230800**
  - GD2: **230900**
  - GD3: **231000** (carubbi2026glucosylsphingosine(lysogb1)an pages 1-2)
- **MeSH:** **D005776** (“Gaucher Disease”) (from ClinicalTrials.gov browse module) (NCT07223944 chunk 1, NCT05324943 chunk 1).
- **Orphanet, ICD‑10, ICD‑11:** Not explicitly present in the retrieved full-text excerpts/trial records; therefore not asserted here.

### 1.3 Common synonyms / alternative names (as used in retrieved sources)
- Gaucher disease; **GD** (rossi2023noninvasivedbsbasedapproaches pages 1-2)
- Gaucher disease **type 1/2/3**; **GD1/GD2/GD3** (rossi2023noninvasivedbsbasedapproaches pages 1-2)
- “glucocerebrosidase deficiency” / “acid beta‑glucosidase deficiency” (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, dardis2022patientcenteredguidelines pages 1-2)

### 1.4 Evidence provenance (patient vs aggregated)
The information in this report is primarily derived from aggregated resources: international guideline synthesis (Dardis et al. 2022), narrative reviews (Giuffrida et al. 2023; Rossi et al. 2023), a population screening cohort (Chang et al. 2024), real-world registry analysis (GOS registry; Zimran et al. 2025), mechanistic animal-model work (Lin et al. 2024), and ClinicalTrials.gov trial records (chang2024newbornscreeningfor pages 1-2, dardis2022patientcenteredguidelines pages 8-9, zimran2025evaluationoflysogb1 pages 1-2, lin2024intrinsiclinkbetween pages 1-2, NCT05324943 chunk 1).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **GBA1** encoding GCase (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, dardis2022patientcenteredguidelines pages 1-2, dubiela2024longandshortterm pages 1-2).

**Important alternative genetic etiology (Gaucher-like biochemistry/phenotype):** If clinical/biochemical features are consistent with GD but **no pathogenic GBA1 variants** are found, international laboratory guidelines recommend considering **saposin C deficiency** and analyzing **PSAP** (prosaposin gene) (dardis2022patientcenteredguidelines pages 10-12).

### 2.2 Risk factors
- **Genetic:** biallelic pathogenic GBA1 variants are causal (dardis2022patientcenteredguidelines pages 1-2). The diagnostic guideline notes extensive allelic heterogeneity; HGMD lists **540 GBA1 variants**, with **403 associated with GD** (dardis2022patientcenteredguidelines pages 9-10).
- **Population ancestry:** incidence is higher in Ashkenazi Jewish populations (e.g., ~1 in 450–1,000 live births reported by a biomarker review) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2).

### 2.3 Protective factors
No protective genetic or environmental factors were explicitly identified in the retrieved excerpts.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction studies were identified in the retrieved excerpts. However, precision-genomics work argues that phenotypic heterogeneity may reflect **multi-locus** genetic contributions (saith2024concurrentgeneticdisorders pages 1-3, saith2025precisiongenomicprofiling pages 1-2).

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with approximate frequencies where available)
From a recent clinical summary excerpt, common clinical findings include:
- **Splenomegaly**: >90% (cojbasicUnknownyeardiagnosisandmanagement pages 5-8)
- **Hepatomegaly**: 60–80% (cojbasicUnknownyeardiagnosisandmanagement pages 5-8)
- **Thrombocytopenia**: ~90% (cojbasicUnknownyeardiagnosisandmanagement pages 5-8)
- **Anemia**: 30–50% (cojbasicUnknownyeardiagnosisandmanagement pages 5-8)
Skeletal involvement is common and may become irreversible if advanced (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, cojbasicUnknownyeardiagnosisandmanagement pages 5-8).

Neurologic involvement distinguishes GD2 (acute severe) and GD3 (chronic neuronopathic) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, rossi2023noninvasivedbsbasedapproaches pages 1-2).

### 3.2 Phenotype characteristics
- **Onset:** ranges from infancy (especially GD2) to adulthood; GD2 typically presents in the first year of life and may be fatal early (cojbasicUnknownyeardiagnosisandmanagement pages 5-8).
- **Progression:** variable; neurologic disease is progressive and generally not improved by current systemic therapies that do not cross the blood–brain barrier (kulkarni2024advancementsinviral pages 10-12, cojbasicUnknownyeardiagnosisandmanagement pages 5-8).

### 3.3 Quality-of-life impact
The retrieved excerpts do not provide standardized QoL instrument statistics (EQ‑5D/SF‑36). Bone disease and cytopenias plausibly drive morbidity, but such statements require additional QoL-specific sources.

### 3.4 Suggested HPO terms (examples)
Based on phenotypes explicitly discussed in retrieved sources:
- **Splenomegaly** (HP:0001744)
- **Hepatomegaly** (HP:0002240)
- **Thrombocytopenia** (HP:0001873)
- **Anemia** (HP:0001903)
- **Bone pain / skeletal dysplasia / osteonecrosis** (multiple; skeletal involvement is explicit but granular HPO mapping would require additional phenotype-specific papers) (cojbasicUnknownyeardiagnosisandmanagement pages 5-8, giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **GBA1** (glucosylceramidase beta 1; glucocerebrosidase) is causal; located near a highly homologous pseudogene, complicating molecular analysis (dardis2022patientcenteredguidelines pages 1-2, dardis2022patientcenteredguidelines pages 8-9).
- **PSAP** can be involved in saposin C deficiency when GD-like phenotype occurs without GBA1 variants (dardis2022patientcenteredguidelines pages 10-12).

### 4.2 Pathogenic variant spectrum and genotype–phenotype examples
- The laboratory guideline describes extensive allelic diversity and complex alleles arising from recombination with the pseudogene; ~10% may have large deletions/recombinants (dardis2022patientcenteredguidelines pages 9-10, dardis2022patientcenteredguidelines pages 8-9).
- Example genotype–phenotype relationships (from biomarker dynamics study):
  - **N370S (c.1226A>G; p.Asn409Ser)**: common; relatively protective of CNS involvement (dubiela2024longandshortterm pages 1-2).
  - **L444P (c.1448T>C; p.Leu483Pro)**: associated with neuronopathic disease in some contexts (e.g., GD3) (dubiela2024longandshortterm pages 1-2).

### 4.3 Modifier genes and “multi-locus” contributions (recent work)
**Mechanistic modifier evidence (animal model):**
- A 2024 mechanistic study reports that **progranulin (PGRN; GRN)** acts as a modifier of GCase biology and disease severity. In Grn−/− mice with graded **Gba1 D409V** dosages, higher mutant dosage produced earlier onset/shorter lifespan and more severe inflammation, lysosomal–autophagy dysfunction, gliosis, and α‑synuclein increases, supporting a threshold model for severity (lin2024intrinsiclinkbetween pages 1-2).

**Human cohort precision-genomics evidence:**
- In a deeply phenotyped cohort with WES, ~**6–6.5%** of GD patients had additional genetic diagnoses contributing to “expanded/atypical” phenotypes, suggesting that some GD presentations behave as multi-locus disorders (saith2024concurrentgeneticdisorders pages 3-5, saith2024concurrentgeneticdisorders pages 1-3).
  - Example cohort statistics: among 275 patients, 18 (6.5%) had expanded phenotypes (preprint) (saith2024concurrentgeneticdisorders pages 3-5) and 17 (6.2%) had atypical phenotypes (peer-reviewed version) (saith2025precisiongenomicprofiling pages 1-2).

### 4.4 Epigenetics / chromosomal abnormalities
No epigenetic or chromosomal-abnormality evidence was identified in the retrieved excerpts.

---

## 5. Environmental Information

No specific environmental, lifestyle, or infectious triggers were identified in the retrieved excerpts as causal contributors to GD. (GD is primarily genetic.)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current understanding)
1. **GBA1 pathogenic variants** → reduced/mislocalized **GCase activity** (dardis2022patientcenteredguidelines pages 1-2).
2. Impaired lysosomal degradation of **GlcCer → ceramide** → accumulation of **GlcCer** and **GlcSph (lyso‑Gb1)** (dardis2022patientcenteredguidelines pages 1-2, giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2).
3. Lipid-laden macrophages (“Gaucher cells”) infiltrate liver, spleen, bone marrow → organomegaly, cytopenias, and bone disease (rossi2023noninvasivedbsbasedapproaches pages 1-2, cojbasicUnknownyeardiagnosisandmanagement pages 5-8).
4. In neuronopathic forms and in modifier contexts, lysosomal dysfunction intersects with neuroinflammation, gliosis, autophagy disruption, and α‑synuclein pathology (lin2024intrinsiclinkbetween pages 1-2).

### 6.2 Molecular pathways / cellular processes (from retrieved mechanistic sources)
Precision-genomic and mechanistic sources emphasize lipid-driven metabolic inflammation and lysosome-autophagy disruption:
- “The accumulation of GlcCer and GlcSph in GD activates a range of pathways, including those involving **inflammasomes**, **iron metabolism**, **necroptosis**, **ferroptosis**, **lysosomal function**, **autophagy**, and **reactive oxygen species (ROS)**.” (Saith et al. 2024 preprint excerpt) (saith2024concurrentgeneticdisorders pages 11-13).
- PGRN/GRN modifier work demonstrates dose-dependent substrate accumulation, inflammatory responses, lysosomal–autophagy dysfunction, microgliosis, and α‑synuclein increases in mouse models (lin2024intrinsiclinkbetween pages 1-2).

### 6.3 Suggested ontology terms
- **GO Biological Process (examples):** lysosomal organization; sphingolipid catabolic process; macrophage activation; autophagy; inflammatory response.
- **CL (cell types):** macrophage (Gaucher cell is macrophage-derived); microglia (in neuronopathic/mechanistic models) (rossi2023noninvasivedbsbasedapproaches pages 1-2, lin2024intrinsiclinkbetween pages 1-2).

---

## 7. Anatomical Structures Affected

### 7.1 Organ level (commonly affected)
- **Spleen, liver, bone marrow, bone** are repeatedly highlighted as key sites of lipid accumulation and clinical disease (rossi2023noninvasivedbsbasedapproaches pages 1-2, cojbasicUnknownyeardiagnosisandmanagement pages 5-8, dardis2022patientcenteredguidelines pages 1-2).
- Neurologic involvement (brain) defines GD2/GD3 and is a major unmet-need domain for therapies (kulkarni2024advancementsinviral pages 10-12, NCT06272149 chunk 1).

### 7.2 Tissue/cell level
- Primary disease cell type: **macrophages** (lipid-laden Gaucher cells) (rossi2023noninvasivedbsbasedapproaches pages 1-2).
- In neuronopathic pathology and modifier models: **microglia** and neurons are implicated through neuroinflammation and neurodegeneration pathways (lin2024intrinsiclinkbetween pages 1-2).

### 7.3 Subcellular level
- **Lysosome** is the core compartment of dysfunction; impaired lysosomal trafficking/delivery of GCase and lysosomal lipid accumulation are central (dardis2022patientcenteredguidelines pages 1-2, lin2024intrinsiclinkbetween pages 1-2).

### 7.4 Suggested UBERON terms (examples)
- Spleen; liver; bone marrow; brain.

---

## 8. Temporal Development

- **Onset:** can be pediatric or adult depending on subtype and genotype (cojbasicUnknownyeardiagnosisandmanagement pages 5-8).
- **Progression:** variable; neurologic forms are progressive and currently poorly addressed by standard ERT/SRT (kulkarni2024advancementsinviral pages 10-12, cojbasicUnknownyeardiagnosisandmanagement pages 5-8).

---

## 9. Inheritance and Population

### 9.1 Inheritance pattern
- **Autosomal recessive** (GD is repeatedly described as such) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, rossi2023noninvasivedbsbasedapproaches pages 1-2, dardis2022patientcenteredguidelines pages 1-2).

### 9.2 Epidemiology (key recent/reviewed statistics)
Estimates vary across sources and populations:
- General population incidence reported as ~**1/40,000–1/60,000** (review) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2) and GD1 incidence **~1/40,000–1/86,000** in non-Jewish populations (review) (rossi2023noninvasivedbsbasedapproaches pages 1-2).
- In Ashkenazi Jews, incidence reported as ~**1/450–1,000** live births (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2) and also ~**1 in 850** in one registry-based review excerpt (zimran2025evaluationoflysogb1 pages 1-2).
- Reported overall incidence range: **0.4–5.8 per 100,000 births** and prevalence **0.7–1.8 per 100,000** (review) (rossi2023noninvasivedbsbasedapproaches pages 1-2).

### 9.3 Newborn screening (2024 data)
A 2024 Shanghai cohort screened **50,108** newborns for 6 LSDs by MS/MS on DBS and confirmed **2 Gaucher** diagnoses among **27** total LSD diagnoses; the combined 6-LSD birth prevalence was **1 in 1,856** live births, with **11.1%** early-onset and **88.9%** later-onset/subclinical forms among confirmed LSDs (chang2024newbornscreeningfor pages 1-2). This supports real-world feasibility of large-scale screening but Gaucher-specific precision is limited by the small number of Gaucher cases in this combined assay (chang2024newbornscreeningfor pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical tests and laboratory confirmation
**Core principle (guideline-level):** GD diagnosis requires biochemical demonstration of deficient GCase/BGLU activity and confirmatory molecular testing where possible (dardis2022patientcenteredguidelines pages 1-2, dardis2022patientcenteredguidelines pages 8-9).

**Gold-standard specimens:** peripheral blood **leukocytes** and/or cultured **skin fibroblasts** (dardis2022patientcenteredguidelines pages 7-8, dardis2022patientcenteredguidelines pages 8-9).

**DBS (dried blood spot):** recommended as a **first-line screen**, but any low activity result must be confirmed in leukocytes/fibroblasts; DBS BGLU testing has low positive predictive value and should not be used alone for diagnosis (dardis2022patientcenteredguidelines pages 7-8, dardis2022patientcenteredguidelines pages 10-12).

**Diagnostic enzyme-activity threshold:** **<15% of normal** in leukocyte/fibroblast homogenates is diagnostic (dardis2022patientcenteredguidelines pages 7-8, dardis2022patientcenteredguidelines pages 8-9).

**Abstract-supported quote (guideline):** Dardis et al. emphasize that “Gaucher disease (GD) is an autosomal recessive lysosomal storage disorder due to the deficient activity of the acid beta-glucosidase (GCase) enzyme, resulting in the progressive lysosomal accumulation of glucosylceramide (GlcCer) and its deacylated derivate, glucosylsphingosine (GlcSph).” (dardis2022patientcenteredguidelines pages 1-2).

### 10.2 Biomarkers
**Lyso‑Gb1 (GlcSph):**
- Widely characterized as a highly sensitive and specific biomarker for diagnosis and treatment monitoring (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2, zimran2025evaluationoflysogb1 pages 1-2).
- Treatment decision support: a cohort study found a DBS lyso‑Gb1 **cutoff >250 ng/mL** was associated with initiation of GD-specific therapy (sensitivity 71%, specificity 87.5%), with treated patients showing higher median lyso‑Gb1 than untreated at diagnosis (dinur2023contributionofglucosylsphingosine pages 6-7).
- Treatment monitoring dynamics:
  - Short-term: average **17% decrease** 30 minutes after ERT infusion in 20 patients (dubiela2024longandshortterm pages 1-2).
  - Longitudinal: real-world registry analysis shows median change **−8.6 ng/mL** in treated vs **+25.0 ng/mL** untreated, and **+19.5 ng/mL** in those stopping treatment (zimran2025evaluationoflysogb1 pages 1-2).

**Chitotriosidase:** useful but lacks specificity and is confounded by common CHIT1 loss-of-function duplication; guideline notes interpretive complications (dardis2022patientcenteredguidelines pages 4-5, dubiela2024longandshortterm pages 1-2).

### 10.3 Genetic testing strategy (implementation considerations)
Guideline highlights:
- GBA1 testing is complicated by a highly homologous pseudogene and recombinant alleles; some methods miss large deletions/recombinants; enzymatic confirmation is mandatory when variants of uncertain significance occur (dardis2022patientcenteredguidelines pages 8-9, dardis2022patientcenteredguidelines pages 9-10).
- If GD phenotype/biochemistry but no GBA1 variants: consider PSAP/saposin C deficiency (dardis2022patientcenteredguidelines pages 10-12).

---

## 11. Outcome / Prognosis

The retrieved excerpts do not provide modern, quantitative survival curves stratified by treatment era. They do note that ERT/SRT improved visceral/hematologic disease (especially GD1), while neuronopathic manifestations remain largely unresponsive to standard systemic therapies (kulkarni2024advancementsinviral pages 10-12, cojbasicUnknownyeardiagnosisandmanagement pages 5-8).

---

## 12. Treatment

### 12.1 Standard disease-specific therapy (real-world implementation)
**Enzyme replacement therapy (ERT):** long-established cornerstone, generally effective for visceral and hematologic manifestations in GD1, but limited for neurologic disease (blood–brain barrier) (kulkarni2024advancementsinviral pages 10-12, giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2).
- A review excerpt reports typical dosing **15–120 units/kg every 2 weeks**, with most clinical/lab/radiologic improvements within ~6 months (except irreversible skeletal disease) (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2).

**Substrate reduction therapy (SRT):** improves visceral/hematologic manifestations and is used in adults with GD1; does not address CNS disease adequately (kulkarni2024advancementsinviral pages 10-12).

### 12.2 Biomarker-informed management
Lyso‑Gb1 is increasingly used to guide treatment decisions and monitor therapy response, including identifying when treatment may be indicated among mildly affected patients and detecting response after starting or stopping ERT (dinur2023contributionofglucosylsphingosine pages 6-7, zimran2025evaluationoflysogb1 pages 1-2).

### 12.3 Emerging/advanced therapeutics (2023–2024 prioritized)
**Rationale:** current ERT/SRT do not cross the blood–brain barrier and do not improve neuronopathic manifestations, motivating gene therapy strategies (kulkarni2024advancementsinviral pages 10-12).

#### AAV liver-directed gene therapy (GD1)
- **FLT201 (GALILEO-1; NCT05324943)**: Phase 1, completed; single IV infusion of replication-incompetent ssAAV; n=6 adults with GD1; primary outcome TEAEs through Week 38 (ClinicalTrials.gov) (NCT05324943 chunk 1).
- **FLT201 (GALILEO-3; NCT07223944)**: Phase 3, recruiting; single IV infusion; n=45 planned; evaluates stable hemoglobin at Week 52 after discontinuation of ERT/SRT (ClinicalTrials.gov) (NCT07223944 chunk 1).

#### AAV systemic gene therapy targeting peripheral disease (GD/GD1)
- **LY3884961 / PR001 (PROCEED; NCT05487599)**: Phase 1/2, recruiting; single IV dose; outcomes include safety, spleen volume, platelets, GCase levels, GlcSph levels, and ability to discontinue/reinitiate ERT/SRT (ClinicalTrials.gov) (NCT05487599 chunk 1).

#### CNS-directed gene therapy for neuronopathic GD2
- **VGN-R08b (NCT06272149)**: Early Phase 1, recruiting; AAV9-human GBA1 delivered intracerebroventricularly in infants ≤24 months; endpoints include safety and survival at 24 months, plus GCase activity and Lyso‑GL1 in blood/CSF (ClinicalTrials.gov) (NCT06272149 chunk 1).

#### Ex vivo autologous HSC lentiviral gene therapy
- **AVR‑RD‑02 (Guard1; NCT04145037)**: Phase 1/2, terminated voluntarily (not for safety/medical reasons). Product is autologous CD34+ HSCs modified ex vivo by lentiviral vector encoding codon-optimized GCase, with busulfan conditioning (ClinicalTrials.gov) (NCT04145037 chunk 1).

**Visual evidence note:** Kulkarni et al. 2024 summarize multiple current clinical trials and identifiers in a dedicated section; the retrieved cropped images support these program listings (kulkarni2024advancementsinviral media cabb2850, kulkarni2024advancementsinviral media 3ff0cbdf).

### 12.4 Suggested MAXO terms (examples)
- Enzyme replacement therapy
- Substrate reduction therapy
- Gene therapy
- Hematopoietic stem cell transplantation / autologous HSC gene therapy

---

## 13. Prevention

### 13.1 Primary prevention
Not applicable in the classic sense for a Mendelian recessive disorder, but reproductive and carrier-screening strategies are relevant.

### 13.2 Secondary prevention (early detection)
**Newborn screening:** MS/MS-based screening with confirmatory biochemical/genetic testing can identify affected newborns, including later-onset forms; 2024 Shanghai data demonstrate implementation at scale (chang2024newbornscreeningfor pages 1-2).

### 13.3 Genetic counseling
The laboratory guideline emphasizes genetic testing as the most reliable method to identify carriers and recommends pre/post-test genetic counseling (dardis2022patientcenteredguidelines pages 8-9, dardis2022patientcenteredguidelines pages 9-10).

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary Gaucher disease evidence was identified in the retrieved excerpts.

---

## 15. Model Organisms

Mechanistic and therapeutic-development work relies heavily on **mouse models** of GD, including modifier models and neuronopathic models. A 2024 mechanistic study used genetically engineered mouse models combining PGRN deficiency with graded Gba1 D409V dosages to demonstrate threshold-like effects on severity, neuroinflammation, lysosome-autophagy dysfunction, and α‑synuclein accumulation (lin2024intrinsiclinkbetween pages 1-2).

---

## Recent developments (2023–2024 emphasis) and real-world applications (high-yield highlights)

1. **Biomarker maturation into clinical decision support:** A 2023 cohort study proposed DBS lyso‑Gb1 **>250 ng/mL** as associated with initiation of GD-specific therapy among newly diagnosed patients, with ROC-derived **71% sensitivity / 87.5% specificity**, while cautioning about inter-laboratory variability (dinur2023contributionofglucosylsphingosine pages 6-7).
2. **Real-world monitoring feasibility:** Registry analysis using DBS lyso‑Gb1 showed treatment initiation or withdrawal produced directionally consistent biomarker changes in hundreds of adults, supporting routine monitoring in practice (zimran2025evaluationoflysogb1 pages 1-2).
3. **Population-scale screening implementation (2024):** Shanghai MS/MS NBS screened >50k newborns and confirmed 2 Gaucher diagnoses within a 6-LSD panel, while highlighting that most confirmed LSD cases were later-onset/subclinical forms, informing counseling/management (chang2024newbornscreeningfor pages 1-2).
4. **Acceleration of gene therapy pipelines:** A 2024 gene-therapy review documents multiple ongoing AAV and lentiviral programs and emphasizes the central limitation of standard therapies for neuronopathic disease due to blood–brain barrier constraints (kulkarni2024advancementsinviral pages 10-12, kulkarni2024advancementsinviral media cabb2850).

---

## Evidence summary table

| Topic | Key findings | Evidence type | Source (first author, year, journal or registry) | Publication date | URL | PMID | Notes |
|---|---|---|---|---|---|---|---|
| Diagnostics / genetics | International Working Group guideline: fluorometric leukocyte/fibroblast GCase assay is gold standard; DBS may be used first-line for screening but must be confirmed in leukocytes or fibroblasts; **enzyme activity <15% of normal** in leukocyte/fibroblast homogenates is diagnostic; **>400 pathogenic GBA1 variants** reported in abstract/background and **540 variants (403 GD-associated)** noted in guideline text; GBA1 testing is complicated by a highly homologous pseudogene and recombinant alleles; ~**10%** of patients may carry large deletions/recombinant alleles; two diagnostic algorithms provided (dardis2022patientcenteredguidelines pages 8-9, dardis2022patientcenteredguidelines pages 9-10, dardis2022patientcenteredguidelines pages 1-2, dardis2022patientcenteredguidelines pages 7-8) | Guideline | Dardis, 2022, *Orphanet Journal of Rare Diseases* | Dec 2022 | https://doi.org/10.1186/s13023-022-02573-6 | not in retrieved text | Important limitation: DBS BGLU has poor positive predictive value and cannot stand alone for diagnosis; variants should be ACMG-classified; consider **PSAP/saposin C deficiency** if phenotype/biochemistry fit but GBA1 is negative (dardis2022patientcenteredguidelines pages 8-9, dardis2022patientcenteredguidelines pages 10-12) |
| Biomarkers / epidemiology / treatment | Lyso-Gb1 review: GD incidence estimated **~1/450–1,000 live births in Ashkenazi Jews**, **~1/40,000–60,000** in general population; North-East Italy newborn-screening estimate **1/16,063**; ERT typically **15–120 U/kg every 2 weeks**; lyso-Gb1 described as the most promising biomarker with higher sensitivity/specificity than chitotriosidase (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2) | Review | Giuffrida, 2023, *Orphanet Journal of Rare Diseases* | Feb 2023 | https://doi.org/10.1186/s13023-023-02623-7 | not in retrieved text | Narrative review; stresses biomarker utility but exact cross-lab cutoffs vary (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2) |
| Biomarkers / treatment decision | Retrospective cohort of **97** newly diagnosed patients: **65** started GD-specific therapy; median lyso-Gb1 **337 ng/mL** in treated vs **153.5 ng/mL** in untreated; proposed DBS **cutoff >250 ng/mL** associated with treatment initiation with **71% sensitivity** and **87.5% specificity** (dinur2023contributionofglucosylsphingosine pages 6-7) | Cohort study | Dinur, 2023, *International Journal of Molecular Sciences* | Feb 2023 | https://doi.org/10.3390/ijms24043945 | not in retrieved text | Authors caution that inter-laboratory methodology/units prevent direct universal adoption of this exact cutoff (dinur2023contributionofglucosylsphingosine pages 6-7) |
| Diagnostics / epidemiology / newborn screening | DBS-centered review/case-based report: incidence **0.4–5.8 per 100,000 births**, prevalence **0.7–1.8 per 100,000**; GD1 about **90%** of cases; GD1 incidence in non-Jewish populations **~1/40,000–1/86,000**, GD2 **~1/150,000**, GD3 **~1/200,000**; tissue glycolipids may rise **20–100×**; illustrates first- and second-tier DBS workflow with low GCase and elevated lyso-Gb1 followed by molecular confirmation (rossi2023noninvasivedbsbasedapproaches pages 1-2) | Review / case-based diagnostic report | Rossi, 2023, *Biomedicines* | Sep 2023 | https://doi.org/10.3390/biomedicines11102672 | not in retrieved text | Useful for NBS-style workflows; not a population screening program outcome paper for GD alone (rossi2023noninvasivedbsbasedapproaches pages 1-2, rossi2023noninvasivedbsbasedapproaches pages 10-11) |
| Biomarkers / treatment monitoring | Eight-year ERT biomarker dynamics: GD1 coefficient of variation **34%** vs GD3 **23%** (**p=0.0003**); in short-term testing, lyso-Gb1 fell by **17% within 30 min post-ERT** (**p<0.0001**) in **20** patients; prior data summarized in paper show lyso-Gb1 can fall from median **~200 ng/mL pre-ERT to <50 ng/mL** after ERT (dubiela2024longandshortterm pages 1-2) | Observational biomarker study | Dubiela, 2024, *Biomolecules* | Jul 2024 | https://doi.org/10.3390/biom14070842 | not in retrieved text | Highlights substantial intra-individual/inter-infusion variability; DBS timing relative to infusion matters (dubiela2024longandshortterm pages 1-2) |
| Newborn screening / epidemiology | Shanghai cohort of **50,108** newborns screened for 6 LSDs by MS/MS on DBS: **353** screened positive; **27** confirmed LSDs (**1 in 1,856** live births overall), including **2 Gaucher** cases; among all LSD diagnoses, **3/27 (11.1%)** early-onset and **24/27 (88.9%)** later-onset/subclinical forms (chang2024newbornscreeningfor pages 1-2) | Cohort newborn-screening study | Chang, 2024, *JAMA Network Open* | May 13, 2024 | https://doi.org/10.1001/jamanetworkopen.2024.10754 | not in retrieved text | Combined 6-LSD study, so Gaucher-specific prevalence estimate is based on only 2 cases; still highly relevant for real-world NBS implementation (chang2024newbornscreeningfor pages 1-2) |
| Biomarkers / registry / treatment outcomes | Gaucher Outcome Survey real-world study: of **2,007** registry participants, **435** met inclusion criteria; median lyso-Gb1 change from baseline to last assessment: **−8.6 ng/mL** in treated, **+25.0 ng/mL** untreated, **+19.5 ng/mL** after stopping treatment; treatment-naive had **−120.5 ng/mL** vs previously treated **−3.3 ng/mL**; velaglucerase alfa subgroup **−32.6 ng/mL** (zimran2025evaluationoflysogb1 pages 1-2) | Registry study | Zimran, 2025, *Orphanet Journal of Rare Diseases* | Jan 2025 | https://doi.org/10.1186/s13023-024-03444-y | not in retrieved text | Strong real-world support for lyso-Gb1 as a treatment-response biomarker using DBS; observational, not randomized (zimran2025evaluationoflysogb1 pages 1-2) |
| Gene therapy / GD1 | **GALILEO-1** first-in-human study of **FLT201**: **NCT05324943**; Phase 1, open-label, single-group; **6** adults with GD1; single **intravenous** dose of a replication-incompetent **ssAAV** vector; primary outcome was treatment-emergent adverse events through Week 38; eligibility required stable ERT/SRT for at least 2 years and deficient GCase activity **≤30% of normal** at diagnosis (NCT05324943 chunk 1, kulkarni2024advancementsinviral media cabb2850) | Clinical trial record | ClinicalTrials.gov / Spur Therapeutics, NCT05324943 | First posted Apr 13, 2022; completed Dec 4, 2024 | https://clinicaltrials.gov/study/NCT05324943 | not in retrieved text | Focused on safety/tolerability plus GCase augmentation; excludes splenectomy and anti-AAVS3 neutralizing antibodies (NCT05324943 chunk 1) |
| Gene therapy / GD1 confirmatory study | **GALILEO-3** confirmatory FLT201 study: **NCT07223944**; Phase 3, non-randomized, single-group; estimated **45** adults with GD1 on stable ERT/SRT ≥2 years; single **intravenous** **ssAAV** FLT201 infusion; primary endpoint: proportion with stable hemoglobin (decrease **no more than 1.5 g/dL**) at Week 52 after discontinuing ERT/SRT (NCT07223944 chunk 1) | Clinical trial record | ClinicalTrials.gov / Spur Therapeutics, NCT07223944 | First posted Nov 3, 2025; recruiting as of Apr 21, 2026 | https://clinicaltrials.gov/study/NCT07223944 | not in retrieved text | Outside 2022–2025 publication window but highly relevant as latest implementation trajectory; MeSH term listed as **Gaucher Disease D005776** in record (NCT07223944 chunk 1) |
| Gene therapy / GD peripheral disease | **PROCEED**: **NCT05487599** of **LY3884961 (PR001)**; Phase 1/2, multicenter, open-label, dose-finding; estimated **15** adults; single **intravenous** dose of replication-incompetent recombinant **AAV**; outcomes include AEs, spleen volume, platelet count, GCase, **GlcSph**, and time to discontinuation/re-initiation of ERT/SRT over **5 years** (NCT05487599 chunk 1) | Clinical trial record | ClinicalTrials.gov / Prevail Therapeutics, NCT05487599 | First posted Aug 4, 2022; recruiting as of Apr 15, 2026 | https://clinicaltrials.gov/study/NCT05487599 | not in retrieved text | Requires centrally confirmed bi-allelic GBA1 variants and stable therapy; anti-AAV9 antibody titer must be **≤1:40** (NCT05487599 chunk 1) |
| Gene therapy / ex vivo HSC lentiviral | **Guard1**: **NCT04145037** of **AVR-RD-02**; Phase 1/2, multinational open-label study; actual enrollment **8**; intervention is **autologous CD34+ HSCs genetically modified ex vivo with lentiviral vector** encoding codon-optimized GCase, with busulfan conditioning; follow-up **52 weeks**; sponsor states termination was voluntary and **not based on safety or medical reasons** (NCT04145037 chunk 1) | Clinical trial record | ClinicalTrials.gov / AVROBIO, NCT04145037 | First posted Oct 30, 2019; results posted Jan 18, 2024 | https://clinicaltrials.gov/study/NCT04145037 | not in retrieved text | Important proof-of-concept for cell-based gene therapy; small sample, early termination limits efficacy interpretation (NCT04145037 chunk 1) |
| Gene therapy / neuronopathic GD2 | **VGN-R08b** exploratory trial: **NCT06272149**; Early Phase 1, single-center, open-label, dose-climbing/expansion; estimated **6** infants **≤24 months** with GD2; **AAV9-human GBA1** delivered by **intracerebroventricular injection**; primary endpoint AEs/SAEs at Week 52; secondary endpoints include survival at **24 months**, GCase activity, GC, and **Lyso-GL1 in blood and CSF**, plus immunogenicity (NCT06272149 chunk 1) | Clinical trial record | ClinicalTrials.gov / Xinhua Hospital, NCT06272149 | First posted Feb 22, 2024 | https://clinicaltrials.gov/study/NCT06272149 | not in retrieved text | Especially relevant for CNS-targeted therapy where ERT/SRT have limited neurologic benefit; excludes anti-AAV9 neutralizing antibody titer **>1:5** (NCT06272149 chunk 1) |


*Table: This table compiles recent high-yield evidence items for Gaucher disease across diagnostics, biomarkers, epidemiology, newborn screening, and emerging gene therapy. It is structured for direct use in a disease knowledge base and emphasizes quantitative thresholds, trial metadata, and implementation caveats.*

---

## Limitations of this report (due to retrieved-source constraints)
- **ICD‑10/ICD‑11 and Orphanet identifiers** were not explicitly present in the retrieved full text excerpts/trial records, and therefore were not asserted.
- **PMIDs** were not provided in the retrieved text chunks for several items (especially MDPI journals and ClinicalTrials.gov records); thus, PMID fields are marked “not in retrieved text” in the summary table.
- Some requested elements (e.g., standardized QoL statistics, comprehensive differential diagnosis lists, and detailed epigenetic profiling) require additional targeted retrieval beyond the current evidence set.


References

1. (carubbi2026glucosylsphingosine(lysogb1)an pages 1-2): Francesca Carubbi, Silvia Linari, and Marco Spada. Glucosylsphingosine (lyso-gb1): an update on its use as a biomarker in gaucher disease. International Journal of Molecular Sciences, 27:1705, Feb 2026. URL: https://doi.org/10.3390/ijms27041705, doi:10.3390/ijms27041705. This article has 2 citations.

2. (giuffrida2023glucosylsphingosine(lysogb1)as pages 1-2): Gaetano Giuffrida, Uros Markovic, Annalisa Condorelli, Valeria Calafiore, Daniela Nicolosi, Marianna Calagna, Stephanie Grasso, Marco Tindaro Valentino Ragusa, Jennifer Gentile, and Mariasanta Napolitano. Glucosylsphingosine (lyso-gb1) as a reliable biomarker in gaucher disease: a narrative review. Orphanet Journal of Rare Diseases, Feb 2023. URL: https://doi.org/10.1186/s13023-023-02623-7, doi:10.1186/s13023-023-02623-7. This article has 58 citations and is from a peer-reviewed journal.

3. (rossi2023noninvasivedbsbasedapproaches pages 1-2): Claudia Rossi, Rossella Ferrante, Silvia Valentinuzzi, Mirco Zucchelli, Carlotta Buccolini, Sara Di Rado, Daniela Trotta, Liborio Stuppia, Luca Federici, and Maurizio Aricò. Noninvasive dbs-based approaches to assist clinical diagnosis and treatment monitoring of gaucher disease. Biomedicines, 11:2672, Sep 2023. URL: https://doi.org/10.3390/biomedicines11102672, doi:10.3390/biomedicines11102672. This article has 12 citations.

4. (dardis2022patientcenteredguidelines pages 1-2): A. Dardis, H. Michelakakis, P. Rozenfeld, K. Fumic, J. Wagner, E. Pavan, M. Fuller, S. Revel-Vilk, D. Hughes, T. Cox, J. Aerts, and the International Working Group of Gaucher Disease. Patient centered guidelines for the laboratory diagnosis of gaucher disease type 1. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02573-6, doi:10.1186/s13023-022-02573-6. This article has 70 citations and is from a peer-reviewed journal.

5. (cojbasicUnknownyeardiagnosisandmanagement pages 5-8): I Ćojbašić. Diagnosis and management of gaucher disease: current approaches and emerging. Unknown journal, Unknown year.

6. (NCT07223944 chunk 1):  A Gaucher Disease Gene Therapy Trial With FLT201. Spur Therapeutics. 2026. ClinicalTrials.gov Identifier: NCT07223944

7. (NCT05324943 chunk 1):  A Gene Therapy Study in Patients With Gaucher Disease Type 1. Spur Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05324943

8. (chang2024newbornscreeningfor pages 1-2): Siyu Chang, Xia Zhan, Yuchao Liu, Huanlei Song, Zizhen Gong, Lianshu Han, Gustavo H. B. Maegawa, Xuefan Gu, and Huiwen Zhang. Newborn screening for 6 lysosomal storage disorders in china. JAMA Network Open, 7:e2410754, May 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.10754, doi:10.1001/jamanetworkopen.2024.10754. This article has 21 citations and is from a peer-reviewed journal.

9. (dardis2022patientcenteredguidelines pages 8-9): A. Dardis, H. Michelakakis, P. Rozenfeld, K. Fumic, J. Wagner, E. Pavan, M. Fuller, S. Revel-Vilk, D. Hughes, T. Cox, J. Aerts, and the International Working Group of Gaucher Disease. Patient centered guidelines for the laboratory diagnosis of gaucher disease type 1. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02573-6, doi:10.1186/s13023-022-02573-6. This article has 70 citations and is from a peer-reviewed journal.

10. (zimran2025evaluationoflysogb1 pages 1-2): Ari Zimran, Shoshana Revel-Vilk, Tama Dinur, Majdolen Istaiti, Jaco Botha, Elena Lukina, Pilar Giraldo, Patrick Deegan, and Stephan vom Dahl. Evaluation of lyso-gb1 as a biomarker for gaucher disease treatment outcomes using data from the gaucher outcome survey. Orphanet Journal of Rare Diseases, Jan 2025. URL: https://doi.org/10.1186/s13023-024-03444-y, doi:10.1186/s13023-024-03444-y. This article has 9 citations and is from a peer-reviewed journal.

11. (lin2024intrinsiclinkbetween pages 1-2): Yi Lin, Xiangli Zhao, Benjamin Liou, Venette Fannin, Wujuan Zhang, Kenneth D R Setchell, Xiaohong Wang, Dao Pan, Gregory A Grabowski, Chuan-ju Liu, and Ying Sun. Intrinsic link between pgrn and gba1 d409v mutation dosage in potentiating gaucher disease. Human molecular genetics, 33:1771-1788, Aug 2024. URL: https://doi.org/10.1093/hmg/ddae113, doi:10.1093/hmg/ddae113. This article has 6 citations and is from a domain leading peer-reviewed journal.

12. (dubiela2024longandshortterm pages 1-2): Pawel Dubiela, Paulina Szymanska-Rozek, Piotr Hasinski, Patryk Lipinski, Grazina Kleinotiene, Dorota Giersz, and Anna Tylki-Szymanska. Long- and short-term glucosphingosine (lyso-gb1) dynamics in gaucher patients undergoing enzyme replacement therapy. Biomolecules, 14:842, Jul 2024. URL: https://doi.org/10.3390/biom14070842, doi:10.3390/biom14070842. This article has 5 citations.

13. (dardis2022patientcenteredguidelines pages 10-12): A. Dardis, H. Michelakakis, P. Rozenfeld, K. Fumic, J. Wagner, E. Pavan, M. Fuller, S. Revel-Vilk, D. Hughes, T. Cox, J. Aerts, and the International Working Group of Gaucher Disease. Patient centered guidelines for the laboratory diagnosis of gaucher disease type 1. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02573-6, doi:10.1186/s13023-022-02573-6. This article has 70 citations and is from a peer-reviewed journal.

14. (dardis2022patientcenteredguidelines pages 9-10): A. Dardis, H. Michelakakis, P. Rozenfeld, K. Fumic, J. Wagner, E. Pavan, M. Fuller, S. Revel-Vilk, D. Hughes, T. Cox, J. Aerts, and the International Working Group of Gaucher Disease. Patient centered guidelines for the laboratory diagnosis of gaucher disease type 1. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02573-6, doi:10.1186/s13023-022-02573-6. This article has 70 citations and is from a peer-reviewed journal.

15. (saith2024concurrentgeneticdisorders pages 1-3): Armaan Saith, Jiapeng Ruan, Noor Ul Ain, Maniya Kasaiyan, Dhanpat Jain, Gary Israel, Sameet Mehta, Nigel S. Bamford, Shiny Nair, and Pramod K. Mistry. Concurrent genetic disorders in gaucher disease: insights into complex phenotypes, genetic modifiers, and targeted therapies. Unknown journal, Dec 2024. URL: https://doi.org/10.20944/preprints202412.1836.v1, doi:10.20944/preprints202412.1836.v1.

16. (saith2025precisiongenomicprofiling pages 1-2): Armaan Saith, Noor Ul Ain, Jiapeng Ruan, Maniya Kasaiyan, Dhanpat Jain, Gary Israel, Sameet Mehta, Nigel S. Bamford, Shiny Nair, and Pramod K. Mistry. Precision genomic profiling in gaucher disease: insights from atypical presentations. Frontiers in Genetics, Nov 2025. URL: https://doi.org/10.3389/fgene.2025.1553036, doi:10.3389/fgene.2025.1553036. This article has 0 citations and is from a peer-reviewed journal.

17. (kulkarni2024advancementsinviral pages 10-12): Akhil Kulkarni, Tiffany Chen, Ellen Sidransky, and Tae-Un Han. Advancements in viral gene therapy for gaucher disease. Genes, 15:364, Mar 2024. URL: https://doi.org/10.3390/genes15030364, doi:10.3390/genes15030364. This article has 16 citations.

18. (saith2024concurrentgeneticdisorders pages 3-5): Armaan Saith, Jiapeng Ruan, Noor Ul Ain, Maniya Kasaiyan, Dhanpat Jain, Gary Israel, Sameet Mehta, Nigel S. Bamford, Shiny Nair, and Pramod K. Mistry. Concurrent genetic disorders in gaucher disease: insights into complex phenotypes, genetic modifiers, and targeted therapies. Unknown journal, Dec 2024. URL: https://doi.org/10.20944/preprints202412.1836.v1, doi:10.20944/preprints202412.1836.v1.

19. (saith2024concurrentgeneticdisorders pages 11-13): Armaan Saith, Jiapeng Ruan, Noor Ul Ain, Maniya Kasaiyan, Dhanpat Jain, Gary Israel, Sameet Mehta, Nigel S. Bamford, Shiny Nair, and Pramod K. Mistry. Concurrent genetic disorders in gaucher disease: insights into complex phenotypes, genetic modifiers, and targeted therapies. Unknown journal, Dec 2024. URL: https://doi.org/10.20944/preprints202412.1836.v1, doi:10.20944/preprints202412.1836.v1.

20. (NCT06272149 chunk 1):  An Exploratory Clinical Trial of VGN-R08b in Patients With Type II Gaucher Disease. Xinhua Hospital, Shanghai Jiao Tong University School of Medicine. 2023. ClinicalTrials.gov Identifier: NCT06272149

21. (dardis2022patientcenteredguidelines pages 7-8): A. Dardis, H. Michelakakis, P. Rozenfeld, K. Fumic, J. Wagner, E. Pavan, M. Fuller, S. Revel-Vilk, D. Hughes, T. Cox, J. Aerts, and the International Working Group of Gaucher Disease. Patient centered guidelines for the laboratory diagnosis of gaucher disease type 1. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02573-6, doi:10.1186/s13023-022-02573-6. This article has 70 citations and is from a peer-reviewed journal.

22. (dinur2023contributionofglucosylsphingosine pages 6-7): Tama Dinur, Peter Bauer, Christian Beetz, Claudia Cozma, Michal Becker-Cohen, Majdolen Istaiti, Arndt Rolfs, Volha Skrahina, Ari Zimran, and Shoshana Revel-Vilk. Contribution of glucosylsphingosine (lyso-gb1) to treatment decisions in patients with gaucher disease. International Journal of Molecular Sciences, 24:3945, Feb 2023. URL: https://doi.org/10.3390/ijms24043945, doi:10.3390/ijms24043945. This article has 16 citations.

23. (dardis2022patientcenteredguidelines pages 4-5): A. Dardis, H. Michelakakis, P. Rozenfeld, K. Fumic, J. Wagner, E. Pavan, M. Fuller, S. Revel-Vilk, D. Hughes, T. Cox, J. Aerts, and the International Working Group of Gaucher Disease. Patient centered guidelines for the laboratory diagnosis of gaucher disease type 1. Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02573-6, doi:10.1186/s13023-022-02573-6. This article has 70 citations and is from a peer-reviewed journal.

24. (NCT05487599 chunk 1):  A Clinical Trial of PR001 (LY3884961) in Patients With Peripheral Manifestations of Gaucher Disease (PROCEED). Prevail Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05487599

25. (NCT04145037 chunk 1):  Lentiviral Vector Gene Therapy - The Guard1 Trial of AVR-RD-02 for Subjects With Type 1 Gaucher Disease. AVROBIO. 2019. ClinicalTrials.gov Identifier: NCT04145037

26. (kulkarni2024advancementsinviral media cabb2850): Akhil Kulkarni, Tiffany Chen, Ellen Sidransky, and Tae-Un Han. Advancements in viral gene therapy for gaucher disease. Genes, 15:364, Mar 2024. URL: https://doi.org/10.3390/genes15030364, doi:10.3390/genes15030364. This article has 16 citations.

27. (kulkarni2024advancementsinviral media 3ff0cbdf): Akhil Kulkarni, Tiffany Chen, Ellen Sidransky, and Tae-Un Han. Advancements in viral gene therapy for gaucher disease. Genes, 15:364, Mar 2024. URL: https://doi.org/10.3390/genes15030364, doi:10.3390/genes15030364. This article has 16 citations.

28. (rossi2023noninvasivedbsbasedapproaches pages 10-11): Claudia Rossi, Rossella Ferrante, Silvia Valentinuzzi, Mirco Zucchelli, Carlotta Buccolini, Sara Di Rado, Daniela Trotta, Liborio Stuppia, Luca Federici, and Maurizio Aricò. Noninvasive dbs-based approaches to assist clinical diagnosis and treatment monitoring of gaucher disease. Biomedicines, 11:2672, Sep 2023. URL: https://doi.org/10.3390/biomedicines11102672, doi:10.3390/biomedicines11102672. This article has 12 citations.
