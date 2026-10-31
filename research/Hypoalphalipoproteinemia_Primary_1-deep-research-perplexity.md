---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-27T11:41:19.962076'
end_time: '2026-10-27T11:46:33.193474'
duration_seconds: 313.23
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypoalphalipoproteinemia Primary 1
  mondo_id: MONDO:0011393
  category: Genetic
  causal_genes: ABCA1
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
citation_count: 54
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 21
  on_topic: 18
  validator_version: 0.4.0
term_validation:
  total_terms: 32
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 17
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: DOID:0080957
    reported_labels:
    - Disease Ontology
    ontology_label: primary hypoalphalipoproteinemia 1
  - term_id: CL:0000057
    reported_labels:
    - fibroblast, relevant to historical efflux assays
    ontology_label: fibroblast
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypoalphalipoproteinemia Primary 1
- **MONDO ID:** MONDO:0011393 (if available)
- **Causal gene(s):** ABCA1
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

Please provide a comprehensive research report on **Hypoalphalipoproteinemia Primary 1** covering all of the
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

# Hypoalphalipoproteinemia, Primary, 1 — comprehensive disease-characteristics report

## Scope and identity clarification

**Hypoalphalipoproteinemia, primary, 1 is an autosomal-dominant HDL-deficiency disorder caused by a heterozygous pathogenic variant in *ABCA1***, encoding ATP-binding cassette transporter A1. It corresponds to **MONDO:0011393 and OMIM 604091**, despite the prompt’s statement that OMIM was not recorded. It is also called **ABCA1-related familial HDL deficiency** or **familial hypoalphalipoproteinemia type 1**. Biallelic *ABCA1* loss causes the allelic but substantially more severe **Tangier disease, OMIM 205400**; classic Tangier findings should not automatically be assigned to monoallelic primary hypoalphalipoproteinemia-1. OMIM specifically attributes the dominant disorder to heterozygous *ABCA1* variants at 9q31.1. [17][223]

**Evidence boundary.** The most disease-specific human evidence comes from small pedigrees and mutation-carrier cohorts assembled before 2010. Recent 2023–2024 research primarily refines ABCA1 structure, variant interpretation, and clinical diagnosis rather than providing large natural-history studies.

---

## 1. Disease information

### Definition

The defining abnormality is persistently reduced plasma HDL cholesterol and apoA-I caused by partial ABCA1 dysfunction, with impaired cellular cholesterol/phospholipid efflux and variable susceptibility to premature atherosclerotic cardiovascular disease. Heterozygotes usually have a milder biochemical phenotype than patients with Tangier disease and generally lack the latter’s systemic reticuloendothelial cholesterol-storage manifestations. MedlinePlus notes that one altered *ABCA1* copy causes familial HDL deficiency, whereas two altered copies cause Tangier disease. [3]

### Identifiers and terminology

| System | Identifier/name | Qualification |
|---|---|---|
| MONDO | **MONDO:0011393**, hypoalphalipoproteinemia, primary, 1 | Target disease |
| OMIM phenotype | **604091**, HDL deficiency, familial, 1 | Autosomal dominant |
| OMIM gene | **600046**, *ABCA1* | Causal gene |
| MedGen | **C5231558** | Maps to MONDO:0011393 |
| MeSH | **D052456**, Hypoalphalipoproteinemias | Broader class, not gene-specific |
| ICD-10-CM | **E78.6**, lipoprotein deficiency | Includes depressed HDL/hypoalphalipoproteinemia |
| ICD-11 | **5C81.0**, hypoalphalipoproteinaemia | Phenotypic code, not gene-specific |
| SNOMED CT | **15346004** | Reported by OMIM |
| Disease Ontology | **DOID:0080957** | Reported cross-reference |
| Orphanet | **ORPHA:425** appears as an OMIM/ClinVar cross-reference | **Curation warning:** current Orphanet 425 is titled *apolipoprotein A-I deficiency* and describes an *APOA1*-related phenotype, so it is not a clean identifier for this *ABCA1*-specific entity. [224][256] |

The broader MeSH concept encompasses low-HDL disorders caused by *ABCA1*, *APOA1*, and *LCAT*, while ICD codes likewise do not distinguish the molecular cause. [240][253]

### Synonyms

- Familial HDL deficiency 1
- HDL deficiency, familial, 1
- ABCA1-associated/ABCA1-related familial high-density lipoprotein deficiency
- Familial hypoalphalipoproteinemia
- Primary hypoalphalipoproteinemia
- FHA, FHA1, FHD, HDLD
- Low serum HDL cholesterol

Some of these terms are nonspecific and may also be used for *APOA1*-related disease. “Tangier disease” is **not** a strict synonym for the heterozygous disorder. [20][234]

### Data provenance

This entry is an **aggregated disease-level synthesis**, not an individual EHR record. MONDO, OMIM, MedGen, ClinVar, HPO, GTR, and literature cohorts aggregate information from pedigrees, research participants, case reports, and laboratories. Recent case reports are patient-level publications but are not equivalent to population-level natural-history data.

---

## 2. Etiology

### Primary cause

The disease is caused by a **germline heterozygous loss-of-function or function-reducing variant in *ABCA1***. ABCA1 normally transfers cellular cholesterol and phospholipids to lipid-poor apoA-I, initiating nascent HDL formation. Monoallelic dysfunction produces partial efflux deficiency; biallelic dysfunction produces Tangier disease. The original molecular identification in families was reported by Brooks-Wilson et al. in 1999 (PMID **10431236**) and Marcil et al. in 1999 (PMID **10533863**). [47][52]

### Genetic risk factors

- A pathogenic monoallelic *ABCA1* variant is the principal causal risk.
- Variant classes include missense, nonsense, frameshift, canonical splice-site, small insertion/deletion, and, less often, exon-level copy-number variants.
- Severity depends on residual protein trafficking, apoA-I binding, ATPase activity, and cholesterol-efflux function.
- Age modifies biochemical penetrance: in the 77-carrier cohort, adults aged 30–70 were more likely than carriers under 30 to have HDL-C below the age- and sex-specific fifth percentile. [46]
- Common variants can modify HDL or coronary risk, but they are not sufficient to diagnose the Mendelian disorder. Meta-analysis associated the *ABCA1* p.Arg219Lys K allele with lower atherosclerosis risk—OR 0.77, 95% CI 0.71–0.84—but substantial heterogeneity limits its use as a clinical protective marker. [136]

### Environmental and acquired modifiers

Environmental factors do **not cause** the monogenic disorder, but they alter measured HDL and cardiovascular consequences:

- Smoking, obesity, sedentary behavior, diabetes/insulin resistance, high-carbohydrate dietary patterns, and severe hypertriglyceridemia may further lower HDL or raise atherosclerotic risk.
- Androgenic steroids, some malignancies, liver failure, paraproteinemia, and severe hypertriglyceridemia can produce secondary low HDL and must be excluded diagnostically. [85][343]
- Traditional risk factors—hypertension, diabetes, smoking, elevated LDL/non-HDL cholesterol, elevated lipoprotein(a), and family history—likely determine much of the variability in clinical vascular disease.

### Protective factors

- Avoidance of tobacco, regular physical activity, healthy weight, diabetes and blood-pressure control, and aggressive LDL/non-HDL reduction lower overall cardiovascular risk, although they do not repair ABCA1 function.
- Genetically lower LDL-C may partly protect some severely ABCA1-deficient individuals, illustrating that HDL concentration alone does not determine atherosclerosis.
- *ABCA1* p.Arg219Lys may be protective at the population level, but association results differ among ancestries and studies; it should not be treated as a clinically validated modifier for an individual family. [141][142]

### Gene–environment interaction

The best-described interaction involves the common p.Arg230Cys variant in Mexican and Indigenous American populations: high-carbohydrate/lower-fat diets were associated with a more unfavorable HDL/triglyceride profile, especially in premenopausal women carrying the allele. An *ABCA1* p.Arg219Lys-by-saturated-fat interaction affecting triglycerides has also been reported. These are common-variant studies, not direct studies of families with MONDO:0011393. [31]

No toxin, radiation exposure, occupational exposure, or infectious agent is established as a cause of primary hypoalphalipoproteinemia-1.

---

## 3. Phenotypes

### Core phenotype table

| Phenotype and type | Characteristics, onset, frequency and course | Suggested HPO term | Functional/QOL impact |
|---|---|---|---|
| **Decreased circulating HDL-C** — laboratory abnormality | Lifelong biochemical tendency, often detectable in childhood but more penetrant with age. In one mutation-carrier cohort, HDL-C was about **40–45% lower** than in unaffected relatives. Variable from modestly low to below 20 mg/dL in severe heterozygotes. [168] | **HP:0003233**, Decreased HDL cholesterol concentration | Usually asymptomatic itself; prompts lifelong surveillance and treatment burden. |
| **Decreased apoA-I** — laboratory abnormality | About **40–45% lower** in the original heterozygote cohort; severe partial deficiency can be much lower because poorly lipidated apoA-I is rapidly catabolized. [358] | Decreased circulating apolipoprotein A-I concentration | Biomarker rather than direct symptom. |
| **Impaired cellular cholesterol efflux** — functional laboratory phenotype | Approximately 50% of normal in many heterozygotes, but variant-specific; generally stable and lifelong. [11] | No established disease-specific HPO term; consider abnormal cholesterol homeostasis | Research/specialist assay rather than routine clinical symptom. |
| **Hypertriglyceridemia** — laboratory abnormality | Variable, usually mild. Mean triglycerides were approximately **40% higher** in 77 heterozygotes than in unaffected relatives, but not all carriers were elevated. [358] | **HP:0002155** | May add pancreatometabolic or cardiovascular management burden if independently severe. |
| **Premature coronary atherosclerosis/CAD** — clinical complication | Adult-onset, age-dependent, variably penetrant. Early familial cohort: symptomatic vascular disease >3-fold more frequent and CAD onset about 10 years earlier than in relatives. Population studies are less conclusive. [358] | **HP:0005181**, Premature coronary artery atherosclerosis | Angina, myocardial infarction, interventions, reduced exercise tolerance, anxiety, medication burden. |
| **Increased carotid arterial-wall thickness** — imaging sign | Progressive subclinical atherosclerosis. In 30 carriers, carotid IMT reached 0.80 mm at age 55 versus age 80 in controls. [74] | HP:0002636 Atherosclerosis or HP:0005181 when premature | Usually asymptomatic until vascular events; useful risk stratifier. |
| **Myocardial infarction** — complication | Not obligatory; may occur before 50 in severely affected individuals with other risk factors. | HP:0001658, Myocardial infarction | Potential major morbidity, disability, and mortality. |

### Frequency and cardiovascular-risk uncertainty

In the landmark study of 77 heterozygotes from 11 families, cholesterol efflux explained 82% of HDL-C variation, and carriers showed more than a threefold increased frequency of CAD. The abstract stated:

> “CAD is more frequent in those heterozygotes with lower cholesterol efflux values.”  
> — Clee et al., *J Clin Invest*, 2000; PMID **11086027** [46]

However, a much larger Danish analysis of four function-reducing variants found a mean HDL-C reduction of 17 mg/dL but no significant increase in ischemic heart disease: combined OR **0.93**, 95% CI 0.53–1.62, among 109 heterozygotes. Its conclusion was:

> “Lower plasma levels of HDL cholesterol due to heterozygosity for loss-of-function mutations in ABCA1 were not associated with an increased risk of IHD.” [13]

The most defensible interpretation is therefore: **premature atherosclerosis is a variable susceptibility rather than an inevitable or fully penetrant feature**, and risk is likely determined by the exact variant, residual efflux, LDL/non-HDL exposure, age, and conventional risk factors.

### Features that should not routinely be assigned

Yellow-orange tonsils, hepatosplenomegaly, peripheral neuropathy, corneal opacity, thrombocytopenia, hemolysis, and systemic macrophage cholesterol storage are primarily **biallelic Tangier disease** findings. A monoallelic patient with these manifestations should be investigated for a second *ABCA1* pathogenic variant or another diagnosis. [31]

No disease-specific EQ-5D, SF-36, PROMIS, or other quality-of-life study was identified.

---

## 4. Genetic and molecular information

### Causal gene and protein

| Attribute | Value |
|---|---|
| Gene | ***ABCA1***, ATP binding cassette subfamily A member 1 |
| HGNC | **HGNC:29** |
| NCBI Gene | **19** |
| OMIM gene | **600046** |
| Ensembl | **ENSG00000165029** |
| MANE transcript | **NM_005502.4** |
| Protein | NP_005493.2, 2,261 amino acids |
| UniProt | **O95477** |
| Location | **9q31.1** |
| Disease mechanism | Germline, predominantly loss of function/hypomorphic function |
| Gene–disease validity | Definitive for MONDO:0011393 in GenCC [29][127][134] |

ABCA1 is a full-size ABC transporter with two transmembrane domains, two nucleotide-binding domains, large extracellular domains, and regulatory regions. It localizes mainly to the plasma membrane and endosomal/vesicular compartments.

### Representative disease-associated variants

This is not an exhaustive variant list; *ABCA1* is highly polymorphic and many ClinVar records are VUS or have conflicting interpretations.

| Variant/example | Class and evidence | Functional consequence |
|---|---|---|
| p.Met1091Thr | Missense; classic familial HDL-deficiency variant | Severe trafficking defect, negligible apoA-I binding and near-absent cholesterol/choline efflux in vitro. [284] |
| p.Cys1477Arg | Missense; well-studied pathogenic loss-of-function control | Impaired surface localization/apoA-I interaction and minimal sterol efflux. |
| p.Pro85Leu | Missense, ClinVar pathogenic for primary hypoalphalipoproteinemia-1 | Segregated with low HDL in an affected kindred; PMID **12204794**. [15][277] |
| c.5398A>C, p.Asn1800His; rs146292819 | Missense; ClinVar likely pathogenic | Population frequency approximately 0.00033 overall; Danish carriers had reduced HDL/apoA-I, but no demonstrated excess IHD in aggregate. [273] |
| Nonsense/frameshift/splice variants | Loss-of-function | Truncation, nonsense-mediated decay, absent or reduced surface protein |
| Exon-level deletion/duplication | Rare structural loss-of-function | Reduced dosage; detectable by CNV analysis rather than routine sequence analysis alone |

### 2024 functional-variant research

Teigen et al., *Journal of Lipid Research*, published January 2024, tested **51 previously unclassified extracellular-domain missense variants**; only **12** had efflux below 50% of wild type: p.Glu284Lys, p.Arg306Cys, p.Tyr482Cys, p.Thr483Pro, p.Leu510Arg, p.Arg579Gln, p.Gly616Val, p.Gln621Arg, p.Gly790Asp, p.Leu1379Phe, p.His1600Arg, and p.Arg1615Trp. All had reduced cell-surface ABCA1. The abstract states:

> “Among these, only 12 variants showed a distinct loss-of-function phenotype, asserting their direct association with severe HDL disorders.”

Some variants showed genotype-specific partial rescue with 4-phenylbutyrate or proteasome inhibition, but this remains **in vitro experimental evidence**, not clinical treatment evidence. PMID **38052254**, publication date January 29, 2024. [298]

### ACMG interpretation

- Pathogenic/likely pathogenic classification should integrate allele frequency, segregation, phenotype, predicted loss of function, and validated efflux/surface-localization studies.
- A missense VUS should not establish the diagnosis by itself.
- The 2024 work showed why computational prediction alone is insufficient: many reported variants retained >80% wild-type efflux.
- Population frequencies should be checked in gnomAD/TOPMed using the exact GRCh build and transcript.
- Disease-causing variants are constitutional/germline, not somatic.

### Modifier, epigenetic and chromosomal findings

- Common *ABCA1*, *ABCG5/ABCG8*, *APOA1*, *LCAT*, *CETP*, *LIPC*, and triglyceride-related alleles may modify the measured lipid profile, but no modifier gene is clinically validated for prognosis in MONDO:0011393.
- miR-33a/b, miR-144 and miR-148a can repress ABCA1 expression in experimental systems. This is regulatory biology, not evidence of a disease-specific epimutation.
- No recurrent aneuploidy, translocation, inversion, methylation defect, or large chromosomal syndrome is established as a cause. Rare intragenic deletions/duplications remain possible.

---

## 5. Environmental information

There is no infectious, toxic, radiological, or occupational cause. Environmental exposures are relevant primarily as:

1. **Phenocopies:** androgen use, severe hypertriglyceridemia, advanced liver disease, monoclonal gammopathy/paraprotein interference, and malignancy.
2. **Cardiovascular modifiers:** smoking, hypertension, diabetes, obesity, poor diet and physical inactivity.
3. **Laboratory modifiers:** acute illness, medications, fasting status, alcohol intake, and marked triglyceride elevation.

Alcohol should not be prescribed to raise HDL because its harms outweigh a biomarker change. Exercise, healthy diet, tobacco avoidance, and weight management are recommended for cardiovascular risk reduction rather than as corrective treatment for the transporter defect.

Suggested environmental annotation: no specific CTD chemical should be designated causal.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous germline pathogenic *ABCA1* variant leads to** reduced production, trafficking, ATPase activity, membrane stability, or apoA-I interaction of the ABCA1 transporter.
2. **Reduced functional ABCA1 at hepatocyte, enterocyte and peripheral-cell membranes leads to** impaired ATP-dependent export of cholesterol and phospholipids to lipid-poor apoA-I.
3. **Impaired lipid transfer leads to** reduced formation of nascent pre-β HDL and accelerated catabolism of poorly lipidated apoA-I.
4. **Reduced nascent-HDL production leads to** low circulating HDL-C and apoA-I; a branch may lead to mild hypertriglyceridemia through altered hepatic lipid handling.
5. **Reduced macrophage cholesterol efflux leads to** intracellular free cholesterol/cholesteryl-ester retention and greater foam-cell propensity.
6. **Foam-cell retention plus conventional vascular risk factors leads to** plaque initiation or progression in arterial walls.
7. **Progressive plaque burden leads to** carotid/coronary atherosclerosis and, variably, angina or myocardial infarction.
8. **Important uncertainty:** the direct step from genetically reduced HDL-C to clinical CAD is not uniformly demonstrated; residual efflux and non-HDL risk factors appear more predictive than HDL concentration alone.

### Molecular pathway

ABCA1-mediated efflux is the first step of reverse cholesterol transport:

- Lipid-poor apoA-I interacts with ABCA1.
- ATP binding and hydrolysis drive conformational changes.
- Cholesterol and phospholipid are extracted/reorganized at the plasma membrane.
- ApoA-I acquires lipids to form discoidal nascent HDL.
- LCAT subsequently esterifies free cholesterol, producing mature spherical HDL.
- HDL cholesterol is delivered to liver directly through SCARB1 or after exchange/remodeling.

Reactome annotations include **HDL assembly, R-HSA-8963896**, and LXR/NR1H2–NR1H3 regulation of cholesterol transport. LXR activation upregulates *ABCA1* transcription as part of a sterol-sensing feedback pathway. [125][126]

### Structural understanding: 2023 development

A 2023 cryo-EM study placed active human ABCA1 in lipid nanodiscs and resolved a 4.0-Å conformation. It found membrane curvature, multiple transporter conformations, and probable lipid densities in a large extracellular hydrophobic pocket. The authors proposed a dynamic “lipid container” model but emphasized that the exact extraction and apoA-I-transfer mechanism remains unresolved. PMID **36889459**, published March 7, 2023. [107]

A complementary 2023 model proposes that ABCA1 extracts phospholipid from the outer membrane leaflet and passes it through a gateway and extracellular tunnel rather than functioning as a conventional alternating-access floppase. This remains a mechanistic model supported by simulation and mutagenesis. PMID **37548415**. [106]

### Cell and tissue contributions

- **Hepatocytes:** principal source of plasma nascent HDL; mouse tissue-specific studies estimate hepatic ABCA1 supplies about 70% of HDL biogenesis.
- **Enterocytes:** contribute approximately 30% in mouse models.
- **Macrophages:** quantitatively smaller contribution to plasma HDL, but critical locally for preventing cholesterol-loaded foam cells.
- **Vascular endothelial and smooth-muscle cells:** ABCA1-dependent membrane cholesterol handling may modify vascular function.
- **Adipocytes and pancreatic β cells:** experimental ABCA1 loss alters glucose homeostasis, but diabetes is not an established core phenotype of heterozygous familial HDL deficiency. [31]

### Suggested mechanism ontology terms

**GO biological process**

- GO:0033344 — cholesterol efflux
- GO:0010875 — positive regulation of cholesterol efflux
- GO:0033700 — phospholipid efflux
- GO:0034378 — chylomicron assembly is not primary; avoid unless specifically supported
- GO:0034380 — high-density lipoprotein particle assembly
- GO:0043691 — reverse cholesterol transport
- GO:0042632 — cholesterol homeostasis
- GO:0006869 — lipid transport
- GO:0006091/other broad metabolic terms should be secondary only

**Cell Ontology**

- CL:0000182 — hepatocyte
- CL:0000584 — enterocyte
- CL:0000235 — macrophage
- CL:0000115 — endothelial cell
- CL:0000192 — smooth muscle cell
- CL:0000057 — fibroblast, relevant to historical efflux assays

**GO cellular components**

- GO:0005886 — plasma membrane
- GO:0010008 — endosome membrane
- GO:0005768 — endosome
- GO:0005764 — lysosome
- GO:0030133 — transport vesicle

### Molecular profiling

- **Lipidomics:** reduced mature α-HDL particles, relative preservation of small pre-β HDL, low apoA-I and variable triglyceride enrichment.
- **Transcriptomics:** no validated patient diagnostic signature. Tangier iPSC-derived hepatocyte dataset **GSE95482** showed absent nascent-HDL formation and altered triglyceride secretion, but represents biallelic deficiency. [218][222]
- **Proteomics/metabolomics:** no disease-specific clinically validated panel beyond apoA-I and HDL subclass analysis.
- **Single-cell/spatial omics:** no robust MONDO:0011393-specific findings.
- **CRISPR/functional genomics:** ABCA1 knockout cell systems and genome-edited pluripotent-stem-cell-derived macrophages recapitulate defective apoA-I-mediated efflux. [219][221]

---

## 7. Anatomical structures affected

### Primary structures

- **Blood/plasma lipoprotein compartment:** low HDL-C and apoA-I.
- **Liver — UBERON:0002107:** reduced hepatic nascent-HDL production.
- **Small intestine — UBERON:0002108:** reduced enterocyte contribution to HDL biogenesis.
- **Arterial wall:** macrophage foam-cell retention and atheroma, especially coronary and carotid arteries.
- **Bone-marrow-derived macrophage system:** relevant cellular mechanism rather than usually apparent organ enlargement in heterozygotes.

### Secondary structures

- **Coronary arteries:** atherosclerosis, stenosis, myocardial ischemia.
- **Carotid arteries:** increased intima-media thickness and plaque.
- **Myocardium:** secondarily affected by ischemia/infarction rather than by direct ABCA1 storage disease.

There is no expected lateralization. Coronary and carotid disease is systemic and may be asymmetric only according to local plaque distribution.

Classic tonsil, spleen, peripheral nerve and corneal involvement should be reserved primarily for biallelic Tangier disease unless specifically documented.

---

## 8. Temporal development

- **Biochemical onset:** congenital/lifelong because the pathogenic variant is present from conception.
- **Recognition:** may occur in childhood during family screening, but many patients are discovered incidentally as adults.
- **Course:** chronic and lifelong; HDL-C remains low, with age-, lifestyle-, metabolic- and treatment-related fluctuations.
- **Vascular stage:** subclinical arterial-wall thickening may precede symptomatic CAD by decades.
- **Advanced stage:** angina, myocardial infarction, revascularization or other atherosclerotic events in a variably penetrant subset.

There are no defined disease stages or spontaneous remissions. LDL-lowering treatment reduces downstream risk but does not normalize ABCA1-mediated HDL formation. The most important opportunity is **early identification before cumulative arterial exposure and conventional risk factors produce plaque**.

---

## 9. Inheritance and population

### Inheritance

- **Autosomal dominant**, caused by one pathogenic *ABCA1* allele.
- An affected heterozygous individual has a nominal **50% chance** of transmitting the variant to each child.
- Two pathogenic alleles cause Tangier disease, producing a gene-dosage/allelic spectrum.
- Expressivity is variable and clinical penetrance for CAD is incomplete and age-dependent.
- Genetic anticipation is not reported.
- Germline mosaicism is theoretically possible but not established as a recurring feature.
- Consanguinity is not required for the dominant disorder; it raises the chance of biallelic disease when a pathogenic allele is present in both parents.

### Epidemiology

The prevalence and incidence of molecularly confirmed primary hypoalphalipoproteinemia-1 are **unknown**. Familial HDL deficiency is considered rare. A population-based sequencing study estimated that rare *ABCA1* variants associated with low HDL may have a minimum frequency around **1 in 1,000**, while approximately 10% of individuals selected from the extreme low-HDL tail carried an *ABCA1* variant; these estimates include variants of variable functional effect and should not be equated with clinically penetrant disease prevalence. [175]

Among 178 probands with HDL-C below the tenth percentile, *ABCA1* mutations were identified in about **9%**; mutations across *ABCA1*, *APOA1*, and *LCAT* explained 42.7% of familial cases versus 14.6% where familial status was uncertain. [174]

### Population distribution

- Disease-causing variants have been reported globally.
- French Canadian families were prominent in the original discovery series, and some cohorts suggested a founder contribution.
- p.Arg230Cys is relatively frequent in Mexican Mestizo and some Indigenous American populations, but it is generally considered a common susceptibility allele rather than a classic high-penetrance familial HDL-deficiency mutation.
- No consistent male:female ratio is expected for autosomal inheritance; sex differences in vascular events may reflect baseline cardiovascular epidemiology rather than transmission.
- There is no validated ethnicity-specific population screening threshold.

---

## 10. Diagnostics

### Clinical diagnostic approach

1. **Confirm persistent low HDL-C** with a repeat fasting lipid profile.
2. Measure total cholesterol, LDL-C, triglycerides, non-HDL-C, apoA-I, apoB and, where appropriate, lipoprotein(a).
3. Exclude severe hypertriglyceridemia, liver failure, renal/thyroid disease, inflammatory illness, androgen exposure, malignancy and paraproteinemia/assay interference.
4. Obtain a three-generation family history of HDL levels and premature vascular disease.
5. Examine for corneal changes, xanthomas, tonsillar discoloration and hepatosplenomegaly; systemic storage findings suggest biallelic disease or another disorder.
6. Perform molecular testing of *ABCA1*, ideally alongside *APOA1* and *LCAT* when the phenotype is not distinctive.
7. Assess cardiovascular burden according to age and risk: blood pressure, diabetes testing, ECG when indicated, coronary calcium/CT angiography, carotid ultrasound or functional ischemia testing based on symptoms and clinical judgment.

In a 2023 clinical report, specialist HDL mapping plus a 24-gene panel identified severe ABCA1 deficiency after conventional lipid testing. The authors concluded that such patients should be referred to a lipid clinic and treatment should optimize non-HDL risk factors. PMID **37545679**. [344]

### Laboratory profile

Typical heterozygous disease:

- HDL-C below the age- and sex-specific fifth percentile or approximately half normal
- Decreased apoA-I
- Normal LDL-C in many patients
- Normal or mildly increased triglycerides
- Reduced large α1/α2 HDL particles
- Reduced apoA-I-mediated cholesterol efflux in specialist research assays

HDL-C under 5 mg/dL, nearly absent apoA-I and only pre-β HDL strongly suggest biallelic Tangier disease, though exceptionally severe heterozygotes and complex genotypes occur.

### Genetic testing

- **Preferred first-line:** *ABCA1* full coding-region and splice-junction sequencing using NGS or Sanger sequencing.
- **If one or no explanatory variant is found:** deletion/duplication analysis by NGS-CNV, MLPA, qPCR or targeted array.
- **Multigene dyslipidemia panel:** include at least *ABCA1, APOA1,* and *LCAT*; broader panels can assess *CETP, LIPC, SCARB1, APOC3, LPL,* and other phenotype-dependent genes.
- **WES/WGS:** appropriate when targeted testing is unrevealing, the phenotype is atypical, or a structural/deep-intronic variant is suspected. WGS offers better noncoding and structural-variant detection.
- **CMA/karyotype/FISH:** low yield and not routine unless syndromic features indicate a chromosomal disorder.
- Mitochondrial and repeat-expansion testing are not indicated.
- GTR lists both coding-sequence and NGS-CNV tests for MONDO:0011393. [418][419]

### Differential diagnosis

| Disorder/cause | Distinguishing findings |
|---|---|
| Biallelic *ABCA1* Tangier disease | HDL-C often <5 mg/dL, extremely low apoA-I, orange tonsils, hepatosplenomegaly, neuropathy, systemic cholesterol-laden macrophages |
| *APOA1*-related hypoalphalipoproteinemia | Absent/reduced apoA-I production, possible xanthomas/corneal opacity; normal ABCA1 efflux machinery |
| Familial LCAT deficiency | Corneal opacity, hemolytic anemia, proteinuria/renal failure; high unesterified cholesterol |
| Fish-eye disease | Partial LCAT deficiency, prominent corneal opacity, generally no renal disease |
| Severe hypertriglyceridemia | Low HDL secondary to TG-rich lipoprotein metabolism |
| Paraproteinemia | Potential assay artifact; discordant lipid methods and monoclonal protein |
| Liver failure/malignancy/androgens | Clinical and biochemical evidence of secondary cause |
| Common polygenic low HDL/metabolic syndrome | Obesity, insulin resistance, high TG; no clearly segregating pathogenic *ABCA1* variant |

### Screening

No population or newborn screening program is established. First-degree relatives should receive lipid/apoA-I testing and, once a familial pathogenic variant is known, targeted genetic testing. Broader dyslipidemia guidance recommends cascade testing beginning with parents, siblings and children and extending through the pedigree. [445]

---

## 11. Outcome and prognosis

No reliable disease-specific 5-year survival, 10-year survival, mortality rate, or life-expectancy estimate exists for monoallelic *ABCA1* familial HDL deficiency.

Most morbidity arises from atherosclerotic cardiovascular disease. Prognosis is expected to depend on:

- residual ABCA1-mediated efflux;
- degree and duration of HDL/apoA-I reduction;
- LDL-C, non-HDL-C, apoB and lipoprotein(a);
- smoking, diabetes, hypertension and obesity;
- age at diagnosis;
- established plaque burden;
- adherence and response to LDL-lowering and other preventive therapy.

The carotid study of 30 mutation carriers found that IMT reached the upper normal limit at age 55 versus 80 in controls and correlated inversely with cholesterol efflux. PMID **11809185**. [74] Conversely, the Danish population data did not demonstrate increased IHD for four heterozygous variants, emphasizing that genotype and low HDL alone are imperfect prognostic markers. [13]

There is no evidence of spontaneous molecular recovery. Cardiovascular risk can be reduced but the underlying HDL-biogenesis defect is lifelong. No validated disease-specific patient-reported outcome or disability scale exists.

---

## 12. Treatment

### Current strategy

There is **no approved treatment that corrects monoallelic ABCA1 deficiency or reliably restores normal HDL formation**. Management targets total atherosclerotic risk, not an arbitrary increase in HDL-C.

| Intervention | Role and evidence | Suggested NCIT intervention concept |
|---|---|---|
| High-intensity statin, e.g. atorvastatin or rosuvastatin | First-line LDL/apoB reduction according to overall ASCVD risk; does not correct ABCA1 function | Statin Therapy / Pharmacologic Intervention |
| Ezetimibe | Add when further LDL-C lowering is needed | Ezetimibe Treatment |
| PCSK9 inhibitor | Consider for established ASCVD or persistently elevated apoB/LDL despite tolerated therapy | PCSK9 Inhibitor Therapy |
| Tobacco cessation | Essential risk reduction | Smoking Cessation Intervention |
| Exercise and Mediterranean-style cardiovascular diet | Improves global risk and fitness; only modest HDL effects expected | Exercise Intervention; Dietary Intervention |
| Blood-pressure and diabetes treatment | Standard guideline-directed prevention | Antihypertensive Therapy; Diabetes Management |
| Aspirin | Secondary prevention or selected high-risk patients, not solely for low HDL | Aspirin Therapy |
| Coronary revascularization | Standard indications for obstructive CAD; not disease-specific | Percutaneous Coronary Intervention / Coronary Artery Bypass Surgery |
| Genetic counseling | Recurrence-risk and family testing | Genetic Counseling |

A 2023 case achieved LDL-C 32 mg/dL with rosuvastatin 40 mg plus ezetimibe 10 mg; HDL remained extremely low, illustrating the intended strategy of reducing non-HDL risk rather than normalizing HDL. [324]

### Treatments not supported for routine use

- **Niacin:** may raise HDL in common dyslipidemia but is often ineffective when the transporter is defective and has not improved outcomes specifically in this disorder.
- **Fibrates:** treat clinically significant hypertriglyceridemia, but should not be used simply to normalize genetically low HDL.
- **CETP inhibitors:** no established disease-specific role.
- **HDL infusion/mimetics:** not proven effective.
- **LXR agonists:** increase ABCA1 expression experimentally but have hepatic lipogenic and other safety limitations; they cannot restore a nonfunctional allele reliably.

### CER-001 trial

The TANGO randomized trial evaluated the HDL mimetic CER-001 in genetically defined familial primary hypoalphalipoproteinemia. After 24 weeks, it did **not** significantly reduce carotid vessel-wall dimensions or arterial-wall inflammation: treatment difference in mean vessel-wall area −0.77 mm², *p*=0.21, with 27 evaluable participants. PMID **32919280**. [329][351]

### Experimental therapy

The 2024 functional study found variant-specific in-vitro rescue with the chemical chaperone **4-phenylbutyrate** or proteasome inhibition. This is hypothesis-generating only: there are no demonstrated clinical response rates or acceptable risk–benefit data for treating patients this way. [298]

No approved gene replacement, CRISPR editing, cell therapy, antisense oligonucleotide, siRNA or mRNA treatment exists for this disease. In principle, liver-directed gene supplementation would need to restore regulated ABCA1 activity without causing inappropriate sterol handling; this remains preclinical.

### Pharmacogenomics

No CPIC or equivalent genotype-guided prescribing guideline exists specifically for *ABCA1*. The causal genotype currently guides diagnosis and intensity of surveillance, not the choice or dose of a particular approved drug.

---

## 13. Prevention

### Primary prevention

The germline variant cannot be prevented after conception. Primary prevention therefore means preventing vascular consequences:

- no tobacco;
- regular aerobic and resistance activity;
- healthy weight;
- Mediterranean-style diet with limited refined carbohydrate and trans/saturated fat;
- blood-pressure and glycemic control;
- early management of elevated LDL-C, non-HDL-C, apoB and lipoprotein(a)-associated risk.

Vaccination has no disease-specific role.

### Secondary prevention

- Cascade lipid and targeted DNA testing in relatives.
- Periodic cardiovascular-risk assessment.
- Selective coronary calcium, carotid imaging or other subclinical-atherosclerosis assessment where results would change management.
- Early treatment of conventional risk factors.

### Tertiary prevention

- Guideline-directed secondary prevention after MI, stroke, peripheral arterial disease or revascularization.
- Cardiac rehabilitation after an event.
- Continued aggressive LDL/apoB lowering and treatment adherence.
- Standard management of heart failure or ischemic complications if they arise.

### Reproductive counseling

An affected heterozygote has a 50% transmission probability. Partner testing becomes particularly relevant if the partner has very low HDL, is related, or comes from a family with *ABCA1*-related disease, because offspring inheriting two pathogenic alleles may develop Tangier disease. Prenatal or preimplantation genetic testing is technically possible after familial variants are defined but is not routinely sought for mild monoallelic disease. Genetic counseling should explicitly discuss VUS uncertainty and the difference between dominant familial HDL deficiency and recessive Tangier disease.

---

## 14. Other species and natural disease

### Naturally occurring model

The strongest natural nonhuman analogue is the **Wisconsin hypoalpha mutant chicken (WHAM)**:

| Attribute | Finding |
|---|---|
| Species | *Gallus gallus*, NCBI Taxon **9031** |
| OMIA | **OMIA:000042-9031** |
| Gene | Chicken *ABCA1* |
| Variant | NM_204145.2:c.265G>A, p.Glu89Lys |
| Origin | Naturally occurring |
| Phenotype | >90% reduction in HDL-C, rapid apoA-I catabolism and reduced phospholipids |
| Mechanism | Defective intracellular trafficking; little ABCA1 reaches the plasma membrane |
| Evidence | PMID **12364545** [181][188] |

A naturally occurring analphalipoproteinemia phenotype is also listed in the golden hamster, *Mesocricetus auratus* (NCBI Taxon **10036**). [183]

These are inherited lipid disorders, not infections, and have no zoonotic or cross-species transmission potential.

---

## 15. Model organisms and experimental systems

### Mouse models

- **Global *Abca1* knockout:** near-absent HDL-C and apoA-I, tissue macrophage lipid accumulation, pulmonary foam cells and altered placental/kidney phenotypes. It models severe biallelic deficiency better than heterozygous human familial HDL deficiency.
- **Heterozygous *Abca1* models:** intermediate efflux/HDL phenotypes, useful for gene-dosage studies.
- **Liver-specific knockout:** plasma HDL falls approximately 70–80%, establishing hepatocytes as the dominant source of circulating HDL.
- **Intestine-specific knockout:** demonstrates the enterocyte contribution.
- **Macrophage/bone-marrow knockout:** useful for local foam-cell and atherosclerosis mechanisms.
- **Endothelial transgenic or knockout models:** study vascular protection, nitric-oxide signaling and diet-induced plaque.
- Crosses with ***Apoe*−/−** or ***Ldlr*−/−** backgrounds are needed to generate robust atherosclerosis because global *Abca1*-null mice do not consistently develop spontaneous human-like CAD. [184][198]

**Limitation:** mouse lipoprotein metabolism differs substantially from humans, including absence of endogenous CETP activity in common laboratory strains; global knockouts also model complete rather than partial deficiency.

### Cellular systems

- Patient skin fibroblasts: historical gold-standard demonstration of reduced apoA-I-mediated efflux.
- HEK293 cells expressing individual ABCA1 variants: scalable functional classification, trafficking and rescue assays.
- THP-1 or primary macrophages: foam-cell and cholesterol-efflux studies.
- CRISPR-edited human pluripotent-stem-cell-derived macrophages: reproduce absent or intermediate efflux according to gene dosage.
- Tangier patient iPSC-derived hepatocyte-like cells: absent nascent-HDL formation and increased triglyceride/ANGPTL3 secretion; useful mechanistically but model biallelic disease. PMID **28330813**. [222]

### Zebrafish

*abca1* perturbation has been used to study cholesterol efflux, HDL-dependent vascular biology and aberrant angiogenesis. It is useful for developmental imaging and genetic screens but does not fully reproduce human lipoprotein composition. [212]

### Applications

These models support:

- pathogenicity testing of VUS;
- ABCA1 trafficking and structural studies;
- quantification of cholesterol/phospholipid efflux;
- identification of chemical chaperones or stabilizers;
- dissection of hepatic versus macrophage contributions;
- preclinical gene-replacement or editing research.

---

## Overall knowledge-base interpretation

Hypoalphalipoproteinemia, primary, 1 should be represented as a **monoallelic, autosomal-dominant *ABCA1* loss-of-function spectrum disorder** whose obligate phenotype is decreased HDL-C/apoA-I and impaired cholesterol efflux. Premature atherosclerosis is important but incompletely penetrant and should be annotated as a variable complication rather than a universal feature. Classic orange tonsils, hepatosplenomegaly and neuropathy belong primarily to **biallelic Tangier disease**.

The most consequential recent advances are not new approved treatments but: (1) active-membrane cryo-EM structures refining the lipid-transport mechanism in 2023; (2) high-throughput functional characterization showing that only 12 of 51 candidate extracellular-domain variants were clearly loss-of-function in 2024; and (3) modern clinical workflows combining apoA-I/HDL subclass analysis, cardiovascular imaging and multigene sequencing. [107][298][343]

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 21 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 20 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0080957` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **primary hypoalphalipoproteinemia 1**
- `CL:0000057` (1 mention) - the report calls it "fibroblast, relevant to historical efflux assays"; CL calls it **fibroblast**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0034378` (1 mention) - the report calls it "chylomicron assembly is not primary"; GO calls it **chylomicron assembly**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`.