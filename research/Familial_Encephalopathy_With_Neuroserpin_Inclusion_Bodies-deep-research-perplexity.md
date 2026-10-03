---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-03T21:22:05.988333'
end_time: '2026-10-03T21:25:47.205400'
duration_seconds: 221.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial Encephalopathy With Neuroserpin Inclusion Bodies
  mondo_id: MONDO:0011412
  category: Mendelian
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
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 10
  verified: 8
  not_found: 0
  obsolete: 2
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 5
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0000720
    reported_labels:
    - Dementia
    ontology_label: obsolete Mood swings
  - term_id: HP:0006893
    reported_labels:
    - Frontal lobe dysfunction
    ontology_label: obsolete Severely dysplastic cerebellum
  - term_id: HP:0002352
    reported_labels:
    - Progressive cognitive decline
    ontology_label: Leukoencephalopathy
  labels_variant: 1
  obsolete_terms:
  - term_id: HP:0000720
    ontology_label: obsolete Mood swings
    replaced_by: HP:0000712
  - term_id: HP:0006893
    ontology_label: obsolete Severely dysplastic cerebellum
    replaced_by: HP:0007033
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Encephalopathy With Neuroserpin Inclusion Bodies
- **MONDO ID:** MONDO:0011412 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Encephalopathy With Neuroserpin Inclusion Bodies** covering all of the
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

# Familial Encephalopathy With Neuroserpin Inclusion Bodies (FENIB): Comprehensive Disease Characteristics Report

Familial encephalopathy with neuroserpin inclusion bodies (FENIB) is a paradigmatic **Mendelian serpinopathy of the nervous system** that illustrates how point mutations in a conformationally labile protease inhibitor can drive slowly progressive neurodegeneration through intracellular polymer accumulation, endoplasmic reticulum (ER) stress, and circuit-level dysfunction culminating in epilepsy and dementia.[1][2][4][9][18] Clinically, FENIB is characterized by variable-age onset cognitive decline with prominent frontal-executive deficits, progressive myoclonus epilepsy and other seizure types that are often medically refractory, and additional neurological manifestations such as tremor, dysarthria, cerebellar signs and pyramidal tract involvement.[2][3][5][8][10] Neuropathologically, the disease is defined by round, eosinophilic, periodic acid–Schiff (PAS)-positive, diastase-resistant neuronal inclusions known as Collins bodies, composed almost exclusively of polymerized mutant neuroserpin retained within the ER of cortical and subcortical neurons.[1][2][9][17][18] Genetically, FENIB results from heterozygous missense variants in the **SERPINI1** gene (also known as *PI12*), located on chromosome 3q26.1, with at least six pathogenic substitutions (e.g. S49P, S52R, H338R, G392E, G392R, R393P) showing a clear genotype–phenotype correlation in which more polymerogenic mutations lead to earlier onset and more severe disease.[1][4][8][9][10][13][18] The condition is exceptionally rare, with Orphanet estimating a prevalence below one per million and MedlinePlus noting only a small number of reported families and sporadic cases worldwide.[3][5] At present, FENIB lacks disease-modifying therapy; management is largely supportive and symptomatic, and the disorder carries a shortened life expectancy, particularly when seizures begin early in life and are difficult to control.[5][10] However, intensive mechanistic work in human tissue, cell systems and transgenic mouse and fly models has made FENIB an important model for understanding serpin polymerization, ER stress–mediated neurodegeneration, and the neurobiology of the neuroserpin–tissue plasminogen activator (tPA) axis, with implications extending to more common dementias and neurodegenerative diseases.[4][9][13][14][16][17]

## 1. Disease Information

### 1.1 Overview and Clinical Definition

Familial encephalopathy with neuroserpin inclusion bodies is a rare autosomal dominant neurodegenerative disease classified among the **serpinopathies**, a group of disorders caused by mutations in serine protease inhibitors leading to protein misfolding and intracellular polymer accumulation.[1][4][9][18] The disease was first recognized in the late 1990s in multigenerational families presenting with presenile dementia, tremor and seizures, in whom neuropathological examination revealed previously undescribed neuronal inclusions that were histologically and biochemically distinct from other known inclusion body dementias.[2][7] Davis and colleagues reported that affected individuals developed an insidious onset of cognitive decline in the fifth decade, with impairment of attention, concentration and daily living skills, personality change, and relatively less marked memory disturbance compared to Alzheimer disease.[2] Subsequent work demonstrated that these inclusions, termed Collins bodies, were composed predominantly of neuroserpin, a neuron-specific serpin that normally functions as an extracellular inhibitor of tPA.[2][4][7][12]

OMIM designates the disorder as “encephalopathy, familial, with neuroserpin inclusion bodies” under entry #604218, using a number sign to indicate that it is caused by heterozygous mutation in the **SERPINI1** gene (MIM 602445) on chromosome 3q26.1.[1] The OMIM summary emphasizes progressive epilepsy and dementia, autosomal dominant inheritance, variable severity and age of onset spanning the second to fifth decades.[1] Orphanet similarly defines FENIB as “a rare serpinopathy characterized by progressive myoclonus epilepsy and/or pre-senile dementia with prominent frontal-lobe features and relative sparing of recall memory,” noting that other neurological manifestations such as cerebellar symptoms and pyramidal signs may occur and that age of onset is highly variable, with reported cases in children as well as elderly patients.[3] MedlinePlus describes FENIB as a disorder causing progressive brain dysfunction (encephalopathy) characterized by dementia, seizures and personality change, often beginning with problems in attention and concentration, dysregulated thought and speech, and later impairment of judgment, insight and memory.[5]

Taken together, FENIB can be succinctly defined as a **monogenic, autosomal dominant neurodegenerative disorder due to SERPINI1 missense variants**, clinically manifesting as progressive frontal-predominant dementia and epilepsy (particularly myoclonic seizures) and pathologically defined by ER-retained neuroserpin polymers forming Collins bodies in cortical and subcortical neurons.[1][2][3][4][5][9] It belongs to the broader MONDO category of Mendelian neurological diseases; the user has provided the Mondo Disease Ontology identifier MONDO:0011412 corresponding to this condition. In ICD-11, KEGG notes association with code 8A61.41 under “Genetic or presumed genetic syndromes primarily expressed as epilepsy,” reflecting the prominent seizure phenotype.[6][11] The disease also aligns with MeSH headings for “Dementia,” “Myoclonic Epilepsies, Progressive,” and “Serpins” when indexing the mechanistic literature.

### 1.2 Key Identifiers and Nosology

Multiple authoritative databases provide standardized identifiers for FENIB, anchoring the disease within biomedical ontologies and classification systems. OMIM lists the disorder as entry **#604218**, “ENCEPHALOPATHY, FAMILIAL, WITH NEUROSERPIN INCLUSION BODIES,” and links it causally to **SERPINI1** (MIM 602445).[1] Orphanet refers to the disease as “Familial encephalopathy with neuroserpin inclusion bodies” with Orpha number **85110**, noting its prevalence below 1 in 1,000,000 and autosomal dominant inheritance.[3] KEGG DISEASE includes the entry H01212 “Familial encephalopathy with neuroserpin inclusion bodies,” specifying that it is an autosomal dominant dementia characterized by accumulation of mutant neuroserpin as PAS-positive, diastase-resistant inclusions, and places it under nervous system diseases, epilepsy or seizures, genetic epileptic syndromes (ICD-11 8A61.41).[6][11]

MedlinePlus Genetics provides an educational entry titled “Familial encephalopathy with neuroserpin inclusion bodies,” and separately an entry on the SERPINI1 gene, further linking gene and phenotype.[5][12][15] Human phenotype ontology resources (though not explicitly in the provided search results) would logically index the disease under MONDO:0011412, with associated HPO terms such as “Seizures” (HP:0001250), “Myoclonus” (HP:0001336), “Dementia” (HP:0000720), “Frontal lobe dysfunction” (HP:0006893), and “Progressive cognitive decline” (HP:0002352), based on the clinical descriptions in OMIM, Orphanet and MedlinePlus.[1][3][5][8][10] 

Synonyms and alternative names are explicitly listed by Orphanet and MedlinePlus. Orphanet uses “FENIB” as an acronym and synonym.[3] MedlinePlus lists several alternative designations including “Familial dementia with neuroserpin inclusion bodies,” “Neuroserpin encephalopathy,” “neuroserpinosis,” “Progressive myoclonus epilepsy associated with neuroserpin inclusion bodies,” and “Progressive myoclonus epilepsy associated with neuroserpinosis,” reflecting the dual emphasis on epilepsy and dementia.[5] Pathology-oriented sources such as Humpath use “FENIB (familial encephalopathy with neuroserpin inclusion bodies)” and “neuroserpin encephalopathy” interchangeably, and highlight that it is an inclusion body dementia due to PI12 gene mutations.[18]

From a nosological standpoint, FENIB sits at the intersection of several overlapping categories: it is a **dementia syndrome**, an **epileptic encephalopathy**, a **progressive myoclonus epilepsy**, and a **protein misfolding disease** within the serpinopathy family.[4][6][8][9][13] KEGG and OMIM emphasize presenile dementia and epilepsy, whereas Orphanet and MedlinePlus emphasize progressive myoclonus epilepsy and frontal lobe dementia, underscoring the phenotypic heterogeneity.[3][5][6] The disease is **Mendelian** in inheritance and is considered **monogenic**, with no evidence to date that polygenic risk or environmental exposures play major causal roles beyond modulating general vulnerability to neurodegeneration.

### 1.3 Data Sources and Evidence Basis

The information available for FENIB stems primarily from **aggregated disease-level resources** and a small number of **case reports, family studies, and mechanistic investigations** rather than large epidemiological cohorts or electronic health record analyses. OMIM, Orphanet, KEGG and MedlinePlus synthesize data from these primary reports into structured summaries.[1][3][5][6][11] The original clinical characterization and genetic mapping derive from the familial cases reported by Davis et al. and Lomas and colleagues, including a large New York State family and an Oregon family with autosomal dominant transmission, as well as later families with distinct SERPINI1 mutations.[2][7][9] Subsequent case reports, such as the neuroserpin encephalopathy with coexistent multiple sclerosis described by Nguengang Wakap et al. and colleagues, and the recent report of FENIB presenting as catatonia, expand the phenotypic spectrum and illustrate diagnostic challenges.[8][10]

Mechanistic understanding comes largely from **in vitro protein biochemistry**, **cell biology experiments in transfected cell lines**, and **transgenic mouse and fly models** expressing wild-type or mutant neuroserpin, as reviewed comprehensively by recent articles by Miranda, Lomas and co-workers on neuroserpin structure, function, physiology and pathology.[4][13][14][17] These sources are catalogued in databases such as PubMed and ClinVar, and many are freely accessible through PubMed Central, enabling detailed structural and functional analyses.[4][9][13][14][16][17] The disease remains extremely rare, and there is no dedicated registry or large natural history study, so prevalence and clinical variability estimates are based on a handful of kindreds and isolated patients rather than population-based data.[3][5][8][10]

In summary, the evidence base for FENIB primarily comprises **clinical case series and reports**, **family-based linkage and genetic analyses**, and **mechanistic laboratory and animal studies**, integrated into disease-level summaries by OMIM, Orphanet, KEGG and MedlinePlus.[1][2][3][4][5][6][9][13] There are no randomized clinical trials or large observational cohorts, which must be considered when evaluating epidemiological and prognostic claims.

## 2. Etiology

### 2.1 Genetic Causal Factors

The primary etiological factor in FENIB is germline mutation in **SERPINI1**, encoding neuroserpin. OMIM explicitly states that familial encephalopathy with neuroserpin inclusion bodies “is caused by heterozygous mutation in the SERPINI1 gene (602445) on chromosome 3q26.”[1] Davis et al. and Lomas et al. report autosomal dominant inheritance in multiple families, with complete cosegregation of SERPINI1 missense variants and disease phenotype.[2][7][9] In the original families, two different heterozygous missense mutations were identified in the PI12 (SERPINI1) gene: a serine-to-proline substitution at position 49 (S49P, “Syracuse” mutation) and a serine-to-arginine substitution at position 52 (S52R, “Portland” mutation).[1][2][7][9][18] These mutations lie in the **shutter region** of the serpin fold, a structurally critical area that regulates opening of the latent conformation and is essential for inhibitory mechanism and conformational stability.[4][9][13]

Subsequent work has identified additional pathogenic SERPINI1 missense variants. The Human Molecular Genetics study by Miranda et al. describes four mutations (S49P, S52R, H338R, G392E) that cause FENIB, all affecting the shutter region and demonstrating a correlation between the predicted molecular instability and the number of neuroserpin inclusions and an inverse correlation with age of onset.[9] The neuroserpin encephalopathy case reported with coexistent multiple sclerosis notes that five different PI12 mutations had previously been described—S49P, S52R, H338R, G392E, G392R—before they identified their novel mutation, and that all are associated with accumulation of mutant neuroserpin within neurons forming intracytoplasmic inclusions.[8] A recent psychiatric case report of FENIB presenting as catatonia describes a heterozygous variant of uncertain significance in exon 9 of SERPINI1 (c.1178G>C; p.Arg393Pro), diagnosed as familial encephalopathy with neuroserpin inclusion bodies based on genomic nomenclature Chr3:g.167543056G>C, again pointing to the pathogenicity of mutations in the C-terminal shutter region.[10]

Biochemical characterization of S49P and S52R neuroserpin shows that both variants have greatly reduced ability to inhibit tPA and a high tendency to form polymers, in keeping with the general mechanism of serpinopathies where point mutations destabilize the native conformation and favor polymerization.[4][13][18] Experimental expression of mutant neuroserpin in COS-7 cells and transgenic mice demonstrates retention of ordered polymers within the ER and formation of intracellular inclusion bodies analogous to Collins bodies.[9][17] In mice overexpressing Syracuse (S49P) and Portland (S52R) mutant neuroserpin, mutant protein accumulates as PAS-positive inclusions within ER-localized structures in neurons and causes clinical symptoms reminiscent of human FENIB.[17]

These data collectively support a model in which **heterozygous SERPINI1 missense variants in critical structural regions of neuroserpin act as dominant toxic gain-of-function mutations**, promoting polymerization and ER retention that injure neurons, while simultaneously impairing neuroserpin’s normal inhibitory function on tPA and potentially other proteases.[4][9][13][17] The genetic etiology is therefore monogenic and highly penetrant, with autosomal dominant transmission in families and occasional sporadic cases arising from de novo variants.[5]

### 2.2 Genetic Risk Factors and Susceptibility Loci

Beyond the causal SERPINI1 missense variants described above, there is currently no robust evidence for additional susceptibility loci or modifier genes that substantially alter risk of developing FENIB. ClinVar records multiple missense variants of SERPINI1 with uncertain significance, with one review noting that ClinVar annotates 61 missense variations of SERPINI1, 14 classified as benign or likely benign, and 47 categorized as variants of uncertain significance.[13] Many of these variants have not been associated with a clinical phenotype, and whether some may confer a mild risk or subclinical polymerization tendency is unknown. The psychiatric case report’s variant p.Arg393Pro was initially classified as a variant of uncertain significance, but the authors interpreted it as causative in the context of the patient’s presentation and family history.[10]

No genome-wide association studies (GWAS) or polygenic risk scores are available for FENIB, a reflection of its extreme rarity and Mendelian character.[3][5] The disease is not associated with common susceptibility alleles in other dementia or epilepsy genes, and there is no evidence that polymorphisms in tPA, plasminogen or other components of the neuroserpin–tPA axis modulate risk in a clinically meaningful way. Thus, **genetic risk for FENIB is dominated by rare high-penetrance heterozygous SERPINI1 missense variants**, with negligible contribution from common variants at other loci, based on current knowledge.[1][3][5][8][9][13]

### 2.3 Environmental and Lifestyle Risk Factors

The available clinical and mechanistic literature does not identify specific environmental, occupational, or lifestyle exposures that causally increase the risk of FENIB. Orphanet and MedlinePlus emphasize that the condition is very rare, inherited in an autosomal dominant pattern, and caused by mutations in SERPINI1, without mention of environmental co-factors.[3][5] The reported families arise from diverse geographical and social backgrounds, including a large New York State family, an Oregon family, and other European kindreds, but there is no suggestion of shared environmental triggers.[2][7][8][10]

Some patients with FENIB, such as the woman with coexistent multiple sclerosis, have other neurological disorders, but these are interpreted as comorbid conditions rather than environmental causes of FENIB.[8] Likewise, the catatonia case report emphasizes neuropsychiatric features but does not implicate psychosocial stressors or substance exposures as etiologic agents.[10] General factors that influence risk of seizures and dementia in the broader population—such as head trauma, vascular risk factors, alcohol use and infections—have not been systematically studied with respect to FENIB, and their relevance likely lies in modulating clinical course rather than determining disease onset.

Therefore, **no specific environmental, lifestyle or toxic risk factors are currently recognized for FENIB**, and the condition is best classified etiologically as a primary genetic disorder driven by SERPINI1 mutations.[1][3][5]

### 2.4 Protective Factors and Gene–Environment Interactions

In the absence of large epidemiological studies or mechanistic investigations focused on modifiers, **protective factors** for FENIB remain largely speculative. There are no known genetic variants that confer protection against neuroserpin polymerization or ER retention, nor are there environmental exposures identified as protective. Some mechanistic work in serpinopathies suggests that enhanced autophagic or proteasomal clearance of polymers could mitigate toxicity, and differences in ER stress response capacity might modulate disease severity, but these concepts have not been directly tested in FENIB patients.[4][9][13][17][18]

Neuroserpin physiology studies indicate that the protein is involved in synaptic plasticity, emotional behaviour and neuronal survival, interacting with tPA and perhaps other proteases.[13][14][16] In mice lacking neuroserpin, behavioural abnormalities and altered synaptic morphology are observed, suggesting that both excess and deficiency of neuroserpin activity can be detrimental.[14][16] However, these findings do not directly translate to protective factors in FENIB, where the primary issue is toxic polymer accumulation.

Given that FENIB is a **monogenic, autosomal dominant disorder with rare occurrence**, meaningful gene–environment interaction data are not available. It is reasonable to hypothesize that environmental factors that increase neuronal stress, such as repeated seizures, metabolic insults or inflammatory episodes, could exacerbate neurodegeneration in individuals with SERPINI1 mutations, but this remains an inference rather than established evidence. Likewise, good seizure control and general neuroprotective measures might slow progression, but no studies have quantified such effects in FENIB patients.[5][8][10]

In sum, current knowledge does not support specific protective factors or defined gene–environment interactions in FENIB, and **the disease is best conceptualized as a genetically determined serpinopathy with relatively limited modulation by external factors**, despite likely individual variability in resilience and comorbid conditions.[1][3][4][5][8][9][13]

## 3. Phenotypes

### 3.1 Global Clinical Phenotype

Clinically, FENIB is characterized by a **constellation of neurological and neuropsychiatric manifestations** that evolve over years, with epilepsy and dementia as core features. Davis et al. describe the disease as presenting in the fifth decade with “an insidious onset of cognitive decline, impairment of attention and concentration, and perseveration, and loss of daily living skills exemplified by poor judgment and lack of insight,” with learning and memory affected but less than in Alzheimer disease.[2] OMIM emphasizes progressive epilepsy and dementia, with onset ranging from the second to fifth decades and variable severity.[1] Orphanet summarizes FENIB as progressive myoclonus epilepsy and/or presenile dementia with frontal-lobe features and relative sparing of recall memory, and notes that cerebellar symptoms and pyramidal signs may also be present.[3] MedlinePlus offers a detailed narrative of intellectual impairment, personality change, language difficulties, seizures with myoclonus and generalized convulsions, and difficulty regulating thoughts and speech.[5]

The clinical course is typically **progressive**, with gradual deterioration in cognitive function, increased seizure frequency, and accumulation of neurological deficits leading ultimately to severe disability and institutionalization in many cases.[1][2][3][5][10] Disease severity is highly variable, reflecting genotype–phenotype correlations and possibly other factors; some patients develop dementia in childhood or adolescence, while others have a later-onset cognitive decline beginning in mid- to late adulthood.[5][9][10][18] The psychiatric case report highlights that FENIB may present initially with catatonia and behavioural disturbances, underlining the breadth of neuropsychiatric phenotypes.[10]

From a human phenotype ontology perspective, key symptom and sign categories include **cognitive impairment**, **frontal lobe dysfunction**, **personality change**, **behavioural abnormalities**, **myoclonic seizures**, **generalized tonic–clonic seizures**, **tremor**, **dysarthria**, **cerebellar ataxia**, **pyramidal tract signs**, and **progressive dementia**.[1][2][3][5][8][10][18] These map to HPO terms such as “Cognitive impairment,” “Executive function deficit,” “Frontal lobe dysfunction,” “Personality changes,” “Behavioral abnormality,” “Myoclonus,” “Epileptic seizures,” “Tremor,” “Dysarthria,” “Cerebellar ataxia,” “Spasticity,” and “Dementia.” The impact on quality of life is profound: patients experience progressive loss of independence, difficulty maintaining employment or academic function, and ultimately require full-time care and management of seizures and other complications.[2][3][5][10]

### 3.2 Cognitive and Behavioural Phenotypes

The **cognitive phenotype** in FENIB is dominated by **frontal-executive dysfunction** and broader impairments of attention, concentration, language and insight. Davis et al. note that affected individuals show perseveration, poor judgment and lack of insight, with learning and memory affected but spared relative to Alzheimer disease, suggesting disproportionate frontal involvement.[2] Orphanet describes presenile dementia with prominent frontal-lobe features and relative sparing of recall memory.[3] MedlinePlus reports that first signs of intellectual impairment may be problems with attention and concentration, difficulty regulating thoughts or speech, and later personality changes, impaired judgment, insight and memory.[5] The psychiatric case of FENIB presenting as catatonia underscores that behavioural and psychomotor abnormalities can be marked, with symptoms such as apathy, despair, hostility and psychomotor disturbances.[10]

These cognitive and behavioural changes align with HPO terms like “Executive function deficit,” “Attention deficit,” “Impaired concentration,” “Personality change,” “Apathy,” “Disinhibition,” and “Psychomotor retardation.” They also have severe impact on quality of life, impairing occupational functioning, social relationships and self-care. MedlinePlus notes that people with FENIB develop difficulty with daily living skills and have trouble regulating their thoughts or speech, leading to loss of independence.[5] Orphanet emphasizes that presenile dementia with frontal features compromises functioning even while recall memory is relatively preserved.[3]

The **age of onset** of cognitive symptoms varies widely. In severe cases, dementia can appear in childhood or adolescence and is often the first sign of FENIB, whereas less severe cases show progressive decline beginning in mid- to late adulthood.[3][5][9][10] Severity ranges from mild early executive dysfunction to profound global dementia leading to institutionalization, with progression generally relentless over years.[1][2][3][5] Frequency of cognitive involvement among affected individuals appears high; virtually all described patients eventually develop significant intellectual impairment, though precise percentages are not available due to small numbers.[1][2][3][5][8][10]

Quality of life impact is extensive. FENIB-related dementia leads to loss of decision-making capacity, safety awareness, and ability to manage finances, work, and relationships. Patients often require supervision and assistance with basic activities of daily living, and behavioural changes can produce caregiver burden and psychosocial stress.[2][5][10] These aspects would map to quality-of-life instruments like EQ-5D and SF-36 as profound impairments in mobility, self-care, usual activities, pain/discomfort (related to seizures and complications), and anxiety/depression.

### 3.3 Seizures and Epileptic Phenotypes

Epilepsy constitutes the second core phenotype in FENIB, often manifesting as **progressive myoclonus epilepsy** and other seizure types. Orphanet explicitly classifies FENIB as a serpinopathy characterized by progressive myoclonus epilepsy and/or presenile dementia.[3] MedlinePlus reports that people with FENIB have seizures involving sudden, involuntary muscle jerking or twitching (myoclonus), and that many also experience at least one other form of seizure, typically generalized seizures with loss of consciousness, muscle rigidity and convulsions.[5] In rare cases, status epilepticus—prolonged seizure activity lasting several minutes—occurs and may be fatal.[5] The psychiatric case review notes that when FENIB begins earlier in life, from the first to third decade, seizures may be the first manifestation, including progressive myoclonus epilepsy, and that seizures may be difficult to control with medication, with episodes of status epilepticus sometimes resulting in death.[10]

OMIM highlights progressive epilepsy and dementia as hallmarks, and case reports describe focal or generalized seizures, dysarthria and tremors in addition to myoclonus.[1][2][8] Neuroserpin encephalopathy case literature mentions clinical manifestations including progressive myoclonus epilepsy (PME), focal or generalized seizures, dysarthria, tremors and dementia.[8] KEGG categorizes FENIB under genetic syndromes primarily expressed as epilepsy, reflecting the frequency and centrality of seizure disorders.[6][11]

Symptom onset for seizures can range from childhood to adulthood. In early-onset forms, myoclonic epilepsy may begin in the first or second decade, followed by rapid deterioration in neurological function.[3][5][10][18] In later-onset disease, seizures may accompany or follow cognitive decline. Severity and progression are generally **progressive**, with increasing frequency and refractoriness to antiepileptic drugs in many patients.[5][10] MedlinePlus explicitly states that in most people with FENIB, anti-seizure medications are not effective, indicating pharmacoresistant epilepsy.[5]

Quality of life impact is substantial. Myoclonus and generalized seizures interfere with daily activities, pose risk of injury, limit driving and employment, and contribute to social isolation and psychological distress.[5][8][10] Status epilepticus is a medical emergency and a cause of mortality. FENIB-related epilepsy corresponds to HPO terms “Myoclonus,” “Generalized tonic-clonic seizures,” “Status epilepticus,” and “Progressive myoclonus epilepsy,” and NCIT terms for clinical interventions would include antiepileptic drug therapy, ketogenic diet (in broader PME contexts), and seizure monitoring.

### 3.4 Motor, Cerebellar and Pyramidal Signs

Beyond seizures, FENIB may present with **motor symptoms** including tremor, dysarthria, cerebellar ataxia and pyramidal tract signs. Orphanet notes that “other neurological manifestations like cerebellar symptoms and pyramidal signs may be present.”[3] The neuroserpin encephalopathy case report describes clinical manifestations such as dysarthria, tremors and dementia, in addition to progressive myoclonus epilepsy.[8] Davis et al. report tremor, and other case descriptions mention gait abnormalities and increased tone consistent with pyramidal involvement.[2][8][10] These features likely reflect involvement of corticospinal tracts, cerebellar pathways and basal ganglia by neuroserpin inclusion pathology.[2][3][8][18]

Symptom onset for motor signs often follows or coincides with seizures and cognitive decline, but may be present earlier in some cases. Severity ranges from mild tremor and dysarthria to disabling ataxia and spasticity. Progression appears gradual but inexorable, contributing to falls, dysphagia and weight loss.[3][5][8][10] Frequency among affected individuals is less clearly defined than seizures and dementia, but cerebellar and pyramidal signs are recurrently mentioned in case series and Orphanet’s summary, suggesting they are common but not universal.[3][8][10][18]

Quality of life is further compromised by these motor manifestations. Dysarthria impairs communication, ataxia leads to falls and loss of ambulation, and pyramidal signs may require assistive devices and physical therapy. HPO terms such as “Tremor,” “Dysarthria,” “Cerebellar ataxia,” “Spasticity,” and “Pyramidal signs” are appropriate phenotype descriptors.

### 3.5 Systemic and Laboratory Phenotypes

FENIB is primarily a central nervous system disorder, and **systemic or laboratory abnormalities** are relatively limited. No characteristic peripheral blood biomarkers or metabolic derangements have been reported in the clinical summaries. MedlinePlus and OMIM focus on neurological features without referencing systemic organ involvement.[1][5] However, causes of death in people with FENIB include status epilepticus and pneumonia, suggesting increased risk of aspiration, respiratory compromise and infections secondary to neurological disability.[5][10]

Neuroimaging findings are not extensively detailed in the provided sources, but given the frontal-lobe cognitive phenotype, one might anticipate frontal cortical and subcortical atrophy on MRI in advanced stages. Histopathologically, the key laboratory phenotypes are the presence of Collins bodies—round, eosinophilic, PAS-positive, diastase-resistant neuronal inclusion bodies distributed in deeper layers of the cerebral cortex and in many subcortical nuclei, especially the substantia nigra.[1][2][9][17][18] Biochemical analysis shows that Collins bodies consist exclusively of neuroserpin, and electron microscopy reveals entangled fibrils and bead-like polymers localized in the ER.[2][9][17][18]

Suggested HPO laboratory-related terms include “Abnormal neuronal inclusions,” “PAS-positive staining of inclusions,” and “Endoplasmic reticulum storage disease,” capturing the histological and subcellular phenotype. Pathology and imaging phenotypes will be elaborated further in the diagnostics section.

### 3.6 Phenotype Progression and Impact

In virtually all documented cases, **FENIB follows a progressive course**. Davis et al. describe affected individuals who eventually require institutionalization, and OMIM notes progressive epilepsy and dementia ending in institutionalization.[1][2] MedlinePlus reports that people with FENIB have a shortened life expectancy, and that earlier onset of signs and symptoms is associated with greater impact on life expectancy.[5] The psychiatric case report emphasizes that early-onset disease with seizures and rapid progression may lead to death from status epilepticus.[10] Transgenic mouse models show that accumulation of mutant neuroserpin precedes development of clinical symptoms and increases over time, supporting a gradual, cumulative pathophysiology.[17]

Quality of life impact across phenotypes is therefore extremely high. Cognitive decline, seizures, motor dysfunction and behavioural changes collectively result in profound disability, caregiver burden and reduced survival. No spontaneous remissions or stable courses have been described; progression appears steady, though rate may vary between patients and mutations.[3][5][9][10][18] HPO terms such as “Progressive neurologic deterioration” and “Neurodegeneration” are apt overarching descriptors.

## 4. Genetic and Molecular Information

### 4.1 SERPINI1 Gene and Neuroserpin Protein

**SERPINI1** (HGNC: 8870), also known as *PI12*, encodes **neuroserpin**, a member of the serpin superfamily of serine protease inhibitors.[1][8][12][13] The gene is located on chromosome 3q26.1, and its protein product is primarily expressed in neurons of the central nervous system and peripheral nervous system.[1][9][12][13] MedlinePlus Genetics explains that the SERPINI1 gene provides instructions for making neuroserpin, which inhibits the activity of tissue plasminogen activator (tPA), thereby participating in cell migration, blood clotting, inflammation and, crucially, the development and function of the nervous system.[12][15] Neuroserpin helps neurons divide and mature (differentiation) and plays a role in the development of synapses, where cell-to-cell communication occurs.[12][15]

Structurally, neuroserpin conforms to the canonical **serpin fold**, consisting of three β-sheets and nine α-helices, with a mobile reactive center loop (RCL) that inserts into β-sheet A upon protease binding, forming a covalent complex and inactivating the protease.[13][14] Serpins utilize a metastable native conformation that is susceptible to conformational rearrangements, which renders them functionally versatile but also vulnerable to misfolding and polymerization when destabilized by mutations.[13][14][18] Neuroserpin’s target protease in the nervous system is tPA, a serine protease involved in fibrinolysis but also expressed in the CNS, where it participates in neuronal migration, axonal growth, synaptic plasticity and neurovascular responses.[13][14][16] Neuroserpin and tPA share overlapping expression patterns in developing and adult brain, suggesting tight regulation of extracellular proteolytic activity.[13][14][16]

Physiologically, neuroserpin has been implicated in **axonogenesis, synaptogenesis, synaptic plasticity and emotional behaviour**. Knockout mice lacking neuroserpin show reduced locomotor activity in novel environments, anxiety-like responses, neophobia, decreased spine-synapse density, altered expression of postsynaptic proteins and deficits in hippocampal-dependent cognitive and social functions.[14][16] Overexpression of neuroserpin in cultured neurons alters dendritic spine number and shape, and neuroserpin manipulation in PC12 cells affects cell-cell adhesion via N-cadherin.[14][16] These observations underscore neuroserpin’s roles beyond protease inhibition, possibly involving direct interactions with adhesion molecules and signaling pathways.[13][14][16]

From a Gene Ontology perspective, neuroserpin is associated with biological processes such as “regulation of proteolysis,” “regulation of synaptic plasticity,” “axon development,” and “regulation of emotional behavior,” and with molecular functions like “serine-type endopeptidase inhibitor activity” and “tissue plasminogen activator inhibitor activity.”[13][14][16] Cellular component GO terms include “extracellular space,” “synapse,” and “endoplasmic reticulum lumen,” reflecting its secreted nature and the ER localization of mutant polymers in FENIB.[9][13][14][17]

### 4.2 Pathogenic Variants and Genotype–Phenotype Correlation

At least six pathogenic missense variants in SERPINI1 have been associated with FENIB, all of which destabilize neuroserpin and promote polymerization. The earliest identified were **S49P (Syracuse)** and **S52R (Portland)**, located in the N-terminal shutter region and discovered in the New York and Oregon families.[1][2][7][9][18] Miranda et al. report that four mutations—S49P, S52R, H338R, G392E—cause FENIB, and all affect the stability of the shutter region.[9] The neuroserpin encephalopathy case report adds **G392R** as a fifth previously described mutation before introducing their novel variant.[8] The recent catatonia-associated case describes **R393P**, again in the C-terminal segment adjacent to G392, consistent with a cluster of pathogenic residues in this region.[10]

Biochemical studies show that S49P and S52R neuroserpin have **strongly reduced ability to inhibit tPA and a high tendency to form polymers**. In vitro expression and purification of these variants demonstrate that they polymerize readily and are unstable in solution, limiting detailed characterization.[4][13] S49P neuroserpin polymerizes faster than wild-type and forms bead-like polymers and entangled aggregates identical in morphology to Z alpha1-antitrypsin mutants, suggesting a shared mechanism across serpinopathies.[18] Miranda et al. show that all four mutations lead to polymerization of neuroserpin and slow trafficking of the mutant protein from the ER, resulting in polymer accumulation in the ER lumen.[9] They also report a striking correlation between the predicted molecular instability of each mutant, the number of neuroserpin inclusions in patient brains and the inverse age of onset of dementia.[9]

Transgenic mouse models corroborate this genotype–phenotype correlation. Mice expressing Portland (S52R) mutant neuroserpin display more severe clinical symptoms and harbor more neuroserpin deposits than Syracuse (S49P) mice, confirming that structural instability correlates with disease severity.[17] Accumulation of mutant neuroserpin precedes development of clinical symptoms, leading to a subclinical phase in which polymers accumulate silently.[17] Pathology sources emphasize that FENIB shows a clear genotype–phenotype correlation, with severity of disease correlating closely with the propensity of mutated neuroserpin to form polymers, and that intracellular protein aggregation alone can be sufficient to cause neurodegeneration.[18]

Variant classification in ClinVar and other clinical databases assigns pathogenic or likely pathogenic status to these missense variants based on segregation data, functional studies and structural modeling.[9][13][18] Population allele frequencies in gnomAD and similar databases are extremely low, consistent with high penetrance and severe phenotype; however, detailed numeric data are not provided in the summarizing resources. All causal variants are **germline heterozygous mutations**, consistent with autosomal dominant inheritance; somatic mutations in SERPINI1 have not been implicated in FENIB or other neurodegenerative diseases in the current literature.[1][3][5][8][9][10]

Functionally, these variants induce a **toxic gain-of-function** mediated by polymerization and ER retention, combined with a partial **loss-of-function** in tPA inhibition. ER retention leads to stress responses and potential activation of the unfolded protein response, whereas reduced secretion and inhibitory capacity of neuroserpin may permit excessive tPA activity, contributing to synaptic dysregulation and increased neuronal excitability.[4][9][12][13][15][16]

### 4.3 Modifier Genes, Epigenetic Factors and Chromosomal Abnormalities

To date, no **modifier genes** have been convincingly shown to alter the severity or expression of FENIB. While differences in ER stress pathways, autophagic capacity and neuroinflammatory responses likely modulate neuronal resilience, specific genetic variants in these pathways have not been linked to clinical variability in FENIB patients.[4][9][13][17][18] Epigenetic changes such as DNA methylation or histone modifications affecting SERPINI1 expression have not been explored in the context of FENIB, and no epigenomic studies have been reported that directly relate chromatin changes to disease.

Similarly, **chromosomal abnormalities** have not been associated with FENIB. The disorder is caused by point mutations in SERPINI1 rather than large-scale deletions, duplications or translocations, and no syndromic cases with additional chromosomal anomalies have been reported.[1][3][5][8][10] This contrasts with some other Mendelian epilepsies and dementias where copy number variants play a significant role.

Thus, the genetic and molecular information on FENIB centers on **SERPINI1 missense variants and neuroserpin protein dysfunction**, without known involvement of modifier genes, epigenetics or chromosomal structural variants, reflecting the monogenic, point-mutation nature of the disease.[1][4][8][9][13][18]

## 5. Environmental Information

### 5.1 Environmental and Lifestyle Factors

As noted in the etiology section, **no specific environmental factors** have been implicated in causing or substantially modifying FENIB. Orphanet and MedlinePlus frame the disease as a hereditary, autosomal dominant condition due to SERPINI1 mutations, and do not mention environmental triggers.[3][5] Case reports and family studies describe affected individuals from diverse backgrounds without shared occupational or toxic exposures that would suggest a common environmental agent.[2][7][8][10]

Lifestyle factors such as smoking, diet, exercise and alcohol use have not been systematically evaluated in FENIB patients. Given the disease’s rarity, it would be difficult to design studies capable of detecting modest lifestyle effects. Clinically, general health recommendations appropriate for epilepsy and dementia—such as minimizing sleep deprivation, avoiding neurotoxic substances, and maintaining vascular health—are applied, but these are extrapolated from broader neurological practice rather than specific evidence in FENIB.[5][10]

### 5.2 Infectious Agents and Other Non-genetic Contributors

No **infectious agents** are known to cause FENIB or trigger its onset. The disorder’s defining features—autosomal dominant inheritance, SERPINI1 missense variants, neuroserpin polymerization—point strongly to a primary genetic etiology.[1][2][4][9][18] Patients may suffer infections such as pneumonia as complications of advanced neurological disability and aspiration, but these are sequelae rather than causes.[5][10]

Other non-genetic factors, such as head trauma or systemic diseases, might influence the clinical course, but there is no evidence that they initiate FENIB. The case with coexistent multiple sclerosis demonstrates that additional neuropathology can coexist, complicating the clinical picture and potentially exacerbating disability, but the authors treat FENIB and multiple sclerosis as distinct conditions.[8]

In summary, **environmental, lifestyle and infectious factors play at most a secondary role in FENIB**, and the disease is best conceptualized as a purely genetic serpinopathy of the nervous system.[1][3][4][5][8][9][13]

## 6. Mechanism and Pathophysiology

### 6.1 Causal Chain from Mutation to Clinical Phenotype

The pathophysiology of FENIB can be summarized as a series of mechanistic steps linking SERPINI1 missense variants to neuroserpin polymerization, ER stress, neuronal dysfunction and the clinical manifestations of epilepsy and dementia. The ordered causal chain below is derived from human neuropathological studies, in vitro biochemistry, cell biology experiments and transgenic animal models, with some links inferred based on general serpin biology and ER stress pathways.[4][9][13][17][18]

| Step | Mechanistic link |
|------|------------------|
| 1 | Heterozygous missense variants in SERPINI1 (e.g. S49P, S52R, H338R, G392E, G392R, R393P) lead to structural destabilization of neuroserpin’s shutter region and reactive center loop, predisposing the protein to misfolding and polymerization.[1][2][4][8][9][13][18] |
| 2 | Destabilized neuroserpin undergoes aberrant intermolecular linkage in the endoplasmic reticulum lumen, resulting in the formation of ordered polymers and aggregates, rather than proper folding and secretion as monomers.[4][9][13][17][18] |
| 3 | Accumulation of polymeric neuroserpin within the ER of cortical and subcortical neurons leads to retention of the protein, formation of PAS-positive, diastase-resistant Collins bodies, and activation of ER stress and unfolded protein response pathways, eventually resulting in neuronal dysfunction and cell death.[2][4][9][17][18] |
| 4 | Reduced secretion of functional neuroserpin into the extracellular space leads to diminished inhibition of tPA and possibly other proteases, resulting in increased extracellular proteolytic activity that may alter synaptic plasticity, dendritic spine morphology, and neuronal excitability.[12][13][14][16] |
| 5 | Combined toxic gain-of-function (ER-retained polymers causing stress and degeneration) and loss-of-function (impaired tPA inhibition leading to excessive protease activity) effects disrupt neuronal circuits in frontal cortex, hippocampus, basal ganglia and cerebellum, leading to progressive cognitive decline, frontal-executive dysfunction and motor abnormalities.[2][3][4][9][13][14][17][18] |
| 6 | Enhanced neuronal excitability and disrupted inhibitory–excitatory balance in cortical and subcortical epileptogenic networks, possibly mediated by altered calcium homeostasis, ER stress signaling and tPA-dependent plasticity changes, result in myoclonic and generalized seizures that are often pharmacoresistant.[4][5][10][13][16] |
| 7 | Progressive neuronal loss in affected regions, accumulation of Collins bodies, and ongoing network dysfunction culminate in presenile dementia, motor impairment, seizures and death, with disease severity and age of onset inversely correlated with the polymerization propensity and instability of the specific neuroserpin mutation.[1][2][4][9][17][18] |

In the following subsections, each element of this causal chain is elaborated, with attention to molecular pathways, cellular processes, protein dysfunction, tissue damage mechanisms, and the involvement of specific cell types and anatomical structures.

### 6.2 Serpin Folding, Shutter Region and Polymerization

Serpins are unique among protease inhibitors in that they utilize a **metastable native conformation** to trap target proteases in a covalent complex. The reactive center loop (RCL) swings into β-sheet A, dragging the protease and distorting its active site, thereby inactivating it.[13][14] This conformational flexibility, while central to serpin function, renders serpin proteins exceptionally prone to misfolding and polymerization when destabilized by point mutations. Neuroserpin, like other serpins, contains a **shutter region** that regulates opening of β-sheet A and RCL insertion. Mutations in this region can alter the energy landscape of folding and favor formation of **polymeric chains** rather than properly folded monomers.[4][9][13][18]

In FENIB, pathogenic mutations such as S49P and S52R lie in this shutter region and have been shown to drastically reduce neuroserpin’s stability and increase its polymerization rate.[4][9][13][18] Structural modeling and biochemical assays reveal that these mutations weaken specific hydrogen bonds and packing interactions, allowing aberrant loop-sheet insertions between serpin molecules and producing linear or cyclic polymers.[4][13][18] Miranda et al. demonstrated that all four studied mutations (S49P, S52R, H338R, G392E) induce neuroserpin polymerization in vitro and in transfected cells, and that the rate of polymer formation correlates with clinical severity.[9] Humpath pathology images show bead-like neuroserpin polymers in Collins bodies that are identical to those formed by Z alpha1-antitrypsin mutants, underscoring a shared structural mechanism among serpinopathies.[18]

Polymer formation occurs **within the ER lumen**, where newly synthesized neuroserpin folds before secretion. Mutant neuroserpin fails to achieve a stable monomeric state and instead forms **entangled polymeric aggregates** that are retained in the ER.[9][17][18] Electron microscopy in human FENIB brains and transgenic mouse models reveals endoplasmic aggregates of abnormal neuroserpin, confirming that Collins bodies represent ER-localized polymer deposits.[9][17][18] The cellular process underlying this is misfolding and aggregation, a type of protein quality control failure captured by GO terms such as “protein folding,” “protein polymerization,” “response to unfolded protein,” and “ER-associated degradation.”

### 6.3 ER Retention, Stress and Neuronal Cell Death

The retention of neuroserpin polymers in the ER lumen triggers **ER stress** and activates the **unfolded protein response (UPR)**, a homeostatic signaling pathway designed to restore protein folding capacity or, failing that, induce apoptosis.[4][9][13][15][17][18] In FENIB, polymer accumulation slows trafficking of neuroserpin from the ER, as shown in cell culture experiments, and leads to the formation of large intraneuronal inclusions long before clinical symptoms appear.[9][17] Transgenic mice expressing Syracuse and Portland mutant neuroserpin accumulate PAS-positive inclusion bodies in neurons that immunoreact with anti-neuroserpin antibody, and these inclusions are localized in the ER by electron microscopy.[17] The magnitude of ER accumulation is directly related to disease severity, as more unstable mutants such as Portland (S52R) produce more inclusions and earlier onset clinical symptoms.[17][18]

MedlinePlus and its SERPINI1 gene fact sheet state that neuroserpin polymers form inclusion bodies within the ER, and that the formation of neuroserpin polymers triggers a stress response in the ER that is communicated to other cell structures and ultimately leads to cell death.[5][12][15] It also notes that the gradual loss of neurons in certain parts of the brain causes progressive dementia and other features of FENIB, and that larger numbers of inclusion bodies cause more severe neurological problems.[5][12][15] These statements align with the mechanistic concept of ER stress–mediated neurodegeneration: chronic ER stress activates pathways such as PERK, IRE1 and ATF6, leading to translational attenuation, induction of chaperones, and, if unresolved, activation of pro-apoptotic signals like CHOP and JNK.[4][13][18] In FENIB, persistent ER stress likely overwhelms compensatory mechanisms, resulting in neuronal apoptosis or necrosis.

Cell types involved include **cortical pyramidal neurons**, **subcortical neurons in the substantia nigra**, and other nuclei where Collins bodies are abundant.[1][2][9][17][18] GO biological processes such as “endoplasmic reticulum stress response,” “apoptotic process,” and “neuron death” and Cell Ontology terms like “cortical pyramidal neuron” and “midbrain dopaminergic neuron” (for substantia nigra involvement) are appropriate descriptors.[1][2][9][17][18] Tissue damage mechanisms include **intracellular protein aggregation**, **oxidative stress**, **disrupted calcium homeostasis**, and **activation of intrinsic apoptotic pathways**, though detailed signaling intermediates remain to be fully elucidated in FENIB specifically.[4][9][13][18]

### 6.4 Loss of Neuroserpin Function and tPA Dysregulation

Concomitant with the toxic gain-of-function of polymer accumulation is a **loss-of-function** of neuroserpin’s normal inhibitory activity on tPA. Mutant neuroserpin is largely retained in the ER and is unstable, leading to reduced secretion of functional protein into the extracellular space.[4][9][12][13][15] Biochemical studies of S49P and S52R neuroserpin variants show a strongly reduced ability to inhibit tPA, and their instability prevents formation of normal complexes.[4][13] MedlinePlus SERPINI1 gene notes that gene variants reduce or eliminate neuroserpin’s ability to inhibit tPA, and that researchers believe unchecked tPA activity may also contribute to FENIB signs and symptoms.[12][15]

tPA is highly expressed in the CNS, with roles in fibrinolysis, neuronal migration, axonal growth, synaptic plasticity and neurovascular responses.[14][16] tPA knockout mice exhibit deficits in hippocampal long-term potentiation (LTP) and striatal synaptic plasticity, while exogenous tPA or overexpression enhances LTP.[16] During visual cortex development, experience-dependent plasticity and dendritic spine pruning are reduced in tPA-knockout mice and partly restored by exogenous tPA.[16] The main inhibitor of tPA in the vascular space is PAI-1, but in the nervous system, neuroserpin is the predominant inhibitor regulating neuronal tPA activity.[16] Neuroserpin overexpression reduces tPA activity and blocks tPA-dependent visual cortical plasticity and cell proliferation in vitro, whereas neuroserpin-knockout mice exhibit increased tPA activity and altered behaviour.[14][16]

In FENIB, reduced neuroserpin secretion likely results in **excess tPA activity at synapses**, which may have complex effects. On one hand, increased tPA could enhance synaptic plasticity and excitability, possibly contributing to epilepsy and seizures. On the other hand, tPA can promote excitotoxicity and neurotoxicity, particularly in ischemic contexts, via plasmin generation, matrix metalloproteinase activation and blood–brain barrier disruption.[14][16] MedlinePlus suggests that formation of neuroserpin polymers likely increases release of calcium ions into cells, leading to hyperactive neurons and seizure-associated abnormal brain activity.[5] This may involve tPA-mediated modulation of NMDA receptor function or other calcium-permeable channels, though this link is inferred from tPA biology rather than directly demonstrated in FENIB.[14][16]

GO terms capturing these processes include “regulation of synaptic plasticity,” “regulation of excitatory postsynaptic potential,” “negative regulation of proteolysis,” and “regulation of calcium ion homeostasis,” while Cell Ontology terms include “hippocampal neuron,” “cortical interneuron,” and “thalamocortical projection neuron,” representing circuits implicated in epilepsy and cognition.

### 6.5 Circuit-Level Dysfunction: Epilepsy and Dementia

The combined effects of ER stress–mediated neuronal loss and tPA dysregulation produce **circuit-level dysfunction** in brain regions underpinning cognition, behaviour and seizure generation. Collins bodies are found throughout the deeper layers of the cerebral cortex and in many subcortical nuclei, especially the substantia nigra.[1][2][9][17][18] This pattern suggests widespread involvement of association cortices, frontal executive networks, basal ganglia loops and motor pathways. Progressive loss and dysfunction of pyramidal neurons in frontal and temporal cortex likely underlie the frontal-predominant dementia phenotype: executive dysfunction, impaired attention and concentration, personality change and perseveration.[2][3][5]

Seizures and myoclonus presumably arise from **hyperexcitability of cortical and subcortical networks**, potentially involving motor cortex, supplementary motor area, thalamus and cerebellar circuits. Altered inhibitory/excitatory balance due to loss of interneurons, increased tPA activity and disrupted synaptic plasticity can lower seizure threshold, while ER stress and calcium dysregulation amplify excitotoxic cascades.[4][5][10][13][16] Progressive myoclonus epilepsy in FENIB resembles other PME syndromes such as Unverricht–Lundborg disease and Lafora disease, but mechanistically differs by involving serpin polymerization rather than storage of glycogen-like polyglucosans or cystatin B dysfunction.[3][5][8][10]

Motor symptoms such as tremor, dysarthria, cerebellar ataxia and pyramidal signs point to involvement of cerebellum, brainstem motor nuclei and corticospinal tracts, where neuroserpin inclusions have been observed.[3][8][18] The substantia nigra inclusion burden suggests potential dopaminergic dysfunction, though parkinsonian features are not prominently reported in the clinical summaries.[1][2][18]

Upstream mechanisms in this cascade include mutation-driven polymerization and ER retention, whereas downstream mechanisms encompass neuronal death, synaptic reorganization, altered network oscillations and clinical manifestations. The interplay between structural damage (neuron loss) and functional alterations (tPA-mediated plasticity changes, excitability) is complex and remains an active area of research.[4][9][13][14][16][17]

### 6.6 Molecular Profiling and Advanced Technologies

Although no large-scale transcriptomic, proteomic or metabolomic profiling studies have been published specifically for FENIB patients, related work on neuroserpin and serpinopathies offers insight into molecular changes. Transgenic mouse models overexpressing mutant neuroserpin have been utilized to examine gene expression changes associated with ER stress and neurodegeneration, though detailed datasets are not summarized in the provided sources.[17] Proteomic analyses of Collins bodies show that they consist exclusively of neuroserpin, with no major contamination by other proteins, emphasizing the specificity of polymer accumulation.[2][9][17]

Neuroserpin’s role in Alzheimer disease (AD) has attracted attention; neuroserpin was found in amyloid-β plaques and upregulated in AD brains, leading to the hypothesis that increased neuroserpin may reduce tPA activity, decrease plasmin-mediated Aβ clearance and contribute to synaptic alterations.[13][14] Conversely, neuroserpin-knockout mice crossed with human APP-J20 transgenic mice show rapid clearance of Aβ1–42 injected into frontal cortex, decreased amyloid peptide levels, reduced plaque numbers and size, increased tPA activity and rescue of spatial memory defects compared to J20 mice.[14] These findings illustrate broader neuroserpin–tPA–plasmin axis roles in neurodegeneration, though they pertain to AD rather than FENIB. They nonetheless suggest that FENIB’s loss of neuroserpin function could have distinct consequences in amyloid processing, although this has not been studied directly.

Advanced technologies such as **single-cell transcriptomics**, **spatial transcriptomics**, and **multi-omics integration** have not yet been applied to FENIB, likely due to the scarcity of human tissue and cases. Functional genomics screens (e.g. CRISPR, RNAi) targeting SERPINI1 or ER stress components could, in principle, reveal modifiers of neuroserpin polymer toxicity, but such studies are not reported in the current literature.[4][13][17]

In summary, molecular profiling of FENIB is currently limited to targeted analyses of neuroserpin polymers, ER stress markers and synaptic proteins in models, with no comprehensive omics datasets. Future application of multi-omics and advanced technologies to FENIB, even in animal models, could clarify downstream pathways and identify potential therapeutic targets.

## 7. Anatomical Structures Affected

### 7.1 Organ and System-Level Involvement

FENIB primarily affects the **central nervous system**, specifically the **brain**, and is categorized among diseases of the nervous system.[1][3][6][11] KEGG places FENIB under “Neurodegenerative disease” and “Epilepsy or seizures,” reflecting its neurodegenerative and epileptic nature.[6][11] The primary organs involved are the **cerebral cortex** and **subcortical nuclei**, including the **substantia nigra**, as highlighted by neuropathological descriptions.[1][2][9][17][18] These structures correspond to UBERON terms such as “cerebral cortex” (UBERON:0000956), “frontal lobe” (UBERON:0001870), “temporal lobe” (UBERON:0001871), and “substantia nigra” (UBERON:0002038), though specific ontology IDs are not listed in the sources.

Secondary organ involvement occurs through complications rather than direct pathology. For example, pneumonia is a documented cause of death in FENIB patients, likely due to aspiration and respiratory compromise resulting from seizures, dysphagia and immobility.[5] Thus, the **respiratory system** can be secondarily affected. Cardiovascular and endocrine systems are not prominently involved.

Body systems impacted include the **nervous system** (cognition, motor control, seizure generation), the **musculoskeletal system** (via spasticity and tremor affecting movement), and the **psychiatric/behavioural domain** (personality change, catatonia).[2][3][5][10][18] HPO and MeSH terms for “Central nervous system disease,” “Epilepsy,” “Dementia,” and “Movement disorders” appropriately classify FENIB.

### 7.2 Tissue and Cell-Level Targets

At the tissue level, FENIB primarily affects **nervous tissue**, comprising neurons and glial cells. Histopathological studies focus on **neurons**, as Collins bodies are described as **neuronal inclusions** distributed throughout the gray matter of the cerebral cortex and certain subcortical nuclei.[2][9][17][18] The deeper layers (e.g. layers V and VI) of the cortex are particularly affected, where large pyramidal neurons reside.[2][17][18] In the substantia nigra, inclusion bodies occur in dopaminergic neurons, though clinical parkinsonism is not emphasized.[1][2][18]

Cell Ontology terms describing affected cells include “cortical neuron,” “pyramidal neuron,” “substantia nigra dopaminergic neuron,” and possibly “cerebellar Purkinje cell” if cerebellar involvement is confirmed.[3][8][18] Although glial cells may respond to neuronal death and protein aggregation with activation and proliferation, specific glial pathology is not a defining feature in FENIB summaries.

At the cellular level, the critical compartment is the **endoplasmic reticulum**, where neuroserpin polymers accumulate. Electron microscopy shows endoplasmic aggregates of abnormal neuroserpin forming bead-like polymers identical to those seen in alpha1-antitrypsin deficiency.[9][17][18] The ER lumen is therefore the key subcellular site of pathology, corresponding to GO Cellular Component terms “endoplasmic reticulum lumen,” “endoplasmic reticulum,” and “intracellular lumen.” Collins bodies appear as round inclusions within neuronal cytoplasm on light microscopy, but ultrastructurally they represent expanded ER cisternae filled with polymers.[2][9][17][18]

### 7.3 Localization and Distribution of Inclusions

Collins bodies are described as **round, 5 to 50 μm in diameter, eosinophilic, PAS-positive and diastase-resistant** neuronal inclusion bodies distributed throughout the deeper layers of the cerebral cortex and many subcortical nuclei, especially the substantia nigra.[1][2][9][17][18] The inclusions can be numerous and arranged in grape-like clusters within affected neurons in transgenic mouse models, mirroring human pathology.[17] They are strongly labeled by anti-neuroserpin antibodies, confirming their composition.[2][9][17][18]

The distribution of inclusions suggests widespread involvement of **bilateral cortical and subcortical structures**, without clear lateralization. Davis et al. describe inclusions throughout gray matter of cerebral cortex and in certain subcortical nuclei, implying diffuse rather than unilateral pathology.[2] Orphanet mentions frontal-lobe features but does not specify lateralization.[3] The anatomical localization correlates with prominent frontal-executive cognitive deficits, motor symptoms and seizures, reflecting involvement of frontal, motor and association cortices and their connected nuclei.[2][3][5][8][18]

Subcellular GO terms like “cytoplasmic vesicle,” “inclusion body,” and “endoplasmic reticulum lumen” capture the localization of Collins bodies, while pathology ontologies would classify them as “neuronal cytoplasmic inclusions” and “serpin inclusion bodies.”

## 8. Temporal Development

### 8.1 Age of Onset and Patterns of Onset

FENIB demonstrates **remarkable variability in age of onset**, ranging from childhood to late adulthood, with a clear correlation to the underlying SERPINI1 mutation. OMIM notes that onset ranges from the second to fifth decades of life, and that severity is variable.[1] Orphanet states that age of onset is variable, and that the disease has been reported in children as well as elderly patients.[3] MedlinePlus adds that signs and symptoms can appear at any age; in severe cases, dementia can appear in childhood or adolescence and may be the first sign, whereas less severe cases show progressive decline beginning in mid- to late adulthood.[5]

The psychiatric case report emphasizes that in early-onset illness (first to third decade), seizures may be the first manifestation, including progressive myoclonus epilepsy, and that disease may progress quite rapidly.[10] Transgenic mouse models demonstrate that mutant neuroserpin accumulation begins early in life and precedes clinical symptoms, suggesting a **subclinical phase** in which polymers accumulate without overt manifestations until a threshold of neuronal dysfunction is reached.[17]

Onset patterns are typically **insidious and chronic**, particularly for cognitive symptoms. Davis et al. describe an insidious onset of cognitive decline in the fifth decade.[2] Seizure onset may be more abrupt, with people experiencing sudden myoclonic jerks or generalized convulsions; however, these seizures often emerge against a background of underlying neuronal network changes that have been developing gradually.[5][10] There are no reports of truly acute presentations, and FENIB is not congenital in the sense of manifesting at birth, though underlying mutations are present from conception.

### 8.2 Disease Progression, Rate and Course

The **progression of FENIB** is generally **slow but relentless**. Over years, patients move from mild cognitive and seizure symptoms to severe dementia, refractory epilepsy, motor disability and institutionalization.[1][2][3][5][10] Miranda et al. note an inverse correlation between predicted molecular instability of neuroserpin mutants and age of onset, implying that more unstable mutants not only cause earlier onset but may also lead to faster progression.[9] Mouse models show that neuroserpin accumulation increases with age, and more polymerogenic mutants produce larger inclusion burdens and more severe clinical phenotypes.[17]

MedlinePlus states that people with FENIB have a shortened life expectancy, and that earlier onset signs and symptoms have greater impact on life expectancy.[5] The psychiatric case report emphasizes rapid progression in early-onset FENIB, with difficult-to-control seizures, status epilepticus and possible death within a relatively short time frame.[10] Orphanet and OMIM describe presenile dementia and progressive myoclonus epilepsy, implying a chronic, progressive course rather than episodic or relapsing-remitting patterns.[1][3] There is no evidence of spontaneous remission or stable disease phases; although symptom progression rate may vary, the overall trajectory is toward worsening.

From a staging perspective, one might conceptualize FENIB as progressing through **early**, **intermediate** and **advanced** stages. Early stages feature subtle cognitive and behavioural changes and occasional seizures. Intermediate stages show more frequent seizures, noticeable dementia, and motor signs. Advanced stages present with severe dementia, refractory epilepsy, profound motor disability and frequent complications such as aspiration pneumonia.[2][3][5][8][10] However, no formal staging system has been proposed in the literature.

### 8.3 Critical Periods and Windows of Intervention

The **critical periods** in FENIB relate to the onset of seizures, emergence of cognitive deficits and the accumulation of neuroserpin polymers. In early-onset disease, the first to third decades represent a high-risk window in which seizures may begin and rapid progression may occur.[5][10][17] In later-onset cases, the fifth and sixth decades mark the typical onset of dementia and functional decline.[1][2][3][5] From a mechanistic standpoint, polymer accumulation begins earlier, and there may be a window in which **interventions targeting ER stress or polymer clearance** could hypothetically delay onset or slow progression, as suggested by the time-dependent accumulation observed in mouse models.[17]

Clinically, early recognition of FENIB—particularly in families with known SERPINI1 mutations—could allow **proactive seizure management**, supportive cognitive interventions and genetic counseling. However, given the lack of disease-modifying therapies, the potential for early intervention to alter outcomes is currently limited. Critical periods are more relevant for anticipatory guidance and management planning than for curative treatment.

## 9. Inheritance and Population

### 9.1 Epidemiology: Prevalence and Incidence

FENIB is an **exceptionally rare disorder**. Orphanet estimates its prevalence as less than 1 per 1,000,000, categorizing it as a very rare disease.[3] MedlinePlus notes that FENIB appears to be very rare and states that the condition was first described in 1999 and that at least 13 affected individuals have been reported worldwide.[5] These numbers likely represent only published cases and may underestimate the true number, but they illustrate the scarcity of diagnosed patients.

Because of this rarity and the absence of dedicated registries, incidence data are not available. One might infer that FENIB accounts for an extremely small fraction of presenile dementia and progressive myoclonus epilepsy cases. Global burden of disease studies do not list FENIB separately, and national registries do not track it specifically.[3][5] Accordingly, FENIB carries negligible public health burden in terms of absolute numbers, but it is of high scientific interest due to its mechanistic insights into serpinopathies and neurodegeneration.

### 9.2 Inheritance Pattern, Penetrance and Expressivity

FENIB follows an **autosomal dominant inheritance pattern**. OMIM explicitly states that transmission patterns in reported families are consistent with autosomal dominant inheritance.[1] Davis et al. describe multigenerational pedigrees in New York and Oregon families in which dementia and epilepsy appear in each of several generations in both genders, consistent with autosomal dominant transmission.[2][7] Orphanet lists autosomal dominant inheritance and notes familial cases as well as sporadic cases resulting from de novo variants.[3] MedlinePlus explains that FENIB is inherited in an autosomal dominant pattern and that in some cases the condition is familial (variant inherited from one affected parent), while other cases are sporadic and result from new variants occurring in parental germ cells or early embryonic development.[5]

Penetrance appears to be **high**, as all documented carriers of pathogenic SERPINI1 missense variants in extended families develop clinical symptoms, though age of onset and severity vary according to the mutation.[1][2][9][18] However, given the small number of families, subclinical or non-penetrant cases cannot be excluded. Expressivity is clearly **variable**: some individuals develop early-onset seizures and rapidly progressive dementia, whereas others manifest later-onset cognitive decline with milder epilepsy.[3][5][8][9][10][18] Genotype–phenotype correlation studies indicate that expressivity is modulated by the specific mutation’s polymerization propensity, with S52R and G392E associated with more severe disease than S49P.[9][17][18]

There is no evidence for **genetic anticipation**, as pathogenic SERPINI1 variants are point mutations rather than repeat expansions, and disease severity does not systematically increase across generations beyond what would be expected from chance.[1][2][9] Germline mosaicism has not been reported, but cannot be excluded in sporadic cases where parents test negative.

Carrier frequency of pathogenic SERPINI1 variants in the general population is unknown but likely extremely low, given the disease’s rarity and severe phenotype. Population genetics databases like gnomAD may note occasional missense variants at SERPINI1, but these are mostly benign or of uncertain significance.[13] Consanguinity does not play a significant role, as the disease is autosomal dominant and arises from heterozygous variants.[3][5]

### 9.3 Population Demographics and Geographic Distribution

Affected populations described in the literature include families from **North America** (New York, Oregon), **Europe** and other regions, reflecting a **global distribution** without clear ethnic predilection.[2][7][8][10] Orphanet lists FENIB as a rare disease without specifying particular ethnic groups at higher risk.[3] MedlinePlus similarly does not mention population differences.[5]

Geographic distribution of specific variants has some clustering due to family origins. For example, the Syracuse (S49P) mutation was identified in a New York State family, and the Portland (S52R) mutation in an Oregon family.[2][7][9][17][18] Other mutations such as H338R and G392E have been reported in European families.[9][13] The catatonia-associated R393P variant arises in a patient whose geographic origin is not detailed in the snippet but likely adds to the spectrum.[10] No founder effects have been conclusively identified; that is, there is no evidence of a single ancestral mutation propagating widely in a specific population.

Sex ratio appears approximately **equal**, as both men and women are affected in reported families.[2][3][5][8][10] Age distribution spans adolescence to old age, with clustering of onset in early adulthood for severe mutations and midlife for milder ones.[3][5][9][10][17][18] Thus, FENIB affects both sexes across a broad age range, with mutation-dependent variation in onset.

## 10. Diagnostics

### 10.1 Clinical Evaluation and Diagnostic Criteria

Diagnosis of FENIB rests on **recognizing the characteristic clinical syndrome**, **identifying SERPINI1 mutations** and, when possible, **documenting Collins bodies in brain tissue**. Clinical evaluation involves detailed assessment of cognitive function, seizure types, motor signs and family history. The combination of progressive frontal-predominant dementia, progressive myoclonus epilepsy, tremor and other neurological signs in a multigenerational pattern should prompt consideration of FENIB, especially when other PME causes have been excluded.[2][3][5][8][10]

Standardized diagnostic criteria specific to FENIB have not been formally published, unlike for more common dementias and epilepsies. However, clinicians rely on criteria analogous to those used for other PMEs: progressive myoclonus, seizures, cognitive decline, and family history of similar symptoms. Differential diagnosis includes Unverricht–Lundborg disease, Lafora disease, neuronal ceroid lipofuscinoses, mitochondrial epilepsies and genetic frontotemporal dementias.[3][5][8][10] Distinguishing features of FENIB include the presence of Collins bodies on pathology and identification of SERPINI1 mutations.

ICD-11 categorization under 8A61.41 (“Genetic or presumed genetic syndromes primarily expressed as epilepsy”) provides a coding framework but does not define specific diagnostic criteria.[6][11] DSM-5 criteria for major neurocognitive disorder and epilepsy apply to the cognitive and seizure aspects but do not capture the underlying genetic and histopathological specificity.

### 10.2 Neuroimaging and Electrophysiology

Neuroimaging findings in FENIB are not comprehensively described in the provided sources, but general principles from dementia and PME suggest that MRI may show **cortical atrophy**, particularly in frontal and temporal lobes, and possible subcortical changes in later stages. Given the presence of neuroserpin inclusions in substantia nigra and other nuclei, one might also see signal changes or volume loss in basal ganglia and midbrain, though again this is inferred.[1][2][3][8][18]

EEG is important for characterizing seizures. In progressive myoclonus epilepsy, EEG often shows generalized spike–wave or polyspike–wave discharges, cortical myoclonic jerks, and background slowing with progression. MedlinePlus and the psychiatric case report mention seizures including myoclonus and generalized convulsions, but do not detail EEG findings.[5][10] Nevertheless, EEG is a key tool for documenting seizure type, frequency and pharmacoresistance. HPO terms like “Abnormal EEG” and “Generalized epileptiform discharges” would be relevant.

No specific functional imaging studies (e.g. FDG-PET, SPECT) are described, but such modalities could, in principle, show hypometabolism in frontal and temporal regions corresponding to cognitive deficits.

### 10.3 Histopathology and Collins Bodies

Histopathology provides a **definitive diagnostic signature** for FENIB. Davis et al. and subsequent studies describe **Collins bodies** as the key pathological finding: round, eosinophilic, PAS-positive, diastase-resistant neuronal inclusion bodies distributed throughout deeper cortical layers and subcortical nuclei such as substantia nigra.[1][2][9][17][18] Extensive histochemical, immunohistochemical and electron microscopic analyses show that these inclusions are distinct from any previously described, and biochemical analysis demonstrates that they consist predominantly or exclusively of neuroserpin.[2][9][17][18]

PAS staining reveals bright positivity indicating carbohydrate-rich or glycoprotein accumulations, and resistance to diastase digestion indicates that glycogen is not the primary component. Immunohistochemistry using affinity-purified anti-neuroserpin antibodies labels Collins bodies strongly, confirming their chemical composition.[2][9][17][18] Electron microscopy shows that inclusions are formed by entangled fibrils that immunogold-label for neuroserpin, and that they represent bead-like polymers and aggregates identical to those formed by alpha1-antitrypsin mutants.[9][17][18]

Pathology sources emphasize that Collins bodies are located within the **endoplasmic reticulum** of neurons, and that they appear as endoplasmic aggregates of abnormal proteins on electron microscopy.[9][17][18] Humpath notes that FENIB is an inclusion body dementia due to PI12 gene mutations and that Collins bodies bear a striking resemblance to inclusions of Z alpha1-antitrypsin in liver, reinforcing the serpinopathy concept.[18]

Because brain biopsy is invasive and not routinely performed in dementia or epilepsy, histopathology is most often obtained postmortem. However, in cases where neurosurgical tissue is available (e.g. temporal lobe resections for refractory epilepsy), identification of Collins bodies could support a diagnosis of FENIB when genetic testing is inconclusive.

### 10.4 Genetic Testing Strategies

Given the monogenic nature of FENIB, **genetic testing for SERPINI1 variants** is central to diagnosis. Single-gene sequencing of SERPINI1 (including all exons and exon–intron boundaries) can detect missense variants such as S49P, S52R, H338R, G392E, G392R and R393P.[1][8][9][10][13][18] The psychiatric case report describes whole-exome sequencing (WES) identifying a heterozygous variant of uncertain significance in SERPINI1 (c.1178G>C, p.Arg393Pro), illustrating the utility of WES in patients with unexplained young-onset dementia and seizures.[10] In such contexts, WES or whole-genome sequencing may reveal previously unrecognized SERPINI1 variants.

Gene panels for **progressive myoclonus epilepsy**, **early-onset dementia** or **serpinopathies** may include SERPINI1, although specific panel compositions are laboratory-dependent. The Genetic Testing Registry (GTR) likely lists tests targeting SERPINI1, but details are not provided in the sources. Chromosomal microarray (CMA), karyotyping and FISH are not useful for FENIB, as the disease arises from point mutations rather than copy-number or structural chromosomal changes.[1][3][5][8][10]

ClinVar and GeneReviews (not summarized here) provide variant-level information, including pathogenicity classifications and evidence. Interpretation of variants follows ACMG/AMP guidelines, integrating segregation, functional data and in silico predictions.[9][13][18] In sporadic cases, de novo variants must be considered, and parental testing helps clarify inheritance patterns.[5][10]

For asymptomatic relatives of affected individuals, targeted testing for the known family mutation enables cascade screening and informs genetic counseling. Prenatal or preimplantation genetic diagnosis is theoretically possible, given the autosomal dominant inheritance and severe phenotype, but no published cases have been reported.

### 10.5 Omics-Based Diagnostics and Biomarkers

At present, **omics-based diagnostics** such as RNA sequencing, proteomics, metabolomics and epigenomics are not standard for FENIB diagnosis. However, proteomic analysis of brain tissue could reveal neuroserpin polymer profiles, and metabolomic studies might detect signatures of ER stress or oxidative damage. No liquid biopsy biomarkers (e.g. circulating neuroserpin levels or polymer fragments) have been validated for clinical use.

MedlinePlus SERPINI1 fact sheets highlight that neuroserpin is secreted and acts extracellularly; theoretically, serum or CSF levels of neuroserpin and tPA could reflect disease state. Yet, in FENIB, mutant neuroserpin is retained in the ER, so circulating levels might be reduced or altered, but no clinical assays have been developed.[12][15] FDA biomarker databases do not list neuroserpin-based biomarkers for FENIB.

Thus, **genetic testing remains the primary diagnostic modality**, supplemented by clinical and pathological assessment. Omics technologies hold promise for research but are not currently used in routine diagnosis.

### 10.6 Differential Diagnosis and Screening

Differential diagnosis of FENIB includes other **progressive myoclonus epilepsies** (e.g. Unverricht–Lundborg disease, Lafora disease), **mitochondrial epilepsies**, **frontotemporal dementias**, **Alzheimer disease with seizures**, and **other inclusion body dementias** such as Lewy body dementia and frontotemporal lobar degeneration with TDP-43 or tau pathology.[3][5][8][10][18] Distinguishing features include FENIB’s specific histopathology of Collins bodies, SERPINI1 mutations, and the combination of frontal-predominant cognitive deficits with PME.

Screening for FENIB in asymptomatic individuals is not currently recommended at the population level, given its rarity. However, **cascade genetic screening** in families with known SERPINI1 mutations is appropriate, and **newborn screening** is not performed. Carrier screening in general populations is unnecessary due to low prevalence and autosomal dominant inheritance. Targeted screening of SERPINI1 in patients with unexplained PME and presenile dementia can be considered as part of comprehensive genetic evaluation.

## 11. Outcome and Prognosis

### 11.1 Survival, Mortality and Life Expectancy

FENIB is associated with **shortened life expectancy**. MedlinePlus states that people with FENIB have a shortened life expectancy and that earlier appearance of signs and symptoms is associated with greater impact on life expectancy.[5] Causes of death include status epilepticus—prolonged seizure activity that can cause brain damage and systemic complications—and pneumonia, often due to aspiration and immobilization.[5][10] The psychiatric case report highlights that early-onset FENIB with difficult-to-control seizures and status epilepticus may result in death, emphasizing the seriousness of the seizure phenotype.[10]

Exact survival rates (e.g. 5-year, 10-year survival) are not available because of the small number of cases and lack of longitudinal registries. However, the progression from onset to death appears to span several years to decades, depending on mutation and age of onset. Later-onset disease may allow survival into older age, albeit with significant disability, whereas childhood-onset disease may lead to death in young adulthood.[3][5][9][10][18]

Mortality is primarily **disease-specific**, attributable to seizures, neurodegeneration and complications of neurological disability rather than unrelated causes. The burden of morbidity and mortality is high for affected individuals but negligible at the population level due to rarity.

### 11.2 Morbidity, Disability and Quality of Life

Morbidity in FENIB is characterized by **progressive cognitive decline, refractory epilepsy, motor disability and behavioural disturbances**, leading to severe disability and dependency. Davis et al. and OMIM describe affected individuals becoming institutionalized due to dementia and seizures.[1][2] Orphanet notes that progressive myoclonus epilepsy and presenile dementia with frontal features cause significant impairment.[3] MedlinePlus details loss of intellectual functioning, personality changes, seizures and difficulties regulating thoughts and speech, all contributing to loss of daily living skills.[5]

Disability outcomes include loss of ability to work or study, inability to perform activities of daily living, requirement for 24-hour care, and increased risk of falls and injuries. Tremor, dysarthria and ataxia impair communication and mobility, adding to disability.[3][5][8][10][18] Psychiatric manifestations such as catatonia and mood changes can further impair functioning and complicate management.[10]

Quality of life is severely compromised in multiple domains. EQ-5D and SF-36 domains such as mobility, self-care, usual activities, pain/discomfort and anxiety/depression would be markedly affected. Caregivers experience substantial burden, and families face emotional distress and financial strain. No specific quality-of-life assessments have been reported in FENIB, but extrapolation from other PME and dementia conditions suggests profound impact.

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in FENIB include **SERPINI1 mutation type**, **age of onset**, and **seizure severity**. The genotype–phenotype correlation described by Miranda et al. shows that more unstable, polymerogenic neuroserpin mutations are associated with more numerous inclusions and earlier onset dementia, implying poorer prognosis.[9] Transgenic mouse studies confirm that mutants like Portland (S52R) produce more severe clinical symptoms than Syracuse (S49P).[17] Thus, **mutation-specific prognosis** is a reality in FENIB.

Age of onset also influences prognosis; childhood- or adolescent-onset cases with severe seizures tend to progress rapidly and have shorter survival, whereas later-onset cases may follow a more protracted course.[3][5][10][18] Seizure control is another prognostic factor; pharmacoresistant epilepsy with frequent status epilepticus episodes carries higher risk of mortality and additional brain damage.[5][8][10] Conversely, effective seizure management might improve survival and function.

Potential prognostic biomarkers include **neuroserpin inclusion burden** (quantified in pathology), **neuroserpin polymerization rate** (assessed in vitro for specific mutants), and **ER stress markers**. However, these are primarily research tools and not used clinically. There are no validated blood or CSF biomarkers that predict FENIB course.

## 12. Treatment

### 12.1 Current Pharmacological and Symptomatic Management

There is currently **no disease-modifying therapy** that reverses or halts neuroserpin polymerization or ER stress in FENIB. Treatment is primarily **symptomatic**, focusing on seizure control, cognitive and behavioural management, and supportive care. MedlinePlus notes that in most people with FENIB, anti-seizure medications are not effective, indicating that epilepsy is often pharmacoresistant.[5] The neuroserpin encephalopathy case report and psychiatric case describe use of standard antiepileptic drugs, but seizures remain difficult to control.[8][10]

Common antiepileptic medications used in PME, such as valproate, levetiracetam, clonazepam and topiramate, may be tried in FENIB, though no controlled trials exist. NCIT clinical intervention terms like “Anticonvulsant therapy” and “Epilepsy management” apply. In some PME syndromes, the ketogenic diet and vagus nerve stimulation are used; whether these strategies benefit FENIB is unknown but could be considered on a case-by-case basis.

Cognitive symptoms are managed similarly to other dementias, with cholinesterase inhibitors or memantine in some cases, though their efficacy in FENIB is not documented. Behavioural disturbances such as agitation, depression, psychosis or catatonia may be treated with psychotropic medications, including antipsychotics, antidepressants and benzodiazepines, as illustrated in the psychiatric case report.[10] Care must be taken to avoid drugs that lower seizure threshold.

### 12.2 Advanced and Experimental Therapeutics

Given the unique mechanism of **serpin polymerization**, researchers have proposed that **small-molecule inhibitors of protein polymerization** might be effective therapies for FENIB and other serpinopathies. Lomas and colleagues, in the Nature paper, state that their findings imply that inhibitors of protein polymerization may be effective therapies for FENIB and perhaps other more common neurodegenerative diseases.[7] Experimental work in alpha1-antitrypsin deficiency has explored chemical chaperones and proteostasis modulators that stabilize serpin folding and reduce polymer formation; similar approaches could be applied to neuroserpin.[4][13][18]

Gene therapy approaches, such as **AAV-mediated delivery of wild-type SERPINI1** or **CRISPR-based correction of mutant alleles**, are theoretically possible but have not progressed to clinical trials. One challenge is that simply increasing neuroserpin expression could exacerbate polymerization if the mutant protein is produced; thus, gene therapy would need to selectively silence mutant alleles or replace them with corrected versions. RNA-based therapies (antisense oligonucleotides, siRNA) targeting mutant SERPINI1 mRNA could reduce production of mutant protein and alleviate ER stress, but these technologies are in early stages for serpinopathies.

Targeted therapies aimed at **ER stress pathways**, such as modulators of PERK, IRE1 or ATF6, could in principle reduce apoptosis and improve neuronal survival in FENIB, but again, no specific trials exist. Neuroserpin’s interaction with tPA suggests that modulating tPA or plasmin activity, perhaps with tPA inhibitors or plasminogen activators, could influence disease, but this carries bleeding and thrombosis risks and is complex.

Immunotherapies directed at neuroserpin polymers are speculative, and no monoclonal antibody therapies have been developed. Cell therapies (e.g. stem cell transplant) are unlikely to address the underlying genetic defect and polymerization mechanism.

### 12.3 Surgical, Supportive and Rehabilitative Interventions

Surgical interventions such as **epilepsy surgery**—resection of seizure foci—could be considered in highly focal epilepsy, but FENIB’s diffuse cortical pathology and PME phenotype make it less amenable to resective surgery. There are no published cases of successful epilepsy surgery in FENIB.[8][10] However, invasive neuromodulation techniques such as deep brain stimulation or responsive neurostimulation could, in theory, be applied, though evidence is lacking.

Supportive care is vital. This includes **physical therapy** to manage ataxia and spasticity, **occupational therapy** to maintain daily living skills, **speech therapy** for dysarthria and language difficulties, and **nutrition support** to prevent weight loss and aspiration.[3][5][8][10] Psychological and social support for patients and families is essential, as is management of comorbid conditions such as depression and anxiety. NCIT terms like “Supportive care,” “Physical therapy,” “Occupational therapy” and “Speech therapy” describe these interventions.

### 12.4 Treatment Outcomes and Personalized Medicine

Treatment outcomes are generally **poor** with respect to seizure control and cognitive decline. MedlinePlus notes that seizures in most people with FENIB are not controlled by anti-seizure medications.[5] Case reports describe ongoing seizures despite polytherapy and progressive cognitive and motor deterioration.[8][10] No disease-modifying therapies exist, so personalized medicine currently focuses on **genetic counseling and risk assessment** rather than genotype-guided pharmacotherapy.

In the future, personalized medicine could leverage **mutation-specific therapies**, such as small molecules tailored to stabilize particular neuroserpin variants or allele-specific RNA therapies. Genotype information (e.g. S49P vs S52R) could inform prognosis and timing of interventions. For now, clinical management is largely uniform across mutations, guided by symptom severity rather than genotype.

## 13. Prevention

### 13.1 Primary, Secondary and Tertiary Prevention

Primary prevention of FENIB by environmental or lifestyle modification is not possible, given its **genetic etiology**. However, **genetic counseling** and **reproductive planning** offer means of reducing disease incidence in families with known SERPINI1 mutations. Couples may consider options such as preimplantation genetic diagnosis (PGD) or prenatal testing to avoid transmission of pathogenic variants.[3][5]

Secondary prevention involves **early detection and management** to reduce complications. For example, early diagnosis of FENIB in at-risk individuals could allow proactive seizure monitoring and management, fall prevention, and nutritional support to mitigate pneumonia risk. However, without disease-modifying therapies, secondary prevention mainly addresses complications rather than the underlying disease.

Tertiary prevention focuses on **limiting disability and improving quality of life** in patients with established FENIB. This includes comprehensive multidisciplinary care, assistive devices, home modifications, and caregiver support to prevent injuries, social isolation and psychological trauma.[3][5][10]

### 13.2 Screening, Risk Stratification and Counseling

Population-based screening for FENIB is not feasible or recommended due to its rarity and lack of effective interventions. However, **cascade screening** of family members in FENIB pedigrees is appropriate. Genetic testing for SERPINI1 variants in asymptomatic at-risk relatives can identify those who carry the mutation, enabling informed reproductive decisions and anticipatory guidance.[5][10]

Risk stratification within families is largely genetic: carriers of pathogenic SERPINI1 variants have high risk of developing FENIB, whereas non-carriers do not. Age of onset and severity can be estimated based on the specific mutation and family history. Genetic counseling should address autosomal dominant inheritance, variable expressivity, potential age of onset, and the current lack of curative treatments.

Behavioral interventions (e.g. lifestyle modifications) have limited impact on disease risk but may improve overall health and resilience. Public health interventions are not needed for FENIB specifically, though general epilepsy and dementia awareness campaigns may encompass rare disorders like FENIB.

## 14. Other Species and Natural Disease

### 14.1 Natural Occurrence in Other Species and Comparative Pathology

No naturally occurring **FENIB-like disease** has been reported in companion animals or wildlife. While serpinopathies such as alpha1-antitrypsin deficiency occur in humans and some animal models, neuroserpin-related encephalopathy appears unique to humans in terms of documented cases.[13][18] OMIA and veterinary databases do not list neuroserpin encephalopathy in animals, based on current knowledge.

Comparative pathology studies focus on **experimental models** rather than natural disease. Transgenic mice and flies expressing mutant neuroserpin develop inclusion bodies and neurological symptoms reminiscent of human FENIB, but these are induced models rather than naturally occurring conditions.[4][13][17] Evolutionary conservation of neuroserpin and tPA across species suggests that similar mechanisms could exist in animals, but spontaneous SERPINI1 mutations causing encephalopathy have not been documented.

### 14.2 Zoonotic Potential and Cross-Species Susceptibility

FENIB is a **noninfectious genetic disorder** and has no zoonotic potential. It cannot be transmitted between individuals or across species except through inheritance of SERPINI1 mutations. Cross-species susceptibility relates only to the potential of SERPINI1 orthologs to develop polymerization-prone mutations, as modeled experimentally in mice and flies.[4][13][17]

## 15. Model Organisms

### 15.1 Mouse Models of Neuroserpin Polymerization

Transgenic **mouse models** have been critical in elucidating FENIB pathophysiology. Miranda et al. generated mice overexpressing mutant forms of human neuroserpin (S49P-Syracuse and S52R-Portland) under the control of the Thy-1 promoter, ensuring expression in central nervous system neurons.[17] These mice exhibit morphological, biochemical and clinical features resembling those found in human FENIB, including large intraneuronal PAS-positive inclusions composed exclusively of mutant neuroserpin, accumulating long before clinical symptoms.[17]

Histological examination reveals massive intraneuronal PAS-positive round bodies reminiscent of human Collins bodies, sometimes numerous and arranged in grape-like clusters.[17] Electron microscopy localizes these aggregates to the ER, confirming that the inclusions are endoplasmic neuroserpin polymers.[17] Mice expressing Portland neuroserpin display more severe clinical symptoms (e.g. motor deficits, seizures) and more neuroserpin deposits than Syracuse mice, validating the genotype–phenotype correlation observed in humans.[17][18]

Phenotype recapitulation in these models includes **neuroserpin polymer accumulation**, **ER stress**, **neuron dysfunction and death**, and **neurological symptoms**. However, mouse lifespans and brain architectures differ from humans, and some features, such as complex cognitive and behavioural changes, may not be fully captured. Nonetheless, these models are invaluable for studying **temporal progression of polymer accumulation**, **ER stress responses**, and **candidate therapeutic interventions** (e.g. proteostasis modulators, ER stress inhibitors).[4][9][13][17][18]

### 15.2 Other Experimental Systems

Beyond mice, **cellular models** such as COS-7 cells expressing mutant neuroserpin have been used to study polymerization and ER retention. Miranda et al. show that H338R and G392E neuroserpin form polymers that accumulate within the ER of COS-7 cells, mimicking neuronal ER retention.[9] Cultured neurons overexpressing neuroserpin have been employed to examine effects on dendritic spines and synaptic plasticity.[14][16] PC12 cell models demonstrate neuroserpin’s role in cell–cell adhesion and N-cadherin-mediated interactions.[14][16]

Fly models (Drosophila melanogaster) overexpressing human polymerogenic neuroserpin have been reported to develop neurological symptoms reminiscent of FENIB, with ER retention causing neuronal damage through a toxic gain-of-function mechanism.[13] These invertebrate models allow genetic screens for modifiers and offer high-throughput platforms for testing potential therapies.

Model limitations include differences in neuroserpin expression patterns, neuroanatomy and lifespan compared to humans. Some aspects of FENIB, such as frontal-executive dysfunction and complex psychiatric symptoms, cannot be fully modeled in animals. Nevertheless, **experimental models faithfully reproduce the core mechanistic features of neuroserpin polymerization and ER stress**, providing powerful tools for mechanistic study and preclinical therapeutic development.[4][9][13][16][17][18]

## Conclusion

Familial encephalopathy with neuroserpin inclusion bodies (FENIB) is a rare but mechanistically instructive **Mendelian serpinopathy of the nervous system**, defined by heterozygous missense mutations in **SERPINI1** that destabilize neuroserpin, precipitating ER-retained polymer formation, Collins body inclusions and progressive neurodegeneration culminating in epilepsy and dementia.[1][2][3][4][5][9][17][18] Clinically, FENIB manifests as variable-age onset frontal-predominant cognitive decline, progressive myoclonus epilepsy and other seizure types, motor signs including tremor, dysarthria, cerebellar symptoms and pyramidal tract involvement, and neuropsychiatric disturbances ranging to catatonia, with severe impact on quality of life and shortened survival.[2][3][5][8][10] Neuropathologically, it is distinguished by PAS-positive, diastase-resistant neuronal inclusion bodies composed almost exclusively of neuroserpin, localized to the ER of deep-layer cortical neurons and subcortical nuclei such as substantia nigra, and showing a clear genotype–phenotype correlation with mutation-specific polymerization propensity.[1][2][9][17][18]

Mechanistically, FENIB exemplifies how **protein conformational diseases** arise from subtle point mutations in structurally labile proteins. Neuroserpin’s metastatic serpin fold permits protease inhibition but is prone to misfolding when the shutter region is perturbed. Mutant neuroserpin polymerizes within the ER, triggering ER stress and unfolded protein response activation, leading to neuronal dysfunction and death as polymers accumulate over time.[4][9][13][15][17][18] Concurrently, reduced neuroserpin secretion impairs tPA inhibition, potentially enhancing extracellular protease activity, altering synaptic plasticity, and increasing neuronal excitability, thereby contributing to seizures and cognitive disruption.[12][13][14][16] The interplay of toxic gain-of-function (polymer accumulation) and loss-of-function (tPA dysregulation) illustrates the complexity of serpinopathies.

From a genetic standpoint, FENIB is unequivocally **autosomal dominant and monogenic**, with pathogenic SERPINI1 missense variants such as S49P, S52R, H338R, G392E, G392R and R393P. Mutation-specific instability correlates inversely with age of onset and directly with inclusion burden, offering a model of genotype–phenotype correlation that informs prognosis and mechanistic understanding.[1][4][8][9][10][13][17][18] Despite its rarity—Orphanet estimates prevalence <1/1,000,000 and MedlinePlus notes only around a dozen reported individuals—FENIB has had outsized impact on our grasp of serpin biology, ER stress in neurodegeneration and the neuroserpin–tPA axis.[3][5][13][14][16]

Diagnostic work-up integrates clinical recognition of progressive myoclonus epilepsy and presenile dementia, genetic testing for SERPINI1 variants, and, when available, histopathological confirmation of Collins bodies. Neuroimaging and EEG contribute to characterization but lack specific FENIB signatures. There are no omics-based diagnostics or validated biomarkers beyond SERPINI1 variant testing.[1][2][3][5][8][9][10][18] Treatment remains largely symptomatic, with antiepileptics often failing to control seizures and cognitive decline inexorable. Supportive multidisciplinary care is essential, but disease-modifying therapies are lacking.[5][8][10]

Looking forward, FENIB offers a **valuable template for targeted therapeutic development**. Small-molecule inhibitors of serpin polymerization, ER stress modulators, and allele-specific gene or RNA therapies could be explored, leveraging insights from alpha1-antitrypsin deficiency and other protein-folding disorders.[4][7][13][18] Transgenic mouse and fly models provide platforms for preclinical testing, and advances in proteostasis and precision medicine may eventually yield interventions that stabilize neuroserpin, enhance polymer clearance or mitigate ER stress, thereby altering the course of FENIB and related serpinopathies.[4][9][13][16][17][18] Genetic counseling and reproductive planning can already reduce disease incidence in affected families, while improved recognition and diagnosis ensure that FENIB is considered among progressive myoclonus epilepsies and presenile dementias.

In conclusion, although FENIB affects only a handful of individuals worldwide, it illuminates fundamental aspects of **protein misfolding, ER stress, synaptic regulation and neurodegeneration**, and continues to serve as a model system with implications extending beyond this rare encephalopathy to broader fields of neurology, molecular medicine and therapeutic innovation.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 0 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000720` (1 mention) - the report calls it "Dementia"; HP calls it **obsolete Mood swings**
- `HP:0006893` (1 mention) - the report calls it "Frontal lobe dysfunction"; HP calls it **obsolete Severely dysplastic cerebellum**
- `HP:0002352` (1 mention) - the report calls it "Progressive cognitive decline"; HP calls it **Leukoencephalopathy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0000720` (obsolete Mood swings) (1 mention) - replaced by `HP:0000712`
- `HP:0006893` (obsolete Severely dysplastic cerebellum) (1 mention) - replaced by `HP:0007033`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0001870` (1 mention) - the report calls it "frontal lobe"; UBERON calls it **frontal cortex**, and lists "frontal lobe cortex" among its other names