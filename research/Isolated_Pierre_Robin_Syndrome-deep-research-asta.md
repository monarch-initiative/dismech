---
provider: asta
model: Asta Scientific Corpus Retrieval
cached: false
start_time: '2026-09-21T10:07:49.138403'
end_time: '2026-09-21T10:07:54.003612'
duration_seconds: 4.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Isolated Pierre Robin Syndrome
  mondo_id: MONDO:0009869
  category: Developmental
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
citation_count: 18
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 28
  on_topic: 11
  off_topic: 2
  off_topic_references:
  - DOI:10.11603/24116-4944.2017.2.7801
  - DOI:10.1097/MD.0000000000036090
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
- **Disease Name:** Isolated Pierre Robin Syndrome
- **MONDO ID:** MONDO:0009869 (if available)
- **Category:** Developmental

## Research Objectives

Please provide a comprehensive research report on **Isolated Pierre Robin Syndrome** covering all of the
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

# Asta Literature Retrieval: Disease Characteristics Research Template Target Disease Disease Name: Isolated Pierre Robin Syndrome MONDO ID: MONDO...

This report is retrieval-only and is generated directly from Asta results.

- Papers retrieved: 18
- Snippets retrieved: 20

## Relevant Papers

### [1] Early communication intervention with young children with Pierre Robin sequence.
- Authors: Lisl Fair, Brenda Louw
- Year: 1998
- Venue: The South African journal of communication disorders = Die Suid-Afrikaanse tydskrif vir Kommunikasieafwykings
- URL: https://www.semanticscholar.org/paper/6c0e9efeb0bd67cc9b97712a02732877fec6b2eb
- DOI: 10.4102/SAJCD.V45I1.718
- PMID: 10472176
- Citations: 6
- Summary: The results indicated that regular early communication intervention sessions over an extended period of time produced positive results, especially for expressive language abilities, and hearing abilities and speech production skills of young children with Pierre Robin sequence should be followed closely duringEarly communication intervention.
- Evidence snippets:
  - Snippet 1 (score: 0.701)
    > The speech-and language development of children with isolated Pierre Robin sequence was found to be impaired and the speech-and language development ofthose children with Pierre Robin sequence and an additional syndrome was found to be even more impaired and delayed than those with isolated Pierre Robin sequence. Since the study conducted by Pashayan & Lewis (1984), limited research was reported on the communication development of young children with Pierre Robin sequence, rendering their work to be a valuable source of information on the early communication development of these children.
    > According to Shprintzen and Bardach (1995) additional syndromes exist in more than half of all Pierre Robin sequence cases, such as Stickler syndrome (34% of all Pierre Robin sequence cases) and Velocardial Facial syndrome (11% of all Pierre Robin sequence cases). The presence of an additional syndrome in young children with Pierre Robin sequence places them at greater risk to display delayed or disordered communication development. Speech-language therapists delivering services to young children are advised to take cognisance ofthe fact that a relatively high number of children with Pierre Robin sequence may have an additional syndrome and to provide services that are responsive to the individual needs of each child (Shprintzen & Bardach, 1995).
  - Snippet 2 (score: 0.580)
    > The communication development of young children with Pierre Robin sequence is traditionally described as being characterised by the same impairments as that of children with cleft lip and palate, namely: velopharyngeal incom-Die Suid-Afrikaanse Tydskrif vir Kommunikasieafwykings, Vol. 45, 1998 Reproduced by Sabinet Gateway under licence granted by the Publisher ( dated 2012) petence, nasal emission, hypernasality, compensatory articulation patterns and delayed language development (McWilliams, Morris & Shelton, 1990). Infants with cleft lip and palate are classified as presenting an established risk for communication disorders (Rossetti, 1996), but the combination and magnitude of the risk factors present in the case history of most young children with Pierre Robin sequence can have an even greater influence on their communication development. A combination of established, biological and environmental risk factors are often associated with young children with Pierre Robin sequence and may have a negative influence on the way a child with Pierre Robin sequence interacts with his environment. These risk factors are summarised in Table 1.
    > Children with Pierre Robin sequence are described indepth in the literature due to the complexity ofthe disorder (Sadewitz, 1992) and special attention is given to research on the early medical complications accompanying Pierre Robin sequence (Bull et aI., 1990;Elliott et aI., 1995;Sadewitz, 1990). In spite of the number of studies on the medical complications of Pierre Robin sequence and the atrisk status of young children with Pierre Robin sequence, a dearth in the literature exists regarding information about the outcome of their communication development. An early study conducted by Pashayan and Lewis in 1984 provided information regarding the speech-and language development of children with isolated Pierre Robin sequence as well as of children with Pierre Robin sequence and an additional syndrome. The speech-and language development of children with isolated Pierre Robin sequence was found to be impaired and the speech-and language development ofthose children with Pierre Robin sequence and an additional syndrome was found to be even more impaired and delayed than those with isolated Pierre Robin sequence.

### [2] Clinical and genetic characterization of patients with Pierre Robin sequence and spinal disease: review of the literature and novel terminal 10q deletion
- Authors: Anudeep Yekula, C. Grant, Mihir Gupta, D. Santiago-Dieppa, Pate J Duddleston et al.
- Year: 2020
- Venue: Child's Nervous System
- URL: https://www.semanticscholar.org/paper/d41e370ce3f41e5e869ec246d18e58957e2b1305
- DOI: 10.1007/s00381-020-04642-2
- PMID: 32399800
- PMCID: 7300078
- Citations: 7
- Summary: The need for early genetic testing and counseling in this patient population is emphasized, in parallel with research efforts to develop molecular classifications to guide clinical management, through a systematic review of spinal disease in patients with PRS.
- Evidence snippets:
  - Snippet 1 (score: 0.639)
    > The Pierre Robin sequence (PRS), also known as Robin sequence, is a pattern of congenital facial abnormalities comprising micrognathia, glossoptosis, and airway obstruction [1]. The reported incidence varies widely with an approximate occurrence of 1 in 8500 to 14,000 births. Approximately 50% of PRS cases are isolated (non-syndromic), while the remainder are associated with additional anomalies such as a genetic or acquired syndrome [2][3][4][5].
    > PRS is most commonly associated with hearing loss, dysmorphic facial features, global developmental delay/ intellectual disability, and/or congenital heart defects [4]. Spinal pathologies have rarely been reported in association with PRS, often co-occurring with other congenital anomalies [6][7][8][9][10][11][12][13][14][15][16][17][18][19][20][21][22]. The molecular genetic and clinical characteristics of spinal disease in PRS remain poorly characterized. We thus performed a systematic review of spinal disease in patients with PRS. We additionally report a case of a PRS patient presenting with tethered cord and lumbar syrinx in the setting of chromosome 10q terminal deletion.
  - Snippet 2 (score: 0.536)
    > We performed a systematic search for all cases of spinal diseases in patients with PRS reported in the literature using the PubMed, Google Scholar, Trip, and MEDLINE databases. The search strategy and results are summarized in Fig. 2. Inclusion criteria were (1) confirmed PRS, (2) any spinal pathology, and (3) English language. Search strings included all combinations of the terms "Pierre Robin sequence" or "Robin sequence" with the terms "spine," "spinal," "vertebral," "tethered," and "scoliosis." Abstracts and full-text articles were screened to identify reports that passed the inclusion criteria. Additional publications were identified from the references listed in each study. We excluded reports that lacked caselevel descriptions of spinal pathology, clinical characteristics, or management. The Preferred Reporting Items for Systematic Reviews and Meta-Analysis (PRISMA) criteria were followed. Ethical approval for the case report was obtained from the Institutional Review Board of Rady Children's Hospital.

### [3] Implementing the Brazilian Database on Orofacial Clefts
- Authors: I. Monlleó, M. I. B. Fontes, E. Ribeiro, Josiane Custódio de Souza, G. Leal et al.
- Year: 2013
- Venue: Plastic Surgery International
- URL: https://www.semanticscholar.org/paper/2cb27733af6824f7231879187a927700037957b1
- DOI: 10.1155/2013/641570
- PMID: 23577250
- PMCID: 3610354
- Citations: 21
- Influential citations: 1
- Summary: The potential and perspectives of the Brazilian Database on Orofacial Clefts (BDOC) may be useful to develop and improve personalized treatment, family planning, and healthcare policies, and could be incorporated into routine patient care.
- Evidence snippets:
  - Snippet 1 (score: 0.619)
    > Individuals with typical OC and Pierre-Robin sequence in isolated and nonisolated presentation were included. Data on abortuses, stillbirths, cleft uvula, median, oblique, and submucous clefts were not included.
    > Typical OC (CL, CLP, and CP) and Pierre-Robin sequence were defined according to the International Classification of Diseases 10th Edition. Terms isolated and associated were used to refer to additional minor or major defects regardless of the cause or mechanism involved while syndromic and nonsyndromic, to refer to the underlying aetiology [13].
    > Case classification was based on the definitions of the IPDTOC Working Group (2011) which defines three phenotype categories: isolated clefts, recognized syndrome, and multimalformed cases (MMC). Accordingly, cases of known nonrandom association (e.g., VACTERL) are included into the category of recognized syndromes. Cases with random combination of major unrelated defects with evidence of distinct aetiological factors are included in the group of MMC. Deformities were considered minor defects [12]. A list of minor defects was reviewed along with ICBDSR in May 2007 and is available at http://www.icbdsr.org/.

### [4] The Robin Anomalad: A case report of genetic disorder with rare oral manifestations
- Authors: K. Deotale, A. Lanjekar, I. Madne, R. Jaiswal, S. Chincholkar et al.
- Year: 2024
- Venue: Archives of Dental Research
- URL: https://www.semanticscholar.org/paper/5cfc76bccb0bcb8762e8176f52483766a4245614
- DOI: 10.18231/j.adr.2024.013
- Summary: This case report describes a case of non-syndromic Pierre Robin Syndrome (ns-PRS) in a 17-year-old male patient with unique oral characteristics, adding to the body of knowledge on unusual PRS presentations. There was enough literature to support all of the unusual findings reported in this instance leading to a precise diagnosis of Grade I ns-PRS. Some individuals with PRS might show all the typical signs, whereas others may appear with only rare signs. Such kind of more rare manifestations...
- Evidence snippets:
  - Snippet 1 (score: 0.590)
    > This case report describes a case of non-syndromic Pierre Robin Syndrome (ns-PRS) in a 17-year-old male patient with unique oral characteristics, adding to the body of knowledge on unusual PRS presentations. There was enough literature to support all of the unusual findings reported in this instance leading to a precise diagnosis of Grade I ns-PRS. Some individuals with PRS might show all the typical signs, whereas others may appear with only rare signs. Such kind of more rare manifestations should be recognized and should be reported further to add credence to the literature on unusual manifestations of PRS.

### [5] DEFINING CHARACTERISTICS OF PRIMARY DENTITION IN A CHILD WITH ISOLATED PIERRE-ROBIN SEQUENCE: UNVEILING A NOVEL PHENOTYPIC EXPRESSION- A CASE REPORT
- Authors: A. I., P. B., R. A.
- Year: 2025
- Venue: International Journal of Advanced Research
- URL: https://www.semanticscholar.org/paper/fb38210f46b25aa94463ed08d47eee1f852a6bc3
- DOI: 10.21474/ijar01/20669
- Summary: A unique phenotypic expression of primary dentition in a child diagnosed with Pierre-Robin sequence is explored, exploring a unique phenotypic expression of primary dentition in a child diagnosed with Pierre-Robin sequence.
- Evidence snippets:
  - Snippet 1 (score: 0.573)
    > DEFINING CHARACTERISTICS OF PRIMARY DENTITION IN A CHILD WITH ISOLATED PIERRE-ROBIN SEQUENCE: UNVEILING A NOVEL PHENOTYPIC EXPRESSION- A CASE REPORT

### [6] Multidisciplinary treatment of Pierre Robin sequence: a review
- Authors: Diego Thiers Oliveira Carneiro, José Ferreira da Cunha-Filho, Raquel Nascimento da Silva
- Year: 2024
- Venue: Brazilian Journal of Dentistry and Oral Radiology
- URL: https://www.semanticscholar.org/paper/994f75f1d79b290abf1858f7ed39577ad577b68b
- DOI: 10.52600/2965-8837.bjdor.2022.1.bjd10
- Citations: 1
- Summary: This study observed a journal of literature and the surgical and non-surgical treatment and multidisciplinary Hospital Infantil Albert Sabin with maxillofacial surgeons, orthodontists, neonatologists, pediatricians, pediatrics surgeons, plastic surgeons, and speech therapists for patients with SPR.
- Evidence snippets:
  - Snippet 1 (score: 0.569)
    > Historically, Fairbairn in 1846, and Lannelongue and Menard in 1891, were the first to describe Pierre Robin Syndrome in patients who exhibited micrognathia, cleft palate, and glossoptosis. Pierre Robin, a French stomatologist, in 1923, pointed to the association of glossoptosis and micrognathia and later added references to cleft palates in his early writings eleven years afterwards [1][2][3]. In 1974, the triad was named Pierre Robin Sequence (PRS) [4]. The term "syndrome" is used when there is a simultaneous presence of several abnormalities originating from a single etiology. The term "sequence" is used when several abnormalities arise from a cascade of events initiated by a single malformation [2,4]. Thus, the term Pierre Robin Syndrome came to be known as Pierre Robin Sequence. Therefore, the well-known PRS has been designated as a non-specific symptomatic complex that can occur in various isolated situations, associated with some syndrome, or associated with other developmental errors, which together do not correspond to a specific syndrome [2].
    > PRS is a triad of anomalies characterized by micrognathia and/or retrognathia, glossoptosis, and obstruction of the upper airways [5]. A cleft palate is present in 90% of the cases [3,6], which makes this clinical evidence not essential for diagnosis, as not all affected by PRS present this finding [7]. Airway obstruction and feeding difficulties are the most common and severe manifestations in the neonatal period. There is heterogeneity of clinical manifestations [8], observing mild expressions of respiratory and feeding difficulties to severe asphyxia crises, which can lead to death if there is no rapid medical intervention [9,10]. Syndromic craniofacial changes may accompany PRS, such as Stickler syndrome, Treacher Collins syndrome, and Neger syndrome, for example [6].
    > The treatment of PRS can occur through non-surgical therapy or surgical intervention. Some newborns can be placed in the considered ideal posture, prone, until there is adequate growth of the jaw.

### [7] A Giant Heart Tumor in Neonate with Clinical Signs of Pierre - Robin Syndrome
- Authors: R. Bejiqi, R. Retkoceri, Hana Xhema-Bejiqi, R. Bejiqi, A. Maloku
- Year: 2017
- Venue: Medical Archives
- URL: https://www.semanticscholar.org/paper/96d87f4cdd707f5ca4856b5a654ec63758085480
- DOI: 10.5455/medarh.2017.71.141-143
- PMID: 28790548
- PMCID: 5511525
- Citations: 1
- Summary: The literature on the fetuses and neonates with cardiac tumors is reviewed in an attempt to determine the various ways which cardiac tumors differ clinically and morphologically in this age group.
- Evidence snippets:
  - Snippet 1 (score: 0.565)
    > Introduction: Pierre Robin syndrome is a congenital condition of facial abnormalities in humans. The three main features are: cleft palate, retrognathia and glossoptosis. Rarely heart tumors are associated with syndromes, mostly are isolated. Case report: In this presentation we describe a 3-weeks-old girl with Pierre-Robin syndrome and giant left ventricle tumor, diagnosed initially by transthoracic echocardiography. The purpose of this report is to review the literature on the fetuses and neonates with cardiac tumors in an attempt to determine the various ways which cardiac tumors differ clinically and morphologically in this age group.

### [8] Anorectal Malformation: An Atypical Association of Pierre Robin Sequence
- Authors: Manal Farouk, S. Kaddah, M. Kotb
- Year: 2022
- Venue: Pediatric Sciences Journal
- URL: https://www.semanticscholar.org/paper/4a1512079a63f6c3709f0a0c16e388ed5bee5568
- DOI: 10.21608/cupsj.2021.100238.1031
- Citations: 2
- Summary: It is reported that single ventricle and anorectal malformation are rare associations of PRS, and prompt diagnosis and initiation of specific management is life-saving in any neonate and especially in those with structural malformations or deformities ofPRS.
- Evidence snippets:
  - Snippet 1 (score: 0.564)
    > Isolated Pierre Robin sequence (PRS) is characterized by underdeveloped jaw, backward displacement of the tongue and upper airway obstruction with or without cleft palate or be part of a known syndrome as VACTREL or CHARGE, or be associated with other malformations as congenital heart disease, lung malformations, musculoskeletal system anomalies, and hereditary progressive arthro-ophthalmopathy. We report a neonate with PRS who presented by choanal atresia, sepsis, single ventricle, large ventricular septal defect; large patent ductus arteriosus, anorectal malformation in the form of high imperforate anus and rectovesical fistula. Anorectal malformation was not previously reported in Pierre Robin sequence. We report that single ventricle and anorectal malformation are rare associations of PRS. Examination for anorectal malformation, prompt diagnosis and initiation of specific management is life-saving in any neonate and especially in those with structural malformations or deformities of PRS. Level of Evidence of Study: IV (1).

### [9] Pierre Robin Sequence
- Authors: U. Rolle, Aranka Ifert, Robert Sader
- Year: 2019
- Venue: Pediatric Surgery
- URL: https://www.semanticscholar.org/paper/fba2ec65fddfdd291f92c1af86e52ba3dcecbae0
- DOI: 10.1007/978-3-642-38482-0_44-2
- Summary: Pierre Robin sequence may be isolated or associated with a syndrome, the commonest being Stickler, Foetal Alcohol, Treacher-Collins and Velocardiofacial syndrome and patients are at risk of inadequate nutrition, aspiration and gastro oesophageal reflux disease.
- Evidence snippets:
  - Snippet 1 (score: 0.563)
    > Disease summary: A diagnosis of Pierre Robin sequence (PRS) is established when a patient exhibits the three clinical hallmarks of microganthia (small mandible), glossoptosis (backward downward displacement of the tongue base) and airway obstruction present from birth. Cleft palate commonly occurs but is not a prerequisite for a diagnosis. Pierre Robin sequence may be isolated (20-40%) or associated with a syndrome, the commonest being Stickler, Foetal Alcohol, Treacher-Collins and Velocardiofacial syndrome. The anatomical features cause a variable degree of airway obstruction and patients may present with stridor, respiratory distress, cyanosis and signs of obstructive sleep apnoea (OSA). Patients may also exhibit other airway pathology such as laryngomalacia and subglottic stenosis. Patients are at risk of inadequate nutrition, aspiration and gastro oesophageal reflux disease. Incidence varies between 1:5000 to 1:85000, the range a reflection of the variable clinical presentation.

### [10] Pierre Robin Sequence in a Child With Ectopic Kidney, Polysyndactyly, And Short Stature: A Case Report
- Authors: Anan Abualshamat, A. Al-Agha
- Year: 2019
- Venue: Cureus
- URL: https://www.semanticscholar.org/paper/933e194cb4477bc594af4fb36ec330d848f3f909
- DOI: 10.7759/cureus.6475
- PMID: 31903312
- PMCID: 6935740
- Citations: 1
- Influential citations: 1
- Summary: The case of a 5-year-old girl with short stature, polysyndactyly, and an ectopic kidney who presented with PRS features is reported.
- Evidence snippets:
  - Snippet 1 (score: 0.559)
    > Pierre Robin sequence (PRS) is a combination of congenital anomalies comprising fetal gnathoglosso-palatoschisis. It was first described by Hilaire in 1822 and included micrognathia, cleft palate, and airway obstruction; this description was followed by that given by Fairbain in 1846 and by Shukowsky in 1911 [1]. Pierre Robin first reported the association between micrognathia and glossoptosis in 1923, which was followed by another case report in 1934 adding cleft palate to the description [2]. In the 1970s, the term "Pierre Robin syndrome" was changed to "Pierre Robin sequence" because the latter term implies a group of clinical findings [3]. The incidence of PRS varies from 1/31206 live births to 1/8060 live births [4][5].Both sex have equal prevalence [6]. PRS can be isolated (iPRS) or part of a genetic syndrome [7]. Severe respiratory distress and failure to thrive, the most common consequences of PRS, are usually secondary to small jaw, particularly when associated with glossoptosis [8][9]. We report a case of a 5-year-old girl with iPRS associated with an ectopic horseshoe kidney, polysyndactyly, and short stature.

### [11] Pierre Robin sequence and keratoconus, a rare association
- Authors: Jorge Hernández-Cerdá, Víctor Alegre-Ituarte, S. González-Ocampo
- Year: 2023
- Venue: Iberoamerican Journal of Medicine
- URL: https://www.semanticscholar.org/paper/bd1ccdd23178391e96a54fecc136f3978147be22
- DOI: 10.53986/ibjm.2023.0006
- Citations: 1
- Summary: A patient with PRS who developed keratoconus is described as a rare manifestation of the disease and its management, and the features of the Robin sequence are illustrated.
- Evidence snippets:
  - Snippet 1 (score: 0.558)
    > Pierre Robin Sequence (PRS) is a disorder affecting fundamentally the head and face, defined by micrognathia, glossoptosis and ultimately, airway restriction. Typically, a wide U-shaped cleft palate has been described associated with this syndrome [1,2]. The Pierre Robin condition is illustrated as a sequence because of the progression of its features. The underdevelopment of the mandible is thought to be secondary to an impairment in intrauterine growth. This micrognathia leads to downward displacement or retraction of the tongue (glossoptosis), which eventually results in airway obstruction and feeding difficulties [3]. Some patients have the features of PRS as part of a syndrome that affects other organs and tissues in the body, such as Stickler syndrome (most frequent) or campomelic dysplasia. When Pierre Robin sequence occurs by itself, it is described as nonsyndromic or isolated [3]. Isolated PRS is typically sporadic but familiar heritance with autosomal dominant heritance has also been described. Various chromosomal anomalies have been associated with PRS, including regions 2q24.1-33.3, 4q32-qter, 17q21-24.3, and 11q21-23.1 [4]. Other associations include gene SOX9, known to be the most common cause of isolated Pierre Robin sequence. Such gene plays a major role in the formation of different tissues during the embryonic development, through the regulation of other genes, mainly those involved in the formation of the mandible. Alterations in the SOX9 gene derive in phenotype changes from cartilage defects during early facial growth [5][6][7].
    > Santoro et al recently studied the prevalence of the disease, analyzing the cases of PRS collected by the populationbased congenital anomaly registries of EUROCAT and found that the overall prevalence was 12.0 per 100 000 births, being higher in the most recent 10-year period (2008-2017) [8].

### [12] АНОМАЛАД П’ЄРА-РОБЕНА В КЛІНІЧНІЙ ПРАКТИЦІ ПЕДІАТРА
- Authors: T. Kosovska, I. Chornomydz, V. Kosovska
- Year: 2017
- Venue: Unknown venue
- URL: https://www.semanticscholar.org/paper/b4e942acf791c65cb91e5e62501026795577bddd
- DOI: 10.11603/24116-4944.2017.2.7801
- Summary: Relevant in this syndrome is to eliminate all adverse factors in the prenatal period, child development, prenatal diagnosis of medical genetic counseling to prevent the birth of a child with an inherited disease.
- Evidence snippets:
  - Snippet 1 (score: 0.557)
    > Isolated cases anomalad Pierre-Robin are always sporadic. Anomalad is part of a syndrome of multiple birth defects, inheritance is determined depending on the type of inheritance underlying syndrome. Relevant in this syndrome is to eliminate all adverse factors in the prenatal period, child development, prenatal diagnosis of medical genetic counseling to prevent the birth of a child with an inherited disease.

### [13] Cervical diastematomyelia in a patient with Pierre-Robin syndrome – A case report
- Authors: Mehar Masroor, Alisha S. Ali, Talha Irshad, Gohar Javed
- Year: 2026
- Venue: Surgical Neurology International
- URL: https://www.semanticscholar.org/paper/6ac9efe901a2824a3f0e0dbeeb1538d9fb7f61dc
- DOI: 10.25259/SNI_877_2025
- PMID: 41783179
- PMCID: 12954261
- Summary: A 6-month-old boy who has cervical diastematomyelia and Pierre-Robin syndrome is a unique case of a 6-month-old boy who has cervical diastematomyelia and PRS.
- Evidence snippets:
  - Snippet 1 (score: 0.555)
    > Pierre-Robin syndrome (PRS) is a congenital disorder characterized by mandibular hypoplasia resulting in backward displacement of the tongue that leads to upper airway obstruction and feeding difficulties. is was first described in 1891; however, the first case was published in 1923 by Pierre-Robin. [3] It can be due to genetic mutations or due to intrauterine growth restriction, leading to mandibular hypoplasia (micrognathia). PRS can be found in isolation or in association with other syndromes, such as stickler syndrome, Treacher Collins syndrome, or in association with other anomalies. e most common anomaly found in association with PRS is cleft palate.
    > Split cord malformation (SCM) or diastematomyelia refers to a congenital condition resulting in the division of the spinal cord into two hemi-cords by a bony, fibrous, or cartilaginous septum. It is also found to be associated with several malformations, such as Klippel-Feil anomaly, Arnold Chiari deformity, and myelomeningocele. [9] Most commonly diastematomyelia are found at the lumbar level. Cervical diastematomyelia itself is extremely rare with only 75 cases reported to date. [8] In this case report, we present a child with Pierre-Robin sequence and cervical diastematomyelia. To the best of our knowledge, no reported case in the literature has discussed the association of cervical diastematomyelia in patients with the Pierre-Robin sequence.

### [14] Restoration of vision in Kniest dysplasia patient characterized by retinal detachment with dialysis of the ora serrata: A case report
- Authors: Xinlei Zhu, Xiaoli Xing, Dongfang Li, Bin Yu
- Year: 2023
- Venue: Medicine
- URL: https://www.semanticscholar.org/paper/6cd37ab174c342d4041043b4f0c79f85697ebd5a
- DOI: 10.1097/MD.0000000000036090
- PMID: 38013291
- PMCID: 10681563
- Citations: 3
- Summary: Advances in genetic screening have improved the management of retinal detachment risk in Kniest dysplasia patients, and surgical intervention successfully reattached the retina and restored vision to 20/25 in the affected eye.
- Evidence snippets:
  - Snippet 1 (score: 0.553)
    > Additionally, the identified COL2A1 gene mutation represents the first report of this particular variant in Kniest dysplasia.
    > Ocular manifestations of hereditary diseases are often overlooked.The patient's right eye was completely blind due to missed surgical intervention.Fortunately, vision in the left eye was restored through elaborate surgery.If childhood eye examinations had been performed regularly after being informed of potential accompanying ocular disease, his condition may have been less severe on presentation to our Ophthalmology Clinic.Previous studies have recommended complete ophthalmologic exams for patients clinically diagnosed with Kniest dysplasia. [11]Congenital non-progressive high myopia, vitreous abnormalities, and retinal detachment are important ocular features of this condition. [9]Additionally, other type II collagen disorders may demonstrate similar ophthalmic findings, thus regular ophthalmologic follow-up is advised. [12]nlike other cases of Kniest dysplasia, this patient was diagnosed with Pierre Robin syndrome in early childhood.Pierre Robin syndrome was first described in 1923 by the French stomatologist Pierre Robin, who reported the association between micrognathia, glossoptosis, and cleft palate. [13]Previous studies have demonstrated that Robin sequence can be associated with various genetic syndromes, most commonly Stickler syndrome and 22q11 deletion syndrome (22q11 DS). [14]The presence of ocular, skeletal or auditory abnormalities in children with Pierre Robin Sequence (PRS) should prompt suspicion for an underlying genetic syndrome.Compared to isolated PRS, additional features of Kniest dysplasia include hearing loss, retinal detachment, and progressive ocular complications that may eventually lead to blindness, as exemplified in this patient's right eye. [15]Early identification of the genetic syndrome underlying PRS is crucial for prompt ophthalmologic referral to monitor for myopia, retinal detachment, and prevention of visual complications. [16]

### [15] Pierre Robin Sequence- Manifestation and Case Report
- Authors: E. Mass, S. Segal, Y. Arieli, U. Zilberman
- Year: 2018
- Venue: Oral Health and Dental Studies
- URL: https://www.semanticscholar.org/paper/2d0ab81e67df7ab2a436eda43cf48c4c43266b0e
- DOI: 10.31532/oralhealthdentstud.1.1.004
- Citations: 1
- Summary: A multidisciplinary team including pediatric, ENT, general and oral surgeons, speech therapist, pediatric dentist, and orthodontic specialists should be involved in the treatment of PRS children for a relatively better quality of life outcome.
- Evidence snippets:
  - Snippet 1 (score: 0.547)
    > According to the Clinical Consensus report on Pierre Robin sequence (PRS), Pierre Rubin is comprising of mandibular micrognathia, glossoptosis and airway obstruction, leading to life-1 threatening obstructive apnea and feeding difficulties during the neonatal period. Cleft palate is considered a common and additional feature, but not a perquisite for diagnosis.
    > The sequence is named after Pierre Robin, whose report was published in 1923 (earlier 2,3 reports were in 1822). The reported incidence is estimated to be 1:8,500-14,000. Williams 4 and his colleagues have argued that not every child with a cleft palate and micrognatia is defined as suffering from PRS, but breathing difficulty is a necessary element for the definition.
    > The syndrome is defined as a sequence, a collection of anomalies caused by early developmental disorders or mechanical processes. The explanation of the sequence definition rather than a syndrome is based on early mandibular developmental disorder, which leads to abnormal tongue position, followed by a series of events, leading to formation of cleft 5 lip and palate.
    > Fourteen different phenotypes of PRS were found, which accentuate the variability of the 5 diagnosis and definition. The differences in defining the sequence also cause differences in 5,6 the prevalence and in reports of related syndromes.
    > PRS may be identified in more than 40 syndromes. It is difficult to identify it during birth and to distinguish it from other related syndromes.

### [16] Predicting Syndromic Status Based on Longitudinal Data from Parental Reports of the Presence of Additional Structural and Functional Anomalies in Children Born with an Orofacial Cleft
- Authors: A. Davies, Yvonne E. Wren, M. Hamilton, J. Sandy, E. Stergiakouli et al.
- Year: 2024
- Venue: Journal of Clinical Medicine
- URL: https://www.semanticscholar.org/paper/21e9031f5733f232a6cb1dd61e14d1cb52024707
- DOI: 10.3390/jcm13226924
- PMID: 39598068
- PMCID: 11594774
- Citations: 2
- Summary: Children born with a cleft who present with two or more anomalies are much more likely to have a syndrome than those with fewer anomalies and should be prioritised for genetic screening and counselling.
- Evidence snippets:
  - Snippet 1 (score: 0.541)
    > Data from the Cleft Collective were used to compare syndrome diagnosis between OFC subtypes, biological sex and the presence of two or more structural and functional anomalies. Among our study, the distribution of OFC subtypes and biological sex was similar to that seen in the UK cleft population born between 2020 and 2022 [29], and although we noted some small differences, this is likely due to our sample being born between 2008 and 2022 and due to small levels of sampling error.
    > Among participants who had two structural and functional anomalies, a diagnosed syndrome and/or sequence was reported in 27.0%, and when excluding isolated Pierre Robin sequence, 16.6% had a diagnosed syndrome. As the number of anomalies present increased so did the proportion of those with a diagnosed syndrome. Among participants who had reported five or more co-occurring anomalies, the proportion of those with a diagnosed syndrome or sequence was 81.5%. The largest difference in the prevalence of anomalies between syndromic and non-syndromic cases was seen in development problems with the jaw (27.3% versus 2.3%, respectively) and developmental delay (30.2% versus 7.2%, respectively). Developmental delay often occurred alongside an additional anomaly (38.3% of cases had developmental delay plus an additional anomaly) and was seen in children with Stickler syndrome, 22q11 deletion, craniosynostosis and CHARGE syndrome.
    > When exploring the likelihood of having a diagnosed syndrome by anomaly presentation, we excluded those children with isolated Pierre Robin sequence because children with Pierre Robin sequence, by definition, have additional anomalies; also, Pierre Robin sequence is usually diagnosed soon after birth, and those children are likely to be prioritised for genetic testing and hence are more likely to have a syndrome diagnosed if present. We investigated the likelihood of having a syndrome based on the presence of structural and functional anomalies, and for the anomalies we explored, we found that where present the likelihood of having a syndrome was between 19% and 75%.

### [17] Dentoskeletal characteristics of non-syndromic pierre robin sequence and isolated incomplete cleft palate children: a retrospective case control study
- Authors: Xiang Zhang, Shuang Yang, Xudong Yang, Zhi-Bo Zhou
- Year: 2025
- Venue: Frontiers in Pediatrics
- URL: https://www.semanticscholar.org/paper/298cb495a2835ccde1a6abc953c3e70d193bcd24
- DOI: 10.3389/fped.2025.1519266
- PMID: 40066465
- PMCID: 11891179
- Summary: The ANB angle, the ArGo/GoPO ratio and the anteroposterior length and area of LPAS could serve as valuable indicators to identify micrognathia in patients with non-syndromic PRS.
- Evidence snippets:
  - Snippet 1 (score: 0.536)
    > Dentoskeletal characteristics of non-syndromic pierre robin sequence and isolated incomplete cleft palate children: a retrospective case control study

### [18] Phenotypes, Developmental Basis, and Genetics of Pierre Robin Complex
- Authors: Susan M. Motch Perrine, Meng Wu, Greg Holmes, B. Bjork, E. Jabs et al.
- Year: 2020
- Venue: Journal of Developmental Biology
- URL: https://www.semanticscholar.org/paper/96d790eff1683ce0c67006a036e8087b65e80f54
- DOI: 10.3390/jdb8040030
- PMID: 33291480
- PMCID: 7768358
- Citations: 18
- Influential citations: 2
- Summary: This review presents the current understanding of PR phenotypes, the proposed pathogenetic processes underlying them, select genes associated with PR, and available animal models that could be used to better understand the genetic basis and phenotypic variation of PR.
- Evidence snippets:
  - Snippet 1 (score: 0.533)
    > Stomatologist Pierre Robin published an article in 1923 [1] describing a triad of clinical findings in a series of patients, namely, micrognathia, glossoptosis, and obstruction of the upper airways [7].
    > Following his widely read contribution to the literature on micrognathia in newborns [2], this triad became known as Pierre Robin syndrome by clinicians [3]. Robin considered acquired or congenital glossoptosis as a consequence of a small mandible leading to respiratory problems. These conditions ultimately result in "physical backwardness" in infancy that persists into adulthood. He also introduced the association of these anomalies with CP [2]. Robin linked the respiratory problems in these children to their physical and psychological development, and indicated that infants with severe retrognathia rarely survive beyond 18 months of age [2]. Through the 1960s, clinicians noted that PR generally occurred without other significant birth defects, although the case of a two-month-old male infant with PR and severe bilateral congenital glaucoma indicated ocular involvement in some affected individuals [8]. Natal teeth were associated with one PR patient in a cohort of infants born at Foothills Provincial Hospital in Calgary, Canada, between 1967 and 1984 [9].
    > The condition was known as Pierre Robin syndrome for nearly 50 years before it was understood that multiple etiologies could underlie the same clinical findings, which did not fit with the prevailing definition of a syndrome: a combination of symptoms resulting from a single cause [10]. In the 1970s, the term Pierre Robin anomalad was introduced [4,5], with the implication that the condition was not a specifically delineated syndrome. Anomalad signifies an etiologically nonspecific complex that can occur as a component of various genetic or teratogenic syndromes of known cause, syndromes of unknown etiology, or as an isolated symptom complex secondary to positional deformation or disruption [11,12]. Anomalad denotes a pattern of morphologic defects that stem from a single, localized, structural anomaly resulting in a cascade of consequent defects [13], so the term implies a sequence of developmental consequences of a primary defect.

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
| On topic | 11 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.11603/24116-4944.2017.2.7801` (1 mention) - АНОМАЛАД П’ЄРА-РОБЕНА В КЛІНІЧНІЙ ПРАКТИЦІ ПЕДІАТРА
  - shared terms: none
- `DOI:10.1097/MD.0000000000036090` (1 mention) - Restoration of vision in Kniest dysplasia patient characterized by retinal detachment with dialysis of the ora serrata: A case report
  - shared terms: associated, patient

Weighed against this report's own most characteristic terms: `snippet`, `syndrome`, `robin`, `pierre`, `sequence`, `year`, `score`, `venue`, `url`, `isolated`, `cleft`, `prs`, `associated`, `palate`, `patient`, `anomalie`, `association`, `glossoptosis`, `micrognathia`, `airway`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

No ontology term identifiers were found in this report.
