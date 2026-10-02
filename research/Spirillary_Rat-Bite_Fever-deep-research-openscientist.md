---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T09:48:36.027880'
end_time: '2026-09-25T10:04:49.660484'
duration_seconds: 973.63
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spirillary Rat-Bite Fever
  mondo_id: MONDO:0020532
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
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 8
  relevance_assessed: 35
  on_topic: 18
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 52
  verified: 51
  not_found: 1
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.019
  labels_checked: 6
  labels_matching: 3
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0031385
    reported_labels:
    - abnormal serology, approximate
    ontology_label: Megakaryocyte nucleus hypolobulation
  - term_id: NCIT:C716
    reported_labels:
    - Penicillin
    - First-line pharmacotherapy:** **Penicillin
    ontology_label: Omeprazole
  - term_id: NCIT:C641
    reported_labels:
    - doxycycline
    ontology_label: Methimazole
  unresolved_terms:
  - UBERON:0005802
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spirillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spirillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spirillary Rat-Bite Fever
- **MONDO ID:** MONDO:0020532 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Spirillary Rat-Bite Fever** covering all of the
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

# Spirillary Rat-Bite Fever (Sodoku) — Comprehensive Disease Characterization

**Disease:** Spirillary Rat-Bite Fever | **MONDO:** MONDO:0020532 | **Category:** Infectious Disease
**Causative agent:** *Spirillum minus* (syn. *Spirillum minor*)
**Report date:** 2026-09-25

> **Evidence-source note.** This is a bacterial zoonosis, not a genetic disorder. Sections designed for
> Mendelian/genetic diseases (host causal genes, pathogenic variants, inheritance, penetrance,
> chromosomal abnormalities, germline/somatic status) are **Not applicable**; where relevant, the
> analogous *pathogen* genetics/biology is provided instead. Evidence is predominantly **human clinical**
> (case reports/series, narrative and systematic reviews) with some **veterinary/microbiological** data.
> Much of the *Spirillum minus*-specific literature is old and observational because the organism cannot
> be cultured on artificial media; contemporary molecular data are sparse.

---

## 1. Disease Information

**Overview.** Spirillary rat-bite fever (RBF) is a systemic, relapsing febrile zoonosis acquired chiefly
through the bite or scratch of a rat (or other rodent) infected with *Spirillum minus*, a small,
tightly-coiled, motile, Gram-negative spiral bacterium. It is one of the two classic forms of rat-bite
fever; the other, streptobacillary RBF, is caused by *Streptobacillus moniliformis*. The spirillary form
predominates in Asia — its Japanese name **"sodoku"** (鼠毒, "rat poison") reflects this — whereas the
streptobacillary form predominates in the Americas and Europe. RBF "is a rare but potentially fatal
zoonotic disease caused by *Streptobacillus moniliformis* or *Spirillum minus*. In Asia, it is often
caused by *Spirillum minus*" (PMID 41480582). It has been recognized as a clinical entity for over
2000 years (PMID 28002119).

**Distinguishing clinical fingerprint (vs streptobacillary form).** Spirillary RBF classically features a
longer incubation (typically 1–4 weeks; often >7 days, vs 3–10 days for streptobacillary), **re-activation
and ulceration of the healed original bite wound**, **regional lymphangitis/lymphadenopathy**, a
**relapsing (recurrent) fever** pattern, and a distinctive violaceous/roseolar-to-macular rash;
**arthritis and myalgia are uncommon** (arthritis is a hallmark of the streptobacillary form). It is
**not** associated with the "Haverhill fever" foodborne/ingestion syndrome (that is streptobacillary).

**Key identifiers.**
- **MONDO:** MONDO:0020532 (spirillary rat-bite fever)
- **ICD-10:** A25.0 (Spirillosis — the spirillary form of rat-bite fever); A25.9 (rat-bite fever, unspecified); parent A25 (Rat-bite fevers)
- **ICD-11:** 1B94 (Rat-bite fever) with the spirillary form as *Spirillum minus* infection
- **MeSH:** "Rat-Bite Fever" (D011906); organism "*Spirillum*" (D013183)
- **SNOMED CT:** Rat-bite fever (disorder); Spirillosis / *Spirillum minus* infection
- **OMIM / Orphanet:** Not applicable as a Mendelian entry. Orphanet does not classify this common-cause
  infectious disease as a rare disease with an ORPHA code (RBF is generally handled through ICD, not
  Orphanet).
- **NCBI Taxonomy (pathogen):** *Spirillum minus* — historically classified in genus *Spirillum*; note the
  type species *Spirillum volutans* is the validly-described genus member. *S. minus* has never been
  formally cultured/validly published under the Bacteriological Code, so its taxonomic status is
  provisional.

**Synonyms / alternative names.** Sodoku; spirillosis; spirillary fever; spirillum fever; *Spirillum minus*
infection; *Spirillum minor* infection; rat-bite fever (spirillary type); (historically) "the Asian form"
of rat-bite fever. Older literature also used *Spirochaeta morsus muris*.

**Information source.** Aggregated disease-level knowledge from case reports, case series and reviews;
there is no large individual-patient (EHR) cohort resource for this rare disease.

**HPO/ontology anchors for the entry:** disease MONDO:0020532; see §3 for HP terms.

---

## 2. Etiology

**Primary cause (infectious).** Infection with ***Spirillum minus***, a Gram-negative, aerobic,
helically-coiled (2–5 tight spirals), rigid, highly motile bacterium (2–5 µm) bearing bipolar polytrichous
flagella. Transmission is by **bite or scratch of an infected rat** (most common), other rodents (mice,
squirrels), or animals that prey on rodents (cats, weasels, dogs). Unlike the streptobacillary form,
**foodborne (ingestion) transmission is not described for *S. minus***. Human-to-human transmission does
not occur. RBF is transmitted "to humans by" rodents and their predators (PMID 39628725), and can even be
established "with contaminated vehicle contact alone, not only as a direct result of a bite" (PMID 26584844,
described for *S. moniliformis*).

**Reservoir.** Wild and domestic (pet/laboratory) rats are the principal reservoir; *S. minus* colonizes
the oropharynx/nasopharynx and conjunctiva of a substantial fraction of healthy rats asymptomatically. A
comprehensive review covers the two causal species, their host species, pathogenicity (virulence factors
and host susceptibility), diagnosis, therapy, epidemiology, transmission and prevention (PMID 19008054).

**Haverhill fever distinction.** The **foodborne** variant, *Haverhill fever*, "is a form of *S.
moniliformis* infection believed to develop after ingestion of contaminated food or water" (PMID 19008054)
— it is **exclusively streptobacillary** and has **no spirillary counterpart** (*S. minus* is not
transmitted by ingestion).

**Risk factors (environmental / behavioral).**
- **Rodent exposure** — the dominant risk factor. In a systematic review of streptobacillary endocarditis,
  "Exposure to rats was noted in 71.8% of patients, with 56.4% recalling a rat bite" (PMID 37101553).
- **Occupational:** laboratory-animal workers, pet-shop/feeder-rodent handlers, veterinarians, farm and
  sanitation workers, biomedical researchers. "Those working in places where rodents breed or are at risk
  of contact with rats or mice might be at risk" (PMID 26584844).
- **Pet ownership** — pet rats are an increasingly common source (PMID 17223620; PMID 26701936:
  "three domestic rats living in the girl's home"). "Keeping rats as pets cannot be recommended" (PMID 34672901).
- **Housing/poverty & crowding** — historically linked to higher rat contact ("housing conditions and
  habits of the people," PMID 19867970); homelessness (PMID 38459199).
- **Demographics:** children and low socioeconomic groups are a vulnerable population (PMID 34672901).
- **Host immune status:** immunocompromise (cirrhosis, CKD, HIV/AIDS) predisposes to severe/complicated
  disease (PMID 29709962; PMID 11139161); RBF has presented as culture-negative septic arthritis in newly
  diagnosed HIV (PMID 21877181). Alcohol-use disorder is a recurrent comorbidity (PMID 20397505).

**Genetic host risk / protective factors.** **Not applicable / none established** — no host germline
susceptibility or protective variants, GWAS loci, or gene–environment interactions have been described for
RBF. Susceptibility is essentially exposure-driven.

**Protective factors (environmental).** Rodent avoidance/control, wound hygiene and prompt post-bite wound
care, use of gloves/protective equipment by animal handlers, and prompt post-exposure antibiotics (see §13).

**CHEBI/agent anchor:** causative agent *Spirillum minus* (NCBITaxon).

---

## 3. Phenotypes (Clinical Manifestations)

RBF "is characterized by a clinical triad of symptoms, fever, rash and arthritis" (PMID 39267964); however
the **spirillary** form has a characteristic pattern that differs from the streptobacillary form. Frequency
figures below are qualitative/derived from case literature (no large prospective cohort exists).

| Phenotype | Type | HP term (suggested) | Onset/course | Frequency in spirillary RBF |
|---|---|---|---|---|
| **Fever, relapsing/recurrent** (spikes to 39–40°C, recurring every 3–5 days over weeks) | Symptom/sign | HP:0001954 (Recurrent fever); HP:0001945 (Fever) | Subacute onset after 1–4 wk incubation; **relapsing** | Very frequent (hallmark) |
| **Ulceration/reactivation of the healed bite wound** (indurated, painful, may eschar) | Clinical sign | HP:0200041 (Skin ulcer); HP:0025276 (Eschar) | Appears with first febrile relapse | Frequent (characteristic of sodoku) |
| **Regional lymphangitis & lymphadenopathy** proximal to bite | Clinical sign | HP:0002716 (Lymphadenopathy); HP:0100763 (Lymphangitis) | With fever onset | Frequent |
| **Rash** — violaceous/red-brown macular, roseolar or maculopapular, classically **petechial-purpuric on the extremities**, and may involve **palms and soles** with mixed maculopapular/pustular eruptions (PMID 21358889, 9856201) | Physical manifestation | HP:0000988 (Skin rash); HP:0007398 (Maculopapular exanthema); HP:0000979 (Purpura); HP:0000967 (Petechiae); HP:0006740 (Palmoplantar rash, approximate) | With febrile relapses | Common (though may be absent — PMID 41480582) |
| **Constitutional:** malaise, headache, rigors/chills, myalgia | Symptom | HP:0002027; HP:0002315; HP:0025143; HP:0003326 | With fever | Common |
| **Arthralgia/arthritis** | Symptom/sign | HP:0002829; HP:0001369 | Later | **Uncommon** in spirillary form (contrasts with streptobacillary, where migratory polyarthritis is typical) |
| **Localized cellulitis** (atypical presentation) | Sign | HP:0100658 (Cellulitis) | Days after bite | Reported (PMID 41480582) |
| **Laboratory: neutrophilia, thrombocytopenia, elevated CRP** | Lab abnormality | HP:0011897; HP:0001873; HP:0011227 | Acute | Reported (PMID 41480582) |
| **Laboratory: anemia, leukocytosis** | Lab abnormality | HP:0001903; HP:0001974 | Variable | Common in RBF (PMID 37101553: anemia 57%, leukocytosis 52%) |
| **False-positive syphilis serology** (VDRL/RPR reactive; treponemal tests negative) | Lab abnormality | HP:0031385 (abnormal serology, approximate) | During illness | Classic for spirillary RBF |
| **Severe/complicated:** endocarditis, meningitis, hepatitis, myocarditis, sepsis | Sign | HP:0100584; HP:0001287; HP:0200119; HP:0100806 | Late/untreated | Rare but high-mortality |

**Age of onset / severity / progression.** Any age; children over-represented among reported cases.
Severity ranges mild → life-threatening; untreated disease is **relapsing** and can persist for weeks to
months, occasionally 1–2 years, with febrile bouts separated by afebrile intervals.

**Quality-of-life impact.** No formal EQ-5D/SF-36/PROMIS data exist for this rare disease. Acute illness
causes days–weeks of incapacitating fever and malaise; treated disease usually resolves without sequelae
("recovered fully"/"without long-term sequelae," PMID 41480582, PMID 26701936). Complicated disease
(endocarditis, osteomyelitis, septic arthritis) can cause lasting disability or death.

---

## 4. Genetic / Molecular Information

**Host genetics — Not applicable.** No causal genes, pathogenic variants, modifier genes, epigenetic
signatures, or chromosomal abnormalities in the human host. Not heritable.

**Pathogen molecular biology (analogous section).** *Spirillum minus* is a fastidious spiral bacterium that
**has never been grown in axenic culture**, so its genome is poorly characterized; there is no validated
reference genome, and identification historically depended on morphology and animal passage rather than
sequencing. This contrasts with *S. moniliformis*, for which 16S rRNA gene sequencing is the mainstay of
molecular identification (PMID 34583654; PMID 35365242). Consequently, no defined virulence genes, toxins,
or resistance determinants are catalogued for *S. minus*; penicillin susceptibility is inferred clinically
(§12).

---

## 5. Environmental Information

- **Infectious agent:** *Spirillum minus* (spiral Gram-negative bacterium). Reservoir: rats/rodents and
  their predators.
- **Environmental factors:** rodent-infested dwellings, poor sanitation, and settings with high
  human–rodent contact (urban poverty, homelessness, agriculture, laboratories, pet trade). Urbanization
  and climate change are increasing human–rodent interactions and zoonotic risk generally (PMID 41011829).
- **Lifestyle factors:** keeping pet rodents; handling feeder rodents; sleeping in rodent-infested
  environments (bites often occur at night on hands/face of sleeping infants).
- **No toxic/radiation/chemical etiology.**

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating event → clinical manifestation)

1. **Rodent bite/scratch (or contact with rodent secretions)** inoculates *Spirillum minus* into the skin
   and subcutaneous tissue → local infection. *(Demonstrated: transmission by bite.)*
2. The inoculation wound **initially heals**, then after an incubation of ~1–4 weeks the organism
   **re-activates locally**, producing induration, ulceration and sometimes eschar at the original bite
   site. *(Characteristic of sodoku; mechanism of the healing-then-reactivation is inferred, not
   molecularly demonstrated.)*
3. Organisms **drain via lymphatics** → **regional lymphangitis and lymphadenopathy**. *(Inferred from
   clinical pattern.)*
4. **Lymphohematogenous dissemination** → intermittent **bacteremia/spirochetemia**, which drives the
   **relapsing fever** (febrile bouts coinciding with waves of bacteremia; afebrile intervals as the host
   immune response transiently clears circulating organisms). *(Inferred, analogous to other relapsing
   bacteremic infections.)*
5. Circulating organisms and the host **innate inflammatory response** (neutrophilia, elevated CRP,
   cytokine release) → systemic constitutional symptoms and the characteristic **exanthem** (probably an
   immune/vasculitic-type cutaneous reaction). RBF has been reported to mimic and induce vasculitis, incl.
   ANCA/anti-endothelial antibodies (PMID 37450033), and to mimic Henoch–Schönlein purpura
   (PMID 29709962), implicating **immune-mediated small-vessel injury** in the skin.
6. **In untreated/immunocompromised hosts,** persistent bacteremia seeds distant sites → **metastatic/deep
   infection**: infective **endocarditis** (valve vegetations; PMID 23993005, 37101553), and (more typical
   of the streptobacillary form) septic arthritis, osteomyelitis, meningitis, hepatitis, myocarditis,
   abscesses → organ failure and, in ~7–13% untreated, **death** (PMID 17223620, 21358889, 34211343).

**Branch point:** After step 4, most immunocompetent, treated patients follow a benign self-limited/curable
course (branch A); a minority — often with valvulopathy or immunocompromise (branch B) — progress to
endocarditis and disseminated disease with high mortality (PMID 37101553; risk in prior valve disease
PMID 1562665; immunocompromise PMID 29709962, 11139161).

### Mechanistic detail / ontology anchors
- **Cellular processes:** acute inflammation (GO:0006954, inflammatory response), innate immune response
  (GO:0045087), neutrophil-mediated response (GO:0002446), possible immune-complex/vasculitic tissue injury.
- **Cell types (CL):** neutrophils (CL:0000775), macrophages (CL:0000235), vascular endothelial cells
  (CL:0000115), lymphocytes.
- **Immune involvement:** predominantly innate + humoral; agglutinating antibodies to the organism arise
  during infection (historically documented, PMID 19867970: "production of powerful agglutinins for the
  organism"). Reactive autoantibodies (ANCA, AECA) can appear (PMID 37450033).
- **Tissue damage mechanisms:** direct bacterial invasion + immune-mediated small-vessel/endothelial injury;
  valve vegetation formation in endocarditis.
- **Molecular pathways:** classical innate pattern-recognition/inflammatory signaling (e.g., TLR–NF-κB,
  IL-1/IL-6/TNF cytokine axes) — **inferred by analogy**, not specifically demonstrated for *S. minus*.
- **Molecular/omics profiling, single-cell, CRISPR screens, etc.:** **Not available** — the organism is
  unculturable and rare; no transcriptomic/proteomic/metabolomic datasets exist. Even for the culturable
  *S. moniliformis*, "Virtually nothing is known regarding prevalence in humans and animal reservoirs,"
  and full-genome studies of *Streptobacillus* are only now being called for to define virulence traits
  (PMID 27088660) — for *S. minus* the genomic knowledge gap is essentially total.

---

## 7. Anatomical Structures Affected

- **Primary site:** skin/subcutaneous tissue at the bite (UBERON:0002097 skin of body; UBERON:0002199
  integumentary system) and **regional lymphatic vessels/nodes** (UBERON:0001473 lymph node;
  UBERON:0001473; lymphatic vessel UBERON:0001473→UBERON:0005802).
- **Body systems involved:** integumentary, lymphatic/hematologic (bacteremia), and — in complications —
  **cardiovascular** (endocardium/heart valves, UBERON:0002165 endocardium; UBERON:0000946 cardiac valve),
  **musculoskeletal** (joints UBERON:0000955→UBERON:0002544; bone), **nervous** (meninges, UBERON:0002360),
  **hepatic** (liver UBERON:0002107), and reticuloendothelial (spleen — splenomegaly reported, PMID 37101553).
- **Tissue/cell level:** vascular endothelium and dermal small vessels (rash/vasculitis); valvular
  endocardial surface (vegetations); synovium and bone in metastatic infection.
- **Subcellular:** no specific organelle target (extracellular bacterium); GO cellular component anchors
  are not specifically implicated.
- **Localization / laterality:** bite-site lesion and lymphadenopathy are **regional/unilateral** (side of
  the bite); rash and systemic features are generalized/bilateral. Endocarditis most often affects the
  **mitral valve**, then aortic > tricuspid > pulmonary (PMID 37101553).

---

## 8. Temporal Development

- **Onset:** acquired at any age; **subacute** onset after an **incubation of ~1–4 weeks** (spirillary form
  characteristically longer than the 3–10 days of streptobacillary RBF; presumptive diagnosis relies on
  "incubation period," PMID 41480582).
- **Course:** untreated disease is **relapsing/episodic** — recurrent febrile bouts every few days with
  afebrile intervals — persisting for weeks to months, occasionally 1–2 years.
- **Progression rate:** variable; usually self-limited-to-chronic if untreated in the immunocompetent, but
  can be rapidly progressive/fatal if endocarditis or sepsis supervenes.
- **Remission:** prompt penicillin produces rapid, usually complete resolution (treatment-induced
  remission); spontaneous resolution can occur but relapse is common without treatment.
- **Critical window:** early antibiotic therapy (before endocarditis/dissemination) is the key
  intervention period — "Early initiation of empiric antibiotic therapy ... can prevent serious
  complications" (PMID 41480582).

---

## 9. Inheritance and Population (Epidemiology)

- **Inheritance:** **Not applicable** (infectious; no heritability, penetrance, expressivity,
  anticipation, mosaicism, founder effect, consanguinity, or carrier frequency).
- **Incidence/prevalence:** true incidence unknown; RBF is **rare, under-reported and under-diagnosed**
  (PMID 29671179; PMID 39628725). Rat bites are frequently **not a mandatory-notification event**, so no
  registry exists — in Buenos Aires "there is no record of it," and 50% of bitten slum residents sought no
  care (PMID 40793882). The largest single Canadian series found **11 cases on Vancouver Island over
  2010–2016** (PMID 31015812). The spirillary form is rarer than the streptobacillary form outside Asia.
- **Geographic distribution:** spirillary RBF (**sodoku**) is concentrated in **Asia** — Japan, China,
  India and elsewhere — "In Asia, it is often caused by *Spirillum minus*" (PMID 41480582); first
  presumptive S. minus case in Nepal reported 2026 (PMID 41480582); a Kenyan case with spirillum-like
  organisms on thick film (PMID 1286642). The streptobacillary form predominates in the Americas/Europe.
  The greater historical frequency in Japan was attributed to housing conditions and rat exposure
  (PMID 19867970).
- **Demographics:** children and people of low socioeconomic status are over-represented (PMID 34672901);
  occupational cohorts (lab/pet-rodent handlers) at risk. Endocarditis series skew male (61.5%) with mean
  age ~41 (PMID 37101553).
- **Sex ratio / age:** no strong intrinsic sex predisposition for uncomplicated disease (exposure-driven);
  bimodal exposure in young children (bites) and adult handlers.

---

## 10. Diagnostics

**The central diagnostic challenge:** *S. minus* **cannot be cultured on artificial media**, and RBF's
symptoms are nonspecific, so diagnosis is frequently **clinical/presumptive** (PMID 41480582:
"the importance of clinical suspicion over microbiological confirmation").

- **Direct microscopy (mainstay for *S. minus*):** demonstration of the characteristic tight spiral,
  motile organism by **darkfield microscopy** or **Giemsa/Wright stain** of blood, bite-wound exudate, or
  aspirate of the regional lymph node. A Kenyan case was diagnosed by "demonstration of spirillum like
  organisms from a thick blood film" (PMID 1286642).
- **Animal inoculation:** intraperitoneal inoculation of blood/exudate into mice or guinea pigs, then
  examining the animal's blood/peritoneal fluid for spirilla — a classic method when microscopy is
  negative.
- **Molecular:** **16S rRNA gene PCR/sequencing** from blood, joint or tissue is the most sensitive
  modern test and can identify RBF organisms in culture-negative cases (PMID 34672901; used for
  *Streptobacillus* speciation in PMID 34583654, 40472936, 35365242). Note a caveat: 16S rRNA analysis
  "may be uncertain for proper pathogen identification" and RBF diagnostics remain a "diagnostic dilemma"
  (PMID 27088660). **Metagenomic next-generation sequencing (mNGS)** can detect the pathogen directly from
  clinical samples "in less than 72 h" even when "blood culture results are negative" (PMID 31315559).
  MALDI-TOF MS is used for *Streptobacillus* but **not** reliable for the unculturable *S. minus*.
- **Blood culture:** typically **negative** for *S. minus* (PMID 41480582); positive cultures instead
  indicate the streptobacillary form (BACTEC/subculture; PMID 29709962, 23993005). Even for
  *S. moniliformis*, routine cultures often fail "because of the fastidious nature of the organism's growth,
  as well as inhibitors present in standard blood culture bottles" — specifically **sodium polyanethol
  sulfonate (SPS)** anticoagulant; the organism may grow only in SPS-free media such as thioglycolate broth
  (PMID 20397505). Prolonged incubation and notifying the lab of suspected RBF are advised.
- **Serology:** no standardized serologic assay; **false-positive non-treponemal syphilis tests
  (VDRL/RPR)** occur in a substantial minority of spirillary cases (treponemal tests negative) — a useful
  diagnostic clue.
- **Laboratory:** neutrophilia, thrombocytopenia, elevated CRP (PMID 41480582); anemia (~57%),
  leukocytosis (~52%), raised inflammatory markers (~58%) across RBF (PMID 37101553).
- **Imaging:** echocardiography (TEE) for suspected endocarditis (PMID 23993005); MRI for
  osteomyelitis/discitis (PMID 34039283, 40472936).
- **Genetic testing (WGS/WES/panels/karyotype/CMA/repeat testing):** **Not applicable** (no host genetic
  disease).
- **Omics-based diagnostics (of the pathogen):** unbiased **metagenomic NGS** of blood, pus or tissue is
  an emerging, rapid, culture-independent confirmatory test (PMID 31315559); host transcriptomic/
  proteomic/metabolomic diagnostic signatures are **not established** for RBF.

**Diagnostic criteria:** no formal society criteria exist; diagnosis rests on **compatible clinical
syndrome + rodent-exposure history + supportive microscopy/PCR** (or response to penicillin).

**Differential diagnosis:** streptobacillary RBF, leptospirosis, borreliosis/relapsing fever, secondary
syphilis (owing to false-positive RPR), Rocky Mountain spotted fever and other rickettsioses, meningococcemia,
infective endocarditis of other cause, disseminated gonococcal infection, viral exanthems, malaria,
reactive/rheumatoid arthritis, ANCA-associated vasculitis (PMID 37450033) and Henoch–Schönlein purpura
(PMID 29709962).

---

## 11. Outcome / Prognosis

- **Untreated mortality ~7–13%** — concordant across sources: "mortality rate of 7% to 10% if untreated" (PMID 21358889), "up to 13%, if untreated" (PMID 34211343), and "10%" (PMID 17223620).
- **With prompt appropriate antibiotics: excellent** — full recovery, usually without sequelae
  (PMID 41480582; PMID 26701936: "full clinical recovery when treated in a timely and appropriate manner").
- **Complications (predominantly untreated/immunocompromised):** infective **endocarditis** (rare but
  frequently fatal — **death in 36%** of pooled cases, surgery in 36%, PMID 37101553), sepsis,
  metastatic septic arthritis/osteomyelitis/discitis (PMID 34039283, 40472936, 26948832), meningitis
  (PMID 34583654), hepatitis, myocarditis, abscess formation, and a **hyperinflammatory syndrome
  resembling hemophagocytic lymphohistiocytosis (HLH)** with multiorgan failure (PMID 32868746).
- **Prognostic factors:** speed of diagnosis/treatment, presence of endocarditis or pre-existing valve
  disease (PMID 1562665), immune status (cirrhosis/CKD/HIV worsen outcome — PMID 29709962, 11139161), and
  age/comorbidity.
- **QoL/disability measures:** no formal instruments reported; residual disability mainly from
  musculoskeletal or cardiac complications.

---

## 12. Treatment

Suggested NCIT anchors given where applicable.

- **First-line pharmacotherapy:** **Penicillin** (NCIT:C716) — IV penicillin G for severe/systemic disease,
  or oral penicillin/amoxicillin for mild disease; typically 7–14 days (uncomplicated), longer for deep
  infection. *S. minus* is penicillin-susceptible; "The bacterium is generally susceptible to penicillin
  antibiotics with full clinical recovery" (PMID 26701936). Patients are often "cured completely after
  intravenous administration of penicillin G" with therapy "completed by an oral course of doxycycline"
  (PMID 9856201). Case cured with penicillin (± gentamicin) — PMID 1286642.
- **Alternatives (penicillin allergy):** **doxycycline** (NCIT:C641)/tetracyclines, **ceftriaxone**
  (NCIT:C1737)/cephalosporins, or macrolides. Combination ampicillin + doxycycline used in the Nepal
  S. minus case (PMID 41480582); ampicillin/sulbactam + doxycycline (PMID 38459199).
- **Endocarditis/deep infection:** high-dose IV penicillin (often with an aminoglycoside such as
  **gentamicin**, NCIT:C557) for 4–6 weeks; ceftriaxone-based regimens also used (PMID 23993005 — IV
  penicillin 6 wk + gentamicin 2 wk; PMID 11139161 — ceftriaxone/gentamicin/penicillin).
- **Aminoglycoside adjunct:** gentamicin as synergistic add-on in severe disease (PMID 1286642, 23993005).
- **Surgical/interventional:** wound debridement for local disease (PMID 41480582); **valve
  replacement/surgery** in ~36% of endocarditis (10/14 needing surgery had replacement, PMID 37101553);
  arthroscopic lavage/DAIR for septic arthritis / prosthetic joint infection (PMID 40472936, 35365242).
- **Supportive care:** antipyretics/analgesia, fluids, treatment of sepsis; NSAIDs for
  arthralgia/vasculitic features (PMID 37450033).
- **Caution:** a **Jarisch–Herxheimer reaction** may follow the first antibiotic doses (as with other
  spiral-organism infections) — monitor and support.
- **Pharmacogenomics, gene/cell/RNA/targeted/immunotherapy:** **Not applicable.**
- **Treatment response:** high cure rates with timely therapy; poorer with delayed diagnosis or
  endocarditis.

---

## 13. Prevention

- **Primary prevention:** **rodent control** and avoidance; safe handling of pet/laboratory rodents
  (gloves, avoid face/hand contact, secure housing); public/occupational **health education**; discourage
  keeping rats as pets, especially around young children ("keeping rats as pets cannot be recommended,"
  PMID 34672901).
- **Post-exposure wound care & prophylaxis:** immediate cleansing/irrigation of bite wounds; consideration
  of **post-bite antibiotic prophylaxis** (e.g., a penicillin/amoxicillin course) after high-risk rodent
  bites; tetanus prophylaxis as indicated.
- **Secondary prevention:** early clinical suspicion in febrile patients with rodent exposure and prompt
  empiric antibiotics to prevent endocarditis/dissemination (PMID 41480582).
- **Tertiary prevention:** complete antibiotic course + follow-up echocardiography where endocarditis is a
  concern; source control (debridement, valve surgery) as needed.
- **Immunization:** **none available** (no human vaccine).
- **Public health / One Health:** integrated rodent surveillance and control; the burden of rodent-borne
  zoonoses is rising with urbanization and climate change, warranting interdisciplinary One Health
  approaches (PMID 41011829).
- **Genetic counseling / screening / newborn screening:** **Not applicable.**

---

## 14. Other Species / Natural Disease

- **Pathogen taxonomy:** *Spirillum minus* (NCBITaxon; genus *Spirillum*).
- **Reservoir hosts (NCBI Taxon):** *Rattus norvegicus* (NCBITaxon:10116, Norway/brown rat),
  *Rattus rattus* (NCBITaxon:10117, black/house rat), *Mus musculus* (NCBITaxon:10090) and other murids;
  carnivores that prey on rodents (cats, dogs, weasels) can transmit via bite.
- **Natural disease in animals:** rats usually carry the organism **asymptomatically** (oropharyngeal/
  conjunctival colonization). Clinically apparent rodent disease is better documented for related
  *Streptobacillus* species — e.g., *Streptobacillus notomytis* caused fatal otitis interna/media with
  neurologic signs in house rats (PMID 29671179), and evidence suggests host tropism (*S. notomytis* with
  *R. rattus* vs *S. moniliformis* with *R. norvegicus*). Analogous systematic carriage of RBF agents in
  pet/feeder murids is globally documented (PMID 37643287).
- **Zoonotic potential / cross-species susceptibility:** **high zoonotic potential** — humans are infected
  from the rodent reservoir; there is no human-to-human spread. Rodents are recognized reservoirs for RBF
  among many bacterial zoonoses (PMID 41011829).
- **Comparative biology / orthologous host genes:** **Not applicable** (no host disease gene).

---

## 15. Model Organisms

- **Classic in vivo model / diagnostic bioassay:** **mouse** (*Mus musculus*, MGI) and **guinea pig**
  (*Cavia porcellus*) intraperitoneal **inoculation** was historically used both to propagate *S. minus*
  (which cannot be grown on media) and as a **diagnostic** tool (examine animal blood/peritoneal fluid for
  spirilla). This is an **induced/experimental infection** model rather than a genetic model.
- **Natural animal host as model:** **rats** (*Rattus* spp., RGD) are natural carriers and have been used
  to study colonization and transmission; *S. notomytis* rat infection provides a natural-disease model of
  *Streptobacillus* pathogenicity (PMID 29671179).
- **Genetic models (knockout/transgenic/etc.):** **Not applicable** — no host genetic disease to model;
  the pathogen is unculturable, precluding standard genetic/CRISPR manipulation and axenic experimental
  systems.
- **Model limitations:** because *S. minus* cannot be cultured, controlled reproducible molecular studies
  are essentially impossible; most mechanistic understanding is inferred from clinical observation and by
  analogy to *S. moniliformis* and other spiral bacteria. Koch's postulates were historically only
  partially fulfilled for RBF organisms (PMID 19867970).
- **Resources:** MGI, RGD (host animals); no dedicated *S. minus* strain repository exists because the
  organism is not maintained in culture.

---

## Summary Answer

Spirillary rat-bite fever (**sodoku**, MONDO:0020532) is a rare, under-diagnosed, **relapsing febrile
zoonosis caused by *Spirillum minus***, a non-culturable spiral Gram-negative bacterium transmitted mainly
by the bite/scratch of infected rats (predominant in Asia). It classically presents after a 1–4-week
incubation with reactivation/ulceration of the healed bite wound, regional lymphadenopathy, a relapsing
fever, and a violaceous rash (arthritis is uncommon, distinguishing it from the streptobacillary form);
diagnosis is largely clinical/presumptive with microscopy, animal inoculation or 16S rRNA PCR because blood
cultures are negative. It is not a genetic disease—there are no host causal genes, inheritance, or
heritable risk factors—and it is **highly treatable with penicillin** (untreated mortality ~7–13%, rising
sharply with complications such as endocarditis), with prevention resting on rodent control, safe rodent
handling, and prompt post-bite wound care and antibiotics.

---

## Limitations and Future Directions

**Evidence limitations.**
- **No high-level evidence.** The entire knowledge base is case reports, small case series, and narrative/
  systematic reviews of those reports — there are **no RCTs, cohort studies, or registries** for RBF, so
  incidence/prevalence, true frequency of each phenotype, and comparative treatment efficacy are all
  imprecise.
- **Spirillary-specific data are especially thin.** Because *S. minus* **cannot be cultured**, most modern
  molecular literature concerns *S. moniliformis*; several claims here (incubation length, relapsing-fever
  mechanism, false-positive RPR, arthritis rarity) rest on classic/older observational descriptions and
  textbook consensus rather than contemporary primary data, and some cited quotes describe the
  streptobacillary form and are extended to the spirillary form by analogy (flagged in-text).
- **Ontology/identifier caveats.** ICD-11 code (1B94) and several UBERON/HP mappings are best-available
  suggestions; the ICD-10 A25.0 "Spirillosis" mapping is the firmest spirillary-specific anchor. *S. minus*
  has no validly published bacteriological name or reference genome.
- **Mechanism is largely inferred.** The pathophysiology causal chain is reconstructed from clinical
  phenomenology plus analogy to other spirochetal/relapsing infections; molecular pathways, cytokine
  profiles, and cell-type contributions have **not** been directly demonstrated for *S. minus*.

**Future directions.**
- Full-genome sequencing of *Streptobacillus* strains and any culturable/enrichable *S. minus* material to
  define virulence traits and improve identification (PMID 27088660).
- Systematic prevalence/carriage surveys in rodent reservoirs and exposed human populations.
- Broader deployment of **16S rRNA PCR and metagenomic NGS** to capture culture-negative and spirillary
  cases and to build a molecularly-confirmed case series (PMID 31315559, 27088660).
- Making rodent bites/RBF a notifiable event to enable real epidemiologic estimates (PMID 40793882).

**Supported vs refuted (framing for this descriptive task).**
- **Supported:** infectious (non-genetic) etiology; penicillin curability; ~7–13% untreated mortality;
  culture-negativity/diagnostic difficulty; rodent-exposure and immunocompromise as risk factors;
  endocarditis as the key lethal complication.
- **Refuted/negative:** no host genetic causal or susceptibility loci; no vaccine; no foodborne (Haverhill)
  route for the spirillary form; no established omics/biomarker diagnostic signature.

---

### Key References (PMIDs)
41480582 (S. minus RBF, Nepal, 2026) · 37450033 (RBF/vasculitis; S. minus morphology) · 39267964 (RBF
triad) · 39628725 (RBF genus review) · 17223620 (RBF review; 10% untreated mortality) · 26701936
(penicillin cure) · 37101553 (systematic review, streptobacillary endocarditis; 36% mortality) · 34672901
(case-report review; 16S PCR; pet-rat caution) · 1286642 (spirillum thick-film diagnosis, Kenya) · 26584844
(non-bite transmission) · 29671179 (*S. notomytis* natural rat disease) · 41011829 (rodent zoonoses / One
Health) · 19867970 (historical etiology) · 28002119 (RBF known >2000 yrs) · 23993005, 11139161, 1562665
(endocarditis) · 29709962 (immunocompromised/HSP-mimic) · 34583654, 40472936, 35365242, 34039283, 38459199,
26948832, 32868746 (complications & molecular diagnosis) · 19008054 (comprehensive RBF review; Haverhill
fever) · 21358889 (pediatric RBF; mortality 7–10%; acral rash) · 34211343 (rodent carriage; mortality up
to 13%) · 34813430 (relapsing fever/rash) · 40793882 (non-notifiable; vulnerable-population survey) ·
31015812 (Vancouver Island case series) · 27088660 (RBF/Streptobacillus diagnostics review; 16S
limitations; prevalence unknown) · 31315559 (metagenomic NGS diagnosis) · 9856201 (pet-rat RBF; penicillin
G + doxycycline cure; palmoplantar rash) · 20397505 (culture pitfalls/SPS inhibitor; thioglycolate broth) ·
21877181 (RBF in HIV/AIDS; culture-negative septic arthritis).

*Evidence base is dominated by case reports/series and reviews; Spirillum-minus-specific molecular data are
scarce because the organism cannot be cultured.*


## Artifacts

- [OpenScientist final report](Spirillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spirillary_Rat-Bite_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 35 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 52 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0031385` (1 mention) - the report calls it "abnormal serology, approximate"; HP calls it **Megakaryocyte nucleus hypolobulation**
- `NCIT:C716` (1 mention) - the report calls it "Penicillin", "First-line pharmacotherapy:** **Penicillin"; NCIT calls it **Omeprazole**
- `NCIT:C641` (1 mention) - the report calls it "doxycycline"; NCIT calls it **Methimazole**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0005802` (1 mention) - UBERON does not contain this term

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C716` - called "Penicillin", "First-line pharmacotherapy:** **Penicillin"