---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T11:05:59.407450'
end_time: '2026-05-10T11:17:15.413079'
duration_seconds: 676.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acoustic Neuroma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acoustic Neuroma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Acoustic Neuroma** covering all of the
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
- **Disease Name:** Acoustic Neuroma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Acoustic Neuroma** covering all of the
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


# Acoustic Neuroma (Vestibular Schwannoma) — Disease Characteristics Research Report (Neoplastic)

**Scope note:** This report synthesizes only the evidence retrieved with the provided tools in this run. Some standard ontology identifiers (e.g., MONDO, MeSH, ICD-10/ICD-11, OMIM, Orphanet) are not present in the retrieved sources, so they are flagged as *not available from the current evidence corpus*.

## 1. Disease Information

### 1.1 Overview (current understanding)
**Acoustic neuroma** is the common clinical name for **vestibular schwannoma (VS)**, a **benign Schwann-cell tumor** that arises on the **vestibulocochlear nerve (cranial nerve VIII)**, typically in the cerebellopontine angle/internal auditory canal region, and can cause hearing loss, tinnitus, and balance symptoms. (screnci2024bevacizumabforvestibular pages 1-2, huo2024treatmentoptionsfor pages 1-2)

**Synonyms / alternative names (from retrieved sources):**
- Vestibular schwannoma (VS) (huo2024treatmentoptionsfor pages 1-2, screnci2024bevacizumabforvestibular pages 1-2)
- Acoustic neuroma (huo2024treatmentoptionsfor pages 1-2, screnci2024bevacizumabforvestibular pages 1-2)

### 1.2 Key identifiers
- **MONDO ID:** not available from retrieved sources.
- **MeSH / ICD-10 / ICD-11 / OMIM / Orphanet:** not available from retrieved sources.

### 1.3 Evidence source type
The information below is derived from:
- **Aggregated disease-level resources**: systematic reviews/meta-analyses and reviews (e.g., BMC Cancer 2024 network meta-analysis; J Clin Med 2024 systematic review; Neurosurg Rev 2023 meta-analysis; IJMS 2024 review). (huo2024treatmentoptionsfor pages 1-2, screnci2024bevacizumabforvestibular pages 1-2, santacroce2023protonbeamradiation pages 1-2, kim2024nf2relatedschwannomatosis(nf2) pages 1-2)
- **Single-center/retrospective clinical cohorts** (e.g., an 88-patient Indonesian series). (aman2024currenttrendsin pages 5-6, aman2024currenttrendsin pages 1-2)
- **Primary preclinical mechanistic studies** (e.g., Brain 2023 Hippo/TEAD targeting). (laraba2023inhibitionofyaptazdriven pages 1-2)

## 2. Etiology

### 2.1 Disease causal factors
**Genetic/mechanistic (core driver): NF2 loss (merlin deficiency).** Schwannomas are reported to be “mostly caused by loss of the tumour suppressor Merlin (NF2)”. (laraba2023inhibitionofyaptazdriven pages 1-2)

**Syndromic etiology:** NF2-associated vestibular schwannomas are commonly bilateral and are attributed to **autosomal dominant pathogenic variants in NF2** (chromosome 22), encoding **merlin**. (screnci2024bevacizumabforvestibular pages 1-2, kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

### 2.2 Risk factors
**NF2-related schwannomatosis (genetic) risk:**
- NF2-related schwannomatosis prevalence and inheritance features are summarized in the 2024 review: autosomal dominant; approximately half inherited; among de novo cases, **25–50% mosaicism**. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

**Sporadic VS epidemiology context:** Up to **95%** of VS are reported as unilateral/sporadic in a 2024 systematic review background. (king2024vestibularschwannomaand pages 1-2)

**Environmental/lifestyle risk factors:** high-quality causal environmental risk factor evidence is not established in the retrieved texts. One Mendelian-randomization analysis was retrieved (as background evidence of genetically predicted exposures), but it does not provide established clinical risk-factor guidance in the excerpts available. ( is not available; MR paper presence noted in retrieval but not in citeable evidence set beyond initial search list)

### 2.3 Protective factors
No clinically established protective factors with quantitative effects were available in the retrieved excerpts for VS specifically.

### 2.4 Gene–environment interaction
No gene–environment interaction results were available in the retrieved excerpts.

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with characteristics and frequencies)
**Typical symptom domains** include hearing loss, tinnitus, and vestibular symptoms; larger tumors can produce hydrocephalus/brainstem compression and cranial neuropathies. (huo2024treatmentoptionsfor pages 1-2)

**Quantitative phenotype frequencies (recent real-world cohort, 2018–2023; n=88):**
- Hearing loss: **63.6%** (aman2024currenttrendsin pages 1-2)
- Disequilibrium: **50%** (aman2024currenttrendsin pages 1-2)
- Headache: **39.7%** (aman2024currenttrendsin pages 1-2)

**Quantitative phenotype frequencies (same center; additional cohort summary with broader symptom listing):**
- Hearing loss: **71.5%**
- Disequilibrium: **50%**
- Headache: **39.7%**
- Tinnitus: **25%**
- Facial nerve palsy: **25%**
- Trigeminal deficits: **20.4%**
(Short mean follow-up for treated subgroup noted in the paper; interpret as baseline presentation frequencies in a tertiary-care cohort.) (aman2024currenttrendsin pages 5-6)

**Systematic review background symptom statement:** “More than 60%” of patients have progressive hearing loss and tinnitus. (huo2024treatmentoptionsfor pages 1-2)

### 3.2 Quality of life impact
Tinnitus is repeatedly emphasized as distressing and QoL-limiting. In a 2024 systematic review on tinnitus outcomes, **36.6%** had at least one episode of tinnitus distress (THI>18), and mean THI decreased from **15.8 preoperatively** to **10.1 postoperatively** at mean follow-up ~**34.7 months**. (king2024vestibularschwannomaand pages 4-5)

### 3.3 HPO term suggestions (phenotype normalization)
Suggested HPO terms (as a starting mapping set; confirm exact term IDs in HPO browser during curation):
- Hearing loss: **HP:0000365** (aman2024currenttrendsin pages 5-6)
- Tinnitus: **HP:0000360** (aman2024currenttrendsin pages 5-6)
- Vertigo/disequilibrium/dizziness: **HP:0002321 / HP:0002329** (aman2024currenttrendsin pages 5-6)
- Headache: **HP:0002315** (aman2024currenttrendsin pages 5-6)
- Facial palsy/weakness: **HP:0000490** (aman2024currenttrendsin pages 5-6)
- Trigeminal sensory deficit/facial numbness: **HP:0003407** (aman2024currenttrendsin pages 5-6)

## 4. Genetic/Molecular Information

### 4.1 Causal genes
**NF2 (merlin)** is the core tumor suppressor gene implicated in NF2-related disease and in schwannoma biology; the 2024 NF2 review places NF2 at **22q12.2**. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

### 4.2 Molecular pathways and cellular processes (current understanding)
**Merlin function and loss-of-function consequences:** merlin is described as a FERM-domain membrane–cytoskeleton scaffolding tumor suppressor (enriched in Schwann cells/adherens junctions) integrating signals controlling proliferation and motility; its loss promotes tumorigenesis. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

**Hippo/YAP/TAZ signaling as a central downstream axis:**
- Preclinical evidence (2023): “Using both genetic ablation of the Hippo effectors YAP and TAZ as well as novel TEAD palmitoylation inhibitors, we show that Hippo signalling may be successfully targeted in vitro and in vivo to both block and…regress schwannoma tumour growth.” (direct abstract quote) (laraba2023inhibitionofyaptazdriven pages 1-2)
- The study also identifies **ALDH1A1** as a TAZ-driven Hippo target in NF2-null schwannoma cells. (laraba2023inhibitionofyaptazdriven pages 1-2)

**Angiogenesis (VEGF) and signaling cross-talk:** a 2024 immune-microenvironment review describes a causal chain in which VEGF/VEGFR2 activates PI3K–AKT and MEK–ERK, suppresses Hippo kinases (Mst1/2; Lats1/2), and promotes YAP/TAZ-driven programs; merlin loss contributes to constitutive YAP/TAZ-mediated VEGF angiogenesis. (jones2024deconvolvingtheimmunea pages 35-39)

**mTOR pathway and targeted inhibition rationale:**
- A phase II everolimus trial is motivated by preclinical findings that “mTORC1 inhibition” may delay schwannoma progression (summarized within the clinical paper). (nghiemphu2024imagingasan pages 1-2)

### 4.3 Epigenetics / multi-omics
No quantitative epigenetic methylation signatures or multi-omics datasets for VS were extractable from the retrieved excerpts, although mechanistic reviews discuss pathway-level regulation and emerging molecular therapies. (kim2024nf2relatedschwannomatosis(nf2) pages 6-7, kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

### 4.4 GO and CL term suggestions (mechanism annotation)
Proposed GO biological process terms for curation (validate with GO browser):
- Hippo signaling: **GO:0035329** (Hippo signaling)
- Regulation of cell proliferation: **GO:0042127**
- Angiogenesis: **GO:0001525**
- PI3K signaling: **GO:0014065** (phosphatidylinositol 3-kinase signaling)
- mTOR signaling: **GO:0031929** (TOR signaling)

Proposed CL cell types:
- Schwann cell: **CL:0000218** (primary tumor lineage)

## 5. Environmental Information

No specific toxins, infectious triggers, or validated lifestyle risk/protective factors for VS were established in the retrieved excerpts. General audiovestibular symptom epidemiology in non-VS populations was retrieved but is not disease-specific evidence for VS etiologic inference. ( not citeable; not in evidence set)

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (integrated model)
1) **Initiating event:** NF2/merlin loss (germline/mosaic in NF2-related schwannomatosis; somatic in sporadic schwannoma) in Schwann lineage. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2, laraba2023inhibitionofyaptazdriven pages 1-2)
2) **Pathway dysregulation:** derepression of Hippo effector activity (YAP/TAZ → TEAD transcriptional programs) and coupling to proliferative and angiogenic signaling (VEGF/VEGFR2 → PI3K/AKT, MEK/ERK; suppression of Hippo core kinases). (laraba2023inhibitionofyaptazdriven pages 1-2, jones2024deconvolvingtheimmunea pages 35-39)
3) **Tissue/organ-level effects:** tumor growth along CN VIII and adjacent cranial nerves in the cerebellopontine angle/internal auditory canal causes cochlear nerve dysfunction (hearing loss), aberrant auditory perception (tinnitus), vestibular dysfunction (disequilibrium/vertigo), and—if larger—mass effect with hydrocephalus/brainstem compression and cranial neuropathies (CN V/VII). (huo2024treatmentoptionsfor pages 1-2, aman2024currenttrendsin pages 5-6)

### 6.2 Upstream vs downstream
- **Upstream:** merlin loss (NF2), VEGF/VEGFR2 activation, TGFβ axis changes (TGFβR2 loss/TGFβR1 upregulation described in review). (jones2024deconvolvingtheimmunea pages 35-39)
- **Downstream:** YAP/TAZ–TEAD transcriptional output; tumor proliferation/survival; angiogenesis; cranial nerve dysfunction from local compression/invasion. (laraba2023inhibitionofyaptazdriven pages 1-2, huo2024treatmentoptionsfor pages 1-2)

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- **Primary site:** vestibulocochlear nerve (CN VIII) / cerebellopontine angle region. (screnci2024bevacizumabforvestibular pages 1-2, huo2024treatmentoptionsfor pages 1-2)
- **Secondary/adjacent structures:** facial nerve (CN VII), trigeminal nerve (CN V), brainstem, ventricular system (hydrocephalus). (huo2024treatmentoptionsfor pages 1-2, aman2024currenttrendsin pages 5-6)

### 7.2 UBERON suggestions
- Vestibulocochlear nerve (UBERON term to be confirmed in ontology browser)
- Cerebellopontine angle (UBERON term to be confirmed)

### 7.3 Lateralization
Most cases are unilateral/sporadic, while NF2-associated disease is commonly bilateral. (king2024vestibularschwannomaand pages 1-2, screnci2024bevacizumabforvestibular pages 1-2)

## 8. Temporal Development

### 8.1 Onset and progression
VS is described as a slowly growing benign tumor with clinical impact evolving as auditory/vestibular symptoms and, for larger tumors, mass effect. (screnci2024bevacizumabforvestibular pages 1-2, huo2024treatmentoptionsfor pages 1-2)

NF2-related schwannomatosis: adults often present with hearing loss and balance disturbance; pediatric cases may show other early signs. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

### 8.2 Staging / grading
A management review excerpt references use of Koos grading (I–IV) for tumor-size-based decision making (not fully detailed in the excerpt). (jones2024deconvolvingtheimmunea pages 35-39)

## 9. Inheritance and Population

### 9.1 Epidemiology (VS)
- VS reported as ~**8% of intracranial tumors** and most common cerebellopontine angle tumor. (huo2024treatmentoptionsfor pages 1-2)
- Reported annual incidence **10.4 per 100,000** (in background of 2024 network meta-analysis). (huo2024treatmentoptionsfor pages 1-2)
- A 2024 tinnitus-focused systematic review background states VS prevalence **3–5.2 per 100,000 person-years**, and **up to 95%** are unilateral/sporadic. (king2024vestibularschwannomaand pages 1-2)

### 9.2 NF2-related schwannomatosis (inheritance)
- **Autosomal dominant**, caused by germline or mosaic NF2 variants (22q12.2). (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)
- **Prevalence** ~**1:50,000**; **birth incidence** ~**1:28,000**. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)
- ~50% inherited; among de novo, **25–50%** mosaicism. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

## 10. Diagnostics

### 10.1 Imaging
- A 2024 AI-in-AN systematic review states **CT and MRI are preferred imaging modalities**; gadolinium contrast improves visualization; typical MRI signal characteristics are described (T1 iso/hypointense; heterogeneous hyperintense T2). (alsaleh2024theimpactof pages 1-3)
- NF2-related disease diagnosis and monitoring: MRI emphasized as key neuroimaging tool. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

### 10.2 Audiology and electrophysiology
- Hearing outcomes and monitoring often use **pure-tone audiometry (PTA)** and **word recognition score (WRS)**; one NF2 bevacizumab series pre-specified hearing change as ≥10% WRS or ≥10 dB PTA thresholds. (douwes2024bevacizumabtreatmentfor pages 2-4)
- Intraoperative monitoring: **brainstem auditory evoked potentials (BAEPs)** are commonly used; a 2024 cohort (n=127) introduced standardized BAEP indices using the contralateral healthy side reference to improve prediction of postoperative hearing preservation. ( not citeable; not in current evidence set)

### 10.3 Emerging/real-world implementations (2023–2024)
- AI applications: models for segmentation, volume estimation, radiomics, decision support, QoL evaluation, and treatment planning are being developed, but standardization and external validation remain key needs. (alsaleh2024theimpactof pages 1-3)

### 10.4 Differential diagnosis
Not systematically extractable from the current evidence excerpts.

## 11. Outcome / Prognosis

### 11.1 Treatment-associated functional outcomes (hearing)
- **Long-term serviceable hearing after SRS**: pooled **18.1% at 10 years** (wide CI). (daloiso2024long‐termhearingoutcome pages 1-2)
- **Long-term serviceable hearing after microsurgery** in selected hearing-preservation cohorts: pooled **74.5% at 10 years**. (daloiso2024long‐termhearingoutcome pages 1-2)

### 11.2 Morbidity/QoL
Tinnitus distress burden and its improvement after interventions have been quantified by THI changes in recent systematic review data. (king2024vestibularschwannomaand pages 4-5)

## 12. Treatment

### 12.1 Treatment strategy (current practice)
A 2024 network meta-analysis frames VS management options as:
- **Observation**
- **Microsurgery (MS)**
- **Radiotherapy**, including **SRS** and fractionated stereotactic radiotherapy (FSRT/ConFSRT)
(PQ evidence indicates decision-making depends on tumor size, symptoms, and preference.) (huo2024treatmentoptionsfor pages 1-2)

### 12.2 Radiotherapy/radiosurgery outcomes
- **CyberKnife radiosurgery hearing preservation:** pooled **68%** (95% CI 59–76%) at mean follow-up **~43 months** among patients with serviceable hearing pre-treatment (systematic review of 13 studies/493 participants). (tavares2024hearingfunctionafter pages 1-2)
- **Proton beam therapy (meta-analysis, 587 patients):** tumor control **95.4%**, progression **4.6%**, facial nerve preservation **93.7%**, hearing preservation **40.6%**, shunt for hydrocephalus **1.4%**. (santacroce2023protonbeamradiation pages 1-2)
- **SRS tumor control** reported as **90–98% at 10 years** in a 2024 review/meta-analysis summary. (pontillo2024hearingpreservationsurgery pages 1-2)

### 12.3 Surgery outcomes
- Reported broadly as <25% hearing preservation overall in a 2024 hearing-preservation surgery meta-analysis summary (noting heterogeneity and limitations), while SRT ~50% (long-term SRT data limited). (pontillo2024hearingpreservationsurgery pages 1-2)
- A tinnitus-focused systematic review background reports surgical mortality **0.38%** and overall complication rate **5.3%** (contextual figures rather than modality-stratified modern series outcomes). (king2024vestibularschwannomaand pages 1-2)

### 12.4 Pharmacotherapy / targeted therapy (NF2-related VS)
**Bevacizumab (anti-VEGF; off-label use in NF2-related VS):**
- Systematic review (9 studies; n=176): tumor volume reduction ≥20% **40%**, stabilization **50%**, progression **10%**; hearing improvement **36%**, stabilization **46%**, deterioration **18%**; severe adverse events **13%**. (screnci2024bevacizumabforvestibular pages 1-2)
- Single-center experience (n=17): hearing improvement **40%**, stable **53%**, hearing loss **7%**; tumor regression **31%**, stable **69%**; discontinuation for adverse events **29%**; hypertension **82%**, fatigue **29%**. (douwes2024bevacizumabtreatmentfor pages 13-14)

**Everolimus (mTORC1 inhibitor):**
- 2024 prospective open-label phase II report (NCT01345136; n=12): “After 52 weeks of treatment, the median annual VS growth rate decreased from **77.2%** at baseline to **29.4%**.” (direct abstract quote) There was **no radiographic response**, and **3/8 (37.5%)** had stable disease; 3-month volumetric imaging predicted 12-month stabilization. (nghiemphu2024imagingasan pages 1-2)
- ClinicalTrials.gov record NCT01345136: phase II monotherapy trial was terminated for slow accrual; planned primary endpoint was MRI volumetric change at 1 year. (NCT01345136 chunk 1)

**Other targeted agents (systematic review through Oct 2022):**
- Lapatinib: hearing response **31% (4/13)**; radiographic response **6% (1/17)**; median TTP ~**14 months**. (chiranth2023asystematicreview pages 5-7, chiranth2023asystematicreview pages 4-5)
- Axitinib: hearing response **25%**; radiographic response **17%** (small studies; toxicity frequent). (chiranth2023asystematicreview pages 4-5)

### 12.5 Experimental / translational directions (2023–2024)
- **Hippo/TEAD inhibition as a candidate strategy:** TEAD palmitoylation inhibitors and YAP/TAZ genetic ablation regressed NF2-null schwannoma growth in preclinical models (positioned as a route toward future clinical translation). (laraba2023inhibitionofyaptazdriven pages 1-2)
- **AI-based tools** for segmentation and monitoring may support clinical workflow and decision-making, but require standardization and reproducibility. (alsaleh2024theimpactof pages 1-3)

### 12.6 MAXO term suggestions (treatment normalization)
Suggested MAXO mappings (confirm in MAXO browser):
- Microsurgical resection of tumor
- Stereotactic radiosurgery
- Fractionated stereotactic radiotherapy
- Proton beam therapy
- Anti-VEGF monoclonal antibody therapy (bevacizumab)
- mTOR inhibitor therapy (everolimus)
- Cochlear implantation (as rehabilitative hearing restoration; referenced as improving QoL outcomes in VS management literature, though quantitative CI outcomes were not extractable in the excerpts here) ( not citeable)

## 13. Prevention

### 13.1 Primary prevention
No primary prevention measures (e.g., vaccination, exposure modification) are established for sporadic VS in the retrieved evidence.

### 13.2 Secondary prevention / early detection
- For NF2-associated disease, proactive MRI screening is recommended/used in registry contexts (mentioned in systematic review). (screnci2024bevacizumabforvestibular pages 1-2)

### 13.3 Genetic counseling
NF2-related schwannomatosis is autosomal dominant with mosaicism common in de novo cases, supporting family counseling and tailored genetic testing strategies (details beyond this were not extractable from retrieved excerpts). (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)

## 14. Other Species / Natural Disease
Not available from the retrieved evidence.

## 15. Model Organisms
- A 2023 primary study used mouse models (Periostin-Cre NF2fl/fl) and human primary schwannoma cells to test Hippo/TEAD targeting. (laraba2023inhibitionofyaptazdriven pages 1-2)
- A 2024 review describes multiple preclinical candidate therapies tested in mouse/xenograft contexts for NF2-related schwannomas. (kim2024nf2relatedschwannomatosis(nf2) pages 6-7)

## Structured summary artifact
The following table consolidates key identifiers, symptom frequencies, molecular mechanisms, diagnostics, treatments, outcomes statistics, and trial IDs from the retrieved evidence.

| Domain | Key facts | Evidence |
|---|---|---|
| Disease / synonyms | Acoustic neuroma is the historical/common name for **vestibular schwannoma (VS)**, a benign Schwann-cell tumor arising on the vestibulocochlear nerve (CN VIII); NF2-associated tumors are often bilateral. | (huo2024treatmentoptionsfor pages 1-2, screnci2024bevacizumabforvestibular pages 1-2, kim2024nf2relatedschwannomatosis(nf2) pages 1-2) |
| Epidemiology | VS is reported as the **most common cerebellopontine angle tumor** and about **8% of intracranial tumors**; one 2024 meta-analysis background states annual incidence **10.4/100,000**. Another 2024 review notes VS prevalence **3–5.2 per 100,000 person-years** and that **up to 95%** are unilateral/sporadic. | (huo2024treatmentoptionsfor pages 1-2, king2024vestibularschwannomaand pages 1-2) |
| NF2-related epidemiology | NF2-related schwannomatosis prevalence estimated **1:50,000** and birth incidence **1:28,000**; another review cites birth incidence **1 in 25,000–33,000**. NF2 accounts for about **~7% of VS cases**. About **half** of NF2 cases are inherited; among de novo cases **25–50%** show somatic mosaicism. | (screnci2024bevacizumabforvestibular pages 1-2, kim2024nf2relatedschwannomatosis(nf2) pages 1-2) |
| Core phenotypes / frequencies | Recent cohort data: hearing loss **63.6%** (or **71.5%** in another cohort summary), disequilibrium **50%**, headache **39.7%**, tinnitus **25%**, facial palsy **25%**, trigeminal deficits **20.4%**. Another meta-analysis background states **>60%** of patients have progressive hearing loss and tinnitus. | (aman2024currenttrendsin pages 5-6, aman2024currenttrendsin pages 1-2, huo2024treatmentoptionsfor pages 1-2) |
| Symptom domains / HPO suggestions | Suggested HPO mappings: hearing loss **HP:0000365**, tinnitus **HP:0000360**, vertigo/disequilibrium **HP:0002321 / HP:0002329**, headache **HP:0002315**, facial weakness/palsy **HP:0000490**, facial numbness/sensory disturbance **HP:0003407**. | (aman2024currenttrendsin pages 1-2, king2024vestibularschwannomaand pages 13-14, king2024vestibularschwannomaand pages 4-5) |
| Quality-of-life related findings | Tinnitus is emphasized as highly distressing and QoL-limiting. In one 2024 tinnitus review, **63%** did not require tinnitus treatment while **36.6%** had at least one episode of tinnitus distress; mean THI fell from **15.8 pre-op** to **10.1 post-op** at mean follow-up **~34.7 months**. | (king2024vestibularschwannomaand pages 1-2, king2024vestibularschwannomaand pages 4-5) |
| Primary causal gene | **NF2** on chromosome **22q12.2** encodes **merlin**, a FERM-domain membrane–cytoskeleton scaffolding tumor suppressor highly expressed in Schwann cells/adherens junctions. Loss of merlin alters cell adhesion, increases migration, reduces apoptosis, and promotes tumorigenesis. | (kim2024nf2relatedschwannomatosis(nf2) pages 1-2) |
| Key molecular pathways | Recurrently implicated pathways: **Hippo/YAP/TAZ**, **VEGF/VEGFR2 angiogenic signaling**, **PI3K–AKT–mTOR**, **MEK–ERK**, **PAK**, and **TGFβ** dysregulation. Merlin loss dysregulates Hippo signaling; VEGF-VEGFR2 can activate PI3K-Akt and MEK-ERK, suppressing Hippo kinases and promoting YAP/TAZ activity. | (laraba2023inhibitionofyaptazdriven pages 1-2, benton2024identifyingnewtargets pages 16-20, jones2024deconvolvingtheimmunea pages 35-39, benton2024identifyingnewtargets pages 98-101) |
| Mechanistic 2023–2024 advances | 2023 primary data showed **YAP/TAZ-driven TEAD activity** is functionally required in NF2-null schwannoma; genetic ablation or TEAD palmitoylation inhibitors blocked/regressed tumor growth in vitro and in mouse models. Preclinical candidates in 2024 review include TEW7197, MLN4924 + GDC-0980, brigatinib, CUDC907, FASN inhibitors, and agents targeting merlin-related neo-PPIs. | (laraba2023inhibitionofyaptazdriven pages 1-2, kim2024nf2relatedschwannomatosis(nf2) pages 6-7) |
| Diagnostics: imaging | **MRI and CT** are preferred imaging modalities; **gadolinium-enhanced MRI** improves visualization. Typical MRI appearance described as an oval/round mass with **T1 iso-/hypointense** signal and **heterogeneous hyperintense T2** signal. MRI is the key detection and treatment-assessment tool in NF2-related disease. | (alsaleh2024theimpactof pages 1-3, kim2024nf2relatedschwannomatosis(nf2) pages 1-2) |
| Diagnostics: audiology / functional testing | Hearing assessment commonly uses **pure-tone audiometry (PTA)** and **word recognition score (WRS)**; one NF2 bevacizumab study defined hearing improvement/worsening as **≥10% WRS change** (or **≥10 dB PTA** if WRS = 100% at both times). **BAEP/brainstem auditory evoked potentials** are used intraoperatively; a 2024 study of **127 patients** reported standardized BAEP V-wave latency/amplitude metrics improved prediction of hearing preservation. | (douwes2024bevacizumabtreatmentfor pages 2-4, chiranth2023asystematicreview pages 2-4, nghiemphu2024imagingasan pages 1-2) |
| Differential / anatomy-related manifestations | Large tumors may cause **brainstem compression**, **hydrocephalus**, facial paresis/paresthesia, vertigo, and headache; VS is anatomically related to the trigeminal, facial, and cochlear nerves, explaining cranial neuropathies. | (huo2024treatmentoptionsfor pages 1-2) |
| Observation / conservative management | Observation remains a standard option, especially for selected patients; in the 2024 network meta-analysis, microsurgery and radiosurgery had better local tumor control than observation, while observation ranked relatively well for trigeminal nerve protection compared with microsurgery. | (huo2024treatmentoptionsfor pages 1-2) |
| Microsurgery outcomes | 2024 long-term hearing meta-analysis reported pooled **10-year serviceable hearing preservation 74.5%** (95% CI 63.5–84.1%) for microsurgery in hearing-preservation cohorts. Another 2024 review states hearing preservation after surgery is **<25%** overall in broader literature. Surgical mortality was reported **0.38%** and overall complication rate **5.3%** in one review. | (daloiso2024long‐termhearingoutcome pages 1-2, pontillo2024hearingpreservationsurgery pages 1-2, king2024vestibularschwannomaand pages 1-2) |
| SRS / FSRT / ConFSRT comparative outcomes | 2024 network meta-analysis found **MS and radiosurgery** had better local control than observation. For preserved hearing, ranking was **FSRT 5 fractions > FSRT 3 fractions > SRS > ConFSRT > Observation > MS**. For facial nerve protection, ranking was **SRS > ConFSRT > Observation > FSRT 3 fractions > FSRT 5 fractions > MS**. For disequilibrium/vertigo improvement, **SRS** ranked best. | (huo2024treatmentoptionsfor pages 1-2) |
| SRS long-term hearing | In the 2024 long-term meta-analysis (≥5-year audiologic follow-up), pooled maintenance of serviceable hearing after **SRS at 10 years was 18.1%** (95% CI 1.7–43.3%), with wide variability. | (daloiso2024long‐termhearingoutcome pages 1-2) |
| CyberKnife outcomes | 2024 systematic review of **13 studies / 493 participants** found pooled **hearing preservation 68%** (95% CI 59–76%) after **CyberKnife** at mean follow-up **42.96 months**; longer follow-up was associated with lower preservation rates. | (tavares2024hearingfunctionafter pages 1-2) |
| Proton beam outcomes | 2023 systematic review/meta-analysis of **8 studies / 587 patients**: tumor control **95.4%**, progression **4.6%**, trigeminal nerve preservation **95.6%**, facial nerve preservation **93.7%**, hearing preservation **40.6%**, hydrocephalus requiring shunt **1.4%**. Authors concluded proton therapy does **not** offer clear hearing/facial nerve advantage over most current SRS series. | (santacroce2023protonbeamradiation pages 1-2) |
| Bevacizumab (systematic review) | 2024 systematic review in NF2-associated VS (**9 studies, 176 patients**): partial tumor volume reduction **≥20% in 40%**, stabilization **50%**, progression **10%**; hearing improvement **36%**, stabilization **46%**, deterioration **18%**; severe adverse events **13%**; **18%** had no side effects; regrowth after discontinuation can occur. | (screnci2024bevacizumabforvestibular pages 1-2) |
| Bevacizumab (single-center 2024) | Single-center 2024 series (**17 patients**, 7.5 mg/kg, median/mean treatment about **7.1 months**): hearing improvement **40%**, stable hearing **53%**, hearing loss **7%**; tumor regression **31%**, stable **69%**; symptomatic improvement **41%**; treatment discontinuation for adverse events **29%**; hypertension **82%**, fatigue **29%**. | (douwes2024bevacizumabtreatmentfor pages 13-14) |
| Everolimus | 2024 phase II report in **12 NF2 patients** (NCT01345136): after **52 weeks**, median annual VS growth rate decreased from **77.2%** to **29.4%**; **no radiographic responses** (≥20% decrease), **3/8 (37.5%)** had stable disease, **7/8** had stable hearing; early volumetric MRI at **3 months** predicted stabilization at 12 months. | (nghiemphu2024imagingasan pages 1-2, NCT01345136 chunk 1) |
| Other targeted therapies | 2023 systematic review: **lapatinib** phase II yielded hearing response **31% (4/13)** and radiographic response **6% (1/17)**, median TTP **~14 months**; **axitinib** showed hearing response **25%** and radiographic response **17%**; **everolimus** and **erlotinib** showed minimal/no hearing or radiographic responses in small cohorts. | (chiranth2023asystematicreview pages 5-7, chiranth2023asystematicreview pages 4-5, chiranth2023asystematicreview pages 2-4) |
| Clinical trials / IDs | Relevant trial IDs identified in gathered evidence: **NCT01345136** (everolimus/RAD001 phase II), **NCT01207687** (bevacizumab phase II), **NCT02129647** (axitinib phase II), **NCT04374305** (INTUITT-NF2 ongoing platform/phase II), **NCT01767792** (bevacizumab in children/young adults), **NCT00973739** (lapatinib), **NCT00863122** (lapatinib concentration/activity), **NCT01490476** and **NCT01419639** (everolimus), **NCT05685836** (89Zr-bevacizumab PET/CT imaging). | (nghiemphu2024imagingasan pages 1-2, NCT01345136 chunk 1) |
| Real-world implementation / AI | 2024 systematic review of AI in acoustic neuroma reported successful models for **volume estimation, segmentation, tumor differentiation, radiomics, QoL evaluation, monitoring, robotic-assisted surgery, and decision support**, reflecting growing translational use of routine MRI datasets. | (alsaleh2024theimpactof pages 1-3) |


*Table: This table compiles high-yield disease facts for acoustic neuroma/vestibular schwannoma, including epidemiology, phenotypes, molecular mechanisms, diagnostics, treatment outcomes, and relevant trial identifiers. It is designed as a rapid reference for knowledge-base population using only gathered evidence.*

## URLs and publication dates (from retrieved sources)
- Huo et al., *BMC Cancer*, **Dec 2024**. https://doi.org/10.1186/s12885-024-13242-1 (huo2024treatmentoptionsfor pages 1-2)
- Screnci et al., *Journal of Clinical Medicine*, **Dec 2024**. https://doi.org/10.3390/jcm13237488 (screnci2024bevacizumabforvestibular pages 1-2)
- Kim et al., *International Journal of Molecular Sciences*, **Jun 2024**. https://doi.org/10.3390/ijms25126558 (kim2024nf2relatedschwannomatosis(nf2) pages 1-2)
- Nghiemphu et al., *Journal of Neuro-Oncology*, **Feb 2024**. https://doi.org/10.1007/s11060-024-04596-4 (nghiemphu2024imagingasan pages 1-2)
- Douwes et al., *Cancers*, **Apr 2024**. https://doi.org/10.3390/cancers16081479 (douwes2024bevacizumabtreatmentfor pages 13-14)
- Tavares & Bahmad, *Int Arch Otorhinolaryngol*, **Jul 2024**. https://doi.org/10.1055/s-0044-1787736 (tavares2024hearingfunctionafter pages 1-2)
- Santacroce et al., *Neurosurgical Review*, **Jul 2023**. https://doi.org/10.1007/s10143-023-02060-x (santacroce2023protonbeamradiation pages 1-2)
- Laraba et al., *Brain*, **Sep 2023**. https://doi.org/10.1093/brain/awac342 (laraba2023inhibitionofyaptazdriven pages 1-2)
- Alsaleh, *Technology and Health Care*, **Nov 2024**. https://doi.org/10.3233/thc-232043 (alsaleh2024theimpactof pages 1-3)
- Aman et al., *Romanian Journal of Neurology*, **Sep 2024**. https://doi.org/10.37897/rjn.2024.3.7 (aman2024currenttrendsin pages 1-2)
- ClinicalTrials.gov NCT01345136, posted record (year in record excerpt: **2015**). https://clinicaltrials.gov/study/NCT01345136 (NCT01345136 chunk 1)


References

1. (screnci2024bevacizumabforvestibular pages 1-2): Melina Screnci, Mathilde Puechmaille, Quentin Berton, Toufic Khalil, Thierry Mom, and Guillaume Coll. Bevacizumab for vestibular schwannomas in neurofibromatosis type 2: a systematic review of tumor control and hearing preservation. Journal of Clinical Medicine, 13:7488, Dec 2024. URL: https://doi.org/10.3390/jcm13237488, doi:10.3390/jcm13237488. This article has 5 citations.

2. (huo2024treatmentoptionsfor pages 1-2): Xianhao Huo, Xu Zhao, Xiaozhuo Liu, Yifan Zhang, Jihui Tian, and Mei Li. Treatment options for unilateral vestibular schwannoma: a network meta-analysis. BMC Cancer, Dec 2024. URL: https://doi.org/10.1186/s12885-024-13242-1, doi:10.1186/s12885-024-13242-1. This article has 6 citations and is from a peer-reviewed journal.

3. (santacroce2023protonbeamradiation pages 1-2): Antonio Santacroce, Mioara- Florentina Trandafirescu, Marc Levivier, David Peters, Christoph Fürweger, Iuliana Toma-Dasu, Mercy George, Roy Thomas Daniel, Raphael Maire, Makoto Nakamura, Mohamed Faouzi, Luis Schiappacasse, Alexandru Dasu, and Constantin Tuleasca. Proton beam radiation therapy for vestibular schwannomas-tumor control and hearing preservation rates: a systematic review and meta-analysis. Neurosurgical Review, Jul 2023. URL: https://doi.org/10.1007/s10143-023-02060-x, doi:10.1007/s10143-023-02060-x. This article has 7 citations and is from a peer-reviewed journal.

4. (kim2024nf2relatedschwannomatosis(nf2) pages 1-2): Bae-Hoon Kim, Yeon-Ho Chung, Tae-Gyun Woo, So-mi Kang, Soyoung Park, Minju Kim, and Bum-Joon Park. Nf2-related schwannomatosis (nf2): molecular insights and therapeutic avenues. International Journal of Molecular Sciences, 25:6558, Jun 2024. URL: https://doi.org/10.3390/ijms25126558, doi:10.3390/ijms25126558. This article has 11 citations.

5. (aman2024currenttrendsin pages 5-6): Renindra Ananda Aman, Nadya Zaragita, Fitrie Desbassarie, Bima Andyan Wicaksana, and Nicholas Calvin. Current trends in vestibular schwannoma management at a referral center in indonesia: a cross-sectional study with retrospective data collection. Romanian Journal of Neurology, 23:272-280, Sep 2024. URL: https://doi.org/10.37897/rjn.2024.3.7, doi:10.37897/rjn.2024.3.7. This article has 0 citations.

6. (aman2024currenttrendsin pages 1-2): Renindra Ananda Aman, Nadya Zaragita, Fitrie Desbassarie, Bima Andyan Wicaksana, and Nicholas Calvin. Current trends in vestibular schwannoma management at a referral center in indonesia: a cross-sectional study with retrospective data collection. Romanian Journal of Neurology, 23:272-280, Sep 2024. URL: https://doi.org/10.37897/rjn.2024.3.7, doi:10.37897/rjn.2024.3.7. This article has 0 citations.

7. (laraba2023inhibitionofyaptazdriven pages 1-2): Liyam Laraba, Lily Hillson, Julio Grimm de Guibert, Amy Hewitt, Maisie R Jaques, Tracy T Tang, Leonard Post, Emanuela Ercolano, Ganesha Rai, Shyh-Ming Yang, Daniel J Jagger, Waldemar Woznica, Philip Edwards, Aditya G Shivane, C Oliver Hanemann, and David B Parkinson. Inhibition of yap/taz-driven tead activity prevents growth of nf2-null schwannoma and meningioma. Brain, 146:1697-1713, Sep 2023. URL: https://doi.org/10.1093/brain/awac342, doi:10.1093/brain/awac342. This article has 62 citations and is from a highest quality peer-reviewed journal.

8. (king2024vestibularschwannomaand pages 1-2): Ava M. King, Jaimee N. Cooper, Karina Oganezova, Jeenu Mittal, Keelin McKenna, Dimitri A. Godur, Max Zalta, Ali A. Danesh, Rahul Mittal, and Adrien A. Eshraghi. Vestibular schwannoma and tinnitus: a systematic review of microsurgery compared to gamma knife radiosurgery. Journal of Clinical Medicine, 13:3065, May 2024. URL: https://doi.org/10.3390/jcm13113065, doi:10.3390/jcm13113065. This article has 6 citations.

9. (king2024vestibularschwannomaand pages 4-5): Ava M. King, Jaimee N. Cooper, Karina Oganezova, Jeenu Mittal, Keelin McKenna, Dimitri A. Godur, Max Zalta, Ali A. Danesh, Rahul Mittal, and Adrien A. Eshraghi. Vestibular schwannoma and tinnitus: a systematic review of microsurgery compared to gamma knife radiosurgery. Journal of Clinical Medicine, 13:3065, May 2024. URL: https://doi.org/10.3390/jcm13113065, doi:10.3390/jcm13113065. This article has 6 citations.

10. (jones2024deconvolvingtheimmunea pages 35-39): AP Jones. Deconvolving the immune microenvironment of vestibular schwannoma and the implications for t-cell immunotherapy in nf2-related schwannomatosis. Unknown journal, 2024.

11. (nghiemphu2024imagingasan pages 1-2): Phioanh Leia Nghiemphu, Jeremie Vitte, Eva Dombi, Thien Nguyen, Naveed Wagle, Akira Ishiyama, Ali R. Sepahdari, David Cachia, Brigitte C. Widemann, Derald E. Brackmann, Joni K. Doherty, Michel Kalamarides, and Marco Giovannini. Imaging as an early biomarker to predict sensitivity to everolimus for progressive nf2-related vestibular schwannoma. Journal of Neuro-Oncology, 167:339-348, Feb 2024. URL: https://doi.org/10.1007/s11060-024-04596-4, doi:10.1007/s11060-024-04596-4. This article has 7 citations and is from a peer-reviewed journal.

12. (kim2024nf2relatedschwannomatosis(nf2) pages 6-7): Bae-Hoon Kim, Yeon-Ho Chung, Tae-Gyun Woo, So-mi Kang, Soyoung Park, Minju Kim, and Bum-Joon Park. Nf2-related schwannomatosis (nf2): molecular insights and therapeutic avenues. International Journal of Molecular Sciences, 25:6558, Jun 2024. URL: https://doi.org/10.3390/ijms25126558, doi:10.3390/ijms25126558. This article has 11 citations.

13. (alsaleh2024theimpactof pages 1-3): Hadeel Alsaleh. The impact of artificial intelligence in the diagnosis and management of acoustic neuroma: a systematic review. Technology and Health Care, 32:3801-3813, Nov 2024. URL: https://doi.org/10.3233/thc-232043, doi:10.3233/thc-232043. This article has 5 citations and is from a peer-reviewed journal.

14. (douwes2024bevacizumabtreatmentfor pages 2-4): Jules P. J. Douwes, Erik F. Hensen, Jeroen C. Jansen, Hans Gelderblom, and Josefine E. Schopman. Bevacizumab treatment for patients with nf2-related schwannomatosis: a single center experience. Cancers, 16:1479, Apr 2024. URL: https://doi.org/10.3390/cancers16081479, doi:10.3390/cancers16081479. This article has 13 citations.

15. (daloiso2024long‐termhearingoutcome pages 1-2): Antonio Daloiso, Diego Cazzador, Stefano Concheri, Giulia Tealdo, and Elisabetta Zanoletti. Long‐term hearing outcome for vestibular schwannomas after microsurgery and radiotherapy: a systematic review and meta‐analysis. Otolaryngology–Head and Neck Surgery, 171:1670-1681, Jul 2024. URL: https://doi.org/10.1002/ohn.910, doi:10.1002/ohn.910. This article has 8 citations.

16. (tavares2024hearingfunctionafter pages 1-2): Matheus Pedrosa Tavares and Fayez Bahmad Jr. Hearing function after cyberknife for vestibular schwannoma: a systematic review. International Archives of Otorhinolaryngology, 28:e543-e551, Jul 2024. URL: https://doi.org/10.1055/s-0044-1787736, doi:10.1055/s-0044-1787736. This article has 2 citations.

17. (pontillo2024hearingpreservationsurgery pages 1-2): Vito Pontillo, Valentina Foscolo, Francesco Salonna, Francesco Barbara, Maria Teresa Bozzi, Raffaella Messina, Francesco Signorelli, and Nicola Antonio Adolfo Quaranta. Hearing preservation surgery for vestibular schwannoma: a systematic review and meta-analysis. Acta Otorhinolaryngologica Italica, 44:S86-S93, May 2024. URL: https://doi.org/10.14639/0392-100x-suppl.1-44-2024-n2900, doi:10.14639/0392-100x-suppl.1-44-2024-n2900. This article has 8 citations and is from a peer-reviewed journal.

18. (douwes2024bevacizumabtreatmentfor pages 13-14): Jules P. J. Douwes, Erik F. Hensen, Jeroen C. Jansen, Hans Gelderblom, and Josefine E. Schopman. Bevacizumab treatment for patients with nf2-related schwannomatosis: a single center experience. Cancers, 16:1479, Apr 2024. URL: https://doi.org/10.3390/cancers16081479, doi:10.3390/cancers16081479. This article has 13 citations.

19. (NCT01345136 chunk 1):  Study of RAD001 for Treatment of NF2-related Vestibular Schwannoma. Jonsson Comprehensive Cancer Center. 2015. ClinicalTrials.gov Identifier: NCT01345136

20. (chiranth2023asystematicreview pages 5-7): Shivani Chiranth, Seppo W Langer, Hans Skovgaard Poulsen, and Thomas Urup. A systematic review of targeted therapy for vestibular schwannoma in patients with nf2-related schwannomatosis. Neuro-Oncology Advances, Aug 2023. URL: https://doi.org/10.1093/noajnl/vdad099, doi:10.1093/noajnl/vdad099. This article has 23 citations and is from a peer-reviewed journal.

21. (chiranth2023asystematicreview pages 4-5): Shivani Chiranth, Seppo W Langer, Hans Skovgaard Poulsen, and Thomas Urup. A systematic review of targeted therapy for vestibular schwannoma in patients with nf2-related schwannomatosis. Neuro-Oncology Advances, Aug 2023. URL: https://doi.org/10.1093/noajnl/vdad099, doi:10.1093/noajnl/vdad099. This article has 23 citations and is from a peer-reviewed journal.

22. (king2024vestibularschwannomaand pages 13-14): Ava M. King, Jaimee N. Cooper, Karina Oganezova, Jeenu Mittal, Keelin McKenna, Dimitri A. Godur, Max Zalta, Ali A. Danesh, Rahul Mittal, and Adrien A. Eshraghi. Vestibular schwannoma and tinnitus: a systematic review of microsurgery compared to gamma knife radiosurgery. Journal of Clinical Medicine, 13:3065, May 2024. URL: https://doi.org/10.3390/jcm13113065, doi:10.3390/jcm13113065. This article has 6 citations.

23. (benton2024identifyingnewtargets pages 16-20): Dorothy Benton. Identifying new targets and drug combinations in neurofibromatosis type 2. ArXiv, 2024. URL: https://doi.org/10.17918/00010718, doi:10.17918/00010718. This article has 1 citations.

24. (benton2024identifyingnewtargets pages 98-101): Dorothy Benton. Identifying new targets and drug combinations in neurofibromatosis type 2. ArXiv, 2024. URL: https://doi.org/10.17918/00010718, doi:10.17918/00010718. This article has 1 citations.

25. (chiranth2023asystematicreview pages 2-4): Shivani Chiranth, Seppo W Langer, Hans Skovgaard Poulsen, and Thomas Urup. A systematic review of targeted therapy for vestibular schwannoma in patients with nf2-related schwannomatosis. Neuro-Oncology Advances, Aug 2023. URL: https://doi.org/10.1093/noajnl/vdad099, doi:10.1093/noajnl/vdad099. This article has 23 citations and is from a peer-reviewed journal.