---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-11T13:27:35.913935'
end_time: '2026-04-11T13:34:19.575536'
duration_seconds: 403.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mediator Complex Neurodevelopmental Disorder
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mediator Complex Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Mediator Complex Neurodevelopmental Disorder** covering all of the
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
- **Disease Name:** Mediator Complex Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Mediator Complex Neurodevelopmental Disorder** covering all of the
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


# Mediator Complex Neurodevelopmental Disorder (MEDopathies): Disease Characteristics Report

## Executive summary
“Mediator Complex Neurodevelopmental Disorder” is best understood as an umbrella of monogenic neurodevelopmental disorders caused by pathogenic variants in genes encoding subunits of the RNA polymerase II Mediator complex (often termed **MEDopathies** or **Neuro‑MEDopathies**). The most clearly identifiable disease entity in the retrieved 2023–2024 evidence is **MED13L haploinsufficiency syndrome** (MRFACD; OMIM/MIM #616789; ORPHA:369891). Other closely related entities in the retrieved evidence include MED13-associated intellectual developmental disorder (MRD61), recessive MED23‑related MRT18, and recessive MED27‑related ponto‑cerebello‑lental degeneration. (maroofian2023biallelicmed27variants pages 3-4, siavriene2023molecularandfunctional pages 1-2, plassche2021med12related(neuro)developmentaldisorders pages 1-3)

A high-value 2023–2024 theme is that **sequence-level interpretation and functional follow-up** (e.g., transcript/protein assays, cell models) are increasingly used to support pathogenicity and refine genotype–phenotype correlations, while patient-advocacy organizations are explicitly organizing trial-readiness roadmaps (e.g., MED13L Foundation 2024 strategic research plan). (siavriene2023molecularandfunctional pages 1-2, heilmann2024themed13lfoundation pages 1-1)

## 1. Disease information

### 1.1 What is the disease?
**Mediator complex neurodevelopmental disorders (MEDopathies)** are neurodevelopmental conditions resulting from disrupted Mediator complex function, leading to dysregulated RNA polymerase II–dependent transcription programs important for brain development. Mechanistically, Mediator is described as “a large, evolutionarily conserved multiprotein complex” that “plays a critical role in facilitating transcriptional regulation by acting as a physical and functional bridge between DNA‑binding transcription factors and the transcriptional machinery.” (maroofian2023biallelicmed27variants pages 3-4)

Because clinical usage and coding tend to be gene-centric, this umbrella is most actionable in practice as a set of **gene-defined syndromes** (e.g., MED13L syndrome/MRFACD; MED12 syndromes; MED27 recessive neurodegeneration/NDD). (maroofian2023biallelicmed27variants pages 3-4, plassche2021med12related(neuro)developmentaldisorders pages 1-3, siavriene2023molecularandfunctional pages 1-2)

### 1.2 Key identifiers (as available in retrieved sources)
- **MED13L haploinsufficiency syndrome / MRFACD**: **OMIM/MIM #616789**; **ORPHA:369891** (siavriene2023molecularandfunctional pages 1-2)
- Representative Mediator-subunit gene MIM IDs referenced in MEDopathy literature include **MED23 (MIM 605042)** and **MED13 (MIM 603808)** and others (e.g., MED17/20/25/11). (maroofian2023biallelicmed27variants pages 3-4, salzano2023casereportnovel pages 1-2, tolmacheva2024expandingphenotypeof pages 1-2)

**Not found in retrieved evidence:** MONDO ID, ICD‑10/ICD‑11 code, MeSH descriptor for a single umbrella entity. (siavriene2023molecularandfunctional pages 1-2)

### 1.3 Common synonyms/alternative names
- **MEDopathies**; **Neuro‑MEDopathies** (umbrella) (maroofian2023biallelicmed27variants pages 3-4)
- **MED13L haploinsufficiency syndrome**, **MED13L syndrome**, **MED13L-related intellectual disability**, **MRFACD** (“mental retardation and distinctive facial features with or without cardiac defects”) (siavriene2023molecularandfunctional pages 1-2, bessenyei2022med13lrelatedintellectualdisability pages 1-2)

### 1.4 Evidence sources (individual vs aggregated)
The retrieved evidence is primarily:
- **Case reports/case series** and genotype-first matchmaker collaborations (MED13, MED23, MED27, MED13L). (tolmacheva2024expandingphenotypeof pages 1-2, salzano2023casereportnovel pages 1-2, maroofian2023biallelicmed27variants pages 3-4)
- **Aggregated research programs/registries**: Simons Searchlight (large prospective observational program including MED13L and MED13). (NCT01238250 chunk 1, NCT01238250 chunk 2)
- **Patient-advocacy strategic planning** for trial readiness: MED13L Foundation SRP (2024). (heilmann2024themed13lfoundation pages 1-1)

## 2. Etiology

### 2.1 Disease causal factors
Primary causal factors are **germline pathogenic variants** in genes encoding Mediator complex subunits. The causal chain is typically: variant → altered Mediator subunit abundance/function/localization → altered Pol II transcriptional regulation → disrupted neurodevelopmental programs → developmental delay/ID and syndromic features. (maroofian2023biallelicmed27variants pages 3-4, plassche2021med12related(neuro)developmentaldisorders pages 1-3, hamada2023med13landits pages 2-2)

### 2.2 Risk factors
- **Genetic**: pathogenic variants in Mediator genes (e.g., MED13L, MED13, MED12, MED23, MED27). (siavriene2023molecularandfunctional pages 1-2, tolmacheva2024expandingphenotypeof pages 1-2, plassche2021med12related(neuro)developmentaldisorders pages 1-3, salzano2023casereportnovel pages 1-2, maroofian2023biallelicmed27variants pages 3-4)
- **Familial recurrence mechanisms**: parental mosaicism can confer recurrence risk even in ostensibly de novo disorders (documented for MED13L). (bessenyei2022med13lrelatedintellectualdisability pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No protective variants or robust gene–environment interactions were identified in the retrieved evidence for these Mendelian conditions. (siavriene2023molecularandfunctional pages 1-2)

## 3. Phenotypes (clinical features)

### 3.1 Cross-MEDopathy phenotype themes
Across Mediator-subunit disorders, convergent features include **global developmental delay/intellectual disability, hypotonia, epilepsy, speech disorders, and behavioral comorbidity**, with additional gene-specific systemic features (e.g., cataracts in MED27; congenital anomalies in MED13 and MED13L). (maroofian2023biallelicmed27variants pages 3-4, fazio2025geneticclinicaland pages 22-24)

### 3.2 MED13L haploinsufficiency syndrome (MRFACD; OMIM/MIM #616789)
A 2023 MED13L paper succinctly states: “**Heterozygous pathogenic variants in the MED13L gene cause impaired intellectual development and distinctive facial features with or without cardiac defects (MIM #616789).**” (siavriene2023molecularandfunctional pages 1-2)

Typical features described across MED13L sources include:
- Neurodevelopment: intellectual disability/developmental delay; marked speech delay/poor speech (siavriene2023molecularandfunctional pages 1-2, bessenyei2022med13lrelatedintellectualdisability pages 1-2)
- Neuromuscular: hypotonia; motor delay (bessenyei2022med13lrelatedintellectualdisability pages 1-2)
- Craniofacial gestalt/dysmorphism: “distinctive facial features” (siavriene2023molecularandfunctional pages 1-2)
- Variable congenital anomalies: plagiocephaly, strabismus, clubfoot (siavriene2023molecularandfunctional pages 1-2)
- Cardiac: variable congenital heart defects (“with or without cardiac defects”) (siavriene2023molecularandfunctional pages 1-2)

**Suggested HPO terms (non-exhaustive, mapped to the described features):**
- Intellectual disability: HP:0001249
- Global developmental delay: HP:0001263
- Speech delay / severe expressive language impairment: HP:0000750, HP:0002463
- Hypotonia: HP:0001252
- Strabismus: HP:0000486
- Plagiocephaly: HP:0001357
- Talipes equinovarus (clubfoot): HP:0001762
- Congenital heart defect: HP:0001627

### 3.3 MED27-related disease: quantitative phenotype frequencies
A 2023 Brain cohort study (57 affected individuals, 30 families) reports a broad continuum from developmental epileptic-dyskinetic encephalopathy to variable NDD with movement abnormalities and provides quantitative frequencies, e.g., **global developmental delay/intellectual disability (100%)**, **bilateral cataracts (89%)**, **infantile hypotonia (74%)**, **microcephaly (62%)**, **gait ataxia (63%)**, **dystonia (61%)**, **epilepsy (50%)**, **limb spasticity (51%)**, and **death before adulthood (16%)**; MRI features include **cerebellar atrophy (100%)** and white matter volume loss (76.4%). (maroofian2023biallelicmed27variants pages 3-4)

Visual evidence for these frequencies is captured from the paper’s Table/Figure. (maroofian2023biallelicmed27variants media 55f96031, maroofian2023biallelicmed27variants media 45999b07)

**Suggested HPO terms:** cataract (HP:0000518), cerebellar atrophy (HP:0001272), dystonia (HP:0001332), spasticity (HP:0001257), epilepsy (HP:0001250), microcephaly (HP:0000252), ataxia (HP:0001251).

### 3.4 MED23-related MRT18 (autosomal recessive)
A 2023 case report/review states: “**Biallelic loss-of-function variants in MED23 cause a recessive syndromic intellectual disability condition with or without epilepsy (MRT18).**” and highlights postnatal progressive microcephaly as an underappreciated feature. (salzano2023casereportnovel pages 1-2)

**Suggested HPO terms:** autosomal recessive inheritance (HP:0000007), progressive microcephaly (HP:0000253), seizures (HP:0001250), hypotonia (HP:0001252), spasticity (HP:0001257), dystonia (HP:0001332).

### 3.5 MED13-associated NDD (MRD61): 2024 phenotype expansion
A 2024 BMC Medical Genomics case report describes an infant with a de novo MED13 missense variant identified by trio WES and proposes expanding the MED13-associated phenotype to include severe multisystem findings and neonatal death in rare cases. (tolmacheva2024expandingphenotypeof pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genes (representative, from retrieved evidence)
- **MED13L** (autosomal dominant, typically de novo; haploinsufficiency) (siavriene2023molecularandfunctional pages 1-2, bessenyei2022med13lrelatedintellectualdisability pages 1-2)
- **MED13** (autosomal dominant; de novo and inherited variants described) (tolmacheva2024expandingphenotypeof pages 1-2, yang2025anovelframeshift pages 7-7)
- **MED12** (X-linked spectrum: FG syndrome, Lujan–Fryns, X-linked Ohdo; and female de novo LoF in Hardikar) (plassche2021med12related(neuro)developmentaldisorders pages 1-3)
- **MED23** (autosomal recessive MRT18) (salzano2023casereportnovel pages 1-2)
- **MED27** (autosomal recessive NDD/neurodegeneration spectrum) (maroofian2023biallelicmed27variants pages 3-4)

A compact map is provided in the table below.

| Gene | Disorder name(s) / synonyms | Key identifier(s) | Inheritance pattern | Hallmark phenotypes (with frequencies if reported) | Key references |
|---|---|---|---|---|---|
| **MED13L** | **MED13L haploinsufficiency syndrome**; **MED13L-related intellectual disability**; **MRFACD** (*mental retardation and distinctive facial features with or without cardiac defects*) | **MIM/OMIM #616789**; **ORPHA:369891**; gene **MED13L MIM 608771** | **Autosomal dominant**, usually **de novo heterozygous** LoF/CNV; parental mosaicism reported | Core syndrome includes intellectual disability/developmental delay, **marked speech delay/poor speech**, hypotonia, motor delay, characteristic facial gestalt, with **cardiac defects variably present**; 2023 functional study also lists plagiocephaly, strabismus, clubfoot, macrostomia; review notes missense variants may be more severe and associated with epilepsy/absent speech/walking; one review states ~**one-third** of reported pathogenic events are large CNVs; no robust pooled prevalence of CHD or speech impairment was given in the gathered evidence (siavriene2023molecularandfunctional pages 1-2, tørring2019ismed13lrelatedintellectual pages 1-5, bessenyei2022med13lrelatedintellectualdisability pages 1-2, fazio2025geneticclinicaland pages 11-13) | **Siavrienė et al. 2023**, *Medicina*, doi:10.3390/medicina59071225, https://doi.org/10.3390/medicina59071225, PMID: ; **Tørring et al. 2019**, *Eur J Med Genet*, doi:10.1016/j.ejmg.2018.06.014, https://doi.org/10.1016/j.ejmg.2018.06.014, PMID: ; **Bessenyei et al. 2022**, *Cold Spring Harb Mol Case Stud*, doi:10.1101/mcs.a006124, https://doi.org/10.1101/mcs.a006124, PMID:  (siavriene2023molecularandfunctional pages 1-2, tørring2019ismed13lrelatedintellectual pages 1-5, bessenyei2022med13lrelatedintellectualdisability pages 1-2, fazio2025geneticclinicaland pages 11-13) |
| **MED13** | **MED13-associated neurodevelopmental disorder**; **intellectual developmental disorder-61 / MRD61** | gene **MED13 OMIM/MIM 603808**; disorder termed **MRD61** in later literature | Predominantly **autosomal dominant**, largely **de novo heterozygous** variants; inherited transmission from affected mother also reported | Universal DD/ID in original cohort; prominent **speech/language delay**, autism/ADHD in some, hypotonia, optic nerve/vision abnormalities, Duane anomaly, mild congenital heart anomalies, dysmorphism; variant types include truncating, missense, in-frame deletion; 2024 neonatal case expanded phenotype to hydrocephalic changes, hypoplastic corpus callosum, optic nerve/chiasm atrophy, brainstem atrophy, multiple organ failure/neonatal death (tolmacheva2024expandingphenotypeof pages 1-2) | **Blok et al. 2018**, *Hum Genet*, doi:10.1007/s00439-018-1887-y, https://doi.org/10.1007/s00439-018-1887-y, PMID: ; **Tolmacheva et al. 2024**, *BMC Med Genomics*, doi:10.1186/s12920-024-01857-z, https://doi.org/10.1186/s12920-024-01857-z, PMID:  (tolmacheva2024expandingphenotypeof pages 1-2) |
| **MED23** | **MED23-related intellectual disability**; **MRT18**; recessive syndromic intellectual disability with/without epilepsy | **MED23 MIM 605042**; **MRT18** | **Autosomal recessive**, **biallelic** pathogenic variants | Classical phenotype includes global DD/ID, **microcephaly**, axial hypotonia, spasticity, choreoathetosis/dystonia, EEG abnormalities and epilepsy; 2023 report emphasized **postnatal progressive microcephaly** as an underappreciated feature; due to rarity, phenotype frequencies remain limited (salzano2023casereportnovel pages 1-2) | **Salzano et al. 2023**, *Front Neurol*, doi:10.3389/fneur.2023.1090082, https://doi.org/10.3389/fneur.2023.1090082, PMID:  (salzano2023casereportnovel pages 1-2) |
| **MED27** | **MED27-associated neurodevelopmental disorder**; **variable ponto-cerebello-lental degeneration with movement disorders**; part of **Neuro-MEDopathies** | gene **MED27**; no OMIM/ORPHA identifier provided in gathered evidence | **Autosomal recessive**, **biallelic** pathogenic variants | Large 2023 series reported **global DD/ID 100%**, **bilateral cataracts 89%**, **infantile hypotonia 74%**, **microcephaly 62%**, **gait ataxia 63%**, **dystonia 61%**, **epilepsy 50%**, **limb spasticity 51%**, **facial dysmorphism 38%**, **death before adulthood 16%**; MRI: **cerebellar atrophy 100%**, white-matter volume loss **76.4%**, pontine hypoplasia **47.2%**, basal ganglia atrophy/signal changes **44.4%** (maroofian2023biallelicmed27variants pages 3-4) | **Maroofian et al. 2023**, *Brain*, doi:10.1093/brain/awad257, https://doi.org/10.1093/brain/awad257, PMID:  (maroofian2023biallelicmed27variants pages 3-4) |
| **MED12** | **MED12-related disorders** including **FG syndrome / Opitz-Kaveggia syndrome**, **Lujan-Fryns syndrome**, **X-linked Ohdo syndrome (Maat-Kievit-Brunner type)**, **non-syndromic X-linked intellectual disability**, and **Hardikar syndrome** | **FG syndrome MIM 305450**; **Lujan-Fryns syndrome MIM 309520**; **X-linked Ohdo syndrome MIM 300895**; gene **MED12** at **Xq13.1** | Mainly **X-linked**; classically **hemizygous inherited missense variants in males** from carrier mothers; also **de novo missense or truncating variants in females**; Hardikar syndrome linked to **de novo nonsense/LoF** in females | Shared features across classical MED12 syndromes include **intellectual disability**, hypotonia, macrocephaly, hyperactivity/behavioral abnormalities, corpus callosum abnormalities, and characteristic craniofacial features; Hardikar syndrome adds facial clefting, pigmentary retinopathy, biliary anomalies, intestinal malrotation; more C-terminal truncations associated with severe syndromic ID in females (plassche2021med12related(neuro)developmentaldisorders pages 1-3) | **van de Plassche & de Brouwer 2021**, *Genes*, doi:10.3390/genes12050663, https://doi.org/10.3390/genes12050663, PMID:  (plassche2021med12related(neuro)developmentaldisorders pages 1-3) |
| **Multiple Mediator subunits** | **MEDopathies / Neuro-MEDopathies** (umbrella term for Mediator-complex neurodevelopmental disorders) | Examples listed in gathered evidence: **MED11 MIM 612383**, **MED17 MIM 603810**, **MED20 MIM 612915**, **MED23 MIM 605042**, **MED25 MIM 610197**, **MED12L MIM 611318**, **MED13 MIM 603808**, **MED13L** | Mixed: **AR**, **AD/de novo**, **X-linked** depending on subunit | Convergent features across the group include developmental delay/intellectual disability, hypotonia, epilepsy, speech/language disorder, autism/behavioral comorbidity, and variable structural brain/cardiac anomalies; the Mediator complex acts as a bridge between DNA-binding transcription factors and RNA polymerase II transcriptional machinery (maroofian2023biallelicmed27variants pages 3-4, fazio2025geneticclinicaland pages 24-24) | **Maroofian et al. 2023**, *Brain*, doi:10.1093/brain/awad257, https://doi.org/10.1093/brain/awad257, PMID: ; **Fazio et al. 2025**, *Genes*, doi:10.3390/genes16121444, https://doi.org/10.3390/genes16121444, PMID:  (maroofian2023biallelicmed27variants pages 3-4, fazio2025geneticclinicaland pages 24-24) |


*Table: This table summarizes Mediator-complex neurodevelopmental disorders mentioned in the gathered evidence, highlighting identifiers, inheritance, hallmark phenotypes, and key references. It is useful as a compact disease-entity map for comparing major MEDopathy subtypes relevant to diagnosis and curation.*

### 4.2 Variant classes and functional consequences (examples)
**MED13L haploinsufficiency**
- 2023 intragenic deletion spanning exons 3–10 predicted truncation (frameshift) and haploinsufficiency; functional follow-up after MED13L silencing found “reduced cell viability; an accelerated aging process; and inhibition of the RB1, E2F1, and CCNC gene expression.” (siavriene2023molecularandfunctional pages 1-2)

**MED13 (CDK8 module-associated)**
- A 2018 cohort described truncating and missense variants, with non-truncating variants clustering in regions involved in ubiquitination/degradation (p.Thr326/p.Pro327), supporting variant-class dependent mechanisms. (yang2025anovelframeshift pages 7-7)

## 5. Environmental information
No specific environmental/lifestyle/infectious contributors were identified in the retrieved evidence for these Mendelian disorders. (siavriene2023molecularandfunctional pages 1-2)

## 6. Mechanism / pathophysiology

### 6.1 Core concept: Mediator as transcriptional bridge
The Mediator complex functions as a transcriptional regulator, “acting as a physical and functional bridge between DNA-binding transcription factors and the transcriptional machinery.” (maroofian2023biallelicmed27variants pages 3-4)

### 6.2 MED13L neurodevelopmental mechanisms (model evidence)
Two lines of mechanistic evidence in the retrieved sources support neuronal roles for MED13L:

1) **Developmental expression + synaptic localization (mouse)**
- MED13L shows developmental stage-dependent expression/localization in mouse brain and “at least partially colocalized with pre- and post-synaptic markers, synaptophysin, and PSD95,” suggesting synaptic involvement. (hamada2021expressionanalysesof pages 1-2)

2) **Corticogenesis/dendrite development (in utero electroporation; 2023)**
- Disease-associated MED13L variants show **distinct subcellular localization** in cortical neurons (some nuclear accumulation; others cytoplasmic), and a truncation variant was “barely detectable,” consistent with haploinsufficiency. (hamada2023med13landits pages 2-2)
- Functionally, MED13L knockdown “abrogated dendritic growth in vivo,” and dendritic growth was rescued by RNAi-resistant wild-type MED13L, but not equivalently by certain disease variants. (hamada2023med13landits pages 2-2)

**Suggested GO Biological Process terms (mechanism-aligned):**
- Regulation of transcription by RNA polymerase II (GO:0006357)
- Neuron projection development (GO:0031175)
- Dendrite development (GO:0016358)
- Synapse organization (GO:0050808)

**Suggested Cell Ontology (CL) cell types:**
- Cortical pyramidal neuron (CL:0000540; used as proxy for “cortical layer II/III pyramidal neurons” described experimentally) (hamada2023med13landits pages 2-2)
- Neural progenitor cell (CL:0000047; mechanistically implicated broadly in NDD studies, though not directly quantified in retrieved excerpts)

## 7. Anatomical structures affected
Primary involvement is the **central nervous system**. In MED27 disease, neuroimaging commonly shows **cerebellar atrophy** and additional brainstem/white matter changes. (maroofian2023biallelicmed27variants pages 3-4)

**Suggested UBERON terms:**
- Brain (UBERON:0000955)
- Cerebellum (UBERON:0002037)
- Cerebral cortex (UBERON:0001851)

## 8. Temporal development
Most MEDopathies present as **early-onset neurodevelopmental disorders** (infancy/childhood), with developmental delay and evolving neurologic manifestations (e.g., epilepsy, movement disorder) depending on the gene. (maroofian2023biallelicmed27variants pages 3-4, siavriene2023molecularandfunctional pages 1-2)

## 9. Inheritance and population

### 9.1 Inheritance patterns (from retrieved evidence)
- Autosomal dominant (often de novo): MED13L, MED13 (siavriene2023molecularandfunctional pages 1-2, tolmacheva2024expandingphenotypeof pages 1-2)
- X-linked spectrum: MED12-related disorders (plassche2021med12related(neuro)developmentaldisorders pages 1-3)
- Autosomal recessive: MED23, MED27 (salzano2023casereportnovel pages 1-2, maroofian2023biallelicmed27variants pages 3-4)

### 9.2 Epidemiology
The retrieved sources do **not** provide rigorous prevalence/incidence estimates for the umbrella “Mediator Complex Neurodevelopmental Disorder.” For MED13L syndrome, one source notes “roughly a hundred reported cases” and that it is among the more common syndromic intellectual disabilities, but this is not a population prevalence estimate. (bessenyei2022med13lrelatedintellectualdisability pages 1-2)

## 10. Diagnostics

### 10.1 Genetic testing approaches in current practice (as reflected in retrieved evidence)
- **Chromosomal microarray / SNP-CGH (CNV detection)** is used when congenital anomalies and/or syndromic NDD is suspected (e.g., MED13L intragenic deletion characterized by SNP-CGH and breakpoint refinement). (siavriene2023molecularandfunctional pages 1-2)
- **Trio whole-exome sequencing (WES)** is emphasized for de novo variant detection in syndromic NDD and congenital anomalies (e.g., MED13 2024 phenotype expansion). (tolmacheva2024expandingphenotypeof pages 1-2)
- **Confirmatory methods**: qPCR, Sanger sequencing (including cDNA), Western blot. (siavriene2023molecularandfunctional pages 1-2)

### 10.2 Emerging/adjacent diagnostics
- **Functional characterization** in patient-derived fibroblasts and CRISPR perturbation experiments are being used to support variant interpretation in MED13L. (siavriene2023molecularandfunctional pages 1-2)

### 10.3 Differential diagnosis (examples)
Given shared phenotypes (DD/ID, speech impairment, hypotonia, dysmorphism, congenital anomalies), differential diagnoses include other syndromic NDDs; Mediator-subunit disorders themselves can overlap (e.g., MED13 vs MED13L; MED12 spectrum). (maroofian2023biallelicmed27variants pages 3-4, plassche2021med12related(neuro)developmentaldisorders pages 1-3, tolmacheva2024expandingphenotypeof pages 1-2)

## 11. Outcome / prognosis
Robust longitudinal survival/functional outcome statistics were not available in the retrieved evidence for the umbrella entity. Notably, MED27 disease includes a reported **16% death before adulthood** in a large cohort, underscoring gene-specific prognosis differences within MEDopathies. (maroofian2023biallelicmed27variants pages 3-4)

## 12. Treatment

### 12.1 Current management
No disease-modifying therapies for MED13L/MED13/MED23/MED27 disorders were identified in the retrieved sources; management is generally supportive and symptom-directed (developmental therapies; seizure management where applicable). (fazio2025geneticclinicaland pages 22-24, siavriene2023molecularandfunctional pages 1-2)

**Suggested MAXO terms (supportive, typical for syndromic NDD):**
- Developmental therapy / early intervention (MAXO:0000942; proxy)
- Speech therapy (MAXO:0000717; proxy)
- Physical therapy (MAXO:0000010; proxy)
- Antiseizure therapy (MAXO:0000647; proxy)

### 12.2 2023–2024 translational/trial-readiness developments
- The **MED13L Foundation strategic research plan (SRP)** (published Jan 2024) frames clinical-trial readiness as an explicit goal, assessing preclinical tools “largely framed through Food and Drug Administration guidelines for the development of therapeutics from bench to bedside.” (heilmann2024themed13lfoundation pages 1-1)

## 13. Prevention
Primary prevention is not applicable in the usual public-health sense for de novo Mendelian disorders; prevention is chiefly via **genetic counseling and reproductive options**.

- **Genetic counseling** should explicitly consider **parental mosaicism** as a recurrence-risk mechanism (documented in MED13L). (bessenyei2022med13lrelatedintellectualdisability pages 1-2)
- Prenatal/preimplantation options are implied by standard practice but were not detailed with rates or protocols in retrieved evidence. (bessenyei2022med13lrelatedintellectualdisability pages 1-2)

## 14. Other species / natural disease
Not addressed in the retrieved evidence.

## 15. Model organisms
- **Mouse neurodevelopmental models**: MED13L expression/localization during mouse brain development (ventricular zone, cortical plate, hippocampus/cerebellum; synaptic colocalization) and in utero electroporation experiments showing dendritic-development phenotypes. (hamada2021expressionanalysesof pages 1-2, hamada2023med13landits pages 2-2)
- **Cell models**: primary cultured hippocampal neurons (localization), fibroblast CRISPR silencing (functional consequences for MED13L). (hamada2021expressionanalysesof pages 1-2, siavriene2023molecularandfunctional pages 1-2)

## Real-world implementations and applications (2023–2024 emphasis)
1) **Clinical sequencing workflows**: integration of CNV arrays + WES (often trio) to identify Mediator-subunit etiologies in syndromic NDD/congenital anomalies (demonstrated in MED13L 2023 functional CNV paper and MED13 2024 case). (siavriene2023molecularandfunctional pages 1-2, tolmacheva2024expandingphenotypeof pages 1-2)
2) **Research registries**: **Simons Searchlight** is a large, remote, prospective observational program enrolling individuals with gene variants including **MED13L** and **MED13**, collecting medical/behavioral/developmental data longitudinally; it reports ~7,000 participants already enrolled and plans up to 100,000. URL: https://simonssearchlight.org/ (trial record first posted 2010-11-10; last update posted 2025-06-06). (NCT01238250 chunk 1, NCT01238250 chunk 2)
3) **Trial readiness infrastructure**: MED13L Foundation SRP (Jan 2024; Therapeutic Advances in Rare Disease; https://doi.org/10.1177/26330040241290252). (heilmann2024themed13lfoundation pages 1-1)

## Notable statistics (from recent studies)
- **MED27 cohort (Brain 2023)**: DD/ID 100%, bilateral cataracts 89%, hypotonia 74%, microcephaly 62%, gait ataxia 63%, dystonia 61%, epilepsy 50%, death before adulthood 16%; MRI cerebellar atrophy 100%. (maroofian2023biallelicmed27variants pages 3-4, maroofian2023biallelicmed27variants media 55f96031, maroofian2023biallelicmed27variants media 45999b07)
- **MED23 rarity**: literature still small; 2023 report notes limited number of reported individuals and variants and highlights postnatal progressive microcephaly. (salzano2023casereportnovel pages 1-2)

## Limitations of this report (evidence availability)
- The retrieved sources did not provide MONDO/ICD/MeSH identifiers for the umbrella “Mediator Complex Neurodevelopmental Disorder.” (siavriene2023molecularandfunctional pages 1-2)
- Many claims requested by the template (population prevalence/incidence, standardized clinical diagnostic criteria, treatment response rates) were not available in the retrieved evidence and would require targeted retrieval from OMIM/Orphanet pages and additional natural history cohorts beyond the currently retrieved texts. (siavriene2023molecularandfunctional pages 1-2)



References

1. (maroofian2023biallelicmed27variants pages 3-4): R. Maroofian, R. Kaiyrzhanov, E. Calì, M. Zamani, M. Zaki, Matteo P. Ferla, D. Tortora, Saeid Sadeghian, Saadia Maryam Saadi, Uzma Abdullah, Ehsan Ghayoor Karimiani, S. Efthymiou, G. Yeşil, Shahryar Alavi, Aisha Al Shamsi, H. Tajsharghi, M. Abdel-Hamid, N. Saadi, F. Al Mutairi, Lama Alabdi, C. Beetz, Zafar Ali, M. B. Toosi, S. Rudnik-Schöneborn, Meisam Babaei, P. Isohanni, Jameel Muhammad, Khan Sheraz, Maha Al Shalan, S. Hickey, Daphna Marom, E. Elhanan, M. Kurian, Dana Marafi, A. Saberi, M. Hamid, R. Spaull, Linyan Meng, S. Lalani, S. Maqbool, F. Rahman, J. Seeger, T. Palculict, Tracy Lau, D. Murphy, N. Mencacci, K. Steindl, A. Begemann, A. Rauch, Sinan Akbaş, Aslanger Ayça Dilruba, V. Salpietro, Hammad Yousaf, S. Ben-Shachar, K. Ejeskär, A. A. Al Aqeel, F. High, Amy Armstrong-Javors, Seyed Mohammadsaleh Zahraei, Tahereh Seifi, Jawaher Zeighami, G. Shariati, A. Sedaghat, S. N. Asl, Mohmmad Shahrooei, G. Zifarelli, L. Burglen, C. Ravelli, J. Zschocke, Ulrich A. Schatz, Maryam Ghavideldarestani, W. Kamel, H. Van Esch, A. Hackenberg, Jenny C. Taylor, L. Al-Gazali, P. Bauer, Joseph J Gleeson, F. Alkuraya, J. Lupski, H. Galehdari, Reza Azizimalamiri, Wendy K. Chung, S. Baig, H. Houlden, and M. Severino. Biallelic med27 variants lead to variable ponto-cerebello-lental degeneration with movement disorders. Brain, 146:5031-5043, Jul 2023. URL: https://doi.org/10.1093/brain/awad257, doi:10.1093/brain/awad257. This article has 19 citations and is from a highest quality peer-reviewed journal.

2. (siavriene2023molecularandfunctional pages 1-2): Evelina Siavrienė, Gunda Petraitytė, Violeta Mikštienė, Živilė Maldžienė, Aušra Sasnauskienė, Vilmantė Žitkutė, Laima Ambrozaitytė, Tautvydas Rančelis, Algirdas Utkus, Vaidutis Kučinskas, and Eglė Preikšaitienė. Molecular and functional characterisation of a novel intragenic 12q24.21 deletion resulting in med13l haploinsufficiency syndrome. Medicina, 59:1225, Jun 2023. URL: https://doi.org/10.3390/medicina59071225, doi:10.3390/medicina59071225. This article has 9 citations.

3. (plassche2021med12related(neuro)developmentaldisorders pages 1-3): Stijn R. van de Plassche and Arjan P. M. de Brouwer. Med12-related (neuro)developmental disorders: a question of causality. Genes, 12 5:663, Apr 2021. URL: https://doi.org/10.3390/genes12050663, doi:10.3390/genes12050663. This article has 26 citations.

4. (heilmann2024themed13lfoundation pages 1-1): Rachel Heilmann, Anna Pfalzer, Terry Jo Bichell, Ananya Terala, Alicia Campbell, Dylan Taatjes, Jamal Ghoumid, Chad Grueter, Jennifer Bain, Randy Strich, Vanessa Dias, Kimberly Sokorai, Nicholas Seaver, Kelly Sexton, and Kathleen Boychuck. The med13l foundation strategic research plan: a roadmap to the future. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241290252, doi:10.1177/26330040241290252. This article has 9 citations.

5. (salzano2023casereportnovel pages 1-2): Emanuela Salzano, Marcello Niceta, Simone Pizzi, Francesca Clementina Radio, Martina Busè, Francesca Mercadante, Sabina Barresi, Arturo Ferrara, Cecilia Mancini, Marco Tartaglia, and Maria Piccione. Case report: novel compound heterozygosity for pathogenic variants in med23 in a syndromic patient with postnatal microcephaly. Frontiers in Neurology, Feb 2023. URL: https://doi.org/10.3389/fneur.2023.1090082, doi:10.3389/fneur.2023.1090082. This article has 4 citations and is from a peer-reviewed journal.

6. (tolmacheva2024expandingphenotypeof pages 1-2): Ekaterina Tolmacheva, Anna S. Bolshakova, Jekaterina Shubina, Margarita S. Rogacheva, Alexey N. Ekimov, Julia L. Podurovskaya, Artem A. Burov, Denis V. Rebrikov, Vladimir G. Bychenko, Dmitry Yu. Trofimov, and Gennady T. Sukhikh. Expanding phenotype of med13-associated syndrome presenting novel de novo missense variant in a patient with multiple congenital anomalies. BMC Medical Genomics, May 2024. URL: https://doi.org/10.1186/s12920-024-01857-z, doi:10.1186/s12920-024-01857-z. This article has 8 citations and is from a peer-reviewed journal.

7. (bessenyei2022med13lrelatedintellectualdisability pages 1-2): Beáta Bessenyei, István Balogh, Attila Mokánszki, Anikó Ujfalusi, Rolph Pfundt, and Katalin Szakszon. Med13l-related intellectual disability due to paternal germinal mosaicism. Cold Spring Harbor Molecular Case Studies, 8:a006124, Oct 2022. URL: https://doi.org/10.1101/mcs.a006124, doi:10.1101/mcs.a006124. This article has 16 citations and is from a peer-reviewed journal.

8. (NCT01238250 chunk 1):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

9. (NCT01238250 chunk 2):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

10. (hamada2023med13landits pages 2-2): Nanako Hamada, Ikuko Iwamoto, and Koh‐ichi Nagata. <scp>med13l</scp> and its disease‐associated variants influence the dendritic development of cerebral cortical neurons in the mammalian brain. Journal of Neurochemistry, 165:334-347, Feb 2023. URL: https://doi.org/10.1111/jnc.15783, doi:10.1111/jnc.15783. This article has 15 citations and is from a domain leading peer-reviewed journal.

11. (fazio2025geneticclinicaland pages 22-24): Alessandro Fazio, Roberta Leonardi, Lorenzo Aliotta, Manuela Lo Bianco, Gennaro Anastasio, Giuseppe Messina, Corrado Spatola, Pietro Valerio Foti, Stefano Palmucci, Antonio Basile, Martino Ruggieri, and Emanuele David. Genetic, clinical and neuroradiological spectrum of med-related disorders: an updated review. Genes, 16:1444, Dec 2025. URL: https://doi.org/10.3390/genes16121444, doi:10.3390/genes16121444. This article has 1 citations.

12. (maroofian2023biallelicmed27variants media 55f96031): R. Maroofian, R. Kaiyrzhanov, E. Calì, M. Zamani, M. Zaki, Matteo P. Ferla, D. Tortora, Saeid Sadeghian, Saadia Maryam Saadi, Uzma Abdullah, Ehsan Ghayoor Karimiani, S. Efthymiou, G. Yeşil, Shahryar Alavi, Aisha Al Shamsi, H. Tajsharghi, M. Abdel-Hamid, N. Saadi, F. Al Mutairi, Lama Alabdi, C. Beetz, Zafar Ali, M. B. Toosi, S. Rudnik-Schöneborn, Meisam Babaei, P. Isohanni, Jameel Muhammad, Khan Sheraz, Maha Al Shalan, S. Hickey, Daphna Marom, E. Elhanan, M. Kurian, Dana Marafi, A. Saberi, M. Hamid, R. Spaull, Linyan Meng, S. Lalani, S. Maqbool, F. Rahman, J. Seeger, T. Palculict, Tracy Lau, D. Murphy, N. Mencacci, K. Steindl, A. Begemann, A. Rauch, Sinan Akbaş, Aslanger Ayça Dilruba, V. Salpietro, Hammad Yousaf, S. Ben-Shachar, K. Ejeskär, A. A. Al Aqeel, F. High, Amy Armstrong-Javors, Seyed Mohammadsaleh Zahraei, Tahereh Seifi, Jawaher Zeighami, G. Shariati, A. Sedaghat, S. N. Asl, Mohmmad Shahrooei, G. Zifarelli, L. Burglen, C. Ravelli, J. Zschocke, Ulrich A. Schatz, Maryam Ghavideldarestani, W. Kamel, H. Van Esch, A. Hackenberg, Jenny C. Taylor, L. Al-Gazali, P. Bauer, Joseph J Gleeson, F. Alkuraya, J. Lupski, H. Galehdari, Reza Azizimalamiri, Wendy K. Chung, S. Baig, H. Houlden, and M. Severino. Biallelic med27 variants lead to variable ponto-cerebello-lental degeneration with movement disorders. Brain, 146:5031-5043, Jul 2023. URL: https://doi.org/10.1093/brain/awad257, doi:10.1093/brain/awad257. This article has 19 citations and is from a highest quality peer-reviewed journal.

13. (maroofian2023biallelicmed27variants media 45999b07): R. Maroofian, R. Kaiyrzhanov, E. Calì, M. Zamani, M. Zaki, Matteo P. Ferla, D. Tortora, Saeid Sadeghian, Saadia Maryam Saadi, Uzma Abdullah, Ehsan Ghayoor Karimiani, S. Efthymiou, G. Yeşil, Shahryar Alavi, Aisha Al Shamsi, H. Tajsharghi, M. Abdel-Hamid, N. Saadi, F. Al Mutairi, Lama Alabdi, C. Beetz, Zafar Ali, M. B. Toosi, S. Rudnik-Schöneborn, Meisam Babaei, P. Isohanni, Jameel Muhammad, Khan Sheraz, Maha Al Shalan, S. Hickey, Daphna Marom, E. Elhanan, M. Kurian, Dana Marafi, A. Saberi, M. Hamid, R. Spaull, Linyan Meng, S. Lalani, S. Maqbool, F. Rahman, J. Seeger, T. Palculict, Tracy Lau, D. Murphy, N. Mencacci, K. Steindl, A. Begemann, A. Rauch, Sinan Akbaş, Aslanger Ayça Dilruba, V. Salpietro, Hammad Yousaf, S. Ben-Shachar, K. Ejeskär, A. A. Al Aqeel, F. High, Amy Armstrong-Javors, Seyed Mohammadsaleh Zahraei, Tahereh Seifi, Jawaher Zeighami, G. Shariati, A. Sedaghat, S. N. Asl, Mohmmad Shahrooei, G. Zifarelli, L. Burglen, C. Ravelli, J. Zschocke, Ulrich A. Schatz, Maryam Ghavideldarestani, W. Kamel, H. Van Esch, A. Hackenberg, Jenny C. Taylor, L. Al-Gazali, P. Bauer, Joseph J Gleeson, F. Alkuraya, J. Lupski, H. Galehdari, Reza Azizimalamiri, Wendy K. Chung, S. Baig, H. Houlden, and M. Severino. Biallelic med27 variants lead to variable ponto-cerebello-lental degeneration with movement disorders. Brain, 146:5031-5043, Jul 2023. URL: https://doi.org/10.1093/brain/awad257, doi:10.1093/brain/awad257. This article has 19 citations and is from a highest quality peer-reviewed journal.

14. (yang2025anovelframeshift pages 7-7): Qi Yang, Qiang Zhang, Sheng Yi, Gaojie Huang, Xunzhao Zhou, Shang Yi, and Jingsi Luo. A novel frameshift variant in the med13 gene causing intellectual developmental disorder-61 in a chinese family. Frontiers in Pediatrics, Oct 2025. URL: https://doi.org/10.3389/fped.2025.1699544, doi:10.3389/fped.2025.1699544. This article has 1 citations.

15. (tørring2019ismed13lrelatedintellectual pages 1-5): Pernille Mathiesen Tørring, Martin Jakob Larsen, Charlotte Brasch-Andersen, Lotte Nylandsted Krogh, Maria Kibæk, Lone Laulund, Niels Illum, Ulrike Dunkhase-Heinl, Antje Wiesener, Bernt Popp, Giuseppe Marangi, Tina Duelund Hjortshøj, Jakob Ek, Ida Vogel, Naja Becher, Laura Roos, Marcella Zollino, and Christina Ringmann Fagerberg. Is med13l-related intellectual disability a recognizable syndrome? European journal of medical genetics, 62 2:129-136, Feb 2019. URL: https://doi.org/10.1016/j.ejmg.2018.06.014, doi:10.1016/j.ejmg.2018.06.014. This article has 46 citations and is from a peer-reviewed journal.

16. (fazio2025geneticclinicaland pages 11-13): Alessandro Fazio, Roberta Leonardi, Lorenzo Aliotta, Manuela Lo Bianco, Gennaro Anastasio, Giuseppe Messina, Corrado Spatola, Pietro Valerio Foti, Stefano Palmucci, Antonio Basile, Martino Ruggieri, and Emanuele David. Genetic, clinical and neuroradiological spectrum of med-related disorders: an updated review. Genes, 16:1444, Dec 2025. URL: https://doi.org/10.3390/genes16121444, doi:10.3390/genes16121444. This article has 1 citations.

17. (fazio2025geneticclinicaland pages 24-24): Alessandro Fazio, Roberta Leonardi, Lorenzo Aliotta, Manuela Lo Bianco, Gennaro Anastasio, Giuseppe Messina, Corrado Spatola, Pietro Valerio Foti, Stefano Palmucci, Antonio Basile, Martino Ruggieri, and Emanuele David. Genetic, clinical and neuroradiological spectrum of med-related disorders: an updated review. Genes, 16:1444, Dec 2025. URL: https://doi.org/10.3390/genes16121444, doi:10.3390/genes16121444. This article has 1 citations.

18. (hamada2021expressionanalysesof pages 1-2): Nanako Hamada, Ikuko Iwamoto, Masashi Nishikawa, and Koh-ichi Nagata. Expression analyses of mediator complex subunit 13-like: a responsible gene for neurodevelopmental disorders during mouse brain development. Developmental Neuroscience, 43:43-52, Apr 2021. URL: https://doi.org/10.1159/000515188, doi:10.1159/000515188. This article has 11 citations and is from a peer-reviewed journal.