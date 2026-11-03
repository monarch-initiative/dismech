---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T19:14:40.996544'
end_time: '2026-10-15T19:16:26.497624'
duration_seconds: 105.5
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodegeneration and Seizures Due to Copper Transport Defect
  mondo_id: MONDO:0957211
  category: Genetic
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
  num_turns: 12
  total_cost_usd: 0.8478961000000005
  session_id: a4618dfa-d284-5dfb-b077-0a3b19b97962
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 1
  verified: 1
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
- **Disease Name:** Neurodegeneration and Seizures Due to Copper Transport Defect
- **MONDO ID:** MONDO:0957211 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neurodegeneration and Seizures Due to Copper Transport Defect** covering all of the
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

I'll start by loading the search tools.

Still gathering sources: PMC and PubMed blocked my fetches, so I'm trying the open-access PDF of the 2025 13-case cohort.

# Neurodegeneration and Seizures Due to Copper Transport Defect (NSCT): research report

**Scope and limits.** This is a report from one session of web searching. Fetches of PubMed and PMC were blocked, so I did not read the Batzios 2022 or Dame 2023 abstracts directly. Claims about them come from search-engine summaries of the papers, the KEGG entry and the Nationwide Children's press release. I read the 2025 cohort only as an abstract (from PDF metadata). I did not obtain its full text or its PMID.

- Per your attribution rules, nothing below is a verified exact quote from a primary abstract. Treat every snippet candidate as a lead until checked with `just fetch-reference`.
- I wrote no ontology CURIEs. HPO, GO, CL, UBERON, CHEBI and NCIT suggestions are term names only, and each needs a lookup before binding.
- One search summary wrongly implied that PMC11419079 was the 13-patient cohort. I opened it: it is a bioRxiv preprint (Lane et al.) with no patients. I corrected this below.

## 1. Disease information

**Overview.** NSCT is an autosomal recessive, infantile-onset syndrome. KEGG describes it as "characterized by hypotonia, global developmental delay, seizures, and rapid brain atrophy," caused by SLC31A1 variants (structured database, [KEGG H02736](https://www.kegg.jp/entry/H02736)). SLC31A1 encodes CTR1, the high-affinity copper uptake transporter.

**Identifiers** (structured databases, not primary literature):
- MONDO:0957211 and OMIM 620306, per a MedGen mirror: [MedGen C5830385](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/www.ncbi.nlm.nih.gov/medgen/C5830385/index.html). MedGen also lists the synonym "NSCT" and locus 9q32.
- OMIM 620306 is also confirmed by [KEGG H02736](https://www.kegg.jp/entry/H02736).
- Gene OMIM 603085 and gene panel listings: [PanelApp AU](https://panelapp-aus.org/panels/3469/gene/SLC31A1/).
- ICD-11 5C64 (disorders of mineral absorption or transport) and KEGG H02736: [KEGG](https://www.kegg.jp/entry/H02736).
- Orphanet and MeSH IDs: **not found** in this session.

**Synonyms.** NSCT. "SLC31A1-related developmental and epileptic encephalopathy" is the title wording of the 2025 cohort, and "CTR1 deficiency" is used informally.

**Individual vs. aggregate.** The sources are individual-patient case reports and small series. There is no registry data.

**Lump/split note.**
- This is a germline Mendelian entity, so it needs no somatic counterpart.
- A search result also said GeneCards links SLC31A1 to "alacrima, achalasia, and impaired intellectual development." I could not corroborate that, so I excluded it. Treat it as unverified.

## 2. Etiology

- **Cause:** bi-allelic SLC31A1 variants, as described in the sources below.
- **Genetic risk and modifiers:** none reported in the sources I reached.
- **Environmental, protective, and gene-environment factors:** none documented.
- **Dietary copper:** the CNS copper deficiency appears to arise from impaired transport, not intake. The sources describe a transporter defect, not dietary deficiency.

## 3. Phenotypes

**Batzios et al. 2022.**
- Source: Batzios S, et al., *Hum Mol Genet* 31:4121-4130, PMID:35913762, DOI:10.1093/hmg/ddac156. The PMID comes from KEGG. The description comes from search summaries.
- Patients: identical male twins, apparently normal for roughly the first two months, then hypotonia, global developmental delay, seizures and rapid brain atrophy.
- Per the summaries, the atrophy was more pronounced than in untreated Menkes disease.

**Dame et al. 2023.**
- Source: Dame C, et al., *Clin Genet* 103:585-589, PMID:36562171.
- Patient: a newborn with a homozygous likely pathogenic SLC31A1 variant (reported as c.236T>C), very low serum copper and ceruloplasmin, and a fatal course.
- Caveat: the title says "fatal congenital copper transport defect." I did not read the paper for onset or the cause of death.

**Brain Commun 2025** (DOI:10.1093/braincomms/fcaf348, "insights from 13 new cases"). The abstract reports:
- "early-onset epileptic encephalopathy, severe neurodevelopmental delay and hypotonia," with high mortality.
- Neuroimaging with "significant brain atrophy and white matter abnormalities."
- 13 cases from 10 families.

The details I could not obtain are onset ages, seizure types, EEG, per-feature frequencies, survival figures, and serum copper and ceruloplasmin across the cohort.

**HPO term names to look up and bind** (leads only):
- Hypotonia
- Global developmental delay
- Seizures / epileptic encephalopathy
- Cerebral atrophy
- Abnormal white matter morphology
- Low serum copper and low ceruloplasmin (a laboratory abnormality; Dame 2023 only)

**Frequencies and quality-of-life data:** not available. Cohort sizes are too small, and the high mortality makes quality-of-life data unlikely.

## 4. Genetic and molecular information

- **Gene:** SLC31A1 (HGNC symbol; use the lowercase `hgnc:` form in the KB after looking up the ID). Locus 9q32.
- **Reported variants:**
  - p.Arg95His (NM_001859.4:c.284G>A) in the Batzios twins.
  - A homozygous variant reported as c.236T>C in Dame 2023. The protein change is not confirmed here.
  - In the 2025 cohort, bi-allelic variants "predominantly p.His120Gln in six cases and p.(Arg102Cys/His) in three cases."
- **Preprint discrepancy:** an earlier medRxiv preprint described p.His120Gln as five cases from four families. The published count is six cases. I did not reconcile the difference.
- **Functional consequence:** probably reduced copper uptake (partial loss of function). The 2025 abstract names RNA sequencing, Western blotting for CTR1 protein and high-resolution respirometry. It does not report the CTR1 protein or RNA results.
- **Population frequency, ClinVar and ClinGen status, founder alleles, epigenetics and chromosomal abnormalities:** not obtained.

## 5. Environmental information

No environmental, lifestyle or infectious factors were identified.

## 6. Mechanism and pathophysiology

**Causal chain** (each step is labelled demonstrated or inferred):
1. Bi-allelic missense variants in SLC31A1 (demonstrated by sequencing in patients) reduce CTR1 function. The mechanism is inferred in humans. The variants were assessed using patient cells and in vitro assays.
2. Reduced CTR1 function lowers cellular copper uptake. The Batzios title and press coverage call it a "copper transport defect."
3. Copper reaching the brain is reduced. Batzios linked the variant to profound CNS copper deficiency (search summary; mechanism inferred). The 2025 preprint abstract says CTR1 is strongly expressed in the basolateral choroid plexus epithelium, which mediates brain copper uptake.
4. Copper-dependent enzymes lose function, notably cytochrome c oxidase (complex IV). The summaries say copper histidinate normalized cytochrome c oxidase activity in the patients' cells in vitro. In the 2025 cohort, patient fibroblasts show "impaired mitochondrial respiration" (abstract).
5. Impaired oxidative phosphorylation leads to neuronal dysfunction and loss. This step is inferred, not demonstrated in patients.
6. Seizures, hypotonia, developmental regression and rapid brain atrophy follow (clinical observation).

**Cell-model support.** Lane et al. 2024 is a preprint in SH-SY5Y neuroblastoma cells, *Atp7a* conditional knockout mice and *Drosophila* (bioRxiv, DOI:10.1101/2024.09.09.612106, PMID:39314281; later published in *Mol Biol Cell*, which I did not verify). In SLC31A1-knockout cells I read:
- Complex IV at about 55% of wild type.
- Basal respiration at 0.53× and glycolysis at 2.03×.
- Higher mTORC1-S6K signaling, with protein synthesis up about 1.5-fold.

This is IN_VITRO and MODEL_ORGANISM evidence, not patient data. The authors interpret the shift as an adaptive response.

**Related disorder.** Menkes disease (ATP7A) is the comparison case. The Batzios summary describes the atrophy as more pronounced than in untreated Menkes disease.

**Ontology term names to look up** (leads only):
- GO: copper ion import; mitochondrial respiratory chain complex IV assembly or cytochrome-c oxidase activity.
- CL: neuron; choroid plexus epithelial cell.
- UBERON: brain; choroid plexus.
- CHEBI: copper(2+) or copper cation.

## 7. Anatomical structures

- **Primary organ:** the brain, with atrophy and white matter abnormalities (2025 abstract).
- **Choroid plexus:** the site of CTR1 expression noted in the preprint abstract.
- **Subcellular compartment:** mitochondria, via the respiratory chain.
- **Lateralization:** not reported.

## 8. Temporal development

- **Onset:** infantile (KEGG). The Batzios twins were apparently normal for about two months, then declined. Dame 2023 describes a congenital presentation.
- **Course:** rapid and progressive, with high mortality in the 2025 cohort.
- **Remission and critical periods:** not documented. Batzios discusses early copper treatment, but I did not read it.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (KEGG).
- **Prevalence, incidence, founder effects, sex ratio, carrier frequency:** not found. The condition is extremely rare, with only a few dozen reported cases.
- **Consanguinity:** not assessed.

## 10. Diagnostics

- **Laboratory:** low serum copper and ceruloplasmin were reported in Dame 2023 (via search summary). Whether this holds across the 13 new cases is unknown.
- **Imaging:** MRI shows brain atrophy and white matter abnormalities.
- **Genetic testing:** sequencing of SLC31A1, via exome, genome or an epilepsy or metal metabolism panel. PanelApp Australia lists SLC31A1 on its Genetic Epilepsy and Metal Metabolism Disorders panels.
- **Functional confirmation:** patient fibroblast studies (cytochrome c oxidase activity, respirometry).
- **Differential diagnosis:** Menkes disease and other ATP7A-related disorders, other copper metabolism disorders, and mitochondrial disease.
- **Screening:** none is established.

## 11. Outcome and prognosis

- **Mortality:** "high mortality" (2025 abstract), and a fatal course in Dame 2023. I have no survival curves or median ages.
- **Prognostic factors:** unknown.

## 12. Treatment

- **Copper histidinate:** used under a formal clinical protocol in the Batzios twins. Per the search summary, it normalized cytochrome c oxidase activity in vitro and was associated with "modest clinical improvement."
- **Candidate NCIT terms** (to look up): pharmacotherapy and supportive care for the seizures. Copper histidinate itself needs a CHEBI or NCIT term lookup.
- **Trials:** I did not search ClinicalTrials.gov. No NCT number is cited here.
- **Experimental:** elesclomol was tested in cells only (Lane et al. preprint).
- **Not documented:** pharmacogenomics, gene therapy, dietary treatment, and specific antiseizure regimens.

## 13. Prevention

- Genetic counseling and carrier testing of parents (standard for recessive disease; not NSCT-specific literature).
- Prenatal and preimplantation testing for known familial variants (inferred; no source).
- No newborn screening or primary prevention is documented.

## 14. Other species and natural disease

I found no OMIA entry or natural disease in other species. I did not search OMIA.

## 15. Model organisms

- **Knockout mice:** the search summary said CTR1 knockout in mice is prenatally lethal. I did not find the primary paper, so I cannot cite it. Classic *Ctr1* knockout studies exist, but I did not verify them.
- **Cell models:** SLC31A1-knockout SH-SY5Y cells; patient fibroblasts.
- **Other models:** *Drosophila* copper-deficiency and *Atp7a* conditional knockout mouse models, in Lane et al. These model copper deficiency, not human SLC31A1 disease specifically. This is a fidelity limitation worth recording.
- **Limitation:** complete loss is embryonic lethal in mice, so human partial-loss variants are hard to model. This is a candidate `HUMAN_MODEL_MISMATCH` discussion, but I have not verified the underlying source.

## Next steps before curation

1. Run `just fetch-reference PMID:35913762` and `PMID:36562171`, then take snippets from the cached abstracts.
2. Find the PMID for the Brain Commun 2025 paper (DOI:10.1093/braincomms/fcaf348) and fetch its full text for onset, seizure types, survival and copper levels.
3. Look up every ontology term named above.
4. Check ClinGen gene-disease validity for SLC31A1, and look for Orphanet and GeneReviews entries.

## Sources

- [KEGG DISEASE H02736](https://www.kegg.jp/entry/H02736), a structured database. It gives the description, OMIM 620306, ICD-11 5C64, PMID:35913762 and PMID:36562171.
- [MedGen C5830385 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/www.ncbi.nlm.nih.gov/medgen/C5830385/index.html), a structured database. It gives MONDO:0957211 and the synonym NSCT.
- [PanelApp Australia, SLC31A1](https://panelapp-aus.org/panels/3469/gene/SLC31A1/), a structured database. It gives the gene OMIM ID and panel listings.
- [Brain Commun 2025 PDF (SGUL repository)](https://openaccess.sgul.ac.uk/id/eprint/117961/1/fcaf348.pdf), primary literature, abstract only.
- [medRxiv preprint of the same cohort](https://www.medrxiv.org/content/10.1101/2024.11.27.24317634.full.pdf), a preprint seen only through search summaries.
- [Lane et al. 2024 preprint, PMC11419079](https://pmc.ncbi.nlm.nih.gov/articles/PMC11419079), a preprint I read directly.
- [Nationwide Children's press release](https://pediatricsnationwide.org/2022/08/15/new-disorder-of-copper-metabolism-identified-caused-by-variants-in-ctr1-gene/), secondary, for the Batzios 2022 discovery.
- [Batzios et al. 2022 (Pure UNIC record)](https://pure.unic.ac.cy/en/publications/newly-identified-disorder-of-copper-metabolism-caused-by-variants/) and the [author PDF](https://pediatricsnationwide.org/wp-content/uploads/2022/09/Batzios-S-Tal-G-DiStasio-AT-et-al.pdf). These are search-listed only. I did not read the full text.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.