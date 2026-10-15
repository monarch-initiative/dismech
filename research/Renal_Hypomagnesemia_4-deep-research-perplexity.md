---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-15T07:16:35.253436'
end_time: '2026-10-15T07:20:39.504559'
duration_seconds: 244.25
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Renal Hypomagnesemia 4
  mondo_id: MONDO:0012717
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
citation_count: 50
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 11
  validator_version: 0.3.0
term_validation:
  total_terms: 38
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 8
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0012717
    reported_labels:
    - MONDO
    ontology_label: renal hypomagnesemia 4
  - term_id: DOID:0060882
    reported_labels:
    - Disease Ontology
    ontology_label: renal hypomagnesemia 4
  - term_id: CL:4030016
    reported_labels:
    - Early DCT epithelial cell
    ontology_label: epithelial cell of early distal convoluted tubule
  - term_id: NCIT:C623
    reported_labels:
    - Evidence from unrelated refractory cases, not HOMG4
    ontology_label: Magnesium Sulfate
  labels_variant: 3
  unresolvable_prefixes:
  - ORPHA
  - Gene
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal Hypomagnesemia 4
- **MONDO ID:** MONDO:0012717 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Renal Hypomagnesemia 4** covering all of the
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

# Renal Hypomagnesemia 4 — comprehensive disease-characteristics report

**Disease:** Renal hypomagnesemia 4  
**Preferred molecular designation:** *EGF*-related primary renal hypomagnesemia with intellectual disability  
**MONDO:** MONDO:0012717  
**Disease class:** Mendelian renal tubular magnesium-transport disorder  
**Evidence status:** Exceptionally rare; the molecularly confirmed human evidence remains limited to **two affected sisters from one consanguineous Dutch family**. Consequently, apparent phenotype frequencies of 100% are not reliable population estimates. OMIM itself marks the phenotype with a question mark, reflecting the limited genetic evidence. [392]

---

## 1. Disease information

### 1.1 Definition and overview

Renal hypomagnesemia 4 (HOMG4) is an autosomal-recessive disorder in which defective basolateral targeting of pro-epidermal growth factor impairs EGF–EGFR stimulation of the apical magnesium channel TRPM6 in distal convoluted tubule cells. The resulting failure of renal magnesium conservation causes chronic hypomagnesemia, infantile generalized seizures, developmental delay, and moderate intellectual disability, while serum calcium and urinary calcium are characteristically normal. [113][391]

The landmark molecular study identified homozygous *EGF* c.3209C>T, p.(Pro1070Leu) in the two sisters. Its abstract summarized the core mechanism as: **“The mutation leads to impaired basolateral sorting of pro-EGF.”** It further linked inadequate renal EGFR stimulation to insufficient TRPM6 activation and magnesium loss. Human clinical, cell-biological, electrophysiologic, and pharmacologic evidence were included in that report. PMID: **17671655**; DOI: **10.1172/JCI31680**; published **August 1, 2007**. [113]

### 1.2 Identifiers and nomenclature

| Identifier/system | Identifier or name | Notes |
|---|---|---|
| MONDO | **MONDO:0012717** | Renal hypomagnesemia 4 |
| OMIM phenotype | **611718** | Hypomagnesemia 4, renal; HOMG4 |
| OMIM gene | **131530** | *EGF* |
| Disease Ontology | **DOID:0060882** | Renal hypomagnesemia 4 |
| Current Orphanet disease | **ORPHA:620368** | EGF-related primary hypomagnesemia with intellectual disability; prevalence listed as <1/1,000,000 |
| Historical Orphanet mapping | **ORPHA:34527** | Familial primary hypomagnesemia with normocalciuria and normocalcemia; now obsolete/group-level terminology |
| ICD-10-CM | **E83.4** | Disorders of magnesium metabolism; not disease-specific |
| ICD-11 | **GB90.4Y** | Other specified renal tubular dysfunction |
| MeSH | **D008275**, Magnesium Deficiency | No disease-specific MeSH descriptor; D008274 denotes magnesium itself |
| SNOMED CT | **80710001** | Primary hypomagnesemia; broader concept |
| UMLS | **C5681825** | EGF-related primary hypomagnesemia with intellectual disability |
| Gene | **HGNC:3229; NCBI Gene:1950; ENSG00000138798** | *EGF*, chromosome 4q25 |
| Protein | **UniProt P01133** | Pro-epidermal growth factor |

The current Orphanet entry gives infancy/childhood onset, absence of secondary hypocalcemia and obesity, and prevalence below one per million. [134] The DO definition and historical ontology cross-references include OMIM 611718, ICD-10-CM E83.4, and ORDO:34527. [391]

### 1.3 Synonyms

| Synonym/alternative name | Comment |
|---|---|
| Hypomagnesemia 4, renal | OMIM name |
| HOMG4 | Abbreviation |
| Renal hypomagnesemia type 4 | Common alternative |
| Isolated recessive renal hypomagnesemia | Historical clinical name |
| Autosomal-recessive isolated renal magnesium loss | Descriptive name |
| EGF-related primary hypomagnesemia | Molecular name |
| EGF familial primary hypomagnesemia | MONDO/NORD synonym |
| EGF-related primary hypomagnesemia with intellectual disability | Current Orphanet name |
| Normocalciuric renal hypomagnesemia due to *EGF* | Biochemical description |

These synonyms are consolidated in MONDO-linked resources and the current/historical Orphanet nomenclature. [394]

### 1.4 Data provenance

The disease entry is based on:

* **Individual-level human observations:** two sisters, originally reported clinically in 1987 and molecularly investigated in 2007.
* **Family segregation:** affected sisters, parents, unaffected siblings, and extended relatives.
* **Aggregate resources:** OMIM, MONDO, Orphanet, ClinVar, Disease Ontology, UniProt.
* **Experimental evidence:** HEK293 and polarized MDCK cells, rat-kidney immunohistochemistry, and a clinical pharmacologic analogue involving cetuximab-treated patients.

It is **not** based on an EHR cohort, population registry, randomized trial, or broad natural-history series.

---

## 2. Etiology

### 2.1 Primary causal factor

The established initiating lesion is homozygosity for the germline missense variant:

**NM_001963.6(*EGF*):c.3209C>T; NP_001954.2:p.(Pro1070Leu); rs121434567.**

The substitution affects the second proline in the cytoplasmic `PKNP`/PXXP basolateral-sorting motif of pro-EGF. It disrupts basolateral—but not apical—delivery/release in polarized epithelial cells. [257]

### 2.2 Risk and protective factors

| Factor class | Evidence and interpretation |
|---|---|
| Biallelic *EGF* p.Pro1070Leu | Primary demonstrated genetic cause; both affected sisters were homozygous |
| Heterozygosity | Parents, two unaffected sisters, and a paternal aunt were unaffected carriers, supporting recessive inheritance |
| Consanguinity | Parents were second cousins; increased the probability of homozygosity for the rare allele |
| Family history | Affected sibling or known carrier parents substantially increases Mendelian recurrence risk |
| Sex | No evidence of sex dependence; both known patients happened to be female |
| Age | Congenital genotype, with manifestations beginning in infancy |
| Low magnesium intake or gastrointestinal loss | Not causal, but expected to worsen magnesium depletion because renal conservation is impaired |
| Magnesium-wasting drugs | Diuretics, cisplatin, aminoglycosides, calcineurin inhibitors, and especially EGFR inhibitors may aggravate the biochemical defect |
| Alcohol misuse | Can worsen magnesium deficiency through low intake, gastrointestinal loss, and renal wasting |
| Adequate magnesium intake/replacement | Reduces deficiency and complication risk but does not correct the inherited trafficking defect |
| Genetic protective variants | None reported |
| Modifier genes | None established |

Loop and thiazide diuretics increase urinary magnesium loss, while prolonged PPI treatment, poor intake, alcoholism, and gastrointestinal disease may further lower magnesium status. [333] EGFR inhibitors are especially mechanistically relevant because cetuximab, panitumumab, and related drugs reproduce renal magnesium wasting by interrupting the same pathway. [336]

### 2.3 Gene–environment interaction

The genotype reduces the kidney’s reserve capacity to conserve magnesium. Accordingly, low dietary intake, diarrhea, vomiting, alcohol-associated depletion, or magnesium-wasting medication should produce a larger fall in serum magnesium than in an unaffected person. This interaction is physiologically plausible but has **not been studied directly in HOMG4 patients**.

Conversely, dietary magnesium restriction induces compensatory renal TRPM6 expression in wild-type mice; that compensation may be inadequate when upstream EGF–EGFR signaling is defective. [310]

No infectious, toxic, occupational, radiation, or immune cause of the Mendelian disorder has been identified.

---

## 3. Phenotypes

### 3.1 Human phenotype table

Frequencies below refer to the only two published molecularly confirmed patients and therefore must not be interpreted as robust estimates.

| Phenotype | Type | Onset/course/severity | Reported frequency | Suggested HPO term | Functional or quality-of-life impact |
|---|---|---|---:|---|---|
| Hypomagnesemia, serum 0.53–0.66 mmol/L | Laboratory abnormality | Chronic; moderate-to-severe | 2/2 | **HP:0002917 Hypomagnesemia** | Requires lifelong monitoring and likely replacement; predisposes to neurologic and cardiac complications |
| Inappropriate renal magnesium excretion | Laboratory/renal sign | Lifelong; persistent | 2/2 | **HP:0005567 Renal magnesium wasting** | Makes correction more difficult despite low serum magnesium |
| Fractional Mg excretion 4.8% and 3.6% | Laboratory abnormality | Persistent in tested adults | 2/2 | HP:0005567 | Confirms impaired tubular conservation |
| Generalized epileptic seizures | Neurologic symptom | Began in first year of life; recurrent but controlled with conventional antiseizure drugs | 2/2 | **HP:0001250 Seizure**; more specific **HP:0002197 Generalized-onset seizure** | Acute danger, medication burden, restrictions on activities |
| Psychomotor/global developmental delay | Developmental manifestation | Childhood; persistent | 2/2 | **HP:0001263 Global developmental delay** or **HP:0011343 Moderate global developmental delay** | Delayed acquisition of motor/cognitive skills |
| Moderate intellectual disability | Behavioral/neurodevelopmental manifestation | Adult outcome; stable/chronic | 2/2 | **HP:0002342 Intellectual disability, moderate** | Lifelong limitations in independent living, education, employment, and communication |
| Brisk tendon reflexes | Clinical neurologic sign | Reported in original family | 2/2 reported collectively | **HP:0001348 Brisk reflexes** | Marker of neuromuscular excitability; direct daily impact uncertain |
| Tetany | Neuromuscular symptom | Included in current Orphanet disease description, but not clearly documented in the two sisters | Unknown | **HP:0001281 Tetany** | Painful spasms and acute functional impairment if present |
| Normocalcemia | Negative laboratory feature | Persistent in reported family | 2/2 | No abnormal HPO term; record as “hypocalcemia absent” | Distinguishes HOMG4 from TRPM6-related hypomagnesemia with secondary hypocalcemia |
| Normocalciuria | Negative/differentiating laboratory feature | Persistent | 2/2 | No abnormal HPO term | Distinguishes hypercalciuric renal hypomagnesemias |
| Normal Na, K, Cl, bicarbonate, pH, PTH, renin and aldosterone | Negative laboratory features | At evaluation | 2/2 where assessed | Record as excluded findings | Supports an isolated magnesium-handling defect |
| Infantile onset | Temporal qualifier | First-year seizure onset | 2/2 | **HP:0003593 Infantile onset** | Defines a critical period for early diagnosis and prevention of recurrent seizures |

The original clinical observations included seizures, mild-to-moderate psychomotor retardation and brisk reflexes. [153] The molecular reassessment documented serum magnesium of 0.53–0.66 mmol/L and fractional magnesium excretion of 4.8% and 3.6%. [164]

### 3.2 Interpretation of neurologic disease

It remains uncertain whether developmental impairment results entirely from early, recurrent hypomagnesemic seizures or whether altered EGF signaling contributes directly to brain development. The original study detected *EGF* expression in human cerebrum, but no patient neuroimaging, neuropathology, or brain-specific functional study established a direct developmental mechanism. Therefore:

* **Renal magnesium wasting:** demonstrated upstream phenotype.
* **Seizures:** strongly compatible with magnesium-dependent neuronal hyperexcitability.
* **Developmental delay/intellectual disability:** associated consistently in the two patients, but exact causal path is partly inferred.

No disease-specific EQ-5D, SF-36, PROMIS, educational, caregiver-burden, or other quality-of-life data are available.

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Attribute | Value |
|---|---|
| Gene symbol | ***EGF*** |
| Name | Epidermal growth factor |
| HGNC | **HGNC:3229** |
| NCBI Gene | **1950** |
| Ensembl | **ENSG00000138798** |
| OMIM gene | **131530** |
| Cytogenetic location | **4q25** |
| GRCh38 coordinates | chr4:109,912,883–110,013,766 |
| Exons | 24 |
| Canonical/MANE transcript | **NM_001963.6** |
| Protein | Pro-epidermal growth factor |
| UniProt | **P01133** |
| Protein class/localization | Single-pass type-I membrane precursor, proteolytically processed to a 53-amino-acid mature EGF peptide |

NCBI describes EGF as a precursor processed into a 53-amino-acid peptide that binds EGFR and regulates cellular proliferation and differentiation. [91] UniProt records p.Pro1070Leu as affecting basolateral sorting and preventing effective EGFR/TRPM6 stimulation. [94]

### 4.2 Pathogenic variant

| Feature | Detail |
|---|---|
| Variant | **NM_001963.6:c.3209C>T** |
| Protein | **NP_001954.2:p.(Pro1070Leu)** |
| Genomic GRCh38 | **NC_000004.12:g.110004540C>T** |
| Genomic GRCh37 | **NC_000004.11:g.110925696C>T** |
| dbSNP | **rs121434567** |
| ClinVar | **Variation ID 16614; VCV000016614.1** |
| Variant type | Germline missense SNV |
| Zygosity in patients | Homozygous |
| ClinVar classification | Pathogenic, one literature-only submission |
| Review status | No expert-panel review; no modern ACMG criteria supplied |
| Last formal evaluation | August 1, 2007 |
| gnomAD frequency | Approximately **0.00003** overall; exomes approximately 0.00002 |
| ExAC frequency | Approximately **0.00003** |
| TOPMed frequency | Approximately 0.00001–0.00002 |
| Functional consequence | Defective polarized sorting/processing and basolateral secretion of pro-EGF; functional loss of local EGF–EGFR signaling |
| Controls in original study | Absent from 126 ethnically matched control chromosomes |

The complete ClinVar record confirms the coordinates, frequencies and single literature-only pathogenic submission. [106] The very low population frequency is compatible with recessive disease, but ClinVar’s classification is not an expert-panel or multi-laboratory consensus.

### 4.3 Segregation and penetrance

Both affected sisters were homozygous. Both parents, two unaffected sisters, and a paternal aunt were heterozygous; two children of the aunt were homozygous reference. This is consistent with high penetrance for the homozygous state and nonpenetrance in heterozygotes, but only two homozygotes are known.

No data establish:

* penetrance percentage;
* age-dependent penetrance;
* allelic series or genotype–phenotype correlation;
* germline mosaicism;
* anticipation;
* a founder mutation;
* modifier genes;
* somatic disease causation;
* disease-specific DNA methylation, histone or chromatin abnormalities;
* recurrent copy-number or chromosomal structural abnormalities.

Assuming Hardy–Weinberg equilibrium and an allele frequency of 2–3×10⁻⁵, a purely illustrative carrier frequency would be about 4–6×10⁻⁵ and homozygous frequency approximately 4–9×10⁻¹⁰. This estimate is uncertain because ancestry-specific frequency, pathogenicity, ascertainment, and founder effects are inadequately characterized.

---

## 5. Environmental information

Renal hypomagnesemia 4 is genetic, not environmentally caused. Clinically relevant exacerbating factors include:

| Environmental/lifestyle factor | Expected effect |
|---|---|
| Magnesium-poor diet or malnutrition | Reduces available magnesium and worsens depletion |
| Chronic diarrhea, malabsorption, vomiting | Adds gastrointestinal magnesium loss |
| Alcohol misuse | Combines inadequate intake, gastrointestinal loss and renal wasting |
| Loop/thiazide diuretics | Increase urinary magnesium excretion |
| Cisplatin/carboplatin, aminoglycosides, amphotericin B, calcineurin inhibitors | Cause tubular magnesium wasting |
| Cetuximab, panitumumab, erlotinib and other EGFR antagonists | Directly interfere with the same EGF–EGFR–TRPM6 axis |
| Long-term proton-pump inhibitors | Mainly reduce intestinal magnesium absorption |
| Adequate dietary magnesium and avoidance of avoidable magnesium-wasting drugs | Protective against biochemical deterioration, not against inheritance |

There is no evidence for smoking, exercise, pollution, radiation, occupational exposure, or infectious-agent involvement specific to HOMG4.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Homozygous *EGF* c.3209C>T causes p.Pro1070Leu** in the cytoplasmic tail of pro-EGF.
2. **p.Pro1070Leu disrupts a PXXP basolateral-sorting motif and leads to reduced basolateral delivery/release** of pro-EGF in polarized distal-tubule epithelium; apical release remains relatively preserved.
3. **Reduced basolateral EGF leads to inadequate activation of basolateral EGFR** on distal convoluted tubule epithelial cells.
4. **Reduced EGFR signaling leads to reduced Src/PI3K–Rac1 and MEK–ERK/AP-1 signaling**, based primarily on subsequent cell studies.
5. **Reduced Src/Rac1 signaling leads to less trafficking and surface abundance of TRPM6/TRPM7-containing channels** at the apical membrane; reduced ERK/AP-1 signaling may additionally lower *TRPM6* transcription.
6. **Reduced apical TRPM6 activity leads to impaired transcellular Mg²⁺ entry** from tubular fluid into DCT epithelial cells.
7. **Impaired DCT magnesium reabsorption results in inappropriately high urinary magnesium excretion despite hypomagnesemia.**
8. **Persistent urinary loss leads to systemic magnesium depletion.**
9. **Systemic magnesium depletion leads to neuronal and neuromuscular hyperexcitability**, producing brisk reflexes, tetany and generalized seizures.
10. **Early recurrent seizures and/or altered EGF signaling are inferred to contribute to psychomotor delay and moderate intellectual disability**; the relative contributions have not been demonstrated.
11. **Potential branch:** severe magnesium deficiency may lead to myocardial electrical instability and arrhythmia, although arrhythmia has not been reported in the two HOMG4 patients.

### 6.2 Experimental support

The 2007 study showed:

* EGF colocalization with NCC-positive distal convoluted tubules in rat kidney.
* Dose-dependent EGF stimulation of TRPM6 current in transfected HEK293 cells, with an EC₅₀ of approximately 1.7 nM.
* Wild-type but not p.Pro1070Leu conditioned medium stimulated TRPM6.
* Cetuximab reduced wild-type EGF-induced current from 491 ± 62 to 286 ± 48 pA/pF, versus 191 ± 22 pA/pF with mock medium.
* In polarized MDCK cells, mutant and wild-type apical media stimulated TRPM6 similarly, but mutant basolateral medium did not.
* Cetuximab-treated patients developed renal magnesium wasting, providing a human pharmacologic phenocopy. [113]

A later primary study reported that EGFR activation recruits Src-family kinases and Rac1, redistributing vesicular TRPM6 to the plasma membrane. PMID associated with JASN 2009; DOI **10.1681/ASN.2008030327**. [241] Another study found EGF-dependent increases in phospho-ERK1/2, c-Fos, c-Jun and *TRPM6* transcription, supporting an ERK/AP-1 branch; PMID **19937979**, published online November 2009. [244]

### 6.3 Current mechanistic interpretation and uncertainty

Recent renal-magnesium reviews continue to place EGF upstream of TRPM6/TRPM7-mediated DCT reabsorption. A 2023 review states that EGF increases TRPM6 membrane expression and transcription and acts as a paracrine DCT regulator. [232] The 2024 Core Curriculum similarly describes DCT magnesium reabsorption through TRPM6/TRPM7 heteromers and paracrine regulation by EGF. [228]

However, **complete *Egf* knockout mice do not develop significant hypomagnesemia**, indicating species differences, ligand redundancy, developmental compensation, or a variant effect more complex than simple EGF absence. [305] Thus, the human p.Pro1070Leu mechanism is best described as **abnormal polarized pro-EGF sorting/processing**, not proven generic EGF haploinsufficiency.

### 6.4 Suggested ontology annotations

| Mechanistic feature | Suggested ontology term |
|---|---|
| Magnesium-ion homeostasis | **GO:0010960** |
| ERBB signaling | **GO:0038127** |
| EGF receptor signaling | GO:0007173, noting that current GO marks this term obsolete in favor of broader/current descendants |
| Protein localization to plasma membrane | **GO:0072659** |
| Vesicle-mediated transport | **GO:0016192** |
| Magnesium-ion transmembrane transport | **GO:1903830** |
| EGF receptor binding | **GO:0005154** |
| Apical plasma membrane | **GO:0016324** |
| Basolateral plasma membrane | **GO:0016323** |
| Plasma membrane | **GO:0005886** |
| Magnesium ion | **CHEBI:18420** |
| DCT epithelial cell | **CL:1000849** |
| Early DCT epithelial cell | **CL:4030016** |

The correct DCT epithelial-cell identifier is CL:1000849. [196] GO:0010960 denotes magnesium-ion homeostasis, while GO:0016323 and GO:0016324 identify basolateral and apical plasma membranes. [426][427]

### 6.5 Omics and advanced technologies

No HOMG4-specific patient transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, organoid, iPSC or integrated multi-omics study was found. Current single-cell kidney atlases recognize DCT epithelial cells and markers such as SLC12A3 and TRPM6, but this is normal-reference annotation rather than disease profiling. [206]

---

## 7. Anatomical structures affected

| Level | Structure/cell/compartment | Role and suggested ontology |
|---|---|---|
| Primary organ | Kidney | Direct site of magnesium wasting; UBERON:0002113 |
| Primary segment | Distal convoluted tubule | Final fine-tuning of urinary magnesium; **UBERON:0001292** |
| Primary cell | DCT epithelial cell | **CL:1000849** |
| Basolateral compartment | Basolateral plasma membrane | Pro-EGF targeting and EGFR localization; **GO:0016323** |
| Apical compartment | Apical plasma membrane | TRPM6/TRPM7 channel localization; **GO:0016324** |
| Secondary system | Central nervous system | Seizures and developmental/cognitive phenotype; direct EGF effect not established |
| Secondary tissue | Skeletal muscle/neuromuscular system | Potential tetany and hyperreflexia caused by systemic magnesium deficiency |
| Secondary system | Cardiovascular conduction system | Potential arrhythmia risk from severe hypomagnesemia; not reported in HOMG4 |
| Gastrointestinal tract | Not primarily defective | Original retention studies indicated preserved intestinal absorption |

The DCT corresponds to UBERON:0001292 and its epithelial cells to CL:1000849. [202][200] The disease is systemic and bilateral by virtue of a germline defect; unilateral or asymmetric renal involvement is not expected.

---

## 8. Temporal development

* **Genetic onset:** conception.
* **Biochemical onset:** probably early life; exact neonatal magnesium values are unavailable.
* **Clinical onset:** generalized seizures in the **first year of life**.
* **Development:** psychomotor delay became evident during childhood.
* **Adult course:** both women had moderate intellectual disability; chronic hypomagnesemia persisted.
* **Pattern:** chronic renal wasting with potentially episodic neurologic decompensation when magnesium falls further.
* **Progression:** no staged progressive nephropathy, nephrocalcinosis or renal failure was reported.
* **Remission:** no spontaneous biochemical remission documented.
* **Critical period:** infancy and early childhood, when seizures and magnesium deficiency may have disproportionate neurodevelopmental consequences.
* **Duration:** presumed lifelong.

No formal natural-history staging system or longitudinal cohort exists.

---

## 9. Inheritance and population characteristics

| Characteristic | Best available evidence |
|---|---|
| Inheritance | **Autosomal recessive** |
| Known affected individuals | **2 sisters** |
| Known families | **1 consanguineous Dutch family** |
| Sex ratio | 0 male:2 female; not interpretable |
| Prevalence | Orphanet: **<1 per 1,000,000** |
| Incidence | Unknown |
| Geographic distribution | Original family from the Netherlands; rare population-database alleles occur more broadly, but ancestry distribution is not adequately reported |
| Penetrance | 2/2 known homozygotes affected; true penetrance unknown |
| Expressivity | Similar in the sisters; broader variability unknown |
| Carrier phenotype | Five identified heterozygotes were unaffected with respect to hypomagnesemia |
| Consanguinity | Important in the only family; parents were second cousins |
| Anticipation | Not applicable/reported |
| Germline mosaicism | Not reported |
| Founder effect | Not established |
| Carrier frequency | Unknown; rough p.Pro1070Leu frequency-based estimate 1 in 17,000–25,000, subject to major uncertainty |
| Population screening | Not justified given extreme rarity and insufficient prevalence data |

Current Orphanet prevalence is below one per million. [134] A review emphasizes that only two affected girls from one consanguineous family have been reported. [380]

For two carrier parents, standard autosomal-recessive recurrence probabilities are **25% affected, 50% carrier, and 25% unaffected/noncarrier per pregnancy**, assuming both parental variants are confirmed and fully penetrant.

---

## 10. Diagnostics

### 10.1 Recommended diagnostic workflow

1. Confirm persistent low total serum magnesium; consider ionized magnesium if available.
2. Measure serum calcium, potassium, bicarbonate, creatinine/eGFR, phosphate, PTH, glucose and albumin.
3. Obtain urine magnesium and creatinine, ideally before major replacement.
4. Calculate fractional magnesium excretion:

\[
FE_{Mg}=\frac{U_{Mg}\times P_{Cr}}{0.7\times P_{Mg}\times U_{Cr}}\times100
\]

5. In hypomagnesemia, an FEMg above approximately **3–4%** supports renal wasting; below 2% suggests an extrarenal source. A 24-hour urinary magnesium above approximately 30 mg/day also supports renal loss. [136]
6. Document serum and urinary calcium. HOMG4 is expected to be normocalcemic and normocalciuric.
7. Exclude acquired causes, particularly diuretics, aminoglycosides, platinum chemotherapy, calcineurin inhibitors, EGFR inhibitors, alcohol misuse and uncontrolled diabetes.
8. Pursue molecular testing when onset is infantile, the condition is familial or unexplained, or neurologic manifestations coexist.
9. Confirm candidate variants with parental segregation and interpret under current ACMG/AMP criteria.

### 10.2 Genetic testing

| Test | Utility |
|---|---|
| Renal tubulopathy/hypomagnesemia multigene panel | Preferred first-line genetic test; should include *EGF, TRPM6, CNNM2, FXYD2, SLC12A3, CLDN16, CLDN19, KCNA1, KCNJ10, HNF1B, ATP1A1, RRAGD* and related genes |
| *EGF* sequencing | Appropriate when phenotype is isolated normocalciuric renal Mg wasting with recessive inheritance |
| Deletion/duplication analysis | Reasonable if sequencing is negative; no HOMG4-causing deletion is currently established |
| WES | Useful for atypical cases or negative panel testing |
| WGS | Useful for deep-intronic, regulatory or structural variants and reanalysis; clinical yield for HOMG4 is unknown |
| RNA sequencing | Research/functional option for suspected splice variants; no established diagnostic assay |
| CMA | Low expected yield for an isolated single-gene phenotype; useful if syndromic features suggest a genomic imbalance |
| Karyotype/FISH | Not routinely indicated |
| Mitochondrial DNA testing | Not indicated unless another phenotype suggests mitochondrial disease |
| Repeat-expansion testing | Not relevant |
| Prenatal/PGT-M testing | Technically possible once familial pathogenic variants are established |

Orphanet lists postnatal molecular testing panels containing *EGF* and other primary-hypomagnesemia genes. [126]

### 10.3 Clinical and ancillary tests

* **ECG:** particularly during severe hypomagnesemia, palpitations or syncope.
* **EEG:** for seizure classification and monitoring.
* **Renal ultrasound:** not diagnostic; useful if hypercalciuria or nephrocalcinosis suggests another disorder.
* **Brain MRI:** may evaluate developmental delay or refractory seizures but no HOMG4-specific imaging pattern is known.
* **Biopsy:** no diagnostic role.
* **Urinary EGF:** biologically attractive but not validated as a HOMG4 diagnostic biomarker.

### 10.4 Differential diagnosis

| Differential | Distinguishing findings |
|---|---|
| *TRPM6*-related hypomagnesemia with secondary hypocalcemia | Much more severe Mg deficiency, impaired intestinal absorption, secondary hypocalcemia |
| *CNNM2*-related hypomagnesemia | Usually dominant/de novo or semidominant; seizures, intellectual disability, obesity or brain abnormalities may occur |
| Gitelman syndrome, *SLC12A3* | Hypokalemia, metabolic alkalosis and hypocalciuria |
| *FXYD2* hypomagnesemia | Usually autosomal dominant; hypocalciuria may occur |
| *CLDN16/CLDN19* disease | Hypercalciuria, nephrocalcinosis, progressive kidney disease; ocular abnormalities with *CLDN19* |
| EAST/SeSAME, *KCNJ10* | Epilepsy, ataxia, sensorineural deafness and salt-wasting tubulopathy |
| *KCNA1* disease | Episodic ataxia and renal magnesium wasting |
| HNF1B-associated disease | Renal malformations/cysts, diabetes, genital anomalies and hypomagnesemia |
| EGFR-related epithelial inflammatory syndrome | Severe skin/gut epithelial inflammation in addition to hypomagnesemia |
| Drug-induced renal Mg wasting | Exposure history; improvement after withdrawal where possible |
| Gastrointestinal loss/PPI-associated deficiency | Low urinary magnesium or FEMg generally <2% |
| Malnutrition/alcohol-related depletion | Clinical context and mixed intake/GI/renal mechanisms |

The combination of urine/serum biochemistry, inheritance and extrarenal manifestations guides differential testing. Hypercalciuria suggests TAL disorders, whereas hypokalemia and metabolic alkalosis suggest Gitelman-like DCT disease. [319]

No newborn screening program or standardized clinical diagnostic criteria exist. Cascade biochemical and genetic testing is appropriate for relatives.

---

## 11. Outcome and prognosis

Disease-specific survival, mortality, five-year survival and life-expectancy statistics are unavailable. Both original patients survived into adulthood, suggesting that the condition is not inevitably fatal when seizures and electrolyte abnormalities are managed.

Important morbidity includes:

* recurrent infantile seizures;
* permanent developmental and cognitive disability;
* chronic treatment and monitoring burden;
* potential tetany, muscle spasm and weakness;
* potential cardiac arrhythmia when magnesium is severely low.

Severe hypomagnesemia can cause torsades de pointes and other fatal arrhythmias, although none were documented in the HOMG4 sisters. [346]

Prognostic factors are inferred to include:

* age at recognition;
* depth and duration of magnesium deficiency;
* seizure burden;
* response and adherence to magnesium replacement;
* exposure to magnesium-wasting drugs;
* renal function;
* coexisting hypokalemia or hypocalcemia.

No validated prognostic biomarker or disease-specific quality-of-life instrument exists. Serum magnesium, FEMg, seizure frequency, EEG findings and developmental trajectory are practical monitoring endpoints.

---

## 12. Treatment

No treatment corrects the inherited pro-EGF trafficking defect. Management is supportive and extrapolated largely from general hypomagnesemia and other renal magnesium-wasting disorders.

### 12.1 Treatment approach

| Intervention | Role/mechanism | Evidence in HOMG4 | Suggested ontology |
|---|---|---|---|
| Oral magnesium salts | Replace ongoing magnesium loss; chloride, lactate or other sustained-release preparations may be better absorbed/tolerated than oxide | No disease-specific response data reported | NCIT: magnesium supplementation; magnesium oxide **NCIT:C29242** |
| IV magnesium sulfate | Acute treatment for severe symptomatic hypomagnesemia, seizures or arrhythmia | General standard, not specifically studied in HOMG4 | **NCIT:C623**; CHEBI:32599 |
| Subcutaneous magnesium sulfate | Slow outpatient replacement in refractory renal wasting | Evidence from unrelated refractory cases, not HOMG4 | NCIT:C623 |
| Amiloride | ENaC blockade can reduce renal magnesium loss | No HOMG4-specific trial; case-level evidence in idiopathic renal Mg wasting | Amiloride hydrochloride **NCIT:C47390** |
| Antiseizure medication | Controls recurrent seizures | Conventional antiseizure drugs controlled seizures in both sisters | NCIT pharmacologic substance terms for the selected agent |
| Dietitian-guided magnesium-rich diet | Adjunct; cannot overcome substantial renal wasting alone | Not specifically studied | NCIT dietary intervention |
| Avoidance of magnesium-wasting medications | Prevents additive renal/GI loss | Mechanistically justified | NCIT medication review/supportive care |
| Developmental, educational, PT/OT and speech support | Addresses lifelong neurodevelopmental morbidity | No formal outcomes reported | NCIT rehabilitation/occupational therapy/speech therapy |

For acute unstable adult hypomagnesemia, general guidance uses 1–2 g magnesium sulfate over approximately 15 minutes, while nonemergent replacement may use 4–8 g over 12–24 hours; pediatric dosing requires weight-based specialist protocols. [165] Oral therapy is generally divided to reduce diarrhea, with careful dose reduction and monitoring when eGFR is below 30 mL/min/1.73 m².

Amiloride raised serum magnesium, lowered FEMg and improved symptoms in one patient with idiopathic renal magnesium wasting, but this is indirect evidence. [287] Continuous home subcutaneous magnesium sulfate at 2 g/day normalized or nearly normalized serum magnesium in a refractory renal-wasting case, again not HOMG4-specific. [176]

### 12.2 Treatment limitations and adverse effects

* Oral magnesium commonly causes diarrhea and abdominal discomfort.
* Rapid IV magnesium can cause flushing, hypotension, bradycardia and respiratory depression.
* Hypermagnesemia is a risk with impaired kidney function.
* Amiloride may cause hyperkalemia, hypotension and renal-function deterioration.
* Magnesium replacement may remain incomplete because renal losses continue.
* Magnesium correction should not automatically replace antiseizure treatment once epilepsy is established.

### 12.3 Experimental and precision therapies

No registered HOMG4-specific interventional trial, gene therapy, RNA therapy, CRISPR treatment, cell therapy or recombinant EGF treatment was identified. Systemic EGF or EGFR agonism would carry substantial proliferative and oncologic concerns and is not an established treatment.

A future precision approach would require kidney/DCT-targeted restoration of correctly polarized EGF signaling or enhancement of TRPM6 surface expression without systemic mitogenic EGFR activation. This remains conceptual.

---

## 13. Prevention

### Primary prevention

The inherited genotype cannot be prevented after conception. Reproductive options include:

* carrier testing of at-risk relatives;
* partner testing;
* preimplantation genetic testing for monogenic disease;
* chorionic-villus or amniotic-fluid prenatal diagnosis when familial variants are known;
* donor gametes or other family-planning options.

### Secondary prevention

* Cascade testing in siblings and relatives.
* Serum magnesium measurement in at-risk infants, especially before seizures occur.
* Early urine magnesium/FEMg assessment.
* Prompt genetic testing for familial infantile hypomagnesemia.
* Early developmental and neurologic assessment.

### Tertiary prevention

* Maintain serum magnesium at the highest safely achievable level.
* Prevent prolonged or recurrent seizures.
* Monitor ECG and associated potassium/calcium abnormalities during severe episodes.
* Avoid preventable magnesium-wasting drugs, especially EGFR inhibitors where alternatives exist.
* Ensure adequate dietary magnesium and treat diarrhea or malabsorption.
* Provide early-intervention, educational and rehabilitation services.

No vaccine, antimicrobial prophylaxis, public-health sanitation intervention or population newborn-screening program applies.

---

## 14. Other species and natural disease

| Species | Taxon/ortholog information | Natural disease evidence |
|---|---|---|
| Human, *Homo sapiens* | NCBI Taxon 9606; *EGF* Gene 1950 | Confirmed HOMG4 |
| Mouse, *Mus musculus* | Taxon 10090; *Egf* Gene **13645**, MGI:95290 | No naturally occurring HOMG4 equivalent identified |
| Rat, *Rattus norvegicus* | Taxon 10116; *Egf* Gene **25313** | Kidney EGF localization used experimentally; no natural HOMG4 |
| Zebrafish, *Danio rerio* | Taxon 7955; *egf* Gene **403045** | Conserved ortholog; no reported natural HOMG4 |
| Dog, *Canis lupus familiaris* | Taxon 9615; *EGF* Gene **403657** | No EGF-related hereditary renal hypomagnesemia found |
| Cat, *Felis catus* | Taxon 9685; *EGF* Gene **493978** | No EGF-related hereditary renal hypomagnesemia found |

MGI records one-to-one vertebrate orthology among human, mouse, rat and zebrafish and mouse *Egf* NCBI Gene 13645. [271] No OMIA entry, breed predisposition, veterinary founder variant, zoonotic transmission or cross-species infectious risk was identified. The mechanism is evolutionarily relevant but the specific human disease does not appear to be a recognized natural veterinary disorder.

---

## 15. Model organisms and experimental systems

| Model | Type | Main finding | Strengths | Limitations |
|---|---|---|---|---|
| HEK293 expressing TRPM6 | In-vitro human cell system | EGF dose-dependently increased TRPM6 current; mutant-conditioned medium failed to stimulate it | Direct electrophysiology and EGFR blockade | Not a polarized DCT cell |
| Polarized MDCK-I cells expressing WT or p.Pro1070Leu pro-EGF | In-vitro canine kidney epithelium | Mutant retained apical release but lacked effective basolateral release | Demonstrates polarized sorting defect | Nonhuman cell line; overexpression |
| Rat kidney immunohistochemistry | Tissue model | EGF colocalized with NCC-positive DCT segments | Anatomical localization | Not a genetic disease model |
| Cetuximab-treated cancer patients | Human pharmacologic phenocopy | EGFR blockade caused renal magnesium wasting | Human in-vivo support for pathway | Acquired drug effect, different initiating lesion |
| *Egf* knockout mouse | Mammalian genetic model | No significant hypomagnesemia at 2 or 4 months | Tests complete ligand deficiency | Does not reproduce p.Pro1070Leu polarized-sorting defect; compensation/redundancy likely |
| Anti-EGFR-treated mouse | Induced mammalian model | Mild hypomagnesemia reported after antibody treatment | Tests receptor blockade | Urinary Mg response was limited; drug model rather than disease |
| TRPM6-deficient models | Downstream pathway models | Demonstrate the importance of TRPM6 to epithelial magnesium handling | Mechanistically relevant | Model a different human disorder and show tissue/species-dependent phenotypes |
| Patient-derived iPSC/DCT organoid | Not yet reported | Potential future model | Could examine human polarized trafficking in native genotype | Currently unavailable |
| *Egf* p.Pro1070Leu knock-in mouse | Not identified | Potential future model | Closest genetic test of the human lesion | Species may still fail to reproduce human renal phenotype |

The absence of hypomagnesemia in *Egf* knockout mice is a major model limitation and argues for creation of a **precise p.Pro1070Leu knock-in**, rather than assuming that complete knockout is equivalent to the human trafficking mutation. [305]

---

## Recent developments and research priorities

No new molecularly confirmed HOMG4 family or independently validated pathogenic *EGF* allelic series was found through the 2023–2024 literature. Recent work instead strengthens and refines the broader renal-magnesium framework:

1. **2023 physiology update:** DCT magnesium fine-tuning is now commonly modeled through TRPM6/TRPM7 heteromeric channels, with EGF regulating membrane abundance and transcription rather than acting simply as a channel opener. [232]
2. **2024 Core Curriculum:** confirms EGF as a paracrine regulator of DCT TRPM6/TRPM7 and provides contemporary biochemical diagnostic thresholds. [228]
3. **2024 human biomarker research:** urinary EGF is increasingly interpreted as a marker of distal tubular mass and correlates with serum magnesium and kidney outcomes, but it is not yet validated for HOMG4 diagnosis or monitoring. [184]
4. **Model discrepancy:** *Egf*-null mice lack the expected severe magnesium phenotype, so human variant-specific trafficking, redundant EGFR ligands, or species-specific DCT physiology require clarification. [305]
5. **Needed studies:** independent patients, modern ACMG/ClinGen gene–disease curation, ancestry-resolved variant frequencies, patient-derived DCT organoids, knock-in animal models, prospective magnesium-replacement outcomes, neurodevelopmental natural history and disease-specific quality-of-life assessment.

### Overall evidence assessment

The **clinical phenotype and biochemical defect are well documented in two related humans**, and the original p.Pro1070Leu functional experiments provide a coherent mechanism. Nevertheless, the gene–disease relationship remains constrained by a single family, a single variant, no independent replication, an old single-submitter ClinVar assertion, and a discordant *Egf*-knockout mouse phenotype. The best current interpretation is therefore:

> **Renal hypomagnesemia 4 is a highly plausible, functionally supported autosomal-recessive pro-EGF polarized-trafficking disorder, but its full allelic spectrum, penetrance, epidemiology, natural history and optimal treatment remain undetermined.**

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 15 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012717` (2 mentions) - the report calls it "MONDO"; MONDO calls it **renal hypomagnesemia 4**
- `DOID:0060882` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **renal hypomagnesemia 4**
- `CL:4030016` (1 mention) - the report calls it "Early DCT epithelial cell"; CL calls it **epithelial cell of early distal convoluted tubule**
- `NCIT:C623` (2 mentions) - the report calls it "Evidence from unrelated refractory cases, not HOMG4"; NCIT calls it **Magnesium Sulfate**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005154` (1 mention) - the report calls it "EGF receptor binding"; GO calls it **epidermal growth factor receptor binding**, and lists "EGF receptor binding" among its other names
- `CHEBI:18420` (1 mention) - the report calls it "Magnesium ion"; CHEBI calls it **magnesium(2+)**, and lists "MAGNESIUM ION" among its other names
- `CL:1000849` (4 mentions) - the report calls it "DCT epithelial cell"; CL calls it **kidney distal convoluted tubule epithelial cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `Gene`, `MGI`.