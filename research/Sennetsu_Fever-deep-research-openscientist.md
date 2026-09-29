---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T12:04:37.890737'
end_time: '2026-09-28T12:20:51.719206'
duration_seconds: 973.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Sennetsu Fever
  mondo_id: MONDO:0000332
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
citation_count: 36
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 14
  quotes_not_checkable: 1
  relevance_assessed: 36
  on_topic: 24
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 39
  verified: 38
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 16
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: GO:0030260
    reported_labels:
    - entry into host cell
    ontology_label: GO_0030260
  - term_id: NCIT:C692
    reported_labels:
    - Doxycycline
    ontology_label: Nimodipine
  - term_id: NCIT:C61815
    reported_labels:
    - Minocycline
    ontology_label: Loracarbef Anhydrous
  - term_id: NCIT:C844
    reported_labels:
    - Tetracycline
    ontology_label: Streptonigrin
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0030260
    ontology_label: GO_0030260
    replaced_by: GO:0044409
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Sennetsu_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Sennetsu_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sennetsu Fever
- **MONDO ID:** MONDO:0000332 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Sennetsu Fever** covering all of the
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

# Sennetsu Fever (Sennetsu Neorickettsiosis): A Comprehensive Disease Characteristics Report

**Disease:** Sennetsu Fever | **MONDO ID:** MONDO:0000332 | **Category:** Infectious Disease
**Etiologic agent:** *Neorickettsia sennetsu* (formerly *Rickettsia sennetsu* / *Ehrlichia sennetsu*)

---

## Summary

**Sennetsu fever is an acute, self-limited, infectious-mononucleosis-like febrile illness caused by *Neorickettsia sennetsu*, a Gram-negative obligate intracellular bacterium of the family Anaplasmataceae (order Rickettsiales, α-Proteobacteria) that replicates within cytoplasmic vacuoles (morulae) of host monocytes and macrophages.** Unlike the tick-borne human ehrlichioses (human monocytic ehrlichiosis caused by *E. chaffeensis*, human granulocytic anaplasmosis caused by *A. phagocytophilum*), Sennetsu fever has **no arthropod vector**. It is a **fish-borne zoonosis**: *N. sennetsu* is a bacterial endosymbiont of digenean trematodes (flukes), and humans are believed to acquire infection by ingesting raw or undercooked fish that harbor metacercariae of infected flukes. The disease is **not genetic** — there are no causal human genes, pathogenic variants, or heritable susceptibility loci; the "molecular/genetic" story of this disease is entirely that of the pathogen's genome and its host–pathogen interaction.

The illness was first recognized in western/southern Japan in the 1950s under the names "Hyuga fever," "Kagami fever," and "glandular fever," epidemiologically linked to raw consumption of grey mullet (*Mugil cephalus*). It presents after roughly a two-week incubation with **fever, chills, headache, malaise, myalgia, generalized (especially postauricular and cervical) lymphadenopathy, hepatosplenomegaly, and peripheral-blood atypical lymphocytosis**. Diagnosis rests on **indirect fluorescent antibody (IFA) serology, PCR/16S rRNA sequencing, and culture**, with intracytoplasmic morulae occasionally visible in monocytes on Giemsa-stained smears. Treatment is with **tetracyclines (doxycycline of choice)**, to which the organism responds rapidly; notably, *N. sennetsu* also retains natural fluoroquinolone susceptibility (GyrA Ser83), unlike resistant *Ehrlichia* species.

Epidemiologically the disease is **rare and under-recognized** — fewer than 100 patients reported globally over ~50 years — yet **subclinical exposure is common** in endemic areas: IgG seroprevalence reaches ~17% among blood donors and febrile patients in Laos, contrasted with only 0.2% of febrile Lao inpatients showing acute PCR-confirmed infection. This gap between high seroprevalence and rare severe disease indicates that most infections are mild or self-resolving. **Prognosis is favorable** — an acutely incapacitating but self-limited, treatable illness with very low mortality and no documented chronic carriage in humans.

---

## Section 1 — Disease Information

**Overview.** Sennetsu fever (Sennetsu neorickettsiosis; Sennetsu rickettsiosis) is an acute zoonotic bacterial infection of monocytes and macrophages producing a mononucleosis-like syndrome. It is described in the literature as "a special type of infectious mononucleosis found in western Japan" ([PMID: 1165122](https://pubmed.ncbi.nlm.nih.gov/1165122/)) and "a little-known human mononucleosis-like disease" unique historically to southern Japan ([PMID: 6425420](https://pubmed.ncbi.nlm.nih.gov/6425420/)).

**Key identifiers.**

| Resource | Identifier / status |
|---|---|
| MONDO | MONDO:0000332 (Sennetsu fever) |
| MeSH | "Sennetsu fever" indexed under Ehrlichiosis / Rickettsiaceae infections |
| OMIM | Not applicable (infectious, non-Mendelian disease) |
| Orphanet | Not a classic Orphanet rare-genetic-disease entry |
| ICD-10 | A79.8 (Other specified rickettsioses) — no specific dedicated code |
| ICD-11 | 1C30-range (Rickettsioses) — no dedicated specific stem code |
| NCBI Taxonomy (agent) | *Neorickettsia sennetsu* |

**Synonyms / alternative names:** Sennetsu neorickettsiosis; Sennetsu rickettsiosis; Sennetsu ehrlichiosis; Hyuga fever; Kagami fever; glandular fever (historical Japanese names); infectious mononucleosis of western Japan.

**Source of information:** All information is derived from **aggregated disease-level resources** — case reports, seroepidemiological surveys, experimental animal/cell-culture studies, and microbiological/genomic characterization — rather than from individual-patient EHR data. Given fewer than 100 globally reported cases ([PMID: 26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/)), the evidence base is small and heavily weighted toward microbiology and seroepidemiology.

---

## Section 2 — Etiology

**Primary cause (infectious).** The disease is caused solely by infection with ***Neorickettsia sennetsu***. As stated directly: "*Neorickettsia sennetsu* is an obligate intracellular bacterium of monocytes and macrophages and is the etiologic agent of human Sennetsu neorickettsiosis" ([PMID: 20833807](https://pubmed.ncbi.nlm.nih.gov/20833807/)). There is **no genetic etiology, no pathogenic human variant, and no inheritance** — Section 4 (human genetics), and the genetic portions of Sections 9, 10, and 12–13 are **not applicable** to this disease.

**Transmission / risk factors (environmental).** The dominant risk factor is **dietary — consumption of raw or undercooked freshwater/brackish fish** carrying Neorickettsia-infected fluke metacercariae. *N. sennetsu* DNA was detected by PCR "for the first time, in a fish (*Anabas testudineus*)" (climbing perch) in Laos ([PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/)). Flukes are the reservoir/vector: "*Neorickettsia* spp. are bacterial endosymbionts of parasitic flukes (Digenea) that also have the potential to infect and cause disease (e.g., Sennetsu fever) in the vertebrate hosts of the fluke" ([PMID: 26873314](https://pubmed.ncbi.nlm.nih.gov/26873314/)). Historically, "metacercariae found in the muscles of grey mullets (*Mugil cephalus*) ingested raw by most 'Hyuga' fever patients" implicated raw grey mullet as the vehicle ([PMID: 7311106](https://pubmed.ncbi.nlm.nih.gov/7311106/)).

Additional risk considerations: residence in or travel to endemic regions (western/southern Japan, Laos, Thailand, Malaysia); occupational or cultural exposure to raw fish dishes. **No arthropod vector** is involved, distinguishing Sennetsu fever from all other human ehrlichioses/anaplasmoses.

**Protective factors:** Thorough **cooking of fish** is the logical primary protective measure (inferred; not formally trialed). No genetic protective variants are relevant. **Gene–environment interactions:** Not applicable — there is no human genetic component.

---

## Section 3 — Phenotypes

Sennetsu fever produces a stereotyped **infectious-mononucleosis-like** clinical picture. Members of the tribe Ehrlichieae including *E. sennetsu* "reside primarily in the cytoplasmic vacuoles of monocytes or granulocytes and cause hematologic abnormalities, lymphadenopathy, and other pathologic changes in the host" ([PMID: 1889044](https://pubmed.ncbi.nlm.nih.gov/1889044/)).

| Phenotype | Type | HPO suggestion | Onset / course | Notes |
|---|---|---|---|---|
| Fever | Symptom/sign | HP:0001945 (Fever) | Acute, ~2 wk after exposure | Cardinal feature |
| Chills | Symptom | HP:0025143 (Chills) | Acute | Common prodrome |
| Headache | Symptom | HP:0002315 (Headache) | Acute | Nonspecific |
| Malaise / fatigue | Symptom | HP:0033834 (Malaise) | Acute | Acutely incapacitating |
| Myalgia | Symptom | HP:0003326 (Myalgia) | Acute | Flu-like |
| Generalized lymphadenopathy (postauricular, cervical) | Clinical sign | HP:0002716 (Lymphadenopathy) | Acute | "Glandular fever" naming reflects this |
| Hepatomegaly | Clinical sign | HP:0002240 (Hepatomegaly) | Acute | Hepatosplenomegaly |
| Splenomegaly | Clinical sign | HP:0001744 (Splenomegaly) | Acute | Hepatosplenomegaly |
| Atypical lymphocytosis | Lab abnormality | HP:0001915 / HP:0031409 (abnormal lymphocyte morphology/count) | Acute | Mononucleosis-like; peripheral smear |
| Leukopenia / lymphopenia | Lab abnormality | HP:0001882 (Leukopenia) | Acute | Reported for ehrlichioses generally |
| Thrombocytopenia | Lab abnormality | HP:0001873 (Thrombocytopenia) | Acute | Reported for ehrlichioses generally |

**Characteristics:** Age of onset — any age with dietary exposure (adult-predominant given diet). Severity — generally **mild to moderate and self-limited**, occasionally "acutely incapacitating" ([PMID: 19635866](https://pubmed.ncbi.nlm.nih.gov/19635866/)). Progression — **acute, self-limited**, resolving spontaneously or rapidly with antibiotics. Frequency — fever and lymphadenopathy are near-universal in symptomatic cases; hematologic abnormalities (leukopenia, thrombocytopenia) are described for ehrlichioses broadly ([PMID: 16786789](https://pubmed.ncbi.nlm.nih.gov/16786789/)).

**Quality-of-life impact:** Acute incapacitation during the febrile phase, but full recovery is expected; no documented long-term disability.

---

## Section 4 — Genetic / Molecular Information

**Human genetics: NOT APPLICABLE.** Sennetsu fever is an infectious disease with **no causal genes, no pathogenic germline/somatic variants, no modifier genes, no epigenetic disease mechanism, and no chromosomal abnormalities** in the human host.

The "molecular information" of relevance concerns the **pathogen genome**:

- ***N. sennetsu* has a small, reduced genome** typical of obligate intracellular Anaplasmataceae: ~878.5 kb by pulsed-field gel electrophoresis ([PMID: 10418133](https://pubmed.ncbi.nlm.nih.gov/10418133/)) and ~881 kb ([PMID: 10765728](https://pubmed.ncbi.nlm.nih.gov/10765728/)); the complete genome (~936 ORFs) was sequenced in comparative genomics of ehrlichiosis agents ([PMID: 16482227](https://pubmed.ncbi.nlm.nih.gov/16482227/)).
- **High conservation with its sister species:** "758 (88.2%) of protein-coding genes are conserved between *N. risticii* and *N. sennetsu*" ([PMID: 19661282](https://pubmed.ncbi.nlm.nih.gov/19661282/)).
- **Retained biosynthetic capacity:** "Unlike members of the Rickettsiaceae family, these pathogenic Anaplasmataceae are capable of making all major vitamins, cofactors, and nucleotides" ([PMID: 16482227](https://pubmed.ncbi.nlm.nih.gov/16482227/)), though with diminished amino-acid biosynthesis.
- **Encoded virulence/interaction machinery:** a type IV secretion system (T4SS), two-component regulatory systems, and expanded outer-membrane protein families; the major surface antigen **P51** functions as a porin and, with Nsp3, is a dominant surface antigen ([PMID: 20833807](https://pubmed.ncbi.nlm.nih.gov/20833807/)).

**Taxonomy of the agent** was reorganized on molecular phylogeny (16S rRNA, groESL): *Rickettsia sennetsu* → *Ehrlichia sennetsu* → ***Neorickettsia sennetsu*** ([PMID: 11760958](https://pubmed.ncbi.nlm.nih.gov/11760958/); minimum 94.9% intra-clade 16S similarity for the Neorickettsia clade).

---

## Section 5 — Environmental Information

**Infectious agent:** *Neorickettsia sennetsu* — Gram-negative, obligate intracellular α-proteobacterium (family Anaplasmataceae). Reference strain **ATCC VR-367 (Miyayama strain)**.

**Reservoir/vector:** Digenean trematodes (flukes). *Neorickettsia* spp. localize within virtually all fluke life-cycle stages (sporocysts, cercariae, metacercariae, adults) and are maintained by **vertical transmission through vitelline cells into eggs** ([PMID: 26873314](https://pubmed.ncbi.nlm.nih.gov/26873314/)). A related genome, the *Fasciola hepatica* endobacterium (nFh, 859,205 bp), is "closely related to the etiological agents of human Sennetsu and Potomac horse fevers" and was localized to the fluke's reproductive tract, eggs, Mehlis' gland, seminal vesicle, and oral suckers — "suggesting putative routes for fluke-to-fluke and fluke-to-host transmission" ([PMID: 28060841](https://pubmed.ncbi.nlm.nih.gov/28060841/)).

**Environmental / lifestyle factor:** the single dominant exposure is **eating raw/undercooked fish** carrying infected metacercariae. No toxins, radiation, pollution, smoking, alcohol, or other lifestyle factors are implicated.

**Chemical entities (CHEBI):** iron/Fe(3+) (CHEBI:29034) — central to pathogen nutrition; doxycycline (CHEBI:50845), tetracycline (CHEBI:27902), minocycline (CHEBI:50694), deferoxamine (CHEBI:4356) as pharmacological entities of relevance.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. A human **ingests raw/undercooked fish** harboring digenean-fluke metacercariae that contain *N. sennetsu* → **introduces the bacterium** into the host (inferred transmission route; direct fish-to-human proof is indirect — fish PCR positivity, [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/)).
2. Released *N. sennetsu* **enters and is taken up by monocytes/macrophages**, its obligatory host cells → **establishes intracellular residence** ([PMID: 20833807](https://pubmed.ncbi.nlm.nih.gov/20833807/)).
3. Inside the cell, the bacterium **resides in a membrane-bound phagosome/vacuole and inhibits phagosome–lysosome fusion** → **evades lysosomal killing** ("unlike rickettsiae, ehrlichiae and chlamydiae multiply in the phagosome of their host cells," [PMID: 1884777](https://pubmed.ncbi.nlm.nih.gov/1884777/)).
4. The bacterium **delivers signals that disable host microbicidal alarm systems** → **creates a "safe haven"** conditioning the leukocyte to share space and nutrients ([PMID: 12860688](https://pubmed.ncbi.nlm.nih.gov/12860688/)).
5. To fuel replication, it **up-regulates host transferrin receptor (TfR) by activating iron-responsive protein 1 (IRP1)** → **increases intracellular iron acquisition** (TfR mRNA rises by 6 h, peaks 24 h; growth blocked by iron chelator deferoxamine — [PMID: 10225882](https://pubmed.ncbi.nlm.nih.gov/10225882/)).
6. Adequately supplied with iron and nutrients (P51 porin admits L-glutamine/sugars), the bacterium **replicates by binary fission into intracytoplasmic microcolonies (morulae)** → **expands the infected monocyte/macrophage population** ([PMID: 6274798](https://pubmed.ncbi.nlm.nih.gov/6274798/); [PMID: 9511829](https://pubmed.ncbi.nlm.nih.gov/9511829/)).
7. Infected macrophages **disseminate to spleen, liver, lymph nodes, and bone marrow** → **produce lymphoreticular activation and organ enlargement** (hepatosplenomegaly, lymphadenopathy) (spleen/macrophage tropism in mice — [PMID: 1165122](https://pubmed.ncbi.nlm.nih.gov/1165122/)).
8. The host mounts a **cell-mediated / reactive lymphocytic response** → produces **atypical lymphocytosis and the mononucleosis-like syndrome** ([PMID: 1889044](https://pubmed.ncbi.nlm.nih.gov/1889044/)).
9. **Systemic cytokine/inflammatory response** → **fever, chills, headache, malaise, myalgia**, plus hematologic abnormalities (leukopenia, thrombocytopenia) (branch: overlapping with other ehrlichioses — [PMID: 16786789](https://pubmed.ncbi.nlm.nih.gov/16786789/)).
10. **Host immunity (importantly cell-mediated) controls infection** → **self-limited resolution**; immunosuppression removes this brake (cyclophosphamide enhances splenic bacterial titers >100-fold in mice — [PMID: 1165122](https://pubmed.ncbi.nlm.nih.gov/1165122/)).

### Supporting detail

- **Molecular pathways / biochemical abnormalities:** IRP1-mediated stabilization of TfR mRNA (iron-response pathway) is the best-characterized host-manipulation node; blocking it (deferoxamine) or arresting bacterial protein synthesis (oxytetracycline, added 6 h post-infection returned TfR mRNA toward baseline) halts replication ([PMID: 10225882](https://pubmed.ncbi.nlm.nih.gov/10225882/)).
- **Metabolic strategy:** the bacterium derives ATP from its **own catabolic activities** (unlike energy-parasitic chlamydiae) and is biosynthetically competent for vitamins/cofactors/nucleotides ([PMID: 1884777](https://pubmed.ncbi.nlm.nih.gov/1884777/); [PMID: 16482227](https://pubmed.ncbi.nlm.nih.gov/16482227/)).
- **Cellular processes:** phagosome maturation arrest, intracellular parasitism, macrophage activation, reactive lymphocyte proliferation.
- **Ultrastructure:** the *E. sennetsu*–*E. risticii* genogroup "usually developed in small individual vacuoles that did not fuse with each other and divided along with the ehrlichiae" ([PMID: 9511829](https://pubmed.ncbi.nlm.nih.gov/9511829/)).

**GO term suggestions:** GO:0030260 (entry into host cell); GO:0051673 (disruption of host cell); GO:0006826 (iron ion transport); GO:0006879 (intracellular iron ion homeostasis); GO:0090382 (phagosome maturation) — inhibited; GO:0006954 (inflammatory response). **CL term suggestions:** CL:0000576 (monocyte); CL:0000235 (macrophage); CL:0000842 (mononuclear cell).

---

## Section 7 — Anatomical Structures Affected

- **Primary target cell:** monocytes and macrophages (CL:0000576, CL:0000235).
- **Primary organs / body systems (lymphoreticular / hematopoietic):**
  - Lymph nodes — generalized, postauricular, cervical lymphadenopathy (UBERON:0000029, lymph node)
  - Spleen — splenomegaly (UBERON:0002106)
  - Liver — hepatomegaly (UBERON:0002107)
  - Bone marrow / blood — hematologic abnormalities (UBERON:0002371 / UBERON:0000178)
- **Body systems:** hematopoietic/immune (lymphoreticular) system; hepatobiliary involvement (hepatomegaly).
- **Tissue/cell level:** mononuclear phagocyte lineage; reactive lymphocytes in peripheral blood.
- **Subcellular level:** the pathogen resides in a **membrane-bound cytoplasmic vacuole/phagosome** (GO:0005768 endosome / GO:0045335 phagocytic vesicle); it up-regulates surface **transferrin receptor** and co-opts endosomal iron trafficking (GO:0005905 clathrin-coated pit; GO:0055037 recycling endosome).
- **Lateralization:** not applicable — systemic/bilateral lymphoreticular involvement.

---

## Section 8 — Temporal Development

- **Onset:** **Acute**, following an incubation of roughly **~2 weeks** after ingestion of contaminated raw fish. Any age with dietary exposure; adult-predominant.
- **Course:** **Self-limited, acute**. Described as an acute, self-limiting mononucleosis-like illness that responds rapidly to tetracyclines ([PMID: 10756846](https://pubmed.ncbi.nlm.nih.gov/10756846/); [PMID: 16786789](https://pubmed.ncbi.nlm.nih.gov/16786789/)).
- **Progression rate:** Rapid onset, then resolution over days to a few weeks; antibiotics accelerate defervescence.
- **Disease pattern:** Monophasic/self-limited; **no documented relapsing-remitting course and no chronic human carriage**.
- **Remission:** Spontaneous or treatment-induced.
- **Critical period:** The acute febrile phase is the window for antibiotic intervention; early doxycycline shortens illness.

---

## Section 9 — Inheritance and Population (Epidemiology)

**Inheritance:** **NOT APPLICABLE** — infectious, non-heritable disease. No penetrance/expressivity/anticipation/founder-effect/consanguinity/carrier-frequency parameters apply.

**Epidemiology.** Sennetsu fever is **rare and under-recognized but with high subclinical seroprevalence** in parts of Southeast Asia:

| Population / setting | Metric | Value | Source |
|---|---|---|---|
| Global, ~50 years | Recognized cases | < 100 | [PMID: 26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/) |
| Laos (donors/febrile/hepatitis/jaundice, N=1,132) | IgG seroprevalence | ~17% | [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/) |
| Thailand (febrile, N=848) | IgG seroprevalence | 4% | [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/) |
| Malaysia (febrile) | IgG seroprevalence | 0% | [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/) |
| Laos febrile inpatients | Acute PCR-confirmed | 4/1,637 (0.2%) | [PMID: 26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/) |
| Thailand febrile patients (N=2,225) | Seroprevalence / acute infection | 0.2% / 0.1% | [PMID: 27139448](https://pubmed.ncbi.nlm.nih.gov/27139448/) |

Direct quote: Lao patients "had a high prevalence (17%) of immunofluorescence assay IgG anti–*N. sennetsu* antibodies compared with 4% and 0% from febrile patients (N = 848) in Thailand and Malaysia, respectively" ([PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/)). The **discordance between ~17% seroprevalence and 0.2% acute hospitalized infection** strongly implies most infections are mild/subclinical and self-resolving.

**Geographic distribution:** Historically western/southern Japan ("Hyuga fever," first described 1950s — [PMID: 6425420](https://pubmed.ncbi.nlm.nih.gov/6425420/)); more recently Laos, Thailand, Malaysia. **Sex ratio / age distribution:** determined by dietary exposure to raw fish rather than by host biology; no strong intrinsic sex predilection documented.

---

## Section 10 — Diagnostics

**Serology (mainstay):** Indirect fluorescent antibody (IFA) using cultured *E./N. sennetsu* antigen detects anti–*N. sennetsu* IgG/IgM: "The antigen derived from our *E. sennetsu* cultures was used to develop an indirect fluorescent antibody test for detection and titration of serum antibodies to the organism" ([PMID: 2985504](https://pubmed.ncbi.nlm.nih.gov/2985504/)).

**Molecular (confirmatory):** PCR amplification and sequencing of **16S rRNA** and species-specific genes. In Laos, "A buffy coat from 1 of 91 patients with undifferentiated fever was positive by 16S rRNA amplification and sequencing and real-time polymerase chain reactions (PCR) targeting two *N. sennetsu* genes" ([PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/)). A **PCR-RFLP** approach differentiates *N. sennetsu* from *E. chaffeensis* and *A. phagocytophilum*; the **gltA (citrate synthase)** gene with RcaI RFLP identifies the Neorickettsia genogroup ([PMID: 11526124](https://pubmed.ncbi.nlm.nih.gov/11526124/)); a 23S rRNA qPCR also detects *N. sennetsu* ([PMID: 25748051](https://pubmed.ncbi.nlm.nih.gov/25748051/)); species-specific **p51/P51** supports differentiation among Neorickettsia species ([PMID: 15297539](https://pubmed.ncbi.nlm.nih.gov/15297539/)).

**Microscopy:** Giemsa-stained blood/tissue may reveal **intracytoplasmic morulae in monocytes** ([PMID: 6274798](https://pubmed.ncbi.nlm.nih.gov/6274798/); [PMID: 16786789](https://pubmed.ncbi.nlm.nih.gov/16786789/)).

**Culture:** Isolation in monocyte/macrophage cell lines (e.g., canine DH82; murine P388D1/RAW 264; human/canine primary monocytes).

**Caveat — cross-reactivity:** Convalescent sera from Sennetsu patients react with ***Ehrlichia canis*** antigen ("convalescent sera from patients with sennetsu fever reacted with *Ehrlichia canis* antigen"; direct FA staining of *E. canis* morulae by patient immunoglobulins), which can aid or confound serodiagnosis ([PMID: 7034563](https://pubmed.ncbi.nlm.nih.gov/7034563/)).

**Clinical criteria / differential diagnosis:** Consider in a patient with acute fever, lymphadenopathy, hepatosplenomegaly, and atypical lymphocytosis **plus a raw-fish exposure history** in an endemic area. Differential includes: EBV/CMV infectious mononucleosis, other ehrlichioses/anaplasmosis, scrub typhus (*Orientia tsutsugamushi*), murine and epidemic typhus, dengue, acute viral hepatitis, leptospirosis, and toxoplasmosis. **Genetic testing / newborn screening: NOT APPLICABLE.**

---

## Section 11 — Outcome / Prognosis

**Prognosis is favorable.** Sennetsu fever is an acute, self-limiting mononucleosis-like illness that responds rapidly to tetracyclines ([PMID: 10756846](https://pubmed.ncbi.nlm.nih.gov/10756846/); [PMID: 16786789](https://pubmed.ncbi.nlm.nih.gov/16786789/)). Walker framed it as "a potentially prevalent, treatable, acutely incapacitating tropical infectious disease" — emphasizing **morbidity (incapacitation) over mortality** ([PMID: 19635866](https://pubmed.ncbi.nlm.nih.gov/19635866/)). With fewer than 100 recognized cases over 50 years and a high subclinical seroprevalence versus rare hospitalization, **most infections are mild/self-resolving** ([PMID: 26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/); [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/)).

- **Mortality:** Very low; deaths are rarely if ever reported — in contrast to *E. chaffeensis* (human monocytic ehrlichiosis), which can be fatal.
- **Recovery:** Complete recovery is expected; no documented chronic carriage or long-term disability.
- **Complications:** Uncommon; potential for more severe/prolonged course in immunosuppressed hosts (analogous to enhanced bacterial growth under immunosuppression in the mouse model, [PMID: 1165122](https://pubmed.ncbi.nlm.nih.gov/1165122/)).
- **Prognostic factors:** Host immune competence (cell-mediated immunity) and timeliness of antibiotic therapy.

---

## Section 12 — Treatment

**First-line pharmacotherapy — tetracyclines.** "The specific treatment consists in tetracycline administration (doxycycline, minocycline) for up to seven days" ([PMID: 10756846](https://pubmed.ncbi.nlm.nih.gov/10756846/)). **Doxycycline is the drug of choice** for the human ehrlichioses/anaplasmoses generally ([PMID: 20077398](https://pubmed.ncbi.nlm.nih.gov/20077398/)). Tetracyclines act by inhibiting bacterial protein synthesis; the pharmacodynamic link to pathogenesis is illustrated by oxytetracycline reversing the infection-driven host TfR mRNA up-regulation ([PMID: 10225882](https://pubmed.ncbi.nlm.nih.gov/10225882/)).

| Drug (NCIT) | Class | Role | Evidence |
|---|---|---|---|
| Doxycycline (NCIT:C692) | Tetracycline | First-line | [PMID: 10756846], [PMID: 20077398] |
| Minocycline (NCIT:C61815) | Tetracycline | Alternative | [PMID: 10756846] |
| Tetracycline (NCIT:C844) | Tetracycline | Effective | [PMID: 10756846] |
| Oxytetracycline | Tetracycline | Effective in vitro/experimental | [PMID: 10225882] |
| Fluoroquinolones | DNA gyrase inhibitor | Naturally susceptible (GyrA Ser83), not first-line | [PMID: 11408229] |

**Notable pharmacology — natural fluoroquinolone susceptibility.** Unlike fluoroquinolone-resistant *Ehrlichia* (e.g., *E. chaffeensis*, *E. canis*), *N. sennetsu* retains a **serine at GyrA position 83** (the susceptible genotype): "A serine residue in position 83 (*Escherichia coli* numbering) in the susceptible species is replaced by an alanine residue in fluoroquinolone-resistant species" ([PMID: 11408229](https://pubmed.ncbi.nlm.nih.gov/11408229/)). This gives a theoretical second-line option, though tetracyclines remain standard.

**Ineffective agents:** Penicillins and sulfonamides are ineffective against this genogroup (demonstrated for a closely related mouse ehrlichial isolate — [PMID: 8380184](https://pubmed.ncbi.nlm.nih.gov/8380184/)).

**Supportive care:** Antipyretics, fluids, rest during the acute phase. **Advanced therapeutics (gene/cell/RNA/immunotherapy), surgery, pharmacogenomics: NOT APPLICABLE.**

---

## Section 13 — Prevention

- **Primary prevention (dominant lever):** **Avoid eating raw/undercooked fish** in endemic areas; adequately cook fish to kill fluke metacercariae. Public-health education on food preparation, and improved fish-farming/sanitation to reduce fluke burdens (inferred from the fish-borne, fluke-associated transmission model — [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/); [PMID: 26873314](https://pubmed.ncbi.nlm.nih.gov/26873314/)).
- **Secondary prevention:** Early clinical recognition and prompt doxycycline in febrile patients with compatible exposure; awareness among clinicians in endemic regions given under-recognition ([PMID: 26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/)).
- **Immunization:** **No vaccine exists.**
- **Prophylaxis / chemoprophylaxis:** None established.
- **Genetic counseling / carrier screening: NOT APPLICABLE.**

---

## Section 14 — Other Species / Natural Disease

- **Agent taxonomy:** *Neorickettsia sennetsu* (NCBI Taxonomy). Closely related to *Neorickettsia risticii* (agent of **Potomac horse fever**) and *Neorickettsia helminthoeca* (agent of **salmon poisoning disease** in dogs).
- **Fluke reservoirs (Digenea):** *Stellantchasmus falcatus* (source of the "SF agent," [PMID: 7311106](https://pubmed.ncbi.nlm.nih.gov/7311106/)); *Plagiorchis elegans* ([PMID: 26873314](https://pubmed.ncbi.nlm.nih.gov/26873314/)); *Fasciola hepatica* harbors the closely related endobacterium nFh ([PMID: 28060841](https://pubmed.ncbi.nlm.nih.gov/28060841/)).
- **Fish hosts:** *Anabas testudineus* (climbing perch, Laos — [PMID: 19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/)); *Mugil cephalus* (grey mullet, historic — [PMID: 7311106](https://pubmed.ncbi.nlm.nih.gov/7311106/)); an *E. sennetsu*-genogroup agent was detected in rainbow trout (*Oncorhynchus mykiss*) and their fluke parasites ([PMID: 10962157](https://pubmed.ncbi.nlm.nih.gov/10962157/)).
- **Comparative pathology:** The Neorickettsia genogroup causes analogous monocytotropic disease across mammals — Potomac horse fever in horses (fever, leukopenia, ~30% fatal — [PMID: 3880925](https://pubmed.ncbi.nlm.nih.gov/3880925/)) and salmon poisoning disease in dogs — sharing macrophage tropism, morula formation, and fluke-borne transmission.
- **Zoonotic potential:** Yes — a fish/fluke-borne zoonosis; cross-species serologic relatedness (e.g., with *E. canis*, [PMID: 7034563](https://pubmed.ncbi.nlm.nih.gov/7034563/)).

---

## Section 15 — Model Organisms

| Model | Type | Findings | Evidence |
|---|---|---|---|
| Mouse (lab) | Mammalian in vivo | Multiplies in spleen/peritoneal macrophages; cyclophosphamide immunosuppression enhances splenic titers >100-fold (to ~10^8.5 MLD) | [PMID: 1165122](https://pubmed.ncbi.nlm.nih.gov/1165122/) |
| Human monocyte cultures | In vitro | Growth cycle resembling *E. canis*; morulae; mouse-infectious | [PMID: 6274798](https://pubmed.ncbi.nlm.nih.gov/6274798/) |
| Non-human primate (monkey) | Mammalian in vivo | Reproduced infectious mononucleosis clinically and pathologically | [PMID: 14322603](https://pubmed.ncbi.nlm.nih.gov/14322603/); [PMID: 14319489](https://pubmed.ncbi.nlm.nih.gov/14319489/) |
| Dog | Mammalian in vivo | Culture-adapted *E. sennetsu* infected dogs; seroconversion, reisolation; no overt disease | [PMID: 2985504](https://pubmed.ncbi.nlm.nih.gov/2985504/) |
| Murine macrophage lines P388D1, RAW 264 | Cell line | Continuous propagation | [PMID: 4025693](https://pubmed.ncbi.nlm.nih.gov/4025693/) |
| Canine macrophage line DH82 | Cell line | Propagation/isolation | [PMID: 26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/) |

**Phenotype recapitulation:** The **non-human primate model faithfully reproduces the human mononucleosis-like disease**; the **mouse model** reproduces macrophage/splenic infection and demonstrates the central role of host immunity in control (via the cyclophosphamide experiment). **Limitations:** rodent models do not fully replicate the human clinical syndrome, and no genetically engineered (knockout/transgenic) model is applicable since this is an infectious, non-genetic disease. Reference strain: **ATCC VR-367 (Miyayama)**.

---

## Mechanistic Model / Interpretation

```
   Raw/undercooked fish with fluke metacercariae  (dietary exposure)
                       |  ingested (transmission INFERRED)
                       v
        N. sennetsu released -> uptake by MONOCYTES / MACROPHAGES
                       |
                       v
     Resides in membrane-bound vacuole -> INHIBITS phagosome-lysosome fusion
                       |                         (evades killing)
                       v
     Disables host "alarm"/microbicidal systems  --> SAFE HAVEN
                       |
                       v
     Activates IRP1 -> up Transferrin Receptor mRNA -> up iron import
                       |  (blocked by deferoxamine; reversed by tetracycline)
                       v
     Binary fission -> MORULAE (intracytoplasmic microcolonies)
                       |
          +------------+-------------+
          v                          v
  Dissemination to spleen/       Reactive lymphocyte
  liver/lymph nodes              proliferation
  -> hepatosplenomegaly,         -> ATYPICAL LYMPHOCYTOSIS
     lymphadenopathy                (mononucleosis-like)
          |                          |
          +------------+-------------+
                       v
        Systemic inflammatory/cytokine response
        -> FEVER, chills, headache, malaise, myalgia
        (+/- leukopenia, thrombocytopenia)
                       |
                       v
     Host cell-mediated immunity controls infection
     -> SELF-LIMITED RESOLUTION (accelerated by doxycycline)
     [immunosuppression removes this brake -> enhanced growth]
```

The pathophysiology is a coherent story of **intracellular immune evasion coupled to host iron piracy**. The **upstream** lesion is macrophage infection and phagosome-maturation arrest; the **central** engine is IRP1-driven transferrin-receptor up-regulation supplying iron for replication; the **downstream** manifestation is lymphoreticular activation producing the mononucleosis-like syndrome. Two therapeutically important nodes are directly demonstrated: (i) **iron dependence** (deferoxamine blocks growth) and (ii) **protein-synthesis dependence** (tetracyclines both cure the disease and reverse the TfR manipulation). Host **cell-mediated immunity** is the natural terminator of infection, explaining both the self-limited course and the enhanced disease seen under immunosuppression.

---

## Evidence Base

| PMID | Contribution | Role |
|---|---|---|
| [20833807](https://pubmed.ncbi.nlm.nih.gov/20833807/) | Agent = obligate intracellular bacterium of monocytes/macrophages; P51 porin | Supports F001, F011 |
| [11760958](https://pubmed.ncbi.nlm.nih.gov/11760958/) | Reclassification into genus *Neorickettsia* (16S) | Supports taxonomy |
| [19635868](https://pubmed.ncbi.nlm.nih.gov/19635868/) | Fish PCR positivity; 17% Lao seroprevalence; PCR diagnosis | Supports F002, F005, F010 |
| [26873314](https://pubmed.ncbi.nlm.nih.gov/26873314/) | Flukes as endosymbiont reservoir/vector | Supports F002 |
| [28060841](https://pubmed.ncbi.nlm.nih.gov/28060841/) | *F. hepatica* endobacterium related to Sennetsu agent; fluke tissue localization | Supports transmission model |
| [10225882](https://pubmed.ncbi.nlm.nih.gov/10225882/) | TfR up-regulation via IRP1; iron dependence; tetracycline reversal | Supports F004, mechanism |
| [1884777](https://pubmed.ncbi.nlm.nih.gov/1884777/) | Phagosomal replication, own ATP metabolism | Supports F011 |
| [12860688](https://pubmed.ncbi.nlm.nih.gov/12860688/) | "Safe haven" immune-evasion strategy | Supports F011 |
| [9511829](https://pubmed.ncbi.nlm.nih.gov/9511829/) | Ultrastructure; small non-fusing vacuoles for Sennetsu genogroup | Supports morphology |
| [1165122](https://pubmed.ncbi.nlm.nih.gov/1165122/) | Mouse model; cyclophosphamide enhancement; mononucleosis of western Japan | Supports F007, F009 |
| [1889044](https://pubmed.ncbi.nlm.nih.gov/1889044/) | Monocyte/granulocyte tropism -> lymphadenopathy, hematologic changes | Supports F007 |
| [6425420](https://pubmed.ncbi.nlm.nih.gov/6425420/) | Historical southern-Japan mononucleosis-like disease | Supports F008 |
| [7311106](https://pubmed.ncbi.nlm.nih.gov/7311106/) | Raw grey mullet; SF fluke agent | Supports F008 |
| [26158273](https://pubmed.ncbi.nlm.nih.gov/26158273/) | <100 global cases; 0.2% acute Lao inpatients; DH82 | Supports F005, F012 |
| [27139448](https://pubmed.ncbi.nlm.nih.gov/27139448/) | Thailand seroprevalence 0.2% / acute 0.1% | Supports F005 |
| [10756846](https://pubmed.ncbi.nlm.nih.gov/10756846/) | Tetracyclines = specific treatment | Supports F006, F012 |
| [20077398](https://pubmed.ncbi.nlm.nih.gov/20077398/) | Doxycycline drug of choice; morula biology | Supports F006 |
| [11408229](https://pubmed.ncbi.nlm.nih.gov/11408229/) | GyrA Ser83 natural fluoroquinolone susceptibility | Supports F006 |
| [2985504](https://pubmed.ncbi.nlm.nih.gov/2985504/) | IFA serodiagnosis; canine model | Supports F009, F010 |
| [7034563](https://pubmed.ncbi.nlm.nih.gov/7034563/) | Serologic cross-reactivity with *E. canis* | Supports F010 caveat |
| [19661282](https://pubmed.ncbi.nlm.nih.gov/19661282/) | 88.2% gene conservation with *N. risticii*; T4SS | Supports F003 |
| [16482227](https://pubmed.ncbi.nlm.nih.gov/16482227/) | Biosynthetic capacity; comparative genomics | Supports F003 |
| [10418133](https://pubmed.ncbi.nlm.nih.gov/10418133/) / [10765728](https://pubmed.ncbi.nlm.nih.gov/10765728/) | Genome size ~878-881 kb (PFGE) | Supports F003 |
| [14322603](https://pubmed.ncbi.nlm.nih.gov/14322603/) / [14319489](https://pubmed.ncbi.nlm.nih.gov/14319489/) | Monkey model reproduces mononucleosis | Supports F009 |
| [4025693](https://pubmed.ncbi.nlm.nih.gov/4025693/) | Murine macrophage cell-line propagation | Supports F009 |
| [15297539](https://pubmed.ncbi.nlm.nih.gov/15297539/) | p51/P51-based species differentiation | Supports F010 |
| [11526124](https://pubmed.ncbi.nlm.nih.gov/11526124/) | gltA RFLP identifies Neorickettsia genogroup | Supports F010 |
| [3880925](https://pubmed.ncbi.nlm.nih.gov/3880925/) | Potomac horse fever comparative disease | Supports Section 14 |
| [10962157](https://pubmed.ncbi.nlm.nih.gov/10962157/) | *E. sennetsu*-genogroup agent in trout/flukes | Supports Section 14 |

---

## Limitations and Knowledge Gaps

1. **Small evidence base.** Fewer than 100 recognized cases over 50 years means clinical descriptions rest on old case series and experimental (animal/cell-culture) work rather than large modern cohorts; frequencies of individual symptoms are qualitative, not precisely quantified.
2. **Transmission not directly proven.** Fish-to-human transmission is *inferred* from fish PCR positivity, seroprevalence patterns, and the fluke-endosymbiont biology; a completed experimental fish→human transmission chain has not been demonstrated, and the exact fish species/fluke species responsible in each endemic focus remain incompletely mapped.
3. **Human pathophysiology extrapolated.** Much of the mechanistic detail (phagosome–lysosome fusion inhibition, IRP1/TfR iron piracy, "safe haven") derives from in vitro cell lines and related Anaplasmataceae; direct human tissue data are limited.
4. **No modern omics on human disease.** No human transcriptomic/proteomic/metabolomic profiling of Sennetsu fever patients exists; molecular profiling is confined to the pathogen genome.
5. **Epidemiology geographically narrow.** Robust seroprevalence data exist mainly for Laos, Thailand, Malaysia and historic Japan; true global distribution, incidence, sex/age structure, and burden are unknown.
6. **Prognosis inferred, not registry-derived.** The "low mortality / self-limited" conclusion follows from rarity of reported severe outcomes and the seroprevalence–hospitalization gap rather than from prospective outcome cohorts.
7. **Not applicable sections.** Human genetics, inheritance, gene therapy, pharmacogenomics, newborn/carrier screening, and oncologic staging are genuinely not applicable to this infectious disease and are marked as such.

---

## Proposed Follow-up Experiments / Actions

1. **Complete the transmission chain experimentally:** feed *N. sennetsu*-positive metacercariae-bearing fish to a permissive animal model (e.g., non-human primate or dog) with molecular tracking to formally prove fish→vertebrate transmission and identify the responsible fluke/fish species per endemic focus.
2. **Prospective clinical cohort with modern diagnostics:** enroll febrile patients in Laos/Thailand with paired IFA serology + multiplex PCR (16S, gltA, p51) to quantify true incidence, symptom frequencies, severity distribution, and outcomes.
3. **Host-response omics:** perform RNA-seq/proteomics on infected human monocytes/macrophages (and patient blood where available) to map the cytokine and iron-metabolism pathways beyond IRP1/TfR.
4. **Mechanistic dissection of iron piracy:** test whether iron-chelation adjuncts (e.g., deferoxamine) potentiate tetracycline killing in vitro and in the mouse model, and characterize the T4SS effectors mediating phagosome-maturation arrest.
5. **Food-safety intervention study:** evaluate community education on cooking fish and improved aquaculture sanitation as primary prevention, using seroincidence as an endpoint.
6. **Fluoroquinolone confirmation:** empirically validate in vitro fluoroquinolone efficacy against *N. sennetsu* (predicted from GyrA Ser83) as a potential alternative for tetracycline-intolerant patients.

---

*Report compiled from 52 reviewed papers and 12 confirmed findings across a 5-iteration autonomous investigation. Evidence types span human clinical/seroepidemiological studies, model-organism (mouse, non-human primate, dog) experiments, in vitro cell-culture work, and comparative/genomic analyses.*


## Artifacts

- [OpenScientist final report](Sennetsu_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Sennetsu_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 14 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 36 |
| On topic | 24 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:19635866`: "acutely incapacitating"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 25 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0030260` (1 mention) - the report calls it "entry into host cell"; GO calls it **GO_0030260**
- `NCIT:C692` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Nimodipine**
- `NCIT:C61815` (1 mention) - the report calls it "Minocycline"; NCIT calls it **Loracarbef Anhydrous**
- `NCIT:C844` (1 mention) - the report calls it "Tetracycline"; NCIT calls it **Streptonigrin**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030260` (GO_0030260) (1 mention) - replaced by `GO:0044409`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `GO:0051673` (1 mention) - the report calls it "disruption of host cell"; GO calls it **disruption of plasma membrane integrity in another organism**, and lists "disruption by virus of host cell membrane" among its other names
- `CL:0000842` (1 mention) - the report calls it "mononuclear cell"; CL calls it **mononuclear leukocyte**, and lists "mononuclear cell" among its other names
- `UBERON:0002106` (1 mention) - the report calls it "Spleen — splenomegaly"; UBERON calls it **spleen**
- `UBERON:0002107` (1 mention) - the report calls it "Liver — hepatomegaly"; UBERON calls it **liver**