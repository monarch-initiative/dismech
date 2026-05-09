---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T15:06:54.303108'
end_time: '2026-05-07T15:23:02.379081'
duration_seconds: 968.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intracranial berry aneurysm
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Intracranial berry aneurysm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Intracranial berry aneurysm** covering all of the
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
- **Disease Name:** Intracranial berry aneurysm
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Intracranial berry aneurysm** covering all of the
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


# Intracranial berry aneurysm (saccular intracranial aneurysm): disease characteristics research report

## 1. Disease information

### 1.1 Overview
Intracranial berry aneurysm refers to the common “saccular” subtype of intracranial aneurysm: a focal, sac-like dilation of a cerebral artery wall that typically arises at arterial branch points/bifurcations—most often within the Circle of Willis—where hemodynamic stresses are highest. Saccular/berry aneurysms constitute ~90% of intracranial aneurysms in contemporary reviews. (tataranu2024advancementsinbrain pages 4-5, ricecanetto2025areviewof pages 2-3)

### 1.2 Synonyms / alternative names
- Intracranial saccular aneurysm
- Cerebral berry aneurysm
- Saccular cerebral aneurysm
- Unruptured intracranial aneurysm (UIA) when not ruptured (clinical state)
- Aneurysmal subarachnoid hemorrhage (aSAH) when rupture causes SAH (complication/state)

Synonymy (“saccular” ≈ “berry”) is explicitly used in recent sources. (tataranu2024advancementsinbrain pages 4-5, ricecanetto2025areviewof pages 2-3)

### 1.3 Key identifiers (ontology and coding)
- **MONDO:** **MONDO_0016483** (“intracranial berry aneurysm”). (OpenTargets Search: intracranial aneurysm)
- **Other clinical coding/terminologies (ICD-10/11, MeSH, OMIM, Orphanet):** Not directly retrievable in the current evidence corpus from tool calls, so these identifiers cannot be asserted with citations here.

### 1.4 Source type for the information in this report
This report is derived from aggregated, disease-level sources (peer-reviewed consensus review, systematic reviews/meta-analyses, and primary genetic studies), plus clinical trial registry metadata (ClinicalTrials.gov) rather than EHR-derived individual-patient data. (tjoumakaris2024ariseiconsensus pages 1-3, bandhauer2024fromconservativeto pages 1-2, liu2024geneticallydeterminedblood pages 1-2, OpenTargets Search: intracranial aneurysm)


## 2. Etiology

### 2.1 Disease causal factors (current understanding)
Intracranial berry aneurysm is widely considered a **multifactorial** vascular disease in which focal arterial-wall weakening and remodeling—driven by abnormal hemodynamic loading—interacts with inflammation, extracellular matrix (ECM) degradation, and genetic susceptibility. (ricecanetto2025areviewof pages 2-3, tjoumakaris2024ariseiconsensus pages 4-5)

A high-quality recent consensus emphasizes that rupture risk reflects a combination of patient-level factors (e.g., sex, family history) and aneurysm-level factors (size, location, morphology), and highlights the growing role of advanced imaging (e.g., vessel wall imaging) and AI for risk prediction rather than any single causal factor. (tjoumakaris2024ariseiconsensus pages 1-3, tjoumakaris2024ariseiconsensus pages 4-5)

### 2.2 Risk factors

#### 2.2.1 Genetic risk factors
**Familial aggregation and heritability**
- In a large primary study focused on THSD1, background epidemiology notes: IA prevalence ≈3%, and 7%–20% of IA patients report a positive family history. (santiagosim2016thsd1(thrombospondintype pages 1-2)
- In a high-impact 2024 consensus, “familial IA” (≥2 first-degree relatives) is highlighted as a high-risk category with screening yield of **~4–11%** and **up to ~20% lifetime SAH risk**; having a single first-degree relative is associated with **~3–4% lifetime rupture risk**. (tjoumakaris2024ariseiconsensus pages 4-5)

**THSD1 (strongest primary mechanistic human-genetic evidence in current corpus)**
- A primary human-genetic and mechanistic study identified THSD1 mutations in familial and sporadic IA. It reports enrichment of THSD1 mutations in IA probands and includes animal and endothelial-cell functional evidence consistent with causality (see §4). (santiagosim2016thsd1(thrombospondintype pages 1-2, santiagosim2016thsd1(thrombospondintype pages 2-2)

**Additional susceptibility genes from family WES**
- A Japanese multiplex-family whole-exome sequencing study identified NPNT (splice donor variant) and CBY2 (missense) as susceptibility genes and showed case–control enrichment of deleterious CBY2 variants. (maegawa2022wholeexomesequencingin pages 1-2)

**Polygenic and GWAS loci (evidence present but not fully enumerated in 2023–2024 sources in this corpus)**
- OpenTargets disease–target evidence links multiple genes to “brain aneurysm” and “intracranial berry aneurysm,” including **THSD1, EDNRA, ATP2B1, STARD13, CDKN2B, SOX17**, among others. (OpenTargets Search: intracranial aneurysm)

#### 2.2.2 Environmental / lifestyle / demographic risk factors
Across clinical reviews and consensus documents, commonly cited modifiable risk factors include:
- **Hypertension** and elevated blood pressure (see Mendelian randomization below). (liu2024geneticallydeterminedblood pages 2-4)
- **Cigarette smoking**. (ricecanetto2025areviewof pages 2-3)
- **Heavy alcohol use** and **sympathomimetic/stimulant drugs** (e.g., cocaine). (findlay2025currentmanagementof pages 1-2)
- **Female sex** is associated with higher prevalence and growth risk in multiple sources. (tjoumakaris2024ariseiconsensus pages 1-3, tataranu2024advancementsinbrain pages 1-2)

**Quantitative recent evidence (2024 Mendelian randomization on BP)**
A 2024 two-sample Mendelian randomization study quantified causal effects of genetically determined blood pressure on IA and aSAH risk. Key results:
- Per genetically predicted **+10 mmHg SBP**: IA OR **1.73** (95% CI 1.45–2.05) and SAH OR **1.93** (1.52–2.45). (liu2024geneticallydeterminedblood pages 2-4)
- Per genetically predicted **+5 mmHg DBP**: IA OR **1.62** (1.39–1.89) and SAH OR **1.64** (1.33–2.01). (liu2024geneticallydeterminedblood pages 2-4)
- Per genetically predicted **+1 mmHg pulse pressure**: IA OR **1.06** (1.03–1.10) and SAH OR **1.04** (1.01–1.08). (liu2024geneticallydeterminedblood pages 2-4)

This study also found that genetic proxies for calcium channel blocker targets were associated with slightly higher IA and SAH risk (IA OR 1.07; SAH OR 1.06), but these results are hypothesis-generating and require clinical validation. (liu2024geneticallydeterminedblood pages 1-2)

### 2.3 Protective factors
Robust protective factors are less established than risk factors in the retrieved core 2023–2024 clinical literature. In the available evidence:
- The ARISE consensus suggests that **absence** of aneurysm wall enhancement on vessel wall imaging may be more useful for establishing stability than enhancement is for proving instability. (tjoumakaris2024ariseiconsensus pages 4-5)

(Additional MR-based dietary protective signals were not part of the requested 2023–2024 prioritization and were not fully evidenced in the retrieved context.)

### 2.4 Gene–environment interactions
Direct, quantitative GxE interaction estimates (e.g., variant-by-smoking, variant-by-hypertension effect modification) were not present in the retrieved evidence set; therefore, only qualitative statements can be made: consensus and reviews emphasize the overlap and interaction between genetic susceptibility and modifiable exposures such as hypertension and smoking in determining IA development and rupture risk. (tjoumakaris2024ariseiconsensus pages 4-5, ricecanetto2025areviewof pages 2-3)


## 3. Phenotypes

### 3.1 Core phenotype spectrum
Intracranial berry aneurysm phenotypes are typically separated into:
1) **Unruptured aneurysm (UIA):** often asymptomatic and discovered incidentally. (ricecanetto2025areviewof pages 2-3)
2) **Ruptured aneurysm → aneurysmal subarachnoid hemorrhage (aSAH):** acute, life-threatening hemorrhagic stroke syndrome. (findlay2025currentmanagementof pages 1-2)

### 3.2 Unruptured aneurysm presentation
- Most unruptured saccular aneurysms are incidental findings; a minority produce symptoms from **mass effect**. (ricecanetto2025areviewof pages 2-3)
- A recent review estimates **~5–6%** present with mass effect symptoms, including cranial nerve palsies such as **oculomotor nerve palsy** (e.g., PComm aneurysm) and visual disturbance from optic pathway compression. (ricecanetto2025areviewof pages 2-3)

**Suggested HPO terms (examples)**
- Asymptomatic clinical course: **HP:0000007** (Clinical course; general placeholder—HPO exact mapping not in evidence)
- Cranial nerve palsy / oculomotor palsy: **HP:0000602** (Oculomotor palsy)
- Visual impairment: **HP:0000505** (Visual impairment)

### 3.3 Rupture / aSAH phenotype
Aneurysmal rupture typically presents with:
- **Thunderclap headache** (classic “worst headache of my life”) and frequently **nausea/vomiting** and reduced consciousness. (findlay2025currentmanagementof pages 1-2, ricecanetto2025areviewof pages 2-3)
- **Meningeal signs** (neck pain/stiffness) and possible focal deficits. (ricecanetto2025areviewof pages 2-3, findlay2025currentmanagementof pages 2-4)
- **Seizures:** one review notes seizures in **up to 25%** of SAH. (ricecanetto2025areviewof pages 2-3)

**Suggested HPO terms (examples)**
- Thunderclap headache: **HP:0032801** (Thunderclap headache)
- Nausea: **HP:0002018**; vomiting: **HP:0002013**
- Altered level of consciousness: **HP:0001250**
- Seizure: **HP:0001250** (note: HPO uses separate term **HP:0001250** for seizures?; exact mapping should be validated externally)
- Nuchal rigidity: **HP:0003306**

### 3.4 Complications and phenotype frequencies
A recent clinical review notes early and delayed complications after rupture including **acute hydrocephalus** and **delayed arterial vasospasm** leading to ischemia. (findlay2025currentmanagementof pages 1-2)

A recent review reports major outcome and complication statistics:
- After rupture, **25% die within 24 hours**, and an additional **25% die within 6 months**, with complications including rebleeding, hydrocephalus, vasospasm, seizures, cardiac stress, and hyponatremia. (ricecanetto2025areviewof pages 4-5)

### 3.5 Quality of life impact
Quality-of-life and mental health impacts for unruptured aneurysms (anxiety, QoL decrement during surveillance) are recognized clinically, but **explicit QoL statistics were not present in the retrieved 2023–2024 evidence corpus** used for this report. Therefore, this section cannot be populated with cited quantitative estimates from the current tool outputs.


## 4. Genetic / molecular information

### 4.1 Causal or high-confidence genes (evidence-based)

#### THSD1 (thrombospondin type 1 domain containing 1)
A primary Stroke study provides multi-layer evidence:
- Human genetics: family-based segregation and case enrichment in 507 probands. (santiagosim2016thsd1(thrombospondintype pages 2-4)
- Functional endothelial cell phenotypes: focal-adhesion/basement membrane adhesion defects (HUVEC-based), with rescue by wild-type THSD1. (santiagosim2016thsd1(thrombospondintype pages 1-2)
- Animal models: zebrafish morpholino knockdown and mouse models showing cerebral bleeding (subarachnoid localization in mouse). (santiagosim2016thsd1(thrombospondintype pages 1-2)

**Example pathogenic variant information (from the study evidence)**
- **R450X (nonsense)**: truncates protein intracellular domain; reported LOD 4.69 in a pedigree and absent in controls and ExAC chromosomes in the cited analysis. (santiagosim2016thsd1(thrombospondintype pages 2-4)

**OpenTargets disease–target evidence**
OpenTargets links THSD1 to MONDO_0016483 (“intracranial berry aneurysm”) with supporting PubMed evidence including PMID **27895300** (THSD1 paper). (OpenTargets Search: intracranial aneurysm)

#### NPNT and CBY2 (susceptibility genes in a multiplex family)
- NPNT splicing donor **c.1515+1G>A** causes aberrant splicing (minigene assay). (maegawa2022wholeexomesequencingin pages 1-2)
- CBY2 missense **p.P83T** and other deleterious CBY2 variants are enriched in probands (8/501) vs controls (0/323). (maegawa2022wholeexomesequencingin pages 1-2)

### 4.2 Modifier genes
No specific modifier-gene effects (variant altering penetrance/severity) were extractable with citations from the retrieved evidence set.

### 4.3 Epigenetic information
No primary epigenetic profiling datasets specific to intracranial berry aneurysm were extractable with citations from the retrieved evidence set.


## 5. Environmental information
Key non-genetic contributors include **blood pressure elevation**, **smoking**, heavy alcohol, and sympathomimetic drug exposure, with strong genetic-instrumented evidence supporting blood pressure as causal for IA and aSAH risk. (liu2024geneticallydeterminedblood pages 2-4, findlay2025currentmanagementof pages 1-2)


## 6. Mechanism / pathophysiology

### 6.1 Causal chain (integrated)
A mechanistically consistent chain supported across consensus/reviews and primary genetics is:
1) **Hemodynamic stress** concentrated at arterial bifurcations and branch points within the Circle of Willis (initiation context). (ricecanetto2025areviewof pages 2-3)
2) **Endothelial dysfunction and vascular wall remodeling** with inflammatory and ECM processes, leading to weakened arterial wall architecture. (tjoumakaris2024ariseiconsensus pages 4-5)
3) **Aneurysm growth and morphological change** (irregular shape, enlargement) in higher-risk lesions; rupture risk depends on size/location/morphology and patient factors. (tjoumakaris2024ariseiconsensus pages 4-5, bandhauer2024fromconservativeto pages 1-2)
4) **Rupture → aSAH**, followed by acute brain injury (hydrocephalus, rebleeding risk) and delayed complications (vasospasm/ischemia). (findlay2025currentmanagementof pages 1-2)

### 6.2 Key pathways and cellular processes (evidence-backed highlights)
- **VEGF signaling:** a 2024 systematic review states that “Recent research has increasingly implicated vascular endothelial growth factor (VEGF) in the development and rupture of intracranial aneurysms.” (OpenTargets Search: intracranial aneurysm) Specifically, it summarizes elevated VEGF expression in IA tissue and fluids and discusses uncertainty about causality. (OpenTargets Search: intracranial aneurysm)
- **Endothelial focal adhesion / basement membrane anchoring:** THSD1 loss-of-function impairs endothelial focal adhesion, providing a plausible molecular mechanism for wall vulnerability. (santiagosim2016thsd1(thrombospondintype pages 1-2)

### 6.3 Suggested ontology terms
**GO Biological Process (examples)**
- Extracellular matrix organization (GO:0030198)
- Inflammatory response (GO:0006954)
- Response to shear stress (GO:0034616)
- Cell–substrate adhesion (GO:0031589)

**Cell Ontology (CL) cell types (examples)**
- Endothelial cell (CL:0000115)
- Vascular smooth muscle cell (CL:0000359)
- Pericyte (CL:0000669)
- Macrophage (CL:0000235)

(These ontology suggestions are consistent with the biology discussed in the evidence but are not explicitly enumerated as ontology mappings in the retrieved texts.)


## 7. Anatomical structures affected

### 7.1 Organ/system level
- Primary system: **cerebrovascular / nervous system**.
- Clinical consequence: hemorrhagic stroke syndrome (aSAH). (findlay2025currentmanagementof pages 1-2)

### 7.2 Localization (key sites)
- Predominantly within the **Circle of Willis**; one review notes nearly 90% localize there, and a 2024 review notes ~85% in anterior circulation. (ricecanetto2025areviewof pages 2-3, tataranu2024advancementsinbrain pages 4-5)
- Common sites include AComm–ACA, PComm–ICA, and MCA bifurcations; AComm aneurysms are particularly common and rupture-prone in cited reviews. (ricecanetto2025areviewof pages 2-3, tataranu2024advancementsinbrain pages 4-5)

**Suggested UBERON terms (examples)**
- Circle of Willis: UBERON:0004708
- Middle cerebral artery: UBERON:0001647
- Internal carotid artery: UBERON:0001555
- Anterior communicating artery: UBERON:0001608


## 8. Temporal development

### 8.1 Onset
Saccular aneurysms are generally considered acquired/developmental lesions that usually form in adulthood and are often detected incidentally in middle age; mean diagnosis age around ~50 years is cited in a recent review. (ricecanetto2025areviewof pages 2-3)

### 8.2 Progression
Progression is heterogeneous: many UIAs remain stable, while a subset grows or changes morphology, prompting intervention. In one cohort of conservatively managed UIAs, 6.9% converted to intervention over a median 26-month follow-up, predominantly triggered by documented aneurysm growth or configuration change. (bandhauer2024fromconservativeto pages 1-2)


## 9. Inheritance and population

### 9.1 Epidemiology
Prevalence estimates vary by method and population:
- ARISE consensus cites UIA prevalence estimates from **0.2% to 10%**. (tjoumakaris2024ariseiconsensus pages 1-3)
- Reviews cite worldwide prevalence in the **2–4%** range. (findlay2025currentmanagementof pages 1-2)

### 9.2 Familial risk
- OR for SAH is reported as **51.0** when **≥2 first-degree relatives** have SAH, emphasizing the magnitude of familial risk in high-risk pedigrees. (santiagosim2016thsd1(thrombospondintype pages 2-2)

### 9.3 Sex differences
- ARISE consensus notes higher incidence in females with relative risk ~2.1. (tjoumakaris2024ariseiconsensus pages 1-3)
- A 2024 review reports an odds ratio of 1.92 for higher prevalence of incidental unruptured aneurysm in females and additional sex-associated growth/de novo formation signals. (tataranu2024advancementsinbrain pages 1-2)


## 10. Diagnostics

### 10.1 Imaging
- In practice and consensus, **digital subtraction angiography (DSA)** with 3D reconstructions is described as the diagnostic gold standard, with **CTA/MRA** as key noninvasive modalities. (tjoumakaris2024ariseiconsensus pages 1-3, ricecanetto2025areviewof pages 2-3)
- For suspected aSAH, **noncontrast CT** is a key first test, typically followed by vessel imaging (CTA/MRA) and/or DSA for aneurysm definition. (ricecanetto2025areviewof pages 2-3)

### 10.2 Emerging diagnostics / biomarkers
- ARISE highlights advanced imaging approaches including contrast-enhanced **3T vessel wall MRI** and intravascular imaging (OCT/IVUS) as promising but requiring more data. (tjoumakaris2024ariseiconsensus pages 1-3)
- Aneurysm wall enhancement on high-resolution imaging is associated with markedly increased prevalence ratios for rupture (11.47) and interval growth (4.62). (tjoumakaris2024ariseiconsensus pages 4-5)

### 10.3 Screening and surveillance
ARISE provides evidence-graded recommendations for noninvasive management surveillance:
- Follow-up with **MRA or CTA** at regular intervals (Class I, Level B).
- A first follow-up at **6–12 months**, then **yearly or every other year** may be reasonable (Class IIb, Level C). (tjoumakaris2024ariseiconsensus pages 4-5)

High-risk group screening highlights:
- **ADPKD**: IA incidence ≈10%; screening and surveillance every 5 years is recommended in the ARISE discussion. (tjoumakaris2024ariseiconsensus pages 4-5)


## 11. Outcome / prognosis

### 11.1 Unruptured aneurysm
Many UIAs remain stable; in one cohort of 144 conservatively managed UIAs, no ruptures occurred over a median 24.5 months follow-up. (bandhauer2024fromconservativeto pages 1-2)

### 11.2 Ruptured aneurysm / aSAH
Ruptured aneurysms are associated with high early and medium-term mortality:
- Review estimate: 25% die within 24 hours and another 25% die within 6 months, often from complications (rebleeding, hydrocephalus, vasospasm, etc.). (ricecanetto2025areviewof pages 4-5)


## 12. Treatment

### 12.1 Interventional treatments (current standard)
Core treatment modalities aim to exclude the aneurysm from circulation:
- **Microsurgical clipping**
- **Endovascular coiling/embolization**
- **Flow diversion**

These approaches are emphasized in 2024 reviews and consensus discussions. (tataranu2024advancementsinbrain pages 1-2, tjoumakaris2024ariseiconsensus pages 1-3)

**Suggested MAXO terms (examples; to be validated in MAXO)**
- Surgical clipping of aneurysm (MAXO term not provided in evidence)
- Endovascular coil embolization (MAXO term not provided in evidence)
- Flow diversion stent placement (MAXO term not provided in evidence)

### 12.2 Flow diversion: outcomes and implementation (recent quantitative data)
A 2023 meta-analysis of long-term (>1 year) outcomes of flow diversion for unruptured aneurysms reported pooled occlusion rates increasing over time: 77% (1y) to 96% (5y), with in-stent stenosis 4.8% and retreatment 5%. (bandhauer2024fromconservativeto pages 1-2)

### 12.3 aSAH acute management concepts (clinical practice)
A clinical management review emphasizes immediate pain and BP control, potential EVD for hydrocephalus, short-term antifibrinolytic therapy, and rapid aneurysm securing, followed by vigilance and treatment for vasospasm/ischemia (including induced hypertension and possible endovascular angioplasty). (findlay2025currentmanagementof pages 1-2)

### 12.4 Clinical trials (real-world implementation)
Multiple flow-diverter studies are active or completed, including large observational registries and small interventional feasibility studies (examples): **NCT05646108 (Tubridge; 5000 planned), NCT06943729 (523), NCT06872684 (GUARD; 183), NCT04918420 (Tonbridge; 142)**. (OpenTargets Search: intracranial aneurysm)


## 13. Prevention

### 13.1 Primary prevention
- Blood pressure control is strongly supported by causal genetic evidence (MR) as a lever to reduce IA and SAH risk. (liu2024geneticallydeterminedblood pages 2-4)
- Avoidance/reduction of smoking and stimulant exposure is consistently highlighted in clinical review risk factors. (findlay2025currentmanagementof pages 1-2, ricecanetto2025areviewof pages 2-3)

### 13.2 Secondary prevention (screening/high-risk surveillance)
- Screening and repeat surveillance are emphasized for high-risk groups (familial IA, ADPKD) with evidence-based follow-up intervals noted above. (tjoumakaris2024ariseiconsensus pages 4-5)

### 13.3 Tertiary prevention
- For aSAH: prevention of rebleeding via early aneurysm securing and prevention/mitigation of secondary brain injury (hydrocephalus and vasospasm) is a central prevention concept. (findlay2025currentmanagementof pages 1-2)


## 14. Other species / natural disease
No naturally occurring non-human intracranial berry aneurysm epidemiology was retrieved in the current evidence set; however, experimental model systems are used extensively (see §15). (santiagosim2016thsd1(thrombospondintype pages 1-2)


## 15. Model organisms
Primary mechanistic evidence in the current corpus includes:
- **Zebrafish THSD1 ortholog knockdown** (morpholino) with increased cerebral hemorrhage. (santiagosim2016thsd1(thrombospondintype pages 2-4)
- **Mouse Thsd1 models** demonstrating cerebral bleeding (including subarachnoid localization in described findings). (santiagosim2016thsd1(thrombospondintype pages 1-2)
- **In vitro endothelial models (HUVECs)** showing focal-adhesion phenotypes and rescue experiments. (santiagosim2016thsd1(thrombospondintype pages 1-2)


## High-yield summary table

| Domain | Key points | Quantitative data | Best recent sources (with year) | URL / PMID / DOI |
|---|---|---|---|---|
| Definition / synonyms / ontology IDs | Intracranial berry aneurysm = saccular intracranial aneurysm; focal dilation of a weakened cerebral artery wall, typically at branch points or bifurcations in the Circle of Willis; saccular or berry aneurysms are the dominant subtype. MONDO ID supported by OpenTargets: MONDO_0016483 (intracranial berry aneurysm). Related OpenTargets disease terms also include brain aneurysm and aneurysm, intracranial berry, 12. | Saccular or berry aneurysms account for about 90% of intracranial aneurysms; about 85% are in anterior circulation; AComm aneurysms comprise 23 to 40% of all IAs and 12 to 15% of unruptured IAs (tataranu2024advancementsinbrain pages 4-5, tataranu2024advancementsinbrain pages 1-2, OpenTargets Search: intracranial aneurysm) | Tjoumakaris et al. Stroke (2024); Tataranu et al. Medicina (2024); OpenTargets context (current) | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.3390/medicina60111820 |
| Epidemiology | UIA prevalence is variably estimated across studies and guidelines; female predominance is consistent. Rupture leads to aneurysmal SAH. | UIA prevalence 0.2 to 10% in ARISE review; other recent reviews cite 2 to 4%, 3 to 5%, or 3.6 to 6%. Female relative risk about 2.1 in ARISE; female OR for incidental UIA 1.92 (95% CI 1.33 to 2.84). Mean age in treated UIA meta-analysis 55.5 years; 70.7% female (tjoumakaris2024ariseiconsensus pages 1-3, findlay2025currentmanagementof pages 1-2, ricecanetto2025areviewof pages 2-3, ricecanetto2025areviewof pages 1-2, tataranu2024advancementsinbrain pages 1-2, bandhauer2024fromconservativeto pages 1-2) | Tjoumakaris et al. (2024); Findlay (2025); Rice-Canetto et al. (2025); Tataranu et al. (2024); Khorasanizadeh et al. (2023) | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.3390/neurolint17030036 ; https://doi.org/10.7759/cureus.80223 ; https://doi.org/10.3390/medicina60111820 ; https://doi.org/10.3171/2023.2.JNS222919 |
| Rupture risk and natural history | Rupture risk rises with aneurysm size, growth, and location; incidental aneurysms are common. Growth or morphologic change often drives treatment conversion. | Reported annual rupture risk: about 0.5% for small UIAs under 5 mm; about 1 to 2% average for incidentally found saccular aneurysms in one review; another review cites 0.7 to 1.9% annual bleed or rupture. In a conservative cohort, 10 of 144 patients (6.9%) later converted to intervention after median 26 months; 0 ruptures during median 24.5 months follow-up (bandhauer2024fromconservativeto pages 1-2, findlay2025currentmanagementof pages 1-2, ricecanetto2025areviewof pages 2-3, tjoumakaris2024ariseiconsensus pages 4-5) | Bandhauer et al. (2024); Findlay (2025); Rice-Canetto et al. (2025); ARISE I (2024) | https://doi.org/10.48620/75950 ; https://doi.org/10.3390/neurolint17030036 ; https://doi.org/10.7759/cureus.80223 ; https://doi.org/10.1161/STROKEAHA.123.046208 |
| Familial risk and population subsets | Family history materially increases risk; screening is emphasized for familial IA and ADPKD. | Familial IA with at least 2 first-degree relatives: screening yield 4 to 11% and lifetime SAH risk up to 20%; with 1 first-degree relative, lifetime rupture risk 3 to 4%. THSD1 paper cites SAH OR 51.0 (95% CI 8.56 to 1117) when at least 2 affected first-degree relatives have SAH; SAH heritability 41% in Nordic twin study. ADPKD incidence or prevalence of IA about 10% (tjoumakaris2024ariseiconsensus pages 4-5, santiagosim2016thsd1(thrombospondintype pages 2-2, santiagosim2016thsd1(thrombospondintype pages 1-2) | Tjoumakaris et al. (2024); Santiago-Sim et al. (2016) | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.1161/STROKEAHA.116.014161 |
| Major risk factors | Established non-genetic risks include hypertension, smoking, female sex, age, heavy alcohol, stimulant use; aneurysm-specific factors include size, location, morphology, and wall enhancement. | Mendelian randomization: per genetically predicted 10 mmHg higher SBP, OR for IA 1.73 (1.45 to 2.05) and SAH 1.93 (1.52 to 2.45); per 5 mmHg higher DBP, OR for IA 1.62 (1.39 to 1.89) and SAH 1.64 (1.33 to 2.01); per 1 mmHg higher pulse pressure, OR for IA 1.06 (1.03 to 1.10) and SAH 1.04 (1.01 to 1.08). Vessel wall enhancement prevalence ratio: rupture 11.47, interval growth 4.62 (liu2024geneticallydeterminedblood pages 2-4, liu2024geneticallydeterminedblood pages 1-2, tjoumakaris2024ariseiconsensus pages 4-5, ricecanetto2025areviewof pages 2-3, findlay2025currentmanagementof pages 1-2, tataranu2024advancementsinbrain pages 4-5) | Liu et al. European Stroke Journal (2024); Tjoumakaris et al. (2024); Rice-Canetto et al. (2025); Findlay (2025); Tataranu et al. (2024) | https://doi.org/10.1177/23969873231204420 ; https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.7759/cureus.80223 ; https://doi.org/10.3390/neurolint17030036 ; https://doi.org/10.3390/medicina60111820 |
| Protective factors | No established pharmacologic preventive therapy yet; some genetic or behavioral signals are investigational only. Fresh fruit intake has Mendelian randomization support; absence of vessel wall enhancement may suggest stability. | Mendelian randomization estimated fresh fruit intake OR for IA 0.28 (95% CI 0.13 to 0.59); no causal relationship found for alcohol or coffee in that MR study. ARISE notes absence of aneurysm wall enhancement is more useful for establishing stability than presence is for proving rupture (tjoumakaris2024ariseiconsensus pages 4-5, tjoumakaris2024ariseiconsensus media f6212793) | ARISE I (2024); Li et al. (2025) as cited in retrieved evidence summary | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.3390/biomedicines13030533 |
| Key genetic finding: THSD1 | Rare familial or susceptibility gene with strong mechanistic support; supported in OpenTargets for MONDO_0016483. Loss of function affects endothelial adhesion and focal adhesions and causes cerebral bleeding in models. | Familial nonsense R450X: LOD 4.69, reported penetrance 100%, allele frequency 0.001; absent in 305 controls and 89040 ExAC chromosomes. THSD1 mutations found in 8 of 507 unrelated IA probands (1.6%, 95% CI 0.8 to 3.1%). OpenTargets links THSD1 to intracranial berry aneurysm and brain aneurysm (santiagosim2016thsd1(thrombospondintype pages 2-2, santiagosim2016thsd1(thrombospondintype pages 2-4, santiagosim2016thsd1(thrombospondintype pages 1-2, OpenTargets Search: intracranial aneurysm) | Santiago-Sim et al. Stroke (2016); OpenTargets context (current) | https://doi.org/10.1161/STROKEAHA.116.014161 |
| Key genetic finding: NPNT and CBY2 | Family-based WES identified novel susceptibility genes in a Japanese multiplex family. NPNT splice defect and CBY2 rare missense burden support susceptibility. | NPNT c.1515+1G>A caused aberrant splicing; CBY2 p.P83T showed cytoplasmic aggregation. Targeted CBY2 resequencing: deleterious variants 8 of 501 probands versus 0 of 323 controls (p = 0.026); variants included p.R46H, p.P83T, and p.L183R (maegawa2022wholeexomesequencingin pages 1-2) | Maegawa et al. PLoS One (2022) | https://doi.org/10.1371/journal.pone.0265359 |
| Key GWAS and polygenic findings | Polygenic architecture with at least 17 to 22 susceptibility loci; pathways point to matrix biology, vascular smooth muscle or pericytes, inflammation, and endothelial signaling. | 2025 multi-ancestry GWAS and meta-analysis: 15438 cases and 1183973 controls, 5 novel associations, total known loci increased to 22; PRS associated with IA across ancestries: European OR 1.87, African OR 1.62, Hispanic OR 2.28. Earlier large GWAS identified 17 loci; genes mentioned across evidence include SOX17, CDKN2B-AS1 or CDKN2B, CNNM2, RBBP8, EDNRA, ATP2B1, STARD13, RP1, and CTAGE1 (baloi2026basicmolecularand pages 2-3, changez2025geneticoverlapof pages 8-9, OpenTargets Search: intracranial aneurysm) | Adkar et al. (2025); summarized in Baloi review (2026); OpenTargets context | https://doi.org/10.1161/CIRCGEN.123.004626 |
| Molecular mechanisms and pathophysiology | Hemodynamic stress at bifurcations triggers endothelial dysfunction, inflammation, smooth-muscle or pericyte remodeling, ECM degradation, and wall instability. VEGF, NF-kB, PDGFRB-ERK, focal adhesion, and matrix-production pathways are recurrent themes. | ARISE and other recent reviews emphasize rupture or growth risk from size, location, morphology, and wall imaging. VEGF overexpression reported in IA tissue, CSF, and systemically; THSD1 loss impairs focal adhesion; 2025 genetics study implicates pericytes and smooth muscle cells; review notes EP2-NF-kB and PDGFRB-ERK-NF-kB axes (tjoumakaris2024ariseiconsensus pages 4-5, santiagosim2016thsd1(thrombospondintype pages 2-4, baloi2026basicmolecularand pages 2-3, changez2025geneticoverlapof pages 8-9) | Nisson et al. (2024); Adkar et al. (2025); Santiago-Sim et al. (2016); ARISE I (2024) | https://doi.org/10.1161/JAHA.124.035638 ; https://doi.org/10.1161/CIRCGEN.123.004626 ; https://doi.org/10.1161/STROKEAHA.116.014161 ; https://doi.org/10.1161/STROKEAHA.123.046208 |
| Diagnostics | DSA remains gold standard; CTA and MRA are standard noninvasive tools; vessel wall MRI and intravascular imaging are promising adjuncts. In SAH, noncontrast CT followed by vascular imaging is standard. | Machine-learning CTA detection sensitivity and specificity about 93.8% and 94.2%. ARISE notes vessel wall enhancement linked to rupture PR 11.47 and growth PR 4.62. CTA diagnosis of aSAH described as high sensitivity and specificity; DSA provides morphology and orientation detail (tjoumakaris2024ariseiconsensus pages 4-5, tjoumakaris2024ariseiconsensus pages 1-3, findlay2025currentmanagementof pages 1-2, tjoumakaris2024ariseiconsensus media f6212793) | Tjoumakaris et al. (2024); Findlay (2025); Shaikh et al. (2024, cited in evidence summary) | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.3390/neurolint17030036 ; https://doi.org/10.5772/intechopen.1006662 |
| Screening and surveillance | High-risk groups: familial IA, ADPKD, selected connective-tissue vasculopathies. Noninvasive follow-up with MRA or CTA at regular intervals; early re-imaging after diagnosis is common. | ADPKD: initial screening plus surveillance every 5 years. UIA follow-up: first imaging at 6 to 12 months, then yearly or every other year may be reasonable. Institutional conservative-management series recommends close radiographic follow-up, especially if aneurysm is greater than 3 mm (tjoumakaris2024ariseiconsensus pages 4-5, bandhauer2024fromconservativeto pages 1-2, tjoumakaris2024ariseiconsensus media f6212793) | Tjoumakaris et al. (2024); Bandhauer et al. (2024) | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.48620/75950 |
| Treatment overview | Main active treatments are microsurgical clipping, endovascular coiling or embolization, and flow diversion; choice depends on rupture status, size, neck, location, morphology, age, and center expertise. Ruptured aneurysms should be managed in high-volume multidisciplinary centers. | Recent Germany-wide analysis across 77684 procedures found outcome differences by modality; in unruptured IA, balloon-assisted coiling, stent-assisted coiling, and intrasaccular flow disruption improved functional independence versus standard coiling, while neurosurgical clipping reduced it; in ruptured IA, SAC, FD, and NSC had worse outcomes than standard coiling (tjoumakaris2024ariseiconsensus pages 1-3, bandhauer2024fromconservativeto pages 1-2) | ARISE I (2024); Vagkopoulos et al. (2025 preprint, from retrieved evidence) | https://doi.org/10.1161/STROKEAHA.123.046208 ; https://doi.org/10.1101/2025.09.23.25336516 |
| Flow diversion outcomes | Flow diversion is increasingly used for selected unruptured aneurysms and some complex lesions; durability is strong but antiplatelet-related issues remain important. | Long-term meta-analysis: pooled complete occlusion after FD 77% at 1 year, 87.4% at 1 to 2 years, 84.5% at 2 years, 89.4% at 3 years, and 96% at 5 years; in-stent stenosis 4.8%, retreatment 5%. Single-center decade study: complete occlusion 72.7%, complications 9.1%; recent era improved occlusion 79.7% versus 61.7% and lower complications 4.1% versus 14.9%. Severe in-stent stenosis in one 2025 series: 5.6% (bandhauer2024fromconservativeto pages 1-2, tataranu2024advancementsinbrain pages 4-5) | Shehata et al. Journal of NeuroInterventional Surgery (2023); Jee et al. Brain Sciences (2024); Alshahrani et al. (2025 summary in retrieved evidence) | https://doi.org/10.1136/jnis-2022-019240 ; https://doi.org/10.3390/brainsci14080847 ; https://doi.org/10.1007/s00701-025-06597-2 |
| Ruptured aneurysm and aSAH management | Emergency priorities: pain and BP control, EVD for hydrocephalus or poor grade, rapid aneurysm securing, then vigilance for delayed cerebral ischemia and vasospasm. | Reviews note repair ideally within 24 to 72 hours after rupture. In one 2024 single-center FD-for-rupture cohort with 39 patients and 40 ruptured IAs, ischemic complications were 37 to 42%, hemorrhagic complications 30 to 33%, and pre-protocol rerupture 11% with none after protocol implementation (findlay2025currentmanagementof pages 1-2, tjoumakaris2024ariseiconsensus pages 1-3) | Findlay (2025); Rantamo et al. (2024) | https://doi.org/10.3390/neurolint17030036 ; https://doi.org/10.1007/s00701-024-06029-7 |
| Relevant ongoing or recent clinical trials | Flow-diverter and aneurysm device studies are active in real-world and interventional settings. | Examples: NCT06943729 observational safety and efficacy study of flow diverters, enrollment 523; NCT05646108 Tubridge flow diverter observational study, enrollment 5000; NCT06411418 evaluation of flow diverter technology device, enrollment 10; NCT06731946 Surpass Evolve flow diverter observational study, enrollment 150; NCT07420179 Derivo 2 Heal versus Derivo 2, enrollment 21; NCT04918420 single-arm Tonbridge FD trial, enrollment 142; NCT01716117 large or giant wide-neck aneurysm embolization system trial, enrollment 213; NCT06872684 GUARD trial, enrollment 183; NCT05060185 FD trial, enrollment 166 (OpenTargets Search: intracranial aneurysm) | ClinicalTrials.gov records retrieved in current evidence context | https://clinicaltrials.gov/study/NCT06943729 ; https://clinicaltrials.gov/study/NCT05646108 ; https://clinicaltrials.gov/study/NCT06411418 ; https://clinicaltrials.gov/study/NCT06731946 ; https://clinicaltrials.gov/study/NCT07420179 ; https://clinicaltrials.gov/study/NCT04918420 ; https://clinicaltrials.gov/study/NCT01716117 ; https://clinicaltrials.gov/study/NCT06872684 ; https://clinicaltrials.gov/study/NCT05060185 |


*Table: This table consolidates disease definition, epidemiology, risk factors, genetics, diagnostics, surveillance, and treatment evidence for intracranial berry aneurysm using only supported context IDs. It is designed as a compact reference for downstream knowledge base population and citation tracing.*


## Direct abstract quotes (for key claims)

- ARISE I (Stroke, May 2024) abstract: “**There is a plethora of microsurgical and endovascular techniques for the treatment of both ruptured and unruptured aneurysms. There is no definitive consensus as to the best treatment option for this cerebrovascular pathology.**” (tjoumakaris2024ariseiconsensus pages 1-3)
- ARISE I (Stroke, May 2024) abstract: “**The consensus strongly recommended nationwide systemic data collection of unruptured IA radiographic images for the analysis and development of machine learning algorithms for rupture risk.**” (tjoumakaris2024ariseiconsensus pages 4-5)
- BP Mendelian randomization (European Stroke Journal, Oct 2024) abstract: “**This MR analysis supports the role of elevated blood pressure in the occurrence of intracranial aneurysms and subarachnoid hemorrhage.**” (liu2024geneticallydeterminedblood pages 1-2)


## Limitations of this report (based on available retrieved evidence)
1) **ICD-10/ICD-11, MeSH, OMIM, and Orphanet identifiers** were not directly available in the retrieved text corpus; therefore they are not populated with citations here.
2) Despite prioritizing 2023–2024, several key clinical phenotype and outcome statistics in the retrieved set came from 2025 reviews; these are included only when they contain quantitative data not present in 2023–2024 sources captured by the tools.
3) Quality-of-life statistics for untreated UIA and long-term neurocognitive outcomes after aSAH were not present in the retrieved evidence set, so QoL cannot be quantitatively summarized with citations.


References

1. (tataranu2024advancementsinbrain pages 4-5): Ligia Gabriela Tataranu, Octavian Munteanu, Amira Kamel, Karina Lidia Gheorghita, and Radu Eugen Rizea. Advancements in brain aneurysm management: integrating neuroanatomy, physiopathology, and neurosurgical techniques. Medicina, 60:1820, Nov 2024. URL: https://doi.org/10.3390/medicina60111820, doi:10.3390/medicina60111820. This article has 5 citations.

2. (ricecanetto2025areviewof pages 2-3): Tyler E Rice-Canetto, Arisa Ueno, Eric Whitney, Louis Reier, Rebecca Houston, and Javed Siddiqi. A review of the current literature on cerebral aneurysms. Cureus, Mar 2025. URL: https://doi.org/10.7759/cureus.80223, doi:10.7759/cureus.80223. This article has 4 citations.

3. (OpenTargets Search: intracranial aneurysm): Open Targets Query (intracranial aneurysm, 17 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (tjoumakaris2024ariseiconsensus pages 1-3): MD Stavropoula I. Tjoumakaris, MD Ricardo Hanel, PhD J Mocco, MD M. Ali-Aziz, MD Mba Michael Froehler Sultan, PhD Barry B. Lieber, MD Alexander Coon, MD Satoshi Tateshima, MD David J. Altschul, MD Sandra Narayanan, MD Kareem El Naamani, MD Phil Taussky, MD Brian L. Hoh, MD Philip Meyers, PhD Matthew J. Gounis, MD David S. Liebeskind, MD Victor Volovici, PhD Gabor Toth, MD Adam Arthur, and MD Ajay K. Wakhloo. Arise i consensus review on the management of intracranial aneurysms. Stroke, 55:1428-1437, May 2024. URL: https://doi.org/10.1161/strokeaha.123.046208, doi:10.1161/strokeaha.123.046208. This article has 36 citations and is from a highest quality peer-reviewed journal.

5. (bandhauer2024fromconservativeto pages 1-2): Benedikt Bandhauer, Philipp Gruber, Lukas Andereggen, Jatta Berberat, Stefan Wanderer, Marco Cattaneo, Gerrit A Schubert, Luca Remonda, Serge Marbacher, and Basil E Grüter. From conservative to interventional management in unruptured intracranial aneurysms. JournalArticle, Sep 2024. URL: https://doi.org/10.48620/75950, doi:10.48620/75950. This article has 5 citations.

6. (liu2024geneticallydeterminedblood pages 1-2): Hanchen Liu, Huiqin Zuo, Ospel Johanna, Rui Zhao, Pengfei Yang, Weixing Chen, Qiang Li, Xiaolei Lin, Yu Zhou, and Jianmin Liu. Genetically determined blood pressure, antihypertensive medications, and risk of intracranial aneurysms and aneurysmal subarachnoid hemorrhage: a mendelian randomization study. European Stroke Journal, 9:244-250, Oct 2024. URL: https://doi.org/10.1177/23969873231204420, doi:10.1177/23969873231204420. This article has 18 citations and is from a peer-reviewed journal.

7. (tjoumakaris2024ariseiconsensus pages 4-5): MD Stavropoula I. Tjoumakaris, MD Ricardo Hanel, PhD J Mocco, MD M. Ali-Aziz, MD Mba Michael Froehler Sultan, PhD Barry B. Lieber, MD Alexander Coon, MD Satoshi Tateshima, MD David J. Altschul, MD Sandra Narayanan, MD Kareem El Naamani, MD Phil Taussky, MD Brian L. Hoh, MD Philip Meyers, PhD Matthew J. Gounis, MD David S. Liebeskind, MD Victor Volovici, PhD Gabor Toth, MD Adam Arthur, and MD Ajay K. Wakhloo. Arise i consensus review on the management of intracranial aneurysms. Stroke, 55:1428-1437, May 2024. URL: https://doi.org/10.1161/strokeaha.123.046208, doi:10.1161/strokeaha.123.046208. This article has 36 citations and is from a highest quality peer-reviewed journal.

8. (santiagosim2016thsd1(thrombospondintype pages 1-2): Teresa Santiago-Sim, Xiaoqian Fang, Morgan L. Hennessy, Stephen V. Nalbach, Steven R. DePalma, Ming Sum Lee, Steven C. Greenway, Barbara McDonough, Georgene W. Hergenroeder, Kyla J. Patek, Sarah M. Colosimo, Krista J. Qualmann, John P. Hagan, Dianna M. Milewicz, Calum A. MacRae, Susan M. Dymecki, Christine E. Seidman, J.G. Seidman, and Dong H. Kim. Thsd1 (thrombospondin type 1 domain containing protein 1) mutation in the pathogenesis of intracranial aneurysm and subarachnoid hemorrhage. Stroke, 47:3005–3013, Dec 2016. URL: https://doi.org/10.1161/strokeaha.116.014161, doi:10.1161/strokeaha.116.014161. This article has 78 citations and is from a highest quality peer-reviewed journal.

9. (santiagosim2016thsd1(thrombospondintype pages 2-2): Teresa Santiago-Sim, Xiaoqian Fang, Morgan L. Hennessy, Stephen V. Nalbach, Steven R. DePalma, Ming Sum Lee, Steven C. Greenway, Barbara McDonough, Georgene W. Hergenroeder, Kyla J. Patek, Sarah M. Colosimo, Krista J. Qualmann, John P. Hagan, Dianna M. Milewicz, Calum A. MacRae, Susan M. Dymecki, Christine E. Seidman, J.G. Seidman, and Dong H. Kim. Thsd1 (thrombospondin type 1 domain containing protein 1) mutation in the pathogenesis of intracranial aneurysm and subarachnoid hemorrhage. Stroke, 47:3005–3013, Dec 2016. URL: https://doi.org/10.1161/strokeaha.116.014161, doi:10.1161/strokeaha.116.014161. This article has 78 citations and is from a highest quality peer-reviewed journal.

10. (maegawa2022wholeexomesequencingin pages 1-2): Tatsuya Maegawa, Hiroyuki Akagawa, Hideaki Onda, and Hidetoshi Kasuya. Whole-exome sequencing in a japanese multiplex family identifies new susceptibility genes for intracranial aneurysms. PLoS ONE, 17:e0265359, Mar 2022. URL: https://doi.org/10.1371/journal.pone.0265359, doi:10.1371/journal.pone.0265359. This article has 8 citations and is from a peer-reviewed journal.

11. (liu2024geneticallydeterminedblood pages 2-4): Hanchen Liu, Huiqin Zuo, Ospel Johanna, Rui Zhao, Pengfei Yang, Weixing Chen, Qiang Li, Xiaolei Lin, Yu Zhou, and Jianmin Liu. Genetically determined blood pressure, antihypertensive medications, and risk of intracranial aneurysms and aneurysmal subarachnoid hemorrhage: a mendelian randomization study. European Stroke Journal, 9:244-250, Oct 2024. URL: https://doi.org/10.1177/23969873231204420, doi:10.1177/23969873231204420. This article has 18 citations and is from a peer-reviewed journal.

12. (findlay2025currentmanagementof pages 1-2): Jay Max Findlay. Current management of aneurysmal subarachnoid hemorrhage. Neurology International, 17:36, Feb 2025. URL: https://doi.org/10.3390/neurolint17030036, doi:10.3390/neurolint17030036. This article has 3 citations.

13. (tataranu2024advancementsinbrain pages 1-2): Ligia Gabriela Tataranu, Octavian Munteanu, Amira Kamel, Karina Lidia Gheorghita, and Radu Eugen Rizea. Advancements in brain aneurysm management: integrating neuroanatomy, physiopathology, and neurosurgical techniques. Medicina, 60:1820, Nov 2024. URL: https://doi.org/10.3390/medicina60111820, doi:10.3390/medicina60111820. This article has 5 citations.

14. (findlay2025currentmanagementof pages 2-4): Jay Max Findlay. Current management of aneurysmal subarachnoid hemorrhage. Neurology International, 17:36, Feb 2025. URL: https://doi.org/10.3390/neurolint17030036, doi:10.3390/neurolint17030036. This article has 3 citations.

15. (ricecanetto2025areviewof pages 4-5): Tyler E Rice-Canetto, Arisa Ueno, Eric Whitney, Louis Reier, Rebecca Houston, and Javed Siddiqi. A review of the current literature on cerebral aneurysms. Cureus, Mar 2025. URL: https://doi.org/10.7759/cureus.80223, doi:10.7759/cureus.80223. This article has 4 citations.

16. (santiagosim2016thsd1(thrombospondintype pages 2-4): Teresa Santiago-Sim, Xiaoqian Fang, Morgan L. Hennessy, Stephen V. Nalbach, Steven R. DePalma, Ming Sum Lee, Steven C. Greenway, Barbara McDonough, Georgene W. Hergenroeder, Kyla J. Patek, Sarah M. Colosimo, Krista J. Qualmann, John P. Hagan, Dianna M. Milewicz, Calum A. MacRae, Susan M. Dymecki, Christine E. Seidman, J.G. Seidman, and Dong H. Kim. Thsd1 (thrombospondin type 1 domain containing protein 1) mutation in the pathogenesis of intracranial aneurysm and subarachnoid hemorrhage. Stroke, 47:3005–3013, Dec 2016. URL: https://doi.org/10.1161/strokeaha.116.014161, doi:10.1161/strokeaha.116.014161. This article has 78 citations and is from a highest quality peer-reviewed journal.

17. (ricecanetto2025areviewof pages 1-2): Tyler E Rice-Canetto, Arisa Ueno, Eric Whitney, Louis Reier, Rebecca Houston, and Javed Siddiqi. A review of the current literature on cerebral aneurysms. Cureus, Mar 2025. URL: https://doi.org/10.7759/cureus.80223, doi:10.7759/cureus.80223. This article has 4 citations.

18. (tjoumakaris2024ariseiconsensus media f6212793): MD Stavropoula I. Tjoumakaris, MD Ricardo Hanel, PhD J Mocco, MD M. Ali-Aziz, MD Mba Michael Froehler Sultan, PhD Barry B. Lieber, MD Alexander Coon, MD Satoshi Tateshima, MD David J. Altschul, MD Sandra Narayanan, MD Kareem El Naamani, MD Phil Taussky, MD Brian L. Hoh, MD Philip Meyers, PhD Matthew J. Gounis, MD David S. Liebeskind, MD Victor Volovici, PhD Gabor Toth, MD Adam Arthur, and MD Ajay K. Wakhloo. Arise i consensus review on the management of intracranial aneurysms. Stroke, 55:1428-1437, May 2024. URL: https://doi.org/10.1161/strokeaha.123.046208, doi:10.1161/strokeaha.123.046208. This article has 36 citations and is from a highest quality peer-reviewed journal.

19. (baloi2026basicmolecularand pages 2-3): Denise Baloi, Henry Freeman, Moneebah Ashraf, Michael Karsy, Brandon Lucke-Wold, and Mehrdad Pahlevani. Basic molecular and genetic pathways underlying intracranial aneurysm formation in the era of molecular and targeted therapies: a 10-year review. Journal of Vascular Diseases, 5:15, Mar 2026. URL: https://doi.org/10.3390/jvd5020015, doi:10.3390/jvd5020015. This article has 0 citations.

20. (changez2025geneticoverlapof pages 8-9): Mah I Kan Changez, Afsheen Nasir, Alexandra Sonsino, Syeda Manahil Jeoffrey, Asanish Kalyanasundaram, Mohammad A. Zafar, Bulat A. Ziganshin, and John A. Elefteriades. Genetic overlap of thoracic aortic aneurysms and intracranial aneurysms. Genes, 16:154, Jan 2025. URL: https://doi.org/10.3390/genes16020154, doi:10.3390/genes16020154. This article has 1 citations.