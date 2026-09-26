---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-24T16:12:01.916042'
end_time: '2026-09-24T16:29:24.256306'
duration_seconds: 1042.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hereditary Sensory and Autonomic Neuropathy Type 1A
  mondo_id: MONDO:0008086
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
citation_count: 34
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 25
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 32
  verified: 29
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.033
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0008086
    reported_labels:
    - MONDO
    ontology_label: neuropathy, hereditary sensory and autonomic, type 1A
  - term_id: HP:0012060
    reported_labels:
    - acro-osteolysis
    ontology_label: Acral lentiginous melanoma
  - term_id: HP:0100261
    reported_labels:
    - neuropathic joint
    ontology_label: Abnormal tendon morphology
  - term_id: HP:0000407
    reported_labels:
    - Subset
    ontology_label: Sensorineural hearing impairment
  labels_variant: 1
  unresolved_terms:
  - HP:0106487
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
  path: Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1A-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1A-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Sensory and Autonomic Neuropathy Type 1A
- **MONDO ID:** MONDO:0008086 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hereditary Sensory and Autonomic Neuropathy Type 1A** covering all of the
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

# Hereditary Sensory and Autonomic Neuropathy Type 1A (HSAN1A): Comprehensive Disease Characterization Report

**Disease:** Hereditary Sensory and Autonomic Neuropathy Type 1A
**MONDO ID:** MONDO:0008086 | **OMIM:** 162400 | **Gene:** *SPTLC1* (9q22.31)
**Category:** Mendelian (autosomal dominant)

---

## Summary

Hereditary Sensory and Autonomic Neuropathy Type 1A (HSAN1A) is the most common autosomal-dominant hereditary sensory neuropathy. It is caused by heterozygous, mostly missense mutations in *SPTLC1*, which encodes long-chain base subunit 1 of **serine palmitoyltransferase (SPT)**, the rate-limiting enzyme of de novo sphingolipid biosynthesis. Rather than acting through simple loss of function, HSAN1A mutations are **neomorphic gain-of-function** changes: they shift the amino-acid substrate preference of SPT away from its canonical substrate L-serine toward L-alanine (and glycine). This produces atypical **1-deoxysphingolipids (1-deoxySLs)** that lack the C1 hydroxyl group, cannot be converted into complex sphingolipids or degraded by the normal catabolic machinery, accumulate to neurotoxic levels, and preferentially injure long dorsal-root-ganglion (DRG) sensory neurons ([PMID: 11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/); [PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/); [PMID: 27016021](https://pubmed.ncbi.nlm.nih.gov/27016021/)).

Clinically, HSAN1A presents in the second-to-third decade with length-dependent, sensory-predominant axonal neuropathy: distal lower-limb sensory loss (pain and temperature prominent), spontaneous shooting/lancinating pain, and variable distal motor involvement. Progressive loss of protective sensation leads to the hallmark **ulceromutilating complications** — recurrent painless foot ulcers, osteomyelitis, neuropathic (Charcot) arthropathy, and distal amputations. The disease shows incomplete penetrance, variable expressivity, and apparent anticipation ([PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/); [PMID: 11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/)). The canonical mutation p.Cys133Trp (c.399T>G) is a **southern-English founder allele** and the single most common cause of HSAN in the UK ([PMID: 11479835](https://pubmed.ncbi.nlm.nih.gov/11479835/); [PMID: 22302274](https://pubmed.ncbi.nlm.nih.gov/22302274/)).

The mechanistic understanding of HSAN1A has direct therapeutic consequences. Because the disease is driven by a substrate-availability defect, **high-dose oral L-serine** competitively restores the canonical reaction, lowers plasma 1-deoxySLs, and has Class I randomized-controlled-trial evidence for slowing progression — the first disease-modifying therapy for the condition ([PMID: 30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/); [PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/)). Cryo-EM structures of the human SPT–ssSPT–ORMDL complex have resolved how catalytic-pocket variants alter substrate selectivity and, importantly, revealed that a distinct set of *SPTLC1* transmembrane-domain variants instead impair ORMDL/ceramide feedback and cause juvenile ALS — establishing that treatment must be genotype-guided ([PMID: 33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/); [PMID: 37308477](https://pubmed.ncbi.nlm.nih.gov/37308477/); [PMID: 35900868](https://pubmed.ncbi.nlm.nih.gov/35900868/)). The same 1-deoxySL/serine-deficiency biology also links HSAN1A to retinal macular telangiectasia type 2, revealing a shared neuronal-retinal degenerative mechanism ([PMID: 31509666](https://pubmed.ncbi.nlm.nih.gov/31509666/)).

---

## 1. Disease Information

**Overview.** HSAN1A is a rare, adult-onset, autosomal-dominant, length-dependent axonal peripheral neuropathy in which sensory fibers are predominantly affected, with variable motor and autonomic involvement. It belongs to the broader group of **hereditary sensory neuropathies (HSNs)** / hereditary sensory and autonomic neuropathies (HSANs), also historically classified among the ulceromutilating neuropathies and, when motor weakness is prominent, overlapping with Charcot-Marie-Tooth (CMT) disorders ([PMID: 15319794](https://pubmed.ncbi.nlm.nih.gov/15319794/); [PMID: 12633143](https://pubmed.ncbi.nlm.nih.gov/12633143/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0008086 |
| OMIM | 162400 (HSAN1A) |
| Gene | *SPTLC1*, OMIM 605712, HGNC:11277, 9q22.31 |
| Orphanet | Hereditary sensory and autonomic neuropathy type 1 (ORPHA:36386) |
| ICD-10 | G60.8 (other hereditary and idiopathic neuropathies) |
| ICD-11 | 8C20 (hereditary neuropathy) range |
| MeSH | Hereditary Sensory and Autonomic Neuropathies (D009477 family) |

**Synonyms / alternative names.** HSAN I; HSAN1; HSN1; HSN I; Hereditary Sensory Neuropathy Type 1; HSN type IA; Neuropathy, Hereditary Sensory Radicular, Autosomal Dominant; ulceromutilating neuropathy (historical).

**Source of information.** This report is derived from **aggregated disease-level resources** — OMIM, Orphanet, and primary/peer-reviewed literature (family cohorts, case series, functional studies, cryo-EM structures, and one randomized controlled trial) — rather than from individual electronic health records.

---

## 2. Etiology

**Primary cause — genetic.** HSAN1A is caused by heterozygous, autosomal-dominant mutations in *SPTLC1*. The genetic mechanism is a **neomorphic gain of function / dominant change of substrate specificity**, not haploinsufficiency. Canonical mutations (p.Cys133Trp, p.Cys133Tyr, p.Val144Asp, and the p.Ser331 variants) alter SPT so that it condenses palmitoyl-CoA with L-alanine and glycine instead of L-serine, generating 1-deoxysphinganine and 1-deoxymethylsphinganine. As Bode & Bode (2018) summarize: *"Mutations in SPT result in a change in enzyme substrate specificity, which causes the production of atypical deoxysphinganine and deoxymethylsphinganine, rather than the normal enzyme product, sphinganine. Levels of these abnormal compounds are elevated in blood of HSN-1 patients"* ([PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/); [PMID: 11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/)).

**Genetic risk factors.**
- **Causal variants:** *SPTLC1* missense variants (see Section 4). Allelic disorders also arise from *SPTLC2* (HSAN1C), which likewise raises 1-deoxySLs ([PMID: 26573920](https://pubmed.ncbi.nlm.nih.gov/26573920/)).
- **Modifier genes:** SPT small subunits (SPTSSA/SPTSSB; yeast ortholog Tsc3) regulate serine-versus-alanine selectivity and are candidate modifiers of 1-deoxySL output ([PMID: 30154231](https://pubmed.ncbi.nlm.nih.gov/30154231/); [PMID: 33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/)).

**Environmental / metabolic risk factors.** Because the deleterious reaction depends on relative amino-acid availability, **low systemic L-serine and high L-alanine** shift the balance toward 1-deoxySL formation. In C133W transgenic mice an L-alanine-enriched diet increased deoxySLs and worsened neuropathy ([PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/)). Metabolic states that lower serine or raise alanine (and, more broadly, conditions raising 1-deoxySLs such as diabetes/metabolic syndrome) are plausible aggravating factors. Sex may modulate motor severity (earlier/more severe motor onset reported in males in some families; [PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/)).

**Protective factors.** **High dietary/therapeutic L-serine** is the key protective factor — it competes L-alanine out of the SPT active site, reducing 1-deoxySL synthesis ([PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/); [PMID: 30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/)). No specific protective germline alleles are established.

**Gene–environment interaction.** The clearest GxE axis is **genotype × serine/alanine availability**: the pathogenic genotype only produces toxic lipids in the context of available L-alanine, and disease burden is tunable by dietary amino-acid manipulation in both directions — a rare example of a Mendelian neuropathy with a dietary modifier that has been exploited therapeutically.

---

## 3. Phenotypes

HSAN1A phenotypes are predominantly **sensory clinical signs and symptoms**, with secondary physical manifestations from denervation.

| Phenotype | Type | Onset | Severity/Progression | Frequency | Suggested HPO |
|---|---|---|---|---|---|
| Distal sensory loss (lower limbs, length-dependent) | Clinical sign/symptom | 2nd–3rd decade | Progressive | Near-universal (core feature) | HP:0106487 (impaired distal vibration); HP:0007328 (impaired pain sensation) |
| Loss of pain & temperature sensation | Symptom | Early | Progressive | Prominent | HP:0007328; HP:0010829 (impaired temperature sensation) |
| Spontaneous shooting/lancinating (neuropathic) pain | Symptom | Variable | Episodic/fluctuating | Common | HP:0009830 (peripheral neuropathy); HP:0000738 |
| Distal foot ulcers (painless) | Physical manifestation | After sensory loss | Recurrent, progressive | Frequent/feared complication | HP:0200042 (skin ulcer) |
| Osteomyelitis / bone infection | Physical manifestation | Later | Progressive | Frequent complication | HP:0002754 (osteomyelitis) |
| Acro-osteolysis / distal amputations | Physical manifestation | Later | Mutilating | Frequent | HP:0012060 (acro-osteolysis) |
| Neuropathic (Charcot) arthropathy | Physical manifestation | Later | Progressive | Variable | HP:0100261 (neuropathic joint) |
| Distal muscle wasting/weakness | Clinical sign | After sensory onset | Variable; sometimes early/severe | Variable | HP:0003693 (distal amyotrophy); HP:0002460 |
| Autonomic involvement (e.g., distal hypohidrosis) | Symptom | Variable | Variable | Variable/mild | HP:0000966 (hypohidrosis) |
| Sensorineural hearing loss (variant families) | Clinical sign | Adult | Variable | Subset | HP:0000407 |

**Onset, severity, progression, frequency.** Onset is typically the second-to-third decade, with initial sensory loss in the feet followed by distal muscle wasting and weakness; as the original gene-identification paper states, *"Initial symptoms are sensory loss in the feet followed by distal muscle wasting and weakness. Loss of pain sensation leads to chronic skin ulcers and distal amputations"* ([PMID: 11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/)). The course is chronic and slowly progressive, with reduced penetrance in some carriers and earlier onset in younger generations (anticipation) ([PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/)).

**Quality-of-life impact.** Insensate feet, recurrent ulceration, osteomyelitis, chronic neuropathic pain, and amputations produce substantial disability affecting mobility, employment, and self-care. Disease-specific QoL instruments are not established; the CMT Neuropathy Score (CMTNS) is used as a composite disability/severity outcome ([PMID: 30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/)).

---

## 4. Genetic / Molecular Information

**Causal gene.** *SPTLC1* (serine palmitoyltransferase long chain base subunit 1), 9q22.31, OMIM 605712, HGNC:11277. It encodes subunit 1 of the SPT heterodimer (with SPTLC2/SPTLC3), the rate-limiting, PLP-dependent enzyme of de novo sphingolipid synthesis. Dawkins et al. mapped *SPTLC1* to chromosome 9q22.1–22.3 and confirmed it as the HSN1 gene: *"We found two mutations to be located in exon 5 (C133Y and C133W) and one mutation to be located in exon 6 of SPTLC1 (V144D). All families showing definite or probable linkage to chromosome 9 had mutations in these two exons"* ([PMID: 11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/)).

**Pathogenic variants (HSAN1A).**

| Variant (protein) | cDNA | Exon | Class | Notes |
|---|---|---|---|---|
| p.Cys133Trp | c.399T>G | 5 | Pathogenic | Most common; southern-English founder allele |
| p.Cys133Tyr | — | 5 | Pathogenic | Original cohort |
| p.Val144Asp | — | 6 | Pathogenic | Original cohort |
| p.Ser331Phe / p.Ser331Tyr | — | — | Pathogenic | "Ser331 syndrome" — severe, HSAN1A + motor neuron disease overlap |

- **Classification:** Established *SPTLC1* HSAN1 variants are ACMG **Pathogenic/Likely Pathogenic** (functional data + segregation + absence from population databases).
- **Variant type/class:** Predominantly **missense**; disease acts by altered substrate specificity, not truncation.
- **Allele frequency:** Pathogenic alleles are essentially absent from gnomAD/population databases.
- **Origin:** **Germline**, autosomal dominant. Parental **mosaicism** has been documented for the allelic ALS branch (asymptomatic parent with ~17% mosaic p.Ala20Thr; [PMID: 39666121](https://pubmed.ncbi.nlm.nih.gov/39666121/)).
- **Functional consequence:** **Neomorphic gain of function** — shift to L-alanine/glycine usage → 1-deoxySL production ([PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/)).

**Allelic branch (distinct disease).** *SPTLC1* transmembrane-domain variants (p.Ala20Ser, p.Ala20Thr, p.Leu38Arg, p.Ser331Tyr) impair binding of ORMDL (negative regulators of SPT), releasing feedback inhibition and increasing overall canonical sphingolipid synthesis (sphinganines/ceramides) → **juvenile/childhood-onset ALS** rather than HSAN1A. Johnson et al. report *"De novo variants in SPTLC1 (p.Ala20Ser in 2 patients and p.Ser331Tyr in 1 patient)"* causing juvenile ALS ([PMID: 34459874](https://pubmed.ncbi.nlm.nih.gov/34459874/)), and the mechanism is that *"SPTLC1-ALS variants map to a transmembrane domain that interacts with ORMDL proteins... ORMDL binding to the holoenzyme complex is impaired in cells expressing pathogenic SPTLC1-ALS alleles, resulting in increased SL synthesis and a distinct lipid signature"* ([PMID: 35900868](https://pubmed.ncbi.nlm.nih.gov/35900868/); [PMID: 37348646](https://pubmed.ncbi.nlm.nih.gov/37348646/)). The p.Ser331 variants uniquely show *"the coexistence of neurotoxic deoxy-sphingolipids with an excess of canonical products of the SPT enzyme"* ([PMID: 35904184](https://pubmed.ncbi.nlm.nih.gov/35904184/); [PMID: 36964315](https://pubmed.ncbi.nlm.nih.gov/36964315/)).

**Modifier genes.** SPTSSA/SPTSSB (small SPT subunits; yeast Tsc3) tune serine-versus-alanine choice and may modify deoxySL output; *"hereditary sensory and autonomic neuropathy type I results from SPT mutations that cause an abnormal accumulation of alanine-derived SPLs. The regulatory mechanism for SPT amino acid selectivity ... [is] unknown"* ([PMID: 30154231](https://pubmed.ncbi.nlm.nih.gov/30154231/)).

**Epigenetic / chromosomal.** No specific epigenetic signature or chromosomal abnormality is implicated; the disorder is a single-gene point-mutation disease.

---

## 5. Environmental Information

- **Environmental / dietary factors:** The dominant non-genetic modifier is **amino-acid availability** — L-serine (protective) versus L-alanine (aggravating), demonstrated by diet manipulation in transgenic mice ([PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/)).
- **Chemical/toxin relevance:** 1-DeoxySLs also mediate **chemotherapy-induced peripheral neuropathy** (paclitaxel, docetaxel), where SPT uses L-alanine and 1-deoxySLs accumulate in DRG — a convergent mechanism relevant to disease modeling but not a cause of HSAN1A itself ([PMID: 32058598](https://pubmed.ncbi.nlm.nih.gov/32058598/)).
- **Lifestyle factors:** No established smoking/alcohol/exercise associations specific to HSAN1A.
- **Infectious agents:** Not applicable — HSAN1A is a monogenic disorder. (Secondary wound infections/osteomyelitis are complications, not causes.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A heterozygous **missense mutation in *SPTLC1*** (e.g., p.Cys133Trp) alters an active-site–proximal residue of the SPT catalytic core → **leads to** a change in the enzyme's amino-acid substrate selectivity.
2. Mutant SPT **condenses palmitoyl-CoA with L-alanine and glycine** instead of L-serine → **results in** synthesis of atypical **1-deoxysphinganine and 1-deoxymethylsphinganine (1-deoxySLs)**. As stated for HSAN1: *"1-Deoxysphingolipids (1-deoxySL) are atypical and neurotoxic sphingolipids formed by alternate substrate usage of the enzyme serine-palmitoyltransferase. Pathologically increased 1-deoxySL formation causes hereditary sensory and autosomal neuropathy type 1 (HSAN1)"* ([PMID: 27016021](https://pubmed.ncbi.nlm.nih.gov/27016021/)).
3. Because 1-deoxySLs **lack the C1 hydroxyl**, they **cannot** be converted to complex sphingolipids or enter the canonical degradation pathway (S1P-lyase route) → **leads to** their intracellular and circulating **accumulation** (elevated in patient plasma; used as a biomarker).
4. Accumulated 1-deoxySLs are **neurotoxic** to sensory neurons → **cause** (branch):
   - 4a. **Ca²⁺ handling abnormalities** and **mitochondrial dysfunction** ([PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/));
   - 4b. **Cytoskeletal disruption** (neurite/axon swelling, retraction);
   - 4c. **NMDA-receptor-mediated excitotoxic signaling** ([PMID: 27016021](https://pubmed.ncbi.nlm.nih.gov/27016021/)).
5. These converge on **dose- and time-dependent reduction of neurite length and neuronal survival** → **results in** degeneration of long **dorsal-root-ganglion (DRG) sensory neurons** and their axons (length-dependent, distal-first).
6. Distal sensory axonopathy **leads to** loss of protective pain/temperature sensation, neuropathic pain, and (variably) distal motor axon loss → **results in** the clinical picture of ulceromutilating sensory neuropathy.
7. Loss of protective sensation → **causes** repeated unperceived trauma → **leads to** foot ulcers → **osteomyelitis**, **Charcot arthropathy**, and **distal amputations** (downstream, secondary tissue-injury cascade).

*Branch (allelic, not HSAN1A):* Transmembrane *SPTLC1* variants **impair ORMDL/ceramide feedback** → **increase canonical sphingolipid synthesis** → **juvenile ALS/motor neuron degeneration**; structurally, *"childhood amyotrophic lateral sclerosis (ALS) variants in the SPTLC1 subunit cause impaired ceramide sensing in the SPT-ORMDL3 mutants"* ([PMID: 35900868](https://pubmed.ncbi.nlm.nih.gov/35900868/); [PMID: 37308477](https://pubmed.ncbi.nlm.nih.gov/37308477/)).

### Detail by category

- **Molecular pathways / biochemistry:** De novo sphingolipid biosynthesis (SPT is the rate-limiting, PLP-dependent condensation step). The defect is a **substrate-specificity shift** producing 1-deoxySLs. Upstream driver = mutation; downstream = lipotoxicity.
- **Cellular processes:** Mitochondrial dysfunction, disrupted Ca²⁺ homeostasis, cytoskeletal/axonal transport failure, and excitotoxicity; net effect is neuronal apoptosis/axon degeneration ([PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/); [PMID: 27016021](https://pubmed.ncbi.nlm.nih.gov/27016021/)).
- **Protein dysfunction:** The mutant SPT holoenzyme is not simply inactivated — it is functionally **reprogrammed** (neomorphic). Cryo-EM shows *"SPTLC1 and SPTLC2 form a dimer of heterodimers as the catalytic core. SPTssa participates in acyl-CoA coordination, thereby stimulating the SPT activity and regulating the substrate selectivity. ORMDL3 is located in the center of the complex, serving to stabilize the SPT assembly"* ([PMID: 33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/)).
- **Metabolic changes:** Diversion of sphingoid-base synthesis toward 1-deoxy species; sensitivity to serine/alanine ratio.
- **Molecular profiling:** iPSC-derived HSN1 neurons show L-serine-responsive deficits in neuronal **ganglioside composition** and axoglial interactions ([PMID: 34337561](https://pubmed.ncbi.nlm.nih.gov/34337561/)). DRG transcriptomics in an S331F mouse implicate mitochondrial pathways, reversible by allele-specific ASO ([PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)).

**Suggested ontology terms.** GO: sphingolipid biosynthetic process (GO:0030148); serine C-palmitoyltransferase activity (GO:0004758); neuron apoptotic process (GO:0051402); mitochondrion organization (GO:0007005). CL: neuron of dorsal root ganglion / sensory neuron (CL:0000101, CL:0000210). CHEBI: 1-deoxysphinganine; sphinganine; L-serine (CHEBI:17115); L-alanine (CHEBI:16977).

---

## 7. Anatomical Structures Affected

- **Organ/body system level:** **Peripheral nervous system** — primary. Predominantly the **somatosensory** system; variable **motor** and **autonomic** involvement. Secondary: **skin** (ulcers), **bone/joints** (osteomyelitis, acro-osteolysis, Charcot joints), and distal **extremities** (amputations).
- **Tissue/cell level:** **Nervous tissue** — dorsal root ganglion **sensory neurons** and their **peripheral axons** (long-fiber, length-dependent). Small (pain/temperature) fibers are prominently affected; myelinated large fibers also lost. Cell Ontology: dorsal root ganglion neuron (CL:0000101), sensory neuron (CL:0000210).
- **Subcellular level:** **Mitochondria** (dysfunction), **endoplasmic reticulum** (SPT is an ER-membrane enzyme; site of the primary lesion), **plasma membrane/cytoskeleton**. GO cellular component: endoplasmic reticulum membrane (GO:0005789); serine C-palmitoyltransferase complex (GO:0017059); mitochondrion (GO:0005739).
- **Localization (UBERON):** dorsal root ganglion (UBERON:0000044); peripheral nerve/sural nerve (UBERON:0001323); sciatic nerve (UBERON:0001322); skin of foot (UBERON:0001513). Distribution is **bilateral and symmetric, distal > proximal, lower limbs > upper limbs**. In allelic MacTel-2 families, the **retina/macula** (UBERON:0000966) is additionally affected.

---

## 8. Temporal Development

- **Onset:** Typically **adult, second-to-third decade**; **insidious/chronic** onset. Anticipation (earlier onset in successive generations) is reported ([PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/)). The Ser331 and allelic ALS variants shift onset to childhood/juvenile.
- **Progression:** Slowly **progressive**, chronic, lifelong. Course begins with distal sensory loss, then distal wasting/weakness and ulceromutilating complications ([PMID: 11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/)).
- **Stages (descriptive):** early (subclinical/sensory symptoms) → intermediate (established sensory loss, neuropathic pain, early ulceration) → advanced (osteomyelitis, Charcot joints, amputations, motor deficits).
- **Patterns:** No spontaneous remission; deterioration is generally steady. **Critical intervention window:** earlier initiation of 1-deoxySL-lowering therapy (L-serine) before irreversible axon loss is expected to be more beneficial — supported by neonatal-vs-adult efficacy signals in ASO mouse studies ([PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant**. **Penetrance is incomplete** and **expressivity variable**; apparent **anticipation** occurs. Houlden et al. describe *"lack of penetrance of the SPTLC1 mutation in some individuals, variability in age of onset along with an earlier age of onset in younger generations, in some patients surprisingly early and often severe motor involvement"* ([PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/)).
- **Epidemiology:** HSAN1 overall is rare (broad HSAN prevalence estimates ~1/100,000–1/1,000,000). In a UK cohort, HSAN gene mutations were found in **14.3% (25/140)** of index patients, and *"The p.Cys133Trp mutation in SPTLC1 is the most common cause of HSAN in the UK population and should be screened first in all patients with sporadic or autosomal dominant HSAN"* ([PMID: 22302274](https://pubmed.ncbi.nlm.nih.gov/22302274/)).
- **Founder effects:** The **p.Cys133Trp (c.399T>G)** allele traces to a common **southern-English founder**: *"The Australian and English families may therefore have a common founder who, on the basis of historical information, has been determined to have lived in southern England prior to 1800"* ([PMID: 11479835](https://pubmed.ncbi.nlm.nih.gov/11479835/)).
- **Germline mosaicism:** Documented for the allelic ALS branch (parental mosaicism ~17%; [PMID: 39666121](https://pubmed.ncbi.nlm.nih.gov/39666121/)).
- **Consanguinity/carrier frequency:** Not relevant for this dominant disorder (unlike recessive HSANs, e.g., HSAN4/*NTRK1*, where consanguinity and founder variants matter — [PMID: 41474134](https://pubmed.ncbi.nlm.nih.gov/41474134/)).
- **Demographics:** Both sexes affected; some families show **earlier/more severe motor involvement in males** ([PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/)). Geographic clustering follows founder-allele dispersal (UK, Australia, Europe/North America).

---

## 10. Diagnostics

**Clinical/electrophysiology.**
- **Nerve conduction studies / EMG:** predominantly **sensory axonal neuropathy** (reduced/absent sensory nerve action potentials), with variable motor axonal features ([PMID: 16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/)).
- **Skin biopsy (PGP9.5):** reduced **intraepidermal nerve-fiber density**; **sural nerve biopsy:** loss of myelinated (and non-myelinated) axons.
- **Quantitative sensory testing:** abnormal small-fiber thresholds early.

**Biomarker.** **Elevated plasma 1-deoxysphingolipids (1-deoxySL)** are a disease-specific biochemical marker and pharmacodynamic readout (they fall with L-serine or ASO therapy) ([PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/); [PMID: 30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/); [PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)).

**Genetic testing.** Sequence *SPTLC1* first (especially p.Cys133Trp in UK/founder populations; [PMID: 22302274](https://pubmed.ncbi.nlm.nih.gov/22302274/)). A **hereditary neuropathy gene panel** (or WES/WGS) covering *SPTLC1, SPTLC2, RAB7A (CMT2B), NTRK1, IKBKAP/ELP1, WNK1/HSN2, ATL1, DNMT1, RFC1*, etc., resolves genetically heterogeneous cases ([PMID: 40211677](https://pubmed.ncbi.nlm.nih.gov/40211677/)). Single-gene testing suffices when a familial variant is known.

**Differential diagnosis.**
- **HSAN1C** (*SPTLC2*, e.g., p.Arg183Trp): later onset (>50), also raises 1-deoxySLs ([PMID: 26573920](https://pubmed.ncbi.nlm.nih.gov/26573920/)).
- **HSN with cough/GERD** (chromosome 3p22–p24 linked): distinct autonomic/aerodigestive features ([PMID: 16311270](https://pubmed.ncbi.nlm.nih.gov/16311270/)).
- **HSAN4 (CIPA, *NTRK1*)**: congenital, anhidrosis, insensitivity to pain, intellectual disability — recessive ([PMID: 41474134](https://pubmed.ncbi.nlm.nih.gov/41474134/); [PMID: 41257813](https://pubmed.ncbi.nlm.nih.gov/41257813/)).
- **Hereditary transthyretin (ATTRv) amyloid polyneuropathy**: sensorimotor + autonomic + cardiac, later onset, amyloid on biopsy ([PMID: 23425518](https://pubmed.ncbi.nlm.nih.gov/23425518/)).
- **CMT2B (*RAB7A*)** and other CMT/HNPP forms with ulceromutilating/overlap features ([PMID: 41179108](https://pubmed.ncbi.nlm.nih.gov/41179108/)).
- **RFC1 (CANVAS), PUM1, COX20**-related sensory neuropathies/ataxia ([PMID: 40211677](https://pubmed.ncbi.nlm.nih.gov/40211677/)).

**Screening.** Not part of newborn screening. **Cascade genetic testing** of at-risk relatives and predictive testing with genetic counseling are appropriate given AD inheritance.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** HSAN1A itself is **not typically life-limiting**; life expectancy is largely preserved. Mortality risk is indirect (sepsis from osteomyelitis, complications of amputation). The allelic **juvenile ALS branch** carries a serious motor-neuron-disease prognosis (though a 30-year survivor is reported — [PMID: 37497262](https://pubmed.ncbi.nlm.nih.gov/37497262/)).
- **Morbidity/disability:** High — chronic neuropathic pain, insensate feet, recurrent ulcers, osteomyelitis, Charcot arthropathy, and amputations drive long-term functional impairment ([PMID: 15319794](https://pubmed.ncbi.nlm.nih.gov/15319794/); [PMID: 12633143](https://pubmed.ncbi.nlm.nih.gov/12633143/)).
- **Disease course/complications:** Progressive; complications are largely preventable with meticulous foot care.
- **Prognostic factors:** Earlier onset, motor involvement (e.g., Ser331 variants), and higher 1-deoxySL burden predict worse course. **Plasma 1-deoxySL** serves as a prognostic/pharmacodynamic biomarker; **CMTNS** tracks disability.
- **Recovery potential:** Established axon loss is largely irreversible; disease-modifying therapy aims to **slow** progression rather than reverse deficits — motivating early intervention.

---

## 12. Treatment

**Disease-modifying — high-dose oral L-serine (first-line, evidence-based).** A randomized, placebo-controlled trial (NCT01733407; n=18; **400 mg/kg/day** L-serine for 1 year plus open-label extension) showed *"After 1 year, the l-serine group experienced improvement in CMTNS relative to the placebo group (-1.5 units, 95% CI -2.8 to -0.1)"*, providing **Class I evidence** that L-serine slows progression; it was safe and lowered plasma deoxysphingolipids ([PMID: 30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/)). Mechanistic basis: *"In mice bearing a transgene expressing the C133W SPTLC1 mutant linked to HSAN1, a 10% L-serine–enriched diet reduced dSL levels. L-serine supplementation also improved measures of motor and sensory performance"* ([PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/)). NCIT: L-Serine.

**Emerging — allele-specific antisense oligonucleotides (ASOs).** In S331F HSN1 mice, GalNAc-conjugated LNA gapmer ASOs achieved **>90% mutant-transcript silencing** in liver, DRG, and sciatic nerve without affecting wild-type transcript, **reduced blood 1-deoxySLs**, and reversed aberrant DRG gene expression — preclinical proof of concept for allele-specific silencing ([PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)). NCIT: Antisense Oligonucleotide Therapy.

**Symptomatic / supportive.**
- **Neuropathic pain:** standard agents (gabapentinoids, duloxetine, tricyclics, carbamazepine/oxcarbazepine for lancinating pain). NCIT: Gabapentin, Duloxetine.
- **Ulcer/wound & foot care:** meticulous podiatric surveillance, protective footwear, offloading, infection control, orthopedic/surgical management of osteomyelitis and Charcot joints — the cornerstone of preventing amputations ([PMID: 41161998](https://pubmed.ncbi.nlm.nih.gov/41161998/)).
- **Rehabilitation:** physical/occupational therapy to preserve range of motion, strength, and balance ([PMID: 41161998](https://pubmed.ncbi.nlm.nih.gov/41161998/)).

**Genotype-guided strategy.** Because catalytic-pocket (HSAN1A) versus transmembrane (ALS) *SPTLC1* variants produce opposite lipid signatures (1-deoxySL excess vs. canonical-SL excess), **therapy must be tailored to genotype/lipid profile**; L-serine targets the 1-deoxySL (HSAN1A) mechanism specifically ([PMID: 35900868](https://pubmed.ncbi.nlm.nih.gov/35900868/); [PMID: 35904184](https://pubmed.ncbi.nlm.nih.gov/35904184/)).

**Pharmacogenomics:** No established PGx dosing guidance specific to HSAN1A.

---

## 13. Prevention

- **Primary prevention:** Not preventable at the population level (Mendelian). **Genetic counseling, prenatal/preimplantation genetic testing**, and reproductive options can prevent transmission. **Dietary L-serine adequacy / avoidance of alanine-loading** may reduce metabolic aggravation in carriers (mechanistically supported; [PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/)).
- **Secondary prevention:** **Cascade genetic testing** of relatives; early biochemical (plasma 1-deoxySL) and neurophysiological monitoring to start disease-modifying therapy before advanced axon loss.
- **Tertiary prevention (most impactful):** Meticulous **foot care and wound surveillance** to prevent ulcers, osteomyelitis, and amputations; pain management; multidisciplinary neuromuscular care.
- **Counseling:** Autosomal-dominant recurrence risk 50%; discuss incomplete penetrance, variable expressivity, anticipation, and the possibility of the allelic ALS phenotype for specific variants.
- **Immunization / public-health / environmental interventions:** Not applicable (non-infectious, monogenic).

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** *Sptlc1* in mouse (NCBI Gene ID 268656) and rat; highly evolutionarily conserved SPT machinery (yeast LCB1/LCB2 with Tsc3 small subunit).
- **Naturally occurring disease:** **Hereditary sensory and autonomic neuropathies occur naturally in dogs**; a retrospective series of 11 dogs described early-onset distal sensory loss with acral mutilation and two electroclinical patterns of differing prognosis, mirroring human ulceromutilating HSAN ([PMID: 42658782](https://pubmed.ncbi.nlm.nih.gov/42658782/)). (OMIA catalogs several canine sensory neuropathies.)
- **Comparative biology/conservation:** The serine/alanine substrate-selectivity mechanism is conserved from yeast (Tsc3 regulating SPT amino-acid choice; [PMID: 30154231](https://pubmed.ncbi.nlm.nih.gov/30154231/)) to humans, underpinning cross-species model validity.
- **Zoonotic potential:** None (genetic disease).

---

## 15. Model Organisms

**Mammalian genetic models (mouse).**
- **C133W *SPTLC1* transgenic mouse** — expresses the human HSAN1 mutation; accumulates deoxysphingolipids and shows sensory/motor deficits. Dietary L-serine lowered dSL and improved performance; L-alanine worsened it — the model that established the L-serine therapeutic rationale ([PMID: 22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/)).
- **S331F *Sptlc1* knock-in mouse** — heterozygous p.S331F; elevated blood 1-deoxySLs; DRG transcriptomic (mitochondrial) changes; used for allele-specific ASO proof of concept ([PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)).
- **Precision *Sptlc1* HSAN1 mouse models** engineered to recapitulate patient genetics/pathophysiology ([PMID: 34875719](https://pubmed.ncbi.nlm.nih.gov/34875719/)).

**Cellular / in vitro models.**
- **Patient iPSC-derived sensory neurons** — reveal L-serine-responsive deficits in ganglioside composition and axoglial interactions, providing a human cellular platform ([PMID: 34337561](https://pubmed.ncbi.nlm.nih.gov/34337561/)).
- **HEK293 / primary DRG cultures** — used to demonstrate 1-deoxySL neurotoxicity (Ca²⁺, mitochondrial, NMDA-receptor, cytoskeletal effects) and to assay mutant SPT activity ([PMID: 29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/); [PMID: 27016021](https://pubmed.ncbi.nlm.nih.gov/27016021/)).
- **Yeast (*S. cerevisiae*)** — Tsc3/LCB system to dissect SPT amino-acid selectivity ([PMID: 30154231](https://pubmed.ncbi.nlm.nih.gov/30154231/)).

**Phenotype recapitulation & limitations.** Mouse models reproduce the biochemical signature (elevated 1-deoxySLs) and sensory/motor deficits and respond to dSL-lowering interventions, validating mechanism and therapy. Limitations include incomplete recapitulation of the full ulceromutilating human phenotype (chronic ulcers, osteomyelitis, amputations), and differences in disease tempo. Naturally occurring canine HSAN offers a complementary large-animal comparator ([PMID: 42658782](https://pubmed.ncbi.nlm.nih.gov/42658782/)).

---

## Mechanistic Model / Interpretation

```
 SPTLC1 missense (e.g., C133W)  ── catalytic-pocket ──► altered SPT substrate selectivity
        │                                                     │
        │                                    (L-serine  →  L-alanine / glycine)
        │                                                     ▼
        │                                    1-deoxysphinganine + 1-deoxymethylsphinganine
        │                                    (no C1-OH → cannot be complexed or degraded)
        │                                                     ▼
        │                               ACCUMULATION (plasma biomarker ↑)
        │                                                     ▼
        │             ┌───────────────┬────────────────┬───────────────────┐
        │        Ca2+ dysreg.   mito dysfunction   cytoskeletal      NMDA-R excitotoxicity
        │             └───────────────┴────────────────┴───────────────────┘
        │                                                     ▼
        │                      DRG sensory neuron / long-axon degeneration
        │                                                     ▼
        │             distal sensory loss + neuropathic pain (± motor)
        │                                                     ▼
        │             unperceived trauma → ulcers → osteomyelitis → amputation
        │
        └── (ALLELIC BRANCH) transmembrane variant (A20S/T, L38R, S331Y)
                 └─► impaired ORMDL/ceramide feedback ─► ↑ canonical sphingolipids
                                                         ─► JUVENILE ALS (distinct disease)

THERAPY: L-serine competes L-alanine at the active site → ↓1-deoxySL → slows progression
         Allele-specific ASO → silences mutant transcript → ↓1-deoxySL (preclinical)
```

**Upstream vs downstream.** The mutation and substrate shift are the **upstream** initiating lesion; 1-deoxySL accumulation is the pivotal **intermediate node** (and the therapeutic target); neuronal degeneration and ulceromutilating complications are **downstream**. The elegance of HSAN1A is that a single upstream metabolic diversion is both the biomarker source and the drug target.

**A shared mechanism beyond nerve.** The same 1-deoxySL/serine-deficiency axis links HSAN1A to **macular telangiectasia type 2**: *"Two variants known to cause HSAN1 were identified as causal for macular telangiectasia type 2: of 11 patients with HSAN1, 9 also had macular telangiectasia type 2. Circulating deoxysphingolipid levels were 84.2% higher among 125 patients with macular telangiectasia type 2 who did not have pathogenic variants affecting SPT than among 94 unaffected controls"* ([PMID: 31509666](https://pubmed.ncbi.nlm.nih.gov/31509666/)). This argues HSAN1A patients may harbor sub-clinical maculopathy and broadens the therapeutic rationale for serine.

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [11242114](https://pubmed.ncbi.nlm.nih.gov/11242114/) | Identifies *SPTLC1* (C133Y, C133W, V144D); core clinical course | Human genetics |
| [11479835](https://pubmed.ncbi.nlm.nih.gov/11479835/) | Southern-English founder for C133W (399T>G) | Haplotype analysis |
| [22302274](https://pubmed.ncbi.nlm.nih.gov/22302274/) | C133W most common HSAN cause in UK; screen first | Cohort/epidemiology |
| [16364956](https://pubmed.ncbi.nlm.nih.gov/16364956/) | Reduced penetrance, anticipation, motor involvement | Clinical/path/genetic |
| [29778900](https://pubmed.ncbi.nlm.nih.gov/29778900/) | 1-deoxySL neurotoxicity: Ca²⁺, mitochondria; substrate-shift | In vitro |
| [27016021](https://pubmed.ncbi.nlm.nih.gov/27016021/) | NMDA-receptor-mediated 1-deoxySL toxicity | In vitro |
| [22045570](https://pubmed.ncbi.nlm.nih.gov/22045570/) | L-serine lowers dSL, improves mice; alanine worsens | Model organism + human |
| [30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/) | RCT: L-serine improves CMTNS by −1.5 (Class I) | Human RCT |
| [33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/) | Cryo-EM SPT–ssSPT–ORMDL3; substrate selectivity | Structural |
| [37308477](https://pubmed.ncbi.nlm.nih.gov/37308477/) | Ceramide sensing; ALS variants impair feedback | Structural |
| [35900868](https://pubmed.ncbi.nlm.nih.gov/35900868/) | TM-domain variants impair ORMDL → ALS lipid signature | Functional |
| [35904184](https://pubmed.ncbi.nlm.nih.gov/35904184/) | Ser331 combines deoxySL + excess canonical SL | Functional/clinical |
| [34459874](https://pubmed.ncbi.nlm.nih.gov/34459874/) | De novo TM variants → juvenile ALS | Human genetics |
| [31509666](https://pubmed.ncbi.nlm.nih.gov/31509666/) | Links SPT/serine/deoxySL to MacTel-2 retina | Human + model |
| [30154231](https://pubmed.ncbi.nlm.nih.gov/30154231/) | Tsc3/small subunit regulates serine-vs-alanine choice | Yeast |
| [41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/) | Allele-specific ASO reverses phenotype in S331F mice | Model organism |
| [34337561](https://pubmed.ncbi.nlm.nih.gov/34337561/) | iPSC model: L-serine-responsive ganglioside deficits | In vitro (human) |
| [26573920](https://pubmed.ncbi.nlm.nih.gov/26573920/) | *SPTLC2* HSAN1C, late-onset, raises deoxySL | Human genetics |

---

## Limitations and Knowledge Gaps

1. **Small trial size.** The pivotal L-serine RCT enrolled only 18 patients ([PMID: 30626650](https://pubmed.ncbi.nlm.nih.gov/30626650/)); long-term efficacy, optimal dose, and hard clinical endpoints (ulcer/amputation rates) need larger, longer studies.
2. **Epidemiology is imprecise.** Prevalence/incidence figures are rough; systematic registry data are lacking. The 14.3% figure is mutation-detection frequency in a referral cohort, not population prevalence.
3. **Genotype–phenotype resolution.** Why some carriers are non-penetrant and what drives anticipation and sex-related motor severity remain unexplained; modifier genes (SPTSSA/SPTSSB) are hypothesized but not clinically validated.
4. **Model gaps.** Rodent models capture biochemistry and mild deficits but not the full ulceromutilating phenotype; no model fully recapitulates human complications.
5. **ASO stage.** Allele-specific silencing is preclinical; human safety/efficacy unproven ([PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)).
6. **Retinal comorbidity.** The frequency of clinically significant MacTel-2 in HSAN1A patients and whether serine therapy protects the retina are unquantified ([PMID: 31509666](https://pubmed.ncbi.nlm.nih.gov/31509666/)).
7. **QoL data.** No disease-specific quality-of-life instrument or systematic QoL dataset exists for HSAN1A.

---

## Proposed Follow-up Experiments / Actions

1. **Larger, longer L-serine trial** with clinically meaningful endpoints (ulcer incidence, amputation-free survival, intraepidermal nerve-fiber density) and defined 1-deoxySL pharmacodynamic targets.
2. **First-in-human allele-specific ASO** program building on GalNAc-LNA data ([PMID: 41124364](https://pubmed.ncbi.nlm.nih.gov/41124364/)), with pan-allele and mutation-specific designs.
3. **Prospective natural-history registry** capturing onset, progression rate, penetrance, sex effects, and genotype-specific outcomes to power prognostic modeling.
4. **Systematic retinal screening (OCT)** of genetically confirmed HSAN1A patients to define MacTel-2 co-occurrence and test whether serine is retino-protective.
5. **Modifier-gene study** of SPTSSA/SPTSSB and serine-metabolism genes to explain penetrance/expressivity variability and identify additional therapeutic levers.
6. **Standardized biomarker assay** for plasma 1-deoxySLs to serve as a validated companion diagnostic/pharmacodynamic endpoint across centers.
7. **Genotype-stratified care pathway** formalizing the catalytic-pocket (HSAN1A) vs transmembrane (ALS) distinction to route patients to appropriate therapy and prognosis.

---

*Evidence source legend:* Human clinical/genetics (family cohorts, RCT), model organism (transgenic/knock-in mouse, dog, yeast), in vitro (iPSC neurons, DRG/HEK cultures), and computational/structural (cryo-EM). Ontology suggestions provided per section (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) for knowledge-base ingestion.


## Artifacts

- [OpenScientist final report](Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1A-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hereditary_Sensory_and_Autonomic_Neuropathy_Type_1A-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 25 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008086` (2 mentions) - the report calls it "MONDO"; MONDO calls it **neuropathy, hereditary sensory and autonomic, type 1A**
- `HP:0012060` (1 mention) - the report calls it "acro-osteolysis"; HP calls it **Acral lentiginous melanoma**
- `HP:0100261` (1 mention) - the report calls it "neuropathic joint"; HP calls it **Abnormal tendon morphology**
- `HP:0000407` (1 mention) - the report calls it "Subset"; HP calls it **Sensorineural hearing impairment**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0106487` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000966` (1 mention) - the report calls it "retina/macula"; UBERON calls it **retina**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.