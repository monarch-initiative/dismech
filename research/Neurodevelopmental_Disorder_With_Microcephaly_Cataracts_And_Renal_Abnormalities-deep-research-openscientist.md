---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-22T16:27:29.658960'
end_time: '2026-10-22T17:01:08.225082'
duration_seconds: 2018.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Microcephaly, Cataracts, And Renal
    Abnormalities
  mondo_id: MONDO:0060664
  category: Mendelian
  causal_genes: GEMIN4
  omim_id: not recorded
  synonyms: NEDMCR
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
citation_count: 7
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 13
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35052432
  relevance_assessed: 8
  on_topic: 4
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 68
  verified: 65
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.015
  labels_checked: 47
  labels_matching: 38
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0060664
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with microcephaly, cataracts, and
      renal abnormalities
  - term_id: DOID:0081263
    reported_labels:
    - DOID
    ontology_label: neurodevelopmental disorder with microcephaly, cataracts, and
      renal abnormalities
  - term_id: NCIT:C15335
    reported_labels:
    - Nutritional Support
    ontology_label: Technology Assessment
  labels_variant: 6
  unresolved_terms:
  - UBERON:0000340
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Neurodevelopmental_Disorder_With_Microcephaly_Cataracts_And_Renal_Abnormalities-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Neurodevelopmental_Disorder_With_Microcephaly_Cataracts_And_Renal_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Microcephaly, Cataracts, And Renal Abnormalities
- **MONDO ID:** MONDO:0060664 (if available)
- **Causal gene(s):** GEMIN4
- **OMIM:** not recorded
- **Synonyms:** NEDMCR
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Microcephaly, Cataracts, And Renal Abnormalities** covering all of the
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

# Neurodevelopmental Disorder With Microcephaly, Cataracts, And Renal Abnormalities (NEDMCR) — GEMIN4

**Disease:** Neurodevelopmental Disorder With Microcephaly, Cataracts, And Renal Abnormalities (NEDMCR)
**Causal gene:** **GEMIN4** (HGNC:15717; NCBI Gene 50628; 17p13.3)
**MONDO:** MONDO:0060664 | **OMIM:** #617913 | **DOID:** 0081263 | **UMLS/MedGen:** C4693567

---

## Summary

**Neurodevelopmental Disorder With Microcephaly, Cataracts, And Renal Abnormalities (NEDMCR)** is an ultra-rare, autosomal-recessive multisystem syndrome caused by **biallelic (homozygous) pathogenic variants in GEMIN4**, a gene on chromosome 17p13.3 encoding a core subunit of the Survival of Motor Neuron (SMN) protein complex. The causal gene is **GEMIN4** (Gem-associated protein 4, UniProt P57678) — not any of the other genes implicated in similarly named microcephaly/cataract syndromes. GEMIN4 functions in the cytoplasmic assembly and maturation of Sm-class small nuclear ribonucleoproteins (snRNPs) that are essential for pre-mRNA splicing, and it additionally participates (with Gemin3/DDX20 and Argonaute AGO2/eIF2C2) in a microRNA-containing ribonucleoprotein (miRNP) complex. Partial loss of GEMIN4 function is believed to impair snRNP biogenesis and microRNA-mediated gene regulation in developing tissues, producing the characteristic triad of neurodevelopmental impairment, congenital cataracts, and renal abnormalities.

The disorder was first delineated in prescreened consanguineous families (Alazami et al. 2015) and independently linked to GEMIN4 through pediatric-cataract genomics (Patel et al. 2017). The largest cohort to date comprises 16 patients from 11 unrelated Saudi consanguineous families (Altassan 2022), in whom only **two recurrent homozygous missense founder alleles — c.314C>T (p.Pro105Leu) and c.2452T>C (p.Trp818Arg)** — accounted for all affected individuals, consistent with a strong founder effect. A third novel homozygous variant, c.440A>G (p.His147Arg), was reported in two siblings (Aldhalaan 2021). All reported patients are homozygous, and the gene shows no evidence of haploinsufficiency (gnomAD pLI ≈ 0), consistent with a recessive, hypomorphic loss-of-function mechanism rather than dominant toxicity.

Clinically, **global developmental delay is the constant feature**, with microcephaly, congenital cataract, seizures, hypotonia/spasticity, and variable renal (hydronephrosis, nephrocalcinosis, renal hypoplasia, tubulopathy), skeletal (osteopenia, epiphyseal dysplasia), and ophthalmologic (optic atrophy) manifestations. Onset is congenital/infantile. There is **no disease-specific or curative therapy**; management is multidisciplinary and supportive, and prevention rests on genetic counseling, carrier/cascade screening, and prenatal/preimplantation genetic testing in at-risk consanguineous families. Model-organism evidence (embryonic-lethal Gemin4-null mouse; Drosophila neuronal knockdown with developmental/motor defects) supports GEMIN4 essentiality and the pathogenic relevance of its loss.

---

## 1. Disease Information

NEDMCR is a Mendelian, autosomal-recessive neurodevelopmental syndrome defined by the combination of microcephaly, congenital cataracts, and renal abnormalities on a background of severe global developmental delay. Information is derived from **aggregated disease-level resources** (OMIM, HPO, MONDO) and from a small number of **individual-patient case series** from consanguineous populations rather than from large EHR datasets.

**Key identifiers (consolidated):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0060664 |
| OMIM (phenotype) | #617913 |
| DOID | DOID:0081263 |
| UMLS / MedGen | C4693567 |
| Orphanet | No dedicated term retrievable |
| MeSH | No dedicated term; indexed via components — Microcephaly (D008831), Cataract (D002386), Neurodevelopmental Disorders (D065886) |

**Synonyms / alternative names:** NEDMCR; "GEMIN4-related neurodevelopmental disorder with microcephaly, cataract, and renal abnormalities." Gene aliases: HC56, HCAP1, HHRF-1, p97.

> "Pathogenic variants in GEMIN4 have recently been linked to an inherited autosomal recessive neurodevelopmental disorder characterized with microcephaly, cataracts, and renal abnormalities (NEDMCR syndrome)" — [PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)

---

## 2. Etiology

**Primary cause — genetic.** NEDMCR is caused by **biallelic (homozygous) pathogenic variants in GEMIN4**. The disease is monogenic and Mendelian; there is no established environmental or infectious contribution. GEMIN4 was "independently mutated in families with a syndrome of cataract, global developmental delay with or without renal involvement" ([PMID: 27878435](https://pubmed.ncbi.nlm.nih.gov/27878435/)).

**Genetic risk factors.** The dominant genetic risk determinant is **consanguinity**: all reported families are consanguineous (predominantly Saudi), and affected individuals are homozygous for founder alleles. Two founder missense variants — **p.Pro105Leu (c.314C>T)** and **p.Trp818Arg (c.2452T>C)** — explain the entire largest cohort, indicating a founder effect. No susceptibility loci or modifier genes have been established.

**Environmental risk factors / protective factors / gene–environment interactions.** None identified or applicable. As a fully penetrant recessive Mendelian disorder, environmental modifiers have not been described. The only operative "protective" factor at the population level is the absence of two pathogenic alleles (i.e., non-carrier or heterozygous carrier status, which is asymptomatic).

---

## 3. Phenotypes

Phenotype data derive primarily from HPO annotations for OMIM:617913 (38 annotations across the initial 3-patient curation) and from case series (Altassan 2022, n=16; Aldhalaan 2021, n=2; Patel 2017). **Global developmental delay is constant**, with variable ophthalmologic, renal, and skeletal involvement. Onset is congenital/infantile; the course is severe and non-remitting, with major impact on quality of life (profound developmental disability, often non-ambulatory and non-verbal).

> "All patients shared global developmental delay with variable ophthalmological, renal, and skeletal manifestations." — [PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)

> "Neurodevelopmental Impairment with Severe Microcephaly, Spastic Quadriplegia, Epilepsy, and Cataracts" — [PMID: 35052432](https://pubmed.ncbi.nlm.nih.gov/35052432/)

### Phenotype table with HPO terms and frequency (HPO/OMIM:617913 curation; frequency denominators small)

| Phenotype | HPO term | Frequency | Type |
|---|---|---|---|
| Seizure | HP:0001250 | Constant (3/3) | Clinical sign (neurologic) |
| Severe global developmental delay | HP:0011344 | Constant (3/3) | Behavioral/cognitive |
| Cataract | HP:0000518 | Constant (3/3) | Physical manifestation (ocular) |
| Microcephaly | HP:0000252 | Constant (3/3) | Physical manifestation |
| Gastroesophageal reflux | HP:0002020 | Constant (3/3) | Clinical sign (GI) |
| Infantile onset | HP:0003593 | Constant (3/3) | Onset descriptor |
| Hypotonia | HP:0001252 | Frequent (2/3) | Clinical sign (neurologic) |
| Brain atrophy | HP:0012444 | Variable (1/3) | Imaging/structural |
| Delayed CNS myelination | HP:0002188 | Variable (1/3) | Imaging/structural |
| Inferior cerebellar vermis hypoplasia | HP:0007068 | Variable (1/3) | Imaging/structural |
| Optic atrophy | HP:0000648 | Variable (1/3) | Ocular |
| Absent speech | HP:0001344 | Variable (1/3) | Behavioral |
| Inability to walk | HP:0002540 | Variable (1/3) | Motor |
| Spasticity | HP:0001257 | Variable (1/3) | Neurologic |
| Growth delay | HP:0001510 | Variable (1/3) | Growth |
| Micrognathia | HP:0000347 | Variable (1/3) | Craniofacial |
| High palate | HP:0000218 | Variable (1/3) | Craniofacial |
| Renal hypoplasia | HP:0000089 | Variable (1/3) | Renal (structural) |
| Hydronephrosis | HP:0000126 | Variable (1/3) | Renal (structural) |
| Nephrocalcinosis | HP:0000121 | Variable (1/3) | Renal |
| Renal artery stenosis | HP:0001920 | Variable (1/3) | Renal/vascular |
| Aminoaciduria | HP:0003355 | Variable (1/3) | Laboratory (tubulopathy) |
| Hypocalcemia | HP:0002901 | Variable (1/3) | Laboratory |
| Hypokalemia | HP:0002900 | Variable (1/3) | Laboratory |
| Hyponatremia | HP:0002902 | Variable (1/3) | Laboratory |
| Osteopenia | HP:0000938 | Variable (1/3) | Skeletal |
| Epiphyseal dysplasia | HP:0002656 | Variable (1/3) | Skeletal |
| Congenital hip dislocation | HP:0001374 | Variable (1/3) | Skeletal |
| Recurrent lower respiratory infections | HP:0002783 | Variable (1/3) | Infectious/respiratory |
| Hypertension | HP:0000822 | Variable (1/3) | Cardiovascular |
| Splenomegaly | HP:0001744 | Variable (1/3) | Hematologic/abdominal |
| Feeding difficulties | HP:0011968 | Variable (1/3) | GI/feeding |
| Dysphagia | HP:0002015 | Variable (1/3) | GI/feeding |
| Autosomal recessive inheritance | HP:0000007 | — | Inheritance |

---

## 4. Genetic / Molecular Information

**Causal gene.** **GEMIN4** (Gem-associated protein 4): HGNC:15717; NCBI Gene 50628; Ensembl ENSG00000179409; UniProt P57678; OMIM gene *606969; canonical transcript ENST00000319004 / **NM_015721**; locus **17p13.3**. Aliases: HC56, HCAP1, HHRF-1, p97.

**Pathogenic variants.** All reported disease alleles are **homozygous missense** variants:

| Variant (cDNA) | Protein | Zygosity | Classification | Source |
|---|---|---|---|---|
| c.314C>T | p.Pro105Leu | Homozygous | Pathogenic (founder) | Altassan 2022 ([PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)) |
| c.2452T>C | p.Trp818Arg | Homozygous | Pathogenic (founder) | Altassan 2022 |
| c.440A>G (exon 2) | p.His147Arg | Homozygous | Novel; in silico + structural support | Aldhalaan 2021 ([PMID: 35052432](https://pubmed.ncbi.nlm.nih.gov/35052432/)) |
| c.226A>G | p.Lys76Glu | — | VUS (ClinVar, under NEDMCR) | ClinVar |
| — | p.Phe125fs | — | Likely pathogenic (ClinVar) | ClinVar |

> "Only two missense, homozygous, pathogenic variants were found in all affected patients, suggesting a founder effect" — [PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)

> "we identified a novel variant in GEMIN4 (NM_015721:exon2:c.440A>G:p.His147Arg) in two siblings from a consanguineous Saudi family" — [PMID: 35052432](https://pubmed.ncbi.nlm.nih.gov/35052432/)

**Allele frequency (gnomAD v4).** All disease alleles are ultra-rare: p.Trp818Arg exome AF = 4.1×10⁻⁶ (no homozygotes); p.Pro105Leu absent from gnomAD; p.Lys76Glu AF = 4.1×10⁻⁶ (exomes) / 2.0×10⁻⁵ (genomes).

**Constraint / functional consequence.** GEMIN4 is **not haploinsufficient**: gnomAD pLI ≈ 0, observed/expected LoF (oe_lof) = 0.77 (90% CI 0.62–0.95), missense Z = 0.09. Heterozygous loss is tolerated and asymptomatic; disease requires biallelic hypomorphic alleles. The mechanism is **partial loss of function (hypomorphic)** — complete loss is embryonic-lethal in mouse, so viable human disease reflects residual-but-reduced GEMIN4 activity. Variants are **germline**; no somatic involvement.

**Modifier genes / epigenetics / chromosomal abnormalities.** None established. No DNA-methylation signature, large structural variant, or aneuploidy is associated with NEDMCR.

---

## 5. Environmental Information

**Not applicable.** NEDMCR is a monogenic autosomal-recessive disorder with no established environmental, lifestyle, or infectious contribution. The relevant population-level factor is **consanguinity**, which increases homozygosity for founder alleles but is a demographic/genetic rather than environmental cause.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic missense variants in GEMIN4** (e.g., p.Pro105Leu, p.Trp818Arg) **result in** a GEMIN4 protein with reduced function (germline, recessive).
2. Reduced GEMIN4 function **leads to** impaired assembly/maturation of the SMN complex, of which GEMIN4 is a core subunit (*inferred from GEMIN4's established role in the SMN complex*).
3. Impaired SMN-complex activity **results in** deficient cytoplasmic assembly and maturation of Sm-class spliceosomal snRNPs and reduced nuclear import of snRNPs/SMN complex (*GEMIN4 carries NLS motifs and drives nuclear import of SMN/Gemins*).
4. Deficient snRNP biogenesis **leads to** perturbed pre-mRNA splicing — and, via the branch below, altered microRNA regulation — compromising RNA metabolism in developing tissues (*inferred; splicing defects not yet directly demonstrated in patient tissue*).
   - **Branch (miRNP):** Reduced GEMIN4 **also impairs** the Gemin3(DDX20)/Gemin4/AGO2 miRNP complex, **leading to** dysregulated microRNA-mediated translational repression of target mRNAs.
5. Disrupted RNA metabolism in highly transcription/splicing-dependent, proliferative developmental tissues (neurons, lens epithelium, renal epithelium) **results in** cell dysfunction/death and failed tissue morphogenesis (*inferred tissue-specific vulnerability*).
6. This **produces** the clinical phenotypes: reduced neuronal proliferation/survival → **microcephaly, brain atrophy, developmental delay, seizures**; lens fiber dysfunction → **congenital cataract**; renal developmental/epithelial dysfunction → **renal hypoplasia, hydronephrosis, nephrocalcinosis, tubulopathy**.

### Supporting molecular detail

- **Molecular pathways / cellular processes.** Core process is **spliceosomal snRNP assembly** (GO:0000387) within the SMN complex, plus **rRNA processing** (GO:0006364) and **miRNA-mediated gene silencing**. "Gemin4 is a member of the Survival Motor Neuron (SMN) protein complex, which is responsible for the assembly and maturation of Sm-class small nuclear ribonucleoproteins (snRNPs)" ([PMID: 29371219](https://pubmed.ncbi.nlm.nih.gov/29371219/)).
- **Nuclear import role.** "Gemin4 overexpression drives SMN and the other Gemin proteins from the cytoplasm into the nucleus" ([PMID: 29371219](https://pubmed.ncbi.nlm.nih.gov/29371219/)), implicating GEMIN4 in nuclear import of the SMN complex and Cajal-body dynamics.
- **miRNP branch.** "Gemin3 and Gemin4 are also in a separate complex that contains eIF2C2, a member of the Argonaute protein family. This novel complex is a large approximately 15S RNP that contains numerous microRNAs" ([PMID: 11914277](https://pubmed.ncbi.nlm.nih.gov/11914277/)). In neuronal cells, "the miRNP proteins eIF2C2 … Gemin3, and Gemin4 along with miRNAs cosediment with polyribosomes" and physically associate with target mRNAs, supporting a role in **translational repression** ([PMID: 14970384](https://pubmed.ncbi.nlm.nih.gov/14970384/)).
- **Protein dysfunction.** Missense substitutions (Pro105Leu, Trp818Arg, His147Arg) are predicted to impair protein function/stability or interaction surfaces (in silico and structural modeling, Aldhalaan 2021) rather than cause complete null — consistent with a hypomorphic, partial loss-of-function effect.
- **Cell types / GO–CL/UBERON annotations.** Affected cell populations: neurons (CL:0000540) and neural progenitors, lens fiber/epithelial cells (CL:0000573/CL:0002224), renal epithelial cells (CL:0002518). Relevant biological processes: GO:0000387 (spliceosomal snRNP assembly), GO:0006364 (rRNA processing), GO:0035195 (miRNA-mediated gene silencing). Cellular compartments: SMN complex (GO:0032797), Cajal body (GO:0015030), gems (GO:0097504), nucleolus (GO:0005730), cytoplasm (GO:0005737).

No disease-specific transcriptomic, proteomic, metabolomic, or lipidomic patient profiling is available; mechanism is inferred from GEMIN4's biochemistry and model systems.

### Mechanistic model (ASCII)

```
  Biallelic hypomorphic GEMIN4 missense variants (p.Pro105Leu / p.Trp818Arg / p.His147Arg)
                                   │  (germline, autosomal recessive)
                                   ▼
             Reduced GEMIN4 protein function  (partial LoF; complete null = embryonic lethal)
                                   │
                                   ▼
             Impaired SMN complex assembly / maturation  (GEMIN4 = core subunit)
                     │                                   │
                     ▼                                   ▼
   Deficient Sm-snRNP biogenesis            Dysregulated Gemin3/Gemin4/AGO2 miRNP
   + reduced nuclear import of snRNPs       (altered miRNA translational repression)
                     │                                   │
                     └──────────────┬────────────────────┘
                                    ▼
          Perturbed RNA metabolism in developmentally active tissues
          (neurons/neural progenitors, lens epithelium, renal epithelium)
                                    │
             ┌──────────────────────┼──────────────────────┐
             ▼                      ▼                       ▼
   Neuronal dysfunction/     Lens fiber             Renal developmental /
   reduced proliferation     dysfunction            epithelial dysfunction
             │                      │                       │
             ▼                      ▼                       ▼
   Microcephaly, brain       Congenital             Renal hypoplasia, hydronephrosis,
   atrophy, delay, seizures  cataract               nephrocalcinosis, tubulopathy
```

The unifying concept is that GEMIN4, as a core subunit of the **SMN complex**, is a general RNA-metabolism factor required for snRNP biogenesis (and miRNP function). Hypomorphic variants spare viability but reduce functional output below the threshold required by the most biosynthetically demanding developmental tissues — explaining the convergence on brain, lens, and kidney. Upstream steps (mutation → SMN-complex impairment) are well supported by GEMIN4 biochemistry; the tissue-specific downstream steps are **inferred** and have not been directly demonstrated in patient tissue.

---

## 7. Anatomical Structures Affected

- **Primary organs / systems — nervous system (UBERON:0001016):** brain (UBERON:0000955) with microcephaly, brain atrophy, delayed myelination, inferior cerebellar vermis hypoplasia (UBERON:0004086).
- **Eye (UBERON:0000970):** lens (UBERON:0000965) — congenital cataract; optic nerve (UBERON:0000941) — optic atrophy. Cataracts are typically **bilateral**.
- **Kidney (UBERON:0002113) / renal system:** renal hypoplasia, hydronephrosis, nephrocalcinosis, renal artery stenosis, tubulopathy (aminoaciduria, electrolyte wasting).
- **Skeletal system (UBERON:0001434):** osteopenia, epiphyseal dysplasia, congenital hip dislocation; craniofacial — micrognathia (UBERON:0000340), high palate.
- **Secondary involvement:** respiratory (recurrent lower respiratory infections — often aspiration-related), gastrointestinal (GERD, dysphagia, feeding difficulties), cardiovascular (hypertension), and splenomegaly.
- **Subcellular compartments (GO Cellular Component):** SMN complex (GO:0032797), SMN–Sm protein complex (GO:0034719), snRNP complex (GO:0030532), Cajal body (GO:0015030), gems (GO:0097504), nuclear body (GO:0016604), nucleolus (GO:0005730), nucleoplasm (GO:0005654), cytosol (GO:0005829).

---

## 8. Temporal Development

- **Onset:** congenital / infantile (HP:0003593). Cataracts and microcephaly are congenital; developmental delay and seizures manifest in infancy.
- **Onset pattern:** chronic, insidious with respect to developmental trajectory; seizures may present acutely.
- **Progression:** severe, non-remitting developmental disability. The neurologic phenotype is largely static-to-progressive (brain atrophy and spastic quadriplegia at the severe end). No relapsing-remitting pattern.
- **Duration:** lifelong, chronic. No spontaneous remission.
- **Critical period:** fetal/early-infant neurodevelopment and lens/kidney organogenesis represent the window of vulnerability; there is no established therapeutic window for intervention given the developmental timing.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007); all patients homozygous. Penetrance appears complete in biallelic carriers; expressivity is variable (notably renal, skeletal, and ophthalmologic features).
- **Epidemiology:** ultra-rare; no formal prevalence/incidence estimates. Reported almost exclusively in consanguineous **Saudi** families. The largest series is 16 patients from 11 families.
- **Founder effect:** two recurrent founder alleles (p.Pro105Leu, p.Trp818Arg) dominate the Saudi cohort. Carrier frequencies are not formally established but alleles are ultra-rare globally (gnomAD AF ≤ ~4×10⁻⁶).
- **Consanguinity:** central — homozygosity for rare founder alleles arises through consanguineous unions.
- **Sex ratio / age distribution:** no sex predilection reported (recessive); affected individuals present in infancy/childhood.
- **Genetic anticipation / germline mosaicism:** not applicable / not reported.

> "Only two missense, homozygous, pathogenic variants were found in all affected patients, suggesting a founder effect" — [PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)

---

## 10. Diagnostics

**Molecular diagnosis is definitive.** The disorder was discovered and is diagnosed by **whole-exome sequencing** (Alazami 2015) with Sanger confirmation (Aldhalaan 2021). In founder populations, **targeted single-variant/single-gene testing** for the recurrent alleles (c.314C>T/p.Pro105Leu; c.2452T>C/p.Trp818Arg) is appropriate and cost-effective.

**Recommended diagnostic approach:**

| Modality | Utility in NEDMCR |
|---|---|
| Whole-exome sequencing (WES) | High — primary discovery and diagnostic tool |
| Whole-genome sequencing (WGS) | Useful if WES negative |
| Targeted / single-gene GEMIN4 testing | High in Saudi founder populations (known recurrent alleles) |
| Gene panels (intellectual disability / cataract / nephropathy) | GEMIN4 should be included |
| Chromosomal microarray / karyotype / FISH | Low yield (no structural lesion) |
| mtDNA / repeat-expansion testing | Not applicable |

**Supportive workup (phenotype characterization):** brain MRI (atrophy, delayed myelination, cerebellar vermis hypoplasia); EEG (seizures); ophthalmologic exam (cataract, optic atrophy); renal ultrasound; renal function and electrolyte panel (hydronephrosis, nephrocalcinosis, tubulopathy); skeletal survey as indicated. Laboratory abnormalities may include hypocalcemia, hypokalemia, hyponatremia, and aminoaciduria.

**Differential diagnosis:** other autosomal-recessive syndromic microcephaly–cataract disorders (e.g., Warburg Micro syndrome [RAB3GAP1/2, RAB18, TBC1D20], Lowe syndrome [OCRL, for cataract + renal tubulopathy], peroxisomal disorders, congenital disorders of glycosylation). GEMIN4 genotyping distinguishes NEDMCR.

**Screening:** carrier and cascade screening of at-risk relatives in founder populations; prenatal and preimplantation genetic testing where the familial variant is known.

> "identifying GEMIN4 defects in patients presenting with neurodevelopmental delay and congenital cataract will help in early diagnosis, appropriate management and prevention plans that can be made for affected families" — [PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)

---

## 11. Outcome / Prognosis

Prognosis is **poor** for neurodevelopmental outcome. Affected individuals have severe global developmental delay, often non-verbal (absent speech) and non-ambulatory (inability to walk, spastic quadriplegia at the severe end), with epilepsy and microcephaly. Morbidity is high: recurrent respiratory infections (aspiration-related), feeding difficulties/dysphagia requiring nutritional support, renal complications, and skeletal problems. Formal survival/mortality statistics are not published given the small cohorts; recurrent respiratory infection and multisystem involvement are plausible contributors to early mortality at the severe end of the spectrum.

- **Prognostic factors:** genotype/severity (the p.His147Arg siblings showed severe microcephaly, spastic quadriplegia, epilepsy); presence/extent of brain atrophy and renal involvement.
- **Quality of life:** profoundly affected; lifelong dependence on caregivers.
- **Recovery potential:** none for the core neurodevelopmental deficit; cataract surgery can address the ocular component.

No prognostic molecular biomarkers beyond genotype are established.

---

## 12. Treatment

**There is no disease-specific or curative therapy.** A ClinicalTrials.gov search returned **0 trials** for GEMIN4/NEDMCR. Management is **multidisciplinary and supportive**, directed at individual manifestations:

| Manifestation | Supportive intervention | NCIT concept (suggested) |
|---|---|---|
| Seizures | Antiepileptic drugs | Anticonvulsant Agent (NCIT:C264) |
| Congenital cataract | Cataract extraction surgery | Cataract Surgery |
| Developmental delay / motor | Physical, occupational, speech therapy | Rehabilitation Therapy (NCIT:C15917) |
| GERD / feeding difficulty / dysphagia | Anti-reflux management, nutritional support / feeding support | Nutritional Support (NCIT:C15335) |
| Renal / electrolyte abnormalities | Electrolyte correction, nephrology management | Supportive Care (NCIT:C15317) |
| Recurrent respiratory infection | Aspiration precautions, infection treatment | Antibiotic Therapy |

- **Pharmacogenomics / gene therapy / cell therapy / RNA-based / targeted / immunotherapy:** none available or in development for NEDMCR.
- **Personalized medicine:** limited to genotype-based diagnosis and counseling.

---

## 13. Prevention

Because NEDMCR is a fully penetrant recessive Mendelian disorder, prevention is **genetic**:

- **Primary prevention:** genetic counseling for consanguineous couples and at-risk families; **carrier screening** for founder alleles in high-prevalence populations.
- **Secondary prevention:** cascade testing of relatives; prenatal diagnosis and **preimplantation genetic testing (PGT)** when the familial variant is known.
- **Tertiary prevention:** early supportive intervention to reduce complications (aspiration prophylaxis, seizure control, cataract surgery, renal monitoring).
- **Counseling:** 25% recurrence risk per pregnancy for carrier couples (autosomal recessive).
- **Immunization / public-health / environmental measures:** not applicable (no infectious or environmental cause).

> "appropriate management and prevention plans that can be made for affected families" — [PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)

---

## 14. Other Species / Natural Disease

**No naturally occurring GEMIN4 disease is catalogued in OMIA for any animal species.** GEMIN4 is deeply conserved (HomoloGene 69193):

| Species | Gene | NCBI Gene ID | NCBI Taxon |
|---|---|---|---|
| Mouse (*Mus musculus*) | Gemin4 | 276919 | 10090 |
| Rat (*Rattus norvegicus*) | Gemin4 | 497958 | 10116 |
| Zebrafish (*Danio rerio*) | gemin4 | 324754 | 7955 |
| *Xenopus* | gemin4 | 100379790 | 8364 |
| *Drosophila melanogaster* | Gemin4 ortholog | — | 7227 |

No zoonotic potential or cross-species transmission (genetic disorder). Evolutionary conservation of the SMN-complex/snRNP-biogenesis machinery underlies the utility of model organisms.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*):** constitutive **Gemin4-null mice die early in embryonic development**, demonstrating essentiality. "Gemin4 null mice die early in embryonic development, demonstrating that Gemin4 is an essential mammalian protein" ([PMID: 29371219](https://pubmed.ncbi.nlm.nih.gov/29371219/)). Heterozygous Gemin4 loss did not modify SMA type I mortality on a severe Smn−/−;SMN2+/+ background. **Limitation:** complete null is embryonic-lethal and therefore does not model the viable, hypomorphic human disease; a conditional/hypomorphic knock-in would be needed to recapitulate NEDMCR.
- **Drosophila melanogaster:** **neuron-specific knockdown of endogenous GEMIN4** produced developmental and motor defects, indicating that loss of GEMIN4 function is detrimental in vivo, paralleling patient phenotypes. "we knocked down endogenous Drosophila GEMIN4 in neurons to further investigate the mechanism of the functional defects in affected patients" ([PMID: 35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/)).
- **Cellular / in vitro:** neuronal cell lines were used historically to define the Gemin3/Gemin4/AGO2 miRNP complex and its polyribosome association ([PMID: 14970384](https://pubmed.ncbi.nlm.nih.gov/14970384/); [PMID: 12554860](https://pubmed.ncbi.nlm.nih.gov/12554860/)).
- **Resources:** MGI (mouse), ZFIN (zebrafish), FlyBase (Drosophila), RGD (rat).

---

## Evidence Base

| PMID | Title (abbrev.) | Role / what it supports | Evidence type |
|---|---|---|---|
| [27878435](https://pubmed.ncbi.nlm.nih.gov/27878435/) | *Novel phenotypes and loci … pediatric cataract* | Original link of biallelic GEMIN4 to cataract + developmental delay ± renal syndrome (cohort n=166/74 families) | Human clinical/genomics |
| [35861185](https://pubmed.ncbi.nlm.nih.gov/35861185/) | *Further delineation of GEMIN4-related NDD …* | Largest cohort (16 patients/11 families); founder effect (two alleles); AR inheritance; Drosophila model | Human clinical + model organism |
| [35052432](https://pubmed.ncbi.nlm.nih.gov/35052432/) | *A Novel … (His147Arg siblings)* | Third novel homozygous variant p.His147Arg; severe phenotype (microcephaly, spastic quadriplegia, epilepsy, cataracts) | Human clinical |
| [29371219](https://pubmed.ncbi.nlm.nih.gov/29371219/) | Gemin4 SMN-complex / mouse study | GEMIN4 core role in snRNP biogenesis; nuclear import; Gemin4-null mouse embryonic lethality | In vitro + mouse model |
| [11914277](https://pubmed.ncbi.nlm.nih.gov/11914277/) | *miRNPs: a novel class of RNPs …* | Gemin3/Gemin4/AGO2 (eIF2C2) miRNP complex containing microRNAs | In vitro |
| [14970384](https://pubmed.ncbi.nlm.nih.gov/14970384/) | *miRNP:mRNA association in polyribosomes …* | Gemin3/Gemin4/eIF2C2 + miRNAs cosediment with polyribosomes and bind target mRNAs (translational repression) | In vitro (neuronal) |
| [12554860](https://pubmed.ncbi.nlm.nih.gov/12554860/) | *Numerous microRNPs in neuronal cells …* | Neuronal miRNPs containing Gemin3/Gemin4; conserved miRNAs | In vitro (neuronal) |

The initial disease delineation (Alazami et al. 2015, *Cell Reports*, PMID 25558065) established NEDMCR in prescreened consanguineous families and underpins the OMIM:617913/HPO curation used throughout this report.

---

## Limitations and Knowledge Gaps

1. **Very small patient numbers.** Phenotype frequencies derive largely from a 3-patient HPO curation and a 16-patient series; frequencies and penetrance estimates are therefore imprecise.
2. **Narrow population base.** Nearly all cases are from consanguineous Saudi families with two founder alleles; the global phenotypic and allelic spectrum is unknown.
3. **Mechanism is largely inferred.** The causal chain from reduced GEMIN4 → snRNP/miRNP dysfunction → tissue-specific pathology is built from GEMIN4 biochemistry and model systems; no patient-tissue splicing/transcriptomic/proteomic data directly demonstrate the downstream steps, and tissue-specificity (why brain/lens/kidney) is unexplained.
4. **No faithful animal model.** The mouse null is embryonic-lethal (does not model viable hypomorphic disease); the Drosophila knockdown captures neuronal dysfunction but not the full multisystem syndrome.
5. **Variant interpretation.** Several ClinVar entries remain VUS; functional validation of specific missense alleles is limited to in silico/structural prediction.
6. **No epidemiologic, survival, or natural-history data** and **no therapeutics** exist.

---

## Proposed Follow-up Experiments / Actions

1. **Functional validation of founder missense alleles** — patient-derived iPSC or heterologous expression assays measuring snRNP assembly, GEMIN4 stability, and SMN-complex integration for p.Pro105Leu, p.Trp818Arg, and p.His147Arg.
2. **Hypomorphic/knock-in mouse model** (e.g., CRISPR knock-in of a founder allele or conditional/tissue-specific Gemin4 reduction) to recapitulate microcephaly, cataract, and renal phenotypes and probe tissue-specific vulnerability.
3. **Patient-tissue or organoid omics** — RNA-seq of patient-derived neural, lens, and kidney organoids to test for splicing alterations and snRNP-dependent transcript changes, and small-RNA-seq to assess miRNP-dependent dysregulation.
4. **Expand the cohort / registry** beyond founder populations via GeneMatcher to define the full allelic and phenotypic spectrum, penetrance, and natural history.
5. **Genotype–phenotype correlation** — systematically relate specific alleles to severity (e.g., neurologic vs renal burden) as more cases accrue.
6. **Carrier-frequency studies** in Saudi and neighboring populations to inform screening and counseling.


## Artifacts

- [OpenScientist final report](Neurodevelopmental_Disorder_With_Microcephaly_Cataracts_And_Renal_Abnormalities-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Neurodevelopmental_Disorder_With_Microcephaly_Cataracts_And_Renal_Abnormalities-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 13 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:35052432`: "Neurodevelopmental Impairment with Severe Microcephaly, Spastic Quadriplegia, Epilepsy, and Cataracts"
  - closest text in source: "She had severe microcephaly and spastic quadriplegia and was unable to control her head or sit independently"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 68 |
| Resolved | 65 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 47 |
| Terms named correctly | 38 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0060664` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with microcephaly, cataracts, and renal abnormalities**
- `DOID:0081263` (1 mention) - the report calls it "DOID"; DOID calls it **neurodevelopmental disorder with microcephaly, cataracts, and renal abnormalities**
- `NCIT:C15335` (1 mention) - the report calls it "Nutritional Support"; NCIT calls it **Technology Assessment**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0000340` (1 mention) - UBERON does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003593` (2 mentions) - the report calls it "Infantile onset", "Onset:** congenital / infantile"; HP calls it **Infantile onset**
- `HP:0002783` (1 mention) - the report calls it "Recurrent lower respiratory infections"; HP calls it **Recurrent lower respiratory tract infections**
- `GO:0035195` (1 mention) - the report calls it "miRNA-mediated gene silencing"; GO calls it **miRNA-mediated post-transcriptional gene silencing**, and lists "miRNA-mediated gene silencing" among its other names
- `UBERON:0001016` (1 mention) - the report calls it "Primary organs / systems — nervous system"; UBERON calls it **nervous system**
- `NCIT:C15917` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Arterial Embolization**
- `NCIT:C15317` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Second-Look Surgery**, and lists "Surgical Revision" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003593` - called "Infantile onset", "Onset:** congenital / infantile"
- `HP:0000007` - called "Autosomal recessive inheritance", "Inheritance:** autosomal recessive"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.