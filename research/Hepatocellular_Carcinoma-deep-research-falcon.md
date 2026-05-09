---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T19:15:48.592712'
end_time: '2026-05-08T19:35:16.062652'
duration_seconds: 1167.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hepatocellular Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 71
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Hepatocellular Carcinoma** covering all of the
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
- **Disease Name:** Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Hepatocellular Carcinoma** covering all of the
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


# Hepatocellular Carcinoma (HCC) — Disease Characteristics Research Report (2023–2024 prioritized)

## Target disease
- **Disease name:** Hepatocellular carcinoma (HCC)
- **MONDO ID:** Not recovered from the available evidence in this run (see Identifiers table) (OpenTargets Search: hepatocellular carcinoma)
- **Category:** Malignant neoplasm; primary liver cancer (HCC comprises ~75–90% of primary liver cancers depending on source) (hwang2024hepatocellularcarcinomaupdates pages 1-3, kinsey2024managementofhepatocellular pages 1-2)

---

## 1. Disease information

### 1.1 Definition / overview (current understanding)
Hepatocellular carcinoma is the most common primary hepatic malignancy and a leading cause of cancer mortality worldwide (cannella2024esressentialsdiagnosis pages 1-3, hwang2024hepatocellularcarcinomaupdates pages 1-3). HCC typically arises in the setting of chronic liver disease/cirrhosis; cirrhosis confers markedly elevated risk compared with non-cirrhotic liver, and clinical management must simultaneously address the tumor and the underlying liver dysfunction (hwang2024hepatocellularcarcinomaupdates pages 1-3, mattos2024hepatocellularcarcinomatherole pages 1-2).

### 1.2 Key identifiers and synonyms
A compact normalization table is provided below.

| Disease name | Common synonyms / alternative names | Identifier system | Code / ID | Status / note | Source | URL / DOI |
|---|---|---|---|---|---|---|
| Hepatocellular carcinoma | HCC; hepatoma | Open Targets / EFO | EFO_0000182 | Retrieved in current evidence as the disease entity used for target associations | Open Targets disease-target association (OpenTargets Search: hepatocellular carcinoma) | https://platform.opentargets.org/disease/EFO_0000182 |
| Hepatocellular carcinoma | HCC; hepatoma | ICD-10 | C22.0 | Malignant neoplasm of liver and intrahepatic bile ducts, liver cell carcinoma | AASLD/CMH surveillance and diagnosis reviews referencing current HCC guideline nomenclature and disease classification context (hwang2024hepatocellularcarcinomaupdates pages 6-7, hwang2024hepatocellularcarcinomaupdates pages 1-3) | https://icd.who.int/browse10/2019/en#/C22.0 |
| Hepatocellular carcinoma | HCC; hepatoma | MONDO | Not available | MONDO identifier was not retrieved in the current evidence set and should be treated as unavailable here | No MONDO ID recovered in gathered evidence; Open Targets search returned EFO disease mapping instead (OpenTargets Search: hepatocellular carcinoma) | Not available |
| Hepatocellular carcinoma | HCC; hepatoma | MeSH | Not retrieved in current evidence | MeSH identifier not directly retrieved in the available evidence, though HCC is consistently defined as the major primary liver cancer | Recent HCC reviews/guidelines use the disease term consistently but do not provide a MeSH code in the retrieved excerpts (hwang2024hepatocellularcarcinomaupdates pages 1-3, cannella2024esressentialsdiagnosis pages 1-3) | https://www.ncbi.nlm.nih.gov/mesh/ |
| Hepatocellular carcinoma | HCC; hepatoma; liver cell carcinoma | Guideline/common usage | Not a formal code | Common naming supported by recent guideline and review literature; HCC is described as the predominant primary liver cancer | Hwang et al. 2024; ESR/ESGAR 2024; ASCO 2024 (hwang2024hepatocellularcarcinomaupdates pages 1-3, cannella2024esressentialsdiagnosis pages 1-3, gordan2024systemictherapyfor pages 1-2) | https://doi.org/10.3350/cmh.2024.0824 ; https://doi.org/10.1007/s00330-024-10606-w ; https://doi.org/10.1200/JCO.23.02745 |


*Table: This table compiles the key identifiers and common names for hepatocellular carcinoma that were recoverable from the gathered evidence. It is useful as a compact normalization reference for knowledge-base curation, while clearly marking identifiers that were not retrieved in the current evidence set.*

**Synonyms / alternative names:** “HCC”, “hepatoma”, “liver cell carcinoma” (common clinical usage in contemporary guidelines/reviews) (kinsey2024managementofhepatocellular pages 1-2, hwang2024hepatocellularcarcinomaupdates pages 1-3).

### 1.3 Evidence source type
The information synthesized here is largely **aggregated disease-level evidence** from international guidelines/reviews and meta-analyses (e.g., ASCO 2024 systemic therapy guideline update; ESR/ESGAR 2024 imaging recommendations; EASL-EASD-EASO 2024 MASLD guideline; CMH 2024 epidemiology review) plus selected **primary/real-world clinical studies** and **genomic cohort studies** (gordan2024systemictherapyfor pages 1-2, cannella2024esressentialsdiagnosis pages 1-3, (easo)2024easleasdeasoclinicalpractice pages 46-48, hwang2024hepatocellularcarcinomaupdates pages 1-3, shen2024efficacyofatezolizumab pages 1-2, song2024genomicprofilinginforms pages 1-2).

---

## 2. Etiology

### 2.1 Primary causal factors
HCC arises through the interaction of chronic liver injury/inflammation/fibrosis with acquired (somatic) genetic and epigenetic alterations in hepatocytes, commonly driven by: chronic viral hepatitis (HBV/HCV), alcohol-associated liver disease (ALD), and metabolic dysfunction–associated steatotic liver disease (MASLD) / metabolic dysfunction–associated steatohepatitis (MASH) (hwang2024hepatocellularcarcinomaupdates pages 1-3, kinsey2024managementofhepatocellular pages 1-2).

### 2.2 Risk factors (genetic + environmental)
**Major clinical risk factors** consistently highlighted across guidelines include cirrhosis, chronic HBV infection, chronic HCV infection, alcohol use/ALD, obesity, type 2 diabetes, and MASLD/MASH; aflatoxin exposure remains important in some regions (kinsey2024managementofhepatocellular pages 1-2, hwang2024hepatocellularcarcinomaupdates pages 4-6).

**Regional/global etiology proportions (GBD 2021, liver cancer overall):** HBV ~39% of cases (37% of deaths), HCV ~29% (30% deaths), ALD ~19% (19% deaths) (hwang2024hepatocellularcarcinomaupdates pages 4-6).

**Genetic susceptibility / modifiers (selected examples):** A 2024 “state of the art” genetic screening review notes that germline polymorphisms in lipid metabolism genes (e.g., PNPLA3, TM6SF2, HSD17B13) modulate NASH/alcohol-related disease severity and influence HCC risk, and that variants in WNT genes or TERT can modulate HCC risk (peruhova2024geneticscreeningof pages 2-4).

### 2.3 Protective factors
At the population level, the declining fraction of HBV- and HCV-related HCC is attributed to **HBV vaccination** and **effective antiviral therapy** reducing chronic viral hepatitis burden (hwang2024hepatocellularcarcinomaupdates pages 1-3, hwang2024hepatocellularcarcinomaupdates pages 4-6). In MASLD, reduction/regression of fibrosis is linked with reduced liver-related risk, supporting fibrosis reduction as a protective strategy against downstream outcomes including HCC ((easo)2024easleasdeasoclinicalpractice pages 46-48).

### 2.4 Gene–environment interactions
The etiology-specific differences in key somatic events (e.g., TERT promoter mutation rates differing by HBV/HCV/nonviral) highlight gene–environment interplay (virus-driven vs metabolic drivers with different mutational selection pressures) (ucdal2024crosstalkbetween pages 1-2).

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes
HCC is frequently asymptomatic until advanced stages; consequently, surveillance aims to detect tumors at a curable stage (wu2024hepatocellularcarcinomasurveillance pages 1-2). Underlying cirrhosis drives common co-phenotypes/complications that influence treatment eligibility (portal hypertension/varices, synthetic dysfunction, etc.), motivating staging systems that integrate liver function and performance status (seth2024clinicalpracticeguidelines pages 2-3, gordan2024systemictherapyfor pages 1-2).

### 3.2 Ontology suggestions (HPO; non-exhaustive)
Because detailed symptom-frequency tables were not available in the retrieved evidence excerpts, below are *suggested* HPO terms for common HCC/cirrhosis-associated clinical features seen in practice (term suggestions only; frequencies not extracted here):
- **HP:0001402** Hepatomegaly
- **HP:0001394** Jaundice
- **HP:0001548** Ascites
- **HP:0002615** Esophageal varices
- **HP:0003073** Elevated serum alpha-fetoprotein
- **HP:0002240** Abdominal pain

### 3.3 Quality of life impact
A multidisciplinary, patient-centered model and early palliative-care integration are increasingly emphasized in 2024-era HCC management reviews because liver dysfunction plus cancer symptoms/toxicities can substantially impair daily functioning (kinsey2024managementofhepatocellular pages 1-2).

---

## 4. Genetic / molecular information

### 4.1 Somatic driver landscape (key concepts)
HCC is dominated by **somatic** alterations rather than single-gene Mendelian causation. Commonly altered genes repeatedly highlighted include **TERT promoter**, **TP53**, and **Wnt/β-catenin pathway genes** (e.g., **CTNNB1**, **AXIN1**) along with chromatin regulators (ARID1A/ARID2), and signaling pathway members spanning PI3K/AKT/mTOR, RAS/MAPK, Hippo, Notch, etc. (ucdal2024crosstalkbetween pages 1-2, szilveszter2024molecularmechanismsin pages 2-4, peruhova2024geneticscreeningof pages 2-4).

**Quantitative frequency ranges (from a 2024 clinical-genomics cohort summary):** TERT promoter ~60%; TP53 ~12–48%; CTNNB1 ~11–37% (song2024genomicprofilinginforms pages 1-2). Another 2024 mechanistic review describes TERT promoter as “the single most common HCC mutation (up to 60%)” and provides etiology-stratified frequencies: HCV ~44%, non-viral ~38%, HBV ~23% (ucdal2024crosstalkbetween pages 1-2).

### 4.2 Pathways and mechanistic chain (example)
A common causal chain described in contemporary reviews is:
1) chronic injury (HBV/HCV, alcohol, MASLD/MASH) → 2) inflammation/fibrosis/cirrhosis microenvironment → 3) selection for telomerase activation (TERT promoter) and oncogenic signaling alterations (Wnt/β-catenin, PI3K/AKT/mTOR, RAS/MAPK, Hippo, Notch) → 4) tumor initiation/progression with immunosuppressive tumor microenvironment and angiogenesis → 5) clinical HCC with recurrence/metastasis risk (hwang2024hepatocellularcarcinomaupdates pages 1-3, szilveszter2024molecularmechanismsin pages 2-4, pessino2024hepatocellularcarcinomaold pages 15-17).

### 4.3 Clinically relevant associations and biomarkers
- **Immune microenvironment associations with genotype:** TP53 mutations have been associated with increased immune infiltration, while CTNNB1 and KMT2D mutations correlate with decreased immune infiltration (implicating Wnt-driven “immune-cold” phenotypes relevant to immunotherapy) (song2024genomicprofilinginforms pages 1-2).
- **Prognostic genomic alterations (example cohort):** LATS1 alterations associated with markedly shorter recurrence-free survival (RFS 5.57 vs 22.47 months) in a 2024 targeted-sequencing cohort (wang2024novelgeneticalterations pages 1-2).

### 4.4 Epigenetics
While detailed locus-level methylation/histone data were not extracted from a single primary epigenome paper in this run, 2024 reviews emphasize that harmful epigenetic modifications (DNA methylation/chromatin changes) interact with driver mutations and contribute to intratumoral heterogeneity and progression; these are also being explored therapeutically in combination regimens (szilveszter2024molecularmechanismsin pages 2-4).

### 4.5 Ontology suggestions
- **GO biological process (examples):** Wnt signaling (GO:0016055), angiogenesis (GO:0001525), epithelial–mesenchymal transition (GO:0001837), inflammatory response (GO:0006954), T cell activation (GO:0042110).

---

## 5. Environmental information

### 5.1 Environmental and lifestyle contributors
- **Alcohol:** ALD is a major and rising contributor to HCC incidence (hwang2024hepatocellularcarcinomaupdates pages 1-3, hwang2024hepatocellularcarcinomaupdates pages 4-6). The MASLD guideline discourages alcohol consumption in all individuals with steatotic liver disease, noting that alcohol worsens liver outcomes and increases HCC risk versus abstinence ((easo)2024easleasdeasoclinicalpractice pages 10-11).
- **Diet/obesity/physical activity:** MASLD guideline highlights associations between unhealthy dietary patterns (e.g., sugar-sweetened beverages, red/processed meat) and higher risk of MASLD and liver cancer, while healthy lifestyle and physical activity reduce risk of MASLD, HCC, and liver-related mortality ((easo)2024easleasdeasoclinicalpractice pages 10-11).
- **Aflatoxin:** geographic concentrations include Sub-Saharan Africa, Southeast Asia, and China (hwang2024hepatocellularcarcinomaupdates pages 4-6).

### 5.2 Infectious agents
HBV and HCV are key infectious causes (hwang2024hepatocellularcarcinomaupdates pages 4-6). Chronic HBV/HCV contributions to liver cancer incidence and death are quantified above (hwang2024hepatocellularcarcinomaupdates pages 4-6).

---

## 6. Mechanism / pathophysiology

### 6.1 Molecular pathways (selected high-confidence)
Pathways repeatedly emphasized in 2024-era mechanistic and clinical-genomics literature include:
- **Wnt/β-catenin** (CTNNB1, AXIN1) (ucdal2024crosstalkbetween pages 1-2, szilveszter2024molecularmechanismsin pages 2-4)
- **PI3K/AKT/mTOR** (common pathway alteration; mutational contributors include PTEN, PIK3CA, MTOR, AKT2) (pessino2024hepatocellularcarcinomaold pages 15-17)
- **RAS/RAF/MAPK** (frequently altered signaling; also prominent in DEN mouse model mutational spectrum) (szilveszter2024molecularmechanismsin pages 2-4, cigliano2024preclinicalmodelsof pages 9-10)
- **Hippo, Notch, Hedgehog** (enriched in WES pathway analyses and reviews) (kassem2024genomiclandscapeof pages 1-2, szilveszter2024molecularmechanismsin pages 2-4)

### 6.2 Immune system involvement (2024 single-cell/spatial advances)
Single-cell and spatial transcriptomics studies in 2024 provide mechanistic insight into **why only a subset of patients respond to PD-1/PD-L1 blockade**:
- An “**immune barrier**” composed of macrophages and cancer-associated fibroblasts (CAFs) can physically/chemically impede CD8+ T-cell infiltration; non-responders show increased immunosuppressive macrophage states (e.g., TREM2+ macrophages, SPP1+ macrophages) and CAF markers (e.g., POSTN) (li2024singlecellanalyses pages 1-2, li2024singlecellanalyses pages 6-8).
- A large integrated single-cell+spatial analysis mapped malignant-cell heterogeneity and identified a pro-metastatic EMT-like tumor-cell subtype with **TGF-β/SMAD3** activation, associated with worse prognosis and an immune-poor (“deserted”) microenvironment; a tumor–fibroblast feedback loop (SPP1–CD44 and CCN2/TGF-β–TGFBR1) was proposed as actionable (guo2024singlecelltumorheterogeneity pages 1-2).

### 6.3 Cell types (CL suggestions)
- **CL:0000182** hepatocyte
- **CL:0000235** macrophage (tumor-associated macrophages)
- **CL:0000066** fibroblast (including CAFs)
- **CL:0000624** CD8-positive, alpha-beta T cell
- **CL:0000115** endothelial cell

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue level (UBERON suggestions)
- Primary organ: **liver** (UBERON:0002107)
- Commonly co-affected tissue state: **cirrhotic liver parenchyma** / fibrotic liver (context of chronic liver disease) (mattos2024hepatocellularcarcinomatherole pages 1-2, hwang2024hepatocellularcarcinomaupdates pages 1-3)

### 7.2 Subcellular/cellular components (GO cellular component suggestions)
Given the strong emphasis on transcriptional reprogramming, signaling, and metabolism in HCC, commonly implicated compartments include nucleus (GO:0005634), mitochondrion (GO:0005739), and plasma membrane (GO:0005886) (pathway-level support in 2024 mechanistic reviews) (szilveszter2024molecularmechanismsin pages 2-4).

---

## 8. Temporal development

### 8.1 Onset and progression
HCC usually develops over years in the context of chronic liver disease with progressive fibrosis/cirrhosis. Contemporary reviews emphasize that shifting etiologies (MASLD/ALD) may worsen ultrasound performance and complicate surveillance because MASLD-associated HCC can occur without cirrhosis (25–30% of MASLD-HCC cases without cirrhosis) (hwang2024hepatocellularcarcinomaupdates pages 6-7).

### 8.2 Staging systems (current practice)
Major guidelines commonly endorse **Barcelona Clinic Liver Cancer (BCLC)** staging to integrate tumor burden, liver function, and performance status, guiding therapy selection (seth2024clinicalpracticeguidelines pages 2-3, seth2024clinicalpracticeguidelines pages 10-11).

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
- **Global burden (GBD 2021):** ~529,000 new liver cancer cases and ~483,800 deaths in 2021; >70% of cases occur in Asia (hwang2024hepatocellularcarcinomaupdates pages 1-3).
- A 2024 surveillance review reports HCC as >800,000 new cases/year and 5-year overall survival ~18% (global summary) (wu2024hepatocellularcarcinomasurveillance pages 1-2).

### 9.2 Demographics
Sex disparity (higher incidence and mortality in men) and marked geographic variation by etiology (HBV-dominant regions in Asia/Africa; HCV prominent in specific countries; rising MASLD/ALD in Western settings) are emphasized in 2024 reviews (kinsey2024managementofhepatocellular pages 1-2, hwang2024hepatocellularcarcinomaupdates pages 1-3).

---

## 10. Diagnostics

### 10.1 Surveillance (real-world implementation)
**AASLD-aligned surveillance:** semi-annual (every 6 months) **abdominal ultrasound plus AFP** for at-risk populations (e.g., Child-Pugh A/B cirrhosis any etiology; Child-Pugh C if transplant candidate; selected non-cirrhotic HBV by risk stratification) (wu2024hepatocellularcarcinomasurveillance pages 4-5, hwang2024hepatocellularcarcinomaupdates pages 6-7). A contemporary review underscores that even ultrasound+AFP still misses over one-third of early-stage HCC (hwang2024hepatocellularcarcinomaupdates pages 6-7).

**MASLD-specific considerations (EASL-EASD-EASO 2024):** surveillance is strongly recommended for MASLD-related cirrhosis; not recommended for non-cirrhotic MASLD/MASH without severe fibrosis (<F3), while F3 may be considered case-by-case; MRI can be used when ultrasound visualization is poor ((easo)2024easleasdeasoclinicalpractice pages 46-48, (easo)2024easleasdeasoclinicalpractice pages 20-21).

### 10.2 Diagnostic imaging criteria (noninvasive diagnosis)
International imaging guidelines converge that **noninvasive HCC diagnosis applies only to high-risk patients**, and relies on **multiphasic contrast-enhanced CT or MRI** as first-line diagnostic exams (cannella2024esressentialsdiagnosis pages 1-3, cannella2024esressentialsdiagnosis pages 3-5). Major imaging features include:
- **Non-rim arterial phase hyperenhancement (APHE)**
- **Non-peripheral washout**
- **Enhancing capsule**
- **Threshold growth** (e.g., LI-RADS ≥50% increase in <6 months) (cannella2024esressentialsdiagnosis pages 5-7, cannella2024esressentialsdiagnosis pages 7-10)

A guideline-comparison table (cropped) is available here and summarizes the major features and size thresholds across EASL/AASLD(LI-RADS)/APASL/KLCA-NCC frameworks (cannella2024esressentialsdiagnosis media b948aa3a).

**Performance characteristics cited in ESR/ESGAR 2024:** a cited meta-analysis reports similar specificity for CT and MRI (>90%) but higher sensitivity for MRI (61–82% vs 48–66%), supporting MRI preference for small lesions when feasible (cannella2024esressentialsdiagnosis pages 3-5).

### 10.3 Biopsy
Biopsy is generally reserved for inconclusive imaging or non-cirrhotic contexts; it carries risks (bleeding, seeding) and non-trivial false-negative rate (~33% reported in a guideline review) (seth2024clinicalpracticeguidelines pages 2-3).

---

## 11. Outcome / prognosis

### 11.1 Survival statistics
- Global surveillance review summary: 5-year overall survival around **~18%** (wu2024hepatocellularcarcinomasurveillance pages 1-2).
- When detected at early stage and treated curatively, 5-year survival can exceed **60%** after resection or transplant in selected patients (wu2024hepatocellularcarcinomasurveillance pages 1-2).

### 11.2 Prognostic factors (examples)
- Liver function and tumor burden drive outcomes and treatment selection, motivating integrated staging frameworks (BCLC) and liver-function measures (e.g., ALBI) (xie2023areviewof pages 1-2, gordan2024systemictherapyfor pages 1-2).
- Molecular features can stratify recurrence and survival in genomic cohorts (e.g., LATS1 recurrence association; immune infiltration differences by TP53 vs CTNNB1) (wang2024novelgeneticalterations pages 1-2, song2024genomicprofilinginforms pages 1-2).

---

## 12. Treatment

### 12.1 Curative-intent local therapies (real-world implementations)
Contemporary guideline syntheses describe the standard curative-intent options for early-stage disease: **surgical resection, percutaneous ablation (e.g., RFA), and liver transplantation**, with transplant selection often using Milan criteria (single ≤5 cm or ≤3 lesions each ≤3 cm, no macrovascular invasion or extrahepatic spread) (wu2024hepatocellularcarcinomasurveillance pages 1-2, seth2024clinicalpracticeguidelines pages 10-11).

### 12.2 Locoregional therapies
Intermediate-stage disease often uses transarterial therapies (TACE) and other locoregional approaches; recent paradigms include combining locoregional with systemic therapy and conversion/downstaging approaches to enable later resection/transplant (li2024introductionto2023 pages 7-7, kinsey2024managementofhepatocellular pages 1-2).

**Example real-world combination implementation (2024):** TACE combined with atezolizumab+bevacizumab in an unresectable HCC multicenter cohort (n=92) had ORR 54.3% (mRECIST) / 41.3% (RECIST 1.1), median OS 15.9 months, median PFS 9.1 months, and grade 3/4 treatment-related AEs 16.3% (shen2024efficacyofatezolizumab pages 1-2).

### 12.3 Systemic therapy (authoritative 2024 guideline recommendations)
**ASCO Guideline Update (May 2024):**
- **Preferred first-line (Child-Pugh A; ECOG PS 0–1):** atezolizumab + bevacizumab **or** durvalumab + tremelimumab (gordan2024systemictherapyfor pages 1-2, gordan2024systemictherapyfor pages 2-4).
- If contraindications to those combinations: sorafenib, lenvatinib, or durvalumab may be offered first-line (gordan2024systemictherapyfor pages 2-4).
- Subsequent-line therapy depends on prior regimen; after atezo+bev, options include TKIs and ramucirumab for AFP ≥400 ng/mL; after durva+treme, a TKI is recommended; after sorafenib/lenvatinib, options include cabozantinib/regorafenib/ramucirumab (AFP ≥400) and immune checkpoint combinations (nivo+ipi) in selected patients (gordan2024systemictherapyfor pages 2-4, gordan2024systemictherapyfor pages 13-14).
- Panel emphasizes variceal screening/management prior to atezo+bev because bevacizumab increases bleeding risk, and recommends caution for Child-Pugh B patients (gordan2024systemictherapyfor pages 4-5, gordan2024systemictherapyfor pages 14-14).

**Pivotal efficacy benchmarks for atezolizumab+bevacizumab (IMbrave150):** Updated median OS 19.2 vs 13.4 months compared with sorafenib (HR 0.66, 95% CI 0.52–0.85) (finn2024efficacyandsafety pages 2-4). A 2024 IMbrave150 subgroup analysis for Vp4 portal vein tumor thrombosis reported median OS 7.6 vs 5.5 months and median PFS 5.4 vs 2.8 months for atezo+bev vs sorafenib, with grade ≥3 treatment-related AEs 43% vs 48% (finn2024efficacyandsafety pages 1-2).

**Real-world effectiveness (meta-analytic):** A 2023 single-arm meta-analysis of atezo+bev (23 studies; 3168 patients) reported pooled median OS 14.7 months, median PFS 6.66 months, ORR 26% (RECIST, long-term), and grade ≥3 AEs 30% (gao2023efficacyandsafety pages 1-2).

### 12.4 MAXO term suggestions (non-exhaustive)
- Liver transplantation; surgical resection; radiofrequency ablation; transarterial chemoembolization; immune checkpoint inhibitor therapy; anti-VEGF therapy; tyrosine kinase inhibitor therapy.

---

## 13. Prevention

### 13.1 Primary prevention
- **HBV vaccination and antiviral therapy** are credited with reducing HBV-related HCC burden over time (hwang2024hepatocellularcarcinomaupdates pages 1-3, hwang2024hepatocellularcarcinomaupdates pages 4-6).
- **Lifestyle/metabolic risk reduction (MASLD guideline, 2024):** weight loss targets for overweight MASLD: ≥5% reduces liver fat; 7–10% improves inflammation; ≥10% improves fibrosis; physical activity targets >150 min/week moderate or 75 min/week vigorous; discouraging alcohol and avoiding ultra-processed foods/sugar-sweetened beverages are recommended ((easo)2024easleasdeasoclinicalpractice pages 46-48, (easo)2024easleasdeasoclinicalpractice pages 10-11).

### 13.2 Secondary prevention (screening/surveillance)
Semi-annual ultrasound ± AFP surveillance in high-risk groups is the central population-level approach (wu2024hepatocellularcarcinomasurveillance pages 4-5, hwang2024hepatocellularcarcinomaupdates pages 6-7). For MASLD, surveillance is recommended for cirrhosis and individualized for F3 fibrosis ((easo)2024easleasdeasoclinicalpractice pages 46-48, (easo)2024easleasdeasoclinicalpractice pages 20-21).

---

## 14. Other species / natural disease
No veterinary or wildlife comparative HCC evidence was retrieved in the current evidence set. (No claim can be supported here without additional targeted retrieval.)

---

## 15. Model organisms and experimental models

### 15.1 Model system landscape (2024 synthesis)
A 2024 review summarizes HCC models spanning chemically/dietary induced models (e.g., DEN; CCl4; NASH diets), genetic/oncogene-driven models (including hydrodynamic tail vein injection and transposon systems), transplantation models (xenografts/PDX; heterotopic and orthotopic), and advanced ex vivo/in vitro platforms (precision-cut tissue slices, organoids, organ-on-chip) (cigliano2024preclinicalmodelsof pages 1-2, cigliano2024preclinicalmodelsof pages 17-18).

### 15.2 Key examples and limitations
- **DEN chemical model:** typically yields HCC by ~40 weeks, male predominant; commonly produces Ras/MAPK-leaning mutation spectra (activating Hras/Braf/Egfr), which can differ from human CTNNB1 mutation patterns (cigliano2024preclinicalmodelsof pages 7-9, cigliano2024preclinicalmodelsof pages 9-10).
- **CCl4 and NASH/fibrosis models:** used to induce liver injury/fibrosis and model NASH→HCC contexts; outcomes are strain- and protocol-dependent (cigliano2024preclinicalmodelsof pages 17-18, cigliano2024preclinicalmodelsof pages 9-10).
- **Hydrodynamic tail vein injection (HTVI):** enables rapid, pathway-specific tumor modeling (e.g., AKT/Ras; c-Met/sgPten; AKT/β-catenin), supporting targeted drug testing and mechanistic studies of initiation (cigliano2024preclinicalmodelsof pages 15-17, cigliano2024preclinicalmodelsof pages 20-21).
- **Organoids:** can retain genomic features/heterogeneity and support screening, but often lack immune/vascular components and can be technically challenging with limited establishment success (e.g., ~30% patient-derived tumoroids reported) (cigliano2024preclinicalmodelsof pages 6-7, cigliano2024preclinicalmodelsof pages 1-2).

---

## Expert opinions / analysis (authoritative sources, 2024)

1) **Systemic therapy sequencing remains complex**: ASCO (2024) emphasizes shared decision-making (toxicity, cost, bleeding risk, autoimmune risk) and cautions extrapolation beyond trial populations (mostly Child-Pugh A), reflecting real-world complexity in patients with cirrhosis (gordan2024systemictherapyfor pages 2-4, gordan2024systemictherapyfor pages 14-14).

2) **Noninvasive imaging diagnosis requires context**: ESR/ESGAR (2024) stresses that noninvasive diagnosis is restricted to high-risk patients and requires combining major imaging features, not relying on a single sign; guideline differences around hepatobiliary phase features can alter sensitivity/specificity (cannella2024esressentialsdiagnosis pages 1-3, cannella2024esressentialsdiagnosis pages 7-10).

3) **Etiology shift is altering detection and outcomes**: The CMH 2024 epidemiology update argues ultrasound surveillance may perform worse as MASLD/ALD increase, and MASLD-associated HCC can arise without cirrhosis—challenging traditional “cirrhosis-only” surveillance paradigms (hwang2024hepatocellularcarcinomaupdates pages 6-7, hwang2024hepatocellularcarcinomaupdates pages 1-3).

---

## Notes on evidence gaps in this run
- **MONDO and MeSH IDs** were not successfully retrieved in the available evidence excerpts; additional ontology-specific retrieval would be required for a fully populated identifier panel.
- **PMID-level citations** were not consistently available from the retrieved excerpts; therefore this report cites DOI/URLs and the provided evidence context IDs.

---

## Key URLs (selected)
- ASCO 2024 guideline update (published May 2024): https://doi.org/10.1200/JCO.23.02745 (gordan2024systemictherapyfor pages 1-2)
- ESR/ESGAR imaging recommendations (published Feb 2024): https://doi.org/10.1007/s00330-024-10606-w (cannella2024esressentialsdiagnosis pages 1-3)
- EASL-EASD-EASO MASLD guideline (published Jun 2024): https://doi.org/10.1159/000539371 ((easo)2024easleasdeasoclinicalpractice pages 46-48)
- CMH epidemiology/surveillance update (published Dec 2024 online): https://doi.org/10.3350/cmh.2024.0824 (hwang2024hepatocellularcarcinomaupdates pages 1-3)
- IMbrave150 Vp4 PVTT subgroup analysis (published Jun 2024): https://doi.org/10.1159/000539897 (finn2024efficacyandsafety pages 1-2)


References

1. (OpenTargets Search: hepatocellular carcinoma): Open Targets Query (hepatocellular carcinoma, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (hwang2024hepatocellularcarcinomaupdates pages 1-3): Soo Young Hwang, Pojsakorn Danpanichkul, Vatche Agopian, Neil Mehta, Neehar D. Parikh, Ghassan K. Abou-Alfa, Amit G. Singal, and Ju Dong Yang. Hepatocellular carcinoma: updates on epidemiology, surveillance, diagnosis and treatment. Clinical and Molecular Hepatology, Dec 2024. URL: https://doi.org/10.3350/cmh.2024.0824, doi:10.3350/cmh.2024.0824. This article has 238 citations.

3. (kinsey2024managementofhepatocellular pages 1-2): Emily Kinsey and Hannah M. Lee. Management of hepatocellular carcinoma in 2024: the multidisciplinary paradigm in an evolving treatment landscape. Cancers, 16:666, Feb 2024. URL: https://doi.org/10.3390/cancers16030666, doi:10.3390/cancers16030666. This article has 136 citations.

4. (cannella2024esressentialsdiagnosis pages 1-3): Roberto Cannella, Marc Zins, and Giuseppe Brancatelli. Esr essentials: diagnosis of hepatocellular carcinoma—practice recommendations by esgar. European Radiology, 34:2127-2139, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10606-w, doi:10.1007/s00330-024-10606-w. This article has 32 citations and is from a domain leading peer-reviewed journal.

5. (mattos2024hepatocellularcarcinomatherole pages 1-2): Angelo Zambam de Mattos, Isadora Zanotelli Bombassaro, Arndt Vogel, and Jose D Debes. Hepatocellular carcinoma-the role of the underlying liver disease in clinical practice. World Journal of Gastroenterology, 30:2488-2495, May 2024. URL: https://doi.org/10.3748/wjg.v30.i19.2488, doi:10.3748/wjg.v30.i19.2488. This article has 13 citations.

6. (hwang2024hepatocellularcarcinomaupdates pages 6-7): Soo Young Hwang, Pojsakorn Danpanichkul, Vatche Agopian, Neil Mehta, Neehar D. Parikh, Ghassan K. Abou-Alfa, Amit G. Singal, and Ju Dong Yang. Hepatocellular carcinoma: updates on epidemiology, surveillance, diagnosis and treatment. Clinical and Molecular Hepatology, Dec 2024. URL: https://doi.org/10.3350/cmh.2024.0824, doi:10.3350/cmh.2024.0824. This article has 238 citations.

7. (gordan2024systemictherapyfor pages 1-2): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 285 citations and is from a highest quality peer-reviewed journal.

8. ((easo)2024easleasdeasoclinicalpractice pages 46-48): European Association for the Study of the Liver (EASL). Easl-easd-easo clinical practice guidelines on the management of metabolic dysfunction-associated steatotic liver disease (masld). Obesity Facts, 17:374-444, Jun 2024. URL: https://doi.org/10.1159/000539371, doi:10.1159/000539371. This article has 316 citations and is from a peer-reviewed journal.

9. (shen2024efficacyofatezolizumab pages 1-2): Xiao Shen, Jin-Xing Zhang, Jin Liu, Sheng Liu, Hai-Bin Shi, Yuan Cheng, Qing-Qiao Zhang, Guo-Wen Yin, and Qing-Quan Zu. Efficacy of atezolizumab plus bevacizumab combined with transarterial chemoembolization for unresectable hepatocellular carcinoma: a real-world study. Journal of Hepatocellular Carcinoma, 11:1993-2003, Oct 2024. URL: https://doi.org/10.2147/jhc.s478604, doi:10.2147/jhc.s478604. This article has 4 citations and is from a peer-reviewed journal.

10. (song2024genomicprofilinginforms pages 1-2): Mengqi Song, Haoyue Cheng, Hao Zou, Kai Ma, Lianfang Lu, Qian Wei, Zejiang Xu, Zirui Tang, Yuanzheng Zhang, Yinan Wang, and Chuandong Sun. Genomic profiling informs therapies and prognosis for patients with hepatocellular carcinoma in clinical practice. BMC Cancer, Jun 2024. URL: https://doi.org/10.1186/s12885-024-12407-2, doi:10.1186/s12885-024-12407-2. This article has 8 citations and is from a peer-reviewed journal.

11. (hwang2024hepatocellularcarcinomaupdates pages 4-6): Soo Young Hwang, Pojsakorn Danpanichkul, Vatche Agopian, Neil Mehta, Neehar D. Parikh, Ghassan K. Abou-Alfa, Amit G. Singal, and Ju Dong Yang. Hepatocellular carcinoma: updates on epidemiology, surveillance, diagnosis and treatment. Clinical and Molecular Hepatology, Dec 2024. URL: https://doi.org/10.3350/cmh.2024.0824, doi:10.3350/cmh.2024.0824. This article has 238 citations.

12. (peruhova2024geneticscreeningof pages 2-4): Milena Peruhova, Sonya Banova-Chakarova, Dimitrina Georgieva Miteva, and Tsvetelina Velikova. Genetic screening of liver cancer: state of the art. World Journal of Hepatology, 16:716-730, May 2024. URL: https://doi.org/10.4254/wjh.v16.i5.716, doi:10.4254/wjh.v16.i5.716. This article has 7 citations.

13. (ucdal2024crosstalkbetween pages 1-2): Mete Ucdal, Ayşe Buruş, and B. Çeltikçi. Cross talk between genetics and biochemistry in the pathogenesis of hepatocellular carcinoma. Hepatology Forum, 5:150-160, Jul 2024. URL: https://doi.org/10.14744/hf.2023.2023.0028, doi:10.14744/hf.2023.2023.0028. This article has 2 citations.

14. (wu2024hepatocellularcarcinomasurveillance pages 1-2): Gavin Wu, Nojan Bajestani, Nooruddin Pracha, Cindy Chen, and Mina S. Makary. Hepatocellular carcinoma surveillance strategies: major guidelines and screening advances. Cancers, 16:3933, Nov 2024. URL: https://doi.org/10.3390/cancers16233933, doi:10.3390/cancers16233933. This article has 24 citations.

15. (seth2024clinicalpracticeguidelines pages 2-3): Ishith Seth, Adrian Siu, Lyndel Hewitt, Ulvi Budak, Beshoy Farah, and Mouhannad Jaber. Clinical practice guidelines for the management of hepatocellular carcinoma: a systematic review. Journal of Gastrointestinal Cancer, 55:318-331, Jul 2024. URL: https://doi.org/10.1007/s12029-023-00961-0, doi:10.1007/s12029-023-00961-0. This article has 4 citations.

16. (szilveszter2024molecularmechanismsin pages 2-4): Raluca-Margit Szilveszter, M. Muntean, and Adrian-Florin Florea. Molecular mechanisms in tumorigenesis of hepatocellular carcinoma and in target treatments—an overview. Biomolecules, 14:656, Jun 2024. URL: https://doi.org/10.3390/biom14060656, doi:10.3390/biom14060656. This article has 18 citations.

17. (pessino2024hepatocellularcarcinomaold pages 15-17): Greta Pessino, Claudia Scotti, and Maristella Maggi. Hepatocellular carcinoma: old and emerging therapeutic targets. Cancers, 16:901, Feb 2024. URL: https://doi.org/10.3390/cancers16050901, doi:10.3390/cancers16050901. This article has 42 citations.

18. (wang2024novelgeneticalterations pages 1-2): Yizhou Wang, Pei-pei Shang, Chang Xu, Wei Dong, Xiaofeng Zhang, Yong Xia, Chengjun Sui, and Cheng Yang. Novel genetic alterations in liver cancer distinguish distinct clinical outcomes and combination immunotherapy responses. Frontiers in Pharmacology, Jun 2024. URL: https://doi.org/10.3389/fphar.2024.1416295, doi:10.3389/fphar.2024.1416295. This article has 3 citations.

19. ((easo)2024easleasdeasoclinicalpractice pages 10-11): European Association for the Study of the Liver (EASL). Easl-easd-easo clinical practice guidelines on the management of metabolic dysfunction-associated steatotic liver disease (masld). Obesity Facts, 17:374-444, Jun 2024. URL: https://doi.org/10.1159/000539371, doi:10.1159/000539371. This article has 316 citations and is from a peer-reviewed journal.

20. (cigliano2024preclinicalmodelsof pages 9-10): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.

21. (kassem2024genomiclandscapeof pages 1-2): Perihan Hamdy Kassem, Iman Fawzy Montasser, Ramy Mohamed Mahmoud, Rasha Ahmed Ghorab, Dina A. AbdelHakam, Marium EL Sayed Ahmad Fathi, Marwa A. Abdel Wahed, Khaled Mohey, Mariam Ibrahim, Mohamed El Hadidi, Yasmine M. Masssoud, Manar Salah, Arwa Abugable, Mohamad Bahaa, Sherif El Khamisy, and Mahmoud El Meteini. Genomic landscape of hepatocellular carcinoma in egyptian patients by whole exome sequencing. BMC Medical Genomics, Aug 2024. URL: https://doi.org/10.1186/s12920-024-01965-w, doi:10.1186/s12920-024-01965-w. This article has 5 citations and is from a peer-reviewed journal.

22. (li2024singlecellanalyses pages 1-2): Yao Li, Fengwei Li, Lei Xu, Xiaodong Shi, Hui Xue, Jianwei Liu, Shilei Bai, Yeye Wu, Zhao Yang, Feng Xue, Yong Xia, Hui Dong, Feng Shen, and Kui Wang. Single cell analyses reveal the pd-1 blockade response-related immune features in hepatocellular carcinoma. Theranostics, 14:3526-3547, Jun 2024. URL: https://doi.org/10.7150/thno.95971, doi:10.7150/thno.95971. This article has 22 citations and is from a domain leading peer-reviewed journal.

23. (li2024singlecellanalyses pages 6-8): Yao Li, Fengwei Li, Lei Xu, Xiaodong Shi, Hui Xue, Jianwei Liu, Shilei Bai, Yeye Wu, Zhao Yang, Feng Xue, Yong Xia, Hui Dong, Feng Shen, and Kui Wang. Single cell analyses reveal the pd-1 blockade response-related immune features in hepatocellular carcinoma. Theranostics, 14:3526-3547, Jun 2024. URL: https://doi.org/10.7150/thno.95971, doi:10.7150/thno.95971. This article has 22 citations and is from a domain leading peer-reviewed journal.

24. (guo2024singlecelltumorheterogeneity pages 1-2): De-Zhen Guo, Xin Zhang, Sen-Quan Zhang, Shi-Yu Zhang, Xiang-Yu Zhang, Jia-Yan Yan, San-Yuan Dong, Kai Zhu, Xin-Rong Yang, Jia Fan, Jian Zhou, and Ao Huang. Single-cell tumor heterogeneity landscape of hepatocellular carcinoma: unraveling the pro-metastatic subtype and its interaction loop with fibroblasts. Molecular Cancer, Aug 2024. URL: https://doi.org/10.1186/s12943-024-02062-3, doi:10.1186/s12943-024-02062-3. This article has 69 citations and is from a highest quality peer-reviewed journal.

25. (seth2024clinicalpracticeguidelines pages 10-11): Ishith Seth, Adrian Siu, Lyndel Hewitt, Ulvi Budak, Beshoy Farah, and Mouhannad Jaber. Clinical practice guidelines for the management of hepatocellular carcinoma: a systematic review. Journal of Gastrointestinal Cancer, 55:318-331, Jul 2024. URL: https://doi.org/10.1007/s12029-023-00961-0, doi:10.1007/s12029-023-00961-0. This article has 4 citations.

26. (wu2024hepatocellularcarcinomasurveillance pages 4-5): Gavin Wu, Nojan Bajestani, Nooruddin Pracha, Cindy Chen, and Mina S. Makary. Hepatocellular carcinoma surveillance strategies: major guidelines and screening advances. Cancers, 16:3933, Nov 2024. URL: https://doi.org/10.3390/cancers16233933, doi:10.3390/cancers16233933. This article has 24 citations.

27. ((easo)2024easleasdeasoclinicalpractice pages 20-21): European Association for the Study of the Liver (EASL). Easl-easd-easo clinical practice guidelines on the management of metabolic dysfunction-associated steatotic liver disease (masld). Obesity Facts, 17:374-444, Jun 2024. URL: https://doi.org/10.1159/000539371, doi:10.1159/000539371. This article has 316 citations and is from a peer-reviewed journal.

28. (cannella2024esressentialsdiagnosis pages 3-5): Roberto Cannella, Marc Zins, and Giuseppe Brancatelli. Esr essentials: diagnosis of hepatocellular carcinoma—practice recommendations by esgar. European Radiology, 34:2127-2139, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10606-w, doi:10.1007/s00330-024-10606-w. This article has 32 citations and is from a domain leading peer-reviewed journal.

29. (cannella2024esressentialsdiagnosis pages 5-7): Roberto Cannella, Marc Zins, and Giuseppe Brancatelli. Esr essentials: diagnosis of hepatocellular carcinoma—practice recommendations by esgar. European Radiology, 34:2127-2139, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10606-w, doi:10.1007/s00330-024-10606-w. This article has 32 citations and is from a domain leading peer-reviewed journal.

30. (cannella2024esressentialsdiagnosis pages 7-10): Roberto Cannella, Marc Zins, and Giuseppe Brancatelli. Esr essentials: diagnosis of hepatocellular carcinoma—practice recommendations by esgar. European Radiology, 34:2127-2139, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10606-w, doi:10.1007/s00330-024-10606-w. This article has 32 citations and is from a domain leading peer-reviewed journal.

31. (cannella2024esressentialsdiagnosis media b948aa3a): Roberto Cannella, Marc Zins, and Giuseppe Brancatelli. Esr essentials: diagnosis of hepatocellular carcinoma—practice recommendations by esgar. European Radiology, 34:2127-2139, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10606-w, doi:10.1007/s00330-024-10606-w. This article has 32 citations and is from a domain leading peer-reviewed journal.

32. (xie2023areviewof pages 1-2): Di-Yang Xie, Kai Zhu, Zheng-Gang Ren, Jian Zhou, Jia Fan, and Qiang Gao. A review of 2022 chinese clinical guidelines on the management of hepatocellular carcinoma: updates and insights. Hepatobiliary Surgery and Nutrition, 12:216-228, Apr 2023. URL: https://doi.org/10.21037/hbsn-22-469, doi:10.21037/hbsn-22-469. This article has 157 citations and is from a peer-reviewed journal.

33. (li2024introductionto2023 pages 7-7): Jiexun Li, Zhuoran Qi, Jian Zhang, Sinuo Chen, and Jinglin Xia. Introduction to 2023 chinese expert consensus on the whole-course management of hepatocellular carcinoma. Hepatoma Research, Mar 2024. URL: https://doi.org/10.20517/2394-5079.2024.16, doi:10.20517/2394-5079.2024.16. This article has 0 citations.

34. (gordan2024systemictherapyfor pages 2-4): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 285 citations and is from a highest quality peer-reviewed journal.

35. (gordan2024systemictherapyfor pages 13-14): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 285 citations and is from a highest quality peer-reviewed journal.

36. (gordan2024systemictherapyfor pages 4-5): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 285 citations and is from a highest quality peer-reviewed journal.

37. (gordan2024systemictherapyfor pages 14-14): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 285 citations and is from a highest quality peer-reviewed journal.

38. (finn2024efficacyandsafety pages 2-4): Richard S. Finn, Peter R. Galle, Michel Ducreux, Ann-Lii Cheng, Norelle Reilly, Alan Nicholas, Sairy Hernandez, Ning Ma, Philippe Merle, Riad Salem, Daneng Li, and Valeriy Breder. Efficacy and safety of atezolizumab plus bevacizumab versus sorafenib in hepatocellular carcinoma with main trunk and/or contralateral portal vein invasion in imbrave150. Liver Cancer, 13:1-14, Jun 2024. URL: https://doi.org/10.1159/000539897, doi:10.1159/000539897. This article has 50 citations and is from a peer-reviewed journal.

39. (finn2024efficacyandsafety pages 1-2): Richard S. Finn, Peter R. Galle, Michel Ducreux, Ann-Lii Cheng, Norelle Reilly, Alan Nicholas, Sairy Hernandez, Ning Ma, Philippe Merle, Riad Salem, Daneng Li, and Valeriy Breder. Efficacy and safety of atezolizumab plus bevacizumab versus sorafenib in hepatocellular carcinoma with main trunk and/or contralateral portal vein invasion in imbrave150. Liver Cancer, 13:1-14, Jun 2024. URL: https://doi.org/10.1159/000539897, doi:10.1159/000539897. This article has 50 citations and is from a peer-reviewed journal.

40. (gao2023efficacyandsafety pages 1-2): Xiaoqiang Gao, Rui Zhao, Huaxing Ma, and Shi Zuo. Efficacy and safety of atezolizumab plus bevacizumab treatment for advanced hepatocellular carcinoma in the real world: a single-arm meta-analysis. BMC Cancer, Jul 2023. URL: https://doi.org/10.1186/s12885-023-11112-w, doi:10.1186/s12885-023-11112-w. This article has 28 citations and is from a peer-reviewed journal.

41. (cigliano2024preclinicalmodelsof pages 1-2): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.

42. (cigliano2024preclinicalmodelsof pages 17-18): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.

43. (cigliano2024preclinicalmodelsof pages 7-9): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.

44. (cigliano2024preclinicalmodelsof pages 15-17): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.

45. (cigliano2024preclinicalmodelsof pages 20-21): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.

46. (cigliano2024preclinicalmodelsof pages 6-7): Antonio Cigliano, Weiting Liao, Giovanni A. Deiana, Davide Rizzo, Xin Chen, and Diego F. Calvisi. Preclinical models of hepatocellular carcinoma: current utility, limitations, and challenges. Biomedicines, 12:1624, Jul 2024. URL: https://doi.org/10.3390/biomedicines12071624, doi:10.3390/biomedicines12071624. This article has 26 citations.
