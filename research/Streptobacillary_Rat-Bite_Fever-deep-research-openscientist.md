---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T09:43:42.305591'
end_time: '2026-09-25T10:01:57.226151'
duration_seconds: 1094.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Streptobacillary Rat-Bite Fever
  mondo_id: MONDO:0020533
  category: Infectious
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 23
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 24
  quotes_valid: 23
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42732473
  relevance_assessed: 23
  on_topic: 19
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 33
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 14
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0020533
    reported_labels:
    - Mondo
    ontology_label: streptobacillary rat-bite fever
  - term_id: DOID:0050144
    reported_labels:
    - Disease Ontology
    ontology_label: Kartagener syndrome
  - term_id: UBERON:0001456
    reported_labels:
    - joint / articular structures
    ontology_label: face
  - term_id: NCIT:C1145
    reported_labels:
    - Penicillin
    ontology_label: Lignan
  - term_id: NCIT:C299
    reported_labels:
    - Amoxicillin
    ontology_label: Beclomethasone Dipropionate
  - term_id: NCIT:C560
    reported_labels:
    - Ceftriaxone
    ontology_label: Hydroxyurea
  - term_id: NCIT:C561
    reported_labels:
    - Doxycycline
    ontology_label: Ibuprofen
  - term_id: NCIT:C1728
    reported_labels:
    - Ampicillin
    ontology_label: Celecoxib
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Streptobacillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Streptobacillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Streptobacillary Rat-Bite Fever
- **MONDO ID:** MONDO:0020533 (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Streptobacillary Rat-Bite Fever** covering all of the
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

# Streptobacillary Rat-Bite Fever (MONDO:0020533): A Comprehensive Disease Characterization

## Summary

**Streptobacillary rat-bite fever (RBF) is a rare, acquired zoonotic bacterial infection caused by the fastidious Gram-negative bacillus *Streptobacillus moniliformis* (with the recently split *Streptobacillus notomytis* recognized as an additional human pathogen).** It is transmitted by rodent bites and scratches, by handling rodents or their excreta, or by ingesting rodent-contaminated food or water — the ingestion form is historically termed **Haverhill fever** (erythema arthriticum epidemicum). After a typical incubation of 3–10 days, the disease produces an acute systemic illness with the classic triad of **fever, an acral (hands/feet) rash, and migratory polyarthritis**. Because it is an infectious rather than a genetic disease, all host-genetic, inheritance, penetrance, and gene-therapy dimensions of the research template are **Not Applicable**.

The central clinical lesson from this investigation is that **outcome hinges almost entirely on time-to-diagnosis, not on host factors.** RBF is exquisitely susceptible to penicillin and is reliably curable when recognized early, yet its nonspecific initial presentation and a difficult-to-culture organism together produce a real risk of diagnostic delay. Untreated or late-treated disease can progress to septic arthritis, osteomyelitis, infective endocarditis, and fatal multi-organ sepsis, with reported untreated case-fatality of **10–13%**. Diagnosis rests on exposure history plus recovery/detection of the organism, aided increasingly by molecular methods (16S rRNA PCR, triplex/multiplex qPCR, metagenomic next-generation sequencing) that circumvent the organism's fastidious growth and inhibition by the anticoagulant sodium polyanethole sulfonate (SPS) in blood-culture bottles.

This report consolidates 15 confirmed findings across 28 reviewed papers. It covers the disease's identifiers and synonyms, etiology and transmission, phenotypes, the (non-genetic) molecular/host picture, environmental and occupational determinants, a stepwise pathophysiological causal chain, anatomical involvement, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and its comparative/veterinary biology. Prevention is behavioral and occupational — no human vaccine exists — and centers on avoiding rodent exposure, wound hygiene, and consideration of post-exposure antibiotic prophylaxis.

---

## 1. Disease Information

**Overview.** Streptobacillary rat-bite fever is a systemic febrile zoonosis caused by *Streptobacillus moniliformis*, "a systemic illness classically characterized by fever, rigors, and polyarthralgias" ([PMID: 17223620](https://pubmed.ncbi.nlm.nih.gov/17223620/)). It is one of two classic forms of rat-bite fever; the other, more common in Asia, is caused by *Spirillum minus* (spirillary RBF / sodoku). This report concerns the streptobacillary form.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Mondo | MONDO:0020533 |
| ICD-10 | A25.1 (Streptobacillosis) |
| ICD-11 | 1B93.0 |
| MeSH | D011906 (Rat-Bite Fever) |
| Disease Ontology | DOID:0050144 |
| Causative organism (NCBI Taxonomy) | txid34105 (*S. moniliformis*) |
| OMIM / Orphanet genetic entry | None (not a Mendelian disease) |

**Synonyms and alternative names.** Streptobacillary fever; streptobacillosis; **Haverhill fever** and **erythema arthriticum epidemicum** (the food/water-borne, ingestion-acquired form); epidemic arthritic erythema. "Rat-bite fever" is the umbrella clinical term shared with the spirillary form.

**Source of information.** The knowledge base entry is derived from **aggregated disease-level resources** — case reports, case series, and narrative reviews — rather than large structured EHR cohorts. The disease is rare and, in most jurisdictions, **not nationally reportable**, so "it may be more prevalent than currently recognized" ([PMID: 42623631](https://pubmed.ncbi.nlm.nih.gov/42623631/)).

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused by infection with *Streptobacillus moniliformis*, a fastidious, pleomorphic, Gram-negative bacillus that is a **commensal of the rat naso-/oropharynx**. A second species, *S. notomytis*, is now recognized as "a distinct species from *Streptobacillus moniliformis* — the primary causative agent of rat-bite fever" and "has been implicated in rare human infections" ([PMID: 40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/)).

**Risk factors (environmental / behavioral).**
- **Rodent exposure** — bites, scratches, handling, or contact with rodent excreta. "Rat-bite fever follows exposure to contaminated bodily fluids of infected rodents" ([PMID: 34323361](https://pubmed.ncbi.nlm.nih.gov/34323361/)).
- **Occupational exposure** — pet-shop employees, laboratory-animal workers, and others in contact with rodents. A fatal case occurred in a 24-year-old pet-shop employee who "contracted the disease through a minor superficial finger wound on a contaminated rat cage" ([PMID: 15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/)).
- **Age and social factors** — young children and people of low socioeconomic status are overrepresented; RBF has "potentially lethal course in a vulnerable population (children and low socioeconomic class)" ([PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/)).
- **Pet-rodent ownership** — an increasing driver as pet rats become more common.

**Genetic risk / protective factors.** **Not applicable.** No causal genes, susceptibility loci, modifier genes, protective alleles, or gene–environment interactions are described for this acquired infection.

---

## 3. Phenotypes

The hallmark is the **clinical triad**: physicians should consider RBF "when fever, rash, and exposure to rats are part of the patient's history" ([PMID: 11724672](https://pubmed.ncbi.nlm.nih.gov/11724672/)); it presents as a "clinical triad of symptoms, fever, rash and arthritis" ([PMID: 39267964](https://pubmed.ncbi.nlm.nih.gov/39267964/)).

| Phenotype | Type | Characteristics | Suggested HPO term |
|---|---|---|---|
| Fever / rigors | Symptom (constitutional) | Abrupt onset, often high; near-universal | HP:0001945 (Fever) |
| Rash (maculopapular, petechial, pustular, purpuric; acral) | Physical manifestation | Characteristically on hands and feet, including palms/soles; hemorrhagic pustules/purpuric lesions | HP:0000988 (Skin rash) |
| Migratory polyarthritis / polyarthralgia | Clinical sign | Asymmetric, migratory; can progress to frank septic arthritis | HP:0005764 (Migratory arthritis) / HP:0002829 (Arthralgia) |
| Myalgia | Symptom | Common in acute phase | HP:0003326 (Myalgia) |
| Headache | Symptom | Frequent | HP:0002315 (Headache) |
| Leukocytosis / neutrophilia | Laboratory abnormality | Variable; WBC may be normal | HP:0001974 (Leukocytosis) |
| Thrombocytopenia | Laboratory abnormality | Reported in severe/atypical cases | HP:0001873 (Thrombocytopenia) |
| Elevated CRP | Laboratory abnormality | Nonspecific inflammatory marker | HP:0011227 (Elevated C-reactive protein) |

RBF presents with "unspecific symptoms, including fever, arthralgia, and polymorphous skin lesions" ([PMID: 34323361](https://pubmed.ncbi.nlm.nih.gov/34323361/)). **Onset** is adult or pediatric (any age), **severity** ranges from mild self-limited illness to fatal sepsis (variable), and **progression** is acute and may be episodic/relapsing if untreated. **Quality-of-life impact** during acute illness is substantial (fever, disabling polyarthritis) but, with prompt treatment, is typically fully reversible; formal EQ-5D/SF-36 data are not available for this rare disease.

---

## 4. Genetic / Molecular Information

**Not applicable.** Streptobacillary RBF is an acquired bacterial infection with **no human causal genes, no inheritance pattern, no pathogenic germline or somatic variants, no disease-defining epigenetic mechanism, and no chromosomal abnormality.** Sections on causal genes, pathogenic variants (classification, allele frequency, somatic vs germline), modifier genes, and host epigenetics are Not Applicable. The relevant "molecular" entity is the pathogen genome itself (NCBI:txid34105), not a host locus. The clinical characterization emphasizes an acute systemic **infectious** course rather than a genetic disease ([PMID: 17223620](https://pubmed.ncbi.nlm.nih.gov/17223620/)).

---

## 5. Environmental Information

- **Infectious agents.** *Streptobacillus moniliformis* (primary) and *S. notomytis* ([PMID: 40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/)). *Spirillum minus* causes the separate spirillary form.
- **Environmental / occupational factors.** Contaminated rodent cages, bedding, feces, and urine; the disease can be acquired occupationally without a bite via a contaminated cage ([PMID: 15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/)).
- **Transmission routes.** (1) Rodent bite or scratch; (2) direct handling / contact with excreta — "Rat-bite fever follows exposure to contaminated bodily fluids of infected rodents" ([PMID: 34323361](https://pubmed.ncbi.nlm.nih.gov/34323361/)); (3) ingestion of contaminated food/water = **Haverhill fever**. Reviews confirm cases "result from rodent bites or exposure to contaminated food or water" ([PMID: 42732473](https://pubmed.ncbi.nlm.nih.gov/42732473/)).
- **Lifestyle factors.** Keeping pet rodents; occupations with rodent contact.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Rodent reservoir colonization** — *S. moniliformis* resides as a commensal of the rat naso-/oropharynx → the rat becomes an asymptomatic carrier and source.
2. **Inoculation** — a bite, scratch, mucosal/skin contact with excreta, or ingestion of contaminated food/water → introduces bacteria into host tissue (or gut, for Haverhill fever).
3. **Local establishment and lymphatic spread** — bacteria seed regional tissue → drain to regional lymph nodes (sinusoidal mononuclear infiltrates observed at autopsy).
4. **Hematogenous dissemination (bacteremia)** — organisms enter the bloodstream → systemic spread and constitutional symptoms (fever, rigors, myalgia). *Documented:* autopsy shows "sinusoidal mononuclear cell infiltrates in regional lymph nodes and the liver" ([PMID: 2718962](https://pubmed.ncbi.nlm.nih.gov/2718962/)).
5. **Branch A — direct septic seeding** → the bacteremia deposits organisms in joints, cardiac valves, and bone → **septic arthritis, infective endocarditis, osteomyelitis** ([PMID: 40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/), [PMID: 15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/)).
6. **Branch B — immune-mediated injury** → bacteremia/antigenemia triggers host immune responses → **leukocytoclastic (small-vessel) vasculitis and reactive arthritis**, with induced ANCA and anti-endothelial antibodies. *Documented:* "general weakness, intermittent fever, leukocytoclastic vasculitis, and arthritis are reported," and this was "the first reported case of ANCA positivity associated with RBF" ([PMID: 37450033](https://pubmed.ncbi.nlm.nih.gov/37450033/)).
7. **Convergence — tissue damage** → both branches produce mononuclear/neutrophilic infiltration and fibrinous exudate → the acral rash, migratory polyarthritis, and, in severe disease, valvular destruction and multi-organ failure.
8. **Terminal outcome (if untreated)** → progressive sepsis, endocarditis, and multi-organ failure → death in ~10–13% of untreated cases.

```
Rat oropharyngeal commensal
        │ inoculation (bite/scratch/contact/ingestion)
        ▼
   Local tissue seeding ── regional lymph nodes
        │
        ▼
   BACTEREMIA (fever, rigors, myalgia)
        │
   ┌────┴──────────────────────────┐
   ▼                               ▼
Branch A: septic seeding       Branch B: immune-mediated
(joints, valves, bone)         (LCV vasculitis, reactive
= septic arthritis,            arthritis, ANCA/anti-endothelial Ab)
endocarditis, osteomyelitis
   └───────────────┬───────────────┘
                   ▼
        Tissue injury: rash, polyarthritis,
        valvular destruction, multi-organ failure
                   ▼
        Death (~10–13% untreated)
```

**Cellular processes and immune involvement.** Inflammation dominates, with mononuclear and neutrophilic infiltration, fibrinous endocarditis, mononuclear meningitis, hepatosplenomegaly, lymphadenopathy, and erythrophagocytosis on autopsy ([PMID: 2718962](https://pubmed.ncbi.nlm.nih.gov/2718962/)). The immune-mediated branch can generate autoantibodies that mimic ANCA-associated vasculitis ([PMID: 37450033](https://pubmed.ncbi.nlm.nih.gov/37450033/)).

**Suggested ontology terms.** GO:0006954 (inflammatory response); GO:0006935 (chemotaxis); GO:0002250 (adaptive immune response); GO:0006909 (phagocytosis, for erythrophagocytosis). Cell types: CL:0000775 (neutrophil), CL:0000235 (macrophage), CL:0000738 (leukocyte), CL:0000115 (endothelial cell, vasculitis target).

**Molecular pathways / omics.** No host signaling-pathway (Wnt/MAPK/mTOR/PI3K-AKT), transcriptomic, proteomic, metabolomic, or lipidomic disease signature is defined — as expected for an acute bacterial infection rather than a chronic host-driven disease. Molecular work centers on **pathogen detection** (16S rRNA, qPCR, mNGS), not host profiling.

---

## 7. Anatomical Structures Affected

**Organ level (primary).** Skin (rash), joints (arthritis), and blood (bacteremia). **Secondary/complication organs.** Heart valves (endocarditis; UBERON:0002134 tricuspid, UBERON:0002137 aortic, UBERON:0002135 mitral), bone (osteomyelitis; UBERON:0001474 bone tissue), meninges (UBERON:0002360), lungs (interstitial pneumonia), liver and spleen (hepatosplenomegaly), and kidneys (acute renal failure in severe sepsis).

**Body systems.** Integumentary, musculoskeletal, cardiovascular, hematologic/lymphatic, and — in disseminated disease — respiratory, hepatobiliary, renal, and central nervous systems.

**Localization / lateralization.** The rash is characteristically **acral and often bilateral** (hands and feet, including palms and soles); the arthritis is **migratory and typically asymmetric/polyarticular**.

**Suggested UBERON terms.** UBERON:0002097 (skin of body), UBERON:0002360 (meninges), UBERON:0001474 (bone tissue), UBERON:0000948 (heart), UBERON:0002405 (immune system), UBERON:0001456 (joint / articular structures).

---

## 8. Temporal Development

- **Incubation.** Typically **3–10 days** after exposure for the streptobacillary form (Haverhill fever similar).
- **Onset pattern.** **Acute/abrupt** — fever, chills, myalgia, followed within days by rash and migratory polyarthritis.
- **Disease course.** If untreated, a **relapsing/episodic** fever pattern can occur, or progression over days-to-weeks to endocarditis and sepsis. A fatal pet-shop case progressed to death **59 days** after the initiating injury ([PMID: 15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/)).
- **With treatment.** Resolution in **days to a few weeks**; the acute systemic illness is otherwise self-limited in some but unpredictably severe in others.
- **Critical period for intervention.** Early empiric antibiotic therapy (before endovascular seeding) is the decisive window; it "can prevent serious complications" ([PMID: 41480582](https://pubmed.ncbi.nlm.nih.gov/41480582/)).

---

## 9. Inheritance and Population

- **Inheritance / genetics.** **Not applicable** — acquired infection with no heritable component, penetrance, expressivity, anticipation, founder effect, or carrier frequency.
- **Epidemiology.** Rare and underreported; not nationally reportable in most settings ([PMID: 42623631](https://pubmed.ncbi.nlm.nih.gov/42623631/)). No reliable population prevalence/incidence figures exist.
- **Age distribution.** Skewed toward children — in a California reference-laboratory series, "50% of the isolates [were] from patients 9 years old or younger" ([PMID: 11724672](https://pubmed.ncbi.nlm.nih.gov/11724672/)).
- **Sex ratio.** Approximately equal in the same series (roughly balanced sex distribution).
- **Vulnerable groups.** Children and people of low socioeconomic status ([PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/)); occupationally exposed workers.
- **Geographic distribution.** Worldwide where rats and humans coexist; streptobacillary form predominates in the Americas and Europe, spirillary form (*Spirillum minus*) more common in Asia. The largest Canadian series reported 11 cases on Vancouver Island (2010–2016) ([PMID: 31015812](https://pubmed.ncbi.nlm.nih.gov/31015812/)).

---

## 10. Diagnostics

**Approach.** Diagnosis requires a **high index of suspicion** anchored on the exposure history, because "Rat bite fever is a diagnosis that can be easily missed from both a clinical and a microbiological point of view" ([PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/)) and "its nonspecific initial presentation combined with difficulties in culturing its causative organism produces a significant risk of delay or failure in diagnosis" ([PMID: 17223620](https://pubmed.ncbi.nlm.nih.gov/17223620/)).

**Microbiological detection.**

| Method | Performance / notes | Citation |
|---|---|---|
| Blood / joint-fluid culture | Gold standard but fastidious; growth may take ≥72 h | [PMID: 38459199](https://pubmed.ncbi.nlm.nih.gov/38459199/) |
| SPS-aware blood culture | SPS anticoagulant inhibits growth; "up to 0.05% w/v ... seems to be inactivated, allowing for growth and detection" | [PMID: 33693831](https://pubmed.ncbi.nlm.nih.gov/33693831/) |
| 16S rRNA gene PCR/sequencing | "an even more sensitive diagnostic test" than culture; also enables species-level ID | [PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/), [PMID: 40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/) |
| Triplex real-time qPCR | LOD 21 copies/reaction (~4–5 streptobacilli) | [PMID: 35738493](https://pubmed.ncbi.nlm.nih.gov/35738493/) |
| Multiplex real-time PCR | 1–2 genome equivalents/µl for *S. moniliformis*-specific target | [PMID: 33618204](https://pubmed.ncbi.nlm.nih.gov/33618204/) |
| Metagenomic next-gen sequencing (mNGS) | "When culture is negative, 16S rRNA PCR or mNGS can be considered" | [PMID: 40038603](https://pubmed.ncbi.nlm.nih.gov/40038603/) |
| MALDI-TOF | Can misidentify *S. notomytis* as *S. moniliformis* (low score); confirm with sequencing | [PMID: 40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/) |

**Laboratory abnormalities.** Nonspecific: leukocytosis/neutrophilia (or normal WBC), thrombocytopenia, elevated CRP ([PMID: 41480582](https://pubmed.ncbi.nlm.nih.gov/41480582/)).

**Diagnostic traps / serologic cross-reactivity.** RBF has produced **false-positive dengue IgM serology** ([PMID: 41245666](https://pubmed.ncbi.nlm.nih.gov/41245666/)) and **induced ANCA/anti-endothelial antibodies** mimicking ANCA-associated vasculitis ([PMID: 37450033](https://pubmed.ncbi.nlm.nih.gov/37450033/)).

**Differential diagnosis.** Meningococcemia, disseminated gonococcal infection/gonococcal arthritis, Rocky Mountain spotted fever, secondary syphilis, infective endocarditis of other causes, reactive/viral arthritis, and systemic vasculitides ([PMID: 34323361](https://pubmed.ncbi.nlm.nih.gov/34323361/)).

**Genetic testing / omics diagnostics.** Not applicable for host diagnosis; molecular tools target the pathogen.

---

## 11. Outcome / Prognosis

- **Untreated mortality.** RBF "carries a mortality rate of 10%" if untreated ([PMID: 17223620](https://pubmed.ncbi.nlm.nih.gov/17223620/)); severe complications carry "a mortality rate as high as 13% without proper treatment" ([PMID: 16858964](https://pubmed.ncbi.nlm.nih.gov/16858964/), [PMID: 42732473](https://pubmed.ncbi.nlm.nih.gov/42732473/)).
- **Complications.** Infective endocarditis (native and prosthetic valves; can require valve replacement), aortic root abscess, septic arthritis, osteomyelitis, meningitis, interstitial pneumonia, and refractory cardiogenic shock. A fatal case progressed to endocarditis "involving first the aortic valve and then the mitral valve and septum" ([PMID: 15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/)); another required VA-ECMO and died of refractory cardiogenic shock ([PMID: 42732473](https://pubmed.ncbi.nlm.nih.gov/42732473/)).
- **Recovery with treatment.** Excellent — most patients recover fully with prompt, appropriate antibiotics.
- **Prognostic factors.** The dominant modifiable determinant is **time-to-diagnosis/treatment**; endovascular involvement (endocarditis) markedly worsens prognosis. Host genetic prognostic biomarkers do not exist.

---

## 12. Treatment

**First-line pharmacotherapy.** **Penicillin** is the standard therapy; RBF has an "almost omnisensitive susceptibility pattern" and responds to "a commonly available standard therapy (penicillin)" ([PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/)). Penicillin G / amoxicillin are curative in uncomplicated disease.

| Scenario | Regimen (reported) | Citation |
|---|---|---|
| Uncomplicated RBF | Penicillin G / amoxicillin | [PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/), [PMID: 42623631](https://pubmed.ncbi.nlm.nih.gov/42623631/) |
| Severe / disseminated | Ampicillin-sulbactam + doxycycline → symptom regression | [PMID: 38459199](https://pubmed.ncbi.nlm.nih.gov/38459199/) |
| Endocarditis / endovascular | Ceftriaxone (e.g., 6-week course) | [PMID: 35693327](https://pubmed.ncbi.nlm.nih.gov/35693327/) |
| Atypical / localized + abscess | IV ampicillin + doxycycline + surgical debridement | [PMID: 41480582](https://pubmed.ncbi.nlm.nih.gov/41480582/) |

**Surgical / interventional.** Valve repair/replacement for endocarditis; incision-and-drainage/debridement for abscesses and septic joints; mechanical circulatory support (ECMO) in refractory shock (often a marker of late presentation).

**Advanced/experimental therapeutics, pharmacogenomics, immunotherapy, gene/cell/RNA therapy.** Not applicable — this is a bacterial infection managed with standard antibiotics.

**Suggested NCIT terms.** NCIT:C1145 (Penicillin), NCIT:C299 (Amoxicillin), NCIT:C560 (Ceftriaxone), NCIT:C561 (Doxycycline), NCIT:C1728 (Ampicillin).

---

## 13. Prevention

- **Primary prevention (behavioral/occupational).** Avoidance of rodent exposure, personal protective equipment, and rodent control. "Keeping rats as pets cannot be recommended" ([PMID: 34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/)); "Education on hazards of animal contact and other preventive measures are needed in small places of business like pet shops" ([PMID: 15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/)).
- **Wound care / post-exposure prophylaxis.** Immediate cleansing of rodent bites/scratches and consideration of post-exposure antibiotic prophylaxis (penicillin/amoxicillin) after high-risk exposures.
- **Secondary prevention.** Early empiric therapy in exposed febrile patients prevents complications ([PMID: 41480582](https://pubmed.ncbi.nlm.nih.gov/41480582/)).
- **Immunization.** **No licensed human vaccine exists.**
- **Public-health measures.** Rodent control, education, and improved clinical awareness; because the disease is not reportable, surveillance is limited.

---

## 14. Other Species / Natural Disease

- **Reservoir.** Rats (*Rattus norvegicus*, NCBI:txid10116) carry *S. moniliformis* as a nasopharyngeal commensal. The organism "is also a pathogen in certain laboratory and domestic animals" ([PMID: 7707673](https://pubmed.ncbi.nlm.nih.gov/7707673/)).
- **Natural / veterinary disease.** Causes epizootics in mice (*Mus musculus*, NCBI:txid10090), disease in guinea pigs and other species, and recurs in barrier-maintained rodent colonies; it is an occupational hazard for laboratory-animal personnel ([PMID: 7707673](https://pubmed.ncbi.nlm.nih.gov/7707673/)). Reported in a dog phlegmon.
- **Zoonotic potential.** High — pet and feeder murid rodents are documented sources of zoonotic *Streptobacillus* transmission in a global systematic review ([PMID: 37643287](https://pubmed.ncbi.nlm.nih.gov/37643287/)).
- **Taxonomy.** Causative agents: *S. moniliformis* (NCBI:txid34105), *S. notomytis* (distinct species; [PMID: 40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/)).

---

## 15. Model Organisms

Because this is a naturally occurring zoonosis, "model organisms" are the natural rodent hosts rather than engineered genetic disease models. **Laboratory mice and rats** serve as infection/carriage models and are relevant to colony health and occupational exposure ([PMID: 7707673](https://pubmed.ncbi.nlm.nih.gov/7707673/)). Guinea pigs and other laboratory species are naturally susceptible. **No knockout/knock-in/transgenic host-genetic models** are relevant, since there is no host genetic etiology. Research applications center on pathogen biology, transmission, diagnostics development (e.g., qPCR/mNGS validation using clinical and animal matrices; [PMID: 35738493](https://pubmed.ncbi.nlm.nih.gov/35738493/)), and colony surveillance.

---

## Mechanistic Model / Interpretation

The disease can be understood as a two-branch dissemination model downstream of a single initiating event (rodent-to-human inoculation of a rat commensal). The **septic branch** explains the most lethal manifestations (endocarditis, osteomyelitis, septic arthritis) via direct hematogenous seeding, while the **immune-mediated branch** explains vasculitic rash, reactive arthritis, and autoantibody phenomena. Both branches converge on inflammatory tissue injury that manifests as the classic triad and, when unchecked, multi-organ failure.

| Dimension | Streptobacillary RBF |
|---|---|
| Etiology | Infectious (*S. moniliformis* ± *S. notomytis*) |
| Host genetics | Not applicable |
| Key modifiable determinant of outcome | Time-to-diagnosis/treatment |
| Curability | High (penicillin-susceptible) |
| Untreated mortality | 10–13% |
| Diagnostic bottleneck | Fastidious culture, SPS inhibition → molecular methods |
| Prevention | Behavioral/occupational; no vaccine |

The overarching interpretation, synthesizing all 15 findings, is that **danger in RBF is a function of recognition, not host susceptibility.** The organism is nearly omnisensitive to antibiotics, so nearly all mortality is attributable to delayed diagnosis driven by nonspecific symptoms and difficult microbiology.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [17223620](https://pubmed.ncbi.nlm.nih.gov/17223620/) | *Rat bite fever and Streptobacillus moniliformis* | Establishes organism, triad, 10% untreated mortality, diagnostic-delay risk |
| [16858964](https://pubmed.ncbi.nlm.nih.gov/16858964/) | *RBF presenting with rash and septic arthritis* | Upper-bound 13% untreated mortality; septic arthritis |
| [11724672](https://pubmed.ncbi.nlm.nih.gov/11724672/) | *RBF: a potential emerging disease* | Triad + exposure; pediatric age skew (50% ≤9 y) |
| [34323361](https://pubmed.ncbi.nlm.nih.gov/34323361/) | *RBF: review of 29 cases* | Transmission via contaminated fluids; broad differential |
| [15029568](https://pubmed.ncbi.nlm.nih.gov/15029568/) | *Fatal RBF in a pet-shop employee* | Non-bite occupational transmission; fatal endocarditis; prevention |
| [34672901](https://pubmed.ncbi.nlm.nih.gov/34672901/) | *RBF: case report review* | 16S rRNA PCR; penicillin standard; vulnerable populations; easily missed |
| [40472936](https://pubmed.ncbi.nlm.nih.gov/40472936/) | *S. notomytis arthritis/osteomyelitis* | Taxonomic expansion; sequencing > MALDI-TOF |
| [2718962](https://pubmed.ncbi.nlm.nih.gov/2718962/) | *Fatal infection in a 2-month-old infant* | Autopsy multi-organ pathology; hematogenous dissemination |
| [37450033](https://pubmed.ncbi.nlm.nih.gov/37450033/) | *RBF mimicking ANCA-associated vasculitis* | Immune-mediated branch; autoantibody diagnostic trap |
| [33693831](https://pubmed.ncbi.nlm.nih.gov/33693831/) | *BDFX40 / 0.05% SPS 55-yr study* | SPS inhibition and its mitigation |
| [35738493](https://pubmed.ncbi.nlm.nih.gov/35738493/) | *Triplex real-time qPCR* | Sensitive molecular quantification (LOD ~4–5 bacteria) |
| [33618204](https://pubmed.ncbi.nlm.nih.gov/33618204/) | *Multiplex real-time PCR* | Species-differentiating culture-free assay |
| [40038603](https://pubmed.ncbi.nlm.nih.gov/40038603/) | *Atypical RBF knee infection (China)* | mNGS/16S when culture negative |
| [35693327](https://pubmed.ncbi.nlm.nih.gov/35693327/) | *RBF in an HIV patient* | Ceftriaxone for endovascular disease |
| [42732473](https://pubmed.ncbi.nlm.nih.gov/42732473/) | *Fatal RBF / MCS conundrum* | 13% mortality; endocarditis; late presentation lethal |
| [42623631](https://pubmed.ncbi.nlm.nih.gov/42623631/) | *A confirmed case of RBF* | Underreporting; not nationally reportable |
| [7707673](https://pubmed.ncbi.nlm.nih.gov/7707673/) | *S. moniliformis — a zoonotic pathogen* | Reservoir; veterinary/laboratory-animal disease |
| [37643287](https://pubmed.ncbi.nlm.nih.gov/37643287/) | *Zoonotic pathogens in pet/feeder rodents* | Pet/feeder rodents as zoonotic source |
| [31015812](https://pubmed.ncbi.nlm.nih.gov/31015812/) | *RBF on Vancouver Island 2010–2016* | Largest Canadian series; epidemiology |
| [41245666](https://pubmed.ncbi.nlm.nih.gov/41245666/) | *False-positive dengue IgM in RBF* | Serologic cross-reactivity trap; migratory polyarthritis |
| [41480582](https://pubmed.ncbi.nlm.nih.gov/41480582/) | *RBF as localized cellulitis (Nepal)* | Atypical presentation; early empiric therapy prevents complications |
| [38459199](https://pubmed.ncbi.nlm.nih.gov/38459199/) | *New awareness for zoonoses / RBF* | Blood culture at 72 h; ampicillin-sulbactam + doxycycline |

---

## Limitations and Knowledge Gaps

- **Evidence quality.** The literature is almost entirely **case reports and small case series**; there are no randomized trials or large prospective cohorts. Reported mortality (10–13%) derives from historical/aggregate reviews, not modern population data.
- **Underreporting.** RBF is not nationally reportable in most jurisdictions, so true incidence/prevalence are unknown and likely underestimated.
- **Pathophysiology.** The immune-mediated branch (vasculitis, ANCA induction) is documented in isolated cases; the mechanistic link (molecular mimicry vs. bystander activation) is **inferred, not experimentally demonstrated**.
- **Species attribution.** The clinical significance and relative frequency of *S. notomytis* vs *S. moniliformis* are only beginning to be resolved as sequencing supplants MALDI-TOF.
- **No host-omics.** As a non-genetic infection, there are no host transcriptomic/proteomic/metabolomic signatures, biomarkers, or genetic model organisms of the disease per se.
- **Diagnostics.** Molecular assays (qPCR, mNGS) are validated largely on mock/animal matrices; broad clinical validation and availability remain limited.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective surveillance / registry.** Establish a multicenter RBF registry (given non-reportable status) to quantify incidence, exposure patterns, species distribution (*S. moniliformis* vs *S. notomytis*), and outcomes.
2. **Molecular diagnostic deployment.** Validate and disseminate 16S rRNA PCR, triplex/multiplex qPCR ([PMID: 35738493](https://pubmed.ncbi.nlm.nih.gov/35738493/), [PMID: 33618204](https://pubmed.ncbi.nlm.nih.gov/33618204/)) and mNGS in routine clinical labs, and standardize SPS-aware blood-culture protocols ([PMID: 33693831](https://pubmed.ncbi.nlm.nih.gov/33693831/)).
3. **Clinical decision support.** Build an exposure-triggered alert ("febrile + rodent contact") to shorten time-to-empiric-therapy, the key outcome determinant.
4. **Mechanistic studies.** Investigate the immune-mediated branch — whether *S. moniliformis* antigens drive ANCA/anti-endothelial antibodies via molecular mimicry ([PMID: 37450033](https://pubmed.ncbi.nlm.nih.gov/37450033/)).
5. **Occupational/public-health intervention.** Evaluate education and PPE programs for pet-shop and laboratory-animal workers, and formalize post-exposure prophylaxis guidance after rodent bites.
6. **Species epidemiology.** Systematically re-identify archived isolates by sequencing to define the burden of *S. notomytis* human disease.

---

*Report compiled from 15 confirmed findings across 28 reviewed papers. Evidence source types: predominantly human clinical case reports/series and narrative reviews, with supporting in vitro/analytical diagnostic-development studies. This is an infectious, non-genetic disease; all host-genetic template sections are marked Not Applicable.*


## Artifacts

- [OpenScientist final report](Streptobacillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Streptobacillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 24 |
| Quoted claims found in source | 23 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 23 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42732473` *(abstract only)*: "a mortality rate as high as 13% without proper treatment"
  - closest text in source: "BACKGROUND: Rat bite fever is a rare infection that can cause severe complications such as infective endocarditis with a mortality rate of 13% if left untreated"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 28 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020533` (2 mentions) - the report calls it "Mondo"; MONDO calls it **streptobacillary rat-bite fever**
- `DOID:0050144` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **Kartagener syndrome**
- `UBERON:0001456` (1 mention) - the report calls it "joint / articular structures"; UBERON calls it **face**
- `NCIT:C1145` (1 mention) - the report calls it "Penicillin"; NCIT calls it **Lignan**
- `NCIT:C299` (1 mention) - the report calls it "Amoxicillin"; NCIT calls it **Beclomethasone Dipropionate**
- `NCIT:C560` (1 mention) - the report calls it "Ceftriaxone"; NCIT calls it **Hydroxyurea**
- `NCIT:C561` (1 mention) - the report calls it "Doxycycline"; NCIT calls it **Ibuprofen**
- `NCIT:C1728` (1 mention) - the report calls it "Ampicillin"; NCIT calls it **Celecoxib**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0011227` (1 mention) - the report calls it "Elevated C-reactive protein"; HP calls it **Elevated circulating C-reactive protein concentration**, and lists "Elevated C-reactive protein level" among its other names
- `GO:0006909` (1 mention) - the report calls it "phagocytosis, for erythrophagocytosis"; GO calls it **phagocytosis**
- `CL:0000115` (1 mention) - the report calls it "endothelial cell, vasculitis target"; CL calls it **endothelial cell**
- `UBERON:0001474` (2 mentions) - the report calls it "bone tissue"; UBERON calls it **bone element**, and lists "bones" among its other names
- `UBERON:0002360` (2 mentions) - the report calls it "meninges"; UBERON calls it **meninx**