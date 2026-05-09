---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T23:12:12.100681'
end_time: '2026-05-05T23:39:44.252828'
duration_seconds: 1652.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinal Cord Ischemia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinal Cord Ischemia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Spinal Cord Ischemia** covering all of the
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
- **Disease Name:** Spinal Cord Ischemia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Spinal Cord Ischemia** covering all of the
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


## Comprehensive Research Report: Spinal Cord Ischemia (Spinal Cord Infarction)

### Scope note
The term **spinal cord ischemia (SCI)** is used variably in the literature to refer to (i) **acute spinal cord infarction** (arterial ischemic stroke of the cord) and/or (ii) **perioperative/iatrogenic spinal cord ischemia** (notably after open or endovascular aortic procedures). This report focuses on both, because “spinal cord ischemia” is most commonly implemented clinically in peri-aortic-surgery spinal cord protection protocols and in stroke-like spinal cord infarction diagnostics. (dokponou2024spinalcordinfarction pages 1-2, chen2023prophylacticcerebrospinalfluid pages 1-2)

---

## 1. Disease Information

### 1.1 What is spinal cord ischemia?
**Spinal cord infarction** is described as a **rare ischemic vascular lesion** of the spinal cord (a “rare stroke subtype”) that presents as an acute or hyperacute myelopathy and is diagnostically challenging because early MRI (including DWI) can be normal or equivocal. (dokponou2024spinalcordinfarction pages 1-2, zedde2025spinalcordinfarction pages 10-11)

**Direct abstract-supported definition (2024 systematic review):** Dokponou et al. describe acute spinal cord infarction as “a rare ischemic vascular lesion” and emphasize difficulty diagnosing it in the acute phase, including that diffusion-weighted MRI may fail to show abnormalities early. (dokponou2024spinalcordinfarction pages 1-2)

### 1.2 Synonyms / alternative names
Commonly used interchangeable terms in the retrieved recent literature include:
- **Spinal cord infarction** (SCI) (dokponou2024spinalcordinfarction pages 1-2)
- **Spinal cord ischemia** (used both for spontaneous infarction and perioperative ischemic injury) (chen2023prophylacticcerebrospinalfluid pages 1-2)
- **Ischemic spinal cord injury** (especially perioperative/aortic contexts) (torre2025spinalcordprotection pages 10-11)
- **Ischemic myelopathy** (historical/vascular syndromic term; identified in review literature) (dokponou2024spinalcordinfarction pages 7-8)

### 1.3 Key identifiers (ICD/MeSH/MONDO)
Within the retrieved full-text set, **formal ICD-10/ICD-11, MeSH, and MONDO identifiers were not explicitly provided**, and thus cannot be asserted from the evidence captured here.

For a knowledge base, spinal cord ischemia/infarction is typically mapped under spinal cord vascular disorders and/or spinal stroke; however, **this report does not provide codes without direct evidence** from the retrieved sources.

### 1.4 Evidence sources (individual vs aggregated)
- **Aggregated evidence**: systematic reviews/meta-analyses for spontaneous spinal cord infarction and for peri-aortic-procedure spinal cord ischemia prevention (TEVAR/open repair) (dokponou2024spinalcordinfarction pages 3-5, chen2023prophylacticcerebrospinalfluid pages 1-2, zheng2024systematicreviewof pages 5-7)
- **Single-center retrospective cohort**: open aortic repair CSF drainage series (n=132) (nasir2023safetyofcerebrospinal pages 1-3)
- **ClinicalTrials.gov registry records**: randomized pilot/phase 2 trials and biomarker observational study (NCT04941157 chunk 1, NCT04600089 chunk 1, NCT04523909 chunk 1)

---

## 2. Etiology

### 2.1 Primary causal factors
#### A. Spontaneous / non-iatrogenic spinal cord infarction
A 2024 systematic review/meta-analysis (876 patients) categorized etiologies as:
- **Vascular**: 44.2%
- **Traumatic**: 14.3%
- **Infectious**: 6.1%
- **Unknown**: 35.5% (dokponou2024spinalcordinfarction pages 3-5)

The same review describes etiologies as spontaneous or iatrogenic and lists common causes including **aortic disease, cardioembolism, systemic hypoperfusion, vasculitis, and idiopathic causes**, with **atherosclerosis commonly implicated**. (dokponou2024spinalcordinfarction pages 1-2)

#### B. Iatrogenic/perioperative spinal cord ischemia (aortic surgery)
Spinal cord ischemia is a feared complication after:
- **Open descending thoracic/thoracoabdominal aortic repair** (nasir2023safetyofcerebrospinal pages 1-3)
- **Thoracic endovascular aortic repair (TEVAR)** and thoracoabdominal endovascular procedures (chen2023prophylacticcerebrospinalfluid pages 1-2)

Mechanistically, these settings involve disruption of spinal cord blood supply, extensive segmental artery coverage, hypoperfusion, embolism, and ischemia–reperfusion injury (particularly after open cross-clamping). (torre2025spinalcordprotection pages 1-2, nasir2023safetyofcerebrospinal pages 6-7)

### 2.2 Risk factors
#### Spontaneous spinal cord infarction: vascular risks (reported frequencies)
A 2025 review summarizing cohort evidence reported common vascular risk factors in SCI as:
- Hypertension ~40%
- Smoking ~30%
- Dyslipidemia ~29%
- Diabetes ~16%
- ~28% without reported vascular risk factors (zedde2025spinalcordinfarction pages 2-4)

However, in the 2024 systematic review/meta-analysis dataset, recorded cardiovascular risk factors were often absent: **66.1% had no recorded cardiovascular risk factors**, with hypertension 17.1% and hypertension+diabetes 6.2% among those reported. (dokponou2024spinalcordinfarction pages 3-5)

#### Peri-TEVAR/aortic risk factors
For TEVAR, risk is increased by procedure- and anatomy-related factors, including extent of aortic coverage and collateral vessel occlusion; a meta-analysis notes reported TEVAR SCI rates range 0–17% in literature, with highest rates in thoracoabdominal aneurysm procedures. (chen2023prophylacticcerebrospinalfluid pages 1-2)

### 2.3 Protective factors
The retrieved evidence is strongest for **perioperative protective strategies** (rather than host protective factors). Key physiology-guided protective principle: maintaining **spinal cord perfusion pressure (SCPP)** by supporting arterial pressure and reducing CSF pressure when needed. (torre2025spinalcordprotection pages 10-11, nasir2023safetyofcerebrospinal pages 6-7)

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to spinal cord ischemia/infarction was identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core clinical features and frequencies
From a 2025 clinical-neuroradiological review synthesis:
- **Motor deficits**: 92%
- **Sensory deficits**: 85%
- **Autonomic dysfunction**: 76%
- **Pain**: 70% (zedde2025spinalcordinfarction pages 6-8)

From a 2024 systematic review/meta-analysis (876 patients), pooled phenotype frequencies included:
- Hemiplegia 23.2%
- Paraplegia 21.7%
- Tetraplegia 14.8%
- Paraparesis 8.9%
- Respiratory dysfunction 11.9%
- Swallowing disturbance 7.6%
- Asymptomatic 11.9% (dokponou2024spinalcordinfarction pages 3-5)

Pain (including radicular/spinal pain) was reported in 68.6% in the 2024 review’s synthesis. (dokponou2024spinalcordinfarction pages 7-8)

### 3.2 Temporal development
**Time to nadir** (time from onset to maximal deficit) is a key discriminator for diagnosis.
- 2024 meta-analysis: <6 h (56.1%), 6–12 h (30.7%), 12–72 h (5.4%), >72 h (7.8%). (dokponou2024spinalcordinfarction pages 3-5)
- 2025 review synthesis: pooled data suggesting **~81% reach nadir within 12 h** (with an additional breakdown in some syntheses), supporting a hyperacute pattern typical of spinal cord infarction. (zedde2025spinalcordinfarction pages 8-10)

### 3.3 HPO term suggestions (non-exhaustive)
Based on the reported phenotypes:
- Paraplegia (**HP:0003401**) / Paraparesis (**HP:0001258**) / Tetraplegia (**HP:0003300**) (dokponou2024spinalcordinfarction pages 3-5)
- Sensory impairment (**HP:0003401** is motor; for sensory: consider **HP:0000769** abnormality of sensation; map more precisely to pain/temperature loss when curated) (zedde2025spinalcordinfarction pages 6-8)
- Neuropathic pain (**HP:0007018**) / Pain (**HP:0012531**) (zedde2025spinalcordinfarction pages 6-8)
- Autonomic dysfunction (**HP:0002459**) including bladder dysfunction (**HP:0000010**) (dokponou2024spinalcordinfarction pages 7-8)
- Dysphagia (**HP:0002015**) (dokponou2024spinalcordinfarction pages 3-5)
- Respiratory distress/failure (**HP:0002098**) (dokponou2024spinalcordinfarction pages 3-5)

(Exact HPO IDs should be validated during knowledge base curation; the above are suggested mappings consistent with the phenotype descriptions.)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and pathogenic variants
Spinal cord ischemia/infarction is **not primarily a monogenic disorder** in the retrieved evidence, and no specific causal genes/variants were identified.

### 4.2 Molecular and cellular mechanisms (pathophysiology)
#### Causal chain (spontaneous and perioperative)
1) **Upstream triggers**
- Arterial occlusion/embolism, aortic disease/dissection, vertebral artery dissection, systemic hypoperfusion/hypotension, perioperative segmental artery coverage or cross-clamping (dokponou2024spinalcordinfarction pages 1-2, torre2025spinalcordprotection pages 1-2)

2) **Perfusion failure and threshold physiology**
- Spinal cord perfusion pressure (SCPP) is conceptualized as **MAP − CSF pressure**; lowering intrathecal CSF pressure (e.g., via CSF drainage) and/or raising MAP can increase SCPP. (nasir2023safetyofcerebrospinal pages 6-7, torre2025spinalcordprotection pages 10-11)

3) **Tissue vulnerability and vascular territories**
- **Anterior spinal artery (ASA)** territory ischemia affects anterior horns/corticospinal/spinothalamic pathways, producing motor deficits, pain/temperature loss, and autonomic dysfunction; posterior spinal artery involvement more strongly affects vibration/proprioception modalities. (zedde2025spinalcordinfarction pages 6-8)

4) **Downstream molecular injury cascades**
In aortic-surgery focused synthesis, secondary injury mechanisms include:
- **Glutamate excitotoxicity**
- **Oxidative stress / reactive oxygen species (ROS)**
- **Mitochondrial dysfunction**
- **Blood–spinal cord barrier disruption**
- **Inflammation**
- **Calcium influx**
These are highlighted especially for ischemia–reperfusion contexts (open repair) and for sustained hypoperfusion contexts (TEVAR). (torre2025spinalcordprotection pages 1-2, torre2025spinalcordprotection pages 2-4)

#### GO term suggestions (biological processes; examples)
- Response to hypoxia (GO:0001666)
- Ischemia–reperfusion injury (often curated via related GO terms such as response to oxidative stress GO:0006979)
- Glutamate receptor signaling pathway (GO:0007215)
- Mitochondrial dysfunction/mitochondrial depolarization (use appropriate GO mitochondrial process terms during curation)
- Inflammatory response (GO:0006954)
- Regulation of blood–brain barrier / blood–spinal cord barrier (curation may use BBB-related GO terms as proxy)

#### CL term suggestions (cell types)
- Neuron (CL:0000540), including spinal motor neuron (specific CL terms may be used)
- Astrocyte (CL:0000127)
- Microglial cell (CL:0000129)
- Oligodendrocyte (CL:0000128)
- Endothelial cell (CL:0000115)

---

## 5. Environmental Information
Spinal cord ischemia/infarction is most strongly linked in the retrieved evidence to:
- **Iatrogenic/surgical exposures** (open aortic repair, TEVAR) (chen2023prophylacticcerebrospinalfluid pages 1-2, nasir2023safetyofcerebrospinal pages 1-3)
- **Hemodynamic exposures** (hypotension/hypovolemia as hypoperfusion drivers) (torre2025spinalcordprotection pages 2-4)

No specific toxin/pollution/occupational exposures were identified in the retrieved sources.

---

## 6. Mechanism / Pathophysiology

### 6.1 Integrated mechanism summary
Aortic-surgery focused synthesis emphasizes the **collateral network concept** for cord perfusion (segmental arteries plus proximal/distal contributors), and notes two injury patterns:
- **Ischemia–reperfusion injury** (more typical after open repair/cross-clamping)
- **Sustained hypoperfusion/energy failure** (typical of TEVAR due to segmental artery coverage) (torre2025spinalcordprotection pages 2-4)

### 6.2 Biomarkers / molecular profiling (limited but emerging)
A prospective observational cohort (TURBO; NCT04523909) leverages standard-of-care lumbar drains to measure perioperative CSF inflammatory markers (e.g., IL6, IL8, IL10, MCP-1) and neural injury markers (NFL, S100B, GFAP, UCHL1, NSE), aiming to characterize neuroinflammatory trajectories in thoracic aortic surgery patients. (NCT04523909 chunk 1)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Primary: **Spinal cord** (UBERON:0002240)
- Often emphasized regions: thoracic cord, thoracolumbar region, conus (zedde2025spinalcordinfarction pages 2-4, zedde2025spinalcordinfarction pages 8-10)

### 7.2 Vascular territories
- **Anterior spinal artery territory** is commonly involved; posterior spinal artery infarcts are less common but recognized. (zedde2025spinalcordinfarction pages 10-11, zedde2025spinalcordinfarction pages 6-8)

### 7.3 Subcellular / compartment suggestions (hypothesis-supporting)
Given oxidative stress/mitochondrial dysfunction emphasis, mitochondrion (GO:0005739) is a plausible key compartment for injury cascades in ischemia–reperfusion contexts. (torre2025spinalcordprotection pages 2-4)

---

## 8. Temporal Development

### 8.1 Onset pattern
- Commonly **acute/hyperacute** with rapid progression to nadir; strong diagnostic support for **severe deficit reaching nadir <12 h**. (zedde2025spinalcordinfarction pages 18-20, dokponou2024spinalcordinfarction pages 3-5)

### 8.2 Course and recovery
Functional outcomes can improve substantially in aggregate: Dokponou et al. report median mRS improving from 3 at admission to 1 at ~12 months in pooled data. (dokponou2024spinalcordinfarction pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
#### Spontaneous spinal cord infarction
A 2025 review synthesis reports:
- SCI estimated at ~1–2% of all strokes and 5–8% of acute myelopathies
- Population incidence estimates ~1.5–3.1 per 100,000 person-years (zedde2025spinalcordinfarction pages 2-4)

A 2024 systematic review reiterates rarity and estimates ~0.3–1% of all strokes. (dokponou2024spinalcordinfarction pages 1-2)

#### Peri-TEVAR spinal cord ischemia
A 2023 meta-analysis (40 studies; n=4,793) estimated pooled TEVAR spinal cord ischemia incidence:
- Overall 3.5% (95% CI 2.6–4.4)
- Immediate 1.3%
- Delayed 1.9% (chen2023prophylacticcerebrospinalfluid pages 6-7)

For TEVAR in type B aortic dissection specifically, a 2024 systematic review (34 studies; n=2,749) reported pooled permanent SCI 2.0% (95% CI 1.0–3.0) and temporary SCI 1.0% (95% CI 0.0–1.0). (zheng2024systematicreviewof pages 1-2)

---

## 10. Diagnostics

### 10.1 Imaging and diagnostic pathway
A 2025 review emphasizes that MRI is central but may be negative early; DWI can help but is imperfect.
- Initial MRI abnormal in ~75% (review synthesis), yet up to ~50% of T2 images may be negative within 24 h and a material fraction can have normal initial MRI despite severe deficits. (zedde2025spinalcordinfarction pages 8-10)
- DWI is recommended with ADC confirmation; DWI restriction often appears early (reported from the third hour) and ADC may normalize after ~7 days. (zedde2025spinalcordinfarction pages 10-11)

Typical MRI patterns:
- Axial “**owl’s eyes**” sign (central gray matter) and sagittal “**pencil-like**” anterior cord hyperintensity (zedde2025spinalcordinfarction pages 8-10)
- In one pooled dataset, owl’s-eye T2 finding was reported in 48.2% (dokponou2024spinalcordinfarction pages 3-5)

Recommended acute workup in suspected infarction includes emergent CTA chest/abdomen to exclude aortic pathology followed by ischemia-sensitive spinal MRI sequences (DWI/ADC). (zedde2025spinalcordinfarction pages 8-10)

### 10.2 CSF/labs
CSF is typically **non-inflammatory**, reported as non-inflammatory in 92% in review synthesis. (zedde2025spinalcordinfarction pages 6-8)

### 10.3 Differential diagnosis
Important mimics include compressive causes such as spinal epidural or intramedullary hematoma (cord compression). (dokponou2024spinalcordinfarction pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Functional outcomes
In pooled data, functional improvement over months is common:
- Median mRS improved from 3 at admission to 1 at ~12 months (Dokponou 2024 synthesis). (dokponou2024spinalcordinfarction pages 1-2)

### 11.2 Mortality
- Dokponou et al. reported mortality 13.4% in their pooled systematic review. (dokponou2024spinalcordinfarction pages 3-5)

In open aortic repair series with CSF drainage (n=132), in-hospital mortality was 7.6%. (nasir2023safetyofcerebrospinal pages 1-3)

---

## 12. Treatment

### 12.1 Spontaneous spinal cord infarction (medical/supportive)
In the 2024 pooled analysis, the most common management was **medical treatment plus physiotherapy** (68.9%), with **surgical decompression** used in 22.8%. (dokponou2024spinalcordinfarction pages 3-5)

MAXO suggestions (to be validated in ontology mapping):
- Rehabilitation therapy / physiotherapy
- Supportive care
- Surgical decompression (when indicated by compressive pathology or selected cases)

### 12.2 Perioperative prevention and management in aortic surgery
Core principle: preserve spinal cord perfusion pressure and collateral circulation.
- SCPP concept: **SCPP = MAP − CSF pressure** (nasir2023safetyofcerebrospinal pages 6-7)
- Strategies: CSF drainage, permissive/induced hypertension, distal aortic perfusion, staged repair, neuromonitoring, collateral preservation/revascularization. (torre2025spinalcordprotection pages 1-2, torre2025spinalcordprotection pages 18-18)

#### CSF drainage evidence (2023–2024)
- TEVAR meta-analysis (Chen 2023): no significant reduction in SCI with prophylactic CSF drainage vs no drainage, but measurable complication risk (major complications 1.6%; epidural/spinal hematoma ~0.9%; intracranial/subdural hemorrhage ~0.8%). (chen2023prophylacticcerebrospinalfluid pages 6-7, chen2023prophylacticcerebrospinalfluid pages 10-14)
- Type B dissection TEVAR systematic review (Zheng 2024): prophylactic CSF drainage not associated with lower permanent SCI (2.0% vs 2.0%) or mortality. (zheng2024systematicreviewof pages 1-2)

In open DTAA/TAAA repair series (Nasir 2023), permanent paraplegia was 3.0% with routine CSF drainage, with CSF drain complications 19% overall (mostly minor) but including serious hemorrhagic events. (nasir2023safetyofcerebrospinal pages 1-3, nasir2023safetyofcerebrospinal pages 6-7)

#### Guidelines / expert synthesis (aortic surgery)
A 2025 expert review summarizes that guideline support is strongest for open TAAA and more conditional for high-risk endovascular procedures (e.g., EACTS/STS 2024 strong recommendation for open TAAA; consider prophylactic drainage for high-risk endovascular cases). (torre2025spinalcordprotection pages 10-11)

MAXO suggestions (perioperative aortic contexts):
- Cerebrospinal fluid drainage
- Blood pressure management / induced hypertension
- Distal aortic perfusion
- Intraoperative neuromonitoring
- Endovascular aortic repair / open aortic repair (procedure ontology mapping)

---

## 13. Prevention

### 13.1 Primary prevention
Not applicable in the conventional public-health sense for spontaneous SCI due to heterogeneous etiologies and rarity; prevention focuses on general vascular risk reduction (hypertension/smoking management) and surgical risk mitigation.

### 13.2 Secondary/tertiary prevention (perioperative)
In aortic surgery, prevention is protocol-driven, emphasizing physiologic protection (SCPP optimization) and rapid rescue because the window to reverse deficits may be short (often discussed as 1–2 hours in expert synthesis). (torre2025spinalcordprotection pages 10-11)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary syndrome was identified in the retrieved sources; the animal evidence primarily concerns **induced experimental models**.

---

## 15. Model Organisms

### 15.1 Model systems used
A systematic review of preclinical aortic cross-clamping models reports use of:
- Mouse, rat, rabbit, dog, pig, baboon, sheep (awad2021histologicalfindingsafter pages 1-2)

A review of models emphasizes that ischemia duration needed for paralysis scales by species (mice ~9–11 min; dogs/pigs ~45–60 min), and that vascular anatomy differences (e.g., artery of Adamkiewicz/radiculomedullary supply) influence reproducibility and translational validity. (awad2013animalmodelsof pages 20-22, awad2013animalmodelsof pages 1-4)

### 15.2 Representative models and applications
- **Mouse aortic cross-clamp model** producing ischemic spinal cord injury with cross-clamp durations of 3–11 minutes and locomotor outcomes assessed by Basso Mouse Scale. (awad2010amousemodel pages 2-4)
- **Canine endovascular embolic model** enabling serial clinical-scanner DWI/ADC characterization; DWI hyperintensity observed within 1 hour and biphasic ADC evolution. (zhang2007temporalevolutionof pages 1-2)

### 15.3 Key conserved pathology
Across cross-clamp models, injury is predominantly in **gray matter**, though white matter injury can occur. (awad2021histologicalfindingsafter pages 1-2)

---

## Recent developments and real-world implementations (2023–2024 priority)

### A. Diagnostic and clinical characterization consolidation
The 2024 systematic review/meta-analysis provides consolidated, quantitative evidence on time-to-nadir, phenotype distributions, imaging signs (owl’s-eye), management patterns, and mRS improvement. (dokponou2024spinalcordinfarction pages 3-5, dokponou2024spinalcordinfarction pages 1-2)

### B. TEVAR spinal cord ischemia prevention evidence update
2023–2024 evidence syntheses converge on a key controversy: **routine prophylactic CSF drainage has not shown clear pooled benefit in TEVAR**, while carrying non-trivial complication risks; selective/high-risk approaches and protocol standardization remain active areas. (chen2023prophylacticcerebrospinalfluid pages 6-7, zheng2024systematicreviewof pages 1-2)

### C. Active clinical research directions (trials)
- NCT04941157: randomized pilot of prophylactic vs therapeutic CSF drain strategy with SCI endpoint (post-op neurologic deficits) (NCT04941157 chunk 1)
- NCT04523909: perioperative CSF cytokines and injury biomarkers around thoracic aortic surgery (NCT04523909 chunk 1)
- NCT04600089: ketamine for opioid-sparing analgesia in TEVAR patients receiving naloxone infusion as an SCI-prophylaxis bundle component (NCT04600089 chunk 1)

---

## Evidence table (structured summary)
| Topic | Citation (authors, year) | PMID/DOI | Publication date (month/year) | Key quantitative findings | Key conclusion/implication | URL |
|---|---|---|---|---|---|---|
| Spontaneous spinal cord infarction / general SCI overview | Dokponou et al., 2024 | DOI: 10.25259/sni_477_2024 | 09/2024 | Systematic review of 117 articles/876 patients; mean age 51.1 ± 19.4 years; 64.4% male; acute spinal cord infarction estimated at ~0.3–1% of all strokes; time to nadir: <6 h 56.1%, 6–12 h 30.7%, 12–72 h 5.4%, >72 h 7.8%; MRI alone used in 64.4%; “owl’s eye” sign 48.2%; T2DWI AUC 0.835 for hyperacute detection; 68.9% received medical therapy + physiotherapy, 22.8% surgical decompression; median mRS improved from 3 at admission to 1 at ~12 months; mortality 13.4% (dokponou2024spinalcordinfarction pages 3-5, dokponou2024spinalcordinfarction pages 1-2, dokponou2024spinalcordinfarction pages 2-3) | Rare ischemic myelopathy with hyperacute presentation in most cases; MRI/DWI are helpful but imperfect early; outcomes can improve substantially with diagnosis, supportive care, and rehabilitation. | https://doi.org/10.25259/sni_477_2024 |
| Spontaneous spinal cord infarction / epidemiology and incidence | Zedde et al., 2025 | DOI: 10.3390/jcm14041293 | 02/2025 | Review estimates SCI at ~1–2% of all strokes and 5–8% of acute myelopathies; population incidence ~1.5–3.1 per 100,000 person-years; about 8% in multilevel aortic disease; prevalence may reach up to 33% after thoraco-abdominal aortic surgery; typical age 6th–7th decades; vascular risk factors reported: hypertension 40%, smoking 30%, dyslipidemia 29%, diabetes 16%; ~28% lacked reported vascular risks (zedde2025spinalcordinfarction pages 2-4, zedde2025spinalcordinfarction pages 18-20) | SCI is probably under-recognized; rapid onset-to-nadir (<12 h) is a strong diagnostic clue, and epidemiologic burden is likely underestimated. | https://doi.org/10.3390/jcm14041293 |
| TEVAR / prophylactic CSF drainage meta-analysis | Chen et al., 2023 | DOI: 10.21037/acs-2023-scp-17 | 09/2023 | Meta-analysis of 40 studies/4,793 TEVAR patients; pooled SCI incidence 3.5% (95% CI 2.6–4.4), immediate SCI 1.3%, delayed SCI 1.9%; no significant difference with CSFD vs no CSFD for any SCI (OR 1.34, 95% CI 0.88–2.04), transient SCI (OR 1.84, 95% CI 0.95–3.54), or permanent SCI (OR 1.25, 95% CI 0.47–3.30); selective CSFD associated with increased transient SCI (OR 2.08, 95% CI 1.06–4.08); CSFD complications: spinal headache 4.3%, major complications 1.6%, epidural/spinal hematoma 0.9%, intracranial/subdural hemorrhage 0.8%, death 0.6%; perioperative mortality 1.7%, mid-term mortality 4.5% (chen2023prophylacticcerebrospinalfluid pages 1-2, chen2023prophylacticcerebrospinalfluid pages 6-7, chen2023prophylacticcerebrospinalfluid pages 10-14) | In endovascular thoracic/thoracoabdominal repair, prophylactic CSFD has not shown clear pooled benefit for reducing SCI and is not benign; patient selection and protocol standardization remain important. | https://doi.org/10.21037/acs-2023-scp-17 |
| TEVAR for type B aortic dissection / CSF drainage systematic review | Zheng et al., 2024 | DOI: 10.1186/s13019-024-02603-3 | 03/2024 | Systematic review of 34 studies/2,749 patients; pooled permanent SCI 2.0% (95% CI 1.0–3.0); temporary SCI 1.0% (95% CI 0.0–1.0); no significant difference in permanent SCI with prophylactic CSFD vs none (2.0% vs 2.0%; P=0.445); no difference between routine vs selective CSFD (P=0.596); 30-day/in-hospital mortality 4.0% with prophylactic CSFD vs 5.0% without (P=0.525); mean Downs and Black score 8.71 (zheng2024systematicreviewof pages 5-7, zheng2024systematicreviewof pages 2-5, zheng2024systematicreviewof pages 1-2) | For TEVAR in type B aortic dissection, pooled nonrandomized data do not support a reduction in permanent SCI or short-term mortality from prophylactic CSFD. | https://doi.org/10.1186/s13019-024-02603-3 |
| Open descending thoracic/thoracoabdominal aortic repair / CSF drainage safety | Nasir et al., 2023 | DOI: 10.21037/acs-2023-scp-0121 | 09/2023 | Single-center 17-year series, n=132 with routine CSFD; in-hospital mortality 7.6%; transient paresis 3.8%; permanent paraplegia 3.0%; CSFD complications 19% overall, including persistent CSF leak 7%, blood-tinged CSF 11%, subdural hematoma in 3 patients, spinal cutaneous fistula 1%; survival 86.4% at 1 year, 75.2% at 5 years, 50.9% at 15 years; ACC/AHA recommendation cited as Class I, Level A for open TAAA repair (nasir2023safetyofcerebrospinal pages 1-3, nasir2023safetyofcerebrospinal pages 4-6, nasir2023safetyofcerebrospinal pages 6-7, nasir2023safetyofcerebrospinal pages 3-4) | In open DTAA/TAAA repair, CSFD remains a commonly used protective adjunct with accepted complication risk; evidence and guidelines are stronger here than for TEVAR. | https://doi.org/10.21037/acs-2023-scp-0121 |
| Guideline/review synthesis for aortic-surgery spinal cord protection | Torre & Pirri, 2025 | DOI: 10.3389/fcvm.2025.1671350 | 09/2025 | Review cites randomized open TAAA data showing paraplegia/paraparesis 13% without vs 2.6% with CSFD; states 2024 EACTS/STS strongly recommend CSFD for open TAAA replacement (Class I, Level B) and advise considering prophylactic drainage for high-risk endovascular cases (Class IIa, Level C); also notes insufficient evidence for routine prophylactic drainage in endovascular procedures (torre2025spinalcordprotection pages 10-11) | Current expert guidance supports CSFD most strongly for open TAAA repair, while high-risk TEVAR decisions should be individualized within bundled spinal cord protection strategies. | https://doi.org/10.3389/fcvm.2025.1671350 |
| Trial: prophylactic vs therapeutic drain strategy in endovascular TAAA repair | NCT04941157 |  | 2022 (registry record) | Randomized pilot interventional study; enrollment 20; compares prophylactic CSF drain placement before high-risk endovascular thoracoabdominal aneurysm repair vs selective/therapeutic placement only if SCI develops; primary outcome: rate of postoperative spinal cord ischemia over 1 year, defined as new lower-extremity neurologic deficit, assessed with Muscle Power Scale (NCT04941157 chunk 2, NCT04941157 chunk 1) | Directly addresses a major unresolved clinical question: whether pre-emptive drain placement improves neurologic outcomes enough to justify drain-related risk. | https://clinicaltrials.gov/study/NCT04941157 |
| Trial: ketamine during TEVAR patients receiving naloxone continuous infusion for SCI prophylaxis | NCT04600089 |  | 2020 (registry record) | Phase 2 randomized double-blind placebo-controlled trial; enrollment 30; ketamine infusion 0.2 mg/kg/h vs saline for 48 h in TEVAR patients receiving naloxone continuous infusion for spinal ischemia prophylaxis; primary outcome cumulative opioid dose over 48 h; secondary outcomes pain scores, delirium (CAM-ICU), uncontrolled hypertension (NCT04600089 chunk 1) | Tests an analgesic strategy within an SCI-prevention bundle, addressing the pain/opioid burden introduced by naloxone-based prophylaxis rather than SCI efficacy directly. | https://clinicaltrials.gov/study/NCT04600089 |
| Trial: CSF neuroinflammatory biomarkers around thoracic aortic surgery | NCT04523909 |  | 2017 (registry record) | Prospective observational cohort; enrollment 100; serial CSF and blood sampling across 9 perioperative timepoints to measure IL6, IL8, IL10, MCP-1, IL1RA, CX3CL1 and markers including NFL, S100B, GFAP, UCHL1, NSE; lumbar drain placed as standard care to reduce periprocedural spinal cord ischemia risk (NCT04523909 chunk 1) | Important translational study for biomarker discovery and mechanistic monitoring; may inform future prediction of perioperative neurologic injury, though it is not an intervention trial for SCI prevention. | https://clinicaltrials.gov/study/NCT04523909 |


*Table: This table summarizes recent core evidence on spontaneous spinal cord infarction and perioperative spinal cord ischemia prevention in aortic surgery. It highlights incidence estimates, imaging and outcome data, CSF drainage meta-analyses, guideline interpretations, and ongoing clinical trial directions.*

---

## Visual evidence from a key 2023 meta-analysis
Chen et al. (2023) provides forest plots and tables summarizing CSF drainage vs no drainage outcomes and complication rates; these were retrieved as cropped figure/table images, including the main results table, forest plots, and CSF-drain complication table. (chen2023prophylacticcerebrospinalfluid media cf49819c, chen2023prophylacticcerebrospinalfluid media 628d27e4, chen2023prophylacticcerebrospinalfluid media 3b07512f, chen2023prophylacticcerebrospinalfluid media 2ef757c8, chen2023prophylacticcerebrospinalfluid media 0f2ce663)

---

## Limitations of this report (evidence availability)
- **Ontology identifiers (MONDO, MeSH, ICD-10/ICD-11)** were not explicitly present in the retrieved full text, so they are not asserted here.
- **PMIDs** were not available in the extracted evidence snippets (most sources provide DOIs and journal metadata). All sources are linked via DOI/ClinicalTrials.gov URLs.
- Some mechanistic claims (e.g., specific cytokine or excitotoxic cascades) appear in expert synthesis rather than primary mechanistic experiments in the retrieved set; preclinical modeling evidence is included to partially address this.


References

1. (dokponou2024spinalcordinfarction pages 1-2): Yao Christian Hugues Dokponou, Fresnel Lutèce Ontsi Obame, Berjo Takoutsing, Mubarak Jolayemi Mustapha, Arsène Daniel Nyalundja, Moussa Elmi Saad, Omar Boladji Adebayo Badirou, Dognon Kossi François de Paule Adjiou, Nicaise Agada Kpègnon, Alngar Djimrabeye, and Nourou Dine Adeniran Bankole. Spinal cord infarction: a systematic review and meta-analysis of patient’s characteristics, diagnosis accuracy, management, and outcome. Surgical Neurology International, 15:325, Sep 2024. URL: https://doi.org/10.25259/sni\_477\_2024, doi:10.25259/sni\_477\_2024. This article has 14 citations and is from a peer-reviewed journal.

2. (chen2023prophylacticcerebrospinalfluid pages 1-2): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

3. (zedde2025spinalcordinfarction pages 10-11): Marialuisa Zedde, Arturo De Falco, Carla Zanferrari, Maria Guarino, Francesca Romana Pezzella, Shalom Haggiag, Gianni Cossu, Rocco Quatrale, Giuseppe Micieli, Massimo Del Sette, and Rosario Pascarella. Spinal cord infarction: clinical and neuroradiological clues of a rare stroke subtype. Journal of Clinical Medicine, 14:1293, Feb 2025. URL: https://doi.org/10.3390/jcm14041293, doi:10.3390/jcm14041293. This article has 16 citations.

4. (torre2025spinalcordprotection pages 10-11): Debora Emanuela Torre and Carmelo Pirri. Spinal cord protection in open and endovascular aortic surgery: current strategies, controversies and future directions. Frontiers in Cardiovascular Medicine, Sep 2025. URL: https://doi.org/10.3389/fcvm.2025.1671350, doi:10.3389/fcvm.2025.1671350. This article has 3 citations and is from a peer-reviewed journal.

5. (dokponou2024spinalcordinfarction pages 7-8): Yao Christian Hugues Dokponou, Fresnel Lutèce Ontsi Obame, Berjo Takoutsing, Mubarak Jolayemi Mustapha, Arsène Daniel Nyalundja, Moussa Elmi Saad, Omar Boladji Adebayo Badirou, Dognon Kossi François de Paule Adjiou, Nicaise Agada Kpègnon, Alngar Djimrabeye, and Nourou Dine Adeniran Bankole. Spinal cord infarction: a systematic review and meta-analysis of patient’s characteristics, diagnosis accuracy, management, and outcome. Surgical Neurology International, 15:325, Sep 2024. URL: https://doi.org/10.25259/sni\_477\_2024, doi:10.25259/sni\_477\_2024. This article has 14 citations and is from a peer-reviewed journal.

6. (dokponou2024spinalcordinfarction pages 3-5): Yao Christian Hugues Dokponou, Fresnel Lutèce Ontsi Obame, Berjo Takoutsing, Mubarak Jolayemi Mustapha, Arsène Daniel Nyalundja, Moussa Elmi Saad, Omar Boladji Adebayo Badirou, Dognon Kossi François de Paule Adjiou, Nicaise Agada Kpègnon, Alngar Djimrabeye, and Nourou Dine Adeniran Bankole. Spinal cord infarction: a systematic review and meta-analysis of patient’s characteristics, diagnosis accuracy, management, and outcome. Surgical Neurology International, 15:325, Sep 2024. URL: https://doi.org/10.25259/sni\_477\_2024, doi:10.25259/sni\_477\_2024. This article has 14 citations and is from a peer-reviewed journal.

7. (zheng2024systematicreviewof pages 5-7): Huajie Zheng, Deqing Lin, Yongbo Cheng, Chaojun Yan, Sanjiu Yu, Jun Li, and Wei Cheng. Systematic review of the effect of cerebrospinal fluid drainage on outcomes after endovascular type b aortic dissection repair. Journal of Cardiothoracic Surgery, Mar 2024. URL: https://doi.org/10.1186/s13019-024-02603-3, doi:10.1186/s13019-024-02603-3. This article has 2 citations and is from a peer-reviewed journal.

8. (nasir2023safetyofcerebrospinal pages 1-3): Afsheen Nasir, Mohammad A. Zafar, Mohamed Abdelbaky, Dimitra Papanikolaou, Hesham Ellauzi, Maryam Shaikh, Bulat A. Ziganshin, and John A. Elefteriades. Safety of cerebrospinal ﬂuid drainage in descending and thoracoabdominal aortic replacement surgery. Annals of Cardiothoracic Surgery, 12:476-483, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-0121, doi:10.21037/acs-2023-scp-0121. This article has 5 citations.

9. (NCT04941157 chunk 1): Adam W Beck. Prophylactic vs Therapeutic Cerebrospinal Fluid Drain Placement During Endovascular Thoracoabdominal Aortic Aneurysm Repair. University of Alabama at Birmingham. 2022. ClinicalTrials.gov Identifier: NCT04941157

10. (NCT04600089 chunk 1): Sam Tyagi. Ketamine in Patients Undergoing TEVAR Procedures Receiving NCI. Sam Tyagi. 2020. ClinicalTrials.gov Identifier: NCT04600089

11. (NCT04523909 chunk 1): Wilson F. Abdo. Trajectory of Neuroinflammatory Markers in Cerebrospinal Fluid Prior to and After Thoracic Aortic Surgery. Radboud University Medical Center. 2017. ClinicalTrials.gov Identifier: NCT04523909

12. (torre2025spinalcordprotection pages 1-2): Debora Emanuela Torre and Carmelo Pirri. Spinal cord protection in open and endovascular aortic surgery: current strategies, controversies and future directions. Frontiers in Cardiovascular Medicine, Sep 2025. URL: https://doi.org/10.3389/fcvm.2025.1671350, doi:10.3389/fcvm.2025.1671350. This article has 3 citations and is from a peer-reviewed journal.

13. (nasir2023safetyofcerebrospinal pages 6-7): Afsheen Nasir, Mohammad A. Zafar, Mohamed Abdelbaky, Dimitra Papanikolaou, Hesham Ellauzi, Maryam Shaikh, Bulat A. Ziganshin, and John A. Elefteriades. Safety of cerebrospinal ﬂuid drainage in descending and thoracoabdominal aortic replacement surgery. Annals of Cardiothoracic Surgery, 12:476-483, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-0121, doi:10.21037/acs-2023-scp-0121. This article has 5 citations.

14. (zedde2025spinalcordinfarction pages 2-4): Marialuisa Zedde, Arturo De Falco, Carla Zanferrari, Maria Guarino, Francesca Romana Pezzella, Shalom Haggiag, Gianni Cossu, Rocco Quatrale, Giuseppe Micieli, Massimo Del Sette, and Rosario Pascarella. Spinal cord infarction: clinical and neuroradiological clues of a rare stroke subtype. Journal of Clinical Medicine, 14:1293, Feb 2025. URL: https://doi.org/10.3390/jcm14041293, doi:10.3390/jcm14041293. This article has 16 citations.

15. (zedde2025spinalcordinfarction pages 6-8): Marialuisa Zedde, Arturo De Falco, Carla Zanferrari, Maria Guarino, Francesca Romana Pezzella, Shalom Haggiag, Gianni Cossu, Rocco Quatrale, Giuseppe Micieli, Massimo Del Sette, and Rosario Pascarella. Spinal cord infarction: clinical and neuroradiological clues of a rare stroke subtype. Journal of Clinical Medicine, 14:1293, Feb 2025. URL: https://doi.org/10.3390/jcm14041293, doi:10.3390/jcm14041293. This article has 16 citations.

16. (zedde2025spinalcordinfarction pages 8-10): Marialuisa Zedde, Arturo De Falco, Carla Zanferrari, Maria Guarino, Francesca Romana Pezzella, Shalom Haggiag, Gianni Cossu, Rocco Quatrale, Giuseppe Micieli, Massimo Del Sette, and Rosario Pascarella. Spinal cord infarction: clinical and neuroradiological clues of a rare stroke subtype. Journal of Clinical Medicine, 14:1293, Feb 2025. URL: https://doi.org/10.3390/jcm14041293, doi:10.3390/jcm14041293. This article has 16 citations.

17. (torre2025spinalcordprotection pages 2-4): Debora Emanuela Torre and Carmelo Pirri. Spinal cord protection in open and endovascular aortic surgery: current strategies, controversies and future directions. Frontiers in Cardiovascular Medicine, Sep 2025. URL: https://doi.org/10.3389/fcvm.2025.1671350, doi:10.3389/fcvm.2025.1671350. This article has 3 citations and is from a peer-reviewed journal.

18. (zedde2025spinalcordinfarction pages 18-20): Marialuisa Zedde, Arturo De Falco, Carla Zanferrari, Maria Guarino, Francesca Romana Pezzella, Shalom Haggiag, Gianni Cossu, Rocco Quatrale, Giuseppe Micieli, Massimo Del Sette, and Rosario Pascarella. Spinal cord infarction: clinical and neuroradiological clues of a rare stroke subtype. Journal of Clinical Medicine, 14:1293, Feb 2025. URL: https://doi.org/10.3390/jcm14041293, doi:10.3390/jcm14041293. This article has 16 citations.

19. (chen2023prophylacticcerebrospinalfluid pages 6-7): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

20. (zheng2024systematicreviewof pages 1-2): Huajie Zheng, Deqing Lin, Yongbo Cheng, Chaojun Yan, Sanjiu Yu, Jun Li, and Wei Cheng. Systematic review of the effect of cerebrospinal fluid drainage on outcomes after endovascular type b aortic dissection repair. Journal of Cardiothoracic Surgery, Mar 2024. URL: https://doi.org/10.1186/s13019-024-02603-3, doi:10.1186/s13019-024-02603-3. This article has 2 citations and is from a peer-reviewed journal.

21. (torre2025spinalcordprotection pages 18-18): Debora Emanuela Torre and Carmelo Pirri. Spinal cord protection in open and endovascular aortic surgery: current strategies, controversies and future directions. Frontiers in Cardiovascular Medicine, Sep 2025. URL: https://doi.org/10.3389/fcvm.2025.1671350, doi:10.3389/fcvm.2025.1671350. This article has 3 citations and is from a peer-reviewed journal.

22. (chen2023prophylacticcerebrospinalfluid pages 10-14): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

23. (awad2021histologicalfindingsafter pages 1-2): Hamdy Awad, Alexander Efanov, Jayanth Rajan, Andrew Denney, Bradley Gigax, Peter Kobalka, Hesham Kelani, D Michele Basso, John Bozinovski, and Esmerina Tili. Histological findings after aortic cross-clamping in preclinical animal models. Journal of neuropathology and experimental neurology, 80:895-911, Sep 2021. URL: https://doi.org/10.1093/jnen/nlab084, doi:10.1093/jnen/nlab084. This article has 12 citations and is from a peer-reviewed journal.

24. (awad2013animalmodelsof pages 20-22): Hamdy Awad, Haytham Elgharably, and Phillip Popovich. Animal models of spinal cord ischemia. ArXiv, pages 225-254, Oct 2013. URL: https://doi.org/10.1007/978-1-62703-197-4\_11, doi:10.1007/978-1-62703-197-4\_11. This article has 3 citations.

25. (awad2013animalmodelsof pages 1-4): Hamdy Awad, Haytham Elgharably, and Phillip Popovich. Animal models of spinal cord ischemia. ArXiv, pages 225-254, Oct 2013. URL: https://doi.org/10.1007/978-1-62703-197-4\_11, doi:10.1007/978-1-62703-197-4\_11. This article has 3 citations.

26. (awad2010amousemodel pages 2-4): Hamdy Awad, Daniel P. Ankeny, Zhen Guan, Ping Wei, Dana M. McTigue, and Phillip G. Popovich. A mouse model of ischemic spinal cord injury with delayed paralysis caused by aortic cross-clamping. Anesthesiology, 113:880-891, Oct 2010. URL: https://doi.org/10.1097/aln.0b013e3181ec61ee, doi:10.1097/aln.0b013e3181ec61ee. This article has 72 citations and is from a domain leading peer-reviewed journal.

27. (zhang2007temporalevolutionof pages 1-2): Jin Song Zhang, Yi Huan, Li Jun Sun, Ya Li Ge, Xue Xin Zhang, and Ying Juan Chang. Temporal evolution of spinal cord infarction in an in vivo experimental study of canine models characterized by diffusion‐weighted imaging. Journal of Magnetic Resonance Imaging, 26:848-854, Oct 2007. URL: https://doi.org/10.1002/jmri.21044, doi:10.1002/jmri.21044. This article has 18 citations and is from a domain leading peer-reviewed journal.

28. (dokponou2024spinalcordinfarction pages 2-3): Yao Christian Hugues Dokponou, Fresnel Lutèce Ontsi Obame, Berjo Takoutsing, Mubarak Jolayemi Mustapha, Arsène Daniel Nyalundja, Moussa Elmi Saad, Omar Boladji Adebayo Badirou, Dognon Kossi François de Paule Adjiou, Nicaise Agada Kpègnon, Alngar Djimrabeye, and Nourou Dine Adeniran Bankole. Spinal cord infarction: a systematic review and meta-analysis of patient’s characteristics, diagnosis accuracy, management, and outcome. Surgical Neurology International, 15:325, Sep 2024. URL: https://doi.org/10.25259/sni\_477\_2024, doi:10.25259/sni\_477\_2024. This article has 14 citations and is from a peer-reviewed journal.

29. (zheng2024systematicreviewof pages 2-5): Huajie Zheng, Deqing Lin, Yongbo Cheng, Chaojun Yan, Sanjiu Yu, Jun Li, and Wei Cheng. Systematic review of the effect of cerebrospinal fluid drainage on outcomes after endovascular type b aortic dissection repair. Journal of Cardiothoracic Surgery, Mar 2024. URL: https://doi.org/10.1186/s13019-024-02603-3, doi:10.1186/s13019-024-02603-3. This article has 2 citations and is from a peer-reviewed journal.

30. (nasir2023safetyofcerebrospinal pages 4-6): Afsheen Nasir, Mohammad A. Zafar, Mohamed Abdelbaky, Dimitra Papanikolaou, Hesham Ellauzi, Maryam Shaikh, Bulat A. Ziganshin, and John A. Elefteriades. Safety of cerebrospinal ﬂuid drainage in descending and thoracoabdominal aortic replacement surgery. Annals of Cardiothoracic Surgery, 12:476-483, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-0121, doi:10.21037/acs-2023-scp-0121. This article has 5 citations.

31. (nasir2023safetyofcerebrospinal pages 3-4): Afsheen Nasir, Mohammad A. Zafar, Mohamed Abdelbaky, Dimitra Papanikolaou, Hesham Ellauzi, Maryam Shaikh, Bulat A. Ziganshin, and John A. Elefteriades. Safety of cerebrospinal ﬂuid drainage in descending and thoracoabdominal aortic replacement surgery. Annals of Cardiothoracic Surgery, 12:476-483, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-0121, doi:10.21037/acs-2023-scp-0121. This article has 5 citations.

32. (NCT04941157 chunk 2): Adam W Beck. Prophylactic vs Therapeutic Cerebrospinal Fluid Drain Placement During Endovascular Thoracoabdominal Aortic Aneurysm Repair. University of Alabama at Birmingham. 2022. ClinicalTrials.gov Identifier: NCT04941157

33. (chen2023prophylacticcerebrospinalfluid media cf49819c): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

34. (chen2023prophylacticcerebrospinalfluid media 628d27e4): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

35. (chen2023prophylacticcerebrospinalfluid media 3b07512f): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

36. (chen2023prophylacticcerebrospinalfluid media 2ef757c8): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.

37. (chen2023prophylacticcerebrospinalfluid media 0f2ce663): Cheng-Hao Jacky Chen, Henry Jiang, and Vinh Dat David Nguyen. Prophylactic cerebrospinal fluid drainage and spinal cord ischemia in thoracic and thoracoabdominal endovascular procedures: a systematic review and meta-analysis. Annals of Cardiothoracic Surgery, 12:392-408, Sep 2023. URL: https://doi.org/10.21037/acs-2023-scp-17, doi:10.21037/acs-2023-scp-17. This article has 13 citations.