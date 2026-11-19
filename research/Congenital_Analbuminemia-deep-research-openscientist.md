---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T14:30:02.786850'
end_time: '2026-10-31T14:48:27.665496'
duration_seconds: 1104.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Congenital Analbuminemia
  mondo_id: MONDO:0014449
  category: Mendelian
  causal_genes: ALB
  omim_id: OMIM:616000
  synonyms: analbuminemia; congenital analbuminaemia; CAA
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
citation_count: 23
reference_validation:
  total_references: 30
  verified: 30
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 30
  on_topic: 16
  validator_version: 0.4.0
term_validation:
  total_terms: 22
  verified: 20
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0100281
    reported_labels:
    - Protein-losing enteropathy mimic / GI morbidity
    ontology_label: Chronic colitis
  labels_variant: 4
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
  path: Congenital_Analbuminemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Congenital_Analbuminemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Analbuminemia
- **MONDO ID:** MONDO:0014449 (if available)
- **Causal gene(s):** ALB
- **OMIM:** OMIM:616000
- **Synonyms:** analbuminemia; congenital analbuminaemia; CAA
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Congenital Analbuminemia** covering all of the
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

# Congenital Analbuminemia (CAA): A Comprehensive Disease Characterization

**Disease:** Congenital Analbuminemia · **MONDO:** MONDO:0014449 · **OMIM:** #616000 · **Orphanet:** ORPHA:88918 · **Causal gene:** *ALB* (albumin), HGNC:399, located on chromosome 4q13.3

---

## Summary

**Congenital analbuminemia (CAA) is an ultra-rare, autosomal-recessive Mendelian disorder caused by biallelic loss-of-function (LoF) variants in the albumin gene, *ALB* (4q13.3; HGNC:399; reference transcript NM_000477).** Affected individuals produce little or no serum albumin (typically <1 g/L, versus a normal ~35–50 g/L), yet—remarkably—the clinical phenotype in adults is usually mild. The paradox of "living without the most abundant plasma protein" is explained by robust physiological compensation: the liver increases synthesis of other secreted proteins (globulins, transferrin, fibrinogen, apolipoprotein A-I) to defend plasma colloid osmotic (oncotic) pressure, and albumin's many ligands (fatty acids, bilirubin, hormones, drugs) are redistributed onto lipoproteins and globulins. The dominant clinical features are therefore mild bilateral ankle oedema, fatigue, mild hypotension, and—most consistently—a secondary dyslipidemia (hypercholesterolemia, elevated beta-lipoproteins), which carries an increased long-term risk of atherosclerotic/coronary disease.

The genetic architecture is one of marked allelic heterogeneity: more than 20 distinct pathogenic *ALB* variants have been described, nearly all predicted to be null alleles (nonsense, frameshift, splice-site, and start-codon mutations acting through premature termination and nonsense-mediated decay). The single most common cause is the recurrent **"Kayseri" frameshift (c.228_229delAT, exon 3)**, which accounts for roughly half of all known cases and is found in geographically and ethnically distinct, often consanguineous populations—a founder effect. Only about 70 cases have been reported worldwide, making CAA one of the rarer Mendelian traits catalogued.

While adults are typically well, the **perinatal and childhood periods carry the highest morbidity**: recent pediatric cohorts reveal a multisystem picture of early-onset oedema, gastrointestinal morbidity (frequently misdiagnosed as protein-losing enteropathy), antenatal complications, recurrent respiratory infections, dyslipidemia, and coagulation/immune abnormalities. Diagnosis rests on demonstrating near-absent serum albumin *without proteinuria*, followed by *ALB* gene sequencing. Management is supportive—lipid-lowering therapy, selective albumin infusion for acute needs (e.g., polyhydramnios in pregnancy), genetic counseling, and careful, free-drug-based dosing of highly protein-bound medications (the unbound drug fraction rises dramatically in the absence of albumin). The principal disease models are the spontaneous **Nagase analbuminemic rat (NAR)** and an engineered **Alb⁻/⁻ mouse**, both of which recapitulate hyperlipidemia and compensatory hepatic protein synthesis while remaining broadly healthy.

---

## Key Findings

### 1. CAA is an autosomal-recessive, allelically heterogeneous disorder caused by biallelic *ALB* loss-of-function variants (F001)

CAA maps unambiguously to the albumin gene *ALB* on chromosome 4q13.3. A landmark review by Minchiotti and colleagues sequenced *ALB* across the known case series and identified **21 distinct molecular defects**: seven nonsense mutations, seven splicing changes, five frameshift/deletions, one frameshift/insertion, and one start-codon mutation. Of the characterized probands, 19 were homozygous and one was compound heterozygous, consistent with a recessive trait that is typically unmasked by consanguinity or in restricted populations. The verified quote establishes the variant-class distribution:

> *"The twenty-one causative defects include seven nonsense mutations, seven changes affecting splicing, five frame-shift/deletions, one frame-shift/insertion and one mutation in the start codon."* — [PMID: 23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/)

Most mutations are private (unique to a single family), but one—the Kayseri allele—recurs across unrelated populations:

> *"Most mutations are unique, but one, named Kayseri, is responsible for about half of the known cases."* — [PMID: 23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/)

### 2. Variant spectrum: predominantly premature-termination (null) alleles acting via loss of function (F005)

The documented pathogenic *ALB* variants are overwhelmingly premature-termination alleles that are predicted to yield no functional protein, whether through nonsense-mediated mRNA decay or production of severely truncated, misrouted polypeptides. Representative variants include:

| Variant (common name) | Location | Type | Note | PMID |
|---|---|---|---|---|
| c.228_229delAT (**Kayseri**) | Exon 3 | Frameshift → premature stop | ~50% of all cases; founder | [12028999](https://pubmed.ncbi.nlm.nih.gov/12028999/) |
| c.1A>C p.Met1Leu (**Afula**) | Exon 1 | Start-codon loss | Druze population, Galilee | [23176518](https://pubmed.ncbi.nlm.nih.gov/23176518/) |
| c.527delC (**Erzurum**) | Exon 5 | Frameshift, stop at codon 215 | — | [27346974](https://pubmed.ncbi.nlm.nih.gov/27346974/) |
| c.1098dupT p.Val367fsTer12 | Exon 9 | Frameshift/insertion | Consanguineous family | [29981851](https://pubmed.ncbi.nlm.nih.gov/29981851/) |
| c.1309A>T | — | Nonsense | — | [32881634](https://pubmed.ncbi.nlm.nih.gov/32881634/) |
| Arg114Ter (CGA>TGA) | Exon 4 | Nonsense | Recurs (Swiss, American) | [15996651](https://pubmed.ncbi.nlm.nih.gov/15996651/) |
| c.1652+1G>A | Intron 12 | Splice-site → exon-12 skipping | Consanguineous | [24627724](https://pubmed.ncbi.nlm.nih.gov/24627724/) |
| c.118+1G>A | Intron 1 | Splice-site | Iraqi newborn | [11781148](https://pubmed.ncbi.nlm.nih.gov/11781148/) |
| c.270+1G>T | Intron 3 | Splice-site | German infant | [26543026](https://pubmed.ncbi.nlm.nih.gov/26543026/) |
| Intron-12 + 3′UTR (compound het) | — | Splice + regulatory | Coronary thrombosis case | [37184254](https://pubmed.ncbi.nlm.nih.gov/37184254/) |

The frameshift mechanism is illustrated directly:

> *"causing a subsequent frame-shift with the generation of a premature stop codon, and an aberrant truncated putative protein product, p.Val367fsTer12"* — [PMID: 29981851](https://pubmed.ncbi.nlm.nih.gov/29981851/)

**Gene/protein identifiers:** HGNC:399, NCBI Gene 213, UniProt P02768, reference transcript NM_000477. One case (Albumin Locust Valley) had a completely normal coding region, suggesting a remote regulatory-element defect ([PMID: 16713595](https://pubmed.ncbi.nlm.nih.gov/16713595/)).

### 3. The adult phenotype is surprisingly mild and dominated by dyslipidemia and mild oedema (F002)

Despite near-total absence of albumin, most adults with CAA are clinically well. The consistent findings are a mild tendency to ankle oedema, asthenia, and moderate hypotension, with laboratory hyperlipidemia:

> *"The condition affects especially the lipid metabolism but apart from a possible increased risk for atherosclerotic complications, it is generally associated with mild clinical symptoms in adults."* — [PMID: 23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/)

> *"the large majority of analbuminemic subjects appear clinically well, the only consistent finding being a slight tendency to develop ankle edema. Asthenia and moderate hypotension have been recorded in several cases."* — [PMID: 115079](https://pubmed.ncbi.nlm.nih.gov/115079/)

Laboratory signatures include increased circulating cholesterol, beta-lipoproteins, and esterified fatty acids.

### 4. Pediatric CAA is a multisystem disorder with higher morbidity (F007, F002)

The perinatal/childhood window is the period of greatest risk. A 2026 genomic/phenotyping study of five children across two kindreds captured the multisystem nature of early disease:

> *"All patients presented with persistent hypoalbuminemia, early-onset edema, gastrointestinal morbidity (frequently leading to misdiagnosis as protein-losing enteropathy), antenatal complications, recurrent respiratory infections, and dyslipidemia"* — [PMID: 42311911](https://pubmed.ncbi.nlm.nih.gov/42311911/)

The authors additionally documented hemostatic and immune abnormalities and advocated individualized monitoring for infectious and thrombotic complications. An earlier case corroborates the childhood pattern of oedema plus respiratory susceptibility:

> *"A 10-year-old white boy suffering from primary analbuminaemia presented with a 6-month history of ankle oedema. From infancy he had suffered from asthma and respiratory tract infections."* — [PMID: 3983720](https://pubmed.ncbi.nlm.nih.gov/3983720/)

**Suggested HPO terms:** Hypoalbuminemia (HP:0003073), Edema (HP:0000969), Pedal edema (HP:0010741), Hypercholesterolemia (HP:0003124), Hyperlipidemia (HP:0003077), Recurrent respiratory infections (HP:0002205), Growth delay (HP:0001510), Abnormal bleeding (HP:0001928), Protein-losing enteropathy (HP:0100281), Fatigue (HP:0012378), Hypotension (HP:0002615).

### 5. The mild phenotype is explained by physiological compensation (F008)

Albumin normally provides ~75–80% of plasma colloid osmotic pressure and transports fatty acids, bilirubin, hormones, metals, and many drugs, while maintaining plasma redox balance:

> *"plays essential roles in regulating oncotic pressure, transporting endogenous and exogenous compounds, and maintaining redox balance"* — [PMID: 42931509](https://pubmed.ncbi.nlm.nih.gov/42931509/)

In CAA, the liver compensates by up-regulating non-albumin secreted proteins, and ligands are redistributed—e.g., bilirubin accumulates in the high-density lipoprotein fraction. The compensation hypothesis is stated directly:

> *"the relative absence of severe illness in analbuminaemia reflects similar compensatory mechanisms afforded by the increase in non-albumin plasma protein levels and by other metabolic adjustments"* — [PMID: 3983720](https://pubmed.ncbi.nlm.nih.gov/3983720/)

A historical series confirms that albumin's transport and nutritional roles are largely dispensable:

> *"there are now 14 reported cases of congenital analbuminemia in which serum albumin is absent or greatly reduced without clinical evidence of edema, decreased hormone levels or abnormal amino acid requirements"* — [PMID: 686645](https://pubmed.ncbi.nlm.nih.gov/686645/)

### 6. Cardiovascular/atherosclerotic complications are the main serious long-term risk (F006)

Chronic hyperlipidemia provides the mechanistic substrate for accelerated atherosclerosis. A young-adult case demonstrated the clinical reality:

> *"confirm that cardiovascular complications must be taken seriously in this pathology"* — [PMID: 37184254](https://pubmed.ncbi.nlm.nih.gov/37184254/) (35-year-old man with recurrent acute coronary syndrome/coronary thrombosis)

> *"apart from a possible increased risk for atherosclerotic complications"* — [PMID: 23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/)

### 7. Diagnosis and supportive treatment (F009)

Diagnosis rests on demonstrating near-absent serum albumin (documented values as low as 0.003 g/L; 81 mg/L; <8 g/L in neonates) with compensatory elevation of globulins and cholesterol. Serum protein electrophoresis/immunofixation shows an absent albumin band; confirmation is by *ALB* sequencing of the 14 exons (classically via SSCP/heteroduplex screening then direct sequencing). The key differential is *acquired* hypoalbuminemia:

> *"The clinical diagnosis may be challenging because of the absence of unambiguous symptoms and because hypoalbuminemia may have many causes different from a genetic lack of the protein."* — [PMID: 26543026](https://pubmed.ncbi.nlm.nih.gov/26543026/)

CAA is distinguished from nephrotic syndrome, protein-losing enteropathy, hepatic failure, and malnutrition chiefly by the **absence of proteinuria** and the germline *ALB* defect. Treatment is supportive: statins for hyperlipidemia and albumin infusion reserved for acute needs—e.g., pregnancy polyhydramnios:

> *"Our patient suffered from polyhydramnios during her pregnancy which was successfully managed with albumin transfusions and had a normal vaginal delivery"* — [PMID: 28154155](https://pubmed.ncbi.nlm.nih.gov/28154155/)

### 8. Drug pharmacokinetics are markedly altered: the free fraction of protein-bound drugs rises dramatically (F010)

Because albumin is the principal plasma drug carrier, its absence sharply increases the unbound (pharmacologically active) fraction of highly protein-bound drugs. In the Nagase analbuminemic rat, the free fraction of mycophenolic acid rose more than ten-fold:

> *"Free fractions of MPA in the control rats and NARs were 2.09 and 24.8%, respectively."* — [PMID: 26643991](https://pubmed.ncbi.nlm.nih.gov/26643991/)

> *"Dose adjustments based on the total MPA may cause unnecessary overexposure to MPA in patients with hypoalbuminemia."* — [PMID: 26643991](https://pubmed.ncbi.nlm.nih.gov/26643991/)

Loop-diuretic studies in NAR show that drug effect depends on residual globulin binding: furosemide binds albumin (and so loses efficacy), whereas azosemide, bumetanide, and torasemide bind globulins and retain activity ([PMID: 24151919](https://pubmed.ncbi.nlm.nih.gov/24151919/); [PMID: 12516076](https://pubmed.ncbi.nlm.nih.gov/12516076/)). This is the single most clinically actionable consequence of CAA: **dose highly protein-bound drugs on free rather than total concentrations.**

### 9. Epidemiology: ultra-rare, recessive, consanguinity-enriched, founder effects (F004)

> *"only about seventy cases have been reported worldwide"* — [PMID: 27346974](https://pubmed.ncbi.nlm.nih.gov/27346974/)

> *"CAA is rare, but its frequency seems to be significantly higher in restricted and minimally admixed populations."* — [PMID: 23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/)

Population frequency is well below 1 per 1,000,000 live births. Many reports arise from consanguineous families. The Kayseri allele has been found in Turkish, Amerindian, Arab, Slovak Romany, and Swedish individuals—consistent with either an ancient shared founder or a recurrent mutational hotspot.

### 10. Etiology is purely genetic; animal models and the AFP analogy (F003, F011)

CAA is a monogenic Mendelian trait with no environmental, toxic, infectious, lifestyle, or epigenetic cause, and no validated modifier genes or protective alleles. Phenotypic variability (severe neonatal vs. asymptomatic adult) is attributed to developmental stage and compensation rather than defined modifiers. The gene-family-redundancy concept is supported by the analogy to alpha-fetoprotein, a homologous albumin-family protein whose congenital deficiency is likewise benign:

> *"Because it is homologous to albumin, congenital deficiency of alpha-fetoprotein may be analogous to analbuminemia, a benign genetic trait."* — [PMID: 1379776](https://pubmed.ncbi.nlm.nih.gov/1379776/)

The **Nagase analbuminemic rat (NAR)**, arising from a spontaneous *Alb* splice-site mutation in Sprague-Dawley rats, is the principal model. It recapitulates age-progressive hyperlipidemia and compensatory hepatic protein synthesis:

> *"All inbred strains of analbuminemic rats showed hyperlipidemia progressing with age"* — [PMID: 3325299](https://pubmed.ncbi.nlm.nih.gov/3325299/)

> *"The liver, in an apparent compensatory response, increases synthesis of a group of secreted proteins defending plasma pi."* — [PMID: 10432383](https://pubmed.ncbi.nlm.nih.gov/10432383/) — NAR is described as "the only known condition in which transcription of both positive and negative acute phase proteins are increased simultaneously."

A TALEN-engineered knockout mouse mirrors the benign human trait:

> *"The resulting Alb(-/-) strains are analbuminemic but healthy."* — [PMID: 25654695](https://pubmed.ncbi.nlm.nih.gov/25654695/)

---

## Section-by-Section Characterization

### 1. Disease Information
CAA is an inborn error in which albumin, the most abundant plasma protein, is absent or severely reduced owing to biallelic *ALB* mutation. **Identifiers:** OMIM #616000; MONDO:0014449; Orphanet ORPHA:88918; MeSH "Analbuminemia." (Note: older literature cites OMIM #103600, an earlier/overlapping entry.) **Synonyms:** analbuminemia, congenital analbuminaemia, CAA, primary analbuminemia, hereditary analbuminemia. The information is aggregated at the disease level from case reports, small case series, molecular-genetic studies, and animal models—not from large EHR/individual-patient datasets (consistent with ultra-rarity).

### 2. Etiology
**Primary cause:** purely genetic—biallelic LoF variants in *ALB* (F001, F011). **Genetic risk factors:** homozygosity/compound heterozygosity for *ALB* null alleles; consanguinity and membership of restricted/founder populations markedly raise risk (F004). **Environmental risk factors:** none established. **Protective factors:** none genetically defined; a lipid-lowering diet may mitigate (but not cause) the secondary hyperlipidemia. **Gene–environment interactions:** none established; phenotype severity is modulated by developmental stage and compensation, not by exposures.

### 3. Phenotypes
Core phenotypes with suggested HPO terms and frequency qualifiers:

| Phenotype | HPO | Type | Onset | Frequency |
|---|---|---|---|---|
| Hypoalbuminemia | HP:0003073 | Lab abnormality | Congenital | Obligate (100%) |
| Hyperlipidemia / hypercholesterolemia | HP:0003077 / HP:0003124 | Lab abnormality | Childhood–adult | Very frequent/consistent |
| Pedal/ankle oedema | HP:0010741 | Clinical sign | Any age | Frequent (mild) |
| Fatigue/asthenia | HP:0012378 | Symptom | Adult | Occasional |
| Hypotension | HP:0002615 | Clinical sign | Adult | Occasional |
| Recurrent respiratory infections | HP:0002205 | Clinical sign | Childhood | Subset |
| Protein-losing enteropathy mimic / GI morbidity | HP:0100281 | Clinical sign | Pediatric | Pediatric cohort |
| Growth delay | HP:0001510 | Physical | Childhood | Subset |
| Abnormal coagulation/bleeding | HP:0001928 | Lab abnormality | Pediatric | Subset |

**Severity:** generally mild in adults, variable/moderate-severe in neonates. **Progression:** stable/chronic in adults; dyslipidemia is progressive. **QoL:** typically preserved in adults; pediatric/perinatal morbidity may impair well-being.

### 4. Genetic/Molecular Information
**Causal gene:** *ALB* (OMIM gene 103600 → phenotype #616000; HGNC:399; NCBI Gene 213; UniProt P02768; NM_000477). **Variant classification:** nearly all reported variants are pathogenic null alleles (nonsense, frameshift, splice-site, start-codon). **Variant type/class distribution** (per 2013 review): 7 nonsense, 7 splicing, 5 frameshift/deletion, 1 frameshift/insertion, 1 start-codon (F001/F005). **Allele frequency:** individually extremely rare; absent or near-absent in gnomAD in homozygous state. **Origin:** germline, recessive. **Functional consequence:** loss of function (no/absent protein). **Modifier genes:** none validated. **Epigenetic/chromosomal abnormalities:** none implicated (one case points to a possible remote regulatory-element defect, [PMID: 16713595](https://pubmed.ncbi.nlm.nih.gov/16713595/)).

### 5. Environmental Information
No environmental, lifestyle, or infectious agent causes or triggers CAA (F011). Diet does not cause disease; dietary lipid management can modulate the secondary dyslipidemia. Not applicable: toxins, radiation, occupational exposure, infectious agents.

### 6. Mechanism / Pathophysiology — Causal Chain

```
1. Biallelic LoF variant in ALB (4q13.3; nonsense/frameshift/splice/start-codon)
   → results in no functional albumin mRNA/protein (via NMD or truncation)
2. Loss of hepatocyte albumin secretion
   → leads to near-absent serum albumin (<1 g/L)
3. Absent albumin  →  branches:
   ├── (A) Loss of ~75–80% of plasma oncotic pressure
   │        → reduced colloid osmotic pressure (pi)
   │        → (i) mild interstitial fluid shift → bilateral ankle oedema
   │        → (ii) sensed by hepatocytes → COMPENSATION:
   │                ↑ transcription of non-albumin secreted proteins
   │                (globulins, transferrin, fibrinogen, apoA-I)
   │                → partial restoration of pi → mild, not severe, oedema
   │        → (iii) low pi stimulates hepatic lipogenesis (↑ACC, ↑FAS)
   │                + reduced lipoprotein catabolism
   │                → hypercholesterolemia / hyperlipidemia
   │                → (long term) atherosclerosis → coronary thrombosis/ACS
   ├── (B) Loss of ligand-transport function
   │        → ligands (fatty acids, bilirubin, hormones) redistributed
   │          onto lipoproteins/globulins → clinically tolerated
   │        → drugs: unbound (free) fraction rises sharply
   │          → altered pharmacokinetics/pharmacodynamics (dosing risk)
   └── (C) Loss of redox-buffering/antioxidant capacity (inferred)
            → reduced plasma antioxidant reserve (mechanistic, not fully
              demonstrated in CAA patients)
```

**Molecular pathways/processes:** hepatic protein secretion (secretory pathway), de novo lipogenesis (acetyl-CoA carboxylase, fatty acid synthase; GO:0006633 fatty acid biosynthetic process), and regulation of oncotic/osmotic homeostasis. The hyperlipidemia mechanism was dissected in NAR vs. nephrotic rats: both show increased hepatic triglyceride secretion driven by reduced π, but proteinuria (absent in CAA/NAR) is required for the *catabolic* lipoprotein defect ([PMID: 7723242](https://pubmed.ncbi.nlm.nih.gov/7723242/); [PMID: 1465061](https://pubmed.ncbi.nlm.nih.gov/1465061/); [PMID: 7611250](https://pubmed.ncbi.nlm.nih.gov/7611250/)). **Cell type:** hepatocyte (CL:0000182) is the central cell. **Protein dysfunction:** complete loss of function (no protein), not misfolding/aggregation/gain of function. **Immune involvement:** secondary (recurrent infections, immune abnormalities in pediatric cohort) rather than primary autoimmunity/immunodeficiency.

**Suggested GO/CL terms:** GO:0005576 (extracellular region), GO:0008289 (lipid binding), GO:0006633 (fatty acid biosynthesis), transport processes; CL:0000182 (hepatocyte).

### 7. Anatomical Structures Affected
**Primary site of defect:** liver (hepatocytes)—the organ of albumin synthesis (UBERON:0002107 liver; CL:0000182 hepatocyte). **Systemically affected compartment:** blood plasma (UBERON:0001969). **Secondary involvement:** cardiovascular system (atherosclerosis), lower-limb soft tissue (oedema), gastrointestinal tract and respiratory tract (pediatric morbidity). **Subcellular:** the hepatocyte secretory pathway—endoplasmic reticulum (GO:0005783) and Golgi (GO:0005794)—is where albumin is normally synthesized and secreted. **Lateralization:** oedema is bilateral/symmetric.

### 8. Temporal Development
**Onset:** congenital (albumin deficiency present from birth); clinical recognition ranges from neonatal to incidental adult diagnosis. **Onset pattern:** chronic/insidious. **Progression:** adult course is stable/chronic-lifelong; secondary hyperlipidemia is slowly progressive and age-dependent (demonstrated in NAR, [PMID: 3325299](https://pubmed.ncbi.nlm.nih.gov/3325299/)). **Critical period:** the perinatal/childhood window is the time of highest vulnerability and intervention opportunity (F002, F007). **Course pattern:** progressive (lipids) on a stable baseline; lifelong. **Remission:** none spontaneous; the genetic defect is permanent.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** complete for the biochemical trait (hypoalbuminemia) in biallelic carriers; clinical expressivity variable. **Expressivity:** variable (severe neonatal to asymptomatic adult). **Anticipation:** not applicable (not a repeat-expansion disorder). **Founder effects:** yes—Kayseri (~50% of cases) and Afula (Druze). **Consanguinity:** frequently present; a major risk amplifier. **Carrier frequency:** unknown but very low; heterozygotes are clinically normal (mild hypoalbuminemia at most). **Epidemiology:** ~70 cases worldwide; prevalence well below 1/1,000,000. **Sex ratio:** no strong sex bias reported (autosomal). **Geographic/ethnic distribution:** enriched in restricted, minimally admixed, consanguineous populations (Turkish, Arab, Druze, Romany, Amerindian, and sporadic European cases).

### 10. Diagnostics
**Laboratory:** serum albumin <1 g/L (down to 0.003 g/L) with elevated globulins and cholesterol (LOINC: serum albumin 1751-7). **Serum protein electrophoresis/immunofixation:** absent albumin band. **Biomarkers:** near-absent albumin plus a dyslipidemia profile. **Confirmatory genetic testing:** single-gene *ALB* sequencing (all 14 exons + splice junctions + UTRs), historically preceded by SSCP/heteroduplex screening; WES/WGS or a hypoalbuminemia/liver gene panel are reasonable first-line in the genomic era. Carrier testing via targeted *ALB* sequencing enables counseling ([PMID: 23176518](https://pubmed.ncbi.nlm.nih.gov/23176518/)). **Not applicable:** karyotype, FISH, CMA, mtDNA, repeat-expansion testing. **Differential diagnosis:** acquired hypoalbuminemia—nephrotic syndrome (proteinuria present), protein-losing enteropathy, hepatic failure, severe malnutrition, burns. CAA is distinguished by absent proteinuria + germline *ALB* defect ([PMID: 26543026](https://pubmed.ncbi.nlm.nih.gov/26543026/)). A reported pitfall is concurrent acute glomerulonephritis masking the diagnosis ([PMID: 18791744](https://pubmed.ncbi.nlm.nih.gov/18791744/)). **Screening:** not part of routine newborn screening; cascade/carrier testing is appropriate in affected families.

### 11. Outcome / Prognosis
**Survival/life expectancy:** generally normal in adults who survive the perinatal/childhood period; no established reduction in adult life expectancy. **Mortality:** increased perinatal/childhood morbidity and mortality is reported ([PMID: 23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/)). **Morbidity:** mild in adults (oedema, fatigue); multisystem in children. **Principal long-term threat:** accelerated atherosclerosis/coronary disease from chronic dyslipidemia ([PMID: 37184254](https://pubmed.ncbi.nlm.nih.gov/37184254/)). **Prognostic factors:** age (perinatal most vulnerable), lipid control, and vigilance for thrombotic/infectious complications. **QoL:** typically preserved in adults.

### 12. Treatment
Management is **supportive**; no curative therapy exists. **Pharmacotherapy:** lipid-lowering agents (statins / HMG-CoA reductase inhibitors; NCIT C1456) for secondary hyperlipidemia. **Albumin replacement:** intravenous human albumin infusion (NCIT C29031 Albumin Human) reserved for acute indications (e.g., polyhydramnios in pregnancy, [PMID: 28154155](https://pubmed.ncbi.nlm.nih.gov/28154155/)); not required as chronic therapy in most adults. **Pharmacogenomics/dosing:** dose highly protein-bound drugs on free (unbound) concentrations, because the free fraction rises dramatically (F010; [PMID: 26643991](https://pubmed.ncbi.nlm.nih.gov/26643991/)); prefer diuretics that act via globulin binding (torasemide/azosemide/bumetanide) over furosemide. **Supportive care:** monitoring for thrombotic and infectious complications, especially in children ([PMID: 42311911](https://pubmed.ncbi.nlm.nih.gov/42311911/)). **Advanced therapeutics (gene/RNA/cell therapy):** none clinically available; theoretically plausible but not developed given the mild phenotype. **Experimental:** no registered CAA-specific trials identified.

### 13. Prevention
**Primary prevention:** not applicable (genetic/congenital); genetic counseling for consanguineous couples and known-carrier families reduces recurrence risk. **Secondary prevention:** early detection of affected neonates to anticipate perinatal morbidity; lipid screening and management to prevent atherosclerotic complications (tertiary prevention). **Genetic screening:** carrier testing and prenatal/preimplantation diagnosis feasible via targeted *ALB* sequencing in known families. **Immunization/public-health/environmental measures:** not applicable (non-infectious, non-environmental). **Counseling:** autosomal-recessive recurrence risk (25% per pregnancy for carrier couples); emphasize benign adult prognosis with careful drug dosing.

### 14. Other Species / Natural Disease
**Taxonomy/orthologues:** rat *Alb* (NCBI Gene 24186; *Rattus norvegicus*, NCBI Taxon 10116) and mouse *Alb* (NCBI Gene 11657; *Mus musculus*). **Natural disease:** spontaneous analbuminemia occurs in the Nagase analbuminemic rat (a splice-site *Alb* mutant). No established spontaneous companion-animal analbuminemia is catalogued in OMIA. **Comparative biology:** albumin belongs to the albumin/AFP/vitamin-D-binding-protein/afamin gene family on chromosome 4; loss of the homologous alpha-fetoprotein is likewise a benign trait ([PMID: 1379776](https://pubmed.ncbi.nlm.nih.gov/1379776/)), supporting gene-family redundancy. **Zoonotic potential:** none (non-transmissible genetic trait).

### 15. Model Organisms
**Nagase analbuminemic rat (NAR):** spontaneous splice-site *Alb* mutant in Sprague-Dawley background; the Rat Genome Database (RGD) model of albumin deficiency. Recapitulates age-progressive hyperlipidemia ([PMID: 3325299](https://pubmed.ncbi.nlm.nih.gov/3325299/)) and compensatory hepatic protein synthesis ([PMID: 10432383](https://pubmed.ncbi.nlm.nih.gov/10432383/)); extensively used to study altered drug pharmacokinetics ([PMID: 26643991](https://pubmed.ncbi.nlm.nih.gov/26643991/), [PMID: 24151919](https://pubmed.ncbi.nlm.nih.gov/24151919/), [PMID: 12516076](https://pubmed.ncbi.nlm.nih.gov/12516076/), [PMID: 31492695](https://pubmed.ncbi.nlm.nih.gov/31492695/)). **Alb⁻/⁻ mouse:** TALEN-engineered knockout; "analbuminemic but healthy," used for human-albumin metabolism and albumin-based drug pharmacokinetics ([PMID: 25654695](https://pubmed.ncbi.nlm.nih.gov/25654695/)). **Phenotype recapitulation:** both models faithfully reproduce the biochemical trait, hyperlipidemia, and compensatory protein synthesis; they do not require the pediatric multisystem complications seen in some human infants (a limitation). **Applications:** oncotic-pressure physiology, hepatic lipogenesis, protein-binding pharmacokinetics, and albumin-drug carrier studies.

---

## Mechanistic Model / Interpretation

CAA is best understood as a **compensated null-allele disorder**. A single lesion—biallelic loss of functional albumin—propagates into two clinically dominant downstream branches (oncotic and transport), each buffered by compensation:

| Lost albumin function | Immediate consequence | Compensation | Residual clinical effect |
|---|---|---|---|
| Oncotic pressure (~75–80% of plasma π) | ↓ colloid osmotic pressure | ↑ hepatic synthesis of globulins/transferrin/fibrinogen/apoA-I | Mild bilateral oedema |
| Oncotic → lipid homeostasis | ↑ hepatic lipogenesis (↑ACC/FAS), ↓ lipoprotein catabolism | Partial, incomplete | Hyperlipidemia → atherosclerosis (main long-term risk) |
| Ligand transport (FA, bilirubin, hormones) | Carrier loss | Redistribution onto lipoproteins/globulins | Clinically tolerated |
| Drug transport | ↑ free drug fraction | None effective | Altered PK/PD → dosing hazard |
| Redox buffering (inferred) | ↓ antioxidant reserve | Uncertain | Not clearly demonstrated in CAA |

The central insight is that **albumin's functions are individually dispensable because each is partially substitutable**, whereas no substitute exists for protein-binding of drugs—explaining why altered pharmacokinetics is the most reproducible and clinically actionable feature. The liver's capacity to simultaneously up-regulate both positive and negative acute-phase proteins in response to low oncotic pressure (a state otherwise seen only in analbuminemia; [PMID: 10432383](https://pubmed.ncbi.nlm.nih.gov/10432383/)) is the physiological lynchpin of the mild phenotype.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [23612153](https://pubmed.ncbi.nlm.nih.gov/23612153/) | *Congenital analbuminaemia: molecular defects and biochemical/clinical aspects* | Core review: variant spectrum, Kayseri ~50%, mild adult phenotype, atherosclerotic risk, population enrichment |
| [27346974](https://pubmed.ncbi.nlm.nih.gov/27346974/) | *A nucleotide deletion and frame-shift…* | ~70 cases worldwide; Erzurum variant |
| [12028999](https://pubmed.ncbi.nlm.nih.gov/12028999/) | *Molecular diagnosis of analbuminemia (Kayseri)* | Defines founder Kayseri c.228_229delAT |
| [42311911](https://pubmed.ncbi.nlm.nih.gov/42311911/) | *Pediatric CAA multisystem phenotyping* | Multisystem pediatric phenotype; PLE mimicry; coagulation/immune signatures |
| [3983720](https://pubmed.ncbi.nlm.nih.gov/3983720/) | *Analbuminaemia—South African patient* | Childhood oedema + infections; compensation hypothesis; bilirubin on HDL |
| [115079](https://pubmed.ncbi.nlm.nih.gov/115079/) | *Analbuminemia (quantitative albumin variant)* | Mild signs: ankle oedema, asthenia, hypotension; dyslipidemia |
| [686645](https://pubmed.ncbi.nlm.nih.gov/686645/) | *Hereditary disorders of albumin synthesis* | Albumin's transport/nutritional roles are dispensable |
| [10432383](https://pubmed.ncbi.nlm.nih.gov/10432383/) | *Coordinate augmentation of liver secretory proteins* | Compensatory hepatic synthesis (NAR) |
| [3325299](https://pubmed.ncbi.nlm.nih.gov/3325299/) | *Analbuminemic inbred rat strains* | Age-progressive hyperlipidemia in NAR |
| [25654695](https://pubmed.ncbi.nlm.nih.gov/25654695/) | *Albumin-deficient mouse models* | Alb⁻/⁻ mouse "analbuminemic but healthy" |
| [26643991](https://pubmed.ncbi.nlm.nih.gov/26643991/) | *MPA PK in NAR* | Free drug fraction 2.09%→24.8%; dosing guidance |
| [37184254](https://pubmed.ncbi.nlm.nih.gov/37184254/) | *CAA with coronary thrombosis* | Cardiovascular risk in young adult; compound-het variants |
| [28154155](https://pubmed.ncbi.nlm.nih.gov/28154155/) | *Pregnancy in CAA* | Albumin transfusion for polyhydramnios; drug-binding concerns |
| [26543026](https://pubmed.ncbi.nlm.nih.gov/26543026/) | *Novel splicing mutation (German infant)* | Diagnostic challenge; differential diagnosis |
| [1379776](https://pubmed.ncbi.nlm.nih.gov/1379776/) | *Congenital deficiency of alpha-fetoprotein* | Gene-family redundancy; benign-trait analogy |
| [7723242](https://pubmed.ncbi.nlm.nih.gov/7723242/) / [1465061](https://pubmed.ncbi.nlm.nih.gov/1465061/) | *Lipid metabolism in NAR vs nephrotic rats* | Mechanism of hyperlipidemia; proteinuria required for catabolic defect |
| [42931509](https://pubmed.ncbi.nlm.nih.gov/42931509/) | *Functional heterogeneity of HSA* | Defines albumin's normal functions (oncotic, transport, redox) |
| [24151919](https://pubmed.ncbi.nlm.nih.gov/24151919/) / [12516076](https://pubmed.ncbi.nlm.nih.gov/12516076/) | *Diuretic PK/PD in NAR* | Globulin- vs albumin-bound diuretic efficacy |

---

## Limitations and Knowledge Gaps

- **Small evidence base:** With only ~70 reported cases, all clinical generalizations rest on case reports and small series; no prospective natural-history cohort exists. Quantitative frequency estimates for individual phenotypes (e.g., what fraction develop coronary disease) are not well defined.
- **Perinatal mortality quantification:** Increased perinatal/childhood morbidity is repeatedly asserted but not quantified in population terms.
- **Modifier biology unknown:** The molecular basis of variable expressivity (severe neonate vs. asymptomatic adult) is not established; no modifier genes identified.
- **Redox/antioxidant branch is inferred:** Loss of albumin's redox-buffering role is mechanistically plausible but not directly demonstrated to produce clinical consequences in CAA patients.
- **One unexplained case:** Albumin Locust Valley has a normal coding region, implying an uncharacterized regulatory mechanism ([PMID: 16713595](https://pubmed.ncbi.nlm.nih.gov/16713595/)).
- **Model gaps:** NAR and Alb⁻/⁻ mouse capture biochemistry and pharmacokinetics but not the pediatric multisystem (GI/immune/coagulation) complications; carrier frequency and gnomAD-based population estimates were not directly computed in this investigation.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify population genetics:** Query gnomAD for *ALB* LoF allele frequencies to estimate carrier frequency and predicted birth prevalence, and to assess whether Kayseri represents a single founder haplotype vs. a recurrent mutational hotspot (haplotype analysis across ethnic groups).
2. **Build a natural-history registry:** Pool the ~70 published cases into a structured dataset (variant, age, phenotype, lipids, cardiovascular events, perinatal outcome) to derive phenotype frequencies and genotype–phenotype correlations.
3. **Cardiovascular risk study:** Systematically assess carotid intima-media thickness/coronary calcium and lipid trajectories in adult CAA patients to quantify atherosclerotic risk and test whether early statin therapy alters outcomes.
4. **Pharmacokinetic guidance:** Develop a free-drug-dosing reference for commonly used, highly protein-bound medications in CAA, extrapolating from NAR data and validating with patient free-concentration measurements.
5. **Molecular characterization of regulatory cases:** Pursue WGS/functional assays for coding-normal cases (e.g., Albumin Locust Valley) to identify regulatory-element lesions.
6. **Model refinement:** Phenotype the pediatric-relevant systems (coagulation, immunity, GI) in Alb⁻/⁻ mice/NAR to determine whether the childhood multisystem picture is modeled or is human-specific.


## Artifacts

- [OpenScientist final report](Congenital_Analbuminemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Congenital_Analbuminemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 30 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 22 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 12 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100281` (2 mentions) - the report calls it "Protein-losing enteropathy mimic / GI morbidity"; HP calls it **Chronic colitis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010741` (2 mentions) - the report calls it "Pedal/ankle oedema"; HP calls it **Pedal edema**, and lists "Pedal oedema" among its other names
- `HP:0001928` (2 mentions) - the report calls it "Abnormal coagulation/bleeding"; HP calls it **Abnormality of coagulation**, and lists "Abnormal blood coagulation studies" among its other names
- `HP:0012378` (2 mentions) - the report calls it "Fatigue/asthenia"; HP calls it **Fatigue**
- `GO:0006633` (2 mentions) - the report calls it "fatty acid biosynthesis"; GO calls it **fatty acid biosynthetic process**, and lists "fatty acid biosynthesis" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.