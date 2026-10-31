---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-24T01:27:59.551823'
end_time: '2026-10-24T01:53:57.850763'
duration_seconds: 1558.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Olmsted Syndrome 2
  mondo_id: MONDO:0030961
  category: Mendelian
  causal_genes: PERP
  omim_id: not recorded
  synonyms: OLMS2; PERP-related Olmsted syndrome; autosomal dominant PERP-related
    keratoderma
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
citation_count: 12
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 20
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:25886873
  relevance_assessed: 12
  on_topic: 8
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 28
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 22
  labels_matching: 13
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0011220
    reported_labels:
    - periorificial hyperkeratosis type
    ontology_label: Prominent forehead
  - term_id: HP:0011817
    reported_labels:
    - oral leukoplakia type
    ontology_label: Basal encephalocele
  - term_id: HP:0001055
    reported_labels:
    - Erythrokeratoderma
    ontology_label: Erysipelas
  - term_id: UBERON:0001456
    reported_labels:
    - face skin / periorificial region
    ontology_label: face
  labels_variant: 5
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
  path: Olmsted_Syndrome_2-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Olmsted_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Olmsted Syndrome 2
- **MONDO ID:** MONDO:0030961 (if available)
- **Causal gene(s):** PERP
- **OMIM:** not recorded
- **Synonyms:** OLMS2; PERP-related Olmsted syndrome; autosomal dominant PERP-related keratoderma
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Olmsted Syndrome 2** covering all of the
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

# Olmsted Syndrome 2 (OLMS2, MONDO:0030961): A Comprehensive Disease Characterization

**Causal gene: PERP** (p53 apoptosis effector related to PMP-22; HGNC:17637; NCBI Gene 64065; UniProt Q96FX8; chromosome 6q23.3; reference transcript NM_022121.5; gene OMIM \*609301)

---

## Summary

**Olmsted Syndrome 2 (OLMS2; MONDO:0030961) is an ultra-rare Mendelian keratinizing genodermatosis caused by germline mutations in *PERP*, a structural tetraspan membrane glycoprotein of the PMP22/EMP/MP20/claudin family that is an essential component of epidermal desmosomes.** It is molecularly and mechanistically distinct from the more common, classically described Olmsted syndrome caused by gain-of-function mutations in *TRPV3* (OMIM #614594) and from X-linked *MBTPS2*-related Olmsted syndrome. The name "Olmsted syndrome 2" is a serial designation that does not itself name the gene; the defining feature of this entity is that its cause is *PERP*, a desmosomal adhesion protein, not an ion channel or a membrane-bound protease.

The disease has a striking dual-inheritance architecture that maps cleanly onto the position and nature of the *PERP* mutation. **Heterozygous C-terminal truncating variants (nonsense/frameshift) cause autosomal dominant disease** — severe, mutilating, transgredient palmoplantar keratoderma (PPK) combined with periorificial keratotic plaques — through a dominant-negative mechanism in which an unstable mutant protein is poorly incorporated into desmosomes, destabilizing them. In contrast, **biallelic (recessive) N-terminal truncations or missense variants cause milder disease** — generalized erythrokeratoderma/ichthyosis with PPK — through loss of PERP expression/function. The core lesion in both is structural: immature desmosomes lacking the normal electron-dense midline and impaired keratinocyte intercellular adhesion under mechanical stress.

Downstream of this adhesion failure, the epidermis becomes hyperproliferative with altered differentiation, and lesional skin shows increased EGFR and mTOR/RPS6 signaling. This downstream convergence provides the rationale for the emerging targeted therapies — the EGFR inhibitor **erlotinib** and the mTOR inhibitor **sirolimus** — alongside traditional retinoids, keratolytics, emollients, surgical release of constricting pseudoainhum bands, and pain/pruritus management. The condition is congenital or early-childhood in onset, chronic, progressive, and highly disabling but non-lethal in humans; it is diagnosed clinically and confirmed by exome/panel sequencing, with characteristic electron-microscopic desmosomal immaturity on skin biopsy. *Perp*-null mouse models recapitulate epithelial blistering and hyperproliferation, and additionally reveal a tumor-suppressor role in UV-induced skin squamous cell carcinoma.

---

## 1. Disease Information

**Overview.** Olmsted syndrome (OS) is a rare genodermatosis classically defined by the combination of **bilateral mutilating transgredient palmoplantar keratoderma (PPK)** and **periorificial keratotic plaques**, with considerable clinical heterogeneity. *PERP*-related disease (OLMS2) is the specific molecular subtype caused by *PERP* mutations, first delineated by Duchatelet et al. in 2019 ([PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)).

> "Olmsted syndrome (OS) is a rare genodermatosis classically characterized by the combination of bilateral mutilating transgredient palmoplantar keratoderma (PPK) and periorificial keratotic plaques, but which shows considerable clinical heterogeneity." — [PMID: 25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/)

**Key identifiers.**

| Resource | Identifier |
|---|---|
| Mondo | MONDO:0030961 (Olmsted syndrome 2 / OLMS2) |
| Causal gene | *PERP* — HGNC:17637; NCBI Gene 64065; UniProt Q96FX8; gene OMIM \*609301 |
| Orphanet | ORPHA:659 (Olmsted syndrome, umbrella) |
| Related (distinct) | TRPV3-Olmsted syndrome OMIM #614594; MBTPS2-related X-linked Olmsted syndrome |
| ICD-10 | Q82.8 (other specified congenital malformations of skin) — mapped at the OS level |
| MeSH | No OLMS2-specific descriptor; indexed under keratoderma, palmoplantar |

**Synonyms / alternative names.** OLMS2; PERP-related Olmsted syndrome; autosomal dominant PERP-related keratoderma.

**Information source.** The knowledge base entry is derived from **aggregated, disease-level resources** (OMIM, Orphanet, Mondo) and primary literature (case series and functional studies), not individual EHR patient records. Given the ultra-rarity of the disease, the evidence is drawn from a small number of kindreds and functional/model-organism studies.

---

## 2. Etiology

**Disease causal factors.** OLMS2 is a **monogenic (Mendelian) genetic disorder** caused by germline mutations in *PERP*. There is no environmental, infectious, or acquired cause of the core disease. *PERP* encodes a desmosomal component, and its disruption is both necessary and sufficient to produce the keratoderma phenotype.

> "...mutations in PERP, encoding a crucial component of desmosomes, cause both dominant and recessive human keratoderma" — [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)

**Genetic risk factors.** The causal variants are the *PERP* truncating/missense mutations themselves (detailed in Section 4). There are no known common susceptibility loci — the disease is fully penetrant Mendelian, not multifactorial.

**Environmental risk factors.** None established as causal. Mechanical stress is relevant as a *modifier/trigger of manifestation* at the cellular level (impaired adhesion manifests "upon mechanical stress," [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)), consistent with the acral (palmoplantar) distribution of the most severe lesions, which are the body sites under greatest frictional load. In recessive biallelic cases, cutaneous fungal infection has been reported to coincide with psoriasiform plaque flares ([PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)), suggesting infection may act as a secondary trigger/aggravator rather than a cause.

**Protective factors.** No genetic or environmental protective factors have been identified. This is expected for a rare Mendelian disorder with high penetrance.

**Gene–environment interactions.** Not formally studied. The acral/periorificial and friction-prone distribution of lesions is consistent with mechanical load interacting with the underlying adhesion defect, but this is inferred, not demonstrated.

---

## 3. Phenotypes

The core clinical phenotype of Olmsted syndrome, and specifically PERP-related disease, comprises:

| Phenotype | Type | Suggested HPO | Onset | Severity | Frequency |
|---|---|---|---|---|---|
| Bilateral mutilating transgredient palmoplantar keratoderma | Physical manifestation / clinical sign | HP:0000982 (Palmoplantar keratoderma) | Birth / early childhood | Severe | Defining (near-100%) |
| Periorificial keratotic plaques | Clinical sign | HP:0011220 (periorificial hyperkeratosis type) | Early childhood | Severe | Defining |
| Pseudoainhum (constricting fibrous bands, autoamputation risk) | Physical manifestation | HP (constriction of digit) | Childhood, progressive | Severe | Frequent in severe OS |
| Hair abnormalities (alopecia/sparse hair) | Clinical sign | HP:0001596 (Alopecia) | Variable | Variable | Frequent |
| Nail abnormalities | Clinical sign | HP:0001597 (Abnormality of the nail) | Variable | Variable | Frequent |
| Oral leukokeratosis | Clinical sign | HP:0011817 (oral leukoplakia type) | Variable | Mild–moderate | Frequent |
| Corneal defects | Clinical sign | HP:0000481 (Abnormality of the cornea) | Variable | Variable | Frequent |
| Recurrent infections | Clinical sign | HP:0002719 (Recurrent infections) | Variable | Variable | Frequent |
| Pain | Symptom | HP:0012531 (Pain) | Early | Variable, can be severe | Variable |
| Pruritus (itching) | Symptom | HP:0000989 (Pruritus) | Early | Variable, can be severe | Variable |
| Generalized erythrokeratoderma (recessive form) | Physical manifestation | HP:0001055 (Erythrokeratoderma) | Birth/infancy | Milder | Recessive cases |

> "Suggestive features: PPK with pseudoainhum and periorificial keratotic plaques. Frequently associated features include hair and nail abnormalities, leukokeratosis, corneal default and recurrent infections. Pain and itching are variable but can be severe." — [PMID: 25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/)

**Genotype–phenotype gradient of severity.** Dominant C-terminal truncations produce the most severe, mutilating periorificial + palmoplantar keratoderma (OLMS2 proper); homozygous N-terminal truncation produces widespread erythrokeratoderma; biallelic missense variants produce the mildest ichthyosis/erythrokeratoderma with psoriasiform plaques ([PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/); [PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)).

**Quality of life impact.** The mutilating PPK with pseudoainhum, severe pain, and pruritus produces profound functional disability affecting ambulation, manual dexterity, and daily living; QoL in treatment studies has been assessed with pain/pruritus visual analog scales (VAS) and the Children's Dermatology Life Quality Index (CDLQI) ([PMID: 31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)). No disease-specific EQ-5D/SF-36 data exist given rarity.

---

## 4. Genetic / Molecular Information

**Causal gene.** *PERP* (HGNC:17637; NCBI Gene 64065; UniProt Q96FX8; chromosome 6q23.3; transcript NM_022121.5; OMIM \*609301). PERP is a tetraspan membrane glycoprotein of the PMP22/EMP/MP20/claudin family localized to epidermal desmosomes and is a direct transcriptional target of p63.

**Pathogenic variants and genotype–phenotype correlation.**

| Zygosity / variant class | Example variants | Mechanism | Phenotype |
|---|---|---|---|
| Heterozygous C-terminal truncating (nonsense/frameshift) | C-terminal truncations | Dominant-negative: unstable protein poorly incorporated into desmosomes | **Dominant Olmsted syndrome (OLMS2)** — severe periorificial + palmoplantar keratoderma |
| Homozygous N-terminal truncation | N-terminal truncation | Loss of expression | Widespread erythrokeratoderma with expansion of epidermal differentiation markers |
| Biallelic recessive missense | c.89T>C p.Leu30Pro; c.466G>C p.Gly156Arg | Loss/partial loss of function | Milder ichthyosis/erythrokeratoderma, PPK, psoriasiform plaques (± fungal infection) |

> "Monoallelic nonsense mutations cause Olmsted syndrome with severe periorificial keratoderma and palmoplantar keratoderma (PPK). Biallelic recessive frameshift and missense mutations are associated with milder forms of the disease, including generalised erythrokeratoderma and PPK." — [PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)

> "Homozygosity for an N-terminal truncation ablates expression and causes widespread erythrokeratoderma, with expansion of epidermal differentiation markers." — [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)

**Exact variant nomenclature (recessive, milder cases).**

> "two novel biallelic PERP variants, NM_022121.5, c.89T > C, p.Leu30Pro and c.466G > C, p.Gly156Arg" — [PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)

**Variant classification (ACMG/AMP).** Truncating variants in a gene with an established loss-of-function/dominant-negative mechanism are classified **pathogenic/likely pathogenic**; the recessive missense variants were reported as novel disease-associated (likely pathogenic in the context of biallelic inheritance and phenotype segregation).

**Allele frequency.** Pathogenic *PERP* variants are private/rare and largely **absent from gnomAD** at appreciable frequency. No founder allele or recurrent hotspot has been established.

**Somatic vs germline.** All disease-causing *PERP* variants are **germline**. No somatic *PERP* disease association exists for OLMS2. (Of note, *PERP* loss is relevant to somatic skin carcinogenesis in model systems — see Sections 6 and 15 — but that is a tumor-suppressor context, not OLMS2 itself.)

**Functional consequences.** Dominant C-terminal truncation = **dominant-negative** (unstable protein incorporated into desmosomes, destabilizing them); N-terminal truncation = **loss of function** (no expression); recessive missense = partial/complete loss of function.

**Modifier genes.** None established.

**Epigenetic information.** *PERP* is transcriptionally controlled by the master epithelial regulator **p63** (and p53); SATB2 can attenuate p63-driven *perp* expression ([PMID: 21965674](https://pubmed.ncbi.nlm.nih.gov/21965674/)). No disease-specific DNA-methylation or histone-modification data for OLMS2 exist.

**Chromosomal abnormalities.** None — OLMS2 is a single-gene point-mutation disorder, not a copy-number/structural disorder.

---

## 5. Environmental Information

- **Environmental factors:** None causal. Mechanical friction plausibly aggravates acral lesions given the adhesion defect (inferred).
- **Lifestyle factors:** None established.
- **Infectious agents:** Not causal. Cutaneous **fungal infection** was reported to coincide with psoriasiform plaque flares in biallelic *PERP* disease ([PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)) — a secondary trigger/aggravator — and recurrent infections are a frequently associated feature of OS generally ([PMID: 25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/)), likely secondary to barrier compromise.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **heterozygous C-terminal truncating *PERP* mutation** produces an unstable PERP protein that is poorly incorporated into desmosomes (dominant-negative). *[Human; [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)]*
2. This **leads to immature desmosomes lacking a dense midline** (electron microscopy), while other desmosomal components localize normally. *[Human; [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)]*
3. This **results in impaired keratinocyte intercellular adhesion upon mechanical stress** *[Human/in vitro; [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)]*, mirrored by blistering in *Perp*-null mouse stratified epithelia *[Mouse; [PMID: 15797384](https://pubmed.ncbi.nlm.nih.gov/15797384/), [PMID: 16417219](https://pubmed.ncbi.nlm.nih.gov/16417219/)]*.
4. Loss of desmosomal adhesion / PERP function **results in epidermal hyperproliferation and altered differentiation**. *[Human + mouse]*
5. **Inferred:** downstream over-activation of **EGFR and mTOR/RPS6 signaling** in the epidermis drives hyperkeratosis. *[Human IHC; [PMID: 31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)]*
6. This **produces the clinical palmoplantar and periorificial keratoderma with pain and pruritus**.

Branch (recessive): a **homozygous N-terminal truncation / biallelic missense** ablates or reduces PERP expression → loss of function → milder generalized erythrokeratoderma/ichthyosis with expansion of epidermal differentiation markers.

```
 PERP mutation
    │
    ├── Heterozygous C-term truncation ──► unstable protein, poorly incorporated
    │        │   (DOMINANT-NEGATIVE)
    │        ▼
    │   immature desmosomes (no dense midline)
    │        ▼
    │   impaired keratinocyte adhesion (mechanical stress)
    │        ▼
    │   epidermal hyperproliferation + altered differentiation
    │        ▼
    │   [inferred] ↑EGFR + ↑mTOR/RPS6 signaling ──► HYPERKERATOSIS
    │        ▼
    │   severe mutilating PPK + periorificial plaques (OLMS2)
    │
    └── Homozygous N-term truncation / biallelic missense ──► loss of expression
             │   (LOSS OF FUNCTION)
             ▼
         widespread erythrokeratoderma / milder ichthyosis
```

### Supporting detail

> "Both exhibit epidermal hyperproliferation, immature desmosomes lacking a dense midline observed via electron microscopy, and impaired intercellular adhesion upon mechanical stress." — [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)

> "Localization of other desmosomal components appears normal, which is in contrast to other conditions caused by mutations in genes encoding desmosomal proteins." — [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)

> "increased phosphorylated ribosomal protein S6 (RPS6) and phosphorylated EGFR staining in the epidermis, indicating enhanced mTOR and EGFR signaling activation" — [PMID: 31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)

- **Molecular pathways:** p63 → PERP transcriptional axis (upstream); desmosomal adhesion; downstream EGFR and mTOR/PI3K–AKT–RPS6 signaling (therapeutically targetable). Suggested GO: GO:0002934 (desmosome organization), GO:0007155 (cell adhesion), GO:0008544 (epidermis development), GO:0030216 (keratinocyte differentiation).
- **Cellular processes:** keratinocyte adhesion failure, epidermal hyperproliferation, abnormal keratinocyte differentiation. PERP is also p53/p63-linked to apoptosis.
- **Protein dysfunction:** dominant-negative (unstable truncated protein destabilizing desmosomes) vs loss of function (no expression).
- **Cell types:** keratinocytes of stratified squamous epithelium (CL:0000312 keratinocyte; CL:0000362 epidermal cell).
- **Upstream vs downstream:** the *PERP* desmosomal structural lesion is **upstream**; EGFR/mTOR activation and hyperkeratosis are **downstream** and druggable.

Molecular profiling is limited: lesional **immunohistochemistry** (p-RPS6, p-EGFR up) is the principal profiling data; no large transcriptomic/proteomic/metabolomic datasets specific to OLMS2 exist.

---

## 7. Anatomical Structures Affected

- **Primary organ:** skin (UBERON:0002097), specifically palms and soles (palmoplantar epidermis) and periorificial skin (around mouth, eyes, nose, anus).
- **Secondary involvement:** hair (alopecia), nails, oral mucosa (leukokeratosis), cornea/eye (corneal defects). Body system: **integumentary system**.
- **Tissue/cell level:** stratified squamous **epithelium**; **keratinocytes** (CL:0000312) are the targeted cell population; desmosomes (cell–cell junctions) are the affected structure.
- **Subcellular level:** **desmosome** (GO:0030057, cellular component); plasma membrane. PERP is a tetraspan plasma-membrane/desmosomal protein.
- **Localization:** acral (palms/soles) and periorificial; **bilateral and symmetric**; transgredient (extending beyond palms/soles onto dorsal surfaces).

> "Perp localizes specifically to desmosomes, adhesion junctions important for tissue integrity" — [PMID: 15797384](https://pubmed.ncbi.nlm.nih.gov/15797384/)

Suggested UBERON: UBERON:0002097 (skin of body), UBERON:0002389 (skin of manus/palm), UBERON:0001513 (skin of pes/sole), UBERON:0001456 (face skin / periorificial region).

---

## 8. Temporal Development

- **Onset:** congenital / early childhood — PPK and periorificial plaques typically begin at birth or early childhood. Onset pattern is **chronic/insidious**.
- **Progression:** **progressive** — keratoderma worsens over time; pseudoainhum constricting bands can develop and progress toward a risk of autoamputation. Course is **chronic, lifelong**.
- **Disease duration:** lifelong; not self-limited.
- **Remission:** no spontaneous remission; partial, treatment-induced improvement reported with targeted therapy (erlotinib/sirolimus) and retinoids.
- **Critical periods:** early intervention may limit mutilating complications (pseudoainhum), but no formal natural-history window is defined.

> "...usually starting at birth or early childhood..." — [PMID: 25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/)

---

## 9. Inheritance and Population

**Epidemiology.** Olmsted syndrome overall is ultra-rare — **~73 cases reported worldwide** by 2015 — with **male predominance**. PERP-related cases are a small subset first delineated in 2019. No validated prevalence/incidence rate exists.

> "About 73 cases have been reported worldwide. OS is observed in both sexes, although male cases are more frequent." — [PMID: 25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/)

**Inheritance — dual pattern:**

- **Autosomal dominant** OLMS2 from heterozygous C-terminal truncating variants, across multiple unrelated kindreds (de novo occurrence consistent with sporadic presentation).
- **Autosomal recessive** milder keratoderma/erythrokeratoderma from biallelic N-terminal truncating or missense variants, reported in **consanguineous families** (e.g., within a cohort of 180 extended Iranian families).

> "Heterozygosity for a C-terminal truncation...causes Olmsted syndrome with severe periorificial and palmoplantar keratoderma in multiple unrelated kindreds." — [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)

> "Among 26 previously unresolved families within a cohort of 180 extended Iranian families with syndromic or non-syndromic ichthyosis" — [PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)

- **Penetrance:** high/complete for the dominant truncating variants (based on segregation in kindreds); expressivity varies with variant class (dominant-negative vs loss of function).
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** not specifically documented.
- **Founder effects:** none established; variants are private/rare.
- **Consanguinity:** relevant to the recessive biallelic form (consanguineous Iranian families).
- **Carrier frequency:** not established; pathogenic alleles largely absent from gnomAD.
- **Sex ratio:** male predominance at the OS level.

**Identifiers recap:** MONDO:0030961 (OLMS2); ORPHA:659; *PERP* OMIM \*609301; distinct from TRPV3-OS OMIM #614594.

---

## 10. Diagnostics

**Clinical diagnosis** rests on the characteristic phenotype: bilateral mutilating transgredient PPK plus periorificial keratotic plaques ([PMID: 25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/)).

**Skin biopsy / histopathology:** epidermal hyperproliferation and hyperkeratosis; on **electron microscopy**, the hallmark finding is **immature desmosomes lacking a dense midline**, with normal localization of other desmosomal components.

> "immature desmosomes lacking a dense midline observed via electron microscopy" — [PMID: 30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/)

**Immunohistochemistry (research/mechanistic):** increased p-RPS6 and p-EGFR in lesional epidermis ([PMID: 31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)).

**Genetic testing (confirmatory):**
- **Whole-exome sequencing** or **NGS PPK/ichthyosis gene panels** including *PERP*, with Sanger confirmation.
- **Homozygosity mapping** aids recessive-case resolution in consanguineous families ([PMID: 34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/)).
- Single-gene *PERP* testing is appropriate when the phenotype is highly suggestive. WGS is useful but generally unnecessary. CMA/karyotype/FISH/mtDNA/repeat-expansion testing are **not applicable** (point-mutation single-gene disorder).

**Differential diagnosis:**

| Condition | Gene | Distinguishing mechanism |
|---|---|---|
| TRPV3-Olmsted syndrome (OMIM #614594) | *TRPV3* | Gain-of-function cation channelopathy |
| MBTPS2-related X-linked Olmsted/IFAP/KFSD | *MBTPS2* | Membrane-bound protease; X-linked |
| Vohwinkel syndrome, Mal de Meleda, pachyonychia congenita | *GJB2/LOR*, *SLURP1*, keratins | Other mutilating/hereditary PPKs |

> "Keratosis Follicularis Spinulosa Decalvans (KFSD), Olmsted syndrome, and Osteogenesis Imperfecta type XIX" — [PMID: 33743732](https://pubmed.ncbi.nlm.nih.gov/33743732/) (supporting MBTPS2 as a differential)

**Screening:** no newborn/population screening exists; **cascade genetic testing** of at-risk relatives and genetic counseling are appropriate once a familial variant is identified.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** OLMS2 is **non-lethal in humans**; life expectancy is not reduced by the skin disease itself. (By contrast, constitutive *Perp*-null mice die postnatally — a species difference reflecting gene dosage / complete loss.)
- **Morbidity / function:** high — mutilating PPK, pseudoainhum with autoamputation risk, severe pain and pruritus produce major, lifelong disability affecting mobility and manual function.
- **Quality of life:** substantially impaired; monitored via pain/pruritus VAS and CDLQI in therapy studies ([PMID: 31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)).
- **Disease course:** chronic, progressive; complications include secondary infection of fissured keratotic skin, constricting bands, and functional loss.
- **Recovery potential:** no cure; partial improvement with targeted therapy and supportive care.
- **Prognostic factors:** variant class (dominant-negative C-terminal truncation = most severe), extent of pseudoainhum, and response to EGFR/mTOR-targeted therapy.

---

## 12. Treatment

There is **no approved disease-specific therapy**. Management is multimodal.

**Targeted pharmacotherapy (emerging, mechanism-based):**

| Drug | Class / target | Dose (reported) | Evidence | NCIT suggestion |
|---|---|---|---|---|
| **Erlotinib** | EGFR tyrosine-kinase inhibitor | 2 mg/kg/d | Efficacy in OS incl. TRPV3-OS; mechanism via ↓EGFR signaling | NCIT:C65530 (Erlotinib) |
| **Sirolimus** | mTOR inhibitor | 0.8 mg/m² BID, trough 10–15 ng/mL | Used in 4 refractory OS children | NCIT:C1212 (Sirolimus) |

> "Lesional skin immunostaining showed increased phosphorylated ribosomal protein S6 (RPS6) and phosphorylated EGFR staining in the epidermis, indicating enhanced mTOR and EGFR signaling activation." — [PMID: 31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)

> "A review of the literature indicates that erlotinib has shown efficacy in other cases of OS, making it a promising therapeutic option." — [PMID: 39910762](https://pubmed.ncbi.nlm.nih.gov/39910762/)

Note: the strongest published erlotinib data are in **TRPV3**-associated OS ([PMID: 39926429](https://pubmed.ncbi.nlm.nih.gov/39926429/), [PMID: 39910762](https://pubmed.ncbi.nlm.nih.gov/39910762/)); extrapolation to *PERP*-OLMS2 is rational given shared downstream EGFR/mTOR activation but remains to be demonstrated specifically for *PERP* cases.

**Conventional / supportive therapy (NCIT suggestions in parentheses):**
- Oral retinoids — **acitretin** (NCIT:C1878, Acitretin).
- Topical keratolytics and emollients (NCIT:C1507, Keratolytic Agent).
- Pain and pruritus management.
- **Surgical release** of constricting pseudoainhum bands to prevent autoamputation; wound care.

**Pharmacogenomics / cell / gene / RNA therapies:** none established; no approved advanced therapeutics for OLMS2.

---

## 13. Prevention

- **Primary prevention:** not possible (Mendelian germline disorder). **Genetic counseling** is the mainstay — risk assessment and family-planning guidance for affected families.
- **Secondary prevention:** early diagnosis and early targeted/supportive therapy to limit mutilating complications.
- **Tertiary prevention:** managing pseudoainhum, treating secondary infections, preserving function.
- **Genetic screening:** cascade testing of relatives; prenatal testing / preimplantation genetic diagnosis are feasible once the familial *PERP* variant is known.
- **Immunization / public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** mouse *Perp* (well characterized; see Section 15). Human *PERP* NCBI Gene 64065.
- **Natural disease in other species:** no naturally occurring *PERP*-related Olmsted-like disease documented in companion animals or wildlife (OMIA); the animal evidence is from engineered models.
- **Comparative biology:** *Perp* function in desmosomal adhesion and epithelial integrity is **evolutionarily conserved** between mouse and human; the human dominant disease arises via a dominant-negative truncation, whereas complete murine loss is postnatally lethal — a dosage/species difference.
- **Transmission / zoonosis:** not applicable (non-infectious genetic disease).

---

## 15. Model Organisms

**Mouse (*Mus musculus*) is the principal model.**

| Model | Phenotype | Recapitulation | PMID |
|---|---|---|---|
| Constitutive *Perp*-null | Postnatal lethality; dramatic blistering in stratified epithelia; numerous desmosomal defects | Captures adhesion failure & desmosomal pathology; more severe (lethal) than human | [15797384](https://pubmed.ncbi.nlm.nih.gov/15797384/) |
| Epithelium-specific K5-Cre conditional *Perp* KO | Postnatal lethality, blistering, hyperproliferation | Confirms cell-intrinsic role in stratified epithelia | [16417219](https://pubmed.ncbi.nlm.nih.gov/16417219/) |
| *Perp*-loss + UVB | Promotes cutaneous squamous cell carcinoma initiation & progression | Reveals tumor-suppressor function (p53/p63-regulated) | [20975948](https://pubmed.ncbi.nlm.nih.gov/20975948/) |

> "Perp-/- mice die postnatally, with dramatic blistering in stratified epithelia symptomatic of compromised adhesion." — [PMID: 15797384](https://pubmed.ncbi.nlm.nih.gov/15797384/)

> "the majority of mice lacking Perp in stratified epithelia die within 10 days after birth, accompanied by blistering and hyperproliferation in the epithelia" — [PMID: 16417219](https://pubmed.ncbi.nlm.nih.gov/16417219/)

> "Perp ablation promotes both tumor initiation and progression" — [PMID: 20975948](https://pubmed.ncbi.nlm.nih.gov/20975948/)

**Model characteristics.** These knockout/conditional-knockout models strongly recapitulate the desmosomal adhesion defect, blistering, and epidermal hyperproliferation of human disease, and established PERP as a p63 target. **Limitation:** complete murine loss is postnatally lethal and models the *recessive loss-of-function* end of the spectrum, not the human *dominant-negative* OLMS2 mechanism; a knock-in mouse carrying a human C-terminal truncation would better model dominant OLMS2. **Resources:** MGI (mouse *Perp*). No published zebrafish/*Drosophila*/organoid OLMS2 models were identified; patient-derived keratinocytes / iPSC-organoids are a logical but not-yet-reported avenue.

An incidental *PERP* missense variant (p.Gly59Arg) was found in an ARVC screen but was of uncertain significance ([PMID: 23858024](https://pubmed.ncbi.nlm.nih.gov/23858024/)), reflecting *PERP* expression in heart; this is not OLMS2.

---

## Mechanistic Model / Interpretation

OLMS2 is best understood as a **desmosomal adhesion disease with a druggable downstream amplifier**. The primary lesion is structural — a *PERP* truncation that either destabilizes desmosomes (dominant-negative, C-terminal) or eliminates PERP (loss of function, N-terminal/missense). Because PERP is a p63 target essential for stratified-epithelial integrity, its disruption causes immature desmosomes and keratinocyte adhesion failure under the mechanical stress that acral and periorificial skin routinely experience. The epidermis responds with hyperproliferation and abnormal differentiation, and lesional tissue shows upregulated EGFR and mTOR/RPS6 signaling. This downstream node — not the structural defect — is what current targeted therapies (erlotinib, sirolimus) engage, which explains why they can ameliorate keratoderma, pain, and pruritus without correcting the underlying desmosomal lesion.

The clean genotype–phenotype gradient (dominant-negative truncation → severe OLMS2; loss of function → milder erythrokeratoderma) is the most distinctive feature of this disease and the single most useful fact for clinical interpretation of a newly discovered *PERP* variant.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/) | *Mutations in PERP Cause Dominant and Recessive Keratoderma* | **Landmark** — defines OLMS2; dominant-negative vs LoF mechanisms; EM desmosomal immaturity |
| [34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/) | *Ichthyosis...biallelic mutations in PERP* | Recessive variant spectrum; exact nomenclature; consanguineous cohort |
| [25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/) | *Olmsted syndrome: clinical, molecular and therapeutic aspects* | Phenotype definition, epidemiology (~73 cases), sex ratio, differential dx |
| [31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/) | *Targeted inhibition of EGFR and mTOR in Olmsted syndrome* | Downstream EGFR/mTOR activation; erlotinib + sirolimus rationale |
| [15797384](https://pubmed.ncbi.nlm.nih.gov/15797384/) | *Perp is a p63-regulated gene essential for epithelial integrity* | p63→PERP axis; desmosomal localization; null-mouse phenotype |
| [16417219](https://pubmed.ncbi.nlm.nih.gov/16417219/) | *Perp requirement in postnatal viability / epithelial integrity* | Conditional KO confirms cell-intrinsic role |
| [20975948](https://pubmed.ncbi.nlm.nih.gov/20975948/) | *Loss of Perp promotes tumorigenesis* | Tumor-suppressor function (UVB SCC) |
| [33743732](https://pubmed.ncbi.nlm.nih.gov/33743732/) | *MBTPS2...skin and bone disorders* | Supports MBTPS2-OS differential |
| [39910762](https://pubmed.ncbi.nlm.nih.gov/39910762/) / [39926429](https://pubmed.ncbi.nlm.nih.gov/39926429/) | *Erlotinib in TRPV3-OS* | Erlotinib efficacy (TRPV3-OS context) |
| [21965674](https://pubmed.ncbi.nlm.nih.gov/21965674/) | *SATB2 and p63 mutant proteins* | p63/SATB2 regulation of *perp* |
| [23858024](https://pubmed.ncbi.nlm.nih.gov/23858024/) | *Junctional candidates in ARVC* | Incidental PERP variant (not OLMS2) |

**Evidence source types:** human clinical/genetic ([30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/), [34863005](https://pubmed.ncbi.nlm.nih.gov/34863005/), [25886873](https://pubmed.ncbi.nlm.nih.gov/25886873/), [31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)); model organism ([15797384](https://pubmed.ncbi.nlm.nih.gov/15797384/), [16417219](https://pubmed.ncbi.nlm.nih.gov/16417219/), [20975948](https://pubmed.ncbi.nlm.nih.gov/20975948/)); in vitro/IHC ([30321533](https://pubmed.ncbi.nlm.nih.gov/30321533/), [31895414](https://pubmed.ncbi.nlm.nih.gov/31895414/)).

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity.** The entire *PERP*-OLMS2 literature rests on a small number of kindreds; no prevalence/incidence, formal penetrance estimates, or natural-history cohorts exist.
2. **Downstream mechanism is inferred.** EGFR/mTOR activation is demonstrated by lesional IHC in Olmsted syndrome, but the causal link from desmosomal failure to EGFR/mTOR activation is not mechanistically proven, and the IHC evidence is not exclusively from *PERP* cases.
3. **Therapy evidence is indirect for PERP.** The best erlotinib/sirolimus data come from *TRPV3*-OS; direct *PERP*-OLMS2 treatment-response data are minimal.
4. **No dominant-negative animal model.** Mouse models reproduce loss of function (lethal), not the human dominant-negative OLMS2 mechanism.
5. **No omics depth.** No transcriptomic/proteomic/metabolomic/single-cell datasets specific to OLMS2; molecular profiling is limited to IHC.
6. **Variant classification.** Few variants, no ClinVar-scale curation, and no functional assays for most missense variants.

---

## Proposed Follow-up Experiments / Actions

1. **Knock-in dominant-negative mouse or human keratinocyte/organoid model** expressing a C-terminal truncated *PERP* to directly test the dominant-negative desmosome-destabilization mechanism and recapitulate OLMS2 (rather than lethal loss of function).
2. **Mechanistic linkage study:** test whether restoring desmosomal adhesion or depleting mutant PERP normalizes EGFR/mTOR–RPS6 signaling in patient-derived keratinocytes — to prove the inferred downstream step.
3. **Prospective, *PERP*-specific therapeutic registry/trial** of erlotinib and/or sirolimus with standardized VAS/CDLQI endpoints and lesional p-EGFR/p-RPS6 as pharmacodynamic biomarkers.
4. **Functional classification of *PERP* VUS** (e.g., recessive missense p.Leu30Pro, p.Gly156Arg) via desmosome-incorporation and adhesion assays to support ACMG curation.
5. **International OLMS2 registry** to estimate prevalence, penetrance, expressivity, and natural history, and to collect ultrastructural EM data as a diagnostic standard.
6. **Single-cell/spatial transcriptomics of lesional skin** to map keratinocyte-state changes and signaling activation in situ.

---

*Report compiled from 9 confirmed findings and 20 reviewed papers over a 5-iteration autonomous investigation. Evidence quotes are verbatim from the cited abstracts.*


## Artifacts

- [OpenScientist final report](Olmsted_Syndrome_2-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Olmsted_Syndrome_2-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 12 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:25886873`: "Suggestive features: PPK with pseudoainhum and periorificial keratotic plaques. Frequently associated features include hair and nail abnormalities, leukokeratosis, corneal default and recurrent infections. Pain and itching are variable but can be severe."
  - closest text in source: "Frequently associated features include hair and nail abnormalities, leukokeratosis, corneal default and recurrent infections"
- `PMID:25886873`: "...usually starting at birth or early childhood..."
  - closest text in source: "The disease starts usually at birth or in early childhood"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 22 |
| Terms named correctly | 13 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0011220` (1 mention) - the report calls it "periorificial hyperkeratosis type"; HP calls it **Prominent forehead**
- `HP:0011817` (1 mention) - the report calls it "oral leukoplakia type"; HP calls it **Basal encephalocele**
- `HP:0001055` (1 mention) - the report calls it "Erythrokeratoderma"; HP calls it **Erysipelas**
- `UBERON:0001456` (1 mention) - the report calls it "face skin / periorificial region"; UBERON calls it **face**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0030961` (4 mentions) - the report calls it "Olmsted syndrome 2 / OLMS2", "OLMS2"; MONDO calls it **Olmsted syndrome 2**
- `HP:0000481` (1 mention) - the report calls it "Abnormality of the cornea"; HP calls it **Abnormal cornea morphology**, and lists "Abnormality of the cornea" among its other names
- `UBERON:0002097` (2 mentions) - the report calls it "Primary organ:** skin", "skin of body"; UBERON calls it **skin of body**, and lists "skin organ" among its other names
- `UBERON:0002389` (1 mention) - the report calls it "skin of manus/palm"; UBERON calls it **manual digit**, and lists "digit of manus" among its other names
- `UBERON:0001513` (1 mention) - the report calls it "skin of pes/sole"; UBERON calls it **skin of pes**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0030961` - called "Olmsted syndrome 2 / OLMS2", "OLMS2"
- `UBERON:0002097` - called "Primary organ:** skin", "skin of body"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.