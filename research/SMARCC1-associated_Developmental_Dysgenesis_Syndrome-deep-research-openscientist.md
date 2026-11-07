---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-04T18:23:55.819810'
end_time: '2026-11-04T18:43:19.901713'
duration_seconds: 1164.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SMARCC1-associated Developmental Dysgenesis Syndrome
  mondo_id: MONDO:0700123
  category: Mendelian
  causal_genes: SMARCC1
  omim_id: not recorded
  synonyms: SMARCC1-related BAFopathy
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
citation_count: 21
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 21
  on_topic: 5
  validator_version: 0.5.1
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 7
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0700123
    reported_labels:
    - MONDO
    ontology_label: SMARCC1-associated developmental dysgenesis syndrome
  - term_id: UBERON:0000955
    reported_labels:
    - 'Primary organ: brain'
    ontology_label: brain
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0070734
    ontology_label: obsolete histone H3-K27 methylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: SMARCC1-associated_Developmental_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: SMARCC1-associated_Developmental_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SMARCC1-associated Developmental Dysgenesis Syndrome
- **MONDO ID:** MONDO:0700123 (if available)
- **Causal gene(s):** SMARCC1
- **OMIM:** not recorded
- **Synonyms:** SMARCC1-related BAFopathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SMARCC1-associated Developmental Dysgenesis Syndrome** covering all of the
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

# SMARCC1-associated Developmental Dysgenesis Syndrome — Comprehensive Disease Report

**MONDO ID:** MONDO:0700123 · **Causal gene:** *SMARCC1* (BAF155; HGNC:11104; OMIM gene 601732; UniProt Q92922) · **Classification:** Mendelian, autosomal-dominant BAFopathy (subclass of MONDO:0700120) · **Synonym:** SMARCC1-related BAFopathy

---

## Summary

**SMARCC1-associated Developmental Dysgenesis Syndrome is an autosomal-dominant, de-novo-dominated Mendelian neurodevelopmental disorder caused by haploinsufficient/damaging variants in *SMARCC1*, the gene encoding BAF155 — the core scaffold subunit of the BAF (mammalian SWI/SNF) ATP-dependent chromatin-remodeling complex.** The disease was defined by Singh et al. (2024) through a large genetic-association study of ventriculomegalic trios, in which rare, protein-altering de novo *SMARCC1* variants surpassed genome-wide significance. The clinical core comprises cerebral ventriculomegaly / congenital hydrocephalus, aqueductal stenosis, corpus callosum abnormalities, developmental delay, and structural cardiac defects, with variable expressivity.

Mechanistically, the disorder is not a disease of impaired cerebrospinal fluid (CSF) dynamics but of **genetic disruption of prenatal neural stem/progenitor biology**. SMARCC1/BAF155 is a scaffold subunit that controls BAF-complex stability; its loss destabilizes the complex and dysregulates the epigenetic landscape of neural progenitors — elevating the repressive histone mark H3K27me3 (via control of the demethylases UTX/JMJD3), de-repressing Wnt signaling, and shifting the balance toward excess progenitor proliferation and impaired neuronal differentiation. Downstream, pro-neurogenic transcription factors NEUROD2 and MAB21L2 are dysregulated. In vivo *Xenopus tropicalis* modeling recapitulated both aqueductal stenosis and cardiac defects and was rescued by wild-type but not patient-variant SMARCC1, establishing loss-of-function pathogenicity.

The entity is newly described and minimally curated: MONDO places it under BAFopathy and links it to *SMARCC1*, but there are **no OMIM/Orphanet/ICD cross-references and no curated HPO phenotype annotations yet**, so all phenotype terms here are literature-derived. Population frequency, penetrance, prognosis, and treatment are therefore characterized qualitatively. Management is supportive and follows general congenital-hydrocephalus practice (CSF diversion via shunt or endoscopic third ventriculostomy, developmental support). No targeted or disease-specific therapy exists.

---

## 1. Disease Information

**Overview.** SMARCC1-associated Developmental Dysgenesis Syndrome is a Mendelian BAFopathy caused by germline (overwhelmingly de novo) variants in *SMARCC1*, which encodes **BAF155**, a core scaffold subunit of the BAF/mSWI/SNF chromatin-remodeling complex. It manifests as a prenatal brain developmental disorder with variable cerebral ventriculomegaly, aqueductal stenosis, corpus callosum anomalies, developmental delay, and cardiac defects (Findings F001, F006; [PMID: 38128548](https://pubmed.ncbi.nlm.nih.gov/38128548/)).

**Key identifiers.**

| Resource | Identifier | Status |
|---|---|---|
| MONDO | MONDO:0700123 | Confirmed (name: "SMARCC1-associated developmental dysgenesis syndrome"); subclass of MONDO:0700120 (BAFopathy) |
| Causal gene | *SMARCC1* (HGNC:11104; OMIM 601732; Ensembl ENSG00000173473; chr3p21.31) | Confirmed |
| OMIM (disease/phenotype) | Not recorded | No dedicated phenotype MIM yet |
| Orphanet | Not recorded | — |
| ICD-10 / ICD-11 | Not recorded | — |
| MeSH | Not recorded | — |
| UniProt (protein) | Q92922 (SMARCC1/BAF155, 1105 aa) | Confirmed |

The MONDO term and its parentage/gene link were verified via EBI OLS4 and the Monarch Initiative API (Findings F011, F012).

**Synonyms.** SMARCC1-related BAFopathy (MONDO synonym); informally "SMARCC1 BAFopathy."

**Information source.** Derived from **aggregated disease-level resources and primary literature**, principally the defining cohort study (Singh et al. 2024) combining whole-exome sequencing of 2,697 ventriculomegalic trios with functional modeling — a research cohort rather than routine EHR. MONDO/Monarch provide ontology placement but no patient-level data.

---

## 2. Etiology

**Primary cause — genetic.** The disease is caused by rare, protein-altering, predominantly **de novo** variants in *SMARCC1*. Singh et al. identified six such variants at highly conserved residues in key functional domains, exceeding genome-wide significance in a cohort of 2,697 ventriculomegalic trios / 8,091 exomes (2016–2023) versus 1,798 control exomes (Findings F001, F006; [PMID: 38128548](https://pubmed.ncbi.nlm.nih.gov/38128548/)). An independent clinical-exome cohort separately identified de novo/loss-of-function *SMARCC1* variants and classified it as a BAFopathy gene (Finding F001; [PMID: 34906496](https://pubmed.ncbi.nlm.nih.gov/34906496/)).

**Genetic risk architecture.** The core mechanism is **haploinsufficiency**: *SMARCC1* is extremely intolerant to loss of function (gnomAD v2.1.1 pLI ≈ 1.00, observed/expected LoF = 43/147.4 = 0.29, LOEUF = 0.38, LoF Z = 7.30; missense Z = 3.01) — a constraint profile consistent with a single damaging allele being sufficient to cause disease (Finding F004). No susceptibility loci or polygenic contributors are established for this monogenic disorder; modifier genes are not yet defined.

**Environmental / protective / lifestyle factors.** None are established. As a de novo dominant developmental disorder, there are no documented environmental triggers, protective alleles, dietary or lifestyle modifiers, infectious agents, or gene-environment interactions — *not applicable / not available* for this entity (Section 5 likewise).

---

## 3. Phenotypes

Because MONDO:0700123 carries **zero curated HPO annotations** (Finding F012, Monarch API disease-to-phenotype count = 0), all phenotype terms below are **literature-derived** from the defining cohort and should be treated as provisional frequencies.

| Phenotype | Type | Suggested HPO | Onset | Notes / frequency (qualitative) |
|---|---|---|---|---|
| Cerebral ventriculomegaly | Imaging/structural sign | HP:0002119 (Ventriculomegaly) | Congenital/prenatal | Core feature; variable presence |
| Congenital hydrocephalus | Clinical sign | HP:0000238 (Hydrocephalus) | Congenital | Core; neurosurgically treated in cohort |
| Aqueductal stenosis | Structural sign | HP:0002410 (Aqueductal stenosis) | Congenital | Prominent; recapitulated in frog model |
| Corpus callosum abnormality | Structural sign | HP:0001273 (Abnormal corpus callosum) | Congenital | "Common" in cohort |
| Developmental delay | Behavioral/neurodevelopmental | HP:0001263 (Global developmental delay) | Infancy/childhood | Common |
| Structural cardiac defect | Physical/structural | HP:0001627 (Abnormal heart morphology) | Congenital | Common; recapitulated in *Xenopus* |

**Characteristics.** Onset is congenital/prenatal for structural brain and cardiac features; developmental delay emerges in infancy–childhood. Severity and progression are **variable** — the defining paper explicitly describes "variable presence of cerebral ventriculomegaly, aqueductal stenosis, developmental delay and a variety of structural brain or cardiac defects" ([PMID: 38128548](https://pubmed.ncbi.nlm.nih.gov/38128548/), Finding F006). Quantitative frequencies, QoL instruments (EQ-5D/SF-36/PROMIS), and per-phenotype severity grading are **not yet available**.

---

## 4. Genetic / Molecular Information

**Causal gene.** *SMARCC1* (BAF155), HGNC:11104, OMIM 601732, Ensembl ENSG00000173473, chr3:47,585,269–47,782,106 (3p21.31). Encodes a 1105-aa core/scaffold subunit of the BAF complex (UniProt Q92922).

**Protein domain architecture and variant localization** (Finding F011; [PMID: 33953332](https://pubmed.ncbi.nlm.nih.gov/33953332/), [PMID: 28438634](https://pubmed.ncbi.nlm.nih.gov/28438634/)):

| Domain | Residues (aa) | Function |
|---|---|---|
| N-terminal module | 28–302 | DNA contact / assembly |
| — MarR-like (putative DNA-binding) | 38–164 | DNA binding |
| — BRCT (N) | 168–211 | Protein interaction |
| — Chromo domain | 217–245 | Chromatin engagement |
| — BRCT (C) | 261–285 | Protein interaction |
| SWIRM domain | 449–546 | Binds SMARCB1/BAF47 (complex assembly) |
| SANT domain | 618–669 | Histone-tail / DNA binding |
| Disordered regions | 296–439, 745–860, 956–1028, 1041–1105 | Flexible linkers |

Pathogenic de novo variants cluster at highly conserved residues within these functional domains (Findings F006, F011).

**Variant classification and population frequency.** ClinVar contains **287** *SMARCC1* records — **68 Pathogenic, 17 Likely pathogenic**, remainder VUS/benign (Finding F010); note this count mixes germline developmental submissions with somatic/cancer classifications, so it is an upper bound on developmental-disease variants. Variant types in the developmental syndrome are **missense (de novo, conserved residues)** and predicted loss-of-function (nonsense/frameshift/splice); pathogenic alleles are effectively **absent from population databases** (gnomAD), consistent with de novo origin and strong constraint.

**Origin and functional consequence.** Germline **de novo** in the developmental syndrome; functional consequence is **loss of function / haploinsufficiency** (not gain-of-function or dominant-negative, per rescue data). A distinct **somatic** role exists in cancer (Finding F009): somatic *SMARCC1* deletion acts as a **tumor suppressor** (oral squamous cell carcinoma, [PMID: 26934577](https://pubmed.ncbi.nlm.nih.gov/26934577/); biallelic loss in malignant mesothelioma, [PMID: 24916674](https://pubmed.ncbi.nlm.nih.gov/24916674/)). >20–25% of human cancers carry mutations in SWI/SNF/BAF subunit genes ([PMID: 35158202](https://pubmed.ncbi.nlm.nih.gov/35158202/)). These somatic contexts are mechanistically and clinically separate from the germline developmental disorder.

**Modifier genes.** Not yet defined.

**Epigenetic information.** The disease mechanism is intrinsically epigenetic: BAF complexes globally control H3K27me2/3 by modulating the demethylases UTX and JMJD3 ([PMID: 26986003](https://pubmed.ncbi.nlm.nih.gov/26986003/), Finding F003). A disease-specific methylation episignature for *SMARCC1* is **not yet reported**.

**Chromosomal abnormalities.** Large 3p21.31 interstitial deletions encompassing *SMARCC1* (among many genes) have been described with developmental delay and dysmorphism ([PMID: 27385966](https://pubmed.ncbi.nlm.nih.gov/27385966/)), but phenotypes in those cases are contiguous-gene effects (e.g., *SETD2*), not the isolated *SMARCC1* syndrome.

---

## 5. Environmental Information

**Not applicable.** No environmental, lifestyle, or infectious factors are established for this monogenic de novo dominant disorder. No toxins, radiation, occupational exposures, dietary factors, or pathogens are implicated.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **de novo damaging/loss-of-function variant in *SMARCC1*** (missense at conserved domain residues, or LoF) arises in the germline → **reduces functional BAF155 (haploinsufficiency)** (demonstrated: genetic constraint pLI≈1, de novo enrichment; F004, F006).
2. Reduced BAF155 scaffold → **destabilizes the BAF (mSWI/SNF) chromatin-remodeling complex**, because BAF155 regulates complex stability and assembly (demonstrated in mouse/in vitro; F003; [PMID: 31020615](https://pubmed.ncbi.nlm.nih.gov/31020615/)).
3. BAF dysfunction → **loss of BAF-mediated control over H3K27 demethylases UTX/JMJD3 → global increase in repressive H3K27me2/3** (demonstrated in mouse forebrain; F003; [PMID: 26986003](https://pubmed.ncbi.nlm.nih.gov/26986003/)).
4. Altered histone-methylation balance (↑H3K27me3 on neuronal-differentiation genes; ↑H3K4me2 on proliferation genes) → **de-repression of Wnt signaling** (demonstrated in mouse late corticogenesis; F005; [PMID: 29779894](https://pubmed.ncbi.nlm.nih.gov/29779894/)).
5. Wnt de-repression → **increased proliferation of neuroepithelial-like neural stem cells and impaired neuronal differentiation** (demonstrated; F005).
6. Imbalanced progenitor proliferation/differentiation → **dysregulation of midgestational neurogenesis transcription factors NEUROD2 and MAB21L2** (demonstrated across human fetal brain and *Xenopus*; F007; [PMID: 38128548](https://pubmed.ncbi.nlm.nih.gov/38128548/)).
7. Disrupted neuro-gliogenesis → **structural brain dysgenesis: aqueductal stenosis, cerebral ventriculomegaly/hydrocephalus, corpus callosum anomalies** — i.e., the primary lesion is developmental, *not* impaired CSF dynamics (inferred for human from model + cohort transcriptomics; supported by F002; [PMID: 33077954](https://pubmed.ncbi.nlm.nih.gov/33077954/)).
8. **Branch — cardiac:** BAF dysfunction in cardiac progenitors → **structural cardiac defects** (demonstrated by *Xenopus* knockdown recapitulation and rescue; F007).
9. Brain dysgenesis + hydrocephalus → **developmental delay and the clinical syndrome** (clinical observation; F006).

```
 SMARCC1 de novo LoF/missense
          │ (haploinsufficiency)
          ▼
 BAF/mSWI-SNF complex destabilized
          │
          ▼
 ↑H3K27me3 (UTX/JMJD3 dysregulation)
          │
          ▼
 Wnt signaling de-repressed
          │
     ┌────┴───────────────┐
     ▼                     ▼
 ↑NSC proliferation   NEUROD2/MAB21L2
 ↓neuronal diff.      dysregulated
     │                     │
     └────────┬────────────┘
              ▼
  Disrupted neuro-gliogenesis ──► aqueductal stenosis,
  (NOT impaired CSF dynamics)      ventriculomegaly, callosal anomaly
              │
              ├──► (branch) cardiac progenitor defect ─► structural cardiac defects
              ▼
  Developmental delay + clinical syndrome
```

**Molecular pathways:** Wnt signaling (de-repressed; KEGG hsa04310); chromatin remodeling / histone methylation (H3K27me2/3; H3K4me2). **Cellular processes:** neural stem cell proliferation (GO:0050767 regulation of neurogenesis), neuronal differentiation (GO:0030182), chromatin remodeling (GO:0006338), histone H3-K27 methylation (GO:0070734). **Protein dysfunction:** loss of scaffold function → complex instability (not aggregation). **Cell types:** neural stem/progenitor cells (CL:0000047 neuronal stem cell; CL:0000031 neuroblast; CL:0000681 radial glial cell), cardiac progenitors. **Subcellular:** nucleus / nuclear chromatin (GO:0000785 chromatin; GO:0016514 SWI/SNF complex; GO:0071564 npBAF complex). **Multi-omics / functional genomics:** cross-species transcriptomics (human fetal brain RNA-seq + *Xenopus*) converging on shared neurogenesis genes (F007); *Xenopus* knockdown-rescue as the in vivo functional assay (F007).

Upstream nodes = SMARCC1 loss → BAF instability → histone-methylation shift; downstream = Wnt/progenitor imbalance → transcription-factor dysregulation → structural malformation.

---

## 7. Anatomical Structures Affected

- **Primary organ: brain** (UBERON:0000955), especially **cerebral ventricles** (UBERON:0002285 lateral ventricle), **cerebral aqueduct** (UBERON:0002289; aqueductal stenosis), **corpus callosum** (UBERON:0002336), neocortex and hippocampus (implicated by BAF-loss cortical models, F005).
- **Secondary / branch organ: heart** (UBERON:0000948) — structural cardiac defects.
- **Body systems:** central nervous system (developmental) and cardiovascular system.
- **Tissue/cell level:** neuroepithelium / neural stem & progenitor cells (CL:0000047, CL:0000681 radial glia, CL:0000031 neuroblast); cardiac progenitor cells.
- **Subcellular:** nucleus / chromatin (GO:0000785); BAF/SWI-SNF complex (GO:0016514, GO:0071564).
- **Localization / lateralization:** midline and bilateral CNS structures; ventriculomegaly typically bilateral. Precise lateralization not systematically reported.

---

## 8. Temporal Development

- **Onset:** congenital/prenatal for brain and cardiac malformations (detectable as fetal/neonatal ventriculomegaly); developmental delay apparent in infancy–childhood. Onset pattern is **chronic/congenital**, arising during **midgestational neurogenesis** — the critical developmental window (F002, F007).
- **Progression:** structural malformations are fixed at birth; hydrocephalus may require intervention. Developmental delay is generally **stable to slowly evolving** rather than neurodegenerative. Formal natural-history/longitudinal data are **not available**.
- **Critical period:** fetal neuro-gliogenesis (midgestation) is the window of vulnerability and the only plausible window for mechanistic intervention — likely inaccessible postnatally.
- **Remission:** none intrinsic; hydrocephalus is managed surgically (symptomatic, not curative).

---

## 9. Inheritance and Population

- **Inheritance pattern:** autosomal dominant, overwhelmingly **de novo** (F001, F006).
- **Penetrance / expressivity:** expressivity is explicitly **variable**; penetrance not precisely quantified given small cohort.
- **Anticipation / mosaicism / founder effects / consanguinity:** not reported / not applicable (de novo dominant, not a repeat-expansion or recessive disorder). Germline/gonadal mosaicism is a theoretical source of recurrence risk.
- **Carrier frequency:** not applicable (de novo dominant); pathogenic alleles essentially absent from gnomAD.
- **Epidemiology:** prevalence and incidence are **not established** — the syndrome is newly defined from a research cohort and carries no Orphanet/registry prevalence figure. It represents a rare, genetically defined subset within the broader congenital-hydrocephalus and BAFopathy populations.
- **Demographics / geography / sex ratio / age distribution:** no population-specific enrichment, geographic clustering, or sex bias established; affected individuals are identified in the prenatal/pediatric period.

For context, the broader Coffin-Siris/Nicolaides-Baraitser BAFopathy family may account for ~1% of intellectual disability ([PMID: 25249037](https://pubmed.ncbi.nlm.nih.gov/25249037/), F008) — but *SMARCC1* disease is a distinct, much rarer entity within that family.

---

## 10. Diagnostics

- **Genetic testing is the definitive diagnostic.** Trio **whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)** identifying a de novo damaging *SMARCC1* variant is the basis of diagnosis (the entity was defined by trio WES; F001, F006). Single-gene testing and BAFopathy/congenital-hydrocephalus **gene panels** including *SMARCC1* are appropriate. **Chromosomal microarray** may detect 3p21.31 deletions but typically as contiguous-gene events ([PMID: 27385966](https://pubmed.ncbi.nlm.nih.gov/27385966/)).
- **Variant interpretation:** ACMG/AMP classification against ClinVar (68 P / 17 LP records; F010); de novo occurrence (PS2), absence from gnomAD (PM2), and conserved functional-domain location support pathogenicity.
- **Imaging:** fetal/neonatal cranial ultrasound and brain **MRI** demonstrate ventriculomegaly, aqueductal stenosis, and callosal anomalies; **echocardiography** for cardiac defects.
- **Laboratory biomarkers / metabolomics / proteomics / liquid biopsy:** no specific biochemical biomarker exists; diagnosis is molecular/radiological.
- **Clinical criteria:** no formal consensus criteria yet (newly defined).
- **Differential diagnosis:** other BAFopathies — Coffin-Siris syndrome (*ARID1B, ARID1A, SMARCB1, SMARCA4, SMARCA2, SMARCE1, ARID2*) and Nicolaides-Baraitser syndrome — which share BAF-subunit etiology but are distinguished by coarse facial features, sparse scalp hair, hypertrichosis, and fifth-digit nail/phalanx hypoplasia rather than the prominent **congenital hydrocephalus/aqueductal stenosis** of SMARCC1 disease (F008; [PMID: 34906496](https://pubmed.ncbi.nlm.nih.gov/34906496/), [PMID: 35813374](https://pubmed.ncbi.nlm.nih.gov/35813374/), [PMID: 27264197](https://pubmed.ncbi.nlm.nih.gov/27264197/)). Also consider other monogenic congenital-hydrocephalus genes (e.g., *TRIM71*, *CCDC88C*, *MPDZ*; [PMID: 29983323](https://pubmed.ncbi.nlm.nih.gov/29983323/)).
- **Screening:** no population or newborn screening exists; **cascade testing** is generally uninformative given de novo origin.

---

## 11. Outcome / Prognosis

Prognostic data specific to SMARCC1 disease are **limited/not formally reported**. Outcome is driven by the severity of hydrocephalus and associated brain/cardiac malformations and by developmental delay. By analogy to genetic congenital hydrocephalus, morbidity relates to neurodevelopmental impairment and shunt-dependence complications (pediatric VP-shunt 30-day failure ~13.8%; [PMID: 42829386](https://pubmed.ncbi.nlm.nih.gov/42829386/)). **Survival, mortality, 5/10-year outcomes, QoL measures, and validated prognostic biomarkers are not available** for this specific entity. Disease course is chronic/lifelong with stable (non-degenerative) neurodevelopmental impairment.

---

## 12. Treatment

**No disease-specific or targeted therapy exists.** Management is **supportive and symptomatic**, following general congenital-hydrocephalus and neurodevelopmental care:

- **Neurosurgical CSF diversion** for hydrocephalus — ventriculoperitoneal shunting (NCIT: Ventriculoperitoneal Shunt) or **endoscopic third ventriculostomy (ETV)**, particularly for obstructive/aqueductal-stenosis physiology (supporting surgical literature: [PMID: 42886343](https://pubmed.ncbi.nlm.nih.gov/42886343/), [PMID: 42829386](https://pubmed.ncbi.nlm.nih.gov/42829386/)).
- **Cardiac management** for structural defects (cardiology/surgical as indicated).
- **Developmental support** — physical, occupational, and speech therapy; early intervention (NCIT: Rehabilitation Therapy).
- **Pharmacotherapy / pharmacogenomics / gene / cell / RNA / targeted / immunotherapy:** none established or applicable.
- **Experimental:** no disease-specific trials (no NCT identifiers) target *SMARCC1* disease. Mechanistically, the epigenetic link (↑H3K27me3 via EZH2/demethylase axis) is of conceptual interest — EZH2 inhibition (GSK126) rescued a *Baf155*-CKO myeloid phenotype in mice ([PMID: 33207205](https://pubmed.ncbi.nlm.nih.gov/33207205/)) — but this is **not** a validated therapy and the prenatal critical window likely limits translational feasibility.

---

## 13. Prevention

- **Primary prevention:** none available (de novo mutation; not preventable by risk-factor modification or immunization).
- **Secondary prevention:** prenatal detection of ventriculomegaly on ultrasound/MRI can prompt genetic evaluation and delivery/neurosurgical planning.
- **Genetic counseling:** recurrence risk for parents of a child with a confirmed de novo variant is low but non-zero due to possible **gonadal mosaicism**; prenatal/preimplantation testing is feasible if a familial variant is identified. Counseling per NSGC/ACMG principles is recommended.
- **Public health / behavioral / environmental / prophylaxis:** not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologs:** *Smarcc1* is conserved across mammals (mouse *Smarcc1*), zebrafish (*smarcc1a/b*), *Xenopus tropicalis* (*smarcc1*), and other vertebrates. BAF-complex function is deeply evolutionarily conserved.
- **Natural disease in other species:** no naturally occurring companion-animal or wildlife disease specifically attributed to *SMARCC1* is catalogued (no established OMIA entry). Veterinary relevance is currently limited to experimental models.
- **Comparative biology:** BAF/SMARCC1 roles in embryonic development, lineage specification, and neural progenitor regulation are conserved from frog to human ([PMID: 26952987](https://pubmed.ncbi.nlm.nih.gov/26952987/), [PMID: 29779894](https://pubmed.ncbi.nlm.nih.gov/29779894/)); a zebrafish study linked BBS6 to Smarcc1a in congenital heart disease ([PMID: 28753627](https://pubmed.ncbi.nlm.nih.gov/28753627/)).
- **Transmission / zoonosis:** not applicable (genetic disorder).

---

## 15. Model Organisms

| Model | Type | Manipulation | Phenotype recapitulation | Reference |
|---|---|---|---|---|
| *Xenopus tropicalis* | Vertebrate (amphibian) | *smarcc1* knockdown; WT vs variant rescue | **Recapitulated aqueductal stenosis AND cardiac defects**; rescued by WT but not patient-variant SMARCC1; shared NEUROD2/MAB21L2 dysregulation with human fetal brain | [PMID: 38128548](https://pubmed.ncbi.nlm.nih.gov/38128548/) (F007) |
| Mouse (*Mus musculus*) | Mammalian | *Baf155/Baf170* conditional KO (forebrain); *Baf155* CKO | ↑H3K27me3, impaired forebrain development; de-repressed Wnt, ↑NSC proliferation, impaired neuronal differentiation | [PMID: 26986003](https://pubmed.ncbi.nlm.nih.gov/26986003/), [PMID: 29779894](https://pubmed.ncbi.nlm.nih.gov/29779894/) (F003, F005) |
| Mouse blastocyst/embryo | Mammalian | BAF155 up/down-regulation | Lineage-specification defects (pluripotency-marker dysregulation) | [PMID: 26952987](https://pubmed.ncbi.nlm.nih.gov/26952987/) |
| Zebrafish (*Danio rerio*) | Vertebrate | *smarcc1a*/*bbs6* manipulation | Congenital-heart-disease-relevant transcriptional changes | [PMID: 28753627](https://pubmed.ncbi.nlm.nih.gov/28753627/) |

**Strengths:** The *Xenopus* model is the strongest disease-specific validation — it reproduces both the neural (aqueductal stenosis) and cardiac arms of the human phenotype and provides variant-level loss-of-function proof via rescue. Mouse BAF155-loss models illuminate the upstream epigenetic (H3K27me3/Wnt) mechanism. **Limitations:** mouse studies use conditional/compound knockouts rather than the human heterozygous de novo state; no reported germline heterozygous *Smarcc1* mouse that fully mirrors the human syndrome; iPSC/organoid models of patient variants are not yet published.

---

## Mechanistic Model / Interpretation

The evidence converges on a single coherent model: **SMARCC1 disease is a chromatinopathy of fetal neurogenesis.** A de novo hit reduces functional BAF155 below the dose the developing brain tolerates (haploinsufficiency, pLI≈1). Because BAF155 is the scaffold that holds the BAF complex together, its loss has an outsized, complex-wide effect — explaining why a single damaging allele is pathogenic. The destabilized complex loses grip on the H3K27-methylation machinery, tipping progenitors toward Wnt-driven over-proliferation and away from neuronal differentiation, and derailing the NEUROD2/MAB21L2 neurogenic program during the narrow midgestational window. The resulting malformed neural tube/ventricular system manifests as aqueductal stenosis and ventriculomegaly, with a parallel branch in cardiac progenitors producing heart defects. Crucially, the hydrocephalus is a **downstream developmental consequence, not a primary plumbing failure** — reframing a "neurosurgical" phenotype as a chromatin-remodeling disorder (F002).

This model cleanly separates the **germline developmental** context (haploinsufficiency → malformation) from the **somatic oncogenic** context (SMARCC1 as a tumor suppressor whose loss drives cancer), unifying them under the theme that SMARCC1 dosage is critical across distinct cellular programs.

---

## Evidence Base

| PMID | Role | How it supports the findings |
|---|---|---|
| [38128548](https://pubmed.ncbi.nlm.nih.gov/38128548/) | **Defining study** | Names the syndrome; genome-wide-significant de novo *SMARCC1* variants in 2,697 trios; *Xenopus* rescue; NEUROD2/MAB21L2 (F001, F006, F007) |
| [34906496](https://pubmed.ncbi.nlm.nih.gov/34906496/) | Independent cohort | De novo/LoF *SMARCC1* in clinical-exome BAFopathy cohort; genotype-first constraint approach (F001, F004, F008) |
| [33077954](https://pubmed.ncbi.nlm.nih.gov/33077954/) | Mechanistic framing | Genetic disruption of neuro-gliogenesis, not CSF dynamics, is the primary CH pathomechanism (F002) |
| [31020615](https://pubmed.ncbi.nlm.nih.gov/31020615/) | Protein function | BAF155 as core/scaffold regulating BAF stability (F003) |
| [26986003](https://pubmed.ncbi.nlm.nih.gov/26986003/) | Epigenetic mechanism | BAF controls H3K27me2/3 via UTX/JMJD3; forebrain development (F003, F005) |
| [29779894](https://pubmed.ncbi.nlm.nih.gov/29779894/) | Mechanism | BAF loss → Wnt de-repression → ↑NSC proliferation, impaired differentiation (F005) |
| [33953332](https://pubmed.ncbi.nlm.nih.gov/33953332/) | Structure | N-terminal MarR/chromo/BRCT module architecture (F011) |
| [28438634](https://pubmed.ncbi.nlm.nih.gov/28438634/) | Structure | SWIRM domain binds BAF47/SMARCB1 (F011) |
| [26934577](https://pubmed.ncbi.nlm.nih.gov/26934577/) / [24916674](https://pubmed.ncbi.nlm.nih.gov/24916674/) / [35158202](https://pubmed.ncbi.nlm.nih.gov/35158202/) | Somatic contrast | SMARCC1 as tumor suppressor; SWI/SNF in >20% cancers (F009) |
| [25249037](https://pubmed.ncbi.nlm.nih.gov/25249037/) | Epidemiologic context | BAFopathy/CSS ~1% of intellectual disability (F008) |

Constraint metrics (pLI, LOEUF) were retrieved directly from the gnomAD GraphQL API; ClinVar counts from NCBI E-utilities; MONDO parentage/gene link from the Monarch Initiative API and EBI OLS4.

---

## Limitations and Knowledge Gaps

1. **Newly defined, minimally curated entity:** no OMIM phenotype MIM, Orphanet, ICD, or MeSH code; **zero curated HPO annotations** (F012). All phenotype frequencies are literature-derived from a single defining cohort.
2. **Small patient numbers:** six de novo variants underpin the definition; penetrance, expressivity ranges, prevalence/incidence, sex ratio, and natural history are not quantified.
3. **Prognosis and treatment:** no disease-specific outcome data, QoL measures, prognostic biomarkers, or targeted therapies; management is extrapolated from general congenital-hydrocephalus practice.
4. **Mechanistic inferences:** the human causal chain from histone-methylation shift → Wnt → malformation is strongly supported in mouse/frog but partly **inferred** for human; the EZH2-inhibition rescue is from a non-neural mouse model and is not a validated therapy.
5. **ClinVar counts** mix germline and somatic submissions, inflating the apparent germline pathogenic-variant pool.
6. No patient-derived iPSC/organoid models or human methylation episignature yet.

---

## Proposed Follow-up Experiments / Actions

1. **Curate HPO annotations** for MONDO:0700123 from the Singh 2024 cohort and future cases, with explicit frequencies, to enable automated phenotype-driven diagnosis.
2. **Establish a patient registry / GeneMatcher recruitment** to quantify prevalence, penetrance, expressivity, sex ratio, and natural history.
3. **Patient-specific iPSC-derived cerebral organoids** carrying the de novo variants to test, in a human system, the predicted H3K27me3 increase, Wnt de-repression, and NEUROD2/MAB21L2 loss, and to screen candidate modulators (e.g., EZH2 inhibitors) for developmental-window rescue.
4. **Generate a heterozygous germline *Smarcc1* mouse** matching the human dosage state to test faithful recapitulation and therapeutic windows.
5. **Define a DNA-methylation episignature** for clinical variant classification (reclassifying VUS).
6. **Cross-reference OMIM/Orphanet/ICD** submissions to formalize identifiers and align the knowledge base.
7. **Structure-function mapping** of each pathogenic variant onto Q92922 domains (MarR/chromo/BRCT module, SWIRM) to predict genotype–phenotype correlation and assembly impact.

---

*Evidence source legend:* human clinical/genetic (38128548, 34906496, 33077954, 29983323, 27385966, 25249037); model organism (38128548 *Xenopus*; 26986003, 29779894, 26952987, 33207205 mouse; 28753627 zebrafish); in vitro/structural (31020615, 33953332, 28438634, 35158202); somatic/computational constraint (26934577, 24916674, gnomAD/ClinVar APIs).


## Artifacts

- [OpenScientist final report](SMARCC1-associated_Developmental_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](SMARCC1-associated_Developmental_Dysgenesis_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 21 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 12 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700123` (4 mentions) - the report calls it "MONDO"; MONDO calls it **SMARCC1-associated developmental dysgenesis syndrome**
- `UBERON:0000955` (1 mention) - the report calls it "Primary organ: brain"; UBERON calls it **brain**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070734` (obsolete histone H3-K27 methylation) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001273` (1 mention) - the report calls it "Abnormal corpus callosum"; HP calls it **Abnormal corpus callosum morphology**, and lists "Abnormal corpus callosum" among its other names
- `GO:0000785` (2 mentions) - the report calls it "Subcellular:** nucleus / chromatin"; GO calls it **chromatin**, and lists "nuclear chromatin" among its other names
- `UBERON:0000948` (1 mention) - the report calls it "Secondary / branch organ: heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names