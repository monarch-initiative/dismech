---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T20:02:45.413374'
end_time: '2026-04-26T20:26:34.022099'
duration_seconds: 1428.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Stevens-Johnson Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Stevens-Johnson Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Stevens-Johnson Syndrome** covering all of the
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
- **Disease Name:** Stevens-Johnson Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Stevens-Johnson Syndrome** covering all of the
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


## Stevens–Johnson Syndrome (SJS) / Toxic Epidermal Necrolysis (TEN): Comprehensive Disease Characteristics Report (2023–2024 emphasis)

### Executive summary
Stevens–Johnson syndrome (SJS) and toxic epidermal necrolysis (TEN) are rare, life-threatening, immune-mediated mucocutaneous reactions—most often drug-triggered—characterized by keratinocyte death with epidermal detachment and prominent mucosal involvement. They are best understood as a single disease spectrum defined by the percentage of detached/detachable body surface area (BSA): **SJS <10% BSA**, **SJS/TEN overlap 10–30%**, **TEN >30%**. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, abulatan2023acompilationof pages 1-2)

Recent (2024) multi-omic single-cell studies reinforce that SJS/TEN pathogenesis is dominated by **HLA class I–restricted, clonally expanded cytotoxic CD8+ T cells** and an inflamed keratinocyte microenvironment; for immune checkpoint inhibitor (ICI)–triggered epidermal necrolysis, macrophage-derived **CXCL10–CXCR3** recruitment of cytotoxic T cells and **TNF signaling** emerge as actionable drivers, with TNF blockade suggested as a targeted strategy. (gibson2024multiomicsinglecellsequencing pages 1-2, chen2024immunecheckpointinhibitorinduced pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
SJS/TEN is a dermatologic emergency with epidermal necrosis and detachment plus mucosal erosions. Definitions by detached/detachable BSA are consistent across recent reviews: **SJS (<10%), overlap (10–30%), TEN (>30%)**. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, abulatan2023acompilationof pages 1-2)

**Clinical hallmarks** emphasized in 2023–2024 sources include fever, painful erythematous rash with blistering and detachment, and mucositis (ocular/oral/genital) with positive Nikolsky sign. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, thong2023druginducedstevensjohnson pages 1-2)

**Abstract quote (definition/etiology framing):** a 2024 multicenter cohort describes SJS/TEN as “**life-threatening acute mucocutaneous disorders usually triggered by drugs**.” (erduran2024evaluationofthe pages 1-3)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)
The retrieved corpus did not include ontology identifier tables (MeSH/MONDO/Orphanet/ICD-11) in accessible text; therefore, these cannot be cited from the evidence provided in this run.

Non-evidence supplemental identifiers commonly used in practice (not cited here due to retrieval limits): ICD-10 includes L51.1 (Stevens-Johnson syndrome) and L51.2 (toxic epidermal necrolysis).

### 1.3 Synonyms / alternative names
- **Epidermal necrolysis (EN)** is commonly used to refer to the spectrum (SJS, overlap, TEN). (erduran2024evaluationofthe pages 1-3)
- **Lyell syndrome** is commonly used for TEN (noted in background and review literature). (abulatan2023acompilationof pages 1-2)

### 1.4 Evidence source type
The report is derived from aggregated disease-level resources (peer-reviewed reviews, systematic reviews, multicenter cohorts, pharmacovigilance registries, and mechanistic multi-omics studies), not single EHR extractions; individual case reports appear only as supporting context in some review sources.

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** drug-triggered immune-mediated cytotoxic reaction is dominant.
- A 2023 ophthalmic review estimates medicines account for ~75% of etiologies. (toth2023ophthalmicaspectsof pages 1-2)
- Drug-induced SJS/TEN is described as a **non-IgE-mediated severe cutaneous adverse reaction** with tissue-level cytotoxic T-cell responses. (thong2023druginducedstevensjohnson pages 1-2)

Other triggers described in recent reviews include infections and (more rarely) vaccination. (abulatan2023acompilationof pages 1-2)

### 2.2 Risk factors
#### Drug triggers (real-world pharmacovigilance)
A 2024 analysis of the Russian national pharmacovigilance database (2019–2023; **n=170 spontaneous reports**) found the top suspected drugs were:
- **lamotrigine 23.5% (n=40)**
- **ibuprofen 12.9% (n=22)**
- **ceftriaxone 8.8% (n=15)**
- **amoxicillin/amoxicillin + beta-lactam inhibitors 8.8% (n=15)**
- **paracetamol 7.6% (n=13)**
- **carbamazepine 5.9% (n=10)**
(plus azithromycin, valproate, omeprazole, levetiracetam at lower frequencies). (zyryanov2024stevens–johnsonsyndromeand pages 4-5)

Drug classes most often implicated were **anti-infectives for systemic use** and **nervous system agents**. (zyryanov2024stevens–johnsonsyndromeand pages 1-2, zyryanov2024stevens–johnsonsyndromeand pages 4-5)

#### Pharmacogenomic risk factors (gene–drug)
A major determinant of risk is **HLA genotype**, which shapes drug-antigen presentation and CD8 T-cell activation.

**DPWG guideline (Nov 2023; DOI: https://doi.org/10.21203/rs.3.rs-3255043/v1)** provides explicit implementation recommendations:
- “**Carbamazepine should not be used in an HLA-B*15:02 positive patient**.” (nijenhuis2023dutchpharmacogeneticsworking pages 1-5)
- For HLA-B*15:02, HLA-B*15:11, or HLA-A*31:01 positive patients, DPWG recommends choosing an alternative AED; if unavoidable, advise immediate reporting of rash. (nijenhuis2023dutchpharmacogeneticsworking pages 1-5)
- For phenytoin, DPWG considers **CYP2C9 genotyping ‘essential’** and recommends maintenance dose reductions with monitoring after 7–10 days. (nijenhuis2023dutchpharmacogeneticsworking pages 1-5)
- DPWG phenytoin dose guidance includes reductions to **~70–75%** (intermediate metabolizers) and **~40–50%** (poor metabolizers), with genotype-specific examples (e.g., *3/*3 ~40%). (nijenhuis2023dutchpharmacogeneticsworking pages 13-16, nijenhuis2023dutchpharmacogeneticsworking pages 16-18)

**HLA associations beyond classic AEDs (beta-lactam SCARs):** In Thai patients with beta-lactam antibiotic–related SCARs (Frontiers in Pharmacology 2023; DOI https://doi.org/10.3389/fphar.2023.1248386), elevated SJS/TEN risk was reported for multiple alleles, including:
- **HLA-B*46:02 OR 17.5 (95% CI 1.5–201.6)**
- **HLA-B*57:01 OR 9.5 (95% CI 1.3–71.5)**
- **HLA-DQB1*03:02 OR 7.5 (95% CI 1.8–30.9)**
- **HLA-C*06:02 OR 4.9 (95% CI 1.1–21.4)**
Protective signal: **HLA-A*02:07 OR 0.1 (95% CI 0.0–0.5)** (noting multiple associations did not survive Bonferroni correction and require validation). (wattanachai2023associationbetweenhla pages 1-2, wattanachai2023associationbetweenhla pages 6-8)

#### Demographic/clinical risk signals
In the 2024 multicenter cohort (n=166), diabetes and comorbidities were more common in deceased patients, and positive blood cultures and fever were associated with higher mortality in multivariable modeling. (erduran2024evaluationofthe pages 8-10)

### 2.3 Protective factors
Genetic protective alleles are not well established broadly, but one study reported **HLA-A*02:07** as protective for beta-lactam–related SCARs (OR 0.1). (wattanachai2023associationbetweenhla pages 6-8)

### 2.4 Gene–environment interactions
SJS/TEN is a paradigmatic gene–environment interaction: exposure to a culprit drug (environment) in a genetically susceptible host (HLA risk allele) drives HLA class I–restricted cytotoxic T-cell responses. This concept is explicit in 2023–2024 expert reviews and single-cell studies. (thong2023druginducedstevensjohnson pages 1-2, gibson2024multiomicsinglecellsequencing pages 1-2)

---

## 3. Phenotypes

### 3.1 Phenotype spectrum and characteristics
Key clinical phenotypes and suggested ontologies are summarized below. Frequencies are included when available.

1) **Prodrome / systemic symptoms**
- Influenza-like illness and fever are common early. (abulatan2023acompilationof pages 1-2)
- **HPO suggestions:** Fever (HP:0001945), Malaise (HP:0033834), Odynophagia (HP:0012531).

2) **Cutaneous lesions and epidermal detachment**
- Painful erythematous rash progressing to bullae and sloughing; positive Nikolsky sign. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, thong2023druginducedstevensjohnson pages 1-2)
- **HPO:** Skin blistering (HP:0008064), Skin erosion (HP:0001070), Epidermal detachment (no single perfect HPO term; may use Skin exfoliation/desquamation—HP:0001009).

3) **Mucosal involvement (multisite mucositis)**
- ≥2 mucosal sites (ocular/oral/genital) emphasized as hallmark; >90% mucosal involvement in drug-induced SJS/TEN is commonly stated in reviews. (thong2023druginducedstevensjohnson pages 1-2, abulatan2023acompilationof pages 1-2)
- **HPO:** Oral ulceration (HP:0000217), Conjunctivitis (HP:0000509), Genital ulceration (HP:0000130).

4) **Ocular involvement and sequelae**
- 2023 ophthalmic review: acute ocular signs in **50–80%**; severe early ocular complications ~**50%**; and ~**90%** develop chronic ocular disease after the acute phase. (toth2023ophthalmicaspectsof pages 1-2)
- **HPO:** Photophobia (HP:0000613), Dry eye (HP:0001097), Symblepharon (HP:0100789), Corneal opacity (HP:0007957), Blindness (HP:0000618).

### 3.2 Anatomy affected (organ/tissue/cell)
- Primary tissue: epidermis and mucosal epithelia. (hasegawa2024stevens–johnsonsyndromeand pages 1-2)
- **UBERON suggestions:** Skin epidermis (UBERON:0001003), Oral mucosa (UBERON:0000344), Conjunctiva (UBERON:0000970).

**Cell types (CL terms; best-effort):**
- Cytotoxic CD8+ T cells (CL:0000625), keratinocytes (CL:0000312), monocytes (CL:0000576), macrophages (CL:0000235). Mechanistic studies emphasize enriched CD8+ T cells in blister fluid and affected skin. (gibson2024multiomicsinglecellsequencing pages 2-3, chen2024immunecheckpointinhibitorinduced pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
SJS/TEN is generally not a monogenic disorder; it is a complex, drug-triggered immune reaction with strong associations to HLA alleles and other pharmacogenomic markers.

### 4.2 Pathogenic / susceptibility variants and gene products
Key susceptibility loci include HLA class I alleles (e.g., HLA-B*15:02 for carbamazepine) and, in some contexts, class II alleles (e.g., DQB1*03:02 in beta-lactam SCARs). (nijenhuis2023dutchpharmacogeneticsworking pages 1-5, wattanachai2023associationbetweenhla pages 6-8)

### 4.3 Molecular mediators and pathways (overview)
Expert reviews summarize that cytotoxic T cells mediate keratinocyte death via **granzyme B, perforin, granulysin**, IFN-γ, TNF-α, and related pathways. (thong2023druginducedstevensjohnson pages 1-2)

A 2024 review notes epidermal cell death is mediated through **Fas–FasL and perforin/granzyme**, and adds that **necroptosis** may also contribute. (hasegawa2024stevens–johnsonsyndromeand pages 1-2)

**GO biological process suggestions (best-effort):**
- T cell mediated cytotoxicity (GO:0001913), regulation of apoptotic process (GO:0042981), necroptotic process (GO:0070266), antigen processing and presentation of peptide antigen via MHC class I (GO:0002474).

---

## 5. Environmental information
The main “environmental” exposure is a culprit medication (or, less often, infection/vaccination). Pharmacovigilance and review data support dominant medication triggers. (toth2023ophthalmicaspectsof pages 1-2, zyryanov2024stevens–johnsonsyndromeand pages 4-5)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (drug-triggered SJS/TEN)
**Upstream:** culprit drug exposure in a susceptible host → drug–HLA presentation → activation/expansion of oligoclonal CD8+ cytotoxic T cells in tissue. (thong2023druginducedstevensjohnson pages 1-2, gibson2024multiomicsinglecellsequencing pages 1-2)

**Downstream:** cytotoxic effector molecules (granulysin, perforin/granzyme; Fas–FasL; TNF/IFN programs) → keratinocyte death, epidermal necrosis/detachment → barrier loss, fluid loss, infection risk → systemic complications. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, thong2023druginducedstevensjohnson pages 1-2)

### 6.2 Recent developments (2024 multi-omics / single-cell)
**Multiomic single-cell atlas (Nature Communications, Oct 2024; DOI https://doi.org/10.1038/s41467-024-52990-3):**
- Abstract quote: “**SJS/TEN … is a rare but life-threatening cutaneous drug reaction mediated by human leukocyte antigen (HLA) class I-restricted CD8+ T-cells**.” (gibson2024multiomicsinglecellsequencing pages 1-2)
- Blister fluid is “**a rich reservoir of oligoclonal CD8+ T-cells with an effector phenotype**” and keratinocytes in affected skin upregulate HLA and interferon-response genes. (gibson2024multiomicsinglecellsequencing pages 1-2)
- Quantitatively, blister fluid averaged **~70% CD8+ T cells** and affected skin had higher CD8+ T-cell proportion than unaffected skin. (gibson2024multiomicsinglecellsequencing pages 2-3)

**ICI-induced epidermal necrolysis mechanism (Nature Communications, accepted Nov 2024; DOI https://doi.org/10.1038/s41467-024-54180-7):**
- Abstract quote: scRNA-seq “**shows overexpression of macrophage-derived CXCL10 that recruits CXCR3+ cytotoxic T lymphocytes (CTL)**” and identifies **TNF signaling** as responsible for macrophage-derived CXCL10 and CTL activation. (chen2024immunecheckpointinhibitorinduced pages 1-2)
- The study included “**6 cohorts including 25 ICI-induced SJS/TEN patients**” (chen2024immunecheckpointinhibitorinduced pages 1-2)
- Treatment implication (from abstract): compared with systemic corticosteroids, “**patients treated with biologic TNF blockade showed a significantly rapid recovery and no recurrence of SCAR with continuous ICI therapy**.” (chen2024immunecheckpointinhibitorinduced pages 1-2)

---

## 7. Anatomical structures affected

- **Skin and mucosa:** epidermis, oral mucosa, conjunctiva, genital mucosa. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, thong2023druginducedstevensjohnson pages 1-2)
- **UBERON suggestions:** Skin epidermis (UBERON:0001003), Conjunctiva (UBERON:0000970), Oral mucosa (UBERON:0000344), Genital mucosa (UBERON term depends on site).

---

## 8. Temporal development (onset and course)
Drug-triggered SJS/TEN typically occurs after a latency following drug start.
- A 2023 review notes a “**median of 2 weeks**” latency (range 4 days–8 weeks) for drug-induced SJS/TEN. (thong2023druginducedstevensjohnson pages 1-2)

Clinical course features include acute epidermal necrolysis and re-epithelialization over weeks (review synthesis). (abulatan2023acompilationof pages 1-2)

---

## 9. Inheritance and population

SJS/TEN is not inherited in a Mendelian fashion; risk is strongly influenced by population HLA allele frequencies and drug exposure.

Population variation is especially important for HLA-B*15:02–associated AED risk, with DPWG highlighting higher prevalence in South/East Asian ancestries and recommending targeted genotyping before specific AEDs in these populations. (nijenhuis2023dutchpharmacogeneticsworking pages 16-18)

---

## 10. Diagnostics

### 10.1 Clinical criteria and classification
- BSA thresholds define SJS/overlap/TEN. (hasegawa2024stevens–johnsonsyndromeand pages 1-2, abulatan2023acompilationof pages 1-2)
- Hallmarks: fever, ≥2 mucosal involvements, positive Nikolsky sign, epidermal detachment. (thong2023druginducedstevensjohnson pages 1-2)

### 10.2 Histopathology
SJS/TEN biopsy classically shows full-thickness epidermal necrosis with mononuclear infiltration and dermo-epidermal separation. (chuenwipasakul2023correlationsbetweenhistopathologic pages 1-2)

### 10.3 Causality assessment (drug attribution)
The **ALDEN** algorithm is described in a 2023 review as a structured drug causality approach based on time lag, drug presence, (re)challenge, dechallenge, notoriety, and alternatives. (abulatan2023acompilationof pages 9-10)

### 10.4 Severity and prognosis scoring: SCORTEN
A 2023 review notes: “**total SCORTEN ≥5 is associated with 90% mortality**.” (thong2023druginducedstevensjohnson pages 1-2)

A 2024 review contains SCORTEN variable tables (risk factors and predicted mortality by score); extracted figure/table evidence is available. (hasegawa2024stevens–johnsonsyndromeand media be19cccd)

---

## 11. Outcome / prognosis

### 11.1 Mortality and complications
**Recent multicenter cohort (Turkey; 12 tertiary centers; 2012–2022; n=166; published May 2024; DOI https://doi.org/10.1007/s13555-024-01180-6):**
- Abstract quote: “**Forty (24.1%) of our patients died in hospital.**” (erduran2024evaluationofthe pages 10-12)
- Mean SCORTEN in first 24h: **2.44 ± 1.42**. (erduran2024evaluationofthe pages 1-3)
- Strong SCORTEN–mortality association: compared with SCORTEN 0–1, mortality ORs were **12** at SCORTEN 3, **22** at SCORTEN 4, and **84** at SCORTEN 5–6. (erduran2024evaluationofthe pages 8-10)
- Complications occurred in **51.8%**, including sepsis **14.5%**, intubation **13.9%**, acute renal failure **12.7%**, UTI **11.4%**, bacteremia (percentage not fully extractable across excerpts). (erduran2024evaluationofthe pages 10-12)

### 11.2 Ocular long-term outcomes
Ocular disease is a major morbidity driver; a 2023 narrative review reports chronic ocular disease in ~90% after acute phase. (toth2023ophthalmicaspectsof pages 1-2)

A 2024 SJS surgical series (BMC Ophthalmology; DOI https://doi.org/10.1186/s12886-024-03461-2) reported that corneal sight-rehabilitating surgery improved vision: pre-op VA **1.96 ± 0.43 logMAR** to optimal **0.74 ± 0.60** and endpoint **1.06 ± 0.82**, mean follow-up **50.6 ± 28.1 months**, with **86.7% success rate**; 88.9% (8/9) were no longer blind. (peng2024theoutcomesof pages 1-2)

---

## 12. Treatment

### 12.1 Supportive care (cornerstone; real-world implementation)
Modern reviews and cohorts emphasize near-universal supportive care including early withdrawal of the offending drug, ICU/burn-unit level wound and fluid management, infection monitoring, nutrition, and multidisciplinary care. (thong2023druginducedstevensjohnson pages 2-3, erduran2024evaluationofthe pages 1-3)

### 12.2 Systemic immunomodulatory therapies (evidence and expert interpretation)
Evidence remains limited by rarity and heterogeneous observational designs; authoritative reviews emphasize uncertainty.

A 2023 expert commentary states: “**The role of immunomodulatory treatments in SJS/TEN is at present not supported by robust evidence from systematic reviews given the lack of randomized controlled trials.**” (thong2023druginducedstevensjohnson pages 1-2)

**Real-world usage (2024 multicenter cohort, n=166):**
- systemic steroids used in **84.3%**
- IVIG in **49.4%**
- cyclosporine in **38.6%**
but “no effect” of systemic steroids/IVIG/cyclosporine on mortality was observed in comparative analyses. (erduran2024evaluationofthe pages 1-3)

### 12.3 Anti-TNF therapy (emerging targeted strategy)
Mechanistic and clinical evidence increasingly implicates TNF in epidermal necrolysis.
- The 2024 ICI-induced SJS/TEN study suggests TNF blockade as a pathway-level intervention and reports faster recovery/no recurrence relative to systemic corticosteroids in that setting. (chen2024immunecheckpointinhibitorinduced pages 1-2)

### 12.4 Ocular acute interventions (amniotic membrane / ProKera)
A 2023 ophthalmic review states that “**Timely amniotic membrane transplantation as a patch combined with conformer, symblepharon ring or ProKera can prevent severe chronic complications.**” (toth2023ophthalmicaspectsof pages 1-2)

### 12.5 MAXO suggestions (best-effort)
- Drug withdrawal (MAXO: drug discontinuation)
- Intensive supportive care (MAXO: supportive therapy)
- Systemic corticosteroid therapy (MAXO)
- Intravenous immunoglobulin therapy (MAXO)
- Cyclosporine therapy (MAXO)
- TNF inhibitor therapy (MAXO)
- Amniotic membrane transplantation (MAXO: surgical procedure / tissue transplantation)

(Exact MAXO IDs are not present in retrieved corpus; terms provided for knowledge-base mapping.)

---

## 13. Prevention

### 13.1 Pharmacogenomic prevention (real-world implementation)
Preemptive HLA screening is one of the clearest implementable prevention strategies.

DPWG guidance recommends avoiding carbamazepine in HLA-B*15:02 carriers and considering genotyping as beneficial in higher-prevalence ancestries. (nijenhuis2023dutchpharmacogeneticsworking pages 1-5, nijenhuis2023dutchpharmacogeneticsworking pages 16-18)

A 2023 expert review notes that preventive HLA genotype screening before carbamazepine and allopurinol prescriptions “may further reduce the incidence of SJS/TEN.” (thong2023druginducedstevensjohnson pages 1-2)

---

## 14. Other species / natural disease
The retrieved evidence in this run did not provide veterinary/natural disease descriptions across other species.

---

## 15. Model organisms / model systems
Recent mechanistic work emphasizes **human tissue-based** and **single-cell** approaches. A practical disease-relevant model system is the **human skin/blister-fluid cellular ecosystem** characterized by multiomic single-cell sequencing. (gibson2024multiomicsinglecellsequencing pages 1-2)

(Additional ex vivo skin explant models are discussed in other retrieved articles but were not fully extracted in this run.)

---

## Key quantitative reference table

| Domain | Item | Key data | Source / setting |
|---|---|---|---|
| Definition / diagnostic threshold | Stevens–Johnson syndrome (SJS) | Epidermal detachment **<10% body surface area (BSA)**; part of the SJS/TEN spectrum with extensive mucosal involvement common (hasegawa2024stevens–johnsonsyndromeand pages 1-2, abulatan2023acompilationof pages 1-2, chuenwipasakul2023correlationsbetweenhistopathologic pages 1-2) | Review/clinical summaries (2023–2024) |
| Definition / diagnostic threshold | SJS/TEN overlap | Epidermal detachment **10–30% BSA** (hasegawa2024stevens–johnsonsyndromeand pages 1-2, abulatan2023acompilationof pages 1-2) | Review/clinical summaries (2023–2024) |
| Definition / diagnostic threshold | Toxic epidermal necrolysis (TEN) | Epidermal detachment **>30% BSA** (hasegawa2024stevens–johnsonsyndromeand pages 1-2, abulatan2023acompilationof pages 1-2) | Review/clinical summaries (2023–2024) |
| Epidemiology / mortality | Japan | Incidence about **2.5/million** for SJS and **1.0/million** for TEN; mortality **4.1%** for SJS and **29.9%** for TEN (hasegawa2024stevens–johnsonsyndromeand pages 1-2) | Japan-focused review citing national data |
| Epidemiology / mortality | International review summary | Overall incidence about **2–7/million/year**; female:male about **2:1**; mortality **10–50%**, higher for TEN (abulatan2023acompilationof pages 1-2) | Multi-country review synthesis |
| Epidemiology / mortality | UK | Incidence **5.76/million/year** (abulatan2023acompilationof pages 1-2, toth2023ophthalmicaspectsof pages 1-2) | Review summaries citing UK data |
| Epidemiology / mortality | France (TEN) | Incidence **1.2–1.3/million/year** for TEN (abulatan2023acompilationof pages 1-2) | Review summary citing French data |
| Epidemiology / mortality | Germany | Incidence **0.93/million** (toth2023ophthalmicaspectsof pages 1-2) | Ophthalmic narrative review |
| Epidemiology / mortality | USA | Incidence **12.35/million** (toth2023ophthalmicaspectsof pages 1-2) | Ophthalmic narrative review |
| Epidemiology / mortality | Europe lethality estimate | Overall lethality **34%**; **24%** for SJS and **49%** for TEN (toth2023ophthalmicaspectsof pages 1-2) | Ophthalmic narrative review |
| Epidemiology / mortality | Prospective-cohort summary | Reported mortality **5–12.5%** for SJS and **25–35%** for TEN (gong2023apoa4asa pages 1-2) | Proteomics/prognosis study background |
| Prognosis tool | SCORTEN high-risk threshold | **SCORTEN ≥5** is associated with about **90% mortality** (thong2023druginducedstevensjohnson pages 1-2) | Prognostic summary / review |
| Prognosis tool | SCORTEN in multicenter cohort | In 166 patients, mean day-1 SCORTEN **2.44 ± 1.42**; mortality **24.1% (40/166)** overall (erduran2024evaluationofthe pages 1-3, erduran2024evaluationofthe pages 10-12, erduran2024evaluationofthe pages 4-6) | Erduran et al. 2024 multicenter study |
| Prognosis tool | Erduran 2024 ORs by SCORTEN category | Versus SCORTEN **0–1**, mortality OR for **SCORTEN 3 = 12** (95% CI 2.363–60.948), **SCORTEN 4 = 22** (95% CI 4.293–112.740), **SCORTEN 5–6 = 84** (95% CI 13.902–507.537); **SCORTEN 2** not significant (p=0.38) (erduran2024evaluationofthe pages 8-10) | Erduran et al. 2024 multicenter study |
| Prognosis tool | Other mortality predictors in Erduran 2024 | Fever OR **2.825**; positive blood cultures OR **3.664**; diabetes mellitus OR **6.273**; comorbidity OR **3.326**; plasmapheresis associated with about **22-fold** higher mortality (95% CI 1.96–247.2) (erduran2024evaluationofthe pages 8-10, erduran2024evaluationofthe pages 10-12) | Erduran et al. 2024 multicenter study |


*Table: This table condenses the key diagnostic thresholds, representative recent epidemiology and mortality statistics, and the main prognostic information for SJS/TEN, including SCORTEN and the 2024 multicenter mortality odds ratios. It is useful as a quick reference for disease classification and risk stratification.*

---

## Notes on evidence limitations (important for knowledge base curation)
1) **PMIDs** were not consistently available in the retrieved full-text snippets; where absent, the report provides DOI/URL and publication month/year from the papers’ metadata.
2) **Ontology IDs (MeSH/MONDO/Orphanet/ICD-11)** were not present in the retrieved documents; therefore, identifier fields should be completed by direct lookup in the relevant ontology portals in a subsequent curation step.
3) Several 2023–2024 potentially high-value sources (e.g., formal S3 guidelines; CRISTEN score paper) were listed as “unobtainable” in retrieval and thus could not be cited.


References

1. (hasegawa2024stevens–johnsonsyndromeand pages 1-2): Akito Hasegawa and Riichiro Abe. Stevens–johnson syndrome and toxic epidermal necrolysis: updates in pathophysiology and management. Chinese Medical Journal, 137:2294-2307, Sep 2024. URL: https://doi.org/10.1097/cm9.0000000000003250, doi:10.1097/cm9.0000000000003250. This article has 34 citations and is from a peer-reviewed journal.

2. (abulatan2023acompilationof pages 1-2): Isaac T Abulatan, Sage G Ben-David, Lery A Morales-Colon, Elisabeth Beason, and Adegbenro O Fakoya. A compilation of drug etiologies of stevens-johnson syndrome and toxic epidermal necrolysis. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.48728, doi:10.7759/cureus.48728. This article has 19 citations.

3. (gibson2024multiomicsinglecellsequencing pages 1-2): Andrew Gibson, Ramesh Ram, Rama Gangula, Yueran Li, Eric Mukherjee, Amy M. Palubinsky, Chelsea N. Campbell, Michael Thorne, Katherine C. Konvinse, Phuti Choshi, Pooja Deshpande, Sarah Pedretti, Mark W. Fear, Fiona M. Wood, Richard T. O’Neil, Celestine N. Wanjalla, Spyros A. Kalams, Silvana Gaudieri, Rannakoe J. Lehloenya, Samuel S. Bailin, Abha Chopra, Jason A. Trubiano, Jason Trubiano, Jonny G. Peter, Simon A. Mallal, and Elizabeth J. Phillips. Multiomic single-cell sequencing defines tissue-specific responses in stevens-johnson syndrome and toxic epidermal necrolysis. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52990-3, doi:10.1038/s41467-024-52990-3. This article has 31 citations and is from a highest quality peer-reviewed journal.

4. (chen2024immunecheckpointinhibitorinduced pages 1-2): Chun-Bing Chen, Shuen-Iu Hung, John Wen-Cheng Chang, Chan-Keng Yang, David Hui-Kang Ma, Yu-Chuan Teng, Chun-Wei Lu, Wei-Ti Chen, Hsiao-Yin Yang, Cheng-Chang Tsai, Chih Liang Wang, Pin-Hsuan Chiang, Jennifer Wu, Ya-Wen Tsai, Lai-Ying Lu, Yang Yu-Wei Lin, Rosaline Chung-Yee Hui, Fu-Mei Hsieh, Chao-Kai Hsu, Chaw-Ning Lee, Yi-Ju Chen, Chih-Chiang Chen, Yilei Cui, Hung-Chih Hsu, Ya-Ching Chang, Chih-Jung Chang, Ho-Chen Lin, Chee Jen Chang, Yu-Jr Lin, Cheng-Lung Ku, Chuang-Wei Wang, and Wen-Hung Chung. Immune checkpoint inhibitor-induced severe epidermal necrolysis mediated by macrophage-derived cxcl10 and abated by tnf blockade. Nature Communications, Dec 2024. URL: https://doi.org/10.1038/s41467-024-54180-7, doi:10.1038/s41467-024-54180-7. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (thong2023druginducedstevensjohnson pages 1-2): Bernard Yu-Hor Thong. Drug-induced stevens johnson syndrome and toxic epidermal necrolysis: interpreting the systematic reviews on immunomodulatory therapies. Asia Pacific Allergy, 13:72-76, Jun 2023. URL: https://doi.org/10.5415/apallergy.0000000000000101, doi:10.5415/apallergy.0000000000000101. This article has 14 citations.

6. (erduran2024evaluationofthe pages 1-3): Funda Erduran, Esra Adışen, Selma Emre, Yıldız Hayran, Emel Bülbül Başkan, Serkan Yazıcı, Aslı Bilgiç, Erkan Alpsoy, Sibel Doğan Günaydın, Leyla Elmas, Melih Akyol, RukiyeYasak Güner, Deniz Aksu Arıca, Yağmur Aypek, Tülin Ergun, Dilan Karavelioğlu, Ayça Cordan Yazıcı, Kübra Aydoğan, Dilek Bayramgürler, Rebiay Kıran, Hilal Kaya Erdoğan, Ersoy Acer, and Akın Aktaş. Evaluation of the factors influencing mortality in patients with stevens-johnson syndrome and toxic epidermal necrolysis: a multicenter study of 166 patients. Dermatology and Therapy, 14:1547-1560, May 2024. URL: https://doi.org/10.1007/s13555-024-01180-6, doi:10.1007/s13555-024-01180-6. This article has 8 citations.

7. (toth2023ophthalmicaspectsof pages 1-2): Gábor Tóth, Andrea Lukács, Frank Schirra, Gábor L. Sándor, Petra Killik, Otto A. Maneschg, Zoltán Z. Nagy, and Nóra Szentmáry. Ophthalmic aspects of stevens–johnson syndrome and toxic epidermal necrolysis: a narrative review. Ophthalmology and Therapy, 12:1795-1811, May 2023. URL: https://doi.org/10.1007/s40123-023-00725-w, doi:10.1007/s40123-023-00725-w. This article has 38 citations and is from a peer-reviewed journal.

8. (zyryanov2024stevens–johnsonsyndromeand pages 4-5): Sergey Zyryanov, Irina Asetskaya, Olga Butranova, Elizaveta Terekhina, Vitaly Polivanov, Alexander Yudin, and Kristina Samsonova. Stevens–johnson syndrome and toxic epidermal necrolysis: analysis of the russian database of spontaneous reports. Pharmaceuticals, 17:675, May 2024. URL: https://doi.org/10.3390/ph17060675, doi:10.3390/ph17060675. This article has 11 citations.

9. (zyryanov2024stevens–johnsonsyndromeand pages 1-2): Sergey Zyryanov, Irina Asetskaya, Olga Butranova, Elizaveta Terekhina, Vitaly Polivanov, Alexander Yudin, and Kristina Samsonova. Stevens–johnson syndrome and toxic epidermal necrolysis: analysis of the russian database of spontaneous reports. Pharmaceuticals, 17:675, May 2024. URL: https://doi.org/10.3390/ph17060675, doi:10.3390/ph17060675. This article has 11 citations.

10. (nijenhuis2023dutchpharmacogeneticsworking pages 1-5): Marga Nijenhuis, Lisanne Manson, Bianca Soree, Nienke de Boer-Veger, Anne Marie Buunk, Elisa Houwink, Arne Risselada, Gerard Rongen, Ron van Schaik, Jesse Swen, Daniel Touw, Roos van Westrhenen, Vera Deneer, and Henk-Jan Guchelaar. Dutch pharmacogenetics working group (dpwg) guideline for the gene-drug interaction of cyp2c9, hla-a and hla-b with anti-epileptic drugs. Nov 2023. URL: https://doi.org/10.21203/rs.3.rs-3255043/v1, doi:10.21203/rs.3.rs-3255043/v1.

11. (nijenhuis2023dutchpharmacogeneticsworking pages 13-16): Marga Nijenhuis, Lisanne Manson, Bianca Soree, Nienke de Boer-Veger, Anne Marie Buunk, Elisa Houwink, Arne Risselada, Gerard Rongen, Ron van Schaik, Jesse Swen, Daniel Touw, Roos van Westrhenen, Vera Deneer, and Henk-Jan Guchelaar. Dutch pharmacogenetics working group (dpwg) guideline for the gene-drug interaction of cyp2c9, hla-a and hla-b with anti-epileptic drugs. Nov 2023. URL: https://doi.org/10.21203/rs.3.rs-3255043/v1, doi:10.21203/rs.3.rs-3255043/v1.

12. (nijenhuis2023dutchpharmacogeneticsworking pages 16-18): Marga Nijenhuis, Lisanne Manson, Bianca Soree, Nienke de Boer-Veger, Anne Marie Buunk, Elisa Houwink, Arne Risselada, Gerard Rongen, Ron van Schaik, Jesse Swen, Daniel Touw, Roos van Westrhenen, Vera Deneer, and Henk-Jan Guchelaar. Dutch pharmacogenetics working group (dpwg) guideline for the gene-drug interaction of cyp2c9, hla-a and hla-b with anti-epileptic drugs. Nov 2023. URL: https://doi.org/10.21203/rs.3.rs-3255043/v1, doi:10.21203/rs.3.rs-3255043/v1.

13. (wattanachai2023associationbetweenhla pages 1-2): Pansakon Wattanachai, Warayuwadee Amornpinyo, Parinya Konyoung, Danklai Purimart, Usanee Khunarkornsiri, Oranuch Pattanacheewapull, Wichittra Tassaneeyakul, and Nontaya Nakkam. Association between hla alleles and beta-lactam antibiotics-related severe cutaneous adverse reactions. Frontiers in Pharmacology, Sep 2023. URL: https://doi.org/10.3389/fphar.2023.1248386, doi:10.3389/fphar.2023.1248386. This article has 18 citations.

14. (wattanachai2023associationbetweenhla pages 6-8): Pansakon Wattanachai, Warayuwadee Amornpinyo, Parinya Konyoung, Danklai Purimart, Usanee Khunarkornsiri, Oranuch Pattanacheewapull, Wichittra Tassaneeyakul, and Nontaya Nakkam. Association between hla alleles and beta-lactam antibiotics-related severe cutaneous adverse reactions. Frontiers in Pharmacology, Sep 2023. URL: https://doi.org/10.3389/fphar.2023.1248386, doi:10.3389/fphar.2023.1248386. This article has 18 citations.

15. (erduran2024evaluationofthe pages 8-10): Funda Erduran, Esra Adışen, Selma Emre, Yıldız Hayran, Emel Bülbül Başkan, Serkan Yazıcı, Aslı Bilgiç, Erkan Alpsoy, Sibel Doğan Günaydın, Leyla Elmas, Melih Akyol, RukiyeYasak Güner, Deniz Aksu Arıca, Yağmur Aypek, Tülin Ergun, Dilan Karavelioğlu, Ayça Cordan Yazıcı, Kübra Aydoğan, Dilek Bayramgürler, Rebiay Kıran, Hilal Kaya Erdoğan, Ersoy Acer, and Akın Aktaş. Evaluation of the factors influencing mortality in patients with stevens-johnson syndrome and toxic epidermal necrolysis: a multicenter study of 166 patients. Dermatology and Therapy, 14:1547-1560, May 2024. URL: https://doi.org/10.1007/s13555-024-01180-6, doi:10.1007/s13555-024-01180-6. This article has 8 citations.

16. (gibson2024multiomicsinglecellsequencing pages 2-3): Andrew Gibson, Ramesh Ram, Rama Gangula, Yueran Li, Eric Mukherjee, Amy M. Palubinsky, Chelsea N. Campbell, Michael Thorne, Katherine C. Konvinse, Phuti Choshi, Pooja Deshpande, Sarah Pedretti, Mark W. Fear, Fiona M. Wood, Richard T. O’Neil, Celestine N. Wanjalla, Spyros A. Kalams, Silvana Gaudieri, Rannakoe J. Lehloenya, Samuel S. Bailin, Abha Chopra, Jason A. Trubiano, Jason Trubiano, Jonny G. Peter, Simon A. Mallal, and Elizabeth J. Phillips. Multiomic single-cell sequencing defines tissue-specific responses in stevens-johnson syndrome and toxic epidermal necrolysis. Nature Communications, Oct 2024. URL: https://doi.org/10.1038/s41467-024-52990-3, doi:10.1038/s41467-024-52990-3. This article has 31 citations and is from a highest quality peer-reviewed journal.

17. (chuenwipasakul2023correlationsbetweenhistopathologic pages 1-2): Donlaporn Chuenwipasakul, Chanudda Washrawirul, Rawiphan Panpruk, Jade Wititsuwannakul, Kridipop Charoenchaipiyakul, Supranee Buranapraditkun, Vilavun Puangsricharern, Jettanong Klaewsongkram, and Pawinee Rerknimitr. Correlations between histopathologic findings, serum biomarker levels, and clinical outcomes in stevens–johnson syndrome/toxic epidermal necrolysis (sjs/ten). Scientific Reports, Aug 2023. URL: https://doi.org/10.1038/s41598-023-40812-3, doi:10.1038/s41598-023-40812-3. This article has 17 citations and is from a peer-reviewed journal.

18. (abulatan2023acompilationof pages 9-10): Isaac T Abulatan, Sage G Ben-David, Lery A Morales-Colon, Elisabeth Beason, and Adegbenro O Fakoya. A compilation of drug etiologies of stevens-johnson syndrome and toxic epidermal necrolysis. Cureus, Nov 2023. URL: https://doi.org/10.7759/cureus.48728, doi:10.7759/cureus.48728. This article has 19 citations.

19. (hasegawa2024stevens–johnsonsyndromeand media be19cccd): Akito Hasegawa and Riichiro Abe. Stevens–johnson syndrome and toxic epidermal necrolysis: updates in pathophysiology and management. Chinese Medical Journal, 137:2294-2307, Sep 2024. URL: https://doi.org/10.1097/cm9.0000000000003250, doi:10.1097/cm9.0000000000003250. This article has 34 citations and is from a peer-reviewed journal.

20. (erduran2024evaluationofthe pages 10-12): Funda Erduran, Esra Adışen, Selma Emre, Yıldız Hayran, Emel Bülbül Başkan, Serkan Yazıcı, Aslı Bilgiç, Erkan Alpsoy, Sibel Doğan Günaydın, Leyla Elmas, Melih Akyol, RukiyeYasak Güner, Deniz Aksu Arıca, Yağmur Aypek, Tülin Ergun, Dilan Karavelioğlu, Ayça Cordan Yazıcı, Kübra Aydoğan, Dilek Bayramgürler, Rebiay Kıran, Hilal Kaya Erdoğan, Ersoy Acer, and Akın Aktaş. Evaluation of the factors influencing mortality in patients with stevens-johnson syndrome and toxic epidermal necrolysis: a multicenter study of 166 patients. Dermatology and Therapy, 14:1547-1560, May 2024. URL: https://doi.org/10.1007/s13555-024-01180-6, doi:10.1007/s13555-024-01180-6. This article has 8 citations.

21. (peng2024theoutcomesof pages 1-2): Rongmei Peng, Miaomiao Chi, Gege Xiao, Hongqiang Qu, Zhan Shen, Yinghan Zhao, and Jing Hong. The outcomes of corneal sight rehabilitating surgery in stevens-johnson syndrome: case series. BMC Ophthalmology, May 2024. URL: https://doi.org/10.1186/s12886-024-03461-2, doi:10.1186/s12886-024-03461-2. This article has 3 citations and is from a peer-reviewed journal.

22. (thong2023druginducedstevensjohnson pages 2-3): Bernard Yu-Hor Thong. Drug-induced stevens johnson syndrome and toxic epidermal necrolysis: interpreting the systematic reviews on immunomodulatory therapies. Asia Pacific Allergy, 13:72-76, Jun 2023. URL: https://doi.org/10.5415/apallergy.0000000000000101, doi:10.5415/apallergy.0000000000000101. This article has 14 citations.

23. (gong2023apoa4asa pages 1-2): Ting Gong, Peng Zhang, Shi-Fan Ruan, Zhixun Xiao, Wen Chen, Min Lin, Qingmei Zhong, Renwei Luo, Qiuyun Xu, Jiamei Peng, Bo Cheng, Fa Chen, Lihong Chen, Wen-Hung Chung, and Chao Ji. Apoa4 as a novel predictor of prognosis in stevens-johnson syndrome/toxic epidermal necrolysis: a proteomics analysis from two prospective cohorts. Journal of the American Academy of Dermatology, 89:45-52, Jul 2023. URL: https://doi.org/10.1016/j.jaad.2023.02.058, doi:10.1016/j.jaad.2023.02.058. This article has 15 citations and is from a domain leading peer-reviewed journal.

24. (erduran2024evaluationofthe pages 4-6): Funda Erduran, Esra Adışen, Selma Emre, Yıldız Hayran, Emel Bülbül Başkan, Serkan Yazıcı, Aslı Bilgiç, Erkan Alpsoy, Sibel Doğan Günaydın, Leyla Elmas, Melih Akyol, RukiyeYasak Güner, Deniz Aksu Arıca, Yağmur Aypek, Tülin Ergun, Dilan Karavelioğlu, Ayça Cordan Yazıcı, Kübra Aydoğan, Dilek Bayramgürler, Rebiay Kıran, Hilal Kaya Erdoğan, Ersoy Acer, and Akın Aktaş. Evaluation of the factors influencing mortality in patients with stevens-johnson syndrome and toxic epidermal necrolysis: a multicenter study of 166 patients. Dermatology and Therapy, 14:1547-1560, May 2024. URL: https://doi.org/10.1007/s13555-024-01180-6, doi:10.1007/s13555-024-01180-6. This article has 8 citations.