---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T11:05:45.843858'
end_time: '2026-05-10T11:26:46.388556'
duration_seconds: 1260.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Punctate Palmoplantar Keratoderma
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Punctate Palmoplantar Keratoderma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Punctate Palmoplantar Keratoderma** covering all of the
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
- **Disease Name:** Punctate Palmoplantar Keratoderma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Punctate Palmoplantar Keratoderma** covering all of the
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


## Comprehensive Research Report: Punctate Palmoplantar Keratoderma (PPPK)

### Target disease
- **Disease name:** Punctate palmoplantar keratoderma (PPPK)
- **Category:** Mendelian (primarily **PPPK type 1 / PPKP1 / Buschke–Fischer–Brauer**, autosomal dominant)
- **MONDO ID:** Not identified in the retrieved full-text sources in this run (reporting limitation).

---

## 1. Disease Information

### 1.1 Overview and definition (current understanding)
Punctate palmoplantar keratoderma (punctate PPK; PPPK/PPKP) is a rare disorder of keratinization characterized by multiple discrete hyperkeratotic papules/lesions on the palms and soles, often progressive with age and prone to coalescence at pressure-bearing sites. A classic description for type 1 notes “progressive development of discrete areas of hyperkeratosis on the palms and soles, followed by more extensive diffuse hyperkeratosis on the pressure-bearing areas of plantar skin.” (matsuzawa2013heterozygousmutationsin pages 1-2)

### 1.2 Key identifiers and subtype taxonomy
In the landmark genetics literature, OMIM recognizes three inherited punctate PPK types: 
- **PPKP1 (Buschke–Fischer–Brauer)**: **OMIM #148600**
- **PPKP2 (porokeratotic type / porokeratosis punctata palmaris et plantaris)**: **OMIM #175860**
- **PPKP3 (acrokeratoelastoidosis)**: **OMIM #101850** (pohler2012haploinsufficiencyforaagab pages 1-2)

The 2021 Japanese Dermatological Association guidelines further subdivide punctate type 1 into:
- **Punctate PPK type 1A:** **AAGAB**
- **Punctate PPK type 1B:** **COL14A1** (yoneda2021japaneseguidelinesfor pages 4-5)

**Orphanet / ICD-10 / ICD-11 / MeSH / MONDO:** these identifiers were not explicitly provided in the retrieved excerpts; therefore, they cannot be reliably populated from this evidence set.

### 1.3 Common synonyms and alternative names
- Punctate palmoplantar keratoderma (PPPK)
- Punctate PPK / PPKP
- **Buschke–Fischer–Brauer disease** (type 1) (gram2023ispunctatepalmoplantar pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5)
- Porokeratosis punctata palmaris et plantaris (type 2) (gram2023ispunctatepalmoplantar pages 1-2)
- Acrokeratoelastoidosis (type 3) (gram2023ispunctatepalmoplantar pages 1-2)

### 1.4 Evidence sources (individual vs aggregated)
The evidence base is dominated by families and case reports/series rather than large epidemiologic cohorts. A 2023 systematic review identified **45 included studies**, where most were **single-family** or **multi-family** reports; it counted **280 index cases** and **817 total affected individuals** across the literature. The review emphasized limitations of study quality and concluded it could not confirm a malignancy association. (gram2023ispunctatepalmoplantar pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (genetic and mechanistic)
**PPPK type 1 (PPKP1/Buschke–Fischer–Brauer)** is most strongly associated with **heterozygous loss-of-function variants in AAGAB**, consistent with **haploinsufficiency**. (pohler2012haploinsufficiencyforaagab pages 1-2, pohler2014newandrecurrent pages 1-2)

A less frequent genetic association reported for punctate PPK type 1 includes **COL14A1**, emphasized in guidelines as punctate type 1B and referenced as occurring in Chinese pedigrees. (yoneda2021japaneseguidelinesfor pages 4-5, thomas2020diagnosisandmanagement pages 5-6)

### 2.2 Risk factors
**Genetic risk:**
- **AAGAB** heterozygous truncating/splice variants (nonsense/frameshift/splice) are repeatedly observed in pedigrees and case series. Recurrent variants include **AAGAB c.370C>T (p.Arg124Ter)**. (pohler2014newandrecurrent pages 2-3, pohler2014newandrecurrent pages 1-2)

**Environmental/occupational modifiers:**
- Lesions may worsen with **water exposure** and at **pressure/friction** sites (knowles2023punctatepalmoplantarkeratoderma pages 4-5, elhaji2020aagabmutationsin pages 1-2).
- Lesions can be worse in **manual labourers** (trauma/friction exposure). (thomas2020diagnosisandmanagement pages 5-6)

**Acquired punctate PPK phenocopies:**
- The 2023 systematic review notes PPK can be hereditary or acquired due to exposures/conditions such as “**arsenic exposure, menopause, and paraneoplastic syndromes**.” (gram2023ispunctatepalmoplantar pages 1-2)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interaction
Direct GxE interaction studies were not identified in this evidence set; however, multiple sources consistently indicate that mechanical stress/pressure and water exposure can modulate severity in genetically affected individuals (suggesting an interaction between inherited predisposition and local environmental triggers). (thomas2020diagnosisandmanagement pages 5-6, elhaji2020aagabmutationsin pages 1-2)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes
**Morphology:** multiple punctate hyperkeratotic papules/lesions on palms and soles, which may coalesce into plaques at pressure-bearing areas. (matsuzawa2013heterozygousmutationsin pages 1-2, pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5)

**Pain and functional impact:** plantar pain can be prominent; a case series highlights plantar pain with functional impact on walking/standing and notes that manual paring and analgesia can help. (zamiri2019painfulpunctatepalmoplantar pages 5-6)

**Progression:** a large Danish cohort reported progression in **31/42 punctate probands (74%)**, stability in **8/42 (19%)**, and improvement in **1/42 (2%)**. (gram2025clinicalandgenetic pages 3-4)

**Distribution:** in the Danish cohort, punctate probands had **palms and soles involvement in 40/42 (95%)**. (gram2025clinicalandgenetic pages 3-4)

### 3.2 Age of onset
- Often begins in adolescence/early adulthood, but range is broad. Median onset for punctate PPK in the Danish cohort was **19.0 years (range 5–47)**. (gram2025clinicalandgenetic pages 3-4)
- A pain-focused series reports onsets spanning childhood through later adulthood (e.g., ~8 to 50s). (zamiri2019painfulpunctatepalmoplantar pages 5-6)

### 3.3 Histopathology
A characteristic lesion histology described in genetic studies includes a **central epidermal depression** with **hypergranulosis** and an overlying **orthokeratotic layer**; immunostaining suggests a **hyperproliferative** basal compartment. (pohler2012haploinsufficiencyforaagab pages 1-2)

### 3.4 Suggested HPO terms (examples)
(IDs not provided in evidence; listed as term labels for mapping)
- Punctate palmoplantar keratoderma
- Palmoplantar hyperkeratosis
- Hyperkeratosis
- Plantar pain
- Progressive skin disease
- Verrucous skin lesion / Hyperkeratotic papule

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **AAGAB** (major gene for PPKP1/PPPK1 type 1A) (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5)
- **COL14A1** (reported; emphasized as type 1B in guidelines; rare compared to AAGAB) (yoneda2021japaneseguidelinesfor pages 4-5, thomas2020diagnosisandmanagement pages 5-6)

### 4.2 Pathogenic variant classes and functional consequences
**AAGAB** variants reported across studies are predominantly truncating/splice variants consistent with **loss of function** and **haploinsufficiency** (pohler2012haploinsufficiencyforaagab pages 1-2, pohler2014newandrecurrent pages 1-2). A 2014 multi-family report noted “**27 distinct loss-of-function mutations** reported in AAGAB,” illustrating substantial allelic heterogeneity. (pohler2014newandrecurrent pages 2-3)

A large 2019 series lists many AAGAB truncating/splice variants across families and includes both familial and sporadic cases, supporting dominant inheritance and recurrent mutational spectra. (zamiri2019painfulpunctatepalmoplantar pages 5-6)

**Founder variant example (recent development):** A 2024 Clinical Genetics study demonstrates **AAGAB c.370C>T (p.Arg124Ter)** is a **founder variant** in Southern Denmark: shared haplotype **3.0 Mb** and an estimated most recent common ancestor **12.1 generations (~339 years; CI 137–568)**; it recommends initial screening for this variant in the region and potentially all Danish punctate PPK patients. (gram2024identificationofa pages 1-2)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic drivers, or chromosomal abnormalities specific to PPPK were identified in the retrieved sources.

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle contributors
- **Mechanical stress/friction:** worse in manual labourers; pressure points are common sites of coalescence. (thomas2020diagnosisandmanagement pages 5-6, pohler2012haploinsufficiencyforaagab pages 1-2)
- **Water exposure:** reported to worsen papules in several reports. (knowles2023punctatepalmoplantarkeratoderma pages 4-5, elhaji2020aagabmutationsin pages 1-2)

### 5.2 Infectious agents
No infectious triggers were identified as causal in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Mechanistic causal chain (AAGAB/PPKP1)
AAGAB encodes p34 (α- and γ-adaptin–binding protein), linked to clathrin adaptor complexes and membrane trafficking. Functional work supports the causal chain:
1) **AAGAB loss-of-function → p34 deficiency** (haploinsufficiency) (pohler2012haploinsufficiencyforaagab pages 1-2, giehl2012nonsensemutationsin pages 1-2)
2) **Disrupted vesicle trafficking/endocytic recycling**, with ultrastructural abnormalities in intracellular vesicle biology in lesional epidermis (pohler2012haploinsufficiencyforaagab pages 1-2, pohler2012haploinsufficiencyforaagab pages 4-5)
3) **Increased EGFR protein and activation**: keratinocyte knockdown leads to markedly increased EGFR protein and phosphorylation, consistent with impaired receptor turnover (pohler2012haploinsufficiencyforaagab pages 4-5)
4) **Keratinocyte hyperproliferation**: increased cell division in vitro and hyperproliferative lesions in vivo (pohler2012haploinsufficiencyforaagab pages 1-2)
5) Clinical manifestation as **focal hyperproliferative hyperkeratosis** (punctate lesions) (pohler2012haploinsufficiencyforaagab pages 1-2)

A complementary mechanistic discussion highlights that impaired RTK endocytosis (EGFR/Axl) could sustain growth-factor signaling and drive hyperkeratosis. (matsuzawa2013heterozygousmutationsin pages 4-4)

### 6.2 Suggested GO biological process / cellular component terms (labels)
- Endocytosis; clathrin-mediated endocytosis (pohler2012haploinsufficiencyforaagab pages 4-5)
- Vesicle-mediated transport; endosomal recycling (pohler2012haploinsufficiencyforaagab pages 1-2)
- EGFR signaling pathway / receptor tyrosine kinase signaling (pohler2012haploinsufficiencyforaagab pages 4-5)
- Regulation of keratinocyte proliferation (pohler2012haploinsufficiencyforaagab pages 1-2)

### 6.3 Suggested CL (cell types)
- Keratinocyte; basal keratinocyte (pohler2012haploinsufficiencyforaagab pages 4-5)

### 6.4 Molecular profiling (transcriptomics/proteomics/metabolomics)
No disease-specific omics profiling studies were identified in the retrieved sources.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- **Primary sites:** palmar and plantar skin (thick glabrous epidermis), frequently both. (gram2025clinicalandgenetic pages 3-4)

### 7.2 Suggested UBERON terms (labels)
- Skin of palm; skin of sole; epidermis

### 7.3 Subcellular/cellular compartments
Mechanistic evidence implicates vesicular/endocytic compartments (clathrin adaptor-related trafficking and receptor turnover). (pohler2012haploinsufficiencyforaagab pages 4-5)

---

## 8. Temporal Development

### 8.1 Onset
Typically after childhood/adolescence, with broad variability by family and cohort; Danish cohort median 19 years. (gram2025clinicalandgenetic pages 3-4)

### 8.2 Course
Often chronic and progressive; lesions increase in number and can coalesce over time. (pohler2012haploinsufficiencyforaagab pages 1-2, gram2025clinicalandgenetic pages 3-4)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Type 1 punctate PPK is classically **autosomal dominant** with variable expressivity; AAGAB variants segregate in pedigrees with multiple affected generations. (pohler2012haploinsufficiencyforaagab pages 1-2, pohler2014newandrecurrent pages 1-2)

### 9.2 Epidemiology and statistics
- Prevalence estimates in a review of inherited PPK: **“1 in 100,000”** with AD inheritance. (thomas2020diagnosisandmanagement pages 5-6)
- A case report cites an estimated prevalence of **1.17 per 100,000**. (knowles2023punctatepalmoplantarkeratoderma pages 4-5)

### 9.3 Founder effects and population distribution (recent)
A 2024 founder study in Southern Denmark supports a founder origin for **AAGAB c.370C>T (p.Arg124Ter)** with a **3.0 Mb shared haplotype** and estimated origin ~**339 years**; it recommends first-tier screening for this variant in Denmark. (gram2024identificationofa pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
Key features include punctate hyperkeratotic lesions on palms/soles; guidelines emphasize excluding look-alikes such as callus/clavus and viral warts when diagnosing PPK. (yoneda2021japaneseguidelinesfor pages 9-10)

### 10.2 Histopathology
Characteristic lesions may show central epidermal depression with orthokeratosis and hypergranulosis, consistent with hyperproliferation. (pohler2012haploinsufficiencyforaagab pages 1-2)

### 10.3 Genetic testing strategy (expert consensus / implementation)
- Guidelines recommend genetic counseling and consent in hereditary PPK (yoneda2021japaneseguidelinesfor pages 10-12).
- In Denmark, initial testing for founder **AAGAB c.370C>T (p.Arg124Ter)** is recommended for regional patients and potentially all Danish punctate PPK patients. (gram2024identificationofa pages 1-2)

### 10.4 Differential diagnosis
The punctate phenotype should prompt consideration of punctate PPK types 1A/1B/2/3 and related entities (including Cole disease), and recognition that PPK can be acquired (e.g., arsenic exposure or paraneoplastic syndromes). (yoneda2021japaneseguidelinesfor pages 10-12, gram2023ispunctatepalmoplantar pages 1-2)

---

## 11. Outcome / Prognosis

PPPK is primarily a chronic morbidity condition with variable severity; pain can be significant and impair ambulation in some patients (zamiri2019painfulpunctatepalmoplantar pages 5-6). No survival/mortality impact was identified in the retrieved sources.

### Malignancy association (expert analysis; 2023 systematic review)
A 2023 Orphanet Journal of Rare Diseases systematic review states: “**we could not confirm an association between PPPK1 and malignancy**” and highlights “**a lack of well-designed studies**” to conclude cancer risk; it questions whether surveillance should be offered on the basis of existing literature. (gram2023ispunctatepalmoplantar pages 1-2)

---

## 12. Treatment

### 12.1 Standard management (real-world implementation)
Evidence and guidelines emphasize symptomatic management:
- **Topical keratolytics/emollients**: urea and salicylic acid preparations are repeatedly listed. (yoneda2021japaneseguidelinesfor pages 8-9, knowles2023punctatepalmoplantarkeratoderma pages 4-5)
- **Mechanical debridement/paring/dermabrasion**: cone cutters/razors/punches/scissors, and patient self-care. (yoneda2021japaneseguidelinesfor pages 8-9, yoneda2021japaneseguidelinesfor pages 9-10)
- **Systemic retinoids**: guideline synthesis reports acitretin use with reported benefit in case-based evidence (see below). (yoneda2021japaneseguidelinesfor pages 10-12)
- Practical measures: **comfortable footwear** and reducing trauma/friction. (thomas2020diagnosisandmanagement pages 5-6)

### 12.2 Retinoids (evidence and statistics)
The Japanese guidelines summarize case-based evidence and state that oral retinoids are useful for PPK; they report **acitretin** was used in **12 cases**, with **10/12 showing therapeutic effect**, and **isotretinoin** in 6 cases with variable outcomes and discontinuation for side effects in some cases. (yoneda2021japaneseguidelinesfor pages 10-12)

### 12.3 Emerging/experimental therapies (2022–2024 developments)
Two completed interventional trials evaluate **KM-001 topical 1% cream**, described as “**a potent and selective TRPV3 antagonist**,” in PPPK1 or pachyonychia congenita:
- **NCT05435638** (ClinicalTrials.gov record dated 2022; Phase 1; **COMPLETED**; enrollment 14): topical KM-001 1% twice daily for 12 or 16 weeks. (NCT05435638 chunk 1)
- **NCT05956314** (ClinicalTrials.gov record dated 2023; Phase 1b; **COMPLETED**; enrollment 18; primary completion Nov 2024; last update Jan 15, 2025): topical KM-001 1% twice daily for 12 or 16 weeks, with pain and clinician/patient global outcomes. (NCT05956314 chunk 1, NCT05956314 chunk 2)

No efficacy results were available in the retrieved trial record excerpts (status only).

### 12.4 Suggested MAXO terms (labels)
- Topical keratolytic therapy (salicylic acid; urea)
- Mechanical debridement/paring
- Systemic retinoid therapy (acitretin; isotretinoin)
- Genetic counseling
- Genetic testing
- Topical TRPV3 antagonist therapy (KM-001; investigational)

---

## 13. Prevention

No disease-specific primary prevention is established for hereditary PPPK. Secondary/tertiary prevention focuses on symptom control and prevention of fissures/pain via keratolytics, debridement, and minimizing mechanical stress. (yoneda2021japaneseguidelinesfor pages 8-9, thomas2020diagnosisandmanagement pages 5-6)

Genetic counseling and cascade testing can be considered for at-risk relatives in hereditary families. (yoneda2021japaneseguidelinesfor pages 10-12)

---

## 14. Other Species / Natural Disease

No naturally occurring animal disease analogs were identified in the retrieved sources.

---

## 15. Model Organisms

No whole-animal model systems were identified in the retrieved sources. However, mechanistic evidence includes **in vitro keratinocyte knockdown** experiments (e.g., HaCaT keratinocytes) showing increased proliferation and altered EGFR protein/phosphorylation, supporting cell-based modeling of AAGAB haploinsufficiency. (pohler2012haploinsufficiencyforaagab pages 1-2, pohler2012haploinsufficiencyforaagab pages 4-5)

---

## Subtype summary table

| Subtype | Synonyms / nomenclature | OMIM ID | Typical clinical features / onset | Known genes | Inheritance | Key citations (year / URL) |
|---|---|---:|---|---|---|---|
| PPKP1 / PPPK1 | Punctate palmoplantar keratoderma type 1; Buschke-Fischer-Brauer disease; punctate PPK type 1A and 1B in Japanese guidelines | 148600 | Progressive discrete hyperkeratotic lesions/papules on palms and soles; often begin in the 1st-2nd decades or after adolescence; lesions increase with age and may coalesce on pressure-bearing plantar skin; type 1A: numerous tiny punctate keratotic papules from childhood-adolescence that can fuse into larger plaques (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5) | **Type 1A:** AAGAB (major established cause); **Type 1B:** COL14A1 (reported in Chinese family/families; much rarer) (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5, gram2023ispunctatepalmoplantar pages 1-2) | Autosomal dominant (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5) | Pohler et al. 2012, https://doi.org/10.1038/ng.2444; Matsuzawa et al. 2013, https://doi.org/10.1038/jid.2013.243; Yoneda et al. 2021, https://doi.org/10.1111/1346-8138.15850; Gram et al. 2023, https://doi.org/10.1186/s13023-023-02862-8 (pohler2012haploinsufficiencyforaagab pages 1-2, matsuzawa2013heterozygousmutationsin pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5, gram2023ispunctatepalmoplantar pages 1-2) |
| PPKP1A | Punctate PPK type 1A; Buschke-Fischer-Brauer type | 148600 | Numerous tiny punctate keratotic papules on palmoplantar skin from childhood to adolescence; lesions gradually increase and may fuse into larger hyperkeratotic lesions (yoneda2021japaneseguidelinesfor pages 4-5) | AAGAB (yoneda2021japaneseguidelinesfor pages 4-5, pohler2012haploinsufficiencyforaagab pages 1-2) | Autosomal dominant (yoneda2021japaneseguidelinesfor pages 4-5) | Yoneda et al. 2021, https://doi.org/10.1111/1346-8138.15850; Pohler et al. 2012, https://doi.org/10.1038/ng.2444 (yoneda2021japaneseguidelinesfor pages 4-5, pohler2012haploinsufficiencyforaagab pages 1-2) |
| PPKP1B | Punctate PPK type 1B | Not specified in provided sources | Included by Japanese guidelines as a punctate PPK subtype; detailed phenotype not expanded in retrieved excerpts beyond punctate palmoplantar hyperkeratosis classification (yoneda2021japaneseguidelinesfor pages 4-5) | COL14A1 (yoneda2021japaneseguidelinesfor pages 4-5, gram2023ispunctatepalmoplantar pages 1-2) | Autosomal dominant (yoneda2021japaneseguidelinesfor pages 4-5) | Yoneda et al. 2021, https://doi.org/10.1111/1346-8138.15850; Gram et al. 2023, https://doi.org/10.1186/s13023-023-02862-8 (yoneda2021japaneseguidelinesfor pages 4-5, gram2023ispunctatepalmoplantar pages 1-2) |
| PPKP2 | Porokeratotic type; porokeratosis punctata palmaris et plantaris; punctate PPK type 2 | 175860 | Tiny punctate keratotic lesions appearing around puberty; histopathology characterized by a coronoid lamella-like column of parakeratotic cells (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5) | Unknown in provided sources (yoneda2021japaneseguidelinesfor pages 4-5) | Autosomal dominant (yoneda2021japaneseguidelinesfor pages 4-5) | Pohler et al. 2012, https://doi.org/10.1038/ng.2444; Yoneda et al. 2021, https://doi.org/10.1111/1346-8138.15850; Gram et al. 2023, https://doi.org/10.1186/s13023-023-02862-8 (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5, gram2023ispunctatepalmoplantar pages 1-2) |
| PPKP3 | Acrokeratoelastoidosis; punctate PPK type 3 | 101850 | Small keratotic papules appearing after adolescence on the marginal edges of palmar and plantar surfaces (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5) | Unknown in provided sources (yoneda2021japaneseguidelinesfor pages 4-5) | Autosomal dominant (yoneda2021japaneseguidelinesfor pages 4-5) | Pohler et al. 2012, https://doi.org/10.1038/ng.2444; Yoneda et al. 2021, https://doi.org/10.1111/1346-8138.15850; Gram et al. 2023, https://doi.org/10.1186/s13023-023-02862-8 (pohler2012haploinsufficiencyforaagab pages 1-2, yoneda2021japaneseguidelinesfor pages 4-5, gram2023ispunctatepalmoplantar pages 1-2) |


*Table: This table summarizes the punctate palmoplantar keratoderma subtype framework used in the retrieved sources, including OMIM identifiers, clinical patterns, inheritance, and the distinction between type 1A (AAGAB) and type 1B (COL14A1). It is useful for quickly aligning historical subtype names with current gene-based understanding.*

---

## Visual evidence (figures)
- Pedigrees/clinical images/histology and an AAGAB mutation schematic (including the panel describing mutation locations relative to functional domains) were retrieved from a multi-family PPPK1 mutation report. (pohler2014newandrecurrent media e8a4666c, pohler2014newandrecurrent media f62067ed, pohler2014newandrecurrent media 7e640702)

---

## Notes on gaps and limitations
1) This run’s retrieved excerpts did not explicitly contain Orphanet/ICD/MeSH/MONDO identifiers; these should be added by querying OMIM/Orphanet/MONDO directly if required for KB completeness.
2) Some gene claims (e.g., COL14A1 as type 1B) are supported here through guideline and review-level evidence but not by direct full-text extraction of the original COL14A1 pedigree paper in this run.
3) ClinicalTrials.gov entries show completed studies of KM-001, but trial results were not present in the retrieved record chunks.


References

1. (matsuzawa2013heterozygousmutationsin pages 1-2): Takamitsu Matsuzawa, T. Kawamura, Y. Ogawa, Masaaki Takahashi, R. Aoki, Kohji Moriishi, Yoshio Koyanagi, Hiroyuki Gatanaga, A. Blauvelt, and Shinji Shimada. Heterozygous mutations in aagab cause type 1 punctate palmoplantar keratoderma with evidence for increased growth factor signaling. Journal of Investigative Dermatology, 133:2805-2808, Dec 2013. URL: https://doi.org/10.1038/jid.2013.243, doi:10.1038/jid.2013.243. This article has 23 citations and is from a highest quality peer-reviewed journal.

2. (pohler2012haploinsufficiencyforaagab pages 1-2): Elizabeth Pohler, Ons Mamai, Jennifer Hirst, Mozheh Zamiri, Helen Horn, Toshifumi Nomura, Alan D Irvine, Benvon Moran, Neil J Wilson, Frances J D Smith, Christabelle S M Goh, Aileen Sandilands, Christian Cole, Geoffrey J Barton, Alan T Evans, Hiroshi Shimizu, Masashi Akiyama, Mitsuhiro Suehiro, Izumi Konohana, Mohammad Shboul, Sebastien Teissier, Lobna Boussofara, Mohamed Denguezli, Ali Saad, Moez Gribaa, Patricia J Dopping-Hepenstal, John A McGrath, Sara J Brown, David R Goudie, Bruno Reversade, Colin S Munro, and W H Irwin McLean. Haploinsufficiency for aagab causes clinically heterogeneous forms of punctate palmoplantar keratoderma. Nature Genetics, 44:1272-1276, Oct 2012. URL: https://doi.org/10.1038/ng.2444, doi:10.1038/ng.2444. This article has 114 citations and is from a highest quality peer-reviewed journal.

3. (yoneda2021japaneseguidelinesfor pages 4-5): Kozo Yoneda, Akiharu Kubo, Toshifumi Nomura, Akemi Ishida‐Yamamoto, Yasushi Suga, Masashi Akiyama, Nobuo Kanazawa, and Takashi Hashimoto. Japanese guidelines for the management of palmoplantar keratoderma. The Journal of Dermatology, Jun 2021. URL: https://doi.org/10.1111/1346-8138.15850, doi:10.1111/1346-8138.15850. This article has 10 citations.

4. (gram2023ispunctatepalmoplantar pages 1-2): S. B. Gram, J. Bjerrelund, A. M. Jelsig, A. Bygum, C. Leboeuf-Yde, and L. B. Ousager. Is punctate palmoplantar keratoderma type 1 associated with malignancy? a systematic review of the literature. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02862-8, doi:10.1186/s13023-023-02862-8. This article has 4 citations and is from a peer-reviewed journal.

5. (pohler2014newandrecurrent pages 1-2): Elizabeth Pohler, M. Huber, S. E. Boonen, M. Zamiri, M. Zamiri, P. A. Gregersen, Mette Sommerlund, Mette Ramsing, Daniel Hohl, W. McLean, and F. Smith. New and recurrent aagab mutations in punctate palmoplantar keratoderma. The British Journal of Dermatology, 171:433-436, Aug 2014. URL: https://doi.org/10.1111/bjd.12927, doi:10.1111/bjd.12927. This article has 10 citations.

6. (thomas2020diagnosisandmanagement pages 5-6): BR Thomas and EA O'TOOLE. Diagnosis and management of inherited palmoplantar keratodermas. Acta Dermato-Venereologica, 100:adv00094-176, Mar 2020. URL: https://doi.org/10.2340/00015555-3430, doi:10.2340/00015555-3430. This article has 50 citations and is from a domain leading peer-reviewed journal.

7. (pohler2014newandrecurrent pages 2-3): Elizabeth Pohler, M. Huber, S. E. Boonen, M. Zamiri, M. Zamiri, P. A. Gregersen, Mette Sommerlund, Mette Ramsing, Daniel Hohl, W. McLean, and F. Smith. New and recurrent aagab mutations in punctate palmoplantar keratoderma. The British Journal of Dermatology, 171:433-436, Aug 2014. URL: https://doi.org/10.1111/bjd.12927, doi:10.1111/bjd.12927. This article has 10 citations.

8. (knowles2023punctatepalmoplantarkeratoderma pages 4-5): A Knowles, M Adams, DA Glass II, MJ Adams, and D Glass. Punctate palmoplantar keratoderma: a case report. Cureus, Jan 2023. URL: https://doi.org/10.7759/cureus.33769, doi:10.7759/cureus.33769. This article has 3 citations.

9. (elhaji2020aagabmutationsin pages 1-2): Youssef Elhaji, Cherise Hedlin, Anu Nath, Emma L. Price, Christopher Gallant, Stacey Northgrave, and Peter R. Hull. Aagab mutations in 18 canadian families with punctate palmoplantar keratoderma and a possible link to cancer. Journal of Cutaneous Medicine and Surgery, 24:28-32, Jan 2020. URL: https://doi.org/10.1177/1203475419878161, doi:10.1177/1203475419878161. This article has 15 citations and is from a peer-reviewed journal.

10. (zamiri2019painfulpunctatepalmoplantar pages 5-6): M. Zamiri, Neil J. Wilson, A. Mackenzie, G. Sobey, C. Leitch, and F.J.D. Smith. Painful punctate palmoplantar keratoderma due to heterozygous mutations in aagab. British Journal of Dermatology, 180:1250-1251, Feb 2019. URL: https://doi.org/10.1111/bjd.17442, doi:10.1111/bjd.17442. This article has 7 citations and is from a highest quality peer-reviewed journal.

11. (gram2025clinicalandgenetic pages 3-4): Stine Bjørn Gram, Klaus Brusgaard, Ulrikke Lei, Mette Sommerlund, Gabrielle Randskov Vinding, Sondre Olai Kjellevold Sleire, Alex Hørby Christensen, Sanne Pedersen Fast, Rasmus Bach, Anette Bygum, and Lilian Bomme Ousager. Clinical and genetic findings in patients with palmoplantar keratoderma. JAMA Dermatology, 161:157, Feb 2025. URL: https://doi.org/10.1001/jamadermatol.2024.4824, doi:10.1001/jamadermatol.2024.4824. This article has 6 citations and is from a domain leading peer-reviewed journal.

12. (gram2024identificationofa pages 1-2): Stine Bjørn Gram, Anne Sofie Fredberg Jørgensen, Anette Bygum, Klaus Brusgaard, and Lilian Bomme Ousager. Identification of a founder variant aagab c.370c>t, p.arg124ter in patients with punctate palmoplantar keratoderma in southern denmark. Clinical Genetics, 105:561-566, Feb 2024. URL: https://doi.org/10.1111/cge.14486, doi:10.1111/cge.14486. This article has 1 citations and is from a peer-reviewed journal.

13. (giehl2012nonsensemutationsin pages 1-2): Kathrin A. Giehl, Gertrud N. Eckstein, Sandra M. Pasternack, Silke Praetzel-Wunder, Thomas Ruzicka, Peter Lichtner, Kerstin Seidl, Mike Rogers, Elisabeth Graf, Lutz Langbein, Markus Braun-Falco, Regina C. Betz, and Tim M. Strom. Nonsense mutations in aagab cause punctate palmoplantar keratoderma type buschke-fischer-brauer. American journal of human genetics, 91 4:754-9, Oct 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.024, doi:10.1016/j.ajhg.2012.08.024. This article has 98 citations and is from a highest quality peer-reviewed journal.

14. (pohler2012haploinsufficiencyforaagab pages 4-5): Elizabeth Pohler, Ons Mamai, Jennifer Hirst, Mozheh Zamiri, Helen Horn, Toshifumi Nomura, Alan D Irvine, Benvon Moran, Neil J Wilson, Frances J D Smith, Christabelle S M Goh, Aileen Sandilands, Christian Cole, Geoffrey J Barton, Alan T Evans, Hiroshi Shimizu, Masashi Akiyama, Mitsuhiro Suehiro, Izumi Konohana, Mohammad Shboul, Sebastien Teissier, Lobna Boussofara, Mohamed Denguezli, Ali Saad, Moez Gribaa, Patricia J Dopping-Hepenstal, John A McGrath, Sara J Brown, David R Goudie, Bruno Reversade, Colin S Munro, and W H Irwin McLean. Haploinsufficiency for aagab causes clinically heterogeneous forms of punctate palmoplantar keratoderma. Nature Genetics, 44:1272-1276, Oct 2012. URL: https://doi.org/10.1038/ng.2444, doi:10.1038/ng.2444. This article has 114 citations and is from a highest quality peer-reviewed journal.

15. (matsuzawa2013heterozygousmutationsin pages 4-4): Takamitsu Matsuzawa, T. Kawamura, Y. Ogawa, Masaaki Takahashi, R. Aoki, Kohji Moriishi, Yoshio Koyanagi, Hiroyuki Gatanaga, A. Blauvelt, and Shinji Shimada. Heterozygous mutations in aagab cause type 1 punctate palmoplantar keratoderma with evidence for increased growth factor signaling. Journal of Investigative Dermatology, 133:2805-2808, Dec 2013. URL: https://doi.org/10.1038/jid.2013.243, doi:10.1038/jid.2013.243. This article has 23 citations and is from a highest quality peer-reviewed journal.

16. (yoneda2021japaneseguidelinesfor pages 9-10): Kozo Yoneda, Akiharu Kubo, Toshifumi Nomura, Akemi Ishida‐Yamamoto, Yasushi Suga, Masashi Akiyama, Nobuo Kanazawa, and Takashi Hashimoto. Japanese guidelines for the management of palmoplantar keratoderma. The Journal of Dermatology, Jun 2021. URL: https://doi.org/10.1111/1346-8138.15850, doi:10.1111/1346-8138.15850. This article has 10 citations.

17. (yoneda2021japaneseguidelinesfor pages 10-12): Kozo Yoneda, Akiharu Kubo, Toshifumi Nomura, Akemi Ishida‐Yamamoto, Yasushi Suga, Masashi Akiyama, Nobuo Kanazawa, and Takashi Hashimoto. Japanese guidelines for the management of palmoplantar keratoderma. The Journal of Dermatology, Jun 2021. URL: https://doi.org/10.1111/1346-8138.15850, doi:10.1111/1346-8138.15850. This article has 10 citations.

18. (yoneda2021japaneseguidelinesfor pages 8-9): Kozo Yoneda, Akiharu Kubo, Toshifumi Nomura, Akemi Ishida‐Yamamoto, Yasushi Suga, Masashi Akiyama, Nobuo Kanazawa, and Takashi Hashimoto. Japanese guidelines for the management of palmoplantar keratoderma. The Journal of Dermatology, Jun 2021. URL: https://doi.org/10.1111/1346-8138.15850, doi:10.1111/1346-8138.15850. This article has 10 citations.

19. (NCT05435638 chunk 1):  Study Designed to Evaluate Safety and Efficacy of 1% Topical Formulation of KM-001 on Type 1 Punctate Palmoplantar Keratoderma or Pachyonychia Congenita Diseases. Kamari Pharma Ltd. 2022. ClinicalTrials.gov Identifier: NCT05435638

20. (NCT05956314 chunk 1):  Assessment of KM-001 - Safety, Tolerability, and Efficacy in Patients With PPPK1 or PC. Kamari Pharma Ltd. 2023. ClinicalTrials.gov Identifier: NCT05956314

21. (NCT05956314 chunk 2):  Assessment of KM-001 - Safety, Tolerability, and Efficacy in Patients With PPPK1 or PC. Kamari Pharma Ltd. 2023. ClinicalTrials.gov Identifier: NCT05956314

22. (pohler2014newandrecurrent media e8a4666c): Elizabeth Pohler, M. Huber, S. E. Boonen, M. Zamiri, M. Zamiri, P. A. Gregersen, Mette Sommerlund, Mette Ramsing, Daniel Hohl, W. McLean, and F. Smith. New and recurrent aagab mutations in punctate palmoplantar keratoderma. The British Journal of Dermatology, 171:433-436, Aug 2014. URL: https://doi.org/10.1111/bjd.12927, doi:10.1111/bjd.12927. This article has 10 citations.

23. (pohler2014newandrecurrent media f62067ed): Elizabeth Pohler, M. Huber, S. E. Boonen, M. Zamiri, M. Zamiri, P. A. Gregersen, Mette Sommerlund, Mette Ramsing, Daniel Hohl, W. McLean, and F. Smith. New and recurrent aagab mutations in punctate palmoplantar keratoderma. The British Journal of Dermatology, 171:433-436, Aug 2014. URL: https://doi.org/10.1111/bjd.12927, doi:10.1111/bjd.12927. This article has 10 citations.

24. (pohler2014newandrecurrent media 7e640702): Elizabeth Pohler, M. Huber, S. E. Boonen, M. Zamiri, M. Zamiri, P. A. Gregersen, Mette Sommerlund, Mette Ramsing, Daniel Hohl, W. McLean, and F. Smith. New and recurrent aagab mutations in punctate palmoplantar keratoderma. The British Journal of Dermatology, 171:433-436, Aug 2014. URL: https://doi.org/10.1111/bjd.12927, doi:10.1111/bjd.12927. This article has 10 citations.