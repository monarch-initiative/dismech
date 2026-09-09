---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-28T10:12:26.577759'
end_time: '2026-08-28T10:27:11.862429'
duration_seconds: 885.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: ACTH-independent Macronodular Adrenal Hyperplasia 3
  mondo_id: ''
  category: Mendelian
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
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 10
  validator_version: 0.2.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: ACTH-independent_Macronodular_Adrenal_Hyperplasia_3-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: ACTH-independent_Macronodular_Adrenal_Hyperplasia_3-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ACTH-independent Macronodular Adrenal Hyperplasia 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **ACTH-independent Macronodular Adrenal Hyperplasia 3** covering all of the
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

# ACTH-Independent Macronodular Adrenal Hyperplasia 3 (AIMAH3) — Comprehensive Disease Report

**Prepared for a disease knowledge-base entry. Evidence is human clinical / genetic unless otherwise stated. Primary citations are given as PMIDs.**

---

## Summary (Answer to the Research Question)

ACTH-independent Macronodular Adrenal Hyperplasia 3 (AIMAH3; OMIM #620990; MONDO:0700299) is a rare, autosomal-dominant Mendelian endocrine tumor-predisposition syndrome that is the genetically defined form of **food-dependent (GIP-dependent) Cushing syndrome (FDCS)**. It is caused by **germline heterozygous loss-of-function (truncating) variants in *KDM1A* (LSD1; chromosome 1p36; gene OMIM 609132)** combined with **somatic loss of the wild-type allele on 1p** in adrenal nodules — a two-hit tumor-suppressor mechanism. Biallelic *KDM1A* inactivation in adrenocortical cells permits **ectopic expression of the glucose-dependent insulinotropic polypeptide receptor (GIPR)**; meal-stimulated GIP (from duodenal K cells) then binds adrenal GIPR, activates cAMP/PKA, and drives **post-prandial cortisol hypersecretion**, producing ACTH-independent Cushing syndrome on a background of **bilateral macronodular adrenal hyperplasia**. It accounts for ~3.3% of all primary bilateral macronodular adrenal hyperplasia (PBMAH) index cases and ~90% of FDCS, shows a striking female predominance, and is definitively treated by adrenalectomy.

---

## 1. Disease Information

- **Overview:** AIMAH3 is a subtype within the ACTH-independent macronodular adrenal hyperplasia phenotypic series in which bilateral, benign, large adrenocortical nodules autonomously secrete cortisol under the control of ingested food. It is the molecular subtype of **food-dependent Cushing syndrome**. Individuals characteristically have **low fasting morning cortisol and low/suppressed ACTH but excess cortisol after eating**.
- **Key identifiers:**
  - **OMIM:** #620990 (AIMAH3); phenotypic series **PS219080** (AIMAH). Gene *KDM1A* OMIM 609132.
  - **MONDO:** MONDO:0700299
  - **MedGen:** CN378661
  - **MeSH:** the closest heading is Cushing Syndrome (D003480); "adrenal hyperplasia, macronodular" is indexed under adrenocortical hyperplasia. No AIMAH3-specific MeSH.
  - **ICD-11:** 5A70 (Cushing syndrome) / 5A74.0 region for ACTH-independent Cushing; **ICD-10:** E24.0 (pituitary-dependent) is not applicable — adrenal Cushing is **E24.8/E24.9**; adrenal hyperplasia **E27.8**. No AIMAH3-specific code.
  - **Orphanet:** Covered under "ACTH-independent macronodular adrenal hyperplasia" (ORPHA:189439 for PBMAH); no distinct AIMAH3 ORPHA code.
  - **UniProt disease:** DI-06963.
- **Synonyms / alternative names:** AIMAH3; ACTH-independent macronodular adrenal hyperplasia 3; **Food-dependent Cushing syndrome (FDCS)**; **GIP-dependent Cushing syndrome**; GIP-dependent PBMAH; (broader, non-synonymous parent terms) primary bilateral macronodular adrenal hyperplasia (PBMAH), bilateral macronodular adrenal disease (BMAD).
- **Position within the AIMAH phenotypic series (PS219080):**

  | Subtype | OMIM # | Gene (OMIM) | Locus | Mechanism | Distinctive feature |
  |---|---|---|---|---|---|
  | AIMAH1 | #219080 | *GNAS* (139320) | 20q13 | **Somatic** activating mutation (R201H/R201S; constitutive Gs) | Not McCune-Albright; mutation absent in blood |
  | AIMAH2 | #615954 | *ARMC5* (615549) | 16p11.2 | Germline + somatic (**two-hit**) | Commonest genetic PBMAH (~20–25%); no food dependence |
  | **AIMAH3** | **#620990** | ***KDM1A* (609132)** | **1p36** | Germline + somatic (**two-hit**, 1p LOH) | **Food/GIP-dependent Cushing** |

  AIMAH patients typically present in the **5th–6th decade (~10 years later than other Cushing causes)**, and most cases are sporadic (OMIM PS219080; Assié 2013 identified ARMC5 in 18/33=55% of macronodular hyperplasia tumors; Chasseloup 2021 PMID 34655521 reported 17 GIP-dependent PBMAH cases with a recurrent 1p/KDM1A deletion).
- **Data source type:** Information is derived from **aggregated disease-level genetic/clinical cohort studies and case series** (e.g., 301-case and 36-case multicentre cohorts) plus individual case reports — not from a single EHR dataset.

---

## 2. Etiology

- **Primary cause — genetic:** Germline heterozygous **inactivating (truncating: frameshift/nonsense) variants in *KDM1A***, with a **somatic second hit** (loss of heterozygosity / deletion of chromosome 1p bearing the wild-type allele) in adrenocortical lesions. "Exome sequencing revealed germline truncating variants of KDM1A … constantly associated with a somatic loss of the KDM1A wild-type allele on 1p, leading to a loss of KDM1A expression both at messenger RNA and protein levels" and "KDM1A inactivation explains about 90% of FDCS PBMAH" (PMID 34906447). This is a two-hit tumor-suppressor model (PMID 41864332).
- **Genetic risk factors:** The germline *KDM1A* LoF allele is the causal susceptibility factor; disease requires the acquired somatic 1p loss. No additional common susceptibility loci are established. *ARMC5* (AIMAH2/PBMAH1) is the differential genetic cause and is **mutually exclusive** with the FDCS phenotype (PMID 39921449).
- **Environmental risk factors / triggers:** The obligate physiological "trigger" is **food/meal intake**, which raises GIP and drives cortisol secretion. Female sex is a strong, unexplained risk marker (100% of KDM1A carriers were women in the largest cohort; PMID 39921449). No toxin, radiation, or occupational exposure is implicated.
- **Protective factors:** None established genetically or environmentally. Conceptually, avoiding the GIP–GIPR axis (e.g., fasting) transiently lowers cortisol but is not therapeutic. Somatic events being required means most heterozygous carriers may remain unaffected (incomplete penetrance).
- **Gene–environment interaction:** The defining GxE interaction is **KDM1A loss (genetic) × dietary GIP secretion (environmental/physiological)** → post-prandial hypercortisolism. Without the genetic lesion, food does not stimulate cortisol; without food, the genetic lesion produces little fasting cortisol excess.
- **Infectious agents:** Not applicable.

---

## 3. Phenotypes

The clinical phenotype is that of **chronic endogenous cortisol excess (Cushing syndrome)**, but with a food-dependent secretory pattern. Onset is typically **adult** (commonly 4th–6th decades), insidious, and slowly progressive. Severity is variable (mild autonomous cortisol secretion → overt Cushing). Key phenotypes and suggested HPO terms:

| Phenotype | Type | HPO term | Notes / frequency |
|---|---|---|---|
| Cushingoid habitus / truncal (central) obesity | physical sign | HP:0002591 (truncal obesity), HP:0001513 (obesity) | Common (OMIM clinical synopsis) |
| Facial fullness ("moon facies") | physical sign | HP:0000283 | Common |
| Arterial hypertension | clinical sign | HP:0000822 | Very common; PBMAH cohorts show high rates |
| Type 2 diabetes / glucose intolerance | lab/clinical | HP:0000857 / HP:0000833 | Common (45% diabetes in PBMAH vs 25% non-PBMAH, PMID 35597729) |
| Abdominal striae | physical sign | HP:0001065 (Striae distensae) | Reported in OMIM synopsis |
| Proximal muscle weakness | symptom/sign | HP:0003701 (proximal muscle weakness) / HP:0003324 | From cortisol-induced myopathy |
| Osteoporosis | lab/imaging | HP:0000939 | Reported |
| Hypercortisolemia / loss of diurnal rhythm | lab abnormality | HP:0003118 (abnormal circulating cortisol), HP:0003119 region | Defining; low AM/high PM cortisol |
| Suppressed ACTH (ACTH-independent) | lab abnormality | HP:0002920 (decreased ACTH) | Defining |
| Bilateral adrenal macronodular hyperplasia | imaging/structural | HP:0008256 (Adrenal hyperplasia); HP:0031044 (adrenocortical hyperplasia) | Defining, bilateral |
| Elevated urinary free cortisol | lab abnormality | HP:0003564 (Hypercortisoluria) | 3.0× ULN in KDM1A vs 1.36× ARMC5 (PMID 39921449) |

- **Phenotype characteristics:** Adult-onset; severity mild→severe/variable; course chronic and slowly progressive; the biochemical hallmark is the **inverted cortisol rhythm** (low morning, high post-prandial/midnight). In the 301-case cohort, KDM1A patients had **higher 24h UFC (3.0× ULN), lower morning cortisol (192 vs 407/428 nmol/L), higher midnight cortisol (487 vs 297/172 nmol/L)** (PMID 39921449).
- **Quality-of-life impact:** As for other forms of Cushing syndrome — impaired physical function (myopathy, obesity, fractures), metabolic/cardiovascular morbidity, and neuropsychiatric effects (mood disturbance, cognitive complaints) reduce QoL; disease-specific QoL is measured with CushingQoL and generic SF-36/EQ-5D. No AIMAH3-specific QoL study exists (data gap).

---

## 4. Genetic / Molecular Information

- **Causal gene:** ***KDM1A*** (lysine demethylase 1A; alias **LSD1, KDM1, AOF2**). HGNC:29079; NCBI Gene 23028; Ensembl ENSG00000004487; UniProt O60341. Gene OMIM 609132. Locus **1p36.12**.
- **Pathogenic variants:**
  - **Classification:** Pathogenic / likely pathogenic per ACMG/AMP (PMID 39921449). VUS reported in broad incidentaloma panels (PMID 41113712).
  - **Variant type/class:** Predominantly **truncating loss-of-function** — frameshift and nonsense (and splice) — germline (PMID 34906447). The second hit is a **somatic structural event (1p LOH/deletion)**.
  - **Allele frequency:** Germline *KDM1A* LoF variants are rare in gnomAD (KDM1A is relatively loss-of-function intolerant); no common population variant. Disease-associated alleles are private/family-specific.
  - **Somatic vs germline:** **Both** required — germline heterozygous LoF + somatic 1p loss (two-hit).
  - **Functional consequence:** **Loss of function** (loss of KDM1A mRNA and protein in adrenal tissue; PMID 34906447), consistent with tumor-suppressor behavior (PMID 41864332).
- **Modifier genes:** None established. *ARMC5* status is mutually exclusive (defines AIMAH2).
- **Epigenetic information:** KDM1A/LSD1 is itself an **epigenetic eraser** — a histone demethylase for **H3K4me1/2 and H3K9me1/2** (PMID 38152966) with scaffolding control of DNA methylation (PMID 39237615). Its loss perturbs the adrenocortical chromatin/transcriptional landscape and is thought to permit **de-repression/ectopic transcription of *GIPR***. Multiomics profiling included methylome and miRNome analyses defining a distinct FDCS molecular group (PMID 34906447).
- **Chromosomal abnormalities:** **Somatic loss of chromosome 1p** (LOH) in adrenal nodules is the recurrent large-scale event (PMID 34906447). In the distinct *unilateral* GIP-adenoma route, **somatic 19q13.32 duplication/rearrangement of the *GIPR* locus** occurs (PMID 36857084) — not AIMAH3.

---

## 5. Environmental Information

- **Environmental factors:** No toxin/radiation/pollution/occupational cause. The relevant "environmental" input is **dietary intake**, which triggers GIP secretion and hence cortisol release.
- **Lifestyle factors:** Meal composition/timing modulates GIP and therefore cortisol; oral (but not IV) glucose triggers cortisol (PMID 21264796). No smoking/alcohol association established.
- **Infectious agents:** Not applicable.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Germline heterozygous KDM1A LoF variant** (constitutional; every cell). *(GO: histone H3K4 demethylase activity GO:0032453; H3K9 demethylase GO:0032454; chromatin organization GO:0006325.)*
2. **Somatic loss of wild-type KDM1A allele (1p LOH)** in an adrenocortical clone → complete loss of KDM1A/LSD1 protein (PMID 34906447). *(Two-hit tumor suppressor; GO:0045596 negative regulation of cell differentiation, GO:0008285/0008284 regulation of cell proliferation.)*
3. **Ectopic expression of the non-mutated GIPR** in adrenocortical cells (aberrant chromatin de-repression) (PMID 36857084, 39059410). *(GO:0004930 G-protein coupled receptor activity; CHEBI: glucose-dependent insulinotropic polypeptide.)*
4. **Post-prandial GIP** (secreted by intestinal K cells; CL:0002097 type K enteroendocrine cell) binds adrenal GIPR → **Gs/cAMP/PKA activation** (GO:0071377 cellular response to glucagon-family peptide; GO:0007189 adenylate cyclase-activating GPCR signaling; cAMP CHEBI:17489).
5. **Stimulation of steroidogenesis** (StAR, CYP11A1, CYP11B1) → **meal-induced cortisol (CHEBI:17650) hypersecretion** and adrenocortical cell proliferation.
6. **Chronic ACTH-independent hypercortisolism** → Cushing syndrome; cortisol feedback suppresses pituitary ACTH (→ low ACTH; internodular adrenal cortex may atrophy).

- **Molecular pathways:** cAMP/PKA signaling (central); GPCR signaling; chromatin/epigenetic regulation (LSD1); Wnt/β-catenin (LSD1 stabilizes β-catenin, PMID 38321961) and Notch (PMID 38152966) as LSD1-regulated proliferation/fate pathways. Reactome: GPCR/adenylate cyclase; KEGG: cortisol synthesis and secretion (hsa04927), cAMP signaling (hsa04024).
- **Cellular processes:** Adrenocortical cell proliferation (nodule formation), dysregulated steroidogenesis, epigenetic transcriptional de-repression.
- **Protein dysfunction:** **Loss of function** of LSD1 (loss of demethylase + scaffolding activity); **gain of aberrant signaling** through ectopic (structurally normal) GIPR.
- **Metabolic changes:** Secondary cortisol-driven metabolic syndrome — hyperglycemia/insulin resistance (type 2 diabetes), dyslipidemia, central adiposity, protein catabolism (myopathy), bone loss.
- **Immune involvement:** No primary autoimmunity; chronic cortisol excess is immunosuppressive (increased infection risk) — downstream, not causal.
- **Tissue-damage mechanisms:** Systemic glucocorticoid toxicity (vascular, bone, muscle, metabolic) rather than direct adrenal tissue injury.
- **Biochemical abnormality:** Receptor dysfunction (ectopic GIPR coupling meals to steroidogenesis) is the core defect.
- **Molecular profiling:** RNA-seq/exome/SNP-array/methylome/miRNome multiomics defined the FDCS group with GIPR ectopic expression and KDM1A loss (PMID 34906447); functional validation in the **H295R** human adrenocortical cell line (PMID 34655521).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** **Adrenal glands / adrenal cortex** — bilateral (UBERON:0002369 adrenal gland; UBERON:0001235 adrenal cortex). Lateralization: **bilateral**, often asymmetric nodularity.
- **Secondary organ involvement (from cortisol excess):** cardiovascular system (hypertension), pancreas/metabolic (diabetes), skeleton (osteoporosis/fractures), skeletal muscle (myopathy), skin (striae), CNS (neuropsychiatric). Body system: **endocrine** (primary), with cardiovascular, musculoskeletal, integumentary, and metabolic secondary involvement.
- **Tissue / cell level:** Adrenocortical epithelial/steroidogenic cells — **CL:0000538 (adrenal cortex cell)** / zona fasciculata cells; ectopic GIPR on these cells. Trigger cells: intestinal **K cells (CL:0002097)** secreting GIP.
- **Subcellular level:** Nucleus/chromatin (LSD1 site of action; GO:0000785 chromatin; GO:0005634 nucleus); plasma membrane (GIPR; GO:0005886); mitochondria and smooth ER (steroidogenesis; GO:0005739, GO:0005790).
- **Localization:** UBERON:0002369 (adrenal gland), UBERON:0001235 (adrenal cortex); bilateral.

---

## 8. Temporal Development

- **Onset:** Adult-onset (typically 40s–60s), **insidious/chronic**. Because a somatic second hit is required, clinical disease emerges in adulthood despite constitutional carriage.
- **Progression:** Slowly **progressive**; ranges from nonfunctional/mild autonomous cortisol secretion (MACS) to overt Cushing over years; adrenal mass/nodularity increases over time. Not staged formally (benign hyperplasia, not a malignancy staging system).
- **Duration/course:** Chronic, lifelong until surgically treated.
- **Patterns:** Post-prandial **episodic** cortisol surges superimposed on chronic excess; **treatment-induced remission** after adrenalectomy; no spontaneous remission. **Critical intervention window:** early detection in mutation-carrying relatives (cascade screening) before overt Cushing/metabolic damage.

---

## 9. Inheritance and Population

- **Epidemiology:** AIMAH3 is very rare. PBMAH itself is an uncommon cause of overt Cushing but a more frequent cause of bilateral adrenal incidentalomas (PMID 41864332); PBMAH is found in ~1/3 of adrenal-incidentaloma patients with subclinical hypercortisolism (PMID 35597729). **KDM1A explains ~3.3% of PBMAH index cases** (10/301) and **~90% of FDCS** (PMID 39921449, 34906447). Precise population prevalence/incidence figures are not established (data gap).
- **Inheritance:** **Autosomal dominant** predisposition (germline heterozygous LoF) with a required somatic second hit → **incomplete/variable penetrance** and variable expressivity. No genetic anticipation or repeat expansion. Founder effects/consanguinity not established. Germline mosaicism not specifically documented.
- **Carrier frequency:** Not established; germline KDM1A LoF is rare in gnomAD.
- **Population demographics:** **Striking female predominance — 100% of KDM1A carriers were women** in the largest cohort (vs ~65% ARMC5, ~67% wild-type; P=.0337) (PMID 39921449). No specific ethnic/geographic clustering established; cases reported across Europe, Canada, Brazil, and Asia.

---

## 10. Diagnostics

- **Laboratory tests / biomarkers:**
  - ACTH-independent hypercortisolism: **suppressed/low ACTH** (HP:0002920), elevated **24h urinary free cortisol** (3.0× ULN typical; PMID 39921449), loss of diurnal rhythm, **non-suppression on 1-mg overnight and low/high-dose dexamethasone** tests.
  - **Inverted rhythm:** low morning, high midnight/post-prandial cortisol. **Morning/midnight plasma cortisol ratio < 0.65 = 100% sensitivity and 100% specificity for FDCS** (PMID 39921449).
  - **Functional confirmatory test:** **Mixed-meal test** showing a significant post-prandial cortisol rise; cortisol rises after **oral but not IV glucose** (PMID 21264796). Screening for aberrant hormone receptors (posture, GnRH, glucagon, vasopressin) per Lacroix protocol may reveal multiple aberrant responses.
- **Imaging:** Adrenal **CT/MRI** shows **bilateral macronodular adrenal hyperplasia** (nodules >1 cm, enlarged glands). ¹⁸F-FDG/other functional imaging not required.
- **Histopathology:** Bilateral macronodular adrenocortical hyperplasia; immunohistochemistry can demonstrate **ectopic GIPR** and loss of KDM1A protein in nodules (PMID 34906447).
- **Genetic testing:** Recommended approach — **germline sequencing of *KDM1A* and *ARMC5*** for PBMAH patients and families (PMID 34906447: "Genetic screening for ARMC5 and KDM1A can now be offered for most PBMAH operated patients and their families"). WES/targeted NGS panels for adrenal tumorigenesis genes are used (PMID 41113712). Somatic 1p LOH can be confirmed on tumor DNA (SNP array/CMA). Single-gene KDM1A testing indicated when FDCS biochemistry is present.
- **Clinical criteria / differential diagnosis:** Diagnose per Endocrine Society/ESE hypercortisolism guidelines, then localize to ACTH-independent bilateral adrenal disease. **Differential:** ARMC5-PBMAH (AIMAH2; no food dependence), unilateral GIP-dependent adenoma (19q13.32; unilateral), other aberrant-receptor AIMAH (LH/hCG, β-adrenergic, vasopressin, serotonin), PPNAD/Carney complex (PRKAR1A), McCune-Albright (GNAS), cortisol-producing adenoma, and adrenocortical carcinoma.
- **Screening:** **Cascade genetic screening** of first-degree relatives of KDM1A carriers; biochemical screening (morning/midnight cortisol ratio, mixed-meal test) in carriers.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** AIMAH3 is a **benign** hyperplasia; prognosis is driven by **cortisol-excess complications**, not by malignancy. With treatment (adrenalectomy), hypercortisolism resolves and prognosis is good. Untreated chronic Cushing carries excess cardiovascular/metabolic/infectious mortality. No AIMAH3-specific survival statistics (data gap).
- **Morbidity/function:** Hypertension, type 2 diabetes, osteoporosis/fractures, myopathy, obesity, thromboembolic and infection risk, and neuropsychiatric morbidity — reversible in part after cure.
- **Complications:** Metabolic syndrome, cardiovascular disease, fragility fractures, infections; post-bilateral-adrenalectomy adrenal insufficiency requiring lifelong replacement.
- **Recovery:** Marked clinical/metabolic improvement after adrenalectomy (PMID 21264796).
- **Prognostic factors/biomarkers:** Degree of hypercortisolism (24h UFC), presence of overt vs mild Cushing, nodule/adenomatous mass, and comorbidity burden. Genotype (KDM1A) predicts the FDCS phenotype and higher UFC (PMID 39921449).

---

## 12. Treatment

- **Surgical (mainstay; NCIT: Adrenalectomy C51765):**
  - **Bilateral adrenalectomy** — definitive for overt Cushing; achieves remission; requires **lifelong glucocorticoid + mineralocorticoid replacement**.
  - **Unilateral (total/subtotal/partial) adrenalectomy** of the more nodular gland — controls milder disease while preserving some adrenal function; effective in ARMC5-PBMAH and applicable to bilateral disease.
- **Pharmacotherapy:**
  - **Somatostatin analogues** (octreotide, octreotide-LAR; multi-ligand **pasireotide/SOM230**) — acutely abolish meal-induced cortisol but show **tachyphylaxis/escape within months** with no durable benefit (PMID 21264796, 23425648). NCIT: Octreotide C1214; Pasireotide C79861.
  - **Steroidogenesis inhibitors** (ketoconazole, metyrapone, osilodrostat, mitotane; NCIT: Ketoconazole C599, Metyrapone C61890, Osilodrostat C124087) — symptomatic control of hypercortisolism (general Cushing management).
  - **GIPR-targeted therapy (investigational/rational):** GIP-receptor antagonism directly addresses the ectopic-receptor mechanism but is not yet an established therapy.
- **Advanced therapeutics:** No approved gene/cell/RNA therapy. LSD1 inhibitors exist in oncology (e.g., iadademstat; PMID 40938473) but are **not** indicated here (the defect is LSD1 loss, so inhibition would be counterproductive).
- **Pharmacogenomics:** None specific to AIMAH3.
- **Treatment strategy / personalized medicine:** Genotype-guided — confirming FDCS/KDM1A supports a mechanism-based approach (meal-timing awareness, consideration of GIP-axis targeting) and, importantly, **family cascade testing**. Choice between unilateral vs bilateral adrenalectomy is individualized to disease severity.
- **Experimental trials:** No AIMAH3-specific registered trials identified; management follows PBMAH/Cushing frameworks (2023 ESE guidelines context, PMID 41871980).

---

## 13. Prevention

- **Primary prevention:** Not possible for the germline lesion. **Secondary prevention** is key: **cascade genetic screening** of relatives of KDM1A carriers and **biochemical surveillance** (morning/midnight cortisol ratio, mixed-meal test, adrenal imaging) to detect disease early before metabolic damage.
- **Tertiary prevention:** Aggressive management of hypertension, diabetes, osteoporosis, and thrombosis risk; adrenalectomy to prevent complications; post-surgical steroid replacement and sick-day rules to prevent adrenal crisis.
- **Genetic counseling:** Autosomal-dominant predisposition with incomplete penetrance; offer counseling regarding ~50% transmission of the germline allele and variable expression; prenatal/PGT is technically possible but rarely pursued for an adult-onset, treatable, benign condition.
- **Immunization/public-health/environmental:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *KDM1A* (NCBI Gene 23028). Orthologs: mouse *Kdm1a* (NCBI Gene 99982), rat *Kdm1a*, and conserved across vertebrates; LSD1 is highly evolutionarily conserved (present in plants, yeast SWM3/orthologs, Drosophila **Su(var)3-3**, C. elegans **spr-5**).
- **Natural disease in animals:** No naturally occurring KDM1A-driven food-dependent Cushing syndrome is documented in companion animals or wildlife (data gap). (Canine Cushing is usually pituitary-dependent or due to adrenal tumors; no GIP-dependent KDM1A analog reported.)
- **Comparative biology:** LSD1's developmental/epigenetic role is conserved; disease-specific adrenal mechanism appears human-observed. Zoonotic potential: not applicable.

---

## 15. Model Organisms

- **Cellular / in vitro models:** **H295R** human adrenocortical carcinoma cell line used to functionally validate GIPR-driven cortisol secretion and the effect of KDM1A defects (PMID 34655521, 34906447). Patient-derived adrenal tissue used for RNA-seq/methylome/IHC (PMID 34906447). iPSC/organoid adrenal models are emerging but not yet AIMAH3-specific.
- **Mouse models:** ***Kdm1a* knockout mice** are established for developmental studies (e.g., conditional Kdm1a deletion in nephron progenitors causing glomerulosclerosis/cysts, PMID 41797715; ESC studies PMID 39237615). **Complete germline Kdm1a knockout is embryonic-lethal** (LSD1 essential for embryogenesis), so no constitutive-null adult model exists; a **conditional/adrenal-specific Kdm1a knockout with somatic loss** would be required to model AIMAH3 — **not yet reported** (data/model gap).
- **Genetic model types available:** Knockout, conditional (floxed), tissue-specific Cre lines for *Kdm1a*; CRISPR/Cas9 KDM1A deletion in human organoids (PMID 41797715).
- **Phenotype recapitulation:** Existing Kdm1a models capture LSD1's epigenetic/developmental functions but **do not recapitulate the adrenal FDCS phenotype** (no ectopic GIPR / food-dependent cortisol model published). This is a key limitation and research opportunity.
- **Resources:** MGI (*Kdm1a*), IMPC/IMSR for knockout alleles; Cellosaurus (H295R, CVCL_0459).

---

## Supported vs Refuted Hypotheses

**Supported:**
- AIMAH3 (OMIM #620990) = KDM1A-driven, GIP/food-dependent Cushing syndrome (PMID 34906447, 39921449, 41864332).
- Two-hit tumor-suppressor mechanism: germline truncating KDM1A LoF + somatic 1p LOH (PMID 34906447).
- Ectopic adrenal GIPR couples meals to cortisol via cAMP/PKA (PMID 39059410, 36857084).
- Morning/midnight cortisol ratio <0.65 diagnoses FDCS with 100% sensitivity/specificity (PMID 39921449).
- Adrenalectomy definitive; somatostatin analogs only transiently effective (PMID 21264796, 23425648).
- Striking female predominance (PMID 39921449).

**Refuted / excluded for AIMAH3 specifically:**
- ARMC5 as the cause (that is AIMAH2/PBMAH1) — ARMC5 carriers do **not** have FDCS (PMID 39921449).
- 19q13.32 GIPR duplication as the mechanism — that drives **unilateral** GIP-adenomas, not bilateral AIMAH3 (PMID 36857084).
- LSD1 *inhibitors* as therapy — the lesion is LSD1 *loss*.

---

## Limitations and Future Directions

- Very small patient numbers (tens of KDM1A cases worldwide); no formal prevalence/incidence, penetrance estimates, survival, or QoL data specific to AIMAH3.
- The mechanism by which KDM1A loss de-represses *GIPR* is not fully resolved; the extreme female predominance is unexplained.
- No animal model reproduces the adrenal FDCS phenotype — an adrenal-specific conditional Kdm1a model is needed.
- GIPR antagonism is a rational but untested targeted therapy.
- Reported (limited-evidence) associations of KDM1A carriers with other tumors (e.g., monoclonal gammopathy/myeloma) warrant confirmation before inclusion in surveillance.

---

*Evidence key PMIDs:* 34906447 (Vaczlavik 2022, KDM1A discovery/multiomics), 34655521 (Chasseloup 2021, GIPR/KDM1A cohort + H295R), 39921449 (Bouys 2025, 301-case screening/genotype-phenotype), 39059410 (Bouys & Bertherat 2024, 35-year FDCS review), 36857084 (Lacroix 2023, GIP-dependent CS mechanisms), 41864332 (Chasseloup & Kamenický 2026, review), 21264796 / 23425648 (somatostatin-analog treatment), 35597729 (PBMAH epidemiology), 38152966 / 39237615 / 38321961 / 41797715 (KDM1A/LSD1 biology & models).


## Artifacts

- [OpenScientist final report](ACTH-independent_Macronodular_Adrenal_Hyperplasia_3-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](ACTH-independent_Macronodular_Adrenal_Hyperplasia_3-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.