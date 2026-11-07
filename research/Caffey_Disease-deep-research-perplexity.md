---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T13:09:40.606648'
end_time: '2026-11-06T13:15:20.436878'
duration_seconds: 339.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Caffey Disease
  mondo_id: MONDO:0007244
  category: Mendelian
  causal_genes: COL1A1
  omim_id: OMIM:114000
  synonyms: infantile cortical hyperostosis
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.5.1
term_validation:
  total_terms: 62
  verified: 59
  not_found: 1
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.016
  labels_checked: 47
  labels_matching: 26
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0004423
    reported_labels:
    - Cortical hyperostosis
    ontology_label: Cranium bifidum occultum
  - term_id: HP:0030892
    reported_labels:
    - Diaphyseal thickening
    ontology_label: Deep cerebral white matter hyperintensities
  - term_id: HP:0005309
    reported_labels:
    - Periosteal reaction
    ontology_label: obsolete Peripheral vascular insufficiency
  - term_id: HP:0002816
    reported_labels:
    - Long bone bowing
    ontology_label: Genu recurvatum
  - term_id: GO:0035195
    reported_labels:
    - response to prostaglandin E
    ontology_label: miRNA-mediated post-transcriptional gene silencing
  - term_id: UBERON:0002223
    reported_labels:
    - rib
    ontology_label: endolymphatic sac
  - term_id: UBERON:0002372
    reported_labels:
    - scapula
    ontology_label: tonsil
  - term_id: UBERON:0001423
    reported_labels:
    - ulna
    ontology_label: radius bone
  - term_id: UBERON:0001421
    reported_labels:
    - radius
    ontology_label: pectoral girdle region
  - term_id: UBERON:0002485
    reported_labels:
    - cortical bone
    ontology_label: prostate duct
  labels_variant: 11
  unresolved_terms:
  - HP:0003389
  obsolete_terms:
  - term_id: HP:0005309
    ontology_label: obsolete Peripheral vascular insufficiency
    replaced_by: HP:0004950
  - term_id: GO:0062023
    ontology_label: obsolete collagen-containing extracellular matrix
    replaced_by: GO:0031012
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Caffey Disease
- **MONDO ID:** MONDO:0007244 (if available)
- **Causal gene(s):** COL1A1
- **OMIM:** OMIM:114000
- **Synonyms:** infantile cortical hyperostosis
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Caffey Disease** covering all of the
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

# Caffey Disease (Infantile Cortical Hyperostosis): Comprehensive Disease Characterization

Caffey disease, also known as *infantile cortical hyperostosis*, is a rare Mendelian disorder in which heterozygous pathogenic variants in the **COL1A1** gene, encoding the alpha-1 chain of type I collagen, lead to episodic, self-limited but often dramatic subperiosteal new bone formation in early infancy, accompanied by soft-tissue swelling, pain, irritability, and systemic inflammation.[1][8][9] The disorder is classically inherited in an autosomal dominant fashion with incomplete penetrance and variable expressivity, and in most familial and many sporadic cases it is caused by a recurrent missense variant c.3040C>T in exon 41 of COL1A1, resulting in substitution of arginine by cysteine at position 836 in the helical domain of the α1(I) chain (p.Arg836Cys, also reported as p.Arg1014Cys), which has been repeatedly confirmed as a pathogenic hotspot in Caffey disease.[9][12][15][16] Clinically, affected infants develop painful swelling and thickening of the diaphyses of long bones, mandible, clavicles, and ribs within the first 5–6 months of life, often with fever and elevated acute-phase reactants, followed by spontaneous resolution of signs by approximately 1–2 years, although recurrences and later-life sequelae such as joint hyperlaxity, hyperextensible skin, hernias, short stature, and increased fracture risk have been documented.[1][5][8][9] Radiographically, there is lamellated periosteal reaction and pronounced cortical hyperostosis of long bone shafts and jaw, typically sparing metaphyses and epiphyses, and histopathology shows periosteal new bone formation and soft-tissue inflammation, which may closely mimic osteomyelitis and other conditions, making misdiagnosis a significant concern in clinical practice.[7][9][10][19] Molecular and pathogenetic studies suggest that the R836C COL1A1 variant subtly alters collagen fibrillogenesis and matrix organization, which in turn may predispose periosteum and contiguous soft tissues to injury and trigger a self-amplifying local inflammatory cascade involving cyclooxygenase-2 (COX-2) and prostaglandin E (PGE) signaling, leading to exuberant subperiosteal bone formation; this hypothesis is supported by the occurrence of similar cortical hyperostosis in infants exposed to PGE therapy and by symptomatic improvement with COX inhibition in some cases.[9][14] While the infantile form is usually benign and self-limited, severe prenatal cortical hyperostosis—sometimes called prenatal Caffey disease—can be lethal, and recent data indicate genetic heterogeneity, with some lethal prenatal cases associated with IFITM5 variants rather than COL1A1 mutations, underscoring a complex and evolving nosology of cortical hyperostosis syndromes.[11][13][16][17][18] Because of its distinctive early-life presentation, monogenic etiology, and intersection with broader collagen-related disorders such as osteogenesis imperfecta and Ehlers–Danlos syndrome, Caffey disease provides a unique window into the biology of periosteal bone formation, collagen matrix function, and inflammatory-osteogenic coupling in human skeletal development.[9][12][14]  

## 1. Disease Information

### 1.1 Definition and clinical overview

Caffey disease, formally designated *infantile cortical hyperostosis*, is a rare skeletal disorder characterized by acute onset of soft-tissue swelling and massive subperiosteal new bone formation in infants, involving predominantly the diaphyses of long bones, the mandible, clavicles, ribs, and sometimes other skeletal elements.[1][8][9] The typical clinical triad comprises irritability, fever, and firm, often tender swellings over affected bones, with radiographs showing cortical thickening and periosteal reaction, and laboratory tests frequently demonstrating elevated alkaline phosphatase and inflammatory markers such as leukocytosis and increased erythrocyte sedimentation rate.[1][5][8][10] Onset usually occurs between birth and 5 months of age and the disease is notable for its self-limited course, with spontaneous regression of bone lesions and clinical symptoms by approximately 1–2 years in the classic infantile form, although residual deformities or subsequent fracture susceptibility may persist in some individuals.[1][5][8][9] The condition was first systematically described by Caffey and Silverman in 1945 as a distinct syndrome of infantile cortical hyperostosis and has since been recognized as a Mendelian disorder with a clear molecular basis in type I collagen abnormalities.[10][18] From an ontological perspective, Caffey disease corresponds to a rare monogenic skeletal dysplasia in the Human Phenotype Ontology (HPO) and is represented in disease ontologies such as MONDO as MONDO:0007244, linking it to the broader class of collagen-related bone disorders.

The core nosologic identity of Caffey disease rests on its combination of early-onset periosteal hyperostosis, systemic inflammatory features, and a characteristic radiologic pattern, together with its autosomal dominant inheritance due to COL1A1 variants.[1][8][9][12] GeneReviews emphasizes that the diagnosis is primarily clinical and radiographic, with molecular confirmation by detection of a heterozygous COL1A1 pathogenic variant, usually c.3040C>T, while also noting that recurrence of bone hyperostosis and inflammatory episodes can occur later in childhood or adulthood in a minority of cases.[3][5][8] MedlinePlus Genetics similarly defines Caffey disease as a bone disorder that most often occurs in babies and notes that excessive cortical bone formation mainly affects the jawbone, shoulder blades, collarbones, and long bone shafts.[13] These authoritative resources aggregate data from multiple case series, family studies, and molecular analyses, rather than from individual electronic health records, thereby providing an integrated disease-level description that informs current clinical understanding.

### 1.2 Nosologic identifiers and classification

Caffey disease is indexed in Online Mendelian Inheritance in Man (OMIM) under entry **114000**, designated as an autosomal dominant disorder with a known molecular basis in the COL1A1 gene at chromosome 17q21.33.[1][8] MedGen, which aggregates phenotype and gene links from multiple databases, lists infantile cortical hyperostosis under Concept ID C0020497 and explicitly links it to COL1A1 as the associated gene, referencing the OMIM entry and GeneReviews chapter.[8] The condition is also catalogued in the NIH Genetic Testing Registry (GTR) under the name “Infantile cortical hyperostosis,” highlighting its autosomal dominant inheritance and referencing the same GeneReviews summary.[4] While the Orphanet identifier is not explicitly given in the provided materials, Caffey disease is recognized by Orphanet as a rare skeletal dysplasia, and MedGen records note that Orphanet considers it a hereditary clinical entity and provides autosomal dominant as one of the modes of inheritance.[4] In universal disease ontologies, Caffey disease is mapped to **MONDO:0007244**, situating it within the broader hierarchy of “type I collagenopathies” and “rare bone diseases.”

Classifications in broader clinical coding systems, such as ICD-10 or ICD-11, typically map Caffey disease under categories related to “other specified disorders of bone development and growth,” but specific codes may vary and are not directly provided in the cited resources.[8] MeSH terms encompass the disorder under “Hyperostosis, Cortical, Infantile” and related headings, consolidating literature indexing in PubMed and other NLM resources. Overall, these identifiers facilitate consistent recognition of Caffey disease across genomic, clinical, and ontological databases, ensuring that data on this rare condition can be integrated and compared across studies and registries.

### 1.3 Synonyms and alternative names

The disease is known by several synonymous names that reflect its core pathologic and demographic characteristics. **Infantile cortical hyperostosis** is the most widely used descriptive term, emphasizing the age of onset and the cortical bone thickening that defines the condition.[8][9][10] Other synonyms include “hyperostosis, cortical, congenital,” “congenital cortical hyperostosis,” and occasionally “Caffey–Silverman disease,” acknowledging the clinicians who first characterized it.[8][10][13] Consumer-facing resources such as MedlinePlus refer to “Caffey disease” and explicitly note “also called infantile cortical hyperostosis,” ensuring that patients and families can recognize that these terms describe the same condition.[13]

MedGen and GTR list “P1PK blood group system, P(2) phenotype” among synonyms in the broader context of COL1A1-related phenotypes, but in the present context the primary focus remains on the skeletal manifestations.[4][8] It is important to distinguish classic Caffey disease from “lethal prenatal cortical hyperostosis” or “lethal prenatal Caffey disease,” which some authors consider a separate or only partially overlapping entity because of its earlier onset, diffuse non-inflammatory hyperostosis, and often fatal outcome.[11][13][17][18] Ontologically, one might treat “infantile cortical hyperostosis” and “Caffey disease” as exact synonyms, while considering “lethal prenatal cortical hyperostosis” a closely related but not identical entity.

### 1.4 Data sources and evidence base

The characterization of Caffey disease in current literature derives from a combination of family-based linkage and sequencing studies, case reports and case series, radiologic and pathologic descriptions, and synthesis in expert-authored reviews and GeneReviews chapters.[3][5][8][9][12][14] The seminal molecular study by Gensure et al. in 2005 in the *Journal of Clinical Investigation* used genome-wide linkage analysis in a large Australian kindred with autosomal dominant infantile cortical hyperostosis, identifying a locus on chromosome 17q21 and ultimately a recurrent missense mutation in COL1A1.[12][14] Subsequent reports from diverse ethnic populations, including Korean, Thai, Indian, and Australian families, have confirmed the same COL1A1 c.3040C>T variant as a recurrent cause of familial and sporadic Caffey disease.[9][13][15][16] These primary studies provide the core genetic evidence base.

GeneReviews provides an updated, peer-reviewed synthesis of clinical, diagnostic, management, and genetic counseling information; the Caffey Disease chapter was initially posted in 2012 and most recently updated in May 2024, integrating new data on molecular genetics, prenatal presentations, and adult sequelae.[2][3][5] MedlinePlus Genetics offers a lay-accessible summary, drawing on GeneReviews and primary literature, while MedGen, OMIM, and the Genetic Testing Registry collate gene–disease associations and testing information.[1][4][8][13] Radiology-focused resources such as Radiopaedia present illustrative cases that highlight diagnostic imaging features and common pitfalls.[7] Together, these data sources reflect aggregated disease-level knowledge rather than isolated electronic health record-derived observations, although case reports inevitably originate from individual patient encounters.

## 2. Etiology

### 2.1 Primary genetic cause: COL1A1 mutations

The primary etiologic factor in classic Caffey disease is a heterozygous missense mutation in **COL1A1**, the gene encoding the α1(I) chain of type I collagen, which is the predominant collagen in bone, skin, and other connective tissues.[1][9][12][13] Gensure et al. reported that affected individuals from a large multi-generational family with autosomal dominant infantile cortical hyperostosis, as well as obligate carriers, shared a heterozygous c.3040C>T transition in exon 41 of COL1A1.[12][14] This nucleotide change results in substitution of arginine by cysteine at amino acid position 836 in the triple-helical domain of the protein (p.Arg836Cys), a region that participates in the characteristic Gly–X–Y repeating sequence of collagen molecules.[9][12][13] The same mutation was subsequently identified in members of two other unrelated families with autosomal dominant Caffey disease and has since been reported as a recurrent “hotspot” pathogenic variant in numerous families and sporadic cases across diverse ethnic backgrounds, including Korean, Thai, Indian, and Australian cohorts.[9][13][15][16]

ClinVar summarizes the COL1A1 c.3040C>T (p.Arg1014Cys) variant, also referred to as p.Arg836Cys due to different numbering conventions, as pathogenic for autosomal dominant Caffey disease with incomplete penetrance, noting that it has been observed to segregate with disease in multiple families.[15] Medscape’s recent review emphasizes that this specific variant is the obligate cause of the familial form of infantile cortical hyperostosis and has been confirmed as a recurrent mutation across diverse ethnic groups, reinforcing its etiologic centrality.[16] MedlinePlus Genetics explicitly states that Caffey disease is caused by a mutation in the COL1A1 gene, replacing arginine with cysteine at position 836 (Arg836Cys), and notes that this leads to type I collagen fibrils that are variable in size and shape.[13] Taken together, these sources provide convergent evidence that COL1A1 c.3040C>T is the principal causal variant in classic Caffey disease.

### 2.2 Genetic risk factors and modifier effects

Beyond the primary pathogenic variant, variability in disease expression and penetrance suggests the existence of genetic modifiers. Gensure et al. noted that among individuals heterozygous for the COL1A1 R836C mutation, only 79% had experienced an episode of cortical hyperostosis, while approximately 21% remained clinically unaffected, indicating reduced penetrance and implying that additional genetic or environmental factors modulate phenotypic expression.[12][14] Moreover, individuals with the mutation but no infantile episodes still displayed adult connective tissue features such as joint hyperlaxity, hyperextensible skin, and inguinal hernias, suggesting a broader subclinical phenotype influenced by other genetic background.[9][12][14] Although specific modifier genes have not been conclusively identified in Caffey disease, the overlap of adult features with Ehlers–Danlos syndrome hypermobility type suggests that variants in other extracellular matrix or connective tissue genes might modulate severity, a hypothesis consistent with broader collagenopathy literature.[9][14]

ClinVar indicates that the COL1A1 c.3040C>T variant is rare in the general population but present in some individuals without known disease, again supporting incomplete penetrance and potential genetic modifiers.[15] However, no genome-wide association studies or systematic modifier analyses have yet been reported specifically for Caffey disease, and thus the identity of such modifiers remains speculative. From a risk perspective, the presence of the COL1A1 R836C variant in a family clearly confers a 50% chance of transmission to offspring, but the probability of developing infantile episodes of cortical hyperostosis is less than 100%, likely in the 70–80% range based on familial data.[5][12][14] This distinction between variant carriage and clinical disease risk is central to genetic counseling.

### 2.3 Environmental and treatment-related risk factors

Although Caffey disease is primarily a genetic disorder, environmental or iatrogenic factors can provoke similar cortical hyperostosis, and these may interact with underlying genetic susceptibility. A notable example is the induction of cortical hyperostosis in infants receiving prostaglandin E (PGE) therapy for ductus-dependent cyanotic heart disease. Ueda et al. reported that prolonged PGE infusion in infants led to cortical hyperostosis resembling infantile cortical hyperostosis, and Heyman et al. subsequently noted elevated PGE serum levels in affected children, with rapid symptom improvement upon treatment with indomethacin, a COX inhibitor that suppresses PGE synthesis.[14] The 2014 mechanistic review on Caffey disease highlights these findings, suggesting that abnormal COX-2/PGE signaling can drive periosteal new bone formation and that PGE therapy provides a “pharmacologic model” of Caffey-like hyperostosis.[9][14]

Whether PGE-induced hyperostosis represents the same disease entity as genetically determined Caffey disease or a phenocopy remains debated. The mechanistic review notes that incidence of non-familial cases attributed to PGE therapy complicates the picture and “indicates that there could be several distinct subtypes of the disease.”[9] It is possible that PGE exposure unmasking a latent susceptibility in carriers of subtle collagen variants could produce a clinical phenotype overlapping with classic Caffey disease, though robust genetic data in PGE-associated cases are limited. Nonetheless, from an etiologic standpoint, high-dose or prolonged PGE therapy in infancy constitutes a clear environmental risk factor for cortical hyperostosis and informs both mechanistic hypotheses and clinical management.

Other environmental risk factors for Caffey disease per se have not been convincingly demonstrated. Early hypotheses invoked viral infections, immune dysregulation, or metabolic abnormalities, but these have not been substantiated in modern molecular studies.[9][10] Case reports often explicitly note absence of trauma, infection, or other systemic illness in affected infants.[10][19] However, because the disease involves inflammatory soft-tissue and bone responses, generic inflammatory triggers or mechanical stress might conceivably modulate severity in carriers of the COL1A1 mutation, although this remains speculative.

### 2.4 Protective factors and absence of known environmental protection

Specific protective genetic variants against Caffey disease have not been described in the literature. The incomplete penetrance of the COL1A1 R836C variant implies that some individuals harboring this mutation never develop infantile cortical hyperostosis, but the underlying reasons—whether due to compensatory genetic variants, differences in immune or inflammatory responses, or stochastic factors—are unknown.[12][14][15] No studies have systematically compared the genomes or transcriptomes of symptomatic versus asymptomatic carriers to identify protective alleles, and thus protective genetic factors remain an unmet research question.

Analogously, there are no recognized environmental or lifestyle factors that prevent Caffey disease in individuals carrying the pathogenic COL1A1 variant. The disease typically manifests in early infancy, before lifestyle factors such as diet or exercise could plausibly exert major influence, and it resolves spontaneously in most cases.[1][5][8][10] At the mechanistic level, avoidance of exogenous PGE therapy in carriers could theoretically reduce risk of exacerbating hyperostosis, but PGE infusion is a life-saving intervention in critically ill infants with ductus-dependent cardiac lesions and is not administered casually; thus this consideration is more about avoiding diagnostic confusion than primary prevention.[9][14] Overall, current evidence does not support specific protective measures beyond standard avoidance of unnecessary medications or exposures in neonates.

### 2.5 Gene–environment interactions

The interplay between genetic and environmental factors in Caffey disease is inferred primarily from the convergence of COL1A1 mutations and PGE-related observations. The mechanistic review argues that periosteal detachment and injury might elicit an inflammatory response that triggers a local positive feedback loop involving COX-2/PGE signaling, thereby driving new bone formation by periosteal osteoblasts.[9] In this model, the COL1A1 R836C mutation alters the collagen matrix environment, making the periosteum more susceptible to microinjury or abnormal inflammatory signaling, while environmental factors such as PGE exposure or mechanical stress provide the inflammatory stimulus. The review states that “abnormal COX2/PGE signaling is likely to play role in periosteal new bone formation in Caffey disease,” linking the genetic defect to a specific environmental-responsive pathway.[9]

The PGE therapy cases support this gene–environment interaction model. In infants without known COL1A1 mutations, prolonged exogenous PGE administration can produce a hyperostosis phenotype that responds to COX inhibition, suggesting that high PGE levels can by themselves drive periosteal new bone formation; in mutation carriers, the threshold for such a response may be lower, or the response more pronounced.[9][14] Although direct evidence for enhanced PGE sensitivity in COL1A1 R836C carriers is lacking, this hypothesis is consistent with the observed variably penetrant and episodic nature of the disease. It illustrates how a specific genetic lesion in the extracellular matrix can interact with inflammatory mediators to produce a highly localized but dramatic skeletal phenotype.

## 3. Phenotypes

### 3.1 Core clinical manifestations in infancy

The prototypical phenotype of Caffey disease is that of a previously healthy infant who develops sudden irritability, refusal to move affected limbs (pseudoparalysis), and visible or palpable swellings over certain bones, usually within the first five months of life.[1][5][8][10] GeneReviews summarizes that Caffey disease is characterized by massive subperiosteal new bone formation, usually involving the diaphyses of long bones as well as ribs, mandible, scapulae, and clavicles, and that these lesions are typically associated with fever, soft-tissue swelling, and pain.[5][8] MedGen notes that painful swelling and systemic fever often accompany the episode, which usually begins before the age of 5 months and resolves before age 2 years.[1][8] Clinical case reports describe infants presenting with mild to moderate fever, intermittent irritability, crying, and localized swelling, without signs of infection such as rash, diarrhea, or organomegaly.[10][19]

In an illustrative case series, a 4-month-old female infant presented with low-grade fever, intermittent irritability, and swelling over the left mandible, left forearm, and supraclavicular area with prominent veins; there was mild redness but no joint swelling or organomegaly, and radiographs showed thickened irregular long bones.[10] Another infant presented at 2.5 months with intermittent fever and irritability, isolated swelling of both mandibular areas, and radiographic mandibular thickening.[10] These cases exemplify the variable yet characteristic pattern: infants are often otherwise well, with localized painful swellings, mild fever, and elevated inflammatory markers, but no systemic infection. The clinical picture can be dramatic enough to raise concern for osteomyelitis, scurvy, or child abuse.[7][10][19]

From an HPO perspective, core phenotypes include subperiosteal new bone formation (HPO term: *Subperiosteal new bone formation*), cortical hyperostosis of long bones and mandible, bone pain (HP:0002653), soft-tissue swelling (HP:0003389), fever (HP:0001945), irritability (HP:0000737), and decreased limb movement or pseudoparalysis (HP:0001384).[8][9][10][19] The impact on quality of life in infancy is significant, as pain and irritability can disrupt feeding, sleep, and normal developmental activities, and caregivers may experience anxiety due to the alarming appearance and differential diagnosis.

### 3.2 Radiographic and skeletal features

Radiographically, Caffey disease has a highly characteristic pattern that is central to diagnosis. OMIM and MedGen describe “massive subperiosteal new bone formation” typically involving the diaphyses of long bones, mandible, and clavicles, with the epiphyses and metaphyses usually spared.[1][8][9] The 2014 review notes that periosteal new bone formation leads to cortical thickening (hyperostosis) of affected bones and swelling of the overlying soft tissue, and that bone lesions are often asymmetric, involving the mandible in 70–90% of cases, the clavicle in about 50%, and ribs and scapulae in 20–30%.[9] In the long bones, primary lesions are localized to the diaphysis, resulting in grossly deformed spindle-shaped bones, and episodes of hyperostosis may also lead to bony bridges between adjacent bones.[9]

Radiopaedia’s case description of infantile cortical hyperostosis demonstrates a lamellated to fusiform periosteal reaction along the shaft of the femur with minimal soft-tissue swelling and subtle periostitis along lower ribs, with the child experiencing chest pain and crying when held; subsequent radiographs showed mandibular periostitis and persistent periosteal reaction, which later resolved by 11 months of age.[7] Another case report describes florid periosteal new bone formation with pronounced cortical thickening involving diaphyses and sparing metaphyses and epiphyses, in line with the classical radiologic description.[10] A case involving skull base sclerosis showed massive sclerosis of skull bones and enlargement of the mandible due to cortical new bone formation, highlighting that cranial bones can also be involved.[19]

These radiologic features correspond to HPO terms such as *Cortical hyperostosis* (HP:0004423), *Diaphyseal thickening* (HP:0030892), *Mandibular hyperostosis*, and *Periosteal reaction* (HP:0005309). The sparing of metaphyses and epiphyses helps distinguish Caffey disease from other infantile bone disorders such as osteomyelitis or hypervitaminosis A.[9][10] Radiographic abnormalities generally evolve through stages, with early periosteal reaction, followed by cortical thickening, and ultimate remodeling and normalization by 1–2 years of age.[19] In severe prenatal cases, fetal radiographs or postnatal imaging can show diffuse cortical hyperostosis of long bones, ribs, and mandible, with marked bony sclerosis and ballooning of diaphyses.[11][18]

### 3.3 Laboratory abnormalities and systemic inflammation

Laboratory findings in Caffey disease reflect a systemic inflammatory state but are nonspecific. OMIM and MedGen note that laboratory findings typically include elevated alkaline phosphatase and sometimes elevations in white blood cell count and erythrocyte sedimentation rate, consistent with bone turnover and inflammation.[1][8] Case reports document elevated ESR, total leukocyte count, C-reactive protein, platelet count, immunoglobulin levels, and decreased hemoglobin, suggesting anemia of inflammation.[10] In one series, both infants had raised ESR and alkaline phosphatase, with other investigations directed at ruling out infection, scurvy, or malignancy.[10] Radiopaedia’s case also mentions raised total leukocyte count and ESR with mild fever, initially prompting an osteomyelitis diagnosis.[7]

These laboratory features map to HPO terms such as *Elevated serum alkaline phosphatase* (HP:0003155), *Leukocytosis* (HP:0001974), *Elevated erythrocyte sedimentation rate* (HP:0003565), *Anemia* (HP:0001903), and *Thrombocytosis* (HP:0001873).[1][8][10] From a quality-of-life standpoint, while these laboratory changes are primarily markers rather than symptoms, they reflect systemic inflammation that contributes to fever, malaise, and discomfort. Because these laboratory abnormalities are nonspecific, they are useful mainly in conjunction with imaging and clinical signs, and must be interpreted cautiously to avoid misdiagnosis as infectious osteomyelitis or malignancy.

### 3.4 Adult sequelae and connective tissue manifestations

An important but sometimes underappreciated aspect of Caffey disease is the persistence of connective tissue manifestations into adulthood among individuals who had infantile cortical hyperostosis. Gensure et al. reported that individuals bearing the COL1A1 R836C mutation, whether or not they had experienced an infantile episode of cortical hyperostosis, exhibited joint hyperlaxity, hyperextensible skin, and inguinal hernias resembling a mild form of Ehlers–Danlos syndrome type III.[12][14] The 2014 review notes that adults with a history of Caffey disease may have joint laxity, skin hyperextensibility, hernias, short stature, and increased risk for bone fractures and/or deformities.[5][8][9] GeneReviews similarly highlights these adult features and recommends long-term surveillance for fracture risk and connective tissue complications.[5][8]

These adult phenotypes correspond to HPO terms such as *Joint hypermobility* (HP:0001382), *Skin hyperextensibility* (HP:0000974), *Inguinal hernia* (HP:0000023), *Short stature* (HP:0004322), and *Increased bone fragility* (HP:0002653, overlapping with fracture propensity).[5][8][9][12][14] They reflect the fact that the COL1A1 R836C mutation affects not only bone but also broader connective tissues, and that infantile cortical hyperostosis is one manifestation within a larger collagenopathy spectrum. In terms of quality of life, joint hypermobility and hernias can cause pain, disability, and require surgical interventions, while increased fracture risk necessitates lifestyle adjustments and monitoring, making long-term follow-up relevant even after infantile bone lesions have resolved.

### 3.5 Prenatal and severe phenotypes

In rare cases, Caffey disease or related cortical hyperostosis syndromes manifest prenatally, often with severe outcomes. MedlinePlus Genetics notes that skeletal abnormalities can sometimes be detected by ultrasound in the last weeks of prenatal development, and describes a more severe disorder, lethal prenatal cortical hyperostosis, which appears earlier in development and is often fatal before or shortly after birth.[13] A detailed case report described a fetus in which prenatal ultrasound suggested severe osteogenesis imperfecta due to short long bones, but postmortem radiographs revealed hyperostosis of long bones, ribs, and mandible, with marked diaphyseal sclerosis and ballooning; histology showed the characteristic findings of infantile cortical hyperostosis, and genetic testing identified the same COL1A1 3040C>T mutation in fetal pulmonary tissue.[11] The authors concluded that this heterozygous mutation can also be found in lethal prenatal cortical hyperostosis, expanding the phenotypic spectrum associated with the variant.[11]

Other prenatal cases, including a recently reported survivor of severe prenatal Caffey’s disease, show diffuse, non-inflammatory hyperostosis with angulation of long bones and polyhydramnios, emphasizing that prenatal cortical hyperostosis is a distinct but overlapping entity.[17][18] Medscape notes that a rare, severe, often lethal prenatal form is characterized by extensive hyperostosis and angulated long bones detected on fetal ultrasound as early as 27 weeks gestation, and that some of these cases are not associated with COL1A1 c.3040C>T, suggesting genetic heterogeneity.[16][17][18] A 2024 report identified a de novo IFITM5 variant c.119C>T (p.Ser40Leu) in neonates with prenatal cortical hyperostosis and negative COL1A1 testing, placing prenatal Caffey disease within the broader spectrum of IFITM5-related disorders distinct from classic infantile Caffey disease.[16]

Phenotypes in prenatal cases include severe skeletal deformities, polyhydramnios, fetal hydrops in some cases, and respiratory compromise after birth due to thoracic rigidity, frequently leading to perinatal death.[11][17][18] In survivors, remodeling and clinical improvement have been observed, but long-term outcomes are still emerging.[17][18] These phenotypes link to HPO terms such as *Prenatal onset* (HP:0003623), *Polyhydramnios* (HP:0001561), *Generalized hyperostosis*, and *Long bone bowing* (HP:0002816), and underscore that the Caffey spectrum spans from classic benign infantile disease to lethal prenatal forms, with distinct but partially overlapping etiologies.

### 3.6 Phenotypic variability, severity, and progression

Caffey disease exhibits notable variability in severity, distribution of skeletal lesions, systemic features, and long-term sequelae. The 2014 review emphasizes that the disease is variably penetrant, involving single or multiple bones, with the mandible most frequently affected and sometimes used as a defining criterion.[9] Some infants present with isolated mandibular involvement and minimal systemic symptoms, while others have multiphasic, multifocal disease with significant fever, irritability, and functional impairment.[9][10] Radiographic involvement may be asymmetric or symmetric, and the pattern of bone involvement can differ between individuals and even between episodes in the same patient.[7][9][19] Disease episodes are typically episodic and self-limited, with spontaneous remission of hyperostosis by 1–2 years, but recurrences in adolescence and later life have been documented, particularly in familial cases.[9]

From a progression standpoint, Caffey disease is best described as episodic with spontaneous remission rather than progressive or chronic. Bone lesions appear acutely, evolve over weeks to months, and gradually regress, with remodeling leading to normalization of radiographs in most cases by late infancy or early childhood.[7][10][19] However, in severe cases—especially prenatal forms—hyperostosis can be so extensive that it compromises organ function, leading to perinatal morbidity and mortality.[11][17][18] Quality-of-life impact ranges from transient pain and irritability in mild cases to prolonged hospitalization and life-threatening complications in severe prenatal cases. This variability underscores the importance of individualized assessment and careful phenotypic documentation, including use of standardized HPO terms, to support genotype–phenotype correlations and natural history studies.

## 4. Genetic and Molecular Information

### 4.1 COL1A1 gene overview and functional context

The **COL1A1** gene encodes the pro-α1(I) chain of type I collagen, a major structural component of bone, skin, tendon, and other connective tissues.[9][12][13] Type I collagen is a heterotrimer composed of two α1(I) chains and one α2(I) chain, encoded by COL1A1 and COL1A2, respectively, and assembles into fibrils that provide tensile strength and structural scaffolding in the extracellular matrix.[9][12] The COL1A1 locus resides on chromosome 17q21.33, and mutations in this gene are known to cause a spectrum of disorders, including various forms of osteogenesis imperfecta (OI types I–IV), some types of Ehlers–Danlos syndrome, and now Caffey disease.[1][9][12][14] The Caffey-associated variant resides in the triple-helical domain characterized by repeating Gly–X–Y sequences essential for proper helix formation and fibril assembly.[9][12][13]

In the context of skeletal development, type I collagen fibrils provide the structural framework upon which hydroxyapatite crystals are deposited, and they also influence the behavior of osteoblasts, osteoclasts, and other matrix-interacting cells via mechanotransduction and integrin-mediated signaling.[9][12][14] Disruption of collagen structure can therefore alter not only the mechanical properties of bone but also cellular responses to mechanical and inflammatory stimuli, contributing to complex phenotypes such as those seen in Caffey disease. The classification of Caffey disease as a “type I collagenopathy” extends the spectrum of COL1A1-related disorders beyond brittle bone disease and classical connective tissue dysplasias, demonstrating that subtle sequence changes can yield distinct tissue- and age-specific phenotypes.[9][12][14]

### 4.2 Pathogenic variant c.3040C>T (p.Arg836Cys / p.Arg1014Cys)

The recurrent Caffey-associated variant is a heterozygous c.3040C>T substitution in exon 41 of COL1A1, leading to an arginine-to-cysteine substitution within the triple-helical domain of the α1(I) chain.[9][12][13][15][16] Due to different numbering conventions that include or exclude the signal peptide and propeptides, this amino acid change has been reported as p.Arg836Cys or p.Arg1014Cys, but both designate the same substitution within the helical region.[9][12][13][15][16] Gensure et al. described this variant as affecting the Y-position of a Gly–X–Y triplet (Arg at the Y position), an unusual type of substitution compared to the more common glycine substitutions observed in osteogenesis imperfecta.[12][14] The JCI commentary on this work notes that, unlike many glycine substitutions that severely disrupt helix stability and have dominant negative effects, the R836C mutation would not be predicted to cause major destabilization, suggesting a subtler structural or functional impact.[14]

ClinVar aggregates submissions describing COL1A1 c.3040C>T as pathogenic for autosomal dominant Caffey disease, citing multiple reports where this variant segregated with disease in families from diverse populations, including Korean patients and several independent kindreds.[15] Medscape emphasizes that this specific variant is a recurrent hotspot mutation across ethnic groups and that detection of c.3040C>T confirms the diagnosis of classic infantile cortical hyperostosis.[16] MedlinePlus Genetics notes that this mutation results in type I collagen fibrils that are variable in size and shape, though the precise mechanism by which these changes cause the signs and symptoms of Caffey disease is not fully understood.[13] Taken together, these findings indicate that COL1A1 c.3040C>T is a gain-of-function or qualitatively altered-function mutation rather than a classic loss-of-function variant, leading to a unique hyperostotic phenotype instead of typical osteopenic OI.

### 4.3 Variant classification, population frequency, and penetrance

In the framework of ACMG/AMP guidelines, the COL1A1 c.3040C>T variant meets multiple criteria for classification as pathogenic, including strong segregation with disease, recurrence in unrelated families, functional impact inferred from location in a critical domain, and absence or extremely low frequency in general population controls.[12][14][15] ClinVar indicates that this variant has been repeatedly reported in individuals and families with infantile cortical hyperostosis and that it exhibits incomplete penetrance, as some carriers do not manifest infantile episodes.[15] The 2014 review notes that 79% of individuals heterozygous for the mutation experienced cortical hyperostosis, while 21% did not, confirming reduced penetrance at the molecular level.[14] This incomplete penetrance is a key consideration in risk counseling and suggests that variant detection is necessary but not sufficient for predicting clinical disease.

Population databases such as gnomAD indicate that the c.3040C>T variant is extremely rare in the general population, consistent with its pathogenic nature; however, a small number of carriers may be present without recorded disease, aligning with incomplete penetrance.[15] Ethnic distribution data from MedlinePlus and Medscape highlight that the variant has been found in diverse ethnicities, including Korean, Thai, Indian, and Australian families, suggesting that it is a recurrent mutation rather than a founder effect confined to a single population.[9][13][15][16] This recurrent nature might reflect a mutational hotspot at this nucleotide position. From a clinical perspective, the very low allele frequency in general populations supports the use of this variant as a diagnostic marker in infants with compatible clinical and radiographic features.

### 4.4 Other genetic findings and heterogeneity (IFITM5 and beyond)

While classic infantile Caffey disease is strongly linked to COL1A1 c.3040C>T, severe prenatal cortical hyperostosis appears genetically heterogeneous. Some lethal prenatal cases, such as the one described by the 1997 case of prenatal cortical hyperostosis, have been found to harbor the same COL1A1 3040C>T mutation, indicating that the same variant can result in a spectrum from benign infantile to lethal prenatal disease, possibly modulated by additional genetic and environmental factors.[11] However, other prenatal cases lack this COL1A1 mutation, and alternative genetic etiologies have been sought. Medscape notes that novel variants in IFITM5, particularly c.119C>T (p.Ser40Leu), have been identified as causes of severe, often lethal prenatal cortical hyperostosis in neonates negative for COL1A1 mutations, placing prenatal Caffey disease within the spectrum of IFITM5-related disorders.[16]

IFITM5 encodes a transmembrane protein expressed in osteoblasts and is known to harbor a recurrent mutation c.-14C>T associated with osteogenesis imperfecta type V, characterized by hyperplastic callus formation and cortical hyperostosis.[16] The identification of IFITM5 variants in prenatal cortical hyperostosis suggests that perturbations in osteoblast-specific signaling pathways can produce hyperostotic phenotypes independent of collagen structural changes. A case series in which prenatal cortical hyperostosis was seen without COL1A1 mutations but with phenotypic similarity to Caffey disease supports this genetic heterogeneity and raises questions about whether prenatal Caffey disease should be classified as a distinct entity.[17][18] These findings underscore that while COL1A1 is the primary causal gene for classic infantile cortical hyperostosis, the broader category of cortical hyperostosis syndromes encompasses multiple genetic etiologies.

### 4.5 Somatic versus germline origin, epigenetics, and structural variants

Available evidence indicates that the COL1A1 c.3040C>T variant in Caffey disease is a germline mutation, present in all cells and transmitted in an autosomal dominant pattern.[12][15][16] Gensure et al. demonstrated heterozygosity for the mutation in affected individuals and obligate carriers, including those with prenatal onset, and did not report somatic mosaicism.[12] De novo occurrences have been documented, as some individuals with Caffey disease have parents without clinical disease and without the mutation, but the proportion of de novo cases is not precisely known.[5][12][13] Somatic variants or mosaicism have not been reported in Caffey disease, although they are known in other collagenopathies and could theoretically contribute to variable expressivity.

No evidence currently implicates large-scale chromosomal abnormalities, copy-number variants, or epigenetic modifications such as DNA methylation changes in the etiology of Caffey disease.[1][8][9] Given that the pathogenic variant is a single nucleotide change in a structurally critical domain, complex structural variants are not necessary to explain the phenotype. At the epigenetic level, it is conceivable that collagen or osteoblast-related gene expression might be modulated by epigenetic factors, influencing penetrance, but no direct data are available. Likewise, transcriptomic, proteomic, or metabolomic profiling specific to Caffey disease has not been reported, limiting insights into global molecular signatures. Mechanistic hypotheses thus remain rooted largely in structural biology and targeted pathway analysis rather than omics-scale data.

## 5. Environmental Information

### 5.1 Prostaglandin E therapy and induced cortical hyperostosis

As noted earlier, a key environmental factor relevant to Caffey-like phenotypes is pharmacologic exposure to prostaglandin E (PGE), particularly PGE1, used in neonates with ductus-dependent congenital heart disease to maintain ductal patency.[9][14] Ueda et al. reported that infants receiving prolonged PGE infusion developed cortical hyperostosis that radiographically and clinically resembled infantile cortical hyperostosis, suggesting that high PGE levels alone can drive periosteal bone formation.[14] Heyman et al. subsequently measured PGE levels in affected children and found them markedly elevated, and observed that treatment with indomethacin, a nonsteroidal anti-inflammatory drug (NSAID) that inhibits COX enzymes and reduces PGE synthesis, led to rapid improvement in irritability and soft-tissue swelling within 6–9 days.[14] The mechanistic review on Caffey disease highlights these findings as evidence that PGE can induce hyperostosis and supports a role for COX-2/PGE signaling in the pathophysiology of Caffey disease.[9][14]

These PGE-induced cases may be considered environmental phenocopies of Caffey disease, although it remains possible that some infants receiving PGE therapy harbor unrecognized collagen or other connective tissue variants that predispose them to exaggerated periosteal responses. Regardless, from a clinical and mechanistic perspective, PGE exposure is a well-documented environmental factor capable of causing hyperostotic lesions in infancy, which can confound diagnosis and informs treatment strategies (e.g., use of COX inhibitors). PGE itself is a bioactive lipid mediator derived from arachidonic acid via COX enzymes, and its role in bone metabolism includes stimulation of bone resorption and formation depending on context; in hyperostosis, excessive or dysregulated PGE signaling likely promotes osteoblastic activity in periosteum.[9][14] Ontologically, PGE corresponds to a CHEBI entity (CHEBI:15551), and its role in hyperostosis links to GO processes such as *response to prostaglandin E* (GO:0035195) and *regulation of osteoblast differentiation* (GO:0045668).

### 5.2 Other environmental and lifestyle factors

Beyond PGE therapy, no consistent environmental exposures have been implicated in Caffey disease. Early hypotheses posited that viral infections or immunologic triggers might initiate inflammatory episodes, but modern case reports often describe infants without preceding infections or trauma, and no specific pathogens have been identified.[9][10][19] Lifestyle factors such as diet, physical activity, or environmental toxins are unlikely to play major roles in a disease that manifests within the first months of life and often resolves spontaneously by age two.[1][5][8] Some historical reports considered hypervitaminosis A, scurvy, or malnutrition in the differential diagnosis, but these conditions have distinct biochemical and radiographic features and are not considered etiologic in Caffey disease.[10] 

It is plausible, though not formally demonstrated, that systemic inflammatory states or mechanical stresses could modulate severity or site-specific manifestations in individuals with the COL1A1 mutation. For example, increased mechanical loading on certain bones or minor trauma might predispose to localized periosteal detachment, acting as a trigger for hyperostosis in genetically predisposed individuals, as suggested by the mechanistic model proposed by Gensure and colleagues.[9] However, this remains speculative, and the current evidence base does not support specific recommendations regarding environmental modification beyond general neonatal care.

### 5.3 Infectious agents and immunologic considerations

No particular infectious agents have been identified as causative in Caffey disease. Historically, the acute inflammatory presentation led some clinicians to suspect osteomyelitis or systemic infection; indeed, infants with Caffey disease often receive empiric antibiotics before the correct diagnosis is established.[7][10][19] However, cultures are typically negative, and histopathology, when performed, shows aseptic inflammation with new bone formation rather than suppurative infection.[9][10][19] The absence of demonstrable pathogens, the familial occurrence, and the identification of a structural collagen lesion all argue against an infectious etiology.[1][9][12]

Nevertheless, immune system involvement is clearly present in the form of inflammatory infiltrates and elevated systemic inflammatory markers. The mechanistic review suggests that the periosteal reaction in Caffey disease may represent a unique immunoinflammatory response to matrix injury, mediated in part by COX-2 and PGE, which modulate both osteoblast and immune cell activity.[9][14] From a Gene Ontology perspective, processes such as *inflammatory response* (GO:0006954), *osteoblast differentiation* (GO:0001649), and *prostaglandin biosynthetic process* (GO:0001516) are relevant. However, no autoimmune or primary immunodeficiency mechanisms have been documented, and thus infection and immunity play more of a downstream or modulatory role rather than being primary etiologic factors.

## 6. Mechanism and Pathophysiology

### 6.1 Ordered causal chain from mutation to phenotype

Step 1: A heterozygous missense mutation in COL1A1 (c.3040C>T; p.Arg836Cys/p.Arg1014Cys) leads to altered type I collagen α1(I) chain structure, resulting in abnormal collagen fibril formation and matrix organization.[9][12][13][14]  

Step 2: The altered collagen matrix in bone and periosteum leads to subtle mechanical and structural fragility or altered mechanotransduction, which results in increased susceptibility of periosteum to detachment or injury under physiological or inflammatory stresses; this step is inferred from radiographic and histologic observations.[9][12][14]  

Step 3: Periosteal detachment and matrix injury lead to activation of local inflammatory responses, including upregulation of COX-2 and increased production of prostaglandin E (PGE), which in turn results in a localized inflammatory milieu around affected bones.[9][14]  

Step 4: Elevated PGE signaling and inflammatory mediators stimulate periosteal osteoblasts and possibly osteoprogenitor cells, leading to exuberant subperiosteal new bone formation and cortical hyperostosis, as evidenced by radiographic and histologic data.[9][12][14]  

Step 5: The new bone formation and associated soft-tissue swelling cause pain, irritability, and decreased limb movement, while systemic spillover of inflammatory mediators results in fever and elevated acute-phase reactants, producing the clinical triad of hyperostosis, soft-tissue swelling, and systemic inflammation.[1][5][8][9][10]  

Step 6: Over time, resolution of inflammation and remodeling of the newly formed bone lead to regression of hyperostosis and normalization of bone structure, although residual deformities and matrix abnormalities in connective tissues persist, leading to adult manifestations such as joint hyperlaxity, skin hyperextensibility, and hernias.[5][8][9][12][14]  

Step 7: In some cases, recurrent or persistent activation of these pathways leads to recurrent episodes of hyperostosis or late-onset cortical thickening, while in severe prenatal cases, early and diffuse activation of the same or related pathways (potentially via different genetic lesions such as IFITM5 variants) results in generalized hyperostosis, skeletal deformity, and possibly lethal perinatal compromise.[11][13][16][17][18]  

### 6.2 Type I collagen structural perturbation and matrix consequences

The central molecular lesion in classic Caffey disease is the substitution of arginine with cysteine in the triple-helical domain of the α1(I) chain of type I collagen.[9][12][13] This domain consists of Gly–X–Y repeats, where glycine occurs every third residue and X and Y positions are often proline or hydroxyproline, contributing to helix stability; however, other charged residues, including arginine, also appear and can participate in electrostatic and hydrogen-bonding interactions.[9][12][14] The JCI commentary notes that the R836C substitution occurs at the Y position, which would not be expected to severely destabilize the triple helix, unlike many glycine substitutions associated with osteogenesis imperfecta, suggesting that the structural impact is more nuanced.[14] Nonetheless, the introduction of a cysteine residue creates a new thiol group that can form aberrant disulfide bonds, potentially leading to abnormal cross-linking, fibril aggregation, or misalignment of collagen fibers.[9][12][14]

MedlinePlus Genetics reports that the COL1A1 mutation that causes Caffey disease results in type I collagen fibrils that are variable in size and shape, although the precise mechanisms linking these changes to clinical manifestations remain unknown.[13] Electron microscopy or biochemical analyses have not been extensively reported in the cited sources, but by analogy to other collagenopathies, one can infer that altered fibril morphology affects mechanical properties such as stiffness, tensile strength, and response to loading, particularly in cortical bone and periosteal regions.[9][14] This altered matrix may render periosteum more prone to detachment under normal mechanical stresses or minor inflammatory insults, providing a structural basis for the hyperostotic response.

From a Gene Ontology perspective, the mutation affects processes such as *collagen fibril organization* (GO:0030199), *extracellular matrix structural constituent* (GO:0005201), and *bone development* (GO:0060348). At the cellular component level, type I collagen fibrils are located in the *extracellular matrix* (GO:0031012), *collagen-containing extracellular matrix* (GO:0062023), and *bone tissue* (UBERON:0002481). The abnormal collagen may alter interaction with integrins and other matrix receptors, influencing signaling pathways controlling osteoblast differentiation and function.

### 6.3 Periosteal biology, COX-2/PGE signaling, and hyperostosis

Periosteum plays a central role in Caffey disease pathophysiology, serving as the site of new bone formation and a key interface between mechanical, inflammatory, and osteogenic processes. The 2014 review suggests that periosteal detachment from underlying bone may be the key pathological process driving hyperostosis, based on radiographic evidence of subperiosteal new bone and thickening.[9] In this scenario, the injury or detachment triggers an inflammatory response that upregulates COX-2, the enzyme responsible for converting arachidonic acid to prostaglandins, including PGE2, which in turn acts in an autocrine and paracrine manner to stimulate osteoblasts and periosteal progenitor cells.[9][14] The review proposes a “local positive feedback loop involving COX-2/PGE signaling” that drives continued new bone formation until the stimulus resolves.[9]

The PGE therapy cases support this model, demonstrating that high PGE levels can mimic or exacerbate the hyperostotic phenotype and that COX inhibition with indomethacin rapidly reduces symptoms.[14] These findings implicate PGE2, acting through its receptors (EP1–EP4), in promoting periosteal bone formation, likely via intracellular pathways such as cAMP/PKA, PI3K–AKT, and MAPK, which regulate osteoblast proliferation and differentiation.[9][14] From a GO standpoint, relevant processes include *prostaglandin E biosynthetic process* (GO:0001516), *positive regulation of ossification* (GO:0045778), and *regulation of osteoblast proliferation* (GO:0033688). The key cell types involved include periosteal osteoblasts (CL:0000129), osteoprogenitor cells (CL:0002518), and inflammatory cells such as macrophages (CL:0000235) and neutrophils (CL:0000775) that produce cytokines and prostaglandins.

In Caffey disease, the altered collagen matrix may sensitize the periosteum to PGE-mediated signals or enhance the magnitude and spatial pattern of osteogenic responses. For example, abnormal fibrils might alter the distribution or binding of PGE or cytokines in the matrix, leading to localized amplification of signaling. Alternatively, altered mechanical properties of the periosteum–bone interface may increase microinjury and release of damage-associated molecular patterns (DAMPs), which then stimulate COX-2 expression in resident cells. These mechanistic hypotheses remain to be tested experimentally but provide a coherent framework linking genetic and inflammatory pathways.

### 6.4 Immune and inflammatory mechanisms

Although Caffey disease is not primarily an immune disorder, inflammation plays a pivotal role in generating symptoms and possibly in driving hyperostosis. Histologic descriptions in the literature, as summarized in the 2014 review and case reports, indicate acute inflammation of soft tissues contiguous with hyperostotic bone, with infiltration of inflammatory cells and edema.[9][19] Clinically, infants exhibit fever, elevated ESR and CRP, leukocytosis, and sometimes thrombocytosis, all hallmarks of systemic inflammation.[1][8][10] These features correspond to GO processes such as *acute inflammatory response* (GO:0002526) and *immune system process* (GO:0002376). The inflammatory milieu likely includes cytokines such as IL-1, IL-6, and TNF, which are known to modulate bone remodeling, although specific cytokine profiles have not been reported for Caffey disease.

The JCI commentary notes that in Caffey disease, “hyperirritability, acute inflammation of soft tissues, and profound alterations of the shape and structure of the underlying bones” occur, highlighting the intertwined nature of inflammation and structural change.[14] The COX-2/PGE axis, as discussed above, bridges inflammation and bone formation, making it a central node in the pathophysiology. The fact that NSAIDs such as indomethacin can ameliorate symptoms and possibly limit hyperostosis by inhibiting prostaglandin synthesis underscores the functional importance of inflammatory pathways.[9][14] However, the inflammatory response in Caffey disease appears self-limited, resolving as bone remodeling progresses, and there is no evidence of chronic autoimmune processes or systemic immune deficiency.

### 6.5 Tissue damage, remodeling, and resolution

Caffey disease offers a striking example of how acute tissue damage and inflammatory responses can be followed by robust remodeling and resolution, at least in the infantile form. The initial insult—whether due to mechanical microinjury, abnormal collagen, or PGE-driven inflammation—leads to periosteal detachment and new bone formation, producing hyperostosis and deformity.[9][12] Over time, however, osteoclast-mediated resorption and osteoblast-mediated remodeling restore more normal cortical architecture, with radiographs often appearing normal by late infancy or early childhood.[7][10][19] This dynamic process involves tightly regulated activities of osteoclasts (CL:0000109) and osteoblasts, and GO processes such as *bone remodeling* (GO:0046849), *osteoclast differentiation* (GO:0030316), and *osteoblast differentiation* (GO:0001649).

In some cases, incomplete remodeling or repeated episodes may leave residual deformities, such as bowing of long bones or mandibular enlargement, and adult connective tissue manifestations reflect persistent matrix abnormalities beyond the bone.[5][8][9][12][14] From a tissue damage perspective, Caffey disease involves limited necrosis or fibrosis; instead, it is primarily characterized by excessive, but ultimately remodelable, bone formation. This contrasts with other inflammatory bone diseases where chronic inflammation leads to fibrosis or permanent damage. The self-limited nature of hyperostosis suggests that once the initiating inflammatory or mechanical signals resolve, the bone’s intrinsic remodeling capacity restores structural equilibrium.

### 6.6 Relationship to other collagenopathies and IFITM5-related disorders

Caffey disease extends the spectrum of collagenopathies and highlights how different mutations in the same gene can produce distinct phenotypes. In osteogenesis imperfecta, most pathogenic COL1A1 mutations involve glycine substitutions in the triple helix or premature stop codons leading to haploinsufficiency, causing brittle bones, fractures, and growth deficiency.[9][12][14] In contrast, the R836C mutation in Caffey disease does not primarily cause osteopenia or fractures in infancy; instead, it leads to localized hyperostosis and only later increased fracture risk in some adults.[9][12] The JCI commentary emphasizes that this mutation “would not be predicted to have such an effect on the collagen molecule” as glycine substitutions, implying that it may alter specific interactions or post-translational modifications rather than global helix stability.[14] Furthermore, the overlap of adult features with Ehlers–Danlos syndrome hypermobility type—joint laxity and skin hyperextensibility—indicates that this mutation affects connective tissue properties in a way that transcends bone alone.[9][12][14]

The identification of IFITM5 variants in prenatal cortical hyperostosis underscores that different molecular pathways can converge on similar hyperostotic phenotypes.[16][17][18] IFITM5 is a small membrane protein expressed in osteoblasts and has been implicated in regulation of bone formation and mineralization; the recurrent promoter mutation c.-14C>T causes OI type V, characterized by hyperplastic callus and interosseous membrane ossification.[16] The newly reported IFITM5 p.Ser40Leu variant associated with prenatal cortical hyperostosis suggests that gain-of-function alterations in osteoblast signaling can produce diffuse hyperostosis, perhaps via increased osteoblast proliferation or altered response to mechanical or hormonal signals.[16] In this context, Caffey disease and related hyperostosis syndromes can be seen as part of a broader group of disorders involving dysregulated periosteal bone formation, whether due to matrix abnormalities (COL1A1), signaling defects (IFITM5), or pharmacologic exposure (PGE).

### 6.7 Upstream versus downstream mechanisms and knowledge gaps

In the causal chain outlined above, COL1A1 mutation and, in some cases, IFITM5 variants or PGE exposure represent upstream initiators, altering matrix structure or signaling pathways. These upstream events lead to mid-level mechanisms such as periosteal detachment, COX-2/PGE upregulation, and inflammatory cell recruitment, which are directly responsible for the downstream clinical manifestations—hyperostosis, pain, swelling, and systemic inflammation.[9][12][14] Upstream mechanisms occur at the level of gene and protein structure (COL1A1, IFITM5), while mid-level mechanisms operate at the level of cells (osteoblasts, osteoclasts, macrophages) and tissues (periosteum, cortical bone). Downstream mechanisms include symptom generation and long-term remodeling.

Significant knowledge gaps remain. For example, the precise structural effect of R836C on collagen fibrils and how it alters cell–matrix interactions is not fully characterized. The exact contribution of COX-2/PGE versus other inflammatory mediators in driving hyperostosis is inferred from pharmacologic data but lacks direct mechanistic dissection in this disease.[9][14] The reasons for incomplete penetrance, variability in severity, and the presence of lethal prenatal forms in some but not all carriers of the same mutation are not understood, suggesting that modifier genes, epigenetic factors, or stochastic events play important roles. There are no omics-level datasets (e.g., transcriptomics, proteomics) specific to Caffey disease, and no experimental models precisely reproducing the R836C mutation in animals have been extensively reported. These gaps limit the ability to design targeted therapies beyond general anti-inflammatory approaches.

## 7. Anatomical Structures Affected

### 7.1 Skeletal distribution and organ-level involvement

Caffey disease predominantly affects the skeletal system, with specific anatomic predilection. The mandible is the most commonly involved bone, affected in 70–90% of cases, and is often used as a defining diagnostic criterion.[9][10][13] Clavicles are affected in about half of cases, ribs and scapulae in 20–30%, and long bones such as tibia, ulna, radius, and femur show diaphyseal involvement.[1][8][9][10] The pelvis and skull can also be involved, with case reports of skull base sclerosis and calvarial hyperostosis.[19] These structures correspond to UBERON terms such as *mandible* (UBERON:0001684), *clavicle* (UBERON:0001105), *rib* (UBERON:0002223), *scapula* (UBERON:0002372), *femur* (UBERON:0000981), *tibia* (UBERON:0000979), *ulna* (UBERON:0001423), *radius* (UBERON:0001421), and *skull* (UBERON:0003129).

Organ-level secondary involvement arises mainly from skeletal changes. For instance, hyperostosis of ribs and clavicles can affect thoracic compliance and breathing in severe cases, particularly in prenatal-onset disease.[11][17][18] Mandibular hyperostosis can cause facial deformity, feeding difficulties, or airway compromise if severe, although in classic infantile cases these issues are usually transient and mild.[9][10][19] There is no primary involvement of internal solid organs such as liver, kidney, or brain, and systemic symptoms such as fever arise from inflammatory mediators rather than organ-specific pathology.[1][5][8] Thus, the primary organ system involved is the musculoskeletal system, particularly bone and connective tissues, with secondary effects on respiratory and gastrointestinal function in severe cases.

### 7.2 Tissue-level pathology: bone, periosteum, and soft tissues

At the tissue level, Caffey disease involves cortical bone, periosteum, and adjacent soft tissues. Radiologic and histologic descriptions emphasize massive subperiosteal new bone formation, leading to cortical thickening and spindle-shaped diaphyses.[1][8][9][10][19] The new bone originates from the inner cambium layer of the periosteum, which contains osteoprogenitor cells capable of intramembranous bone formation.[9][19] Histology reveals layers of woven bone beneath the lifted periosteum, gradually maturing to lamellar bone as remodeling proceeds.[9] Soft-tissue swelling reflects edema and inflammatory infiltrates in subcutaneous tissues and muscle adjacent to hyperostotic bone, sometimes accompanied by increased vascularity and venous prominence.[9][10][19] In skull base cases, thickening of cranial bones and mandible is accompanied by soft-tissue proliferation around the face and neck.[19]

These tissue-level changes align with UBERON terms such as *cortical bone* (UBERON:0002485), *periosteum* (UBERON:0002416), and *subcutaneous tissue* (UBERON:0002190). The primary tissue type involved is connective tissue, comprising bone matrix (mineralized collagen), periosteal fibrous tissue, and associated vasculature. There is no primary involvement of muscle fibers or cartilage, although muscles may be secondarily affected by swelling and altered biomechanics. The presence of acute inflammation in soft tissues places Caffey disease at the intersection of orthopedic and inflammatory pathology.

### 7.3 Cellular participants and cell-type ontology

Key cell types in Caffey disease include osteoblasts, osteocytes, osteoclasts, periosteal fibroblasts, endothelial cells, and inflammatory cells such as macrophages and neutrophils. Osteoblasts (CL:0000129) are responsible for the deposition of new subperiosteal bone; they differentiate from mesenchymal osteoprogenitors residing in the periosteum (CL:0002518). Osteoclasts (CL:0000109) mediate resorption and remodeling of the hyperostotic bone, particularly during resolution.[9][19] Periosteal fibroblasts (CL:0002553) contribute to the fibrous layer of the periosteum and may produce extracellular matrix components, including collagen, which is affected by the COL1A1 mutation.[9][14] Endothelial cells (CL:0000115) form blood vessels needed for the vascularized periosteal callus.

Inflammatory cells include macrophages (CL:0000235), neutrophils (CL:0000775), and possibly lymphocytes (CL:0000542), which infiltrate soft tissues and periosteum during acute episodes.[9][19] These cells produce cytokines and prostaglandins, including PGE2, which influence osteoblast activity and matrix remodeling.[9][14] The interplay between these cell types is captured in GO terms such as *osteoblast differentiation* (GO:0001649), *osteoclast differentiation* (GO:0030316), *macrophage activation* (GO:0042116), and *inflammatory response* (GO:0006954). The COL1A1 mutation affects primarily osteoblast-produced collagen, but because type I collagen is also synthesized by fibroblasts and other mesenchymal cells, broader connective tissue changes occur.

### 7.4 Subcellular compartments and extracellular matrix localization

At the subcellular level, the key compartments involved in Caffey disease are those related to collagen biosynthesis and secretion: the rough endoplasmic reticulum (ER), Golgi apparatus, secretory vesicles, and extracellular space. The α1(I) collagen chain is synthesized in the ER, undergoes post-translational modifications such as hydroxylation and glycosylation, and assembles into triple helices with α2(I) chains before being transported through the Golgi and secreted.[9][12][14] Misfolded or aberrantly modified collagen may be retained in the ER or secreted but organize abnormally into fibrils in the extracellular matrix. The introduction of a cysteine residue could facilitate aberrant disulfide bond formation in the ER or extracellular space, affecting fibril packing.[9][12][14] Relevant GO cellular components include *endoplasmic reticulum* (GO:0005783), *Golgi apparatus* (GO:0005794), *collagen-containing extracellular matrix* (GO:0062023), and *bone matrix* (UBERON:0002481).

The extracellular matrix in bone is a composite of collagen fibrils and mineralized hydroxyapatite, with non-collagenous proteins such as osteocalcin and osteonectin modulating mineral deposition. In Caffey disease, altered collagen fibrils likely change the microenvironment sensed by osteoblasts and osteocytes, possibly influencing mechanosensitive signaling pathways. While these subcellular processes are inferred from general collagen biology rather than disease-specific experiments, they provide a plausible mechanistic link between gene mutation and tissue-level pathology.

### 7.5 Localization, lateralization, and asymmetry

Clinically and radiographically, Caffey disease often displays asymmetric involvement of bones, particularly in long bones and ribs.[7][9][10][19] For example, Radiopaedia’s case shows more pronounced hyperostosis in the left femur compared to the right and subtle periostitis in lower ribs, while another case report describes unilateral mandibular swelling and unilateral involvement of long bones.[7][10] The 2014 review notes that bone lesions are often asymmetric, although symmetric involvement can also occur.[9] Lateralization is thus variable, and no consistent side predominance has been reported. This asymmetry suggests that local factors—such as mechanical stress, microtrauma, or regional differences in vascular supply—modulate expression of the systemic genetic lesion.

Localization to diaphyses rather than metaphyses or epiphyses is another consistent pattern, likely reflecting the thicker periosteum and different mechanical environment in mid-shaft regions.[9][10][19] Prenatal cases, however, may show more diffuse involvement, with generalized hyperostosis of long bones, ribs, and mandible, indicating that in severe forms the disease is less regionally restricted.[11][17][18] Understanding these localization patterns could offer insights into mechanobiology and regional differences in periosteal structure, but detailed studies are lacking.

## 8. Temporal Development

### 8.1 Age of onset and onset patterns

Classic Caffey disease is an early-onset disorder. OMIM and MedGen note that episodes of massive subperiosteal new bone formation usually begin before the age of 5 months, and GeneReviews specifies that onset is between birth and five months, with the majority of infants presenting within the first six months of life.[1][5][8] Medscape cites an average age at onset of approximately 6.8 weeks in the familial form, with about 24% of cases present at birth, indicating that congenital or perinatal onset is not uncommon.[16] Case reports align with this range, describing infants presenting at 2.5 to 4 months with swelling, pain, and fever.[7][10][19] 

The onset pattern is typically acute or subacute, with symptoms developing over days to weeks rather than insidiously over months. Parents may notice sudden swelling, increased irritability, and refusal to move the affected limb, prompting medical evaluation.[7][10][19] Prenatal forms, by contrast, manifest on fetal ultrasound or MRI as early as the late second or early third trimester (around 27–30 weeks gestation), with detection of short, hyperostotic long bones and sometimes polyhydramnios.[11][16][18] These prenatal presentations are often mistaken for osteogenesis imperfecta or other skeletal dysplasias until histology or molecular testing clarifies the diagnosis.[11][18]

### 8.2 Disease course and progression in classic infantile form

In classic infantile Caffey disease, the disease course is generally self-limited and monophasic, though recurrences can occur. The initial episode involves acute inflammation, bone pain, and hyperostosis, which evolve over several weeks to months.[1][5][8][9] Soft-tissue swelling and systemic symptoms such as fever and irritability typically improve within a few weeks, especially with supportive care and NSAIDs, while radiographic hyperostosis peaks later and then gradually regresses.[7][10][19] The majority of cases show complete clinical resolution by age two years, and radiographs often normalize by approximately one year, as demonstrated in Radiopaedia’s case where radiographs at 11 months were “perfectly normal.”[7][10][19] GeneReviews describes the disease as “spontaneously resolving by age two years,” emphasizing its self-limited nature.[5][8]

The progression can be conceptualized in stages: an acute inflammatory stage with soft-tissue swelling and pain, a subacute stage with maximal cortical thickening, and a chronic stage of remodeling and resolution. The rate of progression varies, but the overall course is relatively rapid compared to chronic skeletal dysplasias. The disease pattern is episodic rather than continuously progressive; once an episode resolves, there may be a prolonged asymptomatic period or no recurrence at all.[5][8][9] However, some individuals experience recurrent episodes of hyperostosis, sometimes in different bones, later in childhood or adolescence, suggesting that the susceptibility persists even after the initial resolution.[9]

### 8.3 Prenatal and severe forms: temporal and clinical differences

Prenatal cortical hyperostosis represents a more severe temporal variant of the disease. In such cases, hyperostosis begins in utero, often leading to detectable skeletal abnormalities on prenatal ultrasound or MRI by the late second or early third trimester.[11][16][18] Because intrauterine space and resources are limited, diffuse hyperostosis and bone angulation can lead to fetal movement restriction, polyhydramnios, and, in some cases, hydrops or fetal demise.[11][17][18] The 1997 case described severe hyperostosis with diaphyseal ballooning of long bones, rib and mandibular hyperostosis, and histology consistent with infantile cortical hyperostosis; the pregnancy was terminated at 30 weeks after presumptive diagnosis of severe osteogenesis imperfecta.[11] In other reported cases, infants with prenatal-onset hyperostosis have survived, with postnatal radiographs showing diffuse hyperostosis that gradually remodels over months to years.[17][18]

These prenatal cases demonstrate that the pathogenic mechanisms can operate much earlier in development and that severity is not solely a function of postnatal environment. The onset is congenital, and progression can be life-threatening, particularly due to thoracic restriction and respiratory compromise. Medscape notes that prenatal cortical hyperostosis is more diffuse and non-inflammatory compared to infantile Caffey disease, and that its pathogenetic mechanisms are less well defined.[16][17] From a temporal standpoint, prenatal forms can be considered a distinct disease trajectory with early, diffuse, and sometimes lethal manifestations, in contrast to the late neonatal/infantile onset of classic Caffey disease.

### 8.4 Recurrence, late episodes, and long-term course

While classic Caffey disease is often monophasic, recurrences of bone hyperostosis, fever, and soft-tissue swelling later in life have been documented.[5][8][9] GeneReviews notes that recurrence of bone hyperostosis and associated symptoms can occur later in life and that adults with a history of Caffey disease may develop late skeletal deformities, fractures, and connective tissue manifestations.[5][8] The 2014 review reports several cases of recurrence during adolescence, indicating that the pathogenic mechanisms can be reactivated under certain conditions.[9] These late episodes may involve previously affected bones or new sites, and their triggers are not well understood but could include mechanical stress, hormonal changes, or other systemic factors.

In the long term, many individuals have normal or near-normal skeletal function, particularly if disease was mild and resolved fully in infancy.[5][8][9][10] However, some may have residual deformities, such as bowed long bones, mandibular enlargement, or thoracic shape changes, which can affect aesthetics or function. Adult connective tissue manifestations—joint hypermobility, skin hyperextensibility, and hernias—may lead to chronic musculoskeletal pain, joint instability, or need for surgical repair.[9][12][14] Thus, while the acute disease is self-limited, the long-term course can include chronic manifestations of the underlying collagenopathy.

## 9. Inheritance and Population

### 9.1 Inheritance pattern and penetrance

Caffey disease is inherited in an **autosomal dominant** manner. OMIM, MedGen, GeneReviews, and GTR all explicitly describe the disorder as autosomal dominant, with males and females affected equally

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 62 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 47 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0004423` (1 mention) - the report calls it "Cortical hyperostosis"; HP calls it **Cranium bifidum occultum**
- `HP:0030892` (1 mention) - the report calls it "Diaphyseal thickening"; HP calls it **Deep cerebral white matter hyperintensities**
- `HP:0005309` (1 mention) - the report calls it "Periosteal reaction"; HP calls it **obsolete Peripheral vascular insufficiency**
- `HP:0002816` (1 mention) - the report calls it "Long bone bowing"; HP calls it **Genu recurvatum**
- `GO:0035195` (1 mention) - the report calls it "response to prostaglandin E"; GO calls it **miRNA-mediated post-transcriptional gene silencing**
- `UBERON:0002223` (1 mention) - the report calls it "rib"; UBERON calls it **endolymphatic sac**
- `UBERON:0002372` (1 mention) - the report calls it "scapula"; UBERON calls it **tonsil**
- `UBERON:0001423` (1 mention) - the report calls it "ulna"; UBERON calls it **radius bone**
- `UBERON:0001421` (1 mention) - the report calls it "radius"; UBERON calls it **pectoral girdle region**
- `UBERON:0002485` (1 mention) - the report calls it "cortical bone"; UBERON calls it **prostate duct**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0003389` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005309` (obsolete Peripheral vascular insufficiency) (1 mention) - replaced by `HP:0004950`
- `GO:0062023` (obsolete collagen-containing extracellular matrix) (2 mentions) - replaced by `GO:0031012`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003155` (1 mention) - the report calls it "Elevated serum alkaline phosphatase"; HP calls it **Elevated circulating alkaline phosphatase concentration**, and lists "Elevated alkaline phosphatase" among its other names
- `HP:0001974` (1 mention) - the report calls it "Leukocytosis"; HP calls it **Increased total leukocyte count**, and lists "Leukocytosis" among its other names
- `HP:0001873` (1 mention) - the report calls it "Thrombocytosis"; HP calls it **Thrombocytopenia**
- `HP:0000974` (1 mention) - the report calls it "Skin hyperextensibility"; HP calls it **Hyperextensible skin**, and lists "Skin hyperextensibility" among its other names
- `HP:0003623` (1 mention) - the report calls it "Prenatal onset"; HP calls it **Neonatal onset**
- `GO:0045668` (1 mention) - the report calls it "regulation of osteoblast differentiation"; GO calls it **negative regulation of osteoblast differentiation**, and lists "downregulation of osteoblast differentiation" among its other names
- `GO:0001516` (2 mentions) - the report calls it "prostaglandin biosynthetic process", "prostaglandin E biosynthetic process"; GO calls it **prostaglandin biosynthetic process**
- `GO:0062023` (2 mentions) - the report calls it "collagen-containing extracellular matrix"; GO calls it **obsolete collagen-containing extracellular matrix**
- `UBERON:0002481` (2 mentions) - the report calls it "bone tissue", "bone matrix"; UBERON calls it **bone tissue**
- `UBERON:0002416` (1 mention) - the report calls it "periosteum"; UBERON calls it **integumental system**, and lists "dermal system" among its other names
- `UBERON:0002190` (1 mention) - the report calls it "subcutaneous tissue"; UBERON calls it **subcutaneous adipose tissue**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0001516` - called "prostaglandin biosynthetic process", "prostaglandin E biosynthetic process"
- `UBERON:0002481` - called "bone tissue", "bone matrix"