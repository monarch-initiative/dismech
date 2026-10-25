---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-23T14:56:20.287027'
end_time: '2026-10-23T14:59:43.733323'
duration_seconds: 203.45
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Isolated Congenital Digital Clubbing
  mondo_id: MONDO:0007343
  category: Mendelian
  causal_genes: HPGD
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 15
  not_found: 0
  obsolete: 0
  unverifiable: 9
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0007343
    reported_labels:
    - Mondo
    ontology_label: isolated congenital digital clubbing
  - term_id: HP:0100759
    reported_labels:
    - All fingernails in 11/11 affected members of the key pedigree
    ontology_label: Clubbing of fingers
  - term_id: HP:0100760
    reported_labels:
    - All toenails in 11/11 in the key pedigree
    ontology_label: Clubbing of toes
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - Rhea
  - Taxon
  - MMRRC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Congenital Digital Clubbing
- **MONDO ID:** MONDO:0007343 (if available)
- **Causal gene(s):** HPGD
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Isolated Congenital Digital Clubbing** covering all of the
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

# Isolated Congenital Digital Clubbing  
**MONDO:0007343 | OMIM:119900 | ORPHA:217059 | Mendelian disease**

## Executive summary

**Isolated congenital digital clubbing is an autosomal-recessive disorder caused, in its molecularly established form, by biallelic pathogenic variation in *HPGD*.** *HPGD* encodes cytosolic NAD\(^+\)-dependent 15-hydroxyprostaglandin dehydrogenase (15-PGDH), the principal enzyme initiating prostaglandin E2 (PGE2) inactivation. The defining phenotype is congenital, usually bilateral and symmetric enlargement of the terminal fingers and toes with broad, thick, hyperconvex nails, but without periostosis, pachydermia, arthritis, cardiopulmonary disease, or another systemic cause. The key disease-gene evidence is a six-generation consanguineous Pakistani family in which all 11 affected members were homozygous for *HPGD* NM_000860:c.577T>C, p.(Ser193Pro). The original report called clubbing the “single invariable clinical feature without any associated ectodermal, skeletal or systemic imperfection.” PMID: **18805827**, published **January 2009**, DOI: [10.1136/jmg.2008.061234](https://doi.org/10.1136/jmg.2008.061234). [61][120]

Evidence is exceptionally limited: the specific *HPGD*-defined isolated phenotype rests principally on one large pedigree. The same p.Ser193Pro allele has subsequently been reported with syndromic primary hypertrophic osteoarthropathy (PHO), indicating that genotype–phenotype prediction is not absolute and may depend on residual enzyme activity or other modifiers. A 2023 review supports a prostaglandin-degradation continuum from isolated clubbing to PHO but supplies no new isolated-*HPGD* cohort. [94][301][325]

---

## 1. Disease information

### Definition

Digital clubbing is broadening of the non-edematous soft tissues at the distal digits in all dimensions, accompanied by increased longitudinal and transverse nail curvature. In isolated congenital disease, it is present from birth or early infancy and is not accompanied by an acquired pulmonary, cardiovascular, gastrointestinal, hepatic, infectious, inflammatory, or neoplastic condition. Histologically and anatomically it reflects expansion of connective tissue between the nail matrix and distal phalanx. [16][20][245]

### Identifiers and synonyms

| Resource | Identifier or term | Interpretation |
|---|---|---|
| Mondo | **MONDO:0007343** | Isolated congenital digital clubbing |
| OMIM phenotype | **OMIM:119900** | Digital clubbing, isolated congenital; contrary to the supplied “not recorded” field, an OMIM entry is available |
| Orphanet | **ORPHA:217059** | Isolated nail clubbing |
| UMLS | **C1861514**; MedGen concept **C0345408** | Mapped disease concepts [259][238] |
| MeSH | **D010004**, Osteoarthropathy, Primary Hypertrophic | Broader indexing descriptor; isolated congenital digital clubbing is an entry/indexing term, not a uniquely specific MeSH descriptor [226][227] |
| ICD-10/ICD-10-CM | **Q68.1**, congenital deformity of finger(s) and hand | Approximate congenital code used by Orphanet-derived mappings; not disease-specific [228][239] |
| ICD-10-CM, acquired/unspecified clubbing | **R68.3**, clubbing of fingers/nails | Should not replace Q68.1 when congenital status is established [231][240] |
| ICD-11 | **EE10.0**, abnormality of nail shape, includes digital clubbing | Broader nail-shape category; not specific for inherited congenital clubbing [232] |
| Causal gene identifier | *HPGD*: HGNC:**5154**; NCBI Gene:**3248**; OMIM:**601688**; UniProt:**P15428** | Protein-coding gene at 4q34.1 [46][48][49] |

**Synonyms:** isolated congenital nail clubbing, isolated nail clubbing, hereditary clubbing of digits, hereditary acropachy, isolated congenital acropachy, clubbing of digits, and digital clubbing, isolated congenital. “Watch-glass nails,” “drumstick fingers,” and “Hippocratic fingers” describe the morphology but are not preferred disease names. [40][245][268]

### Evidence provenance

This is primarily a **disease-level aggregation derived from published family studies**, not an EHR-derived disease definition. OMIM’s molecular assignment is based mainly on the Tariq et al. pedigree of 11 affected relatives. Orphanet, Mondo, MedGen, ClinVar, and HPO subsequently aggregate that literature. By contrast, recent EHR statistics for “nail clubbing” include mostly acquired clubbing and must not be interpreted as prevalence of this congenital Mendelian disease. [61][92][365]

---

## 2. Etiology

### Primary cause

The established cause is a **germline homozygous missense variant in *HPGD***, resulting in deficient or reduced 15-PGDH-mediated PGE2 catabolism. The disease maps to chromosome 4q32.3–q34.1; *HPGD* itself lies at 4q34.1. In the original pedigree, homozygosity mapping gave a maximum two-point LOD score of 2.98 and multipoint LOD score of 3.62, followed by identification of c.577T>C, p.Ser193Pro in exon 6. [61][369]

### Risk and protective factors

| Factor class | Current evidence |
|---|---|
| Biallelic *HPGD* pathogenic genotype | Established genetic risk; the original pedigree showed autosomal-recessive segregation. [61][134] |
| Consanguinity | Increases the probability that both parents carry the same rare allele; the molecularly defined family was consanguineous. It is not itself mechanistic. [14] |
| Family history | Strong diagnostic and recurrence-risk indicator. |
| Sex | No demonstrated sex effect in *HPGD*-defined recessive disease: the original affected group comprised four males and seven females. [14] |
| Age | Congenital phenotype; age does not cause the disorder. |
| Environmental, infectious, occupational or lifestyle factors | None established as causes or modifiers of the congenital *HPGD*-related phenotype. Smoking, hypoxia, malignancy, infection, and cardiopulmonary disease are instead causes of **acquired secondary clubbing** and therefore differential diagnoses. |
| Protective variants/modifier genes | None validated. |
| Environmental protective factors | None demonstrated. Avoiding smoking and cardiopulmonary injury is good general health practice but does not prevent a biallelic congenital *HPGD* disorder. |
| Gene–environment interaction | No disease-specific interaction has been demonstrated. A theoretical interaction with drugs that alter prostaglandin synthesis is biologically plausible but untested in isolated congenital clubbing. |

A distinct prostaglandin-clearance gene, ***SLCO2A1***, can produce isolated clubbing or PHO and is an important phenocopy/locus-heterogeneity gene. It should not replace *HPGD* as the causal gene for the MONDO/OMIM target specified here. [34][41][103]

---

## 3. Phenotypes

### Core and associated findings

| Phenotype | Type and characteristics | Onset/course/frequency in *HPGD* pedigree | Suggested HPO term |
|---|---|---|---|
| Digital clubbing | Physical sign: bulbous enlargement of distal digits, increased nail curvature, loss of normal nail-fold angle | Congenital; bilateral, symmetric; present in **11/11** reported affected relatives; apparently lifelong | **HP:0001217 Clubbing** |
| Clubbing of fingers | Physical sign involving distal fingers | All fingernails in 11/11 affected members of the key pedigree | **HP:0100759** |
| Clubbing of toes | Physical sign involving distal toes | All toenails in 11/11 in the key pedigree | **HP:0100760** |
| Thick/broad nail plates | Nail manifestation | Congenital and persistent; enlargement/thickening is part of the defining phenotype | **HP:0001821 Broad nail**; **HP:0001597 Abnormal nail morphology** |
| Hyperconvex nails | Nail manifestation, producing a watch-glass contour | Typical qualitative feature; disease-specific percentage unavailable | **HP:0001795 Hyperconvex nail** |
| Broad distal fingers/toes | Soft-tissue physical manifestation | Typical consequence of clubbing; precise separate frequency unavailable | **HP:0001500 Broad finger**; **HP:0001837 Broad toe** |
| Connective-tissue proliferation beneath nail | Histopathologic/anatomic manifestation | Defining pathologic explanation, but biopsy was not systematically reported in the pedigree | **HP:0003549 Abnormality of connective tissue** |
| Pain | Symptom | Usually absent in isolated congenital clubbing; the condition is generally painless | No positive HPO annotation recommended |
| Periostosis, pachydermia, arthropathy, acro-osteolysis | Syndromic PHO manifestations | **Absent by definition and absent in the original isolated pedigree**; their presence should prompt classification as PHO rather than isolated clubbing | Record as explicitly excluded rather than positive phenotype |
| Ectodermal/systemic abnormalities | Other manifestations | Not reported in the original 11 affected people | No positive annotation |

The strongest family-level statement is that all 11 affected individuals had bilateral symmetric clubbing of every fingernail and toenail without associated abnormalities. [14][369] Orphanet describes isolated clubbing as usually painless, bilateral, and symmetric; occasional sparing of digits is possible in broader hereditary clubbing, although thumbs are almost always affected. [16]

### Severity and quality of life

Severity is primarily cosmetic and morphologic; formal mild/moderate/severe scales have not been validated. Historical hereditary families described congenital clubbing that remained fixed without progression or regression. No disease-specific EQ-5D, SF-36, PROMIS, pain, dexterity, or psychosocial studies were found. Available clinical reviews describe minimal morbidity, with possible concern about appearance rather than loss of hand or foot function. [140][369]

---

## 4. Genetic and molecular information

### Gene and protein

| Feature | Annotation |
|---|---|
| Gene | ***HPGD*** |
| HGNC / NCBI / OMIM | HGNC:5154 / Gene 3248 / OMIM 601688 |
| Location | Chromosome **4q34.1** |
| Transcript used clinically | **NM_000860.6** |
| Protein | 15-hydroxyprostaglandin dehydrogenase [NAD\(^+\)]; UniProt **P15428** |
| Enzyme | EC **1.1.1.141** |
| Protein family | Short-chain dehydrogenase/reductase, SDR36C1 |
| Main reaction | PGE2 + NAD\(^+\) → 15-oxo-PGE2 + NADH + H\(^+\); Rhea:11876 [440] |
| Main compartment | Cytosol/cytoplasm |
| Normal function | Initial oxidation and biological inactivation of PGE2 and other hydroxylated eicosanoids [46][84] |

### Disease-defining variant

| Attribute | Finding |
|---|---|
| HGVS | **NM_000860.6:c.577T>C; NP_000851:p.(Ser193Pro)** |
| Legacy notation | S193P |
| dbSNP | **rs121434481** |
| ClinVar | Variation ID **7920**, pathogenic listing for isolated congenital digital clubbing |
| OMIM allelic variant | **601688.0004** |
| Type | Missense single-nucleotide variant |
| Origin | Germline |
| Zygosity | Homozygous in affected members; obligate carriers heterozygous |
| Segregation | Consistent with autosomal-recessive inheritance in the six-generation pedigree |
| Population evidence | Absent from 300 ethnically matched control chromosomes in the original study; a reliable current gnomAD allele frequency was not available from the retrieved disease record |
| Functional interpretation | Probable partial loss of function/hypomorphic allele, but the original isolated-clubbing paper did not provide a direct enzyme assay |
| ClinVar status caveat | “Pathogenic” is database-submission consensus rather than a ClinGen expert-panel classification; ClinVar does not independently validate submitter interpretations. [286][290] |

A later analysis inferred that p.Ser193Pro is hypomorphic because homozygous isolated-clubbing cases showed a **less than twofold urinary PGE2 increase**, compared with an approximately sixfold increase in severe PHO caused by more disruptive *HPGD* alleles. [71][94] However, p.Ser193Pro was later reported in a family labeled PHO, so residual activity alone may not fully explain expressivity. [301]

### Other molecular categories

- **Modifier genes:** none validated.
- **Somatic variation:** not relevant; this is a germline Mendelian disorder.
- **Epigenetic abnormalities:** no disease-specific methylation, histone, or chromatin signature reported.
- **Chromosomal abnormalities:** no recurrent deletion, duplication, translocation, inversion, or aneuploidy established.
- **Structural variants:** pathogenic exon or gene deletions occur in PHOAR1, but none has been tied specifically to the classic isolated-clubbing pedigree.
- **Molecular profiling:** no disease-specific nail-bed transcriptomic, single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or multi-omic dataset was identified.
- **Functional genomic screens:** no disease-focused CRISPR/RNAi screen has been reported.

---

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, diet, alcohol use, exercise pattern, infection, or microbiome feature has been shown to cause *HPGD*-related isolated congenital digital clubbing.

This distinction is clinically important: **acquired** clubbing may accompany lung cancer, chronic suppurative pulmonary disease, interstitial lung disease, cyanotic congenital heart disease, infective endocarditis, inflammatory bowel disease, cirrhosis, or thyroid acropachy. Those conditions do not become etiologic factors for the congenital Mendelian disorder; rather, their exclusion supports the word “isolated.” [142][252]

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A homozygous germline *HPGD* c.577T>C, p.Ser193Pro variant leads to** altered 15-PGDH protein structure or stability; direct biochemical impairment of this specific allele is strongly inferred but was not directly measured in the original report.  
2. **Reduced 15-PGDH activity leads to** impaired cytosolic NAD\(^+\)-dependent oxidation of PGE2 to much less active 15-oxo-PGE2/PGE-M products.  
3. **Impaired PGE2 degradation results in** a modest chronic increase in biologically active PGE2 and an increased PGE2-to-PGE-M relationship.  
4. **Elevated PGE2 signaling leads to, or is inferred to promote,** endothelial activation, VEGF expression, angiogenesis, vascular permeability, and fibroblast/mesenchymal-cell activity in distal digital tissues.  
5. **Vascular and stromal activation results in** capillary dilation, increased capillary density, edema, fibroblast hyperplasia, and extracellular-matrix/connective-tissue expansion between the nail matrix and distal phalanx.  
6. **Connective-tissue expansion and altered nail-matrix geometry lead to** broadening of terminal digits, thickened hyperconvex nails, loss of the normal Lovibond angle, and a positive Schamroth sign.  
7. **Mechanistic branch—severity threshold, inferred:** modest residual enzyme function may restrict disease to the digits, whereas severe *HPGD* deficiency and greater PGE2 elevation can additionally lead to periostosis, pachydermia, acro-osteolysis, arthritis, and congenital heart manifestations of PHOAR1. [94][169]

### Mechanistic detail and ontology suggestions

15-PGDH is the intracellular component of a two-step clearance system: prostaglandin transporters bring extracellular PGE2 into the cell, after which 15-PGDH oxidizes its 15-hydroxyl group. Deficiency of either *HPGD* or the transporter gene *SLCO2A1* therefore raises PGE2. [83][86]

The direct biochemical reaction is well established, but the tissue-selective route from modest systemic PGE2 elevation to isolated nail clubbing is incompletely demonstrated. PHO and general clubbing histology show increased capillary density and dilation, edema, and fibroblast and vascular-smooth-muscle hyperplasia. PGE2 can stimulate endothelial VEGF expression and angiogenesis, making this the leading mechanistic model rather than a fully proven nail-specific pathway. [318][325]

| Mechanistic entity | Suggested ontology annotation |
|---|---|
| Prostaglandin metabolic process | GO:**0006693** |
| Prostaglandin catabolic process | GO:**0006694** |
| Angiogenesis | GO:**0001525** |
| Extracellular-matrix organization | GO:**0030198** |
| Positive regulation of fibroblast proliferation | GO:**0048146** |
| Cytosol | GO:**0005829** |
| Fibroblast | CL:**0000057** |
| Blood-vessel endothelial cell | CL:**0000071** |
| Osteoblast, relevant mainly to PHO branch | CL:**0000062** |
| PGE2 | CHEBI:**15551**; principal active metabolite in the proposed mechanism |
| NAD\(^+\) | CHEBI:**57540** |
| 15-oxo-PGE2 | CHEBI:**606564** in the annotated HPGD reaction [440] |

There is no evidence that autoimmunity, immunodeficiency, apoptosis, autophagy, mitochondrial failure, or primary oxidative injury initiates isolated clubbing. Inflammation is downstream or secondary in syndromic PHO rather than a demonstrated primary process here.

---

## 7. Anatomical structures affected

| Scale | Affected structure | Suggested ontology |
|---|---|---|
| Organ/body region | Fingers | UBERON:**0002389** |
| Organ/body region | Toes/pedal digits | UBERON:**0001466** |
| Local structure | Nails | UBERON:**0001705** |
| Local structure | Nail bed of finger | UBERON:**0005278** |
| Local structure | Nail matrix | UBERON:**0002283**; verify against the current release because nail-matrix mappings have changed |
| Skeletal landmark | Distal/terminal phalanx | UBERON:**0004300** [434] |
| Tissue | Connective tissue between nail matrix and distal phalanx | No sufficiently specific established Uberon term; annotate parent connective tissue plus site |
| Cell populations | Fibroblasts, endothelial cells, vascular smooth-muscle cells | CL:0000057, CL:0000115/CL:0000071, and CL:0000359 |
| Subcellular site of primary enzyme defect | Cytosol | GO:0005829 |

The condition is normally **bilateral and symmetric**, involving both hands and feet in the molecularly defined pedigree. No internal organ is directly affected in the isolated phenotype. Cardiovascular, skeletal, skin, or joint involvement indicates an allelic syndromic disorder rather than uncomplicated isolated clubbing. [14][16]

---

## 8. Temporal development

- **Onset:** congenital or neonatal; Orphanet also allows early infancy. [19]
- **Pattern:** chronic and insidious in appearance rather than an acute inflammatory event.
- **Course:** generally stable and lifelong. Historical congenital pedigrees reported no progression or regression, although those older autosomal-dominant families were not molecularly linked to *HPGD*. [369]
- **Stages:** no validated staging system. Morphologic clubbing can be described clinically as nail-bed softening, increased Lovibond angle, hyperconvexity, and finally distal bulbous enlargement, but that sequence comes mainly from acquired clubbing literature. [157]
- **Remission:** no spontaneous or treatment-induced remission documented specifically for *HPGD*-related isolated congenital disease.
- **Critical period:** nail and distal-digit development is presumably the vulnerable developmental period, but no human intervention window has been established.
- **Duration:** expected lifelong unless future pathway-directed treatment proves capable of remodeling established connective tissue.

---

## 9. Inheritance and population

### Inheritance

The molecularly established *HPGD* form is **autosomal recessive**. If both parents are heterozygous for the same pathogenic allele, each pregnancy has an expected 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele.

Within the original pedigree, all affected people were homozygous and obligate carriers were heterozygous, consistent with high penetrance of the homozygous genotype in that family. Population-level penetrance is unknown. Variable expressivity is likely because p.Ser193Pro has also been associated with PHO. No anticipation, repeat expansion, or established germline mosaicism has been reported. [92][301]

Autosomal-dominant isolated clubbing families also exist, but one molecular investigation found no *HPGD* mutation and concluded that *HPGD* is not the major gene for dominant isolated clubbing. Those families therefore should not be assigned *HPGD* causality without molecular confirmation. [102][133]

### Epidemiology and demographics

| Statistic | Current evidence |
|---|---|
| Prevalence | **Unknown**; Orphanet provides no numerical estimate. [362] |
| Incidence | Unknown |
| Number in defining *HPGD* pedigree | 11 affected members |
| Sex in defining pedigree | 4 male, 7 female |
| Geographic/ancestral evidence | One six-generation consanguineous Pakistani family; insufficient to infer ethnic enrichment |
| Founder effect | Not established |
| Carrier frequency | Unknown |
| Sex ratio | Unknown; available pedigree does not support male limitation |
| Age distribution | Congenital onset; affected individuals can remain recognizable throughout life |

The 0.03% EHR prevalence reported for broadly coded adult nail clubbing in the US All of Us dataset is **not** a prevalence estimate for isolated congenital *HPGD* disease. [365]

---

## 10. Diagnostics

### Clinical approach

1. **Confirm true clubbing.**
   - Lovibond/profile angle greater than 180°.
   - Phalangeal-depth ratio at the nail fold to distal interphalangeal joint of at least 1.
   - Loss of the diamond-shaped window when corresponding fingers are opposed—positive Schamroth sign. [151][153]

2. **Establish congenital, symmetric, familial, and stable presentation.**
   - Examine all fingers and toes.
   - Obtain childhood photographs and a three-generation pedigree where possible.

3. **Exclude acquired causes.**
   - History and examination for hypoxia, cough, dyspnea, cyanosis, fever, weight loss, diarrhea, liver disease, thyroid disease, and malignancy.
   - Directed pulse oximetry, chest imaging, pulmonary testing, echocardiography, inflammatory testing, gastrointestinal or hepatic evaluation only when clinically indicated.

4. **Exclude syndromic PHO.**
   - Ask about bone/joint pain, swelling, hyperhidrosis, seborrhea, acne, pachydermia, delayed fontanel closure, and congenital heart disease.
   - Obtain long-bone radiographs if pain, swelling, or periostosis is suspected.

### Laboratory and biomarkers

Urinary PGE2 and PGE-M are supportive biochemical markers of prostaglandin-clearance disorders. In *HPGD* deficiency, PGE-M tends to be low and the PGE2/PGE-M ratio high; in *SLCO2A1* deficiency, PGE-M is often increased. These assays are not standardized diagnostic criteria for isolated clubbing and may be unavailable clinically. [166]

Biopsy is unnecessary in a typical case. Expected general clubbing pathology includes capillary dilation and proliferation, edema, fibroblast hyperplasia, vascular smooth-muscle hyperplasia, and sometimes perivascular lymphocytes. [158]

### Genetic testing

| Test | Utility |
|---|---|
| *HPGD* sequencing | Preferred first-line molecular test when the phenotype and pedigree fit the target disease |
| Deletion/duplication analysis | Reasonable if sequencing is negative; available in clinical NGS/CNV assays [123][392] |
| Clubbing/PHO panel | Include at least ***HPGD* and *SLCO2A1***; broader panels may help when additional skeletal, skin, cardiac, or intestinal findings are present |
| Exome sequencing | Appropriate after negative focused testing or for atypical/heterogeneous presentations |
| Genome sequencing | May detect intronic or structural variants missed by exome/panel testing, but no disease-specific superiority data exist |
| CMA, karyotype, FISH | Low yield for a classic recessive single-gene phenotype; reserve for additional congenital anomalies |
| Mitochondrial or repeat-expansion testing | Not indicated |
| RNA sequencing | Research or splice-variant confirmation; not routine for isolated p.Ser193Pro disease |

A diagnosis is molecularly confirmed by pathogenic/likely pathogenic variants on both *HPGD* alleles, ideally with parental phasing. A single heterozygous *HPGD* variant does not usually establish this recessive diagnosis.

### Differential diagnosis

- Secondary clubbing due to pulmonary, cardiac, hepatic, gastrointestinal, infectious, inflammatory, or malignant disease.
- PHOAR1 due to *HPGD* and PHOAR2/PHOAD due to *SLCO2A1*.
- Thyroid acropachy.
- Pseudoclubbing from acro-osteolysis, hyperparathyroidism, scleroderma, or congenital distal-phalanx anomalies.
- Simple hyperconvex nails or onychogryphosis without true distal soft-tissue broadening.
- Other hereditary nail dysplasias.

**Suggested NCIt intervention labels:** Physical Examination; Genetic Testing; DNA Sequencing; Whole Exome Sequencing; Whole Genome Sequencing; Radiography; Echocardiography; Genetic Counseling.

---

## 11. Outcome and prognosis

The isolated condition appears **benign and non-life-limiting**, but no formal survival cohort exists. There are no reported disease-specific mortality rates, five- or ten-year survival figures, or measured reductions in life expectancy. Clubbing itself is not considered an independent cause of mortality; risk in an apparent case comes from missing an acquired systemic cause or a syndromic PHO phenotype. [140]

Expected morbidity is minimal, chiefly cosmetic. No consistent impairment of grip, walking, sensation, nail growth, or activities of daily living has been documented. Established tissue enlargement may be permanent because chronic collagen and connective-tissue remodeling is unlikely to reverse completely. [137]

There are no validated prognostic biomarkers. Potentially relevant research variables include residual 15-PGDH activity, urinary PGE2, urinary PGE-M, PGE2/PGE-M ratio, and emergence of periostosis or pachydermia, but none has been validated specifically in isolated congenital disease.

---

## 12. Treatment

### Current standard

**No specific treatment is required or established for asymptomatic isolated congenital clubbing.** Management consists of confirming that the presentation is hereditary and isolated, reassurance, nail care if needed, and reevaluation if new cardiopulmonary, gastrointestinal, skeletal, joint, or skin symptoms develop. No corrective surgery is standard. [136][137]

### Pathway-directed evidence from related PHO—not direct evidence for this disease

Etoricoxib, a selective COX-2 inhibitor, reduces upstream PGE2 synthesis. In a single-arm PHO trial of 27 patients—including seven with *HPGD* variants—60 mg once daily for nine months was associated with reported improvement in digital clubbing in **74.1%**, joint swelling in 100%, pachydermia in 60.9%, and hyperhidrosis in 55%. PMID: **31508314**; ClinicalTrials.gov **NCT02438709**. [272]

This cannot be directly extrapolated to asymptomatic isolated congenital clubbing: the trial was uncontrolled, enrolled syndromic PHO, and did not report a dedicated isolated-clubbing subgroup. Long-term COX-2 inhibition carries gastrointestinal, renal, and cardiovascular risks, so cosmetic treatment of an otherwise benign congenital morphology is not routinely justified.

| Intervention | Status for isolated disease | Ontology suggestions |
|---|---|---|
| Reassurance/observation | Standard practical management | NCIt: Observation; Supportive Care |
| Nail care | Symptomatic/cosmetic only | NCIt: Supportive Care |
| Analgesic/NSAID | Only if pain occurs and another diagnosis such as PHO has been assessed | NCIt: Nonsteroidal Anti-inflammatory Drug |
| Etoricoxib | Experimental extrapolation from PHO; not established for isolated disease | CHEBI:**6339**; NCIt: Cyclooxygenase-2 Inhibitor [406] |
| Gene therapy, CRISPR, RNA, cell therapy | No clinical implementation or trial identified | Not applicable clinically |
| Surgery | No standard corrective operation | Not applicable |

No pharmacogenomic dosing rule, approved genotype-specific therapy, antisense treatment, gene replacement, or clinical gene-editing program exists.

---

## 13. Prevention

Because the disorder is inherited and congenital, diet, exercise, vaccination, infection control, and exposure reduction do not prevent disease in a fetus that inherits two causal alleles.

- **Primary prevention:** reproductive genetic counseling, partner testing when a familial variant is known, and optional preimplantation genetic testing for monogenic disease.
- **Prenatal diagnosis:** targeted testing of the familial variants using chorionic-villus sampling or amniocentesis can be considered after counseling.
- **Secondary prevention:** cascade testing of adult relatives identifies carriers and avoids unnecessary cardiopulmonary investigations in molecularly confirmed congenital cases.
- **Tertiary prevention:** monitor for features inconsistent with the isolated diagnosis, particularly bone pain, joint swelling, skin thickening, hyperhidrosis, intestinal symptoms, or cardiopulmonary complaints.
- **Population/newborn screening:** not recommended; prevalence is unknown, morbidity is low, and there is no established early therapy.
- **Vaccination or antimicrobial prophylaxis:** not applicable.
- **Public-health or environmental intervention:** not applicable.

Counseling should emphasize recessive recurrence risks while also explaining the limited genotype–phenotype data and the possibility that an *HPGD* genotype may sometimes produce a broader PHO phenotype.

---

## 14. Other species and natural disease

No naturally occurring animal disorder clearly homologous to human *HPGD*-related isolated congenital digital clubbing was identified in OMIA or the veterinary literature. Secondary hypertrophic osteoarthropathy occurs in dogs, cats, horses, and cattle, often without human-like nail clubbing, but it is not established as an inherited *HPGD* disorder. [388]

| Species | Taxon | Ortholog/resource | Evidence |
|---|---:|---|---|
| Human | NCBI Taxon:9606 | *HPGD*, Gene 3248 | Natural Mendelian disease |
| Mouse | NCBI Taxon:10090 | *Hpgd*, NCBI Gene **15446**, MGI:**108085** | Experimental knockout models [182] |
| Rat | NCBI Taxon:10116 | *Hpgd*, NCBI Gene **79242** | Ortholog; no natural isolated-clubbing model established [193] |
| Zebrafish | NCBI Taxon:7955 | *hpgd*, ZFIN:**ZDB-GENE-080728-2** | Ortholog/resource annotation; no validated clubbing phenotype [194][224] |

There is no zoonotic potential, infectious transmission, or cross-species contagion.

---

## 15. Model organisms

### Mouse models

A conventional ***Hpgd* knockout mouse** is the principal mechanistic model. Homozygous knockout pups fail to close the ductus arteriosus and die from congestive heart failure approximately 12–48 hours after birth. Neonatal indomethacin can rescue ductal closure and survival in some animals. The model demonstrates that 15-PGDH is essential for perinatal PGE2 clearance but does **not** adequately recapitulate isolated digital clubbing because early lethality prevents assessment of chronic adult digit morphology. [197][201]

Exact abstract-level model evidence includes: “neonatal death in *Hpgd*−/− mice is due to a patent ductus arteriosus and is rescued by neonatal injection of indomethacin.” PMID-linked mouse pregnancy work was published in **2019**. [198]

Additional models include:

| Model | Phenotype/application | Limitation |
|---|---|---|
| Global *Hpgd* knockout | Elevated PGE2, patent ductus arteriosus, perinatal death | Does not reproduce isolated clubbing |
| Indomethacin-rescued knockout | Permits survival and study of systemic PGE2 biology | Rescue is incomplete; drug treatment alters the pathway being studied |
| *Hpgd* hypomorphic mice | Elevated prostaglandins and spontaneous preterm labor | Reproductive model, not validated for digit clubbing |
| Conditional/floxed *Hpgd* mice | Tissue-specific study of PGE2 clearance | No nail-matrix-specific clubbing study reported |
| Aged *Hpgd*-deficient mice | Increased tissue PGE2 and enhanced hematopoietic/GI regenerative fitness | Demonstrates broader regenerative effects, not the human nail phenotype [199] |
| Small-molecule 15-PGDH inhibition | Experimental elevation of PGE2 to study regeneration or PHO-like pathways | Pharmacologic inhibition may not reproduce lifelong partial p.Ser193Pro deficiency |

Useful repositories include **MGI**, **IMSR**, and **MMRRC:032028-JAX**. [189][197]

---

## Recent developments and expert assessment

| Date | Development | Relevance |
|---|---|---|
| **8 February 2023** | A new *SLCO2A1*-associated family reinforced that inherited isolated nail clubbing is genetically heterogeneous. [41] | Supports including *SLCO2A1* when *HPGD* testing is negative, while retaining *HPGD* for this target entry |
| **11 February 2023** | Structural work described inhibitor-induced conformational closure of 15-PGDH. [167][353] | Advances enzyme biology and drug design, but not treatment of congenital clubbing |
| **29 August 2023** | Comprehensive PHO review synthesized genotype, urinary PGE2/PGE-M biomarkers, pathogenesis, and COX-2 treatment evidence. [83][166] | Best recent pathway-level review; evidence is primarily PHO rather than isolated disease |
| **18 October 2024** | A clinical report used exome testing and an HPO-derived clubbing gene set to diagnose homozygous pathogenic *HPGD*-related PHO after excluding hypoxic causes. [246] | Illustrates real-world genomic diagnosis and the importance of distinguishing isolated clubbing from PHO |
| **7 November 2024** | A novel *HPGD* splice variant causing exon skipping was functionally confirmed by RT-PCR in PHO. [386] | Expands the *HPGD* variant spectrum but does not establish a new isolated-clubbing allele |

### Evidence-weighted conclusion

The causal relationship between biallelic *HPGD* dysfunction and inherited prostaglandin-mediated clubbing is biologically compelling, but the **strictly isolated congenital phenotype is supported by a very small evidence base—principally one 11-person family**. The most defensible knowledge-base representation is therefore:

- **Disease:** isolated congenital digital clubbing, MONDO:0007343.
- **Gene:** ***HPGD***.
- **Inheritance:** autosomal recessive.
- **Defining variant:** NM_000860.6:c.577T>C, p.(Ser193Pro), ClinVar Variation ID 7920.
- **Core phenotypes:** congenital bilateral clubbing of fingers and toes, broad/thick hyperconvex nails.
- **Mechanism:** partial 15-PGDH loss → impaired PGE2 degradation → chronic PGE2 excess → inferred distal vascular/fibroblast activation and connective-tissue expansion.
- **Major exclusions:** periostosis, pachydermia, arthritis, systemic illness.
- **Prevalence:** unknown.
- **Treatment:** observation and reassurance; COX-2 inhibition remains indirect PHO evidence rather than established therapy.
- **Evidence quality:** strong segregation for one pedigree, moderate pathway evidence, limited replication and natural-history evidence.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 9 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007343` (3 mentions) - the report calls it "Mondo"; MONDO calls it **isolated congenital digital clubbing**
- `HP:0100759` (1 mention) - the report calls it "All fingernails in 11/11 affected members of the key pedigree"; HP calls it **Clubbing of fingers**
- `HP:0100760` (1 mention) - the report calls it "All toenails in 11/11 in the key pedigree"; HP calls it **Clubbing of toes**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `Rhea`, `Taxon`, `MMRRC`.