---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-22T16:02:03.356261'
end_time: '2026-09-22T16:20:50.915875'
duration_seconds: 1127.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: DEGCAGS Syndrome
  mondo_id: MONDO:0859181
  category: Mendelian
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
citation_count: 12
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 7
  off_topic: 3
  off_topic_references:
  - PMID:30846446
  - PMID:29482634
  - PMID:21791101
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 49
  verified: 47
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0000955
    reported_labels:
    - Organ/system level:** craniofacial skeleton, brain/CNS
    ontology_label: brain
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0006306
    ontology_label: obsolete DNA methylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: DEGCAGS_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: DEGCAGS_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DEGCAGS Syndrome
- **MONDO ID:** MONDO:0859181 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DEGCAGS Syndrome** covering all of the
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

# DEGCAGS Syndrome: A Comprehensive Disease Characteristics Report

**Disease:** DEGCAGS Syndrome (Developmental Delay with Gastrointestinal, Cardiovascular, Genitourinary, and Skeletal Abnormalities)
**MONDO ID:** MONDO:0859181 · **OMIM:** #619488 · **Gene:** *ZNF699* (OMIM *609571; 19p13.3)
**Category:** Mendelian, autosomal recessive
**Report date:** 2026-09-22 · Evidence base: ~40 patients reported worldwide (largest cohort n=30)

---

## Summary

**DEGCAGS syndrome (OMIM #619488; MONDO:0859181) is an ultra-rare, autosomal-recessive, congenital-onset multisystem malformation and neurodevelopmental disorder caused by biallelic loss-of-function variants in *ZNF699*, a KRAB-domain C2H2 zinc-finger transcription-factor gene on chromosome 19p13.3.** The disorder was first proposed as a novel gene–disease association in 2021 (Bertoli-Avella et al.) and substantially delineated in 2024 by Karimi et al., who assembled the largest cohort to date (30 affected individuals) and defined a reproducible blood DNA-methylation episignature that now serves as a diagnostic and variant-classification tool.

Clinically, DEGCAGS is characterized by near-universal coarse facial dysmorphism and global developmental delay/impaired intellectual development, accompanied by highly variable involvement of the gastrointestinal, cardiovascular, genitourinary, skeletal, dental, cutaneous, central nervous, hematologic/immune, sensory (sensorineural hearing loss, ocular), and airway systems. A hallmark of the disorder is marked clinical variability — including strikingly discordant organ anomalies among full siblings — together with significant infant and childhood mortality. Reported causes of death include heart failure from Tetralogy of Fallot, sepsis, and infection (Dengue).

Mechanistically, DEGCAGS is inferred to arise from loss of KRAB-zinc-finger-protein (KRAB-ZFP)/KAP1(TRIM28)-directed heterochromatin repression, consistent with the observed promoter-predominant hypermethylation episignature (which partially overlaps BAFopathy signatures) and with the general biology of KRAB-ZFPs. There is no targeted or disease-modifying therapy and no dedicated animal model; management is entirely supportive and multidisciplinary. Fewer than ~40 individuals have been reported worldwide as of 2026, and the disorder is frequently associated with consanguinity, though compound-heterozygous cases in non-consanguineous families are also documented.

---

## Key Findings

### Finding 1 — DEGCAGS is caused by biallelic loss-of-function *ZNF699* variants (autosomal recessive)

DEGCAGS syndrome is an autosomal recessive multisystem disorder caused by biallelic, loss-of-function (LoF) variants in *ZNF699*, a KRAB zinc-finger gene on chromosome 19p13.3. Karimi et al. (2024) collected 30 affected individuals (12 new) and confirmed biallelic LoF *ZNF699* as the cause. Reported variant types include frameshift indels (e.g., c.14-17delGAAA, p.Arg5fsTer14; c.975-976delCA, p.His325fsTer8, seen as a compound heterozygous pair), nonsense variants, and homozygous missense changes. The gene was first proposed as a novel disease association in 2021.

> *"Developmental Delay with Gastrointestinal, Cardiovascular, Genitourinary, and Skeletal Abnormalities syndrome (DEGCAGS, MIM #619488) is caused by biallelic, loss-of-function (LoF) ZNF699 variants"* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

> *"We propose six novel gene-disease associations based on 38 patients with variants in the BLOC1S1, IPO8, MMP15, PLK1, RAP1GDS1, and ZNF699 genes."* — [PMID: 33875846](https://pubmed.ncbi.nlm.nih.gov/33875846/)

### Finding 2 — A diagnostic DNA-methylation episignature and marked clinical variability

Karimi et al. (2024) performed blood-DNA methylation profiling in 9 individuals and constructed a classifier that distinguishes DEGCAGS from controls, identifying a robust, reproducible episignature. The syndrome shows variable neurodevelopmental disability, discordant organ anomalies among full siblings, age-related presentation, a shared facial gestalt (validated via GestaltMatcher on 53 facial photos from 5 individuals), and infant mortality. Differentially methylated regions (DMRs) implicate downstream genes plausibly involved in pathogenesis.

> *"We also identified a robust episignature for DEGCAGS syndrome."* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

> *"discordant organ anomalies among full siblings and infant mortality"* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

### Finding 3 — A congenital-onset multisystem malformation syndrome

Across case reports, DEGCAGS features include intrauterine growth restriction, prematurity, neonatal hypotension, generalized hypotonia, bradycardia, apnea, facial dysmorphia, skeletal malformations, and gastrointestinal, immune, urinary, respiratory, cardiac, and visual involvement. Craniofacial features span microcephaly *or* dolichocephaly, coarse facies, synophrys, smooth philtrum, thin upper lip, retromicrognathia, and hair thinning; dental findings include taurodontism, talon cusps, and enamel hypomineralization. Airway involvement includes laryngomalacia, vocal cord dysfunction, and nasopharyngeal/tongue-base hamartomas producing stridor. Hematologic/immune findings include leukopenia, neutropenia, and recurrent pneumonia.

> *"generalized hypotonia, bradycardia, apnea requiring resuscitation and positive pressure ventilation, facial dysmorphia, skeletal malformations, and disorders of the gastrointestinal, immune, urinary, respiratory, cardiac, and visual systems"* — [PMID: 38014480](https://pubmed.ncbi.nlm.nih.gov/38014480/)

> *"microcephaly, coarse facial features, oropharyngeal masses, and developmental delay"* — [PMID: 41205195](https://pubmed.ncbi.nlm.nih.gov/41205195/)

> *"hair thinning, dolichocephaly, retromicrognathia, synophrys, smooth philtrum, thin upper lip"* — [PMID: 42569837](https://pubmed.ncbi.nlm.nih.gov/42569837/)

### Finding 4 — Ultra-rare, consanguinity-associated, no targeted therapy

Fewer than ~40 individuals have been reported worldwide as of 2026; the largest series is 30 individuals (Karimi 2024). Inheritance is autosomal recessive: homozygous variants occur in consanguineous families (e.g., Middle Eastern), and compound-heterozygous variants occur in non-consanguineous families (maternal c.14-17delGAAA / paternal c.975-976delCA). No Orphanet prevalence figure is established; the disorder is classified as ultra-rare. Management is entirely supportive and multidisciplinary: airway surgery/supraglottoplasty for hamartomas, respiratory support, nutritional support, developmental/rehabilitative therapy, and dental care. No pharmacologic, gene, or disease-modifying therapy exists.

> *"We collected data on 30 affected individuals (12 new)."* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

> *"An infant born to a consanguineous Middle Eastern family"* — [PMID: 38014480](https://pubmed.ncbi.nlm.nih.gov/38014480/)

> *"Surgical resection of nasopharyngeal and tongue-base masses with supraglottoplasty was performed."* — [PMID: 41205195](https://pubmed.ncbi.nlm.nih.gov/41205195/)

### Finding 5 — *ZNF699* mutation spectrum and episignature architecture

*ZNF699* (OMIM *609571; HGNC:ZNF699; chr19p13.3) encodes a KRAB-C2H2 zinc-finger protein. The founding cohort (Bertoli-Avella et al. 2021) reported 13 patients from 12 consanguineous, mostly Arab families with 5 homozygous frameshift indels. Karimi et al. (2024) compiled 30 patients (18 from literature + 12 new) carrying 15 distinct variants (~10 frameshift/nonsense, 2 missense, 1 splice-site, 2 in-frame; 7 novel), located in the KRAB domain, the C2H2 zinc-finger domain, or the intervening region. 28/30 patients were homozygous and 2 compound heterozygous (e.g., Biela 2022, Q179X/R443X). The DEGCAGS episignature comprises ~210 DMRs, predominantly hypermethylation, with >50% located in gene promoters and partial overlap with BAFopathy episignatures.

> *"Analysis of differentially methylated regions suggested an effect on genes potentially implicated in the syndrome's pathogenesi[s]"* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

### Finding 6 — Immune and hematologic dysfunction is a core feature

OMIM #619488 lists anemia or pancytopenia, immunodeficiency with recurrent infections, and sensorineural hearing impairment as common features, with death in childhood. Immunodeficiency/recurrent infections are reported in ~42.3% of patients. Case-level evidence includes leukopenia and neutropenia with recurrent pneumonia (4–5 episodes/year) in an infant (Zhu et al. 2026), and the first detailed immunological work-up (Giardino et al. 2026) documenting severe B-cell depletion in a DEGCAGS patient with a novel biallelic *ZNF699* variant. Ali (2024) also noted immune involvement in a neonatal multisystem presentation.

> *"discordant organ anomalies among full siblings and infant mortality"* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

### Finding 7 — Phenotype frequencies and cohort demographics

The Karimi et al. (2024) cohort comprised 30 individuals from 23 families (20 male, 10 female; ages 1 month–21 years; mean age at diagnosis 4.9 years; Middle Eastern, European, Asian, and Hispanic descent), with 26 individuals having detailed clinical data. Feature frequencies (n=26) are summarized below.

| Phenotype | Frequency (n=26) | Percent | Suggested HPO term |
|---|---|---|---|
| Facial dysmorphism | 26/26 | 100% | HP:0001999 |
| Global developmental delay / intellectual disability | 25/26 | ~96% | HP:0001263 / HP:0001249 |
| Skeletal and dental abnormalities | 22/26 | ~85% | HP:0000924 / HP:0000164 |
| Skin/adnexa abnormalities | 19/26 | ~73% | HP:0000951 |
| CNS structural and myelin abnormalities | 17/26 | ~65% | HP:0002011 |
| Gastrointestinal abnormalities | 16/26 | ~62% | HP:0011024 |
| Genitourinary abnormalities | 16/26 | ~62% | HP:0000119 |
| Hypotonia | 15/26 | ~58% | HP:0001252 |
| Immunodeficiency / recurrent infections | ~42% | ~42% | HP:0002715 |
| Sensorineural hearing loss | Variable | — | HP:0000407 |
| Cardiovascular anomalies | Variable | — | HP:0001627 |
| Premature graying of hair | Variable | — | HP:0002216 |

Mortality: 3 deaths in the cohort — heart failure from Tetralogy of Fallot (at 6 months), Dengue fever (at 9 months), and sepsis (at 8 years).

> *"We collected data on 30 affected individuals (12 new)."* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

### Finding 8 — No animal model; complex *ZNF699* orthology

*ZNF699* is a KRAB-C2H2 zinc-finger transcription factor that acts in the nucleus and is predicted to regulate RNA polymerase II transcription. No knockout mouse, zebrafish, or other engineered DEGCAGS model has been reported; functional validation to date is limited to human patient DNA-methylation profiling. Historically, *ZNF699* was proposed as a human ortholog of the *Drosophila* alcohol-tolerance gene *hangover* (*hang*), but with low amino-acid identity (18–26%) and similarity (30–41%), and mammalian orthology of *hang* is complex. *ZNF699* mRNA was shown to be reduced in the dorsolateral prefrontal cortex of carriers of an alcohol-dependence-associated haplotype.

> *"a number of human gene products (including ZNF699) with similar levels of amino-acid identity (18-26%) and similarity (30-41%), are consistently identified as the best matches with the translated hang sequence"* — [PMID: 16940975](https://pubmed.ncbi.nlm.nih.gov/16940975/)

> *"expression of ZNF699 mRNA is significantly reduced in the dorsolateral prefrontal cortex"* — [PMID: 16940975](https://pubmed.ncbi.nlm.nih.gov/16940975/)

### Finding 9 — Protein architecture, structural disruption, episignature-based diagnosis correction, and a hematologic mechanistic link

Giardino et al. (2026) reported a novel homozygous KRAB-domain missense variant c.153C>A (p.Asn51Lys); AlphaFold2 modeling showed disruption of a hydrogen bond between residues 51 and 24 and defined the *ZNF699* domain architecture as a KRAB domain plus 16 C2H2 zinc fingers, causing syndromic combined immunodeficiency with severe B-cell depletion. Critically, the DEGCAGS episignature reclassified this case away from an incorrect ADNP/Helsmoortel–Van der Aa (HVDAS) diagnosis (a de novo ADNP VUS c.817C>T), yielding a high-confidence methylation-variant-pathogenicity score (0.891) and remaining robust despite marked lymphopenia. Hematologically (Bradley et al. 2025), DEGCAGS enters the differential for inherited bone marrow failure / Diamond–Blackfan anemia; anemia was reported in 8/14 early patients, with a proposed mechanistic link via a *ZNF699*–RNA-polymerase-II interaction and RNA Pol II's role in ribosome biogenesis, analogous to the bone-marrow-failure gene *MYSM1*.

> *"which can be used as a screening, diagnostic and classification tool for ZNF699 variants"* — [PMID: 39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/)

---

## Section-by-Section Report

### 1. Disease Information

**Overview.** DEGCAGS syndrome is a congenital-onset, autosomal-recessive multisystem malformation and neurodevelopmental disorder. The acronym stands for **D**evelopmental delay with **G**astrointestinal, **C**ardiovascular, **G**enitourinary, **A**nd **S**keletal abnormalities. It is characterized by near-universal facial dysmorphism and developmental delay, plus a highly variable constellation of organ malformations, growth failure, hypotonia, and hematologic/immune involvement, with significant early-childhood mortality.

**Key identifiers:**
- **OMIM:** #619488 (phenotype); gene *ZNF699* *609571
- **MONDO:** MONDO:0859181
- **Gene / HGNC:** *ZNF699*
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No dedicated Orphanet prevalence entry or specific ICD code identified; the disorder is ultra-rare and recently described (2021 onward). *(Not available / not established.)*

**Synonyms / alternative names:** "Developmental delay with gastrointestinal, cardiovascular, genitourinary, and skeletal abnormalities"; *ZNF699*-related syndrome; DEGCAGS.

**Information source type:** Primarily aggregated disease-level and cohort resources (OMIM, one large multi-center cohort, and individual case reports) rather than EHR-derived population data. The disorder is defined from ~30–40 individually reported patients.

### 2. Etiology

**Causal factor:** Genetic — biallelic loss-of-function variants in *ZNF699* (Finding 1). The disorder is monogenic and Mendelian; there is no evidence for environmental or infectious causation.

**Genetic risk factors:** The only established genetic cause is biallelic *ZNF699* LoF. Consanguinity is a major risk factor, producing homozygous frameshift/nonsense variants (founding Arab cohort; Finding 5). No modifier loci or susceptibility variants have been defined, though the marked intrafamilial variability (discordant siblings) implies unidentified modifiers, stochastic, or epigenetic contributions.

**Environmental / lifestyle / protective factors:** None identified. As a fully penetrant recessive malformation syndrome, environmental and protective factors and gene–environment interactions are **not applicable / not available**.

### 3. Phenotypes

DEGCAGS phenotypes span dysmorphology, neurodevelopment, and multiple organ systems (Findings 3, 7). Onset is congenital/neonatal; developmental delay persists into childhood. Severity is variable, ranging from survivable multisystem involvement to lethal in infancy. See the frequency table under Finding 7 for quantified frequencies and suggested HPO terms.

- **Craniofacial (100%):** coarse facies, synophrys (HP:0000664), smooth philtrum (HP:0000319), thin upper lip (HP:0000219), retromicrognathia (HP:0000278), microcephaly (HP:0000252) *or* dolichocephaly (HP:0000268), hair thinning.
- **Neurodevelopmental (~96%):** global developmental delay (HP:0001263), intellectual disability (HP:0001249), hypotonia (HP:0001252, ~58%), CNS structural/myelin abnormalities (~65%).
- **Dental (part of ~85% skeletal/dental):** taurodontism (HP:0000679), talon cusps, enamel hypomineralization (HP:0006297).
- **Airway/respiratory:** laryngomalacia (HP:0001601), vocal cord dysfunction, nasopharyngeal/tongue-base hamartomas causing stridor (HP:0031416).
- **Gastrointestinal (~62%), genitourinary (~62%), cardiovascular (variable, incl. Tetralogy of Fallot HP:0001636), skin/adnexa (~73%), sensorineural hearing loss (HP:0000407), ocular abnormalities, and hematologic/immune involvement (~42% immunodeficiency).**

**Quality-of-life impact:** Substantial — developmental delay, recurrent infections (4–5 pneumonias/year in some infants), feeding/airway difficulty, and multi-organ malformation impose high caregiving burden and early mortality. Formal QoL instrument data (EQ-5D, SF-36, PROMIS) are **not available** for this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene:** *ZNF699* (OMIM *609571; chr19p13.3), a KRAB-C2H2 zinc-finger transcription factor with a **KRAB domain plus 16 C2H2 zinc fingers** (Finding 9).

**Pathogenic variant spectrum (Finding 5):** 15 distinct variants across 30 patients — ~10 frameshift/nonsense, 2 missense, 1 splice-site, 2 in-frame; 7 novel; distributed across the KRAB domain, the C2H2 zinc-finger array, and the intervening region. Representative variants:

| Variant (cDNA) | Protein | Type | Zygosity context |
|---|---|---|---|
| c.14-17delGAAA | p.Arg5fsTer14 | Frameshift | Compound het (maternal) |
| c.975-976delCA | p.His325fsTer8 | Frameshift | Compound het (paternal) |
| — | p.Gln179Ter (Q179X) | Nonsense | Compound het (Biela 2022) |
| — | p.Arg443Ter (R443X) | Nonsense | Compound het (Biela 2022) |
| c.153C>A | p.Asn51Lys | Missense (KRAB) | Homozygous (Giardino 2026) |

**Variant classification:** Truncating variants are classified pathogenic/likely pathogenic (LoF is the established mechanism). The p.Asn51Lys missense was supported as pathogenic by a high episignature methylation-variant-pathogenicity score (0.891) plus AlphaFold2-predicted H-bond disruption (residues 51–24).

**Allele frequency:** Variants are private/ultra-rare; no common population allele frequency. **Origin:** germline. **Functional consequence:** loss of function.

**Modifier genes:** None identified (intrafamilial variability implies unknown modifiers).

**Epigenetic information:** DEGCAGS carries a diagnostic **DNA-methylation episignature** of ~210 DMRs, predominantly **hypermethylation**, >50% in gene promoters, partially overlapping BAFopathy signatures (Findings 2, 5, 9). This is both a diagnostic tool and a mechanistic clue.

**Chromosomal abnormalities:** None reported; the disorder is caused by point/indel variants, not large structural changes.

### 5. Environmental Information

No environmental, lifestyle, toxic, or infectious contributing factors are established. DEGCAGS is a monogenic recessive disorder. Infections (e.g., recurrent pneumonia, sepsis, Dengue) act as **downstream complications** of the intrinsic immunodeficiency rather than causal triggers.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Biallelic LoF variants in *ZNF699*** (frameshift/nonsense/splice/missense) → loss of functional ZNF699 KRAB-C2H2 zinc-finger transcription factor. *(Demonstrated: genetics.)*
2. Loss of ZNF699 → **loss of KRAB-ZFP/KAP1(TRIM28)-directed heterochromatin repression** at target loci (H3K9me3 deposition and DNA methylation). *(Inferred from general KRAB-ZFP biology; not yet directly demonstrated for ZNF699.)*
3. Loss of targeted repression → **dysregulated DNA methylation** genome-wide, manifesting as the reproducible promoter-predominant **hypermethylation episignature** (~210 DMRs). *(Demonstrated: patient methylation profiling.)*
4. Aberrant methylation/expression of downstream target genes → **dysregulated developmental gene-expression programs** during embryogenesis. *(Inferred; DMRs implicate candidate downstream genes.)*
5. **Branch A — Morphogenesis:** dysregulated developmental programs → multi-organ malformation (craniofacial, skeletal, GI, GU, cardiovascular, CNS). *(Inferred.)*
6. **Branch B — Hematopoiesis/immunity:** proposed ZNF699–RNA-Pol-II interaction and Pol-II role in ribosome biogenesis → impaired hematopoiesis → anemia/pancytopenia and B-cell depletion/immunodeficiency (analogous to *MYSM1*-related bone-marrow failure). *(Inferred/hypothesized.)*
7. **Branch C — Neurodevelopment:** dysregulated CNS gene programs → developmental delay, intellectual disability, hypotonia, white-matter/structural anomalies. *(Inferred.)*
8. Convergent multisystem burden + immunodeficiency → recurrent infection, cardiac failure, growth failure → **infant/childhood mortality**. *(Demonstrated at cohort level.)*

**Supporting detail:**
- **Molecular pathway (upstream):** KRAB-ZFP → KAP1/TRIM28 → SETDB1 (H3K9me3) / NuRD / DNMT heterochromatin machinery; regulation of RNA polymerase II transcription (GO:0006357). Structural work on the KRAB–KAP1 interface ([PMID: 36341546](https://pubmed.ncbi.nlm.nih.gov/36341546/)) validates this repression axis for other KRAB-ZFPs.
- **Cellular processes:** transcriptional/epigenetic dysregulation during development; possible ribosome-biogenesis defect in hematopoietic precursors.
- **Protein dysfunction:** LoF (truncation) or structural destabilization (KRAB-domain missense disrupting H-bonding) → impaired DNA-binding/repressor function.
- **Suggested GO terms:** GO:0006355 (regulation of DNA-templated transcription), GO:0000122 (negative regulation of transcription by RNA Pol II), GO:0006325 (chromatin organization), GO:0006306 (DNA methylation), GO:0140718 (heterochromatin formation).
- **Suggested CL terms:** CL:0000236 (B cell), CL:0000037 (hematopoietic stem cell), CL:0000048 (multipotent progenitor), CL:0000540 (neuron).

### 7. Anatomical Structures Affected

- **Organ/system level:** craniofacial skeleton, brain/CNS (UBERON:0000955), heart (UBERON:0000948), gastrointestinal tract (UBERON:0001555), genitourinary system (UBERON:0000990), skeletal system (UBERON:0001434), teeth (UBERON:0001091), skin/adnexa (UBERON:0002097), hematopoietic/immune system (UBERON:0002390), ear/cochlea (sensorineural hearing loss), and eye.
- **Airway:** larynx (UBERON:0001737), nasopharynx, tongue base — sites of hamartomatous masses.
- **Tissue/cell level:** epithelial, connective, muscle, and nervous tissues; hematopoietic lineages (esp. B cells and erythroid precursors).
- **Subcellular level:** nucleus (GO:0005634) — site of ZNF699 transcription-factor activity; chromatin/heterochromatin.
- **Lateralization:** malformations are generally bilateral/systemic; craniofacial features are symmetric.

### 8. Temporal Development

- **Onset:** congenital/neonatal; often with IUGR and prematurity. Onset pattern is chronic/congenital, not acute.
- **Progression:** developmental delay persists into childhood; the malformation burden is static (structural), while complications (infections, feeding/airway problems, cardiac failure) are the dynamic drivers of morbidity/mortality.
- **Disease course:** chronic/lifelong for survivors; a subset dies in infancy or early childhood.
- **Critical periods:** embryonic organogenesis (malformation window) and infancy (infection/airway vulnerability window — the key window for supportive intervention).

### 9. Inheritance and Population

- **Inheritance:** autosomal recessive; 28/30 patients homozygous, 2 compound heterozygous (Finding 5).
- **Penetrance/expressivity:** apparently high penetrance but **highly variable expressivity**, including discordant full siblings.
- **Consanguinity/founder effects:** strong association with consanguinity; the founding cohort was predominantly Arab consanguineous families. No formal founder haplotype quantified.
- **Epidemiology:** ultra-rare; <~40 individuals reported worldwide as of 2026; no established prevalence/incidence figures.
- **Demographics:** reported across Middle Eastern, European, Asian, and Hispanic populations. In the Karimi cohort: 20 male / 10 female (apparent male excess, likely ascertainment); ages 1 month–21 years; mean age at diagnosis 4.9 years.
- **Genetic anticipation / mosaicism / carrier frequency:** not applicable / not established.

### 10. Diagnostics

- **Genetic testing (primary):** whole-exome or whole-genome sequencing identifying biallelic *ZNF699* variants is the diagnostic gold standard. Single-gene/panel testing is applicable once suspected.
- **Episignature testing:** the DEGCAGS DNA-methylation episignature is a validated **screening, diagnostic, and variant-classification tool** — able to reclassify VUS and correct misdiagnoses (e.g., away from ADNP/HVDAS), robust even under lymphopenia (Finding 9).
- **Supporting laboratory tests:** CBC (anemia, leukopenia, neutropenia, pancytopenia); immunologic work-up (B-cell depletion, immunoglobulin/lymphocyte subsets).
- **Imaging:** brain MRI (structural/myelin anomalies); echocardiography (congenital heart disease); airway endoscopy (laryngomalacia, hamartomas); skeletal survey.
- **Differential diagnosis:** BAFopathies (Coffin–Siris; episignature overlap), ADNP/Helsmoortel–Van der Aa syndrome, and inherited bone-marrow-failure syndromes / Diamond–Blackfan anemia (hematologic overlap). The episignature and *ZNF699* genotype distinguish DEGCAGS.
- **Screening:** carrier screening and cascade testing are appropriate in consanguineous families; no newborn screening exists.

### 11. Outcome / Prognosis

- **Mortality:** significant infant/childhood mortality. In the Karimi cohort, 3 deaths — Tetralogy-of-Fallot heart failure (6 mo), Dengue (9 mo), and sepsis (8 yr).
- **Morbidity:** high — developmental delay/intellectual disability, recurrent infections, feeding/airway compromise, and multi-organ malformation.
- **Prognostic factors:** severity of cardiac malformation, degree of immunodeficiency, and airway involvement appear to drive outcome. No validated prognostic biomarkers.
- **Recovery:** malformations are structural and non-remitting; developmental deficits persist. Formal survival statistics are unavailable given the small cohort.

### 12. Treatment

**No targeted, pharmacologic, gene, or disease-modifying therapy exists.** Management is **supportive and multidisciplinary** (Finding 4):
- **Airway/ENT:** surgical resection of nasopharyngeal/tongue-base hamartomas with supraglottoplasty; airway monitoring.
- **Respiratory:** infection management, ventilatory support as needed.
- **Immunologic/hematologic:** infection prophylaxis/treatment; transfusion support for cytopenias where indicated.
- **Nutritional/GI:** feeding support.
- **Developmental/rehabilitative:** physical, occupational, and speech therapy.
- **Dental:** management of taurodontism, enamel defects.
- **Cardiac:** correction/management of congenital heart disease.

Suggested NCIT categories: supportive care (NCIT:C15277), surgical intervention (NCIT:C15329), rehabilitation therapy. No experimental trials (NCT identifiers) are registered for DEGCAGS.

### 13. Prevention

- **Genetic counseling:** the mainstay — recurrence risk 25% for future pregnancies of carrier couples; especially relevant in consanguineous families.
- **Reproductive options:** carrier screening, prenatal diagnosis, and preimplantation genetic testing once the familial variants are known.
- **Secondary/tertiary prevention:** early identification and management of infections, airway compromise, and cardiac disease to prevent complications.
- Primary population-level prevention, immunization-specific strategies, and public-health/environmental interventions are **not applicable**.

### 14. Other Species / Natural Disease

- **Orthology:** *ZNF699* was historically proposed as a human ortholog of the *Drosophila* *hangover* (*hang*) gene, but with weak sequence identity (18–26%) and complex mammalian orthology (Finding 8).
- **Natural disease in other species:** none reported (no OMIA entry identified).
- **Comparative/veterinary relevance:** not established. *(Not applicable / not available.)*
- **Zoonotic potential:** not applicable (non-infectious genetic disorder).

### 15. Model Organisms

**No dedicated DEGCAGS animal or cellular disease model has been reported** (Finding 8). No knockout mouse, zebrafish, *Drosophila*, or organoid/iPSC model exists to date. Functional validation is currently limited to human patient DNA-methylation profiling and AlphaFold2-based structural modeling of variants. This is a major gap: without a model system, the causal chain from ZNF699 loss to multisystem malformation and immunodeficiency remains largely inferred.

---

## Mechanistic Model / Interpretation

```
   Biallelic LoF ZNF699 variants (frameshift / nonsense / splice / KRAB-missense)
                                   │
                                   ▼
        Loss of ZNF699 KRAB-C2H2 zinc-finger transcription factor
                                   │  (KRAB → KAP1/TRIM28 → SETDB1/DNMT)  [inferred]
                                   ▼
     Loss of targeted heterochromatin repression (H3K9me3 + DNA methylation)
                                   │
                                   ▼
     Dysregulated DNA methylation  →  promoter-predominant HYPERmethylation
              episignature (~210 DMRs)  [DEMONSTRATED, diagnostic]
                                   │
                                   ▼
        Aberrant expression of downstream developmental target genes
        ┌──────────────────────┬───────────────────────┬─────────────────────┐
        ▼                      ▼                       ▼                     ▼
  Morphogenesis          Hematopoiesis/          Neurodevelopment       Craniofacial/
  (heart, GI, GU,        immunity                (DD/ID, hypotonia,     dental/skin
  skeleton)              (anemia, B-cell         white-matter)          patterning
                         depletion; ?RNA-Pol-II/
                         ribosome biogenesis link)
        └──────────────────────┴───────────────────────┴─────────────────────┘
                                   │
                                   ▼
        Multisystem malformation + immunodeficiency + growth failure
                                   │
                                   ▼
        Recurrent infection / cardiac failure → infant/childhood mortality
```

The unifying interpretation is that **ZNF699 is a KRAB-zinc-finger transcriptional repressor whose loss deregulates the epigenetic control of downstream developmental genes**, producing a broad, variable malformation-plus-neurodevelopmental phenotype. The promoter-hypermethylation episignature is both the strongest experimental evidence for an epigenetic-regulatory mechanism and the most clinically useful diagnostic. The BAFopathy episignature overlap situates DEGCAGS among chromatin/transcription-regulatory ("epigenetic machinery") disorders. The hematologic/immune branch — anemia/pancytopenia and B-cell depletion — is a distinctive, under-explained feature, with a proposed but unproven link to RNA-Pol-II function and ribosome biogenesis (by analogy to *MYSM1*).

---

## Evidence Base

| PMID | Title (abbrev.) | Role | Support |
|---|---|---|---|
| [39424669](https://pubmed.ncbi.nlm.nih.gov/39424669/) | *Epigenomic and phenotypic characterization of DEGCAGS syndrome* | Landmark cohort (n=30) | Causal gene, episignature, frequencies, mortality (F1, F2, F5, F7, F9) |
| [33875846](https://pubmed.ncbi.nlm.nih.gov/33875846/) | *Combining exome/genome sequencing… novel gene-disease associations* | Founding association | First proposal of *ZNF699*/DEGCAGS (F1, F5) |
| [38014480](https://pubmed.ncbi.nlm.nih.gov/38014480/) | *Clinical and ocular abnormalities in DEGCAGS* | Case report | Multisystem spectrum, consanguinity (F3, F4) |
| [41205195](https://pubmed.ncbi.nlm.nih.gov/41205195/) | *Novel Airway Challenges…Infant Laryngeal Hamartomas* | Case report | Airway hamartomas, surgical management (F3, F4) |
| [42569837](https://pubmed.ncbi.nlm.nih.gov/42569837/) | *Expanding the Phenotypic Spectrum…Craniofacial/Oral* | Case report | Craniofacial gestalt, dental findings (F3) |
| [42527142](https://pubmed.ncbi.nlm.nih.gov/42527142/) | *Case of DEGCAGS caused by ZNF699 variation* (Zhu 2026) | Case report | Compound-het variants, leukopenia/neutropenia, recurrent pneumonia (F1, F4, F6) |
| [42534679](https://pubmed.ncbi.nlm.nih.gov/42534679/) | *A novel…* (Giardino 2026) | Case report + immunology | KRAB missense, B-cell depletion, AlphaFold2, episignature reclassification (F6, F9) |
| [16940975](https://pubmed.ncbi.nlm.nih.gov/16940975/) | *Alcohol dependence…ZNF699…Drosophila hangover* | Functional/orthology | Weak *hang* orthology, brain expression (F8) |
| [36341546](https://pubmed.ncbi.nlm.nih.gov/36341546/) | *Structure and functional mapping of the KRAB-KAP1 repressor complex* | Mechanistic (other KRAB-ZFP) | Validates KRAB→KAP1→H3K9me3 repression axis (mechanism) |
| [35205213](https://pubmed.ncbi.nlm.nih.gov/35205213/) | *Further Delineation of DEGCAGS…ZNF699* | Phenotype delineation | Supports phenotype spectrum |

Additional KRAB-ZFP/KAP1 mechanistic papers ([PMID: 30846446](https://pubmed.ncbi.nlm.nih.gov/30846446/), [PMID: 29482634](https://pubmed.ncbi.nlm.nih.gov/29482634/), [PMID: 22496453](https://pubmed.ncbi.nlm.nih.gov/22496453/), [PMID: 21876767](https://pubmed.ncbi.nlm.nih.gov/21876767/), [PMID: 21791101](https://pubmed.ncbi.nlm.nih.gov/21791101/)) provide the general biological framework for how KRAB-ZFP/KAP1 loss deregulates DNA methylation and heterochromatin — the inferred mechanism for the DEGCAGS episignature — but do not directly study ZNF699.

---

## Limitations and Knowledge Gaps

- **Small evidence base:** all conclusions rest on <~40 reported patients, one large cohort, and scattered case reports. Frequency estimates and demographics are subject to ascertainment bias (e.g., apparent male excess).
- **Mechanism is largely inferred:** the KRAB-ZFP/KAP1 → H3K9me3 repression step and the RNA-Pol-II/ribosome-biogenesis hematologic link are hypotheses extrapolated from other KRAB-ZFPs and analogous genes, not directly demonstrated for ZNF699. The direct DNA-binding targets of ZNF699 are unknown.
- **No animal/cellular model:** precludes causal validation, target-gene identification, and therapeutic testing.
- **Unexplained variability:** the discordance between full siblings is unexplained — modifier genes, stochastic epigenetic effects, or environmental factors remain uncharacterized.
- **Missing standard resources:** no Orphanet prevalence, ICD code, QoL data, natural-history study, or registry exists.

## Proposed Follow-up Experiments / Actions

1. **Identify ZNF699 direct targets:** perform CUT&RUN/ChIP-seq for ZNF699 (and KAP1) in relevant human cell types (neural progenitors, hematopoietic precursors) to map binding sites and connect them to the promoter-hypermethylated DMRs.
2. **Test the KAP1 dependency:** co-IP / structure-guided mutagenesis to confirm that ZNF699 recruits KAP1 via its KRAB domain, and that the p.Asn51Lys missense abolishes repression (functional silencing assay, as done for ZNF93 in PMID 36341546).
3. **Generate a model system:** create *Znf699* knockout mice and/or patient iPSC-derived organoids and hematopoietic differentiation cultures to test phenotype recapitulation, especially the B-cell/erythroid defect.
4. **Interrogate the hematologic mechanism:** test the proposed ZNF699–RNA-Pol-II interaction and ribosome-biogenesis hypothesis (polysome profiling, nascent-transcription assays) in patient/model hematopoietic cells; compare to *MYSM1*-deficient models.
5. **Build a natural-history registry:** aggregate reported and new patients to quantify penetrance, survival, genotype–phenotype correlations, and modifier candidates; formally establish prevalence and ontology mappings (Orphanet, ICD-11).
6. **Deploy the episignature clinically:** promote routine methylation-episignature testing to resolve *ZNF699* VUS and correct misdiagnoses, and to detect additional cases in existing methylation-array datasets.

---

*Report compiled from 9 confirmed findings and 18 reviewed papers across 5 investigation iterations. Evidence types: predominantly human clinical (cohort + case reports), with in-silico structural modeling (AlphaFold2) and extrapolated in-vitro/model-organism mechanistic context from the broader KRAB-ZFP/KAP1 literature.*


## Artifacts

- [OpenScientist final report](DEGCAGS_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](DEGCAGS_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 7 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:30846446` (3 mentions) - The KRAB-zinc-finger protein ZFP708 mediates epigenetic repression at RMER19B retrotransposons.
  - shared terms: gene
- `PMID:29482634` (3 mentions) - Individual retrotransposon integrants are differentially controlled by KZFP/KAP1-dependent histone methylation, DNA methylation and TET-mediated hydroxymethylation in naïve embryonic stem cells.
  - shared terms: gene
- `PMID:21791101` (3 mentions) - A gene-rich, transcriptionally active environment and the pre-deposition of repressive marks are predictive of susceptibility to KRAB/KAP1-mediated silencing.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `znf699`, `degcag`, `gene`, `variant`, `developmental`, `patient`, `cohort`, `airway`, `disorder`, `episignature`, `hematologic`, `malformation`, `syndrome`, `delay`, `infection`, `disease`, `structural`, `skeletal`, `loss`, `mortality`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 49 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0000955` (1 mention) - the report calls it "Organ/system level:** craniofacial skeleton, brain/CNS"; UBERON calls it **brain**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006306` (obsolete DNA methylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001601` (1 mention) - the report calls it "Airway/respiratory:** laryngomalacia"; HP calls it **Laryngomalacia**
- `GO:0000122` (1 mention) - the report calls it "negative regulation of transcription by RNA Pol II"; GO calls it **negative regulation of transcription by RNA polymerase II**
- `GO:0006306` (1 mention) - the report calls it "DNA methylation"; GO calls it **obsolete DNA methylation**
- `GO:0140718` (1 mention) - the report calls it "heterochromatin formation"; GO calls it **facultative heterochromatin formation**
- `CL:0000048` (1 mention) - the report calls it "multipotent progenitor"; CL calls it **multi fate stem cell**, and lists "multipotent cell" among its other names
- `UBERON:0001737` (1 mention) - the report calls it "Airway:** larynx"; UBERON calls it **larynx**
- `GO:0005634` (1 mention) - the report calls it "Subcellular level:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names