---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-05T17:58:32.726572'
end_time: '2026-11-05T18:15:56.751133'
duration_seconds: 1044.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Melanoma-Pancreatic Cancer Syndrome
  mondo_id: MONDO:0011713
  category: Mendelian
  causal_genes: CDKN2A
  omim_id: OMIM:606719
  synonyms: not recorded
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
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 29
  validator_version: 0.5.1
term_validation:
  total_terms: 24
  verified: 21
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 0
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0011713
    reported_labels:
    - MONDO
    ontology_label: melanoma-pancreatic cancer syndrome
  - term_id: HP:0012056
    reported_labels:
    - Neoplasm
    ontology_label: Cutaneous melanoma
  - term_id: HP:0003764
    reported_labels:
    - Physical sign
    ontology_label: Nevus
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0007050
    ontology_label: GO_0007050
    replaced_by: GO:0051726
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
  path: Melanoma-Pancreatic_Cancer_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Melanoma-Pancreatic_Cancer_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Melanoma-Pancreatic Cancer Syndrome
- **MONDO ID:** MONDO:0011713 (if available)
- **Causal gene(s):** CDKN2A
- **OMIM:** OMIM:606719
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Melanoma-Pancreatic Cancer Syndrome** covering all of the
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

# Melanoma–Pancreatic Cancer Syndrome (MONDO:0011713, OMIM 606719): A Comprehensive Disease Characterization

> **Causal gene: `CDKN2A` (9p21.3), encoding the dual tumor suppressors p16INK4a and p14ARF.** This report characterizes the autosomal dominant hereditary cancer-predisposition syndrome catalogued as OMIM 606719 / MONDO:0011713, in which germline loss-of-function variants in *CDKN2A* predispose to cutaneous melanoma and pancreatic ductal adenocarcinoma (PDAC). It is a specific presentation within the Familial Atypical Multiple Mole Melanoma–Pancreatic Cancer (FAMMM-PC) spectrum. Although the name references melanoma and pancreatic cancer, and the disease is sometimes conflated with FAMMM (OMIM #155601) or CDK4-driven melanoma (OMIM #609048), the molecular lesion of this specific entity is in *CDKN2A* — not CDK4, BRCA2, or PALB2 — and all identifiers above point to the *CDKN2A*-driven entity.

**MONDO:** MONDO:0011713 · **OMIM:** 606719 · **Causal gene:** CDKN2A (9p21.3) · **Category:** Mendelian, autosomal dominant · **Report date:** 2026-11-05

---

## Summary

Melanoma–Pancreatic Cancer Syndrome is an autosomal dominant hereditary cancer predisposition syndrome caused by germline loss-of-function variants in **CDKN2A** on chromosome 9p21.3. This locus is unusual in that it encodes **two distinct tumor suppressor proteins from overlapping reading frames**: p16INK4a (which inhibits CDK4/CDK6 to maintain RB-mediated G1 cell-cycle arrest) and p14ARF (which stabilizes p53 by inhibiting MDM2). Germline inactivation of CDKN2A therefore removes a "pre-installed" driver lesion that both melanocytes and pancreatic ductal epithelium would otherwise need to acquire somatically, lowering the threshold for malignant transformation. The clinical hallmark is the co-occurrence, within families, of **cutaneous melanoma** (often early-onset, multiple primaries, with clinically atypical nevi) and **pancreatic ductal adenocarcinoma**, frequently accompanied by a broader spectrum of tobacco- and UV-potentiated cancers.

Penetrance is high but strongly **ascertainment- and environment-dependent**. In the Dutch founder cohort (p16-Leiden, c.225_243del), carriers face roughly a **70% lifetime melanoma risk and a 15–20% lifetime pancreatic cancer risk**. Population-based estimates of melanoma penetrance are considerably lower (~28% by age 80) than those derived from dense multiple-case kindreds (58–91%), and penetrance rises with cumulative UV exposure across geographic latitude. Tobacco smoking dramatically amplifies the risk of pancreatic, respiratory, and upper-digestive cancers, a clear gene–environment interaction, while MC1R variants act as cosegregating genetic modifiers of melanoma risk.

Management is **cancer-specific rather than syndrome-specific**: there is no therapy for the germline defect itself. Melanoma is managed by surveillance (total-body photography, dermoscopy, sequential digital dermoscopic imaging), wide local excision, and — for advanced disease — modern immune checkpoint inhibitors and BRAF/MEK-targeted therapy. For pancreatic cancer, surgical resection of screen-detected early-stage tumors is the only route to cure; annual MRI/MRCP ± endoscopic ultrasound surveillance of carriers (endorsed by the International Cancer of the Pancreas Screening [CAPS] Consortium) improves resectability, long-term cure, and is cost-effective. Smoking cessation and sun protection are the cornerstones of primary prevention, and genetic counseling with cascade testing is central to family management.

---

## Key Findings

### Finding 1 — CDKN2A germline loss-of-function is the cause (F001)

Germline pathogenic variants in **CDKN2A** (9p21), encoding two tumor suppressors (**p16INK4a** and **p14ARF**) from alternative reading frames, cause this autosomal dominant syndrome of melanoma plus pancreatic ductal adenocarcinoma. Approximately **30–40% of dense FAMMM/PCMS families** carry detectable CDKN2A mutations. p16INK4a inhibits CDK4/CDK6 to maintain RB-mediated G1 arrest; p14ARF stabilizes p53 via MDM2 inhibition — so a single locus guards both of the two canonical tumor-suppressor axes (RB and p53).

- [PMID: 32941720](https://pubmed.ncbi.nlm.nih.gov/32941720/): *"About 30% of PCMS cases carry mutations in CDKN2A. This gene encodes several protein isoforms, one of which, known as p16, regulates the cell-cycle by interacting with CDK4/CDK6 kinases."*
- [PMID: 14871223](https://pubmed.ncbi.nlm.nih.gov/14871223/): *"germline mutations in the INK4a antioncogene encoding p16 protein were found on average in approximately 40% of the FAMMM syndrome."*

### Finding 2 — p16-Leiden penetrance and the value of pancreatic surveillance (F002)

The Dutch founder mutation **c.225_243del** (a 19-bp deletion in exon 2, "**p16-Leiden**") confers roughly a **70% lifetime melanoma risk** and a **15–20% lifetime pancreatic cancer risk**. In a surveillance cohort of 347 carriers undergoing annual MRI ± EUS, PDAC was detected in 8.9%, was resectable in 71%, and long-term cure among resected patients was estimated at **47.1%**. Modeling showed surveillance reduced PDAC mortality by 12.1% and added 2.10 years of life expectancy at ~€14,000/QALY — i.e., cost-effective.

- [PMID: 31203567](https://pubmed.ncbi.nlm.nih.gov/31203567/): *"Carriers of pathogenic variants in CDKN2A have a 70% life-time risk of developing melanoma and 15-20% risk of developing pancreatic cancer (PC)."*
- [PMID: 36785917](https://pubmed.ncbi.nlm.nih.gov/36785917/): *"PDAC was detected in 31 patients (8.9%) and the tumor could be resected in 22 patients (71.0%). Long-term cure among patients with resected PDAC was estimated at 47.1%."*

### Finding 3 — Mouse models confirm the mechanism (F003)

In vivo genetics strongly supports the human mechanism. Ink4a-deficient mice are cancer-prone; melanocyte-specific activated **H-rasG12V on an ink4a-null background** produces spontaneous cutaneous melanoma with short latency and high penetrance, with loss of heterozygosity (LOH) at the wild-type ink4a allele. Tyr::NRAS(Q61K);Cdkn2a-/- mice develop metastasizing melanoma. Knock-in **Cdk4R24C** mice (the INK4-insensitive CDK4 allele that mirrors the human hereditary-melanoma CDK4 mutation) develop tumors with near-complete penetrance. Both the Ink4a/pRB and Arf/p53 arms contribute.

- [PMID: 9353252](https://pubmed.ncbi.nlm.nih.gov/9353252/): *"mice with melanocyte-specific expression of activated H-rasG12V on an ink4a-deficient background develop spontaneous cutaneous melanomas after a short latency and with high penetrance."*
- [PMID: 11726500](https://pubmed.ncbi.nlm.nih.gov/11726500/): *"This mutation (replacement of Arg24 by Cys)... renders Cdk4 insensitive to INK4 inhibitors... homozygous Cdk4(R24C/R24C) mutant mice develop multiple tumors with almost complete penetrance."* (Note: CDK4 R24C is the alternative hereditary-melanoma gene, which phenocopies p16 loss.)

### Finding 4 — Broad extra-melanoma cancer spectrum and gene–environment interaction with tobacco (F004)

In a prospective Swedish cohort of p.Arg112dup (p16-113insArg) carriers, the relative risk versus controls was **43.8** (95% CI 13.8–139.0) for pancreatic cancer, **17.1** (6.3–46.5) for upper-digestive-tract cancer, **15.6** (5.4–46.0) for respiratory cancer, and **5.0** (3.7–7.3) for non-melanoma cancers overall. Critically, **ever-smoking carriers** versus never-smoking carriers had an odds ratio of **9.3** (95% CI 1.9–44.7) for pancreatic/respiratory/upper-digestive cancers — a clear gene–environment interaction. Head-and-neck/oral SCC is also over-represented. MC1R variants cosegregate as melanoma modifiers, and UV exposure modulates penetrance across latitude.

- [PMID: 24935963](https://pubmed.ncbi.nlm.nih.gov/24935963/): *"In carriers prospective RR for non-melanoma cancers was 5.0 (95% CI 3.7 to 7.3), for pancreatic cancer 43.8 (95% CI 13.8 to 139.0), for cancers in upper digestive tissues 17.1 (95% CI 6.3 to 46.5), and in respiratory tissues 15.6 (5.4 to 46.0)."*
- [PMID: 24935963](https://pubmed.ncbi.nlm.nih.gov/24935963/): *"In ever-smoking carriers compared with never-smoking carriers, the odds ratio (OR) of cancers in pancreas, respiratory or upper digestive tissues was 9.3 (95% CI 1.9 to 44.7)."*
- [PMID: 16462187](https://pubmed.ncbi.nlm.nih.gov/16462187/): *"Certain variants in a low-penetrance gene, MC1R... act as a genetic modifier when cosegregating with a deleterious p16 gene. The penetrance of these melanoma-predisposing genes is largely influenced by ultraviolet exposure across geographic latitude."*

### Finding 5 — Cutaneous phenotype: atypical nevi, early-onset and multiple primary melanomas (F005)

CDKN2A-positive patients develop melanoma **earlier** and are prone to **multiple primary melanomas**. In Swedish carriers, melanoma occurred only in mutation carriers (median age 36 years) and correlated with clinically atypical nevi (CAN, P=0.007) and red hair/MC1R, but carriers did **not** uniformly meet full atypical-mole-syndrome criteria (median nevus count 24). Atypical mole syndrome raises melanoma risk but cannot reliably predict germline mutation status.

- [PMID: 20526219](https://pubmed.ncbi.nlm.nih.gov/20526219/): *"A positive mutation status (CDKN2A) was correlated to one or more CAN (P=0.007) but neither to blue eyes, red hair colour, heavy freckling nor high number of nevi."*
- [PMID: 16462187](https://pubmed.ncbi.nlm.nih.gov/16462187/): *"Familial melanoma patients develop melanomas earlier and are prone to developing multiple primary melanomas."*

**Suggested HPO terms:** Cutaneous melanoma (HP:0012056), Dysplastic nevus (HP:0003764), Pancreatic neoplasm (HP:0002894), Neoplasm of the skin (HP:0008069).

### Finding 6 — Treatment is tumor-specific (F006)

There is no therapy for the germline syndrome itself; management targets individual tumors. **Melanoma:** wide local excision for localized disease; for advanced/resectable stage III–IV, immune checkpoint inhibitors (anti-PD-1 nivolumab/pembrolizumab, anti-CTLA-4 ipilimumab, anti-LAG-3 relatlimab) and BRAF/MEK inhibitors (for BRAF-V600 tumors). Neoadjuvant ipilimumab + nivolumab improved event-free survival versus adjuvant nivolumab in the NADINA trial. **Pancreatic cancer:** surgical resection of screen-detected early PDAC is the only route to cure (~47% long-term cure for resected screen-detected tumors). CDKN2A loss produces CDK4/6 dependence, providing a mechanistic rationale for CDK4/6 inhibitors (investigational in CDKN2A-null tumors).

- [PMID: 42794996](https://pubmed.ncbi.nlm.nih.gov/42794996/): *"In resectable macroscopic stage III melanoma, neoadjuvant ipilimumab plus nivolumab with response-driven postoperative management improved event-free survival versus adjuvant nivolumab in NADINA."*

**Suggested NCIT terms:** Pembrolizumab (C106432), Nivolumab (C68924), Ipilimumab (C2654), Dabrafenib (C82386), Trametinib (C77908), Pancreaticoduodenectomy (C51782).

### Finding 7 — Molecular mechanism: p16 destabilization / loss of CDK4 binding → RB hyperphosphorylation → unchecked G1/S (F007)

Molecular dynamics/docking of melanoma-prone p16 mutants shows that many mutations (e.g., G23D, P114S, A60V) **abolish CDK4 binding** while others (R24Q, G67R) partially impair it, disrupting a positive electrostatic patch on the binding surface and lowering complex stability — often without gross structural change. Tumor-derived mutations (P81L, V126D) **destabilize the N-terminal half** of p16, which contains CDK-binding residues. The CDK4 R24C mutation renders CDK4 insensitive to INK4 inhibition, phenocopying p16 loss.

- [PMID: 39821174](https://pubmed.ncbi.nlm.nih.gov/39821174/): *"Despite no significant structural changes in p16 due to mutation, the binding affinity was found to be affected... specific mutations, such as G23D, P114S, and A60V resulted in loss of binding to CDK4."*
- [PMID: 12009890](https://pubmed.ncbi.nlm.nih.gov/12009890/): *"the N-terminal half of p16 is significantly more sensitive to proteolysis in both tumor-derived mutant proteins than in the wild type, suggesting that this region is particularly unstable."*

### Finding 8 — CAPS Consortium endorses pancreatic surveillance for CDKN2A carriers (F008)

The International Cancer of the Pancreas Screening (CAPS) Consortium formally lists **p16 (CDKN2A) carriers with ≥1 affected first-degree relative** as candidates for pancreatic surveillance. The goal is to detect and treat **T1N0M0** margin-negative PDAC and high-grade dysplastic precursors (PanIN/IPMN) using **EUS and/or MRI/MRCP** rather than CT/ERCP. The 2020 update reached consensus on 55 statements; surveillance should start no earlier than age 50 (or 10 years before the youngest affected relative), with germline-mutation carriers potentially starting earlier, in expert multidisciplinary centers. CAPS cyst-management criteria are moderately specific (85%) but insufficiently sensitive (60%) for advanced neoplasia.

- [PMID: 23135763](https://pubmed.ncbi.nlm.nih.gov/23135763/): *"the following were candidates for screening: first-degree relatives (FDRs) of patients with PC from a familial PC kindred with at least two affected FDRs; patients with Peutz-Jeghers syndrome; and p16, BRCA2 and hereditary non-polyposis colorectal cancer (HNPCC) mutation carriers with ≥ 1 affected FDR."*
- [PMID: 31672839](https://pubmed.ncbi.nlm.nih.gov/31672839/): *"surveillance should start no earlier than age 50 or 10 years earlier than the youngest relative with pancreatic cancer."*

### Finding 9 — Melanoma penetrance is ascertainment-dependent (F009)

In a **population-based** kin-cohort sample, melanoma risk in CDKN2A carriers was **14%** (95% CI 8–22) by age 50, **24%** (15–34) by age 70, and **28%** (18–40) by age 80 — markedly lower than estimates from high-density multiple-case families (**58% in Europe to 91% in Australia** by age 80). This gradient reflects both ascertainment bias and cumulative UV exposure by latitude.

- [PMID: 16234564](https://pubmed.ncbi.nlm.nih.gov/16234564/): *"The risk of melanoma in CDKN2A mutation carriers was approximately 14% (95% CI = 8% to 22%) by age 50 years, 24% (95% CI = 15% to 34%) by age 70 years, and 28% (95% CI = 18% to 40%) by age 80 years."*
- [PMID: 16234564](https://pubmed.ncbi.nlm.nih.gov/16234564/): *"the lifetime risk... of melanoma in CDKN2A mutation carriers is very high, ranging from 58% in Europe to 91% in Australia by age 80 years."*

### Finding 10 — CDKN2A is a core somatic PDAC driver, validating the germline mechanism (F010)

Deep sequencing of 499 PDAC patients identified recurrent somatic driver mutations in **KRAS, TP53, CDKN2A, SMAD4, ARID1A, RNF43**; ~90% of PDAC is driven by (currently untargetable) KRAS mutations. The same KRAS-activating + CDKN2A/TP53/SMAD4-inactivating quartet drives PDAC and its variants. This mirrors the germline-plus-second-hit logic of the syndrome: germline CDKN2A loss supplies one of the obligatory PDAC driver lesions, with somatic KRAS activation and TP53/SMAD4 loss completing transformation.

- [PMID: 36999792](https://pubmed.ncbi.nlm.nih.gov/36999792/): *"revealed somatic driver mutations in KRAS, TP53, CDKN2A, SMAD4, ARID1A, RNF43."*
- [PMID: 28722124](https://pubmed.ncbi.nlm.nih.gov/28722124/): *"inactivating mutations in the tumor suppressor genes CDKN2A, TP53, and SMAD4."*

### Finding 11 — Epidemiology: rare Mendelian subset of familial melanoma (F011)

Approximately **5–10% of cutaneous melanoma** occurs in individuals with a family history. CDKN2A germline mutations occur in ~5–20% of familial melanoma and ~30–40% of dense FAMMM/PCMS kindreds, but are **rare in unselected/sporadic** melanoma (e.g., none among 125 consecutive Latvian cases). The Dutch national database catalogued 172 families with 15 distinct pathogenic CDKN2A variants (649 carriers), the founder c.225_243del (p16-Leiden) being most prevalent. The syndrome is rare (Orphanet FAMMM ORPHA:618). Both sexes are affected.

- [PMID: 40851494](https://pubmed.ncbi.nlm.nih.gov/40851494/): *"Approximately 5-10% of cutaneous melanoma occurs in individuals with a family history of the disease. While known high-penetrance genes, such as CDKN2A, explain some cases."*
- [PMID: 32482799](https://pubmed.ncbi.nlm.nih.gov/32482799/): *"We identified 172 families in which 649 individuals carried 15 different pathogenic variants. The most prevalent variant was the founder mutation c.225_243del."*

---

## Comprehensive Section-by-Section Characterization

### 1. Disease Information

**Overview.** Melanoma–Pancreatic Cancer Syndrome (also widely described within the Familial Atypical Multiple Mole Melanoma–Pancreatic Cancer, FAMMM-PC, spectrum) is an autosomal dominant hereditary cancer predisposition syndrome. Affected families show clustering of cutaneous malignant melanoma and pancreatic ductal adenocarcinoma, frequently with multiple atypical (dysplastic) nevi and additional tobacco/UV-related cancers.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| OMIM | 606719 |
| MONDO | MONDO:0011713 |
| Orphanet | ORPHA:618 (FAMMM) |
| Causal gene | CDKN2A (HGNC:1787), 9p21.3 |
| Related gene | CDK4 (alternative, rarer hereditary melanoma locus) |

**Synonyms / alternative names:** FAMMM-PC syndrome; Pancreatic cancer–melanoma syndrome (PCMS); melanoma–pancreatic cancer syndrome; CDKN2A-associated FAMMM. Related OMIM entries: cutaneous malignant melanoma 2 (CMM2, OMIM 155601); FAMMM (OMIM 155601); CDK4-related melanoma (OMIM 609048).

**Source of information:** Primarily aggregated disease-level resources (OMIM, Orphanet) and family-/cohort-based studies (Dutch, Swedish, Italian, Australian/North American registries), plus individual case reports.

### 2. Etiology

**Causal factor:** Germline loss-of-function variants in **CDKN2A** (p16INK4a and/or p14ARF). This is the primary, necessary genetic cause (F001). A minority of hereditary melanoma families instead carry **CDK4** gain-of-function variants (R24C/R24H) that phenocopy p16 loss (F003).

**Genetic risk factors:** Pathogenic CDKN2A variants (e.g., p16-Leiden c.225_243del; p.Arg112dup; p.Arg24Gln; splice and ARF-specific variants). **Modifier:** MC1R variants raise melanoma risk and cosegregate with deleterious p16 (F004). A TERT/CLPTM1L SNP was investigated as a candidate modifier (PMID 31203567).

**Environmental risk factors:** **UV radiation** (melanocytes) and **tobacco smoking** (pancreas, respiratory and upper-digestive epithelium) are the dominant modifiable exposures. Age, sex (both affected), and family history further stratify risk. General PDAC risk factors (diabetes, obesity, alcohol) also apply (PMID 37417291).

**Protective factors:** Sun protection and smoking avoidance reduce penetrance (inferred from the inverse of the documented risk factors). No validated germline protective allele is established for this syndrome.

**Gene–environment interactions:** Strongly demonstrated — ever-smoking carriers have ~9-fold higher risk of pancreatic/respiratory/upper-digestive cancers than never-smoking carriers (OR 9.3), and UV exposure across latitude modulates melanoma penetrance (F004).

### 3. Phenotypes

| Phenotype | Type | HPO | Onset | Frequency / notes |
|---|---|---|---|---|
| Cutaneous melanoma | Neoplasm | HP:0012056 | Early-adult (median ~36 y in carriers) | High; often multiple primaries |
| Pancreatic ductal adenocarcinoma | Neoplasm | HP:0002894 | Adult (mean ~60 y) | 15–20% lifetime (p16-Leiden) |
| Dysplastic / clinically atypical nevi | Physical sign | HP:0003764 | Childhood–adult | Common but not obligate |
| Multiple primary melanomas | Neoplasm | HP:0012056 | Adult | Characteristic |
| Head-and-neck / oral SCC | Neoplasm | — | Adult | Over-represented (PMID 35123577) |
| Respiratory / upper-digestive cancers | Neoplasm | — | Adult | Elevated, tobacco-potentiated |

Severity is high (life-threatening malignancies); progression is tumor-dependent. Quality-of-life impact arises from lifelong surveillance burden, repeated excisions, and the psychological weight of cancer risk; PDAC carries severe QoL and mortality impact. Carriers do **not** uniformly meet full atypical-mole-syndrome criteria (F005).

### 4. Genetic / Molecular Information

**Causal gene:** CDKN2A (HGNC:1787; OMIM 600160), 9p21.3. The locus encodes p16INK4a (transcript using exons 1α-2-3) and p14ARF (exon 1β + alternative reading frame of exon 2), two unrelated proteins (F001).

**Pathogenic variants:** Missense (e.g., p.Arg24Gln, p.Gly23Asp, p.Ala60Val, p.Pro114Ser), in-frame deletions (c.225_243del / p16-Leiden), duplications (p.Arg112dup), splice-site, and ARF-specific lesions. ClinVar/ACMG classifications range pathogenic → likely pathogenic → VUS (e.g., Ala148Thr is a low-penetrance polymorphism, PMID 17505264). Allele frequencies are very low in gnomAD (rare founder alleles region-specific). **Origin:** germline for the syndrome; CDKN2A is also a recurrent **somatic** PDAC/melanoma driver (F010). **Functional consequence:** loss of function (destabilization, loss of CDK4 binding) (F007).

**Modifier genes:** MC1R (melanoma penetrance), candidate TERT/CLPTM1L SNP. **Chromosomal:** second-hit LOH at 9p21 in tumors (F003). **Epigenetic:** CDKN2A promoter hypermethylation is a well-known somatic silencing mechanism in sporadic tumors and can contribute to the "second hit" in carriers.

### 5. Environmental Information

**Environmental factors:** UV radiation (principal melanoma driver). **Lifestyle factors:** tobacco smoking (strong GxE amplifier of pancreatic/aerodigestive risk); alcohol and obesity/diabetes are general PDAC risk factors (PMID 37417291). **Infectious agents:** none implicated.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A **germline CDKN2A loss-of-function variant** is inherited (present in every cell). *(leads to)*
2. **Reduced or absent functional p16INK4a** (and, for many variants, p14ARF), due to protein destabilization and/or loss of CDK4 binding — demonstrated biophysically (F007). *(results in)*
3. **De-repression of CDK4/6–cyclin D kinase activity** (p16 normally inhibits CDK4/6). *(leads to)*
4. **Hyperphosphorylation and inactivation of RB.** *(results in)*
5. **E2F-driven transcription and unchecked G1→S transition**, i.e., escape from senescence/cell-cycle arrest. *(enables)*
6. Acquisition of a **somatic second hit** inactivating the wild-type CDKN2A allele (LOH) — observed in tumors (F003, inferred from mouse LOH). *(combines with)*
7. **Carcinogen-driven oncogenic RAS/MAPK activation** — UV-induced in melanocytes, tobacco-associated KRAS activation in pancreatic ductal cells (F003, F010). *(drives)*
8. **Malignant transformation** of the melanocyte (→ melanoma) or pancreatic ductal epithelial cell (→ PDAC, typically alongside somatic TP53/SMAD4 loss). *(manifests as)*
9. **Clinical melanoma and/or pancreatic ductal adenocarcinoma**, and a broader tobacco/UV-potentiated cancer spectrum.

**Branch (p14ARF arm):** For variants that also disable p14ARF, loss of ARF → failure to inhibit MDM2 → **degradation of p53** → impaired apoptosis/senescence, adding a second oncogenic axis (F001, PMID 12406321, PMID 12019208). Thus a single locus can cripple both the RB and p53 tumor-suppressor pathways. The independent contribution of the ARF arm in humans is partly inferred rather than fully demonstrated.

```
Germline CDKN2A LOF
        │
  ┌─────┴─────────────────────────┐
  ▼ (p16 arm)                      ▼ (p14ARF arm)
↓ p16INK4a                      ↓ p14ARF
  │                               │
CDK4/6–cyclinD ↑               MDM2 unchecked
  │                               │
RB hyperphosphorylation        p53 degraded
  │                               │
E2F ↑ → G1/S escape            apoptosis/senescence ↓
  └───────────────┬───────────────┘
                  ▼
        + somatic 2nd hit (LOH)
        + RAS/MAPK (UV / tobacco)
                  ▼
     Melanocyte / ductal transformation
                  ▼
        Melanoma / PDAC
```

**Molecular pathways:** RB/cell-cycle (CDK4/6–cyclin D–RB–E2F), p53/MDM2, RAS–MAPK. **Cellular processes:** cell-cycle dysregulation, senescence escape, impaired apoptosis. **GO terms:** cell cycle arrest (GO:0007050), regulation of G1/S transition (GO:2000045), cyclin-dependent protein kinase activity (GO:0004693), negative regulation of cell population proliferation (GO:0008285). **CL terms:** melanocyte (CL:0000148), pancreatic ductal cell (CL:0002079).

### 7. Anatomical Structures Affected

- **Primary organs:** skin (UBERON:0002097) — melanocytes; pancreas (UBERON:0001264) — exocrine ductal epithelium.
- **Secondary / extended spectrum:** respiratory tract (UBERON:0000065), upper digestive tract/oral cavity (UBERON:0000167), and other sites in heavily exposed carriers.
- **Tissue/cell level:** epithelial (pancreatic ductal cell, CL:0002079) and neural-crest-derived melanocyte (CL:0000148).
- **Subcellular:** nucleus (GO:0005634) — site of RB/E2F/p53 regulation; cytoplasmic p16–CDK4 interaction.
- **Lateralization:** not applicable (neoplastic, site-variable).

### 8. Temporal Development

**Onset:** Melanoma typically early adulthood (median ~36 y in carriers); PDAC typically later adulthood (mean ~60 y). Course is chronic lifelong cancer risk; individual tumors progress per standard oncologic staging (AJCC). PDAC is often rapidly progressive once invasive — surveillance aims to catch the pre-invasive/early-invasive window (T1N0M0), the critical period for curative intervention (F002, F008). Main-pancreatic-duct dilatation can be an early surveillance signal (PMID 30910317).

### 9. Inheritance and Population

- **Inheritance:** autosomal dominant. **Penetrance:** incomplete, age-dependent, ascertainment- and UV-dependent (melanoma ~28% by 80 population-based vs 58–91% in dense kindreds; PDAC 15–20% in p16-Leiden) (F002, F009).
- **Expressivity:** highly variable (melanoma-only, PDAC-only, or combined; variable extra-tumor spectrum).
- **Founder effects:** p16-Leiden (Netherlands); p.Arg112dup (Sweden); population-specific spectra (F011).
- **Epidemiology:** rare Mendelian subset; familial melanoma ~5–10% of all melanoma, CDKN2A carriers rare in unselected patients; both sexes affected (F011).
- **Genetic anticipation / mosaicism / consanguinity:** not characteristic (dominant, not a repeat-expansion disorder).

### 10. Diagnostics

- **Genetic testing:** single-gene CDKN2A sequencing/del-dup; multigene hereditary-melanoma/pancreatic-cancer panels (CDKN2A, CDK4, BAP1, POT1, BRCA2, PALB2, ATM); WES/WGS in undiagnosed families. GeneReviews/GTR-aligned.
- **Melanoma diagnostics:** dermoscopy, total-body photography, sequential digital dermoscopic imaging; histopathology/IHC; FISH for ambiguous melanocytic lesions (PMID 21834951).
- **Pancreatic diagnostics:** MRI/MRCP and EUS (preferred over CT/ERCP per CAPS); CA 19-9 as adjunct biomarker; liquid biopsy/ctDNA emerging (PMID 41671451).
- **Differential diagnosis:** other hereditary melanoma/pancreatic syndromes (BAP1-TPDS, Peutz-Jeghers, hereditary breast-ovarian [BRCA2/PALB2], Lynch).

### 11. Outcome / Prognosis

Prognosis is tumor- and stage-dependent. **Melanoma:** excellent for early/in-situ disease; modern adjuvant/neoadjuvant immunotherapy improves outcomes in resectable stage III (F006). **PDAC:** historically dismal (~5-year survival ~5% in general population), but **surveillance-detected, resected PDAC in carriers has ~47% long-term cure** (F002). Multiple/synchronous PDAC occurs, sometimes motivating total pancreatectomy (PMID 29769629). Prognostic factors: stage at detection, resectability, smoking status. Pancreatic surveillance adds ~2.1 years life expectancy per cost-effectiveness modeling (F002).

### 12. Treatment

- **Melanoma pharmacotherapy:** anti-PD-1 (pembrolizumab NCIT:C106432, nivolumab NCIT:C68924), anti-CTLA-4 (ipilimumab NCIT:C2654), anti-LAG-3 (relatlimab); BRAF/MEK inhibitors (dabrafenib NCIT:C82386 + trametinib NCIT:C77908) for BRAF-V600 tumors. Neoadjuvant ipilimumab+nivolumab (NADINA) superior to adjuvant nivolumab (F006).
- **Surgical:** wide local excision (melanoma); pancreaticoduodenectomy/partial or total pancreatectomy (NCIT:C51782) for resectable PDAC.
- **Mechanism-based / investigational:** CDK4/6 inhibitors (palbociclib/ribociclib/abemaciclib) rational in CDKN2A-null tumors (F006, F007); PI3K/mTOR combinations explored in CDKN2A-deficient contexts (PMID 28704762).
- **Pharmacogenomics / personalized:** BRAF genotype guides targeted therapy; germline status guides surveillance and family testing.

### 13. Prevention

- **Primary:** sun protection/UV avoidance; **smoking cessation** (especially impactful given GxE, F004).
- **Secondary (early detection):** skin surveillance with TBP/SDDI (PMID 24964862); **annual pancreatic MRI ± EUS** in carriers per CAPS (F008); cascade genetic testing of relatives.
- **Genetic counseling:** risk assessment, family planning, cascade testing; behavioral-change counseling (PMID 35372037).
- **Tertiary:** intensive post-resection surveillance for metachronous tumors.

### 14. Other Species / Natural Disease

- **Orthologous gene:** mouse *Cdkn2a* (Ink4a/Arf). **Taxonomy:** *Mus musculus* (NCBI:txid10090) extensively used.
- **Natural disease:** CDKN2A/p16 pathway alterations occur across many species' cancers; no single well-defined companion-animal "melanoma–pancreatic syndrome" ortholog is established in OMIA, but the pathway is deeply evolutionarily conserved.
- **Comparative biology:** mouse models faithfully reproduce the Ink4a-loss + RAS/MAPK melanoma mechanism, including LOH of the wild-type allele (F003).

### 15. Model Organisms

- **Mammalian (mouse):** Ink4a/Arf knockout; melanocyte-specific H-rasG12V;ink4a-null (spontaneous melanoma); Tyr::NRAS(Q61K);Cdkn2a-/- (metastasizing melanoma); Cdk4R24C knock-in (INK4-insensitive CDK4) (F003).
- **Phenotype recapitulation:** strong for melanoma predisposition, UV/RAS cooperation, and second-hit LOH; both Ink4a/pRB and Arf/p53 arms modeled.
- **Limitations:** mouse skin differs from human; spontaneous PDAC in these specific melanoma models is less emphasized than melanoma (pancreatic modeling typically uses KRAS-driven GEMMs).
- **Resources:** MGI; genetically engineered mouse lines; patient-derived cell lines for p16 structure–function (PMID 12009890, 39821174).

---

## Mechanistic Model / Interpretation

The unifying interpretation is that **germline CDKN2A loss functions as a "pre-installed" driver hit**. Both melanoma and PDAC are multi-hit cancers; CDKN2A inactivation is a recurrent **somatic** driver in both tumor types (F010). A germline carrier is therefore born one obligatory step into the tumorigenic cascade in every cell, dramatically lowering the probability threshold for transformation once tissue-specific carcinogens supply the complementary lesions (UV→melanocyte; tobacco→pancreatic/aerodigestive epithelium). This single model explains:

- **Why both melanoma and PDAC cluster** in the same families (same germline driver, two tissues with potent carcinogen exposures).
- **Why penetrance tracks UV latitude and tobacco** (the complementary somatic hits are environmentally supplied) — the gene–environment interaction (F004) and the population-vs-kindred penetrance gap (F009).
- **Why mouse genetics reproduce the disease** only when Ink4a loss is combined with RAS/MAPK activation and the wild-type allele is lost (F003).
- **Why management is tumor-specific** and surveillance-centric: you cannot replace the germline tumor suppressor, so you intercept tumors early (F002, F006, F008).

| Tissue | Pre-installed hit (germline) | Complementary somatic hit(s) | Environmental driver |
|---|---|---|---|
| Melanocyte | CDKN2A LOF | 2nd-allele LOH; BRAF/NRAS | UV |
| Pancreatic duct | CDKN2A LOF | KRAS; TP53; SMAD4 | Tobacco |

---

## Evidence Base

| PMID | Role | Supports |
|---|---|---|
| [32941720](https://pubmed.ncbi.nlm.nih.gov/32941720/) | Case/review | CDKN2A causality, p16–CDK4/6, 30% frequency (F001) |
| [14871223](https://pubmed.ncbi.nlm.nih.gov/14871223/) | Review | FAMMM pathogenesis, ~40% mutation detection (F001) |
| [31203567](https://pubmed.ncbi.nlm.nih.gov/31203567/) | Cohort | 70% melanoma / 15–20% PDAC lifetime risk (F002) |
| [36785917](https://pubmed.ncbi.nlm.nih.gov/36785917/) | Cohort/modeling | Surveillance resection/cure, cost-effectiveness (F002) |
| [9353252](https://pubmed.ncbi.nlm.nih.gov/9353252/) | Mouse | Ink4a loss + Ras → melanoma (F003) |
| [11726500](https://pubmed.ncbi.nlm.nih.gov/11726500/) | Mouse | CDK4 R24C knock-in tumors (F003) |
| [26587692](https://pubmed.ncbi.nlm.nih.gov/26587692/) | Mouse | NRAS;Cdkn2a-/- metastasizing melanoma (F003) |
| [12406321](https://pubmed.ncbi.nlm.nih.gov/12406321/) | Review | Ink4a/pRB and Arf/p53 arms in melanoma (F003/F007) |
| [24935963](https://pubmed.ncbi.nlm.nih.gov/24935963/) | Prospective cohort | Extra-melanoma RR; tobacco GxE (F004) |
| [16462187](https://pubmed.ncbi.nlm.nih.gov/16462187/) | Review | MC1R modifier, UV penetrance, early/multiple melanoma (F004/F005) |
| [20526219](https://pubmed.ncbi.nlm.nih.gov/20526219/) | Cohort | CAN correlation, not full AMS (F005) |
| [42794996](https://pubmed.ncbi.nlm.nih.gov/42794996/) | Review | Neoadjuvant immunotherapy (NADINA) (F006) |
| [39821174](https://pubmed.ncbi.nlm.nih.gov/39821174/) | Computational | p16 mutations abolish CDK4 binding (F007) |
| [12009890](https://pubmed.ncbi.nlm.nih.gov/12009890/) | In vitro | p16 N-terminal destabilization (F007) |
| [15899796](https://pubmed.ncbi.nlm.nih.gov/15899796/) | In vitro/mouse | CDK4R24C, E2F/topoII mechanism (F007) |
| [23135763](https://pubmed.ncbi.nlm.nih.gov/23135763/) | Guideline | CAPS: p16 carriers as screening candidates (F008) |
| [31672839](https://pubmed.ncbi.nlm.nih.gov/31672839/) | Guideline | CAPS 2020: start age, modality (F008) |
| [33593706](https://pubmed.ncbi.nlm.nih.gov/33593706/) | Guideline eval | CAPS cyst criteria performance (F008) |
| [16234564](https://pubmed.ncbi.nlm.nih.gov/16234564/) | Population study | Ascertainment-dependent penetrance (F009) |
| [36999792](https://pubmed.ncbi.nlm.nih.gov/36999792/) | Sequencing | CDKN2A as somatic PDAC driver (F010) |
| [28722124](https://pubmed.ncbi.nlm.nih.gov/28722124/) | Sequencing | CDKN2A/TP53/SMAD4 PDAC quartet (F010) |
| [40851494](https://pubmed.ncbi.nlm.nih.gov/40851494/) | Review | 5–10% familial melanoma fraction (F011) |
| [32482799](https://pubmed.ncbi.nlm.nih.gov/32482799/) | National cohort | 172 families, variant spectrum, founder (F011) |
| [17505264](https://pubmed.ncbi.nlm.nih.gov/17505264/) | Clinic cohort | CDKN2A rare in unselected melanoma (F011) |

---

## Limitations and Knowledge Gaps

1. **Penetrance uncertainty.** Estimates vary several-fold by ascertainment and geography (28% vs 58–91% for melanoma; PDAC largely from one founder cohort). Variant-specific penetrance for most individual CDKN2A alleles is poorly quantified.
2. **p16 vs p14ARF attribution.** Because the locus encodes two proteins, the independent contribution of ARF loss to the human melanoma/PDAC phenotype remains incompletely resolved; most data are variant-mixed.
3. **PDAC surveillance generalizability.** The strongest surveillance evidence comes from the Dutch p16-Leiden cohort; optimal modality, start age, and interval for other variants/populations are less certain, and CAPS cyst criteria are insufficiently sensitive.
4. **Limited direct germline-syndrome therapeutics.** CDK4/6-inhibitor rationale in CDKN2A-null tumors is mechanistically compelling but not validated in randomized trials for this syndrome.
5. **Modifier genetics.** Beyond MC1R, candidate modifiers (e.g., TERT/CLPTM1L) are not established.
6. **No in-house data analysis.** This report synthesizes literature; no primary dataset was analyzed in these iterations.

---

## Proposed Follow-up Experiments / Actions

1. **Variant-specific penetrance registry:** pool international CDKN2A carrier cohorts to produce allele- and modifier-stratified age-specific risk curves for melanoma and PDAC.
2. **Prospective multi-variant pancreatic surveillance trial:** extend Dutch-style MRI/EUS surveillance to non–p16-Leiden variants and diverse populations; incorporate ctDNA/CA19-9 and cyst-fluid biomarkers to improve sensitivity.
3. **ARF-specific functional dissection:** engineer isogenic cell/mouse models separating p16 vs p14ARF loss to quantify each arm's tissue-specific oncogenic contribution.
4. **CDK4/6-inhibitor biomarker trials:** test CDK4/6 inhibitors (± MEK or PI3K/mTOR inhibitors) in CDKN2A-deficient melanoma and PDAC, using the documented CDK4/6 dependence as the biomarker.
5. **GxE quantification:** formal modeling of smoking-cessation benefit on pancreatic/aerodigestive risk in carriers to strengthen counseling guidance.
6. **Comparative/animal-model program:** evaluate naturally occurring CDKN2A-pathway tumors in companion animals (OMIA) for translational models.

---

*Evidence source types: human clinical/cohort (majority), model organism (mouse: F003), in vitro/biophysical (F007), computational (F007), and guideline/consensus (F008). PMIDs cited throughout; direct abstract quotes provided in Key Findings.*


## Artifacts

- [OpenScientist final report](Melanoma-Pancreatic_Cancer_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Melanoma-Pancreatic_Cancer_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 29 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011713` (4 mentions) - the report calls it "MONDO"; MONDO calls it **melanoma-pancreatic cancer syndrome**
- `HP:0012056` (3 mentions) - the report calls it "Neoplasm"; HP calls it **Cutaneous melanoma**
- `HP:0003764` (2 mentions) - the report calls it "Physical sign"; HP calls it **Nevus**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007050` (GO_0007050) (1 mention) - replaced by `GO:0051726`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002894` (2 mentions) - the report calls it "Neoplasm"; HP calls it **Neoplasm of the pancreas**
- `UBERON:0002097` (1 mention) - the report calls it "Primary organs:** skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names
- `UBERON:0000065` (1 mention) - the report calls it "Secondary / extended spectrum:** respiratory tract"; UBERON calls it **respiratory tract**
- `GO:0005634` (1 mention) - the report calls it "Subcellular:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.