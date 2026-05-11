---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T14:45:57.219282'
end_time: '2026-05-10T14:56:01.118066'
duration_seconds: 603.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ALG12-congenital disorder of glycosylation
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ALG12-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG12-congenital disorder of glycosylation** covering all of the
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
- **Disease Name:** ALG12-congenital disorder of glycosylation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ALG12-congenital disorder of glycosylation** covering all of the
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


# ALG12–Congenital Disorder of Glycosylation (ALG12‑CDG; historical CDG‑Ig) — Disease Characteristics Research Report

## Executive summary
ALG12‑CDG is a very rare autosomal recessive congenital disorder of glycosylation caused by deficiency of the ER luminal α1,6‑mannosyltransferase ALG12, which catalyzes addition of the 8th mannose during lipid‑linked oligosaccharide (LLO) assembly for protein N‑glycosylation. Biochemically it produces a type‑I carbohydrate‑deficient transferrin pattern and characteristic accumulation of truncated LLO/N‑glycans (notably Man7 intermediates and reduced Man8/Man9 species), with multisystem disease that often includes neurodevelopmental impairment, growth failure, dysmorphism, immunodeficiency (hypogammaglobulinemia), coagulation abnormalities, and variable severity up to early death. Recent (2023–2024) literature emphasizes accelerated CDG diagnosis via WES/WGS and emerging multi‑omics/proteomics tools, but also highlights the ongoing lack of targeted therapies for most CDGs, including ALG12‑CDG. (grubenmann2002alg12mannosyltransferasedefect pages 1-2, grubenmann2002alg12mannosyltransferasedefect pages 2-3, ziburova2021anovelhomozygous pages 1-1, monticelli2023congenitaldisordersof pages 1-2, pascoal2024revisitingtheimmunopathology pages 4-6)

## Abbreviations
CDG: congenital disorder(s) of glycosylation; ER: endoplasmic reticulum; LLO: lipid‑linked oligosaccharide; Tf IEF: transferrin isoelectric focusing; MALDI‑TOF: matrix‑assisted laser desorption/ionization time‑of‑flight; MS: mass spectrometry; WES/WGS: whole‑exome/whole‑genome sequencing.

---

## 1. Disease information
### 1.1 What is the disease?
The first molecularly defined report described “a deficiency in the ALG12 ER α1,6‑mannosyltransferase resulting in a novel type of glycosylation disorder” and explicitly stated: “The ALG12 mannosyltransferase defect defines a new type of congenital disorder of glycosylation, designated CDG‑Ig.” (Grubenmann et al., 2002‑09; Human Molecular Genetics; DOI https://doi.org/10.1093/hmg/11.19.2331) (grubenmann2002alg12mannosyltransferasedefect pages 1-2)

A later case report defined the entity as: “Congenital disorder of glycosylation type Ig (ALG12‑CDG) is a rare inherited metabolic disease caused by a defect in alpha‑mannosyltransferase 8, encoded by the ALG12 gene (22q13.33).” (Ziburová et al., 2021‑09; American Journal of Medical Genetics A; DOI https://doi.org/10.1002/ajmg.a.62474) (ziburova2021anovelhomozygous pages 1-1)

### 1.2 Key identifiers
* **MONDO**: **MONDO_0011783** (“ALG12‑congenital disorder of glycosylation”) (OpenTargets disease identifier) (OpenTargets Search: ALG12-congenital disorder of glycosylation-ALG12)
* **OMIM/MIM**: Literature excerpts report **#607143** (ziburova2021anovelhomozygous pages 2-2, sturiale2019alg12cdgnovelglycophenotype pages 1-2); one excerpt reported **OMIM: 607144** (tahata2019complexphenotypesin pages 1-2). These inconsistencies indicate that a direct OMIM lookup is recommended for knowledge‑base normalization.
* **Orphanet / ICD‑10 / ICD‑11 / MeSH**: Not present in the retrieved full texts; would require direct lookup in those databases (limitation of current tool‑retrieved corpus).

### 1.3 Synonyms / alternative names
* ALG12‑CDG (ziburova2021anovelhomozygous pages 1-1)
* ALG12‑congenital disorder of glycosylation (ziburova2021anovelhomozygous pages 7-8)
* CDG‑Ig (historical) (grubenmann2002alg12mannosyltransferasedefect pages 1-2)
* “ALG12 mannosyltransferase defect” / “ALG12 α1,6‑mannosyltransferase deficiency” (functional descriptor) (grubenmann2002alg12mannosyltransferasedefect pages 1-2, sturiale2019alg12cdgnovelglycophenotype pages 1-2)

### 1.4 Evidence sources
Most disease‑specific information is derived from **individual patient case reports/series** plus **aggregated reviews** of CDG (e.g., immunopathology and diagnostic evolution). (grubenmann2002alg12mannosyltransferasedefect pages 1-2, tahata2019complexphenotypesin pages 1-2, monticelli2023congenitaldisordersof pages 1-2, pascoal2024revisitingtheimmunopathology pages 4-6)

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause (genetic):** biallelic pathogenic variants in **ALG12**, encoding an ER mannosyltransferase involved in N‑glycan precursor assembly. (ziburova2021anovelhomozygous pages 2-2, grubenmann2002alg12mannosyltransferasedefect pages 1-2)

Mechanistic definition from a 2021 report: ALG12 encodes “the dolichyl‑P‑mannose Man‑7‑GlcNAc‑2‑PP‑dolichyl‑alpha‑6‑mannosyltransferase,” and “this enzyme transfers the eighth mannose residue from dolichyl‑P‑mannose to lipid‑linked oligosaccharides.” (Ziburová et al., 2021‑09; DOI https://doi.org/10.1002/ajmg.a.62474) (ziburova2021anovelhomozygous pages 2-2)

### 2.2 Risk factors
* **Genetic risk factors (causal variants):** autosomal‑recessive inheritance; risk elevated in families with carrier parents and potentially consanguinity (not directly documented in retrieved excerpts). (ziburova2021anovelhomozygous pages 2-2)
* **Environmental risk factors:** none established for causation in current evidence; clinical complications (e.g., infections) are downstream consequences.

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not specifically described for ALG12‑CDG in the retrieved evidence. In CDG more broadly, host glycan alterations may influence host–pathogen interactions, but ALG12‑specific GxE data were not retrieved. (pascoal2024revisitingtheimmunopathology pages 1-2)

---

## 3. Phenotypes (clinical features)
ALG12‑CDG presents as a **multisystem disorder** with marked inter‑individual variability.

### 3.1 Core phenotype spectrum (human evidence)
* **Neurodevelopmental**: psychomotor delay/intellectual disability and hypotonia are prominent; the index case had “psychomotor retardation” and “hypotonia.” (grubenmann2002alg12mannosyltransferasedefect pages 1-2)
* **Growth / nutrition**: growth retardation/failure to thrive, feeding problems/anorexia. (grubenmann2002alg12mannosyltransferasedefect pages 1-2, ziburova2021anovelhomozygous pages 5-5)
* **Craniofacial / dysmorphism**: characteristic dysmorphism described across cases. (grubenmann2002alg12mannosyltransferasedefect pages 1-2, ziburova2021anovelhomozygous pages 5-5)
* **Immunologic / infection susceptibility**: low immunoglobulins and recurrent infections; the index case had “markedly low immunoglobulins” and recurrent pneumonias requiring immunoglobulin infusions. (grubenmann2002alg12mannosyltransferasedefect pages 2-3)
* **Coagulation**: low antithrombin and other coagulation factor abnormalities; e.g., low antithrombin reported in multiple cases. (grubenmann2002alg12mannosyltransferasedefect pages 2-3, sturiale2019alg12cdgnovelglycophenotype pages 6-8)
* **Genitourinary / endocrine‑related**: male genital anomalies such as “micropenis” and undescended testes in the original case. (grubenmann2002alg12mannosyltransferasedefect pages 2-3)
* **Skeletal**: skeletal abnormalities reported as frequent across published cases. (ziburova2021anovelhomozygous pages 5-5)

A 2021 synthesis of published cases reported frequent features including: “characteristic dysmorphism, psychomotor retardation, hypotonia, and/or skeletal abnormalities,” and also noted “feeding difficulties, respiratory distress, and frequent infections.” (Ziburová et al., 2021‑09; DOI https://doi.org/10.1002/ajmg.a.62474) (ziburova2021anovelhomozygous pages 5-5)

### 3.2 Age of onset, severity, progression
* **Onset** is typically **congenital/neonatal or early infancy**, consistent with CDG type I disorders; a 2021 report describes evaluation in a “newborn” with significant biochemical abnormalities. (ziburova2021anovelhomozygous pages 1-1)
* **Severity is variable**, ranging from severe infantile lethal multisystem disease to milder presentations; a 2019 case series described three brothers including one who “died at 18 months” and two survivors with comparatively milder disease. (tahata2019complexphenotypesin pages 1-2)

### 3.3 Quality of life impact
Direct QoL instrument data specific to ALG12‑CDG were not captured in the retrieved texts. Real‑world impact is inferred from multisystem disability (developmental delay, recurrent infections, feeding problems).

### 3.4 Suggested HPO terms (examples)
(ontology suggestions; not exhaustive)
* Developmental delay — HP:0001263
* Intellectual disability — HP:0001249
* Hypotonia — HP:0001252
* Growth delay / failure to thrive — HP:0001508 / HP:0001507
* Microcephaly — HP:0000252 (reported in some cases) (sturiale2019alg12cdgnovelglycophenotype pages 6-8)
* Recurrent respiratory infections — HP:0002205 (supported by recurrent pneumonias/infections) (grubenmann2002alg12mannosyltransferasedefect pages 2-3, ziburova2021anovelhomozygous pages 5-5)
* Hypogammaglobulinemia — HP:0004313 (grubenmann2002alg12mannosyltransferasedefect pages 2-3, pascoal2024revisitingtheimmunopathology pages 4-6)
* Abnormal coagulation / prolonged aPTT — HP:0011014 / HP:0030842 (sturiale2019alg12cdgnovelglycophenotype pages 6-8)
* Cryptorchidism — HP:0000028; Micropenis — HP:0000054 (grubenmann2002alg12mannosyltransferasedefect pages 2-3)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
* **ALG12** (approved symbol used in OpenTargets; Ensembl ENSG00000182858) (OpenTargets Search: ALG12-congenital disorder of glycosylation-ALG12)

### 4.2 Pathogenic variant classes (examples from primary reports)
Reported variants include missense, frameshift, and (in later literature) intronic splice‑altering variants; most evidence supports **loss‑of‑function or hypomorphic loss‑of‑function**. (grubenmann2002alg12mannosyltransferasedefect pages 1-2, tahata2019complexphenotypesin pages 1-2, ziburova2021anovelhomozygous pages 1-1)

Examples:
* Compound heterozygous missense: **T67M** and **R146Q** in the first report. (grubenmann2002alg12mannosyltransferasedefect pages 1-2)
* Frameshift: **c.1001delA (p.N334TfsX15)** reported in a family case series. (tahata2019complexphenotypesin pages 1-2)
* Missense: **c.1439T>C (p.Leu480Pro)** reported as homozygous in a Slovak patient. (ziburova2021anovelhomozygous pages 1-1)
* Compound heterozygous missense: **c.367G>A (p.Gly123Arg)** and **c.1439T>C (p.Leu480Pro)** in another patient. (sturiale2019alg12cdgnovelglycophenotype pages 6-8)

Population frequency note (limited): p.Leu480Pro was described as having a very low ExAC frequency (“8 × 10−6”). (sturiale2019alg12cdgnovelglycophenotype pages 6-8)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
No ALG12‑CDG‑specific modifier genes, epigenetic mechanisms, or recurrent chromosomal abnormalities were identified in the retrieved texts.

---

## 5. Environmental information
ALG12‑CDG is a **Mendelian** disorder primarily driven by biallelic ALG12 variants; no consistent non‑genetic causal environmental exposures were identified.

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (from gene defect to biochemical signature)
1. **ALG12 enzymatic defect in ER N‑glycan precursor assembly**: ALG12 adds the 8th mannose residue during LLO synthesis. (ziburova2021anovelhomozygous pages 2-2, pascoal2024revisitingtheimmunopathology pages 4-6)
2. **Truncated LLO accumulation**: patient fibroblasts showed accumulation of **DolPP‑GlcNAc2Man7** and absence of mature **DolPP‑GlcNAc2Man9Glc3**. (grubenmann2002alg12mannosyltransferasedefect pages 2-3)
3. **Transfer of truncated glycans to proteins → hypoglycosylation**: serum transferrin IEF shows a type‑I CDG pattern (decreased tetrasialotransferrin with increased disialo/asialo forms). (grubenmann2002alg12mannosyltransferasedefect pages 2-3)
4. **Systemic multisystem disease** due to widespread hypoglycosylation affecting secreted and membrane proteins (neurodevelopment, immunity, coagulation, endocrine axes). (grubenmann2002alg12mannosyltransferasedefect pages 2-3, pascoal2024revisitingtheimmunopathology pages 4-6)

### 6.2 Biochemical abnormalities in serum glycomics
A 2021 report found MS evidence of impaired ALG12 activity: “analysis of neutral serum N‑glycans by mass spectrometry revealed the accumulation of GlcNAc2Man5–7 and decreased levels of GlcNAc2Man8–9.” (ziburova2021anovelhomozygous pages 1-1)

### 6.3 Immune involvement (expert synthesis)
A 2024 immunopathology review classifies ALG12‑CDG among “predominantly antibody deficiencies” characterized by “hypogammaglobulinemia and low IgG.” (Pascoal et al., 2024‑03; Frontiers in Immunology; DOI https://doi.org/10.3389/fimmu.2024.1350101) (pascoal2024revisitingtheimmunopathology pages 3-4, pascoal2024revisitingtheimmunopathology pages 4-6)

Mechanistic framing in the same review: defective glycosylation can lead to “defective antibody glycosylation,” reducing stability and Fc receptor binding, likely contributing to antibody deficiency and infection susceptibility. (pascoal2024revisitingtheimmunopathology pages 4-6)

### 6.4 Suggested GO / CL / pathway terms (examples)
* **GO Biological Process**: protein N‑linked glycosylation; dolichol‑linked oligosaccharide biosynthetic process.
* **GO Cellular Component**: endoplasmic reticulum membrane; ER lumen.
* **Cell Ontology (CL)**: B cell (CL:0000236), plasma cell (CL:0000786), hepatocyte (CL:0000182), neuron (CL:0000540) — reflecting immune, liver/coagulation, and neurodevelopmental involvement.
* **Reactome/KEGG pathway concept**: N‑glycan precursor (LLO) biosynthesis in ER (ALG3/ALG9/ALG12 steps referenced in CDG literature). (pascoal2024revisitingtheimmunopathology pages 4-6)

---

## 7. Anatomical structures affected
Based on reported phenotypes and biochemical effects:
* **Central nervous system** (neurodevelopmental delay, hypotonia) (UBERON:0000955 — brain)
* **Immune system** (hypogammaglobulinemia, infections) (UBERON:0002405 — immune system)
* **Liver / plasma protein production** (coagulation factors, antithrombin, transaminases) (UBERON:0002107 — liver) (grubenmann2002alg12mannosyltransferasedefect pages 2-3, ziburova2021anovelhomozygous pages 5-5)
* **Male reproductive system** (micropenis, cryptorchidism) (UBERON:0000079 — male reproductive system) (grubenmann2002alg12mannosyltransferasedefect pages 2-3)

Subcellular localization relevant to mechanism: **endoplasmic reticulum** (GO:0005783) consistent with ER mannosyltransferase role and LLO assembly. (grubenmann2002alg12mannosyltransferasedefect pages 1-2, ziburova2021anovelhomozygous pages 2-2)

---

## 8. Temporal development
* **Typical onset**: congenital/neonatal or infancy (newborn presentation and early‑life diagnosis described). (ziburova2021anovelhomozygous pages 1-1)
* **Course**: variable; severe early fatal disease has been reported as well as longer survival with chronic multisystem impairment. (tahata2019complexphenotypesin pages 1-2, ziburova2021anovelhomozygous pages 5-5)

No formal staging system specific to ALG12‑CDG was identified.

---

## 9. Inheritance and population
### 9.1 Inheritance
**Autosomal recessive**, supported by homozygous and compound heterozygous cases. (ziburova2021anovelhomozygous pages 2-2, sturiale2019alg12cdgnovelglycophenotype pages 6-8)

### 9.2 Epidemiology
Robust incidence/prevalence estimates for ALG12‑CDG were not found in the retrieved evidence. However, multiple primary sources emphasize extreme rarity:
* “To date, only 15 patients have been diagnosed with ALG12‑CDG globally.” (Ziburová et al., 2021‑09; DOI https://doi.org/10.1002/ajmg.a.62474) (ziburova2021anovelhomozygous pages 1-1)
* Another excerpt states the Slovak case “brings the total number of published cases of this subtype to 16.” (ziburova2021anovelhomozygous pages 5-5)

---

## 10. Diagnostics
### 10.1 Clinical biochemical tests
**Transferrin isoelectric focusing / carbohydrate‑deficient transferrin**
* Index case evidence: transferrin IEF demonstrated decreased tetrasialotransferrin with increased disialo/asialotransferrin (type‑I CDG pattern). (grubenmann2002alg12mannosyltransferasedefect pages 2-3)

**Lipid‑linked oligosaccharide analysis (patient fibroblasts)**
* Demonstrated accumulation of truncated **DolPP‑GlcNAc2Man7** and loss of mature **DolPP‑GlcNAc2Man9Glc3**. (grubenmann2002alg12mannosyltransferasedefect pages 2-3)

**Serum N‑glycan profiling by MS**
* “Accumulation of GlcNAc2Man5–7 and decreased levels of GlcNAc2Man8–9” in neutral serum N‑glycans. (ziburova2021anovelhomozygous pages 1-1)

### 10.2 Genetic testing
**Exome/genome sequencing** is widely used for CDG diagnosis broadly. A 2023 review states: “CDG diagnosis has been at a rapid pace since the introduction of whole‑exome/whole‑genome sequencing as a diagnostic tool.” (Monticelli et al., 2023‑08; Orphanet J Rare Dis; DOI https://doi.org/10.1186/s13023-023-02852-w) (monticelli2023congenitaldisordersof pages 1-2)

The same review also emphasizes: “genetic analysis is the most reliable diagnostic.” (monticelli2023congenitaldisordersof pages 14-15)

### 10.3 Differential diagnosis
A comprehensive differential diagnosis list specific to ALG12‑CDG was not present in the retrieved texts. Practically, it overlaps with other **CDG type I (LLO assembly/transfer) disorders**, where transferrin IEF abnormalities prompt gene‑panel/WES/WGS confirmation.

---

## 11. Outcome / prognosis
Evidence indicates **variable prognosis**:
* Severe early‑fatal multisystem disease is reported (e.g., infant death in a sibling group; fatal neonatal/infant outcomes in some cases). (tahata2019complexphenotypesin pages 1-2, ziburova2021anovelhomozygous pages 5-5)
* Survivors can have chronic neurodevelopmental disability and recurrent infections. (tahata2019complexphenotypesin pages 1-2, grubenmann2002alg12mannosyltransferasedefect pages 2-3)

Quantitative survival curves or life expectancy estimates specific to ALG12‑CDG were not found in retrieved texts.

---

## 12. Treatment
### 12.1 Disease‑modifying therapy
No ALG12‑CDG‑specific disease‑modifying therapy was identified in the retrieved evidence.

### 12.2 Supportive and rehabilitative care (real‑world implementation)
* **Immunoglobulin replacement** has been used in cases with hypogammaglobulinemia; the index case received “regular immunoglobulin infusions.” (grubenmann2002alg12mannosyltransferasedefect pages 2-3)
* However, the 2024 immunopathology review notes that Ig infusion “attempts” in some ALG12‑CDG patients showed “apparent lack of success” (case‑dependent; limited published evidence). (pascoal2024revisitingtheimmunopathology pages 4-6)
* Additional supportive management is implied by disease manifestations (infection management, nutritional support, coagulation monitoring).

**Suggested MAXO terms (examples)**
* Immunoglobulin replacement therapy (MAXO term for IVIG/SCIG)
* Anti‑infective therapy / infection prophylaxis
* Nutritional support / enteral feeding
* Coagulation factor replacement / management of coagulopathy
* Physical therapy / occupational therapy / speech therapy for developmental impairment

### 12.3 Clinical trials
No interventional trials specific to ALG12‑CDG were found. A key real‑world research infrastructure is an observational CDG natural history study:
* **NCT04199000** (ClinicalTrials.gov; first posted 2019; recruiting): observational case‑only study with “genetically, enzymatically, or molecularly confirmed diagnosis of CDG or NGLY1 deficiency,” enrollment target 500; includes questionnaires, clinical exams, Nijmegen progression scale and PROMIS measures; allows biospecimen collection for biomarker/DNA studies. ALG12 is listed among keywords. URL: https://clinicaltrials.gov/study/NCT04199000 (NCT04199000 chunk 1, NCT04199000 chunk 2)

---

## 13. Prevention
No primary prevention exists for Mendelian ALG12‑CDG beyond **reproductive and carrier testing strategies**:
* Carrier testing in at‑risk families (based on known familial variants)
* Prenatal diagnosis / preimplantation genetic testing where appropriate

These approaches were not detailed in the retrieved corpus but follow standard practice for autosomal recessive disorders.

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs for ALG12‑CDG were identified in the retrieved evidence.

---

## 15. Model organisms / experimental systems
Direct ALG12‑CDG functional modeling evidence in the retrieved corpus is limited but includes:
* **Yeast complementation/ortholog modeling**: The original report used yeast functional complementation to show that ALG12 patient mutations fail to rescue an alg12 yeast mutant, supporting pathogenicity. (grubenmann2002alg12mannosyltransferasedefect pages 1-2)

No detailed mammalian or zebrafish ALG12‑specific in vivo phenotype data were retrieved in this tool run; therefore, this section should be revisited with dedicated model‑organism database searches (MGI/ZFIN/IMPC) if required.

---

## Recent developments and latest research (prioritizing 2023–2024)
### Diagnostic acceleration and unmet needs
A 2023 Orphanet Journal of Rare Diseases review (patent‑focused) summarizes the state of the field:
* CDG comprises “more than 160” defects. (monticelli2023congenitaldisordersof pages 1-2)
* “CDG diagnosis has been at a rapid pace since the introduction of whole‑exome/whole‑genome sequencing as a diagnostic tool.” (monticelli2023congenitaldisordersof pages 1-2)
* Despite progress, “diagnostic tools, drugs, and biomarkers are still urgently needed.” (monticelli2023congenitaldisordersof pages 1-2)

### Immune phenotype synthesis for ALG12‑CDG
A 2024 Frontiers in Immunology review places ALG12‑CDG into an inborn‑errors‑of‑immunity framing as predominantly antibody deficiency and discusses how glycosylation defects can compromise antibody properties and infection defense. (pascoal2024revisitingtheimmunopathology pages 3-4, pascoal2024revisitingtheimmunopathology pages 4-6)

### Emerging translational methods
A 2024 targeted proteomics paper describes an MRM assay to quantify low‑abundance ER glycosyltransferases in CDG patient fibroblasts and explicitly situates ALG12 among the ER enzymes in the pathway context (“ALG3, ALG9, ALG12…”). This represents a real‑world implementation of quantitative proteomics for CDG mechanism and potentially diagnostics/biomarker development. (Lin et al., 2024‑01; Int J Mol Sci; DOI https://doi.org/10.3390/ijms25021191) (lin2024targetedproteomicsreveals pages 1-2)

---

## Key statistics and data points (from retrieved studies)
* **Reported patient count**: “only 15 patients” diagnosed globally by 2021; Slovak report increased published cases to 16. (ziburova2021anovelhomozygous pages 1-1, ziburova2021anovelhomozygous pages 5-5)
* **Characteristic serum N‑glycan shift**: accumulation of **GlcNAc2Man5–7** with decreased **GlcNAc2Man8–9** (MS evidence). (ziburova2021anovelhomozygous pages 1-1)
* **Patent landscape (CDG, not ALG12‑specific)**: final list of **43 patents** categorized into therapy (25), delivery (2), and diagnostics (17). (monticelli2023congenitaldisordersof pages 1-2)

---

## Evidence organization artifact
The following table summarizes key facts for knowledge‑base ingestion:

| Category | Key findings (concise) | Evidence type | Primary citations (include PMID if available; otherwise DOI/URL) |
|---|---|---|---|
| Disease definition | ALG12-congenital disorder of glycosylation (ALG12-CDG), historically CDG-Ig, is a rare type I CDG caused by deficiency of ALG12 ER α1,6-mannosyltransferase; severe multisystem disease with hypoglycosylation. OMIM/MIM reported in literature as #607143; one excerpt also cites OMIM:607144. | Human case report, review | Grubenmann et al., 2002, Hum Mol Genet, DOI: https://doi.org/10.1093/hmg/11.19.2331; Ziburová et al., 2021, AJMG A, DOI: https://doi.org/10.1002/ajmg.a.62474; Tahata et al., 2019, Mol Genet Metab, DOI: https://doi.org/10.1016/j.ymgme.2019.08.007 (grubenmann2002alg12mannosyltransferasedefect pages 1-2, ziburova2021anovelhomozygous pages 2-2, tahata2019complexphenotypesin pages 1-2) |
| Gene/enzyme function | ALG12 encodes dolichol-P-mannose:Man7GlcNAc2-PP-dolichyl-α-6-mannosyltransferase / α-mannosyltransferase 8, which adds the 8th mannose to the lipid-linked oligosaccharide precursor during N-glycan biosynthesis in the ER. | Human case report, review | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474; Pascoal et al., 2024, Front Immunol, DOI: https://doi.org/10.3389/fimmu.2024.1350101 (grubenmann2002alg12mannosyltransferasedefect pages 1-2, ziburova2021anovelhomozygous pages 2-2, pascoal2024revisitingtheimmunopathology pages 4-6) |
| Inheritance | Autosomal recessive; reported in homozygous and compound heterozygous states. | Human case report/series | Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474; Tahata et al., 2019, DOI: https://doi.org/10.1016/j.ymgme.2019.08.007; Sturiale et al., 2019, DOI: https://doi.org/10.1007/s10719-019-09890-2 (ziburova2021anovelhomozygous pages 2-2, tahata2019complexphenotypesin pages 1-2, sturiale2019alg12cdgnovelglycophenotype pages 6-8) |
| Core phenotypes | Commonly reported: psychomotor/intellectual delay, hypotonia, growth retardation/failure to thrive, microcephaly, dysmorphic facial features, recurrent infections, feeding difficulties, respiratory distress, skeletal abnormalities; variable severity including neonatal/infantile fatal cases and milder presentations. | Human case report/series, review | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Tahata et al., 2019, DOI: https://doi.org/10.1016/j.ymgme.2019.08.007; Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474; de la Morena-Barrio et al., 2020, DOI: https://doi.org/10.1002/mgg3.1304 (grubenmann2002alg12mannosyltransferasedefect pages 1-2, tahata2019complexphenotypesin pages 1-2, ziburova2021anovelhomozygous pages 5-5) |
| Immune involvement | Predominantly antibody deficiency phenotype: hypogammaglobulinemia/low IgG, recurrent severe bacterial or sinopulmonary infections, altered lymphocyte counts/dysfunction. 2024 review groups ALG12-CDG with predominantly antibody deficiencies. | Human case report, review | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Pascoal et al., 2024, DOI: https://doi.org/10.3389/fimmu.2024.1350101; Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474 (grubenmann2002alg12mannosyltransferasedefect pages 2-3, pascoal2024revisitingtheimmunopathology pages 4-6, ziburova2021anovelhomozygous pages 6-7) |
| Coagulation/endocrine | Reported coagulation abnormalities include low antithrombin III, prolonged APTT, decreased coagulation factors; endocrine/metabolic findings include undetectable IGF-1/IGF-BP3, hypoglycemia, low cholesterol, elevated transaminases, and male genital anomalies (micropenis/cryptorchidism). | Human case report/series | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Sturiale et al., 2019, DOI: https://doi.org/10.1007/s10719-019-09890-2; Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474; Tahata et al., 2019, DOI: https://doi.org/10.1016/j.ymgme.2019.08.007 (grubenmann2002alg12mannosyltransferasedefect pages 2-3, sturiale2019alg12cdgnovelglycophenotype pages 6-8, ziburova2021anovelhomozygous pages 5-5, tahata2019complexphenotypesin pages 1-2) |
| Diagnostics (transferrin IEF, LLO, serum N-glycan MS) | Serum transferrin IEF shows a type I CDG pattern with decreased tetrasialotransferrin and increased disialo-/asialotransferrin. Patient fibroblasts can show truncated LLO with accumulation of DolPP-GlcNAc2Man7 and absence/reduction of mature DolPP-GlcNAc2Man9Glc3. Serum N-glycan MS/MALDI-TOF shows accumulation of GlcNAc2Man5-7 with decreased GlcNAc2Man8-9; transferrin/total serum glycomics can reveal mono-glycosylated transferrin and increased high-mannose/hybrid glycans. | Human case report/series | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474; Sturiale et al., 2019, DOI: https://doi.org/10.1007/s10719-019-09890-2 (grubenmann2002alg12mannosyltransferasedefect pages 2-3, ziburova2021anovelhomozygous pages 1-1, sturiale2019alg12cdgnovelglycophenotype pages 6-8) |
| Variant examples | Reported pathogenic/likely pathogenic examples include compound heterozygous p.T67M and p.R146Q; c.1001delA (p.N334Tfs*15) with c.671C>T (p.T224M, reported as VUS in one series); c.367G>A (p.Gly123Arg) and c.1439T>C (p.Leu480Pro); homozygous c.1439T>C (p.Leu480Pro); novel p.Val26Asp. 2025 report (outside requested priority window) adds an intronic splice variant upstream of exon 2. | Human case report/series | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Tahata et al., 2019, DOI: https://doi.org/10.1016/j.ymgme.2019.08.007; Sturiale et al., 2019, DOI: https://doi.org/10.1007/s10719-019-09890-2; Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474 (grubenmann2002alg12mannosyltransferasedefect pages 1-2, tahata2019complexphenotypesin pages 1-2, sturiale2019alg12cdgnovelglycophenotype pages 6-8, ziburova2021anovelhomozygous pages 1-1) |
| Epidemiology/patient counts | Extremely rare. Literature excerpts report “only 15 patients” worldwide by 2021 and “16 published cases” after the Slovak case; no robust prevalence/incidence estimate identified in available context. | Human case report, review | Ziburová et al., 2021, DOI: https://doi.org/10.1002/ajmg.a.62474; Piedade et al., 2022, J Rare Dis, DOI: https://doi.org/10.1007/s44162-022-00003-6 (ziburova2021anovelhomozygous pages 1-1, ziburova2021anovelhomozygous pages 5-5) |
| Management/supportive care | No disease-specific curative therapy identified in available context. Supportive care includes immunoglobulin replacement/IVIG in patients with hypogammaglobulinemia, management of infections, nutritional/supportive multidisciplinary care, and monitoring of coagulation/endocrine issues. Reported response to Ig infusion may be variable or limited in some ALG12-CDG cases. | Human case report, review | Grubenmann et al., 2002, DOI: https://doi.org/10.1093/hmg/11.19.2331; Pascoal et al., 2024, DOI: https://doi.org/10.3389/fimmu.2024.1350101 (grubenmann2002alg12mannosyltransferasedefect pages 2-3, pascoal2024revisitingtheimmunopathology pages 4-6) |
| Research/real-world implementations | Real-world diagnosis increasingly uses WES/WGS for CDG discovery/confirmation; MS-based glycomics (MALDI-MS/UHPLC-ESI-MS) refines subtype-specific glycophenotypes; targeted proteomics/MRM assays for ER glycosyltransferases were introduced in 2024 and include the ALG12 pathway, supporting translational diagnostics/research. Patent review notes CDG diagnosis accelerated with WES/WGS and that diagnostic tools, drugs, and biomarkers remain urgently needed. | Review, translational research | Monticelli et al., 2023, DOI: https://doi.org/10.1186/s13023-023-02852-w; Sturiale et al., 2019, DOI: https://doi.org/10.1007/s10719-019-09890-2; Lin et al., 2024, DOI: https://doi.org/10.3390/ijms25021191 (monticelli2023congenitaldisordersof pages 1-2, sturiale2019alg12cdgnovelglycophenotype pages 1-2, lin2024targetedproteomicsreveals pages 1-2) |
| Clinical trial registry (NCT04199000) | Ongoing observational natural-history study: “Clinical and Basic Investigations Into Congenital Disorders of Glycosylation” (NCT04199000), recruiting, case-only, target enrollment 500, includes genetically/enzymatically/molecularly confirmed CDG or NGLY1 deficiency; outcomes include disease severity/progression measures and biomarker collection. ALG12 is listed among keywords, making the registry relevant to ALG12-CDG. | Trial registry | ClinicalTrials.gov NCT04199000: https://clinicaltrials.gov/study/NCT04199000 (NCT04199000 chunk 1, NCT04199000 chunk 2) |


*Table: This table summarizes key disease facts, clinical and molecular findings, diagnostics, management, and current research implementations for ALG12-CDG using only evidence available in the conversation context. It is designed for rapid knowledge-base ingestion with source-linked citations.*

---

## Limitations of this report (from available tool‑retrieved corpus)
1. **PMIDs** were not available in the retrieved text snippets for several primary papers (DOIs/URLs were available); therefore, PMID‑level citation could not be consistently provided.
2. **Orphanet/ICD/MeSH identifiers** were not present in the retrieved full texts; normalization would require direct database queries.
3. **Quantitative phenotype frequencies** (percentages across cohorts) are largely unavailable because ALG12‑CDG literature is dominated by small case reports/series.
4. **Animal model phenotype data** specific to ALG12 were not retrieved beyond yeast complementation.

---

## Source URLs and publication dates (high‑priority items)
* Grubenmann et al., “ALG12 mannosyltransferase defect in congenital disorder of glycosylation type Ig.” Human Molecular Genetics. **2002‑09**. https://doi.org/10.1093/hmg/11.19.2331 (grubenmann2002alg12mannosyltransferasedefect pages 1-2)
* Ziburová et al., “A novel homozygous mutation in the human ALG12 gene…” American Journal of Medical Genetics A. **2021‑09**. https://doi.org/10.1002/ajmg.a.62474 (ziburova2021anovelhomozygous pages 1-1)
* Monticelli et al., “Congenital disorders of glycosylation: narration of a story through its patents.” Orphanet J Rare Dis. **2023‑08**. https://doi.org/10.1186/s13023-023-02852-w (monticelli2023congenitaldisordersof pages 1-2)
* Pascoal et al., “Revisiting the immunopathology of congenital disorders of glycosylation: an updated review.” Frontiers in Immunology. **2024‑03**. https://doi.org/10.3389/fimmu.2024.1350101 (pascoal2024revisitingtheimmunopathology pages 1-2)
* Lin et al., “Targeted Proteomics Reveals Quantitative Differences…” Int J Mol Sci. **2024‑01**. https://doi.org/10.3390/ijms25021191 (lin2024targetedproteomicsreveals pages 1-2)
* ClinicalTrials.gov natural history study: **NCT04199000**. First posted **2019**; recruiting. https://clinicaltrials.gov/study/NCT04199000 (NCT04199000 chunk 1)


References

1. (grubenmann2002alg12mannosyltransferasedefect pages 1-2): C. Grubenmann, C. Frank, S. Kjaergaard, E. Berger, M. Aebi, and T. Hennet. Alg12 mannosyltransferase defect in congenital disorder of glycosylation type lg. Human molecular genetics, 11 19:2331-9, Sep 2002. URL: https://doi.org/10.1093/hmg/11.19.2331, doi:10.1093/hmg/11.19.2331. This article has 103 citations and is from a domain leading peer-reviewed journal.

2. (grubenmann2002alg12mannosyltransferasedefect pages 2-3): C. Grubenmann, C. Frank, S. Kjaergaard, E. Berger, M. Aebi, and T. Hennet. Alg12 mannosyltransferase defect in congenital disorder of glycosylation type lg. Human molecular genetics, 11 19:2331-9, Sep 2002. URL: https://doi.org/10.1093/hmg/11.19.2331, doi:10.1093/hmg/11.19.2331. This article has 103 citations and is from a domain leading peer-reviewed journal.

3. (ziburova2021anovelhomozygous pages 1-1): Jana Ziburová, Marek Nemčovič, Sergej Šesták, Jana Bellová, Zuzana Pakanová, Barbara Siváková, Anna Šalingová, Claudia Šebová, Mária Ostrožlíková, Dimitra‐Evanthia Lekka, Jana Brucknerová, Ingrid Brucknerová, Martina Skokňová, Alexandra Mc Cullough, Gabriela Hrčková, Anna Hlavatá, Vladimír Bzdúch, Ján Mucha, and Peter Baráth. A novel homozygous mutation in the human alg12 gene results in an aberrant profile of oligomannose n‐glycans in patient's serum. American Journal of Medical Genetics. Part a, 185:3494-3501, Sep 2021. URL: https://doi.org/10.1002/ajmg.a.62474, doi:10.1002/ajmg.a.62474. This article has 17 citations and is from a peer-reviewed journal.

4. (monticelli2023congenitaldisordersof pages 1-2): Maria Monticelli, Tania D’Onofrio, Jaak Jaeken, Eva Morava, Giuseppina Andreotti, and Maria Vittoria Cubellis. Congenital disorders of glycosylation: narration of a story through its patents. Orphanet Journal of Rare Diseases, Aug 2023. URL: https://doi.org/10.1186/s13023-023-02852-w, doi:10.1186/s13023-023-02852-w. This article has 19 citations and is from a peer-reviewed journal.

5. (pascoal2024revisitingtheimmunopathology pages 4-6): Carlota Pascoal, Rita Francisco, Patrícia Mexia, Beatriz Luís Pereira, Pedro Granjo, Helena Coelho, Mariana Barbosa, Vanessa dos Reis Ferreira, and Paula Alexandra Videira. Revisiting the immunopathology of congenital disorders of glycosylation: an updated review. Frontiers in Immunology, Mar 2024. URL: https://doi.org/10.3389/fimmu.2024.1350101, doi:10.3389/fimmu.2024.1350101. This article has 15 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: ALG12-congenital disorder of glycosylation-ALG12): Open Targets Query (ALG12-congenital disorder of glycosylation-ALG12, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (ziburova2021anovelhomozygous pages 2-2): Jana Ziburová, Marek Nemčovič, Sergej Šesták, Jana Bellová, Zuzana Pakanová, Barbara Siváková, Anna Šalingová, Claudia Šebová, Mária Ostrožlíková, Dimitra‐Evanthia Lekka, Jana Brucknerová, Ingrid Brucknerová, Martina Skokňová, Alexandra Mc Cullough, Gabriela Hrčková, Anna Hlavatá, Vladimír Bzdúch, Ján Mucha, and Peter Baráth. A novel homozygous mutation in the human alg12 gene results in an aberrant profile of oligomannose n‐glycans in patient's serum. American Journal of Medical Genetics. Part a, 185:3494-3501, Sep 2021. URL: https://doi.org/10.1002/ajmg.a.62474, doi:10.1002/ajmg.a.62474. This article has 17 citations and is from a peer-reviewed journal.

8. (sturiale2019alg12cdgnovelglycophenotype pages 1-2): Luisa Sturiale, Sebastiano Bianca, Domenico Garozzo, Alessandra Terracciano, Emanuele Agolini, Angela Messina, Angelo Palmigiano, Francesca Esposito, Chiara Barone, Antonio Novelli, Agata Fiumara, Jaak Jaeken, and Rita Barone. Alg12-cdg: novel glycophenotype insights endorse the molecular defect. Glycoconjugate Journal, 36:461-472, Sep 2019. URL: https://doi.org/10.1007/s10719-019-09890-2, doi:10.1007/s10719-019-09890-2. This article has 22 citations and is from a peer-reviewed journal.

9. (tahata2019complexphenotypesin pages 1-2): Shawn Tahata, Lauren B. Gunderson, Brendan Lanpher, and E. Morava. Complex phenotypes in alg12-congenital disorder of glycosylation (alg12-cdg): case series and review of the literature. Molecular genetics and metabolism, 128:409-414, Dec 2019. URL: https://doi.org/10.1016/j.ymgme.2019.08.007, doi:10.1016/j.ymgme.2019.08.007. This article has 25 citations and is from a peer-reviewed journal.

10. (ziburova2021anovelhomozygous pages 7-8): Jana Ziburová, Marek Nemčovič, Sergej Šesták, Jana Bellová, Zuzana Pakanová, Barbara Siváková, Anna Šalingová, Claudia Šebová, Mária Ostrožlíková, Dimitra‐Evanthia Lekka, Jana Brucknerová, Ingrid Brucknerová, Martina Skokňová, Alexandra Mc Cullough, Gabriela Hrčková, Anna Hlavatá, Vladimír Bzdúch, Ján Mucha, and Peter Baráth. A novel homozygous mutation in the human alg12 gene results in an aberrant profile of oligomannose n‐glycans in patient's serum. American Journal of Medical Genetics. Part a, 185:3494-3501, Sep 2021. URL: https://doi.org/10.1002/ajmg.a.62474, doi:10.1002/ajmg.a.62474. This article has 17 citations and is from a peer-reviewed journal.

11. (pascoal2024revisitingtheimmunopathology pages 1-2): Carlota Pascoal, Rita Francisco, Patrícia Mexia, Beatriz Luís Pereira, Pedro Granjo, Helena Coelho, Mariana Barbosa, Vanessa dos Reis Ferreira, and Paula Alexandra Videira. Revisiting the immunopathology of congenital disorders of glycosylation: an updated review. Frontiers in Immunology, Mar 2024. URL: https://doi.org/10.3389/fimmu.2024.1350101, doi:10.3389/fimmu.2024.1350101. This article has 15 citations and is from a peer-reviewed journal.

12. (ziburova2021anovelhomozygous pages 5-5): Jana Ziburová, Marek Nemčovič, Sergej Šesták, Jana Bellová, Zuzana Pakanová, Barbara Siváková, Anna Šalingová, Claudia Šebová, Mária Ostrožlíková, Dimitra‐Evanthia Lekka, Jana Brucknerová, Ingrid Brucknerová, Martina Skokňová, Alexandra Mc Cullough, Gabriela Hrčková, Anna Hlavatá, Vladimír Bzdúch, Ján Mucha, and Peter Baráth. A novel homozygous mutation in the human alg12 gene results in an aberrant profile of oligomannose n‐glycans in patient's serum. American Journal of Medical Genetics. Part a, 185:3494-3501, Sep 2021. URL: https://doi.org/10.1002/ajmg.a.62474, doi:10.1002/ajmg.a.62474. This article has 17 citations and is from a peer-reviewed journal.

13. (sturiale2019alg12cdgnovelglycophenotype pages 6-8): Luisa Sturiale, Sebastiano Bianca, Domenico Garozzo, Alessandra Terracciano, Emanuele Agolini, Angela Messina, Angelo Palmigiano, Francesca Esposito, Chiara Barone, Antonio Novelli, Agata Fiumara, Jaak Jaeken, and Rita Barone. Alg12-cdg: novel glycophenotype insights endorse the molecular defect. Glycoconjugate Journal, 36:461-472, Sep 2019. URL: https://doi.org/10.1007/s10719-019-09890-2, doi:10.1007/s10719-019-09890-2. This article has 22 citations and is from a peer-reviewed journal.

14. (pascoal2024revisitingtheimmunopathology pages 3-4): Carlota Pascoal, Rita Francisco, Patrícia Mexia, Beatriz Luís Pereira, Pedro Granjo, Helena Coelho, Mariana Barbosa, Vanessa dos Reis Ferreira, and Paula Alexandra Videira. Revisiting the immunopathology of congenital disorders of glycosylation: an updated review. Frontiers in Immunology, Mar 2024. URL: https://doi.org/10.3389/fimmu.2024.1350101, doi:10.3389/fimmu.2024.1350101. This article has 15 citations and is from a peer-reviewed journal.

15. (monticelli2023congenitaldisordersof pages 14-15): Maria Monticelli, Tania D’Onofrio, Jaak Jaeken, Eva Morava, Giuseppina Andreotti, and Maria Vittoria Cubellis. Congenital disorders of glycosylation: narration of a story through its patents. Orphanet Journal of Rare Diseases, Aug 2023. URL: https://doi.org/10.1186/s13023-023-02852-w, doi:10.1186/s13023-023-02852-w. This article has 19 citations and is from a peer-reviewed journal.

16. (NCT04199000 chunk 1): Eva Morava-Kozicz. Clinical and Basic Investigations Into Congenital Disorders of Glycosylation. Icahn School of Medicine at Mount Sinai. 2019. ClinicalTrials.gov Identifier: NCT04199000

17. (NCT04199000 chunk 2): Eva Morava-Kozicz. Clinical and Basic Investigations Into Congenital Disorders of Glycosylation. Icahn School of Medicine at Mount Sinai. 2019. ClinicalTrials.gov Identifier: NCT04199000

18. (lin2024targetedproteomicsreveals pages 1-2): Qingsong Lin, Lei Zhou, Chuen Lam, Roman Sakson, Lars Beedgen, Patrick Bernhard, K. M. Alp, Nicole Lübbehusen, R. Röth, Beate Niesler, Marcin Luzarowski, Olga Shevchuk, Matthias P. Mayer, Christian Thiel, and Thomas Ruppert. Targeted proteomics reveals quantitative differences in low-abundance glycosyltransferases of patients with congenital disorders of glycosylation. International Journal of Molecular Sciences, 25:1191, Jan 2024. URL: https://doi.org/10.3390/ijms25021191, doi:10.3390/ijms25021191. This article has 5 citations.

19. (ziburova2021anovelhomozygous pages 6-7): Jana Ziburová, Marek Nemčovič, Sergej Šesták, Jana Bellová, Zuzana Pakanová, Barbara Siváková, Anna Šalingová, Claudia Šebová, Mária Ostrožlíková, Dimitra‐Evanthia Lekka, Jana Brucknerová, Ingrid Brucknerová, Martina Skokňová, Alexandra Mc Cullough, Gabriela Hrčková, Anna Hlavatá, Vladimír Bzdúch, Ján Mucha, and Peter Baráth. A novel homozygous mutation in the human alg12 gene results in an aberrant profile of oligomannose n‐glycans in patient's serum. American Journal of Medical Genetics. Part a, 185:3494-3501, Sep 2021. URL: https://doi.org/10.1002/ajmg.a.62474, doi:10.1002/ajmg.a.62474. This article has 17 citations and is from a peer-reviewed journal.