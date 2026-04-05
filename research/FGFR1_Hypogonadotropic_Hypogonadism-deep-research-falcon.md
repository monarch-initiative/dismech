---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:58.480985'
end_time: '2026-04-04T12:38:05.111257'
duration_seconds: 786.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: FGFR1-Related Hypogonadotropic Hypogonadism
  mondo_id: ''
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
- **Disease Name:** FGFR1-Related Hypogonadotropic Hypogonadism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FGFR1-Related Hypogonadotropic Hypogonadism** covering all of the
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
- **Disease Name:** FGFR1-Related Hypogonadotropic Hypogonadism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FGFR1-Related Hypogonadotropic Hypogonadism** covering all of the
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


# FGFR1-Related Hypogonadotropic Hypogonadism (FGFR1-related CHH/KS): Comprehensive Disease Characteristics Report

**Scope note.** “FGFR1-related hypogonadotropic hypogonadism” is commonly used clinically to denote **hypogonadotropic hypogonadism 2 with or without anosmia**, i.e., congenital/idiopathic GnRH deficiency due to pathogenic **FGFR1** variants spanning **Kallmann syndrome (KS; with hypo/anosmia)** and **normosmic CHH/IHH**. The evidence base below comes from aggregated cohort studies and curated diagnostic resources plus individual case reports; where cohort-level statistics are provided, they are explicitly identified. 

---

## 1. Disease Information

### 1.1 Concise overview
FGFR1-related CHH/KS is a Mendelian developmental disorder of the reproductive neuroendocrine axis caused by impaired FGFR1-mediated signaling during development, leading to deficient GnRH neuron development and/or function. Clinically it presents as **absent or incomplete puberty**, low sex steroids with **low/inappropriately normal LH/FSH**, and infertility; in the KS subtype, it is accompanied by **anosmia/hyposmia** and often **olfactory bulb/tract hypoplasia/aplasia**. Non-reproductive anomalies (e.g., dental agenesis, cleft lip/palate, synkinesia, hearing loss, renal and skeletal anomalies) occur due to broad roles of FGFR1 in embryonic patterning. (chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2, chung2023theinitiationand pages 2-3)

### 1.2 Key identifiers (ontology and genetic)
A harmonized identifier/synonym table is provided here:

| Entity name | Related disease labels / synonyms | MONDO ID | OMIM / MIM IDs mentioned in retrieved sources | Notes on scope and source |
|---|---|---|---|---|
| FGFR1-related hypogonadotropic hypogonadism | FGFR1-related CHH; FGFR1-related IHH; FGFR1-related Kallmann syndrome spectrum | MONDO_0007844 | FGFR1 gene: OMIM 136350; IHH: MIM 147950 | FGFR1 is the canonical causal gene for “hypogonadotropic hypogonadism 2 with or without anosmia,” spanning anosmic and normosmic presentations; gene-disease pairing supported by Open Targets/MONDO and primary literature (xu2023howhumangenetic pages 1-2, dode2003lossoffunctionmutationsin pages 1-2) |
| Hypogonadotropic hypogonadism 2 with or without anosmia | KS2; FGFR1-related HH; FGFR1-related CHH with or without anosmia | MONDO_0007844 | FGFR1 gene: OMIM 136350 | Most disease-specific MONDO label linked to FGFR1 in Open Targets evidence; corresponds to autosomal dominant FGFR1-associated disease first established by Dodé et al. (dode2003lossoffunctionmutationsin pages 1-2) |
| Congenital hypogonadotropic hypogonadism | CHH; congenital GnRH deficiency; isolated GnRH deficiency | MONDO_0015770 | IHH/CHH commonly discussed under MIM 147950 in retrieved sources | Higher-level disease category including FGFR1-related cases; used in recent diagnostic/genetic reviews and panel-testing discussions (vezzoli2023geneticarchitectureof pages 3-5, sayed2023paneltestingfor pages 2-3) |
| Hypogonadotropic hypogonadism | HH; hypogonadotropic hypogonadism spectrum | MONDO_0018555 | Not disease-specific in retrieved FGFR1 papers | Broad umbrella term from Open Targets/MONDO; useful for database harmonization but less specific than CHH/KS labels (sayed2023paneltestingfor pages 2-3) |
| Kallmann syndrome | KS; IHH with anosmia; anosmic CHH | No MONDO ID retrieved in provided Open Targets context | OMIM series listed in Men et al.: 308700, 147950, 244200, 610628, 612370, 612702 | Clinical subtype defined by hypogonadotropic hypogonadism plus anosmia/hyposmia; Men et al. note ~60% of IHH cases are associated with anosmia and provide a KS OMIM list reflecting locus heterogeneity rather than a single FGFR1-specific identifier (men2020genotypicandphenotypic pages 1-2, chu2023mutationspectrumof pages 1-2) |
| Idiopathic hypogonadotropic hypogonadism | IHH; isolated hypogonadotropic hypogonadism; normosmic IHH when smell is normal | No MONDO ID retrieved in provided Open Targets context for the exact term | IHH: MIM 147950; Men et al. also cite 612370 in the IHH/KS context | Literature term widely used in FGFR1 studies, especially older and cohort papers; includes both normosmic and anosmic forms depending on olfactory status (men2020genotypicandphenotypic pages 1-2, xu2023howhumangenetic pages 1-2, goncalves2015novelfgfr1mutations pages 1-2) |
| Normosmic idiopathic hypogonadotropic hypogonadism | nIHH; normosmic CHH | Not retrieved in provided Open Targets context | Usually discussed under IHH MIM 147950 in retrieved sources | Important phenotypic label because FGFR1 variants can cause both KS and normosmic IHH; emphasizes variable expressivity within the same gene (dode2003lossoffunctionmutationsin pages 1-2, goncalves2015novelfgfr1mutations pages 1-2) |


*Table: This table organizes the key disease labels, MONDO identifiers, OMIM/MIM references, and common synonyms relevant to FGFR1-related hypogonadotropic hypogonadism and the Kallmann syndrome spectrum. It is useful for harmonizing database entries with the terminology used in both recent literature and disease ontologies.*

**MONDO IDs available from Open Targets evidence** include: 
- **Hypogonadotropic hypogonadism**: **MONDO_0018555** (sayed2023paneltestingfor pages 2-3)
- **Congenital hypogonadotropic hypogonadism**: **MONDO_0015770** (sayed2023paneltestingfor pages 2-3)
- **Hypogonadotropic hypogonadism 2 with or without anosmia** (FGFR1-related): **MONDO_0007844** (sayed2023paneltestingfor pages 2-3)

**OMIM/MIM IDs available in retrieved primary literature** include: 
- **FGFR1** gene: **OMIM 136350** (men2020genotypicandphenotypic pages 1-2, dode2003lossoffunctionmutationsin pages 1-2)
- **Idiopathic hypogonadotropic hypogonadism (IHH)**: **MIM 147950** (xu2023howhumangenetic pages 1-2)
- Men et al. list multiple OMIM entries for KS locus heterogeneity (e.g., 308700, 147950, 244200, 610628, 612370, 612702) (men2020genotypicandphenotypic pages 1-2).

**Gaps.** ICD-10/ICD-11, MeSH, and Orphanet identifiers were not present in the full-texts retrieved via the current tool runs; therefore they are not asserted here.

### 1.3 Synonyms and alternative names
Common labels include: 
- **Kallmann syndrome (KS)** (IHH/CHH with hypo/anosmia) (chu2023mutationspectrumof pages 1-2)
- **Congenital hypogonadotropic hypogonadism (CHH)** (with or without anosmia) (dwyer2024classesandpredictors pages 3-4)
- **Idiopathic hypogonadotropic hypogonadism (IHH)**, including **normosmic IHH** (xu2023howhumangenetic pages 1-2, goncalves2015novelfgfr1mutations pages 1-2)

### 1.4 Evidence provenance (individual vs aggregated)
- **Aggregated disease-level resources:** UK NHSE/PanelApp curated gene panels and gene-disease assertions informing clinical testing pipelines (sayed2023paneltestingfor pages 2-3). 
- **Human cohort studies:** e.g., Chinese IHH cohort genotype/phenotype analyses (men2020genotypicandphenotypic pages 1-2). 
- **Case reports:** e.g., females with primary amenorrhea and KS due to de novo FGFR1 variants (xia2021twofemalespresenting pages 1-2). 

---

## 2. Etiology

### 2.1 Primary causal factors
**Genetic cause (primary).** Pathogenic variants in **FGFR1** cause autosomal dominant CHH/KS (historically “KAL2”), first established by Dodé et al. in 2003 as **“Loss-of-function mutations in FGFR1 cause autosomal dominant Kallmann syndrome.”** (Nature Genetics; Mar 2003; https://doi.org/10.1038/ng1122) (dode2003lossoffunctionmutationsin pages 1-2).

**Mechanistic cause (developmental).** FGFR1 participates in **FGF signaling** required for development of GnRH neurons and olfactory structures; reduced dosage/signaling disrupts these developmental processes, producing GnRH deficiency with or without anosmia. (chung2023theinitiationand pages 2-3, dode2003lossoffunctionmutationsin pages 1-2)

### 2.2 Risk factors
- **Genetic:** heterozygous FGFR1 pathogenic variants (missense/nonsense/splice/indels) and, in some families, **CNVs** involving chromosome 8p/FGFR1 locus; Chu et al. reported a pathogenic **del(8)(p12p11.22)** CNV in a KS family and a frameshift FGFR1 variant (RB&E; Mar 2023; https://doi.org/10.1186/s12958-023-01074-w) (chu2023mutationspectrumof pages 1-2). 
- **Oligogenicity as risk/complexity:** FGFR1 variants can be part of **di-/oligogenic** inheritance and may interact with variants in other CHH genes; oligogenicity complicates penetrance and expressivity (goncalves2015novelfgfr1mutations pages 3-4, sayed2023paneltestingfor pages 2-3).

**Environmental risk factors.** No specific toxin/lifestyle triggers were identified in the retrieved FGFR1-focused texts. CHH in general can show variable penetrance and may be influenced by non-genetic factors, but FGFR1-specific gene–environment interactions were not evidenced in the provided sources. (pitteloud2010complexgeneticsin pages 9-10, vezzoli2023geneticarchitectureof pages 3-5)

### 2.3 Protective factors
FGFR1-specific protective factors (genetic or environmental) were not identified in the retrieved sources.

### 2.4 Gene–environment interactions
No FGFR1-specific G×E evidence was retrieved.

---

## 3. Phenotypes

A phenotype-to-HPO mapping table (with onset/course and frequency notes where available) is provided below:

| Phenotype (plain language) | Suggested HPO term(s) and IDs | Typical onset/course | Frequency notes (if in evidence) | Supporting citation IDs from provided context |
|---|---|---|---|---|
| Absent or incomplete puberty / hypogonadotropic hypogonadism | Hypogonadotropic hypogonadism (HP:0000044); Delayed puberty (HP:0000823); Absent puberty (HP:0008194) | Congenital disorder usually recognized in adolescence because of absent/incomplete pubertal development; chronic lifelong course in most patients, though reversal can occur | KS accounts for ~50% of IHH; CHH reversal reported in ~10–15% of cases; reversible CHH broader literature 5–20% | (chu2023mutationspectrumof pages 1-2, dwyer2024classesandpredictors pages 3-4, vezzoli2023geneticarchitectureof pages 3-5) |
| Anosmia or hyposmia | Anosmia (HP:0000458); Hyposmia (HP:0004409) | Congenital/early-onset olfactory deficit; usually stable | About half of IHH/CHH cases are KS with hypo/anosmia; Men 2020 notes ~60% of IHH associated with anosmia | (men2020genotypicandphenotypic pages 1-2, chu2023mutationspectrumof pages 1-2) |
| Olfactory bulb/tract aplasia or hypoplasia on MRI | Aplasia/Hypoplasia of the olfactory bulb (suggested HPO: Olfactory bulb aplasia/hypoplasia, if available in implementation set); Abnormality of the olfactory lobe (HP:0009914) | Congenital structural anomaly, typically stable on imaging | MRI evidence used in diagnosis; Xia 2021 described dysplastic or absent olfactory bulbs and tracts in affected females | (dode2003lossoffunctionmutationsin pages 1-2) |
| Delayed puberty in relatives / variable expressivity | Delayed puberty (HP:0000823) | Adolescence; may be milder than proband phenotype | Seen in FGFR1 families with intrafamilial variability and incomplete penetrance | (xu2023howhumangenetic pages 1-2, goncalves2015novelfgfr1mutations pages 3-4, dode2003lossoffunctionmutationsin pages 1-2) |
| Micropenis and/or cryptorchidism in severe male cases | Micropenis (HP:0000054); Cryptorchidism (HP:0000028) | Congenital/infancy markers of severe GnRH deficiency; may precede pubertal failure | Not quantified in retrieved FGFR1-specific excerpts here, but included in severe CHH phenotype descriptions and reversal stratification work | (dwyer2024classesandpredictors pages 3-4, dwyer2024classesandpredictors pages 9-11) |
| Dental agenesis | Tooth agenesis (HP:0009804) | Congenital developmental anomaly; permanent | Extra-reproductive anomaly repeatedly reported in FGFR1 cohorts; 44.4% of mutation-positive patients in Men 2020 had extra-reproductive anomalies including dental agenesis | (men2020genotypicandphenotypic pages 1-2, chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2) |
| Cleft lip and/or cleft palate | Cleft upper lip (HP:0000204); Cleft palate (HP:0000175) | Congenital; fixed structural anomaly | Included among recurrent non-reproductive FGFR1-associated anomalies | (chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2) |
| Bimanual synkinesis / mirror movements | Mirror movements (HP:0001039); Synkinesia (HP:0001334) | Congenital/childhood, usually persistent | Classic associated anomaly in FGFR1/KS spectrum | (chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2) |
| Corpus callosum agenesis | Agenesis of corpus callosum (HP:0001274) | Congenital brain malformation; static structural feature | Reported among associated anomalies in FGFR1 mutation carriers | (dode2003lossoffunctionmutationsin pages 1-2) |
| Hearing loss / hearing impairment | Hearing impairment (HP:0000365); Sensorineural hearing impairment (HP:0000407) | Congenital or early-onset; variable severity | Men 2020: hearing loss occurred in 5% of IHH individuals; one cited cohort found 16% (7/43) of KS patients with FGFR1/FGF8 mutations had hearing loss | (men2020genotypicandphenotypic pages 5-8, men2020genotypicandphenotypic pages 1-2, dode2003lossoffunctionmutationsin pages 1-2) |
| Renal agenesis or renal hypoplasia | Renal agenesis (HP:0000122); Renal hypoplasia (HP:0000089) | Congenital structural anomaly | Listed as associated non-reproductive feature in KS/FGFR1 spectrum; no percentage in retrieved excerpts | (chu2023mutationspectrumof pages 1-2) |
| Skeletal/limb anomalies (syndactyly, oligodactyly, clinodactyly, hand malformations) | Syndactyly (HP:0001159); Oligodactyly (HP:0001180); Clinodactyly of the 5th finger (HP:0004209); Split hand (HP:0001177) / Split foot (HP:0001839) where relevant | Congenital developmental anomalies | Men 2020 reported hand malformations among extra-reproductive anomalies; Chu 2023 lists skeletal anomalies broadly | (men2020genotypicandphenotypic pages 5-8, men2020genotypicandphenotypic pages 1-2, chu2023mutationspectrumof pages 1-2) |
| Gonadal dysplasia / primary amenorrhea in females | Primary amenorrhea (HP:0000043); Hypogonadism (HP:0000135) | Usually adolescence; chronic unless treated | Xia 2021 described females presenting primary amenorrhea without puberty due to FGFR1 variants | (dode2003lossoffunctionmutationsin pages 1-2) |
| Potential spontaneous reversal of reproductive axis dysfunction | No exact HPO disease-course term; suggest annotation as clinical course note rather than phenotype | Usually early adulthood after years of treatment; may relapse, so requires monitoring | Dwyer 2024: spontaneous reversal in ~10–15% of CHH cases; broader review range 5–20% | (dwyer2024classesandpredictors pages 3-4, vezzoli2023geneticarchitectureof pages 3-5) |


*Table: This table maps key clinical features of FGFR1-related hypogonadotropic hypogonadism/Kallmann syndrome to suggested HPO terms, with onset/course and frequency notes where available. It is designed to support knowledge-base phenotype annotation grounded in the cited evidence.*

### 3.1 Key phenotype themes (narrative)
- **Core reproductive phenotype:** absent/incomplete puberty with low sex steroids and low/inappropriately normal LH/FSH (CHH/IHH). (dwyer2024classesandpredictors pages 3-4)
- **Olfactory phenotype:** anosmia/hyposmia; MRI may show absent/hypoplastic olfactory bulbs and tracts. Xia et al. report: “Magnetic resonance imaging showed dysplastic or absent olfactory bulbs and tracts.” (J Obstet Gynaecol Res; Aug 2021; https://doi.org/10.1111/jog.14966) (xia2021twofemalespresenting pages 1-2).
- **Extra-reproductive anomalies:** cleft lip/palate, dental agenesis, synkinesia, corpus callosum agenesis, hearing loss, renal and skeletal anomalies. These were described in early FGFR1 discovery work and reiterated in later cohort literature. (dode2003lossoffunctionmutationsin pages 1-2, men2020genotypicandphenotypic pages 5-8, chu2023mutationspectrumof pages 1-2)

### 3.2 Quantitative phenotype data (recently extracted)
- In a Chinese IHH cohort study, **44.4%** of mutation-positive individuals (FGFR1/FGF8/FGF17) had extra-reproductive anomalies (including dental agenesis, hearing loss, and hand malformations) (Fertility & Sterility; Jan 2020; https://doi.org/10.1016/j.fertnstert.2019.08.069) (men2020genotypicandphenotypic pages 1-2). 
- Hearing loss frequency reported in the same context: “Hearing loss occurred in **5%** of IHH individuals,” and a cited cohort found **16% (7/43)** of KS patients with FGFR1/FGF8 mutations had hearing loss (men2020genotypicandphenotypic pages 5-8).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **FGFR1** (fibroblast growth factor receptor 1; OMIM 136350) is the canonical causal gene for hypogonadotropic hypogonadism 2 with or without anosmia (dode2003lossoffunctionmutationsin pages 1-2).

### 4.2 Pathogenic variant spectrum and classification
**Variant classes (germline).** Across studies, pathogenic FGFR1 variants include missense, nonsense, splice-site, and small indels, and larger CNVs affecting the locus. Dodé et al. enumerated multiple heterozygous variants across receptor domains in the seminal report (dode2003lossoffunctionmutationsin pages 1-2). Chu et al. (2023) state that “>300 FGFR1 mutations (missense, nonsense, splice, rare deletions) are reported in HGMD” and report both an FGFR1 frameshift and an 8p deletion CNV (chu2023mutationspectrumof pages 1-2).

**Functional consequences.** 
- Many disease-causing variants reduce receptor function (loss-of-function/haploinsufficiency), consistent with autosomal dominant disease (dode2003lossoffunctionmutationsin pages 1-2). 
- Some truncating variants can remove transmembrane/intracellular domains; Men et al. describe truncating receptors “without the transmembrane and intracellular domains” and report an FGFR1 variant (p.W289X) with a “dominant negative effect by interfering with the function of wild-type receptor” (men2020genotypicandphenotypic pages 5-8).

**Incomplete penetrance and variable expressivity.** 
- Gonçalves et al. report FGFR1 mutations “inherited from an apparently normal parent,” described as “cases of incomplete penetrance,” and identify a trigenic mutation in one case supporting oligogenicity (Fertility & Sterility; Nov 2015; https://doi.org/10.1016/j.fertnstert.2015.07.1142) (goncalves2015novelfgfr1mutations pages 3-4). 
- Dodé et al. likewise reported unaffected carriers and variable expressivity among relatives (dode2003lossoffunctionmutationsin pages 1-2).

### 4.3 2023 methodological advance: FGFR1 variant interpretation using human genetic context
Xu et al. (Human Genetics; Oct 2023; https://doi.org/10.1007/s00439-023-02601-w) analyze **143 FGFR1 rare sequence variants** in **175 IHH probands** (95 missense; 48 protein-truncating) and show that FGFR1 missense variants are regionally enriched in functional domains. Incorporating this enrichment into ACMG/AMP evidence **reclassified 37% (20/54)** of FGFR1 missense VUS to pathogenic/likely pathogenic, and phenotypic enrichment among non-proband carriers supported the reclassification (xu2023howhumangenetic pages 1-2). 

### 4.4 Modifier genes / oligogenicity
Oligogenic inheritance is documented in FGFR1-related IHH/KS families (e.g., co-occurring variants in other CHH genes), complicating classical Mendelian counseling (goncalves2015novelfgfr1mutations pages 3-4, goncalves2015novelfgfr1mutations pages 1-2). Recent clinical genetics reviews emphasize that di-/oligogenic inheritance and incomplete penetrance are key interpretive challenges in CHH (sayed2023paneltestingfor pages 2-3).

### 4.5 Epigenetics / chromosomal abnormalities
No FGFR1-specific epigenetic mechanism evidence was retrieved. Large structural variants affecting the FGFR1 region are relevant (e.g., 8p deletion CNV reported as pathogenic) (chu2023mutationspectrumof pages 1-2).

---

## 5. Environmental Information

No FGFR1-specific environmental contributors (toxins, lifestyle, infections) were identified in the retrieved sources. The disease is best supported as a neurodevelopmental genetic disorder with variable expressivity and penetrance (dode2003lossoffunctionmutationsin pages 1-2, sayed2023paneltestingfor pages 2-3).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (from gene to clinical phenotype)
1. **Upstream trigger:** germline FGFR1 loss-of-function (or signaling impairment) (dode2003lossoffunctionmutationsin pages 1-2).
2. **Developmental effect:** reduced FGF8→FGFR1 signaling compromises **GnRH neuron neurogenesis/progenitor survival/differentiation** in the olfactory placode neurogenic niche (chung2023theinitiationand pages 2-3, chung2023theinitiationand pages 6-6).
3. **Anatomical effect:** impairment in olfactory placode/olfactory bulb development (explaining anosmia/hyposmia in KS) and disruption of the GnRH neuron migratory route to the hypothalamus (chung2023theinitiationand pages 2-3, dode2003lossoffunctionmutationsin pages 1-2).
4. **Physiologic effect:** reduced hypothalamic GnRH drive → low/inappropriately normal LH/FSH → low sex steroids (hypogonadotropic hypogonadism) (dwyer2024classesandpredictors pages 3-4).
5. **Clinical outcome:** absent/incomplete puberty, infertility; in KS, anosmia/hyposmia and olfactory bulb/tract hypoplasia/aplasia; plus extra-reproductive congenital anomalies due to broader FGFR1 developmental roles (chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2).

### 6.2 Pathway-level summary with ontology suggestions
A structured mechanism table with suggested GO/CL/UBERON annotations is provided:

| Level | Mechanism statement | Key genes/proteins | Pathway annotations | Suggested GO Biological Process terms | Suggested CL cell types | Suggested UBERON anatomical structures | Evidence type | Supporting citation IDs |
|---|---|---|---|---|---|---|---|---|
| Molecular | FGFR1 loss-of-function is a primary upstream mechanism in FGFR1-related CHH/KS; pathogenic variants include missense, nonsense, splice-site, indels, and CNVs, reducing receptor dosage or signaling capacity. Some variants may also impair receptor dimerization or act dominant-negatively. | FGFR1 | FGF receptor signaling pathway; receptor tyrosine kinase signaling; MAPK/ERK signaling | GO:0008543 fibroblast growth factor receptor signaling pathway; GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway; GO:0000165 MAPK cascade | CL:0000540 neuron | UBERON:0000955 brain; UBERON:0001898 olfactory bulb | Human genetics | (chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2, men2020genotypicandphenotypic pages 1-2) |
| Molecular | FGF8 is a key ligand for FGFR1 during GnRH neuron ontogeny; reduced FGF8-FGFR1 signaling decreases emergence of GnRH neurons and contributes to GnRH deficiency. | FGF8, FGFR1 | FGF signaling; ligand-receptor activation; MAPK/ERK | GO:0008543 fibroblast growth factor receptor signaling pathway; GO:0022008 neurogenesis; GO:0045664 regulation of neuron differentiation | CL:0000540 neuron; CL:0000039 germ line hormone-releasing hormone neuron | UBERON:0002430 olfactory placode; UBERON:0001137 hypothalamus | Human genetics, mouse model | (chung2023theinitiationand pages 2-3, chung2023theinitiationand pages 6-6, miraoui2013mutationsinfgf17 pages 3-3) |
| Molecular | ANOS1/anosmin-1 modulates FGFR1 signaling through interaction with the FGF-FGFR-heparan sulfate complex; HSPGs facilitate FGF-FGFR complex dimerization, linking extracellular matrix biology to receptor activation. | ANOS1, FGFR1, HSPGs, FGF ligands | FGF signaling; heparan sulfate proteoglycan-dependent signaling; extracellular matrix modulation | GO:0008543 fibroblast growth factor receptor signaling pathway; GO:0006027 glycosaminoglycan catabolic process (broader HSPG context); GO:0030200 heparan sulfate proteoglycan metabolic process | CL:0000540 neuron | UBERON:0000955 brain; UBERON:0002430 olfactory placode | Human genetics, mechanistic model | (men2020genotypicandphenotypic pages 5-8, dode2003lossoffunctionmutationsin pages 1-2) |
| Molecular | FGFR1 protein architecture is mechanistically relevant: ligand-binding determinants localize to D2/D3 and the linker, while alternative splicing generates FGFR1b and FGFR1c isoforms with distinct ligand specificities; pathogenic variants in these domains alter ligand recognition and downstream signaling. | FGFR1, FGF8 | FGF receptor binding specificity; receptor isoform-dependent signaling | GO:0005007 fibroblast growth factor-activated receptor activity; GO:0007169 transmembrane receptor protein tyrosine kinase signaling pathway | CL:0000540 neuron | UBERON:0002430 olfactory placode | Human genetics, in silico structural interpretation | (men2020genotypicandphenotypic pages 1-2, goncalves2015novelfgfr1mutations pages 1-2) |
| Cellular | Fgfr1/Fgf8 deficiency acts upstream of GnRH neuron birth: homozygous Fgf8 hypomorph mice show complete loss of GnRH neurons by E11.5, while Fgfr1 hypomorphic newborns show about 90% reduction, indicating a requirement for progenitor survival and neuronal differentiation. | FGF8, FGFR1 | Developmental FGF signaling; neuronal differentiation; survival signaling | GO:0022008 neurogenesis; GO:0030154 cell differentiation; GO:0043523 regulation of neuron apoptotic process | CL:0000039 germ line hormone-releasing hormone neuron; CL:0000540 neuron | UBERON:0002430 olfactory placode; UBERON:0001137 hypothalamus | Mouse model | (chung2023theinitiationand pages 2-3, chung2023theinitiationand pages 6-6, chung2023theinitiationand media 627f77bc) |
| Cellular | GnRH neurons originate outside the CNS in the medial ventral olfactory placode and then migrate along olfactory/vomeronasal/terminal nerve fibers through the cribriform plate toward the preoptic area and hypothalamus; disrupted FGFR1 signaling compromises this developmental trajectory. | FGFR1, FGF8 | Neuronal migration; axon guidance; developmental patterning | GO:0001764 neuron migration; GO:0007411 axon guidance; GO:0021795 cerebral cortex cell migration (broader neurodevelopment context) | CL:0000039 germ line hormone-releasing hormone neuron; CL:0000540 neuron | UBERON:0002430 olfactory placode; UBERON:0008933 cribriform plate; UBERON:0001137 hypothalamus; UBERON:0001871 preoptic area | Mouse model, developmental neurobiology | (chung2023theinitiationand pages 2-3, chung2023theinitiationand pages 6-6, chung2023theinitiationand media 627f77bc) |
| Cellular | FGFR1 also interfaces with axonal morphogenesis pathways: in C. elegans, kal1 mis/overexpression produces an axon-branching phenotype abolished by defects in heparan-sulfate sulfation, supporting a conserved requirement for anosmin/HSPG-dependent morphogenesis. | KAL1/ANOS1 ortholog, HSPGs, FGFR-related signaling context | Axon branching; extracellular matrix-guided morphogenesis | GO:0007416 synapse assembly (broader neuronal wiring context); GO:0031175 neuron projection development; GO:0007411 axon guidance | CL:0000540 neuron | UBERON-equivalent not applicable across species; human-relevant mapping: UBERON:0000955 brain | C. elegans model | (dode2003lossoffunctionmutationsin pages 1-2) |
| Anatomical | Olfactory bulb development is dosage-sensitive to FGFR1 signaling in humans; reduced FGFR1 dosage contributes to olfactory bulb aplasia/hypoplasia, a structural correlate of anosmia/hyposmia in KS. | FGFR1 | FGF signaling in forebrain/olfactory development | GO:0048856 anatomical structure development; GO:0022008 neurogenesis; GO:0001755 neural crest cell migration (broader craniofacial context) | CL:0000540 neuron; CL:0000679 olfactory receptor neuron | UBERON:0001898 olfactory bulb; UBERON:0002430 olfactory placode; UBERON:0000948 forebrain | Human genetics | (dode2003lossoffunctionmutationsin pages 1-2, xia2021twofemalespresenting pages 2-5) |
| Anatomical | FGF pathway expression in the embryonic olfactory placode links early nasal/olfactory development to later hypothalamic reproductive function; Miraoui et al. identify FGF-family expression in the olfactory placode and mouse knockout phenotypes affecting craniofacial/olfactory structures. | FGF17, FGF8, FGFR1 | FGF signaling in embryonic patterning | GO:0009790 embryo development; GO:0048856 anatomical structure development; GO:0060325 face morphogenesis | CL:0000540 neuron | UBERON:0002430 olfactory placode; UBERON:0001898 olfactory bulb; UBERON:0000167 nose | Human genetics, mouse model | (miraoui2013mutationsinfgf17 pages 3-3) |
| Clinical | The downstream clinical syndrome reflects failed GnRH neuronal development and/or migration: absent or incomplete puberty, hypogonadotropic hypogonadism, infertility, and anosmia/hyposmia; MRI may show dysplastic or absent olfactory bulbs and tracts. | FGFR1, FGF8 | Hypothalamic-pituitary-gonadal axis dysfunction secondary to developmental neuroendocrine defect | GO:0003006 developmental process involved in reproduction; GO:0007399 nervous system development | CL:0000039 germ line hormone-releasing hormone neuron; CL:0000151 pituitary gonadotroph | UBERON:0001137 hypothalamus; UBERON:0000007 pituitary gland; UBERON:0001898 olfactory bulb | Human clinical genetics | (chu2023mutationspectrumof pages 1-2, xia2021twofemalespresenting pages 2-5, xia2021twofemalespresenting pages 1-2) |
| Clinical | Extra-gonadal anomalies arise because FGFR1 signaling contributes broadly to embryonic patterning beyond the reproductive axis; reported features include dental agenesis, cleft lip/palate, hearing loss, renal anomalies, and digital/limb malformations. | FGFR1, FGF8 | Developmental patterning; craniofacial and limb morphogenesis | GO:0060325 face morphogenesis; GO:0035108 limb morphogenesis; GO:0001501 skeletal system development | CL:0000066 epithelial cell; CL:0000540 neuron | UBERON:0000164 mouth; UBERON:0002371 kidney; UBERON:0002101 limb | Human genetics | (men2020genotypicandphenotypic pages 5-8, men2020genotypicandphenotypic pages 1-2, chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2) |


*Table: This table summarizes the multilevel pathophysiology of FGFR1-related congenital hypogonadotropic hypogonadism/Kallmann syndrome, linking molecular defects in FGF signaling to GnRH neuron development, olfactory anatomy, and clinical features. It also proposes ontology annotations useful for knowledge-base curation.*

### 6.3 Model-organism evidence (key quantitative results)
Chung & Tsai (Frontiers in Endocrinology; Apr 2023; https://doi.org/10.3389/fendo.2023.1166132) summarize strong mouse evidence for FGF signaling upstream of GnRH neuron birth:
- **Homozygous Fgf8 hypomorphic mice:** complete loss of GnRH neurons by E11.5 
- **Fgfr1 hypomorphic newborn mice:** ~**90% reduction** in GnRH neurons
- **Heterozygous Fgf8 hypomorphs:** ~**50% loss** (chung2023theinitiationand pages 2-3)

A schematic depiction of the GnRH developmental trajectory and the role of Fgf8/Fgfr1 is available in the retrieved figure (chung2023theinitiationand media 627f77bc).

---

## 7. Anatomical Structures Affected

**Primary systems:** neuroendocrine (hypothalamic–pituitary–gonadal axis) and olfactory system. (chung2023theinitiationand pages 2-3, dwyer2024classesandpredictors pages 3-4)

**Key anatomical structures (UBERON suggestions):** 
- **Olfactory placode** (origin of GnRH neurons in development) (chung2023theinitiationand pages 2-3)
- **Cribriform plate** (migration corridor) (chung2023theinitiationand pages 2-3)
- **Preoptic area** and **hypothalamus** (final GnRH neuron destinations) (chung2023theinitiationand pages 2-3)
- **Median eminence** (GnRH neurosecretory target site) (chung2023theinitiationand pages 2-3)
- **Olfactory bulbs/tracts** (structural substrate for anosmia; often hypoplastic/aplastic on MRI) (xia2021twofemalespresenting pages 1-2)

**Secondary structures (developmental anomalies):** craniofacial structures (clefting), teeth (dental agenesis), kidneys (renal anomalies), limbs/digits (skeletal malformations), auditory apparatus (hearing loss). (chu2023mutationspectrumof pages 1-2, dode2003lossoffunctionmutationsin pages 1-2, men2020genotypicandphenotypic pages 5-8)

---

## 8. Temporal Development

### 8.1 Typical onset
Although the developmental defect is congenital, CHH/KS is often **diagnosed in adolescence** when puberty fails to start or progress. (dwyer2024classesandpredictors pages 3-4)

### 8.2 Progression and course
- Most cases require long-term management, but a clinically important subset exhibits **reversal** (return of endogenous reproductive function). Reversal frequency estimates in recent sources range from **~10–15%** in CHH (Dwyer 2024) to **5–20%** across broader literature summaries (Vezzoli 2023) (dwyer2024classesandpredictors pages 3-4, vezzoli2023geneticarchitectureof pages 3-5).

### 8.3 Critical periods
The key biological “critical period” is embryonic GnRH neuron neurogenesis and early migration from the olfactory placode niche, as highlighted by the Fgf8/Fgfr1 hypomorph mouse data. (chung2023theinitiationand pages 2-3)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal dominant** inheritance is established for FGFR1-related KS/CHH with **incomplete penetrance** and **variable expressivity**; oligogenic inheritance can occur. (dode2003lossoffunctionmutationsin pages 1-2, goncalves2015novelfgfr1mutations pages 3-4, sayed2023paneltestingfor pages 2-3)

### 9.2 Epidemiology
- Chu et al. (2023) report estimated KS prevalence of **~1/30,000 men** and **~1/125,000 women**, and state KS accounts for ~**50%** of IHH (chu2023mutationspectrumof pages 1-2).
- CHH is reported to be about **4× more common in males** in the 2024 reversal study background. (dwyer2024classesandpredictors pages 3-4)

### 9.3 Variant prevalence in CHH/IHH cohorts
Men et al. (2020) report the combined prevalence of **FGFR1/FGF8/FGF17 mutations** of **12.4%** in a Chinese IHH cohort (men2020genotypicandphenotypic pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical criteria and hormonal testing
Dwyer et al. (Lancet Diabetes & Endocrinology; Apr 2024; https://doi.org/10.1016/S2213-8587(24)00028-7) define CHH in males as absent/incomplete puberty with **low testosterone (<6 nmol/L)** and **low/inappropriately normal gonadotropins**; partial puberty includes mean testicular volume ≥4 cc (dwyer2024classesandpredictors pages 3-4).

### 10.2 Imaging
- MRI evaluation of the **olfactory bulbs/tracts** is a key diagnostic discriminator for KS. Xia et al. emphasize MRI findings and state MRI of olfactory bulbs/tracts contributes to diagnosis (xia2021twofemalespresenting pages 5-5).

### 10.3 Genetic testing strategy (2023–2024 “real-world” implementation)
- **Panel-based testing:** Sayed & Howard (European Journal of Human Genetics; Dec 2023; https://doi.org/10.1038/s41431-022-01261-0) describe UK NHSE Genomic Medicine Service implementation of a curated CHH panel via PanelApp and note cohort studies showing an underlying variant is found in **21–51%** of CHH/KS cases (sayed2023paneltestingfor pages 2-3). 
- **WES/WGS:** Xia et al. recommend WES as a priority in females with primary amenorrhea without secondary sex characteristics and note that WES can also indicate karyotype/chromosomal abnormalities and CNVs (xia2021twofemalespresenting pages 1-2, xia2021twofemalespresenting pages 5-5).
- **CNV analysis:** Chu et al. employed CNV-seq and classified an 8p deletion spanning FGFR1 as pathogenic (chu2023mutationspectrumof pages 1-2).

### 10.4 Differential diagnosis
In females presenting primary amenorrhea, Xia et al. highlight the need for **karyotype** to exclude Turner syndrome and other chromosomal etiologies (both reported patients were 46,XX) and recommend focused olfactory history plus olfactory MRI (xia2021twofemalespresenting pages 1-2).

---

## 11. Outcome / Prognosis

### 11.1 Fertility prognosis
In male CHH, spermatogenesis and fertility are achievable in approximately **~75%** of men treated with **exogenous gonadotropins (FSH + hCG)** or **pulsatile GnRH**, according to Dwyer 2024 background synthesis (dwyer2024classesandpredictors pages 3-4).

### 11.2 Reversal prognosis
- Spontaneous reversal occurs in **~10–15%** (Dwyer 2024) (dwyer2024classesandpredictors pages 3-4). 
- Dwyer 2024 further reports genetic/clinical associations: non-reversal patients were more likely to show oligogenicity than reversal patients (58.9% vs 29.3%) and baseline testicular volume positively predicted reversal (dwyer2024classesandpredictors pages 9-11).

### 11.3 Morbidity and quality of life impacts
While dedicated QoL instruments were not captured in the retrieved texts, Xia et al. reported osteoporosis/high fracture risk in females at diagnosis (DXA evidence), implying clinically significant morbidity from delayed diagnosis and untreated hypogonadism (xia2021twofemalespresenting pages 1-2).

---

## 12. Treatment

A structured treatment/applications table with outcomes, risks, MAXO suggestions, and clinical trial mappings is provided:

| Treatment goal | Intervention | Typical candidates / sex | Key outcomes / statistics from evidence | Key risks / considerations | Example trials / implementations | Suggested MAXO terms |
|---|---|---|---|---|---|---|
| Puberty induction / virilization | Testosterone replacement (IM or transdermal) | Primarily adolescent or adult males with CHH/KS, including FGFR1-related disease | Standard therapy to induce secondary sexual characteristics; does **not** induce fertility by itself. In male CHH more broadly, treatment improves sexual, bone, metabolic, and psychological health; testicular growth on testosterone may occasionally signal HPG-axis activation. Reversal of CHH has been observed after sex-steroid treatment in a subset of patients; overall spontaneous/therapy-associated reversal is ~10–15% (broader literature 5–20%) (dwyer2024classesandpredictors pages 3-4, vezzoli2023geneticarchitectureof pages 3-5, dwyer2024classesandpredictors pages 9-11) | Requires long-term monitoring of pubertal progression, hematocrit, bone health, and possible later fertility planning; may mask spontaneous reversal unless washout is attempted. Genetic counseling is important because FGFR1-related disease can be transmitted to offspring (dwyer2024classesandpredictors pages 3-4, sayed2023paneltestingfor pages 2-3) | Real-world standard endocrine care; Dwyer 2024 notes reversal has occurred after testosterone treatment in some men, supporting structured adult washout/monitoring in selected patients (dwyer2024classesandpredictors pages 3-4, dwyer2024classesandpredictors pages 9-11) | MAXO: hormone replacement therapy; testosterone replacement |
| Puberty induction / uterine and bone health | Estradiol replacement, later cyclic estrogen-progestin therapy | Primarily adolescent or adult females with CHH/KS, including FGFR1-related disease | Used to induce breast/uterine development and protect bone health. In two FGFR1-positive KS females, one patient was treated with estradiol valerate after diagnosis established by WES and olfactory MRI (xia2021twofemalespresenting pages 2-2) | Requires gradual dose escalation, endometrial protection with progestin when appropriate, and bone-density follow-up; does not restore fertility by itself. In FGFR1-related disease, recurrence risk for offspring should be discussed (xia2021twofemalespresenting pages 2-5, xia2021twofemalespresenting pages 2-2) | Case-level implementation in FGFR1-related female KS: Xia et al. used estradiol valerate in one patient after confirming de novo FGFR1 variant and olfactory bulb agenesis (xia2021twofemalespresenting pages 2-5, xia2021twofemalespresenting pages 2-2) | MAXO: estrogen replacement therapy; progestin therapy |
| Fertility induction / spermatogenesis | hCG followed by hCG + hMG or uFSH (combined gonadotropin therapy) | Males desiring fertility; often used in CHH/KS including FGFR1-related cases | In male CHH broadly, spermatogenesis and fertility are achievable in ~75% of men treated with exogenous gonadotropins or pulsatile GnRH. Men 2020 reported hCG/hMG markedly increased testicular size in mutation-positive patients. In FGFR1/FGF8/FGF17 mutation carriers, fertility is possible but mutation transmission risk remains (men2020genotypicandphenotypic pages 5-8, dwyer2024classesandpredictors pages 3-4) | Months-to-years treatment; monitor testosterone, testicular volume, sperm counts, adverse effects. Genetic counseling is important for autosomal dominant FGFR1 variants; female partners may need reproductive counseling. Limited response may occur in severe cases (men2020genotypicandphenotypic pages 5-8, dwyer2024classesandpredictors pages 3-4) | NCT02310074 compared pulsatile GnRH pump vs hCG alone 6 months then hCG+uFSH 12 months in 76 men; primary outcome partner pregnancy by 18 months; secondary outcomes included time to first sperm and sperm-density thresholds (NCT02310074 chunk 1) | MAXO: chorionic gonadotropin therapy; follicle-stimulating hormone therapy; fertility treatment |
| Fertility induction / spermatogenesis | Pulsatile GnRH / gonadorelin pump | Males with hypothalamic CHH/KS; also some females for ovulation induction | In male CHH broadly, pulsatile GnRH is an established fertility-induction strategy and contributes to the ~75% spermatogenesis/fertility success estimate when combined with gonadotropin-based evidence. In Xia 2021, one female FGFR1-positive KS patient received pulsatile gonadorelin pump therapy (dwyer2024classesandpredictors pages 3-4, xia2021twofemalespresenting pages 2-2) | Pump burden, adherence, cost, need for specialized centers; monitor LH/FSH/testosterone or ovulation response. Appropriate in hypothalamic forms; not a substitute for genetic counseling regarding transmission (dwyer2024classesandpredictors pages 3-4, xia2021twofemalespresenting pages 2-5) | NCT02310074: open-label phase 4 male IHH study of 18-month portable subcutaneous pulsatile GnRH pump vs gonadotropins, with pregnancy and spermatogenesis endpoints (NCT02310074 chunk 1) | MAXO: gonadotropin-releasing hormone therapy; pulsatile hormone administration |
| Ovulation induction / pregnancy | Subcutaneous pulsatile GnRH (gonadorelin acetate) via OmniPod / LutrePulse | Women with hypogonadotropic hypogonadism seeking pregnancy | NCT01976728 was a phase 3 multicenter double-blind randomized placebo-controlled study (39 women) testing 10, 15, or 20 µg/pulse. Primary endpoint: ovulation rate, defined by progesterone ≥6 ng/mL, positive β-hCG, or gestational sac on ultrasound. Secondary endpoints included clinical/biochemical pregnancy, LH surge, follicular development, estradiol/LH/FSH changes, and OHSS frequency (NCT01976728 chunk 1) | Requires normal reproductive tract evaluation, partner semen assessment, and monitoring for ovarian response/OHSS. Practical burdens include pump use and close reproductive-endocrine follow-up (NCT01976728 chunk 2, NCT01976728 chunk 1) | NCT01976728 (LutrePulse): phase 3, randomized, placebo-controlled ovulation-induction trial in women with HH; results posted 2021-03-03 (NCT01976728 chunk 1) | MAXO: ovulation induction; gonadotropin-releasing hormone therapy; assisted reproduction |
| Rescue fertility strategy after poor gonadotropin response | Switch to or trial of pulsatile GnRH after inadequate hCG/hMG response | Selected males with CHH/KS who have poor spermatogenic response to combined gonadotropins | 2024 literature highlights pulsatile GnRH as an alternative strategy for spermatogenesis in poor responders; rationale is restoration of physiologic pituitary stimulation rather than direct gonadotropin replacement. This is especially relevant in specialized male fertility programs (NCT02310074 chunk 1) | Requires specialized expertise and pump access; evidence is evolving and not FGFR1-specific. Persistent infertility can still occur in severe congenital cases (NCT02310074 chunk 1) | Supported by contemporary CHH treatment studies and by the design of NCT02310074 comparing pump therapy with gonadotropins (NCT02310074 chunk 1) | MAXO: gonadotropin-releasing hormone therapy; infertility management |
| Bone / metabolic / general health support | Early diagnosis plus sex-steroid replacement; monitor BMD and metabolic status | Both sexes | CHH management improves sexual, bone, metabolic, and psychological health. Xia 2021 reported osteoporosis/high fracture risk in affected females at diagnosis, underscoring the need for early replacement therapy and bone monitoring (xia2021twofemalespresenting pages 1-2, dwyer2024classesandpredictors pages 3-4) | Delayed diagnosis worsens bone and psychosocial outcomes; ongoing DXA, vitamin D/calcium assessment, and lifestyle counseling may be needed. FGFR1 variants may also have broader metabolic implications, as defective FGFR1 signaling has been linked to lower insulin sensitivity in a 2024 human recall-by-genotype study (xia2021twofemalespresenting pages 1-2, dwyer2024classesandpredictors pages 3-4) | Standard endocrine follow-up rather than disease-specific trial. 2024 FGFR1 human study suggests impaired FGFR1 signaling may contribute to early insulin resistance, supporting attention to metabolic monitoring in variant carriers (dwyer2024classesandpredictors pages 3-4) | MAXO: bone mineral density monitoring; metabolic monitoring; supportive endocrine care |
| Prognostic / management strategy | Structured treatment washout and reassessment for reversal | Mostly adult males after puberty induction or fertility treatment | CHH reversal occurs in ~10–15% of cases; Dwyer 2024 reports most confirmed washouts were after age 18 and that reversal can follow testosterone, gonadotropins, or pulsatile GnRH. Larger baseline testicular volume predicts reversal, whereas cryptorchidism and oligogenicity predict lower reversal likelihood (dwyer2024classesandpredictors pages 3-4, dwyer2024classesandpredictors pages 9-11) | Must distinguish true reversal from temporary improvement; relapse can occur, so long-term monitoring is necessary. Genetic findings generally do not yet change first-line treatment, except for counseling implications (dwyer2024classesandpredictors pages 9-11) | Dwyer 2024 multicenter cross-sectional study provides current evidence base for reversal monitoring and prognosis across referral centers (dwyer2024classesandpredictors pages 3-4, dwyer2024classesandpredictors pages 9-11) | MAXO: treatment monitoring; endocrine function assessment; therapy withdrawal trial |


*Table: This table summarizes current treatment applications for FGFR1-related congenital hypogonadotropic hypogonadism/Kallmann syndrome and CHH more broadly, including puberty induction, fertility induction, bone/metabolic support, and reversal monitoring. It integrates quantitative outcomes, practical considerations, relevant trial examples, and suggested MAXO terms for knowledge-base annotation.*

### 12.1 Puberty induction
- **Males:** testosterone replacement to induce secondary sexual characteristics (dwyer2024classesandpredictors pages 3-4).
- **Females:** estrogen replacement with later cyclic estrogen–progestin therapy; Xia et al. describe estradiol valerate therapy in a female KS patient (xia2021twofemalespresenting pages 2-2).

### 12.2 Fertility induction (real-world implementations)
- **Males:** exogenous gonadotropins (hCG ± FSH/hMG) or pulsatile GnRH; Men et al. report that hCG/hMG increased testicular size in treated males and note reversal in a subset of IHH cases (men2020genotypicandphenotypic pages 5-8).
- **Females:** pulsatile GnRH for ovulation induction. 

### 12.3 Clinical trials (examples)
- **NCT02310074** (Shanghai Jiao Tong University School of Medicine; Phase 4; study start 2010; primary completion Jun 2014): compares **pulsatile GnRH pump** vs **gonadotropin therapy** in **76 men with IHH**; primary endpoint partner pregnancy by 18 months; secondary endpoints include time to first sperm and sperm-density thresholds (ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT02310074) (NCT02310074 chunk 1).
- **NCT01976728** (Ferring; Phase 3; start 2014-04-01; completion 2018-02-23; results posted 2021-03-03): **LutrePulse** (gonadorelin acetate) delivered via OmniPod for **ovulation induction** in women with HH; primary endpoint ovulation rate and secondary pregnancy and follicular outcomes (ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT01976728) (NCT01976728 chunk 1).

### 12.4 Targeted/advanced therapeutics
No FGFR1 gene therapy or FGFR1-targeted molecular therapy trials for FGFR1-related CHH/KS were identified in the retrieved clinical trials set; current treatment is hormonal replacement and fertility induction.

---

## 13. Prevention

**Primary prevention.** Not applicable in the conventional sense for a monogenic developmental disorder. 

**Secondary prevention (early detection).** Earlier recognition of delayed puberty/amenorrhea, structured evaluation of olfaction, and timely endocrine replacement can prevent downstream morbidity (e.g., low bone density) (xia2021twofemalespresenting pages 1-2).

**Genetic counseling (tertiary/recurrence prevention).** Because FGFR1-related CHH/KS is often autosomal dominant with incomplete penetrance and can be oligogenic, recurrence risk counseling is complex; modern panel testing and careful variant interpretation are emphasized as essential to counseling (sayed2023paneltestingfor pages 2-3, dode2003lossoffunctionmutationsin pages 1-2).

Suggested MAXO (prevention-related) terms: genetic counseling; carrier testing; cascade screening (supported conceptually by genetics and counseling emphasis in modern diagnostic reviews) (sayed2023paneltestingfor pages 2-3).

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary disease analogs were retrieved in the provided texts. The strongest cross-species evidence is mechanistic/model-organism rather than naturally occurring disease.

---

## 15. Model Organisms

### 15.1 Mammalian models
Mouse hypomorphic models summarized by Chung & Tsai (2023) provide strong mechanistic evidence for FGF8/FGFR1 roles in GnRH neuron neurogenesis and survival (including ~90% GnRH neuron reduction in Fgfr1 hypomorphic newborns) (chung2023theinitiationand pages 2-3).

### 15.2 Invertebrate models
Dodé et al. cite C. elegans data where kal1 mis/overexpression produces an axon-branching phenotype dependent on heparan-sulfate sulfation, supporting conserved extracellular-matrix modulation relevant to the FGFR1 pathway context (dode2003lossoffunctionmutationsin pages 1-2).

### 15.3 Model limitations
Mouse and C. elegans models capture developmental neurobiology mechanisms but do not fully reproduce the human spectrum of incomplete penetrance, variable expressivity, oligogenic inheritance, and treatment-associated reversal.

---

# High-priority recent developments (2023–2024) — curated summary

1. **Clinical diagnostic implementation:** UK NHSE Genomic Medicine Service CHH panel curated via PanelApp; molecular diagnostic yield across cohorts **21–51%**; key interpretive challenges are oligogenicity and incomplete penetrance (Dec 2023) (sayed2023paneltestingfor pages 2-3).
2. **Variant interpretation advance for FGFR1:** regional enrichment of FGFR1 missense variants across protein domains used to strengthen ACMG/AMP evidence and reclassify **37%** of FGFR1 missense VUS (Oct 2023) (xu2023howhumangenetic pages 1-2).
3. **Clinical course/reversal predictors:** multicenter study standardizing reversal definitions and identifying predictors (cryptorchidism negative; baseline testicular volume positive; oligogenicity associated with non-reversal), while reaffirming fertility success estimates and reversal frequency (Apr 2024) (dwyer2024classesandpredictors pages 3-4, dwyer2024classesandpredictors pages 9-11).

---

# Key abstract quotes (for knowledge-base evidence items)

- Dodé et al. (2003): “Loss-of-function mutations in FGFR1 cause autosomal dominant Kallmann syndrome.” (dode2003lossoffunctionmutationsin pages 1-2)
- Chu et al. (2023): KS prevalence and phenotype spectrum statements; KS described as IHH subtype with anosmia/hyposmia and multiple associated anomalies (chu2023mutationspectrumof pages 1-2).
- Xia et al. (2021): “Magnetic resonance imaging showed dysplastic or absent olfactory bulbs and tracts.” and recommendation that WES “should be a priority” in primary amenorrhea without secondary sex characteristics (xia2021twofemalespresenting pages 1-2).

---

# Data gaps and limitations of this tool-run

- **ICD-10/ICD-11, MeSH, Orphanet IDs** were not present in the retrieved full-text corpus for FGFR1-related CHH/KS and therefore are not provided here.
- **FGFR1-specific penetrance estimates** (numerical) and **variant allele frequencies in gnomAD** were not retrievable with the current evidence set.
- **FGFR1-specific genotype–treatment response statistics** are limited; most treatment outcomes are reported at CHH syndrome level rather than gene-stratified.


References

1. (chu2023mutationspectrumof pages 1-2): Guoming Chu, Pingping Li, Qian Zhao, Rong He, and Yanyan Zhao. Mutation spectrum of kallmann syndrome: identification of five novel mutations across anos1 and fgfr1. Reproductive Biology and Endocrinology : RB&E, Mar 2023. URL: https://doi.org/10.1186/s12958-023-01074-w, doi:10.1186/s12958-023-01074-w. This article has 7 citations.

2. (dode2003lossoffunctionmutationsin pages 1-2): Catherine Dodé, Jacqueline Levilliers, Jean-Michel Dupont, Anne De Paepe, Nathalie Le Dû, Nadia Soussi-Yanicostas, Roney S. Coimbra, Sedigheh Delmaghani, Sylvie Compain-Nouaille, Françoise Baverel, Christophe Pêcheux, Dominique Le Tessier, Corinne Cruaud, Marc Delpech, Frank Speleman, Stefan Vermeulen, Andrea Amalfitano, Yvan Bachelot, Philippe Bouchard, Sylvie Cabrol, Jean-Claude Carel, Henriette Delemarre-van de Waal, Barbara Goulet-Salmon, Marie-Laure Kottler, Odile Richard, Franco Sanchez-Franco, Robert Saura, Jacques Young, Christine Petit, and Jean-Pierre Hardelin. Loss-of-function mutations in fgfr1 cause autosomal dominant kallmann syndrome. Nature Genetics, 33:463-465, Mar 2003. URL: https://doi.org/10.1038/ng1122, doi:10.1038/ng1122. This article has 1039 citations and is from a highest quality peer-reviewed journal.

3. (chung2023theinitiationand pages 2-3): Wilson CJ Chung and Pei-San Tsai. The initiation and maintenance of gonadotropin-releasing hormone neuron identity in congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1166132, doi:10.3389/fendo.2023.1166132. This article has 12 citations.

4. (xu2023howhumangenetic pages 1-2): Wanxue Xu, Lacey Plummer, Stephanie B. Seminara, Ravikumar Balasubramanian, and Margaret F. Lippincott. How human genetic context can inform pathogenicity classification: fgfr1 variation in idiopathic hypogonadotropic hypogonadism. Human Genetics, 142:1611-1619, Oct 2023. URL: https://doi.org/10.1007/s00439-023-02601-w, doi:10.1007/s00439-023-02601-w. This article has 4 citations and is from a peer-reviewed journal.

5. (vezzoli2023geneticarchitectureof pages 3-5): Valeria Vezzoli, Faris Hrvat, Giovanni Goggi, Silvia Federici, Biagio Cangiano, Richard Quinton, Luca Persani, and Marco Bonomi. Genetic architecture of self-limited delayed puberty and congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2022.1069741, doi:10.3389/fendo.2022.1069741. This article has 26 citations.

6. (sayed2023paneltestingfor pages 2-3): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31:387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 32 citations and is from a domain leading peer-reviewed journal.

7. (men2020genotypicandphenotypic pages 1-2): Meichao Men, Jiayu Wu, Yaguang Zhao, Xiaoliang Xing, Fang Jiang, Ruizhi Zheng, and Jia-Da Li. Genotypic and phenotypic spectra of fgfr1, fgf8, and fgf17 mutations in a chinese cohort with idiopathic hypogonadotropic hypogonadism. Fertility and Sterility, 113:158-166, Jan 2020. URL: https://doi.org/10.1016/j.fertnstert.2019.08.069, doi:10.1016/j.fertnstert.2019.08.069. This article has 30 citations and is from a highest quality peer-reviewed journal.

8. (goncalves2015novelfgfr1mutations pages 1-2): Catarina Gonçalves, Margarida Bastos, Duarte Pignatelli, Teresa Borges, José M. Aragüés, Fernando Fonseca, Bernardo D. Pereira, Sílvia Socorro, and Manuel C. Lemos. Novel fgfr1 mutations in kallmann syndrome and normosmic idiopathic hypogonadotropic hypogonadism: evidence for the involvement of an alternatively spliced isoform. Fertility and Sterility, 104:1261-1267.e1, Nov 2015. URL: https://doi.org/10.1016/j.fertnstert.2015.07.1142, doi:10.1016/j.fertnstert.2015.07.1142. This article has 24 citations and is from a highest quality peer-reviewed journal.

9. (dwyer2024classesandpredictors pages 3-4): Andrew A Dwyer, Isabella R McDonald, Biagio Cangiano, Luca Giovanelli, Luigi Maione, Leticia F G Silveira, Taneli Raivio, Ana Claudia Latronico, Jacques Young, Richard Quinton, Marco Bonomi, Luca Persani, Stephanie B Seminara, and Christopher S Lee. Classes and predictors of reversal in male patients with congenital hypogonadotropic hypogonadism: a cross-sectional study of six international referral centres. The Lancet Diabetes &amp; Endocrinology, 12:257-266, Apr 2024. URL: https://doi.org/10.1016/s2213-8587(24)00028-7, doi:10.1016/s2213-8587(24)00028-7. This article has 17 citations and is from a highest quality peer-reviewed journal.

10. (xia2021twofemalespresenting pages 1-2): Junke Xia, Xiao Luo, Xinyuan Zhang, and Xiangdong Kong. Two females presenting primary amenorrhea diagnosed with kallmann syndrome caused by novel fgfr1 variants. Journal of Obstetrics and Gynaecology Research, 47:3727-3731, Aug 2021. URL: https://doi.org/10.1111/jog.14966, doi:10.1111/jog.14966. This article has 1 citations and is from a peer-reviewed journal.

11. (goncalves2015novelfgfr1mutations pages 3-4): Catarina Gonçalves, Margarida Bastos, Duarte Pignatelli, Teresa Borges, José M. Aragüés, Fernando Fonseca, Bernardo D. Pereira, Sílvia Socorro, and Manuel C. Lemos. Novel fgfr1 mutations in kallmann syndrome and normosmic idiopathic hypogonadotropic hypogonadism: evidence for the involvement of an alternatively spliced isoform. Fertility and Sterility, 104:1261-1267.e1, Nov 2015. URL: https://doi.org/10.1016/j.fertnstert.2015.07.1142, doi:10.1016/j.fertnstert.2015.07.1142. This article has 24 citations and is from a highest quality peer-reviewed journal.

12. (pitteloud2010complexgeneticsin pages 9-10): Nelly Pitteloud, Sadia Durrani, Taneli Raivio, and Gerasimos P. Sykiotis. Complex genetics in idiopathic hypogonadotropic hypogonadism. Frontiers of hormone research, 39:142-53, Apr 2010. URL: https://doi.org/10.1159/000312700, doi:10.1159/000312700. This article has 92 citations and is from a peer-reviewed journal.

13. (dwyer2024classesandpredictors pages 9-11): Andrew A Dwyer, Isabella R McDonald, Biagio Cangiano, Luca Giovanelli, Luigi Maione, Leticia F G Silveira, Taneli Raivio, Ana Claudia Latronico, Jacques Young, Richard Quinton, Marco Bonomi, Luca Persani, Stephanie B Seminara, and Christopher S Lee. Classes and predictors of reversal in male patients with congenital hypogonadotropic hypogonadism: a cross-sectional study of six international referral centres. The Lancet Diabetes &amp; Endocrinology, 12:257-266, Apr 2024. URL: https://doi.org/10.1016/s2213-8587(24)00028-7, doi:10.1016/s2213-8587(24)00028-7. This article has 17 citations and is from a highest quality peer-reviewed journal.

14. (men2020genotypicandphenotypic pages 5-8): Meichao Men, Jiayu Wu, Yaguang Zhao, Xiaoliang Xing, Fang Jiang, Ruizhi Zheng, and Jia-Da Li. Genotypic and phenotypic spectra of fgfr1, fgf8, and fgf17 mutations in a chinese cohort with idiopathic hypogonadotropic hypogonadism. Fertility and Sterility, 113:158-166, Jan 2020. URL: https://doi.org/10.1016/j.fertnstert.2019.08.069, doi:10.1016/j.fertnstert.2019.08.069. This article has 30 citations and is from a highest quality peer-reviewed journal.

15. (chung2023theinitiationand pages 6-6): Wilson CJ Chung and Pei-San Tsai. The initiation and maintenance of gonadotropin-releasing hormone neuron identity in congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1166132, doi:10.3389/fendo.2023.1166132. This article has 12 citations.

16. (miraoui2013mutationsinfgf17 pages 3-3): Hichem Miraoui, Andrew A. Dwyer, Gerasimos P. Sykiotis, Lacey Plummer, Wilson Chung, Bihua Feng, Andrew Beenken, Jeff Clarke, Tune H. Pers, Piotr Dworzynski, Kimberley Keefe, Marek Niedziela, Taneli Raivio, William F. Crowley, Stephanie B. Seminara, Richard Quinton, Virginia A. Hughes, Philip Kumanov, Jacques Young, Maria A. Yialamas, Janet E. Hall, Guy Van Vliet, Jean-Pierre Chanoine, John Rubenstein, Moosa Mohammadi, Pei-San Tsai, Yisrael Sidis, Kasper Lage, and Nelly Pitteloud. Mutations in fgf17, il17rd, dusp6, spry4, and flrt3 are identified in individuals with congenital hypogonadotropic hypogonadism. American journal of human genetics, 92 5:725-43, May 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.008, doi:10.1016/j.ajhg.2013.04.008. This article has 340 citations and is from a highest quality peer-reviewed journal.

17. (chung2023theinitiationand media 627f77bc): Wilson CJ Chung and Pei-San Tsai. The initiation and maintenance of gonadotropin-releasing hormone neuron identity in congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1166132, doi:10.3389/fendo.2023.1166132. This article has 12 citations.

18. (xia2021twofemalespresenting pages 2-5): Junke Xia, Xiao Luo, Xinyuan Zhang, and Xiangdong Kong. Two females presenting primary amenorrhea diagnosed with kallmann syndrome caused by novel fgfr1 variants. Journal of Obstetrics and Gynaecology Research, 47:3727-3731, Aug 2021. URL: https://doi.org/10.1111/jog.14966, doi:10.1111/jog.14966. This article has 1 citations and is from a peer-reviewed journal.

19. (xia2021twofemalespresenting pages 5-5): Junke Xia, Xiao Luo, Xinyuan Zhang, and Xiangdong Kong. Two females presenting primary amenorrhea diagnosed with kallmann syndrome caused by novel fgfr1 variants. Journal of Obstetrics and Gynaecology Research, 47:3727-3731, Aug 2021. URL: https://doi.org/10.1111/jog.14966, doi:10.1111/jog.14966. This article has 1 citations and is from a peer-reviewed journal.

20. (xia2021twofemalespresenting pages 2-2): Junke Xia, Xiao Luo, Xinyuan Zhang, and Xiangdong Kong. Two females presenting primary amenorrhea diagnosed with kallmann syndrome caused by novel fgfr1 variants. Journal of Obstetrics and Gynaecology Research, 47:3727-3731, Aug 2021. URL: https://doi.org/10.1111/jog.14966, doi:10.1111/jog.14966. This article has 1 citations and is from a peer-reviewed journal.

21. (NCT02310074 chunk 1): Guang Ning. Efficacy and Safety of Pulsatile Gonadotropin Releasing Hormone Pump Treatment in Patients With Idiopathic Hypogonadotropic Hypogonadism. Shanghai Jiao Tong University School of Medicine. 2010. ClinicalTrials.gov Identifier: NCT02310074

22. (NCT01976728 chunk 1):  LutrePulse Hypogonadotropic Hypogonadism. Ferring Pharmaceuticals. 2014. ClinicalTrials.gov Identifier: NCT01976728

23. (NCT01976728 chunk 2):  LutrePulse Hypogonadotropic Hypogonadism. Ferring Pharmaceuticals. 2014. ClinicalTrials.gov Identifier: NCT01976728