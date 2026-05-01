---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T15:35:57.525843'
end_time: '2026-04-26T15:45:22.132546'
duration_seconds: 564.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pontocerebellar Hypoplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pontocerebellar Hypoplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pontocerebellar Hypoplasia** covering all of the
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
- **Disease Name:** Pontocerebellar Hypoplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pontocerebellar Hypoplasia** covering all of the
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


## Pontocerebellar Hypoplasia (PCH): Disease Characteristics Research Report (2026-04-26)

### Evidence and identifier note
This report is based on the full-text excerpts retrieved via the toolchain (peer‑reviewed primary studies/reviews and ClinicalTrials.gov records). The current evidence set did **not** include explicit OMIM/Orphanet/ICD/MeSH/MONDO code strings for “pontocerebellar hypoplasia” as a parent concept; therefore, identifier codes are reported only when explicitly present in evidence, and otherwise marked **not available in retrieved sources**. (cavusoglu2024evaluationofthe pages 1-2, kukulka2025pontocerebellarhypoplasiaa pages 11-13)

---

## 1. Disease Information

### 1.1 What is the disease?
Pontocerebellar hypoplasia (PCH) is an umbrella term for a heterogeneous group of (usually prenatal or early‑infancy onset) neurodevelopmental disorders characterized by reduced volume (hypoplasia) of the **pons** and **cerebellum**, often with progressive microcephaly and variable supratentorial involvement; many classic subtypes are neurodegenerative. (dijk2018what’snewin pages 1-3, cavusoglu2024evaluationofthe pages 1-2)

A key recent expert framing is that **“PCH” should be used primarily as a radiologic descriptor** (reduced-volume pons and cerebellum), because many monogenic, chromosomal, and acquired conditions can produce a PCH-like imaging pattern. (zakaria2024classic“pch”genes pages 1-4)

**Direct abstract quote (radiologic descriptor and heterogeneity):** “As a descriptive term, PCH refers to pons and cerebellum of reduced volume… many other disorders can result in a similar imaging appearance.” (zakaria2024classic“pch”genes pages 1-4)

### 1.2 Key identifiers
* **MONDO ID:** not available in retrieved sources.
* **OMIM / Orphanet / ICD‑10/ICD‑11 / MeSH:** not available in retrieved sources (codes not explicitly stated in the retrieved full text excerpts).

### 1.3 Common synonyms / alternative names
* “Radiologic pontocerebellar hypoplasia” (used to emphasize imaging finding rather than a specific classic genetic subtype). (zakaria2024classic“pch”genes pages 1-4)
* Proposed re-naming direction: a genetically anchored dyadic nomenclature termed **“pontocerebellar hypoplasia spectrum disorder (PHSD)”** with (gene)-associated PHSD when a molecular cause is known. (kukulka2025pontocerebellarhypoplasiaa pages 11-13, kukulka2025pontocerebellarhypoplasiaa pages 13-14)

### 1.4 Evidence source type
The retrieved evidence is primarily:
* Aggregated disease-level synthesis from reviews. (dijk2018what’snewin pages 1-3, kukulka2025pontocerebellarhypoplasiaa pages 11-13)
* Human cohorts/case series with imaging + genetic evaluation. (zakaria2024classic“pch”genes pages 1-4, cavusoglu2024evaluationofthe pages 1-2)
* Human iPSC/organoid functional modeling. (kagermeier2024humanorganoidmodel pages 1-2)
* ClinicalTrials.gov interventional/observational records (not PCH‑specific drug approvals). (NCT04378075 chunk 1, NCT03572868 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** inherited genetic variants affecting fundamental cellular processes, with a strong over‑representation of genes involved in **RNA processing and translation**, especially **tRNA biology** (splicing and aminoacylation), and additional causes in mitochondrial function and basic metabolism. (dijk2018what’snewin pages 10-11, ghasemi2024broadeningthephenotype pages 11-13)

PCH is also a **radiologic pattern** that can result from:
* **Chromosomal abnormalities**,
* **Monogenic disorders outside classic PCH genes**, and
* **Acquired insults** (e.g., prematurity, hypoxic‑ischemic injury), depending on the cohort studied. (zakaria2024classic“pch”genes pages 1-4)

### 2.2 Risk factors
* **Genetic / familial:** predominance of **autosomal recessive inheritance** in classic PCH types; high rates of **homozygosity** and **consanguinity** in some populations/cohorts. In a Turkish multicenter genetically confirmed cohort (n=64), homozygous mutation occurred in 89.1% and consanguinity in 79.7%. (cavusoglu2024evaluationofthe pages 1-2)
* **Non-genetic (for radiologic PCH phenotype):** acquired etiologies can contribute a minority of radiologic PCH cases (10.5% acquired in one imaging‑defined cohort). (zakaria2024classic“pch”genes pages 17-20)

### 2.3 Protective factors
No protective genetic variants or modifiable protective environmental factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No explicit gene–environment interaction evidence was identified in the retrieved evidence set.

---

## 3. Phenotypes (clinical + suggested HPO terms)

### 3.1 Core phenotypic spectrum (human cohorts)
Across cohorts, common phenotypes include global developmental delay/intellectual disability, abnormal tone, microcephaly, seizures, feeding and respiratory problems, and variable visual/hearing impairment. (zakaria2024classic“pch”genes pages 4-7, cavusoglu2024evaluationofthe pages 1-2)

**Recent quantitative phenotype data (2024 cohorts):**
* **Genetically confirmed PCH cohort, Turkey (n=64):** microcephaly 91.3%, psychomotor retardation 98.4%, abnormal neurologic findings 100%, seizures 63.8%. (cavusoglu2024evaluationofthe pages 1-2)
* **Radiologic PCH cohort (n=38):** global developmental delay in all; feeding difficulties 76%, respiratory issues 64%; 50% non-verbal, 64% non-ambulatory, 45% gastrostomy feeding; ~1/3 mortality with median age at death 8 months. (zakaria2024classic“pch”genes pages 4-7, zakaria2024classic“pch”genes pages 1-4)

### 3.2 Onset, severity, progression
* Onset is often **prenatal** or **neonatal/infancy**, consistent with fetal/postnatal neurodevelopmental disruption and/or early neurodegeneration. (dijk2018what’snewin pages 1-3)
* Imaging and clinical features may **evolve over time**, supporting serial follow‑up imaging. (kukulka2025pontocerebellarhypoplasiaa pages 11-13)

### 3.3 Suggested HPO terms (examples)
* Pontocerebellar hypoplasia: **HP:0001320** (term name; code not verified in retrieved evidence)
* Cerebellar hypoplasia: **HP:0001321** (term name; code not verified)
* Hypoplasia of the pons: (HPO term name; code not verified)
* Microcephaly: **HP:0000252** (term name; code not verified)
* Global developmental delay: **HP:0001263** (term name; code not verified)
* Seizures: **HP:0001250** (term name; code not verified)
* Hypotonia: **HP:0001252** (term name; code not verified)
* Feeding difficulties / dysphagia: **HP:0011968 / HP:0002015** (term names; codes not verified)
* Respiratory insufficiency / apnea: **HP:0002093 / HP:0002104** (term names; codes not verified)
* Optic atrophy / visual impairment: **HP:0000648 / HP:0000505** (term names; codes not verified)

*Note:* HPO term names are provided to support knowledge-base mapping, but exact HPO IDs should be validated against the current HPO release because IDs were not provided in the retrieved sources.

### 3.4 Quality of life impact
Severe motor and communication impairment is common in imaging- and genetics-defined cohorts (e.g., non-ambulatory 64% and non-verbal 50% in a radiologic PCH cohort), implying profound caregiver and daily-function impact. (zakaria2024classic“pch”genes pages 4-7)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (examples emphasized in 2023–2024 evidence)
Recent large cohorts and updated reviews highlight recurrent genes including **CLP1, TSEN54, EXOSC3, RARS2, AMPD2**, with many additional rare causes. (cavusoglu2024evaluationofthe pages 2-5, ghasemi2024broadeningthephenotype pages 1-2)

**Cohort gene frequencies (Turkey, n=64):** CLP1 26.56%; EXOSC3 10.9%; TSEN54 9.3%; RARS2 7.8%. (cavusoglu2024evaluationofthe pages 2-5)

### 4.2 Pathogenic variants (examples)
* **CLP1:** recurrent homozygous missense **c.419G>A (p.Arg140His)** in all CLP1 cases in the Turkish cohort. (cavusoglu2024evaluationofthe pages 1-2)
* **TSEN54 (PCH2A founder):** **c.919G>T (p.Ala307Ser)** recurrent in TSEN54 group in Turkey, and used as the canonical founder genotype for PCH2A in modeling work. (cavusoglu2024evaluationofthe pages 1-2, kagermeier2024humanorganoidmodel pages 1-2)
* **EXOSC3:** recurrent missense variants including **c.395A>C (p.Asp132Ala)** and **c.572G>A (p.Gly191Asp)** noted in cohort summaries. (cavusoglu2024evaluationofthe pages 11-12)
* **RARS2:** a non-coding 5′UTR/promoter variant **NM_020320.3:c.-2A>G** disrupts the Kozak sequence and decreases protein translation, supporting pathogenicity in PCH6. (nicolle2023anoncodingvariant pages 1-2)

### 4.3 Functional consequences (high-level)
A unifying theme is dysfunction in RNA/tRNA processing and translation, including:
* **tRNA intron excision (TSEN complex) and post-splicing processing (CLP1)**; defects are hypothesized to affect translation capacity and neurodevelopmental cell states. (dijk2018what’snewin pages 10-11, kagermeier2024humanorganoidmodel pages 1-2)
* **Mitochondrial tRNA aminoacylation (RARS2)** affecting mitochondrial translation and respiratory chain function. (nicolle2023anoncodingvariant pages 1-2, ghasemi2024broadeningthephenotype pages 11-13)
* **RNA exosome function (EXOSC3 and related EXOSC genes)** affecting RNA processing and ribosome biogenesis signaling. (cavusoglu2024evaluationofthe pages 10-11)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
* **Modifier genes / epigenetics:** not identified in retrieved evidence.
* **Chromosomal abnormalities:** contribute substantially to imaging-defined PCH: 21% chromosomal etiologies in a radiologic cohort (n=38). (zakaria2024classic“pch”genes pages 1-4)

---

## 5. Environmental Information
PCH is primarily genetic; no consistent environmental/lifestyle contributors were identified in the retrieved sources. However, **acquired** causes can mimic radiologic PCH in some patients (e.g., prematurity/hypoxic injury comprising a minority in an imaging cohort). (zakaria2024classic“pch”genes pages 17-20)

---

## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic themes and causal chains
**Upstream trigger:** biallelic pathogenic variants in genes involved in core RNA processing/translation/metabolism → **cell-type and developmental time-window vulnerability** in hindbrain/cerebellar development → impaired progenitor proliferation/differentiation and/or neurodegeneration → reduced pons/cerebellar growth and associated supratentorial abnormalities → severe motor/cognitive impairment, seizures, feeding/respiratory complications. (dijk2018what’snewin pages 10-11, kagermeier2024humanorganoidmodel pages 1-2)

**Direct abstract quote (mechanistic clarification for a noncoding variant):** the RARS2 Kozak variant “disrupts the consensus Kozak sequence, and has a major impact on RARS2 protein translation.” (nicolle2023anoncodingvariant pages 1-2)

### 6.2 Example: TSEN54 (PCH2A) — neurodevelopmental mechanism supported by organoids (2024)
A 2024 human iPSC-derived **regional organoid** model for genetically homogeneous PCH2A (TSEN54 p.Ala307Ser homozygosity) recapitulated brain-region specific hypoplasia and implicated **altered progenitor proliferation kinetics** rather than apoptosis as an early driver.

**Direct abstract quote:** “PCH2a cerebellar organoids were reduced in size compared to controls starting early in differentiation… Although PCH2a cerebellar organoids did not upregulate apoptosis, their stem cell zones showed altered proliferation kinetics…” (kagermeier2024humanorganoidmodel pages 1-2)

Key quantitative cellular readouts included marked changes in SOX2+ progenitor rosette dynamics (e.g., D30 rosette area 24±3.07% vs 2±0.53% in controls, reversing by D50). (kagermeier2024humanorganoidmodel pages 6-8)

### 6.3 Example: CLP1 (PCH10) — tRNA processing and neurodegeneration
CLP1 is described as an RNA kinase required for tRNA splicing/maturation; pathogenic variants impair kinase activity and tRNA processing, with proposed mechanisms including abnormal accumulation of tRNA fragments and broader transcriptional consequences (e.g., reduced mRNA isoform diversity). (cavusoglu2024evaluationofthe pages 11-12)

### 6.4 Example: EXOSC3 (PCH1B) — RNA exosome/ribosome biogenesis signaling
EXOSC genes encode core exosome proteins; exosome dysfunction is linked (via cited literature within cohort review) to disrupted ribosome biogenesis and p53-dependent signaling, offering a mechanistic bridge from RNA processing defects to neurodevelopmental/neurodegenerative phenotypes. (cavusoglu2024evaluationofthe pages 10-11)

### 6.5 Example: RARS2 (PCH6) — mitochondrial translation and metabolic decompensation
RARS2 encodes mitochondrial arginyl‑tRNA synthetase; PCH6 is framed as a mitochondrial disorder with epilepsy/encephalopathy and potential lactic acidosis/respiratory chain defects. (ghasemi2024broadeningthephenotype pages 11-13, dijk2018what’snewin pages 6-7)

### 6.6 Suggested ontology mappings
**GO Biological Process (examples; verify IDs):**
* tRNA processing / tRNA splicing
* mitochondrial translation
* RNA catabolic process / RNA processing
* ribosome biogenesis
* neural precursor cell proliferation

**Cell types (Cell Ontology; examples):**
* Purkinje cell (cerebellum) (implicated by high cerebellar vulnerability and prior models; Purkinje markers present in organoids) (kagermeier2024humanorganoidmodel pages 2-4)
* Neural progenitor cell / radial glia-like progenitors (SOX2+ rosettes) (kagermeier2024humanorganoidmodel pages 6-8)

**Subcellular components (GO CC; examples):**
* mitochondrion (RARS2)
* cytosol/nucleus (RNA processing)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary: central nervous system, especially **hindbrain**.
* **Pons** and **cerebellum** are obligatorily reduced in classic definitions and imaging cohorts. (zakaria2024classic“pch”genes pages 1-4)
Secondary/variable: supratentorial structures (corpus callosum, cortex, white matter) frequently involved in radiologic cohorts. (zakaria2024classic“pch”genes pages 4-7)

### 7.2 Suggested anatomy ontology mappings
* UBERON (examples; verify IDs): pons, cerebellum, cerebellar vermis, cerebellar hemisphere, corpus callosum, cerebral white matter.

---

## 8. Temporal Development

### 8.1 Onset
Typically prenatal detection is possible, but reductions may be subtle early; fetal MRI at 20–25 weeks and repeat at 30–34 weeks is proposed for suspected cases. (kukulka2025pontocerebellarhypoplasiaa pages 11-13)

### 8.2 Progression
Serial imaging is emphasized because reduced growth trajectories or progressive volume loss may be necessary to establish the diagnosis and characterize evolving brain involvement. (kukulka2025pontocerebellarhypoplasiaa pages 11-13)

---

## 9. Inheritance and Population

### 9.1 Inheritance patterns
Classic PCH subtypes are predominantly **autosomal recessive**. (dijk2018what’snewin pages 1-3)
Population structure can strongly influence apparent frequencies (e.g., high consanguinity and recurrent founder variants in certain cohorts). (cavusoglu2024evaluationofthe pages 1-2)

### 9.2 Epidemiology
Incidence/prevalence estimates were not available in the retrieved evidence set. An older review explicitly states that “The incidence of each subtype is unknown.” ()

---

## 10. Diagnostics

### 10.1 Imaging (MRI) and radiologic criteria
MRI is central. One cohort operationalized criteria including:
* Pons hypoplasia defined by **CC pons:CC midbrain <1.5** and/or **AP pons < AP midbrain**.
* Vermis hypoplasia defined as **vermis height or AP vermis diameter <3rd percentile** versus age/sex norms. (zakaria2024classic“pch”genes pages 1-4)

Radiologic patterns used for subtype/differential orientation include **“dragonfly”** and **“butterfly”** cerebellar configurations and a **“figure-of-8” midbrain** pattern (notably associated with AMPD2/PCH9 in reviewed sources). (dijk2018what’snewin pages 6-7, cavusoglu2024evaluationofthe pages 2-5)

### 10.2 Genetic testing approach
Because classic PCH genes may explain only a minority of imaging-defined PCH, broad genetic testing is recommended:
* **Chromosomal microarray (CMA)** plus **exome sequencing or multigene panels** in individuals with PCH-like imaging. (zakaria2024classic“pch”genes pages 1-4)

Where a distinctive imaging/clinical profile exists, targeted testing for known recurrent variants (e.g., TSEN54 p.A307S) is suggested in reviews, with WES for broader detection given ongoing gene discovery. (dijk2018what’snewin pages 13-14)

### 10.3 Metabolic / laboratory workup
A Turkish multicenter study describes routine biochemical/metabolic investigations in evaluation, listing tests such as amino acids (urine/blood), tandem MS, organic acids, VLCFA, biotinidase, and transferrin studies. (cavusoglu2024evaluationofthe pages 1-2)

### 10.4 Differential diagnosis
Differentials include acquired and metabolic mimics and numerous genetic disorders producing PCH-like imaging (e.g., tubulinopathies, CASK, RELN, VLDLR-related disorders, and congenital disorders of glycosylation). (zakaria2024classic“pch”genes pages 1-4, kukulka2025pontocerebellarhypoplasiaa pages 6-7)

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality (recent data)
Prognosis is often poor, but varies widely by etiology and subtype.

**Radiologic PCH cohort (n=38, 2024):** mortality 36%, with median age at death 8 months (mean 17 months). (zakaria2024classic“pch”genes pages 4-7)

Older reviews characterize prognosis as poor with frequent death in infancy/childhood for classic subtypes, consistent with the above cohort. (dijk2018what’snewin pages 1-3)

### 11.2 Morbidity and function
Severe disability is common in imaging-defined cohorts: non-verbal 50%, non-ambulatory 64%, and gastrostomy feeding 45% were reported in one radiologic cohort. (zakaria2024classic“pch”genes pages 4-7)

---

## 12. Treatment

### 12.1 Standard of care: supportive / symptomatic
No disease-modifying therapies were identified in the retrieved clinical literature excerpts; management is multidisciplinary supportive care addressing feeding, ventilation/respiratory issues, seizures, movement disorders, orthopedic complications, and palliative care as needed. (kukulka2025pontocerebellarhypoplasiaa pages 11-13, dijk2018what’snewin pages 6-7)

Specific supportive recommendations highlighted in a review include sleep monitoring for life‑threatening apnea in PCH2A, common need for gavage/PEG feeding, physiotherapy and assistive devices, and symptomatic seizure management (phenobarbital/topiramate mentioned in reported series). (dijk2018what’snewin pages 6-7)

**Suggested MAXO terms (examples; verify IDs):**
* gastrostomy tube placement
* enteral nutrition
* antiepileptic drug therapy
* ventilatory support
* physical therapy / occupational therapy / speech therapy
* palliative care

### 12.2 Experimental / clinical trials (real-world implementations)

**Vatiquinone (PTC743/EPI-743) trial including PCH6 (RARS2):**
ClinicalTrials.gov NCT04378075 evaluated vatiquinone for mitochondrial disease with refractory epilepsy and explicitly included **“Pontocerebellar Hypoplasia Type 6”** among eligible conditions. It was a randomized, double‑blind, placebo‑controlled Phase 2/3 trial (n=68), with primary outcome percent change in observable motor seizure frequency at Week 24; it started 2020‑09‑28, primary completion 2023‑03‑18, completion 2023‑12‑27, and was terminated due to sponsor decision. (NCT04378075 chunk 1, NCT04378075 chunk 2)

URL: https://clinicaltrials.gov/study/NCT04378075 (record referenced by retrieved excerpts) (NCT04378075 chunk 1)

An observational study of isolated small cerebellum (NCT03572868) is relevant to cerebellar hypoplasia outcomes broadly but is not genotype-specific to PCH. (NCT03572868 chunk 1)

URL: https://clinicaltrials.gov/study/NCT03572868 (NCT03572868 chunk 1)

---

## 13. Prevention
No primary prevention is available for most PCH because it is primarily genetic. Secondary prevention focuses on **genetic counseling** and availability of **prenatal testing** once familial pathogenic variants are known (a capability emphasized historically in foundational reviews). ()

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary PCH syndromes were characterized in the retrieved excerpts. However, cross-species modeling is discussed for TSEN54 and related pathways (with limitations due to conservation). (kagermeier2024humanorganoidmodel pages 2-2)

---

## 15. Model Organisms / Model Systems

### 15.1 Human iPSC / organoid models (2024)
A 2024 Disease Models & Mechanisms study established patient-derived iPSC lines (TSEN54 p.Ala307Ser homozygous) and generated **cerebellar and neocortical organoids** reproducing region‑specific growth deficits and altered progenitor dynamics without increased apoptosis. (kagermeier2024humanorganoidmodel pages 1-2, kagermeier2024humanorganoidmodel pages 6-8)

### 15.2 Animal models (limitations + utility)
Animal models for TSEN54 loss can be embryonic lethal and may not reproduce the human region-specific phenotype; species differences in residue conservation are highlighted as a rationale for human organoid modeling. (kagermeier2024humanorganoidmodel pages 2-2)

---

## Recent developments and expert analysis (prioritizing 2023–2024)

1) **Reframing PCH as a radiologic pattern with diverse etiologies (2024):** A 38‑patient cohort concluded classic OMIM PCH genes underlie only a minority of radiologic PCH and recommended broad testing (CMA + exome/panels). This shifts clinical practice away from assuming “classic PCH” when imaging shows pontocerebellar hypoplasia. (zakaria2024classic“pch”genes pages 1-4)

2) **Largest retrieved genetically confirmed national cohort (2024, Turkey):** CLP1 was the most common gene in this cohort, with high homozygosity and consanguinity rates, emphasizing how founder effects and population structure shape observed gene distributions. (cavusoglu2024evaluationofthe pages 1-2, cavusoglu2024evaluationofthe pages 2-5)

3) **Human mechanistic modeling advances (2024):** Regionalized neural organoids for PCH2A provide a direct human experimental system supporting a **neurodevelopmental progenitor proliferation** mechanism (at least early), which can inform target discovery and phenotypic screening endpoints. (kagermeier2024humanorganoidmodel pages 1-2, kagermeier2024humanorganoidmodel pages 6-8)

4) **Noncoding variant interpretation (2023):** The RARS2 Kozak-sequence work demonstrates that pathogenicity in PCH can arise from variants outside coding regions and highlights limitations of mRNA-level assessment alone for noncoding variants. (nicolle2023anoncodingvariant pages 1-2)

---

## Structured summary table
| PCH entity | Key gene(s) / representative variant(s) | Inheritance (if stated) | Hallmark imaging patterns | Key clinical features | Key quantitative statistics | Primary supporting citation IDs |
|---|---|---|---|---|---|---|
| Radiologic PCH cohort (Zakaria 2024) | Heterogeneous causes; classic OMIM PCH genes rare (only 1 patient). Identified etiologies included chromosomal causes and monogenic causes such as **POMGNT1, CASK, AIMP1, ASPM, CHD7, DHCR7, NFIX, OFD1, VLDLR** | Not uniform; chromosomal, monogenic, and acquired etiologies all represented | Universal pons + cerebellar vermis hypoplasia; cerebellar hemisphere hypoplasia in many; “butterfly” pattern common among hemisphere-hypoplasia cases; supratentorial anomalies frequent; no cerebellar atrophy in this cohort | Global developmental delay in all; frequent feeding and respiratory problems, hypotonia, microcephaly, epilepsy, sensory impairment; poor neurodevelopmental outcomes | **n=38**; pons/vermis hypoplasia **100%**; hemisphere hypoplasia **63%**; supratentorial anomalies **71%**; etiologic diagnosis **65%** overall (**21% chromosomal, 34% monogenic, 10% acquired**); non-verbal **50%**; non-ambulatory **64%**; gastrostomy **45%**; mortality **36%**, median age at death **8 months** (zakaria2024classic“pch”genes pages 4-7, zakaria2024classic“pch”genes pages 1-4) | (zakaria2024classic“pch”genes pages 4-7, zakaria2024classic“pch”genes pages 1-4, zakaria2024classic“pch”genes pages 17-20) |
| Genetically confirmed Turkish PCH cohort (Cavusoglu 2024) | Most common **CLP1** c.419G>A (**p.Arg140His**); recurrent **TSEN54** c.919G>T (**p.Ala307Ser**); also **EXOSC3, RARS2, MINPP1, AMPD2, CHMP1A, SEPSECS, TSEN2, TSEN34, TBC1D23, HEATR5B** | Predominantly **autosomal recessive**; homozygous variants common | “Dragonfly” cerebellum (esp. TSEN54/AMPD2), “butterfly” pattern (EXOSC3), flattened pons (CLP1), “figure-of-8” midbrain (AMPD2) | Nearly universal neurodevelopmental impairment with microcephaly, seizures, eye abnormalities, cerebellar/brainstem signs, hypotonia/spasticity; broad genotype-phenotype variability | **n=64**; female **43.8%**, male **56.3%**; homozygous mutations **89.1%**; consanguinity **79.7%**; microcephaly **91.3%**; psychomotor retardation **98.4%**; abnormal neurologic findings **100%**; seizures **63.8%** overall; brainstem signs **55.3%**; cerebellar deficits **67.3%**; eye abnormalities **69.8%**; CLP1 cases **26.56%** of cohort (cavusoglu2024evaluationofthe pages 1-2, cavusoglu2024evaluationofthe pages 2-5) | (cavusoglu2024evaluationofthe pages 1-2, cavusoglu2024evaluationofthe pages 2-5, cavusoglu2024evaluationofthe pages 11-12, cavusoglu2024evaluationofthe pages 10-11, cavusoglu2024evaluationofthe pages 12-14) |
| PCH2A / TSEN54-associated disease | **TSEN54** founder missense c.919G>T (**p.Ala307Ser**); more severe related phenotypes with p.A307S plus loss-of-function/splice variants in TSEN54 | **Autosomal recessive** | Classic **“dragonfly” cerebellar** pattern; pontocerebellar hypoplasia/atrophy; progressive microcephaly | Prenatal/infantile onset; severe developmental impairment, extrapyramidal dyskinesia/choreoathetosis, feeding problems, sleep apnea, seizures; genotype-phenotype correlation with more severe neonatal phenotypes for TSEN54 compound heterozygosity | Founder genotype highlighted across series; severe structural abnormalities often present at birth; exact cohort size varies by study rather than a single pooled estimate (cavusoglu2024evaluationofthe pages 1-2, dijk2018what’snewin pages 1-3, dijk2018what’snewin pages 3-5, ghasemi2024broadeningthephenotype pages 6-7, dijk2018what’snewin pages 13-14) | (cavusoglu2024evaluationofthe pages 1-2, dijk2018what’snewin pages 1-3, dijk2018what’snewin pages 3-5, ghasemi2024broadeningthephenotype pages 6-7, dijk2018what’snewin pages 13-14) |
| PCH2A human organoid model (Kagermeier 2024) | Patient-derived iPSCs with homozygous **TSEN54** c.919G>T (**p.Ala307Ser**) | Human model of an **AR** disorder | Region-specific size reduction reproduced in vitro: cerebellar organoids smaller early; neocortical organoids milder/later deficit; altered SOX2+ rosette dynamics rather than increased apoptosis | Supports a neurodevelopmental component with altered neural progenitor proliferation kinetics and cerebellar-selective vulnerability | **3 patient lines + 3 controls**; cerebellar organoid size difference from **day 10**, neocortical from **day 30**; SOX2+ rosette area at D30 **24±3.07%** in PCH2A vs **2±0.53%** control, reversing by D50 (**2±0.92%** vs **12±1.24%**); no significant apoptosis increase (kagermeier2024humanorganoidmodel pages 6-8, kagermeier2024humanorganoidmodel pages 8-10, kagermeier2024humanorganoidmodel pages 2-2, kagermeier2024humanorganoidmodel pages 1-2) | (kagermeier2024humanorganoidmodel pages 6-8, kagermeier2024humanorganoidmodel pages 8-10, kagermeier2024humanorganoidmodel pages 2-2, kagermeier2024humanorganoidmodel pages 1-2, kagermeier2024humanorganoidmodel pages 2-4) |
| PCH6 / RARS2-associated disease | **RARS2**; noncoding Kozak/promoter-5'UTR variant **NM_020320.3:c.-2A>G** causing major protein-level reduction | **Biallelic / autosomal recessive** | Pontocerebellar involvement with often rapid supratentorial atrophy; mitochondrial-disease context; diffusion imaging may help detect metabolic decompensation in mimics/related cases | Early-onset encephalopathy with severe epilepsy/epileptic encephalopathy; may have lactic acidosis and mitochondrial respiratory chain defects, although lactic acidosis may be absent in some patients | New 2023 paper reports an additional homozygous case with phenotype consistent with PCH6; prior work showed ~**40% mRNA reduction**, while this study showed a **major decrease in protein translation** due to Kozak disruption (ghasemi2024broadeningthephenotype pages 11-13, nicolle2023anoncodingvariant pages 1-2) | (ghasemi2024broadeningthephenotype pages 11-13, nicolle2023anoncodingvariant pages 1-2, dijk2018what’snewin pages 6-7, kukulka2025pontocerebellarhypoplasiaa pages 6-7) |
| PCH1B / EXOSC3-associated disease | **EXOSC3**; recurrent missense variants include **c.395A>C (p.Asp132Ala)** and **c.572G>A (p.Gly191Asp)** | **Autosomal recessive** | Often “butterfly” cerebellar pattern; hypoplasia/atrophy of pons and cerebellum with vermis and hemispheres similarly affected; intracerebellar cysts less common | PCH1 phenotype with anterior horn involvement/motor neuron disease spectrum, hypotonia, weakness, respiratory insufficiency, congenital contractures; some genotypes milder and longer-surviving | EXOSC3 variants account for about **half of PCH1** in older literature; reported mean age at death **9 months** in EXOSC3-mutated cases vs **3 months** in non-EXOSC3 PCH1 in one review summary; in Turkish cohort EXOSC3 cases were **10.9%** (dijk2018what’snewin pages 3-5, cavusoglu2024evaluationofthe pages 10-11, baas2020exosc3pontocerebellarhypoplasia pages 1-4) | (dijk2018what’snewin pages 3-5, cavusoglu2024evaluationofthe pages 10-11, baas2020exosc3pontocerebellarhypoplasia pages 1-4) |
| PCH9 / AMPD2-associated disease | **AMPD2**; multiple homozygous variants reported across series | **Autosomal recessive** | **Dragonfly** cerebellar atrophy/hypoplasia, reduced pons and middle cerebellar peduncles, **“figure-of-8” midbrain**, severe white-matter loss/periventricular leukomalacia-like change, thin/absent corpus callosum | Severe prenatal/early infantile neurodevelopmental disorder with profound delay and microcephaly | MRI phenotype reported as consistent across small published case series; Turkish cohort also linked AMPD2 with dragonfly/figure-of-8 patterns (cavusoglu2024evaluationofthe pages 1-2, cavusoglu2024evaluationofthe pages 11-12) | (cavusoglu2024evaluationofthe pages 1-2, cavusoglu2024evaluationofthe pages 11-12, dijk2018what’snewin pages 6-7) |
| General mechanistic framework (van Dijk 2018; Namavar 2011) | Many genes converge on **RNA processing / translation / tRNA biology**: **TSEN54, TSEN2, TSEN34, TSEN15, CLP1, RARS2, EXOSC3, EXOSC8, EXOSC9**; additional non-RNA genes include **AMPD2, CHMP1A, SLC25A46, PCLO** | Classical PCH subtypes described as largely **autosomal recessive** | Shared core pattern is pontine + cerebellar hypoplasia/atrophy, often with progressive microcephaly and variable supratentorial abnormalities | Severe motor/cognitive disability, feeding/swallowing dysfunction, epilepsy, poor developmental progress; PCH1 includes spinal motor neuron degeneration; prognosis generally poor | Older synthesis: incidence of each subtype unknown; most patients die in **infancy or childhood**; 2018 review notes **17 PCH-related genes** in OMIM at that time, while later reviews report **17 types / 25 genes** or more depending on classification date (ghasemi2024broadeningthephenotype pages 1-2, dijk2018what’snewin pages 1-3, dijk2018what’snewin pages 10-11) | (ghasemi2024broadeningthephenotype pages 1-2, dijk2018what’snewin pages 1-3, dijk2018what’snewin pages 10-11) |


*Table: This table condenses the major PCH entities and evidence types retrieved, linking genes, imaging patterns, clinical manifestations, and the most useful recent quantitative findings. It is designed as a high-density reference for disease knowledge base curation and evidence tracing.*

---

## Key URLs and publication dates (from retrieved records)
* Zakaria et al., “Classic ‘PCH’ Genes are a Rare Cause of Radiologic Pontocerebellar Hypoplasia” — 2024-03; https://doi.org/10.1007/s12311-023-01544-2 (zakaria2024classic“pch”genes pages 1-4)
* Cavusoglu et al., “Evaluation of the Patients with the Diagnosis of Pontocerebellar Hypoplasia: A Multicenter National Study” — 2024-04; https://doi.org/10.1007/s12311-024-01690-1 (cavusoglu2024evaluationofthe pages 1-2)
* Kagermeier et al., “Human organoid model of pontocerebellar hypoplasia 2a…” — 2024-07; https://doi.org/10.1242/dmm.050740 (kagermeier2024humanorganoidmodel pages 1-2)
* Nicolle et al., “A non-coding variant in the Kozak sequence of RARS2…” — 2023-06; https://doi.org/10.1186/s12920-023-01582-z (nicolle2023anoncodingvariant pages 1-2)
* ClinicalTrials.gov: NCT04378075 — trial start 2020-09-28; terminated; https://clinicaltrials.gov/study/NCT04378075 (NCT04378075 chunk 1)

---

## Limitations of this report
* The retrieved evidence did not include explicit OMIM/Orphanet/ICD/MeSH/MONDO identifiers or PMIDs in the text excerpts; therefore, identifier code strings and PMID-based citations could not be provided from tool evidence and should be supplemented by direct queries to OMIM/Orphanet/NCBI MeSH. (cavusoglu2024evaluationofthe pages 1-2, kukulka2025pontocerebellarhypoplasiaa pages 11-13)
* Epidemiologic prevalence/incidence and variant carrier frequency data were not present in the retrieved excerpts. ()


References

1. (cavusoglu2024evaluationofthe pages 1-2): Dilek Cavusoglu, Gulten Ozturk, Dilsad Turkdogan, Semra Hiz Kurul, Uluc Yis, Mustafa Komur, Faruk Incecik, Bulent Kara, Turkan Sahin, Olcay Unver, Cengiz Dilber, Gulen Gul Mert, Cagatay Gunay, Gamze Sarikaya Uzan, Ozlem Ersoy, Yavuz Oktay, Serdar Mermer, Gokcen Oz Tuncer, Olcay Gungor, Gul Demet Kaya Ozcora, Ugur Gumus, Ozlem Sezer, Gokhan Ozan Cetin, Fatma Demir, Arzu Yilmaz, Gurkan Gurbuz, Meral Topcu, Haluk Topaloglu, Ahmet Cevdet Ceylan, Serdar Ceylaner, Joseph G. Gleeson, Dilara Fusun Icagasioglu, and F. Mujgan Sonmez. Evaluation of the patients with the diagnosis of pontocerebellar hypoplasia: a multicenter national study. Cerebellum (London, England), 23:1950-1965, Apr 2024. URL: https://doi.org/10.1007/s12311-024-01690-1, doi:10.1007/s12311-024-01690-1. This article has 10 citations.

2. (kukulka2025pontocerebellarhypoplasiaa pages 11-13): Natalie A Kukulka, Shriya Singh, Matthew T Whitehead, William B Dobyns, Taeun Chang, and Youssef A Kousa. Pontocerebellar hypoplasia: a review from 1912 to 2022. Brain Communications, Aug 2025. URL: https://doi.org/10.1093/braincomms/fcaf298, doi:10.1093/braincomms/fcaf298. This article has 3 citations and is from a peer-reviewed journal.

3. (dijk2018what’snewin pages 1-3): Tessa van Dijk, Frank Baas, Peter G. Barth, and Bwee Tien Poll-The. What’s new in pontocerebellar hypoplasia? an update on genes and subtypes. Orphanet Journal of Rare Diseases, Jun 2018. URL: https://doi.org/10.1186/s13023-018-0826-2, doi:10.1186/s13023-018-0826-2. This article has 187 citations and is from a peer-reviewed journal.

4. (zakaria2024classic“pch”genes pages 1-4): Rohaya Binti Mohamad Zakaria, Maisa Malta, Felixe Pelletier, Nassima Addour-Boudrahem, Elana Pinchefsky, Christine Saint Martin, and Myriam Srour. Classic “pch” genes are a rare cause of radiologic pontocerebellar hypoplasia. The Cerebellum, pages 1-13, Mar 2024. URL: https://doi.org/10.1007/s12311-023-01544-2, doi:10.1007/s12311-023-01544-2. This article has 6 citations.

5. (kukulka2025pontocerebellarhypoplasiaa pages 13-14): Natalie A Kukulka, Shriya Singh, Matthew T Whitehead, William B Dobyns, Taeun Chang, and Youssef A Kousa. Pontocerebellar hypoplasia: a review from 1912 to 2022. Brain Communications, Aug 2025. URL: https://doi.org/10.1093/braincomms/fcaf298, doi:10.1093/braincomms/fcaf298. This article has 3 citations and is from a peer-reviewed journal.

6. (kagermeier2024humanorganoidmodel pages 1-2): Theresa Kagermeier, Stefan Hauser, Kseniia Sarieva, Lucia Laugwitz, Samuel Groeschel, Wibke G. Janzarik, Zeynep Yentür, Katharina Becker, Ludger Schöls, Ingeborg Krägeloh-Mann, and Simone Mayer. Human organoid model of pontocerebellar hypoplasia 2a recapitulates brain region-specific size differences. Disease Models & Mechanisms, Jul 2024. URL: https://doi.org/10.1242/dmm.050740, doi:10.1242/dmm.050740. This article has 10 citations and is from a domain leading peer-reviewed journal.

7. (NCT04378075 chunk 1):  A Study to Evaluate Efficacy and Safety of Vatiquinone for Treating Mitochondrial Disease in Participants With Refractory Epilepsy. PTC Therapeutics. 2020. ClinicalTrials.gov Identifier: NCT04378075

8. (NCT03572868 chunk 1):  Long-term Outcome of Newborns With an Isolated Small Cerebellum. Hospices Civils de Lyon. 2018. ClinicalTrials.gov Identifier: NCT03572868

9. (dijk2018what’snewin pages 10-11): Tessa van Dijk, Frank Baas, Peter G. Barth, and Bwee Tien Poll-The. What’s new in pontocerebellar hypoplasia? an update on genes and subtypes. Orphanet Journal of Rare Diseases, Jun 2018. URL: https://doi.org/10.1186/s13023-018-0826-2, doi:10.1186/s13023-018-0826-2. This article has 187 citations and is from a peer-reviewed journal.

10. (ghasemi2024broadeningthephenotype pages 11-13): Mohammad-Reza Ghasemi, Sahand Tehrani Fateh, Aysan Moeinafshar, Hossein Sadeghi, Parvaneh Karimzadeh, Reza Mirfakhraie, Mitra Rezaei, Farzad Hashemi-Gorji, Morteza Rezvani Kashani, Fatemehsadat Fazeli Bavandpour, Saman Bagheri, Parinaz Moghimi, Masoumeh Rostami, Rasoul Madannejad, Hassan Roudgari, and Mohammad Miryounesi. Broadening the phenotype and genotype spectrum of novel mutations in pontocerebellar hypoplasia with a comprehensive molecular literature review. BMC Medical Genomics, Feb 2024. URL: https://doi.org/10.1186/s12920-024-01810-0, doi:10.1186/s12920-024-01810-0. This article has 13 citations and is from a peer-reviewed journal.

11. (zakaria2024classic“pch”genes pages 17-20): Rohaya Binti Mohamad Zakaria, Maisa Malta, Felixe Pelletier, Nassima Addour-Boudrahem, Elana Pinchefsky, Christine Saint Martin, and Myriam Srour. Classic “pch” genes are a rare cause of radiologic pontocerebellar hypoplasia. The Cerebellum, pages 1-13, Mar 2024. URL: https://doi.org/10.1007/s12311-023-01544-2, doi:10.1007/s12311-023-01544-2. This article has 6 citations.

12. (zakaria2024classic“pch”genes pages 4-7): Rohaya Binti Mohamad Zakaria, Maisa Malta, Felixe Pelletier, Nassima Addour-Boudrahem, Elana Pinchefsky, Christine Saint Martin, and Myriam Srour. Classic “pch” genes are a rare cause of radiologic pontocerebellar hypoplasia. The Cerebellum, pages 1-13, Mar 2024. URL: https://doi.org/10.1007/s12311-023-01544-2, doi:10.1007/s12311-023-01544-2. This article has 6 citations.

13. (cavusoglu2024evaluationofthe pages 2-5): Dilek Cavusoglu, Gulten Ozturk, Dilsad Turkdogan, Semra Hiz Kurul, Uluc Yis, Mustafa Komur, Faruk Incecik, Bulent Kara, Turkan Sahin, Olcay Unver, Cengiz Dilber, Gulen Gul Mert, Cagatay Gunay, Gamze Sarikaya Uzan, Ozlem Ersoy, Yavuz Oktay, Serdar Mermer, Gokcen Oz Tuncer, Olcay Gungor, Gul Demet Kaya Ozcora, Ugur Gumus, Ozlem Sezer, Gokhan Ozan Cetin, Fatma Demir, Arzu Yilmaz, Gurkan Gurbuz, Meral Topcu, Haluk Topaloglu, Ahmet Cevdet Ceylan, Serdar Ceylaner, Joseph G. Gleeson, Dilara Fusun Icagasioglu, and F. Mujgan Sonmez. Evaluation of the patients with the diagnosis of pontocerebellar hypoplasia: a multicenter national study. Cerebellum (London, England), 23:1950-1965, Apr 2024. URL: https://doi.org/10.1007/s12311-024-01690-1, doi:10.1007/s12311-024-01690-1. This article has 10 citations.

14. (ghasemi2024broadeningthephenotype pages 1-2): Mohammad-Reza Ghasemi, Sahand Tehrani Fateh, Aysan Moeinafshar, Hossein Sadeghi, Parvaneh Karimzadeh, Reza Mirfakhraie, Mitra Rezaei, Farzad Hashemi-Gorji, Morteza Rezvani Kashani, Fatemehsadat Fazeli Bavandpour, Saman Bagheri, Parinaz Moghimi, Masoumeh Rostami, Rasoul Madannejad, Hassan Roudgari, and Mohammad Miryounesi. Broadening the phenotype and genotype spectrum of novel mutations in pontocerebellar hypoplasia with a comprehensive molecular literature review. BMC Medical Genomics, Feb 2024. URL: https://doi.org/10.1186/s12920-024-01810-0, doi:10.1186/s12920-024-01810-0. This article has 13 citations and is from a peer-reviewed journal.

15. (cavusoglu2024evaluationofthe pages 11-12): Dilek Cavusoglu, Gulten Ozturk, Dilsad Turkdogan, Semra Hiz Kurul, Uluc Yis, Mustafa Komur, Faruk Incecik, Bulent Kara, Turkan Sahin, Olcay Unver, Cengiz Dilber, Gulen Gul Mert, Cagatay Gunay, Gamze Sarikaya Uzan, Ozlem Ersoy, Yavuz Oktay, Serdar Mermer, Gokcen Oz Tuncer, Olcay Gungor, Gul Demet Kaya Ozcora, Ugur Gumus, Ozlem Sezer, Gokhan Ozan Cetin, Fatma Demir, Arzu Yilmaz, Gurkan Gurbuz, Meral Topcu, Haluk Topaloglu, Ahmet Cevdet Ceylan, Serdar Ceylaner, Joseph G. Gleeson, Dilara Fusun Icagasioglu, and F. Mujgan Sonmez. Evaluation of the patients with the diagnosis of pontocerebellar hypoplasia: a multicenter national study. Cerebellum (London, England), 23:1950-1965, Apr 2024. URL: https://doi.org/10.1007/s12311-024-01690-1, doi:10.1007/s12311-024-01690-1. This article has 10 citations.

16. (nicolle2023anoncodingvariant pages 1-2): Romain Nicolle, Nami Altin, Karine Siquier-Pernet, Sherlina Salignac, Pierre Blanc, Arnold Munnich, Christine Bole-Feysot, Valérie Malan, Barthélémy Caron, Patrick Nitschké, Isabelle Desguerre, Nathalie Boddaert, Marlène Rio, Antonio Rausell, and Vincent Cantagrel. A non-coding variant in the kozak sequence of rars2 strongly decreases protein levels and causes pontocerebellar hypoplasia. BMC Medical Genomics, Jun 2023. URL: https://doi.org/10.1186/s12920-023-01582-z, doi:10.1186/s12920-023-01582-z. This article has 7 citations and is from a peer-reviewed journal.

17. (cavusoglu2024evaluationofthe pages 10-11): Dilek Cavusoglu, Gulten Ozturk, Dilsad Turkdogan, Semra Hiz Kurul, Uluc Yis, Mustafa Komur, Faruk Incecik, Bulent Kara, Turkan Sahin, Olcay Unver, Cengiz Dilber, Gulen Gul Mert, Cagatay Gunay, Gamze Sarikaya Uzan, Ozlem Ersoy, Yavuz Oktay, Serdar Mermer, Gokcen Oz Tuncer, Olcay Gungor, Gul Demet Kaya Ozcora, Ugur Gumus, Ozlem Sezer, Gokhan Ozan Cetin, Fatma Demir, Arzu Yilmaz, Gurkan Gurbuz, Meral Topcu, Haluk Topaloglu, Ahmet Cevdet Ceylan, Serdar Ceylaner, Joseph G. Gleeson, Dilara Fusun Icagasioglu, and F. Mujgan Sonmez. Evaluation of the patients with the diagnosis of pontocerebellar hypoplasia: a multicenter national study. Cerebellum (London, England), 23:1950-1965, Apr 2024. URL: https://doi.org/10.1007/s12311-024-01690-1, doi:10.1007/s12311-024-01690-1. This article has 10 citations.

18. (kagermeier2024humanorganoidmodel pages 6-8): Theresa Kagermeier, Stefan Hauser, Kseniia Sarieva, Lucia Laugwitz, Samuel Groeschel, Wibke G. Janzarik, Zeynep Yentür, Katharina Becker, Ludger Schöls, Ingeborg Krägeloh-Mann, and Simone Mayer. Human organoid model of pontocerebellar hypoplasia 2a recapitulates brain region-specific size differences. Disease Models & Mechanisms, Jul 2024. URL: https://doi.org/10.1242/dmm.050740, doi:10.1242/dmm.050740. This article has 10 citations and is from a domain leading peer-reviewed journal.

19. (dijk2018what’snewin pages 6-7): Tessa van Dijk, Frank Baas, Peter G. Barth, and Bwee Tien Poll-The. What’s new in pontocerebellar hypoplasia? an update on genes and subtypes. Orphanet Journal of Rare Diseases, Jun 2018. URL: https://doi.org/10.1186/s13023-018-0826-2, doi:10.1186/s13023-018-0826-2. This article has 187 citations and is from a peer-reviewed journal.

20. (kagermeier2024humanorganoidmodel pages 2-4): Theresa Kagermeier, Stefan Hauser, Kseniia Sarieva, Lucia Laugwitz, Samuel Groeschel, Wibke G. Janzarik, Zeynep Yentür, Katharina Becker, Ludger Schöls, Ingeborg Krägeloh-Mann, and Simone Mayer. Human organoid model of pontocerebellar hypoplasia 2a recapitulates brain region-specific size differences. Disease Models & Mechanisms, Jul 2024. URL: https://doi.org/10.1242/dmm.050740, doi:10.1242/dmm.050740. This article has 10 citations and is from a domain leading peer-reviewed journal.

21. (dijk2018what’snewin pages 13-14): Tessa van Dijk, Frank Baas, Peter G. Barth, and Bwee Tien Poll-The. What’s new in pontocerebellar hypoplasia? an update on genes and subtypes. Orphanet Journal of Rare Diseases, Jun 2018. URL: https://doi.org/10.1186/s13023-018-0826-2, doi:10.1186/s13023-018-0826-2. This article has 187 citations and is from a peer-reviewed journal.

22. (kukulka2025pontocerebellarhypoplasiaa pages 6-7): Natalie A Kukulka, Shriya Singh, Matthew T Whitehead, William B Dobyns, Taeun Chang, and Youssef A Kousa. Pontocerebellar hypoplasia: a review from 1912 to 2022. Brain Communications, Aug 2025. URL: https://doi.org/10.1093/braincomms/fcaf298, doi:10.1093/braincomms/fcaf298. This article has 3 citations and is from a peer-reviewed journal.

23. (NCT04378075 chunk 2):  A Study to Evaluate Efficacy and Safety of Vatiquinone for Treating Mitochondrial Disease in Participants With Refractory Epilepsy. PTC Therapeutics. 2020. ClinicalTrials.gov Identifier: NCT04378075

24. (kagermeier2024humanorganoidmodel pages 2-2): Theresa Kagermeier, Stefan Hauser, Kseniia Sarieva, Lucia Laugwitz, Samuel Groeschel, Wibke G. Janzarik, Zeynep Yentür, Katharina Becker, Ludger Schöls, Ingeborg Krägeloh-Mann, and Simone Mayer. Human organoid model of pontocerebellar hypoplasia 2a recapitulates brain region-specific size differences. Disease Models & Mechanisms, Jul 2024. URL: https://doi.org/10.1242/dmm.050740, doi:10.1242/dmm.050740. This article has 10 citations and is from a domain leading peer-reviewed journal.

25. (cavusoglu2024evaluationofthe pages 12-14): Dilek Cavusoglu, Gulten Ozturk, Dilsad Turkdogan, Semra Hiz Kurul, Uluc Yis, Mustafa Komur, Faruk Incecik, Bulent Kara, Turkan Sahin, Olcay Unver, Cengiz Dilber, Gulen Gul Mert, Cagatay Gunay, Gamze Sarikaya Uzan, Ozlem Ersoy, Yavuz Oktay, Serdar Mermer, Gokcen Oz Tuncer, Olcay Gungor, Gul Demet Kaya Ozcora, Ugur Gumus, Ozlem Sezer, Gokhan Ozan Cetin, Fatma Demir, Arzu Yilmaz, Gurkan Gurbuz, Meral Topcu, Haluk Topaloglu, Ahmet Cevdet Ceylan, Serdar Ceylaner, Joseph G. Gleeson, Dilara Fusun Icagasioglu, and F. Mujgan Sonmez. Evaluation of the patients with the diagnosis of pontocerebellar hypoplasia: a multicenter national study. Cerebellum (London, England), 23:1950-1965, Apr 2024. URL: https://doi.org/10.1007/s12311-024-01690-1, doi:10.1007/s12311-024-01690-1. This article has 10 citations.

26. (dijk2018what’snewin pages 3-5): Tessa van Dijk, Frank Baas, Peter G. Barth, and Bwee Tien Poll-The. What’s new in pontocerebellar hypoplasia? an update on genes and subtypes. Orphanet Journal of Rare Diseases, Jun 2018. URL: https://doi.org/10.1186/s13023-018-0826-2, doi:10.1186/s13023-018-0826-2. This article has 187 citations and is from a peer-reviewed journal.

27. (ghasemi2024broadeningthephenotype pages 6-7): Mohammad-Reza Ghasemi, Sahand Tehrani Fateh, Aysan Moeinafshar, Hossein Sadeghi, Parvaneh Karimzadeh, Reza Mirfakhraie, Mitra Rezaei, Farzad Hashemi-Gorji, Morteza Rezvani Kashani, Fatemehsadat Fazeli Bavandpour, Saman Bagheri, Parinaz Moghimi, Masoumeh Rostami, Rasoul Madannejad, Hassan Roudgari, and Mohammad Miryounesi. Broadening the phenotype and genotype spectrum of novel mutations in pontocerebellar hypoplasia with a comprehensive molecular literature review. BMC Medical Genomics, Feb 2024. URL: https://doi.org/10.1186/s12920-024-01810-0, doi:10.1186/s12920-024-01810-0. This article has 13 citations and is from a peer-reviewed journal.

28. (kagermeier2024humanorganoidmodel pages 8-10): Theresa Kagermeier, Stefan Hauser, Kseniia Sarieva, Lucia Laugwitz, Samuel Groeschel, Wibke G. Janzarik, Zeynep Yentür, Katharina Becker, Ludger Schöls, Ingeborg Krägeloh-Mann, and Simone Mayer. Human organoid model of pontocerebellar hypoplasia 2a recapitulates brain region-specific size differences. Disease Models & Mechanisms, Jul 2024. URL: https://doi.org/10.1242/dmm.050740, doi:10.1242/dmm.050740. This article has 10 citations and is from a domain leading peer-reviewed journal.

29. (baas2020exosc3pontocerebellarhypoplasia pages 1-4): F Baas and T van Dijk. Exosc3 pontocerebellar hypoplasia. Unknown journal, 2020.
