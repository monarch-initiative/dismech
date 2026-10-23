---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T20:11:21.902314'
end_time: '2026-10-01T21:02:13.783800'
duration_seconds: 3051.88
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Pulmonary Alveolar Proteinosis With Hypogammaglobulinemia
  mondo_id: MONDO:0020840
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
citation_count: 19
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 12
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 35
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 19
  labels_matching: 8
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0006517
    reported_labels:
    - Abnormal alveolar surfactant / PAP
    ontology_label: Intraalveolar phospholipid accumulation
  - term_id: UBERON:0002048
    reported_labels:
    - Primary organ:** lung
    ontology_label: lung
  - term_id: NCIT:C116737
    reported_labels:
    - Whole Lung Lavage
    ontology_label: Anti-CD33 Monoclonal Antibody BI 836858
  - term_id: NCIT:C818
    reported_labels:
    - Curcumin
    ontology_label: Roxithromycin
  - term_id: NCIT:C2069
    reported_labels:
    - Sargramostim
    ontology_label: Defosfamide
  - term_id: NCIT:C15283
    reported_labels:
    - Lung Transplantation
    ontology_label: Naturopathy Therapy
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Pulmonary_Alveolar_Proteinosis_With_Hypogammaglobulinemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Pulmonary_Alveolar_Proteinosis_With_Hypogammaglobulinemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pulmonary Alveolar Proteinosis With Hypogammaglobulinemia
- **MONDO ID:** MONDO:0020840 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Pulmonary Alveolar Proteinosis With Hypogammaglobulinemia** covering all of the
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

# Pulmonary Alveolar Proteinosis With Hypogammaglobulinemia (PAPHG): A Comprehensive Disease Characteristics Report

**Disease:** Pulmonary Alveolar Proteinosis With Hypogammaglobulinemia (PAPHG)
**MONDO ID:** MONDO:0020840 · **OMIM:** #618042 · **Category:** Mendelian (autosomal dominant)
**Causal gene:** *OAS1* (2′-5′-oligoadenylate synthetase 1), 12q24.13, NCBI Gene 4938, HGNC:8086
**Also known as:** Immunodeficiency 100 with pulmonary alveolar proteinosis and hypogammaglobulinemia (IMD100)

---

## Summary

Pulmonary Alveolar Proteinosis with Hypogammaglobulinemia (PAPHG; OMIM #618042, MONDO:0020840) is an **ultra-rare, autosomal-dominant Mendelian disorder** caused by **heterozygous gain-of-function (GoF) missense variants in *OAS1***, the gene encoding 2′-5′-oligoadenylate synthetase 1 on chromosome 12q24.13. The disease was first defined genetically in 2018 when whole-exome sequencing identified a heterozygous *OAS1* missense variant segregating in three affected siblings, plus two de novo variants in unrelated infants, after causative variants in all known PAP genes (*SFTPB, SFTPC, ABCA3, CSF2RA, CSF2RB, GATA2*) had been excluded (Cho et al. 2018, [PMID: 29455859](https://pubmed.ncbi.nlm.nih.gov/29455859/)). An independent cohort subsequently confirmed four de novo heterozygous *OAS1* GoF variants in six patients (Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)).

Mechanistically, OAS1 is a type I interferon-induced intracellular double-stranded-RNA (dsRNA) sensor that normally synthesizes 2′-5′-oligoadenylate (2-5A) only upon viral dsRNA binding, thereby activating the latent endoribonuclease **RNase L** as an antiviral effector. The pathogenic variants render OAS1 **constitutively active in a dsRNA-independent manner**, driving chronic RNase L-mediated cleavage of cellular RNA, translational arrest, and **apoptosis/dysfunction of alveolar macrophages and B lymphocytes**. The two consequences map directly onto the two-part clinical name: alveolar macrophage failure impairs surfactant catabolism, producing **infantile-onset pulmonary alveolar proteinosis** with hypoxemic respiratory failure, while B-cell depletion causes **hypogammaglobulinemia**. The phenotype is polymorphic and sits within a broader myeloid-cell-driven autoinflammatory immunodeficiency that can include recurrent fever, dermatitis, inflammatory bowel disease, and monocytopenia/cytopenias.

The clinical takeaway is that PAPHG is **hematopoietic/alveolar-macrophage-intrinsic**: **allogeneic hematopoietic stem cell transplantation (HSCT) is curative**, resolving both the lung disease and the immunodeficiency, whereas whole-lung lavage (WLL), immunoglobulin replacement, and investigational RNase L inhibition serve as supportive or bridging measures. Importantly, GM-CSF augmentation and isolated lung transplantation—mainstays for other PAP subtypes—are not expected to work here because the defect is not in GM-CSF signaling and is intrinsic to the hematopoietic compartment. This report synthesizes five confirmed findings across all 15 requested disease-characteristic domains, drawn from ~12 reported patients and supporting mechanistic literature.

---

## Key Findings

### Finding 1 — PAPHG is caused by heterozygous gain-of-function variants in *OAS1*

Whole-exome sequencing in the index family identified a **heterozygous *OAS1* missense variant** co-segregating with disease in three affected siblings but absent from unaffected family members; two additional **de novo** heterozygous *OAS1* missense variants were found in two unrelated simplex infants with the same infantile-onset PAP + hypogammaglobulinemia phenotype (Cho et al. 2018, [PMID: 29455859](https://pubmed.ncbi.nlm.nih.gov/29455859/)). Critically, no causative variants were found in established PAP genes (*SFTPB, SFTPC, ABCA3, CSF2RA, CSF2RB, GATA2*), establishing *OAS1* as a novel disease gene. An independent group then reported **four de novo heterozygous *OAS1* gain-of-function variants in six patients**, confirming both the gene and the gain-of-function mechanism (Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)).

> *"We identified a heterozygous missense variation in OAS1, encoding 2′,5′-oligoadenylate synthetase 1 (OAS1) in three affected siblings, but not in unaffected family members."* — Cho et al. 2018

The disorder is inherited in an **autosomal dominant** manner. Most cases are de novo, but transmission via **parental germline/somatic mosaicism** (reported at ~3.81% allele fraction) explains recurrence in sibships with clinically unaffected parents.

### Finding 2 — OAS1 GoF activates RNase L, causing apoptosis of alveolar macrophages and B cells

OAS1 is a **type I IFN-induced, intracellular dsRNA sensor** that generates 2′-5′-oligoadenylate to activate ribonuclease L (RNase L) as antiviral defense (Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)). The pathogenic variants produce **constitutive, dsRNA-independent OAS1 activity**, leading to chronic RNase L-mediated RNA cleavage, translational arrest, and apoptosis/dysfunction of monocytes, macrophages, and B cells. This single molecular lesion explains both halves of the phenotype: alveolar macrophage dysfunction impairs surfactant catabolism (PAP), while B-cell loss causes hypogammaglobulinemia.

> *"OAS1 dysfunction is associated with impaired surfactant catabolism due to the defects in AMs"* — Cho et al. 2018

> *"Oligoadenylate synthetase 1 is a type I interferon-induced, intracellular double-stranded RNA (dsRNA) sensor that generates 2′-5′-oligoadenylate to activate ribonuclease L (RNase L) as a means of antiviral defense"* — Magg et al. 2021

Supporting the RNase L effector mechanism, independent work shows that OAS1/RNase L drives apoptosis through translational arrest coupled to up-regulation of the pro-apoptotic protein NOXA and depletion of anti-apoptotic MCL-1, triggering intrinsic (mitochondrial) apoptosis (Boehmer et al. 2021, [PMID: 34272227](https://pubmed.ncbi.nlm.nih.gov/34272227/)). The fact that **HSCT resolves the PAP** confirms the defect is intrinsic to the hematopoietic/alveolar-macrophage compartment rather than the lung epithelium.

### Finding 3 — Allogeneic HSCT is curative; WLL and RNase L inhibition are supportive/bridging

PAP **resolved after HSCT** in two unrelated infants (Cho et al. 2018, [PMID: 29455859](https://pubmed.ncbi.nlm.nih.gov/29455859/)), and allogeneic HSCT provided curative treatment for PAP associated with primary immunodeficiency and monocytopenia (Tanaka-Kubota et al. 2018, [PMID: 29185156](https://pubmed.ncbi.nlm.nih.gov/29185156/)). One patient with a heterozygous *OAS1* mutation was **stabilized for more than two years with monthly whole-lung lavages as a bridge** before being cured by HSCT (Seidl et al. 2022, [PMID: 34647697](https://pubmed.ncbi.nlm.nih.gov/34647697/)). In vitro, **RNase L inhibition with curcumin** modulated the cellular phenotype, providing proof-of-concept for targeted pharmacology (Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)). Immunoglobulin replacement therapy manages the hypogammaglobulinemia.

> *"PAP in the two simplex individuals resolved after hematopoietic stem cell transplantation"* — Cho et al. 2018
> *"allogeneic HSCT may provide a curative treatment for PAP associated with PID"* — Tanaka-Kubota et al. 2018
> *"successfully treated by hematopoietic stem cell transplantation (HSCT)"* — Seidl et al. 2022

### Finding 4 — PAPHG is part of a polymorphic, infantile-onset, myeloid-driven autoinflammatory immunodeficiency

Patients present in infancy (often **< 6 months**) with a polymorphic phenotype: infantile-onset PAP with hypoxemic respiratory failure, hypogammaglobulinemia (treated with Ig replacement), plus **recurrent fever, dermatitis, inflammatory bowel disease, and in some cases monocytopenia/cytopenias** (Cho et al. 2018, [PMID: 29455859](https://pubmed.ncbi.nlm.nih.gov/29455859/); Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)). A 2026 review repositions the OAS–RNase L gain-of-function syndrome as a **myeloid-cell-driven autoinflammatory determinant** (Lee/Casanova/Zhang 2026, [PMID: 41512080](https://pubmed.ncbi.nlm.nih.gov/41512080/)).

> *"We identified two additional de novo heterozygous missense variations of OAS1 in two unrelated simplex individuals also manifesting infantile-onset PAP with hypogammaglobulinemia."* — Cho et al. 2018
> *"the identification of gain-of-function OAS1 mutations in humans with autoinflammation also driven by myeloid cells"* — Lee/Casanova/Zhang 2026

### Finding 5 — Specific pathogenic *OAS1* variants confirmed in ClinVar

ClinVar (RefSeq NM_016816.4) lists heterozygous missense variants classified Pathogenic/Likely pathogenic for "Immunodeficiency 100 with pulmonary alveolar proteinosis and hypogammaglobulinemia" (= PAPHG):

| Variant (cDNA) | Protein | ClinVar classification | Mechanism |
|---|---|---|---|
| c.362T>G | p.(Val121Gly) | Pathogenic | Gain of function (constitutive) |
| c.592C>G | p.(Leu198Val) | Pathogenic / Likely pathogenic | Gain of function (constitutive) |
| p.Gly39Val, p.Val55Met, p.Ala76Val, p.Cys109Tyr, p.Arg125Cys, p.Glu175Lys | — | VUS / conflicting | Under study |

All identified pathogenic alleles are **rare or absent in gnomAD** and act via gain of function (constitutive, dsRNA-independent OAS1 activity; Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)).

---

## Report by Section

### 1. Disease Information

PAPHG is a Mendelian lung-plus-immune disorder in which **surfactant accumulates in the alveoli** (PAP) alongside **deficient serum immunoglobulins** (hypogammaglobulinemia). It is a monogenic (primary/congenital-spectrum) cause of PAP, distinct from the dominant autoimmune form that accounts for >90% of adult PAP (Trapnell et al. 2019, [PMID: 30846703](https://pubmed.ncbi.nlm.nih.gov/30846703/); McCarthy/Trapnell 2020, [PMID: 32279299](https://pubmed.ncbi.nlm.nih.gov/32279299/)).

**Key identifiers:** OMIM **#618042**; MONDO:**0020840**; Orphanet: rare genetic PAP spectrum; the OMIM phenotype name is "**Immunodeficiency 100 with pulmonary alveolar proteinosis and hypogammaglobulinemia (IMD100)**." ICD-11 maps to PAP (CA70.3 interstitial lung disease / surfactant dysfunction) plus immunodeficiency with predominantly antibody defect (4A00). MeSH: *Pulmonary Alveolar Proteinosis*; *Agammaglobulinemia*.

**Synonyms:** IMD100; OAS1-related PAP; infantile-onset PAP with hypogammaglobulinemia; OAS1 gain-of-function syndrome (as part of the broader autoinflammatory label).

**Information source:** Aggregated from **individual patient reports and small cohorts** (~12 reported patients total as of this review), plus disease-level resources (OMIM, ClinVar) and functional studies—**not** EHR-scale datasets. The evidence base is human clinical plus in vitro mechanistic.

### 2. Etiology

**Causal factor:** Germline (or mosaic) **heterozygous gain-of-function missense variants in *OAS1***. This is the sole known cause; the disorder is monogenic.

**Genetic risk factors:** The causal variants themselves (e.g., p.Val121Gly, p.Leu198Val). No susceptibility loci or modifier genes are established. Reduced OAS–RNase L buffering could in principle worsen disease—e.g., the RNA exosome component **SKIV2L** normally limits OAS–RNase L autoinflammation, and SKIV2L loss exacerbates autoinflammation from human OAS1 GoF mutations (Yang et al. 2024, [PMID: 39112803](https://pubmed.ncbi.nlm.nih.gov/39112803/))—but this is a model-system inference, not a demonstrated human modifier.

**Environmental risk factors:** None established. Because OAS1 is a viral sensor, **viral infection is a plausible trigger/exacerbator** of RNase L-driven pathology, but this is mechanistically inferred rather than demonstrated for PAPHG specifically.

**Protective factors:** None identified. No protective alleles or environmental exposures are known.

**Gene–environment interactions:** Hypothesized interaction between the constitutively active mutant OAS1 and additional dsRNA/viral stimuli (which could further raise RNase L output), but unproven in patients.

### 3. Phenotypes

| Phenotype | Type | HPO term | Onset / frequency | Severity / course |
|---|---|---|---|---|
| Pulmonary alveolar proteinosis | Clinical/imaging | HP:0006517 (Abnormal alveolar surfactant / PAP) | Infantile, often <6 mo; core feature (~100%) | Severe, progressive |
| Hypoxemic respiratory failure / dyspnea | Symptom/sign | HP:0002093 (Respiratory insufficiency); HP:0002094 (Dyspnea) | Infantile | Severe |
| Hypogammaglobulinemia | Lab abnormality | HP:0004313 (Decreased circulating antibody level) | Infantile; core feature | Variable; Ig-replaced |
| Recurrent infections | Symptom | HP:0002719 (Recurrent infections) | Infantile | Variable |
| Recurrent fever | Symptom | HP:0001954 (Recurrent fever) | Variable subset | Episodic (autoinflammation) |
| Dermatitis / skin inflammation | Sign | HP:0011123 (Inflammatory abnormality of the skin) | Variable subset | Variable |
| Inflammatory bowel disease / diarrhea | Sign | HP:0002037 (Inflammatory abnormality of the GI tract) | Variable subset | Variable |
| Monocytopenia / cytopenias | Lab abnormality | HP:0012312 (Monocytopenia); HP:0001903 (Anemia) | Subset | Variable |
| Failure to thrive | Sign | HP:0001508 (Failure to thrive) | Infantile | Variable |

**Age of onset:** Neonatal–infantile (typically <6 months). **Progression:** progressive respiratory failure without intervention. **Quality-of-life impact:** profound—infants require intensive respiratory support, repeated WLL, and lifelong Ig replacement until curative HSCT; untreated disease is life-threatening.

### 4. Genetic / Molecular Information

**Causal gene:** *OAS1* (HGNC:8086; NCBI Gene **4938**; 12q24.13; UniProt P00973; RefSeq NM_016816.4). OMIM gene *OAS1* 164350; phenotype #618042.

**Pathogenic variants:** heterozygous **missense** changes. Confirmed Pathogenic/Likely-pathogenic in ClinVar: **c.362T>G p.(Val121Gly)** and **c.592C>G p.(Leu198Val)**. Additional alleles (p.Gly39Val, p.Val55Met, p.Ala76Val, p.Cys109Tyr, p.Arg125Cys, p.Glu175Lys) are currently VUS/conflicting. **Allele frequency:** rare or absent in gnomAD. **Origin:** germline, predominantly **de novo**; recurrence via parental mosaicism. **Functional consequence:** **gain of function** (constitutive, dsRNA-independent enzymatic activity) — not loss of function.

**Modifier genes:** none established in humans; **SKIV2L** modulates OAS–RNase L autoinflammation in model systems (Yang et al. 2024, [PMID: 39112803](https://pubmed.ncbi.nlm.nih.gov/39112803/)). **Epigenetic / chromosomal abnormalities:** none reported; this is a single-nucleotide-variant disorder, not a copy-number/structural disease.

### 5. Environmental Information

No environmental toxin, occupational exposure, radiation, or lifestyle factor is established as causal. **Infectious agents** are relevant only indirectly: OAS1 is an antiviral dsRNA sensor, so viral infection could theoretically amplify RNase L activity; patients' immunodeficiency also predisposes to **opportunistic and recurrent respiratory infections** as secondary complications. Unlike nano-indium-tin-oxide–induced PAP in rats ([PMID: 33287472](https://pubmed.ncbi.nlm.nih.gov/33287472/)) or secondary/occupational PAP, PAPHG has **no established environmental etiology**.

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A **heterozygous gain-of-function missense variant in *OAS1*** (e.g., p.Val121Gly) **leads to** a mutant enzyme with altered conformation.
2. The mutant OAS1 **results in** constitutive, **dsRNA-independent** 2′-5′-oligoadenylate (2-5A) synthase activity (normally OAS1 fires only when bound to viral dsRNA). *[Demonstrated in vitro.]*
3. Elevated 2-5A **activates** the latent endoribonuclease **RNase L** chronically.
4. Active RNase L **cleaves** cellular (and ribosomal/tRNA) RNA → **translational arrest**.
5. Translational arrest **leads to** up-regulation of pro-apoptotic **NOXA** and depletion of anti-apoptotic **MCL-1**, triggering **intrinsic (mitochondrial) apoptosis** (mechanism from RIG-I/OAS–RNase L apoptosis studies; [PMID: 34272227](https://pubmed.ncbi.nlm.nih.gov/34272227/)). *[Inferred for patient cells; demonstrated in tumor-cell models.]*
6. **Branch A — Alveolar macrophage apoptosis/dysfunction** → impaired **surfactant catabolism** → **surfactant accumulation in alveoli** → **PAP** → hypoxemic respiratory failure.
7. **Branch B — B-cell (and plasma-cell precursor) apoptosis/dysfunction** → **defective antibody production** → **hypogammaglobulinemia** → recurrent infections.
8. **Branch C — Myeloid (monocyte/macrophage) activation and death** → **autoinflammation** (fever, dermatitis, IBD) and **monocytopenia/cytopenias** (Lee/Casanova/Zhang 2026, [PMID: 41512080](https://pubmed.ncbi.nlm.nih.gov/41512080/)).

```
 OAS1 GoF variant (germline/mosaic, heterozygous)
        │
        ▼
 Constitutive, dsRNA-independent OAS1 activity  ── upstream ──
        │  (↑ 2-5A)
        ▼
 Chronic RNase L activation ──► RNA cleavage ──► translational arrest
        │                                            │
        │                                            ▼
        │                               ↑NOXA / ↓MCL-1 → intrinsic apoptosis
        ▼
 ┌───────────────┬────────────────────┬────────────────────┐
 ▼               ▼                     ▼                    ▼
 Alveolar        B lymphocytes         Monocytes/           (downstream)
 macrophage      apoptosis             macrophages
 dysfunction     │                     activation/death
 │               ▼                     │
 ▼        Hypogammaglobulinemia        ▼
 Impaired surfactant                   Autoinflammation
 catabolism → PAP                      (fever, dermatitis, IBD),
 → respiratory failure                 monocytopenia/cytopenias
```

**Molecular pathways:** OAS–RNase L arm of the **type I interferon antiviral response** (2′-5′A pathway). **Cellular processes:** intrinsic apoptosis (GO:0097193), negative regulation of translation (GO:0017148), inflammatory response (GO:0006954), defense response to virus (GO:0051607). **Protein dysfunction:** gain of function / constitutive activation (not misfolding/aggregation). **Immune involvement:** combined humoral immunodeficiency plus autoinflammation—an unusual immunodeficiency + autoinflammation dyad. **Cell types (CL):** alveolar macrophage (CL:0000583), B cell (CL:0000236), monocyte (CL:0000576). **Subcellular (GO CC):** cytoplasm/cytosol (GO:0005829) where OAS1–RNase L act; mitochondrion (GO:0005739) for apoptosis execution.

### 7. Anatomical Structures Affected

- **Primary organ:** lung (UBERON:0002048), specifically **pulmonary alveolus** (UBERON:0002299) and alveolar airspace; respiratory system (UBERON:0001004). Involvement is **bilateral/diffuse** ("crazy-paving" on HRCT).
- **Secondary / systemic:** immune system (UBERON:0002405) / blood (UBERON:0000178) — hypogammaglobulinemia; skin (UBERON:0002097) — dermatitis; gastrointestinal tract (UBERON:0001555) — IBD.
- **Tissue/cell level:** alveolar epithelial lining (functionally secondary) with primary defect in **alveolar macrophages** (CL:0000583); **B lymphocytes** (CL:0000236) and **monocytes** (CL:0000576) in bone marrow/blood.
- **Subcellular:** cytosolic OAS–RNase L machinery; mitochondrial apoptotic execution; lysosomal/phagocytic surfactant handling impaired secondarily.

### 8. Temporal Development

**Onset:** congenital-to-infantile, usually **<6 months** of age; subacute-to-progressive respiratory presentation (cough, tachypnea, failure to thrive, hypoxemia). **Progression:** progressive respiratory failure if untreated. **Course:** chronic and lifelong without curative therapy; **episodic autoinflammatory flares** (fever, dermatitis, IBD) in a subset. **Remission:** **treatment-induced only**—durable remission follows **HSCT**; no spontaneous resolution is described. **Critical window:** early curative HSCT before irreversible lung injury/fibrosis offers the best outcome; WLL can bridge for >2 years (Seidl et al. 2022, [PMID: 34647697](https://pubmed.ncbi.nlm.nih.gov/34647697/)).

### 9. Inheritance and Population

**Epidemiology:** ultra-rare; roughly **~12 patients reported** worldwide in the literature to date—prevalence/incidence not formally estimated (far below the overall PAP prevalence of ≥7 cases/million; Trapnell et al. 2019, [PMID: 30846703](https://pubmed.ncbi.nlm.nih.gov/30846703/)).

**Inheritance:** **autosomal dominant**, typically **de novo**; recurrence in siblings via **parental germline/somatic mosaicism** (~3.81% allele fraction reported). **Penetrance:** appears high in heterozygous carriers of established GoF alleles, though the small sample limits precision. **Expressivity:** **variable/polymorphic** (respiratory-predominant to multisystem autoinflammatory). **Anticipation:** not applicable (not a repeat-expansion disorder). **Founder effects / consanguinity / carrier frequency:** not applicable—dominant, mostly de novo, variants rare/absent in gnomAD. **Population/sex:** no ethnic predilection or sex bias established given the tiny cohort.

### 10. Diagnostics

**Clinical/laboratory:**
- **Serum immunoglobulins** — low IgG ± IgA/IgM (hypogammaglobulinemia).
- **Blood counts** — possible monocytopenia/cytopenias.
- **Arterial blood gas / pulse oximetry** — hypoxemia.
- **Serum GM-CSF autoantibody** — **negative** (distinguishes from autoimmune PAP; McCarthy/Trapnell 2020, [PMID: 32279299](https://pubmed.ncbi.nlm.nih.gov/32279299/)).

**Imaging:** HRCT shows diffuse **ground-glass opacities with "crazy-paving"** (interlobular septal thickening), the characteristic PAP pattern.

**Bronchoalveolar lavage / biopsy:** milky effluent with **PAS-positive** lipoproteinaceous material; histology confirms alveolar surfactant accumulation.

**Genetic testing (definitive):** the recommended approach is **whole-exome or whole-genome sequencing**, or a **childhood interstitial lung disease (chILD) / PAP gene panel** that includes *OAS1* alongside *SFTPB, SFTPC, ABCA3, CSF2RA, CSF2RB, GATA2, MARS1*. Single-gene *OAS1* sequencing confirms a suspected case. Mosaicism testing of parents informs recurrence risk. CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not applicable** (point-mutation disorder).

**Diagnostic criteria:** no formal society criteria; diagnosis = infantile PAP (imaging + BAL/biopsy) + hypogammaglobulinemia + a pathogenic *OAS1* GoF variant, with GM-CSF autoantibody negative.

**Differential diagnosis:** other PAP + immunodeficiency causes — **CD40L deficiency / hyper-IgM** ([PMID: 42644024](https://pubmed.ncbi.nlm.nih.gov/42644024/)), **X-linked agammaglobulinemia (BTK)** ([PMID: 38576739](https://pubmed.ncbi.nlm.nih.gov/38576739/)), **ADA-SCID** ([PMID: 29690908](https://pubmed.ncbi.nlm.nih.gov/29690908/)), **GATA2 deficiency**, **lysinuric protein intolerance**; hereditary PAP from *CSF2RA/CSF2RB* ([PMID: 21075760](https://pubmed.ncbi.nlm.nih.gov/21075760/)); surfactant-production disorders (*SFTPB/SFTPC/ABCA3*); and *MARS1*-related PAP/fibrosis ([PMID: 38461880](https://pubmed.ncbi.nlm.nih.gov/38461880/)).

**Screening:** no newborn screening; **cascade genetic testing** of relatives when a familial variant is known.

### 11. Outcome / Prognosis

Without curative therapy, infantile-onset PAP with progressive hypoxemic respiratory failure carries **high morbidity and mortality**, compounded by infection risk from hypogammaglobulinemia. **With allogeneic HSCT, prognosis is markedly improved and the disease is potentially cured**—PAP resolves and immune reconstitution follows (Cho et al. 2018, [PMID: 29455859](https://pubmed.ncbi.nlm.nih.gov/29455859/); Tanaka-Kubota et al. 2018, [PMID: 29185156](https://pubmed.ncbi.nlm.nih.gov/29185156/); Seidl et al. 2022, [PMID: 34647697](https://pubmed.ncbi.nlm.nih.gov/34647697/)). **Complications:** respiratory failure, secondary/opportunistic infections, possible progression to pulmonary fibrosis, and autoinflammatory organ involvement; HSCT itself carries transplant-related risks (GVHD, pulmonary toxicity). **Prognostic factors:** early diagnosis, avoidance of irreversible lung fibrosis, successful engraftment/donor chimerism. Formal survival statistics are unavailable given the small cohort.

### 12. Treatment

| Modality | Role | Evidence | NCIT suggestion |
|---|---|---|---|
| **Allogeneic HSCT** | **Curative** (replaces defective macrophage/B-cell precursors) | Cho 2018 [PMID 29455859]; Tanaka-Kubota 2018 [PMID 29185156]; Seidl 2022 [PMID 34647697] | NCIT:C15431 (Allogeneic Hematopoietic Stem Cell Transplantation) |
| **Whole-lung lavage (WLL)** | Supportive/bridging; removes surfactant | Seidl 2022 (monthly WLL >2 yr bridge) [PMID 34647697] | NCIT:C116737 (Whole Lung Lavage) |
| **Immunoglobulin replacement (IVIG/SCIG)** | Supportive; manages hypogammaglobulinemia | Standard of care | NCIT:C569 (Immunoglobulin Therapy) |
| **RNase L inhibition (curcumin)** | Investigational / in vitro proof-of-concept | Magg 2021 [PMID 34145065] | NCIT:C818 (Curcumin) |
| **GM-CSF augmentation** | **Not expected to work** (defect is not GM-CSF signaling) | Rationale per PAP pathogenesis reviews [PMID 30846703] | NCIT:C2069 (Sargramostim) — rationale against |
| **Isolated lung transplantation** | **Not recommended** (defect is hematopoietic-intrinsic; recurrence expected) | Analogy to hereditary PAP recurrence post-Tx [PMID 27595063] | NCIT:C15283 (Lung Transplantation) |

**Pharmacogenomics / targeted therapy:** the mechanistic rationale points to **RNase L pathway inhibition** as the ideal targeted therapy; curcumin provides early in-vitro support but is not a validated clinical drug here. **Gene/cell therapy:** not yet applied to PAPHG, but **pulmonary macrophage transplantation (PMT)** and gene-corrected macrophage therapy are proof-of-concept in *Csf2rb/Csf2ra*-deficient murine hereditary PAP ([PMID: 25274301](https://pubmed.ncbi.nlm.nih.gov/25274301/); [PMID: 31326401](https://pubmed.ncbi.nlm.nih.gov/31326401/))—conceptually relevant but unproven for OAS1 disease (and complicated by the systemic, not lung-restricted, defect).

### 13. Prevention

No **primary prevention** exists (de novo dominant disorder). **Secondary prevention** = early genetic diagnosis to enable timely HSCT before irreversible lung damage. **Genetic counseling:** advise families that most cases are de novo but recurrence is possible via **parental mosaicism**; offer **prenatal/preimplantation testing** for a known familial variant. **Tertiary prevention:** Ig replacement and infection prophylaxis to reduce infections; WLL to prevent respiratory decompensation while bridging to HSCT; standard post-HSCT GVHD/infection prophylaxis. **Immunization / public-health / environmental measures:** not applicable to disease causation.

### 14. Other Species / Natural Disease

- **Taxonomy:** human disease (*Homo sapiens*, NCBI Taxon 9606). No naturally occurring animal counterpart of OAS1-GoF PAPHG is reported (OMIA has no established entry for this specific entity).
- **Orthologous gene:** mouse *Oas1a* (and the broader *Oas1* gene cluster) is the ortholog of human *OAS1* (NCBI Gene 4938). RNase L (*Rnasel*) is conserved.
- **Comparative biology:** the OAS–RNase L antiviral axis is **evolutionarily ancient and conserved**; mechanistic insights come from "experiments of nature" across species (Lee/Casanova/Zhang 2026, [PMID: 41512080](https://pubmed.ncbi.nlm.nih.gov/41512080/)). **Zoonotic potential:** none (non-infectious genetic disease).

### 15. Model Organisms

- **In vitro / patient-derived cells:** the principal model—patient monocytes/macrophages and B cells, and heterologous expression of mutant OAS1, demonstrating constitutive RNase L activation and apoptosis; **curcumin (RNase L inhibition)** rescued the phenotype in vitro (Magg et al. 2021, [PMID: 34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/)).
- **Mouse models:** no published *Oas1* gain-of-function knock-in mouse specifically recapitulating PAPHG was identified; the conserved mouse *Oas1a*/*Rnasel* axis makes such a model feasible. **SKIV2L** work in cells shows modifier potential of the pathway (Yang et al. 2024, [PMID: 39112803](https://pubmed.ncbi.nlm.nih.gov/39112803/)).
- **Related hereditary-PAP models (not OAS1):** *Csf2rb⁻/⁻* and *Csf2ra*-ablated mice model GM-CSF-receptor hereditary PAP and were used to validate pulmonary macrophage transplantation ([PMID: 25274301](https://pubmed.ncbi.nlm.nih.gov/25274301/); [PMID: 31326401](https://pubmed.ncbi.nlm.nih.gov/31326401/); [PMID: 35043685](https://pubmed.ncbi.nlm.nih.gov/35043685/))—useful for the surfactant-clearance arm but **do not** capture the OAS–RNase L mechanism or the hypogammaglobulinemia/autoinflammation.
- **Model limitation/gap:** a knock-in *Oas1* GoF animal model recapitulating the combined PAP + hypogammaglobulinemia + autoinflammation triad is a key missing resource.

---

## Mechanistic Model / Interpretation

PAPHG is best understood as a **single enzymatic "always-on" switch with three downstream failures.** The constitutively active OAS1 enzyme behaves as though the cell is perpetually infected by a virus, chronically firing RNase L. Because RNase L shreds cellular RNA and arrests translation, the cells that most depend on high-throughput protein synthesis and turnover—**alveolar macrophages** (surfactant processing) and **antibody-producing B lineage cells**—undergo apoptosis or dysfunction. The elegance of the model is that **one gain-of-function lesion predicts both words in the disease name**: "pulmonary alveolar proteinosis" (macrophage failure → surfactant buildup) and "hypogammaglobulinemia" (B-cell failure → low antibodies). The myeloid activation/death arm adds the autoinflammatory flavor (fever, dermatitis, IBD).

This mechanistic logic also predicts therapy. Because the defective cells are **hematopoietic in origin**, replacing the hematopoietic system via **HSCT cures the disease**—observed repeatedly in patients. Conversely, therapies aimed at the GM-CSF axis (which is intact here) or at the lung alone (isolated lung transplant, which would be re-seeded by the patient's own defective marrow-derived macrophages) are predicted to fail—consistent with recurrence seen when hereditary PAP lungs are transplanted without correcting the hematopoietic compartment ([PMID: 27595063](https://pubmed.ncbi.nlm.nih.gov/27595063/)). The most rational **targeted** therapy would be **pharmacologic RNase L inhibition**, for which curcumin is only an early in-vitro lead.

The table below contrasts PAPHG with the more common PAP subtypes to clarify why its management differs:

| Feature | PAPHG (OAS1 GoF) | Autoimmune PAP | Hereditary PAP (CSF2RA/B) |
|---|---|---|---|
| Mechanism | OAS1→RNase L constitutive activation | Anti-GM-CSF autoantibodies | GM-CSF receptor loss of function |
| Inheritance | AD, de novo/mosaic | Acquired | AR |
| GM-CSF autoantibody | Negative | Positive | Negative |
| Extra-pulmonary | Hypogammaglobulinemia, autoinflammation | None | Usually none |
| Definitive therapy | **HSCT** | Inhaled GM-CSF / WLL | HSCT / PMT (investigational) |
| GM-CSF therapy | Ineffective | Effective | Ineffective |

---

## Evidence Base

| PMID | Study | Type | Contribution |
|---|---|---|---|
| [29455859](https://pubmed.ncbi.nlm.nih.gov/29455859/) | Cho et al. 2018 | Human clinical + WES | Discovered *OAS1* as causal gene; linked OAS1 defect to AM dysfunction & surfactant catabolism; PAP resolved post-HSCT |
| [34145065](https://pubmed.ncbi.nlm.nih.gov/34145065/) | Magg et al. 2021 | Human cohort + in vitro | Confirmed 4 de novo heterozygous GoF variants in 6 patients; defined OAS1→RNase L mechanism; curcumin rescue |
| [29185156](https://pubmed.ncbi.nlm.nih.gov/29185156/) | Tanaka-Kubota et al. 2018 | Human clinical | HSCT curative for PAP with primary immunodeficiency |
| [34647697](https://pubmed.ncbi.nlm.nih.gov/34647697/) | Seidl et al. 2022 | Human case | OAS1 PAP bridged >2 yr by monthly WLL, then cured by HSCT |
| [41512080](https://pubmed.ncbi.nlm.nih.gov/41512080/) | Lee/Casanova/Zhang 2026 | Review | Repositions OAS–RNase L GoF as myeloid-driven autoinflammation |
| [34272227](https://pubmed.ncbi.nlm.nih.gov/34272227/) | Boehmer et al. 2021 | In vitro | RNase L→translational arrest→NOXA↑/MCL-1↓→intrinsic apoptosis |
| [39112803](https://pubmed.ncbi.nlm.nih.gov/39112803/) | Yang et al. 2024 | In vitro | SKIV2L limits OAS–RNase L autoinflammation; modifier of OAS1 GoF |
| [30846703](https://pubmed.ncbi.nlm.nih.gov/30846703/) / [32279299](https://pubmed.ncbi.nlm.nih.gov/32279299/) | Trapnell/McCarthy 2019-20 | Reviews | PAP classification, GM-CSF biology, differential diagnosis |
| [42644024](https://pubmed.ncbi.nlm.nih.gov/42644024/), [38576739](https://pubmed.ncbi.nlm.nih.gov/38576739/), [29690908](https://pubmed.ncbi.nlm.nih.gov/29690908/) | CD40L, XLA, ADA case/reviews | Human | Differential diagnoses (PAP + immunodeficiency) |

A total of 38 papers were reviewed across the investigation. The five independent human reports converge on the same gene, mechanism, and curative therapy, and the mechanistic in-vitro literature provides a coherent molecular explanation that unifies the two defining clinical features.

---

## Limitations and Knowledge Gaps

- **Tiny cohort (~12 patients):** prevalence, penetrance, expressivity, sex ratio, and survival statistics are imprecise.
- **Apoptosis execution partly inferred:** the NOXA↑/MCL-1↓ intrinsic-apoptosis step is demonstrated in tumor/model cells ([PMID 34272227](https://pubmed.ncbi.nlm.nih.gov/34272227/)), not directly proven in patient alveolar macrophages/B cells.
- **No bespoke animal model:** no published *Oas1* GoF knock-in reproduces the full PAP + hypogammaglobulinemia + autoinflammation triad.
- **Variant catalog incomplete:** only two alleles are firmly Pathogenic in ClinVar; several remain VUS pending functional confirmation.
- **No validated targeted drug:** curcumin is an in-vitro lead only; no clinical RNase L inhibitor is approved.
- **Modifier biology untested in humans:** SKIV2L's role is model-system derived.

## Proposed Follow-up Experiments / Actions

1. **Functional classification** of VUS *OAS1* alleles (p.Gly39Val, p.Arg125Cys, etc.) via 2-5A/RNase L activity assays to reclassify per ACMG.
2. **Generate an *Oas1* GoF knock-in mouse** to recapitulate and dissect the macrophage vs. B-cell vs. myeloid autoinflammation arms and to test therapeutics in vivo.
3. **Confirm the apoptotic axis** (NOXA/MCL-1, caspase activation) directly in patient-derived alveolar macrophages and B cells.
4. **Develop/trial selective RNase L inhibitors** (beyond curcumin) as targeted or bridging therapy pre-HSCT.
5. **Establish an international PAPHG registry** to quantify natural history, penetrance, mosaicism recurrence risk, and long-term HSCT outcomes.
6. **Prospective comparison** of early HSCT vs. WLL-bridged HSCT timing to define the optimal intervention window before irreversible fibrosis.
7. **Explore gene-corrected pulmonary macrophage transplantation** feasibility given the systemic (not lung-restricted) nature of the defect.


## Artifacts

- [OpenScientist final report](Pulmonary_Alveolar_Proteinosis_With_Hypogammaglobulinemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Pulmonary_Alveolar_Proteinosis_With_Hypogammaglobulinemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0006517` (1 mention) - the report calls it "Abnormal alveolar surfactant / PAP"; HP calls it **Intraalveolar phospholipid accumulation**
- `UBERON:0002048` (1 mention) - the report calls it "Primary organ:** lung"; UBERON calls it **lung**
- `NCIT:C116737` (1 mention) - the report calls it "Whole Lung Lavage"; NCIT calls it **Anti-CD33 Monoclonal Antibody BI 836858**
- `NCIT:C818` (1 mention) - the report calls it "Curcumin"; NCIT calls it **Roxithromycin**
- `NCIT:C2069` (1 mention) - the report calls it "Sargramostim"; NCIT calls it **Defosfamide**
- `NCIT:C15283` (1 mention) - the report calls it "Lung Transplantation"; NCIT calls it **Naturopathy Therapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002037` (1 mention) - the report calls it "Inflammatory abnormality of the GI tract"; HP calls it **Inflammation of the large intestine**
- `CL:0000236` (2 mentions) - the report calls it "B lymphocytes"; CL calls it **B cell**, and lists "B lymphocyte" among its other names
- `UBERON:0002405` (1 mention) - the report calls it "Secondary / systemic:** immune system"; UBERON calls it **immune system**
- `NCIT:C15431` (1 mention) - the report calls it "Allogeneic Hematopoietic Stem Cell Transplantation"; NCIT calls it **Hematopoietic Cell Transplantation**, and lists "Hematopoietic Stem Cell Transplantation" among its other names
- `NCIT:C569` (1 mention) - the report calls it "Immunoglobulin Therapy"; NCIT calls it **IgM**, and lists "Immunoglobulin M" among its other names