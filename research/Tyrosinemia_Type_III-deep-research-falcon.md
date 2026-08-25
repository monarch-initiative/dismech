---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-23T00:56:18.194969'
end_time: '2026-08-23T01:04:35.522519'
duration_seconds: 497.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tyrosinemia Type III
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Tyrosinemia_Type_III-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tyrosinemia Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tyrosinemia Type III** covering all of the
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
- **Disease Name:** Tyrosinemia Type III
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Tyrosinemia Type III** covering all of the
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


# Tyrosinemia Type III: Disease-Characteristics Research Report

**Evidence cutoff:** searches prioritized literature through 2024. Because tyrosinemia type III (HT3) is exceptionally rare, most human evidence consists of case reports, small series, and retrospective literature reviews rather than cohorts or trials. Statements about treatment, penetrance, and prognosis should therefore be interpreted cautiously.

## Executive summary

Tyrosinemia type III is an autosomal-recessive amino-acid disorder caused by biallelic loss-of-function variants in **HPD**, encoding 4-hydroxyphenylpyruvate dioxygenase. HPD normally converts 4-hydroxyphenylpyruvate to homogentisate in hepatic tyrosine catabolism. Deficiency causes persistent hypertyrosinemia and urinary excretion of 4-hydroxyphenylpyruvate, 4-hydroxyphenyllactate, and 4-hydroxyphenylacetate. Unlike tyrosinemia type I, HT3 ordinarily does not cause progressive hepatorenal failure or succinylacetone accumulation. Neurologic expression is heterogeneous: developmental delay, intellectual disability, seizures, ataxia, and autistic features have been reported, but a substantial fraction of molecularly confirmed patients are asymptomatic. Five of 16 patients summarized in a 2022 review were asymptomatic despite biochemical abnormalities. No reliable genotype–phenotype relationship, population prevalence, standardized treatment guideline, disease-specific clinical trial, or validated prognostic biomarker exists. (szymanska2015tyrosinemiatypeiii pages 3-3, beyzaei2022themutationspectrum pages 3-5, alsharhan2020disordersofphenylalanine pages 31-33)

The principal ontology-ready facts are summarized below.

| domain | established finding | suggested ontology identifiers/terms | evidence strength/limitations |
|---|---|---|---|
| Disease identity | Tyrosinemia type III is an ultra-rare inborn error of tyrosine metabolism caused by deficiency of 4-hydroxyphenylpyruvate dioxygenase; recognized disease identifiers include MONDO:0010162, OMIM:276710, Orphanet:69723 (OpenTargets Search: Tyrosinemia type III-HPD, beyzaei2022themutationspectrum pages 1-2) | MONDO:0010162; OMIM:276710; Orphanet:69723; suggested label synonym: “4-hydroxyphenylpyruvate dioxygenase deficiency” | Strong for identifiers/disease concept from curated resources and review; rarity means phenotype boundaries remain incompletely defined (OpenTargets Search: Tyrosinemia type III-HPD, beyzaei2022themutationspectrum pages 1-2) |
| Synonyms | Reported names include tyrosinemia type III, tyrosinemia type 3, hereditary hypertyrosinemia type III, and 4-hydroxyphenylpyruvate dioxygenase deficiency (szymanska2015tyrosinemiatypeiii pages 1-3, endo2003animalmodelsreveal pages 4-5) | Suggested synonyms only; exact ontology synonym set should be verified in MONDO/Orphanet | Moderate; terminology varies across case reports and older literature (szymanska2015tyrosinemiatypeiii pages 1-3, endo2003animalmodelsreveal pages 4-5) |
| Etiology/gene | Causal gene is HPD, encoding 4-hydroxyphenylpyruvate dioxygenase, in the tyrosine catabolic pathway (OpenTargets Search: Tyrosinemia type III-HPD, endo2003animalmodelsreveal pages 1-2, xie2019hpddegradationregulated pages 1-2) | HPD (HGNC symbol); suggested functional term: loss of function/absent or deficient HPD activity; suggested pathway: tyrosine catabolic process | Strong for gene-disease link, including ClinGen-definitive curation noted in Open Targets-linked evidence; variant-level functional data are sparse for many alleles (OpenTargets Search: Tyrosinemia type III-HPD) |
| Inheritance | Autosomal recessive inheritance with biallelic HPD variants (szymanska2015tyrosinemiatypeiii pages 1-3, sarkargar2023acompoundheterozygous pages 1-3, OpenTargets Search: Tyrosinemia type III-HPD, beyzaei2022themutationspectrum pages 1-2) | Suggested inheritance term: autosomal recessive inheritance [HPO term suggested, exact ID not confirmed here] | Strong for inheritance; penetrance/expressivity remain uncertain because some patients are asymptomatic (beyzaei2022themutationspectrum pages 3-5) |
| Molecular defect | HPD normally converts 4-hydroxyphenylpyruvate to homogentisate; deficiency blocks this step and causes accumulation of upstream tyrosine-related metabolites without the toxic downstream metabolites typical of type I disease (szymanska2015tyrosinemiatypeiii pages 3-3, endo2003animalmodelsreveal pages 1-2, xie2019hpddegradationregulated pages 1-2) | Suggested GO term: tyrosine catabolic process; suggested CHEBI terms: L-tyrosine, 4-hydroxyphenylpyruvate, homogentisate | Strong for pathway position; downstream neurotoxicity mechanism in humans remains unresolved (szymanska2015tyrosinemiatypeiii pages 3-3, xie2019hpddegradationregulated pages 1-2) |
| Pathogenic variants | Review of published patients found 11 HPPD/HPD variants in 16 patients by 2022: 7 missense, 2 nonsense, 1 splice-site, 1 frameshift; recurrent p.Tyr160Cys reported in 2 families; later 2023 case added compound heterozygous p.W25Ter and p.T138M (beyzaei2022themutationspectrum pages 3-5, sarkargar2023acompoundheterozygous pages 1-3) | Suggested sequence consequence terms: missense variant, nonsense variant, splice donor/acceptor variant, frameshift variant | Moderate-strong for published spectrum; many are private variants and genotype-phenotype correlation is not established (beyzaei2022themutationspectrum pages 3-5) |
| Core biochemical phenotype | Elevated blood/serum tyrosine with increased urinary excretion of 4-hydroxyphenylpyruvate, 4-hydroxyphenyllactate, and 4-hydroxyphenylacetate/related p-hydroxyphenyl derivatives is characteristic (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33, endo2003animalmodelsreveal pages 2-2) | Suggested HPO: Hypertyrosinemia [exact ID not confirmed]; suggested lab terms: increased urinary 4-hydroxyphenylpyruvate, increased urinary 4-hydroxyphenyllactate, increased urinary 4-hydroxyphenylacetate | Strong for biochemical signature; exact analyte nomenclature varies by report (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33) |
| Typical tyrosine levels | Reported blood tyrosine values are often ~350–650 μmol/L; examples include 425–535 μmol/L in an asymptomatic girl and 709 μmol/L neonatally in a 2023 Iranian case (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33, sarkargar2023acompoundheterozygous pages 1-3) | Suggested quantitative lab annotation rather than ontology term | Moderate; based on small case series/case reports with assay/reference-range variation (szymanska2015tyrosinemiatypeiii pages 1-3, sarkargar2023acompoundheterozygous pages 1-3) |
| Neurologic phenotypes | Neurologic manifestations reported across cases include developmental delay/psychomotor retardation, intellectual disability/mental retardation, seizures/convulsions, ataxia, and autism; however, some genetically confirmed individuals are asymptomatic (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33, endo2003animalmodelsreveal pages 2-2, beyzaei2022themutationspectrum pages 3-5) | Suggested HPO terms: Developmental delay; Psychomotor retardation; Intellectual disability; Seizure; Ataxia; Autistic behavior [exact IDs not confirmed here] | Moderate; recurrently reported but case numbers are tiny and causality of neurologic findings versus ascertainment bias remains debated (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33) |
| Asymptomatic presentation | A substantial minority of published patients were asymptomatic despite persistent biochemical abnormalities; 5 of 16 patients in the 2022 review were asymptomatic (szymanska2015tyrosinemiatypeiii pages 1-3, szymanska2015tyrosinemiatypeiii pages 3-3, beyzaei2022themutationspectrum pages 3-5) | Suggested phenotype annotation: asymptomatic hypertyrosinemia [suggestion only] | Strong for existence of asymptomatic cases; weak for predicting who will remain asymptomatic long term (beyzaei2022themutationspectrum pages 3-5) |
| Renal phenotype | Classical liver and kidney dysfunction are generally absent, but recurrent proteinuria has been reported in at least one asymptomatic patient and increased propensity for proteinuria has been noted (szymanska2015tyrosinemiatypeiii pages 3-3, sarkargar2023acompoundheterozygous pages 1-3) | Suggested HPO: Proteinuria [exact ID not confirmed] | Weak-moderate; renal involvement is not a consistent core feature and is based on limited case-level evidence (szymanska2015tyrosinemiatypeiii pages 3-3, sarkargar2023acompoundheterozygous pages 1-3) |
| Hepatic phenotype | Unlike tyrosinemia type I, hepatocellular injury is typically absent; reports emphasize no liver damage as a distinguishing feature, though isolated neonatal hepatitis has been described in a 2023 case report (alsharhan2020disordersofphenylalanine pages 31-33, sarkargar2023acompoundheterozygous pages 1-3, endo2003animalmodelsreveal pages 2-2) | Suggested differential annotation rather than core phenotype; UBERON suggestion: liver | Moderate; absence of hepatic disease is a useful differentiator, but occasional hepatic presentations may reflect ascertainment complexity or comorbidity (sarkargar2023acompoundheterozygous pages 1-3) |
| Anatomy/organs | Main tissues relevant to disease biology are liver and kidney, where HPD is mainly expressed; nervous system/brain involvement is implicated clinically by neurologic symptoms (endo2003animalmodelsreveal pages 1-2, beyzaei2022themutationspectrum pages 1-2) | Suggested UBERON: liver, kidney, brain; suggested body systems: metabolic, nervous | Strong for organ expression/pathway anatomy; direct tissue pathology data in humans are sparse (endo2003animalmodelsreveal pages 1-2, beyzaei2022themutationspectrum pages 1-2) |
| Cell types | Human mechanistic literature suggests hepatocytes as primary metabolic cell type; neurons are implicated by neurologic phenotype; one paper also discusses neutrophils/neurons in relation to nitric oxide release, but this is limited evidence (sarkargar2023acompoundheterozygous pages 3-5) | Suggested CL terms: hepatocyte, neuron; suggested CL term: neutrophil (exploratory) | Moderate for hepatocyte/neuron; weak for neutrophil relevance to disease mechanism (sarkargar2023acompoundheterozygous pages 3-5) |
| Subcellular compartments | Disease mechanism involves enzyme deficiency in metabolic pathways; a mouse/mechanistic study identified regulation of HPD protein stability through phosphorylation, ubiquitination, and proteasomal degradation (TTC36-STK33-PELI1 axis) (xie2019hpddegradationregulated pages 1-2, xie2019hpddegradationregulated pages 6-7) | Suggested GO cellular component terms: cytosol/cytoplasm, proteasome complex; suggested process terms: protein ubiquitination, proteasomal protein catabolic process | Moderate for HPD regulation biology, but this evidence is mainly experimental/model-based and not specific to human inherited alleles (xie2019hpddegradationregulated pages 1-2, xie2019hpddegradationregulated pages 6-7) |
| Diagnosis | Diagnostic approach relies on metabolic screening showing elevated tyrosine plus urinary p-hydroxyphenyl metabolites, followed by molecular confirmation of biallelic HPD variants by targeted sequencing, gene panel, WES, or Sanger confirmation (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33, sarkargar2023acompoundheterozygous pages 1-3) | Suggested diagnostic categories: plasma amino acids, urine organic acids, molecular genetic testing | Strong for core diagnostic workflow; no universally standardized diagnostic criteria specific to type III were identified (alsharhan2020disordersofphenylalanine pages 31-33) |
| Differential diagnosis | Important differentials include tyrosinemia type I, tyrosinemia type II, transient neonatal tyrosinemia, and hawkinsinuria; type III differs from type I by lack of succinylacetone accumulation/hepatorenal disease and from type II by generally lower tyrosine levels and absence of corneal/skin disease (szymanska2015tyrosinemiatypeiii pages 3-3, endo2003animalmodelsreveal pages 4-5, alsharhan2020disordersofphenylalanine pages 31-33) | Suggested related disease mappings: tyrosinemia type I, tyrosinemia type II, hawkinsinuria, transient neonatal tyrosinemia [exact ontology IDs not confirmed] | Moderate; differential framework is well supported in reviews, but formal criteria are not standardized for this ultra-rare disorder (alsharhan2020disordersofphenylalanine pages 31-33) |
| Newborn screening | Type III can be detected after elevated tyrosine on newborn screening, but routine screening specificity is limited because tyrosine elevation is nonspecific; published cases include neonatal-screen-detected patients, while some regions report no dedicated HT3 screening program (szymanska2015tyrosinemiatypeiii pages 3-3, beyzaei2022themutationspectrum pages 5-6, sarkargar2023acompoundheterozygous pages 3-5) | Suggested screening annotation: elevated tyrosine on tandem MS/MS newborn screening | Moderate; real-world implementation exists indirectly through tyrosine elevation, but population screening performance metrics for HT3 are not established here (beyzaei2022themutationspectrum pages 5-6, sarkargar2023acompoundheterozygous pages 3-5) |
| Treatment | Main reported treatment is dietary restriction of tyrosine and phenylalanine; one review cites ascorbic acid supplementation (50 mg/day) with normalization of tyrosine and improvement of seizures in a case; some asymptomatic patients were not treated and remained well (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33, sarkargar2023acompoundheterozygous pages 3-5) | Suggested NCIT intervention terms: Dietary modification; Low phenylalanine diet; Low tyrosine diet; Ascorbic acid supplementation | Moderate; evidence is based on case reports/experience only, and benefit for long-term neuroprotection is uncertain (alsharhan2020disordersofphenylalanine pages 31-33) |
| Monitoring/outcomes | Follow-up generally centers on plasma tyrosine, urinary metabolites, neurologic/developmental assessment, and growth; outcomes are variable, with some patients improving on diet and others remaining asymptomatic without clear progression (szymanska2015tyrosinemiatypeiii pages 1-3, sarkargar2023acompoundheterozygous pages 3-5, alsharhan2020disordersofphenylalanine pages 31-33) | Suggested monitoring concepts: plasma tyrosine, urine organic acids, developmental assessment | Weak-moderate; no formal longitudinal natural-history dataset or validated outcome measures were identified (sarkargar2023acompoundheterozygous pages 3-5, alsharhan2020disordersofphenylalanine pages 31-33) |
| Epidemiology | Ultra-rare disorder: only 13 cases were noted by 2015, 16 patients by the 2022 variant review, and about 18 cases cited in a 2023 case report; no robust prevalence or incidence estimates were identified (szymanska2015tyrosinemiatypeiii pages 1-3, beyzaei2022themutationspectrum pages 3-5, sarkargar2023acompoundheterozygous pages 3-5) | Suggested epidemiology annotation: ultra-rare Mendelian disease | Moderate for approximate published case counts; weak for true prevalence/incidence because underdiagnosis is likely (szymanska2015tyrosinemiatypeiii pages 3-3, beyzaei2022themutationspectrum pages 3-5) |
| Population distribution | Reported patients/variants have come from Europe and parts of Asia, including Portugal, Turkey, Sweden, Poland, Japan, Iran, and China; no data were noted from North/Central America, Africa, Australia, or Oceania in the 2022 review (beyzaei2022themutationspectrum pages 3-5) | Suggested demographic annotation only; no founder effect established for type III | Moderate for published geographic distribution; reflects publication bias rather than true population risk (beyzaei2022themutationspectrum pages 3-5) |
| Modifier/protective factors | No validated genetic protective variants, modifier genes, or environmental protective factors specific to human HT3 were identified; genotype-phenotype correlation remains unclear (beyzaei2022themutationspectrum pages 3-5) | None established; leave ontology mapping blank/NA | Weak due to lack of evidence (beyzaei2022themutationspectrum pages 3-5) |
| Prevention/genetic counseling | Primary prevention is not established; secondary prevention may occur through newborn screening flagging elevated tyrosine; tertiary prevention is dietary/metabolic management. Carrier testing, family screening, and prenatal testing are plausible for known familial HPD variants, but disease-specific protocols were not well detailed in retrieved evidence (sarkargar2023acompoundheterozygous pages 1-3, beyzaei2022themutationspectrum pages 5-6) | Suggested counseling concepts: carrier testing, cascade testing, prenatal diagnosis [suggestions only] | Weak-moderate; inferred from Mendelian genetics and review conclusions rather than disease-specific prospective studies (beyzaei2022themutationspectrum pages 5-6) |
| Human evidence quality | Evidence base is dominated by case reports, small series, and reviews; 2022 review explicitly states genotype-phenotype correlation cannot be clearly concluded due to small numbers and private mutations (beyzaei2022themutationspectrum pages 3-5) | Evidence tag suggestion: human clinical case report/series | Strong statement about limitation; this constrains confidence in prognosis and management recommendations (beyzaei2022themutationspectrum pages 3-5) |
| Animal/models | HPD-deficient mice model hypertyrosinemia with elevated tyrosine and urinary metabolites, and generally lack the severe visceral injury seen in type I; newer mechanistic mouse work links reduced hepatic HPD to tyrosinemia and hippocampal neuron injury via TTC36-STK33-PELI1 regulation. Drosophila nutrigenomics work lists tyrosinemia type III among amino-acid-disorder models/platform efforts (endo2003animalmodelsreveal pages 1-2, xie2019hpddegradationregulated pages 1-2, martelli2024identifyingpotentialdietary pages 1-3, martelli2024identifyingpotentialdietary pages 29-30) | Suggested model annotations: mouse knockout model; Drosophila disease model/platform | Moderate for mechanistic utility; mouse neurologic findings may not map directly to human HT3 clinical variability (xie2019hpddegradationregulated pages 1-2) |


*Table: This table provides a compact, ontology-ready summary of Tyrosinemia type III, covering identifiers, genetics, biochemical and clinical features, anatomy, diagnosis, treatment, epidemiology, and model systems. It emphasizes where evidence is strong versus where the ultra-rare nature of the disease leaves major gaps.*

## 1. Disease information

### Definition and identifiers

HT3 is the rarest recognized hereditary defect in the tyrosine-degradation pathway. It is a **Mendelian, autosomal-recessive metabolic disease** caused by deficient HPD activity. (szymanska2015tyrosinemiatypeiii pages 1-3, beyzaei2022themutationspectrum pages 1-2)

* **MONDO:** MONDO:0010162
* **OMIM:** 276710
* **Orphanet:** 69723
* **Causal target:** HPD, Ensembl ENSG00000158104
* **Synonyms:** tyrosinemia type 3; hereditary hypertyrosinemia type III; 4-hydroxyphenylpyruvate dioxygenase deficiency; older literature also uses 4-hydroxyphenylpyruvic-acid oxidase deficiency. (OpenTargets Search: Tyrosinemia type III-HPD, endo2003animalmodelsreveal pages 4-5)
* **ICD/MeSH:** no uniquely validated HT3-specific ICD-10/ICD-11 or MeSH code was established in the retrieved evidence; implementations generally require a broader tyrosinemia/inborn-error code plus molecular detail.

Open Targets aggregates genetic evidence from ClinGen, Genomics England, UniProt, gene2phenotype, and EVA and reports a strong HPD–HT3 association; the ClinGen Aminoacidopathy Gene Curation Expert Panel classified the relationship as **definitive**. (OpenTargets Search: Tyrosinemia type III-HPD)

The evidence is aggregated at disease level from curated resources and published patients. It is not derived from a large EHR cohort. Individual case reports remain the main source for phenotype, treatment, and longitudinal outcomes.

## 2. Etiology, risk, and protective factors

### Causal factors

The primary cause is **germline biallelic HPD dysfunction**. Most reported alleles are missense, nonsense, frameshift, or splice-disrupting variants expected to reduce enzyme abundance or activity. The curated disease mechanism is loss or absence of functional gene product. (OpenTargets Search: Tyrosinemia type III-HPD, beyzaei2022themutationspectrum pages 3-5)

No infectious, toxic, occupational, radiation, smoking, alcohol, or lifestyle cause is known. Dietary phenylalanine and tyrosine influence metabolite concentrations after the genetic block but do not cause the disease.

### Genetic risk

Risk is determined principally by inheriting two pathogenic HPD alleles. For two heterozygous parents, standard autosomal-recessive recurrence probabilities apply per pregnancy: 25% affected, 50% carrier, and 25% unaffected/non-carrier. Consanguinity can increase the probability of homozygosity for a rare family allele, but no HT3-specific quantitative estimate is available.

No validated susceptibility loci, modifier genes, protective alleles, founder variants, anticipation, or germline-mosaicism pattern has been established. Most alleles are private, and genotype–phenotype correlation is unresolved. (beyzaei2022themutationspectrum pages 3-5)

### Environmental and protective factors

Restriction of dietary tyrosine and its precursor phenylalanine lowers plasma tyrosine and is the principal proposed protective intervention after diagnosis. Whether this prevents neurologic disease is unknown. Ascorbic acid was used with dietary treatment in isolated reports, but it is not an established disease-modifying therapy. (alsharhan2020disordersofphenylalanine pages 31-33)

There is no well-defined human gene–environment interaction beyond substrate load through diet. The 2024 Drosophila nutrigenomics study reinforces the broader principle that amino-acid disorders can have strong genotype–diet interactions, but it does not establish a validated HT3 diet in humans. It screened 35 amino-acid-disorder fly models and found diet-altered development or survival in 26 overall. (martelli2024identifyingpotentialdietary pages 1-3)

## 3. Phenotypes

### Biochemical abnormalities

The most consistent phenotype is persistent **hypertyrosinemia**, commonly reported around 350–650 μmol/L, accompanied by marked urinary 4-hydroxyphenylpyruvate, 4-hydroxyphenyllactate, and 4-hydroxyphenylacetate. An asymptomatic girl had serum tyrosine of 425–535 μmol/L; a 2023 infant had 709 μmol/L at 25 days and 455 μmol/L at four months. (szymanska2015tyrosinemiatypeiii pages 1-3, sarkargar2023acompoundheterozygous pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33)

Suggested annotations include **Hypertyrosinemia**, increased urinary 4-hydroxyphenylpyruvate, increased urinary 4-hydroxyphenyllactate, and increased urinary 4-hydroxyphenylacetate. Exact HPO mappings for the metabolite-specific findings should be verified in the current HPO release.

### Neurologic and developmental phenotypes

Reported manifestations include:

* developmental or psychomotor delay;
* intellectual disability;
* seizures, including recurrent seizures/status epilepticus in isolated reports;
* intermittent or chronic ataxia;
* autistic behavior or autism;
* attention/behavioral difficulties in some families. (szymanska2015tyrosinemiatypeiii pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33, sarkargar2023acompoundheterozygous pages 3-5)

Suggested HPO terms include **Global developmental delay**, **Delayed psychomotor development**, **Intellectual disability**, **Seizure**, **Ataxia**, and **Autistic behavior**. Onset ranges from infancy—seizures have occurred by four months—to later childhood recognition through biochemical screening. Severity ranges from absent to substantial neurologic disability, and course may be stable or episodic rather than predictably progressive. (alsharhan2020disordersofphenylalanine pages 31-33, sarkargar2023acompoundheterozygous pages 3-5)

Frequency estimates are unstable. A 2022 review found **5/16 (31.25%)** reported patients asymptomatic despite elevated tyrosine and urinary metabolites. A 2023 case report cited approximately 18 published cases and stated that mental disorders had been reported in 75%, but this estimate is vulnerable to publication and ascertainment bias. (beyzaei2022themutationspectrum pages 3-5, sarkargar2023acompoundheterozygous pages 3-5)

### Visceral, ocular, and cutaneous findings

Classic HT3 generally lacks the liver failure, renal Fanconi syndrome/rickets, and hepatocellular carcinoma risk characteristic of type I, and lacks the painful keratitis and palmoplantar hyperkeratosis characteristic of type II. Liver and kidney function were normal in an older nine-patient series summarized in the 2023 report. Recurrent proteinuria has nevertheless been described, and neonatal hepatitis occurred in one recent infant; neither is established as a core phenotype. (szymanska2015tyrosinemiatypeiii pages 3-3, sarkargar2023acompoundheterozygous pages 1-3, sarkargar2023acompoundheterozygous pages 3-5)

Suggested HPO annotation for the limited renal observation is **Proteinuria**. Hepatitis should remain a case-level association rather than a defining HT3 phenotype.

### Quality of life

No HT3-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or disease-specific quality-of-life study was identified. Likely impacts derive from seizures, ataxia, neurodevelopmental disability, repeated biochemical monitoring, and dietary restriction. Quantitative burden estimates are unavailable.

## 4. Genetic and molecular information

### Gene and protein

**HPD** is located at chromosome 12q24-qter, contains 14 exons, and encodes a 392-amino-acid, approximately 43-kDa iron-containing enzyme. Expression is principally hepatic and renal. The enzyme catalyzes oxidative decarboxylation/rearrangement of 4-hydroxyphenylpyruvate to homogentisate. (alsharhan2020disordersofphenylalanine pages 31-33, endo2003animalmodelsreveal pages 1-2, beyzaei2022themutationspectrum pages 1-2)

Suggested gene/process annotations include **tyrosine catabolic process**, **4-hydroxyphenylpyruvate dioxygenase activity**, iron-ion binding, and oxidoreductase activity. Suggested chemical entities include L-tyrosine, 4-hydroxyphenylpyruvate, homogentisate, 4-hydroxyphenyllactate, and 4-hydroxyphenylacetate; CHEBI identifiers should be resolved against the current CHEBI release.

### Published variant spectrum

The 2022 review identified **11 disease-causing HPD variants among 16 patients**: seven missense, two nonsense, one splice defect, and one frameshift. Listed variants included p.Ala33Thr, IVS11+1G>A, p.Tyr200Ter, p.Ile335Met, p.Tyr160Cys, p.Tyr258Ter, p.Ile267Phe, p.Ala268Val, c.759+1G>A, p.Gly154Ser, and p.Gly83Ter/c.248delG. p.Tyr160Cys was the only recurrent allele across unrelated families in that review. (beyzaei2022themutationspectrum pages 1-2, beyzaei2022themutationspectrum pages 3-5)

The 2023 Iranian case added compound heterozygous **c.75G>A (p.Trp25Ter)**, classified in the report as pathogenic, and **c.413C>T (p.Thr138Met)**, described as likely pathogenic. Each parent carried one allele. The child had biochemical HT3 but no seizures, ataxia, or intellectual disability at 1.5 years. (sarkargar2023acompoundheterozygous pages 1-3)

A 2024 Chinese report found during searching described p.Ala244Val in compound heterozygosity with p.Thr219Met, but full-text evidence was not retrievable here; it should be independently checked before production annotation.

Variant-level population frequencies were not available in the retrieved full text. For knowledge-base population annotation, each allele should be checked directly in the current gnomAD release. All disease-causing variants are germline; somatic HPD variants are not a recognized cause of inherited HT3. Large chromosomal rearrangements, repeat expansions, mitochondrial variants, and disease-specific epigenetic abnormalities have not been established.

### Genotype–phenotype relationship

No robust relationship exists between variant class, tyrosine concentration, and neurologic severity. Tyr160 lies in an alpha helix implicated in inter-subunit contacts and may affect enzyme stability, but this remains structurally inferred rather than proven in patients. The same biochemical defect can accompany severe neurologic disease or an asymptomatic state. (szymanska2015tyrosinemiatypeiii pages 1-3, beyzaei2022themutationspectrum pages 2-3, beyzaei2022themutationspectrum pages 3-5)

## 5. Environmental information

No toxin, pollution, infectious agent, smoking behavior, alcohol exposure, or occupation is known to initiate HT3. Protein intake can alter biochemical substrate load. Excessive dietary restriction, conversely, risks inadequate protein, growth failure, and micronutrient deficiency; dietary care should therefore be supervised by an inherited-metabolic-disease dietitian.

Hawkinsinuria is an allelic but distinct HPD disorder, generally associated with heterozygous variants such as p.Ala33Thr and dominant inheritance. It should not be interpreted as an environmental form of HT3. (endo2003animalmodelsreveal pages 2-2, endo2003animalmodelsreveal pages 4-5)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic event:** biallelic damaging HPD variants reduce functional enzyme.
2. **Primary biochemical block:** conversion of 4-hydroxyphenylpyruvate to homogentisate is impaired.
3. **Metabolic consequence:** plasma tyrosine rises and 4-hydroxyphenylpyruvate is diverted to 4-hydroxyphenyllactate and 4-hydroxyphenylacetate, which are excreted in urine.
4. **Organ consequence:** because the pathway is blocked upstream of homogentisate and fumarylacetoacetate, the severe downstream hepatotoxicity of HT1 does not ordinarily occur.
5. **Possible neurologic consequence:** high tyrosine and/or upstream derivatives may disrupt neural function, but human causality is not proven because multiple untreated patients remain neurologically normal. (szymanska2015tyrosinemiatypeiii pages 3-3, endo2003animalmodelsreveal pages 1-2, xie2019hpddegradationregulated pages 1-2)

Suggested GO biological-process terms are tyrosine catabolic process, aromatic amino-acid family catabolic process, cellular amino-acid metabolic process, protein ubiquitination, and proteasomal protein catabolic process. Primary suggested cell types are **hepatocyte** and **neuron**; kidney tubular cells are biologically plausible from renal HPD expression but not demonstrated as a primary injured population.

### Experimental regulatory mechanism

A 2019 mechanistic study showed that hepatic TTC36 binds HPD and inhibits STK33-mediated phosphorylation of HPD at Thr382. Reduced Thr382 phosphorylation limits PELI1 recruitment, HPD polyubiquitination, and proteasomal degradation. Ttc36-null mice had reduced hepatic HPD, tyrosinemia, hippocampal neuronal injury, and learning/memory deficits. This identifies a regulatory pathway capable of producing an HT3-like state, but **TTC36, STK33, and PELI1 are not validated human HT3 modifier genes**. (xie2019hpddegradationregulated pages 1-2, xie2019hpddegradationregulated pages 6-7)

A direct abstract quotation states: “Ttc36−/− mice have reduced HPD expression in the liver and exhibit tyrosinemia, damage to hippocampal neurons, and deficits of learning and memory.” The study was published in *Nature Communications* on September 16, 2019; DOI: [10.1038/s41467-019-12011-0](https://doi.org/10.1038/s41467-019-12011-0). (xie2019hpddegradationregulated pages 1-2)

### Immune, omics, and tissue-damage evidence

One small human study reported increased nitric-oxide release by neutrophils from an affected woman and proposed a possible connection to nervous-system involvement. This is exploratory and not sufficient to define HT3 as an immune or inflammatory disorder. (sarkargar2023acompoundheterozygous pages 3-5)

No reproducible human HT3 transcriptomic, proteomic, lipidomic, single-cell, spatial-transcriptomic, epigenomic, or integrated multi-omics signature was identified. The TTC36 study used cellular biochemistry and mouse tissues, not clinical multi-omics. The 2024 Drosophila project provides a platform for diet–genotype screening rather than a validated human molecular profile. (martelli2024identifyingpotentialdietary pages 1-3, xie2019hpddegradationregulated pages 1-2)

## 7. Anatomical structures affected

The **liver** is the principal metabolic organ because hepatic HPD carries much of systemic tyrosine catabolism. The kidney also expresses HPD and contributes to amino-acid metabolism. The **central nervous system**, including hippocampal neurons in experimental mice, is the main candidate secondary target of metabolite imbalance. (endo2003animalmodelsreveal pages 1-2, beyzaei2022themutationspectrum pages 1-2, xie2019hpddegradationregulated pages 1-2)

Suggested annotations:

* UBERON: liver, kidney, brain, hippocampus;
* CL: hepatocyte, neuron; renal tubular epithelial cell as a cautious secondary suggestion;
* GO cellular component: cytosol/cytoplasm for metabolic enzyme localization and proteasome complex for experimentally demonstrated HPD turnover.

There is no expected lateralization. Human biopsy or neuropathology series are unavailable.

## 8. Temporal development

The biochemical defect is congenital. Detection can occur neonatally through elevated tyrosine on tandem-mass-spectrometry screening, during infancy after seizures or hepatitis, in childhood through developmental concerns, or incidentally in an asymptomatic older child. (szymanska2015tyrosinemiatypeiii pages 1-3, sarkargar2023acompoundheterozygous pages 1-3, beyzaei2022themutationspectrum pages 5-6)

No formal disease stages exist. Course is variable: some patients have early neurologic manifestations; others remain stable and asymptomatic for years without strict dietary treatment. A patient carrying homozygous c.759+1G>A reportedly retained normal neuropsychological development over seven years despite poor dietary adherence. This observation argues against assuming inevitable progression. (sarkargar2023acompoundheterozygous pages 3-5)

Critical intervention windows are unknown. Early normalization of tyrosine is biologically reasonable, especially in infancy, but no prospective evidence proves that it prevents neurologic disease.

## 9. Inheritance and population

HT3 is autosomal recessive with highly variable expressivity and apparently incomplete clinical penetrance, although biochemical penetrance may be higher. Anticipation is not expected. No sex bias has been demonstrated.

The literature reported 13 cases by 2015, 16 genetically reviewed patients by 2022, and approximately 18 cases in the 2023 report. These are publication counts, not prevalence estimates. True prevalence is probably underestimated because asymptomatic biochemical cases can be missed. No reliable incidence per 100,000 births, carrier frequency, mortality rate, or sex ratio exists. (szymanska2015tyrosinemiatypeiii pages 1-3, beyzaei2022themutationspectrum pages 3-5, sarkargar2023acompoundheterozygous pages 3-5)

Published variants have been reported in Portugal, Turkey, Sweden, Poland, Japan, Iran, and China. The 2022 review found no molecular data from North/Central America, Africa, Australia, or Oceania. This geographic distribution likely reflects case ascertainment and reporting rather than biological restriction. No definitive HT3 founder effect is established. (beyzaei2022themutationspectrum pages 3-5)

## 10. Diagnostics

### Recommended workflow

1. **Plasma amino-acid analysis:** confirm persistent elevated tyrosine.
2. **Urine organic-acid analysis:** quantify 4-hydroxyphenylpyruvate, 4-hydroxyphenyllactate, and 4-hydroxyphenylacetate.
3. **Exclude HT1 urgently:** test blood or urine succinylacetone and assess liver/renal function. Succinylacetone should not be increased in isolated HPD deficiency.
4. **Phenotypic assessment:** neurologic/developmental examination; seizures prompt EEG; ataxia or unexplained neurologic findings may justify brain MRI, although no diagnostic imaging signature exists.
5. **Molecular confirmation:** demonstrate biallelic pathogenic/likely pathogenic HPD variants with a single-gene test, tyrosinemia/aminoacidopathy panel, exome, or genome sequencing, followed by segregation analysis where possible. (szymanska2015tyrosinemiatypeiii pages 1-3, sarkargar2023acompoundheterozygous pages 1-3, alsharhan2020disordersofphenylalanine pages 31-33)

The 2015 case used a TruSight One panel; the 2023 case used WES with Sanger confirmation. WES/WGS is particularly useful when biochemical findings are atypical or a panel is negative. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine because the recognized mechanism is sequence-level HPD dysfunction. (szymanska2015tyrosinemiatypeiii pages 3-3, sarkargar2023acompoundheterozygous pages 1-3)

### Differential diagnosis

* **Tyrosinemia type I—FAH deficiency:** succinylacetone positive; liver failure, renal tubulopathy/rickets, porphyria-like crises, and hepatocellular-carcinoma risk.
* **Tyrosinemia type II—TAT deficiency:** typically higher tyrosine, keratitis/corneal lesions, and painful palmoplantar hyperkeratosis.
* **Transient neonatal tyrosinemia:** resolves with hepatic maturation; associated with prematurity, high protein intake, and/or low vitamin C rather than biallelic HPD variants.
* **Hawkinsinuria:** allelic HPD disorder, usually dominant, with hawkinsin excretion and infantile metabolic symptoms.
* **Secondary hypertyrosinemia:** liver dysfunction, severe illness, nutritional factors, or medication effects. (endo2003animalmodelsreveal pages 4-5, alsharhan2020disordersofphenylalanine pages 31-33)

No consensus clinical diagnostic criteria or disease-specific LOINC panel was identified.

### Screening

HT3 may be detected when newborn screening reports elevated tyrosine by MS/MS, but tyrosine is nonspecific. Programs designed for HT1 increasingly rely on succinylacetone; consequently, an infant with high tyrosine but normal succinylacetone requires evaluation for types II/III, transient neonatal tyrosinemia, and liver disease. Dedicated HT3 screening performance metrics are unavailable. (szymanska2015tyrosinemiatypeiii pages 3-3, beyzaei2022themutationspectrum pages 5-6, sarkargar2023acompoundheterozygous pages 3-5)

## 11. Outcome and prognosis

No survival curves, disease-specific mortality rate, or life-expectancy estimate exists. Available evidence suggests that HT3 is substantially more benign than untreated HT1 and is not known to cause progressive liver failure or hepatocellular carcinoma. Prognosis is driven mainly by whether neurologic manifestations occur. (alsharhan2020disordersofphenylalanine pages 31-33, endo2003animalmodelsreveal pages 1-2)

Some children improve biochemically and symptomatically on diet; others remain asymptomatic without treatment. In the 2015 report, an 11-year-old girl with homozygous p.Tyr160Cys had normal development despite serum tyrosine of 425–535 μmol/L and no tyrosine/phenylalanine-restricted diet. This directly challenges a simple relationship between tyrosine concentration and neurologic injury. (szymanska2015tyrosinemiatypeiii pages 1-3, szymanska2015tyrosinemiatypeiii pages 3-3)

No validated prognostic biomarker exists beyond clinical status, developmental trajectory, seizure control, and metabolite monitoring. Variant class and plasma tyrosine concentration do not reliably predict outcome. Long-term follow-up is needed because existing case numbers and observation periods are insufficient to exclude late manifestations.

## 12. Treatment

### Current management

There is no HT3-specific approved pharmacotherapy. The principal strategy is a **phenylalanine- and tyrosine-restricted diet**, adjusted to maintain adequate growth and essential amino-acid nutrition. Specialized low-protein foods or amino-acid formulas may be needed. Suggested NCIT mappings are dietary intervention, low-protein diet, low-phenylalanine diet, and low-tyrosine diet; exact NCIT identifiers should be checked before ingestion. (alsharhan2020disordersofphenylalanine pages 31-33)

One report summarized in the 2020 review used ascorbic acid 50 mg/day with dietary restriction and observed normalized tyrosine and seizure improvement. Evidence is too limited to recommend vitamin C as a universal stand-alone treatment. (alsharhan2020disordersofphenylalanine pages 31-33)

Supportive care may include antiseizure medication, physical/occupational therapy for ataxia or motor delay, speech/developmental therapy, and educational/behavioral support. No surgery is disease modifying.

### Monitoring

A pragmatic plan includes plasma tyrosine and nutritional amino acids, urine metabolites, growth and nutritional status, liver and renal chemistry initially, urinalysis for proteinuria, and serial neurologic/developmental assessment. EEG or MRI is symptom-directed. No evidence-based target tyrosine range or monitoring interval specific to HT3 has been validated.

### Treatments that should not be imported from HT1

**Nitisinone is not a treatment for HT3.** It pharmacologically inhibits HPD and deliberately creates an HT3-like upstream block when treating HT1; giving it in primary HPD deficiency has no mechanistic rationale and could worsen hypertyrosinemia. Likewise, liver transplantation is not standard HT3 care.

### Experimental therapies and trials

No HT3-specific interventional ClinicalTrials.gov study was identified. Retrieved trials concerned HT1/nitisinone or broad nutritional products, not correction of HPD deficiency. No clinical gene-replacement, gene-editing, cell, RNA, or enzyme-replacement therapy is available.

CRISPR deletion of Hpd has been used experimentally to rescue **Fah-deficient HT1 mice** by converting the severe downstream block to a more benign HT3-like state. This validates pathway position but is not a treatment strategy for patients who already lack HPD. Recent 2024 mouse studies likewise use Hpd editing as a modifier of HT1, not as therapy for HT3.

## 13. Prevention

Primary prevention of spontaneous disease occurrence is not possible through lifestyle modification. Reproductive prevention options include genetic counseling, targeted parental carrier testing after a proband is identified, cascade testing of relatives, prenatal diagnosis, and preimplantation genetic testing for known familial variants. These approaches follow standard autosomal-recessive practice; HT3-specific outcome studies are absent. (sarkargar2023acompoundheterozygous pages 1-3, beyzaei2022themutationspectrum pages 5-6)

Secondary prevention consists of early detection through newborn-screen hypertyrosinemia or family screening and prompt metabolic evaluation. Tertiary prevention consists of controlling excessive tyrosine exposure, maintaining nutrition, monitoring development and seizures, and providing rehabilitation. Vaccination, antimicrobial prophylaxis, sanitation measures, and environmental remediation have no disease-specific role.

## 14. Other species and natural disease

The orthologous pathway is conserved across vertebrates. **Mus musculus** (NCBI Taxonomy 10090) Hpd deficiency produces hypertyrosinemia and urinary tyrosine derivatives. Retrieved evidence did not establish a well-characterized naturally occurring veterinary syndrome equivalent to human HT3 in a specific dog, cat, livestock, or wildlife breed. No zoonotic transmission exists because HT3 is inherited, not infectious.

HPD-deficient mice generally lack the severe visceral damage of FAH deficiency, supporting the clinical distinction between HT3 and HT1. (endo2003animalmodelsreveal pages 1-2)

## 15. Model organisms

### Mouse models

Whole-body Hpd-deficient mice reproduce the biochemical block—high circulating tyrosine and urinary 4-hydroxyphenyl metabolites—and lack the severe hepatorenal injury characteristic of HT1. They are useful for tyrosine-flux studies, toxicity thresholds, and diet testing. Their limitation is that neurologic findings vary by model and may not reproduce the broad human spectrum. (endo2003animalmodelsreveal pages 2-2, endo2003animalmodelsreveal pages 1-2)

Ttc36-null mice provide an acquired-regulatory model: enhanced STK33/PELI1-mediated HPD degradation causes tyrosinemia, hippocampal neuronal damage, and learning/memory impairment. This model is useful for protein-stability mechanisms but is not genetically identical to biallelic human HPD deficiency. (xie2019hpddegradationregulated pages 1-2)

Fah/Hpd double mutants and somatic Hpd-edited Fah-deficient mice model metabolic-pathway rerouting for HT1 research. They demonstrate that an upstream HPD block prevents production of toxic downstream FAH substrates, but they do not directly model treatment of HT3.

### Drosophila

The 2024 *Cell Reports* nutrigenomics project used genetically tractable Drosophila amino-acid-disorder models and defined diets to screen gene–nutrient interactions. The paper states: “Here, we screened 35 Drosophila amino acid disorder models for disease-diet interactions and found 26 with diet-altered development and/or survival.” HT3/OMIM 276710 was included in the platform’s disease-model framework, although the principal detailed rescue experiment concerned isolated sulfite oxidase deficiency rather than HT3. Published March 26, 2024; DOI: [10.1016/j.celrep.2024.113861](https://doi.org/10.1016/j.celrep.2024.113861). (martelli2024identifyingpotentialdietary pages 1-3, martelli2024identifyingpotentialdietary pages 29-30)

No validated HT3 patient-derived iPSC, organoid, zebrafish, rat, yeast, or CRISPR-screen resource was identified in the retrieved evidence.

## Recent developments, 2023–2024

1. **New human genotype, 2023:** an Iranian girl was reported with compound heterozygous p.Trp25Ter and p.Thr138Met HPD variants, neonatal hepatitis, and tyrosine up to 709 μmol/L, but no classic neurologic manifestations at 1.5 years. Published online January 2023; DOI: [10.18502/ijml.v9i4.11619](https://doi.org/10.18502/ijml.v9i4.11619). (sarkargar2023acompoundheterozygous pages 1-3)
2. **New Chinese genotype–phenotype report, 2024:** p.Ala244Val in compound heterozygosity with p.Thr219Met was reported in search metadata. Full-text verification is required before variant curation.
3. **Diet-discovery technology, 2024:** Drosophila nutrigenomics offers scalable testing of amino-acid composition and genotype–diet interactions, but no HT3-specific human recommendation has yet resulted. (martelli2024identifyingpotentialdietary pages 1-3)
4. **Pathway-editing research, 2024:** liver-specific Hpd disruption remains under study as a modifier strategy for HT1 models. It is mechanistically informative for tyrosine catabolism but not therapeutic for HPD-deficient HT3.

## Expert assessment and priority evidence gaps

The most defensible current interpretation is that HT3 is a **biochemically penetrant but clinically variably expressive** HPD deficiency. Neurologic disease is plausible and repeatedly reported, yet the asymptomatic fraction and absence of a concentration–outcome relationship prevent assuming that persistent tyrosine alone is sufficient to cause brain injury. The 2022 review concluded that no definite genotype–phenotype relationship could be drawn because of the small number of patients, phenotypic heterogeneity, and predominance of private variants. (beyzaei2022themutationspectrum pages 3-5)

The highest-priority research needs are an international registry with standardized metabolite and neurodevelopmental data; prospective natural-history follow-up; functional testing of individual HPD alleles; direct gnomAD-based carrier estimates; agreed treatment thresholds and nutritional targets; and patient-derived neuronal/hepatic models. No 2023–2024 study resolved these fundamental uncertainties.

## Key source list

* Beyzaei Z et al. “The mutation spectrum and ethnic distribution of non-hepatorenal tyrosinemia (types II, III).” *Orphanet Journal of Rare Diseases*. Published December 2022. DOI: [10.1186/s13023-022-02579-0](https://doi.org/10.1186/s13023-022-02579-0). (beyzaei2022themutationspectrum pages 1-2, beyzaei2022themutationspectrum pages 3-5)
* Sarkargar F et al. “A Compound Heterozygous HPD Mutation in an Iranian Patient with Hypertyrosinemia Type III.” *International Journal of Medical Laboratory*. January 2023. DOI: [10.18502/ijml.v9i4.11619](https://doi.org/10.18502/ijml.v9i4.11619). (sarkargar2023acompoundheterozygous pages 1-3)
* Szymanska E et al. “Tyrosinemia type III in an asymptomatic girl.” *Molecular Genetics and Metabolism Reports*. December 2015. DOI: [10.1016/j.ymgmr.2015.10.004](https://doi.org/10.1016/j.ymgmr.2015.10.004). (szymanska2015tyrosinemiatypeiii pages 1-3)
* Xie Y et al. “HPD degradation regulated by the TTC36-STK33-PELI1 signaling axis induces tyrosinemia and neurological damage.” *Nature Communications*. September 2019. DOI: [10.1038/s41467-019-12011-0](https://doi.org/10.1038/s41467-019-12011-0). (xie2019hpddegradationregulated pages 1-2)
* Martelli F et al. “Identifying potential dietary treatments for inherited metabolic disorders using Drosophila nutrigenomics.” *Cell Reports*. March 26, 2024. DOI: [10.1016/j.celrep.2024.113861](https://doi.org/10.1016/j.celrep.2024.113861). (martelli2024identifyingpotentialdietary pages 1-3)

**Evidence caveat:** the retrieved records supplied PMIDs for several foundational HPD papers through Open Targets—PMID 11073718, 10942115, 26226126, 27604308, 17560158, and 30984715—but not every article’s PMID was available in the full-text metadata. These identifiers should be cross-checked against PubMed before automated ingestion. (OpenTargets Search: Tyrosinemia type III-HPD)

References

1. (szymanska2015tyrosinemiatypeiii pages 3-3): Edyta Szymanska, Malgorzata Sredzinska, Elzbieta Ciara, Dorota Piekutowska-Abramczuk, Rafal Ploski, Dariusz Rokicki, and Anna Tylki-Szymanska. Tyrosinemia type iii in an asymptomatic girl. Molecular Genetics and Metabolism Reports, 5:48-50, Dec 2015. URL: https://doi.org/10.1016/j.ymgmr.2015.10.004, doi:10.1016/j.ymgmr.2015.10.004. This article has 34 citations.

2. (beyzaei2022themutationspectrum pages 3-5): Zahra Beyzaei, Sara Nabavizadeh, Sara Karimzadeh, and Bita Geramizadeh. The mutation spectrum and ethnic distribution of non-hepatorenal tyrosinemia (types ii, iii). Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02579-0, doi:10.1186/s13023-022-02579-0. This article has 22 citations and is from a peer-reviewed journal.

3. (alsharhan2020disordersofphenylalanine pages 31-33): Hind Alsharhan and Can Ficicioglu. Disorders of phenylalanine and tyrosine metabolism. Translational Science of Rare Diseases, 5:3-58, Jul 2020. URL: https://doi.org/10.3233/trd-200049, doi:10.3233/trd-200049. This article has 45 citations.

4. (OpenTargets Search: Tyrosinemia type III-HPD): Open Targets Query (Tyrosinemia type III-HPD, 12 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (beyzaei2022themutationspectrum pages 1-2): Zahra Beyzaei, Sara Nabavizadeh, Sara Karimzadeh, and Bita Geramizadeh. The mutation spectrum and ethnic distribution of non-hepatorenal tyrosinemia (types ii, iii). Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02579-0, doi:10.1186/s13023-022-02579-0. This article has 22 citations and is from a peer-reviewed journal.

6. (szymanska2015tyrosinemiatypeiii pages 1-3): Edyta Szymanska, Malgorzata Sredzinska, Elzbieta Ciara, Dorota Piekutowska-Abramczuk, Rafal Ploski, Dariusz Rokicki, and Anna Tylki-Szymanska. Tyrosinemia type iii in an asymptomatic girl. Molecular Genetics and Metabolism Reports, 5:48-50, Dec 2015. URL: https://doi.org/10.1016/j.ymgmr.2015.10.004, doi:10.1016/j.ymgmr.2015.10.004. This article has 34 citations.

7. (endo2003animalmodelsreveal pages 4-5): Fumio Endo, Yasuhiko Tanaka, Kaede Tomoeda, Akito Tanoue, Gozoh Tsujimoto, and Kimitoshi Nakamura. Animal models reveal pathophysiologies of tyrosinemias. The Journal of nutrition, 133 6 Suppl 1:2063S-2067S, Jun 2003. URL: https://doi.org/10.1093/jn/133.6.2063s, doi:10.1093/jn/133.6.2063s. This article has 23 citations.

8. (endo2003animalmodelsreveal pages 1-2): Fumio Endo, Yasuhiko Tanaka, Kaede Tomoeda, Akito Tanoue, Gozoh Tsujimoto, and Kimitoshi Nakamura. Animal models reveal pathophysiologies of tyrosinemias. The Journal of nutrition, 133 6 Suppl 1:2063S-2067S, Jun 2003. URL: https://doi.org/10.1093/jn/133.6.2063s, doi:10.1093/jn/133.6.2063s. This article has 23 citations.

9. (xie2019hpddegradationregulated pages 1-2): Yajun Xie, Xiaoyan Lv, Dongsheng Ni, Jianing Liu, Yanxia Hu, Yamin Liu, Yunhong Liu, Rui Liu, Hui Zhao, Zhimin Lu, and Qingbiao Zhou. Hpd degradation regulated by the ttc36-stk33-peli1 signaling axis induces tyrosinemia and neurological damage. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12011-0, doi:10.1038/s41467-019-12011-0. This article has 46 citations and is from a highest quality peer-reviewed journal.

10. (sarkargar2023acompoundheterozygous pages 1-3): Fatemeh Sarkargar, Seyed Ali Madani Manshadi, Ehsan Zare Mehrjardi, Hosein Khodaei, Seyed Mehdi Kalantar, and Seyed Ahmad Mohamamdi. A compound heterozygous hpd mutation in an iranian patient with hypertyrosinemia type iii. International Journal of Medical Laboratory, Jan 2023. URL: https://doi.org/10.18502/ijml.v9i4.11619, doi:10.18502/ijml.v9i4.11619. This article has 0 citations.

11. (endo2003animalmodelsreveal pages 2-2): Fumio Endo, Yasuhiko Tanaka, Kaede Tomoeda, Akito Tanoue, Gozoh Tsujimoto, and Kimitoshi Nakamura. Animal models reveal pathophysiologies of tyrosinemias. The Journal of nutrition, 133 6 Suppl 1:2063S-2067S, Jun 2003. URL: https://doi.org/10.1093/jn/133.6.2063s, doi:10.1093/jn/133.6.2063s. This article has 23 citations.

12. (sarkargar2023acompoundheterozygous pages 3-5): Fatemeh Sarkargar, Seyed Ali Madani Manshadi, Ehsan Zare Mehrjardi, Hosein Khodaei, Seyed Mehdi Kalantar, and Seyed Ahmad Mohamamdi. A compound heterozygous hpd mutation in an iranian patient with hypertyrosinemia type iii. International Journal of Medical Laboratory, Jan 2023. URL: https://doi.org/10.18502/ijml.v9i4.11619, doi:10.18502/ijml.v9i4.11619. This article has 0 citations.

13. (xie2019hpddegradationregulated pages 6-7): Yajun Xie, Xiaoyan Lv, Dongsheng Ni, Jianing Liu, Yanxia Hu, Yamin Liu, Yunhong Liu, Rui Liu, Hui Zhao, Zhimin Lu, and Qingbiao Zhou. Hpd degradation regulated by the ttc36-stk33-peli1 signaling axis induces tyrosinemia and neurological damage. Nature Communications, Sep 2019. URL: https://doi.org/10.1038/s41467-019-12011-0, doi:10.1038/s41467-019-12011-0. This article has 46 citations and is from a highest quality peer-reviewed journal.

14. (beyzaei2022themutationspectrum pages 5-6): Zahra Beyzaei, Sara Nabavizadeh, Sara Karimzadeh, and Bita Geramizadeh. The mutation spectrum and ethnic distribution of non-hepatorenal tyrosinemia (types ii, iii). Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02579-0, doi:10.1186/s13023-022-02579-0. This article has 22 citations and is from a peer-reviewed journal.

15. (martelli2024identifyingpotentialdietary pages 1-3): Felipe Martelli, Jiayi Lin, Sarah Mele, Wendy Imlach, O. Kanca, Christopher K. Barlow, Jefferson Paril, Ralf B. Schittenhelm, John Christodoulou, Hugo J. Bellen, Matthew D. W. Piper, and Travis K. Johnson. Identifying potential dietary treatments for inherited metabolic disorders using drosophila nutrigenomics. Cell reports, 43:113861-113861, Feb 2024. URL: https://doi.org/10.1016/j.celrep.2024.113861, doi:10.1016/j.celrep.2024.113861. This article has 10 citations and is from a highest quality peer-reviewed journal.

16. (martelli2024identifyingpotentialdietary pages 29-30): Felipe Martelli, Jiayi Lin, Sarah Mele, Wendy Imlach, O. Kanca, Christopher K. Barlow, Jefferson Paril, Ralf B. Schittenhelm, John Christodoulou, Hugo J. Bellen, Matthew D. W. Piper, and Travis K. Johnson. Identifying potential dietary treatments for inherited metabolic disorders using drosophila nutrigenomics. Cell reports, 43:113861-113861, Feb 2024. URL: https://doi.org/10.1016/j.celrep.2024.113861, doi:10.1016/j.celrep.2024.113861. This article has 10 citations and is from a highest quality peer-reviewed journal.

17. (beyzaei2022themutationspectrum pages 2-3): Zahra Beyzaei, Sara Nabavizadeh, Sara Karimzadeh, and Bita Geramizadeh. The mutation spectrum and ethnic distribution of non-hepatorenal tyrosinemia (types ii, iii). Orphanet Journal of Rare Diseases, Dec 2022. URL: https://doi.org/10.1186/s13023-022-02579-0, doi:10.1186/s13023-022-02579-0. This article has 22 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Tyrosinemia_Type_III-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.