---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:57.614200'
end_time: '2026-04-04T12:36:35.345416'
duration_seconds: 697.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PRPS1 Deficiency Spectrum
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
- **Disease Name:** PRPS1 Deficiency Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **PRPS1 Deficiency Spectrum** covering all of the
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
- **Disease Name:** PRPS1 Deficiency Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **PRPS1 Deficiency Spectrum** covering all of the
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


# PRPS1 Deficiency Spectrum (PRS-I deficiency) — Comprehensive Disease Characteristics Report (Genetic)

## Executive summary
PRPS1 deficiency (also called PRS-I/PRS deficiency) is an X-linked inborn error of nucleotide metabolism caused by loss-of-function variants in **PRPS1**, encoding phosphoribosyl pyrophosphate synthetase 1 (PRS-I), a key enzyme producing phosphoribosyl pyrophosphate (PRPP). Contemporary literature conceptualizes PRPS1 deficiency as a **phenotypic continuum** spanning X-linked nonsyndromic hearing loss (**DFNX1**) to Charcot–Marie–Tooth neuropathy with optic involvement (**CMTX5**) and severe multisystem disease (**Arts syndrome**), with severity broadly correlating with residual enzymatic activity and, in females, X-chromosome inactivation patterns. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, nassogne2024neurologicalpresentationsof pages 2-3, camici2023inbornerrorsof pages 4-7)

A key recent (2023–2024) development is consolidation of diagnostic biochemical signatures for purine/pyrimidine disorders (including PRPS1 deficiency), and new mechanistic work on **post-translational regulation of PRPS1** (O-GlcNAcylation/AMPK phosphorylation) that also links an Arts-syndrome-associated PRPS1 mutant to reduced PRPS1 activity. (nassogne2024neurologicalpresentationsof pages 2-3, chen2024directstimulationof pages 1-2, chen2024directstimulationof pages 21-25)

Therapeutically, there is no established disease-modifying therapy, but small numbers of Arts syndrome patients have been treated with **S-adenosylmethionine (SAMe)** ± **nicotinamide riboside (NR)** with reported clinical stability/improvement and improved immune cell function in a mechanistic case study. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, lenherr2021cotherapywithsadenosylmethionine pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 4-6)

## Key recent sources and statistics (2023–2024)
| Category | Entity/Source | Identifier(s) | Publication/Key dates | Hallmark features or main contribution | URL/DOI | Citation |
|---|---|---|---|---|---|---|
| Spectrum entity | DFNX1 (X-linked nonsyndromic hearing loss 1) | OMIM #304500 | — | Mild end of PRPS1 deficiency spectrum; primarily progressive sensorineural hearing loss, often congenital-to-childhood onset; hearing loss may range from moderate to profound. | https://omim.org/entry/304500 | (nassogne2024neurologicalpresentationsof pages 2-3, feng2024genomicandphenotypic pages 4-5) |
| Spectrum entity | CMTX5 (Charcot-Marie-Tooth disease X-linked type 5) | OMIM #311070 | — | Intermediate phenotype with sensorineural hearing loss plus peripheral neuropathy, ataxia/hypotonia, and optic neuropathy/optic atrophy. | https://omim.org/entry/311070 | (nassogne2024neurologicalpresentationsof pages 2-3, nassogne2024neurologicalpresentationsof pages 3-4) |
| Spectrum entity | Arts syndrome | OMIM #301835; ORPHA:1187 | — | Most severe PRPS1 deficiency phenotype; congenital sensorineural hearing loss, developmental delay/intellectual disability, hypotonia, ataxia, optic atrophy/retinal disease, recurrent respiratory infections, and early mortality in severe untreated cases. | https://omim.org/entry/301835 ; https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=EN&Expert=1187 | (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, lenherr2021cotherapywithsadenosylmethionine pages 1-2, brouwer2007artssyndromeis pages 3-4) |
| Recent source | Lee et al., *JIMD Reports* | DOI: 10.1002/jmd2.12395 | Sep 2023 | Case report + literature review of SAMe and nicotinamide riboside (NR) therapy in Arts syndrome; notes fewer than 25 reported cases in literature; across treated patients, symptoms were stable or improved, including reduced infection burden and gains in strength/endurance. | https://doi.org/10.1002/jmd2.12395 | (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, lee2023s‐adenosylmethionineandnicotinamide pages 2-4, lee2023s‐adenosylmethionineandnicotinamide pages 4-6) |
| Recent source | Camici et al., *Metabolites* | DOI: 10.3390/metabo13070787 | Jun 2023 | Review framing PRPS1 deficiency as an X-linked phenotypic continuum (DFNX1-CMTX5-Arts syndrome); severity correlates with residual enzyme activity; summarizes hearing loss, neuropathy, optic involvement, and recurrent infections. | https://doi.org/10.3390/metabo13070787 | (camici2023inbornerrorsof pages 4-7) |
| Recent source | Nassogne et al., *Eur J Paediatr Neurol* | DOI: 10.1016/j.ejpn.2023.11.013 | Jan 2024 | Review highlighting diagnostic biochemical markers: decreased PRS activity, decreased plasma uric acid, low urinary hypoxanthine/other purine metabolites, increased urinary orotic acid, and reduced RBC ATP/GTP/NAD/NADP; explicitly lists Arts syndrome OMIM #301835, CMTX5 #311070, DFNX1 #304500. | https://doi.org/10.1016/j.ejpn.2023.11.013 | (nassogne2024neurologicalpresentationsof pages 2-3) |
| Recent source | Feng et al., *Orphanet J Rare Dis* | DOI: 10.1186/s13023-024-03338-z | Sep 2024 | Hearing-loss cohort of 3,646 unrelated patients: overall diagnostic rate 52.72% (1,922/3,646); X-linked genes accounted for ~1.14% (22/1,922) of solved cases; PRPS1 variants were mainly missense; paper notes 30 reported PRPS1 coding mutations overall, including 11 DFNX1, 10 CMTX5, and 5 Arts syndrome. | https://doi.org/10.1186/s13023-024-03338-z | (feng2024genomicandphenotypic pages 4-5, feng2024genomicandphenotypic pages 2-4, feng2024genomicandphenotypic pages 1-2) |
| Recent source | Chen et al., *Nature Chemical Biology* | DOI: 10.1038/s41589-023-01354-x | Jun 2024 | Mechanistic study: OGT-mediated O-GlcNAcylation of PRPS1 promotes active hexamer formation, relieves ADP/GDP feedback inhibition, increases PRPP/nucleotide/NAD synthesis, and antagonizes AMPK-mediated inhibitory phosphorylation; Arts-associated R196W showed decreased O-GlcNAcylation and reduced activity. | https://doi.org/10.1038/s41589-023-01354-x | (chen2024directstimulationof pages 1-2, chen2024directstimulationof pages 21-25, chen2024directstimulationof pages 2-3) |
| Natural history study | NCT06092346, NHGRI observational cohort | ClinicalTrials.gov: NCT06092346 | First posted 2023-10-23; study start 2023-12-19; recruiting; primary completion estimated 2099-01-01 | Prospective natural history study of purine/pyrimidine metabolism disorders; explicitly includes PRPS1-related entries (PRPS1 deficiency/Arts syndrome/CMT); annual clinical evaluation and biospecimen collection to define genomic, clinical, laboratory, pharmacological, and dietary determinants of outcomes. | https://clinicaltrials.gov/ct2/show/NCT06092346 | (NCT06092346 chunk 1, NCT06092346 chunk 2) |


*Table: This table condenses the main clinical entities within the PRPS1 deficiency spectrum and the most relevant recent 2023-2024 sources, including diagnostics, mechanisms, treatment evidence, and the active NIH natural history study.*

---

## 1. Disease information

### What is the disease?
**PRPS1 deficiency spectrum** is a set of allelic X-linked disorders due to reduced PRS-I activity, leading to impaired PRPP generation and downstream deficits in purine nucleotide and NAD/NADP-related metabolism; clinically it manifests as a continuum from isolated/progressive sensorineural hearing loss to neuropathy/optic involvement and severe neurodevelopmental + immunologic disease. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, nassogne2024neurologicalpresentationsof pages 2-3, camici2023inbornerrorsof pages 4-7)

### Key identifiers (evidence-backed from retrieved sources)
- **Gene:** PRPS1 (OMIM *311850) (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, NCT06092346 chunk 1)
- **Arts syndrome:** OMIM **#301835**; Orphanet **ORPHA:1187** (nassogne2024neurologicalpresentationsof pages 2-3, lenherr2021cotherapywithsadenosylmethionine pages 1-2)
- **CMTX5:** OMIM **#311070** (nassogne2024neurologicalpresentationsof pages 2-3)
- **DFNX1:** OMIM **#304500** (nassogne2024neurologicalpresentationsof pages 2-3)

**Not found in the retrieved full texts:** MONDO ID, MeSH descriptor, ICD-10/ICD-11 code(s). This report therefore does not assert them.

### Synonyms and alternative names
- PRPS1 deficiency; PRS-I deficiency; PRS deficiency; phosphoribosyl pyrophosphate synthetase 1 deficiency; phosphoribosylpyrophosphate synthetase deficiency spectrum (nassogne2024neurologicalpresentationsof pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 1-2)
- Arts syndrome (severe PRPS1 deficiency), CMTX5, DFNX1 (nassogne2024neurologicalpresentationsof pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 1-2)

### Evidence provenance
The majority of information is derived from **aggregated literature/reviews** and **case reports/series**, plus one large **hearing loss cohort** study for contribution statistics. (feng2024genomicandphenotypic pages 4-5, lee2023s‐adenosylmethionineandnicotinamide pages 1-2, nassogne2024neurologicalpresentationsof pages 2-3)

---

## 2. Etiology

### Disease causal factors
- **Primary cause:** germline **loss-of-function PRPS1 variants** that reduce PRS-I activity and PRPP production (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, nassogne2024neurologicalpresentationsof pages 2-3, camici2023inbornerrorsof pages 4-7)
- **Inheritance:** X-linked; females can be affected with variable severity influenced by X-inactivation and/or mosaicism (nassogne2024neurologicalpresentationsof pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 6-7)

### Risk factors
- **Genetic:** hemizygous PRPS1 pathogenic variants in males; heterozygous females may exhibit milder features depending on X-inactivation (nassogne2024neurologicalpresentationsof pages 2-3)

### Protective factors
No evidence-based protective variants or environmental protective factors were identified in the retrieved texts.

### Gene–environment interactions
Direct gene–environment interaction evidence specific to PRPS1 deficiency was not identified in the retrieved corpus. However, several reports emphasize **infection-triggered clinical declines** in severe PRPS1 deficiency (Arts syndrome), consistent with physiologic stress exacerbating downstream consequences of nucleotide/NAD deficiency. (lee2023s‐adenosylmethionineandnicotinamide pages 2-4)

---

## 3. Phenotypes (clinical spectrum)

### Spectrum concept (current understanding)
Recent reviews explicitly describe PRPS1 deficiency phenotypes as a **“continuum disease spectrum”**, with severity broadly correlating with residual PRS activity and (in females) X-inactivation. (nassogne2024neurologicalpresentationsof pages 2-3)

### Core phenotypes by syndrome (hallmarks)
**Arts syndrome (severe PRPS1 deficiency)**
- Congenital sensorineural hearing loss; optic atrophy/retinal dystrophy; developmental delay/intellectual disability; hypotonia; ataxia; peripheral neuropathy; **recurrent respiratory infections/immune dysfunction**; potentially early death in severe untreated cases. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, lee2023s‐adenosylmethionineandnicotinamide pages 4-6, brouwer2007artssyndromeis pages 3-4)
- Foundational natural-history detail: in the original AJHG cohort, severe outcomes included early deaths and neuropathologic evidence of profound CNS involvement (e.g., myelin loss). (brouwer2007artssyndromeis pages 3-4)

**CMTX5 (intermediate)**
- Sensorineural hearing loss plus peripheral neuropathy (CMT) and optic neuropathy; ataxia/hypotonia can occur. (nassogne2024neurologicalpresentationsof pages 3-4, nassogne2024neurologicalpresentationsof pages 2-3)

**DFNX1 (milder end)**
- Predominant phenotype: sensorineural hearing loss (often progressive; onset variable). (feng2024genomicandphenotypic pages 4-5, nassogne2024neurologicalpresentationsof pages 2-3)

### Example genotype–biochemical–phenotype correlation
In a study of PRPS1-associated X-linked hearing loss with mild peripheral neuropathy, affected males carrying different PRPS1 missense variants had **markedly reduced erythrocyte PRS-I activity** relative to controls, and severity of enzyme impairment differed by variant, supporting a functional basis for variable expressivity. (robusto2015theexpandingspectrum pages 4-6)

### Suggested HPO terms (non-exhaustive; for knowledge base use)
- Sensorineural hearing impairment **HP:0000407**
- Optic atrophy **HP:0000648**; Retinal dystrophy **HP:0000556**
- Peripheral neuropathy **HP:0009830**; Abnormal nerve conduction velocity **HP:0003430**
- Ataxia **HP:0001251**; Hypotonia **HP:0001252**
- Global developmental delay **HP:0001263**; Intellectual disability **HP:0001249**
- Recurrent respiratory infections **HP:0002205**

**Phenotype frequencies:** robust, cross-study percentage frequencies were not extractable from the retrieved sources; most evidence is case-based. A single recent cohort provides X-linked contributions to a hearing-loss cohort, but not syndrome-specific penetrance/frequency across PRPS1 deficiency spectrum. (feng2024genomicandphenotypic pages 4-5)

---

## 4. Genetic / molecular information

### Causal gene
- **PRPS1** (PRS-I), Xq22.3 (lenherr2021cotherapywithsadenosylmethionine pages 1-2)

### Variant types and genotype–phenotype notes
- Recent cohort/review synthesis notes that PRPS1 disease-associated variants are predominantly **missense**, consistent with the requirement for some residual activity compatible with development. (camici2023inbornerrorsof pages 4-7, feng2024genomicandphenotypic pages 4-5)
- A 2024 review lists the spectrum entities and explicitly ties severity to residual PRS activity, reinforcing a genotype→activity→phenotype model. (nassogne2024neurologicalpresentationsof pages 2-3)

### Reported mutation counts (literature synthesis; 2024)
A 2024 hearing-loss cohort study states that **30 coding-region PRPS1 mutations** had been reported (as summarized there), with distribution across phenotypes including DFNX1 and CMTX5 and fewer for Arts syndrome, and notes that variants are mainly missense. (feng2024genomicandphenotypic pages 4-5)

### Functional consequences
- Loss-of-function PRPS1 variants reduce PRS activity and impair PRPP-dependent metabolic flux; severe cases show multiple downstream nucleotide/cofactor deficiencies. (nassogne2024neurologicalpresentationsof pages 2-3, camici2023inbornerrorsof pages 4-7)

**Modifier genes / epigenetics:** No direct evidence for modifier genes or epigenetic signatures specific to PRPS1 deficiency were identified in the retrieved corpus.

---

## 5. Environmental information
No disease-specific environmental or lifestyle contributing factors were identified from the retrieved sources. Clinical deterioration in severe disease can occur with infections (clinical stressors). (lee2023s‐adenosylmethionineandnicotinamide pages 2-4)

---

## 6. Mechanism / pathophysiology

### Biochemical role of PRPS1 (upstream)
PRPS1 deficiency is secondary to loss-of-function PRPS1 variants; PRS-I generates PRPP, which is utilized in **purine synthesis** and in **NAD/NADP-related pathways**, among others. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2)

Direct abstract-quote evidence (2023):
- “**Phospho‐ribosyl‐pyrophosphate synthetase 1 (PRPS1) deficiency is secondary to loss of function variants in PRPS1. This enzyme generates phospho‐ribosyl‐pyrophosphate (PRPP), which is utilized in the synthesis of purines, nicotinamide adenine dinucleotide (NAD), and NAD phosphate (NADP)** …” (lee2023s‐adenosylmethionineandnicotinamide pages 1-2)

### Downstream biochemical abnormalities (diagnostically relevant)
A 2024 review of purine/pyrimidine disorders provides a concise biochemical signature for PRPS1 deficiency, including:
- decreased PRS activity (RBC/fibroblasts/lymphocytes)
- decreased plasma uric acid
- decreased urinary hypoxanthine and other purine-related metabolites
- increased urinary orotic acid
- decreased RBC ATP, GTP, NAD, and NADP (nassogne2024neurologicalpresentationsof pages 2-3)

### Cellular processes and tissue vulnerability
- Severe disease includes immune dysfunction with recurrent infections; mechanistic case work links nucleotide/NAD replenishment strategies to improved T-cell survival/function. (lenherr2021cotherapywithsadenosylmethionine pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 4-6)

### Recent mechanistic development (2024): PRPS1 regulation by O-GlcNAcylation/AMPK
A 2024 Nature Chemical Biology study demonstrated a regulatory mechanism in which OGT-mediated O-GlcNAcylation promotes PRPS1 hexamer formation and relieves feedback inhibition, and also connects an Arts-syndrome-associated PRPS1 mutant to reduced activity.

Direct abstract-quote evidence (2024):
- “**Phosphoribosyl pyrophosphate synthetase (PRPS1)… was found to be O-GlcNAcylated, which increases PRPS1 activity** …” and “**Arts-syndrome-associated PRPS1 R196W mutant exhibits decreased PRPS1 O-GlcNAcylation and activity** …” (chen2024directstimulationof pages 1-2)

Mechanistic chain (condensed): PRPS1 LOF → ↓PRPP → ↓purine nucleotides and ↓NAD/NADP pools → impaired energy/redox balance and biosynthetic capacity → vulnerability in high-demand tissues (auditory system, nervous system, optic/retinal tissues) and immune dysfunction in severe cases. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, nassogne2024neurologicalpresentationsof pages 2-3, lenherr2021cotherapywithsadenosylmethionine pages 2-3)

### Suggested GO terms (examples)
- GO:0006164 purine nucleotide biosynthetic process
- GO:0006739 NADP metabolic process
- GO:0006766 vitamin metabolic process (for nicotinamide-related pathways)
- GO:0046034 ATP metabolic process

### Suggested CL (cell types) and UBERON (anatomy)
- CL:0000545 T cell; CL:0000625 CD8-positive, alpha-beta T cell; CL:0000624 CD4-positive, alpha-beta T cell (supported by immune-cell functional assays in Arts syndrome) (lenherr2021cotherapywithsadenosylmethionine pages 2-3)
- UBERON:0002107 cochlea; UBERON:0000955 brain; UBERON:0000047 retina; UBERON:0000966 optic nerve; UBERON:0001021 peripheral nerve

---

## 7. Anatomical structures affected
Primary systems implicated across the spectrum include:
- **Auditory system** (sensorineural hearing loss) (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, feng2024genomicandphenotypic pages 4-5)
- **Nervous system** (peripheral neuropathy, ataxia, hypotonia, neurodevelopmental impairment) (nassogne2024neurologicalpresentationsof pages 2-3, brouwer2007artssyndromeis pages 3-4)
- **Visual system** (optic atrophy/retinal dystrophy) (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, nassogne2024neurologicalpresentationsof pages 2-3)
- **Immune/respiratory involvement** in severe disease (recurrent respiratory infections; T-cell dysfunction) (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, lenherr2021cotherapywithsadenosylmethionine pages 2-3)

---

## 8. Temporal development
- **Onset:** often congenital/early childhood for hearing loss; severe Arts syndrome presents in early childhood and can be progressive. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, feng2024genomicandphenotypic pages 4-5)
- **Course:** severe cases may worsen with recurrent infections; treated reports describe more stable trajectories in limited numbers of patients. (lee2023s‐adenosylmethionineandnicotinamide pages 4-6)

---

## 9. Inheritance and population

### Inheritance pattern
- X-linked inheritance is consistently reported; female phenotype variability is linked to X-inactivation and mosaicism. (nassogne2024neurologicalpresentationsof pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 6-7)

### Population statistics (recent)
A large Chinese hearing-loss cohort study (n=3,646) reported:
- overall genetic diagnostic rate **52.72%** (1,922/3,646)
- X-linked gene diagnoses contributed **~1.14%** (22/1,922) of solved cases (feng2024genomicandphenotypic pages 1-2)

This study also describes PRPS1’s contribution as low in that cohort and summarizes the known mutational spectrum (mostly missense; literature-reported coding mutations). (feng2024genomicandphenotypic pages 4-5, feng2024genomicandphenotypic pages 9-10)

**Prevalence/incidence:** no population prevalence/incidence for PRPS1 deficiency spectrum (or Arts syndrome specifically) was extractable from retrieved sources.

---

## 10. Diagnostics

### Clinical testing and biomarkers
A recent review provides a coherent set of biochemical findings supporting diagnosis, including decreased PRS activity and low uric acid with characteristic urinary metabolite changes and reduced RBC nucleotides/cofactors. (nassogne2024neurologicalpresentationsof pages 2-3)

However, biochemical markers can be inconsistent: a 2020 case report explicitly notes that **normal serum/urine purine/pyrimidine metabolite levels do not exclude PRPS1-related disorders**, emphasizing the importance of enzyme testing and/or genetics. (puusepp2020atypicalpresentationof pages 1-2)

### Genetic testing (real-world)
- PRPS1 is “**found on many commercially available genetic panels**” relevant to hearing loss, intellectual disability, and optic atrophy (lee2023s‐adenosylmethionineandnicotinamide pages 4-6)
- WES has been used as a discovery/diagnostic tool in genetically heterogeneous hearing loss (robusto2015theexpandingspectrum pages 1-2)
- Targeted panel sequencing plus confirmatory enzyme assays (erythrocyte PRS activity) has been used in clinical diagnosis (puusepp2020atypicalpresentationof pages 1-2)

### Differential diagnosis
The diagnostic workup in reported cases includes audiologic, neurophysiologic, ophthalmologic and neuroimaging evaluations to distinguish PRPS1-related syndromic disease from other causes of hearing loss, neuropathy, and retinal disease. (puusepp2020atypicalpresentationof pages 1-2)

---

## 11. Outcome / prognosis
- Severe Arts syndrome is associated with progressive decline and early mortality in historical cohorts; the foundational 2007 AJHG report describes early deaths in multiple affected males in the families studied. (brouwer2007artssyndromeis pages 3-4)
- Limited treated case reports suggest improved stability/trajectory, but evidence is low (case-based; no controlled trials). (lee2023s‐adenosylmethionineandnicotinamide pages 4-6)

---

## 12. Treatment

### Current management (real-world)
- Predominantly **supportive/symptomatic management** (e.g., addressing sensory impairment and neurological complications); hypouricemic drugs are relevant for PRPS1 superactivity but do **not** improve hearing/neurodevelopment in PRPS1 deficiency phenotypes. (camici2023inbornerrorsof pages 4-7)

### Experimental / emerging: SAMe and nicotinamide riboside
A 2023 case report plus literature review summarizes the rationale and limited clinical experience:
- rationale: bypass PRPP-dependent steps by supplying downstream precursors to purine and NAD pathways (lee2023s‐adenosylmethionineandnicotinamide pages 1-2)
- direct abstract-quote evidence (2023): “**All patients had stability or improvement of symptoms, suggesting that SAMe and NR can be a treatment option in Arts syndrome, though further studies are warranted.**” (lee2023s‐adenosylmethionineandnicotinamide pages 1-2)

Mechanistic/immune outcomes in Arts syndrome (case-based):
- SAM+NR co-therapy improved T-cell survival/function and partially rescued cytokine responses; biochemical measurements indicated persistent NAD deficiency with partial NADP restoration and improved erythrocyte ATP/GTP. (lenherr2021cotherapywithsadenosylmethionine pages 2-3)

**Visual evidence (treatment case summaries):**
- Lee et al. Table 1 summarizes prior Arts syndrome patients treated with SAMe ± NR and reported outcomes. (lee2023s‐adenosylmethionineandnicotinamide media 265985d2, lee2023s‐adenosylmethionineandnicotinamide media 29d0cecc)

### Clinical trials / studies
- **NCT06092346 (NHGRI)**: observational prospective natural history study of purine/pyrimidine metabolism disorders; explicitly lists PRPS1 deficiency/Arts syndrome/CMT among included conditions; first posted 2023-10-23; study start 2023-12-19; recruiting. URL: https://clinicaltrials.gov/ct2/show/NCT06092346 (NCT06092346 chunk 1, NCT06092346 chunk 2)

### Suggested MAXO terms (examples)
- MAXO:0000472 dietary supplementation
- MAXO:0000782 cochlear implantation (for hearing loss management)
- MAXO:0001175 genetic counseling
- MAXO:0001298 physical therapy

**Uridine therapy:** no uridine intervention evidence was identified in the retrieved corpus; this report does not claim uridine use.

---

## 13. Prevention
- **Primary prevention:** not applicable in the traditional sense for monogenic disorders; focus is on **family planning and carrier detection**.
- **Secondary prevention:** early diagnosis through genetic testing in individuals with suggestive phenotypes (hearing loss ± optic/neuropathy/immunodeficiency) can enable earlier supportive interventions and consideration of experimental supplementation in severe disease. (lee2023s‐adenosylmethionineandnicotinamide pages 4-6)
- **Genetic counseling (X-linked):** counseling is critical given X-linked inheritance, potential female manifestations, and intrafamilial variability influenced by X-inactivation/mosaicism. (nassogne2024neurologicalpresentationsof pages 2-3, lee2023s‐adenosylmethionineandnicotinamide pages 6-7)

---

## 14. Other species / natural disease
No naturally occurring PRPS1 deficiency analogs in non-human species were identified in the retrieved sources.

---

## 15. Model organisms
No PRPS1-deficiency-specific animal model details were retrieved in the current evidence set. The report therefore does not assert specific model phenotypes.

---

## Expert opinion / analysis (evidence-constrained)
The most authoritative recent synthesis supports a pragmatic diagnostic stance: because biochemical markers can be inconsistent, **combined molecular testing and functional enzymology** are emphasized across purine metabolism disorders, including PRPS1-related disease. (puusepp2020atypicalpresentationof pages 1-2, dewulf2022disordersofpurine pages 4-4)

Therapeutic evidence for SAMe/NR remains limited to case reports and small series; nevertheless, the combination of (i) mechanistic plausibility (bypassing PRPP-dependent steps), (ii) reported clinical stability/improvement, and (iii) immune-cell functional rescue in an Arts syndrome case argues that **carefully monitored supplementation protocols** may be reasonable in selected severe cases while awaiting more systematic natural-history data and interventional trials. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2, lenherr2021cotherapywithsadenosylmethionine pages 2-3, NCT06092346 chunk 1)

---

## References (URLs and publication dates)
- Lee A et al. *JIMD Reports*. Sep 2023. “S‐adenosylmethionine and nicotinamide riboside therapy in Arts syndrome: A case report and literature review.” https://doi.org/10.1002/jmd2.12395 (lee2023s‐adenosylmethionineandnicotinamide pages 1-2)
- Nassogne M-C et al. *European Journal of Paediatric Neurology*. Jan 2024. https://doi.org/10.1016/j.ejpn.2023.11.013 (nassogne2024neurologicalpresentationsof pages 2-3)
- Feng H et al. *Orphanet Journal of Rare Diseases*. Sep 2024. https://doi.org/10.1186/s13023-024-03338-z (feng2024genomicandphenotypic pages 1-2)
- Chen L et al. *Nature Chemical Biology*. Jun 2024. https://doi.org/10.1038/s41589-023-01354-x (chen2024directstimulationof pages 1-2)
- de Brouwer APM et al. *American Journal of Human Genetics*. Sep 2007. https://doi.org/10.1086/520706 (brouwer2007artssyndromeis pages 1-2)
- Lenherr N et al. *Molecular Genetics and Metabolism Reports*. Mar 2021. https://doi.org/10.1016/j.ymgmr.2021.100709 (lenherr2021cotherapywithsadenosylmethionine pages 1-2)
- Puusepp S et al. *Molecular Genetics and Metabolism Reports*. Dec 2020. https://doi.org/10.1016/j.ymgmr.2020.100677 (puusepp2020atypicalpresentationof pages 1-2)
- ClinicalTrials.gov NCT06092346. First posted 2023-10-23. https://clinicaltrials.gov/ct2/show/NCT06092346 (NCT06092346 chunk 1)


References

1. (lee2023s‐adenosylmethionineandnicotinamide pages 1-2): Angela Lee, Renatta Knox, Margaret Reynolds, Erin McRoy, and Hoanh Nguyen. S‐adenosylmethionine and nicotinamide riboside therapy in arts syndrome: a case report and literature review. JIMD Reports, 64:417-423, Sep 2023. URL: https://doi.org/10.1002/jmd2.12395, doi:10.1002/jmd2.12395. This article has 7 citations and is from a peer-reviewed journal.

2. (nassogne2024neurologicalpresentationsof pages 2-3): Marie-Cécile Nassogne, Sandrine Marie, and Joseph P. Dewulf. Neurological presentations of inborn errors of purine and pyrimidine metabolism. European Journal of Paediatric Neurology, 48:69-77, Jan 2024. URL: https://doi.org/10.1016/j.ejpn.2023.11.013, doi:10.1016/j.ejpn.2023.11.013. This article has 14 citations and is from a peer-reviewed journal.

3. (camici2023inbornerrorsof pages 4-7): Marcella Camici, Mercedes Garcia-Gil, Simone Allegrini, Rossana Pesi, Giulia Bernardini, Vanna Micheli, and Maria Grazia Tozzi. Inborn errors of purine salvage and catabolism. Metabolites, 13:787, Jun 2023. URL: https://doi.org/10.3390/metabo13070787, doi:10.3390/metabo13070787. This article has 22 citations.

4. (chen2024directstimulationof pages 1-2): Lulu Chen, Qi Zhou, Pingfeng Zhang, Wei Tan, Yingge Li, Ziwen Xu, Junfeng Ma, Gary M. Kupfer, Yanxin Pei, Qibin Song, and Huadong Pei. Direct stimulation of de novo nucleotide synthesis by o-glcnacylation. Nature Chemical Biology, 20:19-29, Jun 2024. URL: https://doi.org/10.1038/s41589-023-01354-x, doi:10.1038/s41589-023-01354-x. This article has 37 citations and is from a highest quality peer-reviewed journal.

5. (chen2024directstimulationof pages 21-25): Lulu Chen, Qi Zhou, Pingfeng Zhang, Wei Tan, Yingge Li, Ziwen Xu, Junfeng Ma, Gary M. Kupfer, Yanxin Pei, Qibin Song, and Huadong Pei. Direct stimulation of de novo nucleotide synthesis by o-glcnacylation. Nature Chemical Biology, 20:19-29, Jun 2024. URL: https://doi.org/10.1038/s41589-023-01354-x, doi:10.1038/s41589-023-01354-x. This article has 37 citations and is from a highest quality peer-reviewed journal.

6. (lenherr2021cotherapywithsadenosylmethionine pages 2-3): Nina Lenherr, John Christodoulou, John Duley, Doreen Dobritzsch, Lynette Fairbanks, Alexandre N. Datta, Isabel Filges, Nicolas Gürtler, Jeroen Roelofsen, André B.P. van Kuilenburg, Claudia Kemper, Erin E. West, Gabor Szinnai, and Martina Huemer. Co-therapy with s-adenosylmethionine and nicotinamide riboside improves t-cell survival and function in arts syndrome (prps1 deficiency). Molecular Genetics and Metabolism Reports, 26:100709, Mar 2021. URL: https://doi.org/10.1016/j.ymgmr.2021.100709, doi:10.1016/j.ymgmr.2021.100709. This article has 23 citations.

7. (lee2023s‐adenosylmethionineandnicotinamide pages 4-6): Angela Lee, Renatta Knox, Margaret Reynolds, Erin McRoy, and Hoanh Nguyen. S‐adenosylmethionine and nicotinamide riboside therapy in arts syndrome: a case report and literature review. JIMD Reports, 64:417-423, Sep 2023. URL: https://doi.org/10.1002/jmd2.12395, doi:10.1002/jmd2.12395. This article has 7 citations and is from a peer-reviewed journal.

8. (feng2024genomicandphenotypic pages 4-5): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

9. (nassogne2024neurologicalpresentationsof pages 3-4): Marie-Cécile Nassogne, Sandrine Marie, and Joseph P. Dewulf. Neurological presentations of inborn errors of purine and pyrimidine metabolism. European Journal of Paediatric Neurology, 48:69-77, Jan 2024. URL: https://doi.org/10.1016/j.ejpn.2023.11.013, doi:10.1016/j.ejpn.2023.11.013. This article has 14 citations and is from a peer-reviewed journal.

10. (lenherr2021cotherapywithsadenosylmethionine pages 1-2): Nina Lenherr, John Christodoulou, John Duley, Doreen Dobritzsch, Lynette Fairbanks, Alexandre N. Datta, Isabel Filges, Nicolas Gürtler, Jeroen Roelofsen, André B.P. van Kuilenburg, Claudia Kemper, Erin E. West, Gabor Szinnai, and Martina Huemer. Co-therapy with s-adenosylmethionine and nicotinamide riboside improves t-cell survival and function in arts syndrome (prps1 deficiency). Molecular Genetics and Metabolism Reports, 26:100709, Mar 2021. URL: https://doi.org/10.1016/j.ymgmr.2021.100709, doi:10.1016/j.ymgmr.2021.100709. This article has 23 citations.

11. (brouwer2007artssyndromeis pages 3-4): Arjan P.M. de Brouwer, Kelly L. Williams, John A. Duley, André B.P. van Kuilenburg, Sander B. Nabuurs, Michael Egmont-Petersen, Dorien Lugtenberg, Lida Zoetekouw, Martijn J.G. Banning, Melissa Roeffen, Ben C.J. Hamel, Linda Weaving, Robert A. Ouvrier, Jennifer A. Donald, Ron A. Wevers, John Christodoulou, and Hans van Bokhoven. Arts syndrome is caused by loss-of-function mutations in prps1. The American Journal of Human Genetics, 81:507-518, Sep 2007. URL: https://doi.org/10.1086/520706, doi:10.1086/520706. This article has 113 citations.

12. (lee2023s‐adenosylmethionineandnicotinamide pages 2-4): Angela Lee, Renatta Knox, Margaret Reynolds, Erin McRoy, and Hoanh Nguyen. S‐adenosylmethionine and nicotinamide riboside therapy in arts syndrome: a case report and literature review. JIMD Reports, 64:417-423, Sep 2023. URL: https://doi.org/10.1002/jmd2.12395, doi:10.1002/jmd2.12395. This article has 7 citations and is from a peer-reviewed journal.

13. (feng2024genomicandphenotypic pages 2-4): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

14. (feng2024genomicandphenotypic pages 1-2): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

15. (chen2024directstimulationof pages 2-3): Lulu Chen, Qi Zhou, Pingfeng Zhang, Wei Tan, Yingge Li, Ziwen Xu, Junfeng Ma, Gary M. Kupfer, Yanxin Pei, Qibin Song, and Huadong Pei. Direct stimulation of de novo nucleotide synthesis by o-glcnacylation. Nature Chemical Biology, 20:19-29, Jun 2024. URL: https://doi.org/10.1038/s41589-023-01354-x, doi:10.1038/s41589-023-01354-x. This article has 37 citations and is from a highest quality peer-reviewed journal.

16. (NCT06092346 chunk 1):  A Natural History Study Seeks to Understand the Clinical, Genomic, Pharmacological, Laboratory, and Dietary Determinates of Pyrimidine and Purine Metabolism Disorders. National Human Genome Research Institute (NHGRI). 2023. ClinicalTrials.gov Identifier: NCT06092346

17. (NCT06092346 chunk 2):  A Natural History Study Seeks to Understand the Clinical, Genomic, Pharmacological, Laboratory, and Dietary Determinates of Pyrimidine and Purine Metabolism Disorders. National Human Genome Research Institute (NHGRI). 2023. ClinicalTrials.gov Identifier: NCT06092346

18. (lee2023s‐adenosylmethionineandnicotinamide pages 6-7): Angela Lee, Renatta Knox, Margaret Reynolds, Erin McRoy, and Hoanh Nguyen. S‐adenosylmethionine and nicotinamide riboside therapy in arts syndrome: a case report and literature review. JIMD Reports, 64:417-423, Sep 2023. URL: https://doi.org/10.1002/jmd2.12395, doi:10.1002/jmd2.12395. This article has 7 citations and is from a peer-reviewed journal.

19. (robusto2015theexpandingspectrum pages 4-6): Michela Robusto, Mingyan Fang, Rosanna Asselta, Pierangela Castorina, Stefano C Previtali, Sonia Caccia, Elena Benzoni, Raimondo De Cristofaro, Cong Yu, Antonio Cesarani, Xuanzhu Liu, Wangsheng Li, Paola Primignani, Umberto Ambrosetti, Xun Xu, Stefano Duga, and Giulia Soldà. The expanding spectrum of prps1-associated phenotypes: three novel mutations segregating with x-linked hearing loss and mild peripheral neuropathy. European Journal of Human Genetics, 23:766-773, Sep 2015. URL: https://doi.org/10.1038/ejhg.2014.168, doi:10.1038/ejhg.2014.168. This article has 40 citations and is from a domain leading peer-reviewed journal.

20. (feng2024genomicandphenotypic pages 9-10): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

21. (puusepp2020atypicalpresentationof pages 1-2): Sanna Puusepp, Karit Reinson, Sander Pajusalu, André B.P. van Kuilenburg, Doreen Dobritzsch, Jeroen Roelofsen, Werner Stenzel, and Katrin Õunap. Atypical presentation of arts syndrome due to a novel hemizygous loss-of-function variant in the prps1 gene. Molecular Genetics and Metabolism Reports, 25:100677, Dec 2020. URL: https://doi.org/10.1016/j.ymgmr.2020.100677, doi:10.1016/j.ymgmr.2020.100677. This article has 16 citations.

22. (robusto2015theexpandingspectrum pages 1-2): Michela Robusto, Mingyan Fang, Rosanna Asselta, Pierangela Castorina, Stefano C Previtali, Sonia Caccia, Elena Benzoni, Raimondo De Cristofaro, Cong Yu, Antonio Cesarani, Xuanzhu Liu, Wangsheng Li, Paola Primignani, Umberto Ambrosetti, Xun Xu, Stefano Duga, and Giulia Soldà. The expanding spectrum of prps1-associated phenotypes: three novel mutations segregating with x-linked hearing loss and mild peripheral neuropathy. European Journal of Human Genetics, 23:766-773, Sep 2015. URL: https://doi.org/10.1038/ejhg.2014.168, doi:10.1038/ejhg.2014.168. This article has 40 citations and is from a domain leading peer-reviewed journal.

23. (lee2023s‐adenosylmethionineandnicotinamide media 265985d2): Angela Lee, Renatta Knox, Margaret Reynolds, Erin McRoy, and Hoanh Nguyen. S‐adenosylmethionine and nicotinamide riboside therapy in arts syndrome: a case report and literature review. JIMD Reports, 64:417-423, Sep 2023. URL: https://doi.org/10.1002/jmd2.12395, doi:10.1002/jmd2.12395. This article has 7 citations and is from a peer-reviewed journal.

24. (lee2023s‐adenosylmethionineandnicotinamide media 29d0cecc): Angela Lee, Renatta Knox, Margaret Reynolds, Erin McRoy, and Hoanh Nguyen. S‐adenosylmethionine and nicotinamide riboside therapy in arts syndrome: a case report and literature review. JIMD Reports, 64:417-423, Sep 2023. URL: https://doi.org/10.1002/jmd2.12395, doi:10.1002/jmd2.12395. This article has 7 citations and is from a peer-reviewed journal.

25. (dewulf2022disordersofpurine pages 4-4): Joseph P. Dewulf, Sandrine Marie, and Marie-Cécile Nassogne. Disorders of purine biosynthesis metabolism. Molecular Genetics and Metabolism, 136:190-198, Jul 2022. URL: https://doi.org/10.1016/j.ymgme.2021.12.016, doi:10.1016/j.ymgme.2021.12.016. This article has 100 citations and is from a peer-reviewed journal.

26. (brouwer2007artssyndromeis pages 1-2): Arjan P.M. de Brouwer, Kelly L. Williams, John A. Duley, André B.P. van Kuilenburg, Sander B. Nabuurs, Michael Egmont-Petersen, Dorien Lugtenberg, Lida Zoetekouw, Martijn J.G. Banning, Melissa Roeffen, Ben C.J. Hamel, Linda Weaving, Robert A. Ouvrier, Jennifer A. Donald, Ron A. Wevers, John Christodoulou, and Hans van Bokhoven. Arts syndrome is caused by loss-of-function mutations in prps1. The American Journal of Human Genetics, 81:507-518, Sep 2007. URL: https://doi.org/10.1086/520706, doi:10.1086/520706. This article has 113 citations.