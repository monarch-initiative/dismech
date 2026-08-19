---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T20:58:42.769425'
end_time: '2026-08-18T21:13:37.170113'
duration_seconds: 894.4
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Hypercholesterolemia 3
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 24
  on_topic: 12
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Hypercholesterolemia_3-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Hypercholesterolemia 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hypercholesterolemia 3** covering all of the
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
- **Disease Name:** Autosomal Dominant Hypercholesterolemia 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Hypercholesterolemia 3** covering all of the
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


# Autosomal Dominant Hypercholesterolemia 3 (ADH3): Disease Characteristics Report

## Executive summary and evidence boundaries

Autosomal dominant hypercholesterolemia 3 (ADH3; FH3) is the rare **PCSK9 gain-of-function (GOF)** subtype of familial hypercholesterolemia (FH). Pathogenic monoallelic PCSK9 variants increase hepatic LDL-receptor (LDLR) degradation, causing lifelong elevation of LDL cholesterol (LDL-C), accelerated atherosclerosis, and premature coronary artery disease (CAD). The defining human discovery was reported by Abifadel et al. in June 2003, *Nature Genetics*, “Mutations in PCSK9 cause autosomal dominant hypercholesterolemia” (PMID **12730697**; DOI: https://doi.org/10.1038/ng1161). Open Targets independently maps ADH3 to **MONDO:0011369** and PCSK9 (ENSG00000169174), with human genetic and approved-therapy evidence. (OpenTargets Search: familial hypercholesterolemia-PCSK9)

A major curation caveat is that most epidemiology, outcomes, diagnostic thresholds, and treatment trials pool all molecular forms of heterozygous FH—predominantly LDLR-related disease. Such findings are identified below as **FH-wide**, not ADH3-specific. Direct ADH3 evidence consists principally of families carrying PCSK9 GOF variants, biochemical studies, and PCSK9-GOF animal models.

The following table provides a compact knowledge-base representation.

| Domain | Summary | Key IDs / ontology suggestions | Evidence qualifier |
|---|---|---|---|
| Identity / identifiers | Autosomal Dominant Hypercholesterolemia 3 (ADH3) is the PCSK9-related monogenic form of familial hypercholesterolemia; evidence here is disease-level, aggregated from databases, guidelines, trials, and literature rather than individual EHR records. | MONDO:0011369; MeSH disease family terms in trial metadata include Hypercholesterolemia/Hyperlipoproteinemia Type II; target gene PCSK9 = ENSG00000169174 (OpenTargets Search: familial hypercholesterolemia-PCSK9, NCT05398029 chunk 1) | Authoritative database + clinical literature; ADH3-specific MONDO supported, but other disease codes were not directly retrieved here. |
| Causal gene and inheritance | Causal gene: **PCSK9**; pathogenic **gain-of-function** alleles cause ADH3/FH3. Inheritance is monoallelic autosomal dominant. | PCSK9; inheritance: autosomal dominant / monoallelic; related FH gene class includes LDLR, APOB, PCSK9 (OpenTargets Search: familial hypercholesterolemia-PCSK9, cesaro2020beyondcholesterolmetabolism pages 1-2, abifadel2023geneticandmolecular pages 1-2) | Strong human genetic evidence; target-disease linkage also supported by drug-approval evidence. |
| Representative GOF variants | Recurrently cited GOF variants include **S127R, F216L, D374Y**; additional GOF variants in prodomain and C-terminal CM1/CHR regions impair LDL association and/or enhance LDLR binding/degradation. | Variant examples: p.Ser127Arg, p.Phe216Leu, p.Asp374Tyr, p.Arg496Trp (sarkar2022pathogenicgainoffunctionmutations pages 1-2, sarkar2022pathogenicgainoffunctionmutations pages 2-3, rosenson2019cholesterolloweringagents. pages 5-5) | Variant list is representative, not exhaustive; some classic primary papers were referenced indirectly or unobtainable in-tool. |
| Core mechanism | PCSK9 is a secreted hepatocyte-enriched protein that binds LDLR and diverts it to endo-lysosomal degradation, reducing receptor recycling and hepatic LDL clearance. GOF variants intensify this process by increasing LDLR affinity and/or altering LDL binding regulation, producing lifelong LDL-C elevation and accelerated atherosclerosis. | GO: LDL receptor catabolic process; GO: receptor-mediated endocytosis; GO CC suggestions: extracellular region, lysosome; CL: hepatocyte; UBERON: liver (rosenson2019cholesterolloweringagents. pages 3-5, sarkar2022pathogenicgainoffunctionmutations pages 2-3, sundararaman2021pcsk9amultifaceted pages 2-4, cesaro2020beyondcholesterolmetabolism pages 1-2) | Human, in vitro, and animal evidence converge; LDLR-independent inflammatory roles are plausible but less disease-defining than hepatic LDLR degradation. |
| Hallmark phenotypes / HPO suggestions | Hallmarks align with heterozygous familial hypercholesterolemia: markedly elevated LDL-C/hypercholesterolemia, tendon/skin xanthomas, corneal arcus, premature coronary artery disease, premature atherosclerosis; stroke risk less consistently increased than CAD. | HPO suggestions: HP:0003124 Hypercholesterolemia; HP:0000991 Xanthoma; HP:0001084 Corneal arcus; HP:0001677 Coronary artery atherosclerosis; HP:0001716 Premature arteriosclerosis (suggestive) (haradashiba2023guidelinesforthe pages 2-4, fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9) | Phenotype frequencies were mainly available for FH broadly, not ADH3-only cohorts. |
| Diagnosis | Diagnosis generally follows FH frameworks: family history, LDL-C level, premature CAD, tendon xanthomas/Achilles tendon thickening, and confirmatory molecular testing. Japanese adult guideline updated Achilles tendon thresholds to **≥8.0 mm men / ≥7.5 mm women** to improve sensitivity. | Diagnostic systems: DLCN / Simon Broome / national FH criteria; test target genes include LDLR, APOB, PCSK9; HPO: HP:0003326 Elevated LDL cholesterol concentration (suggestive) (haradashiba2023guidelinesforthe pages 1-2, yip2023geneticspectrumand pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2) | Clinical diagnosis is usually FH-spectrum; molecular confirmation can specify ADH3. |
| Treatment algorithm | Stepwise care: lifestyle optimization + **high-intensity statin** first line; add **ezetimibe** if needed; add **PCSK9 inhibitor** (alirocumab/evolocumab) for very-high-risk or insufficient control; **inclisiran** or **bempedoic acid** are additional options; **lipoprotein apheresis** for refractory/severe disease. Typical very-high-risk LDL-C goal: **≥50% reduction and <55 mg/dL (<1.4 mmol/L)**. | NCIT suggestions: Statin therapy, Ezetimibe, Alirocumab, Evolocumab, Inclisiran, Bempedoic Acid, Lipoprotein Apheresis (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9, damase2024establishedandemerging pages 1-3, katzmann2020pcsk9inhibitioninsights pages 1-2, rajendran2024acomparativeanalysis pages 1-2) | Algorithm is evidence-based for FH broadly; ADH3-specific response data are limited but PCSK9-targeted therapies are mechanistically central. |
| Epidemiology caveat | No robust prevalence estimate was retrieved for **ADH3 specifically**. Most published epidemiology concerns **all heterozygous FH**, estimated around **1:311 to 1:303** in the general population and **~1:17** among ASCVD patients; prevalence varies by ethnicity and founder effects. | Use disease-level caveat flag: “FH-wide estimate, not ADH3-specific”; MONDO:0011369 only identifies subtype (hu2020prevalenceoffamilial pages 11-11, hu2020prevalenceoffamilial pages 1-2, toftnielsen2022familialhypercholesterolemiaprevalence pages 1-3, taranto2023geneticheterogeneityof pages 1-2) | Important limitation for knowledge-base curation: subtype-specific denominators are not established here. |
| Major trials / real-world implementation | PCSK9-directed implementation includes approved antibodies and emerging gene/RNA approaches. Trial examples: **VERVE-101** base editing in HeFH + ASCVD (**NCT05398029**, phase 1, n=13); pediatric **evolocumab** extension (**NCT02624869**, n=163); adolescent **inclisiran ORION-16** (**NCT04652726**, n=141); alirocumab plaque study **ARCHITECT** (**NCT05465278**, n=104). | NCT05398029; NCT02624869; NCT04652726; NCT05465278 (NCT05398029 chunk 1, NCT05465278 chunk 1, NCT02624869 chunk 1, NCT04652726 chunk 1) | Demonstrates real-world translation from gene discovery to antibodies, siRNA, and base editing. |
| Model organisms | Useful disease models include **AAV-hPCSK9 D374Y mice** causing sustained hypercholesterolemia and atherosclerosis, and **Yucatan miniature pigs/minipigs** carrying human **PCSK9 D374Y** with coronary/aortic lesions. A 2024 **PCSK9 nanoparticle vaccine** used AAV-hPCSK9D374Y mouse models. Limitation: pig models may not reproduce plaque rupture/thrombosis fully. | Species: Mus musculus; Sus scrofa; variant/model driver: PCSK9 D374Y; CL/UBERON relevance: hepatocyte, aorta, coronary artery (rochemolina2015inductionofsustained pages 1-2, perleberg2018geneticallyengineeredpigs pages 4-4, fang2024developmentofa pages 1-3, katsuki2024theroleof pages 7-7) | Strong translational utility for mechanism and therapy testing; imperfect recapitulation of late human plaque complications. |


*Table: This compact table summarizes the most actionable knowledge-base fields for Autosomal Dominant Hypercholesterolemia 3, emphasizing what is directly supported for the PCSK9-related subtype versus what is only available for familial hypercholesterolemia more broadly.*

## 1. Disease information

### Definition and identifiers

ADH3 is a congenital, chronic Mendelian disorder of LDL metabolism caused by monoallelic PCSK9 GOF variants. It is clinically part of heterozygous familial hypercholesterolemia and is characterized by elevated LDL-C from early life, cholesterol deposition in tendons/skin/cornea, and premature atherosclerotic cardiovascular disease (ASCVD).

* **MONDO:** MONDO:0011369, hypercholesterolemia, autosomal dominant, 3.
* **OMIM:** **603776**, Hypercholesterolemia, autosomal dominant, 3; causal gene **PCSK9**, OMIM **607786**. These OMIM numbers are standard database mappings but were not directly returned by the retrieved full-text corpus.
* **Synonyms:** ADH3; FH3; PCSK9-related familial hypercholesterolemia; PCSK9-associated autosomal dominant hypercholesterolemia; familial hypercholesterolemia due to PCSK9 GOF.
* **MeSH umbrella terms:** Hypercholesterolemia; Hyperlipoproteinemia Type II; Familial Hypercholesterolemia. Trial metadata maps relevant studies to MeSH Hypercholesterolemia and Hyperlipoproteinemia Type II. (NCT05398029 chunk 1)
* **ICD:** There is generally no dedicated ADH3 code. ICD-10-CM **E78.01** represents familial hypercholesterolemia; ICD-11 coding is ordinarily at the familial/pure hypercholesterolemia level rather than PCSK9 subtype. Local verification is advisable before database ingestion.
* **Data provenance:** This report uses aggregated disease-level databases, publications, guidelines, and trial registries—not individual-patient EHR data. Some founding evidence derives from individual pedigrees.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The necessary upstream cause is a **germline, heterozygous PCSK9 GOF variant**. PCSK9 GOF may increase LDLR affinity, secretion or effective activity, impair inhibitory LDL binding, or otherwise augment LDLR degradation. Representative variants are p.Ser127Arg (S127R), p.Phe216Leu (F216L), p.Asp374Tyr (D374Y), and p.Arg496Trp (R496W). S127R, F216L, and D374Y cosegregate with hypercholesterolemia in reported families. (rosenson2019cholesterolloweringagents. pages 5-5, sarkar2022pathogenicgainoffunctionmutations pages 1-2)

### Genetic risk and modifiers

* The pathogenic PCSK9 allele is the primary risk factor; first-degree relatives have a **50% transmission probability**.
* Variant-specific function materially affects severity. D374Y increases PCSK9–LDLR affinity by at least tenfold in experimental evidence and is associated with severe disease. (rochemolina2015inductionofsustained pages 1-2)
* Polygenic LDL-C burden and variants in other lipid genes can modify FH expression. FH-wide modifier candidates include common-variant polygenic risk scores and genes producing overlapping dyslipidemias. (taranto2023geneticheterogeneityof pages 1-2, taranto2023geneticheterogeneityof pages 2-4)
* Elevated lipoprotein(a), diabetes, hypertension, smoking, and established ASCVD increase clinical risk even though they do not cause ADH3.

### Protective factors

* **Genetic:** PCSK9 loss-of-function (LOF) alleles lower LDL-C and lifetime ASCVD risk; biallelic human PCSK9 deficiency has been observed with very low LDL-C and no major syndromic phenotype. A UK Biobank burden analysis in Open Targets reported an odds ratio of **0.228** for a PCSK9-LOF association (P=2.25×10⁻¹⁸), although this is protective population evidence, not an ADH3 modifier study. (OpenTargets Search: familial hypercholesterolemia-PCSK9, rosenson2019cholesterolloweringagents. pages 5-5)
* **Environmental/clinical:** avoidance of tobacco, a diet low in saturated/trans fats, exercise, healthy weight, and control of blood pressure/diabetes reduce total cardiovascular risk. They do **not** normalize the genetically elevated LDL-C and should not replace pharmacotherapy.

### Gene–environment interaction

The clinically important interaction is cumulative “cholesterol-years.” A PCSK9 GOF allele raises LDL-C from childhood; smoking, diabetes, hypertension, poor diet, and inactivity add vascular risk, whereas early sustained LDL lowering reduces cumulative arterial exposure. FH-wide analysis estimates that a CHD-producing LDL burden is reached at about **12.5 years** in FH versus roughly **55 years** without FH. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9, ray2022worldheartfederation pages 1-2)

No infectious, toxic, occupational, or radiation exposure is established as a cause of ADH3.

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Elevated LDL-C | Laboratory abnormality; present from childhood, chronic and untreated progressive in cumulative impact; magnitude is variant- and treatment-dependent | **HP:0003141** Increased LDL cholesterol concentration |
| Hypercholesterolemia | Laboratory/diagnostic phenotype, generally highly penetrant but variable | **HP:0003124** Hypercholesterolemia |
| Tendon xanthoma | Physical sign; usually develops after prolonged exposure and may be absent, especially in young or screen-detected people | **HP:0001052** Xanthomatosis / **HP:0000991** Xanthoma |
| Xanthelasma/skin xanthoma | Physical manifestation; age-dependent and non-obligate | **HP:0000493** Xanthelasma |
| Corneal arcus | Physical sign, especially significant when premature | **HP:0001084** Corneal arcus |
| Premature coronary atherosclerosis/CAD | Major progressive complication; adult onset is usual in heterozygous disease but can occur earlier with severe variants | **HP:0001677** Coronary artery atherosclerosis; **HP:0001701** Angina pectoris |
| Myocardial infarction | Clinical complication of plaque disruption/ischemia | **HP:0001658** Myocardial infarction |
| Peripheral arterial disease | Less frequent than CAD but FH-wide risk is elevated | **HP:0004950** Peripheral arterial disease |

FH-wide guidelines report untreated CAD onset commonly at **30–50 years in men** and **50–70 years in women**, a 10–20-fold CAD risk relative to unaffected populations, and approximately 13-fold excess CAD risk in untreated heterozygous FH. Stroke association is less consistent. (haradashiba2023guidelinesforthe pages 2-4)

Published ADH3-only phenotype frequencies and validated quality-of-life estimates are not available from the retrieved evidence. Quality of life is affected indirectly through anxiety regarding inherited risk, lifelong medication/injections, dietary burden, screening, premature angina/MI, and procedural treatment. Screen-detected relatives may initially be asymptomatic; a 2023 Hong Kong study found cascade-detected adults had milder phenotypes than probands. (yip2023geneticspectrumand pages 1-2)

## 4. Genetic and molecular information

### Gene and protein

* **PCSK9**: HGNC **20001**; Ensembl ENSG00000169174; chromosome **1p32.3**.
* Protein: 692-aa secreted proprotein convertase with signal peptide, prodomain, catalytic domain, hinge, and C-terminal cysteine/histidine-rich domain. After autocleavage, the prodomain remains attached; LDLR degradation does not require further proteolytic activity because PCSK9 functions principally as a trafficking chaperone. (sarkar2022pathogenicgainoffunctionmutations pages 2-3, sundararaman2021pcsk9amultifaceted pages 2-4, cesaro2020beyondcholesterolmetabolism pages 1-2)

### Representative pathogenic variants

* **p.Ser127Arg:** prodomain missense GOF; nearly abolishes LDL binding, removing LDL-mediated inhibition of PCSK9 action. Direct in-vitro evidence showed that “LDL binding was nearly abolished” by S127R. (sarkar2022pathogenicgainoffunctionmutations pages 1-2)
* **p.Phe216Leu:** missense GOF, cosegregating with FH in a French family; reported mechanisms include enhanced PCSK9 function/secretion.
* **p.Asp374Tyr:** catalytic-domain missense GOF; markedly increases affinity for the LDLR EGF-A domain and produces a severe phenotype. (sarkar2022pathogenicgainoffunctionmutations pages 2-3, rochemolina2015inductionofsustained pages 1-2)
* **p.Arg496Trp:** C-terminal CM1-domain missense GOF that inhibits LDL association. (sarkar2022pathogenicgainoffunctionmutations pages 1-2)

These are **germline**, not somatic, variants. Population allele frequencies are expected to be very rare and should be extracted per genomic build and transcript directly from gnomAD/ClinVar. No single frequency can safely represent all variants. Classification should use current ClinVar/ClinGen assertions and ACMG/AMP criteria; not every PCSK9 missense variant is pathogenic.

### Other genomic fields

No recurrent aneuploidy, translocation, repeat expansion, mitochondrial variant, or disease-defining epigenetic lesion is established. Germline mosaicism and anticipation are not recognized characteristic mechanisms. Modifier genes/PRS may alter severity, but no ADH3-specific modifier has sufficient evidence for routine clinical annotation. (taranto2023geneticheterogeneityof pages 1-2)

## 5. Environmental information

ADH3 is not environmentally caused. Saturated-fat intake, obesity, inactivity, smoking, diabetes, hypertension, and possibly high Lp(a) amplify LDL burden or vascular consequences. Exercise, cardioprotective diet, weight control, and tobacco avoidance are supportive risk-reduction measures. No pathogen, toxin, pollution exposure, or occupational agent is known to initiate the Mendelian disorder.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** monoallelic PCSK9 GOF variant.
2. **Protein-level effect:** increased PCSK9 activity/LDLR affinity or loss of normal LDL-mediated restraint.
3. **Cellular effect:** secreted PCSK9 binds LDLR on hepatocytes and directs the PCSK9–LDLR complex to endosomes/lysosomes rather than allowing receptor recycling.
4. **Metabolic effect:** fewer surface LDLRs reduce hepatic receptor-mediated LDL uptake, increasing plasma LDL-C and apoB-particle residence time.
5. **Tissue injury:** LDL enters the arterial intima, undergoes modification, and drives macrophage foam-cell formation, inflammation, smooth-muscle responses, necrotic-core formation, and fibrous plaque.
6. **Clinical expression:** xanthomas/corneal lipid deposition and premature CAD, MI, and peripheral arterial disease. (rosenson2019cholesterolloweringagents. pages 3-5, sarkar2022pathogenicgainoffunctionmutations pages 2-3, cesaro2020beyondcholesterolmetabolism pages 1-2)

PCSK9 may additionally promote macrophage activation through lipid-dependent and LDLR-independent pathways. Proposed downstream pathways include ApoER2 degradation, NF-κB activation, and increased TNF-α, IL-1β, and IL-6. These pleiotropic mechanisms are biologically plausible but less firmly established as necessary causes of ADH3 than hepatic LDLR degradation. A 2024 expert review notes that PCSK9 inhibitors reduce events without clearly reducing systemic hs-CRP, arguing against overinterpreting systemic anti-inflammatory effects. (rosenson2019cholesterolloweringagents. pages 3-5, katsuki2024theroleof pages 1-2)

### Suggested ontology annotations

* **GO biological process:** receptor-mediated endocytosis (GO:0006898); cholesterol homeostasis (GO:0042632); regulation of plasma lipoprotein-particle levels (GO:0097006); low-density lipoprotein particle clearance (GO:0034383); lysosomal protein catabolic process (GO:1905146); inflammatory response (GO:0006954); foam-cell differentiation (GO:0050727).
* **GO cellular component:** extracellular region (GO:0005576); plasma membrane (GO:0005886); endosome (GO:0005768); lysosome (GO:0005764); endoplasmic reticulum (GO:0005783); Golgi apparatus (GO:0005794).
* **Cell Ontology:** hepatocyte (**CL:0000182**), macrophage (**CL:0000235**), endothelial cell (**CL:0000115**), vascular-associated smooth-muscle cell (**CL:0000359**), dendritic cell (**CL:0000451**), T cell (**CL:0000084**).

### Molecular profiling and advanced technology

No validated ADH3-specific diagnostic transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature was identified. The actionable molecular profile remains high LDL-C plus a pathogenic PCSK9 GOF allele. Human iPSC hepatocyte and organoid platforms are increasingly useful for lipoprotein biology, but retrieved patient-specific work primarily modeled LDLR-null FH, not ADH3. Consequently, these technologies should be annotated as emerging research platforms rather than established ADH3 diagnostics.

## 7. Anatomical structures affected

* **Primary metabolic organ:** liver—hepatocytes synthesize most circulating PCSK9 and clear LDL through LDLR. Suggested UBERON: liver **UBERON:0002107**.
* **Primary injured system:** arterial tree, especially coronary arteries and aorta; carotid and peripheral arteries may also be involved. Suggested terms: artery **UBERON:0001637**, aorta **UBERON:0000947**, coronary artery **UBERON:0001621**.
* **Secondary deposits:** Achilles and other tendons, skin, eyelids, and corneal periphery.
* **Subcellular sites:** ER/Golgi for PCSK9 synthesis and secretion; plasma membrane for LDLR binding; endosome/lysosome for receptor degradation.
* **Laterality:** systemic and generally bilateral/non-lateralized; coronary lesions are anatomically heterogeneous rather than predictably unilateral.

## 8. Temporal development

The molecular phenotype begins at or before birth because the variant is constitutional, although clinical signs are often absent in childhood. LDL-C elevation is stable/chronic; arterial damage is slowly progressive and proportional to cumulative exposure. Tendon xanthomas and corneal arcus are age-dependent. Untreated clinical CAD generally emerges in adulthood, earlier in men and in severe GOF variants. The disease is lifelong, without spontaneous remission. Treatment can normalize or greatly reduce LDL-C and stabilize/regress plaque but does not remove the inherited allele. The critical intervention period is childhood or as soon after diagnosis as possible. FH guidance recommends statins around ages **8–10 years**, with pediatric targets individualized by risk. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9)

## 9. Inheritance and population

ADH3 is autosomal dominant, affecting all sexes. Penetrance is high for LDL-C elevation but age-dependent and incompletely quantified for each variant; clinical ASCVD penetrance is incomplete because it depends on variant effect, treatment, sex, age, Lp(a), and conventional risk factors. Expressivity is variable. Anticipation and a consanguinity requirement are not expected. Homozygosity or compound genetic states can produce much more severe FH, but this is exceptionally rare.

There is **no robust ADH3-specific prevalence or incidence estimate**. FH-wide meta-analysis of 62 studies and >7.3 million people estimated heterozygous FH prevalence at **1:311** (95% CI 1:250–1:397), about 25 million people globally, and **1:17** among ASCVD populations. (hu2020prevalenceoffamilial pages 11-11, hu2020prevalenceoffamilial pages 1-2) A separate meta-analysis estimated 0.33% (1:303), ranging from 1:192 among Black participants to 1:400 among Asian participants; these are all-gene FH estimates affected by ascertainment and founder effects and must not be assigned directly to ADH3. (toftnielsen2022familialhypercholesterolemiaprevalence pages 1-3)

## 10. Diagnostics

### Clinical evaluation

1. Repeat fasting or nonfasting lipid profile: total cholesterol, calculated/direct LDL-C, HDL-C, triglycerides, non-HDL-C, apoB; measure Lp(a) at least once.
2. Document pretreatment LDL-C, premature CAD, tendon/skin xanthomas, corneal arcus, and three-generation family history.
3. Exclude secondary hypercholesterolemia: hypothyroidism, nephrotic syndrome, cholestatic liver disease, uncontrolled diabetes, medications, and diet-related dyslipidemia.
4. Apply a validated FH framework such as Dutch Lipid Clinic Network, Simon Broome, MEDPED, or national criteria.
5. Assess vascular burden as clinically indicated: ECG/stress testing, coronary CT angiography or calcium assessment, carotid ultrasound, and Achilles-tendon radiography/ultrasound. Japanese 2023 guidance uses Achilles thresholds of **≥8.0 mm in men** and **≥7.5 mm in women**. (haradashiba2023guidelinesforthe pages 1-2)

### Genetic testing

Preferred testing is an FH panel containing **LDLR, APOB, PCSK9, LDLRAP1**, and often APOE plus phenocopy genes **ABCG5, ABCG8, LIPA, CYP27A1**. Sequence and deletion/duplication analysis should be included. A pathogenic/likely pathogenic PCSK9 GOF variant establishes molecular ADH3 and enables targeted cascade testing. (taranto2023geneticheterogeneityof pages 1-2)

Single-gene PCSK9 testing is appropriate when a familial variant is known. WES/WGS is useful for unresolved severe or atypical cases but is not first-line when a validated panel is available. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine. RNA-seq may help resolve selected splice variants but is not standard diagnosis.

Differential diagnoses include LDLR-FH1, APOB-FH2, autosomal-recessive LDLRAP1 disease, polygenic hypercholesterolemia, sitosterolemia, cerebrotendinous xanthomatosis, lysosomal-acid-lipase deficiency, familial combined hyperlipidemia, and secondary hypercholesterolemia.

Cascade screening is a high-value real-world application. In a 2023 Hong Kong series, 31 probands plus 15 relatives were tested; cascade-detected adults had less severe phenotypes and would often have missed local testing criteria. (yip2023geneticspectrumand pages 1-2)

## 11. Outcomes and prognosis

Untreated prognosis is dominated by premature CAD/MI. FH-wide historical data reported cardiac death in **73% of men and 64% of women**, with mean death age around 63 years before statins; mean age increased to 76 years after statin availability. These figures are historical FH-wide estimates, not ADH3-specific survival rates. (haradashiba2023guidelinesforthe pages 1-2)

Prognostic factors include cumulative untreated LDL-C, PCSK9 variant severity, age at treatment, achieved LDL-C, smoking, male sex at younger ages, diabetes, hypertension, Lp(a), and existing ASCVD. There is no validated ADH3-specific 5- or 10-year survival model. Recovery from the genotype does not occur, but cardiovascular excess risk is substantially modifiable through early sustained LDL reduction.

## 12. Treatment

### Current algorithm

1. **Lifestyle and adherence support** for every patient.
2. **High-intensity statin**—atorvastatin or rosuvastatin—as first-line therapy. Atorvastatin 80 mg can reduce LDL-C by about 50%. (damase2024establishedandemerging pages 1-3)
3. Add **ezetimibe** if the target is not reached.
4. Add a **PCSK9 monoclonal antibody**, alirocumab or evolocumab, in very-high-risk disease, inadequate control, or statin intolerance. These agents prevent extracellular PCSK9 from binding LDLR and lower LDL-C by up to approximately **60%**; outcome trials totaling about 46,000 high-risk participants showed roughly **15% relative cardiovascular-risk reduction** over 2.2–2.8 years. (katzmann2020pcsk9inhibitioninsights pages 1-2)
5. Consider **inclisiran**, a hepatocyte-directed siRNA suppressing PCSK9 synthesis, or **bempedoic acid**, particularly where adherence, injection frequency, or statin intolerance is important. A 2024 systematic review reported sustained approximately **50% LDL-C reduction** with inclisiran dosed initially, at 90 days, then every six months. (rajendran2024acomparativeanalysis pages 1-2)
6. **Lipoprotein apheresis** for severe, refractory disease or progressive ASCVD despite maximal medication.

For very-high-risk FH with ASCVD, a commonly recommended goal is **≥50% LDL-C reduction and <55 mg/dL (<1.4 mmol/L)**. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9)

### Adverse effects and pharmacogenomics

Statins may cause myalgia and rarely myopathy/rhabdomyolysis; ezetimibe is usually well tolerated. PCSK9 antibodies chiefly cause injection-site reactions. Inclisiran also causes injection-site reactions; long-term cardiovascular outcome evidence has historically lagged its LDL-lowering evidence. Bempedoic acid may increase uric acid/gout and cholelithiasis. No validated PCSK9-GOF genotype-specific drug-dose rule exists: therapy is guided by baseline risk and achieved LDL-C.

### Trials and advanced therapeutics

* **NCT05398029 (VERVE-101):** completed phase 1, open-label, 13 adults with HeFH, ASCVD, and uncontrolled LDL-C; liver-directed base editing was designed to disrupt PCSK9. This edits a therapeutic target rather than correcting the familial GOF allele itself. (NCT05398029 chunk 1)
* **NCT02624869 (HAUSER-OLE):** 163 participants aged 10–17; evolocumab 420 mg every four weeks for up to 80 weeks. (NCT02624869 chunk 1)
* **NCT04652726 (ORION-16):** randomized phase 3 inclisiran study in 141 adolescents with HeFH; dosing at days 1, 90, and 270 during year 1. (NCT04652726 chunk 1)
* **NCT05465278 (ARCHITECT):** phase 4, 104 molecularly diagnosed FH participants; alirocumab 150 mg every two weeks with coronary CT plaque assessment over 18 months. (NCT05465278 chunk 1)

A 2024 *Circulation* review concluded that DNA- and RNA-based therapeutics may transform FH care as formulation stability and liver-specific delivery improve, but permanent editing requires continued assessment of off-target editing, hepatic toxicity, immunogenicity, and durability. DOI: https://doi.org/10.1161/CIRCULATIONAHA.123.067957, published August 2024. (damase2024establishedandemerging pages 1-3)

Suggested NCIt intervention concepts include statin therapy, ezetimibe, alirocumab, evolocumab, inclisiran, bempedoic acid, lipoprotein apheresis, genetic counseling, and therapeutic gene editing; exact NCIt codes should be validated against the current NCIt release.

## 13. Prevention

* **Primary prevention of genotype:** not possible through lifestyle or vaccination. Genetic counseling, reproductive options, prenatal diagnosis, and preimplantation genetic testing may be discussed after identifying a familial pathogenic variant.
* **Secondary prevention:** universal or targeted childhood lipid screening, opportunistic adult case finding, and cascade genetic/lipid screening. Each first-degree relative has a 50% prior probability.
* **Tertiary prevention:** early, intensive, sustained LDL lowering; tobacco avoidance; treatment of hypertension/diabetes; antiplatelet and other secondary-ASCVD measures when otherwise indicated.
* **Public health:** affordable lipid testing, FH registries, cascade-screening services, and access to statins/combination therapy. The World Heart Federation emphasizes universal screening for inherited dyslipidemias and life-course prevention because apoB/LDL exposure is cumulative. (ray2022worldheartfederation pages 1-2)
* **Immunization:** no approved vaccine prevents ADH3. A PCSK9 nanoparticle vaccine remains experimental. (fang2024developmentofa pages 1-3)

## 14. Other species and natural disease

PCSK9 and LDLR biology is evolutionarily conserved across mammals. No well-established common, naturally occurring veterinary counterpart caused by spontaneous PCSK9 GOF was identified. Most nonhuman evidence is engineered rather than natural disease. Therefore, breed prevalence, zoonotic transmission, and cross-species infectious susceptibility are not applicable. ADH3 is not transmissible.

Relevant taxa are *Mus musculus* (NCBI Taxonomy **10090**) and *Sus scrofa* (**9823**). Orthologous Pcsk9/PCSK9 regulates LDLR turnover in both species.

## 15. Model organisms

### Mouse

A single liver-targeted AAV dose expressing human **PCSK9-D374Y** in wild-type mice produced sustained LDL elevation, macrophage-rich aortic lesions, and fibrous caps, especially with high-fat feeding. The model used 3.5×10¹⁰ AAV particles and avoided lengthy genetic crosses; ApoE deficiency approximately doubled lesion burden. Published January 2015, DOI: https://doi.org/10.1161/ATVBAHA.114.303617. (rochemolina2015inductionofsustained pages 1-2)

Applications include rapid atherosclerosis induction, modifier-gene testing, imaging, and therapeutic evaluation. Limitations include supraphysiologic vector expression, dietary dependence, species-specific lipoprotein metabolism, and incomplete reproduction of decades-long human disease.

### Pig/minipig

Liver-specific human PCSK9-D374Y transgenic Yucatan minipigs show hepatic LDLR depletion, hypercholesterolemia, and coronary/aortic atherosclerotic lesions. Their anatomy and lipoprotein physiology make them useful for imaging and interventional translation. However, reported models did not reliably reproduce human plaque rupture or thrombosis. (perleberg2018geneticallyengineeredpigs pages 4-4, rochemolina2015inductionofsustained pages 10-10)

### Recent application

A June 2024 *Cell Reports Medicine* study used high-fat-diet and AAV-hPCSK9-D374Y mice to test a ferritin nanoparticle PCSK9 vaccine. Vaccination reduced serum lipids, aortic plaque area, and macrophage infiltration through an LDLR- and T-follicular-helper-cell-dependent mechanism. This is preclinical evidence, not an approved preventive treatment. DOI: https://doi.org/10.1016/j.xcrm.2024.101614. (fang2024developmentofa pages 1-3)

## Key direct quotations from retrieved abstracts

* 2023 adult guideline: “Familial hypercholesterolemia (FH) is an autosomal hereditary disorder characterized by hyperLDL cholesterolemia (LDL-C), premature coronary artery disease (CAD), and tendon and skin xanthomas.” Published May 2023; DOI: https://doi.org/10.5551/jat.CR005. (haradashiba2023guidelinesforthe pages 1-2)
* 2022 mechanistic study: “Gain-of-function (GOF) point mutations in PCSK9 are associated with familial hypercholesterolemia.” Published September 2022; DOI: https://doi.org/10.3389/fphys.2022.960272. (sarkar2022pathogenicgainoffunctionmutations pages 1-2)
* 2024 nucleic-acid review: “DNA- and RNA-based therapeutics have the potential to transform the care of patients with FH.” Published August 2024; DOI: https://doi.org/10.1161/CIRCULATIONAHA.123.067957. (damase2024establishedandemerging pages 1-3)
* 2020 prevalence meta-analysis: “With an overall prevalence of 1:311, FH is among the commonest genetic disorders in the GP.” Published June 2020; DOI: https://doi.org/10.1161/CIRCULATIONAHA.119.044795. This quotation concerns all heterozygous FH, not ADH3 alone. (hu2020prevalenceoffamilial pages 1-2)

## Overall assessment

The evidence establishing **PCSK9 GOF as the cause of ADH3 is strong**, supported by cosegregation in human pedigrees, biochemical effects on LDLR trafficking, animal phenocopy, and the clinical success of PCSK9 inhibition. The most important unresolved knowledge-base gaps are ADH3-specific prevalence, penetrance by variant, longitudinal quality-of-life data, validated molecular-omics signatures, and comparative treatment outcomes stratified specifically by PCSK9 GOF genotype.

References

1. (OpenTargets Search: familial hypercholesterolemia-PCSK9): Open Targets Query (familial hypercholesterolemia-PCSK9, 11 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (NCT05398029 chunk 1):  A Study of VERVE-101 in Patients With Familial Hypercholesterolemia and Cardiovascular Disease. Verve Therapeutics, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05398029

3. (cesaro2020beyondcholesterolmetabolism pages 1-2): Arturo Cesaro, Vanessa Bianconi, Felice Gragnano, Elisabetta Moscarella, Fabio Fimiani, Emanuele Monda, Olga Scudiero, Giuseppe Limongelli, Matteo Pirro, and Paolo Calabrò. Beyond cholesterol metabolism: the pleiotropic effects of proprotein convertase subtilisin/kexin type 9 (pcsk9). genetics, mutations, expression, and perspective for long‐term inhibition. BioFactors, 46:367-380, Jan 2020. URL: https://doi.org/10.1002/biof.1619, doi:10.1002/biof.1619. This article has 75 citations and is from a peer-reviewed journal.

4. (abifadel2023geneticandmolecular pages 1-2): Marianne Abifadel and Catherine Boileau. Genetic and molecular architecture of familial hypercholesterolemia. Oct 2023. URL: https://doi.org/10.1111/joim.13577, doi:10.1111/joim.13577. This article has 186 citations and is from a domain leading peer-reviewed journal.

5. (sarkar2022pathogenicgainoffunctionmutations pages 1-2): Samantha K. Sarkar, Angela Matyas, Ikhuosho Asikhia, Zhenkun Hu, Mia Golder, Kaitlyn Beehler, Tanja Kosenko, and Thomas A. Lagace. Pathogenic gain-of-function mutations in the prodomain and c-terminal domain of pcsk9 inhibit ldl binding. Frontiers in Physiology, Sep 2022. URL: https://doi.org/10.3389/fphys.2022.960272, doi:10.3389/fphys.2022.960272. This article has 23 citations.

6. (sarkar2022pathogenicgainoffunctionmutations pages 2-3): Samantha K. Sarkar, Angela Matyas, Ikhuosho Asikhia, Zhenkun Hu, Mia Golder, Kaitlyn Beehler, Tanja Kosenko, and Thomas A. Lagace. Pathogenic gain-of-function mutations in the prodomain and c-terminal domain of pcsk9 inhibit ldl binding. Frontiers in Physiology, Sep 2022. URL: https://doi.org/10.3389/fphys.2022.960272, doi:10.3389/fphys.2022.960272. This article has 23 citations.

7. (rosenson2019cholesterolloweringagents. pages 5-5): Robert S. Rosenson, Robert A. Hegele, and Wolfgang Koenig. Cholesterol-lowering agents. Circulation research, 124 3:364-385, Feb 2019. URL: https://doi.org/10.1161/circresaha.118.313238, doi:10.1161/circresaha.118.313238. This article has 67 citations and is from a highest quality peer-reviewed journal.

8. (rosenson2019cholesterolloweringagents. pages 3-5): Robert S. Rosenson, Robert A. Hegele, and Wolfgang Koenig. Cholesterol-lowering agents. Circulation research, 124 3:364-385, Feb 2019. URL: https://doi.org/10.1161/circresaha.118.313238, doi:10.1161/circresaha.118.313238. This article has 67 citations and is from a highest quality peer-reviewed journal.

9. (sundararaman2021pcsk9amultifaceted pages 2-4): Sai Sahana Sundararaman, Yvonne Döring, and Emiel P C Van Der Vorst. Pcsk9: a multi-faceted protein that is involved in cardiovascular biology. JournalArticle, Jul 2021. URL: https://doi.org/10.48350/157973, doi:10.48350/157973. This article has 80 citations.

10. (haradashiba2023guidelinesforthe pages 2-4): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 108 citations and is from a peer-reviewed journal.

11. (fularski2024unveilingfamilialhypercholesterolemia—review pages 1-2): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

12. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

13. (haradashiba2023guidelinesforthe pages 1-2): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 108 citations and is from a peer-reviewed journal.

14. (yip2023geneticspectrumand pages 1-2): Man-Kwan Yip, Elaine Kwan, Jenny Leung, Emmy Lau, and Wing-Tat Poon. Genetic spectrum and cascade screening of familial hypercholesterolemia in routine clinical setting in hong kong. Genes, 14:2071, Nov 2023. URL: https://doi.org/10.3390/genes14112071, doi:10.3390/genes14112071. This article has 6 citations.

15. (damase2024establishedandemerging pages 1-3): Tulsi R. Damase, Roman Sukhovershin, Biana Godin, Khurram Nasir, and John P. Cooke. Established and emerging nucleic acid therapies for familial hypercholesterolemia. Circulation, 150:724-735, Aug 2024. URL: https://doi.org/10.1161/circulationaha.123.067957, doi:10.1161/circulationaha.123.067957. This article has 8 citations and is from a highest quality peer-reviewed journal.

16. (katzmann2020pcsk9inhibitioninsights pages 1-2): Julius L. Katzmann, Ioanna Gouni-Berthold, and Ulrich Laufs. Pcsk9 inhibition: insights from clinical trials and future prospects. Frontiers in Physiology, Nov 2020. URL: https://doi.org/10.3389/fphys.2020.595819, doi:10.3389/fphys.2020.595819. This article has 103 citations.

17. (rajendran2024acomparativeanalysis pages 1-2): Yazhini Rajendran, Madhumita Nandhakumar, Madhavi Eerike, Nikhila Kondampati, Kalpana Mali, Leo F Chalissery, Venu Gopala R Konda, and Uma Maheswari Nagireddy. A comparative analysis of low-density lipoprotein cholesterol (ldl-c)-lowering activities of bempedoic acid, inclisiran, and pcsk9 inhibitors: a systematic review. Cureus, Sep 2024. URL: https://doi.org/10.7759/cureus.69900, doi:10.7759/cureus.69900. This article has 6 citations.

18. (hu2020prevalenceoffamilial pages 11-11): Pengwei Hu, Kanika I. Dharmayat, Christophe A.T. Stevens, Mansour T.A. Sharabiani, Rebecca S. Jones, Gerald F. Watts, Jacques Genest, Kausik K. Ray, and Antonio J. Vallejo-Vaz. Prevalence of familial hypercholesterolemia among the general population and patients with atherosclerotic cardiovascular disease. Circulation, 141:1742-1759, Jun 2020. URL: https://doi.org/10.1161/circulationaha.119.044795, doi:10.1161/circulationaha.119.044795. This article has 669 citations and is from a highest quality peer-reviewed journal.

19. (hu2020prevalenceoffamilial pages 1-2): Pengwei Hu, Kanika I. Dharmayat, Christophe A.T. Stevens, Mansour T.A. Sharabiani, Rebecca S. Jones, Gerald F. Watts, Jacques Genest, Kausik K. Ray, and Antonio J. Vallejo-Vaz. Prevalence of familial hypercholesterolemia among the general population and patients with atherosclerotic cardiovascular disease. Circulation, 141:1742-1759, Jun 2020. URL: https://doi.org/10.1161/circulationaha.119.044795, doi:10.1161/circulationaha.119.044795. This article has 669 citations and is from a highest quality peer-reviewed journal.

20. (toftnielsen2022familialhypercholesterolemiaprevalence pages 1-3): Frida Toft-Nielsen, Frida Emanuelsson, and Marianne Benn. Familial hypercholesterolemia prevalence among ethnicities—systematic review and meta-analysis. Frontiers in Genetics, Feb 2022. URL: https://doi.org/10.3389/fgene.2022.840797, doi:10.3389/fgene.2022.840797. This article has 65 citations and is from a peer-reviewed journal.

21. (taranto2023geneticheterogeneityof pages 1-2): Maria Donata Di Taranto and Giuliana Fortunato. Genetic heterogeneity of familial hypercholesterolemia: repercussions for molecular diagnosis. International Journal of Molecular Sciences, 24:3224, Feb 2023. URL: https://doi.org/10.3390/ijms24043224, doi:10.3390/ijms24043224. This article has 52 citations.

22. (NCT05465278 chunk 1):  Alirocumab and Plaque Burden In Familial Hypercholesterolaemia. Fundación Hipercolesterolemia Familiar. 2018. ClinicalTrials.gov Identifier: NCT05465278

23. (NCT02624869 chunk 1):  Safety, Tolerability and Efficacy of Evolocumab (AMG 145) in Children With Inherited Elevated Low-density Lipoprotein Cholesterol (Familial Hypercholesterolemia). Amgen. 2016. ClinicalTrials.gov Identifier: NCT02624869

24. (NCT04652726 chunk 1):  Study to Evaluate Efficacy and Safety of Inclisiran in Adolescents With Heterozygous Familial Hypercholesterolemia. Novartis Pharmaceuticals. 2021. ClinicalTrials.gov Identifier: NCT04652726

25. (rochemolina2015inductionofsustained pages 1-2): Marta Roche-Molina, David Sanz-Rosa, Francisco M. Cruz, Jaime García-Prieto, Sergio López, Rocío Abia, Francisco J.G. Muriana, Valentín Fuster, Borja Ibáñez, and Juan A. Bernal. Induction of sustained hypercholesterolemia by single adeno-associated virus–mediated gene transfer of mutant hpcsk9. Arteriosclerosis, Thrombosis, and Vascular Biology, 35:50–59, Jan 2015. URL: https://doi.org/10.1161/atvbaha.114.303617, doi:10.1161/atvbaha.114.303617. This article has 233 citations and is from a domain leading peer-reviewed journal.

26. (perleberg2018geneticallyengineeredpigs pages 4-4): Carolin Perleberg, Alexander Kind, and Angelika Schnieke. Genetically engineered pigs as models for human disease. Disease Models & Mechanisms, Jan 2018. URL: https://doi.org/10.1242/dmm.030783, doi:10.1242/dmm.030783. This article has 257 citations and is from a domain leading peer-reviewed journal.

27. (fang2024developmentofa pages 1-3): Qiannan Fang, Xinyu Lu, Yuanqiang Zhu, Xi Lv, Fei Yu, Xiancai Ma, Bingfeng Liu, and Hui Zhang. Development of a pcsk9-targeted nanoparticle vaccine to effectively decrease the hypercholesterolemia. Cell Reports Medicine, 5:101614, Jun 2024. URL: https://doi.org/10.1016/j.xcrm.2024.101614, doi:10.1016/j.xcrm.2024.101614. This article has 32 citations and is from a peer-reviewed journal.

28. (katsuki2024theroleof pages 7-7): Shunsuke Katsuki, Prabhash Kumar Jha, Elena Aikawa, and Masanori Aikawa. The role of proprotein convertase subtilisin/kexin 9 (pcsk9) in macrophage activation: a focus on its ldl receptor-independent mechanisms. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1431398, doi:10.3389/fcvm.2024.1431398. This article has 14 citations and is from a peer-reviewed journal.

29. (taranto2023geneticheterogeneityof pages 2-4): Maria Donata Di Taranto and Giuliana Fortunato. Genetic heterogeneity of familial hypercholesterolemia: repercussions for molecular diagnosis. International Journal of Molecular Sciences, 24:3224, Feb 2023. URL: https://doi.org/10.3390/ijms24043224, doi:10.3390/ijms24043224. This article has 52 citations.

30. (ray2022worldheartfederation pages 1-2): Kausik K. Ray, Brian A. Ference, Tania Séverin, Dirk Blom, Stephen J. Nicholls, Mariko H. Shiba, Wael Almahmeed, Rodrigo Alonso, Magdalena Daccord, Marat Ezhov, Rosa Fernández Olmo, Piotr Jankowski, Fernando Lanas, Roopa Mehta, Raman Puri, Nathan D. Wong, David Wood, Dong Zhao, Samuel S. Gidding, Salim S. Virani, Donald Lloyd-Jones, Fausto Pinto, Pablo Perel, and Raul D. Santos. World heart federation cholesterol roadmap 2022. Global Heart, 17:75, Oct 2022. URL: https://doi.org/10.5334/gh.1154, doi:10.5334/gh.1154. This article has 189 citations and is from a peer-reviewed journal.

31. (katsuki2024theroleof pages 1-2): Shunsuke Katsuki, Prabhash Kumar Jha, Elena Aikawa, and Masanori Aikawa. The role of proprotein convertase subtilisin/kexin 9 (pcsk9) in macrophage activation: a focus on its ldl receptor-independent mechanisms. Frontiers in Cardiovascular Medicine, Aug 2024. URL: https://doi.org/10.3389/fcvm.2024.1431398, doi:10.3389/fcvm.2024.1431398. This article has 14 citations and is from a peer-reviewed journal.

32. (rochemolina2015inductionofsustained pages 10-10): Marta Roche-Molina, David Sanz-Rosa, Francisco M. Cruz, Jaime García-Prieto, Sergio López, Rocío Abia, Francisco J.G. Muriana, Valentín Fuster, Borja Ibáñez, and Juan A. Bernal. Induction of sustained hypercholesterolemia by single adeno-associated virus–mediated gene transfer of mutant hpcsk9. Arteriosclerosis, Thrombosis, and Vascular Biology, 35:50–59, Jan 2015. URL: https://doi.org/10.1161/atvbaha.114.303617, doi:10.1161/atvbaha.114.303617. This article has 233 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Hypercholesterolemia_3-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 24 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.