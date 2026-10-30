---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T03:39:56.331915'
end_time: '2026-10-27T03:53:51.491338'
duration_seconds: 835.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Immune Dysregulation With Immunodeficiency Due To AIOLOS Haploinsufficiency
  mondo_id: MONDO:0979328
  category: Mendelian
  causal_genes: IKZF3
  omim_id: not recorded
  synonyms: not recorded
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
citation_count: 10
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 21
  relevance_assessed: 12
  on_topic: 9
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0005550
    reported_labels:
    - B-cell lymphoproliferation
    ontology_label: Chronic lymphatic leukemia
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Immune_Dysregulation_With_Immunodeficiency_Due_To_AIOLOS_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Immune_Dysregulation_With_Immunodeficiency_Due_To_AIOLOS_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immune Dysregulation With Immunodeficiency Due To AIOLOS Haploinsufficiency
- **MONDO ID:** MONDO:0979328 (if available)
- **Causal gene(s):** IKZF3
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Immune Dysregulation With Immunodeficiency Due To AIOLOS Haploinsufficiency** covering all of the
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

# Immune Dysregulation With Immunodeficiency Due To AIOLOS Haploinsufficiency (MONDO:0979328)

**Causal gene: *IKZF3* (encoding the Ikaros-family zinc-finger transcription factor AIOLOS)**

---

## Summary

**Immune Dysregulation With Immunodeficiency Due To AIOLOS Haploinsufficiency** (MONDO:0979328) is a rare, autosomal-dominant **inborn error of immunity (IEI)** caused by heterozygous germline variants in ***IKZF3***, the gene encoding the lymphoid-restricted Ikaros-family zinc-finger transcription factor **AIOLOS**. Despite the disease name emphasizing "haploinsufficiency," the broader *IKZF3*-associated disease encompasses two mechanistically distinct classes of variant: (1) **DNA-binding-domain dominant-negative variants** (G159R, N160S, G191R) that abolish DNA binding and pericentromeric heterochromatin targeting and poison wild-type AIOLOS, and (2) **true haploinsufficiency variants** (E82K, Q402*) that reduce functional AIOLOS dosage via protein instability or truncation. Both converge on defective lymphocyte transcriptional programs and produce a combined immunodeficiency with immune dysregulation.

Clinically, affected individuals present with **recurrent sinopulmonary and opportunistic infections** (including *Pneumocystis jirovecii* pneumonia), **hypogammaglobulinemia with abnormal B- and T-cell development**, **autoimmunity and allergy**, and an elevated risk of **B-cell malignancy** (chronic lymphocytic leukemia, CLL). Severity and penetrance are variant-dependent: the original DNA-binding dominant-negative N160S variant was fully penetrant and segregated through a multigeneration family, whereas the haploinsufficiency variants (E82K, Q402*) show **incomplete clinical penetrance**. A fatal case of disseminated vaccine-derived rubella virus (VDRV) granulomatous disease underscores that live attenuated vaccines are contraindicated and that prognosis can be grave.

The disease sits within the broader **Ikaros zinc-finger family (IKZF1/Ikaros, IKZF2/Helios, IKZF3/Aiolos)** spectrum of IEIs that share molecular readouts — loss of DNA binding, loss of pericentromeric targeting, and disrupted dimerization/NuRD-complex function. The human phenotype has been **recapitulated in *Ikzf3* mouse models**, including an Aiolos-null model that develops SLE-like autoimmunity and a humanized knock-in carrying the patient N160S-equivalent mutation. Management follows general combined-immunodeficiency standards (immunoglobulin replacement, antimicrobial prophylaxis, immunomodulation, and allogeneic HSCT for severe phenotypes), with malignancy surveillance, genetic counseling, and strict avoidance of live vaccines.

---

## Key Findings

### Finding 1 — The disease is caused by heterozygous *IKZF3* (AIOLOS) variants

AIOLOS-associated immunodeficiency (MONDO:0979328) is caused by **germline heterozygous variants in *IKZF3***, which encodes the Ikaros-family C2H2 zinc-finger transcription factor **AIOLOS**. The original kindred, described by Kuehn et al. (2021), carried the missense variant **AIOLOS p.N160S** and presented as a novel combined immunodeficiency with T- and B-cell involvement, *Pneumocystis jirovecii* pneumonia, and/or CLL. The N160S mutant **failed DNA binding and pericentromeric targeting** and acted as a **dominant negative over wild-type AIOLOS but not wild-type IKAROS**; the variant was **fully penetrant** in that family.

> "Here we describe a novel combined immunodeficiency due to an IKZF3 mutation in a family presenting with T and B cell involvement, Pneumocystis jirovecii pneumonia, and/or chronic lymphocytic leukemia." — [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)

> "The mutant was fully penetrant and had a dominant-negative effect over WT AIOLOS but not WT IKAROS." — [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)

**Evidence source:** human clinical + in vitro functional studies.

### Finding 2 — Two mechanistic classes of AIOLOS variants: DNA-binding dominant-negative vs. haploinsufficiency

A review by Yamashita & Morio (2024) and the mechanistic study by Kuehn et al. (2024) establish **two distinct variant classes**:

| Variant class | Variants | Protein domain affected | Mechanism | Penetrance |
|---|---|---|---|---|
| **DNA-binding loss-of-function (dominant-negative)** | G159R, N160S, G191R | DNA-binding zinc fingers (ZF2–3) | Abolish DNA binding and pericentromeric targeting; poison WT AIOLOS | Full (N160S) |
| **Haploinsufficiency** | E82K (missense), Q402* (truncating) | Protein-stability domain (E82K); dimerization ZF5–6 lost (Q402*) | Reduced AIOLOS dosage via instability or truncation | Incomplete |

Notably, Kuehn et al. (2024) reported **9 individuals from 3 unrelated families** carrying Q402* or E82K that cause haploinsufficiency **through different mechanisms**. The Q402* truncation lacks the ZF5–6 dimerization domain yet still homodimerizes with WT AIOLOS and **negatively regulates DNA binding through ZF1** — a newly recognized AIOLOS function. E82K affects a **redefined protein-stability domain**.

> "heterozygous missense loss-of-function variants within the DNA-binding domain of the IKZF3 gene (G159R, N160S, and G191R) have been identified in patients with inborn errors of immunity (IEI). Additionally, a missense and a truncating variant (E82K and Q402X) leading to the AIOLOS haploinsufficiency have been documented." — [PMID: 38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/)

> "we report on 9 individuals from 3 unrelated families carrying AIOLOS variants Q402* or E82K, which led to AIOLOS haploinsufficiency through different mechanisms of action." — [PMID: 38015619](https://pubmed.ncbi.nlm.nih.gov/38015619/)

> "Patients with AIOLOS haploinsufficiency showed hypogammaglobulinemia, recurrent infections, autoimmunity, and allergy, but with incomplete clinical penetrance." — [PMID: 38015619](https://pubmed.ncbi.nlm.nih.gov/38015619/)

**Evidence source:** human clinical + in vitro functional studies.

### Finding 3 — *Ikzf3* mouse models recapitulate immunodeficiency and SLE-like autoimmunity

Aiolos-null mice develop **systemic lupus erythematosus (SLE)-like disease** with anti-dsDNA antibodies, immune-complex–mediated glomerulonephritis, B-cell hyperproliferation, elevated B-cell activation markers, and spontaneous germinal centers (Sun et al., 2003). A **knock-in murine model carrying the human N160S-equivalent mutation recapitulated the human immunophenotype** (Kuehn et al., 2021), validating causality.

> "mice lacking the zinc finger transcription factor Aiolos develop the symptoms of human systemic lupus erythematosus (SLE), which is characterized by the production of anti-dsDNA Ab and immune complex-mediated glomerulonephritis." — [PMID: 12574333](https://pubmed.ncbi.nlm.nih.gov/12574333/)

> "The human immunophenotype was recapitulated in a murine model carrying the corresponding human mutation." — [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)

**Evidence source:** model organism (mouse).

### Finding 4 — Clinical phenotype: recurrent infections, immune dysregulation, and malignancy risk

The majority of individuals with AIOLOS-associated IEI manifest **recurrent sinopulmonary infections** plus various bacterial and viral infections. Key documented features across cases:

- **Opportunistic infection** (*Pneumocystis jirovecii* pneumonia) and **progression to CLL** in the index N160S family (Kuehn 2021).
- A **de novo G191R** pediatric patient (age 1 y 4 mo) with recurrent infections, diarrhea, failure to thrive, decreased T lymphocytes and immunoglobulins, and reduced recent thymic emigrants among naive CD4 T cells (Shi 2024).
- **Haploinsufficiency** (E82K, Q402*) patients with hypogammaglobulinemia, recurrent infections, autoimmunity, and allergy (incomplete penetrance; Kuehn 2024).
- A **fatal disseminated vaccine-derived rubella virus (VDRV)** granulomatous disease with multi-organ failure and CNS involvement in an *IKZF3*-mutant patient (Zhou 2026).

> "The majority of individuals with AIOLOS-associated IEI manifest recurrent sinopulmonary infections, as well as various bacterial and viral infections." — [PMID: 38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/)

> "we evaluated a 1-year-4-month-old female patient presenting with recurrent infections, diarrhea, and failure to thrive. Laboratory investigations revealed decreased T lymphocyte and immunoglobulin levels." — [PMID: 38758229](https://pubmed.ncbi.nlm.nih.gov/38758229/)

> "a case of disseminated granulomatous disease associated with live attenuated vaccine-derived rubella virus (VDRV) in an immunodeficient patient who subsequently developed fatal multi-organ failure, including neurological deficits, with VDRV detected in the cerebrospinal fluid" — [PMID: 41746515](https://pubmed.ncbi.nlm.nih.gov/41746515/)

**Evidence source:** human clinical.

### Finding 5 — AIOLOS disease sits within the Ikaros-family (IKZF1/2/3) spectrum of IEIs

Germline mutations across the Ikaros zinc-finger family cause phenotypically overlapping IEIs:

- **IKZF1 (Ikaros)** haploinsufficiency causes autosomal-dominant CVID (e.g., p.His167Tyr; confirmed deleterious via impaired pericentromeric heterochromatin localization and EMSA — a haploinsufficiency mechanism; Stojkic 2024).
- **IKZF2 (Helios)** monoallelic mutations cause immune dysregulation (SLE, ITP, EBV-HLH) with hypogammaglobulinemia and decreased Tfh/NK cells; mutants cannot homodimerize/bind DNA and show aberrant NuRD-complex interactions (Shahin 2022).
- **IKZF3 (AIOLOS)** causes the present disease.

The **shared molecular readouts** are loss of DNA binding, loss of pericentromeric (heterochromatin) targeting, and disrupted dimerization/NuRD-complex function.

> "whole genome sequencing revealed a novel, pathogenic c.499C > T: p.His167Tyr variant in IKZF1 ... Functional testing done through pericentromeric heterochromatin localization and light shift chemiluminescent electrophoretic mobility shift assay confirmed the variant's deleterious effect via a haploinsufficiency mechanism." — [PMID: 38734037](https://pubmed.ncbi.nlm.nih.gov/38734037/)

> "germline mutations in IKZF1 and IKZF3 encoding Ikaros and Aiolos have recently been identified in patients with phenotypically similar immunodeficiency syndromes" — [PMID: 34920454](https://pubmed.ncbi.nlm.nih.gov/34920454/)

> "Functional assays revealed the inability of HeliosR291X to homodimerize and bind target DNA as dimers." — [PMID: 34920454](https://pubmed.ncbi.nlm.nih.gov/34920454/)

**Evidence source:** human clinical + in vitro.

### Finding 6 — AIOLOS molecular function and the mechanistic causal chain

AIOLOS/IKZF3 is a **C2H2 zinc-finger transcription factor highly expressed in the lymphoid lineage**, critical for lymphocyte differentiation and development. Mechanistically it (i) binds DNA via its central zinc fingers, (ii) homodimerizes/heterodimerizes (with IKAROS) via C-terminal zinc fingers, (iii) targets pericentromeric heterochromatin, and (iv) operates with the **NuRD chromatin-remodeling complex**. Disease variants in the DNA-binding domain (N160S, G159R, G191R) abolish DNA binding and pericentromeric targeting and act dominant-negatively over WT AIOLOS; haploinsufficiency variants (E82K, Q402*) reduce dosage. Downstream, AIOLOS **positively regulates CXCR3 on Th1 cells** via an IFN-γ/STAT1 feedback loop (Leonard 2024), **restrains intestinal intraepithelial lymphocyte activation** (Yomogida 2024), and shapes **human Th17 functional states** together with Eos/IKZF (Cerboni 2026).

> "In vitro studies demonstrated that the mutant protein failed DNA binding and pericentromeric targeting." — [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)

> "Patients carrying the AIOLOS p.N160S heterozygous variant displayed impaired humoral responses, abnormal B cell development (high percentage of CD21low B cells and negative CD23 expression), and abrogated CD40 responses." — [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)

> "we identify the Ikaros zinc finger (IkZF) transcription factor Aiolos (Ikzf3) as an additional positive regulator of CXCR3 both in vitro and in vivo using a murine model of influenza virus infection." — [PMID: 39560988](https://pubmed.ncbi.nlm.nih.gov/39560988/)

**Evidence source:** human clinical + in vitro + model organism.

### Finding 7 — Autosomal dominant inheritance, variable penetrance; ultra-rare, both familial and de novo

AIOLOS-associated disease is **autosomal dominant**, caused by heterozygous (monoallelic) *IKZF3* germline variants. Both inherited and de novo origins are documented:

- **N160S** segregated through a multigeneration family and was fully penetrant (Kuehn 2021).
- **E82K and Q402*** were reported in 9 individuals across 3 unrelated families with incomplete penetrance (Kuehn 2024).
- **G191R** arose **de novo** in a sporadic pediatric case (Shi 2024).

The disease is **ultra-rare**: as of 2024–2026, only a few families and **fewer than ~30 affected individuals** carrying a handful of recurrent DNA-binding-domain (G159R, N160S, G191R) and haploinsufficiency (E82K, Q402*) variants have been reported worldwide.

> "we report on 9 individuals from 3 unrelated families carrying AIOLOS variants Q402* or E82K" — [PMID: 38015619](https://pubmed.ncbi.nlm.nih.gov/38015619/)

> "we discovered a de novo mutation in IKZF3 (NM_012481; exon 5 c.571G > C, p.Gly191Arg)" — [PMID: 38758229](https://pubmed.ncbi.nlm.nih.gov/38758229/)

**Evidence source:** human clinical.

### Finding 8 — Management, prognosis, and prevention

No disease-specific therapeutic trials exist; **management follows general combined-immunodeficiency/IEI standards**: immunoglobulin replacement (IVIG/SCIG) for hypogammaglobulinemia, antimicrobial prophylaxis (including anti-*Pneumocystis* trimethoprim-sulfamethoxazole given documented PCP), immunomodulation for autoimmune manifestations, and allogeneic HSCT for severe combined-immunodeficiency phenotypes (potentially curative; inferred from IEI practice). Prognosis is **variable and can be fatal** — disseminated VDRV granulomatous disease produced fatal multi-organ failure with CNS involvement, and the index family developed CLL. Prevention hinges on **genetic counseling** (autosomal dominant, 50% transmission risk, variable/incomplete penetrance, de novo possible), cascade testing, malignancy surveillance, and **strict avoidance of live attenuated vaccines**.

A mechanistic caveat for therapy: the immunomodulatory drugs (IMiDs) / CELMoDs (lenalidomide, pomalidomide, iberdomide, mezigdomide) **degrade** AIOLOS via cereblon — the **opposite** of the therapeutic need in this loss-of-function disease — and are therefore mechanistically contraindicated.

> "a family presenting with T and B cell involvement, Pneumocystis jirovecii pneumonia, and/or chronic lymphocytic leukemia" — [PMID: 34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/)

> "an immunodeficient patient who subsequently developed fatal multi-organ failure, including neurological deficits, with VDRV detected in the cerebrospinal fluid" — [PMID: 41746515](https://pubmed.ncbi.nlm.nih.gov/41746515/)

> "two critical lymphoid transcription factors, Ikaros family zinc finger proteins 1 and 3 (IKZF1 and IKZF3), also known as Ikaros and Aiolos" — [PMID: 38539501](https://pubmed.ncbi.nlm.nih.gov/38539501/)

**Evidence source:** human clinical + inferred from IEI practice.

---

## Report by Template Section

### 1. Disease Information

**Overview.** AIOLOS-associated immunodeficiency / immune dysregulation is a Mendelian, autosomal-dominant inborn error of immunity caused by heterozygous germline variants in ***IKZF3*** (AIOLOS). It is a **combined immunodeficiency with immune dysregulation**: defective humoral and cellular immunity producing recurrent/opportunistic infections, hypogammaglobulinemia, autoimmunity, allergy, and predisposition to B-cell malignancy.

**Key identifiers.**
- **MONDO:** MONDO:0979328
- **Gene:** *IKZF3* (HGNC:13178; NCBI Gene 22806; chromosome 17q12-q21)
- **Protein:** AIOLOS (UniProt Q9UKT9)
- **OMIM/Orphanet/ICD/MeSH:** Not recorded in the provided identifiers; classified broadly under inborn errors of immunity / primary immunodeficiency. (The IUIS IEI classification groups it with the Ikaros-family transcription-factor defects.)

**Synonyms / alternative names.** "AIOLOS haploinsufficiency," "AIOLOS-associated inborn errors of immunity (IEI)," "IKZF3-related combined immunodeficiency," "Immune dysregulation with immunodeficiency due to AIOLOS haploinsufficiency."

**Information source.** Derived from **aggregated disease-level resources and primary case reports / case series** (not EHR cohorts). The evidence base is small (a handful of families; <~30 individuals).

### 2. Etiology

**Primary cause:** monogenic — heterozygous germline *IKZF3* variants. **Genetic risk = the causal variant itself**; there are no established environmental or infectious causes. **Risk factors** are a positive family history (autosomal dominant) and inheritance of a pathogenic allele; de novo variants also occur. **No validated protective genetic/environmental factors** are documented. **Gene–environment interaction:** the main interaction of clinical consequence is iatrogenic/infectious — exposure to **live attenuated vaccines** (e.g., rubella) in a genetically immunodeficient host leads to disseminated vaccine-derived infection (VDRV; PMID 41746515). Pathogen exposure drives the infectious phenotype in the context of the genetic defect.

### 3. Phenotypes

| Phenotype | Type | Onset | Frequency | Suggested HPO |
|---|---|---|---|---|
| Recurrent sinopulmonary/bacterial/viral infections | Clinical sign | Childhood (often) | Majority | HP:0002721 (Recurrent respiratory infections), HP:0002719 (Recurrent infections) |
| Hypogammaglobulinemia / impaired humoral responses | Lab abnormality | Childhood | Common | HP:0004313 (Decreased Ig level), HP:0002720 (Decreased IgG) |
| Abnormal B-cell development (↑CD21low, ↓CD23, abrogated CD40) | Lab abnormality | Childhood | N160S family | HP:0010976 (B-cell abnormality) |
| Decreased T lymphocytes / reduced recent thymic emigrants | Lab abnormality | Infancy (G191R) | Reported | HP:0005403 (Decreased T cells) |
| *Pneumocystis jirovecii* pneumonia | Clinical sign | Variable | Index family | Opportunistic infection |
| Autoimmunity (e.g., cytopenias, SLE-like) | Clinical sign | Variable | Haploinsufficiency class | HP:0002960 (Autoimmunity) |
| Allergy | Clinical sign | Variable | Haploinsufficiency class | HP:0012393 (Allergy) |
| Chronic lymphocytic leukemia | Clinical sign | Adult | Index family | HP:0005550 (B-cell lymphoproliferation) |
| Failure to thrive, diarrhea | Clinical sign | Infancy | G191R case | HP:0001508 (Failure to thrive), HP:0002014 (Diarrhea) |

**Severity/progression:** variable; ranges from mild/incompletely penetrant (E82K, Q402*) to severe/fatal (VDRV case). **Quality-of-life impact:** chronic infection burden, immunoglobulin dependence, autoimmune morbidity, and malignancy risk substantially affect daily functioning; formal QOL instruments have not been applied to this ultra-rare disorder.

### 4. Genetic / Molecular Information

- **Causal gene:** *IKZF3* / AIOLOS (HGNC:13178).
- **Reported pathogenic variants:**
  - **DNA-binding domain (dominant-negative):** G159R, **N160S**, G191R (c.571G>C, de novo) — missense.
  - **Haploinsufficiency:** **E82K** (missense, protein-stability domain), **Q402\*** (nonsense/truncating, loses ZF5–6 dimerization domain).
- **Classification:** pathogenic / likely pathogenic by functional evidence (ACMG PS3-type functional data: loss of DNA binding, loss of pericentromeric targeting, EMSA).
- **Allele frequency:** essentially absent from population databases (ultra-rare; private/de novo).
- **Origin:** germline (familial segregation and de novo both documented).
- **Functional consequences:** dominant-negative loss-of-function (DNA-binding variants) vs. haploinsufficiency (dosage reduction).
- **Modifier genes:** none validated; the paralogous **IKZF1/IKZF2** define a shared functional network. **Epigenetic/chromosomal abnormalities:** not a feature (point variants, not structural).

### 5. Environmental Information

No toxic, occupational, lifestyle, or dietary environmental causes are established. The relevant **infectious agents** are opportunistic/vaccine-derived pathogens that exploit the immunodeficiency: *Pneumocystis jirovecii* (PCP) and **vaccine-derived rubella virus (VDRV)**, plus assorted bacterial and viral infections.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **heterozygous germline *IKZF3* variant** arises (inherited or de novo) → produces an abnormal AIOLOS protein.
2. **Branch A (DNA-binding variants: N160S, G159R, G191R):** the mutant **loses DNA binding and pericentromeric heterochromatin targeting** and **dimerizes with wild-type AIOLOS**, *leading to* a **dominant-negative** poisoning of residual WT AIOLOS function (demonstrated in vitro).
   **Branch B (haploinsufficiency variants: E82K, Q402*):** the variant **reduces functional AIOLOS dosage** — E82K via **protein instability**, Q402* via **truncation** (loss of ZF5–6) that nonetheless retains homodimerization and **negatively regulates DNA binding through ZF1** (demonstrated in vitro).
3. Reduced/abrogated AIOLOS transcriptional activity → **disrupted NuRD-complex–dependent chromatin programs** controlling lymphocyte differentiation (inferred from AIOLOS molecular biology and shared Ikaros-family readouts).
4. → **Abnormal B- and T-cell development**: impaired humoral responses, high CD21low B cells, negative CD23, abrogated CD40 responses, decreased T cells, reduced recent thymic emigrants (demonstrated in patients).
5. → **Combined immunodeficiency** → recurrent sinopulmonary, bacterial, viral, and opportunistic infections (*Pneumocystis*; VDRV) (demonstrated).
6. **Parallel branch — immune dysregulation:** loss of AIOLOS restraint on lymphocyte activation (intestinal IELs; Th1 CXCR3 program; Th17 states) → **autoimmunity, allergy, SLE-like disease** (demonstrated in mice; inferred in patients).
7. **Late branch — malignancy:** chronic B-cell dysregulation/hyperproliferation → predisposition to **B-cell malignancy (CLL)** (observed in the index family; mechanism inferred).

**Molecular pathways / processes.** C2H2 zinc-finger transcription factor activity; NuRD chromatin remodeling; IFN-γ/STAT1 signaling (AIOLOS positively regulates CXCR3 on Th1 cells); lymphocyte differentiation and activation control. **Cell types involved:** B lymphocytes (CL:0000236), T lymphocytes incl. Th1 (CL:0000545), Th17 (CL:0002105), intestinal intraepithelial lymphocytes, naive CD4 T cells. **Suggested GO terms:** GO:0006355 (regulation of transcription, DNA-templated), GO:0030183 (B cell differentiation), GO:0030217 (T cell differentiation), GO:0002376 (immune system process), GO:0045580 (regulation of T cell differentiation). **Subcellular:** nucleus (GO:0005634), pericentromeric heterochromatin (GO:0005721).

### 7. Anatomical Structures Affected

- **Primary system:** hematopoietic/lymphoid and immune system (UBERON:0002405 immune system; UBERON:0002371 bone marrow; UBERON:0002106 spleen; UBERON:0002370 thymus).
- **Secondary involvement:** lungs (recurrent/opportunistic pneumonia; UBERON:0002048), gastrointestinal tract (diarrhea, IEL dysregulation; UBERON:0000160), kidney (immune-complex glomerulonephritis in mouse SLE model; UBERON:0002113), and CNS (VDRV with CSF involvement; UBERON:0001017).
- **Cell level:** B cells, T cells (Th1, Th17), intraepithelial lymphocytes, NK cells (by family analogy).
- **Lateralization:** systemic/bilateral — not a lateralized disorder.

### 8. Temporal Development

- **Onset:** typically **pediatric/childhood**, including infancy (G191R presented at 1 y 4 mo); some features (CLL) are adult-onset. Pattern is **chronic/insidious** with episodic infectious exacerbations.
- **Progression:** variable — from mild/incompletely penetrant to progressive and fatal (VDRV multi-organ failure). **Lifelong** disease.
- **Patterns:** no spontaneous remission; immune function can be stabilized with replacement/prophylaxis. **Critical period:** avoiding live vaccines in early childhood (before immune evaluation) is a key window to prevent catastrophic vaccine-derived infection.

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant (heterozygous/monoallelic).
- **Penetrance:** variant-dependent — **full** for N160S; **incomplete** for E82K/Q402* haploinsufficiency.
- **Expressivity:** variable.
- **Origin:** familial segregation and de novo both documented; no anticipation, founder effect, or consanguinity dependence (dominant).
- **Epidemiology:** ultra-rare; **<~30 reported individuals** worldwide across a few families (as of 2024–2026). Precise prevalence/incidence undetermined. No strong sex bias established; both sexes affected. No defined geographic/ethnic clustering.

### 10. Diagnostics

- **Immunologic workup:** serum immunoglobulins (hypogammaglobulinemia; LOINC panels for IgG/IgA/IgM), lymphocyte subsets (decreased T cells, abnormal B-cell maturation: ↑CD21low, ↓CD23), vaccine/antibody responses, recent-thymic-emigrant quantification, CD40 response assays.
- **Genetic testing (definitive):** **whole-exome or whole-genome sequencing** / IEI gene panels including *IKZF3*; confirm with single-gene / segregation testing. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are **not indicated** (point variants).
- **Functional confirmation:** DNA-binding assays (EMSA), pericentromeric heterochromatin localization, dominant-negative/dimerization assays — these distinguish pathogenic variants and classify mechanism.
- **Differential diagnosis:** CVID; other Ikaros-family defects (IKZF1/Ikaros AD-CVID, IKZF2/Helios immune dysregulation); other combined immunodeficiencies and primary atopic disorders. Distinguish by gene and by the AIOLOS-specific functional signature.
- **Screening:** cascade genetic testing of at-risk relatives.

### 11. Outcome / Prognosis

Prognosis is **variable**. Many patients stabilize with immunoglobulin replacement and prophylaxis, but the disorder carries risks of **autoimmune morbidity, B-cell malignancy (CLL), and life-threatening/fatal infection** (e.g., disseminated VDRV with multi-organ failure and CNS involvement). No formal survival statistics exist for this ultra-rare disease. **Prognostic factors:** variant class/mechanism (DNA-binding dominant-negative appears more fully penetrant/severe), degree of T/B-cell compromise, and infection/malignancy history. Live-vaccine exposure is a major adverse prognostic event.

### 12. Treatment

- **Supportive/replacement:** **immunoglobulin replacement (IVIG/SCIG)** for hypogammaglobulinemia (NCIT: Intravenous Immunoglobulin Therapy); **antimicrobial prophylaxis**, including **trimethoprim-sulfamethoxazole** anti-*Pneumocystis* prophylaxis (NCIT: Trimethoprim-Sulfamethoxazole; CHEBI:9332 sulfamethoxazole).
- **Immunomodulation** for autoimmune/dysregulatory manifestations (corticosteroids, targeted immunosuppression; individualized).
- **Definitive/curative (severe phenotypes):** **allogeneic hematopoietic stem cell transplantation (HSCT)** (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation) — inferred from general combined-immunodeficiency practice; not yet reported as a disease-specific trial.
- **Mechanistically contraindicated:** **IMiDs/CELMoDs** (lenalidomide, pomalidomide, iberdomide, mezigdomide) degrade AIOLOS via cereblon — opposite to the loss-of-function pathology.
- **Experimental/targeted:** none disease-specific; no NCT trials identified for this disease.

### 13. Prevention

- **Primary:** genetic counseling for at-risk families (50% transmission; variable penetrance; de novo possible); avoidance of live attenuated vaccines once immunodeficiency is suspected/confirmed.
- **Secondary:** early immunologic evaluation and genetic diagnosis; cascade/carrier testing; prenatal/preimplantation options via counseling.
- **Tertiary:** infection prophylaxis, immunoglobulin replacement, autoimmune management, and **malignancy surveillance** (CLL).
- **Immunization note:** inactivated vaccines generally acceptable; **live vaccines contraindicated** (VDRV risk).

### 14. Other Species / Natural Disease

- **Orthologous gene:** mouse *Ikzf3* (Aiolos), NCBI Gene 22780. **Model species:** *Mus musculus* (NCBI Taxon 10090).
- **Natural disease in other species:** no well-characterized naturally occurring companion-animal/wildlife disease documented; relevance is primarily experimental. No zoonotic potential.
- **Comparative biology:** AIOLOS function and the SLE-like autoimmune consequence of its loss are conserved in mouse, supporting evolutionary conservation of the lymphoid transcriptional program.

### 15. Model Organisms

- **Aiolos-null mouse:** develops SLE-like autoimmunity (anti-dsDNA, immune-complex glomerulonephritis, B-cell hyperproliferation, spontaneous germinal centers) — models the **immune-dysregulation/autoimmune** arm (PMID 12574333).
- **Humanized knock-in mouse (N160S-equivalent):** recapitulates the **patient immunophenotype** — models the **dominant-negative immunodeficiency** arm (PMID 34694366).
- **Influenza-infection mouse model:** used to show Aiolos positively regulates CXCR3 on Th1 cells (PMID 39560988).
- **Applications:** mechanism of lymphocyte differentiation, autoimmunity, and infection susceptibility. **Limitations:** mouse CRBN resists IMiD-induced AIOLOS degradation (relevant to pharmacology), and incomplete penetrance in human haploinsufficiency may not be fully captured. **Resources:** MGI (Ikzf3).

---

## Mechanistic Model / Interpretation

```
          Heterozygous germline IKZF3 (AIOLOS) variant
                              |
        +---------------------+----------------------+
   BRANCH A: DNA-binding variants            BRANCH B: Haploinsufficiency variants
   (N160S, G159R, G191R)                     (E82K instability; Q402* truncation)
        |                                             |
   Loss of DNA binding +                       Reduced functional AIOLOS dosage
   loss of pericentromeric targeting;          (Q402* retains dimerization,
   DOMINANT-NEGATIVE poisoning of WT AIOLOS     negatively regulates DNA binding via ZF1)
        +---------------------+----------------------+
                              v
          Disrupted NuRD-dependent lymphoid transcription programs
                              v
     Abnormal B-cell (CD21low^, CD23-, CD40v) & T-cell (vT, vRTE) development
                              |
        +---------------------+----------------------+
        v                     v                       v
  Combined             Immune dysregulation      B-cell malignancy
  immunodeficiency     (autoimmunity, allergy,   predisposition
  (recurrent/          SLE-like disease; loss    (CLL)
  opportunistic        of IEL/Th1/Th17 restraint)
  infections: PCP,
  VDRV, bacterial/viral)
```

The unifying interpretation is that **AIOLOS is a dosage- and function-sensitive master regulator of lymphocyte development and activation restraint.** Whether function is lost by poisoning (dominant-negative) or by dosage reduction (haploinsufficiency), the cell cannot execute normal B/T differentiation programs, simultaneously producing **immunodeficiency** (failure of protective immunity) and **immune dysregulation** (failure to restrain autoreactive/inflammatory programs) — the hallmark "immunodeficiency + dysregulation" duality shared across the Ikaros family.

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Evidence type |
|---|---|---|---|
| [34694366](https://pubmed.ncbi.nlm.nih.gov/34694366/) | *T/B abnormalities, PCP, CLL with AIOLOS defect* | Defines disease; N160S dominant-negative; humanized mouse | Human + in vitro + mouse |
| [38015619](https://pubmed.ncbi.nlm.nih.gov/38015619/) | *AIOLOS variants → haploinsufficiency; redefine domains* | Defines haploinsufficiency class (E82K, Q402*); 9 pts/3 families | Human + in vitro |
| [38773004](https://pubmed.ncbi.nlm.nih.gov/38773004/) | *AIOLOS-Associated Inborn Errors of Immunity* | Review; variant catalog + infection phenotype | Review |
| [38758229](https://pubmed.ncbi.nlm.nih.gov/38758229/) | *De novo IKZF3 (G191R) pediatric CID* | De novo origin; infantile combined ID | Human + in vitro |
| [41746515](https://pubmed.ncbi.nlm.nih.gov/41746515/) | *Fatal VDRV granulomatous disease in AIOLOS ID* | Severe/fatal outcome; live-vaccine contraindication | Human |
| [12574333](https://pubmed.ncbi.nlm.nih.gov/12574333/) | *Aiolos mutant mice → SLE-like disease* | Mouse autoimmune phenotype | Mouse |
| [34920454](https://pubmed.ncbi.nlm.nih.gov/34920454/) | *IKZF2 (Helios) monoallelic mutations* | Places AIOLOS in Ikaros-family spectrum; shared dimerization/DNA-binding loss | Human + in vitro |
| [38734037](https://pubmed.ncbi.nlm.nih.gov/38734037/) | *Novel IKZF1 variant, AD CVID* | Paralog IKZF1 haploinsufficiency; shared functional assays | Human + in vitro |
| [39560988](https://pubmed.ncbi.nlm.nih.gov/39560988/) | *Aiolos promotes CXCR3 on Th1 via IFN-γ/STAT1* | Downstream effector program | Mouse + in vitro |
| [38049581](https://pubmed.ncbi.nlm.nih.gov/38049581/) | *Aiolos restrains intestinal IEL activation* | Immune-dysregulation mechanism | Mouse |
| [41922588](https://pubmed.ncbi.nlm.nih.gov/41922588/) | *Aiolos and Eos drive human TH17 states* | Human Th17 regulation by AIOLOS | Human in vitro |
| [38539501](https://pubmed.ncbi.nlm.nih.gov/38539501/) | *Mezigdomide CELMoD* | Confirms IMiDs degrade AIOLOS (therapeutically opposite) | Review |

**How the evidence converges:** The two foundational human papers (34694366, 38015619) establish the two mechanistic variant classes; the review (38773004) and additional case (38758229) extend the clinical/genetic spectrum and de novo occurrence; mouse models (12574333, 34694366, 39560988, 38049581) demonstrate causality and mechanism; and the paralog papers (34920454, 38734037) situate the disease within the Ikaros-family IEI landscape. No paper challenges the core causal model; the IMiD literature (38539501) clarifies that AIOLOS-degrading drugs are mechanistically inappropriate here.

---

## Limitations and Knowledge Gaps

1. **Ultra-rare, small evidence base.** Fewer than ~30 reported individuals; genotype–phenotype correlations and penetrance estimates are based on a handful of families and may shift as more cases emerge.
2. **Missing formal identifiers.** OMIM, Orphanet, ICD, and MeSH IDs were not recorded/confirmed in this investigation; these should be cross-referenced.
3. **Epidemiology undefined.** No reliable prevalence/incidence, sex ratio, or geographic data.
4. **Treatment evidence is inferential.** No disease-specific trials; HSCT utility and immunomodulation choices are extrapolated from general combined-immunodeficiency practice.
5. **Mechanistic gaps.** The precise transcriptional targets linking AIOLOS loss to CLL predisposition, and the determinants of incomplete penetrance in haploinsufficiency variants, remain unresolved.
6. **Single-cell / omics data** specific to patient lymphocytes are limited; most mechanistic resolution derives from mouse and in vitro systems.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for *IKZF3*-associated IEI to refine penetrance, natural history, infection/malignancy rates, and HSCT outcomes.
2. **Patient-derived single-cell multi-omics** (scRNA-seq + scATAC-seq) of B/T compartments to map AIOLOS-dependent regulatory programs and define biomarkers distinguishing dominant-negative vs. haploinsufficiency mechanisms.
3. **Systematic variant functional classification** (saturation DNA-binding/dimerization/pericentromeric-targeting assays) to triage future VUS and correlate mechanism with severity.
4. **Confirm/assign formal ontology identifiers** (OMIM, Orphanet, ICD-11, MeSH) and HPO frequency annotations for the knowledge-base entry.
5. **Evaluate HSCT timing and outcomes** in severe/fatal-risk patients via multicenter case collection; define malignancy-surveillance protocols for CLL.
6. **Reinforce live-vaccine contraindication guidance** in newborn/early-childhood pathways for families with known pathogenic *IKZF3* variants, given the fatal VDRV precedent.

---

*Report compiled from 8 confirmed findings and 27 reviewed papers across 5 investigation iterations. Evidence types are labeled human clinical, model organism (mouse), in vitro, or inferred throughout.*


## Artifacts

- [OpenScientist final report](Immune_Dysregulation_With_Immunodeficiency_Due_To_AIOLOS_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Immune_Dysregulation_With_Immunodeficiency_Due_To_AIOLOS_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 21 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 12 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0005550` (1 mention) - the report calls it "B-cell lymphoproliferation"; HP calls it **Chronic lymphatic leukemia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0010976` (1 mention) - the report calls it "B-cell abnormality"; HP calls it **Decreased total B cell count**, and lists "Low B cell count" among its other names
- `HP:0005403` (1 mention) - the report calls it "Decreased T cells"; HP calls it **Decreased total T cell count**, and lists "Decrease in T cell count" among its other names