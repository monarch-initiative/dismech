---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T18:26:05.272875'
end_time: '2026-05-08T18:34:41.478389'
duration_seconds: 516.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Green Tobacco Sickness
  mondo_id: ''
  category: Environmental
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
- **Disease Name:** Green Tobacco Sickness
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Green Tobacco Sickness** covering all of the
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
- **Disease Name:** Green Tobacco Sickness
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Green Tobacco Sickness** covering all of the
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


# Green Tobacco Sickness (GTS) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Green Tobacco Sickness (GTS)
- **Category:** Environmental / occupational intoxication
- **MONDO ID:** Not identified from the retrieved sources in this run (gap).

---

## 1. Disease information

### Overview (current understanding)
Green tobacco sickness is an **acute occupational nicotine intoxication** occurring primarily during **handling/harvest of green (uncured) tobacco**, especially when leaves/clothing are wet, leading to **transdermal nicotine absorption** and systemic cholinergic/toxic effects. It is generally **self-limited** (often resolving within ~1–2 days), but may require medical care for dehydration or physiologic instability. (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3)

### Synonyms / alternative names
- “Green tobacco sickness” (most common)
- “Green tobacco disease” / “doença da folha verde do tabaco” (Portuguese-language literature term for the same syndrome) (oliveira2010firstreportedoutbreak pages 1-2)

### Key identifiers
- **ICD-10/ICD-11, MeSH, MONDO:** Not recoverable from the full-text evidence obtained in this run (gap).

### Evidence source type
Evidence is derived primarily from:
- **Human outbreak investigations and case-control studies** (e.g., Brazil outbreak) (oliveira2010firstreportedoutbreak pages 1-2)
- **Occupational cohort/survey studies** among farmworkers/harvesters (quandt2000migrantfarmworkersand pages 1-2, fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3)
- **Narrative/expert reviews** synthesizing multiple studies (mcmahon2019greentobaccosickness pages 1-6, mcmahon2019greentobaccosickness pages 14-18)

---

## 2. Etiology

### Disease causal factors (environmental/occupational)
**Primary cause:** systemic nicotine toxicity from **transdermal absorption** of nicotine during contact with **wet tobacco leaves** (and wet clothing contaminated with leaf nicotine). (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3)

**Key mechanistic note:** nicotine can diffuse through the stratum corneum into the bloodstream; absorption increases with skin moisture and damaged skin. (quandt2000migrantfarmworkersand pages 1-2)

### Risk factors
Across studies and reviews, risk is increased by:
- **Harvesting/handling wet leaves** and **wet clothing/shoes** (fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3)
- **Heat/humidity** (increasing sweating and dermal absorption; also reduces PPE tolerance) (mcmahon2019greentobaccosickness pages 1-6, ziska2024recentandprojected pages 5-6)
- **High-intensity contact tasks** (e.g., harvesting wet leaves; barn tasks; transporting bales; bundling/tying) (fassa2018urinarycotininein pages 1-3)
- **Non-smoking status** (observed in Brazil outbreak; also seen in other epidemiologic work) (oliveira2010firstreportedoutbreak pages 1-2, fassa2018urinarycotininein pages 1-3)
- **Younger age** and working in wet conditions (Kentucky outbreak) (ballard1995greentobaccosickness pages 1-3)

#### Genetic risk factors / gene–environment interactions
- A genetic-polymorphism study exists in the retrieved corpus but genotype-specific associations were not extractable from the evidence snippets available in this run; overall, GTS is best supported as an exposure-driven occupational intoxication rather than a Mendelian disease in the retrieved evidence. (mcmahon2019greentobaccosickness pages 1-6)

### Protective factors
- **Avoiding work when plants are wet** and reducing skin contact with leaves. (trapecardoso2005cotininelevelsand pages 1-3, ballard1995greentobaccosickness pages 1-3)
- **Personal protective equipment (PPE)** (water-resistant/chemical-resistant gloves, aprons, rain suits/boots) and prompt changing of wet clothing are repeatedly recommended in occupational health contexts. (ravi2024qualitativestudyto pages 1-2)
- **Nicotine tolerance from prior nicotine use (e.g., smoking)** is sometimes described as potentially protective but is inconsistent and should not be relied upon. (mcmahon2019greentobaccosickness pages 1-6, mcmahon2019greentobaccosickness pages 14-18)

---

## 3. Phenotypes

### Core clinical phenotype (symptoms/signs)
Common symptoms across outbreak reports and surveys include:
- nausea, vomiting
- dizziness, headache
- weakness/asthenia
- pallor and sweating; sometimes hypersalivation

Brazil outbreak report (human outbreak investigation) explicitly lists: **“dizziness, weakness, vomit, nausea and headache”** as the main observed signs/symptoms. (oliveira2010firstreportedoutbreak pages 1-2)

A 2024 qualitative study (women tobacco laborers, India) summarizes reported symptoms including: **“nausea, dizziness, increased salivation, poor appetite, insomnia, and increased sweating.”** (ravi2024qualitativestudyto pages 2-3)

### Additional/severe manifestations
Severe cases can involve dehydration and physiologic instability; earlier U.S. outbreak work reported hospitalizations and ICU admissions (see epidemiology section). (ballard1995greentobaccosickness pages 1-3)

### Temporal pattern
Symptoms typically occur **several hours after exposure**, often later the same day, and resolve in **~1–2 days**; one expert review reports onset often around **~10 hours** after exposure and mean duration **~2.4 days**. (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2)

### Suggested HPO terms (examples)
- **Nausea** (HP:0002018)
- **Vomiting** (HP:0002013)
- **Dizziness** (HP:0002321)
- **Headache** (HP:0002315)
- **Asthenia / Weakness** (HP:0025406)
- **Hyperhidrosis** (HP:0000975)
- **Sialorrhea** (HP:0002307)
- **Abdominal pain** (HP:0002027)
- **Diarrhea** (HP:0002014)
- **Dehydration** (HP:0001944)

(oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 2-3)

### Quality-of-life impact
Workforce studies emphasize lost work time and functional impairment during symptomatic episodes; among migrant farmworkers, most self-managed but some sought care and missed work. (quandt2000migrantfarmworkersand pages 1-2)

---

## 4. Genetic / molecular information

### Causal genes / pathogenic variants
- **Not applicable as a primary disease model** based on retrieved evidence. GTS is an **exposure-mediated intoxication syndrome**.

### Molecular entities (CHEBI)
- **Nicotine** (CHEBI:18723) — principal toxicant in this syndrome (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3)
- **Cotinine** (CHEBI:39941) — primary nicotine metabolite used as exposure biomarker (oliveira2010firstreportedoutbreak pages 1-2, fassa2018urinarycotininein pages 1-3)

---

## 5. Environmental information

### Environmental/occupational exposure
- Direct exposure to **green tobacco leaves**, especially **wet leaves**, is the key environmental driver; moisture increases dermal uptake. (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3)

### Lifestyle factors
- Smoking status is repeatedly associated with differing risk patterns, plausibly via tolerance; however, it is not a recommended preventive strategy. (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6)

### Infectious agents
- Not applicable.

---

## 6. Mechanism / pathophysiology

### Causal chain (trigger → manifestations)
1. **Trigger:** harvesting/handling wet tobacco leaves; sweat/wet clothing increases dermal transfer. (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3)
2. **Exposure:** nicotine crosses the **stratum corneum** into systemic circulation; absorption varies by body site and increases with moisture/skin damage. (quandt2000migrantfarmworkersand pages 1-2)
3. **Downstream physiology:** systemic nicotine affects nicotinic acetylcholine receptor pathways and autonomic function, producing GI symptoms (nausea/vomiting/abdominal symptoms), neurologic symptoms (headache/dizziness/weakness), and sometimes cardiovascular instability. (mcmahon2019greentobaccosickness pages 1-6, ballard1995greentobaccosickness pages 1-3)

### Biomarker kinetics / interpretation
- **Cotinine** (urine/saliva/plasma) is widely used to assess nicotine exposure, but symptom–biomarker correlation can be imperfect due to **timing** and **tolerance**.
- In a large Brazilian study with urine sampling, overall urinary cotinine means did not differ between symptomatic and asymptomatic groups, but among non-smokers, recent picking was associated with higher cotinine and there was symptom-day–dependent decline patterns. (fassa2018urinarycotininein pages 1-3)

### Suggested GO terms (biological processes; high-level)
- Response to nicotine (GO concept; exact GO ID not validated in this run)
- Cholinergic signaling
- Xenobiotic transport and metabolism

### Suggested CL (cell types; high-level)
- **Keratinocyte** (epidermal barrier/absorption interface)

---

## 7. Anatomical structures affected

### Primary interface (route of entry)
- **Skin** (UBERON concept: skin; epidermis/stratum corneum). (quandt2000migrantfarmworkersand pages 1-2)

### Systems affected (clinical manifestations)
- **Gastrointestinal system** (nausea/vomiting/abdominal symptoms) (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6)
- **Nervous system** (headache, dizziness, weakness) (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2)
- **Cardiovascular/autonomic** (occasionally blood pressure/heart-rate instability in severe cases) (ballard1995greentobaccosickness pages 1-3)

---

## 8. Temporal development

- **Onset:** acute/subacute after work exposure, often later the same day or evening (quandt2000migrantfarmworkersand pages 1-2)
- **Course/duration:** self-limited, often ~1–2 days; review estimate mean ~2.4 days (mcmahon2019greentobaccosickness pages 1-6, ballard1995greentobaccosickness pages 1-3)
- **Pattern:** episodic, linked to harvesting periods and wet/heat conditions (ballard1995greentobaccosickness pages 1-3, ziska2024recentandprojected pages 5-6)

---

## 9. Inheritance and population

### Inheritance
- Not a genetic inheritance condition in the primary disease model; exposure-driven.

### Epidemiology (recent data prioritized when available)
Quantitative estimates vary by population, design, and tobacco type:
- **Kentucky, USA (1992–1993 outbreak):** crude incidence **10.0 per 1,000** tobacco workers (1992) and **14.0 per 1,000** (1993); 12 hospitalizations and 2 ICU admissions reported in 1992. (ballard1995greentobaccosickness pages 1-3)
- **Southern Brazil (cross-sectional, 2014):** previous-month prevalence **6.6% (men)** and **11.9% (women)**. (fassa2018urinarycotininein pages 1-3)
- **Northeastern Brazil (outbreak investigation, 2010):** **107 case-patients** identified, using urinary cotinine >10 ng/mL in the case definition; cases had higher median urinary cotinine than controls (p<0.05). (oliveira2010firstreportedoutbreak pages 1-2)
- **North Carolina migrant/seasonal farmworkers (survey):** **41%** reported GTS at least once during a summer season. (quandt2000migrantfarmworkersand pages 1-2)
- **Global prevalence ranges (review-level):** estimates across settings commonly range roughly **8.2%–47%** (review synthesis). (mcmahon2019greentobaccosickness pages 1-6, ravi2024qualitativestudyto pages 1-2)

### Demographics / geography
- Occurs in multiple major tobacco-growing regions (Americas, Asia).
- Vulnerable groups include migrant/seasonal laborers and children/younger workers (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3), and women workers with PPE access inequities (ravi2024qualitativestudyto pages 1-2).

---

## 10. Diagnostics

### Clinical diagnosis (typical approach)
A practical clinical approach combines:
1) recent occupational exposure to green tobacco (especially wet leaves/clothing),
2) compatible symptom cluster,
3) supportive biomarker evidence (cotinine),
while considering key differentials such as pesticide poisoning and heat illness. (oliveira2010firstreportedoutbreak pages 1-2, ballard1995greentobaccosickness pages 1-3)

### Laboratory tests / biomarkers
- **Cotinine** measurement in **urine**, **saliva**, or **blood/plasma** is the most common biomarker approach. (oliveira2010firstreportedoutbreak pages 1-2, trapecardoso2005cotininelevelsand pages 1-3, fassa2018urinarycotininein pages 1-3)
- In the Brazil outbreak investigation, a case-patient definition used **urinary cotinine >10 ng/mL** (assayed by HPLC) plus clinical diagnosis of acute intoxication during the period. (oliveira2010firstreportedoutbreak pages 1-2)

### Differential diagnosis
- **Organophosphate/carbamate pesticide poisoning** (symptom overlap)
- **Heat illness/heat exhaustion**
- **Acute gastroenteritis or other intoxications**

Diagnostic confusion is explicitly raised in occupational studies. (ballard1995greentobaccosickness pages 1-3)

### Genetic testing
- Not indicated as standard-of-care; exposure-mediated condition.

---

## 11. Outcome / prognosis

- Generally **self-limited** with recovery in ~1–2 days (ballard1995greentobaccosickness pages 1-3).
- Morbidity can be significant (dehydration, medical visits, lost work); severe outbreaks included hospitalizations and ICU care. (ballard1995greentobaccosickness pages 1-3)

---

## 12. Treatment

### Supportive management (current practice)
- **Immediate removal from exposure**, rest, symptomatic treatment.
- **Rehydration** (oral/IV) and **antiemetic** management as needed.
- Medical evaluation/admission for severe dehydration or instability. (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3)

### Experimental / proposed pharmacologic strategies (not standard)
An expert review proposes evaluating nicotine-receptor–targeting agents (e.g., mecamylamine, varenicline, cytisine) and nicotine immunization strategies as research tools/potential therapeutics; these are not established standard care for GTS. (mcmahon2019greentobaccosickness pages 14-18)

### Suggested MAXO terms (examples)
- Supportive care
- Fluid replacement therapy
- Antiemetic therapy
- Occupational exposure cessation

---

## 13. Prevention

### Primary prevention (most important)
- Avoid harvesting/handling when leaves are **wet** where feasible.
- Use **PPE** (water-resistant/chemical-resistant gloves; protective outerwear; boots) and change out of wet clothing quickly.
- Worker education and occupational health training. (ravi2024qualitativestudyto pages 1-2)

### System-level implementations
- Training clinicians to recognize GTS and distinguish it from pesticide poisoning.
- Occupational surveillance (e.g., poison-center detection reported historically in the U.S. context). (ballard1995greentobaccosickness pages 1-3)

---

## 14. Other species / natural disease
No veterinary/animal natural disease analogs were identified in the retrieved sources; GTS is primarily characterized as a **human occupational intoxication**.

---

## 15. Model organisms
No dedicated model organism systems for “green tobacco sickness” as a distinct disease entity were identified in the retrieved sources.

---

## Recent developments and latest research (2023–2024 prioritized)

### Climate change as an emerging risk multiplier (2024)
A 2024 paper in *Communications Medicine* analyzed historical and projected harvest-season climate patterns across major tobacco-growing regions (Brazil, China, India, North Carolina USA) using CMIP6 scenarios and estimated that higher temperatures could increase dermal nicotine absorption. Projected nicotine-uptake increases (proxy-based) were on the order of **~28.7% to ~49.6%** under moderate-to-high emissions scenarios, depending on location. (ziska2024recentandprojected pages 5-6)

**Interpretation:** While based on proxy modeling (therapeutic nicotine patch temperature relationships), the study reframes GTS as a climate-sensitive occupational illness and provides quantitative scenario estimates relevant for long-term planning and worker protections. (ziska2024recentandprojected pages 2-5, ziska2024recentandprojected pages 5-6)

### Women’s occupational health and reproductive context (2024)
A 2024 qualitative study of women tobacco farm laborers in Mysore District, India reported GTS symptoms (e.g., headaches, gastric complaints, weakness) and emphasized barriers to PPE access/use and occupational health education, particularly around menstruation, pregnancy, and the postnatal period. (ravi2024qualitativestudyto pages 16-17, ravi2024qualitativestudyto pages 1-2)

---

## Summary artifact for knowledge base population
The following table compiles the most KB-ready facts (definition/synonyms, epidemiology, risks/protection, phenotypes with HPO, diagnostics, management/prevention with MAXO, and chemicals with CHEBI IDs):

| Domain | Item | Details | Ontology suggestions | Evidence |
|---|---|---|---|---|
| Definition / classification | Green Tobacco Sickness (GTS) | Occupational/environmental illness; acute nicotine poisoning caused primarily by dermal absorption of nicotine from wet green tobacco leaves; typically self-limited over 1–2 days, though severe dehydration/hospitalization can occur (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) | MONDO: not clearly established in retrieved sources; MeSH/ICD: not confirmed in retrieved sources | (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) |
| Synonyms | Alternative names | Green tobacco disease; tobacco harvesters’ acute nicotine poisoning; nicotine poisoning from wet tobacco leaves; Portuguese literature uses “doença da folha verde do tabaco” (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6) | Related concept: nicotine poisoning | (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6) |
| Epidemiology | Prevalence range across studies/reviews | Literature review reported prevalence ranging from 6.6% to 56.9% across included studies; another review cited global prevalence 8.2%–47% (mcmahon2019greentobaccosickness pages 1-6, ravi2024qualitativestudyto pages 1-2) | Not applicable | (mcmahon2019greentobaccosickness pages 1-6, ravi2024qualitativestudyto pages 1-2) |
| Epidemiology | Southern Brazil, 2014 | Previous-month prevalence: 6.6% in men and 11.9% in women among tobacco farmers (fassa2018urinarycotininein pages 1-3) | Not applicable | (fassa2018urinarycotininein pages 1-3) |
| Epidemiology | Northeastern Brazil, 2018 study population | Total prevalence 56.9%; women 71.7%, men 35.3% (oliveira2010firstreportedoutbreak pages 1-2) | Not applicable | (oliveira2010firstreportedoutbreak pages 1-2) |
| Epidemiology | Kentucky, USA, 1992–1993 | Incidence 10.0 per 1,000 tobacco workers in 1992 and 14.0 per 1,000 in 1993; 12 hospitalizations and 2 ICU admissions in 1992 outbreak (ballard1995greentobaccosickness pages 1-3) | Not applicable | (ballard1995greentobaccosickness pages 1-3) |
| Epidemiology | North Carolina migrant/seasonal farmworkers | 41% reported GTS at least once during one summer season (quandt2000migrantfarmworkersand pages 1-2) | Not applicable | (quandt2000migrantfarmworkersand pages 1-2) |
| Epidemiology | Brazil outbreak count | 107 laboratory-supported case-patients identified in outbreak investigation (oliveira2010firstreportedoutbreak pages 1-2) | Not applicable | (oliveira2010firstreportedoutbreak pages 1-2) |
| Risk factors | Exposure-related | Harvesting wet leaves; direct skin contact with tobacco; wet clothing/shoes; heat/humidity; physical exertion; leaf bundling/barn tasks/transporting bales; younger age in some studies (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3) | Exposure to nicotine (CHEBI: nicotine) | (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3) |
| Risk factors | Individual / contextual | Non-smoker status in several studies; male sex in some outbreaks; female sex in some prevalence studies; dermatosis/skin damage; long work history; abnormal BMI; concomitant pesticide contact can complicate risk/recognition (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2, fassa2018urinarycotininein pages 1-3) | CL/GO not specific; skin barrier compromise relevant | (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2, fassa2018urinarycotininein pages 1-3) |
| Protective factors | Behavioral / occupational | Avoiding harvest when leaves are wet; reducing skin contact; prompt change from wet clothes; PPE use (water-resistant clothing, gloves, boots, aprons/rain suits); mechanization proposed as exposure-reduction strategy (trapecardoso2005cotininelevelsand pages 1-3, fassa2018urinarycotininein pages 1-3, ravi2024qualitativestudyto pages 1-2) | MAXO: personal protective equipment use; exposure avoidance; health education | (trapecardoso2005cotininelevelsand pages 1-3, fassa2018urinarycotininein pages 1-3, ravi2024qualitativestudyto pages 1-2) |
| Protective factors | Biological / tolerance | Prior nicotine exposure from smoking or other nicotine use may be partially protective via tolerance in some reports, but protection is inconsistent and not reliable (mcmahon2019greentobaccosickness pages 1-6, mcmahon2019greentobaccosickness pages 14-18) | Not applicable | (mcmahon2019greentobaccosickness pages 1-6, mcmahon2019greentobaccosickness pages 14-18) |
| Clinical features | Core symptom cluster | Nausea, vomiting, dizziness, headache, weakness, pallor, sweating/hypersalivation; often begins several hours after exposure and may peak later the same day/evening (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) | HPO: Nausea HP:0002018; Vomiting HP:0002013; Dizziness HP:0002321; Headache HP:0002315; Asthenia/Weakness HP:0025406; Pallor HP:0000980; Hyperhidrosis HP:0000975; Sialorrhea HP:0002307 | (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) |
| Clinical features | Additional manifestations | Abdominal cramps/pain, diarrhea, chills, poor appetite, insomnia, labored respiration; severe cases may involve dehydration, blood pressure/heart-rate instability, seizures, ICU care (trapecardoso2005cotininelevelsand pages 1-3, mcmahon2019greentobaccosickness pages 1-6, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 2-3) | HPO: Abdominal pain HP:0002027; Diarrhea HP:0002014; Chills HP:0025143; Decreased appetite HP:0004396; Insomnia HP:0100785; Dyspnea HP:0002094; Dehydration HP:0001944; Seizure HP:0001250 | (trapecardoso2005cotininelevelsand pages 1-3, mcmahon2019greentobaccosickness pages 1-6, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 2-3) |
| Temporal development | Onset / course | Acute onset after harvest exposure; onset often ~10 hours after exposure; self-limited, mean duration about 2.4 days, usually recovery within 1–2 days (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) | HPO: Acute episode; recurrent/episodic occupational exposure pattern | (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) |
| Diagnostics | Clinical recognition | No universally standardized diagnostic criteria in retrieved sources; common approach combines recent tobacco harvest exposure + compatible symptoms + nicotine/cotinine biomarker evidence, while excluding pesticide poisoning and heat illness (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) | MAXO not applicable | (oliveira2010firstreportedoutbreak pages 1-2, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) |
| Diagnostics / biomarkers | Cotinine | Cotinine is the main nicotine metabolite and widely used biomarker of nicotine exposure; useful in urine, saliva, blood/plasma, but symptom severity does not perfectly track cotinine because tolerance and timing matter (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6, fassa2018urinarycotininein pages 1-3) | CHEBI: cotinine | (oliveira2010firstreportedoutbreak pages 1-2, mcmahon2019greentobaccosickness pages 1-6, fassa2018urinarycotininein pages 1-3) |
| Diagnostics / biomarkers | Sample types and thresholds | Urine: outbreak case definition used urinary cotinine >10 ng/mL; salivary cotinine used in shade tobacco workers; plasma/blood cotinine also studied; urinary cotinine higher soon after symptom onset and declines over days (oliveira2010firstreportedoutbreak pages 1-2, trapecardoso2005cotininelevelsand pages 1-3, fassa2018urinarycotininein pages 1-3) | LOINC not established from retrieved sources | (oliveira2010firstreportedoutbreak pages 1-2, trapecardoso2005cotininelevelsand pages 1-3, fassa2018urinarycotininein pages 1-3) |
| Differential diagnosis | Key rule-outs | Organophosphate/carbamate or other pesticide poisoning, heat illness/heat exhaustion, dehydration, viral gastroenteritis, other acute intoxications (fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 2-3) | Not applicable | (fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 2-3) |
| Management | Acute treatment | Primarily supportive care: removal from exposure, rest, oral/IV rehydration, antiemetics/symptom management, medical evaluation for severe dehydration or cardiovascular instability; evidence base for specific pharmacotherapy remains limited (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) | MAXO: supportive care; fluid replacement; antiemetic therapy; hospital admission when severe | (quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) |
| Management | Experimental / proposed pharmacology | Review proposed studying nicotinic receptor antagonists/partial agonists such as mecamylamine, varenicline, cytisine, and nicotine vaccines, but these are not established standard care for GTS (mcmahon2019greentobaccosickness pages 14-18) | MAXO: investigational drug therapy | (mcmahon2019greentobaccosickness pages 14-18) |
| Prevention | Worker-level prevention | Wear chemical-/water-resistant gloves and clothing, boots, aprons/rain suits; avoid working with wet leaves when possible; change wet clothes quickly; reduce duration/intensity of contact; worker education/first-aid knowledge improves preparedness (trapecardoso2005cotininelevelsand pages 1-3, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 1-2) | MAXO: personal protective equipment use; occupational health education; behavior modification | (trapecardoso2005cotininelevelsand pages 1-3, ballard1995greentobaccosickness pages 1-3, ravi2024qualitativestudyto pages 1-2) |
| Prevention | System / policy / implementation | Train clinicians to distinguish GTS from pesticide poisoning; improve occupational surveillance; expand PPE access and adoption; community campaigns and educational videos increased farmer first-aid knowledge in Indonesia; mechanization suggested where feasible (fassa2018urinarycotininein pages 1-3, ravi2024qualitativestudyto pages 1-2) | MAXO: clinician training; surveillance; preventive counseling; mechanized harvesting | (fassa2018urinarycotininein pages 1-3, ravi2024qualitativestudyto pages 1-2) |
| Recent developments (2023–2024) | Climate change and GTS risk | 2024 analysis projected higher harvest-season temperatures could increase estimated nicotine dermal absorption by ~28.7%–49.6% under moderate/high emissions scenarios across Brazil, China, India, and North Carolina; rainfall and heat may amplify GTS risk (ziska2024recentandprojected pages 2-5, ziska2024recentandprojected pages 5-6) | Environmental exposure context | (ziska2024recentandprojected pages 2-5, ziska2024recentandprojected pages 5-6) |
| Recent developments (2024) | Women’s occupational health | 2024 qualitative study in Mysore, India documented GTS symptoms among women laborers, especially around menstruation/pregnancy/postnatal periods, and highlighted poor awareness, unequal PPE access, and reproductive-health concerns (ravi2024qualitativestudyto pages 16-17, ravi2024qualitativestudyto pages 2-3, ravi2024qualitativestudyto pages 1-2) | HPO terms above; MAXO: maternal occupational health support, PPE provision, health education | (ravi2024qualitativestudyto pages 16-17, ravi2024qualitativestudyto pages 2-3, ravi2024qualitativestudyto pages 1-2) |
| Key chemicals | Nicotine | Principal tobacco alkaloid causing toxicity after dermal absorption from wet leaves; water soluble and readily absorbed through skin (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) | CHEBI: nicotine (CHEBI:18723) | (mcmahon2019greentobaccosickness pages 1-6, quandt2000migrantfarmworkersand pages 1-2, ballard1995greentobaccosickness pages 1-3) |
| Key chemicals | Cotinine | Major metabolite of nicotine used as biomarker in urine, saliva, blood/plasma for exposure assessment (oliveira2010firstreportedoutbreak pages 1-2, fassa2018urinarycotininein pages 1-3) | CHEBI: cotinine (CHEBI:39941) | (oliveira2010firstreportedoutbreak pages 1-2, fassa2018urinarycotininein pages 1-3) |


*Table: This table compiles the core structured facts needed for a Green Tobacco Sickness knowledge base entry, including definition, epidemiology, risk/protective factors, phenotypes, diagnostics, treatment/prevention, and ontology term suggestions. It emphasizes evidence-backed details and recent 2024 developments relevant to occupational and environmental health.*

---

## Key evidence gaps (for curation)
- **ICD-10/ICD-11, MeSH, MONDO identifiers** were not retrievable from the collected sources in this run.
- **Standardized diagnostic criteria** and **validated cotinine thresholds** for toxicity remain non-uniform across studies; timing and nicotine tolerance complicate biomarker interpretation. (fassa2018urinarycotininein pages 1-3, ballard1995greentobaccosickness pages 1-3)
- Limited controlled intervention evidence for PPE/behavioral strategies within the retrieved full texts.

---

## References (URLs and publication dates)
- de Oliveira PPV et al. *First reported outbreak of green tobacco sickness in Brazil.* **Dec 2010**. https://doi.org/10.1590/s0102-311x2010001200005 (oliveira2010firstreportedoutbreak pages 1-2)
- Park SJ et al. *Green tobacco sickness among tobacco harvesters in a Korean village.* **Mar 2018**. https://doi.org/10.1016/j.shaw.2017.06.007 (park2018greentobaccosickness pages 4-4)
- Trapé-Cardoso M et al. *Cotinine levels and green tobacco sickness among shade tobacco workers.* **Oct 2005**. https://doi.org/10.1300/j096v10n02_05 (trapecardoso2005cotininelevelsand pages 1-3)
- McMahon LR. *Green tobacco sickness: mecamylamine, varenicline, and nicotine vaccine as clinical research tools and potential therapeutics.* **Jan 2019**. https://doi.org/10.1080/17512433.2019.1570844 (mcmahon2019greentobaccosickness pages 14-18)
- Quandt SA et al. *Migrant farmworkers and green tobacco sickness: new issues for an understudied disease.* **Mar 2000**. https://doi.org/10.1002/(sici)1097-0274(200003)37:3<307::aid-ajim10>3.0.co;2-z (quandt2000migrantfarmworkersand pages 1-2)
- Fassa AG et al. *Urinary cotinine in tobacco farmers in Southern Brazil.* **Aug 2018**. https://doi.org/10.11606/s1518-8787.2018052000287 (fassa2018urinarycotininein pages 1-3)
- Ballard T et al. *Green tobacco sickness: occupational nicotine poisoning in tobacco workers.* **Oct 1995**. https://doi.org/10.1080/00039896.1995.9935972 (ballard1995greentobaccosickness pages 1-3)
- Ziska L, Parks R. *Recent and projected changes in global climate may increase nicotine absorption and the risk of green tobacco sickness.* **Aug 2024**. https://doi.org/10.1038/s43856-024-00584-x (ziska2024recentandprojected pages 2-5, ziska2024recentandprojected pages 5-6)
- Ravi P et al. *Qualitative study to explore the occupational and reproductive health challenges among women tobacco farm laborers in Mysore District, India.* **May 2024**. https://doi.org/10.3390/ijerph21050606 (ravi2024qualitativestudyto pages 16-17, ravi2024qualitativestudyto pages 2-3, ravi2024qualitativestudyto pages 1-2)


References

1. (quandt2000migrantfarmworkersand pages 1-2): Sara A. Quandt, Thomas A Arcury, John S. Preisser, Deborah Norton, and Colin Austin. Migrant farmworkers and green tobacco sickness: new issues for an understudied disease. American journal of industrial medicine, 37 3:307-15, Mar 2000. URL: https://doi.org/10.1002/(sici)1097-0274(200003)37:3<307::aid-ajim10>3.0.co;2-z, doi:10.1002/(sici)1097-0274(200003)37:3<307::aid-ajim10>3.0.co;2-z. This article has 89 citations and is from a peer-reviewed journal.

2. (ballard1995greentobaccosickness pages 1-3): Terri Ballard, Janet Ehlers, Eugene Freund, Michael Auslander, Victoria Brandt, and William Halperin. Green tobacco sickness: occupational nicotine poisoning in tobacco workers. Archives of Environmental Health: An International Journal, 50:384-389, Oct 1995. URL: https://doi.org/10.1080/00039896.1995.9935972, doi:10.1080/00039896.1995.9935972. This article has 55 citations.

3. (oliveira2010firstreportedoutbreak pages 1-2): Patricia Pereira Vasconcelos de Oliveira, Camila Brederode Sihler, Lenildo de Moura, Deborah Carvalho Malta, Maria Célia de Albuquerque Torres, Sandra Márcia da Costa Pereira Lima, Ana Lucia Alves de Lima, Carlos Eduardo Leite, Vera Luiza da Costa-e-Silva, Jeremy Sobel, and Tatiana Miranda Lanzieri. First reported outbreak of green tobacco sickness in brazil. Cadernos de saude publica, 26 12:2263-9, Dec 2010. URL: https://doi.org/10.1590/s0102-311x2010001200005, doi:10.1590/s0102-311x2010001200005. This article has 62 citations and is from a peer-reviewed journal.

4. (fassa2018urinarycotininein pages 1-3): Anaclaudia Gastal Fassa, Rodrigo Dalke Meucci, Nadia Spada Fiori, Maria Laura Vidal Carrett, and Neice Muller Xavier Faria. Urinary cotinine in tobacco farmers in southern brazil. Revista de Saúde Pública, 52:70, Aug 2018. URL: https://doi.org/10.11606/s1518-8787.2018052000287, doi:10.11606/s1518-8787.2018052000287. This article has 12 citations.

5. (mcmahon2019greentobaccosickness pages 1-6): Lance R. McMahon. Green tobacco sickness: mecamylamine, varenicline, and nicotine vaccine as clinical research tools and potential therapeutics. Expert Review of Clinical Pharmacology, 12:189-195, Jan 2019. URL: https://doi.org/10.1080/17512433.2019.1570844, doi:10.1080/17512433.2019.1570844. This article has 15 citations and is from a peer-reviewed journal.

6. (mcmahon2019greentobaccosickness pages 14-18): Lance R. McMahon. Green tobacco sickness: mecamylamine, varenicline, and nicotine vaccine as clinical research tools and potential therapeutics. Expert Review of Clinical Pharmacology, 12:189-195, Jan 2019. URL: https://doi.org/10.1080/17512433.2019.1570844, doi:10.1080/17512433.2019.1570844. This article has 15 citations and is from a peer-reviewed journal.

7. (ziska2024recentandprojected pages 5-6): Lewis Ziska and Robbie Parks. Recent and projected changes in global climate may increase nicotine absorption and the risk of green tobacco sickness. Communications Medicine, Aug 2024. URL: https://doi.org/10.1038/s43856-024-00584-x, doi:10.1038/s43856-024-00584-x. This article has 4 citations and is from a peer-reviewed journal.

8. (trapecardoso2005cotininelevelsand pages 1-3): Marcia Trapé-Cardoso, Anne Bracker, Deborah Dauser, Cheryl Oncken, Laura Victoria Barrera, Bruce Gould, and Michael R. Grey. Cotinine levels and green tobacco sickness among shade tobacco workersx. Journal of Agromedicine, 10:27-37, Oct 2005. URL: https://doi.org/10.1300/j096v10n02\_05, doi:10.1300/j096v10n02\_05. This article has 18 citations and is from a peer-reviewed journal.

9. (ravi2024qualitativestudyto pages 1-2): Priyanka Ravi, Kiranmayee Muralidhar, Maiya G. Block Ngaybe, Shivamma Nayaka, Poornima Jayakrishna, Ashley A. Lowe, Karl Krupp, Amanda M. Wilson, Frank A. von Hippel, Zhao Chen, Lynn B. Gerald, and Purnima Madhivanan. Qualitative study to explore the occupational and reproductive health challenges among women tobacco farm laborers in mysore district, india. International Journal of Environmental Research and Public Health, May 2024. URL: https://doi.org/10.3390/ijerph21050606, doi:10.3390/ijerph21050606. This article has 5 citations.

10. (ravi2024qualitativestudyto pages 2-3): Priyanka Ravi, Kiranmayee Muralidhar, Maiya G. Block Ngaybe, Shivamma Nayaka, Poornima Jayakrishna, Ashley A. Lowe, Karl Krupp, Amanda M. Wilson, Frank A. von Hippel, Zhao Chen, Lynn B. Gerald, and Purnima Madhivanan. Qualitative study to explore the occupational and reproductive health challenges among women tobacco farm laborers in mysore district, india. International Journal of Environmental Research and Public Health, May 2024. URL: https://doi.org/10.3390/ijerph21050606, doi:10.3390/ijerph21050606. This article has 5 citations.

11. (ziska2024recentandprojected pages 2-5): Lewis Ziska and Robbie Parks. Recent and projected changes in global climate may increase nicotine absorption and the risk of green tobacco sickness. Communications Medicine, Aug 2024. URL: https://doi.org/10.1038/s43856-024-00584-x, doi:10.1038/s43856-024-00584-x. This article has 4 citations and is from a peer-reviewed journal.

12. (ravi2024qualitativestudyto pages 16-17): Priyanka Ravi, Kiranmayee Muralidhar, Maiya G. Block Ngaybe, Shivamma Nayaka, Poornima Jayakrishna, Ashley A. Lowe, Karl Krupp, Amanda M. Wilson, Frank A. von Hippel, Zhao Chen, Lynn B. Gerald, and Purnima Madhivanan. Qualitative study to explore the occupational and reproductive health challenges among women tobacco farm laborers in mysore district, india. International Journal of Environmental Research and Public Health, May 2024. URL: https://doi.org/10.3390/ijerph21050606, doi:10.3390/ijerph21050606. This article has 5 citations.

13. (park2018greentobaccosickness pages 4-4): Sung-Jun Park, Hyun-Sul Lim, Kwan Lee, and Seok-Ju Yoo. Green tobacco sickness among tobacco harvesters in a korean village. Safety and Health at Work, 9:71-74, Mar 2018. URL: https://doi.org/10.1016/j.shaw.2017.06.007, doi:10.1016/j.shaw.2017.06.007. This article has 47 citations and is from a peer-reviewed journal.
