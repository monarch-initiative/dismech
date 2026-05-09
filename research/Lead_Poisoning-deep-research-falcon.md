---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:21:13.840867'
end_time: '2026-05-09T10:38:49.080798'
duration_seconds: 1055.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lead Poisoning
  mondo_id: ''
  category: Environmental
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
- **Disease Name:** Lead Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Lead Poisoning** covering all of the
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
- **Disease Name:** Lead Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Lead Poisoning** covering all of the
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


# Lead Poisoning (Plumbism): Disease Characteristics Research Report

## 1. Disease Information

### Overview / current understanding
Lead poisoning (also termed *plumbism*) is a toxicologic disease caused by absorption of lead (Pb) with subsequent systemic distribution and cumulative retention, producing multisystem injury. Contemporary clinical framing emphasizes that toxicity is not limited to overt “classic” poisoning; low-level chronic exposure is linked to neurodevelopmental harm in children and cardiovascular/kidney disease in adults. In a 2024 *New England Journal of Medicine* review, the CDC’s position is summarized as: **“no safe level of lead had been identified in children”**. (lanphear2024leadpoisoning. pages 3-5)

Lead has a long biologic residence time because most retained Pb is stored in bone, with only a small fraction present in blood at any time; thus blood lead reflects both recent exposure and mobilization from stores. (lanphear2024leadpoisoning. pages 1-2, yu2023publicandoccupational pages 1-3)

### Key identifiers (OMIM / Orphanet / ICD / MeSH / MONDO)
Within the evidence retrieved for this report, **explicit ontology/terminology identifiers (ICD-10/ICD-11, MeSH, MONDO, OMIM, Orphanet)** were **not present** in the full-text excerpts available to the system. Therefore, these cannot be provided with evidence-backed citations in this tool run.

### Synonyms / alternative names
* Lead poisoning
* Plumbism
* Lead intoxication
These terms are used interchangeably in contemporary clinical literature. (lanphear2024leadpoisoning. pages 1-2)

### Evidence source type
The content summarized here is derived primarily from **aggregated disease-level resources** (high-impact reviews and policy analyses) and **primary studies** (randomized trial, observational epidemiology, case report), rather than EHR-only patient-level data. (lanphear2024leadpoisoning. pages 3-5, rogan2001theeffectof pages 1-2, obeng2023thecontributionof pages 2-4)


## 2. Etiology

### Disease causal factors
Lead poisoning is **environmental/toxicant-induced**.

**Routes of exposure** are primarily ingestion and inhalation. (lanphear2024leadpoisoning. pages 2-3, yu2023publicandoccupational pages 1-3)

**Major sources** highlighted in recent clinical/public-health syntheses include:
* Legacy lead-based paint and dust/soil contamination around older housing (especially pre-1960 housing). (lanphear2024leadpoisoning. pages 2-3)
* Water contamination from lead service lines and plumbing components. (lanphear2024leadpoisoning. pages 1-2, lanphear2024leadpoisoning. pages 2-3)
* Industrial emissions and occupational exposures (smelting, battery production/recycling, construction). (lanphear2024leadpoisoning. pages 1-2, lanphear2024leadpoisoning. pages 2-3, yu2023publicandoccupational pages 1-3)
* Consumer products (spices, ceramic/metal cookware, traditional remedies, cultural powders, cosmetics, jewelry/toys). (porterfield2024asnapshotof pages 1-2, porterfield2024asnapshotof pages 2-3, porterfield2024asnapshotof pages 5-6)
* Ongoing specialized uses such as aviation fuel and ammunition (and retained bullet fragments). (lanphear2024leadpoisoning. pages 1-2, lanphear2024leadpoisoning. pages 2-3)

### Risk factors

**Host risk factors / vulnerability**:
* **Young age**: children absorb Pb more readily and have high-risk behaviors (hand-to-mouth). (lanphear2024leadpoisoning. pages 2-3, cuomo2022systemicreviewof pages 1-3)
* **Nutritional deficiencies**: iron or calcium deficiency increases absorption; absorption increases with iron/calcium deficiency. (lanphear2024leadpoisoning. pages 2-3, cuomo2022systemicreviewof pages 1-3)
* **Pregnancy and postpartum**: increased risk of mobilization from bone stores and adverse birth outcomes; maternal Pb is linked to preterm birth. (lanphear2024leadpoisoning. pages 3-5, lanphear2024leadpoisoning. pages 1-2)

**Social and environmental risk factors**:
* Older, poorly maintained housing stock. (lanphear2024leadpoisoning. pages 2-3, jacobs2023childhoodleadpoisoning pages 4-6)
* Occupational exposure in lead-related industries. (yu2023publicandoccupational pages 1-3)
* Consumer products and imported goods exposure, especially in immigrant/refugee communities. (porterfield2024asnapshotof pages 1-2)
* Secondhand tobacco smoke exposure as an additional contributor to children’s BLLs (NHANES 2015–2018). (obeng2023thecontributionof pages 2-4, obeng2023thecontributionof pages 1-2)

### Protective factors
Evidence in retrieved texts supports that improved nutrition (addressing iron deficiency; ensuring adequate calcium and vitamin C) is considered part of management and may reduce absorption risk, but the excerpts do not provide trial-grade quantification of protective effect size. (lowry2010oralchelationtherapy pages 6-9)

### Gene–environment interactions
Recent evidence supports **interindividual susceptibility** via gene–environment interactions:
* In occupationally exposed workers, SNP-by-lead interactions were reported for blood pressure traits. In one cross-sectional study (568 workers), the **CCM3 rs3804610** interaction corresponded to **SBP +0.53 mmHg** and **DBP +0.34 mmHg** per 1 µg/dL blood lead contrast in risk-allele carriers; **VEGFR2 rs2305948** showed negative interaction (SBP −0.28 mmHg; DBP −0.22 mmHg). (ou2024interplayanalysisof pages 1-2)
* A 2022 systematic review summarizes candidate susceptibility loci affecting Pb kinetics and effects (e.g., **ALAD**, **VDR**, **HFE**, GST genes, MT2A) and notes sex- and exposure-dependent effects in some studies. (cuomo2022systemicreviewof pages 6-7)


## 3. Phenotypes

### Core clinical manifestations (symptoms/signs/labs)
A contemporary clinical review describes classic symptoms including fatigue, headache, irritability, abdominal colic and constipation, with very high blood lead levels associated with seizures, encephalopathy, and death. (lanphear2024leadpoisoning. pages 1-2)

**Severe neurologic phenotype (pediatric encephalopathy)**: A 2024 case report describes a 4-year-old presenting with refractory status epilepticus, profound microcytic anemia, and developmental delay at **BLL 116.2 µg/dL**. (kamal2024leadencephalopathypresenting pages 1-2)

### Age of onset, severity, progression
* **Children**: effects can be subtle and neurodevelopmental at low exposures; severe acute manifestations can include encephalopathy and seizures at high BLLs. (lanphear2024leadpoisoning. pages 3-5, kamal2024leadencephalopathypresenting pages 2-4)
* **Adults**: low-level chronic exposure is linked to hypertension, chronic kidney disease/failure, and cardiovascular disease. (lanphear2024leadpoisoning. pages 1-2, yu2023publicandoccupational pages 1-3)

### Suggested HPO terms (non-exhaustive; derived from described phenotypes)
Because HPO identifiers were not included in the retrieved sources, the following are **suggested mapping targets** (to be verified against HPO):
* Seizures; status epilepticus (pediatric encephalopathy) (kamal2024leadencephalopathypresenting pages 1-2)
* Encephalopathy (lanphear2024leadpoisoning. pages 1-2, kamal2024leadencephalopathypresenting pages 2-4)
* Abdominal pain / colic; constipation (lanphear2024leadpoisoning. pages 1-2)
* Microcytic anemia (kamal2024leadencephalopathypresenting pages 1-2)
* Developmental delay / cognitive impairment; ADHD / attention problems (lanphear2024leadpoisoning. pages 3-5, kamal2024leadencephalopathypresenting pages 1-2)
* Hypertension (yu2023publicandoccupational pages 1-3)
* Chronic kidney disease/failure (lanphear2024leadpoisoning. pages 1-2, yu2023publicandoccupational pages 1-3)


## 4. Genetic / Molecular Information

### Causal genes
Lead poisoning is not a Mendelian disorder; it is primarily a toxicant exposure condition. Genetic factors act mainly as **susceptibility/modifier loci** (gene–environment interaction) rather than single-gene causation. (cuomo2022systemicreviewof pages 6-7)

### Modifier genes / susceptibility loci (examples in retrieved evidence)
* **CCM3 (PDCD10)** rs3804610; **VEGFR2 (KDR)** rs2305948; **NOTCH1** rs3124591 in an occupational interaction study of lead and blood pressure. (ou2024interplayanalysisof pages 1-2)
* Candidate genes summarized as influencing Pb kinetics/effects: **ALAD**, **VDR**, **HFE**, GST genes, metallothionein, iron transport genes. (cuomo2022systemicreviewof pages 6-7)

### Epigenetic information
A 2023 state-of-the-science review on occupational toxicant exposure methylation emphasizes that lead exposure is associated with DNA methylation changes (e.g., promoter hypermethylation of genes such as **ALAD**, tumor suppressor loci, and global methylation shifts), but cautions that due to limited longitudinal evidence and heterogeneity **“we cannot say that DNA methylation changes are predictive of disease development due to those exposures.”** (jimenezgarza2023toxicomethylomicsrevisiteda pages 1-2)


## 5. Environmental Information

### Environmental factors and real-world exposure sources
A 2024 high-impact synthesis summarizes lead sources as including legacy paint/soil, water lines, consumer products (spices, ceramics, cosmetics), industrial emissions, and specific ongoing uses (aviation fuel, ammunition). (lanphear2024leadpoisoning. pages 1-2, lanphear2024leadpoisoning. pages 2-3)

### Lifestyle factors
Secondhand tobacco smoke may be a measurable contributor to children’s BLLs: NHANES 2015–2018 data (ages 6–19 years) showed adjusted geometric mean BLLs were **18% higher** at intermediate cotinine and **29% higher** at high cotinine relative to low cotinine. (obeng2023thecontributionof pages 1-2)


## 6. Mechanism / Pathophysiology

### Toxicokinetics and causal chain (trigger → biology → phenotype)
**Trigger**: inhalation/ingestion exposure, with enhanced absorption under iron/calcium deficiency and in young children. (lanphear2024leadpoisoning. pages 2-3)

**Distribution and storage**: most retained Pb is stored in bone (skeleton), with a small blood fraction primarily in red blood cells; bone lead can be remobilized (e.g., physiologic states such as menopause). (lanphear2024leadpoisoning. pages 1-2, yu2023publicandoccupational pages 1-3)

**Cellular/molecular injury mechanisms** (as described in retrieved evidence):
* **Metal mimicry and transport**: Pb mimics calcium/iron/zinc and can enter cells via calcium channels and DMT1. (lanphear2024leadpoisoning. pages 2-3)
* **Oxidative stress and thiol binding** are repeatedly invoked as core mechanisms across organ systems. (cuomo2022systemicreviewof pages 1-3)

**Clinical endpoints**: neurodevelopmental impairment (children), cardiovascular disease and hypertension (adults), and kidney disease. (lanphear2024leadpoisoning. pages 1-2, yu2023publicandoccupational pages 1-3)

### Suggested ontology terms
Because GO/CL/Reactome identifiers were not provided in retrieved excerpts, the following are **suggested** targets (to be verified):
* GO (process): response to toxic substance; oxidative stress response; metal ion homeostasis; neurodevelopment
* CL (cells): neurons; glial cells; erythrocytes; renal tubular epithelial cells; vascular smooth muscle cells


## 7. Anatomical Structures Affected

Evidence supports multi-organ involvement:
* **Nervous system** (brain; neurodevelopmental effects; encephalopathy, seizures). (lanphear2024leadpoisoning. pages 3-5, kamal2024leadencephalopathypresenting pages 1-2)
* **Blood/hematopoietic system** (anemia in severe pediatric case). (kamal2024leadencephalopathypresenting pages 1-2)
* **Kidney** (chronic kidney disease/failure associations in adults). (lanphear2024leadpoisoning. pages 1-2)
* **Cardiovascular system** (hypertension, cardiovascular disease). (lanphear2024leadpoisoning. pages 1-2, yu2023publicandoccupational pages 1-3)
* **Skeleton/bone** as major reservoir for Pb. (lanphear2024leadpoisoning. pages 1-2)

Suggested UBERON targets (to be verified): brain; kidney; heart; aorta; skeleton/bone tissue.


## 8. Temporal Development

### Onset patterns
Lead poisoning may be **acute** (high-dose exposure with colic/encephalopathy) or **chronic/insidious** with low-level exposure producing subtle neurocognitive harms (children) and cardiometabolic disease risk (adults). (lanphear2024leadpoisoning. pages 1-2, lanphear2024leadpoisoning. pages 2-3)

### Critical windows
Childhood neurodevelopment is a key window of vulnerability, with lasting cognitive/behavioral sequelae and limited reversibility emphasized in public health analyses. (sobin2023improvingequitabilityand pages 3-3, lanphear2024leadpoisoning. pages 3-5)


## 9. Inheritance and Population

### Epidemiology and burden (selected statistics)
A 2023 policy/housing review reports a dramatic decline in U.S. pediatric blood lead over decades (NHANES geometric mean **12.8 → 0.82 µg/dL** from 1976–1980 to 2015–2016) and gives 2015–2016 prevalence estimates (ages 1–5): **1.3% ≥5 µg/dL** and **0.2% ≥10 µg/dL**. (jacobs2023childhoodleadpoisoning pages 4-6)

A 2024 consumer-product surveillance synthesis cites a 2021 estimate that **21,172 children (1.9%)** had BLLs ≥ the then-reference value (5 µg/dL), and after the BLRV dropped to 3.5 µg/dL an estimated **2.5%** of U.S. children would exceed it. (porterfield2024asnapshotof pages 1-2)

Global burden: the 2024 NEJM review cites 2019 estimates of **5.5 million cardiovascular deaths** and **765 million IQ points lost** attributable to lead exposure globally. (lanphear2024leadpoisoning. pages 1-2)

### Population disparities
The testing and prevention literature emphasizes socioeconomic inequities and persistent disparities, and argues that primary prevention (removing lead from environments) is the definitive solution. (sobin2023improvingequitabilityand pages 3-3)


## 10. Diagnostics

### Clinical tests / biomarkers
**Venous whole-blood lead level (BLL)** is emphasized as the most widely used biomarker of exposure. (lanphear2024leadpoisoning. pages 1-2)

A 2024 NEJM review summarizes that blood lead is mostly in red blood cells and is the standard biomarker; bone lead can be measured in research contexts and constitutes cumulative burden. (lanphear2024leadpoisoning. pages 1-2)

**Testing implementation / methods**: A policy analysis proposes expanded use of capillary testing (with “clean” collection training) and recommends sensitive analytical methods (ICP-MS or graphite furnace AAS) with low limits of detection to support detection at low BLLs under the 3.5 µg/dL reference value. (sobin2023improvingequitabilityand pages 3-3)

### Screening / thresholds (as supported in retrieved evidence)
* CDC blood lead reference value lowered to **3.5 µg/dL** (2021). (lanphear2024leadpoisoning. pages 2-3, sobin2023improvingequitabilityand pages 3-3)


## 11. Outcome / Prognosis

Low-level exposure can have persistent effects (particularly neurodevelopment), and severe acute toxicity can be fatal or cause long-term neurologic sequelae. The 2024 severe pediatric encephalopathy case report emphasizes that rapid recognition and appropriate management is essential for “neurologically intact survival.” (kamal2024leadencephalopathypresenting pages 1-2)


## 12. Treatment

### Core treatment principles
* **Remove/stop exposure** and perform environmental investigation/abatement; chelation is not a substitute for hazard control. (lowry2010oralchelationtherapy pages 6-9)

### Chelation therapy

#### Evidence base (children with moderate BLLs)
The pivotal multicenter randomized trial (TLC) enrolled 780 children aged 12–33 months with BLLs **20–44 µg/dL**. Succimer reduced mean BLL by **4.5 µg/dL** over the first 6 months, but at 36 months: **“Treatment with succimer did not lead to better scores on cognitive, neuropsychological, or behavioral tests than placebo.”** (rogan2001theeffectof pages 5-6, rogan2001theeffectof pages 3-5)

#### Severe poisoning / encephalopathy
A 2024 pediatric encephalopathy case report notes encephalopathy typically occurs at **>80–100 µg/dL**, and describes combined chelation (succimer, calcium disodium EDTA, and dimercaprol) with repeated courses due to rebound; it provides BSA-based dosing examples for succimer and EDTA and highlights need for close monitoring. (kamal2024leadencephalopathypresenting pages 2-4, kamal2024leadencephalopathypresenting pages 1-2)

### Real-world implementation constraints: chelator shortages
A 2024 analysis of U.S. shortages (2001–2022) identified 13 chelator shortages, with prolonged and overlapping episodes and large price increases. CaNa2EDTA was unavailable for **22.5%** of the period; and BAL’s sole U.S. manufacturer (Akorn) permanently shut down in **February 2023**. (whitledge2024trendsinshortages pages 4-5)

### Suggested MAXO terms (to be verified)
* Chelation therapy
* Environmental exposure removal / abatement
* Blood lead screening
* Nutritional supplementation (iron/calcium) as supportive care


## 13. Prevention

### Primary prevention
Multiple authoritative sources emphasize that definitive prevention requires removing lead hazards before exposure (“primary prevention”), especially in housing and in the imported consumer-product supply chain. (sobin2023improvingequitabilityand pages 3-3, porterfield2024asnapshotof pages 1-2)

### Secondary prevention: screening/testing
A 2023 policy analysis proposes practical improvements to raise equitable detection capacity, including acceptance of capillary samples for final determination (with standardized training/certification) and sensitive analytical methods to support low-level measurement. (sobin2023improvingequitabilityand pages 3-3)

### Public health interventions in practice
A 2024 Environmental Health Perspectives analysis argues consumer products are an increasingly important source: across four U.S. jurisdictions, consumer products were identified in **15%–38%** of investigations, supporting the need for national product surveillance databases and upstream interventions in countries of origin. (porterfield2024asnapshotof pages 1-2, porterfield2024asnapshotof pages 3-5)


## 14. Other Species / Natural Disease
No species-specific veterinary/natural disease evidence was retrieved in the provided corpus for this run. Therefore, this section cannot be completed with citations.


## 15. Model Organisms
Model-organism evidence in the retrieved corpus includes a rodent study showing that blood lead reductions after succimer can overestimate brain lead reductions, emphasizing limitations of using blood lead as a surrogate for neurotoxicant burden. (stangle2004reductionsinblood pages 5-6)

No additional detailed model-organism inventories (mouse/rat/zebrafish/cell models) were retrievable in the excerpts available here; thus this section is partial.


# Key quantitative summary tables

| Item | Population/Context | Value(s) & Units | Year/Period | Source (first author, journal) | URL | Evidence citation id |
|---|---|---|---|---|---|---|
| CDC blood lead reference value (BLRV) | U.S. children; CDC reference/action benchmark | Lowered to **3.5 µg/dL** (from 5 µg/dL) | 2021 | Lanphear, *NEJM*; Sobin, *Milbank Quarterly* | https://doi.org/10.1056/NEJMra2402527 ; https://doi.org/10.1111/1468-0009.12596 | (lanphear2024leadpoisoning. pages 2-3, sobin2023improvingequitabilityand pages 3-3) |
| U.S. child prevalence at prior BLRV | U.S. children with BLLs at or above prior CDC BLRV | **21,172 children (1.9%)** at **≥5 µg/dL** | 2021 study cited in 2024 review | Porterfield, *Environmental Health Perspectives* | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 1-2) |
| U.S. child prevalence at current BLRV | U.S. children expected above current BLRV | **2.5%** expected at **≥3.5 µg/dL** | Post-2021 BLRV estimate | Porterfield, *Environmental Health Perspectives* | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 1-2) |
| NHANES decline in pediatric blood lead | U.S. children aged 1–5 years; geometric mean BLL | **12.8 → 0.82 µg/dL** | 1976–1980 to 2015–2016 | Jacobs, *J Public Health Management Practice* | https://doi.org/10.1097/PHH.0000000000001664 | (jacobs2023childhoodleadpoisoning pages 4-6) |
| NHANES decline in general-population blood lead | U.S. NHANES population metric | **13.1 → 1.64 µg/dL** | 1976–1980 to 1999–2002 | Yu, *Hypertension Research* | https://doi.org/10.1038/s41440-022-01069-x | (yu2023publicandoccupational pages 1-3) |
| Skeletal lead storage fraction | Retained body lead stored in skeleton | **70% in children; 95% in adults** | Contemporary toxicokinetic summary | Lanphear, *NEJM* | https://doi.org/10.1056/NEJMra2402527 | (lanphear2024leadpoisoning. pages 1-2, lanphear2024leadpoisoning. pages 3-5) |
| Severe toxicity threshold: encephalopathy | Pediatric severe lead poisoning | Encephalopathy typically at **>80–100 µg/dL** | Contemporary case-based review | Kamal, *BMC Pediatrics* | https://doi.org/10.1186/s12887-024-04871-3 | (kamal2024leadencephalopathypresenting pages 2-4) |
| Very high acute toxicity threshold | Severe acute poisoning, all ages | **>800 µg/L** associated with **seizures, encephalopathy, death** | Contemporary clinical review | Lanphear, *NEJM* | https://doi.org/10.1056/NEJMra2402527 | (lanphear2024leadpoisoning. pages 1-2) |
| Chelation trial eligibility range | TLC randomized trial in children aged 12–33 months | Baseline venous BLL **20–44 µg/dL** | Trial enrollment period 1994–1997; report 2001 | Rogan, *NEJM* | https://doi.org/10.1056/NEJM200105103441902 | (rogan2001theeffectof pages 1-2) |
| Chelation effect size on blood lead | TLC trial; succimer vs placebo | Mean BLL reduction **4.5 µg/dL** over first **6 months** | 2001 report | Rogan, *NEJM* | https://doi.org/10.1056/NEJM200105103441902 | (rogan2001theeffectof pages 1-2, rogan2001theeffectof pages 5-6) |
| Chelation neurodevelopmental outcome | TLC trial; cognition/behavior | **No significant cognitive, neuropsychological, or behavioral benefit** despite BLL reduction | 36-month follow-up; 2001 report | Rogan, *NEJM* | https://doi.org/10.1056/NEJM200105103441902 | (rogan2001theeffectof pages 5-6, rogan2001theeffectof pages 3-5) |


*Table: This table compiles the main quantitative thresholds and epidemiologic statistics for lead poisoning drawn from the gathered evidence. It highlights current CDC benchmarks, prevalence estimates, toxicokinetic facts, severe-toxicity thresholds, and the major randomized chelation trial findings.*

| Domain | Jurisdiction/Agent | Metric | Value | Time window | Source (author/journal) | URL | Evidence citation id |
|---|---|---|---|---|---|---|---|
| Exposure sources | California | Consumer-products-only share of investigations | 25.8% (93/360) | FY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | California | Housing-only share of investigations | 27.5% (99/360) | FY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | California | Consumer-product attribution range across investigations | 22.3%–39.6% | FY2016–FY2020 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 3-5, porterfield2024asnapshotof pages 2-3) |
| Exposure sources | Oregon | Consumer-products-only share of investigations | 16.7% (30/180) | CY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | Oregon | Housing-only share of investigations | 14.4% (26/180) | CY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | Oregon | Consumer-product attribution range across investigations | 9.2%–19.1% | CY2016–CY2017 examples; broader review 2010–2021 noted 2%–20% | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 3-5, porterfield2024asnapshotof pages 2-3) |
| Exposure sources | New York City | Consumer-product attribution share | 29.4% | FY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | New York City | Housing-related attribution share | 64.2% | FY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | New York City | Multiple-source context | ~90% of children had multiple potential exposure sources | FY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 2-3) |
| Exposure sources | King County, WA | Consumer-product attribution share | 38.1% | CY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 3-5) |
| Exposure sources | King County, WA | Housing-related attribution share | 61.9% | CY2019 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 3-5) |
| Exposure sources | King County, WA | Consumer-product attribution range across investigations | 37%–46% | 2019–2021 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 3-5) |
| Exposure sources | Four jurisdictions combined | Consumer products identified as potential source | 15%–38% of investigations | 2010–2021 | Porterfield et al., *Environmental Health Perspectives* (2024) | https://doi.org/10.1289/ehp14336 | (porterfield2024asnapshotof pages 1-2) |
| Chelator supply | All lead chelators | Total shortage events | 13 shortages | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 1-2, whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | All lead chelators | Median shortage duration | 7.4 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 1-2) |
| Chelator supply | Parenteral chelators | Share of shortages | 61.5% | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 1-2, whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | Parenteral vs non-parenteral | Median shortage duration comparison | 14.2 months vs 2.2 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5, whitledge2024trendsinshortages pages 1-2, whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | Concurrent shortages | Overlapping shortage time | 3.7% of study period | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 1-2) |
| Chelator supply | CaNa2EDTA | Number of shortages | 4 | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5, whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | CaNa2EDTA | Total shortage months | 60.3 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | CaNa2EDTA | Median shortage duration | 21.2 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | CaNa2EDTA | Downtime as share of study period | 22.5% unavailable | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5) |
| Chelator supply | CaNa2EDTA | Average wholesale price (AWP) increase | $42.40 to $6,730 | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5) |
| Chelator supply | BAL (dimercaprol) | Number of shortages | 4 | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5, whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | BAL (dimercaprol) | Total shortage months | 29.5 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | BAL (dimercaprol) | Median shortage duration | 5.8 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | BAL (dimercaprol) | Manufacturing disruption | Sole US manufacturer Akorn permanently shut down after Chapter 7 bankruptcy | Feb 2023 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5, whitledge2024trendsinshortages pages 8-10) |
| Chelator supply | DMSA (succimer) | Number of shortages | 2 | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5, whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | DMSA (succimer) | Total shortage months | 8.3 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | DMSA (succimer) | Median shortage duration | 4.2 months | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 2-4) |
| Chelator supply | DMSA (succimer) | Downtime as share of study period | 3.1% unavailable | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5) |
| Chelator supply | DMSA (succimer) | Average wholesale price (AWP) increase | $469 to $2,671 | 2001–2022 | Whitledge et al., *JPPT* (2024) | https://doi.org/10.5863/1551-6776-29.3.306 | (whitledge2024trendsinshortages pages 4-5) |


*Table: This table summarizes recent U.S. data on source attribution for pediatric lead exposure across four jurisdictions and on shortages of major lead chelators. It is useful for contrasting exposure epidemiology with real-world treatment access constraints.*


# Notes on evidence gaps and identifier limitations
This report prioritizes 2023–2024 sources where available (e.g., Lanphear *NEJM* 2024; Porterfield *EHP* 2024; Yu *Hypertension Research* 2023; Sobin *Milbank Quarterly* 2023; Obeng *BMC Public Health* 2023; Whitledge *JPPT* 2024; Kamal *BMC Pediatrics* 2024). However, **formal disease ontology identifiers (MONDO, MeSH, ICD-10/11) and some requested structured ontology mappings (HPO/GO/CL/UBERON IDs)** were not present in the tool-retrieved excerpts; consequently, they are provided only as *suggested* concepts without identifier codes when not evidence-backed.

# Source figure (visual evidence)
Lanphear et al. (2024) Figure 2 (as retrieved) summarizes major exposure sources and body distribution, including bone storage fractions (70% children; 95% adults). (lanphear2024leadpoisoning. media 5797edb2)

References

1. (lanphear2024leadpoisoning. pages 3-5): Bruce Lanphear, Ana Navas-Acien, and David C. Bellinger. Lead poisoning. The New England journal of medicine, 391 17:1621-1631, Oct 2024. URL: https://doi.org/10.1056/nejmra2402527, doi:10.1056/nejmra2402527. This article has 68 citations and is from a highest quality peer-reviewed journal.

2. (lanphear2024leadpoisoning. pages 1-2): Bruce Lanphear, Ana Navas-Acien, and David C. Bellinger. Lead poisoning. The New England journal of medicine, 391 17:1621-1631, Oct 2024. URL: https://doi.org/10.1056/nejmra2402527, doi:10.1056/nejmra2402527. This article has 68 citations and is from a highest quality peer-reviewed journal.

3. (yu2023publicandoccupational pages 1-3): Yu-Ling Yu, Wen-Yi Yang, Azusa Hara, Kei Asayama, Harry A. Roels, Tim S. Nawrot, and Jan A. Staessen. Public and occupational health risks related to lead exposure updated according to present-day blood lead levels. Hypertension Research, 46:395-407, Oct 2023. URL: https://doi.org/10.1038/s41440-022-01069-x, doi:10.1038/s41440-022-01069-x. This article has 56 citations and is from a peer-reviewed journal.

4. (rogan2001theeffectof pages 1-2): Walter J. Rogan, Kim N. Dietrich, James H. Ware, Douglas W. Dockery, Mikhail Salganik, Jerilynn Radcliffe, Robert L. Jones, N. Beth Ragan, J. Julian Chisolm, and George G. Rhoads. The effect of chelation therapy with succimer on neuropsychological development in children exposed to lead. The New England journal of medicine, 344 19:1421-6, May 2001. URL: https://doi.org/10.1056/nejm200105103441902, doi:10.1056/nejm200105103441902. This article has 493 citations and is from a highest quality peer-reviewed journal.

5. (obeng2023thecontributionof pages 2-4): Alexander Obeng, Taehyun Roh, Anisha Aggarwal, Kido Uyasmasi, and Genny Carrillo. The contribution of secondhand tobacco smoke to blood lead levels in us children and adolescents: a cross-sectional analysis of nhanes 2015–2018. BMC Public Health, Jun 2023. URL: https://doi.org/10.1186/s12889-023-16005-y, doi:10.1186/s12889-023-16005-y. This article has 12 citations and is from a peer-reviewed journal.

6. (lanphear2024leadpoisoning. pages 2-3): Bruce Lanphear, Ana Navas-Acien, and David C. Bellinger. Lead poisoning. The New England journal of medicine, 391 17:1621-1631, Oct 2024. URL: https://doi.org/10.1056/nejmra2402527, doi:10.1056/nejmra2402527. This article has 68 citations and is from a highest quality peer-reviewed journal.

7. (porterfield2024asnapshotof pages 1-2): Kate Porterfield, Paromita Hore, Stephen G. Whittaker, Katie M. Fellows, Anshu Mohllajee, Shakoora Azimi-Gaylon, Berna Watson, Isabel Grant, and Richard Fuller. A snapshot of lead in consumer products across four us jurisdictions. Environmental Health Perspectives, Jul 2024. URL: https://doi.org/10.1289/ehp14336, doi:10.1289/ehp14336. This article has 10 citations and is from a highest quality peer-reviewed journal.

8. (porterfield2024asnapshotof pages 2-3): Kate Porterfield, Paromita Hore, Stephen G. Whittaker, Katie M. Fellows, Anshu Mohllajee, Shakoora Azimi-Gaylon, Berna Watson, Isabel Grant, and Richard Fuller. A snapshot of lead in consumer products across four us jurisdictions. Environmental Health Perspectives, Jul 2024. URL: https://doi.org/10.1289/ehp14336, doi:10.1289/ehp14336. This article has 10 citations and is from a highest quality peer-reviewed journal.

9. (porterfield2024asnapshotof pages 5-6): Kate Porterfield, Paromita Hore, Stephen G. Whittaker, Katie M. Fellows, Anshu Mohllajee, Shakoora Azimi-Gaylon, Berna Watson, Isabel Grant, and Richard Fuller. A snapshot of lead in consumer products across four us jurisdictions. Environmental Health Perspectives, Jul 2024. URL: https://doi.org/10.1289/ehp14336, doi:10.1289/ehp14336. This article has 10 citations and is from a highest quality peer-reviewed journal.

10. (cuomo2022systemicreviewof pages 1-3): Danila Cuomo, Margaret J. Foster, and David Threadgill. Systemic review of genetic and epigenetic factors underlying differential toxicity to environmental lead (pb) exposure. Environmental Science and Pollution Research, 29:35583-35598, Mar 2022. URL: https://doi.org/10.1007/s11356-022-19333-5, doi:10.1007/s11356-022-19333-5. This article has 62 citations and is from a peer-reviewed journal.

11. (jacobs2023childhoodleadpoisoning pages 4-6): David E. Jacobs and Mary Jean Brown. Childhood lead poisoning 1970-2022: charting progress and needed reforms. Journal of Public Health Management and Practice, 29:230-240, Nov 2023. URL: https://doi.org/10.1097/phh.0000000000001664, doi:10.1097/phh.0000000000001664. This article has 48 citations and is from a peer-reviewed journal.

12. (obeng2023thecontributionof pages 1-2): Alexander Obeng, Taehyun Roh, Anisha Aggarwal, Kido Uyasmasi, and Genny Carrillo. The contribution of secondhand tobacco smoke to blood lead levels in us children and adolescents: a cross-sectional analysis of nhanes 2015–2018. BMC Public Health, Jun 2023. URL: https://doi.org/10.1186/s12889-023-16005-y, doi:10.1186/s12889-023-16005-y. This article has 12 citations and is from a peer-reviewed journal.

13. (lowry2010oralchelationtherapy pages 6-9): JA Lowry. Oral chelation therapy for patients with lead poisoning. Unknown journal, 2010.

14. (ou2024interplayanalysisof pages 1-2): Xiao-yan Ou, Chen Xiao, Jun Jiang, Xin-xia Liu, Lili Liu, Yao Lu, Weipeng Zhang, Yun-Shao He, and Zhiqiang Zhao. Interplay analysis of lead exposure with key cardiovascular gene polymorphisms on blood pressure in a cross-sectional study of occupational workers. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-77194-z, doi:10.1038/s41598-024-77194-z. This article has 1 citations and is from a peer-reviewed journal.

15. (cuomo2022systemicreviewof pages 6-7): Danila Cuomo, Margaret J. Foster, and David Threadgill. Systemic review of genetic and epigenetic factors underlying differential toxicity to environmental lead (pb) exposure. Environmental Science and Pollution Research, 29:35583-35598, Mar 2022. URL: https://doi.org/10.1007/s11356-022-19333-5, doi:10.1007/s11356-022-19333-5. This article has 62 citations and is from a peer-reviewed journal.

16. (kamal2024leadencephalopathypresenting pages 1-2): Iqra J. Kamal, Trevor Cerbini, Amanda Clouser, Aileen Hernandez, and Diane P. Calello. Lead encephalopathy presenting as status epilepticus: a case report. BMC Pediatrics, Oct 2024. URL: https://doi.org/10.1186/s12887-024-04871-3, doi:10.1186/s12887-024-04871-3. This article has 4 citations and is from a peer-reviewed journal.

17. (kamal2024leadencephalopathypresenting pages 2-4): Iqra J. Kamal, Trevor Cerbini, Amanda Clouser, Aileen Hernandez, and Diane P. Calello. Lead encephalopathy presenting as status epilepticus: a case report. BMC Pediatrics, Oct 2024. URL: https://doi.org/10.1186/s12887-024-04871-3, doi:10.1186/s12887-024-04871-3. This article has 4 citations and is from a peer-reviewed journal.

18. (jimenezgarza2023toxicomethylomicsrevisiteda pages 1-2): Octavio Jiménez-Garza, Manosij Ghosh, Timothy M. Barrow, and Lode Godderis. Toxicomethylomics revisited: a state-of-the-science review about dna methylation modifications in blood cells from workers exposed to toxic agents. Frontiers in Public Health, Feb 2023. URL: https://doi.org/10.3389/fpubh.2023.1073658, doi:10.3389/fpubh.2023.1073658. This article has 7 citations.

19. (sobin2023improvingequitabilityand pages 3-3): CHRISTINA SOBIN, MARISELA GUTIéRREZ‐VEGA, GISEL FLORES‐MONTOYA, MICHELLE DEL RIO, JUAN M. ALVAREZ, ALEXANDER OBENG, JALEEN AVILA, and GANGA HETTIARACHCHI. Improving equitability and inclusion for testing and detection of lead poisoning in us children. The Milbank Quarterly, 101:48-73, Jan 2023. URL: https://doi.org/10.1111/1468-0009.12596, doi:10.1111/1468-0009.12596. This article has 11 citations.

20. (rogan2001theeffectof pages 5-6): Walter J. Rogan, Kim N. Dietrich, James H. Ware, Douglas W. Dockery, Mikhail Salganik, Jerilynn Radcliffe, Robert L. Jones, N. Beth Ragan, J. Julian Chisolm, and George G. Rhoads. The effect of chelation therapy with succimer on neuropsychological development in children exposed to lead. The New England journal of medicine, 344 19:1421-6, May 2001. URL: https://doi.org/10.1056/nejm200105103441902, doi:10.1056/nejm200105103441902. This article has 493 citations and is from a highest quality peer-reviewed journal.

21. (rogan2001theeffectof pages 3-5): Walter J. Rogan, Kim N. Dietrich, James H. Ware, Douglas W. Dockery, Mikhail Salganik, Jerilynn Radcliffe, Robert L. Jones, N. Beth Ragan, J. Julian Chisolm, and George G. Rhoads. The effect of chelation therapy with succimer on neuropsychological development in children exposed to lead. The New England journal of medicine, 344 19:1421-6, May 2001. URL: https://doi.org/10.1056/nejm200105103441902, doi:10.1056/nejm200105103441902. This article has 493 citations and is from a highest quality peer-reviewed journal.

22. (whitledge2024trendsinshortages pages 4-5): James D. Whitledge, Pelayia Soto, Kieran M Glowacki, D. Calello, Erin R Fox, and M. Mazer-Amirshahi. Trends in shortages of lead chelators from 2001 to 2022. The journal of pediatric pharmacology and therapeutics : JPPT : the official journal of PPAG, 29 3:306-315, Jun 2024. URL: https://doi.org/10.5863/1551-6776-29.3.306, doi:10.5863/1551-6776-29.3.306. This article has 7 citations.

23. (porterfield2024asnapshotof pages 3-5): Kate Porterfield, Paromita Hore, Stephen G. Whittaker, Katie M. Fellows, Anshu Mohllajee, Shakoora Azimi-Gaylon, Berna Watson, Isabel Grant, and Richard Fuller. A snapshot of lead in consumer products across four us jurisdictions. Environmental Health Perspectives, Jul 2024. URL: https://doi.org/10.1289/ehp14336, doi:10.1289/ehp14336. This article has 10 citations and is from a highest quality peer-reviewed journal.

24. (stangle2004reductionsinblood pages 5-6): Diane E Stangle, Myla S Strawderman, Donald Smith, Mareike Kuypers, and Barbara J Strupp. Reductions in blood lead overestimate reductions in brain lead following repeated succimer regimens in a rodent model of childhood lead exposure. Environmental Health Perspectives, 112:302-308, Mar 2004. URL: https://doi.org/10.1289/ehp.6517, doi:10.1289/ehp.6517. This article has 41 citations and is from a highest quality peer-reviewed journal.

25. (whitledge2024trendsinshortages pages 1-2): James D. Whitledge, Pelayia Soto, Kieran M Glowacki, D. Calello, Erin R Fox, and M. Mazer-Amirshahi. Trends in shortages of lead chelators from 2001 to 2022. The journal of pediatric pharmacology and therapeutics : JPPT : the official journal of PPAG, 29 3:306-315, Jun 2024. URL: https://doi.org/10.5863/1551-6776-29.3.306, doi:10.5863/1551-6776-29.3.306. This article has 7 citations.

26. (whitledge2024trendsinshortages pages 2-4): James D. Whitledge, Pelayia Soto, Kieran M Glowacki, D. Calello, Erin R Fox, and M. Mazer-Amirshahi. Trends in shortages of lead chelators from 2001 to 2022. The journal of pediatric pharmacology and therapeutics : JPPT : the official journal of PPAG, 29 3:306-315, Jun 2024. URL: https://doi.org/10.5863/1551-6776-29.3.306, doi:10.5863/1551-6776-29.3.306. This article has 7 citations.

27. (whitledge2024trendsinshortages pages 8-10): James D. Whitledge, Pelayia Soto, Kieran M Glowacki, D. Calello, Erin R Fox, and M. Mazer-Amirshahi. Trends in shortages of lead chelators from 2001 to 2022. The journal of pediatric pharmacology and therapeutics : JPPT : the official journal of PPAG, 29 3:306-315, Jun 2024. URL: https://doi.org/10.5863/1551-6776-29.3.306, doi:10.5863/1551-6776-29.3.306. This article has 7 citations.

28. (lanphear2024leadpoisoning. media 5797edb2): Bruce Lanphear, Ana Navas-Acien, and David C. Bellinger. Lead poisoning. The New England journal of medicine, 391 17:1621-1631, Oct 2024. URL: https://doi.org/10.1056/nejmra2402527, doi:10.1056/nejmra2402527. This article has 68 citations and is from a highest quality peer-reviewed journal.
