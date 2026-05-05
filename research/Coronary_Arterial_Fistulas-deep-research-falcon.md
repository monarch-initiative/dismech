---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T07:43:45.839984'
end_time: '2026-05-05T07:53:20.287328'
duration_seconds: 574.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coronary Arterial Fistulas
  mondo_id: ''
  category: Congenital
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Coronary Arterial Fistulas
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Coronary Arterial Fistulas** covering all of the
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
- **Disease Name:** Coronary Arterial Fistulas
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Coronary Arterial Fistulas** covering all of the
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


## Coronary Arterial Fistulas (CAF): Disease Characteristics Research Report (Congenital)

### Executive summary
Coronary arterial (artery) fistulas (CAFs) are rare congenital (occasionally acquired) coronary anomalies in which an epicardial coronary artery forms an abnormal communication that bypasses the myocardial capillary bed and drains into a cardiac chamber or great vessel/venous circuit, producing variable shunt physiology and potential “coronary steal” with ischemia, arrhythmia, heart failure, endocarditis, aneurysmal degeneration, or incidental/asymptomatic detection. Contemporary practice emphasizes multimodality imaging—especially CT coronary angiography (CTCA) to define origin/course/drainage—followed by individualized management, including transcatheter closure (coils/occluders) for hemodynamically significant or symptomatic lesions. (kumar2023coronaryarteryfistula pages 1-2, li2020coronaryarteryfistulas pages 1-2, kumar2023coronaryarteryfistula pages 2-4)

### Evidence map (recent and key sources)
| Study (first author, year) | Design/Population | Key definitions/notes | Key quantitative results (incidence, success, complications, follow-up) | Clinical implications |
|---|---|---|---|---|
| Kumar, 2023 — *Coronary Artery Fistula: A Diagnostic Dilemma*; Nov 2023; URL: https://doi.org/10.15420/icr.2022.34 | Narrative review of CAF epidemiology, pathophysiology, diagnosis, and management | Defines CAF as a direct communication between an epicardial coronary artery and a cardiac chamber or major intrathoracic vessel; notes most cases are congenital (~90%), but acquired causes are increasingly recognized after PCI, CABG, chest radiation, MI, or vasculitis (kumar2023coronaryarteryfistula pages 1-2, kumar2023coronaryarteryfistula pages 2-4) | Reported incidence: 0.002% in general population; 0.1% among cardiac catheterization patients; present in ~1% of autopsies and 4–15% of young sudden cardiac death cases; states CT coronary angiography has become increasingly important for evaluation and follow-up (kumar2023coronaryarteryfistula pages 1-2, kumar2023coronaryarteryfistula pages 2-4) | Useful synthesis for clinicians: emphasizes coronary steal physiology, multimodality imaging, and individualized management; symptomatic/complicated CAF may need percutaneous or surgical closure, while asymptomatic CAF may be managed conservatively (kumar2023coronaryarteryfistula pages 1-2, kumar2023coronaryarteryfistula pages 2-4) |
| Tabib, 2023 — *Long-term outcome of interventional approaches for treatment of coronary artery fistulas*; Mar 2023; URL: https://doi.org/10.1186/s43044-023-00339-4 | Retrospective cohort; 29 patients treated interventionally at a tertiary center (2009–2019) | CAF described as a rare congenital heart anomaly involving direct connection of a coronary artery to a chamber, coronary sinus/veins, pulmonary artery, or pulmonary veins; 82.9% had isolated CAFs; most drainage was to the right side of the heart (93.1%) (tabib2023longtermoutcomeof pages 1-2, tabib2023longtermoutcomeof pages 2-4) | Mean follow-up 3.3 years (also reported 3.3 ± 2.1 years, range 1–8 years); devices: coils 79.3%, ADO II 18.3%, vascular plug 3.4%, combination 3.4%; postoperative complications in 4 patients (external iliac artery thrombosis, transient PSVT, ST-T changes, mild pericardial effusion), all managed successfully; no coronary injury, device dislocation, dissection, ischemia, coronary dilatation, or death; minimal residual shunt 24.2% closed spontaneously; 17.2% had significant residual shunt closed successfully later (tabib2023longtermoutcomeof pages 1-2, tabib2023longtermoutcomeof pages 2-4) | Supports transcatheter closure as an effective option with low serious complication burden and good medium-term outcomes; retrograde approach was associated with more residual shunts, likely reflecting larger fistulas (tabib2023longtermoutcomeof pages 1-2, tabib2023longtermoutcomeof pages 2-4) |
| Sang, 2024 — *The functional impact on donor vessel following transcatheter closure of coronary artery fistulas—a retrospective study using QFR analysis*; Jul 2024; URL: https://doi.org/10.3389/fcvm.2024.1435025 | Retrospective physiologic/imaging study; 46 patients with 48 CAFs undergoing transcatheter closure (2015–2023) | Focuses on donor-vessel physiology after closure using Quantitative Flow Ratio (QFR); small CAFs generally asymptomatic, whereas medium/large CAFs may cause ischemia, heart failure, arrhythmia, and endocarditis; successful procedure defined as total occlusion or residual shunt with significant flow reduction (sang2024thefunctionalimpact pages 3-5, sang2024thefunctionalimpact pages 2-3, sang2024thefunctionalimpact pages 1-2) | Mean fistula ostium diameter 3.19 ± 1.04 mm; donor vessel diameter 3.45 ± 1.01 mm; baseline QFR lower in medium vs small CAFs (0.93 ± 0.10 vs 0.98 ± 0.03; p<0.05); after occlusion, medium-CAF donor-vessel QFR improved to 0.99 ± 0.01 vs 0.93 ± 0.10 pre-closure (p=0.01), while small CAFs showed no significant QFR change; QFR change greater in medium vs small CAFs (0.06 ± 0.10 vs 0.005 ± 0.012; p=0.01); residual shunt did not significantly alter QFR benefit; most closures used coils (47/48), 1 vascular plug (sang2024thefunctionalimpact pages 3-5, sang2024thefunctionalimpact pages 2-3, sang2024thefunctionalimpact pages 1-2) | Provides recent physiologic evidence that medium CAFs can meaningfully impair donor-vessel flow and may benefit from occlusion; small residual shunts may not negate hemodynamic improvement (sang2024thefunctionalimpact pages 3-5, sang2024thefunctionalimpact pages 7-8, sang2024thefunctionalimpact pages 1-2) |
| Wei, 2024 — *Outcomes of Transcatheter Closure of Congenital Left Circumflex Coronary Artery Fistula*; Aug 2024; URL: https://doi.org/10.1253/circj.cj-23-0800 | Retrospective single-center series; 25 consecutive patients scheduled for transcatheter closure of congenital LCX-CAF (2012–2022) | LCX-CAF is a relatively rare CAF subtype; study highlights technical challenges of LCX anatomy and compares outcomes with LAD-CAF; all patients received anticoagulation or antiplatelet therapy for at least 6 months after closure (wei2024outcomesoftranscatheter pages 1-3) | Mean age 34 ± 20 years; 48% male; mean fistula diameter 6.99 ± 2.04 mm; 84% large fistulas; procedure feasible in 22/25 (reported 77.3%); occluders via transarterial approach in 27.3% and arteriovenous loop in 72.7%; no procedural complications; procedural success similar for single LCX-CAF vs LAD-CAF (81.25% vs 92.86%; P=0.602), but procedure time longer for LCX-CAF (83.06 ± 36.07 vs 36.00 ± 9.49 min; P<0.001); mean follow-up 62.2 ± 45.5 months; myocardial infarction 4.5% (1/22), recanalization 9.1% (2/22) (wei2024outcomesoftranscatheter pages 1-3) | Suggests transcatheter closure is feasible and effective in selected LCX-CAF cases, but anatomy makes procedures more complex and longer; post-closure MI risk warrants continued study of optimal antithrombotic therapy (wei2024outcomesoftranscatheter pages 1-3) |
| Podolec, 2019 — *Presence and characteristics of coronary artery fistulas among patients undergoing coronary angiography*; Nov 2019; URL: https://doi.org/10.33963/kp.14963 | National registry study; 298,558 coronary angiography patients in Poland (2014–2016) | Background epidemiology/anatomy study; defines CAF as abnormal connection between one or more coronary arteries and a heart chamber or great thoracic vessel; mostly congenital, but acquired forms can occur after trauma, infection, or iatrogenic injury (podolec2019presenceandcharacteristics pages 1-2, podolec2019presenceandcharacteristics pages 2-3) | CAF prevalence 0.087% (261/298,558); LAD origin 59.22%, RCA 28.01%, circumflex 12.77%; pulmonary artery most frequent drainage site for LAD- and RCA-origin fistulas; women had higher prevalence than men (0.12% vs 0.07%, P<0.001) (podolec2019presenceandcharacteristics pages 1-2, podolec2019presenceandcharacteristics pages 2-3) | Provides large-scale real-world background on angiographic prevalence and anatomy, useful for contextualizing modern CT and closure series (podolec2019presenceandcharacteristics pages 1-2, podolec2019presenceandcharacteristics pages 2-3) |
| Li, 2020 — *Coronary artery fistulas detected with coronary CT angiography: a pictorial review of 73 cases*; Apr 2020; URL: https://doi.org/10.1259/bjr.20190523 | CT-based case series/review; 21,966 consecutive dual-source CT coronary angiography studies with 73 CAF cases | Imaging-focused background source; defines CAFs as abnormal coronary connections bypassing myocardial capillary bed; >90% congenital; distinguishes coronary-pulmonary artery fistulas and coronary-cameral fistulas; emphasizes CT angiography for detailed anatomy (li2020coronaryarteryfistulas pages 1-2) | CT incidence 0.33% (73/21,966); reported prior incidence ranges 0.05–0.30% for invasive angiography, 0.002% general population, and 0.17–0.9% for CT angiography populations; common origins LM/LAD:RCA:LCX = 30:23:3; multiple origins in 23.3%; drainage to pulmonary trunk 72.6%, RV 12.3%, LV 12.3%, atria 1.4% (li2020coronaryarteryfistulas pages 1-2) | Strong imaging background showing CT detects more incidental/asymptomatic CAFs and better defines origin, course, and drainage for planning intervention and follow-up (li2020coronaryarteryfistulas pages 1-2) |


*Table: This table summarizes key recent and foundational studies on coronary artery fistulas, emphasizing modern diagnosis, anatomy, physiologic impact, and transcatheter closure outcomes. It is useful as a quick evidence map for epidemiology, imaging workup, and management decisions.*

---

## 1. Disease Information

### 1.1 Concise overview and definition
CAF is defined as a “direct communication of the epicardial coronary artery with one of the four chambers or the major vessels of the heart or chest” (review text) (kumar2023coronaryarteryfistula pages 1-2). A closely aligned CT-imaging definition states: “Coronary artery fistulas (CAFs) are abnormal connections of the coronary arteries that bypass the myocardial capillary bed and terminate into chambers of the heart or major blood vessels.” (li2020coronaryarteryfistulas pages 1-2).

**Synonyms / alternative names (used variably in the literature):**
- Coronary artery fistula; coronary arterial fistula (kumar2023coronaryarteryfistula pages 1-2, tabib2023longtermoutcomeof pages 1-2)
- Coronary arteriovenous fistula (CAVF) (li2020coronaryarteryfistulas pages 1-2)
- Coronary-cameral fistula (CCF; fistula to a cardiac chamber) (li2020coronaryarteryfistulas pages 1-2)
- Coronary–pulmonary artery fistula (a common drainage pattern) (li2020coronaryarteryfistulas pages 1-2)

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
The provided full texts did not include standardized identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO). Therefore, identifiers cannot be asserted from the evidence gathered in this run.

### 1.3 Evidence source type
The evidence synthesized here is largely aggregated from:
- Narrative review(s) and imaging review(s) (kumar2023coronaryarteryfistula pages 1-2, li2020coronaryarteryfistulas pages 1-2)
- Registry/observational cohorts (angiography registry, closure cohorts, CT series) (podolec2019presenceandcharacteristics pages 2-3, tabib2023longtermoutcomeof pages 2-4, sang2024thefunctionalimpact pages 1-2, wei2024outcomesoftranscatheter pages 1-3)

---

## 2. Etiology

### 2.1 Primary causes
**Congenital developmental mechanism.** A common mechanistic explanation is persistence/failure of regression of embryonic myocardial sinusoids that normally transform into the capillary network. The review states: “Failure of the regression of the sinusoids leads to fistulous communication between the coronary arteries and the cardiac chambers” (kumar2023coronaryarteryfistula pages 1-2). A CT-focused review similarly notes that if the embryologic sinusoidal spaces persist, “CAF will be formed.” (li2020coronaryarteryfistulas pages 1-2).

**Acquired/iatrogenic causes.** CAFs can be congenital or acquired. The review notes that acquired/sporadic causes (≈10%) are increasingly recognized with rising percutaneous coronary intervention (PCI), coronary artery bypass grafting (CABG), and chest radiation; it also lists myocardial infarction and vasculitis as causes during healing (kumar2023coronaryarteryfistula pages 1-2). A clinical cohort similarly notes acquisition after chest trauma, myectomy, coronary angioplasty, or bypass surgery (tabib2023longtermoutcomeof pages 1-2).

### 2.2 Risk factors
Evidence in the retrieved corpus supports *contextual* risk factors rather than genetic susceptibility loci:
- **Iatrogenic exposure** (PCI/CABG/radiation) and prior myocardial injury/inflammation (MI, vasculitis) (kumar2023coronaryarteryfistula pages 1-2)
- **Association with other congenital cardiac abnormalities**: In one interventional cohort, 17.1% had concurrent congenital abnormalities (e.g., PFO, ASD, single coronary ostium, repaired Tetralogy of Fallot) (tabib2023longtermoutcomeof pages 2-4).

### 2.3 Protective factors / gene–environment interactions
No evidence for genetic protective factors, environmental protective factors, or formal gene–environment interaction studies was found in the retrieved texts.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Common phenotypes and characteristics
CAF presentation ranges from incidental/asymptomatic to complications driven by shunt size, anatomy, and steal physiology.

**Age-related symptom emergence (natural history signal).** The review reports that fistulas are often asymptomatic early but become symptomatic with age: “for age <20 years, only one-fifth of the fistulas are symptomatic, while more than two-thirds of the fistulas are symptomatic after the age of 60 years.” (kumar2023coronaryarteryfistula pages 2-4).

**Symptoms/signs and complications described in reviews and cohorts include:**
- Dyspnea, fatigue, chest discomfort/angina; dizziness/syncope (kumar2023coronaryarteryfistula pages 2-4)
- Heart failure / pulmonary congestion and myocardial infarction depending on shunt/steal (kumar2023coronaryarteryfistula pages 2-4)
- Arrhythmias/conduction abnormalities; endocarditis; valvular regurgitation/papillary muscle dysfunction; rare hemopericardium/cardiac rupture (kumar2023coronaryarteryfistula pages 2-4)
- Volume overload (72.6% in a pediatric interventional cohort), pulmonary hypertension (17.2%) and coronary aneurysm findings (LMCA aneurysm 6.8%; RCA aneurysm 3.4%) (tabib2023longtermoutcomeof pages 2-4)

### 3.2 Suggested HPO terms (examples)
Because HPO codes were not directly provided in the texts, terms below are suggested based on the described phenotypes:
- Chest pain/angina: **HP:0100749 (Chest pain)**
- Dyspnea on exertion: **HP:0002875 (Dyspnea on exertion)**
- Heart failure: **HP:0001635 (Congestive heart failure)**
- Myocardial ischemia: **HP:0001709 (Myocardial ischemia)**
- Myocardial infarction: **HP:0001658 (Myocardial infarction)**
- Arrhythmia: **HP:0011675 (Arrhythmia)**
- Infective endocarditis: **HP:0100587 (Endocarditis)**
- Pulmonary hypertension: **HP:0002092 (Pulmonary hypertension)**
- Continuous murmur (when present): **HP:0030048 (Continuous murmur)**
- Coronary artery aneurysm: **HP:0032300 (Coronary artery aneurysm)**

### 3.3 Quality of life impact
The retrieved texts did not report validated QoL instruments (e.g., SF-36, EQ-5D, PROMIS). Impact is inferred clinically via symptoms (angina/dyspnea/heart failure) but cannot be quantified here.

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and pathogenic variants
No causal genes, pathogenic variants, inheritance patterns, or recurrent syndromic gene associations were reported in the retrieved sources.

### 4.2 Mechanistic developmental biology (molecular-level proxy)
The literature in this run supports a **developmental morphogenesis failure** model (persistence of embryologic sinusoids), but it does not identify specific gene programs (kumar2023coronaryarteryfistula pages 1-2, li2020coronaryarteryfistulas pages 1-2).

### 4.3 Epigenetics, modifier genes, chromosomal abnormalities
No evidence was identified in the retrieved texts.

---

## 5. Mechanism / Pathophysiology

### 5.1 Causal chain (hemodynamic mechanism)
A central mechanism is diversion of high-pressure coronary flow into a low-resistance receiving chamber/vessel, bypassing the myocardial microcirculation. The review states: “The main pathophysiology of CAF is the drainage of high-pressure blood in the arteries into a low-resistance venous system through a channel that bypasses the natural low-pressure small arteriolar and capillary network in the myocardium.” (kumar2023coronaryarteryfistula pages 1-2). This can reduce distal myocardial perfusion (“steal phenomenon”), contributing to exertional angina/ischemia and, with larger shunts, volume overload and pulmonary hypertension/heart failure (kumar2023coronaryarteryfistula pages 2-4, sang2024thefunctionalimpact pages 1-2).

**Physiologic evidence (2024):** A QFR-based study showed that donor vessels supplying **medium** CAFs had lower baseline QFR than those supplying small CAFs (0.93±0.10 vs 0.98±0.03) and that QFR significantly improved after occlusion for medium CAFs (0.99±0.01 vs 0.93±0.10 pre-closure; p=0.01), supporting a functional steal effect reversible by closure (sang2024thefunctionalimpact pages 1-2).

### 5.2 Suggested GO biological process terms (examples)
Based on the reported mechanisms:
- **GO:0001525 angiogenesis** (developmental vascular formation relevant to anomalous communications)
- **GO:0001944 vasculature development**
- **GO:0003015 heart process**
- **GO:0008015 blood circulation**
- **GO:0003013 circulatory system process**
- **GO:0001666 response to hypoxia** / **GO:0001525** (downstream ischemia-related processes; not directly measured molecularly here)

### 5.3 Suggested Cell Ontology (CL) terms (examples)
CAF is primarily an anatomic vascular malformation; implicated cell types in vessel wall and downstream myocardium include:
- **CL:0002543 endothelial cell**
- **CL:0000187 smooth muscle cell**
- **CL:0000746 cardiomyocyte**

---

## 6. Diagnostics

### 6.1 Imaging and diagnostic modalities (current understanding)
**Echocardiography (TTE/TEE).** The review emphasizes TTE’s importance, but notes limited anatomic delineation and states: “Despite this, the diagnostic accuracy is still 35–50%.” (kumar2023coronaryarteryfistula pages 2-4). A closure cohort uses TTE for diagnosis and follow-up and lists typical echo findings (dilated/tortuous coronaries, enlarged chambers, regurgitant flows, diastolic flow reversal in aorta, reduced function) (tabib2023longtermoutcomeof pages 1-2).

**Invasive angiography (IA).** Traditionally a gold standard for defining origin/course and providing hemodynamics; often the initial modality where CAF is found incidentally (kumar2023coronaryarteryfistula pages 2-4).

**CT coronary angiography (CTCA).** The review explicitly states: “CTCA has become the gold standard diagnostic evaluation tool for CAF because of the higher temporal and spatial resolution compared with other imaging modalities.” (kumar2023coronaryarteryfistula pages 2-4). A CT series documents higher detection and detailed 3D anatomic depiction, with more incidental/asymptomatic CAFs found as CT use expands (li2020coronaryarteryfistulas pages 1-2).

**MRI/CMR.** The review notes MRI can delineate anatomy (including 3D MR angiography) but has lower spatial resolution and longer acquisition time than CTCA (kumar2023coronaryarteryfistula pages 2-4).

**Figure evidence (imaging modalities):** Extracted imaging figure panels from the 2023 review illustrate invasive angiography, CTCA confirmation, and MR angiography views for CAF diagnosis (kumar2023coronaryarteryfistula media bbccd634).

### 6.2 Differential diagnosis
The retrieved texts did not provide an explicit differential diagnosis list. In practice, differentials for continuous murmurs/abnormal coronary flow include PDA, arteriovenous malformations, ruptured sinus of Valsalva, anomalous coronary origins with collateralization, and other shunt lesions; however, these cannot be asserted from the evidence collected here.

---

## 7. Epidemiology, demographics, and prognosis

### 7.1 Incidence/prevalence (recently cited statistics)
CAF epidemiology varies by ascertainment method.
- Review-reported estimates: “incidence is only 0.002% in the general population and 0.1% in all cardiac catheterisation patients” (kumar2023coronaryarteryfistula pages 1-2).
- Large angiography registry (Poland; 298,558 angiograms): CAF prevalence 0.087% (261 cases) (podolec2019presenceandcharacteristics pages 2-3).
- CT angiography series (21,966 CTCA studies): 73 CAFs (incidence 0.33%) and a summary of modality-dependent incidence ranges (0.05–0.30% invasive angiography; 0.17–0.9% CTCA cohorts; 0.002% general population) (li2020coronaryarteryfistulas pages 1-2).

### 7.2 Anatomy distribution (origin and drainage)
- Registry: LAD origin 59.22%, RCA 28.01%, circumflex 12.77%; pulmonary artery common drainage, especially for LAD-origin fistulas (podolec2019presenceandcharacteristics pages 2-3).
- CT series: most drain to pulmonary trunk (72.6%), then RV (12.3%) and LV (12.3%) (li2020coronaryarteryfistulas pages 1-2).
- QFR closure study: LAD origin 42%, RCA 50%; drainage PA 54%, LA 33%, RA 8%, RV 4% (sang2024thefunctionalimpact pages 3-5).

### 7.3 Outcomes / prognosis
Prognosis is heterogeneous and anatomy-dependent; modern cohorts support generally favorable procedural safety for selected patients undergoing transcatheter closure.
- Interventional cohort (children; 29 cases, mean follow-up 3.3 years): no deaths; complications in 4 patients, all managed without sequelae; significant residual shunts after first procedure occurred in 17.2% but were closed successfully later; no recurrences reported (tabib2023longtermoutcomeof pages 2-4).
- LCX-CAF transcatheter closure series (adult/predominantly adult, follow-up ~62 months): post-closure myocardial infarction 4.5% (1/22), recanalization 9.1% (2/22) (wei2024outcomesoftranscatheter pages 1-3).

---

## 8. Treatment

### 8.1 Current applications and real-world implementations
**Transcatheter closure (TCC)** is widely implemented for suitable anatomy (e.g., single narrow drainage site, accessible donor vessel), using **coils** and **occluder devices** (e.g., PDA occluder-type devices, vascular plugs). The 2023 cohort reported coils in 79.3% and other occluders less commonly (tabib2023longtermoutcomeof pages 1-2). The 2024 QFR cohort primarily used coils (47/48) (sang2024thefunctionalimpact pages 2-3). The 2024 LCX-CAF series used occluders deployed via transarterial approach or arteriovenous loop (wei2024outcomesoftranscatheter pages 1-3).

**Surgery** remains important for complex anatomy, giant aneurysms, multiple/diffuse fistulas, or when catheter closure is not feasible; however, detailed comparative outcome statistics were not available in the retrieved 2023–2024 texts beyond noting that TCC is “a feasible and effective alternative to surgical repair, with comparable outcomes in selected patients” (wei2024outcomesoftranscatheter pages 1-3).

### 8.2 Indications and expert opinion (from authoritative reviews)
The 2023 review emphasizes individualized decision-making and notes that “Both surgical and percutaneous options are available for symptomatic patients or those with complications, while management of asymptomatic CAF remains a viable alternative.” (kumar2023coronaryarteryfistula pages 1-2). It also reports that antibiotic prophylaxis is recommended once diagnosed (kumar2023coronaryarteryfistula pages 2-4).

### 8.3 Recent data highlights (2023–2024)
- **Functional impact / ischemia physiology:** Medium CAFs demonstrated significant donor-vessel QFR improvement after closure, supporting closure when medium lesions are physiologically important (sang2024thefunctionalimpact pages 1-2).
- **Long-term interventional outcomes (single center):** Minimal residual shunts can close spontaneously; major coronary injury/dissection/ischemia were not observed in a 29-patient cohort (tabib2023longtermoutcomeof pages 2-4).
- **LCX-CAF outcomes:** Feasibility 77.3% (22/25); no procedural complications; MI 4.5% and recanalization 9.1% over ~5 years of follow-up (wei2024outcomesoftranscatheter pages 1-3).

### 8.4 Suggested MAXO terms (examples)
- Transcatheter embolization/occlusion: **MAXO:0000517 (Embolization therapy)** (suggested)
- Cardiac catheterization procedure: **MAXO:0000506 (Cardiac catheterization)** (suggested)
- Surgical ligation/repair of fistula: **MAXO:0000127 (Surgical procedure)** / **MAXO:0000004 (Surgical repair)** (suggested)
- Antiplatelet/anticoagulation therapy (post-closure): **MAXO:0000473 (Anticoagulant therapy)** / **MAXO:0000515 (Antiplatelet therapy)** (suggested)

---

## 9. Prevention

### 9.1 Primary prevention
For congenital CAF, primary prevention is not established in the retrieved evidence.

### 9.2 Secondary/tertiary prevention (complication prevention)
Evidence supports surveillance and anatomy-guided management to prevent ischemia, heart failure, and endocarditis complications (kumar2023coronaryarteryfistula pages 1-2, kumar2023coronaryarteryfistula pages 2-4). For acquired CAF, reducing iatrogenic injury risk during PCI/CABG and monitoring after chest radiation/MI/vasculitis is implicated but not quantified (kumar2023coronaryarteryfistula pages 1-2).

---

## 10. Other species / natural disease & model organisms
No evidence regarding naturally occurring CAF in non-human species, nor dedicated model organisms, was identified in the retrieved texts.

---

## 11. Data gaps and limitations of this evidence synthesis
- Administrative/ontology identifiers (MONDO/MeSH/ICD/OMIM/Orphanet) were not available in the retrieved full texts.
- The retrieved 2023–2024 sources did not report genetics/variant-level associations.
- Differential diagnosis and standardized diagnostic criteria were not explicitly enumerated in the retrieved texts.
- QoL instruments and population-level prospective natural history data were not found in the accessed set.

---

## Appendix: Key quoted abstract/text statements (verbatim)
- “Coronary artery fistula (CAF) is a false vascular channel; that is, a direct communication of the epicardial coronary artery with one of the four chambers or the major vessels of the heart or chest.” (kumar2023coronaryarteryfistula pages 1-2)
- “CTCA has become the gold standard diagnostic evaluation tool for CAF because of the higher temporal and spatial resolution compared with other imaging modalities.” (kumar2023coronaryarteryfistula pages 2-4)
- “Despite this, the diagnostic accuracy is still 35–50%.” (echocardiography accuracy statement) (kumar2023coronaryarteryfistula pages 2-4)
- “Coronary artery fistulas (CAFs) are abnormal connections of the coronary arteries that bypass the myocardial capillary bed and terminate into chambers of the heart or major blood vessels.” (li2020coronaryarteryfistulas pages 1-2)
- QFR study conclusion: “A small  residual shunt has no significant impact on the effectiveness of CAFs occlusion in enhancing donor blood flow.” (sang2024thefunctionalimpact pages 1-2)



References

1. (kumar2023coronaryarteryfistula pages 1-2): Rajesh Kumar, Jathinder Kumar, Cormac O’Connor, Ihsan Ullah, Benjamin Tyrell, Ian Pearson, Sajjad Matiullah, and Kevin Bainey. Coronary artery fistula: a diagnostic dilemma. Interventional Cardiology: Reviews, Research, Resources, Nov 2023. URL: https://doi.org/10.15420/icr.2022.34, doi:10.15420/icr.2022.34. This article has 31 citations.

2. (li2020coronaryarteryfistulas pages 1-2): Ning Li, Peng Zhao, Dawei Wu, and Changhu Liang. Coronary artery fistulas detected with coronary ct angiography: a pictorial review of 73 cases. The British journal of radiology, 93:20190523, Apr 2020. URL: https://doi.org/10.1259/bjr.20190523, doi:10.1259/bjr.20190523. This article has 29 citations.

3. (kumar2023coronaryarteryfistula pages 2-4): Rajesh Kumar, Jathinder Kumar, Cormac O’Connor, Ihsan Ullah, Benjamin Tyrell, Ian Pearson, Sajjad Matiullah, and Kevin Bainey. Coronary artery fistula: a diagnostic dilemma. Interventional Cardiology: Reviews, Research, Resources, Nov 2023. URL: https://doi.org/10.15420/icr.2022.34, doi:10.15420/icr.2022.34. This article has 31 citations.

4. (tabib2023longtermoutcomeof pages 1-2): Avisa Tabib, Hojjat Mortezaeian, Mohammad Mahdavi, Yasaman Khalili, Nikolaus A. Haas, and Sepideh Mohammadhoseini. Long-term outcome of interventional approaches for treatment of coronary artery fistulas: a retrospective cohort study in a great referral center. The Egyptian Heart Journal, Mar 2023. URL: https://doi.org/10.1186/s43044-023-00339-4, doi:10.1186/s43044-023-00339-4. This article has 2 citations.

5. (tabib2023longtermoutcomeof pages 2-4): Avisa Tabib, Hojjat Mortezaeian, Mohammad Mahdavi, Yasaman Khalili, Nikolaus A. Haas, and Sepideh Mohammadhoseini. Long-term outcome of interventional approaches for treatment of coronary artery fistulas: a retrospective cohort study in a great referral center. The Egyptian Heart Journal, Mar 2023. URL: https://doi.org/10.1186/s43044-023-00339-4, doi:10.1186/s43044-023-00339-4. This article has 2 citations.

6. (sang2024thefunctionalimpact pages 3-5): Zhenchi Sang, Qingqi Ji, Huan Tong, Linghong Shen, Xiaolong Wang, and Ben He. The functional impact on donor vessel following transcatheter closure of coronary artery fistulas—a retrospective study using qfr analysis. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1435025, doi:10.3389/fcvm.2024.1435025. This article has 1 citations and is from a peer-reviewed journal.

7. (sang2024thefunctionalimpact pages 2-3): Zhenchi Sang, Qingqi Ji, Huan Tong, Linghong Shen, Xiaolong Wang, and Ben He. The functional impact on donor vessel following transcatheter closure of coronary artery fistulas—a retrospective study using qfr analysis. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1435025, doi:10.3389/fcvm.2024.1435025. This article has 1 citations and is from a peer-reviewed journal.

8. (sang2024thefunctionalimpact pages 1-2): Zhenchi Sang, Qingqi Ji, Huan Tong, Linghong Shen, Xiaolong Wang, and Ben He. The functional impact on donor vessel following transcatheter closure of coronary artery fistulas—a retrospective study using qfr analysis. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1435025, doi:10.3389/fcvm.2024.1435025. This article has 1 citations and is from a peer-reviewed journal.

9. (sang2024thefunctionalimpact pages 7-8): Zhenchi Sang, Qingqi Ji, Huan Tong, Linghong Shen, Xiaolong Wang, and Ben He. The functional impact on donor vessel following transcatheter closure of coronary artery fistulas—a retrospective study using qfr analysis. Frontiers in Cardiovascular Medicine, Jul 2024. URL: https://doi.org/10.3389/fcvm.2024.1435025, doi:10.3389/fcvm.2024.1435025. This article has 1 citations and is from a peer-reviewed journal.

10. (wei2024outcomesoftranscatheter pages 1-3): Peijian Wei, Fang Fang, Fengwen Zhang, Yihang Li, Pengxu Kong, Shuyi Feng, Zhongying Xu, Liang Xu, Junyi Wan, Gejun Zhang, and Xiangbin Pan. Outcomes of transcatheter closure of congenital left circumflex coronary artery fistula. Circulation Journal, 88:1383-1390, Aug 2024. URL: https://doi.org/10.1253/circj.cj-23-0800, doi:10.1253/circj.cj-23-0800. This article has 4 citations and is from a peer-reviewed journal.

11. (podolec2019presenceandcharacteristics pages 1-2): Jakub Podolec, Łukasz Wiewiórka, Zbigniew Siudak, Krzysztof Malinowski, Krzysztof Bartuś, Dariusz Dudek, Krzysztof Żmudka, and Jacek Legutko. Presence and characteristics of coronary artery fistulas among patients undergoing coronary angiography. Kardiologia Polska, 77:1034-1039, Nov 2019. URL: https://doi.org/10.33963/kp.14963, doi:10.33963/kp.14963. This article has 18 citations and is from a peer-reviewed journal.

12. (podolec2019presenceandcharacteristics pages 2-3): Jakub Podolec, Łukasz Wiewiórka, Zbigniew Siudak, Krzysztof Malinowski, Krzysztof Bartuś, Dariusz Dudek, Krzysztof Żmudka, and Jacek Legutko. Presence and characteristics of coronary artery fistulas among patients undergoing coronary angiography. Kardiologia Polska, 77:1034-1039, Nov 2019. URL: https://doi.org/10.33963/kp.14963, doi:10.33963/kp.14963. This article has 18 citations and is from a peer-reviewed journal.

13. (kumar2023coronaryarteryfistula media bbccd634): Rajesh Kumar, Jathinder Kumar, Cormac O’Connor, Ihsan Ullah, Benjamin Tyrell, Ian Pearson, Sajjad Matiullah, and Kevin Bainey. Coronary artery fistula: a diagnostic dilemma. Interventional Cardiology: Reviews, Research, Resources, Nov 2023. URL: https://doi.org/10.15420/icr.2022.34, doi:10.15420/icr.2022.34. This article has 31 citations.