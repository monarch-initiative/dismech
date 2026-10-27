---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T11:41:24.503968'
end_time: '2026-10-27T11:47:18.911734'
duration_seconds: 354.41
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypogonadotropic Hypogonadism 24 Without Anosmia
  mondo_id: MONDO:0009239
  category: Genetic
  causal_genes: FSHB
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.4.0
term_validation:
  total_terms: 24
  verified: 21
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 2
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: DOID:0090088
    reported_labels:
    - Disease Ontology
    ontology_label: hypogonadotropic hypogonadism 24 without anosmia
  - term_id: HP:0000044
    reported_labels:
    - Core disease designation
    ontology_label: Hypogonadotropic hypogonadism
  - term_id: HP:0000823
    reported_labels:
    - Very common in females; variable in males
    ontology_label: Delayed puberty
  - term_id: HP:0008214
    reported_labels:
    - Very common in females
    ontology_label: Decreased serum estradiol
  - term_id: HP:0000789
    reported_labels:
    - Defining in reported adults of both sexes
    ontology_label: Infertility
  - term_id: HP:0008734
    reported_labels:
    - "All foundational male cases; volumes 1\u201312 mL/side"
    ontology_label: Decreased testicular size
  - term_id: HP:0000027
    reported_labels:
    - All three foundational molecularly confirmed men
    ontology_label: Azoospermia
  - term_id: HP:0002750
    reported_labels:
    - Listed by disease resources, but disease-specific quantitative evidence is weak
    ontology_label: Delayed skeletal maturation
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypogonadotropic Hypogonadism 24 Without Anosmia
- **MONDO ID:** MONDO:0009239 (if available)
- **Causal gene(s):** FSHB
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Genetic

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 24 Without Anosmia** covering all of the
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

# Research report: Hypogonadotropic hypogonadism 24 without anosmia

## Executive summary

**Hypogonadotropic hypogonadism 24 without anosmia (HH24) is caused by biallelic pathogenic variants in *FSHB*, the gene encoding the hormone-specific β-subunit of follicle-stimulating hormone (FSH).** It is more precisely described as **congenital isolated FSH deficiency**. Loss of functional FSH impairs ovarian follicle maturation in females and Sertoli-cell support of spermatogenesis in males. The characteristic biochemical pattern is **undetectable or very low basal and GnRH-stimulated FSH, high or high-normal LH, and low sex steroids—especially estradiol in females—with otherwise preserved pituitary function**. Females generally have delayed or incomplete puberty, primary amenorrhea and infertility; males have small testes, azoospermia and infertility, but virilization and testosterone can be normal because LH secretion and Leydig-cell function are relatively preserved. [201][62]

The supplied MONDO identifier is correct: **MONDO:0009239**. Contrary to “OMIM not recorded” in the prompt, the current disease phenotype entry is **OMIM 229070**; *FSHB* itself is OMIM **136530**. “Without anosmia” should be interpreted literally for the *FSHB*-specific disorder: anosmia is not an established feature of isolated FSH deficiency, despite some broad database labels saying “with or without anosmia.” [16][17][25]

Evidence remains limited to small numbers of families, case reports, in-vitro functional studies and animal models. No population-level natural-history study, disease-specific randomized trial, gene therapy, single-cell disease atlas or validated prognostic model has been reported. As of September 7, 2026, no ClinicalTrials.gov study was registered specifically for isolated FSH deficiency. [374]

---

## 1. Disease information

### 1.1 Definition and classification

HH24 is a rare, congenital, autosomal-recessive endocrine disorder in which loss of the *FSHB*-encoded β-subunit prevents formation or secretion of biologically active FSH. Unlike most congenital hypogonadotropic hypogonadism, the defect is at the level of a **single pituitary gonadotropin**, not GnRH neuronal development or generalized pituitary failure. LH secretion is preserved and commonly elevated because low gonadal steroids reduce negative feedback. [3][67]

The most phenotype-specific name is **isolated follicle-stimulating hormone deficiency**. Orphanet defines it as:

> “A rare congenital hypogonadotropic hypogonadism characterized by hypogonadism due to selective deficiency of follicle stimulating hormone (FSH).” [201]

### 1.2 Identifiers and synonyms

| Database or terminology | Identifier/name |
|---|---|
| MONDO | **MONDO:0009239**, hypogonadotropic hypogonadism 24 without anosmia |
| OMIM phenotype | **229070**, hypogonadotropic hypogonadism 24 without anosmia |
| OMIM gene | **136530**, *FSHB* |
| Orphanet | **ORPHA:52901**, isolated follicle stimulating hormone deficiency |
| MedGen/UMLS concept | **C5574957**, MedGen 1806136 |
| Disease Ontology | **DOID:0090088** |
| ICD-10 | **E23.0**, hypopituitarism, as mapped by Orphanet; some secondary resources use E23.6 |
| ICD-11 | **5A61.0**, hypopituitarism; includes isolated FSH deficiency |
| MeSH | No disease-specific descriptor identified; use **Hypogonadism, D007006**, whose entry terms include hypogonadotropic and isolated hypogonadotropic hypogonadism |
| KEGG Disease | **H01253**, isolated follicle-stimulating hormone deficiency |
| SNOMED CT | No consistently exposed disease-specific code found in the reviewed sources |
| NCBI Gene | *FSHB*, **Gene ID 2488** |
| HGNC | **HGNC:3964** |
| Ensembl | **ENSG00000131808** |
| UniProt | **P01225**, follitropin subunit beta |

The disease and gene cross-references are supported by MedGen, Orphanet and HGNC/GenCC. [16][201][164][208]

**Synonyms**

| Synonym |
|---|
| Isolated follicle-stimulating hormone deficiency |
| Isolated FSH deficiency |
| Follicle-stimulating hormone deficiency, isolated |
| FSHB-related hypogonadotropic hypogonadism |
| FSHB hypogonadotropic hypogonadism |
| HH24 |
| Hypogonadism, hypogonadotropic, type 24, without anosmia |

### 1.3 Evidence provenance

This entry is an **aggregated disease-level synthesis**, not an individual EHR record. Its foundational evidence consists of individually published patients and families, ClinVar/OMIM assertions, Orphanet curation, in-vitro expression studies, and *Fshb*-null animal models. The rarity and case-based ascertainment mean that database frequencies should not be treated as unbiased epidemiologic estimates.

---

## 2. Etiology

### 2.1 Primary cause

The established cause is **germline biallelic loss of function in *FSHB***—homozygous or compound-heterozygous nonsense, frameshift or disruptive missense variants. Heterozygous relatives in reported families generally had normal puberty and fertility, supporting recessive inheritance. [150][314]

There is no established infectious, toxic, nutritional or autoimmune cause of genetically defined HH24. Acquired pituitary disease and functional suppression of the hypothalamic-pituitary-gonadal axis are differential diagnoses, not causes of *FSHB*-related HH24.

### 2.2 Genetic risk factors

| Factor | Evidence and interpretation |
|---|---|
| Biallelic pathogenic *FSHB* variants | Necessary and sufficient in molecularly confirmed HH24; strongest established risk factor |
| Consanguinity | Enriches homozygous recessive variants; reported in Brazilian, Kashmiri and Chinese families, among others [150][329] |
| Family history | May show affected siblings but frequently appears negative because carriers are clinically normal |
| *FSHB* c.-211G>T, rs10835638 | Common regulatory susceptibility allele associated with lower FSH and altered male reproductive parameters, but **not sufficient to diagnose HH24**; it is better regarded as a quantitative modifier of FSH secretion [44] |
| Digenic/oligogenic modifiers | Not established for molecularly confirmed isolated FSH deficiency |
| *FSHR* variation | Can modify response to exogenous FSH in broader infertility populations, but is not a proven modifier of HH24 penetrance |

A 2024 case combined an AZFc Y-chromosome deletion with homozygous *FSHB* −211T and low FSH. The patient improved sufficiently after FSH 150 IU three times weekly for six months to cryopreserve motile sperm. This is relevant to pharmacogenetic infertility research, but it is **not a case of classic biallelic *FSHB* loss-of-function HH24**. [130][383]

### 2.3 Environmental and lifestyle risk factors

No environmental exposure is known to cause the Mendelian disorder. Obesity, undernutrition, excessive exercise, severe systemic illness, stress, medications, pituitary trauma, radiation and tumors can cause acquired or functional hypogonadotropic hypogonadism and may worsen reproductive function, but they are phenocopies or comorbid influences rather than causes of *FSHB*-related HH24.

### 2.4 Protective factors

No genetic allele is known to protect against disease when two pathogenic *FSHB* alleles are present. Potentially protective clinical factors are indirect:

- early recognition and sex-steroid replacement during adolescence;
- adequate calcium and vitamin D;
- weight-bearing exercise;
- avoidance of smoking and excessive alcohol;
- prompt fertility-directed FSH replacement.

These measures reduce complications but do not prevent the underlying genetic deficiency.

### 2.5 Gene–environment interaction

No disease-specific gene–environment interaction has been demonstrated. Nutrition, exercise, illness and gonadotoxic exposure may affect residual gonadal function or treatment response, but no reproducible interaction with pathogenic *FSHB* genotype has been established.

---

## 3. Phenotypes

Published counts are too small for reliable percentages. Historical reviews initially summarized six affected females and three males, but later reports added a Chinese man, two Kashmiri sisters and a Chinese woman. Ascertainment strongly favors severely affected infertile individuals. [314][329][345]

### 3.1 Core phenotype table

| Phenotype/type | Typical onset, severity and course | Reported frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Selective FSH deficiency—laboratory abnormality | Congenital defect; recognized at puberty or fertility assessment; persistent without replacement | Defining/obligate in confirmed disease | Gonadotropin deficiency, **HP:0008213**; decreased circulating FSH |
| Absent FSH response to GnRH—laboratory abnormality | Demonstrable at diagnostic testing; stable | Reported in essentially all tested molecularly confirmed cases | Abnormal circulating gonadotropin concentration |
| Elevated basal and stimulated LH—laboratory abnormality | Emerges with loss of gonadal negative feedback; stable or treatment-responsive | Very common; all five women tested in an early series had marked LH responses | Elevated luteinizing hormone, **HP:0011969** |
| Hypogonadotropic hypogonadism—clinical/laboratory | Pubertal or adult presentation; variable severity | Core disease designation | **HP:0000044** |
| Delayed or absent puberty—clinical sign | Adolescence; absent to partial development | Very common in females; variable in males | **HP:0000823** |
| Primary amenorrhea—symptom/sign | Adolescence; persistent without treatment | Reported in all published genetically confirmed females in the foundational series | **HP:0000786** |
| Absent or incomplete breast development—physical sign | Adolescence; Tanner I–III across cases | Common but variably expressed | Abnormal breast development / absent breast development |
| Low estradiol—laboratory abnormality | Adolescence/adulthood; improves with FSH or estrogen | Very common in females | **HP:0008214** |
| Small uterus and ovaries—imaging/physical manifestation | Seen after failed pubertal development | Common in more severe females | Uterine hypoplasia; ovarian hypoplasia |
| Arrested follicular maturation—histologic/imaging manifestation | Persistent without FSH | Primordial/preantral follicles preserved; mature follicles absent | Abnormal ovarian follicle morphology |
| Infertility—functional outcome | Adult reproductive period | Defining in reported adults of both sexes | **HP:0000789** |
| Small testes—physical sign | Puberty/adulthood; severity variable | All foundational male cases; volumes 1–12 mL/side | **HP:0008734** |
| Azoospermia—laboratory/functional abnormality | Adult fertility assessment; persistent without successful replacement | All three foundational molecularly confirmed men | **HP:0000027** |
| Oligospermia/partial spermatogenesis | Possible after treatment or in milder disease | Less common; spermatocytes appeared after one year of FSH in one man | Oligozoospermia |
| Normal or low testosterone—laboratory abnormality | Variable; reflects preserved LH/Leydig function | Normal in two foundational men, low in one | Decreased circulating testosterone |
| Normal male virilization | Puberty | Present in several men despite azoospermia; one severe man lacked puberty | Not an abnormal HPO phenotype; annotate as explicitly absent hypovirilization where appropriate |
| Low inhibin B—laboratory abnormality | Adult male or female testing | Documented in tested men and some women; reflects Sertoli/granulosa dysfunction | Decreased circulating inhibin B |
| Delayed skeletal maturation | Adolescence | Listed by disease resources, but disease-specific quantitative evidence is weak | **HP:0002750** |
| Decreased muscle mass/scant body hair | Adolescence/adulthood | Occasional, especially with low sex steroids | **HP:0003199** and abnormal secondary sexual characteristics |
| Normal olfaction | Lifelong | Expected in isolated *FSHB* disease | Anosmia explicitly absent |

Orphanet summarizes women as having primary amenorrhea, absent/incomplete breast development and infertility, and men as having small testes, azoospermia and infertility. [179] The older detailed human series found that all six women had primary amenorrhea, low FSH, low estradiol and elevated LH, while all three men had azoospermia and low nonresponsive FSH. [67]

### 3.2 Sex-specific variability

**Females.** Severity ranges from absent breast development to Tanner stage III. Ovarian reserve can be partly preserved: primordial follicles and sometimes small antral follicles remain, and AMH may be normal despite very low FSH. This explains why appropriately monitored exogenous FSH can produce follicular growth.

**Males.** The phenotype ranges from absent puberty with testosterone 130 ng/dL and 1–2 mL testes to normal puberty, normal testosterone and moderately reduced testicular volume. Spermatogenesis is much more consistently affected than androgenization. Histology has shown spermatogenic arrest, germ-cell aplasia, small seminiferous tubules, peritubular fibrosis, scant Sertoli cells and Leydig-cell hyperplasia. [67]

Cryptorchidism is not typical of the early cases but was present in the Chinese man with p.Arg115Ter. [314]

### 3.3 Quality-of-life impact

No validated HH24-specific EQ-5D, SF-36 or PROMIS cohort exists. Expected and documented impacts from congenital hypogonadism include:

- distress from delayed puberty and discordance with peers;
- infertility-related anxiety, depression and relationship stress;
- reduced libido and sexual function where sex steroids are deficient;
- treatment burden and prolonged specialist follow-up;
- reduced bone mineral acquisition and risk of osteopenia when estrogen or testosterone remains low.

In a broader study of women with congenital GnRH deficiency—not isolated *FSHB* disease—30 of 55 had depressive symptoms and more than half had a gap in care of at least one year. These statistics should be treated as contextual rather than HH24-specific. [246]

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Attribute | Value |
|---|---|
| Gene | *FSHB*, follicle-stimulating hormone subunit beta |
| HGNC | HGNC:3964 |
| NCBI Gene | 2488 |
| Ensembl | ENSG00000131808 |
| OMIM gene | 136530 |
| Chromosomal position | 11p14.1 |
| UniProt | P01225 |
| Protein | 129 amino acids: 18-aa signal peptide plus 111-aa mature β-subunit |
| Expression | Principally anterior-pituitary gonadotrophs |
| Localization | Secreted glycoprotein hormone subunit |
| Key post-translational features | N-linked glycosylation; six conserved disulfide bonds; cystine-knot/“seatbelt” structure |
| Partner | Common glycoprotein α-subunit, CGA |
| Receptor for mature hormone | FSHR on ovarian granulosa and testicular Sertoli cells |

The human gene is protein coding, at 11p14.1, with HGNC:3964, NCBI Gene 2488 and UniProt P01225. [164][166]

### 4.2 Established or strongly supported disease variants

HGVS differs across historical papers because many numbered the mature protein rather than the signal peptide. The table uses current full-length protein numbering where documented.

| *FSHB* variant | Type/classification | Patients and phenotype | Functional evidence |
|---|---|---|---|
| **c.236_237delTG, p.Val79fs**; historically Val61X | Frameshift; ClinVar pathogenic | Multiple females with absent/partial puberty and amenorrhea; one severely affected male | No measurable immunoreactive or bioactive FSH in CHO-cell studies |
| **c.205T>G, p.Cys69Gly**; historically Cys51Gly | Missense; ClinVar pathogenic | Compound heterozygous with p.Val79fs in a female with absent breast development and amenorrhea | Disrupts conserved cysteine/disulfide structure; no measurable immunoreactive or bioactive FSH [134] |
| **c.282C>A, p.Tyr94Ter**; historically Tyr76X | Nonsense; ClinVar pathogenic | Brazilian sister and brother: partial/full puberty respectively, amenorrhea/azoospermia | No measurable immunoreactive or bioactive FSH [150] |
| **c.298T>C, p.Cys100Arg**; historically Cys82Arg | Missense; ClinVar pathogenic | Serbian man with normal puberty, small testes and azoospermia | Later expression studies found absent immunoreactive and bioactive FSH [22] |
| **c.289delG, p.Ala97fsTer127**; historical Ala79fs108X | Frameshift; pathogenic functional evidence | Spanish woman with partial breast development, primary amenorrhea and infertility | No measurable immunoreactive or bioactive FSH; recombinant FSH caused ovarian response and hyperstimulation [90] |
| **c.343C>T, p.Arg115Ter** | Nonsense; ClinVar likely pathogenic | Chinese man with cryptorchidism and infertility; two Kashmiri sisters with absent puberty and amenorrhea | Predicted truncation of 14 C-terminal residues; segregation in multiple families; treatment response in male [314][329] |
| **p.Arg97Ter**, reported as CGA→TGA | Nonsense; strong case-level/functional evidence; full HGVS cDNA not given in the original report | Chinese woman, primary amenorrhea, Tanner III breasts, infertility | Mutant RNA and intracellular protein present, but no secreted immunoreactive FSH and no FSHR-mediated cAMP activity; structural modeling predicted disruption of dimer stability [345] |

All well-characterized historical variants lie in exon 3 and cause absent or severely impaired FSH production or secretion. The detailed functional review’s abstract-level conclusion was that these variants produced “unmeasurable immune- and bioactive FSH.” [40]

**Population frequency.** Reliable ancestry-specific gnomAD frequencies were not available in the retrieved records. The disease alleles are individually very rare and were usually identified in homozygous state in consanguineous or geographically restricted families. Absence or extreme rarity in population databases is expected but should be verified against the current gnomAD release during clinical interpretation.

**Origin.** These are constitutional **germline** variants. No somatic mechanism is implicated.

### 4.3 Other variants and susceptibility alleles

ClinVar also contains VUS and benign/likely benign *FSHB* variants. These must not be conflated with causal HH24. The promoter variant **c.-211G>T/rs10835638** lowers FSH quantitatively and may influence semen parameters or response to FSH, but it has population-level effects and does not by itself establish this recessive disease. [43]

### 4.4 Penetrance, modifiers and epigenetics

- Penetrance for infertility and severe FSH deficiency appears high in biallelic loss-of-function carriers, but the degree of pubertal development is variable.
- No validated modifier gene explains why some males virilize normally and others do not.
- Residual assay-undetectable FSH, LH action, intra-gonadal paracrine signaling and age are plausible modifiers.
- No disease-specific DNA methylation, histone modification or imprinting defect has been established.
- No recurrent pathogenic chromosomal deletion, inversion or translocation defines HH24.

---

## 5. Environmental, lifestyle and infectious information

| Category | Disease-specific conclusion |
|---|---|
| Toxins/pollution/radiation | No established causal role in genetic HH24 |
| Smoking/alcohol | May impair general fertility or bone health but does not cause *FSHB* deficiency |
| Diet/exercise | Extreme energy deficit can cause functional hypothalamic amenorrhea, an important phenocopy; it does not explain the selective high-LH/absent-FSH pattern |
| Obesity | Can alter reproductive hormones and semen quality but is not an established cause |
| Medications | Opioids, glucocorticoids and sex steroids may suppress the axis and confound testing |
| Infection | No infectious agent causes or triggers *FSHB*-related HH24 |
| Occupational exposure | None established |
| Autoimmunity | Anti-FSH antibodies have been reported in non-genetic isolated FSH-deficiency phenotypes, but are not the mechanism of HH24 |

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Biallelic germline loss-of-function variants in *FSHB*** lead to truncation, disruption of conserved cysteines, misfolding or failure of the FSHβ subunit to assemble normally with CGA.

2. **Defective FSHβ folding/heterodimerization or secretion** results in absent or severely reduced circulating immunoreactive and biologically active FSH.

3. **Loss of FSH binding to FSHR** leads to deficient Gαs–adenylyl cyclase–cAMP–PKA signaling in ovarian granulosa cells and testicular Sertoli cells; reduced PI3K-AKT and ERK/MAPK signaling is also inferred from normal FSHR biology.

4. **Female branch:** impaired granulosa-cell proliferation, aromatase induction and differentiation leads to reduced estradiol and inhibin B and arrest of follicular development before full antral/preovulatory maturation.

5. **Female clinical branch:** low estradiol and failed follicular maturation result in incomplete breast development, small estrogen-deprived reproductive organs, primary amenorrhea, anovulation and infertility.

6. **Male branch:** loss of FSH-dependent Sertoli-cell proliferation and trophic support leads to reduced Sertoli-cell number/function, low inhibin B, small seminiferous tubules and failure or arrest of spermatogenesis.

7. **Male clinical branch:** impaired spermatogenesis results in small testes, azoospermia and infertility; preserved LH→Leydig-cell signaling often maintains testosterone and virilization.

8. **Feedback branch:** reduced estradiol/inhibin B or Sertoli/granulosa feedback leads to increased GnRH drive and elevated LH, but the mutant pituitary cannot produce a normal FSH response.

9. **Long-term downstream branch:** untreated sex-steroid deficiency is inferred to lead to impaired bone-mass acquisition, adverse body composition and psychosocial morbidity; these outcomes are established for hypogonadism generally but have not been quantified specifically in HH24.

### 6.2 Molecular and cellular detail

Mature FSH is a noncovalent α/β heterodimer. The β-subunit confers receptor specificity. Conserved disulfide bonds stabilize a cystine-knot structure and a “seatbelt” that wraps around the α-subunit. Missense substitution of conserved cysteines or C-terminal truncation destabilizes this structure and can prevent secretion of active hormone.

FSH binds FSHR, a seven-transmembrane GPCR. The canonical pathway is:

**FSH–FSHR → Gαs → adenylyl cyclase → cAMP → PKA → CREB and steroidogenic/differentiation gene transcription.**

FSHR can additionally activate PI3K-AKT, ERK1/2, RAS and GSK3β signaling. WikiPathways WP2035 summarizes that FSHR is expressed on granulosa and Sertoli cells and that FSH signaling increases cAMP and activates PKA/PKB/PKC and CREB/FOXO1. [296]

In the ovary, FSH normally induces:

- granulosa-cell proliferation;
- *CYP19A1* aromatase and estradiol production;
- *FSHR* and *CCND2* expression;
- acquisition of LH receptors during terminal follicular differentiation;
- inhibin production and coordinated follicular maturation.

In the testis, FSH acts indirectly on germ cells through Sertoli cells. Sertoli and testosterone signals cooperate to sustain spermatogenesis. [298][309]

### 6.3 Immune, metabolic and tissue-damage mechanisms

- **Immune involvement:** none established in genetic HH24.
- **Inflammation/necrosis:** not primary mechanisms.
- **Metabolism:** low gonadal steroids may secondarily affect bone and body composition; no disease-specific metabolomic signature exists.
- **Tissue damage:** early deficiency is chiefly a failure of maturation and trophic support. Peritubular fibrosis and germ-cell aplasia in some adult testes may represent chronic secondary remodeling.
- **Apoptosis/autophagy:** not demonstrated as primary human disease mechanisms.

### 6.4 Molecular profiling

A pre-single-cell mouse expression study found that *Fshb*-null ovaries retained organized theca cells but had increased granulosa-cell *Fshr* mRNA and decreased aromatase, serum/glucocorticoid-regulated kinase and inhibin/activin-subunit transcripts; granulosa cells failed to acquire LH-receptor expression. [360]

No HH24-specific human:

- single-cell RNA-seq;
- spatial transcriptomic;
- unbiased proteomic;
- metabolomic/lipidomic;
- methylomic;
- multi-omic cohort; or
- CRISPR screen

was identified.

### 6.5 Suggested GO and Cell Ontology annotations

| Mechanism | Suggested ontology terms |
|---|---|
| FSH production/secretion | GO: hormone secretion; GO: peptide hormone processing; GO: protein heterodimerization activity |
| Response to FSH | **GO:0032354**, response to follicle-stimulating hormone |
| Receptor signaling | GO: G protein-coupled receptor signaling; GO: cAMP-mediated signaling; GO: protein kinase A signaling |
| Ovarian effects | GO: ovarian follicle development; GO: granulosa-cell proliferation; GO: estrogen biosynthetic process; GO: ovulation cycle |
| Testicular effects | GO: Sertoli-cell proliferation; GO: spermatogenesis; GO: male gamete generation |
| Gonadotroph | **CL:0000437** |
| Granulosa cell | **CL:0000501** |
| Sertoli cell | **CL:0000216** |
| Leydig cell | Annotate as indirectly affected/preserved target of LH, not a direct FSH target |
| Germ cells | Spermatogonium, spermatocyte and spermatid CL terms as downstream affected populations |

The verified Cell Ontology identifiers include gonadotroph CL:0000437, granulosa cell CL:0000501 and Sertoli cell CL:0000216. [304][308]

---

## 7. Anatomical structures affected

| Level | Structure and role | Suggested ontology |
|---|---|---|
| Primary source organ | Anterior pituitary gonadotrophs synthesize mutant FSHβ; gland architecture and other pituitary hormones are usually normal | Pituitary gland **UBERON:0000007**; anterior pituitary |
| Primary female target | Ovarian granulosa cells and developing follicles | Ovary **UBERON:0000992**; mature ovarian follicle **UBERON:0003982** |
| Secondary female structures | Uterus and breasts are underdeveloped because of low estrogen | Uterus/body of uterus; mammary gland |
| Primary male target | Sertoli cells and seminiferous epithelium | Testis **UBERON:0000473**; seminiferous tubule |
| Secondary male structures | Germ-cell lineages; testicular volume | Spermatogonia, spermatocytes, spermatids |
| Skeletal system | Bone mass and maturation may be secondarily affected by sex-steroid deficiency | Bone/skeleton |
| Subcellular | Secretory pathway—rough ER, Golgi and secretory vesicles—where FSHβ folds, glycosylates, dimerizes and is secreted | GO: endoplasmic reticulum lumen; Golgi lumen; secretory granule; extracellular region |
| Receptor compartment | FSHR at granulosa/Sertoli plasma membrane, with signaling through cytosolic cAMP/PKA complexes | GO: plasma membrane; receptor complex |

Involvement is generally **bilateral and systemic**, not lateralized.

---

## 8. Temporal development and natural history

| Phase | Typical manifestations |
|---|---|
| Fetal/neonatal | Molecular defect is congenital. Classic micropenis and cryptorchidism are not consistent features because LH/testosterone may be preserved; one p.Arg115Ter male had cryptorchidism |
| Childhood | Often clinically silent; follicular and testicular maturation deficits may not yet be obvious |
| Adolescence | Delayed/absent or partial puberty; females fail to menstruate; breast development may remain Tanner I–III; males may have small testes despite virilization |
| Adulthood | Infertility, amenorrhea or azoospermia prompts diagnosis; low bone density, sexual or psychological effects may appear if sex steroids remain low |
| Untreated course | Chronic and lifelong; not episodic |
| With hormone replacement | Secondary sexual characteristics and sex-steroid-dependent health can improve |
| With fertility treatment | Follicular growth/ovulation or partial spermatogenesis may be induced; response is variable and requires months in males |
| Remission | No documented spontaneous molecular remission; treatment-dependent biochemical correction |

The critical intervention windows are adolescence for pubertal induction and peak bone-mass acquisition, and the reproductive period for fertility treatment. Unlike some GnRH-deficiency forms, “reversal” is not expected because the structural *FSHB* lesion remains present.

---

## 9. Inheritance, epidemiology and population

### 9.1 Inheritance

| Feature | Conclusion |
|---|---|
| Mode | **Autosomal recessive** |
| Affected genotype | Homozygous or compound-heterozygous pathogenic *FSHB* variants |
| Carrier phenotype | Usually normal puberty and fertility |
| Recurrence risk | For two confirmed carriers: 25% affected, 50% carrier, 25% unaffected/non-carrier per pregnancy |
| Penetrance | Apparently high for severe FSH deficiency and infertility; precise estimate unavailable |
| Expressivity | Variable, especially pubertal development and testosterone in males |
| Anticipation | Not reported and biologically implausible for these variant classes |
| Germline mosaicism | Not reported; residual theoretical risk after an apparently de novo event |
| Founder effects | No well-established global founder variant; recurrent variants occur in individual consanguineous families |
| Consanguinity | Important enrichment factor |
| Sex limitation | Both sexes are affected; manifestations are sex-specific |

### 9.2 Epidemiology

Orphanet lists prevalence as **unknown**. [210] There is no reliable incidence per 100,000 for molecularly confirmed *FSHB* deficiency.

For context only, congenital hypogonadotropic hypogonadism as a broad category has an estimated incidence of about **1–10 per 100,000 births**, but HH24 is a tiny subset and these figures must not be assigned directly to it. [215] A 2017 report stated that only ten molecularly confirmed patients had been reported up to that point; subsequent published cases have increased the count, but it remains a case-report-level disorder. [314]

No robust evidence supports:

- an ethnicity-specific prevalence;
- a geographic endemic area;
- an accurate male:female ratio;
- a carrier-frequency estimate.

Reported families include Italian, Israeli, US, Brazilian, Serbian, Spanish, Chinese and Kashmiri/Indian ancestry, consistent with worldwide but exceptionally rare occurrence.

---

## 10. Diagnostics

### 10.1 Clinical suspicion

Consider HH24 when either of the following is present:

- female with delayed/incomplete puberty, primary amenorrhea and infertility; or
- male with small testes, azoospermia and infertility, often despite normal virilization,

together with **very low/undetectable FSH and disproportionately normal-high or elevated LH**. Berger et al. concluded:

> “This unusual hormonal profile strongly suggests a defect in the FSH beta-subunit in both sexes.” [62]

### 10.2 Recommended work-up

| Domain | Test and expected result |
|---|---|
| Reproductive hormones | FSH repeatedly very low/undetectable; LH high or high-normal; estradiol low in females; testosterone normal to low in males |
| Dynamic testing | GnRH stimulation: absent or markedly impaired FSH response, exaggerated/preserved LH response |
| Gonadal markers | Inhibin B often low; AMH may be preserved in females |
| Other pituitary axes | Prolactin, TSH/free T4, ACTH/cortisol and IGF-1 generally normal |
| Female imaging | Pelvic ultrasound: small uterus/ovaries, few small follicles or occasionally multicystic ovaries |
| Male testing | At least two semen analyses; azoospermia typical; testicular ultrasound if indicated |
| Bone health | Bone age in adolescents; DXA in prolonged sex-steroid deficiency |
| Neuroimaging | Pituitary/hypothalamic MRI to exclude mass, structural lesion or generalized pituitary disease; typically normal |
| Olfaction | History plus formal smell test if diagnostic uncertainty exists; expected normal |
| Cytogenetics | 46,XX or 46,XY expected; karyotype is useful when Turner or Klinefelter syndrome is in the differential |
| Histology | Ovarian/testicular biopsy is not routinely required; historic findings support follicular or spermatogenic arrest |

A 2020 woman had FSH 0.08 mIU/mL, LH 49.89 mIU/mL and estradiol 16.62 pg/mL; after GnRH, FSH remained below 0.3 while LH exceeded 200 mIU/mL. MRI and other pituitary axes were normal. [345]

### 10.3 Genetic testing strategy

1. **Targeted familial testing** if a pathogenic family variant is known.
2. Otherwise, use a **congenital hypogonadotropic hypogonadism panel** including *FSHB*, rather than beginning with serial single-gene tests when the biochemical pattern is not definitive.
3. Ensure coverage of coding exons, splice junctions and copy-number changes.
4. If panel testing is negative, use exome or genome sequencing with CNV analysis and reanalysis.
5. Confirm candidate variants by an orthogonal method and test parents for phase.
6. Interpret under ACMG/AMP criteria, incorporating recessive segregation and functional evidence.

The NHS/PanelApp clinically reportable CHH genes include *ANOS1, CHD7, FGF8, FGFR1, FSHB, GNRHR, IL17RD, KISS1R, LHB, PROK2, PROKR2, TAC3, TACR3* and *WDR11*. [390] Current commercial panels use NGS with CNV calling, and GTR lists multiple HH panels containing *FSHB*. [397][399]

**Utility by platform**

| Test | Utility |
|---|---|
| *FSHB* sequencing | High when selective absent FSH/high LH pattern is classic |
| Multigene panel | Preferred for genetically heterogeneous delayed puberty/HH |
| WES/WGS | Useful after negative panel, for atypical disease, novel variants or structural/noncoding lesions |
| CMA | Low yield for isolated classic HH24; useful if congenital anomalies or developmental delay suggest a deletion syndrome |
| Karyotype | Differential diagnosis, not detection of point variants in *FSHB* |
| FISH | Not routinely indicated |
| mtDNA testing | Not indicated |
| Repeat-expansion testing | Not indicated |
| RNA sequencing | Research/variant-resolution tool, not standard diagnosis |
| Proteomics/metabolomics/liquid biopsy | No established role |

### 10.4 Differential diagnosis

| Disorder | Distinguishing feature |
|---|---|
| Constitutional delay of growth and puberty | Eventually spontaneous pubertal progression; selective persistent absent FSH/high LH is atypical |
| GnRH-deficiency CHH | Both LH and FSH usually low/inappropriately normal; pulsatile GnRH can restore both |
| Kallmann syndrome | Anosmia/hyposmia and possible olfactory-bulb abnormalities |
| Functional hypothalamic amenorrhea | Energy deficit, exercise/stress; both gonadotropins generally suppressed |
| Pituitary tumor/infiltrative disease | Imaging or additional pituitary deficits |
| Combined pituitary hormone deficiency | Other pituitary axes affected |
| *FSHR* loss of function | FSH elevated rather than absent; ovarian resistance/hypergonadotropic phenotype |
| Primary ovarian insufficiency/Turner syndrome | High FSH and LH |
| Klinefelter syndrome | Small testes, azoospermia, high FSH/LH, 47,XXY |
| Androgen synthesis/action disorders | Abnormal virilization or steroid profile |
| Y-chromosome microdeletion | Male azoospermia with normal/high rather than absent FSH; molecular Y testing |
| Acquired isolated FSH deficiency/anti-FSH antibodies | No biallelic *FSHB* variant; acquired context |

### 10.5 Screening

There is no newborn or population screening program. Appropriate approaches are:

- cascade testing of adult relatives;
- carrier testing for reproductive partners in affected families;
- targeted evaluation of siblings before expected puberty;
- prenatal or preimplantation testing when familial variants are known.

---

## 11. Outcome and prognosis

### 11.1 Survival

No reduced life expectancy or disease-specific mortality has been demonstrated. Five- or ten-year survival statistics do not exist and are not clinically meaningful for this nonlethal endocrine disorder.

### 11.2 Morbidity

The principal untreated morbidity is:

- absent/incomplete puberty;
- infertility;
- azoospermia or anovulation;
- low bone density from prolonged sex-steroid deficiency;
- adverse body composition;
- sexual and psychosocial distress.

### 11.3 Recovery potential

- **Endocrine health:** generally good with appropriate estrogen/progestin or testosterone replacement.
- **Female fertility:** potentially favorable because primordial follicles and ovarian responsiveness can be preserved; successful conception has been reported after gonadotropin treatment.
- **Male fertility:** less predictable. One p.Arg115Ter man had increased testicular volume and spermatocytes in semen after one year of FSH, but full spermatogenesis was not yet demonstrated. [314]
- **Untreated disease:** spontaneous normalization is not expected.

Prognosis probably depends on age at treatment, gonadal size, residual function, duration of untreated deficiency, cryptorchidism and the degree of pre-existing seminiferous damage. No validated prognostic biomarker or calculator exists.

---

## 12. Treatment

Therapy should separate two goals: **pubertal/sex-steroid replacement** and **fertility induction**.

### 12.1 Treatment framework

| Clinical goal | Intervention | Mechanism and evidence | Suggested NCIT intervention concept |
|---|---|---|---|
| Female pubertal induction/maintenance | Low-dose estrogen, gradually increased; add cyclic progestin after breakthrough bleeding or adequate estrogenization | Replaces ovarian steroid deficiency; protects uterus, bone and secondary sexual development | Estrogen Replacement Therapy; Progesterone Therapy |
| Male pubertal induction without immediate fertility goal | Testosterone in gradually increasing doses | Produces virilization and supports bone/muscle; does not correct spermatogenesis | Testosterone Replacement Therapy |
| Female follicular development | Recombinant FSH or urinary FSH, titrated under ultrasound/estradiol monitoring | Directly replaces missing hormone | Follicle Stimulating Hormone Therapy; Ovulation Induction |
| Ovulation trigger | hCG or recombinant LH after adequate follicular growth | Mimics LH surge | Human Chorionic Gonadotropin Therapy |
| Male spermatogenesis | Recombinant FSH, generally for at least 6–12 months; add hCG if testosterone/intratesticular androgen support is inadequate | Stimulates Sertoli cells; hCG stimulates Leydig cells | Gonadotropin Therapy |
| Assisted reproduction | Timed intercourse, IUI, IVF or ICSI depending on gamete response | Bypasses residual fertility barriers | Assisted Reproductive Technology; In Vitro Fertilization; Intracytoplasmic Sperm Injection |
| Bone health | Adequate sex steroids, calcium/vitamin D, exercise; DXA monitoring | Prevents secondary osteoporosis | Bone Density Assessment; Nutritional Supplementation |
| Psychological care | Counseling and fertility-focused psychosocial support | Addresses delayed puberty and infertility burden | Psychosocial Intervention; Genetic Counseling |

### 12.2 Female disease-specific outcomes

The 1993 index woman later conceived after exogenous gonadotropin treatment. [89] In the woman with p.Ala97fs, recombinant FSH induced ovulation but produced signs of ovarian hyperstimulation. [90]

In the 2020 p.Arg97Ter case, urinary FSH was started at 75 IU daily and increased to 150 IU daily. After 13 days, four follicles and estradiol 735 pg/mL were present; hCG triggered ovulation, endometrium reached 14.2 mm, and menstrual bleeding occurred, although pregnancy was not reported. [345]

Because endogenous LH is often high, **FSH monotherapy may be sufficient for follicular growth**, unlike profound GnRH deficiency where both FSH and LH may be needed. Treatment must be individualized.

### 12.3 Male disease-specific outcomes

For typical HH, AUA/ASRM guidance starts hCG to normalize testosterone and adds FSH or an FSH analogue to optimize sperm production. [75] In strictly isolated *FSHB* deficiency with normal testosterone, FSH replacement is mechanistically primary and hCG may not be necessary.

The p.Arg115Ter Chinese man’s testicular volume increased after one year of exogenous FSH, and spermatocytes appeared in seminal samples. [314] This indicates biological response but not a guaranteed pregnancy.

### 12.4 Adverse effects and monitoring

| Treatment | Important risks/monitoring |
|---|---|
| FSH in women | Multifollicular development, ovarian hyperstimulation syndrome, multiple pregnancy; monitor ultrasound and estradiol |
| hCG | Ovarian hyperstimulation in women; gynecomastia, acne, fluid retention or excessive testosterone in men |
| Estrogen/progestin | Thromboembolic and other formulation-dependent risks |
| Testosterone | Erythrocytosis, acne, mood effects; suppresses spermatogenesis and should not be used as fertility therapy |
| Fertility procedures | Procedure-specific risks and psychological/financial burden |

### 12.5 Pharmacogenomics and advanced therapies

*FSHB*/*FSHR* common variants are being studied as predictors of FSH response, but recent expert analysis concludes that evidence is not definitive enough for routine pharmacogenetic dosing. [376]

There is no approved or clinically tested:

- *FSHB* gene replacement;
- CRISPR gene editing;
- mRNA or antisense therapy;
- cell therapy;
- immunotherapy.

Given the availability of replacement FSH and the rarity of disease, advanced molecular therapies remain theoretical.

---

## 13. Prevention

### 13.1 Primary prevention

The molecular lesion cannot be prevented by lifestyle or vaccination. Reproductive options for known carriers include:

- genetic counseling;
- partner testing;
- preimplantation genetic testing for monogenic disease;
- prenatal diagnosis by chorionic-villus sampling or amniocentesis;
- donor gametes.

### 13.2 Secondary prevention

Early detection can prevent prolonged untreated hypogonadism:

- identify delayed puberty by standard pediatric surveillance;
- test FSH, LH and sex steroids promptly;
- screen siblings of affected individuals;
- use cascade genetic testing;
- initiate pubertal induction before prolonged psychosocial and skeletal consequences develop.

### 13.3 Tertiary prevention

- maintain sex-steroid replacement;
- monitor growth, pubertal progression and menstrual or sexual function;
- periodic DXA where deficiency was prolonged;
- optimize calcium/vitamin D and weight-bearing exercise;
- avoid smoking and excessive alcohol;
- offer fertility preservation and reproductive referral;
- prevent ovarian hyperstimulation through low-dose monitored FSH;
- provide mental-health and genetic counseling.

There is no relevant immunization, infectious prophylaxis or public-health environmental intervention.

---

## 14. Other species and natural disease

### 14.1 Orthologs

| Species | NCBI Taxon | Gene/NCBI Gene ID | Relevance |
|---|---:|---:|---|
| Human, *Homo sapiens* | 9606 | *FSHB*, 2488 | Human disease gene |
| House mouse, *Mus musculus* | 10090 | *Fshb*, **14308** | Principal knockout and transgenic model |
| Norway rat, *Rattus norvegicus* | 10116 | *Fshb*, **25447** | Reproductive physiology models |
| Zebrafish, *Danio rerio* | 7955 | *fshb*, **402919** | Gonadotropin-development knockout model |
| Dog, *Canis lupus familiaris* | 9615 | *FSHB*, 485428 | Ortholog; no established homologous natural disease found |
| Cattle, *Bos taurus* | 9913 | *FSHB*, 281171 | Polymorphisms studied for fertility traits |
| Sheep, *Ovis aries* | 9940 | *FSHB*, 443387 | Reproductive biology |
| Horse, *Equus caballus* | 9796 | *FSHB*, 100033829 | Ortholog; no established HH24-like natural disease found |

Ortholog identifiers are summarized by NCBI-linked gene resources. [276][279]

### 14.2 Natural animal disease

No well-established naturally occurring veterinary syndrome directly homologous to human biallelic *FSHB*-related HH24 was identified in OMIA-oriented searches. Livestock *FSHB* polymorphisms have been associated with litter size, semen traits or fertility, but these quantitative traits should not be labeled natural HH24. [282]

There is no zoonotic potential or cross-species transmission because this is an inherited endocrine disorder.

---

## 15. Model organisms

### 15.1 Mouse knockout model

The key model is the germline targeted *Fshb* knockout, **Fshb^tm1Zuk/tm1Zuk** or equivalent null nomenclature, in *Mus musculus*.

| Feature | Female *Fshb*−/− mouse | Male *Fshb*−/− mouse |
|---|---|---|
| FSH | Absent/very low | Absent/very low |
| Fertility | Sterile | Fertile or subfertile, depending on endpoint/background |
| Gonads | Small ovaries; follicular block before antral maturation | Testes about 50–60% smaller |
| Gametogenesis | No mature preovulatory follicles/corpora lutea | All stages can occur, but sperm number and motility are reduced |
| Cyclicity | Absent estrous cycles | Not applicable |
| Uterus | Small/thin | Not applicable |
| LH | Elevated | Usually normal |
| Sertoli/germ cells | Not applicable | Sertoli and germ-cell numbers reduced approximately 30–39%; sperm count reduced about 75% |
| Human-disease fidelity | Strong for female follicular arrest; underestimates the consistent azoospermia seen in affected human males | Important species limitation |

The original study’s conclusion was:

> “FSH-deficient females are infertile due to a block in folliculogenesis prior to antral follicle formation,” whereas males remained fertile despite small testes.  
> Kumar et al., *Nature Genetics*, February 1997, PMID **9020850**. [359]

### 15.2 Rescue models

Pituitary gonadotroph-specific expression of a human *FSHB* transgene completely rescued reproductive phenotypes in null males and females. Ectopic human FSH rescued males more efficiently than females, demonstrating that appropriately regulated pituitary expression is particularly important for female cyclicity. The primary rescue study was published in July 1998, PMID **9645705**. [60][106]

Pharmacologic exogenous FSH also reverses ovarian defects in knockout mice, supporting hormone replacement as mechanism-based treatment.

### 15.3 Zebrafish and other experimental systems

In zebrafish, female *fshb* mutants are subfertile rather than uniformly sterile, while males remain fertile. This demonstrates evolutionary conservation of FSH’s reproductive role but also important species differences in dependence on FSH. [280]

**Cellular models** include:

- CHO cells coexpressing CGA and wild-type or mutant FSHβ to test hormone assembly and secretion;
- FSHR-expressing COV434 granulosa cells to measure cAMP bioactivity;
- structural modeling of mutant α/β heterodimers.

The p.Arg97Ter study found mutant intracellular protein but no secreted immunoreactive FSH and no measurable FSHR-driven cAMP response, directly connecting structural instability to loss of hormone activity. [345]

### 15.4 Model strengths, limitations and applications

| Model | Strength | Limitation | Application |
|---|---|---|---|
| *Fshb* knockout mouse | Reproduces selective FSH deficiency and female follicular arrest | Male mice remain fertile, unlike reported human men | Folliculogenesis, Sertoli biology, hormone replacement |
| Human-*FSHB* transgenic rescue | Establishes causal specificity and cross-species hormone function | Transgene expression may not perfectly model endogenous regulation | Rescue proof, secretion timing |
| Zebrafish knockout | Rapid genetic and reproductive studies | Female phenotype milder; teleost reproductive biology differs | Comparative gonadotropin biology |
| CHO/COV434 assays | Directly tests mutant secretion and bioactivity | Simplified in-vitro context | ACMG functional evidence, structure–function analysis |
| Computational structural models | Explains disrupted cystine knot/dimer interfaces | Predictions require experimental validation | Novel-variant prioritization |

Relevant resources include MGI, IMPC/KOMP/MMRRC for mouse alleles, ZFIN for zebrafish, NCBI Gene and the Alliance of Genome Resources.

---

## Recent developments and research priorities

The most important recent literature is not a new HH24 therapy but refinement of FSH biology, genetic testing and genotype-informed infertility care:

1. **2023:** A man with suspected isolated FSH deficiency acquired spermatogenesis on hMG and his partner conceived naturally after five months, but no pathogenic *FSHB* variant was demonstrated; this supports hormone replacement for the biochemical phenotype, not specifically genotype-confirmed HH24. Published March 15, 2023; PMID **37065358**. [236]

2. **2024:** A combined AZFc deletion and homozygous *FSHB* −211T case partially responded to FSH, illustrating polygenic/combined infertility and potential genotype-guided therapy. Published March 1, 2024. [130]

3. **2024 diagnostic practice:** Modern HH evaluation increasingly uses broad NGS panels with CNV calling and, when negative, exome/genome analysis. *FSHB* remains a high-evidence, clinically reportable recessive gene. [389][390]

4. **Unresolved questions:** true prevalence; complete penetrance; long-term bone and quality-of-life outcomes; optimal male FSH dose/duration; whether early-life FSH can expand Sertoli-cell number; and whether common *FSHB/FSHR* alleles modify treatment response.

The most authoritative interpretation remains that *FSHB*-related HH24 is a highly treatable hormone-deficiency state, but the evidence base is small enough that treatment should be managed by specialist reproductive endocrinology, and variant assertions should rely on segregation plus experimentally demonstrated loss of secreted, bioactive FSH whenever possible.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 11 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0090088` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **hypogonadotropic hypogonadism 24 without anosmia**
- `HP:0000044` (1 mention) - the report calls it "Core disease designation"; HP calls it **Hypogonadotropic hypogonadism**
- `HP:0000823` (1 mention) - the report calls it "Very common in females; variable in males"; HP calls it **Delayed puberty**
- `HP:0008214` (1 mention) - the report calls it "Very common in females"; HP calls it **Decreased serum estradiol**
- `HP:0000789` (1 mention) - the report calls it "Defining in reported adults of both sexes"; HP calls it **Infertility**
- `HP:0008734` (1 mention) - the report calls it "All foundational male cases; volumes 1–12 mL/side"; HP calls it **Decreased testicular size**
- `HP:0000027` (1 mention) - the report calls it "All three foundational molecularly confirmed men"; HP calls it **Azoospermia**
- `HP:0002750` (1 mention) - the report calls it "Listed by disease resources, but disease-specific quantitative evidence is weak"; HP calls it **Delayed skeletal maturation**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000437` (2 mentions) - the report calls it "Gonadotroph"; CL calls it **gonadtroph**, and lists "gonadotroph" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.