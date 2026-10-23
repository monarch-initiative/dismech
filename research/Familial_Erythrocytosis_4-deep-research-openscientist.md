---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-14T15:02:51.677025'
end_time: '2026-10-14T15:40:08.005666'
duration_seconds: 2236.33
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Erythrocytosis 4
  mondo_id: MONDO:0012729
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
citation_count: 14
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:41123216
  relevance_assessed: 15
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:35618957
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 36
  verified: 33
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0002315
    reported_labels:
    - Hyperviscosity-related; variable
    ontology_label: Headache
  - term_id: HP:0001907
    reported_labels:
    - Risk rises with hematocrit; episodic
    ontology_label: Thromboembolism
  - term_id: NCIT:C15843
    reported_labels:
    - Therapeutic Phlebotomy
    ontology_label: Preventive Intervention
  - term_id: NCIT:C156989
    reported_labels:
    - Belzutifan
    ontology_label: Walk or Hike Uphill Question
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0061418
    ontology_label: obsolete regulation of transcription from RNA polymerase II promoter
      in response to hypoxia
    replaced_by: GO:0006357
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
  path: Familial_Erythrocytosis_4-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Familial_Erythrocytosis_4-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Erythrocytosis 4
- **MONDO ID:** MONDO:0012729 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Erythrocytosis 4** covering all of the
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

# Familial Erythrocytosis 4 (ECYT4): A Comprehensive Disease Characteristics Report

**Disease:** Familial Erythrocytosis 4 (ECYT4)
**MONDO ID:** MONDO:0012729 | **OMIM:** 611783 | **Gene:** *EPAS1* (*HIF2A*)
**Category:** Mendelian, autosomal dominant
**Report date:** 2026-10-14

---

## Summary

**Familial Erythrocytosis 4 (ECYT4) is a rare autosomal dominant, secondary (erythropoietin-driven) hereditary erythrocytosis caused by germline gain-of-function missense variants in *EPAS1* (which encodes hypoxia-inducible factor 2-alpha, HIF-2α).** The causal variants cluster in the oxygen-dependent degradation domain (ODDD) of HIF-2α near the critical hydroxylation target proline 531 (P531). By disrupting this hydroxylation site, the variants prevent prolyl hydroxylase domain protein 2 (PHD2/EGLN1) from tagging HIF-2α for von Hippel–Lindau (pVHL)-mediated proteasomal degradation. HIF-2α is consequently stabilized, accumulates, translocates to the nucleus, and constitutively transactivates its target gene *EPO*, producing inappropriate erythropoietin secretion and absolute erythrocytosis with an inappropriately normal-to-elevated serum EPO level.

ECYT4 sits within a well-defined nosology of four Mendelian familial erythrocytoses. It is distinguished from ECYT1 (*EPOR*, primary, low EPO), ECYT2 (*VHL*/Chuvash, recessive, oxygen-sensing), and ECYT3 (*EGLN1*/PHD2, oxygen-sensing) as the *EPAS1*/HIF2A, high-EPO, dominantly inherited oxygen-sensing subtype. The same molecular lesion, when it arises post-zygotically as somatic mosaicism, produces a distinct multisystem disorder — **Pacak–Zhuang syndrome (PZS)** — characterized by multiple paragangliomas/pheochromocytomas, duodenal somatostatinomas, and polycythemia, along with ocular/retinal vascular abnormalities, pancreatic neuroendocrine tumors, and other developmental anomalies. ECYT4 (germline, heritable) and PZS (mosaic, tumor-predisposing) are therefore two phenotypic expressions of the same gain-of-function biology.

Clinically, ECYT4 is managed supportively with therapeutic phlebotomy, cardiovascular-risk optimization, and low-dose aspirin, while cytoreductive therapy is avoided. The most important recent advance is mechanism-targeted pharmacotherapy: **belzutifan**, a small-molecule HIF-2α inhibitor, has been used successfully to normalize hemoglobin in germline *EPAS1*-associated polycythemia without further phlebotomy, directly correcting the underlying pathophysiology. This report integrates nine confirmed findings drawn from 15 primary papers to document the disease across all requested domains, flagging gaps where disease-specific data are absent.

---

## Key Findings

### Finding 1 — Causal genetics: germline gain-of-function *EPAS1*/HIF2A variants clustering near Pro531

ECYT4 is caused by heterozygous germline gain-of-function missense variants in *EPAS1*, the gene encoding HIF-2α. In a European cohort of 41 patients plus 28 relatives with *EPAS1*-associated erythrocytosis, 11 mutations were classified as pathogenic across 17 patients and 23 relatives, and four novel mutations — **D525G, L526F, G527K, and A530S** — were identified clustering close to the key proline residue P531. The functional impact of these variants was validated by luciferase reporter assays demonstrating enhanced HIF-2α-dependent *EPO* promoter induction. As the authors state, *"Gain-of-function mutations in the EPAS1/HIF2A gene have been identified in patients with hereditary erythrocytosis that can be associated with the development of paraganglioma, pheochromocytoma and somatostatinoma"* and *"We described four new mutations (D525G, L526F, G527K, A530S) close to the key proline P531, which broadens the spectrum of mutations involved in erythrocytosis"* ([PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/)).

The P531 residue is the primary hydroxylation acceptor within the ODDD; variants adjacent to it mechanically shield the hydroxylation machinery, which explains the tight genotypic clustering. **Variant class:** missense (point mutations). **Origin:** germline (heritable). **Functional consequence:** gain of function. **HGNC:** EPAS1.

### Finding 2 — Core mechanism: escape from PHD2 hydroxylation and VHL degradation stabilizes HIF-2α and drives EPO

Under normoxia, HIF-α subunits are hydroxylated on specific proline residues by PHD2 (EGLN1), which creates the recognition motif for the pVHL E3 ubiquitin ligase complex and targets HIF-α for proteasomal degradation. Congenital erythrocytosis arises from lesions anywhere along this oxygen-sensing axis: *"CE has been found to be caused by loss-of-function mutations in VHL and PHD2/EGLN1 as well as gain-of-function mutations in HIF-2α (EPAS1), all resulting in constitutive activation of EPO signaling"* ([PMID: 33840141](https://pubmed.ncbi.nlm.nih.gov/33840141/)).

In ECYT4 specifically, the gain-of-function variants cause HIF-2α to evade hydroxylation: *"HIF-2α evades steady-state hydroxylation by the prolyl hydroxylase type 2 (PHD2), which accelerates von Hippel-Lindau (VHL)-mediated proteasomal degradation. In this situation, HIF-2α is stabilized and can translocate to the nucleus"* ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/)). Stabilized nuclear HIF-2α dimerizes with HIF-1β (ARNT) and transactivates hypoxia-response genes, foremost among them *EPO*. This is the central, biochemically demonstrated causal step of the disease.

### Finding 3 — HIF-2α is the principal physiologic transcriptional driver of EPO, tuned by oxygen, iron, and 2-oxoglutarate

The reason *EPAS1* gain-of-function produces erythrocytosis is that HIF-2α is the dominant physiologic transactivator of *EPO*: *"Hypoxia-inducible factor-2 alpha (HIF-2α), a positive regulator of the EPO gene"* ([PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/)). HIF-2α activity is normally tuned by multiple inputs — molecular oxygen and 2-oxoglutarate (co-substrates of PHD2), and iron, which modulates both PHD2 activity and HIF-2α translation. EPO expression and renal HIF-2α are suppressed by iron through an oxidative-stress-dependent pathway, and erythropoietin production is modulated by iron via iron-regulatory-protein/iron-responsive-element control of HIF-2α ([PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/); [PMID: 35618957](https://pubmed.ncbi.nlm.nih.gov/35618957/)). In ECYT4, the constitutive stabilization of HIF-2α overrides these physiologic brakes, uncoupling EPO production from true tissue oxygenation.

### Finding 4 — Historical discovery and heritability

*EPAS1*/HIF2A gain-of-function mutations were first reported in 2012. The landmark paper identified *"two novel somatic gain-of-function mutations in the gene encoding hypoxia-inducible factor 2α (HIF2A) in two patients, one presenting with paraganglioma and the other with paraganglioma and somatostatinoma, both of whom had polycythemia. The two mutations were associated with increased HIF-2α activity and increased protein half-life"* ([PMID: 22931260](https://pubmed.ncbi.nlm.nih.gov/22931260/)). The heritable, germline nature of the erythrocytosis phenotype was established shortly afterward by the report of a germline **F374Y (exon 9)** variant: *"We now report a polycythemic patient with a novel germline HIF2A (F374Y) (exon 9) mutation, inherited from his mother, who developed PHEO/PGL. We show that this is a gain-of-function mutation"* ([PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/)). Notably, there was no loss of heterozygosity in the tumor, consistent with a dominant gain-of-function rather than a classic tumor-suppressor two-hit mechanism.

### Finding 5 — The mosaic counterpart: Pacak–Zhuang syndrome

The somatic-mosaic version of ECYT4 biology is Pacak–Zhuang syndrome (PZS): *"a new syndrome of multiple paragangliomas, somatostatinomas, and polycythemia caused by early postzygotic mosaic mutations in EPAS1, encoding hypoxia-inducible factor 2 alpha (HIF-2α)"* ([PMID: 37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/)). In PZS, polycythemia precedes tumor development and is only partially corrected by tumor removal, with recurrence shortly after surgery ([PMID: 31091718](https://pubmed.ncbi.nlm.nih.gov/31091718/)). EPAS1-related pheochromocytomas/paragangliomas (PPGLs) comprise roughly 3–6% of all PPGLs and show a characteristic phenotype: *"EPAS1-related PPGLs usually occur in the second or third decade of life, more frequently in females, and are usually multiple, adrenal and extra-adrenal, and norepinephrine-secreting"* with metastatic disease in up to 30% ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/)). The phenotypic spectrum also includes ocular/retinal and choroidal vascular abnormalities ([PMID: 31876943](https://pubmed.ncbi.nlm.nih.gov/31876943/)), Chiari malformation type 1 ([PMID: 31185588](https://pubmed.ncbi.nlm.nih.gov/31185588/)), and pancreatic neuroendocrine tumors ([PMID: 41518596](https://pubmed.ncbi.nlm.nih.gov/41518596/)).

### Finding 6 — Mechanism-targeted therapy: belzutifan

The most consequential therapeutic advance is direct pharmacologic inhibition of HIF-2α. In the first reported use of belzutifan for germline *EPAS1*-associated polycythemia — an 11-year-old with a likely-pathogenic *EPAS1* variant causing polycythemia, pulmonary hypertension, and ischemic stroke — *"she started novel therapy with belzutifan, a small molecule inhibitor of HIF-2α, to target her underlying disease pathophysiology. This is the first reported usage of belzutifan for EPAS1-associated polycythemia. The therapy has been well tolerated, and her hemoglobin was restored to normal levels without the need for additional phlebotomy"* ([PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/)). This addresses the disease at its causal node rather than merely managing its hematologic consequence.

### Finding 7 — Transgenic mouse model recapitulation

A transgenic mouse model expressing a gain-of-function *EPAS1*/HIF-2α mutation recapitulates the human phenotype. Through the NIH PPGL translational program, *"the generation and study of a corresponding disease mouse model ... has provided new insights into the natural history of these developmental anomalies and the pathophysiologic role of HIF-2α"* ([PMID: 37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/)). A specific **Epas1^A529V** transgenic model reproduced the ocular/retinal and choroidal vascular features seen in patients ([PMID: 31876943](https://pubmed.ncbi.nlm.nih.gov/31876943/)), and models have been used to study polycythemia, vascular malformations, and neural tube defects ([PMID: 31091718](https://pubmed.ncbi.nlm.nih.gov/31091718/)).

### Finding 8 — Diagnostic framework

Diagnosis requires systematic exclusion of polycythemia vera (PV) and secondary causes. In JAK2-unmutated erythrocytosis, *"Hereditary erythrocytosis should be considered in longstanding erythrocytosis with a positive family history; causes include EPOR mutations (subnormal Epo), high oxygen affinity hemoglobin variants, PIEZO1 mutations, 2,3-bisphosphoglycerate deficiency, methemoglobinemia, and germline oxygen sensing pathway mutations (HIF2A-PHD2-VHL)"* ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)). Management guidance: *"Cytoreductive therapy should be avoided. Phlebotomy should be considered for symptom control. Cardiovascular risk optimization and low-dose aspirin are advised, while the role of HIF2A inhibitors remains unclear"* ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)).

### Finding 9 — Position within the Mendelian erythrocytosis nosology

ECYT4 is one of four classically numbered familial erythrocytoses, distinguished by causal gene, inheritance, and EPO level (see table in the Mechanistic Model section). It is the *EPAS1*/HIF2A, high-EPO, autosomal-dominant, oxygen-sensing subtype ([PMID: 33840141](https://pubmed.ncbi.nlm.nih.gov/33840141/)).

---

## Section-by-Section Report

### 1. Disease Information

- **Overview:** ECYT4 is a rare inherited absolute erythrocytosis (increased red cell mass) caused by constitutive activation of HIF-2α, leading to inappropriate erythropoietin production and secondary polycythemia. It is a lifelong, congenital-onset condition.
- **Key identifiers:** MONDO:0012729; OMIM 611783; gene *EPAS1* (HGNC:3374, OMIM 603349, chromosome 2p21). MeSH: "Familial Erythrocytosis" / "Polycythemia." ICD-10: D75.1 (secondary polycythemia). ICD-11: 3A81 (secondary polycythaemia). Orphanet: within the familial erythrocytosis grouping (e.g., ORPHA:90042 "Autosomal dominant secondary polycythemia"). *(Exact Orphanet subtype code for ECYT4 is not firmly established in the reviewed sources — flagged as uncertain.)*
- **Synonyms/alternative names:** Familial erythrocytosis 4; ECYT4; erythrocytosis, familial, 4; *EPAS1*-related/HIF2A-related congenital erythrocytosis; HIF2A erythrocytosis. The germline erythrocytosis-only presentation is distinct from the mosaic "Pacak–Zhuang syndrome" / "EPAS1 gain-of-function mutation syndrome."
- **Information source:** Primarily aggregated disease-level resources (OMIM, cohort studies, case series) complemented by individual case reports; no large EHR-derived datasets were used.

### 2. Etiology

- **Primary cause (genetic):** Germline heterozygous gain-of-function missense variants in *EPAS1*/HIF2A ([PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/); [PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/)).
- **Genetic risk factors:** The causal variants themselves are the risk factor; they cluster in the C-terminal ODDD near codon 531 (e.g., D525G, L526F, G527K, A530S) and in exon 9 (e.g., F374Y). No separate susceptibility loci or validated modifier genes are established for ECYT4 in the reviewed literature.
- **Environmental risk factors:** None established as *causing* ECYT4. However, HIF-2α activity is physiologically sensitive to hypoxia and iron; environmental hypoxia (altitude) and iron status may plausibly modulate phenotype severity (inferred, not demonstrated for ECYT4).
- **Protective factors:** No genetic protective variants or environmental protective factors specific to ECYT4 are documented. Mechanistically, iron sufficiency suppresses HIF-2α/EPO ([PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/)), but therapeutic phlebotomy deliberately induces iron deficiency, so the net clinical interaction is complex (inferred).
- **Gene–environment interactions:** Not specifically characterized; the oxygen- and iron-responsiveness of the HIF pathway is the plausible substrate for GxE effects (inferred).

### 3. Phenotypes

The core phenotype is a **laboratory abnormality** — absolute erythrocytosis — with downstream clinical signs and symptoms from hyperviscosity and the thrombotic tendency of a high hematocrit.

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| Erythrocytosis / increased red cell mass | Lab abnormality | Congenital onset; lifelong; variable severity | HP:0001901 (Polycythemia) |
| Elevated hemoglobin/hematocrit | Lab abnormality | Congenital; progressive if untreated | HP:0001899 (Increased hemoglobin) |
| Inappropriately normal/high serum EPO | Lab abnormality | Characteristic; distinguishes from EPOR (ECYT1) low-EPO forms | HP:0003573 (Increased serum EPO) |
| Headache | Symptom | Hyperviscosity-related; variable | HP:0002315 |
| Thrombosis / thromboembolism | Clinical sign | Risk rises with hematocrit; episodic | HP:0001907 |
| Pulmonary hypertension | Clinical sign | Reported in severe germline cases | HP:0002092 |
| Ischemic stroke | Clinical sign | Reported in severe germline cases | HP:0002140 |

In germline ECYT4, severe vascular complications (pulmonary hypertension, ischemic stroke) can occur, as in the pediatric case treated with belzutifan ([PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/)). Tumor phenotypes (PPGL, somatostatinoma) and ocular/retinal vascular disease are predominantly features of the **mosaic** PZS form rather than typical germline erythrocytosis-only ECYT4, though the germline tumor-predisposing variant in [PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/) shows overlap is possible. **Quality-of-life data** specific to ECYT4 (EQ-5D, SF-36) are not available in the reviewed literature.

### 4. Genetic / Molecular Information

- **Causal gene:** *EPAS1* / HIF2A (HGNC:3374; OMIM 603349; chromosome 2p21).
- **Pathogenic variants:** Missense substitutions in the ODDD clustering near P531 (D525G, L526F, G527K, A530S) and exon-9 variants (F374Y); A529V used in mouse modeling ([PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/); [PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/); [PMID: 31876943](https://pubmed.ncbi.nlm.nih.gov/31876943/)).
- **Classification:** Pathogenic / likely pathogenic per ACMG, supported by functional luciferase/EPO-promoter assays (functional evidence, PS3) and recurrent clustering (PM1) ([PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/)).
- **Variant type/class:** Missense point mutations.
- **Allele frequency:** Essentially absent from population databases (gnomAD) given rarity and pathogenicity (consistent with private/de novo and familial transmission; not explicitly quantified in sources).
- **Somatic vs germline:** Both occur — germline (heritable ECYT4) and postzygotic somatic mosaic (PZS). No loss of heterozygosity in associated tumors ([PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/); [PMID: 37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/)).
- **Functional consequence:** Gain of function — increased HIF-2α protein half-life and transcriptional activity ([PMID: 22931260](https://pubmed.ncbi.nlm.nih.gov/22931260/)).
- **Modifier genes / epigenetics / chromosomal abnormalities:** None established for ECYT4.

### 5. Environmental Information

No environmental, lifestyle, or infectious agents cause ECYT4; it is a monogenic disorder. Physiologic modulators of the HIF-2α/EPO axis (ambient oxygen tension/altitude, iron availability) may theoretically influence phenotype expression but are not established disease determinants ([PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/); [PMID: 35618957](https://pubmed.ncbi.nlm.nih.gov/35618957/)). Smoking and other causes of secondary erythrocytosis are relevant only as differential diagnoses to exclude.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A germline gain-of-function missense variant in *EPAS1* alters the HIF-2α ODDD near P531 → **leads to** impaired recognition of HIF-2α by PHD2 (EGLN1). *(demonstrated — variant clustering + functional assays, [PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/))*
2. Impaired PHD2-mediated prolyl hydroxylation → **results in** failure of pVHL E3-ligase recognition and loss of ubiquitin-proteasomal degradation of HIF-2α. *(demonstrated, [PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/))*
3. Escape from degradation → **leads to** stabilization and nuclear accumulation of HIF-2α (increased protein half-life). *(demonstrated, [PMID: 22931260](https://pubmed.ncbi.nlm.nih.gov/22931260/); [PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/))*
4. Nuclear HIF-2α dimerizes with HIF-1β/ARNT and binds hypoxia-response elements → **results in** constitutive transactivation of *EPO*. *(demonstrated via EPO-promoter luciferase assays, [PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/); [PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/))*
5. Inappropriately elevated erythropoietin → **leads to** increased EPO-receptor signaling in erythroid progenitors and expanded erythropoiesis. *(demonstrated, [PMID: 33840141](https://pubmed.ncbi.nlm.nih.gov/33840141/))*
6. Expanded red cell mass → **results in** erythrocytosis, elevated hematocrit, and increased blood viscosity → **leads to** headache, thrombosis, and (in severe cases) pulmonary hypertension and ischemic stroke. *(clinical, [PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/))*

**Branch (mosaic lesion):** The identical gain-of-function lesion arising **post-zygotically** → produces mosaic tissue distribution → **leads to** Pacak–Zhuang syndrome: multiple PPGLs, duodenal somatostatinoma, pancreatic NETs, polycythemia, and developmental vascular/ocular anomalies ([PMID: 37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/); [PMID: 41518596](https://pubmed.ncbi.nlm.nih.gov/41518596/); [PMID: 31876943](https://pubmed.ncbi.nlm.nih.gov/31876943/)).

**Upstream vs downstream:** The mutation, hydroxylation escape, and HIF-2α stabilization are upstream; EPO upregulation is the pivotal intermediate; erythrocytosis and its vascular sequelae are downstream.

**Molecular pathway:** HIF oxygen-sensing / hypoxia-response pathway (EGLN1/PHD2 → VHL → HIF-2α → EPO). **Co-substrates:** molecular O₂, 2-oxoglutarate (α-ketoglutarate, CHEBI:30915), ferrous iron (CHEBI:29033) ([PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/)).

**Suggested GO terms:** cellular response to hypoxia (GO:0071456); regulation of transcription from RNA Pol II promoter in response to hypoxia (GO:0061418); protein hydroxylation (GO:0018126); proteasome-mediated ubiquitin-dependent protein catabolic process (GO:0043161); positive regulation of erythrocyte differentiation (GO:0045648).

**Suggested CL terms:** EPO-producing renal interstitial fibroblast; erythroid progenitor cell (CL:0000038); erythroblast (CL:0000765); erythrocyte (CL:0000232).

### 7. Anatomical Structures Affected

- **Organ level (primary):** Kidney (renal interstitial EPO-producing cells; UBERON:0002113) as the EPO source; bone marrow (UBERON:0002371) as the site of expanded erythropoiesis. **Secondary/complication:** blood/vasculature (UBERON:0000178), lungs (pulmonary hypertension; UBERON:0002048), brain (ischemic stroke; UBERON:0000955).
- **Body systems:** Hematopoietic and cardiovascular systems primarily. In the mosaic PZS branch, additionally the autonomic/adrenal system (adrenal medulla, UBERON:0001235; paraganglia), duodenum/pancreas (UBERON:0002114 / UBERON:0001264), and eye (retina/choroid, UBERON:0000966 / UBERON:0001776).
- **Tissue/cell level:** Erythroid lineage cells; renal peritubular fibroblasts; (mosaic) chromaffin cells, neuroendocrine cells, vascular endothelium.
- **Subcellular compartments:** Nucleus (GO:0005634) — site of HIF-2α transcriptional action; cytoplasm — site of hydroxylation/degradation; proteasome (GO:0000502).
- **Lateralization:** Systemic/bilateral (hematologic); tumors in PZS are frequently multiple and bilateral/multifocal.

### 8. Temporal Development

- **Onset:** Congenital — erythrocytosis is present from early life, often detected in childhood or young adulthood; family history is typical ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)). In PZS, polycythemia precedes tumors, which arise in the 2nd–3rd decade ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/); [PMID: 31091718](https://pubmed.ncbi.nlm.nih.gov/31091718/)).
- **Onset pattern:** Chronic/insidious.
- **Progression:** Erythrocytosis is stable-to-progressive and lifelong without treatment; tumor burden (PZS) can be progressive, recurrent, and metastatic (up to ~30%) ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/)).
- **Remission/critical periods:** No spontaneous remission of erythrocytosis; it is treatment-controlled. Early detection permits intervention before thrombotic complications.

### 9. Inheritance and Population

- **Inheritance:** Autosomal dominant (germline ECYT4) ([PMID: 33840141](https://pubmed.ncbi.nlm.nih.gov/33840141/); [PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/)).
- **Penetrance/expressivity:** Appears high for erythrocytosis but with variable expressivity for vascular/tumor features; precise penetrance estimates are not established.
- **Epidemiology:** Very rare; ECYT4 is one of the rarest familial erythrocytoses. Precise prevalence/incidence figures are not available. *EPAS1* variants account for ~3–6% of PPGLs (the mosaic phenotype context) ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/)).
- **Sex ratio:** The *EPAS1*-related tumor phenotype is more frequent in females ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/)); a sex skew for isolated germline erythrocytosis is not established.
- **Founder effects / consanguinity / anticipation / mosaicism:** No founder effect or consanguinity role (dominant). Postzygotic somatic mosaicism is the defining feature of the PZS branch. No genetic anticipation.

### 10. Diagnostics

- **Initial workup:** Confirm absolute erythrocytosis (elevated Hb/Hct, increased red cell mass); measure serum EPO (inappropriately normal/elevated in ECYT4, contrasting with the subnormal EPO of EPOR-driven ECYT1); exclude PV by *JAK2* V617F and exon 12 testing ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)).
- **Exclude secondary causes:** Hypoxia, high-oxygen-affinity hemoglobin variants, smoking, EPO-secreting tumors.
- **Genetic testing:** Targeted *EPAS1* sequencing or a hereditary-erythrocytosis gene panel (EPAS1, EGLN1, VHL, EPOR, HBB/HBA, BPGM, PIEZO1). For suspected mosaicism (PZS), deep sequencing of tumor/affected tissue rather than blood may be required, since variants can be absent or low-level in peripheral blood ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/); [PMID: 37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/)).
- **Differential diagnosis:** PV (JAK2+); other hereditary erythrocytoses (ECYT1/EPOR, ECYT2/VHL-Chuvash, ECYT3/EGLN1); secondary erythrocytosis.
- **Imaging:** Not required for isolated erythrocytosis; in PZS, functional/anatomic imaging for PPGL surveillance.

### 11. Outcome / Prognosis

With appropriate control of hematocrit, the hematologic prognosis of germline ECYT4 is generally good; the principal threat is **thrombosis/hyperviscosity**, with severe cases suffering pulmonary hypertension and ischemic stroke ([PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/)). Disease-specific survival/mortality rates are not quantified in the reviewed literature. In the mosaic PZS branch, prognosis is driven by tumor behavior, including metastatic PPGL in up to ~30% ([PMID: 39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/)). **Prognostic factors:** hematocrit control, presence of vascular complications, and (in PZS) tumor multiplicity/metastasis.

### 12. Treatment

| Modality | Intervention | Role / evidence | Suggested NCIT |
|---|---|---|---|
| Supportive | Therapeutic phlebotomy | First-line for symptom/hematocrit control ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)) | NCIT:C15843 (Therapeutic Phlebotomy) |
| Risk reduction | Low-dose aspirin + CV risk optimization | Advised to reduce thrombosis ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)) | NCIT:C287 (Aspirin) |
| Avoid | Cytoreductive therapy | Should be avoided ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)) | — |
| Targeted | Belzutifan (HIF-2α inhibitor) | Normalized Hb without phlebotomy; mechanism-targeted; first reported in germline EPAS1 polycythemia ([PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/)) | NCIT:C156989 (Belzutifan) |
| PZS tumors | Surgery ± systemic therapy | For PPGL/somatostatinoma; polycythemia only partially corrected by tumor removal ([PMID: 31091718](https://pubmed.ncbi.nlm.nih.gov/31091718/)) | NCIT:C17173 (Surgical Procedure) |

**Pharmacogenomics / personalized medicine:** Belzutifan exemplifies genotype-guided precision therapy — a drug directly targeting the mutated HIF-2α protein. Its routine role in hereditary erythrocytosis is still being defined; guidelines note *"the role of HIF2A inhibitors remains unclear"* ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)), reflecting the gap between early case-level success and formal evidence.

### 13. Prevention

As a monogenic disorder, ECYT4 cannot be prevented primarily. Relevant measures are:
- **Secondary prevention:** Early detection via family screening and genetic testing; cascade testing of at-risk relatives given autosomal dominant inheritance.
- **Tertiary prevention:** Hematocrit control (phlebotomy/belzutifan), aspirin, and CV risk-factor management to prevent thrombosis; in PZS, PPGL surveillance ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/); [PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/)).
- **Counseling:** Genetic counseling for affected families; prenatal/preimplantation options are theoretically available for known family variants. No immunization is applicable.

### 14. Other Species / Natural Disease

- **Taxonomy / orthologs:** Human *EPAS1* (NCBI Gene 2034) has a mouse ortholog *Epas1* (NCBI Gene 13819). The oxygen-sensing pathway (EGLN1/VHL/HIF-2α/EPO) is deeply conserved across mammals.
- **Natural disease in other species:** No well-characterized naturally occurring *EPAS1* gain-of-function erythrocytosis is documented in companion animals or wildlife in the reviewed sources. (*EPAS1* is notable in high-altitude adaptation genetics, e.g., Tibetan human populations and some animals, but that is adaptive variation, not disease.)
- **Zoonotic potential:** Not applicable (non-infectious).

### 15. Model Organisms

- **Mouse (primary model):** Transgenic mice expressing gain-of-function *Epas1*/HIF-2α (including **Epas1^A529V**) recapitulate polycythemia, vascular malformations, neural tube defects, and ocular/retinal/choroidal vascular changes ([PMID: 31091718](https://pubmed.ncbi.nlm.nih.gov/31091718/); [PMID: 31876943](https://pubmed.ncbi.nlm.nih.gov/31876943/); [PMID: 37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/)).
- **Model type:** Mammalian, transgenic/knock-in gain-of-function.
- **Phenotype recapitulation:** Strong for polycythemia and the developmental/vascular/ocular PZS features; the model has clarified natural history and the pathophysiologic role of HIF-2α.
- **Limitations:** Mouse models of mosaic PZS may not fully reproduce the human tumor spectrum or variant-specific severity; germline erythrocytosis-only phenotypes versus mosaic tumor phenotypes depend on expression timing and tissue distribution.
- **Resources:** MGI for *Epas1* alleles; NIH PPGL translational program models.

---

## Mechanistic Model / Interpretation

```
 Germline EPAS1 gain-of-function variant (e.g., D525G/L526F/G527K/A530S near P531; F374Y exon 9)
                                   │
                                   ▼
         Impaired PHD2 (EGLN1) prolyl-hydroxylation of HIF-2α at P531
                                   │
                                   ▼
          Loss of pVHL recognition → no ubiquitin-proteasomal degradation
                                   │
                                   ▼
           HIF-2α stabilized (↑ half-life) → nuclear accumulation
                                   │
                                   ▼
         HIF-2α:HIF-1β binds HRE → constitutive EPO transactivation
                                   │
                                   ▼
        ↑ Serum EPO (inappropriately normal/high) → ↑ erythropoiesis
                                   │
                                   ▼
      Erythrocytosis / ↑ hematocrit / hyperviscosity
                                   │
             ┌─────────────────────┴─────────────────────┐
             ▼                                            ▼
   Headache, thrombosis                     Pulmonary hypertension, ischemic stroke
                                                   (severe cases)

   ── Branch: identical lesion arising POST-ZYGOTICALLY (mosaic) ──►
      Pacak–Zhuang syndrome: multiple PPGL + somatostatinoma +
      pancreatic NET + polycythemia + ocular/vascular + Chiari I
```

**Comparative nosology of Mendelian familial erythrocytoses:**

| Subtype | Gene | Mechanism | Inheritance | Serum EPO |
|---|---|---|---|---|
| ECYT1 | *EPOR* | Gain-of-function (primary) | AD | Low/subnormal |
| ECYT2 (Chuvash) | *VHL* | Loss-of-function (O₂-sensing) | AR | Elevated |
| ECYT3 | *EGLN1*/PHD2 | Loss-of-function (O₂-sensing) | AD | Normal/elevated |
| **ECYT4** | ***EPAS1*/HIF2A** | **Gain-of-function (O₂-sensing)** | **AD** | **Normal/elevated** |

*All secondary (O₂-sensing) subtypes converge on constitutive EPO signaling ([PMID: 33840141](https://pubmed.ncbi.nlm.nih.gov/33840141/)).* The key conceptual insight is that ECYT4 is the **gain-of-function endpoint** of the same pathway whose loss-of-function endpoints (VHL, EGLN1) produce ECYT2/ECYT3 — all four classic subtypes are reducible to "too much EPO signal," reached by different molecular routes.

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/) | *Comprehensive EPAS1 cohort* | Defines causal germline variants clustering near P531; functional validation (F001) |
| [33840141](https://pubmed.ncbi.nlm.nih.gov/33840141/) | *Congenital erythrocytosis* | Places EPAS1 GoF in O₂-sensing nosology; constitutive EPO (F002, F009) |
| [39426935](https://pubmed.ncbi.nlm.nih.gov/39426935/) | *HIF-2α in PPGL pathogenesis* | Molecular stabilization mechanism; tumor demographics (F002, F003) |
| [37450881](https://pubmed.ncbi.nlm.nih.gov/37450881/) | *Pacak–Zhuang syndrome* | Defines mosaic syndrome; mouse model insights (F003, F007) |
| [40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/) | *Belzutifan in EPAS1 erythrocytosis* | First mechanism-targeted therapy success (F004, F006) |
| [22931260](https://pubmed.ncbi.nlm.nih.gov/22931260/) | *Somatic HIF2A GoF, 2012* | Landmark discovery; ↑ half-life/activity (F005) |
| [23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/) | *Germline EPAS1 F374Y* | Proves heritable germline GoF; no tumor LOH (F005) |
| [41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/) | *JAK2-unmutated erythrocytosis 2026* | Diagnostic/management framework (F006) |
| [28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/) | *Iron suppresses EPO via HIF-2α* | HIF-2α as EPO regulator; iron tuning (F008) |
| [35618957](https://pubmed.ncbi.nlm.nih.gov/35618957/) | *Iron–erythropoiesis crosstalk* | IRP/IRE control of HIF-2α (F008) |
| [31876943](https://pubmed.ncbi.nlm.nih.gov/31876943/) | *Retinal/choroidal changes in PZS* | Ocular phenotype; Epas1^A529V mouse (F003, F007) |
| [31091718](https://pubmed.ncbi.nlm.nih.gov/31091718/) | *Transgenic PZS mouse* | Model of mosaic GoF; polycythemia before tumors (F007) |
| [31185588](https://pubmed.ncbi.nlm.nih.gov/31185588/) | *Chiari I in EPAS1 syndrome* | Expands developmental phenotype (F003) |
| [41518596](https://pubmed.ncbi.nlm.nih.gov/41518596/) | *Pancreatic NETs in PZS* | Expands tumor spectrum (F003) |
| [27659016](https://pubmed.ncbi.nlm.nih.gov/27659016/) | *HIF2A PPGL expression cluster* | HIF2A tumors form discrete pseudohypoxic subcluster |

**Consistency:** The 15 papers are mutually reinforcing, with no direct contradictions. The main tension is interpretive: case-level success with belzutifan ([PMID: 40879399](https://pubmed.ncbi.nlm.nih.gov/40879399/)) versus the 2026 guideline's cautious "role remains unclear" ([PMID: 41123216](https://pubmed.ncbi.nlm.nih.gov/41123216/)) — reflecting an evidence-maturity gap rather than disagreement.

---

## Supported and Refuted Hypotheses

No hypotheses were formally refuted during the investigation. The following working hypotheses were **supported** by the evidence:

- **H1 (supported):** ECYT4 is caused by germline gain-of-function *EPAS1* variants near P531 → confirmed (F001, [PMID: 36700397](https://pubmed.ncbi.nlm.nih.gov/36700397/)).
- **H2 (supported):** The mechanism is escape from PHD2/VHL degradation → HIF-2α stabilization → EPO upregulation → confirmed (F002, F003, F008).
- **H3 (supported):** Germline and mosaic forms are two expressions of the same lesion → confirmed (F005, F003).
- **H4 (supported):** HIF-2α inhibition (belzutifan) is a rational, effective therapy → supported by first case report (F004/F006), with the caveat that formal evidence is still limited.

---

## Limitations and Knowledge Gaps

1. **Epidemiology:** No reliable prevalence/incidence figures for germline ECYT4; it is simply described as very rare. Penetrance and expressivity estimates are not quantified.
2. **Germline vs mosaic phenotype boundary:** Much of the deep phenotyping (tumors, ocular, Chiari) derives from the **mosaic** PZS form; the degree to which isolated germline ECYT4 patients develop tumors is less well characterized, though overlap exists ([PMID: 23090011](https://pubmed.ncbi.nlm.nih.gov/23090011/)).
3. **Therapy evidence:** Belzutifan data in germline erythrocytosis are limited to case-level reports; no randomized/controlled data, long-term safety, or dosing standards exist for this indication.
4. **Quality-of-life / natural history:** No ECYT4-specific QoL instruments or longitudinal cohort outcome data were identified.
5. **Allele frequencies and ACMG population criteria:** Precise gnomAD frequencies for individual ECYT4 variants were not extracted.
6. **No primary data analysis:** This report is a literature synthesis; no patient-level datasets were available for independent statistical testing.

---

## Proposed Follow-up Experiments / Actions

1. **Belzutifan evidence development:** Design a prospective registry or basket trial of HIF-2α inhibition in genetically confirmed germline *EPAS1* erythrocytosis, with hematocrit, EPO, thrombotic events, pulmonary pressures, and safety (hypoxia, anemia) as endpoints.
2. **Genotype–phenotype mapping:** Correlate specific ODDD variants (P531-proximal vs exon-9) with erythrocytosis severity and tumor risk to refine surveillance recommendations and penetrance estimates.
3. **Tumor-risk stratification in germline carriers:** Systematically screen germline ECYT4 families for PPGL/somatostatinoma to quantify the germline tumor penetrance currently inferred mainly from mosaic cases.
4. **Population screening:** Query gnomAD/large biobanks for *EPAS1* ODDD variants to estimate true allele frequencies and carrier burden.
5. **Mechanistic refinement:** Use the Epas1^A529V (and new knock-in) mouse models plus structural/AlphaFold analysis of the HIF-2α ODDD to quantify how each variant perturbs PHD2 docking, informing variant classification (PS3).
6. **Iron-axis modulation:** Formally test whether iron status (deliberately lowered by phlebotomy) interacts with HIF-2α stability to modulate ECYT4 severity ([PMID: 28263291](https://pubmed.ncbi.nlm.nih.gov/28263291/)).

---

*Report compiled from 9 confirmed findings and 15 primary-literature sources across a 5-iteration autonomous investigation. Evidence source types: predominantly human clinical (cohorts/case reports) and model organism (transgenic mouse), supported by in vitro functional assays.*


## Artifacts

- [OpenScientist final report](Familial_Erythrocytosis_4-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Familial_Erythrocytosis_4-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41123216` *(abstract only)*: "role remains unclear"
  - Text part not found as substring: 'role remains unclear' (note: only abstract available for PMID:41123216, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35618957` (6 mentions) - The mutual crosstalk between iron and erythropoiesis.
  - shared terms: none

Weighed against this report's own most characteristic terms: `epas1`, `hif-2`, `erythrocytosis`, `ecyt4`, `germline`, `epo`, `variant`, `tumor`, `pzs`, `mosaic`, `gain-of-function`, `polycythemia`, `gene`, `hif2a`, `ppgl`, `phenotype`, `disease`, `mutation`, `belzutifan`, `vascular`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 10 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002315` (1 mention) - the report calls it "Hyperviscosity-related; variable"; HP calls it **Headache**
- `HP:0001907` (1 mention) - the report calls it "Risk rises with hematocrit; episodic"; HP calls it **Thromboembolism**
- `NCIT:C15843` (1 mention) - the report calls it "Therapeutic Phlebotomy"; NCIT calls it **Preventive Intervention**
- `NCIT:C156989` (1 mention) - the report calls it "Belzutifan"; NCIT calls it **Walk or Hike Uphill Question**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0061418` (obsolete regulation of transcription from RNA polymerase II promoter in response to hypoxia) (1 mention) - replaced by `GO:0006357`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001899` (1 mention) - the report calls it "Increased hemoglobin"; HP calls it **Increased hematocrit**
- `HP:0003573` (1 mention) - the report calls it "Increased serum EPO"; HP calls it **Increased total bilirubin**, and lists "Increased bilirubin" among its other names
- `GO:0005634` (1 mention) - the report calls it "Subcellular compartments:** Nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `NCIT:C17173` (1 mention) - the report calls it "Surgical Procedure"; NCIT calls it **Surgery**, and lists "Surgical Profession" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.