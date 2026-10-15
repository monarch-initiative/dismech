---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-02T05:29:47.425226'
end_time: '2026-09-02T05:49:09.086146'
duration_seconds: 1161.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Visceral Heterotaxy 9
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 31
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0030070
    reported_labels:
    - MONDO
    ontology_label: heterotaxy, visceral, 9, autosomal, with male infertility
  - term_id: HP:0011885
    reported_labels:
    - Abnormal visceral situs
    ontology_label: Hemorrhage of the eye
  - term_id: UBERON:0004341
    reported_labels:
    - "left\u2013right organizer / node"
    ontology_label: primitive streak
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Visceral_Heterotaxy_9-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Visceral_Heterotaxy_9-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Visceral Heterotaxy 9
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Visceral Heterotaxy 9** covering all of the
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

# Visceral Heterotaxy 9 (HTX9): A Comprehensive Disease Characterization Report

**Disease:** Visceral Heterotaxy 9 (HTX9)
**OMIM:** #618948 · **MONDO:** MONDO:0030070 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *MNS1* (Meiosis-specific nuclear structural protein 1; HGNC:29636; 15q21.3)

---

## Summary

**Visceral heterotaxy 9 (HTX9) is a rare autosomal-recessive disorder of left–right (L–R) body-axis determination caused by biallelic loss-of-function (LOF) variants in *MNS1*.** MNS1 is a 495–amino-acid coiled-coil microtubule inner protein (MIP) that decorates the doublet microtubules of motile cilia and sperm flagella and supports docking of the outer dynein arms (ODAs) through interaction with the ODA docking-complex (ODA-DC) component CCDC114/ODAD1. When both *MNS1* alleles are inactivated, the motile monocilia of the embryonic node cannot generate the directional leftward fluid flow that normally breaks embryonic symmetry. The consequence is **randomization of situs** — affected individuals may present with situs solitus (normal), situs inversus totalis, or situs ambiguus/heterotaxy — accompanied by **male infertility** (immotile, structurally abnormal sperm) and, variably, sinopulmonary disease reminiscent of primary ciliary dyskinesia (PCD).

The disease is defined by a small human evidence base: two independent studies describing fewer than ~10 affected individuals from consanguineous and founder (Old Order Amish) families ([PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/); [PMID: 31534215](https://pubmed.ncbi.nlm.nih.gov/31534215/)), supported by a foundational *Mns1*-knockout mouse that recapitulates situs inversus, hydrocephalus, male sterility, and axonemal ODA/"9+2" defects ([PMID: 22396656](https://pubmed.ncbi.nlm.nih.gov/22396656/)). Population-database analysis (gnomAD v4) confirms that *MNS1* is tolerant of heterozygous LOF (consistent with a recessive mechanism in which carriers are unaffected) and that the reported pathogenic alleles are rare, with a recurrent p.Arg242* nonsense allele and a near-private Amish founder frameshift.

HTX9 sits within the **motile-ciliopathy / heterotaxy spectrum**. Its clinical burden is driven not by the laterality label itself but by the associated congenital heart disease (when present in heterotaxy) and by fertility consequences. There is **no disease-specific pharmacologic or gene therapy**; management is supportive and organ-directed (cardiac surgical palliation, treatment of respiratory infection, assisted reproduction for male infertility, genetic counseling). This report synthesizes six confirmed findings across 31 reviewed papers and details each of the 15 requested characterization domains, flagging where evidence is absent.

---

## Key Findings

### Finding 1 — HTX9 is caused by biallelic loss-of-function variants in *MNS1*

Two independent human genetic studies converge on recessive *MNS1* LOF as the cause of HTX9. Ta-Shma et al. (2018) identified two recessive LOF *MNS1* mutations across four consanguineous families: a homozygous nonsense mutation **p.Arg242\*** in four males with laterality defects and infertility, and a homozygous nonsense mutation **p.Gln203\*** in one female with laterality defects and recurrent respiratory infections. As the authors state, *"we identified two recessive loss-of-function MNS1 mutations in five individuals from four consanguineous families: 1) a homozygous nonsense mutation p.Arg242\* in four males with laterality defects and infertility and 2) a homozygous nonsense mutation p.Gln203\* in one female with laterality defects and recurrent respiratory infections additionally carrying homozygous mutations in DNAH5"* ([PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/)).

Leslie et al. (2020) independently confirmed the locus in an Old Order Amish family, mapping a single 2.34 Mb region of autozygosity to 15q21.3 and identifying a homozygous frameshift variant: *"This identified a single shared (2.34 Mb) region of autozygosity on chromosome 15q21.3 as the likely disease locus, in which we identified a single candidate biallelic frameshift variant in MNS1 [NM_018365.2: c.407_410del; p.(Glu136Glyfs\*16)]"* ([PMID: 31534215](https://pubmed.ncbi.nlm.nih.gov/31534215/)). *MNS1* encodes Meiosis-specific nuclear structural protein 1 (**HGNC:29636**, chromosome **15q21.3**).

### Finding 2 — MNS1 is an axonemal protein that docks outer dynein arms via CCDC114; its loss causes ODA defects

MNS1 localizes to motile-cilia and flagellar axonemes and physically engages the ODA docking machinery. Ta-Shma et al. showed that *"Immunofluorescence analysis further revealed that MNS1 localizes to the axonemes of respiratory cilia as well as sperm flagella in human"* and that *"co-immunoprecipitation and yeast two hybrid analyses demonstrated that MNS1 dimerizes and interacts with the ODA docking complex component CCDC114"* ([PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/)). Ultrastructural analysis of patient cilia showed a subtle ODA defect resembling that of *Mns1*-deficient mice. This positions MNS1 within the same functional module as established ODA-DC PCD genes (CCDC114/ODAD1, CCDC151, ARMC4, TTC25) — a module whose disruption is a common cause of PCD with laterality randomization ([PMID: 25192045](https://pubmed.ncbi.nlm.nih.gov/25192045/), [PMID: 27486780](https://pubmed.ncbi.nlm.nih.gov/27486780/)).

### Finding 3 — Laterality is randomized, penetrance is incomplete, and the phenotype is milder than classic heterotaxy

A hallmark of HTX9 is *randomized* rather than uniformly inverted situs. In the Amish pedigree, *"Genotyping of multiple family members identified randomisation of the laterality defects in other homozygous individuals, with all wild type or MNS1 c.407_410del heterozygous carriers being unaffected, consistent with an autosomal recessive mode of inheritance"* ([PMID: 31534215](https://pubmed.ncbi.nlm.nih.gov/31534215/)). Thus homozygotes may show situs inversus totalis, situs ambiguus/heterotaxy, or even situs solitus, while heterozygous carriers are clinically normal. The affected phenotype centers on situs abnormality plus male infertility, with variable respiratory infection. The total reported human cohort remains fewer than ~10 individuals, all from consanguineous or founder backgrounds — a key caveat when generalizing severity.

### Finding 4 — The *Mns1*-knockout mouse recapitulates HTX9 and extends the phenotype

Zhou et al. (2012) generated the foundational mouse model, demonstrating that MNS1 is an integral axonemal component: *"MNS1 is expressed in the germ cells in the testes and localizes to sperm flagella in a detergent-resistant manner, indicating that it is an integral component of flagella"* ([PMID: 22396656](https://pubmed.ncbi.nlm.nih.gov/22396656/)). MNS1-deficient males are sterile with markedly reduced sperm production and immotile, short-tailed sperm. The model recapitulates the human laterality defect and reveals additional features: *"In MNS1-deficient sperm flagella, the characteristic arrangement of '9+2' microtubules and outer dense fibers are completely disrupted. In addition, MNS1-deficient mice display situs inversus and hydrocephalus. MNS1-deficient tracheal motile cilia lack some outer dynein arms in the axoneme"* ([PMID: 22396656](https://pubmed.ncbi.nlm.nih.gov/22396656/)). Hydrocephalus (from ependymal motile-cilia dysfunction) is demonstrated in mouse but not yet firmly established as a human HTX9 feature. Mouse *Mns1* = **NCBI Gene 17427**.

### Finding 5 — gnomAD confirms recessive constraint and rarity of pathogenic alleles

gnomAD v4 constraint metrics for *MNS1* (ENSG00000138587; chr15:56,421,544–56,465,137) show the gene is **not depleted of heterozygous LOF**: pLI ≈ 0 (3.6e-19), observed/expected LoF (oe_lof) = 0.875 (90% CI 0.714–1.079; LOEUF ≈ 1.08), lof_z = 0.90. This is exactly the signature expected for a recessive disease gene where a single functional allele suffices for health. The reported pathogenic alleles are rare in gnomAD v4 exomes: **p.Arg242Ter (c.724C>T)** AC=253/AN=1,453,772 (AF ≈ 1.74×10⁻⁴; a recurrent nonsense allele); **p.Gln203Ter (c.607C>T)** AC=7 (AF ≈ 4.8×10⁻⁶); and the **Amish founder p.Glu136GlyfsTer16 (c.407_410del)** AC=2/AN=1,458,458 (AF ≈ 1.37×10⁻⁶, near-private). All appear only as rare heterozygotes.

### Finding 6 — MNS1 is a 495-aa coiled-coil microtubule inner protein with a TPH domain

UniProt **Q8NEH6** (human MNS1, 495 aa) describes a large coiled-coil region (residues ~28–410) and a **Trichohyalin-Plectin-Homology (TPH) domain** (~114–465; Pfam **PF13868** "TPH"; InterPro **IPR043597**; MNS1 family InterPro **IPR026504**; PANTHER **PTHR19265**). Functionally, MNS1 is annotated as a **microtubule inner protein (MIP)** of the dynein-decorated doublet microtubules (DMTs) of the ciliary/flagellar axoneme, required for motile-cilia beating and sperm-flagella assembly. Subcellular localization: nucleus, cilium axoneme, flagellum axoneme. It forms oligomers and interacts with ODAD1 (=CCDC114), BBOF1, and CFAP65; tissue specificity is nasal respiratory epithelium and sperm. The self-oligomerization and CCDC114 interaction are experimentally supported: *"co-immunoprecipitation and yeast two hybrid analyses demonstrated that MNS1 dimerizes and interacts with the ODA docking complex component CCDC114"* ([PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/)).

---

## Detailed Disease Characterization (Sections 1–15)

### 1. Disease Information

HTX9 is a Mendelian disorder of visceral laterality (left–right asymmetry) within the motile-ciliopathy spectrum. Affected individuals fail to establish normal L–R patterning during early embryogenesis, producing situs abnormalities and, in males, infertility.

| Identifier type | Value |
|---|---|
| Disease name | Visceral Heterotaxy 9 (HTX9) |
| OMIM | #618948 |
| MONDO | MONDO:0030070 |
| Causal gene | *MNS1* (OMIM *610766) |
| ICD-10 | Q89.3 (Situs inversus) — closest applicable code |
| ICD-11 | LB20.0 / relevant congenital malformation of laterality codes |
| MeSH | Heterotaxy Syndrome (D059446); Situs Inversus (D012857) |

**Synonyms / related terms:** heterotaxy visceral 9, autosomal recessive; MNS1-related laterality defect; situs inversus with male infertility (MNS1). The disease-level information is **aggregated** from case reports/family studies and a mouse model — not from EHR/individual-patient registries.

### 2. Etiology

- **Primary cause (genetic):** biallelic (homozygous or compound-heterozygous) loss-of-function variants in *MNS1* (Findings 1, 5). Mechanism is loss of function via nonsense/frameshift alleles producing truncated, non-functional protein.
- **Genetic risk factors:** the causal locus is *MNS1*; carrier (heterozygous) state confers no disease risk. **Consanguinity** and **founder-population** membership (Old Order Amish) are the dominant risk contexts because they raise homozygosity for rare recessive alleles.
- **Environmental risk factors:** none established. No toxin, infection, or lifestyle factor is implicated in HTX9 causation.
- **Protective factors:** a single functional *MNS1* allele is fully protective (recessive; gnomAD LOF tolerance, Finding 5). No specific protective modifier alleles are described.
- **Gene–environment interactions:** none documented. In one patient, co-occurring homozygous *DNAH5* mutations were noted ([PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/)), illustrating potential **oligogenic contribution** within the shared ciliary pathway rather than a G×E effect.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset | Frequency / notes |
|---|---|---|---|---|
| Situs inversus totalis | Physical malformation | HP:0001696 (Situs inversus totalis) | Congenital | One of the randomized outcomes |
| Situs ambiguus / heterotaxy | Physical malformation | HP:0011885 (Abnormal visceral situs) | Congenital | Randomized outcome |
| Abnormal cardiac/great-vessel laterality (CHD) | Clinical sign | HP:0030680 (Abnormal cardiovascular morphology) | Congenital | When heterotaxy present |
| Male infertility | Clinical/laboratory | HP:0003251 (Male infertility) | Adult (reproductive) | Consistent in affected males |
| Abnormal sperm motility | Laboratory | HP:0012207 (Abnormal sperm motility) | Adult | Immotile, short-tailed sperm (mouse-confirmed) |
| Recurrent respiratory infections | Clinical sign | HP:0002205 (Recurrent respiratory infections) | Childhood, variable | Variable; PCD-like |
| Hydrocephalus | Clinical sign | HP:0000238 (Hydrocephalus) | Congenital/neonatal | **Mouse-demonstrated; not confirmed human** |

**Characteristics:** onset is **congenital** for laterality/cardiac features and reproductive-age for infertility. **Severity is variable** and strongly dependent on the presence and type of congenital heart disease. **Progression** of the laterality trait itself is **stable** (a fixed structural condition), though associated CHD and infections drive morbidity over time. **Quality-of-life impact** is dominated by cardiac disease (surgical burden) and infertility; individuals with situs inversus totalis and no CHD may be minimally affected.

### 4. Genetic / Molecular Information

- **Causal gene:** *MNS1* (HGNC:29636; OMIM *610766; 15q21.3; NCBI Gene 55329; Ensembl ENSG00000138587; UniProt Q8NEH6).
- **Pathogenic variants (all germline, LOF):**

| Variant (protein) | cDNA | Type | Population | gnomAD v4 AF | Reference |
|---|---|---|---|---|---|
| p.Arg242* | c.724C>T | Nonsense | Consanguineous | 1.74×10⁻⁴ | [PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/) |
| p.Gln203* | c.607C>T | Nonsense | Consanguineous | 4.8×10⁻⁶ | [PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/) |
| p.Glu136Glyfs*16 | c.407_410del | Frameshift | Amish founder | 1.37×10⁻⁶ | [PMID: 31534215](https://pubmed.ncbi.nlm.nih.gov/31534215/) |

- **ACMG classification:** all three are LOF (nonsense/frameshift) variants meeting pathogenic criteria (PVS1 + segregation + rarity).
- **Functional consequence:** loss of function (premature termination / truncated protein lacking the C-terminal region needed for axonemal assembly and ODA-DC interaction).
- **Modifier genes:** possible oligogenic contribution from co-inherited ciliary-gene variants (e.g., *DNAH5* in one case, [PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/)). No formal modifier-gene mapping exists.
- **Epigenetic information:** none reported for HTX9.
- **Chromosomal abnormalities:** none — HTX9 is a single-gene disorder, not a copy-number/aneuploidy syndrome. (Note: unrelated heterotaxy cases involve CNVs at other loci, [PMID: 29843777](https://pubmed.ncbi.nlm.nih.gov/29843777/).)

### 5. Environmental Information

No environmental, lifestyle, or infectious agents are implicated in causing HTX9. This is a purely genetic Mendelian disorder. (Recurrent respiratory infections in some patients are a *consequence* of impaired mucociliary clearance, not a cause.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic LOF variant in *MNS1* (nonsense/frameshift) → **leads to** loss of full-length MNS1 protein (loss of function). *(demonstrated — Findings 1, 5)*
2. Loss of MNS1 → **results in** failure to properly assemble/stabilize the doublet-microtubule inner scaffold and to dock outer dynein arms via CCDC114/ODAD1. *(demonstrated by co-IP/Y2H and TEM — Findings 2, 6)*
3. Defective ODA docking → **leads to** reduced/absent axonemal outer dynein arms and impaired motor force generation. *(demonstrated in human cilia and mouse trachea — Findings 2, 4)*
4a. In **embryonic nodal monocilia**: impaired beating → **fails to generate** directional leftward nodal flow → **fails to break** L–R symmetry → **results in** randomized situs (solitus / inversus / ambiguus). *(inferred from ODA-DC ciliopathy paradigm + mouse situs inversus — Findings 3, 4)*
5a. Randomized cardiac/visceral situs → **can result in** congenital heart disease and malposition of thoraco-abdominal organs. *(clinical)*
4b. In **sperm flagella**: loss of MNS1 → **disrupts** the "9+2" axoneme and outer dense fibers → **results in** immotile, structurally abnormal sperm → **male infertility**. *(demonstrated in mouse — Finding 4)*
4c. In **ependymal/respiratory motile cilia**: ODA loss → impaired mucociliary clearance → recurrent respiratory infection (human, variable) and → hydrocephalus (mouse-demonstrated, human-inferred). *(Finding 4)*

**Upstream** events: the *MNS1* mutation and protein loss. **Downstream:** organ-level malformations and functional deficits. The branch point is the **cell type** in which the defective motile cilium/flagellum operates (node vs. sperm vs. ependyma/airway).

- **Molecular pathways / complexes:** axonemal dynein assembly and docking (ODA-DC module: MNS1–CCDC114/ODAD1–CCDC151–ARMC4–TTC25). GO biological processes: **GO:0003341** (cilium movement), **GO:0060287** (epithelial cilium movement involved in determination of L–R asymmetry), **GO:0007368** (determination of L–R symmetry), **GO:0036158** (outer dynein arm assembly), **GO:0030317** (flagellated sperm motility).
- **Cellular processes:** motile ciliary beating, ciliogenesis, spermiogenesis, mucociliary clearance.
- **Protein dysfunction:** loss of function of a coiled-coil MIP (Q8NEH6); truncation abolishes axonemal incorporation.
- **Cell types (CL):** ciliated node cell / embryonic monociliated node cell; **CL:0000064** (ciliated cell); **CL:0002145** (ciliated columnar cell of tracheobronchial tree); **CL:0000019** (sperm); ependymal cell **CL:0000065**.
- **Immune / metabolic / autoimmune involvement:** none intrinsic; respiratory infections are secondary to impaired clearance.

### 7. Anatomical Structures Affected

- **Primary organs / systems:** cardiovascular system (heart UBERON:0000948, great vessels), abdominal viscera (spleen UBERON:0002106, liver UBERON:0002107, stomach UBERON:0000945, intestine), lungs/airway (UBERON:0002048), male reproductive tract (testis UBERON:0000473; sperm flagellum). The embryonic **left–right organizer / node** (UBERON:0004341) is the initiating site.
- **Secondary involvement:** brain ventricular system (hydrocephalus — mouse); recurrent airway infection.
- **Tissue/cell level:** motile ciliated epithelium (respiratory, ependymal), nodal monociliated cells, spermatozoa.
- **Subcellular (GO cellular component):** ciliary axoneme **GO:0005930**, motile cilium **GO:0031514**, sperm flagellum **GO:0036126**, axonemal microtubule **GO:0005879**, outer dynein arm **GO:0036157**, nucleus **GO:0005634**.
- **Lateralization:** by definition an abnormality of **left–right asymmetry**; situs may be fully mirror-imaged (situs inversus totalis) or discordant/asymmetric across organs (situs ambiguus/heterotaxy).

### 8. Temporal Development

- **Onset:** laterality and cardiac features are **congenital** (determined in early embryogenesis at the L–R organizer). Infertility manifests at reproductive age. Respiratory symptoms, when present, typically begin in childhood.
- **Progression:** the laterality trait is **structurally fixed and stable**. Clinical course is dominated by associated CHD (may require staged surgical palliation) and by recurrent infections; both can be progressive if untreated. Disease is **lifelong**.
- **Critical period:** the **narrow embryonic window** of nodal flow / symmetry breaking (gastrulation/early somitogenesis) is when the primary lesion acts — there is no postnatal opportunity to alter situs.
- **Remission:** not applicable to the structural defect.

### 9. Inheritance and Population

- **Inheritance:** **autosomal recessive** (biallelic LOF; unaffected heterozygous carriers — Findings 1, 3, 5).
- **Penetrance / expressivity:** the *situs* phenotype shows **incomplete/randomized penetrance** — homozygotes may be situs solitus, inversus, or ambiguus (Finding 3). Male infertility appears more consistently penetrant. Expressivity is **variable**.
- **Founder effect:** yes — the **p.Glu136Glyfs\*16** allele is an Old Order Amish founder variant ([PMID: 31534215](https://pubmed.ncbi.nlm.nih.gov/31534215/)). **Consanguinity** underlies the other reported families ([PMID: 30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/)).
- **Carrier frequency:** rare in general populations; p.Arg242* is the most common pathogenic allele (gnomAD AF ≈1.74×10⁻⁴), others near-private (Finding 5).
- **Epidemiology:** true prevalence/incidence of HTX9 specifically is **unknown** (fewer than ~10 published individuals). For context, all-cause heterotaxy affects roughly 1 in 10,000 births and is enriched in congenital heart disease cohorts; PCD (the broader motile-ciliopathy class) is estimated at ~1 in 10,000–20,000.
- **Sex ratio:** both sexes affected for laterality; the infertility phenotype is male-specific by nature. Reported cases skew male because infertility prompted ascertainment.
- **No genetic anticipation** (not a repeat-expansion disorder). Germline mosaicism not reported.

### 10. Diagnostics

- **Clinical/imaging:** situs is established by **echocardiography, chest radiography, abdominal ultrasound, CT/MRI** documenting cardiac position, atrial appendage morphology, spleen status (asplenia/polysplenia), and vessel anatomy. Prenatal ultrasound can detect heterotaxy features ([PMID: 37485264](https://pubmed.ncbi.nlm.nih.gov/37485264/), [PMID: 35518361](https://pubmed.ncbi.nlm.nih.gov/35518361/)).
- **Semen analysis:** asthenozoospermia / immotile sperm in affected males.
- **Ciliary studies:** **nasal nitric oxide (nNO)**, high-speed video microscopy, and transmission electron microscopy (TEM) may show ODA/ODA-DC abnormalities; immunofluorescence for ODA-DC components. These PCD workups are relevant where a PCD-like presentation exists ([PMID: 24577564](https://pubmed.ncbi.nlm.nih.gov/24577564/)).
- **Genetic testing (definitive):** **whole-exome or whole-genome sequencing**, or **PCD/heterotaxy/laterality gene panels** that include *MNS1*; single-gene testing where a founder allele is suspected (e.g., Amish p.Glu136Glyfs*16). Homozygosity mapping is powerful in consanguineous/founder families (used in both index studies). WES is high-yield in genetically heterogeneous PCD ([PMID: 41948467](https://pubmed.ncbi.nlm.nih.gov/41948467/)).
- **Differential diagnosis:** other heterotaxy/PCD genes — *DNAH5, DNAH11, CCDC114/ODAD1, CCDC151, ARMC4, TTC25, ZIC3, NODAL, LEFTY, CFC1, SHROOM3, WDR16* — distinguished by gene identified and by presence/absence of classic PCD airway disease ([PMID: 31040315](https://pubmed.ncbi.nlm.nih.gov/31040315/), [PMID: 27486780](https://pubmed.ncbi.nlm.nih.gov/27486780/), [PMID: 25192045](https://pubmed.ncbi.nlm.nih.gov/25192045/), [PMID: 21936905](https://pubmed.ncbi.nlm.nih.gov/21936905/), [PMID: 25469542](https://pubmed.ncbi.nlm.nih.gov/25469542/)).

### 11. Outcome / Prognosis

- **Prognosis is determined by associated congenital heart disease.** Isolated situs inversus totalis without structural heart disease carries near-normal life expectancy. Heterotaxy with complex CHD (single-ventricle physiology, anomalous pulmonary venous connection, atrioventricular septal defect) carries substantial morbidity and mortality despite surgery. Large heterotaxy cohorts report overall mortality around 40% with limited improvement over decades, and worst outcomes for univentricular circulation with totally anomalous pulmonary venous connection ([PMID: 32647064](https://pubmed.ncbi.nlm.nih.gov/32647064/)).
- **Male infertility:** effectively complete for natural conception; assisted reproduction (ICSI) may be considered.
- **Respiratory morbidity:** where a PCD-like phenotype exists, chronic sinopulmonary infection and bronchiectasis risk apply.
- **Complications:** arrhythmia and heterotaxy-associated surgical risk ([PMID: 41404994](https://pubmed.ncbi.nlm.nih.gov/41404994/)), intestinal malrotation/volvulus risk (Ladd-procedure considerations, [PMID: 36941169](https://pubmed.ncbi.nlm.nih.gov/36941169/)), asplenia-related infection risk.
- **Prognostic factors:** ventricular morphology, pulmonary venous anatomy, spleen status, era of care.

### 12. Treatment

There is **no disease-specific or curative therapy** for HTX9; management is **supportive and organ-directed**.

| Domain | Intervention | NCIT-type term |
|---|---|---|
| Cardiac | Staged surgical palliation (single-ventricle → Fontan), CHD repair, pacemaker for bradyarrhythmia | Cardiac surgical procedure |
| Gastrointestinal | Ladd procedure for malrotation (selective) | Surgical intervention |
| Respiratory | Airway clearance, antibiotics for infections/bronchiectasis (PCD-style management) | Supportive care |
| Infection prophylaxis | Vaccination/antibiotics in asplenia | Antimicrobial prophylaxis |
| Fertility | Assisted reproduction / ICSI | Assisted reproductive technology |
| Genetics | Genetic counseling | Genetic counseling |

- **Pharmacotherapy / pharmacogenomics:** none specific to HTX9.
- **Gene, cell, RNA, targeted, or immunotherapy:** none approved or in trials for HTX9. PCD gene therapy is an emerging general research direction, not HTX9-specific ([PMID: 42135132](https://pubmed.ncbi.nlm.nih.gov/42135132/)).
- **Personalized medicine:** genotype confirmation guides counseling and reproductive planning rather than drug selection.

### 13. Prevention

- **Primary prevention:** not possible for the genetic lesion; **genetic counseling** and **carrier/cascade testing** in affected families (especially founder Amish and consanguineous kindreds) inform reproductive decisions. **Preimplantation genetic testing** and **prenatal diagnosis** are options for known familial variants.
- **Secondary prevention:** prenatal ultrasound/fetal echocardiography for early detection of heterotaxy/CHD; postnatal imaging screening.
- **Tertiary prevention:** management of asplenia (vaccination, antibiotic prophylaxis), surveillance and timely surgery for CHD, aggressive treatment of respiratory infection to prevent bronchiectasis, consideration of prophylactic Ladd procedure where indicated.
- **Immunization / public health / environmental measures:** not applicable to disease causation.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *Mns1* is conserved in mouse (**NCBI Gene 17427**, *Mus musculus*, NCBI:txid10090) and other vertebrates. The mouse ortholog provides the principal experimental model (Finding 4).
- **Natural disease in other species:** no naturally occurring companion-animal or wildlife *MNS1* disease is catalogued in OMIA at review time; the mouse phenotype is engineered, not spontaneous.
- **Comparative biology:** the L–R symmetry-breaking role of motile nodal cilia and the ODA-DC machinery is deeply conserved across vertebrates (mouse, zebrafish), which is why ODA-DC gene defects (e.g., CCDC151, TTC25) produce situs defects across species ([PMID: 25192045](https://pubmed.ncbi.nlm.nih.gov/25192045/), [PMID: 27486780](https://pubmed.ncbi.nlm.nih.gov/27486780/)).
- **Zoonotic potential:** none (genetic disease).

### 15. Model Organisms

- **Principal model — mouse (*Mus musculus*):** the **Mns1-knockout** recapitulates HTX9's core features — situs inversus, hydrocephalus, male sterility with disrupted "9+2" axoneme and outer dense fibers, and tracheal ODA loss ([PMID: 22396656](https://pubmed.ncbi.nlm.nih.gov/22396656/)). This is a **high-fidelity model** for the ciliary/flagellar mechanism and laterality randomization.
- **Model type:** mammalian genetic knockout (constitutive LOF).
- **Phenotype recapitulation:** strong for laterality, sperm ultrastructure/infertility, and ODA defects; the model additionally reveals **hydrocephalus**, well-established in mouse but not yet confirmed as a human HTX9 feature.
- **Limitations:** mouse cannot fully model the variable human sinopulmonary/CHD spectrum; incomplete penetrance/randomization means large cohorts are needed to quantify situs outcomes.
- **Complementary systems:** zebrafish and *Xenopus* are established platforms for heterotaxy-candidate-gene testing generally ([PMID: 26910255](https://pubmed.ncbi.nlm.nih.gov/26910255/)); ODA-DC pathway partners have been modeled in zebrafish/mouse ([PMID: 25192045](https://pubmed.ncbi.nlm.nih.gov/25192045/), [PMID: 27486780](https://pubmed.ncbi.nlm.nih.gov/27486780/)). Resources: MGI, IMPC/KOMP, IMSR.

---

## Mechanistic Model / Interpretation

```
   MNS1 biallelic LOF variant (p.Arg242*, p.Gln203*, p.Glu136Glyfs*16)
                     │  (loss of function; demonstrated)
                     ▼
       Loss of full-length MNS1 (coiled-coil / TPH-domain MIP)
                     │  (microtubule inner protein of axonemal doublets)
                     ▼
   Failed doublet-MT stabilization + failed ODA docking via CCDC114/ODAD1
                     │  (co-IP/Y2H + TEM; demonstrated)
                     ▼
        Reduced / absent axonemal outer dynein arms → weak motor force
                     │
        ┌────────────┼───────────────────────────┐
        ▼            ▼                             ▼
  NODAL MONOCILIA   SPERM FLAGELLUM          RESPIRATORY / EPENDYMAL CILIA
  no leftward       disrupted "9+2" +        impaired mucociliary clearance
  nodal flow        outer dense fibers        │
        │            │                        ├── recurrent airway infection (human, variable)
        ▼            ▼                        └── hydrocephalus (mouse; inferred human)
  RANDOMIZED       IMMOTILE SPERM →
  SITUS            MALE INFERTILITY
  (solitus /
   inversus /
   ambiguus)
        │
        ▼
  CONGENITAL HEART DISEASE / organ malposition (when heterotaxy)
```

The unifying interpretation is that HTX9 is a **cell-type-branched motile ciliopathy**: a single molecular lesion (loss of an axonemal microtubule inner protein) produces divergent organ phenotypes depending on which motile cilium/flagellum fails. The *randomization* of situs — rather than uniform inversion — is the diagnostic signature and reflects loss of the deterministic leftward nodal flow, leaving L–R identity to chance. MNS1 belongs functionally alongside the ODA-DC PCD genes, which explains both the ODA ultrastructural defect and the PCD-like respiratory features seen in a subset of patients.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role in this report |
|---|---|---|---|
| [30148830](https://pubmed.ncbi.nlm.nih.gov/30148830/) | Homozygous LOF *MNS1* mutations cause laterality defects and likely male infertility | Human clinical/genetic | Establishes causality (Finding 1); axonemal localization + CCDC114 interaction (Findings 2, 6) |
| [31534215](https://pubmed.ncbi.nlm.nih.gov/31534215/) | *MNS1* variant associated with situs inversus and male infertility | Human clinical/genetic | Independent confirmation; Amish founder allele; randomized recessive inheritance (Findings 1, 3) |
| [22396656](https://pubmed.ncbi.nlm.nih.gov/22396656/) | MNS1 is essential for spermiogenesis and motile ciliary functions in mice | Model organism (mouse) | Foundational KO; situs inversus, hydrocephalus, sperm/axoneme defects (Finding 4) |
| gnomAD v4 | Population constraint & allele frequencies | Computational/population | Recessive LOF tolerance; allele rarity (Finding 5) |
| UniProt Q8NEH6 / Pfam PF13868 | Protein annotation | Computational/curated | Domain architecture, MIP function (Finding 6) |
| [27486780](https://pubmed.ncbi.nlm.nih.gov/27486780/) | TTC25 deficiency → ODA-DC defects & PCD with L–R randomization | Human + mouse | Contextualizes ODA-DC module and situs randomization |
| [25192045](https://pubmed.ncbi.nlm.nih.gov/25192045/) | CCDC151 mutations disrupt ODA docking complex | Human + zebrafish/mouse | Supports ODA-DC pathway placement of MNS1 |
| [24577564](https://pubmed.ncbi.nlm.nih.gov/24577564/) | Laterality defects other than SIT in PCD | Human clinical | Frames situs-spectrum epidemiology & diagnostics |
| [32647064](https://pubmed.ncbi.nlm.nih.gov/32647064/) | Changes in prognosis of heterotaxy over time | Human clinical | Prognosis/outcomes context (CHD-driven mortality) |

All mechanistic and genetic claims specific to HTX9 rest on the three primary sources (two human, one mouse) plus curated population/protein databases. Broader heterotaxy/PCD papers are used only for contextual framing (differential diagnosis, pathway, prognosis), not to attribute HTX9-specific facts.

---

## Limitations and Knowledge Gaps

1. **Very small human cohort (<10 individuals)** from consanguineous/founder families limits confidence in penetrance estimates, full phenotypic spectrum, and generalizability. Female fertility outcomes are essentially unstudied.
2. **Hydrocephalus** is robustly demonstrated in mouse but **not confirmed as a human HTX9 feature** — an important gap flagged throughout.
3. **No prevalence/incidence data** exist for HTX9 specifically; epidemiology is inferred from the broader heterotaxy/PCD literature.
4. **Oligogenic contributions** (e.g., co-inherited *DNAH5*) are noted anecdotally but not systematically studied; modifier genetics is unknown.
5. **No experimental structure** of MNS1 within a human HTX9-patient axoneme was retrieved; domain/function annotation is from UniProt/Pfam/InterPro and homology.
6. **No therapeutics, biomarkers, or clinical trials** target HTX9 directly; treatment evidence is extrapolated from heterotaxy/CHD and PCD management.
7. **ICD/MeSH mapping** is approximate — no HTX9-specific billing code exists.

---

## Proposed Follow-up Experiments / Actions

1. **Assemble an international *MNS1* patient registry** (GeneMatcher/Matchmaker Exchange) to expand N, quantify penetrance of situs subtypes, and define the true phenotypic range (including whether human hydrocephalus, sinopulmonary disease, and female subfertility occur).
2. **Cryo-EM of patient-derived or reconstituted axonemal doublets** with/without MNS1 to map exactly how MNS1 stabilizes the DMT lattice and positions the ODA-DC — testing the mechanistic step that is currently inferred.
3. **Standardized TEM/immunofluorescence panels** on HTX9 nasal-brush and sperm samples to define the ODA/ODA-DC defect signature for diagnostic use.
4. **Genotype–situs correlation study** across ODA-DC genes (*MNS1, CCDC114, CCDC151, ARMC4, TTC25*) to test whether MNS1 loss yields a milder/more randomized situs distribution than other module members.
5. **Founder-allele carrier screening** in the Old Order Amish (p.Glu136Glyfs*16) to establish carrier frequency and enable cascade counseling.
6. **Reproductive-outcome study** of ICSI success in *MNS1*-related male infertility.
7. **Conditional/tissue-specific mouse models** (node vs. germ cell vs. ependyma) to dissect branch points and test whether the hydrocephalus phenotype has a human correlate.

---

*Report compiled from 6 confirmed findings across 31 reviewed papers and curated database analyses (gnomAD v4, UniProt/Pfam/InterPro). Evidence sources are labeled as human clinical, model organism, in vitro, or computational throughout.*


## Artifacts

- [OpenScientist final report](Visceral_Heterotaxy_9-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Visceral_Heterotaxy_9-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 9 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030070` (2 mentions) - the report calls it "MONDO"; MONDO calls it **heterotaxy, visceral, 9, autosomal, with male infertility**
- `HP:0011885` (1 mention) - the report calls it "Abnormal visceral situs"; HP calls it **Hemorrhage of the eye**
- `UBERON:0004341` (1 mention) - the report calls it "left–right organizer / node"; UBERON calls it **primitive streak**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0030680` (1 mention) - the report calls it "Abnormal cardiovascular morphology"; HP calls it **Abnormal cardiovascular system morphology**
- `HP:0012207` (1 mention) - the report calls it "Abnormal sperm motility"; HP calls it **Reduced sperm motility**