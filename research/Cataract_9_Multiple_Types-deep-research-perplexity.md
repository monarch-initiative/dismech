---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T14:37:57.304314'
end_time: '2026-10-27T14:42:57.798232'
duration_seconds: 300.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 9 Multiple Types
  mondo_id: MONDO:0011413
  category: Genetic
  causal_genes: CRYAA
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
citation_count: 51
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 13
  validator_version: 0.4.0
term_validation:
  total_terms: 29
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 2
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: MONDO:0011413
    reported_labels:
    - MONDO
    ontology_label: cataract 9 multiple types
  - term_id: DOID:0110266
    reported_labels:
    - Disease Ontology
    ontology_label: cataract 9 multiple types
  - term_id: HP:0000482
    reported_labels:
    - Variant-dependent; 50/186 patients in the 2024 literature review
    ontology_label: Microcornea
  - term_id: HP:0000568
    reported_labels:
    - 17/186 in the 2024 review; 5/13 in the original p.Arg116Cys family
    ontology_label: Microphthalmia
  - term_id: HP:0000612
    reported_labels:
    - Occasional, especially p.Arg116Cys
    ontology_label: Iris coloboma
  - term_id: HP:0000501
    reported_labels:
    - Occasional with p.Arg12Cys; major lifelong post-surgical risk
    ontology_label: Glaucoma
  - term_id: HP:0000639
    reported_labels:
    - Secondary, especially with dense bilateral disease
    ontology_label: Nystagmus
  - term_id: HP:0000545
    reported_labels:
    - Uncommon/variant-specific
    ontology_label: Myopia
  - term_id: HP:0000256
    reported_labels:
    - Rare and not clearly a consistent CRYAA manifestation
    ontology_label: Macrocephaly
  - term_id: UBERON:0000390
    reported_labels:
    - Embryonal/fetal/nuclear cataract site
    ontology_label: lens nucleus
  - term_id: UBERON:0002444
    reported_labels:
    - Principal protein-dense tissue
    ontology_label: lens fiber
  - term_id: UBERON:0001803
    reported_labels:
    - Anterior monolayer; source of new fibers
    ontology_label: epithelium of lens
  - term_id: UBERON:0005614
    reported_labels:
    - Proliferative/differentiating region
    ontology_label: lens anterior epithelium
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
- **Disease Name:** Cataract 9 Multiple Types
- **MONDO ID:** MONDO:0011413 (if available)
- **Causal gene(s):** CRYAA
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

Please provide a comprehensive research report on **Cataract 9 Multiple Types** covering all of the
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

# Comprehensive disease-characteristics report: Cataract 9, multiple types

**Cataract 9, multiple types (CTRCT9) is a genetically heterogeneous-appearing but molecularly specific lens disorder caused by germline variants in `CRYAA`, the gene encoding αA-crystallin/HSPB4.** It encompasses autosomal-dominant and autosomal-recessive cataracts of widely varying morphology, onset, and severity, sometimes accompanied by microcornea, microphthalmia, iris coloboma, corneal opacity, glaucoma, or other anterior-segment abnormalities. The correct identifiers are **MONDO:0011413, OMIM phenotype 604219, and CRYAA gene OMIM 123580**; the gene entry should not be mistaken for the phenotype number. [1][2]

**Scope note.** Evidence for this entry comes chiefly from aggregated disease databases and small, family-based case series—not population-scale EHR studies. Most variant–phenotype observations involve one pedigree or a few unrelated families, so penetrance estimates and phenotype frequencies should be interpreted cautiously.

---

## 1. Disease information

### Definition

CTRCT9 is an inherited opacity of the crystalline lens caused by pathogenic `CRYAA` variants. Reported morphologies include nuclear, zonular central nuclear, laminar/lamellar, anterior polar, posterior polar, cortical, embryonal, anterior subcapsular, fan-shaped, sutural, and total cataracts. Disease may be congenital, infantile, childhood-onset, or—less often—progressive presenile cataract. Both autosomal-dominant and autosomal-recessive inheritance have been documented. [2][300]

### Identifiers and names

| Resource | Identifier/name | Comment |
|---|---|---|
| MONDO | **MONDO:0011413** | Cataract 9, multiple types |
| OMIM phenotype | **604219** | Cataract 9, multiple types, with or without microcornea |
| OMIM gene | **123580** | `CRYAA` |
| NCBI Gene | **1409** | `CRYAA` |
| HGNC | **HGNC:2388** | CRYAA |
| MedGen | **C1858679** | Cataract 9 multiple types |
| Disease Ontology | **DOID:0110266** | Cataract 9 multiple types |
| Orphanet | **ORPHA:1377** | Cataract–microcornea syndrome; broader than CRYAA because other genes can cause this phenotype |
| ICD-10-CM | **Q12.0** | Congenital cataract; H26.0-series may be used for infantile/juvenile cataract |
| ICD-11 | **LA12.1** | Congenital cataract |
| MeSH supplementary concept | **C565815** | Cataract 9, multiple types / CRYAA-associated hereditary cataract |
| UMLS | **C1858679** | CTRCT9 concept |
| RefSeq | **NM_000394.4**, **NP_000385.1** | Principal clinical transcript/protein |
| UniProt | **P02489** | α-crystallin A chain/HSPB4 |
| Genomic location | **21q22.3** | GRCh38 approximately chr21:43.169–43.173 Mb in OMIM coordinates |

The OMIM phenotype-to-gene mapping is key 3, indicating that the molecular basis is known. [1][4][5][285][287][425][426]

### Synonyms

- Cataract 9, multiple types
- Cataract 9, multiple types, with or without microcornea
- CTRCT9
- Cataract, autosomal-recessive congenital 1
- CATC1, historical designation for the recessive form
- CRYAA-related cataract
- αA-crystallin-related cataract
- CRYAA-associated cataract–microcornea syndrome

“Cataract–microcornea syndrome” is not CRYAA-specific: `CRYBA4`, `CRYBB1`, `CRYBB2`, `CRYGC`, `CRYGD`, `GJA8`, and `MAF` can produce overlapping disease. [2][303]

---

## 2. Etiology

### Primary cause

The defining cause is a **germline pathogenic or likely pathogenic variant in `CRYAA`**. Most dominant cases involve heterozygous missense variants that impair αA-crystallin oligomerization, solubility, chaperone activity, or cytoprotection. Recessive disease has been reported with homozygous nonsense or missense variants, notably p.Trp9Ter and p.Arg54Cys. [61][62][76]

GenCC contributors have classified the `CRYAA`–CTRCT9 relationship as **definitive** for recessive disease, supported by human segregation and experimental evidence; current cataract gene evaluations also regard the dominant relationship as definitive. [106][113]

### Genetic risk factors

- A pathogenic `CRYAA` allele is the principal risk factor.
- Family history is important in dominant pedigrees, but de novo variants and apparently sporadic cases occur.
- Arginine residues—particularly Arg12, Arg21, Arg49, Arg54, and Arg116—are recurrently altered.
- A 2024 systematic review abstract identified **26 unique reported P/LP variants in 186 patients from 41 families**. Eighteen (68%) were missense, 25 (96%) were reported in the heterozygous state, 13 (50%) were in exon 3, and 16 (62%) altered or deleted an arginine residue. The same review found 50 patients with microcornea and 17 with microphthalmia, though reporting was incomplete. Publication: IOVS 2024;65(7):4677, presented May 5–9, 2024. [125]

### Environmental and acquired risk factors

Maternal rubella, CMV, toxoplasmosis, herpesvirus infection, syphilis, radiation, steroids, trauma, and metabolic disease are important **alternative causes of congenital cataract**, but they do not cause the molecularly defined CRYAA disorder. They should therefore be treated as differential diagnoses or potential modifiers rather than primary etiologies of CTRCT9. [196][203]

Oxidative stress, ultraviolet exposure, glycation, and age-related covalent damage destabilize lens crystallins generally. It is biologically plausible that these stresses accelerate opacity in a lens already carrying a partially dysfunctional αA-crystallin, especially in progressive adolescent/adult presentations, but a reproducible human `CRYAA` genotype-by-environment interaction has not been established. [208][209]

### Protective factors

- **Genetic:** No validated protective `CRYAA` allele or modifier gene is known for CTRCT9.
- **Environmental:** UV protection, avoidance of smoking and unnecessary ocular radiation, and metabolic control are reasonable for general lens health but have not been shown to prevent congenital opacity caused by a highly penetrant `CRYAA` variant.
- Maternal rubella immunization prevents infection-related cataract but does not prevent inherited CRYAA cataract. [370]

### Modifiers

No human modifier gene has been validated. Variable disease within families carrying p.Arg21Gln, p.Arg116Cys, or p.Arg116His suggests effects from genetic background, stochastic lens development, allele dosage, or environmental stress, but these remain unproven.

---

## 3. Phenotypes

### Core and associated phenotypes

| Phenotype | Type and characteristics | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Cataract | Primary clinical sign; usually bilateral lens opacity; morphology highly variable | Defining feature | Cataract **HP:0000518** |
| Congenital cataract | Present at birth or identified in early infancy | Common, especially truncating/recessive and many dominant variants | Congenital cataract **HP:0000519** |
| Nuclear cataract | Central/fetal or embryonal nucleus; often congenital or infantile | Commonly reported with p.Arg49Cys and Arg116 variants | Nuclear cataract, use HPO morphology term where available |
| Lamellar/zonular cataract | Opacity confined initially to a lens lamella; may be mild or progressive | p.Arg12Cys, p.Arg21Trp, p.Arg21Gln | Lamellar cataract **HP:0007971** |
| Anterior polar cataract | Central anterior capsular/polar opacity | Reported with p.Arg116His | Anterior polar cataract **HP:0001134** |
| Posterior polar cataract | Posterior pole opacity, sometimes progressing to nuclear/total opacity | p.Arg12Cys and cataract–microcornea syndrome | Posterior polar cataract |
| Cortical/ring-like cataract | Peripheral cortical opacity | p.Gly98Arg begins in the second decade | Cortical cataract |
| Total/white cataract | Complete or near-complete opacity; severe deprivation risk | Homozygous p.Trp9Ter or p.Arg54Cys; progressive p.Gly98Arg | Total cataract |
| Microcornea | Corneal diameter under about 10 mm; usually bilateral | Variant-dependent; 50/186 patients in the 2024 literature review | **HP:0000482** |
| Microphthalmia | Small globe, sometimes congenital | 17/186 in the 2024 review; 5/13 in the original p.Arg116Cys family | **HP:0000568** |
| Iris coloboma | Developmental iris defect | Occasional, especially p.Arg116Cys | **HP:0000612** |
| Corneal opacity | Variable anterior-segment opacity | Reported with p.Arg116His | Corneal opacity |
| Glaucoma | Congenital/secondary or postoperative; not a universal primary trait | Occasional with p.Arg12Cys; major lifelong post-surgical risk | **HP:0000501** |
| Nystagmus | Consequence of early visual deprivation | Secondary, especially with dense bilateral disease | **HP:0000639** |
| Strabismus/amblyopia | Secondary to asymmetric or delayed visual input | Clinically important but not specifically quantified in CRYAA cohorts | Strabismus; amblyopia |
| Reduced visual acuity/blindness | Functional consequence of central/dense opacity or amblyopia | Severity ranges from subclinical to profound | Reduced visual acuity; blindness |
| Myopia | Associated in some CRYAA families | Uncommon/variant-specific | **HP:0000545** |
| Macrocephaly | Reported in one p.Arg12Cys family | Rare and not clearly a consistent CRYAA manifestation | **HP:0000256** |

The disease is usually bilateral, but asymmetry in cataract density, color, and morphology can be substantial even within a single person. [26][308][330][332][333]

### Onset, progression, and severity

- **Congenital/infantile:** p.Trp9Ter, p.Arg49Cys, p.Arg54Cys, many Arg116 variants.
- **Early childhood:** p.Arg21Gln probands were diagnosed at two and 4.5 years.
- **Adolescent/presenile progressive:** p.Gly98Arg caused peripheral ring-like cortical opacity in the second decade, declining distance vision around age 16, and total cataract in the third decade. [77][78]
- **Stable or slowly progressive:** R116C transgenic mouse opacities did not appreciably worsen between 9 and 30 weeks, but human courses vary.
- **Severity:** ranges from slit-lamp-only punctate opacity in carriers to total congenital white cataract requiring surgery during the first three months.

### Quality-of-life impact

Untreated central congenital cataract disrupts visual development, producing deprivation amblyopia, nystagmus, impaired reading/mobility, and potentially irreversible blindness. Even after surgery, children report difficulties across visual function, school, social, emotional, treatment, worry, and physical-discomfort domains. In a study of 107 postoperative children, PedEyeQ scores were lower than controls across all domains; the functional-vision score in children aged 0–4 was **27 points worse** (95% CI −34 to −19). [212][216]

A qualitative study found that visual-function concerns were mentioned by 100% of interviewed children, social concerns by 94%, treatment burden by 81%, and worry by 75%. [210]

---

## 4. Genetic and molecular information

### Gene and protein

| Feature | Annotation |
|---|---|
| Gene | `CRYAA` |
| HGNC | HGNC:2388 |
| NCBI Gene | 1409 |
| Gene OMIM | 123580 |
| Transcript | NM_000394.4 |
| Protein | NP_000385.1; UniProt P02489 |
| Protein name | αA-crystallin; heat-shock protein beta-4/HSPB4 |
| Chromosome | 21q22.3 |
| Structure | Three coding exons; 173-amino-acid protein |
| Principal expression | Lens, especially lens fiber cells |
| Molecular role | ATP-independent small-heat-shock “holdase” chaperone; structural component of the lens; oligomerization with αB-crystallin |
| Cellular localization | Primarily cytosol/protein complexes; stress- and variant-dependent nuclear localization |

α-crystallin complexes contain approximately 30–40 subunits, with αA:αB near 3:1 in the human lens. They bind damaged or partially unfolded proteins and retain them in large soluble complexes rather than ATP-dependently refolding them. [47][51][319]

### Established and recurrent disease variants

HGVS below is normalized to **NM_000394.4** where possible. Classifications can differ among laboratories, so ClinVar should be rechecked at the time of clinical interpretation.

| Variant | Type | Inheritance/zygosity | Clinical association | Current evidence |
|---|---|---|---|---|
| c.27G>A, p.Trp9Ter | Nonsense | AR, homozygous | Severe congenital cataract; surgery in first 3 months | Pathogenic; PMID **11006246** |
| c.34C>T, p.Arg12Cys | Missense | AD, heterozygous | Posterior polar/laminar cataract, microcornea; occasionally macrocephaly, coloboma, glaucoma | ClinVar pathogenic; PMIDs **17724170**, 19503744, 22045060, 23508780 [133] |
| c.61C>T, p.Arg21Trp | Missense | AD | Central laminar cataract and microcornea | P/LP; PMID **17724170** |
| c.62G>A, p.Arg21Gln | Missense | AD, variably penetrant | Lamellar/nuclear cataract of highly variable severity | Pathogenic; PMID **23255486** |
| c.145C>T, p.Arg49Cys | Missense | AD | Congenital/infantile nuclear cataract | Pathogenic; PMID **14512969** |
| c.160C>T, p.Arg54Cys | Missense | AR when homozygous; subtle carrier signs | Congenital total white cataract and microcornea; heterozygotes may have punctate opacities | Pathogenic |
| c.161G>C, p.Arg54Pro | Missense | AD reported | Childhood cataract | ClinVar pathogenic listing |
| c.245C>T, p.Pro82Leu | Missense | Reported in CTRCT9 | Cataract | Clinical significance requires record-level review |
| c.292G>A, p.Gly98Arg | Missense | AD | Progressive teenage cortical/ring opacity to total presenile cataract | Pathogenic; PMID **16862070** |
| c.346C>T, p.Arg116Cys | Missense | AD | Nuclear, zonular, fan-shaped cataract; microcornea/microphthalmia; sometimes coloboma | Pathogenic; PMID **9467006** |
| c.347G>A, p.Arg116His | Missense | AD | Nuclear, anterior polar, cortical, embryonal, fan-shaped or anterior subcapsular cataract; microcornea/corneal opacity | Pathogenic; PMIDs **17724170**, **18302245** |
| c.440del, p.Gln147ArgfsTer48 | Frameshift/elongation | AD | Severe pediatric cataract; elongation variants may cause multiple ocular abnormalities | Likely pathogenic |
| p.Tyr118Asp | Missense | Experimental mouse allele | Nuclear cataract, fiber disorganization and ER-stress/UPR activation | Model allele, not a canonical human CTRCT9 allele |

ClinVar lists, among others, p.Arg49Cys, p.Arg54Cys, p.Arg21Gln, p.Gly98Arg, p.Arg116Cys, p.Arg116His, p.Arg12Cys, p.Arg21Trp, p.Arg54Pro, and p.Gln147ArgfsTer48 as pathogenic or likely pathogenic. [121][129]

**Population frequency.** Causal alleles are individually very rare or absent from reference datasets. For example, p.Arg12Cys was absent from large early control cohorts and p.Arg54Cys was reported around 3.2×10^-5 in one gnomAD-era analysis; ancestry-specific coverage and variant representation must be considered. A variant that is common in gnomAD would be incompatible with a fully penetrant, severe dominant congenital cataract unless reduced penetrance or misclassification were demonstrated. [132][133]

**Origin.** These are constitutional/germline variants. Somatic `CRYAA` variants are not an established cause of CTRCT9.

### Functional consequences

- **Dominant missense alleles:** usually toxic protein misfolding, abnormal oligomerization, dominant-negative interference with wild-type α-crystallin, reduced chaperone activity, and/or enhanced insolubility.
- **Recessive p.Trp9Ter:** severe loss of functional αA-crystallin.
- **p.Arg54Cys:** dosage-dependent; homozygotes have severe congenital disease, while heterozygotes can have subclinical punctate opacities.
- **Frameshift/elongation variants:** appear associated with particularly severe ocular phenotypes in the 2024 review. [125]

### Modifier, epigenetic, and chromosomal findings

- No validated modifier gene or disease-specific epigenetic signature is established.
- Lens differentiation normally involves substantial DNA-methylation and chromatin remodeling, but CRYAA-specific pathogenic methylation has not been demonstrated. [326]
- Isolated CTRCT9 is not ordinarily caused by aneuploidy, translocation, or large CNV. A deletion encompassing `CRYAA` could theoretically produce disease, but routine karyotyping/CMA is low yield when the phenotype is isolated and sequencing identifies a causal allele.

---

## 5. Environmental information

CTRCT9 is not infectious and is not transmissible. No bacterial, viral, fungal, or parasitic agent causes the `CRYAA`-defined disease.

General lens stressors—UV-A/UV-B reaching the lens, ionizing radiation, oxidation, glycation, corticosteroids, diabetes, smoking, and malnutrition—can cause or accelerate other cataracts. Prenatal TORCH infection and teratogens are especially important alternatives in sporadic congenital disease. [196][208]

For knowledge-base representation:

- **Primary causal factor:** germline genetic variant.
- **Environmental contribution:** unproven modifier.
- **Relevant stress process:** reactive oxygen species/oxidative stress.
- **Suggested ChEBI concepts:** reactive oxygen species; hydrogen peroxide; corticosteroid; 25-hydroxycholesterol/oxysterol, the latter only as an experimental therapeutic.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A germline `CRYAA` missense, nonsense, or frameshift variant leads to** reduced quantity or altered folding/charge of αA-crystallin.
2. **Altered αA-crystallin leads to** defective oligomer assembly, impaired subunit exchange, reduced ATP-independent holdase/chaperone activity, and—for many alleles—increased self-association and insolubility.
3. **Loss of soluble chaperone capacity leads to** failure to sequester damaged α-, β-, and γ-crystallins and increased high-molecular-weight protein aggregates.
4. **Protein aggregation and altered crystallin–membrane/cytoskeleton interactions lead to** disorganization of the protein-dense lens-fiber cytoplasm, abnormal fiber architecture, vacuoles, and light-scattering interfaces.
5. **Branch A—proteotoxic stress:** accumulated mutant/unfolded protein **leads to** ER stress and UPR signaling; sustained UPR **results in** apoptosis or proteotoxic death of lens epithelial/fiber cells. This branch is demonstrated in CRYAA-Y118D and R49C mice and cultured cells but is partly inferred for all human alleles.
6. **Branch B—developmental disruption:** impaired αA-crystallin function during anterior-segment/lens development **is inferred to lead to** microcornea, microphthalmia, coloboma, or corneal opacity in allele-specific cases.
7. **Abnormal lens cells and insoluble aggregates lead to** loss of the regular refractive-index gradient and transparency.
8. **Loss of transparency results in** cataract; if central and present during infancy, obscured retinal input **leads to** deprivation amblyopia, nystagmus, strabismus, and persistent reduced vision.

### Protein dysfunction

αA-crystallin is both a structural lens protein and a small heat-shock chaperone. The original R116C report stated:

> “By sequencing the coding regions of CRYAA, we found that a missense mutation, R116C, is associated with ADCC in this family.”  
> Litt et al., *Human Molecular Genetics*, March 1998, PMID **9467006**. [61]

R116C reduces chaperone activity approximately two- to fourfold in aggregation assays, produces polydisperse oligomers, decreases subunit exchange, and increases membrane binding. R49C becomes abnormally nuclear in transfected lens epithelial cells and fails to protect against staurosporine-induced apoptosis. [277][280]

### Proteostasis, UPR, and cell death

R49C knock-in mouse lenses accumulate insoluble αA- and αB-crystallin. Homozygous lenses show increased apoptosis associated with a fivefold reduction in phosphorylated BAD. The study concluded:

> “αA-R49C promotes protein insolubility and cell death in vivo.”  
> Andley et al., 2008, PMID **18056999**. [276]

In Y118D mice, prolonged ER-stress/UPR activation produces severe fiber-cell stress and death:

> “Prolonged activation of the UPR pathway and severe stress response can cause proteotoxic and ERS-induced cell death in CRYAA-Y118D mutant mice.”  
> 2021, PMID **33929105**. [249]

Likely UPR components include HSPA5/BiP release from IRE1, ATF6, and PERK/EIF2AK3, followed by translational attenuation, ER-associated degradation, DDIT3/CHOP induction, and—if unresolved—apoptosis. In R49C homozygous mouse lenses, `Trib3` reportedly increased 509-fold, with increased `Ddit3` and `Chac1`. [275][282]

### Metabolic and molecular profiling

GC-MS profiling of adult R49C knock-in lenses found fewer sugars and minor sterols with increased lactic acid, indicating altered carbohydrate/energy metabolism in addition to protein aggregation. [240]

Transcriptomic/proteomic studies of R49C lenses found:

- altered `Clic5`, `Ddit3`, `Trib3`, and `Chac1`;
- increased histone H2A/H2B/H4 expression with altered H2/H3 abundance;
- increased creatine kinase B—about 16-fold in heterozygous and 22-fold in homozygous two-day-old lenses in one proteomic analysis. [244][245][251]

These findings are model-organism observations; they are not validated human diagnostic biomarkers.

### Recent research, 2023–2024

- A 2024 molecular-dynamics analysis of 19 αA-crystallin mutants found loss of native compactness and increased flexibility, particularly for R12L, R21L/Q, R54L, R65Q, R116C, and R116H. It is computational evidence, not proof of a therapeutic target in patients. Publication: November 1, 2024 online; *Protein Journal* 43:1045–1069; PMID **39485632**. [31]
- A 2024 systematic review abstract summarized 26 P/LP variants in 186 patients and emphasized marked intrafamilial variability and severe phenotypes with elongation variants. [125]
- A 2024 zebrafish study found an important species difference: loss of `cryaa` did not increase age-related cataract prevalence in fish, unlike early cataract in knockout mice. [248][259]
- Human cataract lenses show progressively greater α-crystallin occupancy of cortical and nuclear lens membranes with increasing cataract grade, accompanied by reduced membrane mobility and increased order/hydrophobicity. Publication: February 5, 2024; PMID **38339214**. This concerns broader cataract biology, not specifically germline CTRCT9. [36][41]

### Suggested GO and cell terms

**Molecular function**

- Structural constituent of eye lens — **GO:0005212**
- Protein-folding chaperone — **GO:0044183**
- Unfolded-protein holdase/chaperone activity, where the current GO release supports it

**Biological process**

- Protein folding — **GO:0006457**
- Negative regulation of protein aggregation
- Response to unfolded protein
- Endoplasmic-reticulum unfolded-protein response
- Negative regulation of apoptotic process — **GO:0043066**
- Lens development in camera-type eye
- Lens fiber-cell differentiation
- Cellular response to oxidative stress

**Cellular component**

- Cytosol
- Cytoplasm
- Nucleoplasm
- Protein-containing complex
- α-crystallin complex
- Plasma membrane/lens-fiber membrane, for abnormal binding

**Cell Ontology**

- Lens epithelial cell — **CL:0002224**
- Lens fiber cell — **CL:0011004**
- Primary lens fiber cell — **CL:0002228** [317]

---

## 7. Anatomical structures affected

### Organ and tissue level

The primary organ is the **eye**, specifically the crystalline lens. Associated disease can involve the cornea, iris, and overall globe.

| Level | Structure | Suggested ontology |
|---|---|---|
| Organ | Eye | UBERON:0000970 |
| Primary site | Lens of camera-type eye | **UBERON:0000965** |
| Lens nucleus | Embryonal/fetal/nuclear cataract site | **UBERON:0000390** |
| Lens fibers | Principal protein-dense tissue | **UBERON:0002444** |
| Lens epithelium | Anterior monolayer; source of new fibers | **UBERON:0001803** |
| Anterior lens epithelium | Proliferative/differentiating region | **UBERON:0005614** |
| Cornea | Microcornea/corneal opacity | UBERON cornea term |
| Iris | Coloboma | UBERON iris term |
| Globe | Microphthalmia | UBERON eyeball term |

The normal lens has only two major cell populations: anterior lens epithelial cells and elongated postmitotic lens fiber cells. [315][317][322]

### Subcellular level

Affected compartments include:

- soluble and insoluble cytoplasmic protein complexes;
- lens-fiber cell membranes;
- cytoskeleton and beaded filaments;
- nucleus/nucleoplasm for abnormally localized variants such as R49C;
- ER/UPR apparatus in model-dependent proteotoxic stress;
- apoptotic machinery.

### Lateralization

Disease is usually **bilateral**, but asymmetry is common. Truly unilateral cataract should prompt careful consideration of persistent fetal vasculature, trauma, infection, or mosaic/local developmental causes rather than automatically attributing it to inherited CTRCT9.

---

## 8. Temporal development

### Onset

- Typical: congenital or early childhood.
- Orphanet classifies cataract–microcornea syndrome as neonatal-onset. [285]
- Less typical: progressive teenage or presenile onset, particularly p.Gly98Arg.
- Onset is generally chronic/insidious rather than acute.

### Course

1. **Early/subclinical:** punctate, polar, nuclear, or lamellar opacity.
2. **Intermediate:** enlargement or increasing density; reduced red reflex and visual acuity.
3. **Advanced:** dense central or total cataract, nystagmus/strabismus, deprivation amblyopia.
4. **Post-treatment:** aphakia or pseudophakia with lifelong refractive, amblyopia, and glaucoma surveillance.

Some opacities are stable; others progress from peripheral or polar opacity to total cataract. There is no spontaneous molecular remission documented. Surgery removes the opaque lens but does not reverse amblyopia already established.

### Critical periods

The first weeks and months are critical for visual-system development. Visually significant unilateral congenital cataract is usually treated at approximately **4–6 weeks**, while dense bilateral disease is generally treated by **6–8 weeks**, balancing amblyopia against anesthesia and glaucoma risks. [166][168]

---

## 9. Inheritance and population

### Inheritance

- **Autosomal dominant:** most reported missense and elongation variants.
- **Autosomal recessive:** homozygous p.Trp9Ter and p.Arg54Cys are established examples.
- **Sex-linked/mitochondrial:** not applicable.
- **Anticipation:** not reported.
- **Germline mosaicism:** theoretically possible but not established as a recurrent feature.
- **Consanguinity:** important in recessive families.
- **Founder effects:** p.Trp9Ter was described in an inbred Jewish Persian family; no broadly established population-wide founder allele is known.
- **Sex ratio:** no expected sex bias for an autosomal trait.

### Penetrance and expressivity

Dominant penetrance is often high in pedigrees, but subtle or age-dependent disease may be missed. In the p.Arg21Gln family, an apparently asymptomatic mother, uncle, and grandfather were found to have mild lamellar opacities only after targeted examination. Recessive p.Arg54Cys carriers had clinically insignificant bilateral punctate opacities, showing that “recessive” does not necessarily mean an entirely normal heterozygous lens. [1][92]

Expressivity is markedly variable in cataract type, density, symmetry, onset, progression, microcornea, and microphthalmia.

### Recurrence risks

- Heterozygous dominant affected individual: approximately **50%** risk per pregnancy, subject to penetrance and variant interpretation.
- Two heterozygous recessive carriers: **25% affected, 50% carrier, 25% neither familial allele** per pregnancy.
- Affected individual homozygous for a recessive variant plus unrelated noncarrier partner: children are expected to be carriers, not affected.

### Epidemiology

No reliable CRYAA-specific prevalence, incidence, carrier frequency, geographic distribution, or mortality statistic is available.

For context, pediatric cataract overall has an estimated incidence of **1.8–3.6 per 10,000 children per year** and prevalence of **1–15 per 10,000**; congenital cataract estimates vary substantially by ascertainment. [225][232]

The rarity of individual alleles and ascertainment through specialist clinics prevent defensible ethnic or regional prevalence comparisons.

---

## 10. Diagnostics

### Clinical examination

1. Newborn red-reflex assessment or identification of leukocoria.
2. Urgent pediatric-ophthalmology examination.
3. Dilated slit-lamp examination to document cataract morphology, density, and laterality.
4. Visual behavior/acuity, fixation preference, strabismus, and nystagmus assessment.
5. Corneal-diameter measurement to identify microcornea.
6. Intraocular pressure, gonioscopy when appropriate, and optic-nerve assessment.
7. Axial length and keratometry for surgical planning.
8. B-scan ultrasonography if the cataract prevents fundus visualization, to exclude persistent fetal vasculature, retinal detachment, retinoblastoma, coloboma, or other posterior pathology. [345][358]

There is no diagnostic blood protein or metabolite biomarker for CTRCT9.

### Genetic-testing strategy

**Preferred approach**

1. Sequence a comprehensive bilateral congenital/childhood cataract panel including at minimum `CRYAA`, other crystallins, connexins, membrane proteins, and developmental genes.
2. Ensure deletion/duplication analysis and adequate `CRYAA` coverage.
3. Confirm a reportable variant by an orthogonal method where required.
4. Perform parental/relative testing for segregation and phase.
5. Use WES or WGS if panel testing is negative, the presentation is syndromic, or a structural/noncoding variant is suspected.

A 2023 US cohort found diagnostic yields of **46.2% for WES, 37.5% for targeted cataract panels, and 11% for microarray**. Publication: February 28, 2023; PMID **36980880**. [185]

WGS may detect intronic, regulatory, structural, or poorly covered variants, but no CRYAA-specific evidence shows that it should routinely precede a high-quality panel or exome.

**Low-yield or non-indicated tests for isolated CRYAA cataract**

- Karyotype, FISH, CMA: reserve for multiple congenital anomalies/developmental delay or suspected CNV.
- Mitochondrial sequencing: not routine.
- Repeat-expansion testing: not applicable.
- RNA-seq/proteomics/metabolomics: research rather than clinical diagnostics.

### Laboratory evaluation

In a clear multigenerational CRYAA family, extensive infectious/metabolic testing can be individualized. In sporadic bilateral cataract or unclear systemic disease, testing can include:

- urine reducing substances;
- glucose and galactose/galactokinase evaluation;
- calcium and phosphorus;
- amino/organic acids if indicated;
- TORCH and syphilis studies guided by maternal and neonatal history;
- renal/liver tests and broader metabolic studies when systemic signs are present. [345][346]

### Differential diagnosis

| Differential | Distinguishing clues |
|---|---|
| Other isolated hereditary cataracts | Similar morphology; distinguished by multigene testing, e.g., `CRYAB`, `CRYBA1`, `CRYBB1`, `CRYBB2`, `CRYGC`, `CRYGD`, `GJA3`, `GJA8`, `MIP`, `HSF4` |
| Congenital infection | Maternal infection, deafness, cardiac disease, microcephaly, retinitis, positive serology/PCR |
| Galactosemia/galactokinase deficiency | Failure to thrive, jaundice/sepsis or oil-droplet cataract, abnormal galactose testing |
| Persistent fetal vasculature | Usually unilateral, microphthalmic eye, retrolental stalk |
| Primary congenital glaucoma | Enlarged rather than small cornea, corneal edema, Haab striae, high IOP |
| Retinoblastoma | Leukocoria with retinal mass on imaging/fundus examination |
| Anterior-segment dysgenesis | Peters anomaly, sclerocornea, adhesions, multiple developmental findings |
| Syndromic cataract | Neurologic, renal, skeletal, dermatologic, endocrine, or dysmorphic abnormalities |

### Screening

AAP/AAO/AAPOS recommendations support inspection and red-reflex testing in newborns, with immediate referral for an abnormal reflex. [364][368]

Once a familial variant is known, cascade testing and targeted slit-lamp examination of apparently unaffected relatives are appropriate.

---

## 11. Outcome and prognosis

### Survival and mortality

CTRCT9 is not known to reduce life expectancy or cause disease-specific mortality. Five- or ten-year survival statistics are therefore not applicable.

### Visual prognosis

Visual outcome depends mainly on:

- cataract density and centrality;
- unilateral versus bilateral disease;
- age at onset;
- age at surgery;
- duration of visual deprivation;
- microphthalmia/microcornea or other structural abnormalities;
- adherence to optical correction and amblyopia treatment;
- development of glaucoma or visual-axis opacification.

Surgery can restore a clear optical pathway, but visual recovery may remain limited by irreversible deprivation amblyopia.

### Complications

- Amblyopia
- Nystagmus and strabismus
- High refractive error/anisometropia
- Visual-axis opacification
- Aphakia/pseudophakia-related complications
- Retinal detachment, less commonly
- Lifelong glaucoma risk after pediatric cataract surgery

In the Infant Aphakia Treatment Study, the ten-year cumulative probability was **22% for glaucoma** and **40% for glaucoma or glaucoma suspect**; risk did not significantly differ between primary IOL and contact-lens groups. [151][153]

At age 10.5 years, approximately 25% of treated unilateral cases had 20/40 or better vision, whereas 44% had 20/200 or worse, illustrating the major impact of deprivation amblyopia despite technically successful treatment. These data are not CRYAA-specific. [153]

---

## 12. Treatment

### Current standard of care

No medication, dietary treatment, gene therapy, or RNA therapy is approved to correct a pathogenic `CRYAA` allele or reliably clear its cataract. Treatment is phenotype-driven.

| Intervention | Indication and implementation | Important outcomes/risks | Suggested NCIT intervention concept |
|---|---|---|---|
| Observation | Small peripheral or non-progressive opacity not impairing the visual axis | Frequent monitoring because progression can occur | Observation |
| Cataract extraction/lensectomy | Visually significant central opacity, typically >3 mm, absent red reflex, poor fixation, strabismus or nystagmus | Restores optical pathway; risks inflammation, glaucoma, visual-axis opacity | Cataract Surgery |
| Posterior capsulotomy/anterior vitrectomy | Common in infants/young children to maintain a clear axis | Reduces secondary visual-axis opacification | Posterior Capsulotomy; Anterior Vitrectomy |
| Contact lens | Optical correction of aphakia, especially infants | Effective but adherence, loss, infection, and parental burden are relevant | Contact Lens Therapy |
| Intraocular lens | Selected children; age, anatomy and surgeon judgment determine primary vs secondary implantation | More early additional procedures in infants; does not eliminate glaucoma risk | Intraocular Lens Implantation |
| Spectacles | Aphakic/pseudophakic correction, bifocal/near add | Essential for visual rehabilitation | Corrective Lens Therapy |
| Occlusion/patching | Treats unilateral or asymmetric amblyopia | Adherence is a major determinant of outcome | Occlusion Therapy |
| Glaucoma treatment | Elevated IOP or glaucomatous damage | May require topical drugs, angle surgery, drainage device or cyclodestruction | Glaucoma Therapy |
| Low-vision/educational support | Persistent visual disability | Improves school access and independence | Low Vision Rehabilitation |

The completed **Infant Aphakia Treatment Study, NCT00212134**, randomized 114 infants with unilateral congenital cataract to primary IOL or contact-lens correction and applied the same patching protocol to both groups. [376][377]

### Timing algorithm

- **Dense unilateral congenital cataract:** generally operate at 4–6 weeks.
- **Dense bilateral congenital cataract:** generally operate by 6–8 weeks, sometimes sequentially about one week apart.
- **Partial opacity:** document visual behavior and progression; operate if visually significant.
- **Older child/adult progressive cataract:** conventional cataract-surgery indications based on function and examination.

### Pharmacotherapy and pharmacogenomics

No CRYAA-specific pharmacogenomic recommendation exists. Postoperative topical corticosteroids, antibiotics, cycloplegics, and glaucoma medications are used according to standard pediatric ophthalmic practice, not genotype.

### Experimental targeted therapy

A 2015 screen identified an oxysterol pharmacological chaperone, “compound 29”/VP1-001, that bound α-crystallins, reduced aggregation, and improved transparency in R49C-CRYAA and R120G-CRYAB mouse models:

> “The most promising compound improved lens transparency in the R49C cryAA and R120G cryAB mouse models of hereditary cataract.”  
> Makley et al., *Science*, November 6, 2015; PMID **26542570**. [386]

A later mouse study reported improvement in refractive-index profiles in 61% of treated lenses and at least one-grade apparent opacity improvement in 46%. [404] However, independent studies failed to show that lanosterol or 25-hydroxycholesterol dissolved cataracts, so these compounds remain preclinical and controversial. [414]

No registered human trial has established a CRYAA pharmacological chaperone, gene replacement, CRISPR editing, ASO, siRNA, or lens-cell therapy as effective treatment.

### Current clinical trials

Trials in congenital/pediatric cataract focus on surgical devices or technique rather than correction of CRYAA:

- **NCT06294795:** toric versus non-toric IOLs in children aged 6–17 with cataract and astigmatism. [375]
- **NCT05461040:** IOL optic capture without anterior vitrectomy versus in-the-bag implantation with vitrectomy. [383]
- **NCT04323982:** traditional bilateral surgery versus surgery using triamcinolone staining of anterior vitreous. [379]
- **NCT05278936:** a congenital/pediatric cataract surgical-technique study. [378]

These studies are not genotype-specific.

---

## 13. Prevention

### Primary prevention

A pathogenic germline CRYAA allele cannot currently be prevented by lifestyle modification. Relevant options are reproductive rather than medical prevention:

- preconception genetic counseling;
- targeted carrier testing for recessive families;
- prenatal diagnosis after chorionic-villus sampling or amniocentesis;
- preimplantation genetic testing for a known familial pathogenic variant;
- donor gametes or other family-planning options.

Rubella vaccination, avoidance of teratogens, and prenatal infection prevention reduce non-genetic congenital cataracts but do not alter inherited CRYAA risk. [370]

### Secondary prevention

- Red-reflex screening from birth.
- Early ophthalmology referral for leukocoria or abnormal reflex.
- Cascade genetic testing and slit-lamp examination in relatives.
- Close monitoring of mild opacities during the visual critical period.
- Prompt surgery before prolonged deprivation.

### Tertiary prevention

- Immediate postoperative optical correction.
- Rigorous amblyopia therapy.
- Lifelong intraocular-pressure and optic-nerve monitoring.
- Surveillance for visual-axis opacification, refractive shift, retinal complications, and treatment adherence.
- Educational and low-vision support.

No vaccine or preventive medication applies specifically to CTRCT9.

---

## 14. Other species and natural disease

Generic cataract occurs naturally in many mammals and birds, but a naturally occurring veterinary cataract definitively homologous to human CRYAA-CTRCT9 has not been firmly established. OMIA lists cataract in dogs, cats, cattle, horses, sheep, rabbits, primates, penguins, bears, pandas, and other species, usually without implicating `CRYAA`. [255][256]

| Species | Taxon | Ortholog/resource | Evidence relevant to CRYAA |
|---|---:|---|---|
| Human | 9606 | `CRYAA`, NCBI Gene 1409 | Natural CTRCT9 |
| House mouse | 10090 | `Cryaa`, NCBI Gene **12954**, MGI:88515 | Knockout, R49C knock-in, R116C transgenic and Y118D models |
| Rat | 10116 | `Cryaa`, NCBI Gene **24273**; NM_012534.4 | Lens-stress and expression models |
| Zebrafish | 7955 | `cryaa`, NCBI Gene **100000769**, ZFIN:ZDB-GENE-020508-1 | CRISPR/null developmental and aging studies |
| Vervet/grivet monkey | 60711/9534 depending taxonomy concept | CRYAA screened | Recessive congenital cataract colony studied, but reported candidate missense findings implicated `GCNT2`, not a proven CRYAA lesion |

There is no zoonotic potential and no horizontal transmission.

---

## 15. Model organisms and experimental systems

### Mouse models

| Model | Phenotype recapitulation | Principal use and limitation |
|---|---|---|
| `Cryaa` knockout | Small lenses; progressive nuclear opacity becoming widespread; cytoplasmic inclusions containing αB-crystallin | Demonstrates requirement for αA-crystallin but models complete loss better than most dominant human missense disease |
| R49C heterozygous/homozygous knock-in | Cataract by early postnatal life; severe congenital cataract and small eye in homozygotes; insoluble crystallins and apoptosis | Strong allele-specific model; homozygous severity exceeds usual human AD disease |
| R49C-neomycin model | Cortical vacuoles by 3 weeks and posterior/nuclear cataracts by 3 months | Useful for membrane architecture; neomycin cassette may influence expression |
| R116C transgenic | Posterior cortical opacity and posterior-suture abnormalities; low expression sufficient | Supports dominant toxicity; transgene dosage/site differ from endogenous human heterozygosity |
| Y118D knock-in | Opaque nuclear cataract, posterior rupture, fiber disorganization and UPR activation | Strong ER-stress model, but Y118D is not a canonical recurrent human CTRCT9 variant |

Targeted `Cryaa` disruption was reported to “induce cataract and cytoplasmic inclusion bodies containing the small heat shock protein alpha B-crystallin,” PMID **9023351**. [454] MGI summarizes that null homozygotes have small lenses with progressive nuclear opacity. [266]

### Zebrafish

CRISPR `cryaa` mutants can show embryonic lens abnormalities by approximately 72 hours post-fertilization, supporting a conserved developmental role. However, adult `cryaa` loss did not reproduce the increased age-related cataract seen in mice; `cryaba` loss had the stronger aging phenotype. This species difference limits direct extrapolation of adult proteostasis. [260][261]

### Cellular and in-vitro models

- HLE-B3 human lens epithelial cells expressing R49C, R116C, G98R, or other variants.
- HEK293T/HeLa aggregation and aggresome assays.
- Recombinant αA-crystallin oligomerization, thermal stability, subunit exchange, membrane binding, and chaperone assays.
- iPSC-derived lentoid bodies, potentially useful for patient-specific lens differentiation and drug screening, although no validated CRYAA patient-derived organoid therapy exists. [243]

### Advanced technologies

- Bulk RNA-seq and proteomics have identified UPR, histone, membrane, and metabolic changes in mutant mouse lenses.
- GC-MS metabolomics has shown increased lactate and reduced sugars/minor sterols in R49C lenses.
- Lens single-cell RNA sequencing now resolves multiple epithelial differentiation states and lens-fiber populations, but a disease-specific single-cell atlas of human CRYAA cataract was not identified. [240][321]
- No mature spatial-transcriptomic or CRISPR-screen dataset currently defines a validated therapeutic target specifically for CTRCT9.

---

## Evidence assessment and knowledge-base conclusions

1. **Causality is strong:** multiple segregating human variants, dominant and recessive pedigrees, biochemical dysfunction, and allele-specific animal models establish `CRYAA` as the causal gene.
2. **Phenotypic heterogeneity is genuine:** morphology and onset cannot be predicted reliably from the disease label alone; even carriers of the same allele may range from subclinical opacity to total cataract.
3. **Core mechanism:** mutant or deficient αA-crystallin disrupts lens proteostasis and architecture through impaired holdase function, abnormal oligomerization, aggregation, and—in some alleles—UPR-mediated apoptosis.
4. **Clinical urgency is developmental:** mortality is not affected, but delayed clearance of a visually significant infantile cataract can produce irreversible amblyopia.
5. **Current treatment remains surgical plus visual rehabilitation:** pharmacological chaperones are promising model-system findings but not approved therapy.
6. **Major data gaps:** CRYAA-specific prevalence, quantitative penetrance, validated modifier genes, longitudinal natural history by genotype, human molecular biomarkers, disease-specific single-cell data, and genotype-directed therapy are unavailable.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 29 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 15 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 13 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011413` (2 mentions) - the report calls it "MONDO"; MONDO calls it **cataract 9 multiple types**
- `DOID:0110266` (2 mentions) - the report calls it "Disease Ontology"; DOID calls it **cataract 9 multiple types**
- `HP:0000482` (1 mention) - the report calls it "Variant-dependent; 50/186 patients in the 2024 literature review"; HP calls it **Microcornea**
- `HP:0000568` (1 mention) - the report calls it "17/186 in the 2024 review; 5/13 in the original p.Arg116Cys family"; HP calls it **Microphthalmia**
- `HP:0000612` (1 mention) - the report calls it "Occasional, especially p.Arg116Cys"; HP calls it **Iris coloboma**
- `HP:0000501` (1 mention) - the report calls it "Occasional with p.Arg12Cys; major lifelong post-surgical risk"; HP calls it **Glaucoma**
- `HP:0000639` (1 mention) - the report calls it "Secondary, especially with dense bilateral disease"; HP calls it **Nystagmus**
- `HP:0000545` (1 mention) - the report calls it "Uncommon/variant-specific"; HP calls it **Myopia**
- `HP:0000256` (1 mention) - the report calls it "Rare and not clearly a consistent CRYAA manifestation"; HP calls it **Macrocephaly**
- `UBERON:0000390` (1 mention) - the report calls it "Embryonal/fetal/nuclear cataract site"; UBERON calls it **lens nucleus**
- `UBERON:0002444` (1 mention) - the report calls it "Principal protein-dense tissue"; UBERON calls it **lens fiber**
- `UBERON:0001803` (1 mention) - the report calls it "Anterior monolayer; source of new fibers"; UBERON calls it **epithelium of lens**
- `UBERON:0005614` (1 mention) - the report calls it "Proliferative/differentiating region"; UBERON calls it **lens anterior epithelium**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.