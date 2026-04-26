---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:27:42.761028'
end_time: '2026-04-25T22:37:53.701716'
duration_seconds: 610.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Menkes Disease
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Menkes Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Menkes Disease** covering all of the
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
- **Disease Name:** Menkes Disease
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Menkes Disease** covering all of the
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


# Menkes Disease (ATP7A-related copper transport disorder) — Comprehensive Disease Characteristics Report

## 1. Disease information

### Overview (current understanding)
Menkes disease (MD) is a rare, typically male-infantile, X-linked disorder of systemic copper deficiency caused by pathogenic variants in **ATP7A**, which encodes a copper-transporting P-type ATPase required for copper distribution to the secretory pathway and copper-dependent enzymes. The disorder is characterized by progressive neurodegeneration, seizures, hypotonia/developmental regression, abnormal hair (classically hypopigmented/brittle/kinky), and connective-tissue/vascular and skeletal abnormalities. (wiecek2024disordersofcopper pages 7-8, fujisawa2022earlyclinicalsigns pages 1-2, vairo2019asystematicreview pages 1-6)

### Key identifiers
* **OMIM:** Menkes disease **#309400** (wiecek2024disordersofcopper pages 7-8, feyter2023atp7a‐relatedcoppertransport pages 14-18)
* **OMIM (allelic disorders within ATP7A spectrum):** Occipital horn syndrome (OHS) **#304150**; X-linked distal spinal muscular atrophy type 3 (SMAX3) **#300489** (feyter2023atp7a‐relatedcoppertransport pages 14-18)
* **MeSH / ICD-10 / ICD-11 / Orphanet / MONDO:** Not retrievable from the available full-text evidence in this run; should be added from OMIM/Orphanet/MeSH/MONDO registries directly (not primary literature).

### Synonyms / alternative names
Reported synonyms include **Kinky Hair Disease**, **Trichopoliodystrophy**, and **Steely Disease**. (wiecek2024disordersofcopper pages 7-8)

### Evidence source type
This report is derived from **aggregated disease-level resources and primary/secondary literature** (systematic reviews, guidelines, case series/case reports) rather than EHR-derived cohorts. (feyter2023atp7a‐relatedcoppertransport pages 18-21, vairo2019asystematicreview pages 1-6, zhu2024brainandthe pages 1-2)

## 2. Etiology

### Disease causal factors
* **Genetic cause:** Pathogenic variants in **ATP7A** (Xq13.3) cause Menkes disease and related ATP7A-spectrum phenotypes. (fujisawa2022earlyclinicalsigns pages 1-2, wiecek2024disordersofcopper pages 7-8)
* **Variant landscape:** >350 disease-causing ATP7A variants have been reported (missense, nonsense, splice-site, indels, and larger events), with approximately one-third arising **de novo**. (wiecek2024disordersofcopper pages 7-8)

### Risk factors
* **Primary risk factor:** Inheritance of a pathogenic ATP7A variant (X-linked). Most affected individuals are male; female presentations are unusual but can occur in special genetic contexts (e.g., unfavorable X-inactivation). (wiecek2024disordersofcopper pages 10-11)

### Protective factors
No validated genetic or environmental protective factors were identified in the retrieved evidence.

### Gene–environment interactions
Not established for Menkes disease in the retrieved evidence; the phenotype is primarily determined by **ATP7A functional residual activity** and timing of therapeutic copper delivery. (tumer2017a37‐year‐oldmenkes pages 1-4, fujisawa2022earlyclinicalsigns pages 1-2)

## 3. Phenotypes (clinical spectrum)

### ATP7A-related clinical subtypes (2023 systematic re-definition)
A systematic review curated **162 molecularly confirmed** individuals and classified them as: **classical Menkes disease (CMD) 62.3%**, **atypical/attenuated Menkes disease (AMD) 11.1%**, **OHS 22.6%**, and **SMAX3 3.7%**. (feyter2023atp7a‐relatedcoppertransport pages 18-21)

Key differentiators:
* **CMD:** seizures as initial symptom or seizures **before 3 months** are highly suggestive; severe neurodevelopmental course and early mortality. (feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **AMD:** ataxia is relatively specific; lower early-demise risk than CMD. (feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **OHS:** occipital horns are pathognomonic; radial head dislocations, herniations, and dental abnormalities support the diagnosis; connective tissue/urologic issues common. (feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **SMAX3:** late-onset distal motor neuropathy without major neuromotor delay; defined by neurophysiology (EMG). (feyter2023atp7a‐relatedcoppertransport pages 24-27)

### Common phenotypes (type → characteristics → suggested HPO)
Below are representative phenotypes strongly supported in the retrieved clinical literature; frequencies are variably reported.

* **Neurodevelopmental delay/regression (symptom/sign):** typical onset in early infancy; often progressive. Suggested HPO: *Global developmental delay (HP:0001263)*, *Developmental regression (HP:0002376)*. (vairo2019asystematicreview pages 1-6)
* **Seizures/epileptic encephalopathy (symptom/sign):** often begin around 2–3 months; may be severe/intractable in classic disease. Suggested HPO: *Seizures (HP:0001250)*, *Infantile spasms (HP:0012469)*. (wiecek2024disordersofcopper pages 8-10, fujisawa2022earlyclinicalsigns pages 1-2)
* **Hypotonia (clinical sign):** early and common. Suggested HPO: *Hypotonia (HP:0001252)*. (vairo2019asystematicreview pages 1-6, feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **Hair abnormalities (physical manifestation):** hypopigmented/brittle/kinky hair in CMD; coarse hair more typical in OHS. Suggested HPO: *Pili torti (HP:0003777)*, *Abnormal hair (HP:0001595)*, *Hypopigmented hair (HP:0005558)*. (feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **Connective tissue/vascular involvement:** vascular tortuosity and bladder diverticula can occur across subtypes and have high complication risk. Suggested HPO: *Arterial tortuosity (HP:0005116)*, *Bladder diverticulum (HP:0000017)*. (feyter2023atp7a‐relatedcoppertransport pages 1-5, feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **Skeletal abnormalities:** wormian bones, metaphyseal changes; OHS with occipital horns/exostoses. Suggested HPO: *Wormian bones (HP:0002645)*, *Metaphyseal widening (HP:0005014)*, *Exostoses (HP:0100777)*, *Occipital horn (HP:0002517)*. (zhu2024brainandthe pages 1-2, feyter2023atp7a‐relatedcoppertransport pages 24-27)

### Quality of life impact (recent data)
A 2023 cross-sectional caregiver study (n=16) using **PedsQL 4.0** and the **PedsQL Family Impact Module** reported very low child HRQOL: overall mean **29.14 (SD 14.73)** on a 0–100 scale, with physical functioning particularly low (**10.55**, SD 10.26). Family impact was substantial, with mean overall family-impact rating **44.16 (SD 17.40)** and low scores in worry and daily activities domains. (rozensztrauch2023healthrelatedqualityof pages 1-2, rozensztrauch2023healthrelatedqualityof pages 7-8, rozensztrauch2023healthrelatedqualityof pages 4-5)

## 4. Genetic / molecular information

### Causal gene
* **ATP7A** (copper-transporting P-type ATPase) is the causal gene in Menkes disease. (fujisawa2022earlyclinicalsigns pages 1-2)

### Pathogenic variant classes and functional consequences
* Menkes disease is driven largely by **loss-of-function** or severely hypomorphic ATP7A variants. Truncating variants are enriched in CMD, while splice-site/intronic variants (allowing low residual expression) are enriched in OHS; SMAX3 is linked to missense variants in/near transmembrane helices essential for copper transport. (feyter2023atp7a‐relatedcoppertransport pages 24-27)

### Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes or disease-specific epigenetic signatures were identified in the retrieved evidence.

## 5. Environmental information
Menkes disease is primarily genetic. No environmental/lifestyle/infectious causal factors were identified in the retrieved evidence.

## 6. Mechanism / pathophysiology

### Core causal chain (systemic copper deficiency → enzyme dysfunction → multisystem phenotype)
ATP7A dysfunction impairs copper export and distribution, leading to **systemic copper deficiency**, low brain copper, and reduced activity of multiple copper-dependent enzymes (including **dopamine β-hydroxylase**, **lysyl oxidase**, and **cytochrome c oxidase**), which in turn drives neurological impairment, connective tissue fragility, and vascular/skeletal manifestations. (wiecek2024disordersofcopper pages 7-8, fujisawa2022earlyclinicalsigns pages 1-2)

### Upstream vs downstream mechanisms
* **Upstream:** impaired ATP7A-dependent copper transport and delivery to the secretory pathway (Golgi incorporation into cuproenzymes). (fujisawa2022earlyclinicalsigns pages 1-2)
* **Downstream:** impaired catecholamine biosynthesis (via dopamine β-hydroxylase), defective connective tissue crosslinking (lysyl oxidase), mitochondrial respiratory defects (cytochrome c oxidase), contributing to neurodegeneration and systemic tissue vulnerability. (wiecek2024disordersofcopper pages 7-8)

### Suggested ontology terms
* **GO Biological Process (examples):** copper ion transport; cellular copper ion homeostasis; catecholamine biosynthetic process; mitochondrial electron transport chain; extracellular matrix organization.
* **Cell types (CL examples):** neurons (incl. noradrenergic neurons), oligodendrocytes (myelination context), enterocytes (intestinal copper handling), vascular smooth muscle cells/fibroblasts (connective tissue phenotype).

## 7. Anatomical structures affected

### Organ systems (supported)
* **Central nervous system:** progressive neurodegeneration, brain atrophy, delayed myelination, seizures. (wiecek2024disordersofcopper pages 8-10, zhu2024brainandthe pages 1-2)
* **Vascular system:** intracranial arterial tortuosity; risk of vascular complications. (zhu2024brainandthe pages 1-2, feyter2023atp7a‐relatedcoppertransport pages 24-27)
* **Skeletal/connective tissue:** wormian bones, metaphyseal changes; occipital horns in OHS. (zhu2024brainandthe pages 1-2, feyter2023atp7a‐relatedcoppertransport pages 24-27)

### Imaging-supported anatomical localization (UBERON suggestions)
* Brain (UBERON:0000955), cerebellum (UBERON:0002037), basal ganglia (UBERON:0002420), intracranial arteries (UBERON:0001637), skull (UBERON:0003129), long bones (UBERON:0002384).

## 8. Temporal development (onset and progression)

* **Typical onset:** early infancy. Neurological disturbances often begin around **2–3 months**, and early hair abnormalities can appear by **1–2 months**. (wiecek2024disordersofcopper pages 8-10, fujisawa2022earlyclinicalsigns pages 1-2)
* **Progression:** typically progressive with neurodevelopmental regression and multisystem complications in CMD. (vairo2019asystematicreview pages 1-6)
* **Critical period for intervention:** neonatal/presymptomatic window is repeatedly emphasized for copper therapy benefit. (vairo2019asystematicreview pages 1-6, fujisawa2022earlyclinicalsigns pages 1-2)

## 9. Inheritance and population

### Inheritance
* **X-linked recessive** (primary). (fujisawa2022earlyclinicalsigns pages 1-2, vairo2019asystematicreview pages 1-6)

### Epidemiology (recently cited estimates)
Reported incidence/prevalence varies by geography:
* Europe incidence estimate: ~**1 in 300,000 live births**. (vairo2019asystematicreview pages 1-6)
* Australia: reports as high as **1 in 40,000**. (vairo2019asystematicreview pages 1-6)
* Japan incidence: **1 in 360,000** (reported in a 2022 review of early signs/treatment). (fujisawa2022earlyclinicalsigns pages 1-2)
* Prevalence estimate: **~1:140,000 males** (review source). (wiecek2024disordersofcopper pages 7-8)

## 10. Diagnostics

### Laboratory tests and biomarkers
* **Serum copper and ceruloplasmin:** classically low, but unreliable for neonates due to low levels in healthy newborns. One pediatric review recommends measuring after the **third week** of life. (wiecek2024disordersofcopper pages 10-11, zhu2024brainandthe pages 1-2)
* **Neonatal plasma catecholamines (guideline-level evidence):** A systematic-review guideline reports that plasma catecholamine analysis supports neonatal diagnosis, with reported diagnostic thresholds of **dopamine/norepinephrine ratio >0.2** and **DOPAC/DHPG ratio >5**, with **100% sensitivity and specificity** in small neonatal cohorts. (vairo2019asystematicreview pages 6-10, vairo2019asystematicreview pages 18-22)

Direct abstract-quote style statements present in the evidence include:
* “**analysis of plasma catecholamine levels is accurate for neonatal diagnosis of Menkes disease**” (systematic review/guideline). (vairo2019asystematicreview pages 1-6)
* “**serum copper and ceruloplasmin levels are not reliable diagnostic biomarkers due to the low concentrations in healthy newborns**” (case report/review). (zhu2024brainandthe pages 1-2)

### Imaging
A 2024 BMC Pediatrics case report/literature review emphasizes characteristic imaging patterns:
* Brain MRI/MRA: **intracranial vascular tortuosity**, cerebral/cerebellar atrophy, delayed myelination/white-matter changes, basal ganglia abnormalities. (zhu2024brainandthe pages 1-2, zhu2024brainandthe media f56ccfea)
* Skeletal radiographs: **wormian bones**, rib flaring, metaphyseal spurring, periosteal reactions. (zhu2024brainandthe pages 1-2, zhu2024brainandthe media f2ce26df)

### Genetic testing
Molecular confirmation by identifying a pathogenic **ATP7A** variant is central; ACMG-based variant classification is used in clinical reporting. (zhu2024brainandthe pages 1-2)

### Prenatal diagnosis and counseling
Prenatal genetic diagnosis is feasible in families with a prior affected child; counseling should consider possibilities such as germline mosaicism when maternal carrier status is not detected. (vairo2019asystematicreview pages 1-6, vairo2019asystematicreview pages 18-22)

## 11. Outcome / prognosis

### Natural history (untreated)
Classic Menkes disease has a poor prognosis, often leading to death in early childhood (commonly cited as before ~3 years). (fujisawa2022earlyclinicalsigns pages 1-2, vairo2019asystematicreview pages 1-6)

### Subtype-stratified mortality (systematic review)
In the 162-person systematic review:
* **CMD mortality 40.6%**, mean age at death **2.3 years**.
* **OHS mortality 13.5%**, mean age at death **25.3 years**.
Infectious disease was the most common cause of death in CMD. (feyter2023atp7a‐relatedcoppertransport pages 18-21)

## 12. Treatment

### Standard disease-modifying therapy: parenteral copper histidine / copper histidinate
Evidence syntheses and clinical programs consistently identify **parenteral copper-histidine / copper histidinate** as the main disease-modifying therapy, with benefit strongest when started in the neonatal/presymptomatic period.

* Guideline conclusion (systematic review): “**treatment with copper-histidine is effective to increase survival and reduce neurologic burden of the disease if initiated in the neonatal period**.” (vairo2019asystematicreview pages 1-6)
* Quantitative survival comparisons summarized in the guideline review include improved survival with neonatal initiation (e.g., **62.5% vs 8.3–37.5%**, and **92% vs 13%** in small cohorts/historical comparisons) and low NNTs to prevent a death (reported as 2.6 and 1.27 across datasets). (vairo2019asystematicreview pages 10-14)
* Treatment response is heterogeneous and may depend on residual ATP7A function; a long-surviving treated individual reached **37 years**, associated with early and sustained parenteral copper and a missense variant consistent with residual transport function, although long-term renal toxicity occurred. (tumer2017a37‐year‐oldmenkes pages 1-4)

**CHEBI suggestion:** copper(II) (CHEBI:29036); copper histidinate / copper bis(histidinate) (map to appropriate CHEBI entry in downstream curation).

**MAXO suggestions:** copper supplementation therapy; subcutaneous drug administration; parenteral trace-element replacement.

### Supportive care (real-world implementation)
Supportive management includes seizure control, nutritional support/feeding tube placement, infection prevention, and management of urologic complications such as bladder diverticula. (zhu2024brainandthe pages 4-6)

### Emerging/experimental therapies (latest research emphasis)
* **CNS-directed AAV gene therapy (preclinical):** In a severe mouse model, CSF-delivered rAAV9 encoding a compact ATP7A (rsATP7A) combined with subcutaneous copper histidinate produced **53.3% long-term (≥300-day) survival** versus **0%** with either treatment alone, with improvements in brain copper, neurochemistry, and neurobehavior. (haddad2018cerebrospinalfluiddirectedraav9rsatp7a pages 1-2)

## 13. Prevention

* **Primary prevention:** not applicable in a genetic disorder, aside from reproductive options.
* **Secondary prevention (early detection):** the key preventive strategy for morbidity/mortality is **early/presymptomatic diagnosis** enabling neonatal copper therapy. Plasma catecholamine ratios are described as accurate for neonatal diagnosis in guideline synthesis. (vairo2019asystematicreview pages 6-10, vairo2019asystematicreview pages 1-6)
* **Genetic counseling / reproductive prevention:** prenatal genetic diagnosis is feasible in families with a known case; counseling should account for potential germline mosaicism. (vairo2019asystematicreview pages 18-22)

## 14. Other species / natural disease
The retrieved evidence does not provide natural (non-laboratory) Menkes-like disease in other species.

## 15. Model organisms
A severe Menkes mouse model has been used to test combined copper replacement and CNS gene therapy strategies, demonstrating major survival and neuropathology improvements with combined CSF rAAV9-rsATP7A plus copper histidinate. (haddad2018cerebrospinalfluiddirectedraav9rsatp7a pages 1-2)

## Current applications and real-world implementations (ClinicalTrials.gov)

* **NCT00001262 (NIH; started 1990; completed 2013):** “Early Copper Histidine Therapy in Menkes Disease,” Phase 1/2 single-group, **n=60**, presymptomatic newborns; primary outcome developmental milestones at 36 months or death. (NCT00001262 chunk 1)
* **NCT00811785 (Cyprium; completed 2020):** Phase 3, **n=93**, daily subcutaneous copper histidinate up to 3 years; survival comparisons for classic Menkes and neurologic outcomes for related phenotypes. (NCT00811785 chunk 1)
* **NCT04074512 (Sentynl; expanded access; “approved for marketing” listing):** provides subcutaneous copper histidinate (CUTX-101) for US pediatric patients <6 years, including newly diagnosed individuals under defined biochemical/genetic criteria. (NCT04074512 chunk 1)

## Expert opinion / analysis (authoritative synthesis)

* A 2019 evidence-based guideline concludes copper-histidine can be disease-modifying **only when initiated in the neonatal period**, and emphasizes the inadequacy of relying on newborn serum copper/ceruloplasmin for early diagnosis, motivating use of neonatal catecholamine testing and prenatal diagnosis in known families. (vairo2019asystematicreview pages 1-6)
* A 2023 systematic review highlights that **counseling is challenging** due to overlap among ATP7A phenotypes, limited predictive biomarkers, and weak genotype–phenotype correlation; it proposes practical subtype criteria and reports substantial differences in mortality between CMD and OHS. (feyter2023atp7a‐relatedcoppertransport pages 18-21, feyter2023atp7a‐relatedcoppertransport pages 24-27)

---

## Reference summary table
The following table consolidates identifiers, subtype definitions, diagnostic biomarkers, epidemiology, and prognosis.

| Domain | Key data | Quantitative details | DOI / URL / Year | Supporting citations |
|---|---|---|---|---|
| Disease / identifiers | Menkes disease; OMIM **#309400**; ATP7A-related copper transport disorder spectrum includes classical Menkes disease (CMD), atypical Menkes disease (AMD), occipital horn syndrome (OHS; OMIM **#304150**), and X-linked distal spinal muscular atrophy type 3 / SMAX3 (OMIM **#300489**) | ATP7A spans ~140 kb with 23 exons; review cohort included **162** molecularly confirmed individuals | De Feyter et al., *J Inherit Metab Dis* 2023; DOI: https://doi.org/10.1002/jimd.12590 | (feyter2023atp7a‐relatedcoppertransport pages 1-5, feyter2023atp7a‐relatedcoppertransport pages 18-21, feyter2023atp7a‐relatedcoppertransport pages 14-18) |
| Synonyms / alternative names | Kinky Hair Disease, Trichopoliodystrophy, Steely Disease; OHS also described as X-linked cutis laxa variant | Primarily affects male infants; female cases rare but reported due to unusual X-inactivation or chromosomal mechanisms | Więcek & Paprocka 2024: https://doi.org/10.3390/metabo14010038; Matsumoto et al. 2024: https://doi.org/10.1038/s41598-023-50668-2 | (wiecek2024disordersofcopper pages 7-8, wiecek2024disordersofcopper pages 10-11, wiecek2024disordersofcopper pages 8-10) |
| Inheritance / causal gene | **X-linked recessive** disorder caused by pathogenic variants in **ATP7A** (ATPase copper transporting alpha; Xq13.3), encoding a copper-transporting P-type ATPase | >**350** disease-causing variants reported; about **one-third de novo** | Więcek & Paprocka 2024: https://doi.org/10.3390/metabo14010038; Fujisawa et al. 2022: https://doi.org/10.1016/j.ymgmr.2022.100849 | (wiecek2024disordersofcopper pages 7-8, wiecek2024disordersofcopper pages 10-11, fujisawa2022earlyclinicalsigns pages 1-2) |
| Major subtypes | **CMD:** early-onset neurodegeneration with early seizures, severe course. **AMD:** attenuated overlap phenotype, ataxia is a key discriminator, better survival. **OHS:** milder connective-tissue-predominant phenotype with occipital horns, radial head dislocations, hernias, bladder diverticula, dental abnormalities. **SMAX3:** late-onset distal motor neuropathy without intellectual disability or occipital horns | Distribution in 162-patient review: CMD **101/162 (62.3%)**; AMD **18/162 (11.1%)**; OHS **37/162 (22.6%)**; SMAX3 **6/162 (3.7%)** | De Feyter et al. 2023: https://doi.org/10.1002/jimd.12590 | (feyter2023atp7a‐relatedcoppertransport pages 1-5, feyter2023atp7a‐relatedcoppertransport pages 18-21, feyter2023atp7a‐relatedcoppertransport pages 14-18, feyter2023atp7a‐relatedcoppertransport pages 24-27) |
| Hallmark biochemical diagnosis | Low serum copper and ceruloplasmin are classic findings, but both are unreliable in healthy newborns/early infancy; **ceruloplasmin may be more sensitive than serum copper** for severity discrimination among ATP7A phenotypes | Measure serum copper / ceruloplasmin **after the 3rd week of life** in one review; conventional blood copper / ceruloplasmin become more diagnostically useful only **after ~3 months** in guideline review | Vairo et al. 2019: https://doi.org/10.1016/j.ymgme.2018.12.005; Więcek & Paprocka 2024: https://doi.org/10.3390/metabo14010038; Zhu et al. 2024: https://doi.org/10.1186/s12887-024-04885-x | (wiecek2024disordersofcopper pages 10-11, vairo2019asystematicreview pages 6-10, vairo2019asystematicreview pages 1-6, feyter2023atp7a‐relatedcoppertransport pages 27-31, zhu2024brainandthe pages 1-2) |
| Plasma catecholamine biomarkers | Neonatal plasma catecholamines are highlighted as accurate early biomarkers because dopamine-β-hydroxylase is copper-dependent | Diagnostic thresholds reported: **dopamine / norepinephrine ratio >0.2** and **dihydroxyphenylacetic acid / dihydroxyphenylglycol ratio >5**; reported **100% sensitivity and 100% specificity** in small neonatal cohorts summarized by guideline | Vairo et al. 2019: https://doi.org/10.1016/j.ymgme.2018.12.005 | (vairo2019asystematicreview pages 6-10, vairo2019asystematicreview pages 18-22) |
| Epidemiology | Rare disorder with region-specific estimates | Europe: incidence about **1 in 300,000 live births**; Australia: reports up to **1 in 40,000**; Japan: incidence **1 in 360,000**; prevalence estimate in one review about **1:140,000 males** | Vairo et al. 2019: https://doi.org/10.1016/j.ymgme.2018.12.005; Fujisawa et al. 2022: https://doi.org/10.1016/j.ymgmr.2022.100849; Więcek & Paprocka 2024: https://doi.org/10.3390/metabo14010038 | (wiecek2024disordersofcopper pages 7-8, fujisawa2022earlyclinicalsigns pages 1-2, vairo2019asystematicreview pages 1-6) |
| Typical onset / hallmark clinical picture | Onset in early infancy with abnormal hair, hypotonia, developmental regression, seizures, connective-tissue and vascular abnormalities, feeding difficulties, autonomic dysfunction; imaging often shows cerebral/cerebellar atrophy and tortuous intracranial vessels | First sign can be sparse/lustreless hair at **1–2 months**; neurological disturbances often begin at **2–3 months**; typical diagnosis at **3–6 months**; mean age at diagnosis in one cohort **8.7 months** | Więcek & Paprocka 2024: https://doi.org/10.3390/metabo14010038; Fujisawa et al. 2022: https://doi.org/10.1016/j.ymgmr.2022.100849; Zhu et al. 2024: https://doi.org/10.1186/s12887-024-04885-x | (wiecek2024disordersofcopper pages 8-10, fujisawa2022earlyclinicalsigns pages 1-2, zhu2024brainandthe pages 1-2) |
| Prognosis / mortality | Natural history is progressive and often fatal in classic disease; respiratory and gastrointestinal complications are common causes of death; OHS and AMD have substantially better survival than CMD | Without treatment, most classic cases die by **<3 years** (some reviews state before **4 years**); in 162-patient review CMD mortality **40.6%**, mean age at death **2.3 years**; OHS mortality **13.5%**, mean age at death **25.3 years**; cerebrovascular accidents reported in up to **10%** | De Feyter et al. 2023: https://doi.org/10.1002/jimd.12590; Vairo et al. 2019: https://doi.org/10.1016/j.ymgme.2018.12.005; Więcek & Paprocka 2024: https://doi.org/10.3390/metabo14010038 | (feyter2023atp7a‐relatedcoppertransport pages 18-21, wiecek2024disordersofcopper pages 10-11, wiecek2024disordersofcopper pages 8-10, vairo2019asystematicreview pages 1-6, feyter2023atp7a‐relatedcoppertransport pages 24-27) |
| Treatment-linked prognosis modifier | Early **parenteral copper-histidine / copper histidinate** is the main disease-modifying therapy; best outcomes occur with **neonatal / presymptomatic** initiation, especially when residual ATP7A activity remains | Early-treated survival in summarized cohorts: **62.5% vs 8.3–37.5%** and **92% vs 13%** versus later/historical comparators; one long-surviving treated patient reached **37 years**; combined mouse therapy **rAAV9-rsATP7A + CuHis** achieved **53.3%** long-term survival vs **0%** with either alone | Vairo et al. 2019: https://doi.org/10.1016/j.ymgme.2018.12.005; Tümer et al. 2017: https://doi.org/10.1111/cge.13083; Haddad et al. 2018: https://doi.org/10.1016/j.omtm.2018.07.002 | (haddad2018cerebrospinalfluiddirectedraav9rsatp7a pages 1-2, tumer2017a37‐year‐oldmenkes pages 1-4, vairo2019asystematicreview pages 1-6, fujisawa2022earlyclinicalsigns pages 1-2, vairo2019asystematicreview pages 10-14) |


*Table: This table compiles core disease metadata, subtype distinctions, diagnostic biomarkers, epidemiology, and prognosis for Menkes disease from the gathered evidence. It is designed as a compact reference for rapid knowledge-base population with direct citation support.*

---

## Notes on evidence gaps
* ICD-10/ICD-11, MeSH, Orphanet, and MONDO identifiers were not extractable from the retrieved full-text set in this run and should be programmatically added from their respective terminologies/databases.
* Treatment evidence in humans remains limited by small cohorts and historical comparisons; heterogeneity by residual ATP7A function is strongly suggested by long-term survivor case evidence. (tumer2017a37‐year‐oldmenkes pages 1-4, vairo2019asystematicreview pages 10-14)


References

1. (wiecek2024disordersofcopper pages 7-8): Sabina Więcek and Justyna Paprocka. Disorders of copper metabolism in children—a problem too rarely recognized. Metabolites, 14:38, Jan 2024. URL: https://doi.org/10.3390/metabo14010038, doi:10.3390/metabo14010038. This article has 18 citations.

2. (fujisawa2022earlyclinicalsigns pages 1-2): Chie Fujisawa, Hiroko Kodama, Yasuhiro Sato, Masakazu Mimaki, Mariko Yagi, Hiroyuki Awano, Muneaki Matsuo, Haruo Shintaku, Sayaka Yoshida, Masaki Takayanagi, Mitsuru Kubota, Akihito Takahashi, and Yoshikiyo Akasaka. Early clinical signs and treatment of menkes disease. Molecular Genetics and Metabolism Reports, 31:100849, Jun 2022. URL: https://doi.org/10.1016/j.ymgmr.2022.100849, doi:10.1016/j.ymgmr.2022.100849. This article has 48 citations.

3. (vairo2019asystematicreview pages 1-6): Filippo Pinto e Vairo, Bruna Cristine Chwal, Silvana Perini, Maria Angélica Pires Ferreira, Ana Carolina de Freitas Lopes, and Jonas Alex Morales Saute. A systematic review and evidence-based guideline for diagnosis and treatment of menkes disease. Molecular genetics and metabolism, 126 1:6-13, Jan 2019. URL: https://doi.org/10.1016/j.ymgme.2018.12.005, doi:10.1016/j.ymgme.2018.12.005. This article has 111 citations and is from a peer-reviewed journal.

4. (feyter2023atp7a‐relatedcoppertransport pages 14-18): S. De Feyter, A. Beyens, and B. Callewaert. <scp><i>atp7a</i></scp>‐related copper transport disorders: a systematic review and definition of the clinical subtypes. Journal of Inherited Metabolic Disease, 46:163-173, Feb 2023. URL: https://doi.org/10.1002/jimd.12590, doi:10.1002/jimd.12590. This article has 27 citations and is from a peer-reviewed journal.

5. (feyter2023atp7a‐relatedcoppertransport pages 18-21): S. De Feyter, A. Beyens, and B. Callewaert. <scp><i>atp7a</i></scp>‐related copper transport disorders: a systematic review and definition of the clinical subtypes. Journal of Inherited Metabolic Disease, 46:163-173, Feb 2023. URL: https://doi.org/10.1002/jimd.12590, doi:10.1002/jimd.12590. This article has 27 citations and is from a peer-reviewed journal.

6. (zhu2024brainandthe pages 1-2): Juncheng Zhu, Yi Liao, Xuesheng Li, Fenglin Jia, Xinmao Ma, and Haibo Qu. Brain and the whole-body bone imaging appearances in menkes disease: a case report and literature review. BMC Pediatrics, Jun 2024. URL: https://doi.org/10.1186/s12887-024-04885-x, doi:10.1186/s12887-024-04885-x. This article has 4 citations and is from a peer-reviewed journal.

7. (wiecek2024disordersofcopper pages 10-11): Sabina Więcek and Justyna Paprocka. Disorders of copper metabolism in children—a problem too rarely recognized. Metabolites, 14:38, Jan 2024. URL: https://doi.org/10.3390/metabo14010038, doi:10.3390/metabo14010038. This article has 18 citations.

8. (tumer2017a37‐year‐oldmenkes pages 1-4): Zeynep Tümer, M. Petris, S. Zhu, J. Mercer, J. Bukrinski, S. Bilz, Kurt Baerlocher, N. Horn, and Lisbeth Birk Møller. A 37‐year‐old menkes disease patient—residual atp7a activity and early copper administration as key factors in beneficial treatment. Clinical Genetics, 92:548-553, Nov 2017. URL: https://doi.org/10.1111/cge.13083, doi:10.1111/cge.13083. This article has 10 citations and is from a peer-reviewed journal.

9. (feyter2023atp7a‐relatedcoppertransport pages 24-27): S. De Feyter, A. Beyens, and B. Callewaert. <scp><i>atp7a</i></scp>‐related copper transport disorders: a systematic review and definition of the clinical subtypes. Journal of Inherited Metabolic Disease, 46:163-173, Feb 2023. URL: https://doi.org/10.1002/jimd.12590, doi:10.1002/jimd.12590. This article has 27 citations and is from a peer-reviewed journal.

10. (wiecek2024disordersofcopper pages 8-10): Sabina Więcek and Justyna Paprocka. Disorders of copper metabolism in children—a problem too rarely recognized. Metabolites, 14:38, Jan 2024. URL: https://doi.org/10.3390/metabo14010038, doi:10.3390/metabo14010038. This article has 18 citations.

11. (feyter2023atp7a‐relatedcoppertransport pages 1-5): S. De Feyter, A. Beyens, and B. Callewaert. <scp><i>atp7a</i></scp>‐related copper transport disorders: a systematic review and definition of the clinical subtypes. Journal of Inherited Metabolic Disease, 46:163-173, Feb 2023. URL: https://doi.org/10.1002/jimd.12590, doi:10.1002/jimd.12590. This article has 27 citations and is from a peer-reviewed journal.

12. (rozensztrauch2023healthrelatedqualityof pages 1-2): Anna Rozensztrauch, Izabela Dzien, and Robert Śmigiel. Health-related quality of life and family functioning of primary caregivers of children with menkes disease. Journal of Clinical Medicine, 12:1769, Feb 2023. URL: https://doi.org/10.3390/jcm12051769, doi:10.3390/jcm12051769. This article has 8 citations.

13. (rozensztrauch2023healthrelatedqualityof pages 7-8): Anna Rozensztrauch, Izabela Dzien, and Robert Śmigiel. Health-related quality of life and family functioning of primary caregivers of children with menkes disease. Journal of Clinical Medicine, 12:1769, Feb 2023. URL: https://doi.org/10.3390/jcm12051769, doi:10.3390/jcm12051769. This article has 8 citations.

14. (rozensztrauch2023healthrelatedqualityof pages 4-5): Anna Rozensztrauch, Izabela Dzien, and Robert Śmigiel. Health-related quality of life and family functioning of primary caregivers of children with menkes disease. Journal of Clinical Medicine, 12:1769, Feb 2023. URL: https://doi.org/10.3390/jcm12051769, doi:10.3390/jcm12051769. This article has 8 citations.

15. (vairo2019asystematicreview pages 6-10): Filippo Pinto e Vairo, Bruna Cristine Chwal, Silvana Perini, Maria Angélica Pires Ferreira, Ana Carolina de Freitas Lopes, and Jonas Alex Morales Saute. A systematic review and evidence-based guideline for diagnosis and treatment of menkes disease. Molecular genetics and metabolism, 126 1:6-13, Jan 2019. URL: https://doi.org/10.1016/j.ymgme.2018.12.005, doi:10.1016/j.ymgme.2018.12.005. This article has 111 citations and is from a peer-reviewed journal.

16. (vairo2019asystematicreview pages 18-22): Filippo Pinto e Vairo, Bruna Cristine Chwal, Silvana Perini, Maria Angélica Pires Ferreira, Ana Carolina de Freitas Lopes, and Jonas Alex Morales Saute. A systematic review and evidence-based guideline for diagnosis and treatment of menkes disease. Molecular genetics and metabolism, 126 1:6-13, Jan 2019. URL: https://doi.org/10.1016/j.ymgme.2018.12.005, doi:10.1016/j.ymgme.2018.12.005. This article has 111 citations and is from a peer-reviewed journal.

17. (zhu2024brainandthe media f56ccfea): Juncheng Zhu, Yi Liao, Xuesheng Li, Fenglin Jia, Xinmao Ma, and Haibo Qu. Brain and the whole-body bone imaging appearances in menkes disease: a case report and literature review. BMC Pediatrics, Jun 2024. URL: https://doi.org/10.1186/s12887-024-04885-x, doi:10.1186/s12887-024-04885-x. This article has 4 citations and is from a peer-reviewed journal.

18. (zhu2024brainandthe media f2ce26df): Juncheng Zhu, Yi Liao, Xuesheng Li, Fenglin Jia, Xinmao Ma, and Haibo Qu. Brain and the whole-body bone imaging appearances in menkes disease: a case report and literature review. BMC Pediatrics, Jun 2024. URL: https://doi.org/10.1186/s12887-024-04885-x, doi:10.1186/s12887-024-04885-x. This article has 4 citations and is from a peer-reviewed journal.

19. (vairo2019asystematicreview pages 10-14): Filippo Pinto e Vairo, Bruna Cristine Chwal, Silvana Perini, Maria Angélica Pires Ferreira, Ana Carolina de Freitas Lopes, and Jonas Alex Morales Saute. A systematic review and evidence-based guideline for diagnosis and treatment of menkes disease. Molecular genetics and metabolism, 126 1:6-13, Jan 2019. URL: https://doi.org/10.1016/j.ymgme.2018.12.005, doi:10.1016/j.ymgme.2018.12.005. This article has 111 citations and is from a peer-reviewed journal.

20. (zhu2024brainandthe pages 4-6): Juncheng Zhu, Yi Liao, Xuesheng Li, Fenglin Jia, Xinmao Ma, and Haibo Qu. Brain and the whole-body bone imaging appearances in menkes disease: a case report and literature review. BMC Pediatrics, Jun 2024. URL: https://doi.org/10.1186/s12887-024-04885-x, doi:10.1186/s12887-024-04885-x. This article has 4 citations and is from a peer-reviewed journal.

21. (haddad2018cerebrospinalfluiddirectedraav9rsatp7a pages 1-2): Marie Reine Haddad, Eun-Young Choi, Patricia M. Zerfas, Ling Yi, Diego Martinelli, Patricia Sullivan, David S. Goldstein, Jose A. Centeno, Lauren R. Brinster, Martina Ralle, and Stephen G. Kaler. Cerebrospinal fluid-directed raav9-rsatp7a plus subcutaneous copper histidinate advance survival and outcomes in a menkes disease mouse model. Molecular Therapy - Methods &amp; Clinical Development, 10:165-178, Sep 2018. URL: https://doi.org/10.1016/j.omtm.2018.07.002, doi:10.1016/j.omtm.2018.07.002. This article has 39 citations.

22. (NCT00001262 chunk 1):  Copper Histidine Therapy for Menkes Diseases. Eunice Kennedy Shriver National Institute of Child Health and Human Development (NICHD). 1990. ClinicalTrials.gov Identifier: NCT00001262

23. (NCT00811785 chunk 1):  Molecular Bases of Response to Copper Treatment in Menkes Disease, Related Phenotypes, and Unexplained Copper Deficiency. Cyprium Therapeutics, Inc.. 2009. ClinicalTrials.gov Identifier: NCT00811785

24. (NCT04074512 chunk 1):  Copper Histidinate Treatment for Menkes Disease. Sentynl Therapeutics, Inc.. ClinicalTrials.gov Identifier: NCT04074512

25. (feyter2023atp7a‐relatedcoppertransport pages 27-31): S. De Feyter, A. Beyens, and B. Callewaert. <scp><i>atp7a</i></scp>‐related copper transport disorders: a systematic review and definition of the clinical subtypes. Journal of Inherited Metabolic Disease, 46:163-173, Feb 2023. URL: https://doi.org/10.1002/jimd.12590, doi:10.1002/jimd.12590. This article has 27 citations and is from a peer-reviewed journal.
