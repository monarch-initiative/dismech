---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T15:25:36.618972'
end_time: '2026-04-05T15:38:21.554197'
duration_seconds: 764.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glioblastoma, IDH-Wildtype
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 63
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glioblastoma, IDH-Wildtype
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Glioblastoma, IDH-Wildtype** covering all of the
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
- **Disease Name:** Glioblastoma, IDH-Wildtype
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Glioblastoma, IDH-Wildtype** covering all of the
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


# Glioblastoma, IDH‑wildtype — Disease Characteristics Research Report (2026-04-05)

## Target disease
- **Disease name:** Glioblastoma, IDH‑wildtype (adult-type diffuse glioma)
- **MONDO ID:** **MONDO:0018177** (glioblastoma) (antonelli2022adulttypediffuse media 491d0085)
- **Category:** Primary malignant CNS tumor; adult-type diffuse glioma; **CNS WHO grade 4** by definition (gue2024the2021world pages 9-12, antonelli2022adulttypediffuse pages 10-11)

### Executive summary
Glioblastoma, IDH‑wildtype (GBM-IDHwt) is the most common adult grade 4 diffuse astrocytic tumor and is defined in WHO CNS5 (2021) by **IDH-wildtype** status plus either classic grade-4 histology (necrosis and/or microvascular proliferation) or one of three molecular “grade-4” signatures (**TERT promoter mutation**, **EGFR amplification**, **combined whole-chromosome +7/−10**) even when histology appears lower grade. (guo2023histologicalandmolecular pages 1-2, antonelli2022adulttypediffuse pages 10-11, antonelli2022adulttypediffuse media 491d0085)

In recent, large real-world cohorts explicitly restricted to **pathologically verified IDH‑wildtype GBM**, median survival is ~11–12 months with ~21–26% 2-year survival. (bruhn2024dopresentingsymptoms pages 1-2, hainfellner2024glioblastomainthe pages 1-3, dhingra2025limitedsurvivalbenefit pages 1-2)


## 1. Disease information
### 1.1. What is the disease?
**Glioblastoma, IDH‑wildtype** is an infiltrative diffuse astrocytic glioma lacking IDH mutation (and typically lacking histone H3 alterations) with **WHO grade 4 biology**. It is diagnosed either by grade-4 histology (necrosis and/or microvascular proliferation) or by specific molecular features that are sufficient to assign grade 4 in IDH‑wildtype diffuse astrocytic tumors. (antonelli2022adulttypediffuse pages 10-11, antonelli2022adulttypediffuse media 491d0085)

**Direct abstract-level quote supporting definition:** In a real-world WHO CNS5 reclassification study, “IDH-wildtype diffuse astrocytic tumors without the histological features of GBM… are considered as molecular GBM (mol-GBM, WHO grade 4) if they harbor any of the following molecular abnormalities: TERT promoter mutation, EGFR amplification, or chromosomal + 7/−10 copy changes.” (guo2023histologicalandmolecular pages 1-2)

### 1.2. Key identifiers and ontologies
- **MONDO:** glioblastoma **MONDO:0018177** (antonelli2022adulttypediffuse media 491d0085)
- **EFO:** glioblastoma multiforme **EFO:0000519** (Open Targets mapping shown in tool output) (antonelli2022adulttypediffuse media 491d0085)
- **MeSH / ICD-10/ICD-11 / Orphanet / OMIM:** Not reliably retrievable from the currently ingested sources in this run; these should be added from curated terminologies in a subsequent pass.

### 1.3. Common synonyms / alternative names
- Glioblastoma, GBM; glioblastoma multiforme (legacy term)
- “Molecular glioblastoma” / “mol‑GBM” (IDH‑wildtype diffuse astrocytic tumor that meets molecular grade-4 criteria without classic histology) (guo2023histologicalandmolecular pages 1-2, antonelli2022adulttypediffuse pages 10-11)

### 1.4. Evidence sources used in this report
This report primarily uses **aggregated disease-level resources**: WHO CNS5-oriented reviews and guidelines, plus **population/registry real‑world cohorts** (e.g., Swedish Brain Tumor Registry; Austrian national registry; SEER) and selected clinical trial/observational studies. (bruhn2024dopresentingsymptoms pages 1-2, hainfellner2024glioblastomainthe pages 1-3, dhingra2025limitedsurvivalbenefit pages 1-2)


## 2. Etiology
### 2.1. Disease causal factors (mechanistic/genetic)
GBM-IDHwt is driven by recurrent alterations in signaling and cell-cycle networks (RTK/RAS/PI3K; TP53; RB pathways), and is defined diagnostically by a subset of molecular hallmarks (TERT promoter mutation, EGFR amplification, and/or +7/−10). (antonelli2022adulttypediffuse pages 10-11, guo2023histologicalandmolecular pages 1-2)

### 2.2. Genetic risk factors / predisposition
#### Mismatch repair (MMR) deficiency and Lynch-associated glioblastoma subgroups
Recent data highlight a rare but clinically important subset of adult IDH‑wildtype glioblastomas with mismatch-repair deficiency and hypermutation:
- In a prospective genomic profiling series of **459** primary treatment-naïve adult IDH‑wildtype GBMs, a distinct “de novo replication repair deficient” subgroup comprised **2% (9/459)**, defined by somatic hypermutation and **biallelic inactivation of a canonical MMR gene**; deleterious MMR variants were often present in the **germline (heterozygous) with somatic second hit**, consistent with underlying Lynch syndrome. This subgroup had universal **giant cell** histology and lacked canonical EGFR amplification and +7/−10; median OS was **36.8 vs 15.5 months** for other GBMs (p<0.001), and **4/5** patients treated with immune checkpoint blockade survived >3 years. (hadad2024“denovoreplication pages 1-2)
- A separate study (n=218) described a rare germline MMR/Lynch subgroup (G3/MMR) with **very poor median survival (3.25 months post-surgery)** in five germline MMR-variant carriers (MLH1, PMS2, MSH2, MSH6). (georgescu2024adultglioblastomawith pages 1-2)

These studies collectively support a clinically actionable concept: **a minority of GBM-IDHwt arises in the context of hereditary (or constitutional) MMR deficiency**, often with hypermutation, and may have differential prognosis and potential sensitivity to checkpoint blockade. (hadad2024“denovoreplication pages 1-2, georgescu2024adultglioblastomawith pages 1-2)

#### Germline predisposition prevalence estimates (WGS-based)
A WGS-based germline analysis in an unselected cohort of **98 adult WHO grade 4 glioma** patients (93.9% IDH‑wildtype) reported:
- Pathogenic/likely pathogenic germline variants relevant to glioblastoma in **~11%** of patients. (opijnen2025wholegenomesequencingbased pages 1-6)
- Enrichment for **MMR genes** (e.g., MSH6, PMS2, MSH2) and other predisposition genes including **TP53 (Li‑Fraumeni), NF1, BRCA1, SUFU**. (opijnen2025wholegenomesequencingbased pages 1-6)
- MMR deficiency as a major mechanism: **7.1%** carried an MMR-gene PGV with multiple MSI cases. (opijnen2025wholegenomesequencingbased pages 15-18)

#### Li-Fraumeni syndrome (TP53) and adult high-grade gliomas
In three adult Li‑Fraumeni syndrome patients with high-grade gliomas, tumors were IDH1/2-wildtype but **lacked typical GBM-IDHwt hallmarks** (TERT promoter mutation, EGFR amplification, +7/−10). Instead, they showed **PDGFRA amplification** and methylation profiles aligning with pediatric-type high-grade glioma RTK1, suggesting that adult predisposition syndromes can yield tumors that mimic glioblastoma histologically but are molecularly distinct. (kibe2024pediatrictypehighgradegliomas pages 1-2)

### 2.3. Environmental risk factors
Within the ingested evidence for this run, **environmental/occupational risk factors were not supported by extractable primary text**. The report therefore does not assert specific environmental risk magnitudes.

### 2.4. Protective factors and gene–environment interactions
Not established in the retrieved evidence set.


## 3. Phenotypes
### 3.1. Common presenting symptoms (with frequencies when available)
**Swedish Brain Tumor Registry (SBTR), IDH-wildtype only (n=1,458; 2018–2021):** presenting symptom categories included focal neurological deficits, cognitive dysfunction, headache, epilepsy (seizures), signs of raised intracranial pressure, and cranial nerve symptoms. Median survival was 345 days (~11.5 months) and 2-year survival 21.5%. (bruhn2024dopresentingsymptoms pages 1-2)

**Austrian population registry (n=1,420; 2014–2018; IDH-wildtype known in 78.5%):** symptom frequencies at presentation were focal neurological deficits **42.2%**, headache **17.3%**, epilepsy **15.6%**, personality changes **10.9%**. (hainfellner2024glioblastomainthe pages 3-4)

### 3.2. Prognostic impact of key phenotypes
In SBTR, **initial cognitive dysfunction** was associated with substantially shorter survival (median **265 vs 409 days**, P<.001) and remained independently adverse after multivariable adjustment; patients with cognitive deficits were less likely to undergo radical surgery and intensive oncologic therapy. (bruhn2024dopresentingsymptoms pages 1-2)

### 3.3. Phenotype characteristics
- **Typical onset:** predominantly late-adult; in the SBTR IDH-wildtype cohort median age was **66 years** (range 18–89). (bruhn2024dopresentingsymptoms pages 1-2)
- **Course/progression:** rapidly progressive with high recurrence; infiltrative spread limits complete resection. (harwood2024glioblastomacellsincrease pages 1-2)

### 3.4. Suggested HPO mappings (examples)
From registry symptom categories and standard neuro-oncology presentation:
- Seizures: **HP:0001250**
- Headache: **HP:0002315**
- Cognitive impairment: **HP:0100543**
- Focal neurological deficit / hemiparesis: **HP:0001263** (or **HP:0001276** for weakness; mapping may be refined by chart abstraction)
- Signs of increased intracranial pressure (e.g., nausea/vomiting, papilledema): **HP:0002516**, **HP:0002013**

(These HPO mappings are ontology suggestions; the evidence sources provide symptom categories but not term IDs.) (bruhn2024dopresentingsymptoms pages 1-2, hainfellner2024glioblastomainthe pages 3-4)


## 4. Genetic / molecular information
### 4.1. Defining diagnostic molecular features (WHO CNS5)
WHO CNS5 defines glioblastoma, IDH‑wildtype as an IDH-wildtype diffuse astrocytic tumor with either (i) necrosis and/or microvascular proliferation, or (ii) one or more of: **TERT promoter mutation**, **EGFR amplification**, and/or **+7/−10**. (antonelli2022adulttypediffuse pages 10-11, antonelli2022adulttypediffuse media 491d0085)

A visual summary of this WHO diagnostic algorithm is available in **Figure 2** from Antonelli & Poliani (2022). (antonelli2022adulttypediffuse media 491d0085)

### 4.2. Common somatic alterations (representative; not exhaustive)
Across real-world WHO CNS5 reclassification cohorts, recurrent alterations include:
- **EGFR, TERT, CDKN2A/B, PTEN**, and copy-number changes across chromosomes including **7 and 10**. (guo2023histologicalandmolecular pages 1-2)

**Quote (abstract) for a cohort-level molecular summary:** “Common molecular features included copy-number changes in chromosomes 1, 7, 9, 10, and 19, as well as alterations in EGFR, TERT, CDKN2A/B, and PTEN…” (guo2023histologicalandmolecular pages 1-2)

### 4.3. Predictive biomarker: MGMT promoter methylation
MGMT promoter methylation is a key predictive biomarker for temozolomide benefit and is incorporated into molecular-testing guidance for WHO CNS5 gliomas. (sahm2023moleculardiagnostictools pages 14-14, sahm2023moleculardiagnostictools pages 2-3)
- Austrian registry: MGMT promoter methylation present in **34.3%** of patients (unknown 30.2%). (hainfellner2024glioblastomainthe pages 3-4)
- WHO2021 real-world reclassification cohort: MGMT promoter methylation predicted improved survival. (guo2023histologicalandmolecular pages 1-2)

### 4.4. Open Targets disease–gene associations (selected)
Open Targets lists multiple associated targets for “glioblastoma multiforme” including **EGFR, TP53, IDH1, PTEN, ATRX, RB1, NF1, TERT**, among others (mapping evidence includes literature PMIDs). (antonelli2022adulttypediffuse media 491d0085)


## 5. Mechanism / pathophysiology
### 5.1. Tumor cell states and plasticity (single-cell/spatial)
Spatial transcriptomics in patient samples indicates that transcriptional subtype distinctions (classical/proneural/mesenchymal) are strongest in tumor cores but attenuate in infiltrated brain tissue, consistent with **state convergence during invasion**. (harwood2024glioblastomacellsincrease pages 1-2)

A key mechanistic theme is **cell-state plasticity** (e.g., transitions toward a mesenchymal program) and coupling to microenvironmental niches. (hendriksen2024immunotherapydrivesmesenchymal pages 1-3, forster2024tumorpseudolineagesfrom pages 27-30)

### 5.2. Infiltration and recurrence
GBM cells disperse into adjacent parenchyma, often tracking vasculature and white matter, enabling escape from resection; recurrence is frequent and often local. A spatial-transcriptomics study notes recurrence “within resection margins in ~90% of patients within one year.” (harwood2024glioblastomacellsincrease pages 1-2)

### 5.3. Neural/synaptic and developmental programs
A 2024 Nature Medicine study defined a prognostic “neural epigenetic signature” across **n=1,058 glioblastoma** samples; high-neural tumors showed synaptic-gene upregulation and worse outcomes (median OS **14.2 vs 21.2 months**, median PFS **6.2 vs 10.0 months**). (drexler2024aprognosticneural pages 1-2)

### 5.4. Immunosuppressive myeloid microenvironment (2024–2025)
A 2025 Science study used single-cell RNA-seq (33 gliomas) and identified distinct MDSC populations in **IDH-wildtype glioblastoma**, including **early progenitor MDSCs (E‑MDSCs)** and **monocytic MDSCs (M‑MDSCs)**. Spatial transcriptomics localized E‑MDSCs with metabolic stem-like tumor cells in pseudopalisading regions and suggested reciprocal tumor–myeloid cross-talk (tumor chemokines recruit E‑MDSCs; E‑MDSCs provide tumor-supportive growth factors). (jackson2025distinctmyeloidderivedsuppressor pages 1-3)

### 5.5. Suggested ontology mappings
**GO biological processes (examples):**
- cell proliferation; cell migration; angiogenesis; hypoxia response; antigen processing and presentation; immune suppression (conceptual mapping based on described programs). (harwood2024glioblastomacellsincrease pages 1-2, jackson2025distinctmyeloidderivedsuppressor pages 1-3)

**Cell Ontology (CL) terms (examples):**
- tumor-associated macrophage / microglia (as described); myeloid-derived suppressor cell (E‑MDSC / M‑MDSC populations) (jackson2025distinctmyeloidderivedsuppressor pages 1-3)


## 6. Diagnostics
### 6.1. Integrated histomolecular diagnosis (WHO CNS5) and testing workflows
WHO CNS5 requires integrated histology plus molecular assessment for many CNS tumors. For adult diffuse gliomas, when an IDH‑wildtype diffuse glioma lacks necrosis/microvascular proliferation, it should be tested for **EGFR amplification, TERT promoter mutation, and +7/−10** to establish a WHO grade-4 diagnosis. (antonelli2022adulttypediffuse pages 10-11)

### 6.2. Molecular testing (EANO guideline highlights; 2023)
The EANO guideline on molecular diagnostic tools emphasizes that WHO CNS5 requires an integrated “histomolecular” diagnosis, and explicitly includes **MGMT promoter methylation** because of its predictive role in IDH‑wildtype GBM. (sahm2023moleculardiagnostictools pages 2-3)

For MGMT promoter methylation testing, EANO recommends reporting assay details (including CpGs interrogated), the numerical test value, and explicit cutoffs/gray zones; it discourages MGMT immunohistochemistry as the basis for clinical decision-making. (sahm2023moleculardiagnostictools pages 14-14)

### 6.3. MGMT assay-method considerations
Methylation-array platforms can output MGMT promoter information, but the guideline notes that “optimal methods and respective cut-offs… are debated” and that CNV-based inferences should be confirmed by orthogonal methods. (sahm2023moleculardiagnostictools pages 11-12)


## 7. Outcomes / prognosis
### 7.1. Registry-derived survival statistics (recent)
- **Sweden (SBTR), IDH‑wildtype only (2018–2021; n=1,458):** median survival **345 days** and **2-year survival 21.5%**. (bruhn2024dopresentingsymptoms pages 1-2)
- **Austria (ABTR-SANOnet; 2014–2018; n=1,420):** median OS **11.6 months** overall and **10.9 months** in proven IDH‑wildtype. (hainfellner2024glioblastomainthe pages 1-3)
- **SEER era analysis (surgery + postoperative RT; n=27,534):** median OS **15 months** in 2016–2020 vs 14 months in 2005–2015; 24‑month OS ~**25.6%** (2016–2020). (Note: SEER analysis not IDH‑specific and lacks TTFields usage capture.) (dhingra2025limitedsurvivalbenefit pages 1-2)

### 7.2. Prognostic factors supported in retrieved sources
- Baseline cognitive impairment: independently adverse (bruhn2024dopresentingsymptoms pages 1-2)
- MGMT promoter methylation: favorable/predictive (guo2023histologicalandmolecular pages 1-2, sahm2023moleculardiagnostictools pages 14-14)
- Maximal resection and Stupp-protocol treatment: favorable (guo2023histologicalandmolecular pages 1-2)


## 8. Treatment
### 8.1. Standard of care (real-world and consensus summary)
The treatment backbone remains **maximal safe resection** followed by **radiotherapy with concurrent and adjuvant temozolomide** (“Stupp regimen”). (antonelli2022adulttypediffuse pages 10-11, latzer2024arealworldobservation pages 1-2)

**Predictive stratifier:** temozolomide benefit is greater in MGMT promoter–methylated tumors, and likely marginal in MGMT-unmethylated tumors. (antonelli2022adulttypediffuse pages 10-11, sahm2023moleculardiagnostictools pages 14-14)

**Suggested MAXO terms (examples):**
- Maximal surgical resection: **MAXO:0001175** (neurosurgical tumor resection; placeholder mapping)
- Radiotherapy: **MAXO:0000058**
- Alkylating chemotherapy (temozolomide): **MAXO:0000647** (chemotherapy; placeholder mapping)

### 8.2. Tumor Treating Fields (TTFields) — real-world implementation and safety
**Safety (post-marketing; 2011–2022):** in a global PMS dataset of **25,898** TTFields-treated CNS tumor patients (68% newly diagnosed GBM), TTFields-related AEs occurred in **56%**; the most frequent were **beneath-array skin reactions (43%)**, electric sensation/tingling (14%), and warmth (12%). No TTFields-related systemic adverse events were reported. (mrugala2024globalpost‑marketingsafety pages 1-2)

**Real-world effectiveness:** a single-institution cohort (2015–2023; follow-up through 2024) of **208** newly diagnosed GBM patients showed longer survival with TTFields: median **OS 21.7 vs 17.7 months (p=0.029)** and **PFS 12.4 vs 9.6 months (p=0.047)** for TTFields vs no TTFields. (riegel2025longtermsurvivalpatterns pages 1-2)

**Suggested MAXO term:** TTFields (device-based electrical field therapy): **MAXO:0001017** (device therapy; placeholder mapping).

### 8.3. Regorafenib for recurrent glioblastoma (real-world and evolving evidence)
**Prospective observational (REGOMA-OSS; 30 Italian centers; n=190; 92.4% IDH-wildtype):** median **OS 7.9 months**, median **PFS 2.6 months**; grade 3–4 drug-related AEs **22.6%**; dose reductions **36%**; no treatment-related deaths. (caccese2024regomaossalarge pages 1-2)

**Third-line after bevacizumab (Turkey; n=65; IDH-wildtype):** median **PFS 2.5 months**, median **OS 4.1 months**; no drug-related deaths reported. (tunbekici2024regorafenibtreatmentfor pages 1-2)

**Platform trial update (GBM AGILE; NCT03970447):** a reported analysis indicated regorafenib accrual was stopped for futility with mean hazard ratios >1 and low Bayesian probability of benefit across signatures, highlighting uncertainty/heterogeneity in benefit and the need for biomarker-driven selection. (khagi2025recentadvancesin pages 7-8)

**Suggested MAXO term:** multi-kinase inhibitor therapy: **MAXO:0000647** (chemotherapy/targeted therapy; placeholder mapping).

### 8.4. Immunotherapy/vaccines (2023–2024)
**DCVax-L (autologous tumor lysate-loaded dendritic cell vaccine; NCT00045968):** in an externally controlled phase 3 study, median OS for newly diagnosed GBM was **19.3 months vs 16.5 months** in controls (HR 0.80; P=.002), with 60-month survival **13.0% vs 5.7%**; in recurrent GBM, median OS was **13.2 vs 7.8 months** (HR 0.58; P<.001). (liau2023…cellvaccination pages 1-2)

**Personalized neoantigen peptide vaccine (real-world “individual healing attempt”; n=173; 2015–2023):** median OS from first diagnosis **31.9 months** (95% CI 25.0–36.5); immune response detected in **90% (87/97)** monitored patients; multiple vaccine-induced T-cell responses associated with longer survival (**53 vs 27 months**, P=0.03). (latzer2024arealworldobservation pages 1-2)

**Expert analysis note:** Recent literature highlights that glioblastoma immunotherapy outcomes must be interpreted cautiously due to heterogeneous trial designs and immunosuppressive microenvironments, and may require combination strategies targeting myeloid suppression and/or mesenchymal programs. (hendriksen2024immunotherapydrivesmesenchymal pages 1-3, jackson2025distinctmyeloidderivedsuppressor pages 1-3)


## 9. Prevention
- **Primary prevention:** Not established beyond avoidance of unproven risk exposures; the current evidence set does not support actionable population-level prevention recommendations.
- **Secondary prevention / screening:** No population screening recommended; surveillance applies mainly to individuals with known hereditary cancer predisposition (e.g., Lynch/MMR deficiency, Li-Fraumeni), but specific imaging surveillance protocols were not extractable from the ingested evidence. (hadad2024“denovoreplication pages 1-2, kibe2024pediatrictypehighgradegliomas pages 1-2)


## 10. Other species / natural disease
Not addressed in the retrieved evidence set for this run.


## 11. Model organisms / experimental models
Not comprehensively retrieved in this run. However, mechanistic studies cited here relied on spatial transcriptomics in patients (harwood2024glioblastomacellsincrease pages 1-2), scRNA-seq/spatial in human tumors (jackson2025distinctmyeloidderivedsuppressor pages 1-3), and xenograft modeling noted in neural-signature work (drexler2024aprognosticneural pages 1-2).


## Visual evidence
Figure 2 in Antonelli & Poliani (2022) provides a WHO CNS5 diagnostic algorithm showing that GBM-IDHwt can be diagnosed by histologic grade-4 features or by molecular criteria (TERT promoter mutation, EGFR amplification, and/or +7/−10). (antonelli2022adulttypediffuse media 491d0085)


## Synthesis table
| Category | Marker / criterion | What it means in glioblastoma, IDH-wildtype | Representative frequency / note from provided sources |
|---|---|---|---|
| WHO CNS5 histologic criterion | Necrosis and/or microvascular proliferation in an IDH-wildtype diffuse astrocytic glioma | Sufficient for diagnosis of glioblastoma, IDH-wildtype, CNS WHO grade 4 when integrated with molecular exclusion of IDH/H3-altered entities (antonelli2022adulttypediffuse pages 10-11, gue2024the2021world pages 9-12, antonelli2022adulttypediffuse media 491d0085) | WHO CNS5 defines GBM as IDH-wildtype with either these histologic features or specified molecular features (gue2024the2021world pages 9-12, antonelli2022adulttypediffuse pages 10-11, antonelli2022adulttypediffuse media 491d0085) |
| WHO CNS5 molecular criterion | TERT promoter mutation | Can upgrade an otherwise lower-grade appearing IDH-wildtype diffuse astrocytic glioma to molecular glioblastoma; less specific than EGFR amplification or +7/−10 when present alone (guo2023histologicalandmolecular pages 1-2, antonelli2022adulttypediffuse pages 10-11) | 66.3% in one WHO2021-classified GBM cohort; editorial cites ~64–82% in molecular subclasses (guo2023histologicalandmolecular pages 1-2, komori2023updateofthe pages 1-2) |
| WHO CNS5 molecular criterion | EGFR amplification | Diagnostic molecular feature for GBM, IDH-wildtype; also associated with poorer OS in IDH-wildtype diffuse gliomas/GBM (antonelli2022adulttypediffuse pages 10-11, guo2023histologicalandmolecular pages 1-2) | 85.5% in GBM in one real-world study; ~50% cited in review literature; 58.7% in a modern RT/TMZ cohort using FISH/NGS/IHC (antonelli2022adulttypediffuse pages 8-10, hainfellner2024glioblastomainthe pages 1-3) |
| WHO CNS5 molecular criterion | Combined whole chromosome 7 gain / chromosome 10 loss (+7/−10) | Diagnostic molecular signature for GBM, IDH-wildtype; often used to identify molecular GBM when histology is lower grade (gue2024the2021world pages 9-12, guo2023histologicalandmolecular pages 1-2, antonelli2022adulttypediffuse pages 10-11) | Common hallmark of conventional IDH-wildtype GBM; noted as absent in a rare de novo replication-repair-deficient GBM subtype (guo2023histologicalandmolecular pages 1-2, antonelli2022adulttypediffuse pages 8-10) |
| Core genomic alteration | PTEN loss / deletion / mutation | Common tumor-suppressor alteration in PI3K-AKT signaling; generally adverse biology/prognosis, not itself diagnostic under WHO CNS5 (antonelli2022adulttypediffuse pages 10-11) | 60% PTEN alterations in one high-grade glioma sequencing cohort; poor-prognosis association reported in IDH-wildtype GBM (hainfellner2024glioblastomainthe pages 1-3, komori2023updateofthe pages 1-2) |
| Core genomic alteration | CDKN2A/B deletion / homozygous deletion | Frequent cell-cycle alteration in GBM; adverse prognostic factor in GBM though not a WHO CNS5 stand-alone diagnostic criterion for IDH-wildtype GBM (guo2023histologicalandmolecular pages 1-2, antonelli2022adulttypediffuse pages 10-11) | Common alteration in GBM cohorts; in one prognostic study, CDKN2A/B homozygous deletion was statistically significant for worse outcome in GBM (guo2023histologicalandmolecular pages 1-2, komori2023updateofthe pages 1-2) |
| Predictive biomarker | MGMT promoter methylation | Predicts better benefit from temozolomide and is associated with improved survival; important for treatment planning, not diagnostic (antonelli2022adulttypediffuse pages 10-11, sahm2023moleculardiagnostictools pages 2-3) | 34.3% methylated in Austrian registry; 49.1% methylated in one IDH-wildtype GBM RT/TMZ cohort; associated with better survival in real-world WHO2021 GBM cohort (hainfellner2024glioblastomainthe pages 3-4, hainfellner2024glioblastomainthe pages 1-3, guo2023histologicalandmolecular pages 1-2) |
| Diagnostic workflow note | IDH / H3 exclusion before calling GBM, IDH-wildtype | Reviews and algorithms stress confirming IDH-wildtype status and considering H3-altered pediatric-type gliomas, especially in younger patients, before applying molecular GBM criteria (antonelli2022adulttypediffuse pages 10-11, antonelli2022adulttypediffuse media 491d0085) | Practical algorithm: if no necrosis/vascular proliferation, test EGFR amplification, TERT promoter mutation, and +7/−10; also evaluate H3 alterations in relevant clinical settings (antonelli2022adulttypediffuse pages 10-11) |
| Representative clinical-genomic profile | Conventional IDH-wildtype GBM landscape | Recurrent alterations cluster in RTK/RAS/PI3K, TP53, and RB pathways; EGFR, TERT, PTEN, CDKN2A/B are repeatedly reported as common (antonelli2022adulttypediffuse pages 10-11, guo2023histologicalandmolecular pages 1-2) | In WHO2021-classified GBM series: common changes involved chromosomes 1, 7, 9, 10, 19 and EGFR, TERT, CDKN2A/B, PTEN (guo2023histologicalandmolecular pages 1-2) |
| Important caveat | Isolated TERT promoter mutation | Supports WHO CNS5 molecular GBM classification, but multiple sources caution that isolated TERTp mutation in a low-grade-appearing diffuse glioma should be interpreted carefully because of limited specificity (antonelli2022adulttypediffuse pages 10-11) | Review explicitly states TERT promoter mutation is the least specific of the three WHO molecular criteria (antonelli2022adulttypediffuse pages 10-11) |


*Table: This table summarizes WHO CNS5 diagnostic rules and major biomarkers for glioblastoma, IDH-wildtype, including their diagnostic, prognostic, or predictive roles. It also gives representative frequencies and practical notes from the cited real-world and review sources.*


## References (URLs and publication dates)
- Antonelli & Poliani. *Pathologica* (2022-12). doi:10.32074/1591-951x-823. https://doi.org/10.32074/1591-951x-823 (antonelli2022adulttypediffuse pages 10-11)
- Sahm et al. EANO guideline. *Neuro-Oncology* (2023-06). doi:10.1093/neuonc/noad100. https://doi.org/10.1093/neuonc/noad100 (sahm2023moleculardiagnostictools pages 14-14)
- Guo et al. WHO2021 real-world reclassification cohort. *Frontiers in Oncology* (2023-07-06). doi:10.3389/fonc.2023.1200815. https://doi.org/10.3389/fonc.2023.1200815 (guo2023histologicalandmolecular pages 1-2)
- Bruhn et al. Swedish Brain Tumor Registry (IDH-wildtype GBM). *Neuro-Oncology Practice* (2024-04). doi:10.1093/nop/npae036. https://doi.org/10.1093/nop/npae036 (bruhn2024dopresentingsymptoms pages 1-2)
- Hainfellner et al. Austrian population registry. *Journal of Neuro-Oncology* (2024-08). doi:10.1007/s11060-024-04808-x. https://doi.org/10.1007/s11060-024-04808-x (hainfellner2024glioblastomainthe pages 1-3)
- Mrugala et al. TTFields PMS safety. *Journal of Neuro-Oncology* (2024-06). doi:10.1007/s11060-024-04682-7. https://doi.org/10.1007/s11060-024-04682-7 (mrugala2024globalpost‑marketingsafety pages 1-2)
- Caccese et al. REGOMA-OSS regorafenib. *ESMO Open* (2024-04). doi:10.1016/j.esmoop.2024.102943. https://doi.org/10.1016/j.esmoop.2024.102943 (caccese2024regomaossalarge pages 1-2)
- Tünbekici et al. regorafenib after bevacizumab (real-world). *Cancers* (2024-12). doi:10.3390/cancers17010046. https://doi.org/10.3390/cancers17010046 (tunbekici2024regorafenibtreatmentfor pages 1-2)
- Harwood et al. Infiltrated brain tissue programs. *Nature Communications* (2024-09). doi:10.1038/s41467-024-52167-y. https://doi.org/10.1038/s41467-024-52167-y (harwood2024glioblastomacellsincrease pages 1-2)
- Drexler et al. Neural epigenetic signature. *Nature Medicine* (2024-05). doi:10.1038/s41591-024-02969-w. https://doi.org/10.1038/s41591-024-02969-w (drexler2024aprognosticneural pages 1-2)
- Hendriksen et al. Immunotherapy-associated MES shift. *Neuro-Oncology* (2024-05). doi:10.1093/neuonc/noae085. https://doi.org/10.1093/neuonc/noae085 (hendriksen2024immunotherapydrivesmesenchymal pages 1-3)
- Jackson et al. MDSC populations. *Science* (2025-01). doi:10.1126/science.abm5214. https://doi.org/10.1126/science.abm5214 (jackson2025distinctmyeloidderivedsuppressor pages 1-3)
- Riegel et al. TTFields real-world survival. *Journal of Neuro-Oncology* (2025-03). doi:10.1007/s11060-025-04946-w. https://doi.org/10.1007/s11060-025-04946-w (riegel2025longtermsurvivalpatterns pages 1-2)
- Hadad et al. De novo replication repair–deficient GBM subgroup. *Acta Neuropathologica* (2024-12). doi:10.1007/s00401-023-02654-1. https://doi.org/10.1007/s00401-023-02654-1 (hadad2024“denovoreplication pages 1-2)
- Liau et al. DCVax-L phase 3 externally controlled cohort trial (as retrieved). NCT00045968. (liau2023…cellvaccination pages 1-2)
- Latzer et al. Personalized peptide vaccine (real-world). *Nature Communications* (2024-08). doi:10.1038/s41467-024-51315-8. https://doi.org/10.1038/s41467-024-51315-8 (latzer2024arealworldobservation pages 1-2)



References

1. (antonelli2022adulttypediffuse media 491d0085): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.

2. (gue2024the2021world pages 9-12): Racine Gue and Dhairya A. Lakhani. The 2021 world health organization central nervous system tumor classification: the spectrum of diffuse gliomas. Biomedicines, 12:1349, Jun 2024. URL: https://doi.org/10.3390/biomedicines12061349, doi:10.3390/biomedicines12061349. This article has 13 citations.

3. (antonelli2022adulttypediffuse pages 10-11): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.

4. (guo2023histologicalandmolecular pages 1-2): Xiaopeng Guo, Lingui Gu, Yilin Li, Zhiyao Zheng, Wenlin Chen, Yaning Wang, Yuekun Wang, Hao Xing, Yixin Shi, Delin Liu, Tianrui Yang, Yu Xia, Junlin Li, Jiaming Wu, Kun Zhang, Tingyu Liang, Hai Wang, Qianshu Liu, Shanmu Jin, Tian Qu, Siying Guo, Huanzhang Li, Yu Wang, and Wenbin Ma. Histological and molecular glioblastoma, idh-wildtype: a real-world landscape using the 2021 who classification of central nervous system tumors. Frontiers in Oncology, Jul 2023. URL: https://doi.org/10.3389/fonc.2023.1200815, doi:10.3389/fonc.2023.1200815. This article has 98 citations.

5. (bruhn2024dopresentingsymptoms pages 1-2): Helena Bruhn, Björn Tavelin, Lena Rosenlund, and Roger Henriksson. Do presenting symptoms predict treatment decisions and survival in glioblastoma? real-world data from 1458 patients in the swedish brain tumor registry. Neuro-Oncology Practice, 11:652-659, Apr 2024. URL: https://doi.org/10.1093/nop/npae036, doi:10.1093/nop/npae036. This article has 9 citations and is from a peer-reviewed journal.

6. (hainfellner2024glioblastomainthe pages 1-3): Andreas Hainfellner, Martin Borkovec, Lukas Seebrecht, Magdalena Neuhauser, Thomas Roetzer-Pejrimovsky, Lisa Greutter, Birgit Surböck, Andrea Hager-Seifert, Doris Gorka-vom Hof, Tadeja Urbanic-Purkart, Martin Stultschnig, Clemens Cijan, Franz Würtz, Bernadette Calabek-Wohinz, Josef Pichler, Isolde Höllmüller, Annette Leibetseder, Serge Weis, Waltraud Kleindienst, Michael Seiberl, Lara Bieler, Constantin Hecker, Christoph Schwartz, Sarah Iglseder, Johanna Heugenhauser, Martha Nowosielski, Claudius Thomé, Patrizia Moser, Markus Hoffermann, Karin Loibnegger, Karin Dieckmann, Matthias Tomschik, Georg Widhalm, Karl Rössler, Christine Marosi, Adelheid Wöhrer, Johannes A. Hainfellner, and Stefan Oberndorfer. Glioblastoma in the real-world setting: patterns of care and outcome in the austrian population. Journal of Neuro-Oncology, 170:407-418, Aug 2024. URL: https://doi.org/10.1007/s11060-024-04808-x, doi:10.1007/s11060-024-04808-x. This article has 6 citations and is from a peer-reviewed journal.

7. (dhingra2025limitedsurvivalbenefit pages 1-2): Shaurya Dhingra, Matthew Koshy, and Mark Korpics. Limited survival benefit in patients diagnosed with glioblastoma post-2016: a seer population based registry analysis. Journal of Cancer Research and Clinical Oncology, Jun 2025. URL: https://doi.org/10.1007/s00432-025-06171-4, doi:10.1007/s00432-025-06171-4. This article has 7 citations and is from a peer-reviewed journal.

8. (hadad2024“denovoreplication pages 1-2): Sara Hadad, Rohit Gupta, Nancy Ann Oberheim Bush, Jennie W. Taylor, Javier E. Villanueva-Meyer, Jacob S. Young, Jasper Wu, Ajay Ravindranathan, Yalan Zhang, Gayathri Warrier, Lucie McCoy, Anny Shai, Melike Pekmezci, Arie Perry, Andrew W. Bollen, Joanna J. Phillips, Steve E. Braunstein, David R. Raleigh, Philip Theodosopoulos, Manish K. Aghi, Edward F. Chang, Shawn L. Hervey-Jumper, Joseph F. Costello, John de Groot, Nicholas A. Butowski, Jennifer L. Clarke, Susan M. Chang, Mitchel S. Berger, Annette M. Molinaro, and David A. Solomon. “de novo replication repair deficient glioblastoma, idh-wildtype” is a distinct glioblastoma subtype in adults that may benefit from immune checkpoint blockade. Acta Neuropathologica, Dec 2024. URL: https://doi.org/10.1007/s00401-023-02654-1, doi:10.1007/s00401-023-02654-1. This article has 38 citations and is from a highest quality peer-reviewed journal.

9. (georgescu2024adultglioblastomawith pages 1-2): Maria-Magdalena Georgescu. Adult glioblastoma with lynch syndrome-associated mismatch repair deficiency forms a distinct high-risk molecular subgroup. Free Neuropathology, Dec 2024. URL: https://doi.org/10.17879/freeneuropathology-2024-5892, doi:10.17879/freeneuropathology-2024-5892. This article has 5 citations and is from a peer-reviewed journal.

10. (opijnen2025wholegenomesequencingbased pages 1-6): Mark P. van Opijnen, Devin R. van Valkengoed, Joep de Ligt, Filip Y.F. de Vos, Marike L.D. Broekman, Edwin Cuppen, and Roelof Koster. Whole genome sequencing-based analysis of genetic predisposition to adult glioblastoma. MedRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.16.25320661, doi:10.1101/2025.01.16.25320661. This article has 1 citations.

11. (opijnen2025wholegenomesequencingbased pages 15-18): Mark P. van Opijnen, Devin R. van Valkengoed, Joep de Ligt, Filip Y.F. de Vos, Marike L.D. Broekman, Edwin Cuppen, and Roelof Koster. Whole genome sequencing-based analysis of genetic predisposition to adult glioblastoma. MedRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.16.25320661, doi:10.1101/2025.01.16.25320661. This article has 1 citations.

12. (kibe2024pediatrictypehighgradegliomas pages 1-2): Yuji Kibe, Fumiharu Ohka, Kosuke Aoki, Junya Yamaguchi, Kazuya Motomura, Eiji Ito, Kazuhito Takeuchi, Yuichi Nagata, Satoshi Ito, Nobuhiko Mizutani, Yoshiki Shiba, Sachi Maeda, Tomohide Nishikawa, Hiroki Shimizu, and Ryuta Saito. Pediatric-type high-grade gliomas with pdgfra amplification in adult patients with li-fraumeni syndrome: clinical and molecular characterization of three cases. Acta Neuropathologica Communications, Apr 2024. URL: https://doi.org/10.1186/s40478-024-01762-7, doi:10.1186/s40478-024-01762-7. This article has 9 citations and is from a peer-reviewed journal.

13. (hainfellner2024glioblastomainthe pages 3-4): Andreas Hainfellner, Martin Borkovec, Lukas Seebrecht, Magdalena Neuhauser, Thomas Roetzer-Pejrimovsky, Lisa Greutter, Birgit Surböck, Andrea Hager-Seifert, Doris Gorka-vom Hof, Tadeja Urbanic-Purkart, Martin Stultschnig, Clemens Cijan, Franz Würtz, Bernadette Calabek-Wohinz, Josef Pichler, Isolde Höllmüller, Annette Leibetseder, Serge Weis, Waltraud Kleindienst, Michael Seiberl, Lara Bieler, Constantin Hecker, Christoph Schwartz, Sarah Iglseder, Johanna Heugenhauser, Martha Nowosielski, Claudius Thomé, Patrizia Moser, Markus Hoffermann, Karin Loibnegger, Karin Dieckmann, Matthias Tomschik, Georg Widhalm, Karl Rössler, Christine Marosi, Adelheid Wöhrer, Johannes A. Hainfellner, and Stefan Oberndorfer. Glioblastoma in the real-world setting: patterns of care and outcome in the austrian population. Journal of Neuro-Oncology, 170:407-418, Aug 2024. URL: https://doi.org/10.1007/s11060-024-04808-x, doi:10.1007/s11060-024-04808-x. This article has 6 citations and is from a peer-reviewed journal.

14. (harwood2024glioblastomacellsincrease pages 1-2): D. Harwood, V. Pedersen, N. Bager, A. Schmidt, T. Stannius, A. Areškevičiūtė, Knud Josefsen, D. Nørøxe, David Scheie, Hannah Rostalski, M. Lü, A. Locallo, U. Lassen, F. Bagger, J. Weischenfeldt, D. Heiland, Kristoffer Vitting-Seerup, S. Michaelsen, and BW Kristensen. Glioblastoma cells increase expression of notch signaling and synaptic genes within infiltrated brain tissue. Nature communications, 15 1:7857, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52167-y, doi:10.1038/s41467-024-52167-y. This article has 47 citations and is from a highest quality peer-reviewed journal.

15. (sahm2023moleculardiagnostictools pages 14-14): Felix Sahm, Sebastian Brandner, Luca Bertero, David Capper, Pim J French, Dominique Figarella-Branger, Felice Giangaspero, Christine Haberler, Monika E Hegi, Bjarne W Kristensen, Kathreena M Kurian, Matthias Preusser, Bastiaan B J Tops, Martin van den Bent, Wolfgang Wick, Guido Reifenberger, and Pieter Wesseling. Molecular diagnostic tools for the world health organization (who) 2021 classification of gliomas, glioneuronal and neuronal tumors; an eano guideline. Neuro-Oncology, 25:1731-1749, Jun 2023. URL: https://doi.org/10.1093/neuonc/noad100, doi:10.1093/neuonc/noad100. This article has 110 citations and is from a domain leading peer-reviewed journal.

16. (sahm2023moleculardiagnostictools pages 2-3): Felix Sahm, Sebastian Brandner, Luca Bertero, David Capper, Pim J French, Dominique Figarella-Branger, Felice Giangaspero, Christine Haberler, Monika E Hegi, Bjarne W Kristensen, Kathreena M Kurian, Matthias Preusser, Bastiaan B J Tops, Martin van den Bent, Wolfgang Wick, Guido Reifenberger, and Pieter Wesseling. Molecular diagnostic tools for the world health organization (who) 2021 classification of gliomas, glioneuronal and neuronal tumors; an eano guideline. Neuro-Oncology, 25:1731-1749, Jun 2023. URL: https://doi.org/10.1093/neuonc/noad100, doi:10.1093/neuonc/noad100. This article has 110 citations and is from a domain leading peer-reviewed journal.

17. (hendriksen2024immunotherapydrivesmesenchymal pages 1-3): Josephine D Hendriksen, Alessio Locallo, Simone Maarup, Olivia Debnath, Naveed Ishaque, Benedikte Hasselbach, Jane Skjøth-Rasmussen, Christina Westmose Yde, Hans S Poulsen, Ulrik Lassen, and Joachim Weischenfeldt. Immunotherapy drives mesenchymal tumour cell state shift and tme immune response in glioblastoma patients. Neuro-oncology, 26:1453-1466, May 2024. URL: https://doi.org/10.1093/neuonc/noae085, doi:10.1093/neuonc/noae085. This article has 17 citations and is from a domain leading peer-reviewed journal.

18. (forster2024tumorpseudolineagesfrom pages 27-30): Leo Carl Förster. Tumor pseudolineages from a healthy lineage template reveal organizational principles and cell-fate modulators in glioblastoma. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00035474, doi:10.11588/heidok.00035474. This article has 0 citations and is from a peer-reviewed journal.

19. (drexler2024aprognosticneural pages 1-2): Richard Drexler, Robin Khatri, Thomas Sauvigny, Malte Mohme, Cecile L. Maire, Alice Ryba, Yahya Zghaibeh, Lasse Dührsen, Amanda Salviano-Silva, Katrin Lamszus, Manfred Westphal, Jens Gempt, Annika K. Wefers, Julia E. Neumann, Helena Bode, Fabian Hausmann, Tobias B. Huber, Stefan Bonn, Kerstin Jütten, Daniel Delev, Katharina J. Weber, Patrick N. Harter, Julia Onken, Peter Vajkoczy, David Capper, Benedikt Wiestler, Michael Weller, Berend Snijder, Alicia Buck, Tobias Weiss, Pauline C. Göller, Felix Sahm, Joelle Aline Menstel, David Niklas Zimmer, Michael B. Keough, Lijun Ni, Michelle Monje, Dana Silverbush, Volker Hovestadt, Mario L. Suvà, Saritha Krishna, Shawn L. Hervey-Jumper, Ulrich Schüller, Dieter H. Heiland, Sonja Hänzelmann, and Franz L. Ricklefs. A prognostic neural epigenetic signature in high-grade glioma. Nature Medicine, 30:1622-1635, May 2024. URL: https://doi.org/10.1038/s41591-024-02969-w, doi:10.1038/s41591-024-02969-w. This article has 110 citations and is from a highest quality peer-reviewed journal.

20. (jackson2025distinctmyeloidderivedsuppressor pages 1-3): Christina Jackson, Christopher Cherry, Sadhana Bom, Arbor G. Dykema, Rulin Wang, Elizabeth Thompson, Ming Zhang, Runzhe Li, Zhicheng Ji, Wenpin Hou, Wentao Zhan, Hao Zhang, John Choi, Ajay Vaghasia, Landon Hansen, William Wang, Brandon Bergsneider, Kate M. Jones, Fausto Rodriguez, Jon Weingart, Calixto-Hope Lucas, Jonathan Powell, Jennifer Elisseeff, Srinivasan Yegnasubramanian, Michael Lim, Chetan Bettegowda, Hongkai Ji, and Drew Pardoll. Distinct myeloid-derived suppressor cell populations in human glioblastoma. Science, 387 6731:eabm5214, Jan 2025. URL: https://doi.org/10.1126/science.abm5214, doi:10.1126/science.abm5214. This article has 78 citations and is from a highest quality peer-reviewed journal.

21. (sahm2023moleculardiagnostictools pages 11-12): Felix Sahm, Sebastian Brandner, Luca Bertero, David Capper, Pim J French, Dominique Figarella-Branger, Felice Giangaspero, Christine Haberler, Monika E Hegi, Bjarne W Kristensen, Kathreena M Kurian, Matthias Preusser, Bastiaan B J Tops, Martin van den Bent, Wolfgang Wick, Guido Reifenberger, and Pieter Wesseling. Molecular diagnostic tools for the world health organization (who) 2021 classification of gliomas, glioneuronal and neuronal tumors; an eano guideline. Neuro-Oncology, 25:1731-1749, Jun 2023. URL: https://doi.org/10.1093/neuonc/noad100, doi:10.1093/neuonc/noad100. This article has 110 citations and is from a domain leading peer-reviewed journal.

22. (latzer2024arealworldobservation pages 1-2): Pauline Latzer, Henning Zelba, Florian Battke, Annekathrin Reinhardt, Borong Shao, Oliver Bartsch, Armin Rabsteyn, Johannes Harter, Martin Schulze, Thomas Okech, Alexander Golf, Christina Kyzirakos-Feger, Simone Kayser, Natalia Pieper, Magdalena Feldhahn, Julian Wünsche, Christian Seitz, Dirk Hadaschik, Claus Garbe, Till-Karsten Hauser, Christian la Fougère, Dirk Biskup, Dawn Brooke, David Parker, Uwe M. Martens, Gerald Illerhaus, Deborah T. Blumenthal, Ryan Merrell, Luisa Sánchez Lorenzo, Máté Hidvégi, Paula de Robles, Sied Kebir, William W. Li, Vincent W. Li, Matthew Williams, Alexandra M. Miller, Santosh Kesari, Michael Castro, Annick Desjardins, David M. Ashley, Henry S. Friedman, Patrick Y. Wen, Elisabeth C. Neil, Fabio M. Iwamoto, Bence Sipos, Karsten Geletneky, Lars Zender, Martin Glas, David A. Reardon, and Saskia Biskup. A real-world observation of patients with glioblastoma treated with a personalized peptide vaccine. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51315-8, doi:10.1038/s41467-024-51315-8. This article has 52 citations and is from a highest quality peer-reviewed journal.

23. (mrugala2024globalpost‑marketingsafety pages 1-2): Maciej M. Mrugala, Wenyin Shi, Fabio Iwomoto, Rimas V. Lukas, Joshua D. Palmer, John H. Suh, and Martin Glas. Global post‑marketing safety surveillance of tumor treating fields (ttfields) therapy in over 25,000 patients with cns malignancies treated between 2011–2022. Journal of Neuro-Oncology, 169:25-38, Jun 2024. URL: https://doi.org/10.1007/s11060-024-04682-7, doi:10.1007/s11060-024-04682-7. This article has 19 citations and is from a peer-reviewed journal.

24. (riegel2025longtermsurvivalpatterns pages 1-2): Devon C. Riegel, Britta L. Bureau, Patrick Conlon, Gordon Chavez, and Jennifer M. Connelly. Long-term survival, patterns of progression, and patterns of use for patients with newly diagnosed glioblastoma treated with or without tumor treating fields (ttfields) in a real-world setting. Journal of Neuro-Oncology, 173:49-57, Mar 2025. URL: https://doi.org/10.1007/s11060-025-04946-w, doi:10.1007/s11060-025-04946-w. This article has 11 citations and is from a peer-reviewed journal.

25. (caccese2024regomaossalarge pages 1-2): M. Caccese, I. Desideri, V. Villani, M. Simonelli, M. Buglione, S. Chiesa, E. Franceschi, P. Gaviani, I. Stasi, C. Caserta, S. Brugnara, I. Lolli, E. Bennicelli, P. Bini, A.S. Cuccu, S. Scoccianti, M. Padovan, S. Gori, A. Bonetti, P. Giordano, A. Pellerino, F. Gregucci, N. Riva, S. Cinieri, V. Internò, M. Santoni, G. Pernice, C. Dealis, L. Stievano, F. Paiar, G. Magni, G.L. De Salvo, V. Zagonel, and G. Lombardi. Regoma-oss: a large, italian, multicenter, prospective, observational study evaluating the efficacy and safety of regorafenib in patients with recurrent glioblastoma. ESMO Open, 9:102943, Apr 2024. URL: https://doi.org/10.1016/j.esmoop.2024.102943, doi:10.1016/j.esmoop.2024.102943. This article has 16 citations and is from a domain leading peer-reviewed journal.

26. (tunbekici2024regorafenibtreatmentfor pages 1-2): Salih Tünbekici, Haydar cagatay Yuksel, Caner Acar, Gökhan Sahin, Seval Orman, Nargiz Majidova, Alper Coskun, Mustafa Seyyar, Mehmet sıddık Dilek, Mahmut Kara, Ahmet Kursat Dıslı, Teyfik Demir, Nagihan Kolkıran, Mustafa Sahbazlar, Erkut Demırcıler, Fatih Kuş, Ali Aytac, Serkan Menekse, Hakan Yucel, Sedat Biter, Tolga Koseci, Ahmet Unsal, Ahmet Ozveren, Alper Sevınc, Erdem Goker, and Pınar Gürsoy. Regorafenib treatment for recurrent glioblastoma beyond bevacizumab-based therapy: a large, multicenter, real-life study. Cancers, 17:46, Dec 2024. URL: https://doi.org/10.3390/cancers17010046, doi:10.3390/cancers17010046. This article has 2 citations.

27. (khagi2025recentadvancesin pages 7-8): Simon Khagi, Rupesh Kotecha, Na Tosha N Gatson, Suriya Jeyapalan, Huda Ismail Abdullah, Nicholas G Avgeropoulos, Eleni T Batzianouli, Moshe Giladi, Leonardo Lustgarten, and Samuel A Goldlust. Recent advances in tumor treating fields (ttfields) therapy for glioblastoma. The Oncologist, Oct 2025. URL: https://doi.org/10.1093/oncolo/oyae227, doi:10.1093/oncolo/oyae227. This article has 43 citations.

28. (liau2023…cellvaccination pages 1-2): LM Liau, K Ashkan, S Brem, and JL Campian. … cell vaccination with extension of survival among patients with newly diagnosed and recurrent glioblastoma: a phase 3 prospective externally controlled cohort trial. Unknown journal, 2023.

29. (komori2023updateofthe pages 1-2): Takashi Komori. Update of the 2021 who classification of tumors of the central nervous system: adult diffuse gliomas. Brain Tumor Pathology, 40:1-3, Dec 2023. URL: https://doi.org/10.1007/s10014-022-00446-1, doi:10.1007/s10014-022-00446-1. This article has 12 citations and is from a peer-reviewed journal.

30. (antonelli2022adulttypediffuse pages 8-10): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 67 citations.
