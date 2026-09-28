---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T00:54:17.305540'
end_time: '2026-09-25T01:12:31.474327'
duration_seconds: 1094.17
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Typhoid Fever
  mondo_id: MONDO:0005619
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
citation_count: 52
reference_validation:
  total_references: 52
  verified: 52
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 52
  on_topic: 44
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 35
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 16
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0002027
    reported_labels:
    - Symptom
    ontology_label: Abdominal pain
  - term_id: HP:0002039
    reported_labels:
    - Symptom
    ontology_label: Anorexia
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0002014
    reported_labels:
    - Symptom
    ontology_label: Diarrhea
  - term_id: HP:0002019
    reported_labels:
    - Symptom
    ontology_label: Constipation
  - term_id: HP:0002240
    reported_labels:
    - Clinical sign
    ontology_label: Hepatomegaly
  - term_id: HP:0001744
    reported_labels:
    - Clinical sign
    ontology_label: Splenomegaly
  - term_id: HP:0011276
    reported_labels:
    - Abnormality of skin morphology
    ontology_label: Vascular skin abnormality
  - term_id: CL:0002270
    reported_labels:
    - M cell / microfold cell
    - M cells
    - Tissue/cell level:** intestinal epithelium and **M cells
    ontology_label: type EC2 enteroendocrine cell
  - term_id: UBERON:0002110
    reported_labels:
    - carrier niche
    ontology_label: gallbladder
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Typhoid_Fever-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Typhoid_Fever-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Typhoid Fever
- **MONDO ID:** MONDO:0005619 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Typhoid Fever** covering all of the
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

# Typhoid Fever (MONDO:0005619): Comprehensive Disease Characteristics Report

## Summary

Typhoid fever is a systemic, potentially life-threatening febrile illness caused by the **human-restricted** bacterium *Salmonella enterica* subspecies *enterica* serovar Typhi (*S.* Typhi). It is transmitted by the fecal–oral route through water and food contaminated by the excreta of acutely infected patients or, critically, of chronic gallbladder carriers who constitute a persistent human reservoir. Unlike the classical templates for Mendelian disorders, typhoid is an **infectious disease with no causal human gene**; host genetics act only as susceptibility modifiers. The Global Burden of Disease Study 2017 estimated **14.3 million (95% UI 12.5–16.3) cases** of typhoid and paratyphoid fevers in 2017 — a 44.6% decline from 1990 — with *S.* Typhi responsible for 76.3% of enteric-fever cases and a global case fatality of 0.95%. Burden is overwhelmingly concentrated in low- and middle-income countries (LMICs) of South Asia and sub-Saharan Africa, and incidence is highest in children under 15 years.

Mechanistically, the disease runs a well-characterized causal chain: ingested bacteria invade the small-intestinal epithelium and Peyer's-patch M cells via the SPI-1 type III secretion system, survive and replicate inside macrophages via the SPI-2 secretion system and the **Vi capsular polysaccharide** (which disturbs host autophagy and evades immune recognition), disseminate through the reticuloendothelial system (liver, spleen, bone marrow, gallbladder), and produce sustained bacteremia and a hyperinflammatory, endotoxin-driven fever. *S.* Typhi uniquely encodes a tripartite **"typhoid toxin" (CdtB + PltA + PltB)** that adds genotoxic and systemic effects. The most lethal complication is **ileal (intestinal) perforation** in weeks 2–3, carrying a pooled case-fatality of 15.4% among hospitalized cases.

Diagnosis still relies on blood culture (imperfect sensitivity), with rapid serologic tests offering only moderate accuracy. Treatment is increasingly constrained by **multidrug-resistant (MDR)** and **extensively drug-resistant (XDR)** strains — leaving azithromycin and carbapenems (meropenem) as the mainstays — while **typhoid conjugate vaccines (Vi-TT)** deliver ~80% efficacy with durable multi-year protection, and improved **water, sanitation and hygiene (WASH)** remains the foundational preventive intervention. Chronic gallbladder carriage (2–5% of infections) not only sustains transmission but is quantitatively linked to gallbladder carcinoma (pooled OR ≈ 4.3).

---

## 1. Disease Information

**Overview.** Typhoid fever (enteric fever) is a systemic bacterial infection characterized by prolonged fever, bacteremia, and involvement of the reticuloendothelial system. It is caused by *Salmonella enterica* serovar Typhi, a Gram-negative, flagellated, facultatively intracellular bacillus that infects only humans. The closely related serovars Paratyphi A, B, and C cause a clinically similar but generally milder "paratyphoid fever"; together they constitute "enteric fever."

**Key identifiers.**
- **MONDO:** MONDO:0005619 (typhoid fever)
- **ICD-10:** A01.0 (Typhoid fever); **ICD-11:** 1A07 (Typhoid fever)
- **MeSH:** D014435 (Typhoid Fever)
- **SNOMED CT:** 4834000 (Typhoid fever)
- **NCBI Taxonomy (pathogen):** *Salmonella enterica* subsp. *enterica* serovar Typhi — txid90370
- **OMIM/Orphanet:** Not a Mendelian disease; no OMIM disease entry. Host **susceptibility loci** have been mapped (see Section 4).

**Synonyms / alternative names.** Enteric fever (when grouped with paratyphoid), typhoid, "slow fever," historically "gastric fever" and "nervous fever."

**Data provenance.** The information in this report is derived almost entirely from **aggregated disease-level resources** — systematic reviews, meta-analyses, randomized controlled trials, GBD modeling, and controlled human infection (challenge) studies — rather than from individual EHR records.

---

## 2. Etiology

**Primary cause (infectious).** The sole causal agent is *S.* Typhi (**Finding F001**). Transmission is fecal–oral via contaminated water and food. The human-restricted nature of the pathogen means the reservoir is entirely human — acute cases and chronic carriers.

**Environmental / behavioral risk factors.** Inadequate **water, sanitation and hygiene (WASH)** is the dominant modifiable driver. A meta-analysis of 27 case-control studies quantified **limited hygiene (OR 2.26, 95% CrI 1.38–3.64)** and **untreated drinking water (OR 1.96)** as risk factors ([PMID: 37644449](https://pubmed.ncbi.nlm.nih.gov/37644449/); **Finding F011**). Field studies add contaminated drinking water, poor sanitation, and **street-food consumption** as severity-associated exposures ([PMID: 42602150](https://pubmed.ncbi.nlm.nih.gov/42602150/)). In Nairobi informal settlements, use of a **shared flush toilet** was independently associated with infection (aOR 2.42, 95% CI 1.69–3.47), as was age 5–16 years ([PMID: 42778887](https://pubmed.ncbi.nlm.nih.gov/42778887/)). Additional host/behavioral factors include young age (school-age children), living in endemic/crowded urban slums, and — for the carrier state — gallstones, biliary abnormalities, and a cholesterol-rich diet.

**Genetic risk factors (host).** Typhoid is not a genetic disease, but host genetic susceptibility has been demonstrated. A controlled human challenge study genotyped volunteers and identified variants associated with enteric-fever susceptibility ([PMID: 35254093](https://pubmed.ncbi.nlm.nih.gov/35254093/); **Finding F007**). Classical literature also implicates *HLA* class II alleles, *TLR* pathway variants, and the *CFTR* locus, though these are modifiers of modest effect rather than causal variants.

**Protective factors.** Vaccination (typhoid conjugate vaccine — Section 13) and improved household WASH are the principal protective factors; a Dhaka slum cohort (n = 98,087) found improved household WASH associated with a **38% reduction** in typhoid risk (adjusted HR 0.62, 95% CI 0.49–0.78) ([PMID: 37983081](https://pubmed.ncbi.nlm.nih.gov/37983081/); **Finding F011**). Pre-existing immunity from prior exposure also protects.

**Gene–environment interaction.** The dominant interaction is between environmental exposure dose (WASH-mediated) and host immune competence; a persistent post-infection "convalescent" transcriptional signature may mark hosts genetically or temporarily unable to mount effective immunity, predisposing to relapse or the carrier state ([PMID: 20018727](https://pubmed.ncbi.nlm.nih.gov/20018727/); **Finding F007**).

---

## 3. Phenotypes

Typhoid presents with an **insidious onset** of sustained fever over the first week, progressing over 2–3 weeks if untreated. In a retrospective series of 305 confirmed cases, **fever was universal (100%)**, followed by abdominal pain (62.0%), loss of appetite (43.3%), headache (40.3%), diarrhea (34.8%), and constipation (24.3%); hepatomegaly (30.1%) and splenomegaly (22.3%) were common ([PMID: 41246786](https://pubmed.ncbi.nlm.nih.gov/41246786/)).

| Phenotype | Type | HPO term | Approx. frequency | Notes |
|---|---|---|---|---|
| Prolonged / stepwise fever | Symptom | HP:0001945 (Fever) | ~100% | Hallmark; rises over week 1 |
| Abdominal pain | Symptom | HP:0002027 | ~62% | Diffuse, RLQ tenderness |
| Anorexia / loss of appetite | Symptom | HP:0002039 | ~43% | Common |
| Headache | Symptom | HP:0002315 | ~40% | Early |
| Diarrhea | Symptom | HP:0002014 | ~35% | More common in children |
| Constipation | Symptom | HP:0002019 | ~24% | Classic in adults |
| Hepatomegaly | Clinical sign | HP:0002240 | ~30% | Reticuloendothelial involvement |
| Splenomegaly | Clinical sign | HP:0001744 | ~22% | Reticuloendothelial involvement |
| Relative bradycardia (Faget sign) | Clinical sign | HP:0001662 (Bradycardia) | Variable | Classic but inconsistent |
| Rose spots (blanching macules) | Physical manifestation | HP:0011276 (Abnormality of skin morphology) | Variable | Trunk, ~week 2 |
| Eosinopenia / leukopenia | Laboratory abnormality | HP:0001882 (Leukopenia) | Common | Supportive lab clue |
| Encephalopathy / "typhoid state" | Behavioral/neuro | HP:0001298 (Encephalopathy) | Severe cases | Delirium, apathy |
| Intestinal perforation | Physical manifestation | HP:0031368 (Intestinal perforation) | severe/late | Week 2–3, lethal |

**Onset:** subacute/insidious (days). **Severity:** variable — from mild self-limited febrile illness to fulminant disease with perforation, shock, and death. **Progression:** progressive over weeks if untreated, then resolving (with treatment) or complicated. **Quality-of-life impact:** substantial acute morbidity (mean hospital stay for perforation 18.4 days; **Finding F006**) and major economic burden — in hospitalized Kenyan children, median societal cost per admission US$96.95, with up to ~24–27% of poorest households facing catastrophic health expenditure ([PMID: 42580776](https://pubmed.ncbi.nlm.nih.gov/42580776/)).

---

## 4. Genetic/Molecular Information

**Causal human genes:** None. Typhoid is an infectious disease; there is no causal germline mutation.

**Host susceptibility loci:** Controlled human infection modeling has identified genetic variants associated with enteric-fever susceptibility ([PMID: 35254093](https://pubmed.ncbi.nlm.nih.gov/35254093/)). Candidate genes in the broader literature include *HLA-DRB1/DQB1*, *TLR4/TLR5*, *SLC11A1* (NRAMP1), and *CFTR* (the CFTR protein has been proposed as an intestinal entry receptor for *S.* Typhi). These are **modifier/susceptibility** loci, not Mendelian causes.

**Pathogen genetic determinants (the relevant "molecular" biology).** Virulence is encoded on *Salmonella* pathogenicity islands (SPIs) and the *viaB* locus:
- **SPI-1** — invasion-associated type III secretion system (T3SS-1).
- **SPI-2** — intracellular survival T3SS-2.
- **SPI-7 / *viaB* locus** — encodes the **Vi capsular polysaccharide** (tviA–E, vexA–E).
- **Typhoid toxin operon** — *cdtB*, *pltA*, *pltB* (**Finding F002**).

**Antimicrobial-resistance genetics (the clinically decisive molecular story).** Resistance is driven by **plasmid acquisition and clonal spread of the H58 lineage**. Emerging cephalosporin resistance in India results from *bla* (e.g., *bla*CTX-M-15) acquisition via plasmids from other bacteria ([PMID: 40208005](https://pubmed.ncbi.nlm.nih.gov/40208005/); **Finding F005**). Fluoroquinolone resistance arises from *gyrA*/*parC* QRDR mutations. XDR strains combine resistance to first-line drugs, fluoroquinolones, and third-generation cephalosporins ([PMID: 41550837](https://pubmed.ncbi.nlm.nih.gov/41550837/)).

**Epigenetic / chromosomal abnormalities:** Not applicable to the human host in the Mendelian sense. (Bacterial DNA methylation regulates virulence gene expression but is outside the human-disease-gene framework.)

---

## 5. Environmental Information

**Environmental factors.** Contaminated water supplies and inadequate sewage/sanitation infrastructure are the principal environmental determinants; fecal contamination of drinking water is the classic transmission route. Wastewater surveillance detects *S.* Typhi in the community and correlates with clinical incidence — each 10-fold increase in typhoid incidence gave 2.43× higher odds of *S.* Typhi wastewater detection ([PMID: 42419341](https://pubmed.ncbi.nlm.nih.gov/42419341/)).

**Lifestyle factors.** Street-food consumption, unsafe water handling and storage, and shared sanitation facilities increase risk ([PMID: 42602150](https://pubmed.ncbi.nlm.nih.gov/42602150/); [PMID: 42778887](https://pubmed.ncbi.nlm.nih.gov/42778887/)). A cholesterol-rich diet favors gallbladder carriage ([PMID: 39636114](https://pubmed.ncbi.nlm.nih.gov/39636114/)).

**Infectious agent.** *Salmonella enterica* subsp. *enterica* serovar Typhi (NCBI Taxon 90370) — the necessary and sufficient cause. CHEBI-relevant chemical entities: lipopolysaccharide/endotoxin (CHEBI:16412), cholesterol (CHEBI:16113).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion** of *S.* Typhi in fecally contaminated water/food → bacteria survive gastric acid and reach the small intestine. *(demonstrated)*
2. **SPI-1 T3SS-1–mediated invasion** of intestinal epithelium and **Peyer's-patch M cells** in the terminal ileum → bacterial translocation across the mucosa. *(demonstrated)*
3. **Uptake by macrophages/dendritic cells**; *S.* Typhi resides in the **Salmonella-containing vacuole (SCV)** and uses **SPI-2 T3SS-2** and the **Vi capsule** to survive intracellularly. The Vi capsule **decreases macrophage autophagy** by down-regulating Nod2 and Galectin-8 (↑LC3-II, ↓p62 in Vi mutants) → enhanced intracellular survival ([PMID: 39732413](https://pubmed.ncbi.nlm.nih.gov/39732413/); **Finding F010**). *(demonstrated)*
4. **Immune evasion / modulation:** Vi paradoxically binds the human C-type lectin **DC-SIGN** to modulate phagocytosis ([PMID: 36286551](https://pubmed.ncbi.nlm.nih.gov/36286551/)); relative to *S.* Typhimurium, *S.* Typhi induces **greater SPI-1–dependent inflammasome activation** (caspase-1, IL-1β, pyroptosis) in monocyte-derived macrophages → hyperinflammatory bacteremic state ([PMID: 32387390](https://pubmed.ncbi.nlm.nih.gov/32387390/); **Finding F010**). *(demonstrated in vitro)*
5. **Reticuloendothelial dissemination:** infected macrophages carry bacteria to mesenteric lymph nodes, then via lymphatics/blood to **liver, spleen, bone marrow, and gallbladder** → primary/secondary bacteremia. *(inferred from classical pathology + demonstrated tropism)*
6. **Sustained bacteremia + endotoxin (LPS)–driven cytokine response** → prolonged stepwise fever, and a reproducible **peripheral-blood transcriptional signature** during acute disease ([PMID: 20018727](https://pubmed.ncbi.nlm.nih.gov/20018727/); **Finding F007**). *(demonstrated)*
7. **Typhoid toxin action:** *S.* Typhi expresses CdtB within the SCV, secreted in outer-membrane vesicles; PltA/PltB deliver the genotoxic **CdtB** to target cells via retrograde Golgi transport → DNA damage, cell-cycle arrest, and contribution to systemic symptoms ([PMID: 18191792](https://pubmed.ncbi.nlm.nih.gov/18191792/), [PMID: 23869968](https://pubmed.ncbi.nlm.nih.gov/23869968/); **Finding F002**). *(demonstrated in vitro/in vivo)*

**Branch A — acute severe disease:** Hyperplasia and necrosis of Peyer's-patch lymphoid tissue in the terminal ileum → mucosal ulceration → **ileal perforation (weeks 2–3)** → peritonitis, sepsis, death (pooled CFR 15.4%; **Finding F006**).

**Branch B — chronic carriage:** Gallbladder colonization, favored by **gallstones and cholesterol-rich diet**, with **CsgD-regulated curli/cellulose biofilm** formation → asymptomatic intermittent shedding (2–5% of infections), antibiotic tolerance, transmission, and long-term **gallbladder carcinoma** risk ([PMID: 41335321](https://pubmed.ncbi.nlm.nih.gov/41335321/), [PMID: 39720794](https://pubmed.ncbi.nlm.nih.gov/39720794/), [PMID: 24612190](https://pubmed.ncbi.nlm.nih.gov/24612190/); **Findings F003, F008**).

### Mechanism map (ASCII)

```
 Ingestion (fecal-oral)
        │
        ▼
 Ileal epithelium / M cells ──SPI-1 T3SS-1──► invasion
        │
        ▼
 Macrophage SCV ──SPI-2 + Vi capsule──► intracellular survival
        │        (↓autophagy via Nod2/Galectin-8; DC-SIGN binding)
        ▼
 Reticuloendothelial spread (liver, spleen, marrow, gallbladder)
        │
        ├──► Sustained bacteremia + LPS ──► fever, blood transcriptional signature
        │
        ├──► Typhoid toxin (CdtB/PltA/PltB) ──► genotoxicity, systemic effects
        │
        ├── BRANCH A ──► Peyer's-patch necrosis ──► ILEAL PERFORATION (wk 2-3) ──► death
        │
        └── BRANCH B ──► gallbladder biofilm on gallstones ──► CHRONIC CARRIAGE ──► gallbladder cancer
```

**Ontology suggestions.** GO biological processes: GO:0009405 (pathogenesis), GO:0052167 (modulation of host immune response), GO:0006909 (phagocytosis), GO:0016236 (macroautophagy), GO:0002526 (acute inflammatory response). Cell types (CL): CL:0000235 (macrophage), CL:0000451 (dendritic cell), CL:0000236 (B cell), CL:0000084 (T cell), CL:0002270 (M cell / microfold cell). Subcellular (GO CC): GO:0005764 (lysosome), GO:0005794 (Golgi). Chemical entities (CHEBI): CHEBI:16412 (LPS), CHEBI:16113 (cholesterol).

---

## 7. Anatomical Structures Affected

- **Primary organs:** terminal **ileum / small intestine** (UBERON:0002116; Peyer's patches UBERON:0011156), **mesenteric lymph nodes** (UBERON:0002509).
- **Reticuloendothelial system:** **liver** (UBERON:0002107; hepatomegaly ~30%), **spleen** (UBERON:0002106; splenomegaly ~22%), **bone marrow** (UBERON:0002371), **gallbladder** (UBERON:0002110 — carrier niche).
- **Secondary/complication sites:** **peritoneum** (perforation → peritonitis), **CNS** (typhoid encephalopathy), skin (rose spots), and — in chronic carriers — gallbladder neoplasia.
- **Body systems:** digestive, lymphatic/reticuloendothelial, hematopoietic, and (severe cases) nervous and cardiovascular systems.
- **Tissue/cell level:** intestinal epithelium and **M cells** (CL:0002270); **macrophages** (CL:0000235) as the primary intracellular niche and key determinant of disease progression ([PMID: 40095029](https://pubmed.ncbi.nlm.nih.gov/40095029/)); lymphocytes (T and B cells) recruited to the gallbladder in carriage (mouse model, [PMID: 31575775](https://pubmed.ncbi.nlm.nih.gov/31575775/)).
- **Subcellular:** the **Salmonella-containing vacuole**, lysosome, and Golgi (typhoid-toxin retrograde transport).
- **Lateralization:** not applicable (systemic disease); ileal lesions are segmental, antimesenteric.

---

## 8. Temporal Development

- **Onset:** insidious/subacute; incubation typically **6–30 days** (usually ~1–2 weeks), dose-dependent.
- **Classic weekly progression (untreated):**
  - Week 1 — rising stepwise fever, headache, malaise, relative bradycardia.
  - Week 2 — sustained high fever, abdominal pain, rose spots, hepatosplenomegaly, "typhoid state" (apathy/delirium).
  - Week 3 — risk of **ileal perforation and intestinal hemorrhage**, peritonitis, shock. Perforation cases nearly all present in the second week of infection ([PMID: 34652510](https://pubmed.ncbi.nlm.nih.gov/34652510/)).
  - Week 4+ — gradual resolution if survived.
- **Duration:** typically **self-limited to weeks** with treatment; relapse in ~5–10% after apparent recovery. **Chronic carriage** (>12 months of shedding) develops in **2–5%** — a lifelong reservoir state (**Finding F003**).
- **Critical intervention window:** early antimicrobial therapy (first week) prevents most complications; the peri-perforation window (week 2–3) is the critical period for surgical intervention.

---

## 9. Inheritance and Population

**Inheritance:** Not applicable (infectious, non-heritable). Host susceptibility is **multifactorial/polygenic** with modest-effect loci.

**Epidemiology (Findings F001, F009).**

| Metric | Estimate | Source |
|---|---|---|
| Global cases (enteric fever), 2017 | 14.3 million (95% UI 12.5–16.3) | [PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/) |
| Trend 1990→2017 | 44.6% decline from 25.9 million | [PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/) |
| Age-standardized incidence, 2017 | 197.8 / 100,000 person-years (↓54.9%) | [PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/) |
| *S.* Typhi share of enteric fever | 76.3% (71.8–80.5) | [PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/) |
| Global case fatality, 2017 | 0.95% (0.54–1.53) | [PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/) |
| WHO EMR annual cases | 5.57–9.23 million; 46,200–163,000 deaths | [PMID: 42413480](https://pubmed.ncbi.nlm.nih.gov/42413480/) |
| Sentinel-site median incidence | 140 / 100,000 person-years | [PMID: 42142522](https://pubmed.ncbi.nlm.nih.gov/42142522/) |

**Geographic distribution:** endemic across **South Asia** (India, Pakistan, Bangladesh, Nepal), **sub-Saharan Africa**, and Southeast Asia; sporadic/travel-associated in high-income countries. Typhoid shows strong **spatial-temporal clustering** — incidence-rate ratio **4.9** in the innermost ring around index cases within 28 days, supporting targeted "ring" vaccination ([PMID: 38913735](https://pubmed.ncbi.nlm.nih.gov/38913735/); **Finding F011**).

**Age/sex:** Incidence highest in **children <15 years** (school-age); a slight male predominance is often reported (e.g., male-to-female ~1.4:1 in a Lahore cohort, [PMID: 41246786](https://pubmed.ncbi.nlm.nih.gov/41246786/)). **Chronic carriage** is more common in older adults, women, and those with gallstones.

---

## 10. Diagnostics

**Reference standard:** **Blood culture** (and, more sensitively, bone marrow culture). Blood culture positivity is imperfect (e.g., 61–78% in various cohorts: [PMID: 31884434](https://pubmed.ncbi.nlm.nih.gov/31884434/), [PMID: 41246786](https://pubmed.ncbi.nlm.nih.gov/41246786/)), reduced further by prior antibiotics.

**Laboratory clues:** leukopenia, eosinopenia, anemia; elevated liver transaminases. Anemia is prominent in perforation cases (62.5% in a Burkina Faso series, [PMID: 28406420](https://pubmed.ncbi.nlm.nih.gov/28406420/)).

**Rapid diagnostic tests (RDTs) / serology (moderate accuracy):** A Cochrane review of 37 studies (5,080 participants) found **TUBEX** sensitivity 78% / specificity 87%; **Typhidot** sensitivity ~78–84% / specificity ~77–79%; **Test-It Typhoid (KIT)** sensitivity 69% / specificity 90% — all only moderately accurate ([PMID: 28545155](https://pubmed.ncbi.nlm.nih.gov/28545155/)). The **Widal test** performs poorly and is not recommended alone. A Bayesian latent-class network analysis found IgM-based tests outperform IgG counterparts, with lateral-flow IgG and Reverse Passive Hemagglutination performing best in South Asian pediatric populations ([PMID: 31067228](https://pubmed.ncbi.nlm.nih.gov/31067228/)).

**Emerging biomarker assays:** Plasma **IgA responses to HlyE + LPS** distinguished acute typhoid from other bacteremic illnesses (AUC 0.95; sensitivity 90%, specificity 92%) ([PMID: 30020426](https://pubmed.ncbi.nlm.nih.gov/30020426/)) — a promising next-generation diagnostic.

**Molecular:** Multiplex qPCR targeting *ttr*, *staG*, *tviB* (used in wastewater surveillance, [PMID: 42419341](https://pubmed.ncbi.nlm.nih.gov/42419341/)); gene markers *invA* (genus), *phsB* (H₂S), and *tviA* (S. Typhi-specific) for identification ([PMID: 42584516](https://pubmed.ncbi.nlm.nih.gov/42584516/)).

**Imaging:** Erect abdominal radiograph showing **pneumoperitoneum** (86.7% of pediatric perforation cases, [PMID: 34652510](https://pubmed.ncbi.nlm.nih.gov/34652510/)) for the perforation complication; ultrasound for hepatosplenomegaly and gallstones.

**Genetic/omics diagnostics:** Not applicable for host diagnosis. Pathogen whole-genome sequencing is used for AMR surveillance and outbreak tracing.

**Differential diagnosis:** malaria, dengue, rickettsial disease, leptospirosis, brucellosis, amebic liver abscess, and other causes of prolonged fever in endemic areas.

---

## 11. Outcome/Prognosis

- **Mortality:** With prompt appropriate antibiotics, case-fatality is low (global ~0.95%, [PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/)). Untreated, historical mortality reached 10–30%.
- **Ileal perforation (principal lethal complication; Finding F006):** Systematic review of 42 reports — **4,626 cases, 706 deaths, pooled CFR 15.4% (95% CI 13.0–17.8%)**, mean hospital stay 18.4 days ([PMID: 24743649](https://pubmed.ncbi.nlm.nih.gov/24743649/)). Single-center CFRs range 17–30% ([PMID: 28406420](https://pubmed.ncbi.nlm.nih.gov/28406420/), [PMID: 24858189](https://pubmed.ncbi.nlm.nih.gov/24858189/)); pediatric perforation mortality ~26.7%, reaching **100% with three or more perforations** ([PMID: 34652510](https://pubmed.ncbi.nlm.nih.gov/34652510/), [PMID: 24858189](https://pubmed.ncbi.nlm.nih.gov/24858189/)).
- **Prognostic factors:** number of perforations, severity of peritonitis, delay to surgery (>2 h operative time), tachycardia/tachypnea at presentation, and serum potassium (dominant predictor of prolonged stay in a pediatric ML model, [PMID: 42048896](https://pubmed.ncbi.nlm.nih.gov/42048896/)).
- **Other complications:** GI hemorrhage, typhoid encephalopathy, myocarditis, relapse (~5–10%), chronic carriage (2–5%), and long-term **gallbladder carcinoma** (pooled OR 4.28; **Finding F008**).
- **Recovery:** most treated patients recover fully; carriage and gallbladder-cancer risk are the key long-term sequelae.

---

## 12. Treatment

**Pharmacotherapy (empiric, guided by local resistance).**

| Drug / class | Role | NCIT (suggested) | Notes |
|---|---|---|---|
| Ceftriaxone (3rd-gen cephalosporin) | First-line where susceptible | C1096 | Failing in XDR strains |
| Azithromycin (macrolide) | Uncomplicated & XDR | C1174 | 96–100% susceptible in recent cohorts |
| Meropenem / carbapenems | Severe / XDR | C61796 | 98–100% susceptible; mainstay for XDR |
| Fluoroquinolones (ciprofloxacin) | Historically first-line | C2471 | Widespread resistance now |
| Ampicillin, chloramphenicol, TMP-SMX | Older first-line | — | MDR resistance common |

**Resistance landscape (Finding F005):** MDR = resistance to ampicillin, chloramphenicol, and TMP-SMX; **XDR** additionally resists fluoroquinolones and third-generation cephalosporins, first reported in Pakistan and spreading (largely H58 lineage). In one XDR cohort, **all isolates resisted ceftriaxone, ciprofloxacin, and first-line agents; meropenem and azithromycin remained 100% and 96.9% susceptible** ([PMID: 41550837](https://pubmed.ncbi.nlm.nih.gov/41550837/)). By 2021, MDR and XDR proportions reached 14.7% and 43.4% in one Pakistani study ([PMID: 38710290](https://pubmed.ncbi.nlm.nih.gov/38710290/)). Emerging cephalosporin resistance in India arises from plasmid-borne *bla* genes ([PMID: 40208005](https://pubmed.ncbi.nlm.nih.gov/40208005/)). Combination regimens (e.g., meropenem + azithromycin) are used for refractory XDR pediatric cases ([PMID: 38404085](https://pubmed.ncbi.nlm.nih.gov/38404085/)).

**Surgical/interventional:** For perforation — **exploratory laparotomy** with simple two-layer closure, ileal resection with anastomosis, or ileostomy, plus peritoneal lavage (NCIT: laparotomy C15320). Timing is critical; operative delay worsens outcome.

**Supportive care:** fluid/electrolyte resuscitation, antipyretics, nutrition, and correction of hypokalemia.

**Experimental / emerging:** Anti-virulence and quorum-sensing (LuxS/AI-2) inhibitors and quorum-quenching biotherapeutics are under investigation but remain preclinical ([PMID: 42530739](https://pubmed.ncbi.nlm.nih.gov/42530739/), [PMID: 42250148](https://pubmed.ncbi.nlm.nih.gov/42250148/)); phage therapy and multi-omics/AI-guided target discovery are being explored.

**Pharmacogenomics:** No established host pharmacogenomic guidance specific to typhoid therapy.

---

## 13. Prevention

**Primary prevention — vaccination (Finding F004).** **Typhoid conjugate vaccines (Vi-TT / Vi-CRM197)** are the leading tool. In the Malawi phase-3 RCT (28,130 children), a single dose of Vi-TT gave **78.3% efficacy** with durable protection over ~4.3 years across all age groups including infants ([PMID: 38281499](https://pubmed.ncbi.nlm.nih.gov/38281499/)). A meta-analysis of 4 trials (111,481 children) found the risk of blood-culture-confirmed typhoid after Vi-TT was **0.18 vs controls** (~80% efficacy) ([PMID: 40788116](https://pubmed.ncbi.nlm.nih.gov/40788116/)); a test-negative design estimated **80.3% effectiveness** ([PMID: 36442498](https://pubmed.ncbi.nlm.nih.gov/36442498/)). Protection may wane 3–5 years post-vaccination (especially in those vaccinated <2 years), and evidence increasingly supports a **booster dose at a longer interval** ([PMID: 42556475](https://pubmed.ncbi.nlm.nih.gov/42556475/)). WHO recommends mass campaigns for children 9 months–15 years followed by routine infant introduction. Older Vi-polysaccharide and Ty21a live-oral vaccines exist but are less suited to young children.

**Primary prevention — WASH (Finding F011).** Safe drinking water, improved sanitation, and hand hygiene reduce transmission; improved household WASH cut typhoid risk 38% ([PMID: 37983081](https://pubmed.ncbi.nlm.nih.gov/37983081/)). WASH and vaccination are complementary.

**Secondary prevention:** early diagnosis/treatment; **carrier detection and treatment** (and cholecystectomy for carriers with gallstones) removes reservoirs. **Wastewater surveillance** enables early outbreak detection and vaccine-impact monitoring ([PMID: 42419341](https://pubmed.ncbi.nlm.nih.gov/42419341/)); **ring vaccination** around cases is supported by spatial clustering ([PMID: 38913735](https://pubmed.ncbi.nlm.nih.gov/38913735/)).

**Tertiary prevention:** prompt surgical management of perforation; antimicrobial stewardship to preserve azithromycin/carbapenems.

**Public health:** sanitation infrastructure, safe food handling (street-food hygiene), health education. Community KAP gaps are large — in Lilongwe, only 8.2% had adequate typhoid knowledge and 16.7% were aware of TCV ([PMID: 41783922](https://pubmed.ncbi.nlm.nih.gov/41783922/)), underscoring the need for education.

---

## 14. Other Species / Natural Disease

*S.* Typhi is **strictly human-restricted** — there is no natural animal reservoir or naturally occurring typhoid fever in other species. This host restriction reflects co-evolution of virulence factors (including host-adapted typhoid toxin; [PMID: 28993610](https://pubmed.ncbi.nlm.nih.gov/28993610/)) with the human host.

- **Zoonotic potential:** none for *S.* Typhi (contrast with non-typhoidal *Salmonella*, which are zoonotic).
- **Comparative biology:** related host-adapted serovars cause analogous systemic disease in animals (e.g., *S.* Gallinarum in poultry, *S.* Dublin in cattle, *S.* Choleraesuis in pigs), providing comparative models of *Salmonella* host adaptation. Pigs infected with *S.* Typhimurium show shedding-level-dependent cytokine/transcriptomic phenotypes relevant to carriage biology ([PMID: 24632525](https://pubmed.ncbi.nlm.nih.gov/24632525/)).
- **Orthologous virulence loci** (SPI-1, SPI-2) are conserved across *Salmonella* serovars.

---

## 15. Model Organisms

Because *S.* Typhi does not naturally infect other species, modeling relies on surrogates:

| Model | System | Use / recapitulation | Limitation |
|---|---|---|---|
| **Mouse — *S.* Typhimurium** | Mammalian, in vivo | "Mouse typhoid": systemic salmonellosis modeling SPI-1/SPI-2 pathogenesis; bioluminescent imaging tracks infection/carriage ([PMID: 39619287](https://pubmed.ncbi.nlm.nih.gov/39619287/)) | Uses a different serovar; lacks Vi capsule and typhoid toxin |
| **Mouse chronic-carriage models** | Mammalian, in vivo | Gallbladder carriage with **Type-2 immune shift** and T/B-cell recruitment to gallbladder ([PMID: 31575775](https://pubmed.ncbi.nlm.nih.gov/31575775/)); cholesterol-rich diet + biofilm factors favor carriage ([PMID: 39636114](https://pubmed.ncbi.nlm.nih.gov/39636114/), [PMID: 41410426](https://pubmed.ncbi.nlm.nih.gov/41410426/)) | Serovar/host mismatch |
| **Humanized mice** | Mammalian, in vivo | Permit *S.* Typhi infection via human immune components | Incomplete reconstitution |
| **Controlled human infection (challenge) model** | Human, in vivo | Gold standard for susceptibility genetics, early transcriptomics, vaccine testing ([PMID: 35254093](https://pubmed.ncbi.nlm.nih.gov/35254093/), [PMID: 37725060](https://pubmed.ncbi.nlm.nih.gov/37725060/)) | Ethical/logistical constraints; controlled dose |
| **Macrophage cell lines / MDMs** | In vitro | Vi-capsule autophagy modulation, SPI-1 inflammasome activation ([PMID: 39732413](https://pubmed.ncbi.nlm.nih.gov/39732413/), [PMID: 32387390](https://pubmed.ncbi.nlm.nih.gov/32387390/)) | Reductionist |
| **Rabbit immunization** | Mammalian | Vaccine immunogenicity/functional antibody assays ([PMID: 30018230](https://pubmed.ncbi.nlm.nih.gov/30018230/)) | Not a disease model |

**Databases:** MGI (mouse), and *Salmonella* genomic resources (EnteroBase, BV-BRC) for pathogen genetics.

---

## Key Findings (with statistical evidence)

### F001 — Human-restricted *S.* Typhi causes a large LMIC-concentrated burden
WHO EMR review: **5.57–9.23 million cases and 46,200–163,000 deaths annually**, mainly in LMICs; sentinel median incidence 140/100,000 py; highest in children <15 y. *"Annually, there are 5.57 to 9.23 million typhoid fever cases and 46,200 to 163,000 associated deaths, mainly in low- and middle-income countries."* ([PMID: 42413480](https://pubmed.ncbi.nlm.nih.gov/42413480/)).

### F002 — Unique tripartite "typhoid toxin"
CdtB (genotoxic subunit) + PltA/PltB (pertussis-toxin homologs) assemble into a holotoxin expressed within the SCV and secreted in outer-membrane vesicles; retrograde Golgi transport is required for DNA damage. *"PltA and PltB are required for the delivery of CdtB from an intracellular compartment to target cells via autocrine and paracrine pathways… this toxin, which we have named 'typhoid toxin'"* ([PMID: 18191792](https://pubmed.ncbi.nlm.nih.gov/18191792/)); *"…expresses its CDT (named as Typhoid toxin) only in the Salmonella-containing vacuole (SCV) of infected cells"* ([PMID: 23869968](https://pubmed.ncbi.nlm.nih.gov/23869968/)).

### F003 — Chronic gallbladder carriage sustains transmission
**2–5% of infections** become chronic carriers; gallstones + CsgD-regulated biofilm enhance persistence and antibiotic resistance. *"Chronic carriers, accounting for 2-5% of infections, play a crucial role in disease transmission… often asymptomatic but intermittently shed bacteria"*; *"Gallstones are strongly associated with the chronic carrier state, providing a niche for bacterial biofilm formation…"* ([PMID: 41335321](https://pubmed.ncbi.nlm.nih.gov/41335321/)).

### F004 — Typhoid conjugate vaccine ~80% efficacious, durable
Meta-analysis of 4 trials (111,481 children): RR 0.18 after Vi-TT. *"Four trials with 111 481 children found the risk of blood culture-confirmed typhoid fever after Vi-TT to be 0.18 compared with nontyphoid vaccines."* ([PMID: 40788116](https://pubmed.ncbi.nlm.nih.gov/40788116/)); field effectiveness 80.3% ([PMID: 36442498](https://pubmed.ncbi.nlm.nih.gov/36442498/)); durable ≥4 years ([PMID: 38281499](https://pubmed.ncbi.nlm.nih.gov/38281499/)).

### F005 — MDR/XDR narrows treatment to azithromycin + carbapenems
*"All isolates were resistant to ceftriaxone, ciprofloxacin, and first-line agents; meropenem and azithromycin remained 100% and 96.9% susceptible."* ([PMID: 41550837](https://pubmed.ncbi.nlm.nih.gov/41550837/)); *"New strains in India show resistance to third-generation cephalosporins due to plasmid acquisition from other bacteria"* ([PMID: 40208005](https://pubmed.ncbi.nlm.nih.gov/40208005/)).

### F006 — Ileal perforation is the major lethal complication
*"a total of 4,626 hospitalized typhoid intestinal perforation cases and 706 deaths were recorded (CFR = 15·4%; 95% CI 13·0%-17·8%)"* ([PMID: 24743649](https://pubmed.ncbi.nlm.nih.gov/24743649/)).

### F007 — Reproducible blood transcriptional signature, persistent convalescent signature
*"typhoid fever induced a distinct and highly reproducible signature in the peripheral blood that changed during treatment and convalescence"*; the persistent convalescent signature may mark hosts *"more susceptible to reinfection, relapse, or the establishment of a carrier state."* ([PMID: 20018727](https://pubmed.ncbi.nlm.nih.gov/20018727/)); susceptibility variants via challenge genotyping ([PMID: 35254093](https://pubmed.ncbi.nlm.nih.gov/35254093/)).

### F008 — Chronic carriage linked to gallbladder carcinoma
*"The overall OR for chronic S. typhi carrier state was 4.28 (95% CI: 1.84-9.96)."* ([PMID: 24612190](https://pubmed.ncbi.nlm.nih.gov/24612190/)).

### F009 — GBD 2017 authoritative burden
*"Globally, 14·3 million (95% UI 12·5-16·3) cases of typhoid and paratyphoid fevers occurred in 2017, a 44·6% decline from 25·9 million in 1990."*; *"Salmonella enterica serotype Typhi caused 76·3% of cases… global case fatality of 0·95% in 2017."* ([PMID: 30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/)).

### F010 — Vi capsule + SPI-1 drive macrophage survival and hyperinflammation
*"Vi capsule of S. Typhi decreased autophagy of macrophages to increase its survival in host cells by decreasing the expression of Nod2 and Galectin-8."* ([PMID: 39732413](https://pubmed.ncbi.nlm.nih.gov/39732413/)); *"S. Typhi, relative to its non-typhoidal counterpart, S. Typhimurium, induces greater SPI-1-dependent inflammasome activation in monocyte-derived macrophages"* ([PMID: 32387390](https://pubmed.ncbi.nlm.nih.gov/32387390/)).

### F011 — WASH is a modifiable risk factor; typhoid clusters spatially
*"Pooled estimates of limited hygiene (OR = 2.26, 95% CrI: 1.38 to 3.64), untreated water (OR = 1.96…)"* ([PMID: 37644449](https://pubmed.ncbi.nlm.nih.gov/37644449/)); *"The IRR in this innermost cluster was 4.9"* ([PMID: 38913735](https://pubmed.ncbi.nlm.nih.gov/38913735/)); improved household WASH → 38% risk reduction ([PMID: 37983081](https://pubmed.ncbi.nlm.nih.gov/37983081/)).

---

## Mechanistic Model / Interpretation

The findings cohere into a single narrative in which **the pathogen's cellular tropism dictates both acute disease and the chronic reservoir**. *S.* Typhi's defining evolutionary innovations — the **Vi capsule** and the **typhoid toxin** — are the molecular reasons it behaves so differently from non-typhoidal *Salmonella*: the Vi capsule permits an intracellular lifestyle (by suppressing autophagy and modulating DC-SIGN-mediated phagocytosis) that would be paradoxical for a normally anti-phagocytic surface structure, while the exaggerated SPI-1 inflammasome response explains the hyperinflammatory bacteremic state clinically seen as prolonged high fever (F010). The macrophage is therefore the pivotal cell (CL:0000235): its permissiveness allows reticuloendothelial dissemination, and the balance of its inflammatory response shapes whether disease is self-limited, fulminant (→ perforation, F006), or transitions to carriage.

The **carriage branch** (F003, F008) transforms an acute infection into a lifelong public-health problem: gallstone-associated biofilm creates an antibiotic-tolerant niche whose intermittent shedding sustains community transmission and whose chronic inflammation drives a >4-fold increase in gallbladder-cancer risk. This links an infectious disease to an oncologic outcome — a rare and important causal chain.

At the population level, the epidemiologic findings (F001, F009, F011) show the disease is **environmentally gated**: burden tracks WASH deficits and clusters spatially, so both WASH investment and geographically targeted vaccination are rational levers. The therapeutic findings (F005) and preventive findings (F004) frame the current crisis and its solution: as XDR strains erode the antibiotic armamentarium, the **conjugate vaccine** (durable ~80% efficacy) shifts control from cure toward prevention.

---

## Evidence Base

| PMID | Contribution | Relationship to findings |
|---|---|---|
| [30792131](https://pubmed.ncbi.nlm.nih.gov/30792131/) | GBD 2017 burden | Anchors F009 (14.3M cases, 76.3% Typhi, CFR 0.95%) |
| [42413480](https://pubmed.ncbi.nlm.nih.gov/42413480/) | WHO EMR burden | Supports F001 |
| [18191792](https://pubmed.ncbi.nlm.nih.gov/18191792/), [23869968](https://pubmed.ncbi.nlm.nih.gov/23869968/) | Typhoid toxin delivery/secretion | Define F002 |
| [39732413](https://pubmed.ncbi.nlm.nih.gov/39732413/), [32387390](https://pubmed.ncbi.nlm.nih.gov/32387390/), [36286551](https://pubmed.ncbi.nlm.nih.gov/36286551/), [40095029](https://pubmed.ncbi.nlm.nih.gov/40095029/) | Vi/SPI-1 macrophage mechanisms | Build F010 |
| [41335321](https://pubmed.ncbi.nlm.nih.gov/41335321/), [39720794](https://pubmed.ncbi.nlm.nih.gov/39720794/), [39636114](https://pubmed.ncbi.nlm.nih.gov/39636114/) | Carriage, biofilm, diet | Support F003 |
| [24612190](https://pubmed.ncbi.nlm.nih.gov/24612190/) | Carriage–gallbladder cancer meta-analysis | Quantifies F008 (OR 4.28) |
| [24743649](https://pubmed.ncbi.nlm.nih.gov/24743649/) | Perforation CFR meta-analysis | Anchors F006 (CFR 15.4%) |
| [40788116](https://pubmed.ncbi.nlm.nih.gov/40788116/), [38281499](https://pubmed.ncbi.nlm.nih.gov/38281499/), [36442498](https://pubmed.ncbi.nlm.nih.gov/36442498/) | Vi-TT efficacy/effectiveness | Establish F004 |
| [41550837](https://pubmed.ncbi.nlm.nih.gov/41550837/), [40208005](https://pubmed.ncbi.nlm.nih.gov/40208005/), [38710290](https://pubmed.ncbi.nlm.nih.gov/38710290/) | XDR resistance | Support F005 |
| [20018727](https://pubmed.ncbi.nlm.nih.gov/20018727/), [37725060](https://pubmed.ncbi.nlm.nih.gov/37725060/), [35254093](https://pubmed.ncbi.nlm.nih.gov/35254093/) | Host transcriptomics/genetics | Support F007 |
| [37644449](https://pubmed.ncbi.nlm.nih.gov/37644449/), [37983081](https://pubmed.ncbi.nlm.nih.gov/37983081/), [38913735](https://pubmed.ncbi.nlm.nih.gov/38913735/) | WASH & clustering | Support F011 |
| [28545155](https://pubmed.ncbi.nlm.nih.gov/28545155/), [31067228](https://pubmed.ncbi.nlm.nih.gov/31067228/), [30020426](https://pubmed.ncbi.nlm.nih.gov/30020426/) | Diagnostics | Section 10 |

---

## Limitations and Knowledge Gaps

1. **No human causal genetics.** Because typhoid is infectious, the template's genetic sections (causal genes, ACMG variant classification, inheritance, penetrance) are largely not applicable; host susceptibility loci are of modest, incompletely mapped effect.
2. **Burden uncertainty.** GBD estimates carry wide uncertainty intervals and depend on modeling; blood-culture under-ascertainment biases incidence downward. Serosurveys and wastewater surveillance are emerging but not standardized.
3. **Mechanistic evidence is largely in vitro / surrogate-model.** Key macrophage mechanisms (Vi–autophagy, SPI-1 inflammasome) derive from cell lines; carriage biology relies on *S.* Typhimurium mouse models that lack Vi and typhoid toxin, limiting direct translation.
4. **Diagnostics remain suboptimal.** Blood culture is insensitive and slow; RDTs are only moderately accurate; the promising IgA/HlyE assay is not yet widely deployed.
5. **Vaccine durability.** Waning immunity 3–5 years post-TCV and optimal booster strategy are unresolved.
6. **Paratyphoid gap.** *S.* Paratyphi A causes a growing share of enteric fever and is not covered by current TCVs.

---

## Proposed Follow-up Experiments / Actions

1. **Deploy next-generation diagnostics:** validate and scale the IgA anti-HlyE/LPS assay ([PMID: 30020426](https://pubmed.ncbi.nlm.nih.gov/30020426/)) and standardize wastewater qPCR surveillance for real-time transmission monitoring and vaccine-impact evaluation.
2. **Define human host-susceptibility architecture:** expand challenge-cohort GWAS ([PMID: 35254093](https://pubmed.ncbi.nlm.nih.gov/35254093/)) and connect it to the persistent convalescent transcriptional signature to predict carriage/relapse risk.
3. **Test carriage-eradication strategies:** anti-biofilm/CsgD-targeted and quorum-quenching agents in gallbladder-carriage models, with the explicit endpoint of interrupting transmission and reducing gallbladder-cancer risk.
4. **Optimize vaccination policy:** trials of TCV booster timing (favoring longer intervals, [PMID: 42556475](https://pubmed.ncbi.nlm.nih.gov/42556475/)) and evaluation of **ring vaccination** exploiting spatial clustering (IRR 4.9, [PMID: 38913735](https://pubmed.ncbi.nlm.nih.gov/38913735/)).
5. **Preserve last-line antibiotics:** implement antimicrobial-stewardship programs and genomic AMR surveillance (H58 lineage, *bla* plasmid tracking) to protect azithromycin and carbapenems.
6. **Advance bivalent/multivalent vaccines** covering *S.* Paratyphi A and iNTS to close the enteric-fever coverage gap ([PMID: 42566676](https://pubmed.ncbi.nlm.nih.gov/42566676/)).

---

*Report compiled from 11 confirmed findings and 59 reviewed papers across 5 investigation iterations. Evidence types span human clinical (RCTs, cohorts, meta-analyses), controlled human infection, model organism (mouse), and in vitro mechanistic studies.*


## Artifacts

- [OpenScientist final report](Typhoid_Fever-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Typhoid_Fever-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 52 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 52 |
| On topic | 44 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 31 |
| Terms named correctly | 16 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002027` (1 mention) - the report calls it "Symptom"; HP calls it **Abdominal pain**
- `HP:0002039` (1 mention) - the report calls it "Symptom"; HP calls it **Anorexia**
- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0002014` (1 mention) - the report calls it "Symptom"; HP calls it **Diarrhea**
- `HP:0002019` (1 mention) - the report calls it "Symptom"; HP calls it **Constipation**
- `HP:0002240` (1 mention) - the report calls it "Clinical sign"; HP calls it **Hepatomegaly**
- `HP:0001744` (1 mention) - the report calls it "Clinical sign"; HP calls it **Splenomegaly**
- `HP:0011276` (1 mention) - the report calls it "Abnormality of skin morphology"; HP calls it **Vascular skin abnormality**
- `CL:0002270` (2 mentions) - the report calls it "M cell / microfold cell", "M cells", "Tissue/cell level:** intestinal epithelium and **M cells"; CL calls it **type EC2 enteroendocrine cell**
- `UBERON:0002110` (1 mention) - the report calls it "carrier niche"; UBERON calls it **gallbladder**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001882` (1 mention) - the report calls it "Leukopenia"; HP calls it **Decreased total leukocyte count**, and lists "Leukopenia" among its other names
- `CHEBI:16412` (2 mentions) - the report calls it "LPS"; CHEBI calls it **lipopolysaccharide**, and lists "LPS" among its other names
- `GO:0009405` (1 mention) - the report calls it "pathogenesis"; GO calls it **obsolete pathogenesis**
- `GO:0052167` (1 mention) - the report calls it "modulation of host immune response"; GO calls it **symbiont-mediated perturbation of host innate immune response**, and lists "modulation of host innate immune response" among its other names
- `GO:0005794` (1 mention) - the report calls it "Golgi"; GO calls it **Golgi apparatus**, and lists "Golgi" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000235` - called "macrophage", "macrophages"
- `CL:0002270` - called "M cell / microfold cell", "M cells", "Tissue/cell level:** intestinal epithelium and **M cells"