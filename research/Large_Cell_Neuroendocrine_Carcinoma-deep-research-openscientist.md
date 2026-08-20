---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-20T03:58:33.556003'
end_time: '2026-08-20T04:15:54.844572'
duration_seconds: 1041.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Large Cell Neuroendocrine Carcinoma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 49
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 7
  relevance_assessed: 49
  on_topic: 37
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Large_Cell_Neuroendocrine_Carcinoma-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Large_Cell_Neuroendocrine_Carcinoma-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Large Cell Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Large Cell Neuroendocrine Carcinoma** covering all of the
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

# Large Cell Neuroendocrine Carcinoma (LCNEC): A Comprehensive Disease Characteristics Report

**Category:** Neoplastic | **Primary MONDO ID:** MONDO:0005057 (site-agnostic) / MONDO:0003960 (pulmonary) | **ICD-O:** 8013/3 | **NCIT:** C4118

---

## Summary

Large cell neuroendocrine carcinoma (LCNEC) is a rare, high-grade, poorly differentiated neuroendocrine carcinoma that accounts for approximately 0.3–3% of all lung cancers and also arises at extrapulmonary sites (thymus/mediastinum, gastrointestinal tract, uterus/cervix, breast, gallbladder, ovary). It is a tobacco-driven somatic malignancy of predominantly elderly male smokers. Diagnosis rests on non-small-cell neuroendocrine morphology — large cells, high mitotic rate (>10 mitoses/2 mm², typically ~70–75 mean), extensive necrosis, and organoid/palisading architecture — combined with **mandatory immunohistochemical confirmation** of neuroendocrine differentiation (chromogranin A, synaptophysin, CD56, with INSM1 and Ki-67 as adjuncts). Central pathology review reveals substantial interobserver variability, with LCNEC confirmed in only ~67% of submitted cases in one national registry, underscoring that this remains a diagnostically challenging entity.

Molecularly, LCNEC occupies a biological space that bridges small cell lung cancer (SCLC) and non-small cell lung cancer (NSCLC). Near-universal *TP53* alteration coexists with two dominant genomic subtypes: an **SCLC-like** subtype (*RB1* + *TP53* co-alteration) and an **NSCLC-like** subtype (*KEAP1*, *KRAS*, *STK11*, *SMARCA4*, *CDKN2A/B*). A third **carcinoid-like** group (*MEN1* mutation without *TP53*) is recognized in large comprehensive genomic profiling cohorts. Orthogonal transcription-factor and YAP1-based classifications further subdivide the disease into therapeutically distinct subsets (ASCL1/NEUROD1-driven, DLL3-high, immune-cold vs. YAP1-high, mesenchymal, inflamed). Tumor mutational burden is high (~12.7 mut/Mb), and homologous-recombination pathway defects, NOTCH-pathway alterations, and epigenetic dysregulation (DNMT1/DNMT3A upregulation, promoter hypermethylation, ASCL1 super-enhancers) contribute to pathogenesis. LCNEC can also arise via neuroendocrine transformation of *EGFR*-mutant lung adenocarcinoma as an acquired resistance mechanism, driven by MYC amplification atop shared clonal *TP53*/*STK11* mutations.

Prognosis is poor overall — stage IV median overall survival (OS) is approximately 7.4 months — although early-stage resected disease reaches 53–86% 5-year survival. Treatment is largely extrapolated from SCLC and NSCLC: platinum-etoposide chemotherapy remains the first-line backbone, chemoimmunotherapy improves outcomes in advanced disease (pooled ORR 49%, first-line OS HR 0.72), surgery is central to localized disease, and DLL3-directed bispecific T-cell engager therapy (tarlatamab) is an emerging targeted option supported by early clinical activity in LCNEC and DLL3-high pulmonary carcinoid.

---

## 1. Disease Information

**Overview.** LCNEC is a poorly differentiated, high-grade neuroendocrine carcinoma composed of large cells with neuroendocrine morphology (organoid nesting, palisading, rosette-like structures, trabeculae) and confirmed neuroendocrine differentiation. In the WHO framework, lung neuroendocrine neoplasms are divided into well-differentiated typical/atypical carcinoids and poorly differentiated high-grade carcinomas comprising LCNEC and SCLC ([PMID: 39756451](https://pubmed.ncbi.nlm.nih.gov/39756451/); [PMID: 28871510](https://pubmed.ncbi.nlm.nih.gov/28871510/)).

**Key identifiers.**

| Resource | Identifier |
|----------|-----------|
| MONDO (site-agnostic) | MONDO:0005057 — large cell neuroendocrine carcinoma |
| MONDO (pulmonary) | MONDO:0003960 — pulmonary large cell neuroendocrine carcinoma |
| MONDO (lung combined LCNEC) | MONDO:0004142 |
| MONDO (parent NEC) | MONDO:0002120 — neuroendocrine carcinoma |
| MONDO (lung NE neoplasm) | MONDO:0005454 |
| MONDO (thymic) | MONDO:0003047 |
| MONDO (ovarian) | MONDO:0003049 |
| MONDO (breast) | MONDO:0003959 |
| MONDO (pancreatic) | MONDO:0006347 |
| MONDO (cervical) | MONDO:0006138 |
| ICD-O morphology | 8013/3 |
| NCIT | C4118 (Lung Large Cell Neuroendocrine Carcinoma) |
| MeSH | D018278 (Carcinoma, Neuroendocrine) |
| OMIM | None — somatic malignancy, no Mendelian entry |

These identifiers were verified via EBI OLS4 MONDO lookup (2026-08) and are documented in **F014/F015** ([PMID: 42526975](https://pubmed.ncbi.nlm.nih.gov/42526975/); [PMID: 39756451](https://pubmed.ncbi.nlm.nih.gov/39756451/)).

**Synonyms / alternative names.** Pulmonary large cell neuroendocrine carcinoma (PLCNEC); large-cell neuroendocrine carcinoma of the lung; high-grade neuroendocrine carcinoma, large cell type; combined LCNEC (when admixed with adenocarcinoma, squamous cell carcinoma, or other NSCLC components).

**Source of information.** Content is derived from aggregated disease-level resources — WHO Classification of Tumours, national registries (SEER, Netherlands Cancer Registry, French EPITHOR), comprehensive genomic profiling cohorts, and the primary literature — rather than individual EHR records.

---

## 2. Etiology

**Causal factors.** LCNEC is a **somatic, tobacco-driven malignancy**. There is no Mendelian/germline cause; disease arises through accumulation of somatic mutations, near-universally including *TP53* alteration, in the setting of heavy tobacco exposure ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/); **F002**, **F006**).

**Environmental / lifestyle risk factors.**
- **Tobacco smoking** is the dominant risk factor: "Most of the LCNEC patients are elderly smoking male" ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/)). Tobacco consumption is independently associated with OS in resected disease ([PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/)).
- **Age and male sex** — patients are typically elderly (mean age at surgery ~63.8 years) and male (~68.8%) ([PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/)).
- **Cannabis smoking** — associated with earlier age at lung cancer diagnosis and a higher relative frequency of LCNEC and adenocarcinoma histology among cannabis vs. tobacco-only smokers, though not an independent prognostic factor ([PMID: 40393352](https://pubmed.ncbi.nlm.nih.gov/40393352/)).

**Genetic risk factors.** No established germline susceptibility loci. The relevant genetic events are somatic drivers (see Section 4). Homologous-recombination pathway alterations are present in a subset and are prognostically relevant ([PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/)).

**Protective factors.** No validated genetic or environmental protective factors are established for LCNEC specifically. By analogy to lung cancer generally, smoking cessation is the principal modifiable protective behavior.

**Gene–environment interactions.** Tobacco carcinogen exposure drives the high mutational burden (TMB ~12.7 mut/Mb) and the *TP53*/*RB1* and NSCLC-driver mutation spectrum that defines LCNEC subtypes ([PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/); [PMID: 40830141](https://pubmed.ncbi.nlm.nih.gov/40830141/)).

---

## 3. Phenotypes

Clinical manifestations are non-specific. LCNEC is often peripheral and in the upper lobes ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/)).

| Phenotype | Type | HPO suggestion | Characteristics |
|-----------|------|----------------|-----------------|
| Cough | Symptom | HP:0012735 | Adult/geriatric onset; non-specific |
| Dyspnea | Symptom | HP:0002094 | Progressive with tumor burden |
| Hemoptysis | Sign | HP:0002105 | Variable |
| Chest pain | Symptom | HP:0100749 | Variable |
| Weight loss / cachexia | Constitutional | HP:0001824 | Advanced disease |
| Pulmonary neoplasm | Physical | HP:0100526 | Frequently peripheral, upper lobe |
| Bone metastasis | Complication | HP:0000766 (abnormal bone) | ~23% synchronous at diagnosis in high-grade lung NEC ([PMID: 40634407](https://pubmed.ncbi.nlm.nih.gov/40634407/)) |
| Brain metastasis | Complication | HP:0002060 (CNS neoplasm) | Independent adverse prognostic factor ([PMID: 39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/)) |
| Liver metastasis | Complication | HP:0006554 | Independent adverse prognostic factor ([PMID: 39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/)) |

**Onset / severity / progression.** Adult-to-geriatric onset; severe and rapidly progressive. "The clinical manifestations are not specific," which contributes to late-stage presentation ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/)). Nearly half of patients present at advanced stage ([PMID: 39287289](https://pubmed.ncbi.nlm.nih.gov/39287289/)). Unlike well-differentiated carcinoids, functional hormonal (carcinoid) syndromes are uncommon.

**Quality-of-life impact.** Direct EQ-5D/SF-36 LCNEC data were not identified; by extrapolation from high-grade lung cancer, symptom burden (dyspnea, pain from metastases, fatigue) and treatment toxicity substantially impair daily functioning. This is a knowledge gap.

---

## 4. Genetic / Molecular Information

**Causal / driver genes and subtypes (F001, F004, F006).** LCNEC has two dominant genomic subtypes plus a carcinoid-like minority:

| Subtype | Defining alterations | Frequency / evidence |
|---------|---------------------|----------------------|
| **SCLC-like** | *RB1* + *TP53* co-alteration | n=557 in CGP cohort ([PMID: 38159439](https://pubmed.ncbi.nlm.nih.gov/38159439/)); ~80% align with SCLC transcriptional profile ([PMID: 40830141](https://pubmed.ncbi.nlm.nih.gov/40830141/)) |
| **NSCLC-like** | *KEAP1*, *KRAS*, *STK11*, *SMARCA4*, *CDKN2A/B*, *MTAP*, *CCND1*, *FGF3/4/19* | ([PMID: 40830141](https://pubmed.ncbi.nlm.nih.gov/40830141/); [PMID: 38159439](https://pubmed.ncbi.nlm.nih.gov/38159439/)) |
| **Carcinoid-like** | *MEN1* mutation without *TP53* GA | n=25 ([PMID: 38159439](https://pubmed.ncbi.nlm.nih.gov/38159439/)) |

> "Genomic analysis identifies distinct non-small cell lung cancer-like (NSCLC-like, KEAP1, KRAS, STK11 mutations) and SCLC-like (RB1, TP53 mutations) LCNEC subtypes, with 80% aligning with SCLC transcriptional profiles." ([PMID: 40830141](https://pubmed.ncbi.nlm.nih.gov/40830141/))

**Additional recurrently altered genes.** *NOTCH1*, *NOTCH2*, *PRKDC*, *SPTA1*, *PTPRD* are mutated at higher rates in LCNEC/SCLC than in carcinoids ([PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/)). 26.3% of LCNECs harbor classical NSCLC driver-gene alterations. The NSCLC-like program also involves PI3K/AKT and RAS/MAPK genes (*PIK3CA*, *KRAS*, *STK11*, *KEAP1*).

**Variant classification, type, and origin.** Alterations are **somatic** (not germline). Types include truncating/nonsense and missense mutations (*TP53*, *STK11*), loss-of-function deletions (*RB1*, *CDKN2A/B*, *SMARCA4*), and copy-number events (MYC amplification during transformation; *FGF3/4/19*, *CCND1* amplification). *TP53* and *RB1* loss are loss-of-function tumor-suppressor events; *KRAS* is gain-of-function. Somatic origin is confirmed by COSMIC/TCGA-type profiling; there are no ClinVar germline pathogenic entries defining this disease.

**Tumor mutational burden.** High: "Large cell neuroendocrine carcinoma (12.7 mutations/Mb) and SCLC (11.9 mutations/Mb) showed higher tumor mutational burdens than TC (2.4 mutations/Mb) and AC (7.1 mutations/Mb)" ([PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/)).

**Transcription-factor / YAP1 axes (F004).** YAP1 status defines two intrinsic subtypes ([PMID: 39150543](https://pubmed.ncbi.nlm.nih.gov/39150543/)):
- **YAP1-high:** mesenchymal, inflamed; co-alterations in *CDKN2A/B* and *SMARCA4* alongside *TP53*; vulnerable to MEK- and AXL-targeting.
- **YAP1-low:** epithelial, immune-cold; *TP53*+*RB1* co-mutation; expresses SCLC transcription factors ASCL1 and NEUROD1; DLL3/CD56 targeting vulnerability.

**Modifier genes.** Homologous-recombination pathway alterations act as therapeutic-response modifiers, predicting longer PFS on systemic therapy (P=.005) ([PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/)).

**Epigenetic information (F011).** First study of DNMT expression in LCNEC (18 cases) found "upregulation of both DNMT1 and DNMT3A compared to control normal lung tissue" ([PMID: 41854102](https://pubmed.ncbi.nlm.nih.gov/41854102/)). Promoter hypermethylation of tumor suppressors (e.g., *RASSF1*, *CDKN2A*, *APC*, *BRCA1*, *CDH1*, *MGMT*, *RARβ*, *RUNX3*, *TIMP3*) links LCNEC to both NSCLC and SCLC — "LCNEC may serve as a biological bridge between non-small cell and small-cell lung carcinoma" ([PMID: 39832203](https://pubmed.ncbi.nlm.nih.gov/39832203/)). ASCL1 acts as a master transcriptional regulator associated with super-enhancers ([PMID: 30121393](https://pubmed.ncbi.nlm.nih.gov/30121393/)).

**Chromosomal abnormalities.** Chromosomal instability, MYC amplification (especially during neuroendocrine transformation), and copy-number alterations at *FGF*/*CCND1* loci. MSI occurs in ~10% of gastric/colorectal NEC but is uncommon in pulmonary LCNEC.

---

## 5. Environmental Information

- **Environmental factors:** Tobacco smoke carcinogens are the principal environmental driver; ionizing radiation and other inhaled carcinogens are plausible by analogy to high-grade lung cancers.
- **Lifestyle factors:** Cigarette smoking (dominant) and cannabis smoking (associated with earlier onset and higher relative LCNEC frequency; [PMID: 40393352](https://pubmed.ncbi.nlm.nih.gov/40393352/)).
- **Infectious agents:** Not applicable for **pulmonary** LCNEC. However, HPV (particularly **HPV18**) is causally associated with **cervical** large cell neuroendocrine carcinoma ([PMID: 42521492](https://pubmed.ncbi.nlm.nih.gov/42521492/); [PMID: 42351440](https://pubmed.ncbi.nlm.nih.gov/42351440/)). Merkel cell polyomavirus causes cutaneous Merkel cell carcinoma, a related high-grade NEC used as a comparator in the literature.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream).**

```
Tobacco carcinogen exposure
        │  (high mutational load, TMB ~12.7/Mb)
        ▼
TP53 loss  ──►  genomic instability / checkpoint failure
        │
   ┌────┴─────────────────────────┐
   ▼                              ▼
RB1 loss (SCLC-like)        KEAP1/KRAS/STK11/SMARCA4 (NSCLC-like)
   │  NOTCH low, ASCL1/NEUROD1     │  RAS/MAPK, PI3K/AKT, KEAP1-NRF2
   │  DLL3 high, immune-cold       │  YAP1-high, mesenchymal, inflamed
   ▼                              ▼
Neuroendocrine differentiation   Epithelial/mesenchymal program
   │                              │
   └──────────┬───────────────────┘
              ▼
   High-grade proliferation (Ki-67 high, >10 mitoses/2mm²),
   necrosis, spread-through-air-spaces (STAS 71–88%)
              ▼
   Early nodal/distant metastasis (bone ~23%, brain, liver) → poor survival
```

**Molecular pathways.** RAS/MAPK, PI3K/AKT/mTOR, NOTCH signaling, KEAP1–NRF2 (via *KEAP1* mutation), Hippo/YAP1, and cell-cycle control (RB1–cyclin D1/CDKN2A) ([PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/); [PMID: 39150543](https://pubmed.ncbi.nlm.nih.gov/39150543/); [PMID: 40830141](https://pubmed.ncbi.nlm.nih.gov/40830141/)). Suggested GO terms: GO:0007219 (Notch signaling pathway), GO:0007265 (Ras protein signal transduction), GO:0035329 (Hippo signaling), GO:0007049 (cell cycle).

**Cellular processes.** Cell-cycle dysregulation (RB1/CDKN2A loss), impaired apoptosis (TP53 loss), neuroendocrine lineage plasticity, and chromosomal instability. Suggested GO terms: GO:0006915 (apoptotic process), GO:0051301 (cell division), GO:0030154 (cell differentiation).

**Protein dysfunction.** Loss-of-function of p53 and RB1 tumor suppressors; SMARCA4 (BRG1) inactivation destabilizes the SWI/SNF chromatin-remodeling complex; gain-of-function KRAS. UniProt: TP53 (P04637), RB1 (P06400), SMARCA4 (P51532), KRAS (P01116), ASCL1 (P50553), DLL3 (Q9NYJ7).

**Metabolic changes.** L-type amino-acid transporter 1 (LAT1/SLC7A5) is overexpressed in 52.4% of LCNEC and correlates with Ki-67, nodal metastasis, and poor outcome ([PMID: 18440724](https://pubmed.ncbi.nlm.nih.gov/18440724/)) — reflecting elevated amino-acid demand of proliferating tumor cells.

**Immune involvement (F010).** Modestly immunogenic relative to SCLC. PD-L1 on tumor cells ~15.1%; immune-cell infiltration and PD-L1-on-immune-cells more strongly correlate with LCNEC than SCLC (57.6% vs 23.3%; 45.8% vs 22.5%; both p<0.01), correlating with high nonsynonymous mutation burden ([PMID: 29378266](https://pubmed.ncbi.nlm.nih.gov/29378266/)). PTEN loss occurs in ~9.5%. However, ASCL1-high/YAP1-low tumors are immune-cold, and some extrapulmonary variants (HPV18+ cervical LCNEC) are poorly immunogenic (TMB 1.21/Mb, minimal PD-L1) with ICI resistance ([PMID: 42521492](https://pubmed.ncbi.nlm.nih.gov/42521492/)).

**Tissue damage mechanisms.** Extensive tumor necrosis, spread-through-air-spaces (STAS identified in 71–88% of high-grade large-/small-cell NE carcinomas; [PMID: 31201506](https://pubmed.ncbi.nlm.nih.gov/31201506/)), and destructive local/metastatic growth.

**Cell types.** Pulmonary neuroendocrine cells / their precursors are the presumed cell of origin; adenocarcinoma cells can transdifferentiate into LCNEC (see transformation, below). Suggested CL terms: CL:0000165 (neuroendocrine cell), CL:0002333 (pulmonary neuroendocrine cell), CL:0001063 (neoplastic cell).

**Multi-omics / transformation (F013).** Combined LCNEC-adenocarcinoma cases show shared clonal *TP53* and *STK11* mutations across components with **MYC amplification acquired during neuroendocrine transformation** ([PMID: 39868963](https://pubmed.ncbi.nlm.nih.gov/39868963/)). Histologic transformation to LCNEC is an acquired *EGFR*-TKI resistance mechanism in *EGFR*-mutant adenocarcinoma ([PMID: 28768973](https://pubmed.ncbi.nlm.nih.gov/28768973/)).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ is most commonly the **lung** (~85% of LCNEC; UBERON:0002048), typically peripheral and upper-lobe. Extrapulmonary primaries (F007): **thymus/mediastinum** (UBERON:0002370), **gastrointestinal tract** — large-cell NEC was 42% of GI-NECs in a 143-case cohort ([PMID: 36264285](https://pubmed.ncbi.nlm.nih.gov/36264285/)), **uterus/cervix** (UBERON:0000995/UBERON:0000002; [PMID: 42111278](https://pubmed.ncbi.nlm.nih.gov/42111278/)), **breast** (UBERON:0000310; [PMID: 39585672](https://pubmed.ncbi.nlm.nih.gov/39585672/)), **gallbladder** (UBERON:0002110; [PMID: 40789532](https://pubmed.ncbi.nlm.nih.gov/40789532/)), and **ovary** (UBERON:0000992).

**Secondary organ involvement.** Bone (~23% synchronous), brain, liver, and regional lymph nodes are common metastatic sites and independent adverse prognostic factors ([PMID: 39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/); [PMID: 40634407](https://pubmed.ncbi.nlm.nih.gov/40634407/)).

**Body systems.** Respiratory (primary), plus skeletal, nervous (CNS), hepatic, and lymphatic systems (metastatic).

**Tissue and cell level.** Epithelial-derived neuroendocrine tumor; targeted/derived cell type is the neuroendocrine cell (CL:0000165) and pulmonary neuroendocrine cell (CL:0002333).

**Subcellular level.** Dense-core neurosecretory granules (basis of chromogranin A/synaptophysin positivity). Suggested GO cellular-component terms: GO:0030141 (secretory granule), GO:0005739 (mitochondrion), GO:0005634 (nucleus).

**Localization / lateralization.** Pulmonary LCNEC is typically a solitary peripheral mass, often upper lobe; laterality is variable (unilateral primary with potential bilateral/distant metastases).

---

## 8. Temporal Development

**Onset.** Adult/geriatric (mean age at surgery ~63.8 years; [PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/)). Onset is insidious with non-specific symptoms, frequently leading to advanced-stage presentation ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/); [PMID: 39287289](https://pubmed.ncbi.nlm.nih.gov/39287289/)).

**Progression / staging.** Staged by AJCC TNM (lung). Progression is rapid, with early nodal and distant metastasis; ~half present at advanced stage and ~23% of high-grade lung NEC have synchronous bone metastasis at diagnosis ([PMID: 40634407](https://pubmed.ncbi.nlm.nih.gov/40634407/)). Disease course is aggressive and progressive rather than relapsing-remitting.

**Duration / patterns.** Chronic in the sense of a lethal, progressive course; median OS in stage IV is ~7.4 months ([PMID: 41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/)). Remissions are treatment-induced, generally not durable. The critical intervention window is at the localized/resectable stage, where surgery offers the best survival.

---

## 9. Inheritance and Population

**Epidemiology.** Incidence ~0.3–3% of lung cancers ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/)); ~3% is a commonly cited figure ([PMID: 41510101](https://pubmed.ncbi.nlm.nih.gov/41510101/)). Incidence appears to be rising, partly due to improved diagnostics ([PMID: 40114491](https://pubmed.ncbi.nlm.nih.gov/40114491/)).

**Inheritance.** Not heritable — somatic, tobacco-driven malignancy with **no Mendelian OMIM entry** (F014). Concepts of penetrance, expressivity, anticipation, founder effects, consanguinity, and carrier frequency are **not applicable**.

**Demographics.** Male predominance (~68.8% men; [PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/)); elderly smokers. Sex is an independent prognostic factor (DSS HR ~1.17 for the higher-risk sex; [PMID: 39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/)). Geographic distribution parallels tobacco-use patterns; no established ethnic predisposition beyond smoking prevalence.

---

## 10. Diagnostics

**Histopathology + IHC (mandatory).** Diagnosis requires non-small-cell neuroendocrine **morphology** (large cells, organoid/palisading architecture, extensive necrosis, severe atypia, >10 mitoses/2 mm² [typically mean ~70–75]) **plus IHC confirmation** of neuroendocrine differentiation. "The confirmation of the neuroendocrine signature by immunohistochemistry is mandatory for the diagnosis; a minimum panel comprising chromogranin A and synaptophysin is recommended" ([PMID: 28871510](https://pubmed.ncbi.nlm.nih.gov/28871510/)). CD56 is diffusely positive; INSM1 and high Ki-67 aid diagnosis ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/); [PMID: 40805240](https://pubmed.ncbi.nlm.nih.gov/40805240/)).

**Ki-67 / grading.** Grading in lung NE neoplasms uses mitotic count ±necrosis; Ki-67 is a helpful adjunct (and its formal inclusion is debated; [PMID: 38728050](https://pubmed.ncbi.nlm.nih.gov/38728050/)). LCNEC shows a high Ki-67 index.

**Diagnostic reliability.** Substantial interobserver variability; central pathology review confirmed LCNEC in only 67% of submitted cases in the Netherlands Cancer Registry (others reclassified as SCLC 34%, NSCLC-NOS 34%) ([PMID: 41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/)). A systematic review found central pathology review is applied in <one-third of studies with marked methodological heterogeneity ([PMID: 42556470](https://pubmed.ncbi.nlm.nih.gov/42556470/)).

**Molecular / genomic testing.** Comprehensive genomic profiling (NGS panels, WES) is useful for subtyping (SCLC-like vs NSCLC-like vs carcinoid-like) and for identifying actionable alterations ([PMID: 38159439](https://pubmed.ncbi.nlm.nih.gov/38159439/); [PMID: 41653583](https://pubmed.ncbi.nlm.nih.gov/41653583/)). RB1 IHC (pRb status) is used for stratification in registry studies ([PMID: 41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/)). Emerging epigenomic cfDNA/liquid-biopsy approaches can detect neuroendocrine transformation noninvasively ([PMID: 38912901](https://pubmed.ncbi.nlm.nih.gov/38912901/)).

**Imaging.** CT and PET for staging; brain MRI given CNS metastasis risk; pro-gastrin-releasing peptide (pro-GRP) can serve as a circulating tumor marker in NE tumors and tracks response (e.g., 1610 → 49.7 ng/mL on tarlatamab; [PMID: 42491047](https://pubmed.ncbi.nlm.nih.gov/42491047/)).

**Differential diagnosis.** SCLC (smaller cells, finer chromatin, higher N:C ratio), basaloid squamous carcinoma, atypical carcinoid (lower mitoses, no necrosis), and metastatic NEC from other sites. IHC (INSM1, chromogranin, synaptophysin, TTF-1, Ki-67) and molecular context resolve most cases.

---

## 11. Outcome / Prognosis

**Survival.** Poor overall; stage-dependent.

| Setting | Outcome | Source |
|---------|---------|--------|
| Stage IV, panel-reviewed | Median OS ~7.4 months | [PMID: 41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/) |
| Resected (EPITHOR, n=1,229) | 5-year OS 52.9% (vs SCLC 45.5%) | [PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/) |
| Resected, stage-selected series | 5-year survival ~86% | [PMID: 41376913](https://pubmed.ncbi.nlm.nih.gov/41376913/) |

**Independent prognostic factors (SEER, n=2,897; F008).** Surgery (HR 0.481, protective), chemotherapy (HR 0.450, protective), bone metastasis (HR 1.284), brain metastasis (HR 1.167), liver metastasis (HR 1.223), plus AJCC N-stage, tumor stage, sex, and age ([PMID: 39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/)). Tobacco, sex, TNM stage, and histologic type were independently associated with OS in EPITHOR ([PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/)).

**Molecular prognostic markers.** Homologous-recombination pathway alterations predict longer PFS with systemic therapy (P=.005; [PMID: 35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/)); LAT1 overexpression predicts poor outcome ([PMID: 18440724](https://pubmed.ncbi.nlm.nih.gov/18440724/)); immune-cell infiltration associates with better PFS ([PMID: 29378266](https://pubmed.ncbi.nlm.nih.gov/29378266/)).

**Complications.** Bone, brain, and liver metastases; early death is common in stage IV (predictive nomograms achieve AUC ~0.85; [PMID: 39287289](https://pubmed.ncbi.nlm.nih.gov/39287289/)).

---

## 12. Treatment

Treatment is extrapolated from SCLC and NSCLC. Suggested NCIT terms in parentheses.

**Pharmacotherapy — first line.** Platinum (cisplatin/carboplatin) + etoposide chemotherapy is the backbone: "In metastatic disease, etoposide-platinum chemotherapy remains the first-line treatment, while targeted therapy can be considered if tumors harbor actionable genomic alterations" ([PMID: 41653583](https://pubmed.ncbi.nlm.nih.gov/41653583/)). NCIT: C63419 (etoposide), C376 (cisplatin), C1282 (carboplatin).

**Chemoimmunotherapy (F003).** Adding immune checkpoint inhibitors improves outcomes: pooled ORR 49% (95% CI 43–55); vs chemo alone ORR OR 2.52; first-line chemo+ICI improved OS (HR 0.72, 95% CI 0.58–0.89) without increasing grade ≥3 AEs ([PMID: 42208366](https://pubmed.ncbi.nlm.nih.gov/42208366/)). Real-world registry data show a survival benefit of immunotherapy (median OS 10.7 vs 6.7 months; HR 0.53) although panel-reviewed cohorts show a smaller, non-significant effect ([PMID: 41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/)). The phase II FIRST-NEC trial (durvalumab + platinum-etoposide, NCT06393816) is prospectively evaluating first-line immunochemotherapy ([PMID: 42526918](https://pubmed.ncbi.nlm.nih.gov/42526918/)). NCIT: C1649 (pembrolizumab), checkpoint inhibitors (durvalumab).

**Targeted / emerging — DLL3-directed therapy (F009).** DLL3 is highly expressed in SCLC-like/ASCL1-associated LCNEC. **Tarlatamab** (DLL3×CD3 bispecific T-cell engager) received FDA accelerated approval (2024) and full approval (2025) for SCLC ([PMID: 42449715](https://pubmed.ncbi.nlm.nih.gov/42449715/)). In a relapsed/refractory LCNEC case (6th-line), tarlatamab produced a partial response (130→78 mm, 40% reduction) with pro-GRP falling 1610→49.7 ng/mL and only grade 1 CRS ([PMID: 42491047](https://pubmed.ncbi.nlm.nih.gov/42491047/)). In DLL3-high pulmonary carcinoid (n=11), response rate was 73% with 100% disease control ([PMID: 42562260](https://pubmed.ncbi.nlm.nih.gov/42562260/)). Additional emerging modalities: TROP2- and B7-H3-directed agents and antibody-drug conjugates ([PMID: 42592685](https://pubmed.ncbi.nlm.nih.gov/42592685/); [PMID: 42582332](https://pubmed.ncbi.nlm.nih.gov/42582332/)). NCIT: C171398 (tarlatamab).

**Surgery.** Central to localized disease and independently protective (HR 0.481; [PMID: 39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/)). Anatomic resection is performed in ~97% of operable cases (90-day mortality ~8.3%; [PMID: 42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/)). In stage I, sublobectomy was an effective option in one SEER analysis ([PMID: 40950692](https://pubmed.ncbi.nlm.nih.gov/40950692/)).

**Radiotherapy.** Chemoradiotherapy improves OS/CSS in stage III; its role in stage IV is context-dependent ([PMID: 42231825](https://pubmed.ncbi.nlm.nih.gov/42231825/)).

**Adjuvant therapy.** SCLC-type adjuvant regimens are associated with better outcomes in resected disease, though in T1-2N0M0 SEER analyses adjuvant chemotherapy did not show a significant OS/CSS benefit over surgery alone in the overall cohort ([PMID: 41510101](https://pubmed.ncbi.nlm.nih.gov/41510101/); [PMID: 41153253](https://pubmed.ncbi.nlm.nih.gov/41153253/)).

**Neuroendocrine-transformed disease.** In *EGFR*-mutant NSCLC with NE transformation, durvalumab + etoposide-platinum gave ORR 43%, median OS 10.2 months (ORCHARD; [PMID: 42361644](https://pubmed.ncbi.nlm.nih.gov/42361644/)).

**Personalized medicine.** Genomic subtyping guides therapy: YAP1-high → MEK/AXL strategies; YAP1-low/DLL3-high → DLL3/CD56 targeting ([PMID: 39150543](https://pubmed.ncbi.nlm.nih.gov/39150543/)); actionable NSCLC drivers → targeted agents ([PMID: 41653583](https://pubmed.ncbi.nlm.nih.gov/41653583/)).

---

## 13. Prevention

- **Primary prevention:** Tobacco control and smoking cessation are the principal strategies, given the dominant smoking etiology ([PMID: 36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/)).
- **Secondary prevention:** Low-dose CT lung cancer screening in high-risk (heavy-smoking, elderly) populations may detect early-stage disease, where surgery is most effective — though LCNEC-specific screening data are lacking.
- **Tertiary prevention:** Surveillance for and management of bone/brain/liver metastases; multimodal therapy to prevent complications.
- **Immunization:** For **cervical** LCNEC, HPV vaccination is a plausible primary preventive measure given HPV18 causation ([PMID: 42521492](https://pubmed.ncbi.nlm.nih.gov/42521492/)); not applicable to pulmonary LCNEC.
- **Genetic counseling / carrier screening:** Not applicable (somatic disease).

---

## 14. Other Species / Natural Disease

Species-specific data for LCNEC are limited. NCBI Taxonomy: *Homo sapiens* (9606). Orthologous driver genes are highly conserved across mammals (*Tp53*, *Rb1*, *Kras*, *Stk11*, *Ascl1*, *Dll3*), supporting cross-species relevance of the pathways involved. Naturally occurring high-grade neuroendocrine carcinomas are reported in companion animals (e.g., pulmonary and gastrointestinal NECs in dogs and cats via OMIA/veterinary literature), but LCNEC-specific comparative pathology was not systematically retrieved in this investigation and remains a knowledge gap. There is no zoonotic transmission (non-communicable neoplasm).

---

## 15. Model Organisms

Direct LCNEC-specific models were not the focus of the retrieved literature, but the field draws heavily on **SCLC genetically engineered mouse models (GEMMs)**, given the SCLC-like biology of most LCNEC. GEMMs based on conditional *Tp53/Rb1* inactivation (and *Trp53/Rb1/Myc* combinations) recapitulate high-grade neuroendocrine lung carcinoma and are used to validate driver mutations and targeted therapies ([PMID: 31134494](https://pubmed.ncbi.nlm.nih.gov/31134494/)). Patient-derived xenografts (including circulating-tumor-cell–derived xenografts, CDX) and patient-derived organoids are used for high-grade NE tumors and for mixed carcinomas (e.g., an endometrial mixed LCNEC organoid/xenograft revealing PI3K/VEGF vulnerabilities; [PMID: 41886729](https://pubmed.ncbi.nlm.nih.gov/41886729/)). Cell lines expressing ASCL1 and NE markers model the ASCL1 super-enhancer program ([PMID: 30121393](https://pubmed.ncbi.nlm.nih.gov/30121393/)).

**Model resources:** MGI (mouse), Cellosaurus/ATCC (cell lines), and PDX/organoid biobanks. **Limitations:** Few models are LCNEC-specific (as opposed to SCLC); the NSCLC-like and YAP1-high subtypes are underrepresented; models incompletely capture the human tumor immune microenvironment and the interobserver diagnostic ambiguity.

---

## Mechanistic Model / Interpretation

LCNEC is best understood as a **lineage-plastic, tobacco-driven high-grade neuroendocrine carcinoma that molecularly bridges SCLC and NSCLC**. A unifying model:

| Axis | SCLC-like pole | NSCLC-like pole |
|------|----------------|-----------------|
| Drivers | *RB1* + *TP53* | *KEAP1/KRAS/STK11/SMARCA4/CDKN2A* |
| Transcription factors | ASCL1, NEUROD1 high | — |
| YAP1 | Low | High |
| Surface target | DLL3 high, CD56 | — |
| Immune phenotype | Immune-cold | Mesenchymal, inflamed |
| Therapeutic vulnerability | DLL3 (tarlatamab), platinum-etoposide | MEK/AXL, NSCLC-driver–targeted agents |

Upstream, tobacco carcinogens generate a high mutational burden and near-universal *TP53* loss. The bifurcation into SCLC-like vs NSCLC-like programs — reinforced by epigenetic machinery (DNMT1/DNMT3A, ASCL1 super-enhancers, promoter hypermethylation) — determines transcription-factor identity, surface-antigen expression (notably DLL3), immune phenotype, and druggable vulnerabilities. Downstream, high-grade proliferation, necrosis, and spread-through-air-spaces produce early metastasis and poor survival. A distinct **transformation route** exists whereby *EGFR*-mutant adenocarcinoma converts to LCNEC under TKI pressure, acquiring MYC amplification atop shared clonal *TP53*/*STK11*. This model directly rationalizes emerging precision approaches: DLL3-directed T-cell engagers for the SCLC-like/ASCL1/DLL3-high pole and MEK/AXL or driver-targeted agents for the YAP1-high/NSCLC-like pole.

---

## Evidence Base

| PMID | Contribution |
|------|-------------|
| [40830141](https://pubmed.ncbi.nlm.nih.gov/40830141/) | Defines SCLC-like vs NSCLC-like genomic subtypes; DLL3-high in SCLC-like LCNEC |
| [38159439](https://pubmed.ncbi.nlm.nih.gov/38159439/) | Large CGP cohort; SCLC-like (n=557), carcinoid-like (n=25) definitions |
| [35641209](https://pubmed.ncbi.nlm.nih.gov/35641209/) | TMB (12.7/Mb); NOTCH/TP53 mutations; HR-pathway predicts PFS |
| [39150543](https://pubmed.ncbi.nlm.nih.gov/39150543/) | YAP1-high vs YAP1-low subtypes and vulnerabilities |
| [36304941](https://pubmed.ncbi.nlm.nih.gov/36304941/) | Incidence, demographics, IHC markers |
| [28871510](https://pubmed.ncbi.nlm.nih.gov/28871510/) | Mandatory IHC (chromogranin A + synaptophysin); histologic features |
| [31201506](https://pubmed.ncbi.nlm.nih.gov/31201506/) | STAS in 71–88% of high-grade NE carcinomas |
| [42208366](https://pubmed.ncbi.nlm.nih.gov/42208366/) | Chemoimmunotherapy meta-analysis (ORR 49%, OS HR 0.72) |
| [41653583](https://pubmed.ncbi.nlm.nih.gov/41653583/) | Platinum-etoposide first-line standard |
| [39268117](https://pubmed.ncbi.nlm.nih.gov/39268117/) | SEER independent prognostic factors with HRs |
| [42341696](https://pubmed.ncbi.nlm.nih.gov/42341696/) | EPITHOR resected 5-year OS 52.9%; demographics |
| [41376913](https://pubmed.ncbi.nlm.nih.gov/41376913/) | Stage-selected resected 5-year survival ~86% |
| [42491047](https://pubmed.ncbi.nlm.nih.gov/42491047/) | Tarlatamab clinical activity in LCNEC |
| [42449715](https://pubmed.ncbi.nlm.nih.gov/42449715/) | Tarlatamab FDA approval status |
| [42562260](https://pubmed.ncbi.nlm.nih.gov/42562260/) | Tarlatamab in DLL3-high pulmonary carcinoid (73% RR) |
| [29378266](https://pubmed.ncbi.nlm.nih.gov/29378266/) | PD-L1/immune infiltration in high-grade lung NEC |
| [41854102](https://pubmed.ncbi.nlm.nih.gov/41854102/) | DNMT1/DNMT3A upregulation in LCNEC |
| [39832203](https://pubmed.ncbi.nlm.nih.gov/39832203/) | LCNEC as methylation bridge between NSCLC/SCLC |
| [30121393](https://pubmed.ncbi.nlm.nih.gov/30121393/) | ASCL1 as master super-enhancer regulator |
| [39868963](https://pubmed.ncbi.nlm.nih.gov/39868963/) | MYC-amplified NE transformation; clonal TP53/STK11 |
| [28768973](https://pubmed.ncbi.nlm.nih.gov/28768973/) | LCNEC transformation as EGFR-TKI resistance |
| [41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/) | Stage IV median OS 7.4 mo; 67% diagnostic confirmation |
| [42556470](https://pubmed.ncbi.nlm.nih.gov/42556470/) | Central pathology review heterogeneity |
| [18440724](https://pubmed.ncbi.nlm.nih.gov/18440724/) | LAT1 overexpression (52.4%) and poor outcome |
| [42521492](https://pubmed.ncbi.nlm.nih.gov/42521492/) | Immune-cold HPV18+ cervical LCNEC, ICI resistance |

---

## Limitations and Knowledge Gaps

1. **Diagnostic reproducibility.** LCNEC is confirmed in only ~67% of cases on central review, with substantial interobserver variability ([PMID: 41240593](https://pubmed.ncbi.nlm.nih.gov/41240593/); [PMID: 42556470](https://pubmed.ncbi.nlm.nih.gov/42556470/)). This introduces classification bias into all registry-based epidemiology and outcomes data.
2. **Evidence quality.** Much survival/treatment evidence derives from retrospective SEER/registry analyses and single-arm/case reports; prospective randomized data specific to LCNEC are scarce (FIRST-NEC is ongoing).
3. **Rarity and subtype under-sampling.** NSCLC-like and YAP1-high subtypes, and extrapulmonary LCNEC, are underrepresented; treatment is largely extrapolated from SCLC/NSCLC.
4. **Quality-of-life data.** No LCNEC-specific EQ-5D/SF-36/PROMIS data were identified.
5. **Model organisms.** Few LCNEC-specific in vivo models exist; the field relies on SCLC GEMMs and PDX/organoids.
6. **Predictive biomarkers.** Reliable biomarkers for ICI benefit and hyperprogression risk are not established.
7. **Comparative/veterinary biology.** Naturally occurring LCNEC in other species is poorly characterized.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective subtype-stratified trials.** Complete and expand trials like FIRST-NEC (NCT06393816) and add DLL3-directed arms (tarlatamab) for SCLC-like/DLL3-high LCNEC, and MEK/AXL inhibitor arms for YAP1-high tumors.
2. **Standardize diagnosis.** Adopt the structured central-pathology-review reporting form and combine IHC + molecular subtyping (RB1 IHC, targeted NGS) to reduce misclassification ([PMID: 42556470](https://pubmed.ncbi.nlm.nih.gov/42556470/)).
3. **Biomarker development.** Validate DLL3, ASCL1/NEUROD1/YAP1, TMB, PD-L1, and HR-deficiency as predictive biomarkers; develop cfDNA/epigenomic liquid biopsies for transformation detection and monitoring ([PMID: 38912901](https://pubmed.ncbi.nlm.nih.gov/38912901/)).
4. **Model building.** Generate LCNEC-specific GEMMs and organoids representing NSCLC-like and YAP1-high subtypes for preclinical drug testing.
5. **Epigenetic therapy.** Test DNMT inhibitors (given DNMT1/DNMT3A upregulation) and ASCL1/super-enhancer-directed strategies ([PMID: 41854102](https://pubmed.ncbi.nlm.nih.gov/41854102/); [PMID: 30121393](https://pubmed.ncbi.nlm.nih.gov/30121393/)).
6. **Extrapulmonary registries.** Establish site-specific registries (thymic, GI, gynecologic) to define subtype-specific biology and optimal therapy.
7. **Patient-reported outcomes.** Collect LCNEC-specific QoL data prospectively.

---

*Report compiled from 15 confirmed findings across 67 reviewed papers. Evidence sources span human clinical (registries, cohorts, case reports), in vitro/genomic profiling, and computational/ontology lookups.*


## Artifacts

- [OpenScientist final report](Large_Cell_Neuroendocrine_Carcinoma-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Large_Cell_Neuroendocrine_Carcinoma-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 49 |
| On topic | 37 |
| Off topic | 0 |

All extracted references resolved successfully.