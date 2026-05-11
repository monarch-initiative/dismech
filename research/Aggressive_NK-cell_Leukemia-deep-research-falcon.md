---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T13:52:57.324944'
end_time: '2026-05-11T14:04:19.824446'
duration_seconds: 682.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aggressive NK-cell Leukemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aggressive NK-cell Leukemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Aggressive NK-cell Leukemia** covering all of the
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
- **Disease Name:** Aggressive NK-cell Leukemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Aggressive NK-cell Leukemia** covering all of the
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


# Aggressive NK-cell Leukemia (ANKL) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Aggressive NK-cell leukemia (ANKL)
- **Category:** Mature NK-cell neoplasm; EBV-associated T/NK-cell neoplasia spectrum
- **MONDO ID:** Not available from the retrieved sources in this run (needs dedicated ontology lookup outside the current evidence set).

## Evidence summary table
| Domain | Key points | Quantitative data | Key source (with year, journal) | URL |
|---|---|---|---|---|
| Definition / classification | ANKL is a rare, fulminant, systemic mature NK-cell neoplasm with acute presentation and grave prognosis; recent reviews note it remains recognized in modern WHO/ICC-era classification of mature T/NK-cell neoplasms. It is distinct from extranodal NK/T-cell lymphoma, though overlap exists in disseminated disease. (hussein2020aggressivenkcell pages 1-3, spaner2024casereportaggressive pages 1-2, ferry2024maturebt pages 8-10) | Median age around 40 years in review cohorts; fewer than 500 cases reported overall in literature summaries. (hussein2020aggressivenkcell pages 1-3, spaner2024casereportaggressive pages 1-2) | El Hussein et al., 2020, *Cancers*; Spaner et al., 2024, *Frontiers in Hematology*; Ferry et al., 2024, *J Hematol Oncol* | https://doi.org/10.3390/cancers12102900 |
| EBV association | EBV is strongly associated with ANKL and is detectable in most cases by EBER; however, EBV-negative ANKL exists and can show similar clinicopathologic features. ANKL often sits within the spectrum of EBV-associated T/NK-cell lymphoproliferative diseases. (hussein2020genomicandimmunophenotypic pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, tang2017aggressivenkcellleukemia pages 1-2, hussein2020aggressivenkcell pages 3-5) | ~90% EBV-driven in a 2024 case review; ~10% EBV-negative in older review; EBER positive in 9/12 cases in one clinicopathologic series. (spaner2024casereportaggressive pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, hussein2020genomicandimmunophenotypic pages 1-2) | Hussein et al., 2020, *Am J Surg Pathol*; Ishida, 2018, *Front Pediatr*; Spaner et al., 2024, *Front Hematol* | https://doi.org/10.1097/pas.0000000000001518 |
| Typical presentation / phenotypes | Common features include fever, constitutional symptoms, hepatosplenomegaly, liver dysfunction, leukemic blood picture, cytopenias, HLH/hemophagocytosis, DIC/coagulopathy, and multiorgan failure; nasal/skin lesions are less common than marrow, blood, liver, and spleen involvement. (hussein2020aggressivenkcell pages 1-3, ni2024clinicopathologicalfeaturesand pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, spaner2024casereportaggressive pages 1-2) | HLH reported in ~60–90% in pediatric case literature summary; in one 12-case series, HLH in 2/12; common involved organs include marrow, peripheral blood, liver, spleen, lymph nodes. (ni2024clinicopathologicalfeaturesand pages 1-2, hussein2020genomicandimmunophenotypic pages 1-2) | Ni et al., 2024, *Turkish Journal of Pediatrics*; El Hussein et al., 2020, *Cancers*; Ishida, 2018, *Front Pediatr* | https://doi.org/10.24953/turkjpediatr.2024.5072 |
| Diagnostic immunophenotype | Characteristic phenotype is NK-lineage with surface CD3 negative and cytoplasmic CD3ε positive; typically CD56+, CD2+, CD94+, cytotoxic marker positive (granzyme B, TIA1, perforin), usually negative for CD4, CD5, CD57, TCR αβ/γδ, and often lacking KIR expression. Bone marrow involvement may be interstitial or sinusoidal/intrasinusoidal. (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020aggressivenkcell pages 3-5, hussein2020genomicandimmunophenotypic pages 2-3) | In one 12-case series: CD56+ 12/12, CD94+ 9/9, CD2+ 10/12, EBER+ 9/12; negative in all tested for surface CD3 12/12, CD5 11/11, CD57 9/9, TCRαβ 11/11, TCRγδ 11/11. Marrow ANKL fraction ranged 1.5% to 96.4%, median 22.5%. (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020genomicandimmunophenotypic pages 2-3) | El Hussein et al., 2020, *Am J Surg Pathol* | https://doi.org/10.1097/pas.0000000000001518 |
| Genetics / pathways | Recurrent alterations cluster in JAK/STAT activation, epigenetic dysregulation, TP53/DNA-repair impairment, and RAS/MAPK signaling; IL10-STAT3-MYC biosynthetic axis and HACE1 hypermethylation have been implicated. (hussein2020aggressivenkcell pages 1-3, ishida2018aggressivenkcellleukemia pages 1-2, tang2017aggressivenkcellleukemia pages 1-2, dufva2018aggressivenaturalkillercell pages 3-4) | Dufva et al.: STAT3 21%, RAS-MAPK genes 21%, DDX3X 29%, epigenetic modifiers 50%; copy-gain/mutation events affecting JAK2/STAT3/STAT5B also reported. Other summaries report TP53 34%, TET2 28%, CREBBP 21%, MLL2/KMT2D 21%, JAK-STAT pathway alterations ~48%, STAT3 mutations ~17%. (dufva2018aggressivenaturalkillercell pages 3-4, ishida2018aggressivenkcellleukemia pages 1-2, sumbly2022aggressivenaturalkiller pages 2-3) | Dufva et al., 2018, *Nat Commun*; Ishida, 2018, *Front Pediatr*; Sumbly et al., 2022, *Cureus* | https://doi.org/10.1038/s41467-018-03987-2 |
| Epidemiology / demographics | ANKL is very rare, with geographic enrichment in Asian and Central/South American populations; most patients are young to middle-aged adults, though pediatric and older adult cases occur. Male predominance is reported in some cohorts. (hussein2020aggressivenkcell pages 1-3, ishida2018aggressivenkcellleukemia pages 1-2, tang2017aggressivenkcellleukemia pages 1-2) | Chinese multicenter cohort: age peak 21–30 years was 29.2% (33/113); male:female ratio nearly 2:1 in that decade. Western clinicopathologic series: median age 47.5 years, 9 men/3 women. (tang2017aggressivenkcellleukemia pages 1-2, hussein2020genomicandimmunophenotypic pages 1-2) | Tang et al., 2017, *Blood Cancer Journal*; El Hussein et al., 2020, *Am J Surg Pathol* | https://doi.org/10.1038/s41408-017-0021-z |
| Prognosis | Prognosis is extremely poor without effective induction and consolidation; many reviews cite median survival under 2–3 months. A subacute subtype with prolonged prodrome may have better outcomes than classic fulminant ANKL. (hussein2020aggressivenkcell pages 1-3, ni2024clinicopathologicalfeaturesand pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, tang2017aggressivenkcellleukemia pages 1-2, spaner2024casereportaggressive pages 1-2) | Median OS 55 days and 1-year survival 4.42% (5/113) in a large cohort; median survival 2 months in a 12-case Western series; review summaries report median survival <2 to <3 months. (tang2017aggressivenkcellleukemia pages 1-2, hussein2020genomicandimmunophenotypic pages 1-2, ni2024clinicopathologicalfeaturesand pages 1-2) | Tang et al., 2017, *Blood Cancer Journal*; El Hussein et al., 2020, *Am J Surg Pathol*; Ni et al., 2024, *Turkish Journal of Pediatrics* | https://doi.org/10.1038/s41408-017-0021-z |
| Treatment: asparaginase-based therapy | Anthracycline-only approaches are generally ineffective; L-asparaginase/pegaspargase-containing regimens are the main active induction strategy. Regimens used include SMILE, AspaMetDex, L-GemOx, and related protocols. (ni2024clinicopathologicalfeaturesand pages 1-2, tang2017aggressivenkcellleukemia pages 1-2) | In Tang et al., among 13 newly diagnosed patients treated with AspaMetDex alone: CR 30.77% (4/13), ORR 76.92% (10/13), median OS 115 days; grade 3–4 hematologic AEs in 53.84% (7/13). Ni et al. summarize chemotherapy CR rate as <36%. (tang2017aggressivenkcellleukemia pages 1-2, ni2024clinicopathologicalfeaturesand pages 1-2) | Tang et al., 2017, *Blood Cancer Journal*; Ni et al., 2024, *Turkish Journal of Pediatrics* | https://doi.org/10.1038/s41408-017-0021-z |
| Treatment: allo-HSCT / outcomes | Allogeneic HSCT is the only modality consistently associated with durable survival in fit responders and is typically pursued after remission induction with asparaginase-based chemotherapy. (tang2017aggressivenkcellleukemia pages 1-2, ni2024clinicopathologicalfeaturesand pages 1-2) | In Tang et al., 7 patients underwent allo-HSCT after CR; median time to transplant 73 days, median OS 300 days, 2-year OS 42.86% (3/7). Ni et al. summarize ~55.5% relapse/progression within 1 year after allo-HSCT. (tang2017aggressivenkcellleukemia pages 1-2, ni2024clinicopathologicalfeaturesand pages 1-2) | Tang et al., 2017, *Blood Cancer Journal*; Ni et al., 2024, *Turkish Journal of Pediatrics* | https://doi.org/10.1038/s41408-017-0021-z |
| Emerging / targeted therapy rationale | Genomic profiling and drug sensitivity studies support investigation of JAK inhibitors, BCL2 inhibition, and immune checkpoint blockade in selected cases, especially where JAK/STAT activation or PD-L1 expression is present. These remain emerging rather than standard ANKL therapies. (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020aggressivenkcell pages 1-3, dufva2018aggressivenaturalkillercell pages 3-4) | pSTAT3 positivity in 3/8 and PD-L1 positivity in 2/8 in one immunophenotypic series; Dufva et al. found NK malignancies highly sensitive to JAK and BCL2 inhibition in drug profiling. (hussein2020genomicandimmunophenotypic pages 1-2, dufva2018aggressivenaturalkillercell pages 3-4) | El Hussein et al., 2020, *Am J Surg Pathol*; Dufva et al., 2018, *Nat Commun* | https://doi.org/10.1038/s41467-018-03987-2 |


*Table: This table condenses core disease facts for aggressive NK-cell leukemia, including classification, EBV association, presentation, diagnostic phenotype, genomics, prognosis, and treatment outcomes. It is useful as a quick evidence-backed reference for building a disease knowledge base entry.*

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
Aggressive NK-cell leukemia (ANKL) is a rare, fulminant systemic malignancy of mature natural killer (NK) cells with acute presentation, frequent cytokine-driven inflammatory complications (e.g., HLH), and very poor survival without rapid disease control and consolidation. Reviews emphasize that its acute clinical syndrome overlaps with other entities (notably EBV-associated lymphoproliferative disorders and NK/T-cell lymphomas), complicating early recognition and resulting in delayed diagnosis and treatment. (hussein2020aggressivenkcell pages 1-3, spaner2024casereportaggressive pages 1-2)

**Direct abstract quote (example):** “Aggressive natural killer cell leukemia (ANKL) is a rare, aggressive hematologic malignancy which often presents as fulminant Epstein-Barr virus (EBV)- driven hemophagocytic lymphohistiocytosis (HLH).” (spaner2024casereportaggressive pages 1-2)

### 1.2 Key identifiers and ontologies
- **WHO/ICC framing:** The current hematopathology ecosystem includes WHO-HAEM5 (2022) and ICC (2022); comparative reviews summarize entity families and naming across systems. A classification comparison review provides the context that WHO-HAEM5 and ICC are the operative modern frameworks for mature B/T/NK neoplasms, and that EBV-positive T/NK entities are explicitly treated as a family. (ferry2024maturebt pages 8-10)
- **ICD/MeSH/OMIM/Orphanet:** Not extractable from the current retrieved evidence set; these require targeted queries to OMIM/Orphanet/MeSH.

### 1.3 Synonyms / alternative names
- “Aggressive NK-cell leukemia” (most common)
- “Aggressive NK-cell leukaemia” (UK spelling)
- Some literature uses “aggressive NK-cell leukemia/lymphoma” in broader discussions of NK-cell malignancies. (ishida2018aggressivenkcellleukemia pages 1-2, NCT03623087 chunk 1)

### 1.4 Evidence source types in this report
- **Aggregated disease-level resources:** pathology/oncology reviews and classification comparison reviews (hussein2020aggressivenkcell pages 1-3, ferry2024maturebt pages 8-10)
- **Human clinical primary studies:** multicenter cohort (n=113) (tang2017aggressivenkcellleukemia pages 1-2), clinicopathologic series with IHC/NGS (n=12) (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020genomicandimmunophenotypic pages 2-3)
- **Human genomic/translational primary studies:** WES + drug profiling (n=14) (dufva2018aggressivenaturalkillercell pages 3-4, dufva2018aggressivenaturalkillercell media 01c6d37e, dufva2018aggressivenaturalkillercell media 2b03bded)
- **Case-based recent literature (2024):** adolescent/pediatric cases emphasizing HLH and diagnostic delays (ni2024clinicopathologicalfeaturesand pages 1-2, spaner2024casereportaggressive pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors

#### Epstein–Barr virus (EBV) association
ANKL is commonly EBV-associated, with EBER positivity in the majority of cases in multiple series, and many reviews describing EBV as a driver in ~90% of cases (though EBV-negative ANKL exists). (hussein2020genomicandimmunophenotypic pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, spaner2024casereportaggressive pages 1-2)

- **Clinicopathologic series:** EBER was positive in 9/12 ANKL cases. (hussein2020genomicandimmunophenotypic pages 1-2)
- **Review synthesis:** ~10% EBV-negative in one review; EBV-negative cases may present in middle-aged adults and can resemble EBV-positive ANKL clinically/pathologically. (ishida2018aggressivenkcellleukemia pages 1-2, sumbly2022aggressivenaturalkiller pages 2-3)

### 2.2 Risk factors
- **Geography/ancestry:** Cohort and review literature repeatedly notes predilection for Asian populations and Central/South America, consistent with EBV-associated NK/T neoplasia geography. (hussein2020aggressivenkcell pages 1-3, tang2017aggressivenkcellleukemia pages 1-2)
- **Pre-existing EBV-associated immune dysregulation:** Several 2024 reports frame ANKL as arising in/with EBV-driven HLH contexts and discuss overlap with chronic active EBV disease in differential diagnosis. (spaner2024casereportaggressive pages 1-2)

**Note:** Specific germline genetic susceptibility loci or robust environmental risk factors were not retrievable from the current evidence set.

### 2.3 Protective factors
No protective factors (genetic or environmental) were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not established in retrieved evidence; EBV infection is a biological exposure interacting with host immune status and tumor genetics, but formal GxE data were not found here.

---

## 3. Phenotypes (clinical features)

### 3.1 Core phenotype spectrum
ANKL commonly presents with an acute systemic inflammatory and hematologic syndrome including:
- **Fever / constitutional symptoms** (symptom)
- **Hepatosplenomegaly** (clinical sign)
- **Cytopenias and leukemic blood picture** (laboratory abnormality)
- **Liver dysfunction / acute liver injury** (laboratory and organ phenotype)
- **Coagulopathy / DIC** (laboratory abnormality, complication)
- **Hemophagocytic lymphohistiocytosis (HLH)** (immune dysregulation syndrome)
- **Multiorgan failure** in severe/refractory disease
These are repeatedly highlighted across reviews, cohorts, and 2024 case literature. (hussein2020aggressivenkcell pages 1-3, ni2024clinicopathologicalfeaturesand pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, spaner2024casereportaggressive pages 1-2, hussein2020genomicandimmunophenotypic pages 2-3)

**Direct abstract quotes (examples):**
- “Patients commonly present acutely with fever, constitutional symptoms, hepatosplenomegaly, and often disseminated intravascular coagulation or hemophagocytic syndrome.” (sumbly2022aggressivenaturalkiller pages 2-3)
- “HLH can serve as the initial manifestation of ANKL.” (ni2024clinicopathologicalfeaturesand pages 1-2)

### 3.2 Age of onset, severity, progression
- **Typical onset:** young to middle-aged adults; however, pediatric/adolescent cases occur. (ni2024clinicopathologicalfeaturesand pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2, tang2017aggressivenkcellleukemia pages 1-2)
- **Course:** fulminant/rapidly progressive in most patients; a “subacute” clinical subtype with prolonged IM-like prodrome (>90 days; median 115 days) was identified in a large cohort. (tang2017aggressivenkcellleukemia pages 2-4)

### 3.3 Frequency (where available)
- **HLH frequency:** A 2024 pediatric-focused review notes HLH is common; in a separate case-literature preprint, HLH co-occurrence is described as frequent; quantitative, cohort-level HLH prevalence was not consistently extractable from all sources here. (ni2024clinicopathologicalfeaturesand pages 1-2)

### 3.4 Quality of life impact
Formal QoL instruments (EQ-5D/SF-36/PROMIS) were not identified in retrieved evidence. Clinical impact is inferred from fulminant symptoms, ICU-level complications (DIC, multiorgan failure), and extremely short survival. (hussein2020aggressivenkcell pages 1-3, tang2017aggressivenkcellleukemia pages 1-2)

### 3.5 Suggested HPO terms (non-exhaustive)
- Fever **HP:0001945**
- Hepatosplenomegaly **HP:0001433** (or hepatomegaly HP:0002240; splenomegaly HP:0001744)
- Pancytopenia **HP:0001876**
- Thrombocytopenia **HP:0001873**
- Elevated lactate dehydrogenase **HP:0003236**
- Disseminated intravascular coagulation **HP:0001907**
- Hemophagocytic lymphohistiocytosis **HP:0031425**
- Acute liver failure **HP:0006557** / abnormal liver function tests **HP:0002910**

---

## 4. Genetic / molecular information

### 4.1 Causal genes
ANKL is **not** a monogenic germline disorder in the retrieved evidence. It is characterized by **somatic** alterations and pathway dysregulation.

### 4.2 Recurrently altered genes and pathways (with frequencies)
Multiple sources converge on three major molecular themes: **JAK/STAT activation**, **epigenetic dysregulation**, and **TP53/DNA repair impairment**, with additional contribution from **RAS/MAPK** signaling. (hussein2020aggressivenkcell pages 1-3, dufva2018aggressivenaturalkillercell pages 3-4)

#### JAK/STAT pathway
- WES study (n=14): **STAT3 mutations ~21%**; copy-number and other alterations implicating JAK/STAT signaling were emphasized. (dufva2018aggressivenaturalkillercell pages 3-4)
- Review synthesis: JAK-STAT pathway alterations reported ~48% overall in some summaries. (sumbly2022aggressivenaturalkiller pages 2-3)

Visual evidence from Dufva et al. shows JAK-STAT component alterations and copy-number gains and summarizes frequencies across cohorts (including JAK2/STAT3/STAT5 alterations). (dufva2018aggressivenaturalkillercell media 01c6d37e, dufva2018aggressivenaturalkillercell media 2b03bded)

#### Epigenetic modifiers
- WES study: epigenetic modifier mutations reported in **~50%**. (dufva2018aggressivenaturalkillercell pages 3-4)
- Review synthesis lists **TET2 (28%)**, **CREBBP (21%)**, **MLL2/KMT2D (21%)** among recurrent events in a summarized cohort. (sumbly2022aggressivenaturalkiller pages 2-3, ishida2018aggressivenkcellleukemia pages 1-2)

#### TP53 pathway
- Review synthesis reports **TP53 mutations ~34%**. (sumbly2022aggressivenaturalkiller pages 2-3, ishida2018aggressivenkcellleukemia pages 1-2)
- A large cohort found TP53 mutations enriched in classic (fulminant) ANKL (37.93%, 11/29 in sequenced classic ANKL), absent in subacute ANKL subtype in that cohort’s sequencing subset. (tang2017aggressivenkcellleukemia pages 2-4)
- Clinicopathologic series: aberrant p53 expression was common (7/8 by IHC), with TP53 mutations detected in 3/6 in the NGS subset. (hussein2020genomicandimmunophenotypic pages 1-2)

#### DDX3X and RAS/MAPK
- WES study: **DDX3X ~29%**, **RAS-MAPK pathway genes ~21%**. (dufva2018aggressivenaturalkillercell pages 3-4)

### 4.3 Epigenetics
ANKL epigenetic dysregulation is supported by recurrent mutations in epigenetic modifiers and literature noting methylation events (e.g., HACE1 hypermethylation mentioned in the large cohort background). (tang2017aggressivenkcellleukemia pages 1-2, hussein2020aggressivenkcell pages 1-3)

### 4.4 Chromosomal abnormalities
Clonal cytogenetic abnormalities are reported in clinical series (5/12 in one series). (hussein2020genomicandimmunophenotypic pages 1-2)

### 4.5 Mechanistic chain (pathophysiology synthesis)
A plausible causal chain supported by current evidence is:
1) EBV infection of NK lineage cells (EBER+) and/or host immune dysregulation contributes to transformation and/or inflammatory phenotype. (hussein2020genomicandimmunophenotypic pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2)
2) Somatic alterations (JAK/STAT activation; epigenetic modifier and TP53 pathway lesions; RAS/MAPK) promote malignant proliferation, survival, and immune evasion. (dufva2018aggressivenaturalkillercell pages 3-4, tang2017aggressivenkcellleukemia pages 2-4)
3) NK-cell cytokine programs and pathway-driven transcriptional changes (including IL10–STAT3–MYC axis described in reviews) contribute to “cytokine storm” physiology and HLH-like systemic inflammation. (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020aggressivenkcell pages 3-5)
4) Downstream manifestations include cytopenias, HLH, DIC, liver dysfunction, and multiorgan failure, driving high early mortality. (hussein2020aggressivenkcell pages 1-3, tang2017aggressivenkcellleukemia pages 1-2)

### 4.6 Suggested ontology terms
- **GO biological process (examples):** JAK-STAT cascade (GO:0007259), cytokine-mediated signaling pathway (GO:0019221), regulation of apoptotic process (GO:0042981), leukocyte proliferation (GO:0070661)
- **Cell Ontology (CL) (examples):** natural killer cell **CL:0000623**; malignant NK cell (no single CL term; represent as NK cell + neoplastic context)

---

## 5. Environmental information

### Infectious agents
- **EBV (Epstein–Barr virus)** is the central infectious association; tumor EBER positivity is common. (hussein2020genomicandimmunophenotypic pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2)

Other environmental and lifestyle associations were not identified in retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Molecular pathways (high-confidence)
- **JAK/STAT signaling activation** as a recurring pathway with STAT3/STAT5 and copy-number events. (dufva2018aggressivenaturalkillercell pages 3-4, dufva2018aggressivenaturalkillercell media 01c6d37e, dufva2018aggressivenaturalkillercell media 2b03bded)
- **Epigenetic dysregulation** (TET2/CREBBP/KMT2D and other epigenetic modifiers). (sumbly2022aggressivenaturalkiller pages 2-3, dufva2018aggressivenaturalkillercell pages 3-4)
- **TP53 impairment** (mutation and/or aberrant protein expression). (hussein2020genomicandimmunophenotypic pages 1-2, tang2017aggressivenkcellleukemia pages 2-4)
- **RAS/MAPK activation** subset. (dufva2018aggressivenaturalkillercell pages 3-4)

### 6.2 Immune involvement
ANKL frequently presents with HLH and systemic inflammation; NK lineage biology (cytokine secretion programs) is implicated as a contributor to cytokine storm physiology in reviews. (hussein2020aggressivenkcell pages 3-5, spaner2024casereportaggressive pages 1-2)

### 6.3 Molecular profiling / multi-omics
- **Genomics:** WES and targeted sequencing characterize recurrent pathways; Dufva et al. provides integrated genomics + drug sensitivity profiling highlighting pathway vulnerabilities. (dufva2018aggressivenaturalkillercell pages 3-4)

**Not found in retrieved evidence:** single-cell or spatial transcriptomics dedicated to ANKL.

---

## 7. Anatomical structures affected

### 7.1 Organ level
Commonly involved sites include **bone marrow and peripheral blood**, with frequent involvement of **liver and spleen**; lymph nodes may be involved; less commonly skin/soft tissue/lung are described in recent pediatric case review. (ni2024clinicopathologicalfeaturesand pages 1-2, ishida2018aggressivenkcellleukemia pages 1-2)

### 7.2 Tissue/cell level
- Targeted population: **neoplastic NK cells** infiltrating marrow and other organs. (hussein2020genomicandimmunophenotypic pages 1-2)

### 7.3 Suggested UBERON terms (examples)
- Bone marrow: **UBERON:0002371**
- Spleen: **UBERON:0002106**
- Liver: **UBERON:0002107**
- Peripheral blood: **UBERON:0000178**

---

## 8. Temporal development

### 8.1 Onset pattern
Often **acute** with rapidly progressive systemic illness prompting “acute leukemia” evaluation. (hussein2020genomicandimmunophenotypic pages 2-3)

### 8.2 Progression
A large cohort distinguished:
- **Classic ANKL:** fulminant presentation and very short OS.
- **Subacute ANKL subtype:** prolonged prodromal IM-like phase >90 days (median 115 days) before fulminant onset, with survival advantage and differing TP53 mutation enrichment. (tang2017aggressivenkcellleukemia pages 2-4)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Robust population incidence/prevalence rates were not found in the retrieved evidence (likely due to rarity and registry limitations). The largest cohort notes extreme rarity (hundreds of cases in the literature) and geographic predilection. (tang2017aggressivenkcellleukemia pages 1-2, hussein2020aggressivenkcell pages 1-3)

### 9.2 Demographics (quantitative)
- **Age peak:** 21–30 years accounted for 29.2% (33/113) in a multicenter Chinese cohort. (tang2017aggressivenkcellleukemia pages 1-2)
- **Sex:** male:female ratio nearly 2:1 in that decade in the same cohort. (tang2017aggressivenkcellleukemia pages 1-2)
- **Western series:** median age 47.5 years; 9 men and 3 women. (hussein2020genomicandimmunophenotypic pages 2-3)

### 9.3 Inheritance
No germline inheritance pattern is established in retrieved evidence; ANKL is characterized by **somatic** oncogenic alterations.

---

## 10. Diagnostics

### 10.1 Diagnostic approach (real-world)
ANKL diagnosis is challenging due to variable morphology and lack of a single defining marker; it requires integration of:
- Peripheral blood and bone marrow morphology
- Flow cytometry (NK immunophenotype)
- EBV testing (EBER ISH)
- IHC and NGS when feasible
In a clinicopathologic series, the acute presentation triggered marrow sampling with suspicion of acute leukemia. (hussein2020genomicandimmunophenotypic pages 2-3)

### 10.2 Immunophenotype (high-yield diagnostic signature)
Across series and reviews, a core pattern includes:
- **Positive:** CD56, CD94, CD2; cytotoxic markers (granzyme B, TIA-1, perforin); often EBER+ (EBV-associated subset)
- **Negative:** surface CD3, CD4, CD5, CD57; TCRαβ/γδ
- Bone marrow patterns: **interstitial** or **intrasinusoidal/sinusoidal** infiltration patterns. (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020aggressivenkcell pages 3-5, hussein2020genomicandimmunophenotypic pages 2-3)

Quantitative immunophenotype from a 12-case series: CD56+ (12/12), CD94+ (9/9), CD2+ (10/12), EBER+ (9/12); surface CD3− (12/12), CD5− (11/11), CD57− (9/9), TCRαβ− (11/11), TCRγδ− (11/11). (hussein2020genomicandimmunophenotypic pages 1-2)

### 10.3 Differential diagnosis (examples)
- EBV-driven HLH without neoplasia vs ANKL presenting as EBV-HLH (emphasized in 2024 adolescent case literature). (spaner2024casereportaggressive pages 1-2)
- Extranodal NK/T-cell lymphoma with leukemic/disseminated phase (clinical overlap discussed in reviews). (hussein2020aggressivenkcell pages 1-3)

### 10.4 Suggested tests / biomarkers
- EBER ISH in marrow/tissue
- Flow cytometry with NK markers (CD56, CD94, CD16, CD2; absence of surface CD3/TCR)
- Plasma EBV DNA (used in related NK/T malignancies; specific ANKL thresholds not established in retrieved evidence)

---

## 11. Outcome / prognosis

### 11.1 Key statistics
- **Median overall survival:** 55 days in a multicenter cohort (n=113). (tang2017aggressivenkcellleukemia pages 1-2)
- **1-year survival:** 4.42% (5/113) in that cohort. (tang2017aggressivenkcellleukemia pages 1-2)
- **Median survival ~2 months:** reported in a Western clinicopathologic series and cited broadly in reviews. (hussein2020genomicandimmunophenotypic pages 1-2, hussein2020aggressivenkcell pages 1-3)

### 11.2 Prognostic factors (reported)
Univariate/multivariate analyses in the large cohort identified clinical subtype, LDH, and treatment modality as prognostic; administration of L-asparaginase-based chemotherapy and allo-HSCT were associated with improved survival. (tang2017aggressivenkcellleukemia pages 2-4)

---

## 12. Treatment

### 12.1 Standard practice (current real-world implementation)
Evidence across cohorts/reviews supports:
1) **L-asparaginase (or pegylated asparaginase)–containing induction chemotherapy** (e.g., SMILE, AspaMetDex, related regimens)
2) **Allogeneic hematopoietic stem cell transplantation (allo-HSCT)** in eligible responders
Despite these strategies, outcomes remain poor for many patients due to rapid progression and treatment-related toxicity in critically ill presentations. (ni2024clinicopathologicalfeaturesand pages 1-2, tang2017aggressivenkcellleukemia pages 1-2, tang2017aggressivenkcellleukemia pages 2-4)

### 12.2 Chemotherapy outcomes (quantitative)
In Tang et al. (n=113 cohort), among 13 newly diagnosed patients treated with **AspaMetDex** chemotherapy alone:
- **CR:** 30.77% (4/13)
- **ORR:** 76.92% (10/13)
- **Median OS:** 115 days (range 37–450)
- **Grade 3–4 hematologic AEs:** 53.84% (7/13)
These data highlight that responses are achievable, but durability is limited without consolidation. (tang2017aggressivenkcellleukemia pages 2-4)

A 2024 pediatric case review notes chemotherapy CR rates overall as **<36%** and summarizes that allo-HSCT still has high relapse/progression within 1 year (~55.5%). (ni2024clinicopathologicalfeaturesand pages 1-2)

### 12.3 Allo-HSCT outcomes (quantitative)
In Tang et al., 7 patients underwent allo-HSCT after CR:
- **Median OS:** 300 days (range 174–1480)
- **2-year OS:** 42.86% (3/7)
This supports allo-HSCT as a key consolidation strategy when remission is achieved and a donor is available. (tang2017aggressivenkcellleukemia pages 2-4)

### 12.4 Emerging/targeted therapies (expert analysis)
Genomic and drug profiling evidence indicates potential vulnerabilities:
- **JAK inhibition** (for JAK/STAT-activated disease)
- **BCL2 inhibition** (drug sensitivity profiling highlighted NK cells’ sensitivity)
- **Immune checkpoint blockade** in selected contexts (PD-L1 expression reported in a subset)
These approaches are not yet established as standard-of-care in the retrieved evidence but are rationally motivated by the genomic landscape. (hussein2020genomicandimmunophenotypic pages 1-2, dufva2018aggressivenaturalkillercell pages 3-4)

### 12.5 Clinical trials (NCT identifiers)
- **NCT03719105** (start 2019-03-01; Early Phase 1; Recruiting): Modified SMILE (mSMILE) including calaspargase pegol; pembrolizumab added for <CR after 2 cycles; followed by allo-HSCT when possible; explicitly includes ANKL in cohort 1. (NCT03719105 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT03719105
- **NCT03623087** (start 2017-07-01; Phase 3; status uncertain in record): “SIMPLE” chemotherapy regimen (cisplatin, gemcitabine, ifosfamide, etoposide, L-asparaginase, dexamethasone) designed as non-inferiority vs SMILE and includes aggressive NK leukaemia among target conditions. (NCT03623087 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT03623087
- **NCT05863234** (2023; Phase I/II; Recruiting; n=7): PPMX-T003 continuous IV administration safety/PK study in ANKL; excludes patients eligible for chemotherapy. (NCT05863234 chunk 1)
  - URL: https://clinicaltrials.gov/study/NCT05863234

### 12.6 Suggested MAXO terms (examples)
- Chemotherapy **MAXO:0000647**
- L-asparaginase therapy (map as chemotherapy + specific drug exposure; MAXO may not have a dedicated asparaginase term)
- Allogeneic hematopoietic stem cell transplantation **MAXO:0000747** (or closest HSCT term depending on MAXO release)
- Immune checkpoint inhibitor therapy (immunotherapy; PD-1 inhibitor)

---

## 13. Prevention
No primary prevention strategies are established for ANKL in retrieved evidence. Prevention is largely not applicable beyond general EBV disease management and immunosuppression/immune dysregulation surveillance in high-risk contexts (not quantified here).

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in retrieved evidence.

---

## 15. Model organisms
No dedicated animal models were identified in the retrieved evidence. The strongest mechanistic evidence here is from human tumor genomics and ex vivo drug sensitivity profiling. (dufva2018aggressivenaturalkillercell pages 3-4)

---

## Recent developments & 2023–2024 highlights (prioritized)
1) **2024 case-based literature** emphasizes that ANKL may present as refractory EBV-HLH and that lack of a “distinct immunologic and morphologic signature” delays diagnosis; early, repeated marrow/peripheral blood flow cytometry is highlighted as critical. (spaner2024casereportaggressive pages 1-2)
2) **2024 pediatric case series** supports the operational treatment strategy of intensive pegaspargase/anthracycline-containing chemotherapy with consideration of HSCT, while underscoring high early mortality (e.g., tumor lysis) and the need for rapid supportive care. (ni2024clinicopathologicalfeaturesand pages 1-2)
3) **WHO/ICC-era classification synthesis (2024)** provides clinicians/pathologists a consolidated view of how modern frameworks align, improving standardization of terminology and diagnostic categorization for mature T/NK neoplasms. (ferry2024maturebt pages 8-10)

---

## Key statistics (for knowledge base)
- **Median OS:** 55 days (Tang et al., 2017; n=113). (tang2017aggressivenkcellleukemia pages 1-2)
- **1-year survival:** 4.42% (5/113). (tang2017aggressivenkcellleukemia pages 1-2)
- **AspaMetDex induction (subset):** CR 30.77%; ORR 76.92%; median OS 115 days; grade 3–4 hematologic AEs 53.84%. (tang2017aggressivenkcellleukemia pages 2-4)
- **Allo-HSCT (subset):** 2-year OS 42.86% (3/7). (tang2017aggressivenkcellleukemia pages 2-4)

---

## Visual evidence (genomic landscape)
Dufva et al. provide figure panels and a table summarizing JAK-STAT pathway alterations (mutations and copy-number gains) across ANKL cohorts and related NK/T malignancies; these visuals support the centrality of JAK/STAT dysregulation in ANKL and the rationale for pathway-directed therapy hypotheses. (dufva2018aggressivenaturalkillercell media 01c6d37e, dufva2018aggressivenaturalkillercell media 2b03bded)

---

## Limitations of this evidence set
- Several requested identifiers (MONDO, OMIM, Orphanet, MeSH, ICD-10/ICD-11) were not available from the retrieved texts in this run.
- Many articles in this run do not provide PMIDs in the extracted text, so **PMID-preferring citations cannot always be satisfied** without additional PubMed-specific retrieval.
- Incidence/prevalence rates and validated QoL measures were not found in the retrieved evidence.



References

1. (hussein2020aggressivenkcell pages 1-3): Siba El Hussein, L. Medeiros, and Joseph Khoury. Aggressive nk cell leukemia: current state of the art. Cancers, 12:2900, Oct 2020. URL: https://doi.org/10.3390/cancers12102900, doi:10.3390/cancers12102900. This article has 67 citations.

2. (spaner2024casereportaggressive pages 1-2): Caroline Spaner, Jessica Durkee-Shock, Andrew Weng, Ryan Stubbins, Alina S. Gerrie, Stefania Pittaluga, Jeffrey I. Cohen, and Luke Y. C. Chen. Case report: aggressive natural killer cell leukemia and refractory hemophagocytic lymphohistiocytosis in an adolescent. Frontiers in Hematology, Jul 2024. URL: https://doi.org/10.3389/frhem.2024.1413794, doi:10.3389/frhem.2024.1413794. This article has 0 citations.

3. (ferry2024maturebt pages 8-10): Judith A. Ferry, Brian Hill, and Eric D. Hsi. Mature b, t and nk-cell, plasma cell and histiocytic/dendritic cell neoplasms: classification according to the world health organization and international consensus classification. Journal of Hematology & Oncology, Jul 2024. URL: https://doi.org/10.1186/s13045-024-01570-5, doi:10.1186/s13045-024-01570-5. This article has 19 citations and is from a domain leading peer-reviewed journal.

4. (hussein2020genomicandimmunophenotypic pages 1-2): Siba El Hussein, Keyur P. Patel, Hong Fang, Beenu Thakral, Sanam Loghavi, Rashmi Kanagal-Shamanna, Sergej Konoplev, Elias J. Jabbour, L. Jeffrey Medeiros, and Joseph D. Khoury. Genomic and immunophenotypic landscape of aggressive nk-cell leukemia. The American Journal of Surgical Pathology, 44:1235-1243, Jun 2020. URL: https://doi.org/10.1097/pas.0000000000001518, doi:10.1097/pas.0000000000001518. This article has 46 citations.

5. (ishida2018aggressivenkcellleukemia pages 1-2): Fumihiro Ishida. Aggressive nk-cell leukemia. Frontiers in Pediatrics, Oct 2018. URL: https://doi.org/10.3389/fped.2018.00292, doi:10.3389/fped.2018.00292. This article has 66 citations.

6. (tang2017aggressivenkcellleukemia pages 1-2): Yuan Tang, D. Wang, H. Luo, M. Xiao, H-S Zhou, D. Liu, Shaoping Ling, N. Wang, X-L Hu, Y. Luo, X. Mao, Q. Ao, J. Huang, W. Zhang, L. Sheng, L. Zhu, Z. Shang, L. Gao, P-L Zhang, M. Zhou, K. Zhou, L. Qiu, Q.‐F. Liu, H.-Y. Zhang, J. Li, J. Jin, L. Fu, W-L Zhao, J-P Chen, X. Du, G. Huang, Q-f Wang, J. Zhou, and L. Huang. Aggressive nk-cell leukemia: clinical subtypes, molecular features, and treatment outcomes. Blood Cancer Journal, Dec 2017. URL: https://doi.org/10.1038/s41408-017-0021-z, doi:10.1038/s41408-017-0021-z. This article has 72 citations and is from a domain leading peer-reviewed journal.

7. (hussein2020aggressivenkcell pages 3-5): Siba El Hussein, L. Medeiros, and Joseph Khoury. Aggressive nk cell leukemia: current state of the art. Cancers, 12:2900, Oct 2020. URL: https://doi.org/10.3390/cancers12102900, doi:10.3390/cancers12102900. This article has 67 citations.

8. (ni2024clinicopathologicalfeaturesand pages 1-2): Yongan Ni, Lei Li, Yuping Wang, and Lirong Sun. Clinicopathological features and treatment of aggressive natural killer cell leukemia: case series and literature review. The Turkish journal of pediatrics, 66 4:481-489, Oct 2024. URL: https://doi.org/10.24953/turkjpediatr.2024.5072, doi:10.24953/turkjpediatr.2024.5072. This article has 1 citations.

9. (hussein2020genomicandimmunophenotypic pages 2-3): Siba El Hussein, Keyur P. Patel, Hong Fang, Beenu Thakral, Sanam Loghavi, Rashmi Kanagal-Shamanna, Sergej Konoplev, Elias J. Jabbour, L. Jeffrey Medeiros, and Joseph D. Khoury. Genomic and immunophenotypic landscape of aggressive nk-cell leukemia. The American Journal of Surgical Pathology, 44:1235-1243, Jun 2020. URL: https://doi.org/10.1097/pas.0000000000001518, doi:10.1097/pas.0000000000001518. This article has 46 citations.

10. (dufva2018aggressivenaturalkillercell pages 3-4): Olli Dufva, Matti Kankainen, Tiina Kelkka, Nodoka Sekiguchi, Shady Adnan Awad, Samuli Eldfors, Bhagwan Yadav, Heikki Kuusanmäki, Disha Malani, Emma I Andersson, Paavo Pietarinen, Leena Saikko, Panu E. Kovanen, Teija Ojala, Dean A. Lee, Thomas P. Loughran, Hideyuki Nakazawa, Junji Suzumiya, Ritsuro Suzuki, Young Hyeh Ko, Won Seog Kim, Shih-Sung Chuang, Tero Aittokallio, Wing C. Chan, Koichi Ohshima, Fumihiro Ishida, and Satu Mustjoki. Aggressive natural killer-cell leukemia mutational landscape and drug profiling highlight jak-stat signaling as therapeutic target. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03987-2, doi:10.1038/s41467-018-03987-2. This article has 163 citations and is from a highest quality peer-reviewed journal.

11. (sumbly2022aggressivenaturalkiller pages 2-3): Vikram Sumbly, Mallorie Vest, and Ian Landry. Aggressive natural killer cell leukemia: a brief overview of its genomic landscape, histological features, and current management. Cureus, Feb 2022. URL: https://doi.org/10.7759/cureus.22537, doi:10.7759/cureus.22537. This article has 17 citations.

12. (NCT03623087 chunk 1): Professor Yok-lam Kwong. SIMPLE Chemotherapy for NK Lymphoma/Leukaemia. The University of Hong Kong. 2017. ClinicalTrials.gov Identifier: NCT03623087

13. (dufva2018aggressivenaturalkillercell media 01c6d37e): Olli Dufva, Matti Kankainen, Tiina Kelkka, Nodoka Sekiguchi, Shady Adnan Awad, Samuli Eldfors, Bhagwan Yadav, Heikki Kuusanmäki, Disha Malani, Emma I Andersson, Paavo Pietarinen, Leena Saikko, Panu E. Kovanen, Teija Ojala, Dean A. Lee, Thomas P. Loughran, Hideyuki Nakazawa, Junji Suzumiya, Ritsuro Suzuki, Young Hyeh Ko, Won Seog Kim, Shih-Sung Chuang, Tero Aittokallio, Wing C. Chan, Koichi Ohshima, Fumihiro Ishida, and Satu Mustjoki. Aggressive natural killer-cell leukemia mutational landscape and drug profiling highlight jak-stat signaling as therapeutic target. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03987-2, doi:10.1038/s41467-018-03987-2. This article has 163 citations and is from a highest quality peer-reviewed journal.

14. (dufva2018aggressivenaturalkillercell media 2b03bded): Olli Dufva, Matti Kankainen, Tiina Kelkka, Nodoka Sekiguchi, Shady Adnan Awad, Samuli Eldfors, Bhagwan Yadav, Heikki Kuusanmäki, Disha Malani, Emma I Andersson, Paavo Pietarinen, Leena Saikko, Panu E. Kovanen, Teija Ojala, Dean A. Lee, Thomas P. Loughran, Hideyuki Nakazawa, Junji Suzumiya, Ritsuro Suzuki, Young Hyeh Ko, Won Seog Kim, Shih-Sung Chuang, Tero Aittokallio, Wing C. Chan, Koichi Ohshima, Fumihiro Ishida, and Satu Mustjoki. Aggressive natural killer-cell leukemia mutational landscape and drug profiling highlight jak-stat signaling as therapeutic target. Nature Communications, Apr 2018. URL: https://doi.org/10.1038/s41467-018-03987-2, doi:10.1038/s41467-018-03987-2. This article has 163 citations and is from a highest quality peer-reviewed journal.

15. (tang2017aggressivenkcellleukemia pages 2-4): Yuan Tang, D. Wang, H. Luo, M. Xiao, H-S Zhou, D. Liu, Shaoping Ling, N. Wang, X-L Hu, Y. Luo, X. Mao, Q. Ao, J. Huang, W. Zhang, L. Sheng, L. Zhu, Z. Shang, L. Gao, P-L Zhang, M. Zhou, K. Zhou, L. Qiu, Q.‐F. Liu, H.-Y. Zhang, J. Li, J. Jin, L. Fu, W-L Zhao, J-P Chen, X. Du, G. Huang, Q-f Wang, J. Zhou, and L. Huang. Aggressive nk-cell leukemia: clinical subtypes, molecular features, and treatment outcomes. Blood Cancer Journal, Dec 2017. URL: https://doi.org/10.1038/s41408-017-0021-z, doi:10.1038/s41408-017-0021-z. This article has 72 citations and is from a domain leading peer-reviewed journal.

16. (NCT03719105 chunk 1): Mitchell Cairo. Chemoimmunotherapy and Allogeneic Stem Cell Transplant for NK T-cell Leukemia/Lymphoma. New York Medical College. 2019. ClinicalTrials.gov Identifier: NCT03719105

17. (NCT05863234 chunk 1):  Safety Evaluation Study for Patients With Aggressive NK-cell Leukemia. Hiroshima University Hospital. 2023. ClinicalTrials.gov Identifier: NCT05863234