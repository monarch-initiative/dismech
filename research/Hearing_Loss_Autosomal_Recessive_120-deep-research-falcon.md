---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:30:59.556082'
end_time: '2026-08-28T11:36:52.292348'
duration_seconds: 352.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hearing Loss Autosomal Recessive 120
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 22
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hearing_Loss_Autosomal_Recessive_120-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Recessive 120
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Recessive 120** covering all of the
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
- **Disease Name:** Hearing Loss Autosomal Recessive 120
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Recessive 120** covering all of the
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


# Hearing Loss, Autosomal Recessive 120 (DFNB120): Research Report

## Executive summary and evidence limits

**Hearing loss, autosomal recessive 120 (DFNB120)** is an ultra-rare Mendelian, nonsyndromic sensorineural hearing-loss disorder caused by biallelic pathogenic variants in **MINAR2**. The foundational 2022 study reported 13 affected people from four unrelated families; nine had congenital and four had prelingual severe-to-profound hearing loss, with progression documented in four. A 2025 report added an independently ascertained consanguineous family with two clinically affected brothers and a homozygous nonsense allele in the tested proband. Thus, the published human phenotype remains based on approximately 15 clinically affected individuals from five families, not a population cohort. (almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3)

The strongest mechanistic evidence is from knockout mouse and zebrafish experiments. MINAR2 loss disrupts cholesterol localization in sensory-hair-cell stereocilia, alters hair-bundle morphology and mechanotransduction, and ultimately causes hair-cell loss and progressive sensorineural hearing loss. Direct biochemical binding of MINAR2 to cholesterol remains proposed rather than definitively demonstrated. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

No DFNB120-specific interventional trial, approved molecular therapy, prevalence estimate, prospective natural-history cohort, or validated prognostic biomarker was identified. No disease-specific human paper from 2023–2024 was recovered; the principal 2024 development was recognition of MINAR2/DFNB120 in a review of genetically modified hearing-loss models. (wang2024geneticallymodifiedpigs pages 1-2)

| DFNB120 evidence summary | Key finding | Evidence type | Citation |
|---|---|---|---|
| Identifiers / synonyms | Hearing loss, autosomal recessive 120; autosomal recessive deafness-120; DFNB120; OMIM 620238; MONDO:0859374 | Disease-level curated + primary human report | (OpenTargets Search: Hearing loss autosomal recessive 120, almontashiri2025biallelicminar2variant pages 1-2) |
| Causal gene | **MINAR2** (membrane integral NOTCH2-associated receptor 2) is the established causal gene | Human genetic + curated association | (OpenTargets Search: Hearing loss autosomal recessive 120, carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2) |
| Inheritance | Autosomal recessive; biallelic loss-of-function/missense-splice-disrupting variants segregate with disease | Human family data | (carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3) |
| Known human cohort | Original report: **13 patients from 4 unrelated families** (2022); independent confirmation: **2 clinically affected siblings** (2025) | Human clinical genetics | (almontashiri2025biallelicminar2variant pages 1-2, carlson2022emergingcomplexitiesof pages 1-2) |
| Core phenotype | Bilateral **severe-to-profound nonsyndromic sensorineural hearing loss**; original cohort included **9 congenital** and **4 prelingual** cases | Human clinical | (almontashiri2025biallelicminar2variant pages 1-2) |
| Progression | Progressive SNHL reported in **4/13** patients in the original cohort; model data also support progressive hearing loss | Human + model | (almontashiri2025biallelicminar2variant pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18) |
| Newest reported variant | **NM_001257308.2:c.319A>T; p.Lys107\***, homozygous nonsense, predicted loss-of-function via nonsense-mediated decay; parents heterozygous; classified likely pathogenic | Human molecular genetics | (almontashiri2025biallelicminar2variant pages 2-3, almontashiri2025biallelicminar2variant pages 1-2) |
| Population frequency | p.Lys107\* observed as **2/767,859 heterozygotes** in **gnomAD v4.1**; no homozygotes reported in the cited report | Human population genetics | (almontashiri2025biallelicminar2variant pages 2-3, almontashiri2025biallelicminar2variant pages 1-2) |
| Mechanism | MINAR2 regulates **cholesterol distribution/homeostasis** in hair bundles; loss reduces stereociliary cholesterol, impairs mechanotransduction, and is associated with longer/thinner bundles and enlarged apical lysosomes | Model/mechanistic | (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18) |
| Models | **Mouse:** loss of Minar2 causes degeneration of hair cells and progressive SNHL; **zebrafish:** hearing loss with mechanotransduction defects and progressive reduction of inner-ear hair cells (to ~30% in adults) | Model organism | (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18) |
| Diagnostics used | Trio **whole-exome sequencing** with average **30×** depth, variant calling including SNV/CNV pipelines, and **Sanger confirmation** in the 2025 family; phenotype-driven interpretation under ACMG/ClinGen guidance | Human diagnostic evidence | (almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3) |
| Treatments / trials | No DFNB120-specific approved molecular therapy identified in cited evidence; **no disease-specific trials found** in the tool search; current care is inferred from general severe-profound SNHL management rather than disease-specific studies | Evidence gap / clinical practice extrapolation | (wang2024geneticallymodifiedpigs pages 1-2) |
| Epidemiology | Disease-specific prevalence/incidence are **not available**; currently documented human evidence is limited to **4 families/13 patients** in 2022 plus **1 additional family with 2 affected siblings** in 2025 | Human evidence summary | (almontashiri2025biallelicminar2variant pages 1-2) |
| Key evidence gaps | Missing/limited: robust prevalence, penetrance, founder effects, standardized natural history, genotype-phenotype correlations, long-term outcomes, and disease-specific therapeutic studies | Evidence gap | (almontashiri2025biallelicminar2variant pages 1-2, wang2024geneticallymodifiedpigs pages 1-2, carlson2022emergingcomplexitiesof pages 1-2) |


*Table: This table condenses the core human, molecular, and model-organism evidence for hearing loss autosomal recessive 120 (DFNB120). It highlights what is established versus what remains unknown, which is useful for rapid knowledge-base population.*

## 1. Disease information

### Definition

DFNB120 is a **bilateral, usually congenital or prelingual, severe-to-profound nonsyndromic sensorineural hearing loss (SNHL)** inherited in an autosomal-recessive manner. “Nonsyndromic” currently means that the reported human patients lacked consistent neurologic, visual, growth, dysmorphic, or systemic abnormalities; it does not exclude subtle manifestations that could emerge through longer surveillance. (carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2)

### Identifiers and synonyms

- **MONDO:** **MONDO:0859374**
- **OMIM phenotype:** **620238**
- **Preferred/synonymous names:** hearing loss, autosomal recessive 120; deafness, autosomal recessive 120; autosomal recessive deafness-120; **DFNB120**; MINAR2-related nonsyndromic sensorineural hearing loss.
- **Causal target:** **MINAR2**, Ensembl **ENSG00000186367**, approved name *membrane integral NOTCH2 associated receptor 2*. Open Targets associates both MINAR2 and OBSCN with this MONDO entry, but the disease-defining human segregation and functional evidence supports **MINAR2**; the lower-scoring OBSCN association should not be treated as an established second DFNB120 cause without independent disease-specific validation. (OpenTargets Search: Hearing loss autosomal recessive 120)
- **ICD-10/ICD-11 and MeSH:** no gene-specific DFNB120 code was found. Use broader congenital/hereditary or sensorineural hearing-loss coding, with the molecular diagnosis represented separately.
- **Orphanet:** no disease-specific Orpha code was established from the retrieved evidence.

The report is synthesized from **aggregated disease resources plus published family-level research**, not individual EHR records. The 2022 and 2025 papers contain patient-level pedigree and clinical data, while MONDO/Open Targets supply aggregated disease-level mappings. (OpenTargets Search: Hearing loss autosomal recessive 120, almontashiri2025biallelicminar2variant pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

The primary cause is **germline biallelic MINAR2 dysfunction**. Reported disease alleles include loss-of-function variants and a missense change shown to disrupt a donor splice site; they segregated with recessive hearing loss. The causal model is therefore deficient functional MINAR2 rather than infection, autoimmunity, trauma, or a recognized environmental exposure. (carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2)

The principal risk factors are:

1. Two pathogenic/likely pathogenic MINAR2 alleles in trans or homozygously.
2. An affected sibling or known carrier parents.
3. Consanguinity, which increases the chance that both parents carry the same rare allele; the 2025 parents were first cousins. (almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3)

No sex-specific susceptibility, modifier gene, protective human allele, founder effect, or environmental protective factor has been demonstrated. Noise, ototoxic drugs, infection, and aging can independently worsen hearing in any person, but no DFNB120-specific interaction has been quantified. Experimental zebrafish data suggest a biologically plausible cholesterol interaction: lowering cholesterol worsened, whereas experimentally increasing it rescued hair-cell defects. This is **model-organism evidence and not a recommendation for dietary, statin, or cholesterol supplementation therapy in humans**. (gao2022kiaa1024lminar2isessential pages 1-2)

## 3. Phenotypes

### Core phenotype

- **Bilateral sensorineural hearing loss** — clinical sign/functional deficit; suggested HPO **HP:0000407**.
- **Congenital hearing impairment** — onset descriptor; **HP:0008527**.
- **Prelingual hearing loss** — suggested HPO **HP:0012715**.
- **Severe hearing impairment** — **HP:0012714**.
- **Profound hearing impairment** — **HP:0012717**.
- **Progressive hearing impairment**, where documented — **HP:0001730**.
- **Nonsyndromic phenotype:** absence of a reproducible extra-auditory syndrome is a disease characterization, not a positive HPO phenotype.

In the original 13 patients, onset was congenital in 9/13 (69%) and prelingual in 4/13 (31%); all had severe-to-profound SNHL, while progression was reported in 4/13 (31%). Ages ranged from 4 to 80 years, and none had neurologic features. (almontashiri2025biallelicminar2variant pages 1-2)

The 2025 proband was a 10-year-old boy with congenital bilateral severe-to-profound SNHL; his 20-year-old brother had the same clinical phenotype. Both had age-appropriate cognition/neurodevelopment, normal growth, no dysmorphism, and unremarkable systemic examinations; the proband had no seizures or visual abnormality. (almontashiri2025biallelicminar2variant pages 1-2)

**Quality of life:** no DFNB120-specific EQ-5D, SF-36, PROMIS, speech-perception, educational, or employment data exist. Severe/profound early hearing loss is expected to affect auditory communication and language access without timely intervention, but that inference should not be stored as a measured DFNB120 outcome. A 2024 review notes that hereditary hearing loss broadly affects communication, cognition, education, and employment and cites a global annual economic burden of approximately US$980 billion for hearing loss overall—not DFNB120. (wang2024geneticallymodifiedpigs pages 1-2)

## 4. Genetic and molecular information

### Gene and alleles

- **Gene:** **MINAR2**; older experimental name **KIAA1024L**.
- **Protein:** membrane integral NOTCH2-associated receptor 2.
- **Inheritance/origin:** constitutional germline, autosomal recessive; no somatic disease mechanism is implicated.
- **Likely molecular effect:** loss of function through nonsense-mediated decay, frameshift/truncation, or splice disruption.

The original families carried multiple biallelic variants: two families shared a homozygous missense allele within the NOTCH receptor intracellular domain that disrupted donor splicing; the other families carried a nonsense allele in that domain and a frameshift affecting the transmembrane domain. Exact HGVS strings for these original alleles were not recoverable from the available full text and should be imported directly from the foundational paper/ClinVar rather than reconstructed. (almontashiri2025biallelicminar2variant pages 1-2)

The independently reported 2025 allele was **NM_001257308.2:c.319A>T; p.(Lys107\*)**, a homozygous exon-2 nonsense variant predicted to trigger nonsense-mediated decay. The proband was homozygous, both parents were heterozygous, and Sanger sequencing confirmed the finding. It was classified **likely pathogenic** under ACMG/AMP criteria **PVS1 + PM2**. The affected brother was not genetically tested, so his genotype is inferred from phenotype and pedigree rather than confirmed. (almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3)

In gnomAD v4.1, c.319A>T was observed heterozygously in **2/767,859 individuals** (reported minor-allele frequency approximately 0.0001%) and not homozygously. This is allele-specific evidence, not an estimate of DFNB120 carrier frequency. (almontashiri2025biallelicminar2variant pages 2-3, almontashiri2025biallelicminar2variant pages 1-2)

No validated modifier genes, disease-specific methylation signature, chromatin abnormality, recurrent copy-number variant, translocation, inversion, or aneuploidy has been reported. Large deletions involving MINAR2 remain diagnostically possible in principle and require CNV-sensitive analysis.

## 5. Environmental, lifestyle, and infectious information

DFNB120 is not known to be caused by toxins, radiation, pollution, diet, smoking, alcohol, occupation, or infection. These exposures remain alternative or additive causes of hearing loss rather than established causes of the Mendelian disorder. There is no evidence of zoonotic transmission or communicability. Because hair-bundle cholesterol homeostasis is implicated experimentally, systemic lipid-modifying exposures deserve research attention, but no human exposure-response data exist. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** biallelic MINAR2 loss → deficient MINAR2 at apical endomembranes/lysosomes and stereociliary membranes → impaired localization and homeostasis of accessible cholesterol in the hair bundle. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

**Intermediate:** reduced stereociliary cholesterol and altered membrane properties/trafficking → longer, thinner, structurally abnormal hair bundles; enlarged apical lysosomes; impaired mechanoelectrical transduction. Reduced accessible cholesterol also induces downstream **SREBP2-responsive genes**, consistent with compensatory cholesterol-homeostasis signaling. (gao2022kiaa1024lminar2isessential pages 17-18)

**Downstream:** sensory-hair-cell dysfunction and progressive loss → impaired conversion of acoustic vibration into receptor current → severe/profound SNHL. Adult zebrafish mutants had an approximately **30% reduction in inner-ear hair cells**. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

MINAR2 contains a conserved sequence resembling the caveolin cholesterol-binding CSD domain; overexpressed protein recruited cholesterol in vitro, mutation of predicted binding residues abolished recruitment, and AlphaFold-based docking gave plausible binding energy. However, the investigators explicitly stated that further biochemical work is needed to establish **direct** cholesterol binding and that the precise transport mechanism remains unclear. (gao2022kiaa1024lminar2isessential pages 17-18)

Suggested ontology annotations include:

- **GO biological process:** sensory perception of sound (**GO:0007605**); auditory receptor cell stereocilium organization (**GO:0060088**); mechanosensory transduction (**GO:0009582**); cholesterol homeostasis (**GO:0042632**); cholesterol transport (**GO:0030301**); lysosome organization (**GO:0007040**).
- **GO cellular component:** stereocilium (**GO:0032420**); stereocilium membrane (**GO:0060171**); lysosome (**GO:0005764**); endoplasmic-reticulum membrane (**GO:0005789**).
- **Cell Ontology:** hair cell (**CL:0000202**), with cochlear inner and outer hair-cell subclasses where supported.
- **CHEBI:** cholesterol (**CHEBI:16113**).

No disease-specific human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omics signature has been established. The available expression and SREBP2 results are experimental-model findings. Immune activation, fibrosis, ischemia, and autoimmunity are not established mechanisms.

## 7. Anatomical structures affected

The primary organ is the **inner ear**, particularly the cochlear sensory epithelium/organ of Corti and its mechanosensory hair cells. At the subcellular level, the critical sites are apical hair bundles, actin-rich stereocilia and their membranes, plus apical endomembrane/lysosomal compartments. Suggested terms are **UBERON:0001844** (cochlea), **UBERON:0002227** (organ of Corti), **UBERON:0001846** (internal ear), and the GO/CL terms above. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

Human disease is consistently bilateral. No reproducible vestibular, auditory-nerve, central nervous-system, retinal, or other-organ involvement has been established. Although MINAR2 is expressed in brain and other tissues, expression alone is not evidence of disease involvement. (carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2)

## 8. Temporal development

Onset is congenital or prelingual and therefore chronic/lifelong. Some patients already have severe/profound impairment at ascertainment; at least 4/13 original cases showed progression, but no standardized stages or annual threshold-change estimates are available. (almontashiri2025biallelicminar2variant pages 1-2)

There is no evidence of spontaneous remission or a relapsing-remitting course. The critical clinical period is early infancy and childhood because auditory access supports speech and language development. Newborn identification, prompt etiologic work-up, and early rehabilitation are therefore important even though no DFNB120-specific intervention window has been experimentally defined.

## 9. Inheritance, penetrance, and population

Inheritance is **autosomal recessive**. For two confirmed carrier parents, each pregnancy conventionally has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of an unaffected non-carrier, subject to correct variant classification and parentage. Consanguinity can increase recurrence by increasing shared rare alleles, as illustrated by the first-cousin parents in the 2025 family. (almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3)

Penetrance appears high among reported biallelic individuals, but ascertainment is strongly phenotype-driven and the sample is too small to estimate penetrance or expressivity statistically. Severity is relatively consistent, while onset/progression varies. Genetic anticipation and germline mosaicism have not been reported.

Disease-specific prevalence, incidence, carrier frequency, sex ratio, geographic distribution, and ethnic enrichment are unknown. Published evidence comprises four families/13 patients in 2022 and one additional family/two affected brothers in 2025. Consequently, “15 patients” describes the identified literature, not worldwide prevalence. (almontashiri2025biallelicminar2variant pages 1-2)

## 10. Diagnostics

### Clinical assessment

Evaluation should establish type, laterality, severity, and course using age-appropriate behavioral audiometry and objective testing such as auditory brainstem response and otoacoustic emissions. Tympanometry helps exclude conductive disease. Speech/language assessment documents functional consequences. Imaging is not diagnostic for DFNB120 but CT/MRI may be indicated before cochlear implantation or when anatomy/neurologic disease is suspected.

### Molecular confirmation

A practical workflow is:

1. Comprehensive hereditary hearing-loss panel that includes **MINAR2**, with deletion/duplication detection.
2. Exome or genome sequencing when panel testing is negative or the phenotype/pedigree is atypical.
3. Confirm candidate variants and phase/segregation in parents and affected relatives.
4. Apply ACMG/AMP/ClinGen criteria and check ClinVar and current population databases.

The 2025 study used trio WES from blood, paired-end Illumina sequencing at mean **30×** depth, GRCh37/hg19 and mitochondrial alignment, SNV/CNV calling with DRAGEN, Manta, and internal algorithms, followed by Sanger confirmation. This demonstrates WES utility but not comparative superiority over panels or WGS. (almontashiri2025biallelicminar2variant pages 1-2, almontashiri2025biallelicminar2variant pages 2-3)

WGS can improve coverage of poorly captured exons, intronic splice variants, and structural variants. CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion assays are not first-line disease-specific tests unless clinical or sequencing findings suggest another diagnosis. RNA analysis may resolve suspected splice variants but is not a validated routine DFNB120 assay.

Differential diagnoses include common recessive nonsyndromic genes such as **GJB2, SLC26A4, OTOF, TMC1, MYO15A**, congenital CMV, ototoxic exposure, inner-ear malformations, auditory neuropathy, and syndromic hearing-loss disorders. Phenotype alone cannot reliably distinguish DFNB120; molecular confirmation is necessary.

## 11. Outcome and prognosis

Available evidence suggests lifelong auditory disability but not shortened survival. No mortality signal, life-expectancy reduction, 5-/10-year survival statistic, or disease-specific hospitalization rate has been reported. Neurologic disease was absent even in original patients up to age 80, arguing against simply transferring the Parkinson-like mouse phenotype to humans. (carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2)

The major morbidity is severe/profound hearing impairment and its downstream communication burden. Prognosis depends on baseline severity, progression, age at auditory intervention, rehabilitation access, and response to amplification or implantation, but no DFNB120-specific outcome series exists. Residual hearing may deteriorate in some patients; serial audiometry is therefore appropriate. There are no validated molecular prognostic biomarkers.

## 12. Treatment

No pharmacologic, gene, RNA, cell, immunologic, or gene-editing therapy is approved specifically for DFNB120. No DFNB120/MINAR2 interventional trial was identified in the targeted ClinicalTrials.gov search.

Current care follows severe/profound pediatric SNHL practice:

- hearing aids where usable residual hearing exists;
- cochlear-implant evaluation when amplification provides insufficient benefit;
- speech-language/auditory rehabilitation and educational accommodations;
- sign-language access according to family/patient preferences;
- serial audiology to document progression;
- multidisciplinary otology, audiology, genetics, and developmental follow-up.

A 2024 review characterizes hearing aids and cochlear implants as traditional interventions for hereditary deafness and notes that they do not restore natural biologic hearing. It identifies inner-ear gene therapy as promising but still requiring improved vectors, editing strategies, delivery, and surgery. These are field-level observations, not DFNB120 treatment evidence. (wang2024geneticallymodifiedpigs pages 1-2)

Suggested NCIt concepts include **Hearing Aid (C157197)**, **Cochlear Implantation**/cochlear implant concepts, **Genetic Counseling**, **Speech Therapy**, and **Gene Therapy** for experimental annotation; local NCIt release identifiers should be verified before database import. Cholesterol manipulation rescued zebrafish cellular defects, but translation is premature because systemic cholesterol alteration could have unrelated risks and the necessary cochlear exposure is unknown. (gao2022kiaa1024lminar2isessential pages 1-2)

## 13. Prevention

The genotype cannot presently be prevented through lifestyle modification. Primary reproductive options after identifying familial variants include genetic counseling, partner/carrier testing, prenatal diagnosis, and preimplantation genetic testing. Cascade testing can identify carrier relatives. Secondary prevention comprises newborn hearing screening, rapid diagnostic audiology, and early molecular testing. Tertiary prevention comprises prompt auditory rehabilitation, language access, educational support, hearing conservation, and avoidance of unnecessary ototoxic exposure.

No vaccine, medication, dietary regimen, or prophylactic procedure prevents DFNB120. Standard vaccination and congenital-infection prevention may reduce other causes of hearing loss but do not prevent MINAR2-related disease.

## 14. Other species and natural disease

Experimental orthologues are established in **Mus musculus** (NCBI Taxon **10090**) and **Danio rerio** (Taxon **7955**). Minar2-null mice develop progressive SNHL with hair-cell degeneration; they also show bradykinesia, rigidity, loss of tyrosine-hydroxylase-positive neurons, and α-synuclein upregulation—features not observed in reported humans. This interspecies discordance limits direct syndromic extrapolation. (carlson2022emergingcomplexitiesof pages 1-2, almontashiri2025biallelicminar2variant pages 1-2)

The zebrafish **minar2fs139** mutant has impaired mechanotransduction, abnormal hair bundles and enlarged apical lysosomes, with progressive adult hair-cell reduction. Its phenotype is milder than the mouse phenotype, plausibly because zebrafish continue generating hair cells into adulthood and may exhibit genetic compensation. (gao2022kiaa1024lminar2isessential pages 17-18)

No naturally occurring veterinary DFNB120-equivalent disease, breed predisposition, VBO identifier, or zoonotic potential was identified. These are engineered or laboratory genetic models, not transmissible disease.

## 15. Model organisms and research applications

### Mouse

The knockout mouse recapitulates progressive SNHL and hair-cell degeneration and supports mammalian cochlear causality. It is useful for longitudinal ABR, cochlear histology, delivery studies, and eventual MINAR2 replacement experiments. Its limitation is additional Parkinson-like motor/neural pathology absent in humans; model phenotypes therefore cannot automatically populate the human disease entry. (carlson2022emergingcomplexitiesof pages 1-2)

### Zebrafish

The minar2fs139 model recapitulates defective auditory/vestibular hair-cell mechanotransduction, stereociliary cholesterol depletion, abnormal bundle morphology, lysosomal enlargement, and progressive hair-cell loss. Pharmacologic cholesterol lowering worsened and cholesterol elevation rescued defects, making the model useful for pathway dissection and compound screening. Continuous adult hair-cell regeneration and possible genetic compensation limit quantitative translation to human cochlear disease. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

### Cellular and computational systems

Cultured-cell overexpression localized MINAR2 mainly to lysosomes and recruited cholesterol. Tagged protein in hair cells localized to apical endomembranes and stereociliary membranes. AlphaFold-based docking supports, but does not prove, a cholesterol-binding interface. No patient-derived iPSC hair-cell model, human cochlear organoid, porcine MINAR2 model, CRISPR therapeutic screen, or disease-specific spatial/single-cell atlas was identified. (gao2022kiaa1024lminar2isessential pages 1-2, gao2022kiaa1024lminar2isessential pages 17-18)

## Key primary sources and dates

1. **Bademci G, et al.** “Mutations in MINAR2 encoding membrane integral NOTCH2-associated receptor 2 cause deafness in humans and mice.” *PNAS*. Published June 2022. **PMID: 35727972**. DOI/URL: https://doi.org/10.1073/pnas.2204084119. The central human conclusion is summarized by the exact statement that the variants “led to loss of function of the gene and were perfectly coinherited with autosomal recessive hearing loss.” (carlson2022emergingcomplexitiesof pages 1-2)
2. **Gao G, et al.** “Kiaa1024L/Minar2 is essential for hearing by regulating cholesterol distribution in hair bundles.” *eLife* 11:e80865. Published **1 November 2022**. DOI/URL: https://doi.org/10.7554/eLife.80865. Exact abstract statement: “Lowering cholesterol levels aggravates, while increasing cholesterol levels rescues the hair cell defects in the kiaa1024L/minar2 mutant.” (gao2022kiaa1024lminar2isessential pages 1-2)
3. **Carlson RJ, Avraham KB.** “Emerging complexities of the mouse as a model for human hearing loss.” *PNAS*. Published **12 August 2022**. DOI/URL: https://doi.org/10.1073/pnas.2211351119. This authoritative commentary emphasizes that mouse motor deficits “were not present in even the oldest humans with comparably severe mutations in MINAR2.” (carlson2022emergingcomplexitiesof pages 1-2)
4. **Wang X, et al.** “Genetically modified pigs: Emerging animal models for hereditary hearing loss.” *Zoological Research* 45:284–291. Published online **6 December 2023**; issue **March 2024**. DOI/URL: https://doi.org/10.24272/j.issn.2095-8137.2023.231. This is a recent field review, not a new DFNB120 human cohort. (wang2024geneticallymodifiedpigs pages 1-2)
5. **Almontashiri NAM.** “Biallelic MINAR2 variant is associated with nonsyndromic severe to profound sensorineural hearing loss.” *Human Genome Variation* 12. Published online **23 October 2025**. DOI/URL: https://doi.org/10.1038/s41439-025-00328-w. Exact abstract conclusion: “Our study provides the first independent confirmation of the MINAR2-related SNHL.” (almontashiri2025biallelicminar2variant pages 1-2)

## Knowledge-base confidence assessment

**High confidence:** MINAR2 causality; autosomal-recessive inheritance; bilateral congenital/prelingual severe-to-profound nonsyndromic SNHL; stereociliary/hair-cell involvement; cholesterol-homeostasis mechanism in experimental models.

**Moderate confidence:** progressive human course, because it was documented in only 4/13 original patients; high penetrance, because all reported biallelic subjects were ascertained through hearing-loss families.

**Low or unavailable:** disease prevalence/incidence, carrier frequency, founder variants, sex effects, environmental modifiers, exact longitudinal prognosis, human biochemical biomarkers, extra-auditory risk, treatment-response rates, and efficacy of cholesterol-directed or gene therapies. These fields should be recorded as **unknown**, not inferred from general hearing-loss literature or animal models.

References

1. (almontashiri2025biallelicminar2variant pages 1-2): Naif A. M. Almontashiri. Biallelic minar2 variant is associated with nonsyndromic severe to profound sensorineural hearing loss. Human Genome Variation, Oct 2025. URL: https://doi.org/10.1038/s41439-025-00328-w, doi:10.1038/s41439-025-00328-w. This article has 0 citations.

2. (almontashiri2025biallelicminar2variant pages 2-3): Naif A. M. Almontashiri. Biallelic minar2 variant is associated with nonsyndromic severe to profound sensorineural hearing loss. Human Genome Variation, Oct 2025. URL: https://doi.org/10.1038/s41439-025-00328-w, doi:10.1038/s41439-025-00328-w. This article has 0 citations.

3. (gao2022kiaa1024lminar2isessential pages 1-2): Ge Gao, Shuyu Guo, Quan Zhang, Hefei Zhang, Cuizhen Zhang, and Gang Peng. Kiaa1024l/minar2 is essential for hearing by regulating cholesterol distribution in hair bundles. Nov 2022. URL: https://doi.org/10.7554/elife.80865, doi:10.7554/elife.80865. This article has 8 citations and is from a domain leading peer-reviewed journal.

4. (gao2022kiaa1024lminar2isessential pages 17-18): Ge Gao, Shuyu Guo, Quan Zhang, Hefei Zhang, Cuizhen Zhang, and Gang Peng. Kiaa1024l/minar2 is essential for hearing by regulating cholesterol distribution in hair bundles. Nov 2022. URL: https://doi.org/10.7554/elife.80865, doi:10.7554/elife.80865. This article has 8 citations and is from a domain leading peer-reviewed journal.

5. (wang2024geneticallymodifiedpigs pages 1-2): Xiao Wang, Tian-Xia Liu, Ying Zhang, Liang-Wei Xu, Shuo-Long Yuan, A-Long Cui, Wei-Wei Guo, Yan-Fang Wang, Shi-Ming Yang, and Jian-Guo Zhao. Genetically modified pigs: emerging animal models for hereditary hearing loss. Zoological Research, 45:284-291, Mar 2024. URL: https://doi.org/10.24272/j.issn.2095-8137.2023.231, doi:10.24272/j.issn.2095-8137.2023.231. This article has 6 citations.

6. (OpenTargets Search: Hearing loss autosomal recessive 120): Open Targets Query (Hearing loss autosomal recessive 120, 16 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (carlson2022emergingcomplexitiesof pages 1-2): Ryan J. Carlson and Karen B. Avraham. Emerging complexities of the mouse as a model for human hearing loss. Proceedings of the National Academy of Sciences of the United States of America, Aug 2022. URL: https://doi.org/10.1073/pnas.2211351119, doi:10.1073/pnas.2211351119. This article has 19 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hearing_Loss_Autosomal_Recessive_120-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.