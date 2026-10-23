---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-25T09:52:44.308521'
end_time: '2026-09-25T10:16:33.289419'
duration_seconds: 1428.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Erysipelothrix Rhusiopathiae Infectious Disease
  mondo_id: MONDO:0006752
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
citation_count: 16
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:19733019
  relevance_assessed: 16
  on_topic: 13
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 39
  verified: 38
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 9
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0006752
    reported_labels:
    - MONDO
    ontology_label: Erysipelothrix rhusiopathiae infectious disease
  - term_id: HP:0100279
    reported_labels:
    - Tenosynovitis
    ontology_label: Ulcerative colitis
  - term_id: GO:0052126
    reported_labels:
    - "movement in host \u2014 spreading"
    ontology_label: GO_0052126
  - term_id: NCIT:C61785
    reported_labels:
    - Penicillin
    ontology_label: Hydrocortisone Acetate
  - term_id: NCIT:C47616
    reported_labels:
    - Ceftriaxone
    ontology_label: Methyldopa
  - term_id: NCIT:C1281
    reported_labels:
    - Vancomycin
    ontology_label: Biohazardous Substance
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0052126
    ontology_label: GO_0052126
    replaced_by: GO:0044000
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Erysipelothrix_Rhusiopathiae_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Erysipelothrix_Rhusiopathiae_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Erysipelothrix Rhusiopathiae Infectious Disease
- **MONDO ID:** MONDO:0006752 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Erysipelothrix Rhusiopathiae Infectious Disease** covering all of the
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

# Erysipelothrix rhusiopathiae Infectious Disease — Comprehensive Disease Characterization

**Target disease:** Erysipelothrix rhusiopathiae infectious disease
**MONDO ID:** MONDO:0006752 · **ICD-10:** A26 (Erysipeloid) · **MeSH:** D004887 (Erysipeloid) / D004886 (Erysipelothrix Infections)
**Category:** Infectious disease (bacterial zoonosis)

---

## Summary

**Erysipelothrix rhusiopathiae infectious disease is an occupationally acquired bacterial zoonosis caused by the Gram-positive bacillus *Erysipelothrix rhusiopathiae*.** It is not a genetic disease; there are no causal genes, pathogenic variants, or inheritance pattern. The "genetic/molecular" dimension of this entry concerns the *pathogen's* virulence genes and the *host's* predisposing comorbidities rather than germline human variation. Human disease presents in three well-established clinical forms whose severity spans a wide range: (1) a localized cutaneous infection known as **erysipeloid** (the most common form, typically a self-limited hand/finger lesion acquired by direct inoculation), (2) a **diffuse/generalized cutaneous** form, and (3) a rare but dangerous **septicemic** form frequently complicated by **infective endocarditis** with case-fatality exceeding 38%.

Pathogenesis is driven principally by two virulence factors: **surface protective antigen A (SpaA)**, an adhesin of the Spa family, and **neuraminidase**, an enzyme that mediates tissue spread — whereas the capsule and hyaluronidase are *not* required for virulence. Progression from a localized skin lesion to invasive, disseminated disease is strongly gated by host susceptibility, particularly immunocompromising conditions such as diabetes mellitus and alcoholic cirrhosis. The organism is intrinsically **resistant to vancomycin**, an important clinical pitfall, because empiric vancomycin for Gram-positive bacteremia will fail; **penicillin and ceftriaxone are the drugs of choice**, with excellent in-vitro activity.

*E. rhusiopathiae* is a broad-host-range pathogen/commensal of mammals, birds, and fish; **swine erysipelas** is the animal disease of greatest prevalence and economic importance and drives much of the veterinary vaccine effort. Control in humans rests on occupational hygiene (protective gloves, wound care among butchers, fishermen, veterinarians, farmers) and, in animals, on **Spa-family (SpaA/SpaC) subunit and attenuated vaccines**, which are well validated in mouse and pig challenge models. This report consolidates 9 confirmed findings across 23 reviewed papers into a knowledge-base-ready characterization spanning all 15 requested domains, flagging clearly where a domain is not applicable to a non-genetic infectious disease.

---

## 1. Disease Information

*Erysipelothrix rhusiopathiae* infectious disease is a zoonotic bacterial infection of humans acquired occupationally through direct contact with colonized/infected animals, their products or wastes, or contaminated soil and water (including marine environments, where the organism persists long-term).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0006752 |
| ICD-10 | A26 (Erysipeloid); A26.7 (Erysipelothrix sepsis); A26.9 (unspecified) |
| ICD-11 | 1B72 (Erysipeloid) |
| MeSH | D004887 (Erysipeloid); D004886 (Erysipelothrix Infections) |
| NCBI Taxonomy (pathogen) | txid1648 (*Erysipelothrix rhusiopathiae*) |
| OMIM / Orphanet | Not applicable (non-genetic infectious disease) |

**Synonyms / alternative names:** Erysipeloid; erysipeloid of Rosenbach; fish-handler's disease; fish poisoning/"fish hand"; seal finger (overlapping usage); whale finger; Erysipelothrix infection; (in animals) swine erysipelas, "diamond skin disease."

**Source of information:** This entry is derived from **aggregated disease-level resources** — authoritative narrative reviews, microbiological studies, veterinary vaccinology, and individual clinical case reports — rather than from a single EHR/patient-level dataset. Because invasive human disease is rare, much of the clinical literature is case reports and small series.

---

## 2. Etiology

**Disease causal factor:** The disease is **infectious**. The sole etiologic agent is *Erysipelothrix rhusiopathiae*, a small, Gram-positive, non-spore-forming, catalase-negative bacillus. There is no genetic (host germline) causation.

**Risk factors (environmental/occupational):**
- **Occupational exposure** is the dominant risk factor. Two authoritative reviews establish that human infection is acquired via contact with animals, their products/wastes, or soil ([PMID: 19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/); [PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/)). High-risk occupations include butchers, abattoir workers, fishermen and fish handlers, veterinarians, farmers, and poultry/swine workers.
- **Direct skin inoculation** through cuts/abrasions on the hands is the typical portal for erysipeloid ([PMID: 26693283](https://pubmed.ncbi.nlm.nih.gov/26693283/)).
- **Host immunocompromise** predisposes to invasive/systemic disease: documented comorbidities include diabetes mellitus, alcoholic cirrhosis, and chronic alcohol abuse ([PMID: 24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/)).

**Genetic risk factors:** Not applicable — no human susceptibility loci, modifier genes, or causal variants are described for this infection.

**Protective factors:** Behavioral/occupational — protective gloves, hand hygiene, prompt wound care, and (in the animal reservoir) vaccination reduce transmission. No genetic protective variants are relevant.

**Gene–environment interactions:** Not applicable in the human-genetic sense. The functional analogue is **pathogen-genotype × host-status interaction**: virulent bacterial genotypes (SpaA⁺, neuraminidase-high) disseminate preferentially in immunocompromised hosts.

---

## 3. Phenotypes

*E. rhusiopathiae* produces three clinical forms (F001), summarized below with suggested HPO terms.

| Phenotype | Type | Onset / course | Frequency | HPO suggestion |
|---|---|---|---|---|
| **Erysipeloid** (localized violaceous, well-demarcated, painful/pruritic plaque, usually hand/finger; spreads peripherally with central clearing) | Clinical sign / skin manifestation | Acute, days after inoculation; usually self-limited over ~2–4 weeks | Most common form | HP:0000988 (Skin rash); HP:0011368 (Dermatological manifestations); HP:0100659 (Abnormal skin morphology) |
| **Local pain / burning / pruritus** at lesion | Symptom | Acute | Common in erysipeloid | HP:0025280 (Pain); HP:0000989 (Pruritus) |
| **Tenosynovitis of a digit** | Clinical sign (complication of erysipeloid) | Subacute extension | Rare complication | HP:0100279 (Tenosynovitis) |
| **Diffuse / generalized cutaneous** form (widespread violaceous lesions ± systemic symptoms) | Physical manifestation | Subacute | Uncommon | HP:0000989 (Pruritus); HP:0011368 |
| **Septicemia / bacteremia** (fever, malaise) | Clinical sign / lab abnormality | Acute–subacute | Rare | HP:0002837 (Bacteremia); HP:0001945 (Fever) |
| **Infective endocarditis** (often native, previously normal valves; valve destruction; embolic events — stroke, retinal artery occlusion) | Clinical sign / complication | Subacute; high morbidity | Rare but severe | HP:0100584 (Endocarditis); HP:0001635 (Congestive heart failure, from valve destruction); HP:0001297 (Stroke) |
| **Musculoskeletal** (psoas abscess, vertebral osteomyelitis, discitis, pyogenic spondylitis) | Clinical sign / complication | Subacute–chronic | Rare, in immunocompromised | HP:0002754 (Osteomyelitis); HP:0003418 (Back pain) |

**Age of onset:** Adult-onset, reflecting occupational exposure; no congenital form. **Severity:** highly variable — from mild self-limited erysipeloid to lethal endocarditis. **Progression:** erysipeloid is typically self-limited; septicemic/endocarditis forms are progressive and potentially fatal if untreated.

**Quality-of-life impact:** Erysipeloid causes transient local pain/functional impairment of the hand; endocarditis and musculoskeletal disease (spondylitis/discitis) cause substantial morbidity, disability, and mortality.

---

## 4. Genetic / Molecular Information

**Human genetics: Not applicable.** There are no causal human genes, pathogenic variants (ACMG/AMP), modifier genes, epigenetic lesions, or chromosomal abnormalities — this is an infectious disease, not a heritable disorder.

**Pathogen molecular determinants (the relevant "molecular" axis):**

- **SpaA (surface protective antigen A)** — a cell-surface adhesin of the **Spa protein family (SpaA, SpaB, SpaC)**. Comparative proteomic/transcriptomic analysis of a virulent strain (HX130709) versus its isogenic avirulent derivative (HX130709a) — profiling 1,299 proteins and 1,673 transcribed genes, with 168 proteins and 475 genes differentially regulated — confirmed **SpaA and neuraminidase, but not hyaluronidase or capsule**, are associated with virulence (F002; [PMID: 27479071](https://pubmed.ncbi.nlm.nih.gov/27479071/)).
- **Neuraminidase (sialidase)** — an enzyme acting as a **pathogenicity/spreading factor**, confirmed by rabbit skin test; substrate affinity increases with glycoprotein molecular weight (F002; [PMID: 16869504](https://pubmed.ncbi.nlm.nih.gov/16869504/)).
- **Spa family classification:** SpaA, SpaB, SpaC, with **SpaC the most broadly cross-protective antigen** (F006; [PMID: 20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/)).

**Epigenetics / chromosomal abnormalities:** Not applicable.

---

## 5. Environmental Information

- **Environmental reservoir/persistence:** The organism persists long-term in the environment, including soil and marine locations, and is a commensal/pathogen across many animal species (F005; [PMID: 19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/)).
- **Occupational/lifestyle factors:** animal handling, fishing/fish processing, butchery, veterinary work; chronic alcohol use is both a lifestyle factor and an immunocompromising comorbidity contributing to invasive disease ([PMID: 24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/)).
- **Infectious agent (taxonomy):** *Erysipelothrix rhusiopathiae* (NCBI txid1648), family *Erysipelotrichaceae*. A related species, *E. piscisicarius*, is relevant to fish and to identification challenges ([PMID: 42670169](https://pubmed.ncbi.nlm.nih.gov/42670169/)).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Occupational contact** with a colonized/infected animal, its products/wastes, or contaminated soil/water **leads to** deposition of *E. rhusiopathiae* on the skin (F001, F008).
2. **Direct inoculation through a cut/abrasion** (usually hand/finger) **results in** entry of the bacterium into the deep dermis, where it resides (F008; [PMID: 26693283](https://pubmed.ncbi.nlm.nih.gov/26693283/), [PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/)).
3. **SpaA-mediated adhesion** to host tissue **promotes** local colonization (F002, F006) — *inferred* from virulence-factor association plus vaccine-protection data.
4. **Neuraminidase (sialidase) cleaves sialic acid** from host glycoproteins, **facilitating** tissue spreading and local invasion (F002; confirmed by rabbit skin test, [PMID: 16869504](https://pubmed.ncbi.nlm.nih.gov/16869504/)).
5. Local spread **produces** the characteristic **erysipeloid** plaque; peripheral extension can **lead to** **tenosynovitis** of the digit (F008; [PMID: 26693283](https://pubmed.ncbi.nlm.nih.gov/26693283/)).

   **↳ Branch A (contained):** In immunocompetent hosts the infection remains localized and is typically self-limited.

   **↳ Branch B (dissemination):** In immunocompromised hosts (diabetes, alcoholic cirrhosis), local containment fails.
6. **Host immunocompromise permits** breach into the bloodstream **→ bacteremia/septicemia** (F007; [PMID: 24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/)).
7. Circulating bacteria **seed heart valves** (often native, previously normal) **→ infective endocarditis** with vegetations (F004).
8. Valve colonization **causes extensive valve destruction** and **generates septic emboli** **→** stroke, retinal artery occlusion, and heart failure (F004; [PMID: 40619580](https://pubmed.ncbi.nlm.nih.gov/40619580/), [PMID: 40087746](https://pubmed.ncbi.nlm.nih.gov/40087746/)).
9. Alternatively, hematogenous seeding of the axial skeleton **→ psoas abscess, vertebral osteomyelitis, discitis, pyogenic spondylitis** (F007; [PMID: 24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/), [PMID: 41111798](https://pubmed.ncbi.nlm.nih.gov/41111798/)).
10. Despite low intrinsic virulence, endocarditis **results in** high case-fatality (>38%); low virulence explains the *rarity* of intracranial (embolic) manifestations relative to more aggressive organisms (F004; [PMID: 40619580](https://pubmed.ncbi.nlm.nih.gov/40619580/)).

```
 Occupational exposure
        │  (skin inoculation)
        ▼
  Deep dermal entry ──SpaA adhesion──► local colonization
        │
        │  neuraminidase (sialidase) → tissue spreading
        ▼
   ERYSIPELOID  ──►  tenosynovitis (rare)
        │
        ├──[immunocompetent]──► self-limited / contained
        │
        └──[immunocompromised: diabetes, alcoholic cirrhosis]
                 │
                 ▼
            BACTEREMIA / SEPTICEMIA
                 ├──► ENDOCARDITIS ─► valve destruction ─► emboli (stroke, RAO), heart failure  (mortality >38%)
                 └──► axial seeding ─► psoas abscess / vertebral osteomyelitis / spondylitis
```

**Upstream vs downstream:** Adhesion (SpaA) and enzymatic spreading (neuraminidase) are **upstream**; septicemia, valve destruction, and embolic organ injury are **downstream**. Host immune status is the pivotal **gate** determining which branch is taken.

**Cell types / processes involved:** keratinocytes/dermal fibroblasts and dermis (erysipeloid); vascular endothelium and cardiac valve endothelium (endocarditis); neutrophil-driven inflammation and abscess formation (musculoskeletal disease). Suggested GO terms: GO:0007155 (cell adhesion), GO:0006954 (inflammatory response), GO:0052126 (movement in host — spreading), GO:0016997 (exo-α-sialidase activity), GO:0044409 (entry into host). Suggested CL terms: CL:0000312 (keratinocyte), CL:0000115 (endothelial cell), CL:0000775 (neutrophil).

**Molecular pathways / metabolic changes / omics:** No canonical human signaling pathway (Wnt/MAPK/mTOR) is implicated. The relevant molecular biology is bacterial (adhesin display, sialidase activity). The comparative proteomic/transcriptomic study (F002) is the key omics dataset, revealing a differentially regulated virulence repertoire.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin — especially hands/fingers (erysipeloid). UBERON:0002097 (skin of body); UBERON:0002389 (manual digit).
- **Secondary (invasive disease):** Heart valves (endocarditis; UBERON:0000946 cardiac valve, UBERON:0002135 mitral valve, UBERON:0002137 aortic valve); vertebral column / intervertebral disc (UBERON:0002228 vertebra; UBERON:0002103 intervertebral disc); psoas muscle (UBERON:0001096); brain vasculature and retina via emboli (UBERON:0000178 blood; UBERON:0000966 retina).
- **Body systems:** integumentary, cardiovascular, musculoskeletal, and (secondarily, via emboli) nervous and visual systems.

**Tissue/cell level:** epithelial/dermal tissue (skin), endothelial tissue (valves, vessels), connective/bone tissue (spondylitis). CL:0000312 (keratinocyte), CL:0000115 (endothelial cell), CL:0000062 (osteoblast, in osteomyelitis).

**Subcellular level:** Host cell-surface sialylated glycoproteins are the substrate of bacterial neuraminidase. GO cellular component: GO:0009986 (cell surface); GO:0005886 (plasma membrane).

**Lateralization:** Erysipeloid is typically **unilateral** (site of inoculation, usually dominant hand); endocarditis/embolic events may be **bilateral** (e.g., bilateral retinal artery occlusion reported — [PMID: 40087746](https://pubmed.ncbi.nlm.nih.gov/40087746/)).

---

## 8. Temporal Development

- **Onset:** Adult-onset (occupational); **acute** for erysipeloid (days after inoculation); **subacute** for endocarditis and musculoskeletal disease.
- **Progression / course:** Erysipeloid is usually **self-limited** (resolves over weeks, faster with antibiotics). The septicemic/endocarditis form is **progressive** and, untreated, potentially fatal; it frequently causes valve destruction (F004). Musculoskeletal disease (spondylitis/discitis) follows a **subacute-to-chronic** course.
- **Remission:** Erysipeloid may remit spontaneously; invasive forms require treatment-induced remission (antibiotics ± surgery).
- **Critical periods / windows of intervention:** Early recognition is crucial — because the organism is **intrinsically vancomycin-resistant**, empiric vancomycin fails, so timely correct identification and penicillin therapy is the key intervention window (F003; [PMID: 12408347](https://pubmed.ncbi.nlm.nih.gov/12408347/)).

---

## 9. Inheritance and Population

**Inheritance:** Not applicable — infectious, non-heritable. No penetrance, expressivity, anticipation, mosaicism, founder effects, consanguinity, or carrier frequency considerations apply.

**Epidemiology:** Human invasive disease is **rare**; endocarditis and systemic infection are reported chiefly as case reports/series. Precise population incidence/prevalence figures are not well established because the disease is uncommon and under-reported; erysipeloid is more frequent but often self-treated and undocumented.

**Population demographics:**
- **Occupational groups** (butchers, fishermen, fish handlers, veterinarians, farmers, abattoir/poultry workers) are the affected population — an occupational rather than ethnic distribution.
- **Sex ratio:** Male predominance is expected given occupational exposure patterns (not precisely quantified in the reviewed evidence).
- **Age:** Adults of working age.
- **Geographic distribution:** Worldwide, wherever animal husbandry, fishing, and meat processing occur; the organism persists in soil and marine environments globally (F005).

---

## 10. Diagnostics

**Microbiological identification (diagnostic signature — F009):** Clinical isolates are **Gram-positive pleomorphic rods**, **catalase-negative and oxidase-negative**, PYR-positive, LAP-positive, alpha-hemolytic, and characteristically **produce H₂S in triple sugar iron (TSI) agar** ([PMID: 16178460](https://pubmed.ncbi.nlm.nih.gov/16178460/)). **Intrinsic vancomycin resistance** is a practical identification clue (one of few vancomycin-resistant Gram-positive rods) that simultaneously mandates a therapy change.

| Test | Result for *E. rhusiopathiae* | Diagnostic value |
|---|---|---|
| Gram stain | Gram-positive slender/pleomorphic rod | Screening |
| Catalase | Negative | Distinguishes from *Corynebacterium* |
| Oxidase | Negative | Supportive |
| H₂S in TSI | **Positive** (characteristic) | Key differentiator ([PMID: 16178460](https://pubmed.ncbi.nlm.nih.gov/16178460/)) |
| Hemolysis (blood agar) | Alpha (greening) | Supportive |
| Vancomycin | **Resistant** (MIC90 64 mg/L) | Clue + therapy trigger ([PMID: 12408347](https://pubmed.ncbi.nlm.nih.gov/12408347/)) |

**Molecular diagnostics:** **16S rDNA sequencing lacks resolution to distinguish among *Erysipelothrix* species**; **long-read (Oxford Nanopore) direct sequencing of clinical tissue** can accurately identify species where MALDI-TOF and 16S misassign them (F009; [PMID: 42670169](https://pubmed.ncbi.nlm.nih.gov/42670169/)).

**Imaging / functional tests (invasive disease):** Echocardiography (transthoracic/transesophageal) for vegetations and valve destruction in suspected endocarditis; MRI/CT for spondylitis, discitis, and psoas abscess; fundoscopy for embolic retinal artery occlusion.

**Blood cultures** are the mainstay for septicemic/endocarditis diagnosis. Erysipeloid diagnosis is often **clinical**, because culture is slow and the organism resides deep in the skin, contributing to under-diagnosis ([PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/)).

**Differential diagnosis:** cellulitis/erysipelas (streptococcal), other bacterial hand infections, **erysipeloid cutaneous leishmaniasis** (an unrelated dermatologic mimic sharing the "erysipeloid" descriptor — [PMID: 35609142](https://pubmed.ncbi.nlm.nih.gov/35609142/)), and other Gram-positive-rod bacteremias (*Listeria*, *Corynebacterium*, *Lactobacillus*).

**Genetic testing / newborn screening / omics diagnostics:** Not applicable to a non-genetic infection (beyond pathogen sequencing above).

---

## 11. Outcome / Prognosis

- **Erysipeloid:** Excellent prognosis; usually self-limited and fully recovers, faster with penicillin.
- **Endocarditis / septicemic form:** **Poor** — mortality can **exceed 38% even with appropriate treatment**, with frequent extensive valve destruction (F004; [PMID: 40619580](https://pubmed.ncbi.nlm.nih.gov/40619580/)). Because it often affects native/previously normal valves, valve replacement may be required.
- **Embolic complications:** stroke and (bilateral) retinal artery occlusion are recognized ([PMID: 40619580](https://pubmed.ncbi.nlm.nih.gov/40619580/), [PMID: 40087746](https://pubmed.ncbi.nlm.nih.gov/40087746/)); the organism's **low virulence** paradoxically makes intracranial embolic manifestations *uncommon* relative to more aggressive pathogens (F004).
- **Musculoskeletal disease:** Recoverable with prolonged antibiotics ± drainage, but under-recognized and can cause lasting spinal morbidity ([PMID: 24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/), [PMID: 41111798](https://pubmed.ncbi.nlm.nih.gov/41111798/)).

**Prognostic factors:** host immune status (diabetes, cirrhosis, alcohol use worsen outcomes), timeliness of correct diagnosis (avoiding vancomycin failure), valvular involvement, and embolic events.

---

## 12. Treatment

**Pharmacotherapy (first-line):** **Penicillin is the drug of choice**; ceftriaxone is an effective alternative. Agar-dilution testing of 60 isolates showed penicillin and ceftriaxone highly active (MIC90 0.03 and 0.125 mg/L) and ciprofloxacin very active (MIC90 0.06 mg/L) (F003; [PMID: 12408347](https://pubmed.ncbi.nlm.nih.gov/12408347/)).

**Critical caveat — intrinsic vancomycin resistance:** The organism is **resistant to vancomycin (MIC90 64 mg/L)** and to gentamicin in reported cases — so standard empiric therapy for Gram-positive bacteremia/endocarditis (vancomycin ± aminoglycoside) will fail (F003; [PMID: 12408347](https://pubmed.ncbi.nlm.nih.gov/12408347/), [PMID: 16178460](https://pubmed.ncbi.nlm.nih.gov/16178460/)). Early species identification is therefore therapeutically decisive.

| Agent | Activity | Role | NCIT suggestion |
|---|---|---|---|
| Penicillin G | MIC90 0.03 mg/L | First-line | NCIT:C61785 (Penicillin) |
| Ceftriaxone | MIC90 0.125 mg/L | Alternative / severe disease | NCIT:C47616 (Ceftriaxone) |
| Ciprofloxacin | MIC90 0.06 mg/L | Alternative | NCIT:C376 (Ciprofloxacin) |
| Vancomycin | MIC90 64 mg/L (**resistant**) | **Avoid** | NCIT:C1281 (Vancomycin) |

**Surgical/interventional:** Valve replacement for destructive endocarditis; drainage of psoas abscess and surgical management of vertebral osteomyelitis/discitis when indicated.

**Supportive care:** wound care for erysipeloid; standard sepsis/endocarditis supportive management for invasive disease.

**Pharmacogenomics / gene / cell / RNA / immunotherapy:** Not applicable to this bacterial infection.

---

## 13. Prevention

**Primary prevention (human):** Occupational hygiene — protective gloves, prompt cleaning/care of cuts and abrasions, and safe handling of animals/fish/meat. No licensed human vaccine exists.

**Primary prevention (animal reservoir — One Health):** **Spa-family vaccines** are the cornerstone of controlling the swine reservoir, indirectly reducing human exposure. Spa proteins comprise SpaA/SpaB/SpaC, with **SpaC the most broadly cross-protective**; mice immunized with rSpaC664 or its N-terminal α-helical domain (rSpaC427) — but not the C-terminal domain — were protected against challenge with serovars 1a, 2, 6, 19, and 18, and **pigs immunized with SpaC427 were protected against the highly virulent heterologous strain Fujisawa (serovar 1a)** (F006; [PMID: 20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/)). Passive transfer of anti-rSpaC427 serum protected mice (antibody-mediated protection). A recombinant **DnaK+SpaA** formulation also conferred protection and delayed symptoms in a swine-erysipelas model (F006; [PMID: 37815427](https://pubmed.ncbi.nlm.nih.gov/37815427/)).

**Secondary/tertiary prevention:** Early recognition of erysipeloid and prompt penicillin to prevent progression; timely correct microbiological identification to avoid vancomycin failure in invasive disease; endocarditis prophylaxis considerations in high-risk hosts.

**Public health / environmental interventions:** Herd vaccination, animal husbandry hygiene, carcass/waste management, and worker education in high-risk industries.

---

## 14. Other Species / Natural Disease

*E. rhusiopathiae* is a genuine **broad-host-range zoonotic pathogen** and the veterinary burden dwarfs the human one.

- **Taxonomy of affected hosts:** swine (*Sus scrofa*), turkeys, chickens, ducks, emus, sheep/lambs, plus many wild and domestic mammals, birds, and fish; the bacterium is a "pathogen or commensal in a wide variety of wild and domestic animals, birds and fish" (F005; [PMID: 19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/)).
- **Principal animal disease:** **Swine erysipelas** — the disease "of greatest prevalence and economic importance" (F005; [PMID: 19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/)). Manifestations include acute septicemia, characteristic "diamond skin" urticarial lesions, chronic arthritis, and endocarditis in pigs. Other diseases: **erysipelas of farmed turkeys, chickens, ducks, and emus**, and **polyarthritis in sheep and lambs** ([PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/)).
- **Comparative pathology:** Human endocarditis and animal (porcine) endocarditis/arthritis share virulence mechanisms (Spa adhesins, neuraminidase), enabling shared vaccine antigens across species.
- **Zoonotic potential:** High — human disease is a direct zoonosis from animal contact; related species *E. piscisicarius* affects fish and complicates identification ([PMID: 42670169](https://pubmed.ncbi.nlm.nih.gov/42670169/)).

---

## 15. Model Organisms

- **Mouse model:** The workhorse for vaccine/immunogenicity studies. Active immunization with rSpaC664/rSpaC427 protected mice against multi-serovar challenge; passive serum transfer confirmed antibody-mediated protection (F006; [PMID: 20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/)).
- **Pig (natural host) challenge model:** Pigs immunized with SpaC427 were protected against the highly virulent heterologous strain **Fujisawa** — a model that faithfully recapitulates the natural disease and is the gold standard for swine-erysipelas vaccine evaluation (F006; [PMID: 20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/), [PMID: 37815427](https://pubmed.ncbi.nlm.nih.gov/37815427/)).
- **Rabbit skin test:** Used to demonstrate the spreading/pathogenicity function of neuraminidase in vivo (F002; [PMID: 16869504](https://pubmed.ncbi.nlm.nih.gov/16869504/)).
- **Isogenic bacterial strain pair:** Virulent HX130709 vs avirulent HX130709a enabled comparative omics that pinpointed SpaA/neuraminidase as virulence factors (F002; [PMID: 27479071](https://pubmed.ncbi.nlm.nih.gov/27479071/)).

**Phenotype recapitulation:** Mouse and especially pig challenge models reproduce protective immunity and lethal challenge well. **Limitation:** models focus on vaccine protection and swine disease; the sporadic, host-status-gated *human* invasive endocarditis is not modeled directly, and no dedicated model captures the human immunocompromised-host dissemination pathway.

---

## Key Findings (with statistical evidence)

### F001 — Three clinical forms; erysipeloid is most common
Two authoritative reviews independently enumerate three recognized human disease forms: localized cutaneous **erysipeloid** (most common), a **diffuse/generalized cutaneous** form, and a **septicemic** form frequently associated with **endocarditis**. Human infection is occupationally acquired via animal/product/waste/soil contact. *"Three forms of human disease have been recognised... a localised cutaneous lesion form, erysipeloid, a generalised cutaneous form and a septicaemic form often associated with endocarditis"* ([PMID: 19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/)); corroborated by [PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/).

### F002 — SpaA and neuraminidase are the key virulence factors (not capsule or hyaluronidase)
Comparative proteomic/transcriptomic analysis of virulent HX130709 vs isogenic avirulent HX130709a (1,299 proteins; 1,673 transcribed genes; 168 proteins and 475 genes differentially regulated) confirmed **SpaA and neuraminidase — but not hyaluronidase or capsule — are associated with virulence**: *"Our study confirms that SpaA and neuraminidase, but not hyaluronidase and capsule, are associated with virulence in E. rhusiopathiae"* ([PMID: 27479071](https://pubmed.ncbi.nlm.nih.gov/27479071/)). Neuraminidase's spreading role was confirmed by rabbit skin test ([PMID: 16869504](https://pubmed.ncbi.nlm.nih.gov/16869504/)).

### F003 — Intrinsic vancomycin resistance; penicillin is first-line
Agar-dilution testing of 60 isolates: penicillin/ceftriaxone highly active (MIC90 0.03 / 0.125 mg/L), ciprofloxacin very active (MIC90 0.06 mg/L), **vancomycin resistant (MIC90 64 mg/L)**. *"Erysipelothrix rhusiopathiae is still resistant to vancomycin (MIC90 64 mg/l)"* and *"Penicillin and ceftriaxone... remained active"* ([PMID: 12408347](https://pubmed.ncbi.nlm.nih.gov/12408347/)).

### F004 — Endocarditis: low-virulence organism, high mortality (~38%)
*"Even with appropriate treatment, mortality from endocarditis associated with E. rhusiopathiae can exceed 38%"* and *"The low virulence of the E. rhusiopathiae pathogen explains the minimal frequency of intracranial manifestations"* ([PMID: 40619580](https://pubmed.ncbi.nlm.nih.gov/40619580/)). Frequent valve destruction; embolic events reported.

### F005 — Broad host range; swine erysipelas is the most economically important animal disease
*"It is a pathogen or a commensal in a wide variety of wild and domestic animals, birds and fish. Swine erysipelas... is the disease of greatest prevalence and economic importance"* ([PMID: 19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/)); also affects turkeys, chickens, ducks, emus, sheep ([PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/)).

### F006 — Spa family (SpaA/B/C) underpins vaccines; mouse and pig models validate protection
*"...Spa proteins... can be classified into three molecular species — SpaA, SpaB, and SpaC — and... SpaC is the most broadly cross-protective"*; *"Pigs immunized with SpaC427... were protected from challenge with the highly virulent heterologous E. rhusiopathiae strain Fujisawa (serovar 1a)"* ([PMID: 20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/)). DnaK+SpaA also protective ([PMID: 37815427](https://pubmed.ncbi.nlm.nih.gov/37815427/)).

### F007 — Host immunocompromise predisposes to invasive disease
Invasive bacteremia with psoas abscess, vertebral osteomyelitis and discitis (L2–L3) in a patient with diabetes mellitus and alcoholic cirrhosis: *"He had underlying diabetes mellitus and alcoholic cirrhosis"* and *"Erysipelothrix infection should be considered as a causative pathogen of musculoskeletal infection in immunocompromised patients"* ([PMID: 24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/)).

### F008 — Erysipeloid is a localized, direct-inoculation hand/finger infection that can extend to tenosynovitis
*"Erysipelothrix rhusiopathiae is a Gram-positive bacterium that in humans causes skin infections, such as erysipeloid, as a result of direct contact with contaminated animals or their waste or products"* ([PMID: 26693283](https://pubmed.ncbi.nlm.nih.gov/26693283/)). Deep-skin residence complicates culture ([PMID: 10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/)).

### F009 — Diagnostic signature: catalase/oxidase-negative Gram-positive rod, H₂S-positive in TSI, vancomycin-resistant
*"...the production of H2S in triple sugar iron agar, was demonstrated"* ([PMID: 16178460](https://pubmed.ncbi.nlm.nih.gov/16178460/)); *"16S rDNA sequencing lacks sufficient resolution to differentiate among Erysipelothrix species"* ([PMID: 42670169](https://pubmed.ncbi.nlm.nih.gov/42670169/)).

---

## Mechanistic Model / Interpretation

The disease is best understood as a **two-stage, host-gated process**. Stage 1 is **local**: after occupational inoculation, the bacterium exploits **SpaA-mediated adhesion** and **neuraminidase-mediated sialic-acid cleavage/spreading** to establish an erysipeloid plaque in the deep dermis. This stage is typically self-limiting in immunocompetent hosts. Stage 2 is **invasive** and occurs primarily when host defenses are compromised (diabetes, alcoholic cirrhosis): the same virulence machinery permits **bloodstream invasion**, followed by **valve seeding (endocarditis)** or **axial skeletal seeding (spondylitis/discitis/psoas abscess)**. The paradox of a "low-virulence" organism causing >38% endocarditis mortality is resolved by noting that low virulence limits *embolic aggressiveness* (fewer intracranial events) while chronic valve colonization still produces lethal *structural* valve destruction. Clinically, the single most consequential mechanistic fact is **intrinsic vancomycin resistance**: the standard empiric Gram-positive regimen is ineffective, so the diagnostic signature (catalase/oxidase-negative rod, H₂S-positive TSI, vancomycin-resistant) must be recognized quickly to switch to penicillin.

---

## Evidence Base

| PMID | Type | Supports |
|---|---|---|
| [19733019](https://pubmed.ncbi.nlm.nih.gov/19733019/) | Review | Three clinical forms; broad host range; swine erysipelas (F001, F005) |
| [10482289](https://pubmed.ncbi.nlm.nih.gov/10482289/) | Review | Three forms; affected animals; deep-skin diagnostic difficulty (F001, F005, F008) |
| [27479071](https://pubmed.ncbi.nlm.nih.gov/27479071/) | Comparative omics (isogenic strains) | SpaA/neuraminidase = virulence; capsule/hyaluronidase not (F002) |
| [16869504](https://pubmed.ncbi.nlm.nih.gov/16869504/) | Enzymology + rabbit skin test | Neuraminidase as spreading/pathogenicity factor (F002) |
| [12408347](https://pubmed.ncbi.nlm.nih.gov/12408347/) | Susceptibility study (60 isolates) | Vancomycin resistance; penicillin/ceftriaxone first-line (F003) |
| [40619580](https://pubmed.ncbi.nlm.nih.gov/40619580/) | Case report/review | Endocarditis mortality >38%; low-virulence paradox (F004) |
| [20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/) | Vaccinology (mouse + pig) | Spa family; SpaC cross-protection; pig challenge (F006) |
| [37815427](https://pubmed.ncbi.nlm.nih.gov/37815427/) | Vaccinology (swine model) | DnaK+SpaA protection (F006) |
| [24772603](https://pubmed.ncbi.nlm.nih.gov/24772603/) | Case report | Immunocompromise → invasive musculoskeletal disease (F007) |
| [26693283](https://pubmed.ncbi.nlm.nih.gov/26693283/) | Case report/review | Erysipeloid = direct inoculation; tenosynovitis (F008) |
| [16178460](https://pubmed.ncbi.nlm.nih.gov/16178460/) | Case report | H₂S-in-TSI; vancomycin/gentamicin resistance (F009, F003) |
| [42670169](https://pubmed.ncbi.nlm.nih.gov/42670169/) | Genomics (Nanopore) | 16S limitation; long-read identification (F009) |
| [40087746](https://pubmed.ncbi.nlm.nih.gov/40087746/) | Case report | Bilateral retinal artery occlusion / embolic endocarditis |
| [41111798](https://pubmed.ncbi.nlm.nih.gov/41111798/) | Case report | Pyogenic spondylitis (zoonotic) |

**Challenging / confounding literature:** Several retrieved papers on *"erysipeloid cutaneous leishmaniasis"* ([PMID: 35609142](https://pubmed.ncbi.nlm.nih.gov/35609142/), [PMID: 33236713](https://pubmed.ncbi.nlm.nih.gov/33236713/)) describe an unrelated *Leishmania* dermatologic entity that merely shares the "erysipeloid" descriptor — a useful reminder for differential diagnosis but not evidence about *E. rhusiopathiae*.

---

## Limitations and Knowledge Gaps

- **Rare-disease evidence base:** Human invasive disease evidence is dominated by case reports; there are **no controlled human incidence/prevalence or mortality datasets**, so epidemiologic figures (except the ~38% endocarditis case-fatality) and sex/age ratios are imprecise.
- **Not a genetic disease:** Sections on causal genes, pathogenic variants, inheritance, penetrance, epigenetics, and newborn/genetic screening are **not applicable**; the "molecular" content is pathogen biology.
- **Host-susceptibility mechanism unquantified:** The dissemination "gate" is described qualitatively (diabetes, cirrhosis, alcohol) without a quantified relative risk or mechanistic immunology.
- **SpaA adhesion step is inferred:** SpaA's causal role rests on virulence-association and vaccine-protection data rather than a direct receptor-binding demonstration in human tissue.
- **No human vaccine:** Vaccine evidence is entirely veterinary (mouse/pig); translation to humans is untested and likely unnecessary given rarity.
- **Identification pitfalls:** MALDI-TOF and 16S can misassign *Erysipelothrix* species; species-level epidemiology (*E. rhusiopathiae* vs *E. piscisicarius*) may be under-resolved in older literature.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify host-susceptibility risk:** Systematic review/meta-analysis of invasive-disease case reports to estimate the association between diabetes/alcoholic cirrhosis and dissemination, and to refine the endocarditis case-fatality estimate.
2. **Define SpaA/neuraminidase mechanism directly:** Identify the human host receptor(s) for SpaA and map neuraminidase substrate specificity on cardiac valve endothelium; test isogenic *spaA* and *nanH* knockouts in an endocarditis model.
3. **Improve species-level diagnostics:** Prospectively benchmark long-read (Nanopore) direct-from-tissue sequencing vs MALDI-TOF/16S for *Erysipelothrix* species assignment ([PMID: 42670169](https://pubmed.ncbi.nlm.nih.gov/42670169/)) and disseminate a rapid "vancomycin-resistant Gram-positive rod → suspect *Erysipelothrix* → start penicillin" clinical alert.
4. **Optimize One-Health vaccines:** Extend SpaC-based cross-serovar protection studies ([PMID: 20926696](https://pubmed.ncbi.nlm.nih.gov/20926696/)) and DnaK+SpaA formulations ([PMID: 37815427](https://pubmed.ncbi.nlm.nih.gov/37815427/)) to broader field serovars to reduce the swine reservoir and, indirectly, human exposure.
5. **Occupational surveillance:** Establish targeted reporting in high-risk industries (abattoirs, fisheries, veterinary) to generate the missing incidence data.

---

*Report compiled from 9 confirmed findings across 23 reviewed papers over 5 investigation iterations. Evidence types span authoritative reviews, comparative bacterial omics, susceptibility testing, veterinary vaccinology (mouse and pig models), and human clinical case reports.*


## Artifacts

- [OpenScientist final report](Erysipelothrix_Rhusiopathiae_Infectious_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Erysipelothrix_Rhusiopathiae_Infectious_Disease-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19733019` *(abstract only)*: "pathogen or commensal in a wide variety of wild and domestic animals, birds and fish"
  - closest text in source: "It is a pathogen or a commensal in a wide variety of wild and domestic animals, birds and fish"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 19 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0006752` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Erysipelothrix rhusiopathiae infectious disease**
- `HP:0100279` (1 mention) - the report calls it "Tenosynovitis"; HP calls it **Ulcerative colitis**
- `GO:0052126` (1 mention) - the report calls it "movement in host — spreading"; GO calls it **GO_0052126**
- `NCIT:C61785` (1 mention) - the report calls it "Penicillin"; NCIT calls it **Hydrocortisone Acetate**
- `NCIT:C47616` (1 mention) - the report calls it "Ceftriaxone"; NCIT calls it **Methyldopa**
- `NCIT:C1281` (1 mention) - the report calls it "Vancomycin"; NCIT calls it **Biohazardous Substance**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0052126` (GO_0052126) (1 mention) - replaced by `GO:0044000`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016997` (1 mention) - the report calls it "exo-α-sialidase activity"; GO calls it **alpha-sialidase activity**
- `GO:0044409` (1 mention) - the report calls it "entry into host"; GO calls it **symbiont entry into host**, and lists "entry into host" among its other names
- `CL:0000062` (1 mention) - the report calls it "osteoblast, in osteomyelitis"; CL calls it **osteoblast**
- `NCIT:C376` (1 mention) - the report calls it "Ciprofloxacin"; NCIT calls it **Cisplatin**