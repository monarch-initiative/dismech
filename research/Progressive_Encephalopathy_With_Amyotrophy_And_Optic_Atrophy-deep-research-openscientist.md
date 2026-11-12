---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T21:58:42.719690'
end_time: '2026-11-11T22:20:08.763826'
duration_seconds: 1286.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Progressive Encephalopathy With Amyotrophy And Optic Atrophy
  mondo_id: MONDO:0014968
  category: Mendelian
  causal_genes: TBCE
  omim_id: OMIM:617207
  synonyms: encephalopathy, progressive, with amyotrophy and optic atrophy; PEAMO;
    PEAMO
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
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 11
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 8
  validator_version: 0.5.1
term_validation:
  total_terms: 35
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0002509
    reported_labels:
    - Progressive encephalopathy
    ontology_label: Limb hypertonia
  - term_id: GO:0005874
    reported_labels:
    - Subcellular level:** microtubule cytoskeleton
    ontology_label: microtubule
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Progressive_Encephalopathy_With_Amyotrophy_And_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Progressive_Encephalopathy_With_Amyotrophy_And_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Encephalopathy With Amyotrophy And Optic Atrophy
- **MONDO ID:** MONDO:0014968 (if available)
- **Causal gene(s):** TBCE
- **OMIM:** OMIM:617207
- **Synonyms:** encephalopathy, progressive, with amyotrophy and optic atrophy; PEAMO; PEAMO
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Progressive Encephalopathy With Amyotrophy And Optic Atrophy** covering all of the
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

# Progressive Encephalopathy With Amyotrophy And Optic Atrophy (PEAMO): A Comprehensive Disease Characterization

**Disease:** Progressive Encephalopathy With Amyotrophy And Optic Atrophy (PEAMO)
**MONDO:** MONDO:0014968 · **OMIM:** #617207 · **Causal gene:** *TBCE* (tubulin-specific chaperone E / tubulin folding cofactor E), HGNC:11582, chromosome **1q42.3**
**Inheritance:** Autosomal recessive · **Category:** Mendelian (rare neurodegenerative tubulinopathy)

---

## Summary

**Progressive Encephalopathy With Amyotrophy And Optic Atrophy (PEAMO) is caused by biallelic loss-of-function variants in *TBCE*, the gene encoding tubulin-specific chaperone E (cofactor E).** TBCE is one of five tubulin-folding cofactors (TBCA–TBCE) essential for assembling the α/β-tubulin heterodimer, the building block of microtubules. PEAMO was delineated as a distinct clinical entity by Sferra and colleagues in 2016, who identified recurrent biallelic *TBCE* mutations—most notably the founder-like missense change c.464T>A (p.Ile155Asn)—in six affected children from four unrelated families originating from the same area of Southern Italy ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)). The disorder is a childhood-onset, progressive neurodegenerative tubulinopathy defined by a clinical triad: **progressive encephalopathy/spastic-ataxic tetraparesis, distal spinal muscular atrophy (amyotrophy) from a distal motor axonal neuropathy, and optic atrophy**, with brain MRI showing progressive thinning of the corpus callosum and cerebro-cerebellar atrophy ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).

Mechanistically, destabilized/degraded TBCE protein impairs microtubule polymerization and disrupts an ARF1/TBCE-dependent Golgi homeostasis program, producing a **distal "dying-back" axonopathy** that begins at the motor endplates and ascends to axonal loss and neuronal apoptosis. This model is strongly supported by the *progressive motor neuronopathy* (pmn) mouse, which carries a *Tbce* missense mutation (p.Trp524Gly), faithfully recapitulates the motor neuronopathy, and is fully rescued by wild-type *Tbce* cDNA—establishing both causality and proof-of-concept for gene replacement ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/); [PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/); [PMID: 24951541](https://pubmed.ncbi.nlm.nih.gov/24951541/); [PMID: 27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/)).

PEAMO sits within a broader **allelic *TBCE* disease spectrum**. In a large aggregation of 335 *TBCE* patients, Sanjad-Sakati syndrome (hypoparathyroidism-retardation-dysmorphism, HRD) was by far the most common presentation (85%), whereas the PEAMO/neurodegenerative phenotype accounted for only ~5% of cases ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)). The critical distinction is that **PEAMO is a progressive neurodegenerative tubulinopathy that lacks the congenital hypoparathyroidism, intrauterine growth retardation, and facial dysmorphism** that define HRD/Sanjad-Sakati and autosomal-recessive Kenny-Caffey syndrome type 1 (KCS1). There is currently **no disease-modifying therapy**; management is supportive. This report synthesizes eight confirmed findings across 19 reviewed papers into a comprehensive, knowledge-base-ready characterization organized by the standard disease-template sections.

---

## Key Findings

### Finding 1 — PEAMO is caused by biallelic loss-of-function variants in *TBCE*

Sferra et al. (2016) established PEAMO as a *TBCE*-related disorder by identifying biallelic *TBCE* mutations in six affected subjects from four unrelated families from the same geographical area in Southern Italy, with the recurrent **c.464T>A (p.Ile155Asn)** variant present in the homozygous or compound-heterozygous state. The authors wrote that the disorder is *"caused by biallelic TBCE mutations, with the c.464T>A (p.Ile155Asn) change occurring at the heterozygous/homozygous state in six affected subjects from four unrelated families originated from the same geographical area in Southern Italy"* ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)). The shared geographic origin and recurrent allele indicate a **founder effect** in the Southern Italian population.

*TBCE* maps to **chromosome 1q42.3** and encodes tubulin-specific chaperone E, one of five tubulin-folding cofactors essential for α/β-tubulin heterodimer formation and microtubule polymerization. The mechanism is **loss of function**: Western blot of patient fibroblasts showed a *"reduced amount of TBCE, suggestive of rapid degradation of the mutant protein"* ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)). Thus the pathogenic variants destabilize TBCE, reducing its steady-state level and compromising its chaperone activity.

- **Ontology terms:** gene *TBCE* (HGNC:11582); MONDO:0014968; variant NM_003193.5:c.464T>A, p.(Ile155Asn); inheritance — autosomal recessive.

### Finding 2 — PEAMO is the minority (~5%) neurodegenerative pole of a broad *TBCE* spectrum

Sartorelli et al. (2026) assembled the largest *TBCE* cohort to date—335 mono-/biallelic patients (13 newly recruited plus 322 from systematic review)—and quantified the relative frequency of each clinical form. *"Sanjad-Sakati syndrome was the most frequent form (85%), while the neurodegenerative phenotype accounted for a minority (5%) of cases"* ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)). PEAMO therefore represents a small fraction of *TBCE* disease, which is dominated by the endocrine-dysmorphic HRD/Sanjad-Sakati presentation.

The neurodegenerative spectrum itself is clinically heterogeneous, ranging from classic PEAMO—*"progressive spastic-ataxic tetraparesis, optic atrophy and distal motor axonal neuropathy, consistent with already named PEAMO"*—to milder complex spastic paraparesis. Neuroimaging frequently showed *"progressive thinning of the corpus callosum, cerebro-cerebellar atrophy"* ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).

### Finding 3 — Core clinical phenotype: early-onset progressive encephalopathy, distal amyotrophy, and optic atrophy

The defining phenotype is captured in the title and text of Sferra et al. (2016): *"TBCE Mutations Cause Early-Onset Progressive Encephalopathy with Distal Spinal Muscular Atrophy,"* describing *"an early-onset and progressive neurodegenerative encephalopathy with distal spinal muscular atrophy resembling the phenotype of pmn/pmn mice"* ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)). Combined with Sartorelli et al. (2026), the **core triad** is:

1. **Progressive encephalopathy / spastic-ataxic tetraparesis** (central nervous system degeneration)
2. **Distal spinal muscular atrophy / amyotrophy** (distal motor axonal neuropathy, lower motor neuron)
3. **Optic atrophy** (anterior visual pathway degeneration)

Onset is in **infancy/early childhood** with a **progressive** course, and neuroimaging shows progressive corpus-callosum thinning and cerebro-cerebellar atrophy ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).

| Phenotype | HPO suggestion | Type | Onset | Course |
|---|---|---|---|---|
| Progressive encephalopathy | HP:0002509 (Progressive encephalopathy) | Clinical sign | Infancy/early childhood | Progressive |
| Spastic-ataxic tetraparesis | HP:0001258 (Spasticity) / HP:0001251 (Ataxia) / HP:0002510 (Spastic tetraplegia) | Clinical sign | Early childhood | Progressive |
| Distal spinal muscular atrophy / amyotrophy | HP:0007373 (Distal amyotrophy) / HP:0007002 (Motor axonal neuropathy) | Clinical sign | Childhood | Progressive |
| Optic atrophy | HP:0000648 (Optic atrophy) | Physical manifestation | Childhood | Progressive |
| Thin corpus callosum | HP:0002079 (Hypoplasia of the corpus callosum) | Imaging/lab | Childhood | Progressive thinning |
| Cerebellar atrophy | HP:0001272 (Cerebellar atrophy) | Imaging/lab | Childhood | Progressive |

### Finding 4 — Mechanism: impaired microtubule polymerization plus ARF1/TBCE-dependent Golgi fragmentation drive a dying-back axonopathy

The mechanistic chain is anchored in mouse and cellular models. In the pmn mouse (Tbce missense), *"Electron microscopy of the sciatic and phrenic nerves of affected mice showed a reduced number of microtubules, probably due to defective stabilization"* ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)), directly linking TBCE loss to axonal microtubule depletion. Schäfer et al. (2017) showed that *"the pmn mutation decreases the level of TBCE, impedes microtubule polymerization in dorsal root ganglion (DRG) neurons and causes progressive loss of microtubules"* with defective microtubule-based axonal transport ([PMID: 27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/)).

Beyond the cytoskeleton, TBCE has a cis-Golgi function. Bellouze et al. (2014) found that *"Loss of TBCE in mutant pmn and TBCE-depleted motor neuron cultures causes defects in Golgi-derived microtubules, as expected, but surprisingly also reduced levels of COPI subunits, decreased recruitment of tethering factors p115/GM130 and impaired Golgi SNARE-mediated vesicle fusion"*; the small GTPase **ARF1 recruits TBCE to the Golgi and rescues fragmentation** ([PMID: 24951541](https://pubmed.ncbi.nlm.nih.gov/24951541/)). The degeneration follows a distal-to-proximal (dying-back) pattern: *"The disease starts at the motor endplates, and then leads to axonal loss and finally to apoptosis of the corresponding cell bodies"* ([PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/)).

### Finding 5 — The pmn mouse is a faithful, fully penetrant model and a gene-rescue proof-of-concept

Martin et al. (2002) identified the causative *Tbce* missense mutation (p.Trp524Gly) in the pmn mouse, which develops progressive caudio-cranial motor axon degeneration from ~2 weeks of age and dies at 4–6 weeks. *"The mutation is fully penetrant, and expressivity does not depend on the genetic background"* ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)). Critically, *"Transgenic complementation with a wildtype Tbce cDNA restored a normal phenotype in mutant mice"* ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)), providing direct causal proof and a foundation for gene-replacement strategies. At the cellular level, *"Isolated motoneurons from pmn mutant mice exhibit shorter axons and axonal swelling with irregularly structured beta-tubulin and tau immunoreactivity"* ([PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/)). The pmn mouse also displays a sensory neuropathy with microtubule loss, broadening its relevance to axonal neurodegeneration ([PMID: 27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/)).

### Finding 6 — Allelic disorders and differential diagnosis: PEAMO vs. HRD/Sanjad-Sakati and KCS1

Parvari et al. (2002) first linked *TBCE* to **hypoparathyroidism-retardation-dysmorphism (HRD / Sanjad-Sakati, OMIM 241410)** and **autosomal-recessive Kenny-Caffey syndrome type 1 (KCS1, OMIM 244460)**, noting that *"The gene TBCE encodes one of several chaperone proteins required for the proper folding of alpha-tubulin subunits and the formation of alpha-beta-tubulin heterodimers"* ([PMID: 12389028](https://pubmed.ncbi.nlm.nih.gov/12389028/)). The Middle Eastern founder mutation is a 12-bp deletion: in 21 Sanjad-Sakati patients from Kuwait, *"All affected persons had homozygous deletion of 12 bp (155-166del) in exon 3 of the TBCE gene. All of the parents were heterozygous carriers of this mutation"* ([PMID: 19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/)). A systematic review of 205 Kenny-Caffey patients noted that *"Symptoms more prevalent in KCS1 included intellectual disability"* ([PMID: 36916904](https://pubmed.ncbi.nlm.nih.gov/36916904/)).

The **key diagnostic distinction**: PEAMO is a progressive neurodegenerative tubulinopathy **without** the congenital hypoparathyroidism, intrauterine growth retardation, or facial dysmorphism that define HRD/KCS1. A given *TBCE* genotype tends to determine which pole of the spectrum is expressed.

### Finding 7 — The *TBCE* neurodegenerative spectrum extends beyond classic PEAMO, with a genotype-phenotype gradient and an out-of-frame rescue mechanism

Sparber et al. (2025) described 7 patients with a **novel, milder *TBCE* phenotype** (amyotrophy, testicular failure, mild intellectual disability ± short stature). *"All patients were homozygous or compound-heterozygous for the NM_003193.5:c.100 + 1G > A variant, which causes a splicing alteration and early frameshift. However, we found that the mild phenotype arises due to translation from an alternative open reading frame, producing a partially functional protein"* ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/)). Patient fibroblasts showed reduced Golgi compactness but normal microtubule dynamics—suggesting a threshold effect in which residual TBCE function attenuates the phenotype. This dovetails with the full spectrum reported by Sartorelli et al. (2026), ranging from classic PEAMO to *"milder complex spastic paraparesis"* ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)). Together these establish a **genotype–phenotype severity gradient governed by residual TBCE activity**.

### Finding 8 — TBCE domain architecture (CAP-Gly, LRR, UBL) mediates both tubulin heterodimer assembly and dissociation/degradation

Serna et al. (2015) solved the structure of the α-tubulin–TBCE–TBCB (αEB) complex, revealing TBCE's three functional domains: **cytoskeleton-associated protein glycine-rich (CAP-Gly)**, **leucine-rich repeat (LRR)**, and **ubiquitin-like (UBL)**. Heterodimer dissociation occurs through *"a steric interaction between β-tubulin and the TBCE cytoskeleton-associated protein glycine-rich (CAP-Gly) and leucine-rich repeat (LRR) domains"*, and *"The protruding arrangement of chaperone ubiquitin-like (UBL) domains in the αEB complex suggests that there is a direct interaction of this complex with the proteasome, thus mediating α-tubulin degradation"* ([PMID: 25908846](https://pubmed.ncbi.nlm.nih.gov/25908846/)). TBCE is thus bifunctional—building heterodimers and controlling their disassembly/turnover—placing it at the heart of tubulin proteostasis. Loss of this activity disturbs *"subcellular organelles that require microtubules for membrane trafficking, such as the Golgi and late endosomal compartments"* ([PMID: 12389028](https://pubmed.ncbi.nlm.nih.gov/12389028/)).

---

## Report by Template Section

### 1. Disease Information

PEAMO is a rare, autosomal-recessive, childhood-onset **neurodegenerative tubulinopathy** characterized by progressive encephalopathy, distal spinal muscular atrophy (amyotrophy), and optic atrophy, caused by biallelic loss-of-function variants in ***TBCE*** ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)).

- **Key identifiers:** OMIM #617207; MONDO:0014968; causal gene *TBCE* (HGNC:11582; 1q42.3).
- **Synonyms:** PEAMO; Encephalopathy, progressive, with amyotrophy and optic atrophy; (overlapping with the "TBCE-related neurodegeneration" / childhood-onset neurodegenerative phenotype).
- **Source of information:** Aggregated disease-level resources (OMIM, published case series/cohorts) and individual-patient reports; the largest dataset is a systematic review + recruited cohort of 335 *TBCE* patients ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).

### 2. Etiology

- **Primary cause:** Genetic—**biallelic loss-of-function variants in *TBCE***. The recurrent founder-like missense c.464T>A (p.Ile155Asn) causes rapid degradation of the mutant protein (reduced TBCE level) ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)).
- **Genetic risk factors:** Causal variants in *TBCE*; founder alleles increase local prevalence (Southern Italian p.Ile155Asn; Middle Eastern 12-bp 155-166del for the allelic HRD/KCS1 disorders) ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/); [PMID: 19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/)). **Consanguinity** and shared ancestry elevate carrier-couple risk.
- **Environmental/infectious/lifestyle risk factors:** None established; this is a monogenic disorder with no demonstrated environmental contribution.
- **Protective factors / modifiers:** Residual TBCE function is protective—variants permitting partial activity (e.g., alternative-ORF translation) produce milder disease ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/)).
- **Gene–environment interactions:** None reported.

### 3. Phenotypes

See the table under Finding 3. Core features: progressive encephalopathy (HP:0002509), spastic-ataxic tetraparesis (HP:0001258/HP:0001251), distal amyotrophy / motor axonal neuropathy (HP:0007373/HP:0007002), optic atrophy (HP:0000648); neuroimaging: thin corpus callosum (HP:0002079) and cerebellar atrophy (HP:0001272). Onset is in **infancy/early childhood**; course is **progressive**; severity is **variable** along a genotype-dependent gradient. Quality-of-life impact is **severe** given progressive motor disability, visual loss, and encephalopathy, though formal QoL-instrument data are not available for this ultra-rare disease.

### 4. Genetic / Molecular Information

- **Causal gene:** *TBCE* (OMIM *604934; HGNC:11582; 1q42.3), encoding tubulin-specific chaperone E / cofactor E.
- **Representative pathogenic variants:** c.464T>A, p.(Ile155Asn) — recurrent missense, Southern Italian PEAMO families ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)); c.100+1G>A — splice/early-frameshift, milder phenotype via alternative-ORF rescue ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/)); 155-166del (12-bp deletion, exon 3) — Middle Eastern founder allele for HRD/KCS1 ([PMID: 19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/)).
- **Variant types:** missense, splice-site, small deletion/frameshift, nonsense/truncating.
- **Functional consequence:** **Loss of function** (reduced protein level/stability) ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)).
- **Origin:** Germline; recessive (biallelic).
- **Modifier genes/epigenetics/chromosomal abnormalities:** No specific modifier genes or epigenetic signatures established; residual TBCE activity itself behaves as the principal modifier of severity.

### 5. Environmental Information

No environmental, lifestyle, toxic, or infectious contributors are established. PEAMO is a monogenic Mendelian disorder.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function *TBCE* variant **leads to** reduced/destabilized TBCE protein (rapid degradation of mutant protein) — *demonstrated* ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)).
2. Reduced TBCE **impairs** α/β-tubulin heterodimer assembly and the heterodimer dissociation/degradation cycle via its CAP-Gly, LRR and UBL domains — *demonstrated* structurally ([PMID: 25908846](https://pubmed.ncbi.nlm.nih.gov/25908846/); [PMID: 12389028](https://pubmed.ncbi.nlm.nih.gov/12389028/)).
3. This **results in** defective microtubule polymerization and progressive microtubule loss in neurons — *demonstrated* ([PMID: 27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/); [PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)).
4a. **Branch A (cytoskeletal/transport):** microtubule loss **impairs** microtubule-based axonal transport — *demonstrated* ([PMID: 27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/)).
4b. **Branch B (Golgi/secretory):** loss of Golgi-localized TBCE **reduces** COPI subunits, **disperses** tethers (p115/GM130) and **impairs** SNARE-mediated vesicle fusion → Golgi fragmentation; ARF1 recruits TBCE to the Golgi and rescues this — *demonstrated* ([PMID: 24951541](https://pubmed.ncbi.nlm.nih.gov/24951541/)).
5. Branches A and B **converge to** compromise motor (and sensory) axon maintenance, initiating degeneration **at the motor endplates** — *demonstrated* ([PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/)).
6. This **leads to** distal "dying-back" axonal loss and ultimately **apoptosis of neuronal cell bodies** — *demonstrated* in mouse ([PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/)).
7. The combined central and peripheral neurodegeneration **manifests as** the PEAMO triad: progressive encephalopathy, distal amyotrophy, and optic atrophy, with thin corpus callosum and cerebro-cerebellar atrophy — *demonstrated clinically* ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/); [PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).

```
TBCE LoF variant
      │ (protein destabilization/degradation)
      ▼
↓ TBCE protein  ──► impaired tubulin heterodimer assembly / dissociation (CAP-Gly, LRR, UBL)
      │
      ├─► ↓ microtubule polymerization ─► MT loss ─► defective axonal transport ┐
      │                                                                          ├─► axon maintenance fails
      └─► ↓ Golgi MTs, ↓COPI, dispersed p115/GM130, impaired SNARE fusion ───────┘   (begins at motor endplate)
                 (ARF1 recruits TBCE → Golgi; rescues fragmentation)                         │
                                                                                             ▼
                                                                     dying-back axonopathy → neuronal apoptosis
                                                                                             │
                                                                                             ▼
                                            PEAMO: encephalopathy + distal amyotrophy + optic atrophy
                                            (thin corpus callosum, cerebro-cerebellar atrophy)
```

- **Upstream:** TBCE loss; tubulin-proteostasis failure. **Downstream:** Golgi fragmentation, transport failure, axonal dying-back, neuronal apoptosis.
- **Cell types (CL):** motor neuron (CL:0000100), neuron (CL:0000540), retinal ganglion cell (CL:0000740, inferred for optic atrophy), sensory neuron / DRG neuron (CL:0000101).
- **GO biological processes:** tubulin complex assembly (GO:0007021), post-chaperonin tubulin folding pathway (GO:0007023), microtubule polymerization (GO:0046785), Golgi organization (GO:0007030), COPI coating of Golgi vesicle (GO:0048205), axonal transport (GO:0098930), neuron apoptotic process (GO:0051402).
- **GO cellular components:** Golgi apparatus (GO:0005794), microtubule (GO:0005874), microtubule cytoskeleton (GO:0015630).

### 7. Anatomical Structures Affected

- **Primary organ/system:** Nervous system (UBERON:0001016). CNS — brain, including corpus callosum (UBERON:0002336) and cerebellum (UBERON:0002037); white matter. PNS — peripheral motor (and sensory) nerves (UBERON:0001021).
- **Visual system:** Optic nerve (UBERON:0000941) — optic atrophy.
- **Secondary involvement:** Skeletal muscle (UBERON:0001134) — neurogenic amyotrophy (secondary to motor axon loss).
- **Cell level:** motor neurons, retinal ganglion cells (inferred), sensory/DRG neurons; nervous tissue.
- **Subcellular level:** microtubule cytoskeleton (GO:0005874), Golgi apparatus (GO:0005794); proteasome interaction (via TBCE UBL domain).
- **Lateralization:** Bilateral / symmetric, consistent with a diffuse neurodegenerative process.

### 8. Temporal Development

- **Onset:** Infancy to early childhood; insidious/chronic onset.
- **Progression:** Progressive, variable rate depending on genotype (residual TBCE activity). Severe PEAMO shows relentless progression; milder *TBCE* phenotypes progress more slowly ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/); [PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).
- **Course pattern:** Chronic, progressive (not relapsing-remitting or episodic).
- **Critical periods:** Early childhood neurodevelopmental window is the period of overt decline; the pmn mouse shows that intervention before axonal loss (gene rescue) can prevent disease, implying an early therapeutic window ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)).

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive; biallelic *TBCE* variants ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)).
- **Penetrance/expressivity:** In the pmn mouse, the mutation is fully penetrant with background-independent expressivity ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)); in humans, expressivity is variable along a genotype-dependent gradient.
- **Epidemiology:** Ultra-rare; precise prevalence/incidence not established. PEAMO accounts for ~5% of *TBCE* disease, which is itself rare ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).
- **Founder effects / geography:** Southern Italian founder allele p.Ile155Asn for PEAMO ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)); Middle Eastern 12-bp founder deletion for the allelic HRD/KCS1 disorders ([PMID: 19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/)).
- **Consanguinity:** Contributes, especially in founder populations (parents are heterozygous carriers).
- **Sex ratio:** No strong sex bias expected for an autosomal-recessive disorder (not specifically quantified for PEAMO).

### 10. Diagnostics

- **Genetic testing (definitive):** Molecular confirmation of biallelic *TBCE* variants via **whole-exome/genome sequencing**, neurodegeneration/neuropathy/hereditary spastic paraplegia gene panels, or targeted *TBCE* testing; carrier testing of parents confirms recessive segregation ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/); [PMID: 19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/)).
- **Neuroimaging:** Brain MRI showing progressive **corpus-callosum thinning** and **cerebro-cerebellar atrophy** ([PMID: 41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/)).
- **Electrophysiology:** Nerve conduction studies / EMG demonstrating a **distal motor axonal neuropathy**; ophthalmologic exam / OCT / VEP for optic atrophy.
- **Functional/laboratory:** Reduced TBCE on Western blot of patient fibroblasts supports loss of function in a research context ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/)). Note: unlike HRD/KCS1, PEAMO does **not** feature hypocalcemia/hypoparathyroidism.
- **Differential diagnosis:** HRD/Sanjad-Sakati (congenital hypoparathyroidism, IUGR, dysmorphism — [PMID: 12389028](https://pubmed.ncbi.nlm.nih.gov/12389028/)); Kenny-Caffey syndrome (KCS1 = *TBCE*; KCS2 = *FAM111A*); other childhood spastic-ataxias, hereditary motor-sensory neuropathies, and optic atrophy syndromes. Absence of endocrine/dysmorphic features distinguishes PEAMO.

### 11. Outcome / Prognosis

Prognosis is poor for classic PEAMO given progressive encephalopathy, motor disability, and visual loss; milder *TBCE* phenotypes have a more protracted course ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/)). Formal survival statistics are not available for this ultra-rare disease. The pmn mouse is lethal at 4–6 weeks, reflecting the severity of complete motor-neuronopathy in the model but not directly translatable to human life expectancy ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)). **Prognostic factor:** degree of residual TBCE function (genotype) is the principal determinant of severity and progression rate.

### 12. Treatment

- **Disease-modifying therapy:** None currently available; management is **supportive/symptomatic** (physical, occupational, and speech therapy; management of spasticity; visual/low-vision support; nutritional and respiratory support as needed; orthopedic management of neurogenic deformities).
- **Proof-of-concept for future therapy:** Transgenic wild-type *Tbce* cDNA fully rescued the pmn mouse phenotype, establishing gene replacement as a rational strategy ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/)). The natural rescue by alternative-ORF translation in milder patients suggests that even partial restoration of TBCE function could be clinically meaningful ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/)).
- **NCIT suggestions (supportive):** Physical Therapy (NCIT:C15327), Occupational Therapy (NCIT:C15316), Supportive Care (NCIT:C15230), Gene Therapy (NCIT:C15262, experimental/conceptual).

### 13. Prevention

- **Primary prevention:** Not applicable (monogenic). **Genetic counseling** for at-risk/consanguineous couples; carrier testing in founder populations (Southern Italian p.Ile155Asn; Middle Eastern 155-166del for allelic disorders).
- **Reproductive options:** Prenatal diagnosis and preimplantation genetic testing (PGT-M) for couples with a known *TBCE* genotype.
- **Cascade testing:** Of relatives once a familial variant is identified ([PMID: 19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/)).

### 14. Other Species / Natural Disease

- **Mouse (NCBI Taxon 10090):** *Tbce* orthologue; the **pmn** (progressive motor neuronopathy) mutant (Tbce p.Trp524Gly) is an established model of TBCE motor neuronopathy ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/); [PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/)).
- **Human orthologue mapping:** The human *TBCE* orthologue maps to 1q42.3 ([PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/)).
- **Comparative biology:** TBCE's tubulin-folding function is deeply conserved across eukaryotes; no companion-animal natural disease is specifically documented, but the conserved mechanism supports cross-species relevance.

### 15. Model Organisms

- **pmn mouse (Mus musculus):** Tbce missense p.Trp524Gly. Phenotype — progressive caudio-cranial motor axon degeneration from ~2 weeks, death at 4–6 weeks; fully penetrant; cellular phenotype of short axons, axonal swelling, irregular β-tubulin/tau, reduced axonal microtubules, Golgi fragmentation, and sensory neuropathy ([PMID: 12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/); [PMID: 12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/); [PMID: 24951541](https://pubmed.ncbi.nlm.nih.gov/24951541/); [PMID: 27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/)).
- **Phenotype recapitulation:** High fidelity for the motor-neuronopathy/axonopathy component; rescuable by wild-type *Tbce* cDNA.
- **Cellular models:** Patient-derived dermal fibroblasts (reduced TBCE; Golgi compactness changes) and TBCE-depleted motor-neuron cultures ([PMID: 27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/); [PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/); [PMID: 24951541](https://pubmed.ncbi.nlm.nih.gov/24951541/)).
- **Limitations:** The pmn mouse is more rapidly lethal than human disease and does not fully capture the human encephalopathy/optic-atrophy spectrum.

---

## Mechanistic Model / Interpretation

PEAMO is best understood as a **tubulin-proteostasis disorder with tissue-selective (neuronal) vulnerability**. TBCE is a bifunctional chaperone: through its CAP-Gly, LRR and UBL domains it both assembles the α/β-tubulin heterodimer and drives its dissociation and proteasomal turnover ([PMID: 25908846](https://pubmed.ncbi.nlm.nih.gov/25908846/)). When biallelic loss-of-function variants destabilize TBCE, two coupled failures ensue: (i) a **cytoskeletal failure**—impaired microtubule polymerization and progressive microtubule loss with defective axonal transport—and (ii) a **secretory failure**—Golgi fragmentation from loss of Golgi-derived microtubules, COPI depletion, tether dispersal, and impaired SNARE-mediated vesicle fusion, which is normally countered by ARF1-dependent recruitment of TBCE to the Golgi. Long, metabolically demanding neurons—motor neurons and retinal ganglion cells—are exquisitely dependent on both microtubule-based transport and Golgi secretory output, explaining why the phenotype is dominated by distal motor amyotrophy, encephalopathy, and optic atrophy. The degeneration proceeds in a **dying-back** pattern, from motor endplate to axon to cell body, culminating in neuronal apoptosis.

The **genotype–phenotype gradient** is the unifying explanatory variable across the entire *TBCE* spectrum: the amount of residual TBCE function determines whether a patient develops severe PEAMO, milder complex spastic paraparesis, or—in the allelic context—the endocrine-dysmorphic HRD/KCS1 phenotypes. The alternative-ORF rescue described by Sparber et al. is a striking natural demonstration that partial restoration of TBCE converts a nominally null allele into a milder disease ([PMID: 39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/)).

| Disorder | Gene | Key founder variant | Hallmark features | Neurodegeneration |
|---|---|---|---|---|
| **PEAMO** (OMIM 617207) | *TBCE* | c.464T>A p.Ile155Asn (S. Italy) | Progressive encephalopathy, distal SMA/amyotrophy, optic atrophy; thin CC, cerebro-cerebellar atrophy | **Yes (defining)** |
| Milder *TBCE* neuro-phenotype | *TBCE* | c.100+1G>A (alt-ORF rescue) | Amyotrophy, testicular failure, mild ID ± short stature | Milder |
| Sanjad-Sakati / HRD (OMIM 241410) | *TBCE* | 155-166del (Middle East) | Congenital hypoparathyroidism, IUGR, dysmorphism, ID | Not the defining feature |
| Kenny-Caffey syndrome type 1 (OMIM 244460) | *TBCE* | 155-166del (Middle East) | Hypoparathyroidism, skeletal findings, ID | Not the defining feature |
| Kenny-Caffey syndrome type 2 | *FAM111A* | — | KCS without microcephaly/ID (classically) | — |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [27666369](https://pubmed.ncbi.nlm.nih.gov/27666369/) | *TBCE Mutations Cause Early-Onset Progressive Encephalopathy with Distal SMA* | **Landmark:** defines PEAMO; identifies p.Ile155Asn founder allele; LoF via protein degradation |
| [41833177](https://pubmed.ncbi.nlm.nih.gov/41833177/) | *Clinical-genetic features of the TBCE spectrum: childhood-onset neurodegeneration* | **Cohort (n=335):** frequencies (PEAMO ~5%, SSS 85%), clinical triad, neuroimaging, spectrum breadth |
| [12389029](https://pubmed.ncbi.nlm.nih.gov/12389029/) | *Missense mutation in Tbce causes pmn in mice* | Model: Trp524Gly; reduced microtubules; full penetrance; wild-type cDNA rescue |
| [12446740](https://pubmed.ncbi.nlm.nih.gov/12446740/) | *Tbce missense in pmn, a motoneuron-disease model* | Dying-back pattern; motoneuron phenotype; 1q42.3 orthologue |
| [24951541](https://pubmed.ncbi.nlm.nih.gov/24951541/) | *Golgi fragmentation via ARF1/TBCE crosstalk* | Golgi/COPI/SNARE mechanism; ARF1 rescue |
| [27488538](https://pubmed.ncbi.nlm.nih.gov/27488538/) | *Sensory neuropathy in pmn: MT polymerization & transport defects* | Microtubule polymerization/axonal-transport mechanism; sensory involvement |
| [25908846](https://pubmed.ncbi.nlm.nih.gov/25908846/) | *Structure of α-tubulin–TBCE–TBCB complex* | Domain architecture (CAP-Gly/LRR/UBL); dissociation & proteasomal degradation |
| [12389028](https://pubmed.ncbi.nlm.nih.gov/12389028/) | *TBCE causes HRD and AR Kenny-Caffey* | TBCE function; allelic disorders; Golgi/endosome trafficking defects |
| [19554981](https://pubmed.ncbi.nlm.nih.gov/19554981/) | *Sanjad-Sakati/KCS1 in Kuwait (n=21)* | Middle Eastern 12-bp founder deletion; recessive carrier inheritance |
| [36916904](https://pubmed.ncbi.nlm.nih.gov/36916904/) | *Expanding the phenotype of Kenny-Caffey* | Distinguishes KCS1/TBCE (intellectual disability) within KCS |
| [39657131](https://pubmed.ncbi.nlm.nih.gov/39657131/) | *Out-of-frame translation rescues a TBCE LoF variant* | Milder phenotype; alternative-ORF rescue; genotype-phenotype gradient |
| [26696811](https://pubmed.ncbi.nlm.nih.gov/26696811/) | *Golgi fragmentation in ALS motor neurons* | Context: TBCE/pmn Golgi mechanism relevant to broader motor neuron disease |

**Evidence source types:** Human clinical/genetic (27666369, 41833177, 39657131, 19554981, 36916904, 12389028); model organism (12389029, 12446740, 27488538, 24951541); in vitro/structural (25908846); review/contextual (26696811).

---

## Limitations and Knowledge Gaps

- **Epidemiology:** No validated prevalence or incidence figures for PEAMO specifically; it is ultra-rare (~5% of an already rare *TBCE* disease).
- **Natural history:** Survival, life expectancy, and standardized disability/QoL outcomes are not quantified; most human evidence comes from small series.
- **Optic-atrophy mechanism:** Retinal ganglion cell involvement is inferred from the clinical phenotype rather than directly demonstrated in a PEAMO model; the pmn mouse best models the motor component.
- **Genotype–phenotype mapping:** Beyond a handful of recurrent alleles, the relationship between specific variants, residual TBCE activity, and PEAMO vs. HRD/KCS1 outcome is incompletely resolved.
- **Therapeutics:** No human disease-modifying therapy exists; the gene-rescue data are murine. Optimal therapeutic window, CNS delivery, and dosing for any future gene/protein therapy are unknown.
- **Modifiers/epigenetics:** No modifier genes or epigenetic contributors identified.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a PEAMO patient registry and natural-history study** to define onset distribution, progression rate, survival, and QoL, enabling future trial endpoints.
2. **Generate a humanized/knock-in mouse (or patient iPSC-derived motor neurons and retinal organoids) carrying p.Ile155Asn** to model the full PEAMO phenotype—including optic atrophy—beyond the pmn mouse.
3. **Quantify residual TBCE function across the variant spectrum** (protein stability, chaperone activity, Golgi/microtubule assays in fibroblasts) to build a predictive genotype–activity–severity model, extending the alternative-ORF rescue observation.
4. **Preclinical gene-replacement/augmentation studies** (AAV-*TBCE*, or splice-modulating/ORF-restoring ASOs for specific alleles such as c.100+1G>A) in cellular and mouse models, leveraging the pmn cDNA-rescue proof-of-concept.
5. **Biomarker development:** evaluate neurofilament light chain and quantitative MRI (corpus-callosum thickness, cerebellar volume) as progression/response biomarkers.
6. **Carrier-screening and counseling programs** in founder populations (Southern Italy; Middle East for allelic disorders), with cascade and reproductive (PGT-M/prenatal) options.

---

*Report compiled from 8 confirmed findings and 19 reviewed papers across 5 investigation iterations. All mechanistic and clinical claims are attributed to primary literature with PMIDs and verified abstract quotes.*


## Artifacts

- [OpenScientist final report](Progressive_Encephalopathy_With_Amyotrophy_And_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Progressive_Encephalopathy_With_Amyotrophy_And_Optic_Atrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002509` (2 mentions) - the report calls it "Progressive encephalopathy"; HP calls it **Limb hypertonia**
- `GO:0005874` (2 mentions) - the report calls it "Subcellular level:** microtubule cytoskeleton"; GO calls it **microtubule**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0007021` (1 mention) - the report calls it "GO biological processes:** tubulin complex assembly"; GO calls it **tubulin complex assembly**
- `GO:0005794` (2 mentions) - the report calls it "GO cellular components:** Golgi apparatus"; GO calls it **Golgi apparatus**
- `UBERON:0001016` (1 mention) - the report calls it "Primary organ/system:** Nervous system"; UBERON calls it **nervous system**
- `UBERON:0000941` (1 mention) - the report calls it "Visual system:** Optic nerve"; UBERON calls it **cranial nerve II**, and lists "02 optic nerve" among its other names
- `UBERON:0001134` (1 mention) - the report calls it "Secondary involvement:** Skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:11582` - called "TBCE", "Ontology terms:** gene *TBCE"