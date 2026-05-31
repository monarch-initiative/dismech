---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T17:35:31.573315'
end_time: '2026-04-25T17:49:20.180381'
duration_seconds: 828.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: COPA Syndrome
  mondo_id: MONDO:0014629
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COPA Syndrome
- **MONDO ID:** MONDO:0014629 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COPA Syndrome** covering all of the
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
- **Disease Name:** COPA Syndrome
- **MONDO ID:** MONDO:0014629 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **COPA Syndrome** covering all of the
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


## COPA Syndrome (MONDO:0014629) — Comprehensive Disease Characteristics Report

### Executive summary
COPA syndrome (also termed **autoimmune interstitial lung disease–arthritis syndrome**) is a **Mendelian, autosomal dominant immune-dysregulation disorder** caused by heterozygous variants in **COPA**, encoding the α-subunit of the **COPI** coatomer complex required for Golgi↔ER trafficking. It classically presents in childhood with **diffuse parenchymal lung disease (often with diffuse alveolar hemorrhage), inflammatory arthritis, and variably kidney disease**, with frequent autoantibody positivity and a **type I interferon (IFN-I)–driven** immunophenotype. Key mechanistic work links COPA dysfunction to **mis-trafficking and ligand-independent activation of STING**, and more recent work (2024) expands pathogenic variation beyond the WD40 domain to the **C-terminal domain (CTD)**, implicating **cGAS/STING**, **ER stress**, and **NF-κB signaling** in disease biology. (vece2016copasyndromea pages 2-4, tsui2018analysisofpulmonary pages 8-10, deng2020adefectin pages 1-5, delafontaine2024heterozygousmutationsin pages 1-2)

---

## 1. Disease information

### 1.1 What is COPA syndrome?
COPA syndrome is a **novel autosomal dominant immune dysregulatory disease** centered on **lung**, **joint**, and sometimes **kidney** autoimmunity/inflammation, attributed to pathogenic variants in **COPA**. (vece2016copasyndromea pages 1-2, vece2016copasyndromea pages 2-4)

**Key concept (definition-level):** COPA syndrome is best understood as an **intracellular trafficking disorder with immune dysregulation**, rather than a single-organ disease, because COPA is ubiquitous yet the phenotype localizes to lung/joint/kidney. (vece2016copasyndromea pages 1-2, padureanu2024copasyndrome—frompathogenesis pages 2-4)

### 1.2 Key identifiers and ontology mapping
- **MONDO:** MONDO:0014629 (mapped in Open Targets as “autoimmune interstitial lung disease-arthritis syndrome”). (padureanu2024copasyndrome—frompathogenesis pages 1-2)
- **OMIM:** **616414** (explicitly stated). (kato2021augmentationofstimulator pages 6-10)
- **Gene:** **COPA** (coat protein complex I subunit alpha). (kumrah2019geneticsofcopa pages 1-2)

**Synonyms / alternative names (used in literature/resources):**
- “autoimmune interstitial lung disease-arthritis syndrome” (ontology label). (padureanu2024copasyndrome—frompathogenesis pages 1-2)
- “autoinflammatory interstitial lung, joint, and kidney disease” (terminology used in mechanistic/clinical literature). (kato2021augmentationofstimulator pages 6-10)

**Evidence provenance:** Most detailed disease knowledge is derived from **aggregated disease-level resources (reviews)** and **small cohorts/case series**, given rarity; some clinical data are from international cohorts (e.g., N=14 pulmonary cohort) and multi-family mechanistic studies. (tsui2018analysisofpulmonary pages 8-10, lepelley2020mutationsincopa pages 1-2, padureanu2024copasyndrome—frompathogenesis pages 4-5)

| Concept | Value | Notes/Source |
|---|---|---|
| Disease name | COPA syndrome | Described as a Mendelian immune dysregulation / autoimmune-autoinflammatory syndrome caused by heterozygous COPA mutations; initial disease-defining report published in 2015. DOI: https://doi.org/10.1038/ng.3279 (watkin2015copamutationsimpair pages 1-11, padureanu2024copasyndrome—frompathogenesis pages 1-2) |
| MONDO ID | MONDO:0014629 | Open Targets evidence maps MONDO_0014629 to “autoimmune interstitial lung disease-arthritis syndrome,” corresponding to COPA syndrome nomenclature in current disease ontologies. (padureanu2024copasyndrome—frompathogenesis pages 1-2) |
| Common synonym | autoimmune interstitial lung disease-arthritis syndrome | Used as a disease synonym/label in disease-target resources; consistent with lung and joint-predominant phenotype. (padureanu2024copasyndrome—frompathogenesis pages 1-2) |
| Causal gene | COPA | COPA encodes coat protein complex I subunit alpha (coatomer subunit α), a COPI component involved in Golgi-to-ER retrograde transport. DOI: https://doi.org/10.2147/TACG.S153600 ; https://doi.org/10.1007/s10875-016-0271-8 (kumrah2019geneticsofcopa pages 1-2, vece2016copasyndromea pages 1-2) |
| Inheritance | Autosomal dominant | Repeatedly described as autosomal dominant/heterozygous with variable expressivity or penetrance. DOI: https://doi.org/10.1007/s10875-016-0271-8 ; https://doi.org/10.2147/TACG.S153600 (vece2016copasyndromea pages 1-2, kumrah2019geneticsofcopa pages 1-2) |
| OMIM | 616414 | Explicitly stated in Kato et al. 2021 excerpt: “COPA syndrome (OMIM 616414).” DOI: https://doi.org/10.1002/art.41790 (kato2021augmentationofstimulator pages 6-10) |
| Discovery year | 2015 | First disease-gene report identified COPA mutations in affected families in 2015. DOI: https://doi.org/10.1038/ng.3279 (watkin2015copamutationsimpair pages 1-11) |
| Core clinical triad | Interstitial/diffuse parenchymal lung disease or diffuse alveolar hemorrhage; arthritis; renal disease/glomerulonephritis | Summarized in early clinical series and reviews as the defining phenotype. DOI: https://doi.org/10.1007/s10875-016-0271-8 ; https://doi.org/10.2147/TACG.S153600 (vece2016copasyndromea pages 2-4, kumrah2019geneticsofcopa pages 1-2) |
| Key protein domain (classical disease variants) | N-terminal WD40 domain | Previously recognized pathogenic variants cluster in the N-terminal WD40 domain and impair retrograde cargo retrieval. DOI: https://doi.org/10.1084/jem.20201045 ; https://doi.org/10.1172/JCI163604 (deng2020adefectin pages 1-5, delafontaine2024heterozygousmutationsin pages 2-3) |
| Additional pathogenic domain recognized in 2024 | C-terminal domain (CTD) | Delafontaine et al. 2024 reported CTD variants causing a COPA-related autoinflammatory syndrome and disrupting COPI integrity/function. DOI: https://doi.org/10.1172/JCI163604 (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3) |
| Recurrent/landmark variant | K230N (p.Lys230Asn) | Explicitly mentioned among COPA missense variants in early disease reports/summaries; associated with impaired dilysine cargo binding. DOI: https://doi.org/10.1038/ng.3279 (watkin2015copamutationsimpair pages 1-11, kumrah2019geneticsofcopa pages 2-3) |
| Recurrent/landmark variant | R233H (p.Arg233His) | Reported in multiple families and later cohorts; one of the classic WD40-domain disease variants. DOI: https://doi.org/10.1084/jem.20200600 ; https://doi.org/10.1038/ng.3279 (lepelley2020mutationsincopa pages 1-2, watkin2015copamutationsimpair pages 1-11) |
| Recurrent/landmark variant | E241K (p.Glu241Lys) | Classic WD40-domain variant; modeled in CopaE241K/+ mice and recurrent in human families. DOI: https://doi.org/10.1084/jem.20201045 ; https://doi.org/10.1002/art.41790 (deng2020adefectin pages 1-5, kato2021augmentationofstimulator pages 6-10) |
| Recurrent/landmark variant | D243G (p.Asp243Gly) | Early disease-associated WD40-domain variant from the discovery series. DOI: https://doi.org/10.1038/ng.3279 (watkin2015copamutationsimpair pages 1-11, kumrah2019geneticsofcopa pages 2-3) |
| Additional variant noted in later cohort | D243N (p.Asp243Asn) | Reported in Lepelley et al. cohort alongside p.R233H, expanding residue-243 pathogenic substitutions. DOI: https://doi.org/10.1084/jem.20200600 (lepelley2020mutationsincopa pages 1-2) |
| 2024 CTD variant | p.C1013S | One of three heterozygous C-terminal domain variants reported in 6 children from 3 unrelated families. DOI: https://doi.org/10.1172/JCI163604 (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3) |
| 2024 CTD variant | p.R1058C | C-terminal domain missense variant associated with COPI dysfunction, trafficking defects, and cGAS/STING-dependent IFN signaling. DOI: https://doi.org/10.1172/JCI163604 (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3) |
| 2024 CTD variant | p.R1142X | C-terminal domain nonsense variant reported in the same 2024 JCI series. DOI: https://doi.org/10.1172/JCI163604 (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3) |


*Table: This table summarizes the core identifiers, nomenclature, inheritance, and major pathogenic COPA variants/domains for COPA syndrome. It is useful as a quick reference for knowledge-base curation and genetic interpretation.*

**Recent reference (2024 review):** Padureanu et al., *Diagnostics* (publication: Dec 2024), DOI: https://doi.org/10.3390/diagnostics14242819. (padureanu2024copasyndrome—frompathogenesis pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline **heterozygous** pathogenic variants in **COPA** (autosomal dominant). (kumrah2019geneticsofcopa pages 1-2, vece2016copasyndromea pages 1-2)

**Core molecular function:** COPA is part of the **COPI complex** mediating **Golgi-to-ER retrograde transport** (and more broadly ER–Golgi trafficking). Pathogenic COPA variants impair cargo retrieval/trafficking, setting up downstream immune activation. (kumrah2019geneticsofcopa pages 1-2, padureanu2024copasyndrome—frompathogenesis pages 2-4)

**Key pathogenic variant classes/domains**
- **Classic COPA syndrome variants** cluster in the **N-terminal WD40 domain**, impairing COPA-mediated retrieval of cargo proteins. (deng2020adefectin pages 1-5, delafontaine2024heterozygousmutationsin pages 2-3)
- **New (2024) disease-associated variants** in the **C-terminal domain (CTD)** (p.C1013S, p.R1058C, p.R1142X) can cause a COPA-related autoinflammatory syndrome through COPI integrity/trafficking disruption and distinct mechanistic features (see §6). (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3)

### 2.2 Risk factors
**Genetic risk factor:** carrying a pathogenic heterozygous COPA variant (e.g., **K230N, R233H, E241K, D243G**, and CTD variants). (watkin2015copamutationsimpair pages 1-11, delafontaine2024heterozygousmutationsin pages 2-3)

**Clinical non-penetrance / modifiers:** In one multi-family study, **~30% clinical nonpenetrance** was reported, supporting modifier effects and variable expressivity among carriers. (lepelley2020mutationsincopa pages 4-5)

### 2.3 Protective factors
Direct protective variants are not established in the provided corpus. A 2025 computational/structural hypothesis paper discusses a potentially protective STING haplotype, but this is outside the requested 2023–2024 prioritization and not primary clinical evidence in the present dataset. (padureanu2024copasyndrome—frompathogenesis pages 4-5)

### 2.4 Gene–environment interactions
Evidence for specific environmental triggers (e.g., infection, exposures) driving onset/severity is not explicitly supported by the retrieved text excerpts; this remains an evidence gap in this tool-retrieved set.

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Major phenotype clusters
**A. Pulmonary disease (core):**
- Interstitial/diffuse parenchymal lung disease; cysts on CT; follicular bronchiolitis on biopsy; may progress despite therapy. (tsui2018analysisofpulmonary pages 8-10, tsui2018analysisofpulmonary media 5488c39b)
- **Diffuse alveolar hemorrhage (DAH)** is common and can occur in childhood; in an international cohort (N=14), **DAH occurred in 50%**. (tsui2018analysisofpulmonary pages 8-10, tsui2018analysisofpulmonary media 5488c39b)

**B. Arthritis (core):** inflammatory arthritis/polyarthritis is the most common extra-pulmonary feature. Reviews summarize arthritis in **~95%** of patients; a clinical immunology cohort reported **arthritis 95% (20/21)**. (padureanu2024copasyndrome—frompathogenesis pages 4-5, volpi2018typeiinterferon pages 9-12)

**C. Renal involvement (variable):** immune-complex glomerulonephritis/nephritis occurs in a subset; one summary of the original cohort reported renal involvement in **4/21**. (kumrah2019geneticsofcopa pages 2-3)

**D. Autoantibodies and immune dysregulation:** ANA, ANCA, RF, anti-CCP can be present; one series reported **~80% ANA positivity**; RF positivity was **71%** in one pulmonary cohort. (vece2016copasyndromea pages 2-4, tsui2018analysisofpulmonary pages 8-10)

### 3.2 Onset, severity, and progression
- Early onset is typical: **76%** had symptom onset before age **5** in one clinical series; mean presentation ~**3.5 years** was summarized for the initial cohort. (vece2016copasyndromea pages 2-4, kumrah2019geneticsofcopa pages 2-3)
- Nonetheless, later onset cases exist (including adult onset), indicating a spectrum of expressivity. (padureanu2024copasyndrome—frompathogenesis pages 4-5)
- Longitudinal data show **radiographic improvement** can occur under immunosuppression, but **pulmonary function may decline overall**. (tsui2018analysisofpulmonary pages 8-10)

### 3.3 Suggested HPO terms (with frequencies where available)
| Clinical feature | Suggested HPO term(s) | Typical onset/course | Frequency/statistics (with N if known) | Key evidence/source |
|---|---|---|---|---|
| Interstitial / diffuse parenchymal lung disease | HP:0006530 Interstitial lung disease; HP:0002205 Pulmonary fibrosis (if fibrosing progression); HP:0002093 Respiratory insufficiency (advanced disease) | Usually early childhood onset; often chronic/progressive; pulmonary disease may precede arthritis; median onset 2.5 years in one cohort | Pulmonary involvement 100% (21/21) in Volpi 2018; pulmonary involvement 98% of 59 cases with detailed clinical data in Padureanu 2024 review; all 14/14 in Tsui 2018 had clinically apparent lung disease (volpi2018typeiinterferon pages 9-12, padureanu2024copasyndrome—frompathogenesis pages 4-5, tsui2018analysisofpulmonary pages 8-10) | Volpi 2018 showed universal lung involvement in 21/21; Padureanu 2024 summarized near-universal pulmonary disease; Tsui 2018 international cohort required genetically confirmed lung disease (volpi2018typeiinterferon pages 9-12, padureanu2024copasyndrome—frompathogenesis pages 4-5, tsui2018analysisofpulmonary pages 8-10) |
| Diffuse alveolar hemorrhage | HP:0001892 Pulmonary hemorrhage; HP:0002105 Hemoptysis; HP:0030973 Diffuse alveolar hemorrhage | Often pediatric onset; can be episodic/relapsing; may present in infancy and recur despite treatment | 50% (7/14) in Tsui 2018 cohort; described as frequent and often immune-mediated in Vece 2016; alveolar hemorrhage may occur as early as infancy in Padureanu 2024 (tsui2018analysisofpulmonary pages 8-10, vece2016copasyndromea pages 2-4, padureanu2024copasyndrome—frompathogenesis pages 4-5) | Tsui 2018: DAH in 50% of subjects; Vece 2016 and Padureanu 2024 describe pulmonary hemorrhage as a hallmark manifestation (tsui2018analysisofpulmonary pages 8-10, vece2016copasyndromea pages 2-4, padureanu2024copasyndrome—frompathogenesis pages 4-5) |
| Pulmonary cysts / cystic lung disease | HP:0100607 Pulmonary cyst; HP:0002110 Cystic lung disease | Childhood onset to early adulthood; may slowly progress over time | Common pulmonary CT finding in Tsui 2018; highlighted in imaging/clinical summaries and Padureanu 2024 review, but exact percentage not given in retrieved text (tsui2018analysisofpulmonary pages 8-10, tsui2018analysisofpulmonary media 5488c39b, padureanu2024copasyndrome—frompathogenesis pages 4-5) | Tsui 2018 identified cysts as among the most common pulmonary findings; imaging review in later literature supports cystic changes as characteristic (tsui2018analysisofpulmonary pages 8-10, tsui2018analysisofpulmonary media 5488c39b, padureanu2024copasyndrome—frompathogenesis pages 4-5) |
| Follicular bronchiolitis | HP:0012382 Bronchiolitis; HP:0033379 Follicular bronchiolitis | Chronic airway-centered inflammatory lung disease; often identified on biopsy after pulmonary symptoms | Common biopsy finding in Tsui 2018 and Icelandic family report; no pooled percentage in retrieved text (tsui2018analysisofpulmonary pages 8-10, tsui2018analysisofpulmonary pages 8-8, tsui2018analysisofpulmonary media 5488c39b) | Tsui 2018 reported follicular bronchiolitis as a common histopathologic feature and a diagnostic clue (tsui2018analysisofpulmonary pages 8-10, tsui2018analysisofpulmonary media 5488c39b) |
| Arthritis / inflammatory polyarthritis | HP:0001369 Arthritis; HP:0001371 Flexion contracture (if advanced); HP:0012399 Polyarthritis | Usually early childhood; chronic, inflammatory; may precede or follow lung disease; often non-erosive but variable | 95% (20/21) in Volpi 2018 table; ~95% overall in Padureanu 2024 review; all 14/14 in Tsui 2018 had arthritis (volpi2018typeiinterferon pages 9-12, padureanu2024copasyndrome—frompathogenesis pages 4-5, tsui2018analysisofpulmonary pages 8-10) | Arthritis is the dominant extrapulmonary feature across cohorts and reviews (volpi2018typeiinterferon pages 9-12, padureanu2024copasyndrome—frompathogenesis pages 4-5, tsui2018analysisofpulmonary pages 8-10) |
| Glomerulonephritis / nephritis / renal involvement | HP:0000123 Nephritis; HP:0000099 Glomerulonephritis; HP:0000083 Renal insufficiency; HP:0002907 Hematuria | Variable; less common than lung/joint disease; may emerge later or be absent | Renal disease in 4/21 patients in Watkin cohort summary; Vece 2016 describes renal disease as part of classic triad; nephritis emphasized in mechanistic papers and 2024 CTD series (kumrah2019geneticsofcopa pages 2-3, vece2016copasyndromea pages 2-4, delafontaine2024heterozygousmutationsin pages 1-2) | Watkin cohort summary reported renal involvement in 4/21; renal disease is recognized but less penetrant than lung or arthritis (kumrah2019geneticsofcopa pages 2-3, vece2016copasyndromea pages 2-4, delafontaine2024heterozygousmutationsin pages 1-2) |
| ANA positivity | HP:0012012 Positive antinuclear antibody test | Early in disease course or during autoimmune manifestations; persistent seropositivity is common | ~80% ANA positivity in Vece 2016; ANA/ANCA and/or RF positivity was common in Tsui 2018 cohort (vece2016copasyndromea pages 2-4, tsui2018analysisofpulmonary pages 8-10) | Vece 2016 reported approximately 80% of patients develop positive ANA; Tsui 2018 included ANA positivity among common clues (vece2016copasyndromea pages 2-4, tsui2018analysisofpulmonary pages 8-10) |
| ANCA positivity | HP:0032063 Positive antineutrophil cytoplasmic antibody test | Often accompanies pulmonary/renal autoimmune phenotype | In Tsui 2018, all subjects were positive for ANCA, ANA, or both; exact isolated ANCA frequency not specified in retrieved text; Vece 2016 reports variable cANCA/pANCA positivity (tsui2018analysisofpulmonary pages 8-10, vece2016copasyndromea pages 2-4) | ANCA seropositivity is common and diagnostically useful, especially with lung disease and arthritis (tsui2018analysisofpulmonary pages 8-10, vece2016copasyndromea pages 2-4) |
| Rheumatoid factor positivity | HP:0032060 Rheumatoid factor positive | Often present in inflammatory arthritis phenotype | 71% RF positivity in Tsui 2018 cohort; 43% RF positivity across 32 cases summarized in Kumrah 2019 review (tsui2018analysisofpulmonary pages 8-10, kumrah2019geneticsofcopa pages 2-3) | RF positivity is frequent and may lead to misclassification as juvenile idiopathic arthritis or rheumatoid arthritis (tsui2018analysisofpulmonary pages 8-10, kumrah2019geneticsofcopa pages 2-3) |
| Early childhood onset | HP:0011462 Childhood onset | Usually before age 5 years in many patients; some adult-onset exceptions occur | 76% had symptom onset before age 5 in Vece 2016; mean age at presentation 3.5 years in Watkin cohort summary; median onset 2.5 years in Lepelley 2020 cohort (vece2016copasyndromea pages 2-4, kumrah2019geneticsofcopa pages 2-3, lepelley2020mutationsincopa pages 1-2) | COPA syndrome is predominantly pediatric-onset, though later-onset milder disease is recognized (vece2016copasyndromea pages 2-4, kumrah2019geneticsofcopa pages 2-3, lepelley2020mutationsincopa pages 1-2) |
| Incomplete penetrance / variable expressivity | HP:0003828 Variable expressivity | Markedly variable; asymptomatic mutation carriers occur; multisystem severity ranges from mild to life-threatening | ~30% clinical nonpenetrance in Lepelley 2020 families; Vece 2016 describes variable expressivity (lepelley2020mutationsincopa pages 4-5, vece2016copasyndromea pages 1-2) | Family studies show unaffected heterozygous carriers and broad phenotypic variability, supporting age- and modifier-dependent penetrance (lepelley2020mutationsincopa pages 4-5, vece2016copasyndromea pages 1-2) |
| Th17 skewing / elevated pro-inflammatory cytokines | HP:0012403 Abnormal T-helper 17 cell physiology; HP:0031784 Increased circulating interleukin-17 level; HP:0011137 Abnormal cytokine level | Chronic immunologic abnormality; likely upstream to ongoing autoimmunity/inflammation | Reported qualitatively in Vece 2016 and reviews; no robust pooled frequency in retrieved text | Vece 2016 described increased Th17 cells and increased IL-1β, IL-6, IL-23; Padureanu 2024 links altered thymic selection and Th17 skewing to disease biology (vece2016copasyndromea pages 2-4, padureanu2024copasyndrome—frompathogenesis pages 2-4) |
| Type I interferon signature / interferonopathy | HP:0034363 Increased interferon signature; HP:0011137 Abnormal cytokine level | Constitutive/chronic immune activation; detectable across serial samples; supports interferonopathy classification | Upregulation demonstrated in index case plus 4 additional COPA patients in Volpi 2018; persistent type I IFN signaling described in Lepelley 2020 and mechanistic studies (volpi2018typeiinterferon pages 9-12, lepelley2020mutationsincopa pages 1-2, deng2020adefectin pages 1-5) | Volpi 2018: “The upregulation of type 1 interferon signaling is demonstrated in the presented case and 4 other patients”; Lepelley 2020 and Deng 2020 mechanistically linked this to STING mistrafficking (volpi2018typeiinterferon pages 9-12, lepelley2020mutationsincopa pages 1-2, deng2020adefectin pages 1-5) |


*Table: This table maps major COPA syndrome manifestations to suggested HPO terms and summarizes the best available onset and frequency data from key cohorts and reviews. It is useful for knowledge-base phenotype curation and for linking clinical features to quantitative evidence.*

**Visual cohort evidence (Tsui et al., ERJ Open Research 2018):** Tables in the paper summarize DAH prevalence, histopathology, treatments, and diagnostic clues. (tsui2018analysisofpulmonary media 5488c39b, tsui2018analysisofpulmonary media 3c75068d)

---

## 4. Genetic / molecular information

### 4.1 Causal gene
- **COPA** (coat protein complex I subunit alpha). (kumrah2019geneticsofcopa pages 1-2)

### 4.2 Pathogenic variants (examples explicitly supported by retrieved evidence)
**WD40-domain (classic) variants:**
- p.Lys230Asn (**K230N**), p.Arg233His (**R233H**), p.Glu241Lys (**E241K**), p.Asp243Gly (**D243G**); another residue-243 substitution p.Asp243Asn (**D243N**) appears in later families. (watkin2015copamutationsimpair pages 1-11, lepelley2020mutationsincopa pages 1-2)

**CTD variants (2024 expansion):**
- p.C1013S, p.R1058C, p.R1142X reported in 6 children from 3 unrelated families. (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3)

**Variant type/class:** missense variants are common for WD40-domain COPA syndrome; CTD includes missense and nonsense. (delafontaine2024heterozygousmutationsin pages 2-3, watkin2015copamutationsimpair pages 1-11)

**Population frequency:** CTD variants were reported as rare in gnomAD (qualitative statement in the excerpt). (delafontaine2024heterozygousmutationsin pages 2-3)

### 4.3 Functional consequence (current understanding)
- WD40 variants impair binding/sorting of proteins targeted for ER retrieval (dilysine-tagged cargos), and mechanistic work identifies STING trafficking defects as a central immune driver. (deng2020adefectin pages 1-5, delafontaine2024heterozygousmutationsin pages 2-3)
- Mutant COPA can increase ER stress markers and autophagosome accumulation (reported in early genetic work excerpts). (watkin2015copamutationsimpair pages 1-11)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
- **Modifier genes:** clinical nonpenetrance (~30%) implies modifiers, but specific modifier loci were not established in the retrieved primary excerpts. (lepelley2020mutationsincopa pages 4-5)
- **Epigenetics/chromosomal abnormalities:** no specific disease-associated chromosomal abnormalities or epigenetic alterations were supported by the retrieved text.

---

## 5. Environmental information
No specific toxins/lifestyle/infectious triggers were directly supported in the retrieved evidence excerpts. Many manifestations can mimic systemic autoimmune disease; however, environment-trigger claims would require additional epidemiologic/immunologic studies not captured in the current evidence set.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (integrated model)
**Upstream defect:** COPA mutation → impaired COPI-mediated trafficking (Golgi↔ER) → abnormal localization/handling of immune sensors and ER homeostasis.

**Key midstream nodes:**
1) **STING mis-trafficking/activation** at the ERGIC/Golgi, driving IFN-I programs. (deng2020adefectin pages 1-5, lepelley2020mutationsincopa pages 1-2)
2) **ER stress** (and impaired autophagy) amplifying inflammatory pathways and immune dysregulation. (watkin2015copamutationsimpair pages 1-11, delafontaine2024heterozygousmutationsin pages 2-3)
3) Downstream **type I interferon signaling**, with skewing toward pro-inflammatory immune phenotypes and autoantibody production. (volpi2018typeiinterferon pages 9-12, vece2016copasyndromea pages 2-4)

**Tissue outcomes:** chronic immune-mediated injury/fibrosis/hemorrhage in **lung**, inflammatory joint disease, and subset kidney immune-complex disease. (vece2016copasyndromea pages 2-4, tsui2018analysisofpulmonary pages 8-10)

### 6.2 STING/type I interferon biology in COPA syndrome (key primary findings)
- **STING retention/accumulation in Golgi:** Lepelley et al. report that “**mutant COPA is associated with an accumulation of STING in the Golgi compartment**” and propose COPA mediates retrograde trafficking of STING from Golgi to ER. (lepelley2020mutationsincopa pages 1-2)
- **Ligand-independent STING activation and genetic rescue:** Deng et al. show mutant COPA causes ligand-independent STING activation, with inflammatory phenotypes in **CopaE241K/+** mice that are **rescued by STING deficiency**. (deng2020adefectin pages 1-5)
- **Adapter role (SURF4):** Deng et al. identify **SURF4** as an adapter facilitating COPA-mediated retrieval of STING. (deng2020adefectin pages 1-5)

### 6.3 cGAS/STING, ER stress, and NF-κB (2024 expansion into CTD)
Delafontaine et al. (JCI 2024) report CTD variants and show:
- “**These CTD COPA mutations disrupt the integrity and the function of coat protein complex I (COPI)**.” (delafontaine2024heterozygousmutationsin pages 1-2)
- Trafficking defects (anterograde and retrograde) with “**a cGAS/STING-dependent upregulation of the type I IFN signaling**.” (delafontaine2024heterozygousmutationsin pages 1-2)
- CTD variants “**induce an activation of ER stress and NF-κB signaling**.” (delafontaine2024heterozygousmutationsin pages 1-2)

### 6.4 Immune cell involvement (suggested CL terms)
Evidence supports T-cell skewing toward Th17 and systemic immune activation.
- Suggested **Cell Ontology (CL)** terms:
  - **CL:0000624** CD4-positive, alpha-beta T cell
  - **CL:0000899** T helper 17 cell
  - **CL:0000542** lymphocyte
  - **CL:0000842** mononuclear cell (PBMC context)
(Th17 skewing and PBMC interferon signatures are described in clinical series and mechanistic studies.) (vece2016copasyndromea pages 2-4, lepelley2020mutationsincopa pages 4-5)

### 6.5 Suggested GO terms (biological process / cellular component)
- **GO:0006886** intracellular protein transport
- **GO:0015031** protein transport
- **GO:0006890** retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum
- **GO:0034976** response to endoplasmic reticulum stress
- **GO:0032481** positive regulation of type I interferon production
- **GO:0035458** cellular response to interferon-beta
- **GO:0038061** NIK/NF-kappaB signaling
(These are consistent with COPI transport defects, ER stress, IFN-I pathway activation, and NF-κB activation described in mechanistic studies.) (deng2020adefectin pages 1-5, delafontaine2024heterozygousmutationsin pages 1-2)

### 6.6 Suggested UBERON anatomy terms (major affected structures)
- **UBERON:0002048** lung
- **UBERON:0002384** joint
- **UBERON:0002113** kidney
Supported by the classic lung–joint–kidney phenotype. (vece2016copasyndromea pages 2-4, kumrah2019geneticsofcopa pages 2-3)

### 6.7 Molecular profiling / “IFN signature” as a biomarker concept
- IFN signature has been shown in COPA syndrome cases and additional patients, and is proposed as a therapeutic/monitoring target. (volpi2018typeiinterferon pages 9-12, NCT06878365 chunk 1)

---

## 7. Anatomical structures affected

### Organ/system level
- **Respiratory:** diffuse parenchymal lung disease/ILD, cysts, DAH; progressive disease is a major driver of morbidity. (tsui2018analysisofpulmonary pages 8-10, padureanu2024copasyndrome—frompathogenesis pages 4-5)
- **Musculoskeletal:** inflammatory arthritis/polyarthritis. (volpi2018typeiinterferon pages 9-12, tsui2018analysisofpulmonary pages 8-10)
- **Renal:** immune-complex glomerulonephritis/nephritis in a subset. (kumrah2019geneticsofcopa pages 2-3)

### Tissue/cell level (examples)
- Lung biopsy findings commonly include **follicular bronchiolitis** and inflammatory changes. (tsui2018analysisofpulmonary media 5488c39b)

### Subcellular localization
- ER–Golgi axis/ERGIC is central; STING accumulation at Golgi and trafficking defects are a mechanistic hallmark. (lepelley2020mutationsincopa pages 1-2, deng2020adefectin pages 1-5)

---

## 8. Temporal development

### Onset
- Predominantly **pediatric**; 76% with onset before age 5 in one clinical series; cohorts show early onset medians in the low single-digit years. (vece2016copasyndromea pages 2-4, lepelley2020mutationsincopa pages 1-2)

### Progression/course
- Course may be chronic/progressive, with episodes of DAH and gradual pulmonary decline; some individuals progress to respiratory failure and may require transplant. (tsui2018analysisofpulmonary pages 8-10, kato2021augmentationofstimulator pages 6-10)

---

## 9. Inheritance and population

### Inheritance
- **Autosomal dominant** with **variable expressivity** and reported nonpenetrance in some families. (vece2016copasyndromea pages 1-2, lepelley2020mutationsincopa pages 4-5)

### Epidemiology (data availability)
Robust prevalence/incidence estimates are not available in the retrieved evidence (typical for ultra-rare Mendelian disorders). Available “case-count” statistics from reviews/cohorts include:
- A review excerpt notes **~79 patients** reported with near-equal sex distribution (39M/40F). (padureanu2024copasyndrome—frompathogenesis pages 4-5)
- Earlier cohort summary: **21 patients from five families**, mean presentation ~3.5 years, and renal involvement in 4/21. (kumrah2019geneticsofcopa pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical suspicion pattern (high-yield recognition)
A practical diagnostic pattern is **childhood-onset** or familial **lung disease (ILD/cysts/DAH) + inflammatory arthritis + autoantibody positivity** (ANA/ANCA ± RF/anti-CCP), with or without renal involvement. (tsui2018analysisofpulmonary pages 8-10, vece2016copasyndromea pages 2-4)

### 10.2 Laboratory findings / biomarkers
- Autoantibodies: ANA (~80% in one series), ANCA, RF (71% in one cohort), anti-CCP. (vece2016copasyndromea pages 2-4, tsui2018analysisofpulmonary pages 8-10)
- Inflammatory markers: CRP/ESR elevations reported. (kato2021augmentationofstimulator pages 6-10)
- IFN-I pathway activation (“IFN signature”) is a mechanistic biomarker concept. (volpi2018typeiinterferon pages 9-12)

### 10.3 Imaging / pathology
- CT findings may include cysts and ground-glass opacities; biopsy often shows follicular bronchiolitis. (tsui2018analysisofpulmonary media 5488c39b)

### 10.4 Genetic testing approach
- Targeted sequencing focusing on the historically implicated region (exons 8–9; WD40 variants) was suggested in one pulmonary cohort when clinical criteria are met; broader panels or exome/genome sequencing may be needed given CTD variants described in 2024. (tsui2018analysisofpulmonary pages 8-10, delafontaine2024heterozygousmutationsin pages 1-2)

### Differential diagnosis (examples)
Because of autoantibodies and organ involvement, COPA syndrome can mimic systemic autoimmune conditions; mechanistic/clinical work emphasizes overlap with type I interferonopathies such as SAVI. (lepelley2020mutationsincopa pages 1-2, volpi2018typeiinterferon pages 9-12)

---

## 11. Outcome / prognosis

### Key prognosis concepts
- Lung disease is frequently the dominant driver of morbidity and may progress despite immunosuppression; some patients undergo lung transplantation. (tsui2018analysisofpulmonary pages 8-10, kato2021augmentationofstimulator pages 6-10)

**Quantitative survival estimates** were not available in the retrieved excerpts.

---

## 12. Treatment

### 12.1 Current real-world treatments (immunosuppression/biologics)
In a pulmonary cohort, patients received immunosuppression including glucocorticoids and steroid-sparing agents; induction regimens for DAH included methylprednisolone plus cyclophosphamide followed by maintenance (e.g., mycophenolate/azathioprine), with radiographic improvement but often ongoing physiologic decline. (tsui2018analysisofpulmonary pages 8-10)

**Real-world implementation evidence (tables/figures):** Tsui et al. include tables listing maintenance immunosuppression and diagnostic clues, plus longitudinal treatment/clinical course plots. (tsui2018analysisofpulmonary media 3c75068d)

### 12.2 Targeted / pathway-informed therapies

**JAK inhibitors (downstream IFN signaling):**
- Lepelley et al. report that “**Based on these results, three patients have been treated with interferon signaling (JAK1) inhibitors**” (paper abstract statement as quoted in excerpt). (lepelley2020mutationsincopa pages 1-2)
- In detailed text excerpt, one patient received ruxolitinib for >1 year with improvement in severe lung disease. (lepelley2020mutationsincopa pages 4-5)
- A 2024 review states: “**JAK inhibitor therapy seems to be the most promising therapeutic choice now**,” while acknowledging long-term lung control data remain limited. (padureanu2024copasyndrome—frompathogenesis pages 4-5)

**STING pathway inhibition (upstream):**
- In vitro work on COPI deficiency demonstrated inflammation in COPA syndrome PBMCs/cell lines can be ameliorated by a small-molecule STING inhibitor (H-151), supporting STING as a target concept; this underpins ongoing interest in STING-directed trials/compounds. (delafontaine2024heterozygousmutationsin pages 17-17)

**Transplantation:**
- Lung transplantation is used in severe progressive cases. (kato2021augmentationofstimulator pages 6-10, tsui2018analysisofpulmonary pages 8-10)

### 12.3 Clinical trials (current / emerging)
**NCT06878365 (BI 3000202; type I interferonopathies including COPA)**
- Title: “A Study to Test How Well BI 3000202 is Tolerated by People With Type 1 Interferonopathies”
- Sponsor: Boehringer Ingelheim
- Phase: 1; open-label; single-group
- Enrollment: 16
- Includes COPA syndrome explicitly (genetic diagnosis: **COPA**)
- Starts: 2025-07-29; status: active, not recruiting
- Outcomes include adverse events and **change in interferon gene score**
ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06878365 (NCT06878365 chunk 1)

**NCT06235580 (observational genotype–phenotype; includes COPA)**
- Observational case-control study at Imagine Institute enrolling genetic diseases with immune and neurological dysfunction; explicitly includes **COPA syndrome**
ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT06235580 (NCT06235580 chunk 1)

### 12.4 Suggested MAXO terms (examples)
- **NCIT:C15986** immunosuppressive therapy (for systemic immunosuppression)
- **MAXO:0000755** Janus kinase inhibitor therapy (for ruxolitinib/baricitinib class)
- **MAXO:0000600** lung transplantation
(These are ontology suggestions; exact MAXO IDs should be validated against the current MAXO release.) (tsui2018analysisofpulmonary pages 8-10, lepelley2020mutationsincopa pages 4-5, kato2021augmentationofstimulator pages 6-10)

---

## 13. Prevention
As a Mendelian autosomal dominant disorder, prevention is primarily via **genetic counseling**, **cascade testing** in families, and early recognition/monitoring for lung disease in carriers. While penetrance can be incomplete, nonpenetrance and variable expressivity complicate predictive counseling. (lepelley2020mutationsincopa pages 4-5, vece2016copasyndromea pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were supported in the retrieved evidence excerpts.

---

## 15. Model organisms / experimental systems
- **Mouse models:** mechanistic studies used **CopaE241K/+** and other targeted Copa alleles and showed **STING-dependent** inflammatory phenotypes rescued by STING deficiency, supporting causal biology. (deng2020adefectin pages 1-5)
- **Patient-derived fibroblasts/cell lines:** CTD variants (R1058C, R1142X) were studied in fibroblasts, demonstrating trafficking defects and cGAS/STING-dependent IFN signaling plus ER stress/NF-κB activation. (delafontaine2024heterozygousmutationsin pages 1-2)

---

## Recent developments (2023–2024 emphasis)
1. **Expanded genetic architecture (CTD COPA variants):** 2024 JCI report established CTD variants causing a COPA-related syndrome and clarified cGAS/STING dependence, ER stress, and NF-κB activation, broadening diagnostic sequencing beyond WD40 exons. Publication: Jan 2024; DOI: https://doi.org/10.1172/jci163604. (delafontaine2024heterozygousmutationsin pages 1-2, delafontaine2024heterozygousmutationsin pages 2-3)
2. **Clinical consolidation and treatment outlook:** 2024 Diagnostics review synthesized phenotype frequencies (e.g., arthritis ~95%, pulmonary involvement near-universal in curated cases) and highlighted JAK inhibitors as the most promising currently available class, while noting limited long-term lung outcome data. Publication: Dec 2024; DOI: https://doi.org/10.3390/diagnostics14242819. (padureanu2024copasyndrome—frompathogenesis pages 4-5, padureanu2024copasyndrome—frompathogenesis pages 1-2)
3. **New phenotypic expansions:** 2023–2024 case reports broadened phenotype (e.g., skin/NMOSD features, cryoglobulinemia) but these represent low-level evidence relative to cohorts. (padureanu2024copasyndrome—frompathogenesis pages 4-5)

---

## Evidence gaps / limitations (for knowledge-base curation)
- **PMIDs:** The retrieved full-text excerpts seldom include explicit PMID fields. One key PMID surfaced via Open Targets for COPA–disease association evidence: **PMID: 25894502** (likely corresponding to the 2015 discovery report). (padureanu2024copasyndrome—frompathogenesis pages 1-2)
- **Population epidemiology:** Prevalence/incidence estimates are not established in the retrieved evidence and generally remain unknown for ultra-rare disorders.
- **Standardized diagnostic criteria:** No formal consensus criteria were retrieved; most clinical guidance is pattern recognition plus genetic confirmation.

---

## Key source URLs (publication date in citation header)
- Watkin et al. *Nature Genetics* (Apr 2015). DOI: https://doi.org/10.1038/ng.3279 (watkin2015copamutationsimpair pages 1-11)
- Vece et al. *Journal of Clinical Immunology* (Apr 2016). DOI: https://doi.org/10.1007/s10875-016-0271-8 (vece2016copasyndromea pages 1-2)
- Tsui et al. *ERJ Open Research* (Apr 2018). DOI: https://doi.org/10.1183/23120541.00017-2018 (tsui2018analysisofpulmonary pages 8-10)
- Lepelley et al. *Journal of Experimental Medicine* (Jul 2020). DOI: https://doi.org/10.1084/jem.20200600 (lepelley2020mutationsincopa pages 1-2)
- Deng et al. *Journal of Experimental Medicine* (Jul 2020). DOI: https://doi.org/10.1084/jem.20201045 (deng2020adefectin pages 1-5)
- Kato et al. *Arthritis & Rheumatology* (Nov 2021). DOI: https://doi.org/10.1002/art.41790 (kato2021augmentationofstimulator pages 6-10)
- Delafontaine et al. *Journal of Clinical Investigation* (Jan 2024). DOI: https://doi.org/10.1172/jci163604 (delafontaine2024heterozygousmutationsin pages 1-2)
- Padureanu et al. *Diagnostics* (Dec 2024). DOI: https://doi.org/10.3390/diagnostics14242819 (padureanu2024copasyndrome—frompathogenesis pages 1-2)
- Clinical trial: NCT06878365 (Start 2025-07-29). https://clinicaltrials.gov/study/NCT06878365 (NCT06878365 chunk 1)
- Observational study: NCT06235580. https://clinicaltrials.gov/study/NCT06235580 (NCT06235580 chunk 1)


References

1. (vece2016copasyndromea pages 2-4): Timothy J. Vece, Levi B. Watkin, Sarah K. Nicholas, Debra Canter, Michael C. Braun, Robert Paul Guillerman, Karen W. Eldin, Grant Bertolet, Scott D. McKinley, Marietta de Guzman, Lisa R. Forbes, Ivan Chinn, and Jordan S. Orange. Copa syndrome: a novel autosomal dominant immune dysregulatory disease. Journal of Clinical Immunology, 36:377-387, Apr 2016. URL: https://doi.org/10.1007/s10875-016-0271-8, doi:10.1007/s10875-016-0271-8. This article has 208 citations and is from a domain leading peer-reviewed journal.

2. (tsui2018analysisofpulmonary pages 8-10): Jessica L. Tsui, Oscar A. Estrada, Zimu Deng, Kristin M. Wang, Christopher S. Law, Brett M. Elicker, Kirk D. Jones, Sharon D. Dell, Gunnar Gudmundsson, Sif Hansdottir, Simon M. Helfgott, Stefano Volpi, Marco Gattorno, Michael R. Waterfield, Alice Y. Chan, Sharon A. Chung, Brett Ley, and Anthony K. Shum. Analysis of pulmonary features and treatment approaches in the copa syndrome. ERJ Open Research, 4:00017-2018, Apr 2018. URL: https://doi.org/10.1183/23120541.00017-2018, doi:10.1183/23120541.00017-2018. This article has 108 citations and is from a peer-reviewed journal.

3. (deng2020adefectin pages 1-5): Zimu Deng, Zhenlu Chong, Christopher S. Law, Kojiro Mukai, Frances O. Ho, Tereza Martinu, Bradley J. Backes, Walter L. Eckalbar, Tomohiko Taguchi, and Anthony K. Shum. A defect in copi-mediated transport of sting causes immune dysregulation in copa syndrome. Journal of Experimental Medicine, Jul 2020. URL: https://doi.org/10.1084/jem.20201045, doi:10.1084/jem.20201045. This article has 214 citations and is from a highest quality peer-reviewed journal.

4. (delafontaine2024heterozygousmutationsin pages 1-2): Selket Delafontaine, Alberto Iannuzzo, Tarin M. Bigley, Bram Mylemans, Ruchit Rana, Pieter Baatsen, Maria Cecilia Poli, Daisy Rymen, Katrien Jansen, Djalila Mekahli, Ingele Casteels, Catherine Cassiman, Philippe Demaerel, Alice Lepelley, Marie-Louise Frémond, Rik Schrijvers, Xavier Bossuyt, Katlijn Vints, Wim Huybrechts, Rachida Tacine, Karen Willekens, Anniek Corveleyn, Bram Boeckx, Marco Baggio, Lisa Ehlers, Sebastian Munck, Diether Lambrechts, Arnout Voet, Leen Moens, Giorgia Bucciol, Megan A. Cooper, Carla M. Davis, Jérôme Delon, and Isabelle Meyts. Heterozygous mutations in the c-terminal domain of copa underlie a complex autoinﬂammatory syndrome. The Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci163604, doi:10.1172/jci163604. This article has 24 citations.

5. (vece2016copasyndromea pages 1-2): Timothy J. Vece, Levi B. Watkin, Sarah K. Nicholas, Debra Canter, Michael C. Braun, Robert Paul Guillerman, Karen W. Eldin, Grant Bertolet, Scott D. McKinley, Marietta de Guzman, Lisa R. Forbes, Ivan Chinn, and Jordan S. Orange. Copa syndrome: a novel autosomal dominant immune dysregulatory disease. Journal of Clinical Immunology, 36:377-387, Apr 2016. URL: https://doi.org/10.1007/s10875-016-0271-8, doi:10.1007/s10875-016-0271-8. This article has 208 citations and is from a domain leading peer-reviewed journal.

6. (padureanu2024copasyndrome—frompathogenesis pages 2-4): Vlad Padureanu, Mircea-Cătălin Forțofoiu, Ionut Donoiu, Eugen-Nicolae Tieranu, Catalin Dumitrascu, Rodica Padureanu, Anca Emanuela Mușetescu, Cristina Alexandru, Carmen Catalina Iorgus, Florin Bobirca, Ana Dascalu, and Anca Bobirca. Copa syndrome—from pathogenesis to treatment. Diagnostics, 14:2819, Dec 2024. URL: https://doi.org/10.3390/diagnostics14242819, doi:10.3390/diagnostics14242819. This article has 4 citations.

7. (padureanu2024copasyndrome—frompathogenesis pages 1-2): Vlad Padureanu, Mircea-Cătălin Forțofoiu, Ionut Donoiu, Eugen-Nicolae Tieranu, Catalin Dumitrascu, Rodica Padureanu, Anca Emanuela Mușetescu, Cristina Alexandru, Carmen Catalina Iorgus, Florin Bobirca, Ana Dascalu, and Anca Bobirca. Copa syndrome—from pathogenesis to treatment. Diagnostics, 14:2819, Dec 2024. URL: https://doi.org/10.3390/diagnostics14242819, doi:10.3390/diagnostics14242819. This article has 4 citations.

8. (kato2021augmentationofstimulator pages 6-10): Takashi Kato, Masaki Yamamoto, Yoshitaka Honda, Takashi Orimo, Izumi Sasaki, Kohei Murakami, Hiroaki Hemmi, Yuri Fukuda‐Ohta, Kyoichi Isono, Saki Takayama, Hidenori Nakamura, Yoshiro Otsuki, Toshiaki Miyamoto, Junko Takita, Takahiro Yasumi, Ryuta Nishikomori, Tadashi Matsubayashi, Kazushi Izawa, and Tsuneyasu Kaisho. Augmentation of stimulator of interferon genes–induced type i interferon production in copa syndrome. Arthritis &amp; Rheumatology, 73:2105-2115, Nov 2021. URL: https://doi.org/10.1002/art.41790, doi:10.1002/art.41790. This article has 41 citations and is from a highest quality peer-reviewed journal.

9. (kumrah2019geneticsofcopa pages 1-2): Rajni Kumrah, Babu Mathew, Vignesh Pandiarajan, Surjit Singh, and Amit Rawat. Genetics of copa syndrome. The Application of Clinical Genetics, 12:11-18, Feb 2019. URL: https://doi.org/10.2147/tacg.s153600, doi:10.2147/tacg.s153600. This article has 27 citations.

10. (lepelley2020mutationsincopa pages 1-2): Alice Lepelley, Maria José Martin-Niclós, Melvin Le Bihan, Joseph A. Marsh, Carolina Uggenti, Gillian I. Rice, Vincent Bondet, Darragh Duffy, Jonny Hertzog, Jan Rehwinkel, Serge Amselem, Siham Boulisfane-El Khalifi, Mary Brennan, Edwin Carter, Lucienne Chatenoud, Stéphanie Chhun, Aurore Coulomb l’Hermine, Marine Depp, Marie Legendre, Karen J. Mackenzie, Jonathan Marey, Catherine McDougall, Kathryn J. McKenzie, Thierry Jo Molina, Bénédicte Neven, Luis Seabra, Caroline Thumerelle, Marie Wislez, Nadia Nathan, Nicolas Manel, Yanick J. Crow, and Marie-Louise Frémond. Mutations in copa lead to abnormal trafficking of sting to the golgi and interferon signaling. The Journal of Experimental Medicine, Jul 2020. URL: https://doi.org/10.1084/jem.20200600, doi:10.1084/jem.20200600. This article has 232 citations.

11. (padureanu2024copasyndrome—frompathogenesis pages 4-5): Vlad Padureanu, Mircea-Cătălin Forțofoiu, Ionut Donoiu, Eugen-Nicolae Tieranu, Catalin Dumitrascu, Rodica Padureanu, Anca Emanuela Mușetescu, Cristina Alexandru, Carmen Catalina Iorgus, Florin Bobirca, Ana Dascalu, and Anca Bobirca. Copa syndrome—from pathogenesis to treatment. Diagnostics, 14:2819, Dec 2024. URL: https://doi.org/10.3390/diagnostics14242819, doi:10.3390/diagnostics14242819. This article has 4 citations.

12. (watkin2015copamutationsimpair pages 1-11): Levi B Watkin, Birthe Jessen, Wojciech Wiszniewski, Timothy J Vece, Max Jan, Youbao Sha, Maike Thamsen, Regie L P Santos-Cortez, Kwanghyuk Lee, Tomasz Gambin, Lisa R Forbes, Christopher S Law, Asbjørg Stray-Pedersen, Mickie H Cheng, Emily M Mace, Mark S Anderson, Dongfang Liu, Ling Fung Tang, Sarah K Nicholas, Karen Nahmod, George Makedonas, Debra L Canter, Pui-Yan Kwok, John Hicks, Kirk D Jones, Samantha Penney, Shalini N Jhangiani, Michael D Rosenblum, Sharon D Dell, Michael R Waterfield, Feroz R Papa, Donna M Muzny, Noah Zaitlen, Suzanne M Leal, Claudia Gonzaga-Jauregui, Eric Boerwinkle, N Tony Eissa, Richard A Gibbs, James R Lupski, Jordan S Orange, and Anthony K Shum. Copa mutations impair er-golgi transport and cause hereditary autoimmune-mediated lung disease and arthritis. Nature Genetics, 47:654-660, Apr 2015. URL: https://doi.org/10.1038/ng.3279, doi:10.1038/ng.3279. This article has 435 citations and is from a highest quality peer-reviewed journal.

13. (delafontaine2024heterozygousmutationsin pages 2-3): Selket Delafontaine, Alberto Iannuzzo, Tarin M. Bigley, Bram Mylemans, Ruchit Rana, Pieter Baatsen, Maria Cecilia Poli, Daisy Rymen, Katrien Jansen, Djalila Mekahli, Ingele Casteels, Catherine Cassiman, Philippe Demaerel, Alice Lepelley, Marie-Louise Frémond, Rik Schrijvers, Xavier Bossuyt, Katlijn Vints, Wim Huybrechts, Rachida Tacine, Karen Willekens, Anniek Corveleyn, Bram Boeckx, Marco Baggio, Lisa Ehlers, Sebastian Munck, Diether Lambrechts, Arnout Voet, Leen Moens, Giorgia Bucciol, Megan A. Cooper, Carla M. Davis, Jérôme Delon, and Isabelle Meyts. Heterozygous mutations in the c-terminal domain of copa underlie a complex autoinﬂammatory syndrome. The Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci163604, doi:10.1172/jci163604. This article has 24 citations.

14. (kumrah2019geneticsofcopa pages 2-3): Rajni Kumrah, Babu Mathew, Vignesh Pandiarajan, Surjit Singh, and Amit Rawat. Genetics of copa syndrome. The Application of Clinical Genetics, 12:11-18, Feb 2019. URL: https://doi.org/10.2147/tacg.s153600, doi:10.2147/tacg.s153600. This article has 27 citations.

15. (lepelley2020mutationsincopa pages 4-5): Alice Lepelley, Maria José Martin-Niclós, Melvin Le Bihan, Joseph A. Marsh, Carolina Uggenti, Gillian I. Rice, Vincent Bondet, Darragh Duffy, Jonny Hertzog, Jan Rehwinkel, Serge Amselem, Siham Boulisfane-El Khalifi, Mary Brennan, Edwin Carter, Lucienne Chatenoud, Stéphanie Chhun, Aurore Coulomb l’Hermine, Marine Depp, Marie Legendre, Karen J. Mackenzie, Jonathan Marey, Catherine McDougall, Kathryn J. McKenzie, Thierry Jo Molina, Bénédicte Neven, Luis Seabra, Caroline Thumerelle, Marie Wislez, Nadia Nathan, Nicolas Manel, Yanick J. Crow, and Marie-Louise Frémond. Mutations in copa lead to abnormal trafficking of sting to the golgi and interferon signaling. The Journal of Experimental Medicine, Jul 2020. URL: https://doi.org/10.1084/jem.20200600, doi:10.1084/jem.20200600. This article has 232 citations.

16. (tsui2018analysisofpulmonary media 5488c39b): Jessica L. Tsui, Oscar A. Estrada, Zimu Deng, Kristin M. Wang, Christopher S. Law, Brett M. Elicker, Kirk D. Jones, Sharon D. Dell, Gunnar Gudmundsson, Sif Hansdottir, Simon M. Helfgott, Stefano Volpi, Marco Gattorno, Michael R. Waterfield, Alice Y. Chan, Sharon A. Chung, Brett Ley, and Anthony K. Shum. Analysis of pulmonary features and treatment approaches in the copa syndrome. ERJ Open Research, 4:00017-2018, Apr 2018. URL: https://doi.org/10.1183/23120541.00017-2018, doi:10.1183/23120541.00017-2018. This article has 108 citations and is from a peer-reviewed journal.

17. (volpi2018typeiinterferon pages 9-12): Stefano Volpi, Jessica Tsui, Marcello Mariani, Claudia Pastorino, Roberta Caorsi, Oliviero Sacco, Angelo Ravelli, Anthony K. Shum, Marco Gattorno, and Paolo Picco. Type i interferon pathway activation in copa syndrome. Clinical Immunology, 187:33-36, Feb 2018. URL: https://doi.org/10.1016/j.clim.2017.10.001, doi:10.1016/j.clim.2017.10.001. This article has 134 citations and is from a peer-reviewed journal.

18. (tsui2018analysisofpulmonary pages 8-8): Jessica L. Tsui, Oscar A. Estrada, Zimu Deng, Kristin M. Wang, Christopher S. Law, Brett M. Elicker, Kirk D. Jones, Sharon D. Dell, Gunnar Gudmundsson, Sif Hansdottir, Simon M. Helfgott, Stefano Volpi, Marco Gattorno, Michael R. Waterfield, Alice Y. Chan, Sharon A. Chung, Brett Ley, and Anthony K. Shum. Analysis of pulmonary features and treatment approaches in the copa syndrome. ERJ Open Research, 4:00017-2018, Apr 2018. URL: https://doi.org/10.1183/23120541.00017-2018, doi:10.1183/23120541.00017-2018. This article has 108 citations and is from a peer-reviewed journal.

19. (tsui2018analysisofpulmonary media 3c75068d): Jessica L. Tsui, Oscar A. Estrada, Zimu Deng, Kristin M. Wang, Christopher S. Law, Brett M. Elicker, Kirk D. Jones, Sharon D. Dell, Gunnar Gudmundsson, Sif Hansdottir, Simon M. Helfgott, Stefano Volpi, Marco Gattorno, Michael R. Waterfield, Alice Y. Chan, Sharon A. Chung, Brett Ley, and Anthony K. Shum. Analysis of pulmonary features and treatment approaches in the copa syndrome. ERJ Open Research, 4:00017-2018, Apr 2018. URL: https://doi.org/10.1183/23120541.00017-2018, doi:10.1183/23120541.00017-2018. This article has 108 citations and is from a peer-reviewed journal.

20. (NCT06878365 chunk 1):  A Study to Test How Well BI 3000202 is Tolerated by People With Type 1 Interferonopathies. Boehringer Ingelheim. 2025. ClinicalTrials.gov Identifier: NCT06878365

21. (delafontaine2024heterozygousmutationsin pages 17-17): Selket Delafontaine, Alberto Iannuzzo, Tarin M. Bigley, Bram Mylemans, Ruchit Rana, Pieter Baatsen, Maria Cecilia Poli, Daisy Rymen, Katrien Jansen, Djalila Mekahli, Ingele Casteels, Catherine Cassiman, Philippe Demaerel, Alice Lepelley, Marie-Louise Frémond, Rik Schrijvers, Xavier Bossuyt, Katlijn Vints, Wim Huybrechts, Rachida Tacine, Karen Willekens, Anniek Corveleyn, Bram Boeckx, Marco Baggio, Lisa Ehlers, Sebastian Munck, Diether Lambrechts, Arnout Voet, Leen Moens, Giorgia Bucciol, Megan A. Cooper, Carla M. Davis, Jérôme Delon, and Isabelle Meyts. Heterozygous mutations in the c-terminal domain of copa underlie a complex autoinﬂammatory syndrome. The Journal of Clinical Investigation, Jan 2024. URL: https://doi.org/10.1172/jci163604, doi:10.1172/jci163604. This article has 24 citations.

22. (NCT06235580 chunk 1):  Genotype-phenotype Characterization Study on Genetic Diseases With Immune and Neurological Dysfunctions. Imagine Institute. 2015. ClinicalTrials.gov Identifier: NCT06235580
