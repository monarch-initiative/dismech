---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T22:25:54.115477'
end_time: '2026-11-12T22:38:08.229917'
duration_seconds: 734.11
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Progressive Microcephaly-Seizures-Cortical Blindness-Developmental
    Delay Syndrome
  mondo_id: MONDO:0014714
  category: Mendelian
  causal_genes: DIAPH1
  omim_id: OMIM:616632
  synonyms: seizures, cortical blindness, microcephaly syndrome; SCBMS
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
  job_id: ceb03212-9559-4a0c-bb48-c362428e77b0
citation_count: 10
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 18
  relevance_assessed: 10
  on_topic: 8
  validator_version: 0.5.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
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
  path: Progressive_Microcephaly-Seizures-Cortical_Blindness-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Progressive_Microcephaly-Seizures-Cortical_Blindness-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Microcephaly-Seizures-Cortical Blindness-Developmental Delay Syndrome
- **MONDO ID:** MONDO:0014714 (if available)
- **Causal gene(s):** DIAPH1
- **OMIM:** OMIM:616632
- **Synonyms:** seizures, cortical blindness, microcephaly syndrome; SCBMS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Progressive Microcephaly-Seizures-Cortical Blindness-Developmental Delay Syndrome** covering all of the
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

# Progressive Microcephaly–Seizures–Cortical Blindness–Developmental Delay Syndrome (SCBMS): A DIAPH1 Cytoskeletopathy

**Disease:** Progressive Microcephaly–Seizures–Cortical Blindness–Developmental Delay Syndrome (SCBMS)
**MONDO:** MONDO:0014714 · **OMIM:** 616632 · **Causal gene:** **DIAPH1** (HGNC:2876; protein product **mDia1**) · **Category:** Mendelian, autosomal recessive

---

## Summary

Progressive Microcephaly–Seizures–Cortical Blindness–Developmental Delay Syndrome (**SCBMS**) is an ultra-rare autosomal-recessive neurodevelopmental and neuro-immunological disorder caused by **biallelic loss-of-function (LOF) variants in *DIAPH1***, the gene encoding the RhoA-effector formin **mDia1** (Diaphanous-related formin 1). The disorder was first established as a human Mendelian condition by Ercan-Sencicek et al. in 2015 ([PMID: 24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/)) and has since been delineated across several cohorts, culminating in a 53-individual series in 2026 ([PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)). It must be carefully distinguished from the *allelic* but mechanistically opposite dominant **gain-of-function** DIAPH1 disorder **DFNA1** (non-syndromic sensorineural deafness with macrothrombocytopenia).

The core clinical phenotype comprises **early-infantile-onset (mean ~2.3 months) progressive postnatal microcephaly, epilepsy, cortical visual impairment/blindness, and severe developmental delay/intellectual disability**, frequently accompanied by occipital-predominant structural brain abnormalities. Beyond the neurological core, DIAPH1 loss produces a striking multisystem signature: **combined immunodeficiency** (low T-cell receptor excision circles [TRECs], low naïve T cells, and T/NK/ILC defects), **mitochondrial dysfunction**, a **DNA-repair defect**, and a notable **predisposition to B-cell lymphoma** (3 of 7 patients in one cohort).

Mechanistically, all of these features converge on the loss of mDia1's dual cytoskeletal function: as a RhoA effector, mDia1 elongates **long, linear, unbranched actin filaments** and coordinates/stabilizes **microtubules**, functions essential for mitosis, cell polarity, migration, and microtubule-organizing-center (MTOC) positioning in both **neuroepithelial precursors / cortical interneurons** and **lymphocytes**. The result is a unified "**cytoskeletopathy**" in which a single molecular lesion branches into neurodevelopmental, immune, and genome-stability phenotypes. No curative therapy exists; diagnosis is molecular (exome/genome sequencing), management is supportive and multidisciplinary, and the prognosis is guarded.

---

## Key Findings

### Finding 1 — Biallelic LOF of *DIAPH1* causes SCBMS (autosomal recessive)

SCBMS (MONDO:0014714; OMIM 616632) is caused by **biallelic loss-of-function variants in *DIAPH1***, which encodes the formin mDia1. Multiple independent cohorts converge on this conclusion:

- **Ercan-Sencicek et al., 2015** ([PMID: 24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/)) — founding study; identified a homozygous nonsense variant **p.Gln778\*** by linkage plus whole-exome sequencing (WES) in a consanguineous family with microcephaly, severe visual impairment, intellectual disability, and short stature.
- **Kaustio et al., 2021** ([PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)) — 7 patients; 5 Finnish homozygous for the splice variant **c.684+1G>A**, 2 Omani homozygous for the frameshift **c.2769delT / p.F923fs**.
- **Esmaeilzadeh et al., 2024** ([PMID: 39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/)) — novel homozygous nonsense **c.1285C>T / p.Gln429\*** plus review of 20 prior cases; recurrent variants **c.2769del, c.684+1G>A, c.2332C>T** account for ~72% of cases.
- **Galassi Deforie et al., 2026** ([PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)) — largest cohort, 53 individuals (33 newly reported).

> "Homozygous loss of DIAPH1 results in seizures, cortical blindness, and microcephaly syndrome (SCBMS)." — [PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)

> "Biallelic DIAPH1 pathogenic variants cause a neurodevelopmental syndrome occasionally associated with immunodeficiency." — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)

The inheritance is **autosomal recessive**, with nonsense, frameshift, and splice LOF variants. This contrasts sharply with the dominant **gain-of-function** DIAPH1 variants that cause DFNA1 / macrothrombocytopenia:

> "Dominant gain-of-function DIAPH1 variants cause macrothrombocytopenia and sensorineural deafness (autosomal dominant non-syndromic hearing loss 1 (DFNA1)), while homozygous loss of DIAPH1 results in seizures, cortical blindness, and microcephaly syndrome (SCBMS)." — [PMID: 38915998](https://pubmed.ncbi.nlm.nih.gov/38915998/)

**Key identifiers:** MONDO:0014714 · OMIM:616632 · gene DIAPH1 (HGNC:2876, chromosome 5q31.3). Synonyms: *seizures, cortical blindness, microcephaly syndrome*; SCBMS. Information is derived from aggregated disease-level resources (OMIM/Orphanet) and from individual-patient case series/cohorts in the primary literature.

### Finding 2 — Core clinical phenotype: progressive microcephaly, epilepsy, cortical visual impairment, developmental delay, early infantile onset

The defining tetrad of SCBMS is **progressive (postnatal) microcephaly, epilepsy, cortical visual impairment/blindness, and severe developmental delay/intellectual disability**, with onset in early infancy.

> "Clinical features included developmental delay, intellectual disability, progressive microcephaly, cortical visual impairment or blindness, epilepsy, and frequent occipital-predominant brain abnormalities." — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/) (n=53)

> "The mean age of onset for patients in the group of 20 patients with a known age of onset was 2.3 months (SD = 1.6)." — [PMID: 39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/)

Nearly half of patients in the large cohort had infections (mainly respiratory, related to epilepsy/aspiration). The 2021 cohort additionally documented mitochondrial dysfunction and immunodeficiency in the same patients ([PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)). The phenotype is **progressive** (microcephaly worsens postnatally) and **severe**, with substantial quality-of-life impact: profound disability, dependence for daily activities, visual loss, and seizure burden.

**Suggested HPO terms:** Progressive microcephaly (HP:0000253), Seizure (HP:0001250), Cortical visual impairment (HP:0100704), Global developmental delay (HP:0001263), Intellectual disability (HP:0001249), Cerebral atrophy (HP:0002059), Cerebellar atrophy (HP:0001272), Recurrent respiratory infections (HP:0002205), Short stature (HP:0004322).

### Finding 3 — Multisystem signature: combined immunodeficiency, mitochondrial dysfunction, DNA-repair defect, and B-cell lymphoma risk

DIAPH1 loss extends well beyond the brain. Kaustio et al. ([PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)) found poor lymphocyte activation/proliferation, defective B-cell maturation, absence of naïve T cells, and mitochondrial dysfunction; critically, **CRISPR DIAPH1 knockout in healthy-donor PBMCs replicated the T-cell activation defect**, and patient T cells showed impaired adhesion and inefficient MTOC repositioning. Three of seven patients developed **B-cell lymphoma**.

> "the patients presented with infection susceptibility due to defective lymphocyte maturation and 3 patients developed B-cell lymphoma" — [PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)

Azizoglu et al., 2024 ([PMID: 39120629](https://pubmed.ncbi.nlm.nih.gov/39120629/)) reported six patients with novel LOF variants and major **T, NK, and ILC defects**:

> "Loss of function mutations in Diaphanous related formin 1 (DIAPH1) are associated with seizures, cortical blindness, and microcephaly syndrome (SCBMS) and are recently linked to combined immunodeficiency." — [PMID: 39120629](https://pubmed.ncbi.nlm.nih.gov/39120629/)

The large 2026 cohort confirmed a consistent immunological laboratory signature even when gross subsets looked normal:

> "T cell receptor excision circles and naïve T-lymphocyte counts were consistently low" — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)

### Finding 4 — Mechanism: mDia1 is a RhoA-effector formin building linear actin and stabilizing microtubules

DIAPH1/mDia1 is a **Diaphanous-related formin** and a canonical downstream effector of the small GTPase **RhoA**. When RhoA-GTP binds mDia1, it relieves the protein's N-terminal (DID)–C-terminal (DAD) autoinhibition, activating the **FH2 domain** to nucleate and processively elongate long, linear, unbranched actin filaments that resist myosin-driven contraction; mDia1 also coordinates and stabilizes microtubules.

> "mDia1 generates linear actin filaments in the maintenance of polarity during adhesion, migration, and division in immune cells and neuroepithelial cells, and in driving tangential migration of cortical interneurons in the rodent" — [PMID: 24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/)

Supporting mechanistic cell biology:
- mDia1 regulates **microtubule stability and dynamics** as a Rho effector coordinating actin and MT cytoskeletons ([PMID: 25298036](https://pubmed.ncbi.nlm.nih.gov/25298036/)).
- The **Memo–RhoA–mDia1** axis controls MT dynamics, adhesion-site formation, and migration ([PMID: 18955552](https://pubmed.ncbi.nlm.nih.gov/18955552/)).
- mDia-family formins assemble long linear filaments capable of withstanding myosin-driven contractile load; combined formin loss causes reduced cortical rigidity, excessive blebbing, and delayed cytokinesis ([PMID: 42827260](https://pubmed.ncbi.nlm.nih.gov/42827260/)).
- Truncation of the FH2 domain (p.R1049X) abolishes F-actin elongation activity and impairs cell–cell junction formation and mitosis ([PMID: 35060117](https://pubmed.ncbi.nlm.nih.gov/35060117/)).

Because mDia1 protein is expressed in human neuronal precursor cells during mitotic division, loss impairs the mitosis, polarity, and migration of neural precursors and cortical interneurons — the cell-biological root of microcephaly and cortical malformation.

**Suggested GO BP terms:** actin filament polymerization (GO:0030041), actin nucleation (GO:0045010), regulation of microtubule cytoskeleton organization (GO:0070507), neuron migration (GO:0001764), mitotic cell cycle (GO:0000278), establishment of cell polarity (GO:0030010).

### Finding 5 — Model organisms partially recapitulate the human disease

| Model | Genetic manipulation | Phenotype recapitulation | Key limitation |
|---|---|---|---|
| **Mouse** (*Diap1* KO) | Constitutive knockout | Grossly **normal body and brain size**; unilateral ventricular enlargement on histology | **Does not model human microcephaly** |
| **Xenopus tropicalis** | Loss of function | **Mirrors growth and eye defects** seen in humans | Non-mammalian |
| **Zebrafish** | Loss of function | No overt malformation; **seizure-like behavior** in Phenothiazine assays | Does not reproduce structural brain defects |
| **Human PBMC (CRISPR KO)** | In-vitro DIAPH1 KO | **Replicates T-cell activation defect** | Immune phenotype only |

> "diap1 (mDia1 knockout (KO))-deficient mice have grossly normal body and brain size" — [PMID: 24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/)

> "The Xenopus model mirrored growth and eye defects seen in humans, whereas zebrafish exhibited no overt malformations but showed seizure-like behavior" — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)

The mouse KO's lack of microcephaly is an important caveat — it likely reflects **functional redundancy** among mammalian formins (e.g., mDia2/mDia3) and species differences in cortical neurogenesis. The human in-vitro CRISPR PBMC model ([PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)) is the strongest direct causal evidence for the immune phenotype.

### Finding 6 — Epidemiology and inheritance: ultra-rare, consanguinity-enriched, with a Finnish founder allele

SCBMS is **ultra-rare**. Only ~20 cases across 7 studies were on record by 2024 ([PMID: 39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/)), expanding to **53 individuals (33 new) by 2026** ([PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)). No formal prevalence/incidence figure is published; the condition sits far below 1/100,000.

Inheritance is **autosomal recessive**, frequently **homozygous in consanguineous pedigrees** (Ercan-Sencicek 2015, Esmaeilzadeh 2024). A **Finnish founder splice variant** drives a population cluster:

> "all Finnish patients homozygous for a rare DIAPH1 splice-variant (NM_005219:c.684+1G>A) enriched in the Finnish population" — [PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/)

> "Twenty cases from seven studies were found after a review of the literature." — [PMID: 39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/)

> "A total of 53 individuals with biallelic DIAPH1 variants, including 33 previously unreported patients, were studied." — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)

Reported populations include Middle Eastern (Omani, Saudi, Iranian, Egyptian), Finnish, and others. Recurrent variants **c.2769del, c.684+1G>A, c.2332C>T** account for ~72% of cases. Penetrance appears high/complete for biallelic LOF; expressivity is variable (notably in immunological severity). Consanguinity is a major risk-amplifying factor; no sex bias is reported (autosomal recessive).

### Finding 7 — Diagnostics, management, and prognosis

**Diagnosis is molecular.** The disorder was discovered by, and is diagnosed with, **whole-exome/whole-genome sequencing** (often aided by linkage/homozygosity mapping in consanguineous families), confirmed by Sanger sequencing:

> "exome sequencing was performed to identify the genetic basis of the clinical presentation in an Iranian 7-year-old boy. Validation of the detected variant was done by Sanger sequencing." — [PMID: 39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/)

**Supportive workup** includes brain MRI (progressive microcephaly, occipital-predominant abnormalities, cerebral/cerebellar atrophy), EEG (epilepsy), ophthalmologic/visual assessment (cortical visual impairment), and immunological evaluation (lymphocyte subsets, TRECs, naïve T cells, immunoglobulins) ([PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/), [PMID: 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/), [PMID: 39120629](https://pubmed.ncbi.nlm.nih.gov/39120629/)).

**Differential diagnosis** includes other primary/progressive microcephaly syndromes (e.g., MCPH genes such as *ASPM*, *WDR62*, *CASK*-related microcephaly), congenital infections (TORCH), and other combined-immunodeficiency-with-neurodevelopmental syndromes; the occipital-predominant imaging, cortical blindness, and combined immunodeficiency with low TRECs/naïve T cells point toward DIAPH1.

**No curative or disease-specific therapy exists.** Management is supportive and symptomatic: antiseizure medications for epilepsy, developmental/rehabilitative therapies (PT/OT/speech), visual support, nutritional support (aspiration risk), and prophylaxis/treatment of infections. Immunological surveillance and oncologic vigilance (lymphoma) are warranted. Genetic counseling (recessive recurrence risk 25%; carrier testing; prenatal/preimplantation options) is central to prevention.

**Prognosis is guarded.** Severe neurodevelopmental disability, early onset (~2.3 months), respiratory infection susceptibility, and lymphoma predisposition dominate the clinical course:

> "The DNA repair defect may influence susceptibility to infection, lymphoma, or treatment-related toxicity." — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)

**Suggested NCIT intervention terms:** Anticonvulsant Agent (C264), Physical Therapy (C15351), Occupational Therapy (C15214), Nutritional Support (C15229), Supportive Care (C15226).

### Finding 8 — Synthesis: a unified RhoA–mDia1 cytoskeletopathy

Integrating five primary clinical studies ([PMIDs 24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/), [33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/), [39120629](https://pubmed.ncbi.nlm.nih.gov/39120629/), [39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/), [41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)) with mechanistic cell biology ([PMIDs 25298036](https://pubmed.ncbi.nlm.nih.gov/25298036/), [18955552](https://pubmed.ncbi.nlm.nih.gov/18955552/), [42827260](https://pubmed.ncbi.nlm.nih.gov/42827260/)), every SCBMS feature traces to loss of a single cytoskeletal function.

> "DIAPH1 is critical for neurodevelopment, immune regulation, and DNA repair." — [PMID: 41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/)

> "mDia1 generates linear actin filaments in the maintenance of polarity during adhesion, migration, and division in immune cells and neuroepithelial cells..." — [PMID: 24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic LOF variant in *DIAPH1*** (nonsense/frameshift/splice; e.g., p.Gln778\*, c.684+1G>A, p.F923fs) **leads to** absent or non-functional **mDia1 formin** protein (loss of function). *[demonstrated — multiple cohorts]*
2. Loss of mDia1 **results in** failure to relieve RhoA-GTP–dependent formin activation, hence **loss of processive elongation of long, linear, unbranched actin filaments** and **loss of coordinated microtubule stabilization**. *[demonstrated in vitro — PMID 24781755, 25298036, 35060117, 42827260]*
3. Defective actin/MT architecture **impairs** cell polarity, mitotic spindle orientation, cytokinesis, cell adhesion/migration, and **MTOC repositioning**. *[demonstrated — patient T cells, CRISPR PBMC; inferred for neural cells]*
4. **Branch A — Neural:** In **neuroepithelial precursors and tangentially migrating cortical interneurons**, impaired division and migration **lead to** reduced neuron production and faulty cortical wiring → **progressive postnatal microcephaly, epilepsy, cortical visual impairment, developmental delay**. *[inferred from mDia1 biology + human phenotype]*
5. **Branch B — Immune:** In **lymphocytes (T, NK, ILC, B)**, impaired adhesion/MTOC positioning and maturation **lead to** poor activation/proliferation, low TRECs and naïve T cells → **combined immunodeficiency** and recurrent (mainly respiratory) infections. *[demonstrated — PMID 33662367, 39120629]*
6. **Branch C — Genome stability:** A **DNA-repair defect** (plus mitochondrial dysfunction) **results in** increased susceptibility to **B-cell lymphoma** and possibly treatment-related toxicity. *[demonstrated association — PMID 33662367, 41860019]*

```
   Biallelic DIAPH1 LOF
            │
     loss of mDia1 formin
   (RhoA effector; linear actin
    elongation + MT stabilization)
            │
  cytoskeletal failure: polarity,
  mitosis, migration, MTOC positioning
            │
   ┌────────┼────────────────┐
   ▼        ▼                ▼
NEURAL    IMMUNE          GENOME STABILITY
precursors/ lymphocytes    DNA repair +
interneurons (T/NK/ILC/B)  mitochondria
   │         │                │
microcephaly combined        B-cell lymphoma
epilepsy    immunodeficiency  risk; infection/
cortical    (low TRECs,       treatment toxicity
blindness   low naive T)
dev. delay
```

### Allelic contrast (same gene, opposite mechanism)

| Feature | **SCBMS** (this disease) | **DFNA1 / macrothrombocytopenia** |
|---|---|---|
| Variant mechanism | **Loss of function** | **Gain of function** (autoinhibition disrupted) |
| Inheritance | Autosomal **recessive** (biallelic) | Autosomal **dominant** (heterozygous) |
| Core phenotype | Microcephaly, seizures, cortical blindness, DD | Sensorineural deafness, macrothrombocytopenia |
| Representative refs | [PMID 33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/), [41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/) | [PMID 38915998](https://pubmed.ncbi.nlm.nih.gov/38915998/), [35060117](https://pubmed.ncbi.nlm.nih.gov/35060117/) |

This allelic series is a cautionary reminder that the shared gene name does not imply a shared disease — SCBMS is strictly the recessive LOF condition.

### Ontology term suggestions

- **Gene/protein:** DIAPH1 (HGNC:2876). **GO BP:** actin filament polymerization (GO:0030041), actin nucleation (GO:0045010), regulation of microtubule cytoskeleton organization (GO:0070507), cell migration (GO:0016477), mitotic cell cycle (GO:0000278), neuron migration (GO:0001764). **GO CC:** actin cytoskeleton (GO:0015629), microtubule cytoskeleton (GO:0015630), cell leading edge (GO:0031252).
- **Cell types (CL):** neuroepithelial cell (CL:0000098), radial glial cell (CL:0000681), GABAergic cortical interneuron (CL:0000617), T cell (CL:0000084), natural killer cell (CL:0000623), innate lymphoid cell (CL:0001065), B cell (CL:0000236).
- **Anatomy (UBERON):** cerebral cortex (UBERON:0000956), occipital lobe (UBERON:0002021), visual cortex (UBERON:0000411), cerebellum (UBERON:0002037), brain (UBERON:0000955).
- **CHEBI:** GTP (CHEBI:15996) — RhoA-GTP activation.

---

## Evidence Base

| PMID | Title (abbreviated) | Type | Contribution |
|---|---|---|---|
| [24781755](https://pubmed.ncbi.nlm.nih.gov/24781755/) | *Homozygous loss of DIAPH1 is a novel cause of microcephaly in humans* | Human clinical + model | **Founding study**; p.Gln778\*; defines mDia1 cytoskeletal biology; mouse KO lacks microcephaly |
| [33662367](https://pubmed.ncbi.nlm.nih.gov/33662367/) | *Loss of DIAPH1 causes SCBMS, combined immunodeficiency, and mitochondrial dysfunction* | Human clinical + in vitro | Immunodeficiency, mitochondrial dysfunction, 3/7 lymphoma; Finnish founder c.684+1G>A; CRISPR PBMC replicates T-cell defect |
| [39120629](https://pubmed.ncbi.nlm.nih.gov/39120629/) | *DIAPH1-Deficiency is Associated with Major T, NK and ILC Defects* | Human clinical | Deep immunophenotyping; T/NK/ILC defects |
| [39578953](https://pubmed.ncbi.nlm.nih.gov/39578953/) | *A Novel Homozygote Pathogenic Variant... (SCBMS): Report of a Family and Literature Review* | Human clinical + review | p.Gln429\*; onset ~2.3 months; 20-case review; recurrent variants (72%) |
| [41860019](https://pubmed.ncbi.nlm.nih.gov/41860019/) | *Recessive loss of DIAPH1 function causes a progressive neurodevelopmental syndrome...* | Human clinical + model | **Largest cohort (n=53)**; occipital-predominant MRI; low TRECs/naïve T; Xenopus & zebrafish models; DNA-repair link |
| [38915998](https://pubmed.ncbi.nlm.nih.gov/38915998/) | *A Novel Variant in DIAPH1 Causing Macrothrombocytopenia and Non-syndromic Hearing Loss* | Human clinical | Establishes **allelic contrast**: dominant GOF = DFNA1/MTP vs recessive LOF = SCBMS |
| [35060117](https://pubmed.ncbi.nlm.nih.gov/35060117/) | *Late-onset hearing loss case associated with a heterozygous truncating variant of DIAPH1* | Human clinical + in vitro | FH2-domain truncation abolishes F-actin elongation; supports LOF biology |
| [25298036](https://pubmed.ncbi.nlm.nih.gov/25298036/) | *The formin DIAPH1 (mDia1) regulates megakaryocyte proplatelet formation...* | In vitro | mDia1 remodels actin AND microtubule cytoskeletons |
| [18955552](https://pubmed.ncbi.nlm.nih.gov/18955552/) | *Memo-RhoA-mDia1 signaling controls microtubules, actin, adhesion sites...* | In vitro | mDia1 as RhoA effector coordinating MT dynamics, adhesion, migration |
| [42827260](https://pubmed.ncbi.nlm.nih.gov/42827260/) | *Daam-, FMNL-, and mDia-family formins jointly regulate cortical actin dynamics* | In vitro | mDia1 builds load-bearing linear filaments; combined loss → cortical/cytokinesis defects; redundancy |

**Convergence:** Human cohorts (clinical genetics), in-vitro CRISPR (causal validation of the immune phenotype), and cross-species models (Xenopus/zebrafish/mouse) together support a single, coherent mechanism. The **mouse KO's absence of microcephaly** is the principal challenge to a simple one-gene-one-phenotype model and points to mammalian formin redundancy and species-specific cortical neurogenesis.

---

## Limitations and Knowledge Gaps

1. **Small denominator.** Even the largest cohort is 53 patients; no validated prevalence/incidence, penetrance quantification, or natural-history survival curves exist. Phenotype frequencies are approximate.
2. **Mechanistic inference in the brain.** The neural branch of the causal chain is **inferred** from mDia1 cell biology and rodent interneuron-migration data plus the human phenotype; direct human neural-cell (e.g., iPSC-derived organoid) demonstration of the microcephaly mechanism is limited.
3. **Model–human discordance.** The mouse *Diap1* KO does not reproduce microcephaly, so no fully faithful mammalian genetic model is yet available; Xenopus and zebrafish capture only subsets of features.
4. **Genotype–phenotype correlation.** Whether specific variants (hypomorphic splice vs complete null) predict immune vs lymphoma vs severity remains unresolved.
5. **Immune/lymphoma quantification.** Lymphoma risk is derived from a single small cohort (3/7); the true lifetime risk and whether all patients require oncologic surveillance are unknown.
6. **DNA-repair mechanism.** The nature of the DNA-repair defect and its molecular link to the actin/MT cytoskeleton is asserted but mechanistically underspecified.
7. **No therapeutics.** There are no disease-modifying treatments, trials, or validated biomarkers of progression. Sections on gene therapy, immunization, infectious agents, and veterinary/natural disease are **not applicable / not reported** for this disorder.

---

## Proposed Follow-up Experiments / Actions

1. **Patient-derived cerebral organoids / iPSC neural models** to directly test the neural branch (progenitor division, spindle orientation, interneuron migration) and close the inference gap in the causal chain.
2. **Conditional / double-formin mouse models** (e.g., *Diaph1* with *Diaph3* or neural-specific conditional KO) to overcome redundancy and recapitulate microcephaly.
3. **Genotype–phenotype registry** across all 53+ patients with standardized MRI, EEG, immune panels (TRECs, naïve T, Ig), and oncologic outcomes to define variant-specific severity and lymphoma risk.
4. **Prospective immunologic and oncologic surveillance protocol** (lymphocyte subsets, TRECs, imaging) given the documented combined immunodeficiency and B-cell lymphoma predisposition; evaluate whether IVIG/antimicrobial prophylaxis improves outcomes.
5. **Molecular dissection of the DNA-repair defect** (e.g., γH2AX dynamics, repair-pathway assays) in patient cells to clarify the genome-stability branch and its link to the cytoskeleton.
6. **Natural-history study** to establish progression rate of microcephaly, epilepsy severity, survival, and causes of mortality (infection/aspiration vs lymphoma).
7. **Carrier-screening consideration** in the Finnish population (founder c.684+1G>A) and consanguineous communities, with genetic counseling and prenatal/preimplantation options for at-risk families.

---

*Report compiled from 8 confirmed findings across 5 iterations and 13 reviewed papers. Evidence source types are indicated per paper (human clinical, in vitro, model organism). All quoted text is verbatim from the cited PubMed abstracts.*


## Artifacts

- [OpenScientist final report](Progressive_Microcephaly-Seizures-Cortical_Blindness-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Progressive_Microcephaly-Seizures-Cortical_Blindness-Developmental_Delay_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:15996` (1 mention) - the report calls it "CHEBI:** GTP"; CHEBI calls it **GTP**, and lists "5'-GTP" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

33 of 35 terms resolved to a current term; the rest could not be looked up either way.