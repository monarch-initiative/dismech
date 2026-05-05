---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T16:49:03.195424'
end_time: '2026-05-05T17:02:14.727465'
duration_seconds: 791.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Livedoid vasculopathy
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Livedoid vasculopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Livedoid vasculopathy** covering all of the
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
- **Disease Name:** Livedoid vasculopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Livedoid vasculopathy** covering all of the
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


## Comprehensive Research Report: Livedoid Vasculopathy (LV)

### Executive summary (current understanding)
Livedoid vasculopathy (LV) is currently best understood as a **noninflammatory thrombotic/occlusive microvascular disorder of dermal vessels** that causes ischemia-driven, painful lower-extremity ulceration and scarring, rather than a primary inflammatory vasculitis. Diagnostic confirmation typically requires **clinicopathologic correlation**, because superficial sampling or sampling older lesions may be nondiagnostic. Antithrombotic therapy (LMWH or DOACs, especially rivaroxaban) is the most consistently supported treatment approach in contemporary reviews and real-world cohorts; escalation strategies include prostanoids (e.g., iloprost) and IVIG for refractory disease. (alavi2013livedoidvasculopathyan pages 1-2, alavi2013livedoidvasculopathyan pages 5-7, burg2022livedoidvasculopathy– pages 1-2, burg2022livedoidvasculopathy– media d7cd3b46)

### Evidence map (condensed)
| Domain | Key findings | Quantitative data | Evidence type | Key citation (year) |
|---|---|---|---|---|
| Definition & synonyms | Livedoid vasculopathy (LV) is a rare, chronic, relapsing **noninflammatory thrombotic/occlusive dermal vasculopathy** of the lower extremities; distinct from inflammatory vasculitis. Historical/alternative names include **livedoid vasculitis**, **segmental hyalinizing vasculitis**, **livedo reticularis with summer ulcerations**, and association with but distinction from **atrophie blanche** (a morphologic scar pattern, not a synonym for all cases). (alavi2013livedoidvasculopathyan pages 1-2, burg2022livedoidvasculopathy– pages 1-2, leeolou2023livedoidvasculopathy pages 1-3) | Rare disease; incidence commonly cited at about **1 per 100,000**. (segui2022acomprehensivereview pages 1-2) | Modified Delphi consensus, review, case review | Alavi et al., *J Am Acad Dermatol* 2013, DOI: 10.1016/j.jaad.2013.07.019; Burg et al., *Front Med* 2022, DOI: 10.3389/fmed.2022.1012178; Leeolou et al., *Dermatol Online J* 2023, DOI: 10.5070/d329562414 |
| Key clinicopathologic triad | Characteristic clinical triad: **livedo racemosa/reticular violaceous pattern + painful small punched-out ulcers + porcelain-white stellate atrophic scars (atrophie blanche)**, usually around ankles/dorsal feet/lower legs. (jatana2025livedoidvasculopathy pages 7-8, segui2022acomprehensivereview pages 2-4, burg2022livedoidvasculopathy– pages 1-2) | Livedo racemosa reported in **82%** in one multicentre cohort and **85%** in one reviewed study. (weishaupt2019characteristicsriskfactors pages 6-7, segui2022acomprehensivereview pages 2-4) | Multicentre cohort, review | Weishaupt et al., *JEADV* 2019, DOI: 10.1111/jdv.15639; Seguí & Llamas-Velasco, *Front Med* 2022, DOI: 10.3389/fmed.2022.993515 |
| Histology / biopsy | Typical biopsy shows **intraluminal fibrin thrombi/thrombosis**, **segmental hyalinization/subintimal hyaline degeneration**, **endothelial proliferation**, vessel-wall thickening, RBC extravasation, and **minimal or absent vasculitic inflammation/leukocytoclasia**. Deep biopsy including ulcer margin and adjacent skin/subcutis is recommended; multiple biopsies may be needed because lesions are segmental. (alavi2013livedoidvasculopathyan pages 5-7, burg2022livedoidvasculopathy– pages 6-8, criado2011livedoidvasculopathyas pages 4-5) | No single validated diagnostic score; biopsy often needed before systemic therapy. (burg2022livedoidvasculopathy– pages 6-8, qi2024identificationofchallenging pages 2-4) | Delphi consensus, review, retrospective study | Alavi et al., *J Am Acad Dermatol* 2013, DOI: 10.1016/j.jaad.2013.07.019; Burg et al., *Front Med* 2022, DOI: 10.3389/fmed.2022.1012178; Qi et al., *Clin Cosmet Investig Dermatol* 2024, DOI: 10.2147/CCID.S466449 |
| Epidemiology | LV is uncommon with female predominance and mainly affects adolescents to middle-aged adults, though older adults are also represented. (segui2022acomprehensivereview pages 1-2, weishaupt2019characteristicsriskfactors pages 6-7, lee2020livedoidvasculopathyin pages 5-7) | Incidence ~**1/100,000**; female:male ratio reported as **3:1** in reviews, **2.1:1** in a multicentre cohort, and **29:11** in a Korean cohort; median age **53 y** (IQR 40.5–68) in one multicentre cohort; onset age **33 y** (range 12–65) in Korean cohort. (segui2022acomprehensivereview pages 1-2, weishaupt2019characteristicsriskfactors pages 6-7, lee2020livedoidvasculopathyin pages 5-7) | Review, multicentre cohort, cohort | Seguí & Llamas-Velasco 2022, DOI: 10.3389/fmed.2022.993515; Weishaupt et al. 2019, DOI: 10.1111/jdv.15639; Lee & Cho 2020, DOI: 10.1111/jdv.16129 |
| Diagnostic delay / misdiagnosis | Diagnosis is frequently delayed and patients are commonly misdiagnosed as vasculitis or eczema-like disorders; clinicopathologic correlation is essential. (qi2024identificationofchallenging pages 2-4, evans2015successfultreatmentof pages 2-2) | Mean diagnostic delay about **5 years** in reviews; **4.61 ± 0.69 years** in a 2024 retrospective study; **85.18% (23/27)** had an alternate prior diagnosis and **73.9% (17/23)** of delayed cases had been labeled allergic vasculitis. (segui2022acomprehensivereview pages 1-2, qi2024identificationofchallenging pages 2-4) | Review, retrospective cohort | Qi et al., *Clin Cosmet Investig Dermatol* 2024, DOI: 10.2147/CCID.S466449; Seguí & Llamas-Velasco 2022, DOI: 10.3389/fmed.2022.993515 |
| Risk factors / associations: thrombophilia | LV is associated with inherited/acquired prothrombotic states including **Factor V Leiden**, **prothrombin G20210A**, **protein C/S or antithrombin abnormalities**, **antiphospholipid antibodies**, **hyperhomocysteinemia**, **lipoprotein(a)** elevation, and **PAI-1/SERPINE1-related impaired fibrinolysis**. (criado2011livedoidvasculopathyas pages 2-3, segui2022acomprehensivereview pages 1-2, gao2020plasminogenactivatorinhibitor‐1 pages 1-3) | Abnormal procoagulant parameters in **44% (11/25)** in one cohort and **42.5% (17/40)** in a Korean cohort; prospective series **52% (18/34)** with thrombophilia; antiphospholipid antibodies **17.64%**, Factor V Leiden **17.64%**, protein C/S deficiency **8.82%** in one series; homocysteine elevated in **10/12 (83%)** and lipoprotein(a) in **5/12 (42%)** in a multicentre cohort. (weishaupt2019characteristicsriskfactors pages 2-4, lee2020livedoidvasculopathyin pages 5-7, segui2022acomprehensivereview pages 1-2) | Cohort, review | Weishaupt et al. 2019, DOI: 10.1111/jdv.15639; Lee & Cho 2020, DOI: 10.1111/jdv.16129; Seguí & Llamas-Velasco 2022, DOI: 10.3389/fmed.2022.993515; Criado et al. 2011, DOI: 10.1016/j.autrev.2010.11.008 |
| Risk factors / associations: PAI-1 and fibrinolysis | Impaired fibrinolysis is a leading mechanistic model. **PAI-1/SERPINE1** overexpression and promoter polymorphisms (especially **4G/5G**, sometimes **4G/4G**) have been repeatedly reported; PAI-1 localizes to lesional extracellular matrix/perivascular tissue. (agirbasli2011enhancedfunctionalstability pages 4-5, gao2020plasminogenactivatorinhibitor‐1 pages 1-3, agirbasli2011enhancedfunctionalstability pages 2-4) | In 20 biopsy-proven LV cases, median PAI-1 antigen **34 vs 17 ng/mL** in controls (**P < 0.01**); residual PAI-1 activity after 16 h was detectable in LV but absent in controls, indicating markedly enhanced stability. PAI-1 4G/5G genotype distribution: **20% 5G/5G, 55% 4G/5G, 25% 4G/4G** in that cohort; a systematic review cited **PAI-1 675 4G/5G in 85.26%** of reported genetically studied cases. (agirbasli2011enhancedfunctionalstability pages 2-4, segui2022acomprehensivereview pages 1-2) | Case-control mechanistic study, review | Agirbasli et al., *J Thromb Thrombolysis* 2011, DOI: 10.1007/s11239-011-0556-y; Gao & Jin, *Int Wound J* 2020, DOI: 10.1111/iwj.13480; Seguí & Llamas-Velasco 2022, DOI: 10.3389/fmed.2022.993515 |
| Risk factors / associations: comorbidities | Reported associated conditions include autoimmune/connective tissue disease, cryoglobulinemia, venous insufficiency, polycythemia vera, and thromboembolic events; hypertension and elevated BMI are common in adult cohorts. (weishaupt2019characteristicsriskfactors pages 6-7, lee2020livedoidvasculopathyin pages 5-7, burg2022livedoidvasculopathy– pages 1-2) | Hypertension in **70%** and elevated BMI in about **40%** of one multicentre cohort; deep vein thrombosis in **11% (3/27)**; venous insufficiency **7.5% (3/40)** and polycythemia vera **2.5% (1/40)** in a Korean cohort. (weishaupt2019characteristicsriskfactors pages 6-7, weishaupt2019characteristicsriskfactors pages 2-4, lee2020livedoidvasculopathyin pages 5-7) | Multicentre cohort, cohort | Weishaupt et al. 2019, DOI: 10.1111/jdv.15639; Lee & Cho 2020, DOI: 10.1111/jdv.16129 |
| First-line treatment: anticoagulation / DOACs | Best-supported current therapy is **anticoagulation**, especially **rivaroxaban** or LMWH; antiplatelets and supportive wound/pain care are often adjunctive. Reviews and algorithms place **LMWH/DOACs as first-line**, with escalation to iloprost or IVIG for refractory disease. (burg2022livedoidvasculopathy– pages 1-2, burg2022livedoidvasculopathy– media d7cd3b46, leeolou2023livedoidvasculopathy pages 1-3) | In a phase 2a single-arm rivaroxaban study of **25 patients**, **95%** had clinically significant pain reduction; **44%** had confirmed hypercoagulability abnormalities, with no apparent efficacy difference by thrombophilia status. In a review of **73 patients**, **82.2% (60/73)** improved on rivaroxaban. (leeolou2023livedoidvasculopathy pages 3-4) | Phase 2a single-arm trial; review/case aggregation | Leeolou et al. 2023 summarizing RILIVA and pooled data, DOI: 10.5070/d329562414; Burg et al. 2022, DOI: 10.3389/fmed.2022.1012178 |
| Real-world treatment effectiveness | In practice, anticoagulants outperform anti-inflammatory regimens; steroids are commonly tried before diagnosis but often ineffective. (weishaupt2019characteristicsriskfactors pages 1-2, qi2024identificationofchallenging pages 2-4) | In multicentre prestudy treatment data, **heparin** was rated good/very good in **12/17 (71%)**; **rivaroxaban 2/2 (100%)** in a very small subset; NSAIDs **1/9 (11%)**; anti-inflammatory regimens had **0/17** effectiveness among exposed patients. Before final diagnosis, **65.21%** received systemic corticosteroids in one 2024 cohort. (weishaupt2019characteristicsriskfactors pages 4-5, qi2024identificationofchallenging pages 2-4) | Multicentre cohort; retrospective cohort | Weishaupt et al. 2019, DOI: 10.1111/jdv.15639; Qi et al. 2024, DOI: 10.2147/CCID.S466449 |
| IVIG and refractory-disease options | **IVIG** is commonly used for refractory LV, especially with severe pain or neuropathy; case-series/systematic-review evidence suggests benefit, but high-quality comparative trials are lacking. Hyperbaric oxygen, TNF inhibitors, JAK inhibitors, sulodexide, and prostanoids/iloprost are reported for difficult cases. (palanisamy2023painmanagementoptions pages 3-3, jatana2025livedoidvasculopathy pages 7-8, ramphall2022comparativeefficacyof pages 9-9) | Quantitative IVIG efficacy figures were not provided in the available excerpts; anti-TNF evidence includes **34.3% pain reduction after 12 weeks** with etanercept in a cited report. A hyperbaric oxygen study enrolled **12** patients with active idiopathic LV (details not extracted here). (palanisamy2023painmanagementoptions pages 3-3) | Systematic review, case series, case reports | Palanisamy et al., *EJCRIM* 2023, DOI: 10.12890/2023_003727; Ramphall et al., *Cureus* 2022, DOI: 10.7759/cureus.28485; Juan et al., *Br J Dermatol* 2006, DOI: 10.1111/j.1365-2133.2005.06843.x |
| Supportive care / implementation | Across reviews and algorithms, management should also include **wound care, pain control, smoking cessation, compression (after excluding significant arterial disease), and cardiovascular risk modification**. (jatana2025livedoidvasculopathy pages 7-8, alavi2013livedoidvasculopathyan pages 5-7, burg2022livedoidvasculopathy– pages 1-2) | Compression should be considered only after arterial disease exclusion (e.g., ABPI/toe pressures); no standardized outcome percentages available in the excerpts. (alavi2013livedoidvasculopathyan pages 5-7) | Consensus/review | Alavi et al. 2013, DOI: 10.1016/j.jaad.2013.07.019; Burg et al. 2022, DOI: 10.3389/fmed.2022.1012178 |


*Table: This table condenses the most clinically useful disease-characterization data for livedoid vasculopathy, including definitions, pathology, epidemiology, risk associations, and treatment outcomes. It is useful as a quick evidence map for knowledge-base curation and clinical reference.*

---

## 1. Disease information

### 1.1 Definition and overview
A widely cited international modified-Delphi analysis characterizes LV as a **“noninflammatory thrombotic condition”** presenting with chronic recurrent reticulated purpura of the legs, painful ulcers (classically around ankles/dorsal feet), and stellate porcelain-white scars. (alavi2013livedoidvasculopathyan pages 1-2)

A 2023 peer-reviewed clinical review similarly defines LV as a rare, painful **thrombo-occlusive vascular disorder** with spontaneous thrombosis in medium-sized arterioles causing local hypoxia and skin ulceration. (leeolou2023livedoidvasculopathy pages 1-3)

### 1.2 Synonyms and alternative names
Synonyms/related terms used in the literature include **livedoid vasculitis**, **segmental hyalinizing vasculitis**, and older usage conflating LV with **atrophie blanche**; however, atrophie blanche is now emphasized as a **morphologic healing pattern** rather than a disease-specific synonym. (alavi2013livedoidvasculopathyan pages 1-2, evans2015successfultreatmentof pages 2-2, jatana2025livedoidvasculopathy pages 7-8)

### 1.3 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)
Within the retrieved full-text corpus for this run, I could not extract authoritative mappings to **MONDO, Orphanet, ICD-10/ICD-11, OMIM, or MeSH IDs** for LV without risking incorrect identifier assignment. This element remains **not available from the provided evidence set**.

### 1.4 Evidence provenance (individual patients vs aggregated resources)
Much of the therapeutic knowledge base remains derived from **case reports/series** and **single-arm cohorts**, reflecting disease rarity. The 2024 diagnostic-delay study and multicenter cohorts provide more aggregated evidence on diagnostic pitfalls and associated risk factors. (qi2024identificationofchallenging pages 2-4, weishaupt2019characteristicsriskfactors pages 6-7)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic framing)
The prevailing model is that LV arises from **microvascular thrombosis and impaired fibrinolysis** in dermal vessels, leading to focal ischemia, ulceration, and scarring. Histology and treatment response patterns support a **procoagulant/prothrombotic** pathogenesis rather than immune-complex vasculitis as the primary driver. (alavi2013livedoidvasculopathyan pages 1-2, criado2011livedoidvasculopathyas pages 4-5, leeolou2023livedoidvasculopathy pages 1-3)

### 2.2 Risk factors

#### 2.2.1 Thrombophilia and hypercoagulability
A 2019 multicentre cohort analysis (derived from a phase IIa rivaroxaban study cohort) reported **prothrombotic abnormalities in 44% (11/25)**, with notably high rates among those tested for specific markers: **elevated homocysteine 10/12 (83%)** and **elevated lipoprotein(a) 5/12 (42%)**. (weishaupt2019characteristicsriskfactors pages 2-4)

A Korean cohort of 40 patients reported **coagulation laboratory abnormalities in 42.5%** (17/40). (lee2020livedoidvasculopathyin pages 5-7)

A 2011 synthesis emphasized frequent associations reported across case series with antiphospholipid antibodies, Factor V Leiden, prothrombin G20210A, MTHFR-related hyperhomocysteinemia, and protein C/S/antithrombin abnormalities. (criado2011livedoidvasculopathyas pages 2-3)

#### 2.2.2 Cardiometabolic and vascular comorbidities
The multicentre analysis reported **hypertension in 70%** and elevated BMI in ~**40%** (11/27) of participants, highlighting frequent coexistence of cardiovascular risk factors in adult cohorts. (weishaupt2019characteristicsriskfactors pages 2-4, weishaupt2019characteristicsriskfactors pages 6-7)

#### 2.2.3 Smoking
A ClinicalTrials.gov observational study explicitly designed to test whether LV has a **“Strong Association With Smoking”** (NCT05878327) compared smoking history and cardiovascular risk factors against the Swiss general population, with secondary thrombophilia screening. However, the registry excerpt provides design/aims rather than quantitative results. (NCT05878327 chunk 1)

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
Direct evidence of gene–environment interaction (e.g., specific variant × smoking effect modification) was not present in the retrieved full-text corpus.

---

## 3. Phenotypes

### 3.1 Core cutaneous phenotype (symptoms/signs)
The canonical clinical triad is:
1) **Livedo racemosa** (persistent, broken, branched violaceous pattern),
2) **Very painful small punched-out ulcers** (often <1 cm),
3) **Porcelain-white atrophic scars (atrophie blanche)** after healing. (jatana2025livedoidvasculopathy pages 7-8, segui2022acomprehensivereview pages 2-4, burg2022livedoidvasculopathy– pages 1-2)

Frequency examples:
- Livedo racemosa ~**82%** in a multicentre cohort. (weishaupt2019characteristicsriskfactors pages 6-7)
- In one reviewed study, livedo racemosa was reported in **85%**. (segui2022acomprehensivereview pages 2-4)

Distribution examples:
- Korean cohort: ankle **84.2%**, leg **65.8%**, foot **42.1%**, upper extremities **7.9%**, with **97.4%** bilaterality. (lee2020livedoidvasculopathyin pages 5-7)

### 3.2 Extracutaneous involvement
Extracutaneous involvement was noted in **13.2%** (5/38) in the Korean cohort excerpt. (lee2020livedoidvasculopathyin pages 5-7)

A diagnostic review notes thrombus formation can involve **vasa nervorum**, providing a mechanistic basis for neuropathic symptoms in some patients. (burg2022livedoidvasculopathy– pages 6-8)

### 3.3 Natural history and temporal course
LV is typically **chronic** and **relapsing**, with substantial diagnostic delay. Review-level estimates cite mean diagnostic delay around **5 years**, and a 2024 retrospective cohort reported mean time from onset to final diagnosis of **4.61 ± 0.69 years**. (segui2022acomprehensivereview pages 1-2, qi2024identificationofchallenging pages 2-4)

### 3.4 Quality-of-life impact
LV is repeatedly described as painful and functionally limiting; one recent clinical review explicitly notes its negative quality-of-life impact (painful ulcers, recurring lesions, scarring). Although QoL instruments (e.g., DLQI, SF-36) were not extractable from this evidence set, cohort descriptions and pain-focused reports emphasize severe pain burden and treatment-refractory pain in some cases. (leeolou2023livedoidvasculopathy pages 1-3, palanisamy2023painmanagementoptions pages 3-3)

### 3.5 Suggested HPO terms (non-exhaustive)
- Livedo racemosa / livedo reticularis-like pattern: **HP:0001001 (Livedo reticularis)** (closest commonly used HPO term)
- Cutaneous ulceration: **HP:0001059 (Cutaneous ulcer)**
- Lower limb pain: **HP:0003418 (Leg pain)** or **HP:0012531 (Pain)**
- Atrophie blanche / atrophic scarring: **HP:0001074 (Scar)** / **HP:0100699 (Atrophic scar)** (depending on preferred granularity)
- Purpura/retiform purpura: **HP:0000979 (Purpura)**
- Peripheral neuropathy (subset): **HP:0009830 (Peripheral neuropathy)**

(These HPO suggestions are ontology mappings; the clinical features are evidence-supported above.)

---

## 4. Genetic / molecular information

### 4.1 Disease architecture
Available evidence supports LV as largely **multifactorial/association-based**, frequently linked to thrombophilia and impaired fibrinolysis, rather than a single-gene Mendelian disorder. (alavi2013livedoidvasculopathyan pages 1-2, segui2022acomprehensivereview pages 1-2)

### 4.2 Candidate/associated genes and variants (reported)
Commonly reported thrombophilia-related genes/variants include:
- **SERPINE1 (PAI-1)** promoter **4G/5G** polymorphism; reviews cite high prevalence among genetically studied cases (e.g., **PAI-1 675 4G/5G in 85.26%** in one systematic review summarized in a 2022 review). (segui2022acomprehensivereview pages 1-2)
- **MTHFR** polymorphisms (C677T, A1298C) and hyperhomocysteinemia associations. (gao2020plasminogenactivatorinhibitor‐1 pages 1-3, segui2022acomprehensivereview pages 1-2)
- **F5 (Factor V Leiden / G1691A)** and **F2 (Prothrombin G20210A)**. (criado2011livedoidvasculopathyas pages 2-3, segui2022acomprehensivereview pages 1-2)
- Natural anticoagulant pathways: protein C/S and antithrombin abnormalities. (weishaupt2019characteristicsriskfactors pages 2-4, criado2011livedoidvasculopathyas pages 2-3)

ClinicalTrials.gov genetic association study (Taiwan) explicitly targeted Factor V Leiden, Prothrombin G20210A, PAI promoter 4G/4G, and MTHFR C677T in “livedo vasculitis” patients with LV-like clinicopathology and histology (fibrin deposition). (NCT00975871 chunk 1)

### 4.3 Functional consequences and mechanistic molecular data (PAI-1)
A mechanistic case-control study of 20 biopsy-proven LV patients reported increased antifibrinolytic signal:
- Median **PAI-1 antigen 34 vs 17 ng/mL** in controls (**P < 0.01**), and detectable residual PAI-1 activity after 16 h in patients but not controls, suggesting substantially enhanced functional stability. (agirbasli2011enhancedfunctionalstability pages 2-4)
This supports the concept that LV may involve **suppressed plasmin generation** (via PAI-1 inhibition of tPA/uPA), promoting persistent fibrin-rich microthrombi. (agirbasli2011enhancedfunctionalstability pages 2-4, gao2020plasminogenactivatorinhibitor‐1 pages 1-3)

### 4.4 ClinVar / ACMG classification
ClinVar-based pathogenicity classifications and population allele frequencies (e.g., gnomAD) were **not available from the retrieved evidence set** in this run.

---

## 5. Environmental information

### 5.1 Environmental/lifestyle factors
Direct quantitative evidence on environmental exposures was limited in the retrieved literature. Smoking has been hypothesized as important enough to motivate an observational study (NCT05878327), but results were not provided in the excerpt. (NCT05878327 chunk 1)

### 5.2 Infectious agents
No infectious agent was identified as a primary trigger in the retrieved evidence set.

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (upstream → downstream)
**Upstream drivers** (heterogeneous across patients):
- Hypercoagulability and thrombophilia (inherited/acquired). (weishaupt2019characteristicsriskfactors pages 2-4, criado2011livedoidvasculopathyas pages 2-3)
- Impaired fibrinolysis (PAI-1/SERPINE1 elevation and/or functional stabilization). (agirbasli2011enhancedfunctionalstability pages 2-4, gao2020plasminogenactivatorinhibitor‐1 pages 1-3)
- Endothelial injury/dysfunction (proposed in reviews) and rheological disturbances (e.g., cryoglobulins). (jatana2025livedoidvasculopathy pages 7-8, weishaupt2019characteristicsriskfactors pages 2-4)

**Intermediate steps**:
- Segmental dermal vessel thrombosis with fibrin deposition and subintimal hyalinization/endothelial proliferation. (alavi2013livedoidvasculopathyan pages 5-7, criado2011livedoidvasculopathyas pages 4-5)

**Downstream manifestations**:
- Cutaneous ischemia/hypoxia → painful purpura/retiform lesions → small punched-out ulcerations → atrophie blanche scarring. (alavi2013livedoidvasculopathyan pages 1-2, segui2022acomprehensivereview pages 2-4)

### 6.2 Immune involvement
Although LV is framed as noninflammatory, direct immunofluorescence may show fibrin (early) and Ig/complement deposition (later) without necessarily implying primary immune-complex vasculitis; slight perivascular leukocytes and absence of leukocytoclasia help distinguish from leukocytoclastic vasculitis. (alavi2013livedoidvasculopathyan pages 5-7, burg2022livedoidvasculopathy– pages 1-2, criado2011livedoidvasculopathyas pages 4-5)

### 6.3 Suggested GO biological process terms (illustrative)
- **Blood coagulation** (GO:0007596)
- **Fibrinolysis** (GO:0042730)
- **Platelet activation** (GO:0030168)
- **Response to hypoxia** (GO:0001666)
- **Wound healing** (GO:0042060)

### 6.4 Suggested Cell Ontology (CL) cell types
- **Endothelial cell** (CL:0000115)
- **Platelet** (CL:0000233)
- **Perivascular macrophage / macrophage** (CL:0000235) (for inflammatory/repair context)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
LV primarily affects skin microvasculature of the **lower extremities** (malleolar region, dorsal foot, lower legs). (segui2022acomprehensivereview pages 2-4, lee2020livedoidvasculopathyin pages 5-7)

### 7.2 Tissue/cell level
- **Dermal small vessels / superficial-to-mid dermis microvasculature** are key sites of thrombosis and hyalinization. (burg2022livedoidvasculopathy– pages 6-8, criado2011livedoidvasculopathyas pages 4-5)
- In some cases, involvement of **vasa nervorum** is discussed as a mechanism for neuropathic symptoms. (burg2022livedoidvasculopathy– pages 6-8)

### 7.3 Suggested UBERON terms (illustrative)
- Skin of lower limb: **UBERON:0004263 (skin of lower limb)**
- Dermis: **UBERON:0002067 (dermis)**
- Lower leg: **UBERON:0000979 (lower leg)**
- Ankle region: **UBERON:0001488 (ankle)**

---

## 8. Temporal development

### 8.1 Onset
Onset spans adolescence through older adulthood. Example cohort data:
- Korean cohort onset central measure **33 years** (range 12–65). (lee2020livedoidvasculopathyin pages 5-7)
- Multicentre cohort median age **53 years** (IQR 40.5–68). (weishaupt2019characteristicsriskfactors pages 2-4)

### 8.2 Progression/course
LV generally follows a **chronic, relapsing** course, with recurrent ulcer episodes and residual scarring. (alavi2013livedoidvasculopathyan pages 1-2, leeolou2023livedoidvasculopathy pages 1-3)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Review-level estimates commonly cite incidence around **1 per 100,000** with **female predominance** (e.g., 3:1). (segui2022acomprehensivereview pages 1-2)

Multicentre and national cohorts show variable but consistent female predominance:
- Female:male ≈ **2.1:1** in a multicentre cohort. (weishaupt2019characteristicsriskfactors pages 6-7)
- Korean cohort: **29 female / 11 male**. (lee2020livedoidvasculopathyin pages 5-7)

### 9.2 Genetic etiology and inheritance pattern
No evidence supports a single Mendelian inheritance for LV overall; rather, it is linked to **susceptibility variants and acquired thrombophilic states**. (segui2022acomprehensivereview pages 1-2, criado2011livedoidvasculopathyas pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical features supporting diagnosis
Typical presentation includes painful retiform purpura/livedo racemosa with recurrent small ulcers in the lower legs/ankles/feet and atrophie blanche scarring. (alavi2013livedoidvasculopathyan pages 1-2, segui2022acomprehensivereview pages 2-4)

### 10.2 Biopsy / histopathology (key diagnostic test)
Core histopathologic features:
- **Intraluminal thrombosis/fibrin thrombi**
- **Endothelial proliferation**
- **Subintimal hyaline degeneration / segmental hyalinization**
with minimal inflammation. (alavi2013livedoidvasculopathyan pages 5-7, criado2011livedoidvasculopathyas pages 4-5)

Biopsy technique (consensus and expert guidance):
- Modified-Delphi recommendations emphasize a **deep 4–6 mm excisional or punch biopsy down to fascia**, including ulcer margin, adjacent healthy skin, and lower subcutis, because disease is segmental and classic changes can be missed. (alavi2013livedoidvasculopathyan pages 5-7)
- Practical diagnostic review recommends avoiding direct ulcer sampling and using deep excision (especially early/active lesions) to exclude deeper vasculitides (e.g., cutaneous PAN). (burg2022livedoidvasculopathy– pages 6-8)

### 10.3 Laboratory workup
Consensus and cohort literature supports targeted evaluation for hypercoagulable/fibrinolytic disorders and autoimmune/paraproteinemia screening as clinically indicated; however, thrombophilia testing may not always change therapy but may assist counseling or identify treatable hyperhomocysteinemia. (alavi2013livedoidvasculopathyan pages 5-7)

### 10.4 Diagnostic pitfalls and differential diagnosis
Misdiagnosis is common:
- 2024 retrospective cohort: **85.18%** had alternate diagnoses before final LV diagnosis; allergic vasculitis was common. (qi2024identificationofchallenging pages 2-4)

Differential diagnosis includes pyoderma gangrenosum, factitial dermatitis, cutaneous polyarteritis nodosa, leukocytoclastic vasculitis, pseudo-Kaposi sarcoma, Degos disease and chronic venous stasis. (jatana2025livedoidvasculopathy pages 7-8)

---

## 11. Outcome / prognosis

### 11.1 Morbidity
Morbidity is dominated by chronic pain, recurrent ulceration, and irreversible scarring. (leeolou2023livedoidvasculopathy pages 1-3, alavi2013livedoidvasculopathyan pages 1-2)

### 11.2 Thromboembolic complications
A multicentre cohort reported deep vein thrombosis in **11% (3/27)**, higher than general population estimates cited by the authors. (weishaupt2019characteristicsriskfactors pages 6-7)

### 11.3 Mortality/survival
No survival or mortality rates were available in the retrieved evidence set; LV is primarily a morbidity-driven dermatologic microvascular disorder.

---

## 12. Treatment

### 12.1 Treatment principles (real-world implementation)
Across consensus/reviews and multicentre cohorts, treatment typically combines:
- **Pain control**
- **Wound care** and infection prevention
- **Compression** only after excluding significant arterial disease (e.g., ABPI/toe pressures)
- **Risk-factor modification** (cardiovascular risks; smoking cessation commonly recommended)
- **Antithrombotic therapy** (anticoagulation ± antiplatelets). (alavi2013livedoidvasculopathyan pages 5-7, jatana2025livedoidvasculopathy pages 7-8)

### 12.2 Anticoagulation (first-line) and DOACs
A 2023 clinical review summarizes evidence that a multicentre single-arm phase 2a study of **25 patients** treated with rivaroxaban showed **clinically significant pain reduction across 95%** of participants, with similar benefit whether or not a known prothrombotic state was present (44% had confirmed hypercoagulability abnormalities). (leeolou2023livedoidvasculopathy pages 3-4)

The same source summarizes a review of **73 patients** with LV in which **82.2% (60/73)** improved with rivaroxaban. (leeolou2023livedoidvasculopathy pages 3-4)

Case-report evidence demonstrates sustained remission on rivaroxaban in recalcitrant LV, including complete healing and absence of new ulcers over months in individual patients. (evans2015successfultreatmentof pages 2-2)

### 12.3 Real-world comparative effectiveness signals
In a multicentre analysis of treatment reality:
- **Heparin** was rated good/very good by patients in **12/17 (71%)**.
- Anti-inflammatory regimens were frequently used but had **0/17** effectiveness among exposed patients.
These findings support anticoagulation as a pragmatic first-line approach. (weishaupt2019characteristicsriskfactors pages 4-5, weishaupt2019characteristicsriskfactors pages 1-2)

### 12.4 IVIG and escalation options
IVIG is commonly cited for refractory LV (especially severe pain/neuropathy), supported by systematic reviews and case series rather than large randomized trials. (palanisamy2023painmanagementoptions pages 3-3, jatana2025livedoidvasculopathy pages 7-8)

### 12.5 Treatment algorithm (expert/authoritative synthesis)
Burg et al. (Frontiers in Medicine, 2022) provide a structured algorithm placing **LMWH/DOACs as first-line**, **iloprost as second-line**, and **IVIG as third-line** escalation, with additional options discussed for refractory disease. (burg2022livedoidvasculopathy– media d7cd3b46)

### 12.6 Other treatments (selected)
- Anti-TNF agents have reported pain benefits in refractory LV (e.g., etanercept with **34.3% pain reduction after 12 weeks** in cited data summarized in a 2023 report). (palanisamy2023painmanagementoptions pages 3-3)
- Hyperbaric oxygen therapy is described as adjunctive/rescue therapy in case series and longer-term follow-up studies, generally in refractory ulceration contexts; robust comparative efficacy data were not extractable from the present evidence set. (palanisamy2023painmanagementoptions pages 3-3)

### 12.7 Suggested MAXO terms (illustrative)
- Anticoagulation therapy: **MAXO:0001020 (anticoagulant therapy)** (or nearest available MAXO anticoagulation term)
- Intravenous immunoglobulin therapy: **MAXO:0000734 (intravenous immunoglobulin therapy)**
- Wound care: **MAXO:0000462 (wound care)**
- Hyperbaric oxygen therapy: **MAXO:0000444 (hyperbaric oxygen therapy)**

---

## 13. Prevention
Primary prevention strategies are not well-defined due to uncertain causality; pragmatic prevention focuses on:
- Managing cardiovascular risk factors
- Smoking cessation
- Preventing ulcer recurrence via maintaining adequate anticoagulation in responsive patients
Evidence in this set is largely inferential from risk-factor associations and treatment response patterns rather than prevention trials. (weishaupt2019characteristicsriskfactors pages 2-4, jatana2025livedoidvasculopathy pages 7-8)

---

## 14. Other species / natural disease
No naturally occurring LV analog in non-human species was identified in the retrieved evidence set.

---

## 15. Model organisms
No established LV-specific animal model was identified in the retrieved evidence set. Mechanistic inference is sometimes supported by broader PAI-1 biology and thrombosis/fibrosis models, but LV-specific model organism resources were not captured here. (agirbasli2011enhancedfunctionalstability pages 4-5)

---

## Recent developments (2023–2024 prioritized)

### Diagnostic delay and misdiagnosis patterns (2024)
A 2024 retrospective cohort (Peking Union Medical College Hospital; publication Aug 2024) quantified a prolonged diagnostic delay (mean **4.61 ± 0.69 years**) and high misdiagnosis burden (**85.18%** with alternate prior diagnoses; allergic vasculitis common), supporting current emphasis on early biopsy and clinicopathologic correlation. URL: https://doi.org/10.2147/CCID.S466449 (published 2024-08). (qi2024identificationofchallenging pages 2-4)

### Ongoing/registered research programs (ClinicalTrials.gov)
- **NCT05878327** (completed; primary completion 2015) was designed to compare smoking prevalence and cardiovascular risk factors against the Swiss general population, with secondary thrombophilia testing. URL: https://clinicaltrials.gov/study/NCT05878327 (registry record excerpt). (NCT05878327 chunk 1)
- **NCT00975871** (completed; completion Apr 2009) evaluated thrombophilia-related polymorphisms (Factor V Leiden, Prothrombin G20210A, PAI 4G/4G, MTHFR C677T) in Taiwanese patients with livedo vasculitis/LV-like clinicopathology. URL: https://clinicaltrials.gov/study/NCT00975871 (registry record excerpt). (NCT00975871 chunk 1)

### Treatment practice consolidation
Contemporary reviews and algorithms continue to consolidate **anticoagulation-first** management, with escalation to iloprost/IVIG, reflecting convergence of cohort outcomes and expert opinion despite limited randomized trial evidence. (burg2022livedoidvasculopathy– media d7cd3b46, weishaupt2019characteristicsriskfactors pages 1-2)

---

## Notes on evidence limitations
- High-quality randomized comparative trials remain scarce; many treatment claims derive from single-arm cohorts and case series. (weishaupt2019characteristicsriskfactors pages 1-2, leeolou2023livedoidvasculopathy pages 3-4)
- Identifier mapping (MONDO/Orphanet/ICD/MeSH) and ClinVar-level variant annotation were not available in the retrieved corpus for this run.
- Smoking association is suggested by trial registry aims but quantitative effect estimates were not captured in available evidence.


References

1. (alavi2013livedoidvasculopathyan pages 1-2): Afsaneh Alavi, Jürg Hafner, Jan P. Dutz, Dieter Mayer, R. Gary Sibbald, Paulo Ricardo Criado, Patricia Senet, Jeffery P. Callen, Tania J. Phillips, Marco Romanelli, and Robert S. Kirsner. Livedoid vasculopathy: an in-depth analysis using a modified delphi approach. Journal of the American Academy of Dermatology, 69 6:1033-1042.e1, Dec 2013. URL: https://doi.org/10.1016/j.jaad.2013.07.019, doi:10.1016/j.jaad.2013.07.019. This article has 159 citations and is from a domain leading peer-reviewed journal.

2. (alavi2013livedoidvasculopathyan pages 5-7): Afsaneh Alavi, Jürg Hafner, Jan P. Dutz, Dieter Mayer, R. Gary Sibbald, Paulo Ricardo Criado, Patricia Senet, Jeffery P. Callen, Tania J. Phillips, Marco Romanelli, and Robert S. Kirsner. Livedoid vasculopathy: an in-depth analysis using a modified delphi approach. Journal of the American Academy of Dermatology, 69 6:1033-1042.e1, Dec 2013. URL: https://doi.org/10.1016/j.jaad.2013.07.019, doi:10.1016/j.jaad.2013.07.019. This article has 159 citations and is from a domain leading peer-reviewed journal.

3. (burg2022livedoidvasculopathy– pages 1-2): Maria Rosa Burg, Carolin Mitschang, Tobias Goerge, and Stefan Werner Schneider. Livedoid vasculopathy – a diagnostic and therapeutic challenge. Frontiers in Medicine, Oct 2022. URL: https://doi.org/10.3389/fmed.2022.1012178, doi:10.3389/fmed.2022.1012178. This article has 33 citations.

4. (burg2022livedoidvasculopathy– media d7cd3b46): Maria Rosa Burg, Carolin Mitschang, Tobias Goerge, and Stefan Werner Schneider. Livedoid vasculopathy – a diagnostic and therapeutic challenge. Frontiers in Medicine, Oct 2022. URL: https://doi.org/10.3389/fmed.2022.1012178, doi:10.3389/fmed.2022.1012178. This article has 33 citations.

5. (leeolou2023livedoidvasculopathy pages 1-3): Melissa C. Leeolou, Kerri E Rieger, and Jennifer E Yeh. Livedoid vasculopathy. Dermatology Online Journal, Nov 2023. URL: https://doi.org/10.5070/d329562414, doi:10.5070/d329562414. This article has 4 citations and is from a peer-reviewed journal.

6. (segui2022acomprehensivereview pages 1-2): Mireia Seguí and Mar Llamas-Velasco. A comprehensive review on pathogenesis, associations, clinical findings, and treatment of livedoid vasculopathy. Frontiers in Medicine, Dec 2022. URL: https://doi.org/10.3389/fmed.2022.993515, doi:10.3389/fmed.2022.993515. This article has 21 citations.

7. (jatana2025livedoidvasculopathy pages 7-8): Gurpoonam Jatana. Livedoid vasculopathy. Journal of Dermatology Research, Mar 2025. URL: https://doi.org/10.46889/jdr.2025.6107, doi:10.46889/jdr.2025.6107. This article has 2 citations.

8. (segui2022acomprehensivereview pages 2-4): Mireia Seguí and Mar Llamas-Velasco. A comprehensive review on pathogenesis, associations, clinical findings, and treatment of livedoid vasculopathy. Frontiers in Medicine, Dec 2022. URL: https://doi.org/10.3389/fmed.2022.993515, doi:10.3389/fmed.2022.993515. This article has 21 citations.

9. (weishaupt2019characteristicsriskfactors pages 6-7): C. Weishaupt, A. Strölin, B. Kahle, A. Kreuter, S. W. Schneider, J. Gerss, M. Eveslage, A. Drabik, and T. Goerge. Characteristics, risk factors and treatment reality in livedoid vasculopathy – a multicentre analysis. Journal of the European Academy of Dermatology and Venereology, 33:1784-1791, Sep 2019. URL: https://doi.org/10.1111/jdv.15639, doi:10.1111/jdv.15639. This article has 71 citations and is from a domain leading peer-reviewed journal.

10. (burg2022livedoidvasculopathy– pages 6-8): Maria Rosa Burg, Carolin Mitschang, Tobias Goerge, and Stefan Werner Schneider. Livedoid vasculopathy – a diagnostic and therapeutic challenge. Frontiers in Medicine, Oct 2022. URL: https://doi.org/10.3389/fmed.2022.1012178, doi:10.3389/fmed.2022.1012178. This article has 33 citations.

11. (criado2011livedoidvasculopathyas pages 4-5): Paulo Ricardo Criado, Evandro Ararigboia Rivitti, Mirian Nacagami Sotto, and Jozélio Freire de Carvalho. Livedoid vasculopathy as a coagulation disorder. Autoimmunity reviews, 10 6:353-60, Apr 2011. URL: https://doi.org/10.1016/j.autrev.2010.11.008, doi:10.1016/j.autrev.2010.11.008. This article has 107 citations and is from a peer-reviewed journal.

12. (qi2024identificationofchallenging pages 2-4): Fei Qi, Yimeng Gao, and Hongzhong Jin. Identification of challenging diagnostic factors in livedoid vasculopathy: a retrospective study. Clinical, Cosmetic and Investigational Dermatology, 17:1747-1756, Aug 2024. URL: https://doi.org/10.2147/ccid.s466449, doi:10.2147/ccid.s466449. This article has 3 citations and is from a peer-reviewed journal.

13. (lee2020livedoidvasculopathyin pages 5-7): J. Lee and Soyun Cho. Livedoid vasculopathy in koreans: clinical features and response to rivaroxaban treatment. Journal of the European Academy of Dermatology and Venereology, Jan 2020. URL: https://doi.org/10.1111/jdv.16129, doi:10.1111/jdv.16129. This article has 19 citations and is from a domain leading peer-reviewed journal.

14. (evans2015successfultreatmentof pages 2-2): John M. Evans, J. Daniel Jensen, and Naveed Sami. Successful treatment of livedoid vasculopathy with rivaroxaban. JAAD Case Reports, 1:340-341, Nov 2015. URL: https://doi.org/10.1016/j.jdcr.2015.08.002, doi:10.1016/j.jdcr.2015.08.002. This article has 21 citations.

15. (criado2011livedoidvasculopathyas pages 2-3): Paulo Ricardo Criado, Evandro Ararigboia Rivitti, Mirian Nacagami Sotto, and Jozélio Freire de Carvalho. Livedoid vasculopathy as a coagulation disorder. Autoimmunity reviews, 10 6:353-60, Apr 2011. URL: https://doi.org/10.1016/j.autrev.2010.11.008, doi:10.1016/j.autrev.2010.11.008. This article has 107 citations and is from a peer-reviewed journal.

16. (gao2020plasminogenactivatorinhibitor‐1 pages 1-3): Yimeng Gao and Hongzhong Jin. Plasminogen activator inhibitor‐1: a potential etiological role in livedoid vasculopathy. International Wound Journal, 17:1902-1908, Oct 2020. URL: https://doi.org/10.1111/iwj.13480, doi:10.1111/iwj.13480. This article has 13 citations and is from a peer-reviewed journal.

17. (weishaupt2019characteristicsriskfactors pages 2-4): C. Weishaupt, A. Strölin, B. Kahle, A. Kreuter, S. W. Schneider, J. Gerss, M. Eveslage, A. Drabik, and T. Goerge. Characteristics, risk factors and treatment reality in livedoid vasculopathy – a multicentre analysis. Journal of the European Academy of Dermatology and Venereology, 33:1784-1791, Sep 2019. URL: https://doi.org/10.1111/jdv.15639, doi:10.1111/jdv.15639. This article has 71 citations and is from a domain leading peer-reviewed journal.

18. (agirbasli2011enhancedfunctionalstability pages 4-5): Mehmet Agirbasli, Mesut Eren, Fatih Eren, Sheila B. Murphy, Zehra A. Serdar, Dilek Seckin, Tuba Zara, M. Cem Mat, Cuyan Demirkesen, and Douglas E. Vaughan. Enhanced functional stability of plasminogen activator inhibitor-1 in patients with livedoid vasculopathy. Journal of Thrombosis and Thrombolysis, 32:59-63, Feb 2011. URL: https://doi.org/10.1007/s11239-011-0556-y, doi:10.1007/s11239-011-0556-y. This article has 36 citations and is from a peer-reviewed journal.

19. (agirbasli2011enhancedfunctionalstability pages 2-4): Mehmet Agirbasli, Mesut Eren, Fatih Eren, Sheila B. Murphy, Zehra A. Serdar, Dilek Seckin, Tuba Zara, M. Cem Mat, Cuyan Demirkesen, and Douglas E. Vaughan. Enhanced functional stability of plasminogen activator inhibitor-1 in patients with livedoid vasculopathy. Journal of Thrombosis and Thrombolysis, 32:59-63, Feb 2011. URL: https://doi.org/10.1007/s11239-011-0556-y, doi:10.1007/s11239-011-0556-y. This article has 36 citations and is from a peer-reviewed journal.

20. (leeolou2023livedoidvasculopathy pages 3-4): Melissa C. Leeolou, Kerri E Rieger, and Jennifer E Yeh. Livedoid vasculopathy. Dermatology Online Journal, Nov 2023. URL: https://doi.org/10.5070/d329562414, doi:10.5070/d329562414. This article has 4 citations and is from a peer-reviewed journal.

21. (weishaupt2019characteristicsriskfactors pages 1-2): C. Weishaupt, A. Strölin, B. Kahle, A. Kreuter, S. W. Schneider, J. Gerss, M. Eveslage, A. Drabik, and T. Goerge. Characteristics, risk factors and treatment reality in livedoid vasculopathy – a multicentre analysis. Journal of the European Academy of Dermatology and Venereology, 33:1784-1791, Sep 2019. URL: https://doi.org/10.1111/jdv.15639, doi:10.1111/jdv.15639. This article has 71 citations and is from a domain leading peer-reviewed journal.

22. (weishaupt2019characteristicsriskfactors pages 4-5): C. Weishaupt, A. Strölin, B. Kahle, A. Kreuter, S. W. Schneider, J. Gerss, M. Eveslage, A. Drabik, and T. Goerge. Characteristics, risk factors and treatment reality in livedoid vasculopathy – a multicentre analysis. Journal of the European Academy of Dermatology and Venereology, 33:1784-1791, Sep 2019. URL: https://doi.org/10.1111/jdv.15639, doi:10.1111/jdv.15639. This article has 71 citations and is from a domain leading peer-reviewed journal.

23. (palanisamy2023painmanagementoptions pages 3-3): Nageshwari Palanisamy, Justine Chinnappan, and Ghassan Bachuwa. Pain management options in a patient with livedoid vasculopathy and peripheral neuropathy. European Journal of Case Reports in Internal Medicine, Feb 2023. URL: https://doi.org/10.12890/2023\_003727, doi:10.12890/2023\_003727. This article has 3 citations.

24. (ramphall2022comparativeefficacyof pages 9-9): Shivana Ramphall, Swarnima Rijal, Vishakh Prakash, Heba Ekladios, Jiya Mulayamkuzhiyil Saju, Naishal Mandal, Nang I Kham, Rabia Shahid, Shaili S Naik, and Sathish Venugopal. Comparative efficacy of rivaroxaban and immunoglobulin therapy in the treatment of livedoid vasculopathy: a systematic review. Cureus, Aug 2022. URL: https://doi.org/10.7759/cureus.28485, doi:10.7759/cureus.28485. This article has 7 citations.

25. (NCT05878327 chunk 1):  Livedoid Vasculopathy: Strong Association With Smoking, Weak Association With Thrombophilia. University of Zurich. 2013. ClinicalTrials.gov Identifier: NCT05878327

26. (NCT00975871 chunk 1):  Correlation of Genetic Polymorphism and Livedo Vasculitis. National Taiwan University Hospital. 2007. ClinicalTrials.gov Identifier: NCT00975871