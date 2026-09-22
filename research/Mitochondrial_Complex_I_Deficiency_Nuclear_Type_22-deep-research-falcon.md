---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T13:54:32.688544'
end_time: '2026-09-04T14:05:27.196311'
duration_seconds: 654.51
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: "Mitochondrial complex I deficiency nuclear type 22, MC1DN22, OMIM\
    \ 618243 \u2014 an autosomal recessive nuclear-gene mitochondrial disease caused\
    \ by biallelic loss-of-function variants in NDUFA10, which encodes the NADH:ubiquinone\
    \ oxidoreductase subunit A10 accessory subunit of respiratory chain complex I.\
    \ This is complex I, NOT complex IV."
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 42
  verified: 41
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 19
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0008872
    reported_labels:
    - feeding/developmental milestone context as applicable
    ontology_label: Feeding difficulties in infancy
  - term_id: HP:0001629
    reported_labels:
    - ventricular hypertrophy/cardiomyopathy mapping should be phenotype-specific
    ontology_label: Ventricular septal defect
  - term_id: HP:0001272
    reported_labels:
    - cerebellar/brainstem-related imaging mapping only where supported
    ontology_label: Cerebellar atrophy
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_22-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial complex I deficiency nuclear type 22, MC1DN22, OMIM 618243 — an autosomal recessive nuclear-gene mitochondrial disease caused by biallelic loss-of-function variants in NDUFA10, which encodes the NADH:ubiquinone oxidoreductase subunit A10 accessory subunit of respiratory chain complex I. This is complex I, NOT complex IV.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex I deficiency nuclear type 22, MC1DN22, OMIM 618243 — an autosomal recessive nuclear-gene mitochondrial disease caused by biallelic loss-of-function variants in NDUFA10, which encodes the NADH:ubiquinone oxidoreductase subunit A10 accessory subunit of respiratory chain complex I. This is complex I, NOT complex IV.** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial complex I deficiency nuclear type 22, MC1DN22, OMIM 618243 — an autosomal recessive nuclear-gene mitochondrial disease caused by biallelic loss-of-function variants in NDUFA10, which encodes the NADH:ubiquinone oxidoreductase subunit A10 accessory subunit of respiratory chain complex I. This is complex I, NOT complex IV.
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial complex I deficiency nuclear type 22, MC1DN22, OMIM 618243 — an autosomal recessive nuclear-gene mitochondrial disease caused by biallelic loss-of-function variants in NDUFA10, which encodes the NADH:ubiquinone oxidoreductase subunit A10 accessory subunit of respiratory chain complex I. This is complex I, NOT complex IV.** covering all of the
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


# Mitochondrial complex I deficiency, nuclear type 22 (MC1DN22)

## Executive summary and evidence scope

MC1DN22 is an **ultra-rare autosomal-recessive nuclear mitochondrial disease caused by biallelic pathogenic variants in `NDUFA10`**. NDUFA10 is an accessory subunit of mitochondrial respiratory-chain **complex I (NADH:ubiquinone oxidoreductase)**. This entity must not be confused with NDUFA4-associated complex IV deficiency or NDUFB10-associated complex I deficiency. The directly retrievable human evidence consists principally of two deeply phenotyped boys reported in 2011 and 2017; consequently, phenotype percentages, penetrance, prevalence, survival curves, and treatment-response rates cannot be estimated reliably. The available phenotype is a Leigh-syndrome-spectrum encephalomyopathy with lactic acidosis, developmental impairment or regression, movement/oculomotor abnormalities, characteristic but variable deep-gray-matter lesions, and severe complex I dysfunction. (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7)

Recent 2023–2024 literature has refined the general structural biology and modeling of complex-I/Leigh disease, but the search did **not** identify a new 2023–2024 NDUFA10-specific clinical cohort. A 2024 review reports that Leigh syndrome commonly begins near 7 months, has median death around 2.4 years, and has an overall incidence near 1 per 40,000 births; these are **Leigh-spectrum figures, not MC1DN22-specific epidemiology**. The same review states that no disease-modifying treatment is clinically approved. (henke2024diseasemodelsof pages 1-2)

| Citation/date | Genotype and segregation | Onset/trigger | Core phenotype | Biochemical findings | MRI/pathology | Course/outcome | Evidence limitations |
|---|---|---|---|---|---|---|---|
| Hoefs et al., *European Journal of Human Genetics*; online 8 Dec 2010, issue Mar 2011; DOI: [10.1038/ejhg.2010.204](https://doi.org/10.1038/ejhg.2010.204) (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 2-3) | Compound heterozygous **NDUFA10** c.1A>G (start-loss; p.Met1?) and c.425A>G (p.Gln142Arg); paternal and maternal, respectively. Both absent from 108 controls and 21 other isolated-complex-I-deficiency patients (hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 2-3) | Male born at 32 weeks after fetal distress; hypotonia evident in early infancy (hoefs2011ndufa10mutationscause pages 1-2) | Poor head control, inability to sit, developmental delay, mildly increased tendon reflexes, abnormal breathing, possible seizure, and hypertrophic cardiomyopathy (hoefs2011ndufa10mutationscause pages 2-3, hoefs2011ndufa10mutationscause pages 1-2) | At 10 months, blood lactate 8.6 mmol/L and CSF lactate 4.9 mmol/L. Complex I activity: fibroblasts 30 mU/U citrate synthase (control 104–206; 29% of lower limit) and muscle 5 mU/mU citrate synthase (control 70–250; 7% of lower limit). Muscle complex III mildly reduced to 68%; complex IV within the displayed reference range. Fibroblasts had reduced NDUFA10/NDUFA9, reduced holo-complex I, and accumulated assembly subcomplexes (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 2-3) | Symmetric basal-ganglia and substantia-nigra lesions. Autopsy showed multiorgan abnormalities, with prominent thalamic and pontine neuropathology supporting classic Leigh syndrome (hoefs2011ndufa10mutationscause pages 2-3) | Progressive disease culminating in fatal cardiorespiratory arrest at 23 months (hoefs2011ndufa10mutationscause pages 2-3) | Single-patient report; no formal prevalence, penetrance, treatment-response, or genotype–phenotype estimates. No reported rescue/complementation experiment in the retrieved evidence; pathogenicity rests on segregation, rarity, conservation/prediction, severe biochemical deficiency, and assembly/protein abnormalities (hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 2-3) |
| Minoia et al., *JIMD Reports*; online 1 Mar 2017; DOI: [10.1007/8904_2017_9](https://doi.org/10.1007/8904_2017_9) (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2) | Homozygous **NDUFA10** c.296G>A (p.Gly99Glu; reported as p.G99E); both parents heterozygous. Parents were third-degree cousins (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2) | Male with nystagmus from 1 month and mild developmental delay; acute deterioration at 2 years 8 months following fever, with later febrile relapses (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2) | Severe weakness/hyposthenia, loss of standing and walking, generalized hypotonia, lower-limb muscle hypotrophy, mildly increased reflexes, gait ataxia, clumsiness, oscillatory nystagmus/oculomotor dysfunction, dystonia, impaired language, and moderate developmental delay (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2) | Plasma lactate 39.2 mg/dL (reference 8–22). Muscle respiratory-chain testing showed clear complex I reduction with milder combined I+III and II+III reductions; histology showed slight cytochrome-*c*-oxidase reduction (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7) | Initial MRI/MRS: bilateral putamen/globus-pallidus disease, asymmetric caudate and left cerebral-peduncle involvement, necrosis, cytotoxic/vasogenic edema, restricted diffusion, and lactate peak. Follow-up showed new caudate, basal nuclei of Meynert, and right-peduncle lesions plus chronic putaminal atrophy and persistent elevated lactate (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7) | Thiamine–biotin treatment produced partial neurologic improvement, but neurological deterioration and fever-associated relapses continued; final survival status was not available in the retrieved evidence (minoia2017wideningtheheterogeneity pages 1-2) | Single-patient report with atypical, evolving MRI findings; no controlled treatment evidence or long-term quantitative outcome. The literature describes very few deeply characterized NDUFA10 cases. Variants summarized secondarily in Dang et al. 2020 should not be counted as independent, fully phenotyped MC1DN22 patients without confirmation from their primary reports (minoia2017wideningtheheterogeneity pages 5-7, dang2020analysisofhuman pages 28-30) |


*Table: Patient-level evidence from the two retrieved, deeply characterized reports of NDUFA10-related mitochondrial complex I deficiency. The table emphasizes the extremely limited case base and separates directly documented findings from evidence gaps.*

## 1. Disease information

### Definition and identifiers

* **Preferred disease name:** mitochondrial complex I deficiency, nuclear type 22.
* **Symbol/synonyms:** MC1DN22; NDUFA10-related mitochondrial disease; NDUFA10-related complex I deficiency; NDUFA10-related Leigh syndrome; Leigh syndrome due to NDUFA10 deficiency.
* **OMIM:** **618243** (specified disease record). The causal gene is `NDUFA10`.
* **MONDO:** a disease-specific MONDO identifier was not verified in the retrieved evidence; a knowledge-base record should not infer one from a generic Leigh-syndrome or complex-I-deficiency term.
* **Orphanet:** no MC1DN22-specific Orphanet identifier was verified. Broader Leigh syndrome/mitochondrial respiratory-chain deficiency categories may apply.
* **ICD-10/ICD-11 and MeSH:** no unique MC1DN22 code was found. Coding generally falls under mitochondrial metabolism/mitochondrial disease or Leigh disease; local coding systems should retain `NDUFA10` and OMIM 618243 as molecular qualifiers.
* **Category:** Mendelian, nuclear-gene, autosomal recessive, primary mitochondrial oxidative-phosphorylation disorder.

The foundational publication described “NDUFA10 mutations [that] cause complex I deficiency in a patient with Leigh disease.” It documented an accessory-subunit defect with deficient complex-I quantity, activity, and assembly—not complex IV disease. DOI: [10.1038/ejhg.2010.204](https://doi.org/10.1038/ejhg.2010.204), published online 8 December 2010 and in the March 2011 issue. (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 3-4)

### Data provenance

The disease definition is aggregated from OMIM-level nomenclature and peer-reviewed literature, but most detailed clinical information is **individual-patient case-report data**, not EHR-derived population data. The 2011 and 2017 papers are human clinical reports supplemented by biochemical, imaging, and cellular evidence. No registry-scale NDUFA10 cohort was retrieved. (hoefs2011ndufa10mutationscause pages 1-2, minoia2017wideningtheheterogeneity pages 2-5)

## 2. Etiology

### Causal factors and genetic risk

The necessary initiating factor is biallelic germline dysfunction of `NDUFA10`. Directly documented genotypes include:

1. Compound heterozygous **c.1A>G** (start-loss, reported as p.Met1?) and **c.425A>G (p.Gln142Arg)**, inherited from the father and mother, respectively. Both were absent from 108 controls and 21 additional patients with isolated complex-I deficiency; p.Gln142Arg affects a conserved residue and had a reported SIFT score of 0.00. (hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 2-3)
2. Homozygous **c.296G>A (p.Gly99Glu; p.G99E)** in a child of third-degree-cousin parents; both parents were heterozygous. (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)
3. A secondary 2020 tabulation lists **c.891T>C (p.Leu294Pro)** with **c.383_384insTAA (reported p.Ser218delinsIS)** in association with Leigh syndrome. Because the retrieved source did not provide a fully characterized independent patient or NDUFA10-specific assembly testing, these should be traced to their primary report before curation as separate confirmed cases. (dang2020analysisofhuman pages 28-30)

The variants are germline. No somatic etiology, susceptibility locus, modifier gene, founder allele, or protective allele has been established for MC1DN22. Variant classification should be performed against the current ClinVar submission and transcript version; the historical papers predate or do not provide a modern ACMG/AMP evidence table. Population allele frequencies were not available in the retrieved evidence and should be checked directly in current gnomAD rather than inferred from historical control absence.

### Environmental, protective, and gene–environment factors

No toxin, infection, diet, lifestyle, sex, or occupational exposure causes MC1DN22. Fever preceded acute deterioration in the 2017 child and recurrent febrile illnesses accompanied later relapses, consistent with metabolic stress unmasking limited respiratory reserve. This is a **trigger/modifier of decompensation**, not the genetic cause. (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)

No validated environmental or genetic protective factor is known. Experimental complex-I literature should not be converted into clinical advice: hypoxia-associated rescue in model systems and PINK1/NDUFA10 interactions remain mechanistic leads, not proven MC1DN22 prevention or treatment.

## 3. Phenotypes

Given only two deeply characterized patients, frequencies below are “reported in one or both cases,” not population estimates.

* **Developmental delay/regression:** early hypotonia, poor head control, inability to sit, delayed milestones, impaired language, loss of standing/walking, and moderate developmental delay. Suggested terms: HP:0001263 (global developmental delay), HP:0002376 (developmental regression), HP:0001252 (hypotonia), HP:0008872 (feeding/developmental milestone context as applicable). Severe and progressive or episodically worsening. (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5)
* **Motor and movement disorder:** weakness/hyposthenia, lower-limb muscle hypotrophy, gait ataxia, clumsiness, dystonia, and mildly brisk reflexes. Suggested terms: HP:0001324 (muscle weakness), HP:0001251 (ataxia), HP:0001332 (dystonia), HP:0001347 (hyperreflexia), HP:0008947 (infantile muscular hypotonia). (hoefs2011ndufa10mutationscause pages 1-2, minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)
* **Ocular motor manifestations:** nystagmus from one month in the second child and severe oculomotor dysfunction later. Suggested terms: HP:0000639 (nystagmus), HP:0000496 (abnormality of eye movement). (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)
* **Seizure/episodic neurologic event:** a possible convulsion was reported in the first child. Suggested term: HP:0001250 (seizure), but annotate as uncertain. (hoefs2011ndufa10mutationscause pages 2-3)
* **Respiratory and cardiac disease:** abnormal breathing and hypertrophic cardiomyopathy occurred in the first child, culminating in cardiorespiratory arrest. Suggested terms: HP:0001629 (ventricular hypertrophy/cardiomyopathy mapping should be phenotype-specific), HP:0001639 (hypertrophic cardiomyopathy), HP:0002793 (abnormal respiratory pattern). (hoefs2011ndufa10mutationscause pages 2-3)
* **Lactic acidosis/hyperlactatemia:** blood lactate 8.6 mmol/L and CSF lactate 4.9 mmol/L in the first patient; plasma lactate 39.2 mg/dL (reference 8–22) in the second. Suggested terms: HP:0003128 (lactic acidosis), HP:0011968 (elevated circulating lactate), HP:0500142 where available for elevated CSF lactate. (hoefs2011ndufa10mutationscause pages 1-2, minoia2017wideningtheheterogeneity pages 2-5)
* **Neuroimaging:** bilateral putamen/globus-pallidus, caudate, substantia-nigra, thalamic, pontine, basal-nucleus-of-Meynert, and cerebral-peduncle involvement; lesions may be symmetric or asymmetric, evolve asynchronously, show necrosis, restricted diffusion, cytotoxic/vasogenic edema, and later atrophy. Suggested terms: HP:0002135 (basal ganglia abnormality), HP:0002180 (neurodegeneration), HP:0002500 (abnormal cerebral white/gray matter imaging; use more specific HPO terms when available), HP:0001272 (cerebellar/brainstem-related imaging mapping only where supported). (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7)
* **Muscle/pathology:** muscle complex-I deficiency and slight cytochrome-c-oxidase histochemical reduction in the second patient; multiorgan autopsy abnormalities with prominent thalamic and pontine pathology in the first. (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5)

No validated EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life scores exist for MC1DN22. Nevertheless, loss of ambulation, developmental disability, recurrent decompensation, cardiopulmonary involvement, and early death imply profound effects on daily function and caregiver burden.

## 4. Genetic and molecular information

`NDUFA10` encodes a nuclear-encoded, mitochondrially imported accessory complex-I subunit. The original report described a predicted 355-amino-acid protein, reduced NDUFA10 and NDUFA9 abundance in patient fibroblasts, diminished assembled holo-complex I, and accumulation of assembly subcomplexes 4 and 5. These findings indicate defective assembly/stability rather than a primary complex-IV lesion. (hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 1-2)

The c.1A>G allele is expected to disrupt translation initiation and therefore cause severe loss of protein production; missense alleles p.Gln142Arg and p.Gly99Glu are expected to impair folding, interaction, stability, or assembly. Patient-specific rescue/complementation was not documented in the retrieved evidence, so “biallelic loss of function” should encompass absent/reduced protein and functional loss rather than imply that every allele is a truncating null. (hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5)

No reproducible modifier gene, epigenetic signature, pathogenic methylation event, chromosomal rearrangement, aneuploidy, or recurrent structural variant has been established. CMA, karyotype, and FISH are therefore not primary assays unless the phenotype suggests an independent chromosomal disorder.

## 5. Environmental information

Environmental exposure is not etiologic. Intercurrent fever/illness can increase ATP demand and catabolic stress, precipitating neurologic deterioration in a genetically energy-limited child. No evidence supports smoking, alcohol, pollution, radiation, occupational exposure, or a specific infectious agent as a causal factor. Routine immunization is not a disease-specific cure but prevention and prompt treatment of infection are rational components of tertiary risk reduction.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic germline `NDUFA10` variants lead to** absent, unstable, or dysfunctional NDUFA10 protein.
2. **NDUFA10 dysfunction leads to** impaired late complex-I assembly/stability, reduced holo-complex I, and accumulation of subassemblies; this was demonstrated in patient fibroblasts. (hoefs2011ndufa10mutationscause pages 3-4)
3. **Reduced holo-complex I leads to** markedly diminished NADH:ubiquinone oxidoreductase activity in fibroblasts and muscle. (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 2-3)
4. **Complex-I catalytic deficiency leads to** impaired NADH oxidation, electron transfer to ubiquinone, and proton translocation across the inner mitochondrial membrane; this biochemical step is established complex-I biology but was not measured in every MC1DN22 tissue.
5. **Impaired electron transport results in** reduced proton-motive force/oxidative ATP production and disturbed NAD+/NADH redox balance; these consequences are strongly inferred from complex-I deficiency rather than directly quantified in the two patients.
6. **Redox and ATP failure leads to** greater glycolytic reliance and lactate accumulation, demonstrated clinically by blood/CSF hyperlactatemia. (hoefs2011ndufa10mutationscause pages 1-2, minoia2017wideningtheheterogeneity pages 2-5)
7. **Energy failure, with likely oxidative and excitotoxic stress, results in** selective dysfunction and injury of high-demand neurons, skeletal muscle, respiratory-control circuits, and myocardium. ROS, apoptosis, inflammation, and excitotoxicity remain plausible downstream branches but were not directly profiled in MC1DN22 patients.
8. **Tissue injury leads to** developmental delay/regression, hypotonia, weakness, ataxia/dystonia, oculomotor abnormalities, basal-ganglia/brainstem necrotizing lesions, cardiomyopathy, respiratory failure, and potentially early death. (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7)
9. **Intercurrent fever increases energetic demand and leads to** episodic decompensation when residual respiratory reserve is inadequate; demonstrated temporally in the 2017 patient, although the exact molecular threshold is inferred. (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)

### Pathways, cells, and ontology suggestions

Relevant pathways are mitochondrial oxidative phosphorylation, respiratory electron transport, complex-I assembly, NADH oxidation, ubiquinone reduction, proton transmembrane transport, and ATP synthesis. Suggested GO terms include GO:0006120 (mitochondrial electron transport, NADH to ubiquinone), GO:0006119 (oxidative phosphorylation), GO:0032981 (mitochondrial respiratory-chain complex-I assembly), GO:0042775 (mitochondrial ATP synthesis coupled electron transport), GO:0015986 (proton-motive-force-driven ATP synthesis), and GO:0005747 (mitochondrial respiratory-chain complex I). Cellular-component annotations include mitochondrion GO:0005739, mitochondrial inner membrane GO:0005743, and mitochondrial matrix-facing complex-I domain.

Likely vulnerable cell types include neurons (CL:0000540), especially projection neurons and brainstem respiratory-control neurons; skeletal myocytes (CL:0000188); and cardiomyocytes (CL:0000746). Cell-type selectivity is inferred from clinical anatomy, not demonstrated by MC1DN22 single-cell analysis.

NDUFA10 also has a deoxyribonucleoside-kinase-like domain and has been linked experimentally to complex-I-associated mitochondrial dGTP binding. That function may connect oxidative metabolism to mitochondrial nucleotide availability, but no patient study has shown that dGTP dysregulation contributes materially to MC1DN22. Likewise, PINK1-dependent phosphorylation of NDUFA10 has been proposed, but Drosophila rescue did not specifically require the tested ND42 Ser-250 phosphorylation site. These findings should remain secondary mechanistic annotations, not the core proven disease mechanism. (pogson2014thecomplexi pages 2-4, pogson2014thecomplexi pages 1-2)

No MC1DN22-specific transcriptomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omic disease signature was retrieved. Modern mitochondrial diagnostics increasingly use transcriptomics, proteomics, and metabolomics when DNA findings are inconclusive, but that is a platform-level development rather than a validated NDUFA10 biomarker. (alston2021thegeneticsof pages 1-2)

## 7. Anatomical structures affected

The primary system is the **central nervous system**, especially deep gray nuclei and brainstem: putamen, globus pallidus, caudate nuclei, substantia nigra, thalamus, pons, basal nuclei of Meynert, and cerebral peduncles. Suggested UBERON terms include brain UBERON:0000955, basal ganglion UBERON:0002420, putamen UBERON:0001874, globus pallidus UBERON:0001876, caudate nucleus UBERON:0001873, substantia nigra UBERON:0002038, thalamus UBERON:0001897, pons UBERON:0000988, and cerebral peduncle UBERON:0001904. Lesions may be bilateral and symmetric, but asymmetric and asynchronous lesions are documented, so strict symmetry is not required. (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7)

Skeletal muscle and heart are additional high-demand organs; hypertrophic cardiomyopathy occurred in one patient. Respiratory involvement may reflect central respiratory-control injury, neuromuscular weakness, cardiac disease, or a combination. At the subcellular level, the key compartment is the mitochondrial inner membrane and its matrix-facing complex-I arm.

## 8. Temporal development

Onset ranged from early infancy—hypotonia or nystagmus—to a major fever-associated decline at 2 years 8 months. The course can therefore be congenital/infantile and insidiously developmental, followed by acute or subacute metabolic decompensation and progressive or relapsing neurologic loss. One child died at 23 months; the second had partial improvement after vitamin therapy but continued progressive deterioration and febrile relapses. No standardized MC1DN22 staging system, remission rate, or longitudinal natural-history cohort exists. (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)

Critical vulnerability periods include infancy/early childhood, rapid neurodevelopment, intercurrent illness, fasting/catabolism, anesthesia, and other periods of increased metabolic demand. Only illness-associated worsening is directly documented for NDUFA10 disease; the remaining periods derive from broader mitochondrial practice.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two carrier parents, the expected risk per pregnancy is 25% affected, 50% carrier, and 25% unaffected/non-carrier. Both documented pedigrees showed parental segregation; consanguinity was present in the homozygous case but is not necessary, as shown by compound heterozygosity in the first family. (hoefs2011ndufa10mutationscause pages 3-4, minoia2017wideningtheheterogeneity pages 1-2)

Penetrance among individuals with two truly pathogenic alleles appears high but cannot be quantified. Expressivity is variable: onset, MRI distribution, episodic versus progressive course, cardiomyopathy, and survival differed between the reported patients. No anticipation is expected for a conventional autosomal-recessive sequence-variant disorder. Germline mosaicism is theoretically possible but unreported. No founder effect, carrier frequency, ethnic enrichment, geographic concentration, sex ratio, prevalence, or incidence has been established. Both deeply described patients were male, but two cases cannot support sex bias.

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** developmental delay/regression, hypotonia, ataxia/dystonia, oculomotor dysfunction, episodic deterioration, lactic acidosis, cardiomyopathy, or Leigh-pattern MRI.
2. **Biochemistry:** blood lactate and pyruvate, blood gas, glucose, comprehensive metabolic studies, plasma amino acids, acylcarnitines, and urine organic acids. CSF lactate may be informative when lumbar puncture is otherwise clinically justified. Normal lactate does not exclude mitochondrial disease.
3. **Imaging:** brain MRI with T1/T2/FLAIR and diffusion sequences; MR spectroscopy may detect a lactate peak. Asymmetric lesions do not exclude Leigh syndrome. (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 5-7)
4. **Cardiac/functional evaluation:** ECG and echocardiography because hypertrophic cardiomyopathy was reported; neurologic, ophthalmologic, feeding, respiratory, hearing, and rehabilitation assessments should be phenotype-directed. (hoefs2011ndufa10mutationscause pages 2-3)
5. **Genetic testing:** trio WES or WGS, or a comprehensive nuclear-plus-mtDNA mitochondrial/Leigh panel containing `NDUFA10`. Exome/WGS from blood has increasingly replaced first-line invasive biopsy; unresolved cases may need genome sequencing, RNA sequencing, proteomics, or assays in clinically relevant tissue. (alston2021thegeneticsof pages 1-2)
6. **Variant confirmation:** orthogonal confirmation, parental segregation, phase determination, current gnomAD frequency, ClinVar review, conservation/structural analysis, and ACMG/AMP classification.
7. **Functional confirmation:** spectrophotometric respiratory-chain assays and blue-native PAGE/complexome or proteomic assessment in fibroblasts or muscle are particularly useful for novel/VUS alleles. Patient fibroblasts can show reduced NDUFA10/NDUFA9, low complex-I activity, reduced holoenzyme, and accumulated subcomplexes. (hoefs2011ndufa10mutationscause pages 3-4)

The first patient’s complex-I activity was 30 versus 104–206 in fibroblasts and 5 versus 70–250 in muscle—approximately 29% and 7% of the lower reference limit. Muscle complex III was mildly reduced to 68%, showing that modest secondary abnormalities do not negate primary complex-I disease. (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 2-3)

### Testing not routinely diagnostic

Karyotype, FISH, repeat-expansion testing, and isolated CMA do not directly test typical biallelic `NDUFA10` sequence variants. mtDNA analysis remains important in a broad Leigh differential but cannot identify a nuclear `NDUFA10` defect. Newborn population screening for MC1DN22 is unavailable. Once familial variants are known, targeted carrier, cascade, prenatal, and preimplantation testing are technically feasible.

### Differential diagnosis

The differential includes other nuclear or mtDNA complex-I deficiencies, pyruvate-dehydrogenase-complex deficiency, biotin-thiamine-responsive basal-ganglia disease, organic acidemias, other Leigh-spectrum disorders, mitochondrial aminoacyl-tRNA-synthetase disease, POLG-related disease, and toxic/infectious bilateral basal-ganglia injury. Distinction requires integrated genotype, respiratory-chain biochemistry, metabolic testing, and imaging rather than MRI alone. The 2017 authors emphasized that variable, nonspecific imaging requires combined clinical, biochemical, and neuroradiologic assessment. (minoia2017wideningtheheterogeneity pages 5-7, minoia2017wideningtheheterogeneity pages 1-2)

## 11. Outcome and prognosis

MC1DN22-specific 5- or 10-year survival, life expectancy, and mortality rates are unavailable. The first patient died from cardiorespiratory arrest at 23 months. The second remained neurologically progressive after partial temporary improvement, but final survival was not available in the retrieved evidence. (hoefs2011ndufa10mutationscause pages 2-3, minoia2017wideningtheheterogeneity pages 1-2)

Potential morbidity includes severe motor and cognitive disability, loss of ambulation, feeding/communication dependence, recurrent metabolic crises, dystonia/ataxia, respiratory compromise, cardiomyopathy, and premature death. No validated prognostic biomarker exists. Plausible adverse indicators—very low residual complex-I activity, early onset, brainstem disease, recurrent crises, cardiomyopathy, and respiratory dysfunction—are clinically reasonable but not validated in an NDUFA10 cohort.

## 12. Treatment

### Current care

There is no approved NDUFA10-directed drug, gene therapy, RNA therapy, cell therapy, or curative surgery. No NDUFA10-specific interventional clinical trial was identified by the trial search. The 2024 Leigh-model review likewise states that no disease-modifying treatment has been clinically approved for Leigh syndrome. (henke2024diseasemodelsof pages 1-2)

Management should be individualized in a specialist mitochondrial/metabolic center:

* prompt treatment of infection, fever, dehydration, hypoglycemia, and catabolism;
* adequate calories and hydration during illness, with an emergency metabolic plan;
* physical, occupational, speech/communication, feeding, and respiratory therapy;
* treatment of seizures, dystonia/spasticity, cardiomyopathy, pain, reflux, and sleep/respiratory disorders according to standard practice;
* nutritional assessment and aspiration prevention;
* periodic neurologic, developmental, cardiac, ophthalmologic, hearing, renal/hepatic, endocrine, and respiratory review according to manifestations.

Thiamine and biotin were used empirically in the 2017 child, with partial neurologic improvement followed by continued deterioration and febrile relapses. This uncontrolled observation does not establish efficacy. (minoia2017wideningtheheterogeneity pages 1-2)

Suggested NCIT intervention concepts include Genetic Counseling, Physical Therapy, Occupational Therapy, Speech Therapy, Nutritional Support, Anticonvulsant Therapy, Cardiac Monitoring, Respiratory Support, and Palliative Care. Exact NCIT codes should be resolved against the current release.

### Experimental research

Drosophila overexpression of ND42, the NDUFA10 homolog, restored complex-I activity and partially rescued flight, climbing, and flight-muscle mitochondrial abnormalities in `pink1` mutants, but not `parkin` mutants. This demonstrates functional relevance and a potential replacement principle, not treatment efficacy in MC1DN22. (pogson2014thecomplexi pages 2-4, pogson2014thecomplexi pages 1-2)

Gene replacement is conceptually attractive because `NDUFA10` is nuclear encoded, but delivery to brain, heart, and muscle, developmental timing, dosing, and safety remain unresolved. Complex-I hypoxia/suppressor studies and broader Leigh organoid/drug screens are preclinical and should not guide off-label exposure.

## 13. Prevention

The genetic lesion cannot presently be prevented after conception. Primary prevention is reproductive:

* carrier testing of the reproductive partner and at-risk relatives;
* targeted prenatal diagnosis by chorionic-villus sampling or amniocentesis after familial variants are established;
* preimplantation genetic testing for monogenic disease;
* donor gametes or adoption according to family preferences.

Because this is a **nuclear autosomal-recessive** disorder, mitochondrial replacement therapy is not an appropriate preventive strategy for `NDUFA10` variants. Secondary prevention consists of early molecular diagnosis and baseline cardiac, neurologic, nutritional, respiratory, and developmental assessment. Tertiary prevention includes vaccination according to routine schedules, prompt infection care, avoidance of prolonged fasting/catabolism, an emergency plan, aspiration prevention, and multidisciplinary surveillance. A genetics diagnosis is particularly important for counseling and reproductive options. (alston2021thegeneticsof pages 1-2)

## 14. Other species and natural disease

Orthologous NDUFA10/ND42 proteins occur across metazoans and preserve complex-I function. No naturally occurring companion-animal, livestock, or wildlife disease confidently equivalent to human MC1DN22 was retrieved, and no breed-specific VBO annotation or zoonotic transmission applies. The disorder is inherited, not infectious, and has no zoonotic potential.

## 15. Model organisms

### NDUFA10-relevant models

* **Drosophila melanogaster** (NCBI Taxonomy 7227): ND42 is the NDUFA10 homolog. RNAi caused excessive mitochondrial fusion/tubulation; transgenic ND42 or its co-chaperone Sicily restored complex-I activity and partially rescued locomotor and flight-muscle mitochondrial phenotypes in `pink1` mutants. Rescue was largely independent of mitophagy and did not require the tested Ser-250 phosphorylation site. This is direct NDUFA10-homolog functional evidence, but it models PINK1 deficiency rather than human biallelic MC1DN22. DOI: [10.1371/journal.pgen.1004815](https://doi.org/10.1371/journal.pgen.1004815), published 20 November 2014. (pogson2014thecomplexi pages 2-4, pogson2014thecomplexi pages 1-2)
* **Human patient fibroblasts:** the most disease-proximal model. They reproduce low NDUFA10/NDUFA9 abundance, reduced complex-I activity and holoenzyme, and abnormal assembly. They do not model neuronal circuitry or whole-organ physiology. (hoefs2011ndufa10mutationscause pages 3-4)

### Indirect Leigh/complex-I models

Yeast, C. elegans, zebrafish, Drosophila, Ndufs4-knockout mice, immortalized cells, patient-derived iPSCs, neurons, cardiomyocytes, and organoids are widely used for Leigh syndrome. A 2024 review emphasizes that iPSC-derived specialized cells and three-dimensional organoids permit cell-type-specific phenotyping and drug screening, but none should be described as an NDUFA10 MC1DN22 model unless `NDUFA10` itself is engineered or patient-derived. (henke2024diseasemodelsof pages 1-2)

No dedicated Ndufa10 knock-in mouse reproducing the reported human alleles, no NDUFA10 patient iPSC line, and no NDUFA10 brain organoid were verified in the retrieved literature. Priority models are isogenic CRISPR-corrected patient iPSCs differentiated into basal-ganglia neurons, brainstem neurons, cardiomyocytes, and myotubes; allele-specific knock-in zebrafish/mice; and rescue with wild-type NDUFA10.

## Recent developments, expert interpretation, and knowledge gaps

The most important contemporary development is methodological: exome and genome sequencing now provide a minimally invasive first-line route to diagnosis, while RNA sequencing, quantitative proteomics, metabolomics, and complexome profiling can resolve difficult variants. The expert review conclusion is that clinically relevant patient tissues and multidisciplinary multi-omics remain pivotal when DNA evidence alone is insufficient. (alston2021thegeneticsof pages 1-2)

The core conclusion from the primary human evidence is robust but narrow: **NDUFA10 is required for normal complex-I assembly/stability and activity**, and biallelic pathogenic variants can produce severe Leigh syndrome. The original study’s experimentally supported observation was reduced complex-I amount/activity and disturbed assembly; its broader proposal that NDUFA10 may regulate electron transfer or phosphorylation-dependent activity remains less certain. (hoefs2011ndufa10mutationscause pages 3-4, hoefs2011ndufa10mutationscause pages 4-5)

Major gaps are: (1) too few patients for frequencies or genotype–phenotype correlations; (2) incomplete modern ACMG/ClinVar/gnomAD curation of all historical alleles; (3) no prospective natural history; (4) no validated biomarker beyond general lactate, imaging, and complex-I assays; (5) no NDUFA10-specific single-cell or multi-omic tissue atlas; (6) no dedicated mammalian or organoid model; and (7) no targeted clinical trial. Any knowledge-base entry should therefore label most frequency, prognosis, and treatment fields as **unknown**, rather than extrapolating numerical values from all-cause Leigh syndrome.

## Key sources and dates

* Hoefs et al. “NDUFA10 mutations cause complex I deficiency in a patient with Leigh disease.” *European Journal of Human Genetics* 19:270–274; online 8 December 2010, issue March 2011. DOI: [10.1038/ejhg.2010.204](https://doi.org/10.1038/ejhg.2010.204). (hoefs2011ndufa10mutationscause pages 1-2, hoefs2011ndufa10mutationscause pages 2-3)
* Minoia et al. “Widening the Heterogeneity of Leigh Syndrome: Clinical, Biochemical, and Neuroradiologic Features in a Patient Harboring a NDUFA10 Mutation.” *JIMD Reports* 37:37–43; online 1 March 2017. DOI: [10.1007/8904_2017_9](https://doi.org/10.1007/8904_2017_9). (minoia2017wideningtheheterogeneity pages 2-5, minoia2017wideningtheheterogeneity pages 1-2)
* Alston et al. “The genetics of mitochondrial disease: dissecting mitochondrial pathology using multi-omic pipelines.” *Journal of Pathology* 254:430–442; online 26 March 2021. DOI: [10.1002/path.5641](https://doi.org/10.1002/path.5641). (alston2021thegeneticsof pages 1-2)
* Henke et al. “Disease models of Leigh syndrome: From yeast to organoids.” *Journal of Inherited Metabolic Disease* 47:1292–1321; accepted 18 September 2024. DOI: [10.1002/jimd.12804](https://doi.org/10.1002/jimd.12804). (henke2024diseasemodelsof pages 1-2)

PMIDs were not displayed in the retrieved full-text metadata; they should be resolved directly in PubMed before database deposition rather than guessed. The quoted article titles above are exact bibliographic titles; longer verbatim abstract quotations were avoided where the retrieved evidence did not expose exact abstract wording.

References

1. (hoefs2011ndufa10mutationscause pages 1-2): Saskia J G Hoefs, Francjan J van Spronsen, Ellen W H Lenssen, Leo G Nijtmans, Richard J Rodenburg, Jan A M Smeitink, and Lambert P van den Heuvel. Ndufa10 mutations cause complex i deficiency in a patient with leigh disease. European Journal of Human Genetics, 19:270-274, Mar 2011. URL: https://doi.org/10.1038/ejhg.2010.204, doi:10.1038/ejhg.2010.204. This article has 115 citations and is from a domain leading peer-reviewed journal.

2. (hoefs2011ndufa10mutationscause pages 2-3): Saskia J G Hoefs, Francjan J van Spronsen, Ellen W H Lenssen, Leo G Nijtmans, Richard J Rodenburg, Jan A M Smeitink, and Lambert P van den Heuvel. Ndufa10 mutations cause complex i deficiency in a patient with leigh disease. European Journal of Human Genetics, 19:270-274, Mar 2011. URL: https://doi.org/10.1038/ejhg.2010.204, doi:10.1038/ejhg.2010.204. This article has 115 citations and is from a domain leading peer-reviewed journal.

3. (minoia2017wideningtheheterogeneity pages 2-5): Francesca Minoia, Marta Bertamino, Paolo Picco, Mariasavina Severino, Andrea Rossi, Chiara Fiorillo, Carlo Minetti, Claudia Nesti, Filippo Maria Santorelli, and Maja Di Rocco. Widening the heterogeneity of leigh syndrome: clinical, biochemical, and neuroradiologic features in a patient harboring a ndufa10 mutation. JIMD reports, 37:37-43, Jan 2017. URL: https://doi.org/10.1007/8904\_2017\_9, doi:10.1007/8904\_2017\_9. This article has 20 citations and is from a peer-reviewed journal.

4. (minoia2017wideningtheheterogeneity pages 5-7): Francesca Minoia, Marta Bertamino, Paolo Picco, Mariasavina Severino, Andrea Rossi, Chiara Fiorillo, Carlo Minetti, Claudia Nesti, Filippo Maria Santorelli, and Maja Di Rocco. Widening the heterogeneity of leigh syndrome: clinical, biochemical, and neuroradiologic features in a patient harboring a ndufa10 mutation. JIMD reports, 37:37-43, Jan 2017. URL: https://doi.org/10.1007/8904\_2017\_9, doi:10.1007/8904\_2017\_9. This article has 20 citations and is from a peer-reviewed journal.

5. (henke2024diseasemodelsof pages 1-2): Marie‐Thérèse Henke, Alessandro Prigione, and Markus Schuelke. Disease models of leigh syndrome: from yeast to organoids. Journal of Inherited Metabolic Disease, 47:1292-1321, Oct 2024. URL: https://doi.org/10.1002/jimd.12804, doi:10.1002/jimd.12804. This article has 19 citations and is from a peer-reviewed journal.

6. (hoefs2011ndufa10mutationscause pages 3-4): Saskia J G Hoefs, Francjan J van Spronsen, Ellen W H Lenssen, Leo G Nijtmans, Richard J Rodenburg, Jan A M Smeitink, and Lambert P van den Heuvel. Ndufa10 mutations cause complex i deficiency in a patient with leigh disease. European Journal of Human Genetics, 19:270-274, Mar 2011. URL: https://doi.org/10.1038/ejhg.2010.204, doi:10.1038/ejhg.2010.204. This article has 115 citations and is from a domain leading peer-reviewed journal.

7. (minoia2017wideningtheheterogeneity pages 1-2): Francesca Minoia, Marta Bertamino, Paolo Picco, Mariasavina Severino, Andrea Rossi, Chiara Fiorillo, Carlo Minetti, Claudia Nesti, Filippo Maria Santorelli, and Maja Di Rocco. Widening the heterogeneity of leigh syndrome: clinical, biochemical, and neuroradiologic features in a patient harboring a ndufa10 mutation. JIMD reports, 37:37-43, Jan 2017. URL: https://doi.org/10.1007/8904\_2017\_9, doi:10.1007/8904\_2017\_9. This article has 20 citations and is from a peer-reviewed journal.

8. (dang2020analysisofhuman pages 28-30): Quynh-Chi L. Dang, Duong H. Phan, Abigail N. Johnson, Mukund Pasapuleti, Hind A. Alkhaldi, Fang Zhang, and Steven B. Vik. Analysis of human mutations in the supernumerary subunits of complex i. Life, 10:296, Nov 2020. URL: https://doi.org/10.3390/life10110296, doi:10.3390/life10110296. This article has 27 citations.

9. (pogson2014thecomplexi pages 2-4): Joe H. Pogson, Rachael M. Ivatt, Alvaro Sanchez-Martinez, Roberta Tufi, Emma Wilson, Heather Mortiboys, and Alexander J. Whitworth. The complex i subunit ndufa10 selectively rescues drosophila pink1 mutants through a mechanism independent of mitophagy. Nov 2014. URL: https://doi.org/10.1371/journal.pgen.1004815, doi:10.1371/journal.pgen.1004815. This article has 94 citations and is from a domain leading peer-reviewed journal.

10. (pogson2014thecomplexi pages 1-2): Joe H. Pogson, Rachael M. Ivatt, Alvaro Sanchez-Martinez, Roberta Tufi, Emma Wilson, Heather Mortiboys, and Alexander J. Whitworth. The complex i subunit ndufa10 selectively rescues drosophila pink1 mutants through a mechanism independent of mitophagy. Nov 2014. URL: https://doi.org/10.1371/journal.pgen.1004815, doi:10.1371/journal.pgen.1004815. This article has 94 citations and is from a domain leading peer-reviewed journal.

11. (alston2021thegeneticsof pages 1-2): Charlotte L Alston, Sarah L Stenton, Gavin Hudson, Holger Prokisch, and Robert W Taylor. The genetics of mitochondrial disease: dissecting mitochondrial pathology using multi‐omic pipelines. The Journal of Pathology, 254:430-442, Mar 2021. URL: https://doi.org/10.1002/path.5641, doi:10.1002/path.5641. This article has 81 citations.

12. (hoefs2011ndufa10mutationscause pages 4-5): Saskia J G Hoefs, Francjan J van Spronsen, Ellen W H Lenssen, Leo G Nijtmans, Richard J Rodenburg, Jan A M Smeitink, and Lambert P van den Heuvel. Ndufa10 mutations cause complex i deficiency in a patient with leigh disease. European Journal of Human Genetics, 19:270-274, Mar 2011. URL: https://doi.org/10.1038/ejhg.2010.204, doi:10.1038/ejhg.2010.204. This article has 115 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_22-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 27 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008872` (1 mention) - the report calls it "feeding/developmental milestone context as applicable"; HP calls it **Feeding difficulties in infancy**
- `HP:0001629` (1 mention) - the report calls it "ventricular hypertrophy/cardiomyopathy mapping should be phenotype-specific"; HP calls it **Ventricular septal defect**
- `HP:0001272` (1 mention) - the report calls it "cerebellar/brainstem-related imaging mapping only where supported"; HP calls it **Cerebellar atrophy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0008947` (1 mention) - the report calls it "infantile muscular hypotonia"; HP calls it **Floppy infant**, and lists "Infantile muscular hypotonia" among its other names
- `HP:0011968` (1 mention) - the report calls it "elevated circulating lactate"; HP calls it **Feeding difficulties**, and lists "Decreased oral intake" among its other names
- `HP:0002135` (1 mention) - the report calls it "basal ganglia abnormality"; HP calls it **Basal ganglia calcification**
- `HP:0002500` (1 mention) - the report calls it "abnormal cerebral white/gray matter imaging; use more specific HPO terms when available"; HP calls it **Abnormal cerebral white matter morphology**
- `GO:0005747` (1 mention) - the report calls it "mitochondrial respiratory-chain complex I"; GO calls it **obsolete mitochondrial respiratory chain complex I**