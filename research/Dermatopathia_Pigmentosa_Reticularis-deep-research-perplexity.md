---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-09T20:58:18.366099'
end_time: '2026-10-09T21:02:16.437472'
duration_seconds: 238.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dermatopathia Pigmentosa Reticularis
  mondo_id: MONDO:0007445
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
citation_count: 59
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 6
  off_topic: 2
  off_topic_references:
  - PMC:PMC6440173
  - PMC:PMC5672609
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0008404
    reported_labels:
    - "Onychodystrophy**\u2014brittle, short, thickened or otherwise malformed nails;\
      \ clinical sign"
    ontology_label: Nail dystrophy
  - term_id: HP:0007455
    reported_labels:
    - Adermatoglyphia**, absent or poorly developed fingerprints; physical manifestation
    ontology_label: Adermatoglyphia
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dermatopathia Pigmentosa Reticularis
- **MONDO ID:** MONDO:0007445 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dermatopathia Pigmentosa Reticularis** covering all of the
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

# Dermatopathia pigmentosa reticularis: disease-characteristics research report

**Dermatopathia pigmentosa reticularis (DPR; MONDO:0007445) is an exceptionally rare, autosomal-dominant ectodermal dysplasia associated with heterozygous *KRT14* variants.** Its characteristic clinical combination is persistent reticulate skin hyperpigmentation, nonscarring alopecia, and nail dystrophy. Absence of fingerprints, palmoplantar keratoderma, and abnormal sweating are additional clues. DPR and Naegeli–Franceschetti–Jadassohn syndrome (NFJS) are closely overlapping *KRT14*-associated phenotypes; a family can show features of both. The evidence base consists mainly of pedigrees, individual case reports, pathology, and a related-syndrome cell experiment—not a prospective natural-history cohort. [52][21][81][65]

**Evidence convention:** “Human clinical” denotes observations in affected people; “in vitro” denotes cell experiments; “mouse” denotes genetically altered mice. An ontology term marked **suggested** is a useful annotation, not evidence that its biological process has been experimentally demonstrated in DPR.

## 1. Disease information

| Characteristic | Disease-level entry |
|---|---|
| Definition | A genetic disorder of ectoderm-derived skin and appendages, recognized clinically by lifelong reticulate hyperpigmentation, diffuse nonscarring alopecia, and onychodystrophy. [52] |
| Identifiers | **MONDO:0007445; OMIM:125595; ORPHA:86920; ICD-10: Q82.4; ICD-11: LD27.0Y; MeSH: C535374; UMLS/MedGen concept: C0406778; MedGen UID: 98037; SNOMED CT: 239088003.** The ICD codes are mapped categories, not necessarily DPR-exclusive diagnostic codes. [52][47] |
| Names | Dermatopathia pigmentosa reticularis; **DPR**. NFJS/DPR denotes the overlapping allelic spectrum, **not** an exact synonym for the narrower DPR phenotype. [47][81] |
| Data provenance | This is an **aggregated disease-level report** drawing on curated resources and published, identifiable case or family observations. It is not derived from an individual’s EHR or a population registry. [47][136][21] |

Primary genetic evidence: Lugassy and colleagues studied **one DPR family and four NFJS families**. Their abstract states, **“Heterozygous nonsense or frameshift mutations in KRT14 were found to segregate with the disease trait in all five families.”** Human pedigree and biopsy study; published online **25 August 2006**, PMID **16960809**, DOI **10.1086/507792**, [article URL](https://pubmed.ncbi.nlm.nih.gov/16960809/). [21]

## 2. Etiology: causes, risks, protection, and environment

| Factor | Finding and interpretation |
|---|---|
| Established cause | Heterozygous, very-early truncating ***KRT14*** variants affecting the keratin-14 nonhelical head region cause the NFJS/DPR spectrum. They alter a keratin network important in basal keratinocytes; the exact reason one carrier has a DPR rather than an NFJS presentation remains unresolved. **Human clinical and molecular evidence.** [21][81] |
| Principal risk factor | A pathogenic familial variant: an affected heterozygous parent has a **50% chance per pregnancy of transmitting the variant**, although the child’s precise phenotype cannot be predicted reliably from that probability. [47][65] |
| Other genetic risk or modifiers | Intra-family phenotypic overlap despite the same frameshift variant demonstrates variable expression; **no validated human DPR modifier gene, susceptibility locus, or polygenic score** was established in the reviewed evidence. Keratin 16 rescue in mice is an experimental compensation result, not proof that human *KRT16* protects against DPR. [65][338] |
| Environmental causes or susceptibility | **No toxin, diet, occupation, smoking habit, infection, or pathogen is established as a cause.** Heat can aggravate discomfort when sweating is impaired; mechanical stress may aggravate acral skin fragility. These are symptom modifiers, not demonstrated determinants of whether a carrier develops DPR. [52][21] |
| Protective variants or exposures | **None established** for preventing disease occurrence. Hydration and heat avoidance address consequences of impaired sweating; they do not correct the inherited cause. [252] |
| Gene–environment interaction | An **in-vitro, related-NFJS** experiment found greater apoptosis after exposure to the inflammatory signal TNF-α when *KRT14* expression was reduced. This supports a plausible cellular stress interaction, **not** an epidemiologically established TNF-α exposure risk for DPR. [web:18049449] |

## 3. Phenotypes, timing, frequency, and impact

**Frequency caution:** The classical triad describes the DPR phenotype, but there are no defensible population-derived percentages for its individual findings. HPO-linked listings provide terms without usable DPR-specific frequencies; the appended “30” on one aggregator’s labels must **not** be interpreted as 30%. One 2019 review counted **21 published DPR patients**, underscoring the small and selected evidence base. [185][136][65]

| Phenotype and type | Suggested HPO term | Onset, course, and severity | Reported frequency and potential impact |
|---|---|---|---|
| Generalized or truncal **reticular hyperpigmentation**; clinical sign | **HP:0007588** | Birth or early childhood; may spread initially, then characteristically **persists throughout life**. Extent varies. | Defining feature; **percentage unavailable**. Visible pigmentation can affect appearance and psychosocial well-being, but a DPR-specific quality-of-life effect size is unavailable. [52][76][185] |
| **Nonscarring scalp alopecia**, sometimes involving eyebrows or other hair; clinical sign | **HP:0002293** (alopecia of scalp); **HP:0001596** (broader alopecia) | Childhood onward; can progressively thin. Usually described as diffuse or partial. | Part of classical triad; **percentage unavailable**. Appearance-related impact is plausible, not quantified. [52][76][97] |
| **Onychodystrophy**—brittle, short, thickened or otherwise malformed nails; clinical sign | **HP:0008404** | Childhood; degree and progression vary. A molecularly confirmed family showed hypertrophic nails, subungual hyperkeratosis, and onycholysis. | Part of triad; **percentage unavailable**. May interfere with nail care or manual tasks; no measured DPR-specific disability estimate. [52][81] |
| **Adermatoglyphia**, absent or poorly developed fingerprints; physical manifestation | **HP:0007455** | Congenital/developmental; persistent. | Variable; **percentage unavailable**. May complicate fingerprint identification; functional burden has not been quantified in DPR. [21][76][185] |
| **Palmoplantar hyperkeratosis/keratoderma**; clinical sign | **HP:0000972** | Childhood, variable thickening; may include pressure-related calluses. | Variable; **percentage unavailable**. Severe thickening can cause discomfort, an individual-care consideration rather than a measured cohort outcome. [52][185] |
| **Hypohidrosis** or, less often, **hyperhidrosis**; symptom/sign | **HP:0000966** for hypohidrosis; assign a hyperhidrosis term separately if present | Developmental, variable; reduced sweating may be accompanied by heat intolerance. | Variable; **percentage unavailable**. Affected individuals may need heat-exposure precautions. [52][252][185] |
| Acral **nonscarring blistering**; clinical sign | Suggested: an HPO skin-blistering term, to be checked against the patient’s distribution | Can occur during the first years of life; not universal. | Occasional; **percentage unavailable**. Blisters can affect comfort and skin integrity. [52][65] |
| **Reticulate oral-mucosal pigmentation**; clinical sign | **HP:0012788** | Timing and severity poorly characterized. | Reported, not obligatory; **percentage unavailable**. A 2023 clinical case described buccal and tongue pigmentation. [185][76] |
| **Abnormal conjunctiva morphology** or other ocular finding; clinical sign | **HP:0000502** | Insufficient data to specify typical onset or severity. | Listed in phenotype resources; **frequency unknown**. Do not assume an eye abnormality in every patient. [185][136] |

The 2023 case report provides a useful **single-patient**, not frequency, example: a 22-year-old man had pigmentation from birth, alopecia, nail dystrophy, and absent dermatoglyphics, while his teeth and sweating were normal. *Pigment International* **2023**, 10(3):172–178; [article URL](https://journals.lww.com/pigi/fulltext/2023/10030/dermatopathia_pigmentosa_reticularis__through_the.7.aspx); no PMID was supplied by the journal page. [76] **No DPR-specific EQ-5D, SF-36, PROMIS, or comparable numerical quality-of-life results** were identified in these sources.

## 4. Genetic and molecular information

| Gene or variant | Classification and origin | Evidence and interpretation |
|---|---|---|
| ***KRT14***; **HGNC:6416**, NCBI Gene **3861**, OMIM gene **148066**, **17q21.2**; protein UniProt **P02533** | Established causal gene for the allelic DPR/NFJS spectrum. | Encodes type-I keratin 14, which partners with keratin 5 in the basal epithelial intermediate-filament network. Most convincingly DPR/NFJS-associated reported changes are heterozygous early stop-gain or frameshift variants; other *KRT14* variant classes can cause **different disorders**, notably epidermolysis bullosa simplex (EBS). [48][53][21] |
| **NM_000526.5:c.54C>A; p.(Cys18Ter)**, historically **C18X** | **Germline**, heterozygous; the original DPR pedigree established segregation. ClinVar’s **DPR-specific** submission calls it **pathogenic**, but its **current overall germline aggregate is uncertain significance** because another submission disagrees. | Do **not** flatten the conflicting ClinVar classifications into an unqualified ACMG consensus. Original DPR-family evidence: PMID **16960809**. ClinVar Variation ID **14626**. Its displayed 1000 Genomes global minor-allele frequency is **0.00040**; ClinVar flags gnomAD frequency at this position as unreliable, so no dependable gnomAD frequency should be asserted. [21][web:14626] |
| **NM_000526.5:c.19C>T; p.(Gln7Ter)**, historically **Q7X** | **Germline**, heterozygous; ClinVar **pathogenic** for NFJS, Variation ID **66333**; also identified in a clinically DPR-affected 2024 family. | Same variant across overlapping labels illustrates why sequence alone need not distinguish DPR from NFJS. ClinVar displays gnomAD frequency approximately **0.00001**, with one heterozygote and no homozygotes in the cited dataset. 2024 case: PMID **39106435**, published online **6 August 2024**, DOI **10.1093/ced/llae310**, [article URL](https://academic.oup.com/ced/article/50/1/246/7728175). [web:66333][81] |
| ***KRT14* c.17delG**, early frameshift | **Germline**, heterozygous; reported in an NFJS family, not the original family labeled DPR. | It and the two early nonsense changes segregated with phenotype in the original five-family study. The paper did not specify a modern reference-transcript accession for its original “17delG” notation; avoid assigning an unverified modern HGVS protein consequence. [21] |

These are **the directly pertinent early variants**, not an exhaustive list of *KRT14* variation. In particular, an aggregator’s other *KRT14* missense records should not be interpreted as proven causal variants for the DPR phenotype merely because they appear under a broadly associated gene or condition. [185][21]

**Molecular interpretation:** Early truncation is established at the DNA level. Reduced functional K14—**haploinsufficiency**—is supported by experiments in NFJS-derived research, but a 2024 DPR report explicitly notes **conflicting evidence** about making haploinsufficiency the complete explanation. Early mutant transcripts may escape complete nonsense-mediated decay, and an alternative downstream translation product was proposed; a dominant-negative contribution has not been conclusively excluded for every variant. No DPR-specific modifier, epigenetic signature, causative chromosomal rearrangement, somatic driver, or reliable variant-based severity predictor is established. A chromosome **1q21.1–q21.2 duplication** detected in the 2024 proband was considered relevant to separate neurodevelopmental findings, **not** the explanation for his DPR skin phenotype. [21][web:18049449][81]

## 5. Environmental and infectious information

DPR is **not classified as an infectious or exposure-induced disease**. No causative bacteria, virus, fungus, parasite, pollutant, radiation exposure, occupational exposure, dietary pattern, smoking pattern, or alcohol exposure is established. Heat exposure matters clinically when sweating is reduced; it should be recorded as a potential **symptom aggravator**, not a cause of the *KRT14* variant. No DPR-specific protective lifestyle intervention or validated gene–environment risk estimate is available. [52][21][252]

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A germline heterozygous early stop-gain or frameshift in *KRT14* leads to** a prematurely interrupted keratin-14 coding sequence in the NFJS/DPR spectrum. **Demonstrated in human families.** [21]
2. **The altered sequence leads to** reduced effective K14 protein or altered production of a short/head-deficient product. **Reduced K14 is experimentally supported for NFJS; the precise contribution of transcript decay versus alternative products in all DPR variants remains unresolved.** [web:18049449][21][81]
3. **Disrupted K14–K5 filament function leads to** altered structural resilience and stress responses in basal keratinocytes. **Filament abnormalities were observed in affected human skin; assigning every downstream effect specifically to DPR rather than the shared NFJS/DPR spectrum is partly inferred.** [21][53]
4. **One branch:** reduced keratinocyte protection against pro-apoptotic signals **leads to** increased basal-cell apoptosis. Human ultrastructure supports increased apoptosis; reducing *KRT14* increased **TNF-α-induced** apoptosis in an NFJS-related HaCaT-cell assay. **Extrapolation of that cell response to every DPR lesion is inferred.** [21][web:18049449]
5. **Pigmentary branch:** basal-layer damage and cell loss **lead to** pigment incontinence and dermal melanophages; these findings **are proposed to contribute to** persistent reticulate hyperpigmentation. **The histology is observed; the complete mechanism generating its netlike distribution is not demonstrated.** [21][76][122]
6. **Developmental/appendage branch:** altered basal-epithelial development and maintenance **lead to** abnormal dermatoglyphics, sweating, hair, nails, and palmoplantar keratinization. **These associations are observed; the precise cell-by-cell developmental sequence is inferred.** [21][52]

The landmark abstract states: **“Ultrastructural examination of patient skin biopsy specimens provided evidence for increased apoptotic activity in the basal cell layer where KRT14 is expressed.”** Human pathology, PMID **16960809**. The mechanistic experiment’s abstract reports, **“decreased KRT14 expression is associated with increased susceptibility to TNF-alpha-induced apoptosis.”** **In-vitro HaCaT study addressing NFJS**, PMID **18049449**, published online **29 November 2007** in *Journal of Investigative Dermatology* **2008**, DOI **10.1038/sj.jid.5701187**, [article URL](https://pubmed.ncbi.nlm.nih.gov/18049449/). Neither quote proves a distinct TNF-α-driven disease pathway in every person with DPR. [21][web:18049449]

| Mechanistic annotation | Defensible knowledge-base entry |
|---|---|
| Upstream protein and process | K14–K5 intermediate-filament organization; suggested **GO:0045109** (intermediate filament organization), **GO:0045095** (keratin filament; cellular component), and **GO:0005882** (intermediate filament; cellular component). [53][285] |
| Downstream process | Increased apoptotic susceptibility; suggested **GO:0006915** (apoptotic process). Pigment incontinence and altered epithelial differentiation are downstream observations or interpretations, **not proof of a named Wnt, MAPK, PI3K–AKT, or mTOR cascade in DPR**. [21][web:18049449] |
| Cells | Primary: basal epidermal **keratinocyte CL:0000312**; suggested basal-cell annotation **CL:0000646**. Melanocytes **CL:0000148** contribute pigment; their being the *primary* mutant target is not demonstrated. Sweat-gland **myoepithelial cell CL:0000185** is a relevant suggested cell type, not a proven exclusive target. [21][292][301] |
| Molecular-profiling limits | Patient-skin ultrastructure and targeted RNA/protein work are available; **no validated DPR-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omics, or CRISPR-screen signature** was established by the cited DPR studies. Do not infer an enzyme deficiency, metabolic biomarker, autoimmunity, or disease-specific epigenetic change. [21][web:18049449][81] |

## 7. Anatomical structures affected

| Level | Affected structures and suggested ontology terms |
|---|---|
| Organ and body system | Primarily the **integumentary system**: skin **UBERON:0002097**, nails **UBERON:0001705**, hair follicles **UBERON:0002073**, and sweat glands **UBERON:0001820**. Oral mucosa and, rarely, ocular structures have been reported. Primary cardiovascular, pulmonary, hepatic, or marrow disease is **not** an established DPR feature. [52][246][81] |
| Tissue and cells | Skin epidermis **UBERON:0001003**, particularly basal epidermal layer **UBERON:0002025**; basal keratinocytes **CL:0000312** and suggested **CL:0000646**. Pigment-laden cells can be found in the underlying dermis; melanocytes **CL:0000148** are relevant to pigment interpretation. [21][76][292] |
| Subcellular | Principally the **cytoplasmic keratin intermediate-filament network**, **GO:0045095/GO:0005882**. A DPR-specific mitochondrial, ER, or lysosomal lesion is not established. [21][53][281] |
| Distribution and laterality | Pigmentation often predominates on the **trunk**, with variable neck, face, flexural, limb, palm, sole, or oral involvement. Alopecia can be diffuse. DPR is **not characteristically unilateral**; distribution varies among individuals. [205][76][81] |

## 8. Temporal development

| Period or course feature | Finding |
|---|---|
| Onset | Usually **neonatal or infancy/early childhood**, insidious rather than an acute illness. Orphanet assigns infancy and neonatal onset. [52] |
| Early evolution | Pigmentation can spread during early childhood. Nail and hair changes can emerge or become more apparent later; in one 2026 clinically diagnosed case, hair thinning and nail abnormalities began at puberty. That is a case observation, **not** a standard disease stage. [76][252] |
| Established course | DPR pigmentation characteristically **persists for life**, unlike the classically fading pigmentation used to describe NFJS. Individual hair or nail findings can vary and progress. **No validated early/intermediate/end-stage scheme or progression-rate estimate** exists. [52][65] |
| Remission and critical periods | Spontaneous disappearance of the characteristic DPR pigment pattern is not expected; no proven curative treatment-induced remission or defined therapeutic window has been reported. Dermatoglyphic differences reflect early development, but no prenatal intervention is established. [52][21] |

## 9. Inheritance and population

| Measure | Best-supported entry |
|---|---|
| Prevalence | Orphanet: **<1 per 1,000,000**; treat as a rarity estimate, **not a measured DPR population survey**. [52] |
| Incidence and carrier frequency | **Unknown**; no reliable cases-per-100,000-per-year or population carrier-rate estimate. [52][65] |
| Published-case statistic | A **2019** account reported **21 published DPR patients** and, separately, **55 NFJS patients from nine families** at that time. These are historical literature counts, **not prevalence or penetrance denominators**. PMID **30968399**, DOI **10.1111/bjd.17997**, [article URL](https://pubmed.ncbi.nlm.nih.gov/30968399/). [65][132] |
| Inheritance and expression | **Autosomal dominant** with **variable expressivity**: relatives carrying a *KRT14* variant can receive DPR, NFJS, or overlapping clinical labels. **Numerical penetrance and age-dependent penetrance are not established.** [21][65] |
| Anticipation, mosaicism, consanguinity | No established repeat-expansion anticipation or quantified germline-mosaicism contribution. Consanguinity is not required by the dominant mechanism. Revertant mosaicism discussed for other *KRT14* disorders should not be entered as proven DPR protection. [21][205] |
| Founder effect | A shared haplotype suggested a **possible** common origin of Q7X in three NFJS families; this does **not** establish a DPR-wide founder allele. [21] |
| Geography, ancestry, sex, age distribution | Reports span regions, without an established racial predilection, geographic prevalence gradient, or measured male:female ratio. The inheritance mechanism permits affected people of either sex. Presentation generally starts in infancy, even when diagnosis occurs in adulthood. [205][52][76] |

## 10. Diagnostics

**Practical diagnostic approach:** recognize the childhood-onset, persistent pigment pattern and the hair–nail findings; inspect palms, soles, dermatoglyphics, sweating, teeth, and oral mucosa; document a pedigree; then seek **heterozygous *KRT14* sequence confirmation**, particularly when NFJS, EBS, or a systemic reticulate-pigmentation disorder is plausible. A 2024 diagnostic review recommends using onset, distribution, and extracutaneous findings to reach a provisional classification while acknowledging overlap. PMID **39139099**, DOI **10.1093/ced/llae322**, published online **14 August 2024**, [article URL](https://academic.oup.com/ced/article/50/1/12/7733322). [260][81][261]

| Test or criterion | Utility and limitation |
|---|---|
| Clinical examination and pedigree | The pigmentation–nonscarring alopecia–nail-dystrophy combination is strongly suggestive; absent dermatoglyphics and abnormal sweating add support. A feature alone is not diagnostic. [52][21] |
| Dermoscopy and trichoscopy | Can document reticulated pigmented and hypopigmented spots, perifollicular change, and palmar loss of ridge patterns. A **2023 single case** demonstrated clinical use; no sensitivity or specificity is established. [76] |
| Skin biopsy | May show basal-layer pigmentation/vacuolization, pigment incontinence and melanophages, with variable hyperkeratosis or mild inflammatory change. Findings support but do not uniquely establish DPR. [76][21] |
| Molecular testing | **Sequence *KRT14*** using a single-gene test or a panel that includes it for ectodermal dysplasia, palmoplantar keratoderma, or inherited skin fragility. Targeted exome sequencing identified **c.19C>T** in the molecularly confirmed 2024 family. Interpret the variant **and its condition-specific ClinVar evidence** alongside segregation and phenotype. [81][261][web:14626] |
| Broader WES/WGS | Reasonable when presentation overlaps other inherited pigmentation disorders or the focused test is unrevealing; not demonstrated to outperform a well-targeted *KRT14* assay for a classical presentation. [81][260] |
| Laboratory and differential-directed testing | There is **no established DPR blood, urine, enzyme, imaging, electrophysiology, or circulating biomarker test**. CBC and telomere evaluation are relevant **when dyskeratosis congenita is suspected**, not routine DPR-confirmatory tests. In the 2024 case, normal telomere length helped challenge that alternative diagnosis. [81] |
| Tests without established routine role | Chromosomal microarray/karyotype/FISH, mitochondrial sequencing, repeat-expansion assays, RNA-seq, proteomics, metabolomics, epigenomics, and liquid biopsy do not diagnose typical *KRT14*-associated DPR. Use them only for a separately justified differential. [81][21] |

| Differential diagnosis | Distinguishing considerations |
|---|---|
| **NFJS** | Same gene and substantial overlap; pigment is classically described as fading with age, and dental-enamel defects are more characteristic. **Neither difference is absolute**, as overlapping families demonstrate. [65][81] |
| **Dyskeratosis congenita/telomere biology disorder** | Pigment and nail findings can mislead; evaluate characteristic nail pattern, oral leukoplakia, marrow/cancer history, and telomere findings as clinically indicated. **Cancer or marrow failure must not automatically be attributed to DPR.** [81] |
| **Dowling–Degos disease**, other inherited reticulate dyschromias, and **EBS with mottled pigmentation** | Distribution, associated hair/nail/sweat findings, blistering history, histology, and appropriate gene testing help distinguish them. [76][260] |

There is **no DPR-specific universal newborn-screening program or formally validated standalone clinical scoring criterion** in these sources. Once a familial variant is established, targeted testing of relatives is feasible with genetics input. [261][52]

## 11. Outcome and prognosis

DPR is generally described as a **lifelong disorder of skin and appendages**, rather than a progressive marrow-failure or malignancy syndrome. However, there are **no reliable DPR-specific five- or ten-year survival rates, life-expectancy estimates, attributable mortality rates, disability scores, or validated prognostic biomarkers**. Persistent pigmentation, hair and nail changes, troublesome keratoderma, impaired sweating, and occasional blisters account for recognized morbidity. Rare ocular observations should be assessed individually rather than assumed to predict outcome. [52][59][81]

The 2024 case demonstrates a consequential diagnostic distinction: the proband’s leukemia and his mother’s tongue cancer initially raised concern for dyskeratosis congenita, but the authors found *KRT14*-associated DPR and stated that the family cancer history **remained unexplained**; cancer had **not previously been established as a DPR feature**. Reclassification changed counseling about prognosis and screening burden and affected the family’s psychological well-being. **One family cannot establish that all carriers lack unrelated cancer risk.** PMID **39106435**. [81]

## 12. Treatment and real-world implementation

**There is no established disease-modifying cure or DPR-specific treatment algorithm.** Treatment is individualized to symptoms; the observations below must not be turned into response-rate claims. [39][76]

| Treatment or intervention | Application and observed outcome | Suggested annotation and evidence limit |
|---|---|---|
| **Topical emollients and keratolytics** | Supportive care for thickened palms and soles; topical retinoic acids are also suggested for hyperkeratosis. This is symptom management, not pigment or genotype correction. [39][76] | Use a locally verified **NCIT supportive-care or dermatologic-intervention** term; no exact NCIT keratolytic code is asserted here. |
| **Etretinate**, systemic retinoid | A **1995 report** describes successful treatment of **DPR-associated palmoplantar keratoderma**; the evidence is a case report, not a trial or an endorsement for routine use. PMID **7591467**, DOI **10.1111/j.1365-4362.1995.tb01099.x**, [PubMed URL](https://pubmed.ncbi.nlm.nih.gov/7591467/). Etretinate has substantial reproductive toxicity and was withdrawn from the US market. [344][322] | **ChEBI:4913**; verify an appropriate NCIT retinoid term locally before coding a current intervention. [227] |
| **Topical minoxidil 5%** | In **one 2022 case**, the patient reported substantially improved scalp hair density after six months. This is neither a controlled effect nor evidence that the underlying DPR changed. PMID **36225994**, DOI **10.4103/idoj.idoj_698_21**, [article URL](https://pubmed.ncbi.nlm.nih.gov/36225994/). [159][158] | **ChEBI:6942**; suggested **NCIT:C47623** (minoxidil). Monitor according to the formulation’s usual safety guidance; no DPR-specific adverse-event rate is available. [221][327] |
| **Azelaic acid 20%** | Used on facial/neck pigmentation in that same case; **reticulate pigmentation did not respond**. Correct a coexisting deficiency separately: that patient’s additional B12-related flexural pigmentation improved with replenishment, which must **not** be counted as reversal of DPR. [159] | Symptom-directed topical intervention; no DPR-specific response rate. |
| **Heat precautions and hydration** | Practical support for those with impaired sweating or heat intolerance; tailor activity to the patient, since some patients sweat normally. [252][76] | Supportive/behavioral intervention; not primary prevention. |
| **Genetic counseling** | Explain dominant transmission, phenotype variability, testing of relatives, and reproductive options after identifying a familial variant. [47][65] | **NCIT:C15240** (Genetic Counseling). [323] |

No DPR-specific **gene, cell, RNA, targeted-molecular, or immunotherapy**, disease-directed surgery, established pharmacogenomic rule, controlled combination regimen, response rate, or NCT-identified interventional trial was established by the disease-specific evidence reviewed here. Do not infer efficacy from EBS therapies merely because *KRT14* is shared. [39][81][264]

## 13. Prevention

| Level | Defensible action |
|---|---|
| Primary | There is **no vaccine, antimicrobial prophylaxis, diet, or exposure avoidance that prevents a germline *KRT14* variant**. Offer genetic counseling and reproductive discussion when the familial variant is known; prenatal or preimplantation testing is technically possible in principle but requires individualized clinical genetics care. [21][323] |
| Secondary | Recognize the phenotype early and confirm an informative familial variant where possible; offer targeted assessment of at-risk relatives. No population-wide or newborn DPR screening program is established. [52][261] |
| Tertiary | Address hyperkeratosis and blisters, assess troublesome heat intolerance, and avoid attributing unrelated systemic signs to DPR without investigation. Preventing symptoms or diagnostic harm is **not** prevention of disease occurrence. [39][81][252] |

## 14. Other species and naturally occurring disease

| Species or group | Taxonomy, ortholog, and natural-disease finding | Comparative interpretation |
|---|---|---|
| **Human** | *Homo sapiens*, **NCBI Taxon 9606**; causal gene *KRT14*, **NCBI Gene 3861**. [46] | Reference DPR disease. |
| **Domestic cat** | *Felis catus*, **NCBI Taxon 9685**; domestic shorthair breed **VBO:0100119**. A naturally affected cat had **homozygous *KRT14* c.979C>T, p.(Gln327*)**, causing **EBS**, not DPR. PMID **32657488**, published online **13 July 2020**, DOI **10.1111/age.12979**, [article URL](https://pubmed.ncbi.nlm.nih.gov/32657488/). [266][268] | Useful evidence of conserved epithelial need for K14, but its **recessive blistering phenotype and later stop position must not be mislabeled as natural feline DPR**. [266] |
| **Other naturally affected species** | **No naturally occurring nonhuman DPR phenotype** was established by the reviewed evidence. | The Mendelian condition is not infectious; **zoonotic transmission does not apply**. [264][266] |

## 15. Model organisms and experimental systems

| Model or resource | What it demonstrates | Limitation for DPR |
|---|---|---|
| ***Krt14* null mouse**; *Mus musculus*, **NCBI Taxon 10090**; ortholog **NCBI Gene 16664**, **MGI:96688** | Homozygous targeted null mice develop severe skin blistering and generally die around **two days after birth**. K15 forms a residual, structurally different filament network. Mouse primary study: PMID **7539810**, *J Cell Biol* **1995**, DOI **10.1083/jcb.129.5.1329**, [article URL](https://pmc.ncbi.nlm.nih.gov/articles/PMC2120471/). [198][337] | Primarily models severe K14 loss/EBS-like fragility, **not the viable, heterozygous, early-head-truncation DPR phenotype**. MGI lists no DPR-specific mouse model in its displayed human-disease model table. [264] |
| ***Krt14* null mouse with basal K16 expression** | Experimental K16 expression substantially rescued early blistering and neonatal lethality, though later alopecia, ulcers, and epithelial defects occurred. PMID **10477769**, *J Cell Biol* **1999**, DOI **10.1083/jcb.146.5.1185**, [article URL](https://pmc.ncbi.nlm.nih.gov/articles/PMC2169494/). [338][345] | Demonstrates partial keratin functional compensation; **not a tested DPR treatment or confirmed human protective modifier**. |
| **HaCaT keratinocytes with reduced *KRT14*** | Greater TNF-α-induced apoptosis under the experimental conditions; doxycycline prevented that assay effect. **In vitro**, PMID **18049449**. [web:18049449] | Tests a pathway proposed for related **NFJS**, not whole-organism DPR pigmentation, dermatoglyphics, or natural history. |
| **Human patient pedigrees and skin biopsies** | Establish sequence segregation, phenotype overlap, pigmentary pathology, and basal-cell ultrastructural findings. PMID **16960809**; contemporary molecularly confirmed family PMID **39106435**. [21][81] | Small numbers and selective ascertainment prevent reliable penetrance, modifier, treatment-response, and prognosis estimates. |

**Knowledge-base priority:** curate **MONDO:0007445 → *KRT14* (HGNC:6416) → early truncating germline variant → basal-keratinocyte filament dysfunction/apoptotic susceptibility → ectodermal and pigmentary findings**, with the phenotype HPO terms above. Keep the **pigment-pattern mechanism, DPR-specific penetrance, variant-specific severity, ClinVar conflict at c.54C>A, and lack of a DPR-faithful animal model** explicitly marked unresolved rather than silently converting inference into fact. [47][21][web:18049449][web:14626][264]

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 6 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC6440173` (1 mention) - Dermatopathia Pigmentosa Reticularis.
  - shared terms: nail
- `PMC:PMC5672609` (1 mention) - Clinical and Genetic Review of Hereditary Acral Reticulate Pigmentary Disorders.
  - shared terms: pigmentation, clinical

Weighed against this report's own most characteristic terms: `dpr`, `krt14`, `established`, `variant`, `phenotype`, `skin`, `nfjs`, `dpr-specific`, `disease`, `url`, `sweating`, `affected`, `pigmentation`, `nail`, `gene`, `family`, `heterozygous`, `hair`, `clinical`, `human`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0008404` (1 mention) - the report calls it "Onychodystrophy**—brittle, short, thickened or otherwise malformed nails; clinical sign"; HP calls it **Nail dystrophy**
- `HP:0007455` (1 mention) - the report calls it "Adermatoglyphia**, absent or poorly developed fingerprints; physical manifestation"; HP calls it **Adermatoglyphia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007588` (1 mention) - the report calls it "Generalized or truncal **reticular hyperpigmentation**; clinical sign"; HP calls it **Reticular hyperpigmentation**
- `HP:0000972` (1 mention) - the report calls it "Palmoplantar hyperkeratosis/keratoderma**; clinical sign"; HP calls it **Palmoplantar hyperkeratosis**
- `HP:0012788` (1 mention) - the report calls it "Reticulate oral-mucosal pigmentation**; clinical sign"; HP calls it **Reticulate pigmentation of oral mucosa**
- `HP:0000502` (1 mention) - the report calls it "Abnormal conjunctiva morphology** or other ocular finding; clinical sign"; HP calls it **Abnormal conjunctiva morphology**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.