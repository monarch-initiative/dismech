---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T13:30:23.149091'
end_time: '2026-09-04T13:48:19.250665'
duration_seconds: 1076.1
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hearing Loss Autosomal Dominant 83
  mondo_id: ''
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
citation_count: 2
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: GO:0005874
    reported_labels:
    - Microtubule cytoskeleton
    - Subcellular level:** **Microtubule cytoskeleton
    ontology_label: microtubule
  - term_id: UBERON:0001681
    reported_labels:
    - spiral ganglion
    ontology_label: nasal bone
  - term_id: HP:0000407
    reported_labels:
    - SNHL
    ontology_label: Sensorineural hearing impairment
  - term_id: HP:0006385
    reported_labels:
    - high-frequency HL
    ontology_label: Short lower limbs
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hearing_Loss_Autosomal_Dominant_83-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hearing_Loss_Autosomal_Dominant_83-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Dominant 83
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Dominant 83** covering all of the
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

# Hearing Loss, Autosomal Dominant 83 (DFNA83) — Comprehensive Disease Report

**Category:** Mendelian (monogenic) disorder
**Causal gene:** *MAP1B* (microtubule-associated protein 1B)
**OMIM phenotype:** #619808 · **Gene OMIM:** *157129 · **Locus:** 5q13.2

> **Annotation note:** The DFNA locus number is *not* a reliable guide to the gene. DFNA83 is caused by ***MAP1B***, not GRAP (GRAP causes autosomal **recessive** DFNB114, OMIM #618456). This report is built on the primary discovery paper (Cui et al., *JCI Insight* 2020, **PMID 33268592**), a *MAP1B* genotype–phenotype review (Zhou et al. 2025, **PMID 40802165**), and a DFNA overview (Aldè et al. 2023, **PMID 37371710**). Evidence is disease-level/aggregated (family studies + model organisms + patient iPSC in vitro work); it is not derived from EHR/individual-patient registries.

---

## Summary

**Hearing Loss, Autosomal Dominant 83 (DFNA83; OMIM #619808)** is a rare, non-syndromic, post-lingual, bilateral, progressive, high-frequency-predominant **sensorineural hearing loss** caused by heterozygous **missense** variants in ***MAP1B*** (microtubule-associated protein 1B) at chromosome **5q13.2**. It was defined by Cui et al. (2020) in three unrelated Chinese families carrying three novel missense variants — **p.Ser1400Gly**, **p.Ile923Thr**, and **p.Phe1838Leu** — that cosegregated with disease ([PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/)).

Mechanistically, DFNA83 is a **"neural" (spiral-ganglion) hearing loss** rather than a hair-cell disorder. MAP1B is selectively expressed in cochlear **spiral ganglion neurons (SGNs)**. Mutant MAP1B shows reduced abundance and deficient phosphorylation, destabilizing microtubule dynamics; in patient iPSC-derived otic sensory neuron-like cells this produced disturbed microtubules, impaired axonal elongation, and defective electrophysiology — all reversed by CRISPR/Cas9 correction. A *Map1b* heterozygous knockout mouse recapitulated late-onset progressive high-frequency SNHL with SGN defects but **structurally preserved cochlear hair cells**, which clinically corresponds to preserved otoacoustic emissions with abnormal neural responses (auditory-neuropathy-like/retrocochlear pattern).

A defining feature of *MAP1B* is **genotype–phenotype pleiotropy**: heterozygous **missense** variants cause isolated deafness (DFNA83, #619808), whereas **loss-of-function/truncating** variants cause **periventricular nodular heterotopia 9 (PVNH9, #618918)** with developmental delay, intellectual disability, and epilepsy. There is no gene-specific or disease-modifying therapy; management is habilitative (hearing aids, cochlear implantation, audiologic surveillance, noise/ototoxin avoidance) with standard autosomal dominant genetic counseling (50% offspring recurrence risk).

---

## Key Findings

1. **DFNA83 is caused by heterozygous *MAP1B* missense variants (5q13.2).** Three novel variants — c.4198A>G (p.Ser1400Gly, MTA domain phospho-site), c.2768T>C (p.Ile923Thr), c.5512T>C (p.Phe1838Leu) — cosegregated with AD nonsyndromic SNHL in 3 unrelated Chinese families ([PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/)).
2. **Mechanism = SGN microtubule dysfunction.** Reduced MAP1B levels and deficient phosphorylation destabilize microtubules in spiral ganglion neurons, impairing axon growth and electrophysiology.
3. **Phenotype = late-onset, progressive, bilateral, high-frequency SNHL** as the sole feature (nonsyndromic).
4. **A *Map1b* heterozygous KO mouse recapitulates the disease**, and CRISPR rescue of patient iPSC neurons establishes causality.
5. **Neural (spiral-ganglion) SNHL with preserved outer hair cell function** — normal cochlear morphology in mouse; preserved DPOAE clinically.
6. **Autosomal dominant, ultra-rare** — only 3 families reported; 50% offspring risk; consider de novo with negative family history.
7. **Management is habilitative** — hearing aids, cochlear implants, audiologic surveillance, genetic counseling.
8. **Conserved MAP-family cochlear biology** — MAP1B restricted to spiral ganglia; MAP1A in inner hair cells; MAP2 in hair cells and SGN nerves.
9. **Genotype–phenotype dichotomy** — missense → DFNA83 (deafness); LOF → PVNH9 (brain malformation) ([PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/)).
10. **Diagnosis** = characteristic audioprofile + AD family history + heterozygous *MAP1B* variant on NGS panel/exome; DPOAE-preserved/ABR-abnormal neural signature.
11. **Prognosis** = non-lethal, normal life expectancy, chronic progressive communication disability; no infectious/toxic cause.
12. **Pleiotropy anchored** — DFNA83 (#619808) vs PVNH9 (#618918), the latter from truncating variants removing the C-terminal LC1 segment (Walters et al. 2018).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous *MAP1B* missense variant** (e.g., p.Ser1400Gly in the MTA domain) is inherited → **results in** an altered MAP1B protein and disrupts a conserved GSK3β/DYRK1A phosphorylation site (Ser1400).
2. This **leads to** reduced MAP1B protein levels and **deficient phosphorylation** (patient iPSC otic neurons; PMID 33268592).
3. Reduced/hypophosphorylated MAP1B **results in** impaired regulation of **microtubule stability and dynamics**.
4. Disturbed microtubule dynamics **lead to** defective **axonal elongation** and altered **electrophysiology** in spiral ganglion neurons — rescued by CRISPR correction.
5. SGN dysfunction **results in** failure of afferent transmission — while **hair cells and cochlear architecture remain intact** (mouse; inferred to explain preserved human DPOAE).
6. This **leads to** a **progressive, high-frequency-predominant sensorineural (neural) hearing loss** — DFNA83.

*Branch:* a **truncating/LOF** *MAP1B* allele (removing LC1) instead shifts the dominant consequence to **defective cortical neuronal migration → PVNH9** rather than isolated deafness.

```
                          MAP1B heterozygous variant
                                    │
             ┌──────────────────────┴──────────────────────┐
       MISSENSE variant                            LOF / TRUNCATING variant
   (partial loss of function,                  (removes C-terminal LC1 domain)
    reduced levels/phospho)                              │
             │                                  Impaired neuronal migration
   SGN microtubule dysfunction                  & cortical organization
   (hair cells spared)                                   │
             │                                    PVNH9 (#618918)
        DFNA83 (#619808)                    Developmental delay, ID, epilepsy
   Isolated progressive SNHL
```

**Ontology mapping:** microtubule cytoskeleton organization **GO:0000226**; microtubule **GO:0005874**; axon development **GO:0061564**; growth cone **GO:0030426**; spiral ganglion neuron (sensory neuron **CL:0000103**); cochlea **UBERON:0001844**; spiral ganglion **UBERON:0001681**; HP:0000407 (SNHL), HP:0001730 (progressive), HP:0006385 (high-frequency HL).

---

## 1. Disease Information

DFNA83 is a rare, **autosomal dominant, non-syndromic, sensorineural hearing loss (SNHL)** in which hearing impairment is the sole clinical feature. It is post-lingual, bilateral, progressive, and predominantly affects high frequencies. Mechanistically it is a **spiral-ganglion-neuron (auditory-neuron) disorder** with structurally preserved cochlear hair cells — a "neural"/auditory-neuropathy-like SNHL rather than a classic sensory (hair-cell) SNHL.

**Key identifiers**
- **OMIM (phenotype):** 619808 — DEAFNESS, AUTOSOMAL DOMINANT 83; DFNA83
- **Gene:** *MAP1B* — OMIM *157129; **HGNC:6836**; **NCBI Gene 4131**; **Ensembl ENSG00000131711**; **UniProt P46821**; reference transcript **NM_005909.4**
- **MONDO:** maps from OMIM:619808 (Deafness, autosomal dominant 83)
- **Orphanet / ICD-10 / ICD-11 / MeSH:** No dedicated DFNA83-specific code identified; classifiable under hereditary/genetic sensorineural hearing loss (ICD-10 H90.x; ICD-11 AB52; MeSH "Hearing Loss, Sensorineural" D006319).
- **Synonyms:** DFNA83; Deafness, autosomal dominant 83; MAP1B-related autosomal dominant hearing loss. (*MAP1B* aliases: MAP5, FUTSCH, PPP1R102, PVNH9.)

---

## 2. Etiology

**Primary cause — genetic.** DFNA83 is a monogenic disorder caused by **heterozygous missense variants in *MAP1B***. No environmental or infectious agent causes the disease.

> *"Three novel heterozygous MAP1B mutations (c.4198A>G, p.1400S>G; c.2768T>C, p.923I>T; c.5512T>C, p.1838F>L) were cosegregated with autosomal dominant inheritance of nonsyndromic sensorineural hearing loss in 3 unrelated Chinese families."* — Cui et al. 2020 ([PMID: 33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/))

**Genetic risk factors:** The causal *MAP1B* missense variant itself is the risk determinant (Mendelian dominant). No susceptibility loci or modifier genes have been defined for DFNA83 (small number of families). Family history (an affected parent) is the principal risk indicator; de novo occurrence is possible.

**Environmental risk / aggravating factors:** None cause the disease, but noise exposure and ototoxic drugs (e.g., aminoglycosides, cisplatin) are plausible **aggravators** of high-frequency SNHL and should be avoided (extrapolated from general DFNA management, PMID 37371710). Aging adds presbycusic decline on top of the genetic loss.

**Protective factors:** None established (genetic or environmental).

**Gene–environment interactions:** Not formally studied for *MAP1B*; the reasonable expectation is that noise/ototoxin exposure accelerates the genetically determined progressive loss. **Evidence: not available for DFNA83 specifically.**

---

## 3. Phenotypes

**Phenotype type:** Clinical sign / laboratory (audiometric) abnormality — bilateral sensorineural hearing loss. No syndromic features (no vestibular, visual, renal, neurologic, or dysmorphic findings reported).

| Characteristic | Detail |
|---|---|
| **Onset** | Post-lingual, late-onset; typically 2nd–3rd decade; variable within families |
| **Severity** | Variable — mild to profound |
| **Progression** | Progressive (worsens with age); sloping (high-frequency-predominant) audiogram |
| **Laterality** | Bilateral |
| **Frequency among carriers** | High penetrance (cosegregated in affected family members); expressivity variable |

**Suggested HPO terms:** Sensorineural hearing impairment **HP:0000407**; Bilateral SNHL **HP:0008619**; Progressive hearing impairment **HP:0001730**; High-frequency hearing impairment **HP:0006385**; Adult onset **HP:0003581**; Variable expressivity **HP:0003828**.

**Quality-of-life impact:** Progressive communication disability affecting speech understanding, education, employment, and social participation. Untreated hearing loss is associated with reduced HRQoL, social isolation, and accelerated cognitive decline in older adults (general hearing-loss literature). Applicable instruments: HHIE, SF-36, EQ-5D, PROMIS. DFNA83-specific QoL data are **not available**.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***MAP1B*** (microtubule-associated protein 1B), 5q13.2. Encodes a large, neuron-enriched cytoskeletal protein synthesized as a polyprotein precursor cleaved into a ~300-kDa heavy chain and a 32-kDa light chain (LC1); it links and coordinates the microtubule and actin cytoskeletons and is heavily regulated by phosphorylation (GSK3β, DYRK1A, CDK5, casein kinase).

**Pathogenic variants (all heterozygous, germline, missense):**

| cDNA (NM_005909.4) | Protein | Domain | Family |
|---|---|---|---|
| c.4198A>G | p.Ser1400Gly | Microtubule-assembly-helping (MTA); conserved phospho-site | NB066 (Han Chinese, 3-gen, 7 affected) |
| c.2768T>C | p.Ile923Thr | Microtubule-binding region | Unrelated Chinese family |
| c.5512T>C | p.Phe1838Leu | Actin-binding region | Unrelated Chinese family |

- **Variant class:** Missense (single-nucleotide). No frameshift/nonsense/splice/structural variants cause DFNA83.
- **Classification (ACMG/AMP):** Reported as novel and pathogenic/likely pathogenic — supported by absence from population databases (PM2), cosegregation (PP1), and strong functional data (PS3, iPSC + CRISPR rescue + mouse).
- **Allele frequency:** Novel; effectively absent from gnomAD/1000 Genomes (consistent with PM2). Exact frequencies **not published**.
- **Origin:** Germline (inherited, autosomal dominant). Somatic origin not applicable.
- **Functional consequence:** **Partial / altered loss of function** — reduced MAP1B protein level and deficient phosphorylation, impairing microtubule stability/dynamics. Heterozygous-null mice phenocopy hearing loss, indicating dosage/haploinsufficiency sensitivity.

> *"the p.1400S>G mutation caused the reduced levels and deficient phosphorylation of MAP1B, which are involved in the microtubule stability and dynamics."* — PMID 33268592

**Genotype–phenotype dichotomy (pleiotropy):** *MAP1B* is a two-disease gene.
> *"loss-of-function (LOF) variants in MAP1B mainly lead to PVNH-related neurological symptoms, while patients with missense variants may only present with deafness."* — Zhou et al. 2025 ([PMID: 40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/))

Thus **missense → DFNA83 (isolated deafness)**; **truncating/LOF → periventricular nodular heterotopia 9 (PVNH9, OMIM #618918)** with developmental delay/intellectual disability, epilepsy, and anterior-predominant cortical malformation. Walters et al. 2018 (*Nat Commun* 9:3456) reported frameshift/nonsense *MAP1B* variants (c.2133delG p.Glu712LysfsTer10; c.3094G>T p.Glu1032Ter; c.4990C>T p.Arg1664Ter) that truncate the heavy chain and remove the C-terminal LC1 segment; PVNH9 shows incomplete penetrance/variable expressivity (further LOF families: PMID 40874586, 41468712).

**Modifier genes / epigenetics / chromosomal abnormalities:** None described for DFNA83. This is a point-mutation disorder; CMA/karyotype are not diagnostic.

---

## 5. Environmental Information

- **Environmental factors / toxins:** None causal. Noise and ototoxic agents are potential aggravators of high-frequency SNHL.
- **Lifestyle factors:** No established diet/smoking/alcohol association with DFNA83; noise-avoidance is prudent.
- **Infectious agents:** Not applicable — DFNA83 is genetic, non-infectious.

---

## 6. Mechanism / Pathophysiology

*(Ordered causal chain and branch diagram provided above in "Mechanistic Model / Interpretation.")*

### Detail by category
- **Molecular pathways:** Cytoskeletal regulation via **GSK3β / DYRK1A–mediated MAP1B phosphorylation** controlling microtubule assembly; MAP1B also bridges microtubules and actin in the growth cone. (Not a canonical Wnt/MAPK/mTOR disease.)
- **Cellular processes:** Neuronal cytoskeletal organization, axon outgrowth/guidance, neurite elongation, synaptic/electrophysiological maturation of auditory neurons. No prominent apoptosis/inflammation; cochlear morphology preserved.
- **Protein dysfunction:** Partial loss of function — reduced abundance + deficient phosphorylation → impaired microtubule-stabilizing activity.
- **Tissue damage mechanism:** Functional (neuronal dysfunction) rather than degenerative/necrotic; SGN electrophysiological defect drives the deficit.
- **Immune / metabolic / epigenetic involvement:** Not implicated.
- **Molecular profiling:** iPSC otic-neuron studies show decreased MAP1B mRNA/protein and impaired neurite outgrowth (PMID 33268592). No transcriptomic/proteomic/metabolomic disease signatures published.
- **Functional genomics:** CRISPR/Cas9 correction of the variant rescued the cellular phenotype — establishing causality.

> *"otic sensory neuron-like cells exhibited disturbed dynamics of microtubules, axonal elongation, and defects in electrophysiological properties"* — PMID 33268592

**Upstream vs downstream:** Mutation/phosphorylation defect (upstream) → microtubule instability → axon/electrophysiology defect → SGN dysfunction → hearing loss (downstream).

**Suggested GO / CL terms:** microtubule cytoskeleton organization **GO:0000226**; microtubule **GO:0005874**; axon development **GO:0061564**; axon guidance **GO:0007411**; neuron projection development **GO:0031175**; growth cone **GO:0030426**; protein phosphorylation **GO:0006468**. Cell type: spiral ganglion neuron (type I afferent; sensory neuron **CL:0000103**).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Inner ear / **cochlea** (UBERON:0001844); specifically the **spiral ganglion** (UBERON:0001681) and **cochlear (auditory) nerve** (UBERON:0001648). Body system: **nervous/auditory system**. No secondary organ involvement (nonsyndromic).
- **Tissue / cell level:** Nervous tissue — **spiral ganglion neurons** (type I afferent auditory neurons; **CL:0000103**). Cochlear hair cells (inner/outer) are **structurally spared** (mouse morphology normal; human DPOAE preserved).
- **Subcellular level:** **Microtubule cytoskeleton** (GO:0005874), **axon** (GO:0030424), **growth cone** (GO:0030426); cytoplasmic/neuronal-projection compartments.
- **Localization / laterality:** Bilateral (HP:0008619); high-frequency (cochlear base) predominant.

> *"MAP1B is highly expressed in the spiral ganglion neurons in the mouse cochlea"* — PMID 33268592

---

## 8. Temporal Development

- **Onset:** Post-lingual, late-onset — typically 2nd–3rd decade; insidious/chronic; variable age within families.
- **Progression:** Slowly progressive; sloping high-frequency configuration deepening over time; severity mild → profound with age.
- **Course:** Chronic, lifelong, non-episodic, non-remitting. Progressive (not fluctuating).
- **Critical periods / intervention window:** Ongoing — early detection, amplification/implantation, and avoidance of noise/ototoxins optimize outcomes. No spontaneous remission.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant**, heterozygous. Each child of an affected individual has a **50%** risk.
- **Penetrance:** High (cosegregation); not formally quantified. **Expressivity: variable.**
- **De novo / mosaicism:** De novo occurrence possible (consider with negative family history; PMID 37371710); germline mosaicism not reported.
- **Anticipation / founder effect / consanguinity:** Not applicable/observed (dominant; missense; unrelated families).
- **Carrier frequency:** Not applicable (dominant; variants ultra-rare/novel).
- **Epidemiology:** **Ultra-rare** — described only in **3 unrelated Chinese families**; no prevalence/incidence established. No sex predilection (autosomal). DFNA collectively ≈ **19%** of nonsyndromic hearing loss, with >50 genes/>80 loci (PMID 37371710).

> *"cosegregated with autosomal dominant inheritance of nonsyndromic sensorineural hearing loss in 3 unrelated Chinese families."* — PMID 33268592

> *"most patients diagnosed with autosomal dominant non-syndromic HL have a hearing-impaired parent, although de novo mutations should be considered in all cases of negative family history"* — PMID 37371710

---

## 10. Diagnostics

- **Audiometry:** Pure-tone audiometry — bilateral, sloping, high-frequency-predominant, progressive SNHL, post-lingual onset (the "audioprofile").
- **Otoacoustic emissions & ABR:** **Preserved DPOAE** (normal outer hair cell function) with abnormal ABR — an **auditory-neuropathy-like / retrocochlear pattern** consistent with SGN involvement.
- **Imaging:** Temporal-bone CT/MRI typically normal; used to exclude structural/retrocochlear lesions. No DFNA83-specific imaging biomarker.
- **Laboratory/biomarkers:** No blood/urine biomarker; diagnosis is audiologic + molecular.
- **Genetic testing (definitive):** Confirm a heterozygous *MAP1B* variant. Recommended: **multigene hereditary-hearing-loss NGS panel or exome sequencing** (WES); the original variants were found by WES. Single-gene *MAP1B* testing is low-yield given heterogeneity. WGS is an option; CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not** applicable.
- **Clinical criteria:** characteristic audioprofile + AD family history + heterozygous pathogenic *MAP1B* variant.
- **Differential diagnosis:** Other progressive high-frequency DFNA (KCNQ4/DFNA2, TECTA/DFNA8/12, ACTG1/DFNA20/26, MYO6/DFNA22, EYA4/DFNA10); **auditory-neuropathy** genes (OTOF, OPA1, DIAPH3, AIFM1); acquired causes — presbycusis, noise-induced hearing loss, ototoxicity.
- **Screening:** Newborn hearing screening may miss post-lingual DFNA83; **cascade genetic testing** of at-risk relatives once the familial variant is known.

> *"Using the whole exome sequencing approach, in combination with functional assays and a mouse disease model, we identified the potentially novel deafness-causative MAP1B gene"* — PMID 33268592

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No effect — normal life expectancy; not life-threatening; nonsyndromic.
- **Morbidity/disability:** Progressive communication disability; impact on education, employment, social function; potential association with isolation and late-life cognitive decline if untreated.
- **Disease course:** Chronic lifelong progression from mild toward severe/profound; no spontaneous recovery. With hearing aids/cochlear implants, functional hearing is generally maintainable.
- **Prognostic factors:** Age, degree of loss, specific variant, amplification/implant timing; adherence to noise/ototoxin avoidance. No molecular prognostic biomarker validated.
- **QoL measures:** EQ-5D, SF-36, PROMIS, HHIE (not DFNA83-specific).

> *"nonsyndromic sensorineural hearing loss"* — PMID 33268592

---

## 12. Treatment

No disease-modifying, gene-targeted, or pharmacologic cure exists. Management is **supportive/habilitative**, guided by severity and progression:

- **Amplification:** **Hearing aids** for mild–moderate loss — NCIT: Hearing Aid (**NCIT:C50076**).
- **Implantation:** **Cochlear implantation** for severe–profound loss — NCIT: Cochlear Implantation (**NCIT:C50236**). Because hair cells/organ of Corti are preserved and surviving SGNs are the CI target, CI is applicable; a purely neural component could theoretically temper outcomes (individualized counseling).
- **Rehabilitation/support:** Auditory rehabilitation, **speech-language therapy** (**NCIT:C15318**), educational support, assistive listening devices.
- **Genetic counseling:** **NCIT:C15220** — 50% recurrence risk; predictive testing of relatives; reproductive options.
- **Pharmacotherapy / advanced therapeutics:** None approved. No pharmacogenomic guidance. **Gene therapy, RNA therapy (ASO/siRNA), cell therapy, targeted/immunotherapy: not available** for *MAP1B*/DFNA83 (research-stage only). No registered DFNA83-specific clinical trials identified.
- **Surgical/interventional:** Cochlear implant surgery is the principal procedure; no other surgery indicated.

---

## 13. Prevention

- **Primary prevention:** Not possible (inherited monogenic disease).
- **Secondary prevention:** Early audiologic detection and intervention; **cascade genetic testing**; at least **annual audiograms** to catch progression; early amplification.
- **Tertiary prevention:** Hearing aids/cochlear implants; **avoid loud-noise and ototoxic exposures**; auditory rehabilitation.
- **Reproductive prevention:** Genetic counseling; **prenatal testing** and **preimplantation genetic testing** once the familial *MAP1B* variant is known.
- **Immunization / public-health / prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *MAP1B* is highly conserved. Mouse **Map1b** (NCBI Gene 17755; **MGI:1306778**; NCBI Taxon **10090**); *Drosophila* ortholog **futsch** (reflected in the human alias "FUTSCH"; NCBI Taxon 7227).
- **Natural disease in animals:** No naturally occurring *MAP1B*-associated deafness reported in companion animals/wildlife (OMIA) to date — DFNA83 models are engineered, not natural.
- **Comparative biology:** The mouse recapitulates human hearing loss (late-onset, progressive, high-frequency). Related family members **MAP2** and **MAP1A** also participate in cochlear function (Map2−/− mice: high-frequency ABR loss with basal OHC reduction), indicating an evolutionarily conserved MAP axis in auditory neurons/hair cells (MAP1A in inner hair cells, MAP1B in spiral ganglia, MAP2 in hair cells and SGN nerves).
- **Zoonosis / cross-species transmission:** Not applicable (genetic disease).

---

## 15. Model Organisms

- **In vivo (mammalian):** **Map1b heterozygous knockout mouse** (*Mus musculus*) — validated model; recapitulates **late-onset progressive SNHL, high-frequency predominant**, with SGN morphology/electrophysiology defects and **normal cochlear/hair-cell morphology** (PMID 33268592). Homozygous nulls are severely affected, so the **heterozygote** is the relevant DFNA83 model.
  > *"Involvement of MAP1B in hearing was confirmed by audiometric evaluation of Map1b heterozygous KO mice."* — PMID 33268592
  > *"These mutant mice displayed late-onset progressive sensorineural hearing loss that was more pronounced in the high frequencie[s]"* — PMID 33268592
- **In vitro (human):** **Patient iPSC-derived otic sensory neuron-like cells** carrying p.Ser1400Gly — reduced MAP1B, disturbed microtubule dynamics, impaired axonal elongation, electrophysiological defects; **rescued by CRISPR/Cas9 correction** (isogenic control).
  > *"Dysfunctions of these derived otic sensory neuron-like cells were rescued by genetically correcting MAP1B mutation using CRISPR/Cas9 technology."* — PMID 33268592
- **Invertebrate:** *Drosophila* **futsch** ortholog available for cytoskeletal/neuronal studies.
- **Model characteristics:** Strong recapitulation of the neural mechanism and audiometric phenotype; **limitations** — timing/severity differences between mouse and human, and human missense variants are not simple nulls (heterozygous-KO mouse approximates but does not perfectly model the missense biochemistry).
- **Resources:** MGI (Map1b MGI:1306778), IMPC/IMSR (mouse alleles), Cellosaurus (patient iPSC lines), FlyBase (futsch).

---

## Evidence Base

| PMID | Study | Type | Contribution |
|---|---|---|---|
| [33268592](https://pubmed.ncbi.nlm.nih.gov/33268592/) | Cui et al. 2020, *JCI Insight* | Human genetics + iPSC + mouse | **Foundational.** Discovery of *MAP1B*/DFNA83; three variants; SGN mechanism; CRISPR rescue; mouse recapitulation |
| [40802165](https://pubmed.ncbi.nlm.nih.gov/40802165/) | Zhou et al. 2025 | Human genetics review | Genotype–phenotype dichotomy (missense→deafness; LOF→PVNH9) |
| [37371710](https://pubmed.ncbi.nlm.nih.gov/37371710/) | Aldè et al. 2023 | Clinical review | DFNA epidemiology, phenotype, management, counseling |
| [40874586](https://pubmed.ncbi.nlm.nih.gov/40874586/) | 2025 | Human clinical | *MAP1B* LOF → PVNH neurodevelopmental phenotype (pleiotropy context) |
| Walters et al. 2018, *Nat Commun* 9:3456 | | Human genetics | PVNH9 truncating-variant spectrum (LC1 deletion) anchoring the pleiotropy contrast |

**How the evidence coheres:** A single landmark paper (PMID 33268592) supplies three converging lines of evidence — human cosegregation across three families, functional iPSC assays with CRISPR rescue (establishing causality, not merely association), and an independent mouse model — an unusually strong package for an ultra-rare disorder. The genotype–phenotype literature (PMIDs 40802165, 40874586) independently anchors the interpretation that missense variants act via partial loss of a cytoskeletal function selectively critical in spiral ganglion neurons, whereas complete loss of function disrupts cortical neuronal migration.

---

## Limitations & Knowledge Gaps

- **Very limited human data** (3 families, one core discovery paper) → prevalence, penetrance, natural history, and cochlear-implant outcomes are unquantified.
- **No independent replication cohort** — the full allelic spectrum and any founder effects remain undefined.
- **Population/ClinVar status** of the three variants (exact gnomAD frequencies, expert classification) not yet publicly detailed.
- **Mechanistic gaps:** why SGNs are selectively vulnerable to missense (vs cortical neurons in LOF); whether variants are hypomorphic vs subtly dominant-negative. The mouse is a heterozygous *knockout* (haploinsufficiency), which may not perfectly model missense biochemistry.
- **Audiologic profiling** (DPOAE-preserved/ABR-abnormal) is inferred from mouse histology and general DFNA principles; systematic human OAE/electrocochleography data are undocumented.
- **No MONDO ID** confirmed here; ontology cross-references should be verified against current releases.

---

## Proposed Follow-up Experiments / Actions

1. **International case ascertainment** via GeneMatcher, DECIPHER, and large deafness exome/biobank cohorts to expand the allelic spectrum and estimate penetrance.
2. **Deep audiologic phenotyping** of carriers (serial PTA, DPOAE, ABR/electrocochleography) to test the predicted preserved-OHC/abnormal-neural signature and quantify progression rate.
3. **Mechanistic disambiguation** — knock-in missense mouse/iPSC models vs heterozygous null to distinguish haploinsufficiency from dominant-negative effects.
4. **Domain-resolved variant-effect mapping** across ABD/MBD/MTA missense substitutions to strengthen ACMG PS3 evidence.
5. **Cochlear implant outcome study** in DFNA83 recipients to determine whether SGN-level pathology attenuates CI benefit.
6. **Therapeutic exploration** — given reversibility by CRISPR correction, test modulation of MAP1B phosphorylation (GSK3β/DYRK1A) or microtubule-stabilizing agents in preclinical SGN models.
7. **Ontology curation** — assign/verify a MONDO ID and finalize HPO/CL/UBERON annotations for knowledge-base ingestion.

---

*Prepared as an autonomous scientific discovery report. Evidence is dominated by a single foundational study (PMID 33268592) supplemented by DFNA and MAP1B genotype–phenotype reviews; all mechanistic and clinical claims are cited to primary/authoritative literature with verified abstract quotes.*


## Artifacts

- [OpenScientist final report](Hearing_Loss_Autosomal_Dominant_83-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hearing_Loss_Autosomal_Dominant_83-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 10 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0005874` (3 mentions) - the report calls it "Microtubule cytoskeleton", "Subcellular level:** **Microtubule cytoskeleton"; GO calls it **microtubule**
- `UBERON:0001681` (2 mentions) - the report calls it "spiral ganglion"; UBERON calls it **nasal bone**
- `HP:0000407` (2 mentions) - the report calls it "SNHL"; HP calls it **Sensorineural hearing impairment**
- `HP:0006385` (2 mentions) - the report calls it "high-frequency HL"; HP calls it **Short lower limbs**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001730` (2 mentions) - the report calls it "progressive"; HP calls it **Progressive hearing impairment**, and lists "Progressive hearing loss" among its other names
- `HP:0008619` (2 mentions) - the report calls it "Localization / laterality:** Bilateral"; HP calls it **Bilateral sensorineural hearing impairment**, and lists "Hearing loss, sensorineural, bilateral" among its other names
- `UBERON:0001648` (1 mention) - the report calls it "cochlear (auditory) nerve"; UBERON calls it **vestibulocochlear nerve**, and lists "cochlear-vestibular nerve" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0005874` - called "Microtubule cytoskeleton", "Subcellular level:** **Microtubule cytoskeleton"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.
