---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:08:05.065631'
end_time: '2026-08-01T17:20:15.024669'
duration_seconds: 729.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peters plus syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Peters_Plus_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peters plus syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peters plus syndrome** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Peters plus syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peters plus syndrome** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Peters plus syndrome: comprehensive disease-characteristics report

## Executive summary

Peters plus syndrome (PPS) is an ultra-rare, congenital, autosomal-recessive multisystem developmental disorder and congenital disorder of O-glycosylation. Molecularly confirmed PPS requires biallelic pathogenic variants in **B3GLCT**—historically **B3GALTL**—together with anterior-segment dysgenesis, usually Peters anomaly, and systemic abnormalities such as short stature/short limbs, brachydactyly, cleft lip/palate, characteristic craniofacial features, and variable neurodevelopmental impairment. It must be distinguished from isolated Peters anomaly and from “Peters-plus-like syndrome,” in which the clinical pattern is similar but biallelic B3GLCT variants are absent. Open Targets identifies B3GLCT as the single associated target for MONDO:0009856, supported by human genetic literature including PMIDs 16909395, 20301637, and 23889335. (OpenTargets Search: Peters plus syndrome, totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 2-3)

The best-established mechanism is loss of an endoplasmic-reticulum glycosylation/quality-control pathway. POFUT2 first O-fucosylates correctly folded thrombospondin type-1 repeats (TSRs); B3GLCT then adds glucose to form **Glcβ1-3Fuc**. Loss of B3GLCT disrupts folding, stabilization, and secretion of a subset of TSR-containing extracellular proteins. There is currently no disease-modifying therapy; care is multidisciplinary, developmental, surgical, and complication-directed. (vasudevan2015petersplussyndrome pages 1-3)

## 1. Disease information

### Definition and classification

PPS is a Mendelian syndromic anterior-segment dysgenesis and congenital glycosylation disorder. Its defining ocular lesion, Peters anomaly, comprises congenital central corneal opacity with abnormal separation/adhesion among cornea, iris, and sometimes lens. Systemic involvement distinguishes PPS from most isolated Peters anomaly. (totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 2-3)

**Key identifiers**

- **MONDO:** MONDO:0009856.
- **OMIM phenotype:** 261540, as reported in the literature.
- **Causal gene:** **B3GLCT**, Ensembl ENSG00000187676; former symbol **B3GALTL**.
- **Orphanet:** PPS is registered as a rare disease, although a numeric ORPHA identifier was not independently verified in the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no PPS-specific code was verified. Coding generally requires broader congenital ocular-malformation, cleft, short-stature, or genetic-syndrome categories; local terminology-service validation is recommended.

Common names include **Peters plus syndrome**, **Peters’-plus syndrome**, **B3GLCT-related Peters plus syndrome**, and older **B3GALTL-related Peters plus syndrome**. “Peters-plus-like syndrome” should not be treated as a synonym for genetically confirmed PPS. (totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 2-3)

The evidence summarized here is aggregated disease-level evidence from peer-reviewed cohorts, case reports, mechanistic experiments, and curated databases—not individual-level EHR data.

## 2. Etiology, risk, protection, and environment

### Causal factor

The primary cause is **biallelic germline pathogenic variation in B3GLCT**, producing autosomal-recessive loss of enzyme function. Affected people are usually homozygous or compound heterozygous; unaffected parents generally carry one allele each. The 2019 molecular case report identified compound heterozygosity for the known canonical splice variant **NM_194318.3:c.660+1G>A (rs80338851)** and novel frameshift **c.755delC, p.Thr252fs**. Its abstract states: “PPS, a very rare subtype of ASD, is a glycosylation disorder, where the dysfunctional B3GLCT gene product, O-fucose-specific β-1,3-glucosyltransferase, is ineffective in providing a noncanonical quality control system for proper protein folding in cells.” Published November 2019; DOI: https://doi.org/10.3390/ijms20236006. (totonzuranska2019contributionofa pages 1-3)

Other documented pathogenic classes include splice-disrupting, nonsense, frameshift, and likely other loss-of-function alleles. Most disease-associated alleles are expected to impair transcript processing or truncate/inactivate the protein. Exact ACMG classifications and population frequencies should be retrieved variant-by-variant from current ClinVar and gnomAD releases before database loading; the retrieved papers did not provide reliable contemporary allele frequencies for every allele.

### Risk and protective factors

The major risk factor is having two carrier parents. For such a couple, each pregnancy has the standard autosomal-recessive probabilities: 25% affected, 50% carrier, and 25% unaffected/non-carrier. Consanguinity can increase the probability that both parents carry the same rare allele, but PPS occurs in non-consanguineous families as well.

No validated susceptibility loci, modifier genes, protective variants, environmental triggers, dietary or lifestyle risks, infectious causes, toxins, occupational exposures, or gene–environment interactions are established. Maternal age, paternal age, sex, smoking, alcohol, diet, and infection should not be represented as PPS causal factors without separate evidence. Because the initiating defect is germline and developmental, lifestyle modification cannot prevent disease in a genetically affected embryo.

## 3. Phenotypes

### Core phenotype and timing

PPS begins prenatally and is clinically congenital. The core constellation includes:

- **Peters anomaly/anterior-segment dysgenesis:** congenital corneal opacity with iridocorneal or corneolenticular adhesions; often bilateral and severe in syndromic disease. Suggested HPO: *Corneal opacity* (HP:0000659), *Anterior segment dysgenesis*, *Peters anomaly*, *Iridocorneal adhesion*.
- **Visual impairment:** caused by opacity, refractive error, cataract where present, sensory-deprivation amblyopia, and secondary glaucoma. Suggested HPO: *Visual impairment*, *Amblyopia*, *Cataract* (HP:0000519), *Glaucoma* (HP:0000501).
- **Disproportionate short stature/short limbs and brachydactyly:** congenital skeletal pattern with persistent growth restriction. Suggested HPO: *Short stature* (HP:0004322), *Brachydactyly* (HP:0001156), *Short limbs*.
- **Cleft lip with or without cleft palate:** congenital; feeding, speech, dental, hearing, and surgical consequences vary. Suggested HPO: *Cleft upper lip* (HP:0000204), *Cleft palate* (HP:0000175).
- **Characteristic craniofacial appearance:** variable facial dysmorphism, often including a prominent forehead, short/upslanting palpebral fissures, broad nasal bridge, and Cupid-bow upper lip in historical descriptions.
- **Developmental delay/intellectual disability:** variable from mild to severe; speech and motor development may both be affected. Suggested HPO: *Global developmental delay* (HP:0001263), *Intellectual disability* (HP:0001249).

Additional reported manifestations include microcephaly or structural CNS anomalies, seizures, hypotonia, hearing impairment, congenital external/middle-ear anomalies, congenital heart defects, vertebral abnormalities, genitourinary malformations, feeding problems, and dental/oral abnormalities. A syndrome-focused oral-health report estimated cardiac malformations in approximately **33%**, but this is based on a very small and ascertainment-biased literature and should be stored as a low-confidence qualitative frequency rather than a population estimate. (viga2018petersplussyndromeoral pages 2-4)

For broader Peters anomaly—not specifically molecularly confirmed PPS—glaucoma has been reported in **30–70%**. This range is clinically useful for surveillance but must not be loaded as a PPS-specific frequency. (delas2025novelgeneticvariants pages 2-3)

### Course and quality of life

Structural malformations are congenital and generally non-remitting. Their consequences are chronic and may evolve: amblyopia becomes less reversible as the visual-development window closes; glaucoma may arise later; short stature persists; developmental demands expose learning and adaptive limitations; cleft-associated feeding, speech, dental, and hearing issues change with age. Formal EQ-5D, SF-36, PROMIS, disease-specific quality-of-life, survival, and disability-weight studies were not found. Nevertheless, visual impairment, repeated anesthesia/surgery, communication difficulties, educational needs, and dependence in daily activities can substantially affect patients and caregivers. (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 3-6)

## 4. Genetic and molecular information

**B3GLCT** encodes beta-3-glucosyltransferase, also described as O-fucose-specific β1,3-glucosyltransferase. The disease alleles are germline; PPS is not a somatic or cancer-associated condition. Current evidence supports loss of function rather than gain of function, dominant-negative action, or haploinsufficiency. Heterozygous carriers are ordinarily unaffected.

The strongest directly documented variants in retrieved evidence are:

- **c.660+1G>A; rs80338851:** canonical donor-splice alteration, recurrent pathogenic PPS allele.
- **NM_194318.3:c.755delC, p.Thr252fs:** frameshift first reported in a compound-heterozygous newborn in 2019.
- Other splice, nonsense, and truncating alleles are reported across the literature, including a previously published novel nonsense allele referenced in later PA-spectrum work. (totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 14-15)

No reproducible modifier gene, disease-specific epigenetic signature, pathogenic methylation abnormality, anticipation, or large recurrent chromosomal rearrangement is established for classic PPS. A Peters-plus-like phenotype caused by other genes or copy-number changes should be classified separately rather than broadening B3GLCT-PPS indiscriminately. (delas2025novelgeneticvariants pages 2-3, delas2025novelgeneticvariants pages 13-14)

## 5. Environmental information

No environmental, lifestyle, occupational, toxic, radiological, nutritional, or infectious factor is known to cause classic PPS. Such factors may affect general pregnancy or surgical health but are not part of PPS etiology. No environmental protective intervention has been shown to reduce penetrance or severity in a fetus with biallelic pathogenic B3GLCT variants.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** biallelic B3GLCT loss-of-function variants reduce or abolish active ER-localized glucosyltransferase.
2. **Substrate recognition:** as TSR-containing secreted proteins fold in the ER, **POFUT2** recognizes properly folded TSRs and adds O-linked fucose to serine/threonine in the TSR consensus sequence.
3. **B3GLCT reaction:** B3GLCT adds glucose in β1-3 linkage to the O-fucose, forming **Glcβ1-3Fuc**.
4. **Quality-control failure:** without B3GLCT, O-fucosylated TSRs lack glucose extension. Folding, stabilization, ER exit, and secretion are impaired for a subset of TSR proteins.
5. **Developmental extracellular-matrix/signaling dysfunction:** affected proteins include members of thrombospondin and ADAMTS/ADAMTS-like families and other TSR-bearing proteins involved in extracellular matrix, morphogenesis, and tissue organization.
6. **Clinical manifestations:** disturbed anterior-eye, craniofacial, skeletal, neural, cardiac, and other organ development produces the congenital PPS phenotype.

Vasudevan et al. showed that B3GLCT is ER-localized and forms the Glcβ1-3Fuc disaccharide on TSRs. They identified 49 TSR-containing proteins, including TSP1/TSP2 and ADAMTS/ADAMTSL proteins. Patient serum showed complete loss of glucose from properdin TSRs, providing a human biochemical readout of functional null status. POFUT2 loss impaired secretion of all tested targets, whereas B3GLCT loss affected a subset, indicating overlapping but non-identical roles. Published February 2015; DOI: https://doi.org/10.1016/j.cub.2014.11.049. (vasudevan2015petersplussyndrome pages 1-3)

Suggested annotations include **GO:0005783 endoplasmic reticulum**, **GO:0006457 protein folding**, protein O-linked glycosylation, ER protein-quality control, protein secretion, extracellular-matrix organization, and embryonic morphogenesis. Relevant candidate cell types include neural crest cells, corneal endothelial/stromal cells, periocular mesenchyme, craniofacial mesenchyme, chondrocytes, and cardiogenic neural-crest derivatives. These cell-level links are biologically plausible but are less directly resolved than the biochemical pathway.

No disease-specific immune, inflammatory, ischemic, fibrotic, mitochondrial-energy, lipidomic, or metabolomic mechanism is established. No validated single-cell, spatial-transcriptomic, patient multi-omic, CRISPR-screen, or proteome-wide PPS signature was found.

## 7. Anatomical structures affected

The primary organ is the **eye**, especially cornea (UBERON:0000964), anterior chamber (UBERON:0001836), iris (UBERON:0001769), and lens (UBERON:0001773). Disease can be bilateral; unilateral disease is more typical of milder isolated PA1 than classic PPS. (delas2025novelgeneticvariants pages 2-3)

Systemic sites include palate (UBERON:0001703), lip and craniofacial skeleton, appendicular skeleton and digits, brain (UBERON:0000955), ear/auditory apparatus, teeth and periodontium, heart (UBERON:0000948), vertebral column, and genitourinary tract. At tissue level, affected compartments include ocular neural-crest-derived mesenchyme, corneal endothelium/stroma, connective tissue, cartilage, bone, and craniofacial tissues. At subcellular level, the central compartment is the **endoplasmic reticulum**, followed downstream by the secretory pathway and extracellular matrix. (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 2-3, vasudevan2015petersplussyndrome pages 1-3)

## 8. Temporal development

The molecular defect acts during embryogenesis. Eye, craniofacial, limb, and organ malformations are therefore congenital rather than acquired. Prenatal ultrasound may detect cleft lip/palate, short limbs, growth restriction, hydrocephalus, agenesis of the corpus callosum, or other severe malformations, but corneal/anterior-segment findings can be difficult to recognize prenatally.

The disorder is lifelong. There is no accepted staging system and no spontaneous remission. Structural lesions are usually stable, whereas complications—glaucoma, amblyopia, refractive error, developmental disability, feeding/speech difficulties, and dental disease—may emerge or worsen over time. Early infancy is a critical window for visual assessment and amblyopia prevention; infancy/childhood are also critical for feeding, cleft, hearing, cardiac, and developmental interventions. (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 3-6)

## 9. Inheritance and population

Inheritance is autosomal recessive with high expected penetrance for biallelic loss-of-function genotypes, although expressivity is variable. Anticipation is not expected. Germline mosaicism has not been established as a major mechanism but cannot be categorically excluded in counseling after an apparently de novo event.

A robust PPS-specific prevalence or annual incidence was not identified. The **2.2–3.1 per 100,000 births** figure reported in recent literature applies to the broader Peters anomaly spectrum, not PPS, and must not be relabeled as PPS prevalence. No validated sex bias, ethnic predilection, national hotspot, carrier frequency, or contemporary founder-effect estimate was found. (delas2025novelgeneticvariants pages 1-2)

## 10. Diagnostics

### Clinical evaluation

A newborn with congenital central corneal opacity plus short limbs/brachydactyly, cleft lip/palate, dysmorphism, developmental or CNS anomalies, and/or heart disease should prompt PPS evaluation. Ophthalmologic examination—often under anesthesia—should define corneal opacity, anterior-chamber depth, iris/corneal/lens adhesions, cataract, axial length, refraction, optic nerve status, retina where visible, and intraocular pressure. Systemic workup should include growth and skeletal assessment, echocardiography, hearing testing, feeding/cleft evaluation, neurologic/developmental assessment, and renal/genitourinary imaging when indicated. (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 3-6)

There is no routine blood chemistry, transferrin-isoelectric-focusing, urine-metabolite, biopsy, EEG, or imaging biomarker specific enough to confirm PPS. The loss of glucose on properdin TSRs is mechanistically informative but is not established as a broadly available clinical assay. (vasudevan2015petersplussyndrome pages 1-3)

### Genetic testing strategy

1. **First-line:** an anterior-segment dysgenesis/Peters anomaly panel including **B3GLCT**, or trio WES/WGS where systemic abnormalities make the differential broad.
2. Ensure coverage of coding exons and canonical splice sites and assess copy-number variation.
3. Confirm candidate variants and parental segregation by Sanger sequencing or equivalent validated methods.
4. If one allele is found, consider deletion/duplication analysis, genome sequencing, and RNA studies for cryptic splice variants.
5. CMA is useful when the phenotype is atypical or suggests a chromosomal Peters-plus-like condition; karyotype/FISH are not routine for classic PPS. Mitochondrial and repeat-expansion testing are not indicated unless another diagnosis is suspected.

In a 95-person Peters anomaly cohort, combined array, panel, exome, and genome approaches identified causes in approximately **one third**; **B3GLCT** was the most frequently implicated gene in syndromic PA, whereas two thirds remained without a molecular diagnosis. This is PA-spectrum diagnostic yield, not PPS test sensitivity. The abstract states: “Causative genetic defects involving 12 genes and CNVs were identified for 1/3 of patients.” Published February 2022; DOI: https://doi.org/10.1111/cge.14123. (chesneau2022firstevidenceof pages 14-17)

### Differential diagnosis

Important alternatives include isolated PA1/PA2; Peters-plus-like syndrome; Axenfeld–Rieger spectrum; aniridia; congenital hereditary endothelial dystrophy; sclerocornea; congenital glaucoma; congenital infections causing corneal/cataract abnormalities; and syndromes involving **PAX6, FOXC1, PITX2, PITX3, FOXE3, CYP1B1, SOX2, PXDN, COL4A1, CDH2, COL6A3, PEX2,** or **ZFHX4**. PA1 tends to be milder, often unilateral, and less systemically involved; PA2 includes corneolenticular adhesion/cataract and is commonly bilateral. PPLS is reserved for a PPS-like clinical phenotype without diagnostic B3GLCT variants. (delas2025novelgeneticvariants pages 2-3, delas2025novelgeneticvariants pages 13-14, chesneau2022firstevidenceof pages 14-17)

## 11. Outcome and prognosis

No reliable five- or ten-year survival, mortality rate, or life-expectancy estimate exists. Prognosis depends chiefly on severity of bilateral eye disease, glaucoma, CNS malformations, congenital heart disease, airway/feeding problems, and developmental impairment. Vision can range from useful residual sight to light perception or blindness. In PA-spectrum follow-up, proposed keratoplasty or keratoprosthesis may be deferred because of glaucoma and retinal-detachment risks; one complex patient retained light perception with normal pressure at age 13, illustrating possible long-term survival but not a population prognosis. (delas2025novelgeneticvariants pages 3-6)

Potential complications include deprivation amblyopia, secondary glaucoma, retinal detachment following complex surgery, graft failure, refractive error, feeding and aspiration difficulties, recurrent otitis/conductive hearing loss, speech impairment, dental disease, seizures, and cardiac morbidity. Recovery of congenital structural abnormalities is not expected, but early visual, surgical, hearing, communication, and developmental interventions may improve function. No validated prognostic molecular biomarker or genotype-based outcome calculator is available.

## 12. Treatment and real-world implementation

There is no approved B3GLCT replacement, substrate therapy, chaperone, gene therapy, genome editing, RNA therapy, cell therapy, immunotherapy, or other targeted treatment.

**Current management is multidisciplinary:**

- **Eyes:** immediate pediatric-ophthalmology assessment; refraction, occlusion/amblyopia therapy, low-vision support, and serial intraocular-pressure monitoring. Selected patients may undergo penetrating keratoplasty, lensectomy/cataract surgery, glaucoma procedures, or keratoprosthesis. Decisions are individualized because severe bilateral dysgenesis, glaucoma, graft failure, and retinal complications may limit benefit. Suggested NCIT concepts: Ophthalmic Examination (NCIT:C47891), supportive care, penetrating keratoplasty, cataract extraction, glaucoma surgery, and low-vision rehabilitation. (delas2025novelgeneticvariants pages 3-6)
- **Cleft/feeding:** feeding support, nutritional monitoring, cleft-lip/palate repair, speech therapy, and ENT/audiology care.
- **Development:** early-intervention services, physical therapy, occupational therapy, speech-language therapy, individualized education, and seizure management when needed.
- **Cardiac/hearing/renal:** lesion-specific cardiology, hearing aids or other auditory rehabilitation, and urologic/nephrologic care.
- **Dental:** preventive oral care is important because clefting, enamel/eruption abnormalities, cooperation limitations, cardiac disease, and anticonvulsant-associated gingival enlargement can complicate treatment. (viga2018petersplussyndromeoral pages 2-4)

No PPS-specific treatment-response rates, comparative surgical trials, pharmacogenomic recommendations, or registered interventional PPS clinical trials were found.

## 13. Prevention

Primary lifestyle prevention and immunization are not applicable. The principal preventive strategy is reproductive:

- molecular confirmation of the familial B3GLCT variants;
- carrier testing for adult relatives;
- genetic counseling regarding 25% recurrence risk when both parents are carriers;
- targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for monogenic disease;
- prenatal ultrasound for structural anomalies, recognizing limited sensitivity for ocular findings.

Secondary/tertiary prevention includes early neonatal recognition, prompt visual-axis and amblyopia management, glaucoma surveillance, echocardiography, hearing assessment, feeding support, and developmental intervention. Population newborn screening is not available or justified for this ultra-rare structural disorder.

## 14. Other species and natural disease

B3GLCT and the POFUT2–TSR glycosylation pathway are evolutionarily conserved, but no naturally occurring veterinary disease established as an orthologous PPS syndrome was identified. PPS is not infectious and has no zoonotic or cross-species transmission. Ortholog records should be obtained from NCBI Gene/Alliance for each target species before assigning numeric gene identifiers.

## 15. Model organisms and experimental systems

The most persuasive PPS mechanism comes from **human cell-biochemical systems and patient serum**, including enzyme localization, glycosylation assays, secretion assays, and properdin glycoform analysis. These models directly test the molecular lesion but do not reproduce the full ocular, craniofacial, skeletal, or neurodevelopmental phenotype. (vasudevan2015petersplussyndrome pages 1-3)

Drosophila and other systems have been used to study conserved glycosyltransferases and TSR O-fucosylation, and mouse studies of individual TSR-containing proteins such as ADAMTS family members illuminate extracellular-matrix development. However, the retrieved evidence did not establish a validated B3glct-null mouse, zebrafish, organoid, or iPSC model that faithfully recapitulates human PPS. Consequently, claims about model-organism phenotype rescue or preclinical therapeutic efficacy would be premature.

## Recent developments and expert interpretation

The 2022 study of 95 Peters anomaly patients demonstrated the practical value—and limitations—of combined CMA, panel, WES, and WGS, with a cause found in only one third and SOX2 newly implicated in PA. This supports broad genomic testing when a patient has an atypical or B3GLCT-negative PPS-like presentation. (chesneau2022firstevidenceof pages 14-17)

A 2023 systematic review of inherited carbohydrate-metabolism disorders included B3GLCT/B3GALTL-related PPS among glycosylation disorders with reported cardiac defects, reinforcing the need for cardiovascular screening but not establishing a new PPS-specific therapy. The main 2024 developments retrieved concerned neurocristopathy frameworks and childhood-glaucoma registry development rather than PPS-specific trials. The field’s principal unmet needs remain a longitudinal natural-history registry, standardized phenotype frequencies, patient-reported outcomes, validated disease models, a clinical glycosylation biomarker, and therapeutic strategies restoring TSR glycosylation or secretion.

The following table provides consolidated ontology and database-loading suggestions. Terms explicitly marked “requiring validation” should be checked against current ontology releases before ingestion.

| Domain | Finding | Suggested ontology identifiers/terms | Evidence/notes |
|---|---|---|---|
| Disease identity | Peters plus syndrome is a rare syndromic Peters anomaly / congenital disorder of glycosylation caused by biallelic B3GLCT variants | MONDO:0009856; suggested term: autosomal recessive congenital disorder of glycosylation; suggested term: syndromic anterior segment dysgenesis | Open Targets links Peters plus syndrome specifically to **B3GLCT**; literature distinguishes PPS from isolated Peters anomaly and Peters-plus-like syndrome (OpenTargets Search: Peters plus syndrome, totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 2-3) |
| Synonyms / nomenclature | Historical/alternative gene name overlap may appear in records | suggested terms requiring validation: Peters'-plus syndrome; Peters plus; B3GALTL-related Peters plus syndrome; B3GLCT-related Peters plus syndrome | Sources note former gene symbol **B3GALTL** and current **B3GLCT**; curation should normalize both (totonzuranska2019contributionofa pages 1-3, vasudevan2015petersplussyndrome pages 1-3) |
| Etiology | Primary cause is germline biallelic loss of function in **B3GLCT** | suggested term: germline autosomal recessive inheritance; HGNC gene symbol: B3GLCT | Human genetic evidence is strong and disease-level, not EHR-derived; recurrent splice and truncating variants reported (OpenTargets Search: Peters plus syndrome, totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 14-15) |
| Key variant class | Recurrent canonical splice variant and other truncating alleles are important pathogenic classes | suggested variant terms: c.660+1G>A (rs80338851); c.755delC (p.Thr252fs) requiring nomenclature validation | c.660+1G>A is repeatedly cited as previously known PPS allele; 2019 report adds novel frameshift c.755delC (totonzuranska2019contributionofa pages 1-3) |
| Core ocular phenotype | Peters anomaly / anterior segment dysgenesis with congenital corneal opacity | HP:0000659 Corneal opacity; suggested HPO term requiring validation: Peters anomaly; suggested HPO term: Anterior segment dysgenesis | Core defining feature of PPS; congenital onset (totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 2-3) |
| Ocular adhesion phenotype | Iridocorneal and/or lenticulocorneal adhesions may accompany corneal opacity | suggested HPO terms requiring ontology validation: iridocorneal adhesions; corneolenticular adhesions | Well-described within Peters anomaly spectrum; use as phenotype mapping after validation (delas2025novelgeneticvariants pages 2-3, chesneau2022firstevidenceof pages 14-17) |
| Ocular lens phenotype | Congenital cataract can occur within Peters anomaly spectrum and PPS differential workup | HP:0000519 Cataract | Cataract is especially relevant in PA2 and syndromic differential diagnosis; not every PPS case has cataract (delas2025novelgeneticvariants pages 2-3, ahmad2022geneticsofcongenital pages 1-6) |
| Ocular complication | Secondary glaucoma is a major vision-threatening complication | HP:0000501 Glaucoma | PA-spectrum review cited glaucoma in 30-70% of PA patients; this should not be over-interpreted as PPS-specific frequency (delas2025novelgeneticvariants pages 2-3) |
| Craniofacial phenotype | Cleft lip with/without cleft palate and characteristic facial dysmorphism | HP:0000204 Cleft upper lip; HP:0000175 Cleft palate | Clinical diagnosis commonly includes cleft lip/palate and facial changes (viga2018petersplussyndromeoral pages 2-4, vasudevan2015petersplussyndrome pages 1-3) |
| Growth / skeletal phenotype | Short stature, short limbs, brachydactyly are characteristic systemic findings | HP:0004322 Short stature; HP:0001156 Brachydactyly; suggested HPO term: rhizomelia/short limbs requiring validation | PPS is distinguished from isolated PA by systemic skeletal/growth findings (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 2-3, vasudevan2015petersplussyndrome pages 1-3) |
| Neurodevelopmental phenotype | Developmental delay / intellectual disability of variable severity | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Often described as variable psychomotor delay/mental retardation in older literature; harmonize to current HPO usage (viga2018petersplussyndromeoral pages 2-4) |
| Auditory phenotype | Hearing loss can occur, sometimes linked to congenital ear malformations | HP:0000365 Hearing impairment | Conductive hearing loss noted in syndrome descriptions and case reports (viga2018petersplussyndromeoral pages 2-4) |
| Cardiac phenotype | Congenital heart defects are variably reported | HP:0001627 Abnormality of the cardiovascular system morphology; suggested HPO term: congenital heart defect requiring validation | One review-oriented source states cardiac malformations in ~33% of reported cases, but this estimate derives from small literature and should be treated cautiously (viga2018petersplussyndromeoral pages 2-4) |
| Additional organ involvement | Brain/CNS, urogenital, and other multisystem anomalies may occur in severe cases | suggested HPO terms requiring validation: hydrocephalus; agenesis of corpus callosum; urogenital abnormality | Prenatal and case literature suggest broader malformation spectrum; evidence is case-based and variable (delas2025novelgeneticvariants pages 14-15) |
| Molecular mechanism | B3GLCT is an ER-localized beta-1,3-glucosyltransferase that adds glucose to O-fucosylated TSRs, producing Glcβ1-3Fuc | GO:0005783 endoplasmic reticulum; suggested GO term: protein O-linked glycosylation; suggested GO term: O-fucose glycan extension on thrombospondin type-1 repeat | Vasudevan et al. provide direct mechanistic evidence for ER localization and TSR disaccharide formation (vasudevan2015petersplussyndrome pages 1-3) |
| Upstream partner | POFUT2 adds the initial O-fucose to properly folded TSRs upstream of B3GLCT | suggested term requiring validation: POFUT2-mediated protein O-fucosylation of TSR domains | PPS mechanism is part of a two-step POFUT2→B3GLCT pathway (vasudevan2015petersplussyndrome pages 1-3) |
| Protein homeostasis mechanism | PPS mutations disrupt a noncanonical ER quality-control system for properly folded TSR-containing proteins | GO:0006457 protein folding; suggested GO term: endoplasmic reticulum protein quality control; suggested GO term: regulation of protein secretion | Mechanistic hallmark from Current Biology 2015; downstream effect is impaired folding/ER exit/secretion for susceptible TSR proteins (totonzuranska2019contributionofa pages 1-3, vasudevan2015petersplussyndrome pages 1-3) |
| Candidate affected protein classes | TSR-containing extracellular proteins are likely downstream effectors | suggested terms requiring validation: thrombospondin-1; thrombospondin-2; ADAMTS family; ADAMTSL family; properdin | Human/cell biochemical evidence supports defective glycosylation of TSR-bearing proteins; exact causal contributors to each PPS feature remain incompletely mapped (vasudevan2015petersplussyndrome pages 1-3) |
| Cell types | Relevant developmental cell populations likely include corneal endothelium, neural crest derivatives, and chondrocytes | CL:0000114 endothelial cell; suggested CL term: corneal endothelial cell; CL:0000000 cell? / suggested CL term: neural crest cell; CL:0000138 chondrocyte | Numeric CL IDs should be validated before loading except for generic chondrocyte/endothelial mappings; literature supports neural crest and connective/skeletal involvement conceptually (delas2025novelgeneticvariants pages 2-3) |
| Anatomical structures | Primary affected sites include cornea, anterior chamber, iris, lens, palate, limb skeleton, brain, and heart | UBERON:0000964 cornea; UBERON:0001769 iris; UBERON:0001773 lens; UBERON:0001836 anterior chamber of eyeball; UBERON:0001703 palate; UBERON:0000922 embryo? / suggested term: limb skeleton; UBERON:0000955 brain; UBERON:0000948 heart | Use validated UBERON mappings for local database ingestion; eye and multisystem anatomy are well supported clinically (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 2-3, vasudevan2015petersplussyndrome pages 1-3) |
| Inheritance / population | Inheritance is autosomal recessive; robust PPS-specific prevalence/incidence not found | suggested term: autosomal recessive inheritance | Do not substitute Peters anomaly prevalence (2.2-3.1 per 100,000 births) for PPS prevalence; PPS remains ultra-rare (totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 1-2) |
| Diagnostics | Diagnostic workflow combines ophthalmic exam with molecular confirmation of biallelic B3GLCT variants | NCIT:C47891 Ophthalmic Examination; NCIT:C84351 Whole Exome Sequencing; suggested NCIT term: gene panel testing; suggested NCIT term: Sanger sequencing confirmation | WES/WGS/panel testing are standard modern approaches in PA-spectrum diagnosis; PPS confirmation is genotype-driven (totonzuranska2019contributionofa pages 1-3, delas2025novelgeneticvariants pages 2-3, chesneau2022firstevidenceof pages 14-17) |
| Differential diagnosis | Distinguish from isolated Peters anomaly and Peters-plus-like syndrome; other PA genes are relevant | suggested disease/gene terms: PAX6, PITX2, PITX3, FOXE3, FOXC1, CYP1B1, SOX2, PXDN, COL4A1, CDH2, PEX2, ZFHX4 | PPLS denotes PPS-like phenotype without B3GLCT variants; isolated/syndromic PA is genetically heterogeneous (delas2025novelgeneticvariants pages 2-3, delas2025novelgeneticvariants pages 13-14, chesneau2022firstevidenceof pages 14-17) |
| Treatment / management | Care is supportive and multidisciplinary; ocular monitoring, amblyopia prevention, glaucoma surveillance, selective surgery, cleft and hearing management | NCIT:C157740 Supportive Care; suggested NCIT terms: penetrating keratoplasty; Boston keratoprosthesis implantation; cleft palate repair; hearing aid therapy; physical therapy; dental care | No disease-modifying therapy found; management is phenotype-directed and risk-benefit sensitive (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 3-6) |
| Prevention | Main preventive options are genetic counseling, reproductive testing, and prenatal/preimplantation diagnosis in at-risk families | NCIT:C15240 Genetic Counseling; suggested NCIT terms: prenatal molecular diagnosis; carrier screening; preimplantation genetic testing | Prevention is familial/reproductive rather than environmental; parental exome sequencing has been used to establish recurrence risk in lethal/prenatal AR disease settings including B3GLCT diagnoses (viga2018petersplussyndromeoral pages 2-4, delas2025novelgeneticvariants pages 14-15) |
| Research / recent developments | Recent work mainly refines PA-spectrum genetics rather than PPS-specific therapy | suggested terms: comprehensive genomic analysis; rare disease registry; molecular diagnosis | 2022-2024 literature highlights expanded PA genes, WES/WGS use, and childhood glaucoma registry context; no PPS interventional trials identified (delas2025novelgeneticvariants pages 3-6, chesneau2022firstevidenceof pages 14-17) |
| Evidence gaps | No validated environmental or infectious cause, protective factor, biomarker panel, targeted therapy, pharmacogenomic rule, omics diagnostic signature, or natural animal disease established | suggested terms: evidence gap; no data | Also no robust PPS-specific survival statistics, QoL instruments, or confirmed whole-animal PPS model were found in retrieved evidence; clinical trial search found no relevant interventional PPS trial (vasudevan2015petersplussyndrome pages 1-3, ahmad2022geneticsofcongenital pages 1-6, delas2025novelgeneticvariants pages 13-14) |


*Table: This table summarizes database-ready disease findings, ontology mappings, and evidence notes for Peters plus syndrome. It emphasizes confirmed identifiers and mechanisms while flagging terms and evidence gaps that require ontology or literature validation.*

## Evidence limitations

PPS literature consists mainly of small series, case reports, and one strong mechanistic program; therefore, many apparent frequencies are vulnerable to ascertainment and publication bias. The PA-spectrum prevalence and glaucoma statistics cannot be treated as molecularly confirmed PPS statistics. No robust data were found for PPS-specific incidence, carrier frequency, sex ratio, survival, formal quality of life, penetrance stratified by variant, environmental interactions, protective alleles, multi-omics signatures, natural animal disease, or treatment efficacy. Direct quotations are limited to text available from retrieved abstracts; quotations should not be inferred from secondary summaries.

References

1. (OpenTargets Search: Peters plus syndrome): Open Targets Query (Peters plus syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (totonzuranska2019contributionofa pages 1-3): Justyna Totoń-Żurańska, Przemysław Kapusta, Magda Rybak-Krzyszkowska, Katarzyna Lorenc, Julita Machlowska, Anna Skalniak, Erita Filipek, Dorota Pawlik, and Paweł P. Wołkow. Contribution of a novel b3glct variant to peters plus syndrome discovered by a combination of next-generation sequencing and automated text mining. International Journal of Molecular Sciences, 20:6006, Nov 2019. URL: https://doi.org/10.3390/ijms20236006, doi:10.3390/ijms20236006. This article has 4 citations.

3. (delas2025novelgeneticvariants pages 2-3): Flora Delas, Samuel Koller, Jordi Maggi, Alessandro Maspoli, Lisa Kurmann, Elena Lang, Wolfgang Berger, and Christina Gerth-Kahlert. Novel genetic variants and clinical profiles in peters anomaly spectrum disorders. International Journal of Molecular Sciences, 26:6454, Jul 2025. URL: https://doi.org/10.3390/ijms26136454, doi:10.3390/ijms26136454. This article has 3 citations.

4. (vasudevan2015petersplussyndrome pages 1-3): Deepika Vasudevan, Hideyuki Takeuchi, Sumreet Singh Johar, Elaine Majerus, and Robert S. Haltiwanger. Peters plus syndrome mutations disrupt a noncanonical er quality-control mechanism. Current Biology, 25:286-295, Feb 2015. URL: https://doi.org/10.1016/j.cub.2014.11.049, doi:10.1016/j.cub.2014.11.049. This article has 105 citations and is from a highest quality peer-reviewed journal.

5. (viga2018petersplussyndromeoral pages 2-4): Maíra Viga, Emílio Sponchiado Júnior, Pollyanna Medina, Ary Filho, and Simone Hanan. Peters-plus syndrome: oral health approach. Revista Portuguesa de Estomatologia, Medicina Dentária e Cirurgia Maxilofacial, Dec 2018. URL: https://doi.org/10.24873/j.rpemd.2018.11.422, doi:10.24873/j.rpemd.2018.11.422. This article has 1 citations.

6. (delas2025novelgeneticvariants pages 3-6): Flora Delas, Samuel Koller, Jordi Maggi, Alessandro Maspoli, Lisa Kurmann, Elena Lang, Wolfgang Berger, and Christina Gerth-Kahlert. Novel genetic variants and clinical profiles in peters anomaly spectrum disorders. International Journal of Molecular Sciences, 26:6454, Jul 2025. URL: https://doi.org/10.3390/ijms26136454, doi:10.3390/ijms26136454. This article has 3 citations.

7. (delas2025novelgeneticvariants pages 14-15): Flora Delas, Samuel Koller, Jordi Maggi, Alessandro Maspoli, Lisa Kurmann, Elena Lang, Wolfgang Berger, and Christina Gerth-Kahlert. Novel genetic variants and clinical profiles in peters anomaly spectrum disorders. International Journal of Molecular Sciences, 26:6454, Jul 2025. URL: https://doi.org/10.3390/ijms26136454, doi:10.3390/ijms26136454. This article has 3 citations.

8. (delas2025novelgeneticvariants pages 13-14): Flora Delas, Samuel Koller, Jordi Maggi, Alessandro Maspoli, Lisa Kurmann, Elena Lang, Wolfgang Berger, and Christina Gerth-Kahlert. Novel genetic variants and clinical profiles in peters anomaly spectrum disorders. International Journal of Molecular Sciences, 26:6454, Jul 2025. URL: https://doi.org/10.3390/ijms26136454, doi:10.3390/ijms26136454. This article has 3 citations.

9. (delas2025novelgeneticvariants pages 1-2): Flora Delas, Samuel Koller, Jordi Maggi, Alessandro Maspoli, Lisa Kurmann, Elena Lang, Wolfgang Berger, and Christina Gerth-Kahlert. Novel genetic variants and clinical profiles in peters anomaly spectrum disorders. International Journal of Molecular Sciences, 26:6454, Jul 2025. URL: https://doi.org/10.3390/ijms26136454, doi:10.3390/ijms26136454. This article has 3 citations.

10. (chesneau2022firstevidenceof pages 14-17): Bertrand Chesneau, Marion Aubert‐Mucca, Félix Fremont, Jacmine Pechmeja, Vincent Soler, Bertrand Isidor, Mathilde Nizon, Hélène Dollfus, Josseline Kaplan, Lucas Fares‐Taie, Jean‐Michel Rozet, Tiffany Busa, Didier Lacombe, Sophie Naudion, Jeanne Amiel, Marlène Rio, Tania Attie‐Bitach, Cécile Lesage, Dominique Thouvenin, Sylvie Odent, Godelieve Morel, Catherine Vincent‐Delorme, Odile Boute, Clémence Vanlerberghe, Anne Dieux, Simon Boussion, Laurence Faivre, Lucile Pinson, Fanny Laffargue, Gwenaël Le Guyader, Guylène Le Meur, Fabienne Prieur, Victor Lambert, Beatrice Laudier, Edouard Cottereau, Carmen Ayuso, Marta Corton‐Pérez, Laurence Bouneau, Cédric Le Caignec, Véronique Gaston, Claire Jeanton‐Scaramouche, Delphine Dupin‐Deguine, Patrick Calvas, Nicolas Chassaing, and Julie Plaisancié. First evidence of <scp><i>sox2</i></scp> mutations in peters' anomaly: lessons from molecular screening of 95 patients. Clinical Genetics, 101:494-506, Feb 2022. URL: https://doi.org/10.1111/cge.14123, doi:10.1111/cge.14123. This article has 29 citations and is from a peer-reviewed journal.

11. (ahmad2022geneticsofcongenital pages 1-6): Reddin Ahmad, Suzannah Bell, and Mariya Moosajee. Genetics of congenital cataract. Aug 2022. URL: https://doi.org/10.1016/j.yaoo.2022.03.004, doi:10.1016/j.yaoo.2022.03.004. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Peters_Plus_Syndrome-deep-research-falcon_artifacts/artifact-00.md)