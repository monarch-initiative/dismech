---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:20:42.329689'
end_time: '2026-05-08T12:36:34.954187'
duration_seconds: 952.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: X-linked Nonsyndromic Hearing Loss
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-linked Nonsyndromic Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **X-linked Nonsyndromic Hearing Loss** covering all of the
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
- **Disease Name:** X-linked Nonsyndromic Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **X-linked Nonsyndromic Hearing Loss** covering all of the
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


## Comprehensive Research Report: X-linked Nonsyndromic Hearing Loss (DFNX)

### Target disease
- **Disease name:** X-linked nonsyndromic hearing loss (X-linked NSHL; **DFNX**) (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 1-2)
- **Category:** Genetic disorder (X-linked)
- **MONDO ID:** Not identified in the retrieved sources (reporting limited to evidence obtained here).

---

## 1. Disease Information

### 1.1 Definition and overview
X-linked deafness (DFNX) refers to hereditary hearing loss caused by pathogenic variants on the X chromosome and includes both syndromic and nonsyndromic entities; “DFNX” is typically used for **X-linked nonsyndromic hearing loss** in the hereditary hearing-loss locus nomenclature (bernardinelli2023clinicalandmolecular pages 1-2, jiang2023advancesingene pages 1-2). Clinical expression is often sex-influenced: hemizygous males are most severely affected, while heterozygous females may show variable hearing loss due to X-chromosome inactivation effects (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 4-5).

### 1.2 Key identifiers (gene/locus-level identifiers available in evidence)
A 2024 Orphanet Journal of Rare Diseases cohort analysis explicitly lists major DFNX gene–locus mappings (including MIM numbers) (feng2024genomicandphenotypic pages 1-2):
- **PRPS1**: DFNX1 (**MIM#304500**) (feng2024genomicandphenotypic pages 1-2)
- **POU3F4**: DFNX2 / DFN3 (**MIM#304400**); gene **OMIM *300039** (bernardinelli2023clinicalandmolecular pages 1-2, bernardinelli2023clinicalandmolecular pages 5-7)
- **SMPX**: DFNX4 (**MIM#300066**) (feng2024genomicandphenotypic pages 1-2)
- **AIFM1**: DFNX5 (**MIM#300614**) (feng2024genomicandphenotypic pages 1-2)
- **COL4A6**: DFNX6 (**MIM#303630**) (feng2024genomicandphenotypic pages 1-2)

### 1.3 Synonyms / alternative names
- “X-linked deafness (DFNX)” (broad category including syndromic and nonsyndromic) (bernardinelli2023clinicalandmolecular pages 1-2)
- “X-linked nonsyndromic hearing loss (DFNX)” (feng2024genomicandphenotypic pages 1-2)
- **POU3F4-related X-linked deafness type 3**: **DFN3** (also referenced as DFNX2) (bernardinelli2023clinicalandmolecular pages 5-7, bernardinelli2023clinicalandmolecular pages 20-21)

### 1.4 Evidence source type
The information summarized here is derived from **aggregated disease-level resources** (peer-reviewed reviews) and **cohort-based clinical genetics studies** (large case series) rather than EHR-only summaries (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variation in X-chromosome genes important for auditory development and/or cochlear cellular function (feng2024genomicandphenotypic pages 1-2, bernardinelli2023clinicalandmolecular pages 1-2).

### 2.2 Risk factors
- **Genetic risk factor:** carrying pathogenic variants in DFNX genes (e.g., POU3F4, PRPS1, SMPX, AIFM1, COL4A6) (feng2024genomicandphenotypic pages 1-2).
- **Sex as a modifier:** males typically more severely affected due to hemizygosity; females may exhibit variable expressivity due to skewed X-inactivation (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 4-5).

### 2.3 Protective factors / gene–environment interaction
No DFNX-specific protective factors or gene–environment interaction data were identified in the retrieved evidence.

---

## 3. Phenotypes (HPO-aligned)

### 3.1 Core phenotype domain
- **Hearing impairment / sensorineural hearing loss** (HP:0000365 / HP:0000407) is the defining phenotype across DFNX genes (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 4-5).

### 3.2 Age of onset and severity (recent cohort statistics)
In a 2024 Chinese cohort of 3646 unrelated patients with hearing loss (HL), X-linked diagnoses were **~1.14% of genetically solved cases (22/1922)** and clinical onset among X-linked HL cases was **congenital or childhood** in all cases; severity in evaluated probands with X-linked variants was predominantly **severe–profound (25/29)** (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 4-5).

### 3.3 Gene-associated phenotype highlights

#### POU3F4 (DFNX2/DFN3)
- Often severe to profound hearing loss with **pathognomonic inner-ear malformation: incomplete partition type III (IP-III)** (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 4-5).
- Imaging features reported include absent/defective modiolus and interscalar septa, dilated internal auditory canal (IAC), and deficient bony separation between cochlea and IAC (feng2024genomicandphenotypic pages 4-5, feng2024genomicandphenotypic pages 6-7). The radiologic comparison (normal vs IP-III) is shown in the retrieved figure (bernardinelli2023clinicalandmolecular media 04c7488e).
- Suggested HPO terms: **Abnormality of the inner ear morphology** (HP:0000364), **Cochlear malformation** (HP:0008551), **Perilymphatic gusher** (HP term not universally standardized; clinical descriptor supported by evidence) (bernardinelli2023clinicalandmolecular pages 1-2, jung2023geneticcharacteristicsand pages 1-2).

#### PRPS1 (DFNX1)
- Reported as a phenotypic spectrum ranging from isolated HL to more severe syndromes; within the provided cohort summary, male cases can show **progressive hearing loss** with onset ranging from congenital through teenage years and severity from moderate to profound (feng2024genomicandphenotypic pages 4-5).
- Suggested HPO terms: **Progressive sensorineural hearing impairment** (HP:0000408) (feng2024genomicandphenotypic pages 4-5).

#### SMPX (DFNX4)
- Associated with **progressive nonsyndromic hearing loss**; truncating variants are associated with typical audiological profiles in childhood (before/after age 10), whereas nontruncating changes were noted as linking more often to distal myopathy phenotypes (not nonsyndromic HL) (feng2024genomicandphenotypic pages 1-2).
- Female carriers may have variable, later-onset hearing loss (often 4th–5th decade), from unilateral/normal to mild–moderate symmetric/asymmetric loss (feng2024genomicandphenotypic pages 6-7).
- Suggested HPO terms: **Progressive hearing impairment** (HP:0000408), **Asymmetric sensorineural hearing impairment** (HP:0008619).

#### AIFM1 (DFNX5)
- Can present as **auditory neuropathy** with postsynaptic lesion and progressive auditory dyssynchrony; cochlear nerve hypoplasia may occur (feng2024genomicandphenotypic pages 10-12).
- Suggested HPO terms: **Auditory neuropathy** (HP:0030781), **Cochlear nerve hypoplasia** (HP:0030795).

#### COL4A6 (DFNX6)
- In the 2024 cohort, no phenotypic differences were identified among POU3F4 or COL4A6 carriers, but cochlear malformation (e.g., cochlear hypoplasia) was described for a COL4A6 variant example (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 2-4).

### 3.4 Quality-of-life impact
Direct QoL instrument data (EQ-5D/SF-36/PROMIS) specific to DFNX were not identified in the retrieved evidence; however, severe–profound congenital/childhood hearing loss implies major communication and developmental impacts, motivating early diagnosis and intervention (feng2024genomicandphenotypic pages 4-5).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
A recent large cohort review of X-linked hereditary HL highlights the principal DFNX genes: **PRPS1, POU3F4, SMPX, AIFM1, COL4A6** (feng2024genomicandphenotypic pages 1-2). POU3F4 is emphasized as the most common gene for X-linked nonsyndromic HL in reviews and cohorts (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 1-2).

### 4.2 Variant types and functional consequences (by gene)

#### POU3F4 (DFNX2/DFN3)
POU3F4 variants include **missense, nonsense, frameshift** (single coding exon), as well as **larger deletions/insertions/inversions and upstream regulatory deletions** affecting expression (bernardinelli2023clinicalandmolecular pages 5-7). The 2024 cohort further reports CNVs including whole-gene deletion (~165 kb) and notes clustering of pathogenic changes in the POU-specific domain and homeodomain with frequent truncation outcomes (feng2024genomicandphenotypic pages 2-4, feng2024genomicandphenotypic pages 6-7). Functionally characterized variants can show abnormal subcellular localization and impaired nuclear trafficking/transcriptional activity (bernardinelli2023clinicalandmolecular pages 5-7).

#### PRPS1 (DFNX1) and AIFM1 (DFNX5)
In the 2024 cohort analysis, causative variants in **PRPS1** and **AIFM1** were mainly **missense**, and phenotypic variability was proposed to correlate with residue-level structural/function effects (feng2024genomicandphenotypic pages 1-2).

#### SMPX (DFNX4)
SMPX DFNX4 is described as X-linked dominant NSHL with a reported set of 15 causative variants, mostly **truncating** and **splice-site** variants with a minority nontruncating/missense variants (feng2024genomicandphenotypic pages 6-7). A genotype–phenotype distinction was noted in which truncating variants were associated with DFNX4 hearing-loss profiles, while nontruncating variants were linked to distal myopathy phenotypes (feng2024genomicandphenotypic pages 1-2).

### 4.3 Modifier genes / epigenetics
No specific modifier-gene findings or epigenetic mechanisms were identified in the retrieved DFNX-focused evidence; sex-related variability due to X-inactivation is an important mechanism for phenotypic differences in females (feng2024genomicandphenotypic pages 4-5).

---

## 5. Environmental Information
DFNX is primarily genetic. No DFNX-specific environmental contributors were identified in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology (with ontology suggestions)

### 6.1 POU3F4: developmental malformation mechanism leading to IP-III
POU3F4 encodes a transcription factor with a major role in middle/inner ear development (bernardinelli2023clinicalandmolecular pages 1-2). The characteristic DFNX2/DFN3 clinical chain supported by the evidence is:
1) **POU3F4 pathogenic variant** → 2) altered transcription factor function/expression (including mislocalization for some variants) → 3) disrupted ear development and characteristic **IP-III** cochlear/IAC anatomy → 4) severe congenital/early hearing loss and surgery-specific risks such as CSF/perilymphatic “gusher” due to abnormal cochlea–IAC communication (bernardinelli2023clinicalandmolecular pages 5-7, feng2024genomicandphenotypic pages 4-5, jung2023geneticcharacteristicsand pages 1-2).

**Ontology suggestions**
- **UBERON:** cochlea (UBERON:0001766), internal auditory canal (UBERON:0001675), stria vascularis (UBERON:0001845).
- **CL (cell types):** otic mesenchyme cell (not always present as a distinct CL label in curated ontologies; mechanistic role supported by review and IP-III literature), cochlear supporting cell, spiral ganglion neuron.
- **GO biological process:** inner ear development; regulation of transcription.

### 6.2 SMPX: hair-cell/kinocilium and mechanotransduction phenotype (model organism evidence; 2024)
A 2024 Scientific Reports study provides in vivo functional evidence that **smpx** is required for mechanosensory hair-cell development/function in zebrafish lateral line neuromasts, with Smpx localized to hair-cell cytoplasm and kinocilium and loss-of-function producing abnormal kinocilia and reduced mechanotransduction (e.g., reduced FM dye uptake) (diana2024differentiationandfunctioning pages 1-2, diana2024differentiationandfunctioning pages 2-3). This supports a causal chain:
1) **SMPX loss-of-function** → 2) impaired hair-cell structural integrity (including kinocilium changes) → 3) reduced mechanotransduction → 4) progressive hearing loss in humans (DFNX4) (diana2024differentiationandfunctioning pages 1-2).

**Direct abstract-supported statement (model evidence):** the paper describes SMPX as “highly expressed in the inner ear hair cells (HCs)” and notes that SMPX mutations have been associated with “X-chromosomal progressive non syndromic hearing loss in humans” (diana2024differentiationandfunctioning pages 1-2).

**Ontology suggestions**
- **CL:** sensory hair cell (CL:0000601).
- **GO:** sensory perception of sound; mechanotransduction; cilium organization.
- **UBERON:** organ of Corti (UBERON:0001894).

### 6.3 AIFM1: auditory neuropathy phenotype
The 2024 DFNX cohort synthesis notes that AIFM1-related auditory neuropathy involves postsynaptic lesions and progressive dyssynchrony; cochlear nerve hypoplasia may occur (feng2024genomicandphenotypic pages 10-12). Mechanistically, this points to neural/synaptic dysfunction downstream of cochlear mechanics.

---

## 7. Anatomical Structures Affected

### 7.1 Primary structures
- **Inner ear/cochlea** (UBERON:0001766) across DFNX conditions (feng2024genomicandphenotypic pages 1-2).
- **IAC–cochlea interface and modiolus** in **POU3F4/IP-III** (feng2024genomicandphenotypic pages 4-5, bernardinelli2023clinicalandmolecular media 04c7488e).

### 7.2 Cell types (evidence-supported)
- **Sensory hair cells** (especially for SMPX) (diana2024differentiationandfunctioning pages 1-2).

### 7.3 Subcellular compartments
SMPX localization includes the **kinocilium** and cytoplasm in zebrafish hair cells, supporting involvement of ciliary and cytoskeletal structures (diana2024differentiationandfunctioning pages 2-3).

---

## 8. Temporal Development

### 8.1 Onset
In a large 2024 molecular epidemiology study, X-linked hereditary HL cases were congenital or began in childhood (feng2024genomicandphenotypic pages 1-2). For SMPX, female carrier onset may occur later (4th–5th decade) (feng2024genomicandphenotypic pages 6-7).

### 8.2 Progression
- Progressive course is highlighted for **PRPS1** male cases and **SMPX** DFNX4 (feng2024genomicandphenotypic pages 4-5, feng2024genomicandphenotypic pages 6-7).

---

## 9. Inheritance and Population

### 9.1 Inheritance patterns
- DFNX conditions are X-linked; DFNX phenotypes show sex-related differences due to X-inactivation (feng2024genomicandphenotypic pages 4-5).
- **SMPX (DFNX4)** is described as X-linked **dominant** nonsyndromic hearing loss (feng2024genomicandphenotypic pages 6-7).

### 9.2 Epidemiology (quantitative data from recent studies)
- A 2023 review estimates DFNX accounts for **up to ~2%** of hereditary hearing loss and that **POU3F4 accounts for ~50%** of X-linked nonsyndromic hearing loss (bernardinelli2023clinicalandmolecular pages 1-2).
- In a 2024 Chinese cohort, the **aggregate contribution** of X-chromosome genes to genetically solved HL was **~1.14% (22/1922)**, with **POU3F4** representing **~59% (13/22)** of those X-linked diagnosed cases (feng2024genomicandphenotypic pages 1-2).

Population variant frequencies (e.g., gnomAD allele frequencies), founder effects, and carrier frequencies were not available in the retrieved evidence set.

---

## 10. Diagnostics

### 10.1 Clinical tests and phenotyping
A recent large cohort used:
- Audiologic assessment including **PTA, ABR, DPOAE**, and clinical severity grading (feng2024genomicandphenotypic pages 2-4).
- Temporal bone imaging (**HRCT / MRI**) to detect malformations such as IP-III (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 4-5).

### 10.2 Genetic testing strategies (real-world implementation)
In the 2024 Chinese study, genetic diagnosis relied on a combination of a **227-gene panel** (majority of cases) and **whole-exome sequencing**, with **third-generation sequencing (TGS)** used when prior NGS approaches did not yield a diagnosis; the overall molecular diagnostic yield across 3646 probands was **52.72% (1922/3646)** (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 2-4).

### 10.3 Differential diagnosis considerations (DFNX vs syndromic X-linked disorders)
The DFNX framework explicitly distinguishes X-linked nonsyndromic HL genes from syndromic X-linked conditions with HL (e.g., Norrie, Alport) (feng2024genomicandphenotypic pages 1-2).

### 10.4 Screening
The evidence emphasizes early genetic diagnosis and monitoring (especially where progression is expected) but did not provide specific newborn screening or carrier screening program metrics.

---

## 11. Outcome / Prognosis

### 11.1 Hearing outcomes and intervention response
- **Cochlear implantation in IP-III:** In a 2023 cohort of 11 IP-III patients, 9/11 had POU3F4 pathogenic variants, **all surgeries had CSF gushers**, and postoperative auditory performance (CAP scores) **improved significantly** (jung2023geneticcharacteristicsand pages 1-2).
- CI outcomes in IP-III are described as variable across reports, and long-term device/linguistic performance may diverge from typical pediatric CI populations (xu2024researchprogresson pages 2-4).

No DFNX-specific mortality or life-expectancy impacts were identified.

---

## 12. Treatment

### 12.1 Standard-of-care treatments and implementations
- **Hearing aids** and **cochlear implantation (CI)** are the principal current interventions in DFNX populations, selected based on severity and benefit (feng2024genomicandphenotypic pages 10-12, feng2024genomicandphenotypic pages 4-5).

### 12.2 DFNX2/DFN3 (POU3F4) surgical considerations (real-world constraints)
POU3F4/IP-III malformation creates high-risk anatomy (direct cochlea–IAC communication), leading to:
- **Perilymphatic/CSF gusher risk** during surgery (highlighted as universal in the 2023 IP-III CI cohort) (jung2023geneticcharacteristicsand pages 1-2).
- **Electrode misplacement** into the IAC risk; recommendations include specialized electrodes (e.g., “cork” stopper / rings), intra-operative CT confirmation, and other intraoperative sealing/packing strategies (xu2024researchprogresson pages 2-4, feng2024genomicandphenotypic pages 10-12).

### 12.3 Advanced therapeutics and experimental approaches (2023–2024 landscape)

#### Gene therapy: state of the field and applicability to DFNX
A 2023 Molecular Therapy review summarizes that inner ear gene therapy strategies typically include **gene replacement, gene suppression, and gene editing**, and emphasizes the practical advantage of local inner-ear delivery due to its confined fluid-filled anatomy (jiang2023advancesingene pages 1-2, jiang2023advancesingene pages 13-14). It also states that “DFNA, DFNB, and DFNX” denote autosomal dominant, autosomal recessive, and X-linked deafness classifications, respectively (jiang2023advancesingene pages 1-2).

**Clinical translation in 2023–2024 (trial reality):** the retrieved clinical-trial landscape is currently dominated by autosomal recessive targets (notably **OTOF/DFNB9**) rather than DFNX genes. Examples include:
- **DB-OTO** (AAV-based) in children/infants with OTOF-related hearing loss (ClinicalTrials.gov **NCT05788536**, recruiting) (clinical trials search results).
- Additional OTOF programs (e.g., **NCT06722170**) and an RNA base-editing study (**NCT06025032**, withdrawn) (clinical trials search results).

No DFNX gene-targeted interventional gene therapy trial was identified in the retrieved ClinicalTrials.gov results.

### 12.4 MAXO term suggestions
- Hearing aid fitting (MAXO term not retrieved here; concept: hearing aid therapy) (feng2024genomicandphenotypic pages 4-5)
- Cochlear implantation (MAXO concept) (jung2023geneticcharacteristicsand pages 1-2)
- Genetic counseling (MAXO concept) (feng2024genomicandphenotypic pages 1-2)

---

## 13. Prevention
No DFNX-specific primary prevention is established (genetic etiology). Secondary/tertiary prevention is largely through **early identification, timely hearing rehabilitation, and genotype-informed surgical planning** (feng2024genomicandphenotypic pages 4-5, jung2023geneticcharacteristicsand pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring DFNX-analog disease in companion animals was identified in the retrieved evidence.

---

## 15. Model organisms
- **Zebrafish smpx loss-of-function** provides a 2024 in vivo mechanistic model showing impaired mechanosensory hair-cell development/function and reduced mechanotransduction, relevant to SMPX DFNX4 pathogenesis (diana2024differentiationandfunctioning pages 1-2, diana2024differentiationandfunctioning pages 2-3).

---

## Expert synthesis (2023–2024 authoritative interpretation)
1) **POU3F4 is the dominant DFNX gene in practice**: reviews estimate POU3F4 accounts for ~50% of X-linked nonsyndromic HL and DFNX overall contributes up to ~2% of hereditary HL; a large 2024 cohort similarly found POU3F4 comprised ~59% of solved X-linked cases (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 1-2). This convergence supports prioritizing POU3F4 in DFNX diagnostic algorithms and pre-surgical planning.
2) **Genotype-informed otologic surgery is a real-world necessity**: IP-III anatomy produces predictable intraoperative risks (CSF gusher, electrode misplacement). Cohort-level surgical evidence shows universal CSF gusher in IP-III CI and significant functional improvement post-CI, supporting CI as beneficial but requiring specialized technique and counseling (jung2023geneticcharacteristicsand pages 1-2, xu2024researchprogresson pages 2-4).
3) **Therapeutic frontier is moving, but DFNX-specific gene therapy is not yet clinical**: 2023–2024 gene therapy progress is substantial in hereditary HL broadly (vectors, routes, editing strategies), but current registered interventional trials in retrieved evidence largely target DFNB9/OTOF rather than DFNX (jiang2023advancesingene pages 1-2).

---

## Summary tables and key visuals

The following table consolidates DFNX gene–phenotype–variant–management mappings extracted from the evidence.

| Gene | DFNX subtype / OMIM MIM number (as reported in evidence) | Protein/function (brief) | Typical phenotype (onset, severity, progression, imaging) | Common variant types (missense/truncating/CNV/regulatory) | Notes on management (CI, surgical risk) | Key recent/authoritative sources with year, DOI/URL, and PMID if present in text |
|---|---|---|---|---|---|---|
| **PRPS1** | **DFNX1; MIM#304500** (feng2024genomicandphenotypic pages 1-2) | Phosphoribosyl pyrophosphate synthetase 1; enzyme in nucleotide/purine biosynthesis spectrum disorders (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 4-5) | Congenital to childhood onset in cohort; male patients can show progressive hearing loss ranging from moderate to profound; may present as isolated HL or part of broader PRPS1 spectrum (feng2024genomicandphenotypic pages 4-5) | Predominantly **missense**; one duplication variant noted (c.937_940dup) (feng2024genomicandphenotypic pages 4-5) | Hearing aids may be insufficient in some cases; cochlear implantation (CI) improved hearing and communication in cohort when HA benefit was limited, but gene-specific quantitative CI data for PRPS1 were not provided (feng2024genomicandphenotypic pages 4-5, feng2024genomicandphenotypic pages 2-4) | **Feng et al., 2024**, *Orphanet J Rare Dis*; DOI: 10.1186/s13023-024-03338-z; URL: https://doi.org/10.1186/s13023-024-03338-z; PMID: — (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 4-5) |
| **POU3F4** | **DFNX2 / DFN3; OMIM #304400**; gene OMIM *300039 (bernardinelli2023clinicalandmolecular pages 1-2, bernardinelli2023clinicalandmolecular pages 5-7, feng2024genomicandphenotypic pages 6-7) | POU-family transcription factor critical for middle/inner ear development (otic mesenchyme/cochlear development) (bernardinelli2023clinicalandmolecular pages 1-2, xu2024researchprogresson pages 1-2) | Usually congenital or childhood-onset, often severe to profound HL; hallmark imaging is **incomplete partition type III (IP-III)** with absent modiolus/interscalar septa, dilated IAC, abnormal communication between cochlea and IAC; can have mixed or sensorineural HL (bernardinelli2023clinicalandmolecular pages 1-2, feng2024genomicandphenotypic pages 4-5, feng2024genomicandphenotypic pages 6-7, xu2024researchprogresson pages 2-4) | **Missense, nonsense, frameshift, indels, structural variants/CNVs, whole-gene deletions, upstream regulatory deletions/insertions/inversions** (bernardinelli2023clinicalandmolecular pages 5-7, feng2024genomicandphenotypic pages 2-4, jung2023geneticcharacteristicsand pages 1-2) | Most important real-world management issue in DFNX: CI is standard but technically difficult in IP-III. Risks include **CSF/perilymphatic gusher** and **electrode misplacement into the IAC**; pre-op CT/MRI, intra-op imaging, sealing cochleostomy, and shorter/straight or special stopper/ring electrodes are recommended. In one 2023 series of 11 IP-III patients, **all** CI surgeries had CSF gushers and CAP scores improved postoperatively (jung2023geneticcharacteristicsand pages 1-2, xu2024researchprogresson pages 2-4, feng2024genomicandphenotypic pages 10-12) | **Bernardinelli et al., 2023**, *Biomedicines*; DOI: 10.3390/biomedicines11061695; URL: https://doi.org/10.3390/biomedicines11061695; PMID: —. **Feng et al., 2024**; DOI: 10.1186/s13023-024-03338-z; URL: https://doi.org/10.1186/s13023-024-03338-z; PMID: —. **Jung et al., 2023**; DOI: 10.21053/ceo.2023.00864; URL: https://doi.org/10.21053/ceo.2023.00864; PMID: —. **Xu et al., 2024**; DOI: 10.1007/s00405-024-08555-7; URL: https://doi.org/10.1007/s00405-024-08555-7; PMID: — (bernardinelli2023clinicalandmolecular pages 1-2, bernardinelli2023clinicalandmolecular pages 5-7, jung2023geneticcharacteristicsand pages 1-2, xu2024researchprogresson pages 2-4) |
| **SMPX** | **DFNX4; MIM#300066** (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 6-7) | Small muscle protein, X-linked; cytoskeleton-associated protein highly expressed in inner-ear hair cells, linked to hair-cell differentiation/maintenance and mechanotransduction (diana2024differentiationandfunctioning pages 1-2, diana2024differentiationandfunctioning pages 2-3) | Typically progressive NSHL; truncating variants associated with characteristic audiological profiles before and after age 10; female carriers may show variable expressivity, often later onset (4th–5th decade), mild–moderate, symmetric or asymmetric HL; no signature malformation emphasized (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 6-7) | Reported pathogenic spectrum includes **truncating** variants (10/15), **splice-site** variants (3/15), and a small number of **nontruncating/missense** variants; truncating variants linked to DFNX4, whereas nontruncating variants have been associated with distal myopathy (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 6-7) | Standard hearing rehabilitation applies; no DFNX4-specific CI risk profile reported in the provided evidence. Mechanistic animal work supports future targetability by molecular therapies, but no DFNX4 clinical gene therapy trial was identified here (feng2024genomicandphenotypic pages 1-2, diana2024differentiationandfunctioning pages 1-2) | **Feng et al., 2024**; DOI: 10.1186/s13023-024-03338-z; URL: https://doi.org/10.1186/s13023-024-03338-z; PMID: —. **Diana et al., 2024**, *Sci Rep*; DOI: 10.1038/s41598-024-58138-z; URL: https://doi.org/10.1038/s41598-024-58138-z; PMID: — (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 6-7, diana2024differentiationandfunctioning pages 1-2) |
| **AIFM1** | **DFNX5; MIM#300614** (feng2024genomicandphenotypic pages 1-2) | Apoptosis-inducing factor, mitochondria-associated; evidence emphasizes structural/functional residue effects and auditory-neuropathy phenotype (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 10-12) | Congenital or childhood-onset X-linked HL in cohort; causative variants mainly missense; associated with **auditory neuropathy**, postsynaptic lesions, progressive auditory dyssynchrony, and sometimes cochlear nerve hypoplasia (CNH) (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 10-12) | Predominantly **missense** (feng2024genomicandphenotypic pages 1-2) | CI may have **limited success** in AIFM1-related auditory neuropathy compared with some other genetic etiologies; genotype can help guide expectations and treatment choice (feng2024genomicandphenotypic pages 10-12) | **Feng et al., 2024**; DOI: 10.1186/s13023-024-03338-z; URL: https://doi.org/10.1186/s13023-024-03338-z; PMID: — (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 10-12) |
| **COL4A6** | **DFNX6; MIM#303630** (feng2024genomicandphenotypic pages 1-2) | Type IV collagen alpha-6 chain; extracellular matrix/basement membrane component (function not elaborated in detail in provided evidence) (feng2024genomicandphenotypic pages 1-2) | Congenital or childhood-onset HL in cohort; no clear phenotypic differences highlighted among carriers in the 2024 Chinese series; can be associated with cochlear malformation, with one reported example of **cochlear hypoplasia and profound SNHL** (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 2-4) | Specific recurrent class not summarized in detail in provided evidence; sequence variants reported, including **missense** example c.1456G>A (feng2024genomicandphenotypic pages 2-4) | CI can be successful in some malformation-associated DFNX cases; the evidence specifically contrasts better potential CI outcomes in some structural-gene cases with poorer results in AIFM1 auditory neuropathy, but COL4A6-specific outcome statistics were not provided (feng2024genomicandphenotypic pages 10-12, feng2024genomicandphenotypic pages 2-4) | **Feng et al., 2024**; DOI: 10.1186/s13023-024-03338-z; URL: https://doi.org/10.1186/s13023-024-03338-z; PMID: — (feng2024genomicandphenotypic pages 1-2, feng2024genomicandphenotypic pages 2-4) |


*Table: This table summarizes the principal genes and loci implicated in X-linked nonsyndromic hearing loss, with phenotype, variant spectrum, and management implications drawn only from the provided evidence. It is useful for rapid comparison of DFNX subtypes and for linking genotype to imaging and cochlear implant considerations.*

A radiologic comparison figure of normal cochlea vs IP-III and a POU3F4 variant summary table were retrieved from a 2023 review; these support the hallmark IP-III malformation and the breadth of reported variant types (bernardinelli2023clinicalandmolecular media 04c7488e, bernardinelli2023clinicalandmolecular media 46a2f715).

---

## Notes on evidence gaps
- **PMIDs** were not present in the retrieved text excerpts for the key sources; DOIs and journal publication months/years are provided where available.
- **MONDO/Orphanet/ICD/MeSH IDs** for the umbrella “X-linked nonsyndromic hearing loss” term were not retrieved in this tool run.
- **Population allele frequencies (gnomAD)** and **founder variants** were not identified in the retrieved evidence.


References

1. (bernardinelli2023clinicalandmolecular pages 1-2): Emanuele Bernardinelli, Florian Huber, Sebastian Roesch, and Silvia Dossena. Clinical and molecular aspects associated with defects in the transcription factor pou3f4: a review. Biomedicines, 11:1695, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061695, doi:10.3390/biomedicines11061695. This article has 13 citations.

2. (feng2024genomicandphenotypic pages 1-2): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

3. (jiang2023advancesingene pages 1-2): Luoying Jiang, Daqi Wang, Yingzi He, and Yilai Shu. Advances in gene therapy hold promise for treating hereditary hearing loss. Molecular Therapy, 31:934-950, Apr 2023. URL: https://doi.org/10.1016/j.ymthe.2023.02.001, doi:10.1016/j.ymthe.2023.02.001. This article has 127 citations and is from a highest quality peer-reviewed journal.

4. (feng2024genomicandphenotypic pages 4-5): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

5. (bernardinelli2023clinicalandmolecular pages 5-7): Emanuele Bernardinelli, Florian Huber, Sebastian Roesch, and Silvia Dossena. Clinical and molecular aspects associated with defects in the transcription factor pou3f4: a review. Biomedicines, 11:1695, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061695, doi:10.3390/biomedicines11061695. This article has 13 citations.

6. (bernardinelli2023clinicalandmolecular pages 20-21): Emanuele Bernardinelli, Florian Huber, Sebastian Roesch, and Silvia Dossena. Clinical and molecular aspects associated with defects in the transcription factor pou3f4: a review. Biomedicines, 11:1695, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061695, doi:10.3390/biomedicines11061695. This article has 13 citations.

7. (feng2024genomicandphenotypic pages 6-7): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

8. (bernardinelli2023clinicalandmolecular media 04c7488e): Emanuele Bernardinelli, Florian Huber, Sebastian Roesch, and Silvia Dossena. Clinical and molecular aspects associated with defects in the transcription factor pou3f4: a review. Biomedicines, 11:1695, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061695, doi:10.3390/biomedicines11061695. This article has 13 citations.

9. (jung2023geneticcharacteristicsand pages 1-2): Jinsei Jung, Se A Lee, Un-Kyung Kim, In Seok Moon, Heon Yung Gee, and Jae Young Choi. Genetic characteristics and audiological performance after cochlear implantation in patients with incomplete partition type iii. Clinical and Experimental Otorhinolaryngology, 16:403-406, Nov 2023. URL: https://doi.org/10.21053/ceo.2023.00864, doi:10.21053/ceo.2023.00864. This article has 1 citations and is from a peer-reviewed journal.

10. (feng2024genomicandphenotypic pages 10-12): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

11. (feng2024genomicandphenotypic pages 2-4): Haifeng Feng, Shasha Huang, Ying Ma, Jinyuan Yang, Yijin Chen, Guojian Wang, Mingyu Han, Dongyang Kang, Xin Zhang, Pu Dai, and Yongyi Yuan. Genomic and phenotypic landscapes of x-linked hereditary hearing loss in the chinese population. Orphanet Journal of Rare Diseases, Sep 2024. URL: https://doi.org/10.1186/s13023-024-03338-z, doi:10.1186/s13023-024-03338-z. This article has 6 citations and is from a peer-reviewed journal.

12. (diana2024differentiationandfunctioning pages 1-2): Alberto Diana, Anna Ghilardi, and Luca Del Giacco. Differentiation and functioning of the lateral line organ in zebrafish require smpx activity. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58138-z, doi:10.1038/s41598-024-58138-z. This article has 1 citations and is from a peer-reviewed journal.

13. (diana2024differentiationandfunctioning pages 2-3): Alberto Diana, Anna Ghilardi, and Luca Del Giacco. Differentiation and functioning of the lateral line organ in zebrafish require smpx activity. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-58138-z, doi:10.1038/s41598-024-58138-z. This article has 1 citations and is from a peer-reviewed journal.

14. (xu2024researchprogresson pages 2-4): Kaifan Xu, Yun Xiao, Jianfen Luo, Xiuhua Chao, Ruijie Wang, Zhaoming Fan, Haibo Wang, and Lei Xu. Research progress on incomplete partition type 3 inner ear malformation. European Archives of Oto-Rhino-Laryngology, 281:3943-3948, Mar 2024. URL: https://doi.org/10.1007/s00405-024-08555-7, doi:10.1007/s00405-024-08555-7. This article has 5 citations and is from a peer-reviewed journal.

15. (jiang2023advancesingene pages 13-14): Luoying Jiang, Daqi Wang, Yingzi He, and Yilai Shu. Advances in gene therapy hold promise for treating hereditary hearing loss. Molecular Therapy, 31:934-950, Apr 2023. URL: https://doi.org/10.1016/j.ymthe.2023.02.001, doi:10.1016/j.ymthe.2023.02.001. This article has 127 citations and is from a highest quality peer-reviewed journal.

16. (xu2024researchprogresson pages 1-2): Kaifan Xu, Yun Xiao, Jianfen Luo, Xiuhua Chao, Ruijie Wang, Zhaoming Fan, Haibo Wang, and Lei Xu. Research progress on incomplete partition type 3 inner ear malformation. European Archives of Oto-Rhino-Laryngology, 281:3943-3948, Mar 2024. URL: https://doi.org/10.1007/s00405-024-08555-7, doi:10.1007/s00405-024-08555-7. This article has 5 citations and is from a peer-reviewed journal.

17. (bernardinelli2023clinicalandmolecular media 46a2f715): Emanuele Bernardinelli, Florian Huber, Sebastian Roesch, and Silvia Dossena. Clinical and molecular aspects associated with defects in the transcription factor pou3f4: a review. Biomedicines, 11:1695, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061695, doi:10.3390/biomedicines11061695. This article has 13 citations.