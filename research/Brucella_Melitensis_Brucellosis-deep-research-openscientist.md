---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-28T22:59:19.071694'
end_time: '2026-09-28T23:15:34.559550'
duration_seconds: 975.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Brucella Melitensis Brucellosis
  mondo_id: MONDO:0001972
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
citation_count: 41
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 42
  on_topic: 23
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 37
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 15
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0030166
    reported_labels:
    - Frequent
    ontology_label: Night sweats
  - term_id: HP:0003326
    reported_labels:
    - ~19% (with fever)
    ontology_label: Myalgia
  - term_id: HP:0001824
    reported_labels:
    - Common (adults > children)
    ontology_label: Weight loss
  - term_id: HP:0100775
    reported_labels:
    - Adults > children (p=0.043)
    ontology_label: Dural ectasia
  - term_id: HP:0003429
    reported_labels:
    - Older adults predominant
    ontology_label: CNS hypomyelination
  - term_id: HP:0002716
    reported_labels:
    - Common
    ontology_label: Lymphadenopathy
  - term_id: HP:0001882
    reported_labels:
    - 21% (acute)
    ontology_label: Decreased total leukocyte count
  - term_id: HP:0002910
    reported_labels:
    - 44% (acute)
    ontology_label: Elevated circulating hepatic transaminase concentration
  - term_id: GO:0140355
    reported_labels:
    - T4SS-dependent protein secretion into host cell
    ontology_label: cargo receptor ligand activity
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Brucella_Melitensis_Brucellosis-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Brucella_Melitensis_Brucellosis-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brucella Melitensis Brucellosis
- **MONDO ID:** MONDO:0001972 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Brucella Melitensis Brucellosis** covering all of the
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

# Brucella melitensis Brucellosis: Comprehensive Disease Characterization

**MONDO ID:** MONDO:0001972 | **Category:** Infectious Disease (zoonosis) | **Report date:** 2026-09-29

---

## Summary

**Brucella melitensis brucellosis is the most common and most clinically severe form of human brucellosis**, a globally distributed bacterial zoonosis acquired primarily from small ruminants (sheep and goats). The etiologic agent, *Brucella melitensis*, is a Gram-negative, facultative intracellular coccobacillus transmitted to humans chiefly through ingestion of unpasteurized dairy products, and secondarily via inhalation and direct skin/mucosal contact. It is fundamentally an **infectious, non-heritable disease**; the only "genetic" dimension is host susceptibility, which is modulated by polymorphisms in cytokine and innate-immune-receptor genes (IL4, IL18, TNF, IL10, TGFB1, TLR4). Because the pathogen resides and replicates inside host macrophages within an endoplasmic-reticulum–derived vacuole, it produces a **chronic, relapsing, multisystem febrile illness** requiring prolonged combination antibiotic therapy.

Mechanistically, the disease follows a well-characterized causal chain from **oral/mucosal entry → uptake by macrophages and dendritic cells → VirB Type IV secretion system (T4SS)–driven remodeling of the Brucella-containing vacuole (BCV) into a replicative ER-derived organelle → intracellular replication and immune subversion (Omp25-mediated TNF-α suppression, inhibition of macrophage apoptosis) → hematogenous dissemination to the reticuloendothelial system, bone/joints, liver, spleen, genitourinary tract, heart and CNS → granulomatous inflammation and the clinical syndrome of undulant fever, arthralgia and hepatosplenomegaly**. Host control depends on a Th1/IFN-γ/IL-12 cellular immune response; when this fails, the organism persists in a myeloid reservoir, producing chronic and focal disease.

Clinically, the three most frequent manifestations are **fever (~83%), arthralgia/arthritis (~67%), and hepatosplenomegaly (~61%)**. Osteoarticular disease (spondylitis, sacroiliitis, osteomyelitis) is the most common complication; neurobrucellosis is rare (~0.9%) and endocarditis, though rare, is the leading cause of brucellosis death. Diagnosis rests on serology (Rose Bengal, standard agglutination test, ELISA) plus blood/tissue culture, with PCR adding sensitivity. First-line treatment is **doxycycline plus rifampicin or doxycycline plus an aminoglycoside** for a prolonged course; monotherapy relapses. Overall mortality is low. With no licensed human vaccine, prevention is a **One-Health enterprise** centered on livestock vaccination (*B. melitensis* Rev1), pasteurization, and reservoir control.

---

## 1. Disease Information

**Overview.** *Brucella melitensis* brucellosis is a systemic zoonotic infection and the predominant cause of human brucellosis worldwide. It is an aggregated, disease-level entity (the knowledge here is drawn from case series, cohorts, registries, and mechanistic studies rather than a single-patient EHR source). The disease is characterized by a variable clinical presentation ranging from acute febrile illness to chronic relapsing multisystem disease.

**Key identifiers.**
- **MONDO:** MONDO:0001972
- **MeSH:** Brucellosis; Brucella melitensis (organism)
- **ICD-10:** A23.0 (Brucellosis due to Brucella melitensis); **ICD-11:** 1B95
- **NCBI Taxonomy (organism):** *Brucella melitensis*, txid29459

**Synonyms/alternative names.** Malta fever, Mediterranean fever, undulant fever, goat/sheep brucellosis, febris melitensis. (Bang's disease historically refers to *B. abortus*.)

> *"Brucella melitensis, one of the organisms responsible for causing the disease in sheep and goat, is responsible for the disease in humans. The disease is transmitted mainly from sheep and goat to humans via ingestion (typically through milk), inhalation, abrasion and so on."* — [PMID: 41132010](https://pubmed.ncbi.nlm.nih.gov/41132010/)

---

## 2. Etiology

**Primary cause — infectious.** The disease is caused entirely by infection with *Brucella melitensis*, a facultative intracellular Gram-negative coccobacillus. Of the four *Brucella* species significant to human health (*B. melitensis*, *B. abortus*, *B. suis*, *B. canis*), *B. melitensis* is the most virulent and the leading cause of human disease. Small ruminants are the reservoir: a systematic review/meta-analysis of 2010–2023 data found pooled *B. melitensis* prevalence of **8.07% (95% CI 6.36–9.78%) in sheep, 2.46% (95% CI 1.70–3.21%) in goats, and 5.54% combined (95% CI 4.63–6.45%)** ([PMID: 41132010](https://pubmed.ncbi.nlm.nih.gov/41132010/)).

**Risk factors (environmental/behavioral — the dominant determinants).**
- **Dietary:** consumption of unpasteurized/fresh milk and dairy or undercooked meat (aOR 5.70, 95% CI 1.94–16.76) ([PMID: 41860883](https://pubmed.ncbi.nlm.nih.gov/41860883/)).
- **Occupational/contact:** rearing livestock at home (aOR 3.75, 95% CI 1.36–10.32), frequent contact with animal manure (aOR 3.29, 95% CI 1.29–8.47); farmers, shepherds, veterinarians, abattoir and laboratory workers are high-risk.
- **Socioeconomic:** lack of formal education (aOR 4.05, 95% CI 1.02–16.01) ([PMID: 41860883](https://pubmed.ncbi.nlm.nih.gov/41860883/)).
- **Demographic:** male sex and adult working age (males 71% of cases in a large Chinese series, 2.45× females) ([PMID: 41632803](https://pubmed.ncbi.nlm.nih.gov/41632803/)).

**Genetic risk factors (host susceptibility, not causal).** Cytokine and innate-immune-receptor gene polymorphisms modulate risk and complications (detailed in §4 and §9):
- **Risk-increasing:** IL-4 rs2243250, IL-18 rs1946519 mutant alleles; TGFβ1 +868 C/T (rs1800470) TT homozygote (OR 2.60, p=0.023); TNF −238 G>A (rs361525) minor A allele (11.4% vs 2.6% in controls, p<0.001) ([PMID: 31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/), [PMID: 25738611](https://pubmed.ncbi.nlm.nih.gov/25738611/), [PMID: 39419734](https://pubmed.ncbi.nlm.nih.gov/39419734/)).
- **Relatively protective:** IFN-γ UTR5644, TGF-β rs1800470/rs1800471, TNF-α rs1800629, IL-10 rs1800872 dominant models ([PMID: 31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/)).

**Protective factors (environmental).** Pasteurization/boiling of milk, use of personal protective equipment, avoidance of aborted animal materials, and public-health education. Treatment compliance is protective against relapse (aOR 0.25, 95% CI 0.09–0.86) ([PMID: 42603185](https://pubmed.ncbi.nlm.nih.gov/42603185/)).

**Gene–environment interactions.** Individuals carrying pro-inflammatory-skewing or immune-modulating genotypes (e.g., TNF/TGFB1/IL variants) who also sustain high infectious exposure (raw dairy, occupational contact) are at compounded risk of infection and focal complications such as spondylodiscitis ([PMID: 39419734](https://pubmed.ncbi.nlm.nih.gov/39419734/)).

---

## 3. Phenotypes

The clinical phenotype is a **chronic relapsing febrile multisystem illness**. Frequencies below are drawn from a Houston 10-year case series (n=18), a North Macedonia series (n=508), and a Saudi pediatric series (n=57).

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Fever / undulant fever | Symptom | ~83% (36.8% sole finding in children) | HP:0001945 (Fever) |
| Arthralgia / arthritis | Symptom / sign | ~67% | HP:0002829; HP:0001369 |
| Hepatosplenomegaly | Clinical sign | ~61% | HP:0001433 |
| Night sweats | Symptom | Frequent | HP:0030166 |
| Myalgia | Symptom | ~19% (with fever) | HP:0003326 |
| Weight loss | Symptom | Common (adults > children) | HP:0001824 |
| Sacroiliitis | Sign / imaging | Adults > children (p=0.043) | HP:0100775 |
| Spondylitis / spondylodiscitis | Sign / imaging | Older adults predominant | HP:0003429 |
| Lymphadenopathy | Sign | Common | HP:0002716 |
| Leukopenia | Lab abnormality | 21% (acute) | HP:0001882 |
| Elevated transaminases | Lab abnormality | 44% (acute) | HP:0002910 |

> *"Common clinical features included fever (83%), arthralgias or arthritis (67%), and hepatosplenomegaly (61%)."* — [PMID: 29863218](https://pubmed.ncbi.nlm.nih.gov/29863218/)

**Age of onset & severity.** Any age; predominantly adult (working-age) but with substantial pediatric burden. Severity is variable — mild self-limited illness to severe focal/chronic disease. **Progression** is episodic/relapsing (undulant fever pattern). Age-dependent phenotype distribution is documented: *"Sacroiliitis was more predominant in adults than children (p = 0.043), while focal hematological involvement was more prevalent in children than in adults (p = 0.004). Spondylitis was more dominant in the old age group"* ([PMID: 39630247](https://pubmed.ncbi.nlm.nih.gov/39630247/)).

**Quality-of-life impact.** Chronic arthralgia, fatigue, night sweats, and osteoarticular complications impair daily functioning and work capacity; in pregnancy, infection can cause anemia, miscarriage, and pre-term birth.

---

## 4. Genetic/Molecular Information

**Causal genes: NONE.** This is an infectious disease with no human causal gene or pathogenic germline/somatic variant. There are no ClinVar pathogenic variants, no inheritance pattern, no chromosomal abnormalities, and no epigenetic disease-defining lesions in the classic Mendelian sense.

**Host susceptibility loci (modifier of risk/severity, not causal).** From a meta-analysis of 25 case-control studies and individual cohorts:

| Gene (HGNC) | Variant | Effect | Evidence |
|---|---|---|---|
| **IL4** | rs2243250 | ↑ susceptibility | [PMID: 31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/) |
| **IL18** | rs1946519 | ↑ susceptibility | [PMID: 31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/) |
| **TGFB1** | +868 C/T (rs1800470), TT | Risk factor, OR 2.60 (p=0.023) | [PMID: 25738611](https://pubmed.ncbi.nlm.nih.gov/25738611/) |
| **TNF** | −238 G>A (rs361525), A allele | ↑ risk & spondylodiscitis (11.4% vs 2.6%) | [PMID: 39419734](https://pubmed.ncbi.nlm.nih.gov/39419734/) |
| **TLR4** | Asp299Gly (rs4986790), Thr399Ile (rs4986791) | Complication risk | [PMID: 39419734](https://pubmed.ncbi.nlm.nih.gov/39419734/) |
| **IL10 / IL6** | High-producer genotypes | ↑ susceptibility | [PMID: 17544674](https://pubmed.ncbi.nlm.nih.gov/17544674/) |
| **IFNG, IL10** | UTR5644 / rs1800872 | Relatively protective | [PMID: 31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/) |

> *"the mutant allele of IL-4 rs2243250 and IL-18 rs1946519 were associated with increased susceptibility to brucellosis"* — [PMID: 31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/)
> *"Carriage of the minor frequency A alleles at -238 of the promoter region of TNF was greater in patients than in controls (11.4% vs 2.6 %, p < 0.001)"* — [PMID: 39419734](https://pubmed.ncbi.nlm.nih.gov/39419734/)

**Pathogen molecular determinants of virulence** (the biologically "causal" genetics reside in the bacterium): the *virB* operon (VirB T4SS), quorum-sensing regulator **VjbR**, two-component system **BvrR/BvrS**, cyclic β-1,2-glucans, **BacA**, outer-membrane proteins **Omp25/Omp28**, and metabolic/membrane genes (*cydDC*, *ptsP*) identified by TraDIS as essential for macrophage survival — *"the discovery of 374 anti-phagocytic associated essential genes"* ([PMID: 41917383](https://pubmed.ncbi.nlm.nih.gov/41917383/), [PMID: 22392933](https://pubmed.ncbi.nlm.nih.gov/22392933/)).

---

## 5. Environmental Information

**Infectious agent.** *Brucella melitensis* (NCBI Taxon 29459); biovars 1–3, with the Eastern Mediterranean lineage/biovar 3 predominant in China ([PMID: 42360586](https://pubmed.ncbi.nlm.nih.gov/42360586/)).

**Environmental/occupational factors.** Contact with infected small ruminants and their products; contaminated manure, birth products, and aborted materials; aerosol exposure in laboratories and abattoirs (a recognized potential bioterrorism agent) ([PMID: 15677842](https://pubmed.ncbi.nlm.nih.gov/15677842/)). **Lifestyle factors:** consumption of raw milk, soft cheeses, and undercooked meat. Cold semi-arid (BSk) climates and spring seasonality are associated with higher small-ruminant seroprevalence ([PMID: 41506444](https://pubmed.ncbi.nlm.nih.gov/41506444/)).

Relevant chemical entities (treatment): doxycycline (CHEBI:50845), rifampicin (CHEBI:28077), streptomycin (CHEBI:17076), gentamicin (CHEBI:27412).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Oral/mucosal/inhalational entry** of *B. melitensis* from contaminated dairy, aerosols, or abraded skin **leads to** uptake at mucosal surfaces.
2. Bacteria are **phagocytosed by macrophages and dendritic cells** (internalization is normal even in avirulent mutants) — **results in** an early endosomal Brucella-containing vacuole (eBCV).
3. The **VirB Type IV secretion system (T4SS)** delivers effector proteins that **remodel the eBCV into a replication-permissive, ER-derived vacuole (rBCV)** — *demonstrated*: VirB-deficient mutants stall in eBCVs and cannot form rBCVs ([PMID: 27899503](https://pubmed.ncbi.nlm.nih.gov/27899503/)).
4. Effectors (BspF via Arf6-GAP ACAP1; Rab2- and α-enolase-engaging effectors) **subvert host secretory/recycling traffic** — **results in** robust intravacuolar replication ([PMID: 34423453](https://pubmed.ncbi.nlm.nih.gov/34423453/), [PMID: 32234817](https://pubmed.ncbi.nlm.nih.gov/32234817/), [PMID: 27900285](https://pubmed.ncbi.nlm.nih.gov/27900285/)).
5. In parallel, **Omp25 suppresses macrophage TNF-α secretion** and Brucella **inhibits macrophage/monocyte apoptosis** — **results in** immune evasion and a protected replicative niche ([PMID: 12414158](https://pubmed.ncbi.nlm.nih.gov/12414158/)).
6. Replicated bacteria convert the rBCV into an **autophagic BCV (aBCV)** — **results in** cell-to-cell egress and dissemination ([PMID: 27899503](https://pubmed.ncbi.nlm.nih.gov/27899503/)).
7. **Hematogenous spread within myeloid cells** to the reticuloendothelial system, bone/joints, liver, spleen, genitourinary tract, heart and CNS — **leads to** multisystem seeding.
8. **Granuloma formation** (non-caseating) and the host **Th1/IFN-γ/IL-12/TNF-α response** attempt clearance — **branch A (effective Th1):** bacterial clearance and recovery; **branch B (failed control):** persistence in lipid-laden CD11c⁺/CD205⁺/Arginase1⁺ reservoir cells → **chronic/relapsing and focal disease** ([PMID: 12414158](https://pubmed.ncbi.nlm.nih.gov/12414158/), [PMID: 26376185](https://pubmed.ncbi.nlm.nih.gov/26376185/)).
9. Persistent granulomatous inflammation in seeded organs **produces the clinical syndrome**: undulant fever, arthralgia/spondylitis, hepatosplenomegaly, and focal complications (endocarditis, neurobrucellosis, epididymo-orchitis).

```
 Raw dairy / aerosol / contact
            |
            v
   Macrophage / DC uptake --> eBCV
            |  VirB T4SS + effectors (BspF/Arf6, Rab2, alpha-enolase)
            v
   rBCV (ER-derived) --> intracellular replication
            |  Omp25 -| TNF-alpha ; apoptosis inhibited
            v
   aBCV --> egress --> hematogenous myeloid dissemination
            |
   +--------+---------+
   v                  v
 Th1/IFN-g/IL-12    Failed control --> lipid-laden CD11c+/CD205+/Arg1+
 clearance            reservoir cells --> chronic/focal disease
   |                  |
   v                  v
 Recovery      Fever, arthralgia, hepatosplenomegaly, focal complications
```

**Molecular pathways / cellular processes.** T4SS effector–host GTPase cascades (Arf6–Rab8a, Rab2); NF-κB signaling (TBK1 promotes control — knockdown increases bacterial survival and reduces IL-1β/IL-6/TNF-α/IFN-γ) ([PMID: 41605070](https://pubmed.ncbi.nlm.nih.gov/41605070/)); autophagy (aBCV egress); inhibited apoptosis; granulomatous inflammation. **GO terms:** GO:0140355 (T4SS-dependent protein secretion into host cell), GO:0006909 (phagocytosis), GO:0016236 (macroautophagy), GO:0006915 (apoptotic process, inhibited), GO:0002250 (adaptive immune response), GO:0032609 (IFN-γ production). **CL terms:** CL:0000235 (macrophage), CL:0000451 (dendritic cell), CL:0000576 (monocyte).

**Immune involvement.** Protective immunity is Th1/cell-mediated: *"Brucella infection results in Type1 (Th1) cellular immune response which promotes a clearance of the bacterial organism. The development of this response is under the control of major cytokines like TNF-alpha, IFN-gamma and IL-12"* ([PMID: 12414158](https://pubmed.ncbi.nlm.nih.gov/12414158/)). Immune evasion via Omp25-mediated TNF-α suppression: *"in humans, B. suis-infected macrophages which produce IL-1, IL-6, IL-10 and several chemokines including IL-8, do not secrete TNF-alpha... this inhibition involves the outer membrane protein Omp25 of Brucella"* ([PMID: 12414158](https://pubmed.ncbi.nlm.nih.gov/12414158/)).

**Subcellular mechanism.** *"BCVs are remodeled into replication-permissive organelles (rBCV) derived from the host endoplasmic reticulum, a process that requires modulation of host secretory functions via delivery of effector proteins by the Brucella VirB type IV secretion system (T4SS)"* ([PMID: 27899503](https://pubmed.ncbi.nlm.nih.gov/27899503/)); *"Brucella abortus generates a host endoplasmic reticulum-derived vacuole (rBCV) that supports its intracellular growth, via VirB Type IV secretion system-mediated delivery of effector proteins"* ([PMID: 34423453](https://pubmed.ncbi.nlm.nih.gov/34423453/)).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** reticuloendothelial system — liver, spleen, bone marrow, lymph nodes (hepatosplenomegaly, lymphadenopathy, non-caseating granulomas). **Secondary/focal:** skeleton and joints (spine, sacroiliac joints — spondylodiscitis, sacroiliitis, osteomyelitis), genitourinary tract (epididymo-orchitis), heart (endocarditis, myopericarditis), CNS (meningoencephalitis, neurobrucellosis), peritoneum (spontaneous bacterial peritonitis), and placenta in pregnancy.

> *"Brucella contributed to 18 (30.51%) of epididymo-orchitis cases during study period."* — [PMID: 40350681](https://pubmed.ncbi.nlm.nih.gov/40350681/)
> *"The cases presented as prolonged fever in 4 patients (40%), spondylodiscitis in 2 (20%), myopericarditis, meningoencephalitis, febrile hepatitis, and cervical lymphadenopathy"* — [PMID: 41021857](https://pubmed.ncbi.nlm.nih.gov/41021857/)

**Body systems:** hematologic/lymphoreticular, musculoskeletal, hepatobiliary, genitourinary, cardiovascular, nervous.

**Tissue/cell level:** phagocytic mononuclear cells (macrophages, monocytes, dendritic cells) are the primary target/reservoir; granuloma-forming myeloid and lymphoid aggregates. **UBERON:** UBERON:0002106 (spleen), UBERON:0002107 (liver), UBERON:0002371 (bone marrow), UBERON:0001474 (bone element), UBERON:0000079 (male reproductive system), UBERON:0000948 (heart), UBERON:0001017 (CNS). **Subcellular (GO CC):** GO:0005783 (endoplasmic reticulum — rBCV origin), GO:0005776 (autophagosome — aBCV), GO:0005768 (endosome — eBCV), GO:0020003 (symbiont-containing vacuole).

---

## 8. Temporal Development

**Onset.** Insidious, over days to weeks after exposure (incubation typically 1–4 weeks, occasionally months). Onset patterns: acute, subacute, or chronic/insidious.

**Progression / stages.** Classically **acute (<8 weeks), subacute (8 weeks–1 year), and chronic (>1 year)**. Undulant (relapsing-remitting) fever is characteristic. Acute disease carries a stronger inflammatory profile and better cure rate: *"patients with acute brucellosis had a significantly higher frequency of leukopenia (21.2 % vs. 0 %; p < 0.01), elevated C reactive protein (CRP) (76.7 % vs. 52.0 %; p = 0.01), and elevated transaminases (43.8 % vs. 20.0 %; p = 0.025)"* — therapeutic response 93.2% acute vs lower in subacute/chronic ([PMID: 41241000](https://pubmed.ncbi.nlm.nih.gov/41241000/)). Chronicity and focalization predict poor outcome: *"Focal brucellosis (OR 3.52, 95 % CI 1.28 - 9.71, p = 0.015) and low albumin levels ... were independent risk factors for therapeutic failure."* ([PMID: 40185219](https://pubmed.ncbi.nlm.nih.gov/40185219/)).

**Patterns.** Remission is treatment-induced; relapse (~3%) typically occurs within months, associated with female sex (aOR 3.68) and non-compliance ([PMID: 42603185](https://pubmed.ncbi.nlm.nih.gov/42603185/)). Early, adherent combination therapy is the critical intervention window.

---

## 9. Inheritance and Population

**Inheritance.** Not applicable — infectious, non-heritable. No penetrance/expressivity/anticipation/mosaicism/founder-effect/carrier-frequency parameters apply. Host susceptibility is **multifactorial/polygenic** (cytokine and TLR gene polymorphisms; §4).

**Epidemiology.** Brucellosis is among the commonest zoonoses globally (>500,000 new human cases/year historically). Regional endemic incidence is high and rising in parts of Asia:

| Setting | Metric | Value | PMID |
|---|---|---|---|
| Ningxia, China (2010–2024) | Avg annual incidence | 35.08/100,000 (peak 84.80 in 2022); 35,665 cases, 0 deaths | [41632803](https://pubmed.ncbi.nlm.nih.gov/41632803/) |
| Western Uganda (pregnant women) | Seroprevalence | 14.0% (95% CI 9.2–18.8) | [41860883](https://pubmed.ncbi.nlm.nih.gov/41860883/) |
| Ethiopia (2015–2024, humans) | Pooled seroprevalence | 6.9% (95% CI 4.9–8.8) | [39696174](https://pubmed.ncbi.nlm.nih.gov/39696174/) |
| China (national human cases) | 2019 → 2023 | 45,046 → 70,439 cases | [42360586](https://pubmed.ncbi.nlm.nih.gov/42360586/) |

> *"A total of 35 665 human brucellosis cases were reported in Ningxia, with no associated deaths, during the study period."* — [PMID: 41632803](https://pubmed.ncbi.nlm.nih.gov/41632803/)

**Demographics.** Male predominance (~2.4:1), driven by occupational exposure. **Geographic distribution:** endemic in the Mediterranean basin, Middle East, Central/South Asia, sub-Saharan Africa, and Latin America; expanding within China from northern pastoral provinces (Inner Mongolia) to industrial southern provinces via livestock trade ([PMID: 42360586](https://pubmed.ncbi.nlm.nih.gov/42360586/)). All ages affected, with substantial pediatric disease in endemic areas.

---

## 10. Diagnostics

**Serology (first-line):** Rose Bengal plate test (RBPT), standard tube agglutination test (SAT), and ELISA (anti-LPS or whole-cell, and recombinant Omp28 which correlated ~90% with RBPT) ([PMID: 20075115](https://pubmed.ncbi.nlm.nih.gov/20075115/)). A ≥4-fold decline in SAT titer after treatment predicts favorable response (OR 5.84) ([PMID: 41241000](https://pubmed.ncbi.nlm.nih.gov/41241000/)).

> *"Serodiagnosis of brucellosis is carried out by detection of antibodies generated against LPS or whole-cell bacterial extracts by ELISA or agglutination tests using colorimetry."* — [PMID: 20075115](https://pubmed.ncbi.nlm.nih.gov/20075115/)

**Culture (definitive):** blood/bone-marrow/tissue culture. Yield is higher in children than adults: *"Positive blood cultures were more frequently reported among children than adults (83% vs 33%,"* ([PMID: 29863218](https://pubmed.ncbi.nlm.nih.gov/29863218/)).

**Molecular:** conventional and real-time PCR add sensitivity, detecting some culture-negative/seropositive samples; combining culture + PCR maximizes detection ([PMID: 18832199](https://pubmed.ncbi.nlm.nih.gov/18832199/)). qPCR showed 100% concordance with RBPT in humans in one Nigerian study ([PMID: 40140617](https://pubmed.ncbi.nlm.nih.gov/40140617/)).

**Laboratory abnormalities:** leukopenia, elevated CRP, elevated transaminases, occasionally pancytopenia. **Imaging:** MRI/CT for spondylodiscitis and sacroiliitis; echocardiography for endocarditis. **Histopathology:** non-caseating granulomas.

**Differential diagnosis:** tuberculosis, typhoid, other causes of undifferentiated fever, endocarditis of other etiology, lymphoma, autoimmune arthritis. **Genetic/omics diagnostics and newborn/carrier screening:** not applicable.

---

## 11. Outcome/Prognosis

**Mortality is low.** A large endemic series reported zero deaths among 35,665 cases ([PMID: 41632803](https://pubmed.ncbi.nlm.nih.gov/41632803/)). Pediatric cohorts show ~88–90% favorable outcomes and ~3% relapse with adherent therapy ([PMID: 42603185](https://pubmed.ncbi.nlm.nih.gov/42603185/)).

**Endocarditis is the leading cause of death.** *"Brucella endocarditis is a rare but a serious complication of human brucellosis."* — frequently requires valve replacement plus prolonged antibiotics ([PMID: 11910696](https://pubmed.ncbi.nlm.nih.gov/11910696/), [PMID: 20362000](https://pubmed.ncbi.nlm.nih.gov/20362000/)).

**Complications.** In a nationwide pediatric cohort (n=1,052): complications 8.3%, most frequently osteoarticular; neurobrucellosis 0.9%; relapse 3.2%. Complications associated with headache (aOR 3.57), arthralgia/arthritis, culture positivity, night sweats, myalgia ([PMID: 42603185](https://pubmed.ncbi.nlm.nih.gov/42603185/)).

> *"Complications occurred in 87 patients (8.3%), most frequently osteoarticular (spondylitis, sacroiliitis, and osteomyelitis), whereas neurobrucellosis was rare (0.9%); relapse occurred in 34 patients (3.2%)."* — [PMID: 42603185](https://pubmed.ncbi.nlm.nih.gov/42603185/)

**Prognostic factors.** Favorable: acute presentation, elevated baseline CRP (OR 4.00), ≥4-fold SAT decline (OR 5.84), treatment adherence. Unfavorable: focal disease (OR 3.52 for failure), chronicity (OR 11.20 in focal cases), low albumin, female sex (relapse). Morbidity is driven by chronic osteoarticular disability; recovery is usually complete with timely therapy.

---

## 12. Treatment

**First-line pharmacotherapy — combination, prolonged (≥6 weeks).** Doxycycline (CHEBI:50845) plus rifampicin (CHEBI:28077), OR doxycycline plus an aminoglycoside (streptomycin/gentamicin).

> *"Regimens containing doxycycline plus streptomycin or doxycycline plus rifampin are effective for most forms of brucellosis."* — [PMID: 15677842](https://pubmed.ncbi.nlm.nih.gov/15677842/)
> *"Trimethoprim-sulfamethoxazole and fluoroquinolones also have good results against Brucella, but are associated with high relapse rates when used as monotherapy."* — [PMID: 15677842](https://pubmed.ncbi.nlm.nih.gov/15677842/)

**Comparative efficacy (network meta-analysis of 43 RCTs).** Relative to standard doxycycline+rifampicin, **doxycycline+gentamicin ranked best (SUCRA 0.94)**, followed by triple therapy (0.87) and doxycycline+streptomycin (0.78) ([PMID: 39172763](https://pubmed.ncbi.nlm.nih.gov/39172763/)). The Ioannina recommendations provide evidence-based guidance ([PMID: 18162038](https://pubmed.ncbi.nlm.nih.gov/18162038/)).

| Regimen | Role | NCIT (approx.) |
|---|---|---|
| Doxycycline + rifampicin | Standard oral first-line | C61815 (doxycycline); C29325 (rifampin) |
| Doxycycline + streptomycin/gentamicin | Severe/focal; best efficacy | C839 (streptomycin); C557 (gentamicin) |
| Triple therapy (add aminoglycoside/TMP-SMX) | Neurobrucellosis, endocarditis, spondylitis | — |
| Surgery + prolonged antibiotics | Endocarditis (valve replacement), abscess drainage | — |

**Special situations.** Neurobrucellosis, endocarditis, and spondylitis require triple therapy and extended duration; endocarditis frequently requires surgical valve replacement. In pregnancy and young children, rifampicin-based regimens are used (tetracyclines/aminoglycosides restricted). **Advanced/targeted/gene/cell/RNA therapies, immunotherapy, pharmacogenomics:** not applicable/not used. **Adverse events:** doxycycline photosensitivity/GI upset, rifampicin hepatotoxicity and drug–drug interactions, aminoglycoside oto-/nephrotoxicity.

---

## 13. Prevention

**No licensed human vaccine exists.** Prevention is a One-Health enterprise.

- **Primary prevention:** livestock vaccination and reservoir control. *"Rev1, the only vaccine currently recommended to control the disease in sheep and goats, has several drawbacks."* ([PMID: 36653223](https://pubmed.ncbi.nlm.nih.gov/36653223/)); *"The mainstay of most control programs is vaccination of sheep and goats with a live vaccine, Rev-1."* ([PMID: 26825313](https://pubmed.ncbi.nlm.nih.gov/26825313/)). Rev1 is safe in sheep only for lambs 3–4 months, causes serological interference and abortion in pregnancy, and is virulent to humans. Next-generation rough-LPS candidates (Rev1Δwzm, 16MΔwzm) improve safety and reduce serological interference ([PMID: 38806353](https://pubmed.ncbi.nlm.nih.gov/38806353/), [PMID: 36653223](https://pubmed.ncbi.nlm.nih.gov/36653223/)).
- **Food safety:** pasteurization/boiling of milk; avoidance of raw dairy and undercooked meat.
- **Occupational protection:** PPE, safe handling of birth/abortion products, laboratory biosafety (BSL-3).
- **Public-health measures:** surveillance, herd testing and culling, quarantine, health education. SEIRS modeling predicts ~3.5 years to eliminate brucellosis on a mixed endemic farm with combined sheep+cattle vaccination ([PMID: 26825313](https://pubmed.ncbi.nlm.nih.gov/26825313/)).
- **Secondary/tertiary prevention:** early diagnosis and treatment of exposed/symptomatic individuals; adherence support to prevent relapse and chronic complications. **Genetic screening/counseling:** not applicable.

---

## 14. Other Species / Natural Disease

**Taxonomy of hosts.** Primary reservoir: sheep (*Ovis aries*, txid9940) and goats (*Capra hircus*, txid9925). Other susceptible species: cattle, swine, dogs, camels, equids, and wild mammals ([PMID: 42360586](https://pubmed.ncbi.nlm.nih.gov/42360586/)).

**Natural disease (veterinary).** In livestock, *B. melitensis* causes reproductive failure — abortion, retained placenta, orchitis/epididymitis, infertility — with major economic impact. *"In livestock, brucellosis causes reproductive failure, including abortions, leading to substantial economic losses."* ([PMID: 41127417](https://pubmed.ncbi.nlm.nih.gov/41127417/)). The organism localizes to placenta and reproductive tissues (tropism classically linked to erythritol).

**Zoonotic transmission.** *"The disease can be transmitted to humans through the food chain or by direct contact with infected animals."* ([PMID: 35482257](https://pubmed.ncbi.nlm.nih.gov/35482257/)). High cross-species susceptibility makes it a paradigmatic One-Health zoonosis.

**Comparative biology.** The intracellular VirB T4SS/BCV mechanism is conserved across *Brucella* species and hosts; granuloma biology parallels other intracellular pathogens (*Mycobacterium*, *Salmonella*, *Yersinia*) ([PMID: 41921569](https://pubmed.ncbi.nlm.nih.gov/41921569/)).

---

## 15. Model Organisms

**Mouse (primary model).** BALB/c and C57BL/6 mice via intranasal/intraperitoneal *B. melitensis* establish chronic splenic infection recapitulating the human myeloid reservoir. *"Most of the infected spleen cells contained high levels of lipids and expressed CD11c and CD205 dendritic cell markers and Arginase1, but were negative for the M2a markers Fizz1 or CD301."* ([PMID: 26376185](https://pubmed.ncbi.nlm.nih.gov/26376185/)).

**Genetic models.** IL-12p40⁻/⁻ (Th1-deficient) mice show uncontrolled splenic reservoir persistence; STAT6 deficiency did not affect bacterial growth; TBK1 knockout promotes bacterial survival in vivo ([PMID: 26376185](https://pubmed.ncbi.nlm.nih.gov/26376185/), [PMID: 41605070](https://pubmed.ncbi.nlm.nih.gov/41605070/)).

**Cellular/in vitro models.** RAW264.7 and J774.A1 murine macrophages, human macrophages/monocytes; used for TraDIS (374 essential intracellular-survival genes) and genome-wide CRISPR host-gene screens ([PMID: 41917383](https://pubmed.ncbi.nlm.nih.gov/41917383/), [PMID: 42617139](https://pubmed.ncbi.nlm.nih.gov/42617139/)).

**Recapitulation & limitations.** Mouse models faithfully reproduce chronic intracellular persistence, Th1-dependent control, and reservoir-cell biology, but do **not** reproduce the undulant fever, osteoarticular disease, or endocarditis of human disease. Natural livestock (sheep/goat) infection best models reproductive pathology and vaccine efficacy.

---

## Mechanistic Model / Interpretation

The unifying theme of *B. melitensis* pathogenesis is **stealthy intracellular parasitism of professional phagocytes**. Two pathogen programs drive disease: (1) the **VirB T4SS**, which converts a doomed endosome into a bespoke ER-derived replicative organelle by hijacking host GTPase traffic (Arf6–Rab8a, Rab2) and secretory machinery; and (2) **innate-immune subversion**, principally Omp25-mediated TNF-α suppression and blockade of macrophage apoptosis. The **outcome bifurcates on host immunity**: a competent Th1/IFN-γ/IL-12/TNF-α (and TBK1/NF-κB) response clears the organism, whereas failure — influenced by cytokine-gene polymorphisms (IL4, IL18, TNF, TGFB1, IL10, TLR4) — permits persistence in lipid-laden dendritic-cell-like reservoir cells and produces the chronic, relapsing, focal disease that accounts for the clinical morbidity (spondylitis, endocarditis, neurobrucellosis).

This model explains the therapeutic logic: because bacteria hide intracellularly, treatment must use **lipophilic, intracellularly-penetrating antibiotics in combination for prolonged courses** — hence doxycycline paired with rifampicin or an aminoglycoside, and the high relapse of monotherapy. It also explains prevention strategy: with human immunity difficult to induce safely, breaking the **animal-reservoir → food/contact → human** chain (Rev1 livestock vaccination, pasteurization, surveillance) is the effective lever.

---

## Evidence Base

| PMID | Contribution | Type |
|---|---|---|
| [41132010](https://pubmed.ncbi.nlm.nih.gov/41132010/) | Etiology, transmission routes, reservoir prevalence | Systematic review/meta-analysis |
| [15677842](https://pubmed.ncbi.nlm.nih.gov/15677842/) | First-line combination therapy; monotherapy relapse | Guidelines |
| [39172763](https://pubmed.ncbi.nlm.nih.gov/39172763/) | Comparative regimen efficacy (doxy+gentamicin best) | Network meta-analysis, 43 RCTs |
| [22392933](https://pubmed.ncbi.nlm.nih.gov/22392933/) | VirB T4SS & VjbR required for intracellular replication | In vitro/mouse |
| [27899503](https://pubmed.ncbi.nlm.nih.gov/27899503/) | rBCV biogenesis requires VirB T4SS | In vitro |
| [34423453](https://pubmed.ncbi.nlm.nih.gov/34423453/) | BspF effector–Arf6-Rab8a cascade | In vitro |
| [12414158](https://pubmed.ncbi.nlm.nih.gov/12414158/) | Omp25/TNF-α evasion; protective Th1 response | Human/in vitro review |
| [26376185](https://pubmed.ncbi.nlm.nih.gov/26376185/) | Chronic splenic reservoir cell phenotype | Mouse model |
| [42603185](https://pubmed.ncbi.nlm.nih.gov/42603185/) | Complications, relapse, compliance | Nationwide pediatric cohort |
| [29863218](https://pubmed.ncbi.nlm.nih.gov/29863218/) | Clinical phenotype frequencies; culture yield | 10-year case series |
| [31816580](https://pubmed.ncbi.nlm.nih.gov/31816580/) | Host cytokine susceptibility variants | Meta-analysis |
| [41632803](https://pubmed.ncbi.nlm.nih.gov/41632803/) | Incidence, male predominance, low mortality | Registry (Ningxia) |
| [11910696](https://pubmed.ncbi.nlm.nih.gov/11910696/) | Endocarditis as serious/fatal complication | Case series |
| [36653223](https://pubmed.ncbi.nlm.nih.gov/36653223/) / [26825313](https://pubmed.ncbi.nlm.nih.gov/26825313/) | Rev1 livestock vaccine, control modeling | Vaccine/modeling |
| [41241000](https://pubmed.ncbi.nlm.nih.gov/41241000/) / [40185219](https://pubmed.ncbi.nlm.nih.gov/40185219/) | Acute vs chronic course; prognostic factors | Cohorts |

Most evidence is **human clinical** (cohorts, case series, meta-analyses) and **model organism/in vitro** (mouse, macrophage). No computational-only findings were relied upon for clinical claims.

---

## Limitations and Knowledge Gaps

1. **Host-genetics evidence is early-stage:** susceptibility SNP associations derive from modest case-control studies with heterogeneity; few are validated in independent cohorts or functionally confirmed.
2. **Mechanistic effector work is largely in *B. abortus*/*B. suis* and murine macrophages;** *B. melitensis*-specific effector repertoires and human-cell validation remain incomplete.
3. **No mouse model reproduces the full human syndrome** (undulant fever, osteoarticular disease, endocarditis), limiting translational inference.
4. **Precise global incidence/prevalence for *B. melitensis* specifically** is confounded by under-reporting, serological cross-reactivity, and species-level ambiguity in surveillance.
5. **No human vaccine and no host-directed therapy** are available; optimal antibiotic duration for focal disease is not firmly established.
6. During citation verification, the Ningxia incidence numeric snippet ([PMID: 41632803](https://pubmed.ncbi.nlm.nih.gov/41632803/)) was flagged as a partial mismatch, while the "zero deaths" quote verified cleanly; incidence figures should be treated as approximate pending source re-check.

---

## Proposed Follow-up Experiments / Actions

1. **Validate host-susceptibility SNPs** (IL4, IL18, TNF-238, TGFB1, TLR4) in large, multi-ancestry prospective cohorts with functional (cytokine-response) readouts and stratification by focal complication.
2. **Define the *B. melitensis*-specific T4SS effector–host interactome** in primary human macrophages using proximity labeling and CRISPR host-gene screens ([PMID: 42617139](https://pubmed.ncbi.nlm.nih.gov/42617139/)), prioritizing druggable nodes (Arf6, Rab2, α-enolase, TBK1/NF-κB).
3. **Advance rough-LPS vaccine candidates** (Rev1Δwzm, 16MΔwzm) toward *B. melitensis* challenge efficacy in pregnant ewes and develop a differentiating (DIVA) serodiagnostic ([PMID: 38806353](https://pubmed.ncbi.nlm.nih.gov/38806353/)).
4. **Run adequately-powered RCTs** confirming doxycycline+gentamicin superiority and defining duration for spondylitis/neurobrucellosis/endocarditis ([PMID: 39172763](https://pubmed.ncbi.nlm.nih.gov/39172763/)).
5. **Deploy integrated molecular surveillance** (MLVA + cgSNP) along livestock-trade corridors to track dominant genotypes and guide region-specific vaccination ([PMID: 42093768](https://pubmed.ncbi.nlm.nih.gov/42093768/), [PMID: 42360586](https://pubmed.ncbi.nlm.nih.gov/42360586/)).
6. **Test host-directed adjuncts** (e.g., TBK1/IFN-axis modulation) to accelerate clearance and reduce relapse in chronic disease ([PMID: 41605070](https://pubmed.ncbi.nlm.nih.gov/41605070/)).

---

*Report compiled from 16 confirmed findings across 5 investigation iterations and 53 reviewed papers. Evidence types are distinguished as human clinical, model organism, or in vitro throughout.*


## Artifacts

- [OpenScientist final report](Brucella_Melitensis_Brucellosis-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Brucella_Melitensis_Brucellosis-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 42 |
| On topic | 23 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 29 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0030166` (1 mention) - the report calls it "Frequent"; HP calls it **Night sweats**
- `HP:0003326` (1 mention) - the report calls it "~19% (with fever)"; HP calls it **Myalgia**
- `HP:0001824` (1 mention) - the report calls it "Common (adults > children)"; HP calls it **Weight loss**
- `HP:0100775` (1 mention) - the report calls it "Adults > children (p=0.043)"; HP calls it **Dural ectasia**
- `HP:0003429` (1 mention) - the report calls it "Older adults predominant"; HP calls it **CNS hypomyelination**
- `HP:0002716` (1 mention) - the report calls it "Common"; HP calls it **Lymphadenopathy**
- `HP:0001882` (1 mention) - the report calls it "21% (acute)"; HP calls it **Decreased total leukocyte count**
- `HP:0002910` (1 mention) - the report calls it "44% (acute)"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `GO:0140355` (1 mention) - the report calls it "T4SS-dependent protein secretion into host cell"; GO calls it **cargo receptor ligand activity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006915` (1 mention) - the report calls it "apoptotic process, inhibited"; GO calls it **apoptotic process**
- `GO:0032609` (1 mention) - the report calls it "IFN-γ production"; GO calls it **type II interferon production**, and lists "IFNG production" among its other names
- `GO:0005783` (1 mention) - the report calls it "endoplasmic reticulum — rBCV origin"; GO calls it **endoplasmic reticulum**
- `GO:0005776` (1 mention) - the report calls it "autophagosome — aBCV"; GO calls it **autophagosome**
- `GO:0005768` (1 mention) - the report calls it "endosome — eBCV"; GO calls it **endosome**