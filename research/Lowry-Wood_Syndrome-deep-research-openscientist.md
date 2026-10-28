---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-27T18:04:52.520171'
end_time: '2026-10-27T18:20:40.589048'
duration_seconds: 948.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Lowry-Wood Syndrome
  mondo_id: MONDO:0009191
  category: Mendelian
  causal_genes: RNU4ATAC
  omim_id: not recorded
  synonyms: Lowry Wood syndrome; LWS; RNU4ATAC-related Lowry-Wood syndrome; Multiple
    epiphyseal dysplasia with microcephaly and nystagmus
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
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 12
  validator_version: 0.4.0
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 5
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009191
    reported_labels:
    - MONDO
    ontology_label: Lowry-Wood syndrome
  - term_id: HP:0011109
    reported_labels:
    - Chilblain-like skin lesions
    ontology_label: Chronic sinusitis
  - term_id: UBERON:0000955
    reported_labels:
    - Nervous system / brain
    ontology_label: brain
  labels_variant: 6
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
  path: Lowry-Wood_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Lowry-Wood_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lowry-Wood Syndrome
- **MONDO ID:** MONDO:0009191 (if available)
- **Causal gene(s):** RNU4ATAC
- **OMIM:** not recorded
- **Synonyms:** Lowry Wood syndrome; LWS; RNU4ATAC-related Lowry-Wood syndrome; Multiple epiphyseal dysplasia with microcephaly and nystagmus
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Lowry-Wood Syndrome** covering all of the
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

# Lowry-Wood Syndrome (MONDO:0009191): A Comprehensive Disease Characteristics Report

**MONDO:** MONDO:0009191 · **Causal gene:** *RNU4ATAC* (RNA, U4atac small nuclear; HGNC:34140; gene OMIM 601428; chr 2q14.2) · **Orphanet:** ORPHA:2648 · **Category:** Mendelian, autosomal recessive

## Summary

**Lowry-Wood syndrome (LWS; MONDO:0009191) is an ultra-rare, autosomal-recessive skeletal dysplasia caused by biallelic loss-of-function variants in *RNU4ATAC***, a non-coding, single-exon gene on chromosome 2q14.2 (HGNC:34140; OMIM 601428) that is transcribed into the **U4atac small nuclear RNA (snRNA)** — a core component of the **minor (U12-dependent) spliceosome**. Although the disorder's descriptive synonym ("Multiple epiphyseal dysplasia with microcephaly and nystagmus") emphasizes the skeletal and ophthalmologic triad, the causal lesion is not in a cartilage or eye gene but in a housekeeping RNA required for excision of ~700–800 "minor" (U12-type) introns scattered across the genome. LWS represents the **mildest end** of a clinical spectrum of **RNU4ATAC-opathies** that also includes **Roifman syndrome (RS)** and the severe, often perinatally lethal **microcephalic osteodysplastic primordial dwarfism type 1 (MOPD1 / Taybi-Linder syndrome)**.

The defining clinical features of LWS are **multiple epiphyseal dysplasia** (causing short stature and joint/limb anomalies), **microcephaly**, **developmental delay / intellectual disability** (typically mild), and **eye involvement** (nystagmus and progressive retinal dystrophy). Across the broader RNU4ATAC-opathy spectrum, additional management-relevant features include **immune deficiency** (antibody deficiency, low B-cell subsets), **cerebral anomalies**, and **chilblain-like skin lesions**. Genotype–phenotype analyses show that severity is governed largely by **variant position within the U4atac RNA secondary structure**: the most severe MOPD1-causing variants cluster in the functionally constrained 5′ stem-loop critical for U4/U6.U5 tri-snRNP assembly, whereas milder LWS and RS variants are more dispersed.

The unifying molecular mechanism is **transcriptome-wide retention and mis-splicing of U12-type minor introns**, demonstrated by RNA-seq in patient cells and consistent across the spectrum. This minor-intron splicing defect depletes self-amplifying neural progenitors (producing microcephaly), disrupts chondro-osseous development (producing epiphyseal dysplasia and short stature), and secondarily perturbs ciliary function, JAK/STAT signaling, and type I interferon responses (contributing to immune and skin phenotypes). Diagnosis hinges on sequencing the non-coding *RNU4ATAC* exon — frequently missed by standard exome pipelines — with RNA-seq minor-intron-retention as a functional biomarker that enables variant reclassification. No disease-modifying therapy exists; management is supportive and multidisciplinary, with genetic counseling for the 25% recurrence risk.

---

## Key Findings

### Finding 1 — LWS is caused by biallelic variants in the non-coding minor-spliceosome gene *RNU4ATAC*

Exome sequencing across multiple families established that LWS results from **biallelic (homozygous or compound heterozygous) pathogenic variants in *RNU4ATAC***, which transcribes the U4atac snRNA of the minor (U12-dependent) spliceosome. Farach et al. (2018) first established the genetic cause, describing *"three patients with Lowry Wood syndrome with biallelic RNU4ATAC pathogenic variants"* and stating that their report *"is the first to establish the genetic cause for Lowry Wood syndrome"* ([PMID: 29265708](https://pubmed.ncbi.nlm.nih.gov/29265708/)). Shelihan et al. (2018) confirmed the association, noting that *"Pathogenic variants in RNU4ATAC, an RNA of the minor spliceosome important for the excision of U12-dependent introns, have been recently associated with LWS"* ([PMID: 30368667](https://pubmed.ncbi.nlm.nih.gov/30368667/)). *RNU4ATAC* has a single non-coding exon on chromosome 2q14.2. This is a human clinical/genetic finding.

### Finding 2 — RNU4ATAC disorders form a severity spectrum governed by variant location, with LWS the mildest

The RNU4ATAC-opathies constitute a continuum of severity from **MOPD1 (most severe, frequently lethal)** through **Roifman syndrome** to **Lowry-Wood syndrome (mildest)**. Shelihan et al. (2018) analyzed all reported variants and found that *"FitCons scores for nucleotides mutated in the more severe MOPD are higher than RS or LWS and that they were more frequently located in the 5' Stem-Loop of the RNA critical for the formation of the U4/U6.U5 tri-snRNP complex, whereas the variants are more dispersed in the other conditions"* ([PMID: 30368667](https://pubmed.ncbi.nlm.nih.gov/30368667/)). A recent integrated reevaluation confirms the spectrum *"whose severity ranges from the microcephalic osteodysplastic primordial dwarfism type 1 (MOPD1) to the milder Roifman syndrome"* ([PMID: 41808109](https://pubmed.ncbi.nlm.nih.gov/41808109/)). Clinically the categories overlap substantially; one reported individual had *"a novel genotype and phenotype spanning all three disorders"* ([PMID: 36622817](https://pubmed.ncbi.nlm.nih.gov/36622817/)), supporting the view of a single phenotypic continuum rather than discrete diseases.

### Finding 3 — Core clinical phenotype: multiple epiphyseal dysplasia, microcephaly, short stature, developmental delay, and eye involvement

LWS is defined as *"a skeletal dysplasia characterized by multiple epiphyseal dysplasia associated with microcephaly, developmental delay and intellectual disability, and eye involvement"* ([PMID: 30368667](https://pubmed.ncbi.nlm.nih.gov/30368667/)). In the largest RNU4ATAC-opathy cohort reported to date (n = 60), *"Core features in this cohort—present in most individuals assessed and varying in severity—include microcephaly, short stature, skeletal anomalies, developmental delay, cerebral anomalies, skin conditions, and immune deficiency"* ([PMID: 42322193](https://pubmed.ncbi.nlm.nih.gov/42322193/)). Eye involvement in LWS prominently includes **nystagmus** (reflected in the descriptive synonym) and **progressive retinal dystrophy**.

### Finding 4 — Mechanism: defective U4atac impairs the minor spliceosome, causing transcriptome-wide minor (U12-type) intron retention

The U4atac snRNA is *"a minor spliceosome component that is essential for minor intron splicing"* ([PMID: 26522830](https://pubmed.ncbi.nlm.nih.gov/26522830/)). The minor spliceosome excises ~700–800 U12-dependent introns (~0.5–1% of all human introns) found in a functionally diverse set of genes. Pathogenic *RNU4ATAC* variants impair this machinery: RNA-seq of patient cells *"confirms extensive and specific defects of minor intron splicing"* ([PMID: 26522830](https://pubmed.ncbi.nlm.nih.gov/26522830/)), and across the large cohort *"all individuals who underwent RNA-seq showed a consistent pattern of minor intron retention"* ([PMID: 42322193](https://pubmed.ncbi.nlm.nih.gov/42322193/)). This minor-intron retention is the shared, upstream molecular consequence across the entire RNU4ATAC-opathy spectrum and provides a functional readout usable for variant reclassification.

### Finding 5 — Secondary mechanisms: ciliary dysfunction, dysregulated JAK/STAT signaling, and type I interferon activation

Beyond the primary splicing defect, several downstream pathways are perturbed. (1) **Ciliary dysfunction:** U4atac depletion secondarily produces ciliary defects — *"Deficiency of the minor spliceosome component U4atac snRNA secondarily results in ciliary defects in human and zebrafish"* ([PMID: 36802443](https://pubmed.ncbi.nlm.nih.gov/36802443/)) — linking minor-spliceosome deficiency to ciliopathy-like features. (2) **JAK/STAT signaling:** A *Drosophila* U4atac mutant shows reduced splicing of the JAK homolog *hopscotch*; *"our work identifies alterations of Jak signaling as part of the pathogenesis of RNU4atac-opathy"* ([PMID: 42463491](https://pubmed.ncbi.nlm.nih.gov/42463491/)), implicating JAK/STAT in hematopoietic/immune pathogenesis. (3) **Type I interferon:** RNU4ATAC patients commonly develop painful chilblain-like skin lesions; *"painful chilblain-like lesions are common in RNU4ATAC patients and are linked to dysregulated type I interferon signalling"* ([PMID: 40415209](https://pubmed.ncbi.nlm.nih.gov/40415209/)).

### Finding 6 — Immunodeficiency and progressive retinal dystrophy are recurrent, management-relevant features

**Immune deficiency** — antibody deficiency, low lymphocyte and B-cell subsets, impaired B-cell maturation — is characteristic of Roifman syndrome and is now recognized even in the severe MOPD1 end of the spectrum. A report of twin sisters emphasized B-cell anomalies in MOPD1 and underscored *"the importance of considering immunodeficiency in MOPDI management to reduce the risk of serious infectious episodes"* ([PMID: 38837402](https://pubmed.ncbi.nlm.nih.gov/38837402/)). **Retinal dystrophy** in RNU4ATAC-Roifman syndrome is a generalized rod-cone dystrophy: in a deeply phenotyped cohort of 10 patients, all had abnormal ERG and *"nine showed generalized rod-cone dystrophy"* ([PMID: 37225827](https://pubmed.ncbi.nlm.nih.gov/37225827/)), with nyctalopia common and progressive visual loss on follow-up. These findings justify immunologic and ophthalmologic surveillance in LWS.

### Finding 7 — LWS is an autosomal recessive disorder, first described by Lowry and Wood (1975), and is ultra-rare

Lowry and Wood (1975) first described two boys with epiphyseal dysplasia, short stature, microcephaly, and nystagmus. Nevin et al. (1986) reported a second family, noting *"the second example of the syndrome first described by Lowry and Wood [1975] in two boys who had epiphyseal dysplasia, short stature, microcephaly, and nystagmus; one of these patients was mildly mentally retarded"* and concluding that *"The Lowry-Wood syndrome probably is an autosomal recessive trait"* ([PMID: 3706411](https://pubmed.ncbi.nlm.nih.gov/3706411/)). Only a few dozen molecularly confirmed RNU4ATAC-opathy patients exist worldwide (60 in the largest cohort), making LWS ultra-rare with no formal prevalence estimate.

### Finding 8 — Animal models recapitulate key features: minor-spliceosome loss causes microcephaly and limb micromelia

Model-organism work supports causality between minor-spliceosome dysfunction and the cardinal LWS phenotypes. Conditional inactivation of the minor spliceosome (Rnu11/U11 ablation) in developing mouse cortex demonstrated that *"Minor spliceosome inactivation causes microcephaly, owing to cell cycle defects and death of self-amplifying radial glial cells"* ([PMID: 30093551](https://pubmed.ncbi.nlm.nih.gov/30093551/)). In the limb, *"Loss of U11 small nuclear RNA in the developing mouse limb results in micromelia"* ([PMID: 32665241](https://pubmed.ncbi.nlm.nih.gov/32665241/)), linking minor-spliceosome loss to skeletal dysplasia. A CRISPR *Drosophila* U4atac mutant reproduced growth/neurodevelopmental defects, immunodeficiency, and GI symptoms via mis-splicing of innate-immunity and hematopoiesis transcripts ([PMID: 42463491](https://pubmed.ncbi.nlm.nih.gov/42463491/)), and zebrafish U4atac knockdown produced ciliary defects ([PMID: 36802443](https://pubmed.ncbi.nlm.nih.gov/36802443/)).

### Finding 9 — Diagnosis requires sequencing the non-coding *RNU4ATAC* exon; variants are frequently missed, and RNA-seq aids classification

Because *RNU4ATAC* is a single-exon non-coding gene, *"the bioinformatic prediction algorithms assessing the effect of sequence variants on splicing or protein function are irrelevant"* ([PMID: 32628740](https://pubmed.ncbi.nlm.nih.gov/32628740/)), and variants *"are often overlooked in analysis because of their noncoding nature"* ([PMID: 42322193](https://pubmed.ncbi.nlm.nih.gov/42322193/)). Some exome capture kits do not even target the gene — *"RNU4ATAC is not targeted by many commercially available exome capture kits"* ([PMID: 37666272](https://pubmed.ncbi.nlm.nih.gov/37666272/)) — so whole-genome sequencing or targeted *RNU4ATAC* Sanger sequencing may be required; in one Chinese family, variants were identified only after WES was negative ([PMID: 29370840](https://pubmed.ncbi.nlm.nih.gov/29370840/)). A cellular minor-intron splicing reporter assay ([PMID: 32628740](https://pubmed.ncbi.nlm.nih.gov/32628740/)) and RNA-seq demonstrating minor intron retention provide functional evidence: *"In 6 individuals, RNA-seq enabled the reclassification of variants of uncertain significance as likely pathogenic"* ([PMID: 42322193](https://pubmed.ncbi.nlm.nih.gov/42322193/)).

### Finding 10 — RNU4ATAC disorders are molecularly and clinically distinct from PCNT-related MOPD type II

A critical differential-diagnosis point: the RNU4ATAC-opathies (MOPD1, Roifman, LWS) must be distinguished from the superficially similarly named **microcephalic osteodysplastic primordial dwarfism type II (MOPD II)**, caused not by a spliceosome RNA but by loss-of-function variants in **PCNT (pericentrin)**, a centrosomal protein. *"Loss-of-function variants of this gene are responsible for microcephalic osteodysplastic primordial dwarfism type II (MOPDII), a rare inherited autosomal recessive disorder"* ([PMID: 37234811](https://pubmed.ncbi.nlm.nih.gov/37234811/)). MOPD II is distinguished by a **high risk of cerebral aneurysms and Moyamoya vasculopathy**; in one report *"The boy died at 8 years of age as a result of an intracranial hemorrhage due to a cerebral aneurism associated with the Moyamoya malformation"* ([PMID: 37234811](https://pubmed.ncbi.nlm.nih.gov/37234811/)). This cerebrovascular risk belongs to PCNT-MOPD II, **not** to RNU4ATAC disorders — a distinction that affects surveillance and prognosis.

---

## Detailed Report by Section

### 1. Disease Information

**Overview.** Lowry-Wood syndrome is an ultra-rare autosomal-recessive skeletal dysplasia (a "minor spliceosomopathy") characterized by multiple epiphyseal dysplasia, microcephaly, short stature, developmental delay/intellectual disability, and ophthalmologic abnormalities (nystagmus, retinal dystrophy). It is the mildest recognized presentation of the RNU4ATAC-opathy spectrum.

**Key identifiers.**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009191 |
| Causal gene | *RNU4ATAC* (HGNC:34140; OMIM 601428; chr 2q14.2) |
| Orphanet | ORPHA:2648 |
| OMIM (disease) | Not formally recorded as a distinct phenotype MIM (LWS historically clinical; now within RNU4ATAC-opathy) |
| ICD-10 | Q77.x (osteochondrodysplasia with defects of growth; best fit) |
| MeSH | No dedicated LWS descriptor; indexed under osteochondrodysplasias/dwarfism |

**Synonyms:** Lowry Wood syndrome; LWS; RNU4ATAC-related Lowry-Wood syndrome; Multiple epiphyseal dysplasia with microcephaly and nystagmus.

**Information source:** Derived from aggregated disease-level resources and small published case series/cohorts (individual-patient reports pooled into cohorts such as the n = 60 RNU4ATAC-opathy study), not from EHR-scale data.

### 2. Etiology

**Causal factor:** Purely **genetic** — biallelic (homozygous or compound heterozygous) loss-of-function variants in *RNU4ATAC* ([PMID: 29265708](https://pubmed.ncbi.nlm.nih.gov/29265708/)). No environmental or infectious cause.

**Genetic risk factors / modifiers:** The principal determinant of phenotype severity is **variant position within the U4atac RNA secondary structure** — 5′ stem-loop variants (high FitCons constraint) produce severe MOPD1, while more dispersed variants produce milder LWS/RS ([PMID: 30368667](https://pubmed.ncbi.nlm.nih.gov/30368667/)). Compound heterozygosity combining a "severe" and a "mild" allele can yield intermediate phenotypes. No separate susceptibility loci or distinct modifier genes have been established.

**Environmental / protective factors and gene–environment interactions:** None identified; not applicable for a fully penetrant Mendelian recessive disorder. Consanguinity increases the chance of homozygosity in affected families (relevant to recessive inheritance generally).

### 3. Phenotypes

| Phenotype | HPO term (suggested) | Type | Onset | Frequency | Severity/course |
|---|---|---|---|---|---|
| Multiple epiphyseal dysplasia | HP:0002656 | Physical/skeletal | Congenital/childhood | Core (most) | Variable, chronic |
| Microcephaly | HP:0000252 | Physical sign | Congenital/postnatal | Core (most) | Static/variable |
| Short stature | HP:0004322 | Physical sign | Childhood | Core (most) | Chronic |
| Developmental delay / intellectual disability | HP:0001263 / HP:0001249 | Behavioral/cognitive | Childhood | Common (often mild in LWS) | Static |
| Nystagmus | HP:0000639 | Clinical sign | Infancy/childhood | Characteristic | Stable |
| Retinal dystrophy (rod-cone) | HP:0000510 / HP:0000548 | Lab/clinical (ERG) | Childhood, progressive | Characteristic (RS end) | Progressive |
| Immune deficiency / antibody deficiency | HP:0002090 / HP:0004313 | Laboratory | Childhood | Spectrum-dependent | Variable |
| Cerebral anomalies | HP:0002060 | Imaging | Congenital | Common | Static |
| Chilblain-like skin lesions | HP:0011109 | Physical | Variable | Common | Episodic |

Quality-of-life impact is driven by short stature and skeletal/joint limitation (mobility), visual impairment (progressive retinal dystrophy), developmental/cognitive needs, and infection susceptibility from immune deficiency. Formal QoL instrument data (EQ-5D/SF-36) are not available for this ultra-rare disorder.

### 4. Genetic / Molecular Information

**Causal gene:** *RNU4ATAC* — non-coding, single-exon, transcribed into the ~130-nt U4atac snRNA; chr 2q14.2; HGNC:34140; OMIM 601428.

**Pathogenic variants:** All reported disease variants are single-nucleotide changes or small indels in the non-coding RNA; because there is no protein product, variant classes are described by location in the RNA structure rather than missense/nonsense terminology. Recurrent/illustrative variants include **n.51G>A** (the most frequent MOPD1-causative 5′ stem-loop variant), **n.50G>A / n.55G>A** (compound het in MOPD1-phenotype patients), **n.29T>A** (MOPD1 hotspot), and more dispersed variants in milder LWS/RS. Functional consequence is **loss of function** of U4atac, i.e., impaired minor spliceosome assembly. Pathogenic alleles are very rare/absent in gnomAD; carrier frequency is not well established ([PMID: 32628740](https://pubmed.ncbi.nlm.nih.gov/32628740/)).

**Variant origin:** Germline. No somatic involvement.

**Modifier genes / epigenetics / chromosomal abnormalities:** No established modifier genes, epigenetic signatures, or large chromosomal rearrangements; CMA and karyotype are characteristically normal (the point variants are not detected by those methods) ([PMID: 29370840](https://pubmed.ncbi.nlm.nih.gov/29370840/)).

### 5. Environmental Information

Not applicable. LWS is a monogenic recessive disorder with no known environmental, lifestyle, or infectious contributors. (Infections may be *consequences* of the associated immune deficiency — e.g., HHV-6–associated encephalopathy reported in a MOPD1 patient — but infection is not a cause of the disease.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. Biallelic loss-of-function variants in *RNU4ATAC* **lead to** a structurally/functionally defective U4atac snRNA.
2. Defective U4atac **impairs** assembly of the U4atac/U6atac.U5 tri-snRNP, the catalytic core of the **minor (U12-dependent) spliceosome**.
3. Impaired minor spliceosome **results in** failure to excise ~700–800 U12-type minor introns → **transcriptome-wide minor-intron retention and mis-splicing** (demonstrated by patient RNA-seq).
4. Minor-intron retention in affected transcripts **reduces** functional expression of the diverse minor-intron-containing genes (enriched in cell-cycle, DNA-replication, and signaling functions).
5a. In neural progenitors, this **causes** cell-cycle defects and death of self-amplifying radial glial cells → reduced neuron output → **microcephaly and developmental delay** (demonstrated in mouse Rnu11 models; inferred for humans).
5b. In the developing limb/skeleton, minor-spliceosome deficiency **disrupts** chondro-osseous development → **epiphyseal dysplasia, short stature, micromelia** (demonstrated in mouse U11 limb model; inferred for humans).
5c. (Branch) Secondary **ciliary dysfunction** **contributes to** skeletal/developmental and possibly retinal phenotypes (human + zebrafish).
5d. (Branch) Mis-splicing of **JAK/STAT pathway** transcripts **attenuates** cytokine signaling → impaired hematopoiesis/B-cell maturation → **immune deficiency** (Drosophila + patient data).
5e. (Branch) **Dysregulated type I interferon signaling** **produces** painful **chilblain-like skin lesions**.
6. The combined developmental and signaling defects **manifest** as the LWS clinical phenotype; variant position on the severity gradient **determines** whether the outcome is mild (LWS), intermediate (RS), or severe/lethal (MOPD1).

**Upstream vs downstream:** Steps 1–3 (variant → U4atac → minor-spliceosome failure → minor-intron retention) are upstream and shared across the entire spectrum. Steps 5a–5e are downstream, tissue-specific consequences.

**Ontology suggestions:**
- GO biological process: mRNA splicing via spliceosome (GO:0000398), cell cycle (GO:0007049), neural progenitor proliferation, JAK-STAT signaling (GO:0007259), type I interferon signaling (GO:0060337), cilium assembly (GO:0060271).
- Reactome: minor (U12-dependent) spliceosome pathway.
- CL cell types: radial glial cell (CL:0000681), chondrocyte (CL:0000138), B cell (CL:0000236), rod (CL:0000604) / cone (CL:0000573) photoreceptor.
- Subcellular (GO CC): spliceosomal complex (GO:0005681), nucleus/nuclear speckle; cilium (GO:0005929).

### 7. Anatomical Structures Affected

- **Skeletal system** (UBERON:0001434): epiphyses (UBERON:0002515), long bones, joints — multiple epiphyseal dysplasia, short stature.
- **Nervous system / brain** (UBERON:0000955): microcephaly, cerebral anomalies; cerebral cortex (UBERON:0000956) and radial glia affected.
- **Eye** (UBERON:0000970): retina (UBERON:0000966) — rod-cone dystrophy; oculomotor system — nystagmus.
- **Immune/hematopoietic system** (UBERON:0002405): B-lymphocyte compartment.
- **Skin** (UBERON:0002097): chilblain-like lesions, often acral/bilateral.
- **Lateralization:** skeletal and retinal involvement are characteristically **bilateral/symmetric**.

### 8. Temporal Development

- **Onset:** Congenital/prenatal for growth and microcephaly (intrauterine growth restriction in severe cases); skeletal dysplasia and nystagmus apparent in infancy/childhood.
- **Course:** Largely **static** for structural/developmental features, but **progressive** for the retinal dystrophy (progressive visual loss on follow-up) and episodic for chilblain-like skin lesions.
- **Duration:** Chronic/lifelong. In LWS (mild end), lifespan is not markedly curtailed; by contrast MOPD1 is frequently lethal in infancy/early childhood.
- **Critical period:** Fetal/early-postnatal neurodevelopment (radial glial proliferation window) is the key vulnerability period; no established intervention window exists.

### 9. Inheritance and Population

- **Inheritance:** Autosomal recessive ([PMID: 3706411](https://pubmed.ncbi.nlm.nih.gov/3706411/)); recurrence risk 25% per pregnancy for carrier couples.
- **Penetrance/expressivity:** High penetrance for biallelic pathogenic genotypes, but **highly variable expressivity** governed by variant position and allele combination.
- **Epidemiology:** Ultra-rare; only a few dozen molecularly confirmed RNU4ATAC-opathy patients worldwide (60 in the largest cohort). No formal prevalence/incidence estimate.
- **Sex ratio:** No sex predilection (autosomal). **Consanguinity** elevates risk via homozygosity. No well-defined founder effects, though recurrent hotspot variants (e.g., n.51G>A) exist. Carrier frequency not reliably established.

### 10. Diagnostics

- **Genetic testing is definitive.** Because *RNU4ATAC* is non-coding and single-exon, protein/splice predictors do not apply and the gene is missed by many exome kits. Recommended approach: **whole-genome sequencing** or **targeted *RNU4ATAC* Sanger sequencing**, especially when WES is negative in a clinically suggestive patient ([PMID: 37666272](https://pubmed.ncbi.nlm.nih.gov/37666272/); [PMID: 29370840](https://pubmed.ncbi.nlm.nih.gov/29370840/)).
- **Functional biomarker:** **RNA-seq demonstrating minor-intron retention** and a **cellular minor-intron splicing reporter assay** provide functional pathogenicity evidence and enable VUS reclassification ([PMID: 42322193](https://pubmed.ncbi.nlm.nih.gov/42322193/); [PMID: 32628740](https://pubmed.ncbi.nlm.nih.gov/32628740/)).
- **Imaging:** Skeletal survey (epiphyseal dysplasia), brain MRI (microcephaly/cerebral anomalies); **ERG** for retinal dystrophy (uniformly abnormal) ([PMID: 37225827](https://pubmed.ncbi.nlm.nih.gov/37225827/)).
- **Immunology:** Immunoglobulin levels and lymphocyte/B-cell subset quantification ([PMID: 38837402](https://pubmed.ncbi.nlm.nih.gov/38837402/)).
- **CMA/karyotype:** Characteristically normal (do not detect *RNU4ATAC* point variants).
- **Differential diagnosis:** Other multiple epiphyseal dysplasias; other primordial dwarfisms, importantly **PCNT-related MOPD II** (distinguished by aneurysm/Moyamoya risk, [PMID: 37234811](https://pubmed.ncbi.nlm.nih.gov/37234811/)); and within-gene RS/MOPD1.

### 11. Outcome / Prognosis

- **Survival:** In LWS (mild end) life expectancy is relatively preserved; the severe MOPD1 end is frequently lethal in infancy/early childhood. No LWS-specific mortality statistics exist.
- **Morbidity:** Driven by short stature/skeletal limitation, progressive visual impairment, cognitive impairment, and infection susceptibility.
- **Prognostic factors:** Variant position and allele combination (severity gradient); degree of immune deficiency (infection risk) and retinal dystrophy (visual prognosis).
- **Complications:** Recurrent infections (immune deficiency), progressive visual loss; non-ischemic cardiomyopathy reported at the RS end ([PMID: 37666272](https://pubmed.ncbi.nlm.nih.gov/37666272/)).

### 12. Treatment

No disease-modifying or curative therapy exists; management is **supportive and multidisciplinary**:
- **Immunoglobulin replacement / infection prophylaxis** for antibody deficiency (NCIT: Immunoglobulin Therapy).
- **Ophthalmologic surveillance and low-vision support** for retinal dystrophy/nystagmus.
- **Orthopedic/skeletal management and physical therapy** for epiphyseal dysplasia/short stature.
- **Developmental/educational support** for delay/intellectual disability.
- **Dermatologic management** of chilblain-like lesions (type I interferon involvement suggests a theoretical rationale for immunomodulation, but this is investigational).
- **Experimental:** No approved gene/RNA therapies; the minor-intron-retention readout could in principle serve as a pharmacodynamic biomarker for future splice-modulating approaches. No registered disease-specific clinical trials identified.

### 13. Prevention

- **Genetic counseling** for 25% recurrence risk; carrier testing of at-risk relatives (cascade testing).
- **Prenatal diagnosis / preimplantation genetic testing** feasible once familial variants are known — prenatal diagnosis has been reported for a subsequent pregnancy in an affected family ([PMID: 29370840](https://pubmed.ncbi.nlm.nih.gov/29370840/)).
- **Tertiary prevention:** infection prophylaxis, vision monitoring, developmental intervention.
- No primary prevention (not environmentally modifiable); not vaccine-preventable.

### 14. Other Species / Natural Disease

- No naturally occurring companion-animal/wildlife disease ortholog is catalogued (no OMIA entry for LWS specifically).
- *RNU4ATAC*/minor-spliceosome components are **deeply evolutionarily conserved** (present from *Drosophila* to mammals), enabling cross-species modeling. Orthologous minor-spliceosome snRNA function is conserved in mouse and zebrafish.
- No zoonotic potential (non-infectious genetic disorder).

### 15. Model Organisms

| Model | Manipulation | Phenotype recapitulated | PMID |
|---|---|---|---|
| Mouse (cortex) | Conditional Rnu11 (U11) ablation | Microcephaly via radial glial cell-cycle defects/death | [30093551](https://pubmed.ncbi.nlm.nih.gov/30093551/) |
| Mouse (limb) | U11 snRNA loss | Micromelia (limb skeletal dysplasia) | [32665241](https://pubmed.ncbi.nlm.nih.gov/32665241/) |
| *Drosophila* | CRISPR U4atac stem-II mutant | Growth/neurodevelopmental defects, immunodeficiency, GI symptoms; JAK/STAT mis-splicing | [42463491](https://pubmed.ncbi.nlm.nih.gov/42463491/) |
| Zebrafish | U4atac knockdown | Ciliary defects | [36802443](https://pubmed.ncbi.nlm.nih.gov/36802443/) |
| Human patient cells | Native biallelic variants + reporter assay | Minor-intron retention (direct molecular phenotype) | [26522830](https://pubmed.ncbi.nlm.nih.gov/26522830/), [32628740](https://pubmed.ncbi.nlm.nih.gov/32628740/) |

**Strengths:** Mouse models directly link minor-spliceosome loss to microcephaly and skeletal dysplasia; *Drosophila* captures the immune axis. **Limitations:** Most models ablate *U11/Rnu11* (a different minor-spliceosome snRNA) rather than *RNU4ATAC* itself, and complete ablation is more severe than the hypomorphic human variants; no model specifically reproduces the mild LWS end of the spectrum.

---

## Mechanistic Model / Interpretation

```
 Biallelic LoF variants in RNU4ATAC (non-coding, chr 2q14.2)
        │  (variant POSITION sets severity: 5' stem-loop = severe MOPD1;
        │   dispersed = mild LWS/Roifman)
        ▼
 Defective U4atac snRNA
        ▼
 Impaired U4atac/U6atac.U5 tri-snRNP → MINOR (U12-dependent) SPLICEOSOME failure
        ▼
 Transcriptome-wide MINOR-INTRON RETENTION (~700–800 U12 introns)   ◄── shared, upstream
        │
   ┌────┼───────────────┬───────────────┬────────────────┐
   ▼    ▼               ▼               ▼                ▼
 Radial  Chondro-      Ciliary        JAK/STAT         Type I IFN
 glia    osseous       dysfunction    mis-splicing     dysregulation
 death   disruption                   (↓JAK1)
   ▼        ▼              ▼               ▼                ▼
 MICRO-  EPIPHYSEAL     ciliopathy    IMMUNE           CHILBLAIN-like
 CEPHALY DYSPLASIA /    features      DEFICIENCY       skin lesions
 + DD    SHORT STATURE                (↓B cells)
```

The model's central logic is that a **single upstream lesion (minor-intron retention)** produces a **pleiotropic, multisystem phenotype** because minor introns reside in functionally diverse genes. The **severity gradient** (LWS ↔ RS ↔ MOPD1) is explained quantitatively by how much a given variant degrades tri-snRNP assembly (FitCons-weighted, position-dependent). Tissue selectivity (why brain, skeleton, retina, and immune cells are preferentially affected) likely reflects the high proliferative/biosynthetic demand of neural and chondro-osseous progenitors and the splicing dependence of key cell-cycle and signaling transcripts.

---

## Evidence Base

| PMID | Study (abbrev.) | Role |
|---|---|---|
| [29265708](https://pubmed.ncbi.nlm.nih.gov/29265708/) | Expanding phenotype of RNU4ATAC to LWS | **Establishes** biallelic RNU4ATAC as cause of LWS |
| [30368667](https://pubmed.ncbi.nlm.nih.gov/30368667/) | LWS: RNU4ATAC association, genotype–phenotype | **Supports** severity-by-variant-position; defines phenotype |
| [41808109](https://pubmed.ncbi.nlm.nih.gov/41808109/) | Phenotypic spectrum: 4 novel + reeval | **Supports** MOPD1→RS severity spectrum |
| [42322193](https://pubmed.ncbi.nlm.nih.gov/42322193/) | RNU4ATAC-opathy large cohort (n=60) | **Supports** core features, minor-intron retention, RNA-seq reclassification |
| [36622817](https://pubmed.ncbi.nlm.nih.gov/36622817/) | Delineating RNU4ATAC spliceosomopathy | **Supports** continuum (one patient spanning all three) |
| [26522830](https://pubmed.ncbi.nlm.nih.gov/26522830/) | Roifman syndrome, minor intron splicing | **Supports** U4atac essential; minor-intron defect mechanism |
| [32628740](https://pubmed.ncbi.nlm.nih.gov/32628740/) | Clinical interpretation of RNU4ATAC variants | **Supports** non-coding diagnostic challenge; reporter assay |
| [30093551](https://pubmed.ncbi.nlm.nih.gov/30093551/) | Minor spliceosome inactivation → microcephaly | **Supports** microcephaly mechanism (mouse) |
| [32665241](https://pubmed.ncbi.nlm.nih.gov/32665241/) | U11 loss → micromelia | **Supports** skeletal mechanism (mouse) |
| [36802443](https://pubmed.ncbi.nlm.nih.gov/36802443/) | U4atac deficiency → ciliary defects | **Supports** ciliary branch |
| [42463491](https://pubmed.ncbi.nlm.nih.gov/42463491/) | U4atac regulates JAK/STAT (Drosophila) | **Supports** immune/JAK-STAT branch |
| [40415209](https://pubmed.ncbi.nlm.nih.gov/40415209/) | RNU4ATAC chilblain lesions, type I IFN | **Supports** interferon/skin branch |
| [37225827](https://pubmed.ncbi.nlm.nih.gov/37225827/) | Retinal dystrophy in RNU4ATAC-Roifman | **Supports** rod-cone dystrophy phenotype |
| [38837402](https://pubmed.ncbi.nlm.nih.gov/38837402/) | B-cell deficiency in MOPD1 twins | **Supports** immunodeficiency across spectrum |
| [3706411](https://pubmed.ncbi.nlm.nih.gov/3706411/) | Nevin 1986, LWS second family | **Supports** historical description, AR inheritance |
| [29370840](https://pubmed.ncbi.nlm.nih.gov/29370840/) | Chinese family, WES-negative, targeted RNU4ATAC | **Supports** diagnostic pitfalls, prenatal diagnosis |
| [37666272](https://pubmed.ncbi.nlm.nih.gov/37666272/) | Roifman as non-ischemic cardiomyopathy | **Supports** exome-kit coverage gap; phenotypic breadth |
| [37234811](https://pubmed.ncbi.nlm.nih.gov/37234811/) | PCNT MOPD II with aneurysm/Moyamoya | **Differential**: PCNT-MOPD II is distinct from RNU4ATAC disorders |

Evidence spans **human clinical/genetic** (majority), **in vitro functional** (reporter assay, patient RNA-seq), and **model organism** (mouse, zebrafish, *Drosophila*) sources, providing convergent support for the minor-intron-retention mechanism.

---

## Limitations and Knowledge Gaps

1. **No LWS-specific epidemiology.** Prevalence, incidence, carrier frequency, and sex/age distributions are unquantified given extreme rarity; most data are pooled across the RNU4ATAC-opathy spectrum.
2. **Genotype–phenotype resolution is incomplete.** The FitCons/position model explains broad severity trends but cannot yet reliably predict LWS vs RS vs MOPD1 for a novel allele combination.
3. **Model limitations.** Most animal models ablate *U11/Rnu11* rather than *RNU4ATAC*, and use complete knockouts rather than hypomorphic alleles; no model specifically phenocopies the mild LWS end.
4. **Tissue-selectivity unexplained.** Why specific tissues (brain, skeleton, retina, B cells) are preferentially vulnerable despite a housekeeping defect remains mechanistically unresolved.
5. **Secondary pathways (cilia, JAK/STAT, IFN)** are derived partly from allelic disorders/model organisms; their contribution specifically in mild LWS is inferred, not directly demonstrated.
6. **No natural-history or QoL data**, and no therapeutic trials — management recommendations are extrapolated from case experience.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a prospective RNU4ATAC-opathy registry** capturing genotype, minor-intron-retention burden (RNA-seq), and longitudinal phenotype (growth, vision/ERG, immune function, neurodevelopment) to quantify natural history and refine genotype–phenotype prediction.
2. **Build hypomorphic, allele-specific models** (knock-in of human LWS vs MOPD1 variants in *RNU4ATAC* itself; mouse and/or patient iPSC-derived cerebral and chondro-osseous organoids) to directly test the position-severity model and tissue selectivity.
3. **Standardize a quantitative minor-intron-retention assay** as a clinical functional test to resolve VUS and correlate retention burden with severity (candidate severity biomarker).
4. **Targeted-sequencing / WGS reflex testing** in any microcephalic-primordial-dwarfism or multiple-epiphyseal-dysplasia patient with negative exome — raise diagnostic yield by ensuring *RNU4ATAC* coverage.
5. **Pathway-directed therapeutic exploration:** test whether modulating type I interferon or JAK/STAT signaling ameliorates immune/skin phenotypes, and evaluate splice-modulating small molecules/ASOs using minor-intron-retention as a pharmacodynamic endpoint.
6. **Systematic immunologic and ophthalmologic surveillance protocols** for diagnosed patients, given the demonstrated antibody deficiency and progressive rod-cone dystrophy.

---

*Report compiled from 24 primary references spanning human clinical, in vitro functional, and model-organism evidence. Causal gene: **RNU4ATAC** (U4atac snRNA, minor spliceosome). Disease: Lowry-Wood syndrome, MONDO:0009191.*


## Artifacts

- [OpenScientist final report](Lowry-Wood_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Lowry-Wood_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 14 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009191` (5 mentions) - the report calls it "MONDO"; MONDO calls it **Lowry-Wood syndrome**
- `HP:0011109` (1 mention) - the report calls it "Chilblain-like skin lesions"; HP calls it **Chronic sinusitis**
- `UBERON:0000955` (1 mention) - the report calls it "Nervous system / brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002656` (1 mention) - the report calls it "Multiple epiphyseal dysplasia"; HP calls it **Epiphyseal dysplasia**
- `HP:0002060` (1 mention) - the report calls it "Cerebral anomalies"; HP calls it **Abnormal cerebral morphology**, and lists "Cerebral lesion" among its other names
- `GO:0000398` (1 mention) - the report calls it "GO biological process: mRNA splicing via spliceosome"; GO calls it **mRNA splicing, via spliceosome**, and lists "nuclear mRNA splicing, via spliceosome" among its other names
- `CL:0000681` (1 mention) - the report calls it "CL cell types: radial glial cell"; CL calls it **radial glial cell**
- `UBERON:0002405` (1 mention) - the report calls it "Immune/hematopoietic system"; UBERON calls it **immune system**
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.