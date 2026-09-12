---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T09:04:13.319334'
end_time: '2026-08-17T09:14:00.381835'
duration_seconds: 587.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Secondary Erythromelalgia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Secondary_Erythromelalgia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Secondary Erythromelalgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Secondary Erythromelalgia** covering all of the
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
- **Disease Name:** Secondary Erythromelalgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Secondary Erythromelalgia** covering all of the
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


# Secondary Erythromelalgia: Disease-Characteristics Research Report

## Executive summary and evidence caveat

Secondary erythromelalgia (secondary EM) is an **acquired, etiologically heterogeneous neurovascular pain syndrome** characterized by recurrent or persistent **burning pain, erythema, and increased skin temperature**, usually in the feet or hands. Heat, exercise, dependency of the limb, prolonged standing, and tight footwear provoke attacks; cooling and elevation typically relieve them. Unlike inherited primary erythromelalgia, secondary EM is not itself an established monogenic channelopathy. It usually appears later in life in association with a myeloproliferative neoplasm (MPN), small-fiber or autonomic neuropathy, autoimmune/connective-tissue disease, metabolic disease, medication, infection, malignancy, toxin, or tissue injury. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 1-2)

The major evidence limitation is that most cohorts and therapeutic studies combine primary, idiopathic, and secondary EM. Consequently, many frequency and response estimates below describe **EM overall**, not secondary EM specifically. Secondary-disease evidence is strongest for the association between platelet-mediated MPNs and aspirin-responsive EM; most other associations and treatments rely on small observational studies, case series, or expert reviews. (skeik2019erythromelalgia pages 1-2, algarni2025comparativeefficacyand pages 4-5, algarni2025comparativeefficacyand pages 1-2)

| Domain | Key finding | Evidence type/strength | Knowledge-base annotation |
|---|---|---|---|
| Definition / phenotype | Secondary erythromelalgia is an acquired neurovascular pain syndrome defined by episodic or persistent burning pain, erythema, warmth, and sometimes swelling, usually in distal extremities; attacks are precipitated by heat, exercise, dependency, footwear, and relieved by cooling/elevation. Compared with inherited primary disease, secondary disease tends to present later and may be more variable, unilateral, or localized. Quantitative phenotype data usually pool primary and secondary cases. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 1-2, algarni2025comparativeefficacyand pages 4-5) | Expert review + systematic review; moderate for core phenotype, lower for subtype distinctions | HPO: Erythema, Burning pain, Increased skin temperature, Distal extremity pain, Edema; UBERON: foot, hand, lower limb; MONDO: secondary erythromelalgia if available/not confirmed |
| Major secondary causes | Reported associations include myeloproliferative neoplasms/disorders (especially essential thrombocythemia, polycythemia vera, myelodysplastic syndromes), neuropathies/small-fiber neuropathy, autoimmune/connective-tissue disease, diabetes/metabolic disease, neoplasia, infections/vaccination, and drugs/toxins such as cyclosporine, calcium-channel blockers, bromocriptine, mercury, burns/frostbite, and mushroom intoxication. Much of this evidence is case-based or mixed-etiology review evidence. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 1-2, algarni2025comparativeefficacyand pages 1-2, algarni2025comparativeefficacyand pages 4-5) | Review-level evidence with many case associations; heterogeneous/variable strength | Disease associations: MPN, SFN, autoimmune disease, diabetes mellitus, neoplasm, infection, drug-induced disease, toxic exposure |
| Mechanism / pathophysiology | Secondary erythromelalgia is mechanistically heterogeneous. In hematologic forms, platelet activation/microthrombotic or prostaglandin-thromboxane-related microvascular dysfunction is the classic model; in neuropathic forms, small-fiber/autonomic dysfunction and vasomotor dysregulation are implicated. Reviews also support abnormal autonomic testing, reduced nerve terminal density, increased skin blood flow/temperature, and tissue hypoxia/shunting concepts, but these mechanisms are often inferred from mixed erythromelalgia cohorts rather than secondary-only cohorts. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 1-2, skeik2019erythromelalgia pages 2-3) | Mixed human clinical + expert review; moderate for MPN/aspirin-responsive mechanism, lower for unified mechanism | GO: platelet activation, blood coagulation, regulation of vasodilation, sensory perception of pain, axon guidance/maintenance, autonomic nervous system process; CL: platelet, peripheral sensory neuron, sympathetic neuron, endothelial cell |
| Diagnostics | Diagnosis is primarily clinical: characteristic attacks of red-hot painful extremities triggered by warmth and relieved by cooling, plus exclusion of mimics and search for an underlying cause. Ancillary tests that may support or subtype disease include CBC/platelets and MPN evaluation, vascular studies (often normal large-vessel Doppler but increased skin temperature/laser Doppler and low TcPO2), autonomic testing, thermography, and skin biopsy for nerve fiber density or intraluminal thrombi. Differential diagnoses include peripheral neuropathy, CRPS, cellulitis/erysipelas, dermatitis, osteomyelitis, SLE, venous/arterial insufficiency, and gout. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3) | Clinical review evidence; moderate for workup principles, limited formal criteria | HPO/differential tags; labs: CBC, platelet count; procedures: skin biopsy, autonomic reflex screen, thermography, laser Doppler, transcutaneous oxygen pressure |
| Epidemiology | Secondary-specific epidemiology is poorly defined. Mixed erythromelalgia estimates cited in reviews include incidence of 1.3/100,000 in Olmsted County and 15/100,000 in New Zealand; reported presentation age ranges 5-90 years with mean around 55 years and female predominance in mixed/reviewed cohorts. An anatomic series cited in review found 88.1% foot involvement, 25.6% hands, 13.7% legs, 2.4% face. These statistics generally do not isolate secondary disease. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 1-2) | Mostly retrospective/review data; weak-to-moderate for secondary disease specifically | Epidemiology note: mixed EM data; Age of onset: adult/later onset enrichment in secondary EM; Sex: female predominance reported |
| Treatment | First-line management is cause-directed plus trigger avoidance and safe cooling. Aspirin is particularly relevant in myeloproliferative-associated secondary erythromelalgia and is a classic response marker in platelet-mediated disease. Other options reported across mixed cohorts include topical amitriptyline-ketamine, lidocaine, misoprostol, iloprost, antihistamines, venlafaxine/SNRI-class drugs, sodium-channel blockers, and procedural escalation (e.g., sympathectomy, neuromodulation) for refractory cases. Systematic-review data across mixed EM showed ~75% pain relief with topical amitriptyline-ketamine and GI toxicity with misoprostol; applicability to secondary EM is uncertain. (skeik2019erythromelalgia pages 1-2, skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 6-7, algarni2025comparativeefficacyand pages 7-9, algarni2025comparativeefficacyand pages 2-4) | Strongest for aspirin in MPN-associated disease from longstanding clinical experience/review; otherwise mostly small mixed studies | NCIT/CHEBI: Aspirin, Amitriptyline, Ketamine, Lidocaine, Misoprostol, Iloprost, Venlafaxine; care pathway: treat underlying cause + symptomatic pain management |
| Trials / recent developments | Recent interventional trials mostly target primary/inherited or idiopathic erythromelalgia, not secondary disease. Examples: EASE/ATX01 topical amitriptyline Phase 2 crossover completed 2024 (14 participants), but exclusion criteria removed patients with other extremity pain causes; burst spinal cord stimulation trial enrolls only primary/idiopathic disease; earlier XPF-001/XPF-002 and PF-05089771 trials were for primary/inherited disease. Thus, current trial evidence is not directly generalizable to secondary erythromelalgia. (NCT04039633 chunk 1, NCT05917912 chunk 1, NCT05917912 chunk 2, NCT01090622 chunk 1, NCT01486446 chunk 2, NCT01769274 chunk 3) | High confidence for exclusion/generalizability statement from trial records | ClinicalTrials: NCT05917912, NCT04039633, NCT01090622, NCT01486446, NCT01769274; intervention classes: topical analgesic, spinal cord stimulation, Nav1.7-targeted agents |
| Genetics / molecular | SCN9A and Nav1.7 are central to inherited primary erythromelalgia, not to secondary erythromelalgia. No established secondary-EM-specific germline causal gene, protective allele, modifier gene, epigenetic signature, or structural chromosomal abnormality was identified in the reviewed evidence. In secondary disease, molecular findings may instead derive from the underlying associated disorder (e.g., somatic driver mutations of myeloproliferative neoplasms), rather than erythromelalgia itself. (assaad2025severeerythromelalgiapain pages 6-8, algarni2025comparativeefficacyand pages 1-2) | High confidence for SCN9A-primary distinction; low evidence for secondary-EM-specific genetics because evidence is largely absent | HGNC/OMIM note: SCN9A relevant mainly to inherited primary EM; secondary EM genetics: none established at disease level |
| Models | Available experimental systems predominantly model inherited primary erythromelalgia, including iPSC-derived sensory neurons carrying SCN9A variants and Nav1.7-related preclinical pain models. These are useful for nociceptor hyperexcitability and analgesic discovery but do not faithfully model the heterogeneous acquired mechanisms of secondary erythromelalgia. No validated natural animal disease or dedicated acquired secondary-EM model was identified in the available evidence. (NCT01769274 chunk 3) | Indirect/model evidence; low for secondary disease relevance | Model annotation: human iPSC sensory neuron model for primary EM; secondary EM model status: none established |


*Table: This table summarizes evidence-grade findings for secondary erythromelalgia across clinical, mechanistic, diagnostic, epidemiologic, therapeutic, genetic, and model domains. It highlights where evidence is strong, where data are mixed with primary erythromelalgia, and where disease-specific gaps remain.*

## 1. Disease information

### Definition and classification

The name derives from Greek *erythros* (red), *melos* (limb), and *algos* (pain). Common names are **erythromelalgia**, **erythermalgia**, **erythralgia**, **Mitchell disease**, and, when acquired, **secondary erythromelalgia/secondary erythermalgia**. The syndrome’s defining clinical triad is red, hot, painful extremities. Swelling may accompany attacks. Secondary EM is best represented as a **disease-level syndrome**, aggregated from clinical literature and disease resources—not as an individual-patient/EHR datum unless a knowledge-base record explicitly links it to a patient. (skeik2019erythromelalgia pages 1-2, skeik2019erythromelalgia pages 2-3)

### Identifiers

- **ICD-10-CM:** I73.81, Erythromelalgia. This code does not reliably distinguish primary from secondary disease.
- **MeSH:** *Erythromelalgia*; a separate secondary-EM descriptor is generally not used.
- **MONDO:** A dedicated, independently curated secondary-EM MONDO identifier could not be confirmed from the retrieved evidence. Use the parent erythromelalgia concept plus a “secondary/acquired” qualifier and causal-disease relationship rather than assigning an unverified ID.
- **OMIM:** OMIM entries chiefly describe inherited primary erythromelalgia associated with **SCN9A**; these should not be used as identifiers for acquired secondary EM.
- **Orphanet/ICD-11:** Erythromelalgia concepts may be indexed, but a separate secondary-disease identifier was not verified in the available evidence.

## 2. Etiology, risks, protective factors, and gene–environment interaction

### Causal or associated factors

1. **Hematologic/MPN:** essential thrombocythemia, polycythemia vera, myelodysplastic syndromes, and related platelet disorders. These are the most clinically actionable secondary causes. Platelet activation, aggregation, and arteriolar microthrombosis are implicated.
2. **Neuropathic/metabolic:** small-fiber neuropathy, diabetic neuropathy/diabetes mellitus, and other peripheral or autonomic neuropathies.
3. **Autoimmune/connective-tissue:** systemic lupus erythematosus and other connective-tissue or inflammatory disorders.
4. **Neoplastic/paraneoplastic:** solid tumors, hematologic malignancy, and paraproteinemic states have been reported.
5. **Drug-associated:** calcium-channel blockers, bromocriptine, and cyclosporine are repeatedly listed; individual drug associations generally derive from case reports.
6. **Infectious or immune triggers:** HIV, infectious mononucleosis, and temporal associations with influenza or hepatitis-B vaccination have been reported, but causality is weak.
7. **Toxic/physical injury:** mercury exposure, mushroom intoxication, burns, and frostbite are reported associations. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 1-2, algarni2025comparativeefficacyand pages 4-5)

### Risk and protective factors

Older age and the presence of an underlying MPN, neuropathy, diabetes, autoimmune disease, malignancy, or an implicated medication increase clinical suspicion. Heat exposure, exercise, prolonged standing, limb dependency, emotional stress, and occlusive footwear are **attack triggers**, not necessarily causes of the underlying disease. Female predominance has been reported in mixed EM cohorts, but a secondary-specific sex ratio is unavailable. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 4-5)

No validated **genetic protective variant**, dietary factor, medication prophylaxis, or population-level environmental protective exposure has been established. Avoidance of heat and mechanical triggers reduces attacks but should be classified as symptom prevention rather than protection against disease onset.

### Gene–environment interaction

No reproducible secondary-EM-specific gene–environment interaction is established. Genetic or somatic drivers may belong to the underlying disorder—for example, MPN biology—while heat or dependency precipitates symptoms through altered microvascular and neural control. This differs fundamentally from inherited EM, in which a germline channel variant directly changes nociceptor excitability.

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| Burning distal-extremity pain | Cardinal subjective symptom; episodic or continuous; mild to incapacitating; attacks last minutes to days | Burning pain; Pain in extremities; Foot pain; Hand pain |
| Erythema | Cardinal visible sign; attack-related, localized, unilateral, asymmetric, or bilateral | Erythema |
| Increased skin temperature | Cardinal sign; worsened by warmth/exercise/dependency | Increased skin temperature |
| Swelling | Variable accompanying manifestation | Peripheral edema |
| Heat intolerance/heat-triggered attacks | Provocation phenotype | Heat intolerance |
| Dysesthesia, allodynia, hyperalgesia | Especially when small-fiber neuropathy is present | Dysesthesia; Allodynia; Hyperalgesia |
| Abnormal sweating/autonomic findings | Variable; supports small-fiber/autonomic involvement | Abnormality of the autonomic nervous system; Abnormal sweating |
| Ulceration, infection, ischemic injury | Usually secondary to severe disease or excessive cooling | Skin ulcer; Recurrent skin infections; Peripheral ischemia |

Secondary EM generally has **adult or late onset**, although onset across all EM forms ranges from childhood to old age. It may be unilateral or localized more often than inherited primary EM, and its course follows the causal disorder: episodic, fluctuating, progressive, or treatment-responsive. Reviews report ages of 5–90 years, with a mean around 55 years, but this is not a secondary-only estimate. (assaad2025severeerythromelalgiapain pages 6-8, algarni2025comparativeefficacyand pages 1-2)

In a 168-patient mixed EM series cited by a systematic review, involvement was reported in the feet in **88.1%**, hands in **25.6%**, legs in **13.7%**, and face in **2.4%**. Approximately 5% reported family history, further illustrating that most EM is not clearly familial, although these values do not isolate secondary cases. (algarni2025comparativeefficacyand pages 1-2)

### Quality of life

Severe attacks interfere with walking, standing, sleep, footwear, work, schooling, and social participation. Patients may resort to continuous cooling or water immersion, creating secondary wounds and infection. Disability, depression, and substantial pain interference are recognized, but validated secondary-EM-specific EQ-5D, SF-36, or PROMIS population norms are unavailable. Modern trials use EQ-5D-5L, Brief Pain Inventory, depression scores, physical activity, and disability measures, reflecting the syndrome’s multidimensional burden. (NCT04039633 chunk 1, NCT05917912 chunk 1)

## 4. Genetic and molecular information

### Distinction from primary erythromelalgia

**SCN9A** encodes the voltage-gated sodium channel NaV1.7. Germline gain-of-function variants cause inherited primary EM by lowering nociceptor firing thresholds. That mechanism should **not** be automatically attributed to secondary EM. Genetic testing is appropriate when onset is early, disease is familial, or the phenotype suggests a channelopathy; it is not a confirmatory test for acquired secondary EM. Reviews report SCN9A variants in 5–36% of selected EM cohorts, but those mixed and referral-enriched estimates do not establish genetic causation in secondary disease. (skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 6-7, algarni2025comparativeefficacyand pages 1-2)

No secondary-EM-specific germline causal gene, HGNC-listed modifier, protective allele, recurrent pathogenic copy-number change, chromosomal abnormality, or validated ACMG variant set is established. Therefore, secondary EM has no meaningful disease-level carrier frequency, penetrance, anticipation, founder effect, or consanguinity pattern.

Where secondary EM accompanies an MPN, somatic molecular findings such as an MPN driver belong to the **underlying neoplasm**, not to EM as an independent inherited disorder. Likewise, no reproducible secondary-EM-specific methylation, histone, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature was identified.

## 5. Environmental, lifestyle, and infectious information

Ambient heat, heated bedding, exercise, prolonged standing, limb dependency, physical activity, emotional stress, and tight shoes commonly precipitate symptoms. Cooling and elevation reduce them. These relationships represent thermoregulatory and hemodynamic provocation rather than traditional epidemiologic exposures. (skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 4-5)

Mercury toxicity, mushroom intoxication, burns, and frostbite are reported potential causes; calcium-channel blockers, bromocriptine, and cyclosporine are medication associations. HIV and infectious mononucleosis have been reported, while vaccine associations are low-level temporal evidence and should not be treated as established causality. Smoking, alcohol intake, diet, obesity, radiation, and occupational exposure have no validated secondary-EM-specific risk estimates in the retrieved literature. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 1-2)

## 6. Mechanism and pathophysiology

Secondary EM is probably a **final common phenotype** produced by several upstream mechanisms.

### A. Platelet–microvascular pathway

**Underlying MPN/platelet activation → platelet aggregation and prostanoid/thromboxane signaling → arteriolar inflammation or microthrombosis → maldistributed skin perfusion and tissue hypoxia → reactive hyperemia, warmth, erythema, and ischemic burning pain.** Clinical aspirin responsiveness supports this model, particularly in essential thrombocythemia or polycythemia vera. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3)

Suggested annotations:
- **GO biological processes:** platelet activation; platelet aggregation; blood coagulation; regulation of vasodilation; inflammatory response; response to hypoxia.
- **Cell Ontology:** platelet; endothelial cell; vascular smooth-muscle cell.
- **Anatomical:** cutaneous arteriole; dermal microvasculature.

### B. Neuropathic/autonomic pathway

**Diabetes, autoimmune neuropathy, toxic injury, or idiopathic small-fiber damage → dysfunction/loss of nociceptive and autonomic fibers → abnormal thermal pain signaling plus impaired sympathetic vasoconstriction and sweating → episodic vasodilation, heat, erythema, allodynia, and burning pain.** Reduced nerve-terminal density and abnormal autonomic reflex testing support this pathway, although studies often combine EM subtypes. (skeik2019erythromelalgia pages 1-2, skeik2019erythromelalgia pages 2-3)

Suggested annotations:
- **GO:** sensory perception of pain; detection of temperature stimulus; regulation of blood vessel diameter; autonomic nervous system process; axon maintenance.
- **CL:** peripheral sensory neuron; nociceptor; sympathetic neuron; Schwann cell; endothelial cell.

### C. Arteriovenous shunting and hypoxia

Thermoregulatory dyscontrol may open arteriovenous shunts while reducing nutritive capillary flow. This can produce the paradox of a visibly hyperemic, warm extremity with low transcutaneous oxygen tension and ischemic pain. Large-vessel Doppler studies may remain normal while skin temperature and laser-Doppler flow increase. (skeik2019erythromelalgia pages 2-3)

No single molecular pathway—MAPK, mTOR, PI3K–AKT, Wnt, or otherwise—has been validated as a unifying secondary-EM pathway. Mitochondrial, metabolic, and immune abnormalities should be annotated according to the underlying disease rather than inferred for all secondary EM.

## 7. Anatomical structures affected

- **Organ/system level:** skin and cutaneous circulation; peripheral and autonomic nervous systems; hematologic system when an MPN is causal.
- **Primary sites:** feet and toes most commonly, followed by hands/fingers and legs; face and ears are uncommon.
- **Tissues:** epidermis and dermis, cutaneous sensory/autonomic nerve fibers, arterioles, venules, capillaries, and arteriovenous anastomoses.
- **Cells:** nociceptors, sympathetic neurons, endothelial cells, vascular smooth-muscle cells, and—within MPN-associated disease—platelets.
- **Subcellular:** plasma membrane ion channels and synaptic/axonal compartments are relevant to neural excitability, but NaV1.7 dysfunction is proven mainly in inherited disease.
- **Localization/lateralization:** bilateral and symmetric disease is typical overall, but acquired disease may be unilateral, asymmetric, or localized. (algarni2025comparativeefficacyand pages 1-2)

Suggested UBERON concepts include skin of foot, foot, toe, hand, finger, lower limb, upper limb, dermis, epidermis, peripheral nerve, blood vessel, and cutaneous microvasculature.

## 8. Temporal development

Secondary EM usually begins after or around the onset of its associated disease and is commonly adult-onset. Presentation may be acute after a drug or injury, subacute with inflammatory disease, or insidious with MPN or neuropathy. Attacks last **minutes to days**, may increase during summer, and range from intermittent flares to continuous symptoms. No validated stage system exists. (skeik2019erythromelalgia pages 2-3)

Remission may follow withdrawal of an offending drug or successful treatment of the underlying disease. MPN-associated symptoms can respond rapidly to antiplatelet and cytoreductive treatment. Neuropathy-associated disease is often chronic and variably treatment-responsive. There is no established critical developmental window, although early recognition is important to prevent cooling injury and to detect an occult hematologic disorder.

## 9. Inheritance, epidemiology, and population

Secondary EM is **acquired/non-Mendelian**. Inheritance, penetrance, carrier frequency, anticipation, germline mosaicism, and prenatal recurrence risk are not applicable unless testing instead establishes inherited primary EM.

Population incidence is poorly defined. Mixed EM studies cited in reviews reported approximately **1.3 per 100,000 person-years in Olmsted County** and **15 per 100,000 in New Zealand**, with female predominance. Geographic differences may reflect case definition and ascertainment rather than true biology. Secondary-specific prevalence, incidence, ethnic distribution, and male:female ratio remain unknown. (skeik2019erythromelalgia pages 2-3)

## 10. Diagnostics

### Clinical diagnosis

Diagnosis is based on the characteristic triad and provocation pattern. A photograph taken during an attack can be useful when the examination is normal between flares. There are no universally accepted validated diagnostic criteria or disease-specific biomarker. The source wording that diagnosis is “usually clinical” accurately summarizes current practice. (skeik2019erythromelalgia pages 1-2)

### Cause-directed workup

1. **CBC with differential and serial platelet/hematocrit assessment**; evaluate persistent thrombocytosis or erythrocytosis for MPN.
2. **Metabolic/neuropathy evaluation:** fasting glucose or HbA1c, vitamin B12, thyroid studies, renal/hepatic testing, serum protein electrophoresis/immunofixation as clinically indicated.
3. **Autoimmune/inflammatory testing:** ANA and disease-specific serologies only when history or examination supports them.
4. **Medication, infection, toxin, and injury history.**
5. **Vascular studies:** pulses and ankle-brachial index/Doppler to exclude occlusive disease; large-vessel Doppler may be normal in EM.
6. **Small-fiber/autonomic tests:** quantitative sensory testing, autonomic reflex screen, sudomotor tests, and 3-mm skin biopsy for intraepidermal nerve-fiber density when neuropathy is suspected.
7. **Thermography/laser Doppler/TcPO2:** supportive research or specialist tests, not standalone diagnostic standards. Skin biopsy may show reduced nerve density or intraluminal thrombi but is neither necessary nor specific. (assaad2025severeerythromelalgiapain pages 6-8, skeik2019erythromelalgia pages 2-3)

### Genetic testing

Single-gene **SCN9A** testing or a pain-channel/small-fiber-neuropathy panel is reasonable for childhood onset, a family history, or a strongly inherited phenotype. WES/WGS may be considered after specialist assessment when a monogenic disorder remains likely. CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing have no routine role in secondary EM. There is no role for population, newborn, or carrier screening.

### Differential diagnosis

Important alternatives are complex regional pain syndrome, Raynaud phenomenon/reperfusion, cellulitis or erysipelas, contact dermatitis, vasculitis, gout, osteomyelitis, arterial or venous insufficiency, acrocyanosis, Fabry disease, peripheral neuropathy, small-fiber neuropathy without EM, and systemic lupus erythematosus. CRPS is often unilateral and follows trauma with trophic/sudomotor abnormalities; cellulitis is persistent and infectious rather than heat-provoked and rapidly cooling-responsive. (skeik2019erythromelalgia pages 2-3)

## 11. Outcomes and prognosis

Secondary EM itself has no established disease-specific mortality rate, survival curve, or reduction in life expectancy. Prognosis depends mainly on the underlying disorder and severity of pain. MPN-associated cases may improve substantially with antiplatelet and disease-directed therapy; acquired neuropathic cases may remain chronic.

Morbidity can be profound: impaired walking, sleep loss, inability to tolerate shoes or warm environments, work/school limitation, anxiety, depression, and social isolation. Complications include maceration, ulceration, infection, tissue ischemia, and rarely amputation—often worsened by prolonged ice or water exposure. (skeik2019erythromelalgia pages 2-3, algarni2025comparativeefficacyand pages 1-2)

Favorable prognostic features include identification of a reversible cause and aspirin-responsive MPN disease. Persistent severe pain, established neuropathy, ulceration, and delayed cause recognition predict greater morbidity. No validated molecular prognostic biomarker exists.

## 12. Treatment and current applications

### Treatment strategy

1. **Identify and treat the underlying cause.**
2. **Avoid attacks safely:** cool environment, fans, elevation, breathable footwear, activity pacing; avoid direct ice and prolonged immersion.
3. **MPN-associated disease:** low-dose aspirin when not contraindicated; manage the MPN with hematology-directed phlebotomy or cytoreduction as appropriate.
4. **Localized symptoms:** topical lidocaine or compounded amitriptyline–ketamine.
5. **Neuropathic phenotype:** gabapentinoids, SNRIs, tricyclics, or sodium-channel blockers selected according to comorbidity and safety.
6. **Refractory disease:** specialist trials of vasoactive therapy, infusions, sympathetic procedures, or neuromodulation.

The literature explicitly states, “There is no single effective treatment for erythromelalgia,” and individualized, multidisciplinary management remains the expert consensus. (skeik2019erythromelalgia pages 1-2, algarni2025comparativeefficacyand pages 2-4)

### Drug and intervention evidence

- **Aspirin:** particularly effective in platelet-mediated MPN-associated secondary EM. Gastrointestinal bleeding, allergy, renal risk, and acquired von Willebrand disease in extreme thrombocytosis must be considered. Suggested NCIT intervention: aspirin therapy/antiplatelet therapy; CHEBI: aspirin.
- **Topical amitriptyline–ketamine:** in a mixed 36-patient cohort, about **75%** reported some pain relief: 3% complete, 39% substantial, and 33% some improvement. This is not a secondary-only response estimate. (algarni2025comparativeefficacyand pages 6-7)
- **Misoprostol:** small controlled studies reported improvements in pain and temperature control, but diarrhea, abdominal pain, and nausea were frequent. (algarni2025comparativeefficacyand pages 6-7)
- **Iloprost:** small studies reported improved cooling scores, sympathetic dysfunction, and disease severity; headache, flushing/erythema, and hypotension can occur. (algarni2025comparativeefficacyand pages 6-7)
- **Lidocaine:** topical or intravenous use aims to stabilize hyperexcitable sensory fibers; experimental studies showed dose-dependent improvement in nociceptive thresholds. Cardiac and neurologic toxicity constrain systemic use. (algarni2025comparativeefficacyand pages 6-7, algarni2025comparativeefficacyand pages 2-4)
- **Other reported agents:** gabapentin/pregabalin, amitriptyline, venlafaxine or other SNRIs, mexiletine, carbamazepine/oxcarbazepine, antihistamines, clonidine, and prostaglandin/vascular agents. Evidence is inconsistent and mostly uncontrolled.
- **Procedures:** sympathetic blocks, epidural/local anesthetic techniques, chemical or surgical sympathectomy, botulinum toxin, and spinal-cord stimulation are rescue options with case-level or very small-study support.
- **Pediatric rescue evidence:** one report described complete resolution in **4 of 5** patients receiving intravenous sodium nitroprusside, initially 1 µg/kg/min and titrated to 5 µg/kg/min; this is low-level evidence and not secondary-specific. (skeik2019erythromelalgia pages 2-3)

A 2025 systematic review found only six eligible studies, totaling **120 patients**: iloprost n=8, misoprostol n=21, topical amitriptyline–ketamine n=36, lidocaine n=27, chemical lumbar sympathectomy n=13, and miscellaneous agents n=11. The small, mixed-etiology evidence base precludes a robust universal hierarchy. (algarni2025comparativeefficacyand pages 4-5, algarni2025comparativeefficacyand pages 1-2)

### Recent developments and trials

- **EASE, NCT05917912:** randomized double-blind Phase 2 crossover study of topical amitriptyline 15% (ATX01), 14 participants; began June 14, 2023 and completed February 29, 2024. Outcomes included attack pain, Brief Pain Inventory, EQ-5D, depression, and rescue cooling. Eligibility excluded important alternative neuropathic pain causes, limiting direct applicability to secondary EM. URL: https://clinicaltrials.gov/study/NCT05917912. (NCT05917912 chunk 1, NCT05917912 chunk 2)
- **Burst spinal-cord stimulation, NCT04039633:** six-patient quadruple-blind crossover study, active but not recruiting; restricted to primary or idiopathic EM and excluded secondary disease. URL: https://clinicaltrials.gov/study/NCT04039633. (NCT04039633 chunk 1)
- Earlier XPF-001, XPF-002, and PF-05089771 NaV1.7 programs enrolled primary/inherited EM, not secondary EM. URLs: https://clinicaltrials.gov/study/NCT01090622, https://clinicaltrials.gov/study/NCT01486446, and https://clinicaltrials.gov/study/NCT01769274. (NCT01090622 chunk 1, NCT01486446 chunk 2, NCT01769274 chunk 3)

Thus, a major 2023–2024 research gap is the continued exclusion or underrepresentation of secondary EM in interventional trials.

## 13. Prevention

There is no vaccine, population screening program, or proven pharmacologic primary prevention. Practical prevention is etiologic and tertiary:

- Monitor blood counts when symptoms or risk factors suggest an MPN.
- Control diabetes and treat reversible neuropathy causes.
- Review and discontinue implicated medication when clinically safe.
- Avoid excessive heat, prolonged standing, tight footwear, and unsafe direct-ice cooling.
- Treat fissures or ulcers early and provide wound-care education.
- Use genetic counseling only when the history suggests **inherited primary** EM; it is not routinely relevant to acquired secondary disease.

No evidence supports prophylactic aspirin for people without EM or an independent cardiovascular/hematologic indication.

## 14. Other species and natural disease

No well-validated naturally occurring veterinary equivalent of acquired secondary EM was identified. Consequently, no specific NCBI Taxon, breed/VBO association, zoonotic transmission, or cross-species prevalence can be assigned. The condition is not infectious or zoonotic as a syndrome.

SCN9A orthologs are evolutionarily conserved across mammals, but their relevance is primarily to nociception and inherited channelopathy. Platelet activation, microvascular thrombosis, diabetic neuropathy, and autonomic dysregulation can be studied in animals, but these reproduce components rather than the full human secondary-EM syndrome.

## 15. Model organisms and experimental systems

Human iPSC-derived sensory neurons carrying pathogenic **SCN9A** variants reproduce lowered firing thresholds and permit pharmacologic reversal of inherited EM phenotypes. These systems and NaV1.7 transgenic/knock-in models are valuable for pain-channel biology but model **primary inherited EM**, not secondary EM. The PF-05089771 program linked iPSC-derived sensory-neuron findings to a primary-EM trial, illustrating this translational application. (NCT01769274 chunk 3)

Potential component models include:

- MPN or platelet-activation mouse models for thrombotic microvascular mechanisms.
- Streptozotocin or genetic diabetes models for acquired small-fiber neuropathy.
- Peripheral nerve injury/inflammation models for nociceptor hyperexcitability.
- Endothelial-flow and microfluidic systems for capillary perfusion and thrombosis.

Their central limitation is failure to reproduce the defining human combination of heat-provoked erythema, thermoregulatory shunting, and severe distal burning pain. No dedicated, validated acquired secondary-EM mouse, rat, zebrafish, Drosophila, organoid, CRISPR-screen, or natural-animal model was identified.

## Knowledge-base conclusions

Secondary erythromelalgia should be represented as an **acquired clinical syndrome with multiple possible causal-disease relationships**, not as an SCN9A disorder. Core phenotype assertions are well supported; secondary-specific epidemiology, molecular profiling, prognosis, and randomized-treatment evidence are sparse. The highest-priority implementation rules are: record the red-hot-burning attack phenotype; document heat/exercise/dependency triggers and cooling response; actively evaluate MPNs and neuropathies; annotate aspirin responsiveness specifically to platelet-mediated disease; and avoid transferring inherited-EM genetic claims or primary-only clinical-trial results to secondary EM.

References

1. (assaad2025severeerythromelalgiapain pages 6-8): Wassim Assaad, Omar El Tarras, Soad Al Osta, and Chady Kallassy. Severe erythromelalgia pain attack in a young lebanese woman leading to hospitalization: a case report and literature review. Cureus, Sep 2025. URL: https://doi.org/10.7759/cureus.91530, doi:10.7759/cureus.91530. This article has 0 citations.

2. (skeik2019erythromelalgia pages 2-3): Nedaa Skeik. Erythromelalgia. Harper's Textbook of Pediatric Dermatology, pages 1961-1964, Nov 2019. URL: https://doi.org/10.1002/9781119142812.ch151, doi:10.1002/9781119142812.ch151. This article has 1 citations.

3. (algarni2025comparativeefficacyand pages 1-2): Abdullah S. Algarni, Reem M. Alharthi, Shaden O. Alqurashi, Ruba M. Alghanmi, Rimaz R. Aldawsari, Maysaa A. Alghamdi, and Ramy Samargandi. Comparative efficacy and tolerability of treatments for erythromelalgia: a systematic review. Medicina, 61:920, May 2025. URL: https://doi.org/10.3390/medicina61050920, doi:10.3390/medicina61050920. This article has 1 citations.

4. (skeik2019erythromelalgia pages 1-2): Nedaa Skeik. Erythromelalgia. Harper's Textbook of Pediatric Dermatology, pages 1961-1964, Nov 2019. URL: https://doi.org/10.1002/9781119142812.ch151, doi:10.1002/9781119142812.ch151. This article has 1 citations.

5. (algarni2025comparativeefficacyand pages 4-5): Abdullah S. Algarni, Reem M. Alharthi, Shaden O. Alqurashi, Ruba M. Alghanmi, Rimaz R. Aldawsari, Maysaa A. Alghamdi, and Ramy Samargandi. Comparative efficacy and tolerability of treatments for erythromelalgia: a systematic review. Medicina, 61:920, May 2025. URL: https://doi.org/10.3390/medicina61050920, doi:10.3390/medicina61050920. This article has 1 citations.

6. (algarni2025comparativeefficacyand pages 6-7): Abdullah S. Algarni, Reem M. Alharthi, Shaden O. Alqurashi, Ruba M. Alghanmi, Rimaz R. Aldawsari, Maysaa A. Alghamdi, and Ramy Samargandi. Comparative efficacy and tolerability of treatments for erythromelalgia: a systematic review. Medicina, 61:920, May 2025. URL: https://doi.org/10.3390/medicina61050920, doi:10.3390/medicina61050920. This article has 1 citations.

7. (algarni2025comparativeefficacyand pages 7-9): Abdullah S. Algarni, Reem M. Alharthi, Shaden O. Alqurashi, Ruba M. Alghanmi, Rimaz R. Aldawsari, Maysaa A. Alghamdi, and Ramy Samargandi. Comparative efficacy and tolerability of treatments for erythromelalgia: a systematic review. Medicina, 61:920, May 2025. URL: https://doi.org/10.3390/medicina61050920, doi:10.3390/medicina61050920. This article has 1 citations.

8. (algarni2025comparativeefficacyand pages 2-4): Abdullah S. Algarni, Reem M. Alharthi, Shaden O. Alqurashi, Ruba M. Alghanmi, Rimaz R. Aldawsari, Maysaa A. Alghamdi, and Ramy Samargandi. Comparative efficacy and tolerability of treatments for erythromelalgia: a systematic review. Medicina, 61:920, May 2025. URL: https://doi.org/10.3390/medicina61050920, doi:10.3390/medicina61050920. This article has 1 citations.

9. (NCT04039633 chunk 1):  Spinal Cord Stimulation for Refractory Pain in Erythromelalgia. St. Olavs Hospital. 2019. ClinicalTrials.gov Identifier: NCT04039633

10. (NCT05917912 chunk 1):  EASE (Efficacy of ATX01 Study in Erythromelalgia). AlgoTherapeutix. 2023. ClinicalTrials.gov Identifier: NCT05917912

11. (NCT05917912 chunk 2):  EASE (Efficacy of ATX01 Study in Erythromelalgia). AlgoTherapeutix. 2023. ClinicalTrials.gov Identifier: NCT05917912

12. (NCT01090622 chunk 1):  Study of XPF-001 in the Treatment of Pain From Primary/Inherited Erythromelalgia (IEM). Xenon Pharmaceuticals Inc.. 2010. ClinicalTrials.gov Identifier: NCT01090622

13. (NCT01486446 chunk 2):  Phase 2a, Exploratory Study to Evaluate the Safety, Efficacy, Tolerability and Pharmacokinetics of XPF-002 in Patients With Primary/Inherited Erythromelalgia. Xenon Pharmaceuticals Inc.. 2011. ClinicalTrials.gov Identifier: NCT01486446

14. (NCT01769274 chunk 3):  Evaluation Of The Efficacy And Safety Of Single Doses Of PF-05089771 In Patients With Primary (Inherited) Erythromelalgia. Pfizer. 2012. ClinicalTrials.gov Identifier: NCT01769274

## Artifacts

- [Edison artifact artifact-00](Secondary_Erythromelalgia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.