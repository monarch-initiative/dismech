---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-23T16:18:51.479093'
end_time: '2026-10-23T16:22:58.824967'
duration_seconds: 247.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 1
  mondo_id: MONDO:0100354
  category: Mendelian
  causal_genes: MYLK
  omim_id: OMIM:249210
  synonyms: Berdon syndrome
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 52
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 8
  validator_version: 0.3.0
term_validation:
  total_terms: 42
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: DOID:0060610
    reported_labels:
    - Disease Ontology, broad MMIHS
    ontology_label: megacystis-microcolon-intestinal hypoperistalsis syndrome
  unresolvable_prefixes:
  - OMIM
  - Gene
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 1
- **MONDO ID:** MONDO:0100354 (if available)
- **Causal gene(s):** MYLK
- **OMIM:** OMIM:249210
- **Synonyms:** Berdon syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome 1** covering all of the
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

# Megacystis–Microcolon–Intestinal Hypoperistalsis Syndrome 1  
**Disease:** MMIHS1 / Berdon syndrome, MYLK-related  
**As-of date:** 23 October 2026

## Executive summary

**Megacystis–microcolon–intestinal hypoperistalsis syndrome 1 (MMIHS1; MONDO:0100354; OMIM:249210) is caused by biallelic loss-of-function variants in *MYLK*, encoding myosin light-chain kinase.** It is an autosomal-recessive, congenital visceral smooth-muscle myopathy in which defective phosphorylation of myosin regulatory light chain impairs actin–myosin contraction, predominantly in the urinary bladder and gastrointestinal tract. The defining manifestations are a massively enlarged but mechanically unobstructed bladder, intestinal hypoperistalsis or chronic intestinal pseudo-obstruction, and usually microcolon. [MYLK](https://www.ncbi.nlm.nih.gov/gene/4638) is **HGNC:7590, NCBI Gene:4638, OMIM:600922**, at 3q21.1. [21][1][91]

The evidence specific to *MYLK*-MMIHS1 remains very limited. The landmark 2017 report described three molecularly confirmed affected individuals from two consanguineous families, carrying either a homozygous frameshift duplication or homozygous splice-altering variant (PMID: **28602422**). A 2024 GeneReviews update still summarized the evidence as two families and three affected persons. A 2025 cohort reported one additional individual labeled as having a *MYLK* p.Gly1607Val variant, but did not report its zygosity, ACMG classification, segregation, or functional validation; it should therefore not yet be treated as established pathogenic evidence. [1][16][37]

**Important scope distinction:** many epidemiologic, management, and survival data below concern genetically heterogeneous MMIHS, especially *ACTG2*-related disease, and cannot automatically be assigned to *MYLK*-MMIHS1. MYLK-specific evidence is explicitly identified wherever possible.

---

## 1. Disease information

### 1.1 Definition

MMIHS is a severe congenital disorder of hollow-viscus smooth muscle characterized by:

- **Megacystis:** massive bladder dilatation without an anatomic outlet obstruction.
- **Intestinal hypoperistalsis:** profoundly reduced or absent intestinal propulsion, producing functional obstruction or chronic intestinal pseudo-obstruction.
- **Microcolon:** an unused, abnormally small-caliber colon, although its absence does not exclude MMIHS.
- Secondary intestinal failure, urinary retention, hydroureteronephrosis, malnutrition, and dependence on parenteral nutrition may follow. [16][61]

The original molecular study summarizes the MYLK form as follows:

> “MMIHS is a congenital disorder characterized by loss of smooth muscle contraction in the bladder and intestine.”  
> — Halim et al., 2017, PMID: **28602422** [1]

### 1.2 Identifiers and nomenclature

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0100354**, megacystis-microcolon-intestinal hypoperistalsis syndrome 1 |
| OMIM phenotype | **OMIM:249210**, MMIHS1 |
| OMIM gene | **OMIM:600922**, *MYLK* |
| Orphanet, broader MMIHS | **ORPHA:2241** |
| MedGen, MYLK-specific | **C5542316** |
| MeSH Supplementary Concept | **C536138** |
| ICD-10 | **Q43.8**, other specified congenital malformations of intestine; not MYLK-specific |
| ICD-11 | **LD2F.1Y**, other specified syndromes with multiple structural anomalies, without predominant body-system involvement |
| Disease Ontology, broad MMIHS | **DOID:0060610** |
| KEGG disease | **H01869** |
| Causal gene | *MYLK*, HGNC:7590; NCBI Gene:4638 |
| Protein | Smooth-muscle myosin light-chain kinase, UniProt **Q15746** |

These ICD, Orphanet, MeSH, and DO identifiers generally designate the broader clinical syndrome rather than specifically the *MYLK* subtype. [49][76][77][78][84][91]

### 1.3 Synonyms

- Megacystis–microcolon–intestinal hypoperistalsis syndrome 1
- MMIHS1
- MYLK-related MMIHS
- Berdon syndrome
- Megacystis–microcolon–intestinal hypoperistalsis syndrome
- Megacystis–microcolon–intestinal hypoperistalsis–hydronephrosis syndrome
- Congenital visceral myopathy, MMIHS spectrum

“Berdon syndrome” and MMIHS without a subtype are umbrella terms and may refer to disease caused by *ACTG2*, *MYH11*, *LMOD1*, *MYL9*, *PDCL3*, *ATP2B4*, or other/unknown causes, not just *MYLK*. [61][19]

### 1.4 Nature of the evidence

The report is based on **aggregated disease resources and published patients**, not individual electronic health records:

- OMIM, MONDO, Orphanet, ClinVar, HPO and GeneReviews: curated disease-level summaries.
- Halim et al. 2017: primary human research on three subjects from two families, plus functional assays and comparison with a mouse model.
- Later cohorts and reviews: retrospective, aggregated syndrome-level evidence.

---

## 2. Etiology, risk factors, and protective factors

### 2.1 Primary cause

The established cause of MMIHS1 is **biallelic germline loss of MYLK function**. The two original families were consanguineous and carried homozygous variants affecting exon 23:

1. A seven-base-pair duplication causing a frameshift and premature termination.
2. A splice-region variant experimentally shown to disrupt normal exon-23 splicing.

Loss of MYLK expression was demonstrated by absent immunohistochemical signal in affected intestine and bladder for the frameshift case; a minigene assay supported abnormal splicing for the second variant. [1]

### 2.2 Risk and protective factors

| Factor category | Current evidence |
|---|---|
| Biallelic pathogenic *MYLK* variants | Established causal risk |
| Heterozygous carrier state | Not known to cause MMIHS1; heterozygous *MYLK* variants can independently cause autosomal-dominant familial thoracic aortic aneurysm/dissection, depending on variant |
| Consanguinity | Increases the probability that both parents carry the same rare recessive allele; both original families were consanguineous |
| Family history/recurrent fetal loss | Important diagnostic clue, particularly fetal megacystis, unexplained intrauterine death, neonatal obstruction, or affected siblings |
| Sex | The broad syndrome has a female predominance, but no MYLK-specific sex effect can be established from three original subjects |
| Environmental, infectious, toxic, dietary or lifestyle exposure | No evidence that these cause MYLK-MMIHS1 |
| Protective genetic variants/modifiers | None established |
| Protective diet/lifestyle | None established for preventing onset |
| Gene–environment interaction | No demonstrated etiologic interaction |

The disorder is congenital and Mendelian; environmental exposures do not substitute for the required biallelic genotype. Postnatal environment and care nevertheless strongly influence complications—particularly catheter infection, parenteral-nutrition-associated liver disease, venous access loss, and malnutrition. [16][1]

### 2.3 Modifier genes and penetrance

No validated modifier gene, protective allele, or epistatic interaction has been reported for *MYLK*-MMIHS1. The small number of known cases prevents reliable estimates of penetrance or genotype–phenotype correlations. The severe phenotype in homozygotes and healthy heterozygous parents in the original families is consistent with high penetrance for those particular biallelic null alleles, but this should not be generalized to every biallelic *MYLK* variant.

---

## 3. Phenotypes

### 3.1 MYLK-specific human observations

The original three molecularly confirmed subjects showed prenatal bladder distension or neonatal gastrointestinal obstruction:

- Two North African siblings had homozygous p.Glu1282GlyfsTer51. One pregnancy was terminated at 15 weeks after fetal megacystis and edema; the other child was born prematurely at 31 weeks and died with respiratory distress. An older likely affected sibling had bladder distension and died in utero at 30 weeks.
- The Indian proband with the homozygous splice variant presented at two days with bilious vomiting. Findings included malrotation, distal microcolon, megacystis, and bilateral hydroureteronephrosis; ganglion cells were present in ileum, arguing against Hirschsprung disease. [1]

### 3.2 Phenotype annotations

| Phenotype | Type and characteristics | MYLK-specific evidence/frequency | Suggested HPO term |
|---|---|---|---|
| Megacystis | Congenital imaging/physical sign; severe, persistent, non-obstructive bladder enlargement | Present in the reported MYLK families; prenatal in several affected pregnancies | **HP:0000021 Megacystis** |
| Intestinal hypoperistalsis | Functional sign; severe, chronic/lifelong; causes pseudo-obstruction | Defining feature | **HP:0100771 Hypoperistalsis** |
| Microcolon | Imaging/surgical sign; congenital, generally stable structural consequence of fetal disuse | Documented in the live-born original proband and 2025 MYLK-labeled patient | **HP:0004388 Microcolon** |
| Abdominal distention | Clinical sign, usually neonatal and recurrent | Common syndrome-wide | **HP:0003270 Abdominal distention** |
| Bilious vomiting/nausea and vomiting | Symptom of functional obstruction; neonatal or recurrent | Original proband presented at two days | **HP:0002017 Nausea and vomiting**; bilious vomiting may be encoded under vomiting |
| Failure to pass meconium | Neonatal symptom of intestinal obstruction | Typical syndrome-wide; not documented for every MYLK case | **HP:0011968 Feeding difficulties in infancy** is not equivalent; use a specific “delayed passage of meconium” term where supported |
| Chronic intestinal pseudo-obstruction | Clinical syndrome; severe, recurrent or continuous | Expected downstream manifestation | **HP:0004389 Intestinal pseudo-obstruction** |
| Intestinal malrotation | Congenital structural finding | Present in the original Indian MYLK case | **HP:0002566 Intestinal malrotation** |
| Duodenal stenosis | Congenital structural sign | Reported in the 2025 MYLK-labeled patient | **HP:0100867 Duodenal stenosis** |
| Urinary retention/acontractile bladder | Functional urologic sign, congenital/chronic | Central expected manifestation | **HP:0000016 Urinary retention**; **HP:0031047 Acontractile bladder** if available in local HPO release |
| Hydroureter/hydronephrosis | Imaging sign, secondary to bladder dysfunction | Bilateral hydroureteronephrosis in the original live-born case | **HP:0000072 Hydroureter**; **HP:0000126 Hydronephrosis** |
| Polyhydramnios or oligohydramnios | Prenatal sign; variable | Polyhydramnios in one family; severe oligohydramnios/anhydramnios in another | **HP:0001561 Polyhydramnios**; **HP:0001562 Oligohydramnios** |
| Prematurity | Birth characteristic | One original child born at 31 weeks | **HP:0001622 Premature birth** |
| Intestinal failure | Functional/metabolic consequence; chronic and severe | Common syndrome-wide and in the 2025 MYLK-labeled patient | **HP:0005244 Gastrointestinal dysmotility** plus clinical intestinal-failure annotation |
| Malnutrition/growth impairment | Clinical/laboratory consequence | Variable with nutritional support | **HP:0001508 Failure to thrive** |
| Cholestasis/IFALD | Laboratory and organ complication of parenteral nutrition | Reported in the 2025 MYLK-labeled patient | **HP:0001396 Cholestasis**; **HP:0001392 Abnormality of the liver** |
| Cholelithiasis | Imaging/clinical complication | Reported in that patient | **HP:0001081 Cholelithiasis** |

The canonical Orphanet HPO set includes abdominal distention, hypoperistalsis, megacystis, microcolon, and nausea/vomiting. [85]

### 3.3 Age, severity, and course

- **Onset:** prenatal or neonatal.
- **Severity:** usually severe in documented null-variant cases.
- **Course:** congenital, chronic, and non-remitting; complications accumulate through intestinal failure, urinary stasis, infection, malnutrition, renal injury, and treatment toxicity.
- **Frequency:** precise MYLK-specific percentages cannot be calculated from three original molecularly established subjects. Broad-MMIHS frequencies must not be substituted as MYLK-specific frequencies.

### 3.4 Quality of life

No MYLK-specific EQ-5D, SF-36, PROMIS, or pediatric quality-of-life study was found. Major burdens include:

- Long-term central venous access and parenteral nutrition.
- Catheterization or urinary diversion.
- Repeated hospitalizations and abdominal operations.
- Stomas, feeding tubes, oral aversion and restricted oral intake.
- Infection and liver-disease risk.
- Caregiver burden and limitations on normal daily activities.

Modern intestinal rehabilitation can support long-term survival and near-normal growth, but does not establish normal quality of life or cure the underlying dysmotility. [72]

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Attribute | Annotation |
|---|---|
| Gene symbol | ***MYLK*** |
| Full name | Myosin light-chain kinase |
| HGNC | **HGNC:7590** |
| NCBI Gene | **4638** |
| OMIM gene | **600922** |
| Cytogenetic location | **3q21.1** |
| Protein | MLCK; UniProt **Q15746** |
| Enzyme | EC **2.7.11.18** |
| Principal function | Calcium/calmodulin-dependent phosphorylation of myosin regulatory light chain, facilitating actin–myosin interaction and contraction |
| Disease inheritance | Autosomal recessive for MMIHS1; distinct heterozygous variants can cause autosomal-dominant familial thoracic aortic aneurysm/dissection 7 |

MYLK encodes long non-muscle MLCK, short smooth-muscle MLCK, and telokin transcripts. The established MMIHS variants affect both long and short MLCK isoforms. UniProt annotates immunoglobulin-like domains, a fibronectin type-III domain, and a C-terminal serine/threonine protein-kinase domain. [90][92]

### 4.2 Pathogenic variants

| Variant, reference transcript | Type; origin | Evidence/classification | Functional consequence | Population frequency |
|---|---|---|---|---|
| **NM_053025.3:c.3838_3844dupGAAAGCG; p.Glu1282GlyfsTer51**; GRCh37 g.123383093_123383099dup; rs1553787823 | Homozygous germline frameshift duplication; exon 23 | Established pathogenic/causal in two siblings; ClinVar SCV000299345; OMIM 600922.0003 | Premature stop near exon 24; absent MYLK immunostaining in affected bladder and intestine, supporting loss of expression/LoF | Exact gnomAD AF was not reported in the primary paper |
| **NM_053025.3:c.3985+5C>A**, represented on the current transcript/strand as **NM_053025.4:c.3985+5G>T**; rs1553787619 | Homozygous germline intronic SNV | ClinVar pathogenic; Variation ID 1473634; OMIM 600922.0004 | Minigene assay eliminated normal 414-bp product; predicted exon-23 skipping, frameshift and premature stop | Exact AF was not given in the primary report |
| **c.4820G>T; p.Gly1607Val** | Missense; zygosity unreported in 2025 cohort | Insufficient publicly reported evidence for pathogenicity in MMIHS1 | No segregation or functional assay reported | Not adequately documented |

The differing c.3985+5 nucleotide descriptions reflect transcript/strand representation; they refer to the same reported genomic change at GRCh37 chr3:123382947 C>A. [120][122][135][136]

> “Expression studies and splicing assays indicated that both variants affect normal *MYLK* expression.”  
> — Halim et al., PMID: **28602422** [1]

### 4.3 Variant interpretation cautions

- MMIHS1 is recessive; a single heterozygous VUS does not establish the diagnosis.
- Truncating variants must be evaluated for affected isoforms and nonsense-mediated decay.
- Missense variants require careful assessment of allele frequency, phase, segregation, functional domain, computational evidence and ideally functional validation.
- *MYLK* has a separate dominant aortopathy association; variant interpretation must be phenotype- and inheritance-specific.
- The 2025 p.Gly1607Val observation should remain a candidate/VUS-level disease association unless further evidence becomes available.

### 4.4 Other molecular features

| Category | Evidence |
|---|---|
| Somatic variants | No role established; reported MMIHS1 variants are germline |
| Large chromosomal abnormalities | None established as a recurrent cause of MYLK-MMIHS1 |
| CNVs | No MYLK deletion/duplication class firmly established for MMIHS1, although exon-level CNV testing remains diagnostically appropriate |
| Modifier genes | None validated |
| DNA methylation/epigenetic signature | No disease-specific episignature reported |
| Repeat expansion | Not applicable |
| Mitochondrial genome | Not implicated |
| Pharmacogenomics | No MYLK-specific treatment-response guideline |

---

## 5. Environmental, lifestyle, and infectious information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol, diet, exercise pattern, bacterial agent, virus, fungus, or parasite is known to cause or trigger MYLK-MMIHS1.

Environmental and healthcare exposures affect **complications**, not the congenital etiology:

- Central venous catheters create infection and thrombosis risk.
- Prolonged parenteral nutrition can cause cholestasis and intestinal-failure-associated liver disease.
- Medications that reduce gastrointestinal or bladder motility can worsen functional obstruction and should be avoided or minimized.
- Catheter-care practices, optimized lipid formulations and specialist intestinal rehabilitation can reduce secondary harm. [16][72]

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Biallelic germline loss-of-function variants in *MYLK*** lead to absent or severely reduced functional smooth-muscle MLCK.
2. **Reduced MLCK activity** leads to inadequate calcium/calmodulin-dependent phosphorylation of myosin regulatory light chain, principally MYL9.
3. **Insufficient regulatory-light-chain phosphorylation** leads to reduced myosin activation and impaired myosin-head interaction with actin filaments.
4. **Defective actin–myosin interaction** results in greatly reduced force generation by visceral smooth-muscle cells.
5. **In bladder detrusor smooth muscle**, impaired contraction leads to failure of bladder emptying, urinary retention and non-obstructive megacystis.
6. **Urinary stasis and high residual volume** lead secondarily to hydroureter, hydronephrosis, infection, renal scarring and potentially kidney failure.
7. **In gastrointestinal muscularis smooth muscle**, impaired contraction leads to weak or absent peristalsis and functional intestinal obstruction.
8. **Prenatal intestinal disuse** is inferred to contribute to microcolon; abnormal smooth-muscle development/function may also contribute.
9. **Postnatal dysmotility** leads to bilious vomiting, abdominal distention, pseudo-obstruction, feeding intolerance and intestinal failure.
10. **Intestinal failure** leads to parenteral-nutrition dependence, which branches into central-line infection/thrombosis and IFALD/cholestasis.
11. **Severe visceral dysfunction and treatment complications** lead to major morbidity, transplantation or death.

Steps 1–4 are supported by human variant assays, protein biology and mouse knockout studies. The exact developmental link between hypomotility and microcolon is biologically plausible but incompletely demonstrated specifically in MYLK patients.

### 6.2 Molecular pathway

Physiologic smooth-muscle contraction follows:

**agonist/depolarization → intracellular Ca²⁺ elevation → Ca²⁺/calmodulin complex → MYLK activation → MYL9/regulatory-light-chain phosphorylation → myosin ATPase activation → actin–myosin cross-bridge cycling → contraction.**

MYLK loss interrupts this pathway upstream of cross-bridge formation. This is primarily a contractile-signaling disorder, not a Wnt, MAPK, mTOR, PI3K–AKT, inflammatory, or metabolic-storage disease. [90][105]

Suggested ontology annotations:

- **GO:0004687** myosin light-chain kinase activity
- **GO:0005516** calmodulin binding
- **GO:0006939** smooth-muscle contraction
- **GO:0031032** actomyosin structure organization
- **GO:0007015** actin filament organization
- **GO:0005524** ATP binding
- **GO:0004674** protein serine/threonine kinase activity

### 6.3 Cellular and tissue mechanism

Immunohistochemistry localized MYLK to smooth-muscle cells in all muscular layers of control fetal intestine and bladder. Affected tissues showed absent MYLK signal but no major change in neurofilament, c-Kit/CD117, mast-cell tryptase or ACTA2 staining, and retained gross cellular architecture. This favors a **primary smooth-muscle functional myopathy**, rather than aganglionosis, loss of interstitial cells of Cajal, or destructive inflammation. [1]

> “Although MYLK is instrumental for the proper function of SMCs, its presence is not required for maintaining the structural architecture of these organs.”  
> — Halim et al., PMID: **28602422** [1]

Suggested cell annotations:

- **CL:0000192** smooth-muscle cell
- Visceral smooth-muscle cell / bladder detrusor myocyte, where supported by the local ontology version
- Enteric neurons and interstitial cells of Cajal are relevant differential cell populations, but are not established as the primary lesion.

### 6.4 Protein dysfunction and subcellular localization

The established variants cause loss of functional MLCK rather than a demonstrated gain-of-function or dominant-negative effect. Relevant compartments include:

- Cytoplasm — **GO:0005737**
- Actin cytoskeleton — **GO:0015629**
- Stress fiber — **GO:0001725**
- Actomyosin contractile apparatus
- Lamellipodium and cleavage furrow for non-muscle isoforms

MLCK itself is not an organelle-resident enzyme; the pathogenic deficit is in cytoplasmic/cytoskeletal contractile signaling. [92]

### 6.5 Metabolic, immune, and tissue-injury components

- No primary metabolic block or disease-specific metabolomic signature is known.
- No primary autoimmunity or immunodeficiency is implicated.
- Inflammation, fibrosis, cholestasis and renal injury are secondary complications rather than initiating mechanisms.
- Sepsis reflects catheter or urinary complications, not an intrinsic immune defect.
- No disease-specific bulk RNA-seq, single-cell, spatial transcriptomic, proteomic, lipidomic or multi-omic patient atlas was identified.
- No published MYLK-directed CRISPR therapeutic screen, patient-derived intestinal organoid or iPSC correction study has yet established a treatment strategy.

---

## 7. Anatomical structures affected

| Level | Structure/cell/compartment | Role |
|---|---|---|
| Primary organ | Urinary bladder — **UBERON:0001255** | Detrusor acontractility, megacystis, urinary retention |
| Primary organ | Small intestine — **UBERON:0002108** | Hypoperistalsis, dilatation, pseudo-obstruction |
| Primary organ | Colon — **UBERON:0001155** | Microcolon and dysmotility |
| Tissue | Muscularis externa / smooth-muscle layers | Principal contractile lesion |
| Cell | Smooth-muscle cell — **CL:0000192** | Loss of MLCK-dependent contraction |
| Secondary structures | Ureters, renal pelvis and kidney | Hydroureteronephrosis, infection, scarring and possible renal failure |
| Secondary organ | Liver and biliary tract | IFALD, cholestasis, gallstones secondary to prolonged parenteral nutrition |
| Secondary system | Central venous system | Catheter infection, thrombosis and access loss |
| Subcellular | Cytoplasm and actin cytoskeleton | MLCK–MYL9–actomyosin pathway |

The gastrointestinal and urinary involvement is generally midline or bilateral/systemic rather than unilateral; hydroureteronephrosis may be bilateral, as in the original MYLK proband. [1]

---

## 8. Temporal development and natural history

### 8.1 Onset

- Pathology begins in fetal life.
- Fetal megacystis can be visible during the first or second trimester.
- Gastrointestinal abnormalities are less readily detected prenatally.
- Live-born infants usually present in the first days of life with abdominal distention, bilious emesis, failure to pass meconium, or inability to void. [16]

Syndrome-wide, prenatal bladder manifestations were reported in approximately **88%**, gastrointestinal abnormalities in **24%**, and prenatal suspicion of the full syndrome in **26%**. These figures are not MYLK-specific. [16]

### 8.2 Course

A practical course model is:

1. **Prenatal stage:** megacystis ± hydroureteronephrosis; abnormal amniotic-fluid volume; occasionally dilated stomach/bowel.
2. **Neonatal stage:** functional bowel obstruction, vomiting, abdominal distention and urinary retention.
3. **Early chronic stage:** decompressive procedures, catheterization or vesicostomy, parenteral nutrition.
4. **Advanced intestinal failure:** recurrent pseudo-obstruction, line infections, IFALD, venous-access loss and recurrent urinary infection.
5. **End-stage/definitive-support stage:** long-term home parenteral nutrition or intestinal/multivisceral transplantation.

Spontaneous remission is not expected. Intestinal rehabilitation can reduce complications and transplantation can restore enteral autonomy, but neither proves correction of the underlying germline defect.

### 8.3 Critical windows

- **Prenatal:** recognition of non-obstructive megacystis permits targeted counseling and molecular testing.
- **Immediately postnatal:** distinguish functional obstruction from surgically correctable atresia, volvulus or Hirschsprung disease; decompress bladder and bowel.
- **Before irreversible renal injury:** institute reliable bladder drainage.
- **Before advanced IFALD or loss of venous access:** optimize parenteral nutrition and consider transplant evaluation.

---

## 9. Inheritance and population

### 9.1 Inheritance

MYLK-MMIHS1 is **autosomal recessive**:

- If both parents are carriers, each pregnancy has:
  - 25% probability of an affected child.
  - 50% probability of an unaffected carrier.
  - 25% probability of an unaffected non-carrier.
- Both sexes can be affected.
- Carriers are not expected to develop MMIHS1.
- Germline mosaicism has not been specifically demonstrated.
- Genetic anticipation is not applicable.
- No MYLK-MMIHS1 founder allele has been established.
- Consanguinity was present in both original families and is an important risk context. [1][16]

### 9.2 Epidemiology

Orphanet estimates broad MMIHS prevalence at **<1 per 1,000,000**. Incidence is unknown. Orphanet historically summarized approximately 230 reported patients, whereas later literature reviews cited about 450 cases and a 2025 paper cited 762 reports through 2023; these differences reflect publication date, inclusion criteria and duplicate-case risk. [61][72][62]

Broad-MMIHS population observations include:

- Female-to-male ratio approximately **2.3:1** in an earlier review.
- Orphanet reported about **71% female**.
- A 2025 cohort was **62% female**.
- These sex ratios should not be interpreted as a MYLK-specific penetrance effect. [61][72][34]

No carrier frequency, birth incidence, high-prevalence ethnicity, geographic cluster or MYLK founder effect can currently be estimated.

---

## 10. Diagnostics

### 10.1 Clinical recognition and imaging

Diagnosis begins with the combination of non-obstructive megacystis and intestinal dysmotility, with or without microcolon.

| Test | Expected information |
|---|---|
| Prenatal ultrasound | Megacystis, hydroureteronephrosis, normal/increased or sometimes reduced amniotic fluid; later dilated stomach/bowel |
| Fetal MRI | May demonstrate dilated esophagus or microcolon |
| Abdominal radiograph | Gastric/small-bowel dilatation and paucity of distal gas |
| Upper-GI contrast series | Dysmotility, dilated stomach/small bowel, malrotation |
| Contrast enema | Microcolon and possible malrotation |
| Kidney/bladder ultrasound | Large-capacity bladder, hydronephrosis, renal parenchymal changes |
| Voiding cystourethrogram | Excludes outlet obstruction; assesses reflux and bladder capacity |
| Urodynamics | Acontractile, high-capacity bladder with poor emptying |
| Renal scan | Renal scarring or differential function |
| Bowel biopsy | May show preserved ganglion cells; useful chiefly to exclude Hirschsprung disease |
| Endoscopy/CT/MRI | Used selectively to exclude mechanical obstruction or proximal stenosis |

There is no diagnostic serum enzyme assay or validated circulating biomarker for MYLK-MMIHS1. [16]

### 10.2 Laboratory monitoring

Laboratory studies assess complications rather than establish the primary diagnosis:

- Creatinine, blood urea nitrogen, electrolytes and estimated GFR.
- AST, ALT, alkaline phosphatase, total/direct bilirubin.
- Albumin, PT/INR and PTT.
- Full blood count and cultures during suspected infection.
- Fat-soluble vitamins, trace elements and other nutritional indices.

### 10.3 Genetic-testing strategy

1. **MMIHS/pediatric intestinal pseudo-obstruction multigene panel** with sequencing and deletion/duplication analysis. At minimum include:
   - *ACTG2, MYLK, MYH11, LMOD1, MYL9, PDCL3,* and *ATP2B4*.
   - Consider other visceral-myopathy, enteric neuropathy and mitochondrial genes according to phenotype.
2. **Trio exome sequencing** if panel testing is negative or the phenotype is atypical.
3. **Genome sequencing** for unresolved cases, particularly possible intronic, structural or regulatory variants.
4. **Targeted familial-variant testing** for relatives once causal biallelic variants are known.
5. Confirm phase: two variants must be shown or strongly inferred to be **in trans**.
6. RNA or minigene testing may clarify suspected splice variants.

CMA and karyotyping can investigate broader congenital anomalies but are not preferred tests for isolated suspected MYLK-MMIHS1. FISH, mitochondrial sequencing and repeat-expansion testing are not routine unless another diagnosis is suspected. [16]

### 10.4 Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| Mechanical lower urinary-tract obstruction | Posterior urethral valves, urethral atresia or stenosis visible by imaging/cystoscopy |
| Hirschsprung disease | Rectal aganglionosis; typically no massive non-obstructive megacystis |
| Small-bowel or colonic atresia | Fixed anatomic obstruction; not generalized smooth-muscle failure |
| Intestinal malrotation/volvulus | Mechanical component demonstrable radiologically or surgically; malrotation may coexist with MMIHS |
| Meconium ileus/cystic fibrosis | CFTR disease, pancreatic insufficiency, characteristic meconium obstruction |
| Prune-belly sequence | Abdominal-wall and urinary anomalies; microcolon/hypoperistalsis not necessarily present |
| ACTG2-related MMIHS | Usually heterozygous, often de novo; clinically overlapping |
| MYH11-related smooth-muscle dysfunction | May include mydriasis and vascular abnormalities |
| MYL9-related MMIHS | Mydriasis may be prominent |
| Congenital enteric neuropathies/mitochondrial disorders | Neuropathic or multisystem findings rather than isolated contractile-protein defect |
| Medication-induced neonatal ileus | Maternal magnesium/opioid exposure; no congenital triad |
| Sepsis or hypothyroidism | Laboratory evidence and absence of characteristic congenital anatomy |

### 10.5 Screening

There is no population newborn-screening program. Appropriate targeted screening includes:

- Prenatal ultrasound in at-risk pregnancies.
- Carrier testing for adult relatives once familial variants are known.
- Cascade testing of relatives.
- Prenatal diagnosis by chorionic-villus sampling or amniocentesis.
- Preimplantation genetic testing for monogenic disease.

---

## 11. Outcome and prognosis

### 11.1 MYLK-specific prognosis

The original MYLK families had severe outcomes—termination, intrauterine death, neonatal death and death in an affected girl—but follow-up details were limited. These outcomes support severe prenatal/neonatal disease for the reported null alleles, but are insufficient to calculate MYLK-specific survival.

The 2025 cohort’s single MYLK-labeled patient was alive at 58 months but required proximal jejunostomy and parenteral nutrition and had persistent ileus, IFALD and cholelithiasis. Because variant pathogenicity details were incomplete, this is supportive but not definitive MYLK natural-history evidence. [37]

### 11.2 Syndrome-wide survival

Historical and modern results differ dramatically:

| Study/era | Survival |
|---|---|
| Published cases, 1976–2004 | 12.6% |
| Published cases, 2004–2011 | 55.6% |
| Japanese nationwide survey | 63% at 5 years; 57% at 10 years |
| Specialized-center cohort, publication 2021 | 100% at 5 years; 100% at 10 years; 86% at 20 years |
| German rehabilitation cohort, 2012–2025 | 88% alive at follow-up, 23/26 |

Improved survival is attributed to multidisciplinary intestinal rehabilitation, better parenteral nutrition, catheter-infection prevention, IFALD management and transplantation. These figures combine genotypes and should not be represented as MYLK-specific survival estimates. [16][72][37]

### 11.3 Major morbidity and causes of death

- Intestinal failure and malnutrition.
- Central-line bloodstream infection and sepsis.
- Venous thrombosis or loss of central access.
- IFALD, cholestasis and liver failure.
- Recurrent urinary tract infection, renal scarring and kidney failure.
- Surgical complications.
- Transplant rejection, infection and treatment-related mortality.
- Respiratory complications of prematurity or severe abdominal distention.

No validated MYLK-specific prognostic biomarker exists. Genotype class, residual contractile activity, severity of bladder/intestinal dysfunction, preservation of renal/liver function and absence of line complications are biologically plausible predictors but are not formally validated.

---

## 12. Treatment

There is **no approved disease-modifying, gene, RNA, or cell therapy for MYLK-MMIHS1**. Care is supportive and multidisciplinary.

### 12.1 Practical treatment algorithm

1. Exclude surgically correctable mechanical obstruction.
2. Decompress the bladder and protect kidneys.
3. Decompress the gastrointestinal tract and correct malrotation, volvulus or stenosis when present.
4. Establish safe nutrition—minimal enteral feeding where tolerated plus parenteral nutrition as needed.
5. Prevent catheter infection, thrombosis, micronutrient deficiency and IFALD.
6. Monitor renal, liver, nutritional and growth status.
7. Refer early to an intestinal-rehabilitation and transplant center.
8. Consider intestinal or multivisceral transplantation for life-threatening intestinal-failure complications.

### 12.2 Interventions

| Intervention | Purpose/evidence | Important risks | Suggested NCIT concept |
|---|---|---|---|
| Clean intermittent catheterization | Bladder emptying and prevention of renal injury | UTI, urethral trauma | Urinary Catheterization |
| Vesicostomy/cystostomy | Continuous bladder decompression when catheterization is inadequate | Infection, stenosis, skin complications | Vesicostomy; Cystostomy |
| Gastrostomy | Gastric decompression, relief of vomiting/distention, feeding access | Infection, leakage, granulation | Gastrostomy |
| Jejunostomy/ileostomy/colostomy | Selective decompression or diversion | Low output, fluid loss, adhesions and repeat surgery; usefulness must be individualized | Jejunostomy; Ileostomy; Colostomy |
| Parenteral nutrition | Sustains growth and life in intestinal failure | CLABSI, thrombosis, IFALD, metabolic bone disease | Parenteral Nutrition |
| Minimal enteral/oral feeding and feeding therapy | Preserves oral skills and may reduce oral aversion where safe | Aspiration, vomiting | Enteral Nutrition; Feeding Therapy |
| Antibiotics | Treatment of line, urinary or other infections; not primary therapy | Resistance and toxicity | Antibiotic Therapy |
| Intestinal transplantation | For irreversible intestinal failure with life-threatening PN complications | Rejection, infection, graft loss and mortality | Intestinal Transplantation |
| Multivisceral transplantation | For combined intestinal/liver or broader organ failure | Major operative and immunosuppressive risks | Multivisceral Transplantation |

### 12.3 Pharmacotherapy

No prokinetic has demonstrated reliable correction of the underlying visceral myopathy. Reviews state that patients generally do not respond to prokinetic agents or gastrointestinal hormones. Drugs that diminish bowel or bladder motility—particularly anticholinergic, opioid and other constipating agents—should be avoided or minimized when clinically possible. [72][16]

### 12.4 Outcomes of nutritional and transplant care

In a specialized-center series:

- 13/25 patients underwent intestinal or multivisceral transplantation.
- Nearly all sufficiently followed transplanted patients achieved enteral autonomy.
- Non-transplanted survivors remained dependent on parenteral nutrition.
- Estimated 5-, 10- and 20-year survival was 100%, 100% and 86%.
- Growth did not differ significantly between transplanted and non-transplanted groups. [72]

These are observational, single-center data without randomization and include no genetically confirmed MYLK patient.

### 12.5 Advanced and experimental therapies

No MYLK-targeted gene replacement, CRISPR editing, mRNA replacement, antisense oligonucleotide, smooth-muscle cell therapy or approved targeted small molecule was identified in clinical use. Major translational obstacles include:

- Achieving broad delivery to bladder and gastrointestinal smooth muscle.
- Restoring expression during fetal/early developmental stages.
- Avoiding excessive vascular or non-muscle MLCK activity.
- Treating extensive established organ dysfunction.

No MMIHS1-specific pharmacogenomic guidance or treatment-response rate is available.

---

## 13. Prevention

### 13.1 Primary prevention

The disease cannot be prevented through vaccination, diet, exercise, toxin avoidance or infection control. Genetic reproductive options include:

- Carrier testing of the reproductive partner of a known carrier.
- Preimplantation genetic testing for monogenic disease.
- Prenatal molecular diagnosis where familial variants are known.
- Donor gametes or other reproductive options after nondirective counseling.

### 13.2 Secondary prevention

Early detection can reduce diagnostic delay and avoid inappropriate repeated surgery:

- Targeted fetal ultrasound in at-risk pregnancies.
- Prompt molecular testing when fetal megacystis occurs without lower urinary obstruction.
- Neonatal bladder/renal imaging and contrast evaluation of the bowel.
- Cascade testing in known families.

### 13.3 Tertiary prevention

- Reliable bladder drainage to prevent infection, reflux, renal scarring and kidney failure.
- Central-line bundles and lock protocols to reduce bloodstream infection.
- Optimized parenteral-nutrition cycling, glucose delivery and lipid formulation to reduce IFALD.
- Nutritional and micronutrient surveillance.
- Early treatment of urinary infection.
- Avoidance of unnecessary surgery and motility-suppressing drugs.
- Early transplant-center referral before irreversible liver failure or loss of venous access. [16][72]

No immunization specifically prevents MMIHS, but routine immunization is important in medically fragile and transplant-candidate patients.

---

## 14. Other species and natural disease

| Category | Finding |
|---|---|
| Human | *Homo sapiens*, NCBI Taxon **9606**; naturally occurring MMIHS1 |
| Other naturally affected species | No well-established spontaneous veterinary equivalent caused by biallelic *MYLK* variants was identified |
| Breed association | None established; no applicable VBO breed term |
| Zoonotic transmission | Not applicable |
| Cross-species transmission | Not applicable |
| Ortholog conservation | MYLK/MLCK contractile function is strongly conserved among vertebrates |
| Veterinary relevance | Primarily comparative/experimental rather than a recognized naturally occurring breed disease |

The absence of a reported natural animal syndrome should not be interpreted as proof that none exists; current evidence is dominated by engineered mouse models.

---

## 15. Model organisms and experimental systems

### 15.1 Conditional mouse model

The key model is an inducible smooth-muscle-specific *Mylk* knockout mouse:

- **Species:** *Mus musculus*, NCBI Taxon **10090**.
- **Model type:** mammalian, conditional knockout.
- **Engineering:** deletion of *Mylk* exons 23–25 using smooth-muscle-22α/**TAGLN** Cre-ERT2.
- **Phenotypes:** severe gut dysmotility, weak peristalsis, gastrointestinal dilatation, reduced food intake and fecal output, abnormal bladder function, hypotension and death after induction.
- Ileal strips generated approximately **13% of control tension** and lacked the normal initial KCl-induced contraction peak.
- The model directly supports the role of MLCK and regulatory-light-chain phosphorylation in gastrointestinal and bladder smooth-muscle function. He et al., *Gastroenterology*, 2008, PMID: **18586037**. [110][117]

> “Targeted deletion of MLCK in adult mouse smooth muscle resulted in severe gut dysmotility characterized by weak peristalsis, dilation of the digestive tract, and reduction of feces excretion and food intake.”  
> — He et al., 2008, PMID: **18586037** [110]

### 15.2 Model strengths and limitations

| Feature | Assessment |
|---|---|
| Recapitulates weak intestinal propulsion | Strong |
| Recapitulates bladder dysfunction | Strong |
| Demonstrates reduced contractile force and impaired RLC phosphorylation | Strong |
| Models complete human developmental onset | Limited—the deletion is experimentally induced, often after development |
| Recapitulates human microcolon | Not clearly established |
| Models exact human alleles | No; it is a conditional knockout rather than variant-specific knock-in |
| Models long-term PN/transplant complications | No |
| Separates smooth-muscle from enteric-neural disease | Strong, because deletion is smooth-muscle targeted |
| Drug-testing usefulness | Good for pathway and contractility studies, but toxicity and systemic vascular effects must be considered |

### 15.3 Cellular and advanced models

No validated patient-derived MYLK-MMIHS1 iPSC smooth-muscle line, bladder organoid, intestinal neuromuscular organoid, variant-specific mouse knock-in, zebrafish model, spatial transcriptomic atlas or high-throughput CRISPR therapeutic screen was identified. These represent important research priorities.

---

## Recent developments and expert assessment

### 2023–2024

- A 2023 whole-genome sequencing study of visceral myopathy found heterozygous *MYLK* variants but judged them unlikely to explain disease because established MYLK-MMIHS is biallelic and loss-of-function. This reinforces strict recessive variant interpretation. [162]
- A 2024 genetics review listed *MYLK* among recognized MMIHS genes but did not provide substantial new MYLK-specific primary cases (PMID: **38461165**). [35]
- The August 2024 GeneReviews update emphasized phenotype-directed multigene panels/exome sequencing, prenatal recognition, bladder protection, intestinal rehabilitation, parenteral nutrition and transplantation. It still counted only two MYLK families/three persons. [16]
- A 2024 practical guide to chronic intestinal pseudo-obstruction recognized biallelic MYLK loss-of-function as a recessive cause and summarized the kinase’s role in phosphorylating myosin light chains for actin–myosin contraction. [3]

### Current expert interpretation

1. **Gene–disease validity is strong but the human evidence base is small.** The two independent families, recessive segregation, consistent phenotype, loss-of-expression/splicing assays and highly concordant conditional mouse model support causality.
2. **The mechanism is a primary visceral myopathy.** Preserved ganglia and gross tissue architecture, together with loss of MLCK-dependent contractility, argue against primary enteric neuropathy.
3. **Variant interpretation must remain conservative.** A heterozygous or isolated missense variant should not be labeled causal without a second allele and convincing segregation/functional evidence.
4. **Modern supportive care has transformed survival**, but published survival estimates are largely syndrome-wide and enriched for *ACTG2*, not MYLK.
5. **Major research gaps** are MYLK-specific natural history, penetrance, residual-function genotype–phenotype correlation, validated patient-derived models, longitudinal quality-of-life data and disease-modifying therapy.

## Overall knowledge-base conclusion

MMIHS1 is a very rare, autosomal-recessive congenital visceral myopathy caused by biallelic *MYLK* loss of function. The most defensible core annotation is:

**MYLK loss → deficient regulatory myosin-light-chain phosphorylation → impaired actin–myosin force generation in bladder and intestinal smooth muscle → non-obstructive megacystis and intestinal hypoperistalsis → microcolon, pseudo-obstruction, urinary tract damage and intestinal failure.**

The association is mechanistically coherent and functionally supported, but precise penetrance, prevalence, variant spectrum and MYLK-specific prognosis remain unknown because only a handful of adequately characterized patients have been published.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0060610` (2 mentions) - the report calls it "Disease Ontology, broad MMIHS"; DOID calls it **megacystis-microcolon-intestinal hypoperistalsis syndrome**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Gene`, `ORPHA`.