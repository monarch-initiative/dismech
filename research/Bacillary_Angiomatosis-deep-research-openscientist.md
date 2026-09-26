---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-26T00:40:20.279526'
end_time: '2026-09-26T00:51:30.616541'
duration_seconds: 670.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bacillary Angiomatosis
  mondo_id: MONDO:0000758
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
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 35
  on_topic: 33
  validator_version: 0.3.0rc2
term_validation:
  total_terms: 56
  verified: 55
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Symptom
    ontology_label: Fever
  - term_id: HP:0002716
    reported_labels:
    - Sign
    ontology_label: Lymphadenopathy
  - term_id: HP:0001744
    reported_labels:
    - Sign
    ontology_label: Splenomegaly
  - term_id: HP:0001903
    reported_labels:
    - Lab
    ontology_label: Anemia
  - term_id: HP:0001873
    reported_labels:
    - Lab
    ontology_label: Thrombocytopenia
  labels_variant: 3
  obsolete_terms:
  - term_id: NCIT:C29408
    ontology_label: RV-B7 (RECOMB VACCINIA/B7)
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Bacillary_Angiomatosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Bacillary_Angiomatosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bacillary Angiomatosis
- **MONDO ID:** MONDO:0000758 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Bacillary Angiomatosis** covering all of the
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

# Bacillary Angiomatosis — Comprehensive Disease Characterization Report

**Disease:** Bacillary Angiomatosis (BA)
**MONDO:** MONDO:0000758 · **Category:** Infectious disease (bacterial, vasoproliferative)
**Report basis:** Aggregated disease-level evidence from peer-reviewed literature (reviews, landmark case-control study, mechanistic in vitro/in vivo studies). No individual-patient/EHR dataset was provided; findings are synthesized from PubMed primary literature. Evidence types are flagged as *human clinical*, *in vitro*, or *model organism*.

---

## Summary (Answer to the Research Question)

Bacillary angiomatosis is an angioproliferative (vascular tumor–forming) infectious disease caused by the Gram-negative bacteria *Bartonella henselae* and *Bartonella quintana*, occurring almost exclusively in immunocompromised hosts—most classically advanced HIV/AIDS (CD4 typically <100 cells/µL) and also solid-organ transplant recipients—and only rarely in immunocompetent individuals. The bacteria hijack vascular endothelium: the secreted autotransporter **BafA** acts as a VEGF-receptor-2 agonist, the trimeric autotransporter adhesin **BadA** activates HIF-1 to drive proangiogenic reprogramming, and the **VirB/D4 type IV secretion system** injects **Bep effectors** that inhibit endothelial apoptosis—together producing lobular capillary proliferations in skin and viscera. It is diagnosed by biopsy (Warthin-Starry silver stain, PCR) and is highly curable with prolonged antibiotics (erythromycin or doxycycline), but disseminated untreated disease can be fatal. It is **not a genetic disease**; there are no causal human genes, and host immunosuppression plus species-specific exposures (cats/cat fleas for *B. henselae*; homelessness, alcoholism, body lice for *B. quintana*) are the key determinants.

---

## 1. Disease Information

**Overview.** BA is a rare, treatable, vasoproliferative bacterial infection characterized by tumor-like proliferations of small blood vessels in skin, subcutaneous tissue, and internal organs. First recognized in the HIV/AIDS epidemic of the 1980s, it is caused by chronic infection with *Bartonella henselae* or *B. quintana* (formerly genus *Rochalimaea*) (PMID 21285862, PMID 8335458).

**Key identifiers.**
- **MONDO:** MONDO:0000758
- **MeSH:** Angiomatosis, Bacillary (D016917)
- **ICD-10:** A44.8 (Other forms of bartonellosis); **ICD-11:** 1C30.Y (Other specified bartonellosis)
- **OMIM / Orphanet:** Not a Mendelian disease → no OMIM gene entry; not a classic Orphanet rare-genetic entry (infectious etiology)
- **SNOMED CT:** Bacillary angiomatosis (disorder)

**Synonyms / alternative names:** Bacillary angiomatosis-peliosis (when visceral peliosis coexists); epithelioid angiomatosis; bacillary epithelioid angiomatosis; (historically) *Rochalimaea* angiomatosis. Bacillary peliosis (hepatis/splenic) is the visceral counterpart.

**Information source.** Disease-level aggregated resources and primary literature (case series, one landmark molecular case-control study, mechanistic studies), not individual EHR data.

---

## 2. Etiology

**Causal factors — infectious (not genetic).** BA is caused by two Gram-negative bacilli: *Bartonella henselae* (NCBI:txid38323) and *Bartonella quintana* (NCBI:txid803). *"Bacillary angiomatosis is an infectious disease caused by 2 gram-negative bacilli, Bartonella henselae and Bartonella quintana"* (PMID 21285862). A permissive host state (immunosuppression) determines progression from infection to vasoproliferation: *"The severity of Bartonella infection correlates with the patient's immune status"* (PMID 24933445).

**Risk factors (environmental / host).**
- **Immunosuppression (dominant):** advanced HIV/AIDS (e.g., CD4 47 cells/µL, PMID 27428207), solid-organ transplant recipients (PMID 22316326). Rare in immunocompetent hosts (PMID 21285862, PMID 16495874).
- ***B. henselae* exposures:** cat contact and cat-flea (*Ctenocephalides felis*) exposure (P≤0.004) (PMID 9407154, PMID 9272384).
- ***B. quintana* exposures:** low income (P=0.003), homelessness (P=0.004), body-louse exposure (P=0.03) (PMID 9407154); chronic alcoholism (PMID 7529895).
- **Genetic risk factors:** None known. **Not applicable** — no susceptibility loci, causal variants, or modifier genes are established for the human host.

**Protective factors.** Immune competence / immune reconstitution (antiretroviral therapy in HIV) reduces risk and aids cure; ectoparasite control (cat flea control, delousing/hygiene) reduces exposure. No genetic protective variants are described.

**Gene–environment interactions.** Not applicable in the classical (human-genetic) sense; the operative interaction is **host immune status × pathogen exposure** (e.g., cat/flea or louse contact in an immunosuppressed host).

---

## 3. Phenotypes (with suggested HPO terms and qualitative frequencies)

BA phenotypes are *clinical signs/physical manifestations* (cutaneous vascular lesions), *symptoms* (fever, malaise), and *laboratory abnormalities* (anemia, thrombocytopenia). Onset is adult (tracks the immunosuppressed adult population); severity ranges mild-to-severe; course is progressive if untreated, resolving with therapy.

| Phenotype | Type | Suggested HPO | Frequency/notes |
|---|---|---|---|
| Cutaneous/subcutaneous vascular papules & nodules (red-violaceous, friable, bleed when traumatized) | Physical sign | HP:0200039 (Papule); HP:0000988 (Skin nodule); HP:0011276 (Vascular skin abnormality) | Most common; hallmark manifestation (PMID 21285862, PMID 11362939) |
| Fever | Symptom | HP:0001945 | Frequent, esp. systemic disease (PMID 10718405) |
| Lymphadenopathy | Sign | HP:0002716 | Common (PMID 22316326) |
| Hepatomegaly / peliosis hepatis | Sign/organ | HP:0002240; HP:0410042 (Hepatic peliosis) | *B. henselae* (PMID 9407154) |
| Splenomegaly / splenic peliosis | Sign | HP:0001744 | Visceral disease (PMID 22316326) |
| Lytic bone lesions / bone pain | Sign | HP:0002754 (Osteomyelitis)/HP:0002653; HP:0002917 | *B. quintana*, long bones (PMID 9407154, PMID 11362939) |
| Weight loss / anorexia / malaise | Symptom | HP:0001824; HP:0002039 | Systemic disease (PMID 10718405) |
| Anemia | Lab | HP:0001903 | Severe cases (PMID 18098054) |
| Thrombocytopenia | Lab | HP:0001873 | *B. quintana* bacteremia (PMID 9895398) |
| GI involvement (hematemesis, mucosal nodules) | Sign | HP:0002248; HP:0025314 | Rare (PMID 12894361) |
| Oral cavity lesions | Sign | HP:0000155 (Oral mucosa abnormality) | Rare (PMID 28902296, PMID 10718405) |
| Panserositis (pleuritis/pericarditis/peritonitis) | Sign | HP:0032261/HP:0001698 | Rare severe (PMID 18098054) |

**Quality-of-life impact:** Painful/disfiguring skin lesions, bleeding, and systemic constitutional symptoms impair function; visceral disease can be life-threatening. No formal EQ-5D/SF-36 data exist for BA specifically; QoL burden is inferred from lesion morbidity and treatable nature.

---

## 4. Genetic / Molecular Information

**Not applicable to the human host — BA is a bacterial infection, not an inherited disorder.** There are **no causal human genes, pathogenic germline/somatic variants, ClinVar entries, allele frequencies, modifier genes, epigenetic disease signatures, or chromosomal abnormalities**.

The relevant "molecular" players are **bacterial virulence genes** (host-microbe interaction):
- ***bafA*** — proangiogenic autotransporter; passenger domain functions as a VEGF analog (PMID 32678094); homologs in *B. quintana*, *B. bacilliformis*, *B. elizabethae* (PMID 35379004, PMID 36810719).
- ***badA*** (Bartonella adhesin A) — trimeric autotransporter adhesin; head domain mediates host adhesion and HIF-1 activation (PMID 18627378, PMID 21557057).
- ***virB/virD4*** T4SS and **Bep** effector genes — translocation of effectors inhibiting apoptosis and driving proangiogenic phenotype (PMID 23163798).
- *B. quintana* Vomps (variably expressed outer-membrane proteins) and Trw conjugation system for erythrocyte adherence (PMID 21557057).

---

## 5. Environmental Information

- **Infectious agents (causal):** *Bartonella henselae* and *Bartonella quintana* (Alphaproteobacteria; family Bartonellaceae). *B. henselae* also causes cat scratch disease and peliosis hepatis; *B. quintana* also causes trench fever and endocarditis (PMID 18444576, PMID 24933445). A rare BA case from *B. elizabethae* has been reported (PMID 36810719).
- **Vectors/reservoirs:** *B. henselae* — reservoir cats, vector cat flea *Ctenocephalides felis*; *B. quintana* — reservoir humans, vector body louse *Pediculus humanus corporis* (PMID 9272384).
- **Lifestyle factors:** homelessness, poverty, chronic alcoholism (for *B. quintana*); cat ownership/exposure (for *B. henselae*) (PMID 9407154, PMID 7529895).
- **Toxins/radiation/occupational exposures:** Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating infection → clinical lesion)

1. **Exposure/inoculation** — a cat scratch/flea (B. henselae) or body louse (B. quintana) **introduces** Bartonella into skin/blood of a (usually immunocompromised) host. *(human clinical/epidemiologic; PMID 9407154)*
2. **Bacterial adhesion** — the trimeric autotransporter adhesin **BadA binds** fibronectin/ECM and endothelial cells, **leading to** autoagglutination and firm attachment. *(in vitro; PMID 18627378, PMID 21557057)*
3. **Proangiogenic reprogramming (branch A)** — BadA engagement **activates HIF-1**, which **results in** transcription of angiogenic genes and **autocrine VEGF secretion** by endothelial cells. *(in vitro; PMID 18627378, PMID 23163798)*
4. **VEGFR-2 mitogenic signaling (branch B)** — the secreted autotransporter **BafA binds VEGF receptor-2** and **activates** its downstream pathway (functioning as a VEGF analog), **driving** endothelial proliferation, tube formation, and microvessel sprouting. *(in vitro + mouse; PMID 32678094)*
5. **Anti-apoptotic survival (branch C)** — the **VirB/D4 T4SS translocates Bep effectors** into endothelial cytoplasm, **causing** invasome-mediated uptake of bacterial aggregates and **inhibiting apoptosis**, so proliferating endothelium survives. *(in vitro; PMID 23163798)*
6. **Stromal amplification** — infected **pericytes** increase VEGF with reduced coverage (PMID 23184416), and persistence in **mesenchymal stromal cells** further **amplifies** endothelial activation/angiogenesis (PMID 34031126). *(in vitro)*
7. **Lesion formation** — combined proliferation + survival + inflammation **produces** a lobular capillary proliferation lined by plump epithelioid endothelial cells with neutrophilic infiltrate and stromal bacterial aggregates — the histologic **bacillary angioma**. *(human clinical; PMID 24718378)*
8. **Dissemination** — because host immunity is impaired, lesions **spread** hematogenously to viscera (liver/spleen peliosis, bone, GI tract, CNS), which **can lead to** organ dysfunction, hemorrhage, and death if untreated. *(human clinical; PMID 11362939, PMID 24933445)*

**Upstream vs downstream:** Adhesion (BadA) and effector delivery (VirB/D4) are upstream; VEGF/VEGFR-2 signaling, HIF-1 activation, and apoptosis inhibition are the core intermediate nodes; endothelial proliferation → lesion formation → dissemination are downstream.

**Molecular pathways:** VEGF/VEGFR-2 signaling, HIF-1α transcriptional program, NF-κB–associated proangiogenic/anti-apoptotic signaling. **KEGG/Reactome:** VEGF signaling pathway; HIF-1 signaling pathway.
**Cellular processes:** angiogenesis, endothelial proliferation, inhibition of apoptosis, inflammation.
**Immune involvement:** disease is permitted by **immunodeficiency**; lesions show mixed neutrophilic/lymphocytic infiltrate; in immunocompetent hosts a granulomatous response contains infection (PMID 9784568).
**Suggested GO terms:** angiogenesis (GO:0001525); sprouting angiogenesis (GO:0002040); VEGF receptor signaling pathway (GO:0048010); cellular response to hypoxia (GO:0071456); negative regulation of apoptotic process (GO:0043066); inflammatory response (GO:0006954).
**Suggested CL terms:** endothelial cell (CL:0000115); blood vessel endothelial cell (CL:0000071); pericyte (CL:0000669); mesenchymal stem cell (CL:0000134); erythrocyte (CL:0000232, for B. quintana bacteremia).
**Omics:** No human disease transcriptomic/proteomic/metabolomic BA signatures are established; mechanistic data are protein/pathway-level (VEGF, HIF-1, BafA/BadA/Bep).

---

## 7. Anatomical Structures Affected

- **Primary organ:** skin (UBERON:0002097) and subcutaneous tissue (UBERON:0002072) — cutaneous/subcutaneous vascular nodules.
- **Secondary/visceral organs:** liver (UBERON:0002107; peliosis hepatis), spleen (UBERON:0002106), bone/bone marrow (UBERON:0002481/UBERON:0002371; lytic lesions, long bones), lymph nodes (UBERON:0000029), GI tract (UBERON:0000160; esophagus/stomach/duodenum), oral mucosa (UBERON:0003343), lung (UBERON:0002048), heart/pericardium, CNS/brain (UBERON:0000955) (PMID 11362939, PMID 12894361, PMID 16495874).
- **Body systems:** primarily **cardiovascular/vascular** (endothelium), with **integumentary**, **hepatobiliary**, **skeletal**, **lymphatic/hematologic**, **digestive**, and occasionally **nervous** involvement.
- **Tissue/cell level:** vascular (connective/endothelial) tissue; target cells = **vascular endothelial cells** (CL:0000115), with **pericytes** (CL:0000669) and stromal cells; *B. quintana*/*B. henselae* also infect **erythrocytes** (CL:0000232) causing bacteremia.
- **Subcellular:** bacteria localize extracellularly (stromal aggregates) and are taken up intracellularly via the **invasome**; effectors act in the endothelial **cytoplasm/plasma membrane** (GO:0005886 plasma membrane; GO:0005829 cytosol).
- **Lateralization:** typically multifocal/bilateral and disseminated rather than lateralized; cutaneous lesions are widely distributed.

---

## 8. Temporal Development

- **Onset:** adult-onset (parallels immunosuppressed adults); **subacute/chronic/insidious** course over weeks to months (e.g., 6-month growing lesions, PMID 23282705; 10-month nodule, PMID 9205511).
- **Progression:** **progressive** if untreated, from localized papules to disseminated visceral disease; can be **rapidly life-threatening** with hemorrhage/organ involvement (PMID 12894361, PMID 18098054).
- **Course pattern:** treatment-induced remission is the rule with adequate therapy; **relapse** occurs with inadequate/short courses (PMID 9272384, PMID 9205511).
- **Duration:** not self-limited in immunocompromised hosts (requires antibiotics); may resolve with prolonged therapy and immune reconstitution.
- **Critical intervention window:** early biopsy-based diagnosis and prompt antibiotics prevent dissemination and death; immune restoration (ART) is a key adjunct.

---

## 9. Inheritance and Population

- **Epidemiology:** Rare; no precise population prevalence/incidence figures exist (opportunistic, under-reported). Incidence fell sharply in high-income settings after combination antiretroviral therapy reduced severe HIV immunosuppression; it remains under-recognized in sub-Saharan Africa despite high HIV prevalence (PMID 24718378). *B. quintana* seroprevalence is high in homeless populations (IgG ≥1:128 in 57% and ≥1:1024 in 11% of Tokyo homeless; PMID 16495631); *B. quintana* bacteremia in 14% of Marseille homeless (PMID 9895398).
- **Inheritance:** **Not applicable** (infectious disease; no Mendelian inheritance, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency).
- **Demographics:** predominantly adults with immunosuppression; historically HIV-infected men; *B. quintana* clusters in homeless/alcoholic, low-income urban populations. No strong ethnic predisposition beyond socioeconomic exposure patterns. Sex ratio reflects the underlying at-risk populations rather than intrinsic disease bias.
- **Geographic distribution:** worldwide; *B. quintana* ("urban trench fever") in homeless populations across the US, Europe, and Japan (PMID 11871479, PMID 16495631).

---

## 10. Diagnostics

- **Biopsy/histopathology (gold standard):** lobular proliferation of capillaries lined by plump, epithelioid/spindled endothelial cells; mixed neutrophilic/leukocytoclastic infiltrate; extracellular amphophilic granular material (bacterial aggregates) (PMID 24718378, PMID 12152480). **Warthin-Starry silver stain** highlights clumps of bacilli — *"A Warthin-Starry stain highlighted clumps of bacilli, confirming the diagnosis of BA"* (PMID 24718378). Electron microscopy can visualize bacilli (PMID 11362939).
- **Molecular:** PCR of lesional tissue (e.g., 16S rRNA, citrate synthase *gltA*, riboflavin synthase *ribC*, or a 298-bp Bartonella fragment) identifies and speciates the organism and can **monitor treatment response** (PMID 9205511, PMID 7529895, PMID 40090362).
- **Serology:** indirect immunofluorescence antibody (IFA) for *Bartonella*-specific IgG/IgM; useful epidemiologically but **poorly reliable** for individual BA diagnosis (PMID 9272384, PMID 11362939).
- **Culture:** possible but **difficult/fastidious**, slow-growing; low sensitivity (PMID 9272384).
- **Imaging:** CT/MRI/ultrasound to define visceral (hepatosplenic peliosis, abscesses) and osseous lesions (PMID 27428207, PMID 22316326).
- **Laboratory:** anemia, thrombocytopenia, elevated inflammatory markers may accompany systemic disease.
- **Genetic/omics testing:** **Not applicable** (no human genetic test; no karyotype/CMA/mtDNA/repeat-expansion role).
- **Differential diagnosis:** Kaposi sarcoma (key mimic), pyogenic granuloma, angiosarcoma, epithelioid hemangioma, verruga peruana (*B. bacilliformis*), cat-scratch disease — distinguished by Warthin-Starry-positive bacilli and vascular-proliferative histology (PMID 10718405, PMID 31780437). BA is antibiotic-curable, unlike KS.
- **Screening:** No population screening; consider *B. quintana* testing in symptomatic homeless/alcoholic patients and BA in HIV patients with vascular skin lesions.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** With appropriate prolonged antibiotics, prognosis is **excellent** (lesions resolve). **Untreated Bartonella infection can cause high mortality** (PMID 24933445); disseminated/visceral disease (e.g., GI hemorrhage, panserositis) is potentially fatal (PMID 12894361, PMID 18098054).
- **Morbidity:** disfiguring/painful, friable, bleeding skin lesions; visceral organ dysfunction; bone pain/lytic lesions. No standardized disability/QoL metrics for BA.
- **Disease course/complications:** hemorrhage from friable lesions, airway/oronasal involvement (oronasal fistula, PMID 28902296), massive GI bleeding (PMID 12894361), anemia and multi-serosal involvement (PMID 18098054).
- **Recovery potential:** high with treatment + immune reconstitution; relapse if therapy is too short.
- **Prognostic factors:** degree/duration of immunosuppression (CD4 count), extent of dissemination, timeliness of diagnosis and adequacy/duration of antibiotics. PCR negativity of lesional material is a favorable treatment-response marker (PMID 9205511).

---

## 12. Treatment

- **First-line pharmacotherapy:** **Erythromycin** (macrolide) is first-line for angioproliferative lesions — *"erythromycin is the first-line antibiotic therapy for the treatment of angioproliferative lesions"* (PMID 24933445). **Doxycycline** (tetracycline) is the principal alternative — *"Doxycycline led to complete resolution"* (PMID 28902296). Azithromycin and clarithromycin are also effective (PMID 21285862, PMID 18098054).
- **Duration:** prolonged — **erythromycin for at least three months** is recommended (or doxycycline) to prevent relapse in immunocompromised patients (PMID 11362939).
- **Severe/systemic disease:** add **rifampicin**; **gentamicin + doxycycline** for associated bacteremia/endocarditis (PMID 24933445).
- **Adjuncts:** **antiretroviral therapy** for immune reconstitution in HIV patients (PMID 27428207); treat/eliminate ectoparasites.
- **Surgical/interventional:** localized excision has been used but relapse/dissemination risk means antibiotics are essential (PMID 12152480, PMID 16495874).
- **Advanced/experimental therapeutics (gene/cell/RNA/targeted/immunotherapy):** **Not applicable** — antibiotics are curative; no such therapies are used.
- **Adverse events:** relate to the antibiotics used (GI intolerance with erythromycin/doxycycline; photosensitivity with doxycycline); a Jarisch-Herxheimer-like reaction can occur at treatment initiation.
- **Suggested NCIT/CHEBI terms:** Erythromycin (NCIT:C578; CHEBI:42355); Doxycycline (NCIT:C513; CHEBI:50845); Azithromycin (NCIT:C609; CHEBI:2955); Clarithromycin (CHEBI:3732); Rifampicin (NCIT:C29408; CHEBI:28077); Gentamicin (NCIT:C61796; CHEBI:27412).

---

## 13. Prevention

- **Primary prevention:** avoid the exposures — for *B. henselae*: cat-flea control, prompt cleaning of cat scratches, caution around cats (esp. for immunosuppressed) (PMID 22316326); for *B. quintana*: **body-louse control/delousing, hygiene, and addressing homelessness** (PMID 9895398, PMID 11871479).
- **Secondary prevention:** early recognition and biopsy of vascular skin lesions in immunosuppressed/homeless patients; prompt antibiotics prevent dissemination.
- **Tertiary prevention:** adequate-duration antibiotics + immune reconstitution (ART) to prevent relapse and complications.
- **Immunization:** **None available** (no vaccine).
- **Public-health interventions:** vector control (fleas/lice), sanitation and services for homeless populations, clinician awareness.
- **Genetic counseling/screening:** **Not applicable** (non-genetic).
- **Prophylaxis:** no established antibiotic prophylaxis; risk-factor reduction is the mainstay.

---

## 14. Other Species / Natural Disease

- **Taxonomy of pathogens:** *Bartonella henselae* (NCBI:txid38323), *Bartonella quintana* (NCBI:txid803); related agents of pathological angiogenesis include *B. bacilliformis* (verruga peruana; NCBI:txid774) and *B. elizabethae* (NCBI:txid34113) (PMID 35379004, PMID 36810719).
- **Natural reservoir/animal disease:** **Cats** (*Felis catus*, NCBI:txid9685) are the natural reservoir of *B. henselae*, harboring asymptomatic intraerythrocytic bacteremia — they are typically **infected but not diseased** (do not develop BA) (PMID 18444576, PMID 21637717). Fleas (*Ctenocephalides felis*) and, for *B. quintana*, human body lice are vectors/reservoirs (PMID 35545848, PMID 40090362).
- **Comparative biology:** *B. henselae* induces angiogenesis in **human** endothelial cells but **not feline** endothelial cells, highlighting host-specific susceptibility (PMID 21637717). Bartonella is the only bacterial genus known to induce pathological angiogenesis in mammals (PMID 23184416).
- **Zoonotic potential:** *B. henselae* is a **zoonosis** (cat-to-human via scratch/flea); *B. quintana* is human-adapted (louse-borne, human reservoir) (PMID 9272384). No orthologous human "disease gene" applies (bacterial etiology).
- **VBO breed associations:** **Not applicable.**

---

## 15. Model Organisms

- **In vitro (primary models):** human umbilical vein and skin microvascular **endothelial cell** lines (accelerated angiogenesis/wound healing on *B. henselae* infection; PMID 21637717); human brain vascular **pericytes** (increased VEGF; PMID 23184416); **mesenchymal stromal cells** (persistence amplifying angiogenesis; PMID 34031126); recombinant **BafA passenger domain** assays (EC proliferation, tube formation, sprouting; PMID 32678094).
- **Mouse model:** immunocompetent **C57BL/6** mice given intraperitoneal *B. henselae* develop **granulomatous hepatitis** peaking week 4, resolving by 12 weeks, with hepatic bacterial DNA persistence ≥3 months (PMID 9784568). *(model organism)*
- **In vivo angiogenesis:** BafA drives **angiogenesis in mice** (PMID 32678094).
- **Genetic/transgenic disease models:** **Not applicable** — BA is an infection; there are no knockout/knock-in "BA models." Bacterial mutants (e.g., *badA⁻*, *bafA* transposon mutants, *virB/D4* strains) are used to dissect virulence (PMID 18627378, PMID 32678094, PMID 23163798).
- **Phenotype recapitulation & limitations:** cellular models reproduce the **angiogenic/anti-apoptotic signaling**; the mouse model reproduces **granulomatous containment** in an immunocompetent host but **not** the disseminated vasoproliferative tumors of immunocompromised humans — underscoring that human immunosuppression is essential to full disease.

---

## Supported and Refuted Hypotheses

**Supported:**
1. BA is caused by *B. henselae* and *B. quintana* and occurs mainly in immunosuppressed hosts. (PMID 21285862, 24933445)
2. Vasoproliferation is driven by bacterial proangiogenic factors: BafA (VEGFR-2 agonist), BadA (HIF-1 activation), and VirB/D4-delivered Beps (apoptosis inhibition). (PMID 32678094, 18627378, 23163798)
3. The two species have partly distinct tropism/exposures: *B. quintana* → subcutaneous/lytic bone lesions, homeless/louse-associated; *B. henselae* → peliosis hepatis, cat/flea-associated. (PMID 9407154)
4. Diagnosis rests on Warthin-Starry histopathology + PCR; treatment with prolonged macrolide/tetracycline is curative. (PMID 24718378, 11362939, 24933445)

**Refuted / excluded:**
- BA is **not** a genetic/heritable disease; no human causal genes, variants, or inheritance pattern apply.
- BA is **not** a neoplasm despite tumor-like appearance; it is a reversible, antibiotic-curable infection (distinguishing it from its mimic Kaposi sarcoma).

## Limitations and Future Directions

- Epidemiology lacks precise prevalence/incidence rates (rare, opportunistic, under-reported); QoL and formal outcome metrics are absent for BA specifically.
- Mechanistic data derive largely from in vitro human EC/pericyte systems and *B. henselae*; fewer *B. quintana* mechanistic studies exist, and no immunocompromised animal model fully reproduces disseminated human BA.
- Future work: an immunodeficient animal model of disseminated BA; comparative *B. quintana* vs *B. henselae* proangiogenic effector biology; molecular epidemiology in under-studied high-HIV-burden regions.

---

*Evidence base: ~15 primary references (reviews, one landmark NEJM molecular case-control study [PMID 9407154], mechanistic in vitro/in vivo studies). Evidence types span human clinical (case series/epidemiology), in vitro (endothelial/pericyte/effector studies), and model organism (mouse). No individual-patient dataset was provided.*


## Artifacts

- [OpenScientist final report](Bacillary_Angiomatosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Bacillary_Angiomatosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc2.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 33 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (1 mention) - the report calls it "Symptom"; HP calls it **Fever**
- `HP:0002716` (1 mention) - the report calls it "Sign"; HP calls it **Lymphadenopathy**
- `HP:0001744` (1 mention) - the report calls it "Sign"; HP calls it **Splenomegaly**
- `HP:0001903` (1 mention) - the report calls it "Lab"; HP calls it **Anemia**
- `HP:0001873` (1 mention) - the report calls it "Lab"; HP calls it **Thrombocytopenia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `NCIT:C29408` (RV-B7 (RECOMB VACCINIA/B7)) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000155` (1 mention) - the report calls it "Oral mucosa abnormality"; HP calls it **Oral ulcer**, and lists "Oral mucosal ulceration" among its other names
- `CL:0000115` (2 mentions) - the report calls it "vascular endothelial cells"; CL calls it **endothelial cell**
- `UBERON:0002097` (1 mention) - the report calls it "Primary organ:** skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names