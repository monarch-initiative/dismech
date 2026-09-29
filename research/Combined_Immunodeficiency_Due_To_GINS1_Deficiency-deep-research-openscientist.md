---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-30T18:31:00.736691'
end_time: '2026-08-30T18:46:47.961696'
duration_seconds: 947.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Combined Immunodeficiency Due To GINS1 Deficiency
  mondo_id: ''
  category: Immunodeficiency
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
citation_count: 8
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 17
  quotes_valid: 16
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35038632
  relevance_assessed: 13
  on_topic: 7
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 1
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: HP:0001875
    reported_labels:
    - lab abnormality
    ontology_label: Decreased total neutrophil count
  - term_id: HP:0040218
    reported_labels:
    - lab abnormality
    ontology_label: Reduced total natural killer cell count
  - term_id: HP:0001511
    reported_labels:
    - clinical sign
    ontology_label: Intrauterine growth retardation
  - term_id: HP:0004322
    reported_labels:
    - clinical sign
    ontology_label: Short stature
  - term_id: HP:0001999
    reported_labels:
    - physical
    ontology_label: Abnormal facial shape
  - term_id: HP:0000501
    reported_labels:
    - clinical sign
    ontology_label: Glaucoma
  - term_id: NCIT:C15431
    reported_labels:
    - conceptual analog
    ontology_label: Hematopoietic Cell Transplantation
  obsolete_terms:
  - term_id: GO:0006268
    ontology_label: obsolete DNA unwinding involved in DNA replication
    replaced_by: GO:0006260
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Combined_Immunodeficiency_Due_To_GINS1_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Combined_Immunodeficiency_Due_To_GINS1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due To GINS1 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Immunodeficiency

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due To GINS1 Deficiency** covering all of the
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

# Combined Immunodeficiency Due to GINS1 Deficiency — Comprehensive Disease Characteristics Report

## Summary

**Combined immunodeficiency due to GINS1 deficiency** (MONDO:0044725; OMIM #617827, "Immunodeficiency 55" / IMD55) is an ultrarare, autosomal-recessive inborn error of DNA replication. It is caused by **biallelic hypomorphic (partial loss-of-function) variants in *GINS1*** (also called *PSF1*), located at chromosome 20p11.21. GINS1 encodes one of four subunits (GINS1/PSF1, GINS2/PSF2, GINS3/PSF3, GINS4/SLD5) of the **GINS complex**, an essential component of the **CDC45–MCM2-7–GINS (CMG) replicative helicase** that unwinds double-stranded DNA at the eukaryotic replication fork. Because complete loss of GINS function is embryonic-lethal, all viable human disease results from partial deficiency, with residual GINS1 activity measured at roughly **3–16%** in patient cells.

The disorder was first defined by Cottineau and colleagues in 2017, who described 5 patients from 4 kindreds and established the **core clinical triad: intrauterine (and usually postnatal) growth retardation, chronic neutropenia, and NK-cell deficiency**. Mechanistically, hypomorphic GINS1 impairs GINS complex assembly, producing basal replication stress, defective checkpoint signaling, impaired cell-cycle control, and genomic instability — all of which are rescued by wild-type GINS1. These defects selectively cripple highly proliferative cell compartments (fetal tissues driving growth; bone-marrow myeloid and NK-cell precursors), explaining the phenotype. Residual enzymatic activity correlates with the severity of growth retardation and the cellular phenotype, though the immunological phenotype is relatively uniform across genotypes.

A 2026 case report (Mackley et al.) expanded the phenotype, describing distinctive facial dysmorphism and **glaucoma** in addition to the core triad, and noted glaucoma appearing across multiple unrelated individuals — pointing toward genuine phenotypic expansion. To date only ~9–10 patients have been reported worldwide. GINS1 deficiency belongs to a small but coherent family of "**replicative-helicase NK-cell deficiencies**," most notably the closely analogous partial MCM4 deficiency (growth retardation, adrenal insufficiency, and selective NK deficiency) and the recently described CDC45 deficiency. Management is currently supportive; no curative, disease-specific therapy has been established, although hematopoietic stem cell transplantation is the conceptual analog drawn from other combined immunodeficiencies.

---

## Key Findings

### Finding 1 — GINS1 deficiency is an autosomal-recessive combined immunodeficiency defined by a core triad

Cottineau et al. (2017, *J Clin Invest*) studied **5 patients from 4 kindreds**, all carrying compound-heterozygous rare mutations in *GINS1* (*PSF1*). Every patient displayed **intrauterine growth retardation, chronic neutropenia, and NK-cell deficiency**, and 4 of 5 also had postnatal growth retardation. This paper established both the disease entity and its defining clinical signature.

> "We studied 5 patients from 4 kindreds, all of whom displayed intrauterine growth retardation, chronic neutropenia, and NK cell deficiency. Four of the 5 patients also had postnatal growth retardation." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

The inheritance and causal chain were summarized directly:

> "Autosomal recessive, partial GINS1 deficiency impairs DNA replication and underlies intra-uterine (and postnatal) growth retardation, chronic neutropenia, and NK cell deficiency." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

A central genotype–phenotype relationship was that residual GINS1 activity graded with disease severity:

> "The residual levels of GINS1 activity reached 3% to 16% in patients' cells, depending on their GINS1 genotype, and correlated with the severity of growth retardation and the in vitro cellular phenotype." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

**Gene/identifier annotations:** *GINS1*/*PSF1*, HGNC:28980, OMIM gene *610608, chromosome 20p11.21 (Ensembl ENSG00000101003; UniProt Q14691); disease OMIM #617827 (IMD55). **Evidence type:** human clinical.

### Finding 2 — Mechanism: GINS1 is an essential CMG replicative-helicase subunit; deficiency causes replication stress and genomic instability

The GINS complex is a **1:1:1:1 heterotetramer** (SLD5/GINS4, PSF1/GINS1, PSF2/GINS2, PSF3/GINS3) essential for the initiation and progression of eukaryotic DNA replication. Together with CDC45 and the MCM2-7 hexamer it forms the **CMG helicase**, the molecular motor that separates the two DNA strands at the replication fork.

> "The CMG [Cdc45-Mcm2-7-GINS(Psf1-3, Sld5)] helicase unwinds the double helix to separate the leading and lagging DNA strands." — [PMID: 35038632](https://pubmed.ncbi.nlm.nih.gov/35038632/)

Complete loss is incompatible with life, underscoring the essentiality of the complex:

> "The GINS complex is essential for eukaryotic DNA replication, and homozygous null mutations of GINS component-encoding genes are embryonic lethal in mice." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

Patient-derived fibroblasts provided direct cellular evidence for the pathomechanism, and crucially the defect was reversible with wild-type gene restoration:

> "The patients' fibroblasts displayed impaired GINS complex assembly, basal replication stress, impaired checkpoint signaling, defective cell cycle control, and genomic instability, which was rescued by WT GINS1." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

**Evidence type:** human clinical + in vitro (patient fibroblasts) + model organism (mouse lethality).

### Finding 3 — Phenotypic spectrum expansion: dysmorphism, glaucoma, and variable infection burden

Mackley et al. (2026) reported a **2-year-old female** with growth retardation, chronic neutropenia, distinctive facial features, and **glaucoma**, carrying compound-heterozygous likely-pathogenic variants **c.-48C>G (p.?)** and **c.247C>T (p.Arg83Cys)**. Their review of all nine individuals reported to date reaffirmed the core triad while highlighting emerging features.

> "We present a 2-year-old female with growth retardation, chronic neutropenia, distinctive facial features, and glaucoma. Exome sequencing revealed two likely pathogenic variants in GINS1, c.-48C>G p.? and c.247C>T p.Arg83Cys." — [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

> "cementing growth retardation, neutropenia, and natural killer cell deficiency as core features." — [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

> "glaucoma has now been observed in multiple unrelated individuals, pointing toward possible phenotypic expansion." — [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

Notably, this proband had **no history of infections**, illustrating that the infection burden is variable and that immunodeficiency may be "mildly symptomatic" in some patients. **Evidence type:** human clinical (case report + literature review).

### Finding 4 — Model organisms and related helicasopathies contextualize the disease

Multiple orthogonal models support the mechanism and place GINS1 deficiency within a disease group:

- **Mouse:** Targeted disruption of *Sld5* (GINS4) causes an inner-cell-mass proliferation defect and peri-implantation embryonic lethality, phenocopying *Psf1* (GINS1)-null mice. *Psf1* haploinsufficiency impairs acute proliferation of bone-marrow hematopoietic stem cells during 5-FU-induced regeneration.

> "targeted disruption of SLD5 in mice causes a defect in cell proliferation in the inner cell mass, resulting in embryonic lethality at the peri-implantation stage." — [PMID: 24244394](https://pubmed.ncbi.nlm.nih.gov/24244394/)

> "haploinsufficiency of PSF1 resulted in failure of acute proliferation of bone marrow hematopoietic stem cells (HSCs) during reconstitution of bone marrow ablated by 5-FU treatment." — [PMID: 24244394](https://pubmed.ncbi.nlm.nih.gov/24244394/)

- ***Drosophila*:** Knockdown of any of the four GINS genes (*Sld5, Psf1, Psf2, Psf3*) yields virtually identical mitotic phenotypes — chromosome condensation defects, chromosome breakage, and polyploidy — confirming the shared essential function of the complex ([PMID: 40577589](https://pubmed.ncbi.nlm.nih.gov/40577589/), [PMID: 20709026](https://pubmed.ncbi.nlm.nih.gov/20709026/)).

- **Analogous human helicasopathy (MCM4):** Partial MCM4 deficiency causes a strikingly parallel human syndrome of growth retardation, adrenal insufficiency, and selective NK-cell deficiency with genomic instability — the key differential diagnosis.

> "partial MCM4 deficiency results in a genetic syndrome of growth retardation with adrenal insufficiency and selective NK deficiency." — [PMID: 22354167](https://pubmed.ncbi.nlm.nih.gov/22354167/)

Together with reviews of inborn NK-cell errors ([PMID: 24135998](https://pubmed.ncbi.nlm.nih.gov/24135998/)), these establish **"replicative-helicase NK deficiencies"** as a recognized category. **Evidence type:** model organism + human clinical (comparative).

### Finding 5 — Genetic architecture: biallelic hypomorphic variants; heterozygotes unaffected; recurrent p.Arg83Cys

gnomAD v4 constraint metrics for *GINS1* (ENSG00000101003) show **pLI ≈ 2.5×10⁻⁷ (i.e., ~0)** and observed/expected LoF (oe_lof) = 0.74 (90% CI 0.55–1.03). This indicates *GINS1* is **not** loss-of-function-intolerant at the heterozygous level, fully consistent with a recessive disease in which carriers are healthy. Reported disease alleles span **5′UTR/promoter-proximal, missense, and splice classes**. The Mackley 2026 case carried:

| Variant | cDNA | Protein | gnomAD exome AF | ClinVar |
|---|---|---|---|---|
| 5′UTR | c.-48C>G | p.? | 3.9×10⁻⁶ (5 alleles) | ultrarare |
| Missense | c.247C>T | p.Arg83Cys | 6.6×10⁻⁴ (951 alleles) | conflicting classifications |
| Missense | c.455G>A | p.Cys152Tyr | — | Likely pathogenic |

Of ~188 ClinVar *GINS1* entries, the majority are variants of uncertain significance (VUS). The preserved residual activity (3–16%) confirms these are **hypomorphic** rather than null alleles.

> "The residual levels of GINS1 activity reached 3% to 16% in patients' cells, depending on their GINS1 genotype." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

> "Exome sequencing revealed two likely pathogenic variants in GINS1, c.-48C>G p.? and c.247C>T p.Arg83Cys." — [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

**Evidence type:** human clinical + computational (population genetics).

### Finding 6 — Disease nosology and identifiers

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0044725 ("combined immunodeficiency due to GINS1 deficiency") |
| OMIM phenotype | #617827 (Immunodeficiency 55, IMD55) |
| OMIM gene | *610608 (*GINS1*) |
| HGNC | HGNC:28980 |
| NCBI Gene | 9837 |
| Ensembl | ENSG00000101003 |
| UniProt | Q14691 |
| Cytoband | 20p11.21 |
| Orphanet | "Combined immunodeficiency due to GINS1 deficiency" |
| MeSH | No dedicated descriptor (indexed under Severe Combined Immunodeficiency / Primary Immunodeficiency Diseases) |

**Synonyms:** CID due to GINS1 deficiency; IMD55; combined immunodeficiency with intrauterine growth retardation–NK cell deficiency–neutropenia; PSF1 deficiency. Information is derived from **aggregated disease-level resources and individual patient case series** (not EHR-scale data).

### Finding 7 — GINS1/PSF1 protein biology and structure

UniProt Q14691 (GINS1/PSF1) is a **196-amino-acid nuclear DNA-replication factor** localizing to the nucleus and chromosome. It is required for GINS complex function in the initiation and progression of DNA replication; GINS is a core component of the CMG helicase that unwinds template DNA. GINS1 forms a stable subcomplex with GINS4 (SLD5) and assembles the GINS heterotetramer (GINS1/2/3/4). Domain annotations: **Pfam PF05916 (SLD5/GINS), InterPro IPR056783**. Multiple experimental structures exist — the human GINS complex (**PDB 2E9X, 2EHO, 2Q9Q**) and cryo-EM human CMG replisome assemblies (**PDB 6XTX, 6XTY, 7PFO, 8OK2, 9E2Z**). Variant-induced failure of assembly directly links protein dysfunction to the cellular phenotype.

> "The patients' fibroblasts displayed impaired GINS complex assembly, basal replication stress, impaired checkpoint signaling, defective cell cycle control, and genomic instability." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

### Finding 8 — Clinical course, diagnostics, prognosis, and management

Cottineau (2017) established that the combined neutropenia + NK-cell deficiency arises from a **maturation blockade in the bone marrow** and was "mildly symptomatic." Onset is **congenital/prenatal** (IUGR), with a chronic postnatal course; growth-retardation severity tracks residual GINS1 activity.

> "The association of neutropenia and NK cell deficiency, which is unusual among primary immunodeficiencies and bone marrow failures, was due to a blockade in the bone marrow and was mildly symptomatic." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

> "The residual levels of GINS1 activity reached 3% to 16% in patients' cells, depending on their GINS1 genotype, and correlated with the severity of growth retardation." — [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

**Diagnostic workup:** complete blood count (chronic neutropenia; HP:0001875); lymphocyte immunophenotyping showing reduced/absent NK cells (CD3⁻CD56⁺; NK deficiency HP:0040218) with relatively preserved T/B lymphocytes; NK cytotoxicity assays; bone-marrow examination (myeloid maturation arrest); growth assessment (IUGR/short stature HP:0001511/HP:0004322); and cytogenetic/genomic-instability testing. **Molecular diagnosis** is via WES/WGS or targeted inborn-errors-of-immunity/bone-marrow-failure gene panels including *GINS1*, with single-gene/segregation testing confirming biallelic variants. **Evidence type:** human clinical.

---

## Section-by-Section Report

### 1. Disease Information
GINS1 deficiency is an ultrarare autosomal-recessive combined immunodeficiency and inborn error of DNA replication. **Overview:** biallelic hypomorphic variants in *GINS1* partially impair the CMG replicative helicase, causing replication stress and a characteristic triad of growth retardation, chronic neutropenia, and NK-cell deficiency. **Identifiers:** MONDO:0044725; OMIM #617827 (IMD55); OMIM gene *610608; HGNC:28980; NCBI Gene 9837; Ensembl ENSG00000101003; UniProt Q14691; Orphanet "Combined immunodeficiency due to GINS1 deficiency"; no dedicated ICD-11/MeSH term (indexed under primary/severe combined immunodeficiency). **Synonyms:** IMD55, CID due to GINS1 deficiency, PSF1 deficiency, combined immunodeficiency with IUGR–NK deficiency–neutropenia. **Source:** disease-level aggregation + individual case series (not EHR).

### 2. Etiology
**Causal factor:** monogenic — biallelic (compound heterozygous or homozygous) **hypomorphic variants in *GINS1***. **Genetic risk:** the disease requires two defective alleles; heterozygous carriers are unaffected (pLI ≈ 0). No environmental, infectious, or lifestyle cause; there are no established modifier genes, protective alleles, or gene–environment interactions. **Consanguinity** increases risk of recessive homozygosity, as with all AR disorders. Residual GINS1 activity (a genotype-dependent quantitative trait) is the principal severity determinant. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

### 3. Phenotypes
| Phenotype | Type | HPO | Onset | Frequency | Severity/course |
|---|---|---|---|---|---|
| Intrauterine growth retardation | clinical sign | HP:0001511 | prenatal | 100% (5/5, 9/9) | severe, tracks residual activity |
| Postnatal growth retardation / short stature | clinical sign | HP:0004322 | infancy | ~80% (4/5) | variable |
| Chronic neutropenia | lab abnormality | HP:0001875 | congenital | core (all) | chronic, "mildly symptomatic" |
| NK-cell deficiency | lab abnormality | HP:0040218 | congenital | core (all) | persistent |
| Distinctive facial features | physical | HP:0001999 | congenital | subset | emerging |
| Glaucoma | clinical sign | HP:0000501 | early childhood | multiple unrelated | emerging |
| Viral susceptibility | symptom | — | variable | variable (some none) | variable |

**Quality-of-life impact:** growth failure and chronic immune surveillance dominate; infection burden is variable and sometimes absent. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/), [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

### 4. Genetic/Molecular Information
**Causal gene:** *GINS1* (*PSF1*), 20p11.21. **Variant classes:** 5′UTR (c.-48C>G), missense (c.247C>T p.Arg83Cys; c.455G>A p.Cys152Tyr Likely pathogenic), and splice. **Population frequency:** disease alleles are rare-to-ultrarare (p.Arg83Cys AF ~6.6×10⁻⁴; c.-48C>G AF ~3.9×10⁻⁶). **Origin:** germline. **Functional consequence:** partial loss of function (hypomorphic) with 3–16% residual activity; not gain-of-function or dominant-negative. **Modifier genes/epigenetics/chromosomal abnormalities:** none established. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/), [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

### 5. Environmental Information
No environmental, lifestyle, or infectious cause. Infections are downstream *consequences* of immunodeficiency, not triggers. Not applicable for toxin/occupational/dietary factors.

### 6. Mechanism / Pathophysiology
See the Mechanistic Model below. **Molecular pathway:** DNA replication initiation/elongation via the CMG helicase (GO:0006270, GO:0006260). **Cellular processes:** replication stress, S-phase/replication checkpoint signaling (GO:0000076), cell-cycle dysregulation, genomic instability. **Protein dysfunction:** impaired GINS heterotetramer assembly → destabilized CMG. **Immune involvement:** immunodeficiency via failed proliferation of NK-lineage and myeloid precursors (bone-marrow maturation blockade). **Tissue-damage mechanism:** proliferation failure/genomic instability in high-turnover compartments. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/), [PMID: 35038632](https://pubmed.ncbi.nlm.nih.gov/35038632/)

### 7. Anatomical Structures Affected
**Organ/system:** bone marrow (UBERON:0002371) and immune system (primary); whole-body growth; eye (UBERON:0000970, glaucoma). **Cell types (CL):** natural killer cell (CL:0000623), neutrophil (CL:0000775), hematopoietic stem/progenitor cell (CL:0000037), myeloid precursors; patient fibroblasts show the cellular defect in vitro. **Subcellular (GO CC):** nucleus (GO:0005634), chromosome (GO:0005694), CMG complex (GO:0071162), GINS complex (GO:0000811). **Lateralization:** systemic/bilateral (e.g., glaucoma may be bilateral).

### 8. Temporal Development
**Onset:** congenital/prenatal (IUGR). **Course:** chronic, lifelong; growth retardation and cytopenias persist. **Progression:** generally stable rather than rapidly progressive; severity set largely at birth by residual activity. No defined staging. **Critical period:** fetal/early-childhood growth window. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears complete for the core triad in biallelic individuals; expressivity variable for growth severity and emerging features. **Epidemiology:** ultrarare — only ~9–10 reported patients worldwide; no formal prevalence/incidence estimate. **Carrier state:** healthy (pLI ≈ 0). **Consanguinity** relevant as for all AR disease. No confirmed founder effect, anticipation, mosaicism, or sex bias documented given the tiny cohort. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/), [PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)

### 10. Diagnostics
**Laboratory:** CBC (chronic neutropenia), lymphocyte immunophenotyping (reduced/absent CD3⁻CD56⁺ NK cells, preserved T/B), NK cytotoxicity assay, bone-marrow aspiration (myeloid maturation arrest), cytogenetic/genomic-instability testing (patient fibroblasts). **Genetic testing:** WES/WGS or targeted IEI/bone-marrow-failure panels including *GINS1*; single-gene/segregation confirmation of biallelic variants; functional residual-activity assay as a confirmatory research tool. **Differential diagnosis:** partial MCM4 deficiency (adds adrenal insufficiency), CDC45 deficiency, other congenital neutropenias and NK-deficiency syndromes. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/), [PMID: 22354167](https://pubmed.ncbi.nlm.nih.gov/22354167/)

### 11. Outcome / Prognosis
Immunodeficiency is often **"mildly symptomatic"**; the bone-marrow blockade underlies the cytopenias. Growth-retardation severity is prognostically tied to residual GINS1 activity. Given documented genomic instability, a theoretical (unquantified) malignancy risk exists by analogy to MCM4. No survival/mortality statistics are available due to the tiny cohort. [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

### 12. Treatment
No disease-specific or curative therapy is established. Management is **supportive**: infection surveillance/prophylaxis, treatment of neutropenia-related infections, growth monitoring, and ophthalmologic care for glaucoma. Hematopoietic stem cell transplantation (NCIT:C15431) is the conceptual analog from other combined immunodeficiencies but would not correct the intrinsic non-hematopoietic growth defect; its role is undefined. No gene/cell/RNA therapy or clinical-trial data specific to GINS1.

### 13. Prevention
No primary prevention (monogenic, congenital). **Secondary/tertiary:** early diagnosis, infection prophylaxis, and surveillance for complications. **Genetic counseling** for recessive recurrence risk (25% in carrier couples); carrier and prenatal/preimplantation testing available once familial variants are known. No newborn-screening program targets GINS1 specifically (though NK/immune deficiencies may be flagged by TREC-based SCID screening in some cases).

### 14. Other Species / Natural Disease
No naturally occurring companion-animal or wildlife disease documented (OMIA has no GINS1 entry). Orthologs are highly conserved: mouse *Gins1*/*Psf1* and *Gins4*/*Sld5*; *Drosophila Psf1/Psf2/Psf3/Sld5*; yeast GINS (Sld5, Psf1-3). Evolutionary conservation of the CMG mechanism is strong across eukaryotes and archaea. Not zoonotic. [PMID: 24244394](https://pubmed.ncbi.nlm.nih.gov/24244394/), [PMID: 40577589](https://pubmed.ncbi.nlm.nih.gov/40577589/)

### 15. Model Organisms
**Mouse:** *Psf1*-null and *Sld5*-null are embryonic-lethal (peri-implantation); *Psf1* haploinsufficiency impairs regenerative HSC proliferation — recapitulates the proliferation-dependence but not the viable hypomorphic human phenotype (a hypomorphic knock-in is lacking). **Drosophila:** RNAi/mutant of any GINS subunit reproduces genomic-instability/mitotic defects. **In vitro:** patient-derived fibroblasts recapitulate impaired GINS assembly, replication stress, and genomic instability, rescued by WT GINS1 — the best available disease-relevant model. **Limitation:** no model reproduces the full human triad simultaneously. [PMID: 24244394](https://pubmed.ncbi.nlm.nih.gov/24244394/), [PMID: 20709026](https://pubmed.ncbi.nlm.nih.gov/20709026/), [PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)

---

## Mechanistic Model / Interpretation

The pathophysiology of GINS1 deficiency follows a clean causal chain from a housekeeping molecular defect to a tissue-selective clinical phenotype:

```
  Biallelic hypomorphic GINS1 variants (residual activity 3–16%)
              │
              ▼
  Impaired assembly of the GINS heterotetramer (GINS1/2/3/4)
              │
              ▼
  Destabilized CMG helicase (CDC45–MCM2-7–GINS)
              │
              ▼
  Reduced/ slowed replication-fork unwinding  →  basal REPLICATION STRESS
              │
              ▼
  Impaired S-phase checkpoint signaling + defective cell-cycle control
              │
              ▼
  GENOMIC INSTABILITY (chromosome breakage, ↑ single-stranded DNA)
              │
              ▼
  Proliferation failure — selectively in HIGHLY DIVIDING compartments
       ├── Fetal/postnatal growth → IUGR + short stature
       ├── Bone-marrow myeloid precursors → maturation blockade → NEUTROPENIA
       └── NK-cell lineage (proliferation-dependent) → NK-CELL DEFICIENCY
              │
              ▼
  Variable viral susceptibility; emerging: dysmorphism, glaucoma
```

**Upstream vs downstream:** The primary (upstream) lesion is a *quantitative* deficit of a structural replisome subunit. Everything downstream — replication stress, checkpoint failure, genomic instability, and cell-cycle arrest — is a generic consequence of a weakened replication machine. The **tissue selectivity** of the clinical phenotype is not explained by tissue-specific gene function (GINS1 is ubiquitous) but by **differential proliferative demand**: the cell populations that must divide fastest during fetal development and hematopoiesis are the most sensitive to a partially crippled replisome. This is the unifying principle of the "replicative-helicase disorders."

**Why NK cells specifically?** NK-cell development appears exquisitely proliferation-dependent, which is why selective NK deficiency is a shared signature of *GINS1*, *MCM4*, and *CDC45* defects. The mouse data reinforce this: *Psf1* haploinsufficiency specifically impairs *acute* HSC proliferation under regenerative stress, precisely the condition under which a marginal replisome is exposed.

**Comparison of replicative-helicase NK deficiencies:**

| Feature | GINS1 deficiency | MCM4 deficiency | CDC45 deficiency |
|---|---|---|---|
| Gene / complex role | GINS subunit (CMG) | MCM2-7 helicase core (CMG) | CMG activator/component |
| Inheritance | Autosomal recessive | Autosomal recessive | Autosomal dominant (allelic-expression bias) |
| Growth retardation | Yes (IUGR + postnatal) | Yes (short stature) | Variable |
| NK-cell deficiency | Yes (core) | Yes (selective, CD56dim) | Yes (variable) |
| Neutropenia | Yes (core) | Not prominent | Variable |
| Adrenal insufficiency | No | Yes (characteristic) | No |
| Genomic instability | Yes | Yes | Yes |
| Key refs | 28414293 | 22354167 / 22354170 | 41867723 |

This comparison is diagnostically useful: the **combination of neutropenia + NK deficiency without adrenal insufficiency** favors GINS1, whereas **adrenal failure + NK deficiency** points to MCM4.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/) | *Inherited GINS1 deficiency underlies growth retardation along with neutropenia and NK cell deficiency* | **Landmark defining paper.** Establishes the disease, core triad, autosomal-recessive inheritance, hypomorphic mechanism (3–16% residual activity), and the fibroblast replication-stress phenotype. Supports Findings 1, 2, 5, 7, 8. |
| [41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/) | *Expanding Phenotype of GINS1 Deficiency: A Case Report and Review* | **Phenotype expansion.** New patient with dysmorphism and glaucoma, variant details (c.-48C>G; p.Arg83Cys), and confirmation of the core triad across 9 individuals. Supports Findings 3, 5. |
| [35038632](https://pubmed.ncbi.nlm.nih.gov/35038632/) | *Increased contribution of DNA polymerase delta to leading-strand replication with an impaired CMG helicase* | Defines GINS role within the CMG helicase. Supports Finding 2. |
| [24244394](https://pubmed.ncbi.nlm.nih.gov/24244394/) | *Requirement of SLD5 for early embryogenesis* | Mouse model: GINS-subunit knockout is embryonic lethal; PSF1 dosage limits HSC proliferation. Supports Finding 4. |
| [22354167](https://pubmed.ncbi.nlm.nih.gov/22354167/) | *Partial MCM4 deficiency…growth retardation, adrenal insufficiency, and NK cell deficiency* | Analogous helicasopathy and primary differential diagnosis. Supports Finding 4. |
| [22354170](https://pubmed.ncbi.nlm.nih.gov/22354170/) | *MCM4 mutation causes adrenal failure, short stature, and NK cell deficiency* | Corroborates MCM4 phenotype and genomic-instability/replicative-helicase theme. Context for Finding 4. |
| [24135998](https://pubmed.ncbi.nlm.nih.gov/24135998/) | *Inborn errors of the development of human natural killer cells* | Frames NK-cell deficiencies including replicative-helicase causes. Context for Finding 4. |
| [40577589](https://pubmed.ncbi.nlm.nih.gov/40577589/), [20709026](https://pubmed.ncbi.nlm.nih.gov/20709026/) | *Drosophila* CMG/Sld5 studies | Show identical mitotic defects on knockdown of any GINS subunit; genomic-integrity role. Context for Finding 4. |
| [41867723](https://pubmed.ncbi.nlm.nih.gov/41867723/) | *Autosomal dominant CDC45 deficiency…* | Related CMG-component immune disease (NK reduction). Comparative context. |
| [31815930](https://pubmed.ncbi.nlm.nih.gov/31815930/), [33322195](https://pubmed.ncbi.nlm.nih.gov/33322195/), [37481989](https://pubmed.ncbi.nlm.nih.gov/37481989/) | Yeast CMG/GINS mechanism papers | Mechanistic support for replication-stress/genomic-instability consequences of impaired GINS/CMG. Context for Finding 2. |

The evidence base is internally consistent: the human genetic/clinical data (28414293, 41689265) are mechanistically explained by orthogonal model-organism and biochemical studies, and the phenotype is cross-validated by the analogous MCM4/CDC45 disorders.

---

## Limitations and Knowledge Gaps

1. **Extremely small sample size.** The entire literature comprises ~9–10 patients from a handful of kindreds. All epidemiological, prognostic, and genotype–phenotype statements are correspondingly uncertain; no formal prevalence/incidence exists (Orphanet lists it among ultrarare immunodeficiencies without a stable point estimate).

2. **No dedicated natural-history or outcome study.** Long-term survival, malignancy risk (theoretically elevated given genomic instability, by analogy to MCM4), and adult outcomes are unknown. Life expectancy and mortality figures cannot be quantified.

3. **No disease-specific treatment evidence.** There are no clinical trials, no gene- or cell-therapy data specific to GINS1, and no FDA-approved therapy. HSCT is a conceptual analog from other CIDs but its role for GINS1 (given the *non*-hematopoietic growth phenotype it would not correct) is undefined.

4. **Variant interpretation is immature.** Most ClinVar *GINS1* entries are VUS; the recurrent p.Arg83Cys allele has conflicting classifications and a relatively high population frequency (AF ~6.6×10⁻⁴), complicating pathogenicity calls. Functional assays (residual-activity measurement) are the current gold standard but are not widely available.

5. **Emerging features are provisional.** Glaucoma and facial dysmorphism are reported in a subset; their penetrance, mechanism, and true association require more cases.

6. **No direct patient-derived omics.** Transcriptomic, proteomic, metabolomic, or single-cell datasets specific to GINS1-deficient patients were not identified; mechanistic inference relies on fibroblast functional assays and model organisms.

7. **No purpose-built animal model of the human disease.** Null mice are embryonic-lethal; a hypomorphic knock-in recapitulating the human hypomorphic state has not been reported, limiting preclinical therapeutic testing.

---

## Proposed Follow-up Experiments / Actions

1. **Build an international patient registry.** Pool the ~10 known cases and prospectively enroll new ones to define natural history, infection burden, malignancy incidence, and survival — the single highest-value action for this ultrarare disease.

2. **Generate a hypomorphic GINS1 mouse (or zebrafish) knock-in** reproducing 3–16% residual activity, to model the *viable* human phenotype (growth retardation, neutropenia, NK deficiency) and serve as a preclinical platform. Null models are uninformative because they are lethal.

3. **Functional variant-classification pipeline.** Develop a standardized cellular assay (GINS complex assembly + residual replication activity + genomic-instability readout) to reclassify the many *GINS1* VUS, especially p.Arg83Cys, and correlate residual activity with clinical severity across more genotypes.

4. **Single-cell profiling of patient bone marrow and NK-lineage cells** to pinpoint the exact developmental stage of the maturation blockade and test the "proliferation-demand" hypothesis for lineage selectivity.

5. **Systematic screening for glaucoma and dysmorphism** in all diagnosed patients to establish penetrance and determine whether ophthalmologic surveillance should be standard of care.

6. **Assess long-term cancer risk** given documented genomic instability, with structured surveillance protocols mirroring those used in MCM4 deficiency and other chromosomal-instability syndromes.

7. **Evaluate whether HSCT corrects the hematologic/immune phenotype** (neutropenia, NK deficiency) while recognizing it cannot address the intrinsic growth defect — clarify the risk/benefit in symptomatic patients.

---

## Consolidated Ontology Term Suggestions

- **Disease:** MONDO:0044725
- **Gene/protein:** HGNC:28980 (*GINS1*); UniProt Q14691
- **Phenotypes (HPO):** Intrauterine growth retardation HP:0001511; Short stature HP:0004322; Neutropenia HP:0001875; NK-cell deficiency HP:0040218; Glaucoma HP:0000501; Abnormal facial shape HP:0001999
- **Biological processes (GO):** DNA replication GO:0006260; DNA replication initiation GO:0006270; DNA unwinding involved in DNA replication GO:0006268; cell-cycle checkpoint signaling GO:0000075; DNA replication checkpoint GO:0000076
- **Cellular components (GO):** CMG complex GO:0071162; GINS complex GO:0000811; nucleus GO:0005634; chromosome GO:0005694
- **Cell types (CL):** natural killer cell CL:0000623; neutrophil CL:0000775; hematopoietic stem cell CL:0000037
- **Anatomy (UBERON):** bone marrow UBERON:0002371; eye UBERON:0000970
- **Treatment (NCIT):** Hematopoietic stem cell transplantation NCIT:C15431 (conceptual analog); supportive care NCIT:C15277

---

*Report compiled from 5 iterations of autonomous investigation, 8 confirmed findings, and 27 reviewed papers. Primary evidence: Cottineau et al. 2017 ([PMID: 28414293](https://pubmed.ncbi.nlm.nih.gov/28414293/)) and Mackley et al. 2026 ([PMID: 41689265](https://pubmed.ncbi.nlm.nih.gov/41689265/)).*


## Artifacts

- [OpenScientist final report](Combined_Immunodeficiency_Due_To_GINS1_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Combined_Immunodeficiency_Due_To_GINS1_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 16 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35038632` *(abstract only)*: "The CMG [Cdc45-Mcm2-7-GINS(Psf1-3, Sld5)] helicase unwinds the double helix to separate the leading and lagging DNA strands."
  - closest text in source: "The CMG [Cdc45-Mcm2-7-GINS(Psf1-3, Sld5)] helicase unwinds the double helix to separate the leading and lagging DNA strands, which are replicated by the specialized DNA polymerases epsilon (Pol ε) and delta (Pol δ), respectively"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001875` (3 mentions) - the report calls it "lab abnormality"; HP calls it **Decreased total neutrophil count**
- `HP:0040218` (3 mentions) - the report calls it "lab abnormality"; HP calls it **Reduced total natural killer cell count**
- `HP:0001511` (3 mentions) - the report calls it "clinical sign"; HP calls it **Intrauterine growth retardation**
- `HP:0004322` (3 mentions) - the report calls it "clinical sign"; HP calls it **Short stature**
- `HP:0001999` (2 mentions) - the report calls it "physical"; HP calls it **Abnormal facial shape**
- `HP:0000501` (2 mentions) - the report calls it "clinical sign"; HP calls it **Glaucoma**
- `NCIT:C15431` (2 mentions) - the report calls it "conceptual analog"; NCIT calls it **Hematopoietic Cell Transplantation**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006268` (obsolete DNA unwinding involved in DNA replication) (1 mention) - replaced by `GO:0006260`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:28980` - called "HGNC", "GINS1"