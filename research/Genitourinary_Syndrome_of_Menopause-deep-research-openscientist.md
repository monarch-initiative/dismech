---
provider: openscientist
cached: false
start_time: '2026-11-14T18:56:34.699352'
end_time: '2026-11-14T19:11:50.174735'
duration_seconds: 915.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Genitourinary Syndrome of Menopause
  mondo_id: MONDO:0001410 (postmenopausal atrophic vaginitis; the nearest MONDO class,
    which is NARROWER than this concept - GSM also covers the urinary tract)
  causal_genes: none; this is an acquired endocrine condition caused by postmenopausal
    oestrogen withdrawal, not a Mendelian disease
  omim_id: none
  synonyms: GSM; vulvovaginal atrophy; atrophic vaginitis; postmenopausal atrophic
    vaginitis; urogenital atrophy
  category: acquired endocrine / urogenital condition of the menopausal transition
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
  job_id: 43dcb635-5e64-4242-a792-fe74eb44990f
citation_count: 33
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:42907052
  relevance_assessed: 34
  on_topic: 30
  needs_review: true
  validator_version: 0.5.1
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Genitourinary_Syndrome_of_Menopause-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Genitourinary_Syndrome_of_Menopause-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Genitourinary Syndrome of Menopause
- **MONDO ID:** MONDO:0001410 (postmenopausal atrophic vaginitis; the nearest MONDO class, which is NARROWER than this concept - GSM also covers the urinary tract) (if available)
- **Causal gene(s):** none; this is an acquired endocrine condition caused by postmenopausal oestrogen withdrawal, not a Mendelian disease
- **OMIM:** none
- **Synonyms:** GSM; vulvovaginal atrophy; atrophic vaginitis; postmenopausal atrophic vaginitis; urogenital atrophy
- **Category:** acquired endocrine / urogenital condition of the menopausal transition

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Genitourinary Syndrome of Menopause** covering all of the
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

# Genitourinary Syndrome of Menopause (GSM): A Comprehensive Disease Characteristics Report

**Disease:** Genitourinary Syndrome of Menopause (GSM)
**MONDO ID:** MONDO:0001410 (postmenopausal atrophic vaginitis — the nearest MONDO class, narrower than GSM, which also covers the urinary tract)
**OMIM:** None
**Causal gene:** None — this is an acquired endocrine condition, not a Mendelian disease
**Category:** Acquired endocrine / urogenital condition of the menopausal transition

---

## Summary

**Genitourinary Syndrome of Menopause (GSM) is an acquired, chronic, progressive hypoestrogenic condition of the lower urogenital tract. It has no causal gene, no OMIM entry, and no pathogenic variant.** The proximate cause is the menopausal withdrawal of ovarian 17β-estradiol — and, to a lesser but real degree, of androgens and the adrenal precursor DHEA — acting on the estrogen receptor α (**ESR1/ERα**) and androgen receptor (**AR**) in the labia, clitoris, vestibule, vagina, urethra, and bladder trigone. ESR1 is the *mediating* (not *mutated*) molecule: the receptor and its ligand are present in normal physiology, and disease arises from ligand deprivation, not from a genetic lesion. GSM replaced the older term "vulvovaginal atrophy" in a 2014 ISSWSH/NAMS consensus because it more accurately captures the genital, sexual, and urinary symptom domains ([PMID: 25155380](https://pubmed.ncbi.nlm.nih.gov/25155380/); [PMID: 25153131](https://pubmed.ncbi.nlm.nih.gov/25153131/)).

The central causal chain is well supported: falling estradiol reduces ESR1 signalling in the urogenital epithelium → thinning of the stratified squamous epithelium with loss of superficial/intermediate cells and depletion of epithelial glycogen → fewer lactobacilli (which ferment glycogen-derived substrates to lactic acid) → a rise in vaginal pH above ~5 → dysbiosis, impaired mucosal barrier and colonization resistance → genital symptoms (dryness, burning, dyspareunia), sexual dysfunction, and urinary symptoms including recurrent urinary tract infection (UTI). This chain is quantified at multiple steps and is confirmed genetically by Esr1-knockout and epithelial-ESR1 conditional-knockout mouse models, which reproduce vaginal atrophy and loss of glycogen/microbiome/pH control.

GSM is highly prevalent (affecting roughly half of postmenopausal women; 10–47% develop debilitating symptoms), does not spontaneously remit, and imposes substantial quality-of-life and sexual-health morbidity while causing no direct mortality. It is highly treatment-responsive: low-dose vaginal estrogen is first-line and is safe — including, after shared decision-making, in most breast and gynecologic cancer survivors — with intravaginal prasterone (DHEA), the oral SERM ospemifene, and non-hormonal moisturizers/lubricants as alternatives. Because the underlying hormone deficit persists, symptoms recur when treatment stops, making GSM effectively a chronic condition requiring ongoing therapy. This report synthesizes 13 confirmed findings across 64 reviewed papers into a complete disease-characteristics dossier spanning all 15 requested sections.

---

## Key Findings

### 1. Disease Information

GSM is defined by the 2014 ISSWSH/NAMS consensus as **"a collection of symptoms and signs associated with a decrease in estrogen and other sex steroids involving changes to the labia majora/minora, clitoris, vestibule/introitus, vagina, urethra and bladder"** ([PMID: 25155380](https://pubmed.ncbi.nlm.nih.gov/25155380/)). The syndrome includes genital symptoms (dryness, burning, irritation), sexual symptoms (lack of lubrication, discomfort/pain, impaired function), and urinary symptoms (urgency, dysuria, recurrent UTI). Symptoms must be bothersome and not better accounted for by another diagnosis.

- **Identifiers:** MONDO:0001410 (postmenopausal atrophic vaginitis — narrower than GSM); MeSH: "Atrophic Vaginitis" / related menopause terms; ICD-10 N95.2 (postmenopausal atrophic vaginitis); ICD-11 GA30.0; no OMIM, no Orphanet rare-disease number (GSM is common, not rare).
- **Synonyms:** GSM; vulvovaginal atrophy (VVA); atrophic vaginitis; postmenopausal atrophic vaginitis; urogenital atrophy.
- **Information source:** Aggregated disease-level resources (consensus guidelines, cohort studies, RCTs) rather than individual EHR records.

This is an **acquired endocrine condition of hypoestrogenism, not a Mendelian disease** — there is no causal gene. The proximate cause is postmenopausal withdrawal of ovarian 17β-estradiol acting on ESR1 in urogenital tissue (Finding F001).

### 2. Etiology and Risk Factors

**Primary cause:** estrogen (and other sex-steroid) withdrawal. There are **no genetic causal factors, no susceptibility loci, and no modifier genes** established for GSM — it is a physiological consequence of menopause.

**Risk factors / high-risk settings** (Finding F007):
- **Natural menopause** — the universal driver.
- **Iatrogenic / induced hypoestrogenism:** aromatase inhibitors (AIs) profoundly lower estrogen and worsen GSM and dyspareunia ([PMID: 42530772](https://pubmed.ncbi.nlm.nih.gov/42530772/)); risk-reducing salpingo-oophorectomy (RRSO) causes immediate surgical menopause ([PMID: 42998015](https://pubmed.ncbi.nlm.nih.gov/42998015/)); cancer treatment–induced menopause (chemotherapy, radiotherapy, GnRH agonists) ([PMID: 42747249](https://pubmed.ncbi.nlm.nih.gov/42747249/)).
- **Premature ovarian insufficiency (POI) and early menopause** — worldwide prevalence ~3.7% and ~12% respectively; frequently cause GSM ([PMID: 42809454](https://pubmed.ncbi.nlm.nih.gov/42809454/)).
- **Breast cancer survivors on endocrine therapy** — "menopause … is abrupt, severe, and treatment-induced" ([PMID: 42907052](https://pubmed.ncbi.nlm.nih.gov/42907052/)).
- **Other hypoestrogenic states:** lactation, hormonal contraception, gender-affirming (testosterone) therapy, and certain medications ([PMID: 42594495](https://pubmed.ncbi.nlm.nih.gov/42594495/)).
- **Lifestyle:** smoking is a recognized contributor to vaginal atrophy ([PMID: 39772973](https://pubmed.ncbi.nlm.nih.gov/39772973/)).

**Protective factors:** systemic or local estrogen exposure. Sexual activity and non-hormonal moisturizers help maintain tissue health. No protective genetic alleles are described (not applicable to a non-genetic condition).

### 3. Phenotypes

The dominant phenotypes, with HPO suggestions where applicable:

| Phenotype | Type | Frequency (reported) | HPO suggestion |
|---|---|---|---|
| Vaginal dryness | Symptom | 77.2% of GSM cases in one cohort | HP:0030016 (vaginal dryness) |
| Loss of lubrication | Sexual symptom | 78.2% | — |
| Loss of libido | Sexual symptom | 79.3% | decreased libido |
| Dyspareunia | Symptom/sign | Very common | dyspareunia |
| Vulvar itching/burning/irritation | Symptom | Common | HP:0025276 (pruritus-adjacent) |
| Urinary urgency | Symptom | Common | HP:0000012 (urinary urgency) |
| Dysuria | Symptom | Common | HP:0100518 (dysuria) |
| Recurrent UTI | Clinical sign | Common | HP:0000010 (recurrent UTI) |
| Elevated vaginal pH (>5) | Lab abnormality | Characteristic | — |
| Vaginal atrophy / loss of rugae | Physical sign | Characteristic | — |

In a cross-sectional cohort of peri/postmenopausal Chinese-speaking sex workers, **GSM prevalence was 83.1% (49/59), with 59.2% reporting moderate-to-severe symptoms**; the most prevalent symptoms were loss of libido (79.3%), loss of lubrication (78.2%), and vaginal dryness (77.2%); higher severity was significantly associated with lower job satisfaction (p=0.002) and reduced ability to work (p=0.009) ([PMID: 42314595](https://pubmed.ncbi.nlm.nih.gov/42314595/)) (Finding F005). The classic estimate is that **"10–47% of postmenopausal women will develop one or more debilitating symptoms"** ([PMID: 20868405](https://pubmed.ncbi.nlm.nih.gov/20868405/)).

**Onset:** adult/late-onset (perimenopausal/postmenopausal, typically >45–50 y, or earlier with iatrogenic/POI causes). **Severity:** variable (mild to severe). **Progression:** chronic and progressive without treatment, non-remitting. **QoL impact:** substantial — sexual dysfunction, impaired daily function, work impairment, and emotional distress.

### 4. Genetic / Molecular Information

**There is no causal gene, no pathogenic variant, no inheritance, no penetrance, and no genetic testing applicable to GSM.** This section is addressed by identifying the *mediating receptor* rather than any mutation.

**ESR1/ERα (HGNC:3467; estrogen receptor 1)** is the key effector (Finding F008). Although no mutation is involved, loss of ESR1 *signalling* (through ligand withdrawal) is sufficient to produce the core lesion:
- In Esr1-knockout mice, **"vaginal epithelial proliferation was reduced, and the epithelium became atrophic in Esr1KO mice by 29 days of age"** ([PMID: 25653281](https://pubmed.ncbi.nlm.nih.gov/25653281/)).
- Conditional epithelial ESR1 deletion abolishes estrogen-induced epithelial proliferation, cornification, MUC1 expression, glycogen deposition, microbial stability, and pH regulation ([PMID: 41279230](https://pubmed.ncbi.nlm.nih.gov/41279230/)).

The **androgen receptor (AR)** and local intracrine androgen synthesis also contribute (Finding F006): human vaginal smooth muscle cells express steroidogenic enzymes (HSD3β1/β2, HSD17β3/β5, 5α-reductase, sulfotransferase) more abundantly than ovary and can synthesize androgens locally from DHEA — **"short-term DHEA supplementation increased Δ4-androstenedione levels … while increasing testosterone and DHT secretion after longer incubation"** ([PMID: 33247714](https://pubmed.ncbi.nlm.nih.gov/33247714/)).

Modifier genes, epigenetic disease mechanisms, and chromosomal abnormalities: **not applicable / none established.**

### 5. Environmental Information

- **Environmental / iatrogenic factors:** aromatase inhibitors, chemotherapy, radiotherapy, GnRH agonists, oophorectomy — all reduce estrogen and precipitate or worsen GSM (Section 2; [PMID: 42747249](https://pubmed.ncbi.nlm.nih.gov/42747249/)).
- **Lifestyle factors:** smoking (pro-atrophic), hormonal contraceptives, SSRIs, and other medications can contribute to vaginal dryness ([PMID: 39772973](https://pubmed.ncbi.nlm.nih.gov/39772973/); [PMID: 42871806](https://pubmed.ncbi.nlm.nih.gov/42871806/)).
- **Infectious agents:** GSM is **not caused by a pathogen.** However, hypoestrogenic dysbiosis predisposes to secondary infection — recurrent UTI (commonly *Escherichia coli*) and altered vaginal flora. The hypoestrogenism–recurrent-UTI association is better supported than associations with bacterial vaginosis or candidiasis ([PMID: 42959465](https://pubmed.ncbi.nlm.nih.gov/42959465/)).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. **Menopause (ovarian follicular depletion) or iatrogenic ovarian suppression** *leads to* a fall in circulating 17β-estradiol (and, with adrenopause, declining DHEA/androgens).
2. Reduced estradiol *results in* diminished ligand occupancy of **ESR1/ERα** in urogenital epithelial and stromal cells (inferred from receptor biology; demonstrated genetically by Esr1-KO atrophy).
3. Reduced ESR1 signalling *leads to* decreased epithelial proliferation and cornification → **thinning of the stratified squamous epithelium** (loss of superficial/intermediate layers, parabasal predominance), reduced collagen/elastin, reduced vascularity, loss of rugae and elasticity.
4. Epithelial thinning *results in* **depletion of intracellular glycogen** (postmenopausal free glycogen median 0.002 vs premenopausal 0.065 µg/µL, P=0.03).
5. Glycogen depletion *leads to* **loss of lactobacilli** (which depend on glycogen-derived substrates; glycogen correlates with Lactobacillus, premenopausal r=0.68, P<0.0001).
6. Loss of lactobacilli *results in* **reduced lactic-acid production and a rise in vaginal pH** (median 4.6 vs 4.0 premenopausal).
7. Higher pH + thin epithelium *leads to* **dysbiosis, impaired mucosal barrier, and reduced colonization resistance**.
8. Branch A — **Genital/sexual manifestations:** reduced lubrication and fragile epithelium *result in* dryness, burning, dyspareunia, and sexual dysfunction.
9. Branch B — **Urinary manifestations:** the same hypoestrogenism thins the urethral/trigonal epithelium and periurethral tissue and reduces colonization resistance, *leading to* urgency, dysuria, and recurrent UTI (often *E. coli*).

**Molecular / cellular detail.** ESR1-driven transcription controls epithelial proliferation, cornification, MUC1 expression, and glycogen deposition ([PMID: 41279230](https://pubmed.ncbi.nlm.nih.gov/41279230/)). Hormone exposure reprograms barrier and immune gene expression: in reconstructed vaginal epithelium, testosterone yields thinner tissue with altered cornification and changes in tight-junction and chemokine gene expression versus estradiol ([PMID: 42121849](https://pubmed.ncbi.nlm.nih.gov/42121849/)). Downstream, **"hypoestrogenism can weaken vaginal, urethral, and bladder epithelial resilience, reduce Lactobacillus-associated colonization resistance, and impair tissue repair"** ([PMID: 42959465](https://pubmed.ncbi.nlm.nih.gov/42959465/)) (Finding F011).

**Upstream vs downstream:** the hormonal deficit and ESR1 hypofunction are upstream; glycogen loss, dysbiosis, pH rise, and barrier failure are intermediate; infection, inflammation, and symptomatic dryness/dyspareunia/urinary complaints are downstream.

**Ontology suggestions:** GO:0030520 (estrogen receptor signaling pathway); GO:0008544 (epidermis/epithelial development); GO:0005977 (glycogen metabolic process); GO:0006954 (inflammatory response). CL:0000076 (squamous epithelial cell); CL:0000192 (smooth muscle cell). CHEBI:16469 (17β-estradiol); CHEBI:28689 (dehydroepiandrosterone); CHEBI:16330 (dihydrotestosterone).

### 7. Anatomical Structures Affected

GSM localizes to the estrogen/androgen-responsive **lower urogenital tract**: "the labia majora/minora, clitoris, vestibule/introitus, vagina, urethra and bladder" ([PMID: 25155380](https://pubmed.ncbi.nlm.nih.gov/25155380/)) (Finding F009). These structures share a common embryologic origin (urogenital sinus) and ER expression, explaining their co-involvement.

| Level | Structure | UBERON / CL / GO suggestion |
|---|---|---|
| Organ | Vagina | UBERON:0000996 |
| Organ | Vulva (labia, clitoris) | UBERON:0000993 / clitoris |
| Organ | Urethra | UBERON:0000057 |
| Organ | Urinary bladder (trigone) | UBERON:0001255 |
| Tissue | Stratified squamous epithelium | epithelium |
| Cell | Squamous/parabasal epithelial cell | CL:0000076 |
| Cell | Vaginal smooth muscle cell | CL:0000192 |
| Subcellular | Nucleus (ESR1 transcription) | GO:0005634 |

Histologically, estrogen loss causes thinning of the vaginal epithelium, reduced glycogen, decreased collagen/elastin and vascularity, loss of rugae, and reduced lubrication ([PMID: 20868405](https://pubmed.ncbi.nlm.nih.gov/20868405/); [PMID: 39772973](https://pubmed.ncbi.nlm.nih.gov/39772973/)). Involvement is **bilateral/symmetric** (a diffuse tissue response to a systemic hormonal change). Body systems: reproductive/genital and urinary (lower urinary tract); endocrine as the driver.

### 8. Temporal Development

- **Onset:** adult/late-onset, coinciding with the menopausal transition (perimenopause through postmenopause); earlier with iatrogenic menopause or POI. Onset is **insidious and chronic**.
- **Progression:** GSM is a **"chronic, progressive hypoestrogenic condition"** ([PMID: 41892504](https://pubmed.ncbi.nlm.nih.gov/41892504/)) (Finding F005). Unlike vasomotor symptoms, which often improve over time, GSM tends to persist and worsen because the estrogen deficit is permanent.
- **Course:** progressive, non-remitting without treatment; **does not spontaneously remit**.
- **Remission:** treatment-induced only; symptoms recur if therapy stops (Finding F012).
- **Critical window:** early initiation of vaginal estrogen yields stronger cytologic/pH responses; older women (≥60 y) show reduced cytologic responsiveness, though treatment improves symptoms at any age ([PMID: 33038141](https://pubmed.ncbi.nlm.nih.gov/33038141/)).

### 9. Inheritance and Population

- **Epidemiology:** highly prevalent. ~50% of postmenopausal women are affected overall; 10–47% develop debilitating symptoms ([PMID: 20868405](https://pubmed.ncbi.nlm.nih.gov/20868405/)); up to 83.1% in some cohorts ([PMID: 42314595](https://pubmed.ncbi.nlm.nih.gov/42314595/)); even higher among breast cancer survivors on endocrine therapy ([PMID: 42461278](https://pubmed.ncbi.nlm.nih.gov/42461278/)).
- **Inheritance:** **not applicable** — no inheritance pattern, no penetrance, no expressivity, no anticipation, no founder effects, no carrier frequency, no consanguinity role. This is an acquired condition.
- **Sex:** affects individuals with estrogen-responsive female urogenital anatomy (natal females; also relevant to transgender men on testosterone and others in hypoestrogenic states). Sex ratio is not a meaningful metric.
- **Age distribution:** concentrated in peri/postmenopausal women (typically ≥45–50 y), with iatrogenic/POI cases occurring earlier.
- **Geographic distribution:** worldwide, wherever women reach menopause; no endemic pattern. Underdiagnosis and undertreatment are common globally.

### 10. Diagnostics

**Diagnosis is clinical** (Finding F004), based on bothersome symptoms plus objective signs on examination: **"Diagnosis should rely on both patient-reported bothersome symptoms and objective clinical signs identified during physical examination. Assessment tools such as the Vaginal Health Index and Vestibular Trophic Health Score may assist in evaluating disease severity"** ([PMID: 42881642](https://pubmed.ncbi.nlm.nih.gov/42881642/)).

**Objective tools:**
- **Vaginal pH** — rises above ~5 with atrophy.
- **Vaginal Maturation Index (VMI)** — cytologic shift from superficial toward parabasal cells; estrogen therapy shifts VMI toward superficial cells (+31.3 superficial cells in one arm) ([PMID: 38412393](https://pubmed.ncbi.nlm.nih.gov/38412393/)).
- **Vaginal Health Index (VHI)** and Vestibular/Vaginal Trophic Health Score — estrogen raises VHI (~+7 points) while non-hormonal moisturizer does not ([PMID: 38412393](https://pubmed.ncbi.nlm.nih.gov/38412393/)).
- **Vaginal cytology / wet mount** — parabasal cells, sometimes with leukocytes (paradoxical inflammatory picture).

**No genetic testing, karyotyping, FISH, CMA, mtDNA, or repeat-expansion testing is applicable.** Omics diagnostics are research-only (microbiome 16S/metagenomics shows compartment-specific Lactobacillus loss; [PMID: 42858690](https://pubmed.ncbi.nlm.nih.gov/42858690/)).

**Differential diagnosis** is important, particularly for dyspareunia: **"intercourse-related pain may also reflect vestibular, pelvic floor, dermatologic, inflammatory, treatment-related, and psychosocial factors"** ([PMID: 42454524](https://pubmed.ncbi.nlm.nih.gov/42454524/)) (Finding F012). GSM must be distinguished from vulvar dermatoses (lichen sclerosus/planus), vestibulodynia, pelvic floor dysfunction, and infection.

### 11. Outcome / Prognosis

GSM is **non-fatal** — not associated with mortality — but causes substantial chronic morbidity: sexual dysfunction, recurrent UTI, and impaired quality of life and work ability ([PMID: 42314595](https://pubmed.ncbi.nlm.nih.gov/42314595/)) (Finding F012). It is **highly treatment-responsive**: low-dose vaginal estrogen, prasterone, and ospemifene reliably improve symptoms and objective signs ([PMID: 42893492](https://pubmed.ncbi.nlm.nih.gov/42893492/); [PMID: 41892504](https://pubmed.ncbi.nlm.nih.gov/41892504/)). However, **symptoms recur if treatment stops** because the underlying estrogen deficiency persists, so ongoing therapy is required. There is no "cure" short of restoring hormonal signalling. Complications include recurrent UTI and sexual dysfunction. Prognostic factors for cytologic response include younger age at treatment initiation ([PMID: 33038141](https://pubmed.ncbi.nlm.nih.gov/33038141/)).

### 12. Treatment

**First-line: low-dose vaginal estrogen** (Finding F003). **"Low-dose vaginal estrogen significantly improves GSM symptoms — including vaginal dryness, dyspareunia, and irritation — while restoring epithelial integrity and normalizing pH"** ([PMID: 42893492](https://pubmed.ncbi.nlm.nih.gov/42893492/)), with similar efficacy across creams, tablets, inserts, and rings, and no increased risk of CVD, VTE, or malignancy in large cohorts. In a class-level network meta-analysis of 24 trial families (4,958 participants), **local vaginal estrogen was the only class with a confidence interval excluding the null** (SMD 0.34, 95% CI 0.02–0.66) ([PMID: 43000041](https://pubmed.ncbi.nlm.nih.gov/43000041/)).

| Therapy | Class / mechanism | Evidence | NCIT suggestion |
|---|---|---|---|
| Low-dose vaginal estrogen (estradiol, estriol, conjugated) | Local ERα agonist | First-line; only class with CI excluding null in NMA | estrogen therapy |
| Intravaginal prasterone (DHEA 6.5 mg) | Intracrine → local androgens + estrogens | FDA/EMA approved; serum steroids stay postmenopausal | prasterone |
| Ospemifene (oral) | SERM; near-full ERα agonist on vaginal epithelium | FDA-approved for dyspareunia | ospemifene |
| Hyaluronic acid moisturizers / lubricants | Non-hormonal | Symptom relief; first-line for mild/contraindicated | lubricant therapy |
| Energy-based (CO2 laser, radiofrequency) | Tissue remodeling | Benefit shown but weaker; sham-controlled trials negative in some settings | — |

**Pharmacogenomics:** not applicable. **Gene/cell/RNA therapies:** not applicable to routine care (investigational regenerative/exosome approaches exist in animal models, e.g. [PMID: 41275445](https://pubmed.ncbi.nlm.nih.gov/41275445/)).

**Mechanistic rationale for ER agonism** (Finding F008): ospemifene **"is the only agent with a nearly full estrogen agonist effect on the vaginal epithelium while having neutral to slight estrogenic effects in the endometrium"** ([PMID: 25087944](https://pubmed.ncbi.nlm.nih.gov/25087944/)), confirming ERα agonism reverses atrophy.

**Recurrent UTI prevention:** vaginal estrogen reduces recurrent UTI by restoring a Lactobacillus-dominant microbiome; a 2025 multisociety guideline recommends topical (not systemic) estrogen for rUTI prevention ([PMID: 42893492](https://pubmed.ncbi.nlm.nih.gov/42893492/)). **"Vaginal estrogen, by restoring urogenital epithelium and the Lactobacillus-dominant microbiome, is recommended in several guidelines for preventing rUTIs"** ([PMID: 42378201](https://pubmed.ncbi.nlm.nih.gov/42378201/)).

**Cancer survivors** (Finding F007): **"Large observational studies and meta-analyses show no increased risk of breast cancer recurrence or mortality among users, including those with estrogen receptor-positive disease and those on tamoxifen"** ([PMID: 42832731](https://pubmed.ncbi.nlm.nih.gov/42832731/)). The VEMORA RCT showed vaginal estrogen improved dryness/dyspareunia versus moisturizer with low serum estradiol in AI users ([PMID: 42530772](https://pubmed.ncbi.nlm.nih.gov/42530772/)). Maximal caution and shared decision-making are warranted for women on aromatase inhibitors.

### 13. Prevention

- **Primary prevention:** menopausal/vaginal estrogen can prevent urogenital atrophy in at-risk women; smoking cessation; sexual activity maintains tissue health.
- **Secondary prevention:** proactive screening — clinicians should ask about genital/urinary symptoms, which are underreported due to stigma ([PMID: 41892504](https://pubmed.ncbi.nlm.nih.gov/41892504/)).
- **Tertiary prevention:** ongoing vaginal estrogen to prevent recurrent UTI and progression; topical estrogen reduces rUTI recurrence ([PMID: 42378201](https://pubmed.ncbi.nlm.nih.gov/42378201/)).
- **Immunization / genetic screening / genetic counseling:** not applicable.
- **Behavioral:** moisturizers, lubricants, pelvic floor therapy, and continued sexual activity.

### 14. Other Species / Natural Disease

- **Taxonomy:** modeled in *Mus musculus* (NCBI:txid10090) and *Rattus norvegicus* (NCBI:txid10116) via ovariectomy.
- **Orthologous gene:** mouse *Esr1* (NCBI Gene 13982) is orthologous to human ESR1.
- **Natural disease:** GSM as such is a human clinical construct; analogous vaginal atrophy occurs in ovariectomized/aged companion animals, but no formal veterinary disease entity is catalogued. **Not a zoonosis.**
- **Comparative biology:** the ovariectomized (OVX) rat is "a highly predictive model of SERM activity in postmenopausal VVA" ([PMID: 23665515](https://pubmed.ncbi.nlm.nih.gov/23665515/)), indicating conserved estrogen-dependent vaginal epithelial biology.

### 15. Model Organisms

- **Ovariectomized (OVX) rat/mouse** — the standard induced model; reproduces epithelial thinning, reduced glycogen, loss of lubrication, and responds to estrogen/SERMs ([PMID: 23665515](https://pubmed.ncbi.nlm.nih.gov/23665515/); [PMID: 41275445](https://pubmed.ncbi.nlm.nih.gov/41275445/)).
- **Esr1-knockout mouse** — genetic proof that ESR1 loss causes vaginal atrophy ([PMID: 25653281](https://pubmed.ncbi.nlm.nih.gov/25653281/)).
- **Epithelial-ESR1 conditional-knockout mouse** — dissects epithelial ESR1's role in glycogen/microbiome/pH control ([PMID: 41279230](https://pubmed.ncbi.nlm.nih.gov/41279230/)).
- **In vitro reconstructed vaginal epithelium** — models hormone-dependent barrier/immune gene expression ([PMID: 42121849](https://pubmed.ncbi.nlm.nih.gov/42121849/)).
- **Phenotype recapitulation:** OVX models reproduce the atrophy and treatment responsiveness well. **Limitations:** rodent vaginal microbiota differs from the human Lactobacillus-dominant community, so the glycogen→lactobacillus→pH axis is harder to model directly; the human intracrine androgen capacity of vaginal tissue is not fully captured.

---

## Mechanistic Model / Interpretation

The evidence across 13 findings converges on a single coherent model: **GSM is a reversible ESR1-ligand-deficiency syndrome of the urogenital tract** (Finding F013). The receptor is normal; the disease is the predictable consequence of removing its ligand.

```
   MENOPAUSE / iatrogenic ovarian suppression
                 │  (↓ ovarian 17β-estradiol; ± ↓ DHEA/androgens)
                 ▼
     ↓ ESR1/ERα signalling in urogenital epithelium  ◄── [Esr1-KO → atrophy; PMID 25653281]
                 │
                 ▼
   Epithelial thinning (parabasal predominance;        [epithelial-ESR1 cKO
   ↓ collagen/elastin, ↓ vascularity, loss of rugae)    abolishes glycogen/
                 │                                        microbiome/pH control;
                 ▼                                        PMID 41279230]
   ↓ Epithelial GLYCOGEN  (0.002 vs 0.065 µg/µL, P=0.03) [PMID 25535963]
                 │
                 ▼
   ↓ LACTOBACILLI  (glycogen–Lactobacillus r=0.68)      [PMID 25535963]
                 │
                 ▼
   ↑ Vaginal pH (4.6 vs 4.0)  →  DYSBIOSIS, ↓ barrier   [PMID 42959465]
                 │
        ┌────────┴─────────┐
        ▼                  ▼
   GENITAL/SEXUAL      URINARY
   dryness,            urgency, dysuria,
   dyspareunia,        recurrent UTI
   ↓ lubrication       (E. coli)
        │                  │
        └───────┬──────────┘
                ▼
   TREATMENT: low-dose vaginal estrogen (restores ERα signalling,
   glycogen, Lactobacillus, pH) → symptom resolution
   ↳ relapse on cessation (deficit persists)
```

The model is internally consistent and bidirectional: the same intervention (restoring ERα ligand) that reverses each step confirms the causal direction. Treatment restores glycogen, serum estradiol/estrone, and Lactobacillus dominance, with symptom improvement tracking these changes — **"Vaginal glycogen, serum estradiol, and estrone significantly increased in women whose [symptoms] improved"** ([PMID: 29206774](https://pubmed.ncbi.nlm.nih.gov/29206774/)). The androgen/intracrine arm ([PMID: 33247714](https://pubmed.ncbi.nlm.nih.gov/33247714/)) explains why DHEA (prasterone), which is converted locally to both androgens and estrogens, is an effective therapy and why the 2014 consensus deliberately referenced "estrogen **and other sex steroids**."

A broader reframing (Finding F010) notes that identical pathophysiology arises from any hypoestrogenic/hypoandrogenic state — "perimenopause, lactation, hormonal contraception, cancer therapies, gender-affirming hormone therapy, and other medications" ([PMID: 42594495](https://pubmed.ncbi.nlm.nih.gov/42594495/)) — supporting a proposed etiology-based "Genitourinary Syndrome" superclass with menopause as one subtype.

---

## Evidence Base

| PMID | Role | How it supports the model |
|---|---|---|
| [25155380](https://pubmed.ncbi.nlm.nih.gov/25155380/) / [25153131](https://pubmed.ncbi.nlm.nih.gov/25153131/) | Definition | Consensus defining GSM, anatomy, symptom domains |
| [25535963](https://pubmed.ncbi.nlm.nih.gov/25535963/) | Mechanism | Quantifies glycogen drop and glycogen–Lactobacillus–pH axis |
| [29206774](https://pubmed.ncbi.nlm.nih.gov/29206774/) | Mechanism | Estrogen/glycogen restoration tracks symptom improvement |
| [41279230](https://pubmed.ncbi.nlm.nih.gov/41279230/) | Mechanism (mouse) | Epithelial ESR1 coordinates glycogen/microbiome/pH |
| [25653281](https://pubmed.ncbi.nlm.nih.gov/25653281/) | Mechanism (mouse) | Esr1-KO → vaginal atrophy; genetic proof |
| [33247714](https://pubmed.ncbi.nlm.nih.gov/33247714/) | Mechanism | Local intracrine androgen synthesis in vaginal tissue |
| [42959465](https://pubmed.ncbi.nlm.nih.gov/42959465/) | Mechanism | Barrier/colonization-resistance failure → infection |
| [42121849](https://pubmed.ncbi.nlm.nih.gov/42121849/) | Mechanism (in vitro) | Hormone-dependent barrier/immune gene expression |
| [20868405](https://pubmed.ncbi.nlm.nih.gov/20868405/) | Epidemiology | 10–47% debilitating symptoms; histology |
| [42314595](https://pubmed.ncbi.nlm.nih.gov/42314595/) | Epidemiology/QoL | 83.1% prevalence; work-ability impact |
| [41892504](https://pubmed.ncbi.nlm.nih.gov/41892504/) | Clinical | Chronic/progressive; management algorithm |
| [42881642](https://pubmed.ncbi.nlm.nih.gov/42881642/) | Diagnosis | Clinical diagnosis; VHI/trophic scores |
| [38412393](https://pubmed.ncbi.nlm.nih.gov/38412393/) | Diagnosis/treatment | VMI/VHI/pH changes with estrogen vs RF vs moisturizer |
| [33038141](https://pubmed.ncbi.nlm.nih.gov/33038141/) | Treatment | Age affects cytologic responsiveness |
| [42893492](https://pubmed.ncbi.nlm.nih.gov/42893492/) | Treatment | First-line efficacy/safety of vaginal estrogen |
| [43000041](https://pubmed.ncbi.nlm.nih.gov/43000041/) | Treatment (NMA) | Vaginal estrogen only class with CI excluding null |
| [25087944](https://pubmed.ncbi.nlm.nih.gov/25087944/) | Treatment | Ospemifene full ERα agonism on vaginal epithelium |
| [42378201](https://pubmed.ncbi.nlm.nih.gov/42378201/) | Treatment | Vaginal estrogen for rUTI prevention |
| [42832731](https://pubmed.ncbi.nlm.nih.gov/42832731/) | Treatment/safety | No increased recurrence in cancer survivors |
| [42530772](https://pubmed.ncbi.nlm.nih.gov/42530772/) | Treatment (RCT) | VEMORA: vaginal estrogen > moisturizer in AI users |
| [42907052](https://pubmed.ncbi.nlm.nih.gov/42907052/) | Risk factor | Iatrogenic menopause as severe-GSM setting |
| [42594495](https://pubmed.ncbi.nlm.nih.gov/42594495/) | Terminology | Identical pathophysiology beyond natural menopause |
| [42454524](https://pubmed.ncbi.nlm.nih.gov/42454524/) | Diagnosis | Multifactorial dyspareunia / differential diagnosis |
| [23665515](https://pubmed.ncbi.nlm.nih.gov/23665515/) | Model | OVX rat predictive of SERM activity in VVA |

---

## Limitations and Knowledge Gaps

- **Not a genetic disease:** Sections on causal genes, inheritance, penetrance, variants, genetic testing, chromosomal abnormalities, and genetic counseling are **not applicable**. The report addresses ESR1/AR as *mediating* molecules, not disease-causing mutations.
- **Prevalence heterogeneity:** reported prevalence ranges widely (10–47% symptomatic to 83% in selected cohorts) because of differing definitions, populations, and underreporting due to stigma. There is no single authoritative incidence/prevalence figure per 100,000.
- **Microbiome model gaps:** the glycogen→lactobacillus→pH mechanism is quantified in human observational data and partly in mice, but rodent vaginal flora differs from humans, limiting mechanistic modeling of the dysbiosis arm.
- **Energy-based therapies:** CO2 laser and radiofrequency show benefit in some trials but recent sham-controlled RCTs were negative (e.g. [PMID: 42879157](https://pubmed.ncbi.nlm.nih.gov/42879157/)), so evidence is weak/limited.
- **Long-term cancer-survivor safety:** reassuring but based largely on observational data; longer RCTs are needed, especially for aromatase-inhibitor users.
- **Androgen contribution:** the quantitative weight of the androgen/intracrine arm relative to estrogen remains incompletely defined.

---

## Proposed Follow-up Experiments / Actions

1. **Standardize epidemiology:** conduct population-based, consensus-definition prevalence/incidence studies to produce comparable per-100,000 estimates across ages and ethnicities.
2. **Longitudinal microbiome mechanism:** multi-compartment (vaginal, periurethral, urinary) 16S/metagenomic cohorts with paired glycogen, pH, and estradiol to formally test the causal chain and its restoration under therapy (building on [PMID: 42858690](https://pubmed.ncbi.nlm.nih.gov/42858690/)).
3. **Long-term cancer-survivor RCTs:** adequately powered trials of low-dose vaginal estrogen and prasterone in AI users with recurrence/mortality endpoints to resolve residual safety uncertainty.
4. **Define the androgen arm:** dose-ranging intravaginal DHEA/androgen studies with tissue intracrine readouts to quantify androgen vs estrogen contributions.
5. **Energy-device evidence:** high-quality sham-controlled trials before routine CO2-laser/RF adoption, per existing negative results.
6. **Terminology adoption:** evaluate the proposed etiology-based "Genitourinary Syndrome" framework ([PMID: 42594495](https://pubmed.ncbi.nlm.nih.gov/42594495/)) to extend evidence-based care to non-menopausal hypoestrogenic populations.
7. **Implementation science:** address underdiagnosis/undertreatment via structured menopause history-taking and clinician decision support, given documented prescribing gaps.

---

*Report compiled from 13 confirmed findings across 64 reviewed papers. Evidence types span human clinical (consensus, RCTs, cohorts, meta-analyses), model organism (Esr1-KO and OVX rodents), and in vitro (reconstructed vaginal epithelium) sources.*


## Artifacts

- [OpenScientist final report](Genitourinary_Syndrome_of_Menopause-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Genitourinary_Syndrome_of_Menopause-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 34 |
| On topic | 30 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42907052` *(abstract only)*: "menopause … is abrupt, severe, and treatment-induced"
  - closest text in source: "Menopause in breast cancer survivors and high-risk women is abrupt, severe, and treatment-induced"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0001410` (3 mentions) - the report calls it "postmenopausal atrophic vaginitis — the nearest MONDO class, narrower than GSM, which also covers the urinary tract", "postmenopausal atrophic vaginitis — narrower than GSM"; MONDO calls it **postmenopausal atrophic vaginitis**
- `HP:0030016` (1 mention) - the report calls it "vaginal dryness"; HP calls it **Dyspareunia**
- `HP:0025276` (1 mention) - the report calls it "pruritus-adjacent"; HP calls it **Abnormality of skin adnexa physiology**
- `GO:0005634` (1 mention) - the report calls it "Nucleus (ESR1 transcription)"; GO calls it **nucleus**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000010` (1 mention) - the report calls it "recurrent UTI"; HP calls it **Recurrent urinary tract infections**, and lists "Recurrent UTIs" among its other names
- `GO:0008544` (1 mention) - the report calls it "epidermis/epithelial development"; GO calls it **epidermis development**
- `CL:0000076` (2 mentions) - the report calls it "squamous epithelial cell", "Squamous/parabasal epithelial cell"; CL calls it **squamous epithelial cell**
- `CL:0000192` (2 mentions) - the report calls it "smooth muscle cell", "Vaginal smooth muscle cell"; CL calls it **smooth muscle cell**
- `CHEBI:16469` (1 mention) - the report calls it "17β-estradiol"; CHEBI calls it **17beta-estradiol**
- `CHEBI:16330` (1 mention) - the report calls it "dihydrotestosterone"; CHEBI calls it **17beta-hydroxy-5alpha-androstan-3-one**, and lists "DIHYDROTESTOSTERONE" among its other names
- `UBERON:0001255` (1 mention) - the report calls it "Urinary bladder (trigone)"; UBERON calls it **urinary bladder**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0001410` - called "postmenopausal atrophic vaginitis — the nearest MONDO class, narrower than GSM, which also covers the urinary tract", "postmenopausal atrophic vaginitis — narrower than GSM"
- `CL:0000076` - called "squamous epithelial cell", "Squamous/parabasal epithelial cell"
- `CL:0000192` - called "smooth muscle cell", "Vaginal smooth muscle cell"
