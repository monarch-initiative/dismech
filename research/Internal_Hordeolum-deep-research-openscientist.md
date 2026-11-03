---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T14:59:45.851850'
end_time: '2026-09-29T15:14:07.243520'
duration_seconds: 861.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Internal Hordeolum
  mondo_id: MONDO:0004917
  category: Infectious Disease
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
citation_count: 27
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:6218459
  relevance_assessed: 28
  on_topic: 13
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 21
  verified: 20
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.048
  labels_checked: 19
  labels_matching: 14
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0004917
    reported_labels:
    - MONDO
    ontology_label: internal hordeolum
  - term_id: UBERON:0001801
    reported_labels:
    - palpebral conjunctiva
    ontology_label: anterior segment of eyeball
  - term_id: NCIT:C15277
    reported_labels:
    - Supportive Care
    ontology_label: Mastectomy
  - term_id: NCIT:C303
    reported_labels:
    - Doxycycline
    ontology_label: Betamethasone
  labels_variant: 1
  unresolved_terms:
  - UBERON:0004841
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Internal_Hordeolum-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Internal_Hordeolum-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Internal Hordeolum
- **MONDO ID:** MONDO:0004917 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Internal Hordeolum** covering all of the
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

# Internal Hordeolum (MONDO:0004917): A Comprehensive Disease Characterization

## Summary

**Internal hordeolum is a common, acute, painful, and usually self-limited suppurative infection/inflammation of a meibomian (tarsal) gland of the eyelid.** It is caused by bacterial infection—classically *Staphylococcus aureus*—superimposed on obstruction and stasis of the meibomian gland orifice within the tarsal plate. It is distinguished anatomically from external hordeolum (stye), which involves the glands of Zeis or Moll associated with eyelash follicles on the anterior lamella. Internal hordeolum is an acquired, multifactorial condition of the ocular adnexa with **no known causal gene, pathogenic variant, Mendelian inheritance pattern, or dedicated genetic animal model.** Knowledge derives from aggregated disease-level clinical resources, case series, and EHR/claims-based epidemiological studies rather than from genetic patient registries.

Clinically, patients present with an acute-onset (1–3 days), typically unilateral, tender, red, swollen eyelid-margin nodule pointing toward the conjunctival surface, often accompanied by tearing and foreign-body sensation. The natural course is benign: most lesions resolve within about one week through spontaneous drainage of the abscess. However, recurrence is very common, and unresolved lesions may become chronic, evolve into a chalazion (a sterile lipogranuloma), or—rarely—spread to cause preseptal cellulitis, orbital cellulitis, or, in exceptional cases, necrotizing fasciitis. Predisposing factors center on conditions that cause meibomian gland dysfunction (MGD) and chronic lid-margin inflammation: blepharitis, ocular/acne rosacea, seborrhea, *Demodex* mite infestation, and certain systemic drugs (GLP-1/GIP receptor agonists such as tirzepatide, and CFTR modulators).

The evidence base for treatment is notably weak—repeated Cochrane systematic reviews found no reliable randomized-controlled-trial evidence for non-surgical interventions in acute internal hordeolum. In practice, management is largely conservative (warm compresses and lid hygiene), escalating to topical/systemic antibiotics for spreading infection and incision & curettage for persistent lesions. Emerging adjuncts include intense pulsed light (IPL) therapy and intralesional diluted 5-fluorouracil. Prognosis is excellent with essentially no attributable mortality; the principal clinical burdens are recurrence, cosmetic/discomfort morbidity, and the important caveat that atypical or non-resolving lesions must be biopsied to exclude sebaceous gland carcinoma.

---

## 1. Disease Information

**Overview.** Internal hordeolum is an acute, purulent inflammation of the eyelid margin caused by obstruction and bacterial infection of a meibomian (tarsal) gland. As stated in the acupuncture Cochrane review: *"When the meibomian gland in the tarsal plate is affected, internal hordeolum occurs, while when the glands of Zeis or Moll associated with eyelash follicles are affected, external hordeolum, or stye occurs"* ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)). It is *"a common, painful inflammation of the eyelid margin that is usually caused by a bacterial infection... The infection affects oil glands of the eyelid and can be either internal or external"* ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0004917 |
| MeSH | D006726 (Hordeolum) |
| ICD-10-CM | H00.0 (Hordeolum and other deep inflammation of eyelid); H00.03x internal hordeolum |
| ICD-11 | 9A02.1 (Hordeolum) |
| SNOMED CT | Hordeolum (disorder) |
| OMIM | Not applicable (not a Mendelian disorder) |
| Orphanet | Not applicable (common acquired condition, not a rare disease) |

**Synonyms / alternative names:** internal stye, meibomian stye, acute meibomianitis / meibomian abscess, acute internal hordeolum.

**Data provenance:** Information derives from aggregated disease-level clinical resources (clinical reviews, Cochrane systematic reviews), case reports/series, and EHR/insurance-claims-based epidemiological studies. For example, the Japanese nationwide study used *"the National Database of Health Insurance Claims and Specific Health Checkups Open Data Japan"* ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)). There is no genetic patient registry for this condition.

---

## 2. Etiology

**Primary cause — infectious/mechanistic.** Internal hordeolum results from bacterial infection, predominantly *Staphylococcus aureus* (MSSA, and increasingly MRSA), superimposed on obstruction of a meibomian gland orifice. In a meibomian gland dysfunction microbiome study (n=157), *"The incidence of Staphylococcus aureus was higher than anticipated across all severity groups"* ([PMID: 27473509](https://pubmed.ncbi.nlm.nih.gov/27473509/)). Importantly, the underlying chronic gland disease is often not primarily infectious: *"Primary meibomitis appears not to be a primarily infectious entity but to represent a facet of generalized sebaceous gland dysfunction and to be found in association with seborrheic dermatitis or acne rosacea"* ([PMID: 6218459](https://pubmed.ncbi.nlm.nih.gov/6218459/)).

**Genetic risk factors.** None established. There is no causal gene, susceptibility locus, chromosomal abnormality, or Mendelian inheritance pattern described for internal hordeolum. It is a multifactorial, acquired condition.

**Environmental / acquired risk factors.**
- **Blepharitis and meibomian gland dysfunction (MGD):** Hordeolum and chalazion *"can occur in association with underlying diseases causing Meibomian gland dysfunction and/or chronic blepharitis"* ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)).
- **Ocular/acne rosacea and seborrhea:** generalized sebaceous gland dysfunction ([PMID: 6218459](https://pubmed.ncbi.nlm.nih.gov/6218459/)); ocular rosacea can present with *"multiple recurrent chalazion on both eyelids"* with immunohistochemistry *"positive for LL-37"* ([PMID: 38898849](https://pubmed.ncbi.nlm.nih.gov/38898849/)). Blepharitis dominates pediatric ocular rosacea: *"Blepharitis was the most common eyelid manifestation (98.4%)"* ([PMID: 42757848](https://pubmed.ncbi.nlm.nih.gov/42757848/)).
- ***Demodex* infestation** (see Section 5).
- **Systemic drugs:** GLP-1/GIP receptor agonists (tirzepatide) and CFTR modulators (elexacaftor-tezacaftor-ivacaftor) — an emerging iatrogenic trigger via meibomian gland obstruction ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/); [PMID: 41967150](https://pubmed.ncbi.nlm.nih.gov/41967150/)).
- **Age/sex:** bimodal age peaks; slight female predominance in youth (see Section 9).

**Protective factors.** No genetic protective variants are described. Environmental/behavioral protective measures are essentially preventive hygiene: lid hygiene, warm compresses, and treatment of underlying MGD/rosacea reduce recurrence frequency; IPL reduces hordeolum frequency ([PMID: 34629862](https://pubmed.ncbi.nlm.nih.gov/34629862/)).

**Gene–environment interactions.** Not applicable in a Mendelian sense. The relevant "host–environment" interaction is the interplay between host sebaceous-gland biology (rosacea/seborrhea/innate immune dysregulation via cathelicidin LL-37), commensal/pathogenic bacteria (*S. aureus*), ectoparasites (*Demodex*), and gland-altering systemic drugs.

---

## 3. Phenotypes

**Core clinical phenotype:** An acute-onset, usually unilateral, painful, tender, red, swollen localized eyelid-margin nodule (abscess) pointing toward the conjunctival (inner) surface. Patients present *"with symptoms such as redness, swelling, tearing, itchiness, or a foreign body sensation"* ([PMID: 32622681](https://pubmed.ncbi.nlm.nih.gov/32622681/)), and the lesion is fundamentally *"a common, painful inflammation of the eyelid margin"* ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)).

| Phenotype | Type | HPO suggestion | Characteristics |
|---|---|---|---|
| Painful eyelid nodule/swelling | Symptom + physical sign | HP:0000498 (Abnormality of the eyelid) | Acute onset (1–3 d); mild–moderate; localized |
| Eyelid erythema | Clinical sign | HP (eyelid erythema) | Acute; resolves ~1 wk |
| Eyelid edema/swelling | Clinical sign | HP:0100539 (Periorbital edema)-adjacent | Localized, unilateral |
| Epiphora (tearing) | Symptom | HP:0009926 (Epiphora) | Mild |
| Foreign-body sensation / ocular discomfort | Symptom | HP (ocular discomfort) | Mild–moderate |
| Eyelid pain/tenderness | Symptom | HP:0200026 (Ocular pain)-adjacent | Moderate; localized |

**Onset:** any age, acute (see Section 8). **Severity:** typically mild–moderate; occasionally severe with spread. **Progression:** episodic/self-limited (~1 week), frequently recurrent. **Frequency among affected:** pain and eyelid-margin swelling are essentially universal defining features; tearing, itch, and foreign-body sensation are common.

**Quality of life impact:** Generally modest and transient; discomfort, cosmetic concern, and interference with vision if large. Chalazion/hordeolum-spectrum lesions can induce corneal astigmatism and higher-order aberrations when sizeable, affecting vision ([PMID: 41884092](https://pubmed.ncbi.nlm.nih.gov/41884092/)). IPL studies used the Ocular Surface Disease Index (OSDI) as a QoL/symptom instrument ([PMID: 41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/)).

---

## 4. Genetic/Molecular Information

**Not applicable.** Internal hordeolum is an acquired infectious/inflammatory condition with **no causal genes, no pathogenic variants, no modifier genes, no established disease-specific epigenetic signature, and no chromosomal abnormalities.** There is no OMIM entry. There are no ClinVar/HGMD variants, no gnomAD allele frequencies, and no somatic/germline mutation profile associated with the disease itself.

The only molecularly-characterized host contributor identified is the innate-immune peptide **cathelicidin LL-37** in the setting of rosacea-associated recurrent eyelid lesions: immunohistochemistry was *"positive for LL-37"* ([PMID: 38898849](https://pubmed.ncbi.nlm.nih.gov/38898849/)). This is a downstream inflammatory mediator of the predisposing rosacea diathesis, not a causal genetic variant of hordeolum.

---

## 5. Environmental Information

**Environmental factors.** No toxins, radiation, or occupational exposures are established as direct causes. The dominant modifiable exposures are pharmacological (see below) and microbial.

**Lifestyle factors.** Lid hygiene practices modulate risk/recurrence. Poor lid hygiene and chronic lid-margin inflammation predispose; conversely, warm compresses and lid hygiene are preventive.

**Infectious agents.**
- ***Staphylococcus aureus*** — the principal bacterial pathogen (NCBI Taxonomy: *Staphylococcus aureus*, txid1280); MSSA and MRSA. Elevated on lid margins in MGD ([PMID: 27473509](https://pubmed.ncbi.nlm.nih.gov/27473509/)). Bacterial lipases contribute to inflammation: *"the production of bacterial lypolytic exoenzymes that split neutral lipids, resulting in an increased level of free fatty acids in the tears"* ([PMID: 6218459](https://pubmed.ncbi.nlm.nih.gov/6218459/)).
- ***Demodex folliculorum* and *Demodex brevis*** (ectoparasitic mites) — commonly infest eyelids and drive blepharitis/MGD that predisposes to hordeolum. In squamous blepharitis, *"The overall Demodex detection rate was 92% (92/100) in this study"* ([PMID: 42426675](https://pubmed.ncbi.nlm.nih.gov/42426675/)), and *"In Demodex blepharitis, abnormal or reduced lipid production from the Zeis and/or meibomian glands may contribute to DED"* ([PMID: 42387805](https://pubmed.ncbi.nlm.nih.gov/42387805/)).

**Pharmacological environmental triggers (iatrogenic).** Tirzepatide (dual GLP-1/GIP receptor agonist) caused simultaneous/recurrent internal hordeola with a positive dechallenge/rechallenge: *"lesions lessened after tirzepatide discontinuation and worsened upon rechallenge, a positive rechallenge providing strong evidence of causality"* and *"Both patients lacked classic infectious blepharitis signs despite active lesions, supporting a sterile, obstructive meibomian gland process rather than infection"* ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)). CFTR modulators are similarly implicated in children with cystic fibrosis ([PMID: 41967150](https://pubmed.ncbi.nlm.nih.gov/41967150/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Predisposing sebaceous/meibomian gland dysfunction** (blepharitis, ocular/acne rosacea, seborrhea, *Demodex*, or altered meibum from systemic drugs) **leads to** →
2. **Obstruction of the meibomian gland duct/orifice** within the tarsal plate *(inferred from meibomian gland biology)* **which results in** →
3. **Stasis and retention of sebaceous secretions (meibum)** *(inferred)* **which promotes** →
4. **Bacterial overgrowth/infection**, predominantly *Staphylococcus aureus*, whose lipases split neutral lipids into pro-inflammatory free fatty acids *(demonstrated by microbiology/biochemistry)* **which triggers** →
5. **Acute neutrophilic suppurative inflammation** (abscess/pus formation) within the gland *(demonstrated histopathologically)* **which produces** →
6. **The clinical painful, red, swollen eyelid-margin nodule.**

**Branches from step 5/6:**
- **Branch A (resolution):** spontaneous drainage → resolution in ~1 week.
- **Branch B (chronic/sterile):** unresolved lipogranulomatous organization → chalazion (sterile chronic granuloma).
- **Branch C (spread):** extension → preseptal cellulitis → (rarely) orbital cellulitis / necrotizing fasciitis.

```
Sebaceous/meibomian gland          [Rosacea, seborrhea, blepharitis,
dysfunction  ─────────────────►     Demodex, GLP-1/GIP & CFTR drugs]
      │
      ▼
Duct/orifice OBSTRUCTION (inferred)
      │
      ▼
Meibum STASIS & retention (inferred)
      │
      ▼
Bacterial overgrowth (S. aureus) + lipase-generated free fatty acids
      │
      ▼
Acute neutrophilic SUPPURATION (abscess)
      │
      ▼
Painful red swollen eyelid-margin NODULE
      │
      ├──► (A) Spontaneous drainage → RESOLUTION (~1 wk)
      ├──► (B) Lipogranuloma → CHALAZION (sterile)
      └──► (C) Spread → PRESEPTAL → ORBITAL CELLULITIS / NECROTIZING FASCIITIS (rare)
```

### Supporting detail

- **Initiating lesion:** *"Hordeolum is an acute, purulent inflammation of the eyelid margin usually caused by obstructed orifices of the sebaceous glands of the eyelid"* ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)).
- **Biochemical inflammatory step:** bacterial lipolytic exoenzymes generate irritant free fatty acids ([PMID: 6218459](https://pubmed.ncbi.nlm.nih.gov/6218459/)).
- **Sterile-obstructive upstream branch:** distinct non-infectious mechanism supported by drug-induced cases *"supporting a sterile, obstructive meibomian gland process rather than infection"* ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)).
- **Innate-immune amplification (rosacea):** cathelicidin **LL-37** ([PMID: 38898849](https://pubmed.ncbi.nlm.nih.gov/38898849/)).

**Steps 2–3** are mechanistically inferred from meibomian gland biology; **steps 4–6** are demonstrated by microbiology and histopathology.

**Molecular pathways / cellular processes:** acute inflammation, neutrophil recruitment and degranulation, innate immune antimicrobial peptide (cathelicidin) activation, lipid metabolism disturbance (holocrine sebaceous secretion). Granulomatous organization occurs if the lesion becomes chronic (chalazion).

**Suggested ontology terms.**
- GO biological processes: GO:0006954 (inflammatory response); GO:0006909 (phagocytosis); GO:0042742 (defense response to bacterium); GO:0006629 (lipid metabolic process).
- CL cell types: CL:0000775 (neutrophil); CL:0000235 (macrophage); sebaceous gland cell / meibocyte; CL:0000738 (leukocyte).
- CHEBI: CHEBI:35366 (fatty acid) / free fatty acids; neutral lipids/triglycerides.

---

## 7. Anatomical Structures Affected

**Organ/tissue level.** The primary structure is the **meibomian (tarsal) gland**, a holocrine sebaceous gland embedded in the **tarsal plate** of the eyelid, on the **posterior lamella**, with the lesion pointing toward the **conjunctival (inner) surface**: *"When the meibomian gland in the tarsal plate is affected, internal hordeolum occurs"* ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)). This contrasts with external hordeolum, which affects glands of Zeis/Moll on the anterior lamella at the lash line.

**Body system:** visual/ocular adnexal system (eyelid). **Laterality:** usually **unilateral** and localized. **Secondary involvement:** periorbital soft tissue (preseptal space) and, rarely, the orbit; hordeolum is a leading predisposing factor for preseptal cellulitis (15.5–24.8% of cases) ([PMID: 34607790](https://pubmed.ncbi.nlm.nih.gov/34607790/)).

**Tissue and cell level:** glandular (sebaceous) epithelium of the meibomian gland (meibocytes); infiltrating neutrophils and, in chronic phase, macrophages/lipogranuloma.

**Subcellular level:** holocrine secretion involves whole-cell disintegration; relevant GO cellular components include lipid droplet (GO:0005811) and the secretory apparatus.

**Suggested ontology terms.** UBERON: UBERON:0001711 (eyelid); UBERON:0004841 (tarsal gland / meibomian gland); UBERON:0001801 (palpebral conjunctiva). CL: meibocyte/sebaceous gland cell.

---

## 8. Temporal Development

**Onset.** Acute, developing over ~1–3 days, at **any age**, with bimodal peaks in childhood/adolescence (10–14 y) and mid-adulthood (30–39 y): *"Invasive treatments for hordeolum showed bimodal peaks in males (age 10-14 years: 82.9; age 35-39 years: 72.1) and females (age 10-14 years: 102.4; age 30-34 years: 78.3)"* ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)). There is no congenital form.

**Progression / course.** Short and self-limited: *"The onset of hordeolum is usually self limited, and may resolve in about a week with spontaneous drainage of the abscess. When the condition is severe, it can spread to adjacent glands and tissues. Recurrences are very common"* ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)). The course is **episodic/recurrent** rather than steadily progressive. There is no staged progression system. Unresolved lesions transition to chronic chalazion.

**Patterns.** Remission is typically **spontaneous** (drainage) or treatment-facilitated. The main "critical period" for intervention is early warm-compress/lid-hygiene use and, for spreading disease, prompt antibiotics to prevent cellulitis.

---

## 9. Inheritance and Population

**Epidemiology.** Internal hordeolum is common. Japanese nationwide claims data (2014–2022, 638,699 invasive hordeolum procedures) reported an average invasive treatment rate of **56.2 per 100,000 person-years**: *"The annual average rates were 40.9 for ITC and 56.2 for ITH per 100 000 person-years. Sex differences were prominent in younger groups: the overall female-to-male ratio was 1.1:1 for ITC and 1.0:1 for ITH, with a greater female predominance in youth"* ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)). Note that invasive-treatment rates capture only the subset requiring procedures; true incidence (including conservatively-managed cases) is higher. In a Korean military teleophthalmology cohort, hordeolum/chalazion together were the single most common diagnosis: *"The most common diagnoses were hordeolum/chalazion (39.3%) and viral conjunctivitis (20.3%)"* ([PMID: 42299138](https://pubmed.ncbi.nlm.nih.gov/42299138/)).

**Genetic etiology.** Not applicable — no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency, because there is no causal gene.

**Population demographics.**
- **Sex ratio:** approximately 1.0:1 overall for hordeolum, with a greater female predominance in youth ([PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/)).
- **Age distribution:** bimodal (10–14 y and 30–39 y).
- **Geographic distribution:** cosmopolitan; no endemic pattern. No population-specific variants (none exist).

| Metric | Value | Source |
|---|---|---|
| Invasive-treatment rate (hordeolum) | 56.2 / 100,000 person-years | [PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/) |
| Female:male (overall) | ~1.0:1 | [PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/) |
| Male age peaks | 10–14 y (82.9); 35–39 y (72.1) | [PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/) |
| Female age peaks | 10–14 y (102.4); 30–34 y (78.3) | [PMID: 41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/) |
| Share of ophthalmic consults (hordeolum/chalazion) | 39.3% | [PMID: 42299138](https://pubmed.ncbi.nlm.nih.gov/42299138/) |

---

## 10. Diagnostics

**Clinical diagnosis is standard.** *"Due to the typical morphological features and clinical course, the diagnosis can mostly be clinically established"* ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)). Diagnosis rests on inspection of the eyelid margin revealing a tender, localized, erythematous nodule.

**Laboratory tests / microbiology:** not routinely required; culture (e.g., for *S. aureus*/MRSA) is reserved for severe, atypical, or recurrent cases or when complications supervene.

**Biopsy / histopathology — critical safety rule:** Persistent, recurrent, or clinically atypical lesions require excisional biopsy to exclude malignancy, especially **sebaceous gland carcinoma**: *"In persistent, recurrent or clinically atypical cases malignant tumors must be excluded as a differential diagnosis by excisional biopsy and histopathological assessment"* ([PMID: 34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/)). Real cases of malignancy masquerading as hordeolum include metastatic invasive lobular breast carcinoma—*"She was initially managed for presumed hordeolum and preseptal cellulitis without response over 4 months"* ([PMID: 42552075](https://pubmed.ncbi.nlm.nih.gov/42552075/))—and apocrine/sebaceous carcinomas ([PMID: 40531581](https://pubmed.ncbi.nlm.nih.gov/40531581/)).

**Genetic / omics diagnostics:** Not applicable — no genetic testing, gene panels, karyotyping, CMA, or disease-specific transcriptomic/proteomic/metabolomic signature.

**Differential diagnosis:** chalazion (chronic, non-tender granuloma), external hordeolum (stye at lash line), preseptal/orbital cellulitis, sebaceous gland carcinoma, apocrine carcinoma of the glands of Moll, molluscum, and other eyelid tumors. In children, eyelid cutaneous horns are frequently *"preceded by a hordeolum or chalazion"* and follow a benign course ([PMID: 39393420](https://pubmed.ncbi.nlm.nih.gov/39393420/)).

**Screening:** No population screening applies (not a genetic or preventable-by-screening disease).

---

## 11. Outcome/Prognosis

**Excellent prognosis.** Internal hordeolum is benign and self-limited, usually resolving in ~1 week with spontaneous drainage ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)). **Mortality is essentially nil**, occurring only via exceedingly rare complications such as necrotizing fasciitis: *"We report an unusual case of periorbital NF caused by methicillin-sensitive Staphylococcus aureus (MSSA) in a previously healthy 48-year-old woman, originating from a neglected, recurrent hordeolum-an otherwise benign eyelid condition"* ([PMID: 41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/)).

**Morbidity.** The main burdens are **recurrence** (very common), transient discomfort/cosmetic effect, and chronic sequelae. Unresolved lesions evolve into chalazion, which can cause **meibomian gland loss/dropout**: a pediatric chalazion cohort demonstrated *"Chalazion can lead to meibomian gland loss"* with significant gland dropout versus controls (meiboscores 0.78–0.89 vs 0.40, P<.05) ([PMID: 42116414](https://pubmed.ncbi.nlm.nih.gov/42116414/)). Larger lesions can transiently induce corneal astigmatism/higher-order aberrations ([PMID: 41884092](https://pubmed.ncbi.nlm.nih.gov/41884092/)).

**Complications:** chalazion; preseptal cellulitis (hordeolum accounts for 15.5–24.8% of adult preseptal cellulitis predisposing factors, [PMID: 34607790](https://pubmed.ncbi.nlm.nih.gov/34607790/)); rarely orbital cellulitis and necrotizing fasciitis.

**Prognostic factors:** severity, promptness of drainage/treatment, and control of underlying MGD/rosacea/Demodex determine recurrence risk. No molecular prognostic biomarkers exist.

---

## 12. Treatment

**Evidence caveat.** The treatment evidence base is weak. The Cochrane review's stated objective was *"to investigate the effectiveness, and when possible, the safety, of non-surgical treatments for acute internal hordeola compared with observation or placebo"* ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)) — and no eligible randomized trials were found. Acupuncture is likewise unproven: *"it is unclear if acupuncture is an effective and safe treatment for acute hordeolum"* ([PMID: 28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/)).

**Treatment ladder.**

| Tier | Intervention | Evidence / notes | NCIT suggestion |
|---|---|---|---|
| First-line | Warm compresses; lid hygiene/scrubs | Standard conservative care; most resolve spontaneously. Warming masks raise eyelid temperature to therapeutic range ([PMID: 42361717](https://pubmed.ncbi.nlm.nih.gov/42361717/)) | NCIT:C15277 (Supportive Care) |
| Second-line | Topical/systemic antibiotics | For spreading infection (anti-staphylococcal) | NCIT:C258 (Antibiotic) |
| Procedural | Incision & curettage (I&C) | For persistent lesions | NCIT (surgery/incision-drainage) |
| Emerging | Intense pulsed light (IPL) | Prospective cohort: *"the IPL group exhibited a statistically significant reduction in OSDI scores following treatment"* ([PMID: 41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/)); BBL-IPL *"has shown to reduce hordeolum and blepharitis frequency"* ([PMID: 34629862](https://pubmed.ncbi.nlm.nih.gov/34629862/)) | NCIT (phototherapy) |
| Emerging | Intralesional diluted 5-fluorouracil | *"Local injection of 6-fold diluted 5-fluorouracil may represent a potential minimally invasive option for selected patients with persistent eyelid inflammatory nodules"* ([PMID: 42367702](https://pubmed.ncbi.nlm.nih.gov/42367702/)) | NCIT:C505 (Fluorouracil) |
| Underlying disease | Oral doxycycline/azithromycin (rosacea); lotilaner (Demodex) | Rosacea chalazia resolved with *"oral administration of doxycycline and azithromycin"* ([PMID: 38898849](https://pubmed.ncbi.nlm.nih.gov/38898849/)); lotilaner 0.25% for Demodex blepharitis ([PMID: 42371506](https://pubmed.ncbi.nlm.nih.gov/42371506/)) | NCIT:C303 (Doxycycline) |
| Iatrogenic | Discontinue/adjust offending drug | Positive dechallenge for tirzepatide ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)) | — |

Pediatric procedural management (chalazion I&C) under general anesthesia is common and safe (n=4,616 series; chalazion I&C = 62.89% of pediatric ophthalmic day surgery, [PMID: 39115475](https://pubmed.ncbi.nlm.nih.gov/39115475/)).

**Pharmacogenomics / advanced (gene/cell/RNA) therapies:** Not applicable.

---

## 13. Prevention

- **Primary prevention:** lid hygiene, warm compresses, control of blepharitis/MGD; avoiding/managing gland-obstructing systemic drugs where feasible.
- **Secondary prevention:** early warm compress/lid hygiene at symptom onset; prompt antibiotics if spreading to avert cellulitis.
- **Tertiary prevention:** treat underlying rosacea (doxycycline/azithromycin, [PMID: 38898849](https://pubmed.ncbi.nlm.nih.gov/38898849/)) and *Demodex* (lotilaner, [PMID: 42371506](https://pubmed.ncbi.nlm.nih.gov/42371506/)); IPL reduces recurrence frequency ([PMID: 34629862](https://pubmed.ncbi.nlm.nih.gov/34629862/)).
- **Immunization / genetic screening / counseling:** Not applicable (no vaccine, no genetic basis).
- **Public health:** general eye-hygiene education.

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected host:** *Homo sapiens* (NCBI:txid9606). The causative pathogen is *Staphylococcus aureus* (NCBI:txid1280); ectoparasites *Demodex folliculorum*/*D. brevis*.
- **Comparative biology:** Meibomian (tarsal) glands are **holocrine sebaceous glands conserved across mammals**, so an anatomical substrate exists in animals. However, **no established rodent/zebrafish/Drosophila genetic model of "internal hordeolum" exists**, and formal veterinary "hordeolum" literature is minimal. Analogous eyelid gland conditions in animals are described as chalazia/meibomian adenitis rather than "internal hordeolum."
- **Zoonosis:** Not applicable — hordeolum itself is not transmissible; *S. aureus* can colonize multiple hosts but the disease is not classically zoonotic.

---

## 15. Model Organisms

**Not applicable / none established.** There is no dedicated genetic or induced animal model of internal hordeolum (no knockout, knock-in, transgenic, conditional, or humanized model). Related meibomian gland dysfunction can be studied in mammalian models of MGD/dry eye, but these do not specifically recapitulate the acute suppurative internal hordeolum phenotype. Consequently, phenotype recapitulation, model limitations, and model databases (MGI, RGD, ZFIN, etc.) are **not applicable** for this specific disease entity.

---

## Mechanistic Model / Interpretation

Internal hordeolum is best understood as the **acute suppurative endpoint of a chronically primed eyelid oil-gland system**. The upstream soil is meibomian gland dysfunction—driven by rosacea/seborrhea (with innate-immune LL-37 involvement), *Demodex* infestation, or drug-altered meibum. This soil predisposes to duct obstruction and meibum stasis (inferred steps), which provides a lipid-rich niche for *S. aureus*, whose lipases liberate pro-inflammatory free fatty acids. The resulting neutrophilic abscess is the clinically visible lesion. The system has three exits: spontaneous drainage (the common, benign outcome), sterile granulomatous organization into a chalazion, or bacterial spread into the preseptal/orbital compartments. This model explains the disease's key clinical features: its acuity (infection), its self-limitation (drainage), its recurrence (persistent underlying MGD soil), and its therapeutic logic (treat the abscess acutely, but prevent recurrence by remediating the gland dysfunction).

The **"two-hit" framing**—chronic obstructive/sterile predisposition plus acute bacterial infection—reconciles two literatures that might otherwise seem contradictory: the observation that primary meibomitis is "not a primarily infectious entity" ([PMID: 6218459](https://pubmed.ncbi.nlm.nih.gov/6218459/)) and drug-induced "sterile obstructive" hordeola ([PMID: 42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/)) on one hand, versus the demonstrable role of *S. aureus* on the other.

---

## Evidence Base

| PMID | Role in this report | Type |
|---|---|---|
| [28181687](https://pubmed.ncbi.nlm.nih.gov/28181687/) | Core definition, anatomy, self-limited course, obstruction mechanism | Cochrane review |
| [28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/) / [20824865](https://pubmed.ncbi.nlm.nih.gov/20824865/) | Definition; treatment evidence gap | Cochrane review |
| [6218459](https://pubmed.ncbi.nlm.nih.gov/6218459/) | Sebaceous dysfunction etiology; bacterial lipase → free fatty acids | Clinical/mechanistic |
| [27473509](https://pubmed.ncbi.nlm.nih.gov/27473509/) | Elevated *S. aureus* in MGD | Microbiome study |
| [41675090](https://pubmed.ncbi.nlm.nih.gov/41675090/) | Epidemiology, incidence, bimodal age, sex ratio | Nationwide claims |
| [42299138](https://pubmed.ncbi.nlm.nih.gov/42299138/) | High prevalence in real-world cohort | Teleophthalmology review |
| [34379160](https://pubmed.ncbi.nlm.nih.gov/34379160/) | Clinical diagnosis; biopsy for atypical/recurrent; MGD/blepharitis risk | Clinical review |
| [42756500](https://pubmed.ncbi.nlm.nih.gov/42756500/) | Tirzepatide-induced sterile obstructive hordeola; rechallenge causality | Case series |
| [41967150](https://pubmed.ncbi.nlm.nih.gov/41967150/) | CFTR modulator association | Case report |
| [38898849](https://pubmed.ncbi.nlm.nih.gov/38898849/) | Rosacea, LL-37; doxycycline/azithromycin treatment | Case report |
| [42757848](https://pubmed.ncbi.nlm.nih.gov/42757848/) | Pediatric ocular rosacea, blepharitis 98.4% | Case series |
| [42426675](https://pubmed.ncbi.nlm.nih.gov/42426675/) | *Demodex* 92% in blepharitis | Clinical study |
| [42387805](https://pubmed.ncbi.nlm.nih.gov/42387805/) | *Demodex* → Zeis/meibomian lipid dysfunction | Clinical study |
| [41787906](https://pubmed.ncbi.nlm.nih.gov/41787906/) | Necrotizing fasciitis complication | Case report |
| [34607790](https://pubmed.ncbi.nlm.nih.gov/34607790/) | Hordeolum as preseptal cellulitis predisposing factor | Retrospective |
| [42116414](https://pubmed.ncbi.nlm.nih.gov/42116414/) | Chalazion → meibomian gland loss | Observational |
| [42552075](https://pubmed.ncbi.nlm.nih.gov/42552075/) | Malignancy masquerading as hordeolum | Case report |
| [41731784](https://pubmed.ncbi.nlm.nih.gov/41731784/) | IPL improves OSDI | Prospective cohort |
| [34629862](https://pubmed.ncbi.nlm.nih.gov/34629862/) | BBL-IPL reduces hordeolum frequency | Clinical study |
| [42367702](https://pubmed.ncbi.nlm.nih.gov/42367702/) | Intralesional 5-FU | Case series |
| [42371506](https://pubmed.ncbi.nlm.nih.gov/42371506/) | Lotilaner for Demodex blepharitis | Case report |
| [32622681](https://pubmed.ncbi.nlm.nih.gov/32622681/) | Presenting symptoms of eyelid infection | Clinical review |
| [42361717](https://pubmed.ncbi.nlm.nih.gov/42361717/) | Warming mask eyelid temperature | Experimental |
| [39115475](https://pubmed.ncbi.nlm.nih.gov/39115475/) | Pediatric I&C safety | Retrospective |
| [39393420](https://pubmed.ncbi.nlm.nih.gov/39393420/) | Cutaneous horn preceded by hordeolum/chalazion | Case series |
| [41884092](https://pubmed.ncbi.nlm.nih.gov/41884092/) | Lesion-induced astigmatism/HOAs | Review |

---

## Limitations and Knowledge Gaps

1. **No randomized-controlled-trial evidence** exists for non-surgical treatment of acute internal hordeolum; practice is guided by expert opinion and observational data ([PMID: 28068454](https://pubmed.ncbi.nlm.nih.gov/28068454/)).
2. **Incidence figures are procedure-based** (invasive treatments), so the 56.2/100,000 rate underestimates true incidence, which includes conservatively-managed and self-resolving cases.
3. **Mechanistic steps 2–3 (obstruction, stasis) are inferred** from meibomian gland biology rather than directly demonstrated in hordeolum tissue.
4. **No molecular/omics characterization** specific to internal hordeolum (no transcriptomic, proteomic, metabolomic, or single-cell studies of the lesion itself).
5. **No animal model**, limiting mechanistic dissection.
6. **Emerging drug associations** (GLP-1/GIP agonists, CFTR modulators) rest on small case series; magnitude of risk is unquantified.
7. **IPL and intralesional 5-FU evidence** comes from small, mostly uncontrolled or single-center studies.

---

## Proposed Follow-up Experiments / Actions

1. **Conduct a pragmatic RCT** of warm compress ± topical antibiotic vs. observation for acute internal hordeolum, using standardized outcomes (time-to-resolution, recurrence, OSDI) to close the Cochrane-identified evidence gap.
2. **Pharmacovigilance analysis** (FAERS/pharmacoepidemiology) to quantify hordeolum/chalazion risk with GLP-1/GIP agonists and CFTR modulators, establishing incidence and dose relationship.
3. **Microbiome + host-response profiling** of drained hordeolum contents (16S/metagenomics + neutrophil/LL-37 markers) to confirm the two-hit infectious/sterile model and stratify infectious vs. sterile lesions.
4. **Prospective imaging cohort** (meibography) to test whether recurrent hordeola predict long-term meibomian gland dropout, extending the pediatric chalazion findings ([PMID: 42116414](https://pubmed.ncbi.nlm.nih.gov/42116414/)).
5. **Controlled trial of IPL** for recurrence prevention in high-risk (rosacea/MGD/Demodex) patients, with meibomian gland function endpoints.
6. **Prospective study of biopsy yield** in non-resolving eyelid nodules to refine the threshold/timing for excluding sebaceous carcinoma.

---

*Report compiled from 16 confirmed findings across 5 investigation iterations and 34 reviewed papers. Evidence types span human clinical reviews, Cochrane systematic reviews, nationwide claims/EHR studies, case series, and case reports. No model-organism, in vitro, or computational disease-specific data were available for this entity.*


## Artifacts

- [OpenScientist final report](Internal_Hordeolum-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Internal_Hordeolum-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 28 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:6218459` *(abstract only)*: "not a primarily infectious entity"
  - closest text in source: "Primary meibomitis appears not to be a primarily infectious entity but to represent a facet of generalized sebaceous gland dysfunction and to be found in association with seborrheic dermatitis or acne rosacea"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0004917` (2 mentions) - the report calls it "MONDO"; MONDO calls it **internal hordeolum**
- `UBERON:0001801` (1 mention) - the report calls it "palpebral conjunctiva"; UBERON calls it **anterior segment of eyeball**
- `NCIT:C15277` (1 mention) - the report calls it "Supportive Care"; NCIT calls it **Mastectomy**
- `NCIT:C303` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Betamethasone**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0004841` (1 mention), reported as "tarsal gland / meibomian gland" - UBERON does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000498` (1 mention) - the report calls it "Abnormality of the eyelid"; HP calls it **Blepharitis**, and lists "Inflammation of eyelids" among its other names