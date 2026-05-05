---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T16:49:03.237026'
end_time: '2026-05-05T17:11:37.358828'
duration_seconds: 1354.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Segmental arterial mediolysis
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Segmental arterial mediolysis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Segmental arterial mediolysis** covering all of the
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
- **Disease Name:** Segmental arterial mediolysis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Segmental arterial mediolysis** covering all of the
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


## Segmental Arterial Mediolysis (SAM): Comprehensive Disease Characteristics Report

### 1. Disease Information

**Concise overview / definition.** Segmental arterial mediolysis (SAM) is a rare, nonatherosclerotic and noninflammatory arteriopathy characterized by degeneration/lysis of the arterial media that predisposes to dissection, aneurysm formation, stenosis/occlusion, and potentially catastrophic hemorrhage, most commonly in medium- to large-caliber visceral (splanchnic) arteries. (bombardieri2024segmentalarterialmediolysis pages 2-3, bombardieri2024segmentalarterialmediolysis pages 3-4, bombardieri2024segmentalarterialmediolysis pages 1-2)

Recent case-based reviews reiterate that SAM is “an uncommon, nonatherosclerotic, noninflammatory, large- to medium-sized arteriopathy” with a predilection for splanchnic branches and a clinical spectrum from incidental findings to life-threatening abdominal hemorrhage and shock. (bombardieri2024segmentalarterialmediolysis pages 1-2)

**Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO).** In the retrieved full-text evidence corpus, explicit OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO identifiers were **not stated**; therefore they are reported here as *not found in evidence* rather than inferred. (naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 1-2)

**Synonyms / alternative names.** The dominant synonym is the abbreviation **SAM**. The entity is also commonly described using class labels such as “non-inflammatory vasculopathy” or “nonatherosclerotic, noninflammatory arteriopathy,” but these are descriptive rather than formal alternative disease names. (najmaoui2023segmentalarterialmediolysis pages 3-5, bombardieri2024segmentalarterialmediolysis pages 1-2)

**Evidence source type.** Most SAM knowledge is derived from aggregated disease-level evidence (retrospective cohorts, systematic reviews, and case reports/series). Major aggregated sources in this corpus include a 111-patient imaging cohort (Naidu 2018) and a 117-patient natural-history/management cohort (Peng 2019), as well as a systematic review of 143 cases (Skeik 2019). (naidu2018segmentalarterialmediolysis pages 1-1, peng2019naturalhistoryand pages 1-2, skeik2019segmentalarterialmediolysis pages 1-2)

| Disease name | Synonyms / alternative names | MeSH term | ICD-10 / ICD-11 | Orphanet ID | MONDO ID | Notes on source type |
|---|---|---|---|---|---|---|
| Segmental arterial mediolysis | Segmental arterial mediolysis; SAM; segmental arterial mediolysis (SAM) | Not found in retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Disease name and abbreviation are consistently used in primary literature and reviews; retrieved corpus did not provide ontology/code identifiers, so these are marked as not found in evidence rather than inferred (bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5, hirose2024gallbladderhemorrhageassociated pages 4-6, bombardieri2024segmentalarterialmediolysis pages 1-2, naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 1-2) |
| Segmental arterial mediolysis | Segmental arterial mediolysis; SAM; noninflammatory vasculopathy; nonatherosclerotic, noninflammatory arteriopathy | Not found in retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Reviews describe SAM as a rare "non-inflammatory" or "nonatherosclerotic, noninflammatory" vasculopathy/arteriopathy; these are descriptive class labels rather than formal synonyms or ontology identifiers (bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5, najmaoui2023segmentalarterialmediolysis pages 1-3, bombardieri2024segmentalarterialmediolysis pages 1-2, skeik2019segmentalarterialmediolysis pages 1-2) |
| Segmental arterial mediolysis | Earlier descriptive/pathologic labels preceding or surrounding current terminology were referenced historically in review text, but no alternative controlled-vocabulary identifier was explicitly supplied in the retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Not found in retrieved evidence | Source base is literature-derived rather than ontology-derived; identifiers such as MeSH, ICD, Orphanet, and MONDO were not explicitly reported in the retrieved papers/case reviews available here (hirose2024gallbladderhemorrhageassociated pages 4-6, slavin2009segmentalarterialmediolysis pages 1-2, slavin2009segmentalarterialmediolysis pages 2-3) |


*Table: This table summarizes the disease name, commonly used synonyms, and the absence of explicit ontology or coding identifiers in the retrieved evidence for segmental arterial mediolysis. It is useful for knowledge-base curation because it distinguishes literature-supported naming from identifiers that were not directly documented in the available sources.*

---

### 2. Etiology

#### Disease causal factors (current understanding)
SAM is widely treated as an **idiopathic** arteriopathy with a **putative vasospastic** trigger and characteristic medial injury rather than primary arteritis. Slavin’s pathologic-radiologic synthesis frames SAM as a “putative vasospastic disorder” causing life-threatening hemorrhages and specific angiographic patterns. (slavin2009segmentalarterialmediolysis pages 1-2)

Peng et al. describe SAM as a “poorly understood nonatherosclerotic, noninflammatory disease due to vacuolization of the arterial media,” and their management recommendations are built around vascular risk control rather than immunosuppression. (peng2019naturalhistoryand pages 7-9)

#### Risk factors (human observational evidence)
Across large series and systematic review synthesis, commonly reported comorbidities include **hypertension** and **tobacco use**:
- In Naidu’s 111-patient cohort, hypertension occurred in 50% and smoking history in 33%. (naidu2018segmentalarterialmediolysis pages 2-3)
- In Skeik’s 143-case synthesis, hypertension was 42.7% and tobacco use 11.9%. (skeik2019segmentalarterialmediolysis pages 4-5)

These are best interpreted as *associated comorbidities* rather than established causal risk factors.

#### Environmental/iatrogenic factors and protective factors
A 2023 review emphasizes experimental and mechanistic plausibility for **vasoconstrictive exposures** and recommends **avoidance of vasoconstrictors such as tobacco, cocaine, and pseudoephedrine**, framing these as potentially relevant triggers in a vasospastic/local hypoxemia model. (najmaoui2023segmentalarterialmediolysis pages 3-5)

**Protective factors** were not explicitly identified in the retrieved evidence.

#### Gene–environment interaction
No gene–environment interaction evidence specific to SAM was identified in the retrieved corpus.

---

### 3. Phenotypes

SAM most commonly presents with acute abdominal pain and can manifest with hemorrhage, shock, and ischemic organ injury due to dissection/thrombosis/occlusion.

Major phenotype frequencies from large cohorts/reviews are summarized below.

| Phenotype | Suggested HPO term | Phenotype type | Typical onset/course in SAM | Approximate frequency / quantitative data | Evidence type | Key source citation |
|---|---|---|---|---|---|---|
| Abdominal pain | HP:0002027 Abdominal pain | Symptom | Usually acute or abrupt adult-onset presentation; may be episodic or resolve with stabilization/regression of arterial lesions | 69.2% in Peng 2019 cohort; 74% in Naidu 2018 cohort; 79.7% in Skeik 2019 systematic review; pooled review range 69.2-82% (peng2019naturalhistoryand pages 1-2, naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5) | Cohort, systematic review, review | (naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 1-2) |
| Flank pain | HP:0032508 Flank pain | Symptom | Acute adult-onset, often associated with renal artery involvement or renal infarction | 21% in Naidu 2018; grouped with abdominal/flank pain in Skeik 2019 79.7% (naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 4-5) | Cohort, systematic review | (naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 4-5) |
| Back pain | HP:0003418 Back pain | Symptom | Acute adult-onset; less common than abdominal pain | 9% in Naidu 2018; included in broad presentation spectrum in reviews (naidu2018segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5) | Cohort, review | (naidu2018segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5) |
| Intra-abdominal hemorrhage / hematoma | HP:0002246 Hemoperitoneum; HP:0011890 Abnormality of the abdomen by imaging study | Clinical sign / complication | Often sudden, severe, potentially life-threatening; may require urgent endovascular or surgical treatment | Intra-abdominal bleeding 49.7% in Skeik 2019; hemorrhage 8.5% in Peng 2019; hematoma 9% at presentation in Naidu 2018; rupture 45.5% in Skeik tabulation (skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 5-7, peng2019naturalhistoryand pages 1-2, naidu2018segmentalarterialmediolysis pages 3-4) | Systematic review, cohort | (skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 5-7, peng2019naturalhistoryand pages 1-2, naidu2018segmentalarterialmediolysis pages 3-4) |
| Hemodynamic shock | HP:0031273 Shock | Clinical sign / complication | Hyperacute catastrophic presentation, usually with rupture/major hemorrhage | 4.2% in Skeik 2019; pooled review estimate 4.2% hemorrhagic shock; older reports cited mortality up to 50% in ruptured cases (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, togawa2023intraabdominalbleedingdue pages 3-4) | Systematic review, review | (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, togawa2023intraabdominalbleedingdue pages 3-4) |
| End-organ ischemia / infarction | HP:0011025 Ischemia; HP:0006510 Renal infarction; HP:0100515 Splenic infarction; HP:0002574 Bowel ischemia | Clinical sign / imaging finding / complication | Acute adult-onset; results from dissection, thrombosis, stenosis, or occlusion; may improve or leave permanent injury | End-organ ischemia/infarction 34% in Naidu 2018; 41.9% in Peng 2019; case reports/reviews describe renal, splenic, and bowel ischemia/infarction (naidu2018segmentalarterialmediolysis pages 3-4, peng2019naturalhistoryand pages 1-2, najmaoui2023segmentalarterialmediolysis pages 3-5, najmaoui2023segmentalarterialmediolysis pages 1-3) | Cohort, review, case report | (naidu2018segmentalarterialmediolysis pages 3-4, peng2019naturalhistoryand pages 1-2, najmaoui2023segmentalarterialmediolysis pages 3-5, najmaoui2023segmentalarterialmediolysis pages 1-3) |
| Hematuria | HP:0000790 Hematuria | Symptom / sign | Usually acute, secondary to renal infarction or renal arterial involvement; uncommon but recognized | Reported as part of SAM presentation spectrum in reviews/case literature; no robust pooled percentage in major cohorts available from extracted evidence (bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5) | Review, case-based review | (bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5) |
| Gastrointestinal bleeding (melena/hematochezia/hemobilia) | HP:0002573 Gastrointestinal hemorrhage; HP:0002249 Melena; HP:0012208 Hematochezia | Symptom / sign / complication | Acute, may accompany visceral artery rupture, bowel ischemia, or hepatobiliary involvement | Melena/hematochezia 5.6% in Skeik 2019; hemobilia and transit bleeding mentioned as less common presentations in reviews (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, bombardieri2024segmentalarterialmediolysis pages 2-3) | Systematic review, review | (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, bombardieri2024segmentalarterialmediolysis pages 2-3) |
| Hypertension (comorbidity) | HP:0000822 Hypertension | Comorbidity / risk marker | Usually pre-existing adult comorbidity; may complicate presentation and management rather than define phenotype | 42.7% in Skeik 2019; 50% in Naidu 2018; 55% in one summarized series; acute hypertension noted in 13.7% in Peng 2019 (skeik2019segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 2-3) | Cohort, systematic review, review | (skeik2019segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 2-3) |
| Asymptomatic / incidental disease | HP:0000007 Autosomal recessive inheritance | Asymptomatic state / incidental finding | Incidental adult diagnosis on imaging; course may remain stable or regress with surveillance | 4.9% in Skeik 2019; approximately 10% asymptomatic in Bombardieri/retrospective series summary; pooled review range 4.9-10.3% (skeik2019segmentalarterialmediolysis pages 4-5, bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5) | Systematic review, cohort summary, review | (skeik2019segmentalarterialmediolysis pages 4-5, bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 3-5) |
| Cerebrovascular symptoms | HP:0001297 Cerebrovascular abnormality; HP:0002315 Headache; HP:0002381 Aphasia | Symptom / neurologic manifestation | Less common; can be acute when cerebral/cervical vessels involved | 11.9% cerebrovascular symptoms in Skeik 2019; cerebrovascular artery involvement about 13% in large reviews (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, skeik2019segmentalarterialmediolysis pages 7-8) | Systematic review, review | (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, skeik2019segmentalarterialmediolysis pages 7-8) |


*Table: This table summarizes the main clinical phenotypes reported for segmental arterial mediolysis, with suggested HPO mappings, typical clinical course, and approximate frequencies from major cohorts and reviews. It is useful for knowledge-base curation because it links symptoms and complications to ontology terms and evidence types.*

**Quality of life impact.** Formal validated QoL instruments (e.g., SF-36/EQ-5D) were not reported in the retrieved SAM studies. However, acute presentations with pain, hemorrhage, and ischemia can be life-threatening or disabling. (skeik2019segmentalarterialmediolysis pages 4-5, peng2019naturalhistoryand pages 1-2)

---

### 4. Genetic/Molecular Information

#### Causal genes / pathogenic variants
No validated causal gene for SAM was identified in the retrieved evidence. Peng et al. explicitly note “a lack of an evident genetic component” and an apparent lack of familial vasculopathies in SAM, with unclear indications for genetic/reproductive counseling. (peng2019naturalhistoryand pages 7-9)

#### Differential-diagnosis genetics (important exclusions)
Noninvasive diagnostic frameworks explicitly exclude connective tissue disorders with known genetic causes (e.g., Ehlers–Danlos, Marfan syndrome, Loeys–Dietz) when evaluating SAM-like imaging patterns. (naidu2018segmentalarterialmediolysis pages 1-2)

#### Epigenetics / multi-omics
No SAM-specific epigenetic, transcriptomic, proteomic, metabolomic, single-cell, spatial, or functional genomics evidence was identified in the retrieved corpus.

---

### 5. Environmental Information

**Environmental/lifestyle factors.** A 2023 review recommends avoiding vasoconstrictors including tobacco and specific sympathomimetic exposures (cocaine, pseudoephedrine) in the context of a vasospastic/local hypoxemia hypothesis. (najmaoui2023segmentalarterialmediolysis pages 3-5)

**Infectious agents.** SAM is characterized as non-arteritic (noninflammatory); evaluation commonly includes exclusion of mycotic aneurysm when clinically suspected. (najmaoui2023segmentalarterialmediolysis pages 3-5)

---

### 6. Mechanism / Pathophysiology

#### Current mechanistic model
SAM is characterized histologically by medial smooth muscle vacuolar degeneration/lysis with disruption of the media and elastic laminae and a relative absence of inflammatory cells. Bombardieri et al. describe “partial or total vacuolization and lysis of the outer arterial media” with “a notable absence of inflammatory cells.” (bombardieri2024segmentalarterialmediolysis pages 3-4)

A widely used conceptual framework distinguishes an **injurious phase** (mediolysis → arterial gaps → dissection/aneurysm) followed by a **reparative phase** (granulation/fibrosis → stabilization or stenotic sequelae). (peng2019naturalhistoryand pages 6-7)

| Mechanism step | Description | Upstream triggers / initiating factors | Downstream vascular lesions / clinical consequences | Suggested GO Biological Process terms | Suggested CL cell types | Key anatomic sites / UBERON terms |
|---|---|---|---|---|---|---|
| 1. Putative vasospastic initiation | Foundational pathology framework proposes SAM begins with a vasospastic insult to muscular arteries, causing focal ischemic injury of the outer media rather than primary arteritis; modern reviews describe a noninflammatory, nonatherosclerotic arteriopathy with possible repetitive vasoconstrictive injury. | Putative vasospasm; local hypoxemia; environmental/iatrogenic vasoconstrictive exposures; hypertension may amplify wall stress; smoking/tobacco and other vasoconstrictors are discussed as possible contributors in reviews, but causality remains unproven. (slavin2009segmentalarterialmediolysis pages 1-2, peng2019naturalhistoryand pages 6-7, najmaoui2023segmentalarterialmediolysis pages 3-5) | Sets up medial injury that progresses to mediolysis, wall weakening, dissection, aneurysm, hemorrhage, or ischemic organ injury. (slavin2009segmentalarterialmediolysis pages 1-2, peng2019naturalhistoryand pages 6-7) | GO:0003013 circulatory system process; GO:0043062 extracellular structure organization; GO:0008217 regulation of blood pressure | CL:0000359 smooth muscle cell; CL:0000115 endothelial cell | UBERON:0001981 blood vessel; UBERON:0001514 abdominal aorta; UBERON:0003103 renal artery; UBERON:0001163 superior mesenteric artery; UBERON:0013704 celiac artery |
| 2. Injurious phase: mediolysis / vacuolar degeneration | The early injurious phase features vacuolization and lysis of smooth muscle in the outer arterial media (“mediolysis”), producing separation between outer media and adventitia and predisposing to arterial gaps. Histopathology emphasizes vacuolar degeneration of smooth muscle with absence of inflammatory infiltrates. (peng2019naturalhistoryand pages 6-7, bombardieri2024segmentalarterialmediolysis pages 3-4, slavin2009segmentalarterialmediolysis pages 1-2) | Continuation of the initiating vasospastic-hypoxic insult; no evidence this is driven by immune-complex vasculitis or atherosclerosis. (slavin2009segmentalarterialmediolysis pages 1-2, bombardieri2024segmentalarterialmediolysis pages 3-4) | Medial weakening, arterial dilatation, predisposition to dissecting hematoma and aneurysm formation. (slavin2009segmentalarterialmediolysis pages 1-2, peng2019naturalhistoryand pages 6-7) | GO:0070269 pyroptosis/apoptotic-like cell death not established; more conservatively GO:0070265 necrotic cell death; GO:0030198 extracellular matrix organization | CL:0000359 smooth muscle cell; CL:0000115 endothelial cell | UBERON:0001981 blood vessel; UBERON:0004572 tunica media of artery |
| 3. Formation of arterial gaps and wall separation | Mediolysis progresses to focal tears/gaps where the media separates from adventitia; Slavin describes this as a primary morphologic event correlated with characteristic angiographic lesions. Bombardieri and Hirose describe focal loss of internal/external elastic laminae and medial disruption without inflammation. (slavin2009segmentalarterialmediolysis pages 2-3, bombardieri2024segmentalarterialmediolysis pages 3-4, hirose2024gallbladderhemorrhageassociated pages 4-6) | Structural failure of already injured media; elastic lamina loss worsens mechanical instability. (hirose2024gallbladderhemorrhageassociated pages 4-6, bombardieri2024segmentalarterialmediolysis pages 3-4) | Arterial gaps become entry points for hemorrhage into the wall, false lumen formation, dissection, pseudoaneurysm/aneurysm, or rupture. (slavin2009segmentalarterialmediolysis pages 1-2, hirose2024gallbladderhemorrhageassociated pages 4-6) | GO:0030198 extracellular matrix organization; GO:0042398 cellular modified amino acid metabolic process (fibrinoid change not directly ontologized here); GO:0007596 blood coagulation | CL:0000066 adventitial fibroblast (suggested fibroblast population); CL:0000359 smooth muscle cell; CL:0000115 endothelial cell | UBERON:0001981 blood vessel; UBERON:0004572 tunica media of artery; UBERON:0004573 tunica adventitia |
| 4. Intramural hemorrhage / dissecting hematoma | Blood dissects through weakened arterial wall at gap junctions, producing intramural or dissecting hematoma; angiographic manifestations include dissections and irregular luminal flaps. (slavin2009segmentalarterialmediolysis pages 1-2, bombardieri2024segmentalarterialmediolysis pages 2-3, peng2019naturalhistoryand pages 6-7) | Arterial gap formation plus hemodynamic stress and pressure loading. (slavin2009segmentalarterialmediolysis pages 1-2, peng2019naturalhistoryand pages 6-7) | Dissection, thrombosed false lumen, luminal narrowing, branch-vessel compromise, acute abdominal/flank pain, renal or visceral infarction. (naidu2018segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 3-4, peng2019naturalhistoryand pages 6-7) | GO:0007596 blood coagulation; GO:0042060 wound healing; GO:0002576 platelet degranulation | CL:0000233 platelet; CL:0000540 macrophage not consistently established in SAM lesions; CL:0000115 endothelial cell | UBERON:0001163 superior mesenteric artery; UBERON:0003103 renal artery; UBERON:0013704 celiac artery; UBERON:0002113 liver artery/hepatic artery |
| 5. Aneurysmal dilatation and beading phenotype | Loss of medial integrity produces arterial dilatation, single aneurysm, or multiple aneurysms/“string-of-beads” appearance; these are core radiographic phenotypes across cohorts. (bombardieri2024segmentalarterialmediolysis pages 3-4, slavin2009segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 3-5) | Ongoing wall weakness after mediolysis and/or reparative remodeling. (slavin2009segmentalarterialmediolysis pages 1-2, peng2019naturalhistoryand pages 6-7) | Rupture risk, intra-abdominal or retroperitoneal hemorrhage, need for embolization or surgery when unstable. (hirose2024gallbladderhemorrhageassociated pages 4-6, togawa2023intraabdominalbleedingdue pages 3-4, peng2019naturalhistoryand pages 6-7) | GO:0030198 extracellular matrix organization; GO:0001525 angiogenesis/remodeling (broadly reparative); GO:0048729 tissue morphogenesis | CL:0000359 smooth muscle cell; CL:0000895 fibroblast; CL:0000115 endothelial cell | UBERON:0001163 superior mesenteric artery; UBERON:0013704 celiac artery; UBERON:0003103 renal artery; UBERON:0002113 hepatic artery; UBERON:0001194 splenic artery |
| 6. Reparative phase: granulation and fibrosis | After the injurious phase, SAM enters a reparative phase characterized by granulation tissue and fibrosis; this can remodel the wall and may stabilize lesions, but can also create stenotic sequelae. (peng2019naturalhistoryand pages 6-7, slavin2009segmentalarterialmediolysis pages 1-2) | Healing response following medial injury and hemorrhage; noninflammatory repair rather than immune-mediated vasculitis. (peng2019naturalhistoryand pages 6-7, bombardieri2024segmentalarterialmediolysis pages 3-4) | Lesion stabilization/regression in many patients; alternatively focal stenosis, occlusion, chronic ischemia, or lesions resembling fibromuscular dysplasia. (naidu2018segmentalarterialmediolysis pages 5-6, peng2019naturalhistoryand pages 7-9, slavin2009segmentalarterialmediolysis pages 1-2) | GO:0042060 wound healing; GO:0009611 response to wounding; GO:0030199 collagen fibril organization; GO:0061448 connective tissue replacement involved in inflammatory response (approximate) | CL:0000895 fibroblast; CL:0000359 smooth muscle cell | UBERON:0001981 blood vessel; UBERON:0004572 tunica media of artery |
| 7. Stenosis / occlusion from remodeling or thrombus | Reparative fibrosis and/or thrombus in a false lumen can narrow or occlude the true lumen. Radiographic phenotypes include stenosis and occlusion; Peng and Naidu note thrombosed false lumens and progression/resolution on surveillance imaging. (naidu2018segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 3-4, peng2019naturalhistoryand pages 7-9) | Dissection with thrombosis; fibrotic repair after mediolysis. (peng2019naturalhistoryand pages 6-7, slavin2009segmentalarterialmediolysis pages 1-2) | End-organ ischemia/infarction of kidney, spleen, bowel, or liver; renovascular hypertension may occur with renal involvement. (bombardieri2024segmentalarterialmediolysis pages 2-3, naidu2018segmentalarterialmediolysis pages 3-4, peng2019naturalhistoryand pages 2-3) | GO:0007596 blood coagulation; GO:0030198 extracellular matrix organization; GO:0001975 response to hypoxia | CL:0000233 platelet; CL:0000115 endothelial cell; CL:0000359 smooth muscle cell | UBERON:0002113 liver; UBERON:0002108 small intestine; UBERON:0002113 liver; UBERON:0002113 kidney/parenchyma approximated by UBERON:0002113?; UBERON:0002106 spleen |
| 8. Hemorrhagic end-organ damage | When aneurysm or dissected segments rupture, patients may develop hematoma, hemoperitoneum, gallbladder hemorrhage, or shock. Recent case reports extend the phenotype to unusual visceral beds such as gallbladder arteries. (hirose2024gallbladderhemorrhageassociated pages 4-6, togawa2023intraabdominalbleedingdue pages 3-4) | Advanced wall disruption of aneurysmal/dissected arterial segments. (hirose2024gallbladderhemorrhageassociated pages 4-6, slavin2009segmentalarterialmediolysis pages 1-2) | Life-threatening intra-abdominal hemorrhage, hypovolemic shock, need for urgent endovascular embolization or surgery. (hirose2024gallbladderhemorrhageassociated pages 4-6, togawa2023intraabdominalbleedingdue pages 3-4, bombardieri2024segmentalarterialmediolysis pages 4-5) | GO:0002576 platelet degranulation; GO:0007596 blood coagulation; GO:0001944 vasculature development/remodeling (broad context) | CL:0000233 platelet; CL:0000115 endothelial cell | UBERON:0000916 abdomen; UBERON:0002110 gallbladder; UBERON:0001163 superior mesenteric artery; UBERON:0001194 splenic artery |
| 9. Absence of primary inflammation as defining negative feature | Histology repeatedly notes “absence of inflammatory cells,” distinguishing SAM from polyarteritis nodosa and other vasculitides. This negative mechanism is diagnostically central and explains why corticosteroids are generally discouraged. (bombardieri2024segmentalarterialmediolysis pages 3-4, bombardieri2024segmentalarterialmediolysis pages 4-5, peng2019naturalhistoryand pages 6-7) | Not immune-complex arteritis; inflammatory marker elevations may be secondary to infarction/bleeding rather than causal vasculitis. (najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 7-9) | Helps guide differential diagnosis and management away from immunosuppression toward vascular surveillance/intervention and blood-pressure control. (najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 6-7) | GO:0006954 inflammatory response — notably not a dominant primary process in SAM | CL:0000775 neutrophil; CL:0000860 eosinophil; CL:0000623 natural killer cell — included here as inflammatory cells generally absent on pathology | UBERON:0001981 blood vessel |
| 10. Dynamic lesion evolution over time | Cohort studies show SAM is biologically dynamic: lesions may regress, remain stable, or progress, and new lesions can appear during follow-up, supporting serial imaging surveillance. (naidu2018segmentalarterialmediolysis pages 1-1, naidu2018segmentalarterialmediolysis pages 3-4, peng2019naturalhistoryand pages 7-9) | Ongoing hemodynamic stress and evolving repair/remodeling after the initial insult. (peng2019naturalhistoryand pages 7-9, slavin2009segmentalarterialmediolysis pages 1-2) | Clinical rationale for repeat CTA at short interval then longitudinal follow-up; intervention is reserved for hemorrhage, hemodynamic instability, bowel ischemia, or threatening aneurysm/dissection. (peng2019naturalhistoryand pages 7-9, najmaoui2023segmentalarterialmediolysis pages 3-5) | GO:0048729 tissue morphogenesis; GO:0042060 wound healing; GO:0003018 vascular process in circulatory system | CL:0000115 endothelial cell; CL:0000359 smooth muscle cell; CL:0000895 fibroblast | UBERON:0001981 blood vessel; commonly UBERON:0013704 celiac artery, UBERON:0001163 superior mesenteric artery, UBERON:0003103 renal artery |


*Table: This table summarizes the proposed pathophysiologic cascade of segmental arterial mediolysis from putative vasospastic injury through medial lysis, dissection, aneurysm, fibrosis, and hemorrhagic or ischemic complications. It also links each step to suggested ontology terms and anatomic/cellular targets for knowledge-base annotation.*

---

### 7. Anatomical Structures Affected

**Organ/system level.** SAM primarily involves **medium-to-large visceral branches of the abdominal aorta**, with common involvement of the celiac, superior mesenteric, renal, hepatic, and splenic arterial territories. (skeik2019segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 1-1, peng2019naturalhistoryand pages 1-2)

**Tissue/cell level.** The dominant injured compartment is the arterial **tunica media** and its **vascular smooth muscle cells**, with subsequent wall separation and remodeling; inflammatory infiltrates are typically absent on pathology. (bombardieri2024segmentalarterialmediolysis pages 3-4, slavin2009segmentalarterialmediolysis pages 1-2)

**Localization and multiplicity.** Multifocal/multivessel involvement is common: in Skeik’s synthesis, multiple-vessel involvement occurred in 62.2%. (skeik2019segmentalarterialmediolysis pages 4-5)

---

### 8. Temporal Development

**Onset pattern.** SAM often presents abruptly with acute pain; in cohorts the dominant presentation is acute abdominal pain. (naidu2018segmentalarterialmediolysis pages 1-1, peng2019naturalhistoryand pages 1-2)

**Progression/course.** SAM is dynamic on imaging surveillance: in Naidu’s cohort, 20% showed progression while most remained stable or resolved; in Peng’s cohort, 28.6% progressed while 27.7% regressed and 43.8% remained stable. (naidu2018segmentalarterialmediolysis pages 1-1, peng2019naturalhistoryand pages 1-2)

---

### 9. Inheritance and Population

#### Epidemiology
A 2023 review summarizes a reported incidence of approximately **1 in 100,000 per year** (rare disease), though this estimate derives from the limited SAM literature and should be interpreted cautiously. (najmaoui2023segmentalarterialmediolysis pages 3-5)

#### Demographics
Across major aggregated studies:
- Median/mean age clusters in the early-to-mid 50s. (naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 4-5, peng2019naturalhistoryand pages 2-3)
- Male predominance is consistently reported (~67–71%). (naidu2018segmentalarterialmediolysis pages 1-1, skeik2019segmentalarterialmediolysis pages 4-5)

#### Inheritance
No Mendelian inheritance pattern is supported in the retrieved evidence; Peng et al. emphasize lack of an evident genetic component. (peng2019naturalhistoryand pages 7-9)

---

### 10. Diagnostics

#### Clinical criteria and differential diagnosis
Because histology is often impractical, SAM is frequently diagnosed clinically using characteristic vascular imaging plus exclusion of vasculitis, atherosclerosis, fibromuscular dysplasia (FMD), and connective tissue disorders. (naidu2018segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 3-5)

Noninvasive diagnostic frameworks (e.g., institutional criteria in Naidu’s AJR cohort) emphasize exclusion of more plausible diagnoses such as FMD/atherosclerosis and exclusion of connective tissue disorders (Ehlers–Danlos, Marfan, Loeys–Dietz), together with serologic evaluation for vasculitis markers. (naidu2018segmentalarterialmediolysis pages 1-2)

#### Imaging
**CT angiography (CTA)** is emphasized as the most accurate and practical modality in contemporary care. A 2023 review states CTA yields “the best diagnostic accuracy,” and Naidu’s cohort relied primarily on contrast-enhanced CT (92% at initial imaging). (najmaoui2023segmentalarterialmediolysis pages 3-5, naidu2018segmentalarterialmediolysis pages 2-3)

Common angiographic/CTA patterns include dissection, aneurysm (including “string-of-beads”), stenosis, and occlusion. (bombardieri2024segmentalarterialmediolysis pages 3-4, naidu2018segmentalarterialmediolysis pages 1-1)

The image below exemplifies the angiographic “string-of-beads” appearance with multifocal dissections/aneurysms.

(connolly2021segmentalarterialmediolysis media 71aca598)

#### Laboratory tests
Work-up often includes ANA/ANCA and inflammatory markers (ESR/CRP) to exclude vasculitis, recognizing that CRP can be secondarily elevated by infarction. (najmaoui2023segmentalarterialmediolysis pages 1-3, najmaoui2023segmentalarterialmediolysis pages 3-5)

---

### 11. Outcome / Prognosis

Overall prognosis in recent cohorts is often favorable with appropriate surveillance and intervention for complications:
- Naidu 2018: no deaths during follow-up; 80% stability/resolution among those with follow-up imaging; 20% progression. (naidu2018segmentalarterialmediolysis pages 1-1, naidu2018segmentalarterialmediolysis pages 4-5)
- Peng 2019: overall mortality 4.3% and disease-specific mortality 0.85%; regression 27.7%, stability 43.8%, progression 28.6%. (peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2)
- Skeik 2019 systematic review: mortality 7%; symptom relief in 91% of reported cases. (skeik2019segmentalarterialmediolysis pages 1-2)

Nonetheless, older reports and rupture presentations can carry high mortality (up to ~50% in acute hypotension/rupture scenarios in historical series), highlighting the need for rapid recognition and hemorrhage control when present. (peng2019naturalhistoryand pages 6-7, togawa2023intraabdominalbleedingdue pages 3-4)

---

### 12. Treatment

There is no single standardized therapy; care is stratified by stability, hemorrhage, and ischemia risk.

| Management strategy | Suggested MAXO term(s) | Typical indication(s) in SAM | Key details / implementation notes | Reported outcome data / frequency | Key supporting sources |
|---|---|---|---|---|---|
| Conservative management: blood pressure control, analgesia, surveillance imaging | MAXO: antihypertensive therapy; pain management; medical surveillance | Hemodynamically stable patients without active major hemorrhage or bowel-threatening ischemia | Common first-line approach after CTA-based diagnosis; includes strict BP control, analgesia, risk-factor modification, and serial CTA follow-up. Recommended short-interval imaging because new lesions/progression can occur early; suggested schedules include 1 week, 3 months, then yearly if stable, or 1, 3, 9 months then annually in review-based practice. | Skeik 2019: conservative treatment reported in 8.1% of pooled cases; antihypertensives 19.9% (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 5-6). Naidu 2018: 80% of followed patients had stability/resolution, no follow-up deaths (naidu2018segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 5-6). Peng 2019: imaging regression 27.7%, stability 43.8%, progression 28.6%; overall mortality 4.3%, disease-specific mortality 0.85% (peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2). 13-case institutional series: most conservatively managed patients showed stabilization/regression (skeik2019segmentalarterialmediolysis pages 1-2). | (naidu2018segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 5-6, najmaoui2023segmentalarterialmediolysis pages 3-5, skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 5-6, peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2) |
| Antiplatelet therapy | MAXO: antiplatelet agent therapy | Stable disease with dissection/thrombotic lumen or ischemic risk; used case-by-case because evidence is limited | Often paired with BP control and imaging surveillance. Role remains uncertain; not disease-specific standard of care. Used more often in non-emergent management than in rupture. | Skeik 2019: antiplatelet therapy in 10.3% of pooled cases (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 5-6). Naidu 2018: antiplatelet therapy in 46/97 patients with follow-up imaging (naidu2018segmentalarterialmediolysis pages 4-5). Peng 2019/Najmaoui review note uncertain benefit and individualized use (najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 7-9). | (naidu2018segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5, skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 5-6, peng2019naturalhistoryand pages 7-9) |
| Anticoagulation | MAXO: anticoagulant therapy | Selected patients with thrombosed false lumen, distal ischemia/infarction, or embolic/thrombotic concern; not universally recommended | Highly individualized because SAM can bleed as well as thrombose. Several recent case reports used heparin/LMWH/warfarin in stable patients with dissections and renal ischemia, but reviews emphasize uncertain net benefit. | Skeik 2019: anticoagulation in 11.8% of pooled cases (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 5-6). Peng 2019: anticoagulants should be started in absence of clinical improvement per authors’ practice summary (peng2019naturalhistoryand pages 7-9). Bombardieri 2024 and Najmaoui 2023 describe successful conservative courses using anticoagulation in selected cases (bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 1-3, bombardieri2024segmentalarterialmediolysis pages 1-2). | (bombardieri2024segmentalarterialmediolysis pages 2-3, najmaoui2023segmentalarterialmediolysis pages 1-3, bombardieri2024segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 3-5, skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 5-6, peng2019naturalhistoryand pages 7-9) |
| Endovascular embolization | MAXO: endovascular embolization | Preferred acute intervention for active bleeding, ruptured aneurysm/pseudoaneurysm, enlarging aneurysm, or unstable hemorrhagic presentation when anatomically feasible | Increasingly favored over open surgery because it is less invasive and can rapidly control hemorrhage; includes coil embolization of culprit visceral branches. Also used when progression on surveillance produces treatable aneurysm. | Skeik 2019: coil embolization 27.9% of pooled cases, the most common specific intervention (skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 5-6). Peng 2019: interventions in 22.2% overall; embolization made up 78.9% of endovascular procedures; endovascular success 84% (peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2). Bombardieri 2024 and Togawa 2023 note endovascular therapy is generally preferred/first approach when feasible (bombardieri2024segmentalarterialmediolysis pages 4-5, togawa2023intraabdominalbleedingdue pages 3-4, bombardieri2024segmentalarterialmediolysis pages 3-4). | (bombardieri2024segmentalarterialmediolysis pages 4-5, togawa2023intraabdominalbleedingdue pages 3-4, bombardieri2024segmentalarterialmediolysis pages 3-4, skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 5-6, peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2) |
| Stent-grafting / angioplasty | MAXO: vascular stent placement; angioplasty | Focal stenosis/dissection/aneurysm in anatomically suitable vessels, especially when preservation of parent artery flow is desired | Less common than embolization; choice depends on vessel caliber, branch pattern, rupture risk, and technical feasibility. Can be used as bridge or alternative to open repair. | Skeik 2019: angioplasty/stenting 8.1% of pooled cases (skeik2019segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 5-6). Institutional 13-case series: 3/13 required stent-grafting of renal/celiac lesions and 1 SMA branch embolization; remaining cases were conservative with stable/regressive follow-up (skeik2019segmentalarterialmediolysis pages 1-2). | (skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 5-6) |
| Open surgery / arterial repair / organ resection | MAXO: vascular surgery; arterial repair; surgical resection | Hemodynamic instability, uncontrolled hemorrhage, bowel infarction/ischemia, failed or infeasible endovascular therapy, or need for pathology-confirming specimen | Includes open arterial repair, bypass/revascularization, aneurysm ligation, or organ surgery (e.g., bowel/gallbladder resection) depending on affected territory and complications. Often reserved for rescue or anatomy not amenable to endovascular treatment. | Skeik 2019: abdominal organ surgery 23.5% and open arterial repair 20.6% (skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 5-6). Peng 2019: open surgery success 93%; perioperative complications uncommon, but one death from ongoing hemorrhage reported in operated patients (peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2). Togawa 2023 supports surgery when anticoagulation is needed and bleeding risk complicates conservative care (togawa2023intraabdominalbleedingdue pages 3-4). | (togawa2023intraabdominalbleedingdue pages 3-4, skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, najmaoui2023segmentalarterialmediolysis pages 5-6, peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2) |
| Avoid corticosteroids | MAXO: avoidance of contraindicated medication | All suspected/confirmed SAM unless another inflammatory disease truly coexists | SAM is noninflammatory; steroids may expose patients to harm and are repeatedly discouraged because SAM can mimic vasculitis. Correct diagnosis prevents inappropriate immunosuppression. | Recent reviews explicitly state corticosteroids are not recommended (najmaoui2023segmentalarterialmediolysis pages 3-5). Peng 2019 advises avoidance of steroids in multimodal medical management (peng2019naturalhistoryand pages 7-9). | (najmaoui2023segmentalarterialmediolysis pages 3-5, peng2019naturalhistoryand pages 7-9) |
| Avoid vasoconstrictors / trigger modification | MAXO: risk factor avoidance; substance avoidance counseling | Suspected vasospastic-trigger model, recurrent/progressive disease risk reduction, and general secondary prevention | Reviews recommend avoiding vasoconstrictive exposures such as tobacco, cocaine, and pseudoephedrine; smoking cessation and cardiovascular risk reduction are commonly advised. | Najmaoui 2023 specifically recommends avoidance of vasoconstrictors and notes environmental factors promoting vasoconstriction/local hypoxemia (najmaoui2023segmentalarterialmediolysis pages 3-5). Peng 2019 recommends tobacco cessation and multimodal risk-factor control (peng2019naturalhistoryand pages 6-7, peng2019naturalhistoryand pages 7-9). | (peng2019naturalhistoryand pages 6-7, peng2019naturalhistoryand pages 7-9, najmaoui2023segmentalarterialmediolysis pages 3-5) |


*Table: This table summarizes real-world treatment approaches for segmental arterial mediolysis, including conservative, medical, endovascular, and surgical options. It also maps each strategy to suggested MAXO-style intervention labels and highlights the limited but important outcome data from major cohorts and reviews.*

Key points supported by authoritative sources:
- **Avoid corticosteroids** unless an alternative inflammatory diagnosis is proven, because SAM is noninflammatory and frequently mimics vasculitis. (peng2019naturalhistoryand pages 7-9, najmaoui2023segmentalarterialmediolysis pages 3-5)
- **Endovascular embolization** is commonly used for bleeding/rupture and is frequently preferred when feasible. (skeik2019segmentalarterialmediolysis pages 4-5, peng2019naturalhistoryand pages 1-2)
- **Conservative management with strict blood-pressure control and surveillance imaging** is common in stable disease; lesion regression/stability is frequent, but progression/new lesions occur in a minority. (naidu2018segmentalarterialmediolysis pages 4-5, peng2019naturalhistoryand pages 1-2)

---

### 13. Prevention

No validated primary prevention strategy exists because causal factors are uncertain. However, secondary-prevention style measures are frequently recommended:
- Avoidance of vasoconstrictors (tobacco, cocaine, pseudoephedrine) in the vasospastic trigger hypothesis. (najmaoui2023segmentalarterialmediolysis pages 3-5)
- Cardiovascular risk-factor optimization and tobacco cessation as part of multimodal medical management. (peng2019naturalhistoryand pages 7-9)

No population screening programs were identified.

---

### 14. Other Species / Natural Disease

No naturally occurring SAM in non-human species was identified in the retrieved evidence.

---

### 15. Model Organisms

No established animal or cellular model systems for SAM were identified in the retrieved evidence.

---

## Recent Developments and 2023–2024 Highlights (prioritized)

1. **Refined clinical emphasis on CTA-based diagnosis and mimicker exclusion.** A 2023 case-based review stresses CTA as the best diagnostic test and the need to exclude vasculitis (including use of FDG-PET/CT in selected cases) and connective tissue disorders. (najmaoui2023segmentalarterialmediolysis pages 3-5)
2. **Expanded phenotypic spectrum in contemporary case literature.** A 2024 case report describes gallbladder hemorrhage associated with SAM, extending awareness to unusual visceral arterial beds and underscoring the role of histopathology in confirmation when surgery occurs. (hirose2024gallbladderhemorrhageassociated pages 4-6)
3. **Ongoing clinical challenge: conservative antithrombotic therapy vs bleeding risk.** 2024 and 2023 case reports highlight that anticoagulation/antiplatelet use is sometimes chosen in stable dissections/ischemia but remains non-standard and must be balanced against hemorrhage risk. (bombardieri2024segmentalarterialmediolysis pages 1-2, togawa2023intraabdominalbleedingdue pages 3-4)

---

## Relevant Statistics and Data (from large cohorts/reviews)

The table below consolidates the best-available quantitative data from major SAM cohorts and systematic review evidence.

| Source | Study type / setting | N | Demographics | Most common presenting symptoms | Most commonly involved arteries | Key imaging findings | Follow-up / outcomes | Notes |
|---|---:|---:|---|---|---|---|---|---|
| Naidu 2018, *AJR* | Retrospective single-center abdominal imaging cohort, 2000–2015 | 111 | Median age 51 y (23–87); 71% male | Abdominal pain 74%; flank pain 21%; back pain 9% | Renal 47%; SMA 46%; celiac trunk 46%; hepatic 23%; iliac 18%; splenic 14% | Dissection 86%; aneurysm 57%; beading/webs 28%; occlusion 19%; rind/wall thickening 15%; end-organ ischemia/infarction 34%; hematoma 9% | 97/111 had follow-up imaging (247 studies), median follow-up 12 mo; progression 20% (19/97); stability or resolution 80% (78/97); no deaths during follow-up | Initial imaging CT in 92%; MRI 5%; multi-territory disease common; diagnosis based on noninvasive imaging criteria with exclusion of mimics (naidu2018segmentalarterialmediolysis pages 1-1, naidu2018segmentalarterialmediolysis pages 4-5, naidu2018segmentalarterialmediolysis pages 3-4, naidu2018segmentalarterialmediolysis pages 1-2, naidu2018segmentalarterialmediolysis pages 2-3) |
| Peng 2019, *J Vasc Surg* | Retrospective institutional natural-history / management cohort, 2000–2016 | 117 | Mean age 52.7 y; 67.5% male | Abdominal pain 69.2%; chronic abdominal pain 15.4%; acute hypertension 13.7%; intra-abdominal hemorrhage 8.5% | Celiac 54.7%; renal 49.6%; SMA 43.6% | Dissection 79.5%; aneurysm 52.1%; end-organ ischemia/infarction 41.9%; radiographic spectrum also included occlusion, stenosis, beading, wall thickening, pseudoaneurysm, fistula | Follow-up imaging in 96.6%; mean follow-up 1258 d; regression 27.7%; stability 43.8%; progression 28.6%; mean time to progression 666 d; overall mortality 4.3%; disease-specific mortality 0.85%; 22.2% underwent intervention; endovascular success 84%, open surgery success 93% | Historical mortality in older series was much higher; recommended short-interval imaging (1 wk, 3 mo, then yearly if stable) and medical risk-factor control; corticosteroids discouraged (peng2019naturalhistoryand pages 6-7, peng2019naturalhistoryand pages 7-9, peng2019naturalhistoryand pages 1-2, peng2019naturalhistoryand pages 2-3) |
| Skeik 2019, *Vascular Medicine* | Systematic review + institutional cases (126 literature cases + 17 center cases) | 143 | Median age 55 y (IQR 48–63); 67.8% male | Abdominal/flank pain 79.7%; intra-abdominal bleeding 49.7%; nausea/vomiting 16.1%; cerebrovascular symptoms 11.9%; shock 4.2%; asymptomatic 4.9% | SMA 53.1%; hepatic 44.8%; celiac 35.7%; renal 25.9%; splenic 24.5%; cerebrovascular 13.3%; IMA 10.5%; multiple-vessel involvement 62.2% | Aneurysm 76.2%; dissection 60.8%; rupture 45.5%; string-of-beads 14.7%; stenosis 18.9%; obstruction 16.9%; thrombosis 14.7%; wall thickening 7.7% | Symptom relief/improvement 90.6%; radiologic improvement 66.3%, unchanged 17.5%, worsened 16.3%; survival 93%; mortality 7% | CT/CTA most used imaging 77.6%–78%; catheter angiography 35%; MRA and ultrasound each ~9%; histology available in 44.1%; treatments: coil embolization 27.9%, abdominal organ surgery 23.5%, open arterial repair 20.6%, antihypertensives 19.9%, anticoagulation 11.8%, antiplatelets 10.3%, angioplasty/stenting 8.1%, conservative therapy 8.1% (skeik2019segmentalarterialmediolysis pages 4-5, skeik2019segmentalarterialmediolysis pages 1-2, skeik2019segmentalarterialmediolysis pages 5-7, najmaoui2023segmentalarterialmediolysis pages 5-6) |
| Najmaoui 2023, *EJCRIM* | Case report + narrative review synthesizing major series | 1 case + review | Review summary: incidence ~1/100,000/year; typically men in their 50s; series ranges include median/mean ages 51–55 y and male proportion ~67–71% | Abdominal pain 69.2–82%; hemorrhagic shock 4.2%; asymptomatic 4.9–10.3% | SMA 43.6–53.1%; celiac trunk 35.7–54.7%; renal 25.9–52%; cerebrovascular ~13% | Dissections 60.8–95%; aneurysms 52.1–76.2%; stenosis 18.9–26%; string-of-beads 14.7–31% | Clinical improvement ~90.6%; radiologic improvement 71.5–83.8%; 1-year survival 93–100%; 3-year survival 95.7% | CT angiography described as the best diagnostic accuracy; histology is gold standard but noninvasive criteria increasingly used; corticosteroids not recommended; conservative care for stable patients and endovascular therapy preferred for unstable cases (najmaoui2023segmentalarterialmediolysis pages 3-5, najmaoui2023segmentalarterialmediolysis pages 5-6) |


*Table: This table summarizes the main quantitative findings for segmental arterial mediolysis from the largest available cohorts and reviews cited in the evidence. It is useful for comparing demographics, vascular distribution, imaging phenotypes, and outcomes across the key SAM literature.*

---

## Expert Opinions / Authoritative Analysis (from cited sources)

- Slavin’s synthesis argues SAM is a distinct clinicopathologic entity with characteristic angiographic patterns arising from medial injury and a tear separating outer media from adventitia, with many lesions that “persist, become smaller, or resolve,” but with potential for delayed complications. (slavin2009segmentalarterialmediolysis pages 1-2)
- Peng et al. emphasize that SAM management should be directed by hemodynamic stability, ischemia, and aneurysm/dissection extent, with multimodal medical therapy and surveillance in non-emergent cases and intervention reserved for acute threats. (peng2019naturalhistoryand pages 7-9)
- Recent internal medicine–oriented reviews emphasize that distinguishing SAM from vasculitis and FMD is critical to avoid inappropriate corticosteroid treatment and to direct care toward imaging surveillance and endovascular options when needed. (bombardieri2024segmentalarterialmediolysis pages 4-5, najmaoui2023segmentalarterialmediolysis pages 3-5)

---

## Notes on limitations of this report

- Ontology identifiers (MONDO, Orphanet), ICD codes, and MeSH IDs were not explicitly present in the retrieved full-text evidence and therefore are not provided.
- High-quality randomized trials do not exist for SAM in the retrieved corpus; evidence is largely observational and case-based.

---

## Key source URLs (publication date in citation block)

- Bombardieri et al., 2024-09. Italian Journal of Medicine. https://doi.org/10.4081/itjm.2024.1795 (bombardieri2024segmentalarterialmediolysis pages 1-2)
- Najmaoui et al., 2023-10. European Journal of Case Reports in Internal Medicine. https://doi.org/10.12890/2023_004085 (najmaoui2023segmentalarterialmediolysis pages 1-3)
- Hirose et al., 2024-01. Surgical Case Reports. https://doi.org/10.1186/s40792-023-01799-1 (hirose2024gallbladderhemorrhageassociated pages 4-6)
- Naidu et al., 2018-04. AJR. https://doi.org/10.2214/AJR.17.18309 (naidu2018segmentalarterialmediolysis pages 1-1)
- Skeik et al., 2019-12. Vascular Medicine. https://doi.org/10.1177/1358863X19873410 (skeik2019segmentalarterialmediolysis pages 1-2)
- Peng et al., 2019-12. Journal of Vascular Surgery. https://doi.org/10.1016/j.jvs.2019.02.068 (peng2019naturalhistoryand pages 1-2)
- Slavin, 2009-11. Cardiovascular Pathology. https://doi.org/10.1016/j.carpath.2008.09.001 (slavin2009segmentalarterialmediolysis pages 1-2)


References

1. (bombardieri2024segmentalarterialmediolysis pages 2-3): Giulia Bombardieri, Alessandra Rustici, Michele Caselli, Chiara Chirico, Veronica Bocchi, and Andrea Montagnani. Segmental arterial mediolysis: a challenging diagnosis in internal medicine. Italian Journal of Medicine, Sep 2024. URL: https://doi.org/10.4081/itjm.2024.1795, doi:10.4081/itjm.2024.1795. This article has 0 citations and is from a peer-reviewed journal.

2. (bombardieri2024segmentalarterialmediolysis pages 3-4): Giulia Bombardieri, Alessandra Rustici, Michele Caselli, Chiara Chirico, Veronica Bocchi, and Andrea Montagnani. Segmental arterial mediolysis: a challenging diagnosis in internal medicine. Italian Journal of Medicine, Sep 2024. URL: https://doi.org/10.4081/itjm.2024.1795, doi:10.4081/itjm.2024.1795. This article has 0 citations and is from a peer-reviewed journal.

3. (bombardieri2024segmentalarterialmediolysis pages 1-2): Giulia Bombardieri, Alessandra Rustici, Michele Caselli, Chiara Chirico, Veronica Bocchi, and Andrea Montagnani. Segmental arterial mediolysis: a challenging diagnosis in internal medicine. Italian Journal of Medicine, Sep 2024. URL: https://doi.org/10.4081/itjm.2024.1795, doi:10.4081/itjm.2024.1795. This article has 0 citations and is from a peer-reviewed journal.

4. (naidu2018segmentalarterialmediolysis pages 1-1): Sailen G. Naidu, Christine O. Menias, Rahmi Oklu, Robert S. Hines, Kinan Alhalabi, Gerges Makar, Fadi E. Shamoun, Stanislav Henkin, and Robert D. McBane. Segmental arterial mediolysis: abdominal imaging of and disease course in 111 patients. American Journal of Roentgenology, 210:899-905, Apr 2018. URL: https://doi.org/10.2214/ajr.17.18309, doi:10.2214/ajr.17.18309. This article has 62 citations and is from a peer-reviewed journal.

5. (skeik2019segmentalarterialmediolysis pages 1-2): Nedaa Skeik, Sydney L Olson, Gopika Hari, and Mary L Pavia. Segmental arterial mediolysis (sam): systematic review and analysis of 143 cases. Vascular Medicine, 24:549-563, Dec 2019. URL: https://doi.org/10.1177/1358863x19873410, doi:10.1177/1358863x19873410. This article has 81 citations and is from a peer-reviewed journal.

6. (najmaoui2023segmentalarterialmediolysis pages 3-5): Marine Najmaoui, Martina Pezzulo, Denis Franchimont, Frédéric Vandergheynst, and Maxime Ilzkovitz. Segmental arterial mediolysis and its mimickers: a case report and review of the literature. European Journal of Case Reports in Internal Medicine, Oct 2023. URL: https://doi.org/10.12890/2023\_004085, doi:10.12890/2023\_004085. This article has 3 citations.

7. (peng2019naturalhistoryand pages 1-2): Kate X. Peng, Victor J. Davila, William M. Stone, Fadi E. Shamoun, Sailendra G. Naidu, Robert D. McBane, and Samuel R. Money. Natural history and management outcomes of segmental arterial mediolysis. Journal of Vascular Surgery, 67:e14, Dec 2019. URL: https://doi.org/10.1016/j.jvs.2019.02.068, doi:10.1016/j.jvs.2019.02.068. This article has 36 citations and is from a domain leading peer-reviewed journal.

8. (hirose2024gallbladderhemorrhageassociated pages 4-6): Yuichi Hirose, Yusuke Tajima, Hiroki Sakata, Toshimasa Uekusa, Kentaro Kamada, Takashi Ikehara, Izuru Matsuda, Satomi Yoneyama, Akio Hidemura, and Hiroyuki Suzuki. Gallbladder hemorrhage associated with segmental arterial mediolysis: a case report. Surgical Case Reports, Jan 2024. URL: https://doi.org/10.1186/s40792-023-01799-1, doi:10.1186/s40792-023-01799-1. This article has 1 citations.

9. (najmaoui2023segmentalarterialmediolysis pages 1-3): Marine Najmaoui, Martina Pezzulo, Denis Franchimont, Frédéric Vandergheynst, and Maxime Ilzkovitz. Segmental arterial mediolysis and its mimickers: a case report and review of the literature. European Journal of Case Reports in Internal Medicine, Oct 2023. URL: https://doi.org/10.12890/2023\_004085, doi:10.12890/2023\_004085. This article has 3 citations.

10. (slavin2009segmentalarterialmediolysis pages 1-2): Richard E. Slavin. Segmental arterial mediolysis: course, sequelae, prognosis, and pathologic-radiologic correlation. Cardiovascular pathology : the official journal of the Society for Cardiovascular Pathology, 18 6:352-60, Nov 2009. URL: https://doi.org/10.1016/j.carpath.2008.09.001, doi:10.1016/j.carpath.2008.09.001. This article has 182 citations.

11. (slavin2009segmentalarterialmediolysis pages 2-3): Richard E. Slavin. Segmental arterial mediolysis: course, sequelae, prognosis, and pathologic-radiologic correlation. Cardiovascular pathology : the official journal of the Society for Cardiovascular Pathology, 18 6:352-60, Nov 2009. URL: https://doi.org/10.1016/j.carpath.2008.09.001, doi:10.1016/j.carpath.2008.09.001. This article has 182 citations.

12. (peng2019naturalhistoryand pages 7-9): Kate X. Peng, Victor J. Davila, William M. Stone, Fadi E. Shamoun, Sailendra G. Naidu, Robert D. McBane, and Samuel R. Money. Natural history and management outcomes of segmental arterial mediolysis. Journal of Vascular Surgery, 67:e14, Dec 2019. URL: https://doi.org/10.1016/j.jvs.2019.02.068, doi:10.1016/j.jvs.2019.02.068. This article has 36 citations and is from a domain leading peer-reviewed journal.

13. (naidu2018segmentalarterialmediolysis pages 2-3): Sailen G. Naidu, Christine O. Menias, Rahmi Oklu, Robert S. Hines, Kinan Alhalabi, Gerges Makar, Fadi E. Shamoun, Stanislav Henkin, and Robert D. McBane. Segmental arterial mediolysis: abdominal imaging of and disease course in 111 patients. American Journal of Roentgenology, 210:899-905, Apr 2018. URL: https://doi.org/10.2214/ajr.17.18309, doi:10.2214/ajr.17.18309. This article has 62 citations and is from a peer-reviewed journal.

14. (skeik2019segmentalarterialmediolysis pages 4-5): Nedaa Skeik, Sydney L Olson, Gopika Hari, and Mary L Pavia. Segmental arterial mediolysis (sam): systematic review and analysis of 143 cases. Vascular Medicine, 24:549-563, Dec 2019. URL: https://doi.org/10.1177/1358863x19873410, doi:10.1177/1358863x19873410. This article has 81 citations and is from a peer-reviewed journal.

15. (skeik2019segmentalarterialmediolysis pages 5-7): Nedaa Skeik, Sydney L Olson, Gopika Hari, and Mary L Pavia. Segmental arterial mediolysis (sam): systematic review and analysis of 143 cases. Vascular Medicine, 24:549-563, Dec 2019. URL: https://doi.org/10.1177/1358863x19873410, doi:10.1177/1358863x19873410. This article has 81 citations and is from a peer-reviewed journal.

16. (naidu2018segmentalarterialmediolysis pages 3-4): Sailen G. Naidu, Christine O. Menias, Rahmi Oklu, Robert S. Hines, Kinan Alhalabi, Gerges Makar, Fadi E. Shamoun, Stanislav Henkin, and Robert D. McBane. Segmental arterial mediolysis: abdominal imaging of and disease course in 111 patients. American Journal of Roentgenology, 210:899-905, Apr 2018. URL: https://doi.org/10.2214/ajr.17.18309, doi:10.2214/ajr.17.18309. This article has 62 citations and is from a peer-reviewed journal.

17. (togawa2023intraabdominalbleedingdue pages 3-4): Yuki Togawa, Susumu Matsushime, Nobuichiro Tamura, and Kazuyuki Kawamoto. Intra-abdominal bleeding due to segmental arterial mediolysis and coexisting pulmonary thromboembolism: a case report. Indian Journal of Surgery, 85:623-626, Jun 2023. URL: https://doi.org/10.1007/s12262-022-03465-6, doi:10.1007/s12262-022-03465-6. This article has 0 citations and is from a peer-reviewed journal.

18. (peng2019naturalhistoryand pages 2-3): Kate X. Peng, Victor J. Davila, William M. Stone, Fadi E. Shamoun, Sailendra G. Naidu, Robert D. McBane, and Samuel R. Money. Natural history and management outcomes of segmental arterial mediolysis. Journal of Vascular Surgery, 67:e14, Dec 2019. URL: https://doi.org/10.1016/j.jvs.2019.02.068, doi:10.1016/j.jvs.2019.02.068. This article has 36 citations and is from a domain leading peer-reviewed journal.

19. (skeik2019segmentalarterialmediolysis pages 7-8): Nedaa Skeik, Sydney L Olson, Gopika Hari, and Mary L Pavia. Segmental arterial mediolysis (sam): systematic review and analysis of 143 cases. Vascular Medicine, 24:549-563, Dec 2019. URL: https://doi.org/10.1177/1358863x19873410, doi:10.1177/1358863x19873410. This article has 81 citations and is from a peer-reviewed journal.

20. (naidu2018segmentalarterialmediolysis pages 1-2): Sailen G. Naidu, Christine O. Menias, Rahmi Oklu, Robert S. Hines, Kinan Alhalabi, Gerges Makar, Fadi E. Shamoun, Stanislav Henkin, and Robert D. McBane. Segmental arterial mediolysis: abdominal imaging of and disease course in 111 patients. American Journal of Roentgenology, 210:899-905, Apr 2018. URL: https://doi.org/10.2214/ajr.17.18309, doi:10.2214/ajr.17.18309. This article has 62 citations and is from a peer-reviewed journal.

21. (peng2019naturalhistoryand pages 6-7): Kate X. Peng, Victor J. Davila, William M. Stone, Fadi E. Shamoun, Sailendra G. Naidu, Robert D. McBane, and Samuel R. Money. Natural history and management outcomes of segmental arterial mediolysis. Journal of Vascular Surgery, 67:e14, Dec 2019. URL: https://doi.org/10.1016/j.jvs.2019.02.068, doi:10.1016/j.jvs.2019.02.068. This article has 36 citations and is from a domain leading peer-reviewed journal.

22. (naidu2018segmentalarterialmediolysis pages 4-5): Sailen G. Naidu, Christine O. Menias, Rahmi Oklu, Robert S. Hines, Kinan Alhalabi, Gerges Makar, Fadi E. Shamoun, Stanislav Henkin, and Robert D. McBane. Segmental arterial mediolysis: abdominal imaging of and disease course in 111 patients. American Journal of Roentgenology, 210:899-905, Apr 2018. URL: https://doi.org/10.2214/ajr.17.18309, doi:10.2214/ajr.17.18309. This article has 62 citations and is from a peer-reviewed journal.

23. (naidu2018segmentalarterialmediolysis pages 5-6): Sailen G. Naidu, Christine O. Menias, Rahmi Oklu, Robert S. Hines, Kinan Alhalabi, Gerges Makar, Fadi E. Shamoun, Stanislav Henkin, and Robert D. McBane. Segmental arterial mediolysis: abdominal imaging of and disease course in 111 patients. American Journal of Roentgenology, 210:899-905, Apr 2018. URL: https://doi.org/10.2214/ajr.17.18309, doi:10.2214/ajr.17.18309. This article has 62 citations and is from a peer-reviewed journal.

24. (bombardieri2024segmentalarterialmediolysis pages 4-5): Giulia Bombardieri, Alessandra Rustici, Michele Caselli, Chiara Chirico, Veronica Bocchi, and Andrea Montagnani. Segmental arterial mediolysis: a challenging diagnosis in internal medicine. Italian Journal of Medicine, Sep 2024. URL: https://doi.org/10.4081/itjm.2024.1795, doi:10.4081/itjm.2024.1795. This article has 0 citations and is from a peer-reviewed journal.

25. (connolly2021segmentalarterialmediolysis media 71aca598): Caoilfhionn M Connolly, Alice Yu, Philip Seo, and Julie J Paik. Segmental arterial mediolysis: a rare cause of abdominal pain masquerading as vasculitis. Rheumatology, 60:e354-e355, Mar 2021. URL: https://doi.org/10.1093/rheumatology/keab326, doi:10.1093/rheumatology/keab326. This article has 0 citations and is from a peer-reviewed journal.

26. (najmaoui2023segmentalarterialmediolysis pages 5-6): Marine Najmaoui, Martina Pezzulo, Denis Franchimont, Frédéric Vandergheynst, and Maxime Ilzkovitz. Segmental arterial mediolysis and its mimickers: a case report and review of the literature. European Journal of Case Reports in Internal Medicine, Oct 2023. URL: https://doi.org/10.12890/2023\_004085, doi:10.12890/2023\_004085. This article has 3 citations.