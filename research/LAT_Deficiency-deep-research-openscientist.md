---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-29T20:37:56.261190'
end_time: '2026-09-29T20:59:52.615580'
duration_seconds: 1316.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: LAT Deficiency
  mondo_id: MONDO:0044721
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
citation_count: 13
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 11
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 32
  labels_matching: 15
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: MONDO:0044721
    reported_labels:
    - MONDO
    ontology_label: severe combined immunodeficiency due to LAT deficiency
  - term_id: HP:0004810
    reported_labels:
    - Lab/clinical
    ontology_label: Congenital hypoplastic anemia
  - term_id: HP:0001973
    reported_labels:
    - Lab/clinical
    ontology_label: Autoimmune thrombocytopenia
  - term_id: HP:0002716
    reported_labels:
    - Physical sign
    ontology_label: Lymphadenopathy
  - term_id: HP:0002110
    reported_labels:
    - Physical sign
    ontology_label: Bronchiectasis
  - term_id: HP:0011355
    reported_labels:
    - Physical manifestation
    ontology_label: Localized skin lesion
  - term_id: HP:0005403
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased total T cell count
  - term_id: HP:0001880
    reported_labels:
    - Lab abnormality
    ontology_label: Increased total eosinophil count
  - term_id: HP:0003212
    reported_labels:
    - Lab abnormality
    ontology_label: Increased circulating IgE concentration
  - term_id: HP:0002720
    reported_labels:
    - Lab abnormality
    ontology_label: Decreased circulating IgA concentration
  labels_variant: 7
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: LAT_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: LAT_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** LAT Deficiency
- **MONDO ID:** MONDO:0044721 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **LAT Deficiency** covering all of the
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

# LAT Deficiency (Immunodeficiency-52): A Comprehensive Disease Characterization

**Disease:** LAT Deficiency · **MONDO:** MONDO:0044721 · **OMIM:** #617514 (Immunodeficiency-52) · **ORPHA:** 504523 · **Gene:** *LAT* (HGNC:6533) · **Category:** Mendelian, autosomal recessive inborn error of immunity

---

## Summary

**LAT deficiency is an ultra-rare (<1/1,000,000) autosomal-recessive inborn error of immunity caused by biallelic loss-of-function (truncating) mutations in *LAT* (Linker for Activation of T cells; chromosome 16p11.2), the transmembrane adaptor protein that nucleates the T-cell receptor (TCR) signalosome.** Loss of LAT abolishes ERK/Ras-MAPK signaling and cripples PLCγ1-dependent Ca²⁺/NFAT signaling downstream of ZAP-70, producing a paradoxical clinical picture: a combined immunodeficiency (T–B+NK+ SCID with recurrent and opportunistic infections) coexisting with severe Th2-skewed immune dysregulation (autoimmune cytopenias, lymphoproliferation, hypergammaglobulinemia, elevated IgE).

The disease was first described in humans in 2016 (Keller et al., three siblings of a consanguineous family) and has since been confirmed in at least two additional independent consanguineous kindreds (Bacchelli 2017; Alizadeh 2023), giving a worldwide total of fewer than ~20 reported patients. In every case the variants are germline, biallelic, and truncating (nonsense or frameshift), removing the cytoplasmic tail of LAT with its critical signaling tyrosines; parents are asymptomatic heterozygous carriers. Symptom onset is in the first months of life (5–10 months in the index kindred), and the disease is usually fatal in early childhood without allogeneic hematopoietic stem cell transplantation (HSCT), which is the only curative treatment.

The human disease sits mechanistically between two long-studied mouse models: the complete *Lat*-null knockout (which arrests thymocyte development, modeling the immunodeficiency arm) and the *Lat*Y136F knock-in (which disrupts only the PLCγ1 docking site and produces a Th2 lymphoproliferative/autoimmune syndrome, modeling the autoimmunity arm). This dual phenotype reflects LAT's dual biological role as **both a positive activator and a negative homeostatic regulator** of TCR signaling. Because LAT deficiency causes T-cell lymphopenia, it is detectable by population-based TREC (T-cell receptor excision circle) newborn screening for SCID, enabling early diagnosis and pre-symptomatic transplantation, which markedly improves survival.

---

## Section 1 — Disease Information

**Overview.** LAT deficiency is a Mendelian primary immunodeficiency (inborn error of immunity) in which the T-cell receptor signaling adaptor LAT is absent or non-functional. It manifests as a combined immunodeficiency accompanied by severe, often early and dominant, autoimmune/immune-dysregulatory disease. Depending on the residual T-cell output, patients are classified along a spectrum from "combined immunodeficiency with autoimmunity" to frank T–B+NK+ severe combined immunodeficiency (SCID).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| OMIM (phenotype) | #617514 — IMMUNODEFICIENCY 52 (IMD52) |
| OMIM (gene) | *602354 (*LAT*) |
| Orphanet | ORPHA:504523 — "T-B+NK+ severe combined immunodeficiency due to LAT deficiency" |
| MONDO | MONDO:0044721 |
| ICD-10 | D81.2 (other combined immunodeficiencies) |
| ICD-11 | 4A01.10 |
| UMLS / GTR | C4479588 |
| GARD | 17938 |
| Gene | *LAT*, HGNC:6533, NCBI Gene 27040, UniProt O43561, chromosome 16p11.2 |

**Synonyms / alternative names.** Immunodeficiency 52 (IMD52); combined immunodeficiency due to LAT deficiency; T-B+NK+ SCID due to LAT deficiency; LAT signalosome deficiency. (LAT = "Linker for Activation of T cells.")

**Data source.** All information derives from aggregated disease-level resources (OMIM, Orphanet) and individual patient case reports/kindreds in the primary literature — there is no EHR/registry-level dataset for this ultra-rare condition. Evidence is a mixture of **human clinical** case reports and mechanistic **model-organism** (mouse) and **in vitro** studies.

---

## Section 2 — Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound heterozygous) loss-of-function mutations in *LAT*. All reported families to date were consanguineous, so the operative genetic mechanism is homozygosity-by-descent of a truncating allele ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/); [PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/); [PMID: 37516813](https://pubmed.ncbi.nlm.nih.gov/37516813/)).

**Genetic risk factors.** The only established risk factor is inheriting two defective *LAT* alleles. **Consanguinity** is the dominant epidemiological risk factor (raises the probability of homozygosity for a rare recessive allele). Heterozygous carriers (including all reported parents) are asymptomatic.

**Environmental / protective factors.** As a monogenic Mendelian disorder, there are **no established environmental risk factors, protective factors, or gene–environment interactions** that initiate the disease. Environmental exposures (pathogens) act only as *triggers* that unmask the immunodeficiency (e.g., CMV, VZV, toxoplasma infections), not as causes. No protective modifier alleles have been reported. This section is largely **not applicable** beyond the genetic cause.

---

## Section 3 — Phenotypes

Phenotype data derive principally from the first kindred (Keller et al. 2016, three siblings, [PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)) supplemented by the SCID-presenting kindreds ([PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/); [PMID: 37516813](https://pubmed.ncbi.nlm.nih.gov/37516813/)).

> *"The three patients presented from early childhood with combined immunodeficiency and severe autoimmune disease"* — Keller et al. ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/))

| Phenotype | Type | HPO term | Onset / severity / frequency |
|---|---|---|---|
| Combined immunodeficiency / recurrent infections | Clinical sign | HP:0005387 (combined immunodeficiency) | Infantile (5–10 mo); severe; core feature in all |
| Autoimmune hemolytic anemia | Lab/clinical | HP:0004810 | Childhood; severe (fatal in one patient) |
| Immune thrombocytopenia | Lab/clinical | HP:0001973 | Childhood; severe |
| Generalized lymphadenopathy | Physical sign | HP:0002716 | Childhood; variable |
| Splenomegaly / hepatosplenomegaly | Physical sign | HP:0001744 / HP:0001433 | Childhood; massive in index patient |
| Bronchiectasis / chronic lung disease | Physical sign | HP:0002110 | Childhood; from recurrent respiratory infection |
| Opportunistic infection (CMV, VZV, toxoplasma) | Clinical sign | — | Infancy–childhood; life-threatening |
| Recurrent gastroenteritis / enteropathy | Symptom | HP:0004385-like | Childhood |
| Skin nodules / edematous purple-red lesions | Physical manifestation | HP:0011355 | Childhood; variable |
| T lymphocytopenia / reduced T cells | Lab abnormality | HP:0005403 | Congenital/progressive; universal |
| Eosinophilia | Lab abnormality | HP:0001880 | Childhood; from Th2 skewing |
| Elevated serum IgE (and high IgG1) | Lab abnormality | HP:0003212 | Childhood; from Th2 skewing |
| Hypogammaglobulinemia (may develop) | Lab abnormality | HP:0002720 | Variable/progressive |

**Onset:** neonatal-to-infantile (first months of life). **Severity:** severe. **Progression:** progressive combined immune deficiency with superimposed episodic autoimmune crises. **Quality of life / outcome:** profound — of the three index siblings, two died in childhood (one at age 9 from disseminated CMV following splenectomy; one at age 2 from AIHA plus thrombocytopenia) and one survived after HSCT at age 8.

> *"manifesting by a progressive combined immune deficiency with severe autoimmune disease"* — Keller et al. ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/))

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *LAT* — Linker for Activation of T cells. HGNC:6533; NCBI Gene 27040; OMIM gene *602354; UniProt O43561; chromosome **16p11.2**. LAT is a palmitoylated transmembrane adaptor localized to membrane rafts with a short extracellular domain and a long cytoplasmic tail bearing multiple tyrosines.

**Pathogenic variants (all germline, biallelic, loss-of-function):**

| Kindred | Variant | Type | Consequence |
|---|---|---|---|
| Keller 2016 ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)) | Homozygous nonsense in exon 5 | Nonsense | Premature stop codon deleting most of the cytoplasmic tail, including the critical signaling tyrosines |
| Bacchelli 2017 ([PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/)) | Novel homozygous frameshift | Frameshift | Premature stop, truncation → **complete loss of function and loss of expression** |
| Alizadeh 2023 ([PMID: 37516813](https://pubmed.ncbi.nlm.nih.gov/37516813/)) | Homozygous p.Y207fsTer33 | Frameshift | Truncated protein; SCID/leaky-SCID |

> *"we describe the first kindred with defective LAT signaling caused by a homozygous mutation in exon 5, leading to a premature stop codon deleting most of the cytoplasmic tail of LAT, including the critical tyrosine residues for signal propagation"* — [PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)

> *"a premature stop codon and protein truncation leading to complete loss of function and loss of expression of LAT"* — [PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/)

**Variant classification (ACMG/AMP):** truncating variants in a gene with an established loss-of-function disease mechanism, segregating with disease in consanguineous families → **pathogenic**. **Allele frequency:** the specific variants are private/ultra-rare (essentially absent from gnomAD). **Somatic vs germline:** germline. **Functional consequence:** loss of function (null); no gain-of-function or dominant-negative human alleles reported (note: the mouse *Lat*Y136F is a *separation-of-function* research allele, not a human disease variant).

**Modifier genes / epigenetics / chromosomal abnormalities:** none established for the human disease. No large-scale cytogenetic changes; this is a single-gene point/frameshift disorder.

---

## Section 5 — Environmental Information

Not applicable as a cause. There are **no environmental factors, lifestyle factors, or infectious agents that cause** LAT deficiency. Infectious agents (CMV, varicella-zoster virus, *Toxoplasma gondii*, common bacterial respiratory pathogens) are **downstream consequences** of the immunodeficiency and drive much of the morbidity and mortality, but they do not initiate the disease.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. A **biallelic truncating *LAT* variant** *results in* loss of LAT protein (or a tail-truncated protein lacking its cytoplasmic tyrosines) ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/), [PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/)).
2. Upon TCR engagement, Lck→ZAP-70 phosphorylation of LAT cannot occur, which *leads to* failure to assemble the **LAT signalosome** (PLCγ1, Grb2/SOS, GADS, SLP-76) at the plasma membrane ([PMID: 18231606](https://pubmed.ncbi.nlm.nih.gov/18231606/)).
3. Absent signalosome *abolishes* Ras–ERK/MAPK signaling **completely** and *impairs* PLCγ1-dependent Ca²⁺/NFAT signaling, while NF-κB signaling is **partially preserved** ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)).
4. Defective proximal TCR signal transduction *impairs* thymic positive selection and peripheral T-cell activation, *resulting in* **T-cell lymphopenia / absent T cells** with absent proliferative responses ([PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/)). This branches:
   - **Branch A (immunodeficiency):** reduced/absent functional T cells *lead to* combined immunodeficiency → recurrent bacterial, viral, and opportunistic infections (CMV, VZV, toxoplasma).
   - **Branch B (autoimmunity/dysregulation, inferred largely from mouse):** loss of LAT's **negative-regulatory / homeostatic** function *permits* TCR–MHC-independent, "quasi-mitogenic" expansion of Th2-skewed CD4⁺ T cells ([PMID: 18209052](https://pubmed.ncbi.nlm.nih.gov/18209052/); [PMID: 16887989](https://pubmed.ncbi.nlm.nih.gov/16887989/)), a process that is **IL-6-dependent** in its early phase ([PMID: 26034173](https://pubmed.ncbi.nlm.nih.gov/26034173/)).
5. Th2 hyperactivity *drives* polyclonal B-cell activation → IgG1/IgE hypergammaglobulinemia, eosinophilia, and autoantibodies *leading to* hematologic autoimmunity (AIHA, ITP), lymphoproliferation (lymphadenopathy, splenomegaly), and tissue immunopathology (immune-complex nephritis in mice).

> *"residual T cells were able to induce Ca(2+) influx and nuclear factor (NF) κB signaling, whereas extracellular signal-regulated kinase (ERK) signaling was completely abolished"* — [PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)

> *"LAT phosphorylation results in the recruitment of a signalosome including PLCgamma1, Grb2/SOS, GADS and SLP-76"* — [PMID: 18231606](https://pubmed.ncbi.nlm.nih.gov/18231606/)

### Signalosome schematic

```
      TCR engagement
           │
        Lck → ZAP-70
           │  (phosphorylates LAT tyrosines)
           ▼
   ┌─────────────────── LAT (membrane raft) ───────────────────┐
   │        │              │              │            │        │
 PLCγ1   Grb2/SOS        GADS          SLP-76        Itk/Vav1   │
   │        │                             │                     │
  Ca²⁺/    Ras→ERK/MAPK              (integrin activation:      │
  NFAT     (ABOLISHED)                Rap1/talin/actin)         │
 (impaired)                                                     │
   └──────── LOSS OF LAT → no signalosome → branches A & B ─────┘
```

**Molecular pathways:** TCR proximal signaling; Ras–MAPK/ERK (KEGG/Reactome "TCR signaling"); PLCγ1–Ca²⁺–NFAT; PI3K and NF-κB (partially preserved). **Cellular processes:** thymocyte development/positive selection, T-cell activation/proliferation, immune homeostasis (dysregulated), inflammation. **Protein dysfunction:** loss of function of the adaptor (no scaffold for signalosome assembly). **Immune involvement:** simultaneous **immunodeficiency** and **autoimmunity/immune dysregulation**. **Metabolic/biochemical:** the defect is a signaling/adaptor defect, not an enzymopathy.

LAT is expressed beyond T cells — in mast cells, NK cells, megakaryocytes, platelets, and early B cells — so non-T lineages may contribute, though human phenotypes there are not well documented.

> *"Although LAT is also expressed in mast cells, natural killer cells, megakaryocytes, platelets, and early B cells"* — [PMID: 16102570](https://pubmed.ncbi.nlm.nih.gov/16102570/)

> *"This unexpected finding revealed that LAT also constitutes a negative regulator of TCR signalling and T cell homeostasis"* — [PMID: 17534068](https://pubmed.ncbi.nlm.nih.gov/17534068/)

**Suggested GO terms:** GO:0050852 (T cell receptor signaling pathway), GO:0070374 (positive regulation of ERK cascade), GO:0002250 (adaptive immune response), GO:0045058 (T cell selection). **Cellular component:** GO:0005886 (plasma membrane), GO:0045121 (membrane raft). **CL terms:** CL:0000084 (T cell), CL:0000624 (CD4+ T cell), CL:0000097 (mast cell), CL:0000623 (NK cell).

---

## Section 7 — Anatomical Structures Affected

**Primary — immune/hematopoietic system** (UBERON:0002405):
- Thymus (UBERON:0002370) — impaired T-cell development
- Bone marrow (UBERON:0002371) — hematopoietic source; HSCT target
- Spleen (UBERON:0002106) — splenomegaly
- Lymph nodes (UBERON:0000029) — lymphadenopathy
- Peripheral blood (UBERON:0000178) — lymphopenia, cytopenias

**Secondary organ involvement:**
- Lung (UBERON:0002048) — bronchiectasis, recurrent pneumonia
- Liver (UBERON:0002107) — hepatomegaly
- Skin (UBERON:0002097) — inflammatory nodules
- Gastrointestinal tract (UBERON:0000160) — gastroenteritis/enteropathy
- Kidney (UBERON:0002113) — immune-complex nephritis (documented in mouse model)

**Cell level:** T lymphocytes (CL:0000084), especially CD4⁺ Th2 cells (CL:0000624); reactive B cells; mast cells/NK cells/platelets express LAT. **Subcellular:** plasma membrane (GO:0005886), membrane raft (GO:0045121). **Lateralization:** systemic/bilateral (not applicable as a focal lateralized disease).

---

## Section 8 — Temporal Development

**Onset:** congenital defect with clinical onset in the **first months of life** (5–10 months in the index kindred); insidious-to-subacute in the immunodeficiency arm, with episodic autoimmune crises. **Progression:** progressive combined immune deficiency; the autoimmune cytopenias are episodic/relapsing and can be acutely life-threatening. **Course/duration:** chronic and lifelong; without HSCT the natural history is high childhood mortality. **Remission:** treatment-induced remission via HSCT (curative); spontaneous remission does not occur. **Critical period:** the neonatal-to-infancy window — early (pre-symptomatic) diagnosis via newborn screening and prompt HSCT is the key opportunity for intervention.

---

## Section 9 — Inheritance and Population

**Epidemiology.** Ultra-rare: Orphanet lists prevalence **<1/1,000,000**. Fewer than ~20 patients have been reported worldwide (Keller 2016, Bacchelli 2017, Alizadeh 2023 kindreds). No reliable incidence figure exists; as a T-cell-lymphopenic SCID it falls within the aggregate SCID birth prevalence detected by newborn screening (e.g., ~1:46,753 in Catalonia [PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/); ~1:12,298 for severe T/B immunodeficiency in Russia [PMID: 41727503](https://pubmed.ncbi.nlm.nih.gov/41727503/)), but LAT accounts for a tiny fraction of these.

**Inheritance:** autosomal recessive. **Penetrance:** complete in biallelic individuals (carriers unaffected). **Expressivity:** variable — the phenotype ranges from CID-with-autoimmunity to frank T–B+NK+ SCID, even within a single sibship. **Anticipation / germline mosaicism / founder effect:** none established. **Consanguinity:** central — all reported families are consanguineous (homozygosity by descent). **Carrier frequency:** unknown but very low; carriers are healthy. **Sex ratio:** ~1:1. **Populations:** reported in consanguineous families (including Arab ancestry) with no established ethnic clustering or founder mutation.

> *"a severe combined immunodeficiency phenotype with absent T cells and normal B-cell and natural killer cell numbers"* — [PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/) (defines the T–B+NK+ classification underpinning ORPHA:504523)

---

## Section 10 — Diagnostics

**Clinical/laboratory tests.** Flow cytometry showing reduced/absent T cells with normal B and NK cell numbers (T–B+NK+ pattern); absent T-cell proliferative responses to mitogens/antigens; abnormal immunoglobulins (variably elevated IgG1/IgE with Th2 skewing, or hypogammaglobulinemia); eosinophilia; autoimmune cytopenias (AIHA, ITP) with positive autoantibodies. Functional signaling assays can show absent ERK phosphorylation and preserved Ca²⁺/NF-κB in residual T cells.

**Newborn screening.** As a cause of T-cell lymphopenia, LAT deficiency is detectable by **TREC (T-cell receptor excision circle) quantification on dried blood spots**, the standard population screen for SCID ([PMID: 42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/); [PMID: 41727503](https://pubmed.ncbi.nlm.nih.gov/41727503/); [PMID: 42496450](https://pubmed.ncbi.nlm.nih.gov/42496450/)).

**Genetic testing.** Definitive diagnosis is molecular. In reported kindreds this used **homozygosity mapping** followed by **Sanger / whole-exome sequencing** ([PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/); [PMID: 37516813](https://pubmed.ncbi.nlm.nih.gov/37516813/)). WES/WGS or SCID/CID gene panels including *LAT* are the recommended approach; single-gene *LAT* testing is appropriate for cascade testing once a familial variant is known.

> *"Homozygosity mapping was used to identify potential defective genes"* — [PMID: 27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/)

**Differential diagnosis.** Other T–B+NK+ SCID (IL7R, CD3D/CD3E/CD3G, PTPRC/CD45, CORO1A); ZAP-70 deficiency; CID with immune dysregulation (IPEX/FOXP3, CTLA4, LRBA, STAT3-GOF, Omenn syndrome); and ALPS for the autoimmune-cytopenia/lymphoproliferation picture.

---

## Section 11 — Outcome / Prognosis

**Natural history is severe.** Without HSCT, OMIM summarizes that most patients die in childhood. In the index kindred, two of three siblings died (ages 2 and 9); the survivor was transplanted. Mortality is driven by opportunistic/disseminated infection (e.g., CMV) and by acute autoimmune cytopenias.

**Prognosis improves markedly with early diagnosis and HSCT.** For SCID generally, early (newborn-screening/family-history) diagnosis substantially improves survival:

> *"The 2-year overall survival (OS) of the late group was 29.2%, in contrast to the 2-year OS of the early diagnosis group of 71.4%"* — [PMID: 40374985](https://pubmed.ncbi.nlm.nih.gov/40374985/)

**Morbidity:** chronic lung disease/bronchiectasis, autoimmune organ damage, growth/developmental impact from chronic illness, and transplant-related complications. **Prognostic factors:** age at diagnosis, presence of active infection at HSCT, and degree of immune dysregulation.

---

## Section 12 — Treatment

**Curative — allogeneic hematopoietic stem cell transplantation (HSCT)** (NCIT: Hematopoietic Cell Transplantation). HSCT is the only curative therapy and replaces the defective hematopoietic/T-lineage compartment.

> *"Hematopoietic cell transplantation (HCT) is the only curative treatment currently available"* — [PMID: 40374985](https://pubmed.ncbi.nlm.nih.gov/40374985/)

In the index kindred, the proband underwent successful HSCT at age 8 ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)).

**Supportive / bridging care (NCIT clinical interventions):**
- Immunoglobulin replacement therapy (IVIG/SCIG) — NCIT: Immunoglobulin Therapy
- Anti-infective prophylaxis — *Pneumocystis jirovecii* prophylaxis (co-trimoxazole), antivirals, antifungals ([PMID: 42496450](https://pubmed.ncbi.nlm.nih.gov/42496450/))
- Management of autoimmune cytopenias — corticosteroids/immunosuppression; splenectomy has been used but carries infection risk (one index patient died of disseminated CMV after splenectomy)
- Use of irradiated, CMV-safe/leukoreduced blood products; avoidance of live vaccines

**Advanced/experimental.** No approved gene therapy, gene editing, RNA-based, or targeted therapy exists specifically for LAT deficiency. Mechanistically, IL-6 blockade is a rational candidate for the autoimmune/lymphoproliferative arm given the mouse data ([PMID: 26034173](https://pubmed.ncbi.nlm.nih.gov/26034173/)), but this is unproven in humans. **Pharmacogenomics:** not applicable. **Personalized medicine:** genotype-confirmed diagnosis guides expedited HSCT.

---

## Section 13 — Prevention

**Primary prevention:** none possible (Mendelian). **Secondary prevention:** TREC **newborn screening** enables pre-symptomatic detection and early HSCT — the single most impactful preventive intervention; pre-transplant anti-infective prophylaxis (PJP, antivirals, antifungals) plus IVIG prevents infectious complications; avoidance of live vaccines and use of irradiated/CMV-safe blood products prevent iatrogenic harm. **Tertiary prevention:** aggressive infection control and management of autoimmune complications. **Genetic counseling:** autosomal recessive with 25% sibling recurrence risk; carrier testing of relatives, and prenatal or preimplantation genetic diagnosis in families with a known variant. **Public health/immunization/environmental measures:** not applicable beyond the above.

---

## Section 14 — Other Species / Natural Disease

**Taxonomy/orthologs:** mouse *Lat* (NCBI Gene 16797; MGI:1342293; *Mus musculus*, NCBI Taxon 10090) is the principal ortholog studied; human *LAT* is NCBI Gene 27040. **Natural disease:** **no naturally occurring LAT deficiency disease is documented in companion animals or wildlife** (OMIA has no *LAT* disease entry as of this review). **Comparative biology:** the TCR-signalosome role of LAT is evolutionarily conserved across mammals, which is why the mouse recapitulates key disease arms. **Zoonotic potential:** not applicable (non-infectious genetic disease).

---

## Section 15 — Model Organisms

The mouse has been the decisive model, and two complementary alleles map onto the two arms of human disease:

| Model | Allele | Phenotype | Human arm modeled |
|---|---|---|---|
| Complete *Lat*-null KO | Full loss | Thymocyte development arrested at CD4–CD8– double-negative (DN3) stage; **no peripheral T cells** | Immunodeficiency |
| *Lat*Y136F knock-in | Tyr136→Phe (PLCγ1 docking site) | Fast-onset polyclonal CD4⁺ **Th2 lymphoproliferation**, massive IL-4/IgG1/IgE, autoantibodies, nephritis, proteinuria | Autoimmunity / dysregulation |
| C-terminal 4-tyrosine knock-ins | Multi-Tyr mutants | Reveal LAT's **negative-regulatory** loss | Homeostatic dysregulation |

> *"Lat(Y136F) mice) develop a fast-onset lymphoproliferative disorder involving polyclonal CD4 T cells that produce massive amounts of Th2 cytokines and trigger severe inflammation and autoantibodies"* — [PMID: 18209052](https://pubmed.ncbi.nlm.nih.gov/18209052/)

> *"a defect intrinsic to Lat(Y136F) CD4 T cells leads to a state of TCR-independent hyperactivity"* — [PMID: 18209052](https://pubmed.ncbi.nlm.nih.gov/18209052/)

> *"we observed early-onset systemic autoimmunity with nephritis showing IgE autoantibody deposits and severe proteinuria"* — [PMID: 16887989](https://pubmed.ncbi.nlm.nih.gov/16887989/)

> *"IL-6 is required for uncontrolled T cell expansion during the early stage of disease development"* — [PMID: 26034173](https://pubmed.ncbi.nlm.nih.gov/26034173/)

**Phenotype recapitulation / limitations.** No single mouse fully matches the human phenotype: the null models the immunodeficiency arm, Y136F models the autoimmunity arm, but human patients present with a **combined, intermediate** picture (reduced/residual T cells *plus* autoimmunity) not captured by either allele alone ([PMID: 27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/)). Notably, mice show lymphoproliferation whereas human patients show reduced T-cell numbers. **Resources:** MGI (mouse). No zebrafish/Drosophila/organoid model is established for this disease.

---

## Mechanistic Model / Interpretation

The unifying insight is that **LAT is a signaling hub with dual, opposing roles**, and losing it simultaneously produces *too little* useful T-cell signaling (immunodeficiency) and *too little restraint* on aberrant T-cell activation (autoimmunity):

```
                 biallelic truncating LAT (null)
                          │
              ┌───────────┴───────────┐
   POSITIVE role lost         NEGATIVE role lost
   (signalosome absent)       (homeostatic brake gone)
        │                             │
  ERK abolished,               TCR-MHC-independent
  Ca²⁺/NFAT impaired            "quasi-mitogenic" Th2
        │                       expansion (IL-6-dependent)
  impaired thymic                    │
  selection / activation      polyclonal B activation,
        │                     IgG1/IgE, autoantibodies,
  T-lymphopenia,               eosinophilia
  absent proliferation               │
        │                     AIHA, ITP, lymphadenopathy,
  recurrent & opportunistic    splenomegaly, nephritis(mouse)
  infections (CMV/VZV/toxo)
        │                             │
        └────────► COMBINED IMMUNODEFICIENCY ◄────────┘
                    + SEVERE AUTOIMMUNITY
```

This resolves the apparent paradox of a SCID-causing gene that also drives autoimmunity, and it explains the variable expressivity: the balance between residual T-cell output (branch A severity) and unrestrained Th2 activity (branch B severity) shifts along the spectrum from "CID + autoimmunity" to "frank T–B+NK+ SCID." Therapeutically, only replacing the entire compartment (HSCT) addresses both arms, which is why it is the sole curative option.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [27242165](https://pubmed.ncbi.nlm.nih.gov/27242165/) | *Early onset combined immunodeficiency and autoimmunity in patients with LOF mutation in LAT* | **Landmark:** first human kindred; defines phenotype, ERK-abolished signaling defect, exon-5 nonsense variant, HSCT outcome |
| [27522155](https://pubmed.ncbi.nlm.nih.gov/27522155/) | *Mutations in LAT lead to a novel form of SCID* | Second kindred; defines T–B+NK+ SCID; frameshift → complete LOF/loss of expression; homozygosity mapping |
| [37516813](https://pubmed.ncbi.nlm.nih.gov/37516813/) | *8 patients with typical/atypical SCID; 7 novel mutations by WES* | Third report; p.Y207fsTer33; confirms recurrent SCID-causing entity, WES diagnosis |
| [18231606](https://pubmed.ncbi.nlm.nih.gov/18231606/) | *ZAP-70-dependent FRET biosensor* | Defines LAT signalosome composition (PLCγ1, Grb2/SOS, GADS, SLP-76) |
| [18209052](https://pubmed.ncbi.nlm.nih.gov/18209052/) | *Th2 lymphoproliferative disorder of LatY136F mice* | Autoimmunity-arm mechanism; T-cell-intrinsic, TCR-independent hyperactivity |
| [16887989](https://pubmed.ncbi.nlm.nih.gov/16887989/) | *LatY136F triggers polyclonal B activation and systemic autoimmunity* | Documents nephritis, IgE autoantibodies, systemic autoimmunity in model |
| [26034173](https://pubmed.ncbi.nlm.nih.gov/26034173/) | *Importance of IL-6 in LAT-mediated autoimmunity* | Identifies IL-6 as driver of early lymphoproliferation |
| [17534068](https://pubmed.ncbi.nlm.nih.gov/17534068/) | *Th2 lymphoproliferation from defective LAT signalosomes* | Establishes LAT's negative-regulatory role |
| [16102570](https://pubmed.ncbi.nlm.nih.gov/16102570/) | *Role of LAT in T-cell development and Th2 differentiation* | Multi-lineage LAT expression; null → thymic block |
| [40374985](https://pubmed.ncbi.nlm.nih.gov/40374985/) | *Newborn screening improves survival in SCID* | Quantifies early- vs late-diagnosis survival; HSCT curative |
| [42079620](https://pubmed.ncbi.nlm.nih.gov/42079620/) / [41727503](https://pubmed.ncbi.nlm.nih.gov/41727503/) / [42496450](https://pubmed.ncbi.nlm.nih.gov/42496450/) | SCID newborn-screening programs | TREC/KREC screening context and diagnostic workflow |

**Evidence quality.** The human disease rests on **case reports of ≤3 independent consanguineous kindreds** (low n but concordant and mechanistically coherent). Mechanism is strongly supported by **mouse genetics** and **in vitro signaling** studies. Prognosis/screening/treatment claims are extrapolated from the broader **SCID** literature, which is robust.

---

## Limitations and Knowledge Gaps

- **Very small human N (<20 patients).** Prevalence, penetrance nuances, full phenotypic range, and genotype–phenotype correlations are provisional.
- **No LAT-specific outcome data.** Survival/HSCT-outcome figures are borrowed from general SCID cohorts, not LAT-specific series.
- **Branch B (autoimmunity) mechanism is inferred from mouse.** The IL-6 dependence and "quasi-mitogenic" Th2 model are demonstrated in *Lat*Y136F mice; direct human confirmation is limited.
- **Model mismatch.** No single mouse reproduces the combined human phenotype (humans have reduced T cells; Y136F mice have lymphoproliferation).
- **No human variant catalog beyond truncating alleles.** Missense/hypomorphic human alleles and their consequences are unknown; no VUS spectrum defined.
- **Non-T lineage contribution (mast cells, NK, platelets, early B cells) is uncharacterized in patients.**
- **No naturally occurring animal disease** documented (OMIA gap).

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international LAT-deficiency registry** to pool the scattered kindreds and capture natural history, HSCT outcomes, and genotype–phenotype data.
2. **Deep immunophenotyping of patients** (single-cell RNA-seq / CITE-seq of residual T cells) to test whether the human Th2-skewing/negative-regulation mechanism mirrors the mouse and to define which cell states drive autoimmunity.
3. **Test IL-6 pathway blockade** (e.g., tocilizumab) as a bridge-to-transplant for the autoimmune/lymphoproliferative arm, given the mouse IL-6 dependence ([PMID: 26034173](https://pubmed.ncbi.nlm.nih.gov/26034173/)).
4. **Assess non-T lineage function** (platelet GPVI signaling, mast cell, NK activity) in patients, since LAT is expressed in these lineages.
5. **Generate a humanized or hypomorphic-allele mouse / patient iPSC-derived thymic organoid** that recapitulates the combined (reduced-T-cell + autoimmunity) human phenotype for preclinical testing.
6. **Explore gene-corrected autologous HSC therapy** (lentiviral *LAT* or base/prime editing) as a future alternative to allogeneic HSCT, mindful that LAT expression must be tightly regulated to avoid recreating dysregulation.
7. **Ensure *LAT* is included in confirmatory SCID gene panels** downstream of TREC-positive newborn screens so that these patients are captured early.

---

*Report compiled from 10 confirmed findings and 22 reviewed papers over 5 investigation iterations. Evidence types: human clinical case reports (Keller 2016, Bacchelli 2017, Alizadeh 2023); mouse model organism studies (LatY136F, Lat-null); in vitro signaling studies; and SCID newborn-screening epidemiology.*


## Artifacts

- [OpenScientist final report](LAT_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](LAT_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 32 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0044721` (2 mentions) - the report calls it "MONDO"; MONDO calls it **severe combined immunodeficiency due to LAT deficiency**
- `HP:0004810` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Congenital hypoplastic anemia**
- `HP:0001973` (1 mention) - the report calls it "Lab/clinical"; HP calls it **Autoimmune thrombocytopenia**
- `HP:0002716` (1 mention) - the report calls it "Physical sign"; HP calls it **Lymphadenopathy**
- `HP:0002110` (1 mention) - the report calls it "Physical sign"; HP calls it **Bronchiectasis**
- `HP:0011355` (1 mention) - the report calls it "Physical manifestation"; HP calls it **Localized skin lesion**
- `HP:0005403` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased total T cell count**
- `HP:0001880` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased total eosinophil count**
- `HP:0003212` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Increased circulating IgE concentration**
- `HP:0002720` (1 mention) - the report calls it "Lab abnormality"; HP calls it **Decreased circulating IgA concentration**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0070374` (1 mention) - the report calls it "positive regulation of ERK cascade"; GO calls it **positive regulation of ERK1 and ERK2 cascade**, and lists "positive regulation of ERK cascade" among its other names
- `CL:0000624` (2 mentions) - the report calls it "CD4+ T cell"; CL calls it **CD4-positive, alpha-beta T cell**
- `CL:0000623` (1 mention) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names
- `UBERON:0002405` (1 mention) - the report calls it "Primary — immune/hematopoietic system"; UBERON calls it **immune system**
- `UBERON:0000178` (1 mention) - the report calls it "Peripheral blood"; UBERON calls it **blood**, and lists "vertebrate blood" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0000160` (1 mention) - the report calls it "Gastrointestinal tract"; UBERON calls it **intestine**, and lists "intestinal tract" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.