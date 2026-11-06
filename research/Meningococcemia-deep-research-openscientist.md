---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-30T03:37:38.787191'
end_time: '2026-09-30T04:08:40.615998'
duration_seconds: 1861.83
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Meningococcemia
  mondo_id: MONDO:0042972
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
citation_count: 47
reference_validation:
  total_references: 48
  verified: 48
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 48
  on_topic: 19
  validator_version: 0.5.1
term_validation:
  total_terms: 38
  verified: 37
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 11
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0042972
    reported_labels:
    - if available
    - meningococcemia
    ontology_label: meningococcemia
  - term_id: HP:0031057
    reported_labels:
    - limb pain
    ontology_label: Skin fissure
  labels_variant: 8
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Meningococcemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Meningococcemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Meningococcemia
- **MONDO ID:** MONDO:0042972 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Meningococcemia** covering all of the
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

# Meningococcemia (MONDO:0042972): A Comprehensive Disease Characteristics Report

*Category: Infectious Disease | Causative agent: Neisseria meningitidis (NCBI:txid487)*
*Evidence base: Aggregated disease-level literature (reviews, cohort studies, surveillance, mechanistic in vitro / humanized-mouse studies). No patient-level EHR data were used.*

---

## Summary

**Meningococcemia is an acute, frequently fulminant bloodstream infection caused by the human-restricted Gram-negative diplococcus *Neisseria meningitidis*.** It is one of the two principal clinical forms of invasive meningococcal disease (IMD), the other being meningococcal meningitis; the two frequently coexist. Meningococcemia is distinguished by rapid progression from a nonspecific febrile prodrome to septic shock, disseminated intravascular coagulation (DIC), purpura fulminans, bilateral adrenal hemorrhage (Waterhouse-Friderichsen syndrome), and multi-organ failure, often within 24 hours of first symptoms.

The pathophysiology is now understood at molecular resolution. Circulating meningococci adhere to microvascular endothelium via **type IV pili**, triggering **ADAM10-dependent shedding of the Endothelial Protein C Receptor (EPCR)**, which cripples the anticoagulant Protein C pathway and produces the localized microvascular thrombosis characteristic of purpura fulminans. In parallel, the bacterium's **lipooligosaccharide/lipopolysaccharide (LPS/endotoxin)** drives a TLR4-mediated cytokine storm (IL-10, TNF, MIF) whose magnitude scales with bacterial load and predicts mortality. Host susceptibility is dominated by **complement function**: inherited deficiencies of the terminal pathway (C5–C9), properdin (CFP, X-linked), and factor D (CFD) markedly increase risk, and this phenotype is now iatrogenically reproduced by the anti-C5 monoclonal antibodies eculizumab and ravulizumab.

Despite prompt third-generation cephalosporin therapy, meningococcemia carries a case-fatality rate of roughly **8–17%**, rising above 20% in the fulminant hemodynamic form, and leaves approximately **10–20% of survivors** with permanent sequelae (limb amputation, hearing loss, skin scarring, renal dysfunction, neurologic deficits). The disease is preventable: conjugate vaccines (MenAfriVac, quadrivalent ACWY, pentavalent ACWYX) and the protein-based 4CMenB vaccine have transformed epidemiology, and rapid contact chemoprophylaxis with ciprofloxacin or rifampicin interrupts secondary transmission. This report synthesizes 14 confirmed findings drawn from 57 reviewed papers across all 15 requested disease-characteristic domains.

---

## Section 1 — Disease Information

**Overview.** Meningococcemia (meningococcal septicemia) is the bloodstream-infection presentation of invasive meningococcal disease caused by *Neisseria meningitidis*, an encapsulated Gram-negative diplococcus that is an obligate human commensal of the nasopharynx. Invasion from the mucosal reservoir into the blood is rare relative to carriage, but when it occurs it can produce fulminant sepsis. IMD classically presents in two overlapping clinical forms — a **neurological/meningitic form** and a **hemodynamic/septicemic form (meningococcemia)** — with a nationwide French adult ICU cohort (RETRO-MENINGO, 654 patients) finding 62% neurological and 38% hemodynamic presentations ([PMID: 40794167](https://pubmed.ncbi.nlm.nih.gov/40794167/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Mondo | MONDO:0042972 (meningococcemia) |
| MeSH | Meningococcal Infections; *Neisseria meningitidis* |
| ICD-10 | A39.2 (acute meningococcemia); A39.4 (meningococcemia, unspecified); A39.1 (Waterhouse-Friderichsen syndrome) |
| ICD-11 | 1D01 (meningococcal infection / invasive meningococcal disease) |
| NCBI Taxonomy | *Neisseria meningitidis* txid487 |

**Synonyms/alternative names.** Meningococcal septicemia; meningococcal sepsis; meningococcal bacteremia; invasive meningococcal disease (septicemic form); systemic meningococcal disease. *Purpura fulminans* and *Waterhouse-Friderichsen syndrome* denote severe complications rather than synonyms.

**Nature of the evidence.** Meningococcemia is characterized primarily through **aggregated disease-level resources** — national surveillance systems, prospective cohorts, autopsy series, and reference-laboratory serogroup/genotype data — supplemented by individual case reports for rare complications. It is not a Mendelian/EHR-genotype disease; host-genetic contribution is confined to susceptibility modifiers (below).

---

## Section 2 — Etiology

**Primary cause (infectious).** The sole causal agent is *Neisseria meningitidis*. Twelve serogroups are defined by capsular polysaccharide; six (A, B, C, W, X, Y) cause nearly all invasive disease. Disease results from the interaction of exposure to a virulent strain with absence of host resistance ([PMID: 11057965](https://pubmed.ncbi.nlm.nih.gov/11057965/)).

**Genetic host risk factors.** Inherited deficiencies of the **terminal complement components (C5, C6, C7, C8, C9)**, **properdin (CFP; X-linked)**, and **factor D (CFD)** of the alternative pathway strongly predispose to invasive meningococcal disease, often with recurrent episodes and atypical serogroups (Y, W-135) (F001). *"Individuals, deficient of properdin or of the terminal pathway components (C5 to C9), are highly susceptible to meningococcal disease"* ([PMID: 25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/)). Factor D deficiency *"abolishes alternative-pathway dependent complement activation by N meningitidis, and leads to an increased susceptibility to invasive meningococcal disease"* ([PMID: 16527897](https://pubmed.ncbi.nlm.nih.gov/16527897/)). Combined **properdin and mannose-binding lectin (MBL2)** deficiency shows epistatic elevation of risk ([PMID: 16337490](https://pubmed.ncbi.nlm.nih.gov/16337490/)).

**Environmental risk factors.** Nasopharyngeal **carriage** is the reservoir; risk of acquisition and disease is elevated by **active and passive smoking** (personal OR 2.5, passive OR 1.6), **male sex** (OR 1.7), **age 15–24 years**, **household crowding**, and **close/household contact** with a case ([PMID: 11399012](https://pubmed.ncbi.nlm.nih.gov/11399012/)) (F007). Infancy and immunosuppression are additional risk states; the hemodynamic form is associated with older age and immunosuppression ([PMID: 40794167](https://pubmed.ncbi.nlm.nih.gov/40794167/)).

**Protective factors.** Carriage of the commensal *Neisseria lactamica* in early childhood is associated with natural immunity/protection — disease *"is a reflection of ... an absence of host resistance among those individuals not carrying N. lactamica"* ([PMID: 11057965](https://pubmed.ncbi.nlm.nih.gov/11057965/)). Vaccination (Section 13) is the dominant modifiable protective factor.

**Gene–environment interaction.** Susceptibility is fundamentally a G×E product: a complement-deficient (or complement-inhibited) host who acquires a virulent, non-carried strain from a crowded/smoking environment is at greatly amplified risk. The iatrogenic version — anti-C5 therapy plus meningococcal exposure — is the clearest example (Section 9/F009).

---

## Section 3 — Phenotypes

Meningococcemia's phenotype evolves rapidly. The classic early triad of **leg pain, cold hands/feet, and abnormal skin color** often precedes the hemorrhagic rash and meningeal signs. In primary-care children, five features carry clinically useful positive likelihood ratios (F012, [PMID: 21375891](https://pubmed.ncbi.nlm.nih.gov/21375891/)):

| Phenotype | HPO suggestion | LR+ (95% CI) | Type |
|---|---|---|---|
| Confusion | HP:0001289 | 24.2 (11.5–51.3) | Sign/behavioral |
| Leg pain | HP:0031057 (limb pain) | 7.6 (4.9–11.9) | Symptom |
| Photophobia | HP:0000613 | 6.5 (3.8–11.0) | Symptom |
| Rash (petechial/purpuric) | HP:0000979 / HP:0000967 | 5.5 (4.3–7.1) | Physical manifestation |
| Neck pain/stiffness | HP:0031179 / HP:0031352 | 5.3 (3.5–8.3) | Sign |

Additional phenotypes and suggested HPO terms:

- **Fever** (HP:0001945) — near-universal nonspecific prodrome.
- **Non-blanching petechial/purpuric rash → purpura fulminans** (HP:0011000 purpura fulminans; HP:0000979 purpura) — may begin maculopapular, becomes hemorrhagic/non-blanching; the hallmark of meningococcemia.
- **Septic shock / hypotension** (HP:0031273 shock; HP:0002615 hypotension) — the dominant driver of mortality (aOR 23.3, [PMID: 25605282](https://pubmed.ncbi.nlm.nih.gov/25605282/)).
- **Disseminated intravascular coagulation** (HP:0005521) — consumptive coagulopathy.
- **Cold extremities / poor perfusion** (HP:0025247 cold extremities) — early red flag.
- **Distal ischemia/necrosis, gangrene** (HP:0100758 gangrene) — leads to amputation.
- **Adrenal hemorrhage / acute adrenal insufficiency** (HP:0008207) — Waterhouse-Friderichsen syndrome.
- **Myocarditis / cardiac dysfunction** (HP:0001638-adjacent) — reversible myocardial depression documented in case reports ([PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/), [PMID: 30293563](https://pubmed.ncbi.nlm.nih.gov/30293563/)).
- **Laboratory abnormalities:** elevated LPS/endotoxin and IL-10, thrombocytopenia, coagulopathy, elevated CSF lactate even without pleocytosis ([PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/)).

**Onset/severity/progression.** Onset is **acute**, spanning all ages but concentrated in infants and adolescents/young adults; severity ranges **moderate-to-severe/fulminant**; progression is **rapid and episodic** (single acute episode, though complement-deficient individuals suffer recurrences).

**Quality-of-life impact.** Survivors of the septicemic form bear substantial long-term QoL burden — amputation, scarring, hearing loss, renal dysfunction, and persistent emotional distress in patients and caregivers ([PMID: 40627264](https://pubmed.ncbi.nlm.nih.gov/40627264/)).

---

## Section 4 — Genetic/Molecular Information

**This is not a Mendelian disease of a single causal human gene.** The relevant human genetics concern **host susceptibility modifiers**, all in the complement system:

| Gene | Locus / pathway | Consequence | Effect |
|---|---|---|---|
| C5, C6, C7, C8A/B, C9 | terminal pathway | Loss of function → no membrane attack complex | High susceptibility, recurrent IMD, atypical serogroups ([PMID: 25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/)) |
| CFP (properdin) | Xp11.23; X-linked | Loss of alternative-pathway amplification | Severe/recurrent IMD; serogroups Y, W-135 ([PMID: 16337490](https://pubmed.ncbi.nlm.nih.gov/16337490/), [PMID: 10909851](https://pubmed.ncbi.nlm.nih.gov/10909851/)) |
| CFD (factor D) | alternative pathway | Abolishes alternative-pathway activation vs *N. meningitidis* | Increased IMD susceptibility ([PMID: 16527897](https://pubmed.ncbi.nlm.nih.gov/16527897/)) |
| MBL2 | lectin pathway | Reduced MBL | Modifier; epistatic with properdin ([PMID: 16337490](https://pubmed.ncbi.nlm.nih.gov/16337490/)) |

**Variant characteristics.** Properdin type I deficiency arises from diverse loss-of-function variants — missense substitutions concentrated in conserved residues of exons 7–8 and premature stops elsewhere in the properdin gene ([PMID: 10909851](https://pubmed.ncbi.nlm.nih.gov/10909851/)); factor D deficiency was described from two novel *CFD* mutations segregating with meningococcal infection in a family ([PMID: 16527897](https://pubmed.ncbi.nlm.nih.gov/16527897/)). These are **germline, loss-of-function** variants; classification is pathogenic for the deficiency phenotype. Population allele frequencies are low; properdin deficiency is X-linked (males affected, carrier females show skewed X-inactivation, [PMID: 10909851](https://pubmed.ncbi.nlm.nih.gov/10909851/)).

**Pathogen genetics** (the true "causal" genome). Virulence determinants of *N. meningitidis* include the polysaccharide **capsule** (serogroup-defining, e.g. *siaD*/*ctrA* loci), **type IV pili** (PilE, and the ATPases PilF/PilT governing pilus assembly/retraction), and **lipooligosaccharide (LOS/LPS)**. Antimicrobial-resistance variants include **penA** mutations (reduced penicillin susceptibility) and **gyrA** mutations (ciprofloxacin resistance) ([PMID: 26357666](https://pubmed.ncbi.nlm.nih.gov/26357666/), [PMID: 35467371](https://pubmed.ncbi.nlm.nih.gov/35467371/)).

**Epigenetics / chromosomal abnormalities.** Not applicable as disease drivers in the human host.

---

## Section 5 — Environmental Information

**Infectious agent.** *Neisseria meningitidis* (NCBI Taxonomy txid487), a strictly human-restricted, encapsulated Gram-negative diplococcus, transmitted person-to-person via respiratory droplets and secretions. Serogroups A, B, C, W, X, Y dominate invasive disease; serogroup distribution varies geographically and shifts over time (serogroup replacement; Section 9).

**Lifestyle factors.** **Smoking** (active and passive) is the best-established modifiable environmental risk factor, elevating carriage/acquisition (personal OR 2.5, passive OR 1.6) ([PMID: 11399012](https://pubmed.ncbi.nlm.nih.gov/11399012/)). Bar/party attendance and shared bedrooms also associate with carriage ([PMID: 27861618](https://pubmed.ncbi.nlm.nih.gov/27861618/)).

**Physical/social environment.** **Crowding** (people per bedroom), **household close contact**, and **congregate settings** (dormitories, schools, military barracks) increase transmission ([PMID: 27861618](https://pubmed.ncbi.nlm.nih.gov/27861618/), [PMID: 11057965](https://pubmed.ncbi.nlm.nih.gov/11057965/)). No chemical toxin, radiation, or occupational exposure is causal; CTD/EPA-type environmental toxins are not applicable.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating event → clinical manifestation)

```
1. Nasopharyngeal acquisition of a virulent, encapsulated N. meningitidis strain
     → colonizes mucosa (carriage).
2. In a susceptible host (absent bactericidal antibody / deficient or inhibited
   complement), meningococci breach the mucosa and enter the bloodstream
     → RESULTS IN bacteremia (meningococcemia).
3. Deficient terminal/alternative complement (inherited C5–C9, properdin, factor D,
   OR iatrogenic anti-C5) fails to form the membrane attack complex
     → RESULTS IN failure to lyse the meningococcus → sustained/high-grade bacteremia.
4. Type IV pili mediate adhesion of circulating meningococci to human microvascular
   endothelial cells
     → LEADS TO vascular colonization; pilus retraction (PilT) sustains bacteremia.
        [BRANCH A — coagulopathy]                    [BRANCH B — inflammation]
5A. Adhesion triggers ADAM10-dependent           5B. LOS/LPS (lipid A) engages TLR4 on
    shedding of Endothelial Protein C Receptor        monocytes/endothelium
    (EPCR)                                              → RESULTS IN NF-κB activation and a
     → RESULTS IN loss of Protein C activation.           cytokine storm (TNF, IL-10, MIF,
6A. Impaired activated Protein C anticoagulant        IL-1β), scaling with bacterial/LPS load.
    activity + endothelial injury                  6B. Cytokines + complement anaphylatoxins
     → LEADS TO localized microvascular thrombosis      → RESULT IN vasodilation, capillary leak,
        and fibrin deposition (purpura fulminans).       and a circulating myocardial depressant
                                                          factor → distributive + cardiogenic shock.
        ↓  (branches converge)
7. Disseminated intravascular coagulation (consumption of clotting factors/platelets)
   + microthrombosis + capillary leak
     → RESULTS IN tissue hypoperfusion, purpura, distal ischemia/gangrene, and
        bilateral adrenal hemorrhage (Waterhouse-Friderichsen syndrome).
8. Multi-organ hypoperfusion + endotoxin/cytokine injury
     → RESULTS IN septic shock, acute kidney injury, myocardial dysfunction,
        and — if untreated — death.
9. In survivors, ischemic/thrombotic tissue loss
     → LEADS TO amputation, skin scarring, hearing loss, and neurologic sequelae.
```

*(Steps 5A–6A demonstrated in vitro and in humanized mouse models; step 5B/6B the TLR4-cytokine arm is supported by human plasma correlations. The convergence on DIC/shock and organ damage is established clinically.)*

### Detail by category

**Molecular pathways.** (i) **Complement cascade** — alternative and terminal pathways; membrane attack complex (C5b-9) is the effector normally clearing the meningococcus; its loss (genetic or pharmacologic) is the master susceptibility lesion (F001, F009). (ii) **TLR4/MyD88–NF-κB signaling** downstream of LPS/lipid A drives cytokine transcription (F005). (iii) **Protein C anticoagulant pathway** — EPCR/thrombomodulin-dependent; its collapse via EPCR shedding is the specific coagulopathic lesion of meningococcal purpura fulminans (F002). Suggested GO terms: GO:0006956 (complement activation), GO:0006957 (alternative pathway), GO:0002250 (adaptive immune response), GO:0007249 (I-κB kinase/NF-κB signaling), GO:0007596 (blood coagulation), GO:0030194 (positive regulation of blood coagulation).

**Cellular processes.** Inflammation (GO:0006954), endothelial activation and injury, leukocyte recruitment, platelet activation, and endothelial EPCR shedding. Cell types (CL): vascular endothelial cell (CL:0000115), monocyte (CL:0000576)/macrophage (CL:0000235), neutrophil (CL:0000775), platelet (CL:0000233).

**Protein dysfunction.** ADAM10 metalloprotease cleaves EPCR from the endothelial surface (*"we identified ADAM10 (A Disintegrin And Metalloproteinase-10) as the protease responsible for this shedding"*, [PMID: 29630665](https://pubmed.ncbi.nlm.nih.gov/29630665/)); this is a gain of proteolytic activity producing loss of anticoagulant receptor function.

**Immune involvement.** Two-edged: complement deficiency/inhibition is immunodeficiency that permits invasion, while overwhelming LPS-driven cytokine release is a maladaptive hyper-inflammatory response. IL-10 is a dominant, paradoxically deleterious mediator — IL-10 immunodepletion from meningococcal sepsis plasma markedly changes monocyte gene expression and cytokine release ([PMID: 25233959](https://pubmed.ncbi.nlm.nih.gov/25233959/)); MIF is highest in shock ([PMID: 17438452](https://pubmed.ncbi.nlm.nih.gov/17438452/)).

**Tissue damage mechanisms.** Ischemia/thrombosis (microvascular occlusion), hemorrhage (adrenal, skin), and necrosis (distal digits/limbs). A circulating **10–25 kDa proteinaceous myocardial depressant factor** causes reversible cardiac dysfunction ([PMID: 12394943](https://pubmed.ncbi.nlm.nih.gov/12394943/)).

**Molecular profiling (severity biomarkers).** Plasma LPS and IL-10 correlate with severity and are highest in non-survivors ([PMID: 25233959](https://pubmed.ncbi.nlm.nih.gov/25233959/)); in shock vs non-shock patients, median LPS 105 vs <0.04 EU/mL, IL-10 2.1×10⁴ vs 4×10¹ pg/mL, and meningococcal DNA 2.9×10⁷ vs <10³ copies/mL ([PMID: 18679115](https://pubmed.ncbi.nlm.nih.gov/18679115/)) (F005).

---

## Section 7 — Anatomical Structures Affected

**Organ / system level.**
- **Primary:** blood/circulatory system (UBERON:0000178 blood; UBERON:0001981 blood vessel), **microvascular endothelium** (skin dermal microvessels are the demonstrated adhesion target).
- **Skin** (UBERON:0002097) — purpura fulminans, petechiae, necrosis.
- **Adrenal glands** (UBERON:0002369) — bilateral hemorrhage (Waterhouse-Friderichsen syndrome).
- **Heart** (UBERON:0000948) — myocarditis/myocardial depression.
- **Kidneys** (UBERON:0002113) — acute kidney injury/renal dysfunction.
- **Meninges/CNS** (UBERON:0002360) — when concurrent meningitis is present.
- **Secondary:** distal extremities (ischemia/amputation), lungs (ARDS), liver, and coagulation system (DIC). Body systems: cardiovascular, hematologic/immune, integumentary, endocrine, renal, and nervous.

**Tissue and cell level.** Endothelial tissue is the specific target; **vascular endothelial cells** (CL:0000115) are directly colonized by type IV pili. Immune effectors: monocytes/macrophages (CL:0000576/CL:0000235), neutrophils (CL:0000775), platelets (CL:0000233).

**Subcellular level.** Endothelial **cell surface/plasma membrane** (GO:0005886) — site of EPCR and its ADAM10-mediated shedding; **extracellular space** (GO:0005615) — cytokines, LPS, complement, shed EPCR.

**Localization / lateralization.** Purpura is typically **bilateral and widespread** (trunk, extremities); adrenal hemorrhage is characteristically **bilateral**; distal ischemia often symmetric ("symmetric peripheral gangrene").

---

## Section 8 — Temporal Development

**Onset.** Acute to hyperacute. Age distribution is **bimodal-to-trimodal** with peaks in infants (<1 yr), adolescents/young adults (15–24 yr), and older adults; onset can occur at any age.

**Progression.** From nonspecific febrile prodrome the disease can progress to shock and death within ~24 hours. Stages: (1) prodrome (fever, malaise, myalgia); (2) early sepsis red-flags (leg pain, cold hands/feet, mottled skin) ([PMID: 21375891](https://pubmed.ncbi.nlm.nih.gov/21375891/)); (3) fulminant phase (purpura fulminans, DIC, shock, adrenal hemorrhage); (4) recovery or death. Course is **acute and self-limited to a single episode** in immunocompetent hosts, but **recurrent** in complement-deficient/inhibited patients.

**Patterns.** Remission is treatment-induced (antibiotics + supportive care) in survivors; there is no chronic phase. The **critical window for intervention is extremely short** — early recognition and immediate antibiotics before shock is the principal determinant of survival, since shock is the dominant independent predictor of death (aOR 23.3) ([PMID: 25605282](https://pubmed.ncbi.nlm.nih.gov/25605282/)).

---

## Section 9 — Inheritance and Population

**Epidemiology.** Endemic incidence in temperate high-income regions is typically **<1–2 per 100,000 per year**, far higher during African meningitis-belt epidemics. US population mortality (1990–2002, 3,335 deaths) was age-adjusted **0.10/100,000/yr**, with 58% of deaths in persons <25 years and elevated mortality in infants, young adults (15–24), and the elderly (>74) ([PMID: 16511378](https://pubmed.ncbi.nlm.nih.gov/16511378/)) (F014). Outbreak incidence can spike (e.g., middle-school students 6.57/100,000, [PMID: 18322129](https://pubmed.ncbi.nlm.nih.gov/18322129/)).

**Age distribution.** Infants <1 yr are the largest single pediatric group (38.6%); children <5 account for 62.7% of pediatric cases ([PMID: 42802197](https://pubmed.ncbi.nlm.nih.gov/42802197/)). Adolescents/young adults are the key **carriage reservoir** ([PMID: 42702664](https://pubmed.ncbi.nlm.nih.gov/42702664/)).

**Seasonality.** Winter/early-spring peaks; mortality *"rose in winter months and declined during the summer"* ([PMID: 16511378](https://pubmed.ncbi.nlm.nih.gov/16511378/)).

**Sex ratio.** Male predominance in carriage (OR 1.7) ([PMID: 11399012](https://pubmed.ncbi.nlm.nih.gov/11399012/)).

**Demographic disparities.** African-American mortality was **1.45×** white and **3.32×** Asian/Pacific Islander rates ([PMID: 16511378](https://pubmed.ncbi.nlm.nih.gov/16511378/)).

**Geographic distribution / serogroup dynamics.** The **African meningitis belt** historically suffered serogroup A epidemics, now eliminated by MenAfriVac; non-A serogroups (C, W, X) have emerged (serogroup X rose significantly in Ghana, P<0.01) ([PMID: 37024833](https://pubmed.ncbi.nlm.nih.gov/37024833/)). Serogroup B predominates in Europe/Americas; W (ST-11) and Y circulate widely.

**Inheritance of susceptibility.** The disease itself is infectious, not inherited, but host susceptibility follows the inheritance of complement genes: **X-linked** for properdin (CFP), **autosomal recessive** for terminal-component and factor D deficiencies. Carrier females of properdin deficiency show variable properdin levels correlated with X-inactivation skewing ([PMID: 10909851](https://pubmed.ncbi.nlm.nih.gov/10909851/)).

---

## Section 10 — Diagnostics

**Laboratory / microbiology.** Definitive diagnosis rests on **culture of *N. meningitidis* from blood or CSF** (sterile-site isolation) plus **real-time PCR** (F011). Multiplex 5′-nuclease (TaqMan) PCR targeting the capsular transport gene **ctrA** detects the organism in CSF, blood, plasma, and serum with ~**88% sensitivity** versus culture (*"The respective sensitivities (as percentages) for N. meningitidis, H. influenzae, and S. pneumoniae were 88.4, 100, and 91.8"*, [PMID: 11283086](https://pubmed.ncbi.nlm.nih.gov/11283086/)); optimized extraction raised ctrA/siaD sensitivity to 93%/91%, and PCR introduction produced a **56% increase in laboratory-confirmed cases** in the UK ([PMID: 10799809](https://pubmed.ncbi.nlm.nih.gov/10799809/)). **siaD PCR** distinguishes serogroups B and C. Supportive labs: thrombocytopenia, prolonged PT/PTT, low fibrinogen, elevated D-dimer (DIC panel), lactate, procalcitonin/CRP, and low cortisol in WFS.

**Biomarkers of severity.** Plasma LPS, IL-10, MIF, and meningococcal DNA copy number stratify shock risk and mortality ([PMID: 25233959](https://pubmed.ncbi.nlm.nih.gov/25233959/), [PMID: 18679115](https://pubmed.ncbi.nlm.nih.gov/18679115/), [PMID: 17438452](https://pubmed.ncbi.nlm.nih.gov/17438452/)).

**A diagnostic pearl:** in fulminant septicemia meningococci may be present in CSF without pleocytosis or biochemical inflammation; **elevated CSF lactate** can be the key clue and should prompt meningeal-dose beta-lactam ([PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/)).

**Imaging.** Adrenal imaging (CT/US) for suspected Waterhouse-Friderichsen syndrome; echocardiography for myocardial dysfunction; imaging is adjunctive, not diagnostic of the infection.

**Clinical criteria / differential diagnosis.** Diagnosis is clinical–microbiological. Key differentials: other bacterial sepsis with purpura (pneumococcal, *H. influenzae*, Gram-negative DIC), Rocky Mountain spotted fever and other rickettsioses, viral hemorrhagic fevers, thrombotic microangiopathies (aHUS/TTP), immune thrombocytopenia, and non-infectious purpura fulminans (protein C/S deficiency). The non-blanching purpuric rash plus rapid shock in a febrile child/young adult is the classic clinical gestalt ([PMID: 21375891](https://pubmed.ncbi.nlm.nih.gov/21375891/)).

**Genetic testing.** Not for diagnosis of the acute infection, but **complement functional testing (CH50/AH50) and targeted sequencing of terminal-complement, CFP, CFD, MBL2 genes** are indicated after invasive disease — especially recurrent episodes, atypical serogroups (Y/W-135), or family history — to identify predisposing deficiency ([PMID: 25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/), [PMID: 31421540](https://pubmed.ncbi.nlm.nih.gov/31421540/)).

---

## Section 11 — Outcome / Prognosis

**Mortality.** Case-fatality ranges roughly **8–17%** overall, higher in the fulminant septicemic form. Canadian prospective cohort (n=868, 2002–2011): CFR **8.4%** ([PMID: 25605282](https://pubmed.ncbi.nlm.nih.gov/25605282/)); Oman 25-year series: **16.7%** ([PMID: 42107173](https://pubmed.ncbi.nlm.nih.gov/42107173/)); Turkish pediatric cohort: overall **13.3%**, ranging *"from 1.2% in meningitis alone to 21.7% in combined meningitis and meningococcem[ia]"* ([PMID: 42802197](https://pubmed.ncbi.nlm.nih.gov/42802197/)) (F003). **Shock is the dominant independent predictor of death (aOR 23.30, P<0.0001)** ([PMID: 25605282](https://pubmed.ncbi.nlm.nih.gov/25605282/)).

**Morbidity / sequelae.** ~**18%** develop complications; the most common in the Canadian cohort were *"hearing loss (5.4%), skin scarring (5.4%), amputation (3.4%), renal dysfunction (2.6%), and seizures (2.5%)"* ([PMID: 25605282](https://pubmed.ncbi.nlm.nih.gov/25605282/)). A broader US/Canada review found *"10.6-41% of IMD survivors had ≥ 1 sequelae"* — seizures, deafness, stroke, amputation, scarring, renal failure — plus persistent emotional distress in survivors and caregivers ([PMID: 40627264](https://pubmed.ncbi.nlm.nih.gov/40627264/)) (F004).

**Prognostic factors.** Presence and depth of shock, DIC, extensive purpura, older age, immunosuppression, and high bacterial/LPS load worsen prognosis; the hemodynamic presentation is associated with older age, immunosuppression, and bacteremia ([PMID: 40794167](https://pubmed.ncbi.nlm.nih.gov/40794167/)). Prognostic biomarkers: plasma LPS, IL-10, MIF, DNA copy number ([PMID: 25233959](https://pubmed.ncbi.nlm.nih.gov/25233959/), [PMID: 18679115](https://pubmed.ncbi.nlm.nih.gov/18679115/)).

**Recovery.** With prompt treatment most survivors recover; myocardial depression is typically reversible ([PMID: 12394943](https://pubmed.ncbi.nlm.nih.gov/12394943/), [PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/)), but ischemic tissue loss (amputation, scarring) and sensorineural hearing loss are permanent.

---

## Section 12 — Treatment

**Empiric/first-line pharmacotherapy.** **Third-generation cephalosporins — ceftriaxone or cefotaxime — are first-line** (NCIT: Ceftriaxone C382; Cefotaxime C328). Surveillance confirms *N. meningitidis* remains uniformly susceptible: *"All isolates were susceptible to ceftriaxone, cefotaxime, meropenem, rifampin, chloramphenicol, and azithromycin. Susceptibility rates were reduced for penicillin (46.8%)"* ([PMID: 42107173](https://pubmed.ncbi.nlm.nih.gov/42107173/)); US surveillance found 8–16.7% penicillin-intermediate isolates driven by *penA* mutations ([PMID: 26357666](https://pubmed.ncbi.nlm.nih.gov/26357666/)) (F006). Meropenem (NCIT C1662) and chloramphenicol are alternatives. Meningeal-dose beta-lactam is warranted when CNS involvement is possible even without pleocytosis ([PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/)).

**Supportive/critical care.** Aggressive **fluid resuscitation, vasopressors** (norepinephrine), respiratory support, and correction of coagulopathy; the majority of severe cases require intensive care (69.9% PICU admission in the Turkish cohort) ([PMID: 42802197](https://pubmed.ncbi.nlm.nih.gov/42802197/)). For **Waterhouse-Friderichsen syndrome**, **corticosteroid (stress-dose) replacement** plus vasopressors is essential ([PMID: 38558654](https://pubmed.ncbi.nlm.nih.gov/38558654/), [PMID: 38408808](https://pubmed.ncbi.nlm.nih.gov/38408808/)).

**Adjuncts under investigation.** Vasodilators for DIC-associated distal ischemia showed benefit in a case report and merit study ([PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/)). Anticoagulant/protein-C-pathway–directed therapies are mechanistically rational given EPCR shedding but are not standard.

**Chemoprophylaxis of contacts (part of treatment strategy).** *"The first-choice antibiotic for chemoprophylaxis of close contacts is ciprofloxacin, followed by rifampicin"* ([PMID: 34843604](https://pubmed.ncbi.nlm.nih.gov/34843604/)); ceftriaxone is an alternative (NCIT: Ciprofloxacin C405; Rifampin C671). Secondary-case risk is highest in the first days and *"secondary cases rarely occur after 14 days"*, so prophylaxis must be prompt ([PMID: 18288075](https://pubmed.ncbi.nlm.nih.gov/18288075/)) (F006).

**Resistance surveillance.** Sporadic ciprofloxacin resistance (*gyrA*) and penicillin/ceftriaxone reduced-susceptibility invasive lineages (serogroup W ST-11) are emerging, mandating ongoing monitoring ([PMID: 35467371](https://pubmed.ncbi.nlm.nih.gov/35467371/), [PMID: 18288075](https://pubmed.ncbi.nlm.nih.gov/18288075/)).

**Pharmacogenomics / advanced therapeutics.** Not applicable — no gene, cell, RNA, or targeted molecular therapy exists for the infection itself.

---

## Section 13 — Prevention

**Primary prevention — vaccination (mainstay).** (F008)

| Vaccine | Target | Key evidence |
|---|---|---|
| **MenAfriVac** (monovalent A conjugate) | Serogroup A | *"Wide use of the groundbreaking vaccine MenAfriVac® has eliminated serogroup A meningococcal meningitis in the African meningitis belt"* ([PMID: 40968077](https://pubmed.ncbi.nlm.nih.gov/40968077/), [PMID: 35455366](https://pubmed.ncbi.nlm.nih.gov/35455366/)) |
| **Quadrivalent ACWY conjugate** (MenACWY-TT, MenACWY-CRM) | A, C, W, Y | Adolescent programs; infant safety demonstrated ([PMID: 42642862](https://pubmed.ncbi.nlm.nih.gov/42642862/)) |
| **Pentavalent ACWYX** (NmCV-5/MenFive) | A, C, W, Y, X | *"Crude VE against all meningococcal meningitis was 88% (95% CI: 62-96), and against NmC specifically was 86% (95% CI: 50-96)"* in a Niger outbreak ([PMID: 42585809](https://pubmed.ncbi.nlm.nih.gov/42585809/), [PMID: 40968077](https://pubmed.ncbi.nlm.nih.gov/40968077/)) |
| **4CMenB** (protein-based) | Serogroup B | England: 75% reduction in MenB IMD in immunized infants; adjusted efficacy 52.7% after primary series, 59.1% after booster ([PMID: 42347623](https://pubmed.ncbi.nlm.nih.gov/42347623/)) |

Serogroup replacement (e.g., emergence of X, shifts in C/W) drives the move to broader pentavalent coverage — *"Serogroup X showed a significant upward trend (P < 0.01)"* ([PMID: 37024833](https://pubmed.ncbi.nlm.nih.gov/37024833/)).

**Behavioral primary prevention.** Smoking cessation and reduction of household crowding lower carriage/transmission ([PMID: 11399012](https://pubmed.ncbi.nlm.nih.gov/11399012/)).

**Secondary/tertiary prevention.** Rapid recognition of red-flag symptoms and immediate antibiotics prevent progression to shock; **contact chemoprophylaxis** (ciprofloxacin/rifampicin) prevents secondary cases ([PMID: 34843604](https://pubmed.ncbi.nlm.nih.gov/34843604/), [PMID: 27227736](https://pubmed.ncbi.nlm.nih.gov/27227736/)).

**Special high-risk population — complement-inhibitor recipients.** Anti-C5 therapy (eculizumab, ravulizumab) *"increases the risk of invasive meningococcal infections"* by blocking terminal C5b-9 ([PMID: 42137634](https://pubmed.ncbi.nlm.nih.gov/42137634/), [PMID: 42234874](https://pubmed.ncbi.nlm.nih.gov/42234874/)) (F009). Expert consensus mandates **vaccination against A, C, W, Y and B for all patients on complement inhibitors, plus antibiotic prophylaxis** (penicillin/rifampicin), because **breakthrough IMD occurs despite vaccination** ([PMID: 42074848](https://pubmed.ncbi.nlm.nih.gov/42074848/)).

**Public-health interventions.** Outbreak response includes mass vaccination and expanded chemoprophylaxis of contacts ([PMID: 27227736](https://pubmed.ncbi.nlm.nih.gov/27227736/)); surveillance of serogroups and resistance guides policy.

---

## Section 14 — Other Species / Natural Disease

***Neisseria meningitidis* is a strictly human-specific pathogen** with **no natural animal reservoir or naturally occurring animal disease** (F013). *"Studying the pathogenesis of this infection was previously limited by the human specificity of the bacteria, which makes in vivo models difficult"* ([PMID: 24747976](https://pubmed.ncbi.nlm.nih.gov/24747976/)). Consequently:

- **Taxonomy of affected species:** *Homo sapiens* only (NCBI Taxon 9606). Pathogen: *Neisseria meningitidis* (txid487).
- **Breed / VBO:** not applicable.
- **Natural disease in other species (OMIA/VetCompass):** none — there is no companion-animal or wildlife meningococcemia.
- **Comparative biology:** the human specificity arises from species-restricted host receptors (e.g., human EPCR, human complement regulators, human CEACAMs and transferrin) that the meningococcus exploits. This is a striking example of host-restricted molecular tropism.
- **Zoonotic potential:** none.

---

## Section 15 — Model Organisms

Because of strict human specificity, conventional animal models fail; the field relies on **humanized systems** (F013):

| Model | Type | Recapitulation | Reference |
|---|---|---|---|
| **Human skin-graft SCID/Beige mouse** ("humanized mouse") | Mammalian, humanized xenograft | Bacteria adhere exclusively to human dermal microvessels → human cytokine secretion, inflammatory recruitment, vascular leakage, thrombosis, and **purpura** — *"replicating the clinical presentation for the first time in an animal model"* | [PMID: 23359320](https://pubmed.ncbi.nlm.nih.gov/23359320/), [PMID: 24747976](https://pubmed.ncbi.nlm.nih.gov/24747976/) |
| Type IV pilus mutants in the humanized model | Genetic (bacterial) manipulation | Pilus-adhesion mutants fail to cause vascular damage; **PilT-dependent pilus retraction required for sustained bacteremia and lethality** | [PMID: 33592056](https://pubmed.ncbi.nlm.nih.gov/33592056/) |
| **3D microfluidic human vessel model** | In vitro engineered human vasculature | Reproduces endothelial integrity/permeability; quantifies microcolony growth, cytoskeleton rearrangement, E-selectin expression, neutrophil response; validated against skin-xenograft mouse | [PMID: 41406015](https://pubmed.ncbi.nlm.nih.gov/41406015/) |
| Properdin-knockout mouse | Mammalian genetic | Probes complement/shock biology in non-septic shock models (not a full IMD model) | [PMID: 18453618](https://pubmed.ncbi.nlm.nih.gov/18453618/) |

**Key mechanistic insight from models:** type IV pili adhesion is the main in vivo mediator of vascular association (*"The adhesive properties of the type IV pili of N. meningitidis were found to be the main mediator of association with the dermal microvessels in vivo"*, [PMID: 23359320](https://pubmed.ncbi.nlm.nih.gov/23359320/)).

**Limitations of models:** the skin-graft model captures the microvascular/purpuric arm but not full systemic multi-organ sepsis, meningitis, or the human adaptive immune response; in vitro vessel models lack systemic physiology. No standard MGI/ZFIN/FlyBase genetic model of the disease exists because the host substrate must be human tissue.

---

## Mechanistic Model / Interpretation

The unifying interpretation is that **meningococcemia is a disease of two converging catastrophes on the human microvascular endothelium**, gated upstream by complement.

```
        HOST GATE (complement)                 PATHOGEN DRIVERS
   terminal C5–C9 / properdin / factor D    type IV pili + capsule + LOS/LPS
   deficient OR anti-C5-inhibited                     │
              │ (permits invasion)                    │
              ▼                                        ▼
        HIGH-GRADE BACTEREMIA  ───────────►  ENDOTHELIAL ADHESION (pili)
                                                       │
                        ┌──────────────────────────────┴───────────────────┐
                        ▼ COAGULOPATHY ARM                    INFLAMMATION ARM ▼
             ADAM10 → EPCR shedding                        LPS → TLR4 → NF-κB
             ↓ Protein C activation                        ↑ IL-10, TNF, MIF, IL-1β
             microvascular thrombosis                      vasodilation, capillary leak,
             = PURPURA FULMINANS                            myocardial depressant factor
                        └──────────────► DIC + SHOCK ◄──────────────┘
                                            │
              ┌─────────────┬───────────────┼───────────────┬──────────────┐
              ▼             ▼               ▼               ▼              ▼
        adrenal        distal limb      acute kidney    myocardial     hearing loss/
        hemorrhage     ischemia →       injury          dysfunction    neuro sequelae
        (WFS)          amputation
```

Two features make meningococcemia mechanistically distinctive rather than generic Gram-negative sepsis: (1) the **specific ADAM10/EPCR/Protein-C lesion** that concentrates thrombosis in the skin microvasculature to produce purpura fulminans, and (2) the **complement gate** that determines who gets invasive disease at all — a gate now routinely opened pharmacologically by anti-C5 drugs. Upstream = complement gate + bacteremia; midstream = pili-driven endothelial adhesion; downstream branches = coagulopathy (EPCR) and inflammation (LPS) converging on DIC/shock; terminal = organ-specific damage and, in survivors, permanent ischemic sequelae.

---

## Evidence Base

| Finding | Key PMIDs | Evidence type | Role |
|---|---|---|---|
| Complement/properdin/factor D deficiency → susceptibility | [25037634](https://pubmed.ncbi.nlm.nih.gov/25037634/), [16527897](https://pubmed.ncbi.nlm.nih.gov/16527897/), [16337490](https://pubmed.ncbi.nlm.nih.gov/16337490/), [10909851](https://pubmed.ncbi.nlm.nih.gov/10909851/) | Human genetics/immunology | Supports host gate |
| EPCR shedding / purpura fulminans mechanism | [29630665](https://pubmed.ncbi.nlm.nih.gov/29630665/), [33592056](https://pubmed.ncbi.nlm.nih.gov/33592056/) | In vitro + humanized model | Supports coagulopathy arm |
| Two clinical forms, form-dependent mortality | [40794167](https://pubmed.ncbi.nlm.nih.gov/40794167/), [42802197](https://pubmed.ncbi.nlm.nih.gov/42802197/) | Human cohorts | Clinical phenotype |
| Mortality ~8–17%, sequelae 10–20% | [25605282](https://pubmed.ncbi.nlm.nih.gov/25605282/), [40627264](https://pubmed.ncbi.nlm.nih.gov/40627264/), [42107173](https://pubmed.ncbi.nlm.nih.gov/42107173/) | Human cohorts/reviews | Prognosis |
| LPS/IL-10/MIF drive shock | [25233959](https://pubmed.ncbi.nlm.nih.gov/25233959/), [18679115](https://pubmed.ncbi.nlm.nih.gov/18679115/), [17438452](https://pubmed.ncbi.nlm.nih.gov/17438452/), [12394943](https://pubmed.ncbi.nlm.nih.gov/12394943/) | Human + in vitro | Inflammation arm |
| Cephalosporin first-line; prophylaxis; resistance | [42107173](https://pubmed.ncbi.nlm.nih.gov/42107173/), [26357666](https://pubmed.ncbi.nlm.nih.gov/26357666/), [34843604](https://pubmed.ncbi.nlm.nih.gov/34843604/), [18288075](https://pubmed.ncbi.nlm.nih.gov/18288075/), [35467371](https://pubmed.ncbi.nlm.nih.gov/35467371/) | Surveillance/guidelines | Treatment |
| Carriage/transmission risk factors | [11399012](https://pubmed.ncbi.nlm.nih.gov/11399012/), [27861618](https://pubmed.ncbi.nlm.nih.gov/27861618/), [11057965](https://pubmed.ncbi.nlm.nih.gov/11057965/) | Human epidemiology | Etiology/prevention |
| Conjugate & 4CMenB vaccines | [40968077](https://pubmed.ncbi.nlm.nih.gov/40968077/), [42585809](https://pubmed.ncbi.nlm.nih.gov/42585809/), [42347623](https://pubmed.ncbi.nlm.nih.gov/42347623/), [35455366](https://pubmed.ncbi.nlm.nih.gov/35455366/), [37024833](https://pubmed.ncbi.nlm.nih.gov/37024833/) | Trials/effectiveness | Prevention |
| Iatrogenic risk from anti-C5 | [42234874](https://pubmed.ncbi.nlm.nih.gov/42234874/), [42137634](https://pubmed.ncbi.nlm.nih.gov/42137634/), [42074848](https://pubmed.ncbi.nlm.nih.gov/42074848/) | Consensus/case reports | Etiology/prevention |
| Waterhouse-Friderichsen syndrome | [42665693](https://pubmed.ncbi.nlm.nih.gov/42665693/), [38408808](https://pubmed.ncbi.nlm.nih.gov/38408808/), [38558654](https://pubmed.ncbi.nlm.nih.gov/38558654/) | Autopsy review/cases | Complication |
| Diagnosis: culture + ctrA PCR | [11283086](https://pubmed.ncbi.nlm.nih.gov/11283086/), [10799809](https://pubmed.ncbi.nlm.nih.gov/10799809/) | Diagnostic validation | Diagnostics |
| Early red-flag symptoms | [21375891](https://pubmed.ncbi.nlm.nih.gov/21375891/) | Primary-care study | Phenotype/diagnosis |
| Human-restricted; humanized models | [23359320](https://pubmed.ncbi.nlm.nih.gov/23359320/), [24747976](https://pubmed.ncbi.nlm.nih.gov/24747976/), [33592056](https://pubmed.ncbi.nlm.nih.gov/33592056/), [41406015](https://pubmed.ncbi.nlm.nih.gov/41406015/) | Model organism | Models/species |
| Epidemiology: age, season, disparity | [16511378](https://pubmed.ncbi.nlm.nih.gov/16511378/), [42802197](https://pubmed.ncbi.nlm.nih.gov/42802197/), [18322129](https://pubmed.ncbi.nlm.nih.gov/18322129/) | Population surveillance | Epidemiology |

---

## Limitations and Knowledge Gaps

1. **No primary molecular data were analyzed** in this investigation; findings are a literature synthesis. Quantitative claims derive from the cited cohorts and reviews, whose populations, eras, and definitions vary (pediatric vs adult, endemic vs epidemic settings), so pooled mortality/sequelae ranges are approximate.
2. **Serogroup- and region-specific granularity** (variant-level epidemiology, exact incidence per serogroup by country/year) was not exhaustively resolved; serogroup replacement is dynamic.
3. **Host-genetic susceptibility beyond complement** (e.g., GWAS-identified common variants such as CFH/CFHR3 loci) was not deeply explored and merits dedicated review.
4. **Therapeutic modulation of the EPCR/Protein-C axis** is mechanistically compelling but clinically unproven; whether restoring EPCR/activated Protein C alters purpura fulminans outcomes is unknown.
5. **Model limitations:** humanized skin-graft and microfluidic models capture microvascular pathology but not systemic multi-organ sepsis, meningitis, or adaptive immunity.
6. **Long-term neurocognitive and psychosocial outcomes** in survivors are under-quantified relative to acute mortality.

---

## Proposed Follow-up Experiments / Actions

1. **Test EPCR/Protein-C–directed adjunct therapy** (e.g., recombinant activated Protein C analogs, ADAM10 inhibition, soluble EPCR) in the humanized skin-graft and 3D microfluidic vessel models, then in early-phase trials for purpura fulminans.
2. **Prospective biomarker-guided risk stratification**: validate a combined plasma LPS + IL-10 + meningococcal DNA copy-number panel as an early triage tool to identify patients destined for shock ([PMID: 18679115](https://pubmed.ncbi.nlm.nih.gov/18679115/)).
3. **Systematic host-genetic study** integrating complement functional assays (CH50/AH50) with sequencing of terminal-complement, CFP, CFD, MBL2, and complement-regulator genes in recurrent/atypical IMD survivors to define screening yield.
4. **Vaccine-policy modeling** for a life-course strategy (infant + adolescent + older-adult) and for pentavalent ACWYX rollout, incorporating serogroup-replacement surveillance ([PMID: 42702664](https://pubmed.ncbi.nlm.nih.gov/42702664/), [PMID: 37024833](https://pubmed.ncbi.nlm.nih.gov/37024833/)).
5. **Optimize complement-inhibitor safety**: prospective registry of breakthrough IMD in eculizumab/ravulizumab recipients to define the optimal vaccination + antibiotic-prophylaxis regimen ([PMID: 42074848](https://pubmed.ncbi.nlm.nih.gov/42074848/)).
6. **Antimicrobial-resistance genomic surveillance** for *penA*/*gyrA* lineages (serogroup W ST-11) to preserve empiric cephalosporin and prophylaxis efficacy ([PMID: 35467371](https://pubmed.ncbi.nlm.nih.gov/35467371/)).
7. **Trial of vasodilator therapy** for DIC-associated distal ischemia to reduce amputation, following the case-report signal ([PMID: 30871501](https://pubmed.ncbi.nlm.nih.gov/30871501/)).

---

*Report compiled from 14 confirmed findings and 57 reviewed papers across a 5-iteration investigation. Ontology suggestions (HPO, GO, CL, UBERON, NCIT, MONDO) are provided inline for knowledge-base ingestion.*


## Artifacts

- [OpenScientist final report](Meningococcemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Meningococcemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 48 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 21 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0042972` (3 mentions) - the report calls it "if available", "meningococcemia"; MONDO calls it **meningococcemia**
- `HP:0031057` (1 mention) - the report calls it "limb pain"; HP calls it **Skin fissure**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008207` (1 mention) - the report calls it "Adrenal hemorrhage / acute adrenal insufficiency"; HP calls it **Primary adrenal insufficiency**, and lists "Adrenocortical insufficiency" among its other names
- `GO:0006957` (1 mention) - the report calls it "alternative pathway"; GO calls it **complement activation, alternative pathway**, and lists "complement cascade, alternative pathway" among its other names
- `GO:0007249` (1 mention) - the report calls it "I-κB kinase/NF-κB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `CL:0000115` (2 mentions) - the report calls it "vascular endothelial cells"; CL calls it **endothelial cell**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0002360` (1 mention) - the report calls it "Meninges/CNS"; UBERON calls it **meninx**, and lists "meningeal layer" among its other names
- `GO:0005886` (1 mention) - the report calls it "cell surface/plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names
- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0042972` - called "if available", "meningococcemia"
