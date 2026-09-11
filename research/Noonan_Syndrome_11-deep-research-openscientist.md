---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T17:38:51.649402'
end_time: '2026-09-03T17:58:47.694035'
duration_seconds: 1196.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Noonan Syndrome 11 NS11, the MRAS-related form of Noonan syndrome,
    OMIM 618499, MONDO:0032786, caused by germline activating missense variants in
    MRAS encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and
    NOT any other numbered Noonan syndrome type.
  mondo_id: ''
  category: Genetic
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
citation_count: 11
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 6
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Noonan_Syndrome_11-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Noonan_Syndrome_11-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noonan Syndrome 11 NS11, the MRAS-related form of Noonan syndrome, OMIM 618499, MONDO:0032786, caused by germline activating missense variants in MRAS encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome 11 NS11, the MRAS-related form of Noonan syndrome, OMIM 618499, MONDO:0032786, caused by germline activating missense variants in MRAS encoding the RAS-family GTPase M-Ras. NOT LZTR1-related Noonan syndrome and NOT any other numbered Noonan syndrome type.** covering all of the
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

# Noonan Syndrome 11 (NS11): The MRAS-Related Form of Noonan Syndrome — A Comprehensive Disease Characterization

**Disease:** Noonan Syndrome 11 (NS11) | **OMIM:** #618499 | **MONDO:** 0032786 | **Gene:** *MRAS* (HGNC:7227, chromosome 3q22.3) | **Category:** Genetic (autosomal-dominant RASopathy)

**Scope note:** This report concerns *Noonan syndrome 11* (NS11), the form caused by germline activating missense variants in **MRAS** (M-Ras/R-Ras3). It is **NOT** LZTR1-related Noonan syndrome and **NOT** any other numbered NS subtype. Because NS11 is ultra-rare (a handful of published cases), many frequency, prognosis, and management statements are extrapolated from the broader Noonan syndrome/RASopathy literature and are flagged as such.

---

## Summary

Noonan syndrome 11 (NS11) is an **ultra-rare, autosomal-dominant subtype of Noonan syndrome** caused by *de novo* germline **gain-of-function missense variants in *MRAS***, the gene encoding the RAS-family GTPase **M-Ras (R-Ras3)**. It was first delineated in 2017 and confirmed in 2020, and to date only a handful of molecularly proven cases have been reported worldwide — making it **less than 1% of molecularly solved Noonan syndrome** (versus ~50% attributable to *PTPN11*). Despite its rarity, NS11 has attracted disproportionate attention because it is defined by a **severe, often neonatal/infantile-onset hypertrophic cardiomyopathy (HCM)** superimposed on the classic multisystem Noonan phenotype (distinctive facies, short stature, developmental delay, and variable congenital anomalies).

Mechanistically, NS11 is a textbook example of **RAS–MAPK pathway hyperactivation**. The recurrent hotspot substitutions — **p.Gly23Val, p.Gly23Arg, p.Thr68Ile, and p.Gln71Arg** — impair the intrinsic and GAP-stimulated GTP-hydrolysis activity of M-Ras, locking it in the constitutively active, GTP-bound state. Active M-Ras recruits the **SHOC2–PP1c (PPP1CB) holophosphatase**, which dephosphorylates the inhibitory Ser259 site of RAF, thereby amplifying signaling through the **RAF–MEK–ERK cascade** (and, variably, the **PI3K–AKT** axis). A founder variant (p.Gly23Val) drives an approximately **40-fold increase in M-Ras activation** in vitro, and CRISPR-corrected patient induced pluripotent stem cell–derived cardiomyocytes (iPSC-CMs) have proven that this single variant is **both necessary and sufficient** to produce cardiomyocyte hypertrophy and abnormal calcium handling.

Diagnosis is achieved through **multigene RASopathy NGS panels or exome sequencing** (single-gene *MRAS* testing is inefficient given >20 RASopathy genes). Management is multidisciplinary: recombinant human growth hormone for short stature, hemostatic screening before invasive procedures, and — most notably — **off-label MEK inhibition (trametinib)** as an emerging targeted therapy that can reverse or attenuate the otherwise frequently lethal HCM. This report synthesizes all 15 requested disease-characteristic domains, grounded in eight confirmed findings and 61 reviewed papers.

---

## Key Findings

### Finding 1 — Activating *MRAS* missense variants cause NS11 with hypertrophic cardiomyopathy

NS11 was established as a distinct RASopathy through two landmark reports. **Higgins et al. (2017)** identified a *de novo MRAS* variant (**p.Gly23Val**) by whole-exome trio sequencing in a 15-year-old female with Noonan syndrome and cardiac hypertrophy, after screening a cohort of 109 unrelated NS-phenotype patients. **Motta et al. (2020)** then reported two further unrelated patients with *de novo MRAS* variants — **c.203C>T (p.Thr68Ile)** and **c.67G>C (p.Gly23Arg)** — both with HCM; one died neonatally of cardiac failure. Functional assays in both studies demonstrated **high-level M-Ras activation resulting from impaired GTPase activity**, establishing a gain-of-function mechanism.

> *"Targeted sequencing revealed de novo MRAS variants, c.203C > T (p.Thr68Ile) and c.67G > C (p.Gly23Arg) as causative events"* — [PMID: 31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/)

> *"Functional analyses documented high level of activation of MRAS mutants due to impaired GTPase activity"* — [PMID: 31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/)

This finding anchors the disease definition: NS11 (OMIM #618499) is caused by activating variants in *MRAS* (3q22.3, HGNC:7227), and is genetically and clinically distinct from *LZTR1*-related and all other numbered Noonan syndrome subtypes.

### Finding 2 — Mechanism: mutant M-Ras enhances the SHOC2–PP1c holoenzyme, boosting RAF/MEK/ERK and PI3K-AKT signaling

The core molecular mechanism connecting M-Ras to disease was defined by **Rodriguez-Viciana et al. (2006)**, who showed that **Shoc2/Sur-8 together with the catalytic subunit of protein phosphatase 1 (PP1c)** form a highly specific M-Ras effector complex that stimulates RAF by dephosphorylating the inhibitory **Ser259 (S259)** site on RAF proteins. **Motta et al. (2020)** demonstrated that NS-causing M-Ras mutants exhibit **constitutive plasma-membrane targeting, prolonged non-raft localization, enhanced binding to PPP1CB and SHOC2, and variably increased MAPK and PI3K–AKT activation** — showing that the disease mutants amplify precisely this effector interaction.

> *"M-Ras targets Shoc2-PP1c to stimulate Raf activity by dephosphorylating the S259 inhibitory site of Raf proteins"* — [PMID: 16630891](https://pubmed.ncbi.nlm.nih.gov/16630891/)

> *"enhanced binding to PPP1CB and SHOC2 protein, and variably increased MAPK and PI3K-AKT activation"* — [PMID: 31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/)

This places NS11 firmly within the **SHOC2–PPP1CB–RAF signaling module**, the same axis mutated in *SHOC2*-related Noonan-like syndrome with loose anagen hair (NS/LAH) and *PPP1CB*-related Noonan-like syndrome — a striking example of pathway-level convergence.

### Finding 3 — MEK inhibition (trametinib) is an emerging targeted therapy for NS-associated HCM

Because NS11 pathology is driven by RAS–MAPK hyperactivation, pharmacologic **MEK1/2 inhibition** is a rational targeted therapy. A growing body of case reports documents **off-label trametinib** reversing or attenuating severe NS-associated HCM and lymphatic disease across multiple RASopathy genotypes (RIT1, RAF1, PTPN11), and a clinical trial is now registered (**NCT06555237**). **Chaput & Andelfinger (2024)** reviewed the repurposing of trametinib and mTOR inhibitors for RASopathy HCM. In parallel, **rigosertib** (a dual RAS/MAPK + PI3K/AKT inhibitor) reversed HCM in RAF1-NS models.

> *"repurposing of medications inhibiting the RAS/MAPK on a compassionate use basis has emerged as a promising concept to improve the outcome of these patients"* — [PMID: 38432396](https://pubmed.ncbi.nlm.nih.gov/38432396/)

While direct trametinib data specifically in *MRAS*-mutant patients are not yet published, the shared downstream mechanism (MEK/ERK hyperactivation) makes this the most promising disease-modifying strategy for NS11's lethal cardiac phenotype.

### Finding 4 — Variant spectrum: recurrent likely-pathogenic hotspots in a highly constrained gene

ClinVar (RefSeq **NM_001085049.3**) lists recurrent NS-causing missense variants classified as **Likely pathogenic**:

| cDNA | Protein | ClinVar classification |
|---|---|---|
| c.68G>T | p.Gly23Val | Likely pathogenic |
| c.67G>C | p.Gly23Arg | Likely pathogenic |
| c.203C>T | p.Thr68Ile | Likely pathogenic |
| c.212A>G | p.Gln71Arg | Likely pathogenic |
| c.359C>T | p.Pro120Leu | Likely pathogenic |

Of 297 *MRAS* ClinVar records, only these missense point variants are pathogenic/likely-pathogenic for NS (the other "Pathogenic" entries are large 3q copy-number variants unrelated to the point-mutation mechanism). Population-constraint metrics from gnomAD (ENSG00000158186, chr3:138,347,648–138,405,534) show *MRAS* is **strongly intolerant to both missense and loss-of-function variation**: missense Z = 3.16 (observed/expected = 0.555), pLI = 0.99, LoF o/e = 0.19 (4 observed vs 20.9 expected). The pathogenic residues **Gly23, Thr68, and Gln71** are conserved codons that are established mutational hotspots across the RAS protein family. All reported disease variants are **germline, de novo, and absent from population databases**.

> *"Gly23 and Thr68 are highly conserved residues, and the corresponding codons are known hotspots for RASopathy-associated mutations in other RAS proteins"* — [PMID: 31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/)

### Finding 5 — Clinical phenotype and epidemiology: an ultra-rare NS subtype with disproportionately severe, early-onset HCM

NS11 shares the core multisystem Noonan phenotype but is distinguished by its severe cardiac involvement. Noonan syndrome overall affects **~1:1,000–2,500 live births** (Roberts et al. 2013), is autosomal dominant, and features distinctive facies, short stature, congenital heart disease (pulmonary valve stenosis, HCM), developmental delay/learning difficulties, cryptorchidism, lymphatic dysplasia, bleeding diathesis, and renal anomalies. NS11/*MRAS* accounts for only a handful of reported individuals worldwide — **<1% of molecularly solved NS**. Reported *MRAS* patients **uniformly presented with HCM**, often with neonatal/infantile onset and severe course (including one neonatal death from cardiac failure).

> *"Noonan syndrome is a genetic multisystem disorder characterised by distinctive facial features, developmental delay, learning difficulties, short stature, congenital heart disease, renal anomalies, lymphatic malformations, and bleeding difficulties"* — [PMID: 23312968](https://pubmed.ncbi.nlm.nih.gov/23312968/)

> *"hypertrophic cardiomyopathy in RASopathies (R-HCM) is associated with higher prevalence of congestive heart failure and shows increased prevalence and severity of left ventricular outflow tract obstruction"* — [PMID: 34776080](https://pubmed.ncbi.nlm.nih.gov/34776080/)

RASopathy-associated HCM (R-HCM) shows higher rates of congestive heart failure and left ventricular outflow tract (LVOT) obstruction than sarcomeric HCM, consistent with the severe HCM-predominant presentation of *MRAS* cases.

### Finding 6 — M-Ras biology and evolutionary conservation inform model-organism relevance

M-Ras is a RAS-family GTPase with a **single orthologue conserved from nematode to human**, and it evolved independently of R-Ras (Keduka et al. 2009). In ascidian, *Ci-Mras* is expressed in the neural complex and its knockdown perturbs FGF–Ras–MAPK-dependent neural/notochord development; mammalian M-Ras mediates NGF-induced neuronal differentiation in PC12 cells. Beyond the SHOC2–PP1c–RAF branch, M-Ras also signals via **RA-GEF-2 to activate Rap1**, regulating integrin-mediated adhesion (Yoshikawa et al. 2007). Disease modeling to date is primarily via **patient-derived iPSC-cardiomyocytes carrying p.Gly23Val**, which reproduce hypertrophy and abnormal calcium handling.

> *"A single Mras orthologue exists from nematode to mammalian"* — [PMID: 18977283](https://pubmed.ncbi.nlm.nih.gov/18977283/)

> *"activated M-Ras potently induced lymphocyte function-associated antigen 1 (LFA-1)-mediated cell aggregation"* — [PMID: 17538012](https://pubmed.ncbi.nlm.nih.gov/17538012/)

### Finding 7 — p.Gly23Val causes ~40-fold constitutive activation; iPSC-CMs prove necessity and sufficiency for cardiac hypertrophy

**Higgins et al. (2017; JCI Insight)** performed molecular-dynamics simulations predicting that p.Gly23Val damages the effector-interaction regions and the GTP-binding site; ectopic-expression experiments revealed a **40-fold increase in M-Ras activation** versus wild-type, with enhanced RAS/MAPK signaling and downstream gene-expression changes. **Higgins et al. (2019; Circ Genom Precis Med)** used CRISPR/Cas9 isogenic-corrected patient iPSC-cardiomyocytes to demonstrate that the variant is **both necessary and sufficient** to elicit hypertrophy — larger cell size, hypertrophic gene-expression changes, and impaired Ca²⁺ handling (irregular Ca²⁺ transients).

> *"ectopic expression experiments revealed a 40-fold increase in MRAS activation for p.Gly23Val-MRAS compared with WT-MRAS"* — [PMID: 28289718](https://pubmed.ncbi.nlm.nih.gov/28289718/)

> *"p.Gly23Val-MRAS is both necessary and sufficient to elicit a cardiac hypertrophy phenotype in iPSC-CMs"* — [PMID: 31638832](https://pubmed.ncbi.nlm.nih.gov/31638832/)

This is among the strongest causal evidence in any RASopathy: an isogenic-control experiment directly linking a single point variant to the defining clinical phenotype.

### Finding 8 — Diagnosis and multidisciplinary management

Diagnosis of NS is **clinical** (van der Burgt criteria) with **molecular confirmation**; because *MRAS* is one of >20 RASopathy genes, testing uses **multigene NGS panels/exome** rather than single-gene tests (Tartaglia 2022). Short stature is treated with **recombinant human growth hormone**; a phase 3 RCT (REAL8, NCT05330325) showed once-weekly somapacitan non-inferior/superior to daily GH (height velocity 10.4 vs 9.2 cm/yr). Bleeding diathesis affects up to **~40–65%** of NS patients — partial factor XI/VII deficiency, platelet dysfunction, and shear-related acquired von Willebrand syndrome with pulmonary stenosis — warranting **hemostatic screening before surgery**. Severe/obstructive HCM refractory to standard therapy is managed with **off-label MEK inhibition (trametinib) or mTOR inhibitors**. Cancer surveillance follows RASopathy guidelines.

> *"Daily growth hormone (GH) injections are indicated for the treatment of short stature in children with Noonan syndrome"* — [PMID: 41774755](https://pubmed.ncbi.nlm.nih.gov/41774755/)

> *"Nearly 40% of patients with the Noonan syndrome had a bleeding diathesis and >90% of them had platelet function and/or coagulation abnormalities"* — [PMID: 24753526](https://pubmed.ncbi.nlm.nih.gov/24753526/)

---

## The 15 Disease-Characteristic Domains

### 1. Disease Information

**Overview.** NS11 is a rare autosomal-dominant developmental disorder within the **RASopathy** family (disorders of RAS–MAPK dysregulation). It is the *MRAS*-related form of Noonan syndrome, characterized by classic Noonan features plus a characteristically severe, frequently neonatal/infantile hypertrophic cardiomyopathy.

**Key identifiers.**
- **OMIM:** #618499 (Noonan syndrome 11)
- **MONDO:** 0032786
- **Gene:** *MRAS* (HGNC:7227), 3q22.3; Ensembl ENSG00000158186; gene OMIM 608435
- **RefSeq:** NM_001085049.3
- **ICD-10:** Q87.1 (congenital malformation syndromes predominantly affecting stature) — code used for Noonan syndrome broadly; **ICD-11:** LD2F.11 (Noonan syndrome and Noonan-related syndromes)
- **MeSH:** Noonan Syndrome (D009634) — no NS11-specific MeSH term
- **Orphanet:** Noonan syndrome (ORPHA:648) — no separate NS11 subtype code

**Synonyms/alternative names.** Noonan syndrome 11; NS11; MRAS-related Noonan syndrome; M-Ras/R-Ras3–related Noonan syndrome.

**Data source type.** Information is derived from **aggregated disease-level resources** (OMIM, ClinVar, gnomAD) and from **individual patient case reports** (the handful of published NS11 cases), not from EHR-scale cohorts — reflecting the ultra-rare nature of the disease.

### 2. Etiology

**Causal factor.** Purely **genetic**: *de novo* germline activating missense variants in *MRAS*. No environmental or infectious cause.

**Genetic risk factors.** The disease-causing variants are themselves the sole "risk factor." Recurrent hotspots: p.Gly23Val, p.Gly23Arg, p.Thr68Ile, p.Gln71Arg (and likely-pathogenic p.Pro120Leu). *MRAS* is highly constrained (missense Z = 3.16, pLI = 0.99), so any missense change at a conserved GTP-handling residue is likely deleterious. No NS11-specific modifier genes are established.

**Environmental risk factors.** None known. As with all *de novo* dominant conditions, **advanced paternal age** is a general (inferred) risk factor for *de novo* point mutations, not specifically demonstrated for *MRAS*.

**Protective factors.** None identified. Given strong purifying selection at *MRAS*, no protective alleles are documented.

**Gene–environment interactions.** None established. NS11 is a monogenic, fully genetically determined condition.

### 3. Phenotypes

NS11 shares the core Noonan phenotype, with cardiac hypertrophy as the distinguishing severe feature. Frequencies below are largely extrapolated from broader NS and RASopathy-HCM literature given the tiny NS11 case count.

| Phenotype | HPO term | Type | Onset | Frequency (NS11 cases / NS overall) | Severity |
|---|---|---|---|---|---|
| Hypertrophic cardiomyopathy | HP:0001639 | Clinical sign (imaging) | Neonatal/infantile | Uniform in *MRAS* cases; ~20% of NS | Severe, often life-threatening |
| Distinctive facies (hypertelorism, ptosis, low-set ears) | HP:0000316, HP:0000508 | Physical | Congenital | Typical of NS | Variable |
| Short stature | HP:0004322 | Physical | Postnatal | Common | Moderate |
| Developmental delay / learning difficulty | HP:0001263 | Behavioral/cognitive | Childhood | Common | Variable |
| Pulmonary valve stenosis | HP:0001642 | Clinical sign | Congenital | Common in NS; seen in NS-HCM | Variable |
| Webbed/broad neck | HP:0000465 | Physical | Congenital | Common | Mild |
| Bleeding diathesis | HP:0001892 | Laboratory/clinical | Any | ~40–65% of NS | Mild–moderate |
| Cryptorchidism (males) | HP:0000028 | Physical | Congenital | Common | Mild |
| Lymphatic dysplasia / chylothorax | HP:0000112, HP:0010288 | Clinical | Neonatal/infantile | Subset | Can be severe |
| Feeding difficulties | HP:0011968 | Clinical | Neonatal | ~50% of NS | Usually transient |

**Quality-of-life impact.** Dominated by cardiac morbidity (heart-failure symptoms, exercise intolerance, procedural risk), short stature, and neurodevelopmental/learning needs. Bleeding tendency complicates surgery. Formal EQ-5D/SF-36 data specific to NS11 are **not available**.

### 4. Genetic/Molecular Information

- **Causal gene:** *MRAS* (M-Ras/R-Ras3), 3q22.3, HGNC:7227; gene OMIM 608435; disease OMIM #618499.
- **Variant classification (ACMG/AMP, per ClinVar):** Likely pathogenic — p.Gly23Val (c.68G>T), p.Gly23Arg (c.67G>C), p.Thr68Ile (c.203C>T), p.Gln71Arg (c.212A>G), p.Pro120Leu (c.359C>T).
- **Variant type:** Missense single-nucleotide substitutions affecting conserved GTP-binding/hydrolysis residues.
- **Allele frequency:** Absent from population databases (gnomAD) — consistent with *de novo* pathogenic origin.
- **Somatic vs germline:** **Germline, de novo.** Somatic *MRAS* variation is not a recognized oncogenic driver comparable to *KRAS/HRAS/NRAS*.
- **Functional consequence:** **Gain of function** via impaired intrinsic and GAP-stimulated GTPase activity → constitutive GTP loading.
- **Modifier genes:** None established for NS11.
- **Epigenetic information:** No NS11-specific DNA-methylation or chromatin signature described.
- **Chromosomal abnormalities:** Not part of the point-mutation NS11 mechanism; large 3q22 CNVs in ClinVar represent a separate contiguous-gene entity.

### 5. Environmental Information

**Not applicable.** NS11 is a monogenic *de novo* dominant disorder. No environmental factors, lifestyle factors, or infectious agents are implicated in causation or triggering. Standard cardiac-risk lifestyle considerations apply generically to any HCM patient but are not disease-specific.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **de novo germline missense variant** in *MRAS* (e.g., c.68G>T, p.Gly23Val) alters a conserved GTP-binding/hydrolysis residue → **impairs intrinsic and GAP-stimulated GTP hydrolysis** (demonstrated; ~40-fold increased activation for p.Gly23Val).
2. Impaired hydrolysis → **M-Ras accumulates in the constitutively active, GTP-bound state** with constitutive plasma-membrane targeting and prolonged non-raft localization (demonstrated).
3. Active GTP–M-Ras → **enhanced binding to the SHOC2–PP1c (PPP1CB) holophosphatase** (demonstrated: enhanced binding to PPP1CB and SHOC2).
4. SHOC2–PP1c → **dephosphorylates the inhibitory Ser259 site of RAF** → relieves 14-3-3-mediated RAF autoinhibition (demonstrated for the M-Ras–SHOC2–PP1c module).
5. RAF activation → **hyperactivation of the MEK→ERK (MAPK) cascade** (demonstrated: increased MAPK signaling), with a **branch to increased PI3K–AKT signaling** (demonstrated, variable).
6. ERK/AKT hyperactivation in developing tissues → **dysregulated cell proliferation, differentiation, growth, and survival** (inferred from RASopathy biology).
7. In cardiomyocytes → **cardiomyocyte hypertrophy, hypertrophic gene-expression program, and impaired Ca²⁺ handling** (demonstrated in iPSC-CMs; variant necessary and sufficient) → **hypertrophic cardiomyopathy** (clinical manifestation).
8. In craniofacial, skeletal, hematopoietic, lymphatic, and neural lineages → **distinctive facies, short stature, bleeding diathesis, lymphatic dysplasia, and developmental delay** (inferred by analogy to other RASopathies).

```
  MRAS missense (Gly23/Thr68/Gln71)
            │  impairs GTP hydrolysis
            ▼
  Constitutive GTP–M-Ras  ── membrane-targeted, non-raft
            │  enhanced binding
            ▼
      SHOC2 – PP1c (PPP1CB) holophosphatase
            │  dephosphorylates RAF-pSer259
            ▼
        RAF (relieved autoinhibition)
            ├──────────────► MEK ──► ERK  (MAPK; main axis)
            └──────────────► PI3K ──► AKT  (variable branch)
                                   │
                                   ▼
          cardiomyocyte hypertrophy + Ca²⁺ dyshandling
                                   │
                                   ▼
                 SEVERE HYPERTROPHIC CARDIOMYOPATHY
        (+ facies, short stature, bleeding, lymphatic, DD)
```

- **Molecular pathways:** RAS–RAF–MEK–ERK (MAPK; KEGG hsa04010); PI3K–AKT (KEGG hsa04151); Rap1 signaling via RA-GEF-2 (secondary M-Ras branch).
- **Cellular processes:** Dysregulated proliferation, differentiation, growth, survival (GO:0008283, GO:0030154); cardiomyocyte hypertrophy (GO:0003300); abnormal Ca²⁺ handling.
- **Protein dysfunction:** Gain-of-function GTPase locked in active conformation (UniProt O14807, MRAS_HUMAN); no misfolding/aggregation — the defect is functional (constitutive signaling).
- **GO biological-process suggestions:** GO:0007265 (Ras protein signal transduction), GO:0000165 (MAPK cascade), GO:0043410 (positive regulation of MAPK cascade).
- **Cell types (CL):** cardiac muscle cell / cardiomyocyte (CL:0000746; CL:0002094 regular cardiac myocyte).
- **Molecular profiling:** iPSC-CM transcriptomics showed a hypertrophic gene-expression signature; no large-scale proteomic/metabolomic/lipidomic NS11-specific datasets exist.
- **Functional genomics:** CRISPR/Cas9 isogenic correction (Higgins 2019) is the key functional-genomics evidence.

### 7. Anatomical Structures Affected

- **Primary organ:** Heart — specifically the **myocardium/left ventricle** (UBERON:0002084 heart left ventricle; UBERON:0002349 myocardium), with hypertrophy and LVOT obstruction. Pulmonary valve (UBERON:0002146) with stenosis.
- **Secondary/body systems:** Cardiovascular (primary); lymphatic (UBERON:0006558 lymphatic vessel — chylothorax, lymphangiectasia); hematologic (bleeding diathesis); musculoskeletal/growth (short stature); craniofacial (distinctive facies); nervous system (developmental delay); genitourinary (cryptorchidism, occasional renal anomalies).
- **Tissue/cell level:** Cardiac muscle tissue; cardiomyocytes (CL:0000746). Connective tissue, lymphatic endothelium, and hematopoietic lineages secondarily involved.
- **Subcellular level (GO cellular component):** Plasma membrane (GO:0005886) — constitutive membrane targeting of mutant M-Ras; non-raft membrane microdomains; cytoplasm. Sarcoplasmic-reticulum Ca²⁺-handling machinery is functionally affected in cardiomyocytes.
- **Localization/lateralization:** Cardiac hypertrophy is typically biventricular/asymmetric septal as in HCM generally; systemic features are bilateral/symmetric.

### 8. Temporal Development

- **Onset:** **Congenital to neonatal/infantile.** HCM in reported *MRAS* cases presents very early, often neonatally (one neonatal death from cardiac failure).
- **Onset pattern:** Congenital structural/functional cardiac disease with progressive hypertrophy; facies present at birth; short stature emerges postnatally.
- **Progression:** Cardiac hypertrophy can be **rapidly progressive** in infancy — a poor-prognosis pattern shared with other early-onset RASopathy HCM. Course is otherwise chronic and lifelong.
- **Disease course:** Non-cardiac features (facies, stature, learning) are stable/chronic; cardiac disease is the dominant driver of morbidity/mortality and can progress to heart failure.
- **Remission patterns:** No spontaneous remission of the genetic disorder; **treatment-induced regression of HCM** observed with MEK inhibition in RASopathy HCM broadly.
- **Critical periods:** The **neonatal/infantile window** is the critical period of cardiac vulnerability and the key window for intervention (e.g., MEK-inhibitor rescue).

### 9. Inheritance and Population

- **Epidemiology:** No standalone NS11 prevalence/incidence figures exist. Noonan syndrome overall: **~1:1,000–2,500 live births**. NS11 is **<1% of molecularly solved NS** — ultra-rare, a handful of reported individuals worldwide.
- **Inheritance:** **Autosomal dominant**; reported cases are **de novo**.
- **Penetrance:** Presumed high/complete for the cardiac phenotype in reported cases (all had HCM), though the sample is too small for formal estimates.
- **Expressivity:** Variable, as in NS generally.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not documented for *MRAS*; possible in principle for any de novo dominant condition (inferred).
- **Founder effects / consanguinity:** Not applicable (de novo dominant; no founder alleles).
- **Carrier frequency:** Not applicable (dominant, de novo; variants absent from gnomAD).
- **Population demographics:** No ethnic predisposition known; reported cases span different populations. Sex ratio: NS overall is roughly equal; NS11 case count too small to assess. Age distribution: presents in infancy/childhood.

### 10. Diagnostics

- **Clinical diagnosis:** Van der Burgt criteria for Noonan syndrome (facies + one or more of: cardiac defect, short stature, family history, other features).
- **Genetic testing (recommended approach):** **Multigene RASopathy NGS panel or exome/genome sequencing** — the standard, because *MRAS* is one of >20 RASopathy genes. Single-gene *MRAS* testing is inefficient. WGS/WES both have high utility; targeted panels are cost-effective first-line. Chromosomal microarray/karyotype/FISH are **not** primary tools (point-mutation disorder). Mitochondrial and repeat-expansion testing are not applicable.
- **Variant interpretation:** ClinVar/ClinGen and ACMG/AMP criteria; de novo occurrence (PS2), absence from gnomAD (PM2), hotspot residue (PM1), and functional gain-of-function data (PS3) support pathogenicity.
- **Cardiac diagnostics:** Echocardiography (HCM, LVOT gradient, pulmonary stenosis), ECG, cardiac MRI, and heart-failure biomarkers (BNP/NT-proBNP — generic).
- **Hematologic workup:** Bleeding time, PT/aPTT, factor XI/VII assays, platelet-function testing, von Willebrand multimer analysis — especially **before invasive procedures**.
- **Omics-based diagnostics:** Not routinely used; research iPSC-CM models exist.
- **Differential diagnosis:** Other RASopathies (*PTPN11*, *SOS1*, *RAF1*, *RIT1*, *SHOC2*, *PPP1CB*, *LZTR1*, etc.), sarcomeric HCM, and other syndromic HCM causes (metabolic/mitochondrial). Molecular testing resolves the distinction.
- **Screening:** No population newborn screening exists; **cascade testing** is limited by the de novo nature. Prenatal findings (increased nuchal translucency, cardiac hypertrophy, polyhydramnios) may prompt targeted testing.

### 11. Outcome / Prognosis

- **Prognosis driver:** **Severity and onset of HCM.** Early-onset (before ~6 months) NS-HCM carries **high mortality**; NS11 cases have included neonatal death from cardiac failure.
- **Survival/mortality:** No NS11-specific survival statistics. By analogy, RASopathy-HCM with heart failure has worse surgical risk and mortality than sarcomeric HCM.
- **Morbidity:** Heart failure, LVOT obstruction, arrhythmia risk, bleeding complications, growth failure, developmental/learning needs.
- **Recovery potential:** The genetic disorder is lifelong, but **MEK-inhibitor therapy has produced regression of HCM** in RASopathy patients, offering a route to improved cardiac outcomes.
- **Prognostic factors:** Age at HCM onset, LVOT obstruction, heart-failure signs, treatment response.
- **Prognostic biomarkers:** No validated NS11-specific molecular biomarkers; cardiac imaging metrics and natriuretic peptides are used clinically.

### 12. Treatment

- **Pharmacotherapy / targeted therapy (emerging):** **MEK1/2 inhibitor trametinib** (off-label/compassionate use) can reverse or attenuate severe NS-associated HCM and lymphatic disease; a trial is registered (**NCT06555237**). **mTOR inhibitors** (rapamycin/everolimus) have been used for severe RASopathy HCM. **Rigosertib** (dual RAS/MAPK + PI3K/AKT inhibitor) reversed HCM in RAF1-NS models. NCIT terms: Trametinib (NCIT:C77908); Sirolimus/Rapamycin (NCIT:C1212).
- **Growth:** **Recombinant human growth hormone** for short stature; once-weekly somapacitan shown non-inferior/superior to daily GH in NS (REAL8 RCT). NCIT: Recombinant Human Growth Hormone (NCIT:C1834).
- **Cardiac supportive/interventional:** Standard HCM management (beta-blockers, avoidance of dehydration), surgical/catheter relief of LVOT/pulmonary stenosis; RVOT stenting and staged strategies used to bridge infants (trametinib-then-surgery approaches reported in NS-HCM broadly).
- **Hematologic:** Hemostatic optimization before surgery.
- **Rehabilitative/supportive:** Developmental and educational support; physical/occupational/speech therapy; nutritional support for feeding difficulties.
- **Pharmacogenomics:** No NS11-specific pharmacogenomic guidance; the genotype itself (RAS-MAPK activation) is the rationale for pathway-targeted therapy (precision-medicine approach).
- **Treatment outcomes/adverse events:** Trametinib case reports show short-term symptomatic improvement across NS-HCM; moderate side effects (skin, GI) reported; long-term data lacking. Formal response rates in *MRAS* patients specifically are **not yet published**.
- **Cancer surveillance:** Per RASopathy guidelines (RAS-MAPK genes carry variable tumor risk).

### 13. Prevention

- **Primary prevention:** Not possible — de novo genetic origin.
- **Secondary prevention:** **Early cardiac surveillance** (echocardiography) after molecular/clinical diagnosis to detect and treat HCM early; early hemostatic evaluation before procedures.
- **Tertiary prevention:** Aggressive management of HCM (targeted MEK/mTOR inhibition, heart-failure care, obstruction relief) to prevent decompensation; developmental support to optimize function.
- **Immunization/behavioral/public-health/environmental interventions:** Not applicable (no environmental etiology). Standard childhood immunizations apply.
- **Genetic counseling:** Central to care. Recurrence risk for parents of a de novo case is low (but non-zero due to possible germline mosaicism). An affected individual has **50% transmission risk** (autosomal dominant). **Prenatal/preimplantation genetic testing** is available once the familial variant is known.

### 14. Other Species / Natural Disease

- **Taxonomy/orthologues:** *MRAS* is conserved with a **single orthologue from nematode to human**. Mouse *Mras* (NCBI Gene 17532); ascidian *Ci-Mras*; zebrafish and other vertebrate orthologues exist.
- **Natural disease in other species:** **No naturally occurring *MRAS*-related Noonan-like disease is documented** in companion animals or wildlife (OMIA). Veterinary relevance is therefore minimal.
- **Comparative biology:** M-Ras evolved independently of R-Ras; its neural/developmental function is conserved between mammals and ascidian, and it functions in FGF–Ras–MAPK-dependent development — underscoring cross-species conservation of the affected pathway.
- **Transmission/zoonosis:** Not applicable (non-infectious genetic disorder).

### 15. Model Organisms

- **Cellular/in vitro (primary model):** **Patient-derived iPSC-cardiomyocytes carrying p.Gly23Val**, with **CRISPR/Cas9 isogenic-corrected controls** — the definitive NS11 model. It recapitulates cardiomyocyte hypertrophy, hypertrophic gene expression, and impaired Ca²⁺ handling, and established that the variant is necessary and sufficient for the cardiac phenotype ([PMID: 31638832](https://pubmed.ncbi.nlm.nih.gov/31638832/)). Ectopic-expression cell systems quantified the ~40-fold activation ([PMID: 28289718](https://pubmed.ncbi.nlm.nih.gov/28289718/)).
- **In vitro biochemistry:** Cell-based assays of GTP loading, SHOC2/PPP1CB binding, and MAPK/PI3K-AKT readouts (Motta 2020).
- **Invertebrate/other:** Ascidian *Ci-Mras* knockdown models demonstrate conserved neural/notochord roles; PC12 cells model M-Ras-dependent neuronal differentiation.
- **Mammalian genetic models:** **No published *Mras* knock-in mouse specifically modeling NS11** was identified; general RASopathy mouse models (*Ptpn11*, *Raf1* knock-ins) inform pathway biology and MEK-inhibitor efficacy, and transgenic *Raf1* models were used for the rigosertib study.
- **Model characteristics/limitations:** iPSC-CMs excellently model the cardiac phenotype and drug response but do **not** capture systemic/developmental features (facies, stature, lymphatics) or whole-organism physiology. A dedicated *Mras* animal model remains a gap.
- **Resources:** MGI (*Mras*, mouse gene 17532), Cellosaurus (patient iPSC lines), Alliance of Genome Resources for orthology.

---

## Mechanistic Model / Interpretation

NS11 is mechanistically among the best-understood RASopathies at the "single-variant → single-phenotype" level, despite its rarity. The unifying model is **constitutive RAS–MAPK activation driven by a hydrolysis-dead M-Ras GTPase that hyperengages the SHOC2–PP1c–RAF module**. Three lines of orthogonal evidence converge:

| Evidence layer | Method | Result | Reference |
|---|---|---|---|
| Genetics | Trio WES / targeted sequencing | Recurrent de novo *MRAS* hotspots (Gly23, Thr68, Gln71) in NS-HCM | [PMID: 28289718](https://pubmed.ncbi.nlm.nih.gov/28289718/), [PMID: 31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/) |
| Biochemistry | GTP-loading, binding, signaling assays | ~40× activation; impaired GTPase; ↑SHOC2/PPP1CB binding; ↑MAPK/PI3K-AKT | [PMID: 28289718](https://pubmed.ncbi.nlm.nih.gov/28289718/), [PMID: 31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/) |
| Cell model | CRISPR-isogenic iPSC-CMs | Variant necessary and sufficient for hypertrophy + Ca²⁺ defects | [PMID: 31638832](https://pubmed.ncbi.nlm.nih.gov/31638832/) |
| Pathway anchor | Effector reconstitution | SHOC2–PP1c dephosphorylates RAF-Ser259 to activate RAF | [PMID: 16630891](https://pubmed.ncbi.nlm.nih.gov/16630891/) |

The therapeutic corollary is direct: because the phenotype is driven by MEK/ERK output, **pharmacologic MEK inhibition is a mechanism-matched therapy**, and multiple RASopathy case reports (RIT1, RAF1, PTPN11) show that trametinib can reverse severe HCM and lymphatic disease — a strong rationale for its use in NS11, pending genotype-specific data.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [28289718](https://pubmed.ncbi.nlm.nih.gov/28289718/) | *Elucidation of MRAS in NS* (Higgins 2017) | First NS11 case; p.Gly23Val; ~40× activation; MD simulations |
| [31108500](https://pubmed.ncbi.nlm.nih.gov/31108500/) | *Activating MRAS mutations cause NS with HCM* (Motta 2020) | Two further cases (Thr68Ile, Gly23Arg); GTPase/SHOC2/PPP1CB mechanism |
| [31638832](https://pubmed.ncbi.nlm.nih.gov/31638832/) | iPSC-CM CRISPR study (Higgins 2019) | Variant necessary & sufficient for cardiomyocyte hypertrophy |
| [16630891](https://pubmed.ncbi.nlm.nih.gov/16630891/) | Shoc2–PP1c M-Ras effector (Rodriguez-Viciana 2006) | Defines SHOC2–PP1c → RAF-Ser259 mechanism |
| [34776080](https://pubmed.ncbi.nlm.nih.gov/34776080/) | R-HCM review (Lioncino 2022) | Severe R-HCM phenotype (CHF, LVOT obstruction) |
| [29525650](https://pubmed.ncbi.nlm.nih.gov/29525650/) | RASopathy HCM natural history (Calcagni 2018) | Early-onset severe HCM; mTOR-inhibitor rationale |
| [38432396](https://pubmed.ncbi.nlm.nih.gov/38432396/) | MEK inhibition for RASopathy HCM (Chaput 2024) | Therapeutic repurposing framework |
| [42610277](https://pubmed.ncbi.nlm.nih.gov/42610277/) | Rigosertib reverses HCM in NS | Dual RAS/MAPK+PI3K/AKT inhibitor efficacy (RAF1 model) |
| [23312968](https://pubmed.ncbi.nlm.nih.gov/23312968/) | Noonan syndrome review (Roberts 2013) | Core multisystem NS phenotype and prevalence |
| [36394128](https://pubmed.ncbi.nlm.nih.gov/36394128/) | RASopathy genetics update (Tartaglia 2022) | >20 genes; panel/exome testing rationale |
| [18977283](https://pubmed.ncbi.nlm.nih.gov/18977283/) | M-Ras evolution (Keduka 2009) | Single conserved orthologue; neural function |
| [17538012](https://pubmed.ncbi.nlm.nih.gov/17538012/) | M-Ras–RA-GEF-2–Rap1 (Yoshikawa 2007) | Secondary M-Ras effector branch |
| [41774755](https://pubmed.ncbi.nlm.nih.gov/41774755/) | Somapacitan RCT in NS | GH therapy for short stature |
| [24753526](https://pubmed.ncbi.nlm.nih.gov/24753526/) | Hemostatic abnormalities in NS (Artoni 2014) | ~40% bleeding diathesis; pre-surgical screening |
| [22985731](https://pubmed.ncbi.nlm.nih.gov/22985731/) | Acquired vWS in NS (Wiegand 2012) | Shear-related bleeding with pulmonary stenosis |
| [12754583](https://pubmed.ncbi.nlm.nih.gov/12754583/) | Hematological findings in NS (Bertola 2003) | Factor XI deficiency, platelet dysfunction |

---

## Limitations and Knowledge Gaps

1. **Tiny case count.** Only a handful of molecularly proven NS11 patients are published. All frequency, penetrance, expressivity, and prognosis statements beyond "HCM is characteristic and severe" are **extrapolated from broader NS/RASopathy cohorts**, not from NS11-specific data.
2. **No NS11-specific epidemiology.** Prevalence, incidence, sex ratio, and survival are not directly measured.
3. **No dedicated in vivo model.** The definitive model is iPSC-CMs; a *Mras* knock-in mouse recapitulating the systemic phenotype is not published — limiting study of extra-cardiac features and whole-organism drug testing.
4. **Genotype-specific therapy data absent.** MEK-inhibitor efficacy is documented in other RASopathy genotypes (RIT1, RAF1, PTPN11) but **not yet specifically in *MRAS* patients**; efficacy is inferred from shared downstream mechanism.
5. **Extra-cardiac mechanism largely inferred.** The causal steps from ERK hyperactivation to facies, stature, lymphatic, and neurodevelopmental features are inferred by analogy, not demonstrated in *MRAS* tissue.
6. **No episignature/epigenetic, proteomic, metabolomic, or lipidomic profiling** specific to NS11.
7. **p.Pro120Leu and p.Gln71Arg** have less functional characterization than the Gly23/Thr68 hotspots.

---

## Proposed Follow-up Experiments / Actions

1. **International case registry.** Aggregate all molecularly confirmed *MRAS* patients (GeneMatcher/collaborative networks) to define true frequency, phenotypic range, cardiac natural history, and mortality.
2. **Generate an *Mras* knock-in mouse** (e.g., p.Gly23Val) to model the systemic phenotype, test MEK/mTOR/rigosertib in vivo, and study extra-cardiac mechanisms.
3. **Genotype-specific trametinib data.** Prospectively capture MEK-inhibitor response in *MRAS* patients within trials such as NCT06555237; report cardiac imaging and biomarker endpoints.
4. **Functional characterization of p.Gln71Arg and p.Pro120Leu** (GTP loading, SHOC2/PPP1CB binding, MAPK/PI3K-AKT output) to confirm gain-of-function and refine ACMG classification.
5. **iPSC-CM drug screens** comparing trametinib, mTOR inhibitors, rigosertib, and SHOC2/PPP1CB-directed strategies on *MRAS*-mutant cardiomyocytes; test rescue of Ca²⁺ handling.
6. **Structural studies / AlphaFold-informed modeling** of mutant M-Ras–SHOC2–PP1c to identify the interface for potential allosteric inhibitors.
7. **Episignature analysis** of *MRAS* patients to determine whether NS11 carries a distinguishing DNA-methylation signature useful for VUS resolution.

---

*Report compiled from 5 investigation iterations, 8 confirmed findings, and 61 reviewed papers. Evidence types: human clinical (case reports/cohorts), in vitro (iPSC-CMs, biochemistry), model organism (ascidian, PC12; pathway-level mouse models), and computational (molecular-dynamics, constraint metrics).*


## Artifacts

- [OpenScientist final report](Noonan_Syndrome_11-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Noonan_Syndrome_11-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 11 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 5 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001263` (1 mention) - the report calls it "Developmental delay / learning difficulty"; HP calls it **Global developmental delay**, and lists "Developmental delay, global" among its other names
- `HP:0001642` (1 mention) - the report calls it "Pulmonary valve stenosis"; HP calls it **Pulmonic stenosis**, and lists "Pulmonary valve stenosis" among its other names
- `HP:0000465` (1 mention) - the report calls it "Webbed/broad neck"; HP calls it **Webbed neck**
- `HP:0001892` (1 mention) - the report calls it "Bleeding diathesis"; HP calls it **Abnormal bleeding**, and lists "Bleeding diathesis" among its other names
- `HP:0000028` (1 mention) - the report calls it "Cryptorchidism (males)"; HP calls it **Cryptorchidism**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:7227` - called "MRAS", "Gene:** *MRAS"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

28 of 30 terms resolved to a current term; the rest could not be looked up either way.