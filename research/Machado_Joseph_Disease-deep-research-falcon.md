---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T15:37:03.058889'
end_time: '2026-04-26T15:53:41.564130'
duration_seconds: 998.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Machado-Joseph Disease
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
- **Disease Name:** Machado-Joseph Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Machado-Joseph Disease** covering all of the
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
- **Disease Name:** Machado-Joseph Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Machado-Joseph Disease** covering all of the
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


# Machado–Joseph Disease (Spinocerebellar Ataxia Type 3) — Disease Characteristics Research Report

**Target disease:** Machado–Joseph disease (MJD) / Spinocerebellar ataxia type 3 (SCA3)  
**Category:** Mendelian (autosomal dominant polyglutamine repeat-expansion disorder) (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, NCT02175290 chunk 1)

## Evidence and citation note
This report is based on the documents retrieved in this run (mostly 2023–2024 reviews, cohort studies, and ClinicalTrials.gov records). Many retrieved excerpts did not include PubMed IDs (PMIDs); therefore, where PMIDs are required, I provide DOI/URL and publication month/year, and explicitly flag PMID unavailability in the retrieved context.

---

## 1. Disease Information

### 1.1 Concise overview
Machado–Joseph disease / SCA3 is a monogenic, progressive neurodegenerative ataxia caused by a pathogenic CAG repeat expansion in **ATXN3**, leading to production of polyglutamine-expanded **ataxin-3** that misfolds and aggregates in neurons (potapenko2024thedeubiquitinasefunction pages 1-2, stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2). Clinically, it is characterized by progressive cerebellar ataxia with frequent additional pyramidal, extrapyramidal (including parkinsonism), oculomotor, and peripheral neuropathic features, culminating in severe disability and premature death (potapenko2024thedeubiquitinasefunction pages 1-2, pilotto2024hereditaryataxiasfrom pages 4-5, paulino2023autophagyinspinocerebellar pages 1-2).

### 1.2 Key identifiers and synonyms
A structured summary of disease nomenclature and identifiers supported by the retrieved evidence is provided below.

| Identifier system | Identifier | Evidence-supported? (yes/no) | Notes | Key citation (pqac id) |
|---|---|---|---|---|
| Preferred disease name | Machado–Joseph disease | yes | Monogenic neurodegenerative disorder; also referred to as SCA3 | (potapenko2024thedeubiquitinasefunction pages 1-2, stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2) |
| Major synonym | Spinocerebellar ataxia type 3 | yes | Standard synonym used interchangeably with Machado–Joseph disease | (potapenko2024thedeubiquitinasefunction pages 1-2, stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2) |
| Major synonym | SCA3 | yes | Common abbreviation in clinical and research literature | (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, NCT02175290 chunk 1) |
| Major synonym | MJD | yes | Common abbreviation for Machado–Joseph disease | (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, NCT02175290 chunk 1) |
| OMIM | 109150 | yes | Explicitly reported for SCA3/Machado–Joseph disease in a 2024 review | (pilotto2024hereditaryataxiasfrom pages 4-5) |
| MONDO | MONDO:0007182 | yes | Disease-target association retrieved for Machado-Joseph disease in Open Targets output | (stahl2024spinocerebellarataxiatype pages 1-2) |
| Orphanet disease entry | Orphanet:98757 | yes | Open Targets output mapped “Spinocerebellar ataxia type 3” to Orphanet_98757 | (stahl2024spinocerebellarataxiatype pages 1-2) |
| ICD-10 | Not established from gathered evidence | no | No ICD-10 code was provided in the gathered evidence set | (stahl2024spinocerebellarataxiatype pages 1-2) |
| ICD-11 | Not established from gathered evidence | no | No ICD-11 code was provided in the gathered evidence set | (stahl2024spinocerebellarataxiatype pages 1-2) |
| MeSH | Not established from gathered evidence | no | No MeSH identifier was provided in the gathered evidence set | (stahl2024spinocerebellarataxiatype pages 1-2) |
| Inheritance | Autosomal dominant | yes | Repeatedly described as an autosomal dominant/polyglutamine ataxia | (stahl2024spinocerebellarataxiatype pages 1-2, NCT02175290 chunk 1, raposo2024bloodandcerebellar pages 1-5) |
| Causal gene | ATXN3 | yes | Causative gene; CAG expansion located in exon 10 | (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, NCT02175290 chunk 1) |
| Gene product | Ataxin-3 | yes | Deubiquitinating enzyme involved in proteostasis/transcriptional regulation | (potapenko2024thedeubiquitinasefunction pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2) |
| Molecular lesion | CAG trinucleotide repeat expansion | yes | Produces expanded polyglutamine tract in ataxin-3 | (potapenko2024thedeubiquitinasefunction pages 1-2, stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2) |
| Normal repeat range | ~12–42 CAGs | yes | One evidence source reports normal alleles approximately 12–42 repeats | (stahl2024spinocerebellarataxiatype pages 1-2) |
| Normal repeat range | up to 44 CAGs | yes | Alternative review reports normal range up to 44 repeats | (pilotto2024hereditaryataxiasfrom pages 4-5) |
| Normal/polyQ range reported | ~13–49 glutamines | yes | Review reports normal ataxin-3 polyQ stretch as 13–49 glutamines | (paulino2023autophagyinspinocerebellar pages 1-2) |
| Pathogenic repeat range | ~52–86 CAGs | yes | Review reports affected individuals typically carry 52–86 repeats | (pilotto2024hereditaryataxiasfrom pages 4-5) |
| Pathogenic repeat range | ~55–87 CAGs | yes | Alternative review reports pathogenic expansions 55–87 repeats/glutamines | (paulino2023autophagyinspinocerebellar pages 1-2) |
| Pathogenic repeat range | ~60–87 CAGs | yes | Review reports pathogenic alleles roughly 60–87 repeats | (stahl2024spinocerebellarataxiatype pages 1-2) |
| Major affected regions | Cerebellum and pons | yes | Frequently highlighted as primary affected regions | (paulino2023autophagyinspinocerebellar pages 1-2, sohail2023adifficultcase pages 1-2) |
| Additional affected regions | Brainstem, basal ganglia, substantia nigra/striatum | yes | Broader neurodegeneration beyond cerebellum contributes to phenotypic heterogeneity | (potapenko2024thedeubiquitinasefunction pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, pilotto2024hereditaryataxiasfrom pages 4-5) |


*Table: This table summarizes evidence-supported nomenclature and core identifiers for Machado–Joseph disease / spinocerebellar ataxia type 3. It also flags identifier systems not established by the gathered evidence so the final report can distinguish confirmed from missing database mappings.*

**Key identifier limitations:** ICD-10/ICD-11 and MeSH identifiers were not present in the retrieved evidence for this run; they should be added via dedicated ontology/database lookup if required for the knowledge base entry (artifact-00).

### 1.3 Evidence source type
Most information here comes from **aggregated disease-level resources and cohorts** (reviews and multi-site observational studies), rather than individual EHR case reports, except for one illustrative case report (sohail2023adifficultcase pages 1-2).

---

## 2. Etiology

### 2.1 Primary causal factors
**Genetic cause (primary):** Pathogenic expansion of a CAG trinucleotide repeat in **exon 10 of ATXN3** produces a polyQ-expanded ataxin-3 protein with toxic gain-of-function properties leading to neuronal dysfunction and degeneration (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2). ATXN3 encodes a deubiquitinating enzyme involved in proteostasis and other functions (potapenko2024thedeubiquitinasefunction pages 1-2).

**Repeat-size ranges (current evidence):**
- Normal: reported approximately **12–42** repeats (stahl2024spinocerebellarataxiatype pages 1-2) or “up to 44” (pilotto2024hereditaryataxiasfrom pages 4-5).
- Pathogenic: typically **~52–86** repeats (pilotto2024hereditaryataxiasfrom pages 4-5) and/or **~55–87** repeats (paulino2023autophagyinspinocerebellar pages 1-2), with some sources describing typical patient ranges **~62–84** (potapenko2024thedeubiquitinasefunction pages 1-2).

### 2.2 Risk factors
**Genetic risk factor:** Carrying the pathogenic ATXN3 expansion is necessary and (age-dependently) sufficient for disease development in autosomal dominant families (stahl2024spinocerebellarataxiatype pages 1-2, NCT02175290 chunk 1).

**Modifier effects (repeat size):** Larger expanded alleles correlate with **earlier age at onset** and greater severity (potapenko2024thedeubiquitinasefunction pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, silva2023thejosephindomain pages 1-2).

**Other genetic/molecular modifiers (emerging):**
- **ATXN3 transcript diversity/splicing:** ATXN3 has extensive alternative splicing; blood vs cerebellum show strong isoform differences (e.g., ATXN3-251 vs ATXN3-214), which may influence selective vulnerability and mRNA-lowering therapy design (raposo2024bloodandcerebellar pages 1-5).
- **Post-transcriptional regulation:** miRNA families and Dicer/Drosha-dependent processing are discussed as modulators of ATXN3 levels (stahl2024spinocerebellarataxiatype pages 1-2).

### 2.3 Protective factors
No specific protective variants or environmental protective factors were identified in the retrieved evidence. The closest related concept is **incomplete penetrance** early in life with age-dependent conversion to symptomatic disease (see Epidemiology/Inheritance) (paulino2023autophagyinspinocerebellar pages 1-2).

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was retrieved in this run.

---

## 3. Phenotypes

### 3.1 Core clinical phenotype and common manifestations
SCA3/MJD is characterized by progressive ataxia with multi-system involvement.

**Commonly described manifestations (from retrieved evidence):**
- **Cerebellar ataxia** (core feature) (paulino2023autophagyinspinocerebellar pages 1-2)
- **Pyramidal and extrapyramidal signs**; **parkinsonism** in some subtypes (pilotto2024hereditaryataxiasfrom pages 4-5, paulino2023autophagyinspinocerebellar pages 1-2)
- **Oculomotor abnormalities** including diplopia/ophthalmoparesis (moura2024spinocerebellarataxiasphenotypic pages 7-9)
- **Peripheral neuropathy** (often axonal sensory) and muscle cramps/atrophy in some subtypes (pilotto2024hereditaryataxiasfrom pages 4-5, moura2024spinocerebellarataxiasphenotypic pages 7-9)
- Dysarthria/dysphagia are highlighted as major disabling features in reviews (potapenko2024thedeubiquitinasefunction pages 1-2)

**Subtype classification (clinical heterogeneity):** A 2024 review describes four clinical subtypes:  
Type I (early onset ~10–30 years; pyramidal/extrapyramidal signs), Type II (most common; onset 2nd–5th decades), Type III (later onset; prominent peripheral neuropathy and muscle atrophy), Type IV (parkinsonism) (pilotto2024hereditaryataxiasfrom pages 4-5).

### 3.2 Quantitative phenotype data (examples from 2024 cohorts)
- In a tertiary ataxia cohort enriched for polyQ SCAs (dominated by MJD/SCA3), **axonal neuropathy** was observed in **16/22 (72.7%)** of polyQ cases evaluated (moura2024spinocerebellarataxiasphenotypic pages 7-9).
- MRI findings in polyQ SCA included **pons** and **cerebellar peduncle** atrophy each in **9/28 (32.1%)** (moura2024spinocerebellarataxiasphenotypic pages 7-9).

### 3.3 Age of onset, severity, progression
- Typical adult onset often falls around the **3rd–5th decades** (median ~39.5 years reported for polyQ SCAs in one cohort; MJD/SCA3 predominant) (moura2024spinocerebellarataxiasphenotypic pages 1-2).
- Disease is progressive and life-limiting. After symptom onset, survival is reported as ~**20–25 years** in a 2024 review, and patients often become wheelchair dependent later in disease (potapenko2024thedeubiquitinasefunction pages 1-2). Another large biomarker study notes clinical ataxia progression over ~**20 years** on average (faber2024stage‐dependentbiomarkerchanges pages 4-7).

### 3.4 Suggested HPO terms (non-exhaustive; evidence-aligned)
- Cerebellar ataxia — **HP:0001251** (paulino2023autophagyinspinocerebellar pages 1-2)
- Dysarthria — **HP:0001260** (potapenko2024thedeubiquitinasefunction pages 1-2)
- Dysphagia — **HP:0002015** (potapenko2024thedeubiquitinasefunction pages 1-2)
- Ophthalmoparesis — **HP:0000602** (moura2024spinocerebellarataxiasphenotypic pages 7-9)
- Peripheral neuropathy / axonal neuropathy — **HP:0009830** (moura2024spinocerebellarataxiasphenotypic pages 7-9)
- Parkinsonism — **HP:0001300** (pilotto2024hereditaryataxiasfrom pages 4-5, paulino2023autophagyinspinocerebellar pages 1-2)
- Muscle atrophy — **HP:0003202** (pilotto2024hereditaryataxiasfrom pages 4-5)

*Ontology note:* HPO IDs are suggested standard mappings; the retrieved documents support the phenotypes but did not themselves provide HPO IDs.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **ATXN3 (ataxin 3)** is the causal gene; CAG repeat expansion in exon 10 is the canonical lesion (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2).

### 4.2 Variant type and consequences
- Variant class: **trinucleotide repeat expansion (CAG)** → **polyglutamine expansion** (stahl2024spinocerebellarataxiatype pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2).
- Functional consequence: **toxic gain of function** with protein misfolding/aggregation and inclusion formation (stahl2024spinocerebellarataxiatype pages 1-2, potapenko2024thedeubiquitinasefunction pages 1-2).

### 4.3 Allele frequency and population databases
Population allele frequencies (e.g., gnomAD) were not available in the retrieved evidence.

### 4.4 Molecular modifiers (selected, evidence-supported)
- **Alternative splicing / isoform usage** differs markedly between blood and cerebellum; this may affect selective vulnerability and design/interpretation of blood biomarkers for target engagement (raposo2024bloodandcerebellar pages 1-5).
- **miRNA-mediated regulation** (miR-181/miR-25 family, miR-9, miR-494) and dependency on Dicer/Drosha are cited as modulators of ATXN3 expression (stahl2024spinocerebellarataxiatype pages 1-2).

---

## 5. Environmental Information
No environmental toxins, lifestyle factors, or infectious triggers were identified in the retrieved evidence set.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
**ATXN3 CAG expansion → polyQ-expanded ataxin-3 → misfolding/aggregation/inclusions → impaired proteostasis (UPS and autophagy), transcriptional and mitochondrial dysfunction (including mitophagy defects and oxidative stress) → selective neurodegeneration (brainstem/cerebellar circuitry and other regions) → progressive motor and multisystem phenotype** (potapenko2024thedeubiquitinasefunction pages 1-2, paulino2023autophagyinspinocerebellar pages 1-2, paulino2023autophagyinspinocerebellar pages 4-5, cui2024spinocerebellarataxiasfrom pages 5-6).

### 6.2 Protein dysfunction and proteostasis
- PolyQ-expanded ataxin-3 has propensity to **misfold, aggregate, and form intranuclear inclusions** containing ubiquitin and proteasomal subunits, supporting impaired clearance and UPS involvement (potapenko2024thedeubiquitinasefunction pages 1-2).
- Ataxin-3 is a **deubiquitinating enzyme** with key roles in proteostasis; UPS impairment is a central mechanistic link to neurodegeneration in MJD (potapenko2024thedeubiquitinasefunction pages 1-2).

**Suggested GO terms (Biological Process; evidence-aligned):**
- Protein ubiquitination / deubiquitination — e.g., **GO:0016567**, **GO:0016579** (potapenko2024thedeubiquitinasefunction pages 1-2)
- Proteasome-mediated ubiquitin-dependent protein catabolic process — **GO:0043161** (potapenko2024thedeubiquitinasefunction pages 1-2)

### 6.3 Autophagy impairment (2023 synthesis; therapeutic relevance)
Autophagy is highlighted as critical for clearance of large oligomeric/aggregated species that are poorly handled by the UPS (paulino2023autophagyinspinocerebellar pages 4-5). Reported disease-associated findings include reduced **beclin-1** in patient fibroblasts and altered LC3-II/p62 patterns in MJD brain, consistent with impaired autophagic flux (paulino2023autophagyinspinocerebellar pages 4-5).

**Suggested GO terms:**
- Autophagy — **GO:0006914** (paulino2023autophagyinspinocerebellar pages 4-5, paulino2023autophagyinspinocerebellar pages 1-2)
- Macroautophagy — **GO:0016236** (paulino2023autophagyinspinocerebellar pages 4-5)

### 6.4 Mitochondrial dysfunction, oxidative stress, and mitophagy (2024 emphasis)
- A 2024 review describes impaired **Parkin/VDAC1-mediated mitophagy** linked to mutant ataxin-3 (aberrant loss of Parkin and reduced VDAC1 polyubiquitination), highlighting the **PINK1/Parkin axis** as a therapeutic target (cui2024spinocerebellarataxiasfrom pages 5-6).
- A 2024 experimental study in an MJD cell model (SK-N-SH expressing mutant ataxin-3) links mutant ataxin-3 toxicity to oxidative stress and mitochondrial dysfunction; **astragaloside IV** reduced mutant ataxin-3 aggregation by enhancing autophagy, improving antioxidant capacity, and improving mitochondrial membrane potential/respiration and dynamics (lin2024astragalosideivreduces pages 1-2).

**Suggested GO terms:**
- Mitophagy — **GO:0000422** (cui2024spinocerebellarataxiasfrom pages 5-6)
- Mitochondrial organization — **GO:0007005** (lin2024astragalosideivreduces pages 1-2)
- Response to oxidative stress — **GO:0006979** (lin2024astragalosideivreduces pages 1-2)

### 6.5 Transcriptional and post-transcriptional dysregulation (2024 review)
A 2024 review notes promoter-binding factors (SP1/CBF), limited CpG methylation findings, and miRNA-mediated regulation of ATXN3; a CRISPR-based endogenous reporter screen identified statins as potential activators of ATXN3 expression, suggesting cholesterol-related biology may be relevant (stahl2024spinocerebellarataxiatype pages 1-2).

### 6.6 Immune system involvement
Neuroinflammation was not substantively addressed in the retrieved excerpts and should be treated as a gap for this run.

**Suggested cell types (CL; evidence-aligned but not directly measured in retrieved excerpts):**
- Purkinje neuron — **CL:0000121** (Purkinje dysfunction/degeneration discussed in model contexts) (pilotto2024hereditaryataxiasfrom pages 13-15, paulino2023autophagyinspinocerebellar pages 4-5)
- Oligodendrocyte — **CL:0000128** (transcriptional abnormalities in some SCA3 models cited indirectly) (shorrock2024cagrepeatselectivecompounds pages 54-55)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary system affected: **central nervous system** (neurodegenerative ataxia) (potapenko2024thedeubiquitinasefunction pages 1-2, stahl2024spinocerebellarataxiatype pages 1-2).

### 7.2 Key regions (human neuropathology/imaging)
- Cerebellum and **pons/brainstem** are repeatedly highlighted as major affected structures (paulino2023autophagyinspinocerebellar pages 1-2).
- Degeneration also involves deep cerebellar nuclei (dentate), and in some cases substantia nigra/basal ganglia/cortex contributing to parkinsonism and cognitive changes (pilotto2024hereditaryataxiasfrom pages 4-5).

**Suggested UBERON terms (examples):**
- Cerebellum — **UBERON:0002037** (paulino2023autophagyinspinocerebellar pages 1-2)
- Pons — **UBERON:0000986** (paulino2023autophagyinspinocerebellar pages 1-2, moura2024spinocerebellarataxiasphenotypic pages 7-9)
- Substantia nigra — **UBERON:0002038** (pilotto2024hereditaryataxiasfrom pages 4-5)

### 7.3 Subcellular localization
Nuclear and cytoplasmic inclusion bodies are described (stahl2024spinocerebellarataxiatype pages 1-2, potapenko2024thedeubiquitinasefunction pages 1-2).

**Suggested GO Cellular Component:**
- Nucleus — **GO:0005634** (stahl2024spinocerebellarataxiatype pages 1-2)

---

## 8. Temporal Development (Natural History)

### 8.1 Onset and course
Typical onset is often in adulthood (e.g., ~30–50 years in polyQ cohorts; subtype-dependent) (pilotto2024hereditaryataxiasfrom pages 4-5, moura2024spinocerebellarataxiasphenotypic pages 1-2). Disease is progressive over decades, commonly described as ~20 years from manifest onset (potapenko2024thedeubiquitinasefunction pages 1-2, faber2024stage‐dependentbiomarkerchanges pages 4-7).

### 8.2 Biomarker-defined pre-ataxic window (major 2024 development)
A major 2024 advance is a **biomarker-led staging framework** anchored to onset.

| Study (year, journal) | Cohort (n) | Biomarkers | Key quantitative findings (with units and timing relative to onset) | Proposed model / implications | URL | Key citation (pqac) |
|---|---:|---|---|---|---|---|
| Faber et al. (2024, *Annals of Neurology*) | 292 SCA3 mutation carriers + 108 controls; 57 pre-ataxic, 235 ataxic | Plasma elongated/mutant ATXN3, serum neurofilament light (NfL), MRI volumes of pons, cerebellar white matter (CWM), cerebellar gray matter (CGM), SARA | Mutant ATXN3 elevated before and after onset (trait marker). NfL deviated from normal ~11.9 years before onset. Pons volume deviated ~2.0 years before onset; CWM volume ~0.3 years before onset. In manifest ataxia, NfL z-score ≥2 in 174/190 (92%); pons/CWM z-scores ≤-2 in ~90% of assessed patients. Multivariable model including NfL/MRI explained 73.9% of SARA variance vs 60.4% without them. SARA cutoff for manifest ataxia: ≥3. (faber2024stage‐dependentbiomarkerchanges pages 1-4, faber2024stage‐dependentbiomarkerchanges pages 4-7, faber2024stage‐dependentbiomarkerchanges pages 15-21, faber2024stage‐dependentbiomarkerchanges pages 7-9) | Data-driven 3-stage model: asymptomatic carrier → biomarker stage (pre-ataxic but NfL abnormal) → ataxia stage; supports biomarker-led early/preventive trial design and staging for targeted therapies. Figure extraction also retrieved staging/trajectory panels. (faber2024stage‐dependentbiomarkerchanges pages 9-12, faber2024stage‐dependentbiomarkerchanges pages 12-15, faber2024stage‐dependentbiomarkerchanges media b30f008b, faber2024stage‐dependentbiomarkerchanges media 807d2b9d) | https://doi.org/10.1002/ana.26824 | (faber2024stage‐dependentbiomarkerchanges pages 1-4, faber2024stage‐dependentbiomarkerchanges pages 4-7, faber2024stage‐dependentbiomarkerchanges pages 15-21, faber2024stage‐dependentbiomarkerchanges pages 7-9, faber2024stage‐dependentbiomarkerchanges pages 9-12, faber2024stage‐dependentbiomarkerchanges pages 12-15, faber2024stage‐dependentbiomarkerchanges media b30f008b, faber2024stage‐dependentbiomarkerchanges media 807d2b9d) |
| Faber et al. (2024, *Annals of Neurology*) — cohort detail row | MRI available in 161; mutant ATXN3 in 134; NfL in 327 measurements across participants | Same as above | Mean age 35.5 years in pre-ataxic carriers and 51.3 years in ataxic carriers; pre-ataxic carriers averaged ~7.7 years before onset; expanded CAG mean ~68.2–68.8 repeats. Clinical disease duration after onset described as ~20 years on average. (faber2024stage‐dependentbiomarkerchanges pages 4-7, faber2024stage‐dependentbiomarkerchanges pages 15-21) | Quantifies the “pre-ataxic window” during which fluid biomarkers become abnormal well before clear structural MRI changes, relevant for enrichment of future interventional studies. | https://doi.org/10.1002/ana.26824 | (faber2024stage‐dependentbiomarkerchanges pages 4-7, faber2024stage‐dependentbiomarkerchanges pages 15-21) |
| Raposo et al. (2024, *bioRxiv* preprint) | Blood n=60; cerebellum n=12 | RNA-seq abundance of ATXN3 splice variants/transcripts in blood and cerebellum | Higher number/abundance of ATXN3 transcripts in cerebellum than blood. ATXN3-251 (3 UIM) expressed ~50-fold more in blood than cerebellum; ATXN3-214 (2 UIM) expressed ~20-fold more in cerebellum than blood. (raposo2024bloodandcerebellar pages 1-5) | Tissue-specific transcript usage may refine molecular biomarker development and improve design of ATXN3 mRNA-lowering therapies by indicating which isoforms dominate in target tissue vs accessible blood. | https://doi.org/10.1101/2023.04.22.537936 | (raposo2024bloodandcerebellar pages 1-5) |
| Moura et al. (2024, *Cerebellum*) — phenotype/imaging cohort relevant to staging | 88 SCA patients total; 38 polyQ SCA cases, of which MJD/SCA3 represented 73.7% of polyQ families/cases | Clinical scales (SARA, INAS), EMG-defined axonal neuropathy, MRI atrophy patterns | PolyQ SCA median age at onset 39.5 years; axonal neuropathy in 16/22 (72.7%) of polyQ cases; pons and cerebellar peduncle atrophy each in 9/28 (32.1%) of polyQ cases. Falls, gait aid use, and wheelchair confinement were tracked as disability milestones. (moura2024spinocerebellarataxiasphenotypic pages 7-9, moura2024spinocerebellarataxiasphenotypic pages 9-10, moura2024spinocerebellarataxiasphenotypic pages 1-2) | Not a biomarker-staging paper per se, but supports real-world structural and functional milestones that align with brainstem/cerebellar degeneration and progression in MJD/SCA3-dominant polyQ cohorts. | https://doi.org/10.1007/s12311-024-01723-9 | (moura2024spinocerebellarataxiasphenotypic pages 7-9, moura2024spinocerebellarataxiasphenotypic pages 9-10, moura2024spinocerebellarataxiasphenotypic pages 1-2) |


*Table: This table summarizes the most relevant 2023-2024 biomarker and staging evidence for Machado-Joseph disease / SCA3, highlighting the quantitative timing of NfL and MRI changes relative to clinical onset. It is useful for identifying current candidate biomarkers, pre-ataxic disease stages, and implications for trial design.*

Key quantitative staging points (ESMI cohort): **NfL becomes abnormal ~11.9 years before ataxia onset**, while pons and cerebellar white matter volume changes deviate closer to onset; mutant ATXN3 in blood is elevated across stages but is less progression-sensitive (faber2024stage‐dependentbiomarkerchanges pages 7-9, faber2024stage‐dependentbiomarkerchanges pages 1-4).

**Visual evidence (figures):** Biomarker trajectories and the proposed carrier/biomarker/ataxia staging model were retrieved as figure crops (faber2024stage‐dependentbiomarkerchanges media b30f008b, faber2024stage‐dependentbiomarkerchanges media 807d2b9d).

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal dominant inheritance is consistently described (stahl2024spinocerebellarataxiatype pages 1-2, NCT02175290 chunk 1).

### 9.2 Penetrance and anticipation-like behavior
- **Age-dependent penetrance/incomplete penetrance** is noted, with probability of remaining asymptomatic approaching zero by age 70 (paulino2023autophagyinspinocerebellar pages 1-2).
- Repeat-length associations (longer CAG → earlier onset, more severe disease) underpin intergenerational anticipation-like patterns (paulino2023autophagyinspinocerebellar pages 1-2, silva2023thejosephindomain pages 1-2).

### 9.3 Epidemiology and geographic distribution (statistics from recent sources)
- Global prevalence estimates in retrieved sources include **~1–5 per 100,000** (paulino2023autophagyinspinocerebellar pages 1-2) and **~1:50,000–100,000** (silva2023thejosephindomain pages 1-2).
- **Founder/high-prevalence regions:** The **Azores** are repeatedly described as a hotspot with particularly high predominance (paulino2023autophagyinspinocerebellar pages 1-2, silva2023thejosephindomain pages 1-2). A 2024 review notes SCA3 can account for **>55%** of autosomal dominant cerebellar ataxia (ADCA) cases in countries such as Portugal (pilotto2024hereditaryataxiasfrom pages 4-5).

**Data gaps:** Incidence, variant-specific geographic distributions/haplotypes, and sex ratio were not available in the retrieved excerpts.

---

## 10. Diagnostics

### 10.1 Genetic testing (real-world implementation)
**Repeat-expansion testing remains central** for suspected polyQ SCAs:
- A cohort study describes use of **multiplex PCR + fragment analysis** to test CAG expansions in a panel including **ATXN3**, alongside targeted single-gene testing and multigene NGS/WES panels (moura2024spinocerebellarataxiasphenotypic pages 2-4).

**Diagnostic yields (single center cohort):**
- Targeted single-gene testing in probands with a suspected diagnosis: **76.9% (20/26)** yield (moura2024spinocerebellarataxiasphenotypic pages 2-4).
- Multigene NGS/WES-based panels: **64.3% (18/28)** yield; no WGS cases were reported in that cohort (moura2024spinocerebellarataxiasphenotypic pages 2-4, moura2024spinocerebellarataxiasphenotypic pages 7-9).

**Clinical trial genetic confirmation threshold:** An intrathecal ASO trial required genetically confirmed SCA3 with **ATXN3 CAG repeats ≥60** (NCT05160558 chunk 1).

### 10.2 Diagnostic delay (quantitative, 2023)
A Brazilian retrospective study (1999–2017; n=428 symptomatic individuals included) reported **median diagnostic delay 5 years** (IQR ~3–8.75). Index cases had longer delays than non-index relatives (median 6 vs 4 years) (pinheiro2023diagnosticdelayof pages 2-5).

### 10.3 Biomarkers and imaging in diagnostic/staging workflows (2024)
- Blood **NfL** and plasma mutant ATXN3, alongside MRI volumes of pons and cerebellar compartments, are being used to define pre-ataxic “biomarker stage” vs manifest ataxia in large cohorts, which may inform future diagnostic and preventive-trial strategies (faber2024stage‐dependentbiomarkerchanges pages 7-9, faber2024stage‐dependentbiomarkerchanges pages 4-7).

**Data gaps:** Differential diagnosis lists, standardized ICD/DSM-like criteria, and formal guidance on WES/WGS sensitivity for expansions were not retrieved in this run.

---

## 11. Outcome / Prognosis
SCA3/MJD is progressive with severe disability and reduced life expectancy:
- A 2024 review reports that advanced disease often leads to wheelchair dependence and survival after symptom onset of approximately **20–25 years** (potapenko2024thedeubiquitinasefunction pages 1-2).
- In a Portuguese cohort context, average life expectancy reduction of **~5.6 years** vs general population (for deceased patients, all of whom had MJD/SCA3) was reported (moura2024spinocerebellarataxiasphenotypic pages 9-10).

---

## 12. Treatment

### 12.1 Current standard of care
No disease-modifying therapy is established; management is largely supportive/symptomatic (paulino2023autophagyinspinocerebellar pages 1-2, sohail2023adifficultcase pages 1-2).

**Suggested MAXO terms (examples):**
- Symptomatic treatment — **NCIT:C15986** (supportive care; general) (sohail2023adifficultcase pages 1-2)
- Physical therapy / rehabilitation — **MAXO:0000012** (not directly evidenced in retrieved excerpts; include only if supported by additional sources)

### 12.2 Disease-modifying and experimental therapeutics (2023–2024 emphasis)

#### 12.2.1 Antisense oligonucleotides (ASOs)
- **BIIB132** (intrathecal ASO targeting ATXN3 pre-mRNA): Phase 1, randomized, placebo-controlled; **terminated**; **enrollment 8**; completion **2023-07-25** (ClinicalTrials.gov **NCT05160558**) (NCT05160558 chunk 1). The major role of NfL/MRI staging work is to support early-stage trials, and the biomarker paper notes initiation of this ASO safety trial (faber2024stage‐dependentbiomarkerchanges pages 4-7).
- A 2024 review reports additional ASO development such as **VO659** in Phase 1/2a (ClinicalTrials.gov **NCT05822908**) (stahl2024spinocerebellarataxiatype pages 6-7).

#### 12.2.2 Autophagy-targeting and small-molecule approaches
- **Trehalose (SLS-005)**: A 2024 review reports tolerability in a small Phase 2 and an ongoing larger IV trial (ClinicalTrials.gov **NCT05490563**) (stahl2024spinocerebellarataxiatype pages 6-7). Autophagy impairment is a core mechanistic rationale (paulino2023autophagyinspinocerebellar pages 4-5).
- **Lithium carbonate**: A 2024 review notes lack of efficacy in a double-blind placebo-controlled Phase 2 trial in ~63 SCA3 patients (pilotto2024hereditaryataxiasfrom pages 20-22). ClinicalTrials.gov includes a completed lithium trial in SCA3 (**NCT01096082**) (NCT05160558 chunk 1).
- **Astragaloside IV** (preclinical, 2024): reduced mutant ataxin-3 levels/aggregation in a cell model while improving oxidative stress and mitochondrial quality control (lin2024astragalosideivreduces pages 1-2).

#### 12.2.3 Gene suppression/editing (preclinical landscape)
Preclinical RNAi/shRNA/siRNA and CRISPR strategies have demonstrated reduction of ataxin-3 aggregation and improvement in motor/neuropathology readouts in models (pilotto2024hereditaryataxiasfrom pages 13-15, cui2024spinocerebellarataxiasfrom pages 6-7). Delivery and safety remain major translational barriers (cui2024spinocerebellarataxiasfrom pages 6-7, stahl2024spinocerebellarataxiatype pages 6-7).

#### 12.2.4 Neuromodulation and supportive-device interventions (real-world trials)
ClinicalTrials.gov records indicate multiple non-pharmacologic trials in MJD/SCA3, including deep TMS (NCT02039206), rTMS (NCT05502432), and a gait intervention using lower-limb weighting (NCT02906046) (NCT02175290 chunk 1). Detailed outcomes were not available in the retrieved trial excerpts for this run.

---

## 13. Prevention
Because SCA3/MJD is monogenic, “prevention” primarily centers on genetic counseling, family-based cascade testing, and early identification of mutation carriers.

**Evidence-supported elements from retrieved sources:**
- A Brazilian diagnostic workflow explicitly distinguishes **direct mutation testing** for individuals from families with known molecular diagnosis versus stepwise panel testing for index cases (pinheiro2023diagnosticdelayof pages 2-5).
- A 2024 biomarker study supports identification of a **pre-ataxic biomarker stage** (~12 years pre-onset NfL rise), suggesting feasibility of preventive/early-intervention trials in carriers before frank ataxia (faber2024stage‐dependentbiomarkerchanges pages 7-9).

**Data gaps:** Formal guidelines for prenatal testing/PGT, and specific genetic counseling recommendations were not retrieved in this run.

---

## 14. Other Species / Natural Disease
No naturally occurring (non-experimental) veterinary SCA3/MJD analogs were identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Model systems used (with evidence)
- **Human cellular models:** patient fibroblasts; iPSC-derived neural models; CRISPR-corrected iPSCs with restored function/electrophysiology (cui2024spinocerebellarataxiasfrom pages 6-7).
- **Rodents:** mouse and rat models used to recapitulate inclusions, Purkinje neuron dysfunction/degeneration, motor deficits; responsive to RNAi/ASO/shRNA interventions in preclinical studies (pilotto2024hereditaryataxiasfrom pages 13-15, cui2024spinocerebellarataxiasfrom pages 9-10).
- **Zebrafish:** transgenic models used for aggregation/autophagy-related phenotypes and rapid screening (cui2024spinocerebellarataxiasfrom pages 9-10).
- **Invertebrates:** Drosophila and C. elegans used in modifier screens; Drosophila expression of expanded human ATXN3 reproduces aspects of SCA3 phenotype (stahl2024spinocerebellarataxiatype pages 6-7, silva2023thejosephindomain pages 1-2).

### 15.2 Model limitations (evidence-aligned)
Key limitations highlighted include delivery barriers (BBB, invasive dosing for ASOs), need for repeated administration, and translational uncertainty from preclinical success to clinical efficacy (cui2024spinocerebellarataxiasfrom pages 6-7, cui2024spinocerebellarataxiasfrom pages 9-10).

---

# Recent developments (2023–2024) — synthesis highlights
1. **Biomarker staging and early disease window:** Large cohort work proposes a carrier → biomarker → ataxia staging model, with **NfL abnormal ~11.9 years pre-onset** (faber2024stage‐dependentbiomarkerchanges pages 7-9, faber2024stage‐dependentbiomarkerchanges media b30f008b, faber2024stage‐dependentbiomarkerchanges media 807d2b9d).
2. **Therapeutic pipeline maturation but setbacks:** Intrathecal ATXN3 ASO trial **NCT05160558** terminated after a small Phase 1 exposure; multiple other approaches (e.g., trehalose IV, VO659) continue (NCT05160558 chunk 1, stahl2024spinocerebellarataxiatype pages 6-7).
3. **Mechanistic refinement:** Reviews emphasize convergent impairment of proteostasis (UPS/autophagy) and mitochondrial quality control (mitophagy via Parkin/VDAC1; PINK1/Parkin) as actionable targets (cui2024spinocerebellarataxiasfrom pages 5-6, paulino2023autophagyinspinocerebellar pages 4-5).
4. **Molecular stratification for mRNA-lowering:** Tissue-specific ATXN3 splice variant abundance differences provide a concrete consideration for target engagement biomarkers and isoform coverage (raposo2024bloodandcerebellar pages 1-5).

---

# Key limitations of this run (for knowledge base completion)
- ICD-10/ICD-11 and MeSH identifiers were not retrieved and should be filled via dedicated ontology lookup.
- Many sources in this run were reviews; primary literature PMIDs were not consistently present in the retrieved excerpts.
- Environmental risk/protective factors, gene–environment interactions, neuroinflammation details, and formal prevention/counseling guidelines were not captured in the retrieved evidence set.


References

1. (stahl2024spinocerebellarataxiatype pages 1-2): Fabian Stahl, Bernd O. Evert, Xinyu Han, Peter Breuer, and Ullrich Wüllner. Spinocerebellar ataxia type 3 pathophysiology—implications for translational research and clinical studies. International Journal of Molecular Sciences, 25:3984, Apr 2024. URL: https://doi.org/10.3390/ijms25073984, doi:10.3390/ijms25073984. This article has 14 citations.

2. (paulino2023autophagyinspinocerebellar pages 1-2): Rodrigo T. Paulino and Clévio Nóbrega. Autophagy in spinocerebellar ataxia type 3: from pathogenesis to therapeutics. International Journal of Molecular Sciences, 24:7405, Apr 2023. URL: https://doi.org/10.3390/ijms24087405, doi:10.3390/ijms24087405. This article has 28 citations.

3. (NCT02175290 chunk 1):  Machado-Joseph Disease in Israel. Meir Medical Center. 2014. ClinicalTrials.gov Identifier: NCT02175290

4. (potapenko2024thedeubiquitinasefunction pages 1-2): Anastasiya Potapenko, Jennilee M. Davidson, Albert Lee, and Angela S. Laird. The deubiquitinase function of ataxin-3 and its role in the pathogenesis of machado-joseph disease and other diseases. Biochemical Journal, 481:461-480, Mar 2024. URL: https://doi.org/10.1042/bcj20240017, doi:10.1042/bcj20240017. This article has 10 citations and is from a domain leading peer-reviewed journal.

5. (pilotto2024hereditaryataxiasfrom pages 4-5): Federica Pilotto, Andrea Del Bondio, and Hélène Puccio. Hereditary ataxias: from bench to clinic, where do we stand? Cells, 13:319, Feb 2024. URL: https://doi.org/10.3390/cells13040319, doi:10.3390/cells13040319. This article has 23 citations.

6. (raposo2024bloodandcerebellar pages 1-5): Mafalda Raposo, Jeannette Hübener-Schmid, Rebecca Tagett, Ana F. Ferreira, Ana Rosa Vieira Melo, João Vasconcelos, Paula Pires, Teresa Kay, Hector Garcia-Moreno, Paola Giunti, Magda M. Santana, Luis Pereira de Almeida, Jon Infante, Bart P. van de Warrenburg, Jeroen J. de Vries, Jennifer Faber, Thomas Klockgether, Nicolas Casadei, Jakob Admard, Ludger Schöls, Olaf Riess, Maria do Carmo Costa, and Manuela Lima. Blood and cerebellar abundance of <i>atxn3</i> splice variants in spinocerebellar ataxia type 3/machado-joseph disease. BioRxiv, Apr 2024. URL: https://doi.org/10.1101/2023.04.22.537936, doi:10.1101/2023.04.22.537936. This article has 8 citations.

7. (sohail2023adifficultcase pages 1-2): Muhammad Sohail, Ajmal Ghoauri, N. Butt, M. Rasheed, Muhammad Umair Javed, Fahmina Ashfaq, Fcps Mbbs, Dr. Dur-e-Sabeh, and Mbbs House Physician. A difficult case to diagnose: machado-joseph disease/spinocerebellar ataxia type iii. Journal of Aziz Fatimah Medical &amp; Dental College, 5:71-73, Dec 2023. URL: https://doi.org/10.55279/jafmdc.v5i2.260, doi:10.55279/jafmdc.v5i2.260. This article has 0 citations.

8. (silva2023thejosephindomain pages 1-2): Rita Sousa e Silva, André Dias Sousa, Jorge Vieira, and Cristina P. Vieira. The josephin domain (jd) containing proteins are predicted to bind to the same interactors: implications for spinocerebellar ataxia type 3 (sca3) studies using drosophila melanogaster mutants. Frontiers in Molecular Neuroscience, Mar 2023. URL: https://doi.org/10.3389/fnmol.2023.1140719, doi:10.3389/fnmol.2023.1140719. This article has 7 citations.

9. (moura2024spinocerebellarataxiasphenotypic pages 7-9): João Moura, Jorge Oliveira, Mariana Santos, Sara Costa, Lénia Silva, Carolina Lemos, José Barros, Jorge Sequeiros, and Joana Damásio. Spinocerebellar ataxias: phenotypic spectrum of polyq versus non-repeat expansion forms. Cerebellum (London, England), 23:2258-2268, Jul 2024. URL: https://doi.org/10.1007/s12311-024-01723-9, doi:10.1007/s12311-024-01723-9. This article has 2 citations.

10. (moura2024spinocerebellarataxiasphenotypic pages 1-2): João Moura, Jorge Oliveira, Mariana Santos, Sara Costa, Lénia Silva, Carolina Lemos, José Barros, Jorge Sequeiros, and Joana Damásio. Spinocerebellar ataxias: phenotypic spectrum of polyq versus non-repeat expansion forms. Cerebellum (London, England), 23:2258-2268, Jul 2024. URL: https://doi.org/10.1007/s12311-024-01723-9, doi:10.1007/s12311-024-01723-9. This article has 2 citations.

11. (faber2024stage‐dependentbiomarkerchanges pages 4-7): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

12. (paulino2023autophagyinspinocerebellar pages 4-5): Rodrigo T. Paulino and Clévio Nóbrega. Autophagy in spinocerebellar ataxia type 3: from pathogenesis to therapeutics. International Journal of Molecular Sciences, 24:7405, Apr 2023. URL: https://doi.org/10.3390/ijms24087405, doi:10.3390/ijms24087405. This article has 28 citations.

13. (cui2024spinocerebellarataxiasfrom pages 5-6): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.

14. (lin2024astragalosideivreduces pages 1-2): Yongshiou Lin, Wenling Cheng, Juichih Chang, Yuling Wu, Mingli Hsieh, and Chin-San Liu. Astragaloside iv reduces mutant ataxin-3 levels and supports mitochondrial function in spinocerebellar ataxia type 3. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-77763-2, doi:10.1038/s41598-024-77763-2. This article has 2 citations and is from a peer-reviewed journal.

15. (pilotto2024hereditaryataxiasfrom pages 13-15): Federica Pilotto, Andrea Del Bondio, and Hélène Puccio. Hereditary ataxias: from bench to clinic, where do we stand? Cells, 13:319, Feb 2024. URL: https://doi.org/10.3390/cells13040319, doi:10.3390/cells13040319. This article has 23 citations.

16. (shorrock2024cagrepeatselectivecompounds pages 54-55): Hannah K. Shorrock, Asmer Aliyeva, Jesus A. Frias, Victoria A. DeMeo, Claudia D. Lennon, Cristina C. DeMeo, Amy K. Mascorro, Sharon Shaughnessy, Hormoz Mazdiyasni, John D. Cleary, Kaalak Reddy, Sweta Vangaveti, Damian S. Shin, and J. Andrew Berglund. Cag repeat-selective compounds reduce abundance of expanded cag rnas in patient cell and murine models of scas. bioRxiv, Aug 2024. URL: https://doi.org/10.1101/2024.08.17.608349, doi:10.1101/2024.08.17.608349. This article has 2 citations.

17. (faber2024stage‐dependentbiomarkerchanges pages 1-4): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

18. (faber2024stage‐dependentbiomarkerchanges pages 15-21): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

19. (faber2024stage‐dependentbiomarkerchanges pages 7-9): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

20. (faber2024stage‐dependentbiomarkerchanges pages 9-12): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

21. (faber2024stage‐dependentbiomarkerchanges pages 12-15): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

22. (faber2024stage‐dependentbiomarkerchanges media b30f008b): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

23. (faber2024stage‐dependentbiomarkerchanges media 807d2b9d): Jennifer Faber, Moritz Berger, Carlo Wilke, Jeannette Hubener‐Schmid, Tamara Schaprian, Magda M. Santana, Marcus Grobe‐Einsler, Demet Onder, Berkan Koyak, Paola Giunti, Hector Garcia‐Moreno, Cristina Gonzalez‐Robles, Manuela Lima, Mafalda Raposo, Ana Rosa Vieira Melo, Luís Pereira de Almeida, Patrick Silva, Maria M. Pinto, Bart P. van de Warrenburg, Judith van Gaalen, Jeroen de Vries, Gulin Oz, James M. Joers, Matthis Synofzik, Ludger Schols, Olaf Riess, Jon Infante, Leire Manrique, Dagmar Timmann, Andreas Thieme, Heike Jacobi, Kathrin Reetz, Imis Dogan, Chiadikaobi Onyike, Michal Povazan, Jeremy Schmahmann, Eva‐Maria Ratai, Matthias Schmid, and Thomas Klockgether. Stage‐dependent biomarker changes in spinocerebellar ataxia type 3. Annals of Neurology, 95:400-406, Dec 2024. URL: https://doi.org/10.1002/ana.26824, doi:10.1002/ana.26824. This article has 36 citations and is from a highest quality peer-reviewed journal.

24. (moura2024spinocerebellarataxiasphenotypic pages 9-10): João Moura, Jorge Oliveira, Mariana Santos, Sara Costa, Lénia Silva, Carolina Lemos, José Barros, Jorge Sequeiros, and Joana Damásio. Spinocerebellar ataxias: phenotypic spectrum of polyq versus non-repeat expansion forms. Cerebellum (London, England), 23:2258-2268, Jul 2024. URL: https://doi.org/10.1007/s12311-024-01723-9, doi:10.1007/s12311-024-01723-9. This article has 2 citations.

25. (moura2024spinocerebellarataxiasphenotypic pages 2-4): João Moura, Jorge Oliveira, Mariana Santos, Sara Costa, Lénia Silva, Carolina Lemos, José Barros, Jorge Sequeiros, and Joana Damásio. Spinocerebellar ataxias: phenotypic spectrum of polyq versus non-repeat expansion forms. Cerebellum (London, England), 23:2258-2268, Jul 2024. URL: https://doi.org/10.1007/s12311-024-01723-9, doi:10.1007/s12311-024-01723-9. This article has 2 citations.

26. (NCT05160558 chunk 1):  A Pharmacokinetics and Safety Study of BIIB132 in Adults With Spinocerebellar Ataxia 3. Biogen. 2022. ClinicalTrials.gov Identifier: NCT05160558

27. (pinheiro2023diagnosticdelayof pages 2-5): Jordânia dos Santos Pinheiro, Lucas Schenatto Sena, Karina Carvalho Donis, Gabriel Vasata Furtado, Maria Luiza Saraiva-Pereira, and Laura Bannach Jardim. Diagnostic delay of hereditary ataxias in brazil: the case of machado-joseph disease. The Cerebellum, 22:348-354, Apr 2023. URL: https://doi.org/10.1007/s12311-022-01404-5, doi:10.1007/s12311-022-01404-5. This article has 3 citations.

28. (stahl2024spinocerebellarataxiatype pages 6-7): Fabian Stahl, Bernd O. Evert, Xinyu Han, Peter Breuer, and Ullrich Wüllner. Spinocerebellar ataxia type 3 pathophysiology—implications for translational research and clinical studies. International Journal of Molecular Sciences, 25:3984, Apr 2024. URL: https://doi.org/10.3390/ijms25073984, doi:10.3390/ijms25073984. This article has 14 citations.

29. (pilotto2024hereditaryataxiasfrom pages 20-22): Federica Pilotto, Andrea Del Bondio, and Hélène Puccio. Hereditary ataxias: from bench to clinic, where do we stand? Cells, 13:319, Feb 2024. URL: https://doi.org/10.3390/cells13040319, doi:10.3390/cells13040319. This article has 23 citations.

30. (cui2024spinocerebellarataxiasfrom pages 6-7): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.

31. (cui2024spinocerebellarataxiasfrom pages 9-10): Zi-Ting Cui, Zong-Tao Mao, Rong Yang, Jia-Jia Li, Shan-Shan Jia, Jian-Li Zhao, Fang-Tian Zhong, Peng Yu, and Ming Dong. Spinocerebellar ataxias: from pathogenesis to recent therapeutic advances. Frontiers in Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnins.2024.1422442, doi:10.3389/fnins.2024.1422442. This article has 32 citations and is from a peer-reviewed journal.
