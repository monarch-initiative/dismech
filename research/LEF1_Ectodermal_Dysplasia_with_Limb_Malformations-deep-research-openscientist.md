---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T18:19:22.015907'
end_time: '2026-10-16T18:44:05.343635'
duration_seconds: 1483.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: LEF1 Ectodermal Dysplasia with Limb Malformations
  mondo_id: MONDO:0979228
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
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 61
  verified: 58
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 47
  labels_matching: 30
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0010486
    reported_labels:
    - Thenar muscle atrophy/hypoplasia
    ontology_label: Abnormality of the hypothenar eminence
  - term_id: HP:0045025
    reported_labels:
    - Sparse eyebrow
    ontology_label: Narrow palpebral fissure
  - term_id: HP:0000028
    reported_labels:
    - case(s)
    ontology_label: Cryptorchidism
  - term_id: CL:0002332
    reported_labels:
    - dermal papilla cell
    ontology_label: multiciliated epithelial cell of the bronchus
  - term_id: UBERON:0003823
    reported_labels:
    - thenar / manus region
    ontology_label: hindlimb zeugopod
  - term_id: NCIT:C15300
    reported_labels:
    - Dental Procedure
    ontology_label: Photodynamic Therapy
  - term_id: NCIT:C15733
    reported_labels:
    - Supportive Care
    ontology_label: Diagnostic Trial
  - term_id: NCIT:C50743
    reported_labels:
    - Ductus Arteriosus Repair
    ontology_label: Skin Irritation
  - term_id: NCIT:C15417
    reported_labels:
    - Genetic Counseling
    ontology_label: Randomized Clinical Trial
  labels_variant: 8
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: LEF1_Ectodermal_Dysplasia_with_Limb_Malformations-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: LEF1_Ectodermal_Dysplasia_with_Limb_Malformations-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** LEF1 Ectodermal Dysplasia with Limb Malformations
- **MONDO ID:** MONDO:0979228 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **LEF1 Ectodermal Dysplasia with Limb Malformations** covering all of the
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

# LEF1 Ectodermal Dysplasia with Limb Malformations — Comprehensive Disease Report

**Disease:** LEF1 Ectodermal Dysplasia with Limb Malformations
**Preferred clinical name:** Ectodermal dysplasia 17, with or without limb malformations (ECTD17)
**MONDO:** MONDO:0979228 · **OMIM:** 621224 · **Causal gene:** *LEF1* (OMIM 153245; HGNC:6551)
**Category:** Mendelian, ultra-rare

---

## Summary

LEF1 Ectodermal Dysplasia with Limb Malformations (ECTD17; MONDO:0979228; OMIM 621224) is an ultra-rare Mendelian multisystem developmental disorder caused by pathogenic germline variants in *LEF1*, the HMG-box transcription factor that serves as the nuclear effector of canonical WNT/β-catenin signaling. The disorder was first delineated as a distinct clinical entity by Dufour and colleagues in 2022, who described 12 affected individuals from 5 families and established *LEF1* as the causal gene through segregation and functional assays ([PMID: 35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/)). The cardinal features combine **ectodermal dysplasia** (sparse eyebrows/hair, oligodontia and other dental anomalies, dry skin, nail dystrophy, hypoplastic nipples/breast tissue) with **limb malformations** (radial ray defects, polydactyly, and split-hand/split-foot malformation).

The central mechanistic insight of this investigation is that **both inheritance pattern and severity are determined by the variant class and its position within the LEF1 protein**. Monoallelic variants that cause haploinsufficiency or loss of DNA binding produce autosomal dominant, mild-to-moderate disease, whereas biallelic variants that abolish β-catenin binding produce autosomal recessive, severe disease. This genotype–severity relationship is grounded in the protein's domain architecture: the N-terminal β-catenin–binding domain (residues 1–62) and the C-terminal HMG-box DNA-binding domain (residues 299–367) define two separable loss-of-function mechanisms. LEF1 is among the most loss-of-function–intolerant genes in the genome (gnomAD pLI = 0.998, LOEUF = 0.212), independently corroborating a haploinsufficiency mechanism for the dominant form.

Mechanistically, LEF1 is required for WNT-dependent epithelial–mesenchymal signaling that drives the development of ectodermal appendages (teeth, hair, whiskers, mammary glands) and the patterning of the limb. The *Lef1*-null mouse recapitulates the ectodermal and mammary components of the human phenotype — absent teeth, hair, vibrissae and mammary glands — but notably **not** the limb-reduction phenotype, an allele/dosage-specific observation that highlights the difference between complete gene ablation (mouse) and the specific partial/domain-selective losses seen in human patients. There is no disease-modifying therapy; management is supportive and multidisciplinary.

---

## Section 1 — Disease Information

**Overview.** ECTD17 is a congenital, developmental syndrome in which disrupted canonical WNT signaling impairs the formation of ectodermal appendages and limb structures. It belongs to the broad family of ectodermal dysplasias (ED), which are defined by abnormalities of two or more ectodermal derivatives (hair, teeth, nails, sweat glands), but is distinguished by the co-occurrence of radial-ray / split-hand-foot limb malformations.

**Key identifiers (verified via EBI OLS / MONDO cross-reference query for MONDO:0979228):**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0979228 — "ectodermal dysplasia 17 with or without limb malformations" |
| OMIM | 621224 (phenotype); 153245 (*LEF1* gene) |
| MedGen | C1876515 (CUI 1876515) |
| UMLS | C6012731 |
| GARD | 0028106 |
| Gene | *LEF1* (HGNC:6551) |

**Synonyms / alternative names:** Ectodermal dysplasia 17 with or without limb malformations; ECTD17; LEF1-related ectodermal dysplasia with limb malformations; LEF1 ectodermal dysplasia–limb malformation syndrome.

**Information source.** Disease-level evidence is derived predominantly from a single aggregated case series (Dufour et al., 2022, 12 individuals) plus curated ontology/database resources (OMIM, MONDO, HPO, ClinVar, gnomAD, UniProt, MGI). This is **not** EHR/population-derived; it is an aggregation of individual-patient reports consolidated into database annotations. (Finding F004.)

---

## Section 2 — Etiology

**Primary cause.** ECTD17 is a monogenic disorder caused by pathogenic germline variants in *LEF1*. There is no known environmental or infectious contribution. (Finding F001.)

**Genetic risk / causal factors.**
- **Monoallelic (heterozygous) variants** → autosomal dominant, mild-to-moderate disease, via **haploinsufficiency** or **loss of DNA binding**.
- **Biallelic variants** (observed in a consanguineous family) → autosomal recessive, severe disease, via **loss of β-catenin binding**.

Dufour et al. summarized the two-mechanism model directly: *"Our functional data indicate that 2 molecular mechanisms are at play: haploinsufficiency or loss of DNA binding are responsible for a mild to moderate phenotype, whereas loss of β-catenin binding caused by biallelic variants is associated with a severe phenotype."* ([PMID: 35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/)) (Finding F001.)

**Environmental risk factors / protective factors / gene–environment interactions.** None established. Given the monogenic, developmental nature of the disorder, there is no literature identifying environmental triggers, protective alleles, lifestyle factors, or GxE interactions. **Consanguinity** is a relevant demographic factor for the recessive, severe form (the biallelic case arose in a consanguineous family). (Finding F001.)

---

## Section 3 — Phenotypes

Phenotype frequencies below are from official HPO annotations for OMIM:621224, sourced to Dufour et al. 2022 ([PMID: 35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/)). The authors summarized: *"The phenotypic spectrum includes various limb malformations, such as radial ray defects, polydactyly or split hand/foot, and ectodermal dysplasia."* (Finding F005.)

### Limb malformations (physical manifestations)

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Split hand | 3/12 | HP:0001171 (Split hand) |
| Short thumb | 4/11 | HP:0009778 (Short thumb) |
| Small thenar eminence | 4/12 | HP:0010486 (Thenar muscle atrophy/hypoplasia) |
| Radial ray deficiency | 1/12 | HP:0002984 (Hypoplasia of the radius / radial ray) |
| Split foot | 1/12 | HP:0001839 (Split foot) |
| Preaxial polydactyly (hand) | case(s) | HP:0001177 (Preaxial hand polydactyly) |
| Toe syndactyly | case(s) | HP:0001770 (Toe syndactyly) |

### Ectodermal features

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Oligodontia | 5/14 | HP:0000677 (Oligodontia) |
| Sparse eyebrows | 6/12 | HP:0045025 (Sparse eyebrow) |
| Dry skin | 5/13 | HP:0000958 (Dry skin) |
| Eczematoid dermatitis | 3/12 | HP:0000964 (Eczema) |
| Abnormal nails | 3/12 | HP:0001597 (Abnormality of the nail) |
| Taurodontia / microdontia / delayed eruption | case(s) | HP:0000679 / HP:0000691 / HP:0000684 |
| Hypohidrosis | 1/12 | HP:0000966 (Hypohidrosis) |

### Mammary features

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Hypoplastic nipples | 4/10 | HP:0002557 (Hypoplastic nipples) |
| Breast hypoplasia | 2/10 | HP:0003187 (Breast hypoplasia) |

The mammary phenotype is mechanistically notable because it directly mirrors the *Lef1*-null mouse (absent mammary gland), consistent with LEF1's known role in mammary bud formation (see Sections 6 and 15).

### Other / variable features

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Mild intellectual disability | 1/12 | HP:0001256 |
| Autism spectrum disorder | 1/12 | HP:0000729 |
| Patent ductus arteriosus | 1/12 | HP:0001643 |
| Cryptorchidism | case(s) | HP:0000028 |
| Short stature | 1/3 | HP:0004322 |

**Phenotype characteristics.** *Onset:* congenital/neonatal (limb and ectodermal structures are developmentally determined). *Severity:* variable, and strongly genotype-dependent (mild-to-moderate in monoallelic AD cases; severe in the biallelic AR case). *Progression:* structural malformations are stable (non-progressive); ectodermal features (dry skin, dental anomalies) are lifelong. *Quality-of-life impact:* driven mainly by hand/foot function (dexterity, grip), dental function/aesthetics, and skin barrier issues; disease-specific QoL instruments have not been applied in the literature. (Finding F005.)

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *LEF1* (lymphoid enhancer-binding factor 1), OMIM 153245, HGNC:6551, located at chromosome **4q25** (chr4:~108.97–109.09 Mb, GRCh37). Canonical transcript NM_016269.5; protein UniProt Q9UJU2 (399 aa). (Findings F006, F007.)

**Constraint / dosage sensitivity.** gnomAD constraint metrics (GRCh37, ENSG00000138795) place LEF1 among the most loss-of-function–intolerant genes:

| Metric | Value | Interpretation |
|---|---|---|
| pLI | 0.998 | Extreme LoF intolerance |
| LOEUF (oe_lof_upper) | 0.212 | Strong constraint |
| Observed/expected LoF | 1 / 22.4 (o/e = 0.045) | Near-complete depletion of LoF alleles |
| LoF Z-score | 4.19 | Highly significant |
| Missense Z-score | 1.57 | Mild missense constraint |

This independent population-genetic signal supports haploinsufficiency as the dominant-disease mechanism — consistent with the functional demonstration that *"haploinsufficiency or loss of DNA binding are responsible for a mild to moderate phenotype"* ([PMID: 35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/)). (Finding F006.)

**Pathogenic variants (ClinVar, transcript NM_016269.5).**

| Variant (cDNA) | Protein | Type | Classification | Association |
|---|---|---|---|---|
| c.856del | p.His286fs | Frameshift | **Pathogenic** | ECTD17 |
| c.469dup | p.Leu157fs | Frameshift | Conflicting | ECTD17 |
| c.811G>T | p.Glu271Ter | Nonsense | VUS | — |
| Large 4q CNVs encompassing *LEF1* | — | Structural (deletion/CNV) | Pathogenic / Likely pathogenic | — |

Variant classes reported for the disorder include **frameshift, nonsense, and missense** alleles plus large structural CNVs. Both of the truncating frameshifts (p.Leu157fs at residue 157, p.His286fs at residue 286) terminate the protein **before** the C-terminal HMG box (residues 299–367), removing the DNA-binding domain — the structural correlate of the "loss of DNA binding" mechanism. (Findings F006, F007.)

**Domain architecture and genotype–severity mapping (UniProt Q9UJU2).**

```
LEF1 protein (399 aa)
 │
 ├─ aa 1–62    N-terminal β-CATENIN (CTNNB1)-BINDING DOMAIN
 │              → biallelic loss here = loss of β-catenin binding = SEVERE (AR)
 │
 ├─ central    Intrinsically disordered, context-dependent regulatory region
 │
 └─ aa 299–367 C-terminal HMG-BOX DNA-BINDING DOMAIN (DNA bending)
                → truncation/loss here = loss of DNA binding = MILD–MODERATE (AD)
```

Dufour et al.: *"whereas loss of β-catenin binding caused by biallelic variants is associated with a severe phenotype."* ([PMID: 35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/)) The N-terminal CTNNB1-binding domain (aa 1–62) is the structural correlate of this severe recessive mechanism. (Finding F007.)

**Relevant GO annotations for LEF1 (Q9UJU2):**
- Molecular function: beta-catenin binding (GO:0008013); gamma-catenin binding (GO:0045295); DNA binding, bending (GO:0008301).
- Biological process: canonical Wnt signaling (GO:0060070); positive regulation of odontoblast differentiation (GO:1901331); secondary palate development (GO:0062009); osteoblast differentiation (GO:0001649); epithelial–mesenchymal transition (GO:0001837 / GO:0010718).

**Modifier genes / epigenetics.** Not established for this disorder. No disease-specific methylation or histone-modification signatures have been reported.

**Chromosomal abnormalities.** Large 4q deletions/CNVs encompassing *LEF1* are classified Pathogenic/Likely pathogenic and represent a structural route to LEF1 haploinsufficiency. (Finding F006.)

---

## Section 5 — Environmental Information

No environmental, lifestyle, or infectious factors are implicated. ECTD17 is a monogenic developmental disorder; environmental factors (toxins, radiation, occupational exposures, smoking/diet/alcohol) and infectious agents are **not applicable**. The only non-genetic epidemiological modifier of relevance is **consanguinity**, which raises the risk of the biallelic (recessive, severe) form. (Finding F001.)

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A germline *LEF1* variant (frameshift/nonsense/missense/CNV, mono- or biallelic) **leads to** reduced LEF1 dosage and/or a LEF1 protein lacking a functional domain.
2. **Branch A (monoallelic):** haploinsufficiency or a variant that removes/impairs the HMG-box DNA-binding domain (aa 299–367) **results in** a quantitative reduction in functional LEF1 available to act on WNT target enhancers → *mild-to-moderate* disease.
3. **Branch B (biallelic):** variants abolishing the N-terminal β-catenin–binding domain (aa 1–62) **result in** a LEF1 that cannot be co-activated by β-catenin → near-complete loss of WNT transcriptional output at LEF1 sites → *severe* disease.
4. Reduced LEF1/β-catenin transcriptional complex activity **leads to** altered expression of canonical WNT target genes (demonstrated by RNA-seq showing altered WNT signaling in patient-derived material). (Finding F001.)
5. Impaired WNT transcriptional output **disrupts** WNT-dependent **epithelial–mesenchymal signaling** required for the induction and morphogenesis of ectodermal appendages (hair follicles, teeth, nails, sweat glands, mammary buds) — *inferred* from LEF1's established role as a WNT readout in these tissues. (Findings F002, F008.)
6. In parallel, impaired WNT-dependent limb-bud patterning (radial ray / AER–ZPA programs) **results in** radial ray defects, polydactyly, and split-hand/split-foot malformation — the step that is *allele/dosage-specific in humans and not reproduced by complete gene knockout in mouse*. (Finding F008.)
7. The combined ectodermal and limb developmental failures **manifest clinically** as ECTD17.

### Supporting detail by category

**Molecular pathways.** Canonical **WNT/β-catenin** signaling. LEF1 is an HMG-box TCF/LEF-family transcription factor that binds β-catenin and acts as the nuclear transcriptional effector of the pathway. Across multiple independent systems LEF1 is a direct WNT readout: in hair-follicle dermal papilla cells, WNT+FGF activation increased *LEF1* 3.8-fold (p < 0.01) ([PMID: 42283394](https://pubmed.ncbi.nlm.nih.gov/42283394/)); bacterial extracellular vesicles induced the canonical Wnt readouts LEF1 and AXIN2 in dermal papilla cells and promoted hair-shaft elongation ([PMID: 42316873](https://pubmed.ncbi.nlm.nih.gov/42316873/)). (Finding F002.)

**Cellular processes.** WNT-driven epithelial–mesenchymal interaction/induction; cell-fate specification and morphogenesis of ectodermal placodes and limb mesenchyme; epithelial–mesenchymal transition (GO:0001837). LEF1 is expressed in the signaling mesenchymal compartments — *"the dermal papilla of hair and whisker follicles, the dental papilla of teeth, and a subset of mesenchymal cells in pubescent mammary glands"* ([PMID: 9786416](https://pubmed.ncbi.nlm.nih.gov/9786416/)). (Finding F008.)

**Protein dysfunction.** Loss of function via (i) truncation removing the HMG box (loss of DNA binding) or (ii) loss of the N-terminal β-catenin–binding domain (loss of co-activator recruitment). These are **loss-of-function / hypomorphic** mechanisms, not gain-of-function. Haploinsufficiency is supported by extreme gnomAD LoF intolerance (pLI 0.998). (Findings F006, F007.)

**Immune / metabolic / tissue-damage mechanisms.** Not primary to this developmental disorder. (LEF1/TCF biology is prominent in T-cell memory and oncogenesis in other contexts, but these are not the pathomechanism of ECTD17.)

**Molecular profiling.** Dufour et al. performed RNA-seq (plus immunofluorescence, immunoblotting, and pulldown) demonstrating altered WNT signaling as the downstream consequence of the variants. (Finding F001.)

### Context — ectodermal dysplasia as a WNT/EDA pathway disease

The placement of ECTD17 within WNT-pathway ED is reinforced by the broader literature: *"Molecular pathogenesis of ED involves mutations of genes encoding key proteins of major developmental pathways, including ectodysplasin (EDA) and wingless-type (WNT) pathways."* ([PMID: 34573371](https://pubmed.ncbi.nlm.nih.gov/34573371/)) (Findings F002, F003.)

### Suggested ontology terms

- **GO biological process:** GO:0060070 (canonical Wnt signaling), GO:1901331 (positive regulation of odontoblast differentiation), GO:0062009 (secondary palate development), GO:0001837 (epithelial–mesenchymal transition), GO:0042476 (odontogenesis), GO:0001942 (hair follicle development), GO:0030879 (mammary gland development).
- **GO molecular function:** GO:0008013 (beta-catenin binding), GO:0008301 (DNA binding, bending).
- **CL cell types:** CL:0002332 (dermal papilla cell), CL:0000062 (odontoblast)/dental papilla cell, mammary mesenchymal cells, limb-bud mesenchymal cells.

---

## Section 7 — Anatomical Structures Affected

**Organ / system level.**
- **Integumentary system (primary):** skin (dry skin, eczematoid dermatitis), hair (sparse eyebrows/hair), nails (dystrophy), sweat glands (hypohidrosis). UBERON:0002097 (skin of body), UBERON:0001037 (strand of hair), UBERON:0001705 (nail), UBERON:0001820 (sweat gland).
- **Dentition:** teeth (oligodontia, taurodontia, microdontia, delayed eruption). UBERON:0001091 (tooth).
- **Musculoskeletal / limbs:** hand/foot skeleton, radial ray, thenar musculature. UBERON:0002398 (manus), UBERON:0002387 (pes), UBERON:0002102 (forelimb), UBERON:0003823 (thenar / manus region).
- **Mammary:** nipple and breast tissue (hypoplastic nipples, breast hypoplasia). UBERON:0001911 (mammary gland), UBERON:0002030 (nipple).
- **Secondary / variable:** cardiovascular (PDA — UBERON:0002061 ductus arteriosus), CNS (mild ID/ASD), reproductive (cryptorchidism).

**Tissue / cell level.** Primarily **epithelial** derivatives of ectoderm and the **mesenchymal** signaling populations that instruct them (dermal papilla, dental papilla, mammary mesenchyme, limb-bud mesenchyme). Cell Ontology: CL:0002332 (dermal papilla cell), dental papilla cells, mammary mesenchymal cells.

**Subcellular level.** LEF1 is a transcription factor; its functional compartment is the **nucleus** (GO:0005634), acting at **chromatin** (GO:0000785) within the β-catenin/LEF1 transcriptional complex.

**Localization / lateralization.** Limb anomalies are typically **bilateral** but may be **asymmetric** (variable between hands and feet); ectodermal features are generalized/bilateral.

---

## Section 8 — Temporal Development

- **Onset:** congenital. Both limb malformations and ectodermal appendage defects are determined during embryonic/fetal development; dental features become evident through infancy/childhood as dentition develops. (Finding F005.)
- **Onset pattern:** developmental (non-acute); features are present from birth or emerge as the relevant structures normally develop.
- **Progression:** structural malformations (limbs, mammary hypoplasia) are **stable/non-progressive**; ectodermal features (dry skin, dental anomalies, nail dystrophy) are **lifelong/chronic** but non-progressive. No disease staging exists.
- **Disease course / duration:** chronic, lifelong; not life-limiting in the reported cohort apart from variable complications.
- **Remission:** none (structural/developmental disorder). No spontaneous or treatment-induced remission.
- **Critical period:** the window of embryonic limb-bud patterning and ectodermal placode induction — the only period during which the primary malformations could, in principle, be modified (not currently actionable).

---

## Section 9 — Inheritance and Population

**Epidemiology.** Prevalence and incidence are **unknown**; the disorder is ultra-rare, with ~12 individuals reported to date. For epidemiological context, the limb component overlaps split-hand/split-foot malformation (SHFM), which *"is a rare condition that occurs in 1 in 8500-25,000 newborns and accounts for 15% of all limb reduction defects."* ([PMID: 30622331](https://pubmed.ncbi.nlm.nih.gov/30622331/)) — but LEF1-specific figures are not established. (Finding F003.)

**Inheritance.** **Both** autosomal dominant and autosomal recessive, depending on variant class:
- **Autosomal dominant** — monoallelic haploinsufficiency or loss of DNA binding (11 affected individuals across 4 unrelated families in the original report).
- **Autosomal recessive** — biallelic loss of β-catenin binding (1 individual, consanguineous family). (Findings F001, F005.)

**Penetrance / expressivity.** Expressivity is **variable** (range of limb and ectodermal severity, including incomplete feature sets per the "with or without limb malformations" nomenclature). Precise penetrance figures are not quantified given the small cohort.

**Other genetic parameters.** Genetic anticipation — not applicable (not a repeat-expansion disorder). Germline mosaicism — not reported. Founder effects — none known. **Consanguinity** — contributory to the recessive severe form. Carrier frequency — not established; given extreme LoF intolerance, LoF alleles are very rare in gnomAD (observed LoF = 1). (Finding F006.)

**Population demographics.** No ethnic predilection, geographic clustering, sex bias, or variant-specific geographic distribution has been established in the small reported cohort.

---

## Section 10 — Diagnostics

**Clinical recognition.** Diagnosis is clinical-plus-molecular: recognition of the combination of ectodermal dysplasia features (hypodontia/oligodontia, sparse hair/eyebrows, dry skin, nail/sweat-gland anomalies, hypoplastic nipples) with limb malformations (radial ray defects, polydactyly, split-hand/foot), followed by confirmatory genetic testing.

**Imaging.** Hand/foot radiographs to characterize radial ray deficiency, split-hand/foot, polydactyly, and thenar hypoplasia; dental radiographs/panoramic imaging for oligodontia and taurodontia. Echocardiography where PDA or other cardiac involvement is suspected.

**Genetic testing (recommended, definitive).**
- **Whole-exome sequencing (WES)** or a targeted **ectodermal dysplasia / limb-malformation gene panel** including *LEF1* is the primary approach, given phenotypic overlap with other WNT/ectodermal loci.
- **Single-gene *LEF1* sequencing** confirms point/indel variants (NM_016269.5).
- **Chromosomal microarray (CMA) / WGS** to detect large **4q CNVs** encompassing *LEF1* when sequencing is negative but dosage loss is suspected. (Finding F006.)
- Variant interpretation per ACMG/AMP; truncating variants and whole-gene deletions are readily classified given strong LoF intolerance, while missense variants may require functional follow-up (β-catenin binding / DNA binding assays, as in the original report).

**Differential diagnosis.** Other WNT/ectodermal and SHFM loci must be distinguished:

| Gene / locus | Overlapping features | Reference |
|---|---|---|
| *TP63* (EEC/SHFM4) | SHFM + hypodontia | [PMID: 31420900](https://pubmed.ncbi.nlm.nih.gov/31420900/), [PMID: 42110406](https://pubmed.ncbi.nlm.nih.gov/42110406/), [PMID: 33294441](https://pubmed.ncbi.nlm.nih.gov/33294441/) |
| *WNT10B*, *DLX5*, *LRP6*, *UBA2* | SHFM | [PMID: 31332306](https://pubmed.ncbi.nlm.nih.gov/31332306/) |
| 10q24 duplication; 17p13.3 (*BHLHA9*) | SHFM | [PMID: 30622331](https://pubmed.ncbi.nlm.nih.gov/30622331/), [PMID: 31332306](https://pubmed.ncbi.nlm.nih.gov/31332306/) |
| *EDA*/*EDAR*/*WNT10A* | Ectodermal dysplasia (hypohidrotic) | [PMID: 34573371](https://pubmed.ncbi.nlm.nih.gov/34573371/) |

*"SHFM and hypodontia are prominent clinical manifestations of TP63-related disorders."* ([PMID: 31420900](https://pubmed.ncbi.nlm.nih.gov/31420900/)) — making *TP63* the key clinical mimic. (Finding F003.)

**Screening.** Cascade genetic testing of at-risk relatives once a familial variant is identified; prenatal/preimplantation genetic testing is feasible for known familial variants. No population newborn screening exists.

---

## Section 11 — Outcome / Prognosis

- **Survival / mortality:** The disorder is generally **not life-limiting**; no disease-specific mortality figures are reported, and life expectancy is expected to be normal in typical (mild-to-moderate) cases. Severe (biallelic) disease and associated anomalies (e.g., PDA) could add complication-dependent risk, but data are limited to single cases.
- **Morbidity / disability:** Driven by **hand/foot function** (grip, dexterity, fine motor tasks) from radial ray/split-hand-foot defects, **dental morbidity** (oligodontia affecting mastication, speech, aesthetics), and **skin/thermoregulation** issues (dry skin, hypohidrosis).
- **Complications:** dental complications, skin barrier/eczematoid dermatitis, and — in individual cases — cardiac (PDA), neurodevelopmental (mild ID/ASD), and genitourinary (cryptorchidism) findings.
- **Prognostic factors:** the strongest prognostic determinant is **genotype** — biallelic β-catenin-binding loss predicts severe disease, whereas monoallelic haploinsufficiency/DNA-binding loss predicts milder disease. (Findings F001, F007.)
- **Quality of life:** formal QoL instruments (EQ-5D, SF-36, PROMIS) have not been applied; impact is inferred from functional/aesthetic domains.

---

## Section 12 — Treatment

There is **no disease-modifying or curative therapy**. Management is **supportive and multidisciplinary**, directed at individual manifestations:

| Domain | Intervention | Suggested NCIT term |
|---|---|---|
| Dental | Restorative/prosthodontic care, dental implants, orthodontics for oligodontia | NCIT:C15300 (Dental Procedure) |
| Limb | Reconstructive/orthopedic hand-foot surgery for SHFM/polydactyly; occupational therapy | NCIT:C15329 (Orthopedic Surgery) |
| Skin | Emollients/barrier care; dermatologic management of eczematoid dermatitis | NCIT:C15733 (Supportive Care) |
| Thermoregulation | Heat-avoidance / environmental measures for hypohidrosis | NCIT:C15733 (Supportive Care) |
| Rehabilitation | Physical / occupational therapy; speech therapy if dentition affects articulation | NCIT:C15351 (Rehabilitation Therapy) |
| Cardiac | PDA closure if clinically indicated | NCIT:C50743 (Ductus Arteriosus Repair) |
| Genetic | Genetic counseling for family planning | NCIT:C15417 (Genetic Counseling) |

- **Pharmacotherapy / pharmacogenomics:** none specific. No targeted WNT-modulating therapy is approved or in trials for this disorder.
- **Advanced therapeutics (gene/cell/RNA/targeted/immuno):** none in clinical use or trials for ECTD17; remain theoretical. LEF1 haploinsufficiency is mechanistically a candidate for dosage-restoration approaches, but the critical developmental window largely precedes diagnosis.
- **Experimental:** no registered ClinicalTrials.gov interventions specific to this disorder (ultra-rare, recently described).

---

## Section 13 — Prevention

- **Primary prevention:** not possible for a congenital monogenic disorder other than through **reproductive genetic counseling**. For families with a known *LEF1* variant, options include prenatal diagnosis and preimplantation genetic testing.
- **Secondary prevention:** early multidisciplinary assessment (dental, orthopedic, dermatologic, cardiac) to anticipate and manage complications; cascade testing of relatives.
- **Tertiary prevention:** optimizing dental, orthopedic, and skin care to prevent secondary functional decline.
- **Counseling:** genetic counseling is central — conveying the variant-class-dependent inheritance (AD vs AR) and recurrence risks, and the elevated risk of the severe recessive form with **consanguinity**. (Findings F001, F007.)
- **Immunization / public health / environmental interventions:** not applicable.

---

## Section 14 — Other Species / Natural Disease

- **Taxonomy / orthologs:** Mouse *Lef1* (NCBI Gene 16842; MGI:96770) is the principal ortholog studied; LEF1/TCF biology is conserved broadly across vertebrates. (Finding F008.)
- **Natural disease / veterinary relevance:** no naturally occurring companion-animal or wildlife equivalent of ECTD17 is documented in OMIA for this gene/phenotype combination; relevance is through engineered models, not spontaneous animal disease.
- **Comparative biology:** The canonical WNT/β-catenin → TCF/LEF transcriptional axis is deeply evolutionarily conserved; LEF1-dependent ectodermal appendage development (hair, teeth, mammary) is conserved between mouse and human. However, species differences in WNT/TCF-LEF usage exist — e.g., *"clear differences between mouse and human pluripotent stem cells"* in TCF/LEF gene regulation ([PMID: 40844425](https://pubmed.ncbi.nlm.nih.gov/40844425/)) — cautioning against assuming identical requirements across contexts.
- **Transmission / zoonosis:** not applicable.

---

## Section 15 — Model Organisms

**Primary model: *Lef1*-null mouse (MGI:96770).** Alliance of Genome Resources / MGI curated phenotypes (51 annotations) include: absent teeth/incisors/molars and arrested tooth development; abnormal/underdeveloped hair follicles, decreased hair follicle number, alopecia; absent/sparse vibrissae; absent mammary gland and abnormal mammary bud; abnormal skin; abnormal craniofacial morphology; dilated cardiomyopathy; absent dentate gyrus/hippocampus and absent cortical barrels; increased skin-tumor incidence; and perinatal/postnatal/preweaning lethality with complete penetrance. (Finding F008.)

**Phenotype recapitulation and the key allele/dosage insight.** The null mouse **recapitulates the ectodermal and mammary components** of the human disease (teeth, hair, whiskers, mammary gland), confirming LEF1-dependence of these appendages: LEF-1 is expressed in *"the dermal papilla of hair and whisker follicles, the dental papilla of teeth, and a subset of mesenchymal cells in pubescent mammary glands"* ([PMID: 9786416](https://pubmed.ncbi.nlm.nih.gov/9786416/)). Crucially, the null mouse does **not** list limb reduction / split-hand-foot / polydactyly phenotypes, and complete knockout is perinatally/postnatally lethal — whereas human patients survive and manifest limb malformations. This dissociation indicates that:
1. the **limb phenotype in humans is allele- and dosage-specific** (partial/domain-selective losses or heterozygous haploinsufficiency), not reproduced by total gene ablation; and
2. mouse complete-null lethality and additional phenotypes (CNS, cardiomyopathy) are **model limitations** not seen in human patients. (Finding F008.)

**Genetic model types and resources.** Conventional *Lef1* knockouts are the main resource (MGI/IMSR). Conditional/tissue-specific and hypomorphic/knock-in alleles that better mimic human domain-selective variants (e.g., β-catenin-binding–deficient or HMG-box–truncated alleles) would more faithfully model the genotype–severity relationship. In vitro systems (dermal papilla cells, hair-follicle organ culture, reporter assays) are well established WNT/LEF1 readout models (e.g., [PMID: 42283394](https://pubmed.ncbi.nlm.nih.gov/42283394/), [PMID: 42316873](https://pubmed.ncbi.nlm.nih.gov/42316873/)).

---

## Mechanistic Model / Interpretation

The investigation converges on a single, internally consistent model in which **a WNT-effector transcription factor's dosage and domain integrity map directly onto inheritance mode and clinical severity**:

```
                         LEF1 germline variant
                                  │
         ┌────────────────────────┴─────────────────────────┐
   MONOALLELIC                                          BIALLELIC
 (haploinsufficiency OR                            (loss of N-terminal
  loss of HMG-box DNA binding)                      β-catenin binding, aa1–62)
         │                                                  │
 Partial ↓ WNT target transcription              Near-total loss of β-catenin
         │                                        co-activation at LEF1 sites
         │                                                  │
  Autosomal DOMINANT                                Autosomal RECESSIVE
  MILD–MODERATE disease                              SEVERE disease
         └────────────────────────┬─────────────────────────┘
                                   │
            Disrupted WNT-dependent epithelial–mesenchymal signaling
                                   │
         ┌─────────────────────────┬───────────────────────────┐
  Ectodermal appendage         Mammary bud                 Limb-bud
  failure (hair, teeth,        hypoplasia                  patterning defect
  nails, sweat glands)         (mirrors Lef1-null mouse)   (radial ray, SHFM,
                                                            polydactyly;
                                                            human allele-specific)
                                   │
                         Clinical ECTD17 phenotype
```

Three independent lines of evidence reinforce this model: (1) the **functional dissection** by Dufour et al. tying variant class to mechanism and severity; (2) the **population-genetics constraint** (pLI 0.998) confirming LEF1 as haploinsufficiency-sensitive; and (3) the **protein domain map** (UniProt) that physically separates the two loss-of-function mechanisms into the N-terminal β-catenin-binding domain and the C-terminal HMG box. The **mouse model** both validates the ectodermal/mammary arm of the mechanism and, by its failure to reproduce the limb phenotype under complete null conditions, sharpens the interpretation that the human limb malformations arise from specific partial/heterozygous losses rather than total absence of LEF1.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/) | *Monoallelic and biallelic variants in LEF1 … new syndrome combining ectodermal dysplasia and limb malformations caused by altered WNT signaling* | **Primary/defining paper.** Establishes causality, the two-mechanism genotype–severity model, phenotype spectrum, and altered WNT signaling (RNA-seq). |
| [9786416](https://pubmed.ncbi.nlm.nih.gov/9786416/) | LEF-1 expression at epithelial–mesenchymal interaction sites | Confirms LEF1 dependence of hair/whisker, tooth, mammary appendages — the ectodermal arm of the mechanism. |
| [34573371](https://pubmed.ncbi.nlm.nih.gov/34573371/) | Ectodysplasin pathway key players in ED | Establishes WNT (and EDA) pathway disruption as an established ED cause, contextualizing LEF1 as a WNT effector. |
| [42283394](https://pubmed.ncbi.nlm.nih.gov/42283394/) | ROBO2 marker / DPC culture with WNT+FGF | LEF1 is a WNT-responsive readout (3.8-fold induction, p<0.01) in dermal papilla cells. |
| [42316873](https://pubmed.ncbi.nlm.nih.gov/42316873/) | Sphingomonas EVs and hair growth | LEF1/AXIN2 induced as canonical Wnt readouts in hair follicles. |
| [30622331](https://pubmed.ncbi.nlm.nih.gov/30622331/) | 10q24 duplication / SHFM spectrum | Epidemiologic anchor for the SHFM component (1/8,500–25,000). |
| [31420900](https://pubmed.ncbi.nlm.nih.gov/31420900/) | TP63 variant, SHFM + hypodontia | Key differential: TP63-related SHFM + hypodontia. |
| [31332306](https://pubmed.ncbi.nlm.nih.gov/31332306/) | SHFM molecular studies (LRP6, UBA2, WNT10B, TP63, DLX5) | Differential-diagnosis gene set for the limb phenotype. |
| [42110406](https://pubmed.ncbi.nlm.nih.gov/42110406/), [33294441](https://pubmed.ncbi.nlm.nih.gov/33294441/) | Novel TP63 variants in SHFM | Additional TP63 differential evidence. |
| [40844425](https://pubmed.ncbi.nlm.nih.gov/40844425/) | TCF/LEF in human vs rodent pluripotency | Cautions on mouse–human differences in TCF/LEF requirement. |

Peripheral LEF1 literature (cancer, T-cell memory, hair-growth pharmacology, β-catenin condensates) was reviewed to characterize LEF1 biology but does **not** bear directly on ECTD17 pathogenesis; it is retained only as supporting context for LEF1's role as a WNT/β-catenin transcriptional effector.

---

## Limitations and Knowledge Gaps

1. **Single-cohort evidence.** Essentially all disease-specific clinical/molecular evidence derives from one report of 12 individuals ([PMID: 35583550](https://pubmed.ncbi.nlm.nih.gov/35583550/)). Phenotype frequencies (e.g., split hand 3/12) are small-n and uncertain.
2. **No epidemiology.** Prevalence, incidence, penetrance, sex ratio, and demographic distribution are unknown.
3. **Genotype–phenotype resolution.** The two-mechanism model is well supported but based on limited variants; the full allelic series (especially missense variants affecting intermediate functions) is not yet mapped to outcomes.
4. **Limb-mechanism gap.** The precise WNT/LEF1 circuitry producing radial-ray/SHFM defects in humans is not experimentally resolved, and the mouse null fails to model it — leaving the limb causal step partly inferred.
5. **No molecular profiling beyond the founding study.** No independent transcriptomic, proteomic, epigenomic, or single-cell datasets specific to patient tissues exist.
6. **No therapeutics.** No disease-specific pharmacology, trials, or outcome data; QoL has not been formally measured.
7. **Model limitations.** Existing *Lef1*-null mice carry confounding phenotypes (lethality, CNS, cardiomyopathy) and do not recapitulate the limb phenotype; domain-selective/conditional alleles are needed.

---

## Proposed Follow-up Experiments / Actions

1. **Expand the patient registry.** Aggregate additional cases via GeneMatcher/Matchmaker Exchange to refine phenotype frequencies, penetrance, expressivity, and the allelic series, and to establish epidemiology.
2. **Functional allelic series.** Systematically test patient and engineered *LEF1* variants in parallel β-catenin-binding (pulldown), DNA-binding (HMG-box), and WNT-reporter/RNA-seq assays to place each variant on the dosage–severity axis (extending the Dufour framework).
3. **Domain-selective mouse models.** Generate knock-in alleles that selectively ablate β-catenin binding (aa 1–62) vs truncate the HMG box, plus limb-bud–conditional alleles, to test whether human-like domain-selective losses reproduce the limb phenotype that the complete null does not.
4. **Developmental limb circuitry.** Use limb-bud organoids / single-cell and spatial transcriptomics to define LEF1-dependent WNT targets in radial-ray and AER/ZPA programs, directly testing the inferred limb causal step.
5. **Variant curation.** Reclassify the "conflicting" p.Leu157fs and VUS p.Glu271Ter with functional data; apply PVS1/PM2 reasoning given extreme LoF intolerance.
6. **Clinical care pathway.** Develop a multidisciplinary surveillance protocol (dental, orthopedic/hand, dermatologic, cardiac, neurodevelopmental) and apply standardized QoL instruments to capture morbidity.
7. **Genetic counseling tooling.** Codify variant-class-based recurrence-risk counseling (AD vs AR) and consanguinity risk for the severe recessive form.

---

*Report compiled from 8 confirmed findings across 5 investigation iterations and 28 reviewed papers. Evidence source types: human clinical/molecular (Dufour et al. cohort; ClinVar; gnomAD), model organism (MGI *Lef1*-null), in vitro (WNT/LEF1 readout systems), and computational/ontology curation (MONDO, OMIM, UniProt, HPO, GO).*


## Artifacts

- [OpenScientist final report](LEF1_Ectodermal_Dysplasia_with_Limb_Malformations-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](LEF1_Ectodermal_Dysplasia_with_Limb_Malformations-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 47 |
| Terms named correctly | 30 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0010486` (1 mention) - the report calls it "Thenar muscle atrophy/hypoplasia"; HP calls it **Abnormality of the hypothenar eminence**
- `HP:0045025` (1 mention) - the report calls it "Sparse eyebrow"; HP calls it **Narrow palpebral fissure**
- `HP:0000028` (1 mention) - the report calls it "case(s)"; HP calls it **Cryptorchidism**
- `CL:0002332` (2 mentions) - the report calls it "dermal papilla cell"; CL calls it **multiciliated epithelial cell of the bronchus**
- `UBERON:0003823` (1 mention) - the report calls it "thenar / manus region"; UBERON calls it **hindlimb zeugopod**
- `NCIT:C15300` (1 mention) - the report calls it "Dental Procedure"; NCIT calls it **Photodynamic Therapy**
- `NCIT:C15733` (2 mentions) - the report calls it "Supportive Care"; NCIT calls it **Diagnostic Trial**
- `NCIT:C50743` (1 mention) - the report calls it "Ductus Arteriosus Repair"; NCIT calls it **Skin Irritation**
- `NCIT:C15417` (1 mention) - the report calls it "Genetic Counseling"; NCIT calls it **Randomized Clinical Trial**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002984` (1 mention) - the report calls it "Hypoplasia of the radius / radial ray"; HP calls it **Hypoplasia of the radius**
- `GO:0008013` (2 mentions) - the report calls it "Molecular function: beta-catenin binding", "beta-catenin binding"; GO calls it **beta-catenin binding**
- `GO:0060070` (2 mentions) - the report calls it "Biological process: canonical Wnt signaling", "canonical Wnt signaling"; GO calls it **canonical Wnt signaling pathway**
- `GO:0001837` (3 mentions) - the report calls it "epithelial–mesenchymal transition"; GO calls it **epithelial to mesenchymal transition**, and lists "epithelial-mesenchymal transition" among its other names
- `CL:0000062` (1 mention) - the report calls it "odontoblast"; CL calls it **osteoblast**
- `UBERON:0001091` (1 mention) - the report calls it "tooth"; UBERON calls it **calcareous tooth**, and lists "tooth" among its other names
- `NCIT:C15329` (1 mention) - the report calls it "Orthopedic Surgery"; NCIT calls it **Surgical Procedure**, and lists "Type of Surgery" among its other names
- `NCIT:C15351` (1 mention) - the report calls it "Rehabilitation Therapy"; NCIT calls it **Adoptive Immunotherapy**, and lists "ACT Therapy" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0008013` - called "Molecular function: beta-catenin binding", "beta-catenin binding"
- `GO:0060070` - called "Biological process: canonical Wnt signaling", "canonical Wnt signaling"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.