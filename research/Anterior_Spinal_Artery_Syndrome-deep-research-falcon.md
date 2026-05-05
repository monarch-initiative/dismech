---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T21:37:00.880533'
end_time: '2026-05-04T21:51:02.560809'
duration_seconds: 841.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Anterior Spinal Artery Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anterior Spinal Artery Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anterior Spinal Artery Syndrome** covering all of the
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
- **Disease Name:** Anterior Spinal Artery Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anterior Spinal Artery Syndrome** covering all of the
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


## Comprehensive Research Report: Anterior Spinal Artery Syndrome (ASAS)

### Executive summary
Anterior spinal artery syndrome (ASAS)—also called **anterior cord syndrome**—is the prototypical clinical syndrome caused by infarction/ischemia in the **anterior spinal artery (ASA) territory**, which supplies the anterior two‑thirds of the spinal cord (including anterior horn cells and corticospinal and spinothalamic tracts). It typically presents as a **hyperacute, often painful myelopathy** with **bilateral motor deficits**, **loss of pain/temperature** with relative **preservation of vibration/proprioception**, and frequent **autonomic dysfunction** (urinary retention/incontinence, bowel dysfunction, sexual dysfunction). (althobaiti2024anteriorspinalartery pages 1-3, althobaiti2024anteriorspinalartery pages 6-7, zedde2025spinalcordinfarction pages 2-4)

Across modern cohorts/reviews, spinal cord infarction (SCI) is rare and frequently under-recognized; epidemiologic estimates and coding granularity are limited. A key contemporary diagnostic signal is **time to nadir <12 hours**, plus **noncompressive MRI** and **non-inflammatory CSF** (for probable/definite spinal cord infarction classifications). (batsou2023spinalcordischemia pages 3-3, zedde2025spinalcordinfarction pages 2-4)

Recent real‑world implementation and research (2023–2024) are most active in the **aortic surgery/endovascular repair** setting, where protocols emphasizing **maintenance of spinal cord perfusion pressure** (MAP targets), **anemia correction (Hb targets)**, **staged repairs**, selective or routine **cerebrospinal fluid drainage (CSFD)**, and intensive neurologic monitoring can reduce persistent neurologic injury. (rosvall2024adedicatedpreventive pages 1-2, sufali2024resultsofa pages 1-3, torre2024enhancingneuroprotectionin pages 10-11)

---

## 1. Disease Information

### 1.1 What is the disease?
ASAS is a **clinical syndrome** reflecting ischemic injury in the vascular territory of the **anterior spinal artery**, usually due to **spinal cord infarction**. Reviews and case reports consistently frame ASAS as ischemia/obstruction of ASA supply to the anterior two‑thirds of the spinal cord; the tract-level anatomy explains the characteristic dissociation of modalities (motor and pain/temperature more affected than dorsal column modalities). (althobaiti2024anteriorspinalartery pages 1-3, zedde2025spinalcordinfarction pages 2-4)

**Direct abstract-supported definition (example, 2023 case literature):** Waack et al. state: “**Anterior cord syndrome (ACS) occurs as a result of ischemia in the territory of the anterior spinal artery (ASA)**,” and describe the typical presentation and tract correlates. https://doi.org/10.7759/cureus.40391 (published Jun 2023). (islam2021anteriorspinalartery pages 7-9)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
* **MONDO / Orphanet / OMIM:** In the retrieved primary literature set, formal MONDO/Orphanet/OMIM IDs were not provided, and ASAS is generally treated as a *syndrome/phenotype of vascular spinal cord infarction* rather than a monogenic disorder. (althobaiti2024anteriorspinalartery pages 1-3, zedde2025spinalcordinfarction pages 2-4)
* **ICD coding:** The retrieved corpus did not include a definitive ICD-10/ICD-11 code mapping for “anterior spinal artery syndrome” specifically; contemporary epidemiologic work tends to code at the level of “spinal cord infarction/ischemia” or related stroke/myelopathy categories rather than syndrome-specific labels. (althobaiti2024anteriorspinalartery pages 1-3)
* **MeSH:** The tool-retrieved content did not provide a direct MeSH descriptor ID for “anterior spinal artery syndrome.” (sliwa1992ischemicmyelopathya pages 1-2)

**Knowledge-base note:** For a practical knowledge base, ASAS is often represented under broader entities such as “spinal cord infarction,” with ASAS as a clinical presentation subtype. (zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 1-3)

### 1.3 Common synonyms and alternative names
Synonyms used in recent literature include:
* **Anterior cord syndrome** (explicitly: “ASAS, alternatively termed anterior cord syndrome”) (althobaiti2024anteriorspinalartery pages 6-7)
* **Anterior spinal cord infarction** and **spinal stroke** as closely related clinical terms used for the same vascular entity/presentation (althobaiti2024anteriorspinalartery pages 1-3)
* Related terms used in search strategies and case literature include **spinal cord infarct**, **spinal cord ischemia**, and ASA occlusion/dissection/compression language. (islam2021anteriorspinalartery pages 4-7)

### 1.4 Evidence source types
The ASAS evidence base is largely:
* **Aggregated disease-level resources**: narrative reviews and systematic reviews of spinal cord infarction/ischemia and aortic surgery complications (batsou2023spinalcordischemia pages 3-3, zedde2025spinalcordinfarction pages 2-4, torre2024enhancingneuroprotectionin pages 8-10)
* **Human clinical observational cohorts/series** (e.g., cohort distributions of SCI subtypes; post-aortic repair prevention protocols) (nagoshi2025imagingcharacteristicsclinical pages 5-8, rosvall2024adedicatedpreventive pages 1-2)
* **Case reports** (helpful for rare iatrogenic triggers and mimics) (althobaiti2024anteriorspinalartery pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
Causation is typically **vascular** (arterial occlusion, embolism, or hypoperfusion), leading to ischemic necrosis of the anterior spinal cord (gray matter and adjacent white matter). (zedde2025spinalcordinfarction pages 2-4, batsou2023spinalcordischemia pages 3-3)

### 2.2 Risk factors (human clinical)
Commonly reported etiologies/risk contexts include:
* **Aortic disease and aortic procedures** (open thoracoabdominal aortic surgery; endovascular repair/EVAR/TEVAR) (zedde2025spinalcordinfarction pages 2-4, rosvall2024adedicatedpreventive pages 1-2)
* **Systemic hypotension / low-flow states** (perioperative or spontaneous) (batsou2023spinalcordischemia pages 3-3, althobaiti2024anteriorspinalartery pages 6-7)
* **Embolic causes** (cardiac embolism; fibrocartilaginous embolism in some contexts) (althobaiti2024anteriorspinalartery pages 6-7, zedde2025spinalcordinfarction pages 2-4)
* **Vertebral artery dissection/occlusion and posterior circulation procedures causing cervical SCI via hypoperfusion/occlusion** (as a general SCI mechanism, relevant to ASA territory) (althobaiti2024anteriorspinalartery pages 6-7)
* **Neuraxial anesthesia/epidural procedures** as iatrogenic contributors in cohort data (nagoshi2025imagingcharacteristicsclinical pages 5-8)

**Quantitative vascular risk factor burden:** One review summarized that “one or more vascular risk factors” were present in **76%** of patients in one study, pooled “at least 1 vascular risk factor” in **81%**, and “at least 3” in **45.5%**. (batsou2023spinalcordischemia pages 1-2)

**Procedure-associated burden:** In a 19-patient Japanese cohort (2012–2022), **57.9%** of SCI cases were iatrogenic (post-cardiac surgery and epidural anesthesia). (nagoshi2025imagingcharacteristicsclinical pages 5-8)

### 2.3 Protective factors
Specific protective genetic or environmental factors for ASAS are not well-established in the retrieved literature. In the aortic-surgery context, “protective” measures are largely **procedural/perfusion optimization strategies** (see Prevention/Treatment sections). (rosvall2024adedicatedpreventive pages 1-2, sufali2024resultsofa pages 1-3)

### 2.4 Gene–environment interactions
No robust gene–environment interaction framework specific to ASAS was identified in the retrieved papers; however, vascular risk factors (smoking, hypertension, dyslipidemia, diabetes) interact with major environmental/iatrogenic triggers (aortic interventions, hypotension) to influence risk. (zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 6-7)

---

## 3. Phenotypes

### 3.1 Core phenotypes and suggested HPO terms
Typical clinical features (with suggested HPO mappings):
* **Acute paraparesis/paraplegia** → *Paraplegia* (HP:0003401), *Paraparesis* (HP:0001258)
* **Acute quadriparesis (cervical lesions)** → *Quadriparesis* (HP:0000749)
* **Loss of pain and temperature sensation** → *Impaired pain sensation* (HP:0007025), *Abnormality of temperature sensation* (HP:0004370)
* **Relative sparing of vibration/proprioception** (clinical dissociation; often described qualitatively) → consider annotating *Normal proprioception* (not standard HPO phenotype; document as “dorsal column sparing” clinical feature)
* **Autonomic dysfunction**: urinary retention/incontinence → *Urinary retention* (HP:0000016) / *Urinary incontinence* (HP:0000020); bowel dysfunction → *Constipation* (HP:0002019) or *Fecal incontinence* (HP:0002607)
* **Acute back/neck pain** → *Back pain* (HP:0003418), *Neck pain* (HP:0000467)

These features are repeatedly emphasized in contemporary case literature describing sudden pain and bilateral paralysis with pain/temperature loss and dorsal column sparing, plus autonomic symptoms. (althobaiti2024anteriorspinalartery pages 1-3, islam2021anteriorspinalartery pages 7-9)

### 3.2 Phenotype characteristics (onset, progression, frequency)
* **Temporal pattern:** Rapid progression to severe deficit is typical; diagnostic reviews emphasize **time to nadir <12 h** as a strong clinical predictor for spinal cord infarction diagnosis. (zedde2025spinalcordinfarction pages 2-4)
* **Quantitative time-to-nadir distribution (meta-analysis):** <6 h **56.1%**, 6–12 h **30.7%**, 12–72 h **5.4%**, >72 h **7.8%**. (batsou2023spinalcordischemia pages 3-3)
* **Frequency among SCI:** In one 19-case cohort, **12/19** presented with ASA syndrome. (nagoshi2025imagingcharacteristicsclinical pages 5-8)

### 3.3 Quality of life impact
ASAS frequently causes persistent gait impairment and autonomic dysfunction requiring prolonged rehabilitation and long-term support; functional outcomes often reflect initial severity. (batsou2023spinalcordischemia pages 3-3, nagoshi2025imagingcharacteristicsclinical pages 5-8)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
ASAS is **not typically a monogenic disorder**; it is a vascular syndrome. No causal gene list for ASAS exists in the retrieved primary sources. (zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 1-3)

### 4.2 Pathogenic variants / modifier genes
Specific inherited thrombophilias are occasionally reported in spinal cord ischemia case literature (outside the retrieved ASAS-focused core set), but within the evidence assembled here, thrombophilia and coagulopathy are treated as **risk contexts** rather than defining genetic causes. (althobaiti2024anteriorspinalartery pages 6-7)

### 4.3 Molecular pathways (inferred, not disease-specific omics)
Although ASAS lacks disease-specific omics studies in the retrieved set, ischemia-reperfusion biology implies involvement of:
* excitotoxicity, oxidative stress, neuroinflammation, endothelial dysfunction, and microvascular failure.
Aortic cross-clamp model review notes predominant **gray matter** (neuronal) injury and variable subsequent white matter injury, supporting selective anterior horn vulnerability. (awad2021histologicalfindingsafter pages 13-14)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle risk factors
The main “environmental” contributors are vascular risk behaviors and comorbidities (e.g., smoking, hypertension, dyslipidemia), plus iatrogenic exposures (aortic procedures, neuraxial anesthesia). A review reports smoking prevalence around **30%**, hypertension **40%**, dyslipidemia **29%**, diabetes **16%** among SCI cases in one synthesis. (zedde2025spinalcordinfarction pages 2-4)

### 5.2 Infectious agents
No specific infectious causal agent is established for ASAS in the retrieved evidence set. (zedde2025spinalcordinfarction pages 2-4)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (clinical mechanism)
1. **Trigger**: ASA occlusion, embolus, hypoperfusion (hypotension), or peri-aortic procedure collateral disruption. (batsou2023spinalcordischemia pages 3-3, zedde2025spinalcordinfarction pages 2-4)
2. **Primary lesion**: ischemia of ASA territory (anterior two‑thirds), especially metabolically vulnerable **gray matter/anterior horns**. (zedde2025spinalcordinfarction pages 2-4, awad2021histologicalfindingsafter pages 13-14)
3. **Clinical manifestation**: motor deficits (corticospinal/anterior horn), pain/temperature loss (spinothalamic), autonomic dysfunction (lateral horn/intermediolateral cell columns), with dorsal column sparing. (zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 1-3)

### 6.2 Tissue injury mechanisms
Preclinical aortic cross-clamp models show a conserved pattern: injury is “predominantly in the grey matter,” with anterior gray matter often worse, and white matter injury emerging later. (awad2021histologicalfindingsafter pages 13-14)

### 6.3 Suggested ontology terms
* **GO biological process**: *ischemic process*; *response to hypoxia*; *neuron death*; *inflammatory response*; *angiogenesis*.
* **CL cell types**: *spinal motor neuron*; *astrocyte*; *microglial cell*; *vascular endothelial cell*.
* **UBERON anatomy**: *spinal cord*; *anterior horn of spinal cord*; *thoracic spinal cord*; *conus medullaris*.

(These are mechanistically motivated; ontology IDs were not provided in the retrieved papers.)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary: **spinal cord** (central nervous system), particularly **anterior horn and anterior/lateral white matter** supplied by ASA. (zedde2025spinalcordinfarction pages 2-4)

### 7.2 Localization
Thoracolumbar involvement is common in SCI; one review notes ~65% thoracolumbar region involvement and that cervical infarctions may present more severely with autonomic dysfunction/upper extremity impairment. (zedde2025spinalcordinfarction pages 2-4)

---

## 8. Temporal Development

### 8.1 Onset
Usually **acute/hyperacute**. Diagnostic reviews emphasize severe deficits developing rapidly (within **<12 h**) as a core discriminant from inflammatory etiologies. (zedde2025spinalcordinfarction pages 2-4, batsou2023spinalcordischemia pages 3-3)

### 8.2 Progression
Symptoms often peak quickly (majority by 72 h), but imaging can lag: DWI may detect early lesions before T2 changes in some patients. In a cohort, DWI within 2 days detected lesions in **62.5% (5/8)**, and a representative case showed DWI positivity on day 2 and T2 changes by day 6. (nagoshi2025imagingcharacteristicsclinical pages 5-8)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
Robust epidemiology is limited; a 2025 review states incidence is “not well documented” and likely underestimated. (zedde2025spinalcordinfarction pages 2-4)

**Quantitative estimates (spinal cord infarction, not ASAS-specific):**
* SCI ~**1–2% of all strokes** and **5–8% of acute myelopathies**. (zedde2025spinalcordinfarction pages 2-4)
* Population incidence reported as **3.1/100,000 person-years** (95% CI 1.6–7.2) in one study cited in review. (zedde2025spinalcordinfarction pages 2-4)

### 9.2 Demographics
Vascular risk factors are common but not universal; one review cites **28%** with no reported vascular risk factors. (zedde2025spinalcordinfarction pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria and diagnostic approach
A contemporary review summarizes proposed diagnostic criteria for spinal cord infarction that are directly applicable to ASAS:
1) **Rapid development** of severe deficits within **12 h**;
2) MRI supportive of infarction and excluding compression;
3) **Non-inflammatory CSF**.
Patients may be categorized as definite/probable/possible SCI. (batsou2023spinalcordischemia pages 3-3)

Another contemporary review stresses that “lack of cord compression on MRI is the only mandatory feature” in proposed criteria, highlighting the need to exclude compressive myelopathy. (zedde2025spinalcordinfarction pages 2-4)

### 10.2 Imaging
MRI findings supporting ASAS include:
* axial **“owl’s eye” / “snake-eye”** anterior horn hyperintensity,
* sagittal **“pencil-like”** anterior T2 hyperintensity,
* **diffusion restriction** (DWI), and often **absence of early enhancement**. (batsou2023spinalcordischemia pages 1-2, althobaiti2024anteriorspinalartery pages 1-3)

**Image evidence:** A 2024 case report figure demonstrates ASA territory infarction with “owl’s eye/snake-eye” appearance on T2/DWI. (ferreira2024anteriorspinalcord media 08b84382)

---

## 11. Outcome / Prognosis

### 11.1 Functional outcomes
A review summarizes that **favorable functional outcome ~40–50%**, and “about half of initially non-ambulatory survivors regained walking.” (batsou2023spinalcordischemia pages 3-3)

In the 19-patient cohort, ASAS predicted poorer ambulatory outcomes: **11/13 (84.6%)** of the poor prognosis group had ASA syndrome, whereas Brown–Séquard presentations were associated with better gait outcomes. (nagoshi2025imagingcharacteristicsclinical pages 5-8)

### 11.2 Prognostic factors
Worse outcomes associate with more severe initial impairment (ASIA A/B), sensory level, and longitudinally extensive MRI lesions. (batsou2023spinalcordischemia pages 3-3)

---

## 12. Treatment

### 12.1 Acute and subacute medical management (evidence-limited)
There is no high-quality ASAS-specific randomized trial base; management is typically extrapolated from vascular neurology and the precipitating cause.

A 2023 review summarized treatment frequencies across series: **antiplatelet agents 68%**, **anticoagulation 8%**, **blood pressure augmentation 6%**, **lumbar drain 6%**; it also notes limited evidence and uncertainty, particularly for CSF drainage in *spontaneous* SCI. (batsou2023spinalcordischemia pages 3-3)

### 12.2 Aortic-repair associated prevention and management (2023–2024 real-world implementation)
The most protocolized “real‑world implementation” literature is peri‑aortic repair spinal cord protection.

**Protocol example (Frontiers in Cardiovascular Medicine, Aug 2024):** Rosvall et al. reported a prevention protocol for complex EVAR with targets **MAP >80 mmHg**, **Hb >110 g/L**, early lower limb reperfusion, and **hourly neurologic checks** for 36–72 h; prophylactic CSFD used selectively. SCI incidence was **1.3% (juxtarenal)** and **6.0% (TAAA)**; persistent SCI after regression was **0.6% (JRA)** and **4.0% (TAAA)**. https://doi.org/10.3389/fcvm.2024.1440674 (Aug 2024). (rosvall2024adedicatedpreventive pages 1-2)

**Protocol example (Vessel Plus, Jan 2024):** Sufali et al. reported a multidisciplinary prevention protocol for elective fenestrated/branched repairs with **staging in 80%**, **MAP >80 mmHg**, **Hb >10 g/dL**, routine CSFD, and neuromonitoring. Outcomes: overall SCI **8%** (2% transient; 6% permanent), permanent paraplegia **3%**, 30‑day mortality **3%**, in-hospital mortality **7%**, and worse 2‑year survival with SCI (**18% vs 69%**). https://doi.org/10.20517/2574-1209.2023.139 (Jan 2024). (sufali2024resultsofa pages 1-3)

**Expert synthesis (Anesthesia Research, Aug 2024):** Torre & Pirri summarize rescue management prioritizing perfusion: increase MAP (cited target **>100 mmHg**) and transfuse to **Hb >10 g/dL**, combined with CSFD; they cite neurologic improvement in **57%** of delayed deficits and complete resolution in **17%** in aggregated reports. https://doi.org/10.3390/anesthres1020010 (Aug 2024). (torre2024enhancingneuroprotectionin pages 10-11, torre2024enhancingneuroprotectionin pages 8-10)

### 12.3 Suggested MAXO terms (treatment actions)
* **Antiplatelet therapy**; **Anticoagulation therapy**; **Blood pressure augmentation**; **Cerebrospinal fluid drainage**; **Endovascular aortic repair management**; **Physical rehabilitation therapy**; **Bladder catheterization/management**.
(MAXO IDs not provided in retrieved papers; actions are supported as clinical interventions.) (batsou2023spinalcordischemia pages 3-3, rosvall2024adedicatedpreventive pages 1-2)

---

## 13. Prevention

Primary prevention is mainly **risk reduction for vascular events** and prevention of iatrogenic SCI in high-risk procedures.

**Aortic procedure prevention (real-world):** Staging extensive repairs, maintaining **MAP and Hb targets**, collateral bed optimization, neurologic monitoring, and selective/routine CSFD reduce persistent injury rates in modern series. (rosvall2024adedicatedpreventive pages 1-2, sufali2024resultsofa pages 1-3)

---

## 14. Other Species / Natural Disease
No naturally occurring ASAS “disease entity” in non-human species was identified in the retrieved evidence set; the translational literature primarily uses **induced ischemia models**. (awad2021histologicalfindingsafter pages 1-2)

---

## 15. Model Organisms

ASAS mechanisms (ischemic anterior spinal cord vulnerability) are modeled using **aortic cross-clamp** or **segmental artery ligation** paradigms (mimicking open repair or TEVAR) and **photochemical/photothrombotic** ischemia models.

### 15.1 TEVAR-like / segmental artery ligation model (mouse; 2023)
Kelani et al. (Anesthesiology, Jan 2023) ligated five pairs of thoracic intercostal arteries to model TEVAR-associated hypoperfusion.
* Spinal cord blood flow drop: thoracic spinal cord mean **−68.55%** (95% CI −80.23 to −56.87). 
* Day‑1 paralysis severity distribution: **9.4% severe**, **37.5% moderate**, **53.1% mild**.
* Severe paralysis mortality: **83% (15/18)** vs moderate **33%** and mild **24%**.
The authors state the model yields variable severity and reversibility resembling clinical variability after aortic repair. https://doi.org/10.1097/ALN.0000000000004515 (Jan 2023). (kelani2023mousemodelof pages 1-3)

### 15.2 Aortic cross-clamp delayed paralysis model (mouse; 2010)
Awad et al. (Anesthesiology, Oct 2010) developed a murine descending aortic cross-clamp model producing **delayed paralysis (24–36 h)** with **>95% survival** through 9 weeks under an optimal protocol (7.5 min clamp at 33°C). It produced severe hindlimb paralysis in **70% (19/27)** and mild but permanent deficits in the remainder, enabling long-term mechanistic and therapy studies. https://doi.org/10.1097/ALN.0b013e3181ec61ee (Oct 2010). (awad2010amousemodel pages 1-2)

### 15.3 Simplified spinal cord ischemia model (mouse; 2010)
Wang et al. (J Neurosci Methods, Jun 2010) reported clamp durations of 0–12 min with “approximately **90% blood flow reduction**” in lumbar spinal cord during cross-clamping; 10-min injury produced persistent deficits with 28‑day survival **80% (4/5)** in an injured group. https://doi.org/10.1016/j.jneumeth.2010.04.003 (Jun 2010). (wang2010developmentofa pages 1-2)

### 15.4 Histopathology across species (systematic review; 2021)
A systematic review of aortic cross-clamp models concluded injury is predominantly **gray matter**, with neuronal degeneration in over two‑thirds of cases and anterior gray matter often worse—consistent with anterior horn vulnerability central to ASAS. https://doi.org/10.1093/jnen/nlab084 (Sep 2021). (awad2021histologicalfindingsafter pages 13-14)

---

## Recent developments & latest research emphasis (2023–2024)
Key 2023–2024 advances in this corpus are pragmatic rather than molecular:
1. **Refined diagnostic frameworks** emphasizing *time to nadir*, MRI exclusion of compression, and non-inflammatory CSF. (batsou2023spinalcordischemia pages 3-3)
2. **More explicit reporting of DWI utility and radiologic lag**, including cohort-level estimates and early DWI detection fractions. (nagoshi2025imagingcharacteristicsclinical pages 5-8)
3. **Protocolized spinal cord protection bundles** for complex EVAR/branched repairs with specific physiologic targets (MAP/Hb), staging, and neurologic monitoring, with measured reductions in persistent SCI and documentation of risk strata (sex, rupture, renal insufficiency, low MAP). (rosvall2024adedicatedpreventive pages 1-2, sufali2024resultsofa pages 1-3)
4. **Translational TEVAR-like murine models (2023)** enabling mechanistic study of collateral variability and tissue injury patterns that resemble human TEVAR-related spinal cord injury heterogeneity. (kelani2023mousemodelof pages 1-3)

---

## Current applications and real-world implementations
* **ICU protocols after complex aortic repair** with hourly neurological checks (36–72 h), MAP and hemoglobin targets, early limb reperfusion, and selective CSF drainage are real-world implementations aimed at reducing permanent neurologic injury. (rosvall2024adedicatedpreventive pages 1-2)
* **Multidisciplinary prevention pathways** integrating vascular surgery, anesthesiology, neuromonitoring, and neuroimaging for early detection and rescue. (sufali2024resultsofa pages 1-3, torre2024enhancingneuroprotectionin pages 10-11)

---

## Expert opinions / analysis (authoritative sources)
Authoritative review analyses emphasize that SCI/ASAS remains underdiagnosed and lacks strong epidemiology; many cases are misdiagnosed as inflammatory myelopathies, and diagnostic pathways are often incomplete. (zedde2025spinalcordinfarction pages 2-4)

Aortic-surgery neuroprotection reviews stress a physiology-based principle: spinal cord perfusion pressure is approximated by **MAP minus CSF pressure**, motivating CSFD and permissive hypertension/anemia correction as rescue strategies. (torre2024enhancingneuroprotectionin pages 8-10)

---

## Statistics and data highlights
* SCI population incidence: **3.1/100,000 person-years** (review-cited estimate). (zedde2025spinalcordinfarction pages 2-4)
* Time to nadir distribution: <6 h **56.1%**, 6–12 h **30.7%** (meta-analysis). (batsou2023spinalcordischemia pages 3-3)
* ASA syndrome frequency in a cohort: **12/19** cases. (nagoshi2025imagingcharacteristicsclinical pages 5-8)
* Complex EVAR protocol outcomes (Aug 2024): SCI **1.3%** (JRA) and **6.0%** (TAAA); persistent SCI **0.6%** and **4.0%** after regression. (rosvall2024adedicatedpreventive pages 1-2)
* F/B‑EVAR protocol outcomes (Jan 2024): overall SCI **8%**, permanent paraplegia **3%**. (sufali2024resultsofa pages 1-3)

---

## Visual evidence
The following MRI figure demonstrates classic ASA-territory infarction imaging (including the “owl’s eye/snake-eye” sign) supportive of ASAS diagnosis. (ferreira2024anteriorspinalcord media 08b84382)

---

## Synthesis artifact
| Domain | Key points | Quantitative data | Evidence type | Primary citations |
|---|---|---|---|---|
| Definition / disease concept | Anterior spinal artery syndrome (ASAS; anterior cord syndrome) is the commonest arterial spinal cord infarction phenotype, caused by ischemia in the ASA territory supplying the anterior two-thirds of the cord; classically affects corticospinal tracts, anterior horns, spinothalamic tracts, and autonomic pathways. | Spinal cord infarction accounts for ~0.3%–2% of strokes/CNS infarctions; ASAS reported as the predominant pattern, up to 87.2% in one review of spinal cord infarction literature. | Review, systematic review, case report | (islam2021anteriorspinalartery pages 4-7, zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 1-3) |
| Core clinical phenotype | Typical syndrome: sudden back/neck/chest pain followed by bilateral leg-predominant weakness or paralysis, loss of pain/temperature sensation with relative sparing of vibration/proprioception, and bladder/bowel/sexual dysfunction; incomplete variants occur. | In disc-related ASAS review: motor weakness 100%, quadriparesis 67%, paraparesis 33%, pain 60%, bowel/bladder disturbance 25%; in one recent cohort, ASA syndrome occurred in 12/19 spinal cord infarction cases. | Systematic review, cohort, case report | (islam2021anteriorspinalartery pages 7-9, islam2021anteriorspinalartery pages 4-7, nagoshi2025imagingcharacteristicsclinical pages 5-8, althobaiti2024anteriorspinalartery pages 1-3) |
| Symptom tempo / onset | Hyperacute onset is a major clue; severe deficits usually reach nadir within hours rather than days, helping distinguish ischemia from inflammatory myelitis. | Meta-analysis: time to nadir <6 h in 56.1%, 6–12 h in 30.7%, 12–72 h in 5.4%, >72 h in 7.8%; proposed strongest diagnostic variable is time to nadir of severe deficits <12 h. | Meta-analysis, review | (batsou2023spinalcordischemia pages 3-3, zedde2025spinalcordinfarction pages 2-4) |
| Etiologies / risk factors | Major causes include aortic surgery/EVAR/TEVAR, aortic dissection/aneurysm, systemic hypotension/low-flow states, embolism, atherosclerosis, vertebral artery disease/dissection, epidural/spinal anesthesia, fibrocartilaginous embolism from disc disease, vasculitis, AVM, coagulopathy/hypercoagulability, and procedure-related vasospasm/arterial injury. | In one recent 19-patient cohort, 57.9% were iatrogenic (8 post-cardiovascular surgery, 3 after epidural anesthesia); vascular risk factors reported in 76%–81% across series/reviews; 28% had no vascular risk factors in one review. | Review, cohort, case report, systematic review | (batsou2023spinalcordischemia pages 1-2, islam2021anteriorspinalartery pages 4-7, althobaiti2024anteriorspinalartery pages 6-7, nagoshi2025imagingcharacteristicsclinical pages 5-8, zedde2025spinalcordinfarction pages 2-4) |
| Population epidemiology | ASAS is rare and likely under-recognized; incidence/prevalence are difficult to estimate because many cases are coded under spinal cord infarction or ischemia rather than a syndrome label. | Population incidence for spinal cord infarction reported as 3.1/100,000 person-years (95% CI 1.6–7.2); spinal cord infarction estimated at 1%–2% of all strokes and 5%–8% of acute myelopathies. | Review | (zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 1-3) |
| Imaging hallmarks | MRI is the preferred confirmatory test. Characteristic findings include longitudinal anterior/ventral T2 hyperintensity (“pencil-like”), axial bilateral anterior horn hyperintensity (“owl’s eye”/“snake-eye”), diffusion restriction on DWI, and usually no acute contrast enhancement. Early MRI may be negative, so repeat imaging can be necessary. | T2/DWI diagnostic signs reported in 40.5%–100% across reviews; in one cohort, early DWI within 2 days was positive in 5/8 (62.5%); MRI consistent with ASA-distribution ischemia in 83% of disc-related ASAS cases. | Review, cohort, case report, systematic review | (batsou2023spinalcordischemia pages 1-2, islam2021anteriorspinalartery pages 4-7, nagoshi2025imagingcharacteristicsclinical pages 5-8, althobaiti2024anteriorspinalartery pages 1-3, ferreira2024anteriorspinalcord media 08b84382) |
| Diagnostic clues / criteria | Diagnosis is clinical-radiologic: acute noncompressive myelopathy, rapid severe deficit evolution, supportive MRI, and exclusion of inflammatory/infectious/compressive mimics. Proposed criteria emphasize rapid development within 12 h, MRI supporting infarction and excluding compression, and non-inflammatory CSF. | Proposed criteria components: severe deficits within 12 h + MRI support/noncompression + non-inflammatory CSF; lack of cord compression is considered the only mandatory MRI feature in one recent review. | Review | (batsou2023spinalcordischemia pages 3-3, zedde2025spinalcordinfarction pages 2-4) |
| Differential diagnosis | Main mimics include transverse myelitis, NMOSD/MOGAD, compressive myelopathy, hemorrhage, tumor, infection, and functional/other acute myelopathies. Absence of enhancement early, very rapid nadir, and non-inflammatory CSF favor infarction. | Not reliably quantified; one review notes many cases are misdiagnosed as acute/subacute myelopathies. | Review, case report | (althobaiti2024anteriorspinalartery pages 6-7, zedde2025spinalcordinfarction pages 2-4, althobaiti2024anteriorspinalartery pages 1-3) |
| Prognosis / functional outcome | Outcomes are highly variable and depend on initial severity, vascular territory, and lesion extent. ASA syndrome generally predicts poorer gait recovery than Brown-Séquard or incomplete syndromes. | Favorable functional outcome reported in ~40%–50%; about half of initially non-ambulatory survivors regained walking; in one 19-patient cohort, poor prognosis group contained 11/13 (84.6%) ASA syndrome cases; in disc-related ASAS, conservative management yielded 40% complete recovery vs 100% after decompression in selected cases. | Review, cohort, systematic review | (islam2021anteriorspinalartery pages 7-9, batsou2023spinalcordischemia pages 3-3, nagoshi2025imagingcharacteristicsclinical pages 5-8) |
| Prognostic factors | Worse outcome is linked to more severe initial impairment, complete deficits, sensory level, longitudinally extensive lesions, and larger perfusion-territory involvement; older age and delayed diagnosis also appear unfavorable. | Predictors of poor outcome reported: ASIA A/B, absent Babinski, sensory level, longitudinally extensive lesions; Brown-Séquard syndrome associated with good prognosis in 5/6 patients in one cohort. | Review, cohort | (batsou2023spinalcordischemia pages 3-3, nagoshi2025imagingcharacteristicsclinical pages 5-8, zedde2025spinalcordinfarction pages 2-4) |
| Acute medical treatment | No ASAS-specific randomized treatment standard exists; management is typically extrapolated from spinal cord infarction and underlying cause. Common approaches include antiplatelet therapy, selected anticoagulation, optimization of perfusion/oxygen delivery, treatment of the precipitating vascular cause, bladder care, and early rehabilitation. Steroids are generally not beneficial for ischemic cord injury unless another diagnosis is being treated. | Review-level treatment frequencies: antiplatelet agents 68%, anticoagulation 8%, blood-pressure augmentation 6%, lumbar drain 6%; one case used aspirin plus statin and rehab. | Review, case report | (batsou2023spinalcordischemia pages 3-3, althobaiti2024anteriorspinalartery pages 6-7) |
| Surgical / interventional treatment | When ASAS is due to reversible mechanical or vascular compromise (e.g., disc compression of ASA/radicular feeder, aortic repair-related hypoperfusion), decompression/revascularization or procedure-specific rescue may improve outcome if performed early. | In the disc-related ASAS review, 58% underwent surgery; all surgically managed patients regained fully functional status, with mean recovery ~23.25 days vs longest 90 days conservatively. | Systematic review | (islam2021anteriorspinalartery pages 7-9, islam2021anteriorspinalartery pages 4-7) |
| Rehabilitation / supportive care | Intensive inpatient neurorehabilitation, mobility training, spasticity management, bowel/bladder management, and long-term support are central because many survivors have chronic gait and autonomic deficits. | Long-term follow-up case series shows outcomes often remain poor but some patients return to work or regain strength over months to years; one recent case improved with intrathecal baclofen for delayed spasticity. | Case series, case report | (althobaiti2024anteriorspinalartery pages 6-7, islam2021anteriorspinalartery pages 7-9) |
| Aortic-surgery prevention protocols | Real-world protocols for preventing perioperative spinal cord ischemia emphasize staged extensive aortic repair, preservation/revascularization of collateral beds, early lower-limb reperfusion, selective or routine CSF drainage, close ICU neurologic checks, and maintenance of perfusion pressure and oxygen delivery. | Example 2024 protocols: MAP >80 mmHg and Hb >110 g/L with hourly neuro checks for 36–72 h after complex EVAR; another protocol used MAP >80 mmHg, Hb >10 g/dL, routine CSFD, staged repair in 80%, overall SCI 8% (2% transient, 6% permanent), paraplegia 3%. | Cohort, protocol study, review | (sufali2024resultsofa pages 1-3, rosvall2024adedicatedpreventive pages 1-2, sufali2024resultsofa pages 3-5) |
| Rescue management of delayed spinal cord ischemia | If neurologic deficits emerge after aortic repair, recommended rescue measures include urgent MAP augmentation, correction of anemia/hypovolemia, CSF drainage or more aggressive drainage targets, oxygenation optimization, rhythm/hemodynamic correction, and imaging to exclude compressive causes. | Review summaries cite MAP targets >100 mmHg in rescue settings, hemoglobin >10 g/dL, and neurologic improvement in 57% of delayed deficits with complete resolution in 17% after rescue strategies including CSF drainage. | Narrative review | (torre2024enhancingneuroprotectionin pages 10-11, torre2024enhancingneuroprotectionin pages 8-10) |
| CSF drainage details / controversies | CSF drainage lowers intrathecal pressure to improve spinal cord perfusion pressure but carries complications; practices vary between routine, selective prophylactic, and rescue-only use depending on procedure risk. | Selective-drain cohort: complications 9.6% overall, severe 0.74%, SCI 1.5% with prophylactic drainage vs 4.8% without; another 2024 complication series found no major drain complications and minor complications in 17.8%; systematic review in TBAD TEVAR found no reduction in permanent SCI (2.0% with vs 2.0% without prophylactic CSFD). | Cohort, systematic review, complication study | (krzyzaniak2024complicationsofcerebrospinal pages 1-2, rosvall2024adedicatedpreventive pages 2-3) |
| Monitoring / implementation | Adjuncts in high-risk aortic settings include MEP/SSEP monitoring, NIRS, and frequent bedside neuro exams; recent Delphi/guideline-style recommendations favor using CSF drainage plus at least one additional monitoring modality in major open TAAA and selected endovascular repairs. | Lumbar NIRS drop ≥30% from baseline correlated with permanent paraplegia in one review summary; ICU hourly neurologic examinations for 36–72 h used in 2024 endovascular protocols. | Narrative review, cohort | (torre2024enhancingneuroprotectionin pages 10-11, rosvall2024adedicatedpreventive pages 1-2) |


*Table: This table condenses recent and foundational evidence on anterior spinal artery syndrome, including presentation, causes, diagnostics, prognosis, and current treatment/prevention strategies. It is designed as a quick-reference artifact for knowledge base curation and citation mapping.*

---

## Limitations of this report (evidence gaps relative to template)
* Formal **MONDO/MeSH/Orphanet/ICD** identifiers for ASAS were not found in the retrieved full-text excerpts and would require dedicated ontology lookups beyond the current paper set. (althobaiti2024anteriorspinalartery pages 1-3, sliwa1992ischemicmyelopathya pages 1-2)
* High-quality ASAS-specific randomized evidence for **antithrombotic selection** (antiplatelet vs anticoagulant) is limited; most recommendations are extrapolated from SCI series or the underlying etiology (e.g., aortic repair context). (batsou2023spinalcordischemia pages 3-3)

---

### Primary-source URLs (examples, with publication dates)
* Rosvall L, et al. *Front Cardiovasc Med*. **Aug 2024**. “A dedicated preventive protocol sustainably avoids spinal cord ischemia after endovascular aortic repair.” https://doi.org/10.3389/fcvm.2024.1440674 (rosvall2024adedicatedpreventive pages 1-2)
* Sufali G, et al. *Vessel Plus*. **Jan 2024**. “Results of a multidisciplinary spinal cord ischemia prevention protocol…” https://doi.org/10.20517/2574-1209.2023.139 (sufali2024resultsofa pages 1-3)
* Torre DE, Pirri C. *Anesthesia Research*. **Aug 2024**. “Enhancing Neuroprotection in Cardiac and Aortic Surgeries: A Narrative Review.” https://doi.org/10.3390/anesthres1020010 (torre2024enhancingneuroprotectionin pages 10-11)
* Kelani H, et al. *Anesthesiology*. **Jan 2023**. “Mouse Model of Spinal Cord Hypoperfusion…” https://doi.org/10.1097/aln.0000000000004515 (kelani2023mousemodelof pages 1-3)
* Zedde M, et al. *J Clin Med*. **Feb 2025**. “Spinal Cord Infarction: Clinical and Neuroradiological Clues…” https://doi.org/10.3390/jcm14041293 (zedde2025spinalcordinfarction pages 2-4)


References

1. (althobaiti2024anteriorspinalartery pages 1-3): Faisal A. Althobaiti, Rayan I. Maghrabi, Naif F Alharbi, Mohammed M Alwadai, Maha K Almatrafi, and Somaya Bajammal. Anterior spinal artery syndrome in a patient with multilevel cervical disc disease: a case report. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64577, doi:10.7759/cureus.64577. This article has 3 citations.

2. (althobaiti2024anteriorspinalartery pages 6-7): Faisal A. Althobaiti, Rayan I. Maghrabi, Naif F Alharbi, Mohammed M Alwadai, Maha K Almatrafi, and Somaya Bajammal. Anterior spinal artery syndrome in a patient with multilevel cervical disc disease: a case report. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64577, doi:10.7759/cureus.64577. This article has 3 citations.

3. (zedde2025spinalcordinfarction pages 2-4): Marialuisa Zedde, Arturo De Falco, Carla Zanferrari, Maria Guarino, Francesca Romana Pezzella, Shalom Haggiag, Gianni Cossu, Rocco Quatrale, Giuseppe Micieli, Massimo Del Sette, and Rosario Pascarella. Spinal cord infarction: clinical and neuroradiological clues of a rare stroke subtype. Journal of Clinical Medicine, 14:1293, Feb 2025. URL: https://doi.org/10.3390/jcm14041293, doi:10.3390/jcm14041293. This article has 16 citations.

4. (batsou2023spinalcordischemia pages 3-3): V Batsou, IS Benetos, and I Vlamis. Spinal cord ischemia: a review of clinical and imaging features, risk factors and long-term prognosis. Unknown journal, 2023.

5. (rosvall2024adedicatedpreventive pages 1-2): Lina Rosvall, Angelos Karelis, Björn Sonesson, and Nuno V. Dias. A dedicated preventive protocol sustainably avoids spinal cord ischemia after endovascular aortic repair. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1440674, doi:10.3389/fcvm.2024.1440674. This article has 8 citations and is from a peer-reviewed journal.

6. (sufali2024resultsofa pages 1-3): Gemmi Sufali, Gianluca Faggioli, Enrico Gallitto, Rodolfo Pini, Andrea Vacirca, Chiara Mascoli, and Mauro Gargiulo. Results of a multidisciplinary spinal cord ischemia prevention protocol in elective repair of crawford's extent i-iii thoracoabdominal aneurysm by fenestrated and branched endografts. Vessel Plus, 8:16, Jan 2024. URL: https://doi.org/10.20517/2574-1209.2023.139, doi:10.20517/2574-1209.2023.139. This article has 1 citations.

7. (torre2024enhancingneuroprotectionin pages 10-11): Debora Emanuela Torre and Carmelo Pirri. Enhancing neuroprotection in cardiac and aortic surgeries: a narrative review. Anesthesia Research, 1:91-109, Aug 2024. URL: https://doi.org/10.3390/anesthres1020010, doi:10.3390/anesthres1020010. This article has 3 citations.

8. (islam2021anteriorspinalartery pages 7-9): Asraful Islam, Mohammad D Hossain, Abu Bakar Siddik, Tyfur Rahman, Ashraful Alam, Md Manjurul Islam Shourav, Nahian Afrida, Sajedur Rahman, and Masum Rahman. Anterior spinal artery syndrome due to intervertebral disc herniation: a systematic review. Journal of Spine Research and Surgery, Mar 2021. URL: https://doi.org/10.1101/2021.03.18.21253916, doi:10.1101/2021.03.18.21253916. This article has 1 citations.

9. (sliwa1992ischemicmyelopathya pages 1-2): James A. Sliwa and Ian C. Maclean. Ischemic myelopathy: a review of spinal vasculature and related clinical syndromes. Archives of physical medicine and rehabilitation, 73 4:365-72, Apr 1992. URL: https://doi.org/10.1016/0003-9993(92)90011-k, doi:10.1016/0003-9993(92)90011-k. This article has 150 citations and is from a highest quality peer-reviewed journal.

10. (islam2021anteriorspinalartery pages 4-7): Asraful Islam, Mohammad D Hossain, Abu Bakar Siddik, Tyfur Rahman, Ashraful Alam, Md Manjurul Islam Shourav, Nahian Afrida, Sajedur Rahman, and Masum Rahman. Anterior spinal artery syndrome due to intervertebral disc herniation: a systematic review. Journal of Spine Research and Surgery, Mar 2021. URL: https://doi.org/10.1101/2021.03.18.21253916, doi:10.1101/2021.03.18.21253916. This article has 1 citations.

11. (torre2024enhancingneuroprotectionin pages 8-10): Debora Emanuela Torre and Carmelo Pirri. Enhancing neuroprotection in cardiac and aortic surgeries: a narrative review. Anesthesia Research, 1:91-109, Aug 2024. URL: https://doi.org/10.3390/anesthres1020010, doi:10.3390/anesthres1020010. This article has 3 citations.

12. (nagoshi2025imagingcharacteristicsclinical pages 5-8): Narihito Nagoshi, Yasuhiro Kamata, Toshiki Okubo, Masahiro Ozaki, Satoshi Suzuki, Kazuki Takeda, Takahito Iga, Kentaro Shimizu, Morio Matsumoto, Masaya Nakamura, and Kota Watanabe. Imaging characteristics, clinical presentation, and prognosis of spinal cord infarction. Jun 2025. URL: https://doi.org/10.21203/rs.3.rs-6730915/v1, doi:10.21203/rs.3.rs-6730915/v1.

13. (batsou2023spinalcordischemia pages 1-2): V Batsou, IS Benetos, and I Vlamis. Spinal cord ischemia: a review of clinical and imaging features, risk factors and long-term prognosis. Unknown journal, 2023.

14. (awad2021histologicalfindingsafter pages 13-14): Hamdy Awad, Alexander Efanov, Jayanth Rajan, Andrew Denney, Bradley Gigax, Peter Kobalka, Hesham Kelani, D Michele Basso, John Bozinovski, and Esmerina Tili. Histological findings after aortic cross-clamping in preclinical animal models. Journal of neuropathology and experimental neurology, 80:895-911, Sep 2021. URL: https://doi.org/10.1093/jnen/nlab084, doi:10.1093/jnen/nlab084. This article has 12 citations and is from a peer-reviewed journal.

15. (ferreira2024anteriorspinalcord media 08b84382): Sílvia Ferreira, Angelo Fonseca, Filipe Correia, Joana Cunha, and Mariana Taveira. Anterior spinal cord infarction: a rare diagnosis with an uncommon presentation. Cureus, Jul 2024. URL: https://doi.org/10.7759/cureus.64083, doi:10.7759/cureus.64083. This article has 3 citations.

16. (awad2021histologicalfindingsafter pages 1-2): Hamdy Awad, Alexander Efanov, Jayanth Rajan, Andrew Denney, Bradley Gigax, Peter Kobalka, Hesham Kelani, D Michele Basso, John Bozinovski, and Esmerina Tili. Histological findings after aortic cross-clamping in preclinical animal models. Journal of neuropathology and experimental neurology, 80:895-911, Sep 2021. URL: https://doi.org/10.1093/jnen/nlab084, doi:10.1093/jnen/nlab084. This article has 12 citations and is from a peer-reviewed journal.

17. (kelani2023mousemodelof pages 1-3): Hesham Kelani, Kara Corps, Sarah Mikula, Lesley C. Fisher, Mahmoud T. Shalaan, Sarah Sturgill, Mark T. Ziolo, Mahmoud Abdel-Rasoul, D. Michele Basso, and Hamdy Awad. Mouse model of spinal cord hypoperfusion with immediate paralysis caused by endovascular repair of thoracic aortic aneurysm. Anesthesiology, 138:403-419, Jan 2023. URL: https://doi.org/10.1097/aln.0000000000004515, doi:10.1097/aln.0000000000004515. This article has 2 citations and is from a domain leading peer-reviewed journal.

18. (awad2010amousemodel pages 1-2): Hamdy Awad, Daniel P. Ankeny, Zhen Guan, Ping Wei, Dana M. McTigue, and Phillip G. Popovich. A mouse model of ischemic spinal cord injury with delayed paralysis caused by aortic cross-clamping. Anesthesiology, 113:880-891, Oct 2010. URL: https://doi.org/10.1097/aln.0b013e3181ec61ee, doi:10.1097/aln.0b013e3181ec61ee. This article has 72 citations and is from a domain leading peer-reviewed journal.

19. (wang2010developmentofa pages 1-2): Zhengfeng Wang, Wei Yang, Gavin W. Britz, Frederick W. Lombard, David S. Warner, and Huaxin Sheng. Development of a simplified spinal cord ischemia model in mice. Journal of Neuroscience Methods, 189:246-251, Jun 2010. URL: https://doi.org/10.1016/j.jneumeth.2010.04.003, doi:10.1016/j.jneumeth.2010.04.003. This article has 18 citations and is from a peer-reviewed journal.

20. (sufali2024resultsofa pages 3-5): Gemmi Sufali, Gianluca Faggioli, Enrico Gallitto, Rodolfo Pini, Andrea Vacirca, Chiara Mascoli, and Mauro Gargiulo. Results of a multidisciplinary spinal cord ischemia prevention protocol in elective repair of crawford's extent i-iii thoracoabdominal aneurysm by fenestrated and branched endografts. Vessel Plus, 8:16, Jan 2024. URL: https://doi.org/10.20517/2574-1209.2023.139, doi:10.20517/2574-1209.2023.139. This article has 1 citations.

21. (krzyzaniak2024complicationsofcerebrospinal pages 1-2): MD Halli Krzyzaniak, BN Martina Vergouwen, MD Darren Van Essen, MD Curtis Nixon, MD R. Scott McClure, MD Nadeem Jadavji, M. M. Randy D. Moore, and MD Kenton Rommens. Complications of cerebrospinal fluid drainage in thoracoabdominal aortic procedures. Canadian Journal of Surgery, 67:E389-E396, Dec 2024. URL: https://doi.org/10.1503/cjs.003624, doi:10.1503/cjs.003624. This article has 1 citations and is from a peer-reviewed journal.

22. (rosvall2024adedicatedpreventive pages 2-3): Lina Rosvall, Angelos Karelis, Björn Sonesson, and Nuno V. Dias. A dedicated preventive protocol sustainably avoids spinal cord ischemia after endovascular aortic repair. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1440674, doi:10.3389/fcvm.2024.1440674. This article has 8 citations and is from a peer-reviewed journal.