---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:07:13.632762'
end_time: '2026-08-19T09:15:35.596350'
duration_seconds: 501.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Deafness, Congenital Heart Defects, and Posterior Embryotoxon
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Deafness_Congenital_Heart_Defects_And_Posterior_Embryotoxon-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Deafness, Congenital Heart Defects, and Posterior Embryotoxon
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Deafness, Congenital Heart Defects, and Posterior Embryotoxon** covering all of the
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
- **Disease Name:** Deafness, Congenital Heart Defects, and Posterior Embryotoxon
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Deafness, Congenital Heart Defects, and Posterior Embryotoxon** covering all of the
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


# Research report: Deafness, Congenital Heart Defects, and Posterior Embryotoxon

## Executive interpretation

**Deafness, congenital heart defects, and posterior embryotoxon** is an exceptionally rare, autosomal-dominant **JAG1-related developmental disorder** catalogued as **MONDO:0060713**. The disease was delineated in one multigenerational family and is best interpreted as a **liver-sparing, atypical Alagille-spectrum phenotype**, rather than a mechanistically separate disorder. Its defining allele is **JAG1 p.Cys234Tyr (p.C234Y)**, which segregated with cardiac defects, deafness, and posterior embryotoxon; all nine studied family members had normal liver function. Subsequent experiments showed defective protein maturation, absent cell-surface localization, failure to activate Notch, and functional JAG1 haploinsufficiency. The very small evidence base means that syndrome-specific frequencies, penetrance, prognosis, and treatment-response estimates cannot be calculated reliably. (OpenTargets Search: Deafness, congenital heart defects, and posterior embryotoxon, bauer2010jagged1(jag1)mutations pages 9-10)

| domain | syndrome-specific finding | evidence level/limitations |
|---|---|---|
| Disease identity | MONDO:0060713 corresponds to an ultra-rare JAG1-related disorder named **deafness, congenital heart defects, and posterior embryotoxon**; currently linked to **JAG1** in disease-target resources. | High confidence for identifier/target mapping; disease definition is based on a very small historical literature base rather than large registries. (OpenTargets Search: Deafness, congenital heart defects, and posterior embryotoxon) |
| Genetic cause | Causal variant reported is **JAG1 p.Cys234Tyr (p.C234Y)**, a missense substitution affecting a conserved cysteine in the first EGF-like repeat. | High confidence from functional/genetic follow-up literature; nucleotide-level HGVS was not available in retrieved context. (bauer2010jagged1(jag1)mutations pages 9-10) |
| Inheritance / pedigree | The phenotype is described as a **familial, autosomal dominant** disorder segregating in a **nine-member family**. | High confidence for dominant familial segregation and studied family size; exact pedigree structure and penetrance values were not available in retrieved context. (bauer2010jagged1(jag1)mutations pages 9-10) |
| Defining phenotype triad | Core syndrome-defining features are **deafness + congenital heart defects + posterior embryotoxon**. | High confidence for the triad; retrieved follow-up source does not fully resolve deafness subtype/severity or the full spectrum of cardiac lesions in each relative. (bauer2010jagged1(jag1)mutations pages 9-10) |
| Liver involvement | In contrast to classic Alagille syndrome, **all nine studied family members had normal liver function**. | High confidence and clinically important distinction; this does not exclude broader JAG1/Alagille overlap in other families. (bauer2010jagged1(jag1)mutations pages 9-10) |
| Molecular mechanism | p.Cys234Tyr causes **defective post-translational processing**, **lack of cell-surface expression**, **failure to activate Notch signaling**, and is interpreted as causing **JAG1 haploinsufficiency**. | High confidence from functional assays in a later study; mechanism is experimentally supported but was not measured directly in the original family report. (bauer2010jagged1(jag1)mutations pages 9-10, bauer2010jagged1(jag1)mutations pages 13-19) |
| Structural interpretation | The altered cysteine is predicted to disrupt **EGF-repeat folding/disulfide bond formation** in a region crucial for ligand-receptor interaction. | High confidence mechanistic inference supported by conservation/structure discussion; still partly inferential rather than direct structural biophysics for this exact family. (bauer2010jagged1(jag1)mutations pages 9-10) |
| Expressivity | The syndrome shows **variable expressivity**, consistent with other familial JAG1 disorders. | Moderate-high confidence; no syndrome-specific quantitative expressivity or penetrance estimates were available. (bauer2010jagged1(jag1)mutations pages 9-10) |
| Relation to Alagille spectrum | Best interpreted as a **liver-sparing / atypical Alagille-spectrum JAG1 phenotype**, not a wholly separate mechanism. | High confidence from gene-level and clinical-overlap evidence; extrapolation beyond the reported family should be done cautiously. (OpenTargets Search: Deafness, congenital heart defects, and posterior embryotoxon, chitayat2016alagillesyndromeclinical pages 1-2, gilbert2019alagillesyndromemutation pages 1-5) |
| Broader Alagille context | Broader JAG1-related Alagille syndrome is **autosomal dominant**, often multisystemic, and may occur **without overt liver disease**; JAG1 accounts for most molecularly confirmed ALGS cases. | Useful contextual evidence only; these data are **not syndrome-specific** for MONDO:0060713. (chitayat2016alagillesyndromeclinical pages 1-2, chitayat2016alagillesyndromeclinical pages 5-7, gilbert2019alagillesyndromemutation pages 1-5, chitayat2016alagillesyndromeclinical pages 2-4, gilbert2019alagillesyndromemutation pages 20-24, gilbert2019alagillesyndromemutation pages 24-27) |
| Diagnostics | Current practical diagnosis would rely on **clinical recognition of the triad plus JAG1 sequencing/CNV analysis**, often within broader congenital heart disease or Alagille/ocular-anomaly testing. | Moderate confidence by extrapolation from JAG1/ALGS diagnostic practice; no syndrome-specific diagnostic guideline was found. (chitayat2016alagillesyndromeclinical pages 5-7, gilbert2019alagillesyndromemutation pages 20-24, gilbert2019alagillesyndromemutation pages 24-27) |
| Treatment / management | **No syndrome-specific therapy** was identified; management is phenotype-directed (cardiac care, hearing evaluation/habilitation, ophthalmic assessment) with genetics follow-up. | Moderate confidence because absence of evidence reflects rarity; no syndrome-specific interventional studies or trials were found. (chitayat2016alagillesyndromeclinical pages 1-2, chitayat2016alagillesyndromeclinical pages 5-7) |
| Epidemiology / natural history | **No syndrome-specific prevalence, incidence, or longitudinal natural-history data** were identified. | High confidence for evidence gap; available frequency data pertain to broader Alagille syndrome, not MONDO:0060713 specifically. (chitayat2016alagillesyndromeclinical pages 1-2, gilbert2019alagillesyndromemutation pages 1-5) |
| Recent developments (2023-2024) | Recent work mainly strengthens the **broader JAG1/Alagille framework**: alternative diagnoses in Axenfeld-Rieger-spectrum testing (2023) and Jag1-dependent cochlear cell-patterning mechanisms in mouse/scRNA-seq studies (2024). | Indirect but relevant; these studies do not add new syndrome-specific human cases for MONDO:0060713. (reis2023alternativegeneticdiagnoses pages 2-4, haan2024jag1repressesnotch pages 1-3) |


*Table: This table summarizes the most defensible syndrome-specific facts for deafness, congenital heart defects, and posterior embryotoxon, while clearly separating direct evidence from broader JAG1/Alagille-spectrum context. It is useful for knowledge-base curation because it highlights what is known with high confidence and where evidence gaps remain.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Deafness, congenital heart defects, and posterior embryotoxon.
* **MONDO:** **MONDO:0060713**.
* **Causal-gene association:** **JAG1**, Ensembl **ENSG00000101384**, encoding jagged canonical Notch ligand 1. Open Targets identifies JAG1 as the sole associated target and links the association to PMID **12022040** and PMID **20437614**. (OpenTargets Search: Deafness, congenital heart defects, and posterior embryotoxon)
* **OMIM/Orphanet:** No confidently verified, disorder-specific OMIM phenotype number or Orphanet number was recovered. It may be indexed under JAG1/Alagille-spectrum disease rather than as a distinct entry.
* **ICD-10/ICD-11 and MeSH:** No syndrome-specific code or heading was identified. Component findings should be coded separately—congenital cardiac malformation, hearing loss, and anterior-segment anomaly—while documenting the molecular diagnosis.
* **Synonyms:** “Familial deafness, congenital heart defects, and posterior embryotoxon”; “JAG1-related deafness–heart defect–posterior embryotoxon syndrome”; descriptively, “liver-sparing JAG1/Alagille-spectrum disorder.” The latter is an interpretive synonym, not necessarily a formal database label.

The source evidence is **patient/family-level**, originating from a nine-member pedigree, with subsequent aggregation in disease databases and JAG1/Alagille reviews. It is not derived from EHR-scale cohorts or population registries. (bauer2010jagged1(jag1)mutations pages 9-10)

### Relationship to Alagille syndrome

Classic Alagille syndrome (ALGS; MIM 118450) is a variable autosomal-dominant disorder involving cholestasis/bile-duct paucity, pulmonary-artery or other cardiac disease, posterior embryotoxon, characteristic facies, and butterfly vertebrae; renal and vascular abnormalities may also occur. Molecular testing has demonstrated that JAG1/NOTCH2-positive individuals can lack overt liver disease. Thus, absence of cholestasis does not exclude a JAG1 disorder. (chitayat2016alagillesyndromeclinical pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is a **heterozygous germline JAG1 missense variant, p.Cys234Tyr**, in the first epidermal-growth-factor-like repeat. The altered cysteine is evolutionarily conserved and normally participates in disulfide bonding required for EGF-repeat folding. Functional evidence supports a loss-of-function/haploinsufficiency mechanism. (bauer2010jagged1(jag1)mutations pages 9-10)

The exact transcript-level cDNA HGVS nomenclature was not available in the retrieved primary evidence and should not be inferred without checking the original sequence reference. The variant should therefore be stored as **JAG1 p.Cys234Tyr**, with transcript and genome build left unresolved pending ClinVar/original-paper verification.

### Risk factors

* **Genetic:** Carrying the familial pathogenic JAG1 allele is the principal risk factor. Affected individuals have a theoretical **50% transmission probability per pregnancy** under autosomal-dominant inheritance. Broader ALGS data indicate that approximately 50–70% of cases are de novo, but this statistic is not specific to this pedigree. (chitayat2016alagillesyndromeclinical pages 5-7)
* **Family history:** A first-degree relative carrying the allele materially increases prior probability, although phenotype cannot be predicted reliably because JAG1 disorders show marked intrafamilial variability. (bauer2010jagged1(jag1)mutations pages 9-10, gilbert2019alagillesyndromemutation pages 1-5)
* **Environmental, infectious, lifestyle, age, and sex factors:** None are established for this Mendelian syndrome.
* **Modifier genes:** No validated modifier was identified for this particular phenotype.
* **Gene–environment interactions:** No syndrome-specific evidence was found.

### Protective factors

No genetic or environmental factor is known to prevent penetrance or protect against the cardiac, auditory, or ocular manifestations. Normal liver function in the reported family is a phenotype observation, not evidence of a protective exposure or allele. (bauer2010jagged1(jag1)mutations pages 9-10)

## 3. Phenotypes

The syndrome-specific literature confirms the triad but does not provide reliable per-feature percentages, complete lesion-level cardiac data, or standardized hearing measurements. Frequencies below should therefore be recorded as **unknown**, except that all nine studied relatives reportedly had normal liver function. (bauer2010jagged1(jag1)mutations pages 9-10)

### Deafness/hearing loss

* **Type:** Clinical symptom/sign; exact conductive versus sensorineural composition in the original family was not recovered.
* **Onset:** Presumed congenital or early developmental from the syndrome definition, but individual ages were unavailable.
* **Severity/course:** Unknown and probably variable; stability versus progression has not been established.
* **Suggested HPO:** **Hearing impairment (HP:0000365)**; use **Sensorineural hearing impairment (HP:0000407)** or **Conductive hearing impairment (HP:0000405)** only after audiologic confirmation.
* **Functional effect:** Potential impairment of speech/language development, education, communication, balance, and social participation. No syndrome-specific PROM, EQ-5D, or SF-36 study exists.

Broader JAG1 disease can produce conductive and sensorineural loss through middle-ear ossicular abnormalities or sensory/neural deficits. This is supportive context, not proof of the hearing-loss subtype in the original family. (haan2024jag1repressesnotch pages 1-3)

### Congenital heart defects

* **Type:** Congenital structural malformation.
* **Onset:** Prenatal/congenital.
* **Severity/course:** Lesion-dependent and variably expressed; exact defects in each original relative were not recovered.
* **Suggested HPO:** **Congenital heart defect (HP:0001627)**. Add lesion-specific terms after echocardiography; in broader JAG1 disease, pulmonary stenosis/peripheral pulmonary artery stenosis and tetralogy of Fallot are prominent.
* **Functional effect:** May cause cyanosis, exercise intolerance, arrhythmia, heart failure, need for catheterization or surgery, and premature mortality depending on lesion severity.

In broader ALGS cohorts, cardiac involvement has been reported in 90–97%, pulmonic stenosis in approximately 67%, and tetralogy of Fallot in 7–16%; these values **must not be assigned to MONDO:0060713** because they come from classic ALGS cohorts. (chitayat2016alagillesyndromeclinical pages 2-4)

### Posterior embryotoxon/anterior-segment anomaly

* **Type:** Ophthalmic clinical sign—an anteriorly displaced/prominent Schwalbe line observed by slit-lamp examination.
* **Onset/course:** Congenital and generally stable.
* **Severity:** Often visually asymptomatic by itself; associated anterior-segment dysgenesis or glaucoma determines visual impact.
* **Suggested HPO:** **Posterior embryotoxon (HP:0000627)**; consider **Anterior segment dysgenesis (HP:0004328)** and **Glaucoma (HP:0000501)** if documented.
* **Frequency:** Unknown in this family. In broader ALGS, posterior embryotoxon is reported in approximately 78–89%, again not a syndrome-specific estimate. (chitayat2016alagillesyndromeclinical pages 2-4)

### Liver phenotype

All nine studied p.Cys234Tyr family members had **normal liver function**, an unusual but important distinction from classic ALGS. Suggested HPO annotation: **Absence of cholestasis** as a negated phenotype rather than a positive HPO feature. Normal biochemical tests do not necessarily establish normal bile-duct anatomy. (bauer2010jagged1(jag1)mutations pages 9-10)

## 4. Genetic and molecular information

* **Gene:** **JAG1**; HGNC-approved symbol JAG1; protein Jagged-1, a membrane-bound canonical Notch ligand.
* **Variant:** **p.Cys234Tyr**, heterozygous, germline, missense, first EGF-like repeat.
* **Classification:** The segregation and functional evidence strongly support pathogenicity, although a current ClinVar assertion and ACMG evidence-code set were not directly recovered.
* **Population frequency:** Not available in the retrieved evidence. Contemporary curation should query gnomAD using verified transcript/genomic coordinates; absence should not be asserted from protein nomenclature alone.
* **Functional class:** Loss of function through defective processing/trafficking and inability to initiate Notch signaling—effectively haploinsufficiency rather than gain of function or dominant negative action. (bauer2010jagged1(jag1)mutations pages 9-10, bauer2010jagged1(jag1)mutations pages 13-19)
* **Chromosomal locus:** JAG1 lies on chromosome 20p12; no syndrome-defining deletion, translocation, inversion, mosaicism, or aneuploidy was identified in this family.
* **Modifiers/epigenetics:** No validated modifier gene, methylation signature, histone abnormality, or disease-specific chromatin alteration is known.

Broader ALGS datasets support haploinsufficiency: most pathogenic JAG1 alleles are truncating, splice-disrupting, or deletions. A 27-year series compiled 401 probands and 111 affected relatives, with 694 JAG1 and 19 NOTCH2 variants documented; 94.3% of molecularly characterized ALGS cases had JAG1 variants, 2.5% NOTCH2 variants, and 3.2% remained unresolved. These are ALGS statistics, not prevalence figures for this named syndrome. (gilbert2019alagillesyndromemutation pages 1-5, gilbert2019alagillesyndromemutation pages 20-24, gilbert2019alagillesyndromemutation pages 24-27)

## 5. Environmental and infectious information

No toxin, radiation exposure, pollution, occupation, diet, smoking, alcohol use, exercise pattern, medication, or infectious agent is known to cause or trigger this disorder. The phenotype results from a developmental germline JAG1 defect. Environmental risk reduction therefore cannot prevent the inherited allele, although ordinary prenatal risk avoidance remains appropriate for general fetal health.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** p.Cys234Tyr removes a conserved cysteine in JAG1’s first EGF-like repeat.
2. **Protein-level defect:** Disulfide-dependent folding and post-translational maturation are disrupted; experimental protein was EndoH-sensitive and localized perinuclearly/within the endoplasmic-reticulum pathway rather than at the plasma membrane. (bauer2010jagged1(jag1)mutations pages 13-19, bauer2010jagged1(jag1)mutations pages 9-10)
3. **Signaling defect:** Mutant JAG1 is absent from the cell surface and cannot activate adjacent-cell Notch receptors. Only the wild-type allele supplies functional surface ligand, producing **JAG1 haploinsufficiency**. (bauer2010jagged1(jag1)mutations pages 9-10)
4. **Developmental consequences:** Reduced cell–cell Notch signaling perturbs fate specification and morphogenesis in the cardiovascular outflow/pulmonary vasculature, anterior eye segment, and inner/middle ear.
5. **Clinical manifestations:** Abnormal cardiac morphogenesis causes congenital heart defects; altered cochlear/ear patterning causes hearing loss; abnormal anterior-segment development produces posterior embryotoxon.

### Suggested ontology annotations

* **GO biological processes:** Notch signaling pathway (**GO:0007219**); cell-fate commitment (**GO:0045165**); inner-ear development (**GO:0048839**); heart development (**GO:0007507**); eye development (**GO:0001654**); epithelial cell differentiation (**GO:0030855**).
* **GO molecular function:** Notch receptor binding (**GO:0005112**).
* **GO cellular components:** plasma membrane (**GO:0005886**), endoplasmic reticulum (**GO:0005783**), extracellular region (**GO:0005576**).
* **Candidate cell types:** cochlear supporting cell, inner hair cell, outer hair cell, vascular endothelial cell, vascular smooth-muscle cell, cardiac neural-crest-derived cell, and anterior-segment mesenchymal/neural-crest-derived cell. Exact CL identifiers should be validated against the current Cell Ontology release.

### Recent mechanistic development, 2024

A 2024 Jag1^Ndr/Ndr mouse study combined cochlear morphology with single-cell RNA sequencing. Its abstract reports “a dose-dependent increase in ectopic inner hair cells, and a reduction in outer hair cells” and “global dysregulation of genes associated with inner ear development and deafness.” Cell-resolved analysis implicated lateral supporting cells and outer-hair-cell specification. This is compelling model-organism evidence for how JAG1 insufficiency can cause auditory dysfunction, but it was not performed in p.Cys234Tyr carriers. DOI: https://doi.org/10.1242/dev.202949; published November 2024. (haan2024jag1repressesnotch pages 1-3)

No syndrome-specific human transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, organoid, or CRISPR-screen dataset was identified.

## 7. Anatomical structures affected

* **Primary organs/systems:** heart and great vessels; auditory system; anterior ocular segment.
* **Possible broader JAG1 surveillance organs:** liver/biliary tree, kidneys, skeleton, and cerebral/systemic vasculature, even though liver function was normal in the defining family. (chitayat2016alagillesyndromeclinical pages 1-2, chitayat2016alagillesyndromeclinical pages 2-4)
* **Suggested UBERON:** heart (**UBERON:0000948**), inner ear (**UBERON:0001846**), cochlea (**UBERON:0001844**), eye (**UBERON:0000970**), cornea (**UBERON:0000964**), liver (**UBERON:0002107**), pulmonary artery (**UBERON:0002012**).
* **Tissues/cells:** cardiac/outflow-tract mesenchyme and vasculature; organ-of-Corti sensory hair cells and supporting cells; corneal limbal/anterior-chamber structures.
* **Subcellular localization:** ER/perinuclear secretory pathway and plasma membrane. The mutant’s failure to reach the latter is central to pathogenesis. (bauer2010jagged1(jag1)mutations pages 13-19, bauer2010jagged1(jag1)mutations pages 9-10)
* **Lateralization:** Hearing loss may be bilateral, but syndrome-specific laterality was not recovered; posterior embryotoxon should be assessed in both eyes.

## 8. Temporal development and natural history

The structural lesions originate during embryogenesis; the clinical pattern is therefore **congenital**, chronic, and lifelong. Posterior embryotoxon is generally stable. Cardiac course depends on lesion anatomy and intervention. Hearing may be detected during newborn screening or later in childhood; progression has not been characterized in this family.

There is no validated staging system, remission pattern, progression rate, or longitudinal natural-history cohort. Critical intervention windows are nevertheless clinically evident: prenatal/early postnatal cardiac assessment, newborn/early-childhood audiologic diagnosis to protect language development, and early ophthalmologic evaluation for associated glaucoma.

## 9. Inheritance and population

* **Inheritance:** Autosomal dominant; familial segregation supports vertical transmission. (bauer2010jagged1(jag1)mutations pages 9-10)
* **Penetrance:** Not quantifiable from available data. The allele segregated with the named phenotype, but individual-feature penetrance was not recovered.
* **Expressivity:** Variable, consistent with familial JAG1 disorders. In broader JAG1-positive families, relatives with the same variant may range from subclinical findings to severe disease, and 47% of mutation-positive relatives in one ALGS analysis did not meet classic criteria. (bauer2010jagged1(jag1)mutations pages 9-10, chitayat2016alagillesyndromeclinical pages 2-4)
* **Anticipation:** No evidence.
* **Germline mosaicism:** Not reported; low residual recurrence risk after an apparently de novo variant is a general counseling consideration.
* **Founder effect, consanguinity, carrier frequency:** None established; “carrier” is not clinically neutral in a dominant disorder.
* **Prevalence/incidence:** Unknown. The named phenotype is supported principally by one nine-member pedigree. Broader ALGS is estimated at roughly 1:30,000–1:50,000 live births, but that figure must not be assigned to MONDO:0060713. (chitayat2016alagillesyndromeclinical pages 1-2, gilbert2019alagillesyndromemutation pages 1-5)
* **Sex/ethnicity/geography:** No reliable syndrome-specific distribution or sex ratio exists.

## 10. Diagnostics

### Clinical evaluation

A practical diagnostic work-up should include:

1. Three-generation pedigree and dysmorphology/medical-genetics examination.
2. Formal audiology: newborn screen where age-appropriate, diagnostic auditory brainstem response, otoacoustic emissions, and behavioral pure-tone audiometry; tympanometry helps distinguish conductive from sensorineural loss.
3. Echocardiography with ECG; add cardiac MRI/CT or catheterization according to the identified lesion.
4. Slit-lamp examination for posterior embryotoxon/anterior-segment dysgenesis; measure intraocular pressure and assess optic nerves.
5. Baseline liver panel—bilirubin fractions, AST/ALT, GGT, alkaline phosphatase, albumin and coagulation—and clinical assessment for cholestasis, despite normal liver function in the original family.
6. Renal function/urinalysis and renal ultrasound; vertebral imaging when clinically indicated; consider vascular/neurovascular assessment based on symptoms and broader ALGS practice. Multidisciplinary ALGS care commonly involves cardiology, hepatology, nephrology, and ophthalmology. (chitayat2016alagillesyndromeclinical pages 1-2, chitayat2016alagillesyndromeclinical pages 5-7)

No disease-specific serum protein, metabolite, histologic, or circulating biomarker exists.

### Genetic testing

* **First line:** A congenital-heart/hearing-loss/anterior-segment or ALGS panel that includes **JAG1** and deletion/duplication analysis. Alternatively, sequence JAG1 directly when the phenotype and family variant are known.
* **Familial testing:** Targeted testing for p.Cys234Tyr after laboratory confirmation of transcript/genomic coordinates.
* **If negative:** JAG1 CNV analysis, NOTCH2, and broader exome/genome testing. In 2023, exome analysis of Axenfeld–Rieger-like cases found pathogenic variants across JAG1, USP9X, CDK13, BCOR, and other regions, supporting broad second-tier testing for overlapping phenotypes. DOI: https://doi.org/10.3390/genes14101948; published October 2023. (reis2023alternativegeneticdiagnoses pages 2-4)
* **Yield in broader ALGS:** Sequencing all JAG1 exons identifies about 85% of variants and CNV analysis approximately another 9%; NOTCH2 testing follows when JAG1 is negative. (gilbert2019alagillesyndromemutation pages 20-24)
* **WES/WGS:** Useful in atypical or panel-negative disease, especially to resolve phenocopies and structural variants. RNA sequencing is investigational for splice effects.
* **CMA:** Appropriate when multiple congenital anomalies/developmental delay suggest a chromosome 20p deletion or another CNV.
* **Karyotype/FISH:** Not routine unless a large rearrangement is suspected.
* **Mitochondrial and repeat-expansion testing:** Not indicated by this phenotype.

### Differential diagnosis

Important alternatives include classic **Alagille syndrome** due to JAG1 or NOTCH2; **Axenfeld–Rieger syndrome** due to PITX2/FOXC1; **CHARGE syndrome**; terminal 6p deletion/FOXC1-related disease; BCOR-related ocular syndromes; and other syndromic hearing-loss/congenital-heart disorders. Liver/biliary disease, characteristic pulmonary-artery lesions, butterfly vertebrae and JAG1 findings favor ALGS spectrum; prominent Axenfeld–Rieger anomaly, dental/umbilical findings and PITX2/FOXC1 variants favor classic ARS. The substantial overlap justifies broad molecular testing. (reis2023alternativegeneticdiagnoses pages 2-4, chitayat2016alagillesyndromeclinical pages 1-2)

## 11. Outcome and prognosis

No syndrome-specific survival rate, life expectancy, mortality rate, disability score, or prognostic biomarker is available. Prognosis should be individualized according to:

* congenital-heart lesion type and hemodynamic severity;
* degree and timing of hearing loss and access to habilitation;
* glaucoma or other sight-threatening anterior-segment disease;
* emergence of hepatic, renal, or vascular manifestations.

Normal liver function in all reported relatives may imply a more favorable hepatic course than classic ALGS, but the family size and absence of long-term standardized follow-up preclude a firm prognostic conclusion. In broader ALGS, early mortality is driven mainly by severe cardiac or hepatic disease and later mortality by vascular events. (bauer2010jagged1(jag1)mutations pages 9-10, chitayat2016alagillesyndromeclinical pages 1-2)

Long-term morbidity may include communication disability, educational impact, cardiac exercise limitation, repeated interventions, and visual loss if glaucoma develops. No disease-specific quality-of-life instrument or recovery-rate study was found.

## 12. Treatment and real-world implementation

There is **no disease-modifying or genotype-specific therapy** for this named syndrome. Treatment is component-directed:

* **Heart disease:** Pediatric cardiology surveillance; medication for heart failure/arrhythmia where indicated; catheter-based dilation/stenting or surgical repair according to anatomy. Suggested NCIt terms: **Cardiac Surgery**, **Cardiac Catheterization**, **Angioplasty**, **Stent Placement**.
* **Hearing loss:** Hearing aids for aidable loss; bone-conduction devices for selected conductive/mixed loss; cochlear implantation for severe-to-profound sensorineural loss meeting standard criteria; speech-language and educational support. Suggested NCIt terms: **Hearing Aid**, **Cochlear Implantation**, **Speech Therapy**, **Audiologic Evaluation**.
* **Eye disease:** Observation for isolated posterior embryotoxon; glaucoma medication, laser, or surgery only when glaucoma/anterior-segment complications occur. Suggested NCIt terms: **Ophthalmologic Examination**, **Glaucoma Therapy**, **Trabeculectomy**.
* **Genetics:** Counseling, cascade testing, and coordinated JAG1/ALGS-spectrum surveillance.

No pharmacogenomic rule, approved targeted drug, gene therapy, cell therapy, antisense/siRNA therapy, or immunotherapy applies. No syndrome-specific interventional ClinicalTrials.gov study was identified. Broader ALGS treatments for cholestasis or liver transplantation are not indicated merely because a patient carries JAG1; they are used only for documented hepatic disease. The reported family had normal liver function. (bauer2010jagged1(jag1)mutations pages 9-10, chitayat2016alagillesyndromeclinical pages 5-7)

## 13. Prevention

* **Primary prevention:** The inherited developmental disorder cannot be prevented by lifestyle modification, vaccination, or prophylactic medication.
* **Reproductive prevention/options:** Genetic counseling; targeted prenatal diagnosis using chorionic-villus sampling or amniocentesis after the familial genomic variant is verified; and IVF with preimplantation genetic testing for monogenic disease. Variable expressivity must be emphasized because genotype does not predict severity reliably. (chitayat2016alagillesyndromeclinical pages 5-7, gilbert2019alagillesyndromemutation pages 1-5)
* **Secondary prevention:** Cascade testing; fetal echocardiography in an at-risk pregnancy; newborn hearing screening followed by definitive audiology; early echocardiography and slit-lamp examination.
* **Tertiary prevention:** Timely cardiac repair, hearing habilitation during language acquisition, glaucoma monitoring, and surveillance for broader JAG1-related liver, renal, and vascular disease.
* **Immunization/public-health or infectious prophylaxis:** No disease-specific measure.

## 14. Other species and natural disease

No naturally occurring veterinary disorder specifically equivalent to this human triad was identified, and there is no zoonotic or transmissible component. JAG1/Notch developmental functions are evolutionarily conserved across vertebrates. Relevant taxa include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, and **Danio rerio (7955)**. Breed-specific VBO annotations, natural animal prevalence, and cross-species transmission are not applicable.

## 15. Model organisms

### Mouse

The principal recent model is the **Jag1 Nodder (Jag1^Ndr)** mouse. Homozygous mice are viable and show auditory/vestibular deficits, increased ectopic inner hair cells, reduced outer hair cells, and supporting-cell abnormalities. Single-cell RNA sequencing demonstrated cell-type-resolved dysregulation of inner-ear-development and deafness genes. This model is valuable for cochlear patterning and JAG1–Notch signaling but does not carry human p.Cys234Tyr and cannot reproduce the exact family’s penetrance or full cardiac/ocular phenotype. (haan2024jag1repressesnotch pages 1-3)

The 2024 abstract’s key statement is: “Jag1-regulated Notch signaling controls cochlear patterning, affecting inner and outer hair cell specification and hearing in Alagille syndrome.” DOI: https://doi.org/10.1242/dev.202949; November 2024. (haan2024jag1repressesnotch pages 1-3)

### Cellular models

Transfected-cell assays of p.Cys234Tyr directly tested maturation, localization, and canonical Notch reporter activity. They showed absent surface expression, defective post-translational processing, and inability to initiate Notch signaling. These assays provide strong variant-level functional evidence but do not model multicellular heart, eye, or cochlear development. DOI: https://doi.org/10.1002/humu.21231; published May 2010; PMID **20437614**. (bauer2010jagged1(jag1)mutations pages 9-10, bauer2010jagged1(jag1)mutations pages 13-19)

No p.Cys234Tyr knock-in animal, patient-derived iPSC, organoid, zebrafish model, or human single-cell atlas specific to MONDO:0060713 was identified.

## Evidence assessment and knowledge-base cautions

The strongest syndrome-specific evidence consists of dominant familial segregation, the p.Cys234Tyr allele, the defining triad, normal liver function in nine studied relatives, and direct loss-of-function assays. Most quantitative clinical statistics come from broader ALGS cohorts and should be stored only as contextual—not disease-specific—evidence. The retrieved literature did not provide exact per-relative cardiac lesions, hearing subtype/severity, age-specific penetrance, allele frequency, standardized outcomes, or treatment-response data. Recent 2023–2024 research advances diagnosis of overlapping anterior-segment disorders and clarifies cochlear JAG1 biology, but it has not expanded the human case series for this particular MONDO entity. (reis2023alternativegeneticdiagnoses pages 2-4, haan2024jag1repressesnotch pages 1-3, bauer2010jagged1(jag1)mutations pages 9-10)

### Key publications

1. Le Caignec C, et al. **Familial deafness, congenital heart defects, and posterior embryotoxon caused by cysteine substitution in the first epidermal-growth-factor-like domain of Jagged 1.** *American Journal of Human Genetics* (2002). PMID **12022040**. The title itself records the primary human finding; Open Targets links it directly to MONDO:0060713 and JAG1. (OpenTargets Search: Deafness, congenital heart defects, and posterior embryotoxon)
2. Bauer RC, et al. **Jagged1 (JAG1) mutations in patients with tetralogy of Fallot or pulmonic stenosis.** *Human Mutation* 31:594–601; May 2010. DOI: https://doi.org/10.1002/humu.21231; PMID **20437614**. This study supplied the decisive p.Cys234Tyr functional evidence. (bauer2010jagged1(jag1)mutations pages 9-10, bauer2010jagged1(jag1)mutations pages 13-19)
3. Gilbert MA, et al. **Alagille syndrome mutation update.** *Human Mutation* 40:2197–2220; August 2019. DOI: https://doi.org/10.1002/humu.23879. This authoritative aggregation supports JAG1 haploinsufficiency, mutation frequencies, and lack of reliable genotype–phenotype prediction. (gilbert2019alagillesyndromemutation pages 1-5, gilbert2019alagillesyndromemutation pages 20-24, gilbert2019alagillesyndromemutation pages 24-27)
4. Reis LM, et al. **Alternative Genetic Diagnoses in Axenfeld–Rieger Syndrome Spectrum.** *Genes* 14:1948; October 2023. DOI: https://doi.org/10.3390/genes14101948. This supports broad sequencing for overlapping ocular-systemic phenotypes. (reis2023alternativegeneticdiagnoses pages 2-4)
5. de Haan S, et al. **Jag1 represses Notch activation in lateral supporting cells and inhibits an outer hair cell fate in the medial cochlea.** *Development* 151; November 2024. DOI: https://doi.org/10.1242/dev.202949. This is the most recent directly relevant mechanistic study. (haan2024jag1repressesnotch pages 1-3)

References

1. (OpenTargets Search: Deafness, congenital heart defects, and posterior embryotoxon): Open Targets Query (Deafness, congenital heart defects, and posterior embryotoxon, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (bauer2010jagged1(jag1)mutations pages 9-10): Robert C. Bauer, Ayanna O. Laney, Rosemarie Smith, Jennifer Gerfen, Jennifer J.D. Morrissette, Stacy Woyciechowski, Jennifer Garbarini, Kathleen M. Loomes, Ian D. Krantz, Zsolt Urban, Bruce D. Gelb, Elizabeth Goldmuntz, and Nancy B. Spinner. Jagged1 (jag1) mutations in patients with tetralogy of fallot or pulmonic stenosis. Human Mutation, 31:594-601, May 2010. URL: https://doi.org/10.1002/humu.21231, doi:10.1002/humu.21231. This article has 165 citations and is from a domain leading peer-reviewed journal.

3. (bauer2010jagged1(jag1)mutations pages 13-19): Robert C. Bauer, Ayanna O. Laney, Rosemarie Smith, Jennifer Gerfen, Jennifer J.D. Morrissette, Stacy Woyciechowski, Jennifer Garbarini, Kathleen M. Loomes, Ian D. Krantz, Zsolt Urban, Bruce D. Gelb, Elizabeth Goldmuntz, and Nancy B. Spinner. Jagged1 (jag1) mutations in patients with tetralogy of fallot or pulmonic stenosis. Human Mutation, 31:594-601, May 2010. URL: https://doi.org/10.1002/humu.21231, doi:10.1002/humu.21231. This article has 165 citations and is from a domain leading peer-reviewed journal.

4. (chitayat2016alagillesyndromeclinical pages 1-2): David Chitayat, Binita Kamath, and Maha Saleh. Alagille syndrome: clinical perspectives. The Application of Clinical Genetics, Volume 9:75-82, Jun 2016. URL: https://doi.org/10.2147/tacg.s86420, doi:10.2147/tacg.s86420. This article has 178 citations.

5. (gilbert2019alagillesyndromemutation pages 1-5): Melissa A. Gilbert, Robert C. Bauer, Ramakrishnan Rajagopalan, Christopher M. Grochowski, Grace Chao, Deborah McEldrew, James A. Nassur, Elizabeth B. Rand, Bryan L. Krock, Binita M. Kamath, Ian D. Krantz, David A. Piccoli, Kathleen M. Loomes, and Nancy B. Spinner. Alagille syndrome mutation update: comprehensive overview of<i>jag1</i>and<i>notch2</i>mutation frequencies and insight into missense variant classification. Human Mutation, 40:2197-2220, Aug 2019. URL: https://doi.org/10.1002/humu.23879, doi:10.1002/humu.23879. This article has 205 citations and is from a domain leading peer-reviewed journal.

6. (chitayat2016alagillesyndromeclinical pages 5-7): David Chitayat, Binita Kamath, and Maha Saleh. Alagille syndrome: clinical perspectives. The Application of Clinical Genetics, Volume 9:75-82, Jun 2016. URL: https://doi.org/10.2147/tacg.s86420, doi:10.2147/tacg.s86420. This article has 178 citations.

7. (chitayat2016alagillesyndromeclinical pages 2-4): David Chitayat, Binita Kamath, and Maha Saleh. Alagille syndrome: clinical perspectives. The Application of Clinical Genetics, Volume 9:75-82, Jun 2016. URL: https://doi.org/10.2147/tacg.s86420, doi:10.2147/tacg.s86420. This article has 178 citations.

8. (gilbert2019alagillesyndromemutation pages 20-24): Melissa A. Gilbert, Robert C. Bauer, Ramakrishnan Rajagopalan, Christopher M. Grochowski, Grace Chao, Deborah McEldrew, James A. Nassur, Elizabeth B. Rand, Bryan L. Krock, Binita M. Kamath, Ian D. Krantz, David A. Piccoli, Kathleen M. Loomes, and Nancy B. Spinner. Alagille syndrome mutation update: comprehensive overview of<i>jag1</i>and<i>notch2</i>mutation frequencies and insight into missense variant classification. Human Mutation, 40:2197-2220, Aug 2019. URL: https://doi.org/10.1002/humu.23879, doi:10.1002/humu.23879. This article has 205 citations and is from a domain leading peer-reviewed journal.

9. (gilbert2019alagillesyndromemutation pages 24-27): Melissa A. Gilbert, Robert C. Bauer, Ramakrishnan Rajagopalan, Christopher M. Grochowski, Grace Chao, Deborah McEldrew, James A. Nassur, Elizabeth B. Rand, Bryan L. Krock, Binita M. Kamath, Ian D. Krantz, David A. Piccoli, Kathleen M. Loomes, and Nancy B. Spinner. Alagille syndrome mutation update: comprehensive overview of<i>jag1</i>and<i>notch2</i>mutation frequencies and insight into missense variant classification. Human Mutation, 40:2197-2220, Aug 2019. URL: https://doi.org/10.1002/humu.23879, doi:10.1002/humu.23879. This article has 205 citations and is from a domain leading peer-reviewed journal.

10. (reis2023alternativegeneticdiagnoses pages 2-4): Linda M. Reis, David J. Amor, Raad A. Haddad, Catherine B. Nowak, Kim M. Keppler-Noreuil, Smith Ann Chisholm, and Elena V. Semina. Alternative genetic diagnoses in axenfeld–rieger syndrome spectrum. Genes, 14:1948, Oct 2023. URL: https://doi.org/10.3390/genes14101948, doi:10.3390/genes14101948. This article has 14 citations.

11. (haan2024jag1repressesnotch pages 1-3): Sandra de Haan, Agustin A. Corbat, Christopher R. Cederroth, Lisa G. Autrum, Simona Hankeova, Elizabeth C. Driver, Barbara Canlon, Matthew W. Kelley, and Emma R. Andersson. Jag1 represses notch activation in lateral supporting cells and inhibits an outer hair cell fate in the medial cochlea. Development, Nov 2024. URL: https://doi.org/10.1242/dev.202949, doi:10.1242/dev.202949. This article has 4 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Deafness_Congenital_Heart_Defects_And_Posterior_Embryotoxon-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.