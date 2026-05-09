---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T08:40:17.179071'
end_time: '2026-05-08T08:54:21.443720'
duration_seconds: 844.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bird Fancier's Lung
  mondo_id: ''
  category: Respiratory Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bird Fancier's Lung
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Bird Fancier's Lung** covering all of the
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
- **Disease Name:** Bird Fancier's Lung
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Bird Fancier's Lung** covering all of the
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


# Bird Fancier’s Lung (BFL) / Avian Hypersensitivity Pneumonitis (HP): Disease Characteristics Research Report

## Executive summary (current understanding)
Bird fancier’s lung (BFL) is a form of hypersensitivity pneumonitis (HP)—an immune-mediated interstitial lung disease triggered by inhalation of avian-derived antigens (e.g., from live birds, feathers, droppings, and feather-containing bedding). Contemporary practice frameworks classify HP into **non-fibrotic** and **fibrotic** phenotypes based primarily on HRCT and/or pathology, because fibrosis strongly influences prognosis and treatment response. Recent (2023–2024) research emphasizes (i) structured exposure assessment, (ii) integration of HRCT + BAL lymphocytosis + serology (antigen-specific IgG/“precipitins”), and (iii) longitudinal monitoring approaches such as serial anti-pigeon IgG testing to infer ongoing exposure and track lung-function decline in fibrotic avian HP. (deutsch2024doesatype pages 2-4, akkurt2024evaluationofclinical pages 1-4, okuda2024longitudinalchangesin pages 1-2)

## 1. Disease information
### 1.1 Overview/definition
HP is described as “an interstitial inflammatory lung disease that develops as a result of exposition to various, mostly organic antigens” and can be subdivided into fibrotic and non-fibrotic forms. (deutsch2024doesatype pages 2-4)

BFL specifically refers to HP caused by exposure to bird-related antigens. In a high-confidence HP cohort, **avian antigen** exposure was operationalized as “regular exposure to a live bird or feather products,” reflecting real-world BFL exposure settings (bird ownership, bird breeding, feather bedding/down products). (kypreos2022impactofnumber pages 1-2)

### 1.2 Key identifiers (ICD/MeSH/MONDO/Orphanet)
The present tool-based literature retrieval did not return authoritative ontology/coding records (e.g., MeSH descriptor page, ICD-10/ICD-11 entry, MONDO, Orphanet) that can be directly cited. Therefore, standardized identifiers are **not populated here** to avoid uncited claims.

### 1.3 Synonyms / alternative names
Within the retrieved clinical/review literature, BFL is used in the context of “avian” HP and “bird-related” HP, and “feather” exposure is treated as a clinically important inciting antigen category. (kypreos2022impactofnumber pages 1-2)

### 1.4 Evidence sources
This report primarily reflects **aggregated disease-level** evidence from retrospective cohorts and diagnostic-method papers (with some prospective/longitudinal follow-up), rather than individual EHR case reports. (deutsch2024doesatype pages 2-4, akkurt2024evaluationofclinical pages 1-4, okuda2024longitudinalchangesin pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors
**Primary causal factor:** inhalation exposure to bird-related antigens (live birds, feathers/down products, droppings; sometimes quantified indirectly by antigen-specific IgG). Avian exposure is among the most prevalent HP exposures in contemporary cohorts. (deutsch2024doesatype pages 2-4, akkurt2024evaluationofclinical pages 1-4)

**Recent cohort evidence (2024):** In a 2019–2023 HP cohort (n=66), avian antigen exposure was one of the most prevalent exposures and was more common among fibrotic HP than non-fibrotic HP in univariate comparisons (70% vs 40%). (deutsch2024doesatype pages 9-10)

### 2.2 Risk factors
#### Environmental/occupational risk factors
- Bird/bird-product exposure dominates identified exposures in some real-world ILD-center populations: in a 2020–2024 HP cohort (n=100), 65% had identifiable exposure, and “86.4% of all known exposures were caused by exposure to birds and bird products.” (akkurt2024evaluationofclinical pages 1-4)
- Co-exposures may contribute to fibrotic phenotype in HP broadly; in the 2019–2023 cohort, avian exposure and coal/biomass heating were more prevalent among fibrotic HP than non-fibrotic HP, but **older age** was the only independent predictor of fibrotic HP in multivariable analysis. (deutsch2024doesatype pages 9-10)

#### Genetic susceptibility (host factors)
Multiple sources emphasize that host susceptibility modifies who develops fibrotic HP, but the retrieved evidence did **not** provide validated single-gene causal variants specific to BFL. For example, the 2024 cohort paper notes “genetic susceptibility… may influence the fibrotic process,” but does not specify causal genes/variants. (deutsch2024doesatype pages 9-10)

### 2.3 Protective factors
Direct, well-quantified protective factors (genetic or environmental) specific to BFL were not identified in the retrieved evidence.

### 2.4 Gene–environment interactions
The retrieved evidence supports a **gene/environment framework** (susceptible host + antigen exposure) but does not provide specific gene–environment interaction loci for BFL. (deutsch2024doesatype pages 9-10)

## 3. Phenotypes (clinical presentation)
### 3.1 Core clinical phenotypes (with suggested HPO terms)
The retrieved studies primarily characterize HP/BFL via exposure history, lung imaging, BAL profile, and lung-function decline rather than symptom prevalence counts. Key disease manifestations that can be mapped to HPO include:

- Dyspnea/shortness of breath (HP:0002094) (inferred as a core ILD manifestation; outcomes include SOBQ in trials) (NCT02496182 chunk 1)
- Cough (HP:0012735) (typical ILD symptom; not quantified in retrieved excerpts)
- Reduced forced vital capacity / restrictive physiology (HP:0033280 “Abnormal lung function test” / or use LOINC mapping for FVC) (okuda2024longitudinalchangesin pages 1-2)
- Reduced diffusing capacity / DLCO abnormality (HP:0002091 “Decreased diffusing capacity of lung for carbon monoxide”) (sadeleer2018effectsofcorticosteroid pages 6-8)
- Imaging phenotypes consistent with HP:
  - Ground-glass opacities (HPO does not directly encode CT patterns; use radiology ontology in implementation)
  - Centrilobular nodules
  - Air trapping / mosaic attenuation / “three-density sign”
  - Fibrosis features: reticulation, traction bronchiectasis, honeycombing, reduced lung volumes (deutsch2024doesatype pages 2-4, akkurt2024evaluationofclinical pages 1-4)

### 3.2 Phenotype characteristics: fibrotic vs non-fibrotic
Modern cohorts apply a phenotype split that is prognostically meaningful:
- In a 2018 cohort (n=202), fibrotic HP had substantially worse prognosis with **median survival 9.2 years**, while non-fibrotic HP had “excellent survival” (median not reached). (sadeleer2018effectsofcorticosteroid pages 1-3, sadeleer2018effectsofcorticosteroid pages 3-6)

### 3.3 Frequency and real-world distributions from recent studies
- HRCT findings (2020–2024 cohort, n=100): reticulation 87%, ground-glass opacities 84.7%, centrilobular nodules 75%, and fibrotic features 40%. (akkurt2024evaluationofclinical pages 1-4)

### 3.4 Quality of life (QoL) impact
QoL impairment is inferred from use of validated QoL and dyspnea measures in chronic HP trials (e.g., SGRQ, SOBQ, EQ-5D). (NCT02496182 chunk 1)

## 4. Genetic / molecular information
### 4.1 Causal genes
No monogenic causal genes for BFL were supported by the retrieved evidence.

### 4.2 Biomarkers and molecular tests (2023–2024 emphasis)
#### Antigen-specific IgG (“precipitins”)
**Key concept:** antigen-specific IgG supports exposure/sensitization assessment but is not sufficient alone to confirm or exclude HP.

**2024 development—longitudinal serology:** A 2024 longitudinal cohort of **fibrotic avian HP** (n=28) found that annual changes in anti-pigeon IgG correlate with changes in FVC: ELISA r = −0.6221 (p<0.001) and ImmunoCAP r = −0.4302 (p=0.022); multiple regression retained significant associations (p=0.012 and p=0.015). The abstract states: “the annual changes in serum IgG antibody titers… correlated with FVC changes.” (okuda2024longitudinalchangesin pages 1-2)

**2024 diagnostic serology cutoffs:** A 10-year retrospective study (54 HP cases; 1516 controls) using a population-derived 97.5th percentile control cutoff reported that 30/54 (56%) HP patients had ≥1 positive IgG precipitin; pigeon-dropping IgG was the most frequent positive, and cutoff values were explicitly reported (e.g., pigeon droppings 62.4 mg/L). (intra2024theroleof pages 1-2, intra2024theroleof pages 5-6)

## 5. Environmental information
### 5.1 Environmental determinants and exposure sources
BFL/avian HP exposures include:
- Live birds and bird breeding/keeping, with sustained exposure duration in many patients (e.g., 19/28 had kept birds >6 months in one fibrotic avian HP cohort). (okuda2024longitudinalchangesin pages 1-2)
- Feather/down products (e.g., feather bedding); these are clinically relevant enough that “feather exposure should be considered an inciting antigen in patients with ILD.” (kypreos2022impactofnumber pages 1-2)

### 5.2 Lifestyle factors
Smoking and other lifestyle factors were not systematically extractable from the cited evidence snippets; thus, they are not summarized with statistics here.

### 5.3 Infectious agents
No specific infectious agent etiology is supported; BFL is characterized as an immune response to inhaled antigens rather than infection. (deutsch2024doesatype pages 2-4)

## 6. Mechanism / pathophysiology
### 6.1 Current mechanistic model (causal chain)
1) Repeated inhalation of bird-related antigens → 2) immune sensitization and immune-mediated alveolitis (often with BAL lymphocytosis) → 3) granulomatous/interstitial inflammation and small-airway involvement → 4) in some individuals, progression to lung fibrosis (fibrotic HP) with worsening restrictive physiology and impaired gas exchange. This broad chain is consistent with modern descriptions that HP is “characterized by immune-mediated inflammation and variable degrees of fibrosis.” (akkurt2024evaluationofclinical pages 1-4)

### 6.2 Immune system involvement and key processes (ontology suggestions)
Suggested GO biological process terms (implementation suggestions):
- GO:0006954 inflammatory response
- GO:0002250 adaptive immune response
- GO:0006950 response to stress
- GO:0042110 T cell activation
- GO:0001817 regulation of cytokine production
- GO:0043062 extracellular matrix organization (fibrotic phenotype)

Suggested Cell Ontology (CL) cell types:
- CL:0000583 alveolar macrophage
- CL:0000084 T cell
- CL:0000236 B cell
- CL:0000542 lymphocyte
- CL:0000182 neutrophil (noting exploratory blood-count associations with HRCT fibrosis features in a 2020–2024 cohort) (akkurt2024evaluationofclinical pages 1-4)

### 6.3 Recent mechanistic/biomarker angle: exposure persistence and serology
Serial anti-pigeon IgG change plausibly reflects ongoing/recurrent antigen exposure and is statistically linked to annual FVC decline in fibrotic avian HP, providing a mechanistically grounded monitoring concept (antigen exposure burden ↔ immune response intensity ↔ disease progression). (okuda2024longitudinalchangesin pages 1-2, okuda2024longitudinalchangesin pages 7-8)

## 7. Anatomical structures affected
### 7.1 Organ and tissue level (UBERON suggestions)
Primary: lung (UBERON:0002048), pulmonary alveolus (UBERON:0002299), bronchiole/small airways (UBERON:0002180).

The clinical characterization explicitly describes involvement of “lung parenchyma and small airways.” (akkurt2024evaluationofclinical pages 1-4)

## 8. Temporal development
### 8.1 Onset and course
HP includes non-fibrotic and fibrotic phenotypes with different clinical trajectories. Fibrotic disease course is associated with chronicity and worse outcomes, while non-fibrotic HP may show physiologic improvement with corticosteroids and exposure avoidance. (sadeleer2018effectsofcorticosteroid pages 1-3, sadeleer2018effectsofcorticosteroid pages 3-6)

## 9. Inheritance and population
### 9.1 Epidemiology
The retrieved evidence base did not contain population-level incidence/prevalence rates specific to BFL (e.g., cases per 100,000). Therefore epidemiologic rates are not provided here.

### 9.2 Population demographics and distributions (from available cohorts)
- Example cohort demographics for fibrotic avian HP (Japan, 2024): mean age 64.5 years, mean FVC 85.3% predicted. (okuda2024longitudinalchangesin pages 1-2)
- Sex distribution varies by cohort; one HP cohort had “equal sex distribution.” (akkurt2025fibroticpatternsand pages 12-12)

## 10. Diagnostics
### 10.1 Key diagnostic concepts (current practice)
Diagnosis is integrative, typically combining:
- **Exposure assessment** (semi-structured questionnaires) (deutsch2024doesatype pages 2-4)
- **HRCT pattern classification** (fibrotic vs non-fibrotic features and small-airway signs) (deutsch2024doesatype pages 2-4)
- **BAL cellular analysis** (lymphocytosis as supportive evidence) (deutsch2024doesatype pages 2-4)
- **Serology** (antigen-specific IgG/precipitins for relevant antigens) (deutsch2024doesatype pages 2-4, intra2024theroleof pages 1-2)
- **Histopathology** in selected cases (e.g., surgical lung biopsy or cryobiopsy) (okuda2024longitudinalchangesin pages 1-2)
- **Inhalation challenge testing** in specialized settings (e.g., pasteurized pigeon egg solution protocol in a fibrotic avian HP cohort) (okuda2024longitudinalchangesin pages 2-4)

### 10.2 Recent diagnostic data points
- BAL lymphocytosis: in the 2019–2023 cohort, median BAL lymphocytes were 38.8% (IQR 26.9–52.6). (deutsch2024doesatype pages 2-4)
- HRCT: fibrotic HP definition included reticular opacities, traction bronchiectasis, reduced lung volume, honeycombing, plus small-airway findings (centrilobular nodules, ground-glass, air trapping, three-density sign). (deutsch2024doesatype pages 2-4)
- Serology cutoffs (example panel, 2024): pigeon droppings IgG cutoff 62.4 mg/L (97.5th percentile controls) and other antigen cutoffs (Penicillium 71.0 mg/L; Aspergillus fumigatus 61.8 mg/L; Alternaria 35.3 mg/L; Aspergillus niger 44.3 mg/L; Micropolyspora faeni 20.5 mg/L). (intra2024theroleof pages 5-6)

### 10.3 Differential diagnosis
The retrieved excerpts did not provide a structured differential diagnosis list. In practice, major differentials for fibrotic HP include idiopathic pulmonary fibrosis and connective tissue disease–associated ILD; however, these statements are not expanded here without direct supporting excerpts.

## 11. Outcome / prognosis
### 11.1 Prognostic strata: fibrotic vs non-fibrotic
Fibrosis is a major determinant of prognosis:
- In a 2018 cohort, fibrotic HP median survival was 9.2 years and fibrotic vs non-fibrotic HP carried HR 4.35 (95% CI 2.22–8.33). (sadeleer2018effectsofcorticosteroid pages 3-6)

### 11.2 Antigen identification and outcomes (real-world prognostic implications)
- In a high-confidence chronic HP cohort (n=136), identification of an inciting antigen by clinical history was independently associated with better transplant-free survival (HR 0.39, 95% CI 0.17–0.89). Median transplant-free survival was 4.89 years with no antigen identified vs 12.8 years with one identified antigen; feather exposure had HR 0.30 vs no antigen (95% CI 0.10–0.96). (kypreos2022impactofnumber pages 4-5, kypreos2022impactofnumber pages 5-7)

## 12. Treatment
### 12.1 Core management principle: exposure remediation/avoidance
Exposure avoidance is a cornerstone intervention:
- In non-fibrotic HP, avoidance was associated with improved lung-function trajectory (FVC from −0.24%/month to +0.92%/month, p=0.016; DLCO from −0.23%/month to +0.37%/month with an immediate +4.0% increase, p=0.04). (sadeleer2018effectsofcorticosteroid pages 6-8)

Suggested MAXO terms (implementation suggestions):
- MAXO:0000527 “avoidance of allergen exposure” (or nearest available allergen/antigen avoidance term)
- MAXO:0000499 “environmental intervention”

### 12.2 Corticosteroids and immunosuppression
- In the same large cohort, corticosteroids improved physiology in non-fibrotic HP (e.g., FVC from −0.35%/month to +0.84%/month after steroids, p<0.001) but showed no physiologic benefit in fibrotic HP and no survival benefit overall. (sadeleer2018effectsofcorticosteroid pages 3-6)

Suggested MAXO terms:
- systemic glucocorticoid therapy
- immunosuppressive therapy (e.g., azathioprine in some trial protocols) (NCT02496182 chunk 1)

### 12.3 Antifibrotics and clinical trials (real-world implementation and ongoing evidence)
Because fibrotic HP can behave like progressive pulmonary fibrosis, antifibrotic strategies have been studied in HP-specific and broader PPF settings.

**Pirfenidone trials in chronic/fibrotic HP (ClinicalTrials.gov):**
- NCT02958917 (posted 2017; terminated during COVID-19): randomized, double-blind trial in fibrotic HP; pirfenidone 2403 mg/day vs placebo for 52 weeks; primary endpoint = change in % predicted FVC at week 52; key inclusion included multidisciplinary-consensus fibrotic HP, age 18–80, FVC ≥40%, DLCO ≥30%. URL: https://clinicaltrials.gov/study/NCT02958917 (NCT02958917 chunk 1, NCT02958917 chunk 2)
- NCT04675619 (start 2019; completed): progressive chronic HP with >10% fibrosis on HRCT and absolute FVC decline >5% in prior 6 months; pirfenidone + standard care vs standard care; endpoints included FVC and 6MWD at 6 months. URL: https://clinicaltrials.gov/study/NCT04675619 (NCT04675619 chunk 1)

Suggested MAXO terms:
- antifibrotic therapy
- pirfenidone treatment

## 13. Prevention
Primary prevention is largely exposure-based: minimizing/avoiding inhalation of bird-derived antigens and feather/down exposure in susceptible individuals or in settings where symptoms have occurred. Prognostic evidence supports that identifying an inciting antigen is associated with improved transplant-free survival, reinforcing prevention via exposure identification/remediation. (kypreos2022impactofnumber pages 5-7)

## 14. Other species / natural disease
No tool-retrieved evidence in this run addressed naturally occurring BFL-like disease in non-human species or zoonotic transmission.

## 15. Model organisms
No tool-retrieved evidence in this run described specific model organisms for BFL/avian HP. (General HP models exist in the literature, but are not summarized here without direct citations.)

## Recent developments (2023–2024) highlighted
1) **Longitudinal serology as disease monitoring in fibrotic avian HP:** serial anti-pigeon IgG (ELISA/ImmunoCAP) correlates with FVC decline (Okuda 2024). (okuda2024longitudinalchangesin pages 1-2, okuda2024longitudinalchangesin pages 2-4)
2) **Population-derived precipitin cutoffs and antigen-panel optimization:** large control dataset used to define 97.5th percentile cutoffs for common antigens including pigeon droppings (Intra 2024). (intra2024theroleof pages 1-2, intra2024theroleof pages 5-6)
3) **Modern cohort quantification of exposure patterns and HRCT findings:** bird/bird-product exposures dominate identified exposures in a tertiary cohort and HRCT frequencies are quantified (Akkurt 2024). (akkurt2024evaluationofclinical pages 1-4)

## Structured evidence table
The following table summarizes high-yield, tool-retrieved evidence most relevant to a BFL knowledge-base entry.

| Topic | Key finding | Study (author year journal) | Population/design | URL/DOI | Citation |
|---|---|---|---|---|---|
| Exposure | In a 2024 HP cohort, 94% reported at least one exposure; avian exposure was more common in fibrotic vs non-fibrotic HP (70% vs 40%, p=0.03), though older age was the only independent predictor of fibrosis. | Deutsch et al. 2024, *Journal of Clinical Medicine* | Retrospective cohort, 66 HP patients diagnosed 2019-2023 | https://doi.org/10.3390/jcm13175074 | (deutsch2024doesatype pages 2-4) |
| Exposure | In a 2024 tertiary-center HP cohort, 65% had identifiable exposure and 86.4% of known exposures were birds/bird products. | Akkurt et al. 2024, preprint | Retrospective cross-sectional study, 100 HP patients (2020-2024) | https://doi.org/10.21203/rs.3.rs-5418767/v1 | (akkurt2024evaluationofclinical pages 1-4) |
| Diagnosis | Median BAL lymphocyte proportion was 38.8% (IQR 26.9-52.6) in the 2024 cohort; fibrotic HP was classified by CT fibrosis (reticulation, traction bronchiectasis, reduced volume, honeycombing) plus small-airway findings. | Deutsch et al. 2024, *Journal of Clinical Medicine* | Retrospective cohort, 66 HP patients | https://doi.org/10.3390/jcm13175074 | (deutsch2024doesatype pages 2-4) |
| Diagnosis | Common HRCT findings in HP were reticulation 87%, ground-glass opacities 84.7%, and centrilobular nodules 75%; fibrotic features were present in 40%. | Akkurt et al. 2024, preprint | Retrospective cross-sectional study, 100 HP patients | https://doi.org/10.21203/rs.3.rs-5418767/v1 | (akkurt2024evaluationofclinical pages 1-4) |
| Biomarkers | Serial anti-pigeon IgG correlated with lung-function decline in fibrotic avian HP: annual IgG change vs relative FVC change, ELISA r=-0.6221 (p<0.001), ImmunoCAP r=-0.4302 (p=0.022); multiple regression remained significant (p=0.012 and p=0.015). | Okuda et al. 2024, *BMC Pulmonary Medicine* | Longitudinal cohort, 28 fibrotic avian HP patients | https://doi.org/10.1186/s12890-024-03063-0 | (okuda2024longitudinalchangesin pages 1-2, okuda2024longitudinalchangesin pages 2-4) |
| Biomarkers | Using 97.5th-percentile control cutoffs, 30/54 HP patients (56%) had ≥1 positive precipitin; pigeon-dropping IgG was the most frequent positive, with 23/30 positive cases showing elevated pigeon-dropping IgG. | Intra et al. 2024, *International Journal of Translational Medicine* | 10-year retrospective study; 54 HP cases, 1516 controls | https://doi.org/10.3390/ijtm4020025 | (intra2024theroleof pages 4-5, intra2024theroleof pages 1-2, intra2024theroleof pages 5-6) |
| Prognosis | Identification of an inciting antigen independently predicted better transplant-free survival (HR 0.39, 95% CI 0.17-0.89, p=0.025). No-antigen group had median transplant-free survival 4.89 years vs 12.8 years for one identified antigen; feather exposure HR 0.30 vs no antigen (95% CI 0.10-0.96, p=0.043). | Kypreos et al. 2022, *PLoS ONE* | Retrospective cohort, 136 high/definite chronic HP patients | https://doi.org/10.1371/journal.pone.0273544 | (kypreos2022impactofnumber pages 4-5, kypreos2022impactofnumber pages 5-7) |
| Prognosis | Fibrotic HP had markedly worse outcomes than non-fibrotic HP: median survival 9.2 years in fibrotic HP, while median survival was not reached in non-fibrotic HP; HR for fibrotic vs non-fibrotic HP 4.35 (95% CI 2.22-8.33, p<0.001). | De Sadeleer et al. 2018, *Journal of Clinical Medicine* | Single-center cohort, 202 HP patients (109 fibrotic, 93 non-fibrotic) | https://doi.org/10.3390/jcm8010014 | (sadeleer2018effectsofcorticosteroid pages 1-3, sadeleer2018effectsofcorticosteroid pages 3-6) |
| Treatment | Corticosteroids improved physiology in non-fibrotic HP but not fibrotic HP; in non-fibrotic HP, FVC changed from -0.35%/month pre-treatment to +0.84%/month after steroid initiation (p<0.001). No survival benefit from corticosteroids was observed. | De Sadeleer et al. 2018, *Journal of Clinical Medicine* | Single-center cohort, 202 HP patients | https://doi.org/10.3390/jcm8010014 | (sadeleer2018effectsofcorticosteroid pages 1-3, sadeleer2018effectsofcorticosteroid pages 3-6) |
| Treatment | Exposure avoidance improved lung function in non-fibrotic HP: FVC trajectory changed from -0.24%/month to +0.92%/month (p=0.016), and DLCO from -0.23%/month to +0.37%/month with an immediate +4.0% increase (p=0.04). In fibrotic HP, FVC improved numerically to +0.28%/month but was not significant (p=0.15). | De Sadeleer et al. 2018, *Journal of Clinical Medicine* | Single-center cohort, exposure avoidance analysis | https://doi.org/10.3390/jcm8010014 | (sadeleer2018effectsofcorticosteroid pages 6-8) |
| Trials | Pirfenidone trial in progressive chronic HP: adults with >10% fibrosis on HRCT and absolute FVC decline >5% in prior 6 months despite conventional therapy; randomized 1:1, n=40; endpoints included FVC and 6MWD at 6 months. | NCT04675619 | Phase 2, randomized, open-label interventional trial | https://clinicaltrials.gov/study/NCT04675619 | (NCT04675619 chunk 1) |
| Trials | Pirfenidone trial in fibrotic HP: pirfenidone 2403 mg/day vs placebo for 52 weeks; primary endpoint was change in % predicted FVC at week 52; included multidisciplinary-consensus FHP, age 18-80, FVC ≥40%, DLCO ≥30%; trial terminated during COVID-19. | NCT02958917 | Phase 2, randomized, double-blind, placebo-controlled trial | https://clinicaltrials.gov/study/NCT02958917 | (NCT02958917 chunk 1, NCT02958917 chunk 2) |
| Trials | Earlier chronic HP pirfenidone study tested pirfenidone added to prednisone + azathioprine; estimated enrollment 60; primary endpoint FVC at 26 and 52 weeks, with HRCT, 6MWD, QoL, echocardiographic PASP, and oxygen desaturation as secondary outcomes. | NCT02496182 | Phase 2/3, randomized, quadruple-masked trial | https://clinicaltrials.gov/study/NCT02496182 | (NCT02496182 chunk 1, NCT02496182 chunk 2) |


*Table: This table compiles compact, high-yield recent evidence and key comparator studies relevant to bird fancier's lung/avian hypersensitivity pneumonitis. It highlights exposure patterns, diagnostic performance, prognostic markers, treatment effects, and active/interpretable clinical trial designs for rapid knowledge-base use.*

## Notes on evidence limitations
- Several knowledge-base fields (ICD/MeSH/MONDO/Orphanet identifiers; population prevalence/incidence; specific genetic variants; animal models) could not be populated with citable evidence using the retrieved document set.
- Some retrieved items are preprints (e.g., Akkurt 2024) and should be treated as non–peer-reviewed until formally published. (akkurt2024evaluationofclinical pages 1-4)


References

1. (deutsch2024doesatype pages 2-4): Kamila Deutsch, Katarzyna B. Lewandowska, Agata Kowalik, Iwona Bartoszuk, Piotr Radwan-Röhrenschef, Małgorzata Sobiecka, Małgorzata Dybowska, Witold Z. Tomkowski, and Monika Szturmowicz. Does a type of inciting antigen correlate with the presence of lung fibrosis in patients with hypersensitivity pneumonitis? Journal of Clinical Medicine, 13:5074, Aug 2024. URL: https://doi.org/10.3390/jcm13175074, doi:10.3390/jcm13175074. This article has 2 citations.

2. (akkurt2024evaluationofclinical pages 1-4): ESMA SEVIL AKKURT, BERNA AKINCI OZYUREK, KEREM ENSARIOGLU, TUGCE SAHIN OZDEMIREL, OZLEM DUVENCI BIRBEN, HAKAN ERTURK, and TUNAHAN DOLMUS. Evaluation of clinical and radiological features of patients diagnosed with hypersensitivity pneumonia. Nov 2024. URL: https://doi.org/10.21203/rs.3.rs-5418767/v1, doi:10.21203/rs.3.rs-5418767/v1.

3. (okuda2024longitudinalchangesin pages 1-2): Ryo Okuda, Tamiko Takemura, Toshihiro Misumi, Akimasa Sekine, Eri Hagiwara, and Takashi Ogura. Longitudinal changes in serum immunoglobulin g testing in patients with fibrotic avian hypersensitivity pneumonitis. BMC Pulmonary Medicine, May 2024. URL: https://doi.org/10.1186/s12890-024-03063-0, doi:10.1186/s12890-024-03063-0. This article has 0 citations and is from a peer-reviewed journal.

4. (kypreos2022impactofnumber pages 1-2): Margaret Kypreos, Kiran Batra, Craig S. Glazer, and Traci N. Adams. Impact of number and type of identified antigen on transplant-free survival in hypersensitivity pneumonitis. PLoS ONE, 17:e0273544, Sep 2022. URL: https://doi.org/10.1371/journal.pone.0273544, doi:10.1371/journal.pone.0273544. This article has 12 citations and is from a peer-reviewed journal.

5. (deutsch2024doesatype pages 9-10): Kamila Deutsch, Katarzyna B. Lewandowska, Agata Kowalik, Iwona Bartoszuk, Piotr Radwan-Röhrenschef, Małgorzata Sobiecka, Małgorzata Dybowska, Witold Z. Tomkowski, and Monika Szturmowicz. Does a type of inciting antigen correlate with the presence of lung fibrosis in patients with hypersensitivity pneumonitis? Journal of Clinical Medicine, 13:5074, Aug 2024. URL: https://doi.org/10.3390/jcm13175074, doi:10.3390/jcm13175074. This article has 2 citations.

6. (NCT02496182 chunk 1):  Pirfenidone in the Chronic Hypersensitivity Pneumonitis Treatment. Grupo Medifarma, S. A. de C. V.. 2015. ClinicalTrials.gov Identifier: NCT02496182

7. (sadeleer2018effectsofcorticosteroid pages 6-8): Laurens J. De Sadeleer, Frederik Hermans, Els De Dycker, Jonas Yserbyt, Johny A. Verschakelen, Eric K. Verbeken, Geert M. Verleden, and Wim A. Wuyts. Effects of corticosteroid treatment and antigen avoidance in a large hypersensitivity pneumonitis cohort: a single-centre cohort study. Journal of Clinical Medicine, 8:14, Dec 2018. URL: https://doi.org/10.3390/jcm8010014, doi:10.3390/jcm8010014. This article has 183 citations.

8. (sadeleer2018effectsofcorticosteroid pages 1-3): Laurens J. De Sadeleer, Frederik Hermans, Els De Dycker, Jonas Yserbyt, Johny A. Verschakelen, Eric K. Verbeken, Geert M. Verleden, and Wim A. Wuyts. Effects of corticosteroid treatment and antigen avoidance in a large hypersensitivity pneumonitis cohort: a single-centre cohort study. Journal of Clinical Medicine, 8:14, Dec 2018. URL: https://doi.org/10.3390/jcm8010014, doi:10.3390/jcm8010014. This article has 183 citations.

9. (sadeleer2018effectsofcorticosteroid pages 3-6): Laurens J. De Sadeleer, Frederik Hermans, Els De Dycker, Jonas Yserbyt, Johny A. Verschakelen, Eric K. Verbeken, Geert M. Verleden, and Wim A. Wuyts. Effects of corticosteroid treatment and antigen avoidance in a large hypersensitivity pneumonitis cohort: a single-centre cohort study. Journal of Clinical Medicine, 8:14, Dec 2018. URL: https://doi.org/10.3390/jcm8010014, doi:10.3390/jcm8010014. This article has 183 citations.

10. (intra2024theroleof pages 1-2): Jari Intra, Alice Biffi, Francesca Basta, Cristina Delfini, Nicoletta Novati, Elisa Zucchetti, Fabrizio Luppi, and Marco Casati. The role of serum igg precipitins against six typical organic antigens involved in hypersensitivity pneumonitis: a 10-year retrospective study of a referral interstitial lung disease centre. International Journal of Translational Medicine, 4:381-386, Jun 2024. URL: https://doi.org/10.3390/ijtm4020025, doi:10.3390/ijtm4020025. This article has 5 citations.

11. (intra2024theroleof pages 5-6): Jari Intra, Alice Biffi, Francesca Basta, Cristina Delfini, Nicoletta Novati, Elisa Zucchetti, Fabrizio Luppi, and Marco Casati. The role of serum igg precipitins against six typical organic antigens involved in hypersensitivity pneumonitis: a 10-year retrospective study of a referral interstitial lung disease centre. International Journal of Translational Medicine, 4:381-386, Jun 2024. URL: https://doi.org/10.3390/ijtm4020025, doi:10.3390/ijtm4020025. This article has 5 citations.

12. (okuda2024longitudinalchangesin pages 7-8): Ryo Okuda, Tamiko Takemura, Toshihiro Misumi, Akimasa Sekine, Eri Hagiwara, and Takashi Ogura. Longitudinal changes in serum immunoglobulin g testing in patients with fibrotic avian hypersensitivity pneumonitis. BMC Pulmonary Medicine, May 2024. URL: https://doi.org/10.1186/s12890-024-03063-0, doi:10.1186/s12890-024-03063-0. This article has 0 citations and is from a peer-reviewed journal.

13. (akkurt2025fibroticpatternsand pages 12-12): Esma Sevil Akkurt, Berna Akıncı Ozyurek, Kerem Ensarioglu, Tugce Sahin Ozdemirel, Ozlem Duvenci Birben, Hakan Erturk, and Tunahan Dolmus. Fibrotic patterns and diagnostic correlates in hypersensitivity pneumonitis: clinical, radiologic, and hematologic insights. Diagnostics, 15:3137, Dec 2025. URL: https://doi.org/10.3390/diagnostics15243137, doi:10.3390/diagnostics15243137. This article has 0 citations.

14. (okuda2024longitudinalchangesin pages 2-4): Ryo Okuda, Tamiko Takemura, Toshihiro Misumi, Akimasa Sekine, Eri Hagiwara, and Takashi Ogura. Longitudinal changes in serum immunoglobulin g testing in patients with fibrotic avian hypersensitivity pneumonitis. BMC Pulmonary Medicine, May 2024. URL: https://doi.org/10.1186/s12890-024-03063-0, doi:10.1186/s12890-024-03063-0. This article has 0 citations and is from a peer-reviewed journal.

15. (kypreos2022impactofnumber pages 4-5): Margaret Kypreos, Kiran Batra, Craig S. Glazer, and Traci N. Adams. Impact of number and type of identified antigen on transplant-free survival in hypersensitivity pneumonitis. PLoS ONE, 17:e0273544, Sep 2022. URL: https://doi.org/10.1371/journal.pone.0273544, doi:10.1371/journal.pone.0273544. This article has 12 citations and is from a peer-reviewed journal.

16. (kypreos2022impactofnumber pages 5-7): Margaret Kypreos, Kiran Batra, Craig S. Glazer, and Traci N. Adams. Impact of number and type of identified antigen on transplant-free survival in hypersensitivity pneumonitis. PLoS ONE, 17:e0273544, Sep 2022. URL: https://doi.org/10.1371/journal.pone.0273544, doi:10.1371/journal.pone.0273544. This article has 12 citations and is from a peer-reviewed journal.

17. (NCT02958917 chunk 1): Evans Fernandez Perez. Study of Efficacy and Safety of Pirfenidone in Patients With Fibrotic Hypersensitivity Pneumonitis. Evans Fernandez Perez. 2017. ClinicalTrials.gov Identifier: NCT02958917

18. (NCT02958917 chunk 2): Evans Fernandez Perez. Study of Efficacy and Safety of Pirfenidone in Patients With Fibrotic Hypersensitivity Pneumonitis. Evans Fernandez Perez. 2017. ClinicalTrials.gov Identifier: NCT02958917

19. (NCT04675619 chunk 1): Eman Shebl. Evaluation of the Efficacy of Pirfenidone in Progressive Chronic Hypersensitivity Pneumonitis. Zagazig University. 2019. ClinicalTrials.gov Identifier: NCT04675619

20. (intra2024theroleof pages 4-5): Jari Intra, Alice Biffi, Francesca Basta, Cristina Delfini, Nicoletta Novati, Elisa Zucchetti, Fabrizio Luppi, and Marco Casati. The role of serum igg precipitins against six typical organic antigens involved in hypersensitivity pneumonitis: a 10-year retrospective study of a referral interstitial lung disease centre. International Journal of Translational Medicine, 4:381-386, Jun 2024. URL: https://doi.org/10.3390/ijtm4020025, doi:10.3390/ijtm4020025. This article has 5 citations.

21. (NCT02496182 chunk 2):  Pirfenidone in the Chronic Hypersensitivity Pneumonitis Treatment. Grupo Medifarma, S. A. de C. V.. 2015. ClinicalTrials.gov Identifier: NCT02496182
