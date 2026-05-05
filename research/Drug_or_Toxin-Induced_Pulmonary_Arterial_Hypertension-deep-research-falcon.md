---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-04T21:37:00.711131'
end_time: '2026-05-04T21:56:43.859200'
duration_seconds: 1183.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Drug- or Toxin-Induced Pulmonary Arterial Hypertension
  mondo_id: ''
  category: Environmental
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Drug- or Toxin-Induced Pulmonary Arterial Hypertension
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Drug- or Toxin-Induced Pulmonary Arterial Hypertension** covering all of the
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
- **Disease Name:** Drug- or Toxin-Induced Pulmonary Arterial Hypertension
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Drug- or Toxin-Induced Pulmonary Arterial Hypertension** covering all of the
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


# Research Report: Drug- or Toxin-Induced Pulmonary Arterial Hypertension (DTI-PAH)

## Executive summary
Drug- or toxin-induced pulmonary arterial hypertension (DTI-PAH) is a **Group 1 pulmonary arterial hypertension (PAH)** subtype in the World Symposium/ESC-ERS clinical classification, in which **exposure to specific drugs or toxins is judged causally implicated** (with strength graded as “definite” or “possible”). Diagnosis generally requires confirmation of **pre-capillary PH by right heart catheterization** and exclusion of other causes of pulmonary hypertension, plus a compatible exposure history; management includes **cessation of the culprit exposure**, risk-stratified PAH therapy, and in some etiologies (e.g., interferon- or dasatinib-associated PAH) a short period of observation may be reasonable for low-risk patients to assess reversibility. Recent 2023–2024 literature emphasizes: (i) rising burden of **methamphetamine-associated PAH**, including large increases in U.S. hospitalizations and high adjusted prevalence ratios among methamphetamine users; (ii) continued refinement of evidence-based culprit lists; and (iii) newer disease-modifying treatments in PAH generally (e.g., **sotatercept**) now incorporated into updated algorithms. (dardi2024riskstratificationand pages 22-24, dardi2024riskstratificationand pages 66-68, chin2024treatmentalgorithmfor pages 11-12, iwata2024trendsandpatterns pages 1-2, chin2024treatmentalgorithmfor pages 7-8, chin2024treatmentalgorithmfor pages 2-3)

---

## 1. Disease information
### 1.1 Definition and overview
DTI-PAH (also termed **drug- or toxin-associated PAH**) is a subtype of **Group 1 PAH** in which PAH occurs in individuals exposed to a suspected causal drug/toxin. Contemporary guidelines/reviews emphasize that drug/toxin-associated PAH can be **clinically indistinguishable** from idiopathic PAH and often requires careful exclusion of other etiologies before attribution. (dardi2024riskstratificationand pages 66-68, iii2020drugandtoxininduced pages 1-3)

Hemodynamic definition of PAH (pre-capillary PH) by right heart catheterization includes **mPAP >20 mmHg**, **PAWP <15 mmHg**, and **increased PVR** (e.g., PVR >2 WU noted in recent definitions). (shafeghat2025stateofthe pages 2-4, chin2024treatmentalgorithmfor pages 5-7)

### 1.2 Terminology and synonyms
Common terms used in recent authoritative sources include:
- “**drug- or toxin-associated PAH**” and abbreviation **DPAH** (ERJ 2024). (dardi2024riskstratificationand pages 66-68, dardi2024riskstratificationand pages 21-22)
- “**drug-/toxin-induced PAH**” and abbreviation **DT-PAH** (ERJ 2024). (chin2024treatmentalgorithmfor pages 1-2, chin2024treatmentalgorithmfor pages 5-7)

### 1.3 Disease identifiers (ontology/coding)
- **ICD-10/ICD-11, MeSH, OMIM, Orphanet, MONDO:** Not retrievable from the currently ingested full texts/snippets in this run. The retrieved ERJ guidelines/reviews provide classification terminology (DPAH/DT-PAH) but do not list ICD/MeSH/MONDO codes in the captured excerpts. (dardi2024riskstratificationand pages 66-68, chin2024treatmentalgorithmfor pages 1-2, dardi2024riskstratificationand pages 22-24)

### 1.4 Evidence sources
Most “disease information” in this report is derived from **aggregated disease-level resources** (7th WSPH/ESC-ERS aligned ERJ documents, narrative and systematic reviews) plus **large administrative-database epidemiology** for methamphetamine-associated PAH. (chin2024treatmentalgorithmfor pages 5-7, dardi2024riskstratificationand pages 22-24, iwata2024trendsandpatterns pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factors (environmental/iatrogenic)
Guidelines classify implicated exposures as **definite** or **possible** associations with PAH; “definite” is supported by **outbreaks, epidemiologic case-control studies, or large multicentre series**, while “possible” is supported by **multiple case series** or mechanistic similarity. (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 1-3)

**Definite**: aminorex, benfluorex, dasatinib, dexfenfluramine, fenfluramine, methamphetamines, toxic rapeseed oil. (dardi2024riskstratificationand pages 22-24)

**Possible**: examples include alkylating agents (cyclophosphamide, mitomycin C), amphetamines, bosutinib, cocaine, diazoxide, sofosbuvir, Qing-Dai/indirubin, interferon α/β, leflunomide, L-tryptophan, phenylpropanolamine, ponatinib, carfilzomib, trichloroethylene, St John’s Wort. (dardi2024riskstratificationand pages 22-24)

### 2.2 Risk factors
**Exposure-related risk**
- Methamphetamine is explicitly classified as a **definite** associated exposure and is increasingly recognized in U.S. centers. (dardi2024riskstratificationand pages 22-24, dardi2024riskstratificationand pages 66-68)

**Host susceptibility (genetic and biologic factors)**
- Evidence supports a **gene–environment (“two-hit”) model**, in which only a subset of exposed individuals develop overt PAH. (iii2020drugandtoxininduced pages 19-21)
- In fenfluramine-associated PAH, **BMPR2 mutations** were reported at frequencies similar to sporadic PAH and **BMPR2 carriers required shorter exposure durations** before developing PAH—supporting genetic susceptibility modifying drug-triggered disease. (seferian2013drugsinducedpulmonary pages 2-3)

### 2.3 Protective factors
- No specific protective genetic variants or protective exposures were identified in the retrieved excerpts.

### 2.4 Gene–environment interactions
- Appetite-suppressant (fenfluramine-class) exposure plus **BMPR2 susceptibility** is a documented interaction pattern in drug-associated PAH. (seferian2013drugsinducedpulmonary pages 2-3)

**Suggested ontology terms**
- CHEBI examples (non-exhaustive): methamphetamine (CHEBI term exists), dasatinib (CHEBI term exists), fenfluramine (CHEBI term exists).

---

## 3. Phenotypes
### 3.1 Clinical symptoms and signs
Symptoms of PAH are often nonspecific early and reflect progressive RV dysfunction:
- **Progressive exertional dyspnoea** is the cardinal symptom. (dardi2024riskstratificationand pages 24-25)
- Other reported symptoms/signs in PAH include fatigue, palpitations, chest pain, syncope, fluid retention/abdominal distension/weight gain in advanced disease. (coman2025updatesonthe pages 1-2)

### 3.2 Hemodynamics (core disease phenotype)
Right heart catheterization defines pre-capillary disease using mPAP, PAWP, and PVR thresholds (e.g., mPAP >20 mmHg, PAWP <15 mmHg, and elevated PVR). (shafeghat2025stateofthe pages 2-4, chin2024treatmentalgorithmfor pages 5-7)

### 3.3 Imaging/laboratory phenotype
- ECG: right axis deviation can raise suspicion; normal ECG + normal BNP/NT-proBNP suggests low likelihood of PH. (dardi2024riskstratificationand pages 24-25)
- Chest radiography: may show RA/RV and pulmonary artery enlargement and peripheral vessel pruning; can be normal. (dardi2024riskstratificationand pages 24-25)
- Baseline labs recommended include CBC, renal/liver function, iron studies, and BNP/NT-proBNP, plus HIV/hepatitis serology and autoimmune screening in the appropriate context. (dardi2024riskstratificationand pages 31-32)

### 3.4 Phenotype frequency and onset
- For methamphetamine-associated PAH hospitalizations (U.S., 2008–2020), the hospitalized cohort skewed **male (59.16%)** and **middle-aged (41–64 years: 45.77%; 26–40 years: 37.52%)**. (iwata2024trendsandpatterns pages 3-4)

### 3.5 Suggested HPO terms (examples)
- Dyspnea (HP:0002094)
- Exertional dyspnea (HP:0002875)
- Syncope (HP:0001279)
- Fatigue (HP:0012378)
- Peripheral edema (HP:0000969)
- Right ventricular hypertrophy (HP:0001708)

(Phenotype concepts supported by PAH symptom descriptions and RV remodeling consequences in the retrieved texts; formal HPO mapping is suggested rather than asserted as directly coded in the sources.) (coman2025updatesonthe pages 1-2, shafeghat2025stateofthe pages 2-4)

---

## 4. Genetic / molecular information
### 4.1 Causal/susceptibility genes
DTI-PAH is primarily environmental, but **genetic susceptibility** is important:
- **BMPR2** is highlighted as a major PAH susceptibility gene in PAH broadly and in gene–environment contexts. (seferian2013drugsinducedpulmonary pages 2-3, shafeghat2025stateofthe pages 2-4)
- Additional PAH genes in the BMP/TGF-β axis reported in PAH pathophysiology reviews include **ENG, ACVRL1, CAV1, SMAD9, GDF2**. (correale2025pathophysiologyofpulmonary pages 2-4)

### 4.2 Pathogenic variants
- Specific variant nomenclatures, ACMG classes, and population allele frequencies were not available in the retrieved excerpts.

### 4.3 Modifier/biologic susceptibility signals
- Methamphetamine-associated PAH may involve susceptibility biology (only a subset of exposed individuals develop PAH). (iii2020drugandtoxininduced pages 19-21, iii2020drugandtoxininduced pages 7-10)

---

## 5. Environmental information
### 5.1 Environmental/iatrogenic exposures
See the summary table artifact below for definite vs possible drug/toxin exposures. (dardi2024riskstratificationand pages 22-24)

### 5.2 Lifestyle factors
- Illicit stimulant exposure (methamphetamine; cocaine) is a key modifiable environmental driver in this category. (dardi2024riskstratificationand pages 22-24, iwata2024trendsandpatterns pages 1-2)

---

## 6. Mechanism / pathophysiology
DTI-PAH is mechanistically heterogeneous; several convergent pathways are repeatedly implicated.

### 6.1 Serotonin signaling and appetite suppressants (anorexigens)
Fenfluramine-class drugs are potent **5-HT uptake inhibitors**; increased serotonin can act as a **growth factor for pulmonary artery smooth muscle cells**, promoting vascular remodeling. (seferian2013drugsinducedpulmonary pages 2-3)

### 6.2 Gene–environment (“two-hit”) susceptibility
Drug/toxin exposure plus host predisposition is a recurring mechanistic frame; only a subset of exposed individuals develop PAH. (iii2020drugandtoxininduced pages 19-21)

### 6.3 Endothelial dysfunction and plexiform arteriopathy
PAH pathology is described as **endothelial-centered**, with plexiform lesions and distal arteriolar remodeling. (shafeghat2025stateofthe pages 2-4)

### 6.4 RhoA/ROCK pathway convergence
ROCK pathway activity is increased in PAH and serotonin-related vasoconstriction/proliferation can converge on ROCK signaling; ROCK inhibition can acutely reduce pulmonary hemodynamic load in studies, motivating therapeutic exploration. (shah2023newdrugsand pages 11-13)

### 6.5 PVOD/PCH-like phenotypes with some drugs
Guidelines caution that DTI-PAH can present with **features of PVOD/PCH**, especially after alkylating agents (e.g., mitomycin C, cyclophosphamide), affecting diagnosis and therapy safety. (dardi2024riskstratificationand pages 66-68)

**Suggested GO biological process terms (examples)**
- Pulmonary artery smooth muscle cell proliferation
- Endothelial cell apoptosis
- Vascular remodeling
- Hypoxic pulmonary vasoconstriction

**Suggested CL cell types (examples)**
- Pulmonary artery endothelial cell
- Pulmonary artery smooth muscle cell
- Macrophage

(These ontology suggestions reflect mechanisms discussed in the retrieved reviews rather than explicit ontology annotations in the cited papers.) (shafeghat2025stateofthe pages 2-4, shah2023newdrugsand pages 11-13)

---

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
- Primary site: **pulmonary arteriolar microvasculature** (distal pulmonary arteries/arterioles), with progressive increase in PVR. (shafeghat2025stateofthe pages 2-4)
- Secondary: **right ventricle** (afterload-induced hypertrophy → dysfunction → right heart failure). (shafeghat2025stateofthe pages 2-4)

**Suggested UBERON terms (examples)**
- Pulmonary artery
- Pulmonary arteriole
- Right ventricle

---

## 8. Temporal development
- Course is typically progressive; some drug-associated cases can show partial/full reversibility after exposure cessation (notably interferons and dasatinib), while stimulant-associated disease is reported to remit rarely. (dardi2024riskstratificationand pages 66-68, chin2024treatmentalgorithmfor pages 11-12)

---

## 9. Inheritance and population
### 9.1 Epidemiology (general PAH context)
Guideline-level estimates for PAH overall (not limited to DTI-PAH) include:
- PAH incidence ≈ **6 per million adults** and prevalence ≈ **48–55 per million** in developed-country registries. (dardi2024riskstratificationand pages 22-24)

### 9.2 Methamphetamine-associated PAH: recent statistics (2024)
A U.S. National Inpatient Sample analysis (2008–2020) reported:
- **9.2-fold increase** in PAH hospitalizations with concurrent methamphetamine use. (iwata2024trendsandpatterns pages 1-2)
- Adjusted prevalence ratio for PAH hospitalization among methamphetamine users vs non-users: **PR 32.19 (95% CI 31.19–33.22)**. (iwata2024trendsandpatterns pages 1-2, iwata2024trendsandpatterns pages 6-7)
- Methamphetamine-associated PAH hospitalizations: **59.16% male**; age distribution concentrated in **41–64 years (45.77%)** and **26–40 years (37.52%)**. (iwata2024trendsandpatterns pages 3-4)

Direct abstract quotes (Frontiers in Cardiovascular Medicine, 2024-10):
- “**A significant increase was evident in patients with pulmonary arterial hypertension (PAH) and concurrent methamphetamine use (9.2-fold).**” (iwata2024trendsandpatterns pages 1-2)
- “**An overall adjusted prevalence ratio (PR) for PAH hospitalizations among concurrent methamphetamine users was 32.19 (CI = 31.19–33.22) compared to non-users.**” (iwata2024trendsandpatterns pages 1-2)

---

## 10. Diagnostics
### 10.1 Diagnostic criteria
- **Gold standard**: right heart catheterization with measurements including SvO2/SaO2, CO, and calculation of PVR; pressures measured at end-expiration. (dardi2024riskstratificationand pages 31-32)
- Hemodynamic definition updates: mPAP threshold lowered to **>20 mmHg** and abnormal PVR threshold lowered (e.g., from >3 WU to >2 WU in ESC/ERS-aligned definitions). (chin2024treatmentalgorithmfor pages 5-7)

### 10.2 Workup and differential diagnosis (practice implementation)
Guideline workup includes ECG, chest radiograph, PFTs/DLCO and ABG, labs (including BNP/NT-proBNP), and multimodality imaging; evaluation aims to exclude other PH groups and comorbidities. (dardi2024riskstratificationand pages 24-25, dardi2024riskstratificationand pages 31-32)

### 10.3 Drug/toxin attribution
- Diagnosis of DPAH generally requires: compatible exposure history + exclusion of alternative causes of PH; careful medication and illicit drug history is emphasized. (dardi2024riskstratificationand pages 66-68, iii2020drugandtoxininduced pages 1-3)

### 10.4 Vasoreactivity testing (important for DT-PAH)
- Vasoreactivity testing is recommended at **index RHC** for **IPAH, HPAH, and DT-PAH** to identify potential calcium-channel blocker responders. Acute response: **≥10 mmHg fall in mPAP to an absolute mPAP <40 mmHg without fall in CO**. (chin2024treatmentalgorithmfor pages 5-7)

---

## 11. Outcome / prognosis
- Methamphetamine-associated PAH is described as having **worse hemodynamics and higher mortality** than idiopathic PAH in some centers. (dardi2024riskstratificationand pages 66-68)
- A prospective cohort summarized in a DTI-PAH review reported substantially poorer survival in Meth-APAH vs IPAH (5-/10-year survival 47.2%/25% vs 64.5%/45.7%). (iii2020drugandtoxininduced pages 5-7)

---

## 12. Treatment
### 12.1 Core principles specific to DTI-PAH (expert guidance)
- **Discontinue the causative agent whenever possible.** (dardi2024riskstratificationand pages 68-69, dardi2024riskstratificationand pages 66-68)
- **Low-risk/mild disease:** observation for **3–4 months** after withdrawal may be considered (especially for interferon- or dasatinib-associated PAH), then initiate PAH therapy if hemodynamics do not normalize. (dardi2024riskstratificationand pages 66-68, chin2024treatmentalgorithmfor pages 11-12)
- **Intermediate/high-risk or advanced disease:** initiate PAH therapy promptly. (dardi2024riskstratificationand pages 68-69)
- **Stimulant-associated PAH:** rarely remits; start PAH therapy and refer for substance-use treatment. (chin2024treatmentalgorithmfor pages 11-12)

### 12.2 Risk-stratified PAH therapy (2024 algorithm; real-world implementation)
The 7th WSPH/ERJ 2024 algorithm emphasizes initial risk assessment and combination therapy escalation. (chin2024treatmentalgorithmfor pages 2-3, chin2024treatmentalgorithmfor media 169fd8c9)
- Non–high-risk: initial combination **ERA + PDE-5i**. (chin2024treatmentalgorithmfor pages 5-7)
- High-risk: **parenteral prostacyclin pathway agent + ERA + PDE-5i** (initial triple therapy) and early transplant evaluation. (chin2024treatmentalgorithmfor pages 5-7, chin2024treatmentalgorithmfor pages 7-8)
- Escalation can yield **maximal four-drug therapy**, adding an **activin-signalling inhibitor** (e.g., sotatercept) to ERA + PDE-5i/sGCS + parenteral prostacyclin. (chin2024treatmentalgorithmfor pages 2-3)

Recent development (2024): add-on **sotatercept** improved outcomes in advanced PAH trials and is incorporated into escalation options in the ERJ 2024 treatment algorithm. (chin2024treatmentalgorithmfor pages 7-8, chin2024treatmentalgorithmfor pages 2-3)

### 12.3 MAXO term suggestions (examples)
- Drug withdrawal / cessation of exposure (MAXO term exists)
- Right heart catheterization (diagnostic procedure)
- Combination pharmacotherapy (endothelin receptor antagonism; PDE5 inhibition; prostacyclin analog therapy; activin signaling inhibition)
- Lung transplantation

---

## 13. Prevention
Primary prevention is largely **exposure prevention** and pharmacovigilance:
- Public-health and clinical emphasis on avoiding/ceasing implicated drugs/toxins (especially illicit stimulants) and maintaining high suspicion for DTI-PAH in unexplained exertional dyspnea. (dardi2024riskstratificationand pages 66-68, iii2020drugandtoxininduced pages 19-21)

---

## 14. Other species / natural disease
- No naturally occurring non-human DTI-PAH syndromes were identified in the retrieved excerpts.

---

## 15. Model organisms / experimental models
DTI-PAH and PAH mechanisms are studied using several rodent and in vitro systems:
- **Monocrotaline (MCT) rodent models** (rats) and **hypoxia models** are commonly used experimental PH/PAH models. (shah2023newdrugsand pages 16-17, shah2023newdrugsand pages 11-13)
- **SU5416 + hypoxia (Sugen/hypoxia) rat models** are used to study severe pulmonary vascular remodeling and RV failure; SU5416 causes pulmonary endothelial apoptosis and is used in combination insult models. (shah2023newdrugsand pages 18-19, yeh2025molecularpathogenesisof pages 18-19)
- In vitro serotonin-pathway relevant models include: anorexigens inhibiting potassium currents in pulmonary vascular smooth muscle preparations and MDMA producing 5HT2B-mediated mitogenic effects in human cell systems (mechanistic analogy to anorexigens). (iii2020drugandtoxininduced pages 19-21)

Limitations: pharmacovigilance analyses emphasize that extrapolating animal results to human drug-induced PAH is challenging. (hlavaty2022identifyingnewdrugs pages 7-8)

---

## Summary artifact: drugs/toxins and evidence grading
| Agent/exposure | Evidence category | Typical context/use | Key mechanistic hypotheses | Notes on reversibility/management | Key citations and year |
|---|---|---|---|---|---|
| Aminorex | Definite | Historical anorexigen/appetite suppressant | Serotonergic pathway; appetite suppressants can inhibit K+ currents and promote pulmonary vasoconstriction/remodeling | Withdraw exposure; historical outbreak established causality; manage as PAH if persistent (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 1-3, seferian2013drugsinducedpulmonary pages 2-3) | Seferian 2013, DOI:10.1016/j.lpm.2013.07.005; Ramirez 2020, DOI:10.21542/gcsp.2019.19; Dardi 2024, DOI:10.1183/13993003.01323-2024 |
| Fenfluramine / Dexfenfluramine | Definite | Anorexigen/appetite suppressants | 5-HT uptake inhibition; 5-HT/5-HT2B-driven PASMC proliferation; gene–environment interaction with BMPR2 susceptibility | Withdraw exposure; clinically resembles idiopathic/heritable PAH; persistent disease may require standard PAH therapy (seferian2013drugsinducedpulmonary pages 1-2, dardi2024riskstratificationand pages 22-24, seferian2013drugsinducedpulmonary pages 2-3) | Seferian 2013, DOI:10.1016/j.lpm.2013.07.005; Dardi 2024, DOI:10.1183/13993003.01323-2024 |
| Benfluorex | Definite | Antidiabetic/anorexigen exposure, especially historical French use | Norfenfluramine-related serotonergic toxicity; pulmonary vascular and valvular toxicity | Stop agent; monitor for PAH and valvular disease; treat residual PAH per guidelines (seferian2013drugsinducedpulmonary pages 1-2, dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 1-3) | Seferian 2013, DOI:10.1016/j.lpm.2013.07.005; Ramirez 2020, DOI:10.21542/gcsp.2019.19; Dardi 2024, DOI:10.1183/13993003.01323-2024 |
| Methamphetamines | Definite | Recreational stimulant use | Endothelial injury/dysfunction; serotonin-related signaling; likely susceptibility-dependent “two-hit” biology | Usually does not remit reliably; stop exposure, start PAH therapy when indicated, and refer for substance-use treatment; associated with worse hemodynamics/outcomes (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 5-7, chin2024treatmentalgorithmfor pages 11-12, iwata2024trendsandpatterns pages 1-2) | Ramirez 2020, DOI:10.21542/gcsp.2019.19; Dardi 2024, DOI:10.1183/13993003.01323-2024; Iwata 2024, DOI:10.3389/fcvm.2024.1445193; Chin 2024, DOI:10.1183/13993003.01325-2024 |
| Dasatinib | Definite | BCR-ABL tyrosine kinase inhibitor for CML/ALL | Endothelial dysfunction and kinase off-target vascular toxicity | Stop agent; partial/full reversal reported in some patients; observe 3–4 months if low risk, otherwise initiate PAH therapy (dardi2024riskstratificationand pages 22-24, dardi2024riskstratificationand pages 66-68, chin2024treatmentalgorithmfor pages 11-12, shah2023newdrugsand pages 11-13) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Chin 2024, DOI:10.1183/13993003.01325-2024; Shah 2023, DOI:10.3390/ijms24065850 |
| Toxic rapeseed oil | Definite | Toxic oil exposure outbreak | Toxin-mediated pulmonary vascular injury; some cases may overlap with venous/capillary involvement | Exposure cessation/supportive care; historical outbreak supports causality (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 1-3) | Ramirez 2020, DOI:10.21542/gcsp.2019.19; Dardi 2024, DOI:10.1183/13993003.01323-2024 |
| Amphetamines (non-methamphetamine) | Possible | Prescription/illicit stimulants | Mechanistic similarity to methamphetamine and anorexigens; monoamine/serotonin effects | Stop exposure; causality weaker than methamphetamine; evaluate/treat persistent PAH conventionally (dardi2024riskstratificationand pages 22-24, seferian2013drugsinducedpulmonary pages 1-2) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Seferian 2013, DOI:10.1016/j.lpm.2013.07.005 |
| Interferon-α / Interferon-β | Possible | Antiviral/immunomodulatory therapy | Endothelial dysfunction and immune-mediated vascular injury | Stop agent when feasible; partial/full reversal has been reported; if no normalization after 3–4 months, initiate PAH therapy (dardi2024riskstratificationand pages 22-24, dardi2024riskstratificationand pages 66-68, chin2024treatmentalgorithmfor pages 11-12, iii2020drugandtoxininduced pages 15-17) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Chin 2024, DOI:10.1183/13993003.01325-2024; Ramirez 2020, DOI:10.21542/gcsp.2019.19 |
| Bosutinib / Ponatinib | Possible | Later-generation BCR-ABL tyrosine kinase inhibitors | Endothelial/vascular toxicity analogous to dasatinib | Consider drug withdrawal and specialist reassessment; manage persistent disease as PAH (dardi2024riskstratificationand pages 22-24, hlavaty2022identifyingnewdrugs pages 1-2) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Hlavaty 2022, DOI:10.1111/bcp.15436 |
| Alkylating agents (cyclophosphamide, mitomycin C) | Possible | Chemotherapy | Pulmonary veno-occlusive disease (PVOD)/capillary injury rather than classic isolated arterial disease | Stop culprit when possible; high caution because PVOD phenotype may worsen with vasodilators; specialist evaluation required (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 15-17, dardi2024riskstratificationand pages 66-68) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Ramirez 2020, DOI:10.21542/gcsp.2019.19 |
| Leflunomide | Possible | DMARD for rheumatologic disease | Unclear; pharmacovigilance signal with plausible vascular toxicity | Case-based reversibility reported after withdrawal; confirm alternative causes and monitor hemodynamics (dardi2024riskstratificationand pages 22-24, hlavaty2022identifyingnewdrugs pages 1-2, iii2020drugandtoxininduced pages 17-19) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Hlavaty 2022, DOI:10.1111/bcp.15436; Ramirez 2020, DOI:10.21542/gcsp.2019.19 |
| Direct-acting antivirals for HCV (e.g., sofosbuvir) | Possible | Antiviral therapy for hepatitis C | Mechanism unclear; limited case reports, often confounded | Consider withdrawal if suspected; causality remains uncertain (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 15-17, iii2020drugandtoxininduced pages 17-19) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Ramirez 2020, DOI:10.21542/gcsp.2019.19 |
| Cocaine | Possible | Recreational stimulant; sometimes levamisole-adulterated | Vasoconstriction/endothelial injury; adulterant levamisole may be metabolized to aminorex | Stop exposure; assess for mixed stimulant/toxin exposure; evidence remains weaker than for methamphetamine (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 17-19, mcgee2018drugassociatedpulmonaryarterial pages 7-8) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Ramirez 2020, DOI:10.21542/gcsp.2019.19; McGee 2018, DOI:10.1080/15563650.2018.1447119 |
| L-tryptophan / St John’s Wort / Qing-Dai (indirubin) | Possible | Supplements/herbal exposures | Contaminant-related injury (L-tryptophan); serotonergic or other vasoactive signaling; unclear for some herbal products | Stop exposure; several reports show hemodynamic improvement after discontinuation for some agents (dardi2024riskstratificationand pages 22-24, iii2020drugandtoxininduced pages 15-17, iii2020drugandtoxininduced pages 17-19) | Dardi 2024, DOI:10.1183/13993003.01323-2024; Ramirez 2020, DOI:10.21542/gcsp.2019.19 |


*Table: This table summarizes the main drugs and toxins linked to pulmonary arterial hypertension, prioritizing the current definite versus possible classifications and the most relevant mechanistic and management implications. It is useful for quickly distinguishing well-established culprits from emerging or lower-certainty signals.*

---

## Visual evidence: PAH treatment algorithm (7th WSPH/ERJ 2024)
The ERJ 2024 PAH treatment algorithm figure provides a practical overview of risk-stratified initial therapy and escalation strategy used in real-world PAH programs. (chin2024treatmentalgorithmfor media 169fd8c9)

---

## Key source list (URLs and dates)
- Dardi et al. *Eur Respir J* (2024-08). “Risk stratification and treatment goals in PAH.” https://doi.org/10.1183/13993003.01323-2024 (dardi2024riskstratificationand pages 66-68, dardi2024riskstratificationand pages 22-24)
- Chin et al. *Eur Respir J* (2024-08). “Treatment algorithm for PAH.” https://doi.org/10.1183/13993003.01325-2024 (chin2024treatmentalgorithmfor pages 5-7, chin2024treatmentalgorithmfor media 169fd8c9)
- Iwata et al. *Front Cardiovasc Med* (2024-10). Methamphetamine-associated PAH hospitalizations (NIS 2008–2020). https://doi.org/10.3389/fcvm.2024.1445193 (iwata2024trendsandpatterns pages 1-2)
- Shah et al. *Int J Mol Sci* (2023-03). “New drugs and therapies in PAH.” https://doi.org/10.3390/ijms24065850 (shah2023newdrugsand pages 11-13, shah2023newdrugsand pages 18-19)
- Ramirez et al. *Glob Cardiol Sci Pract* (2020-02). “Drug- and toxin-induced PAH.” https://doi.org/10.21542/gcsp.2019.19 (iii2020drugandtoxininduced pages 1-3, iii2020drugandtoxininduced pages 5-7)

---

## Notable gaps (for knowledge-base completion)
- Formal cross-ontology identifiers (MONDO, MeSH, Orphanet, ICD-10/ICD-11) were not present in the retrieved excerpts and therefore cannot be reliably populated here.
- Variant-level genetics, penetrance, and population allele frequencies for susceptibility genes are not available in the current evidence set.


References

1. (dardi2024riskstratificationand pages 22-24): Fabio Dardi, Athénaïs Boucly, Raymond Benza, Robert Frantz, Valentina Mercurio, Horst Olschewski, Göran Rådegran, Lewis J. Rubin, and Marius M. Hoeper. Risk stratification and treatment goals in pulmonary arterial hypertension. The European Respiratory Journal, 64:2401323, Aug 2024. URL: https://doi.org/10.1183/13993003.01323-2024, doi:10.1183/13993003.01323-2024. This article has 112 citations.

2. (dardi2024riskstratificationand pages 66-68): Fabio Dardi, Athénaïs Boucly, Raymond Benza, Robert Frantz, Valentina Mercurio, Horst Olschewski, Göran Rådegran, Lewis J. Rubin, and Marius M. Hoeper. Risk stratification and treatment goals in pulmonary arterial hypertension. The European Respiratory Journal, 64:2401323, Aug 2024. URL: https://doi.org/10.1183/13993003.01323-2024, doi:10.1183/13993003.01323-2024. This article has 112 citations.

3. (chin2024treatmentalgorithmfor pages 11-12): Kelly M. Chin, Sean P. Gaine, Christian Gerges, Zhi-Cheng Jing, Stephen C. Mathai, Yuichi Tamura, Vallerie V. McLaughlin, and Olivier Sitbon. Treatment algorithm for pulmonary arterial hypertension. The European Respiratory Journal, 64:2401325, Aug 2024. URL: https://doi.org/10.1183/13993003.01325-2024, doi:10.1183/13993003.01325-2024. This article has 228 citations.

4. (iwata2024trendsandpatterns pages 1-2): Hiroshi Iwata, Y. Chikata, Mohammad Alfrad, Nobel Bhuiyan, Amanda Husein, Jolie A Boullion, Md. Ismail Hossain, Diensn Xing, Md Tareq Ferdous Khan, M. Bhuiyan, Gopi K. Kolluru, Md Mosta ﬁ zur Rahman Bhuiyan, Nicholas E. Goeders, Steven A. Conrad, J. Vanchiere, A. W. Orr, C. Kevil, and Mohammad Alfrad Nobel. Trends and patterns in pulmonary arterial hypertension-associated hospital admissions among methamphetamine users: a decade-long study. Frontiers in Cardiovascular Medicine, Oct 2024. URL: https://doi.org/10.3389/fcvm.2024.1445193, doi:10.3389/fcvm.2024.1445193. This article has 5 citations and is from a peer-reviewed journal.

5. (chin2024treatmentalgorithmfor pages 7-8): Kelly M. Chin, Sean P. Gaine, Christian Gerges, Zhi-Cheng Jing, Stephen C. Mathai, Yuichi Tamura, Vallerie V. McLaughlin, and Olivier Sitbon. Treatment algorithm for pulmonary arterial hypertension. The European Respiratory Journal, 64:2401325, Aug 2024. URL: https://doi.org/10.1183/13993003.01325-2024, doi:10.1183/13993003.01325-2024. This article has 228 citations.

6. (chin2024treatmentalgorithmfor pages 2-3): Kelly M. Chin, Sean P. Gaine, Christian Gerges, Zhi-Cheng Jing, Stephen C. Mathai, Yuichi Tamura, Vallerie V. McLaughlin, and Olivier Sitbon. Treatment algorithm for pulmonary arterial hypertension. The European Respiratory Journal, 64:2401325, Aug 2024. URL: https://doi.org/10.1183/13993003.01325-2024, doi:10.1183/13993003.01325-2024. This article has 228 citations.

7. (iii2020drugandtoxininduced pages 1-3): Ramon L Ramirez III, Christopher A Thomas, Ryan J Anderson, Roberto J Bernardo, Ahmed Al-Motarreb, Jassim Al-Suwaidi, Roham T Zamanian, and Vinicio A De Jesus Perez. Drug- and toxin-induced pulmonary arterial hypertension: current state of the literature. Global Cardiology Science and Practice, Feb 2020. URL: https://doi.org/10.21542/gcsp.2019.19, doi:10.21542/gcsp.2019.19. This article has 3 citations.

8. (shafeghat2025stateofthe pages 2-4): Melika Shafeghat, Yasmin Raza, Roberta Catania, Amir Ali Rahsepar, Blair Tilkens, Michael J. Cuttica, Benjamin H. Freed, Jingbo Dai, You-Yang Zhao, and James C. Carr. State of the art in pulmonary arterial hypertension: molecular basis, imaging modalities, and right heart failure treatment. Biomedicines, 13:1773, Jul 2025. URL: https://doi.org/10.3390/biomedicines13071773, doi:10.3390/biomedicines13071773. This article has 5 citations.

9. (chin2024treatmentalgorithmfor pages 5-7): Kelly M. Chin, Sean P. Gaine, Christian Gerges, Zhi-Cheng Jing, Stephen C. Mathai, Yuichi Tamura, Vallerie V. McLaughlin, and Olivier Sitbon. Treatment algorithm for pulmonary arterial hypertension. The European Respiratory Journal, 64:2401325, Aug 2024. URL: https://doi.org/10.1183/13993003.01325-2024, doi:10.1183/13993003.01325-2024. This article has 228 citations.

10. (dardi2024riskstratificationand pages 21-22): Fabio Dardi, Athénaïs Boucly, Raymond Benza, Robert Frantz, Valentina Mercurio, Horst Olschewski, Göran Rådegran, Lewis J. Rubin, and Marius M. Hoeper. Risk stratification and treatment goals in pulmonary arterial hypertension. The European Respiratory Journal, 64:2401323, Aug 2024. URL: https://doi.org/10.1183/13993003.01323-2024, doi:10.1183/13993003.01323-2024. This article has 112 citations.

11. (chin2024treatmentalgorithmfor pages 1-2): Kelly M. Chin, Sean P. Gaine, Christian Gerges, Zhi-Cheng Jing, Stephen C. Mathai, Yuichi Tamura, Vallerie V. McLaughlin, and Olivier Sitbon. Treatment algorithm for pulmonary arterial hypertension. The European Respiratory Journal, 64:2401325, Aug 2024. URL: https://doi.org/10.1183/13993003.01325-2024, doi:10.1183/13993003.01325-2024. This article has 228 citations.

12. (iii2020drugandtoxininduced pages 19-21): Ramon L Ramirez III, Christopher A Thomas, Ryan J Anderson, Roberto J Bernardo, Ahmed Al-Motarreb, Jassim Al-Suwaidi, Roham T Zamanian, and Vinicio A De Jesus Perez. Drug- and toxin-induced pulmonary arterial hypertension: current state of the literature. Global Cardiology Science and Practice, Feb 2020. URL: https://doi.org/10.21542/gcsp.2019.19, doi:10.21542/gcsp.2019.19. This article has 3 citations.

13. (seferian2013drugsinducedpulmonary pages 2-3): Andrei Seferian, Marie-Camille Chaumais, Laurent Savale, Sven Günther, Pascale Tubert-Bitter, Marc Humbert, and David Montani. Drugs induced pulmonary arterial hypertension. Presse medicale, 42 9 Pt 2:e303-10, Sep 2013. URL: https://doi.org/10.1016/j.lpm.2013.07.005, doi:10.1016/j.lpm.2013.07.005. This article has 54 citations and is from a peer-reviewed journal.

14. (dardi2024riskstratificationand pages 24-25): Fabio Dardi, Athénaïs Boucly, Raymond Benza, Robert Frantz, Valentina Mercurio, Horst Olschewski, Göran Rådegran, Lewis J. Rubin, and Marius M. Hoeper. Risk stratification and treatment goals in pulmonary arterial hypertension. The European Respiratory Journal, 64:2401323, Aug 2024. URL: https://doi.org/10.1183/13993003.01323-2024, doi:10.1183/13993003.01323-2024. This article has 112 citations.

15. (coman2025updatesonthe pages 1-2): Ioan Mircea Coman, Roxana Enache, Georgiana Olaru, Raluca Rancea, Tudor Constantinescu, Andrei Neagu, Miron Al. Bogdan, Ioan Ţilea, Andreea Varga, Nicoleta Bertici, Ovidiu Fira-Mladinescu, Anda Tesloianu, Alexandru Steriade, and Dragos Bumbacea. Updates on the therapeutic approach to pulmonary arterial hypertension. Romanian Journal of Cardiology, 35:225-230, Dec 2025. URL: https://doi.org/10.2478/rjc-2025-0035, doi:10.2478/rjc-2025-0035. This article has 0 citations.

16. (dardi2024riskstratificationand pages 31-32): Fabio Dardi, Athénaïs Boucly, Raymond Benza, Robert Frantz, Valentina Mercurio, Horst Olschewski, Göran Rådegran, Lewis J. Rubin, and Marius M. Hoeper. Risk stratification and treatment goals in pulmonary arterial hypertension. The European Respiratory Journal, 64:2401323, Aug 2024. URL: https://doi.org/10.1183/13993003.01323-2024, doi:10.1183/13993003.01323-2024. This article has 112 citations.

17. (iwata2024trendsandpatterns pages 3-4): Hiroshi Iwata, Y. Chikata, Mohammad Alfrad, Nobel Bhuiyan, Amanda Husein, Jolie A Boullion, Md. Ismail Hossain, Diensn Xing, Md Tareq Ferdous Khan, M. Bhuiyan, Gopi K. Kolluru, Md Mosta ﬁ zur Rahman Bhuiyan, Nicholas E. Goeders, Steven A. Conrad, J. Vanchiere, A. W. Orr, C. Kevil, and Mohammad Alfrad Nobel. Trends and patterns in pulmonary arterial hypertension-associated hospital admissions among methamphetamine users: a decade-long study. Frontiers in Cardiovascular Medicine, Oct 2024. URL: https://doi.org/10.3389/fcvm.2024.1445193, doi:10.3389/fcvm.2024.1445193. This article has 5 citations and is from a peer-reviewed journal.

18. (correale2025pathophysiologyofpulmonary pages 2-4): Michele Correale, Valentina Mercurio, Ester Maria Lucia Bevere, Beatrice Pezzuto, Lucia Tricarico, Umberto Attanasio, Angela Raucci, Anne Lise Ferrara, Stefania Loffredo, Claudio Puteo, Massimo Iacoviello, Maurizio Margaglione, Natale Daniele Brunetti, Carlo Gabriele Tocchetti, Piergiuseppe Agostoni, Claudio Mussolino, and Maria Cristina Vinci. Pathophysiology of pulmonary arterial hypertension: focus on vascular endothelium as a potential therapeutic target. International Journal of Molecular Sciences, 26:9631, Oct 2025. URL: https://doi.org/10.3390/ijms26199631, doi:10.3390/ijms26199631. This article has 8 citations.

19. (iii2020drugandtoxininduced pages 7-10): Ramon L Ramirez III, Christopher A Thomas, Ryan J Anderson, Roberto J Bernardo, Ahmed Al-Motarreb, Jassim Al-Suwaidi, Roham T Zamanian, and Vinicio A De Jesus Perez. Drug- and toxin-induced pulmonary arterial hypertension: current state of the literature. Global Cardiology Science and Practice, Feb 2020. URL: https://doi.org/10.21542/gcsp.2019.19, doi:10.21542/gcsp.2019.19. This article has 3 citations.

20. (shah2023newdrugsand pages 11-13): Aangi J. Shah, Taylor Beckmann, Mounica Vorla, and Dinesh K. Kalra. New drugs and therapies in pulmonary arterial hypertension. International Journal of Molecular Sciences, 24:5850, Mar 2023. URL: https://doi.org/10.3390/ijms24065850, doi:10.3390/ijms24065850. This article has 71 citations.

21. (iwata2024trendsandpatterns pages 6-7): Hiroshi Iwata, Y. Chikata, Mohammad Alfrad, Nobel Bhuiyan, Amanda Husein, Jolie A Boullion, Md. Ismail Hossain, Diensn Xing, Md Tareq Ferdous Khan, M. Bhuiyan, Gopi K. Kolluru, Md Mosta ﬁ zur Rahman Bhuiyan, Nicholas E. Goeders, Steven A. Conrad, J. Vanchiere, A. W. Orr, C. Kevil, and Mohammad Alfrad Nobel. Trends and patterns in pulmonary arterial hypertension-associated hospital admissions among methamphetamine users: a decade-long study. Frontiers in Cardiovascular Medicine, Oct 2024. URL: https://doi.org/10.3389/fcvm.2024.1445193, doi:10.3389/fcvm.2024.1445193. This article has 5 citations and is from a peer-reviewed journal.

22. (iii2020drugandtoxininduced pages 5-7): Ramon L Ramirez III, Christopher A Thomas, Ryan J Anderson, Roberto J Bernardo, Ahmed Al-Motarreb, Jassim Al-Suwaidi, Roham T Zamanian, and Vinicio A De Jesus Perez. Drug- and toxin-induced pulmonary arterial hypertension: current state of the literature. Global Cardiology Science and Practice, Feb 2020. URL: https://doi.org/10.21542/gcsp.2019.19, doi:10.21542/gcsp.2019.19. This article has 3 citations.

23. (dardi2024riskstratificationand pages 68-69): Fabio Dardi, Athénaïs Boucly, Raymond Benza, Robert Frantz, Valentina Mercurio, Horst Olschewski, Göran Rådegran, Lewis J. Rubin, and Marius M. Hoeper. Risk stratification and treatment goals in pulmonary arterial hypertension. The European Respiratory Journal, 64:2401323, Aug 2024. URL: https://doi.org/10.1183/13993003.01323-2024, doi:10.1183/13993003.01323-2024. This article has 112 citations.

24. (chin2024treatmentalgorithmfor media 169fd8c9): Kelly M. Chin, Sean P. Gaine, Christian Gerges, Zhi-Cheng Jing, Stephen C. Mathai, Yuichi Tamura, Vallerie V. McLaughlin, and Olivier Sitbon. Treatment algorithm for pulmonary arterial hypertension. The European Respiratory Journal, 64:2401325, Aug 2024. URL: https://doi.org/10.1183/13993003.01325-2024, doi:10.1183/13993003.01325-2024. This article has 228 citations.

25. (shah2023newdrugsand pages 16-17): Aangi J. Shah, Taylor Beckmann, Mounica Vorla, and Dinesh K. Kalra. New drugs and therapies in pulmonary arterial hypertension. International Journal of Molecular Sciences, 24:5850, Mar 2023. URL: https://doi.org/10.3390/ijms24065850, doi:10.3390/ijms24065850. This article has 71 citations.

26. (shah2023newdrugsand pages 18-19): Aangi J. Shah, Taylor Beckmann, Mounica Vorla, and Dinesh K. Kalra. New drugs and therapies in pulmonary arterial hypertension. International Journal of Molecular Sciences, 24:5850, Mar 2023. URL: https://doi.org/10.3390/ijms24065850, doi:10.3390/ijms24065850. This article has 71 citations.

27. (yeh2025molecularpathogenesisof pages 18-19): Fu-Chiang Yeh, I-Ting Tsai, and I-Tsu Chyuan. Molecular pathogenesis of connective tissue disease-associated pulmonary arterial hypertension: a narrative review. Biomolecules, 15:772, May 2025. URL: https://doi.org/10.3390/biom15060772, doi:10.3390/biom15060772. This article has 0 citations.

28. (hlavaty2022identifyingnewdrugs pages 7-8): Alex Hlavaty, Matthieu Roustit, David Montani, Marie‐Camille Chaumais, Christophe Guignabert, Marc Humbert, Jean‐Luc Cracowski, and Charles Khouri. Identifying new drugs associated with pulmonary arterial hypertension: a who pharmacovigilance database disproportionality analysis. British Journal of Clinical Pharmacology, 88:5227-5237, Jul 2022. URL: https://doi.org/10.1111/bcp.15436, doi:10.1111/bcp.15436. This article has 28 citations and is from a domain leading peer-reviewed journal.

29. (seferian2013drugsinducedpulmonary pages 1-2): Andrei Seferian, Marie-Camille Chaumais, Laurent Savale, Sven Günther, Pascale Tubert-Bitter, Marc Humbert, and David Montani. Drugs induced pulmonary arterial hypertension. Presse medicale, 42 9 Pt 2:e303-10, Sep 2013. URL: https://doi.org/10.1016/j.lpm.2013.07.005, doi:10.1016/j.lpm.2013.07.005. This article has 54 citations and is from a peer-reviewed journal.

30. (iii2020drugandtoxininduced pages 15-17): Ramon L Ramirez III, Christopher A Thomas, Ryan J Anderson, Roberto J Bernardo, Ahmed Al-Motarreb, Jassim Al-Suwaidi, Roham T Zamanian, and Vinicio A De Jesus Perez. Drug- and toxin-induced pulmonary arterial hypertension: current state of the literature. Global Cardiology Science and Practice, Feb 2020. URL: https://doi.org/10.21542/gcsp.2019.19, doi:10.21542/gcsp.2019.19. This article has 3 citations.

31. (hlavaty2022identifyingnewdrugs pages 1-2): Alex Hlavaty, Matthieu Roustit, David Montani, Marie‐Camille Chaumais, Christophe Guignabert, Marc Humbert, Jean‐Luc Cracowski, and Charles Khouri. Identifying new drugs associated with pulmonary arterial hypertension: a who pharmacovigilance database disproportionality analysis. British Journal of Clinical Pharmacology, 88:5227-5237, Jul 2022. URL: https://doi.org/10.1111/bcp.15436, doi:10.1111/bcp.15436. This article has 28 citations and is from a domain leading peer-reviewed journal.

32. (iii2020drugandtoxininduced pages 17-19): Ramon L Ramirez III, Christopher A Thomas, Ryan J Anderson, Roberto J Bernardo, Ahmed Al-Motarreb, Jassim Al-Suwaidi, Roham T Zamanian, and Vinicio A De Jesus Perez. Drug- and toxin-induced pulmonary arterial hypertension: current state of the literature. Global Cardiology Science and Practice, Feb 2020. URL: https://doi.org/10.21542/gcsp.2019.19, doi:10.21542/gcsp.2019.19. This article has 3 citations.

33. (mcgee2018drugassociatedpulmonaryarterial pages 7-8): Michael McGee, Nicholas Whitehead, Jennifer Martin, and Nicholas Collins. Drug-associated pulmonary arterial hypertension. Clinical Toxicology, 56:801-809, Mar 2018. URL: https://doi.org/10.1080/15563650.2018.1447119, doi:10.1080/15563650.2018.1447119. This article has 98 citations and is from a peer-reviewed journal.
