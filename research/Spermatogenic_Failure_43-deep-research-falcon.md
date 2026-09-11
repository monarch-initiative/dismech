---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T13:09:01.017973'
end_time: '2026-09-03T13:20:27.581560'
duration_seconds: 686.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spermatogenic failure 43 (SPGF43, biallelic SPEF2 variants)
  mondo_id: MONDO:0032898
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 8
  verified: 8
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032898
    reported_labels:
    - if available
    ontology_label: spermatogenic failure 43
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spermatogenic_Failure_43-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic failure 43 (SPGF43, biallelic SPEF2 variants)
- **MONDO ID:** MONDO:0032898 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic failure 43 (SPGF43, biallelic SPEF2 variants)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Spermatogenic failure 43 (SPGF43, biallelic SPEF2 variants)
- **MONDO ID:** MONDO:0032898 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic failure 43 (SPGF43, biallelic SPEF2 variants)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Spermatogenic failure 43 (SPGF43; biallelic **SPEF2** variants)

## Executive summary

SPGF43 is an ultra-rare, autosomal-recessive male-infertility disorder caused by biallelic pathogenic variants in **SPEF2**. Its defining laboratory phenotype is severe asthenoteratozoospermia—usually multiple morphological abnormalities of the sperm flagella (MMAF)—with absent, short, coiled, bent, or irregular-calibre tails and nearly absent progressive motility. Human ultrastructural and protein studies place SPEF2 in assembly and function of the sperm axonemal central-pair apparatus, particularly the C1b projection, and implicate defective intraflagellar/intramanchette cargo transport. Some individuals also have chronic upper- or lower-airway symptoms compatible with primary ciliary dyskinesia (PCD), whereas others have isolated infertility; this likely reflects variant- and transcript-dependent expressivity. The current practical applications are molecular diagnosis, reproductive counseling, assessment for PCD, and intracytoplasmic sperm injection (ICSI). There is no established pharmacologic, gene, RNA, or cell therapy and no SPEF2-specific registered clinical trial identified in the search.

The evidence base remains small: the principal reports comprise individual patients or small families ascertained through infertility/MMAF or PCD cohorts. Consequently, prevalence, penetrance, natural history, genotype–phenotype correlations, and treatment-response estimates are not yet population-level quantities.

## 1. Disease information

**Definition.** SPGF43 is the disease-level designation for recessive SPEF2-associated spermatogenic failure. The observable reproductive phenotype overlaps **MMAF**, a severe form of teratozoospermia in which sperm show a mosaic of absent, short, bent, coiled, and irregular-calibre flagella, accompanied by severe asthenozoospermia or complete immotility. The initial 2019 study identified SPEF2 variants in 2 of 42 Han Chinese men selected for MMAF and experimentally demonstrated reduced SPEF2 and disrupted axonemal/mitochondrial-sheath architecture. The authors’ abstract conclusion was: “loss-of-function mutations in the SPEF2 gene can cause the MMAF phenotype in human.” (liu2019lossoffunctionmutationsin pages 1-2)

**Identifiers and terminology.** The supplied disease identifier is **MONDO:0032898**. Common labels include *spermatogenic failure 43*, *SPGF43*, *SPEF2-related male infertility*, *SPEF2-associated MMAF*, and *male infertility due to multiple morphological abnormalities of the sperm flagella*. **SPEF2** is also historically called **KPL2** in animal literature. A distinct, broader phenotype may be described as SPEF2-related PCD or PCD-like disease. Disease-specific Orphanet, MeSH, ICD-10, and ICD-11 entries were not established in the retrieved literature; coding generally occurs under male infertility, abnormal sperm motility/morphology, or PCD rather than a dedicated SPGF43 code. The precise OMIM disease-number/gene-number pair and HGNC numeric identifier should be validated directly against the live OMIM/HGNC records before database ingestion rather than inferred from secondary papers.

**Data provenance.** Clinical findings come from individual patients and families recruited into research infertility/PCD cohorts. MONDO/OMIM-style entries are aggregated disease-level interpretations of those reports—not EHR-derived population surveillance.

## 2. Etiology, risk, and protective factors

The necessary cause is **biallelic germline SPEF2 dysfunction**, usually rare truncating, frameshift, canonical splice, or deleterious missense alleles. Homozygous disease is enriched in consanguineous pedigrees, while compound heterozygosity also occurs. The 2020 study reported three homozygous truncating alleles in two Han Chinese and one Iranian consanguineous family, inherited under a recessive model. Their frequencies in gnomAD were approximately 8×10⁻⁶, 4×10⁻⁶, and absent, respectively. (liu2020homozygousmutationsin pages 2-2, liu2020homozygousmutationsin pages 3-4)

No validated susceptibility loci, modifier genes, protective alleles, environmental causes, infectious triggers, or gene–environment interactions are known specifically for SPGF43. Smoking, heat, toxins, infection, varicocele, and age can impair semen quality generally, but they neither cause the Mendelian disorder nor explain its characteristic central-pair defect. No diet or lifestyle intervention has been shown to restore SPEF2-dependent flagellar assembly. Avoidance of general gonadotoxic exposures is reasonable reproductive care but is not disease-specific prevention.

Potential molecular modifiers include **HYDIN, CFAP69, IFT20, RSPH9**, and other central-pair/transport proteins, based on interaction or localization data, but none has been demonstrated to alter penetrance in human SPGF43. Mouse double-mutant experiments indicate interactions among central-pair genes, but extrapolation to human modifier effects remains experimental.

## 3. Phenotypes

### Core reproductive phenotype

* **Male infertility**—usually recognized in reproductive adulthood after failure to conceive; suggested HPO: **HP:0003251 Male infertility**.
* **Severe asthenozoospermia or complete sperm immotility**—progressive motility was 0% in all three men in one study and total motility was 0–0.6%; suggested HPO: **HP:0011961 Asthenozoospermia**.
* **Teratozoospermia/MMAF**—absent, short, coiled, bent/angulated, and irregular-calibre flagella; suggested HPO: **HP:0012864 Teratozoospermia** and, where supported by the current HPO release, the specific MMAF concept.
* **Oligozoospermia may coexist.** In three subjects, concentrations were 9.3, 10.4, and 21.0×10⁶/mL; suggested HPO: **HP:0000798 Oligospermia**. Semen volumes were normal-range at 2.9–4.0 mL. (liu2020homozygousmutationsin pages 4-5)
* **Axonemal central-pair absence**—TEM may show a 9+0 rather than normal 9+2 configuration; this is a pathology/ultrastructural finding rather than a conventional symptom HPO term. (liu2020homozygousmutationsin pages 3-4)
* **Mitochondrial-sheath and peri-axonemal disorganization** occur in some cases. (liu2019lossoffunctionmutationsin pages 1-2, li2022spermflagellar2 pages 4-6)

In the 2020 three-patient series, normal flagella represented only 13.5%, 30%, and 35% of counted sperm; short tails occurred in 48%, 25%, and 35%; absent tails in 28%, 18%, and 13%; coiled tails in 10%, 24%, and 7%; angulation in 0.5%, 2%, and 5%; and irregular calibre in 0%, 1%, and 5%. These are patient-level observations, not population frequencies. (liu2020homozygousmutationsin pages 4-5)

### Extra-reproductive phenotype

Earlier cohorts reported no bronchitis, sinusitis, pneumonia, or evident PCD; one subject had normal chest radiography and olfactory testing. (liu2019lossoffunctionmutationsin pages 1-2, liu2020homozygousmutationsin pages 5-6) In contrast, three 2024 patients had chronic wet cough, chronic sinusitis, and/or nasal congestion and were described as having likely PCD/PCD-like disease despite preserved respiratory-cilium ultrastructure. Suggested HPO terms include **HP:0032223 Chronic wet cough**, **HP:0011109 Chronic sinusitis**, and **HP:0000458 Anosmia** only when present. (lu2024novelspef2variants pages 1-2)

There is no established neurologic, behavioral, immune, metabolic, or endocrine syndrome in reported human SPGF43. Hydrocephalus and growth/bone abnormalities are prominent in some global Spef2-null mice but have not been established as human SPGF43 manifestations.

**Severity/course.** Reproductive severity is usually high and stable because malformed mature flagella cannot be repaired. Respiratory expressivity is variable. Quantified health-related quality-of-life data—EQ-5D, SF-36, PROMIS, or infertility-specific scores—are unavailable. Likely impacts include involuntary childlessness, treatment burden, psychological distress, and, where PCD occurs, chronic respiratory morbidity; these are clinically plausible but not measured specifically in SPGF43 cohorts.

A study-level summary follows.

| Study/date and URL/DOI | Cohort | SPEF2 variants | Core phenotype/quantitative findings | Respiratory/PCD findings | ART outcome |
|---|---|---|---|---|---|
| **Liu et al., May 2019**, *J Med Genet*; [doi:10.1136/jmedgenet-2018-105952](https://doi.org/10.1136/jmedgenet-2018-105952) | **2 SPEF2-positive men among 42** infertile Han Chinese men with MMAF; 10 fertile controls | P1: **c.12delC** and **c.1745-2A>G**; P2: **c.4102G>T** and **c.4323dupA**; reported as rare, potentially deleterious loss-of-function alleles | Severe asthenozoospermia with absent, short, bent, coiled, and/or irregular-calibre flagella; TEM showed disrupted axonemes and mitochondrial-sheath defects; sperm SPEF2 was significantly reduced by immunofluorescence and western blot (liu2019lossoffunctionmutationsin pages 1-2, liu2019lossoffunctionmutationsin pages 6-6) | No reported bronchitis, sinusitis, pneumonia, or other PCD-related symptoms; genital examination and bilateral testes were normal (liu2019lossoffunctionmutationsin pages 1-2) | P1: two blastocysts after ICSI and one embryo transferred, but **no pregnancy**; maternal age was noted as a possible contributor (liu2019lossoffunctionmutationsin pages 6-6) |
| **Liu et al., May 2020**, *J Med Genet*; [doi:10.1136/jmedgenet-2019-106011](https://doi.org/10.1136/jmedgenet-2019-106011) | **3 affected men** from unrelated consanguineous families: two Han Chinese and one Iranian | Homozygous **c.910C>T (p.Arg304\*)**, **c.3400delA (p.Ile1134Serfs\*13)**, and **c.3240delT (p.Phe1080Leufs\*2)**. gnomAD frequencies: **8×10⁻⁶, 4×10⁻⁶, and 0**, respectively (liu2020homozygousmutationsin pages 2-2, liu2020homozygousmutationsin pages 3-4) | Semen volume **2.9–4.0 mL**; concentration **9.3–21.0×10⁶/mL**; total motility **0–0.6%**; progressive motility **0%**. Normal flagella occurred in only **13.5–35%**; short flagella in **25–48%**. TEM showed central-pair loss and a **9+0** rather than 9+2 axoneme; SPEF2 and CFAP69 staining was absent or markedly reduced (liu2020homozygousmutationsin pages 4-5, liu2020homozygousmutationsin pages 3-4, liu2020homozygousmutationsin pages 5-6) | No obvious PCD-like manifestations documented; one subject had normal chest radiography and olfactory testing, without evident pulmonary or cardiac abnormality (liu2020homozygousmutationsin pages 5-6) | Not reported in the available evidence |
| **Li et al., online Nov 2021 / vol. 24, 2022**, *Asian J Androl*; [doi:10.4103/aja202154](https://doi.org/10.4103/aja202154) | Sperm proteomics from **3 SPEF2-mutant patients** | Previously identified pathogenic SPEF2 genotypes; individual variant notation was not restated in the extracted evidence | **1,262 differentially expressed proteins:** **486 upregulated** and **776 downregulated**. Reduced proteins included SPAG6, RSPH1/RSPH4A, DYNLT1, MNS1 and TOM20; IFT20 and other IFT proteins increased. SPEF2–IFT20 and SPEF2–RSPH9 interactions were experimentally supported, implicating central-pair, radial-spoke, mitochondrial-sheath, and cargo-transport defects (li2022spermflagellar2 pages 4-6, li2022spermflagellar2 pages 3-4, li2022spermflagellar2 pages 6-7) | Not evaluated or not reported in the extracted proteomic evidence | Not reported |
| **Aprea et al., 3 Feb 2023**, *Front Genet*; [doi:10.3389/fgene.2023.1117821](https://doi.org/10.3389/fgene.2023.1117821) | **2 SPEF2 cases within a 10-man cohort** carrying defects in six axonemal genes; overall cohort comprised eight men diagnosed with PCD and two with MMAF-associated infertility | Pathogenic SPEF2 variants were reported, but exact patient-level nomenclature and allele frequencies were not available in the extracted evidence | Andrological assessment plus sperm high-speed video, immunofluorescence, and TEM demonstrated abnormal flagellar composition; SPEF2 was absent or severely reduced in SPEF2-mutant sperm. The study positioned SPEF2 in the central-pair **C1b projection** and supported sperm immunofluorescence as a variant-classification aid (aprea2023pathogenicgenevariants pages 2-3) | Respiratory-cilia work-up was performed, but SPEF2-specific respiratory findings and definitive patient-level PCD classifications were not available in the extracted evidence | Not reported |
| **Lu et al., online 3 Apr 2024**, *J Assist Reprod Genet*; [doi:10.1007/s10815-024-03106-9](https://doi.org/10.1007/s10815-024-03106-9) | **3 affected men from 3 unrelated Han Chinese families** | F1: homozygous **c.4447+1G>A**; F2: compound heterozygous **c.1339C>T (p.Arg447\*)** and **c.1645G>T (p.Glu549\*)**; F3: homozygous **c.2524G>A (p.Asp842Asn)**, transcript **NM_024867.4**. All four were novel/very rare and experimentally supported as deleterious; exact database frequencies and formal ACMG classes were not available in the extracted evidence (lu2024novelspef2variants pages 1-2) | Male infertility with MMAF; mutant sperm had abnormal flagella and loss of the axonemal central-pair complex. Reported ICSI fertilization rates were **100%, 90%, and 82%** (lu2024novelspef2variants pages 12-13, lu2024novelspef2variants pages 1-2) | Chronic wet cough, chronic sinusitis, and/or nasal congestion supported **likely PCD/PCD-like disease**, although respiratory-cilium ultrastructure was reportedly unaffected; definitive PCD status therefore remains cautious (lu2024novelspef2variants pages 1-2) | Each couple underwent one ICSI cycle; **all three achieved healthy live births** (lu2024novelspef2variants pages 1-2, lu2024novelspef2variants pages 12-13) |


*Table: Compact study-level evidence for biallelic SPEF2-associated SPGF43, spanning initial human discovery through 2024 clinical expansion. It highlights cohort sizes, variants, quantitative sperm findings, respiratory involvement, and reported ICSI outcomes while preserving uncertainty.*

## 4. Genetic and molecular information

**Gene.** **SPEF2**, chromosome **5p13.2**, encodes sperm flagellar protein 2, a large, evolutionarily conserved ciliary/flagellar protein. Full-length protein annotations include a calponin-homology region, P-loop NTPase-like fold, EF-hand region, and an IFT20-binding region. Several tissue-specific transcripts are expressed; disruption of long testis transcripts may produce isolated infertility, while alleles affecting broadly expressed isoforms may increase PCD risk. This transcript explanation is plausible and supported by expression observations, but genotype–phenotype rules remain incomplete. (liu2020homozygousmutationsin pages 2-2, li2022spermflagellar2 pages 4-6)

**Reported pathogenic spectrum.** Examples include:

* Compound heterozygous c.12delC and c.1745-2A>G; compound heterozygous c.4102G>T and c.4323dupA (2019). (liu2019lossoffunctionmutationsin pages 1-2, liu2019lossoffunctionmutationsin pages 6-6)
* Homozygous c.910C>T (p.Arg304*), c.3400delA (p.Ile1134Serfs*13), and c.3240delT (p.Phe1080Leufs*2) (2020). These were absent from 1000 Genomes; ExAC frequencies were approximately 8.2×10⁻⁶, 8.3×10⁻⁶, and zero, and gnomAD frequencies approximately 8×10⁻⁶, 4×10⁻⁶, and zero. (liu2020homozygousmutationsin pages 3-4)
* Homozygous c.4447+1G>A; compound heterozygous c.1339C>T (p.Arg447*) plus c.1645G>T (p.Glu549*); and homozygous c.2524G>A (p.Asp842Asn), referenced to NM_024867.4 (2024). (lu2024novelspef2variants pages 1-2)

These are **germline**, not somatic, variants. Most demonstrated alleles act through loss of function, including nonsense-mediated decay, truncation, abnormal splicing, loss/reduction of protein, or disruption of functional domains. Formal ClinVar submissions and ACMG classifications should be assessed variant by variant; a published “pathogenic” assertion is not automatically equivalent to a current ClinVar expert-panel classification. The 2024 missense p.Asp842Asn has experimental support but warrants especially careful transcript, segregation, population-frequency, and functional review.

No recurrent chromosomal abnormality, repeat expansion, mitochondrial-DNA defect, pathogenic epimutation, or disease-specific methylation signature is established. No human modifier gene or somatic mosaic mechanism is proven.

## 5. Environmental information

SPGF43 is genetic. No toxin, pollutant, radiation exposure, occupation, diet, alcohol use, smoking pattern, or infectious agent has been linked specifically to its occurrence or penetrance. General semen-toxic exposures may add nonspecific impairment but have not been shown to interact with SPEF2. The disease is noninfectious and nontransmissible between persons.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic SPEF2 pathogenic variants lead to** absent, truncated, mis-spliced, or dysfunctional SPEF2 in developing spermatids and mature sperm. (liu2019lossoffunctionmutationsin pages 1-2, liu2020homozygousmutationsin pages 3-4)
2. **SPEF2 deficiency leads to** defective interaction/localization with IFT20 and central-pair/radial-spoke partners, including RSPH9; altered CFAP69 and HYDIN-dependent central-apparatus composition is also observed. (liu2020homozygousmutationsin pages 5-6, li2022spermflagellar2 pages 3-4, li2022spermflagellar2 pages 6-7, aprea2023pathogenicgenevariants pages 2-3)
3. **Defective SPEF2-dependent transport and scaffolding lead to** impaired intraflagellar and probably intramanchette cargo delivery during spermiogenesis; the intramanchette contribution is mechanistically supported in models/proteomics but remains partly inferred in humans. (virtanen2016theroleofa pages 44-47, lehti2016microtubulemediatedproteintransport pages 31-34, li2022spermflagellar2 pages 6-7)
4. **Transport/scaffold failure results in** incomplete assembly of the C1b/central-pair apparatus, radial spokes, dynein-associated components, fibrous sheath, outer dense fibres, and mitochondrial sheath. (liu2020homozygousmutationsin pages 4-4, li2022spermflagellar2 pages 4-6, li2022spermflagellar2 pages 3-4)
5. **Axonemal and peri-axonemal disorganization leads to** absent, short, bent, coiled, or irregular sperm flagella and inefficient energy/mechanical coupling. (liu2019lossoffunctionmutationsin pages 1-2, liu2020homozygousmutationsin pages 4-5)
6. **Malformed flagella result in** near-total loss of progressive sperm motility and inability to traverse the female reproductive tract, causing male infertility. (liu2020homozygousmutationsin pages 4-5, liu2020homozygousmutationsin pages 3-4)
7. **Branch—when respiratory motile-cilium function is sufficiently affected, SPEF2 dysfunction leads to** impaired mucociliary clearance and chronic wet cough/sinusitis/nasal congestion; this branch is variably expressed and may occur without obvious TEM abnormalities. (lu2024novelspef2variants pages 1-2)

### Molecular and cellular detail

Normal sperm axonemes contain nine outer doublet microtubules around two central singlets. SPEF2 is associated with the central-pair **C1b projection** and is also detected during spermatid development in the Golgi, manchette, basal body, and forming tail. Human mutant sperm can lose the central pair completely, generating a 9+0 arrangement. (liu2020homozygousmutationsin pages 3-4, lehti2016microtubulemediatedproteintransport pages 31-34, aprea2023pathogenicgenevariants pages 2-3)

Proteomics of sperm from three SPEF2-mutant patients found **1,262 differentially expressed proteins: 486 increased and 776 decreased**. Reduced proteins included central-pair/radial-spoke and dynein-associated components such as SPAG6, RSPH1, RSPH4A, DNALI1, DNAH5, DNAI2, DYNLT1, and MNS1. IFT20, IFT27, IFT54, and IFT144/WDR19 were increased, potentially representing failed cargo assembly or compensatory feedback. SPEF2–IFT20 and SPEF2–RSPH9 interactions were experimentally supported. (li2022spermflagellar2 pages 4-6, li2022spermflagellar2 pages 3-4)

TOM20, AKAP3/AKAP4, oxidative-phosphorylation, glycolytic, and carbon-metabolism proteins were altered. These findings support secondary energetic dysfunction but do not establish a primary metabolic disease. Retained cytoplasm and altered IQUB, UBTD2, ZNRF4, and USP14 suggest disturbed protein degradation; its causal importance is unresolved. (li2022spermflagellar2 pages 4-6, li2022spermflagellar2 pages 6-7)

There is no demonstrated canonical Wnt, MAPK, mTOR, or PI3K–AKT driver, no evidence that inflammation or autoimmunity initiates the disorder, and no disease-specific human metabolomic, lipidomic, epigenomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature beyond sperm proteomics.

**Suggested annotations:** GO biological processes—spermatid development, spermiogenesis, sperm flagellum assembly, cilium movement, microtubule-based movement, intraflagellar transport, protein localization to cilium; GO cellular components—sperm flagellum, axoneme, central-pair apparatus, manchette, basal body, radial spoke, mitochondrial sheath; CL—**spermatid**, **spermatozoon**, **Sertoli cell**, and respiratory **ciliated epithelial cell**. Exact ontology accessions should be resolved against current GO/CL releases.

## 7. Anatomical structures affected

The primary organ is the **testis**, specifically seminiferous epithelium and differentiating haploid spermatids; the clinically assayed cells are ejaculated spermatozoa from the epididymis/seminal tract. External genitalia and testes may appear normal on routine examination despite profound cellular disease. (liu2019lossoffunctionmutationsin pages 1-2)

Primary subcellular sites are the sperm-tail axoneme, central pair/C1b projection, radial spokes, dynein-associated structures, outer dense fibres, fibrous sheath, mitochondrial sheath, basal body, and the transient spermatid manchette. No lateralization applies. Suggested UBERON concepts are testis, seminiferous tubule, epididymis, spermatic part of flagellum, and respiratory epithelium. If PCD-like disease occurs, nasal/sinus and airway ciliated epithelia are secondary sites.

## 8. Temporal development

The molecular lesion is congenital and lifelong, but the reproductive phenotype develops during post-pubertal spermiogenesis and is usually diagnosed in adulthood during infertility evaluation. Onset is insidious rather than acute. There are no validated clinical stages, spontaneous remissions, relapsing pattern, or evidence that malformed sperm improve with age. Each new spermatogenic cycle reproduces the assembly defect.

The critical biological window is elongating-spermatid differentiation, when manchette-dependent trafficking and flagellar assembly occur. For family planning, the actionable window is before ART: establish a molecular diagnosis, assess respiratory features, provide recurrence counseling, and discuss reproductive options.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Affected males generally have biallelic variants; parents are expected to be heterozygous carriers. For two carrier parents, Mendelian risks per pregnancy are 25% biallelic, 50% carrier, and 25% inheriting neither familial allele. A biallelic female may not manifest “spermatogenic failure,” but could theoretically have motile-cilia manifestations; female reproductive consequences are insufficiently characterized.

Consanguinity is prominent in several reports, but compound heterozygous cases demonstrate that disease also occurs in outbred families. Reported subjects include Han Chinese and Iranian individuals and European PCD/infertility cohorts; these observations do not establish ethnic enrichment or a founder effect. (liu2020homozygousmutationsin pages 2-2, lu2024novelspef2variants pages 1-2, aprea2023pathogenicgenevariants pages 2-3)

No prevalence, incidence, carrier-frequency, or sex-ratio estimate exists for SPGF43. Clinically recognized reproductive disease is male-limited by definition. Penetrance for severe sperm dysfunction appears high among published biallelic males, but publication/ascertainment bias precludes a numerical estimate. Respiratory expressivity is variable. Genetic anticipation and confirmed germline mosaicism have not been reported.

## 10. Diagnostics

### Recommended workflow

1. **Clinical infertility assessment:** reproductive/family history, consanguinity, medication/exposure history, physical examination, and at least two semen analyses under current WHO methods.
2. **Sperm phenotyping:** quantify concentration, total/progressive motility, vitality, and detailed tail morphology. MMAF should prompt a genetic cause even when genital anatomy and routine hormones are normal.
3. **Exclude common causes:** karyotype and Y-chromosome microdeletion testing when indicated by severe oligo-/azoospermia; evaluate obstruction, hypogonadism, varicocele, infection, and gonadotoxic exposure.
4. **Molecular testing:** a validated male-infertility/MMAF/PCD panel including **SPEF2**, or WES/WGS with copy-number and splice-aware analysis. Confirm variants and parental phase by Sanger or equivalent testing. WES successfully discovered most reported variants. WGS is useful when WES is negative, particularly for deep-intronic, structural, regulatory, or poorly captured exons.
5. **Functional/pathology support:** sperm immunofluorescence for SPEF2 and interacting structures, and TEM where available. A 2023 study emphasized that sperm immunofluorescence can help classify uncertain missense defects affecting the axonemal ruler, radial-spoke head, and central-pair apparatus. (aprea2023pathogenicgenevariants pages 2-3)
6. **PCD evaluation when symptomatic:** nasal nitric oxide where age/standards permit, high-speed video microscopy, respiratory-cilium IF/TEM, and a comprehensive PCD gene panel. Normal TEM does not exclude PCD or SPEF2-related functional disease.

RNA sequencing of patient cells may demonstrate splice consequences, but is not yet a standardized diagnostic. Proteomics is mechanistically informative rather than routine. CMA, FISH, mitochondrial sequencing, and repeat-expansion testing are not targeted tests for SPGF43 unless another diagnosis is suspected.

**Differential diagnosis.** Other MMAF genes include **DNAH1, CFAP43, CFAP44, CFAP65, CFAP69, FSIP2, ARMC2, CFAP61, TTC29, DNHD1, HYDIN, RSPH1, RSPH9, CCDC39, and CCDC40**. Broader differentials include primary mitochondrial sperm-motility disorders, globozoospermia, macrozoospermia, acephalic spermatozoa syndrome, Kartagener/other PCD, endocrine infertility, obstruction, varicocele, infection, and acquired toxic/thermal damage. Central-pair loss and absent/reduced SPEF2 staining support—but alone do not absolutely prove—SPEF2 causation.

There are no universally accepted SPGF43-specific clinical criteria, newborn screening, or population screening programs. Cascade testing is appropriate after a familial genotype is established.

## 11. Outcome and prognosis

SPGF43 is not known to shorten human life expectancy. Disease-specific mortality and survival statistics are not applicable/available. The major morbidity is persistent infertility; respiratory morbidity may occur in PCD-like cases. Natural conception is expected to be markedly impaired when progressive motility is 0%, but absolute natural-conception probabilities have not been estimated.

ICSI can bypass the requirement for sperm propulsion. In 2019, one couple produced two blastocysts but did not achieve pregnancy after one transfer; maternal age was considered a possible contributor. (liu2019lossoffunctionmutationsin pages 6-6) In the 2024 three-family series, reported ICSI fertilization rates were 100%, 90%, and 82%, and all three couples had healthy live births. These results are encouraging but are only three cycles and must not be interpreted as a general response rate. (lu2024novelspef2variants pages 12-13, lu2024novelspef2variants pages 1-2)

A broader 2024 MMAF cohort—not SPEF2-specific—found reduced embryo-development measures and lower cumulative pregnancy rates relative to controls, while neonatal outcomes did not differ. This reinforces the need for gene- and couple-specific counseling rather than assuming uniformly normal ART outcomes.

## 12. Treatment and current applications

There is no therapy that restores SPEF2 protein or repairs sperm-tail assembly. Antioxidants, hormones, antibiotics, or motility stimulants have no demonstrated SPEF2-specific efficacy unless treating an independent condition.

**Current reproductive strategy:**

* Genetic counseling and confirmatory testing.
* **ICSI** using viable ejaculated sperm when available; suggested NCIt intervention concepts: *Intracytoplasmic Sperm Injection*, *Assisted Reproductive Technology*, and *Genetic Counseling*.
* Surgical sperm retrieval may be considered if adequate ejaculated sperm are unavailable, but SPGF43-specific outcome evidence is lacking.
* Standard embryo culture/transfer and obstetric follow-up.
* Discussion of donor sperm, adoption, or remaining child-free.
* Preimplantation genetic testing for monogenic disease (**PGT-M**) or prenatal diagnosis when the familial variants are known, based on informed preferences and local regulation.

If PCD is diagnosed, use established PCD supportive care—airway-clearance techniques, prompt culture-guided treatment of respiratory exacerbations, vaccination, and specialist surveillance—not a SPEF2-targeted drug.

Gene replacement/editing, mRNA, ASO, and germ-cell therapies remain preclinical concepts. The 2021 proteomics paper stated that its findings “could provide a theoretical basis for gene therapy … in the future,” not that such therapy currently exists. (li2022spermflagellar2 pages 4-6, li2022spermflagellar2 pages 3-4) No relevant SPEF2/SPGF43 interventional clinical trial or NCT identifier was identified.

## 13. Prevention

The genotype cannot be prevented by behavioral modification or immunization. Primary genetic prevention options are voluntary carrier/cascade testing, reproductive counseling, PGT-M, donor gametes, and prenatal diagnosis. There is no newborn screening indication. Secondary prevention consists of early recognition of severe MMAF and timely molecular/PCD assessment, reducing diagnostic delay and avoiding ineffective empiric treatment. Tertiary prevention includes ART for infertility and PCD respiratory care where applicable. Population-wide carrier screening is not currently justified because prevalence and carrier frequency are unknown.

## 14. Other species and natural disease

**Mouse—Mus musculus (NCBI Taxon 10090):** spontaneous/global Spef2 mutants develop male infertility, defective sperm-tail formation, sinusitis, reduced ciliary beat, severe hydrocephalus, and early mortality. Tracheal cilia can look structurally normal while beating about 17% more slowly. Germ-cell conditional knockout avoids some systemic confounding and produces abnormal manchettes and basal bodies, club-shaped heads, truncated/stump tails, impaired spermiation, and very few epididymal sperm; acrosome formation remains comparatively normal. (virtanen2016theroleofa pages 44-47, lehti2016microtubulemediatedproteintransport pages 31-34, virtanen2016theroleof pages 44-47)

**Pig—Sus scrofa (NCBI Taxon 9823):** the naturally occurring immotile short-tail sperm defect is caused by a LINE-1/intronic SPEF2/KPL2 insertion producing aberrant splicing, premature termination, loss of protein, reduced sperm count, and short immotile tails. EM shows missing central microtubules or reduced outer doublets. (liu2020homozygousmutationsin pages 4-4, lehti2016microtubulemediatedproteintransport pages 31-34)

**Cattle—Bos taurus (NCBI Taxon 9913):** a natural SPEF2 splice-disrupting variant in Holstein cattle has been associated with malformed sperm and reduced post-cryopreservation motility. (liu2020homozygousmutationsin pages 4-4)

These are hereditary, noninfectious traits with no zoonotic or cross-species transmission. Their value is comparative: conserved central-pair and transport functions strongly support human variant causality, although severe murine hydrocephalus does not reliably predict the human phenotype.

## 15. Model organisms and experimental systems

* **Global and spontaneous Spef2-mutant mice:** useful for motile-cilium/PCD biology, hydrocephalus, airway clearance, and infertility; limited by early lethality and a systemic phenotype more severe than most reported humans.
* **Male-germ-cell conditional Spef2 knockout mice:** best suited to spermiogenesis, manchette, basal-body, spermiation, and sperm-tail assembly without lethal hydrocephalus; they reproduce infertility and severe flagellar defects but not human allelic heterogeneity. (virtanen2016theroleofa pages 44-47, virtanen2016theroleof pages 44-47)
* **Pig and bull natural mutants:** valuable large-animal models of sperm-tail defects and agricultural fertility, including semen cryopreservation; breed structure and species-specific transcripts limit direct penetrance estimates for humans. (liu2020homozygousmutationsin pages 4-4, lehti2016microtubulemediatedproteintransport pages 31-34)
* **Human sperm and HEK293T interaction assays:** patient sperm supports disease-relevant IF/TEM/proteomics; heterologous co-immunoprecipitation demonstrated SPEF2–RSPH9 interaction but cannot reproduce spermatid architecture. (li2022spermflagellar2 pages 3-4, li2022spermflagellar2 pages 6-7)
* **Chlamydomonas reinhardtii:** a 2024 preprint used a SPEF2-homolog motility mutant to model SPGF43 and explore rescue. This is a tractable conserved-axoneme platform, not evidence of a human treatment.

## Recent developments and expert interpretation

The 2023 Aprea study moved sperm immunofluorescence toward a clinically useful functional assay for uncertain variants and localized SPEF2 within central-pair disease biology. (aprea2023pathogenicgenevariants pages 2-3) The 2024 Lu study expanded the allelic spectrum by four variants, strengthened evidence that SPEF2 disease can bridge MMAF and PCD, and provided three successful ICSI live births. (lu2024novelspef2variants pages 1-2, lu2024novelspef2variants pages 12-13) Current expert interpretation should therefore avoid classifying SPEF2 solely as an isolated-infertility gene: respiratory history and PCD testing are warranted when symptoms are present. Conversely, murine hydrocephalus should not be assigned as a routine human phenotype without human evidence.

The most important limitations are tiny cohorts, infertility/PCD ascertainment bias, inconsistent transcript nomenclature, incomplete ClinVar-level classification, and sparse longitudinal follow-up. Consequently, statements such as complete penetrance, population prevalence, variant-specific respiratory risk, and an ICSI success percentage are presently unsupported.

## Key primary sources and dates

1. Liu W et al. **“Loss-of-function mutations in SPEF2 cause multiple morphological abnormalities of the sperm flagella (MMAF).”** *Journal of Medical Genetics* 56:678–684; published May 2019. DOI/URL: https://doi.org/10.1136/jmedgenet-2018-105952. (liu2019lossoffunctionmutationsin pages 1-2)
2. Liu C et al. **“Homozygous mutations in SPEF2 induce multiple morphological abnormalities of the sperm flagella and male infertility.”** *Journal of Medical Genetics* 57:31–37; 2020. DOI/URL: https://doi.org/10.1136/jmedgenet-2019-106011. Abstract conclusion: “We identified SPEF2 as a novel gene for human MMAF across the populations.” (liu2020homozygousmutationsin pages 2-2, liu2020homozygousmutationsin pages 3-4)
3. Li D-Y et al. **“Sperm flagellar 2 (SPEF2) is essential for sperm flagellar assembly in humans.”** *Asian Journal of Andrology* 24:359–366; online November 2021. DOI/URL: https://doi.org/10.4103/aja202154. Abstract: “A total of 1262 differentially expressed proteins were detected, including 486 upregulated and 776 downregulated.” (li2022spermflagellar2 pages 4-6, li2022spermflagellar2 pages 3-4)
4. Aprea I et al. **“Pathogenic gene variants in CCDC39, CCDC40, RSPH1, RSPH9, HYDIN, and SPEF2 cause defects of sperm flagella composition and male infertility.”** *Frontiers in Genetics* 14; published 3 February 2023. DOI/URL: https://doi.org/10.3389/fgene.2023.1117821. (aprea2023pathogenicgenevariants pages 2-3)
5. Lu W et al. **“Novel SPEF2 variants cause male infertility and likely primary ciliary dyskinesia.”** *Journal of Assisted Reproduction and Genetics* 41:1485–1498; online 3 April 2024. DOI/URL: https://doi.org/10.1007/s10815-024-03106-9. (lu2024novelspef2variants pages 1-2)

PMIDs were not exposed in the retrieved full-text metadata and therefore are not guessed here; they should be programmatically resolved from the DOIs through PubMed/Crossref before knowledge-base loading.

References

1. (liu2019lossoffunctionmutationsin pages 1-2): Wensheng Liu, Yanwei Sha, Yang Li, Libin Mei, Shaobin Lin, Xianjing Huang, Jinhua Lu, Lu Ding, Shuangbo Kong, and Zhongxian Lu. Loss-of-function mutations in spef2 cause multiple morphological abnormalities of the sperm flagella (mmaf). Journal of Medical Genetics, 56:678-684, May 2019. URL: https://doi.org/10.1136/jmedgenet-2018-105952, doi:10.1136/jmedgenet-2018-105952. This article has 83 citations and is from a domain leading peer-reviewed journal.

2. (liu2020homozygousmutationsin pages 2-2): Chunyu Liu, Mingrong Lv, Xiaojin He, Yong Zhu, Amir Amiri-Yekta, Weiyu Li, Huan Wu, Zine-Eddine Kherraf, Wangjie Liu, Jingjing Zhang, Qing Tan, Shuyan Tang, Yong-Jun Zhu, Yading Zhong, Caihua Li, Shixiong Tian, Zhiguo Zhang, Li Jin, Pierre Ray, Feng Zhang, and Yunxia Cao. Homozygous mutations in spef2 induce multiple morphological abnormalities of the sperm flagella and male infertility. Journal of Medical Genetics, 57:31-37, May 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106011, doi:10.1136/jmedgenet-2019-106011. This article has 95 citations and is from a domain leading peer-reviewed journal.

3. (liu2020homozygousmutationsin pages 3-4): Chunyu Liu, Mingrong Lv, Xiaojin He, Yong Zhu, Amir Amiri-Yekta, Weiyu Li, Huan Wu, Zine-Eddine Kherraf, Wangjie Liu, Jingjing Zhang, Qing Tan, Shuyan Tang, Yong-Jun Zhu, Yading Zhong, Caihua Li, Shixiong Tian, Zhiguo Zhang, Li Jin, Pierre Ray, Feng Zhang, and Yunxia Cao. Homozygous mutations in spef2 induce multiple morphological abnormalities of the sperm flagella and male infertility. Journal of Medical Genetics, 57:31-37, May 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106011, doi:10.1136/jmedgenet-2019-106011. This article has 95 citations and is from a domain leading peer-reviewed journal.

4. (liu2020homozygousmutationsin pages 4-5): Chunyu Liu, Mingrong Lv, Xiaojin He, Yong Zhu, Amir Amiri-Yekta, Weiyu Li, Huan Wu, Zine-Eddine Kherraf, Wangjie Liu, Jingjing Zhang, Qing Tan, Shuyan Tang, Yong-Jun Zhu, Yading Zhong, Caihua Li, Shixiong Tian, Zhiguo Zhang, Li Jin, Pierre Ray, Feng Zhang, and Yunxia Cao. Homozygous mutations in spef2 induce multiple morphological abnormalities of the sperm flagella and male infertility. Journal of Medical Genetics, 57:31-37, May 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106011, doi:10.1136/jmedgenet-2019-106011. This article has 95 citations and is from a domain leading peer-reviewed journal.

5. (li2022spermflagellar2 pages 4-6): Dong-Yan Li, Xiao-Xuan Yang, Chao-Feng Tu, Wei-Li Wang, Lan-Lan Meng, Guang-Xiu Lu, Yue-Qiu Tan, Qian-Jun Zhang, and Juan Du. Sperm flagellar 2 (spef2) is essential for sperm flagellar assembly in humans. Asian Journal of Andrology, 24:359-366, Nov 2021. URL: https://doi.org/10.4103/aja202154, doi:10.4103/aja202154. This article has 34 citations and is from a peer-reviewed journal.

6. (liu2020homozygousmutationsin pages 5-6): Chunyu Liu, Mingrong Lv, Xiaojin He, Yong Zhu, Amir Amiri-Yekta, Weiyu Li, Huan Wu, Zine-Eddine Kherraf, Wangjie Liu, Jingjing Zhang, Qing Tan, Shuyan Tang, Yong-Jun Zhu, Yading Zhong, Caihua Li, Shixiong Tian, Zhiguo Zhang, Li Jin, Pierre Ray, Feng Zhang, and Yunxia Cao. Homozygous mutations in spef2 induce multiple morphological abnormalities of the sperm flagella and male infertility. Journal of Medical Genetics, 57:31-37, May 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106011, doi:10.1136/jmedgenet-2019-106011. This article has 95 citations and is from a domain leading peer-reviewed journal.

7. (lu2024novelspef2variants pages 1-2): Wenqing Lu, Yong Li, Lanlan Meng, Chen Tan, Hongchuan Nie, Qianjun Zhang, Yuying Song, Huan Zhang, Yue-Qiu Tan, Chaofeng Tu, Haichun Guo, Longxiang Wu, and Juan Du. Novel spef2 variants cause male infertility and likely primary ciliary dyskinesia. Journal of assisted reproduction and genetics, 41:1485-1498, Apr 2024. URL: https://doi.org/10.1007/s10815-024-03106-9, doi:10.1007/s10815-024-03106-9. This article has 5 citations and is from a peer-reviewed journal.

8. (liu2019lossoffunctionmutationsin pages 6-6): Wensheng Liu, Yanwei Sha, Yang Li, Libin Mei, Shaobin Lin, Xianjing Huang, Jinhua Lu, Lu Ding, Shuangbo Kong, and Zhongxian Lu. Loss-of-function mutations in spef2 cause multiple morphological abnormalities of the sperm flagella (mmaf). Journal of Medical Genetics, 56:678-684, May 2019. URL: https://doi.org/10.1136/jmedgenet-2018-105952, doi:10.1136/jmedgenet-2018-105952. This article has 83 citations and is from a domain leading peer-reviewed journal.

9. (li2022spermflagellar2 pages 3-4): Dong-Yan Li, Xiao-Xuan Yang, Chao-Feng Tu, Wei-Li Wang, Lan-Lan Meng, Guang-Xiu Lu, Yue-Qiu Tan, Qian-Jun Zhang, and Juan Du. Sperm flagellar 2 (spef2) is essential for sperm flagellar assembly in humans. Asian Journal of Andrology, 24:359-366, Nov 2021. URL: https://doi.org/10.4103/aja202154, doi:10.4103/aja202154. This article has 34 citations and is from a peer-reviewed journal.

10. (li2022spermflagellar2 pages 6-7): Dong-Yan Li, Xiao-Xuan Yang, Chao-Feng Tu, Wei-Li Wang, Lan-Lan Meng, Guang-Xiu Lu, Yue-Qiu Tan, Qian-Jun Zhang, and Juan Du. Sperm flagellar 2 (spef2) is essential for sperm flagellar assembly in humans. Asian Journal of Andrology, 24:359-366, Nov 2021. URL: https://doi.org/10.4103/aja202154, doi:10.4103/aja202154. This article has 34 citations and is from a peer-reviewed journal.

11. (aprea2023pathogenicgenevariants pages 2-3): I. Aprea, A. Wilken, C. Krallmann, T. Nöthe-Menchen, H. Olbrich, N. T. Loges, G. W. Dougherty, D. Bracht, C. Brenker, S. Kliesch, T. Strünker, F. Tüttelmann, J. Raidt, and H. Omran. Pathogenic gene variants in ccdc39, ccdc40, rsph1, rsph9, hydin, and spef2 cause defects of sperm flagella composition and male infertility. Frontiers in Genetics, Feb 2023. URL: https://doi.org/10.3389/fgene.2023.1117821, doi:10.3389/fgene.2023.1117821. This article has 38 citations and is from a peer-reviewed journal.

12. (lu2024novelspef2variants pages 12-13): Wenqing Lu, Yong Li, Lanlan Meng, Chen Tan, Hongchuan Nie, Qianjun Zhang, Yuying Song, Huan Zhang, Yue-Qiu Tan, Chaofeng Tu, Haichun Guo, Longxiang Wu, and Juan Du. Novel spef2 variants cause male infertility and likely primary ciliary dyskinesia. Journal of assisted reproduction and genetics, 41:1485-1498, Apr 2024. URL: https://doi.org/10.1007/s10815-024-03106-9, doi:10.1007/s10815-024-03106-9. This article has 5 citations and is from a peer-reviewed journal.

13. (virtanen2016theroleofa pages 44-47): S Virtanen. The role of spef2 in spermatogenesis. Unknown journal, 2016.

14. (lehti2016microtubulemediatedproteintransport pages 31-34): M Lehti. Microtubule-mediated protein transport mechanisms during spermiogenesis. Unknown journal, 2016.

15. (liu2020homozygousmutationsin pages 4-4): Chunyu Liu, Mingrong Lv, Xiaojin He, Yong Zhu, Amir Amiri-Yekta, Weiyu Li, Huan Wu, Zine-Eddine Kherraf, Wangjie Liu, Jingjing Zhang, Qing Tan, Shuyan Tang, Yong-Jun Zhu, Yading Zhong, Caihua Li, Shixiong Tian, Zhiguo Zhang, Li Jin, Pierre Ray, Feng Zhang, and Yunxia Cao. Homozygous mutations in spef2 induce multiple morphological abnormalities of the sperm flagella and male infertility. Journal of Medical Genetics, 57:31-37, May 2020. URL: https://doi.org/10.1136/jmedgenet-2019-106011, doi:10.1136/jmedgenet-2019-106011. This article has 95 citations and is from a domain leading peer-reviewed journal.

16. (virtanen2016theroleof pages 44-47): S Virtanen. The role of spef2 in spermatogenesis. Unknown journal, 2016.

## Artifacts

- [Edison artifact artifact-00](Spermatogenic_Failure_43-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032898` (2 mentions) - the report calls it "if available"; MONDO calls it **spermatogenic failure 43**