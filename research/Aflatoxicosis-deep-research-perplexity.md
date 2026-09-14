---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-09-08T08:02:21.797370'
end_time: '2026-09-08T08:08:56.498313'
duration_seconds: 394.7
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Aflatoxicosis
  mondo_id: MONDO:0700296
  category: Toxicologic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 20
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 65
  verified: 54
  not_found: 2
  obsolete: 4
  unverifiable: 5
  confabulation_rate: 0.033
  labels_checked: 36
  labels_matching: 22
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0001541
    reported_labels:
    - Kwashiorkor
    ontology_label: Ascites
  - term_id: GO:0006638
    reported_labels:
    - lipid peroxidation
    ontology_label: neutral lipid metabolic process
  - term_id: GO:0043408
    reported_labels:
    - mutagenesis
    ontology_label: regulation of MAPK cascade
  - term_id: GO:0002247
    reported_labels:
    - fibrosis
    ontology_label: obsolete clearance of damaged tissue involved in inflammatory
      response wound healing
  labels_variant: 10
  unresolved_terms:
  - NCIT:C45570
  - HP:0006826
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  - term_id: GO:0002247
    ontology_label: obsolete clearance of damaged tissue involved in inflammatory
      response wound healing
  - term_id: GO:0031327
    ontology_label: obsolete negative regulation of cellular biosynthetic process
    replaced_by: GO:0009890
  - term_id: CL:0000213
    ontology_label: obsolete lining cell
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aflatoxicosis
- **MONDO ID:** MONDO:0700296 (if available)
- **Category:** Toxicologic

## Research Objectives

Please provide a comprehensive research report on **Aflatoxicosis** covering all of the
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

# Aflatoxicosis: Comprehensive Disease Characteristics and Research Overview

Aflatoxicosis is a toxicologic disease entity defined by acute or chronic toxicity resulting from exposure to aflatoxins, a group of difuranocoumarin mycotoxins produced predominantly by Aspergillus flavus and Aspergillus parasiticus that contaminate staple food crops and animal feeds under warm, humid, or drought-stressed conditions.[1][2][3][7] At the disease level, aflatoxicosis encompasses a spectrum ranging from fulminant acute hepatic failure with high short‑term mortality to insidious chronic effects such as hepatocellular carcinoma, impaired child growth, immunosuppression, and multi‑organ carcinogenesis, with aflatoxin B1 (AFB1) recognized as one of the most potent naturally occurring chemical carcinogens.[5][7][8] The condition is catalogued as a toxic exposure concept in MedGen and MONDO (MONDO:0700296), with ICD‑10 code T64 (“Toxische Wirkung von Aflatoxin und sonstigem Mykotoxin in kontaminierten Lebensmitteln”) and SNOMED CT term “Toxic effect of aflatoxin” (22721008), underscoring its classification as a mycotoxin poisoning rather than a primary genetic disorder.[10][16] Epidemiologically, aflatoxicosis is a major global health problem: approximately a quarter of the world’s crops are affected by mycotoxins, most notably aflatoxins, and an estimated 4.5 billion people in developing countries are chronically exposed, particularly in sub‑Saharan Africa and South Asia where contaminated maize and groundnuts are dietary staples.[1][7] Acute aflatoxicosis outbreaks, such as the 2004 Kenyan epidemic associated with aflatoxin‑contaminated maize that caused over 125 deaths, highlight the capacity of high‑dose exposure to produce dramatic epidemics of hepatic failure with attack rates of around 8 per 100,000 and mortality ranging from 16.2% to 76.5%.[11][13] At the mechanistic level, ingestion of AFB1 leads to absorption in the small intestine, hepatic bioactivation by cytochrome P450 enzymes to a highly reactive epoxide, formation of DNA and protein adducts, oxidative stress, and hepatocellular necrosis or malignant transformation, processes that have been characterized using sensitive exposure biomarkers such as aflatoxin‑albumin and aflatoxin‑N7‑guanine adducts in human epidemiologic and interventional studies.[5][8][17][18] There is no specific antidote, and clinical management focuses on supportive care and removal of contaminated food or feed, while primary prevention relies on agricultural, dietary, and increasingly probiotic interventions, alongside hepatitis B vaccination to reduce the synergistic burden of aflatoxin‑related liver cancer.[1][2][7][17][18][19]

## 1. Disease Information

Aflatoxicosis is defined as the toxic clinical state resulting from exposure to aflatoxins, which are secondary metabolites of certain toxigenic strains of Aspergillus fungi that grow on carbohydrate‑rich substrates such as maize, groundnuts, tree nuts, rice, sorghum, cottonseed, and other cereals.[1][2][3][7] MedGen describes aflatoxicosis as “toxicity resulting from exposure to aflatoxins,” and cross‑references the MONDO ontology term MONDO:0700296, which captures the disease concept as a toxicologic entity rather than a discrete genetic syndrome.[16] StatPearls notes that aflatoxins are among the major groups of mycotoxins, are produced during food production, harvest, storage, and processing, and that dietary exposure may result in severe toxic and carcinogenic outcomes in humans and animals, emphasizing the central role of contaminated food chains in disease causation.[1] Veterinary and toxicology references similarly define aflatoxicosis as the clinical manifestation of aflatoxin poisoning in animals, particularly in poultry and livestock, where contaminated feeds under hot, drought or high‑moisture storage conditions lead to hepatic and systemic toxicity.[2][3][4][14] Taken together, aflatoxicosis is best understood as a syndrome of aflatoxin poisoning, with distinct acute and chronic forms, occurring on the background of environmental exposure to fungal toxins rather than inherited susceptibility alone.[1][5][7][11]

Key disease identifiers reflect its classification within toxicology and public health frameworks. MedGen and MONDO jointly designate aflatoxicosis under MONDO:0700296, mapping to SNOMED CT “aflatoxin causing toxic effect” (22721008), and capturing synonymous labels such as “Aflatoxin Toxicity,” “Aflatoxin Poisoning,” and “Aflatoxin Toxicities.”[16] ICD‑10 lists code T64, “Toxische Wirkung von Aflatoxin und sonstigem Mykotoxin in kontaminierten Lebensmitteln,” within the broader category of toxic effects of food‑borne mycotoxins, providing a clinical coding framework for diagnosis and surveillance.[10] MeSH terms exist for aflatoxins as chemicals (e.g., “Aflatoxins” with subheadings for toxicity and adverse effects) and for aflatoxins poisoning, although aflatoxicosis as a disease entity is often captured under broader headings such as “mycotoxins/adverse effects” and “foodborne diseases.” Human aflatoxicosis has been the focus of several recent reviews, including a comprehensive evaluation of toxicology, exposure, health consequences, and interventions in developing countries, and a broad review of aflatoxin exposure and associated human health effects, which collectively provide disease‑level syntheses rather than individual case narratives.[6][7]

Common synonyms and alternative names for this disease include aflatoxin poisoning, aflatoxin toxicity, aflatoxin toxicities, aflatoxin poisonings, aflatoxicoses, and Turkey X disease in historical veterinary literature.[3][16] The latter refers to the seminal 1960 outbreak of fatal disease in turkey flocks in Great Britain, originally termed “Turkey X disease” before being traced to a toxin produced by Aspergillus flavus in groundnut meal, leading to the concept and naming of aflatoxicosis.[3][8] In modern clinical and epidemiologic work, the term aflatoxicosis is used for both human and animal disease, with modifiers such as “acute aflatoxicosis” and “chronic aflatoxicosis” denoting the temporal pattern and dose of exposure.[5][7][11] Within SNOMED CT and ICD, the toxic effect terminology implicitly includes both poisoning and toxicity states, capturing both symptomatic clinical disease and subclinical organ injury attributable to aflatoxins.[10][16]

The information synthesized in this report is derived predominantly from aggregated disease‑level resources rather than individual electronic health records. These resources include toxicology textbooks and online clinical references such as StatPearls, which provide structured summaries of aflatoxin toxicity in humans; veterinary manuals and reviews that detail aflatoxicosis in food animals; epidemiologic and toxicologic reviews of aflatoxin exposure and health effects; and mechanistic studies of aflatoxin metabolism and carcinogenicity.[1][2][3][5][7][14] Important primary literature sources include human outbreak investigations, such as the 2004 Kenyan aflatoxicosis epidemic; case reports of acute aflatoxicosis; systematic reviews of outbreak incidence and mortality; and interventional trials using postharvest measures or probiotics to reduce biomarker‑defined exposure.[11][12][13][17][18][19] These human studies provide granular clinical and biomarker data from individual patients, but the disease characteristics summarized here integrate across multiple cohorts and settings. Similarly, animal toxicology studies in rats and poultry, and histopathological investigations of experimental aflatoxin B1 exposure, provide detailed mechanistic and organ‑level descriptions, but are used here to inform general pathophysiologic understanding rather than to catalog individual animal cases.[5][9][20] Thus, the report reflects a synthesis of clinical, epidemiologic, mechanistic, and interventional evidence at the disease level, suitable for populating a comprehensive knowledge base entry.

## 2. Etiology and Risk Factors

Aflatoxicosis is fundamentally an environmentally induced toxicologic disease caused by exposure to aflatoxins, which are bisfuranocoumarin metabolites produced by toxigenic strains of Aspergillus fungi, primarily Aspergillus flavus, Aspergillus parasiticus, and Aspergillus nomius.[1][2][3][4] These molds grow on high‑carbohydrate substrates in the field and in storage, especially under conditions of warm temperatures, high humidity, drought stress, and insect damage, which together create favorable microenvironments for fungal proliferation and toxin production.[2][3][4][7] StatPearls notes that approximately 25% of the world’s crops are affected by mycotoxins, most of which are aflatoxins, and that contamination occurs in two phases: infection of crops by Aspergillus species during growth and development, and accumulation of aflatoxins during storage or transport under warm, humid conditions or severe drought.[1] Veterinary toxicology references echo this, emphasizing that A. flavus and A. parasiticus invade peanuts, nuts, maize, and cottonseed and can rapidly generate high concentrations of aflatoxins, particularly AFB1, when grain moisture exceeds 15% and relative humidity exceeds 75% at temperatures consistently above 21.1°C, conditions frequently encountered in tropical and subtropical climates.[2][3][4][14] Thus, the primary causal factor for aflatoxicosis is ingestion of food or feed contaminated with aflatoxins due to fungal growth in susceptible crops, mediated by environmental and agricultural conditions.

The major aflatoxin congeners relevant to disease include aflatoxin B1 (AFB1), B2 (AFB2), G1 (AFG1), and G2 (AFG2), which are found in contaminated food, and aflatoxin M1 (AFM1) and M2 (AFM2), which are hydroxylated metabolites of AFB1 and AFB2 excreted in milk and urine.[1][4][7] AFB1 is the most prevalent and toxic member of the aflatoxin family, recognized by the International Agency for Research on Cancer (IARC) as a Group 1 human carcinogen, while AFM1 in milk is classified as a Group 2B possible human carcinogen.[1][7] The chemical structure of aflatoxins—a difuran ring fused to a coumarin nucleus—underlies their metabolic activation to reactive epoxide intermediates that form covalent adducts with DNA and proteins, mediating genotoxicity and cytotoxicity.[2][4][5][8] These mechanisms are central to both acute and chronic aflatoxicosis and will be detailed in the pathophysiology section. From an etiologic standpoint, however, the key point is that aflatoxicosis results from the presence of these chemical entities in the diet, rather than from infection with Aspergillus itself; the fungus provides the source of toxin, but the disease is a chemical intoxication rather than a mycosis.[1][2][3][7]

Genetic causal factors at the level of inherited mutations are not primary drivers of aflatoxicosis, and the condition is not considered a Mendelian genetic disease. There are no causal gene mutations or chromosomal abnormalities that, in the absence of exposure, produce aflatoxicosis. Rather, there is emerging evidence that host genetic variation may modulate susceptibility to aflatoxin toxicity by altering the metabolism and detoxification of aflatoxins, for example via polymorphisms in cytochrome P450 enzymes, glutathione S‑transferases, and other xenobiotic metabolizing genes.[5][7] However, specific variants, loci, and their effect sizes have not been comprehensively catalogued in the sources reviewed here, and aflatoxicosis is not listed in OMIM as a primary genetic syndrome. Thus, for the purposes of this knowledge base entry, aflatoxicosis should be classified etiologically as an environmentally induced toxicologic and carcinogenic disease, with potential but insufficiently characterized genetic modifiers of risk.

Environmental risk factors are central to aflatoxicosis. At the level of food production, drought and prolonged hot weather predispose crops, especially maize and groundnuts, to Aspergillus infection and aflatoxin production, often interacting with insect damage that physically disrupts grains and facilitates fungal colonization.[2][3][4][14] High moisture content of grain and water damage in storage further increase the risk of aflatoxin accumulation, and contamination often shows an uneven distribution within a given batch, such that localized pockets of high toxin concentration can pose disproportionate risk when consumed.[1][3][4] At the dietary level, reliance on susceptible staple crops that are not rigorously screened or properly stored, as is common in subsistence farming communities in sub‑Saharan Africa and South Asia, leads to chronically high aflatoxin exposure, with groundnuts and maize identified as major sources.[7][18] StatPearls notes that aflatoxins are regularly found in improperly stored cassava, cottonseed, chili pepper, maize, wheat, millet, peanut, rice, sesame, sunflower seed, and many spices, underscoring the breadth of possible exposure sources.[1] Animals fed contaminated feed can pass aflatoxin metabolites into milk, eggs, and meat, exposing humans via animal products, particularly to AFM1 in milk, although AFM1 is less potent than AFB1.[1][2][7] Occupational exposure can also occur via inhalation of aflatoxin‑contaminated dust among workers handling mouldy grains or feeds, leading to lung cancers and other respiratory effects, and via dermal contact, contributing to skin cancers and localized toxicity.[5] Thus, environmental and occupational contexts that favor aflatoxin contamination and provide frequent exposure routes constitute key risk factors for aflatoxicosis.

Host‑related risk factors include age, co‑morbid infections, nutritional status, and potentially sex, although the latter is not consistently highlighted in the literature. Children are particularly affected by aflatoxin exposure, both because of their dietary patterns and because developing organs and immune systems may be more vulnerable to toxin effects.[1][7] StatPearls notes that approximately 4.5 billion people in developing countries are exposed to substantial levels of aflatoxin and that children are particularly affected, with aflatoxins believed to be involved in nutritional disorders such as kwashiorkor and growth faltering, likely by interfering with micronutrient absorption, protein synthesis, and metabolic enzyme activities.[1][5][7] Chronic infection with hepatitis B virus (HBV) is a major risk factor for aflatoxin‑related hepatocellular carcinoma, with multiple studies demonstrating that aflatoxin exposure and HBV infection together substantially increase the risk of HCC compared to either factor alone.[7][15] A meta‑analysis of p53 codon 249 mutations in HCC found that the mean proportion of tumors harboring the 249(ser) mutation was positively correlated with aflatoxin exposure, and that HBV infection was highly prevalent in high aflatoxin regions, although there was little evidence for a specific HBV–aflatoxin interaction modulating the presence of this particular mutation.[15] Nonetheless, epidemiologic data support HBV as a synergistic cofactor in aflatoxin‑related liver cancer, making HBV infection a critical host risk factor for the most serious chronic consequence of aflatoxicosis. Nutritional deficiencies and poor overall health, common in subsistence farming communities, may further increase vulnerability to aflatoxin toxicity by impairing hepatic detoxification, antioxidant defenses, and immune responses.[5][7]

Protective factors for aflatoxicosis operate at both environmental and individual levels. On the environmental side, postharvest interventions that reduce aflatoxin contamination of groundnut and maize crops have been shown to substantially lower human exposure. In a community‑based intervention study in Guinea, implementation of a package of low‑technology postharvest measures in ten villages, compared to usual practices in ten control villages, led to stable aflatoxin‑albumin adduct concentrations over five months of storage in intervention villages, while control villages experienced more than a three‑fold increase.[18] Specifically, mean aflatoxin‑albumin concentration rose from 5.5 pg/mg immediately after harvest to 18.7 pg/mg five months later in control villages, whereas in intervention villages concentrations remained around 8 pg/mg, less than 50% of control levels at five months.[18] The proportion of individuals with non‑detectable adducts at five months was 20% in intervention villages versus 2% in controls, demonstrating that simple changes in drying, sorting, and storage can act as powerful protective factors against aflatoxicosis.[18] At the individual level, probiotic supplementation has emerged as a promising protective strategy. A randomized controlled trial in young men in Southern China found that a probiotic mixture of Lactobacillus rhamnosus LC705 and Propionibacterium freudenreichii reduced urinary excretion of aflatoxin B1‑N7‑guanine, a biomarker of biologically effective aflatoxin dose, by 36% at three weeks and 55% at five weeks compared with placebo.[17] The geometric mean concentration of AFB1‑N7‑guanine during the intervention was 0.24 ng/mL in the probiotic group versus 0.49 ng/mL in the placebo group, indicating a substantial reduction in systemic exposure.[17] More recently, a randomized, double‑blind, placebo‑controlled trial in Malaysian adults showed that consumption of fermented milk containing Lacticaseibacillus paracasei strain Shirota twice daily for 12 weeks led to a 23% reduction in urinary AFM1 concentrations compared with placebo, and sustained lower serum AFB1‑lysine adduct levels, suggesting that probiotics can reduce both acute and chronic aflatoxin exposure.[19] These studies, based on human clinical data, demonstrate that specific probiotic strains capable of binding aflatoxins in the gut act as protective factors, lowering biomarker‑defined exposure and potentially reducing the risk of aflatoxicosis and downstream liver cancer.[17][19]

Gene–environment interactions in aflatoxicosis primarily involve the interplay between environmental aflatoxin exposure and host factors such as HBV infection and xenobiotic metabolism. As noted above, HBV infection acts as an important cofactor in aflatoxin‑related HCC, with aflatoxin exposure strongly associated with the p53 codon 249 mutation, but with limited evidence that HBV modifies the presence of this specific mutation.[15] Nonetheless, the co‑occurrence of HBV infection and high aflatoxin intake in many endemic regions leads to multiplicative risk of HCC, an archetype of gene–environment interaction where a viral genome and chronic toxin exposure converge on shared target tissues, especially hepatocytes.[7][15] At the level of biochemical metabolism, individual variation in CYP450 isoforms and glutathione S‑transferases likely influences the balance between activation of AFB1 to a reactive epoxide and detoxification to less harmful metabolites, thereby modulating susceptibility to both acute hepatotoxicity and chronic carcinogenicity.[5] Although specific genetic polymorphisms are not detailed in the reviewed sources, mechanistic studies show that detoxifying capacity can be overwhelmed at high toxin doses, leading to a shift in metabolism towards toxic intermediates and severe cellular injury.[5] In this sense, aflatoxicosis exemplifies a disease where environmental toxin exposure is the dominant etiologic factor, but where host genetic and infectious cofactors shape the clinical phenotype and long‑term outcomes.

From an ontology perspective, aflatoxin B1 and related toxins can be represented as chemical entities in CHEBI (e.g., CHEBI:27375 for aflatoxin B1), while risk and protective factors such as “groundnut‑based diet,” “maize‑based diet,” “hepatitis B infection,” and “probiotic therapy” can be encoded as environmental or clinical exposure terms in ontologies such as ECTO (Environmental Conditions, Treatments & Exposures) and NCIT (NCI Thesaurus). For example, NCIT terms relevant to etiology include “NCIT:C45570 Aflatoxin B1,” “NCIT:C134019 Mycotoxin Exposure,” and “NCIT:C123937 Hepatitis B Virus Infection,” providing a structured representation of causal and modifying factors. These annotations can support knowledge base integration of aflatoxicosis as a toxicologic disease with rich gene–environment interaction architecture.

## 3. Clinical Phenotypes

The phenotypic spectrum of aflatoxicosis spans acute and chronic manifestations, involving symptoms, clinical signs, laboratory abnormalities, and long‑term health outcomes. At the symptom and sign level, acute aflatoxicosis typically presents with gastrointestinal complaints, constitutional symptoms, and signs of hepatic failure. A systematic review of acute aflatoxicosis outbreaks found that common symptoms included vomiting, reported in 77–100% of cases, jaundice, present in 88–100%, and abdominal pain, reported in 8–87%.[11] These features reflect acute hepatocellular injury and cholestasis, with nausea and vomiting (suggested HPO term HP:0002013), jaundice (HP:0000952), and abdominal pain (HP:0002027) constituting cardinal manifestations. StatPearls emphasizes that acute aflatoxicosis can lead to acute hepatic failure, with clinical features such as nausea, vomiting, abdominal pain, pulmonary edema, and coma, although detailed symptom frequencies are more fully described in outbreak reports and case series.[1][11][12] A case report of acute aflatoxicosis from Nigeria underscores that diagnosis requires consideration of geographical location, staple diet, clinical features, and exclusion of other infections, highlighting the non‑specific but severe nature of acute presentations.[12] From a phenotype ontology perspective, acute aflatoxicosis can be mapped to HPO terms such as “Acute liver failure” (HP:0001410), “Elevated serum transaminases” (HP:0002910), “Coagulopathy” (HP:0003256), and “Hepatic encephalopathy” (HP:0006826), depending on severity.

Laboratory abnormalities in acute aflatoxicosis include elevations in liver enzymes (AST, ALT), hyperbilirubinemia, prolonged prothrombin time, and hyponatremia, consistent with acute hepatocellular necrosis and impaired hepatic synthetic function. Although specific laboratory values are not exhaustively tabulated in the sources reviewed, the characterization of acute aflatoxicosis as acute hepatic failure, often leading to death, implies severe biochemical derangements.[11][12] In animals, aflatoxicosis similarly presents with elevated serum liver enzymes, decreased albumin, and coagulopathy, and dietary aflatoxin levels two times above tolerable limits are likely to cause clinical disease, including mortality.[2][14] Suggested LOINC terms for relevant laboratory tests include “Liver panel” analytes and “Prothrombin time (PT),” while laboratory phenotype terms in HPO would include “Increased circulating alanine aminotransferase concentration” (HP:0002910) and “Hyperbilirubinemia” (HP:0002904). These abnormalities are usually severe during acute episodes and correlate with symptom severity and prognosis.

Chronic aflatoxicosis, resulting from repeated low‑dose exposure over years, manifests predominantly as carcinogenesis and subclinical organ impairment. The most frequent and severe chronic disease attributable to aflatoxin exposure is primary liver cancer, specifically hepatocellular carcinoma (HCC), and bile duct hyperplasia.[5][7] Repeated exposure to low doses over a lifetime causes chronic diseases, including cancer of the liver, kidney, pancreas, bladder, bone, and other viscera, as well as occupational lung and skin cancers via inhalation and direct contact.[5] Aflatoxins were also reported to cause immunosuppression, teratogenicity, mutagenicity, cytotoxicity, and estrogenic effects in mammals.[5] Chronic exposure is believed to be involved in nutritional disorders such as kwashiorkor and growth faltering, probably by interfering with absorption of micronutrients (e.g., zinc, iron, vitamins), protein synthesis, and metabolic enzyme activities, leading to impaired child growth and possibly cognitive development.[5][7] Suggested HPO terms for chronic phenotypes include “Hepatocellular carcinoma” (HP:0001402), “Growth delay” (HP:0001510), “Immunodeficiency” (HP:0002721), and “Kwashiorkor” (HP:0001541), while the cancer phenotype may be cross‑referenced to NCIT cancer terms. These chronic phenotypes are generally adult‑onset for HCC, with latency of decades after initial exposure, whereas growth impairment and immune suppression manifest in childhood and adolescence.

The age of onset and progression of aflatoxicosis phenotypes varies by exposure intensity and host factors. Acute aflatoxicosis can occur at any age upon ingestion of heavily contaminated food, but outbreaks have disproportionately affected children under 15 and adults over 40, suggesting both behavioral and physiological influences on vulnerability.[11] The onset of acute symptoms is typically subacute, developing over days to weeks after consumption of contaminated food, with progression to hepatic failure and death occurring over days to weeks, depending on dose and supportive care.[11][12] Severity is often high, with mortality rates in outbreaks ranging from 16.2% to 76.5%, and symptom progression is rapid and progressive rather than fluctuating.[11] Chronic aflatoxicosis phenotypes such as HCC usually develop in adulthood, often in middle age or later, after decades of cumulative exposure, and progression is slowly progressive, reflecting the natural history of cirrhosis and liver cancer.[7][15] Growth impairment due to aflatoxin exposure in children manifests as stunting and underweight, with variable severity depending on co‑existing nutritional and infectious factors, and progression may be insidious, with long‑term consequences for adult height and health.[7] Frequency of specific chronic phenotypes (e.g., HCC attributable to aflatoxin) varies by region, with high prevalence in China and sub‑Saharan Africa where aflatoxin exposure and HBV infection are common.[7][15]

Quality of life impact is substantial for both acute and chronic aflatoxicosis. Acute episodes leading to hepatic failure are life‑threatening and carry high mortality, dramatically impairing functioning, causing pain, fatigue, cognitive impairment due to encephalopathy, and often requiring prolonged hospitalization.[11][12] Survivors may experience long‑term sequelae such as chronic liver disease, decreased work capacity, and reduced quality of life. Chronic aflatoxin‑related HCC is associated with poor prognosis, reduced life expectancy, and severe impairment in physical functioning, emotional well‑being, and social participation, as is typical for advanced liver cancer.[7][15] Growth faltering and kwashiorkor in children result in diminished physical capacity, vulnerability to infections, and cognitive development challenges, impacting school performance and economic prospects.[7] Immunosuppression increases susceptibility to infectious diseases, further lowering health‑related quality of life and increasing disability‑adjusted life years lost in affected populations.[5][7] EQ‑5D and SF‑36 instruments have not been specifically studied in aflatoxicosis cohorts in the sources reviewed, but extrapolation from liver disease and cancer literature suggests that aflatoxin‑related conditions significantly reduce scores in domains of mobility, self‑care, usual activities, pain/discomfort, and anxiety/depression.

In addition to classical clinical features, biomarker phenotypes play a central role in characterizing aflatoxicosis. Serum aflatoxin‑albumin adducts, urinary aflatoxin‑N7‑guanine, and urinary AFM1 are measurable biomarkers reflecting internal dose and biologically effective exposure to aflatoxins.[8][17][18][19] Aflatoxin‑albumin adducts can be detected in serum and provide an integrated measure of exposure over weeks to months, with higher concentrations associated with increased liver cancer risk.[8] Urinary AFB1‑N7‑guanine represents a depurinating DNA adduct, and elevated urinary excretion is associated with increased risk of liver cancer; probiotic interventions have demonstrated that lowering this biomarker corresponds to reduced effective aflatoxin dose.[17] AFM1 in urine reflects recent exposure to AFB1 and its metabolism, and is widely used in exposure assessment studies.[7][19] From an ontology standpoint, these biomarkers can be represented using NCIT terms such as “NCIT:C146883 Aflatoxin B1‑Albumin Adduct Measurement” and appropriate LOINC analyte codes, linking biochemical phenotypes to clinical outcomes. Their frequency among exposed individuals is high in endemic regions, with intervention studies reporting detectable aflatoxin‑albumin adducts in the majority of participants at baseline.[18][19]

To summarize phenotypes in a structured manner, aflatoxicosis can be conceptualized as a toxicologic disease with acute hepatic failure, gastrointestinal symptoms, and high mortality at high doses, and chronic carcinogenic, immunotoxic, and growth‑impairing effects at lower, repeated doses. Suggested HPO terms for major clinical features include “Acute liver failure” (HP:0001410), “Jaundice” (HP:0000952), “Vomiting” (HP:0002013), “Abdominal pain” (HP:0002027), “Hepatocellular carcinoma” (HP:0001402), “Growth delay” (HP:0001510), “Kwashiorkor” (HP:0001541), “Immunodeficiency” (HP:0002721), and “Elevated serum transaminases” (HP:0002910). These phenotypes are highly variable in prevalence across populations—but in high‑exposure regions, they contribute substantially to morbidity, mortality, and impaired quality of life, making aflatoxicosis a disease of significant global public health importance.[1][5][7][11][18]

## 4. Genetic and Molecular Information

As a toxicologic disease, aflatoxicosis does not have primary causal genes in the sense of inherited mutations that directly produce disease in the absence of exposure. However, aflatoxins themselves are chemical entities whose metabolism and interaction with macromolecules involve specific human genes and proteins, and chronic aflatoxin carcinogenicity is intimately linked to somatic mutations in key tumor suppressor genes such as TP53. Additionally, the fungal organisms that produce aflatoxins, such as Aspergillus flavus and A. parasiticus, possess biosynthetic gene clusters encoding the enzymes responsible for aflatoxin production, though these belong to the pathogen rather than the human host.[1][2][3][8]

At the level of human molecular biology, aflatoxin B1 is processed in the liver by microsomal cytochrome P450 enzymes (CYP450), especially CYP1A2 and CYP3A4, which bioactivate AFB1 to a highly reactive exo‑8,9‑epoxide intermediate (AFBO).[5] Upon ingestion, AFB1 is absorbed in the duodenum and reaches the liver, where CYP450 bioactivation occurs, generating AFBO that can form covalent adducts with genomic DNA and other functional macromolecules.[5] AFBO reacts primarily with the N7 position of guanine, forming aflatoxin‑N7‑guanine adducts, which can depurinate and lead to mutagenic lesions if not repaired.[5][8] These DNA adducts have been extensively used as biomarkers of exposure, with urinary aflatoxin‑N7‑guanine reflecting ongoing formation and repair of these lesions.[8][17] Serum aflatoxin‑albumin adducts, formed by reaction of AFBO or its hydrolysis products with lysine residues in albumin, provide a long‑term biomarker of exposure and have been used in epidemiologic studies linking exposure to liver cancer.[8][18][19] Thus, while there are no hereditary pathogenic variants associated with aflatoxicosis, key human genes involved in its pathophysiology include CYP450 isoforms (e.g., CYP1A2, CYP3A4), glutathione S‑transferases (e.g., GSTM1, GSTT1) that detoxify AFBO to less harmful conjugates, and DNA repair genes that respond to aflatoxin‑induced lesions.

The most prominent somatic genetic event associated with chronic aflatoxin exposure is the G to T transversion at codon 249 of the TP53 gene, resulting in an arginine‑to‑serine substitution (R249S) in the p53 protein.[15] This mutation is commonly found in HCC from patients in regions with dietary aflatoxin exposure, and has been regarded as a mutational signature of aflatoxin carcinogenesis.[15] A meta‑analysis combining original data from Chinese HCC patients with 48 published studies found that the mean proportion of HCCs harboring the 249(ser) mutation was positively correlated with aflatoxin exposure, with higher aflatoxin levels associated with greater prevalence of this specific p53 mutation.[15] The same analysis found little evidence for an HBV–aflatoxin interaction modulating the presence of p53 249(ser) or any p53 mutation, suggesting that aflatoxin acts as a direct mutagen, while HBV may act via independent mechanisms such as chronic inflammation and integration.[15] From an ontology standpoint, this event can be annotated as a somatic TP53 point mutation (HGNC:11998), with associated GO terms such as “DNA damage response, signal transduction by p53 class mediator” (GO:0030330). In aflatoxin‑related HCC, p53 dysfunction results in loss of normal tumor suppressor activity, contributing to uncontrolled proliferation and resistance to apoptosis.

Other molecular consequences of aflatoxin exposure include widespread oxidative stress and lipid peroxidation, alterations in gene expression, and epigenetic changes. Processing of AFB1 by CYP450 enzymes induces oxidative stress, releasing excessive amounts of reactive oxygen species (ROS) that can attack nitrogen bases and deoxyribose moieties of DNA, generating more than 100 different DNA adducts beyond aflatoxin‑N7‑guanine.[5] ROS can also peroxidize membrane lipids, leading to loss of membrane integrity, mitochondrial damage, and endoplasmic reticulum (ER) stress.[5] These processes involve GO biological processes such as “response to oxidative stress” (GO:0006979), “lipid peroxidation” (GO:0006638), and “apoptotic process” (GO:0006915). Epigenetic changes, including DNA methylation and histone modifications, have been reported in aflatoxin‑induced hepatocarcinogenesis, though specific loci and patterns are beyond the scope of the cited sources. Transcriptomic and proteomic profiling of aflatoxin‑exposed cells and tissues has revealed upregulation of stress response pathways, detoxification enzymes, and DNA repair pathways, and downregulation of normal metabolic and biosynthetic processes, consistent with the broad impact of AFBO adducts on cellular function.[5]

No pathogenic germline variants have been catalogued in ClinVar or HGMD as causal for aflatoxicosis, and aflatoxicosis is not listed as a Mendelian disorder in OMIM, reflecting its primary classification as a toxic exposure disease. Somatic variants, particularly TP53 codon 249 mutations, are the most clinically significant genetic lesions associated with chronic aflatoxin exposure, and are usually catalogued in somatic mutation databases such as COSMIC under HCC entries. Functional consequences of these variants include loss of p53‑mediated cell cycle arrest, impaired DNA damage response, and increased genomic instability, contributing to malignant transformation. From a classification standpoint, these variants would be considered “pathogenic” in the context of somatic cancer genetics, but their presence reflects downstream consequences of exposure rather than inherited susceptibility.

Modifier genes, in the sense of human germline variants that alter severity or expression of aflatoxicosis, are likely to include genes involved in xenobiotic metabolism and antioxidant defenses. For example, deletion polymorphisms in GSTM1 or GSTT1 may reduce detoxification capacity for AFBO and increase risk of DNA adduct formation and carcinogenesis, while functional variants in NQO1 or superoxide dismutases may influence susceptibility to oxidative stress.[5] However, specific evidence from the sources provided is limited, and comprehensive gene–environment interaction studies have not yet firmly established causative modifier alleles. Thus, while the concept of modifier genes is relevant to aflatoxicosis, explicit gene annotations should be treated as hypothetical or inferred rather than demonstrated, pending focused genetic epidemiology studies.

To integrate molecular information into the knowledge base, aflatoxicosis should be annotated with key human gene and protein entities involved in aflatoxin metabolism and response, such as CYP1A2 (HGNC:2595), CYP3A4 (HGNC:2625), GSTM1 (HGNC:4637), GSTT1 (HGNC:4639), and TP53 (HGNC:11998). GO terms for biological processes include “xenobiotic metabolic process” (GO:0006805), “DNA adduct formation” (GO:0006307 as part of DNA repair), “response to DNA damage stimulus” (GO:0006974), and “apoptotic process” (GO:0006915). CHEBI terms for aflatoxins, as noted, encompass the chemical entities central to disease causation. While genetic testing is not relevant for diagnosing aflatoxicosis per se, molecular profiling of aflatoxin‑related HCC can identify TP53 mutations and other somatic alterations, informing cancer prognosis and treatment, but the primary diagnostic emphasis remains on exposure biomarkers and hepatic function tests rather than germline genetics.[5][8][15][17][18][19]

## 5. Environmental and Lifestyle Determinants

Environmental factors are the predominant determinants of aflatoxicosis, and their characterization is essential for understanding disease distribution and designing prevention strategies. As noted, aflatoxins are produced by Aspergillus flavus and related fungi that infect crops in the field and proliferate during storage, with climatic and agronomic conditions playing central roles.[1][2][3][4][7] High temperatures, typically above 21.1°C, combined with either high humidity that increases grain moisture above 15% or drought that stresses crops and makes them more susceptible to infection, favor aflatoxin production.[2][3][4][14] Insect damage to crops further predisposes to fungal invasion by creating entry points and microenvironments conducive to mold growth.[2][3][4][14] From an environmental ontology perspective, these can be represented using terms such as “NCIT:C165860 Drought,” “NCIT:C25672 High Temperature,” and “NCIT:C26549 Insect Infestation,” linked to “NCIT:C134019 Mycotoxin Exposure.” Agricultural practices such as inadequate drying, poor storage (e.g., in damp or unventilated structures), and lack of sorting to remove visibly mouldy kernels exacerbate contamination and increase risk of aflatoxicosis in consumers.[1][3][4][18]

Lifestyle factors related to diet are important determinants of individual exposure. Subsistence farming communities in sub‑Saharan Africa and South Asia often rely heavily on maize and groundnuts as staple foods, and these crops are frequently contaminated with high levels of aflatoxins, making dietary exposure a major public health concern.[7][18] Aflatoxin exposure can occur throughout the life course, beginning in utero through transplacental passage of aflatoxins from mother to fetus, continuing during breastfeeding via AFM1 in breast milk, and persisting through childhood and adulthood via contaminated staple foods.[7] Thus, dietary patterns characterized by high consumption of susceptible crops, lack of dietary diversity, and limited access to safe storage and commercial screening are lifestyle risk factors for aflatoxicosis. Conversely, diets with diversified staples, reduced consumption of high‑risk foods, and access to aflatoxin‑free commercial products are protective. Alcohol consumption and smoking may further increase the risk of aflatoxin‑related liver disease by independently damaging hepatic tissue and interacting with xenobiotic metabolism, although specific evidence in the aflatoxicosis literature is limited.

Infectious agents, particularly hepatitis B virus, act as important cofactors rather than direct causes of aflatoxicosis. Chronic HBV infection, endemic in many high‑aflatoxin regions, substantially increases the risk of HCC among individuals exposed to aflatoxins.[7][15] Thus, the combination of environmental toxin exposure and chronic viral infection produces a synergistic burden of liver cancer, illustrating a complex epidemiologic interaction between infectious diseases and toxic exposures. Other infections, such as hepatitis C virus, may also contribute to liver cancer risk, but HBV is the principal cofactor highlighted in the literature. These relationships can be annotated using NCIT terms for “Hepatitis B Virus Infection” and “Hepatocellular Carcinoma,” linked to “Aflatoxin Exposure” in a causal network.

Public health and socioeconomic contexts profoundly shape environmental and lifestyle determinants of aflatoxicosis. Rapid population growth, climate change, and economic constraints may increase the frequency of droughts and extreme weather events, exacerbating susceptibility of crops to aflatoxin contamination.[2][3][4] Lack of regulatory infrastructure, testing capacity, and enforcement of maximum permissible aflatoxin levels in food in many low‑ and middle‑income countries leads to widespread distribution of contaminated products.[1][7] The U.S. Food and Drug Administration (FDA) considers aflatoxin an unavoidable contaminant in food, and sets action levels for human foods at 20 µg/kg (ppb) for total aflatoxins (except milk, where AFM1 is limited to 0.5 µg/kg), and for animal feed at 20–300 µg/kg depending on species.[4] Many countries lack comparable regulatory thresholds or enforcement mechanisms, and subsistence farmers often consume their own produce without formal testing, increasing exposure. Poverty and food insecurity may force households to consume visibly mouldy food, further elevating risk. Conversely, improved regulatory frameworks, enforcement of aflatoxin limits, subsidized testing, and public awareness campaigns can reduce exposure and thus act as environmental protective factors.[1][7][18]

In this context, behavioral interventions such as education about aflatoxins, training in proper drying and storage, and promotion of crop diversification are important tools for reducing aflatoxicosis. The West African intervention study mentioned earlier demonstrates that simple postharvest measures implemented at subsistence farms can substantially reduce aflatoxin contamination and human exposure, illustrating the power of community‑based environmental interventions.[18] Probiotic supplementation represents a more individualized protective behavior, where consumption of specific fermented products containing aflatoxin‑binding bacteria can lower internal dose despite ongoing environmental contamination.[17][19] Knowledge about aflatoxins itself appears to influence exposure; the Malaysian probiotic study found that subjects with lower aflatoxin knowledge had significantly higher AFB1‑lysine concentrations than those with higher knowledge, suggesting that awareness may inform safer dietary choices.[19] These findings underscore the importance of behavioral and educational strategies in aflatoxicosis prevention.

Taken together, environmental and lifestyle determinants of aflatoxicosis can be summarized as a synergy between climatic conditions that favor fungal growth, agricultural practices that allow contamination, dietary patterns that rely heavily on susceptible crops, infectious cofactors such as HBV, and socioeconomic constraints that limit prevention and control. Ontologically, these determinants can be encoded using exposure and environment frameworks, linking aflatoxicosis to a broad network of risk factors and potential intervention points relevant for public health and clinical practice.

## 6. Mechanisms and Pathophysiology

### Ordered Causal Chain from Exposure to Clinical Manifestation

Step 1 – Chronic or acute dietary exposure to aflatoxin B1 and related aflatoxins from mould‑contaminated maize, groundnuts, and other staples leads to ingestion of these difuranocoumarin mycotoxins and their absorption in the duodenum.[1][3][5][7]

Step 2 – Absorbed aflatoxin B1 is transported via the portal circulation to the liver, where microsomal cytochrome P450 enzymes bioactivate it to a highly reactive exo‑8,9‑epoxide (AFBO), initiating molecular interactions with DNA, proteins, and phospholipids.[5]

Step 3 – AFBO formation results in covalent binding to genomic DNA, producing aflatoxin‑N7‑guanine and other DNA adducts, and to serum albumin and other proteins, generating aflatoxin‑albumin and aflatoxin‑protein adducts that interfere with normal cellular functions.[5][8]

Step 4 – The accumulation of DNA adducts leads to mutations in key genes such as TP53, particularly a G to T transversion at codon 249 (R249S), while protein adducts disrupt vital pathways including messenger RNA synthesis, protein synthesis, and enzyme activity, resulting in genotoxicity and cytotoxicity.[4][5][15]

Step 5 – Bioactivation and adduct formation induce oxidative stress, with excessive reactive oxygen species causing lipid peroxidation, membrane damage, mitochondrial dysfunction, and endoplasmic reticulum stress, leading to hepatocellular vacuolar degeneration, necrosis, and impaired liver function.[5][20]

Step 6 – At high aflatoxin doses, these processes overwhelm cellular detoxification and repair mechanisms, resulting in acute hepatocellular necrosis, massive tissue damage, disruption of cell cycle progression, metabolic failure, and acute hepatic failure with clinical manifestations such as jaundice, vomiting, abdominal pain, and potentially death.[5][11][12][20]

Step 7 – At lower but repeated doses over years, persistent DNA damage, mutations, and epigenetic alterations in hepatocytes lead to progressive dysplasia, bile duct hyperplasia, and eventual hepatocellular carcinoma, especially in the presence of co‑factors like chronic hepatitis B infection.[5][7][15]

Step 8 – Systemically, aflatoxin‑induced interference with protein synthesis, nutrient absorption, and immune cell function results in immunosuppression, growth faltering, and nutritional disorders such as kwashiorkor in children, as well as potential carcinogenesis in other organs exposed via circulation or inhalation.[5][7]

Step 9 – Clinically, these upstream molecular and cellular events manifest as acute and chronic clinical phenotypes, including acute hepatic failure with high mortality, chronic liver disease and HCC, impaired child growth, increased infection susceptibility, and multi‑organ cancers, defining the pathophysiologic spectrum of aflatoxicosis.[5][7][11][15]

### Molecular Pathways and Biochemical Mechanisms

At the molecular level, aflatoxicosis is dominated by the metabolism of aflatoxin B1 by hepatic cytochrome P450 enzymes and the downstream formation of reactive intermediates and adducts. Upon ingestion, AFB1 is absorbed in the duodenum and transported to the liver, where it is bioactivated by CYP450 monooxygenases, particularly CYP1A2 and CYP3A4, to form an exo‑8,9‑epoxide (AFBO) that is highly reactive towards nucleophilic sites in macromolecules.[5] AFBO can undergo two broad fates: detoxification to less harmful metabolites via glutathione conjugation (mediated by GSTs) and other pathways, or reaction with DNA and proteins, producing covalent adducts.[5] The balance between these fates is influenced by dose, enzyme expression, and cellular redox status; at low doses, detoxification mechanisms may suffice, whereas at high doses, AFBO accumulation leads to extensive macromolecular damage.[5] This metabolism can be represented biochemically using KEGG pathways for xenobiotic metabolism and cytochrome P450‑mediated detoxification.

DNA adduct formation is a central mechanism of aflatoxin carcinogenesis. AFBO reacts primarily with the N7 atom of guanine, forming aflatoxin‑N7‑guanine adducts that can depurinate and produce apurinic sites, mispairing, and mutations if not correctly repaired.[5][8] These adducts have been identified and quantified in human urine as aflatoxin‑N7‑guanine, and their presence reflects ongoing genomic damage.[8][17] Other DNA adducts form via ROS‑mediated damage, creating a diverse spectrum of lesions that can overwhelm repair systems. Processing of AFB1 by CYP450 enzymes induces oxidative stress, generating reactive oxygen species that attack nitrogen bases and deoxyribose moieties in DNA, and can produce more than 100 different DNA adducts.[5] The TP53 codon 249 G to T transversion is one prominent mutational consequence, but many other mutations and chromosomal aberrations may accrue over time.[15] Mechanistically, this corresponds to GO processes such as “DNA damage” (GO:0006281), “DNA repair” (GO:0006289), and “mutagenesis” (GO:0043408), and underlies the development of HCC and other aflatoxin‑related cancers.

Protein adducts are particularly important in acute aflatoxicosis. AFBO and its hydrolysis products can react with lysine residues in proteins such as serum albumin, forming aflatoxin‑albumin adducts that serve both as biomarkers and as functional disruptors.[8] Aflatoxin‑protein adducts have been most frequently associated with acute intoxication, as they block protein synthesis and impair enzymes involved in vital functions such as metabolic pathways, DNA replication and repair, and immune responses.[5] This suppression of messenger RNA synthesis and inhibition of protein synthesis appear to be major cytotoxic mechanisms, particularly in hepatocytes, where aflatoxins impair the template activity of chromatin to produce mRNA.[3][4][5] Veterinary toxicology references note that aflatoxins suppress messenger RNA synthesis, leading to inhibition of protein synthesis and targeting the liver, with periacinar necrosis and marked fatty change.[4] These processes can be annotated with GO terms such as “negative regulation of transcription by RNA polymerase II” (GO:0000122), “negative regulation of translation” (GO:0017148), and “protein adduct formation” as part of xenobiotic metabolism.

Phospholipid adducts and membrane lipid peroxidation further contribute to tissue injury. Aflatoxin‑phospholipid adducts and ROS‑induced lipid peroxidation (LPO) are major reasons for disruption of membrane integrity and function in cells, mitochondria, and the ER.[5] Membrane damage can lead to leakage of enzymes, dysregulated ion homeostasis, mitochondrial depolarization, and activation of cell death pathways. Histopathological and ultrastructural studies in rats exposed to AFB1 at 250 µg/kg/day for 8 weeks have demonstrated massive vacuolar degeneration of hepatocytes, necrotic changes, damage to sinusoidal endothelium, aggregations of hyperactive Kupffer cells in the space of Disse, and damaged telocytes, indicating that AFB1 induces irreversible adverse effects on liver microarchitecture.[20] This hepatic injury is characterized by central vein dilatation and congestion, focal hepatocellular necrosis, Kupffer cell proliferation, and distention of interlobular veins, reflecting profound structural and functional disruption.[20] These organ‑level findings correspond to GO cellular component terms such as “mitochondrion” (GO:0005739), “endoplasmic reticulum” (GO:0005783), “plasma membrane” (GO:0005886), and “space of Disse” as a specialized liver microenvironment.

### Cellular Processes and Tissue Damage

At the cellular level, aflatoxicosis is characterized by a spectrum of processes including apoptosis, necrosis, cell cycle dysregulation, inflammation, and impaired cell proliferation and differentiation. Acute high‑dose exposure tends to produce necrosis and acute cell death, particularly in hepatocytes, whereas chronic low‑dose exposure biases towards dysplasia, aberrant proliferation, and eventual neoplasia.[5][20] Severe DNA fragmentation upon exposure to high doses of aflatoxins has been documented, for example in testicular tissues of mice injected with a daily dose of 20 µg AFB1/kg body weight for 21 days, indicating that aflatoxin toxicity is not limited to the liver but can affect germ cells and other tissues.[5] Severe DNA fragmentation is a hallmark of apoptosis, and its presence in testicular tissues suggests potential reproductive toxicity and teratogenicity.[5] In the liver, histologic findings of massive vacuolar degeneration and necrosis indicate both apoptotic and necrotic cell death pathways.[20] Kupffer cell proliferation and invasion of the space of Disse with immune cells and Ito cells overloaded with lipids suggest a robust inflammatory response and activation of stellate cells, which can contribute to fibrosis.[20] These processes involve GO terms such as “apoptotic process” (GO:0006915), “necrotic cell death” (GO:0070265), “inflammatory response” (GO:0006954), and “fibrosis” (GO:0002247).

Immune system involvement in aflatoxicosis includes immunosuppression and altered immune cell function. Chronic aflatoxin exposure has been reported to lower cell‑mediated immunity, increasing susceptibility to infections.[7] Aflatoxins can affect immunocompetent cells by forming adducts with their proteins, impairing their functions, and by indirect nutritional and metabolic effects that compromise immune responses.[5] In animals, aflatoxins are immunosuppressive and can lead to increased susceptibility to infectious diseases, decreased vaccine efficacy, and poor performance.[2][3][4][14] Suggested GO terms for these processes include “negative regulation of immune response” (GO:0006955) and “T cell activation” (GO:0042110), while relevant cell types include hepatocytes (CL:0000182), Kupffer cells (CL:0000860), stellate cells, and various lymphocyte subsets. Clinically, immunosuppression manifests as increased infection rates and poorer outcomes, although specific patterns vary by context and co‑morbid exposures.

Metabolic changes in aflatoxicosis include interference with nutrient absorption, protein synthesis, and metabolic enzyme activities. Chronic exposure is believed to contribute to nutritional disorders such as kwashiorkor and growth faltering by interfering with absorption of micronutrients (zinc, iron, vitamins), protein synthesis, and metabolic enzymes, thereby impairing growth and development.[5][7] In the liver, aflatoxins impair normal metabolic pathways, including gluconeogenesis, lipid metabolism, and detoxification, leading to hypoglycemia, dyslipidemia, and accumulation of toxic metabolites. In animals, aflatoxins reduce feed efficiency, weight gain, and milk production, reflecting systemic metabolic disruption.[2][3][4][14] These metabolic perturbations can be annotated with GO terms such as “negative regulation of protein biosynthetic process” (GO:0031327), “lipid metabolic process” (GO:0006629), and “carbohydrate metabolic process” (GO:0005975). They contribute to clinical phenotypes of weight loss, growth delay, fatigue, and organ dysfunction.

### Upstream versus Downstream Mechanisms and Branching

Mechanistically, upstream events in aflatoxicosis include environmental exposure to aflatoxins, intestinal absorption, hepatic bioactivation by CYP450 enzymes, and initial formation of reactive intermediates and adducts.[1][5][7] These upstream processes are necessary for any downstream effects and are common to both acute and chronic disease presentations. The mechanism then branches, with one branch leading towards acute intoxication and cell death, and another towards cumulative DNA damage and carcinogenesis. In the acute branch, high aflatoxin doses produce extensive protein adducts, suppression of mRNA and protein synthesis, acute oxidative stress, and rapid hepatocellular necrosis, culminating in acute hepatic failure and systemic toxicity.[5][11][20] In the chronic branch, lower doses over time produce persistent DNA adducts, mutations (particularly in TP53), epigenetic changes, and gradual dysregulation of cell cycle control and apoptosis, leading to HCC and other cancers.[5][7][15] Both branches share downstream phenomena such as oxidative stress and immune modulation, but differ in time scale, predominant cell death pathways, and clinical outcomes.

Upstream mechanisms also include host factors such as HBV infection and nutritional status, which modulate the response to aflatoxin exposure. HBV infection creates a chronic inflammatory milieu in the liver, with ongoing cell death and regeneration, that may interact with aflatoxin‑induced mutagenesis to accelerate carcinogenesis.[7][15] Nutritional deficiencies may reduce detoxification capacity and repair mechanisms, increasing vulnerability to both acute and chronic damage.[5][7] Downstream mechanisms involve organ‑level manifestations such as hepatic failure, HCC, growth impairment, and immunosuppression, reflecting the cumulative effect of molecular and cellular events on tissues and systems.

### Suggested GO and CL Terms, and Cell Types Involved

As noted, key GO biological process terms relevant to aflatoxicosis include “xenobiotic metabolic process” (GO:0006805), “response to oxidative stress” (GO:0006979), “DNA damage response, signal transduction by p53 class mediator” (GO:0030330), “apoptotic process” (GO:0006915), “negative regulation of transcription” (GO:0045892), “negative regulation of translation” (GO:0017148), “inflammatory response” (GO:0006954), and “negative regulation of immune response” (GO:0006955). GO cellular component terms include “mitochondrion” (GO:0005739), “endoplasmic reticulum” (GO:0005783), “plasma membrane” (GO:0005886), and “nucleus” (GO:0005634). Relevant CL cell type terms include hepatocytes (CL:0000182), Kupffer cells (CL:0000860), hepatic stellate cells, immunocompetent cells such as T lymphocytes (CL:0000084), and germ cells such as spermatogonia (CL:0000213) in reproductive toxicity contexts. These annotations collectively provide a multi‑scale representation of aflatoxicosis pathophysiology, linking exposure to molecular pathways, cell types, tissues, and clinical manifestations.

## 7. Anatomical Structures and Levels of Involvement

Anatomically, aflatoxicosis primarily affects the liver, but can involve multiple organs and tissues, especially in chronic exposure. The liver is the central organ of aflatoxin metabolism and toxicity, as ingested AFB1 is transported to the liver via the portal vein and processed by hepatocytes and other hepatic cells.[5] Uberon terms relevant to liver involvement include “UBERON:0002107 liver” and specialized microstructures such as “hepatic lobule” and “central vein.” Histopathological studies in rats exposed to AFB1 have demonstrated massive vacuolar degeneration of hepatocytes across hepatic lobules, central vein dilatation and congestion, focal necrosis, Kupffer cell proliferation, and damage to sinusoidal endothelium, highlighting the multi‑compartmental injury within the liver.[20] These findings reflect AFB1’s proclivity to target the hepatic parenchyma and microvasculature, and correspond to human observations of elevated liver enzymes, hyperbilirubinemia, coagulopathy, and histologic features of acute hepatitis and chronic cirrhosis in exposed individuals.[1][5][7][11]

Secondary organ involvement includes the kidney, pancreas, bladder, bone, lung, skin, and reproductive organs, especially in chronic exposure contexts where aflatoxin metabolites circulate systemically.[5] Aflatoxins have been reported to cause cancers in these organs, indicating that aflatoxin‑induced DNA damage and mutagenesis are not confined to the liver.[5] Occupational exposure via inhalation of aflatoxin‑contaminated dust can lead to lung cancers, while dermal contact may lead to skin cancers.[5] Uberon terms for relevant organs include “UBERON:0002048 kidney,” “UBERON:0001264 pancreas,” “UBERON:0001255 urinary bladder,” “UBERON:0001463 lung,” and “UBERON:0002097 skin.” In reproductive toxicity studies, aflatoxin exposure has produced severe DNA fragmentation in testicular tissues, suggesting damage to sperm and germline structures.[5] Uberon terms such as “UBERON:0000473 testis” and “UBERON:0002338 seminiferous tubule” would be relevant in such contexts. System involvement includes the digestive system (due to ingestion and gastrointestinal symptoms), hepatic and biliary systems, immune system (immunosuppression), endocrine system (via estrogenic effects), and hematologic system (coagulopathy and anemia). These multi‑system involvements highlight aflatoxicosis as a disease of broad anatomical reach, even though the liver is the primary target.

At the tissue level, aflatoxicosis disproportionately affects epithelial tissues and parenchymal cells, particularly hepatocytes (simple cuboidal epithelium) in the liver and other organ‑specific epithelial cells in carcinogenic contexts. Connective tissue elements such as sinusoidal endothelium, stellate cells, and extracellular matrix are also affected, particularly in fibrosis and cirrhosis. Histologic findings in AFB1‑treated rat liver include damage to sinusoidal endothelium, hyperactive Kupffer cells occupying the space of Disse, and Ito cells (stellate cells) overloaded with lipids, reflecting injury to endothelial and mesenchymal elements.[20] Telocytes, specialized interstitial cells involved in intercellular signaling and tissue homeostasis, are also damaged, suggesting that aflatoxicosis may disrupt microarchitectural communications.[20] These findings may correspond to Uberon and CL terms for hepatic sinusoidal endothelial cells (CL:0000453), Kupffer cells (CL:0000860), hepatic stellate cells, and telocytes. In the gastrointestinal tract, epithelial cells of the duodenum participate in aflatoxin absorption, but direct toxicity is less extensively documented; however, ingestion of aflatoxin‑contaminated food may cause mucosal irritation and symptoms such as nausea and vomiting.[1][11]

At the subcellular level, aflatoxicosis involves multiple cellular compartments. AFB1 metabolism occurs in the smooth endoplasmic reticulum, where CYP450 enzymes are localized, and AFBO formation takes place.[5] DNA adducts are formed in the nucleus, affecting chromatin structure and gene expression. ROS generation and lipid peroxidation damage mitochondria, leading to mitochondrial swelling, loss of cristae, and impaired ATP production.[5][20] Membrane lipid peroxidation affects the plasma membrane and intracellular organellar membranes, disrupting ion gradients and signaling. Ultrastructural examinations of hepatocytes in AFB1‑treated rats reveal damage to sinusoidal endothelium and telocytes, as well as vacuolar degeneration, indicating widespread subcellular damage.[20] GO cellular component terms such as “endoplasmic reticulum” (GO:0005783), “nucleus” (GO:0005634), “mitochondrion” (GO:0005739), “plasma membrane” (GO:0005886), and “cytoplasm” (GO:0005737) are relevant descriptors of subcellular involvement. These compartments are sites of AFBO formation, DNA adduct binding, lipid peroxidation, and protein adduct formation, and their dysfunction underlies the clinical manifestations of aflatoxicosis.

Localization patterns in aflatoxicosis are largely systemic rather than unilateral or localized. Liver involvement is diffuse, affecting lobules across the organ, rather than confined to specific segments or lobes.[20] In many cases, exposure is systemic, with aflatoxin circulating in the bloodstream and reaching multiple organs, though the liver bears the brunt of injury due to concentration and metabolic activation. Lateralization, in the sense of unilateral versus bilateral involvement, is not typically relevant to aflatoxicosis, as organ systems such as liver, kidney, and bone marrow are centrally located or function bilaterally; however, lung and kidney cancers may arise in one organ preferentially, as in other malignancies. Localized occupational exposure, such as inhalation in one lung region or dermal contact on specific skin areas, may produce localized lesions, but systemic absorption can still occur. Accordingly, aflatoxicosis is best conceptualized as a disease with systemic anatomical impact, centered on the liver but involving multiple tissues and organ systems via circulating toxins and their metabolites.

## 8. Temporal Development and Natural History

The temporal development of aflatoxicosis is shaped by dose, duration, and pattern of exposure, as well as host factors such as age, HBV infection, and nutritional status. Acute aflatoxicosis typically arises after short‑term exposure to high levels of aflatoxin in contaminated food, with onset occurring over days to weeks. Outbreak investigations indicate that ingestion of heavily contaminated maize or groundnuts can lead to acute symptoms, including vomiting, jaundice, and abdominal pain, within days of exposure, with progression to acute hepatic failure and death occurring over subsequent days or weeks.[11][13] In the 2004 Kenyan outbreak, contaminated maize was implicated, and an S strain of Aspergillus flavus was associated with lethal aflatoxicoses.[13] Mortality rates ranged from 16.2% to 76.5%, and an attack rate of 8 cases per 100,000 was estimated in one outbreak.[11] These data illustrate that acute aflatoxicosis has a rapid, progressive course, often culminating in death if exposure is high and supportive care is inadequate. The disease duration in acute cases is typically short, on the order of days to a few weeks, and remission, when it occurs, is induced by cessation of exposure and supportive care rather than spontaneous resolution in the face of ongoing exposure.[1][11][12]

Chronic aflatoxicosis develops over years to decades of exposure to low or moderate levels of aflatoxin. The most serious chronic outcome, hepatocellular carcinoma, usually appears in middle age or later, reflecting a long latency period between initial exposure and clinically detectable cancer.[7][15] Chronic liver disease and cirrhosis may precede HCC, and the progression from chronic exposure to cirrhosis and HCC is slow and progressive, often spanning decades.[7] In high‑exposure regions, the incidence of HCC is among the highest in the world, and aflatoxin contributes substantially to the burden.[7][15] For example, in some regions of China, HCC incidence is extremely high, and chronic HBV infection and dietary aflatoxin exposure are recognized as the main risk factors.[15] Progression patterns in chronic aflatoxicosis thus involve a long subclinical phase where DNA damage, mutations, and epigenetic changes accumulate, followed by an intermediate phase of cirrhosis or dysplasia, and an advanced phase of overt HCC and liver failure.

Growth impairment and nutritional disorders related to aflatoxin exposure in children may manifest over months to years of exposure. Recent evidence suggests that aflatoxin may be an underlying determinant of stunted child growth, and may lower cell‑mediated immunity, increasing disease susceptibility.[7] Studies have reported associations between aflatoxin biomarkers and height‑for‑age or weight‑for‑age Z‑scores, indicating that children with higher aflatoxin exposure exhibit poorer growth.[7] These phenotypes progress gradually, and may not be recognized acutely, but accumulate as long‑term functional deficits. Remission patterns are possible if exposure is reduced or eliminated, particularly if nutritional and health interventions are provided, but some consequences, such as stunted adult height, may be irreversible.

Disease stages in aflatoxicosis can be conceptualized analogously to other toxic and carcinogenic diseases. In acute aflatoxicosis, an early stage comprises mild gastrointestinal symptoms and laboratory evidence of hepatic injury; an intermediate stage involves overt jaundice, coagulopathy, and encephalopathy; and an advanced stage comprises fulminant hepatic failure and multi‑organ dysfunction. Progression rate is rapid, and the course is progressive without relapses, as continued exposure exacerbates damage and cessation of exposure is required for stabilization or recovery.[1][11][12] In chronic aflatoxicosis, early stages involve subclinical DNA damage and biomarker positivity (aflatoxin‑albumin adducts, urinary aflatoxin‑N7‑guanine) without overt disease; intermediate stages involve chronic liver disease and cirrhosis; and advanced stages involve HCC and metastatic cancer.[5][7][8][15] Disease duration is long, and the course is progressive, though interventions such as HBV vaccination, improved diet, and reduced exposure can modify trajectory.

Critical periods in aflatoxicosis include early childhood and perinatal periods, when growth and development are particularly sensitive to nutritional and toxic insults. In utero exposure to aflatoxins via transplacental transfer may affect fetal development, while exposure via breast milk in infancy may influence early growth and immune maturation.[7] Childhood and adolescence are critical periods for linear growth, and aflatoxin exposure during these times may result in stunting and reduced adult height.[7] From an intervention standpoint, the immediate postharvest period is critical for implementing measures to reduce aflatoxin contamination, as contamination often accumulates during storage.[1][18] Similarly, early adulthood is a critical period for HBV vaccination, which can reduce the risk of HBV–aflatoxin synergy in HCC later in life.

In summary, the temporal development of aflatoxicosis can be characterized by rapid onset and progression in acute high‑dose exposures and slow, insidious progression in chronic low‑dose exposures, with distinct critical periods and intervention windows. Understanding these temporal patterns is crucial for designing screening, prevention, and treatment strategies that are appropriately timed to mitigate both immediate and long‑term disease burden.

## 9. Inheritance, Epidemiology, and Population Patterns

Aflatoxicosis is not a genetic disease and has no classical inheritance pattern such as autosomal dominant or recessive transmission. Instead, its “inheritance” is better understood in terms of transmission of environmental exposure and socioeconomic conditions across generations. Families may share dietary patterns, agricultural practices, and HBV infection statuses, leading to clustering of aflatoxin exposure and related diseases within households and communities, but this reflects shared environment rather than germline mutations. Penetrance and expressivity are thus functions of exposure levels and host factors rather than genetic allele frequencies. Genetic anticipation, germline mosaicism, founder effects, consanguinity, and carrier frequency, as defined for Mendelian disorders, are not directly applicable to aflatoxicosis.

Epidemiologically, aflatoxicosis is a major global health problem, particularly in developing countries. StatPearls notes that approximately 25% of the world’s crop is affected by mycotoxins, most of which are aflatoxins, and that approximately 4.5 billion people in developing countries are exposed to substantial levels of aflatoxin.[1] Human aflatoxicosis is especially prevalent in subsistence farming communities in sub‑Saharan Africa and South Asia, where dietary staple food crops such as groundnuts and maize are often highly contaminated.[7] Aflatoxin exposure is considered a major public health concern in these regions, contributing to hepatocellular carcinoma, growth impairment, and immunosuppression.[7] Prevalence and incidence of acute aflatoxicosis episodes are less well characterized, due to under‑reporting and misclassification, but a systematic review identified several outbreaks, with one providing sufficient data to estimate an attack rate of 8 cases per 100,000.[11] Mortality rates in outbreaks ranged from 16.2% to 76.5%, highlighting the severity of acute episodes.[11]

Geographically, regions with hot, humid climates and widespread cultivation of susceptible crops are at highest risk. These include many parts of sub‑Saharan Africa, Southeast Asia, and parts of Latin America and China.[1][7][15][18] In Kenya, maize contaminated with aflatoxins has been implicated in deadly epidemics three times since 1981, including the 2004 outbreak associated with an S strain of Aspergillus flavus.[13] In Guinea, groundnut contamination poses a major exposure source, and the intervention study mentioned earlier was conducted in the lower Kindia region.[18] In China, certain regions have particularly high HCC incidence, attributed to chronic HBV infection and dietary aflatoxin exposure.[15] In developed countries, regulatory frameworks and improved storage and processing have reduced aflatoxin exposure, but pockets of exposure remain, particularly in imported foods and in animal feeds that can transmit AFM1 via milk.[1][2][4][7] Therefore, the geographic distribution of aflatoxicosis is uneven, with endemic areas in the tropics and subtropics, and sporadic cases elsewhere.

Population demographics show that children and older adults are often more severely affected by acute aflatoxicosis. Outbreak data indicate that mortality rates are highest in children under 15 and adults over 40, suggesting age‑related differences in susceptibility and resilience.[11] Children may be more vulnerable due to lower body weight, developing hepatic and immune systems, and higher per‑kilogram exposure when consuming contaminated food. Older adults may have diminished hepatic reserve, co‑morbidities, and reduced ability to recover from acute insults. Chronic aflatoxin‑related HCC predominantly affects adults, often in middle age, with men typically showing higher incidence than women,

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 2 |
| Obsolete | 4 |
| Unverifiable | 5 |
| Terms whose name was checked | 36 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 10 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001541` (2 mentions) - the report calls it "Kwashiorkor"; HP calls it **Ascites**
- `GO:0006638` (1 mention) - the report calls it "lipid peroxidation"; GO calls it **neutral lipid metabolic process**
- `GO:0043408` (1 mention) - the report calls it "mutagenesis"; GO calls it **regulation of MAPK cascade**
- `GO:0002247` (1 mention) - the report calls it "fibrosis"; GO calls it **obsolete clearance of damaged tissue involved in inflammatory response wound healing**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C45570` (1 mention) - NCIT does not contain this term
- `HP:0006826` (1 mention), reported as "Hepatic encephalopathy" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)
- `GO:0002247` (obsolete clearance of damaged tissue involved in inflammatory response wound healing) (1 mention)
- `GO:0031327` (obsolete negative regulation of cellular biosynthetic process) (1 mention) - replaced by `GO:0009890`
- `CL:0000213` (obsolete lining cell) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001410` (2 mentions) - the report calls it "Acute liver failure"; HP calls it **Decreased liver function**
- `HP:0002910` (3 mentions) - the report calls it "Elevated serum transaminases", "Increased circulating alanine aminotransferase concentration"; HP calls it **Elevated circulating hepatic transaminase concentration**
- `HP:0003256` (1 mention) - the report calls it "Coagulopathy"; HP calls it **Abnormality of the coagulation cascade**, and lists "Coagulopathy" among its other names
- `GO:0006974` (1 mention) - the report calls it "response to DNA damage stimulus"; GO calls it **DNA damage response**, and lists "response to DNA damage stimulus" among its other names
- `GO:0006281` (1 mention) - the report calls it "DNA damage"; GO calls it **DNA repair**
- `GO:0006289` (1 mention) - the report calls it "DNA repair"; GO calls it **nucleotide-excision repair**
- `GO:0070265` (1 mention) - the report calls it "necrotic cell death"; GO calls it **obsolete necrotic cell death**
- `GO:0006955` (2 mentions) - the report calls it "negative regulation of immune response"; GO calls it **immune response**
- `GO:0031327` (1 mention) - the report calls it "negative regulation of protein biosynthetic process"; GO calls it **obsolete negative regulation of cellular biosynthetic process**
- `GO:0045892` (1 mention) - the report calls it "negative regulation of transcription"; GO calls it **negative regulation of DNA-templated transcription**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0002910` - called "Elevated serum transaminases", "Increased circulating alanine aminotransferase concentration"