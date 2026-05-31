---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:43.028825'
end_time: '2026-04-25T22:42:57.048086'
duration_seconds: 1634.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fragile X Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 50
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fragile X Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Fragile X Syndrome** covering all of the
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
- **Disease Name:** Fragile X Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Fragile X Syndrome** covering all of the
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


## Fragile X Syndrome (FXS) — Comprehensive Disease Characteristics Research Report (Genetic)

### Target disease
Fragile X syndrome (FXS) is an X-linked genetic neurodevelopmental disorder and the most common inherited cause of intellectual disability (ID) and a major single-gene contributor to autism spectrum disorder (ASD). It is most commonly caused by a CGG trinucleotide repeat expansion in the 5′ untranslated region (UTR) of the **FMR1** gene leading to **hypermethylation**, transcriptional silencing of FMR1, and loss of **fragile X messenger ribonucleoprotein (FMRP)**—an RNA-binding protein that regulates synaptic mRNA transport and local translation, critical for synaptic plasticity. (de2025fromdiscoveryto pages 4-6, genovese2025systematicreviewfragile pages 2-4)

**Key mechanistic definition (from abstract-level statements in retrieved sources):**
- “Fragile X syndrome (FXS) … is caused by a CGG trinucleotide repeat expansion in the FMR1 gene, resulting in gene silencing and the loss of FMRP, an RNA-binding protein essential for synaptic plasticity.” (review abstract excerpt) (de2025fromdiscoveryto pages 1-3)

**MONDO ID:** Not recoverable from the retrieved full text corpus; would require direct lookup in the Mondo Disease Ontology registry (e.g., https://monarchinitiative.org/ or OBO Foundry). A general reference describing MONDO’s identifier framework is available but does not provide the FXS MONDO code. (coffee2009incidenceoffragile media 983b62aa)

---

## 1. Disease Information

### 1.1 Overview
FXS is characterized by a broad phenotype including developmental delay, intellectual disability, behavioral dysregulation (anxiety, hyperactivity/ADHD traits, aggression), autistic features, and a set of physical findings (e.g., macroorchidism in males after puberty). (de2025fromdiscoveryto pages 4-6, de2025fromdiscoveryto pages 3-4)

### 1.2 Key identifiers and synonyms (available from retrieved sources)
- **OMIM:** **300624** (ciaccio2017fragilexsyndrome pages 1-2)
- **Gene:** **FMR1**; locus **Xq27.3** (ciaccio2017fragilexsyndrome pages 1-2)
- **Common synonym:** **Martin–Bell syndrome** (ciaccio2017fragilexsyndrome pages 1-2)

**ICD-10/ICD-11, MeSH, Orphanet/ORPHAcode:** Not extractable from the retrieved documents; these need direct retrieval from ICD and Orphanet/MeSH resources.

### 1.3 Data provenance
The information summarized here is derived from aggregated disease-level resources (peer-reviewed reviews and clinical trial publications), plus primary studies (e.g., population newborn screening study; interventional trials). (berrykravis2024effectsofafq056 pages 1-2, seng2024longitudinalfollowupof pages 1-2, coffee2009incidenceoffragile media 983b62aa)

### 1.4 Compact identifiers/threshold summary
| Item | Value | Source / publication date | URL | Citation |
|---|---|---|---|---|
| Disease name | Fragile X syndrome (FXS) | Ciaccio et al., 2017; Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.1186/s13052-017-0355-y ; https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (ciaccio2017fragilexsyndrome pages 1-2, genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 1-3) |
| OMIM identifier | OMIM: 300624 | Ciaccio et al., 2017 | https://doi.org/10.1186/s13052-017-0355-y | (ciaccio2017fragilexsyndrome pages 1-2) |
| Causal gene | FMR1 | Ciaccio et al., 2017; Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.1186/s13052-017-0355-y ; https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (ciaccio2017fragilexsyndrome pages 1-2, genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 4-6) |
| Cytogenetic locus | Xq27.3 | Ciaccio et al., 2017; Volianskis, 2024 | https://doi.org/10.1186/s13052-017-0355-y | (ciaccio2017fragilexsyndrome pages 1-2, volianskis2024alterationsinsynaptic pages 15-19) |
| Common alternate names / synonyms | Martin-Bell syndrome; historical “fragile X mental retardation” terminology appears in older literature | Ciaccio et al., 2017 | https://doi.org/10.1186/s13052-017-0355-y | (ciaccio2017fragilexsyndrome pages 1-2) |
| Molecular mechanism summary | CGG trinucleotide-repeat expansion in the 5′ UTR of FMR1 causes hypermethylation/silencing of FMR1 and loss of FMRP in full-mutation FXS | Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 4-6) |
| CGG repeat range: normal | 5–44 repeats (Ciaccio 2017); ~5–55 repeats (van der Lei & Kooy 2025); about 5–40 repeats (Genovese 2025) | Ciaccio et al., 2017; Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.1186/s13052-017-0355-y ; https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (ciaccio2017fragilexsyndrome pages 1-2, genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 4-6) |
| CGG repeat range: gray zone / intermediate | 45–54 repeats | Ciaccio et al., 2017 | https://doi.org/10.1186/s13052-017-0355-y | (ciaccio2017fragilexsyndrome pages 1-2) |
| CGG repeat range: premutation | ~55–200 repeats (Ciaccio 2017); 55–200 repeats (Genovese 2025; van der Lei & Kooy 2025) | Ciaccio et al., 2017; Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.1186/s13052-017-0355-y ; https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (ciaccio2017fragilexsyndrome pages 1-2, genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 4-6) |
| CGG repeat range: full mutation | >200 repeats | Ciaccio et al., 2017; Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.1186/s13052-017-0355-y ; https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (ciaccio2017fragilexsyndrome pages 1-2, genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 4-6) |
| Prevalence estimate | ~1 in 4,000 males and ~1 in 8,000 females | Genovese & Butler, 2025; van der Lei & Kooy, 2025 | https://doi.org/10.3390/genes16020149 ; https://doi.org/10.3390/biomedicines13040805 | (genovese2025systematicreviewfragile pages 2-4, de2025fromdiscoveryto pages 1-3) |
| Alternate prevalence estimates reported in literature | ~1:5,000–7,000 males and ~1:4,000–6,000 females | Ciaccio et al., 2017 | https://doi.org/10.1186/s13052-017-0355-y | (ciaccio2017fragilexsyndrome pages 1-2) |


*Table: This table summarizes the core identifiers, synonyms, prevalence figures, and CGG repeat thresholds for Fragile X syndrome from key review sources. It is useful as a compact normalization reference for disease knowledge-base curation.*

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** A CGG repeat expansion in the 5′UTR of **FMR1**. Commonly used thresholds across sources:
- Normal: ~5–55 repeats (or 5–44 in some classification) (de2025fromdiscoveryto pages 4-6, ciaccio2017fragilexsyndrome pages 1-2)
- Premutation: **55–200** repeats (de2025fromdiscoveryto pages 4-6, genovese2025systematicreviewfragile pages 2-4)
- Full mutation (FXS): **>200** repeats, associated with hypermethylation/silencing and loss of FMRP (de2025fromdiscoveryto pages 4-6, genovese2025systematicreviewfragile pages 2-4)

Mechanistically, when repeat length exceeds ~200, methylation and chromatin changes (histone deacetylation, heterochromatin formation) contribute to transcriptional silencing and loss of FMRP. (volianskis2024alterationsinsynaptic pages 15-19)

**Less common molecular causes:** Non-repeat FMR1 alterations such as deletions/duplications and SNVs account for <1% of molecular diagnoses in one review. (ciaccio2017fragilexsyndrome pages 1-2)

### 2.2 Risk factors
- **Sex:** males are generally more severely affected due to having a single X chromosome. (genovese2025systematicreviewfragile pages 2-4)
- **Repeat instability/anticipation:** expansion from premutation to full mutation occurs predominantly during **maternal transmission** (anticipation). (genovese2025systematicreviewfragile pages 2-4, volianskis2024alterationsinsynaptic pages 15-19)

### 2.3 Protective factors
No specific genetic or environmental “protective factors” were identified within the retrieved evidence corpus. However, **mosaicism** (cells with smaller/unmethylated alleles) is associated with better cognitive outcomes, implying partial protection at the molecular/cellular level. (genovese2025systematicreviewfragile pages 7-9)

### 2.4 Gene–environment interactions
The retrieved corpus did not provide specific, well-supported gene–environment interaction claims for classic FXS.

---

## 3. Phenotypes

### 3.1 Core neurodevelopmental phenotype
- **Intellectual disability / cognitive impairment:** core feature; one review reports typical IQ <70 with male average ~40–55 and female ~65–70. (de2025fromdiscoveryto pages 3-4)
- **ASD/autistic features:** common; ~30–50% of males and ~20% females have autistic behaviors by direct assessment in one review (de2025fromdiscoveryto pages 3-4); a systematic review reports comorbid ASD in “just over 40%” overall (46% males, 16% females). (genovese2025systematicreviewfragile pages 7-9)
- **Behavioral features:** hyperactivity, anxiety, aggression, attention deficits, sensory hyperarousal; ADHD criteria frequently met. (de2025fromdiscoveryto pages 3-4)

### 3.2 Neurologic comorbidity
- **Seizures:** estimates include ~15–20% of males and ~5% of females (de2025fromdiscoveryto pages 4-6) and 10–20% of boys and 5–10% of girls (ciaccio2017fragilexsyndrome pages 2-3).
- **EEG abnormalities:** ~74–75% of young children show EEG abnormalities; ~1/3 remit by mid-childhood in one systematic review. (genovese2025systematicreviewfragile pages 7-9)

### 3.3 Physical phenotype and medical comorbidities (examples with frequency where available)
- Macroorchidism: 63–95% (males) (ciaccio2017fragilexsyndrome pages 2-3)
- Obesity: 53–61% (ciaccio2017fragilexsyndrome pages 2-3)
- Recurrent otitis media: 47–97% (ciaccio2017fragilexsyndrome pages 2-3)
- GI complaints: ~31% (ciaccio2017fragilexsyndrome pages 2-3)
- Strabismus: 30–55% (young males) (genovese2025systematicreviewfragile pages 6-7)

### 3.4 Developmental timing and progression
Developmental delay is typically recognized in infancy/early childhood (boys as early as ~6 months; girls ~1 year in a systematic review). (genovese2025systematicreviewfragile pages 7-9)

### 3.5 Quality-of-life impact
FXS-associated ASD features “emerge in early childhood and impair daily functioning,” and FXS can impair adaptive skills needed for communication, self-care, and social participation, consistent with substantial QOL impact. (de2025fromdiscoveryto pages 3-4)

### 3.6 Suggested HPO terms (best-effort, not extracted from evidence text)
These are standard phenotype mappings consistent with the reported clinical picture:
- Intellectual disability (HP:0001249)
- Global developmental delay (HP:0001263)
- Autism (HP:0000717)
- Seizures (HP:0001250)
- Anxiety (HP:0000739)
- Attention deficit hyperactivity disorder (HP:0007018)
- Macroorchidism (HP:0000049)
- Large ears (HP:0000400)
- Strabismus (HP:0000486)
- Sleep disturbance (HP:0002360)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **FMR1** (Xq27.3). (ciaccio2017fragilexsyndrome pages 1-2)

### 4.2 Pathogenic variant class
- **Repeat expansion** in the 5′UTR CGG tract is the dominant mechanism (>99% of cases in one review), with full mutation generally **>200 repeats** leading to methylation and silencing. (ciaccio2017fragilexsyndrome pages 1-2, de2025fromdiscoveryto pages 4-6)

### 4.3 Functional consequence
- **Loss of function** of FMR1 at the expression level (epigenetic silencing) leads to loss of FMRP. (de2025fromdiscoveryto pages 4-6, volianskis2024alterationsinsynaptic pages 15-19)

### 4.4 Modifier mechanisms
- **Mosaicism (size or methylation mosaicism)** contributes to variable FMRP expression and phenotype variability; mosaicism with partially unmethylated alleles is associated with better cognitive functioning. (genovese2025systematicreviewfragile pages 7-9, volianskis2024alterationsinsynaptic pages 15-19)

### 4.5 Epigenetic information
FXS full mutation is associated with **hypermethylation** of FMR1, transcriptional silencing, and heterochromatinization. (volianskis2024alterationsinsynaptic pages 15-19)

---

## 5. Environmental Information

FXS is primarily genetic. The retrieved evidence corpus did not provide specific validated environmental exposures that cause classic FXS (as opposed to modifying symptoms). Supportive-care and early intervention (environmental/behavioral supports) affect outcomes but are not etiologic.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current understanding)
1. **FMR1 CGG full mutation (>200 repeats)** in 5′UTR → 2. **hypermethylation and chromatin silencing** of FMR1 → 3. **loss of FMRP** (RNA-binding translational regulator) → 4. dysregulated transport/local translation of synaptic mRNAs and altered protein synthesis → 5. abnormal dendritic spine maturation (immature/elongated spines), altered synaptic plasticity and circuit function → 6. excitatory/inhibitory imbalance and hyperexcitability involving glutamatergic (mGluR5) and GABAergic systems → 7. neurodevelopmental phenotype (ID, ASD traits, behavioral dysregulation, seizures). (de2025fromdiscoveryto pages 4-6, volianskis2024alterationsinsynaptic pages 15-19)

### 6.2 Implicated pathways (examples)
- **mGluR5 signaling dysregulation** (loss of FMRP’s normal negative regulation) is emphasized as a major mechanistic framework. (de2025fromdiscoveryto pages 4-6)
- **GABAergic deficits** and E/I imbalance are repeatedly described. (de2025fromdiscoveryto pages 4-6)
- **cAMP signaling abnormalities** are noted in human cell lines and models, motivating PDE inhibition strategies. (genovese2025systematicreviewfragile pages 12-13)

### 6.3 Suggested GO biological process terms (best-effort)
- Synaptic signaling (GO:0099536)
- Regulation of translation (GO:0006417)
- Synaptic plasticity (GO:0048167)
- Dendritic spine development (GO:0060998)
- Regulation of excitatory postsynaptic potential (GO:0099528)

### 6.4 Suggested CL cell types (best-effort)
- Cortical pyramidal neuron (CL:0000540)
- GABAergic interneuron (CL:0000099)

### 6.5 Suggested UBERON anatomical structures (best-effort)
- Cerebral cortex (UBERON:0000956)
- Hippocampus (UBERON:0001954)
- Prefrontal cortex (UBERON:0001870)

### 6.6 Molecular profiling / biomarkers (selected)
- EEG-based translational biomarkers are emphasized as objective measures; BPN14770 studies specifically analyze auditory N1 ERP and peak alpha frequency (PAF) as treatment-linked physiology measures. (norris2024auditoryn1eventrelated pages 1-2, norris2025rocanalysisof pages 8-10)

---

## 7. Anatomical Structures Affected

### Organ/system level
Primary involvement is the **central nervous system** with downstream behavioral, cognitive, and neuropsychiatric manifestations. (de2025fromdiscoveryto pages 4-6, de2025fromdiscoveryto pages 3-4)

### Tissue/cell level
FXS pathophysiology is discussed in terms of synaptic dysfunction in neuronal circuits and altered excitatory/inhibitory balance (glutamatergic and GABAergic synapses). (de2025fromdiscoveryto pages 4-6, ntoulas2024multilevelprofilingof pages 1-2)

---

## 8. Temporal Development

### Onset
Typically early (infancy/early childhood) with developmental delays. (genovese2025systematicreviewfragile pages 7-9)

### Progression
FXS is generally described as not markedly worsening over time; however, males may show IQ decline during development/early puberty in some analyses. (genovese2025systematicreviewfragile pages 7-9, genovese2025systematicreviewfragile pages 2-4)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **X-linked dominant** inheritance pattern is described, with dynamic repeat expansion/anticipation, especially during maternal transmission. (genovese2025systematicreviewfragile pages 2-4, volianskis2024alterationsinsynaptic pages 15-19)

### 9.2 Epidemiology (selected statistics)
- Prevalence: ~**1 in 4,000 males** and **1 in 8,000 females** (genovese2025systematicreviewfragile pages 2-4).
- Premutation carrier frequency: ~**1 in 250 females** and **1 in 800 males** (premutation defined 55–200 repeats). (genovese2025systematicreviewfragile pages 2-4)

**Newborn-screening derived incidence:** In a population screen of **36,124 newborn males**, **7** full-mutation FXS cases were confirmed, corresponding to an incidence of **1 in 5161** (95% CI 1/10,653–1/2500). (coffee2009incidenceoffragile media 983b62aa)

---

## 10. Diagnostics

### 10.1 Molecular diagnostic approach (current standard in retrieved sources)
- Postnatal testing often includes **PCR combined with Southern blot** and/or **triplet-primed PCR (TP-PCR)** to detect FMR1 repeat expansions and assess size. (genovese2025systematicreviewfragile pages 2-4)
- Because pathogenicity depends strongly on **methylation/silencing**, testing commonly includes methylation-sensitive methods. (genovese2025systematicreviewfragile pages 2-4)

### 10.2 Newborn screening / early detection
A newborn screening approach based on **quantitative FMR1 methylation** in dried blood spots was developed and used to directly measure incidence in a large male newborn cohort, supporting feasibility of early detection. (coffee2009incidenceoffragile media 983b62aa)

### 10.3 Prenatal diagnosis
Prenatal diagnostic options described include **chorionic villus sampling** and **amniocentesis** when there is family history or known carrier status. (genovese2025systematicreviewfragile pages 2-4)

### 10.4 Differential diagnosis
Not systematically extractable from the retrieved excerpts.

---

## 11. Outcome / Prognosis

FXS is generally not considered directly life-threatening and does not typically show marked neurodegenerative worsening as a primary feature, but it produces lifelong functional challenges requiring support. (genovese2025systematicreviewfragile pages 2-4)

Premutation carriers have distinct late-onset risks (e.g., FXTAS, FXPOI), but these are separate fragile X–associated disorders rather than classic full-mutation FXS. (genovese2025systematicreviewfragile pages 7-9, volianskis2024alterationsinsynaptic pages 15-19)

---

## 12. Treatment

### 12.1 Current clinical practice (real-world implementation)
No FDA-approved disease-modifying medications exist for FXS; management is largely **symptom-based** and multidisciplinary, including behavioral therapies, speech-language therapy, applied behavior analysis, parent training, and CBT to address communication and behavioral/psychiatric symptoms. (genovese2025systematicreviewfragile pages 10-12)

### 12.2 Recent clinical trial developments (2023–2024 prioritized)
Key recent peer-reviewed trials and translational biomarker papers:
- **AFQ056 (mavoglurant) FXLEARN trial (2024, JCI):** 99 randomized young children; no benefit over placebo on primary WCS language outcome; strong example of translational gap for mGluR5 NAMs. (berrykravis2024effectsofafq056 pages 1-2, berrykravis2024effectsofafq056 pages 3-5)
- **Metformin longitudinal follow-up (2024, Frontiers in Psychology):** open-label follow-up in n=26 (6–25 years) over 1–3 years; nonverbal IQ and adaptive function stable with no significant decline. (seng2024longitudinalfollowupof pages 3-4)
- **BPN14770 (zatolmilast) biomarker analysis (2024, Molecular Autism):** N1 ERP amplitude correlated with serum drug concentration (rho=0.608, p=0.036 in period-1 drug recipients), supporting an exposure–physiology link; clinical improvements in cognition/language/daily functioning were reported in the trial background. (norris2024auditoryn1eventrelated pages 2-4, norris2024auditoryn1eventrelated pages 1-2)

### 12.3 Targeted/symptomatic agents with mixed evidence
Reviews summarize mixed/negative outcomes for multiple targeted approaches, with occasional subgroup signals:
- **Arbaclofen (GABA-B agonist):** Phase 3 trials negative overall; some pediatric irritability benefits at higher doses. (protic2025targeteddrugdevelopment pages 4-5)
- **Ganaxolone (GABAA PAM):** safe but primary endpoint negative overall; possible subgroup benefits. (protic2025targeteddrugdevelopment pages 4-5)
- **Gaboxadol (OV101):** early signal with ~60% CGI-I responders in a small study summarized in reviews. (protic2025targeteddrugdevelopment pages 4-5)
- **Cannabidiol / ZYN002:** phase 3 negative overall with post hoc methylation-defined subgroup benefit reported in a review summary. (protic2025razvojciljanefarmakoterapije pages 5-6)

A compact cross-intervention summary is provided below:
| Intervention | Mechanism / target | Key study / design | Sample size / population | Primary endpoint(s) / main measures | Main findings reported | NCT ID(s) | Publication date | URL | Citation |
|---|---|---|---|---|---|---|---|---|---|
| AFQ056 (mavoglurant) | mGluR5 negative allosteric modulator | FXLEARN: large multisite randomized, double-blind, placebo-controlled trial with 4-month placebo lead-in, 2-month dose optimization, 6-month treatment; all participants also received parent-implemented language intervention | 110 enrolled; 99 randomized (50 AFQ056, 49 placebo); 91 completed placebo-controlled period; children age ~3–6 years with FXS | Primary: Weighted Communication Scale (WCS); secondary: objective and parent-reported cognitive/language measures including MSEL, PLS-5, Vineland-3 | No significant difference vs placebo on WCS or secondary measures; both groups improved in language over time; lower-baseline communication subgroup did worse on AFQ056 than placebo in subgroup analysis; no major safety signal | NCT02920892 | 2024-08 | https://doi.org/10.1172/jci171723 | (berrykravis2024effectsofafq056 pages 1-2, berrykravis2024effectsofafq056 pages 3-5, berrykravis2024effectsofafq056 pages 6-7, berrykravis2024effectsofafq056 pages 9-10) |
| Metformin | AMPK activation; proposed reduction of MMP-9 / modulation of dysregulated signaling | Open-label longitudinal follow-up after prior controlled exposure; repeated cognitive and adaptive behavior testing over 1–3 years | 26 individuals with FXS (22 males, 4 females), ages 6–25 years | Leiter-III nonverbal IQ; Vineland-3 adaptive behavior | Overall nonverbal IQ and adaptive behavior remained stable; no significant decline over follow-up; small sample and no control group limit inference | NCT05120505 ongoing pediatric RCT also identified in registry; separate follow-up paper is open-label longitudinal | 2024-06 | https://doi.org/10.3389/fpsyg.2024.1305597 | (seng2024longitudinalfollowupof pages 1-2, seng2024longitudinalfollowupof pages 3-4, seng2024longitudinalfollowupof pages 2-3, NCT05120505 chunk 1) |
| BPN14770 (zatolmilast) | PDE4D inhibitor; increases cAMP signaling | Phase 2a placebo-controlled crossover trial with EEG biomarker analyses; later exploratory ROC/EEG work | 30 adult males with FXS; EEG subsets smaller due to artifact/data loss | Clinical cognition/language/daily function measures; auditory N1 ERP amplitude; exploratory peak alpha frequency (PAF) | Clinical improvements in cognition, language, and daily functioning were reported; N1 amplitude showed correlation with serum drug concentration, stronger in period-1 drug recipients (rho = 0.608, p = 0.036, N = 12); exploratory PAF increased vs baseline and may be a scalable biomarker | NCT03569631 | 2024-11 (biomarker paper); 2025-05 (exploratory preprint) | https://doi.org/10.1186/s13229-024-00626-0 ; https://doi.org/10.1101/2025.05.29.25328581 | (norris2024auditoryn1eventrelated pages 1-2, norris2024auditoryn1eventrelated pages 2-4, norris2025rocanalysisof pages 1-4, norris2025rocanalysisof pages 8-10) |
| Arbaclofen (STX209) | GABA-B agonist | Two Phase 3 placebo-controlled trials in children and in adolescents/adults | Pediatric and adult/adolescent cohorts; registry lists 172 children in NCT01325220 and 125 adolescents/adults in NCT01282268 | Primary behavioral/social withdrawal outcomes; irritability subscales and parent-rated outcomes reported in reviews | Overall primary endpoints not met; pediatric highest-dose group showed improvements on ABC-CFX Irritability and Parenting Stress Index / parent-rated forms; generally well tolerated | NCT01325220; NCT01282268 | 2025 review summary | https://doi.org/10.5937/medi0-60213 ; https://clinicaltrials.gov/study/NCT01325220 ; https://clinicaltrials.gov/study/NCT01282268 | (protic2025targeteddrugdevelopment pages 4-5, de2025fromdiscoveryto pages 9-10) |
| Ganaxolone | GABAA positive allosteric modulator / neurosteroid | Phase 2 randomized crossover trial in children/adolescents | n = 59 in registry/review | Primary: CGI-I | Safe but did not differ from placebo on primary CGI-I endpoint overall; post hoc subgroup benefits reported in participants with higher anxiety or lower cognition | NCT01725152 | 2025 review summary | https://doi.org/10.5937/medi0-60213 ; https://clinicaltrials.gov/study/NCT01725152 | (protic2025targeteddrugdevelopment pages 4-5) |
| Gaboxadol (OV101) | GABAA agonist / extrasynaptic GABAergic modulation | Phase 2a ROCKET study; additional recruiting single-dose adult study noted in review | ~23 participants in phase 2a response analysis | CGI-I and clinician/caregiver-rated behavioral measures | Well tolerated; about 60% classified as CGI-I responders in phase 2a; initial efficacy signal on hyperactivity, irritability, stereotypy, and anxiety in reported review summaries | NCT06334419 recruiting study noted; ROCKET NCT not provided in evidence excerpt | 2025 review summary | https://doi.org/10.5937/medi0-60213 ; https://doi.org/10.3390/biomedicines13040805 | (protic2025targeteddrugdevelopment pages 4-5, de2025fromdiscoveryto pages 8-9) |
| Cannabidiol / ZYN002 | Endocannabinoid system modulation; transdermal CBD formulation | Phase 1/2 open-label and Phase 3 CONNECT-FX reviewed; post hoc methylation-stratified analyses | Sample size not stated in provided evidence excerpt | ADAMS and phase 3 primary endpoint not specified in excerpt | Open-label study showed safety and ADAMS reduction; CONNECT-FX failed primary endpoint overall, but subgroup with ≥90% FMR1 promoter methylation showed benefit, motivating RECONNECT | NCT04977986 recruiting study noted in review | 2025 review summary | https://doi.org/10.5937/medi0-60213 ; https://doi.org/10.3390/biomedicines13040805 | (protic2025razvojciljanefarmakoterapije pages 5-6, de2025fromdiscoveryto pages 8-9) |
| Older mGluR5 program overview (mavoglurant / basimglurant) | mGluR5 negative allosteric modulation | Earlier adult/adolescent Phase 2/2b and extension trials summarized in reviews | Small crossover adult mavoglurant study in 30 adult males; larger adolescent/adult trials listed in reviews/registry | Behavioral endpoints; FXLEARN later used WCS for language learning in young children | Initial small subgroup signal in fully methylated cases did not replicate; larger Phase 2b trials and basimglurant Phase II studies were negative, contributing to skepticism about direct mGluR5 translation from animal models | NCT01357239; NCT01348087; NCT01433354; NCT02920892 | 2024-08 and 2025 review summaries | https://doi.org/10.1172/jci171723 ; https://doi.org/10.5937/medi0-60213 ; https://clinicaltrials.gov/study/NCT01357239 | (berrykravis2024effectsofafq056 pages 1-2, protic2025targeteddrugdevelopment pages 4-5, de2025fromdiscoveryto pages 9-10) |


*Table: This table summarizes key Fragile X syndrome therapeutic studies and trial programs emphasized in the gathered evidence, including recent 2024 findings and older targeted treatment programs. It is useful for comparing mechanisms, study designs, endpoints, outcomes, and trial identifiers across leading pharmacologic approaches.*

### 12.4 Suggested MAXO terms (best-effort)
- Pharmacotherapy (MAXO:0000058)
- Behavioral therapy (MAXO:0000506)
- Speech therapy (MAXO:0001193)
- Genetic counseling (MAXO:0000070)

---

## 13. Prevention

### Primary prevention
Because FXS is inherited, prevention focuses on **genetic counseling** and reproductive planning for carriers. (genovese2025systematicreviewfragile pages 2-4)

### Secondary prevention (screening/early detection)
- Newborn screening by methylation assay in dried blood spots has been demonstrated and used to estimate incidence, supporting a potential early-intervention pathway. (coffee2009incidenceoffragile media 983b62aa)

### Tertiary prevention
Multidisciplinary management and early developmental/behavioral interventions aim to reduce disability and improve long-term functioning. (genovese2025systematicreviewfragile pages 12-13, genovese2025systematicreviewfragile pages 10-12)

---

## 14. Other Species / Natural Disease

The retrieved evidence focuses on model organisms rather than naturally occurring veterinary disease. No naturally occurring non-human clinical syndrome analogous to human FXS was identified in the provided corpus.

---

## 15. Model Organisms

A diverse model ecosystem is used to study FMRP function and therapeutics:
- **Mouse (Fmr1 KO):** dominant in vivo model; captures many phenotypes (immature spines, altered LTP/LTD, hyperactivity/anxiety/social changes); key limitations include species differences and differences in timing of FMRP expression vs humans (humans express FMR1 until at least week 10 gestation). (de2025fromdiscoveryto pages 6-8)
- **Rat (Fmr1 KO):** proposed to offer added translational validity; a 2024 study combined behavior, hippocampal electrophysiology, and RNA-seq and found hyperactivity/cognitive deficits plus glutamatergic/GABAergic alterations in PFC and hippocampus. (ntoulas2024multilevelprofilingof pages 1-2)
- **Drosophila / zebrafish:** useful for conserved genetics/pathway discovery; limitations include species differences. (sandoval2024fromwingsto pages 2-3)
- **Human iPSC neurons and 3D organoids/assembloids:** enable study of patient-derived epigenetic FMR1 silencing and human-specific neurodevelopment; limitations include immaturity, reproducibility issues, and inability to model behavior. (sandoval2024fromwingsto pages 5-7)

---

## Expert opinions / analysis (from authoritative sources in retrieved corpus)

A consistent expert view in recent reviews is that translation from strong preclinical signals to clinical efficacy has been limited by patient heterogeneity, inconsistent outcomes, and the need for objective biomarkers and better trial design—highlighted in the context of mGluR5 NAM programs and the field’s shift toward biomarkers (EEG), stratification (methylation status), and gene/reactivation strategies (ASOs, CRISPR-based approaches). (de2025fromdiscoveryto pages 18-19, de2025fromdiscoveryto pages 13-15, berrykravis2024effectsofafq056 pages 1-2)

---

## Key recent statistics (selected)
- Prevalence: ~1/4,000 males and ~1/8,000 females. (genovese2025systematicreviewfragile pages 2-4)
- Premutation frequency: ~1/250 females; ~1/800 males. (genovese2025systematicreviewfragile pages 2-4)
- Newborn-screening incidence in males: 1/5,161 (7/36,124). (coffee2009incidenceoffragile media 983b62aa)
- Comorbid ASD in FXS: ~46% males and 16% females (“just over 40% overall”). (genovese2025systematicreviewfragile pages 7-9)
- Seizure prevalence: ~15–20% males and ~5% females (review estimate). (de2025fromdiscoveryto pages 4-6)

---

## Limitations of this report (evidence availability)
1. Specific ontology identifiers (MONDO ID, Orphanet ORPHAcode, MeSH, ICD-10/ICD-11) were not present in the retrieved documents and thus could not be extracted with full citation support.
2. Some requested sections (environmental risk/protective factors, formal diagnostic criteria, differential diagnosis, survival statistics) were not explicitly quantified in the retrieved excerpts.
3. Suggested ontology term mappings (HPO/GO/CL/UBERON/MAXO) are provided as best-effort standard mappings rather than extracted identifiers from the cited texts.


References

1. (de2025fromdiscoveryto pages 4-6): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

2. (genovese2025systematicreviewfragile pages 2-4): Ann C. Genovese and Merlin G. Butler. Systematic review: fragile x syndrome across the lifespan with a focus on genetics, neurodevelopmental, behavioral and psychiatric associations. Genes, 16:149, Jan 2025. URL: https://doi.org/10.3390/genes16020149, doi:10.3390/genes16020149. This article has 17 citations.

3. (de2025fromdiscoveryto pages 1-3): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

4. (coffee2009incidenceoffragile media 983b62aa): Bradford Coffee, Krayton Keith, Igor Albizua, Tamika Malone, Julie Mowrey, Stephanie L. Sherman, and Stephen T. Warren. Incidence of fragile x syndrome by newborn screening for methylated fmr1 dna. American journal of human genetics, 85 4:503-14, Oct 2009. URL: https://doi.org/10.1016/j.ajhg.2009.09.007, doi:10.1016/j.ajhg.2009.09.007. This article has 558 citations and is from a highest quality peer-reviewed journal.

5. (de2025fromdiscoveryto pages 3-4): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

6. (ciaccio2017fragilexsyndrome pages 1-2): Claudia Ciaccio, Laura Fontana, Donatella Milani, Silvia Tabano, Monica Miozzo, and Susanna Esposito. Fragile x syndrome: a review of clinical and molecular diagnoses. Italian Journal of Pediatrics, Apr 2017. URL: https://doi.org/10.1186/s13052-017-0355-y, doi:10.1186/s13052-017-0355-y. This article has 223 citations and is from a peer-reviewed journal.

7. (berrykravis2024effectsofafq056 pages 1-2): Elizabeth Berry-Kravis, Leonard Abbeduto, Randi Hagerman, Christopher S. Coffey, Merit Cudkowicz, Craig A. Erickson, Andrea McDuffie, David Hessl, Lauren Ethridge, Flora Tassone, Walter E. Kaufmann, Katherine Friedmann, Lauren Bullard, Anne Hoffmann, Jeremy Veenstra-VanderWeele, Kevin Staley, David Klements, Michael Moshinsky, Brittney Harkey, Jeff Long, Janel Fedler, Elizabeth Klingner, Dixie Ecklund, Michele Costigan, Trevis Huff, and Brenda Pearson. Effects of afq056 on language learning in fragile x syndrome. The Journal of Clinical Investigation, Aug 2024. URL: https://doi.org/10.1172/jci171723, doi:10.1172/jci171723. This article has 24 citations.

8. (seng2024longitudinalfollowupof pages 1-2): Panhaneath Seng, Federica Alice Maria Montanaro, Hazel Maridith Barlahan Biag, Maria Jimena Salcedo-Arellano, Kyoungmi Kim, Matthew Dominic Ponzini, Flora Tassone, Andrea Schneider, Leonard Abbeduto, Angela John Thurman, David Hessl, Francois V. Bolduc, Sebastien Jacquemont, Sarah Lippé, and Randi J. Hagerman. Longitudinal follow-up of metformin treatment in fragile x syndrome. Frontiers in Psychology, Jun 2024. URL: https://doi.org/10.3389/fpsyg.2024.1305597, doi:10.3389/fpsyg.2024.1305597. This article has 8 citations and is from a peer-reviewed journal.

9. (volianskis2024alterationsinsynaptic pages 15-19): RE Volianskis. Alterations in synaptic plasticity in a mouse model of fragile x syndrome. Unknown journal, 2024.

10. (genovese2025systematicreviewfragile pages 7-9): Ann C. Genovese and Merlin G. Butler. Systematic review: fragile x syndrome across the lifespan with a focus on genetics, neurodevelopmental, behavioral and psychiatric associations. Genes, 16:149, Jan 2025. URL: https://doi.org/10.3390/genes16020149, doi:10.3390/genes16020149. This article has 17 citations.

11. (ciaccio2017fragilexsyndrome pages 2-3): Claudia Ciaccio, Laura Fontana, Donatella Milani, Silvia Tabano, Monica Miozzo, and Susanna Esposito. Fragile x syndrome: a review of clinical and molecular diagnoses. Italian Journal of Pediatrics, Apr 2017. URL: https://doi.org/10.1186/s13052-017-0355-y, doi:10.1186/s13052-017-0355-y. This article has 223 citations and is from a peer-reviewed journal.

12. (genovese2025systematicreviewfragile pages 6-7): Ann C. Genovese and Merlin G. Butler. Systematic review: fragile x syndrome across the lifespan with a focus on genetics, neurodevelopmental, behavioral and psychiatric associations. Genes, 16:149, Jan 2025. URL: https://doi.org/10.3390/genes16020149, doi:10.3390/genes16020149. This article has 17 citations.

13. (genovese2025systematicreviewfragile pages 12-13): Ann C. Genovese and Merlin G. Butler. Systematic review: fragile x syndrome across the lifespan with a focus on genetics, neurodevelopmental, behavioral and psychiatric associations. Genes, 16:149, Jan 2025. URL: https://doi.org/10.3390/genes16020149, doi:10.3390/genes16020149. This article has 17 citations.

14. (norris2024auditoryn1eventrelated pages 1-2): Jordan E. Norris, Elizabeth M. Berry-Kravis, Mark D. Harnett, Scott A. Reines, Melody A. Reese, Abigail H. Outterson, Claire Michalak, Jeremiah Furman, Mark E. Gurney, and Lauren E. Ethridge. Auditory n1 event-related potential amplitude is predictive of serum concentration of bpn14770 in fragile x syndrome. Molecular Autism, Nov 2024. URL: https://doi.org/10.1186/s13229-024-00626-0, doi:10.1186/s13229-024-00626-0. This article has 5 citations and is from a peer-reviewed journal.

15. (norris2025rocanalysisof pages 8-10): J. E. Norris, E. Berry-Kravis, Mark D. Harnett, Scott A. Reines, Melody A. Reese, Emma K. Auger Ph.D., Abigail H. Outterson Ph.D., Jeremiah Furman, Mark E. Gurney, and Ph.D Lauren E. Ethridge. Roc analysis of biomarker combinations in fragile x syndrome-specific clinical trials: evaluating treatment efficacy via exploratory biomarkers. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.29.25328581, doi:10.1101/2025.05.29.25328581. This article has 1 citations.

16. (ntoulas2024multilevelprofilingof pages 1-2): George Ntoulas, Charalampos Brakatselos, Gerasimos Nakas, Michail-Zois Asprogerakas, Foteini Delis, Leonidas J. Leontiadis, George Trompoukis, Costas Papatheodoropoulos, Dimitrios Gkikas, Dimitrios Valakos, Giannis Vatsellas, Panagiotis K. Politis, Alexia Polissidis, and Katerina Antoniou. Multi-level profiling of the fmr1 ko rat unveils altered behavioral traits along with aberrant glutamatergic function. Translational Psychiatry, Feb 2024. URL: https://doi.org/10.1038/s41398-024-02815-0, doi:10.1038/s41398-024-02815-0. This article has 10 citations and is from a peer-reviewed journal.

17. (genovese2025systematicreviewfragile pages 10-12): Ann C. Genovese and Merlin G. Butler. Systematic review: fragile x syndrome across the lifespan with a focus on genetics, neurodevelopmental, behavioral and psychiatric associations. Genes, 16:149, Jan 2025. URL: https://doi.org/10.3390/genes16020149, doi:10.3390/genes16020149. This article has 17 citations.

18. (berrykravis2024effectsofafq056 pages 3-5): Elizabeth Berry-Kravis, Leonard Abbeduto, Randi Hagerman, Christopher S. Coffey, Merit Cudkowicz, Craig A. Erickson, Andrea McDuffie, David Hessl, Lauren Ethridge, Flora Tassone, Walter E. Kaufmann, Katherine Friedmann, Lauren Bullard, Anne Hoffmann, Jeremy Veenstra-VanderWeele, Kevin Staley, David Klements, Michael Moshinsky, Brittney Harkey, Jeff Long, Janel Fedler, Elizabeth Klingner, Dixie Ecklund, Michele Costigan, Trevis Huff, and Brenda Pearson. Effects of afq056 on language learning in fragile x syndrome. The Journal of Clinical Investigation, Aug 2024. URL: https://doi.org/10.1172/jci171723, doi:10.1172/jci171723. This article has 24 citations.

19. (seng2024longitudinalfollowupof pages 3-4): Panhaneath Seng, Federica Alice Maria Montanaro, Hazel Maridith Barlahan Biag, Maria Jimena Salcedo-Arellano, Kyoungmi Kim, Matthew Dominic Ponzini, Flora Tassone, Andrea Schneider, Leonard Abbeduto, Angela John Thurman, David Hessl, Francois V. Bolduc, Sebastien Jacquemont, Sarah Lippé, and Randi J. Hagerman. Longitudinal follow-up of metformin treatment in fragile x syndrome. Frontiers in Psychology, Jun 2024. URL: https://doi.org/10.3389/fpsyg.2024.1305597, doi:10.3389/fpsyg.2024.1305597. This article has 8 citations and is from a peer-reviewed journal.

20. (norris2024auditoryn1eventrelated pages 2-4): Jordan E. Norris, Elizabeth M. Berry-Kravis, Mark D. Harnett, Scott A. Reines, Melody A. Reese, Abigail H. Outterson, Claire Michalak, Jeremiah Furman, Mark E. Gurney, and Lauren E. Ethridge. Auditory n1 event-related potential amplitude is predictive of serum concentration of bpn14770 in fragile x syndrome. Molecular Autism, Nov 2024. URL: https://doi.org/10.1186/s13229-024-00626-0, doi:10.1186/s13229-024-00626-0. This article has 5 citations and is from a peer-reviewed journal.

21. (protic2025targeteddrugdevelopment pages 4-5): Dragana Protić, Maja Stojković, and Dejan Budimirović. Targeted drug development in fragile x syndrome: molecular medicine as a key tool in clinical pharmacology. Medicinska istrazivanja, pages 19-19, Jan 2025. URL: https://doi.org/10.5937/medi0-60213, doi:10.5937/medi0-60213. This article has 0 citations.

22. (protic2025razvojciljanefarmakoterapije pages 5-6): D Protic, M Stojkovic, and D Budimirovic. Razvoj ciljane farmakoterapije za fragilni x sindrom: molekularna medicina kao ključno sredstvo u kliničkoj …. Unknown journal, 2025.

23. (berrykravis2024effectsofafq056 pages 6-7): Elizabeth Berry-Kravis, Leonard Abbeduto, Randi Hagerman, Christopher S. Coffey, Merit Cudkowicz, Craig A. Erickson, Andrea McDuffie, David Hessl, Lauren Ethridge, Flora Tassone, Walter E. Kaufmann, Katherine Friedmann, Lauren Bullard, Anne Hoffmann, Jeremy Veenstra-VanderWeele, Kevin Staley, David Klements, Michael Moshinsky, Brittney Harkey, Jeff Long, Janel Fedler, Elizabeth Klingner, Dixie Ecklund, Michele Costigan, Trevis Huff, and Brenda Pearson. Effects of afq056 on language learning in fragile x syndrome. The Journal of Clinical Investigation, Aug 2024. URL: https://doi.org/10.1172/jci171723, doi:10.1172/jci171723. This article has 24 citations.

24. (berrykravis2024effectsofafq056 pages 9-10): Elizabeth Berry-Kravis, Leonard Abbeduto, Randi Hagerman, Christopher S. Coffey, Merit Cudkowicz, Craig A. Erickson, Andrea McDuffie, David Hessl, Lauren Ethridge, Flora Tassone, Walter E. Kaufmann, Katherine Friedmann, Lauren Bullard, Anne Hoffmann, Jeremy Veenstra-VanderWeele, Kevin Staley, David Klements, Michael Moshinsky, Brittney Harkey, Jeff Long, Janel Fedler, Elizabeth Klingner, Dixie Ecklund, Michele Costigan, Trevis Huff, and Brenda Pearson. Effects of afq056 on language learning in fragile x syndrome. The Journal of Clinical Investigation, Aug 2024. URL: https://doi.org/10.1172/jci171723, doi:10.1172/jci171723. This article has 24 citations.

25. (seng2024longitudinalfollowupof pages 2-3): Panhaneath Seng, Federica Alice Maria Montanaro, Hazel Maridith Barlahan Biag, Maria Jimena Salcedo-Arellano, Kyoungmi Kim, Matthew Dominic Ponzini, Flora Tassone, Andrea Schneider, Leonard Abbeduto, Angela John Thurman, David Hessl, Francois V. Bolduc, Sebastien Jacquemont, Sarah Lippé, and Randi J. Hagerman. Longitudinal follow-up of metformin treatment in fragile x syndrome. Frontiers in Psychology, Jun 2024. URL: https://doi.org/10.3389/fpsyg.2024.1305597, doi:10.3389/fpsyg.2024.1305597. This article has 8 citations and is from a peer-reviewed journal.

26. (NCT05120505 chunk 1):  Metformin in Children With Fragile X Syndrome. Children's Hospital of Fudan University. 2021. ClinicalTrials.gov Identifier: NCT05120505

27. (norris2025rocanalysisof pages 1-4): J. E. Norris, E. Berry-Kravis, Mark D. Harnett, Scott A. Reines, Melody A. Reese, Emma K. Auger Ph.D., Abigail H. Outterson Ph.D., Jeremiah Furman, Mark E. Gurney, and Ph.D Lauren E. Ethridge. Roc analysis of biomarker combinations in fragile x syndrome-specific clinical trials: evaluating treatment efficacy via exploratory biomarkers. MedRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.29.25328581, doi:10.1101/2025.05.29.25328581. This article has 1 citations.

28. (de2025fromdiscoveryto pages 9-10): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

29. (de2025fromdiscoveryto pages 8-9): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

30. (de2025fromdiscoveryto pages 6-8): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

31. (sandoval2024fromwingsto pages 2-3): Soraya O. Sandoval, Natasha M. Méndez-Albelo, Zhiyan Xu, and Xinyu Zhao. From wings to whiskers to stem cells: why every model matters in fragile x syndrome research. Journal of Neurodevelopmental Disorders, Jun 2024. URL: https://doi.org/10.1186/s11689-024-09545-w, doi:10.1186/s11689-024-09545-w. This article has 3 citations and is from a peer-reviewed journal.

32. (sandoval2024fromwingsto pages 5-7): Soraya O. Sandoval, Natasha M. Méndez-Albelo, Zhiyan Xu, and Xinyu Zhao. From wings to whiskers to stem cells: why every model matters in fragile x syndrome research. Journal of Neurodevelopmental Disorders, Jun 2024. URL: https://doi.org/10.1186/s11689-024-09545-w, doi:10.1186/s11689-024-09545-w. This article has 3 citations and is from a peer-reviewed journal.

33. (de2025fromdiscoveryto pages 18-19): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.

34. (de2025fromdiscoveryto pages 13-15): Mathijs B. van der Lei and R. Frank Kooy. From discovery to innovative translational approaches in 80 years of fragile x syndrome research. Biomedicines, 13:805, Mar 2025. URL: https://doi.org/10.3390/biomedicines13040805, doi:10.3390/biomedicines13040805. This article has 6 citations.
