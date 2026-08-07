---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-05T18:18:13.552591'
end_time: '2026-08-05T18:26:07.121148'
duration_seconds: 473.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemiconvulsion-Hemiplegia-Epilepsy Syndrome
  mondo_id: ''
  category: Acquired
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hemiconvulsion-Hemiplegia-Epilepsy_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemiconvulsion-Hemiplegia-Epilepsy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Hemiconvulsion-Hemiplegia-Epilepsy Syndrome** covering all of the
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
- **Disease Name:** Hemiconvulsion-Hemiplegia-Epilepsy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Acquired

## Research Objectives

Please provide a comprehensive research report on **Hemiconvulsion-Hemiplegia-Epilepsy Syndrome** covering all of the
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


# Hemiconvulsion–Hemiplegia–Epilepsy Syndrome: Disease-Characteristics Report

## Executive summary

Hemiconvulsion–hemiplegia–epilepsy (HHE) syndrome is a **rare, acquired, predominantly pediatric destructive encephalopathy/epilepsy syndrome**. Its defining sequence is: **(1) prolonged unilateral clonic status epilepticus, usually during fever; (2) immediate or early persistent contralateral hemiplegia; and (3) delayed focal epilepsy**, often accompanied by unilateral cerebral atrophy. The evidence base remains limited mainly to retrospective cohorts, imaging series, surgical series, and case reports; there are no disease-specific randomized trials, validated molecular biomarkers, or robust population incidence estimates.

Open Targets recognizes the related entity **“idiopathic hemiconvulsion-hemiplegia syndrome,” MONDO:0019485**, but lists **zero associated targets**, consistent with the syndrome not having an established single molecular cause. The exact ontology boundary between hemiconvulsion–hemiplegia syndrome and full HHE syndrome should be checked in each resource before automated cross-mapping. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome)

| Domain | Established finding | Evidence type / key study and year | Ontology suggestions | Confidence or gap |
|---|---|---|---|---|
| Disease definition | Hemiconvulsion-Hemiplegia-Epilepsy (HHE) syndrome is an acquired pediatric epilepsy-related syndrome characterized by a stereotyped sequence: prolonged unilateral convulsive status, followed by persistent hemiplegia, then later focal epilepsy; Open Targets lists a related entity as “idiopathic hemiconvulsion-hemiplegia syndrome.” (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | Disease knowledgebase context: Open Targets disease entry; classic syndrome literature exists but was not available in current tool context (2024 Open Targets context) (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | MONDO: related entity present but exact HHE mapping uncertain; NCIT: epilepsy syndrome term uncertain; HPO: Hemiconvulsion/Hemiplegia/Epilepsy terms applicable, exact IDs not verified | Moderate confidence for broad definition; exact ontology crosswalk for classic HHE remains uncertain in available context |
| Classification / origin | The syndrome is best treated as acquired rather than monogenic, because the defining event is an acute destructive hemispheric injury associated with status epilepticus and subsequent cerebral hemiatrophy. | Human clinical syndrome literature cited by search results (Auvin 2012 review; Gastaut 1959; case series), but full text not available in current context | MONDO/Orphanet mapping uncertain; HPO suggestion: acquired cerebral hemiatrophy, hemiparesis, focal seizures | Moderate confidence; primary evidence not fully extracted in tool context |
| Acute trigger sequence | Typical presentation is prolonged febrile hemiclonic status epilepticus in infancy/early childhood, often after a febrile illness, preceding unilateral brain injury. | Human clinical reviews/case series identified by search: Tenney 2012; Auvin 2012; South African series 2012; exact extracted text unavailable | HPO: Febrile seizure term, Status epilepticus term, Clonic seizure term, Focal motor seizure term | Moderate confidence; exact percentages and onset distributions are a current data gap |
| Core neurologic deficit | Persistent contralateral hemiplegia/hemiparesis follows the acute hemiconvulsive episode and is a defining phenotype. | Human clinical syndrome literature identified in searches; not directly extracted | HPO: Hemiparesis; Hemiplegia; Motor developmental impairment if chronic | High confidence for phenotype, low confidence for frequency estimates |
| Epilepsy evolution | Delayed epilepsy commonly emerges after the acute hemiplegic phase, usually as chronic focal drug-resistant epilepsy in a subset of survivors. | Human longitudinal/surgical literature identified by search, including Kim et al. 2008 on delayed epilepsy surgery | HPO: Focal-onset seizure; Drug-resistant epilepsy; Developmental regression/cognitive impairment if present | Moderate confidence; exact latency and response rates not available in current context |
| Neuroimaging | Characteristic imaging pattern: acute unilateral hemispheric edema/swelling with diffusion restriction, followed over time by hemispheric atrophy/hemiatrophy and gliosis. | Human MRI/pathology studies identified in searches: Freeman 2002; Toldo 2007; Auvin 2007; Barcia 2013; exact text not extracted | UBERON: cerebral hemisphere; HPO: Cerebral hemiatrophy, Cerebral edema, Abnormal brain MRI; GO CC not specifically applicable | High confidence for qualitative MRI sequence; numerical timing details remain a gap |
| Electrophysiology | EEG is used to document focal hemispheric seizure activity acutely and later focal epileptiform abnormalities, but no syndrome-specific EEG biomarker is established. | Human clinical literature and epilepsy reviews; no dedicated biomarker evidence retrieved | HPO: Abnormal EEG; Focal epileptiform discharges (exact term ID unverified) | Moderate confidence; syndrome-specific EEG signatures are not well standardized |
| Pathology / mechanism | Available pathology literature supports inflammatory-degenerative hemispheric injury after prolonged seizures, with mechanistic hypotheses centered on excitotoxicity, cytotoxic edema, blood-brain barrier dysfunction, and secondary inflammation rather than a single causal gene. | Human pathology case reports/reviews identified by search (Auvin 2007; Serino 2014) plus general mechanistic support from seizure/brain-injury literature found in context | GO: excitatory neurotransmission, neuroinflammatory response, cell death, response to hypoxia; CL: cortical neuron, astrocyte, microglial cell | Moderate confidence; direct HHE molecular studies are sparse |
| Genetics | SCN1A variants have been reported only in a minority of HHE cases; the available literature supports “low incidence” and argues HHE is not a typical monogenic SCN1A disorder. | Human genetics study identified by search: Kim et al. 2013, “Low incidence of SCN1A genetic mutation in patients with hemiconvulsion–hemiplegia–epilepsy syndrome” | HGNC: SCN1A; HPO: Seizures precipitated by fever may overlap with Dravet-spectrum phenotypes | Moderate-to-high confidence for “not monogenic/low incidence”; exact mutation counts not available in current context |
| Differential diagnosis | Important differentials include Dravet syndrome/GEFS+ spectrum, FIRES/NORSE, Rasmussen encephalitis, stroke, alternating hemiplegia, encephalitis/encephalopathy, and structural or metabolic disorders causing unilateral edema and subsequent atrophy. | Human review literature identified by search; current tool context does not provide extracted differential tables | HPO overlap terms: hemiplegia, focal seizures, fever-associated seizures; MONDO terms uncertain | Moderate confidence; evidence synthesis limited by unavailable full texts |
| Management | Acute management is supportive neurocritical care plus standard status epilepticus treatment; chronic management includes antiseizure medications, rehabilitation, and evaluation for epilepsy surgery in medically refractory cases. | Human clinical reviews/case reports identified by search; no dedicated interventional trials retrieved | NCIT suggestions: anticonvulsant therapy, physical therapy, occupational therapy, epilepsy surgery/hemispherectomy (exact NCIT IDs unverified) | High confidence for real-world practice pattern; low confidence for comparative efficacy data |
| Surgical treatment | In selected patients with delayed refractory epilepsy and a functionally devastated hemisphere, hemispherectomy/hemispherotomy has been reported as a real-world treatment option with seizure benefit in case series. | Human surgical series identified by search: Kim et al. 2008; later hemispherectomy experience papers also identified | NCIT: Hemispherectomy / Hemispherotomy term uncertain; HPO: post-surgical seizure reduction not an HPO phenotype | Moderate confidence; no randomized evidence |
| Epidemiology | HHE is rare; the literature consists mainly of case reports, small series, and retrospective cohorts, with no robust population incidence estimate retrieved in current context. | Search results include small retrospective series (e.g., 35 cases, 10 cases, regional case series), but no population registry evidence extracted | MONDO/Orphanet prevalence term uncertain | High confidence that disease is rare; major quantitative epidemiology gap |
| Recent developments (2023-2024) | Recent searchable material is dominated by isolated case reports and broader epilepsy classification updates; no major 2023-2024 breakthrough mechanistic, genomic, or therapeutic trial program was retrieved. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | Search evidence and Open Targets show no disease-target associations in the retrieved context. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | Open Targets disease-target links absent; omics ontology suggestions not applicable | High confidence for evidence sparsity |
| Trials / translational research | No dedicated interventional clinical trials were retrieved for HHE; no disease-specific target program or drug-development signal was found in Open Targets. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | ClinicalTrials search: no relevant dedicated trial retrieved; Open Targets associatedTargets count = 0. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | NCIT: clinical trial not disease-specific; Open Targets disease-target association absent | High confidence for lack of dedicated trial/target evidence |
| Omics / biomarkers | No HHE-specific transcriptomic, proteomic, metabolomic, spatial, or single-cell studies were retrieved; no validated circulating biomarker or molecular diagnostic signature was identified. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | Evidence gap from tool searches and Open Targets context. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) | GO/CL/omics terms not disease-specific; biomarker ontology mapping unavailable | High confidence that this is a major knowledge gap |


*Table: This table summarizes the most actionable disease-knowledge findings for Hemiconvulsion-Hemiplegia-Epilepsy syndrome and explicitly marks where evidence is based on classic clinical literature versus current gaps. It is useful for rapid knowledge-base curation because it links core syndrome features to ontology suggestions and highlights missing trials, targets, and omics data.*

---

## 1. Disease information

### Definition and classification

HHE is an acquired sequence rather than a conventional inherited epilepsy syndrome. The initial “hemiconvulsion” is prolonged focal motor—usually hemiclonic—status epilepticus. It produces or accompanies acute unilateral hemispheric injury, after which the child has contralateral hemiplegia or severe hemiparesis. Chronic focal epilepsy may emerge after a latent interval.

The term **hemiconvulsion–hemiplegia (HH) syndrome** is appropriately used before recurrent unprovoked epilepsy appears; **HHE syndrome** denotes completion of the three-stage sequence. “Idiopathic” historically indicated absence of a demonstrable antecedent structural lesion, infection, or metabolic disorder, not proof of a primary genetic disease.

### Identifiers and synonyms

| Resource | Suggested entry or status |
|---|---|
| MONDO | **MONDO:0019485**, “idiopathic hemiconvulsion-hemiplegia syndrome”; verify whether the intended record includes the delayed-epilepsy stage (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) |
| Orphanet | Search under *hemiconvulsion-hemiplegia-epilepsy syndrome* and *idiopathic hemiconvulsion-hemiplegia syndrome*; an ORPHA number could not be reliably verified from the retrieved evidence |
| OMIM | No well-established standalone Mendelian HHE phenotype was verified |
| ICD-10 | No specific HHE code; code constituent diagnoses, such as status epilepticus, focal epilepsy, and hemiplegia, according to local coding rules |
| ICD-11 | No disease-specific code verified; use the relevant epilepsy/status and acquired motor-deficit categories |
| MeSH | No dedicated MeSH descriptor verified; use *Epilepsy*, *Status Epilepticus*, *Hemiplegia*, *Seizures, Febrile*, and *Brain Atrophy* |

**Synonyms:** HHE syndrome; hemiconvulsion–hemiplegia–epilepsy syndrome; hemiconvulsion–hemiplegia syndrome; HH syndrome; idiopathic hemiconvulsion–hemiplegia syndrome; infantile hemiconvulsion–hemiplegia and epilepsy syndrome; historically, hemiplegia–hemiconvulsion–epilepsy syndrome.

### Data provenance

The description is derived from **aggregated disease-level literature**, including small retrospective cohorts and imaging series—not from a single patient’s EHR. Major sources include the classic description by Gastaut et al. (1959), the review by Auvin et al. (published September 2012; [DOI](https://doi.org/10.1016/j.ejpn.2012.01.007)), and the 35-patient clinical/imaging/EEG series by Albakaye et al. (published March 2018; [DOI](https://doi.org/10.1016/j.yebeh.2017.12.018)).

---

## 2. Etiology

### Primary causal factors

The proximate trigger is generally **prolonged unilateral status epilepticus in the immature brain**, frequently associated with fever or an acute infection. HHE can also occur in association with pre-existing structural, metabolic, inflammatory, or genetic neurologic disease; such cases are better described as secondary HHE phenotypes.

Reported associations include CNS or systemic infection, congenital adrenal hyperplasia, L-2-hydroxyglutaric aciduria, tuberous sclerosis complex, 1q44 deletion, leukodystrophy, and Dravet syndrome. These heterogeneous associations support HHE as a **final common clinicoradiologic pathway**, not a unitary etiologic disease.

### Risk factors

* **Age:** infancy and early childhood, when fever-provoked seizures and the immature brain’s susceptibility to excitotoxic edema are greatest.
* **Seizure duration and refractoriness:** prolonged focal motor status is the most consistent modifiable risk factor.
* **Hyperthermia/fever:** likely lowers seizure threshold and may amplify seizure-mediated metabolic injury. Experimental work shows that hyperthermia aggravates epileptic brain injury, whereas hypothermia reduces it; this is supportive animal evidence, not HHE-specific clinical proof ([Lundgren et al., DOI](https://doi.org/10.1007/BF00241411)).
* **Underlying neurologic disease:** structural lesions, metabolic disorders, encephalitis/encephalopathy, or developmental and epileptic encephalopathies can predispose to the same sequence.
* **SCN1A:** variants occur in a minority of reported HHE patients and can indicate a Dravet-spectrum phenotype rather than primary HHE. Kim et al. explicitly reported a “low incidence of SCN1A genetic mutation” (published October 2013; [DOI](https://doi.org/10.1016/j.eplepsyres.2013.06.012)).

No reproducible sex, ancestry, lifestyle, toxin, occupational, smoking, alcohol, or dietary risk factor has been established.

### Protective factors

No validated protective allele, diet, supplement, or long-term prophylactic drug has been demonstrated. The most biologically plausible protection is **rapid termination of prolonged seizures**, maintenance of oxygenation, perfusion, glucose, electrolytes, and normothermia, and prompt treatment of infection. These are standards of status-epilepticus care rather than HHE-specific trial results.

### Gene–environment interaction

A reasonable model is that genetic seizure susceptibility—particularly an SCN1A-related fever-sensitive epilepsy or another developmental epilepsy—interacts with fever and prolonged status to cross a threshold for unilateral excitotoxic injury. This remains a susceptibility model; there is no validated polygenic score, modifier locus, or quantified interaction effect.

---

## 3. Phenotypes

| Phenotype | Type, onset, course, severity | Suggested HPO term |
|---|---|---|
| Prolonged unilateral clonic seizure/status | Acute in infancy/early childhood; severe and often fever-associated; defining initial event | Focal motor seizure **HP:0011153**; Status epilepticus **HP:0002133**; Febrile seizures **HP:0002373** |
| Hemiplegia/hemiparesis | Appears during or immediately after status; contralateral to injured hemisphere; persistent, sometimes improving from plegia to paresis | Hemiplegia **HP:0002301**; Hemiparesis **HP:0001269** |
| Delayed focal epilepsy | Develops after a variable latent period; chronic; may be drug resistant | Focal seizures **HP:0007359**; Refractory epilepsy **HP:0002345** |
| Acute unilateral cerebral edema and restricted diffusion | Early MRI sign; severe and evolving | Cerebral edema **HP:0002181**; Abnormal brain MRI **HP:0410263** |
| Cerebral hemiatrophy/gliosis | Chronic consequence, unilateral and usually ipsilateral to the original seizures | Cerebral atrophy **HP:0002059**; Cerebral cortical atrophy **HP:0002120** |
| Intellectual/developmental impairment | Variable; reflects age, lesion extent, status severity, recurrent epilepsy, and underlying cause | Global developmental delay **HP:0001263**; Intellectual disability **HP:0001249** |
| Language impairment | Common when the dominant hemisphere is injured or epilepsy remains active | Delayed speech and language development **HP:0000750** |
| Unilateral spasticity, contracture, gait impairment | Chronic corticospinal consequence | Spasticity **HP:0001257**; Abnormal gait **HP:0001288** |
| Visual-field deficit | Possible with posterior hemispheric injury | Homonymous hemianopia **HP:0002159** |

Reliable phenotype percentages cannot be generalized: by definition, hemiconvulsion and hemiplegia are near-obligate, whereas delayed epilepsy, cognitive impairment, language deficit, and drug resistance vary substantially among small and selected cohorts.

### Quality of life

Persistent unilateral weakness affects ambulation, bimanual activity, dressing, feeding, school participation, and independence. Chronic epilepsy adds medication burden, injury risk, supervision requirements, and psychosocial stress. Cognitive and language impairment may dominate educational outcome. No HHE-specific EQ-5D, PROMIS, SF-36, or validated disease-specific quality-of-life study was identified.

---

## 4. Genetic and molecular information

HHE has **no established defining causal gene, inheritance pattern, penetrance estimate, carrier frequency, founder variant, or recurrent pathogenic chromosomal abnormality**. Open Targets reports no disease-associated target for the mapped idiopathic HH entity. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome)

### Reported genetic findings

* **SCN1A**—HGNC:10585; OMIM gene 182389—has been investigated because prolonged fever-triggered hemiclonic seizures are characteristic of Dravet syndrome. Variants are uncommon in clinically diagnosed HHE and should prompt reassessment for a Dravet-spectrum disorder.
* **1q44 microdeletion** has been described in a single HHE case; causality was explicitly uncertain ([Gupta et al., January 2014](https://doi.org/10.1002/ajmg.a.36198)).
* Individual secondary cases associated with monogenic/metabolic disorders do not establish those genes as causes of idiopathic HHE.

There are no HHE-specific curated variant lists, recurrent pathogenic alleles, allele-frequency estimates, somatic drivers, established modifier genes, epigenetic signatures, methylation episignatures, or chromosomal hotspots. Variant classification should therefore be assigned to the **underlying diagnosed genetic disease**, not to HHE itself.

---

## 5. Environmental information

Fever and acute infection are common seizure precipitants. Reported infections include routine febrile illnesses and isolated cases associated with influenza, HHV-6-related illness, and COVID-19/multisystem inflammatory syndrome. Infection may act through fever, cytokine signaling, altered blood–brain-barrier function, or direct encephalitis; pathogen detection does not automatically establish direct brain infection.

No consistent role is established for pollution, radiation, pesticides, heavy metals, occupation, smoking, alcohol, exercise, or nutrition. Lifestyle variables are largely inapplicable because onset usually occurs in very young children.

---

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream trigger:** fever/infection or another acute cerebral stressor in a susceptible young child.
2. **Prolonged unilateral seizure activity:** sustained excitatory firing markedly increases ATP and oxygen demand.
3. **Ionic and transmitter failure:** glutamate-dependent excitation, sodium and calcium entry, potassium disequilibrium, and impaired Na⁺/K⁺-ATPase activity produce cytotoxic edema.
4. **Neurovascular dysfunction:** hyperperfusion may initially compensate, but autoregulatory failure, blood–brain-barrier disruption, vasogenic edema, and relative hypoxia/ischemia can follow.
5. **Secondary injury:** mitochondrial dysfunction, reactive oxygen species, protease activation, inflammation, microglial and astrocytic activation, apoptosis/necrosis, and axonal injury expand the lesion.
6. **Clinical hemiplegia:** injury to unilateral motor cortex, subcortical white matter, basal ganglia, or corticospinal pathways causes contralateral weakness.
7. **Chronic remodeling:** neuronal loss, gliosis, hemispheric atrophy, and abnormal network reorganization create an epileptogenic substrate, producing delayed focal epilepsy.

The relative contributions of seizure-mediated excitotoxicity, inflammation, perfusion failure, venous congestion, and pre-existing vulnerability differ between patients. Pathology has shown inflammatory-degenerative changes, but no single protein dysfunction or enzyme deficiency defines HHE. A pathology/MRI report with mechanistic implications was published by Auvin et al. in June 2007 ([DOI](https://doi.org/10.1016/j.seizure.2007.01.009)); inflammatory-degenerative histology was also reported by Serino et al. in May 2014 ([DOI](https://doi.org/10.1016/j.ejpn.2013.11.001)).

### Ontology suggestions

* **GO biological process:** glutamatergic synaptic transmission (GO:0035249), regulation of membrane potential (GO:0042391), response to hypoxia (GO:0001666), inflammatory response (GO:0006954), microglial activation (GO:0001774), reactive oxygen species metabolic process (GO:0072593), neuron apoptotic process (GO:0051402), gliosis (GO:0042063).
* **Cell Ontology:** glutamatergic neuron (CL:0000679), GABAergic neuron (CL:0000617), astrocyte (CL:0000127), microglial cell (CL:0000129), oligodendrocyte (CL:0000128), brain vascular endothelial cell, pericyte.
* **GO cellular components:** synapse (GO:0045202), postsynaptic membrane (GO:0045211), mitochondrion (GO:0005739), axon (GO:0030424), myelin sheath (GO:0043209), blood–brain barrier-associated junctions.

### Molecular profiling and advanced technologies

No disease-specific validated transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics dataset was identified. Cytokines, diffusion metrics, and injury proteins remain investigational rather than diagnostic biomarkers.

---

## 7. Anatomical structures affected

The **central nervous system**, particularly one cerebral hemisphere, is primary. Acute abnormalities can involve cortex, subcortical white matter, hippocampus, basal ganglia, thalamus, and corticospinal projections. Chronic findings include unilateral cortical and white-matter volume loss, ventricular enlargement ex vacuo, gliosis, and possible Wallerian degeneration.

Suggested anatomy terms include cerebral hemisphere (**UBERON:0001869**), cerebral cortex (**UBERON:0000956**), cerebral white matter (**UBERON:0002437**), hippocampal formation (**UBERON:0002421**), basal ganglion (**UBERON:0002420**), thalamus (**UBERON:0001897**), and corticospinal tract. Laterality is essential: seizures and hemispheric MRI injury are generally ipsilateral, while hemiplegia is contralateral.

Secondary musculoskeletal consequences include unilateral spasticity, reduced limb growth/use, contracture, hip displacement, scoliosis, and impaired gait; these are complications of upper-motor-neuron injury rather than primary multiorgan disease.

---

## 8. Temporal development

* **Onset:** acute, usually in infancy or early childhood.
* **Acute phase:** prolonged hemiclonic status, often febrile; altered consciousness may persist after motor convulsions stop.
* **Early postictal phase:** hemiplegia becomes evident. MRI may initially be normal, but typically develops unilateral swelling, T2/FLAIR hyperintensity, and diffusion restriction.
* **Evolution over weeks to months:** edema resolves and unilateral atrophy/gliosis emerges. Longitudinal MRI findings in ten children were reported by Barcia et al. (published December 2013; [DOI](https://doi.org/10.1111/dmcn.12233)).
* **Chronic phase:** fixed or partially improving hemiparesis; delayed focal seizures may arise after months or years and persist lifelong.

The critical intervention window is the initial status episode: seizure termination and prevention of systemic secondary insults must occur within minutes, not after imaging changes become established.

---

## 9. Inheritance and population

No reliable prevalence per 100,000 or annual incidence estimate is available. Published evidence includes individual cases, a 10-child longitudinal MRI cohort, a 35-case clinical/imaging/EEG series, and regional retrospective series. These cannot establish population frequency and are vulnerable to referral and survivor bias.

HHE is not normally inherited. Consequently, Mendelian penetrance, anticipation, carrier frequency, founder effects, consanguinity, and germline mosaicism are not applicable unless an underlying genetic disorder is identified. No reproducible sex ratio, ancestry enrichment, or endemic geographic distribution is established. Apparent regional clusters may reflect infection burden, treatment access, or ascertainment rather than population genetics.

---

## 10. Diagnostics

### Clinical approach

Diagnosis is clinicoradiologic and longitudinal. The essential history is prolonged unilateral convulsive status followed by persistent contralateral motor deficit. Delayed recurrent focal seizures complete the HHE sequence.

**Acute investigations** should include:

* continuous or repeated **EEG**, particularly when consciousness does not recover, to exclude ongoing nonconvulsive status;
* urgent **MRI brain** with DWI/ADC, T2/FLAIR, susceptibility imaging, and vascular sequences; CT is useful when MRI is unavailable but is less sensitive;
* glucose, electrolytes, calcium, magnesium, blood count, liver/renal tests, inflammatory markers, cultures, and toxicology as indicated;
* lumbar puncture with microbiology/virology and autoimmune studies when safe and clinically indicated;
* metabolic testing—lactate, ammonia, plasma amino acids, acylcarnitines, urine organic acids—when presentation, imaging, or family history suggests a metabolic disorder.

The characteristic radiologic evolution is acute unilateral hemispheric edema/restricted diffusion followed by cerebral hemiatrophy. Freeman et al. described “characteristic early magnetic resonance imaging findings” (published January 2002; [DOI](https://doi.org/10.1177/088307380201700103)). A normal very-early MRI does not exclude HHE.

### Genetic testing

Genetic testing is not required to confirm acquired HHE, but is appropriate when there was prior developmental abnormality, recurrent fever-sensitive seizures, family history, dysmorphism, congenital anomalies, metabolic clues, or atypical/bilateral imaging.

A practical sequence is an epilepsy/developmental-encephalopathy panel including **SCN1A**, or trio exome/genome sequencing where phenotype is nonspecific. Chromosomal microarray is reasonable for congenital anomalies or intellectual disability. Mitochondrial, repeat-expansion, karyotype, and FISH testing are not routine unless specifically indicated. No HHE-specific liquid biopsy or omics diagnostic is available.

### Differential diagnosis

* **Dravet syndrome:** recurrent fever-sensitive hemiclonic/generalized seizures, often SCN1A-related; early MRI is usually normal and fixed unilateral destructive injury is not required.
* **Rasmussen encephalitis:** progressive focal seizures, epilepsia partialis continua, and gradually progressive unilateral atrophy rather than a single catastrophic febrile hemiclonic episode.
* **Arterial ischemic stroke/cerebral venous thrombosis:** vascular-territory or venous imaging abnormality; seizure may be a consequence rather than the primary insult.
* **Encephalitis/encephalopathy, FIRES/NORSE, or AESD:** generally more diffuse or multifocal seizure burden/imaging, although overlap exists.
* **Alternating hemiplegia of childhood:** recurrent reversible hemiplegic attacks, often ATP1A3-related, rather than fixed post-status deficit with hemiatrophy.
* **MELAS and metabolic stroke-like disorders:** recurrent nonvascular-territory lesions, lactic acidosis, multisystem features.
* **Todd paresis:** transient and resolves, without progressive hemispheric atrophy.
* **Structural focal epilepsy:** pre-existing malformation or lesion should be distinguishable on baseline/serial imaging.

There is no asymptomatic population, newborn, carrier, or cascade screening program for HHE.

---

## 11. Outcome and prognosis

No validated 5- or 10-year survival rate or disease-specific life-expectancy estimate exists. Death can occur during catastrophic status, cerebral edema, or systemic complications, but most literature emphasizes chronic morbidity.

Important long-term outcomes are persistent hemiparesis/spasticity, developmental and intellectual disability, language impairment, visual-field loss, orthopedic complications, and chronic—sometimes drug-resistant—focal epilepsy. Motor recovery is variable; complete recovery is less likely when early weakness is profound and MRI shows extensive cortex, deep nuclei, and white-matter injury.

Plausible adverse prognostic factors include longer/refractory status, delayed seizure control, extensive diffusion restriction, deep-gray involvement, severe edema or raised intracranial pressure, contralateral abnormalities, underlying encephalopathy, and subsequent high seizure burden. None is a clinically validated HHE prognostic biomarker.

---

## 12. Treatment

### Acute treatment

Treatment follows pediatric convulsive status-epilepticus protocols:

1. Airway, breathing, circulation; check glucose; correct hypoxia, hypotension, electrolyte disturbances, and hyperthermia.
2. Prompt benzodiazepine.
3. Rapid second-line antiseizure medication—commonly levetiracetam, fosphenytoin/phenytoin, or valproate, selected according to age, comorbidity, and suspected syndrome.
4. Refractory status: pediatric neurocritical care, continuous EEG, anesthetic infusion and/or additional agents according to protocol.
5. Treat suspected CNS infection empirically until excluded; manage intracranial pressure and severe edema with neurocritical-care/neurosurgical input.

Suggested intervention ontologies are NCIT concepts for **Anticonvulsant Therapy**, **Benzodiazepine**, **Levetiracetam**, **Fosphenytoin**, **Valproic Acid**, **Mechanical Ventilation**, and **Intensive Care**; exact NCIT codes should be verified in the target terminology release. Relevant chemical annotation examples include diazepam (**CHEBI:49575**), lorazepam (**CHEBI:6539**), and valproic acid (**CHEBI:39867**).

No agent has been proven to prevent hemispheric atrophy after the initial seizure. Therapeutic hypothermia, corticosteroids, IVIG, cytokine blockade, and other neuroprotective approaches are not established HHE therapies.

### Chronic treatment and rehabilitation

Antiseizure medication is individualized to seizure type and underlying etiology. Physical, occupational, speech/language, neuropsychological, visual, and orthopedic care should start early. Spasticity may require stretching, orthoses, botulinum toxin, oral antispastic medication, casting, or orthopedic surgery.

For disabling drug-resistant epilepsy arising from a severely injured hemisphere, multidisciplinary presurgical evaluation may support **functional hemispherectomy or hemispherotomy**. Kim et al. reported surgical treatment of delayed epilepsy in HHE (published May 2008; [DOI](https://doi.org/10.1212/01.wnl.0000289192.50924.93)). Evidence is observational; surgery trades existing or anticipated hemispheric disconnection deficits against seizure control.

A small report described ACTH for intractable HHE epilepsy ([Shimakawa et al., August 2015](https://doi.org/10.1016/j.braindev.2014.11.003)), but this does not establish routine efficacy.

### Trials and precision therapy

No dedicated HHE interventional trial or approved gene, cell, RNA, or targeted therapy was retrieved. Open Targets lists no associated therapeutic target for the mapped disease. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome) Genotype-guided treatment applies only when testing identifies another disorder, such as an SCN1A-related epilepsy.

---

## 13. Prevention

**Primary prevention:** no method prevents idiopathic HHE with certainty. Routine immunization and prompt treatment of serious infection reduce some febrile/infectious triggers but have not been shown specifically to prevent HHE.

**Secondary prevention:** caregiver education and an individualized rescue plan for children with previous prolonged seizures or a fever-sensitive epilepsy may shorten seizure duration. Rapid emergency response, early benzodiazepine administration where prescribed, and escalation according to status protocols are the most rational measures.

**Tertiary prevention:** control recurrent seizures; provide early rehabilitation; monitor contractures, hip alignment, scoliosis, nutrition, bone health, learning, behavior, communication, and caregiver burden; evaluate drug-resistant epilepsy early for surgery.

Genetic counseling should explain that classic acquired HHE does not itself confer Mendelian recurrence risk. Recurrence counseling must instead be based on any identified underlying disorder.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary equivalent of human HHE was identified in OMIA-oriented or literature searches. Animals can develop prolonged focal seizures, unilateral brain injury, paresis, and later epilepsy, but these observations do not constitute a validated naturally occurring HHE syndrome. There is no known zoonotic transmission.

Orthologues of susceptibility genes such as **SCN1A** are conserved in mouse, rat, zebrafish, and other vertebrates, but those orthologues model fever-sensitive epilepsy or sodium-channel disease—not the complete acquired HHE sequence.

---

## 15. Model organisms

No single model reproduces the full human triad with high fidelity. Relevant induced systems include:

* **Rodent prolonged-status models** using kainate, pilocarpine, electrical stimulation, or hyperthermia to study excitotoxicity, edema, neuronal death, gliosis, and epileptogenesis.
* **Immature-animal febrile-seizure/status models**, which address developmental susceptibility and the interaction between temperature and seizure injury.
* **SCN1A-deficient mouse or zebrafish models**, useful when studying Dravet-related phenocopies, but not representative of most acquired HHE.
* **Organotypic brain slices, neurons, astrocyte/microglia cultures, and blood–brain-barrier systems**, which isolate excitotoxic, inflammatory, and vascular mechanisms but cannot model hemiplegia or hemispheric network reorganization.

Major limitations are that chemically induced seizures are often bilateral, lesion laterality is artificial, rodent motor lateralization differs from humans, and models rarely reproduce the age-dependent sequence of fever-triggered unilateral status, permanent contralateral hemiplegia, progressive hemiatrophy, and delayed spontaneous focal epilepsy.

---

## Recent developments and expert assessment

The most directly relevant 2024 publication located was a radiologic case report and literature review by Essetti et al., published online in December 2024 ([DOI](https://doi.org/10.1016/j.radcr.2024.09.076)). Another 2024 report described cerebral hemiatrophy and hemiparesis after hemiclonic status in Dravet syndrome ([DOI](https://doi.org/10.1002/epd2.20170)), reinforcing the distinction between classic acquired HHE and genetically defined fever-sensitive epilepsy.

The main expert conclusion remains that HHE is best understood as a **rare acquired clinicoradiologic consequence of prolonged unilateral status in a vulnerable developing brain**. Current priorities are rapid status termination, serial MRI/EEG, rigorous investigation for an underlying etiology, early rehabilitation, and surgical evaluation of appropriately selected drug-resistant cases. The major research gaps are prospective incidence data, standardized diagnostic criteria, quantitative prognostic imaging, acute neuroprotection trials, and disease-specific longitudinal multi-omics.

## Evidence limitations

Direct abstract quotations could not be supplied reliably for most primary studies because many HHE articles were not available as searchable full text through the retrieval system. Titles quoted above—such as “Low incidence of SCN1A genetic mutation…”—are article titles, not presented as abstract quotations. PMID values were omitted where they could not be verified; DOI links and publication months/years are supplied instead to avoid introducing incorrect identifiers. Numerical estimates should not be inferred from selected imaging or surgical cohorts, and absence of a target or trial in the queried resources is evidence of a current database gap, not proof that no experimental work exists.

References

1. (OpenTargets Search: hemiconvulsion-hemiplegia-epilepsy syndrome): Open Targets Query (hemiconvulsion-hemiplegia-epilepsy syndrome, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Hemiconvulsion-Hemiplegia-Epilepsy_Syndrome-deep-research-falcon_artifacts/artifact-00.md)