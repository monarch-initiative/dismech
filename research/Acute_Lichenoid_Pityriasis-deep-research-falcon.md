---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T15:41:53.839816'
end_time: '2026-05-04T16:01:54.708920'
duration_seconds: 1200.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Lichenoid Pityriasis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 39
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Lichenoid Pityriasis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Lichenoid Pityriasis** covering all of the
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
- **Disease Name:** Acute Lichenoid Pityriasis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acute Lichenoid Pityriasis** covering all of the
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


# Acute Lichenoid Pityriasis (PLEVA) — Comprehensive Disease Characteristics Report

## Target disease
**Acute lichenoid pityriasis** is most consistently used in the clinical literature as a synonym for **pityriasis lichenoides et varioliformis acuta (PLEVA)**, the acute pole of the pityriasis lichenoides (PL) spectrum; some sources also refer to PLEVA as **Mucha–Habermann disease**, and the most severe ulceronecrotic systemic variant as **febrile ulceronecrotic Mucha–Habermann disease (FUMHD)**. (jung2020systematicreviewof pages 1-2, ma2024diagnosticchallengesof pages 1-3, fatturi2024pityriasislichenoidesassessment pages 1-2)

| Domain | Key points (with numbers) | Evidence type (review/series/case report) | Citation IDs | Publication year | URL/DOI |
|---|---|---|---|---|---|
| Definitions / synonyms | Acute lichenoid pityriasis corresponds to **pityriasis lichenoides et varioliformis acuta (PLEVA)**; also called **Mucha-Habermann disease** in some sources. It is the acute pole of the pityriasis lichenoides spectrum; severe ulceronecrotic variant = **febrile ulceronecrotic Mucha-Habermann disease (FUMHD)**. | Review; case report | (jung2020systematicreviewof pages 1-2, ma2024diagnosticchallengesof pages 1-3, fatturi2024pityriasislichenoidesassessment pages 1-2) | 2020, 2024 | https://doi.org/10.1111/bjd.18977 ; https://doi.org/10.70672/bcfbzp08 ; https://doi.org/10.1016/j.jped.2024.03.011 |
| Epidemiology stats | Rare disease; one review cites incidence around **0.05%** with slight male predominance and onset in late childhood/young adulthood. Pediatric review noted slight male predominance **56%**. Pediatric Brazilian series: **41** patients total, **5/41 PLEVA (12.2%)**, **32/41 PLC (78.0%)**. Thai pediatric series: **43** patients, **10/43 PLEVA (23.3%)**, male:female **1.3:1**, common onset age **4–7 years**. A 2013 pediatric review summarized series with PLEVA frequencies ranging **25% to 57.3%** among PL cohorts. | Review; retrospective pediatric series | (jung2020systematicreviewof pages 1-2, ma2024diagnosticchallengesof pages 1-3, fatturi2024pityriasislichenoidesassessment pages 1-2, rujimethapass2025pityriasislichenoidesin pages 5-6, boos2013pityriasislichenoidesand pages 1-2) | 2020, 2024, 2025, 2013 | https://doi.org/10.1111/bjd.18977 ; https://doi.org/10.70672/bcfbzp08 ; https://doi.org/10.1016/j.jped.2024.03.011 ; https://doi.org/10.35755/jmedassocthai.2025.5.377-383-02606 ; https://doi.org/10.1007/s13671-013-0054-x |
| Key clinical features and course | Acute eruption of erythematous papules/papulovesicles that may become hemorrhagic/necrotic and heal with **varioliform scarring**. Lesions often involve trunk and extremities; pruritus common; lesions resolve over weeks but recur in crops. Thai series: PLEVA disease duration **1–20 months**, mean about **4 ± 2 months**; diagnosis lag about **1.5 months** in PLEVA vs **3 months** in PLC. Systemic symptoms (e.g., fever, hepatomegaly) were more common in PLEVA; varioliform scars were seen only in PLEVA. Severe FUMHD may include mucosal lesions, high fever, sepsis, cardiomyopathy, pulmonary involvement. | Review; retrospective series; case report | (ma2024diagnosticchallengesof pages 1-3, rujimethapass2025pityriasislichenoidesin pages 5-6, boos2013pityriasislichenoidesand pages 1-2, marinhernandez2023acutelichenoidand pages 1-2) | 2024, 2025, 2013, 2023 | https://doi.org/10.70672/bcfbzp08 ; https://doi.org/10.35755/jmedassocthai.2025.5.377-383-02606 ; https://doi.org/10.1007/s13671-013-0054-x ; https://doi.org/10.24875/bmhim.22000043 |
| Histopathology / diagnostics / differentials | Diagnosis is clinicopathologic and usually confirmed by skin biopsy. Reported findings: **parakeratosis, spongiosis, lichenoid/interface dermatitis, dyskeratotic keratinocytes, erythrocyte extravasation, focal epidermotropism, epidermal necrosis, hemorrhagic crusting/ulceration**; one pediatric case showed **lymphocytic vasculitis** with focal epidermal necrosis. DIF may be negative for **IgG/IgA/IgM/C3**. Important differentials: **guttate psoriasis, varicella, pityriasis rosea, secondary syphilis**, and occasionally **mycosis fungoides**. | Review; case report; diagnostic image/table extraction | (ma2024diagnosticchallengesof pages 1-3, ma2024diagnosticchallengesof pages 3-9, boos2013pityriasislichenoidesand pages 1-2, marinhernandez2023acutelichenoidand pages 1-2, ma2024diagnosticchallengesof media c2c2a990) | 2024, 2013, 2023 | https://doi.org/10.70672/bcfbzp08 ; https://doi.org/10.1007/s13671-013-0054-x ; https://doi.org/10.24875/bmhim.22000043 |
| Triggers / etiology hypotheses | Etiopathogenesis remains uncertain. Main hypotheses: **T-cell dyscrasia / lymphoproliferative process**, **immune-complex hypersensitivity**, or inflammatory reaction to antigenic stimuli. Reported infectious associations include **EBV, HIV, VZV, HSV-2, Toxoplasma gondii, group A streptococcus, parvovirus B19, HHV-8**. Reported exposure triggers include **drugs** (e.g., antidepressants, statins, anti-TNF agents), **subcutaneous immunoglobulin**, and **vaccines** (including MMR; case reports after COVID-19 vaccination also reported in the literature). Pediatric review cited preceding **URI in 33%** and drug/vaccination exposure in **20%**. | Review; case report; pediatric review | (ma2024diagnosticchallengesof pages 1-3, boos2013pityriasislichenoidesand pages 1-2) | 2024, 2013 | https://doi.org/10.70672/bcfbzp08 ; https://doi.org/10.1007/s13671-013-0054-x |
| Treatments and reported response / remission rates | No standardized guideline-supported regimen. Systematic review of **27** studies (**502** participants) found **phototherapy** had the highest proportion of complete remissions; NB-UVB often recommended first-line. Pediatric Brazilian series: overall remission **71.9% (23 patients)**; remission with **antibiotics 56.6% (17 patients)** and with **phototherapy 80% (4 patients)**. Thai series: erythromycin used in **95.3%**, prednisolone **9.3%**, methotrexate **9.3%**; one FUMHD patient responded to methylprednisolone plus methotrexate. Review/case sources list **oral erythromycin ± topical corticosteroids** and **low-dose methotrexate** as common second-line options; refractory disease/FUMHD has been treated with methotrexate, acitretin, dapsone, cyclosporine, and other immunomodulators. One case resolved after **2 months** of oral plus topical corticosteroids. | Systematic review; retrospective pediatric series; case report | (jung2020systematicreviewof pages 1-2, fatturi2024pityriasislichenoidesassessment pages 1-2, rujimethapass2025pityriasislichenoidesin pages 5-6, ma2024diagnosticchallengesof pages 3-9, ma2024diagnosticchallengesof pages 1-3) | 2020, 2024, 2025 | https://doi.org/10.1111/bjd.18977 ; https://doi.org/10.1016/j.jped.2024.03.011 ; https://doi.org/10.35755/jmedassocthai.2025.5.377-383-02606 ; https://doi.org/10.70672/bcfbzp08 |
| Prognosis / CTCL progression signals | Usually benign and self-limited/relapsing, but persistent monitoring is advised. Long-term PL-to-MF progression appears uncommon but documented: one study found **3/58 (5.2%)** developed mycosis fungoides after **3–11 years**; another pediatric cohort reported **1/43 (2.3%)** later diagnosed with MF. In non-MF-associated PL, **85% (35/41)** reported lasting complete remissions in one series. Signals concerning for CTCL evolution include **prolonged clinical course**, appearance of **patches/larger plaques**, increased lymphocytic atypia, reduced apoptotic keratinocytes, reduced **CD7+/CD8+** cells, and **clonal TCR rearrangement**. | Molecular clinicopathologic study; pediatric series; review | (rujimethapass2025pityriasislichenoidesin pages 5-6, rujimethapass2025pityriasislichenoidesin pages 6-7) | 2025 | https://doi.org/10.35755/jmedassocthai.2025.5.377-383-02606 |
| Immunopathogenesis / clonality signals | Data are mixed and not disease-defining. A pediatric review summarized one study reporting monoclonal TCR rearrangement in **57% of PLEVA vs 8% of PLC**, while another found only **1/23** positive, underscoring uncertainty. Overall interpretation in reviews: clonality can occur in PLEVA/PL and does **not** by itself establish lymphoma; clinicopathologic correlation remains essential. | Review summarizing molecular studies | (boos2013pityriasislichenoidesand pages 1-2) | 2013 | https://doi.org/10.1007/s13671-013-0054-x |


*Table: This table compacts the main disease-characteristics evidence for acute lichenoid pityriasis (PLEVA), including epidemiology, phenotype, diagnosis, triggers, treatment outcomes, and prognosis. It is useful as a quick-reference scaffold for a disease knowledge base entry with source-linked claims.*

---

## 1. Disease information
### Overview / definition (current understanding)
PLEVA is an uncommon inflammatory papulosquamous dermatosis characterized clinically by crops of erythematous papules/papulovesicles that may become necrotic/hemorrhagic and can heal with varioliform scarring, with recurrences over time. (ma2024diagnosticchallengesof pages 1-3, jung2020systematicreviewof pages 1-2, marinhernandez2023acutelichenoidand pages 1-2)

### Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Within the retrieved primary and review sources in this run, **ICD-10/ICD-11, MeSH, OMIM, Orphanet, and MONDO identifiers were not explicitly provided**, so they cannot be safely asserted from the evidence base assembled here. (ma2024diagnosticchallengesof pages 1-3, jung2020systematicreviewof pages 1-2)

### Common synonyms / alternative names
* Pityriasis lichenoides et varioliformis acuta (PLEVA) (marinhernandez2023acutelichenoidand pages 1-2, jung2020systematicreviewof pages 1-2)
* Mucha–Habermann disease (jung2020systematicreviewof pages 1-2, ma2024diagnosticchallengesof pages 1-3)
* Febrile ulceronecrotic Mucha–Habermann disease (FUMHD) (severe variant) (ma2024diagnosticchallengesof pages 1-3, fatturi2024pityriasislichenoidesassessment pages 1-2)

### Evidence provenance
Evidence is primarily derived from **aggregated disease-level resources** (systematic reviews and cohort/case series) and supplemented by individual case reports. (jung2020systematicreviewof pages 1-2, marinhernandez2023acutelichenoidand pages 1-2, fatturi2024pityriasislichenoidesassessment pages 1-2)

---

## 2. Etiology
### Disease causal factors (mechanistic hypotheses)
Etiopathogenesis remains uncertain. Frequently cited hypotheses include:
1) **T-cell dyscrasia / lymphoproliferative process** (i.e., antigen-driven clonal/oligoclonal T-cell expansion in skin), and
2) **immune-complex hypersensitivity** reaction to infectious/drug antigens. (ma2024diagnosticchallengesof pages 1-3, boos2013pityriasislichenoidesand pages 1-2, fatturi2024pityriasislichenoidesassessment pages 1-2)

### Risk factors / triggers (2023–2024 emphasis)
Evidence supports PLEVA/PL being **triggered** (not proven caused) by infections, drugs, or vaccines in some patients.

*In a 2024 pediatric series (n=41), triggers were documented in 11/41 (26.8%) patients*, including fever (3), COVID-19 infection (2), and single cases of sun exposure, HIV, parotitis, tonsillitis, cold weather, and COVID-19 vaccination. (fatturi2024pityriasislichenoidesassessment pages 2-4)

A 2024 diagnostic-focused report lists reported infectious triggers (e.g., **EBV, HIV, varicella-zoster virus, HSV-2, Toxoplasma gondii, group A streptococcus**) and notes drug and vaccine triggers in the literature (including anti-TNF and vaccination). (ma2024diagnosticchallengesof pages 1-3)

A pediatric review summarizes that a preceding upper respiratory infection was reported in **33%** and drug/vaccination exposure in **20%** in one summarized series. (boos2013pityriasislichenoidesand pages 1-2)

### Protective factors
No validated genetic or environmental protective factors were identified in the retrieved evidence. (jung2020systematicreviewof pages 1-2, fatturi2024pityriasislichenoidesassessment pages 1-2)

### Gene–environment interactions
No specific gene–environment interaction findings were available in the retrieved full text, although one systematic review explicitly calls for future work on “understanding the interplay between genetic predisposition and environmental factors.” (everettUnknownyear…forpityriasisa pages 61-64)

---

## 3. Phenotypes
### Core clinical phenotypes (with suggested HPO terms)
Key phenotypes include:
* Crops of erythematous papules/papulovesicles, sometimes necrotic/hemorrhagic (suggested HPO: **Papule** [HP:0200031], **Vesicle** [HP:0100796], **Skin ulcer** [HP:0001053]) (ma2024diagnosticchallengesof pages 1-3, marinhernandez2023acutelichenoidand pages 1-2)
* Crusting/necrosis and potential ulceration (HPO: **Skin necrosis** [HP:0001032], **Crusting** [HP:0030799]) (ma2024diagnosticchallengesof pages 1-3)
* Pruritus (HPO: **Pruritus** [HP:0000989]) (rujimethapass2025pityriasislichenoidesin pages 5-6, boos2013pityriasislichenoidesand pages 1-2)
* Varioliform scarring (HPO: **Abnormal scar** [HP:0100699]) (rujimethapass2025pityriasislichenoidesin pages 5-6, marinhernandez2023acutelichenoidand pages 1-2)
* Post-inflammatory dyspigmentation (HPO: **Hypopigmentation of the skin** [HP:0001042]) (marinhernandez2023acutelichenoidand pages 1-2, rujimethapass2025pityriasislichenoidesin pages 5-6)

### Age of onset
Onset often occurs in childhood/young adulthood; pediatric cohorts show onset peaks around preschool/early school ages. (jung2020systematicreviewof pages 1-2, rujimethapass2025pityriasislichenoidesin pages 5-6, fatturi2024pityriasislichenoidesassessment pages 1-2)

### Severity and progression/course
PLEVA is typically acute/subacute and may recur in crops; a Thai pediatric cohort reported PLEVA duration range **1–20 months** with mean **~4±2 months**. (rujimethapass2025pityriasislichenoidesin pages 5-6)

Severe FUMHD can present with mucosal involvement, high fever, and systemic complications (e.g., sepsis, cardiomyopathy, pulmonary involvement). (ma2024diagnosticchallengesof pages 1-3)

### Frequency among affected individuals
In pediatric PL cohorts, PLEVA frequency varies widely by setting and referral patterns; for example, in a 2024 pediatric Brazilian cohort PLEVA was **5/41 (12.2%)**. (fatturi2024pityriasislichenoidesassessment pages 1-2)

### Quality of life impact
Formal HRQoL instruments were not reported in retrieved primary sources; however, a 2024 diagnostic report notes misdiagnosis can lead to substantial emotional/psychological stress (qualitative impact). (ma2024diagnosticchallengesof pages 1-3)

---

## 4. Genetic/molecular information
### Causal genes / pathogenic variants
No causal genes or pathogenic germline variants were identified in the retrieved literature; PLEVA is generally treated as a complex inflammatory dermatosis rather than a monogenic disorder in these sources. (jung2020systematicreviewof pages 1-2, fatturi2024pityriasislichenoidesassessment pages 1-2)

### Molecular findings (limited)
Immunophenotyping can show T-cell–predominant infiltrates. A 2023 pediatric case reported lesional IHC including **CD3+**, **CD4+++**, **CD8+**, **CD7+++**, and **CD20−**. (marinhernandez2023acutelichenoidand pages 1-2)

T-cell receptor clonality is variably detected and is not diagnostic of lymphoma by itself; a pediatric review summarized one study with monoclonal TCR rearrangement in **57% of PLEVA vs 8% of PLC**, while another series found only **1/23** positive, emphasizing heterogeneity and uncertain clinical significance. (boos2013pityriasislichenoidesand pages 1-2)

---

## 5. Environmental information
Environmental contributors are mainly reported as **triggering exposures** (infections, drugs, vaccines) rather than chronic toxic or occupational exposures. (ma2024diagnosticchallengesof pages 1-3, fatturi2024pityriasislichenoidesassessment pages 2-4)

---

## 6. Mechanism / pathophysiology
### Proposed causal chain (current consensus framing)
A common mechanistic framing is: **antigenic stimulus** (infectious agent, drug, vaccine) → **cutaneous immune activation with T-cell–predominant interface/lichenoid dermatitis** → **keratinocyte injury/necrosis and vascular/inflammatory changes** → **papulonecrotic lesions with crusting** → **post-inflammatory dyspigmentation or varioliform scarring**. (ma2024diagnosticchallengesof pages 1-3, marinhernandez2023acutelichenoidand pages 1-2, boos2013pityriasislichenoidesand pages 1-2)

### Cellular processes and pathways (ontology suggestions)
Because the retrieved sources do not provide pathway-specific transcriptomic/proteomic findings, ontology terms are suggested at a high level based on clinicopathology:
* GO biological processes: **T cell activation**, **inflammatory response**, **keratinocyte apoptotic process**, **leukocyte migration** (supported conceptually by interface/lichenoid pattern and T-cell infiltrates) (ma2024diagnosticchallengesof pages 1-3, marinhernandez2023acutelichenoidand pages 1-2)
* Cell types (Cell Ontology): **T cell (CL:0000084)**; plausible involvement of **CD4-positive, alpha-beta T cell (CL:0000624)** and **CD8-positive, alpha-beta T cell (CL:0000625)** consistent with reported IHC (marinhernandez2023acutelichenoidand pages 1-2)

### Immune system involvement
PLEVA lesions show interface/lichenoid dermatitis with epidermotropism in some cases, and PLEVA may represent a benign clonal or oligoclonal T-cell–driven process in a subset. (ma2024diagnosticchallengesof pages 3-9, boos2013pityriasislichenoidesand pages 1-2)

---

## 7. Anatomical structures affected
### Organ and tissue level
Primary involvement is the **skin** (UBERON: **skin** [UBERON:0002097]), with lesions commonly on trunk and extremities. (marinhernandez2023acutelichenoidand pages 1-2, ma2024diagnosticchallengesof pages 1-3)

Severe FUMHD can involve mucosa and systemic organs (cardiopulmonary involvement described). (ma2024diagnosticchallengesof pages 1-3)

### Subcellular level
Not resolved in retrieved evidence.

---

## 8. Temporal development
* **Onset pattern:** acute/subacute crops of papules; individual lesions may resolve within weeks but new lesions recur (ma2024diagnosticchallengesof pages 1-3, marinhernandez2023acutelichenoidand pages 1-2)
* **Course:** variable, often self-limited but may persist months; pediatric cohort mean duration for PLEVA ~4 months (rujimethapass2025pityriasislichenoidesin pages 5-6)
* **Severe course:** FUMHD can be rapidly progressive with systemic complications (ma2024diagnosticchallengesof pages 1-3)

---

## 9. Inheritance and population
PLEVA is not presented as a Mendelian disorder in the retrieved sources; inheritance pattern and penetrance are not established. (jung2020systematicreviewof pages 1-2)

### Epidemiology statistics (available)
* A systematic review cites incidence approximately **0.05%** and notes slight male predominance and typical onset in late childhood/young adulthood. (jung2020systematicreviewof pages 1-2)
* A 2023 pediatric report estimated incidence as **~1/2000 inhabitants** (noted as an estimate in that report). (marinhernandez2023acutelichenoidand pages 1-2)

Because these numbers come from different sources with different contexts, they should be treated as approximate. (jung2020systematicreviewof pages 1-2, marinhernandez2023acutelichenoidand pages 1-2)

---

## 10. Diagnostics
### Clinical evaluation
PLEVA can mimic multiple papulovesicular/papulosquamous eruptions. Diagnostic work-up typically relies on clinical morphology and distribution plus biopsy confirmation. (ma2024diagnosticchallengesof pages 1-3, jung2020systematicreviewof pages 1-2)

### Histopathology
Commonly described findings include **lichenoid/interface dermatitis**, **parakeratosis**, **spongiosis**, **erythrocyte extravasation**, **epidermal necrosis**, **subepidermal blistering**, and sometimes **focal epidermotropism**; one pediatric case highlighted **lymphocytic vasculitis** with focal epidermal necrosis. (ma2024diagnosticchallengesof pages 1-3, ma2024diagnosticchallengesof pages 3-9, marinhernandez2023acutelichenoidand pages 1-2)

Direct immunofluorescence may be negative for immune deposits at the dermal–epidermal junction (IgG/IgA/IgM/C3 negative in a reported case). (ma2024diagnosticchallengesof pages 1-3)

### Differential diagnosis
A differential table extracted from a 2024 diagnostic paper highlights confusion with **guttate psoriasis**, **varicella**, **pityriasis rosea**, and **secondary syphilis**. (ma2024diagnosticchallengesof media c2c2a990)

Histopathology figures supporting interface dermatitis and focal epidermotropism are available from the same report. (ma2024diagnosticchallengesof media 72391849, ma2024diagnosticchallengesof media 01b2711c)

### Omics/genetic testing
Routine genetic testing is not described for PLEVA in the retrieved sources. (jung2020systematicreviewof pages 1-2)

---

## 11. Outcome / prognosis
### General prognosis
PLEVA is generally benign/self-limited but can be relapsing. (jung2020systematicreviewof pages 1-2, rujimethapass2025pityriasislichenoidesin pages 5-6)

### Risk of progression to cutaneous T-cell lymphoma (CTCL)
Progression risk is debated; in a Thai pediatric cohort, **1/43 (2.3%)** was later diagnosed as mycosis fungoides on repeat biopsy. (rujimethapass2025pityriasislichenoidesin pages 5-6)

Clinical concern for MF/CTCL is heightened when clinical morphology changes or the course is prolonged; a 2023 pediatric case illustrates diagnostic overlap when an initial biopsy was read as suggestive of mycosis fungoides but was later revised to PLEVA with lymphocytic vasculitis. (marinhernandez2023acutelichenoidand pages 1-2)

---

## 12. Treatment
### Evidence quality (expert appraisal)
A 2020 systematic review (British Journal of Dermatology) notes: **“The current literature consists almost entirely of uncontrolled studies, and none provides compelling data to support an evidence-based approach to PL treatment.”** (May 2020). (jung2020systematicreviewof pages 1-2)

### First-line and second-line approaches (real-world implementations)
Across reviews and recent summaries, **narrow-band UVB (NB-UVB) phototherapy** is commonly recommended as **first-line**, with **oral erythromycin** or **low-dose methotrexate** (± topical corticosteroids) used as **second-line** options. (ma2024diagnosticchallengesof pages 3-9, feschuk2023pityriasislichenoidesfollowing pages 1-3)

### Quantitative treatment outcomes
*Phototherapy (systematic review evidence):* In a 2020 systematic review, complete response rates were reported as **75.0% (102/136) for NB-UVB** and **69% (25/36) for PUVA**, with relapse after phototherapy in **25.7% (66/257)**. (jung2020systematicreviewof pages 2-4)

*Pediatric real-world outcomes (2024 series):* In a 2024 pediatric cohort, overall remission was **71.9%**; among antibiotic-treated patients remission was **56.6% (17/30)**; among phototherapy-treated patients remission was **80% (4/5)**. (fatturi2024pityriasislichenoidesassessment pages 1-2)

*Pediatric phototherapy-focused evidence:* A pediatric phototherapy literature review reported initial clearance rates of **89.6% for BB-UVB** (with **23.1% recurrence**), **73% for NB-UVB** (with **no recurrence**), and **83% for PUVA** (with **60% recurrence**), with generally mild erythema as the main side effect. (maranda2016phototherapyforpityriasis pages 1-2)

### Systemic therapy for severe disease (FUMHD)
FUMHD may require systemic immunosuppression; methotrexate is repeatedly cited as important in refractory PLEVA/FUMHD. (ma2024diagnosticchallengesof pages 3-9, rujimethapass2025pityriasislichenoidesin pages 5-6)

### MAXO (Medical Action Ontology) suggestions
* **Phototherapy** (e.g., NB-UVB phototherapy) (jung2020systematicreviewof pages 2-4, maranda2016phototherapyforpityriasis pages 1-2)
* **Systemic antibiotic therapy** (macrolides/tetracyclines) (fatturi2024pityriasislichenoidesassessment pages 2-4, fatturi2024pityriasislichenoidesassessment pages 1-2)
* **Topical corticosteroid therapy** (supportive symptom control) (ma2024diagnosticchallengesof pages 3-9)
* **Systemic immunosuppressive therapy** (methotrexate; severe/refractory cases) (ma2024diagnosticchallengesof pages 3-9, rujimethapass2025pityriasislichenoidesin pages 5-6)

### Clinical trials
A ClinicalTrials.gov search in this run returned no relevant interventional trials for PLEVA; retrieved NCT records were unrelated false positives. (clinical trial search output not relevant to PLEVA; no citeable PLEVA trial context IDs available)

---

## 13. Prevention
No evidence-based primary prevention strategies were identified in retrieved sources; because triggers are inconsistent and causality is unproven, prevention is limited to pragmatic measures (avoidance of suspected individual triggers when reproducibly associated) and **close follow-up** for severe/systemic features suggestive of FUMHD. (ma2024diagnosticchallengesof pages 1-3, ma2024diagnosticchallengesof pages 3-9)

---

## 14. Other species / natural disease
No evidence was found in the retrieved sources for naturally occurring PLEVA in other species or zoonotic considerations. (maranda2016phototherapyforpityriasis pages 1-2, ma2024diagnosticchallengesof pages 3-9)

---

## 15. Model organisms
No explicit model organism systems or animal models for PLEVA were described in the retrieved, PLEVA-focused texts in this run. (maranda2016phototherapyforpityriasis pages 1-2, ma2024diagnosticchallengesof pages 3-9)

---

## Recent developments and latest research highlights (prioritize 2023–2024)
1) **SARS-CoV-2 infection/vaccination temporal association literature (2023):** A 2023 review of 14 cases reported that 9/14 (64.3%) followed vaccination and 4/14 (28.6%) followed infection; 12/14 (85.7%) had marked improvement or complete resolution at follow-up, and the authors state **“Naranjo’s ADRPS suggests SARS-CoV-2 may be a ‘probable’ cause of PL,”** while emphasizing uncertainty and possible coincidence. (Jan 2023; https://doi.org/10.1007/s13671-023-00380-1). (feschuk2023pityriasislichenoidesfollowing pages 3-4)

2) **Pityriasis eruptions after COVID-19 vaccination (systematic review, 2023):** A systematic review identified 94 patients with pityriasis/pityriasis-like eruptions after vaccination; **PLEVA accounted for 7.4%** of reported cases; biopsy was performed in 41/94. (Aug 2023; https://doi.org/10.4081/dr.2023.9742). (duzett2023pityriasisfollowingcovid19 pages 2-3)

3) **Large pediatric series with quantified remission predictors (2024):** A 2024 pediatric cohort reported documented triggers in 26.8% and remission rates by therapy (antibiotics vs phototherapy), and found remission odds were higher with onset after age 5 (OR 13.33). (Sep 2024; https://doi.org/10.1016/j.jped.2024.03.011). (fatturi2024pityriasislichenoidesassessment pages 2-4, fatturi2024pityriasislichenoidesassessment pages 1-2)

4) **Diagnostic pitfalls and histopathology emphasis (2024):** A 2024 diagnostic report underscores clinical overlap with guttate psoriasis/varicella/pityriasis rosea/secondary syphilis and provides histopathology examples (subepidermal blistering, interface dermatitis, focal epidermotropism) to support biopsy confirmation. (Nov 2024; https://doi.org/10.70672/bcfbzp08). (ma2024diagnosticchallengesof media c2c2a990, ma2024diagnosticchallengesof media 72391849, ma2024diagnosticchallengesof media 01b2711c)


References

1. (jung2020systematicreviewof pages 1-2): F. Jung, C. Sibbald, M. Bohdanowicz, J. Ingram, V. Piguet, V. Piguet, and V. Piguet. Systematic review of the efficacies and adverse effects of treatments for pityriasis lichenoides. British Journal of Dermatology, 183:1026-1032, May 2020. URL: https://doi.org/10.1111/bjd.18977, doi:10.1111/bjd.18977. This article has 30 citations and is from a highest quality peer-reviewed journal.

2. (ma2024diagnosticchallengesof pages 1-3): Abd Rahman MA, Jamani NA, Abdul Halim S, and Zainun N. Diagnostic challenges of pityriasis lichenoides et varioliformis acuta (pleva). Asian Journal of Medicine &amp; Health Sciences, 7:279-287, Nov 2024. URL: https://doi.org/10.70672/bcfbzp08, doi:10.70672/bcfbzp08. This article has 0 citations.

3. (fatturi2024pityriasislichenoidesassessment pages 1-2): Aluhine L. Fatturi, Mariana A.P. Morgan, Jandrei R. Markus, Lucero Noguera-Morel, and Vânia O. Carvalho. Pityriasis lichenoides: assessment of 41 pediatric patients. Jornal de Pediatria, 100:527-532, Sep 2024. URL: https://doi.org/10.1016/j.jped.2024.03.011, doi:10.1016/j.jped.2024.03.011. This article has 9 citations and is from a peer-reviewed journal.

4. (rujimethapass2025pityriasislichenoidesin pages 5-6): MD¹ Nootchanard Rujimethapass, MD¹ Wanida Limpongsanurak, and MD¹ Srisupalak Singalavanija. Pityriasis lichenoides in thai children: a 10-years review of clinical and treatment outcome. Journal of the Medical Association of Thailand, 108:377-383, May 2025. URL: https://doi.org/10.35755/jmedassocthai.2025.5.377-383-02606, doi:10.35755/jmedassocthai.2025.5.377-383-02606. This article has 1 citations.

5. (boos2013pityriasislichenoidesand pages 1-2): Markus D. Boos, Sara S. Samimi, Alain H. Rook, Albert C. Yan, and Ellen J. Kim. Pityriasis lichenoides and cutaneous t cell lymphoma: an update on the diagnosis and management of the most common benign and malignant cutaneous lymphoproliferative diseases in children. Current Dermatology Reports, 2:203-211, Aug 2013. URL: https://doi.org/10.1007/s13671-013-0054-x, doi:10.1007/s13671-013-0054-x. This article has 6 citations.

6. (marinhernandez2023acutelichenoidand pages 1-2): Eduardo Marín-Hernández, Laura N. Escobar-García, Martha G. Contreras, Alfredo Valero-Gómez, and Georgina A. Siordia-Reyes. Acute lichenoid and varioliform pityriasis in a pediatric patient. Boletín Médico del Hospital Infantil de México, Jun 2023. URL: https://doi.org/10.24875/bmhim.22000043, doi:10.24875/bmhim.22000043. This article has 5 citations.

7. (ma2024diagnosticchallengesof pages 3-9): Abd Rahman MA, Jamani NA, Abdul Halim S, and Zainun N. Diagnostic challenges of pityriasis lichenoides et varioliformis acuta (pleva). Asian Journal of Medicine &amp; Health Sciences, 7:279-287, Nov 2024. URL: https://doi.org/10.70672/bcfbzp08, doi:10.70672/bcfbzp08. This article has 0 citations.

8. (ma2024diagnosticchallengesof media c2c2a990): Abd Rahman MA, Jamani NA, Abdul Halim S, and Zainun N. Diagnostic challenges of pityriasis lichenoides et varioliformis acuta (pleva). Asian Journal of Medicine &amp; Health Sciences, 7:279-287, Nov 2024. URL: https://doi.org/10.70672/bcfbzp08, doi:10.70672/bcfbzp08. This article has 0 citations.

9. (rujimethapass2025pityriasislichenoidesin pages 6-7): MD¹ Nootchanard Rujimethapass, MD¹ Wanida Limpongsanurak, and MD¹ Srisupalak Singalavanija. Pityriasis lichenoides in thai children: a 10-years review of clinical and treatment outcome. Journal of the Medical Association of Thailand, 108:377-383, May 2025. URL: https://doi.org/10.35755/jmedassocthai.2025.5.377-383-02606, doi:10.35755/jmedassocthai.2025.5.377-383-02606. This article has 1 citations.

10. (fatturi2024pityriasislichenoidesassessment pages 2-4): Aluhine L. Fatturi, Mariana A.P. Morgan, Jandrei R. Markus, Lucero Noguera-Morel, and Vânia O. Carvalho. Pityriasis lichenoides: assessment of 41 pediatric patients. Jornal de Pediatria, 100:527-532, Sep 2024. URL: https://doi.org/10.1016/j.jped.2024.03.011, doi:10.1016/j.jped.2024.03.011. This article has 9 citations and is from a peer-reviewed journal.

11. (everettUnknownyear…forpityriasisa pages 61-64): L Everett. … for pityriasis lichenoides chronica, pityriasis lichenoides et varioliformis acuta, and febrile ulceronecrotic mucha–habermann disease: a systematic review. Unknown journal, Unknown year.

12. (ma2024diagnosticchallengesof media 72391849): Abd Rahman MA, Jamani NA, Abdul Halim S, and Zainun N. Diagnostic challenges of pityriasis lichenoides et varioliformis acuta (pleva). Asian Journal of Medicine &amp; Health Sciences, 7:279-287, Nov 2024. URL: https://doi.org/10.70672/bcfbzp08, doi:10.70672/bcfbzp08. This article has 0 citations.

13. (ma2024diagnosticchallengesof media 01b2711c): Abd Rahman MA, Jamani NA, Abdul Halim S, and Zainun N. Diagnostic challenges of pityriasis lichenoides et varioliformis acuta (pleva). Asian Journal of Medicine &amp; Health Sciences, 7:279-287, Nov 2024. URL: https://doi.org/10.70672/bcfbzp08, doi:10.70672/bcfbzp08. This article has 0 citations.

14. (feschuk2023pityriasislichenoidesfollowing pages 1-3): Aileen M. Feschuk, Maxwell Green, Nadia Kashetsky, and Howard I. Maibach. Pityriasis lichenoides following sars-cov-2 infection/vaccination. Current Dermatology Reports, 12:27-32, Jan 2023. URL: https://doi.org/10.1007/s13671-023-00380-1, doi:10.1007/s13671-023-00380-1. This article has 7 citations.

15. (jung2020systematicreviewof pages 2-4): F. Jung, C. Sibbald, M. Bohdanowicz, J. Ingram, V. Piguet, V. Piguet, and V. Piguet. Systematic review of the efficacies and adverse effects of treatments for pityriasis lichenoides. British Journal of Dermatology, 183:1026-1032, May 2020. URL: https://doi.org/10.1111/bjd.18977, doi:10.1111/bjd.18977. This article has 30 citations and is from a highest quality peer-reviewed journal.

16. (maranda2016phototherapyforpityriasis pages 1-2): Eric Laurent Maranda, Megan Smith, Austin H. Nguyen, Vivek N. Patel, Lawrence A. Schachner, and Jimenez J. Joaquin. Phototherapy for pityriasis lichenoides in the pediatric population: a review of the published literature. American Journal of Clinical Dermatology, 17:583-591, Aug 2016. URL: https://doi.org/10.1007/s40257-016-0216-2, doi:10.1007/s40257-016-0216-2. This article has 27 citations and is from a peer-reviewed journal.

17. (feschuk2023pityriasislichenoidesfollowing pages 3-4): Aileen M. Feschuk, Maxwell Green, Nadia Kashetsky, and Howard I. Maibach. Pityriasis lichenoides following sars-cov-2 infection/vaccination. Current Dermatology Reports, 12:27-32, Jan 2023. URL: https://doi.org/10.1007/s13671-023-00380-1, doi:10.1007/s13671-023-00380-1. This article has 7 citations.

18. (duzett2023pityriasisfollowingcovid19 pages 2-3): Laura Duzett, Guadalupe Mercado, Vasiliki Tasouli-Drakou, Alicia Kane, and Alison Tam. Pityriasis following covid-19 vaccinations: a systematic review. Dermatology Reports, Aug 2023. URL: https://doi.org/10.4081/dr.2023.9742, doi:10.4081/dr.2023.9742. This article has 2 citations.