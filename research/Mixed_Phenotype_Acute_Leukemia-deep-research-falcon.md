---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T17:02:50.374970'
end_time: '2026-07-31T17:10:36.465180'
duration_seconds: 466.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mixed Phenotype Acute Leukemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mixed_Phenotype_Acute_Leukemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mixed Phenotype Acute Leukemia
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Mixed Phenotype Acute Leukemia** covering all of the
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
- **Disease Name:** Mixed Phenotype Acute Leukemia
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Mixed Phenotype Acute Leukemia** covering all of the
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


# Mixed Phenotype Acute Leukemia: Disease Characteristics Research Report

**Scope.** This synthesis prioritizes WHO/ICC-era sources and 2023–2024 primary studies. Evidence labels distinguish human cohorts, expert reviews, experimental models, and trial records. DOI links are supplied because the retrieved records did not consistently expose PMIDs; PMIDs are therefore not invented. The data are aggregated disease-level evidence, not individual EHR data.

## Executive summary

Mixed phenotype acute leukemia (MPAL) is a rare, aggressive **acute leukemia of ambiguous lineage** in which the leukemic blasts meet lineage-defining criteria for more than one hematopoietic lineage. B/myeloid MPAL is most common, followed by T/myeloid MPAL. WHO-HAEM5 and the 2022 International Consensus Classification (ICC) combine immunophenotype with genetics and recognize genetically defined groups involving **BCR::ABL1, KMT2A, ZNF384**, and **BCL11B**. Current evidence generally favors an **ALL-type induction regimen**, addition of a tyrosine-kinase inhibitor (TKI) for BCR::ABL1-positive disease, close measurable residual disease (MRD) monitoring, and risk-adapted allogeneic hematopoietic stem-cell transplantation (HSCT), especially in adults. Pediatric patients who clear MRD early can frequently obtain durable remission with ALL therapy without routine HSCT. Recent single-cell studies identify marked inter- and intrapatient heterogeneity but a shared primitive/stem-like state that may explain lineage plasticity, relapse, and lineage switching. (sherban2025acuteleukemiaof pages 12-16, sherban2025acuteleukemiaof pages 20-24, sherban2025acuteleukemiaof pages 1-6, mumme2023singlecellrnasequencing pages 1-2, peretz2024multiomicsinglecell pages 1-2)

| Domain | Key facts | Key numbers | Evidence type | Source / DOI / NCT |
|---|---|---|---|---|
| Definition / classification | Mixed phenotype acute leukemia (MPAL; MONDO:0020743) is an acute leukemia of ambiguous lineage with blasts showing myeloid plus B- or T-lineage features. WHO/ICC-based criteria require lineage-defining markers; B/myeloid is the most common subtype. MPAL with AML-defining recurrent abnormalities such as t(8;21), inv(16), or t(15;17) is excluded from the MPAL category. | ALAL/MPAL represents ~2–3% of acute leukemias; B/myeloid ~67% of MPAL (sherban2025acuteleukemiaof pages 1-6, weinberg2024howtothink pages 5-6) | Classification review + cohort synthesis | Haematologica 2025 doi:10.3324/haematol.2025.287793; Hematology 2024 doi:10.1182/hematology.2024000554 (sherban2025acuteleukemiaof pages 1-6, weinberg2024howtothink pages 5-6) |
| Epidemiology | MPAL is rare in both children and adults. SEER-based incidence data cited in recent review support extreme rarity; pediatric cohorts show male predominance and substantial Hispanic representation in US series. | Incidence 0.35 per 1,000,000 person-years; pediatric MRD cohort: n=94, 66% male, 55% Hispanic, 46% age <10 years (sherban2025acuteleukemiaof pages 1-6, oberley2020significanceofminimal pages 2-3) | Registry/review + multicenter pediatric cohort | Haematologica 2025 doi:10.3324/haematol.2025.287793; Leukemia 2020 doi:10.1038/s41375-020-0741-0 (sherban2025acuteleukemiaof pages 1-6, oberley2020significanceofminimal pages 2-3) |
| Molecular subtypes | Recurrent genomic lesions include BCR::ABL1, KMT2A rearrangements, ZNF384 rearrangements, and BCL11B activation; RUNX1 mutations are enriched. B/myeloid and T/myeloid MPAL have different mutational and methylation patterns. | BCR::ABL1 in 15–20%; KMT2A-r ~10%; ZNF384-r up to 50% of pediatric B/myeloid MPAL; BCL11B activation 10–15% overall and up to one-third of T/myeloid MPAL (sherban2025acuteleukemiaof pages 9-12, weinberg2024howtothink pages 5-6) | Genomic cohort + review | Nature 2018 doi:10.1038/s41586-018-0436-0; Nature Communications 2018 doi:10.1038/s41467-018-04924-z; Hematology 2024 doi:10.1182/hematology.2024000554 (sherban2025acuteleukemiaof pages 9-12, weinberg2024howtothink pages 5-6) |
| Diagnostics | Diagnosis integrates morphology, multiparameter flow cytometry, cytogenetics/FISH, and NGS/RNA fusion testing. Pediatric centrally reviewed cases were predominantly B/myeloid, MPO-positive and CD19-positive. Differential diagnosis includes secondary AML with mixed phenotype, which behaves differently from true MPAL. | Pediatric cohort: 89% B/myeloid, 94% MPO+, 90% CD19+; ALL-directed induction CR 96.6% in MPAL vs 14.3% in secondary AML with mixed phenotype in cited comparative series (oberley2020significanceofminimal pages 2-3, sherban2025acuteleukemiaof pages 6-9) | Multicenter cohort + comparative clinicopathologic study | Leukemia 2020 doi:10.1038/s41375-020-0741-0; Haematologica 2025 doi:10.3324/haematol.2025.287793 (oberley2020significanceofminimal pages 2-3, sherban2025acuteleukemiaof pages 6-9) |
| First-line therapy | Current expert consensus favors ALL-type induction for most MPAL, with TKI added for Philadelphia-positive/BCR::ABL1-positive disease. Pediatric data support ALL therapy without routine upfront HSCT in many cases. | Meta-analytic effect cited: ALL-based therapy superior for CR and OS (OR 0.33 and 0.45 vs AML-based, direction favoring ALL); pediatric 5-year EFS 80%±4% with ALL-type vs 36%±7.2% with AML-type; HyperCVAD CR/CRi 84% in adults (sherban2025acuteleukemiaof pages 12-16, orgel2020mixed‐phenotypeacuteleukemia pages 1-2) | Review/meta-analysis + pediatric cohort | Haematologica 2025 doi:10.3324/haematol.2025.287793; Cancer 2020 doi:10.1002/cncr.32552 (sherban2025acuteleukemiaof pages 12-16, orgel2020mixed‐phenotypeacuteleukemia pages 1-2) |
| MRD / HSCT | MRD is a major prognostic marker. In children, early MRD negativity predicts better survival and may support avoiding HSCT in CR1; in adults, HSCT is often considered for high-risk disease, persistent MRD, or adverse genetics. | 70% EOI MRD-negative after ALL induction; EOI MRD positivity HR 6.00 for 5-year EFS and HR 9.57 for OS; adult transplant registry: 3-year relapse 31.4%, NRM 22.1%, LFS 46.5%, OS 56.3%; MRD-negative adults after induction had 75.8% vs 45.2% 5-year OS in one study (oberley2020significanceofminimal pages 1-2, sherban2025acuteleukemiaof pages 20-24) | Multicenter pediatric cohort + adult transplant registry/review | Leukemia 2020 doi:10.1038/s41375-020-0741-0; Haematologica 2025 doi:10.3324/haematol.2025.287793 (oberley2020significanceofminimal pages 1-2, sherban2025acuteleukemiaof pages 20-24) |
| Prognosis | MPAL overall has poorer outcomes than standard-risk ALL and many AML subsets, but prognosis varies by age, genetics, MRD, and therapy. KMT2A-rearranged and complex-karyotype disease are adverse; Ph+ disease outcomes improve with TKI-based therapy. | Pediatric COG cohort: 5-year EFS 72%±8%, OS 77%±7%; ALL-only/no HSCT subgroup EFS 75%±13%, OS 84%±11%; Ph+ MPAL median OS 53.6 months, 5-year OS 49%; AUL median OS 1.4 months; KMT2A-r associated with ~10-fold increased mortality risk in cited review (orgel2020mixed‐phenotypeacuteleukemia pages 1-2, sherban2025acuteleukemiaof pages 12-16) | Pediatric cohort + review synthesis | Cancer 2020 doi:10.1002/cncr.32552; Haematologica 2025 doi:10.3324/haematol.2025.287793 (orgel2020mixed‐phenotypeacuteleukemia pages 1-2, sherban2025acuteleukemiaof pages 12-16) |
| Recent single-cell developments | Recent 2023–2024 single-cell studies show MPAL is highly heterogeneous yet shares stem-like programs. Pediatric scRNA-seq distinguished B/myeloid from T/myeloid MPAL; adult multiomic single-cell profiling identified a stem-like transcriptional state and a prognostic MPAL95 score. | Pediatric scRNA-seq: >40,000 cells from 9 cases; 44% relapsed/refractory overall in that cohort; adult multiomic study: 14 newly diagnosed cases; MPAL95 predicted survival in an independent cohort (mumme2023singlecellrnasequencing pages 1-2, peretz2024multiomicsinglecell pages 1-2) | Primary single-cell / multiomic studies | Genome Medicine 2023 doi:10.1186/s13073-023-01241-z; Nature Communications 2024 doi:10.1038/s41467-024-52317-2 (mumme2023singlecellrnasequencing pages 1-2, peretz2024multiomicsinglecell pages 1-2) |
| Experimental / translational trials | Active/modern trials are testing lower-intensity or targeted strategies, especially for adults or newly diagnosed disease: blinatumomab for CD19+ MPAL, venetoclax/azacitidine-based combinations, and other investigational regimens. Preclinical ZNF384 models support FLT3 inhibition. | NCT07222579 recruiting (subcutaneous blinatumomab; adult CD19+ MPAL; planned enrollment 78); NCT07517510 phase 2 enrolling by invitation (homoharringtonine + venetoclax + azacitidine; enrollment 40); NCT07573670 phase 2 not yet recruiting (BCL-2 inhibitor + azacitidine; enrollment 52); ZNF384 study tested 71 leukemia samples plus 15 MPAL samples and showed gilteritinib activity in PDX models (NCT07222579 chunk 3, NCT07517510 chunk 1, NCT07573670 chunk 2, dickerson2022znf384fusiononcoproteins pages 15-15) | Clinical trials + preclinical functional study | ClinicalTrials.gov NCT07222579, NCT07517510, NCT07573670; Blood Cancer Discovery 2022 doi:10.1158/2643-3230.bcd-21-0163 (NCT07222579 chunk 3, NCT07517510 chunk 1, NCT07573670 chunk 2, dickerson2022znf384fusiononcoproteins pages 15-15) |


*Table: Concise knowledge-base summary table for mixed phenotype acute leukemia covering classification, epidemiology, molecular features, diagnostics, treatment, prognosis, and recent translational developments. It highlights key numbers and cites the available evidence contexts and trial identifiers for rapid downstream curation.*

## 1. Disease information

### Definition and classification

MPAL belongs to the category **acute leukemia of ambiguous lineage (ALAL)**. Unlike acute undifferentiated leukemia, MPAL has convincing evidence of commitment to at least two lineages. Disease may be:

* **Biphenotypic:** one blast population co-expresses lineage-defining markers.
* **Bilineal/trilineal:** two or more immunophenotypically discrete blast populations together constitute the acute leukemia; bilineal disease may have inferior outcomes.
* **Phenotypic groups:** B/myeloid (approximately 67%), T/myeloid, rare B/T, B/T/myeloid, or T/megakaryoblastic disease. (sherban2025acuteleukemiaof pages 6-9, sherban2025acuteleukemiaof pages 1-6)

WHO/ICC exclude cases whose mixed immunophenotype occurs in an otherwise defining AML entity, including AML with **t(8;21)/RUNX1::RUNX1T1, inv(16)/CBFB::MYH11**, or **t(15;17)/PML::RARA**. Therapy-related or secondary AML with aberrant lymphoid markers must likewise be separated from genuine MPAL. (sherban2025acuteleukemiaof pages 6-9, weinberg2024howtothink pages 5-6)

### Identifiers and synonyms

* **MONDO:** **MONDO:0020743**.
* **Parent concept:** acute leukemia of ambiguous lineage, MONDO:0019460.
* **Synonyms:** mixed-phenotype acute leukemia, mixed phenotype acute leukaemia, MPAL, biphenotypic acute leukemia, bilineal acute leukemia, mixed-lineage acute leukemia. “Biphenotypic leukemia” is historical and should not be treated as exactly synonymous in modern classification.
* **MeSH/OMIM/Orphanet:** no reliably verified MPAL-specific identifiers were exposed by the retrieved primary records. MPAL is a somatic cancer category rather than a classic single-gene Mendelian OMIM disorder.
* **ICD:** ICD-10-CM lacks a robust phenotype-specific MPAL code and cases are commonly mapped under acute leukemia/acute leukemia of ambiguous cell type according to local coding rules; ICD-11 classification should be verified against the deploying jurisdiction’s current release.

Open Targets independently maps MPAL to MONDO:0020743 and identifies clinically relevant lineage targets CD19 and the CD3 complex; this is target-association evidence, not proof that these genes cause MPAL. (OpenTargets Search: mixed phenotype acute leukemia)

## 2. Etiology, risk, and protective factors

MPAL is predominantly a **sporadic clonal somatic malignancy**. Its proximate causes are acquired driver rearrangements/mutations and epigenetic dysregulation in a hematopoietic stem or early progenitor cell capable of multilineage differentiation. There is no single necessary causal gene.

* **Genetic drivers:** BCR::ABL1, KMT2A rearrangements, ZNF384 fusions, and BCL11B activation are the best-established recurrent lesions. Cooperating alterations affect RUNX1, WT1, ETV6, CEBPA, FLT3/JAK–STAT, RAS, IKZF1, and PAX5, among others. (sherban2025acuteleukemiaof pages 9-12, weinberg2024howtothink pages 5-6)
* **Age:** KMT2A-rearranged disease is enriched in infants/children; BCR::ABL1-positive B/myeloid MPAL is enriched in older patients. ZNF384-rearranged disease is particularly prominent in pediatric B/myeloid MPAL. (sherban2025acuteleukemiaof pages 9-12)
* **Secondary disease:** prior myelodysplasia, cytotoxic therapy, or an AML-type mutation pattern should raise concern for secondary AML with mixed phenotype rather than de novo MPAL. In one comparison, secondary AML with mixed phenotype had median overall survival of 10.3 months versus 42.8 months for MPAL and responded very differently to ALL induction. (sherban2025acuteleukemiaof pages 6-9)

No MPAL-specific, reproducible associations with smoking, alcohol, diet, infection, occupation, pollution, or a defined gene–environment interaction were identified. General leukemia risks such as ionizing radiation and prior cytotoxic therapy should not be automatically annotated as MPAL-specific causes. No validated genetic or environmental protective factors are known. These are evidence gaps, not demonstrations that such effects cannot exist.

## 3. Phenotypes

MPAL has an **acute, severe, progressive** presentation at any age. Clinical manifestations largely result from marrow replacement and tissue infiltration rather than from the mixed immunophenotype itself.

| Phenotype | Type and usual behavior | Suggested HPO term |
|---|---|---|
| Anemia, fatigue, pallor, dyspnea | Laboratory abnormality/symptom; common, variable severity | Anemia (HP:0001903), Fatigue (HP:0012378), Pallor (HP:0000980) |
| Thrombocytopenia, bruising, bleeding/petechiae | Laboratory/sign; may become life-threatening | Thrombocytopenia (HP:0001873), Abnormal bleeding (HP:0001892), Petechiae (HP:0000967) |
| Neutropenia, fever, recurrent/severe infection | Laboratory/symptom; fluctuates and worsens with chemotherapy | Neutropenia (HP:0001875), Fever (HP:0001945), Recurrent infections (HP:0002719) |
| Leukocytosis or circulating blasts | Laboratory abnormality; variable | Leukocytosis (HP:0001974), Abnormality of leukocytes (HP:0001881) |
| Bone pain | Symptom, particularly in children | Bone pain (HP:0002653) |
| Hepatosplenomegaly/lymphadenopathy | Clinical signs of infiltration | Hepatomegaly (HP:0002240), Splenomegaly (HP:0001744), Lymphadenopathy (HP:0002716) |
| CNS involvement | Complication at diagnosis or relapse; uncommon but clinically important | Abnormality of the central nervous system (HP:0002011) |
| Mixed-lineage blast phenotype | Defining laboratory/pathology feature | No single adequate HPO term; encode with pathology/NCIT plus marker findings |

A 94-patient pediatric cohort was 89% B/myeloid, 94% MPO-positive, and 90% CD19-positive; 70% had presenting leukocytes below 50,000/µL and 68% were CNS1. These figures describe one US cohort rather than universal frequencies. (oberley2020significanceofminimal pages 2-3)

**Quality of life.** MPAL-specific EQ-5D, SF-36, PROMIS, or utility studies were not identified. Expected impacts include hospitalization, infection isolation, transfusion dependence, treatment toxicity, impaired schooling/work, fertility concerns, and psychological burden, but these should be labeled extrapolations from acute leukemia care rather than MPAL-specific measured effects.

## 4. Genetic and molecular information

### Recurrent somatic lesions

* **BCR::ABL1:** approximately 15–20%, usually B/myeloid and enriched with increasing age. It encodes a constitutively active ABL tyrosine kinase and is therapeutically actionable with a TKI. (sherban2025acuteleukemiaof pages 9-12)
* **KMT2A rearrangement:** approximately 10%; enriched in infants and younger children, usually B/myeloid, and associated with especially poor prognosis. (sherban2025acuteleukemiaof pages 12-16, sherban2025acuteleukemiaof pages 9-12)
* **ZNF384 rearrangement:** reported in up to 50% of pediatric B/myeloid MPAL but uncommon in adult MPAL. Fusion partners include EP300, CREBBP, TCF3, and others. (sherban2025acuteleukemiaof pages 9-12)
* **BCL11B activation/rearrangement:** about 10–15% of MPAL overall and up to one-third of T/myeloid MPAL; it links T/myeloid MPAL biologically to early T-cell precursor ALL. (sherban2025acuteleukemiaof pages 9-12, weinberg2024howtothink pages 5-6)
* **Other alterations:** T/myeloid disease has relatively high mutation burden involving WT1, ETV6, RUNX1, CEBPA, FLT3 and JAK–STAT signaling; B/myeloid disease more often has IKZF1, PAX5, and RAS-pathway lesions. Complex karyotype is adverse. (sherban2025acuteleukemiaof pages 9-12)

These are **somatic structural variants or somatic sequence variants** in the leukemia clone. Population allele frequencies in gnomAD are therefore generally not meaningful for the defining fusions. Patient-specific germline testing is appropriate when age, personal/family history, or the variant allele pattern suggests an inherited leukemia-predisposition syndrome; MPAL itself does not have a defined Mendelian inheritance pattern.

### Epigenetics and functional consequence

Adult integrative profiling separated MPAL into AML-like and ALL-like DNA-methylation groups; lineage-matched therapy produced complete response in 72% versus 22% with molecularly mismatched treatment, supporting a biological rather than merely descriptive role for epigenetic lineage state. Genetically similar blast compartments can display different phenotypes, indicating that epigenetic regulation contributes substantially to lineage ambiguity. (sherban2025acuteleukemiaof pages 12-16, sherban2025acuteleukemiaof pages 9-12)

In ZNF384-rearranged experimental systems, fusion proteins occupy enhancer/intragenic regions, increase H3 lysine acetylation, deregulate stem-cell transcription factors, skew HSPCs toward myeloid differentiation, and promote self-renewal. The study’s abstract states that the fusions “**promote hematopoietic expansion, myeloid lineage skewing, and self-renewal**.” NRAS^G12D or another cooperating proliferative lesion was required for fully penetrant leukemia in mouse HSPCs, whereas human HSPCs developed B/myeloid leukemia. (dickerson2022znf384fusiononcoproteins pages 15-15)

## 5. Environmental and infectious information

There is no established MPAL-specific infectious agent, toxin, dietary exposure, exercise pattern, alcohol association, or smoking association. MPAL is not contagious. Prior chemotherapy/radiotherapy may precede secondary myeloid disease with mixed marker expression, but rigorous distinction from de novo MPAL is essential. No validated MPAL-specific chemopreventive or lifestyle intervention exists.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream initiation:** an acquired rearrangement or mutation occurs in a multipotent HSPC or early progenitor.
2. **Lineage-program disruption:** fusion oncoproteins or transcription-factor dysregulation alter enhancer use, chromatin state, and lineage-specifying transcription.
3. **Cooperating proliferation/survival signaling:** RAS, FLT3, JAK–STAT, ABL1, or related lesions increase survival and expansion.
4. **Stemness and plasticity:** the clone retains multilineage differentiation potential, generating biphenotypic or bilineal blast compartments.
5. **Marrow/tissue expansion:** blasts suppress normal erythropoiesis, granulopoiesis, and megakaryopoiesis, producing anemia, infection, bleeding, and tissue infiltration.
6. **Treatment selection:** lineage-targeted therapy can select phenotypically distinct subclones or promote lineage switch; persistent stem-like/MRD compartments seed relapse. (sherban2025acuteleukemiaof pages 9-12, mumme2023singlecellrnasequencing pages 1-2, peretz2024multiomicsinglecell pages 1-2, dickerson2022znf384fusiononcoproteins pages 15-15)

### Molecular profiling and advanced technologies

The 2023 pediatric scRNA-seq study analyzed **>40,000 cells from nine marrow samples**. B/myeloid and T/myeloid MPAL had distinct signatures; both overexpressed **MAP2K2** and **CD81**, while HBEGF marked B/myeloid and PTEN marked T/myeloid disease. T/myeloid MPAL overlapped strongly with early T-cell precursor ALL, and relapsed samples showed IL-16-pathway upregulation. The abstract concludes that the subtypes have “**distinct scRNAseq profiles from each other, AML, and ALL**.” (mumme2023singlecellrnasequencing pages 1-2)

A September 2024 adult multiomic study profiled **14 newly diagnosed patients** and found that genotype or transcriptome did not reliably predict immunophenotype. A shared primitive transcriptional state correlated with differentiation potential and poorer survival; its 95-gene **MPAL95** score predicted survival in an independent bulk-RNA cohort. The authors’ central conclusion was that MPAL blasts express a “**shared stem cell-like transcriptional profile indicative of high differentiation potential**.” (peretz2024multiomicsinglecell pages 1-2)

Suggested annotations include **GO:0030097 hemopoiesis**, **GO:0045165 cell fate commitment**, **GO:0008283 cell population proliferation**, **GO:0007049 cell cycle**, **GO:0043066 negative regulation of apoptotic process**, **GO:0045595 regulation of cell differentiation**, **GO:0006355 regulation of transcription**, and **GO:0040029 regulation of gene expression, epigenetic**. Relevant cell types include hematopoietic stem cell, hematopoietic multipotent progenitor, lymphoid progenitor, myeloid progenitor, B-lineage lymphoblast, T-lineage lymphoblast, and myeloblast; exact CL identifiers should be ontology-release validated before production ingestion.

## 7. Anatomical structures affected

* **Primary:** bone marrow (**UBERON:0002371**), peripheral blood, and hematopoietic/lymphoid system.
* **Secondary:** spleen (**UBERON:0002106**), liver (**UBERON:0002107**), lymph nodes (**UBERON:0000029**), CNS, skin, and other extramedullary sites.
* **Cellular:** leukemic HSPC/progenitor and its phenotypically diverse blast descendants.
* **Subcellular:** nucleus and chromatin for transcription-factor fusions; cytoplasm/membrane for lineage markers; cytoplasmic and nuclear tyrosine-kinase signaling for BCR::ABL1.
* **Lateralization:** not applicable.

Non-leukemic pediatric MPAL/lymphoma can occur in lymph node, skin, or other extranodal sites. In one prospective series, 11 such cases were found among 146 lymphoblastic lymphomas; all entered complete remission on a lymphoblastic lymphoma protocol. (martin‐guerrero2019non‐leukemicpediatricmixed pages 1-4, martin‐guerrero2019non‐leukemicpediatricmixed pages 16-17)

## 8. Temporal development

Onset is **acute**, developing over days to weeks clinically, although somatic evolution precedes symptoms. It occurs from infancy through old age. Untreated disease is rapidly progressive and not self-limited. Clinical phases are diagnosis, induction, remission/MRD assessment, consolidation/maintenance, and either durable remission or relapse/refractory disease; conventional solid-tumor AJCC staging is not applicable.

The key intervention window is induction and early MRD clearance. In children, end-of-induction MRD positivity was strongly associated with inferior 5-year EFS (HR 6.00) and OS (HR 9.57). Relapse can preserve phenotype, become more homogeneous, or undergo lineage switch. (oberley2020significanceofminimal pages 1-2)

## 9. Inheritance, epidemiology, and population

ALAL/MPAL represents approximately **2–3%** of acute leukemias; a recent review cited a SEER incidence of approximately **0.35 per million person-years**. Broader publications have reported 1–5%, reflecting changes in diagnostic criteria and referral populations. (orgel2020mixed‐phenotypeacuteleukemia pages 1-2, sherban2025acuteleukemiaof pages 1-6)

A nine-case pediatric single-cell cohort had mean age 13.4 years and was 78% male, whereas the larger 94-patient US cohort was 66% male and 55% Hispanic. These observations do not establish a biological ethnic predisposition and may reflect ascertainment and center demographics. (mumme2023singlecellrnasequencing pages 4-5, oberley2020significanceofminimal pages 2-3)

There is no standard autosomal-dominant, autosomal-recessive, X-linked, mitochondrial, founder, carrier-frequency, anticipation, or germline-mosaicism model for MPAL. Penetrance and carrier frequency are therefore not applicable at the disease level. Germline predisposition should be recorded separately when demonstrated.

## 10. Diagnostics

### Recommended workflow

1. **CBC, differential, peripheral smear**, coagulation and tumor-lysis chemistry.
2. **Bone-marrow aspirate/core biopsy** for morphology and blast burden.
3. **Multiparameter flow cytometry** with intensity compared with normal counterparts and assessment for one versus multiple blast populations.
4. **Karyotype and FISH**, including BCR::ABL1 and KMT2A; add probes guided by phenotype.
5. **Broad DNA NGS plus RNA fusion sequencing**, because cryptic ZNF384/BCL11B and kinase fusions may be missed by karyotype or limited panels.
6. **HLA typing** and baseline organ assessment if HSCT is plausible.
7. **MRD assay design at diagnosis**, preserving all abnormal compartments and considering fusion-specific PCR/NGS where validated.

### Lineage-defining criteria

* **Myeloid:** myeloperoxidase (MPO), or monocytic differentiation supported by at least two markers such as CD11c, CD14, CD64, lysozyme, or nonspecific esterase.
* **T lineage:** strong surface or cytoplasmic CD3; recent guidance uses intensity greater than 50% of mature T-cell levels.
* **B lineage:** strong CD19 plus appropriate additional B markers; recent guidance compares intensity with normal B-cell progenitors.
* Acute disease generally requires an aggregate **≥20% blasts**, while genetically defined entities and classification-specific exceptions require careful WHO/ICC application. (sherban2025acuteleukemiaof pages 6-9, sherban2025acuteleukemiaof pages 1-6)

### Differential diagnosis

Exclude AML with defining recurrent genetics, B-ALL or T-ALL with aberrant myeloid antigen expression, early T-cell precursor ALL, AML with minimal differentiation, acute megakaryoblastic leukemia, secondary/therapy-related AML, blast-phase CML, myeloid/lymphoid neoplasms with eosinophilia and kinase rearrangement, and acute undifferentiated leukemia. Merely expressing CD13, CD33, CD7, or another cross-lineage antigen is insufficient for MPAL.

No population, newborn, prenatal, carrier, or asymptomatic screening is recommended. WES/WGS may help unresolved cases but does not replace flow cytometry and RNA fusion detection. Mitochondrial or repeat-expansion testing is not relevant.

## 11. Outcome and prognosis

In a centrally reviewed Children’s Oncology Group cohort, 5-year EFS was **72%±8%** and OS **77%±7%**. Children treated with ALL chemotherapy alone without HSCT had 5-year EFS **75%±13%** and OS **84%±11%**, although selection bias limits causal interpretation. (orgel2020mixed‐phenotypeacuteleukemia pages 1-2)

In an adult transplant registry of 519 MPAL patients, 3-year relapse was **31.4%**, non-relapse mortality **22.1%**, leukemia-free survival **46.5%**, and OS **56.3%**. Another adult series reported 5-year OS of 54% after transplantation; MRD-negative patients had 75.8% versus 45.2% survival. (sherban2025acuteleukemiaof pages 20-24)

Adverse factors include older age, complex karyotype, KMT2A rearrangement, secondary AML-type biology, induction failure, and persistent MRD. BCR::ABL1-positive prognosis has improved substantially with TKI therapy; one synthesis reported median OS 53.6 months and 5-year OS 49%. (sherban2025acuteleukemiaof pages 12-16, sherban2025acuteleukemiaof pages 9-12)

Major complications include bacterial/fungal infection, hemorrhage, tumor lysis, leukostasis, organ toxicity, infertility, graft-versus-host disease, relapse, and lineage switch. MPAL-specific long-term disability and quality-of-life statistics remain sparse.

## 12. Treatment

### Current strategy

1. **ALL-type induction** is generally preferred over AML or hybrid induction. A synthesis found superior complete remission and OS with ALL therapy; pediatric 5-year EFS was reported as 80%±4% with ALL-type versus 36%±7.2% with AML-type therapy. Hyper-CVAD produced CR/CRi in 84% in an adult series. (sherban2025acuteleukemiaof pages 12-16)
2. **BCR::ABL1-positive MPAL:** add an ABL TKI (e.g., imatinib, dasatinib, ponatinib selected by patient and mutation context) promptly.
3. **MRD-adapt therapy:** repeat flow and/or molecular MRD after induction and consolidation. Pediatric end-of-induction MRD negativity below 0.01% occurred in 70% and strongly predicted favorable outcome. (oberley2020significanceofminimal pages 1-2)
4. **HSCT:** not routinely necessary for every pediatric patient who clears MRD; consider in adults, persistent MRD, induction failure, adverse genetics, or relapse. Conditioning choice and comorbidity must be individualized. (sherban2025acuteleukemiaof pages 20-24)
5. **Relapse/targeted therapy:** CD19-positive disease may receive blinatumomab; CD19/CD22-targeted antibodies or CAR-T approaches are biologically plausible but can select lineage-negative or switched clones. Venetoclax-based therapy is investigational. ZNF384-rearranged preclinical models suggest FLT3 inhibition. (dickerson2022znf384fusiononcoproteins pages 15-15, NCT07222579 chunk 3)

Suggested NCIT concepts include acute lymphoblastic leukemia chemotherapy regimen, hyper-CVAD regimen, tyrosine kinase inhibitor therapy, blinatumomab, chimeric antigen receptor T-cell therapy, allogeneic hematopoietic stem-cell transplantation, measurable residual disease assessment, venetoclax, azacitidine, and supportive transfusion therapy; exact NCIT codes should be release validated.

### Current trials and real-world implementation

* **NCT05327894 (Interfant-21):** recruiting phase 3 protocol for infants with KMT2A-rearranged ALL or MPAL; target enrollment 160. Open Targets links this trial to CD19/CD3-relevant MPAL biology. (OpenTargets Search: mixed phenotype acute leukemia)
* **NCT04872478:** recruiting phase 1 MRX-2843 study in adolescent/adult relapsed or refractory AML, ALL, or MPAL; target enrollment 50.
* **NCT07222579:** recruiting subcutaneous blinatumomab study for adult CD19-positive MPAL, including chemotherapy-ineligible, MRD-positive, and relapsed/refractory cohorts. (NCT07222579 chunk 3)
* **NCT07517510:** phase 2 HVA—homoharringtonine, venetoclax, and azacitidine—for newly diagnosed adult MPAL; planned n=40, with 2026 start. (NCT07517510 chunk 1)
* **NCT07573670:** phase 2 BCL-2 inhibitor plus azacitidine for newly diagnosed BCR::ABL1-negative MPAL; planned n=52. (NCT07573670 chunk 2)
* **NCT02135874:** completed phase 2 hybrid clofarabine/idarubicin/cytarabine/vincristine/dexamethasone study, illustrating prior attempts to cover both myeloid and lymphoid biology. (NCT02135874 chunk 2)

These trials are investigational and do not establish efficacy. Supportive care follows acute leukemia standards: tumor-lysis prophylaxis, antimicrobial prophylaxis, irradiated/leukoreduced blood products, fertility preservation, nutrition, psychosocial care, and rehabilitation after deconditioning.

## 13. Prevention

No MPAL-specific primary prevention, vaccine, screening program, prophylactic medication, or validated behavioral intervention exists. Sensible measures include minimizing unnecessary ionizing radiation and carcinogenic exposure and following survivors of prior cytotoxic therapy according to established oncology guidance, but there is no evidence that these measures specifically prevent MPAL.

Secondary prevention is limited to prompt evaluation of unexplained cytopenias, leukocytosis, bruising, infection, or constitutional symptoms; routine screening of asymptomatic people is not justified by the very low incidence. Tertiary prevention includes infection and tumor-lysis prophylaxis, MRD-guided relapse prevention, vaccination planning after chemotherapy/HSCT, and survivorship surveillance. Genetic counseling is indicated only where a separate germline predisposition is suspected or demonstrated.

## 14. Other species and natural disease

No well-defined, naturally occurring veterinary disease that is taxonomically equivalent to human WHO/ICC MPAL was identified. Dogs, cats, and other animals can develop leukemias with ambiguous immunophenotypes, but diagnostic comparability and recurrent molecular drivers are insufficient to annotate these as the same disease. MPAL is not infectious or zoonotic, and cross-species transmission is not applicable.

## 15. Model organisms and experimental systems

The strongest disease models are molecularly engineered systems rather than spontaneous animal disease:

* **EP300::Znf384 knock-in mouse and virally transduced mouse HSPCs:** reproduce progenitor expansion, myeloid skewing, and self-renewal; a cooperating NRAS^G12D lesion was required for fully penetrant leukemia. Limitation: engineered genotype and murine hematopoiesis do not reproduce all human MPAL heterogeneity. (dickerson2022znf384fusiononcoproteins pages 15-15)
* **Human CD34+ HSPCs expressing ZNF384 fusion:** generate B/myeloid leukemia and more directly model human lineage ambiguity. (dickerson2022znf384fusiononcoproteins pages 15-15)
* **Patient-derived xenografts:** preserve aspects of human clone biology and support drug testing. A ZNF384-rearranged xenograft showed marked in-vivo response to the FLT3 inhibitor gilteritinib. Limitation: immunodeficient recipients cannot model an intact immune microenvironment. (dickerson2022znf384fusiononcoproteins pages 15-15)
* **Primary single-cell datasets:** pediatric scRNA-seq and adult DNA/RNA/protein multiomics resolve intratumoral states but are observational and based on nine and 14 patients, respectively. (mumme2023singlecellrnasequencing pages 1-2, peretz2024multiomicsinglecell pages 1-2)

Relevant species are **Homo sapiens (NCBI Taxon 9606)** and **Mus musculus (NCBI Taxon 10090)**. Useful resources include MGI/IMSR for engineered mice, Cellosaurus for cell models, and GEO/SRA for transcriptomic datasets.

## Evidence limitations and expert interpretation

The central uncertainty is not whether MPAL exists, but how best to define and treat its biologically diverse forms. Diagnostic criteria have changed repeatedly, sample sizes are small, and adult and pediatric disease differ. The most defensible current interpretation is that MPAL comprises several genomic diseases converging on **early-progenitor lineage plasticity**, not one uniform cancer. This explains why immunophenotype alone is an imperfect treatment guide and why integrated flow cytometry, fusion testing, mutation profiling, epigenetic/transcriptomic characterization, and MRD are increasingly important. The 2024 single-cell data are promising for risk stratification, but MPAL95 and methylation-guided therapy require prospective validation before routine implementation. (sherban2025acuteleukemiaof pages 9-12, weinberg2024howtothink pages 5-6, peretz2024multiomicsinglecell pages 1-2)

### Key source URLs and publication dates

* Weinberg, *Hematology*, December 2024: https://doi.org/10.1182/hematology.2024000554. (weinberg2024howtothink pages 5-6)
* Peretz et al., *Nature Communications*, September 2024: https://doi.org/10.1038/s41467-024-52317-2. (peretz2024multiomicsinglecell pages 1-2)
* Mumme et al., *Genome Medicine*, October 2023: https://doi.org/10.1186/s13073-023-01241-z. (mumme2023singlecellrnasequencing pages 1-2)
* Dickerson et al., *Blood Cancer Discovery*, March 2022: https://doi.org/10.1158/2643-3230.bcd-21-0163. (dickerson2022znf384fusiononcoproteins pages 15-15)
* Orgel et al., *Cancer*, 2020: https://doi.org/10.1002/cncr.32552. (orgel2020mixed‐phenotypeacuteleukemia pages 1-2)
* Oberley et al., *Leukemia*, February 2020: https://doi.org/10.1038/s41375-020-0741-0. (oberley2020significanceofminimal pages 1-2)
* Alexander et al., *Nature*, September 2018: https://doi.org/10.1038/s41586-018-0436-0. (sherban2025acuteleukemiaof pages 9-12)
* Takahashi et al., *Nature Communications*, July 2018: https://doi.org/10.1038/s41467-018-04924-z. (sherban2025acuteleukemiaof pages 9-12)

References

1. (sherban2025acuteleukemiaof pages 12-16): Adi Sherban and Ofir Wolach. Acute leukemia of ambiguous lineage: the known and the uncertain. Haematologica, 111:813-827, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287793, doi:10.3324/haematol.2025.287793. This article has 3 citations.

2. (sherban2025acuteleukemiaof pages 20-24): Adi Sherban and Ofir Wolach. Acute leukemia of ambiguous lineage: the known and the uncertain. Haematologica, 111:813-827, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287793, doi:10.3324/haematol.2025.287793. This article has 3 citations.

3. (sherban2025acuteleukemiaof pages 1-6): Adi Sherban and Ofir Wolach. Acute leukemia of ambiguous lineage: the known and the uncertain. Haematologica, 111:813-827, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287793, doi:10.3324/haematol.2025.287793. This article has 3 citations.

4. (mumme2023singlecellrnasequencing pages 1-2): Hope L. Mumme, Sunil S. Raikar, Swati S. Bhasin, Beena E. Thomas, Taylor Lawrence, Elizabeth P. Weinzierl, Yakun Pang, Deborah DeRyckere, Chuck Gawad, Daniel S. Wechsler, Christopher C. Porter, Sharon M. Castellino, Douglas K. Graham, and Manoj Bhasin. Single-cell rna sequencing distinctly characterizes the wide heterogeneity in pediatric mixed phenotype acute leukemia. Genome Medicine, Oct 2023. URL: https://doi.org/10.1186/s13073-023-01241-z, doi:10.1186/s13073-023-01241-z. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (peretz2024multiomicsinglecell pages 1-2): Cheryl A. C. Peretz, Vanessa E. Kennedy, Anushka Walia, Cyrille L. Delley, Andrew Koh, Elaine Tran, Iain C. Clark, Corey E. Hayford, Chris D’Amato, Yi Xue, Kristina M. Fontanez, Aaron A. May-Zhang, Trinity Smithers, Yigal Agam, Qian Wang, Hai-ping Dai, Ritu Roy, Aaron C. Logan, Alexander E. Perl, Adam Abate, Adam Olshen, and Catherine C. Smith. Multiomic single cell sequencing identifies stemlike nature of mixed phenotype acute leukemia. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52317-2, doi:10.1038/s41467-024-52317-2. This article has 24 citations and is from a highest quality peer-reviewed journal.

6. (weinberg2024howtothink pages 5-6): Olga K. Weinberg. How to think about acute leukemia of ambiguous lineage. Hematology, 2024:287-292, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000554, doi:10.1182/hematology.2024000554. This article has 16 citations and is from a peer-reviewed journal.

7. (oberley2020significanceofminimal pages 2-3): Matthew J. Oberley, Sunil S. Raikar, Gerald B. Wertheim, Jemily Malvar, Richard Sposto, Karen R. Rabin, Jyotinder N. Punia, Alix E. Seif, Viviane C. Cahen, Reuven J. Schore, Dragos C. Luca, Terri Guinipero, William G. Woods, Maurice R. G. O’Gorman, and Etan Orgel. Significance of minimal residual disease in pediatric mixed phenotype acute leukemia: a multi-center cohort study. Leukemia, 34:1741-1750, Feb 2020. URL: https://doi.org/10.1038/s41375-020-0741-0, doi:10.1038/s41375-020-0741-0. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (sherban2025acuteleukemiaof pages 9-12): Adi Sherban and Ofir Wolach. Acute leukemia of ambiguous lineage: the known and the uncertain. Haematologica, 111:813-827, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287793, doi:10.3324/haematol.2025.287793. This article has 3 citations.

9. (sherban2025acuteleukemiaof pages 6-9): Adi Sherban and Ofir Wolach. Acute leukemia of ambiguous lineage: the known and the uncertain. Haematologica, 111:813-827, Oct 2025. URL: https://doi.org/10.3324/haematol.2025.287793, doi:10.3324/haematol.2025.287793. This article has 3 citations.

10. (orgel2020mixed‐phenotypeacuteleukemia pages 1-2): Etan Orgel, Thomas B. Alexander, Brent L. Wood, Samir B. Kahwash, Meenakshi Devidas, Yunfeng Dai, Todd A. Alonzo, Charles G. Mullighan, Hiroto Inaba, Stephen P. Hunger, Elizabeth A. Raetz, Alan S. Gamis, Karen R. Rabin, Andrew J. Carroll, Nyla A. Heerema, Jason N. Berman, William G. Woods, Mignon L. Loh, Patrick A. Zweidler‐McKay, and John T. Horan. Mixed‐phenotype acute leukemia: a cohort and consensus research strategy from the children’s oncology group acute leukemia of ambiguous lineage task force. Cancer, 126:593-601, Oct 2020. URL: https://doi.org/10.1002/cncr.32552, doi:10.1002/cncr.32552. This article has 79 citations and is from a domain leading peer-reviewed journal.

11. (oberley2020significanceofminimal pages 1-2): Matthew J. Oberley, Sunil S. Raikar, Gerald B. Wertheim, Jemily Malvar, Richard Sposto, Karen R. Rabin, Jyotinder N. Punia, Alix E. Seif, Viviane C. Cahen, Reuven J. Schore, Dragos C. Luca, Terri Guinipero, William G. Woods, Maurice R. G. O’Gorman, and Etan Orgel. Significance of minimal residual disease in pediatric mixed phenotype acute leukemia: a multi-center cohort study. Leukemia, 34:1741-1750, Feb 2020. URL: https://doi.org/10.1038/s41375-020-0741-0, doi:10.1038/s41375-020-0741-0. This article has 28 citations and is from a highest quality peer-reviewed journal.

12. (NCT07222579 chunk 3): Ashkan Emadi, MD PHD. Subcutaneous Blinatumomab for Treatment of Adult Patients With CD19-Positive Mixed Phenotype Acute Leukemia (MPAL). West Virginia University. 2026. ClinicalTrials.gov Identifier: NCT07222579

13. (NCT07517510 chunk 1): Qing Zhang. HVA in the Treatment of Mixed-Phenotype Acute Leukemia(MPAL).. Guangdong Second Provincial General Hospital. 2026. ClinicalTrials.gov Identifier: NCT07517510

14. (NCT07573670 chunk 2): Chen Suning. A Phase 2 Study of Bcl-2 Inhibitor Combined With Azacitidine for Newly Diagnosed Mixed Phenotype Acute Leukemia. The First Affiliated Hospital of Soochow University. 2026. ClinicalTrials.gov Identifier: NCT07573670

15. (dickerson2022znf384fusiononcoproteins pages 15-15): Kirsten M. Dickerson, Chunxu Qu, Qingsong Gao, Ilaria Iacobucci, Zhaohui Gu, Hiroki Yoshihara, Emily A. Backhaus, Yunchao Chang, Laura J. Janke, Beisi Xu, Gang Wu, Evangelia K. Papachristou, Clive S. D'Santos, Kathryn G. Roberts, and Charles G. Mullighan. Znf384 fusion oncoproteins drive lineage aberrancy in acute leukemia. Blood cancer discovery, 3:240-263, Mar 2022. URL: https://doi.org/10.1158/2643-3230.bcd-21-0163, doi:10.1158/2643-3230.bcd-21-0163. This article has 46 citations and is from a peer-reviewed journal.

16. (OpenTargets Search: mixed phenotype acute leukemia): Open Targets Query (mixed phenotype acute leukemia, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

17. (martin‐guerrero2019non‐leukemicpediatricmixed pages 1-4): Idoia Martin‐Guerrero, Itziar Salaverria, Birgit Burkhardt, Catherine Chassagne‐Clement, Monika Szczepanowski, Susanne Bens, Wolfram Klapper, Martin Zimmermann, Edita Kabickova, Yves Bertrand, Alfred Reiter, Reiner Siebert, and Ilske Oschlies. Non‐leukemic pediatric mixed phenotype acute leukemia/lymphoma: genomic characterization and clinical outcome in a prospective trial for pediatric lymphoblastic lymphoma. Genes, Chromosomes and Cancer, 58(6):365-372, Jan 2019. URL: https://doi.org/10.1002/gcc.22726, doi:10.1002/gcc.22726. This article has 10 citations.

18. (martin‐guerrero2019non‐leukemicpediatricmixed pages 16-17): Idoia Martin‐Guerrero, Itziar Salaverria, Birgit Burkhardt, Catherine Chassagne‐Clement, Monika Szczepanowski, Susanne Bens, Wolfram Klapper, Martin Zimmermann, Edita Kabickova, Yves Bertrand, Alfred Reiter, Reiner Siebert, and Ilske Oschlies. Non‐leukemic pediatric mixed phenotype acute leukemia/lymphoma: genomic characterization and clinical outcome in a prospective trial for pediatric lymphoblastic lymphoma. Genes, Chromosomes and Cancer, 58(6):365-372, Jan 2019. URL: https://doi.org/10.1002/gcc.22726, doi:10.1002/gcc.22726. This article has 10 citations.

19. (mumme2023singlecellrnasequencing pages 4-5): Hope L. Mumme, Sunil S. Raikar, Swati S. Bhasin, Beena E. Thomas, Taylor Lawrence, Elizabeth P. Weinzierl, Yakun Pang, Deborah DeRyckere, Chuck Gawad, Daniel S. Wechsler, Christopher C. Porter, Sharon M. Castellino, Douglas K. Graham, and Manoj Bhasin. Single-cell rna sequencing distinctly characterizes the wide heterogeneity in pediatric mixed phenotype acute leukemia. Genome Medicine, Oct 2023. URL: https://doi.org/10.1186/s13073-023-01241-z, doi:10.1186/s13073-023-01241-z. This article has 20 citations and is from a highest quality peer-reviewed journal.

20. (NCT02135874 chunk 2):  Clofarabine, Idarubicin, Cytarabine, Vincristine Sulfate, and Dexamethasone in Treating Patients With Newly Diagnosed or Relapsed Mixed Phenotype Acute Leukemia. M.D. Anderson Cancer Center. 2014. ClinicalTrials.gov Identifier: NCT02135874

## Artifacts

- [Edison artifact artifact-00](Mixed_Phenotype_Acute_Leukemia-deep-research-falcon_artifacts/artifact-00.md)