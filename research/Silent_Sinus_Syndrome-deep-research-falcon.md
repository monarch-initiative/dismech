---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-30T20:26:16.165105'
end_time: '2026-04-30T20:39:59.282467'
duration_seconds: 823.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Silent Sinus Syndrome
  mondo_id: MONDO:0019108
  category: Complex
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
- **Disease Name:** Silent Sinus Syndrome
- **MONDO ID:** MONDO:0019108 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Silent Sinus Syndrome** covering all of the
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
- **Disease Name:** Silent Sinus Syndrome
- **MONDO ID:** MONDO:0019108 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Silent Sinus Syndrome** covering all of the
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


## Silent Sinus Syndrome (SSS) — Comprehensive Disease Characteristics Report

### Target disease
- **Disease name:** Silent sinus syndrome (SSS)
- **MONDO ID:** **MONDO:0019108** (provided by user)
- **Category:** Complex (acquired/anatomic-mechanistic syndrome)

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
Silent sinus syndrome (SSS) is a rare clinical-radiologic entity characterized by progressive collapse (atelectasis) of the maxillary sinus with associated inferior displacement (descent) of the orbital floor, producing **painless, progressive ipsilateral enophthalmos and/or hypoglobus**, often with minimal sinonasal symptoms. Representative definitions include:
- “**Spontaneous, painless enophthalmos, hypoglobus with orbital floor resorption and maxillary sinus collapse on the ipsilateral side**.” (Clarós 2019; URL: https://doi.org/10.1080/00016489.2018.1542161) (claros2019silentsinussyndrome pages 1-3)
- Diagnostic criteria summarized by de Dorlodot 2017 (attributed to Soparkar et al.) include “**modification of facial appearance, enophthalmos and/or hypoglobus, a reduction of maxillary sinus volume on computed tomography (CT) scan, and the absence of sinonasal symptoms**.” (de Dorlodot 2017; URL: https://doi.org/10.1007/s00405-017-4622-8) (dorlodot2017chronicmaxillaryatelectasis pages 1-2)

SSS is widely considered within the spectrum of **chronic maxillary atelectasis (CMA)**, sometimes described as an advanced form (e.g., type 3 CMA in some classification systems). (claros2019silentsinussyndrome pages 1-3, dorlodot2017chronicmaxillaryatelectasis pages 1-2)

### 1.2 Key identifiers
- **MONDO:** MONDO:0019108 (user-provided)
- **ICD-10 / ICD-11, MeSH, Orphanet, OMIM:** Not retrievable using the provided toolchain in this run; therefore **not reported here to avoid introducing uncited identifiers**.

### 1.3 Common synonyms / alternative names
Evidence-supported synonyms and closely related terms:
- **Chronic maxillary atelectasis (CMA)** (spectrum entity including SSS) (dorlodot2017chronicmaxillaryatelectasis pages 1-2)
- **Imploding antrum syndrome** (used in some literature traditions; referenced indirectly via criteria attribution to Soparkar et al.) (dorlodot2017chronicmaxillaryatelectasis pages 1-2)

### 1.4 Evidence-source type
Most SSS knowledge is derived from **aggregated clinical resources** (case series, systematic reviews, narrative reviews) and **individual case reports**, supported by **CT-based radiographic characterization**. (tousidonis2024contemporarytreatmentof pages 7-8, dorlodot2017chronicmaxillaryatelectasis pages 1-2, sivasubramaniam2011silentsinussyndrome pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic / anatomic)
Across recent reviews and classic series, the dominant etiologic model is **functional obstruction** of the maxillary sinus outflow pathway:
- Tousidonis 2024 describes the favored model: “**obstruction of the osteomeatal complex** … causes hypoventilation … accumulation of secretions that creates a **negative pressure** that leads to **atelectasis** of the sinus with **downward displacement of the orbital floor**.” (Tousidonis 2024; published Apr 2024; URL: https://doi.org/10.7759/cureus.57577) (tousidonis2024contemporarytreatmentof pages 7-8)
- Sivasubramaniam 2011 similarly describes osteomeatal occlusion → gas resorption → negative pressure → progressive maxillary atelectasis and orbital floor descent. (URL: https://doi.org/10.1017/S0022215111001952) (sivasubramaniam2011silentsinussyndrome pages 1-2)

### 2.2 Risk factors
#### Anatomic / local factors
- **Ostiomeatal complex / infundibular obstruction** (primary upstream factor). (tousidonis2024contemporarytreatmentof pages 7-8, lee2018silentsinussyndrome pages 1-4)

#### Trauma / iatrogenic (secondary SSS)
Strabbing 2025 explicitly defines secondary SSS as arising after trauma or surgery that disrupts mucociliary clearance, and reports a time-to-onset distribution:
- In 9 secondary SSS patients, the interval from trauma/surgery to SSS onset ranged **1–36 months**, with a **median of 3 months** in the post-traumatic group; **8/9 reported diplopia**. (Strabbing 2025; URL: https://doi.org/10.1007/s10006-025-01391-x) (strabbing2025posttraumaticandiatrogenic pages 1-2)

#### Systemic inflammatory/autoimmune causes (rare)
- Kramer 2024 presents what it describes as the **first reported instance** of **granulomatosis with polyangiitis (GPA)** causing SSS via sinonasal destructive disease producing obstruction: “**around 100 cases** of SSS have been reported so far” and this case is “**the first reported instance of GPA causing SSS**.” (Kramer 2024; published May 2024; URL: https://doi.org/10.7759/cureus.61442) (kramer2024granulomatosiswithpolyangiitis pages 1-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction data were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core symptom/sign phenotype spectrum
Common clinical manifestations reported across series and reviews include:
- **Enophthalmos** and **hypoglobus** (core defining signs) (claros2019silentsinussyndrome pages 1-3, dorlodot2017chronicmaxillaryatelectasis pages 1-2)
- **Orbital/facial asymmetry**, superior sulcus deepening, diminished malar projection (lee2018silentsinussyndrome pages 1-4, tousidonis2024contemporarytreatmentof pages 1-4)
- **Diplopia** (variable; common in some series) (strabbing2025posttraumaticandiatrogenic pages 1-2, sivasubramaniam2011silentsinussyndrome pages 1-2)

Recent review/case-based synthesis (Tousidonis 2024) adds less typical features that may appear:
- “facial hypoesthesia,” eyelid “retraction, ptosis, absent fold,” and dry eye. (tousidonis2024contemporarytreatmentof pages 7-8)

Quantitative clinical displacement estimates from a classic series:
- Sivasubramaniam 2011 cites ranges: **hypoglobus 2–6 mm** and **enophthalmos 2–5 mm**. (sivasubramaniam2011silentsinussyndrome pages 1-2)

### 3.2 Phenotype characteristics
- **Age of onset:** typically adult; often presenting in **third to fifth decades** in major series/reviews. (sivasubramaniam2011silentsinussyndrome pages 1-2, tousidonis2024contemporarytreatmentof pages 4-7, lee2018silentsinussyndrome pages 1-4)
- **Progression:** often described as **slow/progressive**, sometimes over years (Sivasubramaniam 2011; also reiterated in trial registry description). (sivasubramaniam2011silentsinussyndrome pages 1-2, NCT04388345 chunk 1)
- **Frequency among affected individuals:** high-quality population-level phenotype frequency data are not available in the retrieved evidence; in secondary SSS series, **diplopia occurred in 8/9**. (strabbing2025posttraumaticandiatrogenic pages 1-2)

### 3.3 Quality-of-life impact
The ClinicalTrials.gov registry case report notes that **diagnostic delay** “affected the patient lifestyle tremendously.” (NCT04388345 posted May 14, 2020; URL: https://clinicaltrials.gov/study/NCT04388345) (NCT04388345 chunk 1)

### 3.4 Suggested HPO terms (non-exhaustive)
(Provided as ontology suggestions; frequencies not established in retrieved sources.)
- Enophthalmos — **HP:0000654**
- Hypoglobus — **HP:0032007**
- Diplopia — **HP:0000651**
- Facial asymmetry — **HP:0000324**
- Ptosis — **HP:0000508**
- Nasal obstruction (when present, especially in secondary or comorbid CRS) — **HP:0001742**

---

## 4. Genetic / molecular information

### 4.1 Causal genes
No **validated causal genes** for SSS were identified in the retrieved evidence. SSS is primarily characterized as an **acquired/anatomic-mechanistic** entity (ostiomeatal obstruction-driven). (tousidonis2024contemporarytreatmentof pages 7-8, dorlodot2017chronicmaxillaryatelectasis pages 1-2)

### 4.2 Pathogenic variants / modifier genes / epigenetics / chromosomal abnormalities
Not reported in retrieved evidence.

### 4.3 Notable related immunogenetic associations (not SSS-specific)
In the rare etiologic context of GPA presenting with SSS-like anatomy, Kramer 2024 notes GPA genetic associations, including “**HLA-DPB1*0401 and HLA-DPB4**,” but these are **GPA** associations rather than established SSS susceptibility loci. (kramer2024granulomatosiswithpolyangiitis pages 5-7)

---

## 5. Environmental information

### 5.1 Environmental/lifestyle contributors
No lifestyle/toxin/radiation/pollution associations were identified in the retrieved evidence.

### 5.2 Iatrogenic exposures (procedural)
Trauma and prior surgery can precipitate **secondary SSS**; thus, prior orbital or midface procedures constitute relevant iatrogenic “exposures.” (strabbing2025posttraumaticandiatrogenic pages 1-2)

### 5.3 Infectious agents
SSS itself is not presented as a primary infectious disease. Infectious colonization is discussed indirectly in GPA context (e.g., elevated *S. aureus* carriage in GPA patients), which may contribute to inflammation/obstruction in that systemic disease. (kramer2024granulomatosiswithpolyangiitis pages 5-7)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (upstream → downstream)
A consolidated, evidence-based mechanistic model:
1. **Upstream trigger:** obstruction/closure of the **ostiomeatal complex** / infundibulum (anatomic narrowing, inflammation, post-traumatic/iatrogenic changes). (tousidonis2024contemporarytreatmentof pages 7-8, lee2018silentsinussyndrome pages 1-4)
2. **Sinus physiology change:** **hypoventilation** with gas resorption produces **subatmospheric (negative) pressure** in the maxillary sinus. (tousidonis2024contemporarytreatmentof pages 7-8, sivasubramaniam2011silentsinussyndrome pages 1-2)
3. **Tissue-level remodeling:** inward retraction/bowing of maxillary sinus walls → **maxillary atelectasis** and reduced sinus volume; sinus may become opacified (secretions/transudate). (dorlodot2017chronicmaxillaryatelectasis pages 1-2, sivasubramaniam2011silentsinussyndrome pages 1-2)
4. **Orbital consequences:** inferior displacement/thinning/dehiscence of orbital floor → increased orbital volume → **enophthalmos/hypoglobus** and sometimes **diplopia**. (dorlodot2017chronicmaxillaryatelectasis pages 1-2, sivasubramaniam2011silentsinussyndrome pages 1-2)

### 6.2 Cellular and bone remodeling hypotheses
Sheptulin 2024 summarizes competing hypotheses (pressure-driven remodeling vs subclinical inflammation). It cites animal evidence that a pressure drop of **~2 mmHg** could increase osteoclast activity, suggesting a potential pressure–bone remodeling link, while their sampled orbital-floor specimen showed **no osteoclastic activity** in that late-stage sample (implying remodeling may be earlier). (Sheptulin 2024; published Dec 2024; URL: https://doi.org/10.15275/rusomj.2024.0413) (sheptulin2024clinicalandmorphological pages 2-3, sheptulin2024clinicalandmorphological pages 3-3)

### 6.3 Suggested ontology mappings (mechanism)
#### GO biological process terms (suggestions)
- Negative regulation of ventilation / gas exchange in cavity (conceptual; no direct GO mapping in retrieved texts)
- **Bone remodeling** — GO:0046849
- **Osteoclast differentiation** — GO:0030316 (hypothesized involvement) (sheptulin2024clinicalandmorphological pages 2-3)
- **Inflammatory response** — GO:0006954 (subclinical inflammation hypothesis) (sheptulin2024clinicalandmorphological pages 2-3)

#### CL (cell types; suggestions)
- **Osteoclast** — CL:0000092 (hypothesized, stage-dependent) (sheptulin2024clinicalandmorphological pages 2-3)
- **Osteoblast** — CL:0000062 (implied by bone remodeling context)
- **Respiratory epithelial cell** — CL:0002633 (sinus mucosa)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level
Primary anatomical sites:
- **Maxillary sinus** (collapse/atelectasis; opacification; reduced volume) (dorlodot2017chronicmaxillaryatelectasis pages 1-2, tousidonis2024contemporarytreatmentof pages 1-4)
- **Orbit**, especially **orbital floor** (inferior displacement/thinning/dehiscence; changes in orbital volume) (dorlodot2017chronicmaxillaryatelectasis pages 1-2, tousidonis2024contemporarytreatmentof pages 4-7)

### 7.2 Localization and laterality
- Typically **unilateral**, but bilateral cases exist in broader CMA/SSS spectrum (not central in the retrieved evidence set). de Dorlodot series shows a right-side predominance in that cohort: **13/18 (72%) right-sided**. (dorlodot2017chronicmaxillaryatelectasis pages 1-2)

### 7.3 Suggested UBERON terms (suggestions)
- Maxillary sinus — **UBERON:0001734**
- Orbit — **UBERON:0001697**
- Orbital floor (inferior orbital wall) — can be represented via orbit + bony wall anatomy terms (implementation-dependent)

---

## 8. Temporal development

### 8.1 Onset pattern
Often **insidious**; early disease may have no symptoms. Stryjewska-Makuch 2023: “**in the early stage of SSS, the patient does not report any symptoms**.” (published Oct 2023; URL: https://doi.org/10.1007/s00405-022-07697-w) (stryjewskamakuch2023whatmaysurprise pages 6-8)

### 8.2 Progression
Described as slow/progressive in classic descriptions and in the ClinicalTrials.gov case report, contributing to diagnostic delay. (sivasubramaniam2011silentsinussyndrome pages 1-2, NCT04388345 chunk 1)

---

## 9. Inheritance and population

### 9.1 Epidemiology (prevalence/incidence)
No population-based prevalence/incidence estimates were identified in the retrieved evidence.

### 9.2 Case counts / rarity statements
- Kramer 2024 states: “**Only around 100 cases** of SSS have been reported so far.” (published May 2024; URL: https://doi.org/10.7759/cureus.61442) (kramer2024granulomatosiswithpolyangiitis pages 1-3)

### 9.3 Demographics (statistics from clinical series)
- de Dorlodot 2017: **18 patients**, mean age **44.0 ± 16.9** (range 12–70), **7 women/11 men**, right-sided **13/18 (72%)**. (published Jun 2017; URL: https://doi.org/10.1007/s00405-017-4622-8) (dorlodot2017chronicmaxillaryatelectasis pages 1-2)
- Clarós 2019: **15 patients**, **11 women/4 men**, mean duration of enophthalmos **10.7 months**, mean enophthalmos **2.6 mm**, mean hypoglobus **2.7 mm**. (published Jan 2019; URL: https://doi.org/10.1080/00016489.2018.1542161) (claros2019silentsinussyndrome pages 1-3)
- Stryjewska-Makuch 2023 institutional experience: among **1766** paranasal sinus patients (Sept 2017–May 2022), **8 SSS cases** (4 men/4 women), mean age **45.4** (range 31–75). (published Oct 2023; URL: https://doi.org/10.1007/s00405-022-07697-w) (stryjewskamakuch2023whatmaysurprise pages 2-4)

---

## 10. Diagnostics

### 10.1 Imaging (core diagnostic modality)
- CT is repeatedly emphasized as the diagnostic cornerstone; the trial registry explicitly states: “**CT imaging is considered the gold standard for its diagnosis. The classical radiographic findings are opacification and collapse of the sinus walls**.” (NCT04388345; posted May 14, 2020; URL: https://clinicaltrials.gov/study/NCT04388345) (NCT04388345 chunk 1)
- Tousidonis 2024: imaging shows reduced maxillary antrum volume with retraction of maxillary walls; CT/MRI used. (tousidonis2024contemporarytreatmentof pages 7-8)
- de Dorlodot 2017: coronal CT shows complete or partial opacity (complete 10/18, partial 8/18) and orbital floor dehiscence in 12 cases. (dorlodot2017chronicmaxillaryatelectasis pages 1-2)

### 10.2 Key radiographic features
- Reduced maxillary sinus volume; inward bowing of sinus walls; often opacification; inferior displacement/thinning of orbital floor; uncinate lateralization/infundibular occlusion. (dorlodot2017chronicmaxillaryatelectasis pages 1-2, lee2018silentsinussyndrome pages 1-4)
- Important diagnostic nuance: Lee 2018 demonstrates SSS can occur **without ipsilateral maxillary sinus opacification**, reporting average ipsilateral maxillary volume loss of **29% ± 7.1%**. (published Sep 2018; URL: https://doi.org/10.1002/lary.27108) (lee2018silentsinussyndrome pages 1-4)

### 10.3 Clinical evaluation
SSS often presents with ophthalmologic complaints; nasal endoscopy and ENT evaluation are recommended in suspected cases (trial registry). (NCT04388345 chunk 1)

### 10.4 Differential diagnosis (selected)
From de Dorlodot’s exclusion criteria and modern etiologic expansions:
- Prior trauma/surgery causing secondary changes (secondary SSS) (strabbing2025posttraumaticandiatrogenic pages 1-2, dorlodot2017chronicmaxillaryatelectasis pages 1-2)
- Congenital facial/orbital deformity (excluded in de Dorlodot series) (dorlodot2017chronicmaxillaryatelectasis pages 1-2)
- Other causes of acquired enophthalmos/hypoglobus (e.g., orbital pathology; not enumerated in retrieved texts)
- Systemic inflammatory disease causing sinonasal obstruction such as **GPA**, particularly with necrotizing granulomatous inflammation and ANCA positivity. (kramer2024granulomatosiswithpolyangiitis pages 1-3, kramer2024granulomatosiswithpolyangiitis pages 3-5)

---

## 11. Outcome / prognosis

### 11.1 Prognosis and functional outcomes
SSS is generally treatable with surgical restoration of ventilation/drainage, with frequent improvement in ocular position and symptoms.
- Sivasubramaniam 2011 reports that in a 23-case experience treated with uncinectomy/antrostomy alone, **22/23** had **complete or partial resolution**, supporting staged orbital reconstruction when needed. (published Aug 2011; URL: https://doi.org/10.1017/S0022215111001952) (sivasubramaniam2011silentsinussyndrome pages 1-2)

### 11.2 Complications
- Secondary SSS can be associated with diplopia and functional/cosmetic impact; early recognition is advised to prevent severe sequelae. (strabbing2025posttraumaticandiatrogenic pages 1-2)

---

## 12. Treatment

### 12.1 Surgical/interventional (current standard of care)
**Functional endoscopic sinus surgery (FESS)** to restore ventilation/drainage is consistently described as the standard.
- Tousidonis 2024: “**maxillary endoscopic antrostomy and uncinectomy with FESS represent the gold standard**.” (published Apr 2024; URL: https://doi.org/10.7759/cureus.57577) (tousidonis2024contemporarytreatmentof pages 7-8)
- ClinicalTrials.gov registry similarly states: “**Functional endoscopic sinus surgery (FESS) is the standard gold treatment of choice to arrest the progression of the disease**.” (NCT04388345 chunk 1)

### 12.2 Orbital reconstruction (indications and timing controversies)
There is no universal consensus on whether to reconstruct the orbital floor immediately.
- Evidence for **staged/delayed approach:** dynamic remodeling after re-ventilation can improve orbital floor position, potentially avoiding reconstruction; Sivasubramaniam supports delay and reassessment (22/23 improved with FESS alone). (sivasubramaniam2011silentsinussyndrome pages 1-2)
- Sheptulin 2024: staged approach with follow-up CT at 6 months showed sinus pneumatization and orbital-floor elevation, but residual **3–4 mm enophthalmos** and diplopia prompted delayed reconstruction; authors cite arguments to delay 3–6 months to reduce risks of overcorrection/inflammatory complications. (sheptulin2024clinicalandmorphological pages 1-2, sheptulin2024clinicalandmorphological pages 3-3)
- Evidence for **combined/simultaneous approach:** Clarós 2019 reports 13/15 treated with simultaneous ESS and titanium orbital floor implant with significant improvement. (claros2019silentsinussyndrome pages 1-3)

### 12.3 Real-world implementations / advanced techniques (2023–2024 emphasis)
Tousidonis 2024 illustrates contemporary orbit reconstruction adjuncts:
- A combined approach using **patient-specific titanium implant**, FESS, **surgical navigation**, and **intraoperative CT** with objective volumetry: affected orbital volume **28.066 cm³ pre-op** vs **25.257 cm³ post-op** (reduction **2.809 cm³**), with stable 1-year results and no late complications. (published Apr 2024; URL: https://doi.org/10.7759/cureus.57577) (tousidonis2024contemporarytreatmentof pages 4-7)

### 12.4 Treatment outcomes (statistics)
- FESS alone: 22/23 complete or partial resolution in Sivasubramaniam 2011. (sivasubramaniam2011silentsinussyndrome pages 1-2)
- Combined surgery: quantitative ocular metrics in Clarós 2019 (mean pre-op enophthalmos 2.6 mm, hypoglobus 2.7 mm; significant improvement post-op). (claros2019silentsinussyndrome pages 1-3)
- Secondary SSS: Strabbing 2025 reports surgery “restored orbital anatomy and resolved symptoms”; their Table 1 summarizes patient symptom patterns (enophthalmos/hypoglobus/diplopia) and latency post-trigger. (strabbing2025posttraumaticandiatrogenic pages 1-2, strabbing2025posttraumaticandiatrogenic media de48a58f)

### 12.5 Suggested MAXO terms (suggestions)
- Functional endoscopic sinus surgery — **MAXO:0001179** (conceptual mapping; MAXO ID may vary by implementation)
- Maxillary antrostomy / uncinectomy — MAXO procedural descendants (implementation-dependent)
- Orbital floor reconstruction — MAXO surgical reconstruction concept (implementation-dependent)

### 12.6 Pharmacotherapy
No disease-specific pharmacotherapy standards were identified in the retrieved evidence; antibiotics may be used for infectious complications in specific perioperative contexts (e.g., postoperative orbital complication described in a pediatric case report not deeply analyzed here). (tousidonis2024contemporarytreatmentof pages 7-8)

### 12.7 Experimental / clinical trials
No interventional trials were identified. One observational registry entry exists:
- **NCT04388345** (COMPLETED; enrollment 1; posted May 14, 2020): “SILENT SINUS SYNDROME (First Case Report, Saudi Arabia With Recommendation)” (URL: https://clinicaltrials.gov/study/NCT04388345). (NCT04388345 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
No primary-prevention interventions are established in the retrieved evidence.

### 13.2 Secondary/tertiary prevention (complication prevention)
Evidence supports **early recognition** and **timely ENT referral** to prevent progression of cosmetic/functional orbital deformity:
- NCT04388345 recommends “prompt ear, nose, and throat referral” for suspected cases and emphasizes CT-based diagnosis and FESS to arrest progression. (NCT04388345 chunk 1)
- Strabbing 2025 recommends follow-up after trauma/surgery when unexplained orbital changes develop, to prevent severe complications. (strabbing2025posttraumaticandiatrogenic pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary/other-species analogs were identified in the retrieved evidence.

---

## 15. Model organisms
No model organism or in vitro disease models were identified in the retrieved evidence.

---

## High-yield structured summary (artifact)
The following structured table consolidates key concepts, statistics, and management evidence with URLs/DOIs and citation hooks:

| Topic | Key points (include quantitative data where reported) | Evidence type (case series/review/case report/trial registry) | Source (first author year) | Publication date | PMID | URL/DOI | Citation ID to use in answer |
|---|---|---|---|---|---|---|---|
| Clinical definition | SSS defined as spontaneous, usually painless enophthalmos and/or hypoglobus with ipsilateral maxillary sinus collapse/atelectasis and orbital floor descent; often little or no sinonasal symptoms. Some authors place SSS on the spectrum of chronic maxillary atelectasis (type 3 CMA). (claros2019silentsinussyndrome pages 1-3, dorlodot2017chronicmaxillaryatelectasis pages 1-2, sivasubramaniam2011silentsinussyndrome pages 1-2) | Case series/review | Clarós 2019; de Dorlodot 2017; Sivasubramaniam 2011 | 2019-01; 2017-06; 2011-08 | not in retrieved text | https://doi.org/10.1080/00016489.2018.1542161; https://doi.org/10.1007/s00405-017-4622-8; https://doi.org/10.1017/S0022215111001952 | (claros2019silentsinussyndrome pages 1-3, dorlodot2017chronicmaxillaryatelectasis pages 1-2, sivasubramaniam2011silentsinussyndrome pages 1-2) |
| Pathophysiology | Most-cited mechanism: ostiomeatal complex/infundibular obstruction → sinus hypoventilation → gas resorption and subatmospheric pressure → maxillary wall inward bowing/atelectasis → downward orbital floor displacement → increased orbital volume causing enophthalmos/hypoglobus. Sheptulin notes animal data suggesting even a 2 mmHg pressure drop may increase osteoclast activity; histology in one late-stage case showed no active osteolysis, implying remodeling may be stage-dependent. (tousidonis2024contemporarytreatmentof pages 7-8, sheptulin2024clinicalandmorphological pages 2-3, sivasubramaniam2011silentsinussyndrome pages 1-2) | Review/case report/case series | Tousidonis 2024; Sheptulin 2024; Sivasubramaniam 2011 | 2024-04; 2024-12; 2011-08 | not in retrieved text | https://doi.org/10.7759/cureus.57577; https://doi.org/10.15275/rusomj.2024.0413; https://doi.org/10.1017/S0022215111001952 | (tousidonis2024contemporarytreatmentof pages 7-8, sheptulin2024clinicalandmorphological pages 2-3, sivasubramaniam2011silentsinussyndrome pages 1-2) |
| Core phenotypes | Common features: progressive enophthalmos, hypoglobus, orbital asymmetry, diplopia, superior sulcus deepening, diminished malar projection, facial asymmetry; atypical signs can include facial hypoesthesia, eyelid retraction/ptosis, dry eye. Reported displacement magnitudes: hypoglobus 2–6 mm and enophthalmos 2–5 mm. In secondary SSS, 8/9 patients had diplopia. (tousidonis2024contemporarytreatmentof pages 7-8, sivasubramaniam2011silentsinussyndrome pages 1-2, tousidonis2024contemporarytreatmentof pages 1-4, strabbing2025posttraumaticandiatrogenic pages 1-2) | Review/case series/case report | Tousidonis 2024; Sivasubramaniam 2011; Strabbing 2025 | 2024-04; 2011-08; 2025-05 | not in retrieved text | https://doi.org/10.7759/cureus.57577; https://doi.org/10.1017/S0022215111001952; https://doi.org/10.1007/s10006-025-01391-x | (tousidonis2024contemporarytreatmentof pages 7-8, sivasubramaniam2011silentsinussyndrome pages 1-2, tousidonis2024contemporarytreatmentof pages 1-4, strabbing2025posttraumaticandiatrogenic pages 1-2) |
| Imaging findings | CT is the diagnostic mainstay/gold standard. Typical findings: reduced maxillary sinus volume, sinus opacification (often complete or partial), inward bowing of antral walls, inferior displacement/thinning of orbital floor, uncinate lateralization, infundibular occlusion. In de Dorlodot series, opacity was complete in 10/18 and partial in 8/18; orbital floor dehiscence in 12 cases. Lee showed SSS may occur even without sinus opacification; average ipsilateral maxillary volume loss 29% ± 7.1%. (dorlodot2017chronicmaxillaryatelectasis pages 1-2, lee2018silentsinussyndrome pages 1-4, tousidonis2024contemporarytreatmentof pages 1-4, NCT04388345 chunk 1) | Case series/case report/trial registry | de Dorlodot 2017; Lee 2018; Tousidonis 2024; NCT04388345 | 2017-06; 2018-09; 2024-04; 2020-05 | not in retrieved text | https://doi.org/10.1007/s00405-017-4622-8; https://doi.org/10.1002/lary.27108; https://doi.org/10.7759/cureus.57577; https://clinicaltrials.gov/study/NCT04388345 | (dorlodot2017chronicmaxillaryatelectasis pages 1-2, lee2018silentsinussyndrome pages 1-4, tousidonis2024contemporarytreatmentof pages 1-4, NCT04388345 chunk 1) |
| Demographics/statistics | SSS is rare. Kramer 2024 states “around 100 cases described.” Typical age distribution is adult, often 3rd–5th decades; equal-sex distribution is reported by Tousidonis 2024, but individual series vary. de Dorlodot: 18 patients, mean age 44.0 ± 16.9 years, 11 men/7 women, right side in 13/18 (72%). Clarós: 15 patients, 11 women/4 men, mean symptom duration 10.7 months, mean enophthalmos 2.6 mm and hypoglobus 2.7 mm. Stryjewska-Makuch institutional experience: 8 SSS cases among 1766 paranasal sinus patients (2017–2022), mean age 45.4 years, 4 men/4 women. (kramer2024granulomatosiswithpolyangiitis pages 1-3, dorlodot2017chronicmaxillaryatelectasis pages 1-2, claros2019silentsinussyndrome pages 1-3, stryjewskamakuch2023whatmaysurprise pages 2-4) | Case series/review/case report | Kramer 2024; de Dorlodot 2017; Clarós 2019; Stryjewska-Makuch 2023 | 2024-05; 2017-06; 2019-01; 2023-10 | not in retrieved text | https://doi.org/10.7759/cureus.61442; https://doi.org/10.1007/s00405-017-4622-8; https://doi.org/10.1080/00016489.2018.1542161; https://doi.org/10.1007/s00405-022-07697-w | (kramer2024granulomatosiswithpolyangiitis pages 1-3, dorlodot2017chronicmaxillaryatelectasis pages 1-2, claros2019silentsinussyndrome pages 1-3, stryjewskamakuch2023whatmaysurprise pages 2-4) |
| Secondary/associated etiologies | Although often idiopathic, secondary SSS can follow trauma or surgery disrupting mucociliary clearance. In Strabbing 2025, onset after trauma/surgery ranged 1–36 months, median 3 months in post-traumatic cases. Rare associated etiologies include GPA/ANCA vasculitis causing infundibular obstruction and destructive sinonasal disease. Familial clustering has been proposed in later literature, but robust genetic evidence is lacking in retrieved texts. (strabbing2025posttraumaticandiatrogenic pages 1-2, kramer2024granulomatosiswithpolyangiitis pages 5-7, kramer2024granulomatosiswithpolyangiitis pages 3-5) | Case series/case report | Strabbing 2025; Kramer 2024 | 2025-05; 2024-05 | not in retrieved text | https://doi.org/10.1007/s10006-025-01391-x; https://doi.org/10.7759/cureus.61442 | (strabbing2025posttraumaticandiatrogenic pages 1-2, kramer2024granulomatosiswithpolyangiitis pages 5-7, kramer2024granulomatosiswithpolyangiitis pages 3-5) |
| Standard treatment | Functional endoscopic sinus surgery (FESS), typically uncinectomy with middle meatal antrostomy/maxillary antrostomy, is the current standard/gold-standard intervention to re-establish drainage and ventilation and arrest progression. (tousidonis2024contemporarytreatmentof pages 7-8, NCT04388345 chunk 1, stryjewskamakuch2023whatmaysurprise pages 2-4) | Review/trial registry/case series | Tousidonis 2024; NCT04388345; Stryjewska-Makuch 2023 | 2024-04; 2020-05; 2023-10 | not in retrieved text | https://doi.org/10.7759/cureus.57577; https://clinicaltrials.gov/study/NCT04388345; https://doi.org/10.1007/s00405-022-07697-w | (tousidonis2024contemporarytreatmentof pages 7-8, NCT04388345 chunk 1, stryjewskamakuch2023whatmaysurprise pages 2-4) |
| Orbital reconstruction timing | Controversial. Some authors favor FESS alone initially because orbital floor position may remodel after re-aeration; Sivasubramaniam reported 22/23 patients had complete or partial resolution after uncinectomy/antrostomy alone. Delayed reconstruction is often considered for persistent enophthalmos >2 mm, diplopia, or unacceptable cosmesis after reassessment (commonly 3–6 months). Others perform simultaneous ESS plus orbital reconstruction in selected advanced cases. (tousidonis2024contemporarytreatmentof pages 7-8, sheptulin2024clinicalandmorphological pages 3-3, sivasubramaniam2011silentsinussyndrome pages 1-2) | Review/case report/case series | Tousidonis 2024; Sheptulin 2024; Sivasubramaniam 2011 | 2024-04; 2024-12; 2011-08 | not in retrieved text | https://doi.org/10.7759/cureus.57577; https://doi.org/10.15275/rusomj.2024.0413; https://doi.org/10.1017/S0022215111001952 | (tousidonis2024contemporarytreatmentof pages 7-8, sheptulin2024clinicalandmorphological pages 3-3, sivasubramaniam2011silentsinussyndrome pages 1-2) |
| Combined surgery outcomes | Clarós 2019: 13/15 underwent simultaneous ESS plus titanium orbital floor implant; significant pre/post improvement in enophthalmos and hypoglobus, with good long-term aesthetic results. Tousidonis 2024 case: FESS plus patient-specific titanium implant reduced orbital volume from 28.066 cm3 pre-op to 25.257 cm3 post-op (reduction 2.809 cm3), with stable satisfactory 1-year result and no late complications. Secondary SSS series reported restoration of orbital anatomy and symptom resolution after retrograde uncinectomy and orbital reconstruction. (claros2019silentsinussyndrome pages 1-3, tousidonis2024contemporarytreatmentof pages 4-7, strabbing2025posttraumaticandiatrogenic pages 1-2) | Case series/case report | Clarós 2019; Tousidonis 2024; Strabbing 2025 | 2019-01; 2024-04; 2025-05 | not in retrieved text | https://doi.org/10.1080/00016489.2018.1542161; https://doi.org/10.7759/cureus.57577; https://doi.org/10.1007/s10006-025-01391-x | (claros2019silentsinussyndrome pages 1-3, tousidonis2024contemporarytreatmentof pages 4-7, strabbing2025posttraumaticandiatrogenic pages 1-2) |
| Diagnostic caution / differential clues | Differential diagnosis should consider chronic maxillary atelectasis without classic SSS symptoms, prior trauma/surgery, congenital deformity, orbital pathology, and systemic causes of sinonasal obstruction. GPA should be suspected when SSS-like findings coexist with autoimmune history, ANCA positivity, necrotizing granulomatous inflammation, epistaxis, saddle-nose deformity, or renal vasculitis history. SSS should also remain a differential even without maxillary opacification. (dorlodot2017chronicmaxillaryatelectasis pages 1-2, lee2018silentsinussyndrome pages 1-4, kramer2024granulomatosiswithpolyangiitis pages 5-7, NCT04388345 chunk 1) | Case series/case report/trial registry | de Dorlodot 2017; Lee 2018; Kramer 2024; NCT04388345 | 2017-06; 2018-09; 2024-05; 2020-05 | not in retrieved text | https://doi.org/10.1007/s00405-017-4622-8; https://doi.org/10.1002/lary.27108; https://doi.org/10.7759/cureus.61442; https://clinicaltrials.gov/study/NCT04388345 | (dorlodot2017chronicmaxillaryatelectasis pages 1-2, lee2018silentsinussyndrome pages 1-4, kramer2024granulomatosiswithpolyangiitis pages 5-7, NCT04388345 chunk 1) |


*Table: This table summarizes key clinical, radiologic, mechanistic, demographic, and treatment findings for Silent Sinus Syndrome from the retrieved evidence base. It is designed to support rapid citation and knowledge-base population.*

---

## Visual evidence
A cropped table image from Strabbing 2025 summarizing secondary SSS patient-level clinical data (symptoms and time-to-onset) was retrieved and can be used to support secondary SSS statistics and variability in presentation. (strabbing2025posttraumaticandiatrogenic media de48a58f)

---

## Evidence gaps and limitations (for KB curation)
- **Identifiers (ICD/MeSH/Orphanet/OMIM):** not retrieved in this run; should be filled from authoritative ontologies (e.g., MeSH Browser, ICD-11 MMS, Orphanet) in a follow-up curation step.
- **Genetics:** no established causal genes/variants in retrieved evidence; occasional familial clustering hypotheses exist in broader literature but were not evidenced here.
- **Epidemiology:** no incidence/prevalence estimates; literature is largely case series/case reports.
- **QoL instruments:** no EQ-5D/SF-36/PROMIS quantitative data found in retrieved evidence.



References

1. (claros2019silentsinussyndrome pages 1-3): Pedro Clarós, Aleksandra Zofia Sobolewska, Antonio Cardesa, Marta Lopez-Fortuny, and Andres Claros. Silent sinus syndrome: combined sinus surgery and orbital reconstruction – report of 15 cases. Acta Oto-Laryngologica, 139:64-69, Jan 2019. URL: https://doi.org/10.1080/00016489.2018.1542161, doi:10.1080/00016489.2018.1542161. This article has 12 citations and is from a peer-reviewed journal.

2. (dorlodot2017chronicmaxillaryatelectasis pages 1-2): Clotilde de Dorlodot, Stephanie Collet, Philippe Rombaux, Mihaela Horoi, Sergio Hassid, and Philippe Eloy. Chronic maxillary atelectasis and silent sinus syndrome: two faces of the same clinical entity. European Archives of Oto-Rhino-Laryngology, 274:3367-3373, Jun 2017. URL: https://doi.org/10.1007/s00405-017-4622-8, doi:10.1007/s00405-017-4622-8. This article has 38 citations and is from a peer-reviewed journal.

3. (tousidonis2024contemporarytreatmentof pages 7-8): Manuel Tousidonis, Sara Alvarez-Mokthari, Saad Khayat, Guillermo Sanjuan de Moreta, and Santiago Ochandiano. Contemporary treatment of silent sinus syndrome: a case report and literature review. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.57577, doi:10.7759/cureus.57577. This article has 3 citations.

4. (sivasubramaniam2011silentsinussyndrome pages 1-2): R. Sivasubramaniam, Raymond Sacks, and M. Thornton. Silent sinus syndrome: dynamic changes in the position of the orbital floor after restoration of normal sinus pressure. The Journal of Laryngology & Otology, 125:1239-1243, Aug 2011. URL: https://doi.org/10.1017/s0022215111001952, doi:10.1017/s0022215111001952. This article has 75 citations.

5. (lee2018silentsinussyndrome pages 1-4): David S. Lee, Andrew H. Murr, Robert C. Kersten, and Steven D. Pletcher. Silent sinus syndrome without opacification of ipsilateral maxillary sinus. The Laryngoscope, 128:2004-2007, Sep 2018. URL: https://doi.org/10.1002/lary.27108, doi:10.1002/lary.27108. This article has 23 citations.

6. (strabbing2025posttraumaticandiatrogenic pages 1-2): E. M. Strabbing, O. Engin, M. A.J. Telleman, A. P. Nagtegaal, and E. B. Wolvius. Post-traumatic and iatrogenic silent sinus syndrome: a case series. Oral and Maxillofacial Surgery, May 2025. URL: https://doi.org/10.1007/s10006-025-01391-x, doi:10.1007/s10006-025-01391-x. This article has 3 citations and is from a peer-reviewed journal.

7. (kramer2024granulomatosiswithpolyangiitis pages 1-3): Nicholas Kramer, Brandon Manthei, Luke Speier, Jo-Lawrence M Bigcas, and Scott Manthei. Granulomatosis with polyangiitis as an etiology of silent sinus syndrome: a case report. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.61442, doi:10.7759/cureus.61442. This article has 1 citations.

8. (tousidonis2024contemporarytreatmentof pages 1-4): Manuel Tousidonis, Sara Alvarez-Mokthari, Saad Khayat, Guillermo Sanjuan de Moreta, and Santiago Ochandiano. Contemporary treatment of silent sinus syndrome: a case report and literature review. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.57577, doi:10.7759/cureus.57577. This article has 3 citations.

9. (tousidonis2024contemporarytreatmentof pages 4-7): Manuel Tousidonis, Sara Alvarez-Mokthari, Saad Khayat, Guillermo Sanjuan de Moreta, and Santiago Ochandiano. Contemporary treatment of silent sinus syndrome: a case report and literature review. Cureus, Apr 2024. URL: https://doi.org/10.7759/cureus.57577, doi:10.7759/cureus.57577. This article has 3 citations.

10. (NCT04388345 chunk 1): Nouf Saloom Alsaloom. SILENT SINUS SYNDROME (First Case Report, Saudi Arabia With Recommendation). King Saud University. 2019. ClinicalTrials.gov Identifier: NCT04388345

11. (kramer2024granulomatosiswithpolyangiitis pages 5-7): Nicholas Kramer, Brandon Manthei, Luke Speier, Jo-Lawrence M Bigcas, and Scott Manthei. Granulomatosis with polyangiitis as an etiology of silent sinus syndrome: a case report. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.61442, doi:10.7759/cureus.61442. This article has 1 citations.

12. (sheptulin2024clinicalandmorphological pages 2-3): Vladimir A. Sheptulin, Yaroslav O. Grusha, and Dmitry M. Konovalov. Clinical and morphological features of the orbital floor in a patient with silent sinus syndrome: a clinical case report. Russian Open Medical Journal, Dec 2024. URL: https://doi.org/10.15275/rusomj.2024.0413, doi:10.15275/rusomj.2024.0413. This article has 0 citations.

13. (sheptulin2024clinicalandmorphological pages 3-3): Vladimir A. Sheptulin, Yaroslav O. Grusha, and Dmitry M. Konovalov. Clinical and morphological features of the orbital floor in a patient with silent sinus syndrome: a clinical case report. Russian Open Medical Journal, Dec 2024. URL: https://doi.org/10.15275/rusomj.2024.0413, doi:10.15275/rusomj.2024.0413. This article has 0 citations.

14. (stryjewskamakuch2023whatmaysurprise pages 6-8): Grażyna Stryjewska-Makuch, Magdalena Kokoszka, Karolina Goroszkiewicz, Olga Karłowska-Bijak, Bogdan Kolebacz, and Maciej Misiołek. What may surprise a rhinologist in everyday clinical practice: silent sinus syndrome or pneumosinus dilatans/pneumocele? literature review and own experience. European Archives of Oto-Rhino-Laryngology, 280:519-527, Oct 2023. URL: https://doi.org/10.1007/s00405-022-07697-w, doi:10.1007/s00405-022-07697-w. This article has 4 citations and is from a peer-reviewed journal.

15. (stryjewskamakuch2023whatmaysurprise pages 2-4): Grażyna Stryjewska-Makuch, Magdalena Kokoszka, Karolina Goroszkiewicz, Olga Karłowska-Bijak, Bogdan Kolebacz, and Maciej Misiołek. What may surprise a rhinologist in everyday clinical practice: silent sinus syndrome or pneumosinus dilatans/pneumocele? literature review and own experience. European Archives of Oto-Rhino-Laryngology, 280:519-527, Oct 2023. URL: https://doi.org/10.1007/s00405-022-07697-w, doi:10.1007/s00405-022-07697-w. This article has 4 citations and is from a peer-reviewed journal.

16. (kramer2024granulomatosiswithpolyangiitis pages 3-5): Nicholas Kramer, Brandon Manthei, Luke Speier, Jo-Lawrence M Bigcas, and Scott Manthei. Granulomatosis with polyangiitis as an etiology of silent sinus syndrome: a case report. Cureus, May 2024. URL: https://doi.org/10.7759/cureus.61442, doi:10.7759/cureus.61442. This article has 1 citations.

17. (sheptulin2024clinicalandmorphological pages 1-2): Vladimir A. Sheptulin, Yaroslav O. Grusha, and Dmitry M. Konovalov. Clinical and morphological features of the orbital floor in a patient with silent sinus syndrome: a clinical case report. Russian Open Medical Journal, Dec 2024. URL: https://doi.org/10.15275/rusomj.2024.0413, doi:10.15275/rusomj.2024.0413. This article has 0 citations.

18. (strabbing2025posttraumaticandiatrogenic media de48a58f): E. M. Strabbing, O. Engin, M. A.J. Telleman, A. P. Nagtegaal, and E. B. Wolvius. Post-traumatic and iatrogenic silent sinus syndrome: a case series. Oral and Maxillofacial Surgery, May 2025. URL: https://doi.org/10.1007/s10006-025-01391-x, doi:10.1007/s10006-025-01391-x. This article has 3 citations and is from a peer-reviewed journal.