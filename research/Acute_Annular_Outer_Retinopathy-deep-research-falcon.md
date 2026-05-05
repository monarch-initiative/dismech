---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T15:41:53.849597'
end_time: '2026-05-04T15:52:28.518206'
duration_seconds: 634.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Annular Outer Retinopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Annular Outer Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Annular Outer Retinopathy** covering all of the
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
- **Disease Name:** Acute Annular Outer Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Annular Outer Retinopathy** covering all of the
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


## Comprehensive Disease Characteristics Report: Acute Annular Outer Retinopathy (AAOR)

### Scope and evidence base
AAOR is extremely rare and the peer-reviewed evidence base is dominated by case reports/small case series and a limited number of narrative reviews; consequently, many knowledge-base fields (e.g., population prevalence, standardized diagnostic criteria, genetics) remain uncertain or unavailable. Key sources used here include classic descriptions (1995–2010), a larger early case series (2000), an antiretinal antibody report (2008), a multimodal imaging case report (2022), and a 2023 differential-diagnosis review that summarizes multimodal imaging patterns and misdiagnosis scenarios. (donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4, tang2008associationofantiretinal pages 1-3, simunovic2010acuteannularouter pages 1-2, gupta2022acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11)

A structured summary table is provided below.

| Domain | Findings (with brief details) | Evidence type (case report/series/review) | Key citation (PMID if known; otherwise DOI) | Year | URL |
|---|---|---|---|---:|---|
| Definition / relationship to AZOOR | Rare outer retinopathy characterized by a peri-/papillocentric gray-white annular deep retinal ring corresponding to acute scotoma; widely considered a variant within the AZOOR spectrum/complex rather than a clearly separate disease entity (donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4, interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3) | Case report; case series; review | DOI: 10.1016/S0002-9394(14)71176-6 | 1995 | https://doi.org/10.1016/S0002-9394(14)71176-6 |
| Typical symptoms | Sudden or subacute photopsias and visual-field loss/enlarged blind spot; may have decreased color vision, RAPD, floaters; visual acuity ranges from normal to severe loss depending on foveal involvement (simunovic2010acuteannularouter pages 1-2, fekrat2000acuteannularouter pages 1-4, gupta2022acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; case series; review | DOI: 10.1038/eye.2009.252 | 2010 | https://doi.org/10.1038/eye.2009.252 |
| Fundus findings | Irregular incomplete annular/peripapillary gray-white deep retinal opacification or demarcation line; may surround optic nerve, later fade, leaving retinal/RPE atrophy, pigment migration, and vessel attenuation/narrowing; usually little or no anterior chamber/vitreous inflammation (donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4, gupta2022acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; case series; review | DOI: 10.1016/S0002-9394(00)00560-2 | 2000 | https://doi.org/10.1016/S0002-9394(00)00560-2 |
| FAF findings | Hyperautofluorescent annular border/ring around optic nerve with patchy hypoautofluorescent zones of atrophy; hyperautofluorescent spots can mark active peripapillary disease (gupta2022acuteannularouter pages 1-3, simunovic2010acuteannularouter pages 1-2, interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter media 9510383f) | Case report; review; image extraction | DOI: 10.1186/s12886-022-02647-w | 2022 | https://doi.org/10.1186/s12886-022-02647-w |
| OCT findings | Loss of ellipsoid/photoreceptor layers within the ring; abrupt annulus-margin changes with nodular RPE hyperreflectivity/disruption and atrophy; acute reports also describe hyperreflectivity in outer nuclear/Henle layers followed by outer-retinal thinning/atrophy (gupta2022acuteannularouter pages 1-3, seetharam2015newinsightsinto pages 1-2, gupta2022acuteannularouter media 9510383f) | Case report; review | DOI: 10.1186/s12886-022-02647-w | 2022 | https://doi.org/10.1186/s12886-022-02647-w |
| FA findings | Often normal or minimally abnormal early; may show peripapillary/annular hyperfluorescence or patchy RPE-level hyper-/hypofluorescence; original description noted normal FA except increased retinal circulation time in involved quadrant (donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4, simunovic2010acuteannularouter pages 1-2, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; case series; review | DOI: 10.1016/S0002-9394(14)71176-6 | 1995 | https://doi.org/10.1016/S0002-9394(14)71176-6 |
| ICGA findings | Limited data; reported mild peripapillary hypofluorescence/hypofluorescent lesions on multimodal imaging reviews of AAOR/AZOOR variant cases (interlandi2023acuteonsetretinalconditions pages 10-11) | Review | DOI: 10.3390/jcm12175720 | 2023 | https://doi.org/10.3390/jcm12175720 |
| Electrophysiology / visual fields | Goldmann/Humphrey fields show enlarged blind spot, temporal or arcuate scotoma; mfERG commonly abnormal and supports outer-retinal dysfunction; ffERG may also be abnormal in related AZOOR-spectrum disease (tang2008associationofantiretinal pages 1-3, simunovic2010acuteannularouter pages 1-2, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; review | DOI: 10.1001/archophthalmol.2007.5 | 2008 | https://doi.org/10.1001/archophthalmol.2007.5 |
| Course / prognosis | Variable. Ring often disappears over weeks to months; some patients have spontaneous visual recovery or stabilization, but others develop persistent scotomas, RPE/retinal atrophy, pigment clumping/bone spicules, and progressive outer-retinal damage. Very limited case counts; 2022 report noted only 13 published cases (gupta2022acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4, donald1995acuteannularouter pages 1-3, seetharam2015newinsightsinto pages 1-2, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; case series; review | DOI: 10.1111/j.1442-9071.2005.01047.x | 2005 | https://doi.org/10.1111/j.1442-9071.2005.01047.x |
| Reported associations / etiologic hypotheses | Etiology unknown. Proposed mechanisms include immune reaction after occult viral illness, autoimmune retinopathy, paraneoplastic association (breast carcinoma), ANA positivity, and antiretinal antibodies; infectious workups often negative. Reviews also mention interplay of genetic, immune, and environmental triggers in AZOOR-complex disease (gupta2022acuteannularouter pages 1-3, tang2008associationofantiretinal pages 1-3, simunovic2010acuteannularouter pages 1-2, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; small case series; review | DOI: 10.1001/archophthalmol.2007.5 | 2008 | https://doi.org/10.1001/archophthalmol.2007.5 |
| Treatments tried / outcomes | No established therapy or trials. Reported attempts include observation alone, oral prednisone, IV methylprednisolone/oral prednisone, valacyclovir, IV acyclovir. Outcomes mixed: some subjective or partial functional improvement/stabilization, some spontaneous improvement, others worsen despite steroids; evidence remains anecdotal (fekrat2000acuteannularouter pages 1-4, tang2008associationofantiretinal pages 1-3, gupta2022acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11) | Case report; case series; review | DOI: 10.1016/S0002-9394(00)00560-2 | 2000 | https://doi.org/10.1016/S0002-9394(00)00560-2 |


*Table: This table compiles the main clinically relevant features of acute annular outer retinopathy from the available case-based literature and recent reviews. It is useful as a quick reference for disease definition, imaging, hypothesized mechanisms, and the limited treatment evidence.*

---

## 1. Disease Information

### 1.1 What is the disease?
Acute annular outer retinopathy (AAOR) is a rare acute-onset outer retinal disorder characterized clinically by an annular peri-/peripapillary gray-white ring or demarcation line and sudden onset of a scotoma, with evidence of outer retinal disruption on multimodal testing. (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4)

**Authoritative description (primary literature):** In the original AAOR case report, a “23-year-old man developed a rapid-onset, large, dense scotoma … associated with a peculiar gray intraretinal ring corresponding to the edge of the scotoma”. (donald1995acuteannularouter pages 1-3)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)
From the retrieved full-text evidence set, no OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO identifiers were explicitly provided; therefore these identifiers cannot be reliably populated from current evidence. (interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3, donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4)

### 1.3 Common synonyms / alternative names
Synonyms and near-synonyms appearing across sources include:
- **Acute annular outer retinopathy (AAOR)** (preferred) (interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3)
- **Acute annular outer retinopathy as a variant of AZOOR** (formulation used in classic title/description) (donald1995acuteannularouter pages 1-3)
- In some review contexts, AAOR is discussed as an **AZOOR-complex/AZOOR-variant** entity. (interlandi2023acuteonsetretinalconditions pages 10-11)

### 1.4 Evidence source type
Evidence is primarily **individual patient-level clinical observations** (case reports and small case series) aggregated secondarily in reviews. (fekrat2000acuteannularouter pages 1-4, tang2008associationofantiretinal pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
AAOR’s etiology remains **unknown** in primary reports, with leading hypotheses centered on **immune-mediated** and/or **post-viral** processes.

- The original report concluded: “The cause of this disorder, which affects primarily the outer retina, was not determined,” while speculating that the gray border “represents an immune ring phenomenon”. (donald1995acuteannularouter pages 1-3)
- A 2010 report reiterates: “The aetiology of AAOR remains unknown, although an autoimmune mechanism has been suggested.” (simunovic2010acuteannularouter pages 1-2)
- A 2023 review states that many authors speculate AAOR is part of the AZOOR complex and “secondary to an immune reaction following a viral illness”. (interlandi2023acuteonsetretinalconditions pages 10-11)

### 2.2 Risk factors
No validated, quantified risk factors are established in the retrieved evidence. Demographic patterns suggested by AZOOR-complex literature (young women) may apply broadly, but AAOR itself has been described in both sexes and across a wide age range in case series. (fekrat2000acuteannularouter pages 1-4, interlandi2023acuteonsetretinalconditions pages 10-11)

### 2.3 Protective factors
No protective factors were identified in the retrieved evidence. (interlandi2023acuteonsetretinalconditions pages 10-11, fekrat2000acuteannularouter pages 1-4)

### 2.4 Gene–environment interactions
No gene–environment interactions are reported for AAOR in the retrieved evidence. (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

---

## 3. Phenotypes

### 3.1 Core symptoms and signs (with ontology suggestions)
AAOR typically presents with acute or subacute visual field symptoms and photopsias, with variable central acuity depending on foveal involvement.

**Symptoms / functional phenotypes**
- **Photopsia** (HPO: *Photopsia* HP:0001133) (simunovic2010acuteannularouter pages 1-2, gupta2022acuteannularouter pages 1-3)
- **Scotoma / visual field defect** (HPO: *Scotoma* HP:0000575) (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)
- **Enlarged blind spot** (HPO: *Enlarged blind spot* HP:0031796) (gupta2022acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11)
- **Reduced color vision** (HPO: *Abnormality of color vision* HP:0000551) reported in a 2022 case (gupta2022acuteannularouter pages 1-3)

**Ocular examination features**
- **Relative afferent pupillary defect (RAPD)** (HPO: *Relative afferent pupillary defect* HP:0030407) described in AAOR/AZOOR variant discussions and cases (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)
- **Minimal/no vitreous inflammation** (HPO approximation: *Absent vitreous inflammation*; not a standard HPO term—record clinically as “no vitreous cells/haze”) (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

### 3.2 Imaging phenotypes (multimodal)
AAOR is defined largely by multimodal imaging patterns:
- Fundus: peri-/papillocentric gray-white ring/demarcation line (interlandi2023acuteonsetretinalconditions pages 10-11, simunovic2010acuteannularouter pages 1-2)
- Fundus autofluorescence (FAF): annular hyperautofluorescent border with patchy hypoautofluorescent atrophy zones in a 2022 report (gupta2022acuteannularouter pages 1-3) and hyperfluorescent peripapillary spots in 2010 report (simunovic2010acuteannularouter pages 1-2)
- OCT: ellipsoid zone/photoreceptor layer loss within the affected annulus; nodular RPE hyperreflectivity/disruption described in 2022 case (gupta2022acuteannularouter pages 1-3)

**Visual evidence (fundus/OCT/FAF) from Gupta et al., 2022:** fundus, OCT, and FAF figures showing the characteristic annular lesion pattern were retrieved. (gupta2022acuteannularouter media 9510383f, gupta2022acuteannularouter media 0cc2fd2b, gupta2022acuteannularouter media 8798eaea)

### 3.3 Age of onset, severity, progression
- **Onset**: typically acute or subacute, sometimes with progression for ~weeks before stabilization (donald1995acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11)
- **Severity**: visual acuity can be preserved early (“visual acuity … 20/15”) in the original case, but can become severe with foveal involvement (donald1995acuteannularouter pages 1-3, gupta2022acuteannularouter pages 1-3)
- **Progression**: variable; ring may fade but persistent scotomas and later pigmentary/bone-spicule changes can develop (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

### 3.4 Quality of life impact
No formal QoL instruments (e.g., EQ-5D, VFQ-25) were reported in the retrieved evidence. Impact is inferred to be driven by persistent scotomas and/or central vision loss when the fovea is involved. (gupta2022acuteannularouter pages 1-3, donald1995acuteannularouter pages 1-3)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and pathogenic variants
No AAOR-specific causal genes, pathogenic variants, or Mendelian inheritance patterns were reported in the retrieved evidence set. (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4)

### 4.2 Modifier genes / epigenetics / chromosomal abnormalities
No evidence found in the retrieved sources. (interlandi2023acuteonsetretinalconditions pages 10-11)

**Interpretation:** AAOR is treated in the literature as an acquired outer retinopathy within the AZOOR spectrum rather than a heritable monogenic disease. (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
No established lifestyle or toxin exposures are implicated in the AAOR reports within the retrieved evidence. (fekrat2000acuteannularouter pages 1-4, gupta2022acuteannularouter pages 1-3)

### 5.2 Infectious agents
Direct infectious causation is unproven; however, herpetic etiologies have been considered in some reports and viral illness is hypothesized as a trigger in immune-mediated models.

A 2010 case report notes **no serologic evidence of recent infection** with multiple viruses tested: “no serological evidence of recent infection with HSV, HZV, EBV, CMV, Coxsackie virus or echovirus”. (simunovic2010acuteannularouter pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic model (causal chain)
A working model supported by clinical course and multimodal imaging is:
1) **Trigger** (hypothesized viral exposure and/or autoimmune/paraneoplastic immune activation) →
2) **Immune-mediated injury to outer retina/photoreceptors** (outer retinal dysfunction evidenced by scotoma, mfERG abnormalities) →
3) **Structural photoreceptor/ellipsoid zone loss** (OCT) and **RPE changes/atrophy** (FAF and later pigmentary changes) →
4) **Persistent scotoma** and potential secondary pigment migration/bone-spicule changes. (donald1995acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3)

### 6.2 Immune system involvement and antiretinal antibodies
Evidence supporting immune involvement includes:
- “immune ring phenomenon” speculation in classic report (donald1995acuteannularouter pages 1-3)
- ANA positivity in a case with systemic symptoms (simunovic2010acuteannularouter pages 1-2)
- **Antiretinal antibodies**: a 2008 case series reported indirect immunohistochemistry evidence where “positive reactivity was detected along the inner nuclear layers and nerve fiber layers… [and] very faint staining … along the outer nuclear layers,” while “no reactivity was seen in controls”. (tang2008associationofantiretinal pages 1-3)

### 6.3 Candidate pathways / processes and ontology suggestions
Because AAOR lacks molecular profiling in the retrieved evidence, pathway mapping is necessarily hypothesis-driven.

Suggested GO Biological Process terms (hypothesis-aligned):
- **GO:0006955** immune response
- **GO:0002250** adaptive immune response
- **GO:0006915** apoptotic process (outer retinal degeneration)
- **GO:0030198** extracellular matrix organization (for scarring/subretinal fibrosis described in some cases) (fekrat2000acuteannularouter pages 5-8)

Suggested Cell Ontology (CL) terms (site of injury/involvement):
- **CL:0000210** photoreceptor cell (rods/cones)
- **CL:0000134** retinal pigment epithelial cell

---

## 7. Anatomical Structures Affected

### 7.1 Organ / tissue level
- **Primary organ**: eye/retina. (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

### 7.2 Tissue and cell level (with Uberon suggestions)
- **Outer retina / photoreceptor layers** (supported by OCT/ERG and classic discussion of receptor cell involvement) (donald1995acuteannularouter pages 1-3, gupta2022acuteannularouter pages 1-3)
- **RPE** involvement/atrophy as a downstream or evolving feature (gupta2022acuteannularouter pages 1-3, donald1995acuteannularouter pages 1-3)

Suggested UBERON terms (approximate):
- **UBERON:0000966** retina
- **UBERON:0001960** retinal pigment epithelium

### 7.3 Localization and laterality
- Often described as **peripapillary/papillocentric** annular lesions (interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3)
- Often **unilateral**, but bilateral and sequential cases are reported (gupta2022acuteannularouter pages 1-3, fekrat2000acuteannularouter pages 1-4)

---

## 8. Temporal Development

### 8.1 Onset pattern
AAOR is characteristically **acute onset** with possible progression for ~weeks. The original case had “progressive enlargement … for three weeks” before stabilization. (donald1995acuteannularouter pages 1-3)

### 8.2 Progression and stages (practical staging)
A pragmatic staging consistent with case descriptions:
- **Acute phase**: visible gray-white annular ring/demarcation; expanding scotoma; mfERG abnormalities (donald1995acuteannularouter pages 1-3, tang2008associationofantiretinal pages 1-3)
- **Subacute**: ring fades/disappears; scotoma stabilizes or partially improves (interlandi2023acuteonsetretinalconditions pages 10-11, simunovic2010acuteannularouter pages 1-2)
- **Chronic**: RPE atrophy, pigment migration, possible bone-spicule pigment clumping; persistent scotoma (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
No incidence or prevalence estimates were found in the retrieved full-text evidence. (interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3)

**Case counts/statistics available from the evidence set:**
- A 2000 case series reported **4 patients** (2 women aged 29 and 32; 2 men aged 71 and 79). (fekrat2000acuteannularouter pages 1-4)
- A 2022 case report states: “There are only **13 cases** that have been reported in the literature to date.” (gupta2022acuteannularouter pages 1-3)

### 9.2 Inheritance
No inherited pattern is supported by the retrieved literature; AAOR is presented as an acquired condition. (interlandi2023acuteonsetretinalconditions pages 10-11, donald1995acuteannularouter pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical tests and imaging (current real-world implementation)
AAOR diagnosis is primarily clinical and imaging-based.

**Multimodal imaging is central**: A 2023 review describes AAOR as “characterized by a peri-papillary gray-white ring, disruption of the outer retina within the affected area, and sudden onset of a scotoma” and illustrates a multimodal package: ultra-widefield autofluorescence hyperautofluorescent ring, OCT photoreceptor layer loss, FA hyperfluorescent annulus, and ICGA mild peripapillary hypofluorescence. (interlandi2023acuteonsetretinalconditions pages 10-11)

**Functional testing**
- Visual fields (Goldmann/Humphrey) to document blind spot enlargement/scotomas (gupta2022acuteannularouter pages 1-3, tang2008associationofantiretinal pages 1-3)
- Electrophysiology: mfERG depression supporting outer retinal dysfunction (tang2008associationofantiretinal pages 1-3, simunovic2010acuteannularouter pages 1-2)

**Laboratory evaluation (rule-out and association workup)**
Case-based workups often include infectious serologies (herpes viruses, HIV, etc.), autoimmune markers, and systemic evaluation for malignancy when clinically indicated. (simunovic2010acuteannularouter pages 1-2, tang2008associationofantiretinal pages 1-3, gupta2022acuteannularouter pages 1-3)

### 10.2 Differential diagnosis
AAOR (and AZOOR spectrum conditions) may be mistaken for neuro-ophthalmic disease (optic neuritis) because RAPD can occur and fundus findings may be subtle early; a 2023 review emphasizes this misdiagnosis risk and the need for multimodal retinal imaging. (interlandi2023acuteonsetretinalconditions pages 10-11)

Other retinal acute-onset entities considered in differential (as part of broader acute-onset retinal disorders) include AMN/PAMM and other AZOOR-complex entities. (interlandi2023acuteonsetretinalconditions pages 10-11)

### 10.3 Genetic testing
No AAOR-directed genetic testing approach is suggested by the retrieved evidence. (interlandi2023acuteonsetretinalconditions pages 10-11)

---

## 11. Outcome / Prognosis

Prognosis is **variable**.
- Stabilization can occur after an initial expansion phase: “progressive enlargement … for three weeks … followed by stabilization”. (donald1995acuteannularouter pages 1-3)
- Structural and pigmentary sequelae can occur: “Development of pigmentary changes in the form of bone spicules was noted after a year within the affected area”. (interlandi2023acuteonsetretinalconditions pages 10-11)
- Severe vision loss is possible when the lesion crosses the fovea; in the 2022 case, high-dose prednisone was started but visual acuity worsened to 20/400 and later 20/500/count-fingers during rapid progression. (gupta2022acuteannularouter pages 1-3)

No formal survival/mortality outcomes apply, and no prognostic models or biomarkers are validated in the retrieved evidence. (interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3)

---

## 12. Treatment

### 12.1 Evidence summary
There is **no established, evidence-based therapy** for AAOR; reported interventions are anecdotal and based on small numbers.

Treatments attempted in case reports/series include:
- **Observation/no treatment** (some cases) (fekrat2000acuteannularouter pages 1-4, interlandi2023acuteonsetretinalconditions pages 10-11)
- **Systemic corticosteroids**: oral prednisone 40 mg daily tapered over months in a 2008 case; subjective improvement in some series; lack of improvement/worsening in a 2022 case despite high-dose prednisone (tang2008associationofantiretinal pages 1-3, fekrat2000acuteannularouter pages 1-4, gupta2022acuteannularouter pages 1-3)
- **Antivirals**: valacyclovir used when necrosis/herpetic disease considered; IV acyclovir used in suspected herpetic etiology in literature summarized by review/series (tang2008associationofantiretinal pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11, fekrat2000acuteannularouter pages 1-4)

### 12.2 MAXO suggestions
- Systemic corticosteroid therapy (MAXO term suggestion: *corticosteroid therapy*) (gupta2022acuteannularouter pages 1-3, tang2008associationofantiretinal pages 1-3)
- Antiviral therapy (MAXO term suggestion: *antiviral therapy*) (tang2008associationofantiretinal pages 1-3)
- Ophthalmic imaging (MAXO term suggestion: *optical coherence tomography*; *fundus autofluorescence imaging*) (interlandi2023acuteonsetretinalconditions pages 10-11, gupta2022acuteannularouter pages 1-3)

### 12.3 Clinical trials
No AAOR-specific clinical trials were identified in the retrieved ClinicalTrials.gov results within this session. (interlandi2023acuteonsetretinalconditions pages 10-11)

---

## 13. Prevention

No established primary prevention strategies are supported by AAOR-specific evidence. Practical secondary/tertiary prevention is limited to early recognition (to avoid misdiagnosis and unnecessary neurologic workup) and monitoring for progression/complications within the AZOOR spectrum using multimodal imaging and functional testing. (interlandi2023acuteonsetretinalconditions pages 10-11)

---

## 14. Other Species / Natural Disease

No naturally occurring AAOR in other species was identified in the retrieved evidence. (interlandi2023acuteonsetretinalconditions pages 10-11)

---

## 15. Model Organisms

No AAOR-specific model organisms or in vitro models were identified in the retrieved evidence. (interlandi2023acuteonsetretinalconditions pages 10-11)

---

## Recent developments and latest research emphasis (2023–2024)

### 2023: Multimodal imaging and differential diagnosis integration
A 2023 review on acute-onset retinal conditions that mimic optic neuritis emphasizes AAOR as a rare entity and provides a multimodal imaging framework (ultra-widefield FAF, OCT, FA, ICGA) to detect outer retinal disruption and avoid misdiagnosis as optic neuritis. (Publication date: Sep 2023; URL: https://doi.org/10.3390/jcm12175720) (interlandi2023acuteonsetretinalconditions pages 10-11)

### 2024
No AAOR-specific 2024 primary sources were retrievable in the current evidence set; recent-year knowledge is therefore represented by 2022–2023 publications and earlier foundational reports. (gupta2022acuteannularouter pages 1-3, interlandi2023acuteonsetretinalconditions pages 10-11)

---

## Notes on PMID requirement
Several retrieved PDFs/excerpts did not display PMIDs in the parsed text; therefore citations are provided using **DOIs/URLs** from the retrieved sources. For strict PMID-only population of a knowledge base, a follow-on PubMed-anchored pass would be needed to map each DOI to its PMID.

---

## Key source URLs (with publication dates)
- Gass & Stern. *Am J Ophthalmol.* **Mar 1995**. https://doi.org/10.1016/S0002-9394(14)71176-6 (donald1995acuteannularouter pages 1-3)
- Fekrat et al. *Am J Ophthalmol.* **Nov 2000**. https://doi.org/10.1016/S0002-9394(00)00560-2 (fekrat2000acuteannularouter pages 1-4)
- Tang et al. *Arch Ophthalmol.* **Jan 2008**. https://doi.org/10.1001/archophthalmol.2007.5 (tang2008associationofantiretinal pages 1-3)
- Simunovic et al. *Eye.* **Jun 2010** (online Oct 2009). https://doi.org/10.1038/eye.2009.252 (simunovic2010acuteannularouter pages 1-2)
- Gupta et al. *BMC Ophthalmology.* **Nov 2022**. https://doi.org/10.1186/s12886-022-02647-w (gupta2022acuteannularouter pages 1-3)
- Interlandi et al. *J Clin Med.* **Sep 2023**. https://doi.org/10.3390/jcm12175720 (interlandi2023acuteonsetretinalconditions pages 10-11)


References

1. (donald1995acuteannularouter pages 1-3): J. DONALD, M. GASS, and CHARLES STERN. Acute annular outer retinopathy as a variant of acute zonal occult outer retinopathy. American journal of ophthalmology, 119 3:330-4, Mar 1995. URL: https://doi.org/10.1016/s0002-9394(14)71176-6, doi:10.1016/s0002-9394(14)71176-6. This article has 76 citations and is from a domain leading peer-reviewed journal.

2. (fekrat2000acuteannularouter pages 1-4): Sharon Fekrat, C.P Wilkinson, Benjamin Chang, Lawrence Yannuzzi, Howard Schatz, and Julia A Haller. Acute annular outer retinopathy: report of four cases. American journal of ophthalmology, 130 5:636-44, Nov 2000. URL: https://doi.org/10.1016/s0002-9394(00)00560-2, doi:10.1016/s0002-9394(00)00560-2. This article has 58 citations and is from a domain leading peer-reviewed journal.

3. (tang2008associationofantiretinal pages 1-3): Johnny Tang, R. Stevens, A. Okada, M. Chin, R. Nussenblatt, and C. Chan. Association of antiretinal antibodies in acute annular outer retinopathy. Archives of ophthalmology, 126 1:130-2, Jan 2008. URL: https://doi.org/10.1001/archophthalmol.2007.5, doi:10.1001/archophthalmol.2007.5. This article has 26 citations.

4. (simunovic2010acuteannularouter pages 1-2): M P Simunovic, E H Hughes, B S Townend, and I-V Ho. Acute annular outer retinopathy with systemic symptoms. Eye, 24:1125-1126, Jun 2010. URL: https://doi.org/10.1038/eye.2009.252, doi:10.1038/eye.2009.252. This article has 14 citations and is from a peer-reviewed journal.

5. (gupta2022acuteannularouter pages 1-3): Rishi B. Gupta, Harry Dang, Danah Albreiki, Michael LE. Dollin, Bonnie Weston, and Chloe C. Gottlieb. Acute annular outer retinopathy preceded by invasive ductal breast carcinoma: a case report. BMC Ophthalmology, Nov 2022. URL: https://doi.org/10.1186/s12886-022-02647-w, doi:10.1186/s12886-022-02647-w. This article has 4 citations and is from a peer-reviewed journal.

6. (interlandi2023acuteonsetretinalconditions pages 10-11): Emanuela Interlandi, Francesco Pellegrini, Chiara Giuffrè, Daniele Cirone, Daniele Brocca, Andrew G. Lee, and Giuseppe Casalino. Acute-onset retinal conditions mimicking acute optic neuritis: overview and differential diagnosis. Journal of Clinical Medicine, 12:5720, Sep 2023. URL: https://doi.org/10.3390/jcm12175720, doi:10.3390/jcm12175720. This article has 5 citations.

7. (gupta2022acuteannularouter media 9510383f): Rishi B. Gupta, Harry Dang, Danah Albreiki, Michael LE. Dollin, Bonnie Weston, and Chloe C. Gottlieb. Acute annular outer retinopathy preceded by invasive ductal breast carcinoma: a case report. BMC Ophthalmology, Nov 2022. URL: https://doi.org/10.1186/s12886-022-02647-w, doi:10.1186/s12886-022-02647-w. This article has 4 citations and is from a peer-reviewed journal.

8. (seetharam2015newinsightsinto pages 1-2): Shabari S. Seetharam, Lee M. Jampol, and Manjot K. Gill. New insights into acute annular outer retinopathy. RETINAL Cases & Brief Reports, 9:1-6, Jan 2015. URL: https://doi.org/10.1097/icb.0000000000000070, doi:10.1097/icb.0000000000000070. This article has 15 citations and is from a peer-reviewed journal.

9. (gupta2022acuteannularouter media 0cc2fd2b): Rishi B. Gupta, Harry Dang, Danah Albreiki, Michael LE. Dollin, Bonnie Weston, and Chloe C. Gottlieb. Acute annular outer retinopathy preceded by invasive ductal breast carcinoma: a case report. BMC Ophthalmology, Nov 2022. URL: https://doi.org/10.1186/s12886-022-02647-w, doi:10.1186/s12886-022-02647-w. This article has 4 citations and is from a peer-reviewed journal.

10. (gupta2022acuteannularouter media 8798eaea): Rishi B. Gupta, Harry Dang, Danah Albreiki, Michael LE. Dollin, Bonnie Weston, and Chloe C. Gottlieb. Acute annular outer retinopathy preceded by invasive ductal breast carcinoma: a case report. BMC Ophthalmology, Nov 2022. URL: https://doi.org/10.1186/s12886-022-02647-w, doi:10.1186/s12886-022-02647-w. This article has 4 citations and is from a peer-reviewed journal.

11. (fekrat2000acuteannularouter pages 5-8): Sharon Fekrat, C.P Wilkinson, Benjamin Chang, Lawrence Yannuzzi, Howard Schatz, and Julia A Haller. Acute annular outer retinopathy: report of four cases. American journal of ophthalmology, 130 5:636-44, Nov 2000. URL: https://doi.org/10.1016/s0002-9394(00)00560-2, doi:10.1016/s0002-9394(00)00560-2. This article has 58 citations and is from a domain leading peer-reviewed journal.