---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T03:37:38.125210'
end_time: '2026-09-30T04:07:40.373028'
duration_seconds: 1802.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Staphylococcus Aureus Pneumonia
  mondo_id: MONDO:0041879
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
citation_count: 43
reference_validation:
  total_references: 43
  verified: 43
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 8
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:26608923
  relevance_assessed: 43
  on_topic: 18
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 29
  verified: 27
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 3
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0002878
    reported_labels:
    - Sign
    ontology_label: Respiratory failure
  - term_id: UBERON:0002048
    reported_labels:
    - Primary organ:** Lung
    ontology_label: lung
  - term_id: UBERON:0000977
    reported_labels:
    - Secondary/complication organs:** Pleura
    ontology_label: pleura
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0098742
    ontology_label: obsolete cell-cell adhesion via plasma-membrane adhesion molecules
    replaced_by: GO:0098609
  - term_id: GO:0051817
    ontology_label: obsolete modulation of process of other organism involved in symbiotic
      interaction
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Staphylococcus_Aureus_Pneumonia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Staphylococcus_Aureus_Pneumonia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Staphylococcus Aureus Pneumonia
- **MONDO ID:** MONDO:0041879 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Staphylococcus Aureus Pneumonia** covering all of the
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

# Staphylococcus aureus Pneumonia — Comprehensive Disease Characteristics Report

**Disease:** Staphylococcus aureus Pneumonia
**MONDO ID:** MONDO:0041879
**Category:** Infectious Disease
**Report basis:** 5-iteration autonomous literature investigation; 16 confirmed findings; 69 papers reviewed.

---

## Summary

*Staphylococcus aureus* pneumonia is a severe, frequently life-threatening bacterial lower-respiratory-tract infection caused by the Gram-positive coccus *Staphylococcus aureus* (NCBI:txid1280), spanning two dominant clinical contexts: (1) **nosocomial pneumonia** — hospital-acquired (HAP) and ventilator-associated pneumonia (VAP), where *S. aureus* is one of the top pathogens, and (2) **community-acquired necrotizing pneumonia**, an aggressive syndrome in young, previously healthy hosts driven by the Panton-Valentine leukocidin (PVL). Unlike the genetic disorders this template is often applied to, *S. aureus* pneumonia is an **infectious, non-Mendelian disease**: there are no causal human germline genes. Instead, the "genetics" of the disease reside in the **bacterial virulence gene repertoire** (*hla*, *lukS/F-PV*, *psmα*, *agr*), while host genetic contributions are limited to immunodeficiency states (e.g., STAT3/Th17 defects) that raise susceptibility.

The mechanistic core of the disease is now well defined. The pore-forming cytotoxin **alpha-hemolysin (Hla)** binds its host receptor, the zinc-dependent metalloprotease **ADAM10**, on alveolar epithelial cells, upregulating ADAM10 protease activity that cleaves the adherens-junction protein **E-cadherin**, disrupting the epithelial barrier and producing lethal acute lung injury. In parallel, the **agr quorum-sensing** system drives expression of **phenol-soluble modulins (PSMα)** and PVL, which lyse neutrophils (PSMα via MLKL-dependent necroptosis), amplifying inflammation and tissue destruction. Antecedent **influenza** infection is a critical predisposing factor: type I interferon suppresses protective **Th17/IL-17/IL-22 and IL-1β** immunity, converting mild colonization into fulminant necrotizing disease.

Clinically, the disease ranges enormously in severity. PVL-positive necrotizing community-acquired pneumonia carries 40–75% mortality with rapid deterioration, hemoptysis, leukopenia, and septic shock, whereas VAP has an attributable mortality of 3–17%. **PVL-positivity (HR 1.81) and methicillin resistance (HR 2.37) are independent predictors of mortality.** First-line therapy is **vancomycin or linezolid** for MRSA and **cefazolin or anti-staphylococcal penicillins** for MSSA, with toxin-suppressing antibiotics (linezolid, clindamycin) and anti-Hla monoclonal antibody prophylaxis (**suvratoxumab/MEDI4893**) as emerging strategies. No licensed *S. aureus* vaccine exists.

---

## Section 1 — Disease Information

**Overview.** *S. aureus* pneumonia is inflammation and consolidation of the lung parenchyma caused by infection with *S. aureus*. It presents as: community-acquired pneumonia (CAP, often necrotizing and PVL-associated), hospital-acquired pneumonia (HAP), ventilator-associated pneumonia (VAP), and post-influenza secondary bacterial pneumonia. Nosocomial *S. aureus* pneumonia is a leading cause of ICU morbidity and mortality; the 2026 review of HAP/VAP found "*Pseudomonas aeruginosa* and *Staphylococcus aureus* predominate" ([PMID: 42203422](https://pubmed.ncbi.nlm.nih.gov/42203422/)).

**Key identifiers.**
- **MONDO:** MONDO:0041879
- **MeSH:** Pneumonia, Staphylococcal (D011026)
- **ICD-10:** J15.211 (Pneumonia due to MRSA), J15.212 (Pneumonia due to MSSA); J15.2 (Pneumonia due to staphylococcus)
- **ICD-11:** infectious pneumonia codes with *S. aureus* as causative organism
- **SNOMED CT:** 53084003 (Bacterial pneumonia); staphylococcal pneumonia concept
- **OMIM/Orphanet:** Not applicable — this is an acquired infectious disease, not a Mendelian or rare genetic disorder.

**Synonyms / alternative names.** Staphylococcal pneumonia; MRSA pneumonia; MSSA pneumonia; *S. aureus* necrotizing pneumonia; PVL-associated necrotizing pneumonia; CA-MRSA pneumonia; staphylococcal lung infection.

**Information source type.** The evidence base is **aggregated disease-level** (surveillance cohorts, ICU registries, case-control studies, systematic reviews, autopsy series, and animal-model mechanistic work), supplemented by **individual patient** case reports for rare fulminant presentations.

---

## Section 2 — Etiology

**Primary cause (infectious).** The disease is caused by *Staphylococcus aureus*, including both methicillin-susceptible (MSSA) and methicillin-resistant (MRSA) strains, and both community-associated (CA-MRSA, e.g., USA300) and hospital-associated (HA-MRSA) lineages. Virulence is determined by the bacterial toxin repertoire rather than host genetics.

**Risk factors.**
- **Host/environmental:** mechanical ventilation and endotracheal intubation (VAP), ICU admission, prior hospitalization, aspiration (AOR 4.43, 95% CI 1.74–11.24 for pneumonia-pathogen presence, [PMID: 41557657](https://pubmed.ncbi.nlm.nih.gov/41557657/)), older age, immunosuppression, cancer, liver dysfunction, heart failure, long-term catheterization, and high SOFA/qSOFA scores ([PMID: 41758741](https://pubmed.ncbi.nlm.nih.gov/41758741/)). **Antecedent influenza (or influenza-like illness)** is a major predisposing factor for necrotizing CA disease. Nasal/nasopharyngeal *S. aureus* colonization is a reservoir. Occupational exposure to livestock (LA-MRSA CC398) increases carriage.
- **Genetic host susceptibility:** rare. Patients with **hyper-IgE (Job) syndrome** carrying **STAT3** mutations, "who often present with *S. aureus* infections of the lung and skin," lack Th17 immunity ([PMID: 21178015](https://pubmed.ncbi.nlm.nih.gov/21178015/)). IL-1R1 and IL-17RA deficiencies raise susceptibility in models.
- **Pathogen genetic risk factors:** carriage of *lukS-PV/lukF-PV* (PVL), high-level *hla* expression, functional *agr* locus, and *psmα* operon.

**Protective factors.**
- **Host lipoproteins:** serum LDL/ApoB sequesters the agr autoinducing peptide (AIP). "Activation of agr… is inhibited by apolipoprotein B, the structural protein of low-density lipoprotein, which binds and sequesters the secreted agr-signaling peptide (AIP)" ([PMID: 26608923](https://pubmed.ncbi.nlm.nih.gov/26608923/)); lipoprotein deficiency worsened agr-dependent pneumonia.
- **Intact Type 17 immunity** (IL-17/IL-22/IL-23) and IL-1β signaling.
- **Influenza vaccination** (reduces the antecedent viral trigger).

**Gene–environment interactions.** The dominant interaction is **virus–bacterium**: influenza-induced type I IFN suppresses host Th17/IL-1β responses ([PMID: 21178015](https://pubmed.ncbi.nlm.nih.gov/21178015/), [PMID: 24089191](https://pubmed.ncbi.nlm.nih.gov/24089191/)), permitting toxin-armed *S. aureus* to cause necrotizing disease — a bacterial-genotype × viral-environment interaction.

---

## Section 3 — Phenotypes

| Phenotype | Type | HPO suggestion | Frequency / severity | Notes |
|---|---|---|---|---|
| Fever (>39 °C) | Symptom/sign | HP:0001945 (Fever) | Common; higher temp in PVL+ (p=0.01) | [PMID: 11888586](https://pubmed.ncbi.nlm.nih.gov/11888586/) |
| Cough / dyspnea / respiratory distress | Symptom | HP:0012735, HP:0002094 | Very common | Respiratory distress 75% PVL+ |
| Hemoptysis / pulmonary hemorrhage | Sign | HP:0002105 (Hemoptysis) | PVL+ 38% vs 3% (p=0.005) | Hallmark of necrotizing disease |
| Tachycardia (>140 bpm) | Sign | HP:0001649 (Tachycardia) | PVL+ enriched (p=0.02) | |
| Leukopenia | Lab abnormality | HP:0001882 (Leukopenia) | PVL+ ~79%; predicts death (p=0.001–0.002) | Poor-prognosis marker |
| Septic shock / hypotension | Sign | HP:0031273 (Septic shock) | Frequent in fatal PVL+ cases | [PMID: 42501530](https://pubmed.ncbi.nlm.nih.gov/42501530/) |
| Pleural effusion / empyema | Physical/imaging | HP:0002202, HP:0100751 | PVL+ effusion onset (p=0.004) | Complication |
| Hypoxemic respiratory failure / ARDS | Sign | HP:0002878 | Common in severe disease | [PMID: 42454265](https://pubmed.ncbi.nlm.nih.gov/42454265/) |

**Age of onset.** Bimodal. PVL-positive necrotizing CAP strikes **young, previously healthy** patients (median age 14.8 yr vs 70.1 yr for PVL-negative, p=0.001; [PMID: 11888586](https://pubmed.ncbi.nlm.nih.gov/11888586/)); nosocomial disease predominates in older, comorbid, ventilated adults.

**Severity/progression.** Acute, rapidly progressive. In fatal PVL cases, time from onset to death was 5.5 ± 10.1 days ([PMID: 21051855](https://pubmed.ncbi.nlm.nih.gov/21051855/)); 48-hour survival was 63% (PVL+) vs 94% (PVL−) (p=0.007). Episodic/relapsing patterns are not typical; the disease is self-limited with cure or progresses to death.

**Quality of life.** Survivors of severe ICU pneumonia experience post-intensive-care morbidity (muscle wasting, cognitive impairment) common to critical illness; disease-specific QoL instruments (EQ-5D/SF-36) are not established for this entity.

---

## Section 4 — Genetic/Molecular Information

**This is an infectious disease — there are no causal HUMAN germline genes.** The molecular determinants are **bacterial virulence genes**:

| Bacterial gene | Product | Function | Evidence |
|---|---|---|---|
| *hla* | Alpha-hemolysin (Hla/α-toxin) | Pore-forming cytotoxin; binds ADAM10 | [PMID: 21926978](https://pubmed.ncbi.nlm.nih.gov/21926978/), [PMID: 38990361](https://pubmed.ncbi.nlm.nih.gov/38990361/) |
| *lukS-PV / lukF-PV* | Panton-Valentine leukocidin (PVL) | Bicomponent leukocidin; lyses neutrophils | [PMID: 11888586](https://pubmed.ncbi.nlm.nih.gov/11888586/) |
| *psmα1-4* | Phenol-soluble modulins α | Leukocyte-lysis toxins; neutrophil necroptosis | [PMID: 29500427](https://pubmed.ncbi.nlm.nih.gov/29500427/) |
| *agr* (RNAIII) | Accessory gene regulator | Quorum-sensing master virulence regulator | [PMID: 29500427](https://pubmed.ncbi.nlm.nih.gov/29500427/) |
| *seb, sec, tst* | Superantigens SEB, SEC, TSST-1 | T-cell superantigens driving toxic shock | [PMID: 42161902](https://pubmed.ncbi.nlm.nih.gov/42161902/) |
| *mecA* (SCC*mec*) | PBP2a | Methicillin resistance | [PMID: 23524477](https://pubmed.ncbi.nlm.nih.gov/23524477/) |

**Host genetic modifiers of susceptibility.** *STAT3* (hyper-IgE syndrome; loss of Th17), *IL17RA*, *IL1R1* — loss-of-function increases susceptibility (human + mouse). HGNC: STAT3, IL17RA, IL1R1, ADAM10. **ADAM10** is the host receptor whose activity is subverted (not mutated).

**Variant classification / allele frequency / somatic-germline.** Not applicable in the ACMG/ClinVar sense — the disease is not inherited. "Variants" of clinical importance are **bacterial genotypes** (PVL+/−, MRSA/MSSA, clonal complexes CC398, CC5, CC8/USA300, CC30, ST80).

**Epigenetics / chromosomal abnormalities.** Not applicable to the human host. Bacterial global regulation is via *agr* quorum-sensing and *sae/sar* regulons.

---

## Section 5 — Environmental Information

- **Environmental factors:** hospital/ICU environment, endotracheal tubes (biofilm reservoir — MRSA biofilm forms on ETTs, [PMID: 30093624](https://pubmed.ncbi.nlm.nih.gov/30093624/)), contaminated surfaces, livestock/meat exposure.
- **Lifestyle factors:** injection drug use (associated with MSSA bacteremia/endocarditis), smoking (airway epithelial injury), crowding, and occupational livestock contact.
- **Infectious agents (the cause itself):** *Staphylococcus aureus* (NCBI:txid1280). **Co-infecting agents that potentiate disease:** Influenza A virus (H1N1) and Influenza B virus — the key viral co-pathogens converting *S. aureus* colonization into necrotizing/secondary pneumonia ([PMID: 21178015](https://pubmed.ncbi.nlm.nih.gov/21178015/), [PMID: 41619830](https://pubmed.ncbi.nlm.nih.gov/41619830/)).

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. *S. aureus* colonizes the nasopharynx/airway and is aspirated or inhaled into the lower respiratory tract → **leads to** alveolar bacterial burden. (Antecedent influenza injures respiratory epithelium and suppresses immunity — *inferred prerequisite* in young necrotizing cases.)
2. Rising bacterial density activates the **agr quorum-sensing** system (RNAIII) → **results in** upregulated secretion of Hla, PSMα, and PVL. (Demonstrated; agr blockade is protective.)
3. Secreted **Hla binds ADAM10** on alveolar epithelial cells → **upregulates ADAM10 metalloprotease activity** → **cleaves E-cadherin** → **disrupts adherens junctions and the epithelial barrier** → alveolar–capillary leak and lethal acute lung injury. (Demonstrated genetically: Adam10-conditional-knockout mice are resistant, [PMID: 21926978](https://pubmed.ncbi.nlm.nih.gov/21926978/).)
4. **Branch A — Neutrophil destruction:** PSMα1–3 induce **neutrophil necroptosis via MLKL phosphorylation** and PVL forms pores in leukocytes → **results in** leukopenia, release of DAMPs/LDH, and impaired bacterial clearance. (Demonstrated, [PMID: 29500427](https://pubmed.ncbi.nlm.nih.gov/29500427/).)
5. **Branch B — Immune subversion by prior virus:** Influenza type I IFN **suppresses IL-17/IL-22/IL-23 and attenuates IL-1β/NF-κB** → **impairs Type 17 antibacterial immunity** → higher bacterial burden and mortality. (Demonstrated in IL-17R⁻/⁻, IL-22⁻/⁻, IL-1R1⁻/⁻ mice, [PMID: 21178015](https://pubmed.ncbi.nlm.nih.gov/21178015/), [PMID: 24089191](https://pubmed.ncbi.nlm.nih.gov/24089191/).)
6. **Branch C — Inflammasome/pyroptosis amplification:** In influenza–MRSA co-infection, caspase-1 and **GSDMD-mediated macrophage pyroptosis** are activated, and dysregulated type I IFN enhances myeloid TNF-α while suppressing T-cell IFN-γ → **amplifies lung injury**. (Demonstrated; GSDMD inhibitor disulfiram ameliorated disease, [PMID: 41927528](https://pubmed.ncbi.nlm.nih.gov/41927528/), [PMID: 42089309](https://pubmed.ncbi.nlm.nih.gov/42089309/).)
7. Combined barrier failure + neutrophil lysis + cytokine storm → **necrotizing hemorrhagic bronchopneumonia**, hemoptysis, ARDS, septic shock → **culminates in** multi-organ failure and death in severe cases.

### Pathway / process / cell-type detail

- **Molecular pathways:** agr quorum-sensing (RNAIII); ADAM10 sheddase pathway; NF-κB/IL-1β signaling; type I IFN (IFNAR1) signaling; IL-23→IL-17/IL-22 (Type 17) axis; MLKL necroptosis; caspase-1/GSDMD pyroptosis (inflammasome).
- **Cellular processes (GO):** GO:0006909 phagocytosis; GO:0070266 necroptotic process; GO:0070269 pyroptosis; GO:0006954 inflammatory response; GO:0098742 cell-cell adhesion via plasma-membrane adhesion molecules (E-cadherin cleavage); GO:0051817 modulation of host process by symbiont.
- **Protein dysfunction:** host **E-cadherin** proteolytic loss of function; **ADAM10** gain of pathological activity (usurped by Hla); pore formation in host membranes by Hla/PVL/PSM.
- **Immune involvement:** neutrophil-centric defense that is turned against the host (neutrophil necroptosis); Th17 deficiency; macrophage pyroptosis; superantigen-driven T-cell activation (SEB/SEC/TSST-1).
- **Tissue damage mechanisms:** membrane pore-formation/osmotic lysis, hemorrhagic necrosis, oxidative/inflammatory injury, barrier breakdown, edema.
- **Cell types (CL):** CL:0000775 neutrophil; CL:0000583 alveolar macrophage; CL:0002063 type II pneumocyte / CL:0002062 type I pneumocyte; CL:0000066 epithelial cell; CL:0000738 leukocyte.

---

## Section 7 — Anatomical Structures Affected

- **Primary organ:** Lung (UBERON:0002048); lung parenchyma / alveoli (UBERON:0002299 alveolus).
- **Body system:** Respiratory system (UBERON:0001004).
- **Secondary/complication organs:** Pleura (UBERON:0000977) — parapneumonic effusion/empyema; bloodstream — bacteremia; distant sites via metastatic infection; kidney/heart in multi-organ failure and endocarditis.
- **Tissues:** Alveolar epithelium (type I & II pneumocytes), bronchial epithelium, pulmonary capillary endothelium, connective tissue of interstitium.
- **Cells targeted:** alveolar epithelial cells (Hla/ADAM10/E-cadherin), neutrophils (PVL/PSMα), macrophages (GSDMD pyroptosis).
- **Subcellular compartments (GO CC):** plasma membrane (GO:0005886, pore formation); adherens junction (GO:0005912); extracellular space (secreted toxins); cytosol (inflammasome assembly).
- **Localization/lateralization:** Frequently **bilateral** in necrotizing disease ("bilateral necrotizing hemorrhagic bronchopneumonia," [PMID: 42501530](https://pubmed.ncbi.nlm.nih.gov/42501530/)); multilobar involvement common in CA-MRSA ([PMID: 21722847](https://pubmed.ncbi.nlm.nih.gov/21722847/)).

---

## Section 8 — Temporal Development

- **Onset:** Acute to hyperacute. PVL-associated necrotizing CAP often follows an influenza-like prodrome by 1–several days, then deteriorates rapidly.
- **Progression:** Rapid. Fatal PVL cases: onset-to-death 5.5 ± 10.1 days; 48-h survival markedly reduced in PVL+ (63% vs 94%). VAP: median time to ventilator-associated condition onset ~6 days ([PMID: 24709718](https://pubmed.ncbi.nlm.nih.gov/24709718/)).
- **Disease course pattern:** Acute, progressive, self-limited (resolution with effective therapy) or fatal; not relapsing-remitting.
- **Critical periods / intervention windows:** Early source control, prompt appropriate antibiotics, and toxin suppression within the first 24–72 h are decisive; anti-Hla prophylaxis targets the ventilated pre-symptomatic window.

---

## Section 9 — Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable. No Mendelian pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier-frequency parameters apply to the host.

**Epidemiology.**
- *S. aureus* is among the **top pathogens of nosocomial pneumonia** ([PMID: 42203422](https://pubmed.ncbi.nlm.nih.gov/42203422/)); in Chinese HAP cohorts it was the 4th-ranked pathogen at 5.88% ([PMID: 41758741](https://pubmed.ncbi.nlm.nih.gov/41758741/)).
- **VAP incidence:** 2–16 episodes/1000 ventilator-days; attributable mortality 3–17%; *S. aureus* is a leading VAP pathogen with 50–80% MRSA in some series ([PMID: 23524477](https://pubmed.ncbi.nlm.nih.gov/23524477/)).
- In a CDC ventilator-associated-event cohort, *S. aureus* was **the most frequently isolated organism (29%)** ([PMID: 24709718](https://pubmed.ncbi.nlm.nih.gov/24709718/)).

**Population demographics.**
- **Age/sex:** PVL-necrotizing disease — young, previously healthy, often male; nosocomial disease — older comorbid ICU patients.
- **Geography/variants:** PVL prevalence among MRSA varies 0–62% across regions (GCC scoping review, [PMID: 42799093](https://pubmed.ncbi.nlm.nih.gov/42799093/)); CA-MRSA clones vary by region (USA300 in North America; ST80-IV, ST30, ST22 elsewhere). LA-MRSA CC398 clusters in high-livestock-density areas (18.6–23% of human MRSA in one German region, [PMID: 23418434](https://pubmed.ncbi.nlm.nih.gov/23418434/)).

---

## Section 10 — Diagnostics

**Clinical/lab tests.**
- **Lower-respiratory culture** (definitive): endotracheal aspirate vs bronchoalveolar lavage (BAL). BAL-directed diagnostic protocols lowered VAP-attributable mortality to ~1% ([PMID: 22310133](https://pubmed.ncbi.nlm.nih.gov/22310133/)).
- **Blood cultures** for bacteremia; **pleural fluid** analysis for empyema.
- **Molecular:** metagenomic next-generation sequencing (mNGS) identifies co-infections (e.g., PVL+ MSSA + influenza B) when conventional tests fail ([PMID: 41619830](https://pubmed.ncbi.nlm.nih.gov/41619830/)); PCR for *mecA*, *lukS/F-PV*.
- **CBC:** leukopenia is an ominous prognostic sign.

**Stewardship diagnostic — MRSA nasal PCR.** Nasal-swab PCR has excellent negative predictive value: "The MRSA PCR assay demonstrated 88.0% sensitivity and 90.1% specificity, with a positive predictive value of 35.4% and a negative predictive value of 99.2%" ([PMID: 24277023](https://pubmed.ncbi.nlm.nih.gov/24277023/)). A negative swab safely de-escalates empiric vancomycin ([PMID: 38028911](https://pubmed.ncbi.nlm.nih.gov/38028911/)); use caution after intranasal mupirocin decolonization ([PMID: 32959059](https://pubmed.ncbi.nlm.nih.gov/32959059/)).

**Imaging.** Chest X-ray/CT: multilobar consolidation, cavitation/necrosis, effusion, pneumatoceles, abscess.

**Genetic/omics diagnostics for the host:** Not applicable. (Host WGS/WES/panels/karyotype/CMA have no role.) Pathogen genomics (WGS, spa-typing, MLST) is used for surveillance/typing.

**Clinical criteria & differential.** IDSA/ATS HAP/VAP and CAP guidelines. Differential: pneumococcal, *Pseudomonas*, *Klebsiella*, *Acinetobacter*, and viral pneumonias; distinguishing features of *S. aureus* necrotizing disease include rapid cavitation, hemoptysis, leukopenia, and antecedent influenza.

---

## Section 11 — Outcome / Prognosis

| Setting | Mortality | Source |
|---|---|---|
| PVL+ necrotizing CAP (older patients) | ~47% | [PMID: 33833037](https://pubmed.ncbi.nlm.nih.gov/33833037/) |
| PVL+ necrotizing CAP (toddlers) | ~15% | [PMID: 33833037](https://pubmed.ncbi.nlm.nih.gov/33833037/) |
| Necrotizing staph CAP (92-case review) | 42.9% | [PMID: 21051855](https://pubmed.ncbi.nlm.nih.gov/21051855/) |
| VAP (attributable) | 3–17% | [PMID: 23524477](https://pubmed.ncbi.nlm.nih.gov/23524477/) |

**Independent mortality predictors:** "Mortality in older patients was predicted by PVL-positivity (hazard ratio (HR) 1.81, 95% CI 1.03–3.17) and methicillin resistance (HR 2.37, 95% CI 1.29–4.34)" ([PMID: 33833037](https://pubmed.ncbi.nlm.nih.gov/33833037/)). Additional poor-prognosis markers: leukopenia (p=0.002), influenza (p=0.011), hemoptysis (p=0.024) ([PMID: 21051855](https://pubmed.ncbi.nlm.nih.gov/21051855/)).

**Complications:** parapneumonic effusion, empyema, necrotizing pneumonia, lung abscess (local); bacteremia, metastatic infection, multi-organ failure, ARDS, DIC, death (systemic) ([PMID: 32919518](https://pubmed.ncbi.nlm.nih.gov/32919518/)). Toxin-suppressing antibiotics improve outcome (p=0.007, [PMID: 21051855](https://pubmed.ncbi.nlm.nih.gov/21051855/)).

**Recovery:** Survivors may recover fully but face post-ICU morbidity. Disease is self-limited with cure or rapidly fatal without effective therapy.

---

## Section 12 — Treatment

**Pharmacotherapy (first-line).**
- **MRSA pneumonia:** vancomycin OR linezolid — "Both linezolid and vancomycin are approved by USFDA and IDSA guidelines for the management of nosocomial pneumonia due to methicillin-resistant Staphylococcus aureus (MRSA)" ([PMID: 36852899](https://pubmed.ncbi.nlm.nih.gov/36852899/)). Linezolid shows higher clinical cure (53–59%) and less nephrotoxicity than vancomycin (43–47%) in HAP/VAP ([PMID: 38238670](https://pubmed.ncbi.nlm.nih.gov/38238670/), [PMID: 36852899](https://pubmed.ncbi.nlm.nih.gov/36852899/)); vancomycin penetrates alveolar fluid poorly ([PMID: 21722847](https://pubmed.ncbi.nlm.nih.gov/21722847/)). NCIT: Vancomycin (C935), Linezolid (C1697).
- **MSSA pneumonia/bacteremia:** cefazolin or anti-staphylococcal penicillins (nafcillin/oxacillin) — "cefazolin or antistaphylococcal penicillins should be the first-line treatment for methicillin-susceptible Staphylococcus aureus (MSSA) bacteraemia," with cefazolin causing less nephrotoxicity ([PMID: 40349971](https://pubmed.ncbi.nlm.nih.gov/40349971/)). NCIT: Cefazolin (C341), Nafcillin, Oxacillin.
- **Toxin suppression:** linezolid and clindamycin inhibit toxin synthesis; toxin-inhibiting regimens improved outcomes in necrotizing CAP ([PMID: 21051855](https://pubmed.ncbi.nlm.nih.gov/21051855/), [PMID: 21722847](https://pubmed.ncbi.nlm.nih.gov/21722847/)).
- **Alternatives/resistant strains:** daptomycin (bloodstream, not lung — inactivated by surfactant), telavancin; MDRO guidance recommends linezolid or vancomycin for MRSA pneumonia ([PMID: 42661422](https://pubmed.ncbi.nlm.nih.gov/42661422/)).

**Advanced/experimental therapeutics.**
- **Anti-alpha-toxin monoclonal antibody — suvratoxumab (MEDI4893):** SAATELLITE phase 2 RCT evaluated its efficacy "in reducing the incidence of S aureus pneumonia in patients in the intensive care unit (ICU) who are on mechanical ventilation" ([PMID: 33894131](https://pubmed.ncbi.nlm.nih.gov/33894131/)).
- **Anti-Hla scFvs / multivalent nanobodies:** increased survival comparable to vancomycin in murine MRSA pneumonia ([PMID: 42133074](https://pubmed.ncbi.nlm.nih.gov/42133074/), [PMID: 42161902](https://pubmed.ncbi.nlm.nih.gov/42161902/)); AAV-delivered anti-α-toxin mAbs protect in models ([PMID: 41941484](https://pubmed.ncbi.nlm.nih.gov/41941484/)).
- **Anti-virulence small molecules:** agrA inhibitor norwogonin ([PMID: 38990361](https://pubmed.ncbi.nlm.nih.gov/38990361/)); ClpP inhibitor sesamin ([PMID: 39805732](https://pubmed.ncbi.nlm.nih.gov/39805732/)); Hla inhibitors (Jingfang mixture, [PMID: 39083107](https://pubmed.ncbi.nlm.nih.gov/39083107/)).
- **Host-directed:** GSDMD inhibitor disulfiram ameliorated co-infection pneumonia ([PMID: 41927528](https://pubmed.ncbi.nlm.nih.gov/41927528/)); innate immune priming with DDM ([PMID: 41619354](https://pubmed.ncbi.nlm.nih.gov/41619354/)).

**Surgical/interventional & supportive.** Pleural drainage/chest tube for empyema; source control; prone positioning and lung-protective ventilation for ARDS; ECMO in refractory cases (though selected fulminant MSSA managed without ECMO, [PMID: 42454265](https://pubmed.ncbi.nlm.nih.gov/42454265/)).

**Pharmacogenomics.** Not a major factor; vancomycin dosing is guided by renal function/therapeutic drug monitoring rather than host genotype.

---

## Section 13 — Prevention

- **Primary prevention:** VAP bundles (head-of-bed elevation, oral care, sedation minimization, subglottic suctioning), hand hygiene, aspiration precautions, and antimicrobial stewardship; **influenza vaccination** to remove the key viral trigger.
- **Secondary prevention:** MRSA nasal PCR screening for stewardship/de-escalation; active surveillance; MRSA decolonization (intranasal mupirocin) in high-risk/ICU settings.
- **Immunization:** **No licensed *S. aureus* vaccine exists** — "Despite decades of effort, vaccine development has been unsuccessful, highlighting the need for alternative approaches" ([PMID: 41941484](https://pubmed.ncbi.nlm.nih.gov/41941484/)). Toxoid/nanotoxoid and multi-antigen vaccines protect mice ([PMID: 37097076](https://pubmed.ncbi.nlm.nih.gov/37097076/), [PMID: 32197534](https://pubmed.ncbi.nlm.nih.gov/32197534/)) but none are approved.
- **Prophylaxis:** anti-Hla mAb (suvratoxumab) for ventilated, colonized ICU patients ([PMID: 33894131](https://pubmed.ncbi.nlm.nih.gov/33894131/)).
- **Public health / One Health:** livestock-associated MRSA CC398 surveillance and occupational infection control ([PMID: 23418434](https://pubmed.ncbi.nlm.nih.gov/23418434/)).

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy:** *Staphylococcus aureus* — NCBI:txid1280. Host species: human (NCBI:txid9606); reservoir/affected animals: pig (*Sus scrofa*, txid9823), cattle (*Bos taurus*, txid9913), poultry (chicken, txid9031).
- **Natural disease / veterinary relevance:** *S. aureus* causes bovine mastitis and infections across livestock; "Pigs, cattle and poultry are colonized with MRSA and the zoonotic transmission of such MRSA to humans via direct animal contact, environmental contaminations or meat are a matter of concern. Livestock-associated (LA) MRSA are mostly belonging to clonal complex (CC) 398" ([PMID: 23418434](https://pubmed.ncbi.nlm.nih.gov/23418434/)). Other livestock lineages: CC5, CC9, CC97.
- **Zoonotic transmission:** direct animal contact, environmental contamination, and meat.
- **Comparative biology:** Hla/PVL toxin mechanisms are studied primarily in murine lungs; ADAM10 is conserved across mammals, supporting cross-species mechanistic relevance.

---

## Section 15 — Model Organisms

- **Standard model:** murine **intranasal/intratracheal** *S. aureus* pneumonia, especially CA-MRSA **USA300** — the workhorse for pathogenesis and therapeutics ([PMID: 42161902](https://pubmed.ncbi.nlm.nih.gov/42161902/)). Disease is "driven by potent virulence factors such as T-cell superantigens and alpha hemolysin," including SEB, SEC, and TSST-1.
- **Genetic models:** **Adam10 lung-epithelium conditional knockout** (resistant to lethal Hla pneumonia — landmark genetic proof, [PMID: 21926978](https://pubmed.ncbi.nlm.nih.gov/21926978/)); **IL-17R⁻/⁻, IL-22⁻/⁻, IL-1R1⁻/⁻** mice (impaired clearance, [PMID: 21178015](https://pubmed.ncbi.nlm.nih.gov/21178015/), [PMID: 24089191](https://pubmed.ncbi.nlm.nih.gov/24089191/)); myeloid IFNAR1-deletion (improved survival, [PMID: 42089309](https://pubmed.ncbi.nlm.nih.gov/42089309/)).
- **Co-infection models:** influenza A (PR8/H1N1) + MRSA sequential-infection mice ([PMID: 41927528](https://pubmed.ncbi.nlm.nih.gov/41927528/)).
- **Large-animal:** **porcine** MRSA pneumonia models (ETT biofilm, telavancin/linezolid efficacy) ([PMID: 30093624](https://pubmed.ncbi.nlm.nih.gov/30093624/), [PMID: 33046500](https://pubmed.ncbi.nlm.nih.gov/33046500/)).
- **In vitro:** A549 alveolar epithelial cells, RAW264.7 macrophages, primary human neutrophils.
- **Phenotype recapitulation:** murine models reproduce necrotizing pneumonia, toxin-mediated barrier injury, and neutrophil lysis well; **limitations** include species differences in PVL susceptibility (human neutrophils are far more PVL-sensitive than murine), immune-response divergence, and difficulty modeling the human influenza-priming context.

---

## Mechanistic Model / Interpretation

```
 S. aureus in lower airway (± prior influenza injuring epithelium & immunity)
                     │ high density
                     ▼
            agr quorum-sensing (RNAIII)  ── inhibited by host ApoB/LDL (protective)
             │            │             │
             ▼            ▼             ▼
           Hla          PSMα           PVL
             │            │             │
   binds ADAM10      MLKL-driven    pore-forms
   on pneumocyte   neutrophil       in neutrophils
             │      necroptosis          │
   ↑ADAM10 protease    │                 │
             │         └──────┬──────────┘
   cleaves E-cadherin        ▼
             │        Neutrophil loss → LEUKOPENIA, DAMPs
   ADHERENS-JUNCTION /        │
   BARRIER FAILURE            │
             │                │
             └──────┬─────────┘
                    ▼
   [Influenza type I IFN → ↓IL-17/IL-22/IL-23, ↓IL-1β/NF-κB → impaired Type 17 defense]
   [Co-infection → caspase-1/GSDMD macrophage pyroptosis → amplified injury]
                    ▼
   NECROTIZING HEMORRHAGIC BRONCHOPNEUMONIA
   → hemoptysis, ARDS, septic shock → multi-organ failure / death
```

**Upstream vs downstream:** agr activation and Hla–ADAM10 engagement are the **upstream** initiating molecular events; E-cadherin cleavage, neutrophil necroptosis, and immune subversion are **midstream**; hemorrhagic necrosis, ARDS, and shock are **downstream** clinical endpoints. The convergence of *epithelial barrier failure* (Hla/ADAM10) and *innate-effector destruction* (PVL/PSMα) plus *impaired adaptive/innate immunity* (post-influenza) explains why *S. aureus* pneumonia can be so rapidly lethal.

---

## Evidence Base (key papers)

| PMID | Contribution |
|---|---|
| [21926978](https://pubmed.ncbi.nlm.nih.gov/21926978/) | **Landmark**: Hla→ADAM10→E-cadherin barrier mechanism; Adam10-cKO mice resistant |
| [29500427](https://pubmed.ncbi.nlm.nih.gov/29500427/) | agr→PSMα→MLKL neutrophil necroptosis; agr blockade protective |
| [26608923](https://pubmed.ncbi.nlm.nih.gov/26608923/) | Host ApoB/LDL sequesters agr AIP — protective factor |
| [21178015](https://pubmed.ncbi.nlm.nih.gov/21178015/) | Influenza type I IFN suppresses Th17; STAT3/hyper-IgE human link |
| [24089191](https://pubmed.ncbi.nlm.nih.gov/24089191/) | Influenza attenuates IL-1β/NF-κB → impaired Type 17 defense |
| [41927528](https://pubmed.ncbi.nlm.nih.gov/41927528/) | GSDMD pyroptosis in flu-MRSA co-infection; disulfiram rescue |
| [42089309](https://pubmed.ncbi.nlm.nih.gov/42089309/) | Temporal type I IFN: pathogenic myeloid TNF-α, suppressed IFN-γ |
| [11888586](https://pubmed.ncbi.nlm.nih.gov/11888586/) | Case-control defining PVL+ necrotizing pneumonia phenotype |
| [21051855](https://pubmed.ncbi.nlm.nih.gov/21051855/) | 92-case review; mortality predictors; toxin-suppression benefit |
| [33833037](https://pubmed.ncbi.nlm.nih.gov/33833037/) | PVL (HR 1.81) & MRSA (HR 2.37) independent mortality predictors |
| [42501530](https://pubmed.ncbi.nlm.nih.gov/42501530/) | Autopsy + review: fatal PVL necrotizing pneumonia |
| [23524477](https://pubmed.ncbi.nlm.nih.gov/23524477/) | VAP epidemiology; incidence & attributable mortality |
| [24709718](https://pubmed.ncbi.nlm.nih.gov/24709718/) | *S. aureus* most frequent (29%) organism in VAEs |
| [24277023](https://pubmed.ncbi.nlm.nih.gov/24277023/) | MRSA nasal PCR NPV 99.2% — de-escalation tool |
| [36852899](https://pubmed.ncbi.nlm.nih.gov/36852899/) | Vancomycin & linezolid guideline first-line for MRSA pneumonia |
| [40349971](https://pubmed.ncbi.nlm.nih.gov/40349971/) | Cefazolin/ASP first-line for MSSA |
| [33894131](https://pubmed.ncbi.nlm.nih.gov/33894131/) | Suvratoxumab anti-Hla mAb prevention (SAATELLITE) |
| [21722847](https://pubmed.ncbi.nlm.nih.gov/21722847/) | CA-MRSA pneumonia clinical features & therapy |
| [32919518](https://pubmed.ncbi.nlm.nih.gov/32919518/) | Complications of complicated pneumonia |
| [23418434](https://pubmed.ncbi.nlm.nih.gov/23418434/) | LA-MRSA CC398 zoonosis |
| [42161902](https://pubmed.ncbi.nlm.nih.gov/42161902/) | Superantigens + Hla drivers; murine models; nanobodies |

---

## Limitations and Knowledge Gaps

1. **Template mismatch.** This template is designed for genetic/rare diseases; sections on causal human genes, ACMG variant classification, inheritance, penetrance, carrier frequency, and host genetic testing are **not applicable**. The "molecular genetics" of this disease is bacterial.
2. **Human vs model evidence.** Much mechanistic detail (Hla/ADAM10, PSMα necroptosis, GSDMD pyroptosis) is from mouse/in-vitro work; human PVL biology differs (human neutrophils far more PVL-sensitive), complicating translation.
3. **PVL causal debate.** PVL is a strong clinical marker of severe necrotizing disease, but its precise causal weight vs Hla/PSMα in humans remains debated; PVL-negative necrotizing MSSA also occurs ([PMID: 41585354](https://pubmed.ncbi.nlm.nih.gov/41585354/)).
4. **Epidemiologic heterogeneity.** Prevalence/mortality vary widely by region, clone, and care setting; a precise incidence per 100,000 for "*S. aureus* pneumonia" specifically is not cleanly defined in the literature reviewed.
5. **No approved vaccine or anti-toxin therapy is yet standard of care**, despite promising models and phase-2 trials.
6. **No primary experimental dataset** was analyzed here; conclusions are literature-derived.

---

## Proposed Follow-up Experiments / Actions

1. **Human validation of anti-Hla prophylaxis:** analyze SAATELLITE and successor phase-3 outcomes stratified by baseline PVL/agr genotype and influenza co-infection status.
2. **Prospective PVL/agr-typed cohort:** quantify independent contributions of Hla vs PVL vs PSMα to human mortality, adjusting for MRSA status and influenza.
3. **Host-directed therapy trials:** test GSDMD inhibition (disulfiram) and Type 17 augmentation (IL-23/IL-17 axis) as adjuncts in severe/co-infection pneumonia.
4. **Biomarker development:** validate leukopenia, hemoptysis, and circulating toxin/ADAM10-cleaved E-cadherin fragments as early prognostic markers.
5. **Diagnostic stewardship rollout:** broaden MRSA nasal-PCR-guided de-escalation and mNGS for co-infection detection in refractory pneumonia.
6. **One-Health surveillance:** monitor LA-MRSA CC398 spillover and PVL acquisition by hospital lineages.
7. **Vaccine antigen strategy:** pursue multi-antigen/toxoid formulations (Hla + PVL + PSM + superantigens) given single-antigen failures.

---

*Report compiled from 16 confirmed findings and 69 reviewed papers over 5 investigation iterations. Evidence types are labeled inline as human clinical (cohorts/case-control/RCT), model organism (murine/porcine), or in vitro where relevant.*


## Artifacts

- [OpenScientist final report](Staphylococcus_Aureus_Pneumonia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Staphylococcus_Aureus_Pneumonia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 43 |
| On topic | 18 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26608923` *(abstract only)*: "Activation of agr… is inhibited by apolipoprotein B, the structural protein of low-density lipoprotein, which binds and sequesters the secreted agr-signaling peptide (AIP)"
  - closest text in source: "Activation of agr and subsequent virulence factor expression is inhibited by apolipoprotein B, the structural protein of low-density lipoprotein, which binds and sequesters the secreted agr-signaling peptide (AIP)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 9 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002878` (1 mention) - the report calls it "Sign"; HP calls it **Respiratory failure**
- `UBERON:0002048` (1 mention) - the report calls it "Primary organ:** Lung"; UBERON calls it **lung**
- `UBERON:0000977` (1 mention) - the report calls it "Secondary/complication organs:** Pleura"; UBERON calls it **pleura**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0098742` (obsolete cell-cell adhesion via plasma-membrane adhesion molecules) (1 mention) - replaced by `GO:0098609`
- `GO:0051817` (obsolete modulation of process of other organism involved in symbiotic interaction) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `HP:0031273` (1 mention) - the report calls it "Septic shock"; HP calls it **Shock**
- `UBERON:0001004` (1 mention) - the report calls it "Body system:** Respiratory system"; UBERON calls it **respiratory system**