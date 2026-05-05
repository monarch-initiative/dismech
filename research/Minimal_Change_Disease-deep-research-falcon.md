---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-14T19:41:48.959491'
end_time: '2026-04-14T19:51:11.903743'
duration_seconds: 562.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Minimal Change Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Minimal Change Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Minimal Change Disease** covering all of the
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
- **Disease Name:** Minimal Change Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Minimal Change Disease** covering all of the
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


# Minimal Change Disease (MCD) — Disease Characteristics Research Report (2023–2024 prioritized)

## 1. Disease Information

### Overview (current understanding)
Minimal change disease (MCD) is a glomerular disorder/podocytopathy that classically presents with acute nephrotic syndrome (heavy proteinuria with edema) and shows minimal or absent changes on light microscopy, but diffuse podocyte foot-process effacement on electron microscopy. (gauckler2023diagnostikundtherapie pages 1-2, son2023outcomesofminimal pages 1-2)

### Synonyms and alternative names (as used in retrieved sources)
- Minimal change disease (MCD) (son2023outcomesofminimal pages 1-2)
- Minimal change glomerulopathy / “Minimal Change Glomerulopathie” (adult consensus terminology) (gauckler2023diagnostikundtherapie pages 1-2)
- Minimal change nephrotic syndrome (MCNS) (willcocks2024arandomisedtwoarm pages 1-2)

### Key identifiers
The following standard identifiers were **not retrievable from the provided tool context in this run** and therefore are **not reported**: MONDO ID, MeSH ID, Orphanet ID, OMIM entry, ICD-10/ICD-11 code.

### Evidence source type
The report is derived from **aggregated disease-level resources** (consensus statements/guidelines, trial protocols, registry studies) and **primary clinical/translational studies** (cohorts, mechanistic antibody study). (gauckler2023diagnostikundtherapie pages 1-2, hengel2024autoantibodiestargetingnephrin pages 1-3, nakagawa2023demographicsandtreatment pages 1-2)

## 2. Etiology

### Disease causal factors (primary vs secondary)
MCD is widely treated as an immune-mediated podocytopathy based on its typical responsiveness to immunosuppression (particularly glucocorticoids) and emerging autoantibody evidence. (gauckler2023diagnostikundtherapie pages 1-2, hengel2024autoantibodiestargetingnephrin pages 1-3)

A key recent etiologic advance is the identification of **circulating anti-nephrin autoantibodies** in a substantial subset of patients with MCD, supporting an autoimmune subset in which antibodies bind a podocyte slit diaphragm protein (nephrin) and are associated with disease activity. (hengel2024autoantibodiestargetingnephrin pages 1-3)

Secondary/trigger-associated MCD is recognized clinically; adult consensus emphasizes that secondary causes should be actively evaluated in adults. Specific secondary causes were **not enumerated in the retrieved excerpts**, so they are not itemized here. (gauckler2023diagnostikundtherapie pages 1-2)

### Risk factors
- **Relapse-prone disease course:** relapse is common as steroids are tapered/withdrawn, which acts as an important clinical risk context for cumulative immunosuppression-related harm. (mirioglu2024managementofadult pages 3-5, willcocks2024arandomisedtwoarm pages 1-2)
- **Registry-defined steroid dependence / frequent relapse:** in a large Japanese registry of primary nephrotic syndrome, 70.2% of MCD patients were classified as steroid-dependent or frequently relapsing, and 6.4% as steroid-resistant. (nakagawa2023demographicsandtreatment pages 2-4)

Genetic susceptibility loci and gene–environment interaction evidence were **not retrievable from the provided excerpts** and are not reported.

### Protective factors
Protective genetic or environmental factors were **not retrievable from the provided excerpts**.

## 3. Phenotypes

### Core phenotypes (clinical and laboratory)
- **Nephrotic syndrome presentation:** MCD is characterized by edema and nephrotic-range proteinuria in typical presentations. (son2023outcomesofminimal pages 1-2)
- **Adult biopsy cohort features:** in a cohort of 79 adults with biopsy-proven primary MCD, outcomes were evaluated in patients with and without nephrotic-range proteinuria at biopsy; acute kidney injury occurred more often in those with nephrotic-range proteinuria (59.3% vs 5.0%). (son2023outcomesofminimal pages 1-2)

### Phenotype ontology suggestions (HPO)
Formal HPO mappings were **not directly provided in the retrieved excerpts**. Suggested candidate terms based on described phenotypes (requires independent HPO verification before knowledge-base ingestion):
- Nephrotic syndrome; Proteinuria; Edema; Hypoalbuminemia; Acute kidney injury.

### Quality of life impact
Nephrotic syndrome was described as having “debilitating oedema” in an adult trial protocol, consistent with substantial symptom burden and functional limitation. (willcocks2024arandomisedtwoarm pages 1-2)

## 4. Genetic/Molecular Information

### Causal genes and pathogenic variants
Monogenic causes/variants, modifier genes, and allele frequencies were **not retrievable from the provided excerpts**.

### Key molecular findings and biomarkers
**Anti-nephrin autoantibodies (major 2024 development):**
- In a multicenter NEJM study (Aug 2024), anti-nephrin autoantibodies were detected in **44% (46/105) of adults with MCD** and **52% (94/182) of children** with idiopathic nephrotic syndrome; positivity reached **69%** in untreated active adult MCD and **90%** in untreated active children. (hengel2024autoantibodiestargetingnephrin pages 1-3)
- Antibody levels correlated with disease activity and decreased with remission, supporting their use as activity biomarkers (not yet established as routine clinical tests). (hengel2024autoantibodiestargetingnephrin pages 1-3)

**IL-33/ST2 axis:**
A 2023 translational study examined 49 biopsy-proven MCD patients and reported elevated soluble ST2 (sST2) at diagnosis with reductions after remission; podocyte IL-33 expression was increased by immunofluorescence, and patient serum induced IL-33 secretion from podocytes in vitro, suggesting IL-33–related immune response involvement. (zhong2025emergingroleof pages 1-2)

## 5. Environmental Information
Environmental exposures, lifestyle factors, and specific infectious triggers were **not retrievable from the provided excerpts**. Adult consensus notes possible triggering by viral infections or allergens, but detailed exposure-level evidence was not extractable from the excerpted text. (gauckler2023diagnostikundtherapie pages 1-2)

## 6. Mechanism / Pathophysiology

### Current mechanistic model (evidence-based chain)
**Podocyte injury → foot-process effacement → heavy proteinuria → edema/nephrotic syndrome** is the central pathophysiologic chain, supported by diagnostic electron microscopy findings and clinical nephrotic syndrome presentation. (son2023outcomesofminimal pages 1-2, willcocks2024arandomisedtwoarm pages 1-2)

**Autoantibody-mediated subset (anti-nephrin):** The NEJM 2024 study provides a mechanistic link in which anti-nephrin antibodies bind at the slit diaphragm, track with activity, and in an experimental mouse immunization model induce nephrotic syndrome with slit-diaphragm IgG localization, nephrin phosphorylation, and severe cytoskeletal changes. (hengel2024autoantibodiestargetingnephrin pages 1-3)

### Upstream vs downstream mechanisms (as supported here)
- Upstream: immune dysregulation and antibody generation against nephrin (anti-nephrin positive subgroup). (hengel2024autoantibodiestargetingnephrin pages 1-3)
- Downstream: podocyte cytoskeletal/slit diaphragm dysfunction and diffuse foot-process effacement leading to nephrotic-range proteinuria. (hengel2024autoantibodiestargetingnephrin pages 1-3, willcocks2024arandomisedtwoarm pages 1-2)

### Cell types involved (CL suggestions)
Direct Cell Ontology (CL) mappings were not provided in the excerpts; evidence strongly implicates:
- **Podocytes** (glomerular epithelial cells) as the primary injured cell type. (son2023outcomesofminimal pages 1-2, hengel2024autoantibodiestargetingnephrin pages 1-3)
- **B cells** are implicated indirectly by anti-nephrin antibodies and rituximab responsiveness. (hengel2024autoantibodiestargetingnephrin pages 1-3, mirioglu2024managementofadult pages 5-6)

### GO biological process suggestions
Not explicitly enumerated in excerpts; candidate processes (require GO verification): immune response, humoral immune response, antigen–antibody response, regulation of actin cytoskeleton.

### Omics / single-cell / spatial transcriptomics
These were **not retrievable from the provided excerpts**.

## 7. Anatomical Structures Affected

### Organ/tissue/cell levels
- Primary organ: **kidney**; primary structure: **glomerulus**. (willcocks2024arandomisedtwoarm pages 1-2)
- Primary affected cell type: **podocyte** (foot-process effacement; slit diaphragm immune localization). (hengel2024autoantibodiestargetingnephrin pages 1-3, willcocks2024arandomisedtwoarm pages 1-2)

Suggested UBERON terms (require verification): kidney; glomerulus; renal corpuscle.

## 8. Temporal Development

### Onset and course
- MCD often presents with acute nephrotic syndrome in adults. (gauckler2023diagnostikundtherapie pages 1-2)
- Disease course is frequently relapsing: ERA update notes “MCD is known for its relapsing nature” and that approximately two-thirds relapse at least once after remission; trial protocol states ~75% relapse with steroid withdrawal. (mirioglu2024managementofadult pages 3-5, willcocks2024arandomisedtwoarm pages 1-2)

## 9. Inheritance and Population

### Epidemiology (selected recent statistics)
- Adult cohort introduction: MCD comprises approximately **11–20%** of adult primary nephrotic syndrome; one cited South Korean biopsy series reported **9.17%** of biopsies as MCD. (son2023outcomesofminimal pages 1-2)
- Japanese national registry of primary nephrotic syndrome (2015–2018): MCD constituted **56.2% (3394/6036)** of recorded primary nephrotic syndrome cases. (nakagawa2023demographicsandtreatment pages 1-2)

Population incidence for MCD specifically was not directly extractable from available excerpts; however, an adult RCT protocol described primary MCD and FSGS as rare, “affecting about **10 per million population/year**.” (willcocks2024arandomisedtwoarm pages 1-2)

### Demographics
Japan registry: MCD median age of onset 31 years (IQR 16–49) and biopsy age 34 years (IQR 20–50), indicating frequent presentation in younger populations relative to membranous nephropathy. (nakagawa2023demographicsandtreatment pages 2-4)

## 10. Diagnostics

### Clinical tests and biopsy findings
Adult diagnosis is based on **kidney biopsy** with characteristic pathology:
- Light microscopy: absent/minimal changes; (gauckler2023diagnostikundtherapie pages 1-2, son2023outcomesofminimal pages 1-2)
- Immunofluorescence: no immunoglobulin/complement deposition in primary MCD; (son2023outcomesofminimal pages 1-2)
- Electron microscopy: diffuse podocyte foot-process effacement. (gauckler2023diagnostikundtherapie pages 1-2, willcocks2024arandomisedtwoarm pages 1-2)

### Biomarkers
- Anti-nephrin autoantibodies are common in MCD and correlate with disease activity, supporting a role as an activity biomarker, though routine adoption is not established. (hengel2024autoantibodiestargetingnephrin pages 1-3)

### Differential diagnosis
The retrieved excerpts did not provide a structured differential diagnosis list. Practically, adult consensus and trial protocol framing places MCD in the umbrella of “podocytopathies,” particularly alongside primary FSGS, which can share nephrotic syndrome presentation but differs by focal/segmental scarring on pathology. (willcocks2024arandomisedtwoarm pages 1-2)

### Genetic testing
Guidance on genetic testing (WES/WGS/panels) was **not retrievable from the provided excerpts**.

## 11. Outcome/Prognosis

### Short- and medium-term outcomes (available quantitative data)
- Adult cohort (n=79): steroid response rates were **100%** in non-nephrotic-range proteinuria and **92.3%** in nephrotic-range; complete remission at last follow-up was **73.4%**. (son2023outcomesofminimal pages 1-2)
- Relapse burden: about **two-thirds** relapse at least once after remission; trial protocol notes **~75%** relapse as glucocorticoids are withdrawn. (mirioglu2024managementofadult pages 3-5, willcocks2024arandomisedtwoarm pages 1-2)

Mortality and long-term kidney survival specific to MCD were not directly extractable from the retrieved excerpts.

## 12. Treatment

### Guideline-concordant initial therapy (adults)
An ERA Immunonephrology Working Group update summarizing KDIGO 2021 recommends high-dose glucocorticoids for adult MCD with an upper bound of 16 weeks at high dose and tapering after remission. The excerpted KDIGO-based regimen is: “**1 mg/kg/d (max. 80 mg/d) or 2 mg/kg every other day (max. 120 mg/d) for a minimum of 4 weeks, and a maximum of 16 weeks. Taper might be started 2 weeks after CR is obtained**.” (mirioglu2024managementofadult pages 5-6)

The same source notes a KDIGO stopping rule concept: “a patient with no proteinuria response at 16 weeks is unlikely to benefit from continuing high-dose glucocorticoid therapy.” (mirioglu2024managementofadult pages 3-5)

### Steroid-sparing and relapse-prevention strategies
Adult consensus and ERA update identify calcineurin inhibitors, cyclophosphamide, mycophenolic acid, and rituximab as options for steroid-dependent, steroid-resistant, and/or frequently relapsing disease, reflecting real-world practice to reduce relapse and cumulative steroid toxicity. (gauckler2023diagnostikundtherapie pages 1-2, mirioglu2024managementofadult pages 5-6)

### Rituximab (real-world evidence and trials)
- **Low-dose rituximab retrospective study (Apr 2023, BMC Nephrology):** 33 adults with MCD; relapse-treatment group (n=22) receiving 200 mg weekly ×4 then 200 mg q6 months had 95.45% remission and 90.90% relapse-free during follow-up; relapse-prevention group (n=11) receiving 200 mg q6 months had no relapses during median 12 months. (zhang2023efficacyoflowdose pages 1-2)
- **TURING trial protocol (Aug 2024):** phase III, double-blind, placebo-controlled adult RCT recruiting 130–150 participants with de novo or relapsing MCD/FSGS; rituximab 1 g ×2 two weeks apart (and optional week-26 dose if in remission), with standardized steroid taper; primary endpoint is time from remission to relapse. (willcocks2024arandomisedtwoarm pages 1-2, willcocks2024arandomisedtwoarm pages 4-5)

### Real-world implementations and algorithms (visual evidence)
The ERA update includes a visual management summary (flowchart) for adult MCD and a table of steroid regimens (KDIGO vs MINTAC/TURING). (mirioglu2024managementofadult media 6fdf5a00, mirioglu2024managementofadult media fcda3580)

### MAXO suggestions (treatments)
MAXO terms were not provided in excerpts; candidate actions (require MAXO verification): glucocorticoid therapy; B-cell depletion therapy (rituximab); calcineurin inhibitor therapy; cyclophosphamide therapy.

## 13. Prevention
Primary prevention strategies were **not retrievable from the provided excerpts**. The main preventable burdens reflected here are relapse- and treatment-related complications; trial and consensus documents emphasize steroid-sparing approaches to reduce cumulative toxicity. (willcocks2024arandomisedtwoarm pages 1-2)

## 14. Other Species / Natural Disease
Not retrievable from the provided excerpts.

## 15. Model Organisms
A mechanistic mouse model was created in which active immunization with recombinant murine nephrin induced a nephrotic syndrome and MCD-like phenotype, supporting pathogenicity of anti-nephrin autoimmunity. (hengel2024autoantibodiestargetingnephrin pages 1-3)

## Key 2023–2024 Developments (executive synthesis)
1. **Autoimmune subset defined by anti-nephrin antibodies (NEJM 2024):** high prevalence in MCD and correlation with activity; experimental model supports causality. (hengel2024autoantibodiestargetingnephrin pages 1-3)
2. **Adult management refinement and trial pipeline (ERA update 2024 + TURING 2024):** codifies KDIGO-based steroid regimens/limits and highlights rituximab-focused adult RCTs. (mirioglu2024managementofadult pages 5-6, willcocks2024arandomisedtwoarm pages 1-2)
3. **Real-world rituximab minimization strategies (BMC Nephrol 2023):** suggests low-dose schedules may maintain remission with steroid-sparing in selected adults (retrospective evidence). (zhang2023efficacyoflowdose pages 1-2)

## Structured summary table
| Category | Summary | Key sources (URL; publication date) | Evidence IDs |
|---|---|---|---|
| Identifiers & synonyms | **Disease:** Minimal Change Disease (**MCD**); also called **minimal change nephropathy**, **minimal change glomerulopathy**, and **minimal change nephrotic syndrome (MCNS)** in cited sources. **ICD-10:** not retrieved. **MeSH:** not retrieved. **MONDO:** not retrieved. | Gauckler et al., *Diagnostik und Therapie der Minimal Change Glomerulopathie beim Erwachsenen – 2023* — https://doi.org/10.1007/s00508-023-02258-5; Aug 2023. Willcocks et al., *TURING trial protocol* — https://doi.org/10.1186/s12882-024-03576-0; Aug 2024. | (gauckler2023diagnostikundtherapie pages 1-2, willcocks2024arandomisedtwoarm pages 1-2) |
| Core definition & pathology hallmarks | MCD is a **podocytopathy/glomerular disease** that typically presents with **acute nephrotic syndrome**. Diagnostic hallmarks in adults are **near-normal or absent light-microscopic changes**, **absence of immune-complex/electron-dense deposits**, and **diffuse podocyte foot-process effacement on electron microscopy**; biopsy is generally required in adults. | Son et al., *PLOS ONE* — https://doi.org/10.1371/journal.pone.0289870; Aug 2023. Gauckler et al. — https://doi.org/10.1007/s00508-023-02258-5; Aug 2023. | (gauckler2023diagnostikundtherapie pages 1-2, son2023outcomesofminimal pages 1-2) |
| Epidemiology & outcomes | In adults, MCD accounts for about **11–20% of primary nephrotic syndrome**; a South Korean biopsy series cited by Son et al. found **9.17%** of biopsies were MCD. Japanese registry data: **56.2%** of primary nephrotic syndrome cases were MCD (3394/6036). Relapse is common: **~75% relapse as glucocorticoids are withdrawn**; **approximately two-thirds** have at least one relapse after remission, and **up to one-third** become frequently relapsing/steroid-dependent. Steroid response is usually high: in Son et al., remission after steroids was **100%** in non-nephrotic-range proteinuria and **92.3%** in nephrotic-range disease; complete remission at final visit was **73.4%**. Japanese registry: **70.2%** steroid-dependent/frequently relapsing; **6.4%** steroid-resistant. | Son et al. — https://doi.org/10.1371/journal.pone.0289870; Aug 2023. Mirioglu et al., *Nephrol Dial Transplant* — https://doi.org/10.1093/ndt/gfae025; Feb 2024. Nakagawa et al., *Scientific Reports* — https://doi.org/10.1038/s41598-023-41909-5; Sep 2023. Willcocks et al. — https://doi.org/10.1186/s12882-024-03576-0; Aug 2024. | (mirioglu2024managementofadult pages 3-5, son2023outcomesofminimal pages 1-2, nakagawa2023demographicsandtreatment pages 1-2, nakagawa2023demographicsandtreatment pages 2-4, willcocks2024arandomisedtwoarm pages 1-2) |
| Mechanistic advances (2023–2024) | **Anti-nephrin autoantibodies:** major 2024 advance supporting an autoimmune subset of MCD. In adults, anti-nephrin antibodies were found in **44% (46/105)** of MCD patients; in children with idiopathic nephrotic syndrome **52% (94/182)** were positive; prevalence rose to **69%** in active untreated adult MCD and **90%** in untreated active children. Levels correlated with **disease activity/remission**, and experimental immunization induced an **MCD-like nephrotic phenotype** with slit-diaphragm IgG localization, nephrin phosphorylation, and cytoskeletal change. Gauckler notes an earlier cited study with **~30%** positivity. **IL-33/ST2 axis:** serum **sST2** was elevated in MCD at diagnosis, correlated inversely with total protein and positively with creatinine, fell with remission, and podocyte IL-33 expression was increased—supporting a type-2/alarmin-related immune pathway. | Hengel et al., *NEJM* — https://doi.org/10.1056/NEJMoa2314471; Aug 2024. Gauckler et al. — https://doi.org/10.1007/s00508-023-02258-5; Aug 2023. | (gauckler2023diagnostikundtherapie pages 1-2, hengel2024autoantibodiestargetingnephrin pages 1-3) |
| Treatment: glucocorticoids (guideline dosing) | **KDIGO-based initial adult regimen:** prednisone/prednisolone **1 mg/kg/day (max 80 mg/day)** or **2 mg/kg every other day (max 120 mg)** for a **minimum of 4 weeks** and **maximum of 16 weeks**; taper may start **2 weeks after complete remission**. Lack of proteinuria response by **16 weeks** suggests continued high-dose steroids are unlikely to help. Trial regimens summarized by ERA IWG: MINTAC prednisolone arm achieved **84% remission at 8 weeks** and **92% at 16 weeks**. | Mirioglu et al. — https://doi.org/10.1093/ndt/gfae025; Feb 2024. | (mirioglu2024managementofadult pages 5-6) |
| Treatment: rituximab low-dose evidence | Retrospective adult low-dose RTX study (33 biopsy-proven MCD cases): **relapse-treatment cohort n=22** received **200 mg weekly ×4, then 200 mg every 6 months**; **95.45%** remitted (**86.36% CR**, **9.09% PR**), **90.90%** remained relapse-free, median sustained remission **16.3 months**. **Relapse-prevention cohort n=11** received **200 mg every 6 months** and had **0 relapses** during median **12-month** follow-up. Prednisone dose fell significantly after RTX. | Zhang et al., *BMC Nephrology* — https://doi.org/10.1186/s12882-023-03092-7; Apr 2023. | (zhang2023efficacyoflowdose pages 1-2) |
| Treatment: TURING trial / real-world implementation | **TURING** is a **phase III**, **double-blind**, **placebo-controlled**, **1:1 randomized** adult trial of rituximab for **de novo or relapsing MCD/FSGS**, planned enrollment **130–150**. Regimen: **rituximab 1 g ×2 infusions two weeks apart** (plus optional week-26 dose if in remission) versus placebo, with all patients receiving glucocorticoids per KDIGO and tapering after remission. **Primary endpoint:** time from remission to relapse. This reflects current real-world movement toward steroid-sparing, B-cell–targeted therapy while adult RCT evidence is still being generated. | Willcocks et al. — https://doi.org/10.1186/s12882-024-03576-0; Aug 2024. | (willcocks2024arandomisedtwoarm pages 1-2) |
| Clinical interpretation | Overall, current evidence supports MCD as a **mostly steroid-sensitive but relapse-prone autoimmune podocytopathy**, with emerging biomarker-defined subgroups (especially **anti-nephrin-positive** disease) and increasing use of **rituximab** to reduce steroid exposure and prevent relapse. | Synthesized from cited 2023–2024 studies above. | (mirioglu2024managementofadult pages 3-5, gauckler2023diagnostikundtherapie pages 1-2, hengel2024autoantibodiestargetingnephrin pages 1-3, mirioglu2024managementofadult pages 5-6, zhang2023efficacyoflowdose pages 1-2) |


*Table: This table condenses key identifiers, pathology, epidemiology, mechanistic advances, and treatment evidence for minimal change disease using only the specified context IDs. It is designed as a compact reference for rapid knowledge-base population and citation tracing.*

## Notes on evidence gaps in this run
- Standard identifiers (MONDO/MeSH/Orphanet/OMIM/ICD) and formal ontology mappings (HPO/GO/CL/UBERON/MAXO codes) were not available in retrieved excerpts; candidate terms are provided only as suggestions and should be verified against the corresponding ontology resources.
- Detailed differential diagnosis lists, granular environmental risk factors, and comprehensive genetic testing guidance were not extractable from the present evidence set.


References

1. (gauckler2023diagnostikundtherapie pages 1-2): Philipp Gauckler, Heinz Regele, Kathrin Eller, Marcus D. Säemann, Karl Lhotta, Emanuel Zitt, Irmgard Neumann, Michael Rudnicki, Balazs Odler, Andreas Kronbichler, and Martin Windpessl. Diagnostik und therapie der minimal change glomerulopathie beim erwachsenen – 2023. Wiener Klinische Wochenschrift, 135:628-637, Aug 2023. URL: https://doi.org/10.1007/s00508-023-02258-5, doi:10.1007/s00508-023-02258-5. This article has 0 citations and is from a peer-reviewed journal.

2. (son2023outcomesofminimal pages 1-2): Hyung Eun Son, Giae Yun, Eun-Jeong Kwon, Seokwoo Park, Jong Cheol Jeong, Sejoong Kim, Ki Young Na, Jin Ho Paik, and Ho Jun Chin. Outcomes of minimal change disease without nephrotic range proteinuria. PLOS ONE, 18:e0289870, Aug 2023. URL: https://doi.org/10.1371/journal.pone.0289870, doi:10.1371/journal.pone.0289870. This article has 3 citations and is from a peer-reviewed journal.

3. (willcocks2024arandomisedtwoarm pages 1-2): Lisa C Willcocks, Wendi Qian, Ruzaika Cader, Katrina Gatley, Hira Siddiqui, Endurance Tabebisong, Karlena Champion, Andreas Kronbichler, Liz Lightstone, David Jayne, Edward Wilson, and Megan Griffith. A randomised, two-arm (1:1 ratio), double blind, placebo controlled phase iii trial to assess the efficacy, safety, cost and cost-effectiveness of rituximab in treating de novo or relapsing ns in patients with mcd/fsgs (turing). BMC Nephrology, Aug 2024. URL: https://doi.org/10.1186/s12882-024-03576-0, doi:10.1186/s12882-024-03576-0. This article has 5 citations and is from a peer-reviewed journal.

4. (hengel2024autoantibodiestargetingnephrin pages 1-3): Felicitas E. Hengel, Silke Dehde, Moritz Lassé, Gunther Zahner, Larissa Seifert, Annabel Schnarre, Oliver Kretz, Fatih Demir, Hans O. Pinnschmidt, Florian Grahammer, Renke Lucas, Lea Maxima Mehner, Tom Zimmermann, Anja M. Billing, Jun Oh, Adele Mitrotti, Paola Pontrelli, Hanna Debiec, Claire Dossier, Manuela Colucci, Francesco Emma, William E. Smoyer, Astrid Weins, Franz Schaefer, Nada Alachkar, Anke Diemert, Julien Hogan, Elion Hoxha, Thorsten Wiech, Markus M. Rinschen, Pierre Ronco, Marina Vivarelli, Loreto Gesualdo, Nicola M. Tomas, and Tobias B. Huber. Autoantibodies targeting nephrin in podocytopathies. New England Journal of Medicine, 391:422-433, Aug 2024. URL: https://doi.org/10.1056/nejmoa2314471, doi:10.1056/nejmoa2314471. This article has 252 citations and is from a highest quality peer-reviewed journal.

5. (nakagawa2023demographicsandtreatment pages 1-2): Naoki Nakagawa, Tomonori Kimura, Ryuichi Sakate, Takehiko Wada, Kengo Furuichi, Hirokazu Okada, Yoshitaka Isaka, and Ichiei Narita. Demographics and treatment of patients with primary nephrotic syndrome in japan using a national registry of clinical personal records. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-41909-5, doi:10.1038/s41598-023-41909-5. This article has 8 citations and is from a peer-reviewed journal.

6. (mirioglu2024managementofadult pages 3-5): Safak Mirioglu, Lisa Daniel-Fischer, Ilay Berke, Syed Hasan Ahmad, Ingeborg M Bajema, Annette Bruchfeld, Gema M Fernandez-Juarez, Jürgen Floege, Eleni Frangou, Dimitrios Goumenos, Megan Griffith, Sarah M Moran, Cees van Kooten, Stefanie Steiger, Kate I Stevens, Kultigin Turkmen, Lisa C Willcocks, and Andreas Kronbichler. Management of adult patients with podocytopathies: an update from the era immunonephrology working group. Nephrology Dialysis Transplantation, 39:569-580, Feb 2024. URL: https://doi.org/10.1093/ndt/gfae025, doi:10.1093/ndt/gfae025. This article has 31 citations and is from a domain leading peer-reviewed journal.

7. (nakagawa2023demographicsandtreatment pages 2-4): Naoki Nakagawa, Tomonori Kimura, Ryuichi Sakate, Takehiko Wada, Kengo Furuichi, Hirokazu Okada, Yoshitaka Isaka, and Ichiei Narita. Demographics and treatment of patients with primary nephrotic syndrome in japan using a national registry of clinical personal records. Scientific Reports, Sep 2023. URL: https://doi.org/10.1038/s41598-023-41909-5, doi:10.1038/s41598-023-41909-5. This article has 8 citations and is from a peer-reviewed journal.

8. (zhong2025emergingroleof pages 1-2): Anni Zhong, Yi Yu, Tao Cao, Qijun Wan, and Ricong Xu. Emerging role of rituximab in adult minimal change disease: a narrative review of clinical evidence, biomarkers and future perspectives. BMC Nephrology, Mar 2025. URL: https://doi.org/10.1186/s12882-025-04086-3, doi:10.1186/s12882-025-04086-3. This article has 3 citations and is from a peer-reviewed journal.

9. (mirioglu2024managementofadult pages 5-6): Safak Mirioglu, Lisa Daniel-Fischer, Ilay Berke, Syed Hasan Ahmad, Ingeborg M Bajema, Annette Bruchfeld, Gema M Fernandez-Juarez, Jürgen Floege, Eleni Frangou, Dimitrios Goumenos, Megan Griffith, Sarah M Moran, Cees van Kooten, Stefanie Steiger, Kate I Stevens, Kultigin Turkmen, Lisa C Willcocks, and Andreas Kronbichler. Management of adult patients with podocytopathies: an update from the era immunonephrology working group. Nephrology Dialysis Transplantation, 39:569-580, Feb 2024. URL: https://doi.org/10.1093/ndt/gfae025, doi:10.1093/ndt/gfae025. This article has 31 citations and is from a domain leading peer-reviewed journal.

10. (zhang2023efficacyoflowdose pages 1-2): Jian Zhang, Hui Zhao, Xiaoli Li, Rui Qian, Peijuan Gao, Shou-Yan Lu, and Zhigang Ma. Efficacy of low-dose rituximab in minimal change disease and prevention of relapse. BMC Nephrology, Apr 2023. URL: https://doi.org/10.1186/s12882-023-03092-7, doi:10.1186/s12882-023-03092-7. This article has 18 citations and is from a peer-reviewed journal.

11. (willcocks2024arandomisedtwoarm pages 4-5): Lisa C Willcocks, Wendi Qian, Ruzaika Cader, Katrina Gatley, Hira Siddiqui, Endurance Tabebisong, Karlena Champion, Andreas Kronbichler, Liz Lightstone, David Jayne, Edward Wilson, and Megan Griffith. A randomised, two-arm (1:1 ratio), double blind, placebo controlled phase iii trial to assess the efficacy, safety, cost and cost-effectiveness of rituximab in treating de novo or relapsing ns in patients with mcd/fsgs (turing). BMC Nephrology, Aug 2024. URL: https://doi.org/10.1186/s12882-024-03576-0, doi:10.1186/s12882-024-03576-0. This article has 5 citations and is from a peer-reviewed journal.

12. (mirioglu2024managementofadult media 6fdf5a00): Safak Mirioglu, Lisa Daniel-Fischer, Ilay Berke, Syed Hasan Ahmad, Ingeborg M Bajema, Annette Bruchfeld, Gema M Fernandez-Juarez, Jürgen Floege, Eleni Frangou, Dimitrios Goumenos, Megan Griffith, Sarah M Moran, Cees van Kooten, Stefanie Steiger, Kate I Stevens, Kultigin Turkmen, Lisa C Willcocks, and Andreas Kronbichler. Management of adult patients with podocytopathies: an update from the era immunonephrology working group. Nephrology Dialysis Transplantation, 39:569-580, Feb 2024. URL: https://doi.org/10.1093/ndt/gfae025, doi:10.1093/ndt/gfae025. This article has 31 citations and is from a domain leading peer-reviewed journal.

13. (mirioglu2024managementofadult media fcda3580): Safak Mirioglu, Lisa Daniel-Fischer, Ilay Berke, Syed Hasan Ahmad, Ingeborg M Bajema, Annette Bruchfeld, Gema M Fernandez-Juarez, Jürgen Floege, Eleni Frangou, Dimitrios Goumenos, Megan Griffith, Sarah M Moran, Cees van Kooten, Stefanie Steiger, Kate I Stevens, Kultigin Turkmen, Lisa C Willcocks, and Andreas Kronbichler. Management of adult patients with podocytopathies: an update from the era immunonephrology working group. Nephrology Dialysis Transplantation, 39:569-580, Feb 2024. URL: https://doi.org/10.1093/ndt/gfae025, doi:10.1093/ndt/gfae025. This article has 31 citations and is from a domain leading peer-reviewed journal.