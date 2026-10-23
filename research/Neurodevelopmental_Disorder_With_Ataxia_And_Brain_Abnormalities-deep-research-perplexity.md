---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-22T14:58:13.518467'
end_time: '2026-10-22T15:01:13.005775'
duration_seconds: 179.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Ataxia And Brain Abnormalities
  mondo_id: MONDO:0978300
  category: Mendelian
  causal_genes: PTPMT1
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 56
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 16
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 66
  verified: 62
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0978300
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with ataxia and brain abnormalities
  labels_variant: 5
  unresolvable_prefixes:
  - OMIM
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Ataxia And Brain Abnormalities
- **MONDO ID:** MONDO:0978300 (if available)
- **Causal gene(s):** PTPMT1
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

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Ataxia And Brain Abnormalities** covering all of the
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

# Neurodevelopmental disorder with ataxia and brain abnormalities  
**MONDO:0978300 | OMIM:621199 | causal gene: *PTPMT1***

## Executive summary

Neurodevelopmental disorder with ataxia and brain abnormalities—abbreviated **NEDAXBA**—is a newly delineated, autosomal-recessive primary mitochondrial disease caused by **biallelic pathogenic variants in *PTPMT1***. The causal gene encodes a mitochondrial-inner-membrane phosphatase required for de novo cardiolipin synthesis. Loss of PTPMT1 lowers cardiolipin, disturbs mitochondrial membrane architecture and respiratory-chain assembly, and impairs oxidative phosphorylation, particularly affecting the developing nervous system. The defining study, published online on **30 August 2024** and in print in February 2025, described only **six affected individuals from three consanguineous families**, so prevalence, penetrance, full natural history, and genotype–phenotype correlations remain uncertain (Falabella et al., PMID:39279645; DOI: [10.1093/brain/awae268](https://doi.org/10.1093/brain/awae268)). [90][18]

The established clinical spectrum includes neonatal- or infantile-onset developmental delay, progressive microcephaly, ataxia, nystagmus, spasticity, developmental regression, epilepsy, hearing loss, optic atrophy, bulbar dysfunction, and variable MRI abnormalities including cerebellar atrophy, corpus-callosum thinning, hypomyelination, and white-matter signal abnormalities. Evidence is presently based on a very small human cohort, patient fibroblast and muscle studies, cellular rescue experiments, and knockout zebrafish and mouse models—not on population-level epidemiology or clinical trials. [59][90]

---

## 1. Disease information

### Definition and classification

NEDAXBA is a **Mendelian, autosomal-recessive neurodevelopmental and primary mitochondrial disorder**. Its defining molecular lesion is biallelic loss or severe reduction of PTPMT1 function, which compromises cardiolipin metabolism and mitochondrial oxidative phosphorylation. It should not be confused with similarly named disorders caused by other ataxia or structural-brain-abnormality genes. [90]

### Identifiers and names

| Resource | Identifier or term | Status/interpretation |
|---|---|---|
| MONDO | **MONDO:0978300** | Disease-specific MONDO identifier |
| OMIM phenotype | **OMIM:621199** | Neurodevelopmental disorder with ataxia and brain abnormalities |
| OMIM gene | **OMIM:609538** | *PTPMT1* |
| MedGen | **C6012724** | NEDAXBA concept |
| Causal gene | ***PTPMT1*** | Protein tyrosine phosphatase mitochondrial 1 |
| HGNC | **HGNC:26965** | Approved gene identifier |
| NCBI Gene | **114971** | Human *PTPMT1* |
| Ensembl | **ENSG00000110536** | Human gene |
| Cytogenetic location | **11p11.2** | GRCh38 chromosome 11 |
| KEGG disease grouping | H02470 | Neurodevelopmental disorder with structural brain abnormalities |
| ICD-11 | No disease-specific code identified; **LD90.Y** is a possible broad “other specified” developmental-disorder category | Not a validated disease-specific coding assignment |
| ICD-10 | No disease-specific code | Phenotype-based coding would be necessary |
| Orphanet | No dedicated disease entry identified | Very recently described condition |
| MeSH | No disease-specific descriptor identified | Index under mitochondrial diseases, neurodevelopmental disorders, ataxia, etc. |

MedGen recognizes the synonyms **“Neurodevelopmental disorder with ataxia and brain abnormalities”** and **“NEDAXBA,”** and links the condition to MONDO:0978300, OMIM:621199, and *PTPMT1*. [59] The gene is at 11p11.2 and has NCBI Gene ID 114971. [31]

### Evidence provenance

The clinical description is aggregated from:

- Six individually phenotyped patients in three families;
- WES/WGS and segregation studies;
- Patient-derived skin fibroblasts;
- Skeletal muscle from one patient;
- Dry-blood-spot lipid analysis;
- RNA sequencing and quantitative PCR;
- Wild-type complementation/rescue assays;
- CRISPR knockout zebrafish;
- Earlier mouse knockout studies.

This is therefore **individual-level primary research subsequently aggregated into OMIM, MedGen, MONDO, ClinVar, PanelApp, and related resources**, not an EHR-derived epidemiological phenotype.

### Defining abstract quotation

Falabella et al. stated:

> “Here, we report six individuals, from three independent families, harbouring biallelic variants in *PTPMT1*, a mitochondrial tyrosine phosphatase required for de novo cardiolipin biosynthesis.”

They concluded:

> “loss of *PTPMT1* function is associated with a new autosomal recessive PMD caused by impaired cardiolipin metabolism.”

(Published online 30 August 2024; PMID:39279645.) [18][90]

---

## 2. Etiology

### Primary cause

The disease is caused by **germline biallelic *PTPMT1* variants** that reduce functional PTPMT1 protein:

1. **NM_175732.3:c.65A>C, p.(Tyr22Ser)** — homozygous missense variant.
2. **NM_175732.3:c.255G>C, p.(Gln85His)** — homozygous exonic splice-altering variant at the last nucleotide of exon 2.

Both were absent from gnomAD v3 in the defining study. The c.255G>C variant produces multiple abnormal transcripts and nonsense-mediated decay, making splice loss of function more important than the nominal p.Gln85His substitution. [18]

### Risk factors

| Factor | Evidence and interpretation |
|---|---|
| Biallelic pathogenic *PTPMT1* genotype | Necessary established genetic cause |
| Parental carrier status | Each child of two heterozygous carriers has a theoretical 25% recurrence risk per pregnancy |
| Consanguinity | Present in all three reported pedigrees; increases the probability of homozygosity for rare recessive alleles |
| Shared ancestry | Families 2 and 3 shared a haplotype around c.255G>C, suggesting distant common ancestry |
| Sex | Five males and one female were reported, but the cohort is far too small to infer sex-specific risk |
| Environmental exposure | No causal environmental factor established |
| Maternal/paternal age | No association established |
| Family history | Multiple affected siblings or relatives may indicate recessive segregation |

### Protective factors

No validated genetic or environmental protective factors have been identified. Heterozygous carriers were apparently unaffected, but this is evidence for recessive inheritance rather than a protective effect.

### Gene–environment interaction

No disease-specific gene–environment interaction has been demonstrated. Mitochondrial energetic stress could plausibly worsen illness during infection, fasting, anesthesia, fever, or poor nutrition, but that is extrapolated from general mitochondrial-disease management rather than proven for NEDAXBA. One patient died following severe lower-respiratory infection, but this single observation does not prove a specific interaction.

---

## 3. Phenotypes

### Human phenotype summary

Frequencies below are calculated from the six reported individuals and should not be treated as population estimates.

| Phenotype | Type and HPO suggestion | Observed frequency | Onset/course and severity | Functional/QOL effect |
|---|---|---:|---|---|
| Global developmental delay | Symptom/sign; **HP:0001263** | 6/6 (100%) | Neonatal/infantile; mild to severe; sometimes progressive/regressive | Delayed sitting, standing, walking, speech, and learning |
| Microcephaly | Physical sign; **HP:0000252** | 5/6 (83%) | Usually postnatal/progressive; as low as −4.8 SD | Marker of impaired brain growth |
| Cerebellar ataxia | Neurologic sign; **HP:0001251** | 5/6 (83%) | Infantile/early childhood; persistent | Impaired balance, supported standing, inability to walk |
| Bulbar dysfunction | Neurologic sign; **HP:0001283** or HP:0002093 dysphagia | 5/6 (83%) | Infantile/childhood; variable | Feeding and airway-protection difficulties |
| Facial dysmorphism | Physical manifestation; **HP:0001999** | 5/6 (83%) | Congenital/childhood | Mainly diagnostic; direct QOL effect uncertain |
| Nystagmus | Clinical sign; **HP:0000639** | 4/6 (67%) | Often presenting during infancy | Visual instability and impaired motor coordination |
| Spasticity/hypertonia | Sign; **HP:0001257**, HP:0001276 | Approximately 4/6 (67%) | Infantile/childhood, sometimes progressive | Contracture risk; worsened mobility and caregiving burden |
| Developmental regression | Symptom; **HP:0002376** | 3/6 (50%) | From approximately 18–22 months in reported cases | Loss of standing, speech, or command response |
| Optic atrophy | Sign; **HP:0000648** | 3/6 (50%) | Childhood; variable | Visual impairment |
| Epileptic seizures | Symptom/sign; **HP:0001250** | 2/6 (33%) | 6 months or 6 years in the two cases | Treatment and safety burden; seizures became controlled |
| Sensorineural hearing loss | Sign; **HP:0000407** | 2/6 (33%) | Neonatal or childhood; severe in reported cases | Major communication and developmental impact |
| Hypotonia | Sign; **HP:0001252** | At least 1/6; neonatal | May evolve toward spasticity | Delayed motor acquisition |
| Feeding difficulty | Symptom; **HP:0011968** | At least 3/6 | Infantile/childhood | Aspiration and malnutrition risk; one gastrostomy |
| Vomiting | Symptom; **HP:0002013** | 1/6 | Chronic | Required gastrostomy temporarily |
| Hepatomegaly/elevated transaminases | Sign/laboratory; **HP:0002240**, HP:0002910 | 1/6 | Neonatal/childhood | Possible variant-specific multisystem involvement |
| Exercise intolerance/fatigue | Symptom; **HP:0003546** | 1/6 | Childhood | Reduced endurance |
| Behavioral disorder | Behavioral; oppositional behavior, possible **HP:0000717** | 1/6 | Childhood | Social and educational burden |

Clinical features and subject-level observations are from Falabella et al. (PMID:39279645). [18]

### Neuroimaging phenotypes

| MRI phenotype | HPO suggestion | Frequency/notes |
|---|---|---|
| Cerebellar atrophy | **HP:0001272** | 3/6; progressive in S2 and S5 |
| Thin/hypoplastic corpus callosum | **HP:0002079** | 2/6 |
| White-matter signal abnormality | **HP:0002500** | At least 3/6 |
| Hypomyelination | **HP:0003429** | Diffuse in S2 |
| Cerebral/cortical atrophy | **HP:0002059** | S4 |
| Dilated lateral ventricles | **HP:0002119** | S3 and S5 |
| Brainstem atrophy | **HP:0007366** or specific pons/medulla terms | S1 |
| Normal early MRI | — | S6 at nine months, illustrating age dependence |

Five of six individuals had an abnormal MRI at the reported assessment; the youngest had a normal MRI at nine months. [18]

### Laboratory phenotypes

- Venous lactate ranged from normal to mildly elevated; it is **not a sensitive rule-out test**.
- Creatine kinase was normal in all six patients.
- S1 had approximately 50% lower muscle complex-I activity.
- S1 muscle had an approximately 70% reduction in cardiolipin species 72:8.
- Dry blood spots from S1 and S5 had reduced total cardiolipin.
- No disease-specific validated clinical biomarker threshold exists. [18]

No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study has been published.

---

## 4. Genetic and molecular information

### Gene/protein

| Attribute | Annotation |
|---|---|
| Gene | ***PTPMT1*** |
| Full name | Protein tyrosine phosphatase mitochondrial 1 |
| HGNC | HGNC:26965 |
| NCBI Gene | 114971 |
| OMIM gene | 609538 |
| Ensembl | ENSG00000110536 |
| Location | 11p11.2 |
| Disease transcript used | NM_175732.3 |
| Protein type | Mitochondrial dual-specificity/lipid phosphatase |
| Principal substrate | Phosphatidylglycerophosphate |
| Product | Phosphatidylglycerol |
| Pathway | De novo cardiolipin biosynthesis |
| Compartment | Matrix-facing side of the inner mitochondrial membrane |

PTPMT1 dephosphorylates phosphatidylglycerophosphate to phosphatidylglycerol, the committed/penultimate segment of cardiolipin biosynthesis. Whole-body loss in mice markedly depletes cardiolipin and causes embryonic lethality (PMID:21641550). [89]

### Reported disease variants

| Variant | Patients | Variant class | Functional consequence | Population data | Current interpretation |
|---|---:|---|---|---|---|
| NM_175732.3:c.65A>C, p.(Tyr22Ser) | 1 | Missense | Reduced steady-state protein; likely impaired stability/localization; partial/hypomorphic loss of function | Absent from gnomAD v3 in the report | Strong candidate likely pathogenic; functional and segregation support, but only one family |
| NM_175732.3:c.255G>C, p.(Gln85His) | 5 | Exonic splice-region SNV, nominal missense | Cryptic intron retention, exon skipping, premature termination, reduced RNA, nonsense-mediated decay | Absent from gnomAD v3 | ClinVar pathogenic, Variation ID **3899900**; functionally demonstrated splice loss of function |

ClinVar presently lists c.255G>C as pathogenic for NEDAXBA. [74] Earlier work had conservatively called it a VUS but demonstrated intron retention and partial engineered-U1 rescue; the later complete human-genetic and rescue evidence supports pathogenicity (PMID:39279645). [75][78]

### Germline/somatic status and inheritance

Both reported variants are **constitutional germline homozygous variants**. No somatic disease mechanism is known.

### Modifier genes, epigenetics, structural variation

- No modifier gene has been established.
- No disease-specific methylation signature or chromatin abnormality is known.
- No pathogenic CNV, translocation, inversion, or aneuploidy has been linked specifically to this phenotype.
- No repeat-expansion mechanism is implicated.
- Copy-number analyses in the discovery study did not identify an alternative causal lesion.

---

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, occupational exposure, smoking, alcohol, diet, or infectious agents cause NEDAXBA. It is not infectious or transmissible.

Practical mitochondrial-care precautions—avoiding prolonged fasting, dehydration, hyperthermia, and delayed treatment of infection—are reasonable but **not disease-specific evidence-based preventive therapies**. Likewise, exercise may need to be individualized because of ataxia, spasticity, fatigue, and possible mitochondrial intolerance.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic *PTPMT1* pathogenic variants lead to reduced or unstable PTPMT1 protein, or aberrant splicing with nonsense-mediated decay.**
2. **Reduced PTPMT1 phosphatase activity leads to impaired conversion of phosphatidylglycerophosphate to phosphatidylglycerol.**
3. **Impaired phosphatidylglycerol production leads to deficient or compositionally abnormal cardiolipin in the inner mitochondrial membrane.**
4. **Abnormal cardiolipin leads to altered cristae/membrane architecture and mitochondrial fragmentation.**
5. **Membrane disruption leads to defective respiratory-chain complex I and IV assembly/activity and impaired oxidative phosphorylation.**
6. **OXPHOS impairment leads to bioenergetic stress, especially in metabolically vulnerable developing neural precursor/stem cells.**
7. **In mouse neural precursors, bioenergetic stress leads to AMPK–p19/p21 activation, cell-cycle arrest, and increased apoptosis; applying this exact downstream pathway to human NEDAXBA is mechanistically plausible but inferred.**
8. **Impaired precursor function and neuronal development lead to reduced brain growth, white-matter abnormalities, corpus-callosum thinning, and cerebellar/brainstem atrophy.**
9. **These structural and cellular abnormalities result in developmental delay/regression, microcephaly, ataxia, nystagmus, spasticity, epilepsy, hearing loss, optic atrophy, and bulbar dysfunction.**

### Upstream molecular defect

PTPMT1 is a mitochondrial phosphatidylglycerophosphatase. The foundational mouse and cell study found PGP accumulation, decreased phosphatidylglycerol/cardiolipin, abnormal mitochondrial morphology, and impaired respiration; catalytically active PTPMT1 partially rescued the lipid defect (PMID:21641550). [89]

Suggested terms:

- **GO:0006656** phosphatidylcholine biosynthetic process is not the correct primary term; prefer cardiolipin-specific annotations where available.
- **GO:0032049** cardiolipin biosynthetic process.
- **GO:0006644** phospholipid metabolic process.
- **GO:0016311** dephosphorylation.
- **GO:0005739** mitochondrion.
- **GO:0005743** mitochondrial inner membrane.
- **GO:0005759** mitochondrial matrix.
- Chemical entities: phosphatidylglycerophosphate, phosphatidylglycerol, and cardiolipin; cardiolipin is **CHEBI:28494**.

### Mitochondrial consequences demonstrated in patients

Patient fibroblasts showed reduced PTPMT1 protein and fragmented, shortened mitochondria. Expression of wild-type *PTPMT1* restored mitochondrial morphology, providing direct rescue evidence. Early-passage fibroblasts showed reduced NDUFB8, SDHB, and COXII, although this finding was not stable at later passages. Muscle from S1 showed complex-I deficiency and markedly reduced cardiolipin 72:8. [18]

Suggested GO terms:

- Mitochondrial organization — **GO:0007005**
- Mitochondrial respiratory-chain complex assembly — **GO:0033108**
- Oxidative phosphorylation — **GO:0006119**
- Aerobic respiration — **GO:0009060**
- ATP metabolic process — **GO:0046034**
- Mitochondrial fission — **GO:0000266**
- Intrinsic apoptotic signaling — **GO:0097193**

### Neural developmental vulnerability

Conditional deletion of *Ptpmt1* in mouse neural precursor cells blocked postnatal cerebellar development and impaired cerebral development. Pyruvate oxidation was reduced, ATP fell by approximately 50%, and bioenergetic stress activated AMPK-p19/p21-associated cell-cycle arrest. The phenotype included ataxia, tremor, and impaired motor coordination (PMCID:PMC6191298). [13]

Relevant cell types and suggested CL terms include:

- Neural stem cell — **CL:0000047**
- Neural progenitor cell — **CL:0011020**
- Neuron — **CL:0000540**
- Cerebellar granule neuron — **CL:0001031**
- Bergmann glial cell — **CL:0000644**
- Oligodendrocyte — **CL:0000128**, inferred from hypomyelination rather than directly demonstrated
- Skeletal muscle cell — **CL:0000188**
- Cardiomyocyte — **CL:0000746**, supported in cardiac models but not yet a prominent human phenotype

### Metabolism and immune involvement

Altered cardiolipin and OXPHOS are established. PTPMT1 also influences mitochondrial pyruvate utilization and fuel selection in experimental systems. No primary immune deficiency, autoimmunity, or chronic neuroinflammatory mechanism has been demonstrated in NEDAXBA.

### Molecular profiling

Available disease-specific profiling includes:

- RNA-seq: aberrant *PTPMT1* splicing and reduced transcript abundance;
- qPCR: marked transcript loss for c.255G>C;
- immunoblotting: reduced PTPMT1 and selected OXPHOS subunits;
- lipidomics: reduced total cardiolipin and cardiolipin 72:8;
- blue-native electrophoresis: impaired complex-I and IV assembly in zebrafish;
- no published disease-specific single-cell, spatial-transcriptomic, proteomic, epigenomic, or integrated multi-omics atlas.

---

## 7. Anatomical structures affected

| Level | Structure/compartment | Evidence and ontology suggestion |
|---|---|---|
| Organ | Brain; **UBERON:0000955** | Primary affected organ |
| Region | Cerebellum; **UBERON:0002037** | Ataxia and cerebellar atrophy |
| Region | Cerebral cortex; **UBERON:0000956** | Developmental impairment/cortical atrophy |
| Region | Corpus callosum; **UBERON:0002336** | Thin/hypoplastic in two patients |
| Region | Brainstem; **UBERON:0002298** | Pons/medulla atrophy and bulbar dysfunction |
| Tissue | Cerebral white matter; **UBERON:0002437** | Hypomyelination and signal abnormality |
| Sensory organ | Optic nerve; **UBERON:0000962** | Optic atrophy |
| Sensory organ | Inner ear/cochlea; **UBERON:0001844/0001851** | Sensorineural hearing loss |
| Tissue | Skeletal muscle; **UBERON:0001134** | Complex-I and cardiolipin abnormality in S1 |
| Organ | Liver; **UBERON:0002107** | Hepatomegaly/transaminase elevation in one patient |
| Subcellular | Mitochondrion; **GO:0005739** | Central disease compartment |
| Subcellular | Inner mitochondrial membrane; **GO:0005743** | PTPMT1 localization and cardiolipin synthesis |
| Subcellular | Mitochondrial crista; **GO:0030061** | Disrupted in experimental models |

MRI abnormalities are generally bilateral/diffuse; no consistent lateralization has been described.

---

## 8. Temporal development

- **Onset:** birth to 15 months in the reported cohort.
- **Initial manifestations:** neonatal hypotonia or systemic illness in some; otherwise developmental delay and nystagmus in late infancy.
- **Course:** chronic and lifelong; slow to moderate progression.
- **Regression:** documented in three children, beginning around 18–22 months.
- **Microcephaly:** often progressive/postnatal.
- **Cerebellar atrophy:** can emerge or progress on serial MRI.
- **Epilepsy:** ranged from six months to six years; seizures were controllable in the two reported patients.
- **Advanced course:** severe motor dependence, bulbar dysfunction, feeding difficulties, and infection vulnerability may occur.
- **Remission:** no disease remission documented. Seizures may remit with treatment.
- **Critical period:** prenatal and early postnatal neurodevelopment is probably the principal period of vulnerability. Mouse experiments demonstrate a stage-specific requirement for PTPMT1 in postnatal cerebellar development. [1][13]

No validated clinical staging system exists.

---

## 9. Inheritance and population

### Inheritance

- **Autosomal recessive**
- All six reported patients were homozygous.
- Parents were consanguineous in all three pedigrees.
- Both sexes can be affected.
- For two confirmed heterozygous parents: 25% affected, 50% carrier, and 25% unaffected non-carrier probability for each pregnancy.

### Penetrance and expressivity

Penetrance for individuals with two clearly loss-of-function alleles appears high, but only six patients are known, so it cannot be quantified. Expressivity is clearly variable: S1 with p.Tyr22Ser had milder cognitive/motor disease and no microcephaly or cerebellar atrophy, whereas c.255G>C was generally associated with more severe neurological disease. This possible genotype–phenotype relationship remains provisional.

### Epidemiology

No prevalence, incidence, carrier-frequency, or population-registry data are available. Six patients from three families do not permit calculation per 100,000 population.

### Demographics

- Reported ancestry: Kurdish, Turkish, and Iraqi.
- Sex: five males, one female.
- Ages at report: one to sixteen years.
- One patient died at sixteen.
- c.255G>C occurred in Turkish and Iraqi families sharing a haplotype, suggesting a possible regional founder allele, but no founder effect has been formally established. [18]

There is no evidence for anticipation, repeat expansion, or sex-linked inheritance. Germline mosaicism has not been reported but cannot be categorically excluded in genetic counseling.

---

## 10. Diagnostics

### When to suspect NEDAXBA

Consider *PTPMT1*-related disease in a child with:

- Infantile developmental delay with progressive microcephaly;
- Nystagmus and cerebellar ataxia;
- Mixed hypotonia followed by spasticity;
- Developmental regression;
- Hearing loss, optic atrophy, or bulbar dysfunction;
- Cerebellar atrophy, thin corpus callosum, hypomyelination, or white-matter abnormalities;
- Normal CK and normal or mildly elevated lactate;
- Consanguinity or similarly affected siblings.

### Recommended evaluation

1. Neurologic and developmental examination.
2. Growth and serial head-circumference measurements.
3. Brain MRI, including white-matter and cerebellar assessment.
4. EEG if seizures or regression are present.
5. Audiology/brainstem auditory evoked responses.
6. Ophthalmology, optic-nerve examination, and visual evoked potentials.
7. Swallow and feeding evaluation.
8. Plasma lactate, blood gas, CK, liver enzymes, glucose, amino acids, acylcarnitines, and urine organic acids.
9. Cardiac examination, ECG, and echocardiography when clinically indicated, despite the absence of cardiac disease in the original six patients.
10. Molecular confirmation.

A normal lactate, CK, metabolic screen, or early MRI does not exclude the condition.

### Genetic-testing strategy

- **Preferred first line:** trio WES or WGS, or a comprehensive mitochondrial/neurodevelopmental/ataxia panel containing *PTPMT1*.
- **Variant confirmation:** Sanger sequencing and familial segregation.
- **Splice assessment:** patient RNA/cDNA analysis for c.255G>C or novel splice-region variants.
- **Deletion/duplication analysis:** include exon-level CNV calling if sequencing is nondiagnostic.
- **WGS:** useful for intronic, regulatory, structural, and poorly captured exonic variants.
- **CMA:** useful for a broader developmental-disability differential, but not expected to detect the known SNVs.
- **Karyotype/FISH:** low yield unless a chromosomal syndrome is independently suspected.
- **mtDNA sequencing:** appropriate in an unresolved mitochondrial presentation but does not test the nuclear *PTPMT1* cause.
- **Repeat-expansion testing:** not disease-specific.

NCBI currently notes that a dedicated GeneReviews chapter and listed GTR disease-specific test were not available in its gene summary. [124]

### Functional confirmation

Potential research or specialist tests include:

- PTPMT1 immunoblot;
- fibroblast RNA sequencing/qPCR;
- cardiolipin lipidomics in blood, fibroblast, or muscle;
- respiratory-chain enzyme analysis;
- blue-native PAGE;
- mitochondrial morphology assays;
- complementation with wild-type *PTPMT1*.

These are not yet standardized diagnostic criteria.

### Differential diagnosis

| Disorder/group | Distinguishing considerations |
|---|---|
| Barth syndrome, *TAZ* | Cardiolipin remodeling defect, cardiomyopathy, neutropenia, 3-methylglutaconic aciduria, X-linked |
| *SERAC1*-related MEGDEL | Dystonia/deafness, basal-ganglia lesions, 3-methylglutaconic aciduria |
| *PGS1*, *CRLS1*, *TAMM41* disorders | Other cardiolipin-biosynthesis defects; phenotype and biochemical profile overlap |
| *OPA1*, *ACO2*, *PARS2*, *HPDL* disorders | Optic atrophy/ataxia/spasticity/mitochondrial disease |
| *EXOSC3/EXOSC5* disorders | Pontocerebellar involvement, motor-neuron phenotype |
| Congenital disorders of glycosylation | Multisystem developmental disease and cerebellar atrophy |
| Perinatal hypoxic-ischaemic injury | May explain neonatal findings but not recessive segregation, progressive microcephaly, or cardiolipin defect |
| Cerebral palsy | Usually nonprogressive and lacks the molecular/mitochondrial signature |

No standardized clinical diagnostic criteria or newborn screen exists.

---

## 11. Outcome and prognosis

Outcome is variable and inadequately defined:

- S1 was alive at 14 with mild intellectual disability, independent walking, fatigue, hearing loss, and controlled epilepsy.
- S2 never walked, depended on others for all daily activities, and died at 16 after a severe lower-respiratory infection.
- Other patients had variable motor delay, regression, spasticity, ataxia, visual impairment, and feeding difficulty.
- No five- or ten-year survival estimates exist.
- Life expectancy cannot yet be estimated.
- Long-term disability may involve mobility, communication, vision, hearing, feeding, learning, and self-care.

Potential adverse prognostic features—currently unvalidated—include early severe hypotonia, profound developmental delay, regression, bulbar dysfunction, progressive cerebellar atrophy, and a severe splice/LoF genotype. There is no validated prognostic biomarker.

---

## 12. Treatment

### Current standard

There is **no approved disease-modifying therapy, gene therapy, RNA therapy, or PTPMT1 replacement treatment**. No NEDAXBA-specific interventional trial was identified. Management is symptomatic and multidisciplinary.

| Intervention | Indication and comments | Suggested NCIT intervention concept |
|---|---|---|
| Antiseizure medication | Treat according to seizure type; valproate controlled seizures in S2, but mitochondrial specialists should assess hepatic/metabolic risk individually | Anticonvulsant therapy |
| Physical therapy | Ataxia, weakness, spasticity, posture, contracture prevention | Physical therapy |
| Occupational therapy | Adaptive equipment and activities of daily living | Occupational therapy |
| Speech/language therapy | Communication delay; augmentative communication where required | Speech therapy |
| Feeding/swallow therapy | Dysphagia and aspiration risk | Swallowing therapy |
| Gastrostomy | Severe or unsafe oral feeding; used temporarily in S1 | Gastrostomy |
| Spasticity management | Stretching, orthoses, oral antispastic agents, or focal botulinum toxin according to standard practice | Antispastic therapy |
| Hearing aids/cochlear assessment | Sensorineural hearing loss | Hearing rehabilitation |
| Low-vision support | Optic atrophy or visual pathway dysfunction | Vision rehabilitation |
| Nutrition and hydration support | Prevent malnutrition, dehydration, and prolonged fasting | Nutritional support |
| Respiratory care | Vaccination, airway-clearance support, and prompt infection treatment in bulbar dysfunction | Supportive care |
| Educational/behavioral services | Intellectual, language, and behavioral impairment | Developmental intervention |

### Experimental approaches

An engineered U1 snRNA partially corrected c.255G>C mis-splicing in a minigene/HeLa-cell system. This is an important proof of principle but not a patient-ready therapy; residual p.Gln85His protein function and delivery to the nervous system remain unresolved. [115]

Other hypothetical strategies include:

- AAV-mediated *PTPMT1* replacement;
- variant-specific splice-switching oligonucleotides or engineered U1 snRNA;
- small molecules that improve cardiolipin homeostasis;
- mitochondrial membrane or OXPHOS support.

None has demonstrated efficacy in affected humans. Alexidine is a PTPMT1 **inhibitor**, not a treatment for PTPMT1 deficiency, and could be mechanistically undesirable in this disease. [109]

No pharmacogenomic guideline specific to NEDAXBA exists.

---

## 13. Prevention

### Primary prevention

The occurrence of disease in a genetically predisposed embryo cannot be prevented by lifestyle modification or vaccination. Reproductive options for known carrier couples include:

- Preimplantation genetic testing for monogenic disease;
- Chorionic-villus sampling;
- Amniocentesis;
- Donor gametes;
- Adoption;
- Natural conception with or without prenatal testing.

### Secondary prevention

- Cascade testing of adult relatives;
- Carrier testing for the familial variant;
- Early molecular diagnosis in symptomatic siblings;
- Surveillance for hearing, vision, swallowing, seizures, spasticity, and developmental regression.

There is no population newborn screening or general-population carrier-screening recommendation for *PTPMT1*.

### Tertiary prevention

- Early rehabilitation;
- Aspiration assessment;
- Nutritional support;
- Vaccination and prompt infection management;
- Seizure control;
- Contracture and scoliosis prevention;
- Communication and sensory supports.

For confirmed carrier parents, recurrence risk is 25% per pregnancy. Genetic counseling should emphasize the limited natural-history data and variable expressivity.

---

## 14. Other species and natural disease

No naturally occurring veterinary disease confidently attributable to *PTPMT1* variants has been documented in OMIA or the cited literature. Therefore:

- There is no established affected breed or VBO term.
- There is no zoonotic potential.
- There is no cross-species transmission.
- Cross-species relevance derives from conserved experimental biology, not naturally transmissible or spontaneous animal disease.

Orthologs include:

| Species | Taxon ID | Ortholog/resource |
|---|---:|---|
| Human, *Homo sapiens* | 9606 | *PTPMT1*, NCBI Gene 114971 |
| Mouse, *Mus musculus* | 10090 | *Ptpmt1*, MGI:1913711 |
| Zebrafish, *Danio rerio* | 7955 | *ptpmt1*, ZFIN:ZDB-GENE-070112-272 |
| Fruit fly, *Drosophila melanogaster* | 7227 | *Ptpmt1*, FlyBase:FBgn0039111 |

ZFIN explicitly links the zebrafish ortholog to human NEDAXBA. [119] The Drosophila ortholog is predicted to participate in cardiolipin biosynthesis and has phosphatidylglycerophosphatase activity. [36]

---

## 15. Model organisms

### Zebrafish disease model

Falabella et al. generated a CRISPR/Cas9 **4-bp deletion in exon 3** of zebrafish *ptpmt1*, predicted to cause premature truncation.

At 19 days post-fertilization, homozygous mutants showed:

- Reduced body length;
- Reduced head area;
- Failure to inflate the anterior swim-bladder chamber;
- Reduced total cardiolipin and cardiolipin 72:8;
- Reduced assembled complexes I and IV;
- Approximately 50% lower complex-I activity;
- Approximately 30% lower complex-IV activity;
- Normal complex-II assembly, complex-V activity, and citrate-synthase activity.

This model strongly recapitulates growth impairment, microcephaly-like reduced head size, cardiolipin deficiency, and OXPHOS dysfunction, but it does not capture the complete human behavioral, speech, hearing, vision, or long-term degenerative phenotype. [9][90]

### Mouse models

#### Whole-body knockout

Whole-body *Ptpmt1* knockout is lethal before approximately embryonic day 8.5. Knockout embryonic fibroblasts accumulate PGP, lose cardiolipin, have abnormal cristae and fragmented mitochondria, and show impaired respiration (PMID:21641550). [89][128]

#### Neural conditional knockout

Nestin-lineage deletion:

- Blocked normal cerebellar foliation and lamination;
- Compromised cerebral development;
- Caused ataxia, tremor, and impaired coordination;
- Reduced pyruvate oxidation and ATP;
- Produced neural-precursor cell-cycle arrest and apoptosis;
- Disrupted Bergmann-glial development.

This is the most anatomically relevant mammalian model but is more severe than most reported human cases and involves engineered near-complete tissue-specific loss. [1][13]

#### Cardiac conditional knockout

Cardiac deletion impairs cardiolipin synthesis, mitochondrial morphogenesis, complex-I respiration, and embryonic heart development (PMID:34339306). [92] Cardiac surveillance is therefore biologically reasonable, although no overt cardiomyopathy was reported in the six human patients.

### Cellular models

- Patient dermal fibroblasts;
- Mouse embryonic fibroblasts;
- HeLa/minigene splice assays;
- Wild-type *PTPMT1* complementation;
- Potential future patient-derived iPSC neurons or cerebellar organoids.

The defining study specifically proposed neuronal reprogramming/iPSC work because fibroblast OXPHOS abnormalities diminished with passage, highlighting the limitations of fibroblasts as a neurological model. [18]

---

# Evidence assessment and research gaps

The gene–disease relationship is supported by recessive segregation, absence of variants from population controls, RNA/protein effects, patient-tissue cardiolipin and respiratory-chain abnormalities, wild-type rescue, and a concordant knockout-zebrafish phenotype. Nevertheless, current evidence comes from only six people and two pathogenic alleles. Genomics England therefore classified *PTPMT1* as **moderate/amber evidence** on several relevant panels as of 2026, pending independent families and broader replication. [47][48]

Major unmet needs are:

1. Additional unrelated patients and allelic diversity;
2. Prospective natural-history data;
3. Standardized developmental and ataxia outcomes;
4. Validated blood or lipidomic biomarkers;
5. Longitudinal cardiac, hearing, vision, respiratory, and MRI surveillance;
6. Patient-derived neuronal and organoid studies;
7. Preclinical gene-replacement and splice-correction studies;
8. Epidemiological and carrier-frequency estimates.

## Key publications

- Falabella M, et al. **Biallelic PTPMT1 variants disrupt cardiolipin metabolism and lead to a neurodevelopmental syndrome.** *Brain*. Published online 30 August 2024; print February 2025;148(2):647–662. PMID: **39279645**. DOI: [10.1093/brain/awae268](https://doi.org/10.1093/brain/awae268). [18][90]
- Zhang J, et al. **Mitochondrial phosphatase PTPMT1 is essential for cardiolipin biosynthesis.** *Cell Metabolism*. 8 June 2011. PMID: **21641550**. URL: [https://pubmed.ncbi.nlm.nih.gov/21641550/](https://pubmed.ncbi.nlm.nih.gov/21641550/). [89]
- Xiao J, et al. **Structural and functional analysis of PTPMT1, a phosphatase required for cardiolipin synthesis.** *PNAS*. 19 July 2011. PMID: **21730175**. URL: [https://pubmed.ncbi.nlm.nih.gov/21730175/](https://pubmed.ncbi.nlm.nih.gov/21730175/). [94]
- Zheng H, et al. **Mitochondrial oxidation of the carbohydrate fuel is required for neural precursor/stem cell function and postnatal cerebellar development.** *Science Advances*. 10 October 2018. PMCID: **PMC6191298**. URL: [https://pmc.ncbi.nlm.nih.gov/articles/PMC6191298/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6191298/). [13]
- Chen Z, et al. **PTPMT1 Is Required for Embryonic Cardiac Cardiolipin Biosynthesis to Regulate Mitochondrial Morphogenesis and Heart Development.** *Circulation*. 3 August 2021. PMID: **34339306**. URL: [https://pubmed.ncbi.nlm.nih.gov/34339306/](https://pubmed.ncbi.nlm.nih.gov/34339306/). [92]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 16 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 66 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 7 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0978300` (3 mentions) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with ataxia and brain abnormalities**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002079` (1 mention) - the report calls it "Thin/hypoplastic corpus callosum"; HP calls it **Hypoplasia of the corpus callosum**, and lists "Hypoplastic corpus callosum" among its other names
- `HP:0002500` (1 mention) - the report calls it "White-matter signal abnormality"; HP calls it **Abnormal cerebral white matter morphology**, and lists "White matter abnormalities" among its other names
- `HP:0003429` (1 mention) - the report calls it "Hypomyelination"; HP calls it **CNS hypomyelination**
- `HP:0002059` (1 mention) - the report calls it "Cerebral/cortical atrophy"; HP calls it **Cerebral atrophy**
- `HP:0002119` (1 mention) - the report calls it "Dilated lateral ventricles"; HP calls it **Ventriculomegaly**, and lists "Dilated cerebral ventricles" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `MGI`.