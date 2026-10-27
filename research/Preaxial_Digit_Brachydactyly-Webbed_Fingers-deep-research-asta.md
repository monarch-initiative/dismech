---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-09-21T10:10:00.495627'
end_time: '2026-09-21T10:10:04.501523'
duration_seconds: 4.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PAX3 preaxial brachydactyly from EPHA4-PAX3 topological domain boundary
    deletions Lupianez 2015 PMID25959774
  mondo_id: MONDO:0859005
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    query_char_limit: 500
    paper_limit: 50
    snippet_limit: 20
    snippet_paper_limit: 50
    restrict_snippets_to_papers: false
    paper_fields: title,abstract,authors,year,url,venue,journal,tldr,publicationDate,citationCount,influentialCitationCount,externalIds
    publication_date_range: ''
    venues: ''
    inserted_before: ''
fell_back: true
requested_provider: claude_code
provider_attempts:
- provider: claude_code
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: asta
  succeeded: true
citation_count: 14
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 2
  off_topic: 2
  off_topic_references:
  - PMID:26340639
  - DOI:10.3390/genes6030790
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PAX3 preaxial brachydactyly from EPHA4-PAX3 topological domain boundary deletions Lupianez 2015 PMID25959774
- **MONDO ID:** MONDO:0859005 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PAX3 preaxial brachydactyly from EPHA4-PAX3 topological domain boundary deletions Lupianez 2015 PMID25959774** covering all of the
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

# Asta Literature Retrieval: Disease Characteristics Research Template Target Disease Disease Name: PAX3 preaxial brachydactyly from EPHA4-PAX3 to...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 14
- Snippets retrieved: 20

## Relevant Papers

### [1] Chromatin Conformation in Development and Disease
- Authors: Ilias Boltsis, F. Grosveld, G. Giraud, Petros Kolovos
- Year: 2021
- Venue: Frontiers in Cell and Developmental Biology
- URL: https://www.semanticscholar.org/paper/1b7f9b44ad0860b82d8159aa748d0502983cf68e
- DOI: 10.3389/fcell.2021.723859
- PMID: 34422840
- PMCID: 8371409
- Citations: 47
- Influential citations: 1
- Summary: New findings, which have linked chromatin conformation with development, differentiation and diseases and hypothesized on various models are discussed, while integrating all recent findings on how chromatin architecture affects gene expression during development, evolution and disease are integrated.
- Evidence snippets:
  - Snippet 1 (score: 1.025)
    > Brachydactyly Deletions in the EPHA4 locus that include a TAD border result in a fusion of the neighboring TADs, which attaches a cluster of limb-associated EPHA4 enhancers to the PAX3 gene and its concomitant mis-expression (Lupiáñez et al., 2015) Six TAD boundaries encompassing T-ALL related genes

### [2] In vivo dissection of a clustered-CTCF domain boundary reveals developmental principles of regulatory insulation
- Authors: C. Anania, R. D. Acemel, Johanna Jedamzick, Adriano Bolondi, Giulia Cova et al.
- Year: 2021
- Venue: Nature Genetics
- URL: https://www.semanticscholar.org/paper/db0d32f46dcb867d83aa0c6bc8e23ce16d9ccd21
- DOI: 10.1038/s41588-022-01117-9
- PMID: 35817979
- PMCID: 9279147
- Citations: 63
- Influential citations: 2
- Summary: Genetically dissecting the Epha4–Pax3 topological boundary in mice shows that divergent CTCF binding sites (CBSs) are not essential for insulation and that chromatin loops in nonconvergently oriented CBSs can be driven by a loop interference mechanism.
- Evidence snippets:
  - Snippet 1 (score: 0.966)
    > By studying a series of deletions in transgenic mice, we previously demonstrated that a 150 Kilobases (Kb) region, marked as a boundary region across multiple tissues and cell types, is sufficient to segregate the regulatory activities of the Epha4 and Pax3 TADs (Lupiáñez et al., 2015) (Supp. Fig. 1 and 2). The DelB background carries a deletion that removes a portion of the Epha4 TAD, including the gene itself, as well as the boundary region that separates this domain from the adjacent Pax3 TAD. This deletion results in the ectopic interaction between the Epha4 limb enhancers and the Pax3 gene, which causes the misexpression of Pax3 in developing limbs and leads to the shortening of index and thumb fingers (brachydactyly) in mice and also in human patients with equivalent deletions. In contrast, the DelBs background carries a similar deletion but not affecting the EP boundary region, which maintains the regulatory partition between the Epha4 and Pax3 TADs and confines the Epha4 limb-specific enhancers within their own regulatory domain (Fig. 1A, Supp. Fig. 1). Thereby, the genomic configuration of the DelBs background provides a simple, but informative, functional readout to investigate boundary function in vivo. By performing deletions on the genomic components of the EP boundary, we can quantify the consequences of boundary disruption on a single target gene that is reactive to ectopic enhancers and can induce developmental defects. This genomic setup allows us to estimate boundary function at multiple levels: inter-TAD chromatin interactions, gene misexpression and disease-related phenotypes.
    > To explore the genomic features of the EP boundary in vivo, we examined ChIP-seq datasets on developing limbs (Rodríguez-Carballo et al., 2017). This analysis revealed the presence of six clustered CBS at the EP boundary region (Fig. 1A, 1B; Supp Fig 2). CTCF motif analyses confirmed the divergent orientation of these sites, a typical signature of TAD boundaries, with four CBS in a reverse (R) and two in a forward orientation (F).
  - Snippet 2 (score: 0.937)
    > We previously reported that the misexpression of PAX3 during early limb development can lead to a severe shortening of index and thumb fingers (brachydactyly), as observed in human patients carrying large deletions at the EPHA4 locus and in their corresponding mouse models (DelB) (Lupiáñez et al., 2015). Therefore, our collection of mouse mutants provides a unique opportunity to study how boundary insulation strengths directly translate into developmental phenotypes.
    > To evaluate this aspect, we performed tetraploid aggregation experiments with several of our mutant mESC lines and obtained mutant fetuses at E17.5, a developmental stage where the limb defects are already observable (Lupiáñez et al., 2015). We performed alcian blue/alizarin red skeletal staining in mutant limbs and measured relative digit length as a proxy for the phenotype (Fig. 6A and B). First, we analyzed the ΔR1 mutants, which display a moderate Pax3 misexpression in the anterior region of the distal limb (Fig. 1F). A quantification of finger length ratios revealed that mutant limbs are indistinguishable from their corresponding controls. These results demonstrate that the detrimental effects of Pax3 misexpression can be partially buffered, resulting in the development of normal limbs. Next, we analyzed the phenotypic effects of the ΔR1+F2 mutant. In contrast to individual deletions, the combined deletion of R1 and F2 led to a moderate reduction of index digit length (Fig 6A and B; 6.3% compared to controls), consistent with the increased Pax3 misexpression (Fig. 2B). This phenotype demonstrates that weakened boundaries can be permissive to functional interactions between adjacent TADs, resulting in developmental gene expression patterns and associated phenotypes. It is worth noting that the brachydactyly phenotypes of ΔR1+F2 mutants occur despite an observable partition between the Epha4 and Pax3 TADs and across a boundary region that has relatively high boundary scores (Fig. 2C and 2D; boundary score=0.8).

### [3] Three‐dimensional genome structure and function
- Authors: H. Liu, Hsiang-Yu Tsai, Maoquan Yang, Guozhi Li, Q. Bian et al.
- Year: 2023
- Venue: MedComm
- URL: https://www.semanticscholar.org/paper/f183f137046324ad8ecff997086c3c74ebc05ce1
- DOI: 10.1002/mco2.326
- PMID: 37426677
- PMCID: 10329473
- Citations: 19
- Summary: Prospects were made for the research about 3D genome structure, function, and genetic intervention, and the roles in disease development, prevention, and treatment, which may offer some clues for precise diagnosis and treatment of related diseases.
- Evidence snippets:
  - Snippet 1 (score: 0.829)
    > Brachydac-tyly A heterozygous deletion of 1.75-1.9 Mb on 2q35 spanning the TAD boundaries of EphA4 and Pax3 resulted in TAD fusion. In this fused TAD, an enhancer originally regulating EphA4 interacts with the Pax3 promoter.
  - Snippet 2 (score: 0.739)
    > An example of chromosomal rearrangement that impacts gene expression is the Wnt6/Ihh/Epha4/Pax3 locus located on chromosome 2q35-36. A heterozygous deletion of 1.75-1.9 Mb in the 2q35 region results in short-fingered malformation in humans and mice. This deletion disrupts the TAD boundary between Epha4 and Pax3, leading to TAD fusion and producing an 800 kb fused TAD. 258 ithin this fused TAD, the enhancer that initially regulated Epha4 interacts with the Pax3 promoter, causing an increased expression level of Pax3 and a decreased expression level of Epha4, ultimately leading to the development of short-fingered malformations.
    > Not all deletions across TAD boundaries lead to TAD fusion. In the mouse genome, adjacent motifs Sox9-Kcnj show that deleting only the CTCF locus at the boundary does not result in TAD fusion. TAD fusion occurs only after deleting all four CTCF loci within the TADs. Only deleting all four CTCF loci within the TADs leads to TAD fusion, but it does not significantly affect gene expression. 290 The limited impact on gene expression resulting from small deletions may be due to the redundancy of CTCF sites in the TADs. This redundancy mechanism helps maintain the structural and functional stability of TADs and ensures precise gene expression.

### [4] Disruptions of Topological Chromatin Domains Cause Pathogenic Rewiring of Gene-Enhancer Interactions
- Authors: D. Lupiáñez, K. Kraft, V. Heinrich, P. Krawitz, F. Brancati et al.
- Year: 2015
- Venue: Cell
- URL: https://www.semanticscholar.org/paper/183d2e4d4d1dbe2905f336b726a8a6be9dc21090
- DOI: 10.1016/j.cell.2015.04.004
- PMID: 25959774
- PMCID: 4791538
- Citations: 1986
- Influential citations: 63
- Summary: The results demonstrate the functional importance of TADs for orchestrating gene expression via genome architecture and indicate criteria for predicting the pathogenicity of human structural variants, particularly in non-coding regions of the human genome.
- Evidence snippets:
  - Snippet 1 (score: 0.820)
    > We experimentally challenged the assumption that TAD boundary elements are functional and relevant for disease pathogenesis by creating deletions that leave the proposed boundary regions on either side of the Epha4 TAD intact. Both regions contained a cluster of binding sites for CTCF, a factor involved in boundary formation (Dixon et al., 2012;Van Bortle et al., 2014). We engineered additional variants of the Dbf as well as the brachydactyly-associated rearrangements, this time leaving the predicted boundary regions undeleted. No phenotypes and no misexpression of either Ihh or Pax3 were observed. Furthermore, 4C-seq experiments in these mice showed decreased frequency of interaction of the target genes Pax3 and Ihh with the Epha4 domain. Thus, leaving the proposed boundary regions intact diminishes all molecular phenotypes and averts morphological aberrations by preventing ectopic interactions.
    > Distance between regulatory elements and their target genes may be another determining factor. At the HoxD locus, for example, duplications within the TAD that result in an increase in the distance between promoter and enhancers were shown to result in an impairment of activation (Montavon et al., 2012). While we cannot rule out that distance effects contribute to the attenuation of molecular phenotypes, the difference between the deletion sizes is 100 kb for the Dbf/Dbf S alleles and 200 kb for the DelB/DelB S alleles, corresponding to 17% and 12% of the total deletion size, respectively. It appears unlikely that these minor differences in distance alone are sufficient to explain the reversion of molecular phenotypes to near-wild-type levels, given that similar differences in deletion size of 200 kb are present across the brachydactyly families (B1, B2, and B3) without apparent effect on the phenotype.
  - Snippet 2 (score: 0.807)
    > Disruptions of TAD Structure at the EPHA4 Locus Are Associated with Limb Phenotypes The EPHA4 gene resides within a large gene desert flanked by a gene-dense region on the centromeric side and the PAX3 gene on the telomeric side. Hi-C data show that the region is organized into three adjacent TADs, the largest encompassing EPHA4 ( Figure 1A) (Dixon et al., 2012). Studying the genetic causes of rare limb malformations, we identified a series of structural variants at the EPHA4 locus that potentially interfere with the integrity of this region. In mice, Epha4 is expressed during limb development and required for normal innervation of the limb, but inactivation of Epha4 does not cause changes in the limb skeleton (Helmbacher et al., 2000).
    > First, we investigated a dominantly inherited novel type of brachydactyly in three unrelated families, characterized by short digits predominantly on the preaxial (radial) side resulting in stub thumbs, short index fingers and a cutaneous web between the first and second fingers ( Figure 1B; Figure S1). High-resolution array comparative genome hybridization (CGH) revealed heterozygous deletions of 1.75-1.9 Mb on chromosome 2q35-36 in all three affected families. All three deletions include the EPHA4 gene along with a large portion of its surrounding TAD and extend into the non-coding part of the adjacent PAX3 TAD, thereby removing the predicted boundary between the EPHA4 and PAX3 TADs.
    > Second, we studied the molecular cause of F-syndrome, a limb malformation syndrome characterized by severe and complex syndactyly, often involving the first and second fingers, and polydactyly of the feet ( Figure 1C) (Grosse et al., 1969). F-syndrome had previously been mapped to this chromosomal region (2q36), but its genetic cause remained unknown (Camera et al., 1995;Thiele et al., 2004). We used whole-exome sequencing to detect mutations in genes located in the linkage interval but were not able to identify any potentially pathogenic changes. To search for non-coding mutations and structural variations,
  - Snippet 3 (score: 0.771)
    > deletion (DelB s ) excluding the boundary region and CTCF cluster at the telomeric side of the Epha4 TAD (red octagon) was generated and compared with the brachydactyly-like deletion (DelB, including the CTCF cluster). The log2 ratio of the 4C-seq signal of DelB/DelB S shows increased interaction with the Epha4 TAD in the DelB deletion when compared with DelB s deletion (red box). Pax3 (right) shows normal expression of DelB s /+ deletion mice, in contrast to Pax3 misexpression in DelB/+ mice (white arrow). (C) A deletion (Dbf S ) excluding the boundary region and CTCF cluster at the centromeric side of the Epha4 TAD (red octagon) was generated and compared with the doublefoot deletion (Dbf, including the CTCF cluster). The log2 ratio of the 4C-seq signal of Dbf/Dbf S shows increased interaction with the Epha4 TAD in the Dbf deletion when compared with Dbf S deletion (red box). Ihh (right) shows an absence of limb expression in Dbf s /+ deletion mice, in contrast to Ihh misexpression in Dbf/+ deletion mice (white arrow). See also Figure S7. may be a preference toward genes that are poised to get activated in this tissue.
  - Snippet 4 (score: 0.770)
    > The general nature of the structural variations and the resemblance of phenotypes resulting from inversion and duplication (F-syndrome) or duplication and deletion (polydactyly/Dbf) raise the possibility that these phenotypes are caused by convergent alterations in gene regulation. In the case of Dbf mice, ectopic expression of Ihh in the embryonic limb was previously described (Babbs et al., 2008). To examine the new CRISPR-engineered lines for aberrant expression, we performed RNA-seq experiments in E11.5 limbs of wild-type, DelB/+ (brachydactyly-like deletion), InvF/InvF (F-syndromelike inversion), and Dbf/+ (polydactyly) embryos. We analyzed the chromosomal region around the Wnt6/Ihh/Epha4/Pax3 locus (chromosome 1: 73000000-79000000, mm9), for altered levels of gene expression related to the corresponding structural variation. We detected a significant upregulation of Pax3 in DelB/+ limbs, of Wnt6 in InvF/InvF limbs, and of Ihh in the Dbf/+ limbs, whereas all other surrounding genes were unaltered or showed only marginal increases in expression levels ( Figure S3). As expected, Epha4, which is contained in the brachydactyly (DelB) deletion, and all the genes located within the Dbf deletion were downregulated. On the basis of these results, we analyzed the expression patterns of Pax3, Wnt6, and Ihh in the respective mouse mutants by in situ hybridization at E11.5 and compared them with the wild-type Epha4 expression pattern.
    > Epha4 is expressed in a distinct pattern in the developing limb, mainly in the distal mesoderm with predominance to the anterior side ( Figure 3A, right). At the same developmental stage, Pax3 is also expressed in the limb bud, but restricted to migrating muscle cells, evident as faint staining in the proximal limb, and absent from the developing hand plate (
  - Snippet 5 (score: 0.731)
    > of hedgehog proteins can induce polydactyly via the disruption of the anterior-posterior GLI3 gradient (Lettice et al., 2002). While the mechanisms by which ectopic expression of Pax3 may affect skeletal morphology remain to be established, the observed misexpression domains in combination with the morphogenetic potential of Wnt6 and hedgehog proteins offer a plausible molecular explanation for at least two of the human phenotypes observed.
    > Our 4C-seq data using the Epha4 enhancers as a viewpoint ( Figure S6) also show that the regions of ectopic interaction cover many other genes besides the identified targets Pax3, Ihh, and Wnt6. Nevertheless, expression analysis by RNA-seq showed no substantial upregulation of these genes, indicating that either enhancer-promoter distance or other unknown factors contribute to the receptiveness of a promotor to respond to the enhancer. In a Drosophila in vitro system, housekeeping and developmental promoters can respond to different classes of enhancers (Zabidi et al., 2015). It is possible that similar intrinsic specificities help to guide enhancer-promotor in vertebrate genomes. Here, the activated genes are all developmental genes expressed during limb development, indicating that there Figure 6. Boundary Elements at Both Sides of the Epha4 TAD Prevent Ectopic Expression of Neighboring Genes (A) CTCF ChIP-seq track in E14.5 mouse limbs (ENCODE/LICR). Red boxes and octagons mark clusters of CTCF peaks located at the boundary of the Epha4 TAD. The grey box indicates Epha4 TAD. 4C-seq profiles were generated from distal limb buds at E11.5. All data were obtained from heterozygous animals. Aberrant interactions are indicated by red boxes. Pink scissors indicate CRISPR/Cas-induced breakpoints in each deletion. (B) A deletion (DelB s ) excluding the boundary region and CTCF cluster at the telomeric side of the Epha4 TAD (red octagon) was generated and compared with the brachydactyly-like deletion (DelB, including the CTCF cluster).

### [5] Advances in Functional Genomics for Human Health
- Authors: Patrick R. Gonzales
- Year: 2026
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/238a49c334017a976aee6a8b6d7f64edac94c95f
- DOI: 10.3390/genes17070763
- PMID: 42510803
- PMCID: 13410287
- Summary: Prior and current efforts to leverage functional genomics within the intergenic regions for human health within the intergenic regions for human health are reviewed.
- Evidence snippets:
  - Snippet 1 (score: 0.799)
    > Further work from the Mundlos group by Lupiáñez and colleagues confirmed via Hi-C data that human and mouse cells shared a highly similar TAD structure and that mice could serve as an in vivo model system for genetic diseases involving structural and copynumber variants [24]. The group used CRISPR/Cas to generate structural variants within a TAD encompassing the mouse gene Epha4, and flanked by TADs containing Wnt6, Ihh, and Pax3, which is syntenic with the human TADs containing WNT6/IHH/EPHA4/PAX3. Multiple CRISPR/Cas constructs were created in this genomic region to recapitulate the https://doi.org/10.3390/genes17070763 human genetic diseases brachydactyly, F-syndrome, and polydactyly, with disruption of TAD boundaries leading to ectopic interactions between Pax3, Wnt6, and Ihh, respectively, with the enhancers within the Epha4 TAD. Similar results were seen in human embryonic stem cells from patients with the aforementioned diseases. To determine the native sites of action of the enhancers within the Epha4 TAD, they used e11.5 mice to screen for Epha4 enhancers selected from ChIP-Seq data that had activity in limb buds with a lacZ reporter assay. This work was shown to provide a framework for the interpretation of structural variants in human genetic disease through the examination of TADs and TAD boundaries. Similar work by Rajderkar and colleagues in the Pennacchio group confirmed the necessity of intact TAD boundaries for normal genome function via intensive targeted deletion of CTCF-binding regions at these boundaries [25]. In addition to functional genomics research in embryonic mice, some groups utilized zebrafish (Danio rerio) to investigate the function of enhancer sequences in an alternative vertebrate model. Zebrafish diverged from the mammalian lineage ~420 million years ago, have ~70% conservation with human protein-coding genes, and are easy to genetically manipulate and propagate [26,27].

### [6] Disease-associated genetic variants in the regulatory regions of human genes: mechanisms of action on transcription and genomic resources for dissecting these mechanisms
- Authors: E. Ignatieva, E. Matrosova
- Year: 2021
- Venue: Vavilov Journal of Genetics and Breeding
- URL: https://www.semanticscholar.org/paper/34016996eefcea642e5211d397028c402b608edb
- DOI: 10.18699/VJ21.003
- PMID: 34541447
- PMCID: 8408020
- Citations: 8
- Summary: The present review focuses on the molecular genetic mechanisms by which pathogenic genetic variants affect gene expression, and attention is concentrated on the transcriptional level of regulation as an initial step in the expression of any gene.
- Evidence snippets:
  - Snippet 1 (score: 0.782)
    > Analysis of these data using the original 3DPredictor program (Belokopytova et al., 2020), developed on the basis of machine learning algorithms, allows to predict the frequencies of physical contacts between promoters and enhancers in the 3D genome structure with an accuracy that exceeds the accuracy of other known prediction methods.
    > The 3DPredictor was used to analyze the 3D genome structure in homozygous DelB/DelB mice that have a deletion of the 1.5 Mb genomic region containing Epha4. This deletion is accompanied by the appearance of additional contacts between Pax3 gene and Epha4 enhancer region, altering Pax3 expression and leading to brachydactyly. Mice with the DelB/ DelB genotype are a genetic model of human pathology accompanied by limb malformations (Lupiáñez et al., 2015). Testing 3DPredictor on this model has demonstrated the high efficiency of the program: in homozygous DelB/DelB mice, ectopic contacts between the Pax3 gene and Epha4 enhan-cers cluster were predicted (Belokopytova et al., 2020), and these predictions were in good agreement with the experimental data.

### [7] Chromatin Insulators and Topological Domains: Adding New Dimensions to 3D Genome Architecture
- Authors: Navneet Matharu, S. H. Ahanger
- Year: 2015
- Venue: Genes
- URL: https://www.semanticscholar.org/paper/100bc95489221fca74e85e85b2f89af3c2b573d8
- DOI: 10.3390/genes6030790
- PMID: 26340639
- PMCID: 4584330
- Citations: 20
- Influential citations: 1
- Summary: The classical view and the renewed understanding of insulators as global genome organizers are discussed and the plasticity of chromatin structure and its re-organization during pluripotency and differentiation and in situations of cellular stress are discussed.
- Evidence snippets:
  - Snippet 1 (score: 0.780)
    > A recent study demonstrated how structural anomalies in the genome could disrupt TAD organization and result in at least three related human genetic disorders [56]. Three different types of limb malformations, namely brachydactyly (short digits), F-syndrome syndactyly (fused axial digits), and polysyndactyly (duplicated and fused digits), identified in three different families, were investigated. By performing comparative genomic hybridization (CGH), the above mentioned malformations were shown to be associated with genomic aberrations in the q arm of chromosome 2, having four important coding genes, WNT6, IHH, EPHA4, and PAX3. Investigating the TAD organization of the locus revealed that it is structurally divided into three independent TADs, PAX3-TAD, EPHA4-TAD, and WNT6/IHH-TAD (Figure 2a). The brachydactyly family has a deletion that encompasses portions of EPHA4-TAD as well as the boundary separating it from PAX3-TAD (Figure 2b). The F-syndrome family has inversions or duplication having breakpoints within WNT6/IHH TAD and EPHA4-TAD, encompassing the TAD boundary between these two (Figure 2c). The polysyndactyly family has duplications and deletions within WNT6/IHH TAD, also disturbing its TAD boundary (Figure 2d). All these chromosomal aberrations were re-engineered in a mouse model using the CRSIPR/Cas9 system as well as in hESC (human embryonic stem cells) to map genomic interactions using 4C. The gene expression profile of the locus revealed non-cognate association of the gene promoter with the enhancers. These severe limb malformations clearly resulted from perturbations in the TAD structure and its boundaries, which relocate enhancers with gene promoters. These TAD boundaries are associated with CTCF-loop domains in mouse limbs. This study provides strong evidence that disruption of TADs and TAD boundaries could cause severe developmental disorders in humans. Deciphering the structural basis of X-inactivation in Caenorhabditis elegans also revealed the importance of TAD boundaries.

### [8] Enhancers and chromatin structures: regulatory hubs in gene expression and diseases
- Authors: Zhen-Hua Hu, Wee-Wei Tee
- Year: 2017
- Venue: Bioscience Reports
- URL: https://www.semanticscholar.org/paper/0904a1b89195c3ab266af9411c1654c7e3b5ee88
- DOI: 10.1042/BSR20160183
- PMID: 28351896
- PMCID: 5408663
- Citations: 64
- Summary: It is emphasized that the enhancer–promoter interaction landscape provides a critical context to understand the aetiologies and mechanisms behind numerous complex human diseases and provides new avenues for effective transcription-based interventions.
- Evidence snippets:
  - Snippet 1 (score: 0.778)
    > that by limiting enhancer access to a small but privileged group of pioneer TFs, tighter control on tissue-specific gene expression may be achieved [52]. An extra TAD, due to the genomic duplication of the IHH locus and its associated TAD border (blue), leads to polydactyly. In contrast, brachydactyly is caused by a genomic deletion across the TAD border separating the EPHA4 and PAX3 loci (red and green respectively), resulting in the dysregulation of PAX3 by an ectopic EPHA4 enhancer. Finally, a genomic inversion involving IHH locus (blue) and its neighbouring TAD (red) exposes IHH to toxic regulation by an EPHA4 enhancer, leading to F-syndrome.

### [9] Chromatin Landscape During Skeletal Muscle Differentiation
- Authors: O. Hernández-Hernández, Rodolfo Daniel Ávila-Avilés, J. M. Hernández-Hernández
- Year: 2020
- Venue: Frontiers in Genetics
- URL: https://www.semanticscholar.org/paper/4411d78b522948be357b0f55cacd7bca92b19078
- DOI: 10.3389/fgene.2020.578712
- PMID: 33193700
- PMCID: 7530293
- Citations: 25
- Summary: This review will focus on the epigenetic mechanisms modulating muscle gene expression and on the incipient work that addresses three-dimensional genome architecture and its influence in cell fate determination and differentiation to achieve skeletal myogenesis.
- Evidence snippets:
  - Snippet 1 (score: 0.774)
    > Chromosomal translocations causing gene fusions between FKHR (Foxo1) and Pax3 or Pax7 are characteristic of alveolar rhabdomyosarcoma (ARMS), a pediatric soft tissue cancer derived from the muscle lineage (Douglass et al., 1987). The translocation events fuse the transactivation domain of FHKR to the DNA binding domain of Pax3 or Pax7, leading to increased transcription from Pax3 or Pax7 response elements (Galili et al., 1993;Bennicelli et al., 1996;Barr, 2001). These chimeric proteins are expressed at high levels in ARMS tumors. Histologically, the tumors contain collections of poorly differentiated tissue, and weak evidence of muscle differentiation as marked by scant MyoD and desmin staining. Studies on the transcriptional behavior of Pax3-FKHR and Pax7-FKHR suggest that the chromosomal translocations exaggerate the normal function of Pax3 and Pax7 in myogenic progenitor cells, leading to dysregulation of growth, apoptosis, differentiation, and motility (Galili et al., 1993;Bennicelli et al., 1996;Barr, 2001).
    > The relevance of genomic translocations and rearrangements affecting how TADs organize is that they also alter networks of gene regulation relevant for the correct execution of many developmental programs (Li et al., 2018). In addition to its implication in Rhabdomyosarcoma, misregulation of Pax3 is also related with limb malformations. This occurs when deletions of complete parts of TADs and their telomeric boundaries promotes interactions between the enhancer element of the otherwise repressed gene Epha4, with Pax3. The resulting effect of Pax3 over-expression is a brachydactyly phenotype in mutant mice models (Lupiáñez et al., 2015). In the muscular context, the fusion of Pax3 and FKHR genes associated with ARMS, promotes interaction of their regulatory elements and also generates a new TAD (Vicente-García et al., 2017).

### [10] Functional categorization of gene regulatory variants that cause Mendelian conditions
- Authors: Y. H. Hank Cheng, Stephanie C. Bohaczuk, Andrew B. Stergachis
- Year: 2024
- Venue: Human Genetics
- URL: https://www.semanticscholar.org/paper/48992ba728423b349161a24f412f2779c187c5f4
- DOI: 10.1007/s00439-023-02639-w
- PMID: 38436667
- PMCID: 11078748
- Citations: 9
- Influential citations: 1
- Summary: It is identified that non-coding gene regulatory variants can be split into three distinct categories by functional impact, and functional classifications aim to provide a unified terminology for categorizing the functional impact of non-coding variants that disrupt gene regulatory patterns in Mendelian conditions.
- Evidence snippets:
  - Snippet 1 (score: 0.773)
    > GOE variants cause ectopic spatial and/or temporal expression patterns and represent a disease mechanism that is largely unique to regulatory variants (Table 4). Notably, some GOE variants can mimic Mendelian conditions caused by duplications of the target gene. For example, autosomal-dominant adult-onset demyelinating leukodystrophy (ADLD) is caused by overexpression of LMNB1 protein usually attributed to duplication of the LMNB1 gene. However, an ADLD family was discovered to have a deletion that begins 66 kb upstream of the LMNB1 promoter. This deletion encompasses a TAD boundary and results in overexpression of LMNB1 protein via a mechanism termed 'enhancer adoption'. Specifically, a strong enhancer that typically does not regulate LMNB1 is now brought into the same TAD as the LMNB1 promoter, resulting in LMNB1 overexpression analogous to that seen with LMNB1 duplication (Giorgio et al. 2014).
    > Enhancer adoption is a common mechanism through which structural variants can cause regulatory element GOE (Fig. 1D). For example, structural variants within the WNT6/IHH/EPHA4/PAX3 locus can cause distinct phenotypes depending on where a strong cluster of limb enhancers for EPHA4 is situated relative to the WNT6, IHH, or PAX3 genes. Specifically, deletion of a TAD boundary between EPHA4 and PAX3 results in PAX3 adopting this cluster of limb enhancers, resulting in ectopic PAX3 expression and brachydactyly. In contrast, inversions or duplications involving IHH and the TAD boundary between IHH and EPHA4 result in WNT6 adopting this cluster of limb enhancers, resulting in ectopic WNT6 expression and F-syndrome (Lupiáñez et al. 2015).
    > SNVs within distal regulatory elements can also cause GOE. For example, the zone of polarizing activity regulatory sequence (ZRS), located in intron 5 of the LMBR1 gene, regulates SHH.

### [11] Orphan CpG islands amplify poised enhancer regulatory activity and determine target gene responsiveness
- Authors: Tomás Pachano, Víctor Sánchez-Gaya, Thais Ealo, María Mariner-Faulí, Tore Bleckwehl et al.
- Year: 2021
- Venue: Nature genetics
- URL: https://www.semanticscholar.org/paper/5be7c357a685a6b0cdf1764f385d1611410a5379
- DOI: 10.1038/s41588-021-00888-x
- PMID: 34183853
- PMCID: 7611182
- Citations: 86
- Influential citations: 3
- Summary: Genetic manipulation of poised enhancers (PEs) shows that orphan CpG islands promote physical and functional communication between PEs and distally located developmental genes, particularly those with large CGI clusters in their promoters.
- Evidence snippets:
  - Snippet 1 (score: 0.761)
    > for the hs1507 element is shown in the middle 67 . The deletion includes EPHA4, a gene highly expressed in the developing limb, and the TAD boundary separating the EPHA4 and PAX3 TADs. As a result, enhancers that control EPHA4 expression in the limb establish ectopic interactions with PAX3 (i.e. enhancer adoption) and strongly induce its expression in the limb. PAX3 promoter contains a large CGI cluster and is marked with H3K27me3 in ESCs, while one of the major EPHA4 enhancers (hs1507) is associated with an oCGI and is marked with H3K27me3 in ESCs. The high responsiveness of PAX3 to the EPHA4 enhancers is in agreement with our findings.

### [12] EPHA4 haploinsufficiency is responsible for the short stature of a patient with 2q35-q36.2 deletion and Waardenburg syndrome
- Authors: Chuan Li, Rong-Yu Chen, Xin Fan, Jingsi Luo, Jiale Qian et al.
- Year: 2015
- Venue: BMC Medical Genetics
- URL: https://www.semanticscholar.org/paper/49ca9c023370c9f933a4c24186cc264b9f0e37ff
- DOI: 10.1186/s12881-015-0165-2
- PMID: 25928000
- PMCID: 4432946
- Citations: 8
- Summary: Examining overlapping deletions in patients led to the conclusion that EPHA4 is a novel short stature gene and the finding is supported by the splotch-retarded and epha4 knockout mouse models which both showed growth retardation.
- Evidence snippets:
  - Snippet 1 (score: 0.753)
    > He showed a 9.2 cm/year growth rate and an improvement of 1 SD of height after one year treatment (Figure 2).
    > CMA test of patient's DNA using illumina Human SNP cyto-12 array revealed a 4.46 Mb de novo deletion at 2q35-q36.2 (chr2:221,234,146-225,697,363) (hg19, Figure 3). The deletion involved the whole PAX3 gene which is responsible for the Waardenburg syndrome phenotype and neighboring genes including EPHA4.
    > We evaluated previously published cases of overlapping deletions with our case's (Table 2 and Figure 4). We noticed that two thirds of deletion cases reported short stature or growth retardation as one of the phenotypic features when EPHA4 gene was involved in the deletions. The remaining cases did not provide height information. The animal model supported the notion that the EPHA4 deletion is responsible for short stature. The Sp r mutant was created by X-ray mutagenesis and characterized by a cytogenetically detectable deletion of band C4 on mouse chromosome 1. Heterozygous mice displayed   white spotting of the belly, tail and feet, equivalent pigmentary features of WS. They also had persistent growth retardation throughout their development [10]. The deletion is approximately syntenic to human chr2:218,449,525-232,459,056 region, both Pax3 and Epha4 were involved in the deletion. The other Splotch mutants caused by missense mutation (Sp d ) [11] or splicing mutation (Sp) [12] in Pax3 gene do not exhibit growth retardation, suggesting genes adjacent to Pax3 are responsible for the growth retardation phenotype. The most important evidence came from the recent epha4 knockout mouse model. Both heterozygous and homozygous epha4 knockout mice showed significant postnatal growth retardation in a dose dependent manner [13].

### [13] Deletions, Inversions, Duplications: Engineering of Structural Variants using CRISPR/Cas in Mice.
- Authors: K. Kraft, Sinje Geuer, Anja J. Will, Wing-Lee Chan, C. Paliou et al.
- Year: 2015
- Venue: Cell reports
- URL: https://www.semanticscholar.org/paper/27e0cd9ac91d0d1a4a74e3ed622a6bd69b6a74c1
- DOI: 10.1016/j.celrep.2015.01.016
- PMID: 25660031
- Citations: 205
- Influential citations: 4
- Summary: The use of CRISPR/Cas is presented for the fast (10 weeks) and efficient generation of SVs in mice and permits rapid in vivo modeling of genomic rearrangements.
- Evidence snippets:
  - Snippet 1 (score: 0.731)
    > It is likely that the truncated protein exerts a dominant-negative effect, thereby leading to the observed abnormalities of bone formation.
    > A 1.5 Mb Deletion of a Gene Desert Encompassing Epha4 Results in Hindlimb Hopping Gait Large gene deserts are thought to harbor regulatory elements and often surround developmentally active genes. We aimed at using the here-described method to challenge the integrity of such a locus. At the Epha4/Pax3 extended locus, two gene deserts centromeric and telomeric to Epha4 might regulate either one or both genes. Epha4 has been shown to control neuronal guidance in hindlimbs. Pax3 is a transcription factor with important function in the migration of muscle progenitors in the limbs and neural crest migration. Mice with mutations in Pax3 show pigmentation defects, early lethality due to heart defects, spina bifida, and exencephaly. We induced a deletion extending 1 Mb centromeric and 350 kb telomeric to the Epha4 transcription unit (Figure 4A). Heterozygous clones were used to produce mice with a 1.5 Mb deletion, which were subsequently bred to homozygosity. We observed a neurological phenotype in these animals, consisting of a hopping gait, as previously described for Epha4 loss of function (Figure 4B; Movie S1) (Dottori et al., 1998). Other abnormalities were not observed in these mice. In particular, we did not detect any of the Pax3-associated phenotypes such as pigmentation defects and abnormalities of the spine or the brain. Furthermore, in situ hybridization of Pax3 in deletion embryos revealed a normal pattern of expression (data not shown). Our finding that the 1.5 Mb deletion results in a full recapitulation of the Epha4 knockout without additional abnormalities indicates that the region does not contain elements essential for Pax3 regulation.

### [14] EPHA4 signaling dysregulation links abnormal locomotion and the development of idiopathic scoliosis
- Authors: Lianlei Wang, Xinyu Yang, Sen Zhao, Pengfei Zheng, Wen Wen et al.
- Year: 2025
- Venue: eLife
- URL: https://www.semanticscholar.org/paper/aa812609ba34e5d1efb93528fd1a597e873f4592
- DOI: 10.7554/eLife.95324
- PMID: 40662934
- PMCID: 12263152
- Citations: 3
- Summary: This study reanalyzed the loci associated with IS and identified variants in the EPHA4 gene as compelling candidates for IS, providing compelling evidence that neural patterning impairments and disruptions in CPGs may underlie the pathogenesis of IS.
- Evidence snippets:
  - Snippet 1 (score: 0.705)
    > The deletion included the entire PAX3 gene, which was responsible for the Waardenburg syndrome phenotype, and 36 neighboring genes, including EPHA4 (Figure 1K). As scoliosis is not typically associated with Waardenburg syndrome caused solely by PAX3 pathogenic variants (Tassabehji et al., 1993), we hypothesize that the deletion of EPHA4 may be responsible for the IS phenotype in this patient.
    > Notably, the GWAS signal which we mapped to EPHA4 (rs13398147) (Zhu et al., 2015) represents a significant eQTL in esophagus and colon tissues, with the T allele associated with decreased expression of EPHA4. In our East Asian GWAS cohort of 6449 adolescent IS patients and 158,068 controls, we identified another two eQTLs in EPHA4 associated with decreased expression of EPHA4 in brain tissue (Supplementary file 3). In the same GWAS cohort, common SNPs in EPHA4, after aggregation, also showed significant enrichment (p=0.023) in IS patients vs controls. Taken together, the convergence between rare and common variants of EPHA4 that lead to LoF or hypomorphic effects highlights the pivotal role of EPHA4 in the pathogenesis of IS.

## Notes

- This provider combines `search_papers_by_relevance` with `snippet_search`.
- No synthesis or second-stage model call is performed.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 28 |
| On topic | 2 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:26340639` (1 mention) - Chromatin Insulators and Topological Domains: Adding New Dimensions to 3D Genome Architecture.
  - shared terms: gene
- `DOI:10.3390/genes6030790` (1 mention) - Chromatin Insulators and Topological Domains: Adding New Dimensions to 3D Genome Architecture
  - shared terms: gene

Weighed against this report's own most characteristic terms: `pax3`, `epha4`, `gene`, `deletion`, `snippet`, `score`, `year`, `expression`, `url`, `venue`, `enhancer`, `tad`, `limb`, `genetic`, `brachydactyly`, `human`, `mice`, `tads`, `regulatory`, `region`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

No ontology term identifiers were found in this report.
