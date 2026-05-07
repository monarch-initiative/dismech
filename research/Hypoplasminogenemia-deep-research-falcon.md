---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T08:59:14.771227'
end_time: '2026-05-07T09:31:19.148794'
duration_seconds: 1924.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypoplasminogenemia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypoplasminogenemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypoplasminogenemia** covering all of the
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
- **Disease Name:** Hypoplasminogenemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypoplasminogenemia** covering all of the
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


# Comprehensive Disease Characteristics Report: Hypoplasminogenemia (Type 1 Plasminogen Deficiency)

## Executive summary
Hypoplasminogenemia—also called **type 1 plasminogen deficiency (PLGD-1)**—is an ultra-rare, autosomal recessive disorder caused by **biallelic pathogenic variants in *PLG*** that reduce **plasminogen antigen and activity** and thereby impair fibrinolysis and tissue remodeling. The hallmark phenotype is **ligneous disease**, i.e., **fibrin-rich “wood-like” pseudomembranes** on mucosal surfaces (most commonly the conjunctiva), with potentially life-threatening airway involvement. Since 2021, **intravenous plasma-derived human plasminogen (plasminogen, human‑tvmh; Ryplazim)** has become a disease-targeted replacement therapy with evidence for durable lesion control in a phase 2/3 study and post-approval case series. (shapiro2023plasminogenhuman‐tvmhfor pages 1-2, nakar2024casereportrespiratory pages 1-2)

---

## 1. Disease information
### 1.1 Overview (what is the disease?)
Type 1 congenital plasminogen deficiency (hypoplasminogenemia) is defined by **low plasminogen antigen and low functional plasminogen activity**, leading to **impaired fibrin clearance** and accumulation of **fibrin-rich pseudomembranes** on mucosal surfaces (“ligneous” lesions). A 2023 review summarizes that type I disease is autosomal recessive and results in decreased antigenic and functional plasminogen with mucosal fibrin deposition. (silva2023plasminmediatedfibrinolysisin pages 1-2)

**Abstract-supported key concept quote (2023 review):** “*The hemostatic and inflammatory systems work hand in hand to maintain homeostasis at mucosal barrier sites… fibrin is well recognized for its role in mucosal homeostasis, wound healing, and inflammation*.” (silva2023plasminmediatedfibrinolysisin pages 1-2)

### 1.2 Key identifiers
- **MONDO:** **MONDO_0009009 (hypoplasminogenemia)** (OpenTargets). (OpenTargets Search: plasminogen deficiency,hypoplasminogenemia-PLG)
- **OMIM disease:** **Type 1 plasminogen deficiency / hypoplasminogenemia = OMIM #217090**. (panfili2023longtermfollowupin pages 1-3)
- **OMIM gene:** ***PLG* = OMIM #173350**. (panfili2023longtermfollowupin pages 1-3)

*Not retrieved in the current tool evidence (therefore not reported here to avoid guessing):* Orphanet ID, ICD-10/ICD-11 codes, MeSH descriptor.

### 1.3 Synonyms / alternative names
- Type 1 plasminogen deficiency; congenital plasminogen deficiency type I; **PLGD‑1**; “true plasminogen deficiency”; ligneous disease due to plasminogen deficiency. (panfili2023longtermfollowupin pages 1-3, nakar2024casereportrespiratory pages 1-2)

### 1.4 Evidence sources
The information in this report is derived from **peer-reviewed reviews and case reports/series**, plus **ClinicalTrials.gov trial records** and **OpenTargets disease–gene association**. (OpenTargets Search: plasminogen deficiency,hypoplasminogenemia-PLG, NCT02690714 chunk 1, nakar2024casereportrespiratory pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
- **Genetic cause (primary):** biallelic pathogenic variants in ***PLG*** (chromosome **6q26**) that reduce plasminogen antigen and activity (type I). (panfili2023longtermfollowupin pages 1-3, martinfernandez2016theunravellingof pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors
- **Autosomal recessive inheritance** for severe PLGD‑1 (homozygous/compound heterozygous), supported by multiple series. (klammt2011identificationofthree pages 3-4, klammt2011identificationofthree pages 1-2)
- **Consanguinity** is commonly reported in case series enriched from certain regions (e.g., Turkey in one series). (klammt2011identificationofthree pages 1-2)

#### Environmental/clinical triggers (non-genetic)
- Local triggers for mucosal lesion development/worsening (especially in oral disease) include **irritation, infection, poor hygiene, and surgery** in a 2023 review of ligneous periodontitis. (bektaskayhan2023ligneousperiodontitisassociated pages 1-2)

### 2.3 Protective factors
Not established in the retrieved sources.

### 2.4 Gene–environment interactions
Evidence in retrieved texts is suggestive (trauma/infection/surgery as triggers), but no quantitative gene–environment interaction studies were retrieved. (bektaskayhan2023ligneousperiodontitisassociated pages 1-2)

---

## 3. Phenotypes
### 3.1 Core phenotype: ligneous conjunctivitis / keratoconjunctivitis
- **Most frequent manifestation:** ligneous conjunctivitis (LC) affects **>80%** of symptomatic PLGD‑1 patients in a 2024 case series background and is **80%** in a large cited cohort summarized in a 2023 review. (nakar2024casereportrespiratory pages 1-2, silva2023plasminmediatedfibrinolysisin pages 1-2)
- LC lesions are described as **fibrin-rich, “woody” pseudomembranes** on tarsal/palpebral conjunctiva; can bleed and threaten vision through corneal scarring/perforation. (alghubaishi2023recurrentmeningitisand pages 2-4, nasiri2023plasminogendeficiencya pages 3-4)

**Suggested HPO terms** (not tool-validated here):
- Ligneous conjunctivitis / membranous conjunctivitis; conjunctival pseudomembrane; corneal scarring; vision impairment.

### 3.2 Oral/periodontal phenotypes
- **Ligneous gingivitis** reported as **34%** in a large study summarized by a 2023 review; type I deficiency predisposes to **early-onset severe periodontitis in childhood**. (silva2023plasminmediatedfibrinolysisin pages 1-2)
- In a 2023 gingival-lesion literature review, ages for gingival cases spanned **1–66 years**, with a strong female predominance in reported cases (74.3% female in that review). (bektaskayhan2023ligneousperiodontitisassociated pages 2-3)

**Suggested HPO terms:** gingival enlargement; periodontitis; early tooth loss.

### 3.3 Respiratory tract involvement
- **Frequency:** respiratory lesions in **~20–30%** of PLGD‑1 patients (2024 case series background). (nakar2024casereportrespiratory pages 1-2)
- Can involve the **tracheobronchial tree** causing cough/stridor/wheeze/dyspnea and **life‑threatening airway obstruction**; severe manifestations often in infants/young children. (nakar2024casereportrespiratory pages 1-2)

**Image-based evidence (real-world implementation):** bronchoscopy shows obstructing ligneous plaques pre-treatment and resolution after 10 days of IV plasminogen replacement. (nakar2024casereportrespiratory media f6ed748e)

**Suggested HPO terms:** airway obstruction; stridor; bronchial obstruction; recurrent pneumonia.

### 3.4 Genitourinary and gastrointestinal mucosal lesions
Mucosal lesions can occur in **urinary and genital systems** and **gastrointestinal tract**, described across reviews and clinical trial background. (silva2023plasminmediatedfibrinolysisin pages 1-2, shapiro2023plasminogenhuman‐tvmhfor pages 2-2)

**Suggested HPO terms:** cervicitis; infertility; gastrointestinal pseudomembranes.

### 3.5 Ear involvement
Middle ear/tympanic membrane involvement (e.g., otitis media/hearing loss) is described in a 2023 case review. (nasiri2023plasminogendeficiencya pages 3-4)

**Suggested HPO terms:** otitis media; hearing impairment.

### 3.6 Central nervous system (CNS) involvement
- **Congenital/occlusive hydrocephalus** is repeatedly reported in type I disease, including 2023 case reviews and a 2023 pediatric case report background. (nasiri2023plasminogendeficiencya pages 1-3, panfili2023longtermfollowupin pages 1-3)
- **Recurrent meningitis** has been described in association with severe disease in a 2023 case report. (alghubaishi2023recurrentmeningitisand pages 2-4)

**Suggested HPO terms:** hydrocephalus; meningitis.

### 3.7 Quality of life impact
- The phase 2/3 plasminogen replacement study reported quality of life (0–10 scale) was **improved or maintained in 93%** through week 48. (shapiro2023plasminogenhuman‐tvmhfor pages 5-6)

---

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
- **Primary causal gene:** ***PLG* (plasminogen)**. (klammt2011identificationofthree pages 3-4, martinfernandez2016theunravellingof pages 1-2)

### 4.2 Variant spectrum and molecular consequences
- Variant types causing type I deficiency include **missense, splice-site, frameshift, nonsense**, and larger deletions/structural variants; allelic heterogeneity is substantial. (klammt2011identificationofthree pages 3-4, martinfernandez2016theunravellingof pages 1-2)
- In a 23‑patient series, **16/23 (70%)** carried **homozygous or compound-heterozygous *PLG* mutations**, supporting recessive inheritance for severe hypoplasminogenemia. (klammt2011identificationofthree pages 3-4)
- Functional impact includes **reduced plasminogen activity** (e.g., <5% to 57% in one series; normal ~75–120%). (klammt2011identificationofthree pages 3-4)

**Examples (variant + functional correlation):**
- *PLG* c.763G>A (p.Glu255Lys) homozygous: proband activity **2.50%**; heterozygous parents **41.02%** and **54.07%**. (xu2021novelhomozygousmutation pages 1-3)
- *PLG* c.2095T>C (p.Cys699Arg) homozygous: plasminogen level **15%** (normal 75–150% in that report). (alghubaishi2023recurrentmeningitisand pages 2-4)
- Review tables summarize many missense variants with measured antigen/activity and predicted pathogenicity; reference ranges cited include antigen **6–25 mg/dL** and activity **70–140%**. (britorobinson2024plasminogenmissensevariants pages 14-15)

### 4.3 Modifier genes
No definitive modifier genes for ligneous disease penetrance/severity were established in retrieved sources. Some studies consider other thrombosis-risk loci (e.g., *F12*, *F13A1*) in families with thrombotic events, but this is not established as a modifier of ligneous disease itself. (martinfernandez2016theunravellingof pages 4-5)

### 4.4 Epigenetics / chromosomal abnormalities
Not established in the retrieved sources.

### 4.5 Suggested GO (biological process) and CL (cell type) terms
Based on disease mechanism described in reviews (defective fibrinolysis and mucosal wound healing) (silva2023plasminmediatedfibrinolysisin pages 1-2):
- **GO processes (suggested):** fibrinolysis; wound healing; extracellular matrix organization; inflammatory response.
- **CL terms (suggested):** mucosal epithelial cell; neutrophil (given discussion of fibrin–neutrophil activation in periodontal homeostasis). (silva2023plasminmediatedfibrinolysisin pages 1-2)

---

## 5. Environmental information
Not a primary driver in Mendelian PLGD‑1. Local environmental/clinical factors (infection, irritation, surgery) may precipitate lesions in mucosa, especially oral tissues. (bektaskayhan2023ligneousperiodontitisassociated pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Current understanding (causal chain)
1. **Biallelic *PLG* pathogenic variants** → reduced plasminogen antigen/activity (type I). (martinfernandez2016theunravellingof pages 1-2, klammt2011identificationofthree pages 3-4)
2. **Defective plasmin-mediated fibrinolysis** → impaired fibrin clearance and abnormal wound healing. (silva2023plasminmediatedfibrinolysisin pages 1-2, nasiri2023plasminogendeficiencya pages 3-4)
3. **Accumulation of amorphous fibrin-rich material in lamina propria** → pseudomembranous “ligneous” lesions on mucosal surfaces. (silva2023plasminmediatedfibrinolysisin pages 1-2)
4. **Site-specific lesion burden** (conjunctiva, gingiva, airway, GU/GI mucosa) → organ dysfunction (vision loss, tooth loss, airway obstruction, infertility, etc.). (shapiro2023plasminogenhuman‐tvmhfor pages 2-2, nakar2024casereportrespiratory pages 1-2)

### 6.2 Tissue/cell processes highlighted in recent reviews
A 2023 review emphasizes interplay of hemostasis and inflammation at mucosal barriers and highlights fibrin’s role in mucosal homeostasis and periodontitis susceptibility in PLG deficiency. (silva2023plasminmediatedfibrinolysisin pages 1-2)

---

## 7. Anatomical structures affected
### Organ/system level (representative)
- **Eye/conjunctiva:** ligneous conjunctivitis (most common). (silva2023plasminmediatedfibrinolysisin pages 1-2)
- **Oral cavity/periodontium:** ligneous gingivitis/periodontitis; early tooth loss. (silva2023plasminmediatedfibrinolysisin pages 1-2, bektaskayhan2023ligneousperiodontitisassociated pages 1-2)
- **Respiratory tract (larynx/trachea/bronchi):** obstructive ligneous lesions. (nakar2024casereportrespiratory pages 1-2)
- **Genitourinary tract:** cervix/uterus/vagina and other mucosa. (silva2023plasminmediatedfibrinolysisin pages 1-2, alghubaishi2023recurrentmeningitisand pages 2-4)
- **GI tract:** mucosal lesions. (silva2023plasminmediatedfibrinolysisin pages 1-2)
- **CNS:** hydrocephalus (subset). (panfili2023longtermfollowupin pages 1-3, alghubaishi2023recurrentmeningitisand pages 2-4)

**Suggested UBERON terms** (not tool-validated): conjunctiva; gingiva; trachea/bronchus; uterine cervix; gastrointestinal tract.

---

## 8. Temporal development
- **Onset:** typically **infancy/childhood**; mean reported onset **13–16 years** in an ophthalmology case series report; **<20%** present in the 4th–5th decades. (almeida2024ligneousconjunctivitisfreshfrozen pages 1-3)
- **Course:** often chronic/relapsing with recurrence after surgical excision when replacement is not provided; spontaneous remission has been described in a minority. (alghubaishi2023recurrentmeningitisand pages 2-4, panfili2023longtermfollowupin pages 1-3)

---

## 9. Inheritance and population
### 9.1 Inheritance
- **Autosomal recessive** for severe type I PLGD‑1 (homozygous or compound heterozygous). (klammt2011identificationofthree pages 3-4, alghubaishi2023recurrentmeningitisand pages 2-4)

### 9.2 Epidemiology (statistics)
- **Severe type I PLGD (homozygous/compound heterozygous):** estimated **~1.6 per 1,000,000** in Europe. (silva2023plasminmediatedfibrinolysisin pages 1-2)
- **Heterozygous carrier frequency:** **~0.3–0.4%** in the general population (as summarized in a 2023 review). (silva2023plasminmediatedfibrinolysisin pages 1-2)

*Note:* Some papers repeat the 0.3–0.4% figure ambiguously; the 2023 J Dent Res review explicitly applies 0.3–0.4% to heterozygous mutations. (silva2023plasminmediatedfibrinolysisin pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical tests
- **Key laboratory confirmation:** measure both
  - **plasminogen activity** (commonly chromogenic assay; e.g., tPA-activated assays), and
  - **plasminogen antigen**
  to classify **type I vs type II**. (martinfernandez2016theunravellingof pages 1-2, alghafry2025inheriteddisordersof pages 5-6)

### 10.2 Distinguishing type I vs type II
- **Type I (hypoplasminogenemia):** low activity + low antigen. (martinfernandez2016theunravellingof pages 1-2, alghafry2025inheriteddisordersof pages 5-6)
- **Type II (dysplasminogenemia):** low activity with normal antigen; rarely symptomatic. (silva2023plasminmediatedfibrinolysisin pages 1-2, martinfernandez2016theunravellingof pages 1-2)

### 10.3 Routine labs often normal / non-diagnostic
Conventional coagulation tests (e.g., platelet count, PT, aPTT, factor levels, fibrinogen, vWF) can be normal and are not diagnostic; targeted plasminogen assays are needed. (alghafry2025inheriteddisordersof pages 5-6)

### 10.4 Genetic testing
- Confirmatory genetic testing via sequencing of *PLG* (Sanger, WES/WGS, NGS; long-range PCR approaches may help avoid homology/pseudogene issues) is used for definitive diagnosis and family studies. (xu2021novelhomozygousmutation pages 1-3, martinfernandez2016theunravellingof pages 2-3)

### 10.5 Suggested differential diagnosis
Not comprehensively enumerated in retrieved texts. Clinically, LC can be misdiagnosed as nonspecific conjunctivitis early; persistent/recurrent pseudomembranes plus low plasminogen support PLGD‑1. (nasiri2023plasminogendeficiencya pages 3-4)

---

## 11. Outcome / prognosis
- Severity varies with lesion location and burden. Untreated disease can cause major morbidity (blindness, airway obstruction, complications of hydrocephalus) and can be fatal, as emphasized in clinical trial background and case literature. (shapiro2023plasminogenhuman‐tvmhfor pages 2-2, alghubaishi2023recurrentmeningitisand pages 2-4)
- Replacement therapy can produce rapid resolution of life-threatening airway disease in reported cases. (nakar2024casereportrespiratory pages 1-2, nakar2024casereportrespiratory media f6ed748e)

---

## 12. Treatment
### 12.1 Pharmacotherapy / replacement therapy (current standard)
#### Intravenous plasminogen, human‑tvmh (Ryplazim)
- **Trial evidence:** open-label phase 2/3 study (15 subjects) with treatment up to **124 weeks**; dosing **6.6 mg/kg** with individualized intervals. (shapiro2023plasminogenhuman‐tvmhfor pages 1-2)
  - **Efficacy:** in participants with visible assessable lesions, **100% (n=11)** had **≥50% improvement at 48 weeks**; all met the co-primary biochemical endpoint of **≥10% absolute trough plasminogen activity increase** through week 12. (shapiro2023plasminogenhuman‐tvmhfor pages 1-2)
  - **Non-visible lesions:** high proportion resolved among assessed lesions during follow-up (table excerpt). (shapiro2023plasminogenhuman‐tvmhfor pages 4-5)
  - **Safety:** treatment-emergent bleeding AEs in **5/15 (33%)**, mild/short; no neutralizing antibodies detected. (shapiro2023plasminogenhuman‐tvmhfor pages 7-8)
  - **QoL:** improved/maintained in **93%** through week 48. (shapiro2023plasminogenhuman‐tvmhfor pages 5-6)

- **Real-world application (respiratory lesions):** case series of four patients with severe airway disease; rapid clinical improvement and lesion resolution documented, including bronchoscopy resolution by day 10 and durable outpatient/home infusion regimens. (nakar2024casereportrespiratory pages 2-3, nakar2024casereportrespiratory media f6ed748e)

**MAXO (suggested):** plasminogen replacement therapy; intravenous drug administration.

### 12.2 Topical/local approaches (when commercial plasminogen eyedrops unavailable)
- **Membrane excision + topical/subconjunctival FFP + topical heparin:** 2024 report of two LC cases with no recurrence at **12 months**; detailed preparation/storage protocol for FFP aliquots and intensive postoperative regimen. (almeida2024ligneousconjunctivitisfreshfrozen pages 1-3)
- **Topical plasminogen drops compounded from FFP:** 2023 pediatric case report describes ethics-approved topical plasminogen formulation with durable absence of pseudomembranes at **12‑year follow-up**, enabling prosthesis use after debulking surgery. (panfili2023longtermfollowupin pages 1-3)
- **Allogeneic donor plasma drops (clinical trial N-of-1):** protocol NCT05404932 uses donor plasma drops 1–2 drops every 1–5 hours for 2–6 months with safety monitoring (Canada). (NCT05404932 chunk 1)

**MAXO (suggested):** topical plasma administration; conjunctival membrane excision.

### 12.3 Clinical trials and registries (real-world implementation)
- **NCT02690714:** IV plasminogen 6.6 mg/kg, phase 2/3; endpoints include trough plasminogen activity and lesion improvement. (NCT02690714 chunk 1)
- **NCT01554956:** plasminogen eye drops for LC, phase 2/3, enrollment 12; results posted 2023‑01‑25; endpoint includes prevention of pseudomembrane relapse. (NCT01554956 chunk 1)
- **NCT03797495 (HISTORY):** observational registry/biobank planned 100 affected individuals to define natural history and correlate factors with disease expression/severity; includes centralized activity/antigen and genetic testing. (NCT03797495 chunk 1)

---

## 13. Prevention
No primary prevention is established for Mendelian PLGD‑1. Secondary/tertiary prevention is primarily via:
- early recognition of characteristic mucosal lesions and
- genetic counseling / family testing in autosomal recessive disease. (alghubaishi2023recurrentmeningitisand pages 2-4, xu2021novelhomozygousmutation pages 1-3)

---

## 14. Other species / natural disease
- A naturally occurring canine ligneous membranitis/conjunctivitis case (Maltese dog) was linked to a **large *PLG* rearrangement deleting exon 1** and complete lack of plasminogen activity; article frames this as a **spontaneous animal model**. (turba2021alargedeletion pages 1-2)
  - **OMIA:** canine ligneous membranitis is referenced as **OMIA 002020‑9615** in the dog paper. (turba2021alargedeletion pages 1-2)

---

## 15. Model organisms
The retrieved evidence directly supports:
- **Spontaneous dog model** (above). (turba2021alargedeletion pages 1-2)
Additional model organism claims (e.g., engineered Plg−/− mice) are mentioned in case-report literature but were not retrieved as primary full-text evidence here; therefore not expanded to avoid overstatement. (xu2021novelhomozygousmutation pages 1-3)

---

## Recent developments (2023–2024 highlights)
1. **Mechanistic consolidation at mucosal barriers:** 2023 review integrates fibrin biology with mucosal/periodontal homeostasis and emphasizes Mendelian PLG deficiency as a natural experiment for understanding severe early-onset periodontitis. (silva2023plasminmediatedfibrinolysisin pages 1-2)
2. **Expanded therapeutic evidence for IV plasminogen replacement:** 2023 phase 2/3 trial provides long-term (to 124 weeks) efficacy, safety, and QoL outcomes supporting replacement therapy as disease-modifying. (shapiro2023plasminogenhuman‐tvmhfor pages 1-2, shapiro2023plasminogenhuman‐tvmhfor pages 7-8)
3. **Post-approval real-world respiratory rescue:** 2024 case series documents rapid reversal of life-threatening airway lesions, supported by imaging/bronchoscopy and biomarker changes. (nakar2024casereportrespiratory pages 1-2, nakar2024casereportrespiratory media f6ed748e, nakar2024casereportrespiratory media 11094d94)
4. **Continued innovation in topical/local therapy when commercial drops unavailable:** 2024 ophthalmology case series reports standardized FFP/heparin perioperative protocol with 12-month recurrence-free follow-up; N-of-1 trial protocols formalize donor plasma drops. (almeida2024ligneousconjunctivitisfreshfrozen pages 1-3, NCT05404932 chunk 1)

---

## Limitations of this report (evidence gaps in retrieved texts)
- Orphanet/ICD/MeSH identifiers, and contemporary large prospective cohort statistics (beyond the commonly cited Tefs et al. frequencies summarized in 2023–2024 reviews) were not retrieved in the tool-accessible full texts for this run.
- Formal differential diagnosis lists and validated ontology IDs for HPO/GO/UBERON/MAXO terms were not pulled from dedicated ontology databases in the available evidence; terms provided are suggestions based on phenotype descriptions.

---

## Key source list (URLs and publication dates)
- Silva LM et al. **“Plasmin-Mediated Fibrinolysis in Periodontitis Pathogenesis.”** *Journal of Dental Research*. **2023-07**. https://doi.org/10.1177/00220345231171837 (silva2023plasminmediatedfibrinolysisin pages 1-2)
- Shapiro AD et al. **“Plasminogen, human‑tvmh for the treatment of children and adults with plasminogen deficiency type 1.”** *Haemophilia*. **2023-09**. https://doi.org/10.1111/hae.14849 (shapiro2023plasminogenhuman‐tvmhfor pages 1-2)
- Nakar C et al. **“Respiratory lesions successfully treated with intravenous plasminogen, human‑tvmh…”** *Frontiers in Pediatrics*. **2024-09**. https://doi.org/10.3389/fped.2024.1465166 (nakar2024casereportrespiratory pages 1-2)
- de Almeida ICGB, Marback PMF. **“Ligneous conjunctivitis: Fresh-frozen plasma and heparin…”** *Arq Bras Oftalmol*. **2024-03**. https://doi.org/10.5935/0004-2749.2022-0288 (almeida2024ligneousconjunctivitisfreshfrozen pages 1-3)
- Brito-Robinson T et al. **“Plasminogen missense variants…”** *Frontiers in Cardiovascular Medicine*. **2024-06**. https://doi.org/10.3389/fcvm.2024.1406953 (britorobinson2024plasminogenmissensevariants pages 15-16)
- ClinicalTrials.gov **NCT02690714** (2016; results posted 2021): https://clinicaltrials.gov/study/NCT02690714 (NCT02690714 chunk 1)
- ClinicalTrials.gov **NCT01554956** (2013; results posted 2023-01-25): https://clinicaltrials.gov/study/NCT01554956 (NCT01554956 chunk 1)
- ClinicalTrials.gov **NCT03797495** (2018): https://clinicaltrials.gov/study/NCT03797495 (NCT03797495 chunk 1)


References

1. (shapiro2023plasminogenhuman‐tvmhfor pages 1-2): Amy D. Shapiro, Charles Nakar, Joseph M. Parker, Karen Thibaudeau, Roberto Crea, and Per Morten Sandset. Plasminogen, human‐tvmh for the treatment of children and adults with plasminogen deficiency type 1. Haemophilia, 29:1556-1564, Sep 2023. URL: https://doi.org/10.1111/hae.14849, doi:10.1111/hae.14849. This article has 15 citations and is from a peer-reviewed journal.

2. (nakar2024casereportrespiratory pages 1-2): Charles Nakar, Heather McDaniel, Joseph M. Parker, Karen Thibaudeau, Neelam Thukral, and Amy D. Shapiro. Case report: respiratory lesions successfully treated with intravenous plasminogen, human-tvmh, replacement therapy in four patients with plasminogen deficiency type 1. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1465166, doi:10.3389/fped.2024.1465166. This article has 2 citations.

3. (silva2023plasminmediatedfibrinolysisin pages 1-2): L.M. Silva, K. Divaris, T.H. Bugge, and N.M. Moutsopoulos. Plasmin-mediated fibrinolysis in periodontitis pathogenesis. Journal of Dental Research, 102:972-978, Jul 2023. URL: https://doi.org/10.1177/00220345231171837, doi:10.1177/00220345231171837. This article has 17 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: plasminogen deficiency,hypoplasminogenemia-PLG): Open Targets Query (plasminogen deficiency,hypoplasminogenemia-PLG, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (panfili2023longtermfollowupin pages 1-3): Filippo Maria Panfili, Paola Valente, Andrea Ficari, Fabiana Cortellessa, Davide Vecchio, Michaela Veronika Gonfiantini, Paola Sabrina Buonuomo, Giovanna Stefania Colafati, Emanuele Agolini, Maria Bartuli, Alessandra Claudia Modugno, and Marina Macchiaiolo. Long-term follow-up in a pediatric patient with ligneous conjunctivitis due to plg gene mutation in topical plasminogen treatment after successful use of ocular prosthesis for aesthetic rehabilitation: a case report. Italian Journal of Pediatrics, Aug 2023. URL: https://doi.org/10.1186/s13052-023-01503-x, doi:10.1186/s13052-023-01503-x. This article has 2 citations and is from a peer-reviewed journal.

6. (NCT02690714 chunk 1):  A Study of Prometic Plasminogen IV Infusion in Subjects With Hypoplasminogenemia. Prometic Biotherapeutics, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02690714

7. (martinfernandez2016theunravellingof pages 1-2): Laura Martin-Fernandez, Pascual Marco, Irene Corrales, Raquel Pérez, Lorena Ramírez, Sonia López, Francisco Vidal, and José Manuel Soria. The unravelling of the genetic architecture of plasminogen deficiency and its relation to thrombotic disease. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39255, doi:10.1038/srep39255. This article has 24 citations and is from a peer-reviewed journal.

8. (klammt2011identificationofthree pages 3-4): Jürgen Klammt, Louise Kobelt, Dilek Aktas, Ismet Durak, Aslan Gokbuget, Quintin Hughes, Murat Irkec, Idil Kurtulus, Elisabetta Lapi, Hadas Mechoulam, Roberto Mendoza-Londono, Joseph Palumbo, Hansjörg Steitzer, Khalid Tabbara, Zeynep Ozbek, Neri Pucci, Talia Sotomayor, Marian Sturm, Tim Drogies, Maike Ziegler, and Volker Schuster. Identification of three novel plasminogen (plg) gene mutations in a series of 23 patients with low plg activity. Thrombosis and Haemostasis, 105:454-460, Jan 2011. URL: https://doi.org/10.1160/th10-04-0216, doi:10.1160/th10-04-0216. This article has 60 citations and is from a domain leading peer-reviewed journal.

9. (klammt2011identificationofthree pages 1-2): Jürgen Klammt, Louise Kobelt, Dilek Aktas, Ismet Durak, Aslan Gokbuget, Quintin Hughes, Murat Irkec, Idil Kurtulus, Elisabetta Lapi, Hadas Mechoulam, Roberto Mendoza-Londono, Joseph Palumbo, Hansjörg Steitzer, Khalid Tabbara, Zeynep Ozbek, Neri Pucci, Talia Sotomayor, Marian Sturm, Tim Drogies, Maike Ziegler, and Volker Schuster. Identification of three novel plasminogen (plg) gene mutations in a series of 23 patients with low plg activity. Thrombosis and Haemostasis, 105:454-460, Jan 2011. URL: https://doi.org/10.1160/th10-04-0216, doi:10.1160/th10-04-0216. This article has 60 citations and is from a domain leading peer-reviewed journal.

10. (bektaskayhan2023ligneousperiodontitisassociated pages 1-2): Kıvanç Bektaş-Kayhan, Revan Birke Koca-Ünsal, Bora Başaran, and Tiraje Çelkan. Ligneous periodontitis associated with plasminogen deficiency: a review of the literature with two additional cases. Cyprus Journal of Medical Sciences, 7:718-730, Jan 2023. URL: https://doi.org/10.4274/cjms.2022.2021-194, doi:10.4274/cjms.2022.2021-194. This article has 1 citations.

11. (alghubaishi2023recurrentmeningitisand pages 2-4): Somayah A Alghubaishi, Muhammad Saeed, Fadi Abujamous, Hussam Osman, and Badriah G Alasmari. Recurrent meningitis and its rare association with ligneous conjunctivitis and congenital plasminogen deficiency. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.44813, doi:10.7759/cureus.44813. This article has 0 citations.

12. (nasiri2023plasminogendeficiencya pages 3-4): Abdulrahman Nasiri, Marwa Nassar, and Hazzaa Alzahrani. Plasminogen deficiency: a case report and review. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45676, doi:10.7759/cureus.45676. This article has 3 citations.

13. (bektaskayhan2023ligneousperiodontitisassociated pages 2-3): Kıvanç Bektaş-Kayhan, Revan Birke Koca-Ünsal, Bora Başaran, and Tiraje Çelkan. Ligneous periodontitis associated with plasminogen deficiency: a review of the literature with two additional cases. Cyprus Journal of Medical Sciences, 7:718-730, Jan 2023. URL: https://doi.org/10.4274/cjms.2022.2021-194, doi:10.4274/cjms.2022.2021-194. This article has 1 citations.

14. (nakar2024casereportrespiratory media f6ed748e): Charles Nakar, Heather McDaniel, Joseph M. Parker, Karen Thibaudeau, Neelam Thukral, and Amy D. Shapiro. Case report: respiratory lesions successfully treated with intravenous plasminogen, human-tvmh, replacement therapy in four patients with plasminogen deficiency type 1. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1465166, doi:10.3389/fped.2024.1465166. This article has 2 citations.

15. (shapiro2023plasminogenhuman‐tvmhfor pages 2-2): Amy D. Shapiro, Charles Nakar, Joseph M. Parker, Karen Thibaudeau, Roberto Crea, and Per Morten Sandset. Plasminogen, human‐tvmh for the treatment of children and adults with plasminogen deficiency type 1. Haemophilia, 29:1556-1564, Sep 2023. URL: https://doi.org/10.1111/hae.14849, doi:10.1111/hae.14849. This article has 15 citations and is from a peer-reviewed journal.

16. (nasiri2023plasminogendeficiencya pages 1-3): Abdulrahman Nasiri, Marwa Nassar, and Hazzaa Alzahrani. Plasminogen deficiency: a case report and review. Cureus, Sep 2023. URL: https://doi.org/10.7759/cureus.45676, doi:10.7759/cureus.45676. This article has 3 citations.

17. (shapiro2023plasminogenhuman‐tvmhfor pages 5-6): Amy D. Shapiro, Charles Nakar, Joseph M. Parker, Karen Thibaudeau, Roberto Crea, and Per Morten Sandset. Plasminogen, human‐tvmh for the treatment of children and adults with plasminogen deficiency type 1. Haemophilia, 29:1556-1564, Sep 2023. URL: https://doi.org/10.1111/hae.14849, doi:10.1111/hae.14849. This article has 15 citations and is from a peer-reviewed journal.

18. (xu2021novelhomozygousmutation pages 1-3): Liyan Xu, Yajie Sun, Kaili Yang, Dongqing Zhao, Yiqiang Wang, and Shengwei Ren. Novel homozygous mutation of plasminogen in ligneous conjunctivitis: a case report and literature review. Ophthalmic Genetics, 42:105-109, Jan 2021. URL: https://doi.org/10.1080/13816810.2020.1867753, doi:10.1080/13816810.2020.1867753. This article has 7 citations and is from a peer-reviewed journal.

19. (britorobinson2024plasminogenmissensevariants pages 14-15): Teresa Brito-Robinson, Yetunde A. Ayinuola, Victoria A. Ploplis, and Francis J. Castellino. Plasminogen missense variants and their involvement in cardiovascular and inflammatory disease. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1406953, doi:10.3389/fcvm.2024.1406953. This article has 6 citations and is from a peer-reviewed journal.

20. (martinfernandez2016theunravellingof pages 4-5): Laura Martin-Fernandez, Pascual Marco, Irene Corrales, Raquel Pérez, Lorena Ramírez, Sonia López, Francisco Vidal, and José Manuel Soria. The unravelling of the genetic architecture of plasminogen deficiency and its relation to thrombotic disease. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39255, doi:10.1038/srep39255. This article has 24 citations and is from a peer-reviewed journal.

21. (almeida2024ligneousconjunctivitisfreshfrozen pages 1-3): Isabela Costa Guerra Barreto de Almeida and Patrícia Maria Fernandes Marback. Ligneous conjunctivitis: fresh-frozen plasma and heparin use intra-and postoperatively, a report of two cases. Arquivos Brasileiros de Oftalmologia, Mar 2024. URL: https://doi.org/10.5935/0004-2749.2022-0288, doi:10.5935/0004-2749.2022-0288. This article has 5 citations and is from a peer-reviewed journal.

22. (alghafry2025inheriteddisordersof pages 5-6): Maha Al-Ghafry, Mouhamed Yazan Abou-Ismail, and Suchitra S. Acharya. Inherited disorders of the fibrinolytic pathway: pathogenic phenotypes and diagnostic considerations of extremely rare disorders. Seminars in Thrombosis and Hemostasis, 51:227-235, Sep 2025. URL: https://doi.org/10.1055/s-0044-1789596, doi:10.1055/s-0044-1789596. This article has 12 citations and is from a peer-reviewed journal.

23. (martinfernandez2016theunravellingof pages 2-3): Laura Martin-Fernandez, Pascual Marco, Irene Corrales, Raquel Pérez, Lorena Ramírez, Sonia López, Francisco Vidal, and José Manuel Soria. The unravelling of the genetic architecture of plasminogen deficiency and its relation to thrombotic disease. Scientific Reports, Dec 2016. URL: https://doi.org/10.1038/srep39255, doi:10.1038/srep39255. This article has 24 citations and is from a peer-reviewed journal.

24. (shapiro2023plasminogenhuman‐tvmhfor pages 4-5): Amy D. Shapiro, Charles Nakar, Joseph M. Parker, Karen Thibaudeau, Roberto Crea, and Per Morten Sandset. Plasminogen, human‐tvmh for the treatment of children and adults with plasminogen deficiency type 1. Haemophilia, 29:1556-1564, Sep 2023. URL: https://doi.org/10.1111/hae.14849, doi:10.1111/hae.14849. This article has 15 citations and is from a peer-reviewed journal.

25. (shapiro2023plasminogenhuman‐tvmhfor pages 7-8): Amy D. Shapiro, Charles Nakar, Joseph M. Parker, Karen Thibaudeau, Roberto Crea, and Per Morten Sandset. Plasminogen, human‐tvmh for the treatment of children and adults with plasminogen deficiency type 1. Haemophilia, 29:1556-1564, Sep 2023. URL: https://doi.org/10.1111/hae.14849, doi:10.1111/hae.14849. This article has 15 citations and is from a peer-reviewed journal.

26. (nakar2024casereportrespiratory pages 2-3): Charles Nakar, Heather McDaniel, Joseph M. Parker, Karen Thibaudeau, Neelam Thukral, and Amy D. Shapiro. Case report: respiratory lesions successfully treated with intravenous plasminogen, human-tvmh, replacement therapy in four patients with plasminogen deficiency type 1. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1465166, doi:10.3389/fped.2024.1465166. This article has 2 citations.

27. (NCT05404932 chunk 1): Sarah Tehseen. Treatment of Ligneous Conjunctivitis in Children With Plasminogen Deficiency. University of Saskatchewan. 2022. ClinicalTrials.gov Identifier: NCT05404932

28. (NCT01554956 chunk 1):  Efficacy/Safety of Human Plasminogen Eye Drop in Ligneous Conjunctivitis Patients. Kedrion S.p.A.. 2013. ClinicalTrials.gov Identifier: NCT01554956

29. (NCT03797495 chunk 1): Amy D Shapiro, MD. Study of Individuals Affected With Hypoplasminogenemia. Indiana Hemophilia &Thrombosis Center, Inc.. 2018. ClinicalTrials.gov Identifier: NCT03797495

30. (turba2021alargedeletion pages 1-2): M. E. Turba, P. C. Ostan, S. Ghetti, M. Dajbychova, F. Dondi, and F. Gentilini. A large deletion in the plasminogen gene is associated with ligneous membranitis in a maltese dog. Animal Genetics, 52:767-771, Aug 2021. URL: https://doi.org/10.1111/age.13130, doi:10.1111/age.13130. This article has 2 citations and is from a domain leading peer-reviewed journal.

31. (nakar2024casereportrespiratory media 11094d94): Charles Nakar, Heather McDaniel, Joseph M. Parker, Karen Thibaudeau, Neelam Thukral, and Amy D. Shapiro. Case report: respiratory lesions successfully treated with intravenous plasminogen, human-tvmh, replacement therapy in four patients with plasminogen deficiency type 1. Frontiers in Pediatrics, Sep 2024. URL: https://doi.org/10.3389/fped.2024.1465166, doi:10.3389/fped.2024.1465166. This article has 2 citations.

32. (britorobinson2024plasminogenmissensevariants pages 15-16): Teresa Brito-Robinson, Yetunde A. Ayinuola, Victoria A. Ploplis, and Francis J. Castellino. Plasminogen missense variants and their involvement in cardiovascular and inflammatory disease. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1406953, doi:10.3389/fcvm.2024.1406953. This article has 6 citations and is from a peer-reviewed journal.