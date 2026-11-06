---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-21T14:14:44.242082'
end_time: '2026-10-21T14:16:06.194807'
duration_seconds: 81.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Familial progressive retinal dystrophy-iris coloboma-congenital cataract
    syndrome
  mondo_id: MONDO:0014747
  category: Mendelian
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 4
  num_turns: 10
  total_cost_usd: 0.8845613999999999
  session_id: 443f82f9-63c8-59dc-8b61-7885a3eac719
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 19
  verified: 19
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial progressive retinal dystrophy-iris coloboma-congenital cataract syndrome
- **MONDO ID:** MONDO:0014747 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial progressive retinal dystrophy-iris coloboma-congenital cataract syndrome** covering all of the
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

I'm trying to pull the PubMed abstracts for the key papers so the quotes in the report are exact.

# Research report: Familial progressive retinal dystrophy–iris coloboma–congenital cataract syndrome (RDICC; MONDO:0014747)

**Verification status.** Web search worked, but I could not fetch primary-source text. PubMed and PMC fetches were blocked, and E-utilities was refused permission. So:
- No abstract quotes are reproduced here. Everything below is paraphrased from search-result summaries.
- Each PMID is marked **[verify]**, meaning it must go through `just fetch-reference` before it is cited as evidence.
- Items marked "not established" are either not found or not verifiable. I have not filled them from memory.

## 1. Disease information

**Overview.** RDICC is a rare autosomal dominant ocular disorder. Its core features are early-onset, progressive chorioretinal (retinal) dystrophy with marked vision loss, and iris coloboma. Congenital or early-onset cataract is variably present. Occasional congenital glaucoma, iridolenticular adhesions, RPE mottling and mild hypermetropic astigmatism are also reported. [NORD/MONDO page](https://rarediseases.org/mondo-disease/familial-progressive-retinal-dystrophy-iris-coloboma-congenital-cataract-syndrome/), [MalaCards](https://www.malacards.org/card/retinal_dystrophy_and_iris_coloboma_with_or_without_cataract), [SAIL concept library, MONDO:0014747](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0014747/).

**Identifiers** (per the sources above and [MedGen via a mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C4225493/index.html?cmd=HTOff)):
- OMIM 616722
- Orphanet 488197
- GARD 0017888
- MedGen 903733
- MONDO:0014747
- KEGG disease [H02290](https://www.kegg.jp/entry/H02290)
- ICD-10/11 and MeSH mappings: not established.

**Synonyms.**
- Retinal dystrophy and iris coloboma with or without cataract
- RDICC
- Retinal dystrophy and iris coloboma with or without congenital cataract (KEGG wording)

**Do not conflate with** retinal dystrophy–iris coloboma–comedogenic acne syndrome (OMIM 615147, Orphanet 352718). That is a separate, autosomal recessive entity.

**Source of information.** The data are aggregated from family-level case reports, not EHR or individual-patient records.

## 2. Etiology

- **Cause:** a heterozygous, recurrent variant in the seed region of the microRNA gene *MIR204*, **n.37C>T**. It was first reported in a five-generation family (Conte et al., PNAS 2015, PMID 26056285 **[verify]**; KEGG cites this as 112:E3236–45, DOI 10.1073/pnas.1401464112). Per search summaries, the variant segregated with disease in all affected individuals.
- **Second family:** a Czech three-generation family with four affected heterozygotes (Jedlickova et al., Clin Genet 2023, PMID 37321975 **[verify]**). Haplotype analysis excluded relatedness to the original family. The variant is therefore recurrent, not a single founder.
- **Risk, protective and environmental factors:** none established. Modifier genes are not established either; the variable expressivity is unexplained.

## 3. Phenotypes

Frequencies are not quantified in any source I could read. All onset and progression statements are from secondary summaries.

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Retinal/chorioretinal dystrophy | HP:0000556 Retinal dystrophy | Early onset, progressive; core feature |
| Iris coloboma | HP:0000612 Iris coloboma | Variable penetrance |
| Cataract (congenital/early) | HP:0000519 Congenital cataract | "With or without"; the Czech family had premature cataract |
| Congenital glaucoma | HP:0001087 Congenital glaucoma | Occasional |
| Marked vision loss | HP:0000572 Visual loss | Progressive |
| Chorioretinal coloboma | HP:0000567 | Check the primary report |
| Mild hypermetropic astigmatism | HP:0000483 Astigmatism | Reported |
| Retinal pigment epithelial mottling | HP:0000580 | Reported |

Reported: iridolenticular adhesions, from the NORD/MONDO page. HPO terms are suggestions to be confirmed by lookup before binding.

Quality-of-life data: not established.

## 4. Genetic and molecular information

- **Gene:** *MIR204* (9q21.12), which hosts the miRNA miR-204. It sits in intron 6 of *TRPM3*. HGNC ID: look up; I did not verify it.
- **Variant:** n.37C>T, in the miRNA seed region. It is heterozygous germline. ClinVar/ACMG classification and gnomAD frequency were not checked.
- **Mechanism:** the authors propose gain of function. The mutant miRNA has altered targeting, per [PanelApp summarising PMID 26056285](https://panelapp.genomicsengland.co.uk/panels/307/gene/MIR204).
- **Panel status:** *MIR204* is on the Genomics England [structural eye disease panel](https://panelapp.genomicsengland.co.uk/panels/509/gene/MIR204/), as monoallelic.
- **Gene count:** MalaCards lists two genes, but only *MIR204* was confirmed.
- **Epigenetic and chromosomal data:** none found.

## 5. Environmental information

No environmental, lifestyle or infectious factors are known. These slots should be left empty with a note, or given a review-notes waiver.

## 6. Mechanism and pathophysiology

**Causal chain** (steps 3–5 are inferred, not directly demonstrated in humans):
1. A germline *MIR204* n.37C>T substitution in the seed region of miR-204 is the initiating lesion (human genetics, two families).
2. The seed change redirects miR-204 targeting: the mutant miRNA loses some canonical targets and gains new ones. Reporter assays support this (PanelApp summary of PMID 26056285 **[verify]**). This is a gain-of-function or neomorphic effect.
3. Dysregulation of miR-204 target genes and of the pathways they control in eye development follows (inferred). Earlier medaka work (Conte et al., PNAS 2010 **[verify PMID]**) showed that miR-204 knockdown causes small eyes, lens defects and coloboma. The reported effector was elevated *Meis2*, with altered Pax6-pathway regulation.
4. The result is defective optic fissure closure and anterior-segment/lens development, giving iris coloboma and cataract (inferred from the medaka phenotype).
5. In the retina, photoreceptors are lost through increased apoptosis. Injecting mutant miR-204 into medaka reproduced the family's phenotype, including this photoreceptor loss (search summary of PMID 26056285 **[verify]**). This leads to progressive retinal dystrophy.

**Branching:** the anterior-segment/lens branch (coloboma, cataract, glaucoma) is developmental. The retinal branch is degenerative. Why penetrance differs between these branches is unexplained.

**Suggested terms.**
- GO: post-transcriptional gene silencing by miRNA (GO:0035195). Verify by lookup.
- GO: apoptotic process (GO:0006915) and eye development (GO:0001654). Verify by lookup.
- CL: photoreceptor cell (CL:0000210), retinal pigment epithelial cell (CL:0002586), lens epithelial cell. Verify by lookup.

Omics, single-cell, proteomics and screen data: none found.

## 7. Anatomical structures affected

- **Primary:** eye. That covers the retina (photoreceptors and RPE), choroid/chorioretina, iris, and lens (UBERON terms to be looked up).
- **Secondary:** none reported.
- **Laterality:** not established.
- **Subcellular:** cytoplasmic RISC/miRNA machinery.

## 8. Temporal development

- **Onset:** early. The retinal dystrophy is described as early-onset, and the cataract and coloboma as congenital or early. Exact ages are not established.
- **Course:** progressive retinal degeneration with marked vision loss. Staging, remission and critical periods: not established.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant.
- **Penetrance and expressivity:** variable. Iris coloboma, cataract and glaucoma are inconsistently present even within one family (Czech family, per the 2023 abstract summary).
- **Prevalence:** Orphanet-style estimates of about 1 in 8,000, and about 1,000 US cases per GARD, appear on the aggregator page. These look like band placeholders; I would not curate them as measured values.
- **Founder effect:** the two families are unrelated, so the variant is recurrent. Anticipation, germline mosaicism, carrier frequency, sex ratio and geography: not established.

## 10. Diagnostics

- **Genetic testing:** targeted *MIR204* sequencing, or a structural eye disease or inherited retinal disease panel that includes *MIR204*. Note that standard exome pipelines can miss small non-coding RNA genes, so confirm coverage.
- **Clinical:** dilated fundus exam, OCT, fundus autofluorescence, ERG and visual fields. This is standard practice for inherited retinal dystrophy, not RDICC-specific evidence from my sources.
- **Differential:** retinal dystrophy–iris coloboma–comedogenic acne syndrome (OMIM 615147), other coloboma genes (e.g. *PAX6*, *CHD7*), and other inherited retinal dystrophies.
- **Screening and criteria:** none established.

## 11. Outcome and prognosis

Progressive visual loss is expected. Survival, life expectancy, prognostic factors and QoL data: not established.

## 12. Treatment

No disease-specific therapy was found. Management is supportive, so these NCIT terms would apply:
- NCIT:C15747 Supportive Care
- NCIT:C15329 Surgical Procedure (cataract and glaucoma surgery)
- NCIT:C15240 Genetic Counseling
- NCIT:C15315 Rehabilitation (low-vision services)

Clinical trials and pharmacogenomics: none found. I did not search ClinicalTrials.gov. A gain-of-function miRNA seed variant would suggest allele-specific RNA approaches, but that is speculation with no source behind it.

## 13. Prevention

Genetic counseling is the main measure; the condition is autosomal dominant. Preimplantation and prenatal testing are options in principle. Cascade testing of relatives is reasonable. No source-backed screening programme exists.

## 14. Other species and natural disease

Natural disease in other species: not found. I did not check OMIA.

## 15. Model organisms

- **Medaka:** miR-204 knockdown gives small eyes, lens defects and coloboma (Conte 2010). Injecting the n.37C>T miRNA reproduced the family phenotype, including photoreceptor apoptosis (2015). Both are `MODEL_ORGANISM` evidence.
- **Limitation:** miR-204 target repertoire and eye anatomy differ between fish and humans. I have not checked whether a mouse or zebrafish model recapitulates the human phenotype; a search mention of a mouse model was unconfirmed.

## Curation notes

1. Cite only PMIDs fetched into `references_cache/`. The two I have, PMID 26056285 (PanelApp-sourced, not checked in PubMed) and PMID 37321975 (search-sourced), still need fetching. The 2010 medaka paper's PMID is unknown to me.
2. Copy snippets only from fetched text; I did not obtain any.
3. Bind the *MIR204* gene descriptor only after an HGNC lookup. Remember the lowercase `hgnc:` prefix.
4. An `inheritance` block bound to autosomal dominant inheritance (HP:0000006) is supported, subject to lookup.

Sources:
- [NORD/MONDO page](https://rarediseases.org/mondo-disease/familial-progressive-retinal-dystrophy-iris-coloboma-congenital-cataract-syndrome/)
- [MalaCards: RDICC](https://www.malacards.org/card/retinal_dystrophy_and_iris_coloboma_with_or_without_cataract)
- [SAIL concept library, MONDO:0014747](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0014747/)
- [MedGen mirror C4225493](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/medgen/C4225493/index.html?cmd=HTOff)
- [KEGG H02290](https://www.kegg.jp/entry/H02290)
- [Genomics England PanelApp, MIR204 (panel 307)](https://panelapp.genomicsengland.co.uk/panels/307/gene/MIR204)
- [Genomics England PanelApp, MIR204 (panel 509)](https://panelapp.genomicsengland.co.uk/panels/509/gene/MIR204/)
- [Masaryk University publication record for the 2023 Czech family](https://muni.cz/en/research/publications/2367151)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 5 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000580` (1 mention) - the report calls it "Retinal pigment epithelial mottling"; HP calls it **Pigmentary retinopathy**, and lists "Retinal pigment clumping" among its other names
- `GO:0035195` (1 mention) - the report calls it "GO: post-transcriptional gene silencing by miRNA"; GO calls it **miRNA-mediated post-transcriptional gene silencing**
- `GO:0006915` (1 mention) - the report calls it "GO: apoptotic process"; GO calls it **apoptotic process**
- `CL:0000210` (1 mention) - the report calls it "CL: photoreceptor cell"; CL calls it **photoreceptor cell**
- `HP:0000006` (1 mention) - the report calls it "An `inheritance` block bound to autosomal dominant inheritance"; HP calls it **Autosomal dominant inheritance**

Every term resolved, and every label the report gave matched.