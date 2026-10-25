---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T20:55:35.497951'
end_time: '2026-10-23T21:14:44.598132'
duration_seconds: 1149.1
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: TPM2-Related Myopathy
  mondo_id: MONDO:0100196
  category: Mendelian
  causal_genes: TPM2
  omim_id: not recorded
  synonyms: beta-tropomyosin-related myopathy; congenital myopathy 23; nemaline myopathy
    4; cap myopathy 2
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 15
  validator_version: 0.3.0
term_validation:
  total_terms: 45
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0003458
    reported_labels:
    - Myopathic EMG
    - "Electrophysiology / labs** \u2014 myopathic EMG"
    ontology_label: 'EMG: myopathic abnormalities'
  labels_variant: 9
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: TPM2-Related_Myopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: TPM2-Related_Myopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** TPM2-Related Myopathy
- **MONDO ID:** MONDO:0100196 (if available)
- **Causal gene(s):** TPM2
- **OMIM:** not recorded
- **Synonyms:** beta-tropomyosin-related myopathy; congenital myopathy 23; nemaline myopathy 4; cap myopathy 2
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **TPM2-Related Myopathy** covering all of the
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

# TPM2-Related Myopathy (MONDO:0100196): A Comprehensive Disease Characterization

**Causal gene: _TPM2_ (β-tropomyosin), HGNC:12011, NCBI Gene 7169, Ensembl ENSG00000198467, UniProt P07951, cytoband 9p13.3, OMIM gene 190990.**

> **Causal gene stated up front:** This report concerns disease caused by pathogenic variants in **TPM2**, the gene encoding **β-tropomyosin (beta-tropomyosin / slow skeletal-muscle tropomyosin)**, a sarcomeric thin-filament regulatory protein. Serial-number disease aliases (nemaline myopathy 4 / NEM4, congenital myopathy 23 / CMYP23, cap myopathy 2, distal arthrogryposis 1A/2B) all map to TPM2. This is distinct from **TPM3** (α-tropomyosin slow — a different gene causing an overlapping myopathy) and from **TPM1** (cardiac α-tropomyosin — causing cardiomyopathy, not this disease).

---

## Summary

**TPM2-related myopathy (MONDO:0100196)** is a rare, predominantly autosomal-dominant congenital myopathy of skeletal muscle caused by germline pathogenic variants in **_TPM2_**, the gene encoding the sarcomeric thin-filament protein **β-tropomyosin**. This single gene produces an unusually broad clinical–histopathological spectrum: **nemaline myopathy (NEM4 / congenital myopathy 23)**, **cap myopathy**, **core-rod myopathy**, **congenital fiber-type disproportion (CFTD)**, and the contracture-predominant **distal arthrogryposis types 1A and 2B (Sheldon-Hall syndrome)** and **trismus-pseudocamptodactyly (DA7)**. A rare biallelic (recessive) loss-of-function mechanism causes **Escobar-variant multiple pterygium syndrome with congenital myopathy**. The most penetrant single feature across all entities is **muscle weakness**, accompanied by hypotonia, myopathic facies, and (for a subset of alleles) joint contractures.

The dominant pathomechanism is **gain-of-function at the actin–tropomyosin interface**, most prominently manifested as **increased myofibrillar calcium sensitivity ("hypercontractility")**. This molecular phenotype correlates with the clinical contracture phenotype: patients with hypercontractile alleles have far higher rates of limb-joint and jaw contractures. A second, more recently described pathomechanism is **disrupted myogenesis / myofibrillogenesis**, validated across _Drosophila_, mouse myotube, and zebrafish model systems, in which variant severity in developmental assays tracks with clinical severity. Population genetics corroborate a non-haploinsufficiency mechanism: _TPM2_ is strongly **missense-constrained** (gnomAD missense Z = 3.81) yet **loss-of-function–tolerant** (LOEUF 0.88, pLI ≈ 0), exactly the signature expected for a dominant missense/dominant-negative disorder rather than one driven by gene dosage.

Clinically, TPM2 disease tends to be **milder and more stable than TPM3-related disease**, with normal or only mildly elevated creatine kinase, slow-to-no progression, and generally normal life expectancy, although **respiratory muscle weakness is the principal threat to survival**, and a cap-myopathy subset can progress to infantile respiratory failure. There is **no approved disease-modifying therapy**; management is supportive and multidisciplinary (respiratory surveillance, orthopedic correction of contractures/scoliosis, physiotherapy, and nutritional support). One notable treatable complication is a **secondary neuromuscular-transmission defect** in some cap-myopathy patients that responds to anticholinesterase therapy. Diagnosis rests on **muscle biopsy histopathology** (nemaline rods, caps, cores, fiber-type disproportion) plus **molecular confirmation by NGS gene panels or exome/genome sequencing**.

---

## 1. Disease Information

TPM2-related myopathy is a **congenital myopathy of the musculoskeletal system** caused by pathogenic variants in the skeletal-muscle β-tropomyosin gene. The MONDO definition describes it as covering *"a wide spectrum of phenotypes … characterized by muscle weakness, amyotrophy, hypotonia, myopathic facies, scoliosis, and sometimes contractures,"* with histology that is *"variable with nemaline and intranuclear bodies, cap-like lesions, core-like lesions, fiber-type disproportion, and dystrophic features."* MONDO notes that **the most penetrant phenotype among all TPM2-related myopathy entities is muscular weakness**, and that contracture-primary distal arthrogryposis is a related but partly distinct entity.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0100196 (TPM2-related myopathy) |
| Gene | TPM2 · HGNC:12011 · NCBI Gene 7169 · Ensembl ENSG00000198467 · UniProt P07951 · OMIM gene 190990 · cytoband 9p13.3 |
| OMIM (disease aliases) | NEM4 609285 · DA1 108120 · DA2B 601680 |
| Orphanet (entities) | Typical NM ORPHA:171436 · Childhood NM ORPHA:171439 · Cap myopathy ORPHA:171881 · CFTD ORPHA:2020 · DA1 ORPHA:1146 · DA2B/Sheldon-Hall ORPHA:1147 |
| GARD | 0026079 |

**Synonyms / alternative names:** beta-tropomyosin-related myopathy; TPM2 myopathy; autosomal dominant TPM2-related myopathy; congenital myopathy 23 (CMYP23/CMYO23); nemaline myopathy 4 (NEM4); cap myopathy 2; core-rod myopathy; congenital fiber-type disproportion; distal arthrogryposis 1A and 2B; trismus-pseudocamptodactyly (DA7); Escobar-variant multiple pterygium syndrome (recessive).

**Information source:** Aggregated disease-level resources (OMIM, Orphanet, MONDO, HPO) plus primary-literature cohorts and case reports — not EHR/individual-patient registries.

---

## 2. Etiology

**Primary cause — genetic.** TPM2-related myopathy is a **monogenic Mendelian disorder** caused by pathogenic germline variants in _TPM2_. The overwhelming majority are **heterozygous missense substitutions and small in-frame indels** acting dominantly (e.g., ΔK7/p.K7del, ΔK49, R91G, ΔE139, K168E, E181K). A review of **53 families** identified **30 distinct pathogenic variants** with autosomal-dominant inheritance ([PMID: 24692096](https://pubmed.ncbi.nlm.nih.gov/24692096/)). A rare **recessive** route exists through biallelic loss-of-function (e.g., homozygous splice variant c.564-2A>C) ([PMID: 33558124](https://pubmed.ncbi.nlm.nih.gov/33558124/)).

**Genetic risk factors:** The causal variant itself is the risk factor; there are no established susceptibility loci or polygenic modifiers. Variant position (within actin-binding structural motifs vs elsewhere) influences the biochemical and clinical phenotype, though one DA study found "no relation between the types or locations of TPM2 mutations and the clinical characteristics" ([PMID: 30285720](https://pubmed.ncbi.nlm.nih.gov/30285720/)), tempering simple position-based rules.

**Environmental risk factors:** None established. This is a constitutional genetic disorder; onset is typically congenital/neonatal and not triggered by environmental exposures. **Consanguinity** is relevant only to the rare recessive form ([PMID: 33558124](https://pubmed.ncbi.nlm.nih.gov/33558124/)).

**Protective factors:** No genetic or environmental protective factors have been identified. Notably, gnomAD shows **loss-of-function tolerance** — heterozygous LoF is not disease-causing, which is mechanistically informative (haploinsufficiency is non-pathogenic) rather than "protective."

**Gene–environment interactions:** None documented. This is essentially a purely genetic disorder.

---

## 3. Phenotypes

TPM2 disease is **skeletal-muscle-restricted**; **cardiac and CNS involvement is NOT characteristic**. Cardinal phenotypes with suggested HPO terms, severity, and onset:

| Phenotype | HPO term | Type | Onset | Frequency/severity |
|---|---|---|---|---|
| Generalized hypotonia | HP:0001290 (neonatal HP:0001319) | Clinical sign | Congenital/neonatal | Very common; cardinal feature |
| Muscle weakness (proximal) | HP:0003701; Myopathy HP:0003198 | Symptom/sign | Congenital–childhood | Most penetrant feature |
| Facial weakness | HP:0030319; Myopathic facies HP:0002058 | Clinical sign | Early | Common |
| Ptosis | HP:0000508 | Clinical sign | Early | Frequent |
| High/arched palate | HP:0000218 | Physical | Congenital | Frequent |
| Feeding difficulties | HP:0011968 | Symptom | Neonatal | Common, variable |
| Respiratory insufficiency (muscle weakness) | HP:0002747 | Sign | Variable | Main prognostic threat |
| Scoliosis | HP:0002650 | Physical | Childhood | Common |
| Joint contractures | HP:0034392 | Physical | Congenital | Allele-dependent; hypercontractile alleles |
| Arthrogryposis multiplex congenita | HP:0002804 | Physical | Congenital | DA subtypes |
| Talipes equinovarus | HP:0001762 | Physical | Congenital | DA subtypes |
| Camptodactyly | HP:0012385 | Physical | Congenital | DA subtypes |
| Ulnar deviation of hand | HP:0009465 | Physical | Congenital | DA subtypes |
| Nemaline bodies (biopsy) | HP:0003798 | Lab/histology | — | Defining in NM form |
| Central core regions | HP:0030230 | Lab/histology | — | Core-rod form |
| Type 1 fiber predominance | HP:0003803 | Lab/histology | — | CFTD form |
| Myopathic EMG | HP:0003458 | Lab | — | Common |
| Elevated creatine kinase | HP:0008180 | Lab | — | Normal to mildly elevated |

**Severity and progression:** Generally **mild and relatively stable**; TPM2 patients *"tended to present with milder symptoms than those with TPM3 mutations"* ([PMID: 24692096](https://pubmed.ncbi.nlm.nih.gov/24692096/)). Distal-arthrogryposis contractures are typically **non-progressive and congenital** ([PMID: 23401156](https://pubmed.ncbi.nlm.nih.gov/23401156/)).

**Quality-of-life impact:** Weakness, contractures, scoliosis, and respiratory/bulbar involvement impair mobility, feeding, and respiratory function; disease-specific QoL instruments (EQ-5D/SF-36/PROMIS) have not been applied to TPM2-only cohorts (knowledge gap).

---

## 4. Genetic / Molecular Information

**Causal gene:** _TPM2_ (β-tropomyosin), 9p13.3, OMIM 190990. Encodes a two-chain coiled-coil thin-filament regulatory protein that, with the troponin complex, controls Ca²⁺-dependent actin–myosin interaction.

**Pathogenic variants:**
- **Classification:** ClinVar (~480 records): ~148 pathogenic, ~46 likely pathogenic, ~285 VUS, plus benign/likely-benign.
- **Variant type/class:** Overwhelmingly **missense and small in-frame indels** (e.g., ΔK7/c.20_22del, ΔK49, R91G, ΔE139, K168E, E181K, Q103R). Rare splice/intronic LoF (c.564-2A>C) in the recessive form.
- **Allele frequency:** Pathogenic variants are private/rare; absent or extremely rare in gnomAD.
- **Origin:** Germline; both inherited and de novo (recurrent de novo missense documented in MPS-related disorder, [PMID: 32092148](https://pubmed.ncbi.nlm.nih.gov/32092148/)). No somatic role.
- **Functional consequences:** **Gain-of-function / dominant-negative** — increased myofibrillar Ca²⁺ sensitivity and/or disrupted thin-filament polymerization and myogenesis. Recessive disease = **loss of function** (exon-6b isoform).

**Population constraint (gnomAD v2.1.1):** missense Z = **3.81** (strong missense depletion); **pLI ≈ 5.5×10⁻⁶**, observed/expected LoF = 0.63 (26 obs / 41 exp), **LOEUF = 0.88** — the gene is **missense-constrained but NOT loss-of-function–intolerant**, the hallmark of a dominant missense/dominant-negative disorder, not haploinsufficiency.

**Modifier genes / epigenetics / chromosomal abnormalities:** None established for TPM2 disease. No DNA-methylation/histone signatures identified; no recurrent structural/cytogenetic lesions.

---

## 5. Environmental Information

**Environmental factors:** None implicated — this is a constitutional genetic disorder.
**Lifestyle factors:** None causative; physiotherapy and activity modification are supportive, not etiologic.
**Infectious agents:** Not applicable. (Note: sporadic late-onset nemaline myopathy and HIV-associated nemaline myopathy are separate acquired entities not caused by TPM2.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

**Dominant (common) branch — gain-of-function:**

1. A **heterozygous germline missense or small in-frame indel in _TPM2_** (e.g., ΔK7, R91G, E139K) **alters the β-tropomyosin coiled-coil**, especially at residues in repeating actin-binding structural motifs or the N-terminal head-to-tail polymerization region. *(demonstrated: genetics + biochemistry)*
2. This **leads to** altered positioning/dynamics of tropomyosin on the actin thin filament at the **actin–tropomyosin interface**. *(demonstrated in vitro)*
3. Which **results in** either **(a) increased myofibrillar Ca²⁺ sensitivity (hypercontractility)** or **(b) disrupted head-to-tail polymerization and thin-filament assembly**. *(demonstrated: in-vitro motility; zebrafish sarcomere assays)*
4. Branch (a) **leads to** excess contractile tone in developing muscle → **fixed joint and jaw contractures** (distal arthrogryposis, trismus-pseudocamptodactyly). *(inferred from genotype–phenotype correlation)*
5. Branch (b) **leads to** **disrupted myogenesis/myofibrillogenesis** → abnormal fiber formation and structural lesions (nemaline rods from Z-disk/α-actinin material; cap-like subsarcolemmal accumulations; cores; fiber-type disproportion). *(demonstrated in fly/mouse/fish; severity correlates with clinical severity)*
6. Both branches **result in** **muscle weakness, hypotonia, myopathic facies, feeding/respiratory difficulty, scoliosis**. *(clinical)*
7. In some cap-myopathy patients, thin-filament disorganization is **associated with** a **secondary neuromuscular-transmission defect** → fatigable, anticholinesterase-responsive weakness. *(demonstrated in a case)*

**Recessive (rare) branch — loss-of-function:**

1′. **Biallelic LoF** (homozygous splice variant c.564-2A>C abolishing exon-6b acceptor) **leads to** loss of the exon-6b skeletal β-tropomyosin isoform → **Escobar-variant multiple pterygium syndrome + congenital myopathy**; heterozygotes unaffected. *(demonstrated)*

### Upstream vs downstream

| Level | Mechanism | Evidence class |
|---|---|---|
| **Upstream (initiating)** | TPM2 missense/in-frame indel altering coiled-coil | Human genetics; gnomAD constraint |
| **Proximal molecular** | Altered actin–tropomyosin interface; ↑Ca²⁺ sensitivity; impaired polymerization | In vitro motility; computational |
| **Cellular/developmental** | Disrupted myofibrillogenesis; rods/caps/cores | Fly/mouse/fish models; biopsy |
| **Tissue/physiology** | Hypercontractility, weakness, fatigue | Clinical; electrophysiology |
| **Downstream (clinical)** | Contractures, hypotonia, respiratory/bulbar weakness, scoliosis | Clinical cohorts |

**Molecular pathways / processes (GO):** muscle contraction (**GO:0006936**), actin filament organization (**GO:0007015**), regulation of ATP-dependent activity (**GO:0043462**), myogenesis/muscle development. **Molecular function:** actin filament binding (**GO:0051015**), structural constituent of muscle (**GO:0008307**), protein homo-/heterodimerization (**GO:0042803/GO:0046982**).

**Cell types / subcellular (CL / GO-CC):** slow type-I skeletal muscle fiber (**CL:0002211**), skeletal muscle fiber (**CL:0000188**); sarcomere (**GO:0030017**), muscle thin-filament tropomyosin (**GO:0005862**), striated-muscle thin filament (**GO:0005865**), actin cytoskeleton (**GO:0015629**).

**Metabolic / immune / epigenetic:** No primary metabolic defect, no autoimmune/inflammatory mechanism, and no epigenetic mechanism characteristic of TPM2 disease (distinguishing it from acquired sporadic late-onset nemaline myopathy, which has an immune/MGUS association).

---

## 7. Anatomical Structures Affected

**Organ level:** Primary — **skeletal muscle** (UBERON:0001134). Preferentially **axial, facial, limb-girdle, and respiratory (diaphragm/intercostal) muscles**. Secondary — skeleton (scoliosis, joint contractures), respiratory system (ventilatory insufficiency from muscle weakness), and feeding/bulbar apparatus. **No primary cardiac or CNS involvement.**

**Tissue/cell level:** Striated skeletal muscle tissue; **slow (type I) skeletal muscle fibers** (CL:0002211) are preferentially affected — TPM2 is *"mainly expressed in slow, type 1 muscle fibers."* Pathology includes type-1 fiber predominance and atrophy.

**Subcellular level:** **Sarcomere / thin filament** (GO:0030017, GO:0005865, GO:0005862). Nemaline rods derive from Z-disk/α-actinin material; cap-like lesions are subsarcolemmal thin-filament accumulations.

**Localization / lateralization:** Generally **bilateral and symmetric**. Distal arthrogryposis is characteristically bilateral/symmetric (clenched fists, overlapping fingers, talipes equinovarus).

---

## 8. Temporal Development

**Onset:** Typically **congenital or neonatal** (hypotonia, feeding/respiratory difficulty, contractures); some milder cases present in childhood. Prenatal clues include **decreased fetal movements (HP:0001558)** and **polyhydramnios (HP:0001561)**.

**Progression:** **Slow or non-progressive / relatively stable** in most cases. Distal-arthrogryposis contractures are non-progressive. The cap-myopathy subset can progress to respiratory failure in infancy ([PMID: 25079567](https://pubmed.ncbi.nlm.nih.gov/25079567/) context). Disease is **chronic and lifelong**.

**Patterns:** No spontaneous remission; course is static-to-slowly-progressive. **Critical period:** The developmental/myogenesis window is mechanistically critical (disrupted myofibrillogenesis), suggesting early muscle development is a key vulnerability period.

---

## 9. Inheritance and Population

**Epidemiology:** Congenital myopathies as a group: **birth prevalence 14.9/100,000, cumulative incidence by age 35 of 12.3/100,000, point prevalence 3.9/100,000** (western Sweden) ([PMID: 41159764](https://pubmed.ncbi.nlm.nih.gov/41159764/)). TPM2 is a **minority cause**. In distal arthrogryposis, mutations were *"distributed nearly equally across TNNI2, TNNT3, TPM2, and MYH3"* ([PMID: 23401156](https://pubmed.ncbi.nlm.nih.gov/23401156/)) — TPM2 is one of four roughly equal DA genes.

**Inheritance:** Predominantly **autosomal dominant** (de novo or inherited); rare **autosomal recessive** (Escobar-variant). **Penetrance** is high for the dominant form; **expressivity is variable** (same gene → NM/cap/core-rod/CFTD/DA). No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism is plausible but not well documented. **Carrier frequency** of pathogenic LoF alleles is low; heterozygous LoF carriers are unaffected (recessive form). **Consanguinity** is relevant only to the recessive form.

**Population demographics:** No strong ethnic predilection; cases reported worldwide (European, Chinese, Middle Eastern cohorts). No established sex bias. Founder effects are not described for TPM2; the recessive Escobar variant arose in a consanguineous family.

---

## 10. Diagnostics

**Diagnostic pillars:**

1. **Muscle biopsy histopathology** — the defining investigation. *"The condition is defined by the histopathological finding of nemaline bodies (rods) on muscle biopsy"* ([PMID: 27659899](https://pubmed.ncbi.nlm.nih.gov/27659899/)). Findings: nemaline rods (Gomori trichrome red, electron-dense Z-disk-derived bodies; HP:0003798), cap-like subsarcolemmal structures, central cores/mini-cores, congenital fiber-type disproportion (type-1 fibers 12–25% smaller than type-2) with type-1 predominance. **α-actinin immunohistochemistry** highlights rods/caps.
2. **Electrophysiology / labs** — myopathic EMG (HP:0003458); CK normal or mildly elevated (HP:0008180). In cap myopathy with myasthenic features, repetitive nerve stimulation/single-fiber EMG may reveal a transmission defect.
3. **Molecular genetics** — targeted **NGS congenital-myopathy / nemaline gene panels** (TPM2, TPM3, ACTA1, NEB, TNNT1, KBTBD13, RYR1, etc.) or **whole-exome / whole-genome sequencing**; single-gene TPM2 testing when phenotype is characteristic (trismus-pseudocamptodactyly, hypercontractile DA). **Linkage** can map to TPM2 ([PMID: 30285720](https://pubmed.ncbi.nlm.nih.gov/30285720/)). **Intronic/splice variants** (c.564-2A>C) may require **WGS/RNA analysis** beyond exon panels ([PMID: 33558124](https://pubmed.ncbi.nlm.nih.gov/33558124/)).

**Imaging:** Muscle MRI can show selective muscle involvement patterns (supportive, not specific).

**Differential diagnosis:** Other congenital myopathies (TPM3, ACTA1, NEB, KBTBD13/NEM6, RYR1), congenital muscular dystrophies (LAMA2-RD), other distal-arthrogryposis genes (TNNI2, TNNT3, MYH3, PIEZO2), and acquired sporadic late-onset nemaline myopathy (SLONM — distinguished by late onset, MGUS/HIV association, treatable).

**Screening:** No newborn/population screening. **Cascade genetic testing** of at-risk relatives and **prenatal/preimplantation testing** are feasible once the familial variant is known.

---

## 11. Outcome / Prognosis

**Survival / mortality:** Generally **normal-to-near-normal life expectancy**, especially for distal-arthrogryposis and milder myopathy forms. **Respiratory muscle weakness is the principal threat**; the cap-myopathy subset can develop infantile respiratory failure.

**Morbidity / function:** In a cross-sectional nemaline-myopathy study (pooled NM genes, not TPM2-only): *"Fifty-eight percent of individuals needed mechanical support, with 26% requiring wheelchair, tracheostomy, and feeding tube"* ([PMID: 33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/)); course was *"relatively stable."* TPM2 disease is at the **milder** end: *"Patients with TPM2 mutations tended to present with milder symptoms than those with TPM3 mutations"* ([PMID: 24692096](https://pubmed.ncbi.nlm.nih.gov/24692096/)).

**Complications:** Respiratory insufficiency, scoliosis, contractures/orthopedic deformity, feeding difficulty/failure to thrive, and (rarely) secondary neuromuscular-transmission defects.

**Prognostic factors:** Histological subtype (cap → respiratory risk), degree of respiratory/bulbar involvement, and (experimentally) variant severity in myogenesis assays, which correlated with clinical severity in DA patients ([PMID: 35579956](https://pubmed.ncbi.nlm.nih.gov/35579956/)).

---

## 12. Treatment

**No approved disease-modifying therapy.** Management is **supportive and multidisciplinary** (NCIT concepts: supportive care, physical therapy, respiratory therapy, orthopedic surgery, nutritional support):

- **Respiratory care** — surveillance of pulmonary function, non-invasive/invasive ventilation as needed; the main determinant of survival.
- **Orthopedic/rehabilitative** — physiotherapy and occupational therapy for contractures and mobility; surgical correction of scoliosis, talipes, and fixed contractures; serial casting/bracing in distal arthrogryposis.
- **Nutritional/GI** — management of feeding difficulty, dysphagia, reflux; gastrostomy when required.
- **Pharmacotherapy** — no specific drug therapy. A **treatable exception**: cap myopathy with a secondary neuromuscular-transmission defect responds to **anticholinesterase therapy** (e.g., pyridostigmine) — *"We describe a case of cap myopathy with myasthenic features due to a mutation in the TPM2 gene that responded to anticholinesterase therapy"* ([PMID: 25127990](https://pubmed.ncbi.nlm.nih.gov/25127990/)).
- **Pharmacogenomics / gene / cell / RNA therapy** — none established; allele-selective silencing is conceptually attractive given LoF tolerance (see follow-up).

**Treatment strategy:** Genotype/phenotype-guided surveillance (respiratory emphasis for cap myopathy; orthopedic emphasis for DA). No combination or targeted regimens exist.

---

## 13. Prevention

**Primary prevention:** Not possible for a constitutional genetic disorder beyond reproductive options. **Genetic counseling** (autosomal dominant 50% transmission risk; recessive 25% risk in consanguineous families) and **preimplantation/prenatal genetic testing** once the familial variant is known.

**Secondary prevention:** Early multidisciplinary surveillance (respiratory, orthopedic, nutritional) to detect and manage complications early.

**Tertiary prevention:** Prevention of complications — respiratory support to avert failure, scoliosis/contracture correction, aspiration/nutrition management.

**Screening/counseling:** Cascade testing of relatives; genetic counseling per NSGC/ACMG. No immunization or public-health/environmental interventions apply.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs:** Human _TPM2_ is evolutionarily conserved. Orthologs — mouse _Tpm2_ (NCBI Gene **22004**), rat _Tpm2_ (**500450**), zebrafish _tpma_ (**30324**), _Drosophila_ tropomyosin Tm1/Tm2; conserved coiled-coil actin-binding thin-filament protein (HomoloGene 134045).

**Natural disease / veterinary relevance:** **No naturally occurring TPM2 disease is catalogued in OMIA.** There is no documented companion-animal or wildlife spontaneous TPM2 myopathy; all animal disease is **engineered/induced**.

**Comparative biology:** The thin-filament contractile mechanism is deeply conserved from invertebrates to mammals, which is why fly/fish/mouse models recapitulate human TPM2 pathology. **Zoonotic/cross-species transmission:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Model types and genetic models:** Pathogenicity of dominant TPM2 variants has been validated across three systems through **transient overexpression/transgenesis** ([PMID: 35579956](https://pubmed.ncbi.nlm.nih.gov/35579956/)):

| Model | System | Finding |
|---|---|---|
| _Drosophila_ embryo | Invertebrate, in vivo | 4 variants significantly affected muscle development & function |
| Mouse myotube (C2C12-type) | Mammalian, in vitro | Variants disrupted myotube morphogenesis |
| Zebrafish | Vertebrate, in vivo | Impaired muscle development; **severity correlated with clinical severity** (V129A, E139K, A155T) |

An earlier **zebrafish p.K7del model** showed the mutant protein *"fails to localize properly within the thin filament compartment and its expression alters sarcomere length"* ([PMID: 23413262](https://pubmed.ncbi.nlm.nih.gov/23413262/)). **In vitro reconstitution / motility assays** with purified human β-tropomyosin quantify altered Ca²⁺ sensitivity (R91G, [PMID: 29097206](https://pubmed.ncbi.nlm.nih.gov/29097206/); Q93H/E97K, [PMID: 33919826](https://pubmed.ncbi.nlm.nih.gov/33919826/); ΔK7 and motif mutations, [PMID: 23886664](https://pubmed.ncbi.nlm.nih.gov/23886664/)).

**Model characteristics:** These models recapitulate developmental muscle defects, thin-filament mislocalization, altered sarcomere length, and calcium-handling abnormalities, and predict clinical severity. **Limitations:** no established mammalian **knock-in** model of a recurrent allele carried to adulthood; most assays use transient overexpression rather than physiological endogenous expression, and do not fully model the mature-muscle, lifelong clinical course.

**Resources:** MGI (mouse Tpm2), RGD (rat), ZFIN (zebrafish tpma), FlyBase (Tm1/Tm2).

---

## Mechanistic Model / Interpretation (synthesis)

### Genotype → molecular phenotype → clinical phenotype (illustrative)

| Variant | Molecular effect | Predominant clinical phenotype |
|---|---|---|
| ΔK7 (p.K7del) | ↑Ca²⁺ sensitivity; disrupts N-terminal polymerization | Core-rod myopathy; trismus-pseudocamptodactyly (DA7) |
| R91G | High Ca²⁺ sensitivity | Distal arthrogryposis |
| E139K / ΔE139 | ↑Ca²⁺ sensitivity; disrupts myogenesis | Distal arthrogryposis / congenital myopathy |
| R167H | No change in Ca²⁺ sensitivity | Non-hypercontractile myopathy |
| c.564-2A>C (homozygous) | Loss of exon-6b isoform (recessive LoF) | Escobar-variant MPS + congenital myopathy |

The data converge on a **two-branch gain-of-function model**: dominant missense/in-frame alleles perturb the actin–tropomyosin interface, producing either **hypercontractility** (→ contractures/distal arthrogryposis) or **disrupted myofibrillogenesis** (→ structural lesions and weakness), often both. This is independently corroborated by population genetics (missense-constrained, LoF-tolerant) and by cross-species models whose severity predicts clinical severity. A minor, mechanistically opposite recessive LoF branch produces the Escobar-variant phenotype.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [24692096](https://pubmed.ncbi.nlm.nih.gov/24692096/) | *Mutation update & genotype–phenotype, TPM2/TPM3* | Human, 53-family review | Spectrum; hypercontractility–contracture link; milder than TPM3 |
| [23886664](https://pubmed.ncbi.nlm.nih.gov/23886664/) | *Mutations in repeating motifs cause gain of function* | In vitro biochemistry | ↑Ca²⁺ sensitivity; actin–tropomyosin interface |
| [35579956](https://pubmed.ncbi.nlm.nih.gov/35579956/) | *TPM2-directed myogenesis pathomechanism* | Fly/mouse/fish models | Disrupted myogenesis; severity correlation |
| [33558124](https://pubmed.ncbi.nlm.nih.gov/33558124/) | *Homozygous intronic TPM2 → Escobar + myopathy* | Human, consanguineous family | Recessive LoF; splice variant |
| [32092148](https://pubmed.ncbi.nlm.nih.gov/32092148/) | *Recurrent TPM2 variant in MPS-related disorder* | Human, 3 cases | De novo dominant MPS |
| [23401156](https://pubmed.ncbi.nlm.nih.gov/23401156/) | *Mutations in DA1 and DA2B* | Human, 153 kindreds | TPM2 one of four DA genes |
| [41159764](https://pubmed.ncbi.nlm.nih.gov/41159764/) | *Incidence/prevalence of congenital myopathy, Sweden* | Population-based | Epidemiology |
| [25127990](https://pubmed.ncbi.nlm.nih.gov/25127990/) | *Congenital myopathies with secondary NMJ defects* | Human case + review | Treatable NMJ defect |
| [27659899](https://pubmed.ncbi.nlm.nih.gov/27659899/) | *Nemaline myopathies: state of the art* | Review | Biopsy definition |
| [33397769](https://pubmed.ncbi.nlm.nih.gov/33397769/) | *Cross-sectional study of nemaline myopathy* | Human cohort | Morbidity/support needs |
| [23413262](https://pubmed.ncbi.nlm.nih.gov/23413262/) | *Novel K7del expands TPM2 spectrum* | Human + zebrafish | Core-rod; DA7; polymerization defect |
| [29097206](https://pubmed.ncbi.nlm.nih.gov/29097206/) | *Reason for high Ca²⁺ sensitivity (R91G)* | In vitro | R91G biochemistry |
| [33919826](https://pubmed.ncbi.nlm.nih.gov/33919826/) | *Mutations Q93H and E97K* | In vitro | Ca²⁺ regulation |
| [30285720](https://pubmed.ncbi.nlm.nih.gov/30285720/) | *Novel TPM2/PIEZO2 in DA* | Human, linkage + WES | Linkage mapping; no position–phenotype rule |
| [25079567](https://pubmed.ncbi.nlm.nih.gov/25079567/) | *Cap-like structures and nemaline rods* | Human case + review | Cap myopathy natural history (respiratory risk) |

**Source-type triangulation:** human clinical/genetic (majority), in vitro biochemistry (mechanism), multi-species model organisms (developmental mechanism), and gnomAD population constraint. The gain-of-function conclusion is supported by all four independent evidence classes, giving it high confidence.

---

## Limitations and Knowledge Gaps

1. **No TPM2-specific natural-history cohort.** Prognostic data are borrowed from mixed nemaline-myopathy cohorts; TPM2-only survival curves and QoL metrics (EQ-5D/SF-36/PROMIS) are unavailable.
2. **High VUS burden** (~285/480 ClinVar records), limiting clinical interpretation; functional classification is not scaled to the full variant set.
3. **Mechanistic branch weighting unknown** — the relative contribution of hypercontractility vs disrupted myogenesis per patient is not quantified.
4. **Modifier genes and epigenetics uncharacterized** for TPM2 disease.
5. **No approved disease-modifying therapy**; the anticholinesterase response is based on isolated cases.
6. **Imperfect genotype–phenotype prediction** — one study found no relation between variant type/location and clinical features.
7. **Underdiagnosis risk** from deep-intronic/splice variants missed by exon-only panels.

---

## Proposed Follow-up Experiments / Actions

1. **Build a TPM2-specific natural-history registry** (onset, motor/respiratory trajectory, scoliosis, survival) stratified by histological subtype and hypercontractile vs non-hypercontractile allele class.
2. **High-throughput VUS reclassification** using standardized Ca²⁺-sensitivity motility and zebrafish/myotube myogenesis assays; feed results to ClinVar/ClinGen.
3. **Systematic screen for secondary NMJ defects** (RNS, single-fiber EMG) across the cohort to identify anticholinesterase-responsive patients — low-cost, potentially practice-changing.
4. **Preclinical testing of calcium-desensitizing agents** in hypercontractile TPM2 models, targeting the defined druggable node of excess myofilament Ca²⁺ sensitivity.
5. **Allele-selective RNA therapeutics (ASO/siRNA)** to silence the dominant mutant allele, leveraging gnomAD LoF tolerance (haploinsufficiency is not disease-causing).
6. **Routine WGS + RNA-seq** for biopsy-positive, panel-negative congenital myopathy to capture splice variants like c.564-2A>C.
7. **Generate a knock-in mouse** carrying a recurrent hypercontractile allele (R91G or E139K) for in-vivo therapeutic and natural-history studies.

---

*Report generated from a 5-iteration autonomous investigation: 13 confirmed findings, 30 papers reviewed. Evidence classes: human clinical/genetic, in vitro biochemistry, multi-species model organisms, and population-genetic constraint.*


## Artifacts

- [OpenScientist final report](TPM2-Related_Myopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](TPM2-Related_Myopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

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
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 18 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0003458` (2 mentions) - the report calls it "Myopathic EMG", "Electrophysiology / labs** — myopathic EMG"; HP calls it **EMG: myopathic abnormalities**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000218` (1 mention) - the report calls it "High/arched palate"; HP calls it **High palate**, and lists "High arched palate" among its other names
- `HP:0002747` (1 mention) - the report calls it "Respiratory insufficiency (muscle weakness)"; HP calls it **Respiratory insufficiency due to muscle weakness**
- `HP:0009465` (1 mention) - the report calls it "Ulnar deviation of hand"; HP calls it **Ulnar deviation of finger**
- `HP:0003798` (2 mentions) - the report calls it "Nemaline bodies (biopsy)"; HP calls it **Nemaline bodies**
- `HP:0030230` (1 mention) - the report calls it "Central core regions"; HP calls it **Central core regions in muscle fibers**
- `HP:0003803` (1 mention) - the report calls it "Type 1 fiber predominance"; HP calls it **Type 1 muscle fiber predominance**
- `HP:0008180` (2 mentions) - the report calls it "Elevated creatine kinase"; HP calls it **Mildly elevated creatine kinase**
- `CL:0002211` (2 mentions) - the report calls it "slow (type I) skeletal muscle fibers"; CL calls it **type I muscle cell**, and lists "slow twitch muscle fiber" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0003458` - called "Myopathic EMG", "Electrophysiology / labs** — myopathic EMG"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.