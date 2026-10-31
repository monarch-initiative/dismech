---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-23T21:08:09.807943'
end_time: '2026-10-23T21:28:46.487549'
duration_seconds: 1236.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Vertebral, Cardiac, Tracheoesophageal, Renal, and Limb Defects
  mondo_id: MONDO:0030987
  category: Mendelian
  causal_genes: WBP11
  omim_id: OMIM:619227
  synonyms: VCTERL; VCTERL syndrome
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
citation_count: 11
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_variant: 1
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
  path: Vertebral_Cardiac_Tracheoesophageal_Renal_And_Limb_Defects-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Vertebral_Cardiac_Tracheoesophageal_Renal_And_Limb_Defects-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vertebral, Cardiac, Tracheoesophageal, Renal, and Limb Defects
- **MONDO ID:** MONDO:0030987 (if available)
- **Causal gene(s):** WBP11
- **OMIM:** OMIM:619227
- **Synonyms:** VCTERL; VCTERL syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Vertebral, Cardiac, Tracheoesophageal, Renal, and Limb Defects** covering all of the
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

# VCTERL Syndrome (WBP11-Related): Comprehensive Disease Characteristics Report

**Disease:** Vertebral, Cardiac, Tracheoesophageal, Renal, and Limb Defects (VCTERL)
**MONDO:** MONDO:0030987 · **OMIM:** 619227 · **Causal gene:** **WBP11** (HGNC:16461)
**Inheritance:** Autosomal dominant (haploinsufficiency)

---

## Summary

**VCTERL syndrome is an autosomal-dominant multiple-congenital-anomaly disorder caused by heterozygous loss-of-function (LoF) or damaging missense variants in *WBP11* (WW domain binding protein 11; HGNC:16461), the gene that encodes a nuclear spliceosome component (also known as SIPP1/NpwBP/Npw38-binding protein) that activates pre-mRNA splicing.** The disorder was defined by Martin and colleagues in 2020, who identified *WBP11* variants in seven unrelated families presenting with overlapping cardiac, vertebral, tracheo-esophageal, renal, and limb defects — i.e., the VACTERL malformation spectrum ([PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)). VCTERL (OMIM:619227) represents the **Mendelian, WBP11-driven subset** of the broader VACTERL association, which is itself predominantly sporadic and multifactorial.

The disease mechanism is **haploinsufficiency**: a single functional copy of *WBP11* is insufficient for normal organogenesis. This is strongly supported by population-genetics constraint data — *WBP11* has a gnomAD probability-of-LoF-intolerance (pLI) of 1.0 (LOEUF 0.29), placing it among the most LoF-intolerant genes in the genome — and by a *Wbp11* mouse model in which homozygous nulls die before embryonic day 8.5 (an essential gene), while heterozygous nulls are small and recapitulate human defects of the axial skeleton, kidneys, and esophagus. A zebrafish *wbp11* loss-of-function model likewise produces multi-system developmental defects modeling VACTERL. As a spliceosome-associated factor, reduced WBP11 dosage is inferred to impair pre-mRNA splicing of developmental regulators during the first-trimester critical window of mesoderm, foregut, and limb-bud patterning.

Because VCTERL is defined by structural malformations present at birth, there is **no disease-specific pharmacotherapy or gene therapy**; management is organ-directed surgical correction and lifelong multidisciplinary supportive care. Prognosis is driven chiefly by the severity of the component malformations — especially cardiac defects — with high survival after successful repair but substantial long-term morbidity, particularly from the esophageal component (dysphagia, reflux, dysmotility, stricture, Barrett's esophagus, respiratory disease, and reduced quality of life). Inheritance shows incomplete penetrance and highly variable expressivity: the same *WBP11* LoF variant can cause full VACTERL-spectrum disease or isolated Klippel-Feil syndrome, renal agenesis, or esophageal atresia.

---

## Key Findings

### Finding 1 — WBP11 haploinsufficiency causes VCTERL syndrome

Martin et al. (2020) reported **heterozygous predicted loss-of-function and predicted damaging missense variants in *WBP11* in seven unrelated families** with a variety of overlapping congenital malformations spanning the cardiac, vertebral, tracheo-esophageal, renal, and limb systems — the VCTERL/VACTERL spectrum. This established *WBP11* as the causal gene for OMIM:619227, with autosomal-dominant inheritance operating through haploinsufficiency.

> *"we report novel heterozygous predicted loss-of-function (LoF) and predicted damaging missense variants in the WW domain binding protein 11 (WBP11) gene in seven unrelated families with a variety of overlapping congenital malformations, including cardiac, vertebral, tracheo-esophageal, renal and limb defects"* — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)

This is the defining case series and the primary evidence basis for the entire gene–disease relationship.

### Finding 2 — WBP11 encodes a spliceosome component that activates pre-mRNA splicing

*WBP11* (aliases **SIPP1, NpwBP, Npw38-binding protein**) encodes a nuclear-speckle-localized component of the spliceosome. Llorian et al. (2004) characterized SIPP1 (= WBP11) as a **pre-mRNA splicing factor and interactor of protein phosphatase-1 (PP1)** via an RVXF docking motif; it binds PQBP-1/Npw38, localizes to nuclear speckles (storage and assembly sites for splicing factors), and a SIPP1 fragment inhibits splicing catalysis in nuclear extracts. Martin et al. (2020) independently describe WBP11 as a splicing-activating spliceosome component. This makes VCTERL a **spliceosomopathy** — a developmental disorder caused by impaired function of the general pre-mRNA splicing machinery.

> *"SIPP1 for splicing factor that interacts with PQBP-1 and PP1"* — [PMID: 14640981](https://pubmed.ncbi.nlm.nih.gov/14640981/)

> *"we found that SIPP1 is also a component of the spliceosomes and that a SIPP1-fragment inhibits splicing catalysis by nuclear extracts"* — [PMID: 14640981](https://pubmed.ncbi.nlm.nih.gov/14640981/)

> *"WBP11 encodes a component of the spliceosome with the ability to activate pre-messenger RNA splicing"* — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)

### Finding 3 — A *Wbp11* mouse model recapitulates VCTERL and shows the gene is essential for development

Martin et al. (2020) generated a *Wbp11* null allele by CRISPR-Cas9. **Homozygous null embryos die before E8.5**, confirming *Wbp11* is an essential gene. **Heterozygous null mice are under-represented (embryonic/postnatal lethality), are small, and exhibit defects of the axial skeleton, kidneys, and esophagus** — directly mirroring the affected humans and providing experimental support for haploinsufficiency as the disease mechanism.

> *"Wbp11 homozygous null embryos die prior to E8.5, indicating that Wbp11 is essential for development"* — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)

> *"Wbp11 heterozygous null mice are small and exhibit defects in axial skeleton, kidneys and esophagus, similar to the affected individuals"* — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)

A complementary **zebrafish *wbp11* loss-of-function model** (*Loss of wbp11 causes multi-system developmental defects: a zebrafish model of VACTERL association*, [PMID: 42625817](https://pubmed.ncbi.nlm.nih.gov/42625817/)) was also established, broadening the cross-species evidence that *WBP11* dosage governs multi-organ morphogenesis.

### Finding 4 — WBP11 is extremely loss-of-function intolerant (pLI = 1.0), supporting haploinsufficiency

gnomAD constraint metrics for *WBP11* (ENSG00000084463, HGNC:16461, chr12:14,784,582–14,803,486 GRCh38, cytoband 12p12.3–p13.1) place it among the most constrained genes genome-wide:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 1.00 (0.99999998) | Extreme intolerance to heterozygous LoF |
| LOEUF (oe_lof_upper) | 0.291 | Strongly constrained (lower = more constrained) |
| Observed/expected pLoF | 0.18 (12 obs vs 66.7 exp) | ~82% depletion of LoF variants |
| LOF Z | 5.68 | Highly significant LoF depletion |
| Missense Z | 3.93 (oe_mis = 0.68) | Additional missense constraint |

A pLI of 1.0 means essentially no healthy individuals in population databases tolerate a *WBP11* LoF allele without consequence — precisely the signature expected for a haploinsufficient developmental gene, and fully concordant with the human and mouse genetics.

### Finding 5 — VCTERL (WBP11) is a Mendelian cause within the broader VACTERL association

The **VACTERL association** is defined clinically by the co-occurrence of **≥3** component features: **V**ertebral anomalies, **A**nal atresia, **C**ardiac malformations, **T**racheo-**E**sophageal fistula ± esophageal atresia, **R**enal anomalies, and **L**imb abnormalities (Solomon et al. 2012). Most VACTERL is **sporadic and multifactorial**, with low familial recurrence (~1%); only ~11–12% of tracheo-esophageal/VACTERL cases have an identifiable genetic cause (Brosens et al. 2014). *WBP11* LoF defines an autosomal-dominant Mendelian subset (VCTERL, OMIM:619227) that can present as the full VACTERL spectrum **or** as an isolated component phenotype — Klippel-Feil syndrome, renal agenesis, or esophageal atresia. Other established Mendelian VATER/VACTERL genes include *FGF8, FOXF1, HOXD13, LPP, TRAP1,* and *ZIC3* (Reutter et al. 2016).

> *"VACTERL association ... is typically defined by the presence of at least three of the following congenital malformations"* — [PMID: 23165726](https://pubmed.ncbi.nlm.nih.gov/23165726/)

> *"At present, a causal genetic aberration can be identified in 11-12% of patients"* — [PMID: 24931924](https://pubmed.ncbi.nlm.nih.gov/24931924/)

> *"LoF WBP11 variants should be considered as a possible cause of VACTERL association as well as isolated Klippel-Feil syndrome, renal agenesis or esophageal atresia"* — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)

### Finding 6 — Prognosis is driven by component-malformation severity, especially cardiac defects

Outcome in VCTERL/VACTERL is dominated by the severity of the individual malformations. In esophageal-atresia (EA) cohorts, mortality is substantially higher when **major congenital heart disease (CHD)** is present — 60% mortality among neonates with major CHD and 40% among those with VACTERL association (Varga et al. 2026) — and EA patients with VACTERL plus chromosomal anomalies form a high-risk subgroup marked by prematurity, major cardiac defects, and increased sepsis risk (Soyer et al. 2026). With successful surgical repair, overall survival is now high, but **long-term morbidity is substantial**: adults born with esophageal atresia suffer dysphagia, gastro-esophageal reflux, esophageal dysmotility, anastomotic stricture, Barrett's esophagus (with associated esophageal cancer risk), chronic respiratory disease, feeding/nutritional problems, and reduced quality of life, requiring lifelong follow-up.

> *"Mortality was 60% among neonates with major congenital heart defects (CHD) and 40% among those with VACTERL association"* — [PMID: 42463002](https://pubmed.ncbi.nlm.nih.gov/42463002/)

> *"Many of the adults born with œsophageal atresia will suffer from dysphagia, gastro-œsophageal reflux and/or œsophageal dysmotility, leading to nutritional consequences and quality of life impairment"* — [PMID: 35331402](https://pubmed.ncbi.nlm.nih.gov/35331402/)

> *"EA patients with VACTERL-CA represent a high-risk subgroup characterized by prematurity, major cardiac defects, and increased sepsis risk"* — [PMID: 40992427](https://pubmed.ncbi.nlm.nih.gov/40992427/)

### Finding 7 — Etiology/environment: broad VACTERL is multifactorial; WBP11-VCTERL is monogenic

Non-syndromic VACTERL is generally considered multifactorial, with contributions from epigenetic and environmental factors; most cases are sporadic (~1% familial recurrence) (Brosens et al. 2014). **Maternal pregestational diabetes** is an established risk factor for VACTERL-type anomalies — e.g., it significantly increased the risk of hearing loss in VACTERL (OR 3.71, 95% CI 1.5–7.3) and in partial VACTERL (OR 6.7, 95% CI 1.70–26) (Galarreta et al. 2023). Analyses of recurrent constellations of embryonic malformations note an excess of monozygotic twins discordant for the phenotype and elevated assisted-reproductive-technology (ART) use (~18.5%), implicating early post-zygotic/epigenetic disruption (Adam et al. 2020). In contrast, **WBP11-related VCTERL is monogenic**: no environmental trigger is required, although the same developmental pathways may be modulated by such factors.

> *"non-syndromic EA/TEF is generally believed to be a multifactorial condition"* — [PMID: 24931924](https://pubmed.ncbi.nlm.nih.gov/24931924/)

> *"Maternal diabetes significantly increased the risk for HL in VACTERL (odds ratio [OR]: 3.71, 95% confidence interval [CI]: 1.5-7.3)"* — [PMID: 37649433](https://pubmed.ncbi.nlm.nih.gov/37649433/)

> *"Statistically significant associations included an excess of monozygotic twins and 80% discordance rate for the phenotype across all twins. There was an 18.5% rate of ART"* — [PMID: 32924308](https://pubmed.ncbi.nlm.nih.gov/32924308/)

### Finding 8 — Proposed mechanism: reduced splicing capacity disrupts developmental gene programs during organogenesis

The inferred causal chain (partly demonstrated, partly inferred) runs from the molecular lesion to the clinical phenotype. WBP11 is proposed to intersect VACTERL developmental pathways; a 2025 review places *WBP11* among genes influencing VACTERL alongside Sonic Hedgehog (SHH)-pathway components (*SHH, GLI, ZIC3, FOXF1, HOXD13, FGF8*). The mouse *Wbp11*-null lethality before E8.5 confirms an essential early-developmental role.

> *"WBP11 encodes a component of the spliceosome with the ability to activate pre-messenger RNA splicing"* — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)

> *"we describe the influence of TRAP1, COL11A2, SALL4, WBP11, Copy Number Variants, and maternal environmental factors on VACTERL"* — [PMID: 40692799](https://pubmed.ncbi.nlm.nih.gov/40692799/)

### Finding 9 — ClinVar documents an established WBP11 gene–disease relationship

NCBI ClinVar (accessed 2026-10) returns ~228 *WBP11* variant records, of which **100 are classified Pathogenic and 18 Likely Pathogenic**. This corroborates *WBP11* as a well-established, actively curated disease gene for VCTERL/VACTERL-spectrum congenital anomalies, complementing the gnomAD constraint and the defining case series. Reported disease alleles are germline LoF (nonsense/frameshift/splice-site) and damaging missense, plus 12p deletions/CNVs encompassing *WBP11*.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous *WBP11* LoF (nonsense/frameshift/splice) or damaging missense variant** (or a 12p12.3–p13.1 deletion encompassing *WBP11*) arises in the germline. *(demonstrated — [PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/), ClinVar)*
2. This **leads to** reduced dosage of the WBP11/SIPP1 spliceosome co-factor — i.e., haploinsufficiency. *(demonstrated: gnomAD pLI = 1.0; SIPP1 is a bona-fide spliceosome component — [PMID: 14640981](https://pubmed.ncbi.nlm.nih.gov/14640981/))*
3. Reduced WBP11 **results in** globally reduced or altered pre-mRNA splicing efficiency / fidelity. *(inferred — splicing-activating function demonstrated in vitro; a genome-wide splicing defect in affected tissue has not been directly measured)*
4. Altered splicing **impairs** the expression of splicing-sensitive developmental regulators and the proliferation of progenitor cells during the first-trimester critical window of organogenesis. *(inferred; intersection with SHH-pathway genes proposed — [PMID: 40692799](https://pubmed.ncbi.nlm.nih.gov/40692799/))*
5. This **causes** failure of mesoderm, foregut, and limb-bud patterning. *(inferred, supported by mouse/zebrafish phenotypes)*
6. The patterning failures **manifest as** vertebral, cardiac, tracheo-esophageal, renal, and limb malformations — the VACTERL/VCTERL spectrum. *(demonstrated in humans and recapitulated in heterozygous Wbp11 mice and wbp11 zebrafish)*

```
WBP11 LoF / damaging missense / 12p deletion
        │ (demonstrated)
        ▼
Reduced WBP11/SIPP1 dosage  ── haploinsufficiency (pLI = 1.0)
        │ (demonstrated: spliceosome component)
        ▼
↓ pre-mRNA splicing capacity / fidelity
        │ (inferred)
        ▼
Dysregulated developmental gene programs ── (proposed SHH-pathway intersection)
        │ (inferred)
        ▼
Failure of mesoderm / foregut / limb-bud patterning
        │ (mouse E8.5 lethality; het defects; zebrafish)
        ▼
   ┌───────────┬───────────┬──────────────┬──────────┬──────────┐
Vertebral   Cardiac   Tracheo-esoph.   Renal      Limb      (+ anal, genital)
 defects    defects     fistula/EA    anomalies  defects
```

### Where the mechanism branches

The disorder's hallmark **variable expressivity and incomplete penetrance** sit at steps 4–6: the same reduction in splicing capacity can disrupt one organ field or several, producing anything from isolated Klippel-Feil syndrome, isolated renal agenesis, or isolated esophageal atresia up to the full ≥3-feature VACTERL phenotype ([PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)). The branch point is stochastic/modifier-dependent rather than deterministic.

### Ontology annotations

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0030987; OMIM:619227 |
| Gene/protein | HGNC:16461 (*WBP11*); UniProt Q9Y2W2; Ensembl ENSG00000084463 |
| Biological process (GO) | GO:0000398 (mRNA splicing, via spliceosome); GO:0008380 (RNA splicing); GO:0048704 (embryonic skeletal system morphogenesis); GO:0072001 (renal system development) |
| Cellular component (GO) | GO:0005681 (spliceosomal complex); GO:0016607 (nuclear speck); GO:0005634 (nucleus) |
| Molecular function (GO) | GO:0003723 (RNA binding); GO:0019903 (protein phosphatase binding) |
| Anatomy (UBERON) | UBERON:0001130 (vertebral column); UBERON:0000948 (heart); UBERON:0003126 (trachea); UBERON:0001043 (esophagus); UBERON:0002113 (kidney); UBERON:0002101 (limb) |
| Phenotype (HPO) | HP:0003468 (vertebral segmentation defect); HP:0001627 (abnormal heart morphology); HP:0002575 (tracheoesophageal fistula); HP:0002040 (esophageal atresia); HP:0000104 (renal agenesis); HP:0002817 (abnormality of the upper limb); HP:0002023 (anal atresia) |
| Chemical (CHEBI) | Not applicable (no causative/therapeutic chemical entity) |

---

## Section-by-Section Report

### 1. Disease Information
VCTERL (Vertebral, Cardiac, Tracheo-esophageal, Renal, and Limb Defects) is an autosomal-dominant multiple-congenital-anomaly syndrome caused by heterozygous *WBP11* variants. **Identifiers:** MONDO:0030987; OMIM:619227; synonyms VCTERL / VCTERL syndrome. It is the Mendelian, *WBP11*-defined subset of the broader VATER/VACTERL association (OMIM #192350). No single ICD-10/ICD-11 or MeSH code is specific to VCTERL; cases are coded by their component malformations or under the VATER-association descriptor (e.g., ICD-10 Q87.2). Information is derived from **aggregated disease-level resources** (case series, OMIM, ClinVar, gnomAD) rather than EHR-level individual records.

### 2. Etiology
**Primary cause:** monogenic — heterozygous *WBP11* LoF or damaging missense variants (haploinsufficiency). **Genetic risk factors:** the causal *WBP11* allele itself; other VATER/VACTERL Mendelian genes (*FGF8, FOXF1, HOXD13, LPP, TRAP1, ZIC3*) cause phenocopies. **Environmental risk factors** (relevant to the broader VACTERL phenotype, not required for WBP11-VCTERL): maternal pregestational diabetes (OR up to ~6.7 for some features), assisted reproduction/twinning. **Protective factors:** none specifically identified; standard periconceptional care and maternal glycemic control reduce general congenital-anomaly risk. **Gene–environment interactions:** proposed modulation of shared developmental pathways (e.g., SHH signaling) by the maternal metabolic environment, but not demonstrated for *WBP11* specifically.

### 3. Phenotypes
Core phenotypes are structural congenital malformations present at birth (**congenital onset; variable, often severe; stable structurally once repaired**). Frequencies below reflect broader VACTERL ascertainment and *WBP11* case reports.

| Phenotype | HPO term | Type | Notes |
|---|---|---|---|
| Vertebral anomalies (incl. Klippel-Feil) | HP:0003468 / HP:0003027 | Physical/radiologic | Can be isolated in WBP11 |
| Cardiac malformation | HP:0001627 | Physical sign | Dominant prognostic driver |
| Tracheo-esophageal fistula ± esophageal atresia | HP:0002575 / HP:0002040 | Physical sign | Major long-term morbidity |
| Renal anomalies (incl. agenesis) | HP:0000104 / HP:0000077 | Physical/imaging | Most common VACTERL CF overall |
| Limb defects (radial/thumb) | HP:0002817 / HP:0009777 | Physical sign | |
| Anal atresia | HP:0002023 | Physical sign | Variable |
| Genital anomalies | HP:0000078 | Physical sign | ~34% in VACTERL cohorts |

**Quality-of-life impact** is dominated by the esophageal/GI component (dysphagia, reflux, feeding difficulty) and by cardiac/renal severity; adults report measurable reductions on GIQLI/GSRS instruments.

### 4. Genetic/Molecular Information
**Causal gene:** *WBP11* (HGNC:16461; chr12p12.3–p13.1; ENSG00000084463; UniProt Q9Y2W2). **Variant classes:** germline nonsense, frameshift, canonical splice-site, and predicted-damaging missense variants; also 12p deletions/CNVs encompassing *WBP11*. **Classification:** ClinVar lists ~100 Pathogenic and 18 Likely Pathogenic records (ACMG/AMP). **Allele frequency:** extreme LoF depletion in gnomAD (12 observed vs 66.7 expected pLoF; pLI = 1.0; LOEUF 0.29). **Origin:** germline (de novo or inherited). **Functional consequence:** loss of function → haploinsufficiency. **Modifier genes/epigenetics:** not specifically characterized for *WBP11*; variable expressivity suggests unidentified modifiers/stochastic effects.

### 5. Environmental Information
No environmental agent is required to cause WBP11-VCTERL (monogenic). For the overlapping multifactorial VACTERL phenotype, maternal pregestational diabetes is the best-established environmental/metabolic risk factor; ART/twinning associations implicate early post-zygotic events. No infectious agent is implicated.

### 6. Mechanism / Pathophysiology
See the **Mechanistic Model** above for the ordered causal chain. In brief: *WBP11* LoF → reduced WBP11/SIPP1 spliceosome co-factor dosage → impaired pre-mRNA splicing (spliceosomopathy) → dysregulated developmental gene programs (proposed SHH-pathway intersection) → failed mesoderm/foregut/limb-bud patterning → multi-organ malformation. **Cellular processes:** progenitor proliferation/patterning during organogenesis. **Protein dysfunction:** loss of a nuclear-speckle splicing-activating factor; PP1 and PQBP-1/Npw38 interactions. **Upstream vs downstream:** the splicing deficit is upstream; organ-specific morphogenetic failure is downstream.

### 7. Anatomical Structures Affected
**Primary organs:** vertebral column/axial skeleton (UBERON:0001130), heart (UBERON:0000948), trachea (UBERON:0003126) and esophagus (UBERON:0001043), kidney (UBERON:0002113), limbs (UBERON:0002101); also anus/hindgut and genitalia. **Body systems:** skeletal, cardiovascular, respiratory, digestive, genitourinary. **Subcellular:** nucleus / nuclear speckle / spliceosomal complex (GO:0016607, GO:0005681). **Lateralization:** malformations may be unilateral, bilateral, or asymmetric depending on organ.

### 8. Temporal Development
**Onset:** congenital (prenatal organogenesis, first-trimester critical window). **Detection:** prenatal ultrasound detects renal (~45%), TEF (~44%), cardiac (~20%), vertebral (~13%), limb (~11%) features; anal atresia is typically not seen prenatally. **Course:** structural defects are static once repaired, but the esophageal component produces chronic, lifelong GI/respiratory morbidity. **Critical period for intervention:** neonatal surgical correction of life-threatening anomalies (EA/TEF, cardiac, anal atresia).

### 9. Inheritance and Population
**Inheritance:** autosomal dominant, haploinsufficiency; de novo or inherited. **Penetrance:** incomplete. **Expressivity:** highly variable (isolated single-organ to full VACTERL spectrum). **Epidemiology:** VCTERL itself is ultra-rare (seven founding families; a few dozen ClinVar families); the broader VACTERL association occurs in ~1 in 10,000–40,000 births, of which only ~11–12% have an identifiable genetic cause, and *WBP11* is one minority Mendelian contributor. No founder effect, anticipation, or strong sex bias is established for *WBP11*.

### 10. Diagnostics
**Clinical:** recognition of ≥3 VACTERL component features; imaging (echocardiography, renal ultrasound, spinal/limb radiographs, contrast studies for EA/TEF). **Genetic testing:** exome/genome sequencing or multigene congenital-anomaly panels including *WBP11*; chromosomal microarray to detect 12p deletions/CNVs; single-gene *WBP11* testing when the phenotype is suggestive. **Differential diagnosis:** VACTERL of other genetic cause (*FGF8, FOXF1, HOXD13, LPP, TRAP1, ZIC3*), Fanconi anemia (VACTERL-H — screen when radial/renal defects co-occur; worse prognosis, cancer risk), CHARGE syndrome, Feingold syndrome, trisomy 18/21.

### 11. Outcome/Prognosis
Survival is now high after surgical repair but is dominated by **cardiac-defect severity** (up to 60% neonatal mortality with major CHD in EA cohorts; VACTERL + chromosomal anomalies = high-risk subgroup). **Long-term morbidity** (esophageal component): dysphagia, GERD, dysmotility, anastomotic stricture, Barrett's esophagus/cancer risk, chronic respiratory disease, feeding/growth problems, and reduced quality of life. Lifelong multidisciplinary surveillance is mandated.

### 12. Treatment
There is **no disease-specific or gene-directed therapy**. Management is **organ-directed surgical correction** (neonatal repair of EA/TEF, cardiac surgery, anorectal/limb/renal procedures) plus **supportive and rehabilitative care** (nutrition/feeding therapy, anti-reflux management, pulmonary care, physical/occupational/speech therapy). Treatment is individualized by component-malformation profile. NCIT suggestions apply to specific interventions (surgical repair, supportive care) rather than a syndrome-specific agent.

### 13. Prevention
**Primary prevention:** not possible for a de novo monogenic disorder; for the broader phenotype, maternal glycemic control and periconceptional care reduce risk. **Secondary prevention:** prenatal ultrasound detection enables delivery planning at a surgical center. **Genetic counseling:** autosomal-dominant recurrence counseling (50% transmission risk from an affected heterozygous parent, with incomplete penetrance/variable expressivity); prenatal/preimplantation genetic testing possible once a familial *WBP11* variant is known. **Cascade testing** of at-risk relatives is appropriate.

### 14. Other Species / Natural Disease
No naturally occurring companion-animal or wildlife VCTERL disease is documented. The gene is evolutionarily conserved; mouse *Wbp11* (essential; E8.5 lethal when null) and zebrafish *wbp11* are orthologs used experimentally. No zoonotic/transmission relevance.

### 15. Model Organisms
**Mouse:** CRISPR-Cas9 *Wbp11* null — homozygous lethal before E8.5; heterozygotes small with axial-skeleton, kidney, and esophageal defects (strong recapitulation of the human disorder) ([PMID: 33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/)). **Zebrafish:** *wbp11* loss-of-function model with multi-system developmental defects modeling VACTERL ([PMID: 42625817](https://pubmed.ncbi.nlm.nih.gov/42625817/)). **In vitro:** biochemical characterization of SIPP1/WBP11 as a spliceosome component and PP1/PQBP-1 interactor ([PMID: 14640981](https://pubmed.ncbi.nlm.nih.gov/14640981/)). **Limitations:** models capture structural malformation but not the full human variable expressivity; genome-wide splicing consequences in affected human tissues remain to be mapped.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in report |
|---|---|---|---|
| [33276377](https://pubmed.ncbi.nlm.nih.gov/33276377/) | *Heterozygous loss of WBP11 function causes multiple congenital defects in humans and mice* | Human clinical + mouse | **Defining paper**: gene–disease relationship, variants, mouse model, splicing function, expressivity |
| [14640981](https://pubmed.ncbi.nlm.nih.gov/14640981/) | *SIPP1, a novel pre-mRNA splicing factor and interactor of PP1* | In vitro/biochemical | Establishes WBP11/SIPP1 molecular function (spliceosome, PP1, PQBP-1) |
| [42625817](https://pubmed.ncbi.nlm.nih.gov/42625817/) | *Loss of wbp11 ... zebrafish model of VACTERL* | Model organism | Cross-species confirmation of multi-system phenotype |
| [40692799](https://pubmed.ncbi.nlm.nih.gov/40692799/) | *Molecular mechanism, diagnosis, and treatment of VACTERL* | Review | Places WBP11 in VACTERL developmental-pathway context |
| [23165726](https://pubmed.ncbi.nlm.nih.gov/23165726/) | *Clinical geneticists' views of VACTERL/VATER* | Clinical consensus | Diagnostic definition (≥3 features) |
| [24931924](https://pubmed.ncbi.nlm.nih.gov/24931924/) | *Clinical and etiological heterogeneity in tracheo-esophageal malformations* | Review/cohort | Multifactorial etiology; ~11–12% genetic yield |
| [26857713](https://pubmed.ncbi.nlm.nih.gov/26857713/) | *Underlying genetic factors of VATER/VACTERL ... "Renal" phenotype* | Review | Other Mendelian VACTERL genes |
| [42463002](https://pubmed.ncbi.nlm.nih.gov/42463002/) | *Surgical management of EA/TEF in ELBW neonates* | Systematic review | Mortality driven by cardiac/VACTERL severity |
| [40992427](https://pubmed.ncbi.nlm.nih.gov/40992427/) | *Impact of VACTERL and chromosomal anomalies after EA repair (EUPSA)* | Registry | VACTERL high-risk subgroup |
| [35331402](https://pubmed.ncbi.nlm.nih.gov/35331402/) | *Long-term digestive outcome of esophageal atresia* | Clinical review | Long-term GI morbidity/QoL |
| [37649433](https://pubmed.ncbi.nlm.nih.gov/37649433/) | *Ear anomalies/hearing loss in VACTERL and maternal diabetes* | Clinical cohort | Maternal diabetes risk (OR 3.71) |
| [32924308](https://pubmed.ncbi.nlm.nih.gov/32924308/) | *Recurrent constellations of embryonic malformations re-conceptualized* | Epidemiology | Twinning/ART, early developmental disruption |
| [31519362](https://pubmed.ncbi.nlm.nih.gov/31519362/) | *Outcomes in adulthood of gastric transposition for EA* | Clinical cohort | Adult morbidity/QoL data |
| [39998690](https://pubmed.ncbi.nlm.nih.gov/39998690/) | *Long-term GI complications in pediatric EA/TEF* | Clinical review | GI surveillance/management |

All nine confirmed findings rest on verified abstract quotes. The gene–disease relationship (Findings 1–4, 9) is strongly supported by convergent human genetics, mouse and zebrafish models, population constraint, and ClinVar curation. Prognostic and etiologic findings (6–7) derive largely from the broader VACTERL literature and are applied to WBP11-VCTERL by its membership in that spectrum.

---

## Limitations and Knowledge Gaps

- **Small human cohort.** The founding series is seven families; genotype–phenotype correlation, precise penetrance, and sex ratio for *WBP11* specifically are not robustly quantified.
- **Splicing defect is inferred, not measured in patient tissue.** Step 3 of the causal chain (globally altered pre-mRNA splicing) is biochemically plausible (demonstrated splicing-activating function) but has not been directly demonstrated in affected human organs; which specific mis-spliced transcripts drive each malformation is unknown.
- **SHH-pathway intersection is proposed, not proven** for *WBP11*.
- **Modifiers of expressivity unidentified.** The mechanism branching that yields isolated vs full-spectrum phenotypes is not explained.
- **Prognostic data are extrapolated** from the broader VACTERL/EA literature, not from WBP11-genotyped patients.
- **No WBP11-specific epidemiology, QoL instruments, or natural-history study** exists.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-tissue splicing analysis.** RNA-seq of *WBP11*-haploinsufficient patient-derived cells/organoids (and heterozygous mouse/zebrafish tissues) to identify the mis-spliced developmental transcripts linking the splicing deficit to each organ defect — directly testing inferred step 3.
2. **Mechanistic linkage to SHH/morphogen pathways.** Test whether WBP11 reduction alters splicing/expression of SHH-pathway components (*SHH, GLI, ZIC3, FOXF1, HOXD13, FGF8*) during organogenesis.
3. **Conditional / tissue-specific mouse models.** Organ-restricted *Wbp11* heterozygosity to dissect cardiac vs renal vs esophageal contributions and to model variable expressivity.
4. **Genotype–phenotype and penetrance study.** Aggregate ClinVar/GeneMatcher/registry cases to quantify penetrance, expressivity, and sex ratio for *WBP11* variants, and to test LoF-vs-missense severity differences.
5. **Modifier screens.** Variable-expressivity CRISPR/zebrafish modifier screens to identify genetic/environmental modulators of the branch point.
6. **Clinical surveillance protocol.** Define a WBP11-VCTERL-specific multidisciplinary follow-up pathway (cardiac, renal, esophageal/GI, skeletal) and prospective QoL capture (EQ-5D, GIQLI).

---

*Report compiled from 9 confirmed findings and 29 reviewed papers across 5 iterations. Evidence types: human clinical (defining case series, cohorts, registries), model organism (mouse, zebrafish), in vitro/biochemical (SIPP1 characterization), and computational/population genetics (gnomAD constraint, ClinVar).*


## Artifacts

- [OpenScientist final report](Vertebral_Cardiac_Tracheoesophageal_Renal_And_Limb_Defects-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Vertebral_Cardiac_Tracheoesophageal_Renal_And_Limb_Defects-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001627` (2 mentions) - the report calls it "Cardiac malformation"; HP calls it **Abnormal heart morphology**, and lists "Cardiac abnormality" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

27 of 29 terms resolved to a current term; the rest could not be looked up either way.