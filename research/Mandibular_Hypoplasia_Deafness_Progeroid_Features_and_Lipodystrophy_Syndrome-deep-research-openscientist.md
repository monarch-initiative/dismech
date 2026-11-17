---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-13T04:10:38.069282'
end_time: '2026-11-13T04:56:51.367772'
duration_seconds: 2773.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Mandibular Hypoplasia, Deafness, Progeroid Features, and Lipodystrophy
    Syndrome
  mondo_id: MONDO:0014157
  category: Mendelian
  causal_genes: POLD1
  omim_id: OMIM:615381
  synonyms: MDP syndrome; mandibular hypoplasia-hearing loss-progeroid syndrome
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
  job_id: bac38d86-d33c-482c-9679-debe297100fc
citation_count: 15
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 17
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41742372
  relevance_assessed: 17
  on_topic: 15
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 37
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_variant: 5
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
  path: Mandibular_Hypoplasia_Deafness_Progeroid_Features_and_Lipodystrophy_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Mandibular_Hypoplasia_Deafness_Progeroid_Features_and_Lipodystrophy_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mandibular Hypoplasia, Deafness, Progeroid Features, and Lipodystrophy Syndrome
- **MONDO ID:** MONDO:0014157 (if available)
- **Causal gene(s):** POLD1
- **OMIM:** OMIM:615381
- **Synonyms:** MDP syndrome; mandibular hypoplasia-hearing loss-progeroid syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Mandibular Hypoplasia, Deafness, Progeroid Features, and Lipodystrophy Syndrome** covering all of the
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

# Mandibular Hypoplasia, Deafness, Progeroid Features, and Lipodystrophy (MDPL/MDP) Syndrome — Comprehensive Disease Report

**Disease:** Mandibular Hypoplasia, Deafness, Progeroid Features, and Lipodystrophy Syndrome (MDPL/MDP syndrome)
**Causal gene:** **POLD1** (DNA polymerase delta 1, catalytic subunit; p125; HGNC:9175; MIM 174761; 19q13.33)
**MONDO:** MONDO:0014157 · **OMIM:** #615381 · **Orphanet:** ORPHA:280356

---

## Summary

Mandibular Hypoplasia, Deafness, Progeroid features, and Lipodystrophy (MDPL/MDP) syndrome is an ultra‑rare, autosomal dominant **segmental progeroid disorder** caused by heterozygous, almost always *de novo*, pathogenic variants in **POLD1**, the gene encoding the large catalytic p125 subunit of DNA polymerase delta (Pol δ). The single most common cause is the recurrent in‑frame deletion of a single codon at the polymerase active site, **p.Ser605del** (also written p.Ser604del depending on isoform numbering), which abolishes DNA polymerase activity while sparing the 3′→5′ exonuclease (proofreading) function. This mechanistic polarity is the defining feature of POLD1 biology: **polymerase‑domain variants cause the MDPL progeroid/lipodystrophy phenotype, whereas exonuclease‑domain variants cause a cancer‑predisposition syndrome** (colorectal and endometrial cancer) with no progeroid features. Naming the gene explicitly as required: *the causal gene of MDPL is POLD1.*

The core clinical picture is a tetrad of **mandibular hypoplasia, bilateral sensorineural hearing loss (SNHL), progressive partial lipodystrophy, and progeroid facial features**, accompanied by metabolic complications of the lipodystrophy (insulin‑resistant diabetes, severe hypertriglyceridemia with pancreatitis risk, hepatic steatosis) and, particularly in males, hypogonadism. The genotype shapes severity: carriers of the recurrent p.Ser605del allele have significantly more mandibular/oral and male‑gonadal involvement than missense carriers, while some missense and iron–sulfur‑cluster (CysB) variants produce milder or atypical presentations. Mechanistically, loss of Pol δ polymerase activity leads to replication stress and impaired DNA repair, which — together with nuclear‑envelope anomalies, prelamin A accumulation, micronuclei, and aberrant telomeric (TRF1) engagement — drives premature cellular senescence and tissue‑specific failure, most conspicuously of adipose tissue.

There is **no disease‑specific or curative therapy**; management is multidisciplinary and supportive, borrowing from lipodystrophy care (metreleptin, insulin sensitizers, lipid‑lowering agents; emerging incretin agonists), plus hearing rehabilitation, sex‑hormone replacement, orthodontic/maxillofacial management, and careful anesthetic planning. MDPL is ultra‑rare (Orphanet prevalence <1/1,000,000), with only a few dozen genetically confirmed cases, no established sex or ethnic predilection, and no role for population screening because variants are overwhelmingly *de novo*.

---

## Key Findings

### 1. POLD1 heterozygous variants — dominated by the polymerase‑active‑site p.Ser605del — cause MDPL (F001)

The founding study established the molecular cause. Weedon and colleagues (2013) identified a recurring heterozygous single‑codon deletion in *POLD1* affecting the polymerase active site in patients with a multisystem disorder comprising subcutaneous lipodystrophy, deafness, mandibular hypoplasia, and male hypogonadism. The deletion **abolishes DNA polymerase activity but only mildly impairs 3′→5′ exonuclease activity**. Inheritance is autosomal dominant and usually *de novo*; the disorder is catalogued as OMIM #615381, with *POLD1* mapping to 19q13.33 (MIM 174761).

> "Here we report a recurring heterozygous single-codon deletion in POLD1 affecting the polymerase active site that abolishes DNA polymerase activity but only mildly impairs 3'- to 5'-exonuclease activity. This mutation causes a distinct multisystem disorder that includes subcutaneous lipodystrophy, deafness, mandibular hypoplasia and hypogonadism in males." — [PMID: 23770608](https://pubmed.ncbi.nlm.nih.gov/23770608/)

### 2. Domain‑dependent dichotomy: polymerase‑domain → MDPL; exonuclease‑domain → cancer (F002)

POLD1 disease is strikingly partitioned by *where* in the protein the variant falls. Damaging variants within the **exonuclease (proofreading) domain** predispose to cancers, whereas variants at the **polymerase active site** cause the autosomal dominant progeroid syndrome MDPL (Murdocca et al., 2023). The magnitude of the cancer risk for exonuclease‑domain carriers is large: Dominguez‑Valentin/Buchanan et al. (2018) estimated colorectal cancer risk at approximately **82–90% by age 70** for POLD1 proofreading‑variant carriers. A nuance exists — some MDPL patients carry exonuclease‑domain variants (e.g., R507C; Pelosini et al., 2014) — indicating partial genotype–phenotype overlap, but the dominant pattern holds.

> "Damaging variants within the exonuclease domain predispose to cancers, while those occurring in the polymerase active site cause the autosomal dominant Progeroid Syndrome called MDPL…" — [PMID: 36764464](https://pubmed.ncbi.nlm.nih.gov/36764464/)

> "90% (95% CI, 33–99%) and 82% (95% CI, 26–99%) for POLD1 mutation carriers" — [PMID: 29120461](https://pubmed.ncbi.nlm.nih.gov/29120461/)

### 3. Genotype–phenotype correlation within MDPL (F003)

Even among MDPL‑causing variants, genotype predicts severity. Hoff et al. (2026), combining 14 new patients with the literature, compared **p.Ser605del carriers (n=26)** against **missense‑variant carriers (n=15)** and found the deletion carriers had significantly higher prevalence of several craniofacial and gonadal features:

| Feature | Missense carriers | p.Ser605del carriers | P value |
|---|---|---|---|
| Mandibular hypoplasia | 57% | 100% | 0.015 |
| Small mouth | 36% | 100% | 0.015 |
| Crowded teeth | 44% | 91% | 0.046 |
| Male hypogonadism | 0% | 92% | 0.046 |
| Metabolic complications | (no significant difference) | | n.s. |

Consistent with variable expressivity, Lessel et al. (2015) described POLD1 carriers **without** clinically relevant hearing impairment or mandibular underdevelopment — previously thought to be obligate diagnostic features — along with a lower incidence of metabolic abnormalities and joint contractures, plus postnatal short stature and premature greying/hair loss.

> "those with the p.Ser605del (n = 26) POLD1 variant had significantly increased prevalence of mandibular hypoplasia (57% vs 100%…; P = .015), small mouth (36% vs 100%…; P = .015), crowded teeth (44% vs 91%…; P = .046), and hypogonadism in male patients (0% vs 92%…; P = .046)" — [PMID: 41742372](https://pubmed.ncbi.nlm.nih.gov/41742372/)

> "we describe POLD1 mutation carriers without clinically relevant hearing impairment or mandibular underdevelopment, both previously thought to represent obligate diagnostic features. These patients also exhibit a lower incidence of metabolic abnormalities and joint contractures" — [PMID: 26172944](https://pubmed.ncbi.nlm.nih.gov/26172944/)

### 4. Mouse proofreading‑deficient models inform POLD1 biology and separate cancer from aging (F004)

Goldsby et al. (2002) engineered *Pold1* D400A mice that inactivate the 3′→5′ exonuclease. **Homozygotes developed a recessive mutator and cancer phenotype** — 94% developed cancer and died by 18 months (median survival ~10 months; squamous cell skin carcinoma most common) — while heterozygotes were largely unaffected (cancer rates like wild type). Later work (Andrianova et al., 2024) showed exonuclease deficiency acts recessively on the mutation rate, with tumorigenesis requiring somatic inactivation of the wild‑type allele. Critically, Robinson et al. (2021) noted that germline POLE/POLD1 proofreading‑variant carriers do **not** exhibit overt premature aging — reinforcing that the progeroid MDPL phenotype is specific to **polymerase‑domain** (not exonuclease‑domain) dysfunction.

> "this mutation inactivates the 3' --> 5' exonuclease of poldelta and causes a mutator and cancer phenotype in a recessive manner. By 18 months of age, 94% of homozygous Pold1(D400A/D400A) mice developed cancer and died" — [PMID: 12429860](https://pubmed.ncbi.nlm.nih.gov/12429860/)

> "Except for increased cancer risk, individuals with germline POLE/POLD1 mutations do not exhibit overt features of premature aging" — [PMID: 34594041](https://pubmed.ncbi.nlm.nih.gov/34594041/)

### 5. Cellular mechanism of p.Ser605del: nuclear‑envelope anomalies, prelamin A, senescence, persistent DNA damage (F005)

Patient‑derived cells localize the pathology. Fiorillo et al. (2018) studied dermal fibroblasts from a p.Ser605del MDPL patient and observed **severe nuclear envelope anomalies, micronuclei, accumulation of prelamin A, altered cell growth, and cellular senescence**, plus persistence of DNA damage after cisplatin exposure relative to controls. Murdocca et al. (2025) used molecular dynamics to show Ser605del affects the DNA‑binding site and impairs dTTP binding, and alters short linear motifs so the protein acquires an aberrant interaction with the telomeric protein **TRF1** (confirmed by immunoprecipitation), with altered POLD1/TRF1/PARP1 expression in patient fibroblasts. A companion transcriptomic study found differentially expressed transcripts related to connective‑tissue extracellular matrix and a blunted induction of DNA replication/repair genes after X‑irradiation.

> "In patient's fibroblasts we observed severe nuclear envelope anomalies, presence of micronuclei, accumulation of prelamin A, altered cell growth, and cellular senescence. In addition, we observed a persistence of DNA damage after cisplatin exposure, compared to control cells." — [PMID: 30388038](https://pubmed.ncbi.nlm.nih.gov/30388038/)

> "we found that Ser605del affects the DNA-binding site, impairing dTTP binding. The deletion alters short linear motifs involved in protein-protein interactions (PPIs), allowing the acquisition of a F/Y-X-L-X-P (FSLYP) consensus sequence with TRF1, a telomeric…" — [PMID: 41219970](https://pubmed.ncbi.nlm.nih.gov/41219970/)

### 6. Core phenotype tetrad and metabolic complications (F006)

Zuo et al. (2022) summarized that the most frequent MDPL features are **mandibular hypoplasia, characteristic facial appearance, lipodystrophy, and SNHL**. Metabolic complications follow from the lipodystrophy: Dhaliwal et al. (2022) reported **hypertriglyceridemia‑induced pancreatitis with triglycerides in the 3000s mg/dL**; Fiorillo et al. (2018) documented growth retardation, sensorineural deafness, altered subcutaneous fat distribution, and insulin resistance; Sreekumar et al. (2025) reported MDPL presenting with delayed puberty and young‑onset diabetes. Additional reported features include scleroderma‑like skin atrophy and difficult airway, telangiectasias, soft‑tissue calcification, refractory skin ulceration, diabetic retinopathy/eye complaints, and crowded teeth with multiple caries. Importantly, MDPL is distinguished from Werner syndrome by **earlier onset, preserved scalp hair, prominent telangiectasias, SNHL, absence of cataracts, and the lack of a recognized predisposition to malignancy**.

> "the most frequent features included mandibular hypoplasia, characteristic facial appearance, lipodystrophy, and SNHL" — [PMID: 36280868](https://pubmed.ncbi.nlm.nih.gov/36280868/)

> "presented with hypertriglyceridemia induced pancreatitis with triglycerides in the 3000s" — [PMID: 35356184](https://pubmed.ncbi.nlm.nih.gov/35356184/)

> "it can be distinguished by its earlier onset, preserved scalp hair, prominent telangiectasias, sensorineural hearing loss, an absence of cataracts, and a lack of a recognized predisposition to malignancy" — [PMID: 42888013](https://pubmed.ncbi.nlm.nih.gov/42888013/)

**Suggested HPO terms:** Mandibular hypoplasia (HP:0000347), Sensorineural hearing impairment (HP:0000407), Lipodystrophy (HP:0009125)/Lipoatrophy (HP:0100578), Progeroid facial appearance (HP:0005328), Insulin‑resistant diabetes mellitus (HP:0000831), Hypertriglyceridemia (HP:0002155), Hepatic steatosis (HP:0001397), Hypogonadism (HP:0000135), Crowded teeth (HP:0000678), Telangiectasia of the skin (HP:0100585), Short stature (HP:0004322).

### 7. Variant spectrum: recurrent deletion dominates; CysB/4Fe‑4S‑cluster variants modulate severity (F007)

Chopra et al. (2022) noted the recurrent in‑frame serine deletion (p.Ser604del/p.Ser605del) accounts for **18 of 21 reported cases**. Variants in the C‑terminal **CysB motif**, which binds a 4Fe‑4S iron–sulfur cluster, modulate severity: c.3209T>A p.Ile1070Asn produces an unusually severe phenotype, whereas c.3219G>C p.Ser1073Arg produces a milder phenotype (hypothesized to reduce Fe‑S cluster binding without major structural disruption). Other MDPL‑associated variants include exonuclease‑domain R507C and R507H, polymerase‑domain Q1062R (c.3185A>G), W781C, and a frameshift p.Asp25Glufs*16. Variants are almost always *de novo*.

> "most commonly a recurrent in-frame deletion of serine at position 604, accounting for 18 of the 21 reported cases of this condition" — [PMID: 35590056](https://pubmed.ncbi.nlm.nih.gov/35590056/)

> "c.3209 T > A, (p.(Ile1070Asn)) variant in the highly conserved CysB motif in the C-terminal of the POLD1 protein. This region has recently been shown to bind an iron-sulphur cluster of the 4Fe-4S type" — [PMID: 35590056](https://pubmed.ncbi.nlm.nih.gov/35590056/)

### 8. No MDPL‑specific therapy; supportive, lipodystrophy‑based management (F008)

No curative or disease‑modifying therapy targets the POLD1 defect. Care is multidisciplinary and symptom‑directed. For the metabolic/lipodystrophy component, a systematic review of monogenic insulin resistance (Melvin/Semple et al., 2023) found metreleptin lowered triglycerides and HbA1c across lipodystrophy subgroups, and thiazolidinediones improved HbA1c and triglycerides — though evidence is low/very low quality. Metreleptin (recombinant leptin) is approved for generalized lipodystrophy but **not** partial lipodystrophy; GLP‑1/GIP incretin agonists are emerging options for partial forms. MDPL‑directed care also includes hearing aids/cochlear implants for SNHL, sex‑hormone replacement for hypogonadism, orthodontic/maxillofacial management, and careful anesthetic planning for difficult airway and scleroderma‑like skin.

> "Metreleptin use is associated with the lowering of triglycerides and haemoglobin A1c (HbA1c) in all lipodystrophy (n = 111), partial (n = 71) and generalised lipodystrophy (n = 41)" — [PMID: 37794082](https://pubmed.ncbi.nlm.nih.gov/37794082/)

> "MDPL syndrome requires careful preoperative assessment and tailored anesthetic management due to potential airway challenges arising from its distinctive facial features and the possibility of altered anesthetic pharmacokinetics associated with lipodystrophy" — [PMID: 39388000](https://pubmed.ncbi.nlm.nih.gov/39388000/)

**Suggested NCIT terms:** Leptin/Metreleptin therapy, Insulin sensitizing agent (thiazolidinedione), Lipid‑lowering agent (fibrate), Hormone replacement therapy, Hearing aid/Cochlear implant, Orthodontic management.

### 9. Ultra‑rare, autosomal dominant, overwhelmingly *de novo* (F009)

MDPL is repeatedly described as "extremely rare," with only a few dozen genetically confirmed cases worldwide (18 of 21 reported cases carried the recurrent deletion at the time of Chopra et al. 2022; Hoff et al. 2026 added 14 patients). Inheritance is autosomal dominant with pathogenic POLD1 variants almost always *de novo*, so most probands lack affected parents. Cases span diverse populations (European, Japanese, Chinese, Pakistani, Indian). Lessel et al. (2015) argued the syndrome is "probably underdiagnosed." No reliable population prevalence/incidence exists; Orphanet lists ORPHA:280356 with prevalence <1/1,000,000. There is no formal newborn/carrier screening because variants are overwhelmingly *de novo*.

> "POLD1 germline mutations can result in a variably expressed and probably underdiagnosed segmental progeroid syndrome" — [PMID: 26172944](https://pubmed.ncbi.nlm.nih.gov/26172944/)

### 10. Integrated pathophysiology (F010)

The upstream lesion is a heterozygous POLD1 polymerase‑domain variant (p.Ser605del) that abolishes Pol δ 5′→3′ polymerase activity (Weedon 2013). Midstream, in patient cells, this impairs dTTP binding and creates aberrant TRF1/telomere engagement (Murdocca 2025), produces nuclear‑envelope anomalies, prelamin A accumulation, micronuclei, persistent DNA damage, and cellular senescence in fibroblasts (Fiorillo 2018) and early pathology in mesenchymal stem cells (Paola 2024), and dysregulates ECM/connective‑tissue and DNA replication–repair transcripts (Murdocca 2025). Downstream, the clinical phenotype branches: adipose failure → partial lipodystrophy → leptin deficiency/ectopic lipid → insulin‑resistant diabetes, hypertriglyceridemia, hepatic steatosis; plus mandibular hypoplasia, bilateral SNHL, progeroid skin, and male hypogonadism. As Weedon (2013) emphasized, perturbing the ubiquitous POLD1 polymerase has unexpectedly tissue‑specific effects, pointing to a particular role in adipose homeostasis.

> "perturbing the function of the ubiquitously expressed POLD1 polymerase has unexpectedly tissue-specific effects in humans and argues for an important role for POLD1 function in adipose tissue homeostasis" — [PMID: 23770608](https://pubmed.ncbi.nlm.nih.gov/23770608/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **POLD1 polymerase‑domain variant** (most commonly the in‑frame **p.Ser605del**) arises *de novo* in the germline. **→ leads to**
2. **Loss of Pol δ 5′→3′ polymerase catalytic activity** while 3′→5′ exonuclease activity is largely preserved (demonstrated biochemically; Weedon 2013). **→ results in**
3. At the molecular level, **impaired dTTP binding at the DNA‑binding site** and altered short linear motifs that generate an **aberrant interaction with the telomeric protein TRF1** (molecular dynamics + co‑IP; Murdocca 2025). **→ leads to**
4. **Replication stress and impaired DNA repair** (reduced induction of replication/repair genes after irradiation; persistent DNA damage after genotoxic exposure; Murdocca 2025, Fiorillo 2018). **→ results in**
5. **Nuclear‑envelope anomalies, prelamin A accumulation, and micronucleus formation** in patient fibroblasts (Fiorillo 2018) — a convergence point with laminopathy/progeroid biology (inferred link to lamin‑mediated mechanics). **→ drives**
6. **Premature cellular senescence** and altered growth, with early pathological signs detectable even in mesenchymal stem cells (Paola 2024). **→ produces**
7. **Tissue‑specific failure.** The chain then **branches**:
   - **Adipose branch:** progressive **partial lipodystrophy → leptin deficiency / ectopic lipid deposition → insulin‑resistant diabetes, hypertriglyceridemia (± pancreatitis), hepatic steatosis**.
   - **Craniofacial/skeletal branch:** **mandibular hypoplasia, small mouth, crowded teeth, progeroid facies**.
   - **Otologic branch:** **bilateral sensorineural hearing loss**.
   - **Integumentary branch:** **progeroid/atrophic (scleroderma‑like) skin, telangiectasias**.
   - **Gonadal branch:** **male hypogonadism** (strongly associated with p.Ser605del).

Steps 1–3 are directly demonstrated; the step 5→6 convergence with lamin biology is partly inferred; the tissue specificity (step 7), especially adipose vulnerability, remains mechanistically unexplained and is the key open question.

### Domain‑to‑disease map

```
                 POLD1 (p125 catalytic subunit of Pol δ)
                 ┌──────────────────────────────────────────┐
  Exonuclease ───┤ 3'→5' proofreading domain                │──► germline variants (codons ~474-507)
  domain         │   (e.g., L474P, L474I, L486N, V474I)     │     → MUTATOR / CANCER predisposition
                 │                                          │       (CRC ~82-90% by 70; endometrial)
                 ├──────────────────────────────────────────┤
  Polymerase ────┤ 5'→3' polymerase active site             │──► p.Ser605del (recurrent), Q1062R, W781C
  domain         │   (DNA-binding / catalytic)              │     → MDPL progeroid/lipodystrophy
                 ├──────────────────────────────────────────┤
  CysB / 4Fe-4S ─┤ C-terminal iron-sulfur cluster motif     │──► I1070N (severe) / S1073R (mild)
                 └──────────────────────────────────────────┘     → MDPL severity modulation
```

### GO / CL / UBERON / CHEBI suggestions

- **GO biological process:** DNA replication (GO:0006260), lagging strand elongation (GO:0006273), DNA repair (GO:0006281), mismatch repair (GO:0006298), replicative senescence (GO:0090399), telomere maintenance (GO:0000723).
- **GO cellular component:** delta DNA polymerase complex (GO:0043625), nucleus (GO:0005634), nuclear envelope (GO:0005635), nuclear lamina (GO:0005652).
- **CL cell types:** adipocyte (CL:0000136), mesenchymal stem cell (CL:0000134), fibroblast (CL:0000057), dermal fibroblast (CL:0002620).
- **UBERON anatomy:** mandible (UBERON:0001684), subcutaneous adipose tissue (UBERON:0002190), inner ear/cochlea (UBERON:0001844), skin (UBERON:0002097), liver (UBERON:0002107), testis (UBERON:0000473).
- **CHEBI:** triglyceride (CHEBI:17855), insulin (CHEBI:5931), leptin (protein).

---

## Section-by-Section Content

### 1. Disease Information
MDPL is a multisystem **segmental progeroid syndrome** combining mandibular hypoplasia, deafness, progeroid features, and lipodystrophy. **Identifiers:** OMIM #615381; Orphanet ORPHA:280356; MONDO:0014157. **Synonyms:** MDPL syndrome; MDP syndrome; mandibular hypoplasia–hearing loss–progeroid syndrome; a POLD1‑related segmental progeroid/atypical Werner‑like syndrome. The information base is primarily **aggregated disease‑level resources plus individual case reports/small series** (Weedon 2013; Lessel 2015; Hoff 2026); there is no large EHR cohort.

### 2. Etiology
**Primary cause:** monogenic — heterozygous pathogenic variants in **POLD1**, overwhelmingly the *de novo* polymerase‑active‑site deletion p.Ser605del. **Genetic risk factors:** the causal variant itself; variant location (polymerase vs exonuclease vs CysB) is the principal determinant of phenotype/severity. **Environmental risk/protective factors and gene–environment interactions:** none established; MDPL is a Mendelian disorder not known to be modified by diet, toxins, or infection. **Protective genetic factors:** none identified. No infectious agent is involved.

### 3. Phenotypes
See Finding 6 and the HPO list above. Phenotype types span physical manifestations (mandibular hypoplasia, lipodystrophy, progeroid facies), clinical signs/sensory deficits (SNHL), and laboratory abnormalities (hypertriglyceridemia, insulin resistance/diabetes, abnormal liver). **Onset** ranges from childhood (facial/dental, hearing) to progressive lipodystrophy and metabolic disease emerging in later childhood/adulthood. **Severity** is variable and genotype‑linked; **progression** is slow and progressive. **Frequencies:** mandibular hypoplasia and SNHL approach obligate in p.Ser605del carriers (up to 100% and highly frequent), male hypogonadism ~92% in deletion carriers vs 0% in missense carriers. **Quality of life** is affected through metabolic disease, hearing impairment, feeding/dental problems, and progeroid appearance.

### 4. Genetic / Molecular Information
**Causal gene:** POLD1 (HGNC:9175; MIM 174761; 19q13.33). **Variant spectrum:** recurrent in‑frame p.Ser605del dominates (~18/21 historical cases); missense (R507C, R507H, Q1062R, W781C), CysB/Fe‑S variants (I1070N severe, S1073R mild), and a frameshift (p.Asp25Glufs*16) are reported. **Classification:** pathogenic/likely pathogenic for the recurrent deletion; some novel variants are VUS. **Variant type:** predominantly in‑frame deletion and missense. **Allele frequency:** essentially absent from gnomAD (private/de novo). **Origin:** germline, overwhelmingly *de novo*. **Functional consequence:** polymerase loss‑of‑function at the active site with a likely **dominant‑negative/altered‑interaction** component (aberrant TRF1 engagement) rather than simple haploinsufficiency. **Modifier genes:** none established; variant location within POLD1 is the main severity modifier. **Epigenetics/chromosomal abnormalities:** none specific to MDPL described.

### 5. Environmental Information
No environmental, lifestyle, or infectious contributors are established. MDPL is a purely genetic Mendelian disorder. (Not applicable.)

### 6. Mechanism / Pathophysiology
Presented as the ordered causal chain and domain map above (see **Mechanistic Model**). Upstream: polymerase loss‑of‑function → replication stress/impaired repair. Midstream: nuclear‑envelope/prelamin A anomalies, telomere/TRF1 dysfunction, micronuclei, persistent DNA damage → senescence. Downstream (branched): adipose, craniofacial, otologic, integumentary, gonadal manifestations. Molecular profiling: transcriptomics of MDPL fibroblasts shows dysregulated ECM/connective‑tissue genes and blunted DNA replication/repair induction after irradiation (CDC6, CLSPN, XRCC3, RAD51 among validated targets).

### 7. Anatomical Structures Affected
**Organ/system level:** craniofacial skeleton (mandible), auditory system (cochlea/inner ear, bilateral), adipose organ (subcutaneous fat), endocrine/metabolic (pancreas via hypertriglyceridemia, gonads), skin, liver (steatosis), eyes (retinopathy reported). **Tissue/cell level:** adipocytes, mesenchymal stem cells, dermal fibroblasts, connective tissue. **Subcellular:** nucleus, nuclear envelope/lamina, telomeres, Pol δ replication complex. **Lateralization:** hearing loss and lipodystrophy are bilateral; craniofacial involvement midline/symmetric.

### 8. Temporal Development
**Onset:** congenital/pediatric for craniofacial and often hearing features; lipodystrophy and metabolic disease are progressive with onset in childhood–young adulthood. **Course:** chronic, lifelong, slowly progressive; no remission. **Progression rate:** variable, genotype‑dependent. **Critical windows:** early recognition enables hearing rehabilitation, metabolic monitoring, and orthodontic intervention.

### 9. Inheritance and Population
Autosomal dominant; overwhelmingly *de novo* (most probands have unaffected parents). Penetrance appears high for the recurrent deletion with **variable expressivity**. No anticipation (not a repeat expansion). Germline mosaicism theoretically possible but not well documented. No founder effect or consanguinity role (dominant, *de novo*). **Epidemiology:** ultra‑rare (<1/1,000,000; few dozen confirmed cases). No sex or ethnic predilection, though male hypogonadism is a sex‑specific manifestation. "Probably underdiagnosed."

### 10. Diagnostics
Diagnosis rests on **molecular confirmation of a POLD1 variant** (single‑gene testing, lipodystrophy/progeroid gene panels, or WES/WGS) in a patient with the clinical tetrad. Supportive tests: audiometry (bilateral SNHL), fasting lipids (hypertriglyceridemia), glucose/insulin and HbA1c (insulin‑resistant diabetes), DXA/imaging for fat distribution, hepatic ultrasound (steatosis), craniofacial imaging (mandibular hypoplasia), and hormonal evaluation (hypogonadism). **Differential diagnosis:** Werner syndrome (distinguished by earlier onset, preserved scalp hair, telangiectasias, SNHL, absence of cataracts, lack of malignancy predisposition), mandibuloacral dysplasia (LMNA/ZMPSTE24), Hutchinson‑Gilford progeria, other familial partial lipodystrophies (e.g., PPARG‑FPLD3). No specific biomarker beyond genotype; no newborn/population screening is warranted given *de novo* origin.

### 11. Outcome / Prognosis
No formal survival statistics exist for this ultra‑rare disorder. Morbidity is driven by **metabolic complications** (insulin‑resistant diabetes, severe hypertriglyceridemia with pancreatitis risk, hepatic steatosis), **sensory disability** (hearing loss), and **progeroid/craniofacial features**. Unlike exonuclease‑domain POLD1 disease, MDPL carries **no recognized predisposition to malignancy**. Prognostic drivers include genotype (p.Ser605del severity), metabolic control, and timely multidisciplinary management. Lifespan impact is not well quantified.

### 12. Treatment
No disease‑specific/curative therapy. Supportive, multidisciplinary, and largely lipodystrophy‑based:
- **Metabolic:** metreleptin (approved for generalized lipodystrophy; off‑label consideration in partial forms), insulin sensitizers (thiazolidinediones; metformin), lipid‑lowering agents (fibrates) for hypertriglyceridemia, and emerging **incretin (GLP‑1/GIP) agonists** for partial lipodystrophy.
- **Sensory:** hearing aids/cochlear implants.
- **Endocrine:** sex‑hormone replacement for hypogonadism.
- **Craniofacial/dental:** orthodontic and maxillofacial management.
- **Perioperative:** careful anesthetic planning (difficult airway, scleroderma‑like skin, altered pharmacokinetics).
No gene, cell, or RNA‑based therapy exists; no pharmacogenomic guidance specific to MDPL.

### 13. Prevention
No primary prevention (variants are *de novo*). **Genetic counseling** is appropriate: recurrence risk for parents of a *de novo* case is low (but germline mosaicism cannot be fully excluded), while an affected individual has a 50% transmission risk. Prenatal/preimplantation testing is feasible for a known familial variant. Tertiary prevention centers on metabolic monitoring (preventing pancreatitis, controlling diabetes) and audiologic/dental surveillance. No immunization or environmental prevention applies.

### 14. Other Species / Natural Disease
No naturally occurring MDPL‑equivalent disease is described in companion animals or wildlife (not reported in OMIA for this specific syndrome). The POLD1 ortholog is highly conserved; **mouse Pold1** proofreading‑deficient models (D400A) recapitulate the mutator/cancer axis (not the MDPL progeroid axis). NCBI Taxon: *Mus musculus* (10090); *Homo sapiens* (9606). No zoonotic/transmission relevance (Mendelian disorder).

### 15. Model Organisms
- **Mouse (*Mus musculus*):** *Pold1* D400A exonuclease‑dead knock‑in (Goldsby 2002) — models proofreading deficiency → mutator/cancer phenotype; **does not** model the MDPL polymerase‑loss progeroid phenotype. Useful for the cancer‑predisposition (exonuclease) axis and for immunotherapy studies in mutator syndromes.
- **Human in vitro:** patient‑derived **dermal fibroblasts** and **mesenchymal stem cells** carrying p.Ser605del (Fiorillo 2018; Murdocca 2025; Paola 2024) are the principal MDPL disease models, recapitulating senescence, nuclear‑envelope anomalies, prelamin A accumulation, telomere/TRF1 dysfunction, and DNA‑repair defects.
- **Limitations:** no mouse/animal model reproduces the full MDPL multisystem phenotype; adipose‑specific mechanisms and tissue specificity remain unmodeled. iPSC‑derived adipocyte/organoid models are a logical but currently underdeveloped resource.

---

## Evidence Base

| PMID | Study (type) | Contribution |
|---|---|---|
| [23770608](https://pubmed.ncbi.nlm.nih.gov/23770608/) | Weedon 2013 (human genetics, founding) | Identifies POLD1 p.Ser605del polymerase‑active‑site deletion as cause; abolished polymerase, spared exonuclease; adipose‑homeostasis role |
| [36764464](https://pubmed.ncbi.nlm.nih.gov/36764464/) | Murdocca 2023 (review) | States domain‑dependent dichotomy (exonuclease→cancer; polymerase→MDPL) |
| [29120461](https://pubmed.ncbi.nlm.nih.gov/29120461/) | Dominguez‑Valentin/Buchanan 2018 (cohort) | Quantifies CRC risk 82–90% for POLD1 proofreading carriers |
| [41742372](https://pubmed.ncbi.nlm.nih.gov/41742372/) | Hoff 2026 (14 new + literature) | Genotype–phenotype: p.Ser605del vs missense severity differences |
| [26172944](https://pubmed.ncbi.nlm.nih.gov/26172944/) | Lessel 2015 (human genetics) | Variable expressivity; carriers without deafness/mandibular features; underdiagnosis |
| [12429860](https://pubmed.ncbi.nlm.nih.gov/12429860/) | Goldsby 2002 (mouse) | Pold1 D400A exonuclease‑dead → recessive mutator/cancer |
| [34594041](https://pubmed.ncbi.nlm.nih.gov/34594041/) | Robinson 2021 (human cells) | Proofreading carriers lack premature aging; separates cancer from MDPL axis |
| [30388038](https://pubmed.ncbi.nlm.nih.gov/30388038/) | Fiorillo 2018 (patient fibroblasts) | Nuclear‑envelope anomalies, prelamin A, senescence, persistent DNA damage |
| [41219970](https://pubmed.ncbi.nlm.nih.gov/41219970/) | Murdocca 2025 (MD + co‑IP) | Ser605del impairs dTTP binding; aberrant TRF1 interaction |
| [41083899](https://pubmed.ncbi.nlm.nih.gov/41083899/) | Murdocca 2025 (transcriptomics) | ECM/connective‑tissue and DNA replication/repair dysregulation |
| [36280868](https://pubmed.ncbi.nlm.nih.gov/36280868/) | Zuo 2022 (review/case) | Core phenotype frequencies |
| [35356184](https://pubmed.ncbi.nlm.nih.gov/35356184/) | Dhaliwal 2022 (case) | Hypertriglyceridemia‑induced pancreatitis (TG in 3000s) |
| [42888013](https://pubmed.ncbi.nlm.nih.gov/42888013/) | Cutaneous‑manifestation report | Distinguishing MDPL from Werner syndrome |
| [35590056](https://pubmed.ncbi.nlm.nih.gov/35590056/) | Chopra 2022 (case/review) | Recurrent deletion 18/21 cases; CysB/Fe‑S severity modulation |
| [37794082](https://pubmed.ncbi.nlm.nih.gov/37794082/) | Melvin/Semple 2023 (systematic review) | Metreleptin/TZD efficacy in lipodystrophy (applicable to MDPL metabolic care) |
| [39388000](https://pubmed.ncbi.nlm.nih.gov/39388000/) | Sekiguchi 2024 (case) | Anesthetic/perioperative management considerations |
| [39611849](https://pubmed.ncbi.nlm.nih.gov/39611849/) | Paola 2024 (MSC study) | Early pathological signs in mesenchymal stem cells |

**Evidence source types:** human clinical/genetic (Weedon, Lessel, Hoff, Zuo, Chopra, case reports); human in vitro (Fiorillo, Murdocca ×2, Paola); model organism (Goldsby mouse); computational/structural (Murdocca molecular dynamics); systematic review (Melvin/Semple).

---

## Limitations and Knowledge Gaps

1. **Tissue specificity is unexplained.** Why loss of a ubiquitous replicative polymerase preferentially damages adipose tissue, mandible, cochlea, and gonads remains the central open question (Weedon 2013).
2. **Small N / publication bias.** Only a few dozen genetically confirmed cases exist; frequency estimates (e.g., genotype–phenotype percentages) derive from aggregated small series and are subject to ascertainment bias and probable underdiagnosis.
3. **No MDPL animal model.** Existing mouse models capture the exonuclease/cancer axis, not the polymerase‑loss progeroid phenotype; adipose, otologic, and craniofacial mechanisms are unmodeled in vivo.
4. **Mechanistic links partly inferred.** The prelamin A/nuclear‑envelope connection and the precise contribution of aberrant TRF1/telomere engagement to clinical aging are demonstrated in cells but not causally dissected in tissue.
5. **No prognosis/survival data.** Natural‑history and life‑expectancy data are essentially absent.
6. **No targeted therapy or trials.** Metabolic management is extrapolated from lipodystrophy evidence of low/very‑low quality; no MDPL‑specific trials exist.
7. **Variant classification challenges.** Some novel missense and CysB variants remain VUS; functional assays are not standardized for polymerase‑domain (MDPL‑type) variants the way they are being developed for exonuclease (cancer) variants.

---

## Proposed Follow-up Experiments / Actions

1. **iPSC‑derived adipocyte and organoid models** of p.Ser605del to directly test the adipose‑homeostasis hypothesis and screen candidate therapeutics (senolytics, metabolic agents).
2. **Conditional/knock‑in mouse** carrying a polymerase‑active‑site deletion (vs the existing exonuclease‑dead model) to determine whether the progeroid/lipodystrophy phenotype can be recapitulated in vivo.
3. **Mechanistic dissection of the TRF1/telomere axis** — test whether disrupting the aberrant FSLYP/TRF1 interaction rescues senescence in patient cells.
4. **Prelamin A pathway interrogation** — assess whether prelamin A accumulation is causal (e.g., farnesyltransferase/HGPS‑style interventions) or a downstream marker in MDPL cells.
5. **International MDPL registry and natural‑history study** to establish prevalence, penetrance, progression rates, survival, and genotype–phenotype correlations with adequate power.
6. **Prospective evaluation of metreleptin vs incretin (GLP‑1/GIP) agonists** specifically in MDPL‑associated partial lipodystrophy, given emerging incretin data in partial lipodystrophy.
7. **Standardized functional assays** for polymerase‑domain POLD1 variants to resolve VUS and support ACMG/ClinGen classification distinct from exonuclease‑domain cancer variants.

---

*Report compiled from 10 confirmed findings and 42 reviewed papers across 5 investigation iterations. Causal gene: **POLD1**. Primary disease identifiers: MONDO:0014157, OMIM #615381, Orphanet ORPHA:280356.*


## Artifacts

- [OpenScientist final report](Mandibular_Hypoplasia_Deafness_Progeroid_Features_and_Lipodystrophy_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Mandibular_Hypoplasia_Deafness_Progeroid_Features_and_Lipodystrophy_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 17 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:41742372`: "those with the p.Ser605del (n = 26) POLD1 variant had significantly increased prevalence of mandibular hypoplasia (57% vs 100%…; P = .015), small mouth (36% vs 100%…; P = .015), crowded teeth (44% vs 91%…; P = .046), and hypogonadism in male patients (0% vs 92%…; P = .046)"
  - closest text in source: "Compared to individuals with missense variants (n = 15), those with the p.Ser605del (n = 26) POLD1 variant had significantly increased prevalence of mandibular hypoplasia (57% vs 100%, respectively; P = .015), small mouth (36% vs 100%, respectively; P = .015), crowded teeth (44% vs 91%, respectively; P = .046), and hypogonadism in male patients (0% vs 92%, respectively; P = .046)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 5 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006260` (1 mention) - the report calls it "GO biological process:** DNA replication"; GO calls it **DNA replication**
- `GO:0043625` (1 mention) - the report calls it "GO cellular component:** delta DNA polymerase complex"; GO calls it **delta DNA polymerase complex**
- `CL:0000136` (1 mention) - the report calls it "CL cell types:** adipocyte"; CL calls it **adipocyte**
- `UBERON:0001684` (1 mention) - the report calls it "UBERON anatomy:** mandible"; UBERON calls it **mandible**, and lists "mammaliam mandible" among its other names
- `CHEBI:17855` (1 mention) - the report calls it "CHEBI:** triglyceride"; CHEBI calls it **triglyceride**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

35 of 37 terms resolved to a current term; the rest could not be looked up either way.