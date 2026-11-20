---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T04:10:38.048638'
end_time: '2026-11-13T04:43:11.889247'
duration_seconds: 1953.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SCN4A-Related Myopathy, Autosomal Recessive
  mondo_id: MONDO:0100121
  category: Mendelian
  causal_genes: SCN4A
  omim_id: not recorded
  synonyms: congenital myopathy with "corona" fibers, selective muscle atrophy, and
    craniosynostosis; congenital myopathy with severe fetal hypokinesia; congenital
    myopathy with severe foetal hypokinesia; myopathy with ptosis and mild dystrophic
    pattern
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 2ec5efb3-0854-4fff-9f1f-d4fdc66f781a
citation_count: 6
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.5.1
term_validation:
  total_terms: 28
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 18
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0100121
    reported_labels:
    - Mondo
    ontology_label: SCN4A-related myopathy, autosomal recessive
  labels_variant: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SCN4A-Related_Myopathy_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SCN4A-Related_Myopathy_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SCN4A-Related Myopathy, Autosomal Recessive
- **MONDO ID:** MONDO:0100121 (if available)
- **Causal gene(s):** SCN4A
- **OMIM:** not recorded
- **Synonyms:** congenital myopathy with "corona" fibers, selective muscle atrophy, and craniosynostosis; congenital myopathy with severe fetal hypokinesia; congenital myopathy with severe foetal hypokinesia; myopathy with ptosis and mild dystrophic pattern
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SCN4A-Related Myopathy, Autosomal Recessive** covering all of the
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

# SCN4A-Related Myopathy, Autosomal Recessive (MONDO:0100121): A Comprehensive Disease Characterization

## Summary

**SCN4A-Related Autosomal Recessive Myopathy (MONDO:0100121)** is an ultra-rare congenital neuromuscular disorder caused by **biallelic loss-of-function (LOF) variants in *SCN4A***, the gene encoding the **skeletal-muscle voltage-gated sodium channel NaV1.4** (α-subunit, HGNC:10591; UniProt P35499; chromosome 17q23.3; gene MIM 603967). This is mechanistically the **mirror image** of the far more familiar dominant *SCN4A* channelopathies (hyperkalemic/hypokalemic periodic paralysis, paramyotonia congenita, sodium-channel myotonia), which arise from **gain-of-function or altered-gating** mutations. In the recessive disease, reduced or absent sodium current fails to depolarize the sarcolemma sufficiently to generate and propagate muscle action potentials, impairing excitation–contraction coupling and producing weakness rather than hyperexcitability.

The defining clinical feature is a **genotype–severity gradient governed by residual NaV1.4 current**. Complete biallelic loss (two null alleles) causes **lethal fetal akinesia/hypokinesia** — the most severe end, often resulting in intrauterine or neonatal death. A null allele combined with a hypomorphic (partial-function) allele, or two hypomorphic alleles, produces a **survivable congenital myopathy** with neonatal hypotonia, facial/neck/bulbar weakness, respiratory and feeding difficulty, and spinal deformity, which characteristically **improves over the first decade of life**. Specific partial-LOF missense variants (notably at residue **R1460**, and the historical **V1442E**) produce a **fatigable "myasthenic" congenital myopathy** that overlaps with congenital myasthenic syndrome (CMS16, OMIM 614198). The landmark cohort (Zaharieva et al., *Brain* 2016) found 7 of 11 affected individuals died in utero or shortly after birth, with the 4 survivors all improving clinically in childhood.

Converging lines of evidence confirm the recessive, dose-dependent logic: **gnomAD constraint** shows *SCN4A* tolerates heterozygous LOF (pLI ≈ 0, LOEUF 0.61), consistent with asymptomatic carriers; and a **NaV1.4-null mouse** recapitulates the human dose relationship (heterozygous nulls have latent myasthenia without periodic paralysis; homozygous nulls die by postnatal day 2). Diagnosis is **molecular** — biallelic *SCN4A* variants detected by whole-exome/whole-genome sequencing or neuromuscular gene panels — because muscle biopsy shows only nonspecific myopathic changes and EMG shows a myopathic process without myotonia. **No disease-modifying therapy exists;** management is supportive (neonatal respiratory and feeding support, scoliosis management, physiotherapy), with inconsistent empirical benefit from salbutamol, acetazolamide, and acetylcholinesterase inhibitors tried by analogy to CMS.

---

## Section 1 — Disease Information

**Overview.** SCN4A-Related Autosomal Recessive Myopathy is a Mendelian congenital neuromuscular disease caused by biallelic LOF variants in *SCN4A* (NaV1.4). It spans a phenotypic continuum from the most severe **congenital myopathy with severe fetal hypokinesia / fetal akinesia** (frequently lethal) through a **survivable congenital myopathy** (neonatal hypotonia, facial and bulbar weakness, respiratory compromise) to a **fatigable myasthenic congenital myopathy**. This entity is biologically and clinically distinct from the common autosomal **dominant** *SCN4A* channelopathies driven by gain-of-function/altered-gating mechanisms.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Mondo | MONDO:0100121 |
| Causal gene | *SCN4A* (HGNC:10591) |
| Related OMIM phenotype (myasthenic/CMS16) | 614198 (congenital myasthenic syndrome 16) |
| *SCN4A* gene OMIM | 603967 |
| Ensembl | ENSG00000007314 |
| NCBI Gene | 6329 |
| UniProt | P35499 (NaV1.4) |
| Cytogenetic locus | 17q23.3 |

> Note: OMIM was recorded as "not recorded" in the disease template. The most closely linked OMIM phenotype for the myasthenic/recessive end of the spectrum is CMS16 (614198). The broader recessive congenital myopathy/fetal hypokinesia spectrum is captured under MONDO:0100121.

**Synonyms / alternative names.**
- Congenital myopathy with "corona" fibers, selective muscle atrophy, and craniosynostosis
- Congenital myopathy with severe fetal (foetal) hypokinesia
- Myopathy with ptosis and mild dystrophic pattern
- SCN4A-related congenital myopathy; recessive NaV1.4 loss-of-function myopathy

**Information source.** Derived from **aggregated disease-level resources** (OMIM, Orphanet, Mondo) and **individual-patient primary literature** — principally small case series and single case reports, reflecting the ultra-rarity of the condition (dozens of published patients worldwide).

---

## Section 2 — Etiology

**Primary cause — genetic.** The disease is caused exclusively by **biallelic (homozygous or compound heterozygous) LOF variants in *SCN4A***. Zaharieva et al. identified such variants in 11 individuals from 6 unrelated kindreds; each affected case carried **at least one full loss-of-function (null) allele**, and 5 of 6 families had a second LOF allele in trans.

> *"we identified homozygous or compound heterozygous SCN4A mutations in a cohort of 11 individuals from six unrelated kindreds with congenital myopathy"* — [PMID: 26700687](https://pubmed.ncbi.nlm.nih.gov/26700687/)

**Genetic risk factors.** The causal variants are the risk factor. Disease requires **two defective alleles**; a single LOF allele is insufficient (carriers are typically asymptomatic). **Consanguinity** increases risk by raising homozygosity. No modifier loci or susceptibility SNPs have been established; the principal "modifier" is the **identity of the second allele** (null vs hypomorph), which sets residual channel function and therefore severity.

**Environmental risk factors.** None established. This is a monogenic disorder; onset is congenital/prenatal, so postnatal environmental exposures are not causal. **Sex** is not a risk factor (no sex bias; the gene is autosomal). **Family history / consanguinity** are the only relevant demographic factors.

**Protective factors.** The principal "protective" factor is **residual NaV1.4 function** — a hypomorphic allele that retains partial current shifts the phenotype toward survivability and milder disease relative to a complete null. No protective modifier alleles or dietary/lifestyle protective factors are documented. At the population level, gnomAD shows heterozygous LOF is tolerated (pLI ≈ 0), so **a single functional allele is protective** against disease.

**Gene–environment interactions.** None established. Because manifestations are prenatal/congenital and fully penetrant with the biallelic genotype, there is no meaningful GxE axis documented.

---

## Section 3 — Phenotypes

The phenotype is a continuum stratified by residual channel function. Key manifestations, with suggested HPO terms:

| Phenotype | Type | Onset | Severity | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Fetal akinesia / severe hypokinesia | Clinical sign (prenatal) | Prenatal | Severe (often lethal) | Severe end (~7/11 in Zaharieva died in utero/neonatally) | HP:0001558 (Decreased fetal movement) |
| Congenital hypotonia | Clinical sign | Neonatal | Moderate–severe | Survivors | HP:0001319 (Neonatal hypotonia) |
| Facial / neck muscle weakness | Clinical sign | Neonatal | Moderate | Survivors (characteristic) | HP:0030319 (Facial-muscle weakness); HP:0000467 (Neck-muscle weakness) |
| Bulbar weakness / swallowing difficulty | Clinical sign | Neonatal | Moderate–severe | Survivors | HP:0002015 (Dysphagia) |
| Respiratory insufficiency | Clinical sign | Neonatal | Severe | Common; drives mortality | HP:0002093 (Respiratory insufficiency) |
| Ptosis | Physical manifestation | Neonatal/childhood | Mild–moderate | Subset ("myopathy with ptosis") | HP:0000508 (Ptosis) |
| Fatigable weakness (myasthenic) | Symptom | Neonatal/childhood | Variable | Myasthenic subtype (R1460, V1442E) | HP:0003473 (Fatigable weakness) |
| Spinal deformity / scoliosis | Physical manifestation | Childhood | Moderate | Survivors | HP:0002650 (Scoliosis) |
| Recurrent respiratory/bulbar paralytic crises | Clinical sign | Birth onward | Severe episodic | Myasthenic subtype (Tsujino) | HP:0002878 (Respiratory failure) |
| Arthrogryposis / contractures (fetal akinesia sequence) | Physical manifestation | Congenital | Variable | Severe end | HP:0002804 (Arthrogryposis multiplex congenita) |

**Progression.** Severe fetal forms are lethal perinatally. **Survivors characteristically improve over the first decade of life** — an unusual and clinically important feature. Muscle biopsy in survivors shows nonspecific myopathic changes and EMG a myopathic process without myotonia (Zaharieva 2016).

> *"we identified homozygous or compound heterozygous SCN4A mutations in a cohort of 11 individuals from six unrelated kindreds with congenital myopathy"* — [PMID: 26700687](https://pubmed.ncbi.nlm.nih.gov/26700687/)

**Myasthenic subtype features.** Fatigable generalized weakness with decremental CMAP on repetitive nerve stimulation and recurrent attacks of respiratory/bulbar paralysis since birth (Tsujino et al.).

> *"endplate potentials depolarizing the resting potential to -40 mV failed to excite action potentials"* — [PMID: 12766226](https://pubmed.ncbi.nlm.nih.gov/12766226/)

**Quality-of-life impact.** Severe in the neonatal period (ventilator/feeding dependence, risk of death). In survivors, improvement over the first decade with residual facial/axial weakness, scoliosis, and fatigability; impact ranges from moderate disability to relatively preserved function depending on residual current.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *SCN4A* (NaV1.4), HGNC:10591, OMIM 603967, Ensembl ENSG00000007314, NCBI Gene 6329, chromosome 17q23.3. Encodes the pore-forming α-subunit of the adult skeletal-muscle voltage-gated sodium channel responsible for the rapid upstroke of the sarcolemmal action potential.

**Pathogenic variants.** Disease-causing alleles are **biallelic LOF**. Reported variant classes and examples:

| Variant | Type | Functional consequence | Phenotype context | Source |
|---|---|---|---|---|
| Nonsense/null alleles (e.g., p.R1059X) | LOF (null) | Complete loss of function | Severe/lethal when biallelic; combines with hypomorph | Elia 2019 [PMID: 30824560] |
| p.R1460W (homozygous) | Missense, partial LOF | Reduced amplitude, hyperpolarized inactivation shift | Myasthenic congenital myopathy | [PMID: 30824560] |
| p.R1460Q (compound het with p.R1059X) | Missense, mixed LOF+GOF | Loss dominates; GOF features → myotonia in carriers | Myasthenic myopathy | [PMID: 30824560] |
| p.V1442E (with benign p.S246L in trans) | Missense | Enhanced fast inactivation near rest; enhanced use-dependent inactivation | Myasthenic syndrome (CMS16) | Tsujino 2003 [PMID: 12766226] |
| p.Arg1454Trp (LOF) + p.Asn1205Lys | Compound-het missense | LOF | Severe congenital myopathy | Berghold 2022 [PMID: 36090556] |

**Variant classification.** Interpretation follows ACMG/AMP, but with a **mechanism-informed, phenotype-first workflow** because *SCN4A* produces directionally opposite mechanisms (dominant GOF vs recessive LOF). D'Ambrosio et al. emphasize integrating inheritance, channel topology, population frequency, segregation, and **mechanism-matched functional assays**.

> *"severe biallelic loss of function causing congenital myopathy and fetal hypokinesia"* — [PMID: 42793010](https://pubmed.ncbi.nlm.nih.gov/42793010/)

**Allele frequency / population constraint.** gnomAD (GRCh38): **pLI = 3.99e-10 (≈0; NOT LOF-intolerant)**; LOF observed/expected o/e = 0.512 (90% CI 0.429–0.615; **LOEUF 0.61**); observed LOF = 83 vs expected 162; missense Z = 2.29 (mis o/e = 0.89). This pattern — tolerance of heterozygous LOF plus modest missense constraint — is exactly what is expected for a **recessive** disease gene where one working allele suffices.

**Somatic vs germline.** Entirely **germline**; no somatic involvement.

**Functional consequence.** **Loss of function** (reduced channel availability / current amplitude). This contrasts with dominant *SCN4A* disease (gain-of-function, altered gating, gating-pore leak currents). Some myasthenic-subtype missense variants (R1460) show **mixed** LOF+GOF, with LOF driving the recessive myasthenic phenotype.

> *"Recessive inheritance, with experimentally established loss-of-function, is a consistent feature of sodium channel based myasthenia, whereas the mixed gain of function for p.R1460 may also cause susceptibility to myotonia"* — [PMID: 30824560](https://pubmed.ncbi.nlm.nih.gov/30824560/)

**Modifier genes.** None established; the trans allele is the primary determinant of residual function. **Epigenetic changes** and **chromosomal abnormalities**: none implicated — this is a point-mutation/small-variant disease.

---

## Section 5 — Environmental Information

**Environmental factors:** None causal. **Lifestyle factors:** None causal (congenital/prenatal onset). **Infectious agents:** Not applicable — this is a monogenic channelopathy with no infectious trigger. The only non-genetic contributor to recurrence risk is **consanguinity** (a demographic, not environmental, factor).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic LOF variants in *SCN4A*** (null/null, null/hypomorph, or hypomorph/hypomorph) **lead to** reduced or absent functional NaV1.4 α-subunit at the sarcolemma. *(Demonstrated: HEK293/Xenopus functional assays.)*
2. Reduced functional channel **results in** decreased macroscopic sodium current density (INa) in the muscle fiber membrane (sarcolemma, including t-tubules). *(Demonstrated in vitro and in NaV1.4-null mouse: INa ~50% of wild-type in heterozygotes, no compensation by fetal NaV1.5.)*
3. Decreased INa **leads to** failure to reach threshold / failure to generate and propagate muscle action potentials, especially during sustained high-frequency firing. *(Demonstrated: endplate potentials failed to excite action potentials in Tsujino 2003.)*
4. Action-potential failure **results in** impaired excitation–contraction coupling (insufficient t-tubular depolarization to trigger Cav1.1/RyR1 Ca²⁺ release). *(Inferred from channel physiology.)*
5. Impaired E–C coupling **leads to** muscle weakness. The clinical form then **branches by residual current:**
   - **5a. Complete biallelic null (≈0 residual current) → leads to** profound prenatal muscle inactivity → **fetal akinesia/hypokinesia sequence** (contractures, pulmonary hypoplasia) → **intrauterine or neonatal death.**
   - **5b. Null + hypomorph / biallelic hypomorph (low residual current) → leads to** survivable **congenital myopathy** (neonatal hypotonia, facial/bulbar/respiratory weakness, scoliosis) that **improves over the first decade** (inferred: postnatal developmental increase in channel expression/compensation).
   - **5c. Residue-specific partial LOF (e.g., R1460, V1442E; near-normal resting current but failure under load) → leads to** a **fatigable myasthenic congenital myopathy** with decremental CMAP and paralytic crises.

### Detail by category

- **Biochemical abnormality / ion-channel defect (upstream, primary):** Reduced NaV1.4-mediated INa — a classic **sodium-channelopathy LOF** lesion. CHEBI:29101 (sodium ion).
- **Protein dysfunction:** Loss of function via reduced channel availability, hyperpolarized shift of fast inactivation (V1442E, R1460), enhanced use-dependent inactivation. For null alleles, absent protein. GO suggestions: **GO:0005248** (voltage-gated sodium channel activity), **GO:0086010** (membrane depolarization during action potential), **GO:0001508** (action potential).
- **Cellular processes (downstream):** Failure of **skeletal muscle contraction** (GO:0003009) and **membrane depolarization** (GO:0051899); impaired E–C coupling. No apoptosis/inflammation signature is central; biopsy is non-inflammatory.
- **Tissue damage mechanism:** Primarily **functional** (electrical failure) rather than degenerative. Biopsy shows nonspecific myopathic changes (fiber-size variability, fibrofatty replacement of varying severity) — not a specific structural myopathy and not prominent necrosis.
- **Metabolic / immune involvement:** Not implicated. No autoimmunity (distinguishing it from acquired myasthenia gravis), no energy-metabolism defect (though one patient was initially misdiagnosed as mitochondrial myopathy).
- **Molecular profiling:** No disease-specific transcriptomic/proteomic/metabolomic signature established; mechanism is defined by electrophysiology.

**Cell types (CL):** skeletal muscle fiber / myofiber (**CL:0000188**, skeletal muscle cell). **Upstream vs downstream:** the ion-channel defect is upstream; E–C-coupling failure and weakness are downstream.

---

## Section 7 — Anatomical Structures Affected

- **Organ level (primary):** Skeletal muscle (**UBERON:0001134**, skeletal muscle tissue; UBERON:0001630, muscle organ). Facial, neck/axial, bulbar, respiratory (diaphragm/intercostal), and limb muscles.
- **Secondary organ / system involvement:** Respiratory system (respiratory insufficiency/failure — the main driver of mortality; UBERON:0001004); skeletal system (scoliosis/spinal deformity, contractures; UBERON:0002090 axial skeleton). Fetal akinesia sequence secondarily affects lungs (hypoplasia) and joints.
- **Body systems:** **Musculoskeletal** (primary), **respiratory** (secondary). The **neuromuscular junction** is implicated functionally in the myasthenic subtype, but the defect is **post-synaptic / sarcolemmal** (muscle membrane), with normal ACh release and normal endplate structure in Tsujino's case.
- **Tissue/cell level:** Striated muscle tissue; **skeletal muscle fibers (CL:0000188)**. Epithelial/connective/nervous tissues are not primarily affected.
- **Subcellular level:** **Sarcolemma / plasma membrane** and **t-tubule system** where NaV1.4 resides. GO cellular component: **GO:0005886** (plasma membrane), **GO:0030315** (T-tubule).
- **Localization / lateralization:** **Bilateral and generalized** (symmetric), with facial, bulbar, axial, and respiratory predominance.

---

## Section 8 — Temporal Development

- **Onset:** **Congenital / prenatal.** Severe forms present as reduced fetal movement (fetal akinesia/hypokinesia); survivable forms present with neonatal hypotonia. Myasthenic subtype: symptoms "since birth."
- **Onset pattern:** Insidious prenatal onset; myasthenic crises can be acute/episodic.
- **Progression / course:**
  - *Severe (biallelic null):* lethal in utero or in the neonatal period.
  - *Intermediate (survivable congenital myopathy):* **non-progressive to improving** — survivors improve over the **first decade of life**.
  - *Myasthenic subtype:* **fluctuating/episodic** fatigable weakness with paralytic crises.
- **Disease duration:** Chronic lifelong in survivors; perinatally lethal at the severe end.
- **Remission pattern:** No true remission, but clinical **improvement** in childhood survivors (likely treatment-independent, developmental).
- **Critical periods:** Prenatal/perinatal period is the window of maximal vulnerability (akinesia sequence, respiratory failure). The neonatal period is the key intervention window (respiratory and feeding support determine survival).

---

## Section 9 — Inheritance and Population

- **Inheritance:** **Autosomal recessive.** Requires two defective *SCN4A* alleles. This is the key contrast with dominant *SCN4A* channelopathies.
- **Penetrance:** Essentially **complete** for the biallelic genotype.
- **Expressivity:** **Highly variable**, determined by residual NaV1.4 current (null/null vs null/hypomorph vs hypomorph/hypomorph vs residue-specific partial LOF).
- **Carriers:** Obligate heterozygous carriers are **typically asymptomatic** (supported by gnomAD pLI ≈ 0). The NaV1.4-null mouse heterozygote shows only **latent (subclinical) myasthenia**.
- **Genetic anticipation:** Not applicable (no repeat expansion). **Germline mosaicism:** not specifically documented. **Founder effects:** none identified; variants are private across kindreds.
- **Consanguinity:** Contributory (several homozygous cases from consanguineous or isolated kindreds).
- **Epidemiology:** **Ultra-rare** — only dozens of published patients worldwide; formal prevalence/incidence not estimated.
- **Population demographics:** **Panethnic**, reported across multiple ethnicities with **no founder population**, **no sex bias** (autosomal), and onset at birth/prenatally.

> *"we identified homozygous or compound heterozygous SCN4A mutations in a cohort of 11 individuals from six unrelated kindreds with congenital myopathy"* — [PMID: 26700687](https://pubmed.ncbi.nlm.nih.gov/26700687/)

---

## Section 10 — Diagnostics

**Diagnosis is molecular.** Because clinical and histological features are nonspecific, definitive diagnosis requires detection of **biallelic *SCN4A* variants**.

- **Genetic testing (primary modality):** **Whole-exome sequencing (WES)** was the discovery method (Zaharieva 2016). **WGS**, **neuromuscular/congenital-myopathy/CMS gene panels** including *SCN4A*, and **single-gene testing** (when phenotype is strongly suggestive) are all applicable. Segregation analysis confirms biallelic/trans configuration. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not relevant** (small-variant disease).

> *"severe biallelic loss of function causing congenital myopathy and fetal hypokinesia"* — [PMID: 42793010](https://pubmed.ncbi.nlm.nih.gov/42793010/)

- **Muscle biopsy (supportive, nonspecific):** Myopathic features — increased fiber-size variability, fibrofatty tissue of varying severity — **without** specific structural abnormalities (no entity-specific cores/rods). Useful to exclude other congenital myopathies.
- **Electrophysiology:** EMG shows a **myopathic process without myotonia**. In the **myasthenic subtype**, repetitive nerve stimulation shows a **decremental CMAP**; microelectrode studies show endplate potentials that fail to excite action potentials despite normal ACh release and endplate morphology — localizing the defect to the **sarcolemma (post-synaptic muscle membrane)**.
- **Laboratory:** Creatine kinase usually normal or mildly elevated (nonspecific). No specific biomarker exists.
- **Functional assays (research/variant interpretation):** Voltage-clamp in HEK293/Xenopus oocytes to confirm LOF and classify variants per a mechanism-informed ACMG/AMP workflow.
- **Differential diagnosis:** Other congenital myopathies (*RYR1*, *ACTA1*, *NEB*, *TPM2/3*, *MTM1*), congenital myasthenic syndromes (CHRNE, RAPSN, DOK7, CHAT, AGRN, GFPT1, PLEC), SMA, congenital myotonic dystrophy, mitochondrial myopathy (one SCN4A patient was initially misdiagnosed as mitochondrial myopathy), and fetal akinesia deformation sequence of other causes.
- **Screening:** Not part of routine newborn screening. **Carrier and cascade screening** of relatives is appropriate once a familial variant is known; **prenatal/preimplantation testing** is available for at-risk couples.

---

## Section 11 — Outcome / Prognosis

- **Survival / mortality:** **Bimodal and genotype-dependent.** Complete biallelic null → high perinatal mortality (**7 of 11 individuals in Zaharieva 2016 died in utero or shortly after birth**). Survivors (null+hypomorph / biallelic hypomorph) have a chronic but **improving** course.
- **Life expectancy:** Severe end — perinatally lethal. Survivable end — potentially near-normal with supportive care, though respiratory/bulbar weakness and scoliosis carry ongoing risk.
- **Morbidity / function:** Neonatal ventilator and feeding dependence; residual facial/axial weakness, fatigability, and scoliosis in survivors. Characteristic **improvement over the first decade** is a favorable prognostic feature.
- **Complications:** Respiratory failure (leading cause of death), aspiration from bulbar weakness, scoliosis/restrictive lung disease, contractures.
- **Prognostic factors:** The strongest predictor is **residual NaV1.4 current / genotype** (null/null worst; presence of a hypomorphic allele predicts survivability and improvement). Severity of neonatal respiratory compromise is the key clinical prognostic factor.

---

## Section 12 — Treatment

**No disease-modifying therapy exists.** Management is **supportive and symptomatic**.

- **Supportive / rehabilitative (mainstay):** Neonatal **respiratory support** (non-invasive or invasive ventilation), **feeding/swallowing support** (NG/gastrostomy), **scoliosis/spinal deformity management**, and **physiotherapy/occupational therapy**. NCIT: Supportive Care (NCIT:C15329), Physical Therapy (NCIT:C15327), Mechanical Ventilation.
- **Empirical pharmacotherapy (inconsistent benefit):** By analogy to *SCN4A* congenital myasthenic syndrome, agents tried include **acetylcholinesterase inhibitors (pyridostigmine)**, **β2-agonists (salbutamol/albuterol)**, and **acetazolamide** — with **variable and often limited response**. In a genetically confirmed patient (compound heterozygous p.Arg1454Trp LOF + p.Asn1205Lys), there was limited benefit from salbutamol and acetazolamide, and pyridostigmine caused side effects at a minor dose.

> *"We present a now 18-year-old female patient with a severe congenital myopathy phenotype, originally diagnosed as mitochondrial myopathy, however later revealed to constitute a..."* — [PMID: 36090556](https://pubmed.ncbi.nlm.nih.gov/36090556/)

- **Pharmacogenomics / personalized medicine:** Treatment is **genotype/mechanism-guided in principle** — the myasthenic subtype (partial-LOF, NMJ-like safety-margin failure) is the most plausible to respond to cholinergic augmentation, whereas pure structural LOF myopathy is less likely to respond. This mirrors the general CMS principle that drugs beneficial in one subtype can be harmful in another.
- **Advanced therapeutics (gene/cell/RNA therapy), targeted therapy, immunotherapy:** None established or approved for this indication. No gene-replacement or ASO program is reported.
- **Surgical / interventional:** Scoliosis may require orthopedic surgical management.
- **Experimental:** No disease-specific registered clinical trials (no NCT identifiers specific to recessive SCN4A myopathy identified).

---

## Section 13 — Prevention

- **Primary prevention:** Not possible for the congenital disease itself (prenatal onset). **Genetic counseling** for at-risk/consanguineous couples is central. For couples with a known familial biallelic risk, **preimplantation genetic testing (PGT)** and **prenatal diagnosis** allow reproductive risk management.
- **Secondary prevention:** **Carrier screening** and **cascade testing** of relatives once the familial variant is identified; early molecular diagnosis in a hypotonic neonate enables prompt respiratory/feeding support.
- **Tertiary prevention:** Proactive respiratory monitoring/ventilatory support, aspiration precautions, scoliosis surveillance and management, and physiotherapy to prevent contractures.
- **Immunization / public-health / environmental interventions:** Not applicable (non-infectious, monogenic).
- **Counseling:** Autosomal recessive counseling — 25% recurrence risk for carrier × carrier couples; emphasis on consanguinity-related risk.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *SCN4A* (NCBI Gene 6329; NCBI Taxon 9606). Mouse ortholog **Scn4a** (NCBI Gene 110599; NCBI Taxon 10090) is well characterized. Orthologs are highly conserved across vertebrates, reflecting the essential role of NaV1.4 in skeletal-muscle excitability.
- **Natural disease in other species:** Dominant *SCN4A*-type channelopathies occur naturally in animals (e.g., equine hyperkalemic periodic paralysis — a gain-of-function phenotype). A naturally occurring **recessive LOF NaV1.4 myopathy** analogous to the human recessive disease is **not well documented** in companion animals/wildlife.
- **Comparative biology / evolutionary conservation:** The LOF mechanism is conserved — the mouse null phenotype (below) demonstrates that complete loss is neonatally lethal across mammals, confirming conserved essentiality.
- **Transmission:** Not applicable (non-infectious, non-zoonotic).

---

## Section 15 — Model Organisms

- **Primary model — NaV1.4-null mouse (Wu et al., 2016):** Generated by deleting exon 12 of *Scn4a*. This genetic knockout **recapitulates the recessive, dose-dependent human genotype–phenotype relationship:**
  - **Heterozygous nulls:** latent (subclinical) myasthenia with a right-shift of the force–stimulus relation; sodium current density ~50% of wild-type **without compensation by fetal NaV1.5**; **no periodic paralysis.**
  - **Homozygous nulls:** **did not survive beyond the second postnatal day** — modeling human lethal fetal hypokinesia/complete biallelic null.

> *"Mice null for NaV1.4 did not survive beyond the second postnatal day"* — [PMID: 27048647](https://pubmed.ncbi.nlm.nih.gov/27048647/)

> *"Heterozygous null mice have latent myasthenia and a right shift of the force-stimulus relation, without evidence of periodic paralysis"* — [PMID: 27048647](https://pubmed.ncbi.nlm.nih.gov/27048647/)

- **In vitro / heterologous expression models:** **HEK293 cells** and **Xenopus oocytes** expressing mutant Nav1.4 channels, used for voltage-clamp characterization of LOF (reduced amplitude, hyperpolarized inactivation shifts, use-dependent inactivation) — the workhorse for variant interpretation (Tsujino 2003; Elia 2019).
- **Model type / genetic models:** Mammalian knockout (constitutive null); heterologous cell expression systems. Conditional/humanized/knock-in models specific to this disease are not prominently reported.
- **Phenotype recapitulation:** **Strong** — the mouse null reproduces both the carrier (latent myasthenia) and the lethal-homozygote ends of the human spectrum, directly validating the dose-dependent mechanism.
- **Limitations:** The homozygous null's early lethality limits study of the survivable/improving phenotype; hypomorphic knock-in models (null+hypomorph) that would mirror survivable human disease are not established. In vitro systems capture channel biophysics but not tissue-level E–C coupling or the developmental improvement seen in human survivors.
- **Resources:** MGI (mouse *Scn4a*), standard neuromuscular electrophysiology platforms.

---

## Mechanistic Model / Interpretation

The unifying principle is a **continuous dose–response between residual NaV1.4 sodium current and clinical severity.** A single integrated model accounts for the entire phenotypic spectrum:

```
  BIALLELIC SCN4A LOF VARIANTS
          │
          ▼
  ↓ functional NaV1.4 protein at sarcolemma / t-tubule
          │
          ▼
  ↓ macroscopic Na+ current (INa)  ──(mouse: ~50% in het; ~0 in homozygous null)
          │
          ▼
  Failure to generate/propagate muscle action potentials
  (worst during sustained high-frequency firing)
          │
          ▼
  Impaired excitation–contraction coupling → MUSCLE WEAKNESS
          │
   ┌──────┼───────────────────────────────────────────┐
   ▼                     ▼                              ▼
 null/null          null + hypomorph /           residue-specific partial LOF
 (≈0 current)       biallelic hypomorph          (R1460, V1442E)
   │                     │                              │
   ▼                     ▼                              ▼
 FETAL AKINESIA     SURVIVABLE CONGENITAL          FATIGABLE "MYASTHENIC"
 /HYPOKINESIA       MYOPATHY (hypotonia,           CONGENITAL MYOPATHY
 → in utero/        facial/bulbar/respiratory      (decremental CMAP,
 neonatal death     weakness, scoliosis;           paralytic crises)
                    IMPROVES over 1st decade)
```

| Residual current | Genotype | Phenotype | Outcome |
|---|---|---|---|
| ≈ 0% | null / null | Fetal akinesia / severe hypokinesia | Perinatally lethal (7/11 in Zaharieva) |
| Low | null / hypomorph or hypomorph / hypomorph | Congenital myopathy, hypotonia, bulbar/respiratory weakness | Survivable; improves in first decade |
| Partial (load-dependent failure) | R1460W/W; R1460Q + null; V1442E | Fatigable myasthenic myopathy, crises | Chronic; fatigable |
| ~50% (one null allele) | heterozygous carrier | Asymptomatic / latent myasthenia | No disease |

This model is **mechanistically opposite** to dominant *SCN4A* disease, where gain-of-function or gating-pore leak currents cause hyperexcitability (myotonia) or depolarization-induced inexcitability (periodic paralysis). The recessive disease is a **pure loss-of-function hypoexcitability** disorder. Three independent evidence streams converge on this model: human genotype–phenotype series, in vitro electrophysiology confirming LOF, and the NaV1.4-null mouse reproducing both the carrier and lethal-null extremes. gnomAD constraint (pLI ≈ 0) independently confirms that heterozygous LOF is tolerated — the population-genetic signature of a recessive gene.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [26700687](https://pubmed.ncbi.nlm.nih.gov/26700687/) | LOF *SCN4A* cause severe fetal hypokinesia or classical congenital myopathy (Zaharieva, *Brain* 2016) | Human cohort + in vitro | **Landmark**: establishes biallelic LOF → recessive congenital myopathy/fetal hypokinesia; 11 individuals/6 kindreds; 7/11 perinatal death; survivors improve; nonspecific biopsy |
| [30824560](https://pubmed.ncbi.nlm.nih.gov/30824560/) | Myasthenic congenital myopathy from recessive R1460 mutations (Elia, *Neurology* 2019) | Human + voltage-clamp | Defines fatigable myasthenic subtype; recessive LOF consistent across sodium-channel myasthenia |
| [12766226](https://pubmed.ncbi.nlm.nih.gov/12766226/) | Myasthenic syndrome V1442E (Tsujino, *PNAS* 2003) | Human + in vitro | First recessive *SCN4A* disorder (CMS16); sarcolemmal action-potential failure; normal ACh release/endplate |
| [27048647](https://pubmed.ncbi.nlm.nih.gov/27048647/) | NaV1.4-null mice have latent myasthenia (Wu, 2016) | Mouse model | Validates dose-dependence: het = latent myasthenia; homozygous null = neonatal lethal |
| [42793010](https://pubmed.ncbi.nlm.nih.gov/42793010/) | *SCN4A* channelopathies: mechanisms to variant interpretation (D'Ambrosio review) | Review | Frames recessive biallelic LOF vs dominant mechanisms; mechanism-informed ACMG/AMP workflow |
| [36090556](https://pubmed.ncbi.nlm.nih.gov/36090556/) | Novel *SCN4A* case report (Berghold, 2022) | Human case | Genetically confirmed patient; documents limited/inconsistent pharmacotherapy response; misdiagnosis as mitochondrial myopathy |
| [36835142](https://pubmed.ncbi.nlm.nih.gov/36835142/), [29478601](https://pubmed.ncbi.nlm.nih.gov/29478601/), [22353287](https://pubmed.ncbi.nlm.nih.gov/22353287/), [15367858](https://pubmed.ncbi.nlm.nih.gov/15367858/) | CMS reviews | Reviews | Context: *SCN4A* as a recognized CMS gene; supportive pharmacology by analogy |
| gnomAD (ENSG00000007314) | Constraint metrics | Population genetics | pLI ≈ 0, LOEUF 0.61 → heterozygous LOF tolerated (recessive logic) |

**Consistency:** All four primary human/model studies and the population-constraint data point in the same direction — **recessive loss of function with severity set by residual current.** No contradictory evidence was found; the dominant *SCN4A* literature is complementary, not contradictory, because it describes a different (gain-of-function) mechanism.

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity and small samples.** Conclusions rest on a handful of case series/reports (dozens of patients total). No formal prevalence/incidence, natural-history cohort, or registry exists.
2. **No validated biomarker or quantitative severity scale** linking residual INa to clinical outcome in humans; the dose–response model is strongly supported but not quantitatively calibrated in patients.
3. **No survivable-phenotype animal model.** The homozygous null mouse dies neonatally; a hypomorphic/knock-in mouse that would model the survivable, improving human phenotype is lacking, limiting preclinical therapeutic testing.
4. **Mechanism of childhood improvement is unexplained** (hypothesized developmental increase in channel expression or compensatory remodeling — not demonstrated).
5. **Therapeutics are empirical.** No controlled trials; responses to salbutamol/acetazolamide/pyridostigmine are anecdotal and inconsistent. No genotype-stratified treatment evidence.
6. **Variant interpretation is challenging** because *SCN4A* produces opposite mechanisms; functional assays are needed but not universally available.
7. **OMIM entity boundaries** for the recessive congenital-myopathy/fetal-hypokinesia end vs CMS16 (614198) are not fully harmonized.

---

## Proposed Follow-up Experiments / Actions

1. **International natural-history registry** for biallelic *SCN4A* patients to quantify prevalence, survival, and the trajectory of childhood improvement, stratified by genotype (null/null vs null/hypomorph vs hypomorph/hypomorph vs R1460-type).
2. **Genotype–current–phenotype calibration:** systematically voltage-clamp all reported recessive variants under a standardized protocol to derive a quantitative "residual-current index" and correlate with clinical severity.
3. **Hypomorphic/knock-in mouse models** (e.g., R1460W or patient hypomorphic alleles) to model the survivable, improving phenotype and serve as a therapeutic testing platform.
4. **Developmental expression study** of NaV1.4 (and any compensatory channels) in survivors or model muscle to explain childhood improvement — testing the developmental-compensation hypothesis.
5. **Genotype-stratified therapeutic trials/n-of-1 protocols** for the myasthenic subtype (AChE inhibitors, β2-agonists, acetazolamide, 3,4-diaminopyridine), prioritizing partial-LOF genotypes most likely to benefit.
6. **Explore current-enhancing strategies** (e.g., agents that reduce fast inactivation or increase channel availability) specifically for partial-LOF variants with hyperpolarized inactivation shifts (R1460, V1442E).
7. **Standardize variant-curation guidance** (ClinGen/ACMG mechanism-informed framework) distinguishing recessive LOF from dominant GOF *SCN4A* alleles, to reduce misclassification.

---

### Ontology Term Appendix

- **Disease:** MONDO:0100121
- **Gene/Protein:** *SCN4A* HGNC:10591; UniProt P35499 (NaV1.4); NCBI Gene 6329
- **HPO (selected):** HP:0001558 (decreased fetal movement), HP:0001319 (neonatal hypotonia), HP:0030319 (facial-muscle weakness), HP:0002015 (dysphagia), HP:0002093 (respiratory insufficiency), HP:0000508 (ptosis), HP:0003473 (fatigable weakness), HP:0002650 (scoliosis), HP:0002804 (arthrogryposis multiplex congenita)
- **GO (BP):** GO:0001508 (action potential), GO:0086010 (membrane depolarization during AP), GO:0003009 (skeletal muscle contraction), GO:0005248 (voltage-gated sodium channel activity)
- **GO (CC):** GO:0005886 (plasma membrane), GO:0030315 (T-tubule)
- **CL:** CL:0000188 (skeletal muscle cell / myofiber)
- **UBERON:** UBERON:0001134 (skeletal muscle tissue), UBERON:0001004 (respiratory system), UBERON:0002090 (axial skeleton)
- **CHEBI:** CHEBI:29101 (sodium ion)
- **NCIT (interventions):** supportive care (C15329), mechanical ventilation, physical therapy (C15327), pyridostigmine, salbutamol, acetazolamide

---

*Report compiled from a 5-iteration autonomous investigation integrating human clinical cohorts, in vitro electrophysiology, a mouse knockout model, population-genetic constraint (gnomAD), and review literature. Evidence types are indicated throughout; all mechanistic and clinical claims are anchored to cited PMIDs.*


## Artifacts

- [OpenScientist final report](SCN4A-Related_Myopathy_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SCN4A-Related_Myopathy_Autosomal_Recessive-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 23 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100121` (5 mentions) - the report calls it "Mondo"; MONDO calls it **SCN4A-related myopathy, autosomal recessive**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:29101` (2 mentions) - the report calls it "sodium ion"; CHEBI calls it **sodium(1+)**, and lists "SODIUM ION" among its other names
- `GO:0086010` (2 mentions) - the report calls it "membrane depolarization during AP"; GO calls it **membrane depolarization during action potential**
- `CL:0000188` (3 mentions) - the report calls it "skeletal muscle cell / myofiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `UBERON:0002090` (2 mentions) - the report calls it "axial skeleton"; UBERON calls it **postcranial axial skeleton**, and lists "axial skeleton" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0001558` - called "Decreased fetal movement", "decreased fetal movement"
- `HP:0001319` - called "Neonatal hypotonia", "neonatal hypotonia"
- `HP:0002015` - called "Dysphagia", "dysphagia"
- `HP:0002093` - called "Respiratory insufficiency", "respiratory insufficiency"
- `HP:0000508` - called "Ptosis", "ptosis"
- `HP:0003473` - called "Fatigable weakness", "fatigable weakness"
- `HP:0002650` - called "Scoliosis", "scoliosis"
- `HP:0002804` - called "Arthrogryposis multiplex congenita", "arthrogryposis multiplex congenita"