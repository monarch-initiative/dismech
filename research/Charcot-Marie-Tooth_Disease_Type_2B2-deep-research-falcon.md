---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T11:56:22.314779'
end_time: '2026-09-08T12:05:31.181231'
duration_seconds: 548.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth disease type 2B2 (CMT2B2; OMIM 605589; ARCMT2B),
    the autosomal recessive axonal sensorimotor neuropathy mapped to 19q13.3 in a
    large consanguineous Costa Rican family and now attributed to biallelic loss-of-function
    variants in PNKP (polynucleotide kinase 3-phosphatase), specifically p.Gln517ter
    and p.Thr408del, after the earlier MED25 p.Ala335Val assignment was reassigned
    by Leal et al. 2018 (PMID 30039206) and classified DISPUTED by the ClinGen Charcot-Marie-Tooth
    Gene Curation Expert Panel; report the PNKP DNA single-strand break repair mechanism
    and its relationship to the allelic disorders AOA4 and MCSZ
  mondo_id: MONDO:0011570
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011570
    reported_labels:
    - if available
    ontology_label: Charcot-Marie-Tooth disease type 2B2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Charcot-Marie-Tooth_Disease_Type_2B2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth disease type 2B2 (CMT2B2; OMIM 605589; ARCMT2B), the autosomal recessive axonal sensorimotor neuropathy mapped to 19q13.3 in a large consanguineous Costa Rican family and now attributed to biallelic loss-of-function variants in PNKP (polynucleotide kinase 3-phosphatase), specifically p.Gln517ter and p.Thr408del, after the earlier MED25 p.Ala335Val assignment was reassigned by Leal et al. 2018 (PMID 30039206) and classified DISPUTED by the ClinGen Charcot-Marie-Tooth Gene Curation Expert Panel; report the PNKP DNA single-strand break repair mechanism and its relationship to the allelic disorders AOA4 and MCSZ
- **MONDO ID:** MONDO:0011570 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 2B2 (CMT2B2; OMIM 605589; ARCMT2B), the autosomal recessive axonal sensorimotor neuropathy mapped to 19q13.3 in a large consanguineous Costa Rican family and now attributed to biallelic loss-of-function variants in PNKP (polynucleotide kinase 3-phosphatase), specifically p.Gln517ter and p.Thr408del, after the earlier MED25 p.Ala335Val assignment was reassigned by Leal et al. 2018 (PMID 30039206) and classified DISPUTED by the ClinGen Charcot-Marie-Tooth Gene Curation Expert Panel; report the PNKP DNA single-strand break repair mechanism and its relationship to the allelic disorders AOA4 and MCSZ** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth disease type 2B2 (CMT2B2; OMIM 605589; ARCMT2B), the autosomal recessive axonal sensorimotor neuropathy mapped to 19q13.3 in a large consanguineous Costa Rican family and now attributed to biallelic loss-of-function variants in PNKP (polynucleotide kinase 3-phosphatase), specifically p.Gln517ter and p.Thr408del, after the earlier MED25 p.Ala335Val assignment was reassigned by Leal et al. 2018 (PMID 30039206) and classified DISPUTED by the ClinGen Charcot-Marie-Tooth Gene Curation Expert Panel; report the PNKP DNA single-strand break repair mechanism and its relationship to the allelic disorders AOA4 and MCSZ
- **MONDO ID:** MONDO:0011570 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 2B2 (CMT2B2; OMIM 605589; ARCMT2B), the autosomal recessive axonal sensorimotor neuropathy mapped to 19q13.3 in a large consanguineous Costa Rican family and now attributed to biallelic loss-of-function variants in PNKP (polynucleotide kinase 3-phosphatase), specifically p.Gln517ter and p.Thr408del, after the earlier MED25 p.Ala335Val assignment was reassigned by Leal et al. 2018 (PMID 30039206) and classified DISPUTED by the ClinGen Charcot-Marie-Tooth Gene Curation Expert Panel; report the PNKP DNA single-strand break repair mechanism and its relationship to the allelic disorders AOA4 and MCSZ** covering all of the
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


# Charcot–Marie–Tooth Disease Type 2B2 Due to Biallelic *PNKP*: Disease-Characteristics Report

## Executive summary and curation conclusion

Charcot–Marie–Tooth disease type 2B2 (CMT2B2; ARCMT2B; OMIM 605589) is an exceptionally rare, autosomal-recessive, predominantly axonal sensorimotor neuropathy with variably associated cerebellar and oculomotor dysfunction. The definitive disease-specific evidence comes primarily from a large consanguineous Costa Rican family and five additional Costa Rican subjects. The original assignment to homozygous *MED25* p.Ala335Val should be retained only as historical: reanalysis identified homozygous *PNKP* c.1549C>T (p.Gln517Ter) in the extended family and compound-heterozygous p.Gln517Ter/p.Thr408del in the five additional cases. These data support *PNKP*, not *MED25*, as the causal gene; the ClinGen CMT Gene Curation Expert Panel’s disputed classification of the *MED25*–CMT relationship is therefore concordant with the primary evidence. The principal paper was published online July 24, 2018 (PMID 30039206; DOI [10.1007/s10048-018-0555-7](https://doi.org/10.1007/s10048-018-0555-7)). (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

The defining clinical course is adult onset—approximately 28–42 years in the original family—followed by slowly progressive distal weakness and wasting, sensory loss, areflexia, gait impairment, and severe axonal sensorimotor abnormalities on nerve-conduction studies. Dysarthria, gait ataxia, oculomotor abnormalities, and mild cerebellar atrophy can accompany the neuropathy. Unlike severe *PNKP*-related microcephaly, seizures, and developmental delay (MCSZ), the reported CMT2B2 subjects did not have congenital microcephaly, seizures, or developmental delay. CMT2B2 is best curated as the adult-onset, neuropathy-predominant end of a continuous *PNKP*-related spectrum that also includes ataxia with oculomotor apraxia type 4 (AOA4) and MCSZ. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, gatti2019fromcongenitalmicrocephaly pages 1-2)

| Entity/domain | Curated finding | Evidence type/strength | Ontology/database annotation |
|---|---|---|---|
| Disease identity | Charcot-Marie-Tooth disease type 2B2 (CMT2B2; ARCMT2B) is a very rare autosomal-recessive, predominantly axonal sensorimotor neuropathy with mild cerebellar/oculomotor involvement in the reported Costa Rican cases. | Strong for the reported kindreds; limited generalizability because evidence derives from one extended family and five additional Costa Rican subjects (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6) | OMIM: **605589**; MONDO: **MONDO:0011570** supplied by requester—verify against the current MONDO release before ingestion; candidate class: hereditary motor and sensory neuropathy |
| Gene attribution | The best-supported cause is **biallelic PNKP loss-of-function/hypomorphic variation**. The earlier **MED25 p.Ala335Val** attribution was superseded after reanalysis found segregating biallelic PNKP variants; MED25–CMT2B2 validity is classified **Disputed** by the ClinGen CMT Gene Curation Expert Panel. | Strong human segregation/reanalysis evidence for PNKP; contradictory/insufficient evidence for MED25 (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8) | PNKP; candidate relationship: biallelic loss of function → CMT2B2. MED25 should be retained only as a historical/disputed attribution |
| Homozygous genotype | The large consanguineous Costa Rican family carried **PNKP c.1549C>T (p.Gln517Ter; p.Gln517\*) homozygously**. The premature stop lies in the last exon and truncates the conserved C-terminal region. | Strong segregation evidence in the discovery pedigree; pathogenicity supported by predicted structural destabilization, although direct allele-specific functional testing is limited (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8) | Variant class: germline nonsense; candidate ACMG concepts: PVS1/segregation/phenotype specificity, subject to transcript-specific curation |
| Compound-heterozygous genotype | Five unrelated Costa Rican CMT2 subjects were reported with **PNKP c.1549C>T (p.Gln517Ter)** in trans with **c.1221_1223del (p.Thr408del)**. | Strong case-level and segregation evidence across five additional subjects; p.Thr408del had also been associated with recessive ataxia (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 4-6) | Variant classes: germline nonsense plus in-frame deletion; verify HGVS against the designated clinical transcript before database loading |
| Peripheral neuropathy phenotype | Adult-onset, slowly progressive, length-dependent **axonal sensorimotor polyneuropathy** produced gait disturbance, falls, distal weakness and wasting, impaired/absent reflexes, and marked vibration/position-sense loss. Onset in the original family was approximately **28–42 years**; additional cases generally began in the third decade. | Strong but small human case-series evidence; severe disability was variable, including wheelchair dependence in one subject after five years (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6) | Candidate HPO: adult onset; progressive peripheral neuropathy; axonal sensorimotor polyneuropathy; distal muscle weakness/atrophy; areflexia; impaired proprioception; gait disturbance |
| Electrophysiology | Nerve-conduction studies showed markedly reduced or absent sensory responses and reduced compound muscle action potentials, with secondary slowing of motor conduction in severe axonal disease. | Strong objective clinical evidence in reported patients (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6) | Candidate HPO: abnormal peripheral nerve conduction; reduced CMAP amplitude; absent sensory nerve action potentials; axonal degeneration |
| Cerebellar and oculomotor signs | Slurred speech/dysarthria, wide-based or ataxic gait, postural instability, and variable oculomotor abnormalities—including oculomotor apraxia in some subjects—accompanied the neuropathy. MRI could show mild cerebellar atrophy without brainstem or white-matter abnormalities. | Moderate-to-strong case-series evidence; expression was variable (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6) | Candidate HPO: cerebellar ataxia; dysarthria; oculomotor apraxia; abnormality of ocular movements; cerebellar atrophy |
| Features absent in reported CMT2B2 cohort | The Costa Rican CMT2B2 subjects lacked congenital microcephaly, seizures, developmental delay, cognitive impairment, and dystonia, distinguishing their presentation from classic MCSZ. | Strong for examined subjects, but absence cannot be generalized to every future PNKP-neuropathy case (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 4-6) | Negated candidate HPO: microcephaly; seizure; global developmental delay; cognitive impairment; dystonia |
| PNKP protein function | PNKP is a DNA-end-processing enzyme with an N-terminal FHA interaction domain and catalytic **3′-phosphatase** and **5′-kinase** activities. It converts obstructive termini into ligatable **3′-OH/5′-phosphate** ends. | Strong biochemical, structural, and cellular evidence (weinfeld2011tidyinguploose pages 5-7, weinfeld2011tidyinguploose pages 4-5, dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2) | Candidate GO: DNA 3′-phosphatase activity; polynucleotide 5′-hydroxyl-kinase activity; DNA repair; DNA single-strand-break repair; nonhomologous end joining |
| Single-strand-break repair mechanism | Oxidative or TOP1-associated damage generates noncanonical DNA ends. PARP1/PARP2 and the XRCC1 scaffold organize repair; PNKP processes 3′-phosphate and 5′-OH termini, POLB fills gaps, and LIG3 seals the strand. XRCC1 interaction stimulates PNKP recruitment and catalytic turnover. | Strong pathway-level biochemical/cellular evidence; exact recruitment order may vary by lesion and remains partly unresolved (weinfeld2011tidyinguploose pages 4-5, hulmakova2025theroleof pages 20-23, dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2) | Candidate GO: base-excision repair; DNA single-strand-break repair; response to oxidative stress. Candidate compartments: nucleus, chromatin, DNA-repair complex |
| Downstream pathophysiology | Reduced PNKP function is expected to cause persistent strand-break termini, impaired repair, transcriptional/genomic stress, and preferential dysfunction or loss of long-lived peripheral and cerebellar neurons. The final link from the two Costa Rican alleles to selective axonal degeneration remains **inferred**, not directly demonstrated in patient neurons. | Strong general PNKP/DNA-repair evidence but moderate, inferential disease-specific chain (leal2018thepolynucleotidekinase pages 6-8, jiang2022mutationsofthe pages 13-13, dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2) | Candidate GO: cellular response to DNA damage stimulus; maintenance of genome stability; neuron death. Candidate CL: peripheral sensory neuron, lower motor neuron, cerebellar Purkinje cell |
| Allelic relationship to AOA4 | **AOA4 (OMIM 616267)** is another biallelic PNKP disorder, typically emphasizing progressive cerebellar ataxia, oculomotor apraxia, and axonal polyneuropathy. CMT2B2 occupies the neuropathy-predominant, adult-onset end of an overlapping spectrum. | Strong human allelic-spectrum evidence; strict genotype–phenotype boundaries are not established (leal2018thepolynucleotidekinase pages 1-2, gatti2019fromcongenitalmicrocephaly pages 1-2, garrelfs2020eurresearchinformation pages 1-3) | Candidate disease relationship: allelic disorder; candidate HPO: cerebellar ataxia, oculomotor apraxia, axonal neuropathy |
| Allelic relationship to MCSZ | **MCSZ (OMIM 613402)** usually presents with congenital microcephaly, early seizures, developmental delay, and progressive cerebellar atrophy; later neuropathy/ataxia may occur. Published cohorts support a continuum from severe neurodevelopmental disease to adult neurodegeneration. | Strong human evidence for a phenotypic continuum; simple residual-activity rules remain incomplete (gatti2019fromcongenitalmicrocephaly pages 1-2, gatti2019fromcongenitalmicrocephaly pages 2-3, garrelfs2020eurresearchinformation pages 1-3) | Candidate disease relationship: allelic disorder; candidate HPO: congenital microcephaly, early-onset seizure, global developmental delay, cerebellar atrophy |
| Diagnostics | Diagnosis requires neurological examination, nerve-conduction studies/EMG, assessment for ataxia and eye-movement abnormalities, brain MRI when central signs are present, and molecular confirmation of **biallelic PNKP variants** by neuropathy/ataxia panel, exome, or genome sequencing with segregation analysis. | Clinically well supported, but no CMT2B2-specific consensus criteria or validated biochemical diagnostic assay exist (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6) | Candidate NCIT interventions: genetic testing, whole-exome sequencing, whole-genome sequencing, electromyography, nerve-conduction study, magnetic-resonance imaging |
| Treatment status | No approved disease-modifying, gene, RNA, or PNKP-replacement therapy and no relevant CMT2B2-specific interventional trial were identified. Current care is supportive: physical/occupational therapy, orthoses and mobility aids, fall prevention, pain management, speech support, and orthopedic evaluation for deformity. | Supportive practice extrapolated from general CMT/ataxia management; no CMT2B2 treatment-response rates | Candidate NCIT interventions: physical therapy, occupational therapy, orthotic device, assistive device, pain management, speech therapy, orthopedic surgery |
| Epidemiology and evidence gaps | Disease-specific prevalence, incidence, carrier frequency, sex ratio, penetrance, life expectancy, quantitative natural history, modifiers, protective factors, pharmacogenomics, biomarkers, and quality-of-life statistics are unavailable. No exact p.Gln517Ter/p.Thr408del neuronal model or disease-specific single-cell, spatial, or multi-omics dataset was identified. | Major limitation: extremely small, geographically concentrated ascertainment; broader PNKP cohorts cannot substitute for CMT2B2-specific estimates (leal2018thepolynucleotidekinase pages 1-2, gatti2019fromcongenitalmicrocephaly pages 1-2, garrelfs2020eurresearchinformation pages 1-3, hulmakova2025theroleof pages 32-35) | Mark as unknown/not established; avoid assigning population frequencies or phenotype percentages beyond the published cohort |


*Table: Compact knowledge-base table distinguishing PNKP-related CMT2B2 from the disputed MED25 attribution and summarizing its variants, phenotype, mechanism, allelic spectrum, diagnostics, treatment status, and evidence gaps.*

## 1. Disease information

### Definition

CMT2B2 is a hereditary motor and sensory neuropathy in which axonal loss, rather than primary demyelination, is the predominant peripheral-nerve lesion. Its distinctive syndromic extension is mild or variable cerebellar and oculomotor dysfunction. The label “CMT2B2” is historically locus- and pedigree-based; molecularly, the condition is a *PNKP*-related DNA-strand-break-repair disorder. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8)

### Identifiers and synonyms

- **OMIM:** 605589, CMT2B2.
- **MONDO:** MONDO:0011570 was supplied in the request; this mapping should be checked against the current MONDO release before production ingestion.
- **Synonyms:** Charcot–Marie–Tooth disease type 2B2; CMT2B2; autosomal-recessive CMT type 2B; ARCMT2B; hereditary motor and sensory neuropathy, axonal, type 2B2; *PNKP*-related neuropathy-predominant disorder.
- **Related but not synonymous:** AOA4, OMIM 616267; MCSZ, OMIM 613402.
- **ICD:** There is no established subtype-specific ICD-10/ICD-11 code. A broader hereditary motor and sensory neuropathy/Charcot–Marie–Tooth code must be used, with the molecular diagnosis recorded separately.
- **MeSH/SNOMED CT:** Use the broader Charcot–Marie–Tooth disease or hereditary motor and sensory neuropathy concept plus *PNKP* and autosomal-recessive inheritance annotations.

This report summarizes aggregated disease-level evidence from published pedigrees and mechanistic experiments. It is not derived from an EHR or an individual clinical record.

### Historical reassignment and authoritative interpretation

The original 19q13.3 locus was mapped in a large consanguineous Costa Rican family with autosomal-recessive axonal neuropathy, and homozygous *MED25* p.Ala335Val was initially proposed as causal. Because no convincing independent *MED25* CMT cases emerged, Leal and colleagues re-examined the family by exome sequencing. Their abstract states: “Using exome sequencing, we now identified a homozygous nonsense variant (p.Gln517ter) in the last exon of an adjacent gene, the polynucleotide kinase 3′-phosphatase (PNKP) gene.” Five additional subjects carrying one copy of the *MED25* allele instead proved to have two *PNKP* alleles. This independent-genotype logic strongly favors *PNKP* and undermines *MED25* causality. (leal2018thepolynucleotidekinase pages 1-2)

## 2. Etiology

### Causal factors

The primary cause is **germline biallelic damaging variation in *PNKP***. In the extended family, p.Gln517Ter was homozygous; in five additional cases, p.Gln517Ter occurred in trans with the in-frame deletion p.Thr408del. Both genotypes are consistent with partial loss of PNKP function. The disease is not infectious, toxic, immune-mediated, or environmentally acquired. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 4-6)

### Genetic risk

Having two pathogenic or likely pathogenic *PNKP* alleles is the necessary established risk factor. Consanguinity increased the probability of homozygosity in the original family. A first-degree family history compatible with recessive inheritance raises diagnostic probability, but absence of such history does not exclude compound heterozygosity. The *MED25* p.Ala335Val allele is not an independently supported risk factor for CMT2B2 and should not be used for predictive testing by itself. (leal2018thepolynucleotidekinase pages 1-2)

Variant nomenclature should be transcript-verified before clinical loading because historical papers may use differing transcript conventions. The reported forms are:

- *PNKP* c.1549C>T, p.Gln517Ter/p.Gln517* — nonsense, last exon.
- *PNKP* c.1221_1223del, p.Thr408del — in-frame three-base deletion.

Population frequencies, Costa Rican carrier frequencies, and ancestry-stratified frequencies were not established in the retrieved disease-specific literature. No modifier gene, protective allele, epigenetic risk state, or reproducible susceptibility locus has been demonstrated.

### Environmental, protective, and gene–environment factors

No environmental exposure has been shown to cause or protect against CMT2B2. Because reactive oxygen species generate substrates repaired by PNKP, oxidative burden is mechanistically relevant, but no human study shows that smoking, diet, occupation, radiation, alcohol, or exercise modifies penetrance or progression. Avoidance of neurotoxic medications and excessive alcohol is prudent in hereditary neuropathy care, but it is tertiary risk reduction rather than proven CMT2B2-specific prevention. The same distinction applies to exercise: appropriately dosed activity may preserve function, but it does not correct PNKP deficiency.

## 3. Phenotypes

### Core peripheral phenotype

The original family had onset at approximately 28–42 years; additional subjects generally developed polyneuropathy in the third decade. Initial manifestations included gait disturbance, falls, and postural instability. Progression produced distal weakness and atrophy in feet, calves, and hands; absent or impaired tendon reflexes; severe loss of vibration and position sense; claw hands; and, in some cases, pes cavus or hammertoes. Nerve-conduction studies showed absent or markedly reduced sensory responses and low or absent compound muscle action potentials. Modest motor-conduction slowing was interpreted as secondary to severe axonal loss rather than evidence of a primary demyelinating neuropathy. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

Suggested HPO concepts include adult onset, progressive peripheral neuropathy, axonal sensorimotor polyneuropathy, distal muscle weakness, distal muscle atrophy, areflexia, impaired proprioception, reduced vibration sense, gait disturbance, pes cavus, hammertoes, claw hand, reduced CMAP amplitude, and absent sensory nerve action potentials.

### Cerebellar and oculomotor phenotype

Slurred speech/dysarthria was prominent in the additionally characterized cases. Wide-based or mildly ataxic gait, cerebellar dysfunction, and variable oculomotor abnormalities were reported; two listed subjects had oculomotor apraxia. MRI could show mild cerebellar atrophy without brainstem or cerebral white-matter abnormalities. Candidate HPO concepts are cerebellar ataxia, dysarthria, oculomotor apraxia, abnormal ocular movement, postural instability, and cerebellar atrophy. (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

### Severity, progression, and frequency limitations

Expression was variable. One additional subject became wheelchair-dependent after five years, while another remained ambulatory with mild gait ataxia. Frequencies calculated from this tiny, ascertained series would not be valid population estimates. Accordingly, findings such as dysarthria “in all listed additional cases” should be stored as case-series observations, not universal penetrance. (leal2018thepolynucleotidekinase pages 4-6)

### Negated and overlapping features

The Costa Rican CMT2B2 patients lacked microcephaly, seizures, developmental delay, cognitive impairment, and dystonia. These are important **negated phenotypes** for the reported cohort, not absolute exclusion criteria for every future neuropathy-predominant *PNKP* case. Broader *PNKP* cohorts demonstrate overlap: early MCSZ can later acquire neuropathy and ataxia, and adult disease can emphasize polyneuropathy and cerebellar signs. (leal2018thepolynucleotidekinase pages 1-2, gatti2019fromcongenitalmicrocephaly pages 1-2, gatti2019fromcongenitalmicrocephaly pages 2-3)

### Quality of life

No CMT2B2-specific EQ-5D, SF-36, PROMIS, CMT Health Index, or disease-burden study was identified. Nevertheless, the documented falls, hand and foot weakness, sensory loss, speech impairment, orthopedic deformity, and wheelchair dependence indicate substantial effects on mobility, activities of daily living, communication, and independence. Quantitative utility values should be marked unavailable.

## 4. Genetic and molecular information

### Causal gene and protein

*PNKP* encodes polynucleotide kinase 3′-phosphatase, a bifunctional DNA-end-processing enzyme. It contains an N-terminal forkhead-associated interaction domain and catalytic phosphatase and kinase regions. PNKP operates in XRCC1-associated single-strand-break/base-excision repair and XRCC4–LIG4-associated nonhomologous end joining. (weinfeld2011tidyinguploose pages 5-7, weinfeld2011tidyinguploose pages 4-5, dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2)

### Variant interpretation

The reported variants are constitutional/germline, not somatic. p.Gln517Ter truncates a conserved C-terminal region. Structural modeling in the disease report predicted disruption of kinase/phosphatase-domain orientation and the ADP-binding region, providing a plausible reduction-of-function mechanism. p.Thr408del is an in-frame deletion previously observed in recessive ataxia and contributes to disease when paired with p.Gln517Ter. (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

For clinical curation, classification should be performed independently under current ACMG/AMP specifications using the laboratory’s selected transcript, validated population frequency, segregation, phase, and any available functional evidence. “Pathogenic” should not be inferred solely from this report’s wording without that transcript-level review.

### Other molecular categories

No reproducible CMT2B2 modifier genes, methylation signature, chromatin biomarker, large structural rearrangement, somatic mosaicism, or germline mosaicism have been reported. The disease does not involve aneuploidy, repeat expansion, mitochondrial-genome variation, or a recurrent cytogenetic rearrangement. PNKP may participate in mitochondrial DNA repair, but a CMT2B2-specific mitochondrial molecular signature has not been established. (gatti2019fromcongenitalmicrocephaly pages 1-2, hulmakova2025theroleof pages 32-35)

## 5. Environmental information

No toxin, pollutant, radiation exposure, occupation, diet, infection, smoking behavior, or alcohol exposure has been causally associated with CMT2B2. Reactive oxygen species and ionizing radiation generate DNA termini that PNKP normally processes, establishing biochemical substrate relevance—not a demonstrated epidemiologic exposure effect. There is no zoonotic or transmissible agent.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic p.Gln517Ter or p.Gln517Ter/p.Thr408del variation leads to reduced or structurally impaired PNKP function.** Variant-specific structural impairment is supported by modeling; exact residual activity in patient neurons remains incompletely measured. (leal2018thepolynucleotidekinase pages 6-8)
2. **Reduced PNKP leads to inefficient conversion of obstructive DNA 3′-phosphate and 5′-hydroxyl termini into ligatable 3′-OH and 5′-phosphate ends.** This end-processing function is demonstrated biochemically for PNKP. (weinfeld2011tidyinguploose pages 5-7, weinfeld2011tidyinguploose pages 4-5)
3. **Defective end processing leads to delayed single-strand-break/base-excision repair and, potentially, selected double-strand-break repair by NHEJ.** Patient fibroblast literature more consistently demonstrates SSBR impairment; the extent of DSBR impairment varies by allele and assay. (hulmakova2025theroleof pages 32-35, jiang2022mutationsofthe pages 13-13)
4. **Persistent strand-break intermediates lead to transcriptional obstruction, PARP-related stress, genome instability, or cell dysfunction.** These consequences are supported across PNKP and related strand-break-repair models but are not fully demonstrated in CMT2B2 patient axons. (jiang2022mutationsofthe pages 12-13, dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2)
5. **Accumulated DNA-repair stress is inferred to preferentially injure long-lived, metabolically active peripheral neurons and cerebellar circuits.** Neuronal susceptibility is biologically supported by high oxidative metabolism, longevity, and transcriptional activity; selective involvement of particular axons remains unresolved. (dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2)
6. **Peripheral axonal dysfunction and degeneration lead to reduced CMAP/SNAP amplitudes, distal weakness, atrophy, sensory loss, and areflexia.** This clinicophysiologic link is demonstrated in the human cohort. (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)
7. **A parallel cerebellar/oculomotor branch leads to dysarthria, gait ataxia, oculomotor abnormalities, and mild cerebellar atrophy.** The clinical branch is demonstrated; its cellular mechanism is inferred from general PNKP neurobiology. (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

### Single-strand-break repair in detail

Oxidative damage, base-excision intermediates, and trapped topoisomerase-I lesions can leave 3′-phosphate, 3′-phosphoglycolate, or 5′-OH termini that cannot be directly ligated. PARP1 or PARP2 senses damaged chromatin and promotes recruitment of XRCC1. XRCC1 acts as a scaffold for PNKP, DNA polymerase β, and DNA ligase III. PNKP removes 3′ phosphate and phosphorylates 5′ hydroxyl; polymerase fills the gap and LIG3 seals the strand. XRCC1 can stimulate PNKP turnover by displacing it from processed products. Evidence also supports lesion-dependent alternative recruitment orders in which PNKP or APE1 engages an end before stable XRCC1 accumulation; neither model should be treated as universally exclusive. (weinfeld2011tidyinguploose pages 4-5, hulmakova2025theroleof pages 20-23)

A concise functional quotation from the mechanistic literature is that PNKP participates in both “XRCC1-based single-strand break/base-excision repair” and NHEJ. The neurologic relevance arises because unrepaired oxidative SSBs can block transcription in nondividing neurons. (dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2)

### Double-strand-break repair

In NHEJ, PNKP binds the CK2-phosphorylated XRCC4 tail through its FHA domain, processes abnormal DNA ends, and facilitates subsequent ligation by DNA ligase IV. PNKP kinase activity supplies 5′ phosphate, while its phosphatase activity can remove 3′ phosphate. However, lack of immunodeficiency in most *PNKP*-affected people implies that V(D)J-associated end joining is sufficiently preserved by residual function or redundant processing. This helps explain why *PNKP* disease is neurologically prominent rather than a classic radiosensitive immunodeficiency. (hulmakova2025theroleof pages 32-35, weinfeld2011tidyinguploose pages 5-7)

### Allelic spectrum: CMT2B2, AOA4, and MCSZ

- **CMT2B2:** adult-onset, neuropathy-predominant; slowly progressive axonal sensorimotor neuropathy with mild/variable ataxia, dysarthria, oculomotor signs, and cerebellar atrophy; no microcephaly, seizures, or developmental delay in the Costa Rican cohort. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8)
- **AOA4:** generally childhood-to-young-adult progressive cerebellar ataxia with oculomotor apraxia and axonal polyneuropathy. It is a neurodegenerative *PNKP* phenotype rather than a wholly separate pathway.
- **MCSZ:** typically congenital microcephaly, early often intractable seizures, developmental delay, and progressive cerebellar atrophy; neuropathy and ataxia may appear later. More than 40 affected individuals had been summarized by 2019, supporting a continuum from congenital neurodevelopmental disease to adult-onset neurodegeneration. (gatti2019fromcongenitalmicrocephaly pages 1-2, gatti2019fromcongenitalmicrocephaly pages 2-3)

The 2018 authors explicitly concluded that the Costa Rican presentation represented a milder “allelic effect.” Current evidence supports a residual-function continuum but not a deterministic rule linking one domain or activity to one phenotype. The same or nearby alleles can occur across overlapping syndromes; genetic background and unknown modifiers probably contribute. (leal2018thepolynucleotidekinase pages 1-2, gatti2019fromcongenitalmicrocephaly pages 1-2, hulmakova2025theroleof pages 32-35)

### Molecular profiling and recent developments

No CMT2B2-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or integrated multi-omics dataset was identified. Recent work has nevertheless refined the wider PNKP field:

- A 2023 functional study of an AOA4 mutation linked defective DNA-end processing and oxidative-damage responses to neurodegeneration, strengthening the residual-function model, although it did not study the Costa Rican alleles directly.
- A 2024 MCSZ study reported novel variants associated with reduced SSBR, providing contemporary functional confirmation that impaired PNKP repair remains central to the allelic spectrum.
- A 2024 study identified cell-cycle-dependent regulation of PNKP in DNA replication and Okazaki-fragment maturation, expanding PNKP biology beyond canonical strand-break repair; relevance to adult peripheral axons is presently uncertain. (hulmakova2025theroleof pages 32-35, hulmakova2025theroleof pages 38-41)

Suggested GO terms include DNA 3′-phosphatase activity, polynucleotide 5′-hydroxyl-kinase activity, DNA single-strand-break repair, base-excision repair, nonhomologous end joining, cellular response to oxidative stress, DNA-damage response, and maintenance of genome stability. Suggested cell types are peripheral sensory neuron, lower motor neuron, cerebellar Purkinje cell, and Schwann cell; neuronal involvement is primary, whereas a primary Schwann-cell defect is not demonstrated.

## 7. Anatomical structures affected

The primary system is the peripheral nervous system, particularly long motor and sensory axons of distal limbs. Secondary structures include distal skeletal muscle, which undergoes neurogenic wasting, and feet/hands, which develop imbalance-related deformity. Cerebellar and oculomotor pathways are variably involved. Findings are usually bilateral and length-dependent rather than focal or unilateral. (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

Candidate anatomical annotations include peripheral nerve, spinal nerve, motor neuron axon, sensory neuron axon, skeletal muscle of limb, hand, foot, cerebellum, and ocular motor system. Candidate UBERON concepts should be identifier-validated locally. At the subcellular level, relevant compartments are nucleus, chromatin, DNA-repair complex, and possibly mitochondrion; only the nuclear strand-break-repair role is firmly linked to CMT2B2.

## 8. Temporal development

CMT2B2 onset is chronic and insidious, usually in adulthood in the known Costa Rican cases. Early disease consists of gait disturbance, falls, and distal sensorimotor symptoms. Intermediate disease adds progressive weakness, wasting, proprioceptive loss, dysarthria, and ataxia. Advanced disease may require a wheelchair, although progression is variable. No episodic attacks, relapses, or spontaneous remissions were reported. The disorder is lifelong and progressive. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

There is no validated staging system, annualized progression rate, or proven therapeutic window. Earlier identification is nevertheless clinically useful before fixed contractures, recurrent falls, or severe deconditioning emerge.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele. Both sexes are expected to be affected equally. Anticipation is not expected. Penetrance appears high among reported biallelic adults, but the denominator is too small and ascertained to claim complete penetrance. Expressivity is variable. (leal2018thepolynucleotidekinase pages 1-2, leal2018thepolynucleotidekinase pages 4-6)

Consanguinity was central to discovery of the homozygous extended family. The recurrence of p.Gln517Ter and p.Thr408del among Costa Rican cases suggests population enrichment or shared ancestry, but formal haplotype/founder analysis and carrier-frequency data are unavailable. No prevalence per 100,000, incidence, sex ratio, or global geographic distribution can be calculated. The known disease-specific evidence is geographically concentrated in Costa Rica; broader *PNKP* disease has been reported internationally, but it cannot be used as CMT2B2 epidemiology.

## 10. Diagnostics

### Clinical and electrophysiologic assessment

Evaluation should include detailed pedigree and consanguinity history; neurologic examination of distal power, atrophy, reflexes, proprioception, gait, speech, cerebellar function, and eye movements; and nerve-conduction studies/EMG. The expected electrophysiologic pattern is severe axonal sensorimotor polyneuropathy with low or absent SNAPs and CMAPs. Brain MRI is indicated when ataxia, dysarthria, or oculomotor findings are present and may show mild cerebellar atrophy. (leal2018thepolynucleotidekinase pages 6-8, leal2018thepolynucleotidekinase pages 4-6)

Serum alpha-fetoprotein, albumin, and cholesterol may be abnormal elsewhere in the *PNKP* spectrum, particularly AOA4/MCSZ, but no laboratory analyte is a validated CMT2B2 biomarker. A broader nine-patient PNKP cohort found increasing alpha-fetoprotein and progressive cerebellar atrophy across the spectrum; these findings should be considered supportive, not subtype-defining. (garrelfs2020eurresearchinformation pages 1-3)

### Genetic-testing strategy

1. Use a hereditary neuropathy panel that includes *PNKP* and genes for axonal CMT, or a combined neuropathy/ataxia panel when cerebellar signs are present.
2. If negative or the phenotype is atypical, perform trio/family WES or WGS. Exome reanalysis was decisive in correcting the original CMT2B2 assignment. (leal2018thepolynucleotidekinase pages 1-2)
3. Confirm candidate variants by an orthogonal method where required, establish phase and segregation, and review copy-number calling because a sequence-only assay may miss exon-level deletions.
4. Do not diagnose CMT2B2 from *MED25* p.Ala335Val alone.

Single-gene *PNKP* testing is efficient when the familial variants are known. CMA, karyotype, FISH, mitochondrial DNA analysis, and repeat-expansion testing are not first-line for a classic familial case, although they may be used in unresolved differential diagnosis. RNA sequencing may clarify a suspected splice variant but is not a routine validated CMT2B2 assay.

### Differential diagnosis

Important alternatives include other axonal CMT genes; AOA1/APTX, AOA2/SETX, and AOA4/*PNKP*; spinocerebellar ataxia with axonal neuropathy; Friedreich ataxia; POLG-related disease; RFC1 biallelic expansion disease; mitochondrial neuropathies; and acquired toxic, metabolic, inflammatory, or nutritional neuropathy. Adult neuropathy plus dysarthria/oculomotor findings and recessive inheritance should elevate *PNKP*.

### Screening

Population and newborn screening are not indicated because prevalence, carrier frequency, and early intervention benefit are unknown. Cascade testing of adult relatives and targeted carrier testing of reproductive partners are appropriate after molecular confirmation.

## 11. Outcomes and prognosis

No disease-specific survival curve, mortality rate, life-expectancy estimate, or 5-/10-year outcome is available. The principal morbidity is progressive motor and sensory disability, falls, deformity, loss of ambulation, and communication difficulty. At least one patient became wheelchair-dependent rapidly, whereas another retained mobility with mild ataxia, demonstrating substantial prognostic variability. (leal2018thepolynucleotidekinase pages 4-6)

Respiratory failure, cardiomyopathy, immunodeficiency, and systemic organ failure are not established defining complications. A broader PNKP cohort found no consistent immunodeficiency or cancer predisposition; isolated malignancies should not be interpreted as a proven syndrome-level risk. (garrelfs2020eurresearchinformation pages 1-3)

No validated prognostic biomarker exists. Baseline motor function, rate of decline, electrophysiologic axonal loss, falls, contractures, and cerebellar involvement are reasonable clinical monitoring variables but not validated prediction models.

## 12. Treatment

There is no approved disease-modifying therapy, PNKP replacement, gene therapy, RNA therapy, or genome-editing treatment for CMT2B2. No relevant disease-specific interventional trial was identified in the ClinicalTrials.gov search; therefore, response rates and molecular-treatment adverse-event data do not exist.

Current real-world management is multidisciplinary and supportive:

- physical therapy, stretching, balance and gait training, and individualized low-to-moderate intensity conditioning;
- occupational therapy and adaptive strategies for hand weakness;
- ankle–foot orthoses, custom footwear, canes, walkers, or wheelchairs;
- fall prevention and home-safety assessment;
- orthopedic review for progressive cavovarus deformity, contracture, or tendon imbalance, with surgery considered individually;
- standard neuropathic-pain treatment where needed;
- speech-language therapy for dysarthria and swallowing assessment if symptoms emerge;
- neurologic surveillance for ataxia, eye-movement dysfunction, and functional decline.

Candidate NCIT intervention concepts are physical therapy, occupational therapy, orthotic device, assistive device, exercise therapy, pain management, speech therapy, genetic counseling, and orthopedic surgery. These interventions may preserve independence or address complications, but there are no CMT2B2-specific controlled outcome estimates.

## 13. Prevention

Primary prevention through lifestyle or vaccination is not applicable to a Mendelian recessive disorder. Reproductive prevention options include genetic counseling, carrier testing of relatives and partners, prenatal diagnosis, and preimplantation genetic testing for a known familial genotype. Secondary prevention consists of molecular diagnosis before substantial disability and anticipatory assessment of gait, falls, deformity, and cerebellar symptoms. Tertiary prevention includes orthoses, exercise, contracture prevention, safe mobility, pain treatment, and avoidance of unnecessary neurotoxic exposure. There is no prophylactic drug.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disease equivalent to human p.Gln517Ter/p.Thr408del CMT2B2 was identified. There is no breed association, zoonotic potential, transmission, or cross-species infectious susceptibility. PNKP orthologs and DNA-end-processing functions are evolutionarily conserved, which supports comparative modeling, but database-specific NCBI Gene, Taxon, and VBO identifiers should be verified before knowledge-base insertion.

## 15. Model organisms and experimental systems

Complete PNKP loss is embryonically lethal in mice. Conditional neural deletion demonstrated that PNKP is required for neurogenesis and genome stability through multiple DNA-repair pathways, strongly supporting nervous-system dependence on PNKP. These models reproduce severe neurodevelopmental consequences more closely than adult-onset CMT2B2 and should not be described as exact CMT2B2 models. (hulmakova2025theroleof pages 32-35, jiang2022mutationsofthe pages 13-13)

Cellular systems include PNKP-deficient or complemented human cell lines, patient fibroblasts, DNA-end-processing assays, clonogenic genotoxic-sensitivity assays, and structural/biochemical reconstitution. These demonstrate impaired repair, persistent abnormal ends, and sensitivity to oxidative, radiomimetic, or topoisomerase-associated damage. Their limitations are the absence of long axons, neuron–glia interactions, and organismal aging. (weinfeld2011tidyinguploose pages 4-5, jiang2022mutationsofthe pages 13-13, jiang2022mutationsofthe pages 12-13)

No validated knock-in mouse, zebrafish, Drosophila, organoid, or patient-derived motor/sensory-neuron model carrying exactly p.Gln517Ter alone or p.Gln517Ter/p.Thr408del was identified in the evidence reviewed through 2024. Developing isogenic iPSC-derived peripheral sensory and motor neurons with these genotypes is a high-priority research need.

## Evidence quality and knowledge gaps

The *PNKP* reassignment is convincing because it integrates exome discovery, recessive segregation, two genotypic configurations, multiple subjects, biological plausibility, and a coherent allelic spectrum. However, nearly every quantitative disease-characteristic field remains limited by the small, geographically concentrated cohort. Prevalence, penetrance, carrier frequency, longitudinal progression, survival, quality-of-life scores, biomarkers, modifiers, treatment outcomes, and environmental interactions are unknown. Mechanistic evidence is strong for PNKP generally but only partly allele- and cell-type-specific for CMT2B2. Thus, the knowledge-base entry should clearly separate **demonstrated human CMT2B2 observations**, **broader human PNKP-spectrum evidence**, **experimental PNKP mechanism**, and **inferred selective axonal pathophysiology**.

References

1. (leal2018thepolynucleotidekinase pages 1-2): Alejandro Leal, Sixto Bogantes-Ledezma, Arif B. Ekici, Steffen Uebe, Christian T. Thiel, Heinrich Sticht, Martin Berghoff, Corinna Berghoff, Bernal Morera, Michael Meisterernst, and André Reis. The polynucleotide kinase 3′-phosphatase gene (pnkp) is involved in charcot-marie-tooth disease (cmt2b2) previously related to med25. Neurogenetics, 19:215-225, Jul 2018. URL: https://doi.org/10.1007/s10048-018-0555-7, doi:10.1007/s10048-018-0555-7. This article has 51 citations and is from a peer-reviewed journal.

2. (leal2018thepolynucleotidekinase pages 6-8): Alejandro Leal, Sixto Bogantes-Ledezma, Arif B. Ekici, Steffen Uebe, Christian T. Thiel, Heinrich Sticht, Martin Berghoff, Corinna Berghoff, Bernal Morera, Michael Meisterernst, and André Reis. The polynucleotide kinase 3′-phosphatase gene (pnkp) is involved in charcot-marie-tooth disease (cmt2b2) previously related to med25. Neurogenetics, 19:215-225, Jul 2018. URL: https://doi.org/10.1007/s10048-018-0555-7, doi:10.1007/s10048-018-0555-7. This article has 51 citations and is from a peer-reviewed journal.

3. (leal2018thepolynucleotidekinase pages 4-6): Alejandro Leal, Sixto Bogantes-Ledezma, Arif B. Ekici, Steffen Uebe, Christian T. Thiel, Heinrich Sticht, Martin Berghoff, Corinna Berghoff, Bernal Morera, Michael Meisterernst, and André Reis. The polynucleotide kinase 3′-phosphatase gene (pnkp) is involved in charcot-marie-tooth disease (cmt2b2) previously related to med25. Neurogenetics, 19:215-225, Jul 2018. URL: https://doi.org/10.1007/s10048-018-0555-7, doi:10.1007/s10048-018-0555-7. This article has 51 citations and is from a peer-reviewed journal.

4. (gatti2019fromcongenitalmicrocephaly pages 1-2): Marta Gatti, Stefania Magri, Lorenzo Nanetti, Elisa Sarto, Daniela Di Bella, Ettore Salsano, Chiara Pantaleoni, Caterina Mariotti, and Franco Taroni. From congenital microcephaly to adult onset cerebellar ataxia: distinct and overlapping phenotypes in patients with pnkp gene mutations. American Journal of Medical Genetics Part A, 179:2277-2283, Aug 2019. URL: https://doi.org/10.1002/ajmg.a.61339, doi:10.1002/ajmg.a.61339. This article has 29 citations.

5. (weinfeld2011tidyinguploose pages 5-7): Michael Weinfeld, Rajam S. Mani, Ismail Abdou, R. Daniel Aceytuno, and J.N. Mark Glover. Tidying up loose ends: the role of polynucleotide kinase/phosphatase in dna strand break repair. Trends in biochemical sciences, 36 5:262-71, May 2011. URL: https://doi.org/10.1016/j.tibs.2011.01.006, doi:10.1016/j.tibs.2011.01.006. This article has 247 citations and is from a domain leading peer-reviewed journal.

6. (weinfeld2011tidyinguploose pages 4-5): Michael Weinfeld, Rajam S. Mani, Ismail Abdou, R. Daniel Aceytuno, and J.N. Mark Glover. Tidying up loose ends: the role of polynucleotide kinase/phosphatase in dna strand break repair. Trends in biochemical sciences, 36 5:262-71, May 2011. URL: https://doi.org/10.1016/j.tibs.2011.01.006, doi:10.1016/j.tibs.2011.01.006. This article has 247 citations and is from a domain leading peer-reviewed journal.

7. (dumitrache2017polynucleotidekinasephosphatase(pnkp) pages 1-2): Lavinia C. Dumitrache and Peter J. McKinnon. Polynucleotide kinase-phosphatase (pnkp) mutations and neurologic disease. Mechanisms of Ageing and Development, 161:121-129, Jan 2017. URL: https://doi.org/10.1016/j.mad.2016.04.009, doi:10.1016/j.mad.2016.04.009. This article has 95 citations and is from a peer-reviewed journal.

8. (hulmakova2025theroleof pages 20-23): A Hulmáková. The role of polynucleotide kinase/phosphatase in dna strand break repair and its implications in human diseases. Unknown journal, 2025.

9. (jiang2022mutationsofthe pages 13-13): Bingcheng Jiang, Cameron Murray, Bonnie L. Cole, J. N. Mark Glover, Gordon K. Chan, Jean Deschenes, Rajam S. Mani, Sudip Subedi, John D. Nerva, Anthony C. Wang, Christina M. Lockwood, Heather C. Mefford, Sarah E. S. Leary, Jeffery G. Ojemann, Michael Weinfeld, and Chibawanye I. Ene. Mutations of the dna repair gene pnkp in a patient with microcephaly, seizures, and developmental delay (mcsz) presenting with a high-grade brain tumor. Scientific Reports, Mar 2022. URL: https://doi.org/10.1038/s41598-022-09097-w, doi:10.1038/s41598-022-09097-w. This article has 17 citations and is from a peer-reviewed journal.

10. (garrelfs2020eurresearchinformation pages 1-3): MR Garrelfs, S Takada, EJ Kamsteeg, and S Pegge. Eur research information portal. Unknown journal, 2020.

11. (gatti2019fromcongenitalmicrocephaly pages 2-3): Marta Gatti, Stefania Magri, Lorenzo Nanetti, Elisa Sarto, Daniela Di Bella, Ettore Salsano, Chiara Pantaleoni, Caterina Mariotti, and Franco Taroni. From congenital microcephaly to adult onset cerebellar ataxia: distinct and overlapping phenotypes in patients with pnkp gene mutations. American Journal of Medical Genetics Part A, 179:2277-2283, Aug 2019. URL: https://doi.org/10.1002/ajmg.a.61339, doi:10.1002/ajmg.a.61339. This article has 29 citations.

12. (hulmakova2025theroleof pages 32-35): A Hulmáková. The role of polynucleotide kinase/phosphatase in dna strand break repair and its implications in human diseases. Unknown journal, 2025.

13. (jiang2022mutationsofthe pages 12-13): Bingcheng Jiang, Cameron Murray, Bonnie L. Cole, J. N. Mark Glover, Gordon K. Chan, Jean Deschenes, Rajam S. Mani, Sudip Subedi, John D. Nerva, Anthony C. Wang, Christina M. Lockwood, Heather C. Mefford, Sarah E. S. Leary, Jeffery G. Ojemann, Michael Weinfeld, and Chibawanye I. Ene. Mutations of the dna repair gene pnkp in a patient with microcephaly, seizures, and developmental delay (mcsz) presenting with a high-grade brain tumor. Scientific Reports, Mar 2022. URL: https://doi.org/10.1038/s41598-022-09097-w, doi:10.1038/s41598-022-09097-w. This article has 17 citations and is from a peer-reviewed journal.

14. (hulmakova2025theroleof pages 38-41): A Hulmáková. The role of polynucleotide kinase/phosphatase in dna strand break repair and its implications in human diseases. Unknown journal, 2025.

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Type_2B2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011570` (3 mentions) - the report calls it "if available"; MONDO calls it **Charcot-Marie-Tooth disease type 2B2**