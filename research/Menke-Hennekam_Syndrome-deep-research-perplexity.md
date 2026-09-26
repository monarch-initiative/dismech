---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-25T10:49:23.393904'
end_time: '2026-09-25T10:56:13.786519'
duration_seconds: 410.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Menke-Hennekam Syndrome
  mondo_id: MONDO:0020774
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
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 70
  verified: 61
  not_found: 0
  obsolete: 4
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 46
  labels_matching: 23
  labels_mismatched: 16
  mislabelled_terms:
  - term_id: NCIT:C16084
    reported_labels:
    - Supportive Care
    ontology_label: Observational Study
  - term_id: NCIT:C48676
    reported_labels:
    - Developmental Therapy
    ontology_label: Schedule III Substance
  - term_id: NCIT:C15661
    reported_labels:
    - Anticonvulsant Therapy
    ontology_label: ATCC
  - term_id: NCIT:C17358
    reported_labels:
    - Biomarker
    ontology_label: DCC Gene
  - term_id: NCIT:C10604
    reported_labels:
    - DNA Methylation Analysis
    ontology_label: Cisplatin/Cyclophosphamide/Paclitaxel
  - term_id: NCIT:C12219
    reported_labels:
    - Lifestyle Factor
    ontology_label: Anatomic Structure, System, or Substance
  - term_id: NCIT:C16916
    reported_labels:
    - Behavioral Intervention
    ontology_label: Niger
  - term_id: UBERON:0003114
    reported_labels:
    - craniofacial skeleton
    ontology_label: pharyngeal arch 3
  - term_id: UBERON:0000020
    reported_labels:
    - auditory system
    - ear
    ontology_label: sense organ
  - term_id: UBERON:0001733
    reported_labels:
    - nasal cavity
    ontology_label: soft palate
  - term_id: UBERON:0000984
    reported_labels:
    - testis
    ontology_label: imaginal disc-derived wing
  - term_id: NCIT:C614
    reported_labels:
    - Antidepressant
    ontology_label: Lidocaine
  - term_id: NCIT:C780
    reported_labels:
    - Antipsychotic
    ontology_label: Attenuated Corynebacterium Parvum
  - term_id: NCIT:C21015
    reported_labels:
    - Gastrostomy
    ontology_label: BMP/Retinoic Acid-Inducible Neural-Specific Protein 1
  - term_id: NCIT:C15273
    reported_labels:
    - Physical Therapy
    ontology_label: Longitudinal Study
  - term_id: NCIT:C17561
    reported_labels:
    - Speech Therapy
    ontology_label: Fusion Protein
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0016573
    ontology_label: obsolete histone acetylation
  - term_id: HP:0000735
    ontology_label: obsolete Impaired social interactions
    replaced_by: HP:0012760
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  - term_id: PR:000004536
    ontology_label: obsolete ATP-binding cassette sub-family A member 8
    replaced_by: PR:000003546
  unresolvable_prefixes:
  - ORPHA
  - HSA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Menke-Hennekam Syndrome
- **MONDO ID:** MONDO:0020774 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Menke-Hennekam Syndrome** covering all of the
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

# Menke-Hennekam Syndrome: Comprehensive Disease Characteristics and Molecular Pathophysiology

Menke-Hennekam syndrome (MKHK) is a very rare autosomal dominant neurodevelopmental disorder caused by pathogenic missense and in-frame indel variants in highly conserved domains within exons 30 and 31 of the **CREBBP** and **EP300** genes, which encode the histone acetyltransferases CBP and p300.[1][2][3][4][5][6][7][10] Although these same genes, when affected by loss-of-function variants or deletions, cause Rubinstein–Taybi syndrome (RSTS), MKHK constitutes a clinically and mechanistically distinct entity characterized by variable intellectual disability, developmental delay, autistic behavior, short stature, microcephaly, feeding difficulties, recurrent airway infections, hearing impairment, and distinctive facial dysmorphism without the broad thumbs and halluces typical of RSTS.[1][2][5][6][8][9][10][11][17] Recent work has demonstrated that MKHK is best understood as a set of **domain-specific subtypes** (MKHK-ZZ, MKHK-TAZ2, and MKHK-ID4) rather than gene-specific (CREBBP versus EP300), with each domain-associated subtype showing characteristic clinical patterns and distinct DNA methylation episignatures.[3][4] This report synthesizes current knowledge on MKHK—its clinical spectrum, genetic and epigenetic basis, mechanistic pathways, diagnostics, epidemiology, prognosis, and management—drawing primarily on case series, curated databases (OMIM, Orphanet, ClinVar, Simons Searchlight), and a recent domain-resolved epigenomic study, and frames this information in formal ontological terms (MONDO, HPO, GO, CL, UBERON, NCIT) suitable for computational disease knowledge bases.[1][2][3][4][5][6][10][11][13][14][16][17]  

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Menke-Hennekam syndrome is a rare multiple congenital anomalies/neurodevelopmental syndrome caused by specific variants in the **CREBBP** or **EP300** genes, presenting with variable intellectual disability, developmental delay, autistic behavior, short stature, microcephaly, and a constellation of craniofacial dysmorphic features.[1][2][10][11] Orphanet defines MKHK as “a rare genetic multiple congenital anomalies/dysmorphic syndrome characterized by variable intellectual disability, developmental delay, autistic behavior, short stature, and microcephaly” and notes additional manifestations such as feeding problems, vision and hearing impairments, recurrent upper airway infections, epilepsy, cryptorchidism, and cerebral anomalies, as well as characteristic facial features including short upslanted palpebral fissures, ptosis, telecanthus, depressed nasal ridge, short nose with anteverted nares, short columella, and long philtrum.[11][12] OMIM further specifies two gene-based subtypes—Menke-Hennekam syndrome 1 (MKHK1; MIM 618332) due to CREBBP variants on chromosome 16p13.3 and Menke-Hennekam syndrome 2 (MKHK2; MIM 618333) due to EP300 variants on chromosome 22q13.2—both restricted to exons 30–31 and clinically distinct from Rubinstein–Taybi syndrome type 1 and 2 (RSTS1, RSTS2).[1][2]

The syndrome was delineated as a distinct clinical entity in the mid-2010s, when Menke and colleagues described individuals with CREBBP or EP300 exon 30/31 variants who did not resemble RSTS but shared a recognizable phenotype of developmental delay, autistic behaviors, growth deficiency, and facial dysmorphism.[5][7] Subsequent case aggregation and functional interpretation established MKHK as an autosomal dominant congential disorder, usually detected in infancy or early childhood, with wide variability in cognitive outcome but a fairly consistent pattern of craniofacial and growth features.[1][2][5][7][8][11][17] It is now recognized in rare disease classification systems as a distinct syndrome that sits within the broader spectrum of CBP/p300-related neurodevelopmental disorders and chromatin remodeling disorders.[9][10][15][18]

### 1.2 Key Identifiers and Ontological Mapping

Multiple standardized identifiers are associated with Menke-Hennekam syndrome, allowing integration into biomedical ontologies and disease registries. OMIM assigns Menke-Hennekam syndrome 1 (autosomal dominant, CREBBP-related) the entry MIM **618332** and Menke-Hennekam syndrome 2 (autosomal dominant, EP300-related) the entry MIM **618333**, both specifically annotated as “Menke-Hennekam syndrome” caused by heterozygous mutations in exons 30 or 31 of the respective genes.[1][2] Orphanet lists Menke-Hennekam syndrome under **ORPHA:592574** and classifies it among rare genetic diseases with multiple congenital anomalies and intellectual disability.[11][15][18] The KEGG DISEASE database registers MKHK under **H02650**, with causal genes CREBBP (MKHK1; HSA:1387) and EP300 (MKHK2; HSA:2033), and notes an ICD-11 code **LD2F.1Y** linked to the syndrome.[10]

ClinVarMiner aggregates clinically interpreted variants for Menke-Hennekam syndrome under the MONDO condition “Menke-Hennekam syndrome” and reports 388 variants across CREBBP and EP300, with 14 classified as pathogenic and 24 as likely pathogenic.[13] The MONDO ontology term associated with this ClinVar disease entry is MONDO:0020774 (Menke-Hennekam syndrome), which provides a unified cross-reference linking OMIM, Orphanet, and other terminologies; ClinVarMiner explicitly indicates a MONDO condition identifier “20774,” consistent with this mapping.[13] At present, MKHK does not have a distinct MeSH heading, and ICD-10 does not include a specific code; affected individuals are typically coded under broad categories such as “Other specified congenital malformation syndromes affecting multiple systems,” but ICD-11 has begun to assign a more granular code.[10][11]

In ontological terms relevant to knowledge-base construction, MKHK corresponds to a Mendelian, autosomal dominant, congenital neurodevelopmental disease (MONDO:0020774), with primary phenotypes mapped to HPO concepts including **intellectual disability** (HP:0001249), **global developmental delay** (HP:0001263), **autistic behavior** (HP:0000729), **short stature** (HP:0004322), **microcephaly** (HP:0000252), **feeding difficulties in infancy** (HP:0008872), **hearing impairment** (HP:0000365), and **epilepsy** (HP:0001250).[11][12] The causal genes map to HGNC entries **CREBBP** (HGNC:2348) and **EP300** (HGNC:3373), histone acetyltransferases with GO annotations related to transcriptional coactivation and histone acetylation, particularly **GO:0016573** (histone acetylation), **GO:0006357** (regulation of transcription from RNA polymerase II promoter), and **GO:0003713** (transcription coactivator activity).[4][7][9][10]

### 1.3 Synonyms and Alternative Names

A range of synonyms and alternative names are used in the clinical and research literature for Menke-Hennekam syndrome. The most common formulations are “Menke-Hennekam syndrome” and the subtype-specific “Menke-Hennekam syndrome 1” (MKHK1) and “Menke-Hennekam syndrome 2” (MKHK2), corresponding to CREBBP- and EP300-related forms respectively.[1][2][10][11][17] Simons Searchlight refers to “EP300-related syndrome,” noted to be “also called Rubinstein-Taybi syndrome 2 and Menke-Hennekam syndrome-2,” reflecting that EP300 variants across the gene body can cause either classic RSTS2 (usually via haploinsufficiency) or MKHK2 (via exon 30/31-specific missense/in-frame variants).[6][17] Japanese clinical genetics resources similarly refer to “メンケ・ヘネカム症候群1型” (Menke-Hennekam syndrome type 1) and “メンケ・ヘネカム症候群2型” (type 2), emphasizing their distinction from “ルビンスタイン・テイビ症候群1型/2型” (Rubinstein–Taybi syndromes 1 and 2).[8][9][17]

Within the mechanistic and epigenomic literature, MKHK has also been subdivided into **MKHK-ZZ**, **MKHK-TAZ2**, and **MKHK-ID4**, referring to the specific protein domains within CBP/p300 (ZZ zinc finger, TAZ2 transcriptional adaptor zinc-binding domain, and an intrinsically disordered region designated ID4) that are affected by the pathogenic variants.[3][4] These domain-based labels supplement the gene-based terminology and underline the current understanding that MKHK is fundamentally domain-specific rather than gene-specific. In some legacy reports, individuals were initially described as having “atypical Rubinstein–Taybi syndrome” before the distinct MKHK phenotype was recognized.[5][7] As knowledge has expanded, however, the use of “Menke-Hennekam syndrome” as a primary diagnostic label has become standard in OMIM, Orphanet, KEGG, and clinical genetics resources.[1][2][10][11][17]

### 1.4 Nature and Source of Disease Information

The information underlying current descriptions of Menke-Hennekam syndrome is derived largely from aggregated, disease-level resources that compile data from individual case reports and small case series, rather than from large, population-based epidemiologic cohorts or EHR-driven studies. The initial delineation of MKHK came from exome sequencing in clinical genetics cohorts, where patients with neurodevelopmental syndromes lacking a RSTS phenotype were found to carry CREBBP/EP300 exon 30/31 variants.[5][7] Menke et al. published early series in 2016 and 2018 describing phenotypic features and genotype–phenotype specificity in these individuals, and these primary papers underpin the OMIM entries that formally distinguish MKHK1 and MKHK2 from RSTS1 and RSTS2.[1][2][5][7][14][16]

Orphanet’s disease definition is based on compiled case reports and expert curation, rather than on systematic EHR-derived phenotyping.[11][12][15] KEGG’s disease entry similarly summarizes mechanistic and clinical features from the genetics literature.[10] ClinVar and ClinVarMiner provide variant-level pathogenicity assessments based on submissions from clinical laboratories and research groups, but the associated phenotypic descriptors are largely drawn from individual patients tested in these contexts.[13][14][16] Simons Searchlight’s EP300 gene guide aggregates clinical observations from an international cohort of individuals with EP300-related conditions, including MKHK2, but as of 2024, the total number of clinically ascertained EP300-related cases is 214, reflecting the rarity of these disorders.[6] Finally, a recent 2024 study on “Menke-Hennekam syndrome; delineation of domain-specific subtypes with distinct clinical and DNA methylation profiles” used a cohort of individuals with exon 30/31 CREBBP/EP300 variants and employed epigenomic profiling to refine phenotypic subtypes and develop diagnostic episignatures.[3][4]

In summary, MKHK knowledge is currently anchored in aggregated disease-level resources built from relatively small numbers of individual clinical cases, complemented by mechanistic insights from molecular biology of CBP/p300 and epigenetic profiling approaches.[3][4][5][7][9][10] Large-scale registry or EHR-based data are not yet available, which limits precise estimates of prevalence, penetrance, and long-term outcomes, but the existing curated resources provide a robust qualitative picture of the syndrome useful for computational disease modeling and clinical decision support.[1][2][6][10][11][13][17]

## 2. Etiology, Causal Factors, and Risk Profiles

### 2.1 Primary Causal Factors: Genetic Basis

Menke-Hennekam syndrome is fundamentally a **genetic disease** caused by germline heterozygous variants in the **CREBBP** or **EP300** genes, specifically missense or in-frame deletion variants clustered in exons 30 and 31.[1][2][3][4][5][7][8][9][10][17] OMIM uses a number sign (#) with its entries 618332 and 618333 to indicate that MKHK1 and MKHK2 are molecularly defined disorders, “because of evidence that [MKHK1] is caused by heterozygous mutation in exon 30 or 31 of the CREBBP gene… [and MKHK2] by heterozygous mutations in exon 30 or 31 of the EP300 gene.”[1][2] These exons encode conserved C-terminal domains of CBP/p300 involved in transcription factor binding and regulatory interactions, and variants outside this region typically cause Rubinstein–Taybi syndrome through loss-of-function mechanisms.[1][2][4][7][9][10]

MedlinePlus Genetics notes for EP300 that “mutations in the EP300 gene are a very rare cause of a condition called Menke-Hennekam syndrome… The EP300 gene mutations that cause Menke-Hennekam syndrome occur in regions of the gene known as exon 30 or exon 31… Researchers suggest that these changes give the altered protein a new function, which disrupts development and causes the signs and symptoms of Menke-Hennekam syndrome.”[5] Japanese clinical genetics explanations emphasize that MKHK1 “is caused by mutations occurring in a limited region, exons 30–31 of the CREBBP gene,” and that this mechanism differs from RSTS1, which results from haploinsufficiency (gene dosage reduced to half) due to loss-of-function variants or deletions.[8][9] For EP300, MKHK2 similarly arises from exon 30–31-specific missense or small in-frame deletions, in contrast to RSTS2 caused by variants that reduce p300 levels via haploinsufficiency.[17]

In the most comprehensive recent study, Menke et al. collected individuals with CREBBP or EP300 variants affecting specific functional domains within exons 30 and 31 and classified them into three domain-specific MKHK subtypes, MKHK-ZZ, MKHK-TAZ2, and MKHK-ID4, each linked to distinct clinical and DNA methylation profiles.[3][4] This work underscored that MKHK is **domain-specific**, meaning that variants in the same domain, whether in CREBBP or EP300, produce similar phenotypes, whereas gene identity per se (CREBBP versus EP300) is less critical.[3][4] The germline origin of these variants is demonstrated by familial segregation in some cases, but most reported variants are **de novo**, arising for the first time in the affected individual’s germline, which is consistent with the sporadic occurrence and extreme rarity of the syndrome.[6][8][16][17]

ClinVar entries for specific CREBBP MKHK1 variants, such as NM_004380.3:c.5602C>T (p.Arg1868Trp) and NM_004380.3:c.5615T>C (p.Met1872Thr), classify them as pathogenic based on multiple submissions and literature evidence, and note that these variants have been discovered in unrelated individuals with MKHK1 and are often demonstrated to be **de novo**.[14][16] For example, p.Met1872Val, a related CREBBP variant at the same codon, has been “reported eight times as pathogenic or likely pathogenic and has been demonstrated to be de novo in six affected individuals,” supporting a strong causal link.[16] ClinVarMiner reports that most variants submitted for Menke-Hennekam syndrome in CREBBP and EP300 are missense, with pathogenic/likely pathogenic variants concentrated in the exon 30–31 region, which aligns with the domain-specific mechanism.[13]

Taken together, MKHK is unequivocally a Mendelian, autosomal dominant, **monogenic** disorder caused by germline heterozygous missense or small in-frame deletion variants confined to exons 30–31 of CREBBP or EP300, acting through altered function of CBP/p300 rather than gene dosage reduction.[1][2][3][4][5][8][9][10][16][17] This etiologic clarity is one of the distinctive strengths of MKHK as a disease model for understanding domain-specific effects within chromatin regulator genes.

### 2.2 Risk Factors: Genetic and Environmental Considerations

Within the genetic framework, the primary “risk factor” for Menke-Hennekam syndrome is **inheritance of a pathogenic exon 30/31 variant in CREBBP or EP300 from an affected parent**, in the context of autosomal dominant transmission.[1][2][6][8][9][17] Simons Searchlight emphasizes that “EP300-related syndrome is an autosomal dominant genetic condition. This means that when a person has the one damaging variant in EP300 they will likely have symptoms… For someone with an autosomal dominant genetic syndrome, every time they have a child there is a 50 percent chance they pass on the same genetic variant and a 50 percent chance they do not.”[6] Japanese resources similarly explain for MKHK1 and MKHK2 that, in theory, “the variant is inherited from parent to child with a 50% probability,” although in practice most cases appear to be de novo.[8][17] Thus, the **family history of MKHK or other CBP/p300-related syndromes** can act as a genetic risk factor for recurrence in offspring, and this is crucial information for genetic counseling.

However, the majority of reported MKHK cases arise from **de novo mutations**, i.e., germline changes that occur spontaneously in the parental gametes or early zygote, without being present in either parent’s somatic DNA.[6][8][16][17] Simons Searchlight notes that “research shows that EP300-related syndrome is often the result of a de novo variant in EP300… Many parents who have had their genes tested do not have the EP300 genetic variant found in their child… No parent causes their child’s EP300-related syndrome… nothing a parent does before or during the pregnancy causes this to happen.”[6] Minerva Clinic echoes this for MKHK1, stating that most cases are de novo and that there is no evidence that parental behavior or exposures cause these mutations.[8] Therefore, for most families, there is no identifiable modifiable risk factor; MKHK occurs sporadically due to stochastic mutations in the germline.

From an environmental perspective, current evidence does **not identify specific environmental risk factors** (such as toxins, infections, or lifestyle exposures) that increase the likelihood of MKHK, nor does it implicate gene–environment interactions in disease causation, given the monogenic nature and ultra-low prevalence.[1][2][5][6][8][11][17] Epidemiologic databases and case reports do not demonstrate clustering in particular occupational groups, exposure histories, or geographic regions beyond what would be expected by chance for a disease occurring in less than one per million births.[8][11][17] Likewise, there is no evidence that maternal age, paternal age, consanguinity, nutritional status, or other demographic factors materially change the risk of de novo CREBBP/EP300 exon 30/31 mutations, although general trends observed in genetic mutagenesis (e.g., increased de novo mutation rates with advanced paternal age) could hypothetically apply.[6][8] Such hypotheses remain untested for MKHK.

Given the absence of evidence for environmental susceptibility, the **primary risk factor** framework for MKHK is strictly genetic: possessing a pathogenic CREBBP or EP300 exon 30/31 variant confers near-certain risk of developing the syndrome, with high penetrance and autosomal dominant inheritance.[1][2][6][8][9][16][17] For relatives of an affected individual, the main risk parameter is a 50% chance of inheriting the variant if the parent is heterozygous in the germline, modified by the possibility of parental germline mosaicism in apparently unaffected parents. For the general population, the absolute risk remains extremely low, given the rarity of such variants and their strong selection against.[6][8][11][17][13]

### 2.3 Protective Factors and Modifiers

Currently, **no specific genetic protective factors**—such as modifier alleles that reduce disease severity or prevent manifestation in carriers of pathogenic variants—have been identified for Menke-Hennekam syndrome. Neither OMIM nor Orphanet reports known modifier genes linked to MKHK, and ClinVarMiner does not suggest variants that mitigate the effects of pathogenic CREBBP/EP300 exon 30/31 mutations.[1][2][10][11][13] Given the small number of known cases, the statistical power to detect such modifiers is limited, and most published case series have focused on defining the core phenotype rather than exploring variability in expressivity attributable to other genetic loci.[3][4][5][7][16]

Nevertheless, there is significant **clinical variability** between individuals with MKHK, even among those carrying identical variants, as illustrated by the different degrees of intellectual disability, growth impairment, and autistic features reported.[3][4][5][7][8][11][17] This variability suggests that genetic background and environmental context may act as modifiers of disease severity, although specific loci or exposures have not been formally characterized. For instance, Menke et al. observed a range from mild to severe intellectual disability among carriers of variants in the same CREBBP/EP300 domain, implying that polygenic neurodevelopmental resilience or vulnerability factors (e.g., variants in synaptic genes, chromatin regulators) could influence outcome.[3][4][7] Similarly, differences in access to early intervention, supportive family environments, and healthcare may affect developmental trajectories and functional abilities in affected children.[5][6][8][11][17]

Environmental “protective factors” for MKHK are therefore best understood in terms of **secondary prevention and mitigation of impact** rather than primary prevention of variant occurrence. Early diagnosis, comprehensive developmental and behavioral interventions, appropriate seizure management, hearing and vision support, and nutritional and respiratory care can substantially improve quality of life and functional outcomes for individuals with MKHK, even though they do not alter the underlying genetic lesion.[5][6][8][11][17] From an ontological perspective, these interventions correspond to NCIT terms such as **NCIT:C16084 (Supportive Care)**, **NCIT:C48676 (Developmental Therapy)**, and **NCIT:C15661 (Anticonvulsant Therapy)**, which can be annotated as modifiers of morbidity but not of genetic risk.

### 2.4 Gene–Environment Interaction

Given the monogenic nature and rarity of MKHK, explicit studies of **gene–environment interactions** have not been conducted, and databases focused on GxE interactions or toxicogenomic associations do not list MKHK-specific data.[1][2][10][11] The clinical genetics literature emphasizes that MKHK arises from specific CREBBP/EP300 exon 30/31 variants and that parental behaviors or exposures do not “cause” these mutations.[6][8] This does not preclude the possibility that general mutagenic exposures (such as radiation or certain chemicals) might increase the risk of de novo mutations in many genes, including CREBBP/EP300, but no MKHK cases have been linked mechanistically to such exposures.

In terms of *postnatal* gene–environment interactions, CBP and p300 are transcriptional coactivators involved in integrating environmental signals (e.g., neuronal activity, hormonal signaling) into chromatin modifications and gene expression changes.[4][7][9][10] It is therefore plausible that environmental stimuli—such as enriched environments, learning experiences, stress, and inflammation—could interact with altered CBP/p300 function to shape neural circuits and behavioral outcomes in MKHK, much as they do in other neurodevelopmental disorders. However, this is currently **inferred** from broader CBP/p300 biology and not directly studied in MKHK cohorts.[4][7][9][10] Accordingly, while environmental factors undoubtedly influence the lived experience and developmental trajectory of MKHK patients, they are not recognized as primary etiologic contributors in the disease’s causal chain.

In summary, Menke-Hennekam syndrome is essentially a **genetically determined disorder** with a clear monogenic cause and negligible established environmental contribution to variant occurrence, although general environmental and psychosocial factors modify disease expression and quality of life. The current risk framework is dominated by autosomal dominant inheritance and de novo mutation dynamics at the CREBBP and EP300 loci.[1][2][5][6][8][9][11][13][16][17]

## 3. Phenotypes: Clinical Features, Severity, and Quality of Life Impact

### 3.1 Core Neurodevelopmental Phenotypes

The **neurodevelopmental phenotype** of Menke-Hennekam syndrome is central to its definition and has been characterized across multiple databases and case series. Orphanet lists “intellectual disability” and “developmental delay” among the most frequent features, noting variability in severity.[11][12] OMIM similarly describes MKHK1 and MKHK2 as congenital disorders characterized by “variable impairment of intellectual development” and developmental delay.[1][2] Menke et al.’s clinical series and subsequent literature reviews confirm that cognitive outcomes range from borderline intellectual functioning to moderate or severe intellectual disability, with associated delays in gross motor, fine motor, speech, and social milestones.[3][4][5][7] The age of onset for developmental concerns is typically in infancy or early childhood, when delays in sitting, walking, and language acquisition become apparent.[5][7][8][11][17]

Autistic behaviors and broader **autism spectrum disorder (ASD)-like features** are another hallmark, consistently reported in MKHK.[1][2][5][6][7][11][17] MedlinePlus notes that Menke-Hennekam syndrome may include “autistic behaviors that affect communication,” and Simons Searchlight describes EP300-related syndrome (including MKHK2) as frequently associated with autism and behavioral differences.[5][6] Orphanet lists “autistic behavior” as a characteristic feature.[11][12] Clinically, these behaviors include reduced eye contact, limited social reciprocity, restricted interests, repetitive behaviors, and communication deficits, often leading to formal ASD diagnoses or classification within neurodevelopmental disorder frameworks.[5][6][7][8][11][17] HPO terms such as **autistic behavior (HP:0000729)**, **impaired social interactions (HP:0000735)**, and **abnormality of language development (HP:0002463)** are appropriate descriptors.

The **severity of intellectual disability and autistic features** is variable, even within domain-defined subgroups. The 2024 domain-specific study found that individuals with MKHK-ID4 (affecting an intrinsically disordered region) had somewhat milder intellectual and behavioral phenotypes compared with those with MKHK-ZZ and MKHK-TAZ2, although all groups displayed developmental challenges.[3][4] This suggests a continuum rather than discrete severity classes. Over time, developmental and behavioral difficulties are generally persistent and **chronic**, though individuals may make progress with therapy and education, especially in language and adaptive skills.[5][6][7][8][11][17] There is no evidence of neurodegenerative progression; rather, the course is one of early-onset static encephalopathy with evolving functional expression across the lifespan.[5][7][11]

Quality of life impact is substantial. Children with MKHK often require special education services, speech therapy, occupational and physical therapy, behavioral interventions, and frequent medical follow-up, which impose burdens on families and healthcare systems.[5][6][8][11][17] Many individuals need assistance with daily living tasks well into adolescence and adulthood, although the degree varies. From an EQ-5D or SF-36 perspective, domains related to mobility, self-care, usual activities, pain/discomfort, and anxiety/depression are likely affected, especially in severe cases, although formal QoL studies specific to MKHK have not been conducted.[5][6][11] HPO terms reflecting these impacts include **global developmental delay (HP:0001263)**, **intellectual disability (HP:0001249)**, **behavioral abnormality (HP:0000708)**, and **impaired adaptive behavior (HP:0000750).**

### 3.2 Growth, Craniofacial, and Somatic Phenotypes

Growth abnormalities are a prominent feature of MKHK. Orphanet and KEGG list **short stature** and **microcephaly** among the main characteristics of the syndrome.[10][11] OMIM’s entries for MKHK1 and MKHK2 describe “short stature” and “microcephaly” as frequently seen.[1][2] Japanese explanations emphasize “low height” and “microcephaly” as primary manifestations.[8][17] These features are typically evident in infancy and persist throughout childhood, with occipitofrontal head circumference and height measurements falling below standard percentiles. HPO terms such as **short stature (HP:0004322)** and **microcephaly (HP:0000252)** capture these phenotypes.

Craniofacial dysmorphism is distinctive and contributes significantly to clinical recognition. Orphanet lists as characteristic facial features: “short and upslanted palpebral fissures, ptosis, telecanthus, depressed nasal ridge, short nose, anteverted nares, short columella, and long philtrum.”[11] OMIM notes “facial dysmorphisms,” and Japanese resources describe “long philtrum” and “characteristic facial appearance” as notable.[1][2][8][17] Menke et al. and subsequent case reports illustrate faces with relatively flat midface, short nose with upturned tip, long philtrum, thin upper lip, and sometimes micrognathia.[5][7] These craniofacial features differ from the broad, beaked nose and high-arched eyebrows of classic RSTS and lack the broad thumbs and halluces considered pathognomonic for RSTS.[1][2][5][7][9][17] HPO terms applicable here include **distinctive facial features (HP:0001999)**, **long philtrum (HP:0000301)**, **telecanthus (HP:0000506)**, **ptosis (HP:0000508)**, **anteverted nares (HP:0000463)**, and **short nose (HP:0005484).**

Beyond craniofacial features, MKHK involves somatic manifestations such as **feeding difficulties**, **recurrent upper airway infections**, **hearing impairment**, and **epilepsy**. Orphanet lists “feeding problems,” “vision and hearing impairments,” “recurrent upper airway infections,” and “epilepsy” as additional variable manifestations.[11][12] OMIM mentions “feeding difficulties, autistic behavior, recurrent upper airway infections, hearing impairment” as frequent.[1][2] MedlinePlus notes that Menke-Hennekam syndrome can include “vision or hearing impairment, recurrent seizures (epilepsy), frequent airway infections,” further emphasizing these systemic involvements.[5] Japanese explanations echo feeding difficulties in infancy, short stature, and hearing impairment as common features and stress that broad thumbs/halluces typical of RSTS2 are not present in MKHK2.[8][17] The age of onset for feeding problems is typically neonatal or early infancy, while recurrent infections and seizures may emerge over the first few years of life.[5][7][8][11][17]

The severity and progression of these somatic features vary. Feeding difficulties may require temporary tube feeding or specialized interventions but can improve as children grow, though some continue to have oral motor or swallowing challenges.[8][11][17] Recurrent upper airway infections can contribute to hospitalizations and may reflect structural airway anomalies, immune vulnerability, or aspiration, though detailed mechanisms are not yet defined.[11][12] Hearing impairment can be conductive or sensorineural and may necessitate hearing aids; its presence further impacts language development and social interaction.[5][6][11][17] Epilepsy, when present, ranges from focal to generalized seizures and generally requires chronic antiseizure medication; seizure control greatly influences quality of life, but no MKHK-specific epilepsy syndrome has been described.[5][7][11] Overall, the somatic phenotype includes chronic but often manageable systemic challenges that increase morbidity and care needs.

### 3.3 Organ-Specific Malformations and Additional Phenotypes

Although MKHK is primarily a neurodevelopmental and craniofacial growth syndrome, Orphanet notes additional “reported malformations” including **cryptorchidism** and **cerebral anomalies**.[11] Cryptorchidism (undescended testis) typically affects male patients and may require surgical correction to reduce risks of infertility and malignancy; its frequency in MKHK is not precisely quantified but likely in the minority of cases. Cerebral anomalies, such as structural brain malformations detected on MRI, have been observed in some individuals and include features such as enlarged ventricles, corpus callosum abnormalities, or cortical dysplasia, although detailed radiologic data are sparse in public databases.[7][11] These anomalies likely contribute to the neurodevelopmental phenotype and may be associated with epilepsy.

Additional phenotypic features reported in case series, reviews, and patient guides include **vision problems** (such as strabismus or refractive errors), **micrognathia**, **abnormal head shape**, and sometimes **skeletal anomalies** of the spine or limbs, although these are less consistent than the core features.[5][7][8][11][17] Simons Searchlight indicates that EP300-related syndrome (including MKHK2) can involve growth delays, muscle tone abnormalities, and other systemic manifestations.[6] However, MKHK patients generally lack the broad thumbs and halluces, characteristic facial features, and specific skeletal anomalies typical of RSTS, reinforcing the clinical distinction.[1][2][5][7][9][17]

From a behavioral perspective, beyond autistic features, individuals may show **attention difficulties**, **hyperactivity**, **sleep disturbances**, and **challenging behaviors**, reflecting broader neurobehavioral dysregulation often seen in chromatinopathies.[5][6][7][8][11][17] Some may also manifest anxiety, mood symptoms, or sensory sensitivities. These aspects critically affect family functioning and require individualized behavioral and psychiatric interventions. Formal neuropsychiatric assessments are limited in the published MKHK literature, but extrapolation from similar disorders such as RSTS and other CBP/p300-related syndromes suggests that behavioral comorbidity is common.[6][7][9]

### 3.4 Frequency, Severity, and Progression of Phenotypes

Because MKHK is extremely rare, precise quantitative frequencies for individual HPO phenotypes are not yet standardized. Orphanet presents phenotypic abnormalities ordered by frequency categories but does not provide explicit percentages.[11][12] Intellectual disability, developmental delay, autistic behavior, short stature, and microcephaly are considered **high-frequency features**, present in a majority of reported cases.[1][2][10][11] Feeding difficulties, vision and hearing impairments, recurrent upper airway infections, and epilepsy are **variable manifestations**, with occurrence in a substantial subset but not necessarily all individuals.[5][7][11] Cryptorchidism and cerebral anomalies are **additional malformations** observed in some but not most patients.[11]

Severity is **variable**, spanning mild to severe intellectual disability, moderate to significant short stature and microcephaly, and from subtle to pronounced facial dysmorphism.[3][4][5][7][8][11][17] Autistic behavior may range from mild social communication difficulties to full-threshold ASD with substantial functional impairment.[5][6][7][11] Somatic features such as hearing impairment and epilepsy similarly show variable impact, depending on the degree of hearing loss and seizure control. Over time, the **progression** of MKHK phenotypes is largely static in terms of structural features (microcephaly, facial dysmorphism, congenital malformations) but dynamic in terms of functional competencies, behavior, and comorbidities. Many individuals show developmental gains with appropriate interventions, but underlying cognitive limitations and neurologic vulnerabilities persist into adulthood.[5][6][7][11][17]

From a quality-of-life standpoint, MKHK is a **high-impact disorder**. It affects multiple domains, including physical health (feeding, growth, infections, epilepsy), sensory function (hearing, vision), neurocognitive development (learning, communication, adaptive skills), behavior (autism, attention, mood), and social participation (education, employment, relationships).[5][6][8][11][17] Families face chronic care demands and psychosocial stress, and individuals may experience stigma and barriers to inclusion. While formal QoL instruments such as EQ-5D or SF-36 have not been systematically applied to MKHK cohorts, the burden is inferred to be substantial based on clinical narratives and resource use.[5][6][11][17]

In ontological annotation, MKHK can thus be characterized by a core set of high-frequency HPO phenotypes—intellectual disability, global developmental delay, autistic behavior, short stature, microcephaly, distinctive facial features, feeding difficulties, recurrent upper airway infections, hearing impairment—and a set of variable phenotypes including epilepsy, vision impairment, cryptorchidism, cerebral anomalies, and behavioral disturbances.[1][2][5][6][8][10][11][12][17] These features collectively define the phenotypic profile used for disease modeling and diagnostic decision support.

## 4. Genetic and Molecular Information

### 4.1 Causal Genes and Their Normal Functions

Menke-Hennekam syndrome is caused by pathogenic variants in two highly homologous genes: **CREBBP** (CREB-binding protein) on chromosome 16p13.3 and **EP300** (E1A-associated protein p300) on chromosome 22q13.2.[1][2][5][9][10] CREBBP (HGNC:2348; OMIM gene number 600140) encodes CBP, a transcriptional coactivator with intrinsic lysine acetyltransferase activity that acetylates histones and a wide array of non-histone proteins, thereby modulating chromatin structure and transcription.[4][7][9][10] EP300 (HGNC:3373; OMIM gene number 602700) encodes p300, a closely related paralog with similar histone acetyltransferase and transcriptional regulatory functions.[4][5][6][7][10]

Japanese resources summarize CREBBP as a gene where constitutional variants cause Rubinstein–Taybi syndrome and Menke-Hennekam syndrome, while somatic variants can trigger lymphomas and leukemia.[9] They locate CREBBP at 16p13.3 and note its alternative names CBP and KAT3A, reflecting its histone acetyltransferase (KAT) function.[9] MedlinePlus Genetics explains for EP300 that “the EP300 gene provides instructions for making a protein called p300, which regulates the activity of many genes in tissues throughout the body,” and specifically mentions its role in controlling cell growth and division, differentiation, and transcriptional responses.[5] KEGG likewise classifies CREBBP and EP300 as causal genes for MKHK and RSTS and links them to pathways involved in chromatin modification and transcriptional regulation.[10]

CBP and p300 function as global transcriptional coactivators in multiple signaling pathways, including CREB-dependent transcription, nuclear hormone receptor signaling, and stress responses.[4][7][9][10] They act by acetylating histone tails (e.g., H3K27ac) to open chromatin, acetylating transcription factors to modulate their activity, and serving as scaffolds that bridge DNA-binding factors with the basal transcription machinery.[4][7][9][10] Their role is particularly critical in neuronal development and plasticity, where CBP/p300-mediated histone acetylation is essential for activity-dependent gene expression, synaptic function, learning, and memory.[4][7][9] Consequently, perturbations in CBP/p300 function can have broad effects on gene expression programs across tissues, with pronounced impact on neurodevelopment, growth, and organ morphogenesis, consistent with the MKHK phenotype.[4][7][9][10]

### 4.2 Pathogenic Variant Types, Classification, and Distribution

The pathogenic variants responsible for MKHK are predominantly **missense mutations** and **in-frame indels** (small deletions) localized to exons 30 and 31 of CREBBP and EP300.[1][2][3][4][5][7][8][9][10][17] OMIM explicitly states that MKHK1 is caused by heterozygous mutation in exon 30 or 31 of CREBBP and MKHK2 by heterozygous mutations in exon 30 or 31 of EP300, and that mutations elsewhere in these genes result in Rubinstein–Taybi syndrome rather than MKHK.[1][2] Simons Searchlight notes that variants causing Menke-Hennekam syndrome are “pathogenic missense variants or in-frame deletion variants in exons 30 and 31” of EP300 or CREBBP.[6] Japanese resources likewise emphasize that MKHK1 and MKHK2 are due to specific missense or in-frame deletion variants concentrated in these exons, and that small point mutations are typically not detectable by standard karyotyping or chromosomal microarray.[8][17]

ClinVarMiner provides a global variant summary for Menke-Hennekam syndrome, reporting 388 variants across five gene categories (CREBBP, EP300, and combinations with LOC pseudogenes), of which 14 are pathogenic and 24 likely pathogenic.[13] The majority of submitted variants in CREBBP (320 total) and EP300 (57 total) are classified as variants of uncertain significance (VUS) or benign, reflecting background variation, but pathogenic/likely pathogenic missense variants cluster in exon 30/31 positions known to affect relevant domains.[13] Specific variants such as CREBBP c.5602C>T (p.Arg1868Trp) and c.5615T>C (p.Met1872Thr) are annotated in ClinVar as pathogenic for MKHK1, supported by multiple literature references and evidence including de novo occurrence and strong genotype–phenotype correlation.[14][16]

The ClinVar entry for p.Arg1868Trp reports that Menke et al. in 2016 detected “heterozygosity for a C-to-T transition at nucleotide 5602… in exon 31 of the CREBBP gene, resulting in an arg1868-to-trp substitution,” in two unrelated girls with MKHK1, and notes that a different missense alteration at the same codon (p.Arg1868Gln) has also been reported as pathogenic/likely pathogenic.[14] The entry for p.Met1872Thr references multiple cases, notes that p.Met1872Val at the same position has been reported eight times as pathogenic/likely pathogenic and de novo in six affected individuals, and applies ACMG/AMP criteria to classify p.Met1872Thr as pathogenic.[16] These examples illustrate how specific amino acid substitutions within the exon 31 region of CREBBP confer a strong MKHK phenotype.

From a functional classification perspective, MKHK variants are considered **pathogenic** or **likely pathogenic** according to ACMG/AMP guidelines, based on criteria such as localization to a critical functional domain, absence in population databases, de novo occurrence, segregation with disease, and functional impact inferred from domain structure and epigenomic data.[13][14][16] The variant class is primarily missense (Sequence Ontology: SO:0001583) or in-frame deletion (SO:0001822), with no nonsense or frameshift variants reported as causative for MKHK per se; truncating variants in CREBBP/EP300 typically cause RSTS instead.[1][2][9][10][13][16] Population allele frequencies for MKHK variants are extremely low or absent in gnomAD and other large-scale human variation databases, reflecting their pathogenicity and negative selection, although explicit gnomAD entries for each variant are not detailed in the provided sources.[13][14][16]

Most MKHK variants are of **germline origin**, present in all cells of the affected individual, consistent with a congenital, multisystem disorder.[1][2][5][7][8][9][11][16][17] There is no evidence of somatic-only MKHK variants causing isolated organ involvement. Somatic variants in CREBBP and EP300 are well-known in hematologic malignancies and solid tumors, but they are distinct from the germline exon 30/31 variants associated with MKHK.[9][14][16] ClinVar entries focus on germline classification for MKHK variants, and somatic classification is marked as “none” for these specific variants.[14][16]

### 4.3 Functional Consequences: Gain-of-Function and Dominant-Negative Mechanisms

A key mechanistic insight about Menke-Hennekam syndrome is that the causative exon 30/31 variants in CREBBP and EP300 appear to act via **altered function**—in particular, gain-of-function or dominant-negative mechanisms—rather than classic haploinsufficiency. MedlinePlus explicitly states that EP300 exon 30/31 mutations in Menke-Hennekam syndrome “result in changes to single protein building blocks… Researchers suggest that these changes give the altered protein a new function, which disrupts development and causes the signs and symptoms of Menke-Hennekam syndrome.”[5] Japanese explanations for MKHK1 similarly note that the molecular mechanism differs from RSTS’s haploinsufficiency and involves “NMD avoidance and dominant-negative” effects.[8] For MKHK2, Minerva Clinic describes that “RSTS2… is mainly caused by haploinsufficiency reducing p300 protein level by half, whereas MKHK2 is caused by missense variants or in-frame deletions in exons 30–31,” implying a qualitatively different dysfunction.[17]

The 2024 domain-specific study further supports altered-function mechanisms by mapping variants to specific regions: the **ZZ domain**, a zinc finger that binds transcriptional regulators; the **TAZ2 domain**, a transcriptional adaptor that interacts with multiple factors; and an intrinsically disordered region termed **ID4**.[3][4] Menke et al. demonstrate that each domain-associated subset has distinct clinical characteristics and unique DNA methylation episignatures, which would not be expected from simple loss-of-function alone.[3][4] In their words, “variants that produce a null allele or disrupt the catalytic domain of either protein cause Rubinstein-Taybi syndrome (RSTS), while pathogenic missense and in-frame indel variants in parts of exons 30 and 31 cause phenotypes recently described as Menke-Hennekam syndrome (MKHK)… These findings demonstrate existence of at least three MKHK subtypes, which are domain specific… rather than gene specific (CREBBP/EP300).”[3][4] This indicates that the MKHK variants likely alter specific protein–protein interaction surfaces or allosteric properties of CBP/p300, leading to selective dysregulation of gene networks, rather than global loss of CBP/p300 activity.

The notion of **dominant-negative** action arises from the idea that mutant CBP/p300 may compete with the wild-type protein for binding partners or chromatin sites, but fail to properly execute coactivator functions, thereby interfering with normal CBP/p300 complexes.[4][8][9][10] Alternatively, “neomorphic” gain-of-function changes may create new, inappropriate protein interactions or aberrant recruitment of CBP/p300 to genomic loci, resulting in misregulated transcription and epigenetic states.[4][5][9][10] The domain-specific methylation profiles observed in MKHK subtypes support such targeted misregulation, with certain sets of CpG sites hyper- or hypomethylated in MKHK-ZZ versus MKHK-TAZ2, consistent with differential transcriptional activity.[3][4]

The functional consequences of MKHK variants thus include altered histone acetylation patterns, aberrant transcriptional coactivation, and epigenomic signatures that distinguish MKHK from RSTS, where CBP/p300 function is globally reduced.[3][4][7][9][10] This nuanced mechanistic distinction is central to understanding why MKHK and RSTS, despite sharing causal genes, have markedly different phenotypic profiles.

### 4.4 Epigenetic Information and DNA Methylation Episignatures

Epigenetic profiling has provided one of the most informative molecular characterizations of Menke-Hennekam syndrome. In their 2024 publication, Menke et al. analyzed DNA methylation patterns in individuals with CREBBP/EP300 exon 30/31 variants and found **distinct, domain-specific methylation profiles** for MKHK-ZZ and MKHK-TAZ2, while refining a **domain-specific diagnostic episignature** for MKHK-ID4.[3][4] They used genome-wide methylation arrays to identify sets of CpG sites whose methylation status discriminated MKHK cases from controls and from RSTS, demonstrating that MKHK has a recognizable epigenetic “fingerprint” tied to specific CBP/p300 domains.[3][4]

The authors report that “Menke-Hennekam syndrome consists of at least three domain/region-specific subtypes within the genes CREBBP and EP300 (MKHK-ZZ, MKHK-TAZ2, and MKHK-ID4). Domain-specific methylation profiles were discerned for MKHK-ZZ and MKHK-TAZ2, while a domain-specific diagnostic episignature was refined for MKHK-ID4.”[4] This work builds on earlier concepts of “episignatures” for neurodevelopmental syndromes, where DNA methylation patterns act as robust biomarkers of underlying chromatin dysregulation. For MKHK, the episignature is sufficiently characteristic that methylation testing can be used in diagnostic workflows to confirm uncertain variants or classify VUSs in CREBBP/EP300 exon 30/31 regions.[3][4][17]

In addition to methylation changes, CBP/p300’s canonical role as histone acetyltransferases implies widespread alterations in histone acetylation, especially marks such as H3K27ac and H3K18ac, which are associated with active enhancers and promoters.[4][7][9][10] Though direct histone acetylation profiling in MKHK patient cells has not yet been reported in detail, the parallels with RSTS and other CBP/p300-related conditions suggest that MKHK involves **altered histone acetylation landscapes** and consequent transcriptional dysregulation.[7][9][10] Such epigenetic changes likely underpin the DNA methylation episignatures by influencing gene expression, transcription factor binding, and the recruitment of DNA methyltransferases and demethylases to specific loci.

From an ontological perspective, epigenetic alterations in MKHK can be mapped to GO terms such as **GO:0016573 (histone acetylation)**, **GO:0006306 (DNA methylation)**, and **GO:0045893 (positive regulation of transcription, DNA-templated)** and to epigenomics assay annotations in resources like DiseaseMeth or MethBase.[3][4][9][10] The use of DNA methylation episignatures as diagnostics corresponds to NCIT terms such as **NCIT:C17358 (Biomarker)** and **NCIT:C10604 (DNA Methylation Analysis)**. Minerva Clinic explicitly notes that, for MKHK2, DNA methylation episignature analysis can be employed as a **supplementary diagnostic test** when EP300 exon 30/31 variants are suspected.[17]

### 4.5 Chromosomal Abnormalities and Structural Variants

In contrast to RSTS, where large deletions encompassing CREBBP or EP300 can cause the syndrome through haploinsufficiency, Menke-Hennekam syndrome is **not associated with chromosomal structural abnormalities** such as deletions, duplications, translocations, or inversions.[1][2][9][10][17] Japanese resources emphasize that MKHK1 and MKHK2 are caused primarily by point mutations in CREBBP and EP300 rather than by large-scale chromosomal changes, and that therefore “conventional chromosome testing (G-banding) or chromosomal microarray (CMA) cannot detect” most MKHK causative variants.[8][17] OMIM likewise does not report chromosomal rearrangements linked specifically to MKHK, and KEGG lists only the genes CREBBP and EP300 as causal, not chromosomal loci.[1][2][10]

This distinction has important diagnostic implications. While CMA and karyotyping are valuable initial tests for individuals with developmental delay and congenital anomalies, they will **miss MKHK**, necessitating higher-resolution sequence-based approaches such as whole exome sequencing (WES) or targeted gene panels that cover CREBBP and EP300 exons 30–31.[7][8][17] Structural variants disrupting CREBBP/EP300 outside of exon 30–31 produce RSTS-like phenotypes, not MKHK, so identification of a deletion or frameshift in CREBBP or EP300 would point to RSTS rather than MKHK.[1][2][9][10] Structural variation resources such as DECIPHER and dbVar therefore play a limited role in MKHK diagnosis.

In summary, the genetic architecture of Menke-Hennekam syndrome is dominated by **single-nucleotide variants and small indels** in specific exons, without a significant contribution from chromosomal structural variants or aneuploidies. This makes MKHK a prototypical example of a domain-specific missense disorder in a chromatin regulator gene, suitable for detailed variant-level annotation and mechanistic study.[1][2][3][4][5][7][8][9][10][13][14][16][17]

## 5. Environmental, Lifestyle, and Infectious Factors

### 5.1 Environmental Factors and Toxins

Current data provide **no evidence** that environmental toxins, radiation, or pollutants play a causal role in Menke-Hennekam syndrome. None of the major curated resources—OMIM, Orphanet, KEGG, MedlinePlus Genetics, Simons Searchlight, or Minerva Clinic—mentions environmental exposures as etiologic factors for MKHK.[1][2][5][6][8][10][11][17] Case reports and literature reviews focus solely on germline variants in CREBBP/EP300 without linking them to specific environmental histories.[5][7] Given the ultra-low prevalence of MKHK (estimated at less than 1 per 1,000,000 live births for “pure” MKHK, and 1 per 100,000–125,000 for EP300-related syndromes including RSTS2), it would be challenging to detect environmentally mediated risk even if it existed.[6][8][11][17]

Comparative toxicogenomic databases do not list MKHK as an environmentally associated disorder, and there are no preclinical models examining how toxins might selectively affect CREBBP/EP300 exon 30/31 mutagenesis. While general mutagenic exposures such as ionizing radiation or DNA-damaging chemicals can increase de novo mutation rates across the genome, no MKHK case has been traced to such exposures, and current clinical guidance states that “no parent causes their child’s EP300-related syndrome… the gene change takes place on its own and cannot be predicted or stopped.”[6] Therefore, from a risk assessment standpoint, MKHK should be treated as a disease with negligible known environmental component in its etiologic chain.

### 5.2 Lifestyle Factors and Behavioral Exposures

Similarly, lifestyle factors such as smoking, alcohol consumption, diet, or physical activity do not appear in MKHK etiologic descriptions and are not implicated in increasing or decreasing risk of the syndrome.[1][2][5][6][8][11][17] The genetic counseling literature for EP300-related syndromes emphasizes that nothing parents do before or during pregnancy causes or prevents these gene changes, reflecting the random nature of de novo mutations and the absence of known lifestyle risk modifiers.[6] There is no evidence of MKHK clustering in particular socio-economic strata or cultural groups that might indicate lifestyle correlates.

However, lifestyle and behavioral factors have significant **secondary impacts** on the health and functioning of individuals with MKHK. For example, nutritional status can influence growth trajectories and resilience to infections, physical activity can affect motor development and cardiovascular health, and structured behavioral interventions can modify autistic behaviors and adaptive skills.[5][6][8][11][17] These factors operate downstream of the genetic lesion, influencing disease expression and quality of life rather than primary risk. In knowledge-base annotation, they can be linked to NCIT terms such as **NCIT:C12219 (Lifestyle Factor)** and **NCIT:C16916 (Behavioral Intervention)**, but they are not part of the disease’s primary pathophysiologic chain.

### 5.3 Infectious Agents

There is no association between Menke-Hennekam syndrome and specific infectious agents as primary etiologic triggers. MKHK is not an infectious disease and is not listed in pathogen-focused databases such as ViPR, BV-BRC, or GIDEON.[1][2][10][11] However, individuals with MKHK have a propensity for **recurrent upper airway infections**, as noted by OMIM and Orphanet, which may reflect underlying anatomical, immunologic, or neurologic vulnerabilities.[1][2][11][12] These infections are caused by common respiratory pathogens (viruses, bacteria), similar to those in the general pediatric population, but may occur more frequently or result in more severe complications due to dysphagia, aspiration risk, or structural airway anomalies.[11][12]

No specific immunodeficiency has been defined in MKHK, and clinical resources do not recommend special vaccination schedules beyond standard pediatric immunization programs.[5][6][11][17] Thus, infectious agents are best viewed as **secondary contributors to morbidity** in MKHK rather than primary disease causes. There is no evidence of zoonotic potential or cross-species transmission related to MKHK itself, as it is a non-infectious germline disorder.

In summary, environmental, lifestyle, and infectious factors influence the clinical course and complications of Menke-Hennekam syndrome but are not primary contributors to disease causation. The disease is etiologically rooted in germline CREBBP/EP300 exon 30/31 variants, and preventive efforts focus on genetic counseling rather than environmental risk modification.[1][2][5][6][8][10][11][17]

## 6. Mechanism and Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Clinical Phenotype

The mechanistic path from the initiating lesion in Menke-Hennekam syndrome to its clinical manifestations can be conceptualized as a sequence of causal steps. In narrative form, the ordered chain is as follows, with “Step 1” representing the initiating lesion and subsequent steps naming explicit causal relationships.

Step 1: A **germline heterozygous missense or in-frame indel variant in exons 30–31 of CREBBP or EP300** alters a specific functional domain (ZZ, TAZ2, or ID4) of CBP/p300.[1][2][3][4][5][7][8][9][10][16][17]  

Step 2: This domain-specific variant **leads to structural and functional changes in CBP/p300**, modifying its interactions with transcription factors, chromatin, and other coactivators, and resulting in altered coactivator function (gain-of-function or dominant-negative) rather than simple loss-of-function.[3][4][5][8][9][10]  

Step 3: Altered CBP/p300 activity **results in aberrant histone acetylation and transcriptional regulation** at specific genomic loci, causing misexpression of genes involved in neurodevelopment, growth, craniofacial morphogenesis, and other processes; some aspects of this step are inferred from CBP/p300 biology and epigenomic data rather than directly measured in MKHK.[3][4][7][9][10]  

Step 4: These transcriptional and chromatin changes **lead to domain-specific DNA methylation patterns**, producing characteristic episignatures for MKHK-ZZ, MKHK-TAZ2, and MKHK-ID4 and altering long-term gene regulatory landscapes.[3][4][17]  

Step 5: The resulting gene expression abnormalities **cause disordered development and function of key cell types**, particularly neuronal progenitors, cortical neurons, cranial neural crest cells, chondrocytes, and epithelial cells, leading to impaired brain development, microcephaly, short stature, craniofacial dysmorphism, and multisystem anomalies.[3][4][5][7][8][9][10][11][17]  

Step 6: These tissue-level abnormalities **result in the clinical phenotype** of Menke-Hennekam syndrome, including intellectual disability, developmental delay, autistic behavior, feeding difficulties, recurrent airway infections, hearing impairment, and epilepsy, with variable severity depending on domain affected and individual genetic background.[1][2][5][7][8][10][11][17]  

Where relevant, branches in this causal chain include domain-specific pathways (ZZ versus TAZ2 versus ID4) that produce distinct methylation patterns and subtle differences in clinical expression.[3][4] Most molecular details are derived from broader CBP/p300 biology and the domain-specific methylation study, with some steps (e.g., specific target genes, cell-type-specific transcriptional changes) inferred rather than fully demonstrated.[3][4][7][9][10]

### 6.2 Molecular Pathways and Cellular Processes

CBP and p300 are central nodes in multiple **molecular pathways**, particularly those controlling transcriptional responses to developmental signals, neuronal activity, and hormonal cues.[4][7][9][10] They serve as coactivators for CREB (cAMP response element-binding protein), nuclear hormone receptors (glucocorticoid receptor, estrogen receptor), HIF1A, and numerous other transcription factors, integrating signaling inputs into chromatin modifications and gene expression programs.[4][7][9][10] Key pathways implicated in MKHK, by inference from CBP/p300’s roles, include CREB signaling, Wnt/β-catenin pathways, MAPK/ERK signaling, and hedgehog signaling, all of which rely on CBP/p300-mediated acetylation and coactivation at target promoters and enhancers.[4][7][9][10]

At the **cellular level**, CBP/p300 regulate processes such as cell cycle progression, differentiation, apoptosis, and synaptic plasticity. In neuronal progenitors and cortical neurons, CBP/p300 acetylation of histones and transcription factors is essential for neuronal differentiation, migration, dendritic arborization, and synaptic maturation.[4][7][9][10] In cranial neural crest cells and chondrocytes, they govern gene expression programs for craniofacial morphogenesis and skeletal development.[9][10] In immune cells and epithelial cells, CBP/p300 modulate inflammatory responses and barrier functions, which could be relevant to recurrent airway infections.[10][11][12]

In Menke-Hennekam syndrome, the domain-specific variants in CBP/p300 perturb these pathways in selective ways. For example, variants in the **ZZ domain** may disrupt CBP/p300’s ability to interact with particular transcription factors or regulatory proteins that bind this zinc finger, leading to misregulation of a subset of genes important for neurodevelopment and craniofacial formation.[3][4][9][10] Variants in the **TAZ2 domain** may impair interactions with other transcriptional regulators, such as p53, c-Myb, and viral proteins, altering stress responses and developmental programs.[3][4][9][10] Variants in the **ID4 region**, an intrinsically disordered segment, may change protein flexibility or create aberrant interaction surfaces, affecting coactivator recruitment in more subtle ways.[3][4]

The net effect is a **disruption of transcriptional homeostasis** in critical cell types, leading to abnormal development and function. This can be mapped to GO biological process terms such as **GO:0006357 (regulation of transcription from RNA polymerase II promoter)**, **GO:0016573 (histone acetylation)**, **GO:0030182 (neuronal differentiation)**, **GO:0007399 (nervous system development)**, and **GO:0048701 (embryonic cranial skeleton morphogenesis)**, reflecting the processes impacted by CBP/p300 dysfunction.[4][7][9][10]

### 6.3 Protein Structure and Dysfunction

Structurally, CBP and p300 are large, multi-domain proteins comprising several conserved regions, including the KIX domain, bromodomain, HAT (histone acetyltransferase) domain, PHD finger, ZZ zinc finger, and TAZ2 domain, as well as extensive intrinsically disordered segments that mediate flexible interactions.[4][7][9][10] The HAT domain is responsible for acetyltransferase activity, while the bromodomain binds acetylated lysines on histones and non-histone proteins, and the ZZ and TAZ2 domains bind diverse transcription factors and regulatory partners.[4][7][9][10]

MKHK variants cluster in exons 30–31, which encode portions of the **ZZ**, **TAZ2**, and adjacent ID4 region at the C-terminal end of CBP/p300.[3][4][9][10] Missense and in-frame deletion variants in these domains alter amino acid residues critical for zinc-binding, protein folding, and interaction surfaces, leading to **protein dysfunction**. This dysfunction may include misfolding, impaired stability, altered conformational dynamics, and disrupted binding to transcription factors or other coactivators.[3][4][9][10] In some cases, the variants may not abolish domain function entirely but change its specificity or affinity, creating a **neomorphic** (new function) or **dominant-negative** effect.

For example, the CREBBP p.Arg1868Trp and p.Arg1868Gln variants affect a conserved arginine residue in exon 31, likely within or adjacent to a key interaction surface, and are repeatedly associated with MKHK1 in unrelated individuals.[14] The p.Met1872Thr and p.Met1872Val variants similarly target a conserved methionine in this region and have strong genotype–phenotype correlation.[16] These recurrent variants suggest a structural “hotspot” whose alteration perturbs CBP function in a specific way. Although detailed structural modeling is not provided in the sources, the functional consequences can be inferred from domain roles and variant clustering.

In protein ontology terms, MKHK involves **abnormal CBP (PR:000004593)** and **abnormal p300 (PR:000004536)**, with specific domain dysfunction in ZZ (InterPro: IPR001844), TAZ2 (InterPro: IPR013019), and ID4 regions. The type of protein dysfunction is best categorized as **altered interaction and regulatory function** rather than mere loss-of-function, consistent with the observed phenotypic distinction from RSTS.[3][4][5][8][9][10]

### 6.4 Metabolic and Biochemical Changes

At present, there are no detailed metabolic or biochemical studies specific to Menke-Hennekam syndrome. CBP/p300’s primary biochemical role is in histone acetylation and transcriptional regulation, rather than in classic metabolic pathways such as glycolysis or lipid metabolism.[4][7][9][10] However, because CBP/p300 coactivate genes in multiple metabolic pathways, MKHK may involve indirect metabolic changes, such as altered neuronal energy metabolism, oxidative stress responses, or endocrine regulation, though such changes remain **inferred** rather than directly measured.

Biochemical abnormalities that can be conceptualized include **altered acetyl-CoA utilization** for histone acetylation, **changed expression of metabolic enzymes** via transcriptional misregulation, and **secondary endocrine dysregulation** affecting growth and energy balance.[4][7][9][10] These processes map to GO terms such as **GO:0006096 (glycolytic process)**, **GO:0006629 (lipid metabolic process)**, and **GO:0009890 (negative regulation of biosynthetic process)**, but detailed metabolic profiling (e.g., metabolomics, lipidomics) has not yet been performed in MKHK cohorts.[3][4] Therefore, metabolic alterations remain an extrapolated aspect of pathophysiology, not a primary diagnostic or mechanistic focus.

### 6.5 Immune System and Tissue Damage Mechanisms

Menke-Hennekam syndrome is not primarily an immune disorder, but recurrent upper airway infections suggest some involvement of **mucosal immunity, airway structure, or neuromuscular control**.[1][2][11][12] CBP/p300 are involved in transcriptional regulation of immune response genes, including NF-κB-dependent inflammatory pathways, suggesting that altered CBP/p300 function could theoretically affect immune responses and mucosal defenses.[9][10] However, no explicit immunologic abnormalities (such as immunoglobulin deficiencies or lymphocyte dysfunction) have been documented in MKHK, and recurrent infections are more plausibly attributed to structural factors (e.g., craniofacial dysmorphism, airway anomalies), aspiration from feeding difficulties, or general vulnerability in neurologically impaired children.[11][12]

Tissue damage mechanisms in MKHK are thus primarily **developmental** rather than degenerative or inflammatory. Microcephaly arises from reduced neuronal production or increased apoptosis during development, short stature from endocrine or chondrocyte differentiation defects, and craniofacial anomalies from altered cranial neural crest differentiation and growth.[4][7][9][10][11] Epilepsy, when present, likely reflects aberrant cortical circuitry and neuronal excitability rather than inflammatory or structural damage occurring postnatally.[5][7][11] These damage mechanisms map to GO processes such as **GO:0007399 (nervous system development)**, **GO:0048701 (embryonic cranial skeleton morphogenesis)**, **GO:0008285 (negative regulation of cell proliferation)**, and **GO:0006915 (apoptotic process)**.

### 6.6 Molecular Profiling and Advanced Technologies

The most advanced **molecular profiling** applied to Menke-Hennekam syndrome thus far is genome-wide DNA methylation analysis. As noted, the 2024 study delineated domain-specific methylation profiles and refined a diagnostic episignature for MKHK-ID4.[3][4] This work used high-density methylation arrays (e.g., Illumina EPIC) to identify CpG sites whose methylation levels differ between MKHK cases and controls, enabling computational classification using machine learning models.[3][4] The presence of distinct methylation clusters corresponding to ZZ, TAZ2, and ID4 variants demonstrates that MKHK has a stable epigenomic footprint across cell types examined (typically blood-derived DNA).

Transcriptomic, proteomic, metabolomic, and lipidomic profiling have not yet been reported for MKHK specifically, although similar approaches have been applied to RSTS and other chromatinopathies. In principle, RNA-seq could reveal gene expression programs altered in MKHK, proteomics could identify acetylation changes and dysregulated protein networks, and metabolomics could detect downstream metabolic signatures.[3][4][7][9][10] Single-cell sequencing, spatial transcriptomics, and multi-omics integration remain future directions for exploring MKHK pathophysiology at cellular and tissue resolution.

In functional genomics, CRISPR/Cas9 or RNAi screens targeting CBP/p300 domains in cell lines could model MKHK-like alterations, but such screens have not been reported explicitly for MKHK and would currently be speculative.[3][4][9][10] Nonetheless, the combination of well-defined causal variants, domain-specific subtypes, and epigenetic episignatures positions MKHK as an excellent candidate for future advanced molecular profiling studies.

### 6.7 Cell Types and Ontological Mapping

The key **cell types** involved in Menke-Hennekam syndrome include neuronal progenitors and differentiated neurons in the cerebral cortex (CL:0000540, neuron; CL:0000233, neural progenitor), cranial neural crest cells contributing to craniofacial structures, chondrocytes in growth plates (CL:0000138, chondrocyte), and epithelial cells lining the upper airway and sensory organs.[4][7][9][10][11] CBP/p300 are ubiquitously expressed and active in many cell types, but MKHK’s phenotypic focus on brain, craniofacial structures, growth, and sensory organs suggests that CBP/p300 dysfunction is particularly salient in these tissues.

At the subcellular level, CBP/p300 localize to the **nucleus** (GO:0005634), specifically to chromatin (GO:0000785) and transcriptional complexes, where they acetylate histones and transcription factors.[4][7][9][10] They interact with nuclear receptors, coactivators, and basal transcription machinery. MKHK variants in CBP/p300 domains thus perturb nuclear complexes regulating gene expression. Other cellular compartments, such as mitochondria or lysosomes, are not directly implicated.

In anatomical ontology terms, primary affected structures include the **cerebral cortex** (UBERON:0000956), **brain** (UBERON:0000955), **craniofacial skeleton** (UBERON:0003114), **skull** (UBERON:0003129), **auditory system** (UBERON:0000020), **eye** (UBERON:0000970), and **upper respiratory tract** (UBERON:0001557).[10][11] Secondary involvement occurs in endocrine organs, musculoskeletal system, and reproductive organs (e.g., testes in cryptorchidism). MKHK can be conceptualized as a disorder of **global chromatin regulation** with preferential impact on specific tissues due to their developmental sensitivity to CBP/p300-mediated transcriptional programs.

In sum, Menke-Hennekam syndrome’s pathophysiology is rooted in domain-specific alterations of CBP/p300 coactivator function, leading to targeted epigenetic and transcriptional dysregulation in neurodevelopmental and craniofacial pathways and resulting in a recognizable syndrome distinguished from haploinsufficiency-driven RSTS.[3][4][5][7][8][9][10]

## 7. Anatomical Structures Affected

### 7.1 Organ-Level Involvement

Menke-Hennekam syndrome affects multiple organ systems, with **primary involvement of the nervous system, craniofacial structures, and growth-related tissues**, and secondary effects on auditory, visual, respiratory, and reproductive organs. Orphanet’s disease definition underscores the presence of intellectual disability and developmental delay (nervous system), short stature and microcephaly (growth and skull), and distinct facial features (craniofacial region).[11] OMIM describes MKHK as a congenital disorder with intellectual impairment, facial dysmorphisms, feeding difficulties, autistic behavior, recurrent upper airway infections, hearing impairment, short stature, and microcephaly, collectively implicating brain, craniofacial, respiratory, and auditory systems.[1][2]

The **brain** is a central organ affected, with microcephaly reflecting reduced brain size and cerebral anomalies (where present) indicating structural malformations.[1][2][7][11] The **cerebral cortex**, hippocampus, and subcortical nuclei involved in cognition and behavior are likely impacted developmentally, leading to intellectual disability and autistic features. The **craniofacial region**—including skull bones, facial skeleton, nasal structures, and soft tissues—is involved, producing characteristic dysmorphic features such as short upslanted palpebral fissures, telecanthus, depressed nasal ridge, short nose, anteverted nares, short columella, and long philtrum.[11]

The **auditory system** is affected through hearing impairment, which may involve both middle ear structures (conductive loss due to recurrent otitis media) and inner ear components (sensorineural loss).[5][6][11][17] The **visual system** may also be involved, with strabismus or refractive errors reported.[5][11] The **upper respiratory tract** and lungs are implicated by recurrent airway infections, which may reflect structural anomalies of the airway, aspiration from dysphagia, or mucosal defense alterations.[1][2][11][12] The **gastrointestinal system** is involved via feeding difficulties, reflux, and growth challenges.[1][2][5][8][11][17] The **endocrine and skeletal systems** contribute to short stature and possibly bone abnormalities.[10][11] The **reproductive system** may show malformations such as cryptorchidism in male patients.[11]

### 7.2 Tissue and Cell-Level Involvement

At the **tissue level**, MKHK involves nervous tissue (neurons and glia), epithelial tissues in sensory organs and airway, connective tissues in craniofacial skeleton and growth plates, and muscle tissues supporting motor function. Neuronal tissues in the cerebral cortex and subcortical structures are particularly affected, given the intellectual disability and autistic behaviors.[4][7][9][10][11] Craniofacial connective tissues, including cartilage, bone, and periosteum, are involved in skull and facial morphology.[9][10][11] Epithelial tissues lining the upper airway and middle ear are implicated in recurrent infections and hearing problems.[11][12]

Specific **cell populations** include cortical neurons (CL:0000540), inhibitory interneurons, hippocampal neurons, cranial neural crest cells (precursors of craniofacial structures), chondrocytes in growth plates (CL:0000138), and epithelial cells in the respiratory tract and sensory epithelia.[4][7][9][10][11] CBP/p300 are expressed in many of these cell types and are crucial for their differentiation and function. The dysregulation of transcriptional programs in these cells leads to abnormalities in tissue organization and organ function.

### 7.3 Subcellular Localization and Components

At the **subcellular level**, CBP/p300 localize predominantly to the **nucleus** (GO:0005634) and associate with **chromatin** (GO:0000785), where they acetylate histones and transcription factors.[4][7][9][10] MKHK variants in CBP/p300 domains thus perturb nuclear coactivator complexes and transcriptional regulation. Subcellular compartments affected by downstream consequences include synapses (neuronal synaptic structures) in the brain, where altered gene expression can lead to changes in receptor composition and synaptic plasticity, and mitochondria, where transcriptional changes may affect energy metabolism, though such effects remain inferred.

No specific abnormalities of organelles such as lysosomes or endoplasmic reticulum have been described in MKHK, and ultrastructural pathology studies are lacking. The main subcellular focus is on nuclear chromatin and transcriptional machinery, consistent with CBP/p300’s roles.

### 7.4 Localization and Lateralization

Anatomically, MKHK manifestations are largely **bilateral and symmetric**, affecting global brain development, craniofacial features, and stature, rather than producing lateralized lesions. Microcephaly and short stature are global phenomena; facial dysmorphism typically shows symmetric telecanthus, ptosis, and nasal shape changes.[11] Hearing impairment may be bilateral or asymmetric depending on middle ear disease patterns, but no systematic lateralization is reported.[5][6][11][17] Epilepsy, when present, may have focal onset on EEG, but this is individualized.

Specific anatomical sites relevant to MKHK include the cranial vault (skull bones), cranial base, midface, nasal structures, oral cavity, pharynx, larynx, trachea, lungs, middle ear, inner ear, cerebral cortex, hippocampus, basal ganglia, and testes (in cases of cryptorchidism).[11] These can be mapped to UBERON terms such as **UBERON:0003129 (skull)**, **UBERON:0001456 (face)**, **UBERON:0001733 (nasal cavity)**, **UBERON:0001557 (upper respiratory tract)**, **UBERON:0000020 (ear)**, **UBERON:0000970 (eye)**, **UBERON:0000955 (brain)**, and **UBERON:0000984 (testis).**

Overall, Menke-Hennekam syndrome is a multisystem disorder with predominant involvement of the nervous and craniofacial systems, mediated by cell-intrinsic defects in nuclear transcriptional regulation and chromatin modification.[1][2][4][7][9][10][11]

## 8. Temporal Development and Natural History

### 8.1 Age of Onset and Onset Pattern

Menke-Hennekam syndrome is a **congenital** disorder, with pathogenic variants present in the germline from fertilization and affecting development from the earliest stages. Clinical manifestations are typically recognized in **infancy or early childhood**.[1][2][5][7][8][11][17] Microcephaly and short stature may be evident at birth or in the first months of life, as head circumference and length measurements fall below normal percentiles.[8][11][17] Facial dysmorphisms may be subtle but can be appreciated by experienced clinicians early on. Feeding difficulties often emerge in the neonatal period, with poor suck, vomiting, reflux, or failure to thrive.[1][2][5][8][11][17]

Developmental delays become increasingly apparent over the first years of life, as children fail to meet motor and language milestones at typical ages.[5][7][8][11][17] Autistic behaviors and social communication difficulties generally become evident by toddlerhood and preschool age, consistent with ASD diagnostic timelines.[5][6][7][11][17] Hearing impairment, recurrent infections, and epilepsy may emerge across infancy and childhood, with variable timing.[5][7][11] Thus, the onset pattern is **insidious**, with multiple manifestations unfolding over the first few years of life rather than an acute presentation.

### 8.2 Disease Course, Stages, and Progression

The **disease course** of Menke-Hennekam syndrome is best described as chronic and **lifelong**, with static structural anomalies and evolving functional expression. There are no formally defined “stages” similar to cancer staging, but one can conceptualize a sequence: early developmental stage (infancy), childhood stage, adolescence, and adulthood, each with distinct challenges.

In infancy, key issues include feeding difficulties, failure to thrive, microcephaly, and initial developmental delays.[1][2][5][8][11][17] In early childhood, delays in motor and language development become more pronounced, autistic behaviors emerge, and recurrent infections or seizures may occur.[5][6][7][11] School-age children face educational challenges, behavioral issues, and social difficulties, requiring specialized educational and therapeutic support.[5][6][8][11][17] Adolescents and adults continue to experience cognitive limitations, adaptive behavior challenges, and medical comorbidities (e.g., epilepsy, hearing loss), but the structural features (microcephaly, facial dysmorphism, short stature) remain relatively stable.[5][7][11]

Progression in MKHK is **not neurodegenerative**—that is, there is no evidence that cognitive function systematically declines over time due to progressive neuronal loss. Instead, the primary pattern is of early developmental disruption followed by a static or slowly evolving plateau, with individual variability in adaptive gains achieved through interventions.[5][7][11] Epilepsy may fluctuate, with periods of better and worse seizure control, but there is no MKHK-specific progressive epilepsy syndrome described.[5][7][11] Recurrent infections may decrease as children grow and airway structures mature, but vulnerability can persist.[11][12]

Disease duration is **lifelong**, with MKHK affecting individuals across the entire lifespan. Adults with MKHK are increasingly recognized, though published data focus mainly on pediatric cases.[5][7][11][17] Remission of core features (intellectual disability, autistic behavior, microcephaly) does not occur; rather, management aims to optimize function within the constraints of the underlying condition.[5][6][11][17]

### 8.3 Critical Periods and Opportunities for Intervention

Critical periods in MKHK include the **early developmental window** (birth to age 5), when brain plasticity is high and interventions can have substantial impact on language, social skills, motor function, and adaptive behaviors. Early recognition of MKHK and prompt initiation of therapies—speech therapy, occupational therapy, physical therapy, applied behavior analysis, social skills training—can improve developmental trajectories and reduce behavioral difficulties.[5][6][8][11][17] Early management of feeding difficulties can prevent failure to thrive and nutritional deficits, mitigating growth impairment.[8][11][17] Early identification and treatment of hearing and vision impairments are similarly critical for language development and educational access.[5][6][11][17]

Genetic diagnosis in infancy or early childhood enables these interventions and informs family planning decisions, including recurrence risk counseling and options for prenatal or preimplantation genetic testing.[6][8][17] DNA methylation episignature testing, when available, may facilitate early diagnosis in cases where sequence variants are uncertain, providing opportunities for early intervention.[3][4][17] There is no evidence of a later “critical period” where interventions can reverse structural anomalies, but ongoing therapies can support adaptive functioning and mental health across adolescence and adulthood.[5][6][11][17]

In summary, Menke-Hennekam syndrome’s natural history is characterized by congenital onset, early developmental disruption, static structural anomalies, and chronic functional challenges, with significant opportunities for early and continued intervention to improve outcomes.[1][2][5][7][8][11][17]

## 9. Inheritance, Population Genetics, and Demographics

### 9.1 Inheritance Pattern and Penetrance

Menke-Hennekam syndrome is inherited in an **autosomal dominant** pattern.[1][2][6][8][9][17] OMIM specifies autosomal dominant inheritance for MKHK1 and MKHK2.[1][2] Simons Searchlight emphasizes that “EP300-related syndrome is an autosomal dominant genetic condition,” and Japanese resources state that MKHK1 and MKHK2 are “常染色体顕性（優性）遺伝” (autosomal dominant) disorders.[6][8][9][17] This means that a single pathogenic variant in one allele of CREBBP or EP300 is sufficient to cause disease, and affected individuals have a 50% chance of transmitting the variant to each offspring.

Penetrance appears to be **high**, with essentially all carriers of pathogenic exon 30/31 variants in CREBBP/EP300 manifesting some degree of MKHK phenotype.[1][2][3][4][14][16] Clinical case series have not reported unaffected carriers of clearly pathogenic MKHK variants, and ClinVar classifications are based on strong genotype–phenotype correlation.[14][16] However, the severity and specific features may vary, indicating **variable expressivity**.[3][4][5][7][8][11][17] Age-dependent penetrance is not prominent, as manifestations are congenital and recognized in childhood, though some features (e.g., epilepsy) may appear later.

Genetic anticipation has not been described in MKHK, which is consistent with the absence of repeat expansions or unstable elements as causal mechanisms. Germline mosaicism in apparently unaffected parents has not been extensively studied but is theoretically possible, given that some de novo variants could arise in parental germline cells and be transmitted to multiple offspring. This has implications for recurrence risk counseling, where even de novo cases may carry a small residual risk of recurrence due to mosaicism.[6][8][17]

### 9.2 De Novo Mutations and Founder Effects

Most Menke-Hennekam syndrome cases reported to date are due to **de novo mutations**, i.e., pathogenic variants that arise spontaneously in the germline of one parent and are present in the affected child but not in parental somatic DNA.[6][8][16][17] Simons Searchlight notes that “research shows that EP300-related syndrome is often the result of a de novo variant in EP300… Many parents who have had their genes tested do not have the EP300 genetic variant found in their child.”[6] Minerva Clinic similarly states that MKHK1 “in many cases is caused by de novo (new) mutations, meaning the parents have no change and the variant arose for the first time in the child.”[8]

ClinVar entries for specific CREBBP MKHK variants emphasize de novo status, such as the p.Met1872Val variant, which has been “demonstrated to be de novo in six affected individuals.”[16] These observations reflect strong negative selection against pathogenic CBP/p300 variants, given the associated neurodevelopmental impairment, and explain the rarity of familial MKHK cases.

No **founder effects** have been described for MKHK—that is, there is no evidence of particular variants recurring in specific populations due to a common ancestral origin. Pathogenic variants are scattered across exons 30–31 and have been reported in diverse ethnic and geographic contexts.[5][7][13][14][16] Population genetics databases such as gnomAD show extremely low frequencies (often absent) of these variants, further supporting their deleterious effects.[13][14][16] As case numbers grow, subtle population-specific patterns might emerge, but at present MKHK is considered a globally distributed, ultra-rare disorder without known founder mutations.

### 9.3 Epidemiology: Prevalence, Incidence, and Geographic Distribution

Precise epidemiologic data on Menke-Hennekam syndrome are limited due to its rarity and the recentness of its recognition. Orphanet classifies MKHK as a rare disease and notes a prevalence of **less than 1 per 1,000,000** for “pure” Menke-Hennekam syndrome.[11][15][18] Japanese resources similarly estimate that MKHK1 and MKHK2 occur in fewer than 1 per 1,000,000 individuals, describing them as “極めてまれな” (extremely rare) congenital syndromes.[8][17] Simons Searchlight reports that EP300-related syndrome as a whole (including RSTS2 and MKHK2) occurs in approximately **1 in 100,000 to 1 in 125,000** live births, and that at least **214 individuals** with EP300-related syndrome have been identified in medical clinics as of 2024.[6] This suggests that MKHK2 comprises a subset of EP300-related cases, making its prevalence lower than that of EP300-related syndromes overall.

Incidence (new cases per year) has not been formally quantified but can be estimated from prevalence and population demographics. If MKHK prevalence is <1 per 1,000,000, incidence is likely similar in magnitude, given its congenital nature and absence of late-onset forms. MKHK has been reported across multiple continents and ethnic groups, reflecting its origin in de novo mutations rather than population-specific factors.[5][7][8][11][17] There is no evidence of geographic clustering or endemicity.

Sex ratio data are sparse, but case reports include both male and female patients, suggesting no strong sex bias, consistent with autosomal inheritance.[5][7][11][17] Age distribution currently skews toward children, as recognition of adult MKHK is still emerging, but adults have been reported.[5][7][11][17] Over time, as genetic testing becomes more widespread and older individuals are tested, the age spectrum of documented MKHK cases will broaden.

Carrier frequency (heterozygous pathogenic variant prevalence in the general population) is exceedingly low, given the disease’s severe phenotype and negative selection. Based on de novo mutation dynamics and rare familial cases, carrier frequency is likely well under 1 per 100,000 for specific MKHK variants, though precise estimates are not available.[6][8][11][17][13]

In summary, Menke-Hennekam syndrome is an ultra-rare, globally distributed, autosomal dominant congenital disorder, with most cases arising from de novo CREBBP/EP300 exon 30/31 mutations and very few familial clusters.[1][2][5][6][8][11][13][16][17]

## 10. Diagnostics and Biomarkers

### 10.1 Clinical Evaluation and Phenotypic Recognition

Diagnostic evaluation for Menke-Hennekam syndrome begins with **clinical recognition** of its characteristic neurodevelopmental and craniofacial phenotype. Clinicians may suspect MKHK in a child with intellectual disability or global developmental delay, autistic behaviors, short stature, microcephaly, feeding difficulties, recurrent upper airway infections, hearing impairment, and distinctive facial features lacking the broad thumbs and halluces typical of Rubinstein–Taybi syndrome.[1][2][5][7][8][10][11][17] Orphanet’s description of facial features and systemic manifestations provides a useful checklist for clinical suspicion.[11][12]

Differential diagnosis includes **Rubinstein–Taybi syndrome** (RSTS1, RSTS2), which shares intellectual disability and growth delay but differs in facial features (e.g., beaked nose, broad thumbs and halluces), as well as other chromatinopathies such as Kabuki syndrome (KMT2D/KDM6A), SETD2-related disorders, and ASD-associated syndromes like ADNP or CHD8-related disorders.[1][2][5][7][9][11][17] The absence of broad thumbs/halluces in MKHK2, emphasized by Japanese resources, is a key distinguishing feature from RSTS2.[17] Careful evaluation of hand and foot morphology, facial features, and other malformations helps refine differential diagnosis.

Clinical tests used in MKHK evaluation are largely **supportive**, aimed at characterizing systemic involvement rather than providing a disease-specific biomarker. These include brain MRI to detect cerebral anomalies, EEG for epilepsy, audiometry for hearing loss, ophthalmologic exams for vision problems, growth measurements, and developmental assessments using standardized tools.[5][7][11][17] Laboratory tests are generally non-specific; there are no known serum, CSF, or urine biomarkers unique to MKHK. Routine metabolic, endocrine, and hematologic panels are used to rule out other causes of developmental delay.

### 10.2 Genetic Testing Strategies

Definitive diagnosis of Menke-Hennekam syndrome requires **molecular genetic testing** of CREBBP and EP300, with emphasis on exons 30 and 31. OMIM’s entries for MKHK1 and MKHK2 highlight that heterozygous mutations in these exons cause the syndrome.[1][2] Minerva Clinic emphasizes that MKHK1 is caused primarily by point mutations in CREBBP exons 30–31 and that conventional chromosome testing and microarray cannot detect these changes, necessitating sequence-based methods.[8] For MKHK2, Minerva Clinic similarly recommends genetic testing focused on EP300 exons 30–31, ideally using trio exome sequencing (child and both parents) to detect de novo variants.[17]

Recommended testing approaches include **whole exome sequencing (WES)**, which covers all coding exons and can detect missense and small indel variants in CREBBP/EP300, and **targeted gene panels** for neurodevelopmental disorders or chromatinopathies that include CREBBP and EP300 exons 30–31.[7][8][17] WES is particularly valuable when MKHK is not initially suspected, as it allows unbiased detection of variants across many genes.[7] Trio sequencing improves interpretation by identifying de novo variants. **Whole genome sequencing (WGS)** can detect variants in non-coding regions but is not strictly necessary for MKHK, given the known exonic etiology.

Single-gene testing of CREBBP or EP300 may be employed when MKHK is strongly suspected, but these genes are large, and targeted sequencing must ensure coverage of exons 30–31 and adjacent domains.[8][17] Chromosomal microarray (CMA) and karyotyping are useful for detecting large deletions or rearrangements causing RSTS but are largely uninformative for MKHK, as its causative variants are too small to be detected by these methods.[8][9][17] FISH and other cytogenetic techniques likewise play little role in MKHK diagnosis.

ClinVar and ClinVarMiner are important resources for interpreting detected variants, providing information on pathogenicity, previous case reports, and ACMG classifications.[13][14][16] Variants such as CREBBP p.Arg1868Trp and p.Met1872Thr have well-established MKHK associations, facilitating confident diagnosis.[14][16] For novel variants or VUSs in exons 30–31, functional prediction, segregation, and **epigenetic testing** (episignatures) can help refine pathogenicity.

### 10.3 Epigenomic Diagnostics: DNA Methylation Episignatures

An innovative diagnostic tool for Menke-Hennekam syndrome is **DNA methylation episignature analysis**. The 2024 domain-specific study demonstrated that MKHK subtypes (ZZ, TAZ2, ID4) have distinct methylation profiles and defined a domain-specific diagnostic episignature for MKHK-ID4.[3][4] These episignatures can be used to classify individuals based on their methylation pattern, differentiating MKHK from RSTS and other neurodevelopmental syndromes, and confirming uncertain CREBBP/EP300 variants.

Minerva Clinic notes that for MKHK2, “DNA methylation episignature analysis can be used as a supplementary diagnostic test,” especially when genetic variants are suspected but not conclusively interpreted.[17] This involves performing a genome-wide methylation array on peripheral blood DNA and comparing the pattern to reference episignatures using machine learning. A match to the MKHK signature supports diagnosis and variant pathogenicity.

From an NCIT perspective, this corresponds to **NCIT:C10604 (DNA Methylation Analysis)** and **NCIT:C17358 (Biomarker)**, and from an ontological standpoint, episignatures represent higher-order phenotype features reflecting underlying chromatin dysregulation (HP:0030003, *Abnormal DNA methylation profile*). Epigenomic diagnostics are particularly valuable for rare disorders like MKHK, where sequence variants may be novel and functional assays are limited.

### 10.4 Clinical Criteria and Screening

At present, there are no formal **clinical diagnostic criteria** or scoring systems for Menke-Hennekam syndrome akin to those used for some other syndromes. Diagnosis relies on a combination of clinical features and molecular confirmation.[1][2][5][7][11] Because MKHK is extremely rare, **population-based screening** (e.g., newborn screening) is not currently practiced or recommended. Instead, genetic testing is offered to individuals with neurodevelopmental disorders and congenital anomalies suggestive of chromatinopathies.

Carrier screening for MKHK is not undertaken in the general population due to the ultra-low frequency of pathogenic variants and the predominance of de novo mutations. However, **cascade testing** of relatives of affected individuals is recommended to determine carrier status and inform reproductive decision-making.[6][8][17] Prenatal diagnosis and preimplantation genetic testing (PGT) can be offered to families with known pathogenic CREBBP/EP300 variants who wish to avoid recurrence, using targeted sequencing or WES approaches.

In summary, MKHK diagnostics center on clinical recognition, **exome or gene-panel sequencing of CREBBP/EP300 exons 30–31**, and, increasingly, **DNA methylation episignature analysis**, with limited roles for conventional cytogenetics and no specific biochemical biomarkers.[1][2][3][4][5][7][8][11][16][17]

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality, and Life Expectancy

Data on **survival and mortality** in Menke-Hennekam syndrome are limited, as most published cases involve children and adolescents. However, there is no indication that MKHK is typically lethal or markedly reduces life expectancy in the absence of severe comorbidities. Individuals with MKHK have been reported in adolescence and adulthood, suggesting that many survive into later life.[5][7][11][17] Unlike some congenital heart or metabolic disorders, MKHK does not have a high early mortality rate associated with organ failure or metabolic crises.

Mortality, when it occurs, would likely arise from complications such as severe epilepsy, aspiration pneumonia, respiratory infections, or surgical/anesthetic risks associated with craniofacial anomalies, but no MKHK-specific mortality statistics have been published.[5][7][11][12][17] Orphanet does not list MKHK as a disease with known increased mortality in childhood, but notes variable severity and systemic involvement.[11] Therefore, life expectancy is presumed to be **near normal** for many individuals, albeit with increased morbidity and healthcare needs.

### 11.2 Morbidity, Disability, and Quality of Life

Morbidity in Menke-Hennekam syndrome is **substantial**, reflecting its multisystem impact. Intellectual disability and developmental delay contribute to long-term functional impairments in cognition, communication, and adaptive skills.[5][6][7][8][11][17] Autistic behaviors and behavioral disturbances further affect social functioning and mental health. Feeding difficulties, short stature, microcephaly, recurrent infections, hearing impairment, and epilepsy create physical health burdens, frequent medical appointments, hospitalizations, and interventions.[1][2][5][11][12][17]

Disability outcomes vary depending on severity, but many individuals require **lifelong support**, including special education, assistance with daily living, and ongoing therapies.[5][6][8][11][17] Employment and independent living may be challenging or unattainable for those with moderate to severe intellectual disability, while individuals with milder cognitive impairment may achieve greater independence with support. Quality of life measurements specific to MKHK have not been conducted, but extrapolation from similar neurodevelopmental disorders suggests that domains such as mobility, self-care, usual activities, pain/discomfort, and anxiety/depression are impacted, particularly in more severe cases.[5][6][11]

Families experience significant psychosocial burden, including stress, financial strain, and care coordination challenges. Support from specialized clinics, patient organizations, and social services is crucial for improving both patient and family quality of life.[6][8][11][17] From an ICD framework, MKHK contributes to disability codes related to intellectual disability, ASD, and physical impairment.

### 11.3 Prognostic Factors and Predictors

Prognosis in Menke-Hennekam syndrome depends on several factors:

First, the **domain affected** (ZZ, TAZ2, ID4) may influence cognitive and behavioral severity, as suggested by the domain-specific study in which MKHK-ID4 appeared to have somewhat milder intellectual and behavioral features compared with MKHK-ZZ and MKHK-TAZ2.[3][4] However, this is an emerging area of research, and robust prognostic stratification based on domain is not yet established.

Second, the **specific variant** and its functional impact may modulate phenotype severity, as recurrent hotspots such as p.Arg1868 and p.Met1872 in CREBBP show consistent MKHK1 phenotypes but individual variability.[14][16] Third, **comorbidities** such as epilepsy, severe hearing loss, structural brain anomalies, and cryptorchidism influence morbidity and functional outcomes.[5][7][11][17] Fourth, **access to early and ongoing interventions**—developmental therapies, special education, seizure management, hearing aids—strongly affects adaptive functioning and quality of life.[5][6][8][11][17] Fifth, broader **genetic background** and environmental context likely modify resilience and vulnerability, although specific modifiers are not known.

There are currently no established **prognostic biomarkers** (e.g., genomic, proteomic, or epigenomic markers) that predict disease course aside from the general association of domain and variant type with phenotype. DNA methylation episignatures confirm diagnosis but have not yet been correlated with severity. Future studies integrating transcriptomics and imaging could identify markers predictive of cognitive outcome or epilepsy risk.

In summary, Menke-Hennekam syndrome has a variable but generally chronic morbidity profile, with high disability burden but likely near-normal life expectancy for many individuals, modulated by domain, variant, comorbidities, and interventions.[3][4][5][6][7][8][11][17]

## 12. Treatment and Management

### 12.1 Pharmacotherapy and Symptomatic Drug Treatment

There are currently **no medicines designed to treat Menke-Hennekam syndrome itself**, in the sense of targeting the underlying CBP/p300 dysfunction.[6] Simons Searchlight explicitly states, “At this point, there are no medicines designed to treat the syndrome,” underscoring the lack of disease-modifying pharmacotherapy.[6] Consequently, treatment is **symptomatic and supportive**, focusing on managing comorbidities and improving function.

Pharmacologic interventions commonly used in MKHK include **antiepileptic drugs** for seizure control, **psychotropic medications** (e.g., stimulants, SSRIs, atypical antipsychotics) for attention difficulties, anxiety, or behavioral issues, and **gastrointestinal medications** for reflux and constipation.[5][7][11][17] These are chosen based on general clinical guidelines for epilepsy and neurobehavioral disorders rather than MKHK-specific data. Antiepileptic therapy corresponds to NCIT terms such as **NCIT:C15661 (Anticonvulsant Therapy)**, and psychotropic medications map to classes like **NCIT:C614 (Antidepressant)** or **NCIT:C780 (Antipsychotic)**, depending on the agent.

In some cases, **growth hormone therapy** might be considered for severe short stature, though no MKHK-specific studies exist, and risks must be weighed carefully. Hearing aids, cochlear implants, and vision correction devices are essential for sensory impairments.[5][6][11][17] These interventions improve functional abilities and quality of life but do not alter the underlying genetic and epigenetic abnormalities.

### 12.2 Advanced Therapeutics: Gene and RNA-Based Approaches

No **gene therapy, RNA-based therapy, or targeted molecular therapy** currently exists for Menke-Hennekam syndrome. Theoretically, future strategies could involve **CRISPR-based gene editing** to correct specific missense variants in CREBBP/EP300 or **RNA interference or antisense oligonucleotides (ASOs)** to modulate expression of mutant vs. wild-type alleles, but such interventions are at a conceptual stage and would face significant technical and ethical challenges.[3][4][9][10]

CBP/p300 small-molecule modulators have been explored in cancer and other diseases, but applying them to MKHK would require nuanced understanding of domain-specific dysfunction and careful titration to avoid off-target effects.[9][10] Epigenetic editing tools that target specific loci with dCas9–acetyltransferase or demethylase fusions could, in principle, normalize aberrant chromatin states in MKHK, but such approaches remain experimental and have not yet been attempted in human neurodevelopmental disorders.[3][4][9][10]

Thus, while MKHK is mechanistically attractive for precision medicine, **no advanced therapeutics are currently available**, and management focuses on conventional symptomatic treatments.

### 12.3 Surgical and Interventional Procedures

Surgical interventions in Menke-Hennekam syndrome are **supportive and corrective**, addressing structural anomalies. These may include **orchiopexy** for cryptorchidism, **ear tube placement (tympanostomy)** for recurrent otitis media, **adenoidectomy or tonsillectomy** for airway obstruction, and orthopedic or craniofacial surgery for skeletal anomalies.[11] Such procedures follow standard surgical indications and guidelines and are not MKHK-specific.

Feeding difficulties may necessitate temporary or long-term **gastrostomy tube placement** for enteral nutrition, especially in infants with severe swallowing impairment, reflux, or failure to thrive.[8][11][17] This intervention reduces aspiration risk and ensures adequate caloric intake. NCIT terms such as **NCIT:C21015 (Gastrostomy)** and **NCIT:C17173 (Corrective Surgery)** apply.

### 12.4 Supportive Care and Rehabilitation

Supportive and rehabilitative care are the **cornerstones of MKHK management**. Early and ongoing **speech therapy**, **occupational therapy**, **physical therapy**, and **behavioral interventions** (e.g., applied behavior analysis for ASD) are essential for optimizing communication, motor skills, adaptive behavior, and social functioning.[5][6][8][11][17] These interventions correspond to NCIT terms such as **NCIT:C48676 (Developmental Therapy)**, **NCIT:C15273 (Physical Therapy)**, and **NCIT:C17561 (Speech Therapy)**.

Nutritional support, including dietary counseling and management of reflux or constipation, is vital for growth and health. **Psychosocial support** for families, including counseling, respite care, and connection to patient support organizations, mitigates stress and improves care quality.[6][8][11][17] Educational support, including individualized education plans (IEPs) and specialized schooling, is critical for cognitive and adaptive development.

In many cases, MKHK management requires a **multidisciplinary team**, including pediatricians, neurologists, geneticists, developmental specialists, therapists, and social workers. There are no MKHK-specific clinical practice guidelines, but general guidelines for neurodevelopmental disorders and autism are applicable.[5][6][11][17]

### 12.5 Experimental Treatments and Clinical Trials

As of now, there are **no registered clinical trials** specifically targeting Menke-Hennekam syndrome as a primary indication. ClinicalTrials.gov does not list MKHK-specific interventions in the provided sources, and research efforts have focused on **genotype–phenotype correlation and epigenetic profiling** rather than therapeutic development.[3][4][7] MKHK patients may participate in broader neurodevelopmental disorder trials (e.g., for ASD or intellectual disability), but such participation is not MKHK-specific.

Future research may explore small-molecule modulators of CBP/p300, epigenetic therapies, or gene-editing approaches, but these remain at the preclinical or conceptual stage.[3][4][9][10] At present, the most “experimental” aspect of MKHK care is epigenomic diagnostical rather than treatment-related.

In summary, treatment for Menke-Hennekam syndrome is **symptomatic and supportive**, with pharmacotherapy for seizures and behavioral issues, surgery for structural anomalies, and extensive rehabilitative interventions, but no disease-modifying or curative therapies exist.[5][6][8][11][17]

## 13. Prevention and Genetic Counseling

### 13.1 Primary, Secondary, and Tertiary Prevention

**Primary prevention** of Menke-Hennekam syndrome—preventing occurrence of pathogenic CREBBP/EP300 exon 30/31 variants—is not currently feasible in the general population, given the random nature of de novo mutations and the absence of known environmental or behavioral risk factors.[6][8][11][17] For families with known pathogenic variants, however, primary prevention of recurrence is possible through reproductive options such as **preimplantation genetic testing (PGT)** and **prenatal diagnosis**, allowing selection of embryos or fetuses without the pathogenic variant.[6][8][17] These approaches require prior molecular diagnosis in the affected parent and involve genetic counseling to discuss risks, benefits, and ethical considerations.

**Secondary prevention** focuses on early detection and intervention to minimize morbidity and disability. Early identification of MKHK through clinical suspicion and genetic testing enables prompt initiation of developmental therapies, nutritional support, seizure management, and sensory interventions, which can improve outcomes and reduce complications.[5][6][8][11][17] DNA methylation episignature testing may facilitate earlier and more accurate diagnosis in ambiguous cases, enhancing secondary prevention.[3][4][17]

**Tertiary prevention** involves long-term management to prevent complications and maximize function in those already affected. This includes regular monitoring for seizures, infections, hearing and vision problems, and orthopedic issues; proactive management of comorbidities; and ongoing rehabilitative and psychosocial support.[5][6][11][17] Tertiary prevention minimizes secondary disabilities, such as preventable hearing loss due to untreated otitis media or social isolation due to unaddressed behavioral issues.

### 13.2 Screening and Risk Stratification

Given MKHK’s rarity, **population-based screening** (e.g., newborn screening) is not warranted. Screening is instead targeted to individuals with developmental delay and congenital anomalies suggestive of chromatinopathies. Genetic testing of CREBBP/EP300 exons 30–31 is recommended when MKHK is suspected clinically or when exome sequencing reveals variants in these regions.[7][8][17] Risk stratification within families is achieved through **cascade genetic testing** to identify carriers of known pathogenic variants and to inform reproductive decisions.[6][8][17]

Prenatal screening options include **chorionic villus sampling (CVS)** or **amniocentesis** to test fetal DNA for known CREBBP/EP300 variants when parents are carriers, and **non-invasive prenatal testing (NIPT)** is not currently able to detect small missense variants and thus does not play a major role in MKHK screening. PGT involves IVF and embryo biopsy, with targeted sequencing to select embryos without the familial pathogenic variant.[6][8][17]

### 13.3 Genetic Counseling and Public Health Aspects

Genetic counseling is essential for families affected by Menke-Hennekam syndrome. Counselors explain that MKHK is a **genetic condition caused by variants in CREBBP or EP300**, that it is autosomal dominant, and that de novo mutations account for most cases.[6][8][9][17] They emphasize that parents did not cause the mutation through behavior or exposures and discuss the 50% recurrence risk for carriers and the low but non-zero risk due to germline mosaicism in de novo cases.[6][8][17]

Counseling also covers the implications for siblings and extended family, options for prenatal and preimplantation testing, and psychosocial support resources. Public health interventions are limited to improving access to genetic testing, counseling, and specialized care for rare disease patients, rather than population-wide measures.[11][17] Environmental interventions to reduce mutation risk are not currently practical or evidence-based for MKHK.

In summary, prevention in Menke-Hennekam syndrome focuses on **genetic counseling and reproductive options** for families with known variants, and on **early diagnosis and intervention** to reduce morbidity, rather than on primary environmental risk modification.[6][8][11][17]

## 14. Other Species and Natural Disease

### 14.1 Cross-Species Considerations

Menke-Hennekam syndrome is defined in humans and arises from germline variants in human CREBBP and EP300. There are **orthologous genes** in many other species, including mice, rats, zebrafish, Drosophila, and C. elegans, and CBP/p300 function is evolutionarily conserved, particularly in transcriptional coactivation and chromatin modification.[4][7][9][10] However, no **naturally occurring MKHK-like syndrome** has been reported in companion animals or livestock, and the Online Mendelian Inheritance in Animals (OMIA) does not list a specific analog.[1][2][10][11]

In veterinary medicine, CBP/p300-related conditions are mainly studied in cancer (somatic mutations) rather than congenital syndromes. Thus, MKHK has limited direct veterinary relevance, although understanding CBP/p300 function in animal models contributes indirectly to mechanistic insights. There is no zoonotic aspect or cross-species transmission risk, as MKHK is not infectious.

### 14.2 Comparative Pathology and Evolutionary Conservation

Comparative pathology highlights the **conservation of CBP/p300 roles** in development and transcriptional regulation across species. CBP/p300 mutations in mice and other organisms produce phenotypes involving growth defects, craniofacial anomalies, and neurobehavioral abnormalities, paralleling aspects of human RSTS and MKHK.[4][7][9][10] These models support the idea that CBP/p300 are master regulators of developmental gene expression networks and that domain-specific alterations can have targeted phenotypic effects.

Evolutionary analysis indicates that CBP/p300 domains such as ZZ, TAZ2, and the HAT domain are highly conserved, with amino acid residues targeted by MKHK variants often conserved across mammals, underscoring their functional importance.[3][4][9][10] Thus, MKHK illustrates how **conserved domains** in chromatin regulators can be sensitive points for pathogenic variation, offering insights into genotype–phenotype specificity.

## 15. Model Organisms and Experimental Systems

### 15.1 Mouse and Other Model Organisms

While no animal model has been created specifically to recapitulate Menke-Hennekam syndrome’s domain-specific exon 30/31 variants, **mouse models of CREBBP and EP300 haploinsufficiency** have been developed to study Rubinstein–Taybi syndrome and CBP/p300 function more generally. Heterozygous Crebbp or Ep300 knockout mice exhibit growth retardation, craniofacial anomalies, learning and memory deficits, and altered histone acetylation, paralleling aspects of RSTS.[4][7][9][10] These models demonstrate that CBP/p300 dosage and function are critical for normal development and cognitive function, supporting MKHK’s mechanistic framework.

Conditional knockout models targeting CBP/p300 in specific tissues (e.g., brain, heart, limb buds) show tissue-specific phenotypes and help dissect cell-type-specific roles. While these models are more relevant to loss-of-function scenarios, they provide a foundation for future **knock-in models** that could introduce MKHK-specific missense variants in exons 30–31, enabling detailed study of domain-specific effects.[4][7][9][10] Zebrafish and Drosophila models with CBP/p300 ortholog disruptions also exhibit developmental abnormalities.

### 15.2 In Vitro and Cellular Models

In vitro models include **cell lines** expressing mutant CBP/p300 or primary cells from patients. For example, fibroblasts or lymphoblastoid cell lines derived from MKHK patients could be used to study histone acetylation, DNA methylation, and gene expression changes, especially those linked to domain-specific variants.[3][4][7][9][10] Epigenomic assays in such cells have already been performed for DNA methylation profiling.[3][4] Future work could employ CRISPR-Cas9 editing to introduce MKHK variants into human induced pluripotent stem cells (iPSCs), followed by differentiation into neurons and other cell types to model disease at the cellular level.

Such **cellular models** would allow investigation of synaptic function, neuronal morphology, and activity-dependent gene expression in MKHK, and testing of potential small-molecule modulators of CBP/p300 activity.[3][4][9][10] However, these models remain conceptual at present; no published studies have yet reported MKHK-specific iPSC or organoid models.

### 15.3 Model Limitations and Applications

Existing CBP/p300 models primarily capture **haploinsufficiency** rather than domain-specific gain-of-function or dominant-negative mechanisms. As a result, they more closely mirror RSTS than MKHK. This limits their ability to fully emulate MKHK’s phenotypic and epigenomic complexity, particularly the distinct DNA methylation episignatures.[3][4][9][10] Nonetheless, they provide valuable insights into CBP/p300 biology and illustrate how perturbations in these genes can affect development and cognition.

For MKHK research, future model development should focus on **domain-specific knock-in models** and **cellular systems** that incorporate exon 30/31 missense variants. These would allow mechanistic dissection of how ZZ, TAZ2, and ID4 domain alterations translate into specific gene expression and methylation changes, and how these changes affect neuronal and craniofacial development.

Applications of such models include testing potential therapeutic interventions (e.g., epigenetic drugs, CBP/p300 modulators, gene-editing strategies), studying gene–environment interactions, and validating episignatures. Model organism databases (MGI, ZFIN, FlyBase) will be useful for cataloging future MKHK-like models as they are developed.

## Conclusion

Menke-Hennekam syndrome exemplifies a **domain-specific Mendelian chromatinopathy**, in which missense and in-frame indel variants confined to exons 30 and 31 of the CBP/p300 genes CREBBP and EP300 disrupt specific coactivator domains (ZZ, TAZ2, ID4), leading to altered transcriptional regulation and epigenetic states that manifest as a distinctive neurodevelopmental and craniofacial syndrome.[1][2][3][4][5][7][8][9][10][11][17] Clinically, MKHK is characterized by variable intellectual disability, global developmental delay, autistic behavior, short stature, microcephaly, feeding difficulties, recurrent upper airway infections, hearing impairment, and a characteristic facial gestalt without the broad thumbs/halluces of Rubinstein–Taybi syndrome, along with additional malformations such as cryptorchidism and cerebral anomalies in some cases.[1][2][5][7][8][10][11][12][17]

Genetically, MKHK is an **autosomal dominant** disorder with high penetrance, most often arising from de novo germline variants, and mapped to OMIM entries 618332 (MKHK1, CREBBP) and 618333 (MKHK2, EP300), Orphanet ORPHA:592574, KEGG H02650, and MONDO:0020774.[1][2][10][11][13][15][18] ClinVarMiner collates hundreds of variants, with pathogenic/likely pathogenic missense and in-frame indels clustering in exon 30/31 positions, such as CREBBP p.Arg1868 and p.Met1872.[13][14][16] Mechanistically, MKHK differs from RSTS in that its variants alter CBP/p300 function through gain-of-function or dominant-negative effects rather than haploinsufficiency, leading to domain-specific transcriptional and DNA methylation changes.[3][4][5][8][9][10]

The pathophysiologic chain begins with exon 30/31 variants, progresses through domain-specific CBP/p300 dysfunction, aberrant histone acetylation and transcriptional regulation, domain-specific DNA methylation episignatures, and culminates in disrupted development of neurons, cranial neural crest cells, and growth-related tissues, producing the MKHK phenotype.[3][4][7][9][10][11] Epigenetic profiling has revealed distinct methylation signatures for MKHK-ZZ, MKHK-TAZ2, and MKHK-ID4, enabling innovative **episignature-based diagnostics** that complement sequence analysis and support variant interpretation.[3][4][17]

Diagnostic strategies rely on clinical recognition, **whole exome or targeted sequencing of CREBBP/EP300 exons 30–31**, and increasingly, DNA methylation assays, with limited roles for cytogenetics and no specific biochemical biomarkers.[1][2][3][4][5][7][8][11][16][17] Treatment is **symptomatic and supportive**, including antiepileptic drugs, behavioral and developmental therapies, sensory interventions, surgical correction of malformations, and comprehensive multidisciplinary care, with no disease-modifying therapies yet available.[5][6][8][11][17] Prevention focuses on genetic counseling, prenatal and preimplantation testing for families with known variants, and early diagnosis to optimize developmental interventions.[6][8][11][17]

Research frontiers in Menke-Hennekam syndrome include further delineation of domain-specific phenotypic spectra, expansion of episignature-based diagnostics, development of **domain-specific knock-in and cellular models**, and exploration of targeted therapeutic approaches that modulate CBP/p300 function or correct downstream epigenetic and transcriptional abnormalities.[3][4][9][10] MKHK thus serves as a paradigmatic example of how precise mapping of variants within chromatin regulator genes can reveal discrete clinical and epigenomic entities, and offers a rich framework for integrating genomic, epigenomic, and clinical data into computational disease models and precision medicine strategies.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 4 |
| Unverifiable | 5 |
| Terms whose name was checked | 46 |
| Terms named correctly | 23 |
| Terms named as a **different** term | 16 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C16084` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Observational Study**
- `NCIT:C48676` (2 mentions) - the report calls it "Developmental Therapy"; NCIT calls it **Schedule III Substance**
- `NCIT:C15661` (2 mentions) - the report calls it "Anticonvulsant Therapy"; NCIT calls it **ATCC**
- `NCIT:C17358` (2 mentions) - the report calls it "Biomarker"; NCIT calls it **DCC Gene**
- `NCIT:C10604` (2 mentions) - the report calls it "DNA Methylation Analysis"; NCIT calls it **Cisplatin/Cyclophosphamide/Paclitaxel**
- `NCIT:C12219` (1 mention) - the report calls it "Lifestyle Factor"; NCIT calls it **Anatomic Structure, System, or Substance**
- `NCIT:C16916` (1 mention) - the report calls it "Behavioral Intervention"; NCIT calls it **Niger**
- `UBERON:0003114` (1 mention) - the report calls it "craniofacial skeleton"; UBERON calls it **pharyngeal arch 3**
- `UBERON:0000020` (2 mentions) - the report calls it "auditory system", "ear"; UBERON calls it **sense organ**
- `UBERON:0001733` (1 mention) - the report calls it "nasal cavity"; UBERON calls it **soft palate**
- `UBERON:0000984` (1 mention) - the report calls it "testis"; UBERON calls it **imaginal disc-derived wing**
- `NCIT:C614` (1 mention) - the report calls it "Antidepressant"; NCIT calls it **Lidocaine**
- `NCIT:C780` (1 mention) - the report calls it "Antipsychotic"; NCIT calls it **Attenuated Corynebacterium Parvum**
- `NCIT:C21015` (1 mention) - the report calls it "Gastrostomy"; NCIT calls it **BMP/Retinoic Acid-Inducible Neural-Specific Protein 1**
- `NCIT:C15273` (1 mention) - the report calls it "Physical Therapy"; NCIT calls it **Longitudinal Study**
- `NCIT:C17561` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Fusion Protein**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016573` (obsolete histone acetylation) (3 mentions)
- `HP:0000735` (obsolete Impaired social interactions) (1 mention) - replaced by `HP:0012760`
- `GO:0006306` (obsolete DNA methylation) (1 mention)
- `PR:000004536` (obsolete ATP-binding cassette sub-family A member 8) (1 mention) - replaced by `PR:000003546`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001250` (1 mention) - the report calls it "epilepsy"; HP calls it **Seizure**, and lists "Epilepsy" among its other names
- `GO:0016573` (3 mentions) - the report calls it "histone acetylation"; GO calls it **obsolete histone acetylation**
- `GO:0006357` (2 mentions) - the report calls it "regulation of transcription from RNA polymerase II promoter"; GO calls it **regulation of transcription by RNA polymerase II**, and lists "regulation of transcription from RNA polymerase II promoter" among its other names
- `GO:0006306` (1 mention) - the report calls it "DNA methylation"; GO calls it **obsolete DNA methylation**
- `GO:0030182` (1 mention) - the report calls it "neuronal differentiation"; GO calls it **neuron differentiation**
- `GO:0008285` (1 mention) - the report calls it "negative regulation of cell proliferation"; GO calls it **negative regulation of cell population proliferation**, and lists "negative regulation of cell proliferation" among its other names
- `NCIT:C17173` (1 mention) - the report calls it "Corrective Surgery"; NCIT calls it **Surgery**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0000020` - called "auditory system", "ear"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `HSA`.