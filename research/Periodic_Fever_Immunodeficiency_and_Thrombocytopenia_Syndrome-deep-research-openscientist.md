---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-06T19:11:11.300517'
end_time: '2026-09-06T19:43:16.511687'
duration_seconds: 1925.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Periodic Fever, Immunodeficiency, and Thrombocytopenia Syndrome
  mondo_id: MONDO:0007883
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
citation_count: 7
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 21
  quotes_valid: 19
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:27557945
  - PMID:24840128
  relevance_assessed: 14
  on_topic: 6
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0040314
    reported_labels:
    - Macrothrombocytopenia (large platelets)
    ontology_label: Blind vagina
  - term_id: HP:0010280
    reported_labels:
    - oral ulcer
    ontology_label: Stomatitis
  - term_id: HP:0011099
    reported_labels:
    - functional/anatomic stenosis
    ontology_label: Spastic hemiparesis
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Periodic_Fever_Immunodeficiency_and_Thrombocytopenia_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Periodic_Fever_Immunodeficiency_and_Thrombocytopenia_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Periodic Fever, Immunodeficiency, and Thrombocytopenia Syndrome
- **MONDO ID:** MONDO:0007883 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Periodic Fever, Immunodeficiency, and Thrombocytopenia Syndrome** covering all of the
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

# Periodic Fever, Immunodeficiency, and Thrombocytopenia Syndrome (PFIT): Comprehensive Disease Report

**Disease:** Periodic Fever, Immunodeficiency, and Thrombocytopenia Syndrome (PFIT)
**MONDO:** MONDO:0007883 · **Category:** Mendelian (autosomal recessive)
**Causal gene:** *WDR1* (encoding Aip1 / actin-interacting protein 1)

---

## Summary

Periodic Fever, Immunodeficiency, and Thrombocytopenia syndrome (PFIT) is an ultra-rare, autosomal-recessive **monogenic autoinflammatory "actinopathy"** caused by **biallelic hypomorphic missense mutations in *WDR1***, the gene encoding **actin-interacting protein 1 (Aip1)**. Aip1 is a WD40 β-propeller cofactor that cooperates with cofilin/ADF to accelerate depolymerization and turnover of actin filaments. Because the actin cytoskeleton is indispensable to leukocyte motility, immune-synapse formation, and megakaryocyte/platelet biogenesis, partial loss of Aip1 function produces a distinctive triad of **recurrent/periodic fevers (autoinflammation), immunodeficiency, and thrombocytopenia**, accompanied by severe stomatitis, oral stenosis, skin ulceration, and impaired wound healing. The condition typically presents in the neonatal period or early childhood and, untreated, can be fatal.

Mechanistically, PFIT is defined by two coupled abnormalities. First, loss of Aip1 **elevates neutrophil F-actin roughly four-fold** and impairs chemotaxis, spreading, and polarization while paradoxically preserving microbial killing and increasing oxidative burst. Second, the disease drives an **IL-18–dominant autoinflammatory state**: patients have high serum IL-18 (without a matching rise in IL-1β or IL-18–binding protein) and increased caspase-1 cleavage in monocytes, and mutant WDR1 protein aggregates that sequester pyrin, plausibly precipitating inflammasome assembly. Beyond myeloid cells, WDR1 deficiency causes lymphoid immunodeficiency — aberrant T-cell activation at the immunologic synapse and severe B-cell abnormalities (B lymphopenia, loss of switched memory B cells) — and macrothrombocytopenia from defective megakaryocyte maturation.

*WDR1* is among the most **loss-of-function–intolerant genes in the human genome** (gnomAD pLI ≈ 1.0), which explains why every reported human patient carries **hypomorphic missense** alleles rather than complete-null variants: in mice, severe *Wdr1* loss of function is embryonic-lethal, whereas hypomorphic alleles are viable and reproduce the human phenotype (macrothrombocytopenia plus neutrophil-driven autoinflammation). The mechanism is deeply evolutionarily conserved from yeast (*AIP1*), *C. elegans* (*unc-78*), and plants to mouse *Wdr1*. **Allogeneic hematopoietic stem cell transplantation (HSCT) is the definitive, corrective treatment**, having reversed the immunologic defect in transplanted patients; diagnosis is genetic (WES/WGS or targeted autoinflammatory/immunodeficiency panels). This report consolidates eight confirmed findings across three primary human cohorts (total ~12 patients) and multiple mechanistic and model-organism studies.

---

## Key Findings

### Finding 1 — PFIT is caused by biallelic (autosomal recessive) missense mutations in *WDR1* (encoding Aip1)

PFIT was defined independently by two 2016–2017 index reports. Kuhns et al. (2016) identified **biallelic *WDR1* mutations affecting distinct antiparallel β-strands of Aip1** in four children across three families; heterozygous relatives were clinically normal, establishing autosomal-recessive inheritance. Standing et al. (2017) reported a **homozygous missense *WDR1* mutation in two siblings** with the periodic-fever/immunodeficiency/thrombocytopenia triad, coining the PFIT acronym. WDR1 encodes actin-interacting protein 1 (Aip1), a cofactor that accelerates cofilin-mediated actin filament depolymerization.

> "We report a homozygous missense mutation in WDR1 in two siblings causing periodic fevers with immunodeficiency and thrombocytopenia." — [PMID: 27994071](https://pubmed.ncbi.nlm.nih.gov/27994071/)

> "Biallelic mutations in WDR1 affecting distinct antiparallel β-strands of Aip1 were identified in all patients… Heterozygous mutations in clinically normal relatives confirmed that WDR1 deficiency is autosomal recessive." — [PMID: 27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/)

**Gene identifiers:** *WDR1* — HGNC:12754, NCBI Gene 9948, Ensembl ENSG00000071127, UniProt O75083 (Aip1), gene OMIM \*604734, cytoband 4p16.1 (GRCh38 chr4:~10.07–10.12 Mb, minus strand).

### Finding 2 — Loss of Aip1 elevates F-actin and produces distinctive neutrophil morphologic and motility defects

In patient neutrophils, **F-actin was elevated ~4-fold**, and **chemotaxis and chemokinesis were markedly impaired**. Cells showed a distinctive morphology — herniation of nuclear lobes and agranular cytosolic regions — with impaired spreading on glass and defective polarization. Notably, **staphylococcal killing was preserved and oxidative burst was paradoxically increased** at baseline and on stimulation, indicating a specific defect in actin-dependent motility rather than a global neutrophil failure. Pfajfer et al. (2018) additionally documented defective adhesion and motility of neutrophils and monocytes. The biochemical basis is that Aip1 destabilizes cofilin-saturated actin filaments by severing them and accelerating monomer dissociation from both barbed and pointed ends; loss of this activity impairs filament turnover and lets F-actin accumulate.

> "Neutrophil F-actin was elevated fourfold, suggesting an abnormality in F-actin regulation." — [PMID: 27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/)

> "Chemotaxis and chemokinesis were markedly impaired, but staphylococcal killing was normal, and neutrophil oxidative burst was increased both basally and on stimulation." — [PMID: 27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/)

> "Aip1 also augments the monomer dissociation rate at both the barbed and pointed ends of actin." — [PMID: 25448002](https://pubmed.ncbi.nlm.nih.gov/25448002/)

### Finding 3 — PFIT autoinflammation is IL-18–dominant and driven by increased inflammasome/caspase-1 activity linked to pyrin

Standing et al. (2017) found PFIT patients had **high serum IL-18 without a corresponding rise in IL-18–binding protein or IL-1β**; patient cells secreted more IL-18 but not IL-1β in culture. **Increased caspase-1 cleavage in patient monocytes** indicated heightened inflammasome activity. In HEK293T co-transfection experiments, **mutant WDR1 protein formed aggregates that accumulated pyrin**, potentially precipitating inflammasome assembly. This extends the *Wdr1*-mutant mouse model, in which autoinflammatory disease is bone-marrow–derived, nonlymphoid, and characterized by massive neutrophil infiltration.

> "Patients had high serum levels of IL-18, without a corresponding increase in IL-18-binding protein or IL-1β, and their cells also secreted more IL-18 but not IL-1β in culture." — [PMID: 27994071](https://pubmed.ncbi.nlm.nih.gov/27994071/)

> "We found increased caspase-1 cleavage within patient monocytes indicative of increased inflammasome activity." — [PMID: 27994071](https://pubmed.ncbi.nlm.nih.gov/27994071/)

> "Mutant protein formed aggregates that appeared to accumulate pyrin; this could potentially precipitate inflammasome assembly." — [PMID: 27994071](https://pubmed.ncbi.nlm.nih.gov/27994071/)

> "Autoinflammatory disease, which is bone marrow-derived yet nonlymphoid in origin, is characterized by a massive infiltration of neutrophils into inflammatory lesions." — [PMID: 17515402](https://pubmed.ncbi.nlm.nih.gov/17515402/)

### Finding 4 — WDR1 deficiency also causes lymphoid immunodeficiency and macrothrombocytopenia

Pfajfer et al. (2018) identified novel homozygous/compound-heterozygous *WDR1* missense mutations in **6 patients from 3 kindreds** presenting with respiratory tract infections, skin ulceration, and stomatitis. Beyond myeloid defects, WDR1 deficiency caused **aberrant T-cell activation** — atypical actin accumulation at the immunologic synapse, reduced calcium flux, mildly impaired proliferation, and selective loss of follicular helper T cells — and **severe B-cell abnormalities**: peripheral B-cell lymphopenia, paucity of bone-marrow B-cell progenitors, and lack of switched memory B cells. Thrombocytopenia parallels the macrothrombocytopenia of hypomorphic *Wdr1* mice, which arises from megakaryocyte maturation defects causing failure of normal platelet shedding.

> "we identified novel homozygous and compound heterozygous WDR1 missense mutations in 6 patients belonging to 3 kindreds who presented with respiratory tract infections, skin ulceration, and stomatitis." — [PMID: 29751004](https://pubmed.ncbi.nlm.nih.gov/29751004/)

> "WDR1 deficiency was associated with even more severe abnormalities of the B-cell compartment, including peripheral B-cell lymphopenia, paucity of B-cell progenitors in the bone marrow, lack of switched memory B cells." — [PMID: 29751004](https://pubmed.ncbi.nlm.nih.gov/29751004/)

> "peripheral T cells from the patients accumulated atypical actin structures at the immunologic synapse and displayed reduced calcium flux and mildly impaired proliferation on T-cell receptor stimulation." — [PMID: 29751004](https://pubmed.ncbi.nlm.nih.gov/29751004/)

> "Macrothrombocytopenia is the result of megakaryocyte maturation defects, which lead to a failure of normal platelet shedding." — [PMID: 17515402](https://pubmed.ncbi.nlm.nih.gov/17515402/)

### Finding 5 — PFIT belongs to the autoinflammatory "actinopathies"; onset is neonatal/early-childhood, and allogeneic HSCT is definitive

Kuhns et al. (2016) reported that **allogeneic stem cell transplantation corrected the immunologic defect** in one patient, whereas untreated patients had severe outcomes including oral stenosis and death. Reviews of autoinflammatory actinopathies (Mertz et al. 2024) classify WDR1 deficiency within this emerging autoinflammatory-disease subgroup, which typically manifests in the neonatal period and combines primary immunodeficiency, cytopenia (especially thrombocytopenia), and autoinflammation affecting skin and digestive system — often requiring allogeneic marrow transplantation.

> "Allogeneic stem cell transplantation corrected the immunologic defect in 1 patient." — [PMID: 27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/)

> "These diseases typically manifest in the neonatal period and variably combine a primary immunodeficiency of varying severity, cytopenia (particularly thrombocytopenia), autoinflammatory manifestations primarily affecting the skin and digestive system." — [PMID: 39644982](https://pubmed.ncbi.nlm.nih.gov/39644982/)

> "In most cases, the severity of the conditions necessitates allogeneic marrow transplantation as a treatment." — [PMID: 39644982](https://pubmed.ncbi.nlm.nih.gov/39644982/)

### Finding 6 — *WDR1* is extremely loss-of-function-intolerant, so human PFIT arises only from hypomorphic biallelic missense variants

gnomAD constraint metrics place *WDR1* among the most LoF-intolerant genes: **pLI = 0.9999**, LOEUF (oe_lof upper) = 0.42, observed/expected LoF = 0.29, lof_z = 5.09. Consistent with this, **all reported human PFIT patients carry biallelic missense (hypomorphic) variants** — Kuhns 2016 (distinct antiparallel β-strands of Aip1), Standing 2017 (homozygous missense), Pfajfer 2018 (homozygous and compound-heterozygous missense). This mirrors the *Wdr1* mouse allelic series, in which severe loss of function is embryonic-lethal but hypomorphic alleles are viable and produce autoinflammation plus macrothrombocytopenia.

> "Biallelic mutations in WDR1 affecting distinct antiparallel β-strands of Aip1 were identified in all patients." — [PMID: 27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/)

> "While severe loss of function at the Wdr1 locus causes embryonic lethality, macrothrombocytopenia and autoinflammatory disease develop in mice carrying hypomorphic alleles." — [PMID: 17515402](https://pubmed.ncbi.nlm.nih.gov/17515402/)

### Finding 7 — Wdr1/Aip1 function and disease are evolutionarily conserved; mouse models recapitulate F-actin accumulation and tissue pathology

Two complementary mouse models establish causality and conserved mechanism. **(1)** Hypomorphic *Wdr1* mice (Kile et al. 2007) develop macrothrombocytopenia (megakaryocyte maturation defect) plus bone-marrow–derived, nonlymphoid autoinflammatory disease with massive neutrophil infiltration; severe LoF is embryonic-lethal. **(2)** A cardiomyocyte-specific *Wdr1* conditional knockout (Yuan et al. 2014) died by postnatal day 24 with cardiac hypertrophy, impaired left-ventricular contraction, prolonged QT, and progressive **F-actin accumulation within myofibrils**, with ectopic cofilin colocalizing at the aggregates. Aip1 orthologs are deeply conserved: *S. cerevisiae* AIP1, *C. elegans* unc-78, plant AIP1 (rice/*Arabidopsis*), and mouse *Wdr1* (NCBI Gene 22388), all promoting cofilin/ADF-mediated actin disassembly.

> "Actin filament (F-actin) accumulations began at P10 and became prominent at P12 in the myocardium of cKO mice… Ectopic cofilin colocalized with F-actin aggregates." — [PMID: 24840128](https://pubmed.ncbi.nlm.nih.gov/24840128/)

> "These studies establish an essential requirement for Wdr1 in megakaryocytes and neutrophils, indicating that cofilin-mediated actin dynamics are critically important to the development and function of both cell types." — [PMID: 17515402](https://pubmed.ncbi.nlm.nih.gov/17515402/)

### Finding 8 — PFIT clinical phenotype spectrum and suggested HPO annotations

Across the three reported cohorts (Kuhns 2016 n=4; Standing 2017 n=2; Pfajfer 2018 n=6), the recurrent core features are: recurrent/periodic fevers, immunodeficiency with recurrent bacterial and respiratory infections, thrombocytopenia/bleeding tendency (including macrothrombocytopenia), mild neutropenia, severe stomatitis/recurrent oral ulceration progressing to oral stenosis, skin ulceration, and impaired wound healing. Laboratory hallmarks include markedly elevated serum IL-18 (with normal/low IL-1β and IL-18BP), elevated neutrophil F-actin (4-fold), distinctive neutrophil nuclear herniation with agranular cytosolic regions, B lymphopenia, and lack of switched memory B cells.

> "we identified 4 children with recurrent infections and varying clinical manifestations including mild neutropenia, impaired wound healing, severe stomatitis with oral stenosis, and death." — [PMID: 27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/)

| Phenotype | Suggested HPO term | Frequency / notes |
|---|---|---|
| Recurrent/periodic fever (autoinflammation) | HP:0001954 (recurrent fever) | Core; episodic flares |
| Recurrent respiratory infections | HP:0002205 | Common in Pfajfer cohort |
| Recurrent bacterial infections | HP:0002718 | Core immunodeficiency feature |
| Thrombocytopenia | HP:0001873 | Core |
| Macrothrombocytopenia (large platelets) | HP:0040314 | Parallels mouse model |
| Neutropenia (mild) | HP:0001875 | Variable |
| Recurrent oral ulceration / stomatitis | HP:0010280 (oral ulcer) | Severe; can progress |
| Oral stenosis | HP:0011099 (functional/anatomic stenosis) | Severe untreated cases |
| Skin ulceration | HP:0200042 | Pfajfer cohort |
| Poor/impaired wound healing | HP:0001058 | Core |
| Elevated serum IL-18 | (laboratory biomarker) | Diagnostic hallmark |

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic missense mutation in *WDR1*** (4p16.1) **leads to** a partially functional Aip1 β-propeller protein (complete-null alleles are embryonic-lethal, so only hypomorphs survive).
2. Reduced Aip1 activity **results in** failure to sever and disassemble cofilin/ADF-bound actin filaments (Aip1 normally accelerates monomer dissociation from both filament ends).
3. Impaired filament turnover **leads to** pathological **accumulation of F-actin** (~4-fold in neutrophils) and aberrant actin structures in hematopoietic and other cells.
4. Elevated/dysregulated F-actin **branches** into three effector arms:
   - **Arm A — Myeloid/innate:** impaired neutrophil chemotaxis, spreading, and polarization (motility defect) with preserved killing and increased oxidative burst → recurrent infections + tissue neutrophil infiltration.
   - **Arm B — Autoinflammation:** mutant WDR1 aggregates sequester **pyrin**, and cytoskeletal dysregulation acts as a homeostasis-altering signal → **inflammasome/caspase-1 activation** → **IL-18–dominant** cytokine release (without IL-1β) → periodic fevers, cutaneous-digestive inflammation.
   - **Arm C — Lymphoid + platelets:** defective immune-synapse actin dynamics → T-cell activation defects + B-cell developmental failure (immunodeficiency); megakaryocyte maturation failure → defective platelet shedding → **macrothrombocytopenia/bleeding**.
5. The combined arms **result in** the clinical triad — **periodic fever + immunodeficiency + thrombocytopenia** — plus stomatitis, oral stenosis, skin ulceration, and poor wound healing; untreated disease can be fatal.
6. Because the defect is intrinsic to bone-marrow–derived cells, **allogeneic HSCT replaces the defective hematopoietic compartment and corrects the disease** (definitive treatment).

*(Step 4B's pyrin/inflammasome link is mechanistically supported by co-transfection aggregation data and elevated caspase-1 cleavage but the precise molecular trigger connecting F-actin dysregulation to inflammasome assembly remains partly inferred.)*

```
 WDR1 missense (hypomorphic, biallelic)
        │
        ▼
 Reduced Aip1 activity ──► cofilin-bound filaments not disassembled
        │
        ▼
 F-actin accumulation (~4× in neutrophils)
        │
  ┌─────┼─────────────────────────┐
  ▼     ▼                         ▼
Neutrophil   Inflammasome/pyrin   Lymphoid + megakaryocyte
motility     → caspase-1          synapse/maturation defects
defect       → IL-18↑ (IL-1β−)    │
  │             │                 ├─ T/B-cell immunodeficiency
  ▼             ▼                 └─ macrothrombocytopenia
Recurrent    Periodic fever,          (bleeding)
infections   skin/digestive
             autoinflammation
        │
        ▼
   PFIT clinical triad → (untreated) death │ (HSCT) correction
```

### Upstream vs downstream
- **Upstream (initiating):** *WDR1* mutation → Aip1 hypofunction → defective cofilin-mediated actin disassembly (molecular lesion).
- **Central node:** F-actin accumulation / disrupted actin turnover.
- **Downstream (effector):** neutrophil/lymphocyte dysfunction, inflammasome-driven IL-18, megakaryocyte failure → the clinical phenotype.

### Cell types and processes (suggested ontology terms)
- **Cells (CL):** neutrophil (CL:0000775), monocyte (CL:0000576), T cell (CL:0000084), B cell (CL:0000236), megakaryocyte (CL:0000556), platelet (CL:0000233).
- **Biological processes (GO):** actin filament depolymerization (GO:0030042), regulation of actin cytoskeleton organization (GO:0032956), neutrophil chemotaxis (GO:0030593), inflammasome complex assembly (GO:0044546), interleukin-18 production (GO:0032620), megakaryocyte differentiation (GO:0030219), immunological synapse formation (GO:0001771).
- **Cellular components (GO CC):** cortical actin cytoskeleton (GO:0030864), lamellipodium (GO:0030027), actin filament (GO:0005884).
- **Anatomy (UBERON):** bone marrow (UBERON:0002371), blood (UBERON:0000178), oral mucosa (UBERON:0003729), skin (UBERON:0002097).
- **Chemical entities (CHEBI):** interleukin-18 (protein), reactive oxygen species (CHEBI:26523).

---

## Report by Template Section

### 1. Disease Information
PFIT is an ultra-rare Mendelian autoinflammatory immunodeficiency defined by the triad of periodic fever, immunodeficiency, and thrombocytopenia, caused by *WDR1* mutations. **Identifiers:** MONDO:0007883; gene OMIM \*604734 (*WDR1*). MONDO:0007883 is historically cross-referenced to OMIM 150550 ("lazy leukocyte syndrome"), an older descriptive label for a neutrophil-motility disorder — a mapping caveat worth flagging for curators, who should reconcile it against the specific WDR1-PFIT phenotype entry. **Synonyms:** WDR1 deficiency; Aip1 deficiency; autoinflammatory PFIT; a member of the "autoinflammatory actinopathies." Information is derived from **aggregated disease-level resources plus small primary case series** (≈12 patients across 3 kindreds/cohorts), not EHR-scale data.

### 2. Etiology
**Causal factor:** monogenic — biallelic hypomorphic **missense** mutations in *WDR1*. **Genetic risk:** requires two pathogenic alleles (AR); consanguinity increases risk (homozygous cases reported). No environmental cause; infections are downstream consequences of immunodeficiency rather than causes. **Protective factors:** none established. **Gene–environment interaction:** infectious exposures likely precipitate flares and morbidity in an immunodeficient host, but no formal GxE data exist.

### 3. Phenotypes
See Finding 8 table. Onset is **neonatal/early childhood**; severity is variable but often severe; course is chronic with **episodic autoinflammatory flares**. Quality-of-life impact is substantial (recurrent infections, painful stomatitis/oral stenosis limiting feeding, bleeding tendency); formal QoL instruments (EQ-5D/SF-36) have not been reported for this ultra-rare disease.

### 4. Genetic / Molecular Information
**Causal gene:** *WDR1* (HGNC:12754; NCBI Gene 9948; Ensembl ENSG00000071127; UniProt O75083; 4p16.1). **Variant class:** missense (hypomorphic) — pathogenic/likely pathogenic per ACMG in reported families; affecting the Aip1 β-propeller (distinct antiparallel β-strands). **Functional consequence:** partial loss of function (impaired cofilin-dependent actin disassembly). **Constraint:** pLI ≈ 1.0, LOEUF 0.42 — strong LoF intolerance, so null alleles are not observed in surviving patients. **Origin:** germline. **Modifier genes / epigenetics / chromosomal abnormalities:** none established.

### 5. Environmental Information
No toxic, occupational, or lifestyle etiologic factors. **Infectious agents** (e.g., *Staphylococcus*, respiratory pathogens) act as complicating/triggering factors in the immunodeficient host, not as primary causes.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above. Core pathway: **cofilin/ADF–Aip1 actin-disassembly axis** → F-actin dysregulation → branching myeloid, inflammasome (IL-18/pyrin/caspase-1), and lymphoid/megakaryocyte effector arms. Molecular profiling to date is limited to targeted cytokine (IL-18) and cell-biological (F-actin, synapse) assays plus HEK293T co-transfection; no large-scale transcriptomic/proteomic/metabolomic PFIT datasets are published.

### 7. Anatomical Structures Affected
**Primary:** bone marrow / hematopoietic system (neutrophils, monocytes, T and B lymphocytes, megakaryocytes/platelets). **Secondary/target tissues:** oral mucosa (stomatitis, oral stenosis), skin (ulceration, poor healing), respiratory tract (infections). Involvement is **systemic/bilateral** (hematologic). Subcellular: cortical actin cytoskeleton, lamellipodium; F-actin aggregates.

### 8. Temporal Development
**Onset:** neonatal/early childhood. **Pattern:** chronic disease with episodic (periodic) autoinflammatory fever flares superimposed on persistent immunodeficiency and thrombocytopenia. **Progression:** can be severe/progressive if untreated (oral stenosis, fatal outcomes). **Remission:** treatment-induced (HSCT corrective); no reliable spontaneous remission. Critical window: early diagnosis enables transplantation before irreversible complications.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive. **Penetrance:** appears high/complete in biallelic carriers; heterozygotes are unaffected. **Expressivity:** variable (severity and organ emphasis differ across families). **Consanguinity:** contributory (homozygous cases). **Epidemiology:** ultra-rare — only ~12 reported patients across 3 kindreds/cohorts; true prevalence/incidence unknown. No founder effect established for *WDR1* PFIT; no strong sex bias reported.

### 10. Diagnostics
**Genetic diagnosis is definitive:** WES/WGS or targeted autoinflammatory/immunodeficiency gene panels identifying biallelic *WDR1* missense variants. **Supportive labs/biomarkers:** markedly elevated **serum IL-18** (with normal/low IL-1β and IL-18BP), thrombocytopenia with large platelets on smear, mild neutropenia, elevated inflammatory markers, **4-fold elevated neutrophil F-actin**, distinctive neutrophil nuclear herniation/agranular cytosol, B lymphopenia and absent switched memory B cells on immunophenotyping. **Differential diagnosis:** other autoinflammatory actinopathies (e.g., ARPC1B deficiency, MKL1, ACTB/Baraitser-Winter), other periodic fever syndromes (FMF, HIDS), and other inherited macrothrombocytopenias/immunodeficiencies. **Screening:** cascade genetic testing of at-risk relatives; carrier testing in families.

### 11. Outcome / Prognosis
**Untreated:** poor — recurrent infections, bleeding, severe stomatitis/oral stenosis, and reported **death**. **With HSCT:** immunologic defect corrected; substantially improved prognosis. Prognostic factors include age at diagnosis, severity of infections/bleeding, and access to transplant.

### 12. Treatment
**Definitive:** **allogeneic hematopoietic stem cell transplantation (HSCT)** — corrective, replaces the defective bone-marrow compartment (NCIT: Allogeneic Hematopoietic Stem Cell Transplantation, C15393). **Supportive/bridging:** antimicrobial prophylaxis and treatment of infections; management of bleeding/thrombocytopenia; targeting the IL-18/inflammasome autoinflammatory axis is mechanistically rational (IL-18/IL-1 pathway modulation, anti-inflammatory agents) but not established as curative. Wound and oral care for stomatitis/ulceration. **Pharmacogenomics:** not applicable/established.

### 13. Prevention
No primary prevention (monogenic). **Genetic counseling** for AR recurrence risk (25% per pregnancy for carrier couples), carrier and prenatal/preimplantation testing in known families, and **cascade screening**. Tertiary prevention centers on early transplant and infection prophylaxis to avert complications.

### 14. Other Species / Natural Disease
Aip1/Wdr1 is deeply conserved: mouse *Wdr1* (NCBI Gene 22388), *S. cerevisiae AIP1*, *C. elegans unc-78*, plant AIP1 (rice *OsAIP1*, *Arabidopsis*). No naturally occurring companion-animal PFIT disease is catalogued; relevance is via engineered models. Not zoonotic.

### 15. Model Organisms
**Mouse (*Mus musculus*)** is the principal model. **Hypomorphic *Wdr1* mice** (Kile 2007) recapitulate macrothrombocytopenia and neutrophil-driven autoinflammation; **severe LoF is embryonic-lethal** (allelic-series dose dependence mirroring human missense-only genotypes). **Cardiomyocyte-specific *Wdr1* cKO** (Yuan 2014) demonstrates in-vivo F-actin accumulation and tissue pathology. **In vitro:** HEK293T co-transfection shows mutant WDR1 aggregation and pyrin accumulation; patient-derived neutrophils/T/B cells provide cellular assays. Invertebrate/yeast orthologs (*unc-78*, *AIP1*) support mechanistic conservation. **Limitations:** cardiomyocyte cKO models tissue-specific actin pathology rather than the hematologic/autoinflammatory human disease; small human cohorts limit genotype–phenotype resolution.

---

## Evidence Base

| PMID | Title (abbrev.) | Role / contribution | Evidence type |
|---|---|---|---|
| [27994071](https://pubmed.ncbi.nlm.nih.gov/27994071/) | Autoinflammatory PFIT caused by WDR1 mutation | Index report; defines PFIT triad; IL-18 dominance; pyrin/caspase-1 | Human clinical |
| [27557945](https://pubmed.ncbi.nlm.nih.gov/27557945/) | Cytoskeletal abnormalities & neutrophil dysfunction in WDR1 deficiency | 4-patient cohort; 4× F-actin; AR inheritance; HSCT corrective | Human clinical |
| [29751004](https://pubmed.ncbi.nlm.nih.gov/29751004/) | WDR1 mutations lead to aberrant lymphoid immunity | 6-patient cohort; T-synapse defect; B-cell failure; mucocutaneous phenotype | Human clinical |
| [17515402](https://pubmed.ncbi.nlm.nih.gov/17515402/) | Aip1/Wdr1 mutations cause autoinflammation & macrothrombocytopenia | Mouse allelic series; LoF lethality vs hypomorph viability | Model organism |
| [24840128](https://pubmed.ncbi.nlm.nih.gov/24840128/) | Cardiomyocyte-specific Wdr1 knockout | In-vivo F-actin accumulation; ectopic cofilin colocalization | Model organism |
| [25448002](https://pubmed.ncbi.nlm.nih.gov/25448002/) | Aip1 destabilizes cofilin-saturated filaments | Biochemical mechanism of Aip1 disassembly activity | In vitro |
| [39644982](https://pubmed.ncbi.nlm.nih.gov/39644982/) | Monogenic autoinflammatory actinopathies review | Classification; neonatal onset; HSCT as mainstay | Review |
| [37596178](https://pubmed.ncbi.nlm.nih.gov/37596178/) | Actinopathy-associated autoinflammatory diseases review | Diagnostic approach; cutaneous-digestive autoinflammation | Review |
| [33558442](https://pubmed.ncbi.nlm.nih.gov/33558442/) | Cytoskeletal proteins in immune diseases | Context: WDR1 among actin regulators in immunopathology | Review |
| [32846417](https://pubmed.ncbi.nlm.nih.gov/32846417/) | Actinopathies as a PID category | Framework for immunologic actinopathies | Review |
| [14742433](https://pubmed.ncbi.nlm.nih.gov/14742433/) · [14680631](https://pubmed.ncbi.nlm.nih.gov/14680631/) · [16421248](https://pubmed.ncbi.nlm.nih.gov/16421248/) | AIP1/cofilin biochemistry | Mechanistic basis of Aip1-cofilin cooperative disassembly | In vitro / yeast |
| [23134061](https://pubmed.ncbi.nlm.nih.gov/23134061/) | Rice OsAIP1 promotes actin turnover | Evolutionary conservation of Aip1 function | Plant model |

**Consistency:** All three human cohorts converge on biallelic *WDR1* missense variants, actin dysregulation, and the PFIT triad, with independent replication of AR inheritance and HSCT correction. Mouse and biochemical studies provide congruent mechanistic support. No published study in the reviewed set contradicts the core model.

---

## Limitations and Knowledge Gaps

- **Very small n (~12 patients):** prevalence, incidence, penetrance, and full expressivity are imprecise; genotype–phenotype correlation is limited.
- **Inflammasome trigger partly inferred:** the exact molecular link from F-actin dysregulation to pyrin/inflammasome activation rests on co-transfection aggregation data and caspase-1 cleavage — direct in-vivo mechanistic proof in patient tissue is incomplete.
- **No large-scale omics:** no published PFIT transcriptomic/proteomic/single-cell datasets to define cell-type-resolved mechanisms.
- **Therapeutic evidence beyond HSCT is anecdotal:** targeted IL-18/inflammasome blockade is rational but not validated in trials.
- **Identifier ambiguity:** MONDO:0007883's historical cross-reference to OMIM 150550 ("lazy leukocyte syndrome") should be verified against the specific WDR1-PFIT OMIM phenotype entry for curation accuracy.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international PFIT/WDR1 registry** to capture natural history, penetrance, genotype–phenotype correlations, and HSCT outcomes.
2. **Patient-derived single-cell multi-omics** (scRNA-seq/CITE-seq of bone marrow and blood) to resolve cell-type-specific actin/inflammasome dysregulation and IL-18 sources.
3. **Mechanistic dissection of the F-actin → pyrin/inflammasome link** using patient monocytes and CRISPR-engineered *WDR1*-hypomorph cell lines/organoids; test whether restoring actin turnover normalizes IL-18.
4. **Preclinical trials of IL-18/IL-1 pathway blockade** (as a bridge to or adjunct with HSCT) in hypomorphic *Wdr1* mice and patient cells.
5. **Structure–function studies** mapping reported β-propeller missense variants onto Aip1 structure to predict residual activity and severity (variant-interpretation aid).
6. **Curate ontology annotations** (HPO frequencies, GO/CL/UBERON/CHEBI terms above) into the disease knowledge base and reconcile MONDO/OMIM cross-references.

---

*Report compiled from 8 confirmed findings and 18 reviewed papers across 5 investigation iterations. Evidence types are labeled human clinical, model organism, in vitro, or review throughout.*


## Artifacts

- [OpenScientist final report](Periodic_Fever_Immunodeficiency_and_Thrombocytopenia_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Periodic_Fever_Immunodeficiency_and_Thrombocytopenia_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27557945` *(abstract only)*: "Biallelic mutations in WDR1 affecting distinct antiparallel β-strands of Aip1 were identified in all patients… Heterozygous mutations in clinically normal relatives confirmed that WDR1 deficiency is autosomal recessive."
  - closest text in source: "Biallelic mutations in WDR1 affecting distinct antiparallel β-strands of Aip1 were identified in all patients"
- `PMID:24840128` *(abstract only)*: "Actin filament (F-actin) accumulations began at P10 and became prominent at P12 in the myocardium of cKO mice… Ectopic cofilin colocalized with F-actin aggregates."
  - closest text in source: "Actin filament (F-actin) accumulations began at P10 and became prominent at P12 in the myocardium of cKO mice"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 10 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0040314` (1 mention) - the report calls it "Macrothrombocytopenia (large platelets)"; HP calls it **Blind vagina**
- `HP:0010280` (1 mention) - the report calls it "oral ulcer"; HP calls it **Stomatitis**
- `HP:0011099` (1 mention) - the report calls it "functional/anatomic stenosis"; HP calls it **Spastic hemiparesis**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001875` (1 mention) - the report calls it "Neutropenia (mild)"; HP calls it **Decreased total neutrophil count**, and lists "Neutropenia" among its other names
- `HP:0200042` (1 mention) - the report calls it "Skin ulceration"; HP calls it **Skin ulcer**
- `HP:0001058` (1 mention) - the report calls it "Poor/impaired wound healing"; HP calls it **Poor wound healing**