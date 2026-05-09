---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T21:37:00.687363'
end_time: '2026-05-04T21:54:06.373589'
duration_seconds: 1025.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hereditary Arterial and Articular Multiple Calcification Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Arterial and Articular Multiple Calcification Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Arterial and Articular Multiple Calcification Syndrome** covering all of the
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
- **Disease Name:** Hereditary Arterial and Articular Multiple Calcification Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Arterial and Articular Multiple Calcification Syndrome** covering all of the
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


# Hereditary Arterial and Articular Multiple Calcification Syndrome (HAAMCS) / CALJA / ACDC — Disease Characteristics Research Report

## Executive summary
Hereditary arterial and articular multiple calcification syndrome is an ultra-rare Mendelian ectopic-mineralization disorder caused by biallelic loss-of-function variants in **NT5E** (encoding the ecto-5′-nucleotidase **CD73**). It is characterized by **medial calcification of medium-to-large peripheral arteries (predominantly lower extremities)** and **periarticular calcifications** (often hands/feet/wrists/ankles), producing **intermittent claudication and chronic limb ischemia** plus **arthritis-like symptoms, early osteoarthritis, severe joint pain and deformity**. The best-supported molecular mechanism is loss of CD73-generated **adenosine**, leading to **increased TNAP activity**, reduced functional **pyrophosphate (PPi)** anti-mineralization capacity, and increased propensity for **hydroxyapatite** deposition in arterial media and periarticular tissues. Recent (2024) clinical-trial evidence suggests **etidronate** is safe and may **slow progression** of lower-extremity arterial calcification on CT, without reversal of established calcifications.

## 1. Disease information
### 1.1 Concise overview (what is the disease?)
Arterial calcification due to deficiency of CD73 (ACDC; used synonymously with CALJA/HAAMCS in recent clinical literature) is described as a “very rare autosomal recessive ectopic mineralization syndrome” caused by loss-of-function variants in **NT5E**, producing “massive de novo calcifications” in the **media** of medium-to-large arteries (predominantly lower extremities) and **periarticular regions**, causing **claudication, rest ischemic pain, severe joint pain, and deformities**. (ferrante2024pilotstudyto pages 1-3)

### 1.2 Key identifiers and synonyms
A compact normalization table is provided below.

| Field | Value |
|---|---|
| Preferred name | Hereditary arterial and articular multiple calcification syndrome (ferrante2024pilotstudyto pages 1-3) |
| Major synonyms | Calcification of joints and arteries (CALJA); arterial calcification due to deficiency of CD73 (ACDC); CD73 deficiency / NT5E deficiency–associated arterial and periarticular calcification (maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 6-7) |
| MONDO ID | MONDO:0008895 (Open Targets disease association output) |
| OMIM ID | OMIM 211800 (reported for ACDC) (ferrante2024pilotstudyto pages 1-3) |
| Causal gene | NT5E (encodes CD73; 5'-nucleotidase ecto) (ferrante2024pilotstudyto pages 1-3, hilaire2011nt5emutationsandarterial pages 1-2) |
| Inheritance | Autosomal recessive; biallelic loss-of-function variants reported, including homozygous and compound heterozygous cases (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2, hilaire2011nt5emutationsandarterial pages 5-6, markello2011vascularpathologyof pages 2-4) |
| Epidemiology notes | Ultra-rare disorder; fewer than 20 patients reported worldwide in the 2024 pilot-study background, while the 2023 CALJA review states 23 published cases; prevalence estimated as <1 in 1,000,000 (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 2-5) |


*Table: This table summarizes the core naming and identifier information for hereditary arterial and articular multiple calcification syndrome, including accepted synonyms and disease-gene linkage. It is useful as a compact normalization reference for downstream knowledge base entry and curation.*

**Notes on missing identifiers:** Orphanet, ICD-10/ICD-11, and MeSH identifiers were not present in the retrieved evidence set and therefore cannot be asserted here.

### 1.3 Evidence source type
Evidence in this report is derived primarily from:
- Human primary clinical genetics (NEJM 2011) and case series/case reports (human clinical evidence). (hilaire2011nt5emutationsandarterial pages 1-2, mandalapu2024imagingfindingsof pages 1-2)
- Human interventional trial protocol and pilot study (NIH; NCT01585402; Vascular Medicine 2024). (NCT01585402 chunk 2, ferrante2024pilotstudyto pages 1-3, ferrante2024pilotstudyto pages 6-8)
- Mouse knockout model and mechanistic cell studies (in vivo and in vitro). (li2014juxtaarticularjointcapsulemineralization pages 1-3, hilaire2011nt5emutationsandarterial pages 8-10)
- Recent mechanistic reviews situating the ABCC6→ENPP1→CD73→TNAP axis in ectopic calcification disorders. (kauffenstein2024thepurinergicnature pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors
- **Primary cause:** germline **biallelic (autosomal recessive) loss-of-function** variants in **NT5E**, encoding CD73. (ferrante2024pilotstudyto pages 1-3, hilaire2011nt5emutationsandarterial pages 1-2)
- **Mechanistic cause:** CD73 deficiency disrupts extracellular nucleotide metabolism (AMP→adenosine) and removes adenosine-mediated suppression of TNAP, promoting ectopic calcification. (hilaire2011nt5emutationsandarterial pages 8-10, hilaire2011nt5emutationsandarterial pages 10-11)

### 2.2 Risk factors
- **Genetic:** pathogenic NT5E variants (see Section 4). Autosomal recessive inheritance is supported by consanguinity in an early pedigree and homozygous/compound heterozygous genotypes across families. (hilaire2011nt5emutationsandarterial pages 5-6, markello2011vascularpathologyof pages 2-4)
- **Environmental/clinical:** no validated environmental risk factors were identified in the retrieved disease-specific sources. General vascular-calcification literature emphasizes phosphate/pyrophosphate balance (e.g., hyperphosphatemia, PPi deficiency) as drivers of calcification, but these are not established as CALJA-specific modifiable risk factors. (villabellosta2024vascularcalcificationa pages 1-2, villabellosta2024vascularcalcificationa pages 6-7)

### 2.3 Protective factors
No disease-specific genetic or environmental protective factors were identified in the retrieved evidence. Mechanistically, **restoring adenosine signaling** or **inhibiting TNAP** reduces calcification in patient-derived cellular models, implying pathway-level protection, but this is not yet established as a clinical protective factor. (hilaire2011nt5emutationsandarterial pages 8-10)

### 2.4 Gene–environment interactions
No explicit gene–environment interaction studies specific to CALJA/ACDC were identified in the retrieved evidence. However, murine phenotype expressivity varies with genetic background (e.g., Abcc6 allele confounding) and diet (high phosphorus/low magnesium “acceleration diet”), suggesting context dependence in ectopic mineralization processes. (li2014juxtaarticularjointcapsulemineralization pages 3-4, li2014juxtaarticularjointcapsulemineralization pages 6-7)

## 3. Phenotypes
A structured phenotype table with HPO suggestions is provided here.

| Clinical phenotype | Phenotype type | Suggested HPO term(s) | Brief evidence-based notes on onset / frequency / severity | Key sources |
|---|---|---|---|---|
| Medial arterial calcification of lower extremities | Imaging / vascular sign | HP:0004967 Peripheral arterial calcification; HP:0005124 Arteriosclerosis | Hallmark feature; typically affects medium-to-large lower-extremity arteries (femoral, popliteal, tibial) with medial, nonatherosclerotic calcification. Adult presentation predominates; joint symptoms may begin earlier. Often severe and progressive. (ferrante2024pilotstudyto pages 1-3, joolharzadeh2019cd73(clusterof pages 2-3, hilaire2011nt5emutationsandarterial pages 5-6, mandalapu2024imagingfindingsof pages 1-2) | (ferrante2024pilotstudyto pages 1-3, joolharzadeh2019cd73(clusterof pages 2-3, hilaire2011nt5emutationsandarterial pages 5-6, mandalapu2024imagingfindingsof pages 1-2) |
| Intermittent claudication | Symptom | HP:0005117 Intermittent claudication | One of the most consistent symptomatic vascular manifestations; mean onset around 29 years in the 2024 pilot-study background. Can become activity-limiting and progress to rest pain/chronic ischemia. (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2) | (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2) |
| Low ankle-brachial index (ABI) | Functional / vascular test abnormality | HP:0030879 Abnormal ankle-brachial index | Reduced ABI reflects lower-limb ischemia; examples include <0.8 in review summaries, 0.59/0.58 in one rheumatology case, and 0.4 bilaterally in a 2024 imaging case. Severity varies but may be marked. (joolharzadeh2019cd73(clusterof pages 2-3, ichikawa2015arterialcalcificationdue pages 1-1, mandalapu2024imagingfindingsof pages 1-2) | (joolharzadeh2019cd73(clusterof pages 2-3, ichikawa2015arterialcalcificationdue pages 1-1, mandalapu2024imagingfindingsof pages 1-2) |
| Chronic limb ischemia, arterial occlusion, or limb-threatening ischemia | Clinical sign / complication | HP:0005290 Peripheral vascular insufficiency; HP:0005114 Arterial occlusion | Progressive vascular disease may lead to femoropopliteal obliteration/occlusion, chronic foot ischemia, ulcers, or chronic limb-threatening ischemia. Severe cases may require bypass surgery. (ferrante2024pilotstudyto pages 6-8, hilaire2011nt5emutationsandarterial pages 5-6, maffi2023calcificationofjoints pages 2-5, maffi2023calcificationofjoints pages 5-6) | (ferrante2024pilotstudyto pages 6-8, hilaire2011nt5emutationsandarterial pages 5-6, maffi2023calcificationofjoints pages 2-5, maffi2023calcificationofjoints pages 5-6) |
| Periarticular soft-tissue calcification of hands/feet | Imaging / musculoskeletal sign | HP:0005686 Calcification of hand joints; HP:0100590 Periarticular calcification | Core musculoskeletal hallmark, often involving wrists, hands, ankles, and feet; commonly visible on radiographs or CT. Joint manifestations often begin in adolescence or early adulthood; can be bulky and painful. (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4) | (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4) |
| Arthritis / recurrent non-erosive mono- or oligoarthritis | Clinical diagnosis / symptom complex | HP:0001369 Arthritis | Frequently causes rheumatology referral and misdiagnosis as inflammatory arthritis. Described as recurrent, migratory, asymmetric, and typically non-erosive; may improve with colchicine or NSAIDs in some reports. (maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 2-5) | (maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 2-5) |
| Early-onset osteoarthritis / degenerative joint disease | Clinical sign | HP:0002758 Osteoarthritis; HP:0003074 Early onset | CALJA is repeatedly described as causing early osteoarthritis, particularly in small joints of hands/feet, sometimes beginning in adolescence. Severity is variable; deformity may develop over time. (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2) | (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2) |
| Joint pain and deformity | Symptom / physical manifestation | HP:0002829 Arthralgia; HP:0001376 Joint deformity | Severe joint pain is common and may be debilitating; the 2024 pilot-study background highlights severe joint pain and deformities as major disease burdens. Can persist despite limited effect of current therapies on calcification burden. (ferrante2024pilotstudyto pages 6-8, ferrante2024pilotstudyto pages 1-3, joolharzadeh2019cd73(clusterof pages 4-5) | (ferrante2024pilotstudyto pages 6-8, ferrante2024pilotstudyto pages 1-3, joolharzadeh2019cd73(clusterof pages 4-5) |
| Arterial tortuosity, ectasia, or arteriomegaly | Imaging / vascular sign | HP:0002616 Arterial tortuosity; HP:0030964 Arterial ectasia; HP:0030963 Arteriomegaly | Distinctive vascular morphology in some patients, especially femoral/popliteal arteries; can accompany calcification and help distinguish from typical atherosclerotic PAD. Seen on CT, radiographs, and angiographic studies. (joolharzadeh2019cd73(clusterof pages 2-3, hilaire2011nt5emutationsandarterial pages 5-6, mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 4-6) | (joolharzadeh2019cd73(clusterof pages 2-3, hilaire2011nt5emutationsandarterial pages 5-6, mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 4-6) |
| Pseudogout / CPPD-like acute calcific episodes | Episodic symptom complex | HP:0005191 Pseudogout | Some patients have pseudogout-like attacks or are described as having calcific periarthritis / CPPD-like disease; dual-energy CT may exclude urate and support non-gout crystal deposition. Evidence is case-based rather than cohort-based. (markello2011vascularpathologyof pages 2-4, mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4) | (markello2011vascularpathologyof pages 2-4, mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4) |
| Elevated inflammatory markers (subset) | Laboratory abnormality | HP:0003565 Increased erythrocyte sedimentation rate; HP:0011227 Increased C-reactive protein level | Not universal. Some cases, including the 2023 review case, showed persistently elevated ESR/CRP that improved with colchicine; other reports documented normal ESR/CRP. Best treated as a variable, non-core phenotype. (maffi2023calcificationofjoints pages 2-5, mandalapu2024imagingfindingsof pages 1-2) | (maffi2023calcificationofjoints pages 2-5, mandalapu2024imagingfindingsof pages 1-2) |
| Normal serum calcium, phosphate, and parathyroid hormone | Laboratory finding / often normal studies | HP:0011047 Abnormal serum calcium level; HP:0002905 Abnormal serum phosphate level; HP:0030312 Abnormal parathyroid hormone level | Routine mineral metabolism tests are often normal despite extensive ectopic calcification. Reports specifically note normal calcium, phosphate, vitamin D, renal function, and/or PTH in several patients. This is diagnostically useful because dramatic calcification occurs without classic systemic mineral imbalance. (ichikawa2015arterialcalcificationdue pages 1-1, hilaire2011nt5emutationsandarterial pages 1-2, mandalapu2024imagingfindingsof pages 1-2) | (ichikawa2015arterialcalcificationdue pages 1-1, hilaire2011nt5emutationsandarterial pages 1-2, mandalapu2024imagingfindingsof pages 1-2) |


*Table: This table summarizes the core clinical and laboratory phenotypes reported for calcification of joints and arteries / arterial calcification due to CD73 deficiency, with suggested HPO terms and concise notes on onset, frequency, and severity where available. It is designed to support disease knowledge-base curation and phenotype annotation.*

### 3.1 Age of onset and progression (from clinical evidence)
- Mean age for **joint symptoms**: ~17 years (pilot-study background). (ferrante2024pilotstudyto pages 1-3)
- Mean age for **claudication**: ~29 years (pilot-study background). (ferrante2024pilotstudyto pages 1-3)
- Disease can progress to severe occlusive disease: in the 2024 etidronate pilot cohort, all had activity-limiting claudication and “complete occlusion of most of the large lower-extremity arteries” was noted as baseline severity in many. (ferrante2024pilotstudyto pages 6-8)

### 3.2 Quality of life impact
Direct validated QoL instruments (EQ-5D/SF-36/PROMIS) were not found in the retrieved evidence. Functional limitation is strongly implied by activity-limiting claudication and severe joint pain/deformities in trial/case literature. (ferrante2024pilotstudyto pages 6-8, ferrante2024pilotstudyto pages 1-3)

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
- **NT5E** (encodes CD73; ecto-5′-nucleotidase) is the established causal gene. (hilaire2011nt5emutationsandarterial pages 1-2)

### 4.2 Pathogenic variants (examples and classes)
Variant examples and classes are summarized here.

| HGVS cDNA | Protein change | Variant class | Zygosity / inheritance context | Source paper / year | Key associated phenotype notes |
|---|---|---|---|---|---|
| c.662C>A | p.S221X | Nonsense | Homozygous in Family 1; autosomal recessive. Also reported as one allele in compound heterozygous patient | St Hilaire et al., 2011; Markello et al., 2011 (hilaire2011nt5emutationsandarterial pages 1-2, markello2011vascularpathologyof pages 2-4) | Symptomatic lower-extremity arterial calcification with periarticular hand/foot joint-capsule calcification; femoropopliteal occlusion and claudication/rest pain spectrum (hilaire2011nt5emutationsandarterial pages 1-2, hilaire2011nt5emutationsandarterial pages 5-6) |
| c.1073G>A | p.C358Y | Missense | Homozygous in Family 2; autosomal recessive | St Hilaire et al., 2011 (hilaire2011nt5emutationsandarterial pages 7-8, hilaire2011nt5emutationsandarterial pages 1-2) | Lower-limb radiographic/CT arterial calcifications with periarticular calcification; adult-onset symptomatic disease (hilaire2011nt5emutationsandarterial pages 7-8, hilaire2011nt5emutationsandarterial pages 5-6) |
| c.1609dupA | p.V537fsX7 | Frameshift | Compound heterozygous with c.662C>A in Family 3 / individual case; autosomal recessive | St Hilaire et al., 2011; Markello et al., 2011 (hilaire2011nt5emutationsandarterial pages 7-8, markello2011vascularpathologyof pages 2-4) | Early exertional calf pain, reduced ABI, extensive medial arterial calcification, periarticular calcifications/pseudogout, arteriomegaly/aneurysmal change (markello2011vascularpathologyof pages 2-4) |
| c.3G>C | p.M1I | Start-loss / initiation codon variant | Reported in later families/case summaries; biallelic recessive context in CALJA literature | Joolharzadeh & St Hilaire, 2019; Maffi et al., 2023 (joolharzadeh2019cd73(clusterof pages 2-3, maffi2023calcificationofjoints pages 2-5) | CALJA/ACDC phenotype with intermittent claudication, lower-extremity arterial insufficiency, periarticular calcifications and arthritis/early osteoarthritis (joolharzadeh2019cd73(clusterof pages 2-3, maffi2023calcificationofjoints pages 2-5) |
| c.751+2T>C | — (splice; exon 3 skipping reported) | Splice-site | Reported in recessive CALJA families/case summaries | Joolharzadeh & St Hilaire, 2019; Maffi et al., 2023 (joolharzadeh2019cd73(clusterof pages 2-3, maffi2023calcificationofjoints pages 2-5) | Periarticular calcification and lower-limb arterial calcification/ischemia consistent with CALJA phenotype (joolharzadeh2019cd73(clusterof pages 2-3, maffi2023calcificationofjoints pages 2-5) |
| c.751+1G>A | — | Splice-donor | Novel homozygous variant in 2023 case report; autosomal recessive | Maffi et al., 2023 (maffi2023calcificationofjoints pages 1-2) | Chronic arthritis, recurrent migratory non-erosive arthritis, extensive periarticular calcific deposits, bilateral femoral/popliteal obliteration, claudication; inflammatory markers improved with colchicine (maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 2-5) |
| c.1387C>T | p.R463X | Nonsense | Reported in 2024 radiology case as pathogenic NT5E variant; zygosity not specified in retrieved excerpt | Mandalapu & Stevens, 2024 (mandalapu2024imagingfindingsof pages 1-2) | Severe bilateral femoral/popliteal calcification and tortuosity/ectasia, periarticular hand/foot/wrist calcifications, ABI as low as 0.4, chronic claudication/ischemia (mandalapu2024imagingfindingsof pages 1-2) |


*Table: This table summarizes NT5E pathogenic variants reported in the retrieved evidence for hereditary arterial and articular multiple calcification syndrome / CALJA / ACDC. It highlights variant class, inheritance context, and the main associated vascular and periarticular phenotypes for rapid knowledge-base curation.*

**Variant classes observed across reports include:** nonsense, missense, frameshift, splice-site, and start-loss variants. (hilaire2011nt5emutationsandarterial pages 7-8, joolharzadeh2019cd73(clusterof pages 2-3, maffi2023calcificationofjoints pages 1-2)

**ClinVar/gnomAD allele frequency data:** not available in the retrieved full-text evidence; therefore, population frequencies cannot be reliably reported here.

### 4.3 Functional consequences
Primary data indicate NT5E mutations produced “essentially nonfunctional CD73,” with patient fibroblasts showing nearly absent CD73 activity and rescue of AMP-dependent phosphate production after CD73 re-expression. (hilaire2011nt5emutationsandarterial pages 7-8)

### 4.4 Pathways and mechanistic chain (current understanding)
**Core pathway (disease-relevant extracellular purine/PPi axis):**
- ENPP1 converts extracellular ATP to AMP and **pyrophosphate (PPi)**; CD73 (NT5E) converts AMP to **adenosine** and inorganic phosphate (Pi). (hilaire2011nt5emutationsandarterial pages 10-11)
- PPi inhibits calcification; TNAP degrades PPi; **adenosine inhibits TNAP**. Thus, CD73 deficiency lowers adenosine, increasing TNAP activity and favoring calcification. (hilaire2011nt5emutationsandarterial pages 10-11)

**Direct mechanistic evidence (patient cells):** CD73-deficient fibroblasts showed increased TNAP staining/activity and calcium phosphate crystal formation that was prevented by CD73 rescue, adenosine supplementation, or a TNAP inhibitor (levamisole). (hilaire2011nt5emutationsandarterial pages 8-10)

**Integration with broader ectopic calcification spectrum (recent review perspective, 2024):** ABCC6, ENPP1, and CD73 are presented as a functional sequence generating two inhibitors of calcification—PPi and adenosine—and CALJA (NT5E/CD73 mutations) is described as part of a continuum with PXE and GACI. (kauffenstein2024thepurinergicnature pages 1-2)

### Suggested ontology terms
- **GO Biological Process (examples):** extracellular nucleotide catabolic process; regulation of biomineral tissue development; regulation of alkaline phosphatase activity; biomineralization.
- **GO Molecular Function (examples):** 5′-nucleotidase activity; AMP phosphohydrolase activity.
- **CL (cell types likely central):** vascular smooth muscle cell (VSMC); fibroblast.

(These ontology suggestions reflect the mechanisms explicitly described in primary studies and reviews, but are not directly enumerated in the retrieved texts.) (hilaire2011nt5emutationsandarterial pages 8-10, joolharzadeh2019cd73(clusterof pages 2-3)

## 5. Environmental information
No disease-specific environmental, lifestyle, toxin, or infectious triggers were identified in the retrieved evidence. Murine work indicates that mineralization phenotypes can be influenced by dietary phosphorus/magnesium content and genetic background, but translation to human modifiable exposures remains unproven. (li2014juxtaarticularjointcapsulemineralization pages 6-7, li2014juxtaarticularjointcapsulemineralization pages 3-4)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (upstream → downstream)
1. **Trigger:** biallelic LOF variants in **NT5E** → absent/nonfunctional **CD73**. (hilaire2011nt5emutationsandarterial pages 1-2)
2. **Upstream biochemical effect:** impaired conversion of AMP to **adenosine** (reduced extracellular adenosine signaling). (hilaire2011nt5emutationsandarterial pages 10-11)
3. **Intermediate regulatory effect:** reduced adenosine-mediated inhibition of **TNAP** → increased TNAP activity and accelerated PPi breakdown. (hilaire2011nt5emutationsandarterial pages 10-11, hilaire2011nt5emutationsandarterial pages 8-10)
4. **Downstream physicochemical effect:** reduced local anti-mineralization capacity (functional PPi deficiency / increased Pi/PPi ratio) → calcium phosphate (hydroxyapatite) precipitation in susceptible tissues. (hilaire2011nt5emutationsandarterial pages 8-10, maffi2023calcificationofjoints pages 1-2)
5. **Tissue pathology:** medial arterial calcification (peripheral arteries) + periarticular calcific deposits. (ferrante2024pilotstudyto pages 1-3, mandalapu2024imagingfindingsof pages 1-2)
6. **Clinical manifestations:** claudication/ischemia and arthritis-like pain/deformity. (ferrante2024pilotstudyto pages 1-3, mandalapu2024imagingfindingsof pages 1-2)

### 6.2 Cell types and processes
- Human pathology is described as **medial** and **nonatherosclerotic** calcification with vascular smooth muscle disorganization/dysplasia in review summaries. (joolharzadeh2019cd73(clusterof pages 2-3)
- Patient-derived fibroblast models demonstrate TNAP upregulation and crystal formation under calcifying conditions. (hilaire2011nt5emutationsandarterial pages 8-10)

## 7. Anatomical structures affected
### 7.1 Organ/system level
- **Cardiovascular system:** lower-extremity arteries (femoral, popliteal, tibial and related beds) are the dominant vascular sites; trunk/coronaries may be relatively spared in some imaging cases. (mandalapu2024imagingfindingsof pages 1-2, maffi2023calcificationofjoints pages 5-6)
- **Musculoskeletal system:** periarticular tissues and small joints of hands/feet/wrists/ankles; can involve other joints (feet/shoulders/elbows/hips/spine) in the etidronate pilot cohort description. (ferrante2024pilotstudyto pages 6-8)

### 7.2 Tissue/cell level and suggested ontology mapping
- **UBERON (examples):** femoral artery; popliteal artery; tibial artery; wrist joint; metacarpophalangeal joint; periarticular region.
- **CL (examples):** vascular smooth muscle cell; fibroblast.
- **GO cellular component (examples):** extracellular region; plasma membrane (for GPI-anchored CD73).

(These are suggested mappings; the retrieved evidence provides strong anatomic specificity but does not itself enumerate UBERON/CL identifiers.) (mandalapu2024imagingfindingsof pages 1-2, ferrante2024pilotstudyto pages 6-8)

## 8. Temporal development
- Onset is typically adolescent-to-adult, with joint manifestations reported earlier than vascular claudication on average. (ferrante2024pilotstudyto pages 1-3)
- Course is progressive in many cases, potentially leading to occlusions and chronic limb-threatening ischemia. (ferrante2024pilotstudyto pages 6-8, maffi2023calcificationofjoints pages 5-6)

## 9. Inheritance and population
- **Inheritance:** autosomal recessive (supported by consanguinity, disease confined to one generation, and biallelic genotypes). (hilaire2011nt5emutationsandarterial pages 5-6, markello2011vascularpathologyof pages 2-4)
- **Epidemiology:** ultra-rare. A 2024 trial background states “fewer than 20 patients reported worldwide” and a prevalence “<1 in 1,000,000,” while a 2023 CALJA review states “Only 23 cases have been described so far.” (ferrante2024pilotstudyto pages 1-3, maffi2023calcificationofjoints pages 1-2)
- **Population-specific variants/founder effects:** not systematically established in the retrieved evidence.

## 10. Diagnostics
A structured diagnostics and management table is provided below.

| Domain | Modality/Intervention | Details | Evidence/implementation notes | Source |
|---|---|---|---|---|
| Diagnostic | CT calcium scoring (LECaS) | Lower-extremity CT calcium score used as a primary endpoint in the NIH etidronate study; protocol adapted coronary calcium-scoring concepts for the overwhelming lower-extremity calcification burden in ACDC/CALJA | Used longitudinally to assess progression rather than reversal; in the 3-year pilot, etidronate appeared to slow/halt progression of lower-extremity arterial calcification, though existing calcification was not reversed (ferrante2024pilotstudyto pages 3-4, NCT01585402 chunk 2, ferrante2024pilotstudyto pages 6-8) | Ferrante et al., 2024; NCT01585402 (ferrante2024pilotstudyto pages 3-4, NCT01585402 chunk 2, ferrante2024pilotstudyto pages 6-8) |
| Diagnostic | Ankle-brachial index (ABI) | Rest and post-exercise ABI used to quantify ischemia and vascular blood flow | Characteristically reduced in affected patients; examples include ABI 0.59/0.58 in a rheumatology case, 0.4 bilaterally in the 2024 imaging case, later 0.66 right and 0.74 left on follow-up; trial used ABI as a co-primary outcome but functional improvement was limited (ichikawa2015arterialcalcificationdue pages 1-1, mandalapu2024imagingfindingsof pages 1-2, ferrante2024pilotstudyto pages 6-8) | Ichikawa et al., 2015; Mandalapu & Stevens, 2024; Ferrante et al., 2024 (ichikawa2015arterialcalcificationdue pages 1-1, mandalapu2024imagingfindingsof pages 1-2, ferrante2024pilotstudyto pages 6-8) |
| Diagnostic | Plain radiographs | X-rays of knees, hands, feet, and affected vascular territories show extensive periarticular calcific deposits and dense arterial calcification | Practical first-line imaging for small-joint/periarticular calcification and peripheral arterial calcification; frequently reveals calcifications that prompt NT5E-directed workup (ichikawa2015arterialcalcificationdue pages 1-1, maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2) | Ichikawa et al., 2015; Maffi et al., 2023; Mandalapu & Stevens, 2024 (ichikawa2015arterialcalcificationdue pages 1-1, maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2) |
| Diagnostic | MRI (incidental vascular finding) | Knee MRI performed for meniscal symptoms incidentally demonstrated marked tortuosity and dense calcification of the popliteal artery | Illustrates that ACDC/CALJA may first be recognized incidentally on musculoskeletal imaging; should trigger review of prior vascular imaging and broader calcification differential (mandalapu2024imagingfindingsof pages 1-2) | Mandalapu & Stevens, 2024 (mandalapu2024imagingfindingsof pages 1-2) |
| Diagnostic | Dual-energy CT | Dual-energy CT of extremities showed extensive periarticular soft-tissue calcifications in wrists, hands, ankles, and feet without uric acid signal | Helpful in differentiating ACDC/CALJA from gout/tophaceous disease; supports calcium-containing periarticular deposits rather than monosodium urate (mandalapu2024imagingfindingsof pages 1-2) | Mandalapu & Stevens, 2024 (mandalapu2024imagingfindingsof pages 1-2) |
| Diagnostic | Doppler ultrasound | Demonstrated bilateral obliteration/occlusion of femoral and popliteal arteries in a CALJA case | Useful noninvasive vascular screen in patients with claudication and suspected lower-limb arterial disease; complements ABI and CT/radiography (maffi2023calcificationofjoints pages 1-2) | Maffi et al., 2023 (maffi2023calcificationofjoints pages 1-2) |
| Diagnostic | Genetic testing for NT5E | Diagnosis established by identifying biallelic/inactivating NT5E variants; variants reported in the literature include nonsense, missense, frameshift, start-loss, and splice-site changes | Recommended when lower-extremity arterial calcification coexists with periarticular calcification/arthritis-like disease; case reports emphasize systematic calcification NGS panels including NT5E and related genes in differential diagnosis (maffi2023calcificationofjoints pages 1-2, hilaire2011nt5emutationsandarterial pages 7-8, hilaire2011nt5emutationsandarterial pages 1-2, joolharzadeh2019cd73(clusterof pages 2-3) | St Hilaire et al., 2011; Maffi et al., 2023; review data (maffi2023calcificationofjoints pages 1-2, hilaire2011nt5emutationsandarterial pages 7-8, hilaire2011nt5emutationsandarterial pages 1-2, joolharzadeh2019cd73(clusterof pages 2-3) |
| Diagnostic | Laboratory evaluation | Serum calcium, phosphate, vitamin D, renal function, PTH, ESR/CRP, RF, anti-CCP, and uric acid are commonly checked | Many reports note normal Ca/P/PTH and negative rheumatologic markers despite marked calcification; inflammatory markers can be normal or elevated in some inflammatory/articular presentations (hilaire2011nt5emutationsandarterial pages 1-2, ichikawa2015arterialcalcificationdue pages 1-1, mandalapu2024imagingfindingsof pages 1-2, maffi2023calcificationofjoints pages 2-5) | St Hilaire et al., 2011; Ichikawa et al., 2015; Mandalapu & Stevens, 2024; Maffi et al., 2023 (hilaire2011nt5emutationsandarterial pages 1-2, ichikawa2015arterialcalcificationdue pages 1-1, mandalapu2024imagingfindingsof pages 1-2, maffi2023calcificationofjoints pages 2-5) |
| Therapy | Etidronate (bisphosphonate) | Open-label NIH pilot: 14 days every 3 months for 3 years (12 cycles), 20 mg/kg daily or 10 mg/kg twice daily; seven genetically confirmed adults enrolled | Safe and generally well tolerated; did not reverse established vascular/periarticular calcifications but appeared to slow progression of lower-extremity vascular calcification on CT; no clear ABI/treadmill improvement; adverse events were mainly GI/arthralgia with two grade 3 possibly related events (ferrante2024pilotstudyto pages 3-4, ferrante2024pilotstudyto pages 1-3, ferrante2024pilotstudyto pages 6-8) | Ferrante et al., 2024; NCT01585402 (ferrante2024pilotstudyto pages 3-4, ferrante2024pilotstudyto pages 1-3, ferrante2024pilotstudyto pages 6-8) |
| Therapy | Colchicine | Used in a CALJA patient with recurrent non-erosive inflammatory arthritis and elevated ESR/CRP | Reported to improve articular symptoms and normalize inflammatory markers, but lower-limb claudication was unaffected; evidence limited to case-level observation (maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 2-5, maffi2023calcificationofjoints pages 5-6) | Maffi et al., 2023 (maffi2023calcificationofjoints pages 1-2, maffi2023calcificationofjoints pages 2-5, maffi2023calcificationofjoints pages 5-6) |
| Therapy | NSAIDs | Used for acute periarticular/arthritis-like flares and pain control | Case literature reports effective treatment of acute joint flares with NSAIDs; supportive rather than disease-modifying (ichikawa2015arterialcalcificationdue pages 1-1, maffi2023calcificationofjoints pages 5-6) | Ichikawa et al., 2015; Maffi et al., 2023 (ichikawa2015arterialcalcificationdue pages 1-1, maffi2023calcificationofjoints pages 5-6) |
| Therapy | Surgical revascularization / bypass | Example: femoral-to-posterior tibial bypass in a patient with severe ischemic disease from NT5E deficiency | Can improve symptoms in advanced occlusive disease/chronic limb-threatening ischemia; reflects real-world management when arterial obstruction is severe (markello2011vascularpathologyof pages 2-4, maffi2023calcificationofjoints pages 5-6) | Markello et al., 2011; Maffi et al., 2023 (markello2011vascularpathologyof pages 2-4, maffi2023calcificationofjoints pages 5-6) |
| Therapy | Antiplatelet therapy and statin | Real-world management in case reports included clopidogrel, low-dose aspirin/dual antiplatelet therapy, atorvastatin, and antihypertensive therapy (amlodipine) | Used for peripheral arterial disease risk reduction/symptom stabilization rather than direct anti-calcification; one 2024 imaging case noted stabilization while on this regimen after NIH bisphosphonate enrollment (mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4) | Mandalapu & Stevens, 2024 (mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4) |
| Therapy | Supportive monitoring and functional assessment | Trial/clinical follow-up included CT imaging, ABI, treadmill testing (Gardner protocol), pain and activity indices, blood/urine tests, dental exams, and hand radiographs | Supports longitudinal monitoring of progression and treatment tolerance in this chronic ultra-rare disease; current care remains largely supportive and individualized outside the etidronate pilot (ferrante2024pilotstudyto pages 1-3, ferrante2024pilotstudyto pages 3-4, NCT01585402 chunk 2) | Ferrante et al., 2024; NCT01585402 (ferrante2024pilotstudyto pages 1-3, ferrante2024pilotstudyto pages 3-4, NCT01585402 chunk 2) |


*Table: This table summarizes the main clinical diagnostic modalities and current management evidence for CALJA/ACDC, emphasizing how the disease is recognized in practice and what treatment approaches have supporting data. It is useful for translating case reports and the 2024 pilot study into a structured knowledge base format.*

### 10.1 Imaging hallmarks (visual evidence)
Radiology figures from the 2024 case report demonstrate representative patterns of **dense popliteal/femoral arterial calcification and tortuosity** plus **periarticular hand calcifications**, consistent with the core phenotype. (mandalapu2024imagingfindingsof media 377fe2eb, mandalapu2024imagingfindingsof media 00a5cd92, mandalapu2024imagingfindingsof media a1258f08)

### 10.2 Differential diagnosis
Differential diagnoses highlighted in the 2024 imaging case include pseudoxanthoma elasticum, generalized arterial calcification of infancy, chronic renal failure/secondary hyperparathyroidism, gout, and scleroderma, with dual-energy CT used to exclude urate. (mandalapu2024imagingfindingsof pages 1-2, mandalapu2024imagingfindingsof pages 2-4)

### 10.3 Genetic testing approach (implementation)
Diagnosis is confirmed by identification of pathogenic **NT5E** variants; recent literature supports the utility of systematic NGS panel approaches for overlapping vascular calcification phenotypes (including NT5E and related genes such as ENPP1 and ABCC6). (maffi2023calcificationofjoints pages 1-2)

## 11. Outcome / prognosis
- Prognosis remains incompletely defined due to rarity. Severe morbidity can result from progressive lower-extremity arterial occlusion and debilitating joint pain. (ferrante2024pilotstudyto pages 6-8, ferrante2024pilotstudyto pages 1-3)
- Quantitative survival or life-expectancy statistics were not available in the retrieved disease-specific evidence.

## 12. Treatment
### 12.1 Targeted / disease-modifying evidence: etidronate
**NIH pilot study (Vascular Medicine, Apr 2024; DOI: https://doi.org/10.1177/1358863X241235669; publication date Apr 2024):**
- Seven adults with genetically confirmed ACDC received intermittent etidronate (14 days every 3 months for 3 years). (ferrante2024pilotstudyto pages 3-4)
- Primary endpoints included lower-extremity CT calcium score and ABI; authors conclude etidronate “appeared to have slowed the progression of further vascular calcification” but did not reverse existing vascular or periarticular calcifications; it was “safe and well tolerated.” (ferrante2024pilotstudyto pages 1-3)
- Additional reported quantitative context includes coronary Agatston scores (mean prestudy 183 ± 43; posttreatment 226 ± 84) in the cohort description. (ferrante2024pilotstudyto pages 6-8)

**Trial registration:** ClinicalTrials.gov **NCT01585402** (interventional; completed; enrollment 7; Phase 2). URL: https://clinicaltrials.gov/study/NCT01585402 (NCT01585402 chunk 2)

### 12.2 Symptom-directed and supportive management (real-world)
- **Colchicine:** in a CALJA case with persistent inflammatory marker elevation, colchicine “ameliorated articular symptoms and normalized inflammatory markers,” but claudication was unaffected. (maffi2023calcificationofjoints pages 1-2)
- **NSAIDs:** reported effective for acute joint flares in a rheumatology case report. (ichikawa2015arterialcalcificationdue pages 1-1)
- **Revascularization surgery:** femoral-to-posterior tibial bypass improved symptoms in a severe case (evidence of advanced PAD management). (markello2011vascularpathologyof pages 2-4)
- **Antiplatelet/statin/vascular risk management:** used in case-based management; a 2024 imaging case described stabilization with medical therapy and NIH trial participation. (mandalapu2024imagingfindingsof pages 1-2)

### Suggested MAXO terms (examples)
- Etidronate therapy (bisphosphonate therapy)
- Antiplatelet therapy
- Vascular bypass surgery
- Colchicine therapy
- Nonsteroidal anti-inflammatory drug therapy

(MAXO identifiers were not present in the retrieved evidence; these are mapping suggestions for knowledge base use.)

## 13. Prevention
No primary prevention is established beyond:
- **Genetic counseling** (autosomal recessive inheritance; cascade testing where a familial NT5E variant is known). (hilaire2011nt5emutationsandarterial pages 5-6)
- **Secondary/tertiary prevention:** early recognition of the distinctive imaging pattern and ABI impairment to avoid misdiagnosis and inappropriate immunosuppression, and to implement vascular surveillance and symptom management. (maffi2023calcificationofjoints pages 1-2, mandalapu2024imagingfindingsof pages 1-2)

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were identified in the retrieved evidence.

## 15. Model organisms
### 15.1 Mouse model (Nt5e/CD73 deficiency)
A key model is the **Nt5e−/− (CD73-deficient) mouse** (Nt5e^tm1Jgsc). These mice develop **juxta-articular/joint-capsule mineralization** and show biochemical shifts consistent with a pro-mineralization state (increased serum Pi, decreased plasma PPi, increased Pi/PPi ratio), but **lack overt vascular mineralization**, indicating partial phenotypic recapitulation and important species/model limitations. (li2014juxtaarticularjointcapsulemineralization pages 1-3, li2014juxtaarticularjointcapsulemineralization pages 4-5)

### 15.2 Model limitations and implications
Species/model differences (including adenosine metabolism differences and tissue microenvironment differences) likely contribute to the absent vascular phenotype in mice, as emphasized in expert review. (joolharzadeh2019cd73(clusterof pages 3-4)

## Recent developments and authoritative expert perspectives (2023–2024 emphasis)
- **2023:** CALJA case report/review emphasizes frequent rheumatologic misdiagnosis, limited treatment options, and case-based response to colchicine in an inflammatory phenotype; it reiterates rarity (“Only 23 cases have been described so far.”). URL: https://doi.org/10.1007/s42399-023-01485-1 (published May 2023). (maffi2023calcificationofjoints pages 1-2)
- **2024:** NIH pilot trial reports safety and signals of slowed vascular calcification progression with etidronate, providing the strongest prospective human interventional evidence to date. URL: https://doi.org/10.1177/1358863X241235669 (published Apr 2024). (ferrante2024pilotstudyto pages 1-3, ferrante2024pilotstudyto pages 6-8)
- **2024:** A mechanistic review frames CALJA/NT5E within a broader “purinergic disease” continuum (ABCC6→ENPP1→CD73→TNAP) linking PPi and adenosine as dual anti-calcification factors. URL: https://doi.org/10.3390/biology13020074 (published Jan 2024). (kauffenstein2024thepurinergicnature pages 1-2)

## Key gaps (evidence not found in retrieved sources)
- Orphanet/ICD-10/ICD-11/MeSH identifiers.
- Robust prevalence/incidence estimates beyond case counts and rough prevalence assertions.
- Systematic variant-level population frequencies (gnomAD) and ClinVar classifications.
- Standardized clinical diagnostic criteria and validated QoL instruments.
- Long-term survival/mortality statistics.

## References (URLs and dates where available)
- St Hilaire et al. “NT5E mutations and arterial calcifications.” *NEJM* (Feb 2011). DOI/URL: https://doi.org/10.1056/NEJMoa0912923 (hilaire2011nt5emutationsandarterial pages 1-2)
- Ferrante et al. “Pilot study … etidronate … ACDC.” *Vascular Medicine* (Apr 2024). DOI/URL: https://doi.org/10.1177/1358863X241235669 (ferrante2024pilotstudyto pages 1-3)
- ClinicalTrials.gov NCT01585402 (posted 2012; completed). URL: https://clinicaltrials.gov/study/NCT01585402 (NCT01585402 chunk 2)
- Maffi et al. “Calcification of joints and arteries (CALJA) … case report and literature review.” *SN Comprehensive Clinical Medicine* (May 2023). DOI/URL: https://doi.org/10.1007/s42399-023-01485-1 (maffi2023calcificationofjoints pages 1-2)
- Mandalapu & Stevens. “Imaging findings … ACDC: A case study.” *Journal of Radiology Case Reports* (Feb 2024). DOI/URL: https://doi.org/10.3941/jrcr.v17i12.5175 (mandalapu2024imagingfindingsof pages 1-2)
- Li et al. “Juxta-articular joint-capsule mineralization in CD73 deficient mice …” *Cell Cycle* (Aug 2014). DOI/URL: https://doi.org/10.4161/15384101.2014.943567 (li2014juxtaarticularjointcapsulemineralization pages 1-3)
- Kauffenstein et al. “The purinergic nature of pseudoxanthoma elasticum.” *Biology* (Jan 2024). DOI/URL: https://doi.org/10.3390/biology13020074 (kauffenstein2024thepurinergicnature pages 1-2)


References

1. (ferrante2024pilotstudyto pages 1-3): Elisa A Ferrante, Cornelia D Cudrici, Mahmood Rashidi, Yi-Ping Fu, Rebecca Huffstutler, Katherine Carney, Marcus Y Chen, Cynthia St Hilaire, Kevin Smith, Hadi Bagheri, James D Katz, Carlos R Ferreira, William A Gahl, Manfred Boehm, and Alessandra Brofferio. Pilot study to evaluate the safety and effectiveness of etidronate treatment for arterial calcification due to deficiency of cd73 (acdc). Vascular Medicine, 29:245-255, Apr 2024. URL: https://doi.org/10.1177/1358863x241235669, doi:10.1177/1358863x241235669. This article has 13 citations and is from a peer-reviewed journal.

2. (maffi2023calcificationofjoints pages 1-2): Michele Maffi, Giammarco De Mattia, Maria Rosa Mazzoni, Angela Michelucci, Benedetta Toschi, Caligo Maria Adelaide, Marta Mosca, and Maurizio Mazzantini. Calcification of joints and arteries (calja) is a rare cause of arthritis and lower limb ischemia: case report and literature review. SN Comprehensive Clinical Medicine, 5:1-8, May 2023. URL: https://doi.org/10.1007/s42399-023-01485-1, doi:10.1007/s42399-023-01485-1. This article has 2 citations and is from a peer-reviewed journal.

3. (maffi2023calcificationofjoints pages 6-7): Michele Maffi, Giammarco De Mattia, Maria Rosa Mazzoni, Angela Michelucci, Benedetta Toschi, Caligo Maria Adelaide, Marta Mosca, and Maurizio Mazzantini. Calcification of joints and arteries (calja) is a rare cause of arthritis and lower limb ischemia: case report and literature review. SN Comprehensive Clinical Medicine, 5:1-8, May 2023. URL: https://doi.org/10.1007/s42399-023-01485-1, doi:10.1007/s42399-023-01485-1. This article has 2 citations and is from a peer-reviewed journal.

4. (hilaire2011nt5emutationsandarterial pages 1-2): Cynthia St. Hilaire, Shira G. Ziegler, Thomas C. Markello, Alfredo Brusco, Catherine Groden, Fred Gill, Hannah Carlson-Donohoe, Robert J. Lederman, Marcus Y. Chen, Dan Yang, Michael P. Siegenthaler, Carlo Arduino, Cecilia Mancini, Bernard Freudenthal, Horia C. Stanescu, Anselm A. Zdebik, R. Krishna Chaganti, Robert L. Nussbaum, Robert Kleta, William A. Gahl, and Manfred Boehm. <i>nt5e</i>mutations and arterial calcifications. New England Journal of Medicine, 364:432-442, Feb 2011. URL: https://doi.org/10.1056/nejmoa0912923, doi:10.1056/nejmoa0912923. This article has 531 citations and is from a highest quality peer-reviewed journal.

5. (hilaire2011nt5emutationsandarterial pages 5-6): Cynthia St. Hilaire, Shira G. Ziegler, Thomas C. Markello, Alfredo Brusco, Catherine Groden, Fred Gill, Hannah Carlson-Donohoe, Robert J. Lederman, Marcus Y. Chen, Dan Yang, Michael P. Siegenthaler, Carlo Arduino, Cecilia Mancini, Bernard Freudenthal, Horia C. Stanescu, Anselm A. Zdebik, R. Krishna Chaganti, Robert L. Nussbaum, Robert Kleta, William A. Gahl, and Manfred Boehm. <i>nt5e</i>mutations and arterial calcifications. New England Journal of Medicine, 364:432-442, Feb 2011. URL: https://doi.org/10.1056/nejmoa0912923, doi:10.1056/nejmoa0912923. This article has 531 citations and is from a highest quality peer-reviewed journal.

6. (markello2011vascularpathologyof pages 2-4): Thomas C. Markello, Laura K. Pak, Cynthia St. Hilaire, Heidi Dorward, Shira G. Ziegler, Marcus Y. Chen, Krishna Chaganti, Robert L. Nussbaum, Manfred Boehm, and William A. Gahl. Vascular pathology of medial arterial calcifications in nt5e deficiency: implications for the role of adenosine in pseudoxanthoma elasticum. Molecular genetics and metabolism, 103 1:44-50, May 2011. URL: https://doi.org/10.1016/j.ymgme.2011.01.018, doi:10.1016/j.ymgme.2011.01.018. This article has 134 citations and is from a peer-reviewed journal.

7. (maffi2023calcificationofjoints pages 2-5): Michele Maffi, Giammarco De Mattia, Maria Rosa Mazzoni, Angela Michelucci, Benedetta Toschi, Caligo Maria Adelaide, Marta Mosca, and Maurizio Mazzantini. Calcification of joints and arteries (calja) is a rare cause of arthritis and lower limb ischemia: case report and literature review. SN Comprehensive Clinical Medicine, 5:1-8, May 2023. URL: https://doi.org/10.1007/s42399-023-01485-1, doi:10.1007/s42399-023-01485-1. This article has 2 citations and is from a peer-reviewed journal.

8. (mandalapu2024imagingfindingsof pages 1-2): Aniruddh Mandalapu and Kathryn J Stevens. Imaging findings of arterial calcification due to deficiency of cd73: a case study. Journal of Radiology Case Reports, 17:27-33, Feb 2024. URL: https://doi.org/10.3941/jrcr.v17i12.5175, doi:10.3941/jrcr.v17i12.5175. This article has 1 citations.

9. (NCT01585402 chunk 2):  Etidronate for Arterial Calcifications Due to Deficiency in CD73 (ACDC). National Heart, Lung, and Blood Institute (NHLBI). 2012. ClinicalTrials.gov Identifier: NCT01585402

10. (ferrante2024pilotstudyto pages 6-8): Elisa A Ferrante, Cornelia D Cudrici, Mahmood Rashidi, Yi-Ping Fu, Rebecca Huffstutler, Katherine Carney, Marcus Y Chen, Cynthia St Hilaire, Kevin Smith, Hadi Bagheri, James D Katz, Carlos R Ferreira, William A Gahl, Manfred Boehm, and Alessandra Brofferio. Pilot study to evaluate the safety and effectiveness of etidronate treatment for arterial calcification due to deficiency of cd73 (acdc). Vascular Medicine, 29:245-255, Apr 2024. URL: https://doi.org/10.1177/1358863x241235669, doi:10.1177/1358863x241235669. This article has 13 citations and is from a peer-reviewed journal.

11. (li2014juxtaarticularjointcapsulemineralization pages 1-3): Qiaoli Li, Thea P Price, John P Sundberg, and Jouni Uitto. Juxta-articular joint-capsule mineralization in cd73 deficient mice: similarities to patients with nt5e mutations. Cell Cycle, 13:2609-2615, Aug 2014. URL: https://doi.org/10.4161/15384101.2014.943567, doi:10.4161/15384101.2014.943567. This article has 64 citations and is from a peer-reviewed journal.

12. (hilaire2011nt5emutationsandarterial pages 8-10): Cynthia St. Hilaire, Shira G. Ziegler, Thomas C. Markello, Alfredo Brusco, Catherine Groden, Fred Gill, Hannah Carlson-Donohoe, Robert J. Lederman, Marcus Y. Chen, Dan Yang, Michael P. Siegenthaler, Carlo Arduino, Cecilia Mancini, Bernard Freudenthal, Horia C. Stanescu, Anselm A. Zdebik, R. Krishna Chaganti, Robert L. Nussbaum, Robert Kleta, William A. Gahl, and Manfred Boehm. <i>nt5e</i>mutations and arterial calcifications. New England Journal of Medicine, 364:432-442, Feb 2011. URL: https://doi.org/10.1056/nejmoa0912923, doi:10.1056/nejmoa0912923. This article has 531 citations and is from a highest quality peer-reviewed journal.

13. (kauffenstein2024thepurinergicnature pages 1-2): Gilles Kauffenstein, Ludovic Martin, and Olivier Le Saux. The purinergic nature of pseudoxanthoma elasticum. Biology, Jan 2024. URL: https://doi.org/10.3390/biology13020074, doi:10.3390/biology13020074. This article has 8 citations.

14. (hilaire2011nt5emutationsandarterial pages 10-11): Cynthia St. Hilaire, Shira G. Ziegler, Thomas C. Markello, Alfredo Brusco, Catherine Groden, Fred Gill, Hannah Carlson-Donohoe, Robert J. Lederman, Marcus Y. Chen, Dan Yang, Michael P. Siegenthaler, Carlo Arduino, Cecilia Mancini, Bernard Freudenthal, Horia C. Stanescu, Anselm A. Zdebik, R. Krishna Chaganti, Robert L. Nussbaum, Robert Kleta, William A. Gahl, and Manfred Boehm. <i>nt5e</i>mutations and arterial calcifications. New England Journal of Medicine, 364:432-442, Feb 2011. URL: https://doi.org/10.1056/nejmoa0912923, doi:10.1056/nejmoa0912923. This article has 531 citations and is from a highest quality peer-reviewed journal.

15. (villabellosta2024vascularcalcificationa pages 1-2): Ricardo Villa-Bellosta. Vascular calcification: a passive process that requires active inhibition. Biology, 13:111, Feb 2024. URL: https://doi.org/10.3390/biology13020111, doi:10.3390/biology13020111. This article has 29 citations.

16. (villabellosta2024vascularcalcificationa pages 6-7): Ricardo Villa-Bellosta. Vascular calcification: a passive process that requires active inhibition. Biology, 13:111, Feb 2024. URL: https://doi.org/10.3390/biology13020111, doi:10.3390/biology13020111. This article has 29 citations.

17. (li2014juxtaarticularjointcapsulemineralization pages 3-4): Qiaoli Li, Thea P Price, John P Sundberg, and Jouni Uitto. Juxta-articular joint-capsule mineralization in cd73 deficient mice: similarities to patients with nt5e mutations. Cell Cycle, 13:2609-2615, Aug 2014. URL: https://doi.org/10.4161/15384101.2014.943567, doi:10.4161/15384101.2014.943567. This article has 64 citations and is from a peer-reviewed journal.

18. (li2014juxtaarticularjointcapsulemineralization pages 6-7): Qiaoli Li, Thea P Price, John P Sundberg, and Jouni Uitto. Juxta-articular joint-capsule mineralization in cd73 deficient mice: similarities to patients with nt5e mutations. Cell Cycle, 13:2609-2615, Aug 2014. URL: https://doi.org/10.4161/15384101.2014.943567, doi:10.4161/15384101.2014.943567. This article has 64 citations and is from a peer-reviewed journal.

19. (joolharzadeh2019cd73(clusterof pages 2-3): Pouya Joolharzadeh and Cynthia St. Hilaire. Cd73 (cluster of differentiation 73) and the differences between mice and humans. Arteriosclerosis, Thrombosis, & Vascular Biology, 39:339-348, Mar 2019. URL: https://doi.org/10.1161/atvbaha.118.311579, doi:10.1161/atvbaha.118.311579. This article has 60 citations and is from a domain leading peer-reviewed journal.

20. (ichikawa2015arterialcalcificationdue pages 1-1): Naomi Ichikawa, Atsuo Taniguchi, Hirotaka Kaneko, Manabu Kawamoto, Chieko Sekita, Ayako Nakajima, and Hisashi Yamanaka. Arterial calcification due to deficiency of cd73 (acdc) as one of rheumatic diseases associated with periarticular calcification. Journal of clinical rheumatology : practical reports on rheumatic & musculoskeletal diseases, 21 4:216-20, Jun 2015. URL: https://doi.org/10.1097/rhu.0000000000000245, doi:10.1097/rhu.0000000000000245. This article has 35 citations.

21. (maffi2023calcificationofjoints pages 5-6): Michele Maffi, Giammarco De Mattia, Maria Rosa Mazzoni, Angela Michelucci, Benedetta Toschi, Caligo Maria Adelaide, Marta Mosca, and Maurizio Mazzantini. Calcification of joints and arteries (calja) is a rare cause of arthritis and lower limb ischemia: case report and literature review. SN Comprehensive Clinical Medicine, 5:1-8, May 2023. URL: https://doi.org/10.1007/s42399-023-01485-1, doi:10.1007/s42399-023-01485-1. This article has 2 citations and is from a peer-reviewed journal.

22. (mandalapu2024imagingfindingsof pages 2-4): Aniruddh Mandalapu and Kathryn J Stevens. Imaging findings of arterial calcification due to deficiency of cd73: a case study. Journal of Radiology Case Reports, 17:27-33, Feb 2024. URL: https://doi.org/10.3941/jrcr.v17i12.5175, doi:10.3941/jrcr.v17i12.5175. This article has 1 citations.

23. (joolharzadeh2019cd73(clusterof pages 4-5): Pouya Joolharzadeh and Cynthia St. Hilaire. Cd73 (cluster of differentiation 73) and the differences between mice and humans. Arteriosclerosis, Thrombosis, & Vascular Biology, 39:339-348, Mar 2019. URL: https://doi.org/10.1161/atvbaha.118.311579, doi:10.1161/atvbaha.118.311579. This article has 60 citations and is from a domain leading peer-reviewed journal.

24. (mandalapu2024imagingfindingsof pages 4-6): Aniruddh Mandalapu and Kathryn J Stevens. Imaging findings of arterial calcification due to deficiency of cd73: a case study. Journal of Radiology Case Reports, 17:27-33, Feb 2024. URL: https://doi.org/10.3941/jrcr.v17i12.5175, doi:10.3941/jrcr.v17i12.5175. This article has 1 citations.

25. (hilaire2011nt5emutationsandarterial pages 7-8): Cynthia St. Hilaire, Shira G. Ziegler, Thomas C. Markello, Alfredo Brusco, Catherine Groden, Fred Gill, Hannah Carlson-Donohoe, Robert J. Lederman, Marcus Y. Chen, Dan Yang, Michael P. Siegenthaler, Carlo Arduino, Cecilia Mancini, Bernard Freudenthal, Horia C. Stanescu, Anselm A. Zdebik, R. Krishna Chaganti, Robert L. Nussbaum, Robert Kleta, William A. Gahl, and Manfred Boehm. <i>nt5e</i>mutations and arterial calcifications. New England Journal of Medicine, 364:432-442, Feb 2011. URL: https://doi.org/10.1056/nejmoa0912923, doi:10.1056/nejmoa0912923. This article has 531 citations and is from a highest quality peer-reviewed journal.

26. (ferrante2024pilotstudyto pages 3-4): Elisa A Ferrante, Cornelia D Cudrici, Mahmood Rashidi, Yi-Ping Fu, Rebecca Huffstutler, Katherine Carney, Marcus Y Chen, Cynthia St Hilaire, Kevin Smith, Hadi Bagheri, James D Katz, Carlos R Ferreira, William A Gahl, Manfred Boehm, and Alessandra Brofferio. Pilot study to evaluate the safety and effectiveness of etidronate treatment for arterial calcification due to deficiency of cd73 (acdc). Vascular Medicine, 29:245-255, Apr 2024. URL: https://doi.org/10.1177/1358863x241235669, doi:10.1177/1358863x241235669. This article has 13 citations and is from a peer-reviewed journal.

27. (mandalapu2024imagingfindingsof media 377fe2eb): Aniruddh Mandalapu and Kathryn J Stevens. Imaging findings of arterial calcification due to deficiency of cd73: a case study. Journal of Radiology Case Reports, 17:27-33, Feb 2024. URL: https://doi.org/10.3941/jrcr.v17i12.5175, doi:10.3941/jrcr.v17i12.5175. This article has 1 citations.

28. (mandalapu2024imagingfindingsof media 00a5cd92): Aniruddh Mandalapu and Kathryn J Stevens. Imaging findings of arterial calcification due to deficiency of cd73: a case study. Journal of Radiology Case Reports, 17:27-33, Feb 2024. URL: https://doi.org/10.3941/jrcr.v17i12.5175, doi:10.3941/jrcr.v17i12.5175. This article has 1 citations.

29. (mandalapu2024imagingfindingsof media a1258f08): Aniruddh Mandalapu and Kathryn J Stevens. Imaging findings of arterial calcification due to deficiency of cd73: a case study. Journal of Radiology Case Reports, 17:27-33, Feb 2024. URL: https://doi.org/10.3941/jrcr.v17i12.5175, doi:10.3941/jrcr.v17i12.5175. This article has 1 citations.

30. (li2014juxtaarticularjointcapsulemineralization pages 4-5): Qiaoli Li, Thea P Price, John P Sundberg, and Jouni Uitto. Juxta-articular joint-capsule mineralization in cd73 deficient mice: similarities to patients with nt5e mutations. Cell Cycle, 13:2609-2615, Aug 2014. URL: https://doi.org/10.4161/15384101.2014.943567, doi:10.4161/15384101.2014.943567. This article has 64 citations and is from a peer-reviewed journal.

31. (joolharzadeh2019cd73(clusterof pages 3-4): Pouya Joolharzadeh and Cynthia St. Hilaire. Cd73 (cluster of differentiation 73) and the differences between mice and humans. Arteriosclerosis, Thrombosis, & Vascular Biology, 39:339-348, Mar 2019. URL: https://doi.org/10.1161/atvbaha.118.311579, doi:10.1161/atvbaha.118.311579. This article has 60 citations and is from a domain leading peer-reviewed journal.