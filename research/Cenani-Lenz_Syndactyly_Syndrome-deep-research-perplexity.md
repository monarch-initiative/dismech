---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-16T11:53:21.730059'
end_time: '2026-10-16T11:56:16.081948'
duration_seconds: 174.35
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cenani-Lenz Syndactyly Syndrome
  mondo_id: MONDO:0008931
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 50
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:38013226
  relevance_assessed: 23
  on_topic: 11
  off_topic: 2
  off_topic_references:
  - DOI:10.1155/2019/9652649
  - PMC:PMC6766129
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 69
  verified: 64
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 10
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0008931
    reported_labels:
    - MONDO
    ontology_label: Cenani-Lenz syndactyly syndrome
  - term_id: DOID:0090015
    reported_labels:
    - Disease Ontology
    ontology_label: Cenani-Lenz syndactyly syndrome
  - term_id: HP:0000494
    reported_labels:
    - Primarily dysmorphic feature
    ontology_label: Downslanted palpebral fissures
  - term_id: CL:0002320
    reported_labels:
    - Metanephric mesenchymal cell
    ontology_label: connective tissue cell
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0001163
    ontology_label: obsolete Abnormality of the metacarpal bones
    replaced_by: HP:0005916
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cenani-Lenz Syndactyly Syndrome
- **MONDO ID:** MONDO:0008931 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cenani-Lenz Syndactyly Syndrome** covering all of the
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

# Cenani–Lenz Syndactyly Syndrome: Disease-Characteristics Research Report

**Disease:** Cenani–Lenz syndactyly syndrome  
**Preferred abbreviation:** CLSS or CLS  
**MONDO:** MONDO:0008931  
**Disease class:** Mendelian congenital-malformation syndrome  
**Core molecular diagnosis:** Biallelic pathogenic variants in **LRP4**

> **Scope note.** CLSS is exceptionally rare, so most evidence comes from individual families, small case series, functional cell studies, and mouse models—not epidemiologic cohorts or randomized trials. A 2024 publication added a prenatal case and new *LRP4* variant, while a 2023 study expanded the phenotype to include congenital myasthenic syndrome in one patient. [PMID: 38013226; PMID: 37640745] [47][59]

---

## 1. Disease information

### 1.1 Definition

Cenani–Lenz syndactyly syndrome is a congenital developmental disorder characterized by severe, usually bilateral complex syndactyly or oligosyndactyly, disorganization and fusion of metacarpal/phalangeal bones, radioulnar abnormalities, and variably renal and craniofacial malformations. The classical hand resembles a “mitten” because of nearly complete digital fusion and synostosis. Lower-limb involvement is common but generally less severe. [16][17]

The molecularly defined classical disorder is an **autosomal-recessive LRP4 loss-of-function disorder**. Related but nosologically distinct “Cenani–Lenz-like” phenotypes can result from rearrangements involving *GREM1–FMN1* or, rarely, *APC* variants. [PMID: 20381006; PMID: 30569497; PMID: 20610440] [6][136][147]

### 1.2 Identifiers and terminology

| Resource | Identifier/name |
|---|---|
| MONDO | **MONDO:0008931** |
| OMIM | **#212780**, Cenani-Lenz syndactyly syndrome |
| Orphanet | **ORPHA:3258** |
| MedGen/UMLS | **C1859309** |
| MeSH supplementary concept | **C538150** |
| GARD | **5084** |
| ICD-10 | **Q78.4**; broad osteochondrodysplasia category rather than a highly specific CLSS code |
| ICD-11 | **LB79.Y**, other specified congenital musculoskeletal anomaly category |
| Disease Ontology | **DOID:0090015** |
| Causal-gene OMIM | **LRP4, OMIM *604270** |
| Common synonyms | Cenani-Lenz syndrome; Cenani syndactyly; Cenani-Lenz syndactyly; Cenani syndactylism; syndactyly type VII/type 7; CLSS; CLS |

These mappings are reported by Orphanet, OMIM/ClinVar and MedGen. [18][80]

### 1.3 Evidence granularity

The information is predominantly **aggregated disease-level knowledge reconstructed from individual patients and pedigrees**. The landmark molecular study examined 14 families and found recessive *LRP4* variants in 12; many later publications are single-family or single-patient reports. It is not derived from population-scale EHR analysis. [PMID: 20381006] [6]

---

## 2. Etiology

### 2.1 Causal factors and risk factors

| Factor | Evidence and interpretation |
|---|---|
| Biallelic *LRP4* variants | Established principal cause. Homozygous or compound-heterozygous missense, splice, nonsense, and frameshift variants impair LRP4 function. [PMID: 20381006] [6] |
| Autosomal-recessive inheritance | Parents are usually unaffected heterozygotes; recurrence risk is 25% for each pregnancy when both parents carry the familial variant. [79] |
| Consanguinity | Strong ascertainment/risk factor because it increases homozygosity for rare alleles. Eleven of 12 mutation-positive families in the original study were reported as consanguineous. [PMID: 20381006] [6] |
| Family history | Affected siblings and multiple affected members occur in extended recessive pedigrees. |
| Founder variants | *LRP4* p.Asp529Asn was found on a shared Turkish haplotype and p.Asp137Asn on a shared Egyptian haplotype, supporting founder effects. [PMID: 20381006] [6] |
| Sex | No evidence of sex-dependent genetic risk; both sexes can be affected because inheritance is autosomal. |
| Environmental, infectious, lifestyle factors | None demonstrated as causes or modifiers of CLSS. |
| Maternal age, paternal age, toxins, diet | No reproducible association identified. |

### 2.2 Protective factors

No genetic or environmental protective factor has been established. Unaffected heterozygous carriers are protected from classical recessive CLSS by retention of one functional allele, but this is inheritance biology rather than a clinically actionable protective intervention.

### 2.3 Gene–environment interaction

No CLSS-specific gene–environment interaction has been demonstrated. Embryonic phenotype is driven primarily by altered developmental signaling during tightly constrained windows of limb and renal morphogenesis. Nutritional, toxicologic, infectious, or lifestyle modulation remains unstudied.

### 2.4 Related genetic phenocopies

A heterozygous 1.7-Mb duplication encompassing *GREM1* and *FMN1* produced autosomal-dominant, isolated Cenani–Lenz-like oligosyndactyly. Other *GREM1–FMN1* rearrangements can cause oligosyndactyly, radioulnar synostosis, hearing loss, and renal defects. These should be treated as differential molecular diagnoses rather than routine causes of classical MONDO:0008931. [PMID: 20610440] [147]

---

## 3. Phenotypes

All major abnormalities are **congenital**, although renal dysfunction, dental consequences, scoliosis, or functional disability may be recognized later. Frequencies below are either qualitative or calculated at the family level from the 12 mutation-positive families in Li et al.; they should not be interpreted as population estimates. [PMID: 20381006] [6]

| Phenotype/type | Onset, severity, course and frequency | Functional/QOL impact | Suggested HPO term |
|---|---|---|---|
| Hand syndactyly | Congenital; usually bilateral and severe/complex; typical in 10/12 molecular families, partial in two and absent as “typical” in one atypical family | Major limitation in grasp, pinch, writing, dressing and self-care; surgery may not restore normal function | Syndactyly, **HP:0001159**; finger syndactyly, **HP:0006101** |
| Oligodactyly/digital-ray reduction | Congenital; variable from partial absence to severe hand/foot agenesis | Reduces manipulative and weight-bearing function | Oligodactyly, **HP:0012165** |
| Metacarpal/phalangeal disorganization or absence | Congenital; reported in all 12 landmark mutation-positive families | Limits reconstructive options and explains poor postoperative function | Abnormal metacarpal morphology, **HP:0001163**; absent phalanges |
| Metacarpal synostosis | Congenital; 11/12 families in the landmark series | Rigid fused rays, reduced hand span and independent digit motion | Metacarpal synostosis, **HP:0009701** |
| Radioulnar synostosis | Congenital; at least 8/10 assessable families in the landmark series | Restricts pronation/supination and activities requiring forearm rotation | Radioulnar synostosis, **HP:0002974** |
| Short radius/ulna and brachymesomelia | Congenital, nonprogressive skeletal malformation; variable | Reduced reach and mechanical leverage | Hypoplasia of radius, **HP:0002984**; hypoplasia of ulna, **HP:0003022** |
| Foot/toe syndactyly | Congenital and common, generally milder than hands | Can affect footwear, gait and balance; severity variable | Toe syndactyly, **HP:0001770** |
| Nail aplasia/hypoplasia | Congenital; very common in affected hands and variable in feet | Cosmetic impact and reduced protection of distal digits | Anonychia, **HP:0001798**; nail dysplasia, **HP:0001597** |
| Renal agenesis | Congenital; unilateral or bilateral. Renal agenesis/hypoplasia occurred in over half of reported *LRP4*-positive families | Unilateral disease requires surveillance; bilateral agenesis is lethal prenatally or neonatally | Renal agenesis, **HP:0000104** |
| Renal hypoplasia | Congenital; unilateral or bilateral | Risk of reduced renal reserve, hypertension and chronic kidney disease | Renal hypoplasia, **HP:0000089** |
| Ectopic kidney | Congenital, occasional | May predispose to obstruction or infection, though CLSS-specific rates are unknown | Ectopic kidney, **HP:0000086** |
| Prominent/broad forehead | Congenital facial morphology; 9/12 landmark families | Usually cosmetic, little direct functional effect | Prominent forehead, **HP:0011220** |
| Hypertelorism | Congenital; approximately 7/12 landmark families | Usually cosmetic | Hypertelorism, **HP:0000316** |
| Downslanting palpebral fissures | Congenital; minority of families | Primarily dysmorphic feature | **HP:0000494** |
| Malar hypoplasia/flattening | Congenital; common but variable | Usually cosmetic; can contribute to craniofacial profile | Malar flattening, **HP:0000272** |
| Micrognathia/retrognathia | Congenital; approximately half of landmark families | Severe cases could affect feeding or airway, but CLSS-specific outcome data are absent | Micrognathia, **HP:0000347** |
| Hypodontia/enamel hypoplasia/early tooth loss | Congenital dental-development abnormality or later consequence; uncommon/variable | Chewing, speech, dental health and cosmetic burden | Hypodontia, **HP:0000668**; enamel hypoplasia, **HP:0006297** |
| Vertebral anomalies, scoliosis, hemivertebrae | Occasional; congenital structure with possible progression of curvature during growth | Pain, posture and mobility effects if severe | Hemivertebrae, **HP:0002937**; scoliosis, **HP:0002650** |
| Developmental delay | Not core; reported in isolated patients, generally absent in most cases | Variable | Global developmental delay, **HP:0001263** |
| Hearing loss, cataract, pulmonary stenosis, hypothyroidism | Isolated case-level associations; causality to CLSS uncertain | Feature-dependent | Hearing impairment **HP:0000365**; cataract **HP:0000518**; pulmonary stenosis **HP:0001642** |
| Fluctuating weakness/CMS | Newly documented in one 2023 patient with p.Tyr607Cys; not established as a routine CLSS manifestation | Fatigability, impaired mobility and neuromuscular disability | Muscle weakness **HP:0001324**; fatigable weakness **HP:0003473** |

MedGen lists the major limb, craniofacial, dental, vertebral, nail and cardiac findings. [91] No validated CLSS-specific EQ-5D, SF-36, PROMIS or quality-of-life cohort has been published.

---

## 4. Genetic and molecular information

### 4.1 Causal gene

| Attribute | Value |
|---|---|
| Gene | **LRP4**, LDL receptor-related protein 4 |
| HGNC | **HGNC:6696** |
| NCBI Gene | **4038** |
| Ensembl | **ENSG00000134569** |
| OMIM gene | ***604270** |
| UniProt | **O75096** |
| Location | **11p11.2** |
| Protein type | Large single-pass type-I membrane receptor with extracellular LDL-A repeats, EGF-like domains and YWTD β-propeller regions |
| Principal CLSS consequence | Partial or complete loss of protein function, commonly through impaired folding/secretory trafficking and failure to reach the cell surface |

Gene identifiers are supported by NCBI/HGNC-linked resources. [61][63]

### 4.2 Representative reported variants

| *LRP4* variant | Type/origin | Evidence or reported interpretation |
|---|---|---|
| c.409G>A, p.Asp137Asn | Homozygous missense; Egyptian founder | Impaired surface localization and Wnt-antagonist function |
| c.479G>A, p.Cys160Tyr | Homozygous missense | Functionally deficient |
| c.1345G>A, p.Asp449Asn | Homozygous missense | Functionally deficient |
| c.1382A>C, p.Thr461Pro | Homozygous missense | Disease segregating |
| c.1417C>T, p.Leu473Phe | Homozygous missense | Functionally deficient |
| c.1585G>A, p.Asp529Asn | Homozygous missense; Turkish founder | Functionally deficient |
| c.3049T>C, p.Cys1017Arg | Homozygous missense | Segregated in a large Pakistani family |
| c.547+1G>A | Homozygous canonical splice variant | Predicted/observed loss of function |
| c.200-9G>A and c.4959G>C | Compound-heterozygous splice variants | Aberrant transcripts and premature truncation |
| c.289G>T, p.Glu97Ter | Homozygous nonsense | Severe CLSS; near-complete loss of function |
| c.2858T>C, p.Leu953Pro | Homozygous missense | Limb and kidney phenotype |
| c.316+1G>A | Homozygous splice donor | Severe CLSS |
| c.4910G>A, p.Cys1637Tyr | Homozygous missense | CLSS with recurrent ketotic hypoglycemia in two brothers; hypoglycemia remains an uncertain expansion |
| c.1820A>G, p.Tyr607Cys | Homozygous missense | 2023 CLSS/CMS overlap; altered agrin and WNT11 binding and reduced acetylcholine-receptor clustering |
| c.282C>A, p.Asn94Lys | Homozygous missense | 2024 prenatal CLSS report; classified as causative by the authors |
| c.3813del, p.Thr1272Leufs*18 | Frameshift | Reported likely pathogenic in a 2025 case |
| c.4910G>A, p.Cys1637Tyr | Missense | VUS in the 2025 compound-heterozygous case, despite earlier homozygous disease association |

The initial variant spectrum and functional assays are from PMID:20381006. [6] The 2024 report states:

> “Exome sequencing revealed a novel biallelic c.282C>A variant in… *LRP4*… causing p.(Asn94Lys).” [PMID: 38013226] [47]

### 4.3 Variant interpretation and population frequency

* Classical CLSS variants are **germline**; no somatic form is recognized.
* Pathogenic mechanisms include nonsense/frameshift-mediated loss of function, abnormal splicing, and missense-induced folding or trafficking defects.
* Landmark missense variants were absent from at least 250 controls, but those historical controls are too small to estimate allele frequency. [PMID:20381006] [6]
* Most credible disease alleles are absent or exceptionally rare in population databases. Exact gnomAD frequencies must be recorded variant by variant and genome build by genome build; no meaningful disease-wide carrier frequency is available.
* ClinVar assertions can differ by variant and submitter. Classification should be based on the current ClinVar record, segregation, functional evidence, population frequency, and ACMG/AMP criteria rather than assuming that every published variant is pathogenic.

### 4.4 Modifiers, epigenetics and structural abnormalities

No validated modifier gene or CLSS-specific methylation/epigenetic signature is known. A *GREM1–FMN1* duplication is a distinct dominant phenocopy, not an established modifier of biallelic *LRP4* disease. No recurrent aneuploidy, translocation, inversion, or mitochondrial variant causes classical CLSS.

---

## 5. Environmental information

| Category | Current evidence |
|---|---|
| Environmental toxins/radiation/pollution | No established causal or modifying exposure |
| Smoking, alcohol, diet, exercise | No demonstrated relationship to occurrence or severity |
| Occupational exposure | Not applicable to a congenital Mendelian developmental disorder |
| Infectious agent | None |
| Immune trigger | None established |
| Prenatal environment | May influence general fetal outcome, but no CLSS-specific interaction has been shown |

Therefore, environmental-risk or lifestyle-prevention claims should not be entered into the knowledge base as established associations.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **Biallelic pathogenic germline variation in *LRP4*** leads to reduced production, abnormal splicing, truncation, misfolding, or defective trafficking of LRP4.
2. **Deficient cell-surface LRP4** leads to loss of its normal integration/antagonism of LRP5/6-mediated canonical WNT signaling and perturbation of WNT–BMP interactions.
3. **Dysregulated WNT/BMP signaling in embryonic limb ectoderm, especially the apical ectodermal ridge**, leads to abnormal spatial expression of FGF8, SHH and BMP-family developmental signals; this in-vivo human step is partly inferred from mouse models.
4. **Abnormal limb-bud patterning and impaired interdigital separation/apoptosis** lead to syndactyly, abnormal digit number, synostosis and disorganization of metacarpals, metatarsals and phalanges.
5. **Altered skeletal patterning and growth** lead to shortened radius/ulna, radioulnar synostosis and brachymesomelia.
6. **In the renal branch, deficient LRP4 signaling** leads to delayed or failed ureteric-bud initiation/outgrowth.
7. **Delayed ureteric budding** leads to inadequate reciprocal stimulation of metanephric mesenchyme, failed differentiation and, variably, renal hypoplasia, ectopia or unilateral/bilateral agenesis.
8. **In the craniofacial/dental branch, altered WNT/BMP integration** leads to abnormal facial-bone and tooth morphogenesis, producing malar hypoplasia, micrognathia, hypodontia, enamel defects or tooth fusion; much of this causal detail is supported by mouse models.
9. **For selected β-propeller variants, impaired agrin–LRP4–MuSK signaling at the neuromuscular junction** leads to reduced acetylcholine-receptor clustering and can result in congenital myasthenic weakness; this has been directly demonstrated for p.Tyr607Cys but is not universal in CLSS. [PMID:37640745] [59]

### 6.2 Molecular and cellular detail

The landmark functional study showed that wild-type LRP4 strongly antagonized WNT1/LRP6-mediated β-catenin reporter activity in HEK293T cells, whereas five CLSS missense proteins lost or markedly reduced that activity. Cell-surface biotinylation showed defective plasma-membrane delivery despite broadly comparable total protein abundance. [PMID:20381006] [6]

Direct abstract evidence states:

> “LRP4 is known to antagonize LRP6-mediated activation of canonical Wnt signaling, a function that is lost by the identified mutations.” [PMID:20381006, published May 14, 2010] [6]

Mouse evidence indicates structural abnormalities of the apical ectodermal ridge and disturbed *Fgf8*, *Bmp4* and *Shh* expression. The precise sequence from excessive canonical WNT activity to each human skeletal lesion remains partly inferred rather than directly measured in human embryos. [37]

### 6.3 Kidney mechanism and quantitative model evidence

In an *Lrp4* null mouse cohort of 156 postnatal animals, **51% had bilateral and 22% unilateral renal agenesis**. The investigators observed delayed ureteric budding with failure to stimulate metanephric mesenchyme in time. [109][116]

> “Lrp4−/− mice show a delay in ureteric bud formation that results in unilateral or bilateral kidney agenesis.” [PMID associated with the 2010 PLoS One study] [116]

### 6.4 Neuromuscular-junction branch

LRP4 is an obligate agrin receptor/coreceptor that recruits and activates MuSK, promoting postsynaptic acetylcholine-receptor clustering. Most classical CLSS patients have no overt neuromuscular phenotype. In 2023, however, a homozygous p.Tyr607Cys β-propeller variant caused limb/renal malformations plus weakness, fatigability and an electrophysiologic decrement; patient myotubes had significantly reduced AChR aggregation. [PMID:37640745, August 28, 2023] [59][60]

### 6.5 Suggested ontology annotations

| Mechanistic entity | Suggested ontology term |
|---|---|
| Canonical WNT signaling | GO:0060070, canonical Wnt signaling pathway |
| Negative regulation of canonical WNT | GO:0090090 |
| Limb morphogenesis | GO:0035108 |
| Embryonic limb morphogenesis | GO:0030326 |
| Apoptotic process | GO:0006915 |
| Bone development/ossification | GO:0060348 / GO:0001503 |
| Kidney development | GO:0001822 |
| Ureteric-bud development | GO:0001657 |
| Neuromuscular-junction development | GO:0007528 |
| Acetylcholine-receptor clustering | GO:0095500 |
| Plasma membrane | GO:0005886 |
| Cell surface | GO:0009986 |
| Limb-bud ectodermal cell | CL annotation should use the closest developmental ectoderm/epithelial-cell term; no CLSS-specific cell term |
| Metanephric mesenchymal cell | CL:0002320 |
| Skeletal-muscle cell/myotube | CL:0000188 / CL:0002372 |
| Osteoblast | CL:0000062 |
| Osteocyte | CL:0000137 |

### 6.6 Omics and advanced technologies

No disease-specific bulk transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic or genome-scale CRISPR study has been established for CLSS patients. Available molecular profiling is chiefly targeted reporter assays, protein trafficking, ligand-binding, splicing, and patient-myotube AChR-clustering experiments.

---

## 7. Anatomical structures affected

| Level | Structures/cells | Suggested ontology |
|---|---|---|
| Primary organ/system | Hands, fingers, carpal/metacarpal/phalangeal skeleton | UBERON:0002398 hand; UBERON:0001435 carpal region; UBERON:0002389 digit |
| Primary organ/system | Feet, toes, metatarsals and phalanges | UBERON:0002387 foot |
| Upper limb | Radius, ulna, radioulnar articulation and forearm | UBERON:0001423 radius; UBERON:0001424 ulna; UBERON:0003403 forearm |
| Renal | Kidney, ureteric bud and metanephric mesenchyme | UBERON:0002113 kidney; UBERON:0000084 metanephros |
| Craniofacial | Frontal, orbital, maxillary/malar and mandibular regions | UBERON:0001708 jaw; UBERON:0001684 mandible |
| Dental | Tooth primordia, enamel and permanent dentition | UBERON:0001091 tooth |
| Vertebral/thoracic | Vertebrae, ribs, sternum | UBERON:0002412 vertebral column |
| Neuromuscular, selected cases | Skeletal muscle neuromuscular junction | UBERON:0001015 musculature; GO:0031594 neuromuscular junction |
| Cellular | Limb-bud ectoderm/AER cells, chondrogenic and osteogenic precursors, metanephric mesenchyme, ureteric epithelium | Developmental epithelial, mesenchymal, chondrocyte and osteoblast CL terms |
| Subcellular | Plasma membrane and secretory pathway; postsynaptic membrane at NMJ | GO:0005886; GO:0045211 |

Hand involvement is generally bilateral and nearly symmetrical, although exact digital anatomy can be asymmetric. Lower limbs are usually bilaterally involved but less severe. Renal agenesis may be unilateral or bilateral. [16][6]

---

## 8. Temporal development

* **Biological onset:** embryonic, during limb-bud and renal-organogenesis windows.
* **Clinical onset:** congenital; detected prenatally by ultrasound in severe cases or at birth.
* **Pattern:** not acute, episodic, inflammatory or relapsing. The structural malformations are largely stable, while secondary orthopedic, renal, dental and functional consequences may evolve with growth.
* **Critical periods:** limb patterning and interdigital separation in early embryogenesis; ureteric-bud initiation during metanephric kidney development. There is no postnatal therapy capable of reversing these developmental events.
* **Disease duration:** lifelong.
* **Remission:** not applicable to congenital skeletal malformations. Surgical reconstruction may improve function but is not biologic remission.
* **Lethal end of spectrum:** bilateral renal agenesis can cause fetal or neonatal death; the original series included a neonate who died on the first day of life and pregnancies terminated after prenatal diagnosis of bilateral agenesis. [PMID:20381006] [6]

---

## 9. Inheritance and population

| Characteristic | Current evidence |
|---|---|
| Inheritance | Autosomal recessive for classical *LRP4*-related CLSS |
| Recurrence | 25% affected, 50% carrier and 25% unaffected/noncarrier per pregnancy when both parents are carriers |
| Penetrance | Apparently high for limb abnormalities among biallelic pathogenic genotypes, but organ-specific manifestations—especially kidney and craniofacial anomalies—are incompletely penetrant |
| Expressivity | Markedly variable, from near-isolated hand syndactyly to extensive limb reduction, renal agenesis and multisystem disease |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Germline mosaicism | Not established, although low residual recurrence risk is theoretically possible after an apparently de novo event |
| Consanguinity | Common in reported families and increases recessive risk |
| Founder effects | p.Asp529Asn in Turkish families; p.Asp137Asn in Egyptian families |
| Carrier frequency | Unknown; no population-screening estimate |
| Sex ratio | No established bias |
| Geographic distribution | Cases reported from Turkey, Egypt, Pakistan, Jordan, Iran, Europe, China, Jewish families and, recently, Sudan; this reflects family ascertainment rather than endemicity |
| Prevalence | Orphanet: **<1 per 1,000,000** |
| Incidence | Not calculated |
| Historical case count | Orphanet stated fewer than 30 described cases; later reports have increased the count, but no current global registry total exists |

Orphanet reports prevalence below one per million and notes that most cases occurred in related families. [16]

---

## 10. Diagnostics

### 10.1 Clinical evaluation

The diagnosis should be suspected in a neonate or child with complex bilateral hand syndactyly/oligodactyly plus metacarpal disorganization, radioulnar synostosis, shortened forearms, renal anomaly or the characteristic facial gestalt.

| Investigation | Purpose |
|---|---|
| Hand, forearm and foot radiographs | Define synostoses, absent/disorganized bones, digital-ray number, radioulnar anatomy and surgical feasibility |
| Renal ultrasound | Mandatory evaluation for agenesis, hypoplasia, ectopia or other structural anomaly |
| Serum creatinine/eGFR, electrolytes and urinalysis | Baseline and longitudinal renal function, especially with a solitary or hypoplastic kidney |
| Blood pressure | Surveillance for renal-associated hypertension |
| Dental evaluation and panoramic imaging | Hypodontia, enamel hypoplasia, abnormal eruption or early tooth loss |
| Spine/chest radiographs when indicated | Hemivertebrae, scoliosis, ribs and pectus abnormality |
| Echocardiography | If murmur or other cardiac signs; pulmonary stenosis is not a universal feature |
| Audiology and ophthalmology | Symptom-directed because hearing loss and cataract are occasional |
| EMG/repetitive nerve stimulation | Only with weakness or fatigability; evaluates possible LRP4-related CMS |
| Developmental assessment | If delay is suspected |

Abdominal ultrasound and periodic renal-function testing are specifically recommended by expert review. [79]

### 10.2 Genetic-testing strategy

1. **First-line:** sequence *LRP4* with deletion/duplication analysis when the phenotype is classic.
2. **Panel testing:** a limb-malformation/syndactyly panel including *LRP4*, *GREM1*, *FMN1*, *APC*, *HOXD13*, *GJA1*, *FGF16* and other phenotype-relevant genes is reasonable when the presentation is atypical.
3. **Trio WES:** preferred when there are multisystem abnormalities, uncertain clinical classification, negative panel testing, or prenatal disease. The 2024 report explicitly described exome sequencing as powerful and preferred for syndactyly-related phenotypes. [PMID:38013226] [47]
4. **WGS:** useful after negative WES/panel testing because it can identify noncoding splice variants, structural variants and rearrangements across *GREM1–FMN1*.
5. **CMA:** appropriate when intellectual disability, multiple congenital anomalies or a suspected *GREM1–FMN1* copy-number change is present.
6. **Karyotype/FISH:** low yield unless a cytogenetic rearrangement is suspected; not routine for classical disease.
7. **Mitochondrial and repeat-expansion testing:** not indicated.
8. **RNA analysis:** useful for suspected splice variants to demonstrate aberrant transcripts.
9. **Parental segregation testing:** essential for phasing, carrier confirmation and recurrence counseling.

The GTR listed 24 clinical tests for this condition at the time captured by the source. [77]

### 10.3 Prenatal and preimplantation diagnosis

* Detailed fetal ultrasound may detect severe oligosyndactyly, abnormal hands/feet, shortened forearms and bilateral renal agenesis, although syndactyly alone can be difficult to visualize.
* If familial variants are known, targeted chorionic-villus or amniotic-fluid testing provides definitive prenatal diagnosis.
* Preimplantation genetic testing for monogenic disease is technically feasible.
* Trio/family WES may diagnose a previously unresolved fetal-malformation phenotype.

### 10.4 Differential diagnosis

| Differential | Distinguishing considerations |
|---|---|
| Carpenter syndrome | Craniosynostosis, polysyndactyly and broader craniofacial abnormalities |
| Apert syndrome | Craniosynostosis with characteristic symmetrical “mitten” syndactyly; usually *FGFR2*, autosomal dominant |
| Acrocephalopolysyndactyly disorders | Craniosynostosis and polydactyly predominate |
| Greig cephalopolysyndactyly | Macrocephaly/hypertelorism and preaxial polydactyly; *GLI3* |
| HOXD13-related syndactyly/synpolydactyly | Usually dominant, characteristic central digital duplications, typically no renal agenesis |
| GREM1–FMN1 rearrangement syndrome | Can closely resemble CLSS; identify by CNV analysis |
| APC-associated limb malformation | May have a CLSS-like phenotype; assess personal/family polyposis history, although some reported limb cases lacked polyposis |
| VACTERL association | Limb and renal anomalies but requires broader association pattern |
| Thrombocytopenia-absent radius | Absent radii with thumbs present and thrombocytopenia |
| Sclerosteosis 2 | Also *LRP4*-related but characterized by progressive high bone mass rather than congenital CLSS limb pattern |

There are no universally adopted standalone clinical diagnostic criteria; diagnosis is clinical-radiographic and confirmed molecularly.

---

## 11. Outcome and prognosis

* **Survival:** No 5-year, 10-year or median-survival estimates exist. Survival is expected to be broadly normal in patients without bilateral renal agenesis or severe renal failure, but this has not been demonstrated in a longitudinal cohort.
* **Mortality:** Bilateral renal agenesis is the principal known lethal complication. Perinatal respiratory failure in null mice should not be automatically extrapolated to humans.
* **Morbidity:** Primarily chronic upper-limb functional impairment, restricted forearm rotation, altered gait/footwear needs, cosmetic burden and possible renal morbidity.
* **Renal prognosis:** Depends on nephron mass and whether a functioning contralateral kidney is present. A solitary or hypoplastic kidney requires lifelong monitoring.
* **Neuromuscular prognosis:** Unknown because CLSS-associated CMS has been documented only exceptionally.
* **Quality of life:** No disease-specific instrument or cohort estimate is available. Severe hand abnormalities can markedly affect independence; published reviews note poor hand function even after surgery. [24]
* **Prognostic factors:** extent of metacarpal/phalangeal disorganization, presence of usable thumb/digital rays, radioulnar synostosis, bilateral versus unilateral renal disease, baseline renal function, and—rarely—neuromuscular involvement.
* **Prognostic biomarkers:** none validated.

---

## 12. Treatment

There is no curative or disease-modifying therapy and no approved drug directed at LRP4/WNT signaling for CLSS.

| Intervention | Indication and expected outcome | Suggested NCIt concept |
|---|---|---|
| Multidisciplinary congenital-hand assessment | Define anatomy and realistic functional goals, ideally in infancy | Clinical evaluation |
| Syndactyly release/digital reconstruction | Create individualized functional rays, improve grasp or hygiene; results may be unsatisfactory when bones are severely fused/disorganized | **Surgical Procedure, C15329**; reconstructive surgery |
| Orthopedic surgery | Selected forearm, foot, hip or spinal abnormalities | Orthopedic surgery |
| Occupational therapy | Adaptive grasp, self-care, school/work equipment and postoperative rehabilitation | **Occupational Therapy, C15309** |
| Physical therapy | Mobility, range of motion, strength and gait | **Physical Therapy, C15311** |
| Orthoses/prosthetic or adaptive devices | Improve limb positioning, ambulation or daily function | Assistive device |
| Renal surveillance | Blood pressure, urinalysis, creatinine/eGFR and ultrasound follow-up | Disease surveillance |
| Nephrology management | Standard management of reduced renal function, hypertension, infection or obstruction | Supportive care |
| Dental treatment | Preventive dentistry, restorations, prosthodontics or orthodontics | Dental treatment |
| CMS-directed therapy | If physiologically confirmed, management by neuromuscular specialists; no CLSS-specific response rates exist | Pharmacologic therapy/supportive care |
| Genetic counseling | Recurrence calculation and reproductive options | **Genetic Counseling, C15241** |

Orphanet recommends reconstruction of an individualized digit but warns that syndactyly-release outcomes can be unsatisfactory. [76] Expert review recommends radiographic definition of anatomy and surgical consultation during the first year of life. [79]

### Experimental treatment and trials

No CLSS-specific gene therapy, CRISPR, RNA therapy, cell therapy, WNT-targeted drug, immunotherapy or registered interventional trial has established efficacy. Prenatal pathway manipulation would carry major off-target developmental risks and remains theoretical.

---

## 13. Prevention

| Prevention level | Applicable measure |
|---|---|
| Primary prevention | No lifestyle, vaccine, drug or exposure modification prevents a sporadic inherited case. Reproductive carrier testing and PGT-M can prevent an affected pregnancy in known carrier couples. |
| Secondary prevention | Early prenatal molecular diagnosis or fetal ultrasound; prompt neonatal renal imaging and radiographic characterization |
| Tertiary prevention | Early hand/orthopedic assessment, rehabilitation, renal surveillance, dental care and management of scoliosis or CMS to reduce complications |
| Cascade screening | Test adult relatives for the familial variant where reproductive information is desired |
| Population screening | Not justified because prevalence and carrier frequency are extremely low and not established |
| Newborn screening | Not included in biochemical newborn-screening programs; visible congenital findings usually trigger evaluation |
| Immunization/prophylaxis | No disease-specific vaccine or preventive medication |
| Public-health/environmental intervention | Not applicable because there is no demonstrated infectious or environmental cause |

Genetic counseling should explain the 25% recurrence risk for carrier couples, variable expressivity, options for prenatal diagnosis, PGT-M, donor gametes and adoption. [79]

---

## 14. Other species and naturally occurring disease

| Species | Taxonomy/model information | Natural phenotype and comparative relevance |
|---|---|---|
| Domestic cattle, *Bos taurus* | NCBI Taxon **9913**; bovine *LRP4* ortholog | Autosomal-recessive syndactyly or “mulefoot,” OMIA:000963-9913. Independent *LRP4* variants occur in Holstein, Angus, Simmental and Simmental–Charolais cattle. The principal phenotype is fused digits/uncloven hooves, generally less multisystemic than human CLSS. [123][130] |
| House mouse, *Mus musculus* | NCBI Taxon **10090**; *Lrp4* NCBI Gene **228357**, MGI:2442252 | Induced and spontaneous alleles cause fully penetrant polysyndactyly, dental abnormalities, growth impairment and variably renal agenesis; severe null alleles can cause neonatal lethality. [106][107] |
| Fruit fly, *Drosophila melanogaster* | NCBI Taxon **7227**; orthologous *Lrp4* | Regulates synaptic organization; useful for conserved synaptic biology but does not reproduce mammalian limb or renal morphogenesis. [74] |

Bovine disease is naturally occurring and economically relevant because fused hooves can impair locomotion and breeding value. It is not zoonotic, infectious or transmissible between species. The shared *LRP4* association demonstrates evolutionary conservation of distal-limb developmental function.

---

## 15. Model organisms

| Model | Type/genotype | Phenotype recapitulation | Applications and limitations |
|---|---|---|---|
| *Lrp4* null mouse | Targeted knockout replacing exon 1 with a stop/neomycin cassette | Polysyndactyly, delayed ureteric budding, unilateral/bilateral renal agenesis, tooth abnormalities and perinatal death | Strong model for limb/kidney causality; more severe and often polydactylous compared with human oligodactyly |
| Hypomorphic/spontaneous *Lrp4* mouse | Partial-function alleles | Viable mice with polysyndactyly, digit fusion and craniofacial/dental abnormalities | Useful for dosage and domain studies; exact human variants may behave differently |
| Domain-specific knock-in mouse | Extracellular/intracellular-domain alleles | Extracellular-domain disruption produces stronger limb phenotype than many intracellular-domain changes | Dissects structural requirements of LRP4 |
| Patient-derived myotubes | Human primary in-vitro model, p.Tyr607Cys | Reduced acetylcholine-receptor clustering and impaired ligand interactions | Direct human evidence for CMS mechanism; represents one variant/patient |
| HEK293T reporter model | Transfected wild-type or mutant LRP4, LRP6, WNT1 | Quantifies loss of WNT antagonism and defective membrane localization | Mechanistically tractable but not a developing limb or kidney |
| Bovine mulefoot | Naturally occurring large-animal model | Digital fusion due to recessive *LRP4* variants | Valuable comparative limb model; renal and craniofacial phenotypes usually differ from human CLSS |
| Chick limb-bud manipulation | Developmental experimental model, particularly GREM1 overexpression | Cenani–Lenz-like digit-reduction patterns | Useful for BMP/WNT spatial patterning; not an *LRP4*-specific whole-disease model |

The mouse model quantitatively reproduces renal-organogenesis failure: among 156 null animals, 73% had agenesis—51% bilateral and 22% unilateral. [109] MGI records targeted, spontaneous, ENU-induced and endonuclease-generated *Lrp4* alleles and notes polysyndactyly, renal agenesis, abnormal incisors, growth retardation and neonatal respiratory death. [106][107]

---

# Recent developments and evidence assessment

| Publication date | Development | Evidence type |
|---|---|---|
| **August 28, 2023** | Homozygous *LRP4* c.1820A>G, p.Tyr607Cys linked CLSS limb/renal abnormalities with congenital myasthenic syndrome; patient-myotube and ligand-binding assays supported impaired agrin–LRP4–MuSK signaling. PMID:37640745; DOI:10.1038/s41598-023-41008-5. [59] | Single human case plus in-vitro functional evidence |
| **November 27, 2023 / January 2024 issue** | Prenatal CLSS diagnosis with homozygous c.282C>A, p.Asn94Lys; expanded the variant spectrum and emphasized WES in fetal syndactyly. PMID:38013226; DOI:10.1002/mgg3.2319. [47][114] | Fetal case report and literature review |
| **2021** | New *LRP4* variants p.Asp99His and p.Arg545Trp showed reduced ability to inhibit WNT signaling. [40] | Human families plus reporter assay |
| **2019** | Review clarified the mechanistic and nosologic relationship among *LRP4*, *GREM1–FMN1* and *APC* Cenani–Lenz-like disorders. PMID:30569497. [136] | Expert review |
| **2010 landmark** | Recessive *LRP4* variants found in 12/14 families; renal anomalies recognized as common; impaired trafficking and WNT antagonism demonstrated. PMID:20381006; DOI:10.1016/j.ajhg.2010.03.004. [6] | Multihousehold human series plus functional assays |

## Overall evidence conclusion

The strongest disease model is that **biallelic germline loss of LRP4 cell-surface function dysregulates embryonic WNT/BMP signaling, disrupting limb and kidney morphogenesis**. Limb malformations are highly penetrant, while renal, facial, dental and neuromuscular findings show variable expression. Clinical care remains anatomy- and complication-directed, with genetic diagnosis, renal surveillance, reconstructive assessment, rehabilitation and reproductive counseling as the main current implementations. No disease-modifying therapy, validated biomarker, population-screening program or CLSS-specific natural-history registry outcome has yet been established.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 23 |
| On topic | 11 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:38013226` *(abstract only)*: "Exome sequencing revealed a novel biallelic c.282C>A variant in… *LRP4*… causing p.(Asn94Lys)."
  - closest text in source: "Exome sequencing revealed a novel biallelic c.282C⟩Avariant in low-density lipoprotein receptor-related protein 4 (LRP4; OMIM604270; NM_002334.4) causing p"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1155/2019/9652649` (2 mentions) - A Review of the Genetics and Pathogenesis of Syndactyly in Humans and Experimental Animals: A 3-Step Pathway of Pathogenesis
  - shared terms: syndactyly
- `PMC:PMC6766129` (1 mention) - A Review of the Genetics and Pathogenesis of Syndactyly in Humans and Experimental Animals: A 3-Step Pathway of Pathogenesis.
  - shared terms: syndactyly

Weighed against this report's own most characteristic terms: `lrp4`, `renal`, `clss`, `variant`, `limb`, `disease`, `syndactyly`, `agenesis`, `congenital`, `function`, `abnormalitie`, `developmental`, `kidney`, `phenotype`, `bilateral`, `functional`, `dental`, `established`, `severe`, `loss`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 69 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 16 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008931` (4 mentions) - the report calls it "MONDO"; MONDO calls it **Cenani-Lenz syndactyly syndrome**
- `DOID:0090015` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **Cenani-Lenz syndactyly syndrome**
- `HP:0000494` (1 mention) - the report calls it "Primarily dysmorphic feature"; HP calls it **Downslanted palpebral fissures**
- `CL:0002320` (1 mention) - the report calls it "Metanephric mesenchymal cell"; CL calls it **connective tissue cell**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001163` (obsolete Abnormality of the metacarpal bones) (1 mention) - replaced by `HP:0005916`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0090090` (1 mention) - the report calls it "Negative regulation of canonical WNT"; GO calls it **negative regulation of canonical Wnt signaling pathway**
- `GO:0095500` (1 mention) - the report calls it "Acetylcholine-receptor clustering"; GO calls it **acetylcholine receptor signaling pathway**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`, `MGI`.