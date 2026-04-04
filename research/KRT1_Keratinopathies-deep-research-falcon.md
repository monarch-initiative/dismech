---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:50.804441'
end_time: '2026-04-04T12:56:56.781697'
duration_seconds: 845.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KRT1 Keratinopathies
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KRT1 Keratinopathies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KRT1 Keratinopathies** covering all of the
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
- **Disease Name:** KRT1 Keratinopathies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KRT1 Keratinopathies** covering all of the
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


# Comprehensive Research Report: KRT1 Keratinopathies (Mendelian)

## Executive summary
KRT1 keratinopathies are dominantly inherited (often de novo; sometimes mosaic) disorders of epidermal differentiation and mechanical integrity caused by pathogenic variants in **KRT1** (Keratin 1). The phenotype spectrum is classically anchored by **epidermolytic ichthyosis / epidermolytic hyperkeratosis** (EI/EHK; OMIM **113800**) and **epidermolytic palmoplantar keratoderma (EPPK), Vörner type** (OMIM **144200**), with frequent palmoplantar involvement in KRT1-associated disease. Recent work (2023–2025) highlights: (i) measurable early-life burden and genotype–severity correlations in cohort studies, (ii) emerging immunologic mechanisms (e.g., TLR2→NF-κB/GATA3) linking barrier failure to hyperkeratosis and keratin regulation, and (iii) early therapeutic exploration of biologics targeting the Th17 axis (IL‑17A blockade) and clinical trials of IL‑17A/IL‑12/23 blockade in inherited ichthyoses. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, frommherz2025epidermolyticichthyosisclinical pages 4-5, cheng2025firstsuccessfultreatment pages 3-4, tagoe2023chronicactivationof pages 1-5, NCT03041038 chunk 1)

---

## Target disease
- **Disease name (umbrella):** KRT1 keratinopathies
- **Category:** Mendelian
- **Causal gene:** **KRT1** (Keratin 1)

### MONDO / Orphanet / ICD / MeSH identifiers
Within the retrieved full-text evidence set for this run, **Orphanet, ICD-10/ICD-11, MeSH, and MONDO identifiers were not explicitly stated** for KRT1 keratinopathies; therefore they cannot be reliably populated from the current evidence corpus. OMIM identifiers were extractable (below). (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, smith2019novelandrecurrent pages 1-3)

---

## 1. Disease information
### 1.1 What is the disease?
“KRT1 keratinopathies” refers to a spectrum of inherited skin cornification/cell-fragility disorders due to KRT1 variants affecting suprabasal keratinocytes. The most canonical KRT1-associated entities are:
- **Epidermolytic ichthyosis (EI)**, historically also termed **epidermolytic hyperkeratosis (EHK)** or **bullous ichthyosiform erythroderma**, characterized by congenital erythroderma with blistering/erosions followed by progressive hyperkeratosis. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, smith2019novelandrecurrent pages 1-3)
- **Epidermolytic palmoplantar keratoderma (EPPK; Vörner type)**, often a diffuse palm/sole hyperkeratosis phenotype; most commonly due to KRT9 but can be due to KRT1. (smith2019novelandrecurrent pages 5-6, smith2019novelandrecurrent pages 1-3)

### 1.2 Key identifiers (from evidence)
- **Epidermolytic ichthyosis (EI)**: OMIM **113800** (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, smith2019novelandrecurrent pages 1-3)
- **Epidermolytic palmoplantar keratoderma (EPPK; Vörner type)**: OMIM **144200** (smith2019novelandrecurrent pages 5-6, smith2019novelandrecurrent pages 1-3)
- **KRT1 gene**: OMIM **139350** (aljuwaied2024epidermolytichyperkeratosistype pages 9-10, gram2025clinicalandgenetic pages 2-3)

### 1.3 Common synonyms / alternative names
- EI synonyms: **epidermolytic hyperkeratosis (EHK)**; “formerly known as bullous ichthyosiform erythroderma” (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)
- EPPK synonyms: **epidermolytic PPK**, **Vörner type** (smith2019novelandrecurrent pages 5-6, smith2019novelandrecurrent pages 1-3)

### 1.4 Evidence source type
Most information is derived from:
- **Aggregated disease-level cohorts** (e.g., German EI cohort; Danish PPK cohort) (frommherz2025epidermolyticichthyosisclinical pages 4-5, gram2025clinicalandgenetic pages 1-2)
- **Primary case reports** expanding variant spectrum and demonstrating therapeutic hypotheses (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, cheng2025firstsuccessfultreatment pages 3-4)
- **Mechanistic experimental models** (rat/human keratinocytes; organotypic cultures) (tagoe2023chronicactivationof pages 8-13)

| Clinical entity | Key synonyms | Inheritance | Key OMIM identifiers | Typical onset/course | Hallmark features | Key supporting citations |
|---|---|---|---|---|---|---|
| KRT1-related epidermolytic ichthyosis | Epidermolytic hyperkeratosis (EHK); bullous ichthyosiform erythroderma; keratinopathic ichthyosis | Usually autosomal dominant; can occur de novo; mosaic cases also reported | EI OMIM 113800; KRT1 OMIM 139350 | Usually present at birth with erythroderma, blistering, and erosions; blistering often decreases over weeks to months, followed by progressive generalized hyperkeratosis in childhood/adolescence; severity variable, with KRT1 often associated with more severe/intermediate disease and frequent palmoplantar involvement | Congenital erythroderma; superficial blisters/erosions; generalized ichthyotic hyperkeratosis; palmoplantar keratoderma; painful fissures; pruritus; contractures/joint limitation in severe cases; histology shows epidermolytic hyperkeratosis/granular degeneration | (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, aljuwaied2024epidermolytichyperkeratosistype pages 9-10, frommherz2025epidermolyticichthyosisclinical pages 4-5, smith2019novelandrecurrent pages 5-6, smith2019novelandrecurrent pages 1-3) |
| KRT1-related epidermolytic palmoplantar keratoderma | EPPK; epidermolytic PPK; Vörner type palmoplantar keratoderma | Autosomal dominant | EPPK OMIM 144200; KRT1 OMIM 139350 | Typically begins in infancy or early childhood; chronic lifelong course with persistent diffuse palmoplantar hyperkeratosis; phenotype may remain localized to palms/soles or coexist with broader epidermolytic ichthyosis depending on variant | Diffuse well-demarcated palmar and plantar hyperkeratosis; fissuring; painful cracks; erythematous/violaceous border in some families; limited or absent blistering in localized forms; variable intrafamilial severity | (gram2025clinicalandgenetic pages 1-2, gram2025clinicalandgenetic pages 2-3, smith2019novelandrecurrent pages 5-6, smith2019novelandrecurrent pages 1-3, smith2019novelandrecurrent pages 3-5) |
| Broader KRT1 keratinopathy spectrum | KRT1 keratinopathies; KRT1-associated keratinopathic ichthyosis/PPK spectrum | Predominantly autosomal dominant; de novo and postzygotic mosaicism documented | KRT1 gene OMIM 139350; associated disease OMIMs include 113800 and 144200 | Spectrum ranges from severe neonatal EI with later diffuse hyperkeratosis to milder/pure palmoplantar disease; genotype-phenotype relationships are complex because pathogenic variants are distributed across the protein rather than confined to one hotspot | Suprabasal keratinocyte fragility from keratin filament dysfunction; PPK is more strongly associated with KRT1 than KRT10; recent cohorts identified novel KRT1 variants and documented substantial disease burden, including NICU need in neonatal EI and underweight in infancy in a subset | (frommherz2025epidermolyticichthyosisclinical pages 4-5, smith2019novelandrecurrent pages 5-6, smith2019novelandrecurrent pages 1-3, smith2019novelandrecurrent pages 6-7) |


*Table: This table summarizes the main KRT1-associated clinical entities, their synonyms, inheritance, OMIM identifiers, typical course, and hallmark manifestations. It is useful as a compact reference for mapping KRT1 variation to epidermolytic ichthyosis and epidermolytic palmoplantar keratoderma phenotypes.*

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** pathogenic **germline or postzygotic (mosaic) variants in KRT1**, generally acting through **dominant-negative disruption** of suprabasal keratin intermediate filament networks, leading to cellular fragility and barrier dysfunction. (aljuwaied2024epidermolytichyperkeratosistype pages 2-9, smith2019novelandrecurrent pages 6-7)

### 2.2 Risk factors
- **Genetic:** KRT1 pathogenic variants (heterozygous) are sufficient; disease may be **de novo** or **inherited**. Mosaicism can contribute to segmental presentations or complex genotype-phenotype effects. (frommherz2025epidermolyticichthyosisclinical pages 4-5, diociaiuti2020firstcaseof pages 1-4)
- **Environmental/mechanical:** While not quantified in the retrieved sources, clinical descriptions emphasize palmoplantar fissuring and pain, consistent with **mechanical stress** worsening volar manifestations in keratin disorders (supported indirectly by palmoplantar disease focus and cohort characterization). (cheng2025firstsuccessfultreatment pages 3-4, smith2019novelandrecurrent pages 5-6)

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved full-text corpus.

### 2.4 Gene–environment interactions
Direct G×E interaction studies specific to KRT1 keratinopathies were not identified in the retrieved evidence. Mechanistic work supports a model where barrier defects and inflammatory signaling form a feedback loop influencing keratin expression (see Pathophysiology). (tagoe2023chronicactivationof pages 8-13)

---

## 3. Phenotypes
### 3.1 Core phenotype domains (with suggested HPO terms)
Below are common manifestations across KRT1 keratinopathies; frequencies are included when available.

1. **Neonatal erythroderma / widespread erythema**  
   - HPO: **HP:0001041** (Erythroderma) / **HP:0000988** (Erythema)
   - Typical onset: **at birth** in EI (frommherz2025epidermolyticichthyosisclinical pages 4-5, smith2019novelandrecurrent pages 1-3)

2. **Skin blistering / erosions (early life)**  
   - HPO: **HP:0008064** (Blistering of the skin), **HP:0001073** (Skin erosions)
   - Course: often prominent neonatally and may lessen over weeks–months, followed by hyperkeratosis (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, aljuwaied2024epidermolytichyperkeratosistype pages 2-9)

3. **Generalized hyperkeratosis / scaling (ichthyosis phenotype)**  
   - HPO: **HP:0000962** (Hyperkeratosis), **HP:0008066** (Ichthyosis), **HP:0000976** (Palmoplantar hyperkeratosis) when volar
   - Progression: hyperkeratosis emerges in childhood/adolescence after neonatal blistering/erythroderma (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)

4. **Palmoplantar keratoderma (PPK)**  
   - HPO: **HP:0000972** (Palmoplantar keratoderma)
   - Frequency estimates: a 2024 case report cites ~**60%** palmoplantar involvement in EHK/EI (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)
   - Phenotype: diffuse, well-demarcated palmar/plantar hyperkeratosis with fissures and pain (cheng2025firstsuccessfultreatment pages 3-4, smith2019novelandrecurrent pages 5-6)

5. **Pruritus (itching)**  
   - HPO: **HP:0000989** (Pruritus)
   - Noted as severe in pediatric EI treated with IL‑17A blockade (cheng2025firstsuccessfultreatment pages 1-3)

6. **Fissuring and pain**  
   - HPO: **HP:000裂** (no single universal HPO for “fissures”; commonly mapped to **HP:0100881** (Skin fissures) in many ontologies)
   - Described in KRT1-EPPK and KRT1-EI with thick volar keratosis (cheng2025firstsuccessfultreatment pages 3-4, smith2019novelandrecurrent pages 5-6)

7. **Joint limitation/contractures (severe cases)**  
   - HPO: **HP:0001371** (Flexion contracture), **HP:0001387** (Joint contracture)
   - Reported in severe EHK with thickening around joints (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, aljuwaied2024epidermolytichyperkeratosistype pages 9-10)

### 3.2 Phenotype severity and QoL impact (data)
- In a German EI cohort, early-life morbidity was substantial: **25/41** required immediate incubator/NICU care; **17/44 (38.6%)** were underweight or <5th percentile in infancy; **6/45 (13.3%)** were preterm. (frommherz2025epidermolyticichthyosisclinical pages 4-5)
- A biologic-treated pediatric EI case tracked **DLQI** and symptom scales (NRS, VAS) and reported improvement alongside clinical severity score reductions. (cheng2025firstsuccessfultreatment pages 1-3)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **KRT1 (Keratin 1)**: OMIM **139350** (gram2025clinicalandgenetic pages 2-3)

### 4.2 Pathogenic variants (examples from primary literature)
The evidence corpus includes multiple KRT1 variant examples across domains:
- **KRT1 c.583A>T; p.Ile195Phe** (reported as novel/likely pathogenic in a 2024 EHK case report) (aljuwaied2024epidermolytichyperkeratosistype pages 9-10, aljuwaied2024epidermolytichyperkeratosistype pages 2-9)
- **KRT1 c.1432G>A; p.Glu478Lys (p.E478K)** (de novo; pediatric EI case treated with IL‑17A blockade) (cheng2025firstsuccessfultreatment pages 1-3)
- Smith et al. 2019 variants spanning KRT1 including **p.Leu187Pro**, **p.Leu187Phe**, **p.Ser233Leu**, **p.Leu485Phe**, **p.Leu485Pro**, and splice-site/insertions (e.g., **c.1254+1G>A → p.Gln418_Ile419ins18**) across EI/EPPK presentations (smith2019novelandrecurrent pages 1-3, smith2019novelandrecurrent pages 3-5)
- Diociaiuti et al. 2020 cohort lists KRT1 variants including **c.1792dupA (p.Ser598Lysfs*56)** and **c.1319C>T (p.Ala440Val)** and others in KRT1-associated EI cases with frequent PPK (diociaiuti2020firstcaseof pages 4-5, diociaiuti2020firstcaseof pages 7-9)

**Variant class distribution:** predominantly missense in conserved keratin rod domains, with some frameshift/tail-domain variants associated with milder phenotypes in cohort observations. (diociaiuti2020firstcaseof pages 7-9, aljuwaied2024epidermolytichyperkeratosistype pages 2-9)

### 4.3 Genotype–phenotype correlations
- KRT1 mutations can produce EI and/or EPPK; Smith et al. emphasize that KRT1 mutations are distributed through the protein and “**can result in a range of phenotypes**,” yielding complex correlations. (smith2019novelandrecurrent pages 1-3)
- In the German EI cohort, **KRT1 germline variants** were associated more frequently with intermediate/severe disease (**15/19**) and higher severity scores (median **mIASI 19.10** for KRT1 vs **14.40** for KRT10). (frommherz2025epidermolyticichthyosisclinical pages 4-5)
- Diociaiuti et al. report PPK in nine EI patients, corresponding mainly to KRT1-mutant cases, consistent with the classic association of KRT1 with prominent palmoplantar disease. (diociaiuti2020firstcaseof pages 7-9, diociaiuti2020firstcaseof pages 1-4)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, disease-specific epigenetic signatures, or chromosomal abnormalities for KRT1 keratinopathies were extractable from the retrieved evidence.

---

## 5. Environmental information
No specific toxins, lifestyle factors, or infectious triggers were systematically identified in the retrieved evidence as causal. However, complications such as bacterial colonization and odor are described in clinical narratives, motivating careful infection surveillance and barrier support. (aljuwaied2024epidermolytichyperkeratosistype pages 9-10)

---

## 6. Mechanism / pathophysiology
### 6.1 Core structural mechanism (keratin filament dysfunction)
Keratin 1 is expressed in suprabasal epidermal layers (paired with type I keratins such as KRT10 in many contexts). Pathogenic variants in conserved α-helical rod domains disrupt keratin filament assembly and cause keratinocyte fragility and cytolysis.
- A 2024 KRT1 EHK report describes mutations disrupting helix initiation/termination and filament assembly, leading to cytolysis/blister formation. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, aljuwaied2024epidermolytichyperkeratosistype pages 2-9)

**Suggested GO biological process terms** (conceptual mapping):
- GO: **keratinization**, **intermediate filament organization**, **epidermis development**, **cornified envelope formation**, **response to mechanical stimulus**.

**Suggested GO cellular component terms:**
- GO: **intermediate filament cytoskeleton**, **desmosome** (due to keratin anchoring), **cornified envelope**.

**Suggested CL (cell types):**
- CL: **keratinocyte**, especially **suprabasal keratinocyte** (spinous/granular layer keratinocytes).

### 6.2 Barrier failure → inflammation and hyperkeratosis feedback (recent mechanistic model)
A 2023 mechanistic preprint proposes TLR2 activation as a shared pathway in ichthyoses that links innate immune signaling to differentiation programs and KRT1 expression:
- TLR2 activation increased differentiation/cornified envelope gene expression and induced hyperkeratosis in organotypic culture; conversely, blockade reduced KRT1 expression in disease models. (tagoe2023chronicactivationof pages 1-5, tagoe2023chronicactivationof pages 8-13)
- The authors state that blockade of TLR2 signaling “**reduced the expression of keratin 1**,” and that **GATA3 overexpression was “sufficient to increase Keratin 1 expression.”** (tagoe2023chronicactivationof pages 1-5, tagoe2023chronicactivationof pages 13-17)
- Quantitative signatures include **1810 differentially expressed genes** after TLR2 agonist stimulation and **38/61 (62%)** gene overlap between TLR2 activation and ARCI knockdown models. (tagoe2023chronicactivationof pages 13-17, tagoe2023chronicactivationof pages 8-13)

This provides a plausible chain: **primary barrier/structural defect → endogenous danger signals → TLR2/NF‑κB activation → GATA3-driven differentiation and keratinization programs → hyperkeratosis and altered KRT1 expression**, which could be therapeutically targetable. (tagoe2023chronicactivationof pages 8-13)

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
Primary tissue involved is **skin**, with strong involvement of **palmoplantar epidermis** in KRT1-related disease.
- Suggested UBERON terms: **UBERON:0002097 (skin)**, **UBERON:0004264 (palm)**, **UBERON:0004278 (sole of foot)**.

### 7.2 Cell/subcellular level
- Cell: **suprabasal keratinocytes** (spinous/granular layers) (aljuwaied2024epidermolytichyperkeratosistype pages 9-10)
- Subcellular: **keratin intermediate filaments / tonofilaments**, with tonofilament aggregation described on ultrastructure in keratinopathic ichthyoses. (diociaiuti2020firstcaseof pages 1-4)

---

## 8. Temporal development
- **Typical onset:** congenital or neonatal for EI; infancy/early childhood typical for EPPK manifestations. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, smith2019novelandrecurrent pages 5-6)
- **Course:** neonatal blistering/erythroderma often improves, with progressive hyperkeratosis emerging later; severity can decrease with age in some cohorts (not uniformly). (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, diociaiuti2020firstcaseof pages 12-14)

---

## 9. Inheritance and population
### 9.1 Inheritance
- Predominantly **autosomal dominant** (including de novo). (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, smith2019novelandrecurrent pages 1-3)
- **Postzygotic mosaicism** is clinically relevant and has been detected in ichthyosis cohorts; mosaic disease can complicate genotype–phenotype relationships. (frommherz2025epidermolyticichthyosisclinical pages 4-5)

### 9.2 Epidemiology (available quantitative data)
- A 2024 case report cites EHK/EI prevalence as approximately **1:200,000 to 1:300,000**. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)
- Palmoplantar involvement is cited as ~**60%** in that same source (contextual estimate). (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)

Large population prevalence/incidence estimates stratified by KRT1 specifically were not available in the retrieved evidence.

---

## 10. Diagnostics
### 10.1 Clinical and pathology-based diagnosis
- Classic EI features (erythroderma + blistering at birth, later hyperkeratosis) guide clinical suspicion. (smith2019novelandrecurrent pages 1-3)
- Histology often shows **epidermolytic hyperkeratosis / granular degeneration**: orthohyperkeratosis, suprabasal vacuolated keratinocytes and irregular keratohyalin granules. (sussmuth2026defininghistologicalpatterns pages 18-20)
- Dermatopathology alone is not fully specific; EHK patterns can appear in other conditions (epidermal nevi, keratoses, carcinomas, inflammatory diseases), so molecular confirmation is recommended. (sussmuth2026defininghistologicalpatterns pages 25-27)

### 10.2 Genetic testing
- NGS-based approaches (exome/genome with targeted panels) provide high yield in genetically heterogeneous keratinization disorders such as PPK: 83% diagnostic yield in a Danish PPK cohort (including KRT1 cases). (gram2025clinicalandgenetic pages 1-2, gram2025clinicalandgenetic pages 2-3)
- Genetic testing is emphasized for definitive subtype assignment and genetic counseling in keratinopathic ichthyoses. (diociaiuti2020firstcaseof pages 1-4)

---

## 11. Outcome / prognosis
KRT1 keratinopathies are generally chronic and lifelong skin disorders with substantial morbidity but typically not characterized by systemic organ failure in the retrieved evidence.
- Burden is highest in neonatal period for EI (NICU need) and in chronic symptoms such as fissuring pain, pruritus, and mobility limitation. (frommherz2025epidermolyticichthyosisclinical pages 4-5, aljuwaied2024epidermolytichyperkeratosistype pages 9-10)
- Quantitative survival/life expectancy data were not identified in the retrieved full-text set.

---

## 12. Treatment
### 12.1 Standard-of-care / real-world implementation
Common approaches include:
- **Barrier repair and symptom control:** emollients and keratolytics as first-line; careful balancing to avoid worsening blistering or barrier compromise. (aljuwaied2024epidermolytichyperkeratosistype pages 9-10)
- **Antimicrobials for fissures/erosions:** management of open lesions with antimicrobials until healed is recommended in clinical descriptions. (aljuwaied2024epidermolytichyperkeratosistype pages 9-10)
- **Systemic retinoids:** oral retinoids (e.g., **acitretin**) for severe hyperkeratosis; included in case-based management. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)

**Suggested MAXO mappings (conceptual):**
- MAXO: topical emollient therapy; keratolytic therapy; systemic retinoid therapy; antimicrobial therapy for skin infection/erosions.

### 12.2 Recent/experimental therapeutics (2023–2025)
**Anti–IL‑17A therapy (case-level evidence):**
- A 2025 case report describes a 4-year-old with KRT1 EI (c.1432G>A; p.E478K) treated with **Vunakizumab** (anti–IL‑17A). The report explicitly states: “**It inhibits the interaction of IL-17A with its receptor** … and alleviates the inflammatory process,” and reports improvements after three months. (cheng2025firstsuccessfultreatment pages 1-3)
- Quantitative improvement: **IASI-E 11.6 → 5.3** and **IASI-S 14.1 → 9.3**; inflammatory biomarkers (IL‑17A, TNF‑α, sIL‑2R) normalized; “no observed adverse effects or elevated infection rates.” (cheng2025firstsuccessfultreatment pages 3-4, cheng2025firstsuccessfultreatment pages 4-5)

**Clinical trials relevant to KRT1/EI (biologics and pathway therapies):**
- **Secukinumab (anti–IL‑17A) in ichthyoses (NCT03041038)** included **epidermolytic ichthyosis**, was Phase 2, randomized crossover, quadruple-masked, enrolling 20 adults, with primary endpoints of Week‑16 IASI reduction and mucocutaneous infection counts. (NCT03041038 chunk 1)
- Additional biologic trials include ustekinumab extension (NCT04549792) and an EGFR-inhibition study for keratinopathies (NCT06545695), though detailed subtype/endpoints were not available in the retrieved trial text chunks. (NCT04549792 chunk 2)

| NCT number | Title | Status | Phase | Population / subtypes relevant to KRT1 keratinopathies | Intervention | Design | Primary endpoints | Enrollment | Key dates | Citation context IDs |
|---|---|---|---|---|---|---|---|---:|---|---|
| NCT03041038 | The Efficacy and Safety of Secukinumab in Patients With Ichthyoses | Completed | Phase 2 | Adults with confirmed ichthyosis including autosomal recessive congenital ichthyosis (ARCI-LI, ARCI-CIE), epidermolytic ichthyosis (EI), and Netherton syndrome; mesh terms also include “Hyperkeratosis, Epidermolytic,” making it directly relevant to KRT1-associated epidermolytic disease | Secukinumab 300 mg SC weekly for 5 weeks then monthly vs placebo (sterile saline) | Interventional, randomized, crossover, quadruple-masked | Efficacy: reduction at Week 16 in Ichthyosis Area Severity Index (IASI); Safety: total number of bacterial or fungal mucocutaneous infections through Week 16 | 20 | Start: 2016-12; Primary completion: 2020-08-31 (actual); Study completion: 2020-08-31 (actual); Results first posted: 2021-08-25 | (NCT03041038 chunk 2, NCT03041038 chunk 1) |
| NCT04549792 | An Open-Label and Long-Term Extension Study to Evaluate the Efficacy and Safety of Ustekinumab in the Treatment of Patients With Ichthyoses | Completed | Early Phase 1 | Ichthyosis population; excludes ichthyosis vulgaris and X-linked recessive ichthyosis; relevant as a biologic study in inherited ichthyoses/keratinization disorders, though EI/KRT1-specific inclusion is not explicit in retrieved chunks | Ustekinumab | Open-label, long-term extension | Not stated in retrieved excerpts | 13 | Registry metadata indicates 2021 record; specific start/completion/results dates not available in retrieved excerpts | (NCT04549792 chunk 2) |
| NCT06545695 | Epidermal Growth Factor Receptor Inhibition for Keratinopathies | Not yet recruiting | Phase 1/Phase 2 | Keratinopathies; likely highly relevant to KRT1 keratinopathies by title, but subtype-specific eligibility details were not available in retrieved excerpts | EGFR inhibition | Interventional; further randomization/masking details not available in retrieved excerpts | Not available in retrieved excerpts | 44 | Dates not available in retrieved excerpts | (NCT03041038 chunk 2, NCT04549792 chunk 2, NCT03041038 chunk 1) |
| NCT00074685 | National Registry for Ichthyosis and Related Disorders | Completed | Not applicable (observational) | Broad ichthyosis and related disorders registry; useful for natural history, phenotyping, and case ascertainment relevant to rare KRT1-associated ichthyoses, though EI-specific inclusion details were not available in retrieved excerpts | Registry / observational data collection | Observational registry | Not available in retrieved excerpts | 610 | Dates not available in retrieved excerpts | (NCT03041038 chunk 2, NCT04549792 chunk 2, NCT03041038 chunk 1) |
| NCT05312073 | Study of in Vivo and in Vitro Transcriptomic and Proteomic Signatures in Unhereditary Ichtyosis | Completed | Not applicable | Unhereditary ichthyosis; lower direct relevance to KRT1 Mendelian keratinopathies, but potentially informative for inflammatory/barrier molecular signatures | Transcriptomic/proteomic profiling study | Interventional / translational profiling study; detailed allocation and masking not available in retrieved excerpts | Not available in retrieved excerpts | 18 | Dates not available in retrieved excerpts | (NCT03041038 chunk 2, NCT04549792 chunk 2, NCT03041038 chunk 1) |


*Table: This table summarizes ClinicalTrials.gov studies with direct or potential relevance to KRT1 keratinopathies, especially epidermolytic ichthyosis. It highlights which trials explicitly included epidermolytic/hyperkeratotic subtypes, what interventions were tested, and where retrieved record details remain incomplete.*

### 12.3 Expert/authoritative analysis (from primary authors)
- Smith et al. emphasize the complexity of genotype–phenotype correlation for KRT1, noting KRT1 mutations “**can result in a range of phenotypes**,” motivating careful variant-level interpretation as mutation-specific therapies emerge. (smith2019novelandrecurrent pages 1-3, smith2019novelandrecurrent pages 6-7)
- Süßmuth et al. caution that the epidermolytic hyperkeratosis pattern is diagnostically helpful but not specific, reinforcing the need for genetic confirmation for classification. (sussmuth2026defininghistologicalpatterns pages 25-27)

---

## 13. Prevention
Primary prevention of new cases is not feasible for de novo dominant disorders, but **genetic counseling and reproductive planning** are key:
- Because KRT1 disorders can be de novo and mosaic, recurrence risk assessment may require sensitive testing strategies and careful counseling. (frommherz2025epidermolyticichthyosisclinical pages 4-5, diociaiuti2020firstcaseof pages 1-4)
- Secondary/tertiary prevention focuses on preventing complications of barrier dysfunction (erosions, secondary infection) with proactive skin care and prompt antimicrobial management when fissures/erosions occur. (aljuwaied2024epidermolytichyperkeratosistype pages 9-10)

---

## 14. Other species / natural disease
No naturally occurring non-human KRT1 keratinopathy was identified in the retrieved evidence corpus.

---

## 15. Model organisms and experimental systems
The retrieved evidence supports several experimental systems relevant to mechanisms and therapeutic discovery:
- **Rat epidermal keratinocytes (REKs)** and **human keratinocytes** used for time-course RNA-seq and pathway perturbation (TLR2 agonism; NF‑κB/GATA3 axis) demonstrating regulation of keratinization programs and KRT1 expression. (tagoe2023chronicactivationof pages 13-17, tagoe2023chronicactivationof pages 8-13)
- **Organotypic skin cultures** showing dose-dependent cornified layer thickening after TLR2 activation and response to pathway blockade. (tagoe2023chronicactivationof pages 8-13)

Dedicated **Krt1 knock-in/knockout mouse model papers** were not available in accessible full-text during this run, so specific model strain details and phenotypic recapitulation cannot be cited here.

---

## Recent developments snapshot (prioritizing 2023–2025)
| Year/month | Study type | Development relevant to KRT1 keratinopathies | Key quantitative data | Citation context IDs |
|---|---|---|---|---|
| 2025-05 | Case report | First reported use of IL-17A blockade with Vunakizumab in a 4-year-old boy with KRT1-related epidermolytic ichthyosis (KRT1 c.1432G>A, p.Glu478Lys / p.E478K) after failure of conventional topical/keratolytic/retinoid approaches; rationale based on elevated Th17-associated inflammatory markers | Dosing: 120 mg every 10 days for 3 cycles, then every 3 weeks; IASI-E improved 11.6 → 5.3; IASI-S improved 14.1 → 9.3; biomarkers IL-17A, TNF-α, sIL-2R normalized by 3 months; no observed adverse effects or increased infections | (cheng2025firstsuccessfultreatment pages 3-4, cheng2025firstsuccessfultreatment pages 1-3, cheng2025firstsuccessfultreatment pages 4-5) |
| 2025-05 | Cohort study | Large German epidermolytic ichthyosis cohort refined genotype-phenotype correlations and quantified early-life burden; KRT1 germline variants were associated more often with intermediate/severe disease than KRT10 | 44 patients total; 25/41 required immediate incubator/NICU care; 6/45 (13.3%) preterm; 17/44 (38.6%) underweight or <5th percentile in infancy; KRT1 intermediate/severe in 15/19; median mIASI 19.10 for KRT1 vs 14.40 for KRT10 | (frommherz2025epidermolyticichthyosisclinical pages 4-5) |
| 2025-02 | PPK cohort study | Danish palmoplantar keratoderma cohort showed value of genomic diagnosis in heterogeneous PPK, including KRT1-associated cases relevant to epidermolytic palmoplantar keratoderma within the KRT1 spectrum | 142 patients from 76 families; molecular diagnosis in 63/76 probands (83%); 27 disease-causing variants across 13 genes; KRT1 accounted for 3/76 probands | (gram2025clinicalandgenetic pages 1-2, gram2025clinicalandgenetic pages 2-3, gram2025clinicalandgenetic pages 7-8) |
| 2024-11 | Case report | Novel heterozygous KRT1 epidermolytic hyperkeratosis / epidermolytic ichthyosis variant expanded the mutational spectrum and reiterated classic KRT1-associated clinical course and pathology | Prevalence cited as ~1:200,000-1:300,000; palmoplantar involvement reported in ~60% of cases; variant reported as KRT1 c.583A>T, p.Ile195Phe | (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, aljuwaied2024epidermolytichyperkeratosistype pages 9-10, aljuwaied2024epidermolytichyperkeratosistype pages 2-9) |
| 2023-06 | Mechanistic preprint | Chronic TLR2 activation was proposed as a shared ichthyosis pathway that upregulates KRT1 through NF-κB and GATA3, linking innate immune signaling to hyperkeratosis and suggesting TLR2 blockade as a therapeutic strategy | RNA-seq identified 1810 differentially expressed genes after PAM3CSK4; 38/61 (62%) genes overlapped between TLR2 activation and ARCI knockdown models; 20 proteins upregulated and 18 downregulated (≥1.5-fold) in proteomics; KRT1 increased by ~12-24 h after TLR2 activation; organotypic cultures showed dose-dependent cornified layer thickening | (tagoe2023chronicactivationof pages 1-5, tagoe2023chronicactivationof pages 13-17, tagoe2023chronicactivationof pages 8-13, tagoe2023chronicactivationof pages 17-20, tagoe2023chronicactivationof pages 20-24) |
| 2023-11 | Diagnostic case report | Molecular confirmation remained essential in atypical epidermolytic ichthyosis presentations lacking classic blistering or clear epidermolysis on histology, underscoring relevance for differential diagnosis within keratinopathic ichthyosis | Single adult case; KRT10 c.467G>A (p.Arg156His); illustrates that unclear clinicopathologic cases may require sequencing for confirmation | (aljuwaied2024epidermolytichyperkeratosistype pages 1-2, sussmuth2026defininghistologicalpatterns pages 25-27, sussmuth2026defininghistologicalpatterns pages 18-20) |


*Table: This table summarizes notable 2023-2025 clinical and mechanistic developments relevant to KRT1 keratinopathies, including therapeutic innovation, cohort burden data, and emerging pathway biology. It is useful for quickly identifying what is new, quantitatively supported, and potentially actionable.*

---

## Key citations with URLs and publication dates (from retrieved sources)
- Aljuwaied et al. **Nov 2024**. *Epidermolytic Hyperkeratosis Type 1 with a New Heterozygous Mutation in KRT1 Gene: A Case Report.* **DOI:** https://doi.org/10.69709/genomc.2024.135001 (aljuwaied2024epidermolytichyperkeratosistype pages 1-2)
- Tagoe et al. **Jun 2023** (preprint). *Chronic activation of Toll-like receptor 2 induces an ichthyotic skin phenotype.* **DOI:** https://doi.org/10.1101/2022.06.06.494922 (tagoe2023chronicactivationof pages 1-5)
- Frommherz et al. **May 2025**. *Epidermolytic ichthyosis: clinical spectrum and burden of disease in a large German cohort.* **DOI:** https://doi.org/10.1111/jdv.20096 (frommherz2025epidermolyticichthyosisclinical pages 4-5)
- Cheng et al. **May 2025**. *First successful treatment of epidermolytic ichthyosis with Vunakizumab: A case report.* **DOI:** https://doi.org/10.3389/fimmu.2025.1574255 (cheng2025firstsuccessfultreatment pages 3-4)
- Smith et al. **Oct 2019**. *Novel and recurrent mutations in keratin 1 cause epidermolytic ichthyosis and palmoplantar keratoderma.* **DOI:** https://doi.org/10.1111/ced.13800 (smith2019novelandrecurrent pages 1-3)
- Diociaiuti et al. **Oct 2020**. *First case of KRT2 epidermolytic nevus and novel clinical and genetic findings in 26 Italian patients with keratinopathic ichthyoses.* **DOI:** https://doi.org/10.3390/ijms21207707 (diociaiuti2020firstcaseof pages 1-4)
- ClinicalTrials.gov **NCT03041038** (posted results metadata available in record). *Secukinumab in patients with ichthyoses (includes epidermolytic ichthyosis).* https://clinicaltrials.gov/study/NCT03041038 (NCT03041038 chunk 1)

---

## Limitations of this report (evidence-bound)
1. Cross-ontology identifiers (Orphanet/ICD/MeSH/MONDO) were not present in the retrieved full-text excerpts and thus are not populated here.
2. Several clinical trial records were only partially captured in the retrieved chunks (e.g., NCT04549792, NCT06545695), limiting endpoint/date/result extraction.
3. Dedicated Krt1 in vivo model organism primary papers were not available as full text within this run; only keratinocyte/organotypic experimental systems could be cited.


References

1. (aljuwaied2024epidermolytichyperkeratosistype pages 1-2): Maitha Abdulla Aljuwaied, Waqas Saad Abdulwahha, Mays Alrim Mustafa Al Moukdad, Moza Kamil Bin Kamil Alshamsi, Sham Zain AlAbdin, Ahmed Elbarkouky, Omar El Khatib, and Salahdein Aburuz. Epidermolytic hyperkeratosis type 1 with a new heterozygous mutation in krt1 gene: a case report. GenoMed Connect, 1:1, Nov 2024. URL: https://doi.org/10.69709/genomc.2024.135001, doi:10.69709/genomc.2024.135001. This article has 0 citations.

2. (frommherz2025epidermolyticichthyosisclinical pages 4-5): Leonie Frommherz, Kathrin Giehl, Josephine Hofmann, Stefanie Huebner, Kirstin Kiekbusch, Teodora Sabkova, Kira Süßmuth, Svenja Alter, Iliana Tantcheva‐Poór, Hagen Ott, Judith Fischer, and Cristina Has. Epidermolytic ichthyosis: clinical spectrum and burden of disease in a large german cohort. Journal of the European Academy of Dermatology and Venereology, 39:1028-1037, May 2025. URL: https://doi.org/10.1111/jdv.20096, doi:10.1111/jdv.20096. This article has 7 citations and is from a domain leading peer-reviewed journal.

3. (cheng2025firstsuccessfultreatment pages 3-4): Wenjie Cheng, Chaolan Pan, Zhe Sun, Peiyi Sun, Jiawen Li, Zhirong Yao, Xiaoxiao Wang, and Jia Zhang. First successful treatment of epidermolytic ichthyosis with vunakizumab: a case report. Frontiers in Immunology, May 2025. URL: https://doi.org/10.3389/fimmu.2025.1574255, doi:10.3389/fimmu.2025.1574255. This article has 4 citations and is from a peer-reviewed journal.

4. (tagoe2023chronicactivationof pages 1-5): Hephzi Tagoe, Sakinah Hassan, Gehad Youssef, Wendy Heywood, Kevin Mills, John I. Harper, and Ryan F.L. O’Shaughnessy. Chronic activation of toll-like receptor 2 induces an ichthyotic skin phenotype. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2022.06.06.494922, doi:10.1101/2022.06.06.494922. This article has 8 citations.

5. (NCT03041038 chunk 1): Amy Paller. The Efficacy and Safety of Secukinumab in Patients With Ichthyoses. Northwestern University. 2016. ClinicalTrials.gov Identifier: NCT03041038

6. (smith2019novelandrecurrent pages 1-3): F. J. D. Smith, I. M. Kreuser‐Genis, C. S. Jury, N. J. Wilson, A. Terron‐Kwiatowski, and M. Zamiri. Novel and recurrent mutations in keratin 1 cause epidermolytic ichthyosis and palmoplantar keratoderma. Clinical and Experimental Dermatology, 44:528-534, Oct 2019. URL: https://doi.org/10.1111/ced.13800, doi:10.1111/ced.13800. This article has 33 citations and is from a peer-reviewed journal.

7. (smith2019novelandrecurrent pages 5-6): F. J. D. Smith, I. M. Kreuser‐Genis, C. S. Jury, N. J. Wilson, A. Terron‐Kwiatowski, and M. Zamiri. Novel and recurrent mutations in keratin 1 cause epidermolytic ichthyosis and palmoplantar keratoderma. Clinical and Experimental Dermatology, 44:528-534, Oct 2019. URL: https://doi.org/10.1111/ced.13800, doi:10.1111/ced.13800. This article has 33 citations and is from a peer-reviewed journal.

8. (aljuwaied2024epidermolytichyperkeratosistype pages 9-10): Maitha Abdulla Aljuwaied, Waqas Saad Abdulwahha, Mays Alrim Mustafa Al Moukdad, Moza Kamil Bin Kamil Alshamsi, Sham Zain AlAbdin, Ahmed Elbarkouky, Omar El Khatib, and Salahdein Aburuz. Epidermolytic hyperkeratosis type 1 with a new heterozygous mutation in krt1 gene: a case report. GenoMed Connect, 1:1, Nov 2024. URL: https://doi.org/10.69709/genomc.2024.135001, doi:10.69709/genomc.2024.135001. This article has 0 citations.

9. (gram2025clinicalandgenetic pages 2-3): Stine Bjørn Gram, Klaus Brusgaard, Ulrikke Lei, Mette Sommerlund, Gabrielle Randskov Vinding, Sondre Olai Kjellevold Sleire, Alex Hørby Christensen, Sanne Pedersen Fast, Rasmus Bach, Anette Bygum, and Lilian Bomme Ousager. Clinical and genetic findings in patients with palmoplantar keratoderma. JAMA Dermatology, 161:157, Feb 2025. URL: https://doi.org/10.1001/jamadermatol.2024.4824, doi:10.1001/jamadermatol.2024.4824. This article has 5 citations and is from a domain leading peer-reviewed journal.

10. (gram2025clinicalandgenetic pages 1-2): Stine Bjørn Gram, Klaus Brusgaard, Ulrikke Lei, Mette Sommerlund, Gabrielle Randskov Vinding, Sondre Olai Kjellevold Sleire, Alex Hørby Christensen, Sanne Pedersen Fast, Rasmus Bach, Anette Bygum, and Lilian Bomme Ousager. Clinical and genetic findings in patients with palmoplantar keratoderma. JAMA Dermatology, 161:157, Feb 2025. URL: https://doi.org/10.1001/jamadermatol.2024.4824, doi:10.1001/jamadermatol.2024.4824. This article has 5 citations and is from a domain leading peer-reviewed journal.

11. (tagoe2023chronicactivationof pages 8-13): Hephzi Tagoe, Sakinah Hassan, Gehad Youssef, Wendy Heywood, Kevin Mills, John I. Harper, and Ryan F.L. O’Shaughnessy. Chronic activation of toll-like receptor 2 induces an ichthyotic skin phenotype. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2022.06.06.494922, doi:10.1101/2022.06.06.494922. This article has 8 citations.

12. (smith2019novelandrecurrent pages 3-5): F. J. D. Smith, I. M. Kreuser‐Genis, C. S. Jury, N. J. Wilson, A. Terron‐Kwiatowski, and M. Zamiri. Novel and recurrent mutations in keratin 1 cause epidermolytic ichthyosis and palmoplantar keratoderma. Clinical and Experimental Dermatology, 44:528-534, Oct 2019. URL: https://doi.org/10.1111/ced.13800, doi:10.1111/ced.13800. This article has 33 citations and is from a peer-reviewed journal.

13. (smith2019novelandrecurrent pages 6-7): F. J. D. Smith, I. M. Kreuser‐Genis, C. S. Jury, N. J. Wilson, A. Terron‐Kwiatowski, and M. Zamiri. Novel and recurrent mutations in keratin 1 cause epidermolytic ichthyosis and palmoplantar keratoderma. Clinical and Experimental Dermatology, 44:528-534, Oct 2019. URL: https://doi.org/10.1111/ced.13800, doi:10.1111/ced.13800. This article has 33 citations and is from a peer-reviewed journal.

14. (aljuwaied2024epidermolytichyperkeratosistype pages 2-9): Maitha Abdulla Aljuwaied, Waqas Saad Abdulwahha, Mays Alrim Mustafa Al Moukdad, Moza Kamil Bin Kamil Alshamsi, Sham Zain AlAbdin, Ahmed Elbarkouky, Omar El Khatib, and Salahdein Aburuz. Epidermolytic hyperkeratosis type 1 with a new heterozygous mutation in krt1 gene: a case report. GenoMed Connect, 1:1, Nov 2024. URL: https://doi.org/10.69709/genomc.2024.135001, doi:10.69709/genomc.2024.135001. This article has 0 citations.

15. (diociaiuti2020firstcaseof pages 1-4): Andrea Diociaiuti, Daniele Castiglia, Marialuisa Corbeddu, Roberta Rotunno, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Giovanna Zambruno, and May El Hachem. First case of krt2 epidermolytic nevus and novel clinical and genetic findings in 26 italian patients with keratinopathic ichthyoses. International Journal of Molecular Sciences, 21:7707, Oct 2020. URL: https://doi.org/10.3390/ijms21207707, doi:10.3390/ijms21207707. This article has 21 citations.

16. (cheng2025firstsuccessfultreatment pages 1-3): Wenjie Cheng, Chaolan Pan, Zhe Sun, Peiyi Sun, Jiawen Li, Zhirong Yao, Xiaoxiao Wang, and Jia Zhang. First successful treatment of epidermolytic ichthyosis with vunakizumab: a case report. Frontiers in Immunology, May 2025. URL: https://doi.org/10.3389/fimmu.2025.1574255, doi:10.3389/fimmu.2025.1574255. This article has 4 citations and is from a peer-reviewed journal.

17. (diociaiuti2020firstcaseof pages 4-5): Andrea Diociaiuti, Daniele Castiglia, Marialuisa Corbeddu, Roberta Rotunno, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Giovanna Zambruno, and May El Hachem. First case of krt2 epidermolytic nevus and novel clinical and genetic findings in 26 italian patients with keratinopathic ichthyoses. International Journal of Molecular Sciences, 21:7707, Oct 2020. URL: https://doi.org/10.3390/ijms21207707, doi:10.3390/ijms21207707. This article has 21 citations.

18. (diociaiuti2020firstcaseof pages 7-9): Andrea Diociaiuti, Daniele Castiglia, Marialuisa Corbeddu, Roberta Rotunno, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Giovanna Zambruno, and May El Hachem. First case of krt2 epidermolytic nevus and novel clinical and genetic findings in 26 italian patients with keratinopathic ichthyoses. International Journal of Molecular Sciences, 21:7707, Oct 2020. URL: https://doi.org/10.3390/ijms21207707, doi:10.3390/ijms21207707. This article has 21 citations.

19. (tagoe2023chronicactivationof pages 13-17): Hephzi Tagoe, Sakinah Hassan, Gehad Youssef, Wendy Heywood, Kevin Mills, John I. Harper, and Ryan F.L. O’Shaughnessy. Chronic activation of toll-like receptor 2 induces an ichthyotic skin phenotype. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2022.06.06.494922, doi:10.1101/2022.06.06.494922. This article has 8 citations.

20. (diociaiuti2020firstcaseof pages 12-14): Andrea Diociaiuti, Daniele Castiglia, Marialuisa Corbeddu, Roberta Rotunno, Sabrina Rossi, Elisa Pisaneschi, Claudia Cesario, Angelo Giuseppe Condorelli, Giovanna Zambruno, and May El Hachem. First case of krt2 epidermolytic nevus and novel clinical and genetic findings in 26 italian patients with keratinopathic ichthyoses. International Journal of Molecular Sciences, 21:7707, Oct 2020. URL: https://doi.org/10.3390/ijms21207707, doi:10.3390/ijms21207707. This article has 21 citations.

21. (sussmuth2026defininghistologicalpatterns pages 18-20): Kira Süßmuth, Vinzenz Oji, Jacqueline Bodes, Isabelle Jochum, Florian Muhs, Katalin Komlosi, Ingrid Hausser, Matthias Schmuth, Heiko Traupe, Judith Fischer, and Dieter Metze. Defining histological patterns in inherited ichthyoses: toward a diagnostic algorithm based on 66 confirmed cases. Dermatopathology, 13:9, Feb 2026. URL: https://doi.org/10.3390/dermatopathology13010009, doi:10.3390/dermatopathology13010009. This article has 0 citations.

22. (sussmuth2026defininghistologicalpatterns pages 25-27): Kira Süßmuth, Vinzenz Oji, Jacqueline Bodes, Isabelle Jochum, Florian Muhs, Katalin Komlosi, Ingrid Hausser, Matthias Schmuth, Heiko Traupe, Judith Fischer, and Dieter Metze. Defining histological patterns in inherited ichthyoses: toward a diagnostic algorithm based on 66 confirmed cases. Dermatopathology, 13:9, Feb 2026. URL: https://doi.org/10.3390/dermatopathology13010009, doi:10.3390/dermatopathology13010009. This article has 0 citations.

23. (cheng2025firstsuccessfultreatment pages 4-5): Wenjie Cheng, Chaolan Pan, Zhe Sun, Peiyi Sun, Jiawen Li, Zhirong Yao, Xiaoxiao Wang, and Jia Zhang. First successful treatment of epidermolytic ichthyosis with vunakizumab: a case report. Frontiers in Immunology, May 2025. URL: https://doi.org/10.3389/fimmu.2025.1574255, doi:10.3389/fimmu.2025.1574255. This article has 4 citations and is from a peer-reviewed journal.

24. (NCT04549792 chunk 2): Amy Paller. An Open-Label and Long-Term Extension Study to Evaluate the Efficacy and Safety of Ustekinumab in the Treatment of Patients With Ichthyoses. Northwestern University. 2021. ClinicalTrials.gov Identifier: NCT04549792

25. (NCT03041038 chunk 2): Amy Paller. The Efficacy and Safety of Secukinumab in Patients With Ichthyoses. Northwestern University. 2016. ClinicalTrials.gov Identifier: NCT03041038

26. (gram2025clinicalandgenetic pages 7-8): Stine Bjørn Gram, Klaus Brusgaard, Ulrikke Lei, Mette Sommerlund, Gabrielle Randskov Vinding, Sondre Olai Kjellevold Sleire, Alex Hørby Christensen, Sanne Pedersen Fast, Rasmus Bach, Anette Bygum, and Lilian Bomme Ousager. Clinical and genetic findings in patients with palmoplantar keratoderma. JAMA Dermatology, 161:157, Feb 2025. URL: https://doi.org/10.1001/jamadermatol.2024.4824, doi:10.1001/jamadermatol.2024.4824. This article has 5 citations and is from a domain leading peer-reviewed journal.

27. (tagoe2023chronicactivationof pages 17-20): Hephzi Tagoe, Sakinah Hassan, Gehad Youssef, Wendy Heywood, Kevin Mills, John I. Harper, and Ryan F.L. O’Shaughnessy. Chronic activation of toll-like receptor 2 induces an ichthyotic skin phenotype. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2022.06.06.494922, doi:10.1101/2022.06.06.494922. This article has 8 citations.

28. (tagoe2023chronicactivationof pages 20-24): Hephzi Tagoe, Sakinah Hassan, Gehad Youssef, Wendy Heywood, Kevin Mills, John I. Harper, and Ryan F.L. O’Shaughnessy. Chronic activation of toll-like receptor 2 induces an ichthyotic skin phenotype. bioRxiv, Jun 2023. URL: https://doi.org/10.1101/2022.06.06.494922, doi:10.1101/2022.06.06.494922. This article has 8 citations.