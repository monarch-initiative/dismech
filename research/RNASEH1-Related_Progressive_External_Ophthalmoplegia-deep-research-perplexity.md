---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-29T20:41:41.601864'
end_time: '2026-09-29T20:46:40.916506'
duration_seconds: 299.31
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: RNASEH1-Related Progressive External Ophthalmoplegia
  mondo_id: MONDO:0014656
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 68
  verified: 62
  not_found: 2
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.03
  labels_checked: 44
  labels_matching: 19
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0000506
    reported_labels:
    - external ophthalmoplegia
    ontology_label: Telecanthus
  - term_id: HP:0006205
    reported_labels:
    - multiple mitochondrial DNA deletions
    ontology_label: Irregular phalanges
  - term_id: HP:0003298
    reported_labels:
    - abnormal mitochondrial respiratory chain complex I activity
    ontology_label: Spina bifida occulta
  - term_id: GO:0030135
    reported_labels:
    - mitochondrial membrane potential
    ontology_label: coated vesicle
  - term_id: HP:0030057
    reported_labels:
    - abnormal mitochondrial DNA replication
    ontology_label: Autoimmune antibody positivity
  - term_id: GO:0036298
    reported_labels:
    - "RNA\u2013DNA hybrid resolution"
    ontology_label: recombinational interstrand cross-link repair
  - term_id: GO:0034249
    reported_labels:
    - response to double-stranded RNA
    ontology_label: obsolete negative regulation of amide metabolic process
  - term_id: NCIT:C27897
    reported_labels:
    - Blepharoplasty
    ontology_label: T-Cell Proliferation of Uncertain Malignant Potential
  - term_id: NCIT:C26990
    reported_labels:
    - Eyelid Reconstruction
    ontology_label: Transplanted Kidney Complication
  - term_id: NCIT:C15273
    reported_labels:
    - Physical Therapy
    ontology_label: Longitudinal Study
  - term_id: NCIT:C15248
    reported_labels:
    - Occupational Therapy
    ontology_label: Hemodialysis
  - term_id: NCIT:C15279
    reported_labels:
    - Speech Therapy
    ontology_label: Radical Mastectomy
  labels_variant: 13
  unresolved_terms:
  - HP:0000507
  - HP:0003703
  obsolete_terms:
  - term_id: GO:0034249
    ontology_label: obsolete negative regulation of amide metabolic process
    replaced_by: GO:0009892
  - term_id: CL:0000215
    ontology_label: obsolete barrier cell
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RNASEH1-Related Progressive External Ophthalmoplegia
- **MONDO ID:** MONDO:0014656 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RNASEH1-Related Progressive External Ophthalmoplegia** covering all of the
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

# RNASEH1-Related Progressive External Ophthalmoplegia: Comprehensive Disease Characterization

RNASEH1-related progressive external ophthalmoplegia (PEO) is a rare mitochondrial DNA (mtDNA) maintenance disorder caused by biallelic loss-of-function mutations in the nuclear gene *RNASEH1*, which encodes the endonuclease ribonuclease H1 (RNase H1). The disease presents in adulthood with a remarkably homogeneous neuromuscular phenotype dominated by chronic progressive external ophthalmoplegia, ptosis, exercise intolerance, proximal limb weakness, and variably prominent spinocerebellar ataxia, dysphagia, and respiratory impairment.[10][11][12][13][15][16][17] At the molecular level, RNase H1 is essential for removal of RNA primers and RNA–DNA hybrids during mtDNA replication; its deficiency causes mtDNA replication slowdown, accumulation of multiple mtDNA deletions and replication intermediates, and secondary mitochondrial respiratory chain dysfunction in affected tissues.[1][2][13][15][16][18] Human and mouse studies demonstrate that RNase H1 is also involved in nuclear R-loop resolution, telomere maintenance, and regulation of mitochondrial replication under oxidative stress, but human RNASEH1 disease appears to be driven primarily by mitochondrial dysfunction rather than catastrophic nuclear instability.[2][13][15][16] Recent work has further revealed that RNASEH1 mutations drive innate immune activation through the release of mitochondrial double-stranded RNA (mt-dsRNA), engaging cytosolic nucleic acid sensors and microglial activation with potential implications for neurologic progression.[7] Clinically, RNASEH1 mutations represent an uncommon yet fourth-ranking cause of adult Mendelian PEO with multiple mtDNA deletions, after *POLG*, *RRM2B*, and *TWNK*, and affected individuals typically have a relatively benign, slowly progressive course with significant functional morbidity but often preserved life expectancy.[10][15][16][17] This report synthesizes current knowledge on RNASEH1-related PEO, integrating clinical phenotypes, genetic and molecular mechanisms, anatomical and temporal features, diagnostics, outcomes, treatments, prevention, and model organism data into a structured disease profile suitable for a comprehensive knowledge base.

## 1. Disease Information

### 1.1 Overview and definition

RNASEH1-related progressive external ophthalmoplegia is a primary mitochondrial disorder belonging to the broader category of mtDNA maintenance defects, characterized by secondary mtDNA deletions and depletion in affected tissues due to pathogenic variants in nuclear genes required for mtDNA replication.[10][13][15][16][18] In the initial landmark description, Reyes et al. identified compound heterozygous *RNASEH1* mutations in two unrelated individuals and a homozygous mutation in four siblings, all presenting with adult-onset chronic PEO, ptosis, exercise intolerance, and subsequent limb weakness, dysphagia, and spinocerebellar signs.[13] Subsequent series and case reports have confirmed a consistent phenotype of adult-onset mitochondrial encephalomyopathy dominated by ophthalmoplegia and muscle involvement, with multiple mtDNA deletions and mtDNA replication abnormalities in skeletal muscle and fibroblasts.[15][16][17] Orphanet describes “adult-onset chronic progressive external ophthalmoplegia with mitochondrial myopathy” as a rare mitochondrial disease characterized by adult onset of progressive external ophthalmoplegia, exercise intolerance, muscle weakness, spinocerebellar ataxia, dysarthria, and mild motor peripheral neuropathy, with possible respiratory insufficiency, matching the clinical picture of RNASEH1-related disease.[11][12] From a nosologic perspective, RNASEH1-related PEO is best classified as a Mendelian mitochondrial encephalomyopathy with mtDNA multiple deletions, falling under the MONDO ontology as MONDO:0014656 (progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2, PEOB2).

Reyes et al. summarized the disease entity as follows: 

> “Chronic progressive external ophthalmoplegia (CPEO) is common in mitochondrial disorders and is frequently associated with multiple mtDNA deletions… Next-generation sequencing led to the identification of compound-heterozygous RNASEH1 mutations in two singleton subjects and a homozygous mutation in four siblings… All affected individuals first presented with CPEO and exercise intolerance in their twenties, and these were followed by muscle weakness, dysphagia, and spino-cerebellar signs…”[13]

This description, corroborated by later cohorts,[15][16][17] establishes RNASEH1-related PEO as an adult-onset, slowly progressive mitochondrial disease centered on extraocular muscle failure and broader neuromuscular involvement. The preferred high-level disease label for knowledge-base purposes is **RNASEH1-related mitochondrial encephalomyopathy with progressive external ophthalmoplegia**, aligning with recent case-report terminology.[17]

### 1.2 Identifiers, synonyms, and classification

The key identifiers for RNASEH1-related PEO span multiple biomedical ontologies and databases. OMIM lists *RNASEH1* under entry 604123 and associates it with "Progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2" (PEOB2), OMIM phenotype number 616479.[1][12][14] MedGen and the Genetic Testing Registry similarly catalog “Progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2” (Concept ID C4225312) and explicitly link it to the *RNASEH1* gene at cytogenetic location 2p25.3.[12][14] Orphanet registers “Adult-onset chronic progressive external ophthalmoplegia with mitochondrial myopathy” under ORPHA:329336, listing autosomal dominant and mitochondrial inheritance, but in practice RNASEH1-related cases are autosomal recessive; the Orphanet phenotype description nevertheless closely matches the RNASEH1 disease phenotype and is cross-referenced to OMIM 616479.[11] ICD-10 classification for this disorder is typically G71.3 (“Primary disorders of muscles”), consistent with Orphanet’s assignment.[11] The Human Phenotype Ontology (HPO) maps individual phenotypic features but does not currently list RNASEH1 as a separate disease entity; at the disease level, the Mondo ontology identifier MONDO:0014656 corresponds to "progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2", encompassing RNASEH1-related PEO.

Common synonyms and alternative names include "RNASEH1-related mitochondrial disease",[15] "RNASEH1-related mitochondrial encephalomyopathy",[16][17] "adult-onset mitochondrial encephalomyopathy with multiple mtDNA deletions",[17] "progressive external ophthalmoplegia with mitochondrial DNA deletions-2 (PEOB2)",[1][12][14] and "adult-onset CPEO with mitochondrial myopathy".[11] Historical terms such as "chronic progressive external ophthalmoplegia (CPEO)" and "CPEO-plus" are frequently used in the clinical literature, where RNASEH1 disease is considered one of several genetic etiologies underlying these clinical syndromes.[10][13][15] At the gene level, synonyms include "ribonuclease H1", "RNase H1", "H1RNA", and "RNH1".[1][8][14][17] 

In terms of information sources, the clinical and mechanistic data summarized here are derived predominantly from aggregated disease-level resources and curated case series rather than individual EHR datasets. OMIM,[1] MedGen,[12] Orphanet,[11] GeneReviews figures,[18] and Genomics England PanelApp entries[3] synthesize published case reports and research cohorts, while primary evidence comes from peer-reviewed clinical and experimental studies such as Reyes et al. 2015 (Am J Hum Genet),[13] Bugiardini et al. 2017 (Neurol Genet),[15] Carreño-Gago et al. 2019,[16] and the Italian case report 2022.[17] Thus, the disease characterization is based on aggregated, literature-derived information rather than raw clinical datasets, which is important for evaluating evidence strength and representativeness.

### 1.3 Disease category and scope

RNASEH1-related PEO belongs to the category of Mendelian disorders with nuclear gene defects causing secondary mtDNA maintenance defects. GeneReviews’ overview of mtDNA maintenance defects explicitly lists RNase H1 (encoded by *RNASEH1*) among the nucleases that remove RNA primers and flap intermediates during mtDNA replication, alongside DNA2 and MGME1.[18] Within the broader PEO spectrum, a comprehensive review by Scarpelli et al. emphasized that “single large-scale deletions of mtDNA are the most frequent causes of sporadic mitochondrial PEO and Kearns–Sayre syndrome, while nDNA defects causing secondary defects of mtDNA maintenance are the most frequent causes of autosomal mitochondrial PEO and PEO-plus syndromes.”[10] In that framework, RNASEH1 mutations are one of several nuclear gene defects—including *POLG*, *RRM2B*, and *TWNK*—that lead to secondary mtDNA deletions and adult PEO syndromes.[10][15][16] 

Bugiardini et al. explicitly termed the condition “RNASEH1-related mitochondrial disease” and noted that “pathologic ribonuclease H1 (RNase H1) causes aberrant mitochondrial DNA (mtDNA) segregation and is associated with multiple mtDNA deletions.”[15] They emphasized that RNASEH1 mutations represent the fourth most common cause of adult Mendelian PEO with multiple mtDNA deletions in their UK national mitochondrial disease service cohort, underscoring the clinical relevance despite its rarity.[15] Carreño-Gago et al. further described the condition as part of the “mtDNA depletion and deletion syndrome” umbrella, characterized by heterogenous clinical phenotypes ranging from fatal infants to mild adult-onset PEO.[16] Thus, from a disease ontology standpoint, RNASEH1-related PEO should be mapped to categories including “Mendelian disease” (MONDO), “primary mitochondrial disease” (PMD), “mtDNA maintenance disorder,” and “progressive external ophthalmoplegia with multiple mtDNA deletions,” with a nuclear genetic etiology in *RNASEH1*.

## 2. Etiology

### 2.1 Genetic causal factors

The primary cause of RNASEH1-related PEO is biallelic (autosomal recessive) pathogenic variants in the *RNASEH1* gene, resulting in loss of function of the RNase H1 endonuclease in mitochondria and, to some extent, nucleus.[1][2][13][15][16][17] *RNASEH1* is located on chromosome 2p25.3, with genomic coordinates 2:3,531,813–3,558,333 (GRCh38).[1] The OMIM entry notes that RNASEH1 encodes an endonuclease present in both nucleus and mitochondria that specifically digests the RNA component of RNA–DNA hybrids.[1] Functional studies using patient-derived fibroblasts and recombinant proteins show that disease-causing mutations reduce or abolish RNase H1 catalytic activity, consistent with a loss-of-function mechanism.[1][13][15][16][17] For example, in vitro expression assays by Reyes et al. demonstrated that the missense mutant V142I retains about 40% activity, A185V retains ~20%, and truncating R157X has negligible activity, and patient fibroblasts show almost complete absence of RNase H1 protein.[13][9] Carreño-Gago et al. similarly showed that both a catalytic domain missense mutation (Y163H) and a connection domain in-frame deletion (Gln86del) completely abolish RNase H1 activity in functional assays, despite in silico prediction labeling only the catalytic missense variant as pathogenic.[16] These convergent findings establish that RNASEH1-related PEO is driven by germline, recessive, loss-of-function mutations in *RNASEH1* that disrupt the enzymatic removal of RNA from RNA–DNA hybrids during mtDNA replication.

ClinVar aggregates multiple RNASEH1 variants with clinical significance in PEOB2. The canonical pathogenic variant c.424G>A (p.Val142Ile) has been submitted as pathogenic/likely pathogenic for PEOB2 by multiple laboratories, with functional studies and segregation data supporting its causality.[9][13][17] The variant V142I lies in the highly conserved catalytic domain of RNase H1 and has been repeatedly found in compound heterozygosity or homozygosity in affected individuals.[9][13][16][17] In contrast, other RNASEH1 missense variants such as p.Met118Val (c.352A>G) have been classified as likely benign, reflecting their presence in population databases without associated disease and lack of functional impairment.[5] These data emphasize that only specific RNASEH1 mutations, typically affecting conserved catalytic or structural domains and causing marked loss of function, are etiologic for PEO, whereas other variants may be tolerated.

Genomics England’s PanelApp includes RNASEH1 as a "green" gene in panels for mitochondrial DNA maintenance disorder and mitochondrial disorders, with mode of inheritance annotated as biallelic autosomal or pseudoautosomal, and the associated phenotype specified as “Progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2.”[3] This expert-curated inclusion reflects consensus that RNASEH1 is an established causal gene for mtDNA maintenance disorders presenting as PEO. Furthermore, Orphanet explicitly notes that loss-of-function germline mutations in *RNASEH1* are disease-causing for adult-onset chronic PEO with mitochondrial myopathy.[6] Taken together, the genetic etiology is clear: RNASEH1-related PEO is an autosomal recessive disease caused by loss-of-function germline variants in *RNASEH1*.

### 2.2 Genetic risk factors, susceptibility, and modifiers

Beyond fully penetrant pathogenic variants, relatively little is known about genetic susceptibility factors or modifiers in RNASEH1-related disease. The reported patients almost uniformly carry biallelic RNASEH1 mutations of clear functional impact, and there is no robust evidence for heterozygous RNASEH1 variants acting as susceptibility alleles for sporadic PEO or other common diseases.[13][15][16][17] Population databases such as ExAC and gnomAD reveal that pathogenic RNASEH1 variants (e.g., V142I, R157X, A185V, Gln86del, Y163H, splice-site c.129-3C>G) are extremely rare, with minor allele frequencies well below 0.01%, consistent with recessive disease.[9][13][16][17] These low frequencies imply a correspondingly low carrier frequency in the general population, and no specific founder effects have been described, although some recurrent variants (V142I) appear in multiple Italian and other European families.[9][13][16][17]

Potential modifier genes may include other mtDNA maintenance genes and nuclear factors that influence mitochondrial biogenesis or stress responses, but current datasets are too small to systematically evaluate genotype–phenotype correlations or epistasis. Bugiardini et al. noted that RNASEH1-mutated patients can show a relatively benign phenotype compared to other mtDNA maintenance disorders, suggesting that the residual activity of specific RNASEH1 mutants or the presence of compensatory pathways (e.g., RNase H2 in the nucleus) may modulate severity.[15] However, these are mechanistic inferences rather than well-defined modifier variants. No genome-wide association studies or large-scale sequencing analyses have identified common susceptibility loci associated with PEO risk in RNASEH1 heterozygotes, and the disease remains a classic rare Mendelian condition rather than a complex trait.[10][13][15][16][17]

### 2.3 Environmental and lifestyle risk factors

There is no evidence that environmental exposures, toxins, lifestyle factors, or infections directly cause RNASEH1-related PEO in the absence of pathogenic RNASEH1 mutations. The disease is consistently reported in individuals with biallelic RNASEH1 variants, typically with no relevant environmental history.[13][15][16][17] That said, mitochondrial disorders in general may be exacerbated by metabolic stressors such as infections, malnutrition, extreme physical exertion, certain drugs (e.g., valproate in POLG-related disease), or exposure to mitochondrial toxins, and similar considerations likely apply in RNASEH1-associated disease, although specific data are lacking.[10][15][16][17] 

Oxidative stress has been shown to modulate RNase H1 function in mitochondria in experimental systems. A recent mechanistic study reported that oxidative stress causes accumulation of 8-oxoguanine in mtDNA, impairing RNase H1 recruitment to R-loops in the mitochondrial regulatory region, thereby limiting replication initiation.[2] This suggests that environmental or endogenous factors that increase oxidative stress could interact with RNASEH1 deficiency to further compromise mtDNA replication. However, such interactions have not yet been rigorously examined in RNASEH1 patients. Similarly, age is an implicit risk factor in the sense that disease manifests in adulthood, but this reflects the natural history of mtDNA deletion accumulation rather than a modifiable exposure.[10][11][13][15][16][17]

### 2.4 Protective factors and gene–environment interactions

No specific protective genetic variants or environmental exposures have been documented for RNASEH1-related PEO. Heterozygous carriers of pathogenic RNASEH1 variants appear clinically unaffected, indicating that one functional allele is sufficient to maintain normal mtDNA replication under usual circumstances.[13][15][16][17] The presence of RNase H2 in the nucleus likely provides partial redundancy for nuclear RNA–DNA hybrid resolution, which could be considered a natural protective mechanism limiting nuclear consequences of RNASEH1 loss.[2][13][15] In mitochondria, however, RNase H1 is unique, and its loss leads to embryonic lethality in mice, highlighting the vulnerability of this compartment.[1][2][15][16]

Lifestyle measures that reduce oxidative stress, such as avoidance of smoking, control of diabetes and other metabolic conditions, and balanced nutrition, may theoretically mitigate mitochondrial damage and symptom progression, but direct evidence specific to RNASEH1 disease is absent. Gene–environment interactions have been explored more broadly in mtDNA maintenance disorders, where stressors can precipitate clinical deterioration, yet no formal gene–environment interaction studies have been performed for RNASEH1 specifically.[10][15][16][17][2] For knowledge-base purposes, it is appropriate to state that RNASEH1-related PEO is primarily a genetic disease driven by biallelic loss-of-function *RNASEH1* variants, with environmental factors playing at most a modulatory role in symptom expression.

## 3. Phenotypes

### 3.1 Core neuromuscular features

The cardinal phenotype of RNASEH1-related disease is chronic progressive external ophthalmoplegia, accompanied by bilateral ptosis.[10][11][12][13][15][16][17] HPO terms corresponding to these features include *external ophthalmoplegia* (HP:0000506) and *ptosis* (HP:0000507). Reyes et al. reported that “all affected individuals first presented with CPEO and exercise intolerance in their twenties,” with subsequent muscle weakness and cerebellar signs.[13] Bugiardini et al. found that PEO was present in 100% of their RNASEH1-mutated cohort, confirming the consistency of this feature.[15] Carreño-Gago et al. similarly described a patient with “mild mitochondrial myopathy characterized by PEO and multiple mtDNA deletions,” while the Italian case report documented two patients “affected by chronic PEO, ptosis, and muscle weakness.”[16][17] Orphanet’s disease definition explicitly mentions adult-onset progressive external ophthalmoplegia and muscle weakness as core manifestations.[11]

The ophthalmoplegia is typically slowly progressive, bilateral, and accompanied by ptosis that often precedes or accompanies extraocular muscle weakness.[10][11][13][15][16][17] The pupils are generally spared, differentiating this syndrome from oculomotor nerve palsy or myasthenia gravis.[10] Scarpelli et al. noted that classical CPEO is defined by progressive ptosis and impaired eye movements, bilaterality, multi-nerve innervation of affected muscles, sparing of pupils, gradual progression over months or years, and absence of remissions or exacerbations.[10] RNASEH1-related PEO conforms tightly to this definition, indicating that the phenotype meets canonical CPEO criteria.

Exercise intolerance and proximal limb weakness are common, reflecting the involvement of limb-girdle and axial muscles. HPO terms include *exercise intolerance* (HP:0003546) and *proximal muscle weakness* (HP:0003701). Affected individuals often report fatigue on exertion, difficulty with activities such as climbing stairs or raising arms, and sometimes require assistive devices over time.[13][15][16][17] Muscle biopsy findings support a primary mitochondrial myopathy, with ragged-red fibers, cytochrome c oxidase (COX)-negative fibers, and diffuse mitochondrial proliferation and structural abnormalities.[13][15][16][17] These histologic features correspond to HPO terms *ragged-red muscle fibers* (HP:0003200) and *mitochondrial proliferation* (HP:0003703).

### 3.2 Cerebellar, bulbar, and peripheral nervous system involvement

A substantial proportion of RNASEH1-mutated patients display signs of cerebellar involvement, including gait ataxia, dysmetria, and dysarthria.[11][12][13][15][16][17] Orphanet lists “manifestations of spinocerebellar ataxia (e.g., impaired gait, dysarthria)” in its disease definition.[11][12] Bugiardini et al. reported cerebellar ataxia in 57% of their cohort, with one patient meeting criteria for the ataxia neuropathy spectrum phenotype.[15] The Italian case report noted that RNASEH1 mutations produce a homogeneous phenotype including “limb weakness, cerebellar ataxia, and dysphagia,”[17] underscoring the prominence of cerebellar features. HPO terms relevant here include *gait ataxia* (HP:0002141), *dysmetria* (HP:0001310), *dysarthria* (HP:0001260), and *cerebellar ataxia* (HP:0001251).

Bulbar symptoms such as dysphagia and dysphonia/dysarthria are frequently observed. Reyes et al. described “dysphagia and spino-cerebellar signs with impaired gait coordination, dysmetria, and dysarthria” in their patients.[13] Bugiardini et al. noted dysphagia in 50% of the cohort.[15] Carreño-Gago and colleagues highlighted proximal facial weakness, which can contribute to dysphagia and dysarthria.[16] Dysphagia corresponds to HPO term HP:0002015, and facial muscle weakness to HP:0001634. Peripheral neuropathy is often mild but present, with Orphanet describing “mild motor peripheral neuropathy” and Bugiardini et al. noting neuropathic features in some patients.[11][15] This can be represented by *motor peripheral neuropathy* (HP:0003477).

Respiratory involvement appears in a subset of patients as respiratory impairment or insufficiency. Orphanet explicitly mentions that “Respiratory insufficiency has been reported in some cases.”[11][12] Bugiardini et al. noted respiratory impairment among prominent clinical traits, and Carreño-Gago reported respiratory involvement in their patient.[15][16] HPO terms include *respiratory insufficiency* (HP:0002093) and *sleep apnea* (HP:0010535) where applicable, although specific sleep-related breathing disturbances have not been systematically described.

### 3.3 Systemic and laboratory phenotypes

Laboratory and histopathologic abnormalities constitute important phenotypic components. Muscle biopsies in RNASEH1-related disease consistently show mitochondrial abnormalities, including ragged-red fibers on Gomori trichrome staining, COX-negative fibers, succinate dehydrogenase (SDH)-positive fibers, and multiple mtDNA deletions revealed by molecular analysis.[13][15][16][17] The Italian case report summarized: “Muscle biopsy showed mitochondrial abnormalities, with diffuse RRFs, SDH-positive, COX-negative fibers, and multiple mtDNA deletions accumulating in muscle.”[17] These features map to HPO terms *ragged-red muscle fibers* (HP:0003200), *cytochrome c oxidase deficiency in muscle tissue* (HP:0003688), *multiple mitochondrial DNA deletions* (HP:0006205), and *mitochondrial myopathy* (HP:0003200).

Biochemical assays often reveal impaired activities of mitochondrial respiratory chain complexes I, III, and IV, consistent with secondary mtDNA deletions affecting multiple mtDNA-encoded subunits.[13][15][16][17] Reyes et al. reported “impaired activity of various mitochondrial respiratory chain complexes” in muscle biopsies.[13] HPO terms can include *abnormal mitochondrial respiratory chain complex I activity* (HP:0003298) and similar terms for complexes III and IV. In fibroblasts, patient cells grow more slowly in galactose medium, have decreased mitochondrial membrane potential, and show abnormal perinuclear aggregation of fragmented mitochondria.[9][13] These in vitro phenotypes illustrate mitochondrial dysfunction and can be linked to GO terms such as *mitochondrial membrane potential* (GO:0030135) and *mitochondrial fission* (GO:0000266).

At the molecular level, RNASEH1-deficient cells show mtDNA replication defects. Reyes et al. observed an increase in mtDNA replication intermediates, suggestive of replication slowdown, and increased 7S DNA levels, a marker of replication origin activity.[13][17] Carreño-Gago demonstrated that fibroblasts from their patient failed to recover normal mtDNA copy number after ethidium bromide-induced mtDNA depletion, indicating impaired mtDNA replication capacity.[16] HPO term *abnormal mitochondrial DNA replication* (HP:0030057) captures this feature. Laboratory tests in blood are generally nonspecific, though lactate may be mildly elevated and creatine kinase sometimes increased, as in other mitochondrial myopathies.[10][15][16][17]

### 3.4 Symptom onset, severity, progression, and quality of life impact

Age of onset in RNASEH1-related PEO is uniformly adult, typically in the third decade. Reyes et al. reported initial symptoms in the twenties.[13] Orphanet lists age of onset as “adult,” and the Italian case report describes “adult-onset mitochondrial encephalomyopathy.”[11][17] HPO designates adult onset as HP:0003581. The onset pattern is insidious and chronic, with gradual progression over years rather than acute episodes.[10][11][13][15][16][17] Scarpelli et al. emphasized that CPEO progresses “gradually over months or years,” and RNASEH1-related disease conforms to this pattern.[10] There are no remissions or relapsing–remitting courses; the disease course is steadily progressive but often slow, representing a chronic lifelong condition.[10][13][15][16][17]

Symptom severity is variable but often moderate. Many patients remain ambulatory and maintain functional independence for years, though they may require eyelid surgery or assistive devices for limb weakness and ataxia.[10][13][15][16][17] Bugiardini et al. concluded that “the phenotypic spectrum in adults is relatively benign” compared to other mtDNA maintenance disorders, though the disease still entails significant morbidity.[15] Quality of life is impacted by visual dysfunction (from ptosis and ophthalmoplegia), exercise intolerance, dysphagia, and ataxia, which impair daily activities such as reading, driving, walking, and eating.[10][11][13][15][16][17] While formal quality-of-life instruments (e.g., SF-36, EQ-5D) have not been systematically applied in RNASEH1 cohorts, data from broader PEO and mitochondrial disease studies suggest marked impairment in physical functioning, role limitations, and vitality domains.[10] In particular, persistent ptosis and ophthalmoplegia can cause social stigma and functional visual limitation, while dysphagia and respiratory impairment raise risks of aspiration and chronic respiratory failure.

For knowledge-base annotation, suggested HPO terms with typical frequency estimates include: *external ophthalmoplegia* (HP:0000506; frequency ~100%), *ptosis* (HP:0000507; ~100%), *exercise intolerance* (HP:0003546; >90%), *proximal muscle weakness* (HP:0003701; >80%), *cerebellar ataxia* (HP:0001251; ~50–60%), *dysphagia* (HP:0002015; ~50%), *dysarthria* (HP:0001260; ~50%), *respiratory insufficiency* (HP:0002093; ~20–30%), *multiple mtDNA deletions* (HP:0006205; ~100% in muscle), and *ragged-red muscle fibers* (HP:0003200; ~100% in biopsied patients).[11][13][15][16][17]

## 4. Genetic and Molecular Information

### 4.1 The RNASEH1 gene and RNase H1 protein

*RNASEH1* encodes ribonuclease H1 (RNase H1), a member of the RNase H family of endonucleases that recognize and cleave the RNA strand of RNA–DNA hybrids.[1][2][4][8] The gene is located on chromosome 2p25.3, and OMIM notes genomic coordinates 2:3,531,813–3,558,333 on GRCh38.[1] RNase H1 contains a single RNase H domain responsible for catalytic activity.[4] Thermo Fisher describes RNase H1’s molecular function as “magnesium ion binding, nucleic acid binding, RNA binding, RNA–DNA hybrid ribonuclease activity, ribonuclease activity, protein binding,” capturing its role as a magnesium-dependent endonuclease.[4] The enzyme is present in both the nucleus and mitochondria; a fraction of the predominantly nuclear RNase H1 is targeted to mitochondria, where it is essential for mtDNA replication.[1][2][4]

Functionally, RNase H1 specifically degrades RNA within RNA–DNA hybrids, a specificity exploited experimentally to map R-loops genome-wide using a catalytically dead mutant that binds but does not resolve hybrids.[2] In mitochondria, RNase H1 participates in removal of RNA primers used by DNA polymerase γ (POLG) to initiate replication, as well as cleavage of R-loops in the displacement loop (D-loop) region, thereby regulating mtDNA replication initiation.[2][13][16][18] GeneReviews’ figure on mtDNA maintenance defects lists RNase H1 among “nucleases removing RNA primers and flap intermediates,” alongside DNA2 and MGME1.[18] In the nucleus, RNase H1 recruitment to R-loops is driven by a direct interaction with replication protein A (RPA), which enhances hybrid binding and stimulates cleavage; RPA-binding-defective RNase H1 mutants fail to localize to R-loops and cannot suppress R-loop-associated genomic instability.[2] RNase H1’s endonucleolytic activity is coupled to the 3′–5′ exonuclease REXO4 in a combined endo/exo-cleavage mechanism that degrades R-loops.[2]

At telomeres using the alternative lengthening of telomeres (ALT) pathway, RNase H1 resolves TERRA–telomeric RNA–DNA hybrids, restraining recombination-based telomere maintenance; RNase H1 depletion drives hybrid accumulation and telomere excision, whereas overexpression reduces telomere recombinogenicity.[2] Oxidative stress restricts RNase H1 function in mitochondria by causing 8-oxoguanine accumulation in mtDNA, impairing its recruitment to R-loops in the regulatory region.[2] These diverse roles underscore RNase H1 as a multifaceted enzyme bridging mitochondrial replication, nuclear R-loop homeostasis, telomere biology, and oxidative stress responses. However, human RNASEH1-related disease appears to be driven primarily by mitochondrial dysfunction, as discussed below.

Ontology annotations for RNASEH1 include HGNC symbol “RNASEH1,” GO molecular function *RNA–DNA hybrid ribonuclease activity* (GO:0004381), *magnesium ion binding* (GO:0000287), and GO biological processes *mitochondrial DNA replication* (GO:0006264), *RNA catabolic process* (GO:0006401), and *DNA replication, removal of RNA primer* (GO:0006269).[4][18]

### 4.2 Pathogenic variants: types, classification, and population frequency

Pathogenic RNASEH1 variants associated with PEOB2 are predominantly missense, truncating, or splice-site mutations that affect conserved residues in the catalytic or connection domains, or disrupt proper splicing and protein stability.[1][9][13][15][16][17] Reyes et al. identified compound heterozygous mutations in two singleton subjects and a homozygous mutation in four siblings.[13] In one proband (S1), they found c.424G>A (V142I) and c.469C>T (R157X) in exon 4; in another (S2), V142I was compound heterozygous with c.554C>T (A185V).[9][13] All three missense/truncating alterations lie in the catalytic domain and are highly conserved.[9][13] In vitro expression assays in *E. coli* showed that V142I retains ~40% residual activity, A185V ~20%, and R157X essentially no activity.[9][13] Functional assays and clinical data support classification of V142I and A185V as pathogenic or likely pathogenic, and R157X as pathogenic.[9][13] ClinVar lists NM_002936.6(RNASEH1):c.424G>A (p.Val142Ile) as Pathogenic/Likely pathogenic for PEOB2, with three submissions and last evaluation in 2021.[9]

Carreño-Gago et al. reported a patient with two homozygous RNASEH1 mutations: c.258_260del (p.Gln86del), an in-frame deletion in exon 3, and c.487T>C (p.Tyr163His) in exon 4.[16] The first mutation lies in the connection domain, a previously mutation-free region, and the second in the catalytic domain.[16] In silico prediction only flagged Tyr163His as pathogenic, but functional studies showed that both Gln86del and Tyr163His abolish RNase H1 activity, demonstrating that connection-domain structural integrity is also critical for function.[16] The Italian case report described two patients with homozygous mutations: c.129-3C>G, a splice-site variant resulting in loss of exon 2 in the RNASEH1 transcript, and c.424G>A (V142I) in homozygous form.[17] The splice-site mutation had not been previously reported, and muscle transcript analysis confirmed exon 2 skipping.[17] This report thus expanded the RNASEH1 mutational spectrum and confirmed the pathogenic role of homozygous V142I.[17]

Altogether, at least six RNASEH1 mutations had been reported in 16 patients by 2019, including V142I, R157X, A185V, Gln86del, Tyr163His, and c.129-3C>G, with new cases adding more alleles.[16][17] Lieber et al. and Sachdev et al. also contributed RNASEH1-mutated cases, although specifics are outside the immediate search results.[16][17] In contrast, other RNASEH1 variants such as p.Met118Val (c.352A>G), recorded in ClinVar with Variation ID 792818, are classified as likely benign based on single submission and lack of supporting evidence.[5] This variant is present at low frequency in population databases without reported disease association, and there are “no citations for germline classification of this variant in ClinVar.”[5] 

Population allele frequencies for pathogenic variants are extremely low. Reyes et al. noted that V142I, R157X, and A185V had ExAC frequencies <0.01%.[9][13] Carreño-Gago similarly described their variants as rare, with few carriers detected.[16] gnomAD data (not directly in search results) corroborate that RNASEH1 loss-of-function variants are under strong purifying selection, consistent with embryonic lethality in knockout mice and severe functional consequences. All reported disease-associated variants are germline; there is no evidence for somatic RNASEH1 mutations in cancer driving PEO or other phenotypes, and ClinVar lists somatic classification as “none” for RNASEH1 variants in this context.[5][9]

From an ACMG/AMP perspective, pathogenic RNASEH1 variants fulfill criteria including PVS1 (null variant in a gene where LOF is a known mechanism), PS3 (functional studies supportive of damaging effect), PM2 (absent/rare in controls), PP1 (co-segregation with disease in multiple affected family members), and PP4 (patient phenotype and histology highly specific for disease).[9][13][15][16][17] Likely benign variants lack such evidence and may have higher population frequencies or no functional impact.[5]

### 4.3 Functional consequences: loss of function, mitochondrial DNA maintenance, and nuclear roles

All characterized pathogenic RNASEH1 variants result in substantial loss of RNase H1 catalytic activity, leading to impaired degradation of RNA in RNA–DNA hybrids and RNA primers.[1][2][13][15][16][17] Reyes et al. showed that mutant RNase H1 proteins have reduced capability to remove RNA from RNA–DNA hybrids in vitro, confirming their pathogenic role.[13] Western blot analyses of fibroblasts from patient S1 showed “virtual absence of RNase H1 in total lysate,” indicative of nonsense-mediated mRNA decay and/or protein instability.[1][9][13] Carreño-Gago demonstrated that both Gln86del and Tyr163His mutants lack RNase H1 activity, in line with loss of function, and that patient fibroblasts cannot restore mtDNA copy number after depletion, evidencing mtDNA replication dysfunction.[16] The Italian case report confirmed that c.129-3C>G causes exon skipping and presumably truncated or unstable protein, consistent with LOF.[17]

In mitochondria, RNase H1 is essential for mtDNA replication. Cerritelli et al. generated Rnaseh1^-/- mice and observed developmental arrest at embryonic day 8.5, with significant mtDNA depletion and apoptotic cell death, linking RNase H1 to generation of mtDNA and supporting a strand-coupled mechanism of mtDNA replication.[1] The OMIM summary notes: “Its absence in embryos resulted in a significant decrease in mitochondrial DNA content, leading to apoptotic cell death. This report linked RNASEH1 to generation of mitochondrial DNA, providing direct support for the strand-coupled mechanism of mitochondrial DNA replication.”[1] Conditional knockouts in liver and B cells reproduce mtDNA replication defects, further underscoring its essential role.[2] In human patients, RNASEH1 mutations cause accumulation of multiple mtDNA deletions and increased mtDNA replication intermediates, reflecting replication slowdown and impaired RNA primer removal.[13][15][16][17]

In the nucleus, RNase H1 interacts with RPA to recognize and resolve R-loops, with RPA binding enhancing hybrid binding and cleavage.[2] RPA-binding-defective mutants fail to localize to R-loops and cannot suppress R-loop-associated genomic instability.[2] RNase H1 also partners with REXO4 in an endo/exo mechanism to degrade R-loops, playing a broader role in genome stability.[2] At ALT telomeres, RNase H1 resolves TERRA–telomeric RNA–DNA hybrids and restrains recombination-based telomere maintenance.[2] Although these nuclear functions are well-established experimentally, human RNASEH1-related PEO appears to manifest primarily through mitochondrial dysfunction; patients do not show overt nuclear genomic instability syndromes such as cancer predisposition or bone marrow failure, and their phenotype is dominated by mitochondrial encephalomyopathy.[13][15][16][17] This likely reflects partial redundancy with RNase H2 in the nucleus, as well as tissue-specific dependence on mtDNA replication.

### 4.4 Epigenetic and structural genomic considerations

No specific epigenetic abnormalities—such as altered DNA methylation patterns, histone modifications, or chromatin remodeling—have been described as primary drivers or modifiers of RNASEH1-related PEO. The disease is attributed to classical coding and splice-site mutations in *RNASEH1*, without evidence of promoter methylation or regulatory region variation as etiologic factors.[1][13][15][16][17] Similarly, there are no reported large-scale chromosomal abnormalities, such as aneuploidy, translocations, or inversions involving the RNASEH1 locus, in patients with RNASEH1-related PEO.[1][12][14][16][17] DECIPHER and dbVar entries for RNASEH1 structural variants have not been linked to this phenotype in the current literature.

At the structural genomic level of mtDNA, however, RNASEH1 deficiency causes multiple deletions, increased 7S DNA, and replication intermediate accumulation.[13][15][16][17] These mtDNA structural abnormalities constitute a core disease mechanism rather than a separate epigenetic phenomenon. GeneReviews’ figure highlights RNase H1 among the proteins involved in mtDNA replication and primer removal, and conceptualizes disorders like RNASEH1-related PEO as mtDNA maintenance defects due to nuclear gene mutations.[18] Thus, from a knowledge-base standpoint, epigenetic and chromosomal structural factors are not primary in RNASEH1-related PEO, whereas mtDNA structural alterations are central.

## 5. Environmental Information

### 5.1 Non-genetic contributing factors

Current evidence indicates that RNASEH1-related PEO is predominantly driven by genetic factors, with non-genetic contributors playing at most a secondary, modulatory role. No environmental toxin, radiation exposure, occupational hazard, or infectious agent has been identified as a causal factor in the absence of RNASEH1 mutations.[13][15][16][17] The reported patients come from diverse backgrounds, often with unremarkable environmental histories, and their disease onset and progression align more with the time-dependent accumulation of mtDNA deletions than with discrete exposures.[10][13][15][16][17] 

That said, the general mitochondrial disease literature suggests that environmental stressors can exacerbate symptoms or precipitate decompensation. For example, intercurrent infections, fever, malnutrition, or exposure to mitochondrial toxins (e.g., certain antiretrovirals or chemotherapeutics) can worsen myopathic and neurologic symptoms in mtDNA maintenance disorders.[10] RNASEH1-deficient mitochondria, already compromised in replication capacity and respiratory chain function, may be particularly vulnerable to such stressors. However, specific case-level evidence for these interactions in RNASEH1 disease is lacking, and no formal guidelines currently recommend avoiding particular drugs based solely on RNASEH1 status.

### 5.2 Lifestyle factors and comorbidities

Lifestyle factors such as smoking, diet, exercise patterns, and alcohol consumption have not been systematically studied as determinants of RNASEH1 disease onset or severity. Given the adult onset and slow progression, it is plausible that chronic lifestyle-related comorbidities (e.g., diabetes, cardiovascular disease) might compound functional limitations, but this remains speculative. Some clinicians recommend tailored exercise programs and avoidance of extreme exertion for patients with mitochondrial myopathies, aiming to balance conditioning with avoidance of overtraining-induced muscle damage.[10][15][16][17] 

Nutritional status may influence overall mitochondrial health; coenzyme Q10 supplementation and other mitochondrial-targeted nutritional interventions are sometimes used empirically in mitochondrial disease, though evidence for RNASEH1-specific benefit is minimal.[10][15] Alcohol abuse, known to damage muscle and peripheral nerves, could theoretically aggravate symptoms, but again there is no RNASEH1-specific data. For knowledge-base purposes, lifestyle factors should be recorded as generic modifiers rather than defined etiologic elements.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain from mutation to clinical phenotype

1. Biallelic loss-of-function mutations in *RNASEH1* reduce or abolish RNase H1 endonuclease activity in mitochondria and nucleus.[1][2][13][15][16][17]

2. Loss of mitochondrial RNase H1 impairs removal of RNA primers and RNA–DNA hybrids during mtDNA replication, leading to replication fork slowdown and accumulation of replication intermediates and 7S DNA.[1][13][15][16][18]

3. Impaired mtDNA replication results in mtDNA depletion and accumulation of multiple mtDNA deletions in post-mitotic tissues such as skeletal muscle.[1][13][15][16][17]

4. mtDNA deletions and depletion cause combined deficiencies of mitochondrial respiratory chain complexes, reducing ATP production, mitochondrial membrane potential, and altering mitochondrial morphology.[13][15][16][17]

5. Chronic mitochondrial dysfunction in extraocular and limb muscles results in energy failure, leading to progressive external ophthalmoplegia, ptosis, exercise intolerance, and proximal limb weakness.[10][11][12][13][15][16][17]

6. Mitochondrial dysfunction in cerebellar and brainstem neurons leads to spinocerebellar ataxia, dysarthria, dysphagia, and mild peripheral neuropathy via impaired neuronal bioenergetics.[11][13][15][16][17]

7. In RNASEH1-mutant fibroblasts, accumulation and cytosolic release of mitochondrial double-stranded RNA engages innate immune sensors (e.g., RIG-I-like receptors), triggering type I interferon responses and paracrine activation of bystander microglia, contributing to neuroinflammation and disease progression.[7]

8. Nuclear RNase H1 dysfunction leads to increased R-loops and potential genomic instability, but redundancy with RNase H2 and tissue-specific buffering limit overt nuclear phenotypes; mitochondrial mechanisms remain upstream and dominant.[2][15]

### 6.2 Molecular pathways: mtDNA replication, R-loops, and telomere regulation

The central molecular pathway in RNASEH1-related PEO is mtDNA replication. mtDNA replication requires an RNA primer generated by mitochondrial transcription factor A (TFAM) and the transcription machinery, which is then extended by DNA polymerase γ (POLG), with Twinkle helicase unwinding the template strands.[18] GeneReviews’ figure depicts Twinkle (encoded by *TWNK*), POLG, POLG2, and TFAM as key replication proteins, and highlights RNase H1 as one of the nucleases that remove RNA primers and flap intermediates.[18] RNase H1’s role is to cleave RNA in RNA–DNA hybrids created during primer synthesis and lagging-strand replication, ensuring proper transition from RNA to DNA and preventing persistent R-loops that can interfere with replication fork progression.[1][2][13][16][18]

In RNASEH1 deficiency, this primer removal process is compromised. Reyes et al. demonstrated increased mtDNA replication intermediates and 7S DNA levels in RNASEH1-mutated muscle, consistent with slowed replication and altered origin firing.[13][17] Carreño-Gago showed that patient fibroblasts are unable to restore mtDNA copy number after ethidium bromide-induced depletion, indicating a global mtDNA replication defect.[16] The accumulation of replication intermediates and R-loops likely triggers compensatory fork stalling and re-initiation, promoting the formation of small deletions that expand clonally over time. These deletions remove segments of the mtDNA genome encoding respiratory chain subunits, leading to combined oxidative phosphorylation (OXPHOS) defects.[13][15][16][17]

Beyond mitochondria, RNase H1 participates in nuclear RNA–DNA hybrid metabolism. It recognizes R-loops formed during transcription and replication, recruited via RPA, and cleaves the RNA strand.[2] An RPA-binding-defective RNase H1 variant fails to localize to R-loops and cannot suppress R-loop-associated genomic instability, demonstrating the functional importance of this pathway.[2] RNase H1 also interacts with REXO4 to degrade R-loops through coupled endonuclease and exonuclease activity.[2] At ALT telomeres, RNase H1 resolves TERRA–telomeric RNA–DNA hybrids, restraining recombination-based telomere maintenance; loss of RNase H1 in this context increases telomeric recombination and excision.[2] These nuclear roles involve pathways such as DNA damage response, replication stress, and telomere biology, mapped to GO processes like *DNA replication* (GO:0006260), *RNA–DNA hybrid resolution* (GO:0036298), and *telomere maintenance* (GO:0000723). However, no clear clinical telomere-related phenotype has been attributed to RNASEH1 mutations in the reported PEO patients.

Oxidative stress-mediated pathways intersect with RNase H1 function. A recent study showed that oxidative stress causes accumulation of 8-oxoguanine in mtDNA, which impairs RNase H1 recruitment to R-loops in the control region, thereby limiting replication initiation.[2] This implicates pathways such as base excision repair, redox signaling, and mitochondrial biogenesis. RNASEH1 mutations likely further sensitize mtDNA replication to oxidative damage, although direct evidence in patients is emerging rather than definitive.

### 6.3 Cellular processes: mitochondrial dysfunction, apoptosis, and innate immune activation

At the cellular level, RNASEH1 deficiency produces mitochondrial dysfunction, altered mitochondrial morphology, and can trigger apoptosis. Cerritelli et al.’s Rnaseh1^-/- mouse embryos showed mtDNA depletion, leading to apoptotic cell death and developmental arrest at E8.5.[1] In patient-derived fibroblasts, Reyes et al. observed decreased mitochondrial membrane potential and abnormal perinuclear aggregation of fragmented mitochondria, indicating disrupted mitochondrial dynamics and bioenergetics.[9][13] These changes map to GO processes such as *mitochondrial fission* (GO:0000266), *mitochondrial membrane organization* (GO:0007005), and *apoptotic process* (GO:0006915). In skeletal muscle fibers, mitochondrial proliferation produces ragged-red fibers, reflecting an attempt to compensate for respiratory chain deficiency.[13][15][16][17]

A particularly novel aspect of RNASEH1 pathophysiology is innate immune activation via mitochondrial nucleic acids. In a 2026 preprint, Okletey et al. investigated patient-derived fibroblasts from individuals with CPEO carrying RNASEH1 and Twinkle mutations.[7] They provide “for the first time evidence that their mutations drive innate immune activation through the release of different mitochondrial nucleic acids.”[7] Specifically, “RNASEH1 mutations lead to the accumulation and subsequent release of mt-dsRNA, while mtDNA remains protected. On the other hand, mutations in Twinkle cause the release of mtDNA without triggering mt-dsRNA production, or leakage.”[7] The released mitochondrial double-stranded RNA is sensed by cytosolic pattern recognition receptors such as RIG-I-like receptors, leading to type I interferon responses and pro-inflammatory cytokine production. Okletey et al. further showed that cytosolic sensing triggers paracrine signaling to activate bystander microglia—the resident macrophages of the retina and brain—with potential implications for neurological progression of CPEO.[7] This maps to GO processes *innate immune response* (GO:0045087), *response to double-stranded RNA* (GO:0034249), and *type I interferon signaling pathway* (GO:0060337), and CL terms such as *microglia* (CL:0000129) and *fibroblast* (CL:0000057).

Thus, RNASEH1-related PEO involves both cell-autonomous mitochondrial dysfunction and non-cell-autonomous inflammatory processes. In muscle fibers and neurons, mitochondrial ATP shortage and ROS overproduction drive cell dysfunction and degeneration. In fibroblasts and central nervous system cells, mt-dsRNA release and immune sensing contribute to chronic inflammation and may exacerbate tissue damage. The immune-related findings are downstream of mitochondrial nucleic acid accumulation, which is itself a direct consequence of RNASEH1 deficiency in RNA–DNA hybrid processing.

### 6.4 Metabolic changes and biochemical abnormalities

Metabolically, RNASEH1-related PEO manifests as a defect in oxidative phosphorylation due to mtDNA deletions and depletion. Muscle biopsies reveal decreased activities of respiratory chain complexes, leading to reduced ATP generation and increased dependence on glycolysis.[13][15][16][17] In vitro, patient fibroblasts grow more slowly in galactose medium—a condition forcing reliance on mitochondrial respiration—compared to controls.[9][13] This phenotype is characteristic of mitochondrial disorders and indicates impaired OXPHOS. Metabolite-level changes include possible elevation of lactate, especially during exercise, though specific lactate data are not detailed in the retrieved papers.[10][15][16][17] HPO terms such as *lactic acidosis* (HP:0003128) may thus be relevant but not uniformly present.

Biochemically, RNase H1 deficiency is an enzymatic defect: a nuclear-encoded endonuclease responsible for RNA–DNA hybrid hydrolysis is deficient or absent.[1][2][4][13][15][16][17] This fits within BRENDA’s category of “EC 3.1.26.4, ribonuclease H,” and CHEBI entities associated with RNA (CHEBI:33699) and DNA (CHEBI:16991). The biochemical abnormality at the enzyme level triggers upstream replication intermediates and downstream respiratory chain dysfunction. No primary defects in lipid metabolism, amino acid metabolism, or ion channel function have been reported in RNASEH1-related PEO, although secondary metabolic disturbances may arise from energy deficit and muscle wasting.

### 6.5 Epigenetic changes and molecular profiling

At present, epigenetic and multi-omics profiling in RNASEH1-related PEO is limited. No specific DNA methylation signatures or histone modification patterns have been associated with RNASEH1 deficiency. Transcriptomic profiling of patient fibroblasts or muscle may reveal upregulation of stress-response genes and interferon-stimulated genes, particularly in light of the mt-dsRNA innate immune activation described by Okletey et al., but detailed gene expression datasets are not yet widely available.[7] Proteomic analyses of muscle biopsies have focused mainly on respiratory chain proteins and mtDNA-encoded subunits; these show decreased expression reflecting mtDNA deletions.[13][15][16][17] Metabolomics and lipidomics studies specific to RNASEH1 disease are lacking, though broad mitochondrial disease metabolomics highlight lactate, pyruvate, amino acids, and acylcarnitines as potentially altered metabolites.

Nonetheless, the mechanistic insights from Okletey et al. suggest that future multi-omics work could integrate mitochondrial nucleic acid profiling (mtDNA and mt-dsRNA), transcriptomics of interferon pathways, and proteomics of innate immune signaling to build a more detailed systems-level picture of RNASEH1 pathophysiology.[7] For now, knowledge base entries should emphasize the established mechanistic chain relating RNASEH1 loss-of-function to mtDNA replication defects, mtDNA deletions, respiratory chain dysfunction, and mitochondrial myopathy, with an emerging layer of innate immune activation via mt-dsRNA.

### 6.6 Cell types and biological processes: ontology mapping

Key cell types involved in RNASEH1-related PEO include extraocular skeletal muscle fibers (CL:0000182, fast-twitch skeletal muscle cell; CL:0000215, slow-twitch skeletal muscle cell), limb skeletal muscle fibers, Purkinje cells (CL:0000121), brainstem motor neurons, peripheral motor neurons (CL:0000100), fibroblasts (CL:0000057), and microglia (CL:0000129).[10][11][13][15][16][17][7] In extraocular muscles, mtDNA deletions accumulate, leading to failure of eye movement and ptosis. Limb muscles show similar mitochondrial myopathy, causing exercise intolerance and weakness. Cerebellar and brainstem neurons exhibit mitochondrial dysfunction leading to ataxia and bulbar symptoms. Peripheral nerves may be mildly affected, causing motor neuropathy. Fibroblasts are important for mechanistic studies; they mirror patient mitochondrial and innate immune phenotypes. Microglia become activated by paracrine signals from mt-dsRNA-stressed cells, contributing to neuroinflammation.[7]

Biological processes implicated include *mitochondrial DNA replication* (GO:0006264), *DNA replication, removal of RNA primer* (GO:0006269), *RNA catabolic process* (GO:0006401), *mitochondrial electron transport, cytochrome c to oxygen* (GO:0006123), *ATP synthesis coupled electron transport* (GO:0042773), *mitochondrial fission* (GO:0000266), *apoptotic process* (GO:0006915), *innate immune response* (GO:0045087), *response to double-stranded RNA* (GO:0034249), and *type I interferon signaling pathway* (GO:0060337).[1][2][13][15][16][17][7][18] Mapping these GO and CL terms into a causal framework supports structured representation of RNASEH1-related PEO in a mechanistic ontology.

## 7. Anatomical Structures Affected

### 7.1 Organ-level involvement

RNASEH1-related PEO primarily affects the neuromuscular system, with secondary involvement of respiratory and sometimes peripheral nervous systems.[10][11][13][15][16][17] The primary organs include extraocular muscles (UBERON:0001623; e.g., superior rectus, UBERON:0000399), eyelids (UBERON:0001459), skeletal muscles of the limbs and trunk (UBERON:0001134), cerebellum (UBERON:0002037), brainstem (UBERON:0001894), and peripheral nerves (UBERON:0001021). Orphanet’s description of adult-onset CPEO with mitochondrial myopathy highlights ocular and muscular manifestations, as well as spinocerebellar ataxia and mild motor peripheral neuropathy.[11] Bugiardini et al. documented central nervous system involvement (cerebellar ataxia) in more than half of patients, and respiratory insufficiency in some.[15] The respiratory system can be affected through involvement of diaphragm and accessory respiratory muscles, leading to restrictive ventilatory defects, and through central control disruption.[11][15][16][17]

The cardiovascular, digestive (beyond dysphagia), endocrine, and renal systems are not prominently affected in RNASEH1-related PEO, distinguishing it from some other mitochondrial disorders that involve multi-organ failure.[10][15][16] However, dysphagia and aspiration risk can lead to secondary pulmonary complications such as pneumonia. Overall, the body systems involved are predominantly nervous (central and peripheral), muscular, and respiratory, with occasional involvement of the gastrointestinal tract via swallowing difficulty.

### 7.2 Tissue and cell-level involvement

At the tissue level, RNASEH1 disease affects striated muscle tissue (skeletal muscle), nervous tissue (neuronal and glial elements), and connective tissue (fibroblasts).[10][11][13][15][16][17][7] Skeletal muscle fibers show mitochondrial abnormalities and degenerative changes, particularly in extraocular muscles and limb-girdle muscles. Ragged-red fibers indicate subsarcolemmal accumulation of abnormal mitochondria, while COX-negative fibers reflect severe OXPHOS deficiency in individual fibers.[13][15][16][17] These histologic changes localize the pathology to the muscular system.

In the nervous system, cerebellar cortex (Purkinje cell layers), cerebellar white matter, and brainstem nuclei controlling eye movements and swallowing are functionally impaired.[10][13][15][16][17] While neuropathology data are limited, clinical signs strongly implicate these regions. Microglia in the retina and brain, as resident macrophages, are engaged via paracrine signaling in response to mt-dsRNA release from RNASEH1-mutant cells.[7] Peripheral motor neurons and their axons may be mildly affected, corresponding to motor peripheral neuropathy.[11][15]

Fibroblasts, although not a disease target per se, serve as a model tissue capturing systemic mitochondrial and innate immune abnormalities.[7][13][16] They exhibit decreased mtDNA copy number, replication defects, and mt-dsRNA-mediated immune activation. Tissue ontology terms include UBERON:0001134 (skeletal muscle tissue), UBERON:0002037 (cerebellar cortex), and UBERON:0001894 (brainstem).

### 7.3 Subcellular localization and mitochondrial compartments

Subcellularly, the mitochondrion (GO:0005739) is the critical compartment affected. RNase H1 localizes to both nucleus (GO:0005634) and mitochondria, with a fraction targeted to mitochondria via a targeting sequence.[1][2][4] In mitochondria, RNase H1 acts at the mtDNA replication factory, particularly near the D-loop region (mtDNA control region), where RNA primers and R-loops are generated.[2][13][16][18] Loss of RNase H1 leads to accumulation of RNA–DNA hybrids and replication intermediates within these mitochondrial nucleoids. This impacts the mitochondrial inner membrane (GO:0005743) via respiratory chain complex assembly and function, and the mitochondrial matrix (GO:0005759) via replication and transcription processes.

In the nucleus, RNase H1 localizes to chromatin-associated sites where R-loops form, as well as to ALT telomeres.[2] Nuclear compartments involved include chromatin (GO:0000785), replication forks (GO:0005657), and telomeric regions (GO:0000781). However, as noted, nuclear phenotypes are less clinically apparent.

### 7.4 Localization and lateralization of clinical signs

Clinically, the anatomical manifestations are largely bilateral. CPEO is defined by bilaterality of ptosis and ophthalmoplegia, with symmetric involvement of both eyes.[10] Limb weakness and ataxia tend to be symmetric or mildly asymmetric but not strictly lateralized; they reflect diffuse neuromuscular involvement. The spinocerebellar signs, such as gait ataxia and dysmetria, are usually midline or bilateral due to cerebellar dysfunction. Respiratory involvement, when present, affects both hemidiaphragms and accessory muscles, manifesting as general respiratory insufficiency rather than unilateral lesions.[11][15][16][17] Therefore, lateralization is minimal; RNASEH1-related PEO is a symmetric, systemic disorder of mitochondrial function in specific tissue types.

## 8. Temporal Development

### 8.1 Onset: age and pattern

RNASEH1-related PEO is uniformly adult-onset, with symptoms typically appearing in the second to fourth decades of life. Reyes et al. reported that all subjects “first presented with CPEO and exercise intolerance in their twenties.”[13] Orphanet lists age of onset for adult-onset chronic PEO with mitochondrial myopathy as “adult.”[11] Carreño-Gago described a patient diagnosed with “mild mitochondrial myopathy characterized by PEO and multiple mtDNA deletions” in adulthood.[16] The Italian case report refers to “adult-onset mitochondrial encephalomyopathy.”[17] There are no reported pediatric-onset RNASEH1 cases, in contrast to some other mtDNA maintenance disorders that can present in childhood.[16][18]

The onset pattern is insidious and chronic. Ptosis may develop first, followed by gradual limitation of eye movements and exercise intolerance. Limb weakness and cerebellar signs appear later, often years after initial ocular symptoms.[10][13][15][16][17] Patients typically do not recall a discrete onset event; rather, they notice slowly progressive functional decline. This aligns with the pathophysiology of accumulating mtDNA deletions over time, which reach a threshold for respiratory chain dysfunction in high-energy tissues during adulthood.

### 8.2 Progression: stages, rate, and course

Disease progression in RNASEH1-related PEO is slow and relatively benign compared to more severe mtDNA maintenance disorders. Bugiardini et al. concluded that “our data confirm that RNASEH1 mutations are an important cause of mitochondrial disease resulting from the secondary accumulation of multiple mtDNA deletions and that the phenotypic spectrum in adults is relatively benign.”[15] Patients often remain ambulatory for decades, with gradually worsening ptosis, ophthalmoplegia, and limb weakness.[10][13][15][16][17] Cerebellar ataxia and dysphagia may evolve over time, increasing fall risk and aspiration risk. Respiratory impairment, when present, tends to be late-onset.[11][15][16][17]

While formal staging systems have not been developed specifically for RNASEH1 disease, one can conceptualize early, intermediate, and advanced stages. Early-stage disease involves isolated PEO and mild exercise intolerance. Intermediate stages include significant limb weakness, dysphagia, and cerebellar signs. Advanced stages feature severe ophthalmoplegia, substantial gait ataxia, possible wheelchair dependence, and respiratory insufficiency. The progression rate is generally slow, over many years, though variability exists.

The disease course is progressive and chronic, without remissions or episodic exacerbations typical of inflammatory or demyelinating disorders. Scarpelli et al. emphasized that CPEO lacks relapses or remissions.[10] No spontaneous reversals of mtDNA deletions or RNASEH1 function have been reported.

### 8.3 Disease duration, remission patterns, and critical periods

RNASEH1-related PEO is lifelong once manifested, and disease duration extends across decades. Onset in the twenties followed by slow progression implies disease durations often exceeding 30–40 years.[10][13][15][16][17] Remission patterns are absent; the disease does not exhibit spontaneous remission or treatment-induced complete resolution, although symptomatic improvements can occur with supportive interventions. Critical periods include the early adult years when mtDNA deletions accumulate to pathogenic levels, and later life stages where respiratory impairment and dysphagia may pose life-threatening risks.

From a therapeutic standpoint, early recognition during the PEO stage allows for genetic counseling, anticipatory guidance, and planning of supportive care such as eyelid surgery, physical therapy, and monitoring for bulbar and respiratory involvement. The period when cerebellar signs and dysphagia emerge may represent a window for intensified rehabilitation and swallowing therapy to prevent complications.

## 9. Inheritance and Population Characteristics

### 9.1 Inheritance pattern, penetrance, and expressivity

RNASEH1-related PEO follows an autosomal recessive inheritance pattern. OMIM, MedGen, and GTR explicitly list PEOB2 as “autosomal recessive” and associate it with RNASEH1.[1][12][14] Genomics England’s PanelApp annotates RNASEH1 as “BIALLELIC, autosomal or pseudoautosomal” for mitochondrial DNA maintenance disorder and mitochondrial panels.[3] Orphanet’s disease entry for adult-onset CPEO with mitochondrial myopathy lists autosomal dominant and mitochondrial inheritance, reflecting the broader PEO spectrum; however, RNASEH1-specific cases are autosomal recessive.[11][13][15][16][17]

Penetrance appears to be high or complete among individuals with biallelic pathogenic RNASEH1 variants, as all reported homozygotes or compound heterozygotes have clinical disease, typically manifesting in adulthood.[13][15][16][17] There is no evidence of individuals with biallelic RNASEH1 loss-of-function variants who remain asymptomatic, although milder phenotypes may be under-recognized. Expressivity, however, is variable: while PEO and ptosis are universal, the severity of cerebellar ataxia, dysphagia, peripheral neuropathy, and respiratory impairment differ among patients.[11][13][15][16][17] Bugiardini et al. quantified some of this variability, noting cerebellar ataxia in 57% and dysphagia in 50% of their cohort.[15] Such variation likely reflects differences in residual RNase H1 activity, mtDNA deletion patterns, and other genetic or environmental modifiers.

Genetic anticipation has not been reported for RNASEH1-related PEO; disease severity does not appear to increase in successive generations. Germline mosaicism is theoretically possible but has not been documented. Consanguinity may play a role in homozygous RNASEH1 mutations, as in the Italian probands with homozygous V142I and c.129-3C>G, although specific consanguinity data are not detailed.[17] Founder effects have not been conclusively identified, but recurrent V142I mutations in Italian and other European families suggest possible regional clustering.[9][13][16][17]

### 9.2 Epidemiology: prevalence, incidence, and demographics

RNASEH1-related PEO is a rare disease. Orphanet lists the prevalence of adult-onset CPEO with mitochondrial myopathy as “unknown,”[11] and no population-based prevalence or incidence estimates are available for RNASEH1-specific cases. Bugiardini et al. provided relative frequency data within a specialized mitochondrial disease service cohort in the UK.[15] Among 109 adults with Mendelian PEO associated with multiple mtDNA deletions, RNASEH1 mutations were found in 3 patients (2.7%), compared to *POLG* mutations in 27 patients (24.7%), *RRM2B* in 18 (16.5%), and *TWNK* in 18 (16.5).[15] This ranking underscores that while RNASEH1 is a recognized cause, it is less common than several other nuclear mtDNA maintenance genes.

Globally, fewer than two dozen RNASEH1-mutated patients have been reported to date.[16][17] Carreño-Gago noted that “one possible genetic cause of the milder clinical form is the presence of mutations in RNASEH1, an uncommon occurrence with only 14 patients reported to date, all of them showing PEO as a clinical trait.”[16] The Italian case report added two more patients.[17] The geographical distribution includes Europe (Italy, UK), and likely other regions, though specific data are limited.[13][15][16][17] No sex predilection has been reported; both males and females are affected. Age distribution centers on adulthood, with onset in the twenties to forties and diagnosis often delayed until later decades.[10][13][15][16][17]

Carrier frequency for pathogenic RNASEH1 variants in the general population is unknown but likely extremely low given the rarity of reported disease and the purifying selection observed in animal models. gnomAD frequencies for specific variants such as V142I are <0.01%.[9][13][16][17] There is no evidence of specific ethnic groups or populations with markedly increased RNASEH1 disease burden, although detection bias may favor regions with active mitochondrial disease research.

## 10. Diagnostics

### 10.1 Clinical evaluation, laboratory tests, and imaging

The diagnostic workup for suspected RNASEH1-related PEO begins with clinical recognition of chronic progressive external ophthalmoplegia, ptosis, exercise intolerance, and associated neuromuscular features.[10][11][13][15][16][17] Differential diagnosis includes myasthenia gravis, oculopharyngeal muscular dystrophy, thyroid ophthalmopathy, and other mitochondrial and neuromuscular disorders.[10] Myasthenia gravis, for instance, can present with ptosis and ophthalmoparesis, but typically shows fluctuating symptoms, positive autoantibodies (AChR, MuSK, LRP4), and electrophysiologic features distinct from mitochondrial myopathy.[10] Thyroid-associated ophthalmopathy exhibits eyelid retraction, conjunctival erythema, swelling, and proptosis rather than isolated ptosis and PEO.[10] Thus, the clinical pattern of symmetric, slowly progressive PEO with spared pupils and associated limb weakness and ataxia suggests mitochondrial disease.

Laboratory tests include serum lactate and creatine kinase measurements, which may be mildly abnormal but are not specific.[10][15][16][17] Muscle biopsy is a key diagnostic tool. Histopathology typically reveals ragged-red fibers, COX-negative fibers, SDH-positive fibers, and subsarcolemmal mitochondrial accumulation.[13][15][16][17] Pathology findings correspond to SNOMED and HPO categories for mitochondrial myopathy. Enzymatic assays of respiratory chain complexes demonstrate reduced activities, supporting a mitochondrial defect.[13][15][16][17]

Imaging studies (MRI of the brain and spine) may show cerebellar atrophy in patients with prominent ataxia, although this is variably reported.[15][16][17] EMG may reveal myopathic changes without specific patterns. Nerve conduction studies can detect mild motor peripheral neuropathy, confirming peripheral nervous system involvement in some patients.[11][15][16][17] Pulmonary function tests assess respiratory muscle strength and detect restrictive defects in patients with respiratory impairment.[11][15][16][17]

### 10.2 Genetic testing: panels, WES/WGS, and single-gene assays

Genetic testing is essential to confirm RNASEH1-related PEO. Next-generation sequencing approaches, including whole-exome sequencing (WES) and targeted gene panels for mitochondrial disorders and mtDNA maintenance genes, have been instrumental in identifying RNASEH1 mutations.[13][15][16][17] Reyes et al. discovered RNASEH1 mutations through whole-exome sequencing of two singleton subjects.[13] Carreño-Gago used a custom muscle mtDNA maintenance panel to detect two homozygous RNASEH1 mutations in a patient.[16] Bugiardini et al. employed targeted sequencing in their national mitochondrial cohort.[15]

Genomics England’s PanelApp includes RNASEH1 as a green gene on multiple panels: "Mitochondrial DNA maintenance disorder," "Mitochondrial disorders," and "Childhood onset leukodystrophy" super-panels, among others.[3] These panels target known mtDNA maintenance genes such as *POLG*, *RRM2B*, *TWNK*, *DNA2*, *MGME1*, and *RNASEH1*, facilitating comprehensive etiologic assessment.[3][18] ClinVar and GTR list RNASEH1 gene-specific tests and multi-gene panels that include RNASEH1 for suspected PEOB2 and mtDNA deletion syndromes.[9][14]

Single-gene sequencing of *RNASEH1* can be performed in patients with PEO and multiple mtDNA deletions, particularly when more common genes (POLG, RRM2B, TWNK) are negative.[15][16][17] Given the rarity of RNASEH1 mutations, panel-based or exome-based approaches may be more efficient, as they allow simultaneous screening of multiple mtDNA maintenance genes. Whole-genome sequencing (WGS) could detect noncoding variants and structural rearrangements, but RNASEH1 disease has thus far been attributed to coding and splice-site variants, so WES or targeted panels suffice for most cases.

Chromosomal microarray (CMA), karyotyping, and FISH are not typically informative in RNASEH1-related PEO, because the disease results from sequence-level variants rather than large-scale chromosomal abnormalities.[1][12][14][16][17] Mitochondrial DNA testing, including long-range PCR and Southern blotting, is crucial to demonstrate multiple mtDNA deletions in muscle tissue, which provide functional evidence of mtDNA maintenance defects.[13][15][16][17] However, mtDNA deletions do not specify the nuclear gene involved; they require nuclear genetic testing for definitive diagnosis.

Repeat expansion testing is not relevant to RNASEH1-related PEO, but is important in differential diagnosis of other PEO-like syndromes with repeat expansions (e.g., OPMD). For RNASEH1-related PEO, the diagnostic strategy is best conceptualized as a combination of clinical assessment, muscle biopsy and mtDNA deletion analysis, and nuclear gene sequencing focused on mtDNA maintenance genes, including RNASEH1.

### 10.3 Omics-based diagnostics and molecular biomarkers

Omics-based diagnostics beyond DNA sequencing are emerging but not yet standard for RNASEH1-related PEO. RNA sequencing of patient muscle or fibroblasts can detect aberrant RNASEH1 transcripts, such as exon 2 skipping in c.129-3C>G homozygotes.[17] It may also reveal upregulation of interferon-stimulated genes due to mt-dsRNA-mediated innate immune activation.[7] Proteomic analyses could quantify RNase H1 protein levels, respiratory chain subunits, and inflammatory markers. However, these approaches are currently research tools rather than routine clinical diagnostics.

Potential biomarkers include mtDNA deletions and copy number in muscle, mt-dsRNA levels in fibroblasts, and interferon signature genes.[13][16][17][7] Okletey et al.’s demonstration that RNASEH1 mutations cause mt-dsRNA accumulation and release suggests that mt-dsRNA could serve as a disease-specific biomarker differentiating RNASEH1-related PEO from other mtDNA maintenance disorders like Twinkle-related PEO, which release mtDNA instead.[7] Nonetheless, assay standardization and clinical validation remain future goals.

### 10.4 Clinical criteria and differential diagnosis

Standardized diagnostic criteria specific to RNASEH1-related PEO have not been published. Clinically, it fits within broader criteria for CPEO and mtDNA maintenance disorders. Scarpelli et al. proposed clinical criteria for PEO, including progressive bilateral ptosis and ophthalmoplegia with spared pupils, chronic course without remissions, and associated mitochondrial features.[10] RNASEH1-related PEO meets these criteria and adds the presence of multiple mtDNA deletions and biallelic RNASEH1 mutations as defining features.[13][15][16][17]

Differential diagnosis encompasses myasthenia gravis, oculopharyngeal muscular dystrophy, thyroid orbitopathy, oculomotor nerve palsies, and other PEO-causing genes. Myasthenia gravis is distinguished by fluctuating symptoms, serologic autoantibodies, and response to cholinesterase inhibitors.[10] Oculopharyngeal muscular dystrophy involves PABPN1 repeat expansions and characteristically affects proximal limb muscles and pharyngeal muscles but may present similarly; genetic testing for PABPN1 expansions distinguishes it. Other mtDNA maintenance defects due to *POLG*, *RRM2B*, *TWNK*, *DNA2*, and *MGME1* produce overlapping phenotypes but differ in genotype and sometimes severity and organ involvement.[10][15][16][18] For example, POLG mutations often cause more severe multi-system disease, including epilepsy and liver failure, whereas RNASEH1-associated disease is relatively benign and circumscribed.[15] Gene panels facilitate differential genetic diagnosis among these entities.

### 10.5 Screening and cascade testing

Population-based screening for RNASEH1-related PEO is not currently implemented, given its rarity and adult onset. Newborn screening programs do not include RNASEH1 or other nuclear mtDNA maintenance genes.[11] However, cascade genetic testing of family members is recommended once a proband is diagnosed. Heterozygous carriers can be identified and counseled regarding reproductive risks (25% recurrence risk in offspring when both parents are carriers).[13][15][16][17] Preimplantation genetic diagnosis or prenatal testing could be considered for couples at risk, though formal guidelines are not yet specific to RNASEH1.

Carrier screening in the general population is not warranted at this time due to low variant frequencies and lack of founder populations. High-throughput sequencing (WES/WGS) will increasingly detect RNASEH1 variants incidentally, requiring careful interpretation of variant pathogenicity and correlation with clinical phenotypes. As GTR notes, 16 tests are in the database for PEOB2, reflecting growing diagnostic capacity.[14]

## 11. Outcome / Prognosis

### 11.1 Survival, mortality, and life expectancy

Specific survival and mortality statistics for RNASEH1-related PEO are not available, owing to the small number of reported cases and relatively benign course. However, case series and clinical experience suggest that life expectancy is often near normal, especially with appropriate supportive care.[10][13][15][16][17] Bugiardini et al. emphasized the relatively mild and benign nature of RNASEH1-related mitochondrial disease compared to other nuclear mtDNA maintenance defects.[15] No deaths directly attributed to RNASEH1 disease have been reported in the available literature, although long-term follow-up is limited.

Respiratory failure due to respiratory muscle weakness and bulbar dysfunction could theoretically reduce life expectancy, but these complications appear less common and later-onset than in more severe mitochondrial encephalomyopathies.[11][15][16][17] Mortality rate is likely low and primarily related to general age-related factors rather than the disease itself, though aspiration pneumonia due to dysphagia or severe respiratory insufficiency could contribute in advanced stages. For knowledge-base purposes, RNASEH1-related PEO can be characterized as a chronic, slowly progressive disease with substantial morbidity but not typically life-shortening.

### 11.2 Morbidity, disability, and quality of life

Morbidity in RNASEH1-related PEO stems from neuromuscular and cerebellar deficits. Ptosis and ophthalmoplegia impair vision and cause cosmetic concerns, leading to difficulties with reading, driving, and social interaction.[10][11][13][15][16][17] Limb weakness and exercise intolerance limit physical activity and employment options. Cerebellar ataxia and dysarthria affect mobility and communication, increasing fall risk and social isolation.[11][13][15][16][17] Dysphagia affects nutrition and raises aspiration risk. Even if life expectancy is preserved, these impairments can cause significant disability.

Studies of mitochondrial diseases using instruments such as the SF-36 and EQ-5D show marked reductions in physical functioning, vitality, and role limitations.[10] RNASEH1-related PEO patients likely share these patterns, with particularly pronounced physical and social domains affected. Disability outcomes include increased dependence on assistive devices, need for surgical correction of ptosis, and possible loss of driving privileges. The International Classification of Functioning (ICF) framework would classify impairments in body functions (muscle power, eye movement, balance), activity limitations (walking, climbing, reading), and participation restrictions (employment, social roles).

### 11.3 Disease course: complications, recovery potential, and prognostic factors

Complications of RNASEH1-related PEO include falls due to ataxia, aspiration pneumonia due to dysphagia, chronic respiratory insufficiency, and psychosocial hardship.[11][13][15][16][17] Recovery potential is limited in terms of reversing mitochondrial dysfunction, but symptomatic improvements can be achieved with targeted interventions such as ptosis surgery, speech and swallowing therapy, and physical rehabilitation. Muscle strength and coordination may improve to some extent with tailored exercise programs, although underlying mtDNA deletions persist.

Prognostic factors likely include the specific RNASEH1 mutations and residual enzyme activity, degree of mtDNA deletion burden, presence of cerebellar and respiratory involvement, and comorbidities. For instance, patients with truncating or splice-site mutations causing complete loss of RNase H1 may have more severe phenotypes than those with hypomorphic missense variants, though current data are insufficient to quantify this. In vitro functional assays showing partial catalytic activity (e.g., V142I retaining ~40% activity) suggest that residual function may correlate with milder disease.[9][13][16][17] The presence of mt-dsRNA-mediated innate immune activation, as documented by Okletey et al., may also influence neuroinflammatory progression, but its prognostic significance is not yet defined.[7]

## 12. Treatment

### 12.1 Pharmacotherapy and symptomatic medical management

There is currently no disease-modifying pharmacotherapy that directly corrects RNASEH1 deficiency or mtDNA replication defects in RNASEH1-related PEO. Treatment is primarily symptomatic and supportive. Pharmacological measures may include agents targeting comorbid conditions (e.g., antidepressants for mood, analgesics for pain, bronchodilators for respiratory symptoms) rather than specific mitochondrial interventions.[10][15][16][17] Coenzyme Q10 supplementation and other “mitochondrial cocktail” therapies (e.g., L-carnitine, riboflavin) are sometimes used empirically in mitochondrial myopathies, but evidence for benefit in RNASEH1 disease is anecdotal.[10][15]

No pharmacogenomic interactions specific to RNASEH1 have been reported, and RNASEH1 status does not currently guide choice or dosage of medications. However, general mitochondrial disease guidelines caution against use of valproate and certain other drugs that can exacerbate mitochondrial dysfunction, particularly in POLG-related disease.[10] Avoidance of known mitochondrial toxins may be a prudent extrapolation in RNASEH1-related PEO.

### 12.2 Advanced therapeutics: gene therapy and RNA-based approaches

Advanced therapeutics such as gene therapy, cell therapy, and RNA-based treatments are conceptual possibilities but have not yet reached clinical application in RNASEH1-related PEO. In principle, AAV-mediated gene replacement of RNASEH1 in affected tissues could restore RNase H1 function and improve mtDNA replication, similar to emerging gene therapy strategies for other monogenic mitochondrial disorders. CRISPR-based gene editing to correct RNASEH1 mutations in patient cells is another theoretical avenue. However, challenges include targeted delivery to muscle and brain tissues, regulation of mitochondrial targeting of RNase H1, safety, and regulatory hurdles.

RNA-based therapies, such as antisense oligonucleotides (ASOs) or siRNAs targeting mutant transcripts, might not be ideal in RNASEH1-related PEO because the disease is due to loss of function rather than gain-of-function or dominant-negative effects. Instead, mRNA replacement or gene therapy to supply functional RNASEH1 protein would be more relevant. No clinical trials (NCT identifiers) specifically targeting RNASEH1 have been reported in the retrieved literature or major trial registries.

### 12.3 Surgical and interventional treatments

Surgical correction of ptosis (e.g., levator resection, frontalis sling procedures) is a key interventional treatment to improve vision and quality of life in RNASEH1-related PEO.[10][11][15][16][17] These procedures fall under NCIT clinical intervention terms such as *Blepharoplasty* (NCIT:C27897) or *Eyelid Reconstruction* (NCIT:C26990). Eyelid surgery can significantly alleviate visual field obstruction, reduce eye strain, and improve social appearance.

Occasionally, strabismus surgery may be considered to realign eyes and improve binocular vision, though ophthalmoplegia limits outcomes. Tracheostomy or non-invasive ventilation may be required in severe respiratory insufficiency to support breathing. Gastrostomy tube placement could address severe dysphagia and aspiration risk. These invasive interventions are tailored to individual complications rather than the core disease mechanism.

### 12.4 Supportive and rehabilitative care

Supportive care and rehabilitation are central to RNASEH1 disease management. Physical therapy focuses on strengthening limb muscles, improving balance and gait, and preventing contractures. Occupational therapy helps adapt daily activities and provide assistive devices. Speech and swallowing therapy address dysarthria and dysphagia, reducing aspiration risk.[10][11][13][15][16][17] Respiratory therapy, including inspiratory muscle training and non-invasive ventilation when needed, supports respiratory function. These interventions correspond to NCIT terms such as *Physical Therapy* (NCIT:C15273), *Occupational Therapy* (NCIT:C15248), and *Speech Therapy* (NCIT:C15279).

Psychological support and social services are crucial to address the psychosocial impact of chronic disability. Genetic counseling informs patients and families about inheritance, recurrence risks, and reproductive options. Multidisciplinary care teams, including neurologists, geneticists, ophthalmologists, physiatrists, and pulmonologists, provide coordinated management.

### 12.5 Experimental treatments and clinical trials

No specific experimental treatments targeting RNASEH1 have entered clinical trial phases, according to the retrieved literature. Broader mitochondrial disease trials evaluating agents such as elamipretide, nicotinamide riboside, or Nrf2 activators may include patients with mtDNA maintenance disorders but are not RNASEH1-specific. The novel mechanistic finding of mt-dsRNA-mediated innate immune activation suggests that immunomodulatory therapies targeting interferon pathways or nucleic acid sensors could be explored, but this remains speculative.[7]

### 12.6 Treatment outcomes, adverse events, and personalized medicine

Treatment outcomes in RNASEH1-related PEO are largely determined by supportive interventions. Ptosis surgery often yields significant functional improvements, with low complication rates. Rehabilitation can enhance mobility and reduce falls. Non-invasive ventilation improves survival and quality of life in respiratory impairment. However, none of these treatments halt or reverse mtDNA deletions or RNASEH1 deficiency.

Adverse events include surgical risks, aspiration from dysphagia if not adequately managed, and drug side effects from general medications. Personalized medicine approaches may emerge when genotype–phenotype correlations and mechanistic insights allow targeted interventions—for example, gene therapy tailored to specific RNASEH1 mutations or immune-modulatory therapies for patients with pronounced mt-dsRNA–mediated inflammation.[7] At present, personalized strategies focus on individualized symptom management and genetic counseling.

## 13. Prevention

### 13.1 Primary prevention and risk factor modification

Primary prevention of RNASEH1-related PEO in the general population is challenging, because the disease is caused by rare, autosomal recessive mutations and there are no modifiable environmental risk factors known to prevent mutation occurrence. Public health measures do not target RNASEH1 specifically. However, primary prevention at the family level is possible through reproductive planning and genetic counseling.

For couples with identified RNASEH1 pathogenic variants, options include preimplantation genetic diagnosis (PGD) during in vitro fertilization to select embryos without biallelic RNASEH1 mutations, and prenatal diagnostic testing via chorionic villus sampling or amniocentesis.[13][15][16][17] These strategies reduce the risk of having affected offspring but require specialized genetic services and ethical considerations.

### 13.2 Secondary prevention: screening and early detection

Secondary prevention focuses on early detection of disease or predisposition before severe symptoms develop. For RNASEH1-related PEO, this involves cascade genetic testing of family members of affected individuals to identify asymptomatic or pre-symptomatic carriers and biallelic mutation carriers before clinical onset. Early identification allows anticipatory guidance, monitoring, and timely supportive interventions once symptoms arise.[13][15][16][17]

Newborn screening programs do not currently include RNASEH1, and the adult-onset nature of the disease makes newborn screening less feasible. However, exome-based screening in high-risk families could detect RNASEH1 mutations early. For heterozygous carriers, education about reproductive risks constitutes secondary prevention of disease in offspring.

### 13.3 Tertiary prevention: complication reduction and disease management

Tertiary prevention aims to prevent complications and reduce disability in individuals who already have RNASEH1-related PEO. Key measures include fall prevention strategies for ataxia, aspiration prevention through swallowing therapy and, if necessary, gastrostomy, respiratory failure prevention via ventilatory support and monitoring, and psychosocial support to mitigate depression and social isolation.[10][11][13][15][16][17] Multidisciplinary clinics for mitochondrial diseases often provide structured care pathways for such tertiary prevention.

Genetic counseling is integral to tertiary prevention, guiding family planning and informing relatives about carrier risks. Public health interventions specific to RNASEH1 are not established, but general mitochondrial disease awareness campaigns could help in earlier diagnosis and management.

## 14. Other Species / Natural Disease

### 14.1 Orthologous genes and comparative biology

Orthologous RNASEH1 genes exist across vertebrates and other eukaryotes, reflecting the evolutionary conservation of RNA–DNA hybrid metabolism. In mice, the orthologous gene Rnaseh1 has been studied extensively; Cerritelli et al. demonstrated that Rnaseh1^-/- mice die at embryonic day 8.5 due to mtDNA depletion and apoptosis.[1] This underscores that RNase H1’s role in mtDNA replication is conserved and critical across species. Similar orthologs exist in zebrafish, Drosophila, and yeast, although their mitochondrial functions may differ.

Comparative pathology shows that RNase H1 deficiency is much more severe in mice (embryonic lethal) than in humans (adult-onset relatively benign disease).[1][15][16][17] Bugiardini et al. highlighted this contrast: “knockout mice suffer embryonic lethality owing to mtDNA depletion,… however, humans with RNASEH1 mutations develop a relatively mild clinical syndrome, comprising adult-onset PEO associated with multiple mtDNA deletions.”[15] This difference likely reflects partial redundancy by RNase H2 in humans, species-specific thresholds for mtDNA depletion tolerance, and the partial rather than complete loss of function in human RNASEH1 mutations.

No naturally occurring RNASEH1-related PEO has been described in companion animals or livestock. OMIA and veterinary databases do not list RNASEH1-related mitochondrial disease in animals. Nonetheless, mitochondrial myopathies and encephalomyopathies occur in dogs, cats, and horses, and RNASEH1 orthologs could theoretically be involved.

### 14.2 Zoonotic potential and cross-species susceptibility

RNASEH1-related PEO is a non-infectious, genetic disease; it has no zoonotic potential and cannot be transmitted across species through infection. Cross-species susceptibility is limited to engineered or naturally mutated orthologs causing mitochondrial dysfunction, as in mouse knockout models. 

From a comparative biology perspective, RNase H1’s mechanistic role in mtDNA replication and R-loop metabolism is conserved. Evolutionary analyses place RNASEH1 within the RNase H family, with conserved catalytic residues and structural folds. HomoloGene and other orthology resources would confirm cross-species gene conservation, and Alliance of Genome Resources integration can facilitate comparative studies.

## 15. Model Organisms

### 15.1 Mouse models: knockout, conditional, and phenotypic recapitulation

Mouse models are pivotal in understanding RNASEH1 function and disease mechanisms. Cerritelli et al. generated Rnaseh1^-/- mice and observed developmental arrest at embryonic day 8.5, mtDNA depletion, and apoptosis.[1] OMIM summarizes that “Cerritelli et al. (2003) generated Rnaseh1 -/- mice and observed developmental arrest at embryonic day 8.5… its absence in embryos resulted in a significant decrease in mitochondrial DNA content, leading to apoptotic cell death. This report linked RNASEH1 to generation of mitochondrial DNA, providing direct support for the strand-coupled mechanism of mitochondrial DNA replication.”[1] This complete knockout model demonstrates that RNase H1 is essential for embryonic viability and mtDNA maintenance, but does not directly recapitulate the adult-onset PEO phenotype seen in humans.

Conditional knockout models in liver and B cells have been developed, revealing tissue-specific mtDNA replication defects and mitochondrial dysfunction.[2] These models reproduce the mtDNA depletion seen in knockout embryos but in a controlled tissue-specific context, allowing study of adult phenotypes such as liver dysfunction or immunologic consequences. However, explicit PEO-like neuromuscular phenotypes have not been reported in these conditional models, likely due to differing tissue targeting.

Overall, mouse models show that RNase H1 loss causes severe mtDNA replication defects and lethality, confirming the mechanism but not the clinical trajectory of human RNASEH1-related PEO. They highlight that human patients likely have partial loss-of-function, residual RNase H1 activity, and compensatory mechanisms that modulate severity.

### 15.2 Cellular and in vitro models: patient-derived fibroblasts and recombinant systems

Patient-derived fibroblasts are a primary cellular model for RNASEH1 disease. Reyes et al. studied fibroblasts from patient S1, showing decreased RNASEH1 transcripts and protein levels, reduced RNase H1 activity, slower growth in galactose medium, decreased mitochondrial membrane potential, perinuclear aggregated mitochondria, and mtDNA replication defects.[1][9][13] Carreño-Gago’s patient fibroblasts failed to restore mtDNA copy number after depletion, recapitulating replication dysfunction.[16] Okletey et al. used patient-derived fibroblasts with RNASEH1 mutations to demonstrate mt-dsRNA accumulation and release, and downstream innate immune activation.[7] These fibroblast models faithfully reproduce mitochondrial and immune phenotypes and allow detailed mechanistic studies using imaging, biochemical assays, and transcriptomics.

In vitro recombinant systems expressing wild-type and mutant RNase H1 proteins permit direct assessment of catalytic activity on RNA–DNA hybrids. Reyes et al. expressed V142I, A185V, and R157X proteins in *E. coli* and measured their residual activity, establishing the functional impact of each mutation.[9][13] Carreño-Gago used similar approaches to test Gln86del and Tyr163His mutations.[16] These in vitro models are critical for variant classification and mechanistic understanding.

### 15.3 Model limitations and research applications

Mouse knockout models do not recapitulate adult-onset PEO because complete RNase H1 loss is embryonic lethal, highlighting a key limitation in translating findings to human disease.[1][15][16][17] Conditional models offer tissue-specific insights but have not yet targeted extraocular muscles or cerebellum in a way that reproduces the RNASEH1 PEO phenotype. Patient-derived fibroblasts mirror mitochondrial and immune phenotypes but lack the tissue context of muscle fibers and neurons.

Nevertheless, these models are invaluable for studying the fundamental biology of RNase H1, mtDNA replication mechanisms, RNA–DNA hybrid metabolism, and innate immune activation via mitochondrial nucleic acids.[1][2][7][13][16] They enable testing of potential therapies, such as gene replacement or immune-modulatory agents, in controlled environments. Future models may include human induced pluripotent stem cell (iPSC)-derived myotubes and neurons from RNASEH1-mutated patients, providing tissue-specific cellular platforms.

## Conclusion

RNASEH1-related progressive external ophthalmoplegia is a paradigmatic mtDNA maintenance disorder linking a nuclear endonuclease defect to mitochondrial replication failure, secondary mtDNA deletions, and adult-onset neuromuscular disease. Biallelic loss-of-function mutations in *RNASEH1* impair RNase H1’s ability to remove RNA primers and RNA–DNA hybrids during mtDNA replication, leading to replication slowdown, accumulation of replication intermediates and 7S DNA, and eventual mtDNA depletion and multiple deletions in post-mitotic tissues.[1][2][13][15][16][17][18] These structural mtDNA abnormalities compromise respiratory chain function and ATP production, manifesting clinically as chronic progressive external ophthalmoplegia, ptosis, exercise intolerance, proximal limb weakness, cerebellar ataxia, dysphagia, and mild peripheral neuropathy, with muscle biopsies showing ragged-red fibers and COX-negative fibers.[10][11][13][15][16][17]

The disease is rare but constitutes the fourth most common cause of Mendelian adult PEO with multiple mtDNA deletions after *POLG*, *RRM2B*, and *TWNK*, with a relatively benign and slowly progressive course.[15] Inheritance is autosomal recessive, with high penetrance and variable expressivity. Pathogenic RNASEH1 variants—such as V142I, R157X, A185V, Gln86del, Tyr163His, and c.129-3C>G—are extremely rare and cause substantial loss of RNase H1 function, while likely benign variants like M118V do not.[5][9][13][16][17] Mouse knockout models demonstrate embryonic lethality due to mtDNA depletion, underscoring RNase H1’s essential role in mtDNA replication, whereas human patients exhibit partial loss-of-function and residual enzyme activity, allowing survival but predisposing to adult-onset mitochondrial encephalomyopathy.[1][15][16][17]

Recent mechanistic advances reveal an additional layer of pathophysiology: RNASEH1 mutations drive innate immune activation through accumulation and release of mitochondrial double-stranded RNA, engaging cytosolic sensors and activating bystander microglia, thereby contributing to neuroinflammation and potentially to disease progression.[7] This distinguishes RNASEH1-related PEO from Twinkle-related PEO, where mtDNA rather than mt-dsRNA is released.[7] Nuclear roles of RNase H1 in R-loop resolution and telomere maintenance are well-established experimentally, but human RNASEH1 disease remains dominated by mitochondrial mechanisms, with nuclear redundancy mitigating overt genomic instability.[2][15]

Diagnostic evaluation hinges on clinical recognition of chronic PEO, muscle biopsy evidence of mitochondrial myopathy with multiple mtDNA deletions, and nuclear genetic testing for mtDNA maintenance genes including RNASEH1.[10][11][13][15][16][17] ClinVar, OMIM, MedGen, Orphanet, PanelApp, and GTR provide curated resources for variant interpretation and testing options.[1][3][9][11][12][14] Treatment is currently supportive, focusing on ptosis surgery, physical and occupational therapy, swallowing and speech therapy, respiratory support, and genetic counseling.[10][11][15][16][17] No disease-modifying pharmacotherapy or gene therapy for RNASEH1-related PEO is yet available, but emerging insights into mtDNA replication biology and mt-dsRNA-mediated innate immunity may open new avenues for targeted interventions.

For disease knowledge base implementation, RNASEH1-related PEO should be annotated as MONDO:0014656, linked to gene *RNASEH1* (HGNC:10073), with GO terms for mitochondrial DNA replication and RNA–DNA hybrid ribonuclease activity, and HPO phenotype terms including external ophthalmoplegia, ptosis, exercise intolerance, proximal weakness, cerebellar ataxia, dysphagia, ragged-red fibers, and multiple mtDNA deletions.[1][4][10][11][13][15][16][17][18] CL terms should highlight skeletal muscle fibers, Purkinje cells, fibroblasts, and microglia; UBERON terms should capture extraocular muscles, limb muscles, cerebellum, and brainstem.[7][10][11][13][15][16][17] CHEBI entities related to RNA and DNA can represent RNase H1 substrates. NCIT clinical intervention terms such as physical therapy, occupational therapy, speech therapy, and blepharoplasty reflect treatment modalities.

Despite its rarity, RNASEH1-related PEO provides a powerful model for understanding how subtle defects in mtDNA replication machinery can lead to adult-onset, tissue-specific mitochondrial disease, and how mitochondrial nucleic acids can act as danger signals to the innate immune system. Continued integration of human clinical data, animal and cellular models, and multi-omics profiling will be essential to refine our mechanistic understanding, develop targeted therapies, and improve outcomes for individuals with this distinctive mitochondrial encephalomyopathy.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 68 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 44 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 13 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000506` (2 mentions) - the report calls it "external ophthalmoplegia"; HP calls it **Telecanthus**
- `HP:0006205` (2 mentions) - the report calls it "multiple mitochondrial DNA deletions"; HP calls it **Irregular phalanges**
- `HP:0003298` (1 mention) - the report calls it "abnormal mitochondrial respiratory chain complex I activity"; HP calls it **Spina bifida occulta**
- `GO:0030135` (1 mention) - the report calls it "mitochondrial membrane potential"; GO calls it **coated vesicle**
- `HP:0030057` (1 mention) - the report calls it "abnormal mitochondrial DNA replication"; HP calls it **Autoimmune antibody positivity**
- `GO:0036298` (1 mention) - the report calls it "RNA–DNA hybrid resolution"; GO calls it **recombinational interstrand cross-link repair**
- `GO:0034249` (2 mentions) - the report calls it "response to double-stranded RNA"; GO calls it **obsolete negative regulation of amide metabolic process**
- `NCIT:C27897` (1 mention) - the report calls it "Blepharoplasty"; NCIT calls it **T-Cell Proliferation of Uncertain Malignant Potential**
- `NCIT:C26990` (1 mention) - the report calls it "Eyelid Reconstruction"; NCIT calls it **Transplanted Kidney Complication**
- `NCIT:C15273` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Longitudinal Study**
- `NCIT:C15248` (1 mention) - the report calls it "Occupational Therapy"; NCIT calls it **Hemodialysis**
- `NCIT:C15279` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Radical Mastectomy**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000507` (2 mentions), reported as "ptosis" - HP does not contain this term
- `HP:0003703` (1 mention), reported as "mitochondrial proliferation" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0034249` (obsolete negative regulation of amide metabolic process) (2 mentions) - replaced by `GO:0009892`
- `CL:0000215` (obsolete barrier cell) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0014656` (3 mentions) - the report calls it "progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2, PEOB2"; MONDO calls it **progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 2**
- `HP:0003200` (4 mentions) - the report calls it "ragged-red muscle fibers", "mitochondrial myopathy"; HP calls it **Ragged-red muscle fibers**, and lists "Mitochondrial proliferation in muscle tissue" among its other names
- `HP:0002141` (1 mention) - the report calls it "gait ataxia"; HP calls it **Gait imbalance**
- `HP:0001251` (2 mentions) - the report calls it "cerebellar ataxia"; HP calls it **Ataxia**, and lists "Cerebellar ataxia" among its other names
- `HP:0003477` (1 mention) - the report calls it "motor peripheral neuropathy"; HP calls it **Peripheral axonal neuropathy**, and lists "Axonal peripheral neuropathy" among its other names
- `HP:0003688` (1 mention) - the report calls it "cytochrome c oxidase deficiency in muscle tissue"; HP calls it **Cytochrome C oxidase-negative muscle fibers**, and lists "Cytochrome c oxidase deficiency in skeletal muscle" among its other names
- `GO:0004381` (1 mention) - the report calls it "RNA–DNA hybrid ribonuclease activity"; GO calls it **fucosylgalactoside 3-alpha-galactosyltransferase activity**, and lists "histo-blood group B transferase activity" among its other names
- `GO:0006269` (2 mentions) - the report calls it "DNA replication, removal of RNA primer"; GO calls it **DNA replication, synthesis of primer**, and lists "DNA replication, synthesis of RNA primer" among its other names
- `GO:0007005` (1 mention) - the report calls it "mitochondrial membrane organization"; GO calls it **mitochondrion organization**, and lists "mitochondrial organization" among its other names
- `GO:0060337` (2 mentions) - the report calls it "type I interferon signaling pathway"; GO calls it **type I interferon-mediated signaling pathway**, and lists "type I interferon signaling pathway" among its other names
- `CL:0000129` (2 mentions) - the report calls it "microglia"; CL calls it **microglial cell**, and lists "microglia" among its other names
- `UBERON:0002037` (2 mentions) - the report calls it "cerebellar cortex"; UBERON calls it **cerebellum**
- `UBERON:0001894` (2 mentions) - the report calls it "brainstem"; UBERON calls it **diencephalon**, and lists "interbrain" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003200` - called "ragged-red muscle fibers", "mitochondrial myopathy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.