---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:29:35.863321'
end_time: '2026-05-09T11:01:15.567741'
duration_seconds: 1899.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Platelet-Type von Willebrand Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Platelet-Type von Willebrand Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Platelet-Type von Willebrand Disease** covering all of the
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
- **Disease Name:** Platelet-Type von Willebrand Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Platelet-Type von Willebrand Disease** covering all of the
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


# Platelet-Type von Willebrand Disease (PT‑VWD): Disease Characteristics Research Report

## Executive summary
Platelet-type von Willebrand disease (PT‑VWD) is a rare **autosomal dominant** inherited platelet disorder (a VWD mimic) caused by **gain-of-function (GoF) variants in GP1BA (GPIbα)** that increase platelet binding to von Willebrand factor (VWF), leading to removal of high-molecular-weight (HMW) VWF multimers and sometimes platelet–VWF complexes from circulation, with mucocutaneous bleeding and variable thrombocytopenia/macrothrombocytopenia. It is **frequently misdiagnosed as VWD type 2B**, and correct discrimination is clinically critical because management differs—**platelet transfusion is generally preferred**, while therapies that raise VWF (e.g., desmopressin) can worsen thrombocytopenia. (othman12011platelettypevonwillebrand pages 1-2, othman2011platelettypevonwillebrand pages 3-5)

Recent work (2023) expands the pathogenic variant landscape beyond the “classic” C‑terminal disulphide loop region of GPIbα (e.g., new leucine-rich repeat variants such as p.Leu194Phe), reinforcing the need for **GP1BA sequencing** when the phenotype resembles type 2B VWD. (monteiro2023anewcase pages 1-2)


## 1. Disease information

### 1.1 Overview (what is the disease?)
PT‑VWD is an inherited bleeding disorder in which the primary defect lies in the platelet receptor **GPIbα** (encoded by **GP1BA**), not in plasma VWF; it produces a **VWD-like phenotype** with enhanced platelet–VWF interaction, loss of HMW VWF multimers in plasma, and bleeding. (othman2011platelettypevonwillebrand pages 3-5)

**Direct abstract quote (definition/pathogenesis):** Haematologica’s mechanistic study states PT‑VWD is “**characterized by thrombocytopenia with large platelets caused by gain-of-function variants in GP1BA leading to enhanced GPIbα-von Willebrand factor (vWF) interaction**.” (bury2019mechanismsofthrombocytopenia pages 1-5)

### 1.2 Synonyms / alternative names
- Platelet-type von Willebrand disease (PT‑VWD) (othman12011platelettypevonwillebrand pages 1-2)
- Pseudo–von Willebrand disease / platelet-type pseudo‑VWD (historical) (othman2011platelettypevonwillebrand pages 5-6)

### 1.3 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
The accessible full texts reviewed here **did not report OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO identifiers** in extractable form. This is an evidence gap for this tool-run corpus and should be filled by consulting OMIM/Orphanet/MONDO directly.

### 1.4 Evidence source type
Most PT‑VWD evidence is **aggregated disease-level** from reviews/registries and **individual-level** from case reports and mechanistic studies, including human megakaryocyte experiments and transgenic mouse models. (othman2016platelettypevon pages 2-3, bury2019mechanismsofthrombocytopenia pages 1-5)


## 2. Etiology

### 2.1 Disease causal factors
- **Genetic (primary):** GoF variants in **GP1BA** leading to increased affinity of platelet GPIbα for VWF A1 domain and inappropriate platelet–VWF binding. (othman12011platelettypevonwillebrand pages 1-2, othman2011platelettypevonwillebrand pages 3-5)

### 2.2 Risk factors
- **Family history** consistent with autosomal dominant inheritance. (othman12011platelettypevonwillebrand pages 2-3)
- **Physiologic states raising VWF** (pregnancy, stress, infection) can aggravate thrombocytopenia/bleeding phenotype by increasing VWF available for mutant platelet binding. (othman2011platelettypevonwillebrand pages 3-5)
- **Antiplatelet medications** (e.g., aspirin) may worsen bleeding. (othman12011platelettypevonwillebrand pages 1-2, othman12011platelettypevonwillebrand pages 2-3)

### 2.3 Protective factors
Not specifically identified in the retrieved corpus.

### 2.4 Gene–environment interactions
No PT‑VWD–specific gene–environment interaction studies were identified in the retrieved corpus; physiologic VWF increases (e.g., pregnancy) may be viewed as an exposure that interacts with GP1BA GoF variants. (othman2011platelettypevonwillebrand pages 3-5)


## 3. Phenotypes

### 3.1 Core phenotype spectrum
**Bleeding (symptoms/signs):** Typically mild-to-moderate mucocutaneous bleeding (epistaxis, post-dental extraction bleeding, postsurgical bleeding), often exacerbated in pregnancy or with aspirin/antiplatelet drugs. (othman12011platelettypevonwillebrand pages 2-3, othman2011platelettypevonwillebrand pages 2-3)

**Laboratory abnormalities:**
- Enhanced ristocetin-induced platelet aggregation/agglutination (**enhanced RIPA** at low ristocetin). (othman2011platelettypevonwillebrand pages 2-3)
- Selective loss of **HMW VWF multimers** from plasma; discordance between functional and antigen assays (e.g., reduced VWF activity relative to VWF:Ag). (othman2011platelettypevonwillebrand pages 3-5, othman12011platelettypevonwillebrand pages 3-4)
- Variable thrombocytopenia; can include platelet clumping and macrothrombocytopenia. (othman2011platelettypevonwillebrand pages 3-5, othman12011platelettypevonwillebrand pages 3-4)

**Quantitative example (2023 case report):** platelet count range reported 127–161×10^9/L and MPV examples 12–14.2 fL (above referenced normal range). (monteiro2023anewcase pages 2-2)

### 3.2 Phenotype characteristics (age of onset, severity, progression)
- Often recognized after hemostatic challenges (e.g., surgery) and may be underrecognized because many patients “do not seek advice unless they have serious bleeds.” (othman12011platelettypevonwillebrand pages 2-3)
- Severity: commonly mild-to-moderate; registry authors describe “moderate bleeding diathesis.” (othman2016platelettypevon pages 2-3)
- Course: chronic/lifelong inherited disorder with episodic bleeding around challenges.

### 3.3 Suggested HPO terms (non-exhaustive)
(Informatic suggestions based on phenotypes explicitly described in the literature)
- Epistaxis (HP:0000421) (othman12011platelettypevonwillebrand pages 2-3)
- Abnormal bleeding (HP:0001892)
- Postoperative hemorrhage (HP:0002783) (othman12011platelettypevonwillebrand pages 2-3)
- Menorrhagia (HP:0000132) *not directly evidenced in retrieved PT‑VWD texts; common in mucocutaneous bleeding disorders—mark as potential but unconfirmed here*
- Thrombocytopenia (HP:0001873) (othman12011platelettypevonwillebrand pages 2-3)
- Macrothrombocytopenia (HP:0001902) (othman2011platelettypevonwillebrand pages 3-5, monteiro2023anewcase pages 2-2)
- Increased mean platelet volume (laboratory phenotype; maps to macrothrombocytopenia context) (monteiro2023anewcase pages 2-2)

### 3.4 Quality-of-life impact
Not quantified in retrieved corpus; mucocutaneous bleeding and pregnancy/periprocedural planning plausibly impacts daily functioning.


## 4. Genetic / molecular information

### 4.1 Causal gene(s)
- **GP1BA** (platelet glycoprotein Ibα) is the causal gene for PT‑VWD; definitive diagnosis is by identification of causative GP1BA mutation. (othman2011platelettypevonwillebrand pages 2-3, othman12011platelettypevonwillebrand pages 3-4)

### 4.2 Pathogenic variant spectrum (representative)
A 2025 population-genetic prevalence analysis enumerated **9 distinct GP1BA variants** previously reported to cause PT‑VWD: **p.Arg127Gln, p.Leu194Phe, p.Trp246Leu, p.Gly249Val, p.Gly249Ser, p.Asp251Tyr, p.Met255Val, p.Met255Ile, and p.Thr436_Ala444del**. (seidizadeh2025globalprevalenceof pages 3-4)

Older reviews described classic variants such as **p.Gly233Val, p.Met239Val, p.Gly233Ser** and a 27 bp in-frame deletion. (othman2011platelettypevonwillebrand pages 3-5, othman12011platelettypevonwillebrand pages 2-3)

**Recent development (2023):** A case report identified a novel/rare GoF variant **c.580C>T (p.Leu194Phe)** in a leucine-rich repeat of GPIbα, supporting that disease-causing GoF variants can occur outside the classic C‑terminal disulphide loop region. (monteiro2023anewcase pages 1-2)

### 4.3 Functional consequence
GoF variants increase spontaneous or low-threshold binding of VWF A1 to the GPIbα leucine-rich repeat concavity / regulatory loops, promoting platelet–VWF complex formation and clearance. (othman12011platelettypevonwillebrand pages 3-4, monteiro2023anewcase pages 2-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
Not identified in retrieved corpus.


## 5. Environmental information
PT‑VWD is primarily genetic; key modulating “exposures” include physiologic VWF increases (pregnancy, stress, infection) and medications that affect platelet function (aspirin). (othman12011platelettypevonwillebrand pages 2-3, othman2011platelettypevonwillebrand pages 3-5)


## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current understanding)
1) **GP1BA GoF variant → hyperresponsive GPIbα** with increased affinity for VWF (othman2011platelettypevonwillebrand pages 3-5)
2) **Inappropriate platelet–VWF binding** (including HMW multimers) → (a) selective depletion of HMW VWF multimers from plasma and reduced platelet-dependent VWF activity; (b) formation of platelet–VWF complexes subject to accelerated clearance (seidizadeh2025globalprevalenceof pages 1-3, bury2019mechanismsofthrombocytopenia pages 1-5)
3) **Thrombocytopenia/macrothrombocytopenia** arises from combined mechanisms: impaired thrombopoiesis (abnormal proplatelet formation), ectopic platelet release in bone marrow, and increased clearance. (bury2019mechanismsofthrombocytopenia pages 1-5)

### 6.2 Cellular mechanisms and pathways (primary experimental evidence)
A key mechanistic study using patient-derived megakaryocytes (GP1BA Met239Val) and a transgenic mouse (GPIbα Gly233Val) found:
- Early VWF binding during megakaryocyte differentiation and abnormal proplatelet formation with fewer enlarged tips (bury2019mechanismsofthrombocytopenia pages 1-5)
- Ectopic proplatelet formation on type I collagen, linked to defective collagen-triggered signaling with impaired **RhoA–ROCK–MLC2** axis activation and altered **Lyn (SFK)/GPVI-related** signaling (bury2019mechanismsofthrombocytopenia pages 1-5)
- Increased extravascular platelets in bone marrow and shortened platelet survival; desmopressin-induced VWF rise produced a marked platelet count drop in mutant mice. (bury2019mechanismsofthrombocytopenia pages 1-5)

### 6.3 Suggested ontology terms
**GO biological processes (suggested):**
- Platelet activation (GO:0030168)
- Platelet aggregation (GO:0070527)
- Hemostasis (GO:0007599)
- Megakaryocyte differentiation (GO:0030219)
- Platelet formation / thrombopoiesis (GO:0030218)
- Regulation of actin cytoskeleton organization (GO:0032956) (mechanistically relevant to proplatelet formation)

**Cell Ontology (CL) terms (suggested):**
- Megakaryocyte (CL:0000556) (bury2019mechanismsofthrombocytopenia pages 1-5)
- Platelet (thrombocyte) (CL:0000233)


## 7. Anatomical structures affected
- Primary: blood/vascular compartment; **platelets** and circulating **VWF multimers**. (othman12011platelettypevonwillebrand pages 1-2)
- Bone marrow megakaryopoiesis/thrombopoiesis is implicated (ectopic release; increased extravascular platelets). (bury2019mechanismsofthrombocytopenia pages 1-5)

**UBERON term suggestions:**
- Bone marrow (UBERON:0002371)
- Blood (UBERON:0000178)
- Spleen (UBERON:0002106) (mouse splenomegaly reported). (othman2011platelettypevonwillebrand pages 5-6)


## 8. Temporal development
Typical onset is congenital/inherited, but clinical recognition is often delayed until bleeding challenges. (othman12011platelettypevonwillebrand pages 2-3)


## 9. Inheritance and population

### 9.1 Inheritance
Autosomal dominant. (seidizadeh2025globalprevalenceof pages 1-3, othman12011platelettypevonwillebrand pages 2-3)

### 9.2 Epidemiology and statistics
**Case-based counts and registries:**
- 2011 review: “**44 cases (31 females and 13 males) of 18 families**” known at that time. (othman12011platelettypevonwillebrand pages 2-3)
- ISTH SSC registry/website report (2016): international registry lists **55 cases** (17 males, 38 females). (othman2016platelettypevon pages 2-3)

**Misdiagnosis:**
- International registry project analyzing putative type 2B/PT-VWD: 17/110 had GP1BA mutations consistent with PT‑VWD; authors estimate **~15% misdiagnosis rate** of PT‑VWD (misdiagnosed as 2B). (othman2016platelettypevon pages 2-2, othman2011platelettypevonwillebrand pages 5-6)

**Population-genetic prevalence estimate (gnomAD v4.1):**
- Estimated global prevalence **136 per 10^6** (2.5 per 10^6 “severe,” 134 per 10^6 “mild”). Highest subgroup estimates: Africans/African Americans 160 per 10^6; Finnish 156 per 10^6; Europeans 149 per 10^6; South Asians 110 per 10^6. (seidizadeh2025globalprevalenceof pages 1-3)


## 10. Diagnostics

### 10.1 Key clinical/laboratory tests and diagnostic features
PT‑VWD and type 2B VWD are both characterized by **enhanced RIPA**, reduced HMW multimers, and often thrombocytopenia—making differentiation challenging. (othman12011platelettypevonwillebrand pages 3-4)

**RIPA operationalization and thresholds (real-world implementation):**
- RIPA performed on PRP (example adjustment to 250×10^9/L) using at least two ristocetin concentrations, typically **1.0 mg/mL (high) and 0.5 mg/mL (low)**; some centers use low-dose **0.6–0.7 mg/mL** or a dose yielding ~30% aggregation. (othman2011platelettypevonwillebrand pages 2-3)
- Caveat: some type 2B cases can respond at intermediate low levels (~0.7 mg/mL), so cutoffs overlap. (othman12011platelettypevonwillebrand pages 3-4)

**VWF activity/antigen ratio guidance:**
- ISTH SSC communication notes VWF:RCo/VWF:Ag ratio **<0.6** as part of the PT‑VWD laboratory picture (with enhanced RIPA and HMW multimer loss). (othman2016platelettypevon pages 1-2)

### 10.2 Specialized discrimination tests (PT‑VWD vs type 2B)
- **RIPA mixing studies** (including simplified assays) (othman2016platelettypevon pages 1-2, othman2011platelettypevonwillebrand pages 2-3)
- **Cryoprecipitate challenge** (useful but not infallible; false positives reported) (othman2011platelettypevonwillebrand pages 2-3)
- **Flow cytometry assays** of ristocetin-induced VWF binding (othman2016platelettypevon pages 1-2)

### 10.3 Genetic testing
**Definitive discrimination** relies on genetics:
- GP1BA mutation supports PT‑VWD; VWF A1 domain (often exon 28) mutation supports type 2B VWD. (othman2011platelettypevonwillebrand pages 2-3)
- 2011 review explicitly describes GP1BA sequencing as the “gold standard” definitive test. (othman12011platelettypevonwillebrand pages 3-4)

### 10.4 Differential diagnosis (selected)
- Type 2B von Willebrand disease (primary) (othman12011platelettypevonwillebrand pages 1-2)
- Immune thrombocytopenia (misdiagnosis risk in thrombocytopenic presentations) (seidizadeh2025globalprevalenceof pages 1-3)


## 11. Outcome / prognosis

### 11.1 Prognosis and complications
The retrieved corpus supports **generally mild-to-moderate bleeding** but does not provide quantitative mortality/survival or long-term disability measures. (othman2016platelettypevon pages 2-3)

### 11.2 Evidence gaps
Registry authors emphasize limited systematic data for special situations (e.g., pregnancy) and limited comprehensive longitudinal outcomes. (othman2016platelettypevon pages 3-3)


## 12. Treatment

### 12.1 Core management principle
Because PT‑VWD is driven by excessive platelet–VWF binding, therapies that raise circulating VWF can worsen thrombocytopenia, so treatment differs from type 2B VWD. (othman2011platelettypevonwillebrand pages 3-5, dorgalaleh2025precisionmedicinein pages 2-3)

### 12.2 Hemostatic therapies
- **Platelet transfusion / platelet concentrates**: described as **ideal/primary treatment** to secure hemostasis in bleeding situations. (othman2011platelettypevonwillebrand pages 3-5, dorgalaleh2025precisionmedicinein pages 2-3)
- **Desmopressin (DDAVP)**: advised to avoid or use cautiously; mechanistic evidence shows DDAVP-induced VWF increase caused a **marked platelet count drop** in mutant mice. (bury2019mechanismsofthrombocytopenia pages 1-5, othman2011platelettypevonwillebrand pages 3-5)
- **VWF/FVIII concentrates**: may worsen thrombocytopenia; if required, some authors suggest very low dosing to achieve hemostasis without a platelet drop; one target suggested is **VWF:RCo ~40–47 μ/dL**. (othman2011platelettypevonwillebrand pages 3-5)

### 12.3 Pregnancy/peripartum (real-world implementation)
A pregnancy case report describes multidisciplinary planning with platelet monitoring and peripartum platelet support (two units of platelets before delivery) and notes regional anesthesia contraindication in that case context. (grover2013pseudo(platelettype)von pages 1-2)

### 12.4 Clinical trials
A ClinicalTrials.gov query (PT‑VWD / pseudo‑VWD) returned a clinical trial record but **no clearly relevant interventional trial specific to PT‑VWD** in the retrieved results. (tool state; no trial context IDs were produced)

### 12.5 Suggested MAXO terms (informatic suggestions)
- Platelet transfusion (MAXO term suggestion) (grover2013pseudo(platelettype)von pages 1-2)
- Desmopressin administration (MAXO suggestion; contraindication/caution context) (othman2011platelettypevonwillebrand pages 3-5)
- VWF replacement therapy (MAXO suggestion; caution/low-dose context) (othman2011platelettypevonwillebrand pages 3-5)


## 13. Prevention
Primary prevention is not applicable for a Mendelian disorder; **secondary/tertiary prevention** centers on:
- avoiding platelet-affecting drugs when possible (aspirin) (othman12011platelettypevonwillebrand pages 1-2)
- accurate molecular diagnosis to avoid harmful treatments (e.g., DDAVP in PT‑VWD) (othman12011platelettypevonwillebrand pages 3-4)
- genetic counseling for autosomal dominant inheritance (50% transmission risk referenced in pregnancy case report) (grover2013pseudo(platelettype)von pages 1-2)


## 14. Other species / natural disease
No naturally occurring veterinary PT‑VWD analogs were identified in the retrieved corpus.


## 15. Model organisms and model systems

### 15.1 Mouse models
A transgenic model expressing **human GPIbα Gly233Val (G233V)** reproduces key PT‑VWD features (enhanced ristocetin-induced aggregation, prolonged bleeding time, splenomegaly and increased splenic megakaryocytes). (othman2011platelettypevonwillebrand pages 5-6)

### 15.2 Human megakaryocyte models
Patient-derived megakaryocytes (GP1BA Met239Val) demonstrate early VWF binding, abnormal proplatelet formation, and ectopic proplatelet release on collagen with defects in RhoA–MLC2 signaling and altered Lyn phosphorylation. (bury2019mechanismsofthrombocytopenia pages 1-5)

### 15.3 hiPSC/CRISPR models (2023)
A hiPSC model with engineered **GP1BA p.M255V** GoF mutation recapitulated macrothrombocytopenia-like platelet production defects and implicated reduced ERK1/2 activation and increased MLC2 phosphorylation; ROCK inhibition rescued phenotypes. (pawinwongchai2023studyofplatelet pages 1-6)

### 15.4 Model limitations
Species differences in GP1BA/VWF interaction are noted (mouse vs human sequence similarity ~70–75% in VWF-binding region), which may alter translatability. (othman2011platelettypevonwillebrand pages 3-5)


## Key quick-reference table
| Key concept / definition | Causative gene | Representative GP1BA gain-of-function variants (protein level) | Key distinguishing diagnostic lab features | Differential points vs type 2B VWD | Treatment implications | Citations |
|---|---|---|---|---|---|---|
| Rare autosomal dominant inherited platelet disorder (historically “pseudo-von Willebrand disease”) caused by platelet hyperresponsiveness with excessive GPIbα–VWF binding, producing a VWD-like phenotype with mucocutaneous bleeding and often thrombocytopenia. | **GP1BA** (encodes platelet glycoprotein Ibα, GPIbα) | Classic and recent variants reported across evidence include **p.Gly233Val**, **p.Gly233Ser**, **p.Met239Val** (older nomenclature may appear as p.Met255Val), **p.Trp246Leu**, **p.Gly249Val**, **p.Gly249Ser**, **p.Asp251Tyr**, **p.Met255Ile**, **p.Arg127Gln**, **p.Leu194Phe**, and **p.Thr436_Ala444del** / 27-bp deletion. | Hallmark is **enhanced RIPA at low-dose ristocetin** (commonly ~0.5 mg/mL; some centers 0.6–0.7 mg/mL), **selective loss of high-molecular-weight VWF multimers in plasma**, discordantly low platelet-dependent VWF function relative to antigen (e.g., low **VWF:RCo/VWF:Ag**, often **<0.6**), with normal/variable FVIII and intermittent thrombocytopenia or macrothrombocytopenia. | Phenotype overlaps strongly with type 2B VWD, but PT-VWD is a **platelet receptor defect** rather than a VWF defect. Discrimination relies on **RIPA mixing studies**, historically **cryoprecipitate challenge**, flow-cytometric VWF-binding assays, and especially **genetic testing**: **GP1BA** variant confirms PT-VWD, whereas **VWF** A1-domain variant supports type 2B VWD. | Management differs from VWD: **desmopressin (DDAVP)** or **VWF/FVIII concentrates** may worsen thrombocytopenia by increasing VWF available for mutant platelet binding; **platelet concentrates** are generally preferred for major bleeding/procedures. Pregnancy can worsen thrombocytopenia/bleeding as circulating VWF rises; multidisciplinary obstetric planning and platelet support may be needed. | (othman12011platelettypevonwillebrand pages 1-2, othman12011platelettypevonwillebrand pages 2-3, othman2011platelettypevonwillebrand pages 2-3, othman2011platelettypevonwillebrand pages 3-5, othman2016platelettypevon pages 1-2, bury2019mechanismsofthrombocytopenia pages 1-5, othman12011platelettypevonwillebrand pages 3-4, seidizadeh2025globalprevalenceof pages 3-4, monteiro2023anewcase pages 2-2, monteiro2023anewcase pages 1-2, othman2016platelettypevon pages 2-3) |


*Table: This table condenses the core disease concept, genetic basis, representative GP1BA variants, distinguishing diagnostic findings, differential diagnosis against type 2B VWD, and key management implications for platelet-type von Willebrand disease. It is useful as a quick-reference artifact for clinical and knowledge-base curation.*

## Visual evidence (variant table)
The ISTH SSC communication includes a **table of GP1BA variants and registered PT‑VWD cases** (Table 1), useful for curation of historical variant–case mappings. (othman2016platelettypevon media 05132cc9)


## Expert opinion and consensus (as supported in retrieved sources)
- PT‑VWD is “often misdiagnosed and underdiagnosed,” with clinically important misclassification as type 2B VWD; experts emphasize combining phenotypic assays (RIPA ± mixing) with **molecular confirmation** to guide therapy. (othman12011platelettypevonwillebrand pages 1-2, othman12011platelettypevonwillebrand pages 3-4)
- Registry authors emphasize that systematic data—especially in pregnancy and other “special situations”—remain limited and motivate international registry participation for evidence generation. (othman2016platelettypevon pages 3-3)


## URLs and publication dates (key sources)
- Othman M. *Seminars in Thrombosis & Hemostasis* (Jul 2011). https://doi.org/10.1055/s-0031-1281030 (othman12011platelettypevonwillebrand pages 1-2)
- Othman M. *Blood Reviews* (Jul 2011). https://doi.org/10.1016/j.blre.2011.03.003 (othman2011platelettypevonwillebrand pages 5-6)
- Othman M et al. ISTH SSC communication. *J Thromb Haemost* (Feb 2016). https://doi.org/10.1111/jth.13204 (othman2016platelettypevon pages 1-2)
- Bury L et al. *Haematologica* (Jan 2019). https://doi.org/10.3324/haematol.2018.200378 (bury2019mechanismsofthrombocytopenia pages 1-5)
- Monteiro C et al. *Br J Haematol* (Aug 2023). https://doi.org/10.1111/bjh.19025 (monteiro2023anewcase pages 1-2)
- Johnsen J. *von Willebrand disease* (2024; journal metadata unavailable in retrieved record). (johnsen2024vonwillebranddisease pages 5-7)
- Seidizadeh O et al. *Res Pract Thromb Haemost* (Jan 2025). https://doi.org/10.1016/j.rpth.2025.102682 (seidizadeh2025globalprevalenceof pages 1-3)


## Notes on missing items relative to template
- Formal ontology/registry identifiers (OMIM/Orphanet/MONDO/MeSH/ICD) were not extractable from the retrieved papers and should be completed by direct database lookups.
- Quantitative phenotype frequencies (percentages of specific bleeding manifestations) and validated QoL instruments (SF‑36/EQ‑5D) were not found in the retrieved corpus.
- PT‑VWD-specific clinical practice guidelines from 2023–2024 were not retrieved; most guidance is from expert reviews/SSC communications plus mechanistic data and case reports.


References

1. (othman12011platelettypevonwillebrand pages 1-2): Maha Othman1. Platelet-type von willebrand disease: a rare, often misdiagnosed and underdiagnosed bleeding disorder. Semin Thromb Hemost, 37:464-469, Jul 2011. URL: https://doi.org/10.1055/s-0031-1281030, doi:10.1055/s-0031-1281030. This article has 66 citations.

2. (othman2011platelettypevonwillebrand pages 3-5): Maha Othman. Platelet-type von willebrand disease: three decades in the life of a rare bleeding disorder. Blood reviews, 25 4:147-53, Jul 2011. URL: https://doi.org/10.1016/j.blre.2011.03.003, doi:10.1016/j.blre.2011.03.003. This article has 60 citations and is from a peer-reviewed journal.

3. (monteiro2023anewcase pages 1-2): Catarina Monteiro, Ana Gonçalves, Mónica Pereira, Catarina Lau, Sara Morais, and Rosário Santos. A new case of platelet‐type von willebrand disease supports the recent findings of gain‐of‐function gp1ba variants outside the c‐terminal disulphide loop enhances affinity for von willebrand factor. British Journal of Haematology, 203:673-677, Aug 2023. URL: https://doi.org/10.1111/bjh.19025, doi:10.1111/bjh.19025. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (bury2019mechanismsofthrombocytopenia pages 1-5): Loredana Bury, Alessandro Malara, Stefania Momi, Eleonora Petito, Alessandra Balduini, and Paolo Gresele. Mechanisms of thrombocytopenia in platelet-type von willebrand disease. Haematologica, 104:1473-1481, Jan 2019. URL: https://doi.org/10.3324/haematol.2018.200378, doi:10.3324/haematol.2018.200378. This article has 60 citations.

5. (othman2011platelettypevonwillebrand pages 5-6): Maha Othman. Platelet-type von willebrand disease: three decades in the life of a rare bleeding disorder. Blood reviews, 25 4:147-53, Jul 2011. URL: https://doi.org/10.1016/j.blre.2011.03.003, doi:10.1016/j.blre.2011.03.003. This article has 60 citations and is from a peer-reviewed journal.

6. (othman2016platelettypevon pages 2-3): Maha Othman, Maha Othman, Harmanpreet Kaur, E. J. Favaloro, D. Lillicrap, J. D. Paola, Paul J. Harrison, and P. Gresele. Platelet type von willebrand disease and registry report: communication from the ssc of the isth. Journal of Thrombosis and Haemostasis, 14:4-411, Feb 2016. URL: https://doi.org/10.1111/jth.13204, doi:10.1111/jth.13204. This article has 34 citations and is from a peer-reviewed journal.

7. (othman12011platelettypevonwillebrand pages 2-3): Maha Othman1. Platelet-type von willebrand disease: a rare, often misdiagnosed and underdiagnosed bleeding disorder. Semin Thromb Hemost, 37:464-469, Jul 2011. URL: https://doi.org/10.1055/s-0031-1281030, doi:10.1055/s-0031-1281030. This article has 66 citations.

8. (othman2011platelettypevonwillebrand pages 2-3): Maha Othman. Platelet-type von willebrand disease: three decades in the life of a rare bleeding disorder. Blood reviews, 25 4:147-53, Jul 2011. URL: https://doi.org/10.1016/j.blre.2011.03.003, doi:10.1016/j.blre.2011.03.003. This article has 60 citations and is from a peer-reviewed journal.

9. (othman12011platelettypevonwillebrand pages 3-4): Maha Othman1. Platelet-type von willebrand disease: a rare, often misdiagnosed and underdiagnosed bleeding disorder. Semin Thromb Hemost, 37:464-469, Jul 2011. URL: https://doi.org/10.1055/s-0031-1281030, doi:10.1055/s-0031-1281030. This article has 66 citations.

10. (monteiro2023anewcase pages 2-2): Catarina Monteiro, Ana Gonçalves, Mónica Pereira, Catarina Lau, Sara Morais, and Rosário Santos. A new case of platelet‐type von willebrand disease supports the recent findings of gain‐of‐function gp1ba variants outside the c‐terminal disulphide loop enhances affinity for von willebrand factor. British Journal of Haematology, 203:673-677, Aug 2023. URL: https://doi.org/10.1111/bjh.19025, doi:10.1111/bjh.19025. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (seidizadeh2025globalprevalenceof pages 3-4): Omid Seidizadeh, Andrea Cairo, Maha Othman, and Flora Peyvandi. Global prevalence of platelet-type von willebrand disease. Research and Practice in Thrombosis and Haemostasis, 9:102682, Jan 2025. URL: https://doi.org/10.1016/j.rpth.2025.102682, doi:10.1016/j.rpth.2025.102682. This article has 12 citations and is from a peer-reviewed journal.

12. (seidizadeh2025globalprevalenceof pages 1-3): Omid Seidizadeh, Andrea Cairo, Maha Othman, and Flora Peyvandi. Global prevalence of platelet-type von willebrand disease. Research and Practice in Thrombosis and Haemostasis, 9:102682, Jan 2025. URL: https://doi.org/10.1016/j.rpth.2025.102682, doi:10.1016/j.rpth.2025.102682. This article has 12 citations and is from a peer-reviewed journal.

13. (othman2016platelettypevon pages 2-2): Maha Othman, Maha Othman, Harmanpreet Kaur, E. J. Favaloro, D. Lillicrap, J. D. Paola, Paul J. Harrison, and P. Gresele. Platelet type von willebrand disease and registry report: communication from the ssc of the isth. Journal of Thrombosis and Haemostasis, 14:4-411, Feb 2016. URL: https://doi.org/10.1111/jth.13204, doi:10.1111/jth.13204. This article has 34 citations and is from a peer-reviewed journal.

14. (othman2016platelettypevon pages 1-2): Maha Othman, Maha Othman, Harmanpreet Kaur, E. J. Favaloro, D. Lillicrap, J. D. Paola, Paul J. Harrison, and P. Gresele. Platelet type von willebrand disease and registry report: communication from the ssc of the isth. Journal of Thrombosis and Haemostasis, 14:4-411, Feb 2016. URL: https://doi.org/10.1111/jth.13204, doi:10.1111/jth.13204. This article has 34 citations and is from a peer-reviewed journal.

15. (othman2016platelettypevon pages 3-3): Maha Othman, Maha Othman, Harmanpreet Kaur, E. J. Favaloro, D. Lillicrap, J. D. Paola, Paul J. Harrison, and P. Gresele. Platelet type von willebrand disease and registry report: communication from the ssc of the isth. Journal of Thrombosis and Haemostasis, 14:4-411, Feb 2016. URL: https://doi.org/10.1111/jth.13204, doi:10.1111/jth.13204. This article has 34 citations and is from a peer-reviewed journal.

16. (dorgalaleh2025precisionmedicinein pages 2-3): Akbar Dorgalaleh and Maha Othman. Precision medicine in rare bleeding disorders. Seminars in Thrombosis and Hemostasis, 51:099-102, Dec 2025. URL: https://doi.org/10.1055/s-0044-1800833, doi:10.1055/s-0044-1800833. This article has 2 citations and is from a peer-reviewed journal.

17. (grover2013pseudo(platelettype)von pages 1-2): Neetu Grover, Vincent Boama, and Munazzah Rifat Chou. Pseudo (platelet-type) von willebrand disease in pregnancy: a case report. BMC Pregnancy and Childbirth, 13:16-16, Jan 2013. URL: https://doi.org/10.1186/1471-2393-13-16, doi:10.1186/1471-2393-13-16. This article has 24 citations and is from a peer-reviewed journal.

18. (pawinwongchai2023studyofplatelet pages 1-6): Jaturawat Pawinwongchai. Study of platelet production from megakaryocyte by using induced pluripotent stem cell. ArXiv, 2023. URL: https://doi.org/10.58837/chula.the.2020.28, doi:10.58837/chula.the.2020.28. This article has 0 citations.

19. (othman2016platelettypevon media 05132cc9): Maha Othman, Maha Othman, Harmanpreet Kaur, E. J. Favaloro, D. Lillicrap, J. D. Paola, Paul J. Harrison, and P. Gresele. Platelet type von willebrand disease and registry report: communication from the ssc of the isth. Journal of Thrombosis and Haemostasis, 14:4-411, Feb 2016. URL: https://doi.org/10.1111/jth.13204, doi:10.1111/jth.13204. This article has 34 citations and is from a peer-reviewed journal.

20. (johnsen2024vonwillebranddisease pages 5-7): J Johnsen. Von willebrand disease. Unknown journal, 2024.