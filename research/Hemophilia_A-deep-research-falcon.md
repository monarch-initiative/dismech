---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:47.641428'
end_time: '2026-04-25T22:31:58.187524'
duration_seconds: 970.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemophilia A
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemophilia A
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hemophilia A** covering all of the
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
- **Disease Name:** Hemophilia A
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hemophilia A** covering all of the
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


## Comprehensive Disease Characteristics Report: Hemophilia A (Genetic)

### Target disease
Hemophilia A (HA) is a congenital **X‑linked recessive bleeding disorder** caused by pathogenic defects in **F8**, the gene encoding coagulation **factor VIII (FVIII)**, leading to reduced/absent FVIII activity and impaired hemostasis. (li2023f8geneinversion pages 1-2, gupta2024expertopinionson pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Recent primary genetics literature provides a concise definitional statement suitable for a KB entry: **“Hemophilia A (HA, OMIM#306700) is an X‑linked recessive bleeding disorder caused by the defects in the F8 gene, which encodes coagulation factor VIII (FVIII).”** (li2023f8geneinversion pages 1-2)

Severity is defined by baseline FVIII activity; a 2024 expert review lists: mild **0.05–0.4 IU/mL (6%–40%)**, moderate **0.01–0.05 IU/mL (2%–5%)**, and severe **<0.01 IU/mL (<1%)**, with spontaneous bleeding characteristic of severe disease. (gupta2024expertopinionson pages 1-2)

### 1.2 Key identifiers (as available from retrieved sources)
* **OMIM**: **306700** (Hemophilia A) (li2023f8geneinversion pages 1-2, liu2023comprehensiveanalysisof pages 1-2)
* **Causal gene**: **F8** (Factor VIII) (li2023f8geneinversion pages 1-2, chernyi2024recentadvancesin pages 1-3)

**Not available in retrieved full text evidence**: MONDO ID, Orphanet ID, ICD‑10/ICD‑11 codes, MeSH ID. These are commonly available from OMIM/Orphanet/MeSH but were not present in the retrieved documents, so they are not asserted here.

### 1.3 Synonyms and alternative names
* Hemophilia A; **HA** (li2023f8geneinversion pages 1-2, gupta2024expertopinionson pages 1-2)
* Factor VIII deficiency / coagulation factor VIII deficiency (explicitly used as description/synonym) (li2023f8geneinversion pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated)
The evidence in this report is derived from:
* **Aggregated resources**: systematic reviews/meta-analyses and narrative reviews (e.g., emicizumab meta-analysis; gene therapy reviews) (prudente2024emicizumabprophylaxisin pages 6-7, deshpande2024adenoassociatedvirus–basedgene pages 1-2)
* **Clinical trial datasets**: phase 3 GENEr8‑1 long-term follow-up and related analyses (leavitt2024efficacysafetyand pages 1-2, long2024clinicalimmunogenicityoutcomes pages 1-2)
* **Single-center patient series**: perioperative outcomes on emicizumab (rener2023managementandoutcomes pages 1-2)
* **Molecular diagnostic cohorts**: regional/country genetics studies (zhang2023moleculardiagnosisof pages 1-2, li2023f8geneinversion pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause**: germline pathogenic variants in **F8**, which encodes FVIII; HA is X‑linked recessive. (li2023f8geneinversion pages 1-2, chernyi2024recentadvancesin pages 1-3)

### 2.2 Risk factors
#### Genetic risk factors
* **High-impact F8 variants** (e.g., deletions or nonsense variants) are noted to influence risk of developing inhibitory antibodies (inhibitors) to FVIII. A 2024 gene-therapy review states: “risk of developing inhibitory antibodies is influenced by genetic factors such as gene deletion or nonsense mutation on FVIII, as well as ethnicity.” (chernyi2024recentadvancesin pages 3-4)
* A 2024 expert review notes inhibitors can develop in **up to ~30% in severe HA**. (gupta2024expertopinionson pages 2-3)

#### Environmental/clinical risk factors
No specific environmental causal risk factor is established for congenital HA itself (genetic disorder). However, treatment exposure (repeated FVIII infusions) is tied to inhibitor formation risk and to historical infection risks in the plasma-derived era. (chernyi2024recentadvancesin pages 3-4)

### 2.3 Protective factors
No protective genetic variants were identified in the retrieved evidence. Clinically, **achieving higher steady FVIII activity** reduces spontaneous bleeding risk; Roctavian review notes FVIII levels **~12%–20%** protect against spontaneous hemorrhage and joint bleeds. (samelsonjones2024roctaviangenetherapy pages 1-2)

### 2.4 Gene–environment interactions
Not specifically addressed in retrieved evidence for congenital HA.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (current understanding)
* **Bleeding diathesis** ranging from trauma-related to spontaneous bleeds depending on baseline FVIII activity; spontaneous bleeding is characteristic of severe disease (<1% FVIII). (gupta2024expertopinionson pages 1-2, li2023f8geneinversion pages 1-2)
* **Hemarthroses and hemophilic arthropathy** are key complications; patients with inhibitors have greater morbidity including arthropathy and worse quality of life. (prudente2024emicizumabprophylaxisin pages 6-7)

### 3.2 Phenotype characteristics
#### Age of onset
Severe HA often presents early in life; an adult cohort study notes severe cases are “often diagnosed within the first two years of life,” while mild cases may be diagnosed later. (vasava2024astudyof pages 5-6)

#### Severity and progression
Severity is largely determined by baseline FVIII activity (mild/moderate/severe). (gupta2024expertopinionson pages 1-2)
Progression is driven by recurrent bleeding (especially joints), which can lead to chronic arthropathy. (prudente2024emicizumabprophylaxisin pages 6-7)

### 3.3 Quality-of-life impact
A 2024 phase 3 gene-therapy follow-up reports sustained, clinically meaningful improvement in hemophilia-specific HRQoL after valoctocogene roxaparvovec at 4 years (Haemophilia-Specific Quality of Life Questionnaire total score change significant). (leavitt2024efficacysafetyand pages 1-2)

### 3.4 Suggested HPO terms (examples)
Because retrieved texts did not provide an explicit HPO mapping, below are **suggested** HPO concepts for KB normalization (not directly asserted by cited sources):
* Hemarthrosis / joint bleeding: **HP:0003065** (Hemarthrosis)
* Abnormal bleeding: **HP:0001892** (Bleeding)
* Prolonged activated partial thromboplastin time: **HP:0003645** (Abnormality of partial thromboplastin time)
* Hemophilic arthropathy: can be represented via arthropathy terms (e.g., **HP:0002758** Arthritis) + site qualifiers.

**Limitation**: phenotype frequency-by-HPO (percent affected) could not be robustly extracted from the retrieved evidence corpus.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
* **F8** (Factor VIII) is the causal gene for congenital hemophilia A. (li2023f8geneinversion pages 1-2, chernyi2024recentadvancesin pages 1-3)

Gene locus and structure: F8 is located at **Xq28** and comprises **26 exons** and **25 introns** (~186–187 kb), per molecular diagnostic studies. (zhang2023moleculardiagnosisof pages 1-2, li2023f8geneinversion pages 1-2)

### 4.2 Pathogenic variants (variant classes and frequencies)
Hemophilia A shows extensive allelic heterogeneity (thousands of variants catalogued). (zhang2023moleculardiagnosisof pages 1-2)

Key recurrent structural variants in severe HA:
* **Intron 22 inversion (Inv22 / IVS22)**: approximately **45%** of severe HA. (zhang2023moleculardiagnosisof pages 1-2, li2023f8geneinversion pages 1-2)
* **Intron 1 inversion (Inv1 / IVS1)**: approximately **1–2%** of severe HA. (zhang2023moleculardiagnosisof pages 1-2)

Representative abstract quote supporting Inv22 frequency: **“Intron 22 inversion (Inv22) is found in about 45% of patients with severe hemophilia A.”** (li2023f8geneinversion pages 1-2)

### 4.3 Variant detection approaches (molecular diagnostics)
A 2023 molecular study describes a standard workflow: FVIII activity (FVIII:C) by **one-stage clotting assay**, inhibitor titer by **Bethesda assay**, and genetic testing by inversion-specific PCR methods plus NGS with Sanger confirmation. (zhang2023moleculardiagnosisof pages 1-2)

### 4.4 Modifier genes / epigenetics
No congenital HA modifier genes or epigenetic mechanisms were identified in the retrieved evidence set.

### 4.5 Chromosomal abnormalities
Not a dominant mechanism in retrieved evidence beyond F8 inversions/large rearrangements. (zhang2023moleculardiagnosisof pages 1-2)

---

## 5. Environmental Information

### 5.1 Environmental factors
Congenital HA is genetic; no environmental causes were identified. Historical treatment-related infectious risk is documented (HIV/HCV in the 1980s era of plasma products). A 2024 review notes: “Up to 60–70% of individuals with severe hemophilia were found to have contracted HIV in the 1980s, and nearly all of them contracted hepatitis C.” (chernyi2024recentadvancesin pages 3-4)

### 5.2 Lifestyle factors / infectious agents
Not applicable as primary causal factors for congenital HA; infection risk pertains to past treatment-era blood product exposure. (chernyi2024recentadvancesin pages 3-4)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (genotype → phenotype)
1. **F8 pathogenic variant** → reduced/absent FVIII expression or activity. (li2023f8geneinversion pages 1-2)
2. Low FVIII → impaired intrinsic pathway amplification and reduced capacity to generate stable clotting (clinically manifested as prolonged bleeding; severe disease shows spontaneous bleeds). (gupta2024expertopinionson pages 1-2, li2023f8geneinversion pages 1-2)
3. Recurrent bleeding, particularly into joints → chronic joint damage (hemophilic arthropathy) and reduced quality of life. (prudente2024emicizumabprophylaxisin pages 6-7)
4. Therapeutic FVIII exposure can induce **FVIII inhibitors** (alloantibodies) that neutralize infused FVIII, increasing bleeding morbidity and mortality. (prudente2024emicizumabprophylaxisin pages 6-7, gupta2024expertopinionson pages 2-3)

### 6.2 Key molecular/therapeutic mechanisms (2023–2024 understanding)
* **Emicizumab mechanism**: a bispecific antibody that “bridges the gap between activated factor IX and factor X to replace the missing activated factor VIII.” (chernyi2024recentadvancesin pages 5-6)
* **Gene therapy mechanism**: hepatotropic AAV gene addition to enable endogenous expression of B‑domain deleted FVIII; key limitation highlighted is **declining FVIII expression over time** after Roctavian. (samelsonjones2024roctaviangenetherapy pages 1-2)
* **Physiologic FVIII-producing cells**: liver sinusoidal endothelial cells (LSEC) are a natural FVIII source; a 2024 EMBO Mol Med study states: “Coagulation factor VIII (FVIII), the gene mutated in hemophilia A, is naturally expressed by LSEC.” (milani2024gp64pseudotypedlentiviralvectors pages 1-2)

### 6.3 Suggested ontology terms
#### GO (Biological Process) – suggestions
* blood coagulation (GO:0007596)
* hemostasis (GO:0007599)
* regulation of thrombin generation (GO term family; specific mapping may be needed)
* immune response to foreign protein (for inhibitor formation)

#### CL (Cell Ontology) – suggestions
* liver sinusoidal endothelial cell (LSEC)
* hepatocyte
* macrophage / Kupffer cell
* megakaryocyte / platelet lineage (for platelet-targeted FVIII concepts)

#### UBERON – suggestions
* liver (UBERON:0002107)
* synovial joint (UBERON:0000978)

---

## 7. Anatomical Structures Affected

### Organ/system level
* **Blood / hemostasis system** (primary)
* **Joints** (hemarthroses → arthropathy) (prudente2024emicizumabprophylaxisin pages 6-7)

### Tissue/cell level
* Liver-relevant tissues for gene therapy and endogenous FVIII production include hepatocytes and **LSEC** (milani2024gp64pseudotypedlentiviralvectors pages 1-2)

---

## 8. Temporal Development

* **Onset**: congenital; severe disease often recognized early in childhood (often within first two years), while mild disease may be diagnosed later. (vasava2024astudyof pages 5-6)
* **Course**: chronic lifelong without disease-modifying cure; modern prophylaxis and gene therapy aim to reduce or eliminate bleeding episodes. (leavitt2024efficacysafetyand pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance
* X‑linked recessive inheritance (li2023f8geneinversion pages 1-2)

### 9.2 Epidemiology (recent statistics)
* Incidence estimates include **~1 in 5,000 male births**. (zhang2023moleculardiagnosisof pages 1-2, li2023f8geneinversion pages 1-2)
* A 2024 immunogenicity paper states incidence as **“24.6 out of 100,000 males.”** (long2024clinicalimmunogenicityoutcomes pages 1-2)
* Regional prevalence example: pooled prevalence in Africa **6.82 per 100,000 persons** (95% CI 5.16–8.48). (chernyi2024recentadvancesin pages 1-3)

**Limitation**: detailed age distribution, ethnicity-specific prevalence, and global registry-derived prevalence/incidence were not directly retrievable from the available full-text evidence.

---

## 10. Diagnostics

### 10.1 Clinical and laboratory testing
* Screening often begins with **prolonged aPTT**, while PT and platelet count can be normal; confirmatory testing measures FVIII activity. (gupta2024expertopinionson pages 2-3)
* FVIII activity measurement:
  * **One-stage aPTT-based clotting assay** is the most common worldwide. (bowyer2023factorviiiand pages 1-2)
  * **Chromogenic substrate assays** are used in specialized labs; one-stage vs chromogenic assays can disagree in mild HA and for some therapies, including gene therapy monitoring. (bowyer2023factorviiiand pages 1-2)

### 10.2 Inhibitor testing
* Inhibitor titers can be quantified using the **Bethesda assay** (explicitly described in 2023 molecular diagnostic work). (zhang2023moleculardiagnosisof pages 1-2)

### 10.3 Genetic testing
A 2023 diagnostic study lists commonly used inversion detection methods (e.g., inverse-shift PCR, long-distance PCR), and documents use of long-range PCR/multiplex PCR for Inv22/Inv1 plus NGS and Sanger confirmation for other variants. (zhang2023moleculardiagnosisof pages 1-2)

A 2024 expert review emphasizes that >3,500 pathogenic F8 variants are reported, and that NGS and Sanger sequencing improve diagnostic yield and can enable preimplantation genetic diagnosis. (gupta2024expertopinionson pages 15-16)

### 10.4 Differential diagnosis
Not systematically addressed for congenital HA in retrieved evidence (acquired hemophilia A and other causes of prolonged aPTT are discussed in other literature, but not part of this congenital HA evidence set).

---

## 11. Outcome / Prognosis

### Modern outcomes (bleeding control)
Long-term phase 3 data show gene therapy can substantially reduce bleeding and factor usage at 4 years, with many participants experiencing zero treated bleeds in year 4. (leavitt2024efficacysafetyand pages 1-2)

**Limitation**: explicit life expectancy, all-cause mortality, and cause-specific mortality rates were not provided in the retrieved evidence.

---

## 12. Treatment

### 12.1 Standard of care: factor replacement
Regular FVIII replacement (standard or extended half-life products) remains a core prophylaxis approach; limitations include IV administration burden and inhibitor development. (gupta2024expertopinionson pages 2-3, gupta2024expertopinionson pages 1-2)

**MAXO suggestions**:
* clotting factor replacement therapy (MAXO term family)
* prophylactic treatment (MAXO:0000069; confirm exact term mapping in MAXO)

### 12.2 Non-factor prophylaxis: emicizumab
**Evidence of effectiveness**: A 2024 systematic review/meta-analysis in people with HA and inhibitors found lower treated-bleed ABR on emicizumab vs bypassing agents, with standardized mean difference **−1.58** (95% CI −2.50 to −0.66; P=0.0008). (prudente2024emicizumabprophylaxisin pages 6-7)

**Safety considerations**: the same review notes thrombotic events/TMA have been associated with concurrent high-dose aPCC for >1 day; anti-drug antibodies were reported and emicizumab can persist for ~6 months. (prudente2024emicizumabprophylaxisin pages 6-7)

**Real-world implementation**: A 2023 single-center perioperative series (12 procedures in 8 adults on emicizumab) reported **no major bleeds, thrombotic events, deaths, or new inhibitors**, supporting feasibility of surgery with appropriate adjunct hemostasis. (rener2023managementandoutcomes pages 1-2)

**MAXO suggestions**:
* monoclonal antibody therapy
* bleeding prophylaxis

### 12.3 Inhibitors and immune tolerance induction (ITI)
A 2024 gene-therapy review reports ITI success is **~60%–80%**, while **20%–40%** of severe HA patients do not achieve tolerance, with predictors including high peak inhibitor titer and prior failed ITI. (chernyi2024recentadvancesin pages 3-4)

**MAXO suggestions**:
* immune tolerance induction therapy

### 12.4 Advanced therapeutics: AAV gene therapy (Roctavian / valoctocogene roxaparvovec)
**Regulatory status**: Roctavian was conditionally approved in Europe (Aug 2022) and approved in the US (June 2023). (samelsonjones2024roctaviangenetherapy pages 1-2)

**Efficacy at 4 years (GENEr8‑1)**: mean treated ABR reduced **−82.6%** and annualized FVIII infusion rate reduced **−95.5%** vs baseline; in year 4, **81/110** rollover participants had **0 treated bleeds**. Week‑208 chromogenic FVIII activity mean **16.1 IU/dL**, median **6.7 IU/dL**. (leavitt2024efficacysafetyand pages 1-2)

**Comparative effectiveness**: a propensity-score comparison reports treated ABR **4.40 vs 0.85** and all-bleed ABR **5.01 vs 1.54** (FVIII prophylaxis vs valoctocogene roxaparvovec), and zero treated bleeds in **32.9% vs 82.1%** (controls vs treated). (leavitt2024efficacysafetyand pages 1-2)

**Immunogenicity**: “No FVIII inhibitors were detected following administration of valoctocogene roxaparvovec,” and all participants developed durable anti-AAV5 antibodies; pre-existing anti-AAV5 antibodies occur in **29.7%** of people with HA globally. (long2024clinicalimmunogenicityoutcomes pages 1-2)

**Liver safety / monitoring**: ALT elevations are common; GENEr8‑1 year‑4 data report ALT elevation as the most common adverse event (56/131 participants in year 4). (leavitt2024efficacysafetyand pages 1-2)

A 2024 Blood Advances expert guidance paper provides detailed visual guidance for liver monitoring and management of ALT elevations after Roctavian (eligibility workup, monitoring schedule, and a corticosteroid management algorithm). (mura2024liverrelatedaspectsof media 8f4fbc2d, mura2024liverrelatedaspectsof media 4d9b2f5b, mura2024liverrelatedaspectsof media 179ecf90)

---

## 13. Prevention

### Genetic counseling and reproductive options
A 2024 expert review recommends genetic analysis to identify carriers and support counseling; it notes chorionic villous sampling at **11–14 weeks** in carrier pregnancies and that NGS/Sanger sequencing support molecular diagnosis and preimplantation genetic diagnosis approaches. (gupta2024expertopinionson pages 15-16)

### Tertiary prevention (preventing complications)
Prophylaxis to minimize bleeding is emphasized as a strategy to prevent morbidity (e.g., arthropathy), including early prophylaxis approaches. (gupta2024expertopinionson pages 2-3)

---

## 14. Other Species / Natural Disease
The retrieved evidence did not explicitly document naturally occurring hemophilia A in companion animals; it does support broader comparative models including **dogs with hemophilia A** used in research. (chernyi2024recentadvancesin pages 6-8)

---

## 15. Model Organisms

### 15.1 Common models
* **Hemophilia A mouse models**, including Alb‑F8*R593C strain used for gene-therapy studies. (milani2024gp64pseudotypedlentiviralvectors pages 14-15)
* **Dogs with hemophilia A** as large-animal translational models. (chernyi2024recentadvancesin pages 6-8)

### 15.2 Mechanistic relevance of cell types
A 2024 experimental gene-therapy study emphasizes LSECs as physiologic FVIII producers and demonstrates correction of hemophilia A mice by targeting FVIII expression to liver endothelium. (milani2024gp64pseudotypedlentiviralvectors pages 1-2)

---

## Recent developments and real-world implementations (2023–2024 highlights)

1. **Emicizumab** continues to expand real-world use, including perioperative management with favorable outcomes in a single-center series and improved bleed prophylaxis vs bypassing agents in inhibitor populations. (prudente2024emicizumabprophylaxisin pages 6-7, rener2023managementandoutcomes pages 1-2)
2. **Licensed gene therapy** (Roctavian) is supported by 4‑year phase 3 outcomes demonstrating sustained reductions in ABR and factor usage, but with clinically important considerations around ALT elevations and monitoring, plus unanswered questions around FVIII expression durability declines. (samelsonjones2024roctaviangenetherapy pages 1-2, leavitt2024efficacysafetyand pages 1-2, mura2024liverrelatedaspectsof media 8f4fbc2d)

---

## Key quantitative findings table (2023–2024)
| Topic | Key findings (include numbers) | Population/setting | Year | Source (journal) | URL | PMID if available | Evidence citation ID |
|---|---|---|---|---|---|---|---|
| Epidemiology | Hemophilia A incidence in males is about **1/5,000**; one review also reports incidence as **24.6 per 100,000 males** | General population / congenital HA | 2023-2024 | *Global Medical Genetics*; *Molecular Therapy* | https://doi.org/10.1055/s-0043-1774322 ; https://doi.org/10.1016/j.ymthe.2024.05.033 |  | (zhang2023moleculardiagnosisof pages 1-2, long2024clinicalimmunogenicityoutcomes pages 1-2) |
| Epidemiology | Pooled prevalence of HA in Africa: **6.82 cases per 100,000 persons** (95% CI **5.16-8.48**) | Systematic review/meta-analysis of 15 African studies | 2024 | *BMC Public Health* | https://doi.org/10.1186/s12889-024-20165-w |  | (chernyi2024recentadvancesin pages 1-3) |
| Genetics | **Intron 22 inversion (Inv22)** is found in about **45%** of severe HA; **intron 1 inversion** accounts for about **1-2%** of severe HA | Severe congenital HA | 2023 | *Frontiers in Genetics*; *Global Medical Genetics* | https://doi.org/10.3389/fgene.2023.1098795 ; https://doi.org/10.1055/s-0043-1774322 |  | (zhang2023moleculardiagnosisof pages 1-2) |
| Genetics | In a Belarus cohort, **20.4%** had inhibitor history; among severe HA, **45.1% (37/82)** had Inv22 and **1.2% (1/82)** had Inv1; pathogenic F8 variants identified in **99% (97/98)** | 98 patients with HA in Belarus | 2023 | *Pediatric Hematology/Oncology and Immunopathology* | https://doi.org/10.24287/1726-1708-2023-22-3-48-57 |  | (zhang2023moleculardiagnosisof pages 1-2) |
| Diagnostics | FVIII activity and VWF antigen measured by **one-stage clotting assay**; inhibitor titers quantified by **Bethesda assay**; inversion testing by long-range PCR/multiplex PCR, with NGS plus Sanger confirmation for non-inversion variants | Molecular diagnosis workflow in congenital HA | 2023 | *Global Medical Genetics* | https://doi.org/10.1055/s-0043-1774322 |  | (zhang2023moleculardiagnosisof pages 1-2) |
| Diagnostics | The **one-stage aPTT-based assay** is the most commonly used worldwide; **chromogenic substrate assays** are available in specialized labs; assay choice can materially change FVIII results, including in mild HA and during monitoring of replacement products or gene therapy | Laboratory diagnosis/monitoring of HA | 2023 | *Seminars in Thrombosis and Hemostasis* | https://doi.org/10.1055/s-0042-1758870 |  | (bowyer2023factorviiiand pages 1-2) |
| Treatment | In severe HA, inhibitors develop in up to **~30%**; current ITI success is about **60%-80%**, leaving **20%-40%** unsuccessful | Severe congenital HA with inhibitors | 2024 | *Biomolecules*; *Cureus* | https://doi.org/10.3390/biom14070854 ; https://doi.org/10.7759/cureus.c172 |  | (chernyi2024recentadvancesin pages 3-4, gupta2024expertopinionson pages 2-3) |
| Emicizumab safety/effectiveness | Compared with bypassing-agent prophylaxis, emicizumab reduced treated-bleed ABR with standardized mean difference **-1.58** (95% CI **-2.50 to -0.66**, **P=0.0008**); BPA effectiveness reported at **~60%-72%**, and up to **20%** of bleeds may remain uncontrolled on standard BPA regimens | Systematic review/meta-analysis in PwHA with inhibitors | 2024 | *São Paulo Medical Journal* | https://doi.org/10.1590/1516-3180.2023.0102.r1.20022024 |  | (prudente2024emicizumabprophylaxisin pages 6-7) |
| Emicizumab safety/effectiveness | In a perioperative real-world series, **12 procedures** in **8 adults** on emicizumab (3 minor, 9 major) had **no major bleeds, thrombotic events, deaths, or new inhibitors** | Single-center invasive-procedure cohort | 2023 | *Hematology Reports* | https://doi.org/10.3390/hematolrep15040062 |  | (rener2023managementandoutcomes pages 1-2) |
| Gene therapy | In phase 3 GENEr8-1, valoctocogene roxaparvovec achieved **-82.6%** reduction in treated ABR and **-95.5%** reduction in annualized FVIII infusion rate at 4 years; during year 4, **81/110** rollover participants had **0 treated bleeds**; week-208 chromogenic FVIII activity mean **16.1 IU/dL**, median **6.7 IU/dL** | 134 adult males with severe HA, no inhibitors | 2024 | *Research and Practice in Thrombosis and Haemostasis* | https://doi.org/10.1016/j.rpth.2024.102615 |  | (leavitt2024efficacysafetyand pages 1-2) |
| Gene therapy | Propensity-score comparison: mean treated ABR **4.40 vs 0.85** and all-bleed ABR **5.01 vs 1.54** for FVIII prophylaxis vs valoctocogene roxaparvovec; zero treated bleeds in **82.1% vs 32.9%** and zero all bleeds in **58.0% vs 28.5%** | Severe HA: GENEr8-1 treated cohort vs contemporaneous FVIII-prophylaxis controls | 2024 | *Advances in Therapy* | https://doi.org/10.1007/s12325-024-02834-9 |  | (leavitt2024efficacysafetyand pages 1-2) |
| Gene therapy safety | After valoctocogene roxaparvovec, **no FVIII inhibitors** were detected; all participants developed durable anti-AAV5 antibodies; pre-existing anti-AAV5 antibodies occur in **29.7%** of people with HA globally | Phase 3 GENEr8-1 immunogenicity analysis | 2024 | *Molecular Therapy* | https://doi.org/10.1016/j.ymthe.2024.05.033 |  | (long2024clinicalimmunogenicityoutcomes pages 1-2) |
| Gene therapy safety | In year 4 of GENEr8-1, ALT elevation was the most common adverse event: **56/131** participants; another expert guidance source notes **88.8%** of GENEr8-1 participants had ALT elevations overall | Post-gene-therapy liver safety monitoring | 2024 | *Research and Practice in Thrombosis and Haemostasis*; *Blood Advances* | https://doi.org/10.1016/j.rpth.2024.102615 ; https://doi.org/10.1182/bloodadvances.2024013750 |  | (leavitt2024efficacysafetyand pages 1-2, mura2024liverrelatedaspectsof media 8f4fbc2d) |


*Table: This table compiles key quantitative 2023-2024 findings for congenital Hemophilia A across epidemiology, F8 genetics, diagnostic assays, emicizumab use, and gene therapy. It is useful as a quick evidence map for populating a disease knowledge base with recent, citable data.*

---

## Notes on evidence gaps
* MONDO/Orphanet/ICD/MeSH identifiers were not present in the retrieved documents and thus are not verified here.
* Many phenotype frequencies and long-term survival/life expectancy outcomes are typically available in registries (e.g., WFH, national registries) but were not accessible in the retrieved full-text corpus.
* 2023–2024 primary trial outcome data for other non-factor agents (e.g., fitusiran, concizumab) were not present in retrievable full texts; this report therefore focuses on emicizumab and valoctocogene roxaparvovec, which were well supported.


References

1. (li2023f8geneinversion pages 1-2): Shaoying Li, Jianchun He, Liming Chu, Shuai Ren, Wenzhi He, Xiaoyan Ma, Yanchao Wang, Mincong Zhang, Lingyin Kong, Bo Liang, and Qing Li. F8 gene inversion and duplication cause no obvious hemophilia a phenotype. Frontiers in Genetics, Feb 2023. URL: https://doi.org/10.3389/fgene.2023.1098795, doi:10.3389/fgene.2023.1098795. This article has 4 citations and is from a peer-reviewed journal.

2. (gupta2024expertopinionson pages 1-2): Naresh Gupta, Anupam Dutta, Bilal Ahmed, Cecil R Ross, Chandrakala S, Gerard Dolan, M. J. John, Nita Radhakrishnan, Sunita Aggarwal, Tulika Seth, Varun Kaul, and Vijay Shah. Expert opinions on the management of hemophilia a in india: the role of emicizumab. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.c172, doi:10.7759/cureus.c172. This article has 13 citations.

3. (liu2023comprehensiveanalysisof pages 1-2): Yingdi Liu, Dongzhi Li, Dongyi Yu, Qiaowei Liang, Guilan Chen, Fucheng Li, Lu Gao, Zhuo Li, Tiantian Xie, Le Wu, Aiping Mao, Lingqian Wu, and Desheng Liang. Comprehensive analysis of hemophilia a (cahea): towards full characterization of the f8 gene variants by long-read sequencing. Thrombosis and Haemostasis, 123:1151-1164, Jun 2023. URL: https://doi.org/10.1055/a-2107-0702, doi:10.1055/a-2107-0702. This article has 28 citations and is from a domain leading peer-reviewed journal.

4. (chernyi2024recentadvancesin pages 1-3): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Biomolecules, 14:854, Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 40 citations.

5. (prudente2024emicizumabprophylaxisin pages 6-7): Tiago Paiva Prudente, Ricardo Mesquita Camelo, Rafael Alves Guimarães, and Maria do Rosário Ferraz Roberti. Emicizumab prophylaxis in people with hemophilia a and inhibitors: a systematic review and meta-analysis. São Paulo Medical Journal, May 2024. URL: https://doi.org/10.1590/1516-3180.2023.0102.r1.20022024, doi:10.1590/1516-3180.2023.0102.r1.20022024. This article has 1 citations.

6. (deshpande2024adenoassociatedvirus–basedgene pages 1-2): Saarang R. Deshpande, Keerthy Joseph, Jiayi Tong, Yong Chen, Allyson Pishko, and Adam Cuker. Adeno-associated virus–based gene therapy for hemophilia a and b: a systematic review and meta-analysis. Blood Advances, 8:5957-5974, Nov 2024. URL: https://doi.org/10.1182/bloodadvances.2024014111, doi:10.1182/bloodadvances.2024014111. This article has 27 citations and is from a peer-reviewed journal.

7. (leavitt2024efficacysafetyand pages 1-2): Andrew D. Leavitt, Johnny Mahlangu, Priyanka Raheja, Emily Symington, Doris V. Quon, Adam Giermasz, Maria Fernanda López Fernández, Gili Kenet, Gillian Lowe, Nigel S. Key, Carolyn M. Millar, Steven W. Pipe, Bella Madan, Sheng-Chieh Chou, Robert Klamroth, Jane Mason, Hervé Chambost, Flora Peyvandi, Elaine Majerus, Dominic Pepperell, Christine Rivat, Hua Yu, Tara M. Robinson, and Margareth C. Ozelo. Efficacy, safety, and quality of life 4 years after valoctocogene roxaparvovec gene transfer for severe hemophilia a in the phase 3 gener8-1 trial. Research and Practice in Thrombosis and Haemostasis, 8:102615, Nov 2024. URL: https://doi.org/10.1016/j.rpth.2024.102615, doi:10.1016/j.rpth.2024.102615. This article has 37 citations and is from a peer-reviewed journal.

8. (long2024clinicalimmunogenicityoutcomes pages 1-2): Brian R. Long, Tara M. Robinson, Jonathan R.S. Day, Hua Yu, Kelly Lau, Urooj Imtiaz, Kathryn S. Patton, Greg de Hart, Joshua Henshaw, Suresh Agarwal, Christian Vettermann, Stephen J. Zoog, and Soumi Gupta. Clinical immunogenicity outcomes from gener8-1, a phase 3 study of valoctocogene roxaparvovec, an aav5-vectored gene therapy for hemophilia a. Molecular Therapy, 32:2052-2063, Jul 2024. URL: https://doi.org/10.1016/j.ymthe.2024.05.033, doi:10.1016/j.ymthe.2024.05.033. This article has 27 citations and is from a highest quality peer-reviewed journal.

9. (rener2023managementandoutcomes pages 1-2): Karla Rener, Saša Anžej Doma, Martina Fink, Helena Podgornik, and Irena Preložnik Zupan. Management and outcomes of invasive procedures in individuals with hemophilia a on emicizumab prophylaxis: a single center experience. Hematology Reports, 15:597-607, Nov 2023. URL: https://doi.org/10.3390/hematolrep15040062, doi:10.3390/hematolrep15040062. This article has 4 citations.

10. (zhang2023moleculardiagnosisof pages 1-2): Xialin Zhang, Kun Chen, Sicheng Bian, Gang Wang, Xiuyu Qin, Ruijuan Zhang, and Linhua Yang. Molecular diagnosis of hemophilia a and pathogenesis of novel f8 variants in shanxi, china. Global Medical Genetics, 10:247-262, Sep 2023. URL: https://doi.org/10.1055/s-0043-1774322, doi:10.1055/s-0043-1774322. This article has 3 citations.

11. (chernyi2024recentadvancesin pages 3-4): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Biomolecules, 14:854, Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 40 citations.

12. (gupta2024expertopinionson pages 2-3): Naresh Gupta, Anupam Dutta, Bilal Ahmed, Cecil R Ross, Chandrakala S, Gerard Dolan, M. J. John, Nita Radhakrishnan, Sunita Aggarwal, Tulika Seth, Varun Kaul, and Vijay Shah. Expert opinions on the management of hemophilia a in india: the role of emicizumab. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.c172, doi:10.7759/cureus.c172. This article has 13 citations.

13. (samelsonjones2024roctaviangenetherapy pages 1-2): Benjamin J. Samelson-Jones, Juliana C. Small, and Lindsey A. George. Roctavian gene therapy for hemophilia a. Blood Advances, 8:5179-5189, Oct 2024. URL: https://doi.org/10.1182/bloodadvances.2023011847, doi:10.1182/bloodadvances.2023011847. This article has 38 citations and is from a peer-reviewed journal.

14. (vasava2024astudyof pages 5-6): Renuka Vasava, Minal Shastri, Vaishnavi M Rathod, Gayatri Laha, Vaishnovi Vaishnovi, Nipakumari J Patel, Rajani Deshagoni, Prerna Singh, Nandan Joshi, and Darshankumar M Raval. A study of clinical profile and treatment in adult hemophilia patients with special reference to the inhibitor levels. Cureus, Feb 2024. URL: https://doi.org/10.7759/cureus.54663, doi:10.7759/cureus.54663. This article has 2 citations.

15. (chernyi2024recentadvancesin pages 5-6): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Biomolecules, 14:854, Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 40 citations.

16. (milani2024gp64pseudotypedlentiviralvectors pages 1-2): Michela Milani, Cesare Canepari, S. Assanelli, Simone Merlin, Ester Borroni, Francesco Starinieri, Mauro Biffi, Fabio Russo, Anna Fabiano, Desirèe Zambroni, Andrea Annoni, L. Naldini, Antonia Follenzi, and Alessio Cantore. Gp64-pseudotyped lentiviral vectors target liver endothelial cells and correct hemophilia a mice. EMBO Molecular Medicine, 16:1427-1450, Apr 2024. URL: https://doi.org/10.1038/s44321-024-00072-8, doi:10.1038/s44321-024-00072-8. This article has 17 citations and is from a highest quality peer-reviewed journal.

17. (bowyer2023factorviiiand pages 1-2): Annette E. Bowyer and Robert C. Gosselin. Factor viii and factor ix activity measurements for hemophilia diagnosis and related treatments. Seminars in Thrombosis and Hemostasis, 49:609-620, Dec 2023. URL: https://doi.org/10.1055/s-0042-1758870, doi:10.1055/s-0042-1758870. This article has 42 citations and is from a peer-reviewed journal.

18. (gupta2024expertopinionson pages 15-16): Naresh Gupta, Anupam Dutta, Bilal Ahmed, Cecil R Ross, Chandrakala S, Gerard Dolan, M. J. John, Nita Radhakrishnan, Sunita Aggarwal, Tulika Seth, Varun Kaul, and Vijay Shah. Expert opinions on the management of hemophilia a in india: the role of emicizumab. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.c172, doi:10.7759/cureus.c172. This article has 13 citations.

19. (mura2024liverrelatedaspectsof media 8f4fbc2d): Vincenzo La Mura, Vincenzo Cardinale, Raimondo De Cristofaro, Adriano De Santis, Giovanni Di Minno, Luca Fabris, Fabio Marra, Filomena Morisco, Flora Peyvandi, Maurizio Pompili, Cristina Santoro, Ezio Zanon, and Giancarlo Castaman. Liver-related aspects of valoctocogene roxaparvovec gene therapy for hemophilia a: expert guidance for clinical practice. Blood Advances, 8:5725-5734, Nov 2024. URL: https://doi.org/10.1182/bloodadvances.2024013750, doi:10.1182/bloodadvances.2024013750. This article has 11 citations and is from a peer-reviewed journal.

20. (mura2024liverrelatedaspectsof media 4d9b2f5b): Vincenzo La Mura, Vincenzo Cardinale, Raimondo De Cristofaro, Adriano De Santis, Giovanni Di Minno, Luca Fabris, Fabio Marra, Filomena Morisco, Flora Peyvandi, Maurizio Pompili, Cristina Santoro, Ezio Zanon, and Giancarlo Castaman. Liver-related aspects of valoctocogene roxaparvovec gene therapy for hemophilia a: expert guidance for clinical practice. Blood Advances, 8:5725-5734, Nov 2024. URL: https://doi.org/10.1182/bloodadvances.2024013750, doi:10.1182/bloodadvances.2024013750. This article has 11 citations and is from a peer-reviewed journal.

21. (mura2024liverrelatedaspectsof media 179ecf90): Vincenzo La Mura, Vincenzo Cardinale, Raimondo De Cristofaro, Adriano De Santis, Giovanni Di Minno, Luca Fabris, Fabio Marra, Filomena Morisco, Flora Peyvandi, Maurizio Pompili, Cristina Santoro, Ezio Zanon, and Giancarlo Castaman. Liver-related aspects of valoctocogene roxaparvovec gene therapy for hemophilia a: expert guidance for clinical practice. Blood Advances, 8:5725-5734, Nov 2024. URL: https://doi.org/10.1182/bloodadvances.2024013750, doi:10.1182/bloodadvances.2024013750. This article has 11 citations and is from a peer-reviewed journal.

22. (chernyi2024recentadvancesin pages 6-8): Nikita Chernyi, Darina Gavrilova, Mane Saruhanyan, Ezekiel S. Oloruntimehin, Alexander Karabelsky, Evgeny Bezsonov, and Alexander Malogolovkin. Recent advances in gene therapy for hemophilia: projecting the perspectives. Biomolecules, 14:854, Jul 2024. URL: https://doi.org/10.3390/biom14070854, doi:10.3390/biom14070854. This article has 40 citations.

23. (milani2024gp64pseudotypedlentiviralvectors pages 14-15): Michela Milani, Cesare Canepari, S. Assanelli, Simone Merlin, Ester Borroni, Francesco Starinieri, Mauro Biffi, Fabio Russo, Anna Fabiano, Desirèe Zambroni, Andrea Annoni, L. Naldini, Antonia Follenzi, and Alessio Cantore. Gp64-pseudotyped lentiviral vectors target liver endothelial cells and correct hemophilia a mice. EMBO Molecular Medicine, 16:1427-1450, Apr 2024. URL: https://doi.org/10.1038/s44321-024-00072-8, doi:10.1038/s44321-024-00072-8. This article has 17 citations and is from a highest quality peer-reviewed journal.
