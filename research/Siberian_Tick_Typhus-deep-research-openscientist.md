---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T05:59:08.767856'
end_time: '2026-09-25T06:12:20.571696'
duration_seconds: 791.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Siberian Tick Typhus
  mondo_id: MONDO:0001154
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
citation_count: 17
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 8
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 29
  verified: 28
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001945
    reported_labels:
    - Symptom
    ontology_label: Fever
  - term_id: HP:0000988
    reported_labels:
    - Physical manifestation
    ontology_label: Skin rash
  - term_id: HP:0002716
    reported_labels:
    - Clinical sign
    ontology_label: Lymphadenopathy
  - term_id: HP:0001873
    reported_labels:
    - Lab abnormality
    ontology_label: Thrombocytopenia
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
  path: Siberian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Siberian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Siberian Tick Typhus
- **MONDO ID:** MONDO:0001154 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Siberian Tick Typhus** covering all of the
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

# Siberian Tick Typhus (North Asian Tick Typhus): A Comprehensive Disease Characterization

**Disease:** Siberian Tick Typhus (North Asian Tick Typhus)
**MONDO ID:** MONDO:0001154
**Category:** Infectious Disease (tick-borne, spotted fever group rickettsiosis)
**Causative agent:** *Rickettsia sibirica* (NCBITaxon:35793), obligate intracellular Gram-negative alphaproteobacterium

---

## Summary

Siberian tick typhus (STT), also called North Asian tick typhus, is an acute, generally mild and self-limited **spotted fever group (SFG) rickettsiosis** caused by the obligate intracellular bacterium *Rickettsia sibirica*. It is transmitted to humans by the bite of ixodid (hard) ticks, principally of the genera *Dermacentor* (notably *D. nuttalli*) and *Haemaphysalis*, across a broad Eurasian endemic zone spanning Siberia, Mongolia, northern China, and Central Asia. The disease is a zoonosis maintained in nature by a tick–small-mammal cycle in which humans are incidental hosts infected during outdoor activity. This report synthesizes nine cited findings and 23 reviewed papers into a complete disease-knowledge-base entry covering etiology, clinical phenotype, pathophysiology, immunity, diagnostics, epidemiology, treatment, prevention, and comparative/zoonotic biology.

Clinically, STT presents with the classic SFG triad of an **inoculation eschar (tache noire)** at the tick-bite site, **fever**, and a **maculopapular rash**, frequently accompanied by regional lymphadenopathy. A distinct subspecies, *R. sibirica* subsp. *mongolitimonae*, causes **lymphangitis-associated rickettsiosis (LAR)**, in which roughly one-third of patients develop a rope-like lymphangitis extending from the eschar to draining lymph nodes. The underlying pathophysiology is a **disseminated small-vessel vasculitis**: bacteria delivered by the tick bite use surface-exposed outer-membrane proteins (OmpA/OmpB of the Sca family, plus Adr1/Adr2) to adhere to and invade **vascular endothelial cells**, producing endothelial injury, procoagulant/platelet activation, and the characteristic rash and eschar. Protective host defense is **cell-mediated**, dominated by IFN-γ-producing NK cells (innate phase) and CD8+ cytotoxic T cells (adaptive phase).

The prognosis is excellent. **Doxycycline** is the first-line curative therapy and produces rapid recovery with very rare sequelae. Diagnosis rests on indirect immunofluorescence assay (IFA) serology and PCR/sequencing of the *ompA* and *gltA* genes, ideally from an eschar biopsy or swab. There is **no licensed vaccine and no genetic component to susceptibility**; prevention is entirely based on **personal anti-tick measures** (repellents, permethrin-treated clothing, tick checks). This is fundamentally an environmentally/exposure-driven infectious disease, and its "risk factors," "inheritance," and "genetic testing" dimensions are therefore largely not applicable in the classical Mendelian sense.

---

## Key Findings

### Finding 1 — Etiology and vector (F001)

Siberian tick typhus is a spotted-fever-group rickettsiosis caused by *Rickettsia sibirica*, an obligate intracellular bacterium transmitted by ixodid ticks of the genus *Dermacentor*. Molecular surveillance in Inner Mongolia, China (2019; 408 ticks screened) detected *R. sibirica* in *Dermacentor nuttalli* ticks, with *gltA* haplotypes (G8/G10) and *ompA* haplotypes (O16/O19) clustering phylogenetically with *R. sibirica* [PMID: 35934699](https://pubmed.ncbi.nlm.nih.gov/35934699/). The comprehensive geographic review by Parola et al. classifies *R. sibirica* among the tick-borne SFG *Rickettsia* zoonoses [PMID: 24092850](https://pubmed.ncbi.nlm.nih.gov/24092850/), which states: *"Tick-borne rickettsioses are caused by obligate intracellular bacteria belonging to the spotted fever group of the genus Rickettsia."* The Inner Mongolia study identifies the principal regional vector: *"The tick species Dermacentor nuttalli is considered the main vector carrying SFGR in Inner Mongolia."*

This establishes the disease as **infectious, not genetic**: the sole necessary cause is inoculation of *R. sibirica* via a tick bite. Ontology anchors: causative organism — *Rickettsia sibirica* (NCBITaxon:35793); vector — *Dermacentor nuttalli*.

### Finding 2 — Clinical triad, LAR subspecies, and benign course (F002)

STT produces the classic SFG clinical triad — **inoculation eschar (tache noire), fever, and maculopapular rash** — often with regional lymphadenopathy following a tick bite. A clinically important variant is caused by *R. sibirica* subsp. *mongolitimonae*, which produces **lymphangitis-associated rickettsiosis (LAR)**. The defining review states: *"This bacterium induces the lymphangitis-associated rickettsiosis, a still unfamiliar rickettsiosis that is mainly characterized by fever with a rope-like lymphangitis and/or lymphadenopathy and skin eschar occurring after tick bites"* and *"Sequellae are very rare and treatment with doxycycline is recommended"* [PMID: 24034636](https://pubmed.ncbi.nlm.nih.gov/24034636/). The frequency of the lymphangitis feature is quantified in a second source: *"Approximately, one-third of the patients with this infection experience lymphangitis from the inoculation eschar to the draining lymph nodes, and, in that case, the infection is named 'lymphangitis-associated rickettsiosis' (LAR)"* [PMID: 33969876](https://pubmed.ncbi.nlm.nih.gov/33969876/).

Suggested HPO phenotype terms: **Fever (HP:0001945)**, **Skin rash (HP:0000988)** / Maculopapular exanthema, **Lymphadenopathy (HP:0002716)**, **Skin ulcer/eschar (HP:0200042)**, **Headache (HP:0002315)**, **Myalgia (HP:0003326)**.

### Finding 3 — Pathophysiology: endothelial infection, vasculitis, and procoagulant activation (F003)

The core pathophysiology of STT, shared across SFG rickettsioses, is a **diffuse vasculitis with endothelial injury**. *R. sibirica* infects **vascular endothelial cells**, producing a disseminated small-vessel vasculitis. Supporting evidence from the closely related SFG agent *R. conorii* (Mediterranean spotted fever, MSF) states: *"The physiopathology of Mediterranean spotted fever includes diffuse vasculitis with endothelial injury"* [PMID: 20797742](https://pubmed.ncbi.nlm.nih.gov/20797742/). In vivo studies of MSF patients demonstrate the downstream procoagulant cascade: *"Our results provide biochemical evidence for the occurrence of TXA2-dependent platelet activation and thrombin generation in vivo, together with endothelial dysfunction"* [PMID: 8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/) — reflecting thromboxane-A2-dependent platelet activation, thrombin generation, and elevated endothelin-1.

Suggested GO terms: **response to bacterium (GO:0009617)**, **inflammatory response (GO:0006954)**, **blood coagulation (GO:0007596)**, **platelet activation (GO:0030168)**. Suggested CL/UBERON terms: **endothelial cell (CL:0000115)**, **blood vessel endothelium (UBERON:0004638)**, **skin (UBERON:0002097)**.

### Finding 4 — Diagnosis by IFA serology and ompA/gltA PCR (F004)

Diagnosis relies on **indirect immunofluorescence assay (IFA)** serology (seroconversion or ≥4-fold titer rise), plus **PCR targeting the ompA and gltA genes with DNA sequencing**, ideally performed on an eschar biopsy or swab. The standard molecular protocol is described as *"a standard PCR reaction using primers suitable for hybridisation within the conserved region of genes coding for outer membrane protein A (ompA) and citrate synthase (gltA) and DNA sequencing were performed"* [PMID: 23168048](https://pubmed.ncbi.nlm.nih.gov/23168048/). Non-invasive eschar sampling is now validated: *"New approaches, such as swabbing of eschars to obtain material to be tested by PCR, have emerged in recent years and have played a role in describing emerging tick-borne rickettsioses"* [PMID: 24092850](https://pubmed.ncbi.nlm.nih.gov/24092850/). In MSF biopsy series, PCR positivity reached 72.6% of samples, and IFA identifies the majority of serologically confirmed cases.

### Finding 5 — Protective immunity is cell-mediated (NK cells + CD8+ T cells + IFN-γ) (F005)

Protective immunity to endothelium-targeting SFG rickettsiae is **cell-mediated**, not primarily antibody-driven. In murine models, resistant animals show higher frequencies of IFN-γ+ CD8+ T cells and cytotoxic NK cells; NK-deficient *Rag−/−γc−/−* mice show impaired clearance, severe hepatic thrombosis, and low serum IFN-γ. Key evidence: *"these findings reveal that NK cells mediate the innate phase of host protection against infection with rickettsiae, most likely via IFN-γ production"* and *"NK cells are involved in preventing rickettsial infection-induced endothelial cell damage"* [PMID: 22617213](https://pubmed.ncbi.nlm.nih.gov/22617213/). For adaptive immunity: *"resistance to rickettsial infections is attributed to the induction of antigen-specific T cells, particularly CD8(+) T cells"* [PMID: 25043277](https://pubmed.ncbi.nlm.nih.gov/25043277/), with the anti-*Rickettsia* CD8+ response peaking around 7 days post-infection and IFN-γ and granzyme B serving as correlates of protection.

Suggested CL terms: **CD8-positive, alpha-beta T cell (CL:0000625)**, **natural killer cell (CL:0000623)**. Suggested GO terms: **interferon-gamma production (GO:0032609)**, **T cell mediated cytotoxicity (GO:0001913)**.

### Finding 6 — Surface proteins mediate endothelial invasion and are protective antigens (F006)

Rickettsial **surface-exposed outer-membrane proteins** — OmpA and OmpB (Sca autotransporter family), plus Adr1, Adr2, OmpW, Porin_4, and TolC — mediate adhesion to and invasion of vascular endothelial cells and are immunoprotective antigens. Proteomic surface labeling of *R. rickettsii* identified these SEPs, and immunization studies showed functional relevance: *"sera from mice immunized with rAdr1, rAdr2, or rOmpW reduced R. rickettsii adherence to and invasion of vascular endothelial cells"* and *"Surface-exposed proteins (SEPs) of R. rickettsii may play important roles in its pathogenesis or immunity"* [PMID: 24950252](https://pubmed.ncbi.nlm.nih.gov/24950252/). These proteins provide the molecular link between the initiating tick inoculation and the endothelial tropism that drives disease, and they are the targets of the *ompA* PCR used diagnostically (Finding 4).

Suggested GO cellular-component terms: **outer membrane (GO:0019867)**, **cell surface (GO:0009986)**. Suggested GO process term: **entry into host cell (GO:0030260)**.

### Finding 7 — Prevention is entirely non-immunological (personal anti-tick measures) (F007)

There is **no licensed vaccine and no recommended routine chemoprophylaxis** for SFG rickettsiosis. Prevention is entirely based on **personal protective measures against tick bites**: DEET/picaridin repellents, permethrin-treated clothing, tick checks, and prompt tick removal. The CDC position: *"Personal protection measures to prevent human tick encounters from resulting in bites are widely recommended as the first line of defense against health impacts associated with ticks"* [PMID: 35364518](https://pubmed.ncbi.nlm.nih.gov/35364518/). Efficacy is quantified: repellent/permethrin formulations showed *"estimated repellencies ranging from 93 to 97%"* in bioassays [PMID: 32073128](https://pubmed.ncbi.nlm.nih.gov/32073128/). Field durability is a caveat — 33% of permethrin-treated forester pants had no measurable permethrin after one year of wear [PMID: 34958094](https://pubmed.ncbi.nlm.nih.gov/34958094/).

Suggested NCIT-style intervention terms: insect repellent use; protective clothing; vector control.

### Finding 8 — Animal reservoirs/sentinels and male-biased human exposure (F008)

Domestic and wild mammals act as **sentinels and amplifying hosts** in the SFG rickettsial cycle, and human seropositivity is **male-associated**, consistent with outdoor exposure rather than any genetic predisposition. Seroprevalence surveys show high SFG rickettsial IgG in animals: 57–59% of dogs and 59% of cats in Tasmania (*"59% of cats and 57% of dogs were positive for antibodies"* [PMID: 20148824](https://pubmed.ncbi.nlm.nih.gov/20148824/)); and 58.5% of dogs, 48.1% of black rats, and 38.3% of humans in a Peruvian rural community. In that community, *"only male gender was statistically associated with having IgG antibodies against Rickettsia spp. (p-value=0.049, chi-square test)"* [PMID: 39799873](https://pubmed.ncbi.nlm.nih.gov/39799873/). The male predominance reflects occupational/recreational outdoor activity and tick exposure, reinforcing the environmental etiology.

### Finding 9 — Doxycycline is curative; excellent prognosis (F009)

**Doxycycline is the first-line curative therapy** for STT and related SFG rickettsioses, producing rapid recovery with very rare sequelae. *"Sequellae are very rare and treatment with doxycycline is recommended"* [PMID: 24034636](https://pubmed.ncbi.nlm.nih.gov/24034636/), and a recent case series confirms *"All patients were treated with doxycycline and recovered without complications"* [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/). The excellent prognosis, combined with the absence of a vaccine and reliance on vector avoidance (Finding 7), completes the management picture. Suggested NCIT term: **Doxycycline (NCIT:C542)**; CHEBI: **doxycycline (CHEBI:50845)**.

---

## Full Disease-Knowledge-Base Entry (15 Sections)

### 1. Disease Information

STT is an acute febrile zoonotic infection of the SFG rickettsioses. **Identifiers:** MONDO:0001154; MeSH "Rickettsiosis, Siberian Tick" / "spotted fever"; ICD-10 A77.2 (Spotted fever due to *Rickettsia sibirica*); ICD-11 1C30.2. It is not an OMIM/Orphanet Mendelian entry (infectious, not genetic). **Synonyms:** North Asian tick typhus, North Asian tick-borne rickettsiosis, Siberian tick-borne typhus, *Rickettsia sibirica* infection. Information is derived from **aggregated disease-level resources** (case series, seroprevalence surveys, molecular surveillance) rather than individual EHR data.

### 2. Etiology

**Causal factor:** infectious — inoculation of *R. sibirica* through the bite of an infected ixodid tick (Finding 1). There are **no genetic risk factors**; susceptibility loci, causal variants, and modifier genes are **not applicable** to this infectious disease. **Environmental/behavioral risk factors:** outdoor occupational or recreational activity in endemic Eurasian foci (Siberia, Mongolia, northern China, Central Asia), spring–summer tick season, contact with tick-infested vegetation or animals; **male sex** is statistically associated with seropositivity as a proxy for exposure (Finding 8). **Protective factors** are behavioral (tick avoidance, repellents, protective clothing — Finding 7), not genetic. **Gene–environment interactions:** not applicable.

### 3. Phenotypes

| Phenotype | Type | HPO term | Frequency / notes |
|---|---|---|---|
| Fever | Symptom | HP:0001945 | Near-universal; acute onset after incubation |
| Inoculation eschar (tache noire) | Clinical sign | HP:0200042 (skin ulcer) | Hallmark at bite site |
| Maculopapular rash | Physical manifestation | HP:0000988 | Common |
| Regional lymphadenopathy | Clinical sign | HP:0002716 | Common, esp. in LAR |
| Lymphangitis (LAR, *mongolitimonae*) | Clinical sign | — | ~1/3 of *mongolitimonae* cases (Finding 2) |
| Headache / myalgia | Symptoms | HP:0002315 / HP:0003326 | Frequent constitutional |
| Thrombocytopenia | Lab abnormality | HP:0001873 | Reported in rickettsial infection |

**Characteristics:** adult-onset (exposure-driven, any age); **acute** onset; severity generally **mild–moderate** and self-limited; **monophasic** course resolving with treatment. **Quality-of-life impact** is transient and low given rapid response to doxycycline and rare sequelae.

### 4. Genetic/Molecular Information

**Not applicable** in the human-host sense — there are no causal human genes, pathogenic variants, modifier genes, epigenetic lesions, or chromosomal abnormalities. The relevant molecular genetics are **pathogen-side**: the *R. sibirica* genes *ompA* (outer membrane protein A) and *gltA* (citrate synthase) are used for molecular typing and phylogeny (Findings 1, 4), and surface-protein genes *ompB*, *adr1*, *adr2*, *ompW* encode virulence/adhesion factors (Finding 6).

### 5. Environmental Information

**Infectious agent:** *Rickettsia sibirica* (including subsp. *sibirica* and subsp. *mongolitimonae*). **Vectors/environment:** ixodid ticks — *Dermacentor nuttalli* (principal), other *Dermacentor* spp., *Haemaphysalis*, and (for *mongolitimonae*) *Hyalomma* and *Rhipicephalus* ticks in the broader region. Transmission occurs in natural steppe/forest-steppe habitats. No toxin, radiation, or pollution etiology.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. An infected ixodid tick bites the human host and **inoculates** *R. sibirica* into the dermis (initiating exposure). → leads to
2. Bacteria use **surface-exposed outer-membrane proteins (OmpA/OmpB, Adr1/Adr2)** to **adhere to and invade vascular endothelial cells** at and beyond the bite site (Finding 6). → results in
3. Intracellular replication and cell-to-cell spread causing **local endothelial injury and the inoculation eschar (tache noire)**; lymphatic spread produces regional lymphadenopathy and, for *mongolitimonae*, **lymphangitis (LAR)** (Finding 2). → leads to
4. Hematogenous dissemination and **disseminated small-vessel vasculitis with endothelial injury** (Finding 3). → results in
5. **Procoagulant activation** — thromboxane-A2-dependent platelet activation, thrombin generation, endothelial dysfunction (↑endothelin-1) — and increased vascular permeability (Finding 3). → produces
6. The clinical manifestations: **maculopapular rash, fever, and (rarely) more severe vascular complications**. Branch: in parallel, the host mounts a protective response —
7. **NK cells (innate) and CD8+ T cells (adaptive), via IFN-γ and granzyme B, clear infected endothelium** and prevent endothelial damage/thrombosis (Finding 5), leading to resolution — accelerated by doxycycline (Finding 9).

Steps 2, 3, 5, and 7 are supported by direct experimental evidence (largely from closely related SFG agents *R. rickettsii* and *R. conorii*, extrapolated to *R. sibirica*, which is noted as an **inference** where species-specific data are lacking). Molecular pathways: bacterial cell entry, host inflammatory response, coagulation cascade. Cell types: endothelial cells (target); NK cells, CD8+ T cells (protection). GO/CL/UBERON terms as listed under Findings 3, 5, 6.

### 7. Anatomical Structures Affected

- **Primary organ/tissue:** vascular endothelium (systemic small vessels) — **UBERON:0004638** (blood vessel endothelium); **skin (UBERON:0002097)** at eschar and rash.
- **Secondary:** lymphatic vessels/nodes (lymphangitis, lymphadenopathy — **UBERON:0000029** lymph node); potential liver/vascular complications in severe disease.
- **Body systems:** cardiovascular (vascular), integumentary, lymphatic/immune.
- **Cell level:** endothelial cell (**CL:0000115**). **Subcellular:** cytoplasm (intracellular replication) — GO cytoplasm (GO:0005737).
- **Lateralization:** eschar typically **unilateral/localized** (single bite site); rash **generalized/bilateral**.

### 8. Temporal Development

**Onset:** acute, after a short incubation following the tick bite; any age (exposure-dependent, adult-predominant). **Course:** monophasic, **self-limited**, resolving over days to weeks; prompt doxycycline shortens course. **Progression:** generally mild and non-progressive; sequelae very rare (Findings 2, 9). **Remission:** treatment-induced (rapid) or spontaneous in mild cases. **Critical period:** early doxycycline initiation optimizes outcome.

### 9. Inheritance and Population

**Epidemiology:** endemic across Siberia, Mongolia, northern China, Kazakhstan, and Central Asia; seasonal (tick-activity months). Animal seroprevalence is high (dogs 57–58.5%, cats 59%, rats 48%), indicating widespread enzootic circulation (Finding 8). **Inheritance:** not applicable (infectious). **Penetrance/expressivity/anticipation/founder effects/consanguinity/carrier frequency:** all not applicable. **Demographics:** **male predominance** in seropositivity (p=0.049), attributable to outdoor exposure (Finding 8); no ethnic genetic predisposition. **Geographic distribution** tracks the range of *Dermacentor*/*Haemaphysalis* vectors and their small-mammal reservoirs.

### 10. Diagnostics

**Serology:** IFA (reference standard) — seroconversion or ≥4-fold titer rise (Finding 4). **Molecular:** PCR of *ompA* and *gltA* with sequencing, from **eschar biopsy or swab** (non-invasive), or from blood/rash biopsy (Finding 4). **Supportive labs:** thrombocytopenia may be present. **Clinical criteria:** compatible triad (eschar + fever + rash) plus endemic tick exposure. **Differential diagnosis:** other SFG rickettsioses (MSF/*R. conorii*, *R. slovaca* TIBOLA/SENLAT, *R. raoultii*, *R. aeschlimannii*), tularemia, Lyme borreliosis, typhus group, and other eschar-forming tick-borne illnesses. **Genetic/omics/newborn screening:** not applicable.

### 11. Outcome/Prognosis

**Excellent.** With doxycycline, recovery is rapid and complete; *"All patients... recovered without complications"* [PMID: 40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/). **Mortality** is very low for *R. sibirica* (in contrast to more virulent SFG agents such as *R. rickettsii*). **Sequelae are very rare** [PMID: 24034636](https://pubmed.ncbi.nlm.nih.gov/24034636/). **Complications** (severe vasculitis, thrombosis) are uncommon and associated with delayed treatment. **Prognostic factors:** timeliness of doxycycline, host immune competence (NK/CD8+ IFN-γ response — Finding 5), and comorbidity.

### 12. Treatment

**First-line:** **Doxycycline** (tetracycline-class; inhibits bacterial protein synthesis) — curative, rapid response (Finding 9). **Alternatives** for SFG rickettsioses include other tetracyclines and, in specific circumstances, chloramphenicol or fluoroquinolones/macrolides (agent- and patient-dependent). **No advanced therapeutics** (gene, cell, RNA, targeted, or immunotherapy) are relevant. **Supportive care** for fever/pain as needed. **Pharmacogenomics:** not applicable. NCIT/CHEBI: Doxycycline (NCIT:C542; CHEBI:50845).

### 13. Prevention

**Entirely non-immunological** (Finding 7). **Primary prevention:** personal anti-tick measures — DEET/picaridin repellents, permethrin-treated clothing (93–97% repellency), tick checks, prompt tick removal; environmental/vector control in high-risk settings. **Secondary/tertiary:** early recognition and doxycycline. **Immunization:** no licensed vaccine. **Prophylaxis:** routine post-bite antibiotics **not** recommended. **Public health:** health education for outdoor workers/travelers in endemic zones; note permethrin durability declines over ~1 year of wear (Finding 7 caveat).

### 14. Other Species / Natural Disease

**Taxonomy of hosts/reservoirs:** small mammals (rodents), dogs (*Canis lupus familiaris*, NCBITaxon:9615), cats (*Felis catus*, NCBITaxon:9685), and rats serve as reservoirs/sentinels with high seroprevalence (Finding 8). **Vector:** *Dermacentor nuttalli* and related ixodids. **Zoonotic potential:** STT is a **zoonosis** maintained in a tick–mammal cycle; humans are incidental hosts. Domestic animals are largely asymptomatic amplifying/sentinel hosts. Comparative pathology: the endothelial-tropism mechanism is conserved across SFG *Rickettsia* species and their mammalian hosts.

### 15. Model Organisms

**Mouse models** are the principal experimental system for SFG rickettsial immunity and pathogenesis: resistant/susceptible mouse strains, *Rag−/−γc−/−* NK-deficient mice, and challenge/immunization studies define the NK/CD8+/IFN-γ correlates of protection (Findings 5, 6). **In vitro:** vascular endothelial cell infection assays model adhesion/invasion (Finding 6). Most mechanistic data derive from *R. rickettsii*/*R. conorii* models and are **extrapolated** to *R. sibirica*; species-specific *R. sibirica* models are a knowledge gap. Cattle *Cowdria (Ehrlichia) ruminantium* work [PMID: 9573061](https://pubmed.ncbi.nlm.nih.gov/9573061/) provides comparative evidence that infected endothelial cells present antigen to protective T cells.

---

## Mechanistic Model / Interpretation

```
 TICK BITE (Dermacentor nuttalli inoculates R. sibirica)
              │
              ▼
 [Surface proteins OmpA/OmpB, Adr1/Adr2]  ── adhere & invade ──►  VASCULAR ENDOTHELIAL CELLS
              │                                                          │
              ▼                                                          ▼
   Local injury → ESCHAR (tache noire)                     Hematogenous dissemination
   Lymphatic spread → lymphadenopathy / LAR (mongolitimonae)            │
                                                                        ▼
                                            DISSEMINATED SMALL-VESSEL VASCULITIS
                                                                        │
                                    ┌───────────────────────────────────┤
                                    ▼                                   ▼
                    Procoagulant activation                     Increased vascular
                    (TXA2 → platelets, thrombin,                permeability
                     ↑endothelin-1)                                     │
                                    └───────────────┬───────────────────┘
                                                    ▼
                                    FEVER + MACULOPAPULAR RASH
                                                    │
        ┌───────────────────────────────────────────┘
        ▼ (host defense branch)
 NK cells (innate) + CD8+ T cells (adaptive) ── IFN-γ, granzyme B ──► clear infected endothelium
        │
        ▼
 RESOLUTION  ◄──── accelerated by DOXYCYCLINE ────►  EXCELLENT PROGNOSIS, rare sequelae
```

The disease is best understood as a **linear infectious cascade** with a protective immune branch. The single initiating lesion (tick inoculation) is amplified through endothelial tropism into a systemic vasculitis; the same surface proteins that drive invasion are the antigens recognized by protective cellular immunity and the genetic targets of molecular diagnostics. Because there is no host genetic component, the disease's "risk," "protection," and "prevention" all operate at the level of **exposure** — explaining the male, outdoor-associated epidemiology and the vector-avoidance basis of prevention.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Evidence type |
|---|---|---|---|
| [35934699](https://pubmed.ncbi.nlm.nih.gov/35934699/) | *Rickettsia* in *D. nuttalli*, Inner Mongolia | F001 vector & agent | Molecular surveillance |
| [24092850](https://pubmed.ncbi.nlm.nih.gov/24092850/) | Tick-borne rickettsioses worldwide | F001 taxonomy, F004 eschar swab | Review |
| [24034636](https://pubmed.ncbi.nlm.nih.gov/24034636/) | LAR by *R. sibirica mongolitimonae* | F002 clinic, F009 doxycycline | Clinical review |
| [33969876](https://pubmed.ncbi.nlm.nih.gov/33969876/) | LAR by *R. sibirica mongolitimonae* | F002 ~1/3 lymphangitis | Clinical review |
| [20797742](https://pubmed.ncbi.nlm.nih.gov/20797742/) | *R. conorii* meningoencephalitis | F003 vasculitis | Clinical/mechanistic |
| [8584998](https://pubmed.ncbi.nlm.nih.gov/8584998/) | *R. conorii* coagulation activation | F003 procoagulant | Human in vivo |
| [23168048](https://pubmed.ncbi.nlm.nih.gov/23168048/) | MSF in Trakya, Turkey | F004 ompA/gltA PCR | Clinical series |
| [22617213](https://pubmed.ncbi.nlm.nih.gov/22617213/) | NK cells vs. rickettsiae | F005 innate immunity | Mouse model |
| [25043277](https://pubmed.ncbi.nlm.nih.gov/25043277/) | Anti-*Rickettsia* CD8+ response | F005 adaptive immunity | Mouse model |
| [24950252](https://pubmed.ncbi.nlm.nih.gov/24950252/) | *R. rickettsii* surface proteins | F006 invasion/antigens | Proteomics + immunization |
| [35364518](https://pubmed.ncbi.nlm.nih.gov/35364518/) | Personal protection vs. ticks | F007 prevention | Review/guidance |
| [32073128](https://pubmed.ncbi.nlm.nih.gov/32073128/) | Repellent efficacy vs. ticks | F007 93–97% repellency | Bioassay |
| [34958094](https://pubmed.ncbi.nlm.nih.gov/34958094/) | Permethrin uniform durability | F007 durability caveat | Field study |
| [39799873](https://pubmed.ncbi.nlm.nih.gov/39799873/) | SFG rickettsiae, Peru | F008 male exposure | Seroprevalence |
| [20148824](https://pubmed.ncbi.nlm.nih.gov/20148824/) | SFG in cats/dogs, Tasmania | F008 animal sentinels | Seroprevalence |
| [40608626](https://pubmed.ncbi.nlm.nih.gov/40608626/) | Rickettsiosis case series, Turkey | F009 doxycycline outcome | Clinical series |
| [26384814](https://pubmed.ncbi.nlm.nih.gov/26384814/) | Rickettsioses in Europe | Context: LAR classification | Review |
| [9573061](https://pubmed.ncbi.nlm.nih.gov/9573061/) | *Cowdria* T-cell immunity | Comparative endothelial immunity | Cattle model |

**Key strength:** the mechanistic and immunological findings are internally consistent and cross-supported by multiple SFG species. **Key caveat:** much of the mechanistic/immunological detail derives from *R. rickettsii* and *R. conorii* rather than *R. sibirica* directly, and is applied by inference within the SFG.

---

## Limitations and Knowledge Gaps

1. **Species-specific data scarcity.** Most pathophysiology (Findings 3, 5, 6) comes from *R. conorii* and *R. rickettsii*. *R. sibirica*-specific endothelial-invasion, immune-correlate, and virulence studies are limited; extrapolation within the SFG is reasonable but not proven for STT.
2. **Epidemiology from proxies.** The male-predominance and seroprevalence findings (F008) derive from non-endemic comparators (Peru, Tasmania) rather than core Eurasian STT foci; precise STT incidence/prevalence per 100,000 in Siberia/Mongolia/China was not quantified here.
3. **No quantitative severity/QoL data.** Phenotype frequencies are qualitative or drawn from related agents; formal QoL instruments have not been applied to STT.
4. **Diagnostic performance figures** (e.g., 72.6% PCR positivity) come from MSF series, not STT-specific cohorts.
5. **No host-genetics dimension** exists for this infectious disease, so Sections 4 and much of 9 are "not applicable" by nature rather than by data gap.
6. **Vaccine/therapeutic pipeline** for SFG rickettsioses remains preclinical; the protective-antigen work (F006) is promising but not yet translated.

---

## Proposed Follow-up Actions

1. **Quantify STT-specific epidemiology** by mining Russian/Chinese/Mongolian surveillance and registry literature for incidence, seasonality, and age/sex distribution in core endemic foci.
2. **Confirm *R. sibirica*-specific mechanisms**: seek in vitro endothelial-invasion and murine immunity studies using *R. sibirica* itself to validate the extrapolated OmpA/OmpB/Adr and NK/CD8+/IFN-γ findings.
3. **Compile a differential-diagnosis matrix** distinguishing STT from co-circulating eschar-forming rickettsioses (*R. slovaca*, *R. raoultii*, *R. aeschlimannii*, *R. conorii*) by vector, geography, eschar location, and lymphadenopathy pattern.
4. **Assess subspecies delineation**: further characterize *R. sibirica* subsp. *mongolitimonae* (LAR) vs. subsp. *sibirica* clinical and molecular distinctions.
5. **Evaluate protective-antigen vaccine candidates** (Adr1/Adr2/OmpW) for cross-protection across SFG species, given the shared endothelial mechanism.
6. **Ontology curation**: finalize HPO/GO/CL/UBERON/NCIT/CHEBI mappings proposed above for knowledge-base ingestion.

---

*Report compiled from 5 investigation iterations, 9 confirmed cited findings, and 23 reviewed papers. Evidence types span human clinical series, mouse and cattle models, in vitro assays, molecular surveillance, and seroprevalence surveys. Where R. sibirica-specific data were unavailable, findings from closely related spotted fever group Rickettsia are applied by explicit inference.*


## Artifacts

- [OpenScientist final report](Siberian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Siberian_Tick_Typhus-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001945` (2 mentions) - the report calls it "Symptom"; HP calls it **Fever**
- `HP:0000988` (2 mentions) - the report calls it "Physical manifestation"; HP calls it **Skin rash**
- `HP:0002716` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Lymphadenopathy**
- `HP:0001873` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Thrombocytopenia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0030260` (GO_0030260) (1 mention) - replaced by `GO:0044409`