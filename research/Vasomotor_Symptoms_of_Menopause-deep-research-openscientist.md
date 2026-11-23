---
provider: openscientist
cached: false
start_time: '2026-11-14T18:57:05.197927'
end_time: '2026-11-14T19:13:22.485670'
duration_seconds: 977.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vasomotor Symptoms of Menopause
  mondo_id: none - MONDO has no class for menopausal vasomotor symptoms (hot flushes
    / night sweats); the nearest coded anchor is ICD-10-CM N95.1 menopausal and female
    climacteric states
  causal_genes: none; this is an acquired thermoregulatory condition caused by postmenopausal
    oestrogen withdrawal acting on hypothalamic KNDy neurons, not a Mendelian disease
  omim_id: none
  synonyms: VMS; hot flushes; hot flashes; night sweats; menopausal vasomotor symptoms
  category: acquired thermoregulatory condition of the menopausal transition
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    save_artifacts: true
    artifact_max_bytes: 5242880
    artifact_keep_runtime: false
    artifact_extra_extensions: []
    artifact_include_globs: []
    artifact_exclude_globs: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
run_metadata:
  job_id: 46f7a838-bc00-4c05-b3a7-1c29d4252661
citation_count: 31
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 33
  on_topic: 27
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Vasomotor_Symptoms_of_Menopause-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Vasomotor_Symptoms_of_Menopause-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vasomotor Symptoms of Menopause
- **MONDO ID:** none - MONDO has no class for menopausal vasomotor symptoms (hot flushes / night sweats); the nearest coded anchor is ICD-10-CM N95.1 menopausal and female climacteric states (if available)
- **Causal gene(s):** none; this is an acquired thermoregulatory condition caused by postmenopausal oestrogen withdrawal acting on hypothalamic KNDy neurons, not a Mendelian disease
- **OMIM:** none
- **Synonyms:** VMS; hot flushes; hot flashes; night sweats; menopausal vasomotor symptoms
- **Category:** acquired thermoregulatory condition of the menopausal transition

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Vasomotor Symptoms of Menopause** covering all of the
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

# Vasomotor Symptoms of Menopause: A Comprehensive Disease Characteristics Report

## Summary

**Vasomotor symptoms of menopause (VMS)** — hot flushes/flashes and night sweats — are an **acquired, non-Mendelian thermoregulatory disorder** of the menopausal transition. There is **no causal gene** and no OMIM/MONDO entry; the nearest coded anchor is **ICD-10-CM N95.1** (menopausal and female climacteric states). The initiating lesion is **withdrawal of ovarian estradiol** (CHEBI:16469 17β-estradiol). Estrogen loss de-represses a discrete population of hypothalamic arcuate-nucleus neurons co-expressing **kisspeptin, neurokinin B (NKB), and dynorphin** — the **KNDy neurons** — which become hypertrophic and hyperactive. These neurons signal via **neurokinin B acting on the NK3 receptor (NK3R), encoded by *TACR3***, onto thermoregulatory neurons in the hypothalamic preoptic area, narrowing the "thermoneutral zone" so that trivial elevations in core body temperature trigger inappropriate heat-dissipation responses — cutaneous vasodilation and sweating — perceived as a hot flash.

Although VMS has no Mendelian cause, human genetics, pathophysiology, and pharmacology converge on a single molecular node: a trans-ethnic GWAS identified ***TACR3*** (the NK3R gene) as the only genome-wide-significant susceptibility locus, and **NK3R antagonists (fezolinetant, and the dual NK1/NK3 antagonist elinzanetant)** are now proven non-hormonal therapies. This convergence makes VMS an unusually mechanistically "solved" common condition despite the absence of a disease gene.

VMS affect **50–80% of women**, persist for a **median of 7.4 years** (longest in Black/African American women, median 10.1 years), and are not merely a nuisance: frequent/persistent VMS mark an **adverse cardiovascular risk profile and elevated CVD/stroke event risk**, and cluster with **sleep disturbance and mood symptoms** into a triad that drives quality-of-life impairment. Treatment is led by **menopausal hormone therapy (MHT)** — most effective, favorable risk/benefit for women <60 years or within 10 years of menopause ("timing hypothesis") — with non-hormonal options including **NK3R antagonists** (~58% achieve ≥50% VMS reduction), **SSRIs/SNRIs, gabapentin, and cognitive behavioral therapy (CBT)**. The NK3R antagonist class carries a **hepatic (transaminase-elevation) safety signal** requiring liver monitoring.

---

## Key Findings

### Finding 1 — Core mechanism: estrogen withdrawal → KNDy hyperactivity → NK3R signaling to the preoptic heat-defense pathway

The central pathophysiology of VMS is now well established from convergent human neuropathology, animal models, and reverse-pharmacology. Postmenopausal women show marked **hypertrophy and increased neurokinin B expression** in arcuate-nucleus KNDy neurons. When estradiol declines, these neurons — normally restrained by estrogen negative feedback — become hyperactive. They project from the arcuate nucleus to the **median preoptic nucleus** of the hypothalamic preoptic area, the brain's heat-defense integrator, where NKB acting on **NK3R** triggers heat-loss effectors: cutaneous vasodilation and sweating.

Rance et al. ([PMID: 23872331](https://pubmed.ncbi.nlm.nih.gov/23872331/)) summarize the animal evidence: *"activation of NK₃R in the median preoptic nucleus, part of the heat-defense pathway, reduces body temperature. Finally, ablation of KNDy neurons reduces cutaneous vasodilatation and partially blocks the effects of estrogen on thermoregulation."* A 2025 review ([PMID: 40330614](https://pubmed.ncbi.nlm.nih.gov/40330614/)) states the full chain: *"the kisspeptin-neurokinin B-dynorphin (KNDy) neuron complex … becomes hyperactive when estradiol levels decrease. KNDy neurons project from the arcuate nucleus to thermoregulatory areas within the hypothalamic preoptic area, where heat loss mechanisms are triggered, including cutaneous vasodilation and sweating."* The therapeutic corollary ([PMID: 42045091](https://pubmed.ncbi.nlm.nih.gov/42045091/)) is that *"VMS pathogenesis centers on the hypothalamic KNDy neuron network and is primarily mediated by Neurokinin B acting on the NK3 receptor"* — validated by the efficacy of NK3R antagonism.

**Ontology anchors:** GO:0001659 (temperature homeostasis), GO:0007204 signaling / cutaneous vasodilation (heat loss); CL kisspeptin/KNDy neuron of the arcuate nucleus; UBERON:0001882 (arcuate nucleus of hypothalamus), UBERON:0002661 (preoptic area); CHEBI: neurokinin B, 17β-estradiol (CHEBI:16469).

### Finding 2 — Epidemiology: high prevalence, long duration, racial/ethnic disparity

VMS are among the most common conditions of midlife women. In the SWAN cohort (Study of Women's Health Across the Nation; n=3302 enrolled, 1449 with frequent VMS), Avis et al. ([PMID: 25686030](https://pubmed.ncbi.nlm.nih.gov/25686030/)) found *"The median total VMS duration was 7.4 years. Among 881 women who experienced an observable FMP [final menstrual period], the median post-FMP persistence was 4.5 years."* Duration varied by onset timing: women symptomatic while still pre/early-perimenopausal had the longest course (median >11.8 years), while postmenopausal-onset symptoms were shortest (median 3.4 years).

A striking racial/ethnic disparity exists: *"Compared with women of other racial/ethnic groups, African American women reported the longest total VMS duration (median, 10.1 years)."* Part of this disparity is attributable to social stressors: everyday discrimination is associated with VMS in Black women ([PMID: 38595299](https://pubmed.ncbi.nlm.nih.gov/38595299/)) — *"Higher levels of discrimination were associated with concurrent reporting of any (odds ratio [OR], 1.57 [1.31-1.89]) and frequent (≥6 d) VMS (OR, 1.55 [1.21-1.99])."* Prevalence is 50–80% ([PMID: 40330614](https://pubmed.ncbi.nlm.nih.gov/40330614/)), with substantial negative quality-of-life impact.

### Finding 3 — Genetic susceptibility maps to *TACR3*, the same receptor targeted by effective drugs

While VMS is not a genetic disease, susceptibility has a heritable component mapping precisely to the drug target. A WHI trans-ethnic GWAS meta-analysis (n=17,695 European/African/Hispanic American women; Crandall et al. [PMID: 28231077](https://pubmed.ncbi.nlm.nih.gov/28231077/)) found *"14 SNPs, all located on chromosome 4 in the tachykinin receptor 3 (TACR3) locus"* with P < 5×10⁻⁸, and *"These SNPs' effect sizes were similar across studies/participants' ancestry (odds ratio ∼1.5). Genetic variation in TACR3 may contribute to the risk of VMS."* The SWAN Genomic Substudy (Zhao et al. [PMID: 33906203](https://pubmed.ncbi.nlm.nih.gov/33906203/)) replicated and identified a protective allele: *"The C-allele of rs74827081 in TACR3 was associated with reduced likelihood of frequent VMS in White women (odds ratio [OR] = 0.49 [95% CI, 0.29-0.83])."* Polygenic risk scores for reproductive aging (age at menarche/menopause) also predicted VMS trajectories.

**Gene annotation:** *TACR3* (HGNC:11528), chromosome 4q24, encoding the NK3 receptor (NK3R), a class A GPCR; the natural ligand is neurokinin B (encoded by *TAC3*).

### Finding 4 — Treatment efficacy: hormone therapy is most effective; NK3R antagonists are proven non-hormonal options

**Menopausal hormone therapy (MHT)** is the gold standard. Kaunitz & Manson ([PMID: 26348174](https://pubmed.ncbi.nlm.nih.gov/26348174/)): *"Hormone therapy (HT) represents the most effective treatment for these symptoms with oral and transdermal estrogen formulations having comparable efficacy."* The **timing hypothesis** governs risk/benefit ([PMID: 30484736](https://pubmed.ncbi.nlm.nih.gov/30484736/)): *"the risk of adverse cardiovascular events for HT are low for women <60 years of age or within 10 year from menopause."* Mehta ([PMID: 33841322](https://pubmed.ncbi.nlm.nih.gov/33841322/)) concurs that risks are low for healthy women under 60 or within ten years of menopause.

**Fezolinetant**, a selective NK3R antagonist, is the first-in-class non-hormonal mechanistic therapy. In SKYLIGHT 2 (phase 3 RCT, NCT04003142; Johnson et al. [PMID: 36734148](https://pubmed.ncbi.nlm.nih.gov/36734148/)): *"For VMS frequency, W4 least squares mean (SE) reduction vs placebo: fezolinetant 30 mg, -1.82 (0.46; P < .001); 45 mg, -2.55 (0.46; P < .001)"*, with benefit by week 1 maintained to week 52 and serious TEAEs ≤2%. Pooled SKYLIGHT 1+2 ([PMID: 41259888](https://pubmed.ncbi.nlm.nih.gov/41259888/)): *"A greater proportion of fezolinetant-treated participants had a reduction of ≥50 % in VMS frequency from baseline to week 12 versus placebo (58.7 % versus 36.0 %, odds ratio [95 % CI]: 2.542 [1.868-3.472])."* In breast-cancer survivors where MHT is contraindicated, SSRIs/SNRIs and gabapentin are reasonable choices ([PMID: 14663778](https://pubmed.ncbi.nlm.nih.gov/14663778/)).

| Treatment | Class | Key efficacy evidence | PMID |
|---|---|---|---|
| Estrogen ± progestogen (MHT) | Hormonal | Most effective treatment; oral/transdermal comparable | 26348174 |
| Fezolinetant 45 mg | NK3R antagonist | ≥50% VMS reduction in 58.7% vs 36.0% placebo (OR 2.54) | 41259888, 36734148 |
| Elinzanetant | Dual NK1/NK3 antagonist | ~65% VMS reduction (OASIS program) | 42045091 |
| SSRIs/SNRIs (e.g., paroxetine) | Serotonergic/noradrenergic | Reasonable non-hormonal choice; MRS reduction vs placebo | 14663778, 42171505 |
| Gabapentin | α2δ calcium channel ligand | Reasonable non-hormonal choice | 14663778 |
| CBT | Behavioral | Hedges' g −0.60 to −0.87 on bother | 42252432 |

### Finding 5 — Phenotype: an episodic triad with sleep disturbance and mood symptoms

The VMS phenotype is **recurrent, episodic hot flashes** (sudden sensation of heat, flushing, sweating, sometimes palpitations/anxiety) and **night sweats**, each lasting ~1–5 minutes, often worst at night. VMS rarely occur in isolation. A real-world survey (Kingsberg et al. [PMID: 38695491](https://pubmed.ncbi.nlm.nih.gov/38695491/); 2451 physician forms, 1029 patient questionnaires) found that *"Significant burden from the triad of natural or induced menopausal symptoms, sleep disturbances and mood changes affected women's daily activities, work and quality of life more than vasomotor symptoms alone."* A treatment-preference study ([PMID: 37650213](https://pubmed.ncbi.nlm.nih.gov/37650213/)) found *"86.5% and 87.8% reported moderate to very severe VMS and sleep problems during the preceding month,"* and that sleep improvement was the single most valued treatment attribute.

**HPO suggestions:** flushing (HP:0032324), abnormal/increased sweating — hyperhidrosis (HP:0000975), insomnia (HP:0100785), anxiety (HP:0000739), depressivity (HP:0000716), palpitations (HP:0001962).

### Finding 6 — VMS as a cardiovascular risk biomarker

Frequent/persistent VMS are an observational biomarker of poorer cardiovascular health. Thurston ([PMID: 37577812](https://pubmed.ncbi.nlm.nih.gov/37577812/)) summarizing SWAN + MsHeart/MsBrain: *"frequent and/or persistent VMS are associated with adverse CVD risk factor profiles, poorer underlying peripheral vascular and cerebrovascular health, and elevated risk for clinical CVD events."* Carson & Thurston ([PMID: 37214424](https://pubmed.ncbi.nlm.nih.gov/37214424/)): *"VMS have been associated with multiple indicators of cardiovascular disease (CVD) risk, including an unfavorable CVD risk factor profile, increased subclinical CVD, and elevated risk of CVD events."* VMS are also linked to stroke risk ([PMID: 42339545](https://pubmed.ncbi.nlm.nih.gov/42339545/)). These are prospective-cohort associations — **not proven causal**. Notably, in SWAN target-trial emulation ([PMID: 42709460](https://pubmed.ncbi.nlm.nih.gov/42709460/)), MHT initiation in perimenopausal/recently postmenopausal women with VMS was associated with a 22% lower CVD risk (aHR 0.78, 95% CI 0.62–0.98), stronger within 10 years of menopause — though the authors caution against using this to justify MHT for CVD prevention.

### Finding 7 — Animal model: the ovariectomized (OVX) rat with KNDy-neuron ablation

The standard induced model is the **ovariectomized rat** with **tail-skin-temperature (TSKIN)** readout as a hot-flash proxy. Mittelman-Smith et al. ([PMID: 23150555](https://pubmed.ncbi.nlm.nih.gov/23150555/)) used the selective toxin **NK3-saporin** injected into the arcuate nucleus to ablate KNDy neurons: *"KNDy neuron ablation consistently reduced tail-skin temperature (T(SKIN)), indicating that KNDy neurons facilitate cutaneous vasodilatation, an important heat dissipation effector. Moreover, KNDy ablation blocked the reduction of T(SKIN) by 17β-estradiol (E(2))."* This demonstrates KNDy neurons are **required** for cutaneous vasodilation and for estrogen's thermoregulatory effect — the causal spine of the human disease. **Species/orthologs:** rat (*Rattus norvegicus*, NCBI Taxon 10116) *Tacr3*; mouse (*Mus musculus*, 10090) *Tacr3*.

### Finding 8 — Proximate physiology: a narrowed thermoneutral zone with elevated noradrenergic tone

At the whole-body level, Freedman ([PMID: 24012626](https://pubmed.ncbi.nlm.nih.gov/24012626/)) frames the hot flash as *"a rapid and exaggerated heat dissipation response … triggered by small elevations in core body temperature (Tc) acting within a greatly reduced thermoneutral zone, i.e., the Tc region between the upper (sweating) and lower (shivering) thresholds. This is due in part, but not entirely, to estrogen depletion at menopause. Elevated central sympathetic activation, mediated through α2-adrenergic receptors, is one factor responsible for narrowing of the thermoneutral zone."* Crucially, absolute estradiol does not distinguish symptomatic from asymptomatic women ([PMID: 15852197](https://pubmed.ncbi.nlm.nih.gov/15852197/)): *"the appearance of hot flashes coincides with estrogen withdrawal, this does not entirely explain the phenomenon because estrogen levels do not differ between symptomatic and asymptomatic women."* Central sensitivity — not estradiol level — determines who is symptomatic, explaining why *TACR3* genotype and noradrenergic tone matter.

### Finding 9 — Non-hormonal/behavioral management: CBT and psychosocial interventions

Psychosocial interventions meaningfully reduce hot-flash bother. A meta-analysis (Robinson et al. [PMID: 42252432](https://pubmed.ncbi.nlm.nih.gov/42252432/); 28 RCTs, 2,887 women): *"Psychosocial interventions produced medium-to-large reductions in the bothersomeness of hot flushes and night sweats at short-term follow-up (Hedges' g = - 0.60 to - 0.87) and medium-term follow-up (g = - 0.50 to - 0.77)."* A CBT systematic review ([PMID: 41462190](https://pubmed.ncbi.nlm.nih.gov/41462190/); 16 studies, 910 women) found *"CBT significantly improves health-related quality of life and alleviates vasomotor, psychological, and sleep-related symptoms,"* with group-based CBT most effective. A CBT-for-menopausal-insomnia pilot RCT ([PMID: 42084929](https://pubmed.ncbi.nlm.nih.gov/42084929/)): *"CBT-MI compared with MEC significantly reduced ISI (CBT-MI vs. MEC: -10.2±1.15 vs. -6.2±0.99; P=0.007), HFDIS (CBT-MI vs. MEC: -1.3±0.29 vs. -0.5±0.17; P=0.01)."* Physiology-based measures — ambient cooling, paced respiration, clonidine (α2-agonist) — also reduce flashes.

### Finding 10 — Diagnosis is clinical; no confirmatory biomarker

VMS are **diagnosed clinically** from characteristic self-reported symptoms during the menopausal transition; **no laboratory or imaging test confirms VMS**. Objective ambulatory sternal skin-conductance monitoring quantifies flashes in research but is not routine. Hormonal testing has a narrow role: *"Measuring serum follicle stimulating hormone (FSH) and estradiol levels are helpful when in doubt"* ([PMID: 24338340](https://pubmed.ncbi.nlm.nih.gov/24338340/)) to define menopausal status when the picture is ambiguous — not to diagnose VMS. Differential diagnosis of secondary flushing: thyroid dysfunction, carcinoid syndrome, pheochromocytoma, infection, anxiety/panic disorder, and medication effects.

### Finding 11 — Etiology and risk factors: estrogen withdrawal is the cause; induced menopause is worst

The primary cause is **loss of ovarian estradiol** — natural, surgical, or iatrogenic. Induced menopause produces the most severe VMS: *"the unique situation of surgical menopause (with oophorectomy) and cancer therapy, conditions that are associated with frequent, severe, hot flashes"* ([PMID: 40330614](https://pubmed.ncbi.nlm.nih.gov/40330614/)); *"Menopausal symptoms can be particularly severe due to the sudden loss of ovarian function"* ([PMID: 34761721](https://pubmed.ncbi.nlm.nih.gov/34761721/)). Drivers of treatment-induced VMS (iVMS): bilateral oophorectomy, GnRH agonists, aromatase inhibitors, tamoxifen, and chemotherapy-induced ovarian failure. **Modifiable risk factors:** VMS severity associates with incident type 2 diabetes — *"incident T2DM was positively associated with increasing age, BMI, daily alcohol consumption, moderate-to-severe vasomotor symptoms (VMS, OR=1.045, 95% CI: 1.011 to 1.079)"* ([PMID: 37671810](https://pubmed.ncbi.nlm.nih.gov/37671810/)); smoking and higher BMI increase risk; discrimination/psychosocial stress increase burden ([PMID: 38595299](https://pubmed.ncbi.nlm.nih.gov/38595299/)). **Protective factors:** physical activity; the *TACR3* rs74827081 C-allele (genetic protective modifier).

### Finding 12 — NK3R-antagonist safety: a hepatic signal requiring liver monitoring

Real-world pharmacovigilance has flagged a **hepatic (transaminase-elevation) signal** for the NK3R-antagonist class. A WHO VigiAccess analysis (Li et al. [PMID: 42610452](https://pubmed.ncbi.nlm.nih.gov/42610452/); 1,091 reports, 2,143 AEs): *"Liver-related abnormalities showed consistent signals, including increased alanine aminotransferase (ROR=20.60), aspartate aminotransferase (ROR=22.95), and bilirubin (ROR=12.52), suggesting a clustered hepatic signal."* A FAERS disproportionality analysis ([PMID: 42547587](https://pubmed.ncbi.nlm.nih.gov/42547587/)) found serious liver injury as a regulatory concern across ROR/PRR/BCPNN/MGPS algorithms. An elinzanetant hepatic-safety review (Lewis et al. [PMID: 41849128](https://pubmed.ncbi.nlm.nih.gov/41849128/)): *"The occurrence of elevated liver enzymes has been observed in clinical use with NK-3 receptor antagonists, e.g., fezolinetant and pavinetant, with recommendations for liver monitoring in the fezolinetant labeling information."* In pivotal RCTs serious TEAEs remained infrequent (≤2%).

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Ovarian follicular depletion / oophorectomy / endocrine cancer therapy** → **falling circulating estradiol (17β-estradiol)**. *(Demonstrated — the universal trigger.)*
2. Estradiol withdrawal **removes negative-feedback restraint on arcuate-nucleus KNDy neurons** → KNDy neurons **hypertrophy and overexpress neurokinin B** and become hyperactive. *(Demonstrated — human neuropathology, PMID 23872331.)*
3. Hyperactive KNDy neurons **release excess neurokinin B** onto projections to the **median preoptic nucleus** of the hypothalamic preoptic area. *(Demonstrated in rodent tract-tracing/pharmacology.)*
4. Neurokinin B **activates NK3R (TACR3)** on preoptic thermoregulatory neurons → **destabilizes the heat-defense set-point and narrows the thermoneutral zone**, compounded by **elevated central α2-adrenergic/noradrenergic tone**. *(Demonstrated pharmacologically + physiologically, PMID 24012626.)*
5. Within the narrowed thermoneutral zone, a **small rise in core body temperature crosses the sweating threshold** → **inappropriate heat-dissipation response**. *(Demonstrated.)*
6. Heat-dissipation effectors fire: **cutaneous vasodilation (flushing) + sweating + sometimes palpitations/anxiety** = the **hot flash / night sweat**. *(Demonstrated — effector physiology.)*
   - **Branch A (downstream sequelae):** nocturnal flashes → **sleep fragmentation** → **mood disturbance** → compounded QoL/work impairment (the triad).
   - **Branch B (associated risk marker):** frequent/persistent VMS **co-segregate with adverse vascular biology** → elevated CVD/stroke event risk *(association, causation unproven)*.

```
 Estradiol withdrawal (ovarian failure / oophorectomy / cancer Rx)
            │  removes estrogen restraint
            ▼
 Arcuate KNDy neurons  ──hypertrophy, ↑ neurokinin B──►  HYPERACTIVE
            │  NKB release
            ▼
 NK3R (TACR3) on median preoptic nucleus  ◄── ↑ central α2-adrenergic tone
            │  destabilized set-point
            ▼
 NARROWED THERMONEUTRAL ZONE
            │  small ΔTc crosses sweating threshold
            ▼
 Heat-dissipation response:  cutaneous vasodilation + sweating
            ▼
        HOT FLASH / NIGHT SWEAT
          ├──► sleep disruption ──► mood symptoms ──► ↓ QoL (triad)
          └──► marker of adverse vascular health ──► ↑ CVD/stroke risk (assoc.)

 Therapeutic logic:
   • Estrogen (MHT) ........ restores step-2 restraint (most effective)
   • NK3R antagonist ....... blocks step-4 (fezolinetant / elinzanetant)
   • SSRI/SNRI, clonidine .. dampen noradrenergic component of step-4
   • CBT / cooling / paced respiration .. widen tolerance / raise threshold
```

The elegance of VMS biology is that **three independent lines of evidence converge on NK3R/TACR3**: (a) human genetics (the sole GWAS locus is *TACR3*), (b) pathophysiology (KNDy→NK3R→preoptic area), and (c) pharmacology (NK3R antagonists work). This convergence is why VMS, despite being a common acquired condition with no disease gene, is mechanistically "solved" to the receptor level.

---

## Section-by-Section Knowledge Base Content

**1. Disease Information.** Acquired thermoregulatory condition of the menopausal transition. Identifiers: no OMIM, no MONDO class, no Orphanet number; **ICD-10-CM N95.1** (menopausal and female climacteric states); **MeSH D019584 (Hot Flashes)**. Synonyms: VMS, hot flushes, hot flashes, night sweats, menopausal vasomotor symptoms. Information is drawn from **aggregated disease-level resources and cohort studies** (SWAN, WHI), not single-patient EHR.

**2. Etiology.** Cause: estradiol withdrawal. Genetic risk/modifier: *TACR3* (not causal). Environmental/lifestyle risk: induced/surgical menopause (strongest), smoking, obesity/high BMI, diabetes, alcohol, psychosocial stress/discrimination. Protective: physical activity, *TACR3* rs74827081 C-allele. Gene–environment interaction: central NK3R sensitivity (genotype) × degree/abruptness of estrogen loss (environment) determines symptom expression.

**3. Phenotypes.** Hot flashes (flushing HP:0032324), night sweats/hyperhidrosis (HP:0000975), palpitations (HP:0001962), insomnia (HP:0100785), anxiety (HP:0000739), depressivity (HP:0000716). Adult/perimenopausal onset; severity mild–severe (variable); course episodic/fluctuating; frequency 50–80% of women; median duration 7.4 y.

**4. Genetic/Molecular.** No causal gene. Susceptibility/modifier: *TACR3* (HGNC:11528, 4q24). Variants are common polymorphisms (e.g., rs74827081), not ACMG pathogenic variants; germline; population allele frequencies vary by ancestry with consistent ~1.5 OR. No chromosomal abnormalities. Epigenetics: estrogen-dependent regulation of HSP70/NO axis proposed (PMID 28903474, hypothesis-level).

**5. Environmental.** Iatrogenic triggers: oophorectomy, aromatase inhibitors, tamoxifen, GnRH agonists, chemotherapy. Lifestyle: smoking, obesity, alcohol, physical inactivity. No infectious agent.

**6. Mechanism.** See causal chain above. Molecular pathway: GPCR signaling (NK3R/Gq), noradrenergic/α2-adrenergic signaling. Cellular process: neuronal hyperexcitability (GO:0001659 temperature homeostasis). Cell type: KNDy/kisspeptin neuron (arcuate). No immune/metabolic primary defect (HSR/HSP70 link is hypothesis-level).

**7. Anatomy.** Primary: hypothalamus — **arcuate nucleus (UBERON:0001882)** and **preoptic area/median preoptic nucleus (UBERON:0002661)**. Effectors: **skin (UBERON:0002097)** cutaneous vasculature and **eccrine sweat glands (UBERON:0001820)**. Systems: nervous (CNS/autonomic), endocrine, integumentary, cardiovascular. Subcellular: plasma-membrane GPCR signaling (GO:0005886).

**8. Temporal development.** Onset: perimenopausal/adult, typically ages ~45–55; insidious. Course: episodic/fluctuating, chronic over years; median 7.4 y total, 4.5 y post-FMP; often remits spontaneously but may persist >10 y. Critical window: within 10 years of menopause (optimal MHT risk/benefit).

**9. Inheritance and population.** Not Mendelian — multifactorial/polygenic susceptibility. Prevalence 50–80% of menopausal women. Longest duration in African American women. Exclusively affects individuals undergoing menopause (overwhelmingly female; also relevant to androgen-deprivation/gender-affirming contexts).

**10. Diagnostics.** Clinical diagnosis; no confirmatory biomarker. FSH/estradiol only to clarify menopausal status when uncertain. Research tool: sternal skin-conductance monitoring. Rule out thyroid disease, carcinoid, pheochromocytoma, infection, anxiety/panic, drug effects.

**11. Prognosis.** Non-fatal, self-limited over years but with major QoL/sleep/mood morbidity; marker (not proven cause) of elevated CVD/stroke risk. Prognostic factors: onset timing (early perimenopausal onset → longer duration), race/ethnicity, BMI, smoking.

**12. Treatment.** MHT (most effective; NCIT: Estrogen Therapy / Hormone Replacement Therapy); NK3R antagonists fezolinetant and elinzanetant (dual NK1/NK3); SSRIs/SNRIs (paroxetine), gabapentin, oxybutynin, clonidine; CBT; cooling/paced respiration. Pharmacogenomics: *TACR3* genotype modulates baseline risk; fezolinetant metabolized to ES259564. Monitor liver enzymes on NK3R antagonists.

**13. Prevention.** No primary prevention of menopause itself. Where oophorectomy is elective, ovarian conservation / salpingectomy-with-ovarian-conservation avoids abrupt surgical VMS (PMID 34295957, 34761721). Tertiary prevention: treat VMS to prevent sleep/mood/QoL sequelae; manage cardiometabolic risk factors. Behavioral: weight management, smoking cessation, physical activity.

**14. Other species.** Not a naturally occurring disease, but the **ovariectomized rat (NCBI Taxon 10116)** and mouse (10090) with tail-skin-temperature readout model the thermoregulatory physiology; orthologs *Tacr3*, *Tac3*, *Kiss1*. No veterinary natural-disease counterpart; no zoonosis.

**15. Model organisms.** Primary induced model: **OVX rat ± NK3-saporin KNDy ablation** (PMID 23150555) — recapitulates estrogen-dependent cutaneous vasodilation and KNDy requirement; limitation: rodents lack subjective hot-flash report; TSKIN is a proxy. Mouse *Tacr3*/*Kiss1* genetic models inform receptor biology.

---

## Evidence Base

| PMID | Study / type | How it supports the findings |
|---|---|---|
| [23872331](https://pubmed.ncbi.nlm.nih.gov/23872331/) | Rance — mechanism review | KNDy→NK3R→preoptic heat-defense; KNDy ablation reduces vasodilation |
| [40330614](https://pubmed.ncbi.nlm.nih.gov/40330614/) | 2025 thermoregulation review | Full causal chain; prevalence 50–80%; induced menopause worst |
| [42045091](https://pubmed.ncbi.nlm.nih.gov/42045091/) | Elinzanetant review | NKB–NK3R as primary mediator |
| [25686030](https://pubmed.ncbi.nlm.nih.gov/25686030/) | SWAN natural history | Median duration 7.4 y; African American longest (10.1 y) |
| [38595299](https://pubmed.ncbi.nlm.nih.gov/38595299/) | SWAN | Discrimination → VMS in Black women (OR ~1.55–1.57) |
| [28231077](https://pubmed.ncbi.nlm.nih.gov/28231077/) | WHI trans-ethnic GWAS | *TACR3* sole genome-wide locus (OR ~1.5) |
| [33906203](https://pubmed.ncbi.nlm.nih.gov/33906203/) | SWAN genomics | *TACR3* rs74827081 protective allele (OR 0.49) |
| [36734148](https://pubmed.ncbi.nlm.nih.gov/36734148/) | SKYLIGHT 2 RCT | Fezolinetant efficacy, LS-mean −2.55 at W4 |
| [41259888](https://pubmed.ncbi.nlm.nih.gov/41259888/) | Pooled SKYLIGHT 1+2 | ≥50% responders 58.7% vs 36.0% (OR 2.54) |
| [26348174](https://pubmed.ncbi.nlm.nih.gov/26348174/) | Review | MHT most effective |
| [30484736](https://pubmed.ncbi.nlm.nih.gov/30484736/) | Review | Timing hypothesis |
| [33841322](https://pubmed.ncbi.nlm.nih.gov/33841322/) | Review | HT risks low for women <60 / within 10 y |
| [14663778](https://pubmed.ncbi.nlm.nih.gov/14663778/) | Review | SSRIs/gabapentin for breast-cancer survivors |
| [38695491](https://pubmed.ncbi.nlm.nih.gov/38695491/) | Real-world survey | VMS–sleep–mood triad worse than VMS alone |
| [37650213](https://pubmed.ncbi.nlm.nih.gov/37650213/) | Preference study | 86.5% severe VMS, 87.8% sleep problems |
| [37577812](https://pubmed.ncbi.nlm.nih.gov/37577812/) | SWAN/MsHeart review | VMS ↔ CVD risk/events |
| [37214424](https://pubmed.ncbi.nlm.nih.gov/37214424/) | Review | VMS ↔ subclinical + clinical CVD |
| [42709460](https://pubmed.ncbi.nlm.nih.gov/42709460/) | SWAN target-trial emulation | MHT in VMS women aHR 0.78 for CVD (timing-dependent) |
| [42339545](https://pubmed.ncbi.nlm.nih.gov/42339545/) | Review | VMS ↔ stroke |
| [23150555](https://pubmed.ncbi.nlm.nih.gov/23150555/) | OVX rat NK3-saporin | KNDy required for cutaneous vasodilation + estrogen effect |
| [24012626](https://pubmed.ncbi.nlm.nih.gov/24012626/) | Freedman mechanism | Narrowed thermoneutral zone; α2-adrenergic |
| [15852197](https://pubmed.ncbi.nlm.nih.gov/15852197/) | Freedman | Estradiol level equal in symptomatic/asymptomatic |
| [42252432](https://pubmed.ncbi.nlm.nih.gov/42252432/) | Meta-analysis | Psychosocial g −0.60 to −0.87 |
| [41462190](https://pubmed.ncbi.nlm.nih.gov/41462190/) | CBT review | CBT improves QoL/VMS/sleep |
| [42084929](https://pubmed.ncbi.nlm.nih.gov/42084929/) | CBT-MI RCT | ↓ ISI, ↓ hot-flash interference |
| [24338340](https://pubmed.ncbi.nlm.nih.gov/24338340/) | Clinical | FSH/estradiol only when in doubt |
| [37671810](https://pubmed.ncbi.nlm.nih.gov/37671810/) | Cohort | VMS severity ↔ T2DM (OR 1.045), BMI, alcohol |
| [34761721](https://pubmed.ncbi.nlm.nih.gov/34761721/) | Toolkit | Surgical menopause → severe symptoms |
| [42610452](https://pubmed.ncbi.nlm.nih.gov/42610452/) | WHO VigiAccess | Hepatic signal (ALT ROR 20.6, AST 22.95) |
| [42547587](https://pubmed.ncbi.nlm.nih.gov/42547587/) | FAERS | Serious liver injury signal |
| [41849128](https://pubmed.ncbi.nlm.nih.gov/41849128/) | Elinzanetant safety | NK3R class hepatic signal; liver monitoring |

---

## Limitations and Knowledge Gaps

- **No disease ontology anchor.** VMS lacks OMIM/MONDO/Orphanet entries; knowledge-base ingestion must use ICD-10-CM N95.1 and MeSH D019584 as proxies, which blur VMS with broader "climacteric states."
- **Causation vs. association for CVD.** The VMS↔cardiovascular/stroke link is consistently observed in prospective cohorts but **not established as causal**; shared upstream vascular/autonomic biology may drive both. The SWAN MHT target-trial emulation suggests benefit but with explicit caution about residual confounding.
- **Central sensitivity unexplained at the molecular level.** Because estradiol levels do not differ between symptomatic and asymptomatic women, the determinants of individual NK3R/noradrenergic set-point sensitivity (beyond *TACR3* genotype) remain incompletely defined.
- **Animal-model proxy limits.** Rodent tail-skin-temperature is an objective effector readout but cannot capture the subjective hot-flash percept or the night-sweat/sleep/mood sequelae.
- **NK3R-antagonist hepatotoxicity.** The hepatic signal is derived largely from disproportionality analyses (FAERS/VigiAccess), which establish signals but not incidence or causation; long-term and oncology-population safety data for fezolinetant/elinzanetant are still maturing.
- **Underrepresentation and disparity drivers.** Mechanistic understanding of why African American women have longer, more severe VMS (beyond discrimination/psychosocial mediation) is incomplete.
- **Epigenetics/metabolic hypotheses unconfirmed.** The NO–HSP70/heat-shock-response hypothesis (PMID 28903474) linking estrogen deficiency to inflammatory disease is intriguing but not mechanistically proven in humans.

---

## Proposed Follow-up Experiments / Actions

1. **Establish causality of the VMS–CVD link** via Mendelian randomization using *TACR3* and reproductive-aging polygenic scores as instruments, and via SWAN target-trial emulations — to determine whether treating VMS (e.g., with NK3R antagonists) alters cardiovascular endpoints.
2. **Prospective hepatic-safety registry** for fezolinetant/elinzanetant with scheduled ALT/AST/bilirubin monitoring to convert pharmacovigilance signals into incidence estimates and identify pharmacogenomic (CYP, *TACR3*) predictors of transaminitis.
3. **Genotype-stratified NK3R-antagonist trials** testing whether *TACR3* risk/protective alleles predict response magnitude — a precision-medicine test of the genetics↔pharmacology convergence.
4. **Dedicated trials in induced/surgical menopause and breast-cancer survivors** (where VMS is most severe and MHT contraindicated), with NK3R antagonists and oncologic safety endpoints.
5. **Mechanistic single-cell/spatial transcriptomics** of human hypothalamic arcuate and preoptic tissue across menopausal status to map KNDy hypertrophy and NK3R expression at cell-type resolution (CELLxGENE / Human Cell Atlas integration).
6. **Head-to-head and combination studies** of CBT + NK3R antagonist vs. either alone, targeting the full VMS–sleep–mood triad rather than hot-flash count alone.
7. **Disparities research** dissecting biological vs. social mediators of the longer VMS course in African American women, integrating discrimination measures with vascular and neuroendocrine phenotyping.

---

*Report compiled from 5 iterations, 12 confirmed findings, and 44 reviewed papers. Evidence types span human cohort studies (SWAN, WHI), randomized controlled trials (SKYLIGHT, OASIS programs), human neuropathology, rodent models (OVX rat), and real-world pharmacovigilance.*


## Artifacts

- [OpenScientist final report](Vasomotor_Symptoms_of_Menopause-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Vasomotor_Symptoms_of_Menopause-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 33 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `UBERON:0002661` (2 mentions) - the report calls it "preoptic area"; UBERON calls it **superior frontal gyrus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001882` (2 mentions) - the report calls it "arcuate nucleus of hypothalamus"; UBERON calls it **nucleus accumbens**, and lists "accumbens nucleus" among its other names
