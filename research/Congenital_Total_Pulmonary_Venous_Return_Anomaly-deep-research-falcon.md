---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:17:41.968655'
end_time: '2026-05-05T23:38:55.696400'
duration_seconds: 1273.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Total Pulmonary Venous Return Anomaly
  mondo_id: ''
  category: Congenital Cardiovascular Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Total Pulmonary Venous Return Anomaly
- **MONDO ID:**  (if available)
- **Category:** Congenital Cardiovascular Disorder

## Research Objectives

Please provide a comprehensive research report on **Congenital Total Pulmonary Venous Return Anomaly** covering all of the
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
- **Disease Name:** Congenital Total Pulmonary Venous Return Anomaly
- **MONDO ID:**  (if available)
- **Category:** Congenital Cardiovascular Disorder

## Research Objectives

Please provide a comprehensive research report on **Congenital Total Pulmonary Venous Return Anomaly** covering all of the
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


# Congenital Total Pulmonary Venous Return Anomaly (Total Anomalous Pulmonary Venous Connection/Return; TAPVC/TAPVR)

**Scope note:** In contemporary clinical literature, “congenital total pulmonary venous return anomaly” corresponds to **total anomalous pulmonary venous connection/return (TAPVC/TAPVR)**, a congenital cardiovascular malformation where **all pulmonary veins fail to connect to the left atrium** and instead drain to the right atrium or systemic venous circulation. (cheng2024clinicaldiagnosisand pages 1-4, xue2023prenataldiagnosisand pages 1-2)

## 1. Disease Information

### 1.1 Overview (current understanding)
TAPVC/TAPVR is a **rare cyanotic congenital heart disease** in which **oxygenated pulmonary venous blood returns to the right-sided circulation/systemic veins** rather than the left atrium, causing systemic desaturation and abnormal pulmonary/systemic blood flow patterns. (cheng2024clinicaldiagnosisand pages 1-4, xue2023prenataldiagnosisand pages 1-2)

A major determinant of early clinical deterioration is **pulmonary venous obstruction (PVO)** along the anomalous venous pathway, which increases pulmonary venous pressure, drives pulmonary edema, and worsens hypoxemia/hemodynamic compromise. (xue2023prenataldiagnosisand pages 2-3, cheng2024clinicaldiagnosisand pages 4-6)

### 1.2 Key identifiers and coding systems
- **ICD-10 (registry definition):** Q262 / Q26.2 “Total anomalous pulmonary venous connection” used to identify TAPVC in a nationwide registry study. (henningsen2025nationwideregistrystudy pages 2-3)
- **Prenatal classification system:** Commonly described using the historical **Darling classification** into four anatomic types: supracardiac, intracardiac/cardiac, infracardiac, and mixed. (cheng2024clinicaldiagnosisand pages 4-6, xue2023prenataldiagnosisand pages 1-2)
- **MONDO / Orphanet / OMIM / MeSH:** Not retrievable from the currently available full-text corpus in this run; therefore **not reported here**.

### 1.3 Common synonyms and alternative names
- Total anomalous pulmonary venous **connection** (TAPVC)
- Total anomalous pulmonary venous **return** (TAPVR)
- Total anomalous pulmonary venous **drainage** (TAPVD) (terminology varies across fetal imaging literature) (azab2022tbx5variantwith pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated)
Most information below is derived from **aggregated cohorts** (fetal cohorts and surgical cohorts), **retrospective registries**, and **review-level synthesis**, supplemented by smaller case series. (xue2023prenataldiagnosisand pages 1-2, li2023totalanomalouspulmonary pages 1-2, henningsen2025nationwideregistrystudy pages 2-3)

## 2. Etiology

### 2.1 Primary causal factors (mechanistic)
Clinical and surgical literature describes TAPVC/TAPVR as arising from **abnormal embryologic development/remodeling of pulmonary venous connections** and venous pole structures, with contributions from **genetic variation** in some patients. (cheng2024clinicaldiagnosisand pages 4-6, xue2023prenataldiagnosisand pages 1-2)

### 2.2 Genetic risk factors (genes and syndromic associations)
**TBX5 (Holt–Oram syndrome expansion):**
- A pathogenic **TBX5 nonsense variant** (c.577G>T; p.Gly193*) was reported in a family where the proband had **mixed-type TAPVR**, and subsequent phenotyping supported Holt–Oram syndrome. This report is described as the *first genetic investigation* reporting this association. (azab2022tbx5variantwith pages 1-2)

**ANKRD1 (candidate gene; gain-of-function signal; mechanistic animal model):**
- A mechanistic study reports that increased ANKRD1 levels (including gain-of-function contexts) have been associated in humans with TAPVR and motivated creation of a **myocardial ANKRD1 overexpression mouse model**. In transgenic mice, myocardial ANKRD1 overexpression caused **sinus venosus/venous pole remodeling defects** with **abnormal pulmonary vein–systemic venous communications**, linking a plausible developmental mechanism to anomalous venous return phenotypes. (piroddi2020myocardialoverexpressionof pages 1-3, piroddi2020myocardialoverexpressionof pages 7-9, piroddi2020myocardialoverexpressionof pages 3-4)

**Associated laterality/heterotaxy context (clinical association):**
In fetal cohorts, TAPVC frequently co-occurs with complex congenital heart disease and laterality disorders such as right atrial isomerism (a heterotaxy phenotype). (xue2023prenataldiagnosisand pages 7-7, xue2023prenataldiagnosisand pages 8-10)

### 2.3 Environmental risk/protective factors; GxE
No TAPVC-specific, well-supported protective factors or gene–environment interaction evidence was identified in the retrieved corpus. Environmental teratogen evidence is not established in the extracted TAPVC-focused texts.

## 3. Phenotypes

### 3.1 Core clinical presentation (typical)
Neonatal/infant presentations in clinical series commonly include **respiratory distress/shortness of breath**, **cyanosis**, recurrent respiratory infections/pneumonia, and heart failure/poor growth—particularly in obstructed forms. (cheng2024clinicaldiagnosisand pages 1-4, cheng2024clinicaldiagnosisand pages 4-6)

### 3.2 Fetal imaging phenotypes and prenatal “suspicious signs”
A structured fetal echocardiography approach highlighted suspicious ultrasound findings such as:
- “**a small LA**,” “**an increased distance from the LA to the descending aorta**,” “**a smooth posterior wall of the LA**,” “**unobservable orifices of the PV**,” “**evident extra vessels and centrifugal venous flow**,” and “**an abnormal dilated vein (e.g., SVC, INN, AZV, IVC, or CS)**.” (xue2023prenataldiagnosisand pages 2-3)

### 3.3 Suggested HPO terms (examples)
*Note: HPO IDs are suggested based on phenotype labels; they were not retrieved from an ontology database in this run.*
- Cyanosis (HP:0000969)
- Respiratory distress (HP:0002098)
- Tachypnea (HP:0002789)
- Recurrent pneumonia (HP:0006532)
- Pulmonary venous obstruction/stenosis (concept; may map to Pulmonary vein stenosis (HP:0012728))
- Failure to thrive (HP:0001508)

### 3.4 Quality of life impact
No TAPVC-specific validated QoL instrument results (e.g., PedsQL, SF-36) were found in the retrieved TAPVC-focused corpus.

## 4. Genetic / Molecular Information

### 4.1 Causal genes and pathogenic variants (evidence-supported in retrieved corpus)
- **TBX5**: c.577G>T; p.Gly193* (nonsense; loss-of-function) associated with mixed-type TAPVR in a Holt–Oram syndrome context (family-based trio exome sequencing). (azab2022tbx5variantwith pages 1-2)

### 4.2 Candidate genes / functional mechanisms
- **ANKRD1**: gain-of-function/dysregulation implicated as a candidate driver of venous pole remodeling defects relevant to anomalous pulmonary venous return; transgenic overexpression produces congenital sinus venosus defects and later diastolic dysfunction. (piroddi2020myocardialoverexpressionof pages 1-3, piroddi2020myocardialoverexpressionof pages 7-9)

### 4.3 Variant class and origin
- TBX5 variant reported: nonsense (likely pathogenic in the report’s interpretation). (azab2022tbx5variantwith pages 1-2)
- ANKRD1 evidence in retrieved corpus: gain-of-function/dysregulation signal and experimental overexpression model; specific human variant nomenclature is not fully extractable from the limited snippets provided. (piroddi2020myocardialoverexpressionof pages 3-4, piroddi2020myocardialoverexpressionof pages 1-3)

### 4.4 Modifier genes, epigenetics, chromosomal abnormalities
No specific, TAPVC-focused modifier gene sets, epigenetic signatures, or recurrent CNVs could be extracted from the retrieved full-text corpus in this run.

## 5. Environmental Information
No TAPVC-specific environmental, lifestyle, occupational, or infectious causal triggers were identified in the retrieved TAPVC-focused literature.

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (integrated clinical + developmental model)
1. **Developmental misconnection/remodeling failure** results in absent direct pulmonary vein–left atrium connection and anomalous drainage to systemic venous pathways/right atrium. (xue2023prenataldiagnosisand pages 1-2, cheng2024clinicaldiagnosisand pages 1-4)
2. Mixing of oxygenated pulmonary venous blood with systemic venous blood in the right atrium leads to **cyanosis/hypoxemia** and abnormal loading conditions. (cheng2024clinicaldiagnosisand pages 1-4)
3. **Pulmonary venous obstruction** (when present) increases pulmonary venous pressure, aggravating pulmonary congestion and worsening hypoxemia and hemodynamics; obstruction status strongly influences prognosis and urgency of intervention. (xue2023prenataldiagnosisand pages 2-3, cheng2024clinicaldiagnosisand pages 4-6)
4. Post-repair, some patients develop **pulmonary vein stenosis (PVS)/recurrent obstruction**, a major driver of reintervention, morbidity, and mortality. (wen2024insightintothe pages 12-14, alifu2024assessingtherisk pages 3-5)

### 6.2 Molecular/cellular processes (evidence-linked)
**ANKRD1 gain-of-function model (mouse):** myocardial overexpression causes sinus venosus defects originating from impaired embryonic remodeling, with early transcriptional perturbations involving **GATA4 and NKX2-5** and downstream sarcomeric/titin modulation; embryos show abnormal venous pole connections, and adults develop progressive diastolic dysfunction. (piroddi2020myocardialoverexpressionof pages 1-3, piroddi2020myocardialoverexpressionof pages 7-9)

### 6.3 Suggested ontology mappings
**GO (Biological Process) suggestions:**
- Heart morphogenesis (GO:0003007)
- Cardiovascular system development (GO:0072358)
- Pulmonary vein development (term exists conceptually; exact GO ID not retrieved in this run)
- Blood vessel morphogenesis (GO:0048514)

**CL (Cell Ontology) suggestions:**
- Cardiomyocyte (CL:0000746)
- Endothelial cell (CL:0000115)
- Cardiac fibroblast (CL term exists; exact ID not retrieved in this run)

**UBERON (Anatomy) suggestions:**
- Pulmonary vein (UBERON term)
- Left atrium (UBERON term)
- Sinus venosus / venous pole region (UBERON term)

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Primary:** pulmonary veins and their confluence, left atrium (failed connection), right atrium/systemic venous pathways receiving pulmonary venous return. (xue2023prenataldiagnosisand pages 1-2, cheng2024clinicaldiagnosisand pages 1-4)
- **Secondary functional involvement:** lungs (pulmonary congestion/edema, especially with obstruction), pulmonary vasculature (risk of pulmonary hypertension), and systemic oxygen delivery (cyanosis). (cheng2024clinicaldiagnosisand pages 4-6, cheng2024clinicaldiagnosisand pages 1-4)

## 8. Temporal Development
- **Onset:** congenital; often clinically apparent in the neonatal period, especially in obstructed TAPVC. (cheng2024clinicaldiagnosisand pages 4-6)
- **Course:** without surgery, high early mortality is reported; after repair, risk of postoperative pulmonary vein stenosis/obstruction often appears within months and can progress rapidly. (cheng2024clinicaldiagnosisand pages 4-6, wen2024insightintothe pages 12-14)

## 9. Inheritance and Population

### 9.1 Epidemiology (selected recent/representative statistics)
- TAPVC is described as approximately **2% of congenital heart disease** in a recent clinical summary. (cheng2024clinicaldiagnosisand pages 4-6)
- In a TBX5-associated report, TAPVR is described as ~**7 per 100,000 live births** (and ~1–3% of CHD). (azab2022tbx5variantwith pages 1-2)

### 9.2 Sex ratio / demographics
A clinical summary notes TAPVC is reported more frequently in males than females. (cheng2024clinicaldiagnosisand pages 4-6)

### 9.3 Inheritance
The retrieved corpus supports **heterogeneous genetic architecture**: sporadic cases predominate, but rare **monogenic syndromic** associations (e.g., TBX5 in Holt–Oram) and candidate gene mechanisms (ANKRD1 gain-of-function contexts) exist. (azab2022tbx5variantwith pages 1-2, piroddi2020myocardialoverexpressionof pages 1-3)

## 10. Diagnostics

### 10.1 Prenatal diagnosis (real-world implementation)
A fetal cohort describes a **four-step prenatal ultrasonography** workflow:
1) demonstrate absent PV–LA connections; 2) identify common pulmonary vein and drainage route for subtype classification; 3) assess obstruction (turbulence and max velocity >50 cm/s suggested); 4) assess associated malformations. (xue2023prenataldiagnosisand pages 2-3)

**Performance (2023 fetal cohort):** diagnostic accuracy by type was reported as **95% (supracardiac), 75% (intracardiac), 95% (infracardiac), 77% (mixed)**; among isolated TAPVC (n=21), **6 were missed** and **1 misclassified** prenatally. (xue2023prenataldiagnosisand pages 8-10, xue2023prenataldiagnosisand pages 1-2)

**Figure/Table evidence (classification + drainage routes + obstruction):** Table 5 from the fetal cohort provides structured subtype and drainage-route detail along with obstruction findings. (xue2023prenataldiagnosisand media 1a8f0ae4)

### 10.2 Postnatal diagnosis
- **Transthoracic echocardiography (TTE)** is typically first-line but can have mis-/underdiagnosis in some settings.
- **Computed tomographic angiography (CTA)** can increase anatomic diagnostic clarity and can also be used for surgical planning, but introduces radiation/contrast considerations. (cheng2024clinicaldiagnosisand pages 4-6, matsuhisa2020computedtomographybasedsurgical pages 1-2)

### 10.3 Differential diagnosis (not exhaustively captured in retrieved corpus)
Differentials for cyanotic neonatal CHD with pulmonary overcirculation/respiratory distress may include transposition physiology, obstructed left-sided lesions, and other complex CHD; specific differential algorithms were not retrievable from society guidelines in the current corpus.

## 11. Outcome / Prognosis

### 11.1 Natural history without intervention
A clinical summary reports very poor natural prognosis without timely surgical intervention (e.g., mortality up to **48.8% in infancy** and high mortality in the first year in severe physiologic circumstances). (cheng2024clinicaldiagnosisand pages 4-6)

### 11.2 Contemporary surgical outcomes and complications
- Review-level synthesis describes **early postoperative mortality** in published series commonly ranging from **<10% to ~20%**, with **postoperative pulmonary vein stenosis (PVS)** as the most common complication and an incidence often cited around **10–20%**. (wen2024insightintothe pages 12-14)
- In a single-center 2023 series using **primary sutureless repair** (n=80), there were **2 early deaths** and **1 late death**, and **2 patients developed postoperative PVO** with **no reintervention** required. (li2023totalanomalouspulmonary pages 1-2)

### 11.3 Reoperation risk stratification (2024 evidence)
A 2024 cohort found that **pre-discharge mild PVO** (Doppler velocity **>1.2 m/s**) was associated with substantially higher reoperation rates; in the fully adjusted model, HR **13.90** (95% CI 1.16–166.5) for reoperation within 1 year. (alifu2024assessingtherisk pages 3-5, alifu2024assessingtherisk pages 5-6)

## 12. Treatment

### 12.1 Surgical/interventional treatment (current practice)
**Definitive management is surgical repair**, typically in the neonatal period when clinically indicated. (cheng2024clinicaldiagnosisand pages 4-6)

**Primary sutureless repair (2023 outcomes):** In a single-center series (2015–2020), primary sutureless repair across all Darling subtypes showed low postoperative PVO incidence (2/80) and no reintervention, supporting the view that sutureless approaches may reduce anastomotic-level restenosis risk across subtypes. (li2023totalanomalouspulmonary pages 1-2)

**Imaging-guided surgical planning (CTA era effect):** A 112-patient era comparison reported marked improvement in 5-year survival with a CTA-based strategy (biventricular: 69%→97%; single-ventricle: 21%→70%) and reduced/managed PVS burden with aggressive reintervention. (matsuhisa2020computedtomographybasedsurgical pages 1-2)

**Technique comparisons:** For supracardiac TAPVC, a modified L-shaped incision approach was associated with improved freedom from death/postoperative PVO versus the posterior technique, especially in those with preoperative obstruction. (feng2020midtermresultsof pages 1-2)

### 12.2 Supportive perioperative management
Postoperative management may include intensive care strategies and **pulmonary hypertension-directed therapies** (e.g., inhaled nitric oxide, endothelin receptor antagonists, PDE-5 inhibitors, prostacyclin) as adjuncts when pulmonary hypertension is present. (cheng2024clinicaldiagnosisand pages 4-6)

### 12.3 Pharmacotherapy / advanced therapeutics
No TAPVC-specific disease-modifying pharmacotherapy trials, gene therapy, or RNA therapeutics were identified in the retrieved corpus.

### 12.4 Suggested MAXO terms (examples)
*Note: MAXO IDs not retrieved in this run; terms suggested as labels.*
- Surgical repair of congenital heart defect (e.g., “TAPVC repair”)
- Sutureless pulmonary venous anastomosis
- Computed tomography angiography for preoperative planning
- Echocardiographic surveillance / follow-up

## 13. Prevention

Primary prevention of TAPVC is not established. Practical prevention focuses on:
- **Secondary prevention via prenatal detection** and perinatal planning (delivery at tertiary center; timely neonatal stabilization/surgery). (xue2023prenataldiagnosisand pages 8-10)
- **Genetic counseling/testing** when syndromic features or familial recurrence is suspected (e.g., TBX5/Holt–Oram context). (azab2022tbx5variantwith pages 1-2)

## 14. Other Species / Natural Disease
No naturally occurring veterinary TAPVC disease series were identified in the retrieved corpus.

## 15. Model Organisms
A transgenic mouse model with **myocardial ANKRD1 overexpression** demonstrates congenital venous pole defects (sinus venosus defects; abnormal PV–systemic venous communications) and progressive functional deterioration, providing a mechanistic model relevant to anomalous pulmonary venous return. (piroddi2020myocardialoverexpressionof pages 1-3, piroddi2020myocardialoverexpressionof pages 7-9)

## Recent developments (2023–2024 highlights)
- **Structured fetal diagnostic protocols** with quantified type-specific accuracy and documentation that **isolated TAPVC is more likely to be missed** than syndromic/heterotaxy-associated TAPVC. (xue2023prenataldiagnosisand pages 8-10, xue2023prenataldiagnosisand pages 1-2)
- **Expansion of sutureless repair evidence** showing low postoperative obstruction rates in a 2023 single-center cohort. (li2023totalanomalouspulmonary pages 1-2)
- **Quantitative echocardiographic risk stratification** immediately prior to discharge (1.2 m/s threshold) associated with markedly increased reoperation risk within 1 year. (alifu2024assessingtherisk pages 3-5)

## Evidence map of key studies
| Topic | Key findings with quantitative stats | Population/Design | Year | Publication (journal) | Identifier (DOI and PMID if available) | URL |
|---|---|---|---|---|---|---|
| Classification / prenatal diagnosis | Four-step prenatal ultrasonography in 62 confirmed fetal TAPVC cases; subtype distribution: supracardiac 20/62 (32%), intracardiac 12/62 (19%), infracardiac 21/62 (34%), mixed 9/62 (15%); prenatal diagnostic accuracy by type: 95%, 75%, 95%, 77%, respectively; among 21 isolated TAPVC cases, 6 were missed and 1 was misclassified prenatally; literature cited in-study reported prenatal PVO prevalence 34.1% (95% CI 22.7%–47.7%); suspicious signs included small LA, increased LA–descending aorta distance, smooth posterior LA wall, absent PV orifices, extra vessels/centrifugal venous flow, and dilated systemic veins; obstruction marker on Doppler: turbulent flow or max velocity >50 cm/s (xue2023prenataldiagnosisand pages 8-10, xue2023prenataldiagnosisand pages 2-3, xue2023prenataldiagnosisand pages 1-2) | Retrospective fetal cohort; prenatal US with postnatal echo/surgery/autopsy confirmation | 2023 | Frontiers in Pediatrics | DOI: 10.3389/fped.2023.1206032; PMID: not available in context | https://doi.org/10.3389/fped.2023.1206032 |
| Surgery / outcomes | Primary sutureless repair in 80 TAPVC patients: supracardiac 35 (43.8%), cardiac 24 (30%), infracardiac 17 (21.2%), mixed 4 (5%); median age at repair 16.5 days, median weight 3.5 kg; preoperative PVO 20/80 (25%); early deaths 2, late death 1; postoperative PVO in 2 patients, none required reintervention; prolonged CPB time (p=0.009), preoperative pneumonia (p=0.022), and gender (p=0.041) associated with higher postoperative PV flow velocity; authors argue primary sutureless repair may reduce subtype-related differences in postoperative obstruction (li2023totalanomalouspulmonary pages 1-2) | Single-center retrospective surgical series (2015–2020) | 2023 | Frontiers in Surgery | DOI: 10.3389/fsurg.2022.1086596; PMID: not available in context | https://doi.org/10.3389/fsurg.2022.1086596 |
| Postoperative obstruction predictors | Mild pre-discharge pulmonary vein obstruction defined as Doppler velocity >1.2 m/s; postoperative mild obstruction present in 12/38 (31.6%); median follow-up 10.0 months; reoperation within 1 year was higher with mild obstruction (33.3% vs 7.7%); fully adjusted HR for reoperation 13.90 (95% CI 1.16–166.5), with threshold analysis supporting 1.2 m/s as a practical cutoff for intensified follow-up; routine follow-up echo at 1, 3, 6, and 12 months (alifu2024assessingtherisk pages 1-2, alifu2024assessingtherisk pages 5-6, alifu2024assessingtherisk pages 3-5, alifu2024assessingtherisk pages 2-3) | Single-center retrospective cohort after TAPVC repair | 2024 | Frontiers in Cardiovascular Medicine | DOI: 10.3389/fcvm.2024.1399659; PMID: not available in context | https://doi.org/10.3389/fcvm.2024.1399659 |
| Surgery / outcomes / imaging-guided planning | CTA-based surgical planning in 112 repaired TAPVC patients comparing era 1 (1996–2010, n=56) vs era 2 (2011–2018, n=56); 5-year survival in biventricular hearts improved from 69% to 97% (P=0.0024); in single-ventricle hearts from 21% to 70% (P=0.0007); post-repair PVS in biventricular hearts fell from 23% to 13%, and in single-ventricle hearts from 60% to 36%; since 2011, 12 patients with post-repair PVS had multiple reinterventions with 5-year survival 88%; preoperative CTA associated with improved survival and PVS-free survival (matsuhisa2020computedtomographybasedsurgical pages 1-2) | Retrospective era-comparison cohort | 2020 | European Journal of Cardio-Thoracic Surgery | DOI: 10.1093/ejcts/ezaa028; PMID: not available in context | https://doi.org/10.1093/ejcts/ezaa028 |
| Surgery / technique comparison | Modified L-shaped incision vs posterior technique for supracardiac TAPVC in 121 patients (53 vs 68; matched 52 pairs); median follow-up 33 months; operative mortality 5/121 (4.1%), late mortality 12/121 (9.9%); postoperative PVO in 21 patients overall; in matched patients with preoperative PVO, freedom from death and postoperative PVO at 1 and 3 years was 100% and 85.7% in L-shaped group vs 90% and 22.9% in posterior-technique group (P=0.002); posterior technique independently increased risk of death/PVO (HR 4.12, 95% CI 1.12–15.16; P=0.03) (feng2020midtermresultsof pages 1-2) | Single-center retrospective comparative study with propensity matching | 2020 | European Journal of Cardio-Thoracic Surgery | DOI: 10.1093/ejcts/ezaa264; PMID: not available in context | https://doi.org/10.1093/ejcts/ezaa264 |
| Genetics / molecular | First genetically confirmed association of mixed-type TAPVR with Holt-Oram syndrome due to TBX5 nonsense variant c.577G>T (p.Gly193*); trio WES identified cosegregating variant; study notes TAPVR accounts for ~1–3% of CHD and ~7 per 100,000 live births; protein modeling indicated reduced non-covalent bonding and impaired DNA-binding stability of mutant TBX5; expands cardiac phenotype spectrum for TBX5/HOS (azab2022tbx5variantwith pages 1-2) | Family-based human genetic case report with trio exome sequencing | 2022 | Molecular Medicine Reports | DOI: 10.3892/mmr.2022.12726; PMID: not available in context | https://doi.org/10.3892/mmr.2022.12726 |
| Genetics / molecular / model organism | ANKRD1 gain-of-function/overexpression linked to anomalous pulmonary venous return biology: prior human evidence cited TAPVR patients with ANKRD1 dysregulation (3–4-fold transcript increase or 10–20% protein-stability increase); myocardial ANKRD1-overexpressing transgenic mice developed sinus venosus defects with anomalous PV–systemic venous communications, venous-pole remodeling defects, early GATA4/Nkx2.5 upregulation, and progressive diastolic dysfunction/heart failure; provides mechanistic support for ANKRD1 as a TAPVR candidate gene (piroddi2020myocardialoverexpressionof pages 3-4, piroddi2020myocardialoverexpressionof pages 12-13, piroddi2020myocardialoverexpressionof pages 1-3, piroddi2020myocardialoverexpressionof pages 7-9) | Transgenic mouse model with supporting human candidate-gene context | 2020 | Cardiovascular Research | DOI: 10.1093/cvr/cvz291; PMID: not available in context | https://doi.org/10.1093/cvr/cvz291 |


*Table: This table condenses high-value recent and foundational studies on TAPVC/TAPVR across prenatal diagnosis, operative strategy, postoperative obstruction risk, and genetics. It is useful as a quick-reference evidence map for building a disease knowledge base entry.*

## Key visual evidence
The following table image (from a 2023 fetal cohort) summarizes TAPVC anatomic subtypes, drainage routes, and obstruction findings, supporting the classification and prenatal evaluation sections. (xue2023prenataldiagnosisand media 1a8f0ae4)

## Limitations of this report (data availability)
- MONDO/Orphanet/OMIM/MeSH identifiers, formal guideline documents, and TAPVC-specific QoL datasets were not retrievable in the accessible corpus for this run; therefore, these elements are flagged as unavailable rather than inferred.
- Some epidemiology estimates are study-/setting-specific; population-level prevalence estimates vary by ascertainment method and inclusion criteria.


References

1. (cheng2024clinicaldiagnosisand pages 1-4): Weiping Cheng, Junzhao Zhu, Youbo Xu, Yingqiang Guo, and Lexiang Shi. Clinical diagnosis and treatment of 5 cases of tapcv in infants. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-3480976/v1, doi:10.21203/rs.3.rs-3480976/v1.

2. (xue2023prenataldiagnosisand pages 1-2): Xiaoying Xue, Qiumei Wu, Mingtao Xiong, Wen Ling, Shan Guo, Hong Ma, Biying Huang, Min Liu, Xiuqing Qiu, and Zongjie Weng. Prenatal diagnosis and postnatal verification in fetuses with total anomalous pulmonary venous connection. Frontiers in Pediatrics, Jun 2023. URL: https://doi.org/10.3389/fped.2023.1206032, doi:10.3389/fped.2023.1206032. This article has 6 citations.

3. (xue2023prenataldiagnosisand pages 2-3): Xiaoying Xue, Qiumei Wu, Mingtao Xiong, Wen Ling, Shan Guo, Hong Ma, Biying Huang, Min Liu, Xiuqing Qiu, and Zongjie Weng. Prenatal diagnosis and postnatal verification in fetuses with total anomalous pulmonary venous connection. Frontiers in Pediatrics, Jun 2023. URL: https://doi.org/10.3389/fped.2023.1206032, doi:10.3389/fped.2023.1206032. This article has 6 citations.

4. (cheng2024clinicaldiagnosisand pages 4-6): Weiping Cheng, Junzhao Zhu, Youbo Xu, Yingqiang Guo, and Lexiang Shi. Clinical diagnosis and treatment of 5 cases of tapcv in infants. Unknown journal, Oct 2024. URL: https://doi.org/10.21203/rs.3.rs-3480976/v1, doi:10.21203/rs.3.rs-3480976/v1.

5. (henningsen2025nationwideregistrystudy pages 2-3): Maj Beldring Henningsen, Cathrine Bohnstedt, Therese Risom Vestergaard, Morten Holdgaard Smerup, Pi Vejsig Madsen, and Lone Graff Stensballe. Nationwide registry study of long term survival and comorbidities in total anomalous pulmonary venous connection in denmark. Scientific Reports, Aug 2025. URL: https://doi.org/10.1038/s41598-025-15769-0, doi:10.1038/s41598-025-15769-0. This article has 3 citations and is from a peer-reviewed journal.

6. (azab2022tbx5variantwith pages 1-2): Bilal Azab, Dunia Aburizeg, Weizhen Ji, Lauren Jeffries, Nooredeen Isbeih, Amal Al‑Akily, Hashim Mohammad, Yousef Osba, Mohammad Shahin, Zain Dardas, Ma'mon Hatmal, Iyad Al‑Ammouri, and Saquib Lakhani. Tbx5 variant with the novel phenotype of mixed-type total anomalous pulmonary venous return in holt-oram syndrome and variable intrafamilial heart defects. Molecular Medicine Reports, May 2022. URL: https://doi.org/10.3892/mmr.2022.12726, doi:10.3892/mmr.2022.12726. This article has 11 citations and is from a peer-reviewed journal.

7. (li2023totalanomalouspulmonary pages 1-2): Gefei Li, Baoying Meng, Cheng Zhang, Weimin Zhang, Xiaodong Zhou, Qing Zhang, and Yiqun Ding. Total anomalous pulmonary venous connection in 80 patients: primary sutureless repair and outcomes. Frontiers in Surgery, Jan 2023. URL: https://doi.org/10.3389/fsurg.2022.1086596, doi:10.3389/fsurg.2022.1086596. This article has 5 citations.

8. (piroddi2020myocardialoverexpressionof pages 1-3): Nicoletta Piroddi, Paola Pesce, Beatrice Scellini, Stefano Manzini, Giulia S Ganzetti, Ileana Badi, Michela Menegollo, Virginia Cora, Simone Tiso, Raffaella Cinquetti, Laura Monti, Giulia Chiesa, Steven B Bleyl, Marco Busnelli, Federica Dellera, Daniele Bruno, Federico Caicci, Annalisa Grimaldi, Roberto Taramelli, Lucia Manni, David Sacerdoti, Chiara Tesi, Corrado Poggesi, Simonetta Ausoni, Francesco Acquati, and Marina Campione. Myocardial overexpression of ankrd1 causes sinus venosus defects and progressive diastolic dysfunction. Cardiovascular research, 116:1458-1472, Nov 2020. URL: https://doi.org/10.1093/cvr/cvz291, doi:10.1093/cvr/cvz291. This article has 40 citations and is from a domain leading peer-reviewed journal.

9. (piroddi2020myocardialoverexpressionof pages 7-9): Nicoletta Piroddi, Paola Pesce, Beatrice Scellini, Stefano Manzini, Giulia S Ganzetti, Ileana Badi, Michela Menegollo, Virginia Cora, Simone Tiso, Raffaella Cinquetti, Laura Monti, Giulia Chiesa, Steven B Bleyl, Marco Busnelli, Federica Dellera, Daniele Bruno, Federico Caicci, Annalisa Grimaldi, Roberto Taramelli, Lucia Manni, David Sacerdoti, Chiara Tesi, Corrado Poggesi, Simonetta Ausoni, Francesco Acquati, and Marina Campione. Myocardial overexpression of ankrd1 causes sinus venosus defects and progressive diastolic dysfunction. Cardiovascular research, 116:1458-1472, Nov 2020. URL: https://doi.org/10.1093/cvr/cvz291, doi:10.1093/cvr/cvz291. This article has 40 citations and is from a domain leading peer-reviewed journal.

10. (piroddi2020myocardialoverexpressionof pages 3-4): Nicoletta Piroddi, Paola Pesce, Beatrice Scellini, Stefano Manzini, Giulia S Ganzetti, Ileana Badi, Michela Menegollo, Virginia Cora, Simone Tiso, Raffaella Cinquetti, Laura Monti, Giulia Chiesa, Steven B Bleyl, Marco Busnelli, Federica Dellera, Daniele Bruno, Federico Caicci, Annalisa Grimaldi, Roberto Taramelli, Lucia Manni, David Sacerdoti, Chiara Tesi, Corrado Poggesi, Simonetta Ausoni, Francesco Acquati, and Marina Campione. Myocardial overexpression of ankrd1 causes sinus venosus defects and progressive diastolic dysfunction. Cardiovascular research, 116:1458-1472, Nov 2020. URL: https://doi.org/10.1093/cvr/cvz291, doi:10.1093/cvr/cvz291. This article has 40 citations and is from a domain leading peer-reviewed journal.

11. (xue2023prenataldiagnosisand pages 7-7): Xiaoying Xue, Qiumei Wu, Mingtao Xiong, Wen Ling, Shan Guo, Hong Ma, Biying Huang, Min Liu, Xiuqing Qiu, and Zongjie Weng. Prenatal diagnosis and postnatal verification in fetuses with total anomalous pulmonary venous connection. Frontiers in Pediatrics, Jun 2023. URL: https://doi.org/10.3389/fped.2023.1206032, doi:10.3389/fped.2023.1206032. This article has 6 citations.

12. (xue2023prenataldiagnosisand pages 8-10): Xiaoying Xue, Qiumei Wu, Mingtao Xiong, Wen Ling, Shan Guo, Hong Ma, Biying Huang, Min Liu, Xiuqing Qiu, and Zongjie Weng. Prenatal diagnosis and postnatal verification in fetuses with total anomalous pulmonary venous connection. Frontiers in Pediatrics, Jun 2023. URL: https://doi.org/10.3389/fped.2023.1206032, doi:10.3389/fped.2023.1206032. This article has 6 citations.

13. (wen2024insightintothe pages 12-14): Chen Wen, Geng Shen, Chenhao Fang, and Lan Tian. Insight into the research history and trends of total anomalous pulmonary venous connection: a bibliometric analysis. Journal of Cardiothoracic Surgery, May 2024. URL: https://doi.org/10.1186/s13019-024-02787-8, doi:10.1186/s13019-024-02787-8. This article has 6 citations and is from a peer-reviewed journal.

14. (alifu2024assessingtherisk pages 3-5): Ailixiati Alifu, Haifan Wang, and Renwei Chen. Assessing the risk of reoperation for mild pulmonary vein obstruction post-tapvc repair: a retrospective cohort study. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1399659, doi:10.3389/fcvm.2024.1399659. This article has 2 citations and is from a peer-reviewed journal.

15. (xue2023prenataldiagnosisand media 1a8f0ae4): Xiaoying Xue, Qiumei Wu, Mingtao Xiong, Wen Ling, Shan Guo, Hong Ma, Biying Huang, Min Liu, Xiuqing Qiu, and Zongjie Weng. Prenatal diagnosis and postnatal verification in fetuses with total anomalous pulmonary venous connection. Frontiers in Pediatrics, Jun 2023. URL: https://doi.org/10.3389/fped.2023.1206032, doi:10.3389/fped.2023.1206032. This article has 6 citations.

16. (matsuhisa2020computedtomographybasedsurgical pages 1-2): Hironori Matsuhisa, Yoshihiro Oshima, Tomonori Higuma, Shunsuke Matsushima, Shota Hasegawa, Yuson Wada, Michio Matsuoka, and Toshikatsu Tanaka. Computed tomography-based surgical strategy for total anomalous pulmonary venous connection. European journal of cardio-thoracic surgery : official journal of the European Association for Cardio-thoracic Surgery, 58:237-245, Feb 2020. URL: https://doi.org/10.1093/ejcts/ezaa028, doi:10.1093/ejcts/ezaa028. This article has 8 citations.

17. (alifu2024assessingtherisk pages 5-6): Ailixiati Alifu, Haifan Wang, and Renwei Chen. Assessing the risk of reoperation for mild pulmonary vein obstruction post-tapvc repair: a retrospective cohort study. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1399659, doi:10.3389/fcvm.2024.1399659. This article has 2 citations and is from a peer-reviewed journal.

18. (feng2020midtermresultsof pages 1-2): Zicong Feng, Yang Yang, Fengpu He, Kunjing Pang, Kai Ma, Sen Zhang, Lei Qi, Guanxi Wang, Fengqun Mao, Jianhui Yuan, and Shoujun Li. Mid-term results of modified l-shaped incision technique for supracardiac total anomalous pulmonary venous connection. European journal of cardio-thoracic surgery : official journal of the European Association for Cardio-thoracic Surgery, 58:1261-1268, Sep 2020. URL: https://doi.org/10.1093/ejcts/ezaa264, doi:10.1093/ejcts/ezaa264. This article has 9 citations.

19. (alifu2024assessingtherisk pages 1-2): Ailixiati Alifu, Haifan Wang, and Renwei Chen. Assessing the risk of reoperation for mild pulmonary vein obstruction post-tapvc repair: a retrospective cohort study. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1399659, doi:10.3389/fcvm.2024.1399659. This article has 2 citations and is from a peer-reviewed journal.

20. (alifu2024assessingtherisk pages 2-3): Ailixiati Alifu, Haifan Wang, and Renwei Chen. Assessing the risk of reoperation for mild pulmonary vein obstruction post-tapvc repair: a retrospective cohort study. Frontiers in Cardiovascular Medicine, Jun 2024. URL: https://doi.org/10.3389/fcvm.2024.1399659, doi:10.3389/fcvm.2024.1399659. This article has 2 citations and is from a peer-reviewed journal.

21. (piroddi2020myocardialoverexpressionof pages 12-13): Nicoletta Piroddi, Paola Pesce, Beatrice Scellini, Stefano Manzini, Giulia S Ganzetti, Ileana Badi, Michela Menegollo, Virginia Cora, Simone Tiso, Raffaella Cinquetti, Laura Monti, Giulia Chiesa, Steven B Bleyl, Marco Busnelli, Federica Dellera, Daniele Bruno, Federico Caicci, Annalisa Grimaldi, Roberto Taramelli, Lucia Manni, David Sacerdoti, Chiara Tesi, Corrado Poggesi, Simonetta Ausoni, Francesco Acquati, and Marina Campione. Myocardial overexpression of ankrd1 causes sinus venosus defects and progressive diastolic dysfunction. Cardiovascular research, 116:1458-1472, Nov 2020. URL: https://doi.org/10.1093/cvr/cvz291, doi:10.1093/cvr/cvz291. This article has 40 citations and is from a domain leading peer-reviewed journal.