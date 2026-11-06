---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:28:53.426346'
end_time: '2026-11-04T18:51:19.615386'
duration_seconds: 1346.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: RDH12-Related Dominant Retinopathy
  mondo_id: MONDO:0800100
  category: Mendelian
  causal_genes: RDH12
  omim_id: not recorded
  synonyms: autosomal dominant RDH12-related retinal dystrophy
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
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 13
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 36
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 4
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0800100
    reported_labels:
    - RDH12-related dominant retinopathy
    - Fingert 2008; Muthiah 2022
    ontology_label: RDH12-related dominant retinopathy
  - term_id: HP:0000548
    reported_labels:
    - Reduced along temporal meridian vs normative
    ontology_label: Cone/cone-rod dystrophy
  - term_id: UBERON:0000970
    reported_labels:
    - Organ level:** Eye
    ontology_label: eye
  - term_id: UBERON:0005396
    reported_labels:
    - macula lutea
    ontology_label: carotid artery segment
  labels_variant: 3
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
  path: RDH12-Related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: RDH12-Related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RDH12-Related Dominant Retinopathy
- **MONDO ID:** MONDO:0800100 (if available)
- **Causal gene(s):** RDH12
- **OMIM:** not recorded
- **Synonyms:** autosomal dominant RDH12-related retinal dystrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **RDH12-Related Dominant Retinopathy** covering all of the
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

# RDH12-Related Dominant Retinopathy (MONDO:0800100): Comprehensive Disease Characterization

**Causal gene: _RDH12_ (retinol dehydrogenase 12; HGNC:19977; NCBI Gene 145226; Ensembl ENSG00000139988; UniProt Q96NR8; chromosome 14q24.1).**

> **Scope note.** This report concerns the **autosomal dominant** retinopathy caused by heterozygous *RDH12* variants (MONDO:0800100), an allelic but distinct entity from the far more common **autosomal recessive** *RDH12*-associated Leber congenital amaurosis/early-onset severe retinal dystrophy (LCA13; OMIM #612712). Because the dominant form is rare, much of the molecular and mechanistic literature is shared between the two and is drawn from the recessive/cell/animal literature; the distinction is made explicit throughout. Evidence source types are labeled: **[human clinical]**, **[in vitro]**, **[model organism]**, **[computational]**.

---

## 1. Disease Information

**Overview.** RDH12-related dominant retinopathy is a rare inherited retinal dystrophy (IRD) transmitted in an autosomal dominant fashion and caused by specific heterozygous C-terminal frameshift variants in *RDH12*. Clinically it is a **comparatively mild, late(r)-onset rod–cone dystrophy / retinitis pigmentosa** with variable expressivity and incomplete penetrance — in sharp contrast to the severe, blinding, childhood-onset recessive disease caused by biallelic *RDH12* loss-of-function. The first dominant family (Fingert et al. 2008, **PMID 18779497** [human clinical]) had "a mild form of RP" with "late onset and relatively mild severity … dramatically different from the other disease associated with mutation in this gene, autosomal recessive Leber congenital amaurosis." The most completely characterized dominant pedigree (Muthiah et al. 2022, **PMID 34031043** [human clinical]) reclassified the phenotype as a rod–cone dystrophy with variable expression.

**Key identifiers.**
- **MONDO:** MONDO:0800100 (RDH12-related dominant retinopathy).
- **Gene OMIM:** *RDH12* 608830. **Phenotype OMIM:** no distinct dominant phenotype MIM number is currently assigned; the recessive allelic disorder is "Leber congenital amaurosis 13" OMIM #612712. The dominant RP is described in the literature but not given its own MIM phenotype number (consistent with the template note "OMIM: not recorded").
- **Orphanet:** No dominant-specific ORPHA code; related umbrella entities are retinitis pigmentosa (ORPHA:791) and Leber congenital amaurosis (ORPHA:65).
- **ICD-11:** 9B70 Retinitis pigmentosa / hereditary retinal dystrophy (9B70.0). **ICD-10:** H35.52 (pigmentary retinal dystrophy).
- **MeSH:** Retinitis Pigmentosa (D012174); Retinal Dystrophies (D058499).
- **HGNC:** 19977. **UniProt:** Q96NR8.

**Synonyms / alternative names.** Autosomal dominant RDH12-related retinal dystrophy; autosomal dominant RDH12 retinopathy; RDH12-associated autosomal dominant retinitis pigmentosa; RDH12 rod–cone dystrophy (dominant).

**Information source.** Disease-level aggregated resources (OMIM, ClinVar, gnomAD, Ensembl) plus **individual-patient** case series/pedigree studies (Fingert 2008; Muthiah 2022). No EHR-scale datasets exist for this ultra-rare entity.

---

## 2. Etiology

**Primary cause — genetic.** The disease is monogenic/Mendelian, caused by **heterozygous pathogenic variants in *RDH12***. Reported dominant alleles are C-terminal single-nucleotide frameshifts clustering around codons 253–260:
- **c.776delG (776delG)** — original dominant family (Fingert et al. 2008, PMID 18779497) [human clinical].
- **c.763delG** — four-generation British pedigree (Muthiah et al. 2022, PMID 34031043) [human clinical].
- **c.759del, p.(Phe254Leufs*24)** — dominant RP patient used to derive iPSC line UCLi014-A (Sarkar et al. 2021, PMID 34216980) [human clinical / in vitro].

**Risk factors.**
- *Genetic:* The causal heterozygous *RDH12* frameshift is the sole established determinant. A positive **family history** is the dominant risk indicator. No susceptibility loci or validated modifier genes are reported for the dominant form.
- *Environmental/other:* No proven environmental, occupational, infectious, lifestyle, age, or sex risk factors. **Light exposure** is a biologically plausible modulator (RDH12 detoxifies light-generated retinaldehyde; Rdh12⁻/⁻ mice show light-induced photoreceptor apoptosis — Maeda et al. 2006, PMID 17032653 [model organism]), but no clinical evidence links ambient light to dominant-disease severity.

**Protective factors.** None established. Genotype itself is protective relative to the recessive disease: within the recessive spectrum, homozygosity for the hypomorphic p.Leu99Ile allele is associated with milder, later disease (Daich Varela et al. 2024, PMID 37714431 [human clinical]).

**Gene–environment interactions.** Not formally characterized. The inferred interaction is **light/oxidative load × RDH12 dysfunction → aldehyde-driven photoreceptor stress** (inferred, not demonstrated in dominant patients).

---

## 3. Phenotypes

The dominant phenotype is a **mild rod–cone dystrophy / retinitis pigmentosa** (Muthiah 2022, PMID 34031043; Fingert 2008, PMID 18779497) [human clinical]. Key features, with suggested HPO terms:

| Phenotype | Type | Characteristics (onset / severity / course / frequency) | HPO |
|---|---|---|---|
| Rod–cone dystrophy / retinitis pigmentosa | clinical sign | Adult/late onset; mild–moderate; slowly progressive; defining feature | HP:0000510 (Retinitis pigmentosa), HP:0000548 (Cone/cone-rod dystrophy) |
| Reduced/constricted visual field | sign | Progressive peripheral constriction; present in affected adults | HP:0001133 (Constriction of peripheral visual field), HP:0001123 (Visual field defect) |
| Relatively preserved central visual acuity | sign | VA −0.1 to 0.2 logMAR in affected (much better than recessive) | HP:0000505 (Visual impairment, mild) |
| Macular/parafoveal atrophy; perifoveal hypo-autofluorescence with hyper-AF ring | sign (imaging) | Progressive; parafoveal/peripapillary hyper-AF ring → enlarging perifoveal hypo-AF | HP:0007754 (Macular dystrophy), HP:0030506 (Yellow/altered autofluorescence) |
| Outer retinal / outer nuclear layer thinning (OCT) | sign (imaging) | Mild foveal total-retinal and ONL thinning | HP:0030466 (Abnormal full-field ERG), HP:0011512 (abnormal photoreceptor) |
| Reduced cone density (adaptive optics) | sign (imaging) | Reduced along temporal meridian vs normative | HP:0000548 |
| Rod–cone ERG dysfunction | lab/electrophysiology | Rod-cone pattern; peripheral macular dysfunction on pattern ERG | HP:0000512 (Abnormal electroretinogram), HP:0007984 (abnormal retinal physiology) |
| Nyctalopia (night blindness) | symptom | Typical of rod-predominant dystrophy | HP:0000662 (Nyctalopia) |

Note: The dominant disease generally **lacks** the devastating early features of recessive RDH12-LCA (congenital/early childhood blindness, universal macular atrophy from age 2, non-recordable ERG in infancy, dense bone-spicule pigmentation) documented in Fahim et al. 2019 (PMID 30979730) and Daich Varela & Michaelides 2022 (PMID 35491887) [human clinical].

**Quality-of-life impact.** Progressive peripheral field loss and night blindness impair mobility and night driving; relatively preserved central acuity means reading/face recognition are often retained longer than in the recessive disease. No disease-specific EQ-5D/SF-36/PROMIS data exist for the dominant form; IRDs broadly reduce vision-related QoL (NEI-VFQ).

---

## 4. Genetic / Molecular Information

**Causal gene.** *RDH12* (HGNC:19977; OMIM 608830; Ensembl ENSG00000139988; chr14:67,701,886–67,734,451, GRCh38 [computational, gnomAD]). Encodes a 316-aa NADPH-dependent retinal reductase of the short-chain dehydrogenase/reductase (SDR) superfamily (UniProt Q96NR8; Pfam PF00106/adh_short; InterPro IPR002347).

**Pathogenic variants (dominant).** Heterozygous **frameshift** C-terminal variants: c.776delG, c.763delG, c.759del p.(Phe254Leufs*24). These lie in the final coding region and are predicted to **escape nonsense-mediated decay (NMD)**, producing a stable, altered truncated protein [computational inference].
- *ACMG classification:* dominant alleles are rare/private and functionally supported; recessive frameshifts here are classified Pathogenic/Likely pathogenic in ClinVar.
- *Allele frequency:* dominant alleles are essentially **absent from population databases** (Fingert: not in 158 controls; gnomAD does not list these as recurrent) — consistent with private, family-specific mutations.
- *Origin:* **germline**, segregating through pedigrees (AD). No somatic involvement.
- *Functional consequence:* **predicted gain of function / dominant-negative** (Muthiah 2022, PMID 34031043): "predicted to result in a gain of function, that causes disease in a gene typically associated with biallelic (recessive) variants." Supported by **gnomAD constraint** [computational]: pLI = 7.8×10⁻⁵, LOEUF (oe_lof upper) = 0.889, obs/exp LoF = 0.617 — RDH12 **tolerates heterozygous LoF**, so haploinsufficiency is not the mechanism.

**Variant landscape (gene-wide, mostly recessive).** ClinVar lists 674 variants for RDH12 [computational], dominated by frameshift and missense alleles distributed across the coding sequence (e.g., c.43del p.Leu15Cysfs*4; c.146T>C p.Leu49Ser; c.295C>A p.Leu99Ile; c.701G>A p.Arg234His; c.759del p.Phe254Leufs*24). The recessive common allele **p.Leu99Ile (c.295C>A)** was the most frequent variant (52/… alleles) in a South American cohort (Daich Varela et al. 2024, PMID 37714431) [human clinical].

**Modifier genes / epigenetics / chromosomal abnormalities.** None established for the dominant disease. No DNA-methylation/histone or large structural (CNV/translocation) mechanisms are implicated; a heterozygous *RDH12* deletion has been reported in the recessive/compound setting (Sarkar et al. 2020, PMID 32322264).

**Suggested ontology terms.** Gene product GO: GO:0004745 (NAD(P)+-retinol dehydrogenase / all-trans-retinol dehydrogenase activity), GO:0052650 (all-trans-retinol dehydrogenase (NADP+) activity), GO:0042574 (retinal metabolic process), GO:0007601 (visual perception).

---

## 5. Environmental Information

No established environmental, toxic, radiation, occupational, dietary, lifestyle, or infectious causes/triggers. The only biologically relevant exogenous factor is **light**, which generates the all-trans-retinal substrate that RDH12 detoxifies (inferred modulator; CHEBI:17898 all-trans-retinal). No infectious agents are involved. [No data available for this disease specifically.]

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **heterozygous C-terminal frameshift** in *RDH12* (e.g., c.763delG, c.776delG, c.759del) **results in** an mRNA that **escapes nonsense-mediated decay** (last-exon rule) *(inferred)*.
2. This **leads to** expression of a **stable mutant RDH12 protein with an altered/extended C-terminus** (the C-terminus contains the amphipathic membrane-association region) *(inferred; protein-level data limited)*.
3. The mutant protein **acts via a predicted gain-of-function / dominant-negative mechanism** — it is **not** simple haploinsufficiency, because gnomAD shows RDH12 tolerates heterozygous LoF (pLI≈0) and recessive-allele carriers are unaffected **[computational support]**. The mutant is inferred to **mislocalize and/or poison** normal retinoid handling in the photoreceptor inner segment *(inferred)*.
4. Reduced effective RDH12 reductase activity **results in** impaired reduction of **all-trans-retinal (atRAL) → all-trans-retinol (atROL)** in the inner segment **[in vitro: Belyaeva 2005 PMID 15865448; Sarkar 2021 PMID 34445569]**.
5. atRAL and reactive lipid-peroxidation aldehydes (e.g., 4-HNE) **accumulate**, which **leads to** cytotoxicity and disrupted retinoid homeostasis **[in vitro: Lee 2008 PMID 18396173]**.
6. Aldehyde accumulation **induces oxidative stress and the ER unfolded-protein response** (upregulation of sXBP1, CHOP/DDIT3, ATF4) **[in vitro: Sarkar 2021 PMID 34445569]**.
7. Oxidative + ER stress **results in photoreceptor apoptosis**, branching to **rod-predominant degeneration** first (night blindness, peripheral field loss) and **cone/macular involvement** (central atrophy, reduced cone density) **[model organism: zebrafish rdh12; human clinical: Muthiah 2022]**.
8. Progressive photoreceptor loss **manifests clinically as** a slowly progressive rod–cone dystrophy/RP with macular atrophy — milder than the recessive disease because residual wild-type RDH12 and partial function persist *(inferred)*.

**Branch (recessive comparison):** biallelic LoF → near-complete loss of RDH12 → severe early atRAL/aldehyde toxicity → fulminant childhood macular atrophy and LCA (Fahim 2019, PMID 30979730).

### Mechanistic detail by category
- **Molecular pathways / biochemistry:** Visual (retinoid) cycle; RDH12 reduces atRAL using NADPH (~2000-fold NADP(H) preference; highest catalytic efficiency for all-trans-retinal kcat/Km ≈ 900 min⁻¹ µM⁻¹) (Belyaeva 2005, PMID 15865448) [in vitro]. KEGG "Retinol metabolism" (hsa00830); Reactome "The canonical retinoid cycle in rods."
- **Cellular processes:** apoptosis (GO:0006915), response to oxidative stress (GO:0006979/GO:0034599), ER unfolded-protein response (GO:0030968), autophagy alteration (reduced atg12), photoreceptor outer-segment phagocytosis disruption.
- **Protein dysfunction:** loss of enzymatic reductase activity in mutants; for dominant alleles, a **gain-of-function/dominant-negative** stable product (vs misfolding/degradation seen with some missense recessive alleles).
- **Metabolic changes:** accumulation of all-trans-retinal (CHEBI:17898) and toxic aldehydes (4-hydroxynonenal, CHEBI:58266); disturbed retinyl ester/retinoic acid balance (Lee 2008, PMID 18396173).
- **Immune involvement:** none primary.
- **Tissue-damage mechanism:** oxidative stress + aldehyde toxicity + ER stress → photoreceptor cell death.
- **Molecular profiling:** iPSC lines (PMID 34216980) and HEK/ARPE-19 models (PMID 34445569; PMID 41683787) provide expression/functional data; no patient tissue transcriptomics/proteomics/metabolomics for the dominant form.

**Cell types (CL):** photoreceptor cell (CL:0000210), rod (CL:0000604), cone (CL:0000573); adjacent retinal pigment epithelial cell (CL:0002586). **Subcellular (GO CC):** photoreceptor inner segment (GO:0001917), endoplasmic reticulum membrane (GO:0005789), smooth ER / membrane-anchored.

---

## 7. Anatomical Structures Affected

- **Organ level:** Eye (UBERON:0000970); specifically the **retina** (UBERON:0000966) and **macula lutea** (UBERON:0005396). Primary disease is confined to the eye; no systemic/secondary organ involvement (non-syndromic).
- **Tissue/cell level:** Neural retina — **photoreceptor layer**; rod and cone photoreceptors (CL:0000604, CL:0000573); secondary RPE changes and inner retinal remodeling. **Peripapillary sparing** and **macular/parafoveal atrophy** are characteristic patterns.
- **Subcellular:** Photoreceptor **inner segment** (RDH12 localization; GO:0001917), ER (stress response).
- **Localization & laterality:** **Bilateral and symmetric** (HP:0012832 Bilateral). Regional: parafoveal/perifoveal and peripapillary (macula UBERON:0005396; optic disc region).

---

## 8. Temporal Development

- **Onset:** Adult/late onset for the dominant disease — "late onset and relatively mild severity" (Fingert 2008, PMID 18779497). Variable; some mutation carriers are detectable only subclinically (e.g., on adaptive optics) reflecting **incomplete penetrance** (Muthiah 2022, PMID 34031043). Pattern is **insidious/chronic**. (Contrast recessive: congenital/early-childhood onset, mean 4.1 yr — Fahim 2019, PMID 30979730.)
- **Progression:** Slowly **progressive** over decades; stages = early (ring of hyper-AF, mild field constriction) → intermediate (enlarging perifoveal atrophy, ONL thinning) → advanced (extensive outer-retinal atrophy, significant field loss) with relative central-acuity preservation until late. Lifelong chronic disease; no remission.
- **Critical periods / intervention window:** Because photoreceptors persist for decades, there is a **wide therapeutic window** for the dominant disease (in contrast to the narrow infantile window in recessive disease, where early macular atrophy limits gene-replacement benefit).

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal dominant** (AD) for MONDO:0800100 (Fingert 2008; Muthiah 2022). The gene far more commonly causes **autosomal recessive** LCA13.
- **Penetrance:** **Incomplete / age-dependent**; penetrance determination is modality-dependent (subclinical carriers detected only by adaptive optics) (Muthiah 2022, PMID 34031043).
- **Expressivity:** **Variable** (Muthiah 2022).
- **Anticipation:** None reported (not a repeat-expansion disorder).
- **Germline mosaicism / founder effects / consanguinity:** No founder effect or consanguinity role for the dominant alleles (private mutations; AD does not require consanguinity). Consanguinity is relevant only to the recessive disease.
- **Carrier frequency:** Not applicable in the AD sense (dominant alleles are private). For recessive disease, heterozygous LoF carriers exist in gnomAD but are unaffected.
- **Epidemiology / prevalence:** **No reliable prevalence/incidence estimate** exists for the dominant form — it is described in only a handful of pedigrees worldwide (ultra-rare). As gene-level context, **RDH12 accounts for 3.4%–10.5% of LCA/EOSRD** (Fahim 2019, PMID 30979730) — but these are predominantly recessive cases.
- **Demographics:** Reported dominant families are of European (British/US) ancestry; too few to infer ethnic predilection, geographic clustering, sex ratio (expected ~1:1 for AD), or age distribution.

---

## 10. Diagnostics

- **Clinical/imaging tests (core):**
  - **Fundus autofluorescence (FAF):** parafoveal/peripapillary hyper-AF ring, perifoveal hypo-AF (Muthiah 2022).
  - **Spectral-domain OCT:** foveal total-retinal and ONL thinning; outer-retinal disruption.
  - **Adaptive optics scanning light ophthalmoscopy:** reduced cone density (sensitive for subclinical carriers).
  - **Full-field & pattern ERG:** rod–cone pattern of dysfunction; peripheral macular dysfunction.
  - **Visual fields (perimetry):** peripheral constriction.
  - Fundus photography: variable pigmentary changes/macular atrophy.
- **Laboratory/biomarkers:** No blood/urine biomarker or enzyme assay; diagnosis is clinical + genetic. (Research biomarker: all-trans-retinal/aldehyde handling, not clinical.)
- **Genetic testing (definitive):** **Single-gene / IRD gene-panel next-generation sequencing**, **whole-exome (WES)** and **whole-genome sequencing (WGS)** identify the heterozygous *RDH12* frameshift; segregation analysis across the pedigree confirms dominant transmission (Muthiah 2022 used NGS incl. WGS). Chromosomal microarray/karyotype/FISH/mtDNA/repeat-expansion testing are **not indicated** (point-level frameshift mechanism). RNA studies can confirm NMD escape (research).
- **Clinical criteria / differential diagnosis:** No disease-specific criteria. Differentials: other dominant RP genes (RHO, PRPH2, RP1, PRPF31, NR2E3), cone–rod dystrophy genes (GUCA1A, CRX), and — critically — **recessive RDH12-LCA/EOSRD** (distinguished by congenital/severe early onset, universal early macular atrophy, non-recordable infantile ERG, biallelic variants). Genotyping + segregation resolves these.
- **Screening:** Cascade genetic testing of at-risk relatives in known pedigrees (with adaptive-optics/FAF to detect subclinical carriers). No population newborn/carrier screening (ultra-rare, AD, private alleles).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** **Not life-limiting**; normal life expectancy. No disease-specific mortality (eye-restricted disorder).
- **Morbidity/function:** Chronic visual disability — progressive peripheral field loss and nyctalopia with **relatively preserved central acuity**; prognosis is markedly **better than the recessive disease**, which causes childhood legal blindness. Within recessive RDH12, p.Leu99Ile homozygotes reach legal blindness at an older age (Daich Varela 2024, PMID 37714431) [human clinical].
- **Disease course/complications:** Slowly progressive outer-retinal atrophy; possible late cystoid macular changes/cataract (general RP complications). No spontaneous recovery.
- **Prognostic factors:** Specific variant, age, extent of macular atrophy on OCT/FAF, cone density on AO, residual field/ERG amplitude. No validated molecular prognostic biomarker.
- **QoL measures:** No dominant-form-specific instruments reported; NEI-VFQ-25 applicable clinically.

---

## 12. Treatment

**No approved disease-specific therapy exists** for RDH12 retinopathy (Daich Varela & Michaelides 2022, PMID 35491887: "There is currently no treatment available for RDH12-retinopathy") [human clinical review].

- **Supportive/rehabilitative (standard of care):** low-vision aids, orientation & mobility training, occupational therapy, refraction/glare control (tinted lenses), management of cataract/cystoid macular edema, genetic counseling. NCIT: C15277 (Rehabilitation Therapy), C15296 (Supportive Care).
- **Pharmacotherapy / mechanism-based (experimental, in vitro):** **Aldehyde/retinaldehyde scavengers** — **pregabalin** attenuated atRAL-induced ER stress in mutant RDH12 cells (Sarkar 2021, PMID 34445569) [in vitro]; conceptually related scavengers (e.g., primary-amine trap drugs). Antioxidants/ER-stress modulators are candidate strategies. No clinical trials for the dominant form. NCIT: C47484 (Pregabalin); C275 (Antioxidant).
- **Gene therapy:** **AAV-mediated *RDH12* gene augmentation** is in preclinical development (patents held by Ali and Thompson groups per Fahim 2019, PMID 30979730; in-vitro rAAV-RDH12 functional studies, Pavlova et al. 2026, PMID 41683787) [in vitro / preclinical]. **Caveat:** gene *augmentation* (adding wild-type) treats loss-of-function recessive disease but may be **insufficient for a dominant gain-of-function allele**, which may instead require **allele-specific knockdown/editing** (ASO, siRNA, CRISPR). NCIT: C15431 (Gene Therapy); C117202 (AAV Vector).
- **Cell therapy / other advanced modalities:** iPSC-derived retinal models exist for drug screening (PMID 34216980) but no clinical cell therapy. Not applicable: immunotherapy, targeted small molecules, surgery (beyond cataract).
- **Pharmacogenomics:** Not applicable.

---

## 13. Prevention

- **Primary prevention:** Not possible for a germline Mendelian disorder. **Genetic counseling** for affected AD families (50% transmission risk) with options for **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)**. NCIT: C15265 (Genetic Counseling).
- **Secondary prevention:** **Cascade genetic testing** and ophthalmic surveillance (FAF/OCT/AO) of at-risk relatives for early detection; monitor for treatable complications (cataract, CME).
- **Tertiary prevention:** Low-vision rehabilitation; avoidance of excessive light exposure is biologically rational (RDH12 clears light-generated aldehydes) though unproven clinically.
- **Immunization / public-health / behavioral / prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** *RDH12* is conserved in vertebrates — human (NCBI Gene 145226; *Homo sapiens* NCBI:txid9606), mouse *Rdh12* (NCBI Gene 77974; *Mus musculus* NCBI:txid10090), zebrafish *rdh12* (*Danio rerio* NCBI:txid7955). Orthology: Alliance of Genome Resources / HomoloGene.
- **Natural disease in other species:** No well-established naturally occurring *RDH12* retinopathy is cataloged in companion animals (no prominent OMIA entry); disease knowledge is from engineered models rather than spontaneous animal disease.
- **Comparative biology:** The retinoid (visual) cycle and RDH12's atRAL-reductase role are evolutionarily conserved; however, **mice do not recapitulate human severity** (redundancy with other RDHs, lower retinoid flux), a key cross-species difference.
- **Transmission:** Not applicable (non-infectious, non-zoonotic).

---

## 15. Model Organisms

- **Mouse (mammalian):** *Rdh12*-knockout mice (MGI) — **mild phenotype that fails to recapitulate human disease**: slowed atRAL reduction and delayed dark adaptation, accelerated 11-cis-retinal production, and **increased susceptibility to light-induced photoreceptor apoptosis** (Maeda et al. 2006, PMID 17032653); grossly normal retinal histology at 10 months with normal ERG and retinoid levels (Kurth et al. 2007, PMID 17130236) [model organism]. *Limitation:* no spontaneous severe degeneration → poor efficacy model; useful for light-damage and retinoid-flux studies.
- **Zebrafish:** CRISPR-Cas9 *rdh12* mutant (*rdh12^u533*, c.17_23del; p.(Val6AlafsTer5)) shows disrupted outer-segment phagocytosis, rhodopsin mislocalization, reduced atg12/sod2 — **early rod-predominant degeneration** (Sarkar et al. 2021, PMID 34445569) [model organism]. Better captures degeneration/oxidative-ER-stress phenotype.
- **Cellular / in vitro:** HEK-293 and ARPE-19 lines expressing WT vs mutant RDH12 for atRAL-toxicity, oxidative/ER-stress, and rAAV-RDH12 functional assays (PMID 34445569; PMID 41683787); purified-enzyme kinetics (PMID 15865448).
- **iPSC / organoids:** Patient-derived iPSC line **UCLi014-A** from a dominant-RP patient (heterozygous c.759del p.(Phe254Leufs*24)) and **UCLi015-A** from a recessive-LCA patient (Sarkar et al. 2021, PMID 34216980) — enabling retinal-organoid disease modeling, mechanism comparison, and drug screening [in vitro]. **This dominant-patient iPSC line is the most directly relevant model for MONDO:0800100.**
- **Model databases:** MGI (mouse), ZFIN (zebrafish), Cellosaurus (iPSC lines), Alliance of Genome Resources.

---

## Summary of Evidence Types & Key Citations
- **Human clinical:** PMID 18779497 (Fingert 2008, first dominant family, 776delG); PMID 34031043 (Muthiah 2022, c.763delG, deep phenotyping, GoF prediction); PMID 34216980 (dominant-patient iPSC, c.759del); PMID 30979730 (recessive natural history; RDH12 = 3.4–10.5% of LCA/EOSRD); PMID 37714431 (South American cohort, p.Leu99Ile); PMID 35491887 (review, no treatment).
- **In vitro:** PMID 15865448 (enzyme kinetics); PMID 18396173 (4-HNE/aldehyde toxicity); PMID 34445569 (oxidative/ER stress, pregabalin rescue + zebrafish); PMID 41683787 (rAAV-RDH12).
- **Model organism:** PMID 17032653 (light-induced apoptosis KO mouse); PMID 17130236 (KO mouse normal histology).
- **Computational / population genetics:** gnomAD constraint (pLI≈0, LOEUF 0.89) — RDH12 tolerant of heterozygous LoF, arguing against haploinsufficiency.

## Limitations
- The dominant entity is **ultra-rare** (a few pedigrees); phenotype, penetrance, natural history, and epidemiology are based on small samples.
- The **gain-of-function/dominant-negative mechanism is predicted/inferred**, not experimentally proven at the protein level for the dominant alleles.
- Most mechanistic/therapeutic data derive from **recessive, cell, or animal** contexts and are extrapolated to the dominant disease.
- No prevalence/incidence, QoL, or clinical-trial outcome data specific to the dominant form.

## Future Directions
- Protein-level studies (localization, stability, dominant-negative testing) of c.763delG/c.776delG/c.759del, ideally in patient iPSC-derived retinal organoids (UCLi014-A).
- Allele-specific silencing/editing strategies appropriate to a dominant GoF allele, and testing aldehyde scavengers/antioxidants.
- Natural-history registries and standardized imaging/functional outcome measures for the dominant phenotype.


## Artifacts

- [OpenScientist final report](RDH12-Related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](RDH12-Related_Dominant_Retinopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 11 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0800100` (5 mentions) - the report calls it "RDH12-related dominant retinopathy", "Fingert 2008; Muthiah 2022"; MONDO calls it **RDH12-related dominant retinopathy**
- `HP:0000548` (2 mentions) - the report calls it "Reduced along temporal meridian vs normative"; HP calls it **Cone/cone-rod dystrophy**
- `UBERON:0000970` (1 mention) - the report calls it "Organ level:** Eye"; UBERON calls it **eye**
- `UBERON:0005396` (2 mentions) - the report calls it "macula lutea"; UBERON calls it **carotid artery segment**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000505` (1 mention) - the report calls it "Visual impairment, mild"; HP calls it **Visual impairment**
- `CHEBI:17898` (2 mentions) - the report calls it "Metabolic changes:** accumulation of all-trans-retinal"; CHEBI calls it **all-trans-retinal**
- `GO:0006915` (1 mention) - the report calls it "Cellular processes:** apoptosis"; GO calls it **apoptotic process**, and lists "activation of apoptosis" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0800100` - called "RDH12-related dominant retinopathy", "Fingert 2008; Muthiah 2022"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.