---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:15:34.814795'
end_time: '2026-05-05T23:43:49.120226'
duration_seconds: 1694.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy
  mondo_id: ''
  category: Neurodegenerative Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disease

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy** covering all of the
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
- **Disease Name:** Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disease

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy** covering all of the
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


## Comprehensive Disease Characteristics Research Report
### Target disease
**Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy (ADLD; LMNB1-related autosomal dominant leukodystrophy)** — a rare, progressive adult-onset leukodystrophy caused by **LMNB1 overexpression**, leading to **central nervous system (CNS) demyelination** with a characteristic symmetric MRI pattern and prominent autonomic dysfunction. (ortiz2024aretrospectivereview pages 1-2, neri2023understandingtheultrarare pages 1-2)

| Disease / synonyms | Key identifiers explicitly stated | Causal gene & mechanism | Typical age of onset | Core clinical features | Hallmark MRI findings | Natural history / prognosis | Source year & DOI URL | Best supporting citations |
|---|---|---|---|---|---|---|---|---|
| Adult-onset autosomal dominant demyelinating leukodystrophy (ADLD); LMNB1-related autosomal dominant leukodystrophy; adult-onset autosomal dominant leukodystrophy with autonomic symptoms | OMIM/MIM #169500 explicitly stated | **LMNB1** (5q23.2); heterozygous **LMNB1 duplication** causing Lamin B1 overexpression and CNS demyelination | Usually 4th-6th decade; mean/median onset around late 30s to 40s | Early autonomic dysfunction (bladder, erectile dysfunction, orthostatic hypotension, sweating abnormalities), then spasticity/pyramidal signs, ataxia/tremor, later cognitive decline | Symmetric confluent T2 white-matter hyperintensities involving deep/periventricular cerebral WM, corticospinal tracts, posterior limb of internal capsule, corpus callosum, brainstem, middle/superior cerebellar peduncles; spinal cord atrophy/thinning | Slowly progressive, fatal/life-limiting; survival often 10-20+ years after onset | 2024, https://doi.org/10.1007/s44162-024-00055-w ; 2019, https://doi.org/10.1136/jnnp-2018-319481 ; 2017, https://doi.org/10.3389/fnmol.2017.00215 | (ortiz2024aretrospectivereview pages 1-2, ortiz2024aretrospectivereview pages 2-3, dai2017anlmnb1duplication pages 1-2, lin2011adultonsetautosomaldominant pages 1-2) |
| LMNB1-related ADLD due to **upstream noncoding deletion** | OMIM #169500 explicitly stated | **LMNB1**; large heterozygous **upstream deletion** (e.g., ~660 kb) removes a topological domain boundary, causing **enhancer adoption** and LMNB1 overexpression | 4th-5th decade typically; reported deletion cases 32-52 years | Progressive leukodystrophy with weakness, spasticity, hypophonia/dysarthria, cerebellar dysfunction; compared with duplication cases, may show less early dysautonomia and less cerebellar/spinal involvement | Widespread white-matter alterations; corticospinal tract involvement from upper frontal lobes to cerebral peduncles; spinal cord may be relatively less affected than duplication cases in some families | Fatal progressive course; death often 10-20 years after onset | 2015, https://doi.org/10.1093/hmg/ddv065 ; 2019, https://doi.org/10.1212/nxg.0000000000000305 | (giorgio2015alargegenomic pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2) |
| Longitudinal LMNB1-duplication ADLD natural history | Not focused on identifier; disease is LMNB1-related ADLD | **LMNB1 duplication** | Symptoms usually begin in 5th-6th decade; MRI may be abnormal >10 years before symptoms and as early as age 29 in asymptomatic carriers | Autonomic dysfunction often precedes motor symptoms; ascending myelopathy pattern with gait impairment, spastic paraplegia progressing to tetraplegia/pseudobulbar palsy; mild early cognitive issues, dementia late | Extensive T2 hyperintensities in cerebellar peduncles and cerebral WM with relatively spared periventricular rim early; pyramidal tract extension; all carriers showed spinal cord WM abnormalities; no gadolinium enhancement | **EDSS 6** at mean 59 ± 8 years (**11 ± 5 years** from onset); **EDSS 8** at mean 61 ± 6 years (**14 ± 4 years** from onset); interval EDSS 6→8 **5 ± 2 years**; deaths at mean 66 ± 6 years (**17 ± 6 years** from onset); median survival **18 years** | 2015, https://doi.org/10.1002/ana.24452 | (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 1-2, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 7-9) |
| Mayo Clinic retrospective LMNB1-related ADLD cohort | No additional identifier stated in excerpt beyond disease name | All 8 patients had **LMNB1 duplication** | Onset range **33-64 years**; median onset **38.5 years**; median diagnosis age **46 years** | Cognitive difficulties **8/8**, fatigue **7/8**, mood disturbances **5/8**, tremor **4/8**, migraine **4/8**; sex-specific first symptoms included erectile dysfunction/neurogenic bladder in men and weakness/bladder dysfunction/depression in women | All reviewed brain MRIs showed symmetric confluent T2 deep cerebral/periventricular WM hyperintensities with internal capsule, corpus callosum, brainstem corticospinal tract, superior/middle cerebellar peduncle involvement; spine MRI showed moderate diffuse cord atrophy | Median diagnostic delay **6 years** (IQR 2.3-10); white-matter MRI abnormalities can predate symptoms by **9-16 years** in examples; no cure, supportive management only | 2024, https://doi.org/10.1007/s44162-024-00055-w | (ortiz2024aretrospectivereview pages 1-2, ortiz2024aretrospectivereview pages 2-3, ortiz2024aretrospectivereview pages 3-5) |


*Table: This table condenses the core disease-defining information for LMNB1-related adult-onset autosomal dominant demyelinating leukodystrophy, including identifiers, mechanisms, phenotype, imaging, and prognosis. It is useful as a quick-reference artifact for knowledge-base population and citation tracking.*

| Domain | Key points for LMNB1-related ADLD | Practical implementation / test or treatment | Source year + URL | Evidence |
|---|---|---|---|---|
| Diagnostic clues: clinical phenotype | Adult-onset leukodystrophy, usually 4th-5th decade; early autonomic dysfunction is typical (bladder/bowel dysfunction, orthostatic hypotension, sweating abnormalities, erectile dysfunction), followed by gait impairment, pyramidal signs/spasticity, ataxia, and later cognitive decline; women may present with motor-predominant phenotypes and cases may be mistaken for multiple sclerosis or bvFTD-spectrum disease | Suspect LMNB1-related ADLD in adults with progressive dysautonomia plus spastic-ataxic syndrome and family history suggestive of autosomal dominant inheritance | 2024: https://doi.org/10.1007/s44162-024-00055-w ; 2023: https://doi.org/10.3389/fneur.2023.1219324 | (ortiz2024aretrospectivereview pages 3-5, muthusamy2023adultonsetleukodystrophiesa pages 10-11) |
| Diagnostic clues: hallmark MRI | Stereotyped MRI pattern: symmetric confluent T2 white-matter hyperintensities involving deep/periventricular cerebral white matter, corticospinal tracts, posterior limb of the internal capsule, corpus callosum, brainstem, and middle/superior cerebellar peduncles; relative sparing of subcortical U-fibers and periventricular rim may help; spinal cord atrophy/thinning is common; no contrast enhancement is typical | Obtain brain MRI with T2/FLAIR and spine imaging; recognize that MRI abnormalities can predate symptoms by years and may be the earliest clue | 2024: https://doi.org/10.1007/s44162-024-00055-w ; 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2015: https://doi.org/10.1002/ana.24452 | (ortiz2024aretrospectivereview pages 2-3, muthusamy2023adultonsetleukodystrophiesa pages 10-11, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7) |
| Recommended genetic confirmation | Disease is caused by LMNB1 dosage/expression abnormalities: usually heterozygous LMNB1 duplication, rarely upstream deletion causing LMNB1 overexpression | Order targeted LMNB1 copy-number / structural-variant testing when clinicoradiologic pattern is suggestive | 2024: https://doi.org/10.1007/s44162-024-00055-w ; 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2015: https://doi.org/10.1093/hmg/ddv065 | (ortiz2024aretrospectivereview pages 3-5, muthusamy2023adultonsetleukodystrophiesa pages 10-11, giorgio2015alargegenomic pages 1-2) |
| Genetic methods to use | Copy-number focused methods are required; literature specifically supports targeted CNV/duplication testing and notes use of MLPA, gene-targeted microarray/aCGH, capillary-array methods, qPCR/other CNV assays in adult leukodystrophy workflows; custom array-CGH identified upstream LMNB1 deletion in one family | Preferred methods: LMNB1 deletion/duplication analysis, MLPA, array-CGH/gene-targeted microarray, or other validated CNV assays; consider single-gene LMNB1 testing first if phenotype is classic | 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2024: https://doi.org/10.1007/s44162-024-00055-w ; 2015: https://doi.org/10.1093/hmg/ddv065 | (muthusamy2023adultonsetleukodystrophiesa pages 23-24, ortiz2024aretrospectivereview pages 3-5, ortiz2024aretrospectivereview pages 2-3, giorgio2015alargegenomic pages 1-2) |
| Limitation of standard NGS | Standard short-read NGS/WES/WGS may miss LMNB1 duplications/upstream deletions and other CNV/deep intronic/complex variants; relying only on routine NGS can delay diagnosis | If exome/genome is negative but MRI/phenotype strongly suggest ADLD, reflex to CNV-focused LMNB1 testing rather than stopping workup | 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2024: https://doi.org/10.1007/s44162-024-00055-w | (muthusamy2023adultonsetleukodystrophiesa pages 10-11, ortiz2024aretrospectivereview pages 3-5, muthusamy2023adultonsetleukodystrophiesa pages 21-23) |
| Ancillary autonomic testing | Autonomic reflex screen, tilt table, QSART, thermoregulatory sweat testing, and urodynamics often show orthostatic hypotension, anhidrosis, and bladder dysfunction | Useful both for phenotype definition and longitudinal monitoring, especially in early dysautonomia | 2024: https://doi.org/10.1007/s44162-024-00055-w | (ortiz2024aretrospectivereview pages 2-3) |
| Ancillary electrophysiology | EMG/NCS are often normal or do not show polyneuropathy; neurophysiology may instead support central myelopathy (e.g., SSEPs, motor conduction delay in some series) | Use EMG/NCS mainly to exclude peripheral neuropathy mimics rather than to confirm ADLD | 2024: https://doi.org/10.1007/s44162-024-00055-w ; 2015: https://doi.org/10.1002/ana.24452 | (ortiz2024aretrospectivereview pages 2-3, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7) |
| General adult leukodystrophy workflow | First exclude acquired mimics (infectious, inflammatory, autoimmune, vascular, neoplastic, toxic, metabolic), then integrate family history, exam, MRI pattern recognition, biochemical testing, and genetics; advanced MRI and periodic reinterpretation improve yield | Practical workflow: history + 3-generation pedigree -> MRI pattern review -> targeted biochemical tests for treatable mimics -> targeted CNV/single-gene testing if classic -> broader panel/WES/WGS with reanalysis if unresolved | 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2019: https://doi.org/10.1148/rg.2019180081 ; 2018: https://doi.org/10.1038/nrneurol.2017.175 | (muthusamy2023adultonsetleukodystrophiesa pages 23-24, muthusamy2023adultonsetleukodystrophiesa pages 1-2, muthusamy2023adultonsetleukodystrophiesa pages 21-23, kohler2018adulthoodleukodystrophies pages 3-4, resende2019adultleukodystrophiesa pages 1-2) |
| Key differential: multiple sclerosis / acquired inflammatory myeloleukoencephalopathy | ADLD can mimic MS, but ADLD typically has symmetric confluent white-matter disease, prominent dysautonomia, lack of gadolinium enhancement, and spinal cord atrophy rather than inflammatory lesions; acquired causes are suggested by rapid onset, steroid responsiveness, systemic features, enhancement | Use MRI symmetry/enhancement pattern, course, and inflammatory context to separate ADLD from MS and other acquired disorders | 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2019: https://doi.org/10.1136/jnnp-2018-319481 | (muthusamy2023adultonsetleukodystrophiesa pages 10-11, lynch2019practicalapproachto pages 2-3, muthusamy2023adultonsetleukodystrophiesa pages 21-23) |
| Key differential: AMN / X-ALD and other inherited leukodystrophies | AMN may show normal brain MRI or pyramidal-tract changes with spinal cord atrophy; AMACR deficiency shows symmetric thalamic/midbrain/pons/cerebellar-tract changes and elevated pristanic acid; CSF1R disease may have early psychiatric syndrome and punctate calcifications on CT/gradient-echo; Gordon Holmes syndrome has prominent cerebellar atrophy/endocrine clues | Distinguish with VLCFA testing, pristanic acid, CT/gradient-echo for calcifications, endocrine evaluation, and disorder-specific gene testing | 2023: https://doi.org/10.3389/fneur.2023.1219324 ; 2019: https://doi.org/10.1136/jnnp-2018-319481 | (muthusamy2023adultonsetleukodystrophiesa pages 10-11, lynch2019practicalapproachto pages 2-3) |
| Current standard treatment | No curative or approved disease-modifying therapy; management is supportive and symptomatic | Symptom-directed care may include bladder/autonomic management, spasticity relief, physical/functional exercise, cognitive support, dietary guidance/neurotrophic support in reported case series, and multidisciplinary follow-up | 2024: https://doi.org/10.1007/s44162-024-00055-w ; 2025: https://doi.org/10.3389/fnins.2025.1531593 | (ortiz2024aretrospectivereview pages 3-5, jiang2025casereportlmnb1 pages 4-5) |
| Investigational therapy: allele-specific RNAi | Preclinical proof-of-concept supports allele-specific RNA interference to reduce LMNB1 toward physiologic levels without over-suppression; siRNA/shRNA targeting rs1051644 restored LMNB1 mRNA/protein near control levels and improved nuclear morphology and neurite growth in fibroblasts, directly reprogrammed neurons, and oligodendrocyte models | Experimental only; supports LMNB1-lowering as a rational targeted strategy for future translation | 2019: https://doi.org/10.1093/brain/awz139 | (giorgio2019allelespecificsilencingas pages 1-6, giorgio2019allelespecificsilencingas pages 6-10, giorgio2019allelespecificsilencingas pages 17-20, giorgio2019allelespecificsilencingas pages 20-23) |
| Investigational therapy: personalized ASO clinical trial | ClinicalTrials.gov lists a personalized antisense oligonucleotide trial for a single participant with LMNB1-duplication ADLD: nL-LMNB1-001, open-label, phase 1/2, active-not-recruiting, sponsor n-Lorem Foundation with Mayo Clinic collaboration, enrollment 1 | Endpoints at baseline and 6/12/18/24 months include gait motion analysis, 6-minute walk, 25-feet walk, neurological functioning, MRI brain atrophy; secondary measures include urodynamics, autonomic testing, and safety/tolerability | 2025 registry entry: https://clinicaltrials.gov/study/NCT06816498 | (NCT06816498 chunk 1) |


*Table: This table summarizes how LMNB1-related ADLD is recognized and confirmed in practice, including the MRI and autonomic phenotype, the need for CNV-focused LMNB1 testing beyond standard NGS, major differential diagnoses, and the current treatment landscape from supportive care to emerging gene-silencing therapies and the personalized ASO trial NCT06816498.*

---

## 1. Disease information
### 1.1 Overview (current understanding)
ADLD is a **slowly progressive, life-limiting/fatal** adult-onset leukodystrophy characterized by **progressive CNS white-matter loss/demyelination**, typically beginning with **autonomic dysfunction** and later evolving to **spasticity/pyramidal signs and ataxia**, with **cognitive decline** occurring later in the course in many patients. (ortiz2024aretrospectivereview pages 1-2, neri2023understandingtheultrarare pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)

A key practical diagnostic observation from longitudinal cohorts is that **MRI can become abnormal many years before symptoms**, making imaging pattern recognition a major real-world entry point for diagnosis. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7, ortiz2024aretrospectivereview pages 3-5)

### 1.2 Key identifiers
* **OMIM/MIM:** **169500** (“ADLD”) is explicitly stated in multiple primary sources. (dai2017anlmnb1duplication pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)
* **Other requested identifiers (Orphanet, ICD-10/11, MeSH, MONDO):** not present in the retrieved full-text excerpts used for this report; therefore they cannot be reported here with evidence-grade citation. (ortiz2024aretrospectivereview pages 1-2, neri2023understandingtheultrarare pages 1-2)

### 1.3 Synonyms / alternative names
Synonyms used in the cited literature include:
* “**LMNB1-related autosomal dominant leukodystrophy**” (ortiz2024aretrospectivereview pages 1-2)
* “**Adult-onset autosomal dominant leukodystrophy with autonomic symptoms**” (santos2012adultonsetautosomaldominant pages 3-3)
* “**Autosomal Dominant Leukodystrophy with Autonomic Disease**” (educational materials) (gosky2021assessmentanddevelopment pages 92-96)

### 1.4 Evidence provenance
The information in this report is derived primarily from:
* **Aggregated disease-level resources:** expert reviews and structured diagnostic guides for adult leukodystrophies (2023–2024 emphasized). (neri2023understandingtheultrarare pages 1-2, muthusamy2023adultonsetleukodystrophiesa pages 10-11)
* **Human clinical cohorts/case series:** longitudinal natural history (Finnsson 2015) and a 2024 Mayo Clinic retrospective cohort. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7, ortiz2024aretrospectivereview pages 1-2)
* **Mechanistic/model-organism studies:** transgenic mouse and cellular models summarized in the 2023 mechanistic review. (neri2023understandingtheultrarare pages 4-6, neri2023understandingtheultrarare pages 6-7)

---

## 2. Etiology
### 2.1 Disease causal factors
ADLD is fundamentally a **genetic dosage/regulatory disorder**: both coding and non-coding structural alterations at the **LMNB1** locus converge on **LMNB1 (lamin B1) overexpression**, which is considered causal for CNS demyelination. (neri2023understandingtheultrarare pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)

Two established pathogenic alteration classes:
1. **Tandem duplication spanning LMNB1** (most common) → increased LMNB1 gene dosage and expression. (dai2017anlmnb1duplication pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)
2. **Upstream non-coding deletions** that cause **enhancer adoption** (disrupted 3D genomic boundary permitting forebrain enhancers to activate LMNB1) → LMNB1 overexpression without LMNB1 coding duplication. (giorgio2015alargegenomic pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)

Quantitative tissue evidence for LMNB1 overexpression includes ~2–3-fold increased LMNB1 transcripts in one upstream-deletion family, and ~7-fold increased lamin B1 protein in frontal lobe compared with control in postmortem tissue. (giorgio2015alargegenomic pages 1-2)

### 2.2 Risk factors
**Primary risk factor: autosomal dominant inheritance** of a pathogenic LMNB1 structural variant. Family history is frequently present (e.g., 6/8 in one Mayo cohort). (ortiz2024aretrospectivereview pages 1-2)

Non-genetic/environmental susceptibility factors are not established in the cited sources; the disorder is best understood as genetically driven. (neri2023understandingtheultrarare pages 1-2)

### 2.3 Protective factors
No protective genetic variants or protective environmental factors were identified in the retrieved evidence. (neri2023understandingtheultrarare pages 1-2)

### 2.4 Gene–environment interaction
Not clearly established in the retrieved evidence. Some clinical observations in longitudinal cohorts include **pseudoexacerbations with heat, fever, or infections**, suggesting that environmental stressors can transiently worsen symptoms, but these do not constitute validated causal gene–environment interactions. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (human)
Across cohorts, the most characteristic phenotype is **early autonomic dysfunction**, followed by progressive motor system involvement:
* **Autonomic dysfunction:** neurogenic bladder/urinary urgency, orthostatic hypotension, anhidrosis/sweating abnormalities; in a longitudinal cohort, bladder dysfunction was present in **100%** and orthostatic hypotension in **77%**. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7)
* **Pyramidal tract dysfunction:** spasticity, progressive spastic paraparesis progressing caudal→rostral in advanced disease. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)
* **Cerebellar involvement:** ataxia, tremor; in a Mayo cohort tremor occurred in **4/8**. (ortiz2024aretrospectivereview pages 1-2)
* **Cognitive/psychiatric:** cognitive difficulties were reported in **8/8** in the Mayo cohort; mood disturbances **5/8**; sleep issues **4/8**. (ortiz2024aretrospectivereview pages 1-2)

### 3.2 Phenotype characteristics (age of onset, progression)
* **Onset:** commonly in the **4th–6th decade**; 2024 Mayo cohort onset range **33–64 years**. (ortiz2024aretrospectivereview pages 1-2)
* **Progression:** slow, insidious progression over years with increasing disability; a characteristic ascending myelopathy pattern is described in the longitudinal study. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 1-2, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)

### 3.3 Phenotype frequencies (recent quantitative cohort)
From an 8-patient Mayo Clinic retrospective cohort (molecularly confirmed LMNB1 duplication):
* cognitive difficulties **8/8**
* fatigue **7/8**
* sleep issues **4/8**
* mood disturbances **5/8**
* tremor **4/8**
* migraine **4/8**
* family history positive **6/8**
* diagnostic delay: median **6 years** (IQR 2.3–10)
(ortiz2024aretrospectivereview pages 1-2)

### 3.4 Quality of life impact
Direct standardized quality-of-life instruments (EQ-5D/SF-36/PROMIS) were not reported in the retrieved excerpts. However, progressive disability milestones (EDSS progression) and autonomic morbidity (urodynamic abnormalities) indicate substantial impairment in mobility and daily functioning. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7, ortiz2024aretrospectivereview pages 2-3)

### 3.5 Suggested HPO terms (examples)
Based on described clinical features, plausible HPO mappings include:
* Autonomic dysfunction: **Neurogenic bladder (HP:0000010)**; **Orthostatic hypotension (HP:0001278)**; **Anhidrosis (HP:0000970)**; **Erectile dysfunction (HP:0100639)** (ortiz2024aretrospectivereview pages 1-2, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7)
* Motor: **Spasticity (HP:0001257)**; **Spastic paraplegia (HP:0001258)**; **Ataxia (HP:0001251)**; **Tremor (HP:0001337)** (ortiz2024aretrospectivereview pages 1-2, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)
* Cognitive/psychiatric: **Cognitive impairment (HP:0100543)**; **Depression (HP:0000716)** (ortiz2024aretrospectivereview pages 1-2)

(These HPO IDs are suggested mappings; the retrieved sources did not explicitly list HPO codes.)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
**LMNB1** (lamin B1) is the causal gene; disease results from **LMNB1 overexpression** rather than canonical loss-of-function. (neri2023understandingtheultrarare pages 1-2, lin2011adultonsetautosomaldominant pages 1-2)

### 4.2 Pathogenic variant classes
* **Structural duplication** of LMNB1 (copy-number gain), often spanning the full gene. (dai2017anlmnb1duplication pages 1-2, santos2012adultonsetautosomaldominant pages 3-3)
* **Nonrecurrent upstream deletions** (regulatory structural variants) causing enhancer adoption. (giorgio2015alargegenomic pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)

### 4.3 Functional consequence
The convergent molecular consequence is **increased Lamin B1 levels** (gain-of-function by overexpression), perturbing nuclear lamina stoichiometry and downstream chromatin/transcription/splicing programs in myelin-relevant cells. (neri2023understandingtheultrarare pages 2-4, neri2023understandingtheultrarare pages 6-7)

### 4.4 Modifier genes / epigenetics
Direct human modifier genes were not identified in the retrieved excerpts. However, mechanistic work suggests epigenetic shifts in oligodendrocytes under LMNB1 overexpression, including **increased repressive histone marks (H3K9me3, H3K27me3)** and **reduced activating acetylation marks (AcH3, AcH4)** in aged oligodendrocytes in transgenic models. (neri2023understandingtheultrarare pages 6-7)

---

## 5. Environmental information
No specific environmental toxins, lifestyle exposures, or infectious triggers were established as causal in the retrieved literature excerpts; ADLD is best understood as genetically caused. (neri2023understandingtheultrarare pages 1-2)

---

## 6. Mechanism / pathophysiology (current understanding)
### 6.1 Causal chain (integrated model)
1. **Upstream trigger:** LMNB1 structural variant (duplication or upstream deletion) → **LMNB1 overexpression**. (neri2023understandingtheultrarare pages 1-2, nmezi2019genomicdeletionsupstream pages 1-2)
2. **Nuclear lamina/chromatin effects:** Lamin B1 excess disturbs nuclear lamina architecture (misshaped/folded nuclei; increased nuclear rigidity) and alters chromatin organization and transcriptional silencing at the nuclear periphery. (neri2023understandingtheultrarare pages 4-6, lin2011adultonsetautosomaldominant pages 1-2)
3. **Myelin cell dysfunction (oligodendrocyte-centered mechanisms):** oligodendrocyte-targeted LMNB1 overexpression can cause premature differentiation arrest and repression of lipid synthesis pathways; in one spinal-cord transgenic model, multiple downregulated genes mapped to lipid synthesis and lipidomics showed reduced myelin lipids. (neri2023understandingtheultrarare pages 4-6)
4. **Spliceopathy and myelin gene dysregulation:** LMNB1 increase is associated with upregulation of **RAVER2**, inhibiting PTB and contributing to abnormal splicing of PTB-target genes including **PLP1**, and PLP1 downregulation has been linked to reduced YY1 binding. (neri2023understandingtheultrarare pages 7-9, dai2017anlmnb1duplication pages 1-2)
5. **Non-cell-autonomous contributions (astrocytopathy):** astrocyte LMNB1 accumulation can reduce **LIF/LIF-R signaling** and downstream PI3K/Akt/mTOR pathway activity, impairing support for oligodendrocytes; astrocytes show reduced viability and reactive changes. (neri2023understandingtheultrarare pages 6-7, neri2023understandingtheultrarare pages 7-9)
6. **Downstream tissue outcome:** progressive, largely non-inflammatory CNS demyelination with vacuolated white matter and relative preservation of oligodendroglia in pathology descriptions. (lin2011adultonsetautosomaldominant pages 1-2)

### 6.2 Immune involvement
ADLD is generally described as lacking prominent inflammatory demyelination; neuropathology notes vacuolated white matter without significant inflammatory infiltrates, distinguishing it from autoimmune demyelination paradigms. (lin2011adultonsetautosomaldominant pages 1-2)

### 6.3 Oxidative stress / inflammatory signaling
Patient-derived cells show disturbed oxidative stress responses and increased ROS after oxidative challenge, and increased activation of inflammatory signaling markers (e.g., phosphorylated NF-κB) in fibroblast-based studies, though confirmation in patient CNS tissue remains an open need. (neri2023understandingtheultrarare pages 7-9)

### 6.4 Suggested GO biological process terms (examples)
Based on mechanisms discussed:
* **Chromatin organization** and **negative regulation of transcription** (lin2011adultonsetautosomaldominant pages 1-2, neri2023understandingtheultrarare pages 6-7)
* **Myelination** / **oligodendrocyte differentiation** (neri2023understandingtheultrarare pages 4-6)
* **Lipid biosynthetic process** (myelin lipid synthesis dysregulation) (neri2023understandingtheultrarare pages 4-6)
* **mRNA splicing** (RAVER2/PTB axis) (neri2023understandingtheultrarare pages 7-9)

(GO IDs not explicitly provided in the sources; these are suggested mappings.)

### 6.5 Suggested Cell Ontology (CL) terms (examples)
Key implicated cell types include:
* **Oligodendrocytes** (myelin-producing CNS glia) (neri2023understandingtheultrarare pages 4-6, oranburg2023establishingmodelsystems pages 27-31)
* **Astrocytes** (LIF signaling and reactive changes) (neri2023understandingtheultrarare pages 7-9)
* **Neurons** (nuclear morphology and neurite phenotypes in models) (giorgio2019allelespecificsilencingas pages 20-23)

(CL IDs not explicitly provided; suggested mappings.)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
Primary: **central nervous system** white matter (brain and spinal cord), with prominent clinical contributions from autonomic pathways and long motor tracts. (ortiz2024aretrospectivereview pages 2-3, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7)

### 7.2 Tissue/cell level
Primary tissue: **CNS white matter** with demyelination; implicated cell types include **oligodendrocytes** (directly, via cell-specific overexpression models) and **astrocytes** (supportive signaling dysfunction). (neri2023understandingtheultrarare pages 4-6, neri2023understandingtheultrarare pages 6-7)

### 7.3 Subcellular
Core subcellular compartment implicated: **nuclear lamina / nuclear envelope** and its chromatin tethering domains. (lin2011adultonsetautosomaldominant pages 1-2)

### 7.4 Suggested UBERON terms (examples)
* **Brain white matter** and **spinal cord white matter** (ortiz2024aretrospectivereview pages 2-3, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)
* **Internal capsule** and **corpus callosum** (ortiz2024aretrospectivereview pages 2-3)
* **Cerebellar peduncles** (ortiz2024aretrospectivereview pages 2-3)

(UBERON IDs not explicitly provided; suggested mappings.)

---

## 8. Temporal development
### 8.1 Onset
Onset is typically **insidious in mid-adulthood** (often 4th–6th decade), with MRI abnormalities potentially preceding symptoms by a decade or more in some individuals. (ortiz2024aretrospectivereview pages 1-2, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7)

### 8.2 Progression and staging (data-supported milestones)
Longitudinal natural history in LMNB1-duplication families provides disability and survival estimates:
* EDSS 6 at mean age **59 ± 8** years, about **11 ± 5 years** from symptom onset.
* EDSS 8 at mean age **61 ± 6** years, about **14 ± 4 years** from onset.
* Deaths at mean age **66 ± 6** years, about **17 ± 6 years** from onset.
* Median survival after onset **18 years**.
(finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7, finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)

### 8.3 Remission/relapse patterns
A relapsing-remitting course is not typical; pseudoexacerbations with heat/infection can occur. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12)

---

## 9. Inheritance and population
### 9.1 Inheritance
Inheritance is **autosomal dominant**, consistent with structural variants that increase LMNB1 expression. (gosky2021assessmentanddevelopment pages 18-22, nmezi2019genomicdeletionsupstream pages 1-2)

### 9.2 Epidemiology
ADLD is **ultra-rare**; multiple sources state that **>30 families** have been reported worldwide and that **exact prevalence is unknown** due to rarity and diagnostic challenges. (neri2023understandingtheultrarare pages 1-2, ortiz2024aretrospectivereview pages 3-5)

Educational materials summarize older literature counts as “at least **24 families**” and “**>70 individuals**,” and emphasize likely underdiagnosis. (gosky2021assessmentanddevelopment pages 18-22)

No robust sex ratio, penetrance estimates, or population prevalence/incidence rates were identified in the retrieved excerpts. (ortiz2024aretrospectivereview pages 3-5)

---

## 10. Diagnostics
### 10.1 Clinical and imaging diagnostics
The practical, high-yield diagnostic pathway is:
1. Recognize the **adult-onset dysautonomia + spastic-ataxic syndrome**.
2. Identify the **characteristic symmetric MRI pattern**, including corticospinal tract involvement and cerebellar peduncle lesions; spine MRI may show cord thinning/atrophy.
3. Confirm with **LMNB1 duplication/deletion testing**, using methods that detect CNVs/structural variants.
(ortiz2024aretrospectivereview pages 3-5, muthusamy2023adultonsetleukodystrophiesa pages 10-11)

MRI details in a 2024 cohort: all reviewed MRIs showed **symmetric confluent deep cerebral and periventricular T2 hyperintensities** with involvement of **posterior limb internal capsule**, **corpus callosum**, **brainstem corticospinal tracts**, **superior/middle cerebellar peduncles**, and spine MRI showed **diffuse spinal cord atrophy**. (ortiz2024aretrospectivereview pages 1-2, ortiz2024aretrospectivereview pages 2-3)

### 10.2 Genetic testing strategy
A critical real-world point from 2023–2024 expert sources is that **routine short-read NGS may not reliably detect LMNB1 duplications/upstream deletions**, so the clinician must order CNV/structural-variant assays (e.g., deletion/duplication analysis, MLPA, gene-targeted microarray/array-CGH) when the phenotype/MRI are classic. (muthusamy2023adultonsetleukodystrophiesa pages 21-23, ortiz2024aretrospectivereview pages 3-5)

### 10.3 Differential diagnosis (key examples)
Because adult leukodystrophies overlap with MS and other acquired leukoencephalopathies, reviews emphasize first excluding acquired mimics and using imaging patterns/biochemical testing to distinguish inherited conditions. (muthusamy2023adultonsetleukodystrophiesa pages 23-24, muthusamy2023adultonsetleukodystrophiesa pages 21-23)

A 2023 practical guide explicitly highlights differentials and distinguishing tests, including AMN/X-ALD (VLCFA; spinal cord atrophy), AMACR deficiency (pristanic acid), CSF1R disease (calcifications on CT/gradient-echo), and emphasizes the LMNB1 ADLD MRI signature and CNV testing needs. (muthusamy2023adultonsetleukodystrophiesa pages 10-11)

---

## 11. Outcome / prognosis
ADLD is slowly progressive but ultimately severe, with a multi-decade course in many patients. Quantified outcomes include EDSS milestone timing and survival described above (Section 8). (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7)

Diagnostic delay is substantial in real-world practice: median **6 years** from symptom onset to diagnosis in one 2024 cohort. (ortiz2024aretrospectivereview pages 1-2)

---

## 12. Treatment
### 12.1 Current standard of care (real-world)
No established disease-modifying therapy was identified in the cited clinical literature; care is **supportive/symptomatic**, targeting dysautonomia (bladder and orthostatic intolerance), spasticity, mobility and functional decline, and cognitive/psychiatric symptoms. (ortiz2024aretrospectivereview pages 3-5, jiang2025casereportlmnb1 pages 4-5)

### 12.2 Experimental / emerging therapeutics
**LMNB1-lowering strategies** are the most mechanistically aligned targeted approaches:

1. **Allele-specific RNA interference (preclinical proof-of-concept).** In patient fibroblasts and disease-relevant cellular models, allele-specific siRNA/shRNA targeting a common LMNB1 3′UTR SNP (rs1051644) reduced LMNB1 expression toward physiologic levels and improved ADLD-associated cellular phenotypes. In directly reprogrammed neurons, allele-specific shRNA produced ~**30%** Lamin B1 protein reduction with improved nuclear anomalies and neurite growth. (giorgio2019allelespecificsilencingas pages 17-20, giorgio2019allelespecificsilencingas pages 20-23)

2. **Personalized antisense oligonucleotide (ASO) therapy clinical trial (single participant).** ClinicalTrials.gov lists an open-label phase 1/2 trial of a personalized ASO (nL-LMNB1-001) in a single participant with LMNB1-duplication ADLD (NCT06816498), started **2025-03-17**, ACTIVE_NOT_RECRUITING; endpoints include gait metrics (6-minute walk, 25-foot walk, motion analysis), neurological functioning, MRI brain atrophy, plus urodynamics and autonomic tests for secondary outcomes. (NCT06816498 chunk 1)

### 12.3 Suggested MAXO terms (examples)
Not explicitly provided in sources; suggested mappings include:
* Genetic counseling (autosomal dominant inheritance) (gosky2021assessmentanddevelopment pages 18-22)
* Symptomatic treatment of spasticity and autonomic dysfunction (jiang2025casereportlmnb1 pages 4-5)
* Antisense oligonucleotide therapy / RNA interference (investigational) (NCT06816498 chunk 1, giorgio2019allelespecificsilencingas pages 17-20)

---

## 13. Prevention
Primary prevention is not currently feasible because ADLD is a dominantly inherited genetic disorder. Prevention is best framed as:
* **Secondary prevention:** early recognition via MRI/clinical features and confirmatory genetic testing to reduce diagnostic delay and enable anticipatory management and trial eligibility. (ortiz2024aretrospectivereview pages 3-5, muthusamy2023adultonsetleukodystrophiesa pages 21-23)
* **Tertiary prevention:** management of complications (orthostatic hypotension, bladder dysfunction, spasticity) and supportive rehabilitation. (ortiz2024aretrospectivereview pages 2-3)

Genetic counseling is central given autosomal dominant inheritance and 50% transmission risk to offspring of an affected parent. (gosky2021assessmentanddevelopment pages 18-22)

---

## 14. Other species / natural disease
No naturally occurring veterinary ADLD analogs were identified in the retrieved evidence; the literature retrieved emphasizes engineered model systems rather than naturally occurring cross-species disease. (neri2023understandingtheultrarare pages 2-4)

---

## 15. Model organisms
Multiple model systems support mechanistic study and therapy development:
* **Transgenic mouse models** with oligodendrocyte-specific LMNB1 overexpression (Plp1 promoter; PLP-FLAG-LMNB1) recapitulate age-dependent white matter degeneration and motor dysfunction, supporting oligodendrocytes as key vulnerability points. (oranburg2023establishingmodelsystems pages 27-31, henck2024singlecellsequencing pages 26-29)
* **LMNB1BAC / PLP-LMNB1Tg mice** show age-dependent demyelination and neurological phenotypes (motor/cognitive/epileptic), summarized in the 2023 review. (neri2023understandingtheultrarare pages 2-4)
* **Human cellular models** include patient-derived fibroblasts and directly reprogrammed neurons used for mechanistic assays and proof-of-concept gene silencing. (giorgio2019allelespecificsilencingas pages 17-20)

Limitations emphasized across sources: cell-type specificity remains incompletely explained, mechanistic findings vary by model, and many molecular signatures require validation in patient CNS tissue. (neri2023understandingtheultrarare pages 2-4)

---

## Direct abstract quotes supporting key claims (from retrieved abstracts)
* 2024 cohort definition: “**LMNB1-related autosomal dominant leukodystrophy (ADLD) is a slowly progressive neurodegenerative disorder caused by overexpression of LMNB1.**” (ortiz2024aretrospectivereview pages 1-2)
* 2015 enhancer adoption mechanism: “**Chromosomal rearrangements with duplication of the lamin B1 (LMNB1) gene underlie autosomal dominant adult-onset demyelinating leukodystrophy (ADLD), a rare neurological disorder in which overexpression of LMNB1 causes progressive central nervous system demyelination.**” (giorgio2015alargegenomic pages 1-2)
* 2025 trial registry summary (ClinicalTrials.gov): describes “**Personalized Antisense Oligonucleotide Therapy for A Single Participant With LMNB1 Mutation Associated Autosomal Dominant Leukodystrophy (ADLD)**” with endpoints including gait testing and MRI atrophy measures. (NCT06816498 chunk 1)

---

## Notes on missing template elements
* **MONDO / Orphanet / ICD / MeSH codes:** not available in the retrieved excerpts; reporting them without evidence would require direct database querying not supported by the current tool evidence set. (neri2023understandingtheultrarare pages 1-2)
* **Variant-level HGVS nomenclature, ClinVar classifications, gnomAD allele frequencies:** not present in the retrieved excerpts; ADLD is primarily associated with structural variants (duplications/deletions) that often require specialized CNV assays and may not be represented uniformly in variant databases. (muthusamy2023adultonsetleukodystrophiesa pages 21-23)



References

1. (ortiz2024aretrospectivereview pages 1-2): Judit M. Perez Ortiz, Karthik Muthusamy, W. Oliver Tobin, Ralitza Gavrilova, Margot A. Cousin, and Radhika Dhamija. A retrospective review of lmnb1-related autosomal dominant leukodystrophy. Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1007/s44162-024-00055-w, doi:10.1007/s44162-024-00055-w. This article has 0 citations.

2. (neri2023understandingtheultrarare pages 1-2): Irene Neri, Giulia Ramazzotti, Sara Mongiorgi, Isabella Rusciano, Marianna Bugiani, Luciano Conti, Margot Cousin, Elisa Giorgio, Quasar S. Padiath, Giovanna Vaula, Pietro Cortelli, Lucia Manzoli, and Stefano Ratti. Understanding the ultra-rare disease autosomal dominant leukodystrophy: an updated review on morpho-functional alterations found in experimental models. Molecular Neurobiology, 60:6362-6372, Jul 2023. URL: https://doi.org/10.1007/s12035-023-03461-1, doi:10.1007/s12035-023-03461-1. This article has 16 citations and is from a peer-reviewed journal.

3. (ortiz2024aretrospectivereview pages 2-3): Judit M. Perez Ortiz, Karthik Muthusamy, W. Oliver Tobin, Ralitza Gavrilova, Margot A. Cousin, and Radhika Dhamija. A retrospective review of lmnb1-related autosomal dominant leukodystrophy. Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1007/s44162-024-00055-w, doi:10.1007/s44162-024-00055-w. This article has 0 citations.

4. (dai2017anlmnb1duplication pages 1-2): Yi Dai, Yaling Ma, Shengde Li, Santasree Banerjee, Shengran Liang, Qing Liu, Yinchang Yang, Bin Peng, Liying Cui, and Liri Jin. An lmnb1 duplication caused adult-onset autosomal dominant leukodystrophy in chinese family: clinical manifestations, neuroradiology and genetic diagnosis. Frontiers in Molecular Neuroscience, Jul 2017. URL: https://doi.org/10.3389/fnmol.2017.00215, doi:10.3389/fnmol.2017.00215. This article has 25 citations.

5. (lin2011adultonsetautosomaldominant pages 1-2): Shu-Ting Lin, Louis J. Ptáček, and Ying-Hui Fu. Adult-onset autosomal dominant leukodystrophy: linking nuclear envelope to myelin. The Journal of Neuroscience, 31:1163-1166, Jan 2011. URL: https://doi.org/10.1523/jneurosci.5994-10.2011, doi:10.1523/jneurosci.5994-10.2011. This article has 33 citations.

6. (giorgio2015alargegenomic pages 1-2): Elisa Giorgio, Daniel Robyr, Malte Spielmann, Enza Ferrero, Eleonora Di Gregorio, Daniele Imperiale, Giovanna Vaula, Georgios Stamoulis, Federico Santoni, Cristiana Atzori, Laura Gasparini, Denise Ferrera, Claudio Canale, Michel Guipponi, Len A. Pennacchio, Stylianos E. Antonarakis, Alessandro Brussino, and Alfredo Brusco. A large genomic deletion leads to enhancer adoption by the lamin b1 gene: a second path to autosomal dominant adult-onset demyelinating leukodystrophy (adld). Human Molecular Genetics, 24:3143-3154, Feb 2015. URL: https://doi.org/10.1093/hmg/ddv065, doi:10.1093/hmg/ddv065. This article has 178 citations and is from a domain leading peer-reviewed journal.

7. (nmezi2019genomicdeletionsupstream pages 1-2): Bruce Nmezi, Elisa Giorgio, Raili Raininko, Anna Lehman, Malte Spielmann, Mary Kay Koenig, Rahmat Adejumo, Melissa Knight, Ralitza Gavrilova, Murad Alturkustani, Manas Sharma, Robert Hammond, William A. Gahl, Camilo Toro, Alfredo Brusco, and Quasar S. Padiath. Genomic deletions upstream of lamin b1 lead to atypical autosomal dominant leukodystrophy. Neurology Genetics, Feb 2019. URL: https://doi.org/10.1212/nxg.0000000000000305, doi:10.1212/nxg.0000000000000305. This article has 31 citations.

8. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 1-2): Johannes Finnsson, Jimmy Sundblom, Niklas Dahl, Atle Melberg, and Raili Raininko. Lmnb1‐related autosomal‐dominant leukodystrophy: clinical and radiological course. Annals of Neurology, 78:412-425, Jul 2015. URL: https://doi.org/10.1002/ana.24452, doi:10.1002/ana.24452. This article has 61 citations and is from a highest quality peer-reviewed journal.

9. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 6-7): Johannes Finnsson, Jimmy Sundblom, Niklas Dahl, Atle Melberg, and Raili Raininko. Lmnb1‐related autosomal‐dominant leukodystrophy: clinical and radiological course. Annals of Neurology, 78:412-425, Jul 2015. URL: https://doi.org/10.1002/ana.24452, doi:10.1002/ana.24452. This article has 61 citations and is from a highest quality peer-reviewed journal.

10. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 9-12): Johannes Finnsson, Jimmy Sundblom, Niklas Dahl, Atle Melberg, and Raili Raininko. Lmnb1‐related autosomal‐dominant leukodystrophy: clinical and radiological course. Annals of Neurology, 78:412-425, Jul 2015. URL: https://doi.org/10.1002/ana.24452, doi:10.1002/ana.24452. This article has 61 citations and is from a highest quality peer-reviewed journal.

11. (finnsson2015lmnb1‐relatedautosomal‐dominantleukodystrophy pages 7-9): Johannes Finnsson, Jimmy Sundblom, Niklas Dahl, Atle Melberg, and Raili Raininko. Lmnb1‐related autosomal‐dominant leukodystrophy: clinical and radiological course. Annals of Neurology, 78:412-425, Jul 2015. URL: https://doi.org/10.1002/ana.24452, doi:10.1002/ana.24452. This article has 61 citations and is from a highest quality peer-reviewed journal.

12. (ortiz2024aretrospectivereview pages 3-5): Judit M. Perez Ortiz, Karthik Muthusamy, W. Oliver Tobin, Ralitza Gavrilova, Margot A. Cousin, and Radhika Dhamija. A retrospective review of lmnb1-related autosomal dominant leukodystrophy. Journal of Rare Diseases, Oct 2024. URL: https://doi.org/10.1007/s44162-024-00055-w, doi:10.1007/s44162-024-00055-w. This article has 0 citations.

13. (muthusamy2023adultonsetleukodystrophiesa pages 10-11): Karthik Muthusamy, Ajith Sivadasan, Luke Dixon, Sniya Sudhakar, Maya Thomas, Sumita Danda, Zbigniew K. Wszolek, Klaas Wierenga, Radhika Dhamija, and Ralitza Gavrilova. Adult-onset leukodystrophies: a practical guide, recent treatment updates, and future directions. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1219324, doi:10.3389/fneur.2023.1219324. This article has 30 citations and is from a peer-reviewed journal.

14. (muthusamy2023adultonsetleukodystrophiesa pages 23-24): Karthik Muthusamy, Ajith Sivadasan, Luke Dixon, Sniya Sudhakar, Maya Thomas, Sumita Danda, Zbigniew K. Wszolek, Klaas Wierenga, Radhika Dhamija, and Ralitza Gavrilova. Adult-onset leukodystrophies: a practical guide, recent treatment updates, and future directions. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1219324, doi:10.3389/fneur.2023.1219324. This article has 30 citations and is from a peer-reviewed journal.

15. (muthusamy2023adultonsetleukodystrophiesa pages 21-23): Karthik Muthusamy, Ajith Sivadasan, Luke Dixon, Sniya Sudhakar, Maya Thomas, Sumita Danda, Zbigniew K. Wszolek, Klaas Wierenga, Radhika Dhamija, and Ralitza Gavrilova. Adult-onset leukodystrophies: a practical guide, recent treatment updates, and future directions. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1219324, doi:10.3389/fneur.2023.1219324. This article has 30 citations and is from a peer-reviewed journal.

16. (muthusamy2023adultonsetleukodystrophiesa pages 1-2): Karthik Muthusamy, Ajith Sivadasan, Luke Dixon, Sniya Sudhakar, Maya Thomas, Sumita Danda, Zbigniew K. Wszolek, Klaas Wierenga, Radhika Dhamija, and Ralitza Gavrilova. Adult-onset leukodystrophies: a practical guide, recent treatment updates, and future directions. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1219324, doi:10.3389/fneur.2023.1219324. This article has 30 citations and is from a peer-reviewed journal.

17. (kohler2018adulthoodleukodystrophies pages 3-4): Wolfgang Köhler, Julian Curiel, and Adeline Vanderver. Adulthood leukodystrophies. Nature Reviews Neurology, 14:94-105, Jan 2018. URL: https://doi.org/10.1038/nrneurol.2017.175, doi:10.1038/nrneurol.2017.175. This article has 169 citations and is from a highest quality peer-reviewed journal.

18. (resende2019adultleukodystrophiesa pages 1-2): Lucas Lopes Resende, Anderson Rodrigues Brandão de Paiva, Fernando Kok, Claudia da Costa Leite, and Leandro Tavares Lucato. Adult leukodystrophies: a step-by-step diagnostic approach. Radiographics : a review publication of the Radiological Society of North America, Inc, 39 1:153-168, Jan 2019. URL: https://doi.org/10.1148/rg.2019180081, doi:10.1148/rg.2019180081. This article has 93 citations.

19. (lynch2019practicalapproachto pages 2-3): David S Lynch, Charles Wade, Anderson Rodrigues Brandão de Paiva, Nevin John, Justin A Kinsella, Áine Merwick, Rebekah M Ahmed, Jason D Warren, Catherine J Mummery, Jonathan M Schott, Nick C Fox, Henry Houlden, Matthew E Adams, Indran Davagnanam, Elaine Murphy, and Jeremy Chataway. Practical approach to the diagnosis of adult-onset leukodystrophies: an updated guide in the genomic era. Journal of Neurology, Neurosurgery, and Psychiatry, 90:543-554, Nov 2019. URL: https://doi.org/10.1136/jnnp-2018-319481, doi:10.1136/jnnp-2018-319481. This article has 152 citations.

20. (jiang2025casereportlmnb1 pages 4-5): Yumeng Jiang, Lu Han, Yaqi Li, Zhihong Zhao, Zikai Xin, and Zilong Zhu. Case report: lmnb1 duplication-mediated autosomal dominant adult leukodystrophy in a chinese family and literature review of chinese patients. Frontiers in Neuroscience, Feb 2025. URL: https://doi.org/10.3389/fnins.2025.1531593, doi:10.3389/fnins.2025.1531593. This article has 0 citations and is from a peer-reviewed journal.

21. (giorgio2019allelespecificsilencingas pages 1-6): Elisa Giorgio, Martina Lorenzati, Pia Rivetti di Val Cervo, Alessandro Brussino, Manuel Cernigoj, Edoardo Della Sala, Anna Bartoletti Stella, Marta Ferrero, Massimiliano Caiazzo, Sabina Capellari, Pietro Cortelli, Luciano Conti, Elena Cattaneo, Annalisa Buffo, and Alfredo Brusco. Allele-specific silencing as treatment for gene duplication disorders: proof-of-principle in autosomal dominant leukodystrophy. Brain : a journal of neurology, 142:1905-1920, May 2019. URL: https://doi.org/10.1093/brain/awz139, doi:10.1093/brain/awz139. This article has 26 citations.

22. (giorgio2019allelespecificsilencingas pages 6-10): Elisa Giorgio, Martina Lorenzati, Pia Rivetti di Val Cervo, Alessandro Brussino, Manuel Cernigoj, Edoardo Della Sala, Anna Bartoletti Stella, Marta Ferrero, Massimiliano Caiazzo, Sabina Capellari, Pietro Cortelli, Luciano Conti, Elena Cattaneo, Annalisa Buffo, and Alfredo Brusco. Allele-specific silencing as treatment for gene duplication disorders: proof-of-principle in autosomal dominant leukodystrophy. Brain : a journal of neurology, 142:1905-1920, May 2019. URL: https://doi.org/10.1093/brain/awz139, doi:10.1093/brain/awz139. This article has 26 citations.

23. (giorgio2019allelespecificsilencingas pages 17-20): Elisa Giorgio, Martina Lorenzati, Pia Rivetti di Val Cervo, Alessandro Brussino, Manuel Cernigoj, Edoardo Della Sala, Anna Bartoletti Stella, Marta Ferrero, Massimiliano Caiazzo, Sabina Capellari, Pietro Cortelli, Luciano Conti, Elena Cattaneo, Annalisa Buffo, and Alfredo Brusco. Allele-specific silencing as treatment for gene duplication disorders: proof-of-principle in autosomal dominant leukodystrophy. Brain : a journal of neurology, 142:1905-1920, May 2019. URL: https://doi.org/10.1093/brain/awz139, doi:10.1093/brain/awz139. This article has 26 citations.

24. (giorgio2019allelespecificsilencingas pages 20-23): Elisa Giorgio, Martina Lorenzati, Pia Rivetti di Val Cervo, Alessandro Brussino, Manuel Cernigoj, Edoardo Della Sala, Anna Bartoletti Stella, Marta Ferrero, Massimiliano Caiazzo, Sabina Capellari, Pietro Cortelli, Luciano Conti, Elena Cattaneo, Annalisa Buffo, and Alfredo Brusco. Allele-specific silencing as treatment for gene duplication disorders: proof-of-principle in autosomal dominant leukodystrophy. Brain : a journal of neurology, 142:1905-1920, May 2019. URL: https://doi.org/10.1093/brain/awz139, doi:10.1093/brain/awz139. This article has 26 citations.

25. (NCT06816498 chunk 1):  Personalized Antisense Oligonucleotide Therapy for A Single Participant With LMNB1 Mutation Associated Autosomal Dominant Leukodystrophy (ADLD). n-Lorem Foundation. 2025. ClinicalTrials.gov Identifier: NCT06816498

26. (santos2012adultonsetautosomaldominant pages 3-3): Michael M. Dos Santos, Caspar Grond-Ginsbach, Suna Su Aksay, Bowang Chen, Sandrine Tchatchou, Nicole I. Wolf, Marjo S. Knaap, and Armin J. Grau. Adult-onset autosomal dominant leukodystrophy due to lmnb1 gene duplication. Journal of Neurology, 259:579-581, Mar 2012. URL: https://doi.org/10.1007/s00415-011-6225-4, doi:10.1007/s00415-011-6225-4. This article has 37 citations and is from a domain leading peer-reviewed journal.

27. (gosky2021assessmentanddevelopment pages 92-96): MD Gosky. Assessment and development of online educational materials for autosomal dominant leukodystrophy. Unknown journal, 2021.

28. (neri2023understandingtheultrarare pages 4-6): Irene Neri, Giulia Ramazzotti, Sara Mongiorgi, Isabella Rusciano, Marianna Bugiani, Luciano Conti, Margot Cousin, Elisa Giorgio, Quasar S. Padiath, Giovanna Vaula, Pietro Cortelli, Lucia Manzoli, and Stefano Ratti. Understanding the ultra-rare disease autosomal dominant leukodystrophy: an updated review on morpho-functional alterations found in experimental models. Molecular Neurobiology, 60:6362-6372, Jul 2023. URL: https://doi.org/10.1007/s12035-023-03461-1, doi:10.1007/s12035-023-03461-1. This article has 16 citations and is from a peer-reviewed journal.

29. (neri2023understandingtheultrarare pages 6-7): Irene Neri, Giulia Ramazzotti, Sara Mongiorgi, Isabella Rusciano, Marianna Bugiani, Luciano Conti, Margot Cousin, Elisa Giorgio, Quasar S. Padiath, Giovanna Vaula, Pietro Cortelli, Lucia Manzoli, and Stefano Ratti. Understanding the ultra-rare disease autosomal dominant leukodystrophy: an updated review on morpho-functional alterations found in experimental models. Molecular Neurobiology, 60:6362-6372, Jul 2023. URL: https://doi.org/10.1007/s12035-023-03461-1, doi:10.1007/s12035-023-03461-1. This article has 16 citations and is from a peer-reviewed journal.

30. (neri2023understandingtheultrarare pages 2-4): Irene Neri, Giulia Ramazzotti, Sara Mongiorgi, Isabella Rusciano, Marianna Bugiani, Luciano Conti, Margot Cousin, Elisa Giorgio, Quasar S. Padiath, Giovanna Vaula, Pietro Cortelli, Lucia Manzoli, and Stefano Ratti. Understanding the ultra-rare disease autosomal dominant leukodystrophy: an updated review on morpho-functional alterations found in experimental models. Molecular Neurobiology, 60:6362-6372, Jul 2023. URL: https://doi.org/10.1007/s12035-023-03461-1, doi:10.1007/s12035-023-03461-1. This article has 16 citations and is from a peer-reviewed journal.

31. (neri2023understandingtheultrarare pages 7-9): Irene Neri, Giulia Ramazzotti, Sara Mongiorgi, Isabella Rusciano, Marianna Bugiani, Luciano Conti, Margot Cousin, Elisa Giorgio, Quasar S. Padiath, Giovanna Vaula, Pietro Cortelli, Lucia Manzoli, and Stefano Ratti. Understanding the ultra-rare disease autosomal dominant leukodystrophy: an updated review on morpho-functional alterations found in experimental models. Molecular Neurobiology, 60:6362-6372, Jul 2023. URL: https://doi.org/10.1007/s12035-023-03461-1, doi:10.1007/s12035-023-03461-1. This article has 16 citations and is from a peer-reviewed journal.

32. (oranburg2023establishingmodelsystems pages 27-31): TDF Oranburg. Establishing model systems to study mechanisms of cell specificity in autosomal dominant leukodystrophy. Unknown journal, 2023.

33. (gosky2021assessmentanddevelopment pages 18-22): MD Gosky. Assessment and development of online educational materials for autosomal dominant leukodystrophy. Unknown journal, 2021.

34. (henck2024singlecellsequencing pages 26-29): Jana Henck. Single cell sequencing as a phenotyping strategy to decipher the molecular mechanisms of developmental disorders. Text, Jan 2024. URL: https://doi.org/10.17169/refubium-43507, doi:10.17169/refubium-43507. This article has 0 citations and is from a peer-reviewed journal.