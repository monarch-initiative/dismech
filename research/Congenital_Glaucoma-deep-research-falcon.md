---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:14:52.915477'
end_time: '2026-08-20T07:24:01.437194'
duration_seconds: 548.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Glaucoma
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Glaucoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Glaucoma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Glaucoma** covering all of the
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
- **Disease Name:** Congenital Glaucoma
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Glaucoma** covering all of the
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


# Congenital Glaucoma: Comprehensive Disease-Characteristics Report

## Scope and evidence conventions

“Congenital glaucoma” is sometimes used broadly for glaucoma recognized at or shortly after birth. This report focuses on **primary congenital glaucoma (PCG)**—the Mendelian, nonsyndromic developmental glaucoma that usually manifests by age 3—and distinguishes it from secondary childhood glaucoma caused by anterior-segment anomalies, systemic syndromes, acquired disease, or cataract surgery. Evidence is aggregated at disease/cohort level; it is **not derived from an individual EHR**. Mechanistic evidence is labeled as human, animal, or in vitro where appropriate.

The compact curation summary below complements the narrative report.

| Domain | Compact summary | Ontology / terminology suggestions | Evidence type | Caveats | Citations |
|---|---|---|---|---|---|
| Definition / onset | Primary congenital glaucoma (PCG) is the main primary childhood glaucoma subtype, usually presenting from birth to age 3 years, often within the first 6 months, due to developmental aqueous outflow abnormality causing elevated intraocular pressure (IOP), globe enlargement, and optic neuropathy. | MONDO:0018110; HPO onset suggestions: HP:0003577 Congenital onset, HP:0011463 Childhood onset | Disease review; genomics review; clinical perspective | Some sources discuss “childhood glaucoma” broadly; confirm whether a database entry should be restricted to isolated PCG versus broader primary childhood glaucoma. | (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 1-2, mandal2023approachtoprimary pages 2-3) |
| Key identifiers | Suggested disease-level identifiers: MONDO:0018110; OMIM phenotype 231300 / GLC3A; ORPHA:98976; ICD-10 Q15.0; MeSH D005901. These are ontology metadata rather than patient-derived observations. | OMIM/Orphanet/ICD/MeSH/MONDO metadata | Curated ontology metadata | Verify against current ontology releases before KB ingestion; not all were evidenced in retrieved papers. | (coviltir2025primarycongenitaland pages 2-4) |
| Epidemiology | Reported incidence/prevalence varies widely by ancestry and consanguinity: ~1 in 10,000–68,000 in Western countries; ~1:2500 in Saudi Arabia; ~1:8200 in Palestinian Arabs; ~1:1250 in Slovakian Gypsies. PCG contributes substantially to childhood blindness (about 5–18% globally; 4.2% cited in India). Bilateral disease occurs in ~70%, often asymmetrically. | HPO pattern suggestions: HP:0012837 Bilateral, HP:0012838 Unilateral, HP:0000628 Increased intraocular pressure | Epidemiology review; clinical review | Rates differ because of case definition, registry coverage, and referral bias. | (coviltir2025primarycongenitaland pages 2-4, pan2024exploringthegenetic pages 1-2, mandal2023approachtoprimary pages 2-3, coviltir2025primarycongenitaland pages 1-2) |
| Principal genes / inheritance | Major PCG genes include CYP1B1 and LTBP2 (typically autosomal recessive), TEK and ANGPT1 (autosomal dominant), and FOXC1 in some developmental/anterior-segment cases; CYP1B1 is the most frequently implicated gene overall and shows marked population-specific prevalence. SVEP1 has evidence as a modifier of TEK-related disease. | Gene symbols: CYP1B1, LTBP2, TEK, ANGPT1, FOXC1, SVEP1; inheritance: AR, AD | Human genetics review; human cohort genomics; model-supported modifier evidence | Genetic architecture is heterogeneous; many cohorts remain unsolved and inheritance can appear complex/digenic in some families. | (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 11-12, pan2024exploringthegenetic pages 14-15) |
| Hallmark phenotypes | Classic presentation includes epiphora, photophobia, blepharospasm, corneal edema/haze, enlarged corneal diameter, Haab striae, buphthalmos, myopic shift, elevated IOP, optic disc cupping/asymmetry, and later visual field/vision loss. | HPO suggestions: HP:0000627 Epiphora, HP:0000613 Photophobia, HP:0000652 Blepharospasm, HP:0007957 Corneal edema, HP:0001083 Buphthalmos, HP:0000518 Cataract not core/if present assess secondary causes, HP:0000540 Hypermetropia not typical, HP:0000602 Ophthalmoplegia not typical, HP:0000598 Abnormality of the optic disc, HP:0007686 Increased cup-to-disc ratio, HP:0000541 Myopia, HP:0007906 Haab striae | Clinical review; disease review | Frequency of each sign varies with age at detection and severity; phenotype overlap with secondary childhood glaucoma is common. | (coviltir2025primarycongenitaland pages 2-4, mandal2023approachtoprimary pages 2-3, coviltir2025primarycongenitaland pages 1-2) |
| Mechanism / anatomy | Core mechanism is developmental malformation of aqueous outflow pathways, especially trabecular meshwork and Schlemm canal. CYP1B1 dysfunction is linked to oxidative-stress and extracellular-matrix dysregulation in trabecular meshwork development; TEK/ANGPT1 signaling is crucial for Schlemm canal endothelial development; LTBP2 implicates extracellular matrix / TGF-β-associated structures; downstream consequence is elevated IOP with retinal ganglion cell injury and optic neuropathy. | GO suggestions: GO:0003151 outflow tract morphogenesis (approximate developmental analog; verify), GO:0030198 extracellular matrix organization, GO:0006979 response to oxidative stress, GO:0001525 angiogenesis, GO:0070934 CRYAB? verify before use, GO:0042060 wound healing not core; CL suggestions: trabecular meshwork cell, endothelial cell of Schlemm canal, retinal ganglion cell, neural crest-derived periocular mesenchymal cell; UBERON suggestions: UBERON:0001769 trabecular meshwork, UBERON:0010414 Schlemm canal, UBERON:0000924 cornea, UBERON:0000966 retina, UBERON:0001780 optic nerve | Human genetics review; mouse/zebrafish/cellular evidence | Several GO/CL/UBERON terms should be checked in the target ontology for exact preferred labels/IDs; zebrafish CYP1B1 models do not fully recapitulate human glaucoma. | (pan2024exploringthegenetic pages 14-15, pan2024exploringthegenetic pages 7-9, gomez2020establishingzebrafishdanio pages 46-51, vasiliou2008roleofcyp1b1 pages 1-2, pan2024exploringthegenetic pages 2-4) |
| Diagnosis | Diagnosis is clinical and often requires examination under anesthesia (EUA). Common criteria require childhood onset plus at least two features such as IOP >21 mmHg, glaucomatous optic nerve changes, corneal enlargement/Haab striae/edema, progressive myopia, or visual field defects. Gonioscopy is important; differential diagnosis includes megalocornea, keratoglobus, Peters anomaly, sclerocornea, and optic nerve hypoplasia. | HPO diagnostic features as above; NCIT-style test concepts: tonometry, gonioscopy, fundoscopy, axial length measurement, corneal diameter measurement | Clinical review; clinical perspective | Pediatric examination is difficult and often anesthesia-dependent; criteria differ somewhat across sources/CGRN adaptations. | (coviltir2025primarycongenitaland pages 2-4, mandal2023approachtoprimary pages 2-3, coviltir2025primarycongenitaland pages 1-2) |
| Genetic testing | Gene panels, WES, and WGS can establish a molecular diagnosis, support counseling, and occasionally refine prognosis. In the Genomics England childhood glaucoma cohort, expanded analysis raised solved families to 26%; CYP1B1 accounted for 55% of solved families and novel TEK and FOXC1 variants/CNVs were identified. | Testing concepts: targeted glaucoma panel, WES, WGS, CNV analysis | Human cohort genomics; systematic review | Diagnostic yield remains incomplete; non-coding variants, CNVs, and panel limitations can reduce sensitivity. | (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 11-12) |
| Treatment algorithm | Surgery is the cornerstone. Initial treatment is usually angle surgery: goniotomy or trabeculotomy; combined trabeculotomy-trabeculectomy is often favored in severe edematous/megalocornea presentations in some regions. Refractory cases may need trabeculectomy with antifibrotics or glaucoma drainage devices; cyclodestructive procedures are generally reserved for poor-visual-potential/advanced cases. Medical therapy is supportive/temporary rather than definitive. | NCIT suggestions: Goniotomy, Trabeculotomy, Trabeculectomy, Glaucoma Drainage Device Implantation, Cyclophotocoagulation, Mitomycin C therapy | Clinical perspective; review; interventional trial registry | Surgical choice varies by corneal clarity, age, severity, and regional practice; high-quality randomized evidence remains limited. | (coviltir2025primarycongenitaland pages 2-4, mandal2023approachtoprimary pages 2-3, NCT04116450 chunk 1, NCT03541551 chunk 1, NCT04683289 chunk 1, NCT06189326 chunk 1) |
| Prognosis / outcomes | With timely treatment, prognosis can be favorable: stationary disease reported in 90.3% at 1 year, 70.8% at 10 years, and 58.3% at 34 years; median better-eye visual acuity reported as 20/30. Earlier presentation/intervention tends to improve angle-surgery success. Quality of life is reduced overall but tracks with visual acuity. | Outcome concepts: vision preservation, amblyopia prevention, low-vision rehabilitation | Review synthesis | Long-term results depend on age at diagnosis, corneal disease, surgical control, amblyopia management, and follow-up adherence. | (coviltir2025primarycongenitaland pages 1-2, coviltir2025primarycongenitaland pages 10-11) |
| Prevention / counseling | No general primary prevention is established for sporadic cases, but in high-risk/consanguineous families, genetic counseling, cascade testing, reproductive counseling, and early ophthalmic screening of relatives/newborns can reduce diagnostic delay and support family planning. Secondary prevention centers on rapid recognition of epiphora/photophobia/blepharospasm and urgent referral. | Counseling concepts: genetic counseling, carrier testing, cascade screening, prenatal/preimplantation options where locally available | Public-health review; genetics review; clinical perspective | Evidence is stronger for counseling/early detection than for population-wide screening programs. | (alsaei2024increasingthediagnostic pages 1-2, mandal2023approachtoprimary pages 2-3) |
| Recent developments (2023–2024) | Notable recent advances include broader childhood-glaucoma genetic syntheses (2024), improved genome-analysis pipelines revealing missed TEK/FOXC1/CNV diagnoses (2024), and exploratory AI/deep-learning image models for pediatric glaucoma detection with reported sensitivity 0.85 and specificity 0.94. Multiple ongoing/recent PCG surgical trials compare trabeculotomy variants, adjunctive Ologen, and deep sclerectomy. | Methods terms: AI-assisted screening, WGS reanalysis, CNV detection | Recent reviews, genomics study, clinical trials | AI performance requires external validation; many trials are single-center and procedure-specific. | (alsaei2024increasingthediagnostic pages 1-2, coviltir2025primarycongenitaland pages 1-2, NCT03541551 chunk 1, NCT04683289 chunk 1, NCT06189326 chunk 1) |
| Models / comparative biology | Mouse models support CYP1B1-related trabecular meshwork defects and TEK/ANGPT1-dependent Schlemm canal development with IOP elevation and retinal ganglion cell loss. Zebrafish cyp1b1 knockout shows craniofacial/ECM phenotypes and incomplete penetrance but does not fully reproduce human glaucoma, highlighting species differences. | Model systems: mouse knockout/conditional models, zebrafish CRISPR knockout, endothelial cell assays | Model organism and in vitro evidence | Model validity is pathway-specific rather than full-phenotype complete. | (pan2024exploringthegenetic pages 14-15, pan2024exploringthegenetic pages 7-9, gomez2020establishingzebrafishdanio pages 46-51, vasiliou2008roleofcyp1b1 pages 1-2) |


*Table: This table condenses the highest-yield disease characteristics for primary congenital glaucoma, including identifiers, genetics, mechanism, diagnosis, management, and models. It is designed as a compact curation aid and flags where ontology metadata or mechanistic interpretations should be verified before database ingestion.*

## 1. Disease information

### Definition and classification

PCG is a severe developmental optic neuropathy caused by malformed aqueous-humor outflow structures. Impaired drainage raises intraocular pressure (IOP), stretching the compliant infant eye and producing corneal enlargement, buphthalmos, and ultimately retinal ganglion-cell/optic-nerve injury. PCG is defined clinically by onset in early childhood—typically birth to age 3—without another ocular or systemic disorder sufficient to explain the glaucoma. Most children present within the first 6 months. The Childhood Glaucoma Research Network classifies PCG under primary childhood glaucoma, separate from juvenile open-angle glaucoma and secondary childhood glaucomas. (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 1-2, mandal2023approachtoprimary pages 2-3)

### Identifiers and synonyms

Suggested current metadata are **MONDO:0018110**, **OMIM 231300/GLC3A**, **ORPHA:98976**, **ICD-10-CM Q15.0**, and **MeSH D005901**. These identifiers should be checked against the release used by the target knowledge base because terminology mappings change and the retrieved primary papers did not independently establish every identifier. Common names are *primary congenital glaucoma*, *congenital glaucoma*, *infantile glaucoma*, *trabeculodysgenesis-associated glaucoma*, and historically *hydrophthalmos/buphthalmos*. “Buphthalmos” properly describes the enlarged globe, not the entire disease.

## 2. Etiology, risk, and protective factors

### Causal factors

PCG is primarily genetic and developmental. The strongest genes are **CYP1B1** and **LTBP2** (usually autosomal recessive) and **TEK** and **ANGPT1** (usually autosomal dominant). **FOXC1** can produce developmental glaucoma or an overlapping anterior-segment dysgenesis phenotype. CYP1B1 is the predominant known cause, but its contribution varies markedly by ancestry: a 2024 systematic review found reported CYP1B1 prevalence of approximately **5–86%** across PCG populations. In the 100,000 Genomes childhood-glaucoma cohort, CYP1B1 accounted for **55% of molecularly solved families**. (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 11-12)

### Genetic risk and modifiers

Consanguinity and an affected sibling or parent are major risk indicators. Only about **10–40%** of PCG is reported as familial, however, so absence of family history does not exclude a Mendelian cause. TEK disease shows incomplete penetrance and variable expressivity; **SVEP1** has experimental and familial evidence as a modifier of TEK expression and disease severity. Possible digenic/modifier relationships involving CYP1B1 with MYOC or TEK have been proposed but are not established as routine diagnostic models. (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 11-12, pan2024exploringthegenetic pages 14-15)

Pathogenic alleles include missense, nonsense, frameshift, splice, deletion/CNV, and other loss-of-function variants. The relevant origin is **germline**, not somatic. Truly pathogenic recessive alleles are generally rare in population databases; no universal carrier frequency is appropriate because founder alleles and consanguinity create strong population differences. Variant-specific gnomAD frequency and ClinVar/ACMG classification should therefore be stored rather than a single disease-wide frequency.

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, diet, smoking behavior, or occupational exposure is accepted as a primary cause of isolated PCG. Environmental epidemiology is sparse and does not support actionable lifestyle prevention. The main “protective” factors are not biologic alleles or exposures, but **early recognition, prompt IOP-lowering surgery, refractive correction, amblyopia treatment, and sustained follow-up**, which reduce preventable visual loss. Evidence for clinically meaningful gene–environment interaction or protective variants remains insufficient.

## 3. Phenotypes

The characteristic symptom triad is **epiphora, photophobia, and blepharospasm**. Signs include corneal edema/haze, enlarged corneal diameter, horizontal Descemet-membrane breaks (Haab striae), buphthalmos, elevated IOP, progressive axial elongation/myopia, optic-disc cupping, rim loss, and later visual-field or visual-acuity loss. PCG is bilateral in approximately **70%**, but severity is often asymmetric. (mandal2023approachtoprimary pages 2-3)

Suggested phenotype terms include epiphora (**HP:0000627**), photophobia (**HP:0000613**), blepharospasm (**HP:0000652**), corneal edema (**HP:0007957**), buphthalmos (**HP:0001083**), myopia (**HP:0000541**), increased IOP (**HP:0000628**), abnormal optic disc (**HP:0000598**), and increased cup-to-disc ratio (**HP:0007686**). Exact HPO identifiers and preferred labels should be validated before ingestion.

Severity is variable and progressive without treatment. Corneal enlargement is particularly useful in infants: normal horizontal diameter is about 10 mm at birth; concerning thresholds include **≥11 mm in a newborn, >12 mm before age 1, and >13 mm at any age**. Symptoms, repeated anesthesia, spectacles/contact lenses, amblyopia treatment, surgery, and fear of blindness affect both child and caregiver quality of life. Better visual acuity correlates with better quality of life, but validated PCG-specific patient-reported outcome data remain limited. (mandal2023approachtoprimary pages 2-3, coviltir2025primarycongenitaland pages 1-2)

## 4. Genetic and molecular information

* **CYP1B1:** cytochrome-P450 monooxygenase; principally biallelic loss of function. More than 200 variants have been reported. Missense changes may impair heme binding, folding, stability, or catalytic activity; truncating/splice alleles usually abolish function. Human genetic evidence is strong.
* **LTBP2:** biallelic loss-of-function alleles disrupt extracellular microfibrils and ciliary-zonule/outflow architecture; association with TGF-β-related extracellular-matrix biology is plausible, although LTBP2 does not simply function as a conventional latent-TGF-β carrier in every context. Human genetic and mouse evidence support causality.
* **TEK/TIE2 and ANGPT1:** heterozygous loss-of-function/haploinsufficiency impairs angiopoietin–TEK signaling required for Schlemm-canal endothelial development. Penetrance is incomplete and expressivity variable.
* **FOXC1:** heterozygous dosage or functional defects impair neural-crest/periocular-mesenchyme programs and anterior-segment formation. FOXC1 more often causes an anterior-segment dysgenesis spectrum, including Axenfeld–Rieger phenotypes, than strictly isolated PCG.
* **SVEP1:** candidate modifier of TEK-related penetrance/severity, not an independently validated common PCG gene. (pan2024exploringthegenetic pages 14-15, pan2024exploringthegenetic pages 7-9, gomez2020establishingzebrafishdanio pages 46-51)

A 2024 Japanese study found CYP1B1 variants in 9 of 29 childhood-glaucoma families, including novel p.A202T, p.D274E, p.Q340*, and p.V420G, and novel heterozygous FOXC1 variants p.Q23fs, p.Q70R, and p.E163*. The observations illustrate population specificity and the need for ACMG/AMP assessment rather than assuming pathogenicity from novelty alone.

No reproducible PCG-specific methylation, histone, repeat-expansion, mitochondrial, or somatic-mutation mechanism is established. Large FOXC1 CNVs can be causal, so copy-number analysis should not be omitted. In the 100,000 Genomes study, expanded analysis increased solved families from **17% to 26%**, identifying missed TEK variants and a pathogenic FOXC1 CNV; smaller panels and prioritization of coding SNVs/indels had missed structural, CNV, and noncoding candidates. (alsaei2024increasingthediagnostic pages 1-2)

## 5. Mechanism and pathophysiology

The principal causal chain is:

**developmental gene defect → trabecular-meshwork/Schlemm-canal dysgenesis → increased aqueous outflow resistance → elevated IOP → infant globe and corneal stretching → buphthalmos, Haab striae, edema, axial myopia → retinal ganglion-cell axonal injury and optic-nerve cupping → irreversible visual-field and acuity loss.**

CYP1B1 appears upstream in fetal trabecular-meshwork development, oxidative homeostasis, extracellular-matrix regulation, and metabolism of endogenous retinoids, steroids, arachidonate, and melatonin. Cyp1b1-deficient mice develop abnormal trabecular meshwork and Schlemm canal and greater susceptibility to pressure-induced axonopathy. (vasiliou2008roleofcyp1b1 pages 1-2, pan2024exploringthegenetic pages 2-4)

TEK is expressed by Schlemm-canal endothelium; ANGPT1 promotes TEK activation, endothelial survival, and vessel stability. Conditional Tek or angiopoietin deletion in mice causes canal loss, ocular hypertension, and rapid retinal ganglion-cell injury. One model reported IOP of **35.58 ±2.01 mmHg** after combined angiopoietin deletion versus **23.53 ±1.50 mmHg** with Angpt1 deletion alone. This is animal-model evidence, not a human clinical threshold. (pan2024exploringthegenetic pages 7-9)

Relevant suggested processes are extracellular-matrix organization (**GO:0030198**), response to oxidative stress (**GO:0006979**), endothelial development/angiogenesis (**GO:0001525**), neural-crest development, aqueous-humor outflow, and retinal ganglion-cell death. Relevant cells are trabecular-meshwork cells, Schlemm-canal endothelial cells, neural-crest-derived periocular mesenchyme, corneal endothelial cells, and retinal ganglion cells. Exact CL identifiers should be validated.

No validated clinical metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature currently diagnoses PCG. Zebrafish transcriptomics implicates extracellular matrix, adhesion, proliferation, lipid/retinoid metabolism, oxidation–reduction, and inflammation, but translation to human disease remains uncertain. (pan2024exploringthegenetic pages 14-15, gomez2020establishingzebrafishdanio pages 46-51)

## 6–7. Anatomy and localization

The primary organ is the **eye**, especially the iridocorneal angle, trabecular meshwork, Schlemm canal, cornea, sclera, anterior chamber, optic nerve head, retina, and retinal ganglion-cell axons. Suggested anatomy terms include trabecular meshwork (**UBERON:0001769**), cornea (**UBERON:0000964; verify release**), retina (**UBERON:0000966**), and optic nerve (**UBERON:0001780**). Subcellular dysfunction can involve CYP1B1-associated endoplasmic-reticulum/microsomal enzyme activity and nuclear FOXC1 transcriptional regulation. Disease is usually bilateral but asymmetric; no consistent right/left preference is known. There is ordinarily no direct extraocular organ involvement in isolated PCG.

## 8–9. Temporal development, inheritance, and population epidemiology

Onset is congenital or infantile, usually insidious and progressive. Untreated disease does not remit spontaneously. Early stages feature tearing, photophobia, corneal haze, and IOP elevation; intermediate disease produces globe enlargement, Haab striae, myopia, and optic cupping; advanced disease causes corneal scarring, profound optic neuropathy, amblyopia, and irreversible blindness.

Reported frequency varies from roughly **1 per 10,000–68,000** in Western populations to approximately **1:2,500 in Saudi Arabia, 1:8,200 in Palestinian Arabs, and 1:1,250 in Slovakian Roma**, largely reflecting founder effects and consanguinity. Males are slightly overrepresented in many sporadic cohorts, whereas familial cases may approach equal sex distribution. PCG contributes about **5–18% of childhood blindness** in published syntheses. (coviltir2025primarycongenitaland pages 2-4, mandal2023approachtoprimary pages 2-3, coviltir2025primarycongenitaland pages 1-2)

CYP1B1/LTBP2 disease implies a 25% recurrence risk for each pregnancy when both parents are confirmed carriers. TEK/ANGPT1/FOXC1 disease can imply a 50% transmission risk from a heterozygous parent, modified by incomplete penetrance and variable expressivity. Anticipation is not established. Germline mosaicism is theoretically possible but not a defining feature. Founder effects and consanguinity are important; carrier frequency must be calculated for the relevant population and variant.

## 10. Diagnostics

### Clinical evaluation

A complete examination—often under anesthesia—includes tonometry, horizontal corneal diameter, pachymetry where feasible, corneal inspection, gonioscopy, axial length/refraction, dilated optic-nerve examination, and serial photography or OCT when technically possible. An accepted CGRN-style diagnosis requires childhood glaucoma with at least two findings such as IOP >21 mmHg, optic-nerve cupping/asymmetry or rim thinning, progressive myopia/axial enlargement, corneal enlargement/edema/Haab striae, or reproducible visual-field loss. (coviltir2025primarycongenitaland pages 2-4, mandal2023approachtoprimary pages 2-3)

Differential diagnoses include isolated megalocornea, keratoglobus, birth-trauma Descemet tears, Peters anomaly, sclerocornea, congenital hereditary endothelial dystrophy, mucopolysaccharidosis, optic-nerve hypoplasia, retinoblastoma-associated glaucoma, steroid/uveitic glaucoma, and glaucoma associated with aniridia, Axenfeld–Rieger syndrome, Sturge–Weber syndrome, or congenital cataract surgery. (coviltir2025primarycongenitaland pages 1-2)

### Genetic testing

Recommended testing begins with a childhood-glaucoma/anterior-segment panel containing at least **CYP1B1, LTBP2, TEK, ANGPT1, and FOXC1**, with deletion/duplication analysis. Broader genes should be included when syndromic or anterior-segment findings are present. If negative, trio WES or preferably WGS with CNV, structural, splice, and noncoding analysis is reasonable. CMA is useful when developmental delay, congenital anomalies, or suspected chromosomal imbalance accompanies glaucoma. Karyotype/FISH are targeted tests, not routine first-line assays. Mitochondrial and repeat-expansion testing are not generally indicated. (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 11-12)

No biochemical blood test or liquid-biopsy biomarker confirms PCG. Cascade examination and variant testing are appropriate for relatives after a molecular diagnosis. Population newborn biochemical screening is not available.

## 11. Outcomes and prognosis

PCG does not materially shorten life expectancy; morbidity is visual. Reported stationary disease declined from **90.3% at 1 year to 70.8% at 10 years and 58.3% at 34 years**, demonstrating the need for lifelong surveillance. Median better-eye visual acuity of **20/30** has been reported in appropriately managed cohorts, but severe bilateral impairment remains possible. Angle-surgery success was approximately **90% for presentation at 2–12 months** versus **50% in later-onset cases** in one synthesis. Prognosis worsens with advanced corneal enlargement/scarring, severe initial optic neuropathy, delayed surgery, uncontrolled IOP, repeated operations, anisometropia/amblyopia, and poor follow-up. (coviltir2025primarycongenitaland pages 10-11)

## 12. Treatment and current implementation

Surgery is definitive first-line treatment. Clear corneas commonly permit **goniotomy**; **trabeculotomy**, including circumferential microcatheter/suture techniques, bypasses limited gonioscopic visibility. Severe edematous/megalocornea presentations in India and the Middle East are often treated with combined **trabeculotomy–trabeculectomy**, sometimes with mitomycin C. Refractory disease may require trabeculectomy, a glaucoma drainage device, or repeat angle surgery. Cyclophotocoagulation is usually reserved for advanced or poor-visual-potential eyes. (coviltir2025primarycongenitaland pages 2-4, mandal2023approachtoprimary pages 2-3)

Topical beta-blockers, carbonic-anhydrase inhibitors, prostaglandin analogues, and selected other agents are bridges to surgery or adjuncts afterward, not cures for dysgenesis. Drug choice requires pediatric systemic-safety attention. Optical correction, amblyopia therapy, corneal care, low-vision rehabilitation, educational support, and caregiver counseling are essential.

Real-world trials include completed microcatheter circumferential trabeculotomy (**NCT04116450**, 25 eyes), randomized circumferential suture trabeculotomy versus rigid-probe viscotrabeculotomy (**NCT04683289**, 51 participants), and Ologen-assisted versus unaugmented combined trabeculotomy–trabeculectomy (**NCT03541551**, 44 participants). Another 40-participant study compared nonpenetrating deep sclerectomy with combined trabeculotomy–trabeculectomy (**NCT06189326**). These studies use IOP control, medication burden, corneal diameter, axial length, cup-to-disc ratio, and complications as outcomes. (NCT04116450 chunk 1, NCT03541551 chunk 1, NCT04683289 chunk 1, NCT06189326 chunk 1)

No approved gene, cell, RNA, or genotype-directed pharmacologic therapy currently corrects PCG. Pharmacogenomic prescribing standards are unavailable.

Suggested NCIT intervention concepts are goniotomy, trabeculotomy, trabeculectomy, glaucoma drainage-device implantation, cyclophotocoagulation, mitomycin C, refraction correction, and low-vision rehabilitation; exact NCIT codes should be release-validated.

## 13. Prevention

There is no vaccine or lifestyle-based primary prevention. For known familial disease, genetic counseling should cover inheritance, penetrance, recurrence, carrier/cascade testing, and locally available prenatal or preimplantation genetic testing. At-risk newborns require early ophthalmic examination even if asymptomatic. Secondary prevention consists of caregiver/professional education about tearing, light sensitivity, eyelid squeezing, corneal haze, or an enlarging eye and urgent referral. Tertiary prevention comprises durable IOP control, amblyopia treatment, refractive correction, protection of the better eye, and lifelong monitoring.

## 14–15. Other species and models

Naturally occurring congenital glaucoma is reported in veterinary medicine, particularly in some dog breeds, but the retrieved evidence did not support reliable breed/VBO, variant, or incidence annotations; these should not be populated without an OMIA/veterinary-specific review. PCG is noninfectious and has no zoonotic transmission.

**Mouse models** provide the strongest mechanistic validation. Cyp1b1-null mice show trabecular-meshwork/Schlemm-canal abnormalities and oxidative-stress susceptibility; conditional Tek or Angpt deletion produces Schlemm-canal loss, ocular hypertension, buphthalmos, and retinal ganglion-cell injury. **Zebrafish cyp1b1 knockout** is useful for developmental and transcriptomic studies but does not faithfully reproduce glaucoma: adult craniofacial defects showed incomplete penetrance, and no glaucoma phenotype was observed. Thus it is a pathway model rather than a complete phenocopy. (pan2024exploringthegenetic pages 14-15, pan2024exploringthegenetic pages 7-9, gomez2020establishingzebrafishdanio pages 46-51, vasiliou2008roleofcyp1b1 pages 1-2)

## Recent 2023–2024 developments and expert assessment

The most consequential recent development is improved genome interpretation rather than a new therapy. The 2024 100,000 Genomes reanalysis showed that expanding gene lists and interrogating CNVs, structural variants, and noncoding regions increased diagnostic yield to **26%**, while a 2024 systematic review identified **53 genes** discussed across childhood-glaucoma literature and emphasized the absence of standardized testing guidelines. (alsaei2024increasingthediagnostic pages 1-2, pan2024exploringthegenetic pages 11-12)

Exploratory deep-learning analysis of gaze photographs achieved reported sensitivity **0.85** and specificity **0.94**, but external validation and evaluation across ancestries, ages, corneal opacity, and imaging devices are required before population screening. (coviltir2025primarycongenitaland pages 1-2)

The prevailing expert position is that **rapid clinical recognition and surgery remain more immediately vision-saving than molecular diagnosis**, while genomic testing adds value for etiologic classification, recurrence counseling, detecting syndromic disease, and future precision trials. Major research gaps are unsolved families, penetrance modifiers, validated functional assays for variants of uncertain significance, standardized patient-reported outcomes, prospective comparative surgery trials, and human single-cell/spatial characterization of the developing outflow tract.

## Selected recent sources and abstract-supported statements

* Al-Saei et al., *BMC Genomics*, May 2024, DOI: https://doi.org/10.1186/s12864-024-10353-8. Abstract: “This analysis effectively raises the total number of solved CG families in the GE100KGP to 26%.” (alsaei2024increasingthediagnostic pages 1-2)
* Pan and Iwata, *Children*, April 2024, DOI: https://doi.org/10.3390/children11040454. The review identifies CYP1B1, LTBP2, TEK, ANGPT1, and FOXC1 as central PCG genes and integrates relevant animal pathways. (pan2024exploringthegenetic pages 11-12, pan2024exploringthegenetic pages 7-9)
* Mandal et al., *Taiwan Journal of Ophthalmology*, October 2023, DOI: https://doi.org/10.4103/tjo.tjo-d-23-00104. Abstract: “Medical therapy only serves as a supportive role, and surgical intervention remains the principal therapeutic modality.” (mandal2023approachtoprimary pages 2-3)
* Kumar et al., *PLOS ONE*, February 2024, DOI: https://doi.org/10.1371/journal.pone.0298883. The systematic review screened 1,916 records, included 196 studies, and found that CYP1B1 prevalence varied by region and population. (pan2024exploringthegenetic pages 11-12)

PMIDs were not consistently present in the retrieved full-text metadata; DOI URLs are therefore supplied rather than risking incorrect PMID assignment.

References

1. (alsaei2024increasingthediagnostic pages 1-2): Omayma Al-Saei, Samantha Malka, Nicholas Owen, Elbay Aliyev, Fazulur Rehaman Vempalli, Paulina Ocieczek, Bashayer Al-Khathlan, Khalid Fakhro, and Mariya Moosajee. Increasing the diagnostic yield of childhood glaucoma cases recruited into the 100,000 genomes project. BMC Genomics, May 2024. URL: https://doi.org/10.1186/s12864-024-10353-8, doi:10.1186/s12864-024-10353-8. This article has 5 citations and is from a peer-reviewed journal.

2. (pan2024exploringthegenetic pages 1-2): Yang Pan and Takeshi Iwata. Exploring the genetic landscape of childhood glaucoma. Children, 11:454, Apr 2024. URL: https://doi.org/10.3390/children11040454, doi:10.3390/children11040454. This article has 18 citations.

3. (mandal2023approachtoprimary pages 2-3): Anil Kumar Mandal, Debasis Chakrabarti, and Vijaya K. Gothwal. Approach to primary congenital glaucoma: a perspective. Oct 2023. URL: https://doi.org/10.4103/tjo.tjo-d-23-00104, doi:10.4103/tjo.tjo-d-23-00104. This article has 22 citations.

4. (coviltir2025primarycongenitaland pages 2-4): Valeria Coviltir, Maria Cristina Marinescu, Bianca Maria Urse, and Miruna Gabriela Burcel. Primary congenital and childhood glaucoma—a complex clinical picture and surgical management. Diagnostics, 15:308, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030308, doi:10.3390/diagnostics15030308. This article has 13 citations.

5. (coviltir2025primarycongenitaland pages 1-2): Valeria Coviltir, Maria Cristina Marinescu, Bianca Maria Urse, and Miruna Gabriela Burcel. Primary congenital and childhood glaucoma—a complex clinical picture and surgical management. Diagnostics, 15:308, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030308, doi:10.3390/diagnostics15030308. This article has 13 citations.

6. (pan2024exploringthegenetic pages 11-12): Yang Pan and Takeshi Iwata. Exploring the genetic landscape of childhood glaucoma. Children, 11:454, Apr 2024. URL: https://doi.org/10.3390/children11040454, doi:10.3390/children11040454. This article has 18 citations.

7. (pan2024exploringthegenetic pages 14-15): Yang Pan and Takeshi Iwata. Exploring the genetic landscape of childhood glaucoma. Children, 11:454, Apr 2024. URL: https://doi.org/10.3390/children11040454, doi:10.3390/children11040454. This article has 18 citations.

8. (pan2024exploringthegenetic pages 7-9): Yang Pan and Takeshi Iwata. Exploring the genetic landscape of childhood glaucoma. Children, 11:454, Apr 2024. URL: https://doi.org/10.3390/children11040454, doi:10.3390/children11040454. This article has 18 citations.

9. (gomez2020establishingzebrafishdanio pages 46-51): Jurgienne Arizza Gomez Umali. Establishing zebrafish, danio rerio, as a genetic model for glaucoma. Text, 2020. URL: https://doi.org/10.48336/k82g-gr50, doi:10.48336/k82g-gr50. This article has 0 citations and is from a peer-reviewed journal.

10. (vasiliou2008roleofcyp1b1 pages 1-2): Vasilis Vasiliou and Frank J. Gonzalez. Role of cyp1b1 in glaucoma. Annual Review of Pharmacology and Toxicology, 48:333-358, Feb 2008. URL: https://doi.org/10.1146/annurev.pharmtox.48.061807.154729, doi:10.1146/annurev.pharmtox.48.061807.154729. This article has 268 citations and is from a highest quality peer-reviewed journal.

11. (pan2024exploringthegenetic pages 2-4): Yang Pan and Takeshi Iwata. Exploring the genetic landscape of childhood glaucoma. Children, 11:454, Apr 2024. URL: https://doi.org/10.3390/children11040454, doi:10.3390/children11040454. This article has 18 citations.

12. (NCT04116450 chunk 1): Shaaban Elwan. MicrocatheterTrabeculotomy in Primary Congenital Glaucoma. Minia University. 2017. ClinicalTrials.gov Identifier: NCT04116450

13. (NCT03541551 chunk 1): HERF. Ologen® Collagen Matrix in Patients With Primary Congenital Glaucoma Undergoing Trabeculectomy. L.V. Prasad Eye Institute. 2018. ClinicalTrials.gov Identifier: NCT03541551

14. (NCT04683289 chunk 1):  Visco-Circumferential-Suture-Trabeculotomy Versus Trabeculotomy. Mansoura University. 2015. ClinicalTrials.gov Identifier: NCT04683289

15. (NCT06189326 chunk 1): Ehab Tharwat. Non-penetrating Deep Sclerectomy Versus Trabeculotomy- Trabeculectomy Operation in Treatment of Primary Congenital Glaucoma. Al-Azhar University. 2022. ClinicalTrials.gov Identifier: NCT06189326

16. (coviltir2025primarycongenitaland pages 10-11): Valeria Coviltir, Maria Cristina Marinescu, Bianca Maria Urse, and Miruna Gabriela Burcel. Primary congenital and childhood glaucoma—a complex clinical picture and surgical management. Diagnostics, 15:308, Jan 2025. URL: https://doi.org/10.3390/diagnostics15030308, doi:10.3390/diagnostics15030308. This article has 13 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Glaucoma-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.