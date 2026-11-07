---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T08:57:54.758092'
end_time: '2026-10-31T09:37:03.407185'
duration_seconds: 2348.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intellectual Developmental Disorder With Autism And Speech Delay
  mondo_id: MONDO:0011627
  category: ''
  causal_genes: TBR1
  omim_id: OMIM:606053
  synonyms: autism, susceptibility to, 5; AUTS5; autism-related speech delay; phrase
    speech delay, autism-related
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
citation_count: 20
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 20
  on_topic: 18
  validator_version: 0.4.0
term_validation:
  total_terms: 30
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 18
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: UBERON:0001885
    reported_labels:
    - amygdala
    ontology_label: dentate gyrus of hippocampal formation
  labels_variant: 5
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Intellectual_Developmental_Disorder_With_Autism_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Intellectual_Developmental_Disorder_With_Autism_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder With Autism And Speech Delay
- **MONDO ID:** MONDO:0011627 (if available)
- **Causal gene(s):** TBR1
- **OMIM:** OMIM:606053
- **Synonyms:** autism, susceptibility to, 5; AUTS5; autism-related speech delay; phrase speech delay, autism-related
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder With Autism And Speech Delay** covering all of the
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

# Intellectual Developmental Disorder With Autism And Speech Delay (TBR1-Related Disorder)

**MONDO:0011627 · OMIM:606053 · AUTS5 · Causal gene: _TBR1_ (T-box brain transcription factor 1, HGNC:11590, 2q24.2)**

---

## Summary

**Intellectual Developmental Disorder With Autism And Speech Delay** (MONDO:0011627; OMIM 606053; also catalogued as "autism, susceptibility to, 5" / AUTS5) is an autosomal-dominant neurodevelopmental disorder caused by **de novo heterozygous loss-of-function or damaging missense variants in _TBR1_**, a neuron-specific T-box transcription factor expressed in the cerebral cortex, amygdala and olfactory bulb. The disorder is defined clinically by the triad of **intellectual disability (ID), autistic traits, and speech/language delay**. In the largest clinical cohort (25 new individuals plus literature review), ID was present in 100% of affected individuals and autistic traits in 76%, with no recognizable facial gestalt — distinguishing this as a "molecular," not dysmorphic, syndrome [PMID: 32005960].

Mechanistically, TBR1 is a **master regulator of cortical neuron identity**. It specifies deep-layer-6 corticothalamic projection neuron fate, directs neuronal migration and axon guidance, and transcriptionally controls a network of other autism-spectrum-disorder (ASD) risk genes. Haploinsufficiency (a ~50% reduction in dosage) produces two convergent, well-studied disease mechanisms demonstrated in `Tbr1+/-` mice: (1) **abnormal brain wiring** — disrupted inter- and intra-amygdalar axonal projections and whole-brain dyssynchronization — and (2) **NMDA-receptor hypofunction / excitation–inhibition (E–I) imbalance**, because the CASK–TBR1 transcriptional complex normally drives expression of the NMDAR subunit gene _GRIN2B_ (NMDAR2b). The speech-delay component is mechanistically linked to disruption of the direct **TBR1–FOXP2** protein interaction, FOXP2 being the classic speech/language transcription factor. At the severe end of the clinical spectrum, TBR1 variants cause frank cortical malformation (frontal pachygyria), placing the disorder on a continuum "from intellectual disability to frontal pachygyria" [PMID: 30268909].

There is **no disease-specific or curative therapy**; clinical management is supportive (early intervention, speech therapy, special education, behavioral/ASD management). However, the mouse model has yielded a rich pipeline of **mechanism-based rescue strategies** — partial NMDAR agonism (D-cycloserine), trans-synaptic zinc mobilization and dietary zinc/nutrient cocktails, and deep-brain stimulation of the basolateral amygdala — all of which ameliorate social and cognitive deficits in `Tbr1+/-` mice, defining a translational roadmap toward targeted treatment.

---

## Key Findings

### Finding 1 — TBR1 haploinsufficiency causes an NDD of ID, autistic traits and speech delay

De novo heterozygous loss-of-function (truncating) and damaging missense variants in **_TBR1_** (T-box brain transcription factor 1; chromosome 2q24.2) cause this neurodevelopmental disorder. In the defining clinical cohort of 25 previously unreported individuals combined with a literature review, **intellectual disability was observed in 100% of individuals and autistic traits in 76%**, with *"no recognizable facial phenotype"* identified [PMID: 32005960]. TBR1 is independently classified as a **high-confidence ASD/ID risk gene**, and *"in humans, de novo mutations in TBR1 are important causes of sporadic autism and intellectual disability"* [PMID: 28057268]. The gene encodes *"a T-box transcription factor expressed in the cerebral cortex [that] regulates the expression of several candidate genes for autism spectrum disorders"* [PMID: 32005960].

> **Evidence class:** Human clinical (cohort + review). **Penetrance:** ID ~100%, autistic traits ~76%. **Suggested HPO terms:** HP:0001249 (Intellectual disability), HP:0000717 (Autism), HP:0000750 (Delayed speech and language development).

### Finding 2 — TBR1 specifies cortical layer-6 corticothalamic identity; dosage controls L6 connectivity

TBR1 acts at a defined step of the pyramidal-neuron lineage. *"Tbr2 and Tbr1 are expressed during successive stages of differentiation in the pyramidal neuron lineage, from Tbr2+ intermediate progenitors to Tbr1+ postmitotic glutamatergic neurons. At each stage, Tbr2 and Tbr1 regulate laminar and regional identity of cortical projection neurons, cell migration, and axon guidance"* [PMID: 28057268]. The laminar specification is gated by the repressor CTIP1/BCL11a: *"lower levels of CTIP1 in layer 6 are required for TBR1 expression, which directs the corticothalamic fate"* [PMID: 25972180], while CTIP1 represses _Tbr1_ in layer 5. Conditional neonatal studies further show that **Tbr1 dosage controls cortical layer-6 connectivity** [PMID: 30318412], establishing dosage-sensitivity as the proximate cause of circuit miswiring.

> **Evidence class:** Model organism (mouse), developmental. **Suggested GO terms:** GO:0021895 (cerebral cortex neuron differentiation), GO:0007411 (axon guidance), GO:0001764 (neuron migration). **CL term:** CL:0000679 (glutamatergic neuron); **UBERON:** UBERON:0005390 (neocortex layer 6).

### Finding 3 — Tbr1 haploinsufficiency disrupts amygdalar projections and causes NMDAR (Grin2b) hypoactivity / E–I imbalance

This is the central disease mechanism derived from the `Tbr1+/-` mouse. *"Tbr1 haploinsufficiency results in defective axonal projections of amygdalar neurons and the impairment of social interaction, ultrasonic vocalization, associative memory and cognitive flexibility in mice. Loss of a copy of the Tbr1 gene altered the expression of Ntng1, Cntn2 and Cdh8 and reduced both inter- and intra-amygdalar connections"* [PMID: 24441682]. There were *"fewer c-FOS-positive neurons and lack of GRIN2B induction in Tbr1(+/-) amygdalae"* [PMID: 24441682], directly implicating NMDAR hypofunction. The molecular basis is transcriptional: the CASK–TBR1 complex drives the NMDAR2b/_GRIN2B_ promoter — *"NMDAR2b, a downstream target of the CASK-Tbr-1 complex"* [PMID: 20067577]. Thus TBR1 haploinsufficiency unites the two leading ASD pathophysiology models — **abnormal connectivity and E–I imbalance** — in a single gene [PMID: 26578866].

> **Evidence class:** Model organism (mouse), molecular. **Suggested GO terms:** GO:0050804 (modulation of chemical synaptic transmission), GO:0098976 (excitatory chemical synaptic transmission). **CHEBI:** CHEBI:29105 (zinc(2+)); CHEBI:42191 (N-methyl-D-aspartate). **UBERON:** UBERON:0002887 (basolateral amygdala) / UBERON:0001885 (amygdala).

### Finding 4 — NMDAR-targeted and nutritional/neuromodulatory interventions rescue deficits in Tbr1+/- mice

Because the lesion converges on NMDAR hypofunction in the amygdala, multiple orthogonal interventions reverse the phenotype in the mouse model:

| Intervention | Mechanism | Outcome in Tbr1+/- mice | Citation |
|---|---|---|---|
| **D-cycloserine** (partial NMDA agonist) | Direct NMDAR co-agonism; local amygdalar infusion | Ameliorates behavioral defects | [PMID: 24441682] |
| **Clioquinol** (zinc ionophore) | Trans-synaptic Zn²⁺ mobilization → Src/NMDAR activation | Improves social interaction | [PMID: 25981743] |
| **Dietary zinc supplementation** | Restores amygdalar synaptic function | Rescues fear-based learning & social interaction | [PMID: 35303947] |
| **Low-dose nutrient cocktail** (zinc + BCAA + serine) | Normalizes BLA hyperactivation/hyperconnectivity | Improves social behavior & associative memory | [PMID: 41329641] |
| **Deep brain stimulation of BLA** (theta-burst) | Restores whole-brain synchronization | Increases nose-to-nose social interaction | [PMID: 39012916] |

Key supporting quotes: *"upregulation of amygdalar neuronal activity by local infusion of a partial NMDA receptor agonist, d-cycloserine, ameliorates the behavioral defects of Tbr1(+/-) mice"* [PMID: 24441682]; *"Clioquinol also improves social interaction in mice haploinsufficient for the transcription factor Tbr1, which accompanies NMDAR activation in the amygdala"* [PMID: 25981743]; *"dietary zinc supplementation prevents impairments in auditory fear memory and social interaction"* [PMID: 35303947].

> **Evidence class:** Model organism (mouse), interventional/preclinical. **Suggested NCIT terms:** C61735 (D-cycloserine), C731 (Zinc). No human trials for this indication yet.

### Finding 5 — De novo TBR1 variants disrupt localization, transcriptional repression, homodimerization and the TBR1–FOXP2 interaction linked to speech

Functional assays distinguish pathogenic from benign variation and explain the speech phenotype. *"De novo truncating and missense mutations disrupt multiple aspects of TBR1 function, including subcellular localization, interactions with co-regulators and transcriptional repression. Missense mutations inherited from unaffected parents did not disturb function in our assays"* [PMID: 25232744]. Critically, TBR1 *"interacts with FOXP2, a transcription factor implicated in speech/language disorders, and ... this interaction is disrupted by pathogenic mutations affecting either protein"* [PMID: 25232744] — providing a direct molecular bridge to the "speech delay" in the disease name. A dedicated interactome screen identified ~250 TBR1 partners and mapped *"two distinct protein-binding domains of TBR1 that have essential roles in protein-protein interaction"* disrupted by NDD variants [PMID: 36579832].

> **Evidence class:** In vitro / functional genomics. **Genotype specificity:** de novo damaging variants disrupt function; inherited parental missense do not. **Gene link:** FOXP2 (OMIM 605317).

### Finding 6 — TBR1 directly regulates a network of ASD risk genes in the developing neocortex

Genome-wide binding data show TBR1's role as an ASD hub. *"TBR1-bound regions are enriched adjacent to ASD genes. ASD genes were also enriched among genes that are differentially expressed in Tbr1 knockouts, which together with the ChIP-seq data, suggests direct transcriptional regulation"* [PMID: 27325115]. Of nine ASD genes examined, seven were misexpressed in Tbr1-knockout cortex (six with increased expression in deep cortical layers), and TBR1-regulated ASD genes are relatively intolerant to loss-of-function mutations in human populations — consistent with a dosage-sensitive regulatory network whose perturbation propagates ASD risk.

> **Evidence class:** Model organism + computational (ChIP-seq, population constraint).

### Finding 7 — TBR1-related disorder spans a structural brain-malformation spectrum detectable on MRI

Brain imaging reveals a graded structural phenotype. In the clinical cohort, *"MRI analysis revealed a reduction of the anterior commissure and suggested new features including dysplastic hippocampus and subtle neocortical dysgenesis"* [PMID: 32005960] — anomalies that parallel those of Tbr1 mutant mice. At the severe end, two individuals with the same de novo frameshift (c.1588_1594dup, p.(Thr532Argfs*144)) presented with **frontal pachygyria and severe ID**, and the authors concluded that *"TBR1-related disorders range from intellectual disability to frontal pachygyria"* [PMID: 30268909].

> **Evidence class:** Human clinical (neuroimaging). **Suggested HPO terms:** HP:0002119 (ventriculomegaly-adjacent abnormal brain morphology — use HP:0012443 Abnormal brain morphology), HP:0001302 (Pachygyria), hippocampal dysplasia, anterior commissure reduction.

### Finding 8 — Pathogenic missense variants cluster in the T-box DNA-binding domain, but in silico prediction overcalls pathogenicity

De novo missense variants *"located in the T-box DNA-binding domain ... disrupt TBR1 protein function"* (localization, transcriptional activity, protein interactions) [PMID: 30250039]. However, variant interpretation requires functional confirmation: of three T-box missense variants from ASD cases, *"only two of the three tested variants severely disrupted TBR1 protein function, despite in silico predictions that all would be deleterious"* [PMID: 30250039]. The same work characterized *"a putative interaction with BCL11A, a transcription factor that was recently implicated in a neurodevelopmental syndrome involving developmental delay and language deficits"* [PMID: 30250039], linking TBR1 to a wider language-deficit network.

> **Evidence class:** In vitro / functional genomics. **Clinical implication:** functional assays should supplement ACMG/AMP in silico evidence (PP3) for T-box missense VUS.

### Finding 9 — TBR1 converges with other ASD regulators on shared promoters; disruption shifts neuron-to-glia fate and reproduces ASD brain signatures

ChIP-seq of five ASD-associated transcriptional regulators (ARID1B, BCL11A, FOXP1, **TBR1**, TCF7L2) in developing human and mouse cortex showed extensive binding-site overlap, especially at promoters. *"The overlap within a promoter region, 1-2,000 bp upstream of the transcription start site, was highly predictive of brain-expressed genes. This signature was observed in 96 out of 102 ASD-associated genes"* [PMID: 38850535]. Functionally, *"In vitro CRISPRi against ARID1B and TBR1 ... After 8 days, NeuN+ and CALB+ cells were decreased, GFAP+ cells were increased, and transcriptomic signatures correlated with the postmortem brain samples from individuals with ASD"* [PMID: 38850535] — demonstrating that TBR1 loss shifts the **neuron-to-glia fate balance** and recreates human ASD brain signatures.

> **Evidence class:** Human + model organism + in vitro (ChIP-seq, CRISPRi). **CL terms:** CL:0000127 (astrocyte, GFAP+), CL:0000540 (neuron, NeuN+).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A **de novo heterozygous variant in _TBR1_** (truncating/frameshift/nonsense, or damaging missense in the T-box DNA-binding domain) **leads to** ~50% reduction of functional TBR1 protein (haploinsufficiency). *Demonstrated* for LoF; *demonstrated functionally* for a subset of T-box missense.
2. Reduced TBR1 dosage **results in** impaired transcriptional control at TBR1 target promoters, because mutant protein shows altered subcellular localization, lost homodimerization, disrupted co-regulator binding, and reduced transcriptional repression/activation [PMID: 25232744].
3. This **branches** into several downstream effects:
   - **Branch A (cortical identity):** mis-specification of deep layer-6 corticothalamic projection neuron identity and altered laminar/regional fate **leads to** aberrant migration, axon guidance and — at the severe end — cortical malformation (frontal pachygyria) [PMID: 28057268, 25972180, 30318412, 30268909].
   - **Branch B (amygdalar wiring):** dysregulation of Ntng1, Cntn2, Cdh8 **leads to** defective inter-/intra-amygdalar axonal projections and whole-brain dyssynchronization [PMID: 24441682, 39012916].
   - **Branch C (NMDAR/E–I):** loss of CASK–TBR1 drive on the _GRIN2B_/NMDAR2b promoter **results in** NMDAR hypofunction and excitation–inhibition imbalance [PMID: 20067577, 24441682].
   - **Branch D (speech):** disruption of the TBR1–FOXP2 interaction **leads to** failure of the speech/language transcriptional program [PMID: 25232744].
   - **Branch E (network/fate):** de-repression/misexpression of a network of ASD risk genes and a **neuron-to-glia fate shift** **reproduce** ASD cortical transcriptomic signatures [PMID: 27325115, 38850535].
4. These converge to **produce** the clinical triad: intellectual disability (~100%), autistic traits (~76%), and speech/language delay, with variable structural brain anomalies on MRI [PMID: 32005960, 30268909].

```
            de novo TBR1 variant (LoF / T-box missense)
                           │  haploinsufficiency (~50% dose)
                           ▼
          impaired TBR1 transcriptional program
          (localization, dimerization, repression lost)
      ┌──────────┬──────────┬───────────┬──────────┬───────────┐
      ▼          ▼          ▼           ▼          ▼
   L6 cortical  amygdalar  CASK-TBR1   TBR1-FOXP2  ASD-gene
   mis-spec.    axon       → ↓GRIN2B   disrupted   network +
   (pachygyria) defects    (NMDAR hypo)(speech)    neuron→glia
      └──────────┴──────────┴───────────┴──────────┴───────────┘
                           ▼
         ID (~100%) + autistic traits (~76%) + speech delay
                 ± MRI malformation spectrum
```

**Upstream vs downstream:** The TBR1 variant and its transcriptional dysfunction are the single upstream node; cortical mis-specification, amygdalar miswiring, NMDAR hypofunction, FOXP2-pathway failure and ASD-network dysregulation are parallel downstream branches that each contribute to the shared clinical endpoint. The convergence on NMDAR hypofunction is the most therapeutically actionable node (Finding 4).

### Section-by-section disease knowledge base content

**1. Disease Information.** A rare autosomal-dominant neurodevelopmental disorder; synonyms AUTS5, "autism, susceptibility to, 5," autism-related speech delay, phrase speech delay. Identifiers: MONDO:0011627, OMIM:606053 (phenotype AUTS5), gene _TBR1_. Information is a mix of **individual patient reports/cohorts** (clinical genetics) and **aggregated resources** (OMIM, ClinVar, HPO).

**2. Etiology.** Primary cause is **genetic** — de novo heterozygous variants in TBR1; no environmental or infectious cause. The variant is typically de novo (not inherited); inherited parental missense variants are functionally benign [PMID: 25232744]. No established environmental risk or protective factors specific to this monogenic disorder; nutritional zinc status is a modeled modifier of severity (preclinical only). Gene–environment interaction is suggested by nutrient-cocktail rescue (zinc/BCAA/serine) in mice [PMID: 41329641].

**3. Phenotypes.** Core: intellectual disability (HP:0001249, ~100%), autism/autistic traits (HP:0000717, ~76%), delayed speech/language (HP:0000750, high frequency). Others across the spectrum: cortical malformation/pachygyria (HP:0001302), abnormal brain morphology (HP:0012443), anterior commissure reduction, dysplastic hippocampus. Onset is **congenital/early childhood**; course is **stable (non-progressive)** developmental; severity **variable** (mild ASD-without-ID to severe ID with pachygyria) [PMID: 32948248, 30268909]. QoL impact: lifelong effects on communication, social function, independent living.

**4. Genetic/Molecular.** Causal gene TBR1 (2q24.2). Variant types: frameshift (e.g., c.1588_1594dup p.(Thr532Argfs*144); c.26del p.(Pro9Leufs*12)), nonsense, splice, and missense clustered in the T-box DNA-binding domain (e.g., K228E). Classification: pathogenic/likely pathogenic per ACMG, with functional assays recommended for T-box missense VUS. Origin: **germline de novo**. Functional consequence: **loss of function / haploinsufficiency** (some missense act as dominant-negative on dimerization/repression). Modifier/partner genes: CASK, FOXP2, BCL11A, CINAP. Allele frequency: absent/ultra-rare in gnomAD (de novo).

**5. Environmental.** Not applicable as a cause (monogenic). Dietary micronutrients (zinc) modulate phenotype severity in models only.

**6. Mechanism.** See causal chain above.

**7. Anatomical structures.** Primary organ: **brain** (UBERON:0000955), specifically neocortex layer 6 (UBERON:0005390), amygdala/basolateral amygdala (UBERON:0002887), hippocampus (UBERON:0002421), anterior commissure (UBERON:0000935), olfactory bulb (UBERON:0002264). Body system: **nervous system**. Cell types: glutamatergic cortical projection neurons (CL:0000679), with secondary astrocyte/glia shifts (CL:0000127). Subcellular: **nucleus** (GO:0005634) — TBR1 is a nuclear transcription factor; synapse (GO:0045202) downstream. Lateralization: bilateral; amygdalar projection defects notably disrupt contralateral projections.

**8. Temporal development.** Congenital onset, insidious; recognized in infancy/early childhood via developmental delay. Non-progressive, lifelong/chronic course. Critical period = prenatal/neonatal corticogenesis (the window of TBR1 action and of potential layer-6 connectivity correction in models).

**9. Inheritance & population.** Autosomal dominant, **de novo** in nearly all cases. Penetrance high (ID ~100% among reported). Expressivity variable. No anticipation, no founder effect, consanguinity not relevant. Prevalence: rare; exact figures unavailable (one of many monogenic ASD/ID genes, each <1% of ASD). Germline mosaicism theoretically possible but not documented. Sex ratio not firmly established; ASD overall male-skewed.

**10. Diagnostics.** Diagnosis is **molecular** — WES/WGS or NDD/ASD/epilepsy gene panels detect the TBR1 variant (e.g., a 268-gene ID/ASD/epilepsy panel) [PMID: 32948248]. CMA for structural variants. MRI may show anterior commissure reduction, hippocampal dysplasia, or pachygyria but is non-diagnostic. No biochemical biomarker. Functional assays assist T-box missense interpretation [PMID: 30250039]. Clinical criteria: DSM-5 ASD + standardized ID assessment. Differential: other monogenic ASD/ID (ARID1B, FOXP1, BCL11A, GRIN2B, MEF2C, SCN2A).

**11. Outcome/Prognosis.** Non-lethal; normal life expectancy expected. Morbidity is lifelong intellectual/communication disability; prognosis correlates with variant severity and presence of cortical malformation/epilepsy. No disease-specific mortality.

**12. Treatment.** No curative/targeted therapy. Supportive: early intervention, **speech therapy**, occupational/physical therapy, special education, standard ASD behavioral management, and anti-seizure medication if epilepsy. Preclinical/experimental (mouse): D-cycloserine (NCIT:C61735), zinc (NCIT:C731)/clioquinol, nutrient cocktails, BLA deep-brain stimulation (Finding 4). No pharmacogenomic guidance specific to the gene.

**13. Prevention.** No primary prevention (de novo). **Genetic counseling** key: recurrence risk low (de novo) but germline mosaicism cannot be excluded; prenatal/PGT possible for a known familial variant. No population screening.

**14. Other species / natural disease.** TBR1 is highly conserved; mouse _Tbr1_ (NCBI Gene 21375) is the principal ortholog studied. No recognized naturally occurring TBR1 disease in companion animals; expression/development studied comparatively in pig and wild boar cortex [PMID: 40498232]. Mechanisms (layer-6 specification, Cajal-Retzius/Reelin biology) are evolutionarily conserved across mammals.

**15. Model organisms.** The **`Tbr1+/-` (heterozygous knockout) mouse** is the gold-standard model, recapitulating amygdalar miswiring, NMDAR hypofunction, impaired social interaction, ultrasonic vocalization, associative memory and cognitive flexibility deficits [PMID: 24441682, 26578866]. `Tbr1-/-` is neonatal-lethal with severe cortical/amygdala/olfactory-bulb defects (models severe-end biology only). Conditional/neonatal deletion models dissect layer-6 connectivity [PMID: 30318412]. Knock-in missense (e.g., K228E) [PMID: 31680851] and in vitro CRISPRi in cortical cultures/organoids [PMID: 38850535] extend the toolkit. Limitation: `Tbr1+/-` does not reproduce the full cortical-migration phenotype seen in nulls/humans with pachygyria.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports | Evidence type |
|---|---|---|---|
| [32005960](https://pubmed.ncbi.nlm.nih.gov/32005960/) | De novo TBR1 variants, 25 individuals + review | F1, F7 (penetrance, MRI spectrum) | Human clinical cohort |
| [28057268](https://pubmed.ncbi.nlm.nih.gov/28057268/) | Control of neuronal development by T-box genes | F1, F2 (de novo cause; laminar identity) | Review/model |
| [25972180](https://pubmed.ncbi.nlm.nih.gov/25972180/) | CTIP1/BCL11a represses TBR1 | F2 (L6 corticothalamic fate) | Model organism |
| [30318412](https://pubmed.ncbi.nlm.nih.gov/30318412/) | Neonatal Tbr1 dosage controls L6 connectivity | F2 (dosage sensitivity) | Model organism |
| [24441682](https://pubmed.ncbi.nlm.nih.gov/24441682/) | Tbr1 haploinsufficiency impairs amygdalar projections | F3, F4 (wiring, NMDAR, D-cycloserine) | Model organism |
| [20067577](https://pubmed.ncbi.nlm.nih.gov/20067577/) | CASK phosphorylation regulates NMDAR2b | F3 (CASK–TBR1 → GRIN2B) | In vitro/molecular |
| [26578866](https://pubmed.ncbi.nlm.nih.gov/26578866/) | TBR1 controls brain wiring & activity in ASD | F3 (integrated wiring + E–I model) | Review |
| [25981743](https://pubmed.ncbi.nlm.nih.gov/25981743/) | Trans-synaptic zinc improves social interaction | F4 (clioquinol rescue) | Model organism |
| [35303947](https://pubmed.ncbi.nlm.nih.gov/35303947/) | Dietary zinc rescues learning/synaptic function | F4 (zinc rescue) | Model organism |
| [41329641](https://pubmed.ncbi.nlm.nih.gov/41329641/) | Low-dose nutrient mixtures ameliorate deficits | F4 (nutrient cocktail) | Model organism |
| [39012916](https://pubmed.ncbi.nlm.nih.gov/39012916/) | DBS of BLA alters connectivity & social behavior | F4 (neuromodulation) | Model organism |
| [25232744](https://pubmed.ncbi.nlm.nih.gov/25232744/) | De novo TBR1 mutations disrupt protein functions | F5 (LoF, TBR1–FOXP2, genotype specificity) | In vitro/functional |
| [36579832](https://pubmed.ncbi.nlm.nih.gov/36579832/) | TBR1 interactome | F5 (interaction domains) | In vitro |
| [27325115](https://pubmed.ncbi.nlm.nih.gov/27325115/) | TBR1 regulates ASD risk genes in neocortex | F6 (ASD gene network) | Model + computational |
| [30250039](https://pubmed.ncbi.nlm.nih.gov/30250039/) | Functional characterization of TBR1 variants | F8 (T-box hotspot; in silico overcall; BCL11A) | In vitro |
| [30268909](https://pubmed.ncbi.nlm.nih.gov/30268909/) | TBR1 → cortical malformations and ID | F7 (frontal pachygyria severe end) | Human clinical |
| [38850535](https://pubmed.ncbi.nlm.nih.gov/38850535/) | Five ASD transcriptional regulators share loci | F9 (promoter convergence; neuron→glia; CRISPRi) | Human + in vitro |
| [32948248](https://pubmed.ncbi.nlm.nih.gov/32948248/) | De novo frameshift in ASD without ID | Phenotypic variability (mild end) | Human clinical |
| [31680851](https://pubmed.ncbi.nlm.nih.gov/31680851/) | TBR1-K228E knock-in model | Model organism (missense) | Model organism |
| [40498232](https://pubmed.ncbi.nlm.nih.gov/40498232/) | Reelin/Tbr1 cells in wild boar neocortex | Comparative/conservation | Comparative |

All nine knowledge-state findings are supported by verified abstract quotes (see Key Findings). No contradictory finding was identified; the only internal tension — the mild case of ASD-without-ID carrying a de novo frameshift [PMID: 32948248] — is consistent with variable expressivity rather than a challenge to causation.

---

## Limitations and Knowledge Gaps

- **Epidemiology is unquantified.** No population prevalence/incidence, sex ratio, or geographic data exist for this specific disorder; it is one of many ultra-rare monogenic ASD/ID causes. Carrier frequency is effectively zero (de novo).
- **Human mechanistic data are limited.** Most mechanistic insight derives from `Tbr1+/-` mice and in vitro assays. Human postmortem/neuroimaging data are from small cohorts (≤7–25 individuals). The `Tbr1+/-` mouse does not reproduce the cortical-migration/pachygyria phenotype of severe human cases.
- **Genotype–phenotype correlation is incomplete.** Why the same de novo frameshift yields severe ID + pachygyria in some but milder ASD-without-ID in others is unexplained; modifier genes, mosaicism, and genetic background remain untested.
- **Variant interpretation is hard.** In silico predictors overcall T-box missense pathogenicity [PMID: 30250039]; functional assays are not routinely available in the clinic, leaving many VUS.
- **No human therapeutic data.** All rescue strategies (D-cycloserine, zinc, nutrient cocktails, DBS) are preclinical; none has been tested in TBR1 patients, and dose/timing/critical-window translatability is unknown.
- **Penetrance/expressivity estimates** derive from ascertainment-biased clinical cohorts and may overstate severity.

---

## Proposed Follow-up Experiments / Actions

1. **Natural-history registry & deep phenotyping** of TBR1 patients (genotype, MRI, cognition, language, epilepsy) to establish prevalence, penetrance, sex ratio, and genotype–phenotype correlation — resolving whether truncation site or domain predicts pachygyria vs mild ASD.
2. **Clinical pilot of NMDAR-modulating therapy** (e.g., D-cycloserine) or **zinc supplementation** in TBR1 patients, given consistent multi-study preclinical rescue [PMID: 24441682, 35303947, 41329641]; include social-communication and EEG E–I biomarker endpoints.
3. **Standardized functional assay panel** (localization, dimerization, transcriptional repression, FOXP2/BCL11A binding) as a routine adjunct to ACMG/AMP for T-box missense VUS classification [PMID: 25232744, 30250039, 36579832].
4. **Human iPSC-derived cortical organoid models** of patient-specific TBR1 variants to test the neuron-to-glia fate shift [PMID: 38850535] and screen correctors in a human genetic background.
5. **Developmental-window / dosage-restoration experiments** (conditional re-expression, ASO/gene-dosage upregulation) in mice to define the critical period for correcting layer-6 connectivity [PMID: 30318412] and whether postnatal intervention is possible.
6. **Map the TBR1–FOXP2–BCL11A language network** transcriptionally (ChIP-seq/CUT&RUN + RNA-seq) in human neurons to pinpoint the speech-delay effector genes and candidate drug targets.


## Artifacts

- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Autism_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Intellectual_Developmental_Disorder_With_Autism_And_Speech_Delay-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 18 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0001885` (1 mention) - the report calls it "amygdala"; UBERON calls it **dentate gyrus of hippocampal formation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0005390` (2 mentions) - the report calls it "neocortex layer 6"; UBERON calls it **cortical layer I**, and lists "neocortex layer 1" among its other names
- `CHEBI:42191` (1 mention) - the report calls it "N-methyl-D-aspartate"; CHEBI calls it **EDTA(4-)**, and lists "ethylenediaminetetraacetate" among its other names
- `UBERON:0002887` (2 mentions) - the report calls it "basolateral amygdala"; UBERON calls it **basal amygdaloid nucleus**, and lists "basolateral amygdalar nucleus" among its other names
- `CL:0000127` (2 mentions) - the report calls it "astrocyte, GFAP+"; CL calls it **astrocyte**
- `CL:0000540` (1 mention) - the report calls it "neuron, NeuN+"; CL calls it **neuron**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.