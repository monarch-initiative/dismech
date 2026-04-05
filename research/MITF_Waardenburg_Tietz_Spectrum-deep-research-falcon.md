---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:50.665036'
end_time: '2026-04-04T12:54:18.081882'
duration_seconds: 687.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MITF Waardenburg-Tietz Spectrum
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MITF Waardenburg-Tietz Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **MITF Waardenburg-Tietz Spectrum** covering all of the
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
- **Disease Name:** MITF Waardenburg-Tietz Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **MITF Waardenburg-Tietz Spectrum** covering all of the
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


# MITF Waardenburg–Tietz Spectrum (Genetic) — Comprehensive Disease Characteristics Report

**Scope and definitions used here.** “MITF Waardenburg–Tietz spectrum” is used as a practical umbrella for phenotypes caused by pathogenic variants in *MITF* (OMIM #156845) that manifest as (i) Waardenburg syndrome type 2 / type 2A (WS2/WS2A; MIM/OMIM #193510) and (ii) the allelic, generally more severe Tietz albinism–deafness syndrome (Tietz syndrome; TADS/TS; OMIM #103500). (rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2)

**Priority of evidence.** Recent (2023–2024) review/cohort sources were prioritized for current concepts and statistics; older primary studies were used for mechanistic and genotype–phenotype details when necessary. (bertanitorres2023waardenburgsyndromethe pages 1-2, buonfiglio2024comprehensiveapproachfor pages 1-2, sun2024decipheringpotentialcausative pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview

*MITF* Waardenburg–Tietz spectrum is a group of **auditory–pigmentary disorders** in which congenital (often profound) **sensorineural hearing loss** co-occurs with **pigmentary abnormalities** of the hair, skin, iris, and sometimes retinal pigment epithelium, due to pathogenic variants in the melanocyte lineage transcription factor **MITF**. (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2, guimaraes2023inheritedcausesof pages 6-11)

A key clinical discriminator within the spectrum is the **pattern of hypopigmentation**:
- **WS2/WS2A**: typically patchy pigment anomalies with variable expressivity and frequent **heterochromia iridis**; **absence of dystopia canthorum** distinguishes WS2 from WS1. (rauschendorf2019homozygousintronicmitf pages 1-3, thongpradit2020mitfvariantscause pages 2-3)
- **Tietz syndrome/TADS**: typically **generalized albinoid-like hypopigmentation** and **profound congenital bilateral sensorineural hearing loss**; individuals may be described as born “snow white” with some pigment acquisition later. (guimaraes2023inheritedcausesof pages 6-11)

### 1.2 Key identifiers and cross-references

**OMIM/MIM identifiers (from peer-reviewed sources):**
- *MITF* gene: **OMIM #156845** (rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11)
- Waardenburg syndrome type 2 / 2A: **MIM/OMIM #193510** (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2)
- Tietz syndrome / Tietz albinism-deafness syndrome: **OMIM #103500** (rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2)
- Differential/subtype context:
  - WS1: **OMIM #193500** (dystopia canthorum) (rauschendorf2019homozygousintronicmitf pages 1-3)
  - WS3: **OMIM #148820** (rauschendorf2019homozygousintronicmitf pages 1-3)
  - WS4: **OMIM #277580** (Hirschsprung disease association) (rauschendorf2019homozygousintronicmitf pages 1-3)

**MONDO / Orphanet / ICD / MeSH:** Not retrievable from the current tool evidence set; these should be added by querying MONDO/Orphanet/ICD/MeSH directly in a subsequent curation step. (Evidence limitation)

### 1.3 Synonyms / alternative names
- Waardenburg syndrome type 2A (MITF-related)
- Waardenburg syndrome type 2 (MITF subset)
- Tietz syndrome
- Tietz albinism-deafness syndrome (TADS)
- Tietz albinism–deafness syndrome / Tietz albinism-deafness (TS)
(rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2)

### 1.4 Evidence source type (individual vs aggregated)
- **Aggregated disease-level resources / reviews & cohorts**: genotype–phenotype statistics and diagnostic yields (e.g., 443 curated literature cases; 26-proband NGS cohort). (bertanitorres2023waardenburgsyndromethe pages 1-2, sun2024decipheringpotentialcausative pages 1-2)
- **Individual/family studies**: deep molecular confirmation (e.g., intronic splice variant validated by minigene assay; segregation in pedigrees). (rauschendorf2019homozygousintronicmitf pages 3-5, rauschendorf2019homozygousintronicmitf media 630e66b8)

---

## 2. Etiology

### 2.1 Disease causal factors

**Primary cause (genetic):** Pathogenic variants in *MITF* that disrupt melanocyte development and/or function, leading to pigmentary abnormalities and inner-ear melanocyte/stria vascularis dysfunction consistent with sensorineural hearing loss. (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

**Current understanding of causality and allelism:** WS2A and Tietz syndrome are described as **allelic disorders** caused by heterozygous *MITF* variants, with Tietz generally considered the more severe end (generalized hypopigmentation, profound congenital deafness). (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2, guimaraes2023inheritedcausesof pages 6-11)

### 2.2 Risk factors

**Genetic risk factors (causal variants):**
- Heterozygous *MITF* variants are a major cause of WS2A and can also cause Tietz syndrome. (thongpradit2020mitfvariantscause pages 2-3)
- Variant classes supported in evidence include:
  - **Non-truncating basic-domain variants** (often associated with WS2/Tietz overlap and variable expressivity). (leger2012novelandrecurrent pages 1-2, leger2012novelandrecurrent pages 3-4)
  - **Truncating variants** (e.g., nonsense/frameshift) reported in WS families (example: *MITF* c.1198C>T p.Arg400* segregating in a family). (buonfiglio2024comprehensiveapproachfor pages 1-2)
  - **Splice-region/intronic variants** that impair splicing and reduce functional MITF (e.g., *MITF* c.33+5G>C; intron retention and likely NMD demonstrated by minigene assays). (rauschendorf2019homozygousintronicmitf pages 3-5)
  - **Biallelic variants** can produce more severe phenotypes or different inheritance patterns (see inheritance section). (rauschendorf2019homozygousintronicmitf pages 1-3, thongpradit2020mitfvariantscause pages 2-3, rauschendorf2019homozygousintronicmitf pages 3-5)

**Environmental risk factors:** No disease-specific environmental risk factors were identified in the retrieved evidence; the condition is primarily monogenic. (Evidence limitation)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence for MITF Waardenburg–Tietz spectrum. (Evidence limitation)

### 2.4 Gene–environment interactions
No gene–environment interactions specific to this condition were identified in the retrieved evidence. (Evidence limitation)

---

## 3. Phenotypes (with ontology suggestions)

### 3.1 Core phenotype domains (current consensus)

**Auditory phenotype**
- **Congenital sensorineural hearing loss** is central for both WS2A and Tietz syndrome; Tietz is commonly described as **bilateral, congenital, profound** hearing loss with limited speech development. (guimaraes2023inheritedcausesof pages 6-11)
- In Waardenburg syndrome more broadly, WS2 is distinguished as lacking dystopia canthorum and showing deafness with pigmentary anomalies. (rauschendorf2019homozygousintronicmitf pages 1-3, bertanitorres2023waardenburgsyndromethe pages 1-2)

**Pigmentary phenotypes**
- **Iris**: blue irides and/or heterochromia iridis are common in WS2A; Tietz tends to have uniformly blue irides (without heterochromia). (thongpradit2020mitfvariantscause pages 2-3, guimaraes2023inheritedcausesof pages 6-11)
- **Skin/hair**: patchy depigmentation or white forelock/premature graying is typical for WS2A; Tietz shows generalized hypopigmentation from birth (“albinoid-like”). (leger2012novelandrecurrent pages 1-2, guimaraes2023inheritedcausesof pages 6-11)
- **Freckles**: high frequency reported in MITF basic-domain cohort and genotype–phenotype analyses point to freckles as enriched with *MITF* variants. (leger2012novelandrecurrent pages 3-4, sun2024decipheringpotentialcausative pages 1-2)

**Ocular/retinal findings**
- Tietz syndrome may show **diffuse retinal hypopigmentation** but “other ocular abnormalities (nystagmus, photophobia) are typically absent.” (guimaraes2023inheritedcausesof pages 6-11)
- MITF is also reviewed as important for retinal pigment epithelium biology and can be associated with diverse ocular phenotypes in animal models; direct translation to human MITF Waardenburg–Tietz clinical care remains limited. (garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

### 3.2 Recent (2023–2024) statistics and phenotype associations

From a 2024 clinical genetics-focused paper:
- WS accounts for **~2–5% of congenital hearing loss**. (buonfiglio2024comprehensiveapproachfor pages 1-2)
- Bilateral hearing impairment is reported as more frequent in WS2 (~**90%**), and WS2 hearing defects are described as progressive in **~70%** of cases (note: this statistic is for WS2 broadly and not restricted to MITF-only cases). (buonfiglio2024comprehensiveapproachfor pages 1-2)
- White forelock / premature graying is reported in **~one-third** of WS1/WS2 cases. (buonfiglio2024comprehensiveapproachfor pages 1-2)

From a 2024 literature-curated genotype–phenotype association analysis (443 cases):
- “**Skin freckles and premature graying of hair were more frequently observed in cases with MITF variants**.” (sun2024decipheringpotentialcausative pages 1-2)

From a MITF basic-domain cohort (older but genotype-specific):
- “**striking frequency of freckles (60%)** … mainly in Asian populations (66%).” (leger2012novelandrecurrent pages 3-4)

### 3.3 Phenotype list with suggested HPO terms

Below are high-yield phenotypes and candidate HPO mappings (terms are suggested; exact IDs should be verified against HPO):
- Sensorineural hearing loss (HP:0000407) (guimaraes2023inheritedcausesof pages 6-11, thongpradit2020mitfvariantscause pages 2-3)
- Congenital onset hearing loss (HP:0003577) (guimaraes2023inheritedcausesof pages 6-11)
- Profound hearing impairment (HP:0012719) (Tietz) (guimaraes2023inheritedcausesof pages 6-11)
- Iris heterochromia (HP:0001100) (WS2A) (thongpradit2020mitfvariantscause pages 2-3)
- Blue iris (HP:0000657) (thongpradit2020mitfvariantscause pages 2-3)
- Hypopigmentation of the skin (HP:0001010) (guimaraes2023inheritedcausesof pages 6-11)
- Patchy skin hypopigmentation (HP:0001059) (WS2A) (thongpradit2020mitfvariantscause pages 2-3)
- White forelock (HP:0002211) / Premature graying of hair (HP:0002226) (buonfiglio2024comprehensiveapproachfor pages 1-2, sun2024decipheringpotentialcausative pages 1-2)
- Freckling (HP:0001480) (leger2012novelandrecurrent pages 3-4, sun2024decipheringpotentialcausative pages 1-2)
- Retinal hypopigmentation (suggested) (guimaraes2023inheritedcausesof pages 6-11)
- Microphthalmia (HP:0000568) (not typical for classic WS2A/Tietz, but appears in porcupine model; interpret cautiously for humans) (li2024identificationofthe pages 1-2)

### 3.4 Quality-of-life impacts
The retrieved evidence does not provide disease-specific validated QoL instrument outcomes (EQ-5D/SF-36/PROMIS). However, congenital/profound hearing loss generally impacts communication and education, motivating early rehabilitation strategies; disease-specific QoL datasets should be added from dedicated hearing-loss QoL literature. (Evidence limitation)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **Causal gene:** *MITF* (OMIM #156845). (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2)
- **Gene product / role:** MITF is a **basic helix–loop–helix leucine zipper (bHLHZip)** transcription factor central to melanocyte development and melanin synthesis; it is also implicated in retinal pigment epithelium structure/function. (leger2012novelandrecurrent pages 1-2, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

### 4.2 Pathogenic variant classes and functional consequences

**Loss-of-function / haploinsufficiency vs dominant-negative:**
- WS2 has been described with **haploinsufficiency** as a plausible mechanism (reviewed in functional studies and mechanistic discussions). (guimaraes2023inheritedcausesof pages 6-11)
- For WS2A/Tietz-associated missense variants, a major mechanism is failure of MITF to bind DNA and activate melanocyte promoters: functional study summary indicates that “**Eleven of 18 WS2A and TS mutations showed no DNA-binding or transcription activation potential**.” (grill2013mitfmutationsassociated pages 7-7)

**Splicing disruption (isoform-specific):**
- A +5 donor splice-site variant (**c.33+5G>C**) can produce intron retention in MITF-M minigene assays (3.23-fold increase), consistent with reduced functional MITF-M transcript via degradation (likely NMD), and severe phenotypes in homozygotes. (rauschendorf2019homozygousintronicmitf pages 3-5)

**Post-translational regulation and a Waardenburg-linked coding variant (2023):**
- A 2023 Nature Communications paper reports that p300/CBP-mediated **acetylation at MITF K206** reduces MITF residence time and shifts DNA-binding preference away from differentiation-associated CATGTG motifs toward CACGTG elements, and states that this mechanism provides “**a mechanistic explanation of why a human K206Q MITF mutation is associated with Waardenburg syndrome**.” (louphrasitthiphol2023acetylationreprogramsmitf pages 1-2)

### 4.3 Inheritance patterns and penetrance/expressivity

**Autosomal dominant (classic):**
- Heterozygous *MITF* variants cause WS2A and Tietz syndrome with autosomal dominant inheritance. (thongpradit2020mitfvariantscause pages 2-3, leger2012novelandrecurrent pages 1-2)
- Variable penetrance/expressivity and intrafamilial variation are emphasized for WS. (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 3-4)

**Autosomal recessive / biallelic effects (expanded mechanisms):**
- *MITF* can cause **autosomal recessive nonsyndromic sensorineural hearing loss** in some families with biallelic variants, with heterozygotes asymptomatic in that context. (thongpradit2020mitfvariantscause pages 2-3)
- Homozygous/splice-region MITF variant can cause **more severe WS2A** phenotype compared with heterozygotes, illustrating dosage effects. (rauschendorf2019homozygousintronicmitf pages 3-5)

### 4.4 Modifier genes / genetic interactions
- A genotype–phenotype analysis suggested freckles may be influenced by modifiers; **MC1R** is proposed as a candidate modifier affecting freckling/pigmentation because it upregulates MITF and influences melanin type. (leger2012novelandrecurrent pages 3-4)
- A family study discusses co-segregation of a temperature-sensitive *TYR* variant (p.R402Q) as a plausible pigmentation modifier (restoring pigment in cooler acral areas), but this is not established as a general modifier for the spectrum. (rauschendorf2019homozygousintronicmitf pages 5-7)

### 4.5 Epigenetics
No disease-specific epigenetic signatures (methylation/histone/chromatin) were identified in the retrieved evidence. (Evidence limitation)

### 4.6 Chromosomal abnormalities
No recurrent chromosomal abnormalities specific to MITF Waardenburg–Tietz spectrum were identified in the retrieved evidence; however, CNVs affecting WS genes (including *SOX10* and *PAX3*) are discussed in general WS diagnostics. (buonfiglio2024comprehensiveapproachfor pages 1-2)

### 4.7 Ontology suggestions (GO / CL)

**Candidate GO biological process terms (suggested):**
- Melanocyte differentiation; Melanocyte development; Regulation of transcription by RNA polymerase II; Melanin biosynthetic process; Neural crest cell migration/differentiation (supported conceptually by neural crest/melanocyte mechanism discussions). (bertanitorres2023waardenburgsyndromethe pages 1-2, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

**Candidate Cell Ontology (CL) terms (suggested):**
- Melanocyte; neural crest cell; retinal pigment epithelial cell (MITF role in RPE emphasized in eye review). (garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

---

## 5. Environmental Information

No specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence set; MITF Waardenburg–Tietz spectrum is primarily genetic. (Evidence limitation)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current synthesis)

1) **Upstream genetic trigger:** Pathogenic variants in *MITF* (coding, truncating, or splice-disrupting) reduce or alter MITF transcriptional activity. (grill2013mitfmutationsassociated pages 7-7, rauschendorf2019homozygousintronicmitf pages 3-5)

2) **Cellular developmental impact:** Because MITF regulates melanocyte differentiation, survival, and migration, its dysfunction results in abnormal development/function of melanocytes derived from the neural crest. (rauschendorf2019homozygousintronicmitf pages 1-3, bertanitorres2023waardenburgsyndromethe pages 1-2)

3) **Tissue-level consequences:**
- **Skin/hair/iris hypopigmentation** due to reduced melanin production and/or reduced melanocyte number/function. (thongpradit2020mitfvariantscause pages 2-3, guimaraes2023inheritedcausesof pages 6-11)
- **Sensorineural hearing loss** likely related to the requirement for melanocytes (e.g., in the stria vascularis) for normal cochlear function (supported indirectly by the classification of WS/Tietz as auditory–pigmentary syndromes and the centrality of melanocyte developmental programs). (rauschendorf2019homozygousintronicmitf pages 1-3, thongpradit2020mitfvariantscause pages 2-3)
- **Retinal/RPE hypopigmentation** and RPE functional effects are described particularly in Tietz and in animal models; MITF’s role in RPE ion transport is highlighted in a 2024 review. (guimaraes2023inheritedcausesof pages 6-11, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

### 6.2 Molecular pathways and recent mechanistic developments

**Transcriptional target selectivity via acetylation (2023):**
- MITF acetylation at K206 (p300/CBP-mediated) reduces residence time and changes motif selectivity (CATGTG → CACGTG bias), providing a mechanistic explanation linking K206Q to Waardenburg syndrome. (louphrasitthiphol2023acetylationreprogramsmitf pages 1-2)

**Splicing and isoform specificity (2019; still clinically important):**
- Intronic splice-site variants can selectively disrupt MITF-M, with intron retention and likely NMD reducing functional transcript; this highlights a practical diagnostic principle: exome-only analysis may miss pathogenic regulatory/splice variants. (rauschendorf2019homozygousintronicmitf pages 3-5)

**Suggested pathway involvement / feedback:**
- Genetic and phenotypic heterogeneity in MITF-associated WS2 has been tied to Wnt pathway regulatory feedback and interactions (in mechanistic literature on MITF regulation and phenotypic variability). (leger2012novelandrecurrent pages 3-4)

### 6.3 Molecular profiling / omics
No human disease-specific transcriptomic/proteomic/metabolomic profiles were identified in the retrieved evidence set for MITF Waardenburg–Tietz spectrum. (Evidence limitation)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue systems
- **Auditory system:** inner ear structures implicated by congenital sensorineural hearing loss. (guimaraes2023inheritedcausesof pages 6-11, thongpradit2020mitfvariantscause pages 2-3)
- **Integumentary system:** skin and hair pigmentation defects. (thongpradit2020mitfvariantscause pages 2-3, guimaraes2023inheritedcausesof pages 6-11)
- **Eye:** iris pigmentation anomalies; retinal hypopigmentation; potential RPE involvement. (guimaraes2023inheritedcausesof pages 6-11, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

### 7.2 Ontology suggestions (UBERON; suggested)
- Inner ear / cochlea; skin; hair follicle; iris; retina; retinal pigment epithelium. (garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2, guimaraes2023inheritedcausesof pages 6-11)

### 7.3 Subcellular localization (suggested)
- **Nucleus** for transcription factor activity; multiple variants affect nuclear localization or chromatin binding dynamics (e.g., K206 acetylation effects; NLS-region variants in other studies; Arg217del in animal model). (louphrasitthiphol2023acetylationreprogramsmitf pages 1-2, li2024identificationofthe pages 9-10)

---

## 8. Temporal Development

### 8.1 Onset
- **Typically congenital/early life:** Tietz syndrome is characterized by congenital profound bilateral sensorineural hearing loss and generalized hypopigmentation from birth. (guimaraes2023inheritedcausesof pages 6-11)
- WS2/WS2A commonly includes congenital hearing loss and pigment anomalies; variability exists. (thongpradit2020mitfvariantscause pages 2-3, rauschendorf2019homozygousintronicmitf pages 1-3)

### 8.2 Progression
- In WS2 (broadly), hearing defects have been described as progressive in ~70% (note: not restricted to MITF-only cases in the evidence). (buonfiglio2024comprehensiveapproachfor pages 1-2)

### 8.3 Staging
No standardized staging systems were identified in the retrieved evidence. (Evidence limitation)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- Waardenburg syndrome prevalence estimate: **~1 per 42,000**. (guimaraes2023inheritedcausesof pages 6-11)
- WS accounts for **~2–5% of congenital hearing loss** (broad WS estimate). (buonfiglio2024comprehensiveapproachfor pages 1-2)

### 9.2 Inheritance
- **Autosomal dominant** is typical for MITF-related WS2A and Tietz syndrome. (thongpradit2020mitfvariantscause pages 2-3)
- **Autosomal recessive** inheritance can occur for MITF-associated nonsyndromic hearing loss and severe biallelic presentations. (thongpradit2020mitfvariantscause pages 2-3, rauschendorf2019homozygousintronicmitf pages 3-5)

### 9.3 Penetrance and expressivity
- Variable penetrance and variable expressivity are emphasized for WS phenotypes (inter- and intrafamilial). (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 3-4)

### 9.4 Population demographics
No robust sex ratio, ethnicity-specific prevalence, or founder effect data specific to MITF Waardenburg–Tietz spectrum were identified in the retrieved evidence. (Evidence limitation)

---

## 10. Diagnostics

### 10.1 Clinical evaluation and differential diagnosis
**Clinical clues (high yield):** auditory–pigmentary phenotype with WS2 defined by absence of dystopia canthorum; generalized hypopigmentation and profound congenital hearing loss suggests Tietz syndrome. (rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11)

**Differential diagnosis:** other Waardenburg subtypes (WS1/WS3 with dystopia canthorum; WS4 with Hirschsprung disease), and other hypopigmentation/deafness syndromes. (rauschendorf2019homozygousintronicmitf pages 1-3)

### 10.2 Genetic testing approaches (real-world implementations)

**NGS-driven diagnostic workflows (2023–2024 evidence):**
- A 2023 cohort used **exome sequencing** (including trio analysis for some) and then a **targeted NGS panel** for unresolved cases; overall causative variants were found in **20/26 (77%)** probands, with *MITF* variants among the most frequent. (bertanitorres2023waardenburgsyndromethe pages 1-2)
- A 2024 study emphasizes integration of methods: **WES for SNVs**, **CNV calling from WES raw data**, and **MLPA** for CNV validation, improving diagnostic certainty and enabling tailored genetic counseling. (buonfiglio2024comprehensiveapproachfor pages 1-2)

**Critical limitation of exon-only approaches:**
- An intronic splice-site pathogenic variant (c.33+5G>C) was not found by exome coding analysis and required intronic investigation plus **functional minigene splicing assay** to confirm impact. (rauschendorf2019homozygousintronicmitf pages 3-5)

### 10.3 Diagnostic figure evidence (pedigree + splicing functional assay)
Rauschendorf et al. provide visual evidence for (i) segregation of a pathogenic intronic *MITF* variant with WS2A phenotype within a pedigree and (ii) minigene splicing disruption consistent with intron retention (functional mechanism). (rauschendorf2019homozygousintronicmitf media 630e66b8, rauschendorf2019homozygousintronicmitf media d692a364)

---

## 11. Outcome / Prognosis

No syndrome-specific survival or mortality differences were identified in the retrieved evidence. The condition is primarily defined by hearing and pigmentation phenotypes, and prognosis is largely driven by early identification and effectiveness/timing of hearing rehabilitation and educational support. (Evidence limitation; management rationale aligns with congenital hearing loss care principles.)

---

## 12. Treatment

### 12.1 Current standard management (real-world)
No disease-modifying therapy for MITF Waardenburg–Tietz spectrum was identified in the retrieved evidence set. Care is supportive and multidisciplinary.

**Hearing rehabilitation (core intervention):**
- Early audiologic evaluation and rehabilitation (hearing aids and/or cochlear implantation where appropriate), plus speech/language therapy and educational accommodations, are standard clinical implementations for severe congenital sensorineural hearing loss. (Supported indirectly by the centrality of congenital SNHL in this spectrum; disease-specific CI trials were not found.) (guimaraes2023inheritedcausesof pages 6-11)

**Dermatologic/ophthalmologic care:**
- Counseling and monitoring for pigmentary/ocular features (iris/retinal hypopigmentation); the 2023 review notes diffuse retinal hypopigmentation in Tietz, while the 2024 MITF-eye review emphasizes MITF’s importance in RPE function (suggesting ophthalmic assessment can be appropriate). (guimaraes2023inheritedcausesof pages 6-11, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

**Genetic counseling / cascade testing:**
- Recommended due to autosomal dominant inheritance with variable expressivity and possibility of mild findings in heterozygous parents; highlighted in family-based studies. (rauschendorf2019homozygousintronicmitf pages 7-10)

### 12.2 Clinical trials / experimental therapies
A ClinicalTrials.gov search using “MITF Waardenburg syndrome OR Tietz syndrome” did **not** yield relevant disease-specific interventional trials in the retrieved set; returned trials were unrelated (e.g., orthodontic). (Evidence limitation from tool result; no relevant trial context IDs for MITF were returned.)

### 12.3 MAXO suggestions (to be validated)
- Hearing aid fitting; cochlear implantation; speech therapy; genetic counseling; genetic testing. (General MAXO mapping suggestions; no MAXO IDs retrieved.)

---

## 13. Prevention

Primary prevention is not applicable for monogenic MITF Waardenburg–Tietz spectrum in the usual sense; prevention focuses on **reproductive counseling** and **early detection**.

- **Secondary prevention:** early identification of congenital hearing loss and prompt rehabilitation to improve language and developmental outcomes. (guimaraes2023inheritedcausesof pages 6-11)
- **Genetic counseling and cascade testing** in families with known variants to enable early diagnosis and reproductive planning. (rauschendorf2019homozygousintronicmitf pages 7-10)

---

## 14. Other Species / Natural Disease

### 14.1 Naturally occurring non-human disease/models relevant to MITF auditory–pigmentary phenotypes

A 2024 Scientific Reports paper describes a **naturally occurring porcupine model** with Mitf **c.875_877delGAA p.(Arg217del)** associated with hypopigmentation and congenital deafness and explicitly frames it as reminiscent of human WS2. (Publication date: Dec 2024; URL: https://doi.org/10.1038/s41598-024-82975-7) (li2024identificationofthe pages 1-2)

The paper includes a detailed ABR methodology (0.5–32 kHz, stepwise attenuation to threshold) and BSA-based mapping (88 SNP and 336 InDel candidate sites), validated by Sanger sequencing. (li2024identificationofthe pages 2-3, li2024identificationofthe pages 1-2)

---

## 15. Model Organisms

### 15.1 Mouse models
A 2024 review summarizes numerous mouse *Mitf* mutations and highlights their relevance to hypopigmentation and ocular phenotypes, emphasizing MITF’s roles in the retinal pigment epithelium and ocular physiology. (Publication date: Sep 2024; URL: https://doi.org/10.3390/genes15101258) (garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2)

### 15.2 Porcupine model (2024)
The naturally occurring porcupine Mitf Arg217del model provides an additional system for studying congenital deafness and pigmentary disorders with an MITF lesion analogous to human recurrent variants in the spectrum. (li2024identificationofthe pages 1-2)

### 15.3 Model limitations
- Many mechanistic data are derived from cancer biology or animal ocular phenotypes and may not directly capture the human congenital auditory–pigmentary phenotype. (garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2, louphrasitthiphol2023acetylationreprogramsmitf pages 1-2)

---

# Recent developments and expert analysis (2023–2024 highlights)

1) **Integrated genomic diagnostics is now routine for WS**: 2023–2024 cohort work emphasizes WES/panels, trio sequencing, and CNV calling/MLPA as practical clinical workflows, achieving high diagnostic yields (e.g., 77% in one cohort). (bertanitorres2023waardenburgsyndromethe pages 1-2, buonfiglio2024comprehensiveapproachfor pages 1-2)

2) **Computational multi-data integration is being used to resolve undiagnosed WS**: A 2024 Orphanet Journal of Rare Diseases paper combined protein interaction networks and phenotype similarity and analyzed 443 curated cases, finding genotype–phenotype patterns (e.g., MITF variants enriched for freckles and premature graying). (sun2024decipheringpotentialcausative pages 1-2)

3) **Mechanistic precision is increasing for specific variants**: A 2023 Nature Communications study provides a mechanistic framework for how MITF acetylation at K206 changes binding selectivity and may explain disease association of K206Q with Waardenburg syndrome. (louphrasitthiphol2023acetylationreprogramsmitf pages 1-2)

4) **New natural models for MITF auditory–pigmentary phenotypes**: 2024 work reports naturally occurring Mitf Arg217del in porcupines, with ABR-confirmed deafness and hypopigmentation, supporting cross-species conservation of MITF-dependent pigment/hearing biology. (li2024identificationofthe pages 1-2, li2024identificationofthe pages 2-3)

---

# Visual evidence (from primary literature)

The pedigree/phenotype segregation and splicing functional assay supporting an intronic MITF pathogenic mechanism in WS2A is shown in Rauschendorf et al. (Figure panels extracted). (rauschendorf2019homozygousintronicmitf media 630e66b8, rauschendorf2019homozygousintronicmitf media d692a364)

---

# Summary table

| Entity | Key identifiers (OMIM/MIM numbers) | Core clinical features (hearing, pigmentation, ocular) | Inheritance | Notes / diagnostic clues / statistics |
|---|---|---|---|---|
| Waardenburg syndrome type 2 / 2A (MITF-related subset) | WS2 MIM/OMIM #193510; WS2A is the MITF-associated WS2 subtype; MITF OMIM #156845 (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2, bertanitorres2023waardenburgsyndromethe pages 1-2, buonfiglio2024comprehensiveapproachfor pages 1-2) | Congenital sensorineural hearing loss; pigmentary abnormalities of hair, skin, and iris; absence of dystopia canthorum distinguishes WS2 from WS1; ocular findings can include blue irides and heterochromia iridis (rauschendorf2019homozygousintronicmitf pages 1-3, thongpradit2020mitfvariantscause pages 1-2, thongpradit2020mitfvariantscause pages 2-3, bertanitorres2023waardenburgsyndromethe pages 1-2) | Usually autosomal dominant due to heterozygous MITF variants; variable penetrance and expressivity; rare biallelic MITF cases can be more severe or present differently (rauschendorf2019homozygousintronicmitf pages 1-3, thongpradit2020mitfvariantscause pages 1-2, thongpradit2020mitfvariantscause pages 2-3, rauschendorf2019homozygousintronicmitf pages 3-5) | WS prevalence ~1/42,000; WS accounts for ~2–5% of congenital hearing loss; bilateral hearing impairment is more frequent in WS2 (~90%); hearing defects in WS2 are reported as progressive in ~70%; white forelock/premature graying occurs in about one-third of WS1/WS2 cases; freckles and premature graying are more frequent with MITF variants; in a basic-domain MITF cohort, freckles occurred in 60% overall (66% in Asian patients) (guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 3-4, bertanitorres2023waardenburgsyndromethe pages 1-2, buonfiglio2024comprehensiveapproachfor pages 1-2, sun2024decipheringpotentialcausative pages 1-2) |
| Tietz syndrome / Tietz albinism-deafness syndrome (TADS/TS) | Tietz syndrome / TADS OMIM #103500; MITF OMIM #156845 (rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2) | Congenital, bilateral, profound sensorineural hearing loss; generalized hypopigmentation/albinoid phenotype with fair skin, blonde-to-white hair, white eyebrows/eyelashes; blue eyes and diffuse retinal hypopigmentation; typically no nystagmus or photophobia reported (guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2, thongpradit2020mitfvariantscause pages 2-3) | Autosomal dominant; typically caused by heterozygous MITF variants; considered allelic with MITF-related WS2A and generally more severe in pigmentation/hearing phenotype (rauschendorf2019homozygousintronicmitf pages 1-3, guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2) | Clinical overlap with WS2A, but Tietz is usually distinguished by generalized rather than patchy depigmentation, uniformly blue irides rather than heterochromia, and profound congenital deafness; patients may be described as born “snow white” with some later pigment gain (guimaraes2023inheritedcausesof pages 6-11, leger2012novelandrecurrent pages 1-2) |
| MITF gene | MITF OMIM #156845; microphthalmia-associated transcription factor; bHLH-leucine zipper / bHLHZip transcription factor (rauschendorf2019homozygousintronicmitf pages 1-3, leger2012novelandrecurrent pages 1-2, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2, guimaraes2023inheritedcausesof pages 6-11) | Governs melanocyte differentiation, growth, survival, migration, melanin synthesis, and contributes to retinal pigment epithelium biology and ion transport; pathogenic variants can cause WS2A, Tietz syndrome, and in some contexts recessive nonsyndromic sensorineural hearing loss (rauschendorf2019homozygousintronicmitf pages 1-3, thongpradit2020mitfvariantscause pages 1-2, garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2, rauschendorf2019homozygousintronicmitf pages 3-5) | Dominant for classic MITF-related WS2A/Tietz presentations; recessive inheritance reported for some MITF-associated nonsyndromic hearing loss and severe biallelic syndromic presentations (thongpradit2020mitfvariantscause pages 1-2, thongpradit2020mitfvariantscause pages 2-3, rauschendorf2019homozygousintronicmitf pages 3-5) | Diagnostic workup increasingly uses NGS/WES with targeted panels, trio analysis when possible, CNV calling from exome data, and MLPA for validation; in a 2023 Brazilian WS cohort, causative variants were found in 20/26 probands (77%), including 8 MITF variants; intronic/splice-region variants may be missed by exon-focused analysis and may require functional assays such as minigene splicing studies (bertanitorres2023waardenburgsyndromethe pages 1-2, buonfiglio2024comprehensiveapproachfor pages 1-2, rauschendorf2019homozygousintronicmitf pages 3-5) |


*Table: This table summarizes the MITF-related Waardenburg–Tietz spectrum, including WS2/WS2A, Tietz syndrome, and the MITF gene itself. It compiles identifiers, hallmark clinical features, inheritance, and high-yield diagnostic statistics supported by the gathered evidence.*

---

# Direct abstract quotes (supporting key statements)

- On Tietz syndrome core phenotype: described as “**characterised by congenital sensorineural hearing loss and generalised loss of pigmentation**” (review of inherited dual sensory impairment). (guimaraes2023inheritedcausesof pages 6-11)
- On WS2 genetics and NGS diagnostic yield: In a 26-proband cohort, causative variants were detected in **20/26** and WS2 is “**typically caused by pathogenic heterozygous variants in MITF and SOX10** …” (abstract-derived content). (bertanitorres2023waardenburgsyndromethe pages 1-2)

(Additional quotes are embedded as exact phrases within evidence summaries above where provided by the extracted evidence text.)

---

# Key evidence gaps for knowledge-base completion

- MONDO, Orphanet, ICD-10/ICD-11, and MeSH identifiers were not retrieved in the current evidence set.
- Disease-specific QoL metrics, survival/mortality statistics, and controlled treatment outcome studies specific to MITF-related WS2A/Tietz were not identified.
- Environmental risk/protective factors and gene–environment interactions are not supported by the retrieved evidence.

These gaps are best addressed by direct queries to MONDO/Orphanet/ICD/MeSH resources and targeted searches for guideline documents and otology/rehabilitation outcome cohorts stratified by *MITF* genotype.


References

1. (rauschendorf2019homozygousintronicmitf pages 1-3): Marc‐Alexander Rauschendorf, Andreas D. Zimmer, Astrid Laut, Philipp Demmer, Bernd Rösler, Rudolf Happle, Silvina Sartori, and Judith Fischer. Homozygous intronic mitf mutation causes severe waardenburg syndrome type 2a. Pigment Cell & Melanoma Research, 32:85-91, Sep 2019. URL: https://doi.org/10.1111/pcmr.12733, doi:10.1111/pcmr.12733. This article has 16 citations and is from a domain leading peer-reviewed journal.

2. (guimaraes2023inheritedcausesof pages 6-11): Thales Antonio Cabral de Guimaraes, Elizabeth Arram, Ahmed F Shakarchi, Michalis Georgiou, and Michel Michaelides. Inherited causes of combined vision and hearing loss: clinical features and molecular genetics. British Journal of Ophthalmology, 107:1403-1414, Sep 2023. URL: https://doi.org/10.1136/bjo-2022-321790, doi:10.1136/bjo-2022-321790. This article has 30 citations and is from a highest quality peer-reviewed journal.

3. (leger2012novelandrecurrent pages 1-2): Sandy Léger, Xavier Balguerie, Alice Goldenberg, Valérie Drouin-Garraud, Annick Cabot, Isabelle Amstutz-Montadert, Paul Young, Pascal Joly, Virginie Bodereau, Muriel Holder-Espinasse, Robyn V Jamieson, Amanda Krause, Hongsheng Chen, Clarisse Baumann, Luis Nunes, Hélène Dollfus, Michel Goossens, and Véronique Pingault. Novel and recurrent non-truncating mutations of the mitf basic domain: genotypic and phenotypic variations in waardenburg and tietz syndromes. European Journal of Human Genetics, 20:584-587, Jan 2012. URL: https://doi.org/10.1038/ejhg.2011.234, doi:10.1038/ejhg.2011.234. This article has 50 citations and is from a domain leading peer-reviewed journal.

4. (bertanitorres2023waardenburgsyndromethe pages 1-2): William Bertani-Torres, Karina Lezirovitz, Danillo Alencar-Coutinho, Eliete Pardono, Silvia Souza da Costa, Larissa do Nascimento Antunes, Judite de Oliveira, Paulo Alberto Otto, Véronique Pingault, and Regina Célia Mingroni-Netto. Waardenburg syndrome: the contribution of next-generation sequencing to the identification of novel causative variants. Audiology Research, 14:9-25, Dec 2023. URL: https://doi.org/10.3390/audiolres14010002, doi:10.3390/audiolres14010002. This article has 7 citations.

5. (buonfiglio2024comprehensiveapproachfor pages 1-2): Paula Inés Buonfiglio, Agustín Izquierdo, Mariela Vanina Pace, Sofia Grinberg, Vanesa Lotersztein, Paloma Brun, Carlos David Bruque, Ana Belén Elgoyhen, and Viviana Dalamón. Comprehensive approach for the genetic diagnosis of patients with waardenburg syndrome. Journal of Personalized Medicine, 14:906, Aug 2024. URL: https://doi.org/10.3390/jpm14090906, doi:10.3390/jpm14090906. This article has 5 citations.

6. (sun2024decipheringpotentialcausative pages 1-2): Fengying Sun, Minmin Xiao, Dong Ji, Feng Zheng, and Tieliu Shi. Deciphering potential causative factors for undiagnosed waardenburg syndrome through multi-data integration. Orphanet Journal of Rare Diseases, Jun 2024. URL: https://doi.org/10.1186/s13023-024-03220-y, doi:10.1186/s13023-024-03220-y. This article has 3 citations and is from a peer-reviewed journal.

7. (thongpradit2020mitfvariantscause pages 2-3): Supranee Thongpradit, Natini Jinawath, Asif Javed, Saisuda Noojarern, Arthaporn Khongkraparn, Thipwimol Tim-Aroon, Krisna Lertsukprasert, Bhoom Suktitipat, Laran T. Jensen, and Duangrurdee Wattanasirichaigoon. Mitf variants cause nonsyndromic sensorineural hearing loss with autosomal recessive inheritance. Scientific Reports, Jul 2020. URL: https://doi.org/10.1038/s41598-020-69633-4, doi:10.1038/s41598-020-69633-4. This article has 29 citations and is from a peer-reviewed journal.

8. (rauschendorf2019homozygousintronicmitf pages 3-5): Marc‐Alexander Rauschendorf, Andreas D. Zimmer, Astrid Laut, Philipp Demmer, Bernd Rösler, Rudolf Happle, Silvina Sartori, and Judith Fischer. Homozygous intronic mitf mutation causes severe waardenburg syndrome type 2a. Pigment Cell & Melanoma Research, 32:85-91, Sep 2019. URL: https://doi.org/10.1111/pcmr.12733, doi:10.1111/pcmr.12733. This article has 16 citations and is from a domain leading peer-reviewed journal.

9. (rauschendorf2019homozygousintronicmitf media 630e66b8): Marc‐Alexander Rauschendorf, Andreas D. Zimmer, Astrid Laut, Philipp Demmer, Bernd Rösler, Rudolf Happle, Silvina Sartori, and Judith Fischer. Homozygous intronic mitf mutation causes severe waardenburg syndrome type 2a. Pigment Cell & Melanoma Research, 32:85-91, Sep 2019. URL: https://doi.org/10.1111/pcmr.12733, doi:10.1111/pcmr.12733. This article has 16 citations and is from a domain leading peer-reviewed journal.

10. (garciallorca2024themicrophthalmiaassociatedtranscription pages 1-2): Andrea García-Llorca and Thor Eysteinsson. The microphthalmia-associated transcription factor (mitf) and its role in the structure and function of the eye. Genes, 15:1258, Sep 2024. URL: https://doi.org/10.3390/genes15101258, doi:10.3390/genes15101258. This article has 7 citations.

11. (leger2012novelandrecurrent pages 3-4): Sandy Léger, Xavier Balguerie, Alice Goldenberg, Valérie Drouin-Garraud, Annick Cabot, Isabelle Amstutz-Montadert, Paul Young, Pascal Joly, Virginie Bodereau, Muriel Holder-Espinasse, Robyn V Jamieson, Amanda Krause, Hongsheng Chen, Clarisse Baumann, Luis Nunes, Hélène Dollfus, Michel Goossens, and Véronique Pingault. Novel and recurrent non-truncating mutations of the mitf basic domain: genotypic and phenotypic variations in waardenburg and tietz syndromes. European Journal of Human Genetics, 20:584-587, Jan 2012. URL: https://doi.org/10.1038/ejhg.2011.234, doi:10.1038/ejhg.2011.234. This article has 50 citations and is from a domain leading peer-reviewed journal.

12. (li2024identificationofthe pages 1-2): Kang Li, Chunmao Huo, Hong Long, Ketong Tang, and Shibin Zhang. Identification of the mitf gene mutation causing congenital deafness and pigmentation disorders in porcupines using bsa-seq. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-82975-7, doi:10.1038/s41598-024-82975-7. This article has 0 citations and is from a peer-reviewed journal.

13. (grill2013mitfmutationsassociated pages 7-7): Christine Grill, Kristín Bergsteinsdóttir, Margrét H. Ögmundsdóttir, Vivian Pogenberg, Alexander Schepsky, Matthias Wilmanns, Veronique Pingault, and Eiríkur Steingrímsson. Mitf mutations associated with pigment deficiency syndromes and melanoma have different effects on protein function. Human molecular genetics, 22 21:4357-67, Nov 2013. URL: https://doi.org/10.1093/hmg/ddt285, doi:10.1093/hmg/ddt285. This article has 88 citations and is from a domain leading peer-reviewed journal.

14. (louphrasitthiphol2023acetylationreprogramsmitf pages 1-2): Pakavarin Louphrasitthiphol, Alessia Loffreda, Vivian Pogenberg, Sarah Picaud, Alexander Schepsky, Hans Friedrichsen, Zhiqiang Zeng, Anahita Lashgari, Benjamin Thomas, E. Elizabeth Patton, Matthias Wilmanns, Panagis Filippakopoulos, Jean-Philippe Lambert, Eiríkur Steingrímsson, Davide Mazza, and Colin R. Goding. Acetylation reprograms mitf target selectivity and residence time. Nature Communications, Sep 2023. URL: https://doi.org/10.1038/s41467-023-41793-7, doi:10.1038/s41467-023-41793-7. This article has 20 citations and is from a highest quality peer-reviewed journal.

15. (rauschendorf2019homozygousintronicmitf pages 5-7): Marc‐Alexander Rauschendorf, Andreas D. Zimmer, Astrid Laut, Philipp Demmer, Bernd Rösler, Rudolf Happle, Silvina Sartori, and Judith Fischer. Homozygous intronic mitf mutation causes severe waardenburg syndrome type 2a. Pigment Cell & Melanoma Research, 32:85-91, Sep 2019. URL: https://doi.org/10.1111/pcmr.12733, doi:10.1111/pcmr.12733. This article has 16 citations and is from a domain leading peer-reviewed journal.

16. (li2024identificationofthe pages 9-10): Kang Li, Chunmao Huo, Hong Long, Ketong Tang, and Shibin Zhang. Identification of the mitf gene mutation causing congenital deafness and pigmentation disorders in porcupines using bsa-seq. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-82975-7, doi:10.1038/s41598-024-82975-7. This article has 0 citations and is from a peer-reviewed journal.

17. (rauschendorf2019homozygousintronicmitf media d692a364): Marc‐Alexander Rauschendorf, Andreas D. Zimmer, Astrid Laut, Philipp Demmer, Bernd Rösler, Rudolf Happle, Silvina Sartori, and Judith Fischer. Homozygous intronic mitf mutation causes severe waardenburg syndrome type 2a. Pigment Cell & Melanoma Research, 32:85-91, Sep 2019. URL: https://doi.org/10.1111/pcmr.12733, doi:10.1111/pcmr.12733. This article has 16 citations and is from a domain leading peer-reviewed journal.

18. (rauschendorf2019homozygousintronicmitf pages 7-10): Marc‐Alexander Rauschendorf, Andreas D. Zimmer, Astrid Laut, Philipp Demmer, Bernd Rösler, Rudolf Happle, Silvina Sartori, and Judith Fischer. Homozygous intronic mitf mutation causes severe waardenburg syndrome type 2a. Pigment Cell & Melanoma Research, 32:85-91, Sep 2019. URL: https://doi.org/10.1111/pcmr.12733, doi:10.1111/pcmr.12733. This article has 16 citations and is from a domain leading peer-reviewed journal.

19. (li2024identificationofthe pages 2-3): Kang Li, Chunmao Huo, Hong Long, Ketong Tang, and Shibin Zhang. Identification of the mitf gene mutation causing congenital deafness and pigmentation disorders in porcupines using bsa-seq. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-82975-7, doi:10.1038/s41598-024-82975-7. This article has 0 citations and is from a peer-reviewed journal.

20. (thongpradit2020mitfvariantscause pages 1-2): Supranee Thongpradit, Natini Jinawath, Asif Javed, Saisuda Noojarern, Arthaporn Khongkraparn, Thipwimol Tim-Aroon, Krisna Lertsukprasert, Bhoom Suktitipat, Laran T. Jensen, and Duangrurdee Wattanasirichaigoon. Mitf variants cause nonsyndromic sensorineural hearing loss with autosomal recessive inheritance. Scientific Reports, Jul 2020. URL: https://doi.org/10.1038/s41598-020-69633-4, doi:10.1038/s41598-020-69633-4. This article has 29 citations and is from a peer-reviewed journal.