---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:32:14.568160'
end_time: '2026-05-08T10:48:48.109207'
duration_seconds: 993.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cadmium Poisoning
  mondo_id: ''
  category: Environmental
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 52
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cadmium Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Cadmium Poisoning** covering all of the
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
- **Disease Name:** Cadmium Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Cadmium Poisoning** covering all of the
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


## Cadmium Poisoning (Cadmium Toxicity): Comprehensive Disease Characteristics Report (Environmental)

### 1. Disease Information
Cadmium poisoning (also termed *cadmium toxicity* or *cadmium intoxication*) is an exposure-mediated toxicologic disorder caused by acute high-dose cadmium (Cd) exposure (often inhalational) or chronic low-to-moderate exposure with long-term bioaccumulation, particularly in the kidney cortex. Acute disease is often dominated by pulmonary injury, while chronic disease is dominated by renal tubular injury with downstream effects on bone and other systems. (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 12-13)

**Key identifiers (ontology/classification):** MONDO, MeSH, ICD-10/ICD-11 identifiers were **not retrievable from the tool evidence** in this run and therefore are not reported here to avoid fabrication. (artifact-00)

**Common synonyms/alternative names:** cadmium toxicity; cadmium intoxication; chronic cadmium exposure toxicity; cadmium-induced nephrotoxicity (subset). (vamsi2024cadmiumtoxicityunveiling pages 8-9, balalimood2025recentadvancesin pages 9-11)

**Evidence sources:** The retrieved evidence base is primarily aggregated disease-level resources (reviews) and population/cohort studies (NHANES, regional cohorts), not EHR-derived phenotyping. (balalimood2025recentadvancesin pages 9-11, shi2024associationsofmixed pages 1-2)

| Concept item | Details | Evidence/notes | Key sources (URL; year) |
|---|---|---|---|
| Disease name | Cadmium poisoning | Environmental/toxic exposure disorder caused by acute or chronic exposure to cadmium or cadmium compounds. Acute disease is dominated by inhalational or high-dose ingestion toxicity; chronic disease reflects bioaccumulation, especially in kidney cortex. (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 12-13) | Balali-Mood et al., Heliyon, https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Chakif & Furrer, Int J Mol Sci, https://doi.org/10.3390/ijms27083513; 2026. |
| Core alternative names | Cadmium toxicity; cadmium intoxication; cadmium exposure toxicity | Recent reviews use these terms interchangeably in clinical/environmental toxicology contexts rather than as distinct diseases. (balalimood2025recentadvancesin pages 11-12, vamsi2024cadmiumtoxicityunveiling pages 8-9) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Vamsi et al., https://doi.org/10.36468/pharmaceutical-sciences.1427; 2024. |
| Disease category | Environmental / toxicologic / heavy-metal poisoning | Non-Mendelian, exposure-mediated condition; evidence in retrieved tools is disease-level literature and cohort/review evidence, not patient-specific EHR-derived ontology records. (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 12-13) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. |
| MONDO ID | not retrieved from tool evidence | Do not infer or invent identifier. | Not retrieved from ontology-focused tool evidence. |
| MeSH ID / descriptor ID | not retrieved from tool evidence | Do not infer or invent identifier. | Not retrieved from ontology-focused tool evidence. |
| ICD-10 / ICD-11 code | not retrieved from tool evidence | Toxic-effect coding likely exists in classification systems, but explicit code was not retrieved from tool evidence and should not be invented here. | Not retrieved from tool evidence. |
| Acute cadmium poisoning | Usually follows inhalation of cadmium oxide fumes/dust or high-dose ingestion | Defined clinically by respiratory irritation with symptom onset typically within 6–12 h after inhalation; may progress to cough, fever, respiratory distress, hypoxia, pneumonitis, pulmonary insufficiency, or death in severe cases. One review notes inhalation of 5 mg/m3 for 8 h may be lethal. (balalimood2025recentadvancesin pages 9-11, balalimood2025recentadvancesin pages 11-12, chakif2026heavymetaltoxicity pages 12-13) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. |
| Chronic cadmium poisoning | Long-term bioaccumulation disorder, especially affecting kidney, bone, lung, and cardiovascular system | Cadmium has a very long biologic half-life in kidney (~20–30 years in review evidence). Hallmark chronic effects are renal proximal tubular injury, proteinuria, progressive CKD, and skeletal demineralization/osteomalacia/osteoporosis. (chakif2026heavymetaltoxicity pages 12-13, chakif2026heavymetaltoxicity pages 7-8) | Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. |
| Major exposure sources | Food, smoking/tobacco, occupational inhalation, contaminated air/water/soil | Tobacco smoke is a major source; each cigarette may contain ~0.5–1 µg Cd. Occupational sources include mining, smelting, battery manufacture/recycling, fossil fuel combustion, plating, fertilizer production, and waste disposal. (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 7-8) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. |
| Renal hallmark definition | Cadmium nephrotoxicity with tubular and glomerular effects | Chronic exposure causes often irreversible proteinuria and tubular dysfunction. Nordberg review notes albuminuria is mainly glomerular and may fall when blood Cd decreases, while tubular dysfunction markers (β2-microglobulin, NAG) appear linked to accumulated tubular Cd and seem more irreversible. (nordberg2025metallothioneinandother pages 9-11) | Nordberg & Nordberg, Biomolecules, https://doi.org/10.3390/biom15081083; 2025. |
| Key renal biomarkers | Urine Cd (body burden), blood Cd (recent/ongoing exposure), urinary β2-microglobulin, urinary NAG, urinary albumin, eGFR | Reviews and cohorts repeatedly use urine Cd and blood Cd as exposure biomarkers; β2-microglobulin (B2-MG/β2-MG), NAG, and albuminuria are effect biomarkers; eGFR decline tracks clinically important renal loss. (nordberg2025metallothioneinandother pages 12-14, nordberg2025metallothioneinandother pages 9-11, chakif2026heavymetaltoxicity pages 12-13, chakif2026heavymetaltoxicity pages 14-16) | Nordberg & Nordberg, https://doi.org/10.3390/biom15081083; 2025. Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. |
| β2-microglobulinuria threshold | Urinary β2-microglobulin >300 µg/g creatinine (or >300 µg/L in some studies) | Used in multiple studies/reviews as a threshold for cadmium-related tubular dysfunction/kidney dysfunction. Nordberg review explicitly references urinary B2M >300 µg/g creatinine; Kwon study used β2-MG >300 µg/L as reference exceedance. (nordberg2025metallothioneinandother pages 9-11, nordberg2025metallothioneinandother pages 11-12, kwon2023associationbetweenlevels pages 9-10) | Nordberg & Nordberg, https://doi.org/10.3390/biom15081083; 2025. Kwon et al., https://doi.org/10.1038/s41598-022-27292-7; 2023. |
| NAG threshold / interpretation | Urinary NAG is an early tubular injury biomarker; threshold examples vary by study | Nordberg figure legend cited UNAG >23 U/g creatinine; Kwon study used NAG >11.5 U/L as reference exceedance; increased NAG is consistently linked with urinary cadmium. (nordberg2025metallothioneinandother pages 11-12, kwon2023associationbetweenlevels pages 9-10) | Nordberg & Nordberg, https://doi.org/10.3390/biom15081083; 2025. Kwon et al., https://doi.org/10.1038/s41598-022-27292-7; 2023. |
| Urinary cadmium threshold for renal risk | ~2–5 µg/g creatinine may indicate elevated body burden/renal risk; >10 µg/g creatinine associated with irreversible kidney damage in one review | Chakif review states chronic renal risk may occur at lower urinary levels than older models suggested and that ~2–5 µg/g creatinine may indicate elevated burden/risk. Vamsi review states urinary Cd <10 µg/g creatinine is associated with reversible renal dysfunction, whereas >10 µg/g creatinine can cause irreversible kidney damage. (chakif2026heavymetaltoxicity pages 14-16, vamsi2024cadmiumtoxicityunveiling pages 8-9) | Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. Vamsi et al., https://doi.org/10.36468/pharmaceutical-sciences.1427; 2024. |
| Metallothionein-related definition | Cadmium binds metallothionein (MT); MT is central to transport, sequestration, and renal toxicity modification | Nordberg review emphasizes MT as central to toxicokinetics: Cd-MT transports cadmium to renal tubules, and MT expression/protection modifies kidney injury risk. Anti-MT antibodies and low zinc status may worsen susceptibility. (nordberg2025metallothioneinandother pages 12-14, nordberg2025metallothioneinandother pages 9-11) | Nordberg & Nordberg, https://doi.org/10.3390/biom15081083; 2025. |
| Bone disease definition | Cadmium-related osteotoxicity / Itai-itai-like disease | Chronic exposure is associated with low bone mineralization, decalcification, fractures, osteomalacia, and osteoporosis; classic severe manifestation is Itai-itai disease. (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 12-13) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. |
| Lung involvement definition | Acute toxic inhalation injury and chronic pulmonary toxicity | Acute inhalation causes irritant pneumonitis/respiratory distress; chronic exposure has been linked to COPD/emphysema in reviews. (balalimood2025recentadvancesin pages 9-11, balalimood2025recentadvancesin pages 11-12) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. |
| Clinical management definition | Source control and supportive care are first-line; chelation is limited/controversial for cadmium | Reviews emphasize removing exposure, supportive care, occupational controls, smoking cessation, and nutrition. Routine chelation is not first-line; benefits are uncertain and some agents may worsen toxicity. BAL/dimercaprol is specifically discouraged/contraindicated for cadmium because Cd-BAL complexes may be more nephrotoxic. (balalimood2025recentadvancesin pages 11-12, chakif2026heavymetaltoxicity pages 16-17, chakif2026heavymetaltoxicity pages 8-9, vamsi2024cadmiumtoxicityunveiling pages 8-9) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Chakif & Furrer, https://doi.org/10.3390/ijms27083513; 2026. Vamsi et al., https://doi.org/10.36468/pharmaceutical-sciences.1427; 2024. |
| Protective/nutritional modifiers | Adequate zinc, iron, selenium, calcium may reduce cadmium uptake or toxicity | Reviews cite dietary sufficiency and good zinc status as protective; Nordberg review highlights inverse associations between zinc status/Zn-Cd quotient and tubular dysfunction. (balalimood2025recentadvancesin pages 9-11, nordberg2025metallothioneinandother pages 11-12) | Balali-Mood et al., https://doi.org/10.1016/j.heliyon.2025.e42696; 2025. Nordberg & Nordberg, https://doi.org/10.3390/biom15081083; 2025. |


*Table: This table summarizes the key identifiers, synonyms, and working clinical definitions for cadmium poisoning from the retrieved evidence base. It highlights how recent reviews define acute versus chronic toxicity and the main biomarkers and thresholds used in practice.*

---

### 2. Etiology
#### 2.1 Primary causal factors
Cadmium poisoning is primarily an **environmental/occupational toxic exposure** condition. Primary exposure routes include ingestion (diet), inhalation (occupational, tobacco smoke), and exposure through contaminated air/water/soil. (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 7-8)

#### 2.2 Risk factors
**Major exposure sources:**
- **Tobacco smoking:** A recent clinical review notes that “each cigarette may contain ~0.5–1 μg Cd,” highlighting tobacco smoke as a major atmospheric source. (balalimood2025recentadvancesin pages 9-11)
- **Occupational/industrial:** mining, smelting, battery manufacture/recycling, fossil fuel combustion, plating, fertilizer production, and waste disposal are emphasized as major sources. (balalimood2025recentadvancesin pages 9-11)
- **Dietary exposure:** Cd is widely present in foods; chronic exposure is therefore common. (satarug2025hypertensioninpeople pages 16-17)

**Host susceptibility:**
- **Iron deficiency/low iron stores** can increase intestinal absorption of Cd; women and children are noted as higher-risk groups due to lower iron stores. (satarug2026aretheguidelines pages 3-5)
- **Zinc deficiency/low zinc status** increases susceptibility to Cd kidney injury; zinc status modifies tubular toxicity risk in human evidence. (nordberg2025metallothioneinandother pages 9-11)

**Co-exposures:**
- Co-exposure to **inorganic arsenic** can potentiate Cd nephrotoxicity with more-than-additive tubular effects, and MT status may modify susceptibility in animal data summarized in review. (nordberg2025metallothioneinandother pages 12-14, nordberg2025metallothioneinandother pages 11-12)

#### 2.3 Protective factors
- **Adequate zinc status** is associated with lower prevalence of Cd-related tubular dysfunction; higher Zn/Cd quotients were strongly protective in population data summarized in a kidney-focused review. (nordberg2025metallothioneinandother pages 11-12)
- Nutritional sufficiency (iron/zinc/selenium; calcium) is repeatedly proposed as a practical exposure-mitigation approach for oral Cd assimilation. (balalimood2025recentadvancesin pages 9-11, satarug2025hypertensioninpeople pages 16-17)

#### 2.4 Gene–environment interactions (current evidence base)
Cadmium toxicity is not typically modeled as a monogenic disorder; instead, **gene–environment** interactions are framed through toxicokinetics/toxicodynamics modifiers. Metallothionein (MT) induction and MT-related biomarkers/antibodies are repeatedly discussed as determinants of Cd distribution and kidney injury susceptibility in human and animal evidence. (nordberg2025metallothioneinandother pages 12-14, nordberg2025metallothioneinandother pages 9-11)

*Ontology suggestions (non-exhaustive):* CHEBI: cadmium(2+) (cadmium ion); environmental exposure to heavy metal; exposure to tobacco smoke.

---

### 3. Phenotypes
Cadmium toxicity phenotypes depend on dose and route.

#### 3.1 Acute cadmium poisoning (typically inhalation)
**Core manifestations:** respiratory irritation progressing over hours to pneumonitis/respiratory distress.
- A clinical review describes symptom onset within **6–12 hours** after inhalation with cough/fever/respiratory distress and potential progression to hypoxia and pulmonary failure. (balalimood2025recentadvancesin pages 9-11)
- Quantitative lethality estimate in one review: **“The inhalation exposure to 5 mg/m3 for 8 h may be lethal.”** (balalimood2025recentadvancesin pages 11-12)

**Suggested HPO terms (examples):**
- Dyspnea (HP:0002094)
- Cough (HP:0012735)
- Fever (HP:0001945)
- Hypoxemia (HP:0012418)

#### 3.2 Chronic cadmium toxicity (bioaccumulation)
**Kidney (most sensitive/critical target):**
- Renal tubular injury with low-molecular-weight proteinuria; chronic kidney disease risk; effect biomarkers include urinary β2-microglobulin and urinary NAG; clinical endpoints include eGFR decline and albuminuria/proteinuria. (chakif2026heavymetaltoxicity pages 12-13, nordberg2025metallothioneinandother pages 9-11)
- Chronic renal injury is often described as difficult to reverse once established; a review emphasizes that tubular biomarkers may reflect more irreversible injury compared with albuminuria changes following reductions in blood Cd. (nordberg2025metallothioneinandother pages 9-11)

**Bone:** osteomalacia/osteoporosis/fractures (classically Itai-itai disease in severe exposures). (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 12-13)

**Neurologic/cognitive:** neurotoxicity signals in population studies (see Epidemiology/Statistics). (lu2024associationofurinary pages 1-2)

**Cardiovascular:** hypertension risk and related kidney-mediated mechanisms are discussed in expert reviews. (satarug2025hypertensioninpeople pages 10-12)

**Suggested HPO terms (examples):**
- Proteinuria (HP:0000093)
- Albuminuria (HP:0000097)
- Abnormal glomerular filtration rate (HP:0012211)
- Renal tubular dysfunction (HP:0000126)
- Osteoporosis (HP:0000939)
- Bone pain (HP:0002653)

**Quality of life impacts (evidence directionality):** In severe or chronic exposure, renal dysfunction and bone disease plausibly impair mobility and daily functioning; however, standardized QoL metrics (SF-36/EQ-5D) were not captured in the retrieved tool evidence.

---

### 4. Genetic/Molecular Information
#### 4.1 Causal genes / pathogenic variants
Cadmium poisoning is not a Mendelian disorder in the retrieved evidence; thus **no causal gene list or pathogenic variant catalog** is appropriate as “disease-causing” in the classical clinical genetics sense.

#### 4.2 Molecular modifiers and key targets (mechanistic relevance)
**Metallothionein (MT):** central protective/sequestration protein in Cd toxicokinetics and renal tubular handling. MT influences transport of Cd to renal tubules and binds Cd intracellularly, modulating injury risk. (nordberg2025metallothioneinandother pages 12-14, nordberg2025metallothioneinandother pages 9-11)

**Metal transporters implicated in uptake (review evidence):** DMT1, ZIP14, ATP7A, TRPV6 are discussed as routes by which Cd enters cells, with higher absorption in low-iron states. (satarug2026aretheguidelines pages 3-5)

*Ontology suggestions:*
- GO (biological process): response to cadmium ion; metal ion transport; response to oxidative stress; renal tubular cell apoptotic process; inflammatory response.
- CL (cell types): kidney proximal tubule epithelial cell (CL:0002306); hepatocyte (CL:0000182); macrophage (CL:0000235).

---

### 5. Environmental Information
**Environmental factors:** cadmium contamination of air, water, soil, and food chain; occupational industrial emissions; battery waste. (balalimood2025recentadvancesin pages 9-11)

**Lifestyle factors:** cigarette smoking is repeatedly highlighted as a major preventable contributor to Cd body burden; smoking cessation is explicitly recommended as a cadmium reduction strategy. (chakif2026heavymetaltoxicity pages 16-17)

**Infectious agents:** not applicable.

---

### 6. Mechanism / Pathophysiology (Causal Chain)
A consensus mechanistic chain in the retrieved evidence is:

1) **Exposure and absorption:** via inhalation (occupational/tobacco) and ingestion (diet). (balalimood2025recentadvancesin pages 9-11, chakif2026heavymetaltoxicity pages 7-8)

2) **Distribution and long residence time:** Cd binds proteins including metallothionein and concentrates in the **renal cortex**; a recent review states cadmium has a very long biologic half-life (~**20–30 years**). (chakif2026heavymetaltoxicity pages 12-13)

3) **Cellular entry and injury pathways:** Cd can hijack metal transporters (e.g., DMT1/ZIP14/ATP7A/TRPV6) to enter target cells. (satarug2026aretheguidelines pages 3-5)

4) **Renal tubular injury and functional decline:** proximal tubular dysfunction is a central clinical manifestation, with effect biomarkers including β2-microglobulin and NAG. (chakif2026heavymetaltoxicity pages 12-13, chakif2026heavymetaltoxicity pages 14-16)

5) **System-level outcomes:** CKD progression (eGFR loss), proteinuria/albuminuria; downstream effects include bone demineralization/fractures and cardiometabolic outcomes. (chakif2026heavymetaltoxicity pages 12-13, satarug2025hypertensioninpeople pages 10-12)

**Oxidative stress/mitochondrial dysfunction:** Reviews describe Cd-driven ROS generation and mitochondrial impairment; expert commentary also links Cd exposure to oxidative stress and inflammation across organs. (satarug2026aretheguidelines pages 16-18, balalimood2025recentadvancesin pages 9-11)

**Metallothionein and zinc interactions:** MT is portrayed as protective by binding Cd, and zinc status modifies susceptibility (e.g., higher Zn/Cd quotients protective against tubular dysfunction in population evidence summarized by Nordberg & Nordberg). (nordberg2025metallothioneinandother pages 11-12)

**Advanced/omics evidence:** mixture modeling and pathway-based analyses are emerging in human studies (e.g., mixed metal exposure modeling in NHANES; BKMR/WQS approaches), supporting a shift from single-metal to mixture-aware causal inference. (shi2024associationsofmixed pages 1-2)

---

### 7. Anatomical Structures Affected
**Primary organs:**
- **Kidney (renal cortex; proximal tubule):** principal site of accumulation and chronic injury. (chakif2026heavymetaltoxicity pages 12-13)
- **Lung:** key site for acute inhalational injury. (balalimood2025recentadvancesin pages 9-11)
- **Bone/skeleton:** demineralization/osteomalacia/osteoporosis and fracture risk. (chakif2026heavymetaltoxicity pages 12-13)

**Secondary systems:** cardiovascular (hypertension), nervous system (neurotoxicity/cognition), liver involvement in toxicokinetics. (satarug2025hypertensioninpeople pages 10-12, lu2024associationofurinary pages 1-2)

*Ontology suggestions:*
- UBERON: kidney cortex; proximal convoluted tubule; lung; bone tissue.
- GO Cellular Component: mitochondrion; cytosol; nucleus.

---

### 8. Temporal Development
**Onset patterns:**
- **Acute:** subacute respiratory syndrome hours after inhalation (6–12 h described). (balalimood2025recentadvancesin pages 9-11)
- **Chronic:** insidious, cumulative exposure with long tissue half-life, manifesting over years to decades. (chakif2026heavymetaltoxicity pages 12-13)

**Progression:**
- Expert review emphasizes that Cd-related loss of eGFR due to nephron destruction is irreversible once established (“eGFR deterioration due to Cd-induced nephron destruction is irreversible”). (satarug2025hypertensioninpeople pages 16-17)

---

### 9. Inheritance and Population
Cadmium poisoning is **not inherited**; it is primarily exposure-driven.

**Epidemiology/burden (recent quantitative data):**
- In NHANES 2011–2020 (n=9,056), kidney stone prevalence was **10.82%**, and urinary Cd was associated with higher kidney stone odds (see Section 5 Table). (ye2023nationalanalysisof pages 4-5)
- In NHANES 2011–2018 mixture analysis (n=3,080), CKD prevalence was **18.90%** (582 cases) and high mixed-metal exposure increased CKD odds; cadmium was a high-importance contributor in BKMR (PIP 0.911 in urine; 0.845 in blood). (shi2024associationsofmixed pages 4-5)
- In a Korean vulnerable-area cohort (n=298; mean age 70.3), exposure-area mean blood Cd was **1.89 µg/L** vs **0.89 µg/L** in control; urinary Cd **2.11 µg/L** vs **1.11 µg/L**, with renal biomarker associations. (kwon2023associationbetweenlevels pages 1-2)

**Demographics:** Susceptibility patterns include sex differences and higher absorption risk in low-iron states; race/ethnicity differences appear in some outcomes (e.g., cognition association in REGARDS observed among White but not Black participants). (satarug2026aretheguidelines pages 3-5, lu2024associationofurinary pages 1-2)

---

### 10. Diagnostics
**Core diagnostic strategy:** exposure history + biomonitoring + organ injury assessment.

#### 10.1 Exposure biomarkers
- **Urine cadmium (creatinine-corrected):** emphasized as a marker of Cd body burden; one review notes urine is often preferred for cadmium body burden. (chakif2026heavymetaltoxicity pages 14-16)
- **Blood cadmium:** more reflective of recent/ongoing exposure in many frameworks; correlated with some kidney outcomes and albuminuria trajectories in review evidence. (nordberg2025metallothioneinandother pages 9-11)

#### 10.2 Effect biomarkers (kidney)
Common effect biomarkers in human studies/reviews include:
- **Urinary β2-microglobulin** (β2M): tubular reabsorptive dysfunction marker. A widely used threshold is **β2M excretion 300 µg/g creatinine** (β2-microglobulinuria). (satarug2025hypertensioninpeople pages 14-16)
- **Urinary NAG:** tubular injury marker. Thresholds vary by study (examples include UNAG >23 U/g creatinine in a review figure legend and NAG >11.5 U/L as a reference exceedance in a regional cohort study). (nordberg2025metallothioneinandother pages 11-12, kwon2023associationbetweenlevels pages 9-10)
- **Albuminuria/proteinuria and eGFR:** clinically relevant endpoints; expert analysis argues eGFR decline should be prioritized in risk assessment relative to β2M-based endpoints. (satarug2026aretheguidelines pages 3-5, satarug2025hypertensioninpeople pages 10-12)

**Threshold examples (interpretation is study-specific):**
- A 2024 review states urinary Cd <10 µg/g creatinine is associated with reversible renal dysfunction, while >10 µg/g creatinine can cause irreversible damage. (vamsi2024cadmiumtoxicityunveiling pages 8-9)
- Another review suggests chronic renal risk may occur at **~2–5 µg/g creatinine** urinary Cd. (chakif2026heavymetaltoxicity pages 14-16)

#### 10.3 Differential diagnosis
Not systematically enumerated in the retrieved tool evidence; clinically, differential for tubular proteinuria/CKD includes diabetes, hypertension, other nephrotoxins (e.g., lead), and multiple-metal co-exposures, consistent with mixture analyses. (shi2024associationsofmixed pages 1-2)

---

### 11. Outcome / Prognosis
**Renal prognosis:** Chronic Cd exposure is associated with persistent renal tubular injury and progressive CKD risk. Expert commentary emphasizes irreversibility of eGFR deterioration once nephron destruction occurs. (satarug2025hypertensioninpeople pages 16-17)

**Population outcome signals:**
- In a Thai cohort analysis (n=737), risks of low eGFR and albuminuria rose ~twofold per doubling ECd/Ccr, and severe tubular injury risk (NAG/Ccr) increased with Cd burden. (satarug2024urinarynacetylglucosaminidasein pages 12-13)

Mortality rates and formal survival estimates were not retrieved in the tool evidence.

---

### 12. Treatment
**General principle:** remove exposure and provide supportive care; routine chelation is controversial for cadmium.

#### 12.1 Immediate management (acute inhalation/ingestion)
A clinical review emphasizes supportive measures including decontamination and pulmonary management. For acute cases it describes GI decontamination (e.g., gastric lavage when appropriate) and the use of corticosteroids for pulmonary inflammation in some contexts; dialysis is generally not effective except in renal failure. (balalimood2025recentadvancesin pages 11-12)

#### 12.2 Chelation therapy (evidence limitations)
- Expert review statement: **“therapeutically effective chelation treatment to remove Cd from the kidneys does not exist.”** (satarug2025hypertensioninpeople pages 16-17)
- Dimercaprol (BAL) is discouraged/contraindicated for cadmium in review evidence because Cd–BAL complexes can be more nephrotoxic than cadmium alone. (vamsi2024cadmiumtoxicityunveiling pages 8-9)
- Succimer (DMSA), DMPS, and DTPA are discussed as possible chelation options in some reviews, but with uncertain clinical benefit and important limitations; multiple sources stress that chelation should only be considered if benefits outweigh harms and that “source control is the anchor.” (balalimood2025recentadvancesin pages 11-12, chakif2026heavymetaltoxicity pages 16-17)

#### 12.3 Emerging/experimental strategies
A prevention-oriented approach using an orally administered chelating polymer (Chitosan@DOTAGA) was tested in mice to chelate Cd in the gut and reduce systemic effects from contaminated diet exposure (7 mg/kg cadmium in food). The polymer remained confined to the GI tract and reduced pathology scores (kidney score control 2 vs saline 27 vs treated 7) in this model. (howard2023combatingleadand pages 6-8)

**MAXO suggestions (non-exhaustive):**
- Removal of exposure source; smoking cessation; occupational exposure mitigation; supportive care; toxicology consultation; chelation therapy (restricted/conditional).

---

### 13. Prevention
Prevention is emphasized as the dominant strategy:
- Smoking cessation and dietary/exposure avoidance are repeatedly recommended. (chakif2026heavymetaltoxicity pages 16-17, satarug2025hypertensioninpeople pages 16-17)
- Occupational hygiene and ventilation; limiting industrial Cd uses; proper battery recycling/disposal; and nutrition optimization (iron/zinc/selenium adequacy) to reduce uptake are recommended in clinical management review evidence. (balalimood2025recentadvancesin pages 9-11, balalimood2025recentadvancesin pages 11-12)

---

### 14. Other Species / Natural Disease
Naturally occurring cadmium toxicosis in animals was not explicitly retrieved in the tool evidence; however, multiple reviews describe cadmium toxicity across humans and animals and emphasize conserved renal and bone targets. (nordberg2025metallothioneinandother pages 17-18)

---

### 15. Model Organisms
**Mouse models (in vivo):**
- A 2023 mouse study used dietary Cd exposure (7 mg/kg in food) and assessed mitigation via oral chelating polymer (Chitosan@DOTAGA). The polymer’s biodistribution was confined to the digestive tract and it reduced kidney and liver pathology scores compared with saline-exposed mice. (howard2023combatingleadand pages 6-8, howard2023combatingleadand pages 5-6)

Model limitations: exposure regimen and doses may not reflect human chronic low-dose dietary exposure; translation requires careful toxicokinetic scaling.

---

## Recent Developments and Real-World Implementations (2023–2024 emphasis)
Recent literature shows a shift toward (i) **mixture-aware exposure modeling** (e.g., BKMR/WQS in NHANES), (ii) **lower-effect thresholds** and debates about which renal endpoints best reflect clinically meaningful harm (eGFR vs β2M), and (iii) preventive “gut chelation” or exposure-blocking strategies in preclinical models. (shi2024associationsofmixed pages 4-5, satarug2025hypertensioninpeople pages 10-12, howard2023combatingleadand pages 6-8)

| Study (first author, year) | Population/design | Exposure metric | Outcome(s) | Key quantitative results | Notes |
|---|---|---|---|---|---|
| Ye, 2023 | NHANES 2011–2020 cross-sectional analysis; 9,056 U.S. adults aged ≥20 years | Urinary cadmium, quartiles: Q1 0.025–0.104 µg/L; Q2 0.105–0.218 µg/L; Q3 0.219–0.435 µg/L; Q4 0.435–7.581 µg/L | Self-reported kidney stones | Kidney stone prevalence 10.82%. Fully adjusted ORs vs Q1: Q2 1.40 (95% CI 1.06–1.84), Q3 1.18 (0.88–1.59), Q4 1.54 (1.10–2.06); continuous urinary Cd OR 1.13 (1.01–1.26). Restricted cubic spline showed a non-linear association (P for non-linear <0.001). DOI: https://doi.org/10.3389/fpubh.2023.1146263 (ye2023nationalanalysisof pages 1-2, ye2023nationalanalysisof pages 4-5) | Suggests even relatively low urinary Cd ranges are associated with higher kidney stone odds; cross-sectional design limits causal inference. |
| Shi, 2024 | NHANES 2011–2018 cross-sectional mixture analysis; 3,080 adults, 582 CKD cases (18.90%) | Urine and whole-blood metal mixtures including cadmium, manganese, lead, mercury | Chronic kidney disease (CKD) | High mixed-metal exposure associated with increased CKD odds: urine mixture OR 1.58 (95% CI 1.26–1.99); whole-blood mixture OR 1.67 (1.19–2.34). BKMR PIPs in overall population highlighted urine Cd 0.911 and blood Cd 0.845 among important contributors. DOI: https://doi.org/10.1038/s41598-024-63858-3 (shi2024associationsofmixed pages 4-5, shi2024associationsofmixed pages 1-2) | Cadmium acted within a co-exposure context rather than as a single-metal model; interactions were more evident in participants with T2DM. |
| Kwon, 2023 | Korean environmentally vulnerable-area study; n=298 total (low-exposure abandoned mine n=74, high-exposure abandoned mine n=68, refinery n=121, control n=35); mean age 70.3 years | Blood Cd and urinary Cd; heavy metal biomonitoring in exposed vs control regions | Renal biomarkers: urinary NAG, urinary β2-microglobulin (β2-MG), eGFR | In exposure areas vs control: mean blood Cd 1.89 vs 0.89 µg/L; urinary Cd 2.11 vs 1.11 µg/L. Blood Cd in refinery area had OR 38 for exceeding reference value vs control; urinary Cd was 7-fold higher in the low-exposure mine area vs control. Urinary Cd positively correlated with NAG in all areas; blood Cd associated with increased odds of β2-MG >300 µg/L and eGFR <60 mL/min/1.73 m²; NAG reference threshold >11.5 U/L. DOI: https://doi.org/10.1038/s41598-022-27292-7 (kwon2023associationbetweenlevels pages 9-10, kwon2023associationbetweenlevels pages 1-2) | Supports renal tubular injury as a prominent human signal of environmental Cd exposure; small regional study but with strong area contrasts. |
| Satarug, 2024 | Thai environmentally exposed cohort/cross-sectional analysis; 737 non-diabetic adults, 9.1% with eGFR ≤60 mL/min/1.73 m² | Urinary Cd normalized to creatinine clearance (ECd/Ccr); renal biomarkers normalized similarly | Low eGFR, albuminuria, tubular injury (NAG), β2-microglobulin-related tubular dysfunction | Risks of low eGFR and albuminuria rose twofold per doubling ECd/Ccr. Doubling ECd/Ccr increased risk of severe tubular injury measured by NAG/Ccr (POR 4.80, p=0.015). ENAG/Ccr associated with ECd/Ccr in men β=0.447 and women β=0.394; inversely associated with eGFR in women β=-0.178 and in high-Cd body burden group β=-0.223. Reported benchmark/threshold values include ECd/Ecr 0.5 µg/g linked to 2.6- to 3.6-fold higher odds of abnormal NAG excretion; BMDLs 0.5–0.8 and 0.7–1.2 µg/g creatinine; some studies suggest <0.3 µg/g. DOI: https://doi.org/10.3390/toxics12110775 (satarug2024urinarynacetylglucosaminidasein pages 12-13) | Highlights that tubular biomarkers and GFR decline may reflect partly different mechanisms/kinetics of Cd nephrotoxicity. |
| Lu, 2024 | REGARDS prospective cohort subcohort; 2,172 adults free of baseline cognitive impairment/stroke; mean age 64.1 years; 54.8% female; 38.7% Black; average follow-up ~10 years | Baseline urinary creatinine-corrected cadmium; dichotomized at median or analyzed by tertiles | Global cognitive impairment and domain-based cognitive impairment | During follow-up: 195 cases of global cognitive impairment and 53 domain-based cases. No overall association in full sample, but among White participants, high urinary Cd (≥median) was associated with doubled odds of global cognitive impairment: OR 2.07 (95% CI 1.18–3.64). Median urinary Cd was similar by race: Black 0.414 µg/g, White 0.407 µg/g. DOI: https://doi.org/10.1212/WNL.0000000000209808 (lu2024associationofurinary pages 1-2, lu2024associationofurinary pages 4-5, lu2024associationofurinary pages 8-9, lu2024associationofurinary pages 2-4) | Prospective design strengthens temporal inference; association appeared race-specific in this cohort and was not seen for domain-specific impairment overall. |


*Table: This table summarizes recent human studies linking cadmium exposure to kidney, renal biomarker, and cognitive outcomes, emphasizing 2023–2024 evidence. It is useful for quickly comparing exposure metrics, sample sizes, and quantitative effect estimates relevant to cadmium poisoning and chronic cadmium toxicity.*

---

## Visual Evidence (Tables)
The following extracted tables provide visual documentation of participant characteristics and measured blood/urine cadmium levels by region in a vulnerable-area cohort study.

- Participant characteristics and biomarker tables (cadmium levels; renal indicators) from Kwon et al. (Scientific Reports, 2023). (kwon2023associationbetweenlevels media 0a68bf68, kwon2023associationbetweenlevels media a1f51e53)

---

## Notes on Evidence Quality and Gaps
- Many quantitative human findings come from cross-sectional analyses (NHANES), which support association but not definitive causality. (ye2023nationalanalysisof pages 1-2, shi2024associationsofmixed pages 1-2)
- Prospective evidence exists for some outcomes (e.g., cognition in REGARDS), but findings can be subgroup-dependent and require replication. (lu2024associationofurinary pages 1-2)
- Standard ontology identifiers (MONDO/MeSH/ICD) were not retrievable from tool evidence in this run and should be added from dedicated ontology resources in a subsequent curation step. (artifact-00)


References

1. (balalimood2025recentadvancesin pages 9-11): Mahdi Balali-Mood, Nastaran Eizadi-Mood, Hossein Hassanian-Moghaddam, Leila Etemad, Mohammad Moshiri, Maryam Vahabzadeh, and Mahmood Sadeghi. Recent advances in the clinical management of intoxication by five heavy metals: mercury, lead, chromium, cadmium and arsenic. Heliyon, 11:e42696, Feb 2025. URL: https://doi.org/10.1016/j.heliyon.2025.e42696, doi:10.1016/j.heliyon.2025.e42696. This article has 65 citations.

2. (chakif2026heavymetaltoxicity pages 12-13): Dib Chakif and Julien Furrer. Heavy metal toxicity in clinical and environmental health: sources, mechanisms, diagnostics, and evidence-based management of mercury, lead, cadmium, and arsenic. International Journal of Molecular Sciences, 27:3513, Apr 2026. URL: https://doi.org/10.3390/ijms27083513, doi:10.3390/ijms27083513. This article has 0 citations.

3. (vamsi2024cadmiumtoxicityunveiling pages 8-9): N. Mohana Vamsi, J. Pavan Kumar, K. Ramadevi, and P. Swathi. Cadmium toxicity: unveiling the threat to human health. Indian Journal of Pharmaceutical Sciences, Jan 2024. URL: https://doi.org/10.36468/pharmaceutical-sciences.1427, doi:10.36468/pharmaceutical-sciences.1427. This article has 27 citations.

4. (shi2024associationsofmixed pages 1-2): Xiaoru Shi, Xiao Wang, Jia Zhang, Ying Dang, Changping Ouyang, Jinhua Pan, Aimin Yang, and Xiaobin Hu. Associations of mixed metal exposure with chronic kidney disease from nhanes 2011–2018. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-63858-3, doi:10.1038/s41598-024-63858-3. This article has 29 citations and is from a peer-reviewed journal.

5. (balalimood2025recentadvancesin pages 11-12): Mahdi Balali-Mood, Nastaran Eizadi-Mood, Hossein Hassanian-Moghaddam, Leila Etemad, Mohammad Moshiri, Maryam Vahabzadeh, and Mahmood Sadeghi. Recent advances in the clinical management of intoxication by five heavy metals: mercury, lead, chromium, cadmium and arsenic. Heliyon, 11:e42696, Feb 2025. URL: https://doi.org/10.1016/j.heliyon.2025.e42696, doi:10.1016/j.heliyon.2025.e42696. This article has 65 citations.

6. (chakif2026heavymetaltoxicity pages 7-8): Dib Chakif and Julien Furrer. Heavy metal toxicity in clinical and environmental health: sources, mechanisms, diagnostics, and evidence-based management of mercury, lead, cadmium, and arsenic. International Journal of Molecular Sciences, 27:3513, Apr 2026. URL: https://doi.org/10.3390/ijms27083513, doi:10.3390/ijms27083513. This article has 0 citations.

7. (nordberg2025metallothioneinandother pages 9-11): Gunnar F. Nordberg and Monica Nordberg. Metallothionein and other factors influencing cadmium-induced kidney dysfunction: review and commentary. Biomolecules, 15:1083, Jul 2025. URL: https://doi.org/10.3390/biom15081083, doi:10.3390/biom15081083. This article has 8 citations.

8. (nordberg2025metallothioneinandother pages 12-14): Gunnar F. Nordberg and Monica Nordberg. Metallothionein and other factors influencing cadmium-induced kidney dysfunction: review and commentary. Biomolecules, 15:1083, Jul 2025. URL: https://doi.org/10.3390/biom15081083, doi:10.3390/biom15081083. This article has 8 citations.

9. (chakif2026heavymetaltoxicity pages 14-16): Dib Chakif and Julien Furrer. Heavy metal toxicity in clinical and environmental health: sources, mechanisms, diagnostics, and evidence-based management of mercury, lead, cadmium, and arsenic. International Journal of Molecular Sciences, 27:3513, Apr 2026. URL: https://doi.org/10.3390/ijms27083513, doi:10.3390/ijms27083513. This article has 0 citations.

10. (nordberg2025metallothioneinandother pages 11-12): Gunnar F. Nordberg and Monica Nordberg. Metallothionein and other factors influencing cadmium-induced kidney dysfunction: review and commentary. Biomolecules, 15:1083, Jul 2025. URL: https://doi.org/10.3390/biom15081083, doi:10.3390/biom15081083. This article has 8 citations.

11. (kwon2023associationbetweenlevels pages 9-10): Jung-Yeon Kwon, Seungho Lee, Ulziikhishig Surenbaatar, Hyoun-Ju Lim, Byoung-Gwon Kim, Sang-Yong Eom, Yong Min Cho, Woo Jin Kim, Byeng-Chul Yu, Kwan Lee, and Young-Seoub Hong. Association between levels of exposure to heavy metals and renal function indicators of residents in environmentally vulnerable areas. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-022-27292-7, doi:10.1038/s41598-022-27292-7. This article has 40 citations and is from a peer-reviewed journal.

12. (chakif2026heavymetaltoxicity pages 16-17): Dib Chakif and Julien Furrer. Heavy metal toxicity in clinical and environmental health: sources, mechanisms, diagnostics, and evidence-based management of mercury, lead, cadmium, and arsenic. International Journal of Molecular Sciences, 27:3513, Apr 2026. URL: https://doi.org/10.3390/ijms27083513, doi:10.3390/ijms27083513. This article has 0 citations.

13. (chakif2026heavymetaltoxicity pages 8-9): Dib Chakif and Julien Furrer. Heavy metal toxicity in clinical and environmental health: sources, mechanisms, diagnostics, and evidence-based management of mercury, lead, cadmium, and arsenic. International Journal of Molecular Sciences, 27:3513, Apr 2026. URL: https://doi.org/10.3390/ijms27083513, doi:10.3390/ijms27083513. This article has 0 citations.

14. (satarug2025hypertensioninpeople pages 16-17): Soisungwan Satarug. Hypertension in people exposed to environmental cadmium: roles for 20-hydroxyeicosatetraenoic acid in the kidney. Journal of Xenobiotics, Aug 2025. URL: https://doi.org/10.3390/jox15040122, doi:10.3390/jox15040122. This article has 2 citations.

15. (satarug2026aretheguidelines pages 3-5): Soisungwan Satarug. Are the guidelines for dietary and workplace exposure to cadmium adequate? Unknown journal, Apr 2026. URL: https://doi.org/10.20944/preprints202604.0484.v1, doi:10.20944/preprints202604.0484.v1.

16. (lu2024associationofurinary pages 1-2): Liping Lu, Yijia Zhang, Meghan Angley, Shai Bejerano, John D. Brockman, Leslie A. McClure, Frederick W. Unverzagt, Alyce D. Fly, and Ka Kahe. Association of urinary cadmium concentration with cognitive impairment in us adults. Neurology, Oct 2024. URL: https://doi.org/10.1212/wnl.0000000000209808, doi:10.1212/wnl.0000000000209808. This article has 10 citations and is from a highest quality peer-reviewed journal.

17. (satarug2025hypertensioninpeople pages 10-12): Soisungwan Satarug. Hypertension in people exposed to environmental cadmium: roles for 20-hydroxyeicosatetraenoic acid in the kidney. Journal of Xenobiotics, Aug 2025. URL: https://doi.org/10.3390/jox15040122, doi:10.3390/jox15040122. This article has 2 citations.

18. (satarug2026aretheguidelines pages 16-18): Soisungwan Satarug. Are the guidelines for dietary and workplace exposure to cadmium adequate? Unknown journal, Apr 2026. URL: https://doi.org/10.20944/preprints202604.0484.v1, doi:10.20944/preprints202604.0484.v1.

19. (ye2023nationalanalysisof pages 4-5): Zhenyang Ye, Zaizhi Chen, Jin-Ying Luo, Lijing Xu, Dongping Fan, and Jia Wang. National analysis of urinary cadmium concentration and kidney stone: evidence from nhanes (2011–2020). Frontiers in Public Health, Mar 2023. URL: https://doi.org/10.3389/fpubh.2023.1146263, doi:10.3389/fpubh.2023.1146263. This article has 8 citations.

20. (shi2024associationsofmixed pages 4-5): Xiaoru Shi, Xiao Wang, Jia Zhang, Ying Dang, Changping Ouyang, Jinhua Pan, Aimin Yang, and Xiaobin Hu. Associations of mixed metal exposure with chronic kidney disease from nhanes 2011–2018. Scientific Reports, Jun 2024. URL: https://doi.org/10.1038/s41598-024-63858-3, doi:10.1038/s41598-024-63858-3. This article has 29 citations and is from a peer-reviewed journal.

21. (kwon2023associationbetweenlevels pages 1-2): Jung-Yeon Kwon, Seungho Lee, Ulziikhishig Surenbaatar, Hyoun-Ju Lim, Byoung-Gwon Kim, Sang-Yong Eom, Yong Min Cho, Woo Jin Kim, Byeng-Chul Yu, Kwan Lee, and Young-Seoub Hong. Association between levels of exposure to heavy metals and renal function indicators of residents in environmentally vulnerable areas. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-022-27292-7, doi:10.1038/s41598-022-27292-7. This article has 40 citations and is from a peer-reviewed journal.

22. (satarug2025hypertensioninpeople pages 14-16): Soisungwan Satarug. Hypertension in people exposed to environmental cadmium: roles for 20-hydroxyeicosatetraenoic acid in the kidney. Journal of Xenobiotics, Aug 2025. URL: https://doi.org/10.3390/jox15040122, doi:10.3390/jox15040122. This article has 2 citations.

23. (satarug2024urinarynacetylglucosaminidasein pages 12-13): Soisungwan Satarug. Urinary n-acetylglucosaminidase in people environmentally exposed to cadmium is minimally related to cadmium-induced nephron destruction. Toxics, 12:775, Oct 2024. URL: https://doi.org/10.3390/toxics12110775, doi:10.3390/toxics12110775. This article has 7 citations.

24. (howard2023combatingleadand pages 6-8): Jordyn Ann Howard, Halyna Kuznietsova, Natalia Dziubenko, Axel Aigle, Marco Natuzzi, Eloise Thomas, Vladimir Lysenko, Laurent David, Thomas Brichart, François Lux, and Olivier Tillement. Combating lead and cadmium exposure with an orally administered chitosan-based chelating polymer. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-28968-4, doi:10.1038/s41598-023-28968-4. This article has 23 citations and is from a peer-reviewed journal.

25. (nordberg2025metallothioneinandother pages 17-18): Gunnar F. Nordberg and Monica Nordberg. Metallothionein and other factors influencing cadmium-induced kidney dysfunction: review and commentary. Biomolecules, 15:1083, Jul 2025. URL: https://doi.org/10.3390/biom15081083, doi:10.3390/biom15081083. This article has 8 citations.

26. (howard2023combatingleadand pages 5-6): Jordyn Ann Howard, Halyna Kuznietsova, Natalia Dziubenko, Axel Aigle, Marco Natuzzi, Eloise Thomas, Vladimir Lysenko, Laurent David, Thomas Brichart, François Lux, and Olivier Tillement. Combating lead and cadmium exposure with an orally administered chitosan-based chelating polymer. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-023-28968-4, doi:10.1038/s41598-023-28968-4. This article has 23 citations and is from a peer-reviewed journal.

27. (ye2023nationalanalysisof pages 1-2): Zhenyang Ye, Zaizhi Chen, Jin-Ying Luo, Lijing Xu, Dongping Fan, and Jia Wang. National analysis of urinary cadmium concentration and kidney stone: evidence from nhanes (2011–2020). Frontiers in Public Health, Mar 2023. URL: https://doi.org/10.3389/fpubh.2023.1146263, doi:10.3389/fpubh.2023.1146263. This article has 8 citations.

28. (lu2024associationofurinary pages 4-5): Liping Lu, Yijia Zhang, Meghan Angley, Shai Bejerano, John D. Brockman, Leslie A. McClure, Frederick W. Unverzagt, Alyce D. Fly, and Ka Kahe. Association of urinary cadmium concentration with cognitive impairment in us adults. Neurology, Oct 2024. URL: https://doi.org/10.1212/wnl.0000000000209808, doi:10.1212/wnl.0000000000209808. This article has 10 citations and is from a highest quality peer-reviewed journal.

29. (lu2024associationofurinary pages 8-9): Liping Lu, Yijia Zhang, Meghan Angley, Shai Bejerano, John D. Brockman, Leslie A. McClure, Frederick W. Unverzagt, Alyce D. Fly, and Ka Kahe. Association of urinary cadmium concentration with cognitive impairment in us adults. Neurology, Oct 2024. URL: https://doi.org/10.1212/wnl.0000000000209808, doi:10.1212/wnl.0000000000209808. This article has 10 citations and is from a highest quality peer-reviewed journal.

30. (lu2024associationofurinary pages 2-4): Liping Lu, Yijia Zhang, Meghan Angley, Shai Bejerano, John D. Brockman, Leslie A. McClure, Frederick W. Unverzagt, Alyce D. Fly, and Ka Kahe. Association of urinary cadmium concentration with cognitive impairment in us adults. Neurology, Oct 2024. URL: https://doi.org/10.1212/wnl.0000000000209808, doi:10.1212/wnl.0000000000209808. This article has 10 citations and is from a highest quality peer-reviewed journal.

31. (kwon2023associationbetweenlevels media 0a68bf68): Jung-Yeon Kwon, Seungho Lee, Ulziikhishig Surenbaatar, Hyoun-Ju Lim, Byoung-Gwon Kim, Sang-Yong Eom, Yong Min Cho, Woo Jin Kim, Byeng-Chul Yu, Kwan Lee, and Young-Seoub Hong. Association between levels of exposure to heavy metals and renal function indicators of residents in environmentally vulnerable areas. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-022-27292-7, doi:10.1038/s41598-022-27292-7. This article has 40 citations and is from a peer-reviewed journal.

32. (kwon2023associationbetweenlevels media a1f51e53): Jung-Yeon Kwon, Seungho Lee, Ulziikhishig Surenbaatar, Hyoun-Ju Lim, Byoung-Gwon Kim, Sang-Yong Eom, Yong Min Cho, Woo Jin Kim, Byeng-Chul Yu, Kwan Lee, and Young-Seoub Hong. Association between levels of exposure to heavy metals and renal function indicators of residents in environmentally vulnerable areas. Scientific Reports, Feb 2023. URL: https://doi.org/10.1038/s41598-022-27292-7, doi:10.1038/s41598-022-27292-7. This article has 40 citations and is from a peer-reviewed journal.
